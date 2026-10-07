# A3. VWAP Reversion and Anchored VWAP

Status: research dossier. Section 7 ideas are untested hypotheses. Not investment advice.
Labels: [PR] peer-reviewed, [WP] working paper, [PRAC] practitioner claim, [UNV] unverified.

## 1. Summary, horizon, asset class, holding period

VWAP (volume-weighted average price) is the cumulative average of price weighted by volume, usually reset at the session open. Two quite different trading uses sit under one name. (1) Intraday VWAP reversion: price stretched away from session VWAP (often measured in standard-deviation bands) is faded back toward it, on the theory that institutional execution benchmarks pull price toward VWAP. (2) Anchored VWAP (AVWAP): VWAP started from a chosen event or pivot (earnings day, swing low, year start) and used as a dynamic support/resistance or "who is in profit" line, mostly in swing trading, popularised by Brian Shannon. Holding periods: minutes to hours for session VWAP fades; days to weeks for AVWAP. Assets: liquid equities, ETFs, index futures. Critical headline: the evidence base for the reversion rule is thin and the one vendor test I found is negative; the best-publicised VWAP "system" in recent literature (Zarattini and Aziz) is trend-following around VWAP, the opposite of a fade, and its full text (second pass) shows zero modelled slippage with roughly 15 flips per day, so neither side has a cost-realistic test. A small own sanity check (section 5, 60 days, 5-minute bars) pointed weakly toward reversion, not continuation; it is not proof.

## 2. Origin and who uses it

- Berkowitz, Logue and Noser, "The Total Cost of Transactions on the NYSE" (Journal of Finance, 1988): proposed trade-date VWAP as a benchmark for measuring execution quality, as an estimate of the price facing a non-strategic trader [PR; I read it via secondary summaries].
- Madhavan, "VWAP Strategies" (Trading, Spring 2002, an ITG practitioner publication): discusses guaranteed-VWAP bids, forward VWAP crosses and automated participation strategies, and warns that uncritical use of VWAP as a benchmark can increase costs and risk; VWAP is reasonable for smaller, non-urgent orders. [PRAC from a broker-dealer researcher; full text read.]
- Bialkowski, Darolles and Le Fol, "Improving VWAP strategies: a dynamic volume approach" (Journal of Banking and Finance 2008): models intraday volume (market-wide plus stock-specific components, ARMA/SETAR) to track end-of-day VWAP more closely, tested on CAC 40 stocks. [PR; abstract-level read.] This is about execution, not about alpha.
- Brian Shannon (author of a book on multi-timeframe technical analysis; I could not confirm the exact title from a source and do not cite it) popularised AVWAP; on the CMT Association podcast he credited Paul Levine with developing the anchored version. He is a swing trader (holds of roughly 3-6 days, sometimes weeks) per that interview. [PRAC]
- Zach Hurwitz on Chat With Traders (2015) discussed using VWAP to gauge where large participants interact with markets; the show notes do not state rules or whether he fades or follows it. [PRAC, no rules]
- Zarattini and Aziz, "VWAP: The Holy Grail for Day Trading Systems" (SSRN 4631351, Nov 2023). [WP, promotional context; full text read in second pass via the Concretum-hosted PDF. Aziz's firm and the co-author's Bear Bull Traders sell trading education, and the paper itself calls the system not "fully developed".]
- Gao, Han, Li and Zhou, "Market intraday momentum" (Journal of Financial Economics 2018): first half-hour return predicts last half-hour return of the S&P 500 ETF; relevant because it is academic evidence for intraday continuation, not reversion. [PR; full text of a working-paper version read in second pass.]

## 3. Economic rationale and the other side

