# A2. Opening Range Breakout and Intraday Momentum

Status: research dossier. Section 7 ideas are untested hypotheses. Not investment advice.
Labels: [PR] peer-reviewed, [WP] working paper, [PRAC] practitioner claim, [UNV] unverified.

## 1. Summary, horizon, asset class, holding period

Two related families. (a) Opening range breakout (ORB): after the first n minutes of the session define a high/low range, then trade a break of that range in the direction of the opening move, with a stop and an end-of-day exit. (b) Index-level intraday momentum: the return from the prior close to the first 30 minutes (and sometimes the penultimate half-hour) predicts the return in the last 30 minutes, so you hold the index ETF/future only for the closing window. Horizon: minutes to one session; no overnight holding. Assets: single stocks (ORB), index ETFs/futures (SPY, ES, QQQ), commodity futures (Crabel's original). Win rates are low for the stock version (a QuantConnect commenter cited about 17 percent; the paper's best-stock tables show about 19-26 percent) and profits depend on a few large winners.

## 2. Origin and who uses it

- Toby Crabel, Day Trading with Short Term Price Patterns and Opening Range Breakout (1990): volatility-based breakout from the open (Open plus/minus a "stretch"), combined with narrow-range setups such as NR7. I have not read the book; the rule description below is from a third-party backtest summary [PRAC, secondary]. Zarattini et al. credit Crabel with introducing ORB.
- Raschke and Connors (1995, "Momentum Pinball") combined a 60-minute ORB with RSI; Brock, Lakonishok and LeBaron (1992) tested simple technical rules on a century of Dow data; Holmberg et al. (2012) studied volatility ORB in crude oil; Tsai et al. (2018) and others tested index ORBs [all as cited in the Zarattini et al. literature review; I did not read them].
- Zarattini, Barbon and Aziz, "A Profitable Day Trading Strategy for the U.S. Equity Market" (SSRN 4729284, Feb 2024). Authors have commercial ties to Concretum Research and Bear Bull Traders/Peak Capital (day-trading education). [WP]
- Zarattini, Aziz and Barbon, "Beat the Market: An Effective Intraday Momentum Strategy for S&P500 ETF (SPY)" (Swiss Finance Institute Research Paper 24-97, SSRN 4824172). [WP]
- Gao, Han, Li and Zhou, "Market intraday momentum" (Journal of Financial Economics, 2018). [PR]
- Baltussen, Da, Lammers and Martens, "Hedging demand and market intraday momentum" (JFE 2021). [PR]
- Heston, Korajczyk and Sadka (Journal of Finance 2010) on intraday return continuation at lags of exact multiples of a day. [PR]

## 3. Economic rationale and the other side

- ORB (single stocks): the first minutes on a news-driven day reveal an abnormal supply/demand imbalance that large, slowly executing institutions (who split orders across the day) keep pushing; Zarattini et al. state this logic and add that it should apply only to "Stocks in Play" (abnormal relative volume, usually a catalyst such as earnings). The other side: traders who fade the open, and market makers who widen quotes but lose to persistent informed flow.
- Index intraday momentum: Gao et al. propose infrequent rebalancers and late traders reacting to early information. Baltussen et al. argue gamma hedging by option dealers and leveraged-ETF rebalancing creates same-direction trading late in the day, and that the effect reverses over following days. Under that story the counterparty is the hedger who must trade regardless of price, and the premium is paid for absorbing that flow. If hedging demand shifts (zero-day options growth, ETF rebalancing rules) the effect can change.
- Honest caveat: these stories are plausible but the economics are not proven; the Stocks-in-Play result may also reflect post-announcement drift in a high-volatility subset.

## 4. Canonical rules

