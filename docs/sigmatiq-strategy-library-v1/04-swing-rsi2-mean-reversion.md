# 04. RSI-2 Mean Reversion — Twist: RSI2-VX

> **Library:** Sigmatiq Strategy Library | **Bucket:** Swing (1–10 days) | **Style:** Long-only short-term mean reversion (pullback buying)
> **Instruments:** US large/liquid equities and index ETFs (SPY, QQQ, sector ETFs) | **Typical holding period:** 2–7 trading days | **Complexity (1–5):** 2 | **Evidence grade (A–C):** B (strong published in-sample evidence, multiple independent replications, known post-2008 decay)
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise. This library contains no local backtests yet.

---

## 1. Origin & lineage

**Creator / popularizer.** Larry Connors (founder of TradingMarkets.com and Connors Research) and Cesar Alvarez (his Director of Research, ex-Microsoft Excel engineer). The canonical publication is the book *Short Term Trading Strategies That Work* (Connors & Alvarez, 2008, TradingMarkets Publishing, ISBN 978-0-9819239-0-1), chapter 9: "The 2-Period RSI — The Trader's Holy Grail of Indicators?" A full PDF copy of the book was located and read for this document (see §8). Connors' framing philosophy is "buy the fear, sell the greed" — quantified short-term reversion to the mean.

**Intellectual lineage.**

- The RSI itself is J. Welles Wilder's (1978). Connors/Alvarez's contribution was empirical: they report that across ~8 million stock trades (1995–2007) the standard 14-period RSI showed *no* statistical edge, while shortening to 2 periods produced a monotone relationship: the lower the RSI(2), the larger the subsequent 1-day/2-day/1-week outperformance (book, ch. 9).
- The strategy is a systematic formalization of the older "buy pullbacks in an uptrend" discretionary practice. The book's ch. 2–3 document that buying 10-day *lows* in the S&P 500 (1995–2007) made +1048.70 SPX points being invested only 28.81% of the time with 73.5% winners, while buying 10-day *highs* lost ~100 points — the anti-breakout result that motivates all Connors pullback systems.
- The book's ch. 8 extends the idea intraday: buying 10-day-low stocks a further 10% lower on a limit the next day produced +4.35% average 5-day gains with 63% winners (14,939 trades) — the deeper the panic, the larger the edge.
- Connors Research later extended the work into the cumulative-RSI, RSI-25/RSI-4, and TPS (Trend, Pullback, Scaling-in) product lines; the 2008 book remains the primary public source.

**How it is actually used.** Mostly as an index-ETF timing tool (SPY/QQQ) or as a stock-scan pullback entry with a trend filter. Independent replications exist and were read: Jeff Swanson (EasyLanguage Mastery, 2012–2013) re-implemented and parameter-swept it on SPX/ES and ETFs; Quantitativo (2024) re-ran the edge on 21,000+ listed *and delisted* US stocks since 1998 (~2.5M events) and built portfolio variants. Both are annotated in §8.

## 2. The original rules (as published)

### 2.1 The flagship "RSI(2) under 5" S&P strategy (book, ch. 9)

Exact published rules:

1. The S&P 500 index is above its 200-day moving average.
2. The 2-period RSI of the S&P 500 closes below 5.
3. Buy the S&P on the close.
4. Exit when the S&P closes above its 5-period moving average.

Published results (Connors/Alvarez, 1995–2007, S&P 500 index):

| Metric | Value |
| --- | --- |
| Number of signals | 49 |
| Percent correct | 83.6% |
| Total S&P points made | +522.92 |
| Average hold | ≈ 3 trading days |
| Stop loss | None used |

No stop loss is used; the book's ch. 6 ("Rule 5 — Stops Hurt") argues stops systematically degraded performance across hundreds of tested variations on stocks/indices. Their published stop test (stock above 200-day MA closing at a 10-day low; exit = close above 10-day MA or stop x% below entry):

| Stop % | # Trades | Avg % P/L | Avg bars held | % winners |
| --- | --- | --- | --- | --- |
| None | 236,237 | 0.58% | 7.74 | 69.81% |
| 1% | 394,480 | 0.19% | 2.89 | 26.89% |
| 3% | 321,824 | 0.20% | 4.11 | 47.31% |
| 5% | 286,991 | 0.20% | 5.01 | 57.54% |
| 7% | 268,410 | 0.22% | 5.65 | 62.72% |
| 10% | 253,863 | 0.27% | 6.31 | 66.55% |
| 20% | 239,605 | 0.39% | 7.26 | 69.35% |
| 50% | 236,337 | 0.56% | 7.70 | 69.81% |

