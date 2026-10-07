# 15. Pairs Trading / Statistical Arbitrage — Twist: KALMAN-B2

> **Library:** Sigmatiq Strategy Library V2 | **Bucket:** Swing (1–10d) | **Style:** Relative value
> **Instruments:** US equities, sector ETFs | **Typical holding period:** 2–10 days | **Complexity (1–5):** 5 | **Evidence grade (A–C):** B
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise.

## 1. Origin & lineage

**Morgan Stanley lineage.** Nunzio Tartaglia's 1980s pairs desk (Gerry Bamberger) → Gatev–Goetzmann–Rouwenhorst (2006) distance-method formalization → Avellaneda–Lee (2010) ETF-factor models → Kalman/cointegration practitioner standard (Vidyamurthy; Chan *Algorithmic Trading*). Desks today run sector-neutral baskets, not single pairs; our twist is that basket version.

## 2. The original rules (as published)

- **GGR (2006):** match pairs by minimized 12-month price-distance; trade 2-sigma divergences of the normalized spread; hold to convergence or 6 months; 1962–2002 US equities profitable pre-costs (authors' claim, decayed after publication).
- **Cointegration (Vidyamurthy/Chan):** ADF-tested hedge ratio; z-score entry/exit; stop on cointegration breakdown.
- **Avellaneda–Lee:** ETF-implied principal-component residuals; trade idiosyncratic mean reversion.
- **What desks actually do (unpublished):** baskets, Kalman hedge ratios, borrow-aware shorts, hard half-life gates.

## 3. Why it works — mechanism & evidence

**Mechanism.** Common-factor exposure explains most comovement; residuals reflect transient liquidity/attention imbalances between close substitutes; hedged baskets isolate the idiosyncratic snap-back while staying sector/market neutral.

**Supporting evidence (all attributed, none ours):**

- GGR (2006) report ~11% annualized excess pre-costs 1962–2002, decaying post-publication (authors' own decay note).
- Avellaneda–Lee (2010) report ETF-factor residuals trade profitably 1997–2007 pre-costs (authors' sample).
- Chan practitioner texts document live pairs/stat-arb Sharpe compression from ~2 to ~1 as crowds entered (practitioner consensus).

**Contradictory / decay evidence:**

- Post-2002 GGR replication Sharpe roughly halves; 2007 quant-quake and 2020 factor-breakdown episodes show crowded unwind risk.
- Single-pair cointegration breaks on corporate events (M&A, fraud, regime change) — the classic pair-death.
- Borrow costs/hard-to-borrow on the short leg erase paper spreads in small caps.

**Synthesis.** Single-pair distance trading is mostly decayed; the surviving form is sector-neutral residual baskets with adaptive hedge ratios and explicit breakdown exits.

## 4. The twist: KALMAN-B2

1. **Sector-neutral baskets (targets single-pair death):** 5–15 longs vs 5–15 shorts per sector basket; no single-pair concentration.
2. **Kalman hedge ratios (targets static-ratio drift):** time-varying beta per name; freeze trading when Kalman innovation variance spikes (ratio unstable).
3. **Half-life regime gate (targets non-stationary spreads):** trade only when estimated OU half-life in [2, 10] days; otherwise stand down (trending, not reverting).
4. **Event veto (targets corporate-breakdown):** no new pairs 5 days around earnings/M&A/FDA for either leg.
5. **Crowding overlay (targets quant-quake):** halve gross when basket 5-day correlation to generic value/reversal factors exceeds 0.7.

## 5. Full specification of the twist variant

**Universe.** Russell 1000 + 9 sector ETFs; price > $10, borrow-available, no earnings within 5d.

**Data requirements.** Daily bars, borrow-rate feed, corporate calendar, sector map, ETF holdings for factor neutralization.

**Signal definitions (formulas).**

- Residual via sector-ETF regression (60-day) or PCA-3; Kalman beta; OU half-life from AR(1) on spread; z = resid/sigma_60d.
- Enter |z| >= 2.0 with half-life gate; exit |z| <= 0.5; stop |z| >= 4.0 (breakdown, not add).

**Entries.**

Dollar- and beta-neutral basket adds on z-thresholds; scale in halves at 2.0/2.5; no adds past 3.0.

**Exits.**

Convergence 0.5; breakdown stop 4.0; 10-day time-stop; event-day forced flatten on either leg.

**Position sizing.**

0.3% risk per pair, 3% gross per basket; borrow-cost-adjusted (skip if borrow > 5% annualized eats 50% of expected).

**Risk limits.**

Sector/dollar neutrality bands; single-name 1% cap; quant-stress halt (basket drawdown > 3 sigma → halve, > 5 sigma → flat).

**Cost model & capacity.**

5–10 bps/side + borrow; capacity moderate (baskets scale better than single pairs; still capped in small caps).

**Parameters to validate (plateau, not peak):** z {1.5, 2.0, 2.5}; half-life {1–7, 2–10, 3–15}d; lookback {30, 60, 90}d; stop {3, 4, 5} sigma.

## 6. Failure modes & regime dependence

Factor-breakdown months; M&A/event breaks; borrow squeezes; crowded-reversal unwinds (all baskets mean-revert the wrong way together).

## 7. Validation protocol

**Status: no local backtest exists yet.** This library contains zero proprietary results; everything above is literature.

- **Data:** Daily point-in-time 2000–present incl. delisted; borrow history; corporate calendar; ETF holdings vintages.
- **Splits:** chronological train / validation / test; no random k-fold. Purged/embargoed where labels overlap; walk-forward anchored.
- **Cost/slippage model:** $0.003–$0.005/share all-in or 5–10 bps per side; borrow costs on shorts; limit-fill haircut 70% on touches; stress 2x/3x.
- **Pitfalls:** survivorship (point-in-time universe incl. delisted); look-ahead in fundamentals/earnings timestamps; same-bar ambiguity (stop-first); corporate actions (splits/dividends adjusted with point-in-time factors).
- **Robustness:** plateau heatmaps; bootstrap CIs; placebo (randomized entries, same exits — must be ~zero); yearly + VIX-quintile sub-samples; best-year removal.
- **Acceptance criteria:** OOS Sharpe >= 0.8 net of 2x costs; PF >= 1.2; per-trade t >= 2; max DD <= 2x in-sample; positive in >= 60% of years.

## 8. Sources read (annotated)

1. **Gatev, Goetzmann & Rouwenhorst (2006), "Pairs Trading."** https://papers.ssrn.com (search "Pairs Trading GGR") — distance method + decay note. Known via secondary citation.
2. **Avellaneda & Lee (2010), "Statistical arbitrage in the US equities market."** https://papers.ssrn.com — ETF-factor residuals. Known via secondary citation.
3. **Chan, *Algorithmic Trading* (2013, Wiley).** https://www.wiley.com — cointegration/Kalman practice + Sharpe-compression note. Book-level knowledge.

## 9. Further reading

- Vidyamurthy *Pairs Trading* (cointegration detail).
- 2007 quant-quake post-mortems (Khandani–Lo).
- Kalman-filter pairs notebooks (practitioner).
