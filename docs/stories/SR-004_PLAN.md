# SR-004 — Validate observed fills and funded stock accounting

## Owner research-review amendment — October 7, 2026

The owner explicitly waived separate code/PR review for this strategy-research project and authorized autonomous work within its operating scope. This supersedes older mandatory Codex-review clauses in research plans, templates, checklists and pending-delivery descriptions, including SR-006's review activation dependency. Separate review is optional, not a merge/Done gate. No completed review is retrospectively claimed. This does not waive source qualification, causal validity, independent relevant numerical verification, CI, privacy, exact source/artifact verification, release acceptance or current scope. It does not apply to equity-features or chartsspeak development. Retain the eight tracking stages; Code review records agent evidence inspection and the owner waiver, not independent approval. Frozen historical receipts remain unchanged; old review requirements below are historical where they conflict with this amendment.


Parent: [E03](https://github.com/atulsrivas1/strategy-research/issues/10). Release plan: [M2](../releases/M2_PLAN.md). Backlog mapping: B-003. Current lifecycle is in the [Project](https://github.com/users/atulsrivas1/projects/4); readiness classification: **blocked**.

## Hypothesis and information value

Apparent stock movement remains economically meaningful under feasible fills and funded allocation.

Expected information value: Very high: separates touches from executable economics. Effort: Medium/high; estimates describe planning complexity, not deadlines or velocity.

## Sources and prior lessons

[Preserved lessons](../LEARNINGS.md), imported report claims not independently replayed; L-005/L-007/L-010/L-014. Read linked source/lesson limitations before selecting work. Literature and imported reports are not local replication. See [source map](../sources/SOURCE_MAP.md).

## Dependencies and required data

[SR-002](https://github.com/atulsrivas1/strategy-research/issues/2), [SR-009](https://github.com/atulsrivas1/strategy-research/issues/15)

Qualified quotes/sizes and event/receipt clocks, actions/dividends, declared capital/position constraints and order model. Owner risk/capital decisions needed for funded comparison.

## Baseline and experiment

Identical frozen stock orders under bar proxy and quote-supported execution; independent hand-worked cash, overlap, reservation, integer-quantity, action and exit fixtures.

Trial/search budget: One fixed fixture suite and bounded replay; no latency/allocation tuning.

## Acceptance and rejection

Exact cash/position identity and predeclared numeric tolerances; no unsupported quote implies a fill. Unknown fills stay unknown/unfilled and enter bounds. Reject executable benefit if net improvement disappears under credible costs; missing evidence blocks the claim.

- [ ] Before execution, freeze exact mathematics/units/clocks, eligibility, dataset version and exposure, splits/purge, costs, metrics, quantitative thresholds and command in a versioned experiment specification. A feasibility or documentation story records why market-run fields do not apply.
- [ ] Independent relevant checks establish the claimed scope; any bug invalidates affected results, not the market hypothesis.
- [ ] Save all variants, failed runs, exclusions, amendments, exact commands/manifests and uncertainty; publish only sanitized methodology/aggregates.
- [ ] Deliver the scoped verdict and limitations, including rejected/inconclusive/no-change findings; do not require a positive strategy to complete research.
- [ ] Update applicable report/source notes, lessons, index, backlog dependencies and handoff in the same story.
- [ ] Separate completed Codex review covers final head; findings resolved/dispositioned, relevant checks pass, declared deliverable published and actual source/artifacts verified before Done.

## Deliverables and resume

Public plan, applicable sanitized result or feasibility/decision report, evidence index and delivery receipt. Detailed commands, manifests, logs, ledgers and original source provenance remain in the private evidence store. Do not fabricate a run command before implementation. Select dependency-satisfied work from the ranked backlog; no experiment starts merely because this plan exists.

## M2 readiness evidence, not acceptance closure

[Actual bounded findings](../../reports/M2-readiness.md) document useful outcome-free work and remaining dependencies. No strategy result, observed-fill qualification, final access, completed hosted review, release or Done claim. Original plans retained; full applicable acceptance remains open.
