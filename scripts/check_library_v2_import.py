"""Verify documentary identity and overlap coverage; no data readers."""
from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parents[1];lib=root/'docs/strategy-library-v2'
manifest=json.loads((lib/'MANIFEST.json').read_text(encoding='utf-8'));assert len(manifest)==39
assert len({r['file'] for r in manifest})==39
for r in manifest:
    assert hashlib.sha256((lib/r['file']).read_bytes()).hexdigest()==r['public_sha256']
    assert r['source_sha256']==r['private_sha256']
    if r['file']=='README.md':assert len(r['transformations'])==1
    else:assert r['source_sha256']==r['public_sha256'] and not r['transformations']
mapping=json.loads((lib/'MAPPING.json').read_text(encoding='utf-8'))
assert len(mapping)==36 and {r['note'] for r in mapping}=={f'{n:02}' for n in range(1,37)}
new=[r for r in mapping if r['kind'].startswith('Distinct')];old=[r for r in mapping if r['kind'].startswith('Existing')]
assert len(new)==12 and len(old)==24 and len({r['story'] for r in new})==12
assert {r['story'] for r in new}=={f'SR-{n:03}' for n in range(56,68)}
for r in mapping:
    assert (lib/r['file']).is_file();s=(root/f'docs/stories/{r["story"]}_PLAN.md').read_text(encoding='utf-8')
    assert f'Release plan: [{r["release"]}]' in s
assert len([r for r in new if r['release']=='M7'])==2
assert 'reported prior research' in (lib/'IMPORT_NOTES.md').read_text(encoding='utf-8')
assert 'zero historical comparisons' in (root/'docs/releases/M7_PLAN.md').read_text(encoding='utf-8')
print('39documents /36notes:24existing family mappings+12new questions;2M7/10M4;no strategy replay')
