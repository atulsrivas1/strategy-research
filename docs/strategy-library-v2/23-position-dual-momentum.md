# 23. Dual Momentum (Time-Series + Cross-Sectional) — Twist: VMOM2

> **Library:** Sigmatiq Strategy Library V2 | **Bucket:** Position (weeks–months) | **Style:** Momentum
> **Instruments:** Global equities, bonds, REITs, commodities (ETF proxies) | **Typical holding period:** 1–12 months | **Complexity (1–5):** 3 | **Evidence grade (A–C):** A
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise.

## 1. Origin & lineage

**Gary Antonacci (2012–14).** *Dual Momentum Investing*: combine time-series (absolute: own vs T-bills) + cross-sectional (relative: US vs ACWI) momentum on 12-month lookbacks, monthly rebalance; reported 1974–2013 backtests beating buy-hold with lower drawdowns (author's computation). Academic roots: Jegadeesh–Titman (1993) cross-sectional; Moskowitz–Ooi–Pedersen (2012) time-series; Barroso–Santa-Clara (2015) volatility management. Practitioner standard: Faber GTAA / Keller DAA cousins.

## 2. The original rules (as published)

- **Relative:** hold the stronger of US vs ex-US over trailing 12 months.
- **Absolute:** hold it only if its 12-month excess over T-bills is positive; else T-bills/bonds.
- **Rebalance:** monthly; 12-month formation, 1-month holding (Faber variants use 1/3/6/12 composites).
- **What varies:** lookback (6 vs 12), safe asset (bills vs bonds vs cash-plus), universe breadth.

## 3. Why it works — mechanism & evidence

**Mechanism.** Continuation from slow information diffusion + herding + confirmation over months; absolute leg adds crash protection by exiting to bills when both legs weaken (time-series filter); volatility clustering makes vol-scaling improve risk-adjusted capture.

**Supporting evidence (all attributed, none ours):**

- Antonacci reports 1974–2013 dual-momentum Sharpe/drawdown dominance vs buy-hold (author's backtest; costs lightly modeled).
- Jegadeesh–Titman (1993) + MOP (2012) document cross-sectional and time-series momentum across assets/decades (academic core, A-grade family).
- Barroso–Santa-Clara (2015) show vol-managed momentum roughly doubles Sharpe vs raw (authors' sample; debated out-of-sample).

**Contradictory / decay evidence:**

- Momentum crashes (2009, 2020 reversals) hit dual momentum hard — absolute leg lags the turn.
- Post-2010 US-vs-exUS persistence made the relative leg a buy-and-hold-US proxy (regime luck, not timing skill — critics' note).
- Monthly rebalance + 12-month lookback whipsaws in fast reversals (V-shaped 2020).

**Synthesis.** Dual momentum is the most academically supported rule in this library; its weaknesses are crash-lag and single-lookback rigidity. Our twist adds vol management, quality filtering, and a crash flag.

## 4. The twist: VMOM2

1. **Volatility-managed sizing (targets crash-lag):** scale equity exposure by 12%/realized-6M-vol (Barroso–Santa-Clara), capped 1.0x, floored 0.25x.
2. **52-week-high quality filter (targets weak-relative winners):** relative winner must also be within 10% of 52-week high, else hold bills (avoids value-trap relatives).
3. **Crash flag (targets momentum crashes):** if trailing-3M market vol > 2x 3-year median AND 12M formation spread inverts, force bills regardless of absolute signal.
4. **Composite lookback (targets single-window whipsaw):** vote 6/9/12-month formation; require 2-of-3 agreement for equity leg.
5. **Bond-ladder safe asset (targets bill-drag):** safe leg = 1–3Y Treasury ladder, not bills (carry without duration risk).

## 5. Full specification of the twist variant

**Universe.** US (SPY), ex-US (ACWI/VEA), aggregate bonds (AGG/SHY ladder), T-bills; optional REIT/commodity sleeves.

**Data requirements.** Monthly total-return indices + T-bill series, 52-week highs, realized-vol estimator, rebalance calendar.

**Signal definitions (formulas).**

- Formation excess over bills per lookback; 2-of-3 vote; 52-week proximity; vol-scale factor; crash-flag booleans.

**Entries.**

Monthly rebalance into voted winner (or ladder if absolute fails/flag fires); 1-month minimum hold (no mid-month trades).

**Exits.**

Monthly rotation only; crash flag = immediate bills at next close (sole intra-month exception).

**Position sizing.**

Vol-scaled 0.25–1.0x equity; remainder in ladder; rebalance bands 5% (no micro-trades).

**Risk limits.**

Crash flag hard; single-sleeve 100% cap (no leverage); regime note: expect multi-year US-concentration stretches (by design).

**Cost model & capacity.**

ETF expense + 2–5 bps/rebalance; taxes: monthly rotation is taxable — prefer IRA/401k wrappers (disclosed).

**Parameters to validate (plateau, not peak):** Lookbacks {6, 9, 12} voting; vol target {10%, 12%, 15%}; proximity {5%, 10%, 15%}; crash mult {1.5, 2.0, 2.5}x.

## 6. Failure modes & regime dependence

V-shaped reversals (sell-the-low then miss the rip); decade-long single-region dominance (relative leg idle); vol-target lag in gap regimes.

## 7. Validation protocol

**Status: no local backtest exists yet.** This library contains zero proprietary results; everything above is literature.

- **Data:** Monthly total-return 1970–present; bills/bonds history; ETF proxies post-inception with index backfill disclosed.
- **Splits:** chronological train / validation / test across full market cycles (must include a bear); no random k-fold; walk-forward anchored.
- **Cost/slippage model:** 5–15 bps/side + borrow on shorts; dividends/splits point-in-time; stress 2x/3x.
- **Pitfalls:** survivorship (delisted included); look-ahead in fundamentals (report-date, not period-end); same-bar ambiguity (conservative fills); corporate actions.
- **Robustness:** plateau heatmaps; bootstrap CIs; placebo (random entries, same exits ~zero); yearly + drawdown-regime sub-samples; best-year removal.
- **Acceptance criteria:** OOS CAGR > benchmark with lower max DD (trend) or Sharpe >= 1.0 (drift); per-trade t >= 2; positive in >= 60% of years; survives 2008/2020/2022 sub-samples.

## 8. Sources read (annotated)

1. **Antonacci, *Dual Momentum Investing* (2014).** https://www.optimalmomentum.com — rules + 1974–2013 backtests. Book/site-level knowledge.
2. **Jegadeesh & Titman (1993); Moskowitz, Ooi & Pedersen (2012).** Journals — cross-sectional + time-series momentum. Known via secondary citation.
3. **Barroso & Santa-Clara (2015), "Momentum has its moments."** https://papers.ssrn.com — vol management. Known via secondary citation.

## 9. Further reading

- Faber GTAA / Keller DAA (tactical cousins).
- Momentum-crash literature (Daniel–Moskowitz).
- 52-week-high (George–Hwang) overlay notes.
