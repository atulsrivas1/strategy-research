"""Verify imported documentation only; no market data or backtests."""
from pathlib import Path
import hashlib,json,re
root=Path(__file__).resolve().parents[1]
library=root/'docs/strategy-library'
manifest=json.loads((library/'MANIFEST.json').read_text(encoding='utf-8'))
assert len(manifest)==21 and len({r['file'] for r in manifest})==21
for row in manifest:
    b=(library/row['file']).read_bytes()
    assert hashlib.sha256(b).hexdigest()==row['source_sha256']==row['public_sha256']==row['private_sha256']
    assert row['transformations']==[]
codes=set()
for i in range(28,48):
    s=(root/f'docs/stories/SR-{i:03}_PLAN.md').read_text(encoding='utf-8')
    code=re.search(r'Qualify ([A-E][1-4]):',s)[1];assert code not in codes;codes.add(code)
    release=re.search(r'Release plan: \[(M[47])\]',s)[1]
    assert release==('M7' if code in {'B1','B2','B3','D1','D2','D4','E4'} else 'M4')
assert codes=={f'{group}{n}' for group in 'ABCDE' for n in range(1,5)}
assert 'reported prior research' in (library/'IMPORT_NOTES.md').read_text(encoding='utf-8')
assert 'zero historical comparisons' in (root/'docs/releases/M7_PLAN.md').read_text(encoding='utf-8')
print('21 imported document hashes; 20 unique dossiers/stories; 7 M7 / 13 M4 assignments; no market reads')
