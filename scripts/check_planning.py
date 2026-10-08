"""Validate sanitized planning structure; never loads market data."""
from pathlib import Path
import json, re

ROOT=Path(__file__).resolve().parents[1]
ALLOW_ROOT={'README.md','AGENTS.md','.gitignore'}
ALLOW_DOCS={'WORKFLOW.md','BACKLOG.md','RESEARCH_INDEX.md','ROADMAP.md','DELIVERY_POLICY.md','RESEARCH_BRIEF.md','LEARNINGS.md','CODE_REVIEW.md','PROJECT_KNOWLEDGE.md','DATA_CONTRACT.md','VALIDATION_PLAN.md','SESSION_HANDOFF.md','DASHBOARD.md','STORY_TEMPLATE.md'}
ALLOW_OTHER={'docs/knowledge/BACKLOG_WORKFLOW.md', 'reports/SR-002-input-audit.md', 'docs/sources/SOURCE_MAP.md', 'reports/M0-qualification.md', 'fixtures/reference_machinery.py', 'docs/sources/AQUA.md', 'scripts/check_planning.py', 'reports/EQ-001-P1.md', 'scripts/check_reference_fixtures.py', '.github/PULL_REQUEST_TEMPLATE.md', 'docs/releases/M0_RECEIPT.md', '.github/workflows/planning.yml', 'fixtures/chronology.py', 'scripts/check_chronology.py', 'reports/M0-post-merge-review.md'}
STORY_IDS=list(range(1,69))
RELEASE_IDS=list(range(8))
allowed=ALLOW_ROOT|{'docs/'+p for p in ALLOW_DOCS}|ALLOW_OTHER|{f'docs/stories/SR-{i:03}_PLAN.md' for i in STORY_IDS}|{f'docs/releases/M{i}_PLAN.md' for i in RELEASE_IDS}|{'docs/releases/M0_HANDOFF.md'}
allowed|={'docs/knowledge/SCANNER_CONTEXT_PROTOCOL.md'}
allowed|={'scripts/check_tracking.py','reports/TRACKING-SYNC.md'}
allowed|={'reports/DETAILED-REVIEW.md','docs/REPLAN.md','docs/RESEARCH_PLAN.json','docs/releases/M7_HANDOFF.md'}
allowed|={'docs/design/DESIGN.md','docs/design/APPLICABILITY.md','docs/design/APPLICABILITY.json','docs/design/REQUIREMENTS.json','docs/design/BUILD_REGISTER.md','docs/design/TEMPLATES.md','docs/design/WALKTHROUGHS.md','scripts/check_design.py'}
allowed|={'docs/releases/M6_RECEIPT.md'}
allowed|={'fixtures/d1_inputs.py','scripts/check_d1_inputs.py','reports/D1-input-qualification.md'}
allowed|={'fixtures/daily_inputs.py','scripts/check_daily_inputs.py','reports/D1-daily-inputs.md'}
allowed|={'fixtures/session_proxy.py','scripts/check_session_proxy.py','reports/D1-session-feasibility.md'}
allowed|={'fixtures/relative_strength.py','scripts/check_relative_strength.py','reports/D2-source-qualification.md'}
allowed|={'fixtures/fundamental_vintages.py','scripts/check_fundamental_vintages.py','reports/E4-vintage-qualification.md'}
allowed|={'fixtures/earnings_surprise.py','scripts/check_earnings_surprise.py','reports/B3-source-qualification.md'}
allowed|={'fixtures/rsi2.py','scripts/check_rsi2.py','reports/B1-source-qualification.md'}
allowed|={'fixtures/opening_gap.py','scripts/check_opening_gap.py','reports/B2-source-qualification.md'}
allowed|={'fixtures/scheduled_event.py','scripts/check_scheduled_event.py','reports/D4-source-qualification.md'}
allowed|={'fixtures/filing_purchase.py','scripts/check_filing_purchase.py','reports/V3-04-source-qualification.md'}
allowed|={'fixtures/window_volume.py','scripts/check_window_volume.py','reports/V2-14-source-qualification.md'}
allowed|={'fixtures/flag_endpoints.py','scripts/check_flag_endpoints.py','reports/V2-18-source-qualification.md'}
allowed|={'reports/M7-readiness-ledger.md'}
allowed|={'fixtures/source_admission.py','scripts/check_source_admission.py','reports/D1-source-admission.md'}
allowed|={'reports/D1-lineage-location.md'}
allowed|={'reports/D1-preparation-provenance.md'}
allowed|={'reports/D1-recovery-disposition.md','docs/contracts/SR-022_AVAILABILITY_CAPTURE.md'}
allowed|={'reports/M1-development.md','reports/M1-methodology.md','reports/M1-feasibility.md','docs/sources/M1_REVERSAL.md','docs/sources/M1_AUXILIARY.md','fixtures/m1_math.py','scripts/check_m1.py'}
allowed|={'reports/M2-readiness.md','fixtures/m2_foundation.py','scripts/check_m2.py','scripts/verify_m2.py'}
allowed|={'fixtures/m2_sleeves.py','scripts/check_m2_sleeves.py','reports/M2-context-proxy.md','reports/M2-veto-diagnosis.md','docs/knowledge/EVENT_CONTINUATION_DESIGN.md','docs/sources/EVENT_CONTINUATION.md'}
allowed|={'docs/strategy-library/B-short-term/B1-rsi2-short-term-reversal.md', 'docs/strategy-library/D-medium-term/D2-cross-sectional-momentum.md', 'docs/releases/M6_HANDOFF.md', 'docs/strategy-library/C-vol-and-flow/C3-dealer-gamma-exposure-opex-flows.md', 'docs/strategy-library/D-medium-term/D1-trend-following-turtles-cta.md', 'scripts/check_library_import.py', 'docs/strategy-library/A-intraday/A2-opening-range-breakout-intraday-momentum.md', 'docs/strategy-library/C-vol-and-flow/C1-variance-risk-premium-harvesting.md', 'docs/strategy-library/C-vol-and-flow/C2-dispersion-correlation-trading.md', 'docs/strategy-library/D-medium-term/D3-carry-fx-futures.md', 'docs/strategy-library/MANIFEST.json', 'docs/strategy-library/E-long-term/E4-canslim-minervini-growth-breakout.md', 'docs/strategy-library/CATALOG.md', 'docs/strategy-library/B-short-term/B3-post-earnings-announcement-drift.md', 'docs/strategy-library/E-long-term/E1-value-plus-quality.md', 'docs/strategy-library/A-intraday/A3-vwap-anchored-vwap-reversion.md', 'docs/strategy-library/E-long-term/E3-risk-parity-all-weather.md', 'docs/strategy-library/INDEX.md', 'docs/strategy-library/IMPORT_NOTES.md', 'docs/strategy-library/A-intraday/A1-inventory-skew-market-making.md', 'docs/strategy-library/E-long-term/E2-low-volatility-betting-against-beta.md', 'docs/strategy-library/D-medium-term/D4-seasonality-fomc-turn-of-month.md', 'docs/strategy-library/C-vol-and-flow/C4-crypto-funding-basis-carry.md', 'docs/strategy-library/B-short-term/B4-pairs-trading-statistical-arbitrage.md', 'docs/strategy-library/B-short-term/B2-overnight-drift-gap-fade.md', 'docs/strategy-library/A-intraday/A4-volume-profile-order-flow-auction.md'}
allowed|={'docs/strategy-library-v3/08-invest-graham-ncav.md', 'docs/strategy-library-v3/04-swing-opportunistic-insiders.md', 'docs/strategy-library-v3/IMPORT_NOTES.md', '.gitattributes', 'docs/strategy-library-v3/SOURCES.md', 'docs/strategy-library-v3/02-intraday-last-half-hour.md', 'docs/strategy-library-v3/MANIFEST.json', 'docs/strategy-library-v3/01-close-moc-imbalance.md', 'docs/strategy-library-v3/07-portfolio-commodity-basis.md', 'docs/strategy-library-v3/03-intraday-williams-oops.md', 'docs/strategy-library-v3/INDEX.md', 'docs/strategy-library-v3/CATALOG.md', 'docs/strategy-library-v3/05-position-merger-arbitrage.md', 'docs/strategy-library-v3/ROSTER.md', 'docs/strategy-library-v3/README.md', 'docs/strategy-library-v3/SESSION_HANDOFF.md', 'docs/strategy-library-v3/06-position-spinoff-drift.md', 'scripts/check_library_v3_import.py'}
allowed|={'docs/strategy-library-v2/25-portfolio-dalio-allweather.md', 'docs/strategy-library-v2/34-invest-piotroski-fscore.md', 'docs/strategy-library-v2/35-invest-terry-smith-quality.md', 'docs/strategy-library-v2/02-ultra-latency-cross-venue-arb.md', 'docs/strategy-library-v2/IMPORT_NOTES.md', 'docs/strategy-library-v2/12-intraday-wyckoff-orderflow.md', 'docs/strategy-library-v2/29-portfolio-multifactor-ensemble.md', 'docs/strategy-library-v2/27-portfolio-managed-futures-cta.md', 'docs/strategy-library-v2/20-position-turtle-trend.md', 'docs/strategy-library-v2/21-position-oneil-canslim.md', 'docs/strategy-library-v2/18-swing-bonde-high-tight-flag.md', 'docs/strategy-library-v2/14-swing-qullamaggie-episodic-pivots.md', 'scripts/check_library_v2_import.py', 'docs/strategy-library-v2/03-ultra-tape-reading-scalping.md', 'docs/strategy-library-v2/16-swing-overnight-gap-momentum.md', 'docs/strategy-library-v2/13-swing-connors-rsi2.md', 'docs/strategy-library-v2/17-swing-darvas-box.md', 'docs/strategy-library-v2/32-invest-lynch-garp.md', 'docs/strategy-library-v2/_TEMPLATE.md', 'docs/strategy-library-v2/05-ultra-opening-drive-scalping.md', 'docs/strategy-library-v2/30-portfolio-tail-hedge-universa.md', 'docs/strategy-library-v2/09-intraday-vwap-reversion.md', 'docs/strategy-library-v2/15-swing-pairs-stat-arb.md', 'docs/strategy-library-v2/04-ultra-inventory-skew-avellaneda-stoikov.md', 'docs/strategy-library-v2/23-position-dual-momentum.md', 'docs/strategy-library-v2/22-position-minervini-sepa.md', 'docs/strategy-library-v2/CATALOG.md', 'docs/strategy-library-v2/10-intraday-aziz-bull-flag.md', 'docs/strategy-library-v2/ROSTER.md', 'docs/strategy-library-v2/33-invest-greenblatt-magic-formula.md', 'docs/strategy-library-v2/README.md', 'docs/strategy-library-v2/MAPPING.json', 'docs/strategy-library-v2/11-intraday-raschke-taylor-cycle.md', 'docs/strategy-library-v2/19-position-livermore-trend.md', 'docs/strategy-library-v2/26-portfolio-vrp-put-writing.md', 'docs/strategy-library-v2/24-position-pead-drift.md', 'docs/strategy-library-v2/36-invest-permanent-index-tilt.md', 'docs/strategy-library-v2/06-ultra-liquidity-sweep-fade.md', 'docs/strategy-library-v2/08-intraday-fisher-acd.md', 'docs/strategy-library-v2/01-ultra-queue-imbalance-market-making.md', 'docs/strategy-library-v2/07-intraday-crabel-orb.md', 'docs/strategy-library-v2/31-invest-buffett-value.md', 'docs/strategy-library-v2/MANIFEST.json', 'docs/strategy-library-v2/28-portfolio-fx-carry.md'}
allowed|={'docs/sigmatiq-strategy-library-v1/02-intraday-vwap-mean-reversion.md', 'docs/sigmatiq-strategy-library-v1/MANIFEST.json', 'docs/sigmatiq-strategy-library-v1/MAPPING.json', 'docs/sigmatiq-strategy-library-v1/10-portfolio-volatility-risk-premium.md', 'scripts/check_sigmatiq_v1_import.py', 'docs/sigmatiq-strategy-library-v1/11-portfolio-risk-parity.md', 'docs/sigmatiq-strategy-library-v1/_TEMPLATE.md', 'docs/sigmatiq-strategy-library-v1/09-position-turtle-trend-following.md', 'docs/sigmatiq-strategy-library-v1/IMPORT_NOTES.md', 'docs/sigmatiq-strategy-library-v1/04-swing-rsi2-mean-reversion.md', 'docs/sigmatiq-strategy-library-v1/01-intraday-opening-range-breakout.md', 'docs/sigmatiq-strategy-library-v1/06-swing-pairs-statistical-arbitrage.md', 'docs/sigmatiq-strategy-library-v1/12-portfolio-multifactor-ensemble.md', 'docs/sigmatiq-strategy-library-v1/03-intraday-order-flow-imbalance.md', 'docs/sigmatiq-strategy-library-v1/CATALOG.md', 'docs/sigmatiq-strategy-library-v1/07-position-post-earnings-drift.md', 'docs/sigmatiq-strategy-library-v1/README.md', 'docs/sigmatiq-strategy-library-v1/08-position-dual-momentum.md', 'docs/sigmatiq-strategy-library-v1/05-swing-episodic-pivots.md'}
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
