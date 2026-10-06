"""Validate sanitized planning structure; never loads market data."""
from pathlib import Path
import json, re

ROOT=Path(__file__).resolve().parents[1]
ALLOW_ROOT={'README.md','AGENTS.md','.gitignore'}
ALLOW_DOCS={'WORKFLOW.md','BACKLOG.md','RESEARCH_INDEX.md','ROADMAP.md','DELIVERY_POLICY.md','RESEARCH_BRIEF.md','LEARNINGS.md','CODE_REVIEW.md','PROJECT_KNOWLEDGE.md','DATA_CONTRACT.md','VALIDATION_PLAN.md','SESSION_HANDOFF.md','DASHBOARD.md','STORY_TEMPLATE.md'}
ALLOW_OTHER={'.github/PULL_REQUEST_TEMPLATE.md','.github/workflows/planning.yml','scripts/check_planning.py','docs/sources/SOURCE_MAP.md','docs/sources/AQUA.md','docs/knowledge/BACKLOG_WORKFLOW.md','reports/EQ-001-P1.md'}
allowed=ALLOW_ROOT|{'docs/'+p for p in ALLOW_DOCS}|ALLOW_OTHER|{f'docs/stories/SR-{i:03}_PLAN.md' for i in range(1,22)}|{f'docs/releases/M{i}_PLAN.md' for i in range(5)}
tracked={p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.relative_to(ROOT).parts and '__pycache__' not in p.relative_to(ROOT).parts}
assert tracked==allowed, f'Unexpected/missing publication files: {sorted(tracked^allowed)}'
links=0
for name in sorted(tracked):
    text=(ROOT/name).read_text(encoding='utf-8')
    if name != 'scripts/check_planning.py':
        assert not re.search(r'(?<![A-Za-z])[A-Za-z]:[/\\]|(?:^|\s)/(?:Users|home)/|BEGIN.*PRIVATE KEY|gh[pousr]_[A-Za-z0-9]{20}|api[_-]?key\s*=',text,re.I), f'Publication privacy pattern: {name}'
    if name.endswith('.md'):
        for target in re.findall(r'\]\(([^)]+)\)',text):
            if '://' in target or target.startswith('#'): continue
            assert (ROOT/name).parent.joinpath(target.split('#')[0]).is_file(), f'Broken relative link: {name} -> {target}'
            links+=1
stages=re.findall(r'^\| (Backlog|Ready|In progress|Code review|Test|Ready to release|Released|Done) \|',(ROOT/'docs/WORKFLOW.md').read_text(),re.M)
assert stages==['Backlog','Ready','In progress','Code review','Test','Ready to release','Released','Done']
graph={}
for i in range(1,22):
    sid=f'SR-{i:03}';text=(ROOT/f'docs/stories/{sid}_PLAN.md').read_text(encoding='utf-8')
    assert text.startswith('# '+sid+' — '),sid
    for section in ['Hypothesis and information value','Sources and prior lessons','Dependencies and required data','Baseline and experiment','Acceptance and rejection','Deliverables and resume']:
        assert '## '+section in text,(sid,section)
    assert len(re.findall(r'Release plan: \[M\d\]',text))==1,sid
    assert re.search(r'Parent: \[E\d{2}\]\(https://github.com/atulsrivas1/strategy-research/issues/\d+\)',text),sid
    dep=text.split('## Dependencies and required data',1)[1].split('## Baseline and experiment',1)[0]
    graph[sid]=set(re.findall(r'\[(SR-\d{3})\]',dep))
def visit(sid,path):
    assert sid not in path,'Dependency cycle: '+str(path+[sid])
    for dependency in graph[sid]:
        assert dependency in graph,(sid,dependency)
        visit(dependency,path+[sid])
for sid in graph: visit(sid,[])
plans='\n'.join((ROOT/f'docs/stories/SR-{i:03}_PLAN.md').read_text(encoding='utf-8') for i in range(1,22))
assert set(re.findall(r'B-\d{3}',plans))=={f'B-{i:03}' for i in range(1,13)}
assert all((ROOT/f'docs/releases/M{i}_PLAN.md').is_file() for i in range(5))
assert 'no published' in (ROOT/'docs/ROADMAP.md').read_text().lower() or 'no github release/tag has been published' in (ROOT/'docs/ROADMAP.md').read_text().lower()
print(json.dumps(dict(files=len(tracked),relative_links=links,story_plans=len(graph),backlog_items=12,release_plans=5,dependency_graph='acyclic',privacy='pattern scan passed; human/agent semantic review still required',scope='documentation only; no market data or strategy test'),indent=2))