### 4a. Zarattini-Barbon-Aziz 5-minute ORB on Stocks in Play (from the paper)
1. Universe filter each day: open price above $5; average volume over the prior 14 days at least 1,000,000 shares; 14-day ATR above $0.50.
2. Relative volume after the first 5 minutes: opening-range (09:30-09:35 ET) volume divided by its 14-day average of the same window. Require at least 100 percent and keep the 20 highest.
3. Direction from the first 5-minute candle: bullish candle means long only; bearish means short only; doji means no trade.
4. Entry: stop order at the candle high (long) or low (short), triggered after the first 5 minutes.
5. Stop loss: 10 percent of the 14-day ATR from the entry price.
6. Exit: stop, else market close at 16:00 ET. No profit target.
7. Sizing: risk 1 percent of capital per trade at the stop, leverage capped at 4x.

### 4b. Crabel-style volatility ORB (secondary description)
Buy stop at Open plus stretch and sell stop at Open minus stretch, where the stretch is a multiple (a backtest cited used 2) of a 10-day average of "noise" (distance from the open to the nearest extreme); the first order filled is the position and the opposite order is the protective stop [PRAC, secondary].

### 4c. Gao et al. last half-hour rule
Signal: return from prior close to 10:00 (first half-hour, per paper; secondary sources add the 12th half-hour combination). Hold the index ETF in the last 30 minutes if positive; short or stay in cash if negative; exit at the close. A QuantConnect version used market-on-close exit.

### 4d. Zarattini et al. SPY intraday momentum
Public description: a "noise area" (typical intraday movement) is the boundary; trend-following positions open when price leaves it, with dynamic trailing stops, rather than only in the last 30 minutes. I could not read the exact definitions (noise area construction, check frequency, sizing); my recollection that the area is built from average time-of-day absolute move relative to the open and that a VWAP is involved in the stop is [UNV]. Read the paper before implementing.

## 5. Evidence

