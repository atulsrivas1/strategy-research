# SR-012 — Specify downside-risk diagnostics for long entries

## M1 feasibility-only amendment — October 6, 2026

This pass delivers the bounded [design/feasibility/defer decision](../../reports/M1-feasibility.md), not the empirical extension described below. Original dependencies and future scopes remain visible. Zero auxiliary veto/flow ablations, zero fits, zero monthly/news outcomes. Scope is reconciled for review, not yet accepted as release/Done. Separate final-head review/publication requirements remain.

Parent: [E02](https://github.com/atulsrivas1/strategy-research/issues/9). Release plan: [M1](../releases/M1_PLAN.md). Backlog mapping: B-009 adaptation. Current lifecycle is in the [Project](https://github.com/users/atulsrivas1/projects/4); readiness classification: **exploratory**.

## Hypothesis and information value

One causal context veto may avoid poor long entries without sacrificing more upside than it saves.

Expected information value: Medium: directly supports avoiding unsuitable longs. Effort: Small/medium; estimates describe planning complexity, not deadlines or velocity.

## Sources and prior lessons

[Preserved lessons](../LEARNINGS.md), imported report claims not independently replayed; L-013/L-014. This stock adaptation is a new hypothesis, not replication of prior option veto. Read linked source/lesson limitations before selecting work. Literature and imported reports are not local replication. See [source map](../sources/SOURCE_MAP.md).

## Dependencies and required data

[SR-003](https://github.com/atulsrivas1/strategy-research/issues/3), [SR-004](https://github.com/atulsrivas1/strategy-research/issues/4)

Qualified same-clock stock contexts, frozen stock entries and executable outcomes; no short/put trades.

## Baseline and experiment

Long-stock baseline versus one predeclared veto in shadow; compare avoided losses, rejected winners, net expectancy and coverage with equal accounting.

Trial/search budget: One veto/control, no filter grid; design only until supported baseline.

## Acceptance and rejection

Adoption requires incremental net benefit with dependence-aware lower bound above zero under stress and acceptable participation/risk. Harm rejects tested veto; post-outcome thresholds exploratory. Actual veto and numeric risk limit must be frozen before run.

- [ ] Before execution, freeze exact mathematics/units/clocks, eligibility, dataset version and exposure, splits/purge, costs, metrics, quantitative thresholds and command in a versioned experiment specification. A feasibility or documentation story records why market-run fields do not apply.
- [ ] Independent relevant checks establish the claimed scope; any bug invalidates affected results, not the market hypothesis.
- [ ] Save all variants, failed runs, exclusions, amendments, exact commands/manifests and uncertainty; publish only sanitized methodology/aggregates.
- [ ] Deliver the scoped verdict and limitations, including rejected/inconclusive/no-change findings; do not require a positive strategy to complete research.
- [ ] Update applicable report/source notes, lessons, index, backlog dependencies and handoff in the same story.
- [ ] Separate completed Codex review covers final head; findings resolved/dispositioned, relevant checks pass, declared deliverable published and actual source/artifacts verified before Done.

## Deliverables and resume

Public plan, applicable sanitized result or feasibility/decision report, evidence index and delivery receipt. Detailed commands, manifests, logs, ledgers and original source provenance remain in the private evidence store. Do not fabricate a run command before implementation. Select dependency-satisfied work from the ranked backlog; no experiment starts merely because this plan exists.
