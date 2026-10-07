# 20. Turtle Trend Following — Twist: TURTLE-X2

> **Library:** Sigmatiq Strategy Library V2 | **Bucket:** Position (weeks–months) | **Style:** Trend / Donchian
> **Instruments:** Futures + FX + liquid equities | **Typical holding period:** Weeks to months | **Complexity (1–5):** 4 | **Evidence grade (A–C):** B+
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise.

## 1. Origin & lineage

**Richard Dennis / William Eckhardt Turtles (1983–88).** Dennis (pits-to-$200M legend) bet Eckhardt that trading could be taught; ~20 novices trained on Donchian-breakout + ATR-sizing rules traded firm capital. Reported group profits (~$175M aggregate, trader-reported; Curtis Faith *Way of the Turtle*, 2007; Michael Covel *Complete TurtleTrader*). Eckhardt's logic: robust medium-term trend capture with volatility-normalized risk across uncorrelated futures.

## 2. The original rules (as published)

- **System 1:** 20-day Donchian break entry; 10-day break exit; last-break-failure skip filter (skip if prior break won — take all System 2 breaks).
- **System 2:** 55-day break entry; 20-day exit (always taken).
- **Stop:** 2 ATR (20-day EMA of TR); unit = 1% risk / (2 ATR * $/point).
- **Adds:** +1 unit per +0.5 ATR favorable; max 4 units single market, 6 correlated, 10 direction, 12 total.
- **Filters:** liquidity (no thin markets), no earnings-single-stock nuance (futures-first design).

## 3. Why it works — mechanism & evidence

**Mechanism.** Fat-tailed price trends + volatility-normalized pyramiding: Donchian breaks enter nascent trends; ATR sizing equalizes risk across silos; adds concentrate in winners; the long option-like payoff (many small stops, few large runners) matches commodity/futures return kurtosis.

**Supporting evidence (all attributed, none ours):**

- Turtle aggregate profits reported by Faith/Covel (trader-reported; no independent audit — weight as strong practitioner claim).
- Hurst–Ooi–Pedersen (2017) document trend-following premia across 100+ years/assets (academic family evidence).
- SG CTA / BTOP50 long-run positive skew with crisis alpha (index fact, manager-aggregated).

**Contradictory / decay evidence:**

- Post-2010 trend Sharpe compressed (crowding + central-bank smoothing + faster reversals); 2011–2019 whipsaw strings are the documented drought.
- Donchian parameters are curve-fit-prone; System 1 vs 2 choice swings results by sample.
- Equity-only Turtle underperforms futures-diversified Turtle (asset-mix dependence).

**Synthesis.** Turtle rules remain the cleanest trend prototype; their modern failure is correlated whipsaw + fixed lookbacks. Our twist adapts lookback, caps correlation heat, and adds an equity-curve breaker.

## 4. The twist: TURTLE-X2

1. **Adaptive Donchian (targets fixed-lookback whipsaw):** length = 20d in high-vol regimes, 55d in low-vol (ATR-percentile switch); never optimize per-market.
2. **Correlation-cluster heat caps (targets correlated bleed):** cap 2 units per 0.7+ correlated cluster (energies, metals, rates, equity-index treated as clusters).
3. **Equity-curve circuit breaker (targets drought grind):** halve size after -10% book DD; halt new breaks after -15% until +5% recovery.
4. **Breakout-quality gate (targets chop breaks):** require 20-day ADX > 20 or 60-day autocorrelation positive for System-1 breaks (System-2 always taken, smaller).
5. **Volatility-of-volatility stop (targets gap-through-2ATR):** size *= clip(1 - ATR-spike/3, 0.33, 1.0) when ATR jumps > 50% week-over-week.

## 5. Full specification of the twist variant

**Universe.** 30+ liquid futures (equity-index, rates, FX, energies, metals, ags) + FX majors + ETF proxies where futures unavailable.

**Data requirements.** Daily futures (back-adjusted for signals, unadjusted for PnL), ATR(20), ADX, correlation matrix, roll calendar.

**Signal definitions (formulas).**

- Adaptive length by ATR-percentile regime; break = close beyond Donchian; quality gate ADX/autocorr for S1.
- Unit = 1% / (2 ATR * point value), VoV-scaled; cluster caps applied pre-entry.

**Entries.**

System breaks as published (S1 with skip rule + quality gate; S2 always); adds +0.5 ATR to 4-unit single-market cap within cluster caps.

**Exits.**

10d (S1) / 20d (S2) Donchian exits; 2-ATR stop; circuit-breaker halves/halting overlay.

**Position sizing.**

1% per unit, VoV-scaled; book heat capped by clusters + curve breaker.

**Risk limits.**

Cluster caps; curve breaker; roll-aware (exit/re-enter rules around front-month expiry, no delivery holds).

**Cost model & capacity.**

Commissions + 1-tick/side + roll slippage; capacity large (futures-diversified).

**Parameters to validate (plateau, not peak):** Lengths {10/20/55 adaptive switch points}; ADX {15, 20, 25}; breaker {-8/-12, -10/-15, -12/-20}%.

## 6. Failure modes & regime dependence

Correlated whipsaw (all clusters false-break together); volatility-spike gaps through 2-ATR stops; long flat-drought years testing discipline.

## 7. Validation protocol

**Status: no local backtest exists yet.** This library contains zero proprietary results; everything above is literature.

- **Data:** Futures daily 1990–present back-adjusted + roll calendar; ETF proxies where needed; costs per era.
- **Splits:** chronological train / validation / test across full market cycles (must include a bear); no random k-fold; walk-forward anchored.
- **Cost/slippage model:** 5–15 bps/side + borrow on shorts; dividends/splits point-in-time; stress 2x/3x.
- **Pitfalls:** survivorship (delisted included); look-ahead in fundamentals (report-date, not period-end); same-bar ambiguity (conservative fills); corporate actions.
- **Robustness:** plateau heatmaps; bootstrap CIs; placebo (random entries, same exits ~zero); yearly + drawdown-regime sub-samples; best-year removal.
- **Acceptance criteria:** OOS CAGR > benchmark with lower max DD (trend) or Sharpe >= 1.0 (drift); per-trade t >= 2; positive in >= 60% of years; survives 2008/2020/2022 sub-samples.

## 8. Sources read (annotated)

1. **Faith, *Way of the Turtle* (2007).** Publisher: https://www.mcgrallhill.com (search) — full rule disclosure. Book-level knowledge.
2. **Covel, *The Complete TurtleTrader* (2007).** Publisher pages — experiment history + performance narrative. Book-level knowledge.
3. **Hurst, Ooi & Pedersen, "A Century of Evidence on Trend-Following."** https://papers.ssrn.com — family evidence. Known via secondary citation.

## 9. Further reading

- Eckhardt interview transcripts (risk philosophy).
- SG CTA / BTOP50 methodology notes.
- Fed trend-drought post-mortems (2011–2019).