- Benchmark flow hypothesis: many institutional orders are executed by algorithms that target VWAP over a horizon, and traders are evaluated against it. That produces predictable, volume-proportional flow that dampens drift away from VWAP during execution. If true, price deviation from VWAP draws in passive/benchmark flow on the other side. But this is a hypothesis; the published VWAP execution papers I found are about tracking VWAP, not about whether price mean-reverts to it. Madhavan's own point cuts the other way: traders measured against VWAP can game timing, which changes behaviour and costs.
- Self-fulfilling level: Shannon argues widely watched levels become self-fulfilling and treats anchors as "levels of interest", looking for confluence. Behavioural/coordination, not proven.
- Cost-basis story for AVWAP: AVWAP from an event approximates the average price of buyers since then; price above it means most buyers are in profit, below means underwater. This is an interpretation, not a measurement of who holds the shares.
- Intraday periodicity: Heston, Korajczyk and Sadka (JF 2010) find return continuation at exact multiples of a day, which is consistent with systematic intraday trading patterns, but the paper does not establish VWAP execution as the cause [PR; mechanism speculative].
- Other side of a fade: momentum/informed traders pushing price away on news; of a trend-follow around VWAP: mean-reversion traders and liquidity providers who lean against it.

## 4. Canonical rules

### 4a. Session VWAP band fade (typical practitioner rule)
1. VWAP = cumulative(price x volume) / cumulative(volume), reset at the open (use typical price or bar close consistently).
2. Bands: VWAP plus/minus k times a volume-weighted standard deviation of price around VWAP (k=2 common).
3. Skip the first ~30 minutes when bands are still expanding (practitioner advice, e.g. Tradezella guide).
4. Entry: bar close beyond the band; long below the lower band, short above the upper.
5. Target: VWAP (or a fixed number of points); stop: beyond the band by a buffer or fixed distance.
6. Flat by the close.

### 4b. Anchored VWAP (swing)
1. Choose an anchor: earnings/news day, major pivot low or high, IPO date, start of year/quarter.
2. AVWAP = sum(typical price x volume from anchor) / sum(volume from anchor).
3. Long bias while price holds above AVWAP from a bullish anchor; buy pullbacks to the line that hold, or breakouts above it; exit or stop on a close below. Shannon's stated principle: buy strength after a dip rather than the dip itself; trail stops under higher lows; trim a portion near resistance. Rules are discretionary.

### 4c. Zarattini-Aziz VWAP trend system (for contrast)
Rules as stated in the paper's full text (second pass): VWAP uses the mean of high, low and close per 1-minute bar weighted by volume, regular hours only. At 09:31 go long if the price is above VWAP, short if below. The stop is a 1-minute close on the other side of VWAP, which flips the position (so the system is almost always in the market); anything open is closed at 16:00. Position size is 100 percent of equity, no leverage. Commission is $0.0005 per share and slippage is assumed to be zero, with the authors saying higher commissions hurt the strategy. This corrects my first-pass note, which relied on QuantConnect pages.

## 5. Evidence

