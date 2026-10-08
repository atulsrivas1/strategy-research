"""Offline local observations. Integrity and local time are not source admission."""
import argparse
from contextlib import closing
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sqlite3

SCHEMA = 'research-local-observations-v1'
FIELDS = {'schema', 'seq', 'source_id', 'sha256', 'bytes', 'collection_start',
          'collection_end', 'first_seen', 'previous_sha256', 'revision_of',
          'clock_basis', 'source_qualification', 'availability_status',
          'event_at', 'provider_published_at'}


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def instant(value):
    result = datetime.fromisoformat(value)
    if result.tzinfo is None or result.utcoffset().total_seconds() != 0:
        raise ValueError('UTC observation time required')
    return result


def seal(payload):
    return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def read_records(connection):
    tables = {r[0] for r in connection.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")}
    if not tables:
        return []
    if tables != {'metadata', 'observations'}:
        raise ValueError('Not a recorder ledger; existing database left unchanged')
    metadata = dict(connection.execute('SELECT key,value FROM metadata'))
    if metadata != {'schema': SCHEMA}:
        raise ValueError('Unsupported ledger schema')
    return [(seq, json.loads(body), digest) for seq, body, digest in connection.execute('SELECT seq,payload,receipt_sha256 FROM observations ORDER BY seq')]


def verify_records(records):
    prior_hash = None
    latest = {}
    first_seen = {}
    prior_end = None
    for expected_seq, (seq, p, digest) in enumerate(records, 1):
        if set(p) != FIELDS or p['schema'] != SCHEMA or seq != expected_seq or type(p['seq']) is not int or p['seq'] != seq:
            raise ValueError('Receipt sequence/schema mismatch')
        if seal(p) != digest or p['previous_sha256'] != prior_hash:
            raise ValueError('Receipt hash/link mismatch')
        if not isinstance(p['source_id'], str) or not p['source_id'].strip():
            raise ValueError('Missing logical source identity')
        if not isinstance(p['sha256'], str) or len(p['sha256']) != 64 or any(c not in '0123456789abcdef' for c in p['sha256']):
            raise ValueError('Invalid byte digest')
        if type(p['bytes']) is not int or not 0 <= p['bytes'] <= 16*1024*1024:
            raise ValueError('Invalid byte count')
        start, end, first = map(instant, (p['collection_start'], p['collection_end'], p['first_seen']))
        if start > end or first > end or (prior_end is not None and start < prior_end):
            raise ValueError('Observation chronology mismatch')
        if (p['clock_basis'], p['source_qualification'], p['availability_status'], p['event_at'], p['provider_published_at']) != ('local_recorder_utc', 'unknown', 'observed_local_only', None, None):
            raise ValueError('v1 cannot qualify source/provider/historical clocks')
        key = (p['source_id'], p['sha256'])
        if key not in first_seen:
            if first != end:
                raise ValueError('New version first-seen must be collection completion')
            first_seen[key] = p['first_seen']
        if p['first_seen'] != first_seen[key]:
            raise ValueError('Version first-seen overwritten')
        previous = latest.get(p['source_id'])
        revision = previous['seq'] if previous and previous['sha256'] != p['sha256'] else None
        if p['revision_of'] != revision:
            raise ValueError('Revision link mismatch')
        latest[p['source_id']] = p
        prior_hash, prior_end = digest, end
    return first_seen, latest


def stable_bytes(source):
    path = Path(source)
    before = path.stat()
    if not path.is_file() or before.st_size > 16*1024*1024:
        raise ValueError('Regular file within 16MiB required')
    with path.open('rb') as f:
        body = f.read(16*1024*1024+1)
    after = path.stat()
    signature = lambda s: (s.st_dev, s.st_ino, s.st_size, s.st_mtime_ns, s.st_ctime_ns)
    if signature(before) != signature(after) or len(body) != before.st_size:
        raise ValueError('Source changed during collection')
    digest = hashlib.sha256(body).hexdigest()
    with path.open('rb') as f:
        repeated = f.read(16*1024*1024+1)
    if hashlib.sha256(repeated).hexdigest() != digest or signature(path.stat()) != signature(after):
        raise ValueError('Source unstable during verification')
    return digest, len(body)


def observe(database, source, source_id):
    if not isinstance(source_id, str) or not source_id.strip():
        raise ValueError('Logical source identity required')
    if Path(database).resolve() == Path(source).resolve():
        raise ValueError('Ledger and input must be separate files')
    with closing(sqlite3.connect(database, timeout=15)) as c, c:
        c.execute('BEGIN IMMEDIATE')
        records = read_records(c)
        first_seen, latest = verify_records(records)
        start = utc_now()
        digest, size = stable_bytes(source)
        end = utc_now()
        seq = len(records)+1
        previous = latest.get(source_id)
        p = dict(schema=SCHEMA, seq=seq, source_id=source_id, sha256=digest, bytes=size,
                 collection_start=start, collection_end=end,
                 first_seen=first_seen.get((source_id, digest), end),
                 previous_sha256=records[-1][2] if records else None,
                 revision_of=previous['seq'] if previous and previous['sha256'] != digest else None,
                 clock_basis='local_recorder_utc', source_qualification='unknown',
                 availability_status='observed_local_only', event_at=None, provider_published_at=None)
        receipt_hash = seal(p)
        verify_records(records+[(seq,p,receipt_hash)])
        if not records and not list(c.execute("SELECT name FROM sqlite_master WHERE name='metadata'")):
            c.execute('CREATE TABLE metadata(key TEXT PRIMARY KEY,value TEXT NOT NULL)')
            c.execute('INSERT INTO metadata VALUES(?,?)', ('schema',SCHEMA))
            c.execute('CREATE TABLE observations(seq INTEGER PRIMARY KEY,payload TEXT NOT NULL,receipt_sha256 TEXT NOT NULL)')
        c.execute('INSERT INTO observations VALUES(?,?,?)', (seq,json.dumps(p,sort_keys=True),receipt_hash))
        c.commit()
        return dict(payload=p, receipt_sha256=receipt_hash)


def validate(database):
    # Read-only URI prevents creating or changing a ledger while validating.
    with closing(sqlite3.connect(Path(database).resolve().as_uri()+'?mode=ro', uri=True)) as c:
        records=read_records(c)
        if not records:
            raise ValueError('No completed observations')
        verify_records(records)
        return dict(observations=len(records), schema=SCHEMA, source_admission=False)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    commands=parser.add_subparsers(dest='command',required=True)
    capture=commands.add_parser('observe')
    capture.add_argument('--ledger',required=True)
    capture.add_argument('--file',required=True)
    capture.add_argument('--source-id',required=True)
    check=commands.add_parser('validate');check.add_argument('--ledger',required=True)
    args=parser.parse_args()
    result=observe(args.ledger,args.file,args.source_id) if args.command=='observe' else validate(args.ledger)
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
