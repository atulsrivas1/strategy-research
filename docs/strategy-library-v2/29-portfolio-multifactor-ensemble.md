# 29. Multi-Factor Equity Ensemble — Twist: FLEX2

> **Library:** Sigmatiq Strategy Library V2 | **Bucket:** Portfolio / Macro | **Style:** Factor
> **Instruments:** Global equities (long-only + 130/30 variants) | **Typical holding period:** Monthly rebalance, years-long | **Complexity (1–5):** 5 | **Evidence grade (A–C):** A-
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise.

## 1. Origin & lineage

**Fama–French → Asness/AQR lineage.** Fama–French 3/5-factor (1993/2015) + Carhart momentum + Novy-Marx/Asness quality/profitability → AQR value-momentum-quality ensemble (Asness–Frazzini–Pedersen; *Efficient Frontier*/*AQR whitepapers*). Practitioner standard: diversified factor sleeves with vol targeting and crowding overlays. Our twist adds vol-regime sleeve weights + a constant-ex-ante-vol governor.

## 2. The original rules (as published)

- **Sleeves:** value (HML/E-P, EBIT/TEV), momentum (12-1), quality/profitability (gross profits/assets, low accruals), low-vol/betting-against-beta.
- **Construction:** rank z-scores, cap-weighted or equal-risk sleeves, NYSE breakpoints, monthly/quarterly rebalance.
- **AQR rendering:** value + momentum + quality with risk-balanced sleeves and transaction-cost-aware turnover.
- **What varies:** factor definitions (a dozen value ratios), neutralization (sector/country), rebalance speed.

## 3. Why it works — mechanism & evidence

**Mechanism.** Distinct premia (distress/behavioral value, continuation momentum, franchise quality, leverage-aversion low-vol) with low cross-correlation combine into a smoother ensemble; premia persist via risk + behavior + limits-to-arbitrage; turnover/crowding management determines net capture.

**Supporting evidence (all attributed, none ours):**

- Fama–French / Carhart document value/size/momentum premia across decades/markets (academic core).
- Asness et al. document value-momentum-quality complementarity and ensemble Sharpe gains (authors' constructions).
- Frazzini–Pedersen betting-against-beta + Novy-Marx profitability extend the sleeve set (academic).

**Contradictory / decay evidence:**

- Value's post-2007 drawdown (growth dominance) and momentum's 2009/2020 crashes show multi-year single-sleeve pain; ensembles still draw down when sleeves correlate (2018/2020).
- Post-publication decay + crowding debates (McLean–Pontiff: ~35–50% post-publication decay across anomalies).
- Turnover/taxes erase much of high-churn factor paper edge in taxable accounts.

**Synthesis.** The ensemble survives where single factors die: diversify sleeves, govern turnover, watch crowding, hold ex-ante vol constant — and expect value to test faith for a decade.

## 4. The twist: FLEX2

1. **Vol-regime sleeve weights (targets static-mix fragility):** momentum weight cut 50% when market vol > 2x median (crash-prone); quality/low-vol weight doubled in same regime.
2. **Crowding overlay (targets quant-quake):** halve value+momentum when pair-wise factor crowding (short interest + valuation spread compression) exceeds 80th percentile.
3. **Constant ex-ante vol (targets risk drift):** 10% book-vol target rebalanced monthly; leverage floats mechanically.
4. **Turnover budget (targets churn bleed):** 100%/year single-side max; signal-hysteresis bands (0.2 z) suppress micro-rotations.
5. **Tax-aware sleeve placement (targets taxable erosion):** momentum/low-vol (high turnover) in tax-advantaged; value/quality in taxable; 130/30 only where borrow/prime allows.

## 5. Full specification of the twist variant

**Universe.** Developed + EM equities (MSCI breadth); NYSE breakpoints; no microcaps (liquidity veto).

**Data requirements.** Fundamentals point-in-time, prices, borrow, crowding proxies (valuation spreads, short interest), turnover monitor.

**Signal definitions (formulas).**

- Sleeve z-scores (value/mom/quality/low-vol); crowding percentile; vol-regime flag; ex-ante vol estimate.

**Entries.**

Monthly rebalance to voted sleeve weights with hysteresis; crowding/vol overlays applied at rebalance (no intra-month except vol-spike halt).

**Exits.**

Rotation-driven; vol-spike halt halves momentum intra-month (sole exception).

**Position sizing.**

10% ex-ante vol; sleeve risk-balanced (equal vol contribution baseline ± regime tilts).

**Risk limits.**

Sleeve concentration caps; crowding halt-halving; turnover budget hard; EM 30% max.

**Cost model & capacity.**

5–15 bps/side + borrow on 130/30 shorts; turnover-budgeted; taxes modeled (placement disclosed).

**Parameters to validate (plateau, not peak):** Vol target {8%, 10%, 12%}; crowd pct {70th, 80th, 90th}; hysteresis {0.1, 0.2, 0.3}z; turnover {80%, 100%, 150%}.

## 6. Failure modes & regime dependence

Sleeve-correlation spikes (all factors sell together); decade-long value droughts; crowding unwinds; turnover overruns in whipsaw years.

## 7. Validation protocol

**Status: no local backtest exists yet.** This library contains zero proprietary results; everything above is literature.

- **Data:** Global equities + fundamentals point-in-time 1990–present; crowding proxies; borrow; delisted included.
- **Splits:** chronological across cycles (must include 2008, 2020, 2022); no random k-fold; walk-forward anchored.
- **Cost/slippage model:** ETF expense + 2–10 bps/rebalance; options spreads + borrow where used; futures roll costs; stress 2x/3x.
- **Pitfalls:** look-ahead in index/constituent vintages; survivorship; same-bar ambiguity on rotation days; corporate actions; options expiry/pin.
- **Robustness:** plateau heatmaps; bootstrap CIs; placebo allocations (~zero edge); yearly + VIX/inflation-regime sub-samples; best-year removal.
- **Acceptance criteria:** OOS risk-adjusted dominance vs stated benchmark net of 2x costs; max DD within 1.2x of in-sample; positive in >= 60% of 3-year windows.

## 8. Sources read (annotated)

1. **Fama & French 3/5-factor; Carhart momentum.** Journals — sleeve premia. Known via secondary citation.
2. **Asness, Frazzini & Pedersen / AQR whitepapers.** https://www.aqr.com — ensemble + risk-balanced construction. Firm-authored.
3. **McLean & Pontiff on post-publication decay.** Journal of Finance — ~decay framing. Known via secondary citation.

## 9. Further reading

- Novy-Marx profitability; Frazzini–Pedersen BAB.
- Factor-crowding measurement papers.
- Tax-efficient factor implementation notes.
