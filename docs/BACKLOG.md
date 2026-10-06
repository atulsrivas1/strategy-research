# Ranked research scope

US individual stocks, long shares first and bought calls later; ETFs excluded this pass. GitHub Project owns lifecycle status; labels distinguish ready/blocked/exploratory/deferred/completed. No story creation starts an experiment.

Governance delivery SR-006/SR-007 is in Code review pending actual reviewer qualification. SR-002 is the next Ready research audit.

| Rank | Story / backlog | Readiness | Information value and effort | Dependencies |
|---|---|---|---|---|
| 1 | [SR-002](https://github.com/atulsrivas1/strategy-research/issues/2) / B-001 | ready | Very high: resolves anomalies comparable to the apparent signal effect; Small; provisional 3 complexity points | Scope/access gates in plan |
| 2 | [SR-008](https://github.com/atulsrivas1/strategy-research/issues/14) / B-001 | blocked | Very high: unblocks broader inference; Medium | [SR-002](https://github.com/atulsrivas1/strategy-research/issues/2) |
| 3 | [SR-009](https://github.com/atulsrivas1/strategy-research/issues/15) / B-003 | blocked | Very high across all experiments; Medium | [SR-002](https://github.com/atulsrivas1/strategy-research/issues/2) |
| 4 | [SR-010](https://github.com/atulsrivas1/strategy-research/issues/16) / B-001/B-003 | blocked | Very high: protects confirmation; Small/medium | [SR-002](https://github.com/atulsrivas1/strategy-research/issues/2), [SR-008](https://github.com/atulsrivas1/strategy-research/issues/14) |
| 5 | [SR-003](https://github.com/atulsrivas1/strategy-research/issues/3) / B-004 | blocked | High: directly answers long-stock timing question; Medium | [SR-002](https://github.com/atulsrivas1/strategy-research/issues/2), [SR-008](https://github.com/atulsrivas1/strategy-research/issues/14), [SR-009](https://github.com/atulsrivas1/strategy-research/issues/15), [SR-010](https://github.com/atulsrivas1/strategy-research/issues/16) |
| 6 | [SR-004](https://github.com/atulsrivas1/strategy-research/issues/4) / B-003 | blocked | Very high: separates touches from executable economics; Medium/high | [SR-002](https://github.com/atulsrivas1/strategy-research/issues/2), [SR-009](https://github.com/atulsrivas1/strategy-research/issues/15) |
| 7 | [SR-019](https://github.com/atulsrivas1/strategy-research/issues/25) / B-003 | blocked | High reuse confidence; not prerequisite to every private audit; Small/medium | [SR-002](https://github.com/atulsrivas1/strategy-research/issues/2), [SR-009](https://github.com/atulsrivas1/strategy-research/issues/15) |
| 8 | [SR-020](https://github.com/atulsrivas1/strategy-research/issues/26) / B-004 confirmation | blocked | Very high after development support; Medium, depends on sample accrual | [SR-003](https://github.com/atulsrivas1/strategy-research/issues/3), [SR-004](https://github.com/atulsrivas1/strategy-research/issues/4), [SR-010](https://github.com/atulsrivas1/strategy-research/issues/16) |
| 9 | [SR-011](https://github.com/atulsrivas1/strategy-research/issues/17) / B-008 | exploratory | Medium/high, distinct mechanism but costly prerequisites; Medium feasibility; high eventual study | [SR-002](https://github.com/atulsrivas1/strategy-research/issues/2), [SR-008](https://github.com/atulsrivas1/strategy-research/issues/14) |
| 10 | [SR-012](https://github.com/atulsrivas1/strategy-research/issues/18) / B-009 adaptation | exploratory | Medium: directly supports avoiding unsuitable longs; Small/medium | [SR-003](https://github.com/atulsrivas1/strategy-research/issues/3), [SR-004](https://github.com/atulsrivas1/strategy-research/issues/4) |
| 11 | [SR-013](https://github.com/atulsrivas1/strategy-research/issues/19) / B-011 | exploratory | Medium, only after price baseline; Medium/high | [SR-002](https://github.com/atulsrivas1/strategy-research/issues/2), [SR-009](https://github.com/atulsrivas1/strategy-research/issues/15), [SR-003](https://github.com/atulsrivas1/strategy-research/issues/3) |
| 12 | [SR-014](https://github.com/atulsrivas1/strategy-research/issues/20) / B-012 | exploratory | Low now; avoids expensive repeated failure; Small | [SR-003](https://github.com/atulsrivas1/strategy-research/issues/3), [SR-010](https://github.com/atulsrivas1/strategy-research/issues/16) |
| 13 | [SR-015](https://github.com/atulsrivas1/strategy-research/issues/21) / B-002 | blocked | Very high for calls; conditional priority; Medium | [SR-002](https://github.com/atulsrivas1/strategy-research/issues/2), [SR-009](https://github.com/atulsrivas1/strategy-research/issues/15) |
| 14 | [SR-005](https://github.com/atulsrivas1/strategy-research/issues/5) / B-010 | blocked | High after stock evidence; low before it; Medium/high | [SR-003](https://github.com/atulsrivas1/strategy-research/issues/3), [SR-004](https://github.com/atulsrivas1/strategy-research/issues/4), [SR-015](https://github.com/atulsrivas1/strategy-research/issues/21), [SR-020](https://github.com/atulsrivas1/strategy-research/issues/26) |
| 15 | [SR-016](https://github.com/atulsrivas1/strategy-research/issues/22) / B-005 | blocked | Medium/high only after call evidence; Medium | [SR-005](https://github.com/atulsrivas1/strategy-research/issues/5), [SR-015](https://github.com/atulsrivas1/strategy-research/issues/21), [SR-010](https://github.com/atulsrivas1/strategy-research/issues/16) |
| 16 | [SR-021](https://github.com/atulsrivas1/strategy-research/issues/27) / B-009 | blocked | Medium/low, conditional on simpler call policies; Small/medium | [SR-016](https://github.com/atulsrivas1/strategy-research/issues/22), [SR-010](https://github.com/atulsrivas1/strategy-research/issues/16) |
| 17 | [SR-017](https://github.com/atulsrivas1/strategy-research/issues/23) / B-006 | deferred | Low current relevance; conditional medium; Small proposal; medium later | Scope/access gates in plan |
| 18 | [SR-018](https://github.com/atulsrivas1/strategy-research/issues/24) / B-007 | deferred | Low current relevance because ETFs excluded; Small preservation | Scope/access gates in plan |

Every [story plan](ROADMAP.md) records hypothesis, supporting evidence, data, baseline, trial budget, decision/rejection criteria and documentation acceptance. Rankings reflect the current stock-first objective: input/universe/machinery and causal controls resolve more uncertainty than model or option tuning. Stock contexts diagnose downside; short selling/puts are excluded.

## Top three research priorities

1. SR-002: explain missing references/close definitions; anomalies can outweigh the apparent pilot effect.
2. SR-008: establish point-in-time eligible membership/actions before claiming a broader stock result.
3. SR-009: independent timing/accounting invariants prevent false improvements from implementation errors.

## Preserved completed and unsuccessful work

SR-001 foundation delivered; EQ-001-P1 locally completed/inconclusive, not promoted. Source import/planning C-001/C-002 completed locally; imported strategies unreplicated. [Lessons](LEARNINGS.md) retain classifier/continuation failures, insufficient training, concentration, grids/reentry/rescue/roll failures and target-specific context harm. No unchanged retry without a documented mechanism/data/implementation change. ETFs B-007 and intraday B-006 remain deferred under M4.

## Maintenance

After every run record all variants/failures and exposure, update scoped lessons and dependencies, rerank by uncertainty resolved/relevance/feasibility and select the next best Ready question. Numerical thresholds/splits not yet specified block execution rather than being invented after outcomes. See [knowledge workflow](knowledge/BACKLOG_WORKFLOW.md).
