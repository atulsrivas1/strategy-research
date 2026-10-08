# B2 — Opening-gap timing and source qualification

October 8, 2026. Related [SR-033](https://github.com/atulsrivas1/strategy-research/issues/52), planned [M7](../docs/releases/M7_PLAN.md), accepted [shared design](../docs/releases/M6_RECEIPT.md). Scientific status: untested locally. This increment builds synthetic split-only gap machinery; no historical prices, gaps, identities, signals, trades, outcomes or new lake data were read.

## Primary definitions and scope

[Lou, Polk and Skouras, JFE 2019](https://personal.lse.ac.uk/polk/research/TugOfWar.pdf), abstract/introduction and section 3 (printed pages 195–196), was read directly from an author-hosted copy. The main opening measure is first-half-hour VWAP, not the official opening-cross price. Overnight returns are imputed from intraday and dividend-inclusive close-to-close returns, with corporate events assigned overnight and a stated treatment of missing opens. Their monthly long/short portfolio decomposition and cross-period reversal claims differ from a single opening gap and our proposed five-session long-only continuation. The paper also cautions that trading costs reduce strategy attractiveness. No source performance was locally reproduced.

[Nasdaq cross FAQ](https://www.nasdaqtrader.com/content/productsservices/trading/crosses/openclose_faqs.pdf), questions 5–6, was read directly. Official prices depend on the cross or specified eligible-trade fallback; a minute bar alone cannot certify them. A feature requiring the published open cannot automatically be used to enter that same auction. Current documentation does not independently establish all historical rule versions or qualify other venues.

Original overnight-hold and intraday-fade expressions remain outside the current 2–10-session strategy scope. Imported negative gap-fade/cost evidence and other source versions stay preserved, with their original reported/unverified grades. A gap-continuation adaptation needs its own frozen economic hypothesis; source import or correct arithmetic does not register an experiment.

## Ingredient and independent checks

[Opening-gap contract](../fixtures/opening_gap.py) requires one security/currency, raw unadjusted official endpoints bound to declared source IDs, a qualified adjacent exchange-session ledger and explicit endpoint boundary/availability clocks. It compares UTC instants without assuming calendar-day adjacency or a fixed UTC open across daylight saving. Nonzero subsecond timestamps are rejected before parsing, avoiding silent nanosecond truncation. The intentionally strict endpoint/boundary contract excludes unqualified delayed or fallback endpoint cases; it does not certify every legitimate exchange event.

An identity-bound complete action ledger covers the exact interval. Known effective splits align the old close to current share units using **new shares per old share**. Cash distributions and other actions block this split-only ingredient; they cannot be silently interpreted as information-driven gaps. Unknown action completeness/availability, double-adjusted endpoints, future values and mismatched identity/basis/source/session boundaries block calculation.

[65 independent hand-derived checks](../scripts/check_opening_gap.py) include raw 100→102, split-two old 100→new 51, reverse-split-half old 100→new 204 and combined offsetting splits: each has a 2% split-aligned opening gap. Checks cover a declared Friday–Monday/DST toy calendar, timezone equivalence, preopen and arrival-equality decisions, flat/down gaps, cash distributions, duplicate/late actions, unknown source clocks, malformed values and caller precision. These are synthetic fixtures and authority assertions, not actual source certification.

The output is a split-only **price gap**, not dividend-inclusive overnight return, scanner, trading profit or an executable open fill. The decision must follow opening-price arrival. Any eventual entry requires separately qualified later execution and accounting; costs are not inferred from prices.

## Data blockers and build disposition

[D1 session-source qualification](D1-session-feasibility.md) retains unqualified official endpoints, auction/eligible-trade/correction fields, original arrivals and corporate-action completeness. Existing minute/daily sources cannot silently become a matched official-close/open feed. No new inventory, selected market rows or parity claim is made here.

Next source build under existing shared requirements: recover venue-specific endpoint lineage and source versions, eligible-trade/correction semantics, original arrival clocks and complete action/adjacent-calendar receipts. Supply official endpoint or separately labeled VWAP adapters, with missing-open/fallback handling and exact accepted-engine parity checks. Lost historical arrival evidence requires prospective capture or another qualified source; no source-owner job, paid acquisition or live configuration is started.

Before replay, freeze the actual scanner, decision/later-entry/exit, scanner-only matched control and one stock/market policy, four context states, original weights and vetoed cash, avoided losses and sacrificed winners net costs, supported chronology/uncertainty and an explicitly registered budget. Existing M1/M2 evidence and exhausted M2 budget remain unchanged. Historical strategy trials/final evaluations zero; final access disabled. Full SR-033 stays open at partial Test, M7 planned/unreleased; agent inspection under owner waiver, no independent approval claimed. Next ranked source qualification: SR-043 low-volatility/beta.
