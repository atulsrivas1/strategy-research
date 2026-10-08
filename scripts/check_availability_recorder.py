"""Independent synthetic persistence/clock checks; no actual provider capture."""
from pathlib import Path
from contextlib import closing
import sys,sqlite3,json,tempfile,unittest
from concurrent.futures import ThreadPoolExecutor
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'research'))
import availability_recorder as recorder


class CaptureChecks(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name);self.file=self.root/'synthetic.txt';self.file.write_bytes(b'abc')
        self.db=self.root/'observations.sqlite'

    def capture(self):return recorder.observe(self.db,self.file,'synthetic-object')

    def test_known_digest_repeat_revision_and_reversion(self):
        first=self.capture()['payload'];second=self.capture()['payload']
        self.assertEqual(first['sha256'],'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad')
        self.assertEqual(first['bytes'],3)
        self.assertEqual(second['first_seen'],first['first_seen'])
        self.assertIsNone(second['revision_of'])
        self.file.write_bytes(b'changed');third=self.capture()['payload']
        self.assertEqual(third['revision_of'],2)
        self.file.write_bytes(b'abc');fourth=self.capture()['payload']
        self.assertEqual(fourth['revision_of'],3)
        self.assertEqual(fourth['first_seen'],first['first_seen'])
        self.assertEqual(recorder.validate(self.db)['observations'],4)
        self.assertFalse(recorder.validate(self.db)['source_admission'])
        for p in [first,second,third,fourth]:
            self.assertIsNone(p['event_at']);self.assertIsNone(p['provider_published_at'])
            self.assertEqual(p['availability_status'],'observed_local_only')
            self.assertEqual(p['source_qualification'],'unknown')

    def test_missing_and_unstable_file_do_not_append(self):
        self.capture();self.file.unlink()
        with self.assertRaises(FileNotFoundError):self.capture()
        self.assertEqual(recorder.validate(self.db)['observations'],1)
        self.file.write_bytes(b'abc')
        original=Path.open
        count=[0]
        def changed_open(path,*args,**kwargs):
            if path==self.file and args and args[0]=='rb':
                count[0]+=1
                if count[0]==2:path.write_bytes(b'changed')
            return original(path,*args,**kwargs)
        with patch.object(Path,'open',changed_open),self.assertRaises(ValueError):self.capture()
        self.assertEqual(recorder.validate(self.db)['observations'],1)

    def test_interrupted_sql_write_rolls_back(self):
        self.capture()
        with closing(sqlite3.connect(self.db)) as c, c:
            c.execute("CREATE TRIGGER interrupt BEFORE INSERT ON observations BEGIN SELECT RAISE(ABORT,'simulated interrupted write'); END")
        with self.assertRaises(sqlite3.IntegrityError):self.capture()
        self.assertEqual(recorder.validate(self.db)['observations'],1)

    def mutate(self,change,reseal=True,seq=1):
        with closing(sqlite3.connect(self.db)) as c, c:
            body,digest=c.execute('SELECT payload,receipt_sha256 FROM observations WHERE seq=?',(seq,)).fetchone()
            payload=json.loads(body);change(payload)
            c.execute('UPDATE observations SET payload=?,receipt_sha256=? WHERE seq=?',(json.dumps(payload),recorder.seal(payload) if reseal else digest,seq))

    def test_overwritten_first_seen_rejected_even_resealed(self):
        self.capture();second=self.capture()['payload']
        self.mutate(lambda p:p.update(first_seen=second['collection_end']),seq=2)
        with self.assertRaisesRegex(ValueError,'first-seen overwritten'):recorder.validate(self.db)

    def test_wrong_revision_link_rejected_even_resealed(self):
        self.capture();self.file.write_bytes(b'changed');self.capture()
        self.mutate(lambda p:p.update(revision_of=None),seq=2)
        with self.assertRaisesRegex(ValueError,'Revision link'):recorder.validate(self.db)

    def test_falsely_qualified_clock_rejected_even_resealed(self):
        self.capture();self.mutate(lambda p:p.update(availability_status='historically_qualified'))
        with self.assertRaisesRegex(ValueError,'cannot qualify'):recorder.validate(self.db)

    def test_reversed_interval_rejected_even_resealed(self):
        self.capture();self.mutate(lambda p:p.update(collection_start='9999-01-01T00:00:00+00:00'))
        with self.assertRaisesRegex(ValueError,'chronology'):recorder.validate(self.db)

    def test_hash_corruption_rejected(self):
        self.capture();self.mutate(lambda p:p.update(bytes=4),reseal=False)
        with self.assertRaisesRegex(ValueError,'hash/link'):recorder.validate(self.db)

    def test_concurrent_observations_serialized(self):
        with ThreadPoolExecutor(max_workers=4) as pool:
            results=list(pool.map(lambda _:self.capture(),range(4)))
        self.assertEqual(sorted(r['payload']['seq'] for r in results),[1,2,3,4])
        self.assertEqual(len({r['payload']['first_seen'] for r in results}),1)
        self.assertEqual(recorder.validate(self.db)['observations'],4)

    def test_existing_unrelated_database_preserved(self):
        with closing(sqlite3.connect(self.db)) as c, c:c.execute('CREATE TABLE unrelated(value TEXT)')
        with self.assertRaisesRegex(ValueError,'existing database'):self.capture()
        with closing(sqlite3.connect(self.db)) as c:
            self.assertEqual(c.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall(),[('unrelated',)])

    def test_backdated_local_clock_fails_without_append(self):
        first=self.capture()['payload']
        with patch.object(recorder,'utc_now',return_value='2000-01-01T00:00:00+00:00'),self.assertRaisesRegex(ValueError,'chronology'):self.capture()
        self.assertEqual(recorder.validate(self.db)['observations'],1)
        self.assertEqual(recorder.instant(first['first_seen']).utcoffset().total_seconds(),0)


if __name__=='__main__':unittest.main()
