# SR-016 — Compare frozen call-management policies

Parent: [E04](https://github.com/atulsrivas1/strategy-research/issues/11). Release plan: [M3](../releases/M3_PLAN.md). Backlog mapping: B-005. Current lifecycle is in the [Project](https://github.com/users/atulsrivas1/projects/4); readiness classification: **blocked**.

## Hypothesis and information value

Rare winners may reward a higher target, but concentration and funded execution may erase its advantage.

Expected information value: Medium/high only after call evidence. Effort: Medium; estimates describe planning complexity, not deadlines or velocity.

## Sources and prior lessons

[Preserved lessons](../LEARNINGS.md), imported report claims not independently replayed; L-004/L-007/L-011/L-014/L-015. Revisit justification: individual-stock supported decisions plus qualified new quote paths, not unchanged ETF replay. Read linked source/lesson limitations before selecting work. Literature and imported reports are not local replication. See [source map](../sources/SOURCE_MAP.md).

## Dependencies and required data

[SR-005](https://github.com/atulsrivas1/strategy-research/issues/5), [SR-015](https://github.com/atulsrivas1/strategy-research/issues/21), [SR-010](https://github.com/atulsrivas1/strategy-research/issues/16)

Supported stock-to-call expression, qualified full quote paths, identical entries/contracts/funding and unused evaluation.

## Baseline and experiment

Fixed +50% versus fixed +200% under identical support exits/funding; optional split only if declared sizing feasibility before outcomes.

Trial/search budget: Two policies; at most three with predeclared feasible split; no target/reentry/roll/rescue grids.

## Acceptance and rejection

Incremental net/risk criteria frozen before run; dependent intervals, largest-date and unknown-exit stress required. No promotion if costs/concentration explain advantage. Negative result limited to chosen policy/market.

- [ ] Before execution, freeze exact mathematics/units/clocks, eligibility, dataset version and exposure, splits/purge, costs, metrics, quantitative thresholds and command in a versioned experiment specification. A feasibility or documentation story records why market-run fields do not apply.
- [ ] Independent relevant checks establish the claimed scope; any bug invalidates affected results, not the market hypothesis.
- [ ] Save all variants, failed runs, exclusions, amendments, exact commands/manifests and uncertainty; publish only sanitized methodology/aggregates.
- [ ] Deliver the scoped verdict and limitations, including rejected/inconclusive/no-change findings; do not require a positive strategy to complete research.
- [ ] Update applicable report/source notes, lessons, index, backlog dependencies and handoff in the same story.
- [ ] Separate completed Codex review covers final head; findings resolved/dispositioned, relevant checks pass, declared deliverable published and actual source/artifacts verified before Done.

## Deliverables and resume

Public plan, applicable sanitized result or feasibility/decision report, evidence index and delivery receipt. Detailed commands, manifests, logs, ledgers and original source provenance remain in the private evidence store. Do not fabricate a run command before implementation. Select dependency-satisfied work from the ranked backlog; no experiment starts merely because this plan exists.
