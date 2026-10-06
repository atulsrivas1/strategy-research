# SR-014 — Check predictor sample and decision feasibility

Parent: [E02](https://github.com/atulsrivas1/strategy-research/issues/9). Release plan: [M1](../releases/M1_PLAN.md). Backlog mapping: B-012. Current lifecycle is in the [Project](https://github.com/users/atulsrivas1/projects/4); readiness classification: **exploratory**.

## Hypothesis and information value

A predictor is useful only with independent support and changed economically meaningful decisions.

Expected information value: Low now; avoids expensive repeated failure. Effort: Small; estimates describe planning complexity, not deadlines or velocity.

## Sources and prior lessons

[Preserved lessons](../LEARNINGS.md), imported report claims not independently replayed; L-001/L-002/L-003. Read linked source/lesson limitations before selecting work. Literature and imported reports are not local replication. See [source map](../sources/SOURCE_MAP.md).

## Dependencies and required data

[SR-003](https://github.com/atulsrivas1/strategy-research/issues/3), [SR-010](https://github.com/atulsrivas1/strategy-research/issues/16)

Unique episode counts, feature availability and decision diversity; documented changed mechanism before retry; old forecasts remain development.

## Baseline and experiment

Feasibility/counts first; compare proposed decision reach to constant-policy baseline. Do not fit a model in this story.

Trial/search budget: One feasibility audit, zero model fits/search.

## Acceptance and rejection

Insufficient independent support or identical reachable decisions stops modeling. Future model story requires power/precision rationale, fixed features, chronological calibration and incremental economic criterion. Probability-score improvement alone is insufficient.

- [ ] Before execution, freeze exact mathematics/units/clocks, eligibility, dataset version and exposure, splits/purge, costs, metrics, quantitative thresholds and command in a versioned experiment specification. A feasibility or documentation story records why market-run fields do not apply.
- [ ] Independent relevant checks establish the claimed scope; any bug invalidates affected results, not the market hypothesis.
- [ ] Save all variants, failed runs, exclusions, amendments, exact commands/manifests and uncertainty; publish only sanitized methodology/aggregates.
- [ ] Deliver the scoped verdict and limitations, including rejected/inconclusive/no-change findings; do not require a positive strategy to complete research.
- [ ] Update applicable report/source notes, lessons, index, backlog dependencies and handoff in the same story.
- [ ] Separate completed Codex review covers final head; findings resolved/dispositioned, relevant checks pass, declared deliverable published and actual source/artifacts verified before Done.

## Deliverables and resume

Public plan, applicable sanitized result or feasibility/decision report, evidence index and delivery receipt. Detailed commands, manifests, logs, ledgers and original source provenance remain in the private evidence store. Do not fabricate a run command before implementation. Select dependency-satisfied work from the ranked backlog; no experiment starts merely because this plan exists.