Reading: every stop level hurt; the tighter the stop, the worse the damage. Even a 50% stop was marginally worse than none.

### 2.2 Cumulative RSI variant (book, ch. 9, pp. 67–72)

Rules:

1. Security above its 200-day MA.
2. Sum the past X days of RSI(2) readings (X = 2 or 3).
3. Buy on close if the cumulative sum < Y.
4. Exit when RSI(2) closes above 65.

Published results (SPY, inception Jan 1993 – Dec 2007):

| Parameters | Signals | % correct | SPY points | Avg gain/trade | Avg hold |
| --- | --- | --- | --- | --- | --- |
| X=2, Y=35 | 50 | 88.0% | +65.53 | +1.26% | 3.7 days |
| X=2, Y=50 | 105 | 85.47% | +105.95 | +1.05% | 3.57 days |
| X=3, Y=45 (ch. 12 variant) | 78 | 79.49% | +779.51 SPX pts | — | < 5 days |

The authors note the Y=50 version "picked up approximately all the SPY gains made in 15 years while only being in the market less than 20% of the time." For individual stocks (cumulative RSI < 10, price > $5, ADV ≥ 250k shares, 1995–2007): 77,068 trades, **69% profitable**, average gain "nearly four times greater than the gains for all stocks for the same holding period."

### 2.3 The underlying edge table (book, ch. 9, Table 9.1 and text)

Benchmark, all stocks above their 200-day MA, 1995–2007 (8M+ trades): 1-day +0.05%, 2-day +0.10%, 1-week +0.25%. Edge by RSI(2) bucket:

| RSI(2) reading | 1-day | 2-day | 1-week |
| --- | --- | --- | --- |
| < 10 | +0.07% | +0.21% | +0.49% |
| < 5 | +0.13% | +0.13% | +0.62% |
| < 2 | +0.21% | +0.47% | +0.79% |
| < 1 | +0.25% | +0.56% | +0.93% |
| > 90 | — | 0.00% | −0.07% |
| > 95 | — | −0.03% | −0.07% |
| > 98 | −0.04% | −0.14% | −0.19% |
| > 99 | −0.09% | −0.23% | −0.29% |

The gradient is monotone in both directions — the core empirical claim of the book.

### 2.4 Related published siblings (same book)

- **Double 7s:** SPY above 200-day MA; buy a 7-day closing low; sell at a 7-day closing high. SPY 1993–2007: 153 trades, 80.4% correct, avg +0.85%/trade, +122.36 points. Also published for QQQQ (68 trades, 79.4%), FXI (26 trades, 76.9%), EWZ (63 trades, 81.0%).
- **VIX Stretches:** SPY above 200-day MA; VIX ≥ 5% above its 10-day MA for 3+ consecutive days → buy close; exit when RSI(2) of SPY > 65. 33 trades, 84.85% correct, +363.90 SPX points.
- **VIX RSI strategy:** RSI(2) of VIX > 90 AND today's VIX open > yesterday's VIX close AND RSI(2) of SPY < 30 → buy close; exit RSI(2) of SPY > 65. 92 trades, 79.35% correct, +879.46 SPX points.
- **TRIN strategy:** SPY above 200-day MA; RSI(2) of SPY < 50; TRIN closes > 1.00 for 3 consecutive days → buy; exit RSI(2) > 65. 90 trades, 75.56% correct; profitable every year but 2002 (−5.11 pts).
- **S&P short side:** SPY below 200-day MA; 4+ consecutive up closes → sell short; cover on close below 5-day MA. 16 trades, 68.75% correct, +169.91 points.
- **VIX 5% rule (ch. 5):** since 1995, the S&P 500 lost money on a net basis in the 5 days following the VIX closing 5%+ *below* its 10-day MA; VIX 5%+ *above* its 10-day MA preceded better-than-2:1 weekly returns vs average.

### 2.5 Known disagreements across sources

