"""Validate sanitized planning structure; never loads market data."""
from pathlib import Path
import json, re

ROOT=Path(__file__).resolve().parents[1]
ALLOW_ROOT={'README.md','AGENTS.md','.gitignore'}
ALLOW_DOCS={'WORKFLOW.md','BACKLOG.md','RESEARCH_INDEX.md','ROADMAP.md','DELIVERY_POLICY.md','RESEARCH_BRIEF.md','LEARNINGS.md','CODE_REVIEW.md','PROJECT_KNOWLEDGE.md','DATA_CONTRACT.md','VALIDATION_PLAN.md','SESSION_HANDOFF.md','DASHBOARD.md','STORY_TEMPLATE.md'}
ALLOW_OTHER={'docs/knowledge/BACKLOG_WORKFLOW.md', 'reports/SR-002-input-audit.md', 'docs/sources/SOURCE_MAP.md', 'reports/M0-qualification.md', 'fixtures/reference_machinery.py', 'docs/sources/AQUA.md', 'scripts/check_planning.py', 'reports/EQ-001-P1.md', 'scripts/check_reference_fixtures.py', '.github/PULL_REQUEST_TEMPLATE.md', 'docs/releases/M0_RECEIPT.md', '.github/workflows/planning.yml', 'fixtures/chronology.py', 'scripts/check_chronology.py', 'reports/M0-post-merge-review.md'}
STORY_IDS=list(range(1,26))+list(range(28,56))
RELEASE_IDS=[0,1,2,3,4,6]
allowed=ALLOW_ROOT|{'docs/'+p for p in ALLOW_DOCS}|ALLOW_OTHER|{f'docs/stories/SR-{i:03}_PLAN.md' for i in STORY_IDS}|{f'docs/releases/M{i}_PLAN.md' for i in RELEASE_IDS}|{'docs/releases/M0_HANDOFF.md'}
allowed|={'docs/knowledge/SCANNER_CONTEXT_PROTOCOL.md'}
allowed|={'reports/M1-development.md','reports/M1-methodology.md','reports/M1-feasibility.md','docs/sources/M1_REVERSAL.md','docs/sources/M1_AUXILIARY.md','fixtures/m1_math.py','scripts/check_m1.py'}
allowed|={'reports/M2-readiness.md','fixtures/m2_foundation.py','scripts/check_m2.py','scripts/verify_m2.py'}
allowed|={'fixtures/m2_sleeves.py','scripts/check_m2_sleeves.py','reports/M2-context-proxy.md','reports/M2-veto-diagnosis.md','docs/knowledge/EVENT_CONTINUATION_DESIGN.md','docs/sources/EVENT_CONTINUATION.md'}
allowed|={'docs/strategy-library/B-short-term/B1-rsi2-short-term-reversal.md', 'docs/strategy-library/D-medium-term/D2-cross-sectional-momentum.md', 'docs/releases/M6_HANDOFF.md', 'docs/strategy-library/C-vol-and-flow/C3-dealer-gamma-exposure-opex-flows.md', 'docs/strategy-library/D-medium-term/D1-trend-following-turtles-cta.md', 'scripts/check_library_import.py', 'docs/strategy-library/A-intraday/A2-opening-range-breakout-intraday-momentum.md', 'docs/strategy-library/C-vol-and-flow/C1-variance-risk-premium-harvesting.md', 'docs/strategy-library/C-vol-and-flow/C2-dispersion-correlation-trading.md', 'docs/strategy-library/D-medium-term/D3-carry-fx-futures.md', 'docs/strategy-library/MANIFEST.json', 'docs/strategy-library/E-long-term/E4-canslim-minervini-growth-breakout.md', 'docs/strategy-library/CATALOG.md', 'docs/strategy-library/B-short-term/B3-post-earnings-announcement-drift.md', 'docs/strategy-library/E-long-term/E1-value-plus-quality.md', 'docs/strategy-library/A-intraday/A3-vwap-anchored-vwap-reversion.md', 'docs/strategy-library/E-long-term/E3-risk-parity-all-weather.md', 'docs/strategy-library/INDEX.md', 'docs/strategy-library/IMPORT_NOTES.md', 'docs/strategy-library/A-intraday/A1-inventory-skew-market-making.md', 'docs/strategy-library/E-long-term/E2-low-volatility-betting-against-beta.md', 'docs/strategy-library/D-medium-term/D4-seasonality-fomc-turn-of-month.md', 'docs/strategy-library/C-vol-and-flow/C4-crypto-funding-basis-carry.md', 'docs/strategy-library/B-short-term/B4-pairs-trading-statistical-arbitrage.md', 'docs/strategy-library/B-short-term/B2-overnight-drift-gap-fade.md', 'docs/strategy-library/A-intraday/A4-volume-profile-order-flow-auction.md'}
allowed|={'docs/strategy-library-v3/08-invest-graham-ncav.md', 'docs/strategy-library-v3/04-swing-opportunistic-insiders.md', 'docs/strategy-library-v3/IMPORT_NOTES.md', '.gitattributes', 'docs/strategy-library-v3/SOURCES.md', 'docs/strategy-library-v3/02-intraday-last-half-hour.md', 'docs/strategy-library-v3/MANIFEST.json', 'docs/strategy-library-v3/01-close-moc-imbalance.md', 'docs/strategy-library-v3/07-portfolio-commodity-basis.md', 'docs/strategy-library-v3/03-intraday-williams-oops.md', 'docs/strategy-library-v3/INDEX.md', 'docs/strategy-library-v3/CATALOG.md', 'docs/strategy-library-v3/05-position-merger-arbitrage.md', 'docs/strategy-library-v3/ROSTER.md', 'docs/strategy-library-v3/README.md', 'docs/strategy-library-v3/SESSION_HANDOFF.md', 'docs/strategy-library-v3/06-position-spinoff-drift.md', 'scripts/check_library_v3_import.py'}
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
stages=re.findall(r'^\| (Backlog|Ready|In progress|Code review|Test|Ready to release|Released|Done) \|',(ROOT/'docs/WORKFLOW.md').read_text(encoding='utf-8'),re.M)
assert stages==['Backlog','Ready','In progress','Code review','Test','Ready to release','Released','Done']
graph={}
for i in STORY_IDS:
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
plans='\n'.join((ROOT/f'docs/stories/SR-{i:03}_PLAN.md').read_text(encoding='utf-8') for i in STORY_IDS)
assert set(re.findall(r'B-\d{3}',plans))=={f'B-{i:03}' for i in range(1,13)}
assert all((ROOT/f'docs/releases/M{i}_PLAN.md').is_file() for i in RELEASE_IDS)
assert 'planned, unreleased' in (ROOT/'docs/releases/M6_PLAN.md').read_text(encoding='utf-8')
print(json.dumps(dict(files=len(tracked),relative_links=links,story_plans=len(graph),backlog_items=12,release_plans=len(RELEASE_IDS),dependency_graph='acyclic',privacy='pattern scan passed; human/agent semantic review still required',scope='sanitized documentation and synthetic fixtures; no market data or strategy test'),indent=2))
