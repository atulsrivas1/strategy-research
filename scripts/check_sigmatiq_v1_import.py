"""Document identities and existing-story coverage; no empirical data."""
from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parents[1];lib=root/'docs/sigmatiq-strategy-library-v1'
manifest=json.loads((lib/'MANIFEST.json').read_text(encoding='utf-8'))
assert len(manifest)==14 and len({r['file'] for r in manifest})==14
for r in manifest:
    assert hashlib.sha256((lib/r['file']).read_bytes()).hexdigest()==r['source_sha256']==r['private_sha256']==r['public_sha256']
    assert not r['transformations']
mapping=json.loads((lib/'MAPPING.json').read_text(encoding='utf-8'))
assert len(mapping)==12 and {r['note'] for r in mapping}=={f'{n:02}' for n in range(1,13)}
expected={1:29,2:30,3:31,4:32,5:62,6:35,7:34,8:64,9:40,10:36,11:46,12:44}
for r in mapping:
    assert r['story']==f'SR-{expected[int(r["note"])]:03}'
    assert (lib/r['file']).is_file();s=(root/f'docs/stories/{r["story"]}_PLAN.md').read_text(encoding='utf-8')
    assert f'Release plan: [{r["release"]}]' in s and '../sigmatiq-strategy-library-v1/'+r['file'] in s
assert 'reported prior research' in (lib/'IMPORT_NOTES.md').read_text(encoding='utf-8')
assert 'zero historical comparisons' in (root/'docs/releases/M7_PLAN.md').read_text(encoding='utf-8')
print('14exact source documents;12existing-story mappings;0new stories/trials;Chartsspeak source distinct')