- **Entry timing:** the book buys *on the close* of the signal day. Quantitativo (2024) tested buying at the *next open* and reports the SPY version degraded badly (67% total return over 25 years, 157 trades); a reader comment on the article states "entering at the next open significantly reduces the edge," consistent with the author's results. Close-of-signal execution is materially better in the literature but operationally harder (MOC orders on a close-computed signal).
- **Exit:** book uses close > 5-day MA (index version) or RSI(2) > 65 (cumulative version). Swanson (2013) found a 10-day MA exit and RSI threshold 10 (not 5) roughly doubled net profit on SPX ($28.7k → $62.8k, 129 → 227 trades, profit factor 2.97 → 2.74) — i.e., the published parameters are *not* optima in his replication, but all tested threshold values 1–30 and exit-MA lengths 1–30 were profitable, which he reads as robustness.
- **Stops:** the book's "stops hurt" finding is for equities/indices without leverage. Swanson found a $2,000 hard stop (2% of his $100k test account) on the ES futures version *improved* net profit ($62.8k → $66.7k), profit factor (2.74 → 2.93), and win rate (83% → 84%). Disagreement likely explained by instrument (futures gap risk) and his ATR-normalized sizing. Unresolved; our twist takes a middle path (§4b).
- **RSI computation variant:** Wilder's smoothing (the book's convention — the book prints Wilder's formula) vs Cutler's simple-average RSI give materially different RSI(2) values. Sources rarely state which they use. Any replication must fix this choice explicitly; we fix Wilder.

## 3. Why it works — mechanism & evidence

**Mechanism (as argued in the literature).**

1. **Short-horizon overreaction / liquidity provision.** Multi-day selloffs inside long-term uptrends are driven by stop cascades, margin liquidation, and panic — the book: "selling begets more panic selling until the stock reaches some level, leading to an extremely oversold condition before it snaps back." The buyer of RSI(2) < 5 is selling short-term liquidity to forced sellers and is paid for it.
2. **Trend filter as catastrophe avoidance.** Connors: "most cataclysmic individual stock drops, over the past century, have occurred when the stock was under its 200-day moving average" (Bear Stearns, Washington Mutual, United Airlines, Citigroup charts in ch. 4). Their 8M-trade study shows average 5-day gains are higher above the 200-day MA than below.
3. **Behavioral asymmetry of fear vs greed.** The book's own table (§2.3) is asymmetric: the deepest oversold bucket earns +0.93%/week while the deepest overbought bucket loses only −0.29%/week. Fear reverts harder than greed.
4. **Overnight risk is underpriced, not overpriced.** Ch. 7 ("It Pays to Hold Positions Overnight") argues the obvious-sounding caution (day-only holding) was "extremely wrong since 1995" — overnight holding captured the edge despite 9/11, LTCM, Enron, and the 2007 credit events occurring in that window.

**Quantified edge (all literature claims, not ours).**

- Connors/Alvarez gradient table — §2.3 (8M+ trades, 1995–2007).
- Quantitativo (2024), 21k stocks incl. delisted, 1998–2024, bull regime (S&P 500 > 200-day SMA) only: buying any stock with RSI(2) < 5 and holding 5 days → mean **+3.3%**/event, 60% positive, winners avg +9.8%, losers avg −6.6%, positive skew; vs RSI(2) > 5 baseline +0.3% with 52/48 coin-flip. Difference significant at p < 0.05. Average of 551 qualifying stocks per day (median 453, max 2,844) — the signal is frequent enough to be portfolio-traded.
- Quantitativo's size cut: the edge is *stronger in smaller caps* ("probably being competed away in larger cap stocks by quantitative funds ... not looking at smaller cap stocks, where the edge still persists and is fat"), but nano-caps carry ~89% eventual delisting probability — a trap for naive small-cap versions.
- Swanson (2013), SPX 1983–2013, $2k risk per trade, ATR(10)-normalized share count, no reinvestment: original rules → 129 trades, 82% profitable, PF 2.97, $28.7k net on $100k. Every RSI threshold 1–30, every exit-MA length 1–30, and every fixed holding period 1–30 days tested was profitable — parameter robustness evidence. He also documents a real **drawdown regime starting 2011**: "the standard 2-period trading system ... has been in a drawdown. During 2011 the market experienced a sudden and sustained drop which put the system into loss. It has been slowly recovering since."
- Swanson cross-market table (modified rules): SPY PF 3.12 (87% winners, 293 trades), ES PF 2.05, DIA 2.13, IWM 2.24, IYY 2.09, QQQ 1.98 — holds up across index ETFs.

