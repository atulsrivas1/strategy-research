# SR-022 — Qualify decision-time stock and market context

Parent: [E06](https://github.com/atulsrivas1/strategy-research/issues/34). Release plan: [M2](../releases/M2_PLAN.md). Scientific status: not tested; milestone planned/unreleased. [Live story](https://github.com/atulsrivas1/strategy-research/issues/35).

## Hypothesis and information value

The existing data can support a causal scanner/context comparison only if stock features and a non-ETF market measure have qualified historical clocks, lineage, coverage and comparable availability. Presence alone can otherwise produce a hindsight filter.


## Sources and prior lessons

- [M1 accepted release](https://github.com/atulsrivas1/strategy-research/releases/tag/m1-restricted-evidence-v1): one allocation comparison remained inconclusive, cost-sensitive and unpromoted.
- [Existing pullback/source plan](https://github.com/atulsrivas1/strategy-research/blob/main/docs/stories/SR-003_PLAN.md): original local uptrend-pullback result was inconclusive; price touches did not establish attainable profits.
- [Prior downside/context design](https://github.com/atulsrivas1/strategy-research/blob/main/docs/stories/SR-012_PLAN.md) and [flow qualification](https://github.com/atulsrivas1/strategy-research/blob/main/docs/stories/SR-013_PLAN.md): feasibility/design delivery is not empirical filter success.
- [Preserved lessons](https://github.com/atulsrivas1/strategy-research/blob/main/docs/LEARNINGS.md): filters can discard profitable trades; prior imported option results were configuration-dependent and were not locally replicated.

Owner explicitly requests scanner plus contemporaneous stock/market context and new versions of already backtested stock scenarios. The new incremental question is context utility, not an unchanged retry or a search for filters that remove known losers. Original results and released source remain immutable. Both old windows remain exposed development; no fresh holdout claim.



## Dependencies and required data

[SR-008](https://github.com/atulsrivas1/strategy-research/issues/14), [SR-019](https://github.com/atulsrivas1/strategy-research/issues/25). Shared [scanner/context protocol](../knowledge/SCANNER_CONTEXT_PROTOCOL.md). Read qualified source/calculation/availability contracts and freeze applicable execution/cost policy before outcomes. New market context cannot be inferred from schema presence or a research-only output. Context qualification and synthetic checks can proceed while empirical gates remain blocked; replay cannot.

## Baseline and experiment

## Data, baseline and work

Baseline: frozen stock-price extracts provide OHLC, SMA50/100 and prior-reference dates, but not a complete qualified market layer. Read only input schemas/metadata and required past/current observations; exclude outcome modules. Inventory relevant stock context, prior-low semantics and non-ETF market regime candidates, historical available-at/freshness contracts and exact source versions. Qualify blocked/research-only context outputs individually rather than adopting all generated scores. Do not rebuild source features without a separate versioned need.

Acceptance: field-by-field contract, coverage and causal-prefix/future-perturbation checks; exact scanner binding; independently checked generation/source/calculation parity where consumed. Missing clocks, unavailable market history or unresolved blocked lineage must yield an explicit non-adoption/defer decision. No inference that an 18-stock cohort is representative market breadth.

Priority P1, information value high (blocks all honest context tests), effort medium. Planning budget one relevant context inventory, zero strategy replays/models/threshold searches. Dependencies: existing SR-008/019 bounded input qualifications; unqualified new fields stay blocked. Follow-up execution needs SR-004 and the new harness story.



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
