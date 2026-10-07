# SR-052 — Qualify V3-05: Merger arbitrage

Parent: [E08](https://github.com/atulsrivas1/strategy-research/issues/46). Release plan: [M4](../releases/M4_PLAN.md).
State: Deferred: deal-life horizon and stock-deal hedges/borrow outside scope. Scientific status: untested locally. Low current-scope priority; small archival qualification, empirical effort unestimated and excluded this pass.

## Hypothesis and information value

Deal spreads compensate break, delay and funding risks. MNA-D versus always-invested ungated deal-spread control; preserve event-time annualization warning and downside exposure. The purpose is to resolve testability/evidence gaps, not infer a profitable rule from historic source numbers. Canonical horizon and instruments cannot be transferred silently to five-session US long-only stocks.

## Sources and prior lessons

[V3-05 source dossier](../strategy-library-v3/05-position-merger-arbitrage.md) sections 1–9, especially source reading limits, failure modes and proposed validation. [Source log](../strategy-library-v3/SOURCES.md) and [import notes](../strategy-library-v3/IMPORT_NOTES.md) distinguish the originating author's paper reads from this project's verification. Their grades/numbers are reported findings; no V3 local backtest exists. [Existing library catalog](../strategy-library/CATALOG.md) and [M2 unsuccessful context tests](../../reports/M2-context-proxy.md) remain preserved. No unchanged failed gate retry or retrospective exclusion of known losers.

## Dependencies and required data

point-in-time announced/cancelled/completed deal tape, offers/revisions, breaks, executable borrow and calendar-time ledger. [SR-008](https://github.com/atulsrivas1/strategy-research/issues/14) actions/universe, [SR-010](https://github.com/atulsrivas1/strategy-research/issues/16) chronology/exposure, [SR-022](https://github.com/atulsrivas1/strategy-research/issues/35) context clocks, [SR-025](https://github.com/atulsrivas1/strategy-research/issues/38) matched accounting and [SR-004](https://github.com/atulsrivas1/strategy-research/issues/4) applicable execution qualification remain required for empirical adoption. Explicit owner scope expansion is needed before empirical work. An import is not that instruction.

## Baseline and experiment

MNA-D versus always-invested ungated deal-spread control; preserve event-time annualization warning and downside exposure. The canonical section7 thresholds/splits/grids are archived proposed designs, not frozen project experiments. Originating notes calling old calendar ranges holdout do not establish that those dates are untouched here. Reconcile the project exposure registry first; final access disabled. Current import budget: zero historical comparisons, zero final evaluations.

Before any eligible future experiment freeze exact rule/version, point-in-time inputs, decision/entry/exit clocks, causal missing-data/universe policies, chronological boundaries/purge, baseline, costs/turnover, sample support, dependence-aware uncertainty and numerical decision criteria. Every strategy test retains scanner-alone matched control versus one preregistered stock/market-context overlay with aligned/conflicting/neutral/unknown states, cash for vetoes and no rescaling. Count avoided losses and sacrificed winners, cost/implementation stresses and all unavailable/censored observations. No automatic grids, live risk limits or holdout claims imported from source notes.

## Acceptance and rejection

Qualification accepts a verifiable source/rule/input contract or records an honest scoped feasibility blocker. Missing source facts must not be guessed. For eligible future empirical tests, net incremental benefit must exceed the preregistered threshold with adequate frozen support and a dependence-aware interval above zero, survive execution/cost stress and avoid concentration-driven apparent success. Nonpositive net benefit rejects only the tested scope; an interval spanning zero is inconclusive; bugs invalidate results. Numeric cost/support/search choices must be registered before outcomes; none is approved by this import. Preserve all failed runs and rejected variants. Separate research PR review is optional under the owner's waiver; CI, relevant independent numerical checks, privacy and delivered-byte verification still apply.

## Deliverables and resume

Source/rule qualification note, versioned experiment specification or scoped blocker, provenance/commands/checks and all later outcomes if authorized; update lessons, backlog, index, handoff and Project. Current story is planning only, not complete empirical research. Keep M4 deferred. Preserve the dossier and resolve source questions only when relevant; no empirical runner launch. No ETF/short/intraday/futures/year-horizon expansion, paid data, new chat, worker or final access.