- Session VWAP band fade, DAX, 15-minute bars, 4 Oct 2016 to 1 Oct 2026, 2-sigma session-anchored bands, fixed 30-point target and 50-point stop, 100 percent of equity, 0.02 percent commission per side, no slippage: total return -98.6 percent versus +137.5 percent buy-and-hold, win rate 59.17 percent, profit factor 0.64, 8,943 trades; every full year negative [PRAC: vendor (Backtrex) test, some exit logic undefined, so not a clean test]. Lesson: with a target smaller than the stop, a 59 percent win rate is not enough, and frequent signals in trends feed the stops. This does not prove all VWAP fades fail; no variant was tested.
- I found no peer-reviewed study of intraday price reversion to VWAP and no stock or futures backtest with significance tests, costs and out-of-sample results. Most public material is TradingView scripts whose authors themselves disclaim validation. Treat the reversion claim as [UNV].
- Zarattini and Aziz trend-around-VWAP [WP, full text read in second pass; authors' own backtest, no independent replication found]. Reported: $25,000 to $192,656 on QQQ (671 percent total, 43 percent a year, volatility 18 percent, Sharpe 2.1, max drawdown 9.4 percent) versus buy-and-hold 126 percent, Sharpe 0.7, drawdown 35.6 percent in the table (the abstract says 37), 2 Jan 2018 to 28 Sep 2023; TQQQ variant 8,242 percent with drawdown 36.1 percent. Details that change how much to trust it: (a) 21,967 trades on QQQ over about 5.7 years (roughly 15 a day), hit ratio 17 percent, average gain 5.7 times average loss; (b) zero slippage assumed, commission $0.0005 per share ($6,547 total on QQQ, $400,619 on TQQQ), and the authors note that higher commissions hurt; net profit per share traded is about 1.3 cents ($167,656 over 13.09 million shares, my arithmetic from the paper's Table 3), so a half-spread of 0.5 cent per share traded would remove roughly 40 percent of it and a full 1 cent roughly three-quarters; that is an illustration, not a test in the paper; (c) one instrument family, one sample, no out-of-sample split, no parameter search disclosed but also no robustness table beyond a comparison with 9/20/100/200-period moving-average systems, where VWAP did best (SMA200 Sharpe 0.9); (d) their descriptive test sums 1-minute price changes by prior-bar side of VWAP and finds continuation (about +$320 per share above, about -$280 below, 2018-2023) with no significance test; (e) the regression alpha of 38 percent a year (t above 5) is computed on the same sample; (f) most profit comes from 09:30-12:00 and 15:00-16:00. The authors themselves say it is not a "fully developed trading system". Community replications reported much weaker numbers ("no holy grail" per a QuantConnect page; a different implementation: 592.9 percent, Sharpe 1.754, turnover 2,183 percent) [PRAC, from the first pass, not re-opened]. Note on my first-pass inference: I wrote that a fade of the same instrument is "presumably losing at the same horizon". That does not follow, because their signal flips on a 1-minute close across VWAP while a 2-sigma band fade trades rare, large deviations; the two are different rules and can coexist.
- Gao, Han, Li, Zhou (JFE 2018, working-paper full text read): S&P 500 ETF first half-hour return predicts the last half-hour return; in-sample R-squared 1.6 percent (2.6 percent combined with the twelfth half-hour), out-of-sample R-squared 1.2 percent (1.8 percent combined), timing strategy 6.67 percent a year at 6.19 percent volatility (Sharpe 1.08 versus 0.29 buy-and-hold) with the authors claiming it survives transaction costs; stronger on volatile and high-volume days. This is academic support for end-of-day continuation after a strong open, a different statement from VWAP deviation continuation, but it is the closest peer-reviewed support for the Zarattini direction and a caution against blanket fading. [PR]
- Own small sanity check, second pass (NOT proof): 12 liquid ETFs and megacaps (SPY, QQQ, IWM, DIA, AAPL, MSFT, NVDA, AMZN, META, TSLA, JPM, XOM), yfinance 5-minute regular-hours bars, 15 July to 7 Oct 2026 (60 sessions, 720 ticker-days), typical price (H+L+C)/3 session VWAP, bands from a running volume-weighted deviation. Assumed cost 1 bp per side (2 bp round trip), no borrow, no slippage beyond that. (1) Signed forward return after a 5-minute close above/below VWAP (positive = continuation): all bars after the first 30 minutes, minus 1.3 bp over the next 30 minutes and minus 6.3 bp to the close; bars beyond 2 sigma, minus 5.5 bp (30 minutes) and minus 17.9 bp (to close) over 621 ticker-days. The naive t-statistics (about -5 to -8) are inflated because tickers move together on the same days; SPY alone over 60 days gave minus 0.5 bp (t about -1.3) and minus 2.8 bp to close (t about -1.9), i.e. not distinguishable from zero. (2) An always-in follow-VWAP rule on 5-minute closes (Zarattini-style but coarser), about 7.5 flips per ticker-day: gross minus 12 bp a day, net of 1 bp per side minus 21 bp a day; every ticker negative net. (3) A 2-sigma fade, one trade per ticker-day after 30 minutes, target VWAP, stop 1.5 times the distance, otherwise flat at close: 626 trades, win rate 59 percent, average win 43 bp versus average loss 55 bp, profit factor 1.15, mean 5.3 bp gross and 3.3 bp net (t about 1.4, not significant). Reading: in this one recent quarter, 5-minute data did not reproduce VWAP continuation and gave a weak, insignificant reversion tilt. Limits: 60 days of one regime, 5-minute rather than 1-minute bars, ETFs and megacaps only, no out-of-sample split, correlated tickers, my own untested band definition, and the price path is one trade per day so the sample is small. Treat as a sanity check that the mechanics run, not as evidence for or against either side.
- AVWAP: the Shannon podcast page gives anecdotes (an IPO-date anchor acting as support in 2008 and again recently) and an uncited recollection that a stock's daily range stays within S2/R2 pivots about 86 percent of the time (stated from memory in the interview) plus a recollection of Ken Griffin's testimony about VWAP-based executions; no backtests, no sample sizes [PRAC]. A Take Profit page cites a ~67 percent win rate with no test [UNV]. I found no independent test of AVWAP.
- Madhavan: tracking VWAP is hard in practice; automated VWAP strategies have tracking error and shortfalls on days with unusual price/volume patterns [PRAC].
- Post-publication decay and capacity: no measurement possible given absence of baseline evidence.