**Contradictory / decay evidence (must not be ignored).**

- Quantitativo's portfolio version (10 slots, all-cap stocks, RSI(2) < 5, exit close > prior day's high): "massively works until 2008, then it stops working and struggles until this day" — 17.8%/yr overall but all of it earned in the first 8–9 years; Sharpe 0.72; payoff ratio 0.74; ~460 trades/yr. The fix that restored performance in their tests: restrict to large/mega caps (delisting probability 35%/9% vs >70% small-cap) and cut to 2 concurrent positions → claimed 30.3%/yr, Sharpe 1.09, max DD 35%, 64% win rate, ~90 trades/yr. *Their* backtest, not ours, and the parameter path (10 → 2 positions) invites overfit skepticism; their own 100-run random-selection robustness pass still beat the benchmark, which is the more convincing evidence that the raw signal persists.
- The strategy is long-tail sensitive: 2008-type markets produce repeated RSI(2) < 5 readings *below* the 200-day MA (filtered out) but sharp whipsaws around the MA during regime transitions. Swanson's 2011 drawdown shows even the index version has multi-year flat/losing stretches.
- Crowding: RSI(2) is among the most widely known quant rules in retail and quant circles. The pre-2009 concentration of returns in Quantitativo's portfolio test is a warning; the persistence of the single-event edge to 2024 in their data is the counterweight.

## 4. The twist: RSI2-VX

Three modifications, each tied to a documented weakness of the original.

### (a) VIX futures term-structure position sizing (the "VX")

*Weakness addressed:* the 200-day MA is a slow, binary regime filter. It keeps you fully out below the MA (fine) but grants *full size* during the early stages of vol shocks that begin above the MA (Feb 2018, Aug 2015, the Apr 2026 one-day inversion) — precisely when pullback-buying drawdowns cluster. The VIX futures curve shape is a faster, continuous stress gauge.

Evidence read this session:

- FlashAlpha's 2018–2026 study (413 Friday closes): the curve spent ~14.5% of weeks in backwardation (median VIX 23.8 in those weeks); backwardation does **not** predict negative forward returns (median 4-week +1.45% backwardation vs +1.69% contango — "inversions cluster mid-panic, and mid-panic is where violent rebounds live too") but **widens the forward return distribution ~60%**: "the curve is not forecasting direction. It is forecasting the size of whatever happens next." Their practical conclusion: backwardation is "a position-sizing input, not a direction call," and halving size preserves the expected-return profile at roughly contango-era risk.
- thetrading.tools' 16-year IVTS (VIX/VIX3M) series: backwardation on 7.6% of trading days since 2010 across 103 episodes; sustained backwardation (5+ days) historically associated with deeper drawdowns. Live anchor as of 2026-10-06: contango, day 126 of the current regime, VIX 15.01 / VIX3M 17.64, IVTS 0.8509.
- AlgoKing's regime-filter post uses slope bands +5% / +1% / −5% for full/reduced/minimal/defensive states — a workable band structure we adapt.

Our mandate goes one step beyond FlashAlpha's "halve it" conclusion to *flat* in backwardation, accepting the documented cost of missing panic-rebound trades in exchange for tail control. This is a deliberate, testable deviation — the validation protocol (§7) must quantify the foregone return.

Rule — compute state S daily from VIX/VIX3M (primary; front/second-month futures slope as cross-check):

| State | Condition (VIX/VIX3M) | Condition (futures slope (VX2−VX1)/VX1) | Size multiplier |
| --- | --- | --- | --- |
| Contango | < 0.97 | > +1% | 1.0× |
| Flat | 0.97 – 1.00 | −1% … +1% | 0.5× |
| Backwardation | > 1.00 | < −1% | 0× (no new entries) |

Existing positions are NOT force-closed in backwardation — they keep their standard exits (rebounds cluster there; FlashAlpha). If VIX/VIX3M > 1.10 (deep backwardation), also cancel resting entries for 5 sessions (sustained-stress rule).

### (b) Exit = RSI(2) > 70 OR 2×ATR(10) trailing stop, whichever first

