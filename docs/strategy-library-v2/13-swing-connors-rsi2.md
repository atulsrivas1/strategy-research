# 13. Connors RSI-2 Mean Reversion — Twist: RSI2-VX2

> **Library:** Sigmatiq Strategy Library V2 | **Bucket:** Swing (1–10d) | **Style:** Mean reversion
> **Instruments:** Liquid US equities, SPY/QQQ | **Typical holding period:** 1–5 days | **Complexity (1–5):** 2 | **Evidence grade (A–C):** B
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise.

## 1. Origin & lineage

**Larry Connors / Cesar Alvarez.** *Short Term Trading Strategies That Work* (2008) + Connors Research Quantified Strategies: the RSI-2 pullback system — buy stretched pullbacks in uptrends (close > 200-day SMA, RSI-2 < 10), exit on close above 5-day SMA. Alvarez's published extensions added VIX/streak and intraday-timing variants. Practitioner base: thousands of retail/systematic swing traders run RSI-2 screens (FinViz/TC2000 presets).

## 2. The original rules (as published)

- **Setup:** close above 200-day SMA (uptrend filter).
- **Trigger:** RSI-2 closes under 10 (Connors reports deeper is better: sub-5 variants).
- **Entry:** next open / on close; Alvarez variants scale in over 2–3 down closes.
- **Exit:** close above 5-day SMA (first strength), no fixed stop in the original (time/mean exit IS the stop) — practitioner adds use 5–8% hard stops.
- **Disagreement:** RSI threshold (5 vs 10), SMA exit (3 vs 5 day), whether to require consecutive down closes.

## 3. Why it works — mechanism & evidence

**Mechanism.** Short-horizon overreaction + liquidity-demand snap-back: multi-day pullbacks in intact uptrends reflect impatient selling into patient bids; 2-period RSI isolates the stretch; the uptrend filter keeps the trade with the higher-timeframe drift.

**Supporting evidence (all attributed, none ours):**

- Connors–Alvarez report high win-rates (~70%+) on the exit-above-5SMA rule across US equities 1995–2007 (authors' backtests; costs lightly modeled — weight accordingly).
- Short-horizon reversal literature (Jegadeesh 1990; Lehmann 1990) finds 1-week reversal portfolios earn positive spreads (academic, different rule, same family).
- Practitioner replications (Alvarez blog updates) show the edge concentrates in low-VIX uptrends.

**Contradictory / decay evidence:**

- No-stop original suffers gap-through-trend tails (2008/2020 pullbacks that kept falling); drawdowns exceed the marketed win-rate comfort.
- Post-2010 replications show decay vs 1990s–2000s (higher efficiency, more mean-reversion algos competing).
- Threshold-mining risk: RSI(2)<10 vs <5 vs streak variants — published 'best' varies by sample.

**Synthesis.** RSI-2 is the cleanest short-term mean-reversion prototype: real snap-back tendency, fragile in trend breaks. Needs a trend-quality gate, a hard stop, and VIX-aware sizing — exactly our twist.

## 4. The twist: RSI2-VX2

1. **VIX term-structure gate (targets bear-pullback traps):** trade only when VIX < 25 and term structure in contango (front < 3M); otherwise halve size or stand down.
2. **Trend-quality filter (targets falling knives):** require SMA50 > SMA200 and 20-day slope positive (not just close > SMA200).
3. **Hard stop + time-stop (targets no-stop tails):** 0.75x ATR(10) stop + 5-day time exit even if 5SMA rule unmet.
4. **Streak scaling (targets single-dip timing):** half size on first RSI-2 < 10, add half on second consecutive sub-10 close (Alvarez-style, capped).
5. **ATR trailing exit overlay (targets giveback):** after +1 ATR profit, trail at 0.5 ATR; 5SMA exit remains primary.

## 5. Full specification of the twist variant

**Universe.** Russell 1000 non-OTC, price > $10, ADV > $10M; SPY/QQQ ETF sleeve. Long-only (shorts are a separate spec).

**Data requirements.** Daily bars + SMA200/50, RSI-2, ATR(10), VIX + VIX3M term, borrow/dividend calendar.

**Signal definitions (formulas).**

- RSI-2 (Wilder, 2-period) on closes; trigger close < 10 (add leg second close < 10).
- Trend: close > SMA200 AND SMA50 > SMA200 AND slope20 > 0. VIX gate as above.

**Entries.**

Next open after trigger (half); second consecutive trigger adds half; stop 0.75x ATR(10) from entry.

**Exits.**

Close above 5-day SMA (all out); ATR trail after +1R; 5-day time-stop; earnings within 3 days vetoes entry.

**Position sizing.**

0.75% risk cap per name; portfolio heat max 6 concurrent; VIX > 25 halves size.

**Risk limits.**

Earnings blackout 3d; single-name 2% equity cap; market-regime halt (VIX backwardation + SPY < SMA200 = no new entries).

**Cost model & capacity.**

$0.003/share + 5 bps slippage assumed; capacity large (liquid large caps, days-long holds).

**Parameters to validate (plateau, not peak):** RSI {5, 10, 15}; SMA exit {3, 5}; stop {0.5, 0.75, 1.0 ATR}; time-stop {3, 5, 7}d.

## 6. Failure modes & regime dependence

Waterfall declines (trend filter lags); VIX-regime flips mid-hold; earnings gaps through stops; crowded RSI-2 screens fading the same dip (simultaneous exits).

## 7. Validation protocol

**Status: no local backtest exists yet.** This library contains zero proprietary results; everything above is literature.

- **Data:** Daily 2000–present point-in-time (incl. delisted), VIX history, earnings dates, splits/dividends.
- **Splits:** chronological train / validation / test; no random k-fold. Purged/embargoed where labels overlap; walk-forward anchored.
- **Cost/slippage model:** $0.003–$0.005/share all-in or 5–10 bps per side; borrow costs on shorts; limit-fill haircut 70% on touches; stress 2x/3x.
- **Pitfalls:** survivorship (point-in-time universe incl. delisted); look-ahead in fundamentals/earnings timestamps; same-bar ambiguity (stop-first); corporate actions (splits/dividends adjusted with point-in-time factors).
- **Robustness:** plateau heatmaps; bootstrap CIs; placebo (randomized entries, same exits — must be ~zero); yearly + VIX-quintile sub-samples; best-year removal.
- **Acceptance criteria:** OOS Sharpe >= 0.8 net of 2x costs; PF >= 1.2; per-trade t >= 2; max DD <= 2x in-sample; positive in >= 60% of years.

## 8. Sources read (annotated)

1. **Connors & Alvarez, *Short Term Trading Strategies That Work* (2008).** Publisher: https://www.tradingmarkets.com — RSI-2 rules + author backtests. Book-level knowledge.
2. **Jegadeesh (1990) on short-term reversal.** Journal of Finance — 1-week reversal evidence. Known via secondary citation.
3. **Connors Research / Alvarez blog updates.** Search "Connors RSI-2 VIX" — regime extensions. Practitioner-authored; illustrative.

## 9. Further reading

- Lehmann (1990) reversal portfolios.
- Alvarez mean-reversion timing overlays.
- Quantpedia RSI-2 replication notes.
