# D1 session feasibility and unresolved source authority

October 8, 2026. Related [SR-040](../docs/stories/SR-040_PLAN.md), planned [M7](../docs/releases/M7_PLAN.md). Continues [daily-input qualification](D1-daily-inputs.md). One outcome-free input pilot, no strategy replay or final access.

## Completed bounded pilot

[Minute aggregator](../fixtures/session_proxy.py) computes a deliberately labeled **half-open minute proxy**, preserving missing bins and rejecting invalid prices, identity ambiguity, duplicate intervals and timestamp truncation. Original data remains unchanged. [25 hand-derived checks](../scripts/check_session_proxy.py) independently verify OHLC/volume arithmetic, exact boundaries, gaps, ordering, timezone offsets and exclusion of preopen/future prices. No official-close or empirical authority is granted by its output.

One AAPL development day, September 10, 2025, was selected before reading values. Its stored minute source was hashed before and after the read. All 390 expected minute bins in the declared 9:30 a.m.–4 p.m. Eastern half-open window are present and internally valid. An independent calculation over the frozen selected rows matches all five OHLC/volume aggregates and the complete minute grid. Prices outside that interval were not read. The detailed proxy values and source receipts remain private. This establishes mechanics and sample bin coverage, not an economic result, broad symbol coverage or original-feed parity.

## Why official-session qualification remains blocked

[Databento Mini specification](https://databento.com/docs/venues-and-datasets/equs-mini) describes an aggregated, derived feed; original trade venues are anonymized and OHLCV spans its component venues. [OHLCV conventions](https://databento.com/docs/schemas-and-data-formats/ohlcv) describe interval-start timestamps and caution that trade conditions, corrections and aggregation choices matter. Neither statement qualifies every listing venue or proves equivalence with the distinct daily-summary feed.

[Nasdaq's cross FAQ](https://www.nasdaqtrader.com/content/productsservices/trading/crosses/openclose_faqs.pdf), questions 5–6, describes a closing cross initiated at 4 p.m. that sets the official closing price, with a last-sale-eligible fallback when absent. A half-open minute filter cannot certify auction inclusion or the official-close fallback. Current documentation does not independently establish every historical September 2025 rule/version.

The sampled prepared minute schema retains timestamp, symbol, instrument ID, OHLC and volume. Its neighboring prepared trade schema retains timestamp, symbol, instrument ID, price, size and tick-rule sign. The sampled trade/quote schemas lack separate event/capture/original-arrival clocks, original venue and auction/last-sale/correction eligibility fields. Their absence here does not prove the original source lacks them. Restore and qualify lineage through the source owner or an authorized research adapter; never invent those fields from prices or assume a timestamp's role.

Corporate-action completeness and original historical arrival remain unqualified. The first qualification's original Turtle-rule PDFs remain inaccessible and unverified. Accordingly the one-day proxy does not make D1 testable under strict core-session/source/clock requirements. No daily-summary versus Mini numeric equality is asserted; they are different source scopes.

## Disposition and next work

D1 has a reproducible ingredient/scanner contract, bounded date and stored-price reconciliation, a labeled minute aggregation pilot and explicit blocked requirements. Full SR-040 remains open with partial qualification; M7 remains unreleased. Park additional market reads pending source-owned eligibility/auction/clock and action evidence, or an explicitly accepted and separately preregistered proxy scope. Existing restricted M0 receipts stay immutable; no automatic retrospective replay or new verdict about their validity.

Advance sequentially to D2 source/ranking qualification while these strict inputs are blocked. Source readiness is independent of empirical admission: no context tuning, trial allowance, fresh holdout, paid purchase, producer job or new execution session is created. Agent evidence inspection under the owner's separate-review waiver; no independent hosted approval claimed. CI and exact delivered-source checks remain required.
