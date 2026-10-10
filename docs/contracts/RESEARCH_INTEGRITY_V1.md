# Research integrity v1 — prospective shared infrastructure

SR-025 / E06 / M2 owns the funded matched-accounting build; SR-008/010/022 and SR-040/041 consume the input, chronology and receipt contracts. This version adds infrastructure without changing historical engines, reports, trials, verdicts or budgets. Full story qualification and M7 release remain open. Separate review is optional under the owner waiver; agent inspection is not independent approval.

## Execution receipt

[execution_guard.py](../../research/execution_guard.py) discovers the actual function-based engine and referenced local module/function dependencies, verifies loaded function code against source, and binds exact bytes separately from LF-normalized hashes. Callback source/code, guard source, frozen protocol, Python/platform and exact input snapshots are recorded before callbacks run. Every discovered local source is retained by content hash. A caller supplies the preregistered development allowlist; unknown/protected inputs are rejected before reading their bytes. An attempt directory cannot be reused. Source changes or callback/evaluator failures retain a failed receipt and never qualify as a successful run.

This is an audited offline Python execution contract, not a sandbox. Arbitrary dynamic imports, generated code, class-based engines, mutable global/closure configuration and external I/O are outside its guarantee. Function-local imports and locally defined engine classes fail closed. Declare configuration in the frozen protocol and import supported dependencies before execution. Callbacks must consume the supplied immutable byte snapshots, with no extra loaders. Review the entire runner, declared imports and holdout map before use. Successful receipts establish this scoped execution binding, not provider provenance, causal validity or profitability. Do not backfill the missing historical D2 pre-run engine hash.

## Lossless input and chronology

[lossless_inputs.py](../../research/lossless_inputs.py) retains positive stable security ID, original symbol, session date, Decimal price strings, integer/unknown volume, original timezone-aware timestamps and explicit source/unit/action/clock assumptions. Reject float inputs, nonfinite/nonpositive prices, invalid OHLC, duplicate security/date and ambiguous symbol-to-ID mappings. Quarantine ambiguities for an explicit adapter disposition; never silently merge ticker histories. Source rows already reduced to floats cannot regain precision through this adapter.

History selection requires positive sufficient unique history and excludes future dates. Known arrival timestamps require an explicit decision clock and late rows are excluded. Unknown arrivals remain explicitly exploratory date proxies; no qualified clock flag is created. This does not infer official sessions, price adjustments or security master authority. Price-gap diagnostics trigger investigation, never retrospective loser removal or an assumed split/news/error cause.

## Funded paired accounting

[funded_ledger.py](../../research/funded_ledger.py) uses exact rational arithmetic with explicit finite initial cash, fixed original notionals, fractional shares and proportional per-side fees. Model open exits before open entries, then close marks. Decision precedes entry and exit is later than entry. Whole entry batches are unfilled if purchases plus fees exceed available cash; no implicit borrowing or outcome-based order selection. Overlay vetoes retain cash and never redistribute size. Same original opportunities and notionals must be used in both arms.

Report unfilled cash orders, missing entry prices, censored exits and unknown marks separately. Missing marks imply unknown NAV; missing scheduled exits remain invested/censored without an invented later fill. Return values are exact Fractions; serialize as rational or documented decimal strings, never round silently. Every reported NAV equals cash plus marked active positions. Funding feasibility is distinct from completed observations. Candidate and baseline funding failures can differ because previous proceeds differ: disclose both schedules; an unmatched fill schedule cannot establish the isolated overlay effect. A preregistered shared feasible allocation/reservation rule is required for a fully matched funded performance comparison.

The implementation models fractional lots, zero interest, no borrowing and supplied prices. It does not implement integer-lot sizing, fixed/minimum broker commissions, spreads/impact, splits/dividends, broker fills or a live capital mandate. Explicit assumptions permit exploratory use; missing evidence does not block that use. Actual corporate-action unit breaks or impossible chronology require numerical correction/quarantine, not fabricated cashflows.

## Next empirical protocol

Before new outcomes, freeze these decisions under the existing responsible strategy story:

1. Separate scanner versus a fixed opportunity-matched benchmark from scanner-plus-context versus the unchanged scanner. State the mechanism, economic benefit and falsification for each; an overlay failure does not reject the underlying family.
2. Justify formation history independently of holding horizon. Distinguish the source strategy from a short-history adaptation. Avoid convenience-window or symbol selection after outcomes.
3. Inventory all exposed development dates across projects and protect the final holdout. Set exact training/development/evaluation ranges, purge/embargo, decision-time universe and availability assumptions. Previously inspected windows are not fresh confirmation.
4. Set numeric minimum support, unique-security/concentration limits, nonoverlapping temporal coverage and a finite trial budget prospectively. A 20-date window with five-day overlapping holdings offers only four disjoint five-day blocks; do not treat 60 slots as 60 independent trials. Broader regime coverage is a requirement to design, not evidence already obtained.
5. Specify a dependence-aware interval and stopping rule for each hypothesis. Separate a failed point criterion, a negative interval, an interval crossing zero, insufficient support, funding failure and unusable input. Preserve old preregistered verdicts.
6. Freeze original sizing and funding reservation, event ordering, costs/stresses, missing-price/action/session treatment, matched benchmark schedule and ledger conservation checks. Stock-only context with unknown market state is not a tested market-regime filter.
7. Use this guard and lossless adapter in a new versioned runner, independently verify order generation and accounting, then record every attempt. No old experiment is automatically rerun and no exhausted budget is reset by infrastructure delivery.

Exact new market dates, numeric thresholds and any new strategy experiment are deliberately left to its next frozen protocol. There is no current empirical claim from this build.