## 6. Failure regimes and risks

- Trend days (news, gap-and-go): the fade is stopped repeatedly; the DAX test shows the cumulative damage.
- Early-session instability: VWAP and bands are noisy in the first 30 minutes.
- Low-liquidity names: VWAP is a poor reference with sparse volume; spreads exceed the reversion edge.
- Anchor selection bias: the AVWAP anchor is chosen with hindsight, and many anchors can be drawn that "worked"; this is the same forking-paths issue as pattern recognition.
- Cost sensitivity: high turnover with small average win (the DAX test average win about 0.13 percent of account versus 0.31 percent average loss).
- Regime shift in benchmark flow (more dark/ATS execution, close-oriented execution) is unmeasured.
- Index-futures session definitions: using the wrong session open for VWAP (RTH versus Globex) changes everything.

## 7. MY TWIST (hypotheses, NOT backtested)

### Twist 1: Regime-gated VWAP fade
- Rationale: the vendor test shows an ungated fade loses; fades should be valid only in balanced, low-trend conditions.
- Rule change: take 4a entries only if (i) a trend-efficiency filter (net displacement over N minutes divided by path length, or a variance ratio below 1) shows balance, (ii) relative volume of the stock is not elevated (below 1.0, i.e. not in play), (iii) the index is inside its own VWAP band, and (iv) time is after the first 30-45 minutes. Target VWAP at 50-100 percent of the distance, stop at 1.5x the distance to target (reward/risk not below 1:1).
- Parameters: k (1.5-3), efficiency threshold, lookback N (30-90 minutes), relative-volume cut, reward/risk.
- Expected effect: fewer trades, profit factor above 1 if the thesis is true.
- Falsification: if net profit factor after 2x modelled slippage is not above 1.1 out of sample, or the gated version is not significantly better than the ungated baseline on the same instrument set (paired test on daily P&L), reject.

### Twist 2: Placebo-tested catalyst AVWAP
- Rationale: test whether AVWAP carries information beyond "a moving average that starts on a special day".
- Rule change: anchor at the earnings-gap day; enter long on the first touch of AVWAP after at least a set number of days above it with declining volume on the pullback; stop at a close below the line; compare against placebo AVWAPs anchored on random days in the same stock, and against a plain moving average of equal slope.
- Parameters: minimum days above (3-10), pullback volume ratio (0.5-1.0 of average), stop buffer (0.5 ATR), holding cap (5-20 days).
- Expected effect: if anchors carry information, the touch-and-hold probability and forward 5-day return should beat the placebo.
- Falsification: if the earnings-anchored AVWAP does not beat random-anchor placebos and the equal-slope moving average by a margin whose bootstrap confidence interval excludes zero, conclude AVWAP is mere smoothing.

### Twist 3: Relative-volume switch between trend and fade around VWAP
- Rationale: the Zarattini line (follow VWAP) and the practitioner line (fade VWAP) may each work in different regimes; abnormal opening relative volume is the regime variable that A2's source shows matters.
- Rule change: if opening-range relative volume is at least 150 percent, trade with the VWAP side (long above, short below) with a trailing stop; if below 80 percent, run Twist 1's fade; between, stay out.
- Parameters: relative-volume thresholds, VWAP side hysteresis (0.1-0.3 sigma), trailing stop.
- Expected effect: raises combined Sharpe through diversification between regimes.
- Falsification: if the regime split does not produce opposite-signed average returns for trend versus fade in out-of-sample data (interaction term insignificant), reject the switch.

## 8. Implementation spec

Data: tick or 1-minute bars with volume per venue; consolidated tape preferred (VWAP from a single venue differs); correct session boundaries; corporate action adjustments for AVWAP; earnings calendar.

