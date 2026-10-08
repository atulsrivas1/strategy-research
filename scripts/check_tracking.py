"""Cross-check current story, epic and release declarations; never loads market data.

Optional --snapshot verifies native GitHub links against a locally captured API inventory.
CI checks the versioned planning relationships without a network credential.
"""
from pathlib import Path
import argparse,json,re

ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('--snapshot',type=Path)
args=parser.parse_args()
stories={}
for path in sorted((ROOT/'docs/stories').glob('SR-*_PLAN.md')):
    text=path.read_text(encoding='utf-8')
    sid=path.stem.removesuffix('_PLAN')
    parent=re.search(r'Parent: \[(E\d{2})\]\(https://github.com/atulsrivas1/strategy-research/issues/(\d+)\)',text)
    release=re.search(r'Release plan: \[(M\d)\]',text)
    assert parent and release,sid
    current=text.split('## Current delivery reconciliation — October 7, 2026',1)[1].split('## Preserved plan and amendments',1)[0]
    assert 'Separate research PR review is optional' in current,sid
    stories[sid]={'epic':parent[1],'parent':int(parent[2]),'release':release[1]}
assert len(stories)==68
for n in range(28,68):
    sid=f'SR-{n:03}'
    text=(ROOT/f'docs/stories/{sid}_PLAN.md').read_text(encoding='utf-8')
    dependencies=text.split('## Dependencies and required data',1)[1].split('## Baseline and experiment',1)[0]
    assert '[SR-068](https://github.com/atulsrivas1/strategy-research/issues/91)' in dependencies,(sid,'missing design prerequisite')
assert stories['SR-068']['epic']=='E08' and stories['SR-068']['release']=='M6'
plan=json.loads((ROOT/'docs/RESEARCH_PLAN.json').read_text(encoding='utf-8'))
inventory={row['story']:row for row in plan['stories']}
assert len(plan['stories'])==len(inventory)==68 and set(inventory)==set(stories)
for sid,row in inventory.items():
    assert row['epic']==stories[sid]['epic'] and row['release']==stories[sid]['release'],(sid,'priority inventory assignment drift')
    text=(ROOT/f'docs/stories/{sid}_PLAN.md').read_text(encoding='utf-8')
    deps=text.split('## Dependencies and required data',1)[1].split('## Baseline and experiment',1)[0]
    assert set(row['dependencies'])==set(re.findall(r'\[(SR-\d{3})\]',deps)),(sid,'priority dependency drift')
    assert row['priority'] in text.split('## Current delivery reconciliation',1)[0]
assert {sid for sid,row in inventory.items() if row['release']=='M6'}=={'SR-068'}
assert {sid for sid,row in inventory.items() if row['release']=='M7'}=={f'SR-{n:03}' for n in (32,33,34,40,41,43,47,51,62,63)}
for release in sorted({s['release'] for s in stories.values()}):
    text=(ROOT/f'docs/releases/{release}_PLAN.md').read_text(encoding='utf-8')
    current=text.split('## Current assigned stories',1)[1].split('\n## ',1)[0]
    declared=re.findall(r'\[(SR-\d{3})\]',current)
    expected={sid for sid,s in stories.items() if s['release']==release}
    assert len(declared)==len(set(declared)) and set(declared)==expected,(release,'story assignment drift')
roadmap=(ROOT/'docs/ROADMAP.md').read_text(encoding='utf-8').split('## Preserved roadmap history',1)[0]
epics={}
for line in roadmap.splitlines():
    match=re.match(r'\| \[(E\d{2})\]',line)
    if match:
        assert match[1] not in epics,'duplicate epic row'
        epics[match[1]]=set(re.findall(r'\[(SR-\d{3})\]',line))
assert set(epics)=={s['epic'] for s in stories.values()}
for epic,declared in epics.items():
    assert declared=={sid for sid,s in stories.items() if s['epic']==epic},(epic,'roadmap membership drift')
assert len(epics)==8 and len(epics['E08'])==41
assert epics['E08']-{f'SR-{n:03}' for n in range(28,68)}=={'SR-068'}
workflow=(ROOT/'docs/WORKFLOW.md').read_text(encoding='utf-8')
review_row=next(line for line in workflow.splitlines() if line.startswith('| Code review |'))
assert 'optional under owner waiver' in review_row and 'required before merge' not in review_row
for sid in ('SR-023','SR-024'):
    current=(ROOT/f'docs/stories/{sid}_PLAN.md').read_text(encoding='utf-8').split('## Preserved plan and amendments',1)[0]
    assert 'comparison completed' in current and 'Budget exhausted' in current and 'full story open' in current
native_checks=0
if args.snapshot:
    snapshot=json.loads(args.snapshot.read_text(encoding='utf-8'))
    issues={re.match(r'\[(SR-\d{3})\]',i['title'])[1]:i for i in snapshot['issues'] if re.match(r'\[SR-\d{3}\]',i['title'])}
    assert set(issues)==set(stories)
    for sid,s in stories.items():
        issue=issues[sid]
        children=snapshot['epic_children'][str(s['parent'])]
        assert issue['number'] in {c['number'] for c in children},(sid,'native parent drift')
        assert issue['milestone']['number']==int(s['release'][1:])+1,(sid,'live milestone drift')
        assert issue['number']==inventory[sid]['issue'] and issue['title']==inventory[sid]['title'],(sid,'inventory identity drift')
        native_checks+=1
print(json.dumps({'stories':len(stories),'epics':len(epics),'release_assignments':'matched','native_story_checks':native_checks,'scope':'documentation relationships only; no market replay'}))
