# 25. Dalio All-Weather / Risk Parity — Twist: RP-REG2

> **Library:** Sigmatiq Strategy Library V2 | **Bucket:** Portfolio / Macro | **Style:** Asset allocation
> **Instruments:** Global stocks, bonds, commodities, gold, TIPS | **Typical holding period:** Months to years (quarterly rebalance) | **Complexity (1–5):** 3 | **Evidence grade (A–C):** B+
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise.

## 1. Origin & lineage

**Ray Dalio / Bridgewater All Weather (1996).** Risk-balanced allocation across growth/inflation environments (30% stocks, 40% long bonds, 15% intermediate, 7.5% gold/commodities — the retail rendering; institutional version levers to equalize risk). Lineage: Markowitz → Qian risk-parity formalization → Bridgewater implementation → retail Risk Parity / Permanent Portfolio cousins. Dalio *Principles* + All Weather whitepapers + Behind-the-numbers factsheets are the primary record.

## 2. The original rules (as published)

- **All Weather weights (retail):** 30% stocks / 40% long Treasuries / 15% intermediate / 7.5% gold / 7.5% commodities; rebalance quarterly/annually.
- **Risk-parity core (Qian):** equal risk contribution (ERC): w_i * marginal-risk equal across sleeves; lever the diversified mix to target vol.
- **Environment framing:** hold assets for rising/falling growth × rising/falling inflation quadrants.
- **What varies:** leverage (retail unlevered vs institutional levered), commodity/gold split, rebalance frequency.

## 3. Why it works — mechanism & evidence

**Mechanism.** Risk diversification across macro quadrants + volatility harvesting via rebalancing: equal risk weights prevent equity-concentration drawdowns; uncorrelated sleeves (long duration in deflation scares, gold/commodities in inflation) offset at different cycle turns; rebalancing sells rich, buys cheap mechanically.

**Supporting evidence (all attributed, none ours):**

- Bridgewater reports All Weather 1996–present risk-adjusted persistence through multiple cycles (firm-published; fee/vehicle details matter — read skeptically).
- Risk-parity literature (Qian; Asness–Frazzini–Pedersen ' explicitly) documents leverage-aversion premium capture via diversified risk balance.
- 2008 episode: risk-parity drawdowns far smaller than 60/40 (widely replicated fact).

**Contradictory / decay evidence:**

- 2022 stock/bond correlation flip broke the diversifier: long bonds fell with stocks; unlevered All Weather suffered double-digit drawdowns (the documented failure).
- Post-2010 low-rate era flattered duration-heavy mixes; forward returns from higher-rate starts differ structurally.
- Leverage + illiquidity spirals hit levered parity in March 2020 (basis/cash squeezes forced de-risking).

**Synthesis.** Risk parity is the correct equity-concentration antidote with one known poison (joint stock/bond selloffs). Our twist adds drawdown control plus inflation/growth nowcast tilts instead of static weights.

## 4. The twist: RP-REG2

1. **ERC core (targets equity concentration):** risk-balance stocks/rates/commodities/gold at equal ex-ante vol contribution, monthly re-estimated (not fixed 30/40/15/7.5).
2. **CPPI drawdown control (targets 2022-style joint selloffs):** floor at 85% of trailing-1Y high; scale exposure by (cushion/floor-distance); never override manually.
3. **Growth/inflation nowcast tilts (targets static-weight drift):** ±10pp tilts from PMI-vs-trend and inflation-surprise indices (mechanical, published rules).
4. **Duration-ladder rates (targets long-bond cliffs):** rates sleeve as 2–10Y ladder, not 20Y+ bullet (convexity without the 2022 cliff).
5. **Vol-target overlay (targets leverage spirals):** 8% portfolio vol target; delever automatically when realized vol exceeds 12%.

## 5. Full specification of the twist variant

**Universe.** Global equities (VT/VTI/VEA), Treasuries ladder (SHY/IEF/TLT blend), TIPS, gold (GLD), broad commodities (DBC/PDBC).

**Data requirements.** Monthly total-return + CPI/PPI/PMI vintages, realized-vol estimator, rebalance calendar.

**Signal definitions (formulas).**

- ERC weights from 60-day covariance; nowcast scores z-scored; CPPI multiplier m=3, floor 85%; vol-target 8%.

**Entries.**

Quarterly rebalance to ERC ± tilts; CPPI/vol overlays applied monthly (no intra-month trading except floor breach).

**Exits.**

Rebalance-driven only; floor breach = de-risk to floor asset (bills) until cushion rebuilds.

**Position sizing.**

Unlevered retail default (1.0x); institutional 1.2–1.5x only with vol-target governor engaged.

**Risk limits.**

Floor hard; vol-target hard; single-sleeve 50% cap; 2022-regime monitor (stock/bond correlation > 0.3 = tilt to gold/commodities).

**Cost model & capacity.**

ETF expense + 2–5 bps/rebalance; taxes: rebalance in tax-advantaged wrappers preferred (disclosed).

**Parameters to validate (plateau, not peak):** ERC window {30, 60, 90}d; floor {80%, 85%, 90%}; vol target {6%, 8%, 10%}; tilt {±5, ±10, ±15}pp.

## 6. Failure modes & regime dependence

Joint stock/bond/commodity selloffs (1970s + 2022 family); nowcast whipsaw; vol-target lag in gap regimes.

## 7. Validation protocol

**Status: no local backtest exists yet.** This library contains zero proprietary results; everything above is literature.

- **Data:** Monthly total-return 1970–present; CPI vintages; ETF backfill disclosed pre-inception.
- **Splits:** chronological across cycles (must include 2008, 2020, 2022); no random k-fold; walk-forward anchored.
- **Cost/slippage model:** ETF expense + 2–10 bps/rebalance; options spreads + borrow where used; futures roll costs; stress 2x/3x.
- **Pitfalls:** look-ahead in index/constituent vintages; survivorship; same-bar ambiguity on rotation days; corporate actions; options expiry/pin.
- **Robustness:** plateau heatmaps; bootstrap CIs; placebo allocations (~zero edge); yearly + VIX/inflation-regime sub-samples; best-year removal.
- **Acceptance criteria:** OOS risk-adjusted dominance vs stated benchmark net of 2x costs; max DD within 1.2x of in-sample; positive in >= 60% of 3-year windows.

## 8. Sources read (annotated)

1. **Bridgewater All Weather whitepapers/factsheets.** https://www.bridgewater.com — environment framing + retail weights. Firm-authored.
2. **Qian on risk parity / ERC.** Search "Risk Parity Fundamentals Qian" — ERC math. Known via secondary citation.
3. **Asness, Frazzini & Pedersen on leverage aversion.** Journal of Finance — risk-balance premium. Known via secondary citation.

## 9. Further reading

- Dalio *Principles* macro-cycle chapters.
- 2022 risk-parity post-mortems.
- Permanent Portfolio (Browne) comparison notes.