Signals: session VWAP and volume-weighted standard deviation (running update), AVWAP per anchor, efficiency ratio, relative volume, index VWAP distance.

Sizing: risk 0.25-0.5 percent of equity per trade for fades (low payoff, many trades), position cap vs ADV; no pyramiding into trends.

Execution: limit orders at the band for fades (adverse selection risk: fills occur when price keeps going); marketable-limit on confirmation; time stop at 60-120 minutes; flat at close.

Costs: commission, half-spread in/out, a stop slippage model at 1-2x spread, borrow for shorts; 0.04 percent round-trip commission was used in the vendor test and is not conservative for small names.

Pseudo-code:
```
on each bar t after 10:15:
  vwap_t = sum(p*v)/sum(v); sd_t = sqrt(sum(v*(p-vwap_t)^2)/sum(v))
  z = (close-vwap_t)/sd_t
  if regime_ok(eff_ratio, relvol, index_z) and z<=-k and no_position: buy; target=vwap_t+(1-f)*(-z*sd_t) ; stop = entry - 1.5*abs(target-entry)
  mirror for shorts
  exit: target, stop, 120-min time stop, 15:55 flatten
```

## 9. Backtest plan

- First replicate the vendor baseline on your own data to ensure the machinery reproduces its losing result; then test gates one at a time. A pipeline that cannot reproduce a known negative is suspect.
- Walk-forward: choose k, windows, thresholds on a rolling training window; test on the next window; final hold-out never touched until the end. Use at least 5 years and multiple instruments (index futures, liquid ETFs, a large-cap basket).
- Multiple testing: record every variant; deflated Sharpe, SPA/reality check; for the AVWAP placebo test use permutation tests with thousands of random anchors.
- Cost realism: slippage stress at 1x, 2x, 3x; separate maker/taker fill assumptions for band orders (price may "touch" without filling).
- Metrics: profit factor, expectancy per trade net of costs, payoff ratio, hit rate, Sharpe, drawdown, exposure time, regime-conditioned results (trend vs balance days), turnover.

## 10. Risk management and kill-switch

- Per-trade stop always at order entry; max 1-2 concurrent positions per instrument; no averaging down.
- Daily loss cap (for example 1.5 percent) and a consecutive-stop rule: after 3 consecutive stops on one instrument, stop fading for the day (trend day identification).
- Disable fades on scheduled-news days (FOMC, CPI) unless explicitly tested.
- Kill if rolling 100-trade net expectancy is negative with confidence, or if live slippage exceeds 2x modelled.
- AVWAP positions: size such that a stop at the line is at most the per-trade risk; cap number of simultaneous AVWAP trades in the same sector.

## 11. Annotated sources

