# SR-009 — Verify causal simulation and accounting fixtures

Parent: [E01](https://github.com/atulsrivas1/strategy-research/issues/8). Release plan: [M0](../releases/M0_PLAN.md). Backlog mapping: B-003. Current lifecycle is in the [Project](https://github.com/users/atulsrivas1/projects/4); readiness classification: **blocked**.

## Hypothesis and information value

Independent invariants expose timing and accounting defects before new market comparisons.

Expected information value: Very high across all experiments. Effort: Medium; estimates describe planning complexity, not deadlines or velocity.

## Sources and prior lessons

[Preserved lessons](../LEARNINGS.md), imported report claims not independently replayed; L-009/L-010/L-012 and pilot adapter correction. Read linked source/lesson limitations before selecting work. Literature and imported reports are not local replication. See [source map](../sources/SOURCE_MAP.md).

## Dependencies and required data

[SR-002](https://github.com/atulsrivas1/strategy-research/issues/2)

Qualified input contracts and existing research engine, hand-derived expected fixtures; synthetic fixtures publishable.

## Baseline and experiment

Independent prior/current/stale reference, warmup, completed-bar, split-boundary, missing/action, duplicate/overlap/cash and same-bar ambiguity fixtures.

Trial/search budget: One bounded suite and small deterministic replay; no optimizer.

## Acceptance and rejection

Exact timestamps/categories and declared numeric tolerances; future-input perturbation cannot change earlier decisions; any failing invariant invalidates affected replay. Passing is machinery acceptance, not edge.

- [ ] Before execution, freeze exact mathematics/units/clocks, eligibility, dataset version and exposure, splits/purge, costs, metrics, quantitative thresholds and command in a versioned experiment specification. A feasibility or documentation story records why market-run fields do not apply.
- [ ] Independent relevant checks establish the claimed scope; any bug invalidates affected results, not the market hypothesis.
- [ ] Save all variants, failed runs, exclusions, amendments, exact commands/manifests and uncertainty; publish only sanitized methodology/aggregates.
- [ ] Deliver the scoped verdict and limitations, including rejected/inconclusive/no-change findings; do not require a positive strategy to complete research.
- [ ] Update applicable report/source notes, lessons, index, backlog dependencies and handoff in the same story.
- [ ] Separate completed Codex review covers final head; findings resolved/dispositioned, relevant checks pass, declared deliverable published and actual source/artifacts verified before Done.

## Deliverables and resume

Public plan, applicable sanitized result or feasibility/decision report, evidence index and delivery receipt. Detailed commands, manifests, logs, ledgers and original source provenance remain in the private evidence store. Do not fabricate a run command before implementation. Select dependency-satisfied work from the ranked backlog; no experiment starts merely because this plan exists.

Bounded execution/feasibility evidence: [M0 report](../../reports/M0-qualification.md). Full story acceptance and public delivery remain partial; no approved scope deletion or Done.

Coordinator acceptance correction: reject nonfinite, nonpositive and non-integer-cent marks before synthetic equity calculation; retain original fixture evidence and add nine independent invalid-mark cases. Passing corrected reference tests does not certify integration or market data.
