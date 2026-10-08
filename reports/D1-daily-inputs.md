# D1 daily inputs: normalization, calendar and stored lineage

October 8, 2026. Related story [SR-040](../docs/stories/SR-040_PLAN.md), planned [M7](../docs/releases/M7_PLAN.md). Continuation of [first qualification](D1-input-qualification.md). Empirical admission remains blocked; zero historical strategy trials or final evaluations.

## What now qualifies

The same previously exposed development sample contains exactly the 20 prior US-equity trading dates from August 13 through September 10, 2025, independently derived from the exchange calendar. [NYSE's 2025 calendar](https://www.nyse.com/publicdocs/ICE_NYSE_2025_Yearly_Trading_Calendar.pdf) was read and visually checked; the [Nasdaq Labor Day notice](https://m.nasdaqtrader.com/TraderNews.aspx?id=ETA2025-58) confirms the September 1 closure. This date check covers that bounded interval only; it does not qualify a full historical calendar or each symbol's eligible-session universe.

All 20 stored source partitions match the hashes in the reference's source manifest. Selecting only the declared AAPL rows yields one identity row per date, valid basic OHLC bounds and nonnegative integer volume. Their 20 highs and 20 closes match the embedded reference exactly at the declared serialization tolerance of 0.00000001 dollars; observed maximum differences are zero. This verifies 40 numeric comparisons against the **curated-prepared input layer**, not an independent original-feed replay, production feature-engine parity or a market result.

[Daily normalizer](../fixtures/daily_inputs.py) now handles explicit decimal-dollar versus integer-nanosecond prices, undefined integer sentinels, identity/volume checks, timezone-aware UTC interval bounds and immutable original values. Its bounded calendar refuses dates outside the audited interval. The 20 actual ingredient rows normalize and match that calendar. Original observations and detailed receipts stay private.

## Session and availability distinction

[Databento's OHLCV specification](https://databento.com/docs/schemas-and-data-formats/ohlcv) defines the timestamp as interval start and daily intervals by UTC dates; exchange-session aggregation may require finer data. A UTC daily bar ending at midnight can contain information after the regular-session close. It cannot be relabeled as a completed core-session bar or an observed arrival timestamp.

[NYSE core hours](https://www.nyse.com/trade/hours-calendars) describe a 9:30 a.m.–4 p.m. Eastern session. In the audited summer interval, midnight UTC is 8 p.m. Eastern on the preceding local date. Therefore date completeness and numeric agreement do not authorize using a full UTC-day close at the same day's 4 p.m. decision. This is a timing constraint, not measured look-ahead incidence or evidence that every sampled bar contains a late trade.

The contract retains `available_at=None` and unknown clock authority unless independently supplied. Synthetic clock admission requires a qualified core-session basis, completed interval, qualified historical/observed arrival and arrival no later than decision. Modeled and reconstructed clocks remain ineligible. The previous artifact's September 2026 reconstruction does not establish September 2025 arrival.

## Action basis built; actual source still blocked

A research-only **split-only feature view** is implemented separately from unchanged original/execution prices. It requires dated action completeness, source/version identity and qualified relevant event clocks. Apply price factors only to observations before an event's effective date, when that event is effective by the decision and already available; volume uses reciprocal split factors. Future-effective events cannot alter a past view. Duplicate event versions and unsupported actions block. Cash-dividend adjustments are explicitly excluded from this price-breakout basis, so it does not produce dividend-adjusted total returns or replace dividend accounting.

[Databento's adjustment example](https://databento.com/docs/examples/adjustment-factors/applying-adjustment-factors) applies cumulative factors before effective dates; the local contract additionally requires historical decision-time authority. Provider example code alone does not supply those clocks or authorize data acquisition. The actual sample's unavailable corporate-action source correctly blocks the feature view. An empty event list cannot establish action completeness.

## Verification and remaining work

[60 independent hand-derived checks](../scripts/check_daily_inputs.py) cover units, undefined prices, exact calendar boundaries, timezone offsets, interval completion, split/reverse-split/composed factors, reciprocal volumes, source immutability, future-event invariance and admission failures. They complement the earlier 45 D1 ingredient checks. Neither suite claims empirical efficacy or accepted external-package consumption.

Next prerequisite is a read-only feasibility check of finer-session inputs and the source availability/action contracts. Two possible designs remain proposals: assemble qualified core-session bars from finer owned inputs, or preregister a distinctly labeled full-UTC-day scanner with its later decision clock. Do not silently change the frozen hypothesis or choose a route using outcomes. Missing observed historical arrival may require prospective capture or an explicitly accepted modeled-only scope; software cannot invent it.

The finer-input metadata check now finds all 60 expected prepared partitions: minute bars, trades and trade-triggered quotes for each of the same 20 dates. Only file existence and Parquet schemas were read; no finer price values or symbol-specific coverage were inspected. This supports a feasible core-session qualification route, not a certified reconstruction. Preregister source identity, listing/venue coverage, eligible trade conditions, timezone/session and auction boundaries, corrections and delivery clocks before constructing session OHLCV. Trade-triggered quotes are not continuous quote history. A minute-filter shortcut must not silently omit or misassign the closing auction.

Broad historical universe, adjustment/action completeness, historical arrival, executable entry/exit evidence, funding/matched accounting and the exact scanner/context empirical protocol remain unqualified. Prior SR-008/SR-010 **closed restricted M0 acceptance is preserved**; references identify capability lineage, not newly broadened completion or automatic reopening. Current bounded work stays under SR-040, with shared SR-022/SR-004/SR-025 blockers. Full SR-040 remains open; M7 is unreleased. No original feed, source-owner job, fresh holdout, context retry or scientific release was launched.

Agent inspected source/evidence under the owner waiver; separate PR review is optional and no independent approval is claimed. CI and exact published-source verification remain delivery requirements.
