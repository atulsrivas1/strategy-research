"""Documentation witnesses; no market data or empirical results."""
from pathlib import Path
import hashlib,json,re
root=Path(__file__).resolve().parents[1];lib=root/'docs/strategy-library-v3'
rows=json.loads((lib/'MANIFEST.json').read_text(encoding='utf-8'));assert len(rows)==13
assert len({r['file'] for r in rows})==13
for r in rows:
    b=(lib/r['file']).read_bytes();assert hashlib.sha256(b).hexdigest()==r['public_sha256']
    assert r['source_sha256']==r['private_sha256']
    if r['file']=='README.md':assert len(r['transformations'])==1
    else:assert r['source_sha256']==r['public_sha256'] and not r['transformations']
codes=set()
for i in range(48,56):
    s=(root/f'docs/stories/SR-{i:03}_PLAN.md').read_text(encoding='utf-8')
    code=re.search(r'Qualify V3-(\d\d):',s)[1];assert code not in codes;codes.add(code)
    assert f'Release plan: [M{7 if code=="04" else 4}]' in s
assert codes=={f'{i:02}' for i in range(1,9)}
assert 'reported prior research' in (lib/'IMPORT_NOTES.md').read_text(encoding='utf-8')
assert 'zero historical comparisons' in (root/'docs/releases/M7_PLAN.md').read_text(encoding='utf-8')
print('13 source documents; 8 unique stories; 1 M7 / 7 M4; imported holdouts are not qualified')