*Weakness addressed:* the close-above-5-day-MA exit is blind to momentum quality — it exits on any weak bounce and can sit through full retracements that never close above the 5-MA before collapsing again (the 2011 experience). Connors' own VIX-based strategies and the cumulative-RSI stock strategy exit on RSI(2) > 65; we use 70 to give positions slightly more room (sweep 60–80 in validation). The 2×ATR(10) trailing stop resolves the "stops hurt" (book, equities) vs "stops helped" (Swanson, futures) disagreement by using a *wide, volatility-scaled* stop: the book's table shows damage concentrated at tight stops (1–7%); 2×ATR(10) on a liquid large-cap is typically 4–8% away — the region where the book's own table shows harm shrinking — while capping the single-trade tail the no-stop original exposes (a stock that keeps falling after entry; the 200-day MA cannot prevent single-name collapse).

### (c) Per-trade risk cap 0.75% of equity with ATR-based sizing

*Weakness addressed:* the original has no sizing rule at all (implicitly all-in on one index). Quantitativo's replication shows the failure mode of naive portfolio versions is concentration in delisting-prone small caps; risk-based sizing plus a liquidity/large-cap universe constraint is the antidote.

- Shares N = (0.0075 × E) / (2 × ATR(10)), E = current equity — the trailing-stop distance equals the risk budget by construction.
- Executed shares = N × S (term-structure multiplier).
- Caps: notional ≤ 25% of E per position; notional ≤ 5% of 20-day ADV (the 5% ADV cap follows Quantitativo's liquidity rule); max 6 concurrent positions (aggregate heat ≤ 4.5%).

Net effect vs original: same entry DNA (200-day MA + RSI(2) extreme), but regime-aware size, momentum-based exits, and defined risk per trade.

## 5. Full specification of the twist variant

**Universe.** Primary: S&P 500 constituents + the 20 most liquid US sector/index ETFs. Filters: price > $5, 20-day ADV > $20M, listed ≥ 1 year. Delisting-safe data mandatory (include delisted names in backtests). Large/mega-cap tilt per Quantitativo's delisting finding.

**Data.** Daily OHLCV (adjusted for signals, raw for execution P&L — document the convention); VIX and VIX3M index closes (2007–); VIX front/second-month futures settlements (Cboe, 2004–) as cross-check; pre-2007 history either reconstructed (constant-maturity 3-month implied vol) or excluded — state which in the run log.

**Indicator computation reference (fix these exactly).**

- RSI(2), Wilder smoothing:
  - Up_t = max(C_t − C_{t−1}, 0); Down_t = max(C_{t−1} − C_t, 0).
  - AvgUp_t = (AvgUp_{t−1} × (n−1) + Up_t) / n, n = 2; same for AvgDown. Seed with simple average of first n values.
  - RS = AvgUp / AvgDown; RSI = 100 − 100 / (1 + RS). If AvgDown = 0 → RSI = 100.
- SMA(200): simple mean of last 200 closes.
- ATR(10), Wilder: TR_t = max(H−L, |H−C_{t−1}|, |L−C_{t−1}|); ATR_t = (ATR_{t−1} × 9 + TR_t) / 10.
- Term-structure ratio: IVTS = VIX / VIX3M (close basis). Futures slope = (VX2 − VX1) / VX1 (settlement basis).

**Entry (long only).** Evaluate at close of day t; all conditions required:

1. C_t > SMA(200)_t.
2. RSI(2)_t < 5 (primary; sweep {3, 5, 10}).
3. S_t > 0 (not backwardation; use prior-day futures state for MOC equity orders — settlement-time mismatch, see §7).
4. No existing position in the name; fewer than 6 open positions.
5. Rank multiple candidates by lowest RSI(2), ties by larger ADV.

Execution: MOC at t (preferred per literature) or open t+1 (measure the degradation; Quantitativo's SPY test says it is large).

**Sizing.** Per §4c. Example: E = $10M, ATR(10) = $2.50, S = 1.0 → N = (75,000) / (5.00) = 15,000 shares; notional cap 25% × $10M = $2.5M → at $100/share, $1.5M notional passes; at $200/share, capped to 12,500 shares.

**Exit (first trigger wins).**

1. RSI(2)_t > 70 → exit MOC.
2. Trailing stop: stop_t = max close since entry − 2 × ATR(10) at that close's reading; intraday touch → exit (model slippage §7).
3. Regime hard exit: C_t < SMA(200)_t while in position → exit next open (mirrors Quantitativo's regime-exit rule).
4. Time stop: 10 trading days → exit MOC (keeps the strategy inside the swing bucket; original average hold was 3–4 days).

**Risk limits.** Per-trade ≤ 0.75% of equity at stop distance. Portfolio heat ≤ 4.5%. Deep-backwardation (IVTS > 1.10) → no new entries for 5 sessions.

**Costs.** Commission $0.005/share; slippage 2 bps/side large-cap, 5 bps/side mid-cap; stop fills at stop − 1×(avg spread) − 5 bps; overnight gap-through-stop filled at next open when open < stop.

**Capacity.** At 5% ADV participation and the universe above, ~$150–300M before market impact erodes >25% of the per-trade edge (literature edge ≈ 0.5–1.5%/trade; impact at 5% ADV over 2–5 day holds is well under that). The ETF-only variant scales higher.

**Execution pseudocode.**

```text
for each trading day t:
    update RSI2, SMA200, ATR10 for all universe names
    S <- term_structure_state(t-1 futures settle, t VIX/VIX3M close)
    for each open position:
        if close < SMA200: queue exit at next open
        elif RSI2 > 70: queue exit MOC
        elif low <= trailing_stop: exit at stop (modeled fill)
        elif days_held == 10: queue exit MOC
    if S == 0: skip new entries
    else:
        candidates <- [C > SMA200 and RSI2 < 5 and no position]
        sort by RSI2 ascending
        for c in candidates until 6 positions:
            N <- 0.0075 * equity / (2 * ATR10_c) * S
            N <- min(N, 0.25 * equity / price_c, 0.05 * ADV20_c)
            submit MOC buy N shares
```

## 6. Failure modes & regime dependence

1. **Sustained bear markets / MA whipsaw (2000–2002, 2008, 2022):** long stretches below the 200-day MA = zero trades (opportunity cost, not losses), but transition zones produce whipsaw entries just above the MA. Swanson's 2011 drawdown is the template: a sudden sustained drop put the system under water for ~2 years.
2. **Backwardation clustering:** vol shocks cluster; the sizing rule goes to zero exactly when the *best* historical entries (deep panic lows above the MA) occur. FlashAlpha's data (median 4-week +1.45% post-inversion) quantifies what we forfeit. Accepted deliberately; monitor the foregone-return tracker as an early-warning metric.
3. **Edge decay / crowding:** Quantitativo's all-cap portfolio version died after 2008; the published edge concentrates pre-2009. If large-cap RSI(2) < 5 events stop reverting, the strategy has no second engine.
4. **Single-name gap risk:** earnings/bankruptcy gaps through the 2×ATR stop (long-only, overnight holds). The 200-day MA reduces but does not eliminate this (Quantitativo: even mega-caps carry ~9% long-horizon delisting probability).
5. **Exit-regime mismatch:** RSI(2) > 70 exits early in strong V-recoveries (gives back the runner); the trailing stop exits late in slow bleeds. Swanson's sweeps show a flat-but-monotone response surface — mild comfort, not immunity.
6. **Early-warning indicators:** rolling 100-trade win rate < 55% (literature norm 70–85%); avg winner / avg loser < 0.6; share of entries taken at S = 0.5 rising (regime drift); IVTS > 1.0 for > 20 consecutive sessions; foregone-return tracker (paper P&L of skipped backwardation entries) strongly positive for > 6 months → escalate the 0× rule for review.

## 7. Validation protocol

**Data needs.** Survivorship-bias-free US equities 1995–2026 with delisting returns (CRSP/Compustat or Sharadar-equivalent); SPY/QQQ/sector ETFs from inception; VIX futures daily settlements (Cboe, 2004–) and VIX/VIX3M (2007–); corporate-action-adjusted prices for signals, unadjusted for fills.

**Chronological splits.**

- **Replication gate (in-sample reference):** 1995–2007 — reproduce the book's flagship table before anything else: target ≈ 49 SPX signals, ~84% win rate, ~3-day average hold, ≈ +523 SPX points. If we cannot reproduce within tolerance, stop and fix the engine (RSI variant is the prime suspect).
- **Decay check:** 2008–2015 — Swanson's 2011 drawdown must appear; if our engine shows smooth profits there, it is wrong.
- **True out-of-sample:** 2016–2026 — must include Feb 2018 (volmageddon), Dec 2018, Mar 2020, the 2022 bear, and the Apr 2026 backwardation episode.
- **Walk-forward:** 5-year train / 1-year test, rolled annually; parameters frozen per fold.

**Cost/slippage model.** As §5. Stress passes: 2× slippage; all stop fills at next open (worst case); MOC→next-open entry degradation measured explicitly (literature says it is large — treat as a first-class result, not a footnote).

**Strategy-specific pitfalls.**

- *Look-ahead:* RSI(2)/SMA(200)/ATR computed on close t may only trade at close t (MOC) or open t+1 — never "signal at close, fill at same day's better intraday price."
- *Settlement-time mismatch:* VIX futures settle at a different time than the equity close — use prior-day futures state for MOC equity entries, or a same-day 15:45 ET snapshot; document the choice.
- *RSI variant:* fix Wilder smoothing; a Cutler RSI(2) is a different indicator at 2 periods.
- *Survivorship/delisting:* mandatory; Quantitativo showed the small-cap version is a delisting trap (89% nano-cap death probability).
- *Backwardation foregone-return accounting:* report the opportunity cost of the 0× rule as a separate line item.
- *Multiple testing:* threshold/exit sweeps are exploratory; only the frozen spec counts for acceptance.

**Robustness checks.** RSI threshold {3, 5, 10}; exit RSI {60, 65, 70, 75, 80}; ATR multiple {1.5, 2, 2.5}; ATR length {10, 14, 20}; sizing states {1/0.5/0} vs {1/0.75/0.5} (the FlashAlpha-faithful variant); universe {S&P 500, S&P 1500, ETF-only}; entry {MOC, next open}. Demand plateau-shaped response surfaces, not a single peak.

**Acceptance criteria (pre-registered).** Out-of-sample 2016–2026, net of stress costs: Sharpe ≥ 0.8 on deployed capital (exposure-adjusted), max drawdown ≤ 15% at 0.75% risk, win rate ≥ 60%, profit factor ≥ 1.5, ≥ 150 OOS trades, positive expectancy in each macro sub-period (2016–19, 2020–21, 2022–26). Replication gate first. If the backwardation 0× rule costs > 30% of gross expectancy vs the {1/0.75/0.5} variant, escalate to the desk for a rule-change decision.

## 8. Sources read (annotated)

1. **Connors, L. & Alvarez, C., *Short Term Trading Strategies That Work* (2008), full PDF.** URL: https://img1.wsimg.com/blobby/go/b298ce5b-3c11-48f0-9704-0e059e7cfa1a/downloads/short_term_trading_strategies_that_work_larry_and_cesar.pdf — accessed 2026-10-07. Read in full (OCR-degraded but legible). Taken: exact RSI(2) flagship rules and results (49 signals / 83.6% / +522.92 pts / ~3-day holds); cumulative-RSI rules and both parameter sets (88% / +65.53 pts; 85.47% / +105.95 pts; 3-day/45 variant 79.49% / +779.51 SPX pts); stock version (77,068 trades, 69%); the 8M-trade RSI(2) gradient table (§2.3); the "stops hurt" table (§2.1); VIX 5% rule; VIX Stretches, VIX RSI, TRIN, Double 7s, S&P short rules and stats; 200-day MA catastrophe rationale; intraday limit-order edge table (+4.35% avg for 10%-lower limits, 63% winners); ch. 7 overnight-risk argument.
2. **Swanson, J., "Connors 2-Period RSI Update For 2013", EasyLanguage Mastery (Aug 26, 2013).** URL: https://easylanguagemastery.com/connors-rsi-update-for-2013/ — accessed 2026-10-07. Read in full. Taken: independent SPX replication 1983–2013 (129 trades, 82%, PF 2.97, $28.7k on $100k at $2k risk); the 2011 drawdown disclosure; parameter sweeps (threshold 1–30, exit-MA 1–30, hold 1–30 days — all profitable); modified rules (threshold 10, 10-day MA exit) → $62.8k, PF 2.74, 227 trades; $2,000 hard stop *improving* results ($66.7k, PF 2.93 — contradicts the book; flagged); multi-ETF table (SPY PF 3.12 / 87%, ES 2.05, IWM 2.24, DIA 2.13, IYY 2.09, QQQ 1.98). Companion page https://easylanguagemastery.com/strategies/rsi-and-how-to-profit-from-it/ (same rules restated with a $1,000 catastrophic stop; cumulative-RSI rules) read via search extract.
3. **Quantitativo, "The Holy Grail still works" (Jun 15, 2024).** URL: https://www.quantitativo.com/p/the-holy-grail-still-works — accessed 2026-10-07. Read in full. Taken: 2.5M-event edge quantification (+3.3% mean 5-day, 60% positive, p < 0.05 vs +0.3% baseline); event frequency (avg 551 stocks/day); small-cap edge gradient and delisting-probability trap (nano 89%, large 35%, mega 9%); failure of the naive 10-slot portfolio version post-2008 (Sharpe 0.72, payoff 0.74); large/mega-cap + 2-position fix (their claimed 30.3%/yr, Sharpe 1.09, 64% win rate — attributed, not endorsed); 100-run random-selection robustness pass; next-open entry cost warning; 5%-of-ADV liquidity rule; regime-exit rule (close below 200-day → next open).
4. **FlashAlpha, "VIX Term Structure Inversions Since 2018: What Backwardation Actually Signals" (2026).** URL: https://flashalpha.com/articles/vix-term-structure-inversions-since-2018-data-study — accessed 2026-10-07 (via search-extracted full text). Taken: 14.5% of weeks in backwardation 2018–2026, median VIX 23.8; median 4-week forward return +1.45% backwardation vs +1.69% contango (no direction signal); ~60% wider forward dispersion; "position-sizing input, not a direction call" — the direct motivation (and tension) for our 0× rule.
5. **thetrading.tools, "VIX Term Structure Today: VIX/VIX3M Ratio, Backwardation & Futures Curve".** URL: https://www.thetrading.tools/vix-term-structure — accessed 2026-10-07. Taken: IVTS definition (VIX/VIX3M, backwardation > 1.0); 7.6% of days in backwardation since 2010 across 103 episodes; sustained (5+ day) backwardation associated with deeper drawdowns; index-vs-futures curve measurement caveat; live anchor as of 2026-10-06: contango day 126, VIX 15.01, VIX3M 17.64, IVTS 0.8509.
6. **AlgoKing, "VIX futures term structure as regime filter" (May 2026).** URL: https://algos.pro/posts/2026-05-06-vix-term-structure-regime-filter/ — accessed 2026-10-07 (via search extract). Taken: concrete slope bands (+5% / +1% / −5%) used as reference for our 3-state sizing; their theta-strategy P&L by regime (+$1,340 avg daily in steep contango, 76% win rate over 91 days, vs −$920 / 37% over 11 backwardation days) as regime-dependence evidence.
7. **Easycators, "Cumulative RSI-2 Trading Strategy – Short Term Trading Strategies That Work".** URL: https://easycators.com/thinkscript/cumulative-rsi-2-trading-strategy/ — accessed 2026-10-07 (via search extract). Taken: independent restatement of the book's p.67–68 numbers (88% / 65.53 pts / 1.26% avg / 3.7 days; alternate 85.46% / 105.95 pts / 1.05% / 3.57 days) — corroborates the PDF's OCR-degraded figures.

## 9. Further reading

- Connors Research / TradingMarkets later publications on TPS, RSI-25, and "Buy the Fear, Sell the Greed" (2018) — known via secondary citation; not accessed this session.
- Wilder, J.W., *New Concepts in Technical Trading Systems* (1978) — the RSI definition (not accessed; primary for the indicator only).
- Simon, D.P. & Campasano, J. (2014), VIX futures slope trading, as reviewed in "U.S. Stock Returns and VIX Futures Curve", *Journal of Wealth Management* 21(2) — https://www.pm-research.com/content/iijwealthmgmt%3A%3A%3A21%3A%3A%3A2%3A%3A%3A107.full.pdf — literature-review section read via search extract (Simon & Campasano: sell/buy VIX futures on contango/backwardation hedged with S&P futures was profitable); full text paywalled.
- Alvarez, C., *Alvarez Quant Trading* blog — RSI(2) variant tests and stop-loss studies (known via secondary citation; not accessed).
- QuantifiedStrategies.com RSI(2) replications (known via secondary citation; not accessed).