| # | Source | Type | Grade | Note |
|---|---|---|---|---|
| 1 | Madhavan, VWAP Strategies (2002) https://www.smallake.kr/wp-content/uploads/2014/07/TP_Spring_2002_Madhavan.pdf | Practitioner journal | B | Read; about execution not alpha |
| 2 | Berkowitz, Logue, Noser (JF 1988), DOI 10.1111/j.1540-6261.1988.tb02591.x | Paper | A | Via secondary summaries only |
| 3 | Bialkowski, Darolles, Le Fol (JBF 2008) https://hal.archives-ouvertes.fr/hal-02877984 | Paper | A | Abstract level |
| 4 | Backtrex DAX VWAP band fade https://backtrex.com/en/backtests/vwap-band-fade-dax | Vendor backtest | C | Only quantitative fade test found; vendor, costs partial |
| 5 | CMT Association, Fill the Gap ep. 61 (Shannon) https://cmtassociation.org/podcast/fill-the-gap-episode-sixty-one-anchored-vwap-legend-brian-shannon-cmt/ | Interview page | C | Anecdotal, no tests |
| 6 | Chat With Traders, Zach Hurwitz https://chatwithtraders.com/video/an-interview-with-a-vwap-trader-zach-hurwitz | Interview notes | C | Show notes only, no rules |
| 7 | Zarattini and Aziz, VWAP paper, full text (Concretum-hosted PDF) https://concretumgroup.com/wp-content/uploads/2026/02/Volume-Weighted-Average-Price.pdf ; summary page https://concretumgroup.com/volume-weighted-average-price-vwap-the-holy-grail-for-day-trading-systems/ | Working paper, authors' backtest | B- (was C) | Full text read; rules and costs now verified; zero slippage, one sample, 22k trades, no out-of-sample; SSRN page returned 403 |
| 8 | Bear Bull Traders post https://bearbulltraders.com/?p=2606339 | Newsletter | C | Same claims |
| 9 | Heston, Korajczyk, Sadka (JF 2010) https://ar5iv.arxiv.org/html/1005.3535 | Paper | A | Summary read; periodicity, not VWAP |
| 10 | TradingView AVWAP reversion scripts and Tradezella VWAP guide https://www.tradezella.com/blog/vwap-trading-strategy | Practitioner | C | Rules only, no stats |
| 11 | Take Profit AVWAP page https://takeprofitapp.com/en/learn/anchored-vwap-trading | Educational | C | Unsupported win-rate claim |
| 12 | Gao, Han, Li, Zhou, Market intraday momentum (JFE 2018), working-paper PDF https://c.mql5.com/forextsd/forum/173/intraday_momentum_-_the_first_half-hour_return_predicts_the_last_half-hour_return.pdf | Paper (published version A; the PDF is a mirrored draft) | A- | Full text of the mirrored draft read; continuation evidence, not VWAP |
| 13 | Own sanity check, scripts and yfinance 5-minute data (60 sessions, 12 tickers), section 5 | Own computation | D (illustrative) | Small sample, 5-minute bars, correlated tickers; not evidence |

## 12. Open questions

1. Does intraday price mean-revert to session VWAP at all after costs, in any liquid instrument? Needs a clean statistical test (autocorrelation of VWAP deviation, not a trading rule). Second pass: my 60-session 5-minute check was weakly negative on continuation and insignificant on fade, which neither confirms nor refutes Zarattini-Aziz (1-minute data, 2018-2023); a multi-year, 1-minute, clustered-by-day test is still missing.
2. Does benchmark-algorithm flow create measurable pull toward VWAP, or only dampen deviation during execution?
3. Is AVWAP informative relative to random-anchor placebos?
4. How do the Zarattini VWAP-trend results hold with realistic costs and recent data, given the high turnover? Their own Table 3 implies about 1.3 cents net profit per share traded, so spread assumptions decide the result.
5. Which session definition and price input (typical price vs close) matter most for results?
6. Does the effect differ for index futures vs single stocks vs ETFs?

## Second-pass changelog

Date: 2026-10-07. What changed and why:
- Zarattini-Aziz upgraded from "summary only, rules unverified" to full text read: rules, costs (zero slippage, $0.0005 per share), trade count (21,967 on QQQ), hit ratio (17 percent) and the authors' own caveat are now stated; grade C to B-. Their continuation test (sum of 1-minute changes by prior-bar side of VWAP) is descriptive and has no significance test.
- Removed my first-pass inference that a fade of the same instrument "is presumably losing" because the trend system works; the two rules differ in signal frequency and are not logical opposites.
- Corrected buy-and-hold drawdown (35.6 percent in the paper's table; abstract says 37).
- Added Gao-Han-Li-Zhou (JFE 2018) as the closest peer-reviewed intraday continuation evidence, with in- and out-of-sample R-squared; it supports end-of-day continuation after a strong open, not VWAP behavior specifically.
- Added an own small sanity check (section 5): 12 tickers, 60 sessions, 5-minute bars, 2 bp round-trip cost. Result: no VWAP continuation at 5 minutes, always-in follow loses after costs, 2-sigma fade slightly positive but insignificant (t about 1.4). Heavily caveated; naive t-statistics are inflated by cross-ticker correlation.
- Still not improved: no peer-reviewed test of reversion to VWAP or of anchored VWAP; Berkowitz-Logue-Noser and Bialkowski et al. remain secondary/abstract level (not retrievable this pass); Madhavan unchanged from the first pass; the SSRN abstract page returned 403; Backtrex vendor test remains the only fade backtest and is not re-verified.
- Section 7 twists unchanged and remain untested hypotheses.
