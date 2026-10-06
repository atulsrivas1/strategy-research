# SR-008 — Qualify historical stock universe and corporate actions

Parent: [E01](https://github.com/atulsrivas1/strategy-research/issues/8). Release plan: [M0](../releases/M0_PLAN.md). Backlog mapping: B-001. Current lifecycle is in the [Project](https://github.com/users/atulsrivas1/projects/4); readiness classification: **blocked**.

## Hypothesis and information value

Point-in-time membership and action handling eliminate survivorship and identity artifacts before expanding the cohort.

Expected information value: Very high: unblocks broader inference. Effort: Medium; estimates describe planning complexity, not deadlines or velocity.

## Sources and prior lessons

[EQ-001-P1](../../reports/EQ-001-P1.md), locally tested and inconclusive; L-016/DQ-002; DQ-001/DQ-002. Read linked source/lesson limitations before selecting work. Literature and imported reports are not local replication. See [source map](../sources/SOURCE_MAP.md).

## Dependencies and required data

[SR-002](https://github.com/atulsrivas1/strategy-research/issues/2)

Historical common-stock eligibility, large/mid-cap and liquidity observations known at selection, symbol changes/delistings and corporate-action lineage.

## Baseline and experiment

Compare convenience cohort with outcome-blind historical membership; independently reconcile a fixed identity/action boundary sample.

Trial/search budget: One fixed membership specification and boundary sample; no winning-stock selection.

## Acceptance and rejection

Selection uses past-only facts; delisted/renamed and excluded names documented; coverage denominators complete. Missing historical membership blocks representative-universe claims. No outcome-based ticker replacement.

- [ ] Before execution, freeze exact mathematics/units/clocks, eligibility, dataset version and exposure, splits/purge, costs, metrics, quantitative thresholds and command in a versioned experiment specification. A feasibility or documentation story records why market-run fields do not apply.
- [ ] Independent relevant checks establish the claimed scope; any bug invalidates affected results, not the market hypothesis.
- [ ] Save all variants, failed runs, exclusions, amendments, exact commands/manifests and uncertainty; publish only sanitized methodology/aggregates.
- [ ] Deliver the scoped verdict and limitations, including rejected/inconclusive/no-change findings; do not require a positive strategy to complete research.
- [ ] Update applicable report/source notes, lessons, index, backlog dependencies and handoff in the same story.
- [ ] Separate completed Codex review covers final head; findings resolved/dispositioned, relevant checks pass, declared deliverable published and actual source/artifacts verified before Done.

## Deliverables and resume

Public plan, applicable sanitized result or feasibility/decision report, evidence index and delivery receipt. Detailed commands, manifests, logs, ledgers and original source provenance remain in the private evidence store. Do not fabricate a run command before implementation. Select dependency-satisfied work from the ranked backlog; no experiment starts merely because this plan exists.
