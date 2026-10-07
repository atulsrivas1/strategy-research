# SR-023 — Rework the uptrend-pullback test with context

Parent: [E06](https://github.com/atulsrivas1/strategy-research/issues/34). Release plan: [M2](../releases/M2_PLAN.md). Scientific status: not tested; milestone planned/unreleased. [Live story](https://github.com/atulsrivas1/strategy-research/issues/36).

## Hypothesis and information value

Temporary pullbacks inside an uptrend may recover more reliably when stock context does not indicate a prior-range breakdown and market conditions support long risk. Incremental net benefit can be negative if the gate removes rebound winners.


## Sources and prior lessons

- [M1 accepted release](https://github.com/atulsrivas1/strategy-research/releases/tag/m1-restricted-evidence-v1): one allocation comparison remained inconclusive, cost-sensitive and unpromoted.
- [Existing pullback/source plan](https://github.com/atulsrivas1/strategy-research/blob/main/docs/stories/SR-003_PLAN.md): original local uptrend-pullback result was inconclusive; price touches did not establish attainable profits.
- [Prior downside/context design](https://github.com/atulsrivas1/strategy-research/blob/main/docs/stories/SR-012_PLAN.md) and [flow qualification](https://github.com/atulsrivas1/strategy-research/blob/main/docs/stories/SR-013_PLAN.md): feasibility/design delivery is not empirical filter success.
- [Preserved lessons](https://github.com/atulsrivas1/strategy-research/blob/main/docs/LEARNINGS.md): filters can discard profitable trades; prior imported option results were configuration-dependent and were not locally replicated.

Owner explicitly requests scanner plus contemporaneous stock/market context and new versions of already backtested stock scenarios. The new incremental question is context utility, not an unchanged retry or a search for filters that remove known losers. Original results and released source remain immutable. Both old windows remain exposed development; no fresh holdout claim.



## Dependencies and required data

[SR-022](https://github.com/atulsrivas1/strategy-research/issues/35), [SR-025](https://github.com/atulsrivas1/strategy-research/issues/38), [SR-004](https://github.com/atulsrivas1/strategy-research/issues/4). Shared [scanner/context protocol](../knowledge/SCANNER_CONTEXT_PROTOCOL.md). Read qualified source/calculation/availability contracts and freeze applicable execution/cost policy before outcomes. New market context cannot be inferred from schema presence or a research-only output. Context qualification and synthetic checks can proceed while empirical gates remain blocked; replay cannot.

## Baseline and experiment

## Baseline, new version and controls

Create EQ-001-CONTEXT-v2; preserve original EQ-001-P1 rule and outcomes. Scanner: original two-session pullback within Close > SMA50 > SMA100, with original causal price/liquidity conditions. Use separately qualified common-cohort/date/clock controls; any move from the original 20 names to approved 18, or stronger R2 schedule, gets a bridge/reconciliation record and is never attributed to context utility. No outcome-selected stock removal.

Compare qualified scanner alone versus identical scanner plus the one preregistered stock/market policy, next exact-session entry and five-session exit. Exposed periods stay development, protected final disabled. Distinguish scanner-return proxies from executed/funded accounting. Count +2/3% touches as descriptive only, not target fills.

Required data/dependencies: SR-022 field clocks/market coverage, SR-025 harness, SR-004 applicable executable-baseline economics and frozen exposure registry. Numeric decision thresholds, action/cash policy and costs must be frozen before replay; default proposal is >10 bps incremental mean, uncertainty excluding zero and positive predeclared execution stresses, with adequate paired-date support. Otherwise reject the incremental claim when <=0; classify positive-but-uncertain results inconclusive, not universally reject pullbacks.

Priority P2 after shared gates; high information value (directly addresses owner's stock-movement objective), effort medium. Budget one unchanged scanner, one joint overlay, one five-session horizon, primary plus at most three predeclared costs; no fitting, optimization or final access.



## Acceptance and rejection

Scanner alone is the matched control; scanner plus one preregistered joint stock/market policy is the candidate. Declare aligned/conflicting/neutral/unknown states using fields actually available at decision time; stock and market states reported separately. Missing, stale or late context is unknown. No ETF strategies, shorts, calls, hidden threshold/feature grid, ticker pruning, management changes or final holdout access. A new context comparison consumes a new explicit budget, not remaining M1 budget.

Preserve original opportunities/weights, rejected allocation in cash, no rescaling retained names. Count avoided losses and sacrificed winners net of costs; keep every candidate, unavailable context, unfilled/censored observation and failed run. Freeze exact formulas, sources/versions/clocks, chronology, costs, support thresholds, metrics, uncertainty and rejection criteria before outcome access. Independent relevant correctness checks precede historical replay. Context usefulness must survive differential costs and uncertainty, not merely raise win rate.

- [ ] Complete relevant source/clock qualification and dependency evidence.
- [ ] Frozen bounded specification, numerical criteria and actual trial/exposure registry before outcomes.
- [ ] All controls, outcomes or honest blockers, failed attempts and limitations preserved.
- [ ] Updated source-linked lessons, ranked backlog/index/handoff and sanitized methodology.
- [ ] Completed final-head Codex review/findings disposition and applicable CI.
- [ ] Declared publication/source/artifacts verified before Done. Planning alone is not delivery or a released trading strategy.

No live orders, purchases, source-production jobs or automatic new session/schedule. Scientific rejection or inconclusive results can complete a faithfully delivered research story. M1 owner-review exception does not extend here.


## Deliverables and resume

Versioned specification, field/clock coverage manifest or honest blocker, independent relevant checks, complete commands/provenance and failed attempts, scoped report/lessons/index/backlog/handoff. Original results remain immutable; no final holdout or new session is created. First qualify SR-022, then the shared SR-025/SR-004 gates before either replay. Exact source/CI/reviewer response and publication verification precede Done.