Zarattini-Barbon-Aziz (stocks) [WP, authors' backtest, 1 Jan 2016 to 31 Dec 2023, about 7,000 US stocks incl. delisted names via CRSP, IQFeed intraday data, commission only: $0.0035 per share, starting capital $25,000; no slippage or borrow cost mentioned in the text I read]:
- Base 5-minute ORB on all stocks passing the filters: 3.2 percent annualised return, 6.6 percent volatility, Sharpe 0.48, max drawdown 13 percent, alpha 3.3 percent, beta about 0.01, versus S&P 500 buy-and-hold 14.2 percent annualised and Sharpe 0.78. The paper itself reports the base strategy underperformed. Total net gain about 30 percent over the period.
- Relative-volume bucket analysis: mean net P&L per trade about -0.02R below 100 percent relative volume, 0.08R above 100 percent, and about 0.38R at more than 30x (R = the stop distance).
- Top-20 Stocks in Play version: total net return 1,637 percent, annualised 41.6 percent, volatility 14.8 percent, Sharpe 2.81, max drawdown 12 percent, alpha 35.8 percent, beta about 0.
- Other opening ranges (15, 30, 60 minutes) were weaker than 5 minutes; the authors say the reason is unclear. (Table values were garbled in my text extraction, so I quote no numbers.)

Critical reading:
- The edge appears only after a selection step chosen after observing that relative volume matters; there is one sample, 8 years, mostly a bull market, no out-of-sample period. The paper states the parameters were "minimal" and economically motivated, which is argued, not demonstrated.
- 4x leverage and 1 percent risk per trade with 20 positions amplify results; a 10 percent ATR stop is very tight, so gap/stop slippage is a first-order risk. Fills at the exact stop price in a backtest on minute data are optimistic; the QuantConnect thread flagged stop-placement timing differences between minute backtests and live fills. Commenters there also reported that results looked weak in other years, that filters such as a higher price floor hurt performance, and suspected selection bias [PRAC, anonymous forum comments, unverified]. A replication with 1,000 stocks found a good 2016 only (Sharpe 2.396 vs. 0.836 for SPY) and 17 of 25 parameter sets beating the benchmark [PRAC, forum post; period limited].
- Slippage and market impact are not modelled; small-cap, news-driven names at the open have wide spreads. This is the largest threat to the result.
- CXO Advisory's summary reproduces the rules and calls out that the paper's results are behind a paywall on their page; it is a secondary source.

Zarattini-Aziz VWAP trend paper (SSRN 4631351; QQQ 2018-2023): authors claim $25,000 became $192,656 (671 percent), max drawdown 9.4 percent, Sharpe 2.1, and a TQQQ variant 8,242 percent. Net of commissions only. A QuantConnect page said several public replications were far weaker [PRAC, unverified]. Promotional; treat as unverified.

Zarattini-Aziz-Barbon SPY intraday momentum [WP]: 2007 to early 2024, total return 1,985 percent, annualised 19.6 percent, Sharpe 1.33, stated as net of costs; paper states commissions and slippage were assessed but I did not see assumptions. A follow-up forum post by Maroy reports Sharpe over 3 and returns over 50 percent after optimising all parameters and trying different exits, with no stated period, costs or out-of-sample test [PRAC; high overfitting risk].

Gao et al. [PR]: S&P 500 ETF (1993-2013 in the published abstract) first half-hour return predicts last half-hour return; stronger on volatile, high-volume, recession and macro-news days; present in ten other ETFs. Earlier working-paper numbers, as summarised by CXO: in-sample R-squared about 0.02 (0.035 with the 12th half-hour, 0.048 in high-volatility), out-of-sample R-squared up to 0.018/0.027; trading rule about 6.3 percent gross annualised versus -0.5 percent for always holding the last half-hour; frictions ignored. CXO's own 441-day replication (2012-2014) gave R-squared 0.014. These R-squared values come from a secondary summary of a working version, not the JFE paper. Post-publication: a QuantConnect SPY/IWM/IYR replication (2015 to 2020) had a negative Sharpe over the full period (-0.628) and lost to its benchmark most of the time, with no cost assumptions stated [PRAC; very short sample]. This suggests decay or fragility.

Baltussen et al. [PR]: more than 60 futures, 1974-2020, last-30-minute predictability from earlier-day returns, reversing over following days, linked to gamma hedging demand.

Heston et al. [PR]: NYSE data 2001-2005; continuation at exact one-day multiples, strongest in first and last half-hours; the mechanism is not proven.

Crabel-style futures ORB: third-party backtests on a 42-market portfolio (from 1980) exist but are shown mainly at zero or a $50-100 round-turn cost sensitivity; I found no source confirming profitability after costs [PRAC, secondary].

## 6. Failure regimes and risks

- Low-volume or range-bound days: breakouts reverse; a 17-25 percent win rate means long losing streaks.
- Gap days and halts: stops fill far from the trigger.
- Regime change in hedging demand: the index effect depends on dealer gamma and leveraged-ETF flows.
- Crowding: ORB is widely taught; opening-minute spreads are widest, and stop orders cluster at the same range highs.
- Costs: per-share commissions are small relative to spread/slippage; borrow for shorts in small caps and locate failures.
- Overfitting: shopping among 1/5/15/30/60-minute ranges, ATR multiples, relative-volume cut-offs and filters.
- PDT and margin rules for sub-$25k accounts; leverage amplifies gap losses.
- Single-sample bull-market bias.

## 7. MY TWIST (hypotheses, NOT backtested)

### Twist 1: Cost-aware Stocks in Play (execution-gated ORB)
- Rationale: paper edge may be consumed by spread and stop slippage in the most extreme relative-volume names.
- Rule change: keep the 4a rules; add a pre-trade estimated cost c = half-spread plus k times participation (shares / opening-range volume) and skip the trade if expected gross edge 0.08R-0.38R minus c is below a threshold; use limit-if-touched or a capped market order rather than a pure stop; rank by relative volume divided by spread in bps.
- Parameters: k, max spread (5-30 bps), entry slippage assumption (1-10 bps), ATR stop fraction (5-20 percent).
- Expected effect: lower gross return, more realistic and possibly higher net Sharpe.
- Falsification: if net Sharpe under a stress of 5 bps round-trip slippage plus half-spread is below 1.0 in out-of-sample years, or the gated version does not beat the ungated one net of the same costs, abandon.

### Twist 2: Catalyst-split ORB
- Rationale: relative volume mixes earnings, news and index events with random volume spikes.
- Rule change: tag each name as earnings-day, gap greater than 1 ATR, or other; trade only categories whose in-sample R per trade is positive and stable; require the opening gap and first candle to agree in sign.
- Parameters: gap threshold (0.5-2 ATR), relative-volume floor (100-300 percent), top N (5-20).
- Expected effect: fewer trades, higher R per trade.
- Falsification: if the gap-agreement tag adds no statistically significant incremental R per trade over relative volume alone in a regression with year fixed effects (p above 0.10 out of sample), drop it.

### Twist 3: Gamma-gated last-half-hour trade
- Rationale: Baltussen et al. tie the effect to hedging demand; if true, the signal should be stronger when dealers are short gamma and weaker otherwise.
- Rule change: trade the Gao signal only when a gamma proxy (for example sign of dealer net gamma from public open interest estimates, or high VIX with large option volume) indicates short-gamma conditions and the first-half-hour move exceeds a threshold of recent volatility.
- Parameters: volatility threshold (0.5-1.5 daily sigma), gamma proxy definition, holding window (last 30 or 60 minutes).
- Expected effect: fewer, larger-edge trades; the unconditional effect looks too small to survive costs.
- Falsification: if net P&L per trade at 1 bp round-trip cost in the 2018-present sample is not positive with a block-bootstrap confidence interval excluding zero, or the gamma-gated subset shows no larger effect than the ungated one, reject.

## 8. Implementation spec

Data: 1-minute (better, tick) bars and NBBO for the whole US universe, corporate actions, borrow availability, earnings calendar, pre-market volume. Survivorship-free universe (the paper used CRSP). For index version: 1-minute SPY/ES data, prior close, option open interest if using a gamma proxy.

Signals: opening-range high/low and candle colour; relative volume; ATR(14) daily; for index: first-half-hour return.

Sizing: risk-based (1 percent of capital divided by stop distance), cap leverage and per-name notional, cap shares at a small fraction of expected volume.

Execution: at 09:35 place stop-entries for the top names; cancel unfilled at a cutoff (for example 11:00); flat by 15:55-16:00. Use capped marketable limit orders; avoid trading names with spread above the limit.

Costs: commission (the paper: $0.0035/share), half-spread at entry and exit, stop slippage as a multiple of spread, short borrow fees, SEC/FINRA fees, market-data fees. Stress at two to three times estimated slippage.

Pseudo-code:
```
09:35: for s in universe: if px>5 and adv14>=1e6 and atr14>0.5:
    rv[s] = vol_0930_0935[s]/mean(vol_0930_0935 last 14d)
  pick top20 with rv>=1
  for s in picks: dir = sign(close_0935-open); if dir==0: skip
    entry = high_0935 if dir>0 else low_0935
    stop  = entry - dir*0.10*atr14
    qty = min(0.01*equity/abs(entry-stop), 4*equity/20/entry, vol_cap)
    place stop-entry order
intraday: on fill -> place stop; at 15:59 flatten all
```

## 9. Backtest plan

- Survivorship-free universe, point-in-time ADV/ATR, adjust for splits properly (the paper used unadjusted intraday data to avoid look-ahead; replicate that).
- Replicate the paper first, then test cost stress. Walk-forward by year: choose parameters on years 1..k, test year k+1; a final untouched hold-out period (for example the latest 2 years, which postdate the paper's sample).
- Multiple testing: log every variant (range length, ATR fraction, relative volume cut, top-N); report deflated Sharpe, and use SPA/reality-check across the variant set; apply Bonferroni or Benjamini-Hochberg to per-feature tests.
- Index version: use predictive regressions with HAC errors, out-of-sample R-squared versus a rolling-mean benchmark, then trading net of cost; test sub-periods before and after 2014 publication.
- Metrics: net R per trade, hit rate, payoff ratio, Sharpe, max drawdown, worst day, turnover, capacity (fraction of volume), P&L concentration (top 5 percent of trades share of profit), and alpha versus market, momentum and short-term reversal factors.

## 10. Risk management and kill-switch

- Per-trade 1 percent at stop (or lower while unverified), max gross leverage below 4x, max positions, per-name volume cap.
- Daily loss limit (for example 3 percent), consecutive-loss pause, and a rolling 60-day live-vs-backtest expectancy comparison: stop trading if live net R per trade is below zero with lower confidence bound over a set number of trades.
- Halt-aware logic, no trading on days with exchange issues, and no new entries after a cutoff.
- Kill if realised slippage exceeds twice the modelled slippage for two weeks.
- Start with paper then minimum size; the strategy's low win rate demands patience and strict rule adherence.

## 11. Annotated sources

| # | Source | Type | Grade | Note |
|---|---|---|---|---|
| 1 | Zarattini, Barbon, Aziz, A Profitable Day Trading Strategy for the U.S. Equity Market (SSRN 4729284); PDF https://www.alexandria.unisg.ch/server/api/core/bitstreams/3c2989c4-688d-4d78-8a71-f02690990d51/content | Working paper | B | Read full text; authors have commercial interest; costs = commission only |
| 2 | CXO Advisory summary https://www.cxoadvisory.com/individual-investing/intraday-trading-of-overactive-stocks-via-opening-range-breakout/ | Blog summary | B | Confirms rules; paywalled results |
| 3 | QuantConnect forum replication https://quantconnect.com/forum/discussion/18444/Opening+Range+Breakout+for+Stocks+in+Play/p0/comment-37562 | Forum | C | Partial replication, anonymous comments |
| 4 | Zarattini, Aziz, Barbon, Beat the Market (SFI 24-97) https://www.sfi.ch/de/publications/n-24-97-beat-the-market-an-effective-intraday-momentum-strategy-for-s-p500-etf-spy and https://concretumgroup.com/beat-the-market-an-effective-intraday-momentum-strategy-for-sp500-etf-spy/ | Working paper abstract | B | Abstract only; rules not verified |
| 5 | Maroy follow-up https://forums.bearbulltraders.com/topic/4002-improvements-to-intraday-momentum-strategies-using-parameter-optimization-and-different-exit-strategies/ | Forum | C | No costs or OOS |
| 6 | Gao, Han, Li, Zhou, Market intraday momentum (JFE 2018) https://www.sciencedirect.com/science/article/pii/S0304405X14002323 | Paper | A | Fetch blocked; read via secondary summaries |
| 7 | CXO on Gao et al. https://cxoadvisory.com/calendar-effects/first-and-last-half-hours-of-trading-linked | Blog | B | Source of R-squared numbers and 441-day replication |
| 8 | QuantConnect intraday ETF momentum https://www.quantconnect.com/learning/articles/investment-strategy-library/intraday-etf-momentum | Replication | C | Short sample, no costs |
| 9 | Baltussen, Da, Lammers, Martens (JFE 2021) https://ideas.repec.org/a/eee/jfinec/v142y2021i1p377-403.html | Paper | A | Read via search summary |
| 10 | Heston, Korajczyk, Sadka (JF 2010) https://ar5iv.arxiv.org/html/1005.3535 | Paper | A | Read via search summary |
| 11 | Zarattini and Aziz VWAP paper summary https://concretumgroup.com/volume-weighted-average-price-vwap-the-holy-grail-for-day-trading-systems/ | Promotional summary | C | Authors' claims |
| 12 | Crabel ORB summary (oxfordstrat and others) https://oxfordstrat.com/trading-strategies/narrow-range/ | Practitioner backtests | C | Secondary; book not read |

## 12. Open questions

1. Does the Stocks-in-Play edge survive realistic spreads and stop slippage, and the 2024-2026 period (post-sample)?
2. Is it just post-earnings-announcement drift observed early in the day? Needs a regression against gap and earnings dummies.
3. Why would 5-minute ranges beat 15/30/60-minute ones (authors say unclear)? Possible sample artefact.
4. Has the last-half-hour effect decayed post-2014 and with growth of zero-day options?
5. What are the exact SPY noise-area definitions and costs in the Beat the Market paper (read the full text)?
6. How correlated is the strategy with other short-term momentum and volatility factors?
