# B1. RSI(2) and Short-Term Reversal

Status: research dossier, written 2026-10-07; second pass 2026-10-07 (see section 13 for what changed). Research only, not investment advice. Nothing in section 7 has been backtested by me; the section 5 reproduction tests only the plain published-style RSI(2) rules on SPY. "Read" in the source list means I opened and read the document text; "snippet" means I only saw a search-result abstract or summary and the claim is second-hand.

## 1. Summary, horizon, asset class, holding period

Short-term reversal is the tendency of stocks that fell over the last day to month to bounce, and of recent winners to give back gains. Larry Connors and Cesar Alvarez popularised a retail-friendly version: buy a liquid stock or index ETF that closes very oversold on a 2-period RSI while still above its 200-day average, and sell into the first bounce. Academics (Lehmann, Jegadeesh) documented the cross-sectional version from 1990; Nagel (2012) reads the profit as payment for supplying liquidity. Horizon: 1 to 5 trading days (typical hold about 2 to 4 days). Asset class: US equities and equity index ETFs (single-name long/short for the academic version). Typical holding period: about 2 days in one community backtest, longer for scaled variants.

My critical view up front: the academic effect is real but concentrated in small, illiquid stocks and in stress periods, and most of the large-cap, post-2000 version is marginal after realistic costs. The retail RSI(2) index-ETF version is mostly a way of being long equities a small fraction of the time with a high win rate and a bad loss tail, not a proven standalone alpha. Second-pass refinement from my own SPY reproduction (section 5): on plain SPY with the 200-day filter the signal is genuinely better than random entries in an uptrend and shows a small positive market-model alpha, but the strategy is invested only about 5% to 10% of the time, compounds at 2% to 5% a year versus 10.9% for buy-and-hold, and the alpha shrinks to roughly 1.4% to 1.8% a year (t about 1.8 to 1.95) once open fills and 5 bp per side are assumed. Earlier "20% to 35% in market" language applied to other variants (StockCharts RSI(5), Substack single-name tests), not to RSI(2) below 5 or 10 on SPY.

## 2. Origin and who uses it

- Lehmann (1990, QJE, "Fads, Martingales, and Market Efficiency") and Jegadeesh (1990, JF) documented one-week and one-month reversal. Lehmann argued that at a weekly horizon fundamentals should barely change, so reversals look like liquidity or price-pressure effects. Second pass: I read the full text of Lehmann's NBER working-paper version (WP 2533, March 1988; the published QJE text may differ). Jegadeesh (1990, JF 45(3):881-898) I could not obtain: the publisher copy is paywalled and Semantic Scholar lists no open copy, so it stays secondary-summary only. Lo and MacKinlay (1990) argued part of the contrarian profit comes from delayed reaction to common factors rather than overreaction (secondary).
- Connors and Alvarez: "Short Term Trading Strategies That Work" (2008; some sources date it 2009) is the usual source of RSI(2) rules. I did not read the book and did not use the unauthorised full-text copies that circulate online. Second pass: the StockCharts Chart School RSI(2) page (read) attributes to Connors: long when RSI(2) is at or below 5 (he reportedly found higher returns below 5 than below 10), 200-day SMA trend filter, entry near the close or next open, exit on a close above the 5-day SMA, and no stops (stops reportedly hurt in his tests); it gives no sample period, return table or cost assumptions. Other secondary listings (MQL5 product page, search snippets) give a looser variant, RSI(2) below 10 with exit above 65, and Quantified Strategies describes the 2009 "High Probability ETF Trading" R3 rule as RSI(2) below 10, exit above 70, on a 20-ETF basket (rules page paywalled). So the thresholds are a family (5 or 10; exit SMA5 or RSI 65 or 70), and the book's own performance tables remain unverified. The Connors Research ConnorsRSI guidebook (2012) is a related product, not the RSI(2) rules themselves (read).
- Practitioners: quant equity market-neutral funds have run contrarian/reversal books for decades. Khandani and Lo (2007) simulate the Lehmann/Lo-MacKinlay contrarian strategy to study the August 2007 quant unwind (summary read; full paper not read).
- Robeco-affiliated authors (Blitz, Huij, Lansdorp, Verbeek) built the "residual reversal" variant, which is used in factor-investing research (CXO summary read; paper not read).

## 3. Economic rationale: why an edge might exist, and who is on the other side

Mechanism candidates, in order of how well evidence supports them:

1. Liquidity provision / inventory pressure. Selling pressure from impatient or forced sellers moves price away from value; a buyer who absorbs it is paid a premium that reverts. Nagel (2012) uses reversal returns as the proxy for that premium and finds the expected return and conditional Sharpe ratio rise with the VIX, interpreted as intermediaries withdrawing capital in stress. The counterparties are the sellers who need immediacy: funds hitting risk limits, retail panic, index/ETF flows.
2. Illiquidity and bid-ask effects. Avramov, Chordia and Goyal (2006) tie reversals to illiquidity and high turnover and conclude profits are too small to survive trading costs (abstract only, snippet). Part of any measured reversal is bid-ask bounce: in Nagel's data the gap between transaction-price and quote-midpoint returns is large (0.30% vs 0.18% per day gross).
3. Sentiment on the short side. Da, Liu and Schaumburg (2014, snippet) argue reversal that is not explained by fundamental news (proxied by analyst revisions) earns about four times the risk-adjusted return of the standard strategy; liquidity shocks drive the long leg, sentiment plus short-sale constraints drive the short leg. Implication: the long leg is the cleaner liquidity trade.
4. Clientele timing. Lou, Polk and Skouras (2019, read) find short-term reversal profits accrue overnight, not intraday. That matters for execution (section 7).

Who loses: forced or impatient sellers. Who competes: market makers, HFTs and stat-arb funds, which is why the large-cap, high-frequency edge has been competed down.

## 4. Canonical rules

A. Connors-style RSI(2) long-only pullback (as widely reproduced by third parties; thresholds vary by source, so I treat these as a family, not a single canonical rule).
- Universe: liquid index ETFs or large stocks.
- Trend filter: close above 200-day SMA.
- Entry: 2-period RSI (Wilder smoothing) below 5 (some versions below 10) on the close; buy at the close or next open.
- Exit: close above the 5-day SMA (some versions: RSI(2) above 65, or above 70), or close below the 200-day SMA.
- Mirror short version (RSI(2) above 95, price below 200-day) exists in the Backtrex test but is rarely used.
- Scaled variant (R-bloggers 2009): add in steps as RSI falls through 20, 15, 10, 5.
Sources for the rules: Backtrex, backtest.substack, R-bloggers, StockCharts Chart School (all read). Connors' original book thresholds: partly corroborated second-hand (StockCharts: long at RSI(2) of 5 or lower above the 200-day, exit above the 5-day SMA, no stops; other write-ups use below 10 with exit above 65 or 70), but not verified against the book itself.

B. Academic cross-sectional reversal.
- Daily or weekly: rank stocks on past 1-week (or 1-month) return, long losers, short winners, dollar-neutral, optionally market-adjusted (Nagel averages five strategies weighting on negative market-adjusted returns of days t-1 to t-5).
- Monthly "residual" version (Blitz et al.): rank on Fama-French 3-factor residuals standardised by their 36-month standard deviation, long top decile, short bottom decile.

## 5. Evidence

Label key: P = peer-reviewed; W = working paper; V = vendor/practitioner; U = unverified.

Cross-sectional literature
- (P, read) Nagel (2012 RFS), US stocks 1998 to 2010, reversal strategy built from five lookbacks, gross of costs: mean 0.30% per day on transaction prices (Sharpe 8.44) and 0.18% per day on quote midpoints (Sharpe 4.50); hedged versions are similar. The author states that with costs the Sharpe ratios would be much lower. Returns were near 1% per day in the 1998 LTCM and 2000-01 episodes, fell steadily to under 0.2% per day by 2007, then spiked in 2008. Industry-level reversal earned about 0.02% per day (Sharpe 0.56). These are gross numbers on an idealised close-to-close construction; do not read them as achievable.
- (P, snippet via CXO summary) Blitz et al. (2013 JFM), 1926 to 2008, monthly: residual reversal gross Sharpe 1.28 vs 0.62 for conventional; conventional reversal likely unprofitable after costs; residual version net above 8% per year with breakeven round-trip cost of about 0.56%; net 0.67%/month in the 500 largest stocks. Cost estimates came from 1991 to 1993 institutional data, so they may be stale or too optimistic.
- (P, snippet) Avramov-Chordia-Goyal (2006 JF): contrarian profits concentrate in illiquid, high-turnover stocks and are too small to survive costs.
- (W version of P, full text read) Lehmann, NBER WP 2533 (March 1988; published QJE 1990). CRSP daily data, NYSE and AMEX stocks, July 1962 to December 1986. Stocks that were winners in one week averaged about -0.35% to -0.55% the next week and losers about +0.86% to +1.24% (confirms the earlier secondary quote). The zero-investment winner/loser portfolio was positive in roughly 90% of weeks and in each of the 49 six-month periods, with no visible decline over the sample. It is a very high-turnover book (more than 2,000 round trips a week). Under one-way costs of 0.05% to 0.2% (floor traders, large managers) the two one-week strategies stayed positive in every six-month period, but the strategy based on returns two weeks earlier did not, and Lehmann's 0.3% to 0.4% retail-broker cost cases are less comfortable. Sample ends 1986, so this says nothing about the post-2000 large-cap picture.
- (W, full text read) McLean-Pontiff working-paper version (May 2013; 82 characteristics, not the 97 in the published 2016 JF version): average out-of-sample decay about 10% (not significantly different from zero) and post-publication decay about 35% (different from both 0% and 100%); decay larger for low idiosyncratic-risk portfolios, which is the limits-to-arbitrage signature. The published-version figures I quoted below (26% and 58%) remain snippet-level. The paper does not single out short-term reversal in the text I searched.
- (P, summary read) Khandani-Lo (2007): average daily return of the simulated contrarian strategy declined with growth in equity market-neutral assets (a low of 0.13% in 2006, per a secondary abstract summary), managers added leverage, and the strategy suffered a violent unwind in the week of 6 August 2007 followed by a rebound on 10 August.
- (P, snippet) Hou, Xue and Zhang (2020 RFS) report that most anomalies, including trading-frictions ones like short-term reversal, fail to replicate once microcaps are down-weighted (65% of 452 anomalies fail the single-test hurdle). I could not confirm the reversal-specific t-statistic.
- (P, snippet) McLean and Pontiff (2016 JF): across 97 predictors, long-short returns fell about 26% out of sample and 58% post-publication on average (published version, snippet; the working-paper figures I read are in the bullet above). Not specific to reversal, but a sensible prior.

RSI(2) and Connors-family evidence (all V or U, treat sceptically)
- Backtrex Nasdaq-100 test (read): RSI(2)<5, above 200-day SMA, exit above 5-day SMA, October 2016 to October 2026, 0.02% commission per side, no slippage: +26.9% total vs +528.3% buy-and-hold, CAGR 2.4%, max drawdown -25.0%, 65 trades, win rate 75.4%, average win 1.58% vs average loss 3.11%, profit factor 1.55. Same rules on the S&P 500 returned +18.1% in the same decade per the page. Takeaway: high hit rate, tiny edge, poor compounding.
- backtest.substack Nasdaq-100 stocks (read): RSI(2)<10 with SMA filters, December 2006 to late 2025, four slots, 17.84% annual return, Sharpe 1.10, profit factor 1.45, max drawdown 29.15%, no stated costs, unclear survivorship handling. Likely gross and flattered by current-constituent bias; U.
- StockCharts RSI(5) test (read): 2000 to 2016, 5-day RSI 30/70 with golden-cross filter, $10 per trade, next-open fills: SPY about 7% per year vs buy-and-hold 5.22% per year (55% max drawdown), in market 20% to 35% of the time, average win rate 78%. Not RSI(2).
- R-bloggers (read): S&P 500 2000 to 2009 scaled RSI(2), 1,123 trades, max drawdown about -15.7%, no costs, no out-of-sample test.
- Connors Research guidebook (read, disclaimed as simulated and not costed): ConnorsRSI pullback on stocks, 2001 to mid-2012, entry via limit orders 4% to 10% below the prior close, claimed average gains per trade of 8% to 12.5% for the best parameter variants with under two-day durations. I regard this as unverifiable and likely driven by parameter selection and limit-fill assumptions (a limit buy far below the close fills only on the days it hurts least). The guidebook itself carries the standard hypothetical-performance disclaimer.

Second-pass additional practitioner evidence (all V/U)
- Substack "Guru Finance Insights" SPY test (read, free part only): SPY from October 2000 to about September 2026, 200-day filter, RSI(2) below 10, exit RSI(2) above 70 or 10 days, 100% of capital per trade, no stop. 181 trades (about 7 a year), average hold 3.7 days, 82% win rate, time in market 10.2%, max drawdown -13.8% vs -55.2% for buy-and-hold, Sharpe 0.62 vs 0.53, growth of $1 to 2.49 vs 8.68. Costs are said to be "considered" with no figures given; the walk-forward split is paywalled. Tallies with my own reproduction below (same order of magnitude of trades, exposure and drawdown).
- Quantitativo (read): Connors-style 2-day cumulative RSI on large and mega-cap US stocks, about 1998/99 to 2024, at most 3 positions, entry below 10, exit above 65, 200-day filter. Reports about 26.6% a year, Sharpe 1.18, max drawdown 37%, but states no transaction costs, does not address survivorship explicitly, tunes on a 198-parameter grid in-sample, and the author says he would not trade it (drawdown) and suspects the edge has weakened since about 2014. Treat the return as an upper bound.
- Searches for an SSRN paper, thesis or peer-reviewed out-of-sample test of RSI(2) found none; the independent evidence is blogs, forums and vendor pages. Quantified Strategies pages were paywalled or bot-blocked, so I cite their claims only via search snippets.

Own reproduction on SPY (second pass; Python, scripts and data kept in the session scratchpad, not in the repo)
- Data and sample: Yahoo Finance daily SPY via yfinance, dividend-adjusted, 29 January 1993 to 30 September 2026 (8,475 rows); the first 200 days are the warm-up, so strategy statistics start in late 1993 (32.8 years). Ken French daily Mkt-RF/RF file (CRSP 202608 vintage, to 31 August 2026) used for alpha regressions, which therefore end in August 2026.
- Rules (no tuning; the two threshold variants listed in section 4 and nothing else): long when Wilder RSI(2) is below 5 (or below 10) on the close and the close is above the 200-day SMA; exit at the first close above the 5-day SMA or below the 200-day SMA. Two fill assumptions: (a) enter and exit at the signal-day close (MOC), (b) enter at the next open and exit at the next open after the exit signal. Costs 0, 1 bp and 5 bp per side on SPY (a flat assumption, not a spread model). Flat days earn zero in the Sharpe/CAGR rows; the alpha rows add the T-bill rate (RF) when flat.
- Results, RSI(2) below 5: 129 trades, average hold 3.0 days, 80% wins, exposure 4.7% (close fills) or 6.2% (open fills), average gross trade return +0.68%. Close fills: CAGR 2.64% / 2.56% / 2.24% at 0 / 1 / 5 bp per side, Sharpe (rf=0) 0.63 / 0.61 / 0.54, max drawdown -12.5% to -13.5%. Open fills: CAGR 2.43% / 2.35% / 2.03%, Sharpe 0.54 / 0.53 / 0.46, max drawdown -14.8% to -15.8%. Buy-and-hold over the same days: CAGR 10.86%, Sharpe 0.65, max drawdown -55.2%.
- Results, RSI(2) below 10: 265 trades, average hold 3.1 days, 75% wins, exposure 10.0% (close) or 13.2% (open), average gross trade +0.58%. Close fills: CAGR 4.62% / 4.46% / 3.79%, Sharpe 0.82 / 0.79 / 0.68, max drawdown -14.6% to -16.1%. Open fills: CAGR 3.81% / 3.65% / 2.98%, Sharpe 0.66 / 0.63 / 0.52, max drawdown -18.0% to -19.5%.
- Beta check (the "is it just market beta" test): daily regression on Mkt-RF with the cash rate added when flat, Newey-West 5 lags. RSI<5: market beta 0.05, alpha 2.06% a year (t 2.99) with close fills and no costs; 1.98% (t 2.89) at 1 bp; 1.71% (t 2.22) with open fills at 1 bp; 1.40% (t 1.83) with open fills at 5 bp. RSI<10: beta 0.09, alpha 3.42% (t 3.91) close fills no costs; 3.26% at 1 bp; 2.45% (t 2.60) open fills 1 bp; 1.82% (t 1.95) open fills 5 bp. These alphas apply to the whole account while the strategy is deployed only 5% to 13% of the time, so they are small in absolute terms.
- Random-entry control (RSI<5, close fills, no costs): the same number of trades and the same holding lengths, with entries drawn at random from days above the 200-day SMA, averaged +0.14% per trade (5th to 95th percentile -0.07% to +0.35%, 2,000 draws) versus +0.68% for the actual signal; no random draw reached the actual figure. So the RSI trigger adds real information beyond "be long in an uptrend". Caveat: the random trades ignore the exit rule's selection of winners, so the control is crude.
- Sub-periods (RSI<10, close fills, no costs): CAGR 6.16% (Sharpe 1.03) for 1994 to 2006, 2.95% (0.58) for 2007 to 2014, 4.00% (0.71) for 2015 to 2026. Mean daily return on in-market days was 25.0 bp, 12.8 bp and 15.3 bp versus an unconditional SPY mean of 4.7, 3.7 and 5.7 bp. The edge roughly halved from 2007 on (the book appeared in 2008) yet stayed positive, in line with McLean-Pontiff style decay and not a disappearance. For RSI<5: 29.9, 18.6 and 19.8 bp.
- Caveats (heavy): single instrument, one data vendor (Yahoo adjusted prices; the "open" is not an auction fill); 129 to 265 trades give wide error bars (t of 2 to 4 at best); the close-fill rows assume the final close is known when ordering, which a real MOC order at about 15:50 only approximates; flat costs ignore impact and the 2008 and 2020 spread blowouts; the 200-day and SMA5 parameters are the published ones and were chosen by others on earlier data, so the sample is not clean out-of-sample even post-2008; only two thresholds and two fills were run, but the family was fixed before looking. This does not test single-name or long-short reversal, the section 7 twists, or any residual-reversal variant.

Net judgement: no peer-reviewed evidence tests the specific RSI(2) rules; the retail evidence is vendor backtests with optimistic or absent cost modelling. My own SPY reproduction finds a real but small effect: an alpha of roughly 1.4% to 3.4% a year on deployed-capital basis, positive in all three sub-periods, vs random-entry controls, but it compounds at far less than buy-and-hold because it is in the market 5% to 13% of the time, and the post-2008 edge is about half the 1994 to 2006 edge. The underlying phenomenon is decayed in large caps post-2000 and revives in stress.

## 6. Failure regimes and risks

- Trend-down crashes: an oversold stock above its 200-day average can keep falling; the loss per losing trade (about 3% in the Backtrex test) is roughly double the win. Example regimes: Feb to Mar 2020 (worst year -12.2% in the Backtrex test was 2020), 2008 style cascades.
- Crowding/unwind: August 2007 quant unwind (Khandani-Lo) shows leveraged reversal books fail together, and the rebound arrives too late for stopped-out holders.
- Costs and microstructure: bid-ask bounce inflates close-to-close backtests; fills at the close or open differ from the signal price. Avramov et al. say the profits are too small after costs in many cuts.
- Small-cap concentration and short-side constraints: borrow fees, recalls, and hard-to-borrow names kill the short leg.
- News-driven drops: reversal does not hold when the fall is fundamental (Da et al.). Earnings gaps trend (see B3).
- Overfitting: thresholds (5, 10, 15; SMA 5, 10) are tuned on the same data. Connors-type guidebooks sweep parameters and report the best.
- Persistence low-vol regimes: signal fires rarely and returns are thin (the Backtrex 65 trades in 10 years).

## 7. MY TWIST (hypotheses, NOT backtested)

Twist 1: Overnight-only capture of the reversal.
- Rationale: Lou-Polk-Skouras (read) report that short-term reversal profits accrue overnight, with intraday returns carrying little. If true for the retail RSI(2) signal, holding through the intraday session to wait for "close above 5-day SMA" adds risk without return.
- Rule change: enter on the closing auction when RSI(2) < 10 and price > 200-day SMA; exit at the next open (limit-on-open) if open is above the entry close, otherwise hold and apply the standard exit.
- Parameters to test: RSI threshold {3, 5, 10}; exit rule {next open, next close, SMA5}; max holding {1, 3, 5} days.
- Expected effect: similar mean return per trade, lower holding time, lower drawdown, but higher turnover costs and more sensitivity to opening auction slippage.
- Falsification: reject if after realistic open/close auction slippage (at least 5 bps per side for ETFs, 10 bps for single stocks) the overnight-only variant has lower net Sharpe than the SMA5 exit in at least 2 of 3 non-overlapping sub-periods (2007 to 2012, 2013 to 2019, 2020 to 2026), or if the overnight share of total trade P&L is below 60%.

Twist 2: VIX-conditional sizing and "residual" ranking for single stocks.
- Rationale: Nagel (read) finds expected reversal returns rise with VIX; Blitz et al. and Da et al. suggest stripping factor and news components improves the signal.
- Rule: rank liquid large-cap stocks by 5-day return residualised against the market, sector, and Fama-French factors; exclude names with an earnings release or analyst revision spike in the last 3 days; long-only bottom decile; scale gross exposure by a VIX percentile (e.g., 1.0x if VIX in the top tercile of its trailing 3-year range, 0.5x middle, 0.25x low).
- Parameters: lookback {3, 5, 10} days; VIX terciles vs 20/30 thresholds; news filter on/off.
- Expected effect: better returns per unit of risk and fewer large losses from fundamental drops; lower capacity use in calm markets.
- Falsification: reject if the VIX-scaled version fails to beat the unscaled one on net Sharpe with a block-bootstrap p-value under 0.10 after correcting for the number of variants tried, or if the news filter removes more than 40% of profits with no Sharpe improvement.

Twist 3 (optional): Breadth-of-selloff trigger.
- Rationale: selling pressure across the market (Boyarchenko et al. note market sell-offs generate robust overnight reversals, see B2) is more liquidity-driven than idiosyncratic drops.
- Rule: only take RSI(2) entries when at least X% of the universe also has RSI(2) < 10.
- Parameters: X in {10%, 25%, 40%}.
- Falsification: no improvement over base rule in net profit factor in 2 of 3 sub-periods.

## 8. Implementation spec

Data: adjusted daily OHLCV (split and dividend adjusted), survivorship-free universe with point-in-time constituents, delisting returns, borrow and fee data for shorts, VIX, earnings calendar, analyst revision feed (optional), opening and closing auction prints (to price MOC/MOO fills).
Signals: RSI(2) with Wilder smoothing on adjusted closes; SMA(200), SMA(5); optional residual return from a 60-day rolling regression on market and sector ETFs.
Sizing: equal-risk per position, 0.25% to 0.5% of equity at risk per trade using a 2x ATR(14) disaster stop; cap 4 to 6 concurrent names; sector cap 30%; gross cap 100% (no leverage in the base spec).
Execution: signals at close, orders as MOC where eligible or next-open limit; ETFs preferred. No limit orders far below the close in testing (to avoid the fill-bias seen in the guidebook).
Stops: time stop (exit by day 5); disaster stop at 3x ATR or -8%; exit if close below SMA(200).
Cost model: ETFs 1 to 3 bps half-spread plus 0.5 bp impact; large-cap stocks 3 to 5 bps plus impact scaled by participation (square-root law), small caps higher; short borrow fee 25 to 300 bps annualised by name; commissions per broker. Stress case doubles costs.

Pseudo-code:
```
for each day t after close:
  for s in universe(t) if liquid(s) and price>5 and adv>$20m:
    rsi2 = RSI(close[s],2); trend = close[s] > SMA(close[s],200)
    if flat(s) and trend and rsi2 < 10 and not earnings_within(s,3):
        queue_buy(s, size=risk_size(s), at=MOC_or_next_open)
  for s in positions:
    if close[s] > SMA(close[s],5) or close[s] < SMA(close[s],200) or days_held>=5:
        queue_sell(s, at=next_open)
```

## 9. Backtest plan

- Universe and period: US large caps plus 10 to 15 index/sector ETFs, 2003 to 2026 (needs ETF history), point-in-time, delistings included.
- Walk-forward: fix design on 2003 to 2012, validate on 2013 to 2019, test untouched on 2020 to 2026; parameter re-estimation only inside a rolling 5-year window with a 1-year step.
- Multiple testing: log every variant run. Report deflated Sharpe ratio and apply Holm or Benjamini-Hochberg across the parameter grid. Prefer plateaus over peaks: require neighbouring thresholds (RSI 5 and 10; SMA 5 and 10) to be profitable.
- Costs: baseline plus 2x cost stress; test next-open vs MOC fills; reject any edge that vanishes at 2x.
- Controls: compare to a random-entry strategy with the same exposure time (the main trap is mistaking market beta in 20% to 35% exposure for alpha) and to buy-and-hold scaled to the same time in market.
- Metrics: net CAGR, Sharpe, Sortino, max drawdown, ulcer index, profit factor, average win/loss, tail ratio, trade count, exposure, alpha vs market (CAPM and FF5+momentum), stability by year and by VIX regime, share of P&L overnight vs intraday, capacity vs ADV participation.

## 10. Risk management and kill-switches

- Per trade: disaster stop and 5-day time stop; no averaging down beyond pre-defined scale-in (if used, total scale-in risk capped at 1x base risk).
- Portfolio: max 6 positions, 30% sector cap, daily loss limit 2% of equity (halt for the day), rolling 20-day drawdown trigger.
- Kill-switch (suggested, my own thresholds, not from sources): pause new entries if (a) live drawdown exceeds 1.5x the worst backtest drawdown, or (b) 10 consecutive losing trades, or (c) rolling 12-month net Sharpe below zero for two consecutive quarters, or (d) VIX above 40 with correlation spike (reversal books have been hurt in unwind events). Resume only after a review.
- Crowding watch: track factor returns for reversal (e.g., published daily short-term reversal factor) and market-neutral fund performance for unwind signals.

## 11. Annotated sources

| # | Source | URL | Type | Grade | Read? |
|---|---|---|---|---|---|
| 1 | Nagel, Evaporating Liquidity (RFS 2012; NBER w17653) | https://nber.org/papers/w17653 and Cochrane-hosted PDF at https://www.johnhcochrane.com/s/Nagel_LiqSupply_9a.pdf | Peer-reviewed | A | Read PDF text |
| 2 | Lou, Polk, Skouras, A tug of war (JFE 2019) | https://personal.lse.ac.uk/polk/research/TugOfWar.pdf | Peer-reviewed | A | Read |
| 3 | Khandani and Lo, What happened to the quants in August 2007 (JIM 2007) | https://web.mit.edu/Alo/www/Papers/august07.html | Peer-reviewed | A- | Abstract only |
| 4 | Blitz et al., Short-term residual reversal (JFM 2013), CXO summary | https://www.cxoadvisory.com/technical-trading/purified-short-term-stock-reversal/ | Secondary summary of peer-reviewed | B | Read summary |
| 5 | Avramov, Chordia, Goyal (JF 2006) | https://ideas.repec.org/a/bla/jfinan/v61y2006i5p2365-2394.html | Peer-reviewed | A | Snippet |
| 6 | Lehmann, Fads, Martingales, and Market Efficiency (NBER WP 2533, 1988; QJE 1990) | https://www.nber.org/system/files/working_papers/w2533/w2533.pdf | Working-paper version of peer-reviewed | A- | Read full WP text (QJE text not seen) |
| 7 | Da, Liu, Schaumburg (Mgmt Sci 2014) | https://ideas.repec.org/a/inm/ormnsc/v60y2014i3p658-674.html | Peer-reviewed | A | Snippet |
| 8 | Hou, Xue, Zhang, Replicating Anomalies (RFS 2020) | https://www.nber.org/papers/w23394.pdf | Peer-reviewed | A | Snippet |
| 9 | McLean and Pontiff (JF 2016); working-paper version (2013) | https://ivey.uwo.ca/media/3775549/pontiff.pdf | Peer-reviewed; WP read | A (published) / A- (WP read) | Read WP full text (82 characteristics); published 97-predictor figures snippet only |
| 10 | Backtrex Connors RSI(2) Nasdaq-100 | https://backtrex.com/en/backtests/connors-rsi-2-nasdaq-100 | Vendor backtest | C+ | Read |
| 11 | backtest.substack, The 2-Period RSI | https://backtest.substack.com/p/the-2-period-rsi-a-simple-system | Blog | C | Read |
| 12 | StockCharts SystemTrader RSI(5) test (Arthur Hill) | https://articles.stockcharts.com/article/articles-arthurhill-2016-12-systemtrader---testing-and-tweaking-an-rsi-mean-reversion-system-for-spy-qqq-and-ijr/ | Practitioner article | C+ | Read |
| 13 | R-bloggers RSI(2) Evaluation (2009) | https://www.r-bloggers.com/2009/06/rsi2-evaluation/ | Blog | C | Read |
| 14 | Connors Research, ConnorsRSI guidebook (2012) | https://c.mql5.com/forextsd/forum/119/connorsrsi-pullbacks-guidebook.pdf | Vendor publication | C | Read |
| 15 | StockCharts Chart School, RSI(2) | https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/rsi-2 | Educational page summarising Connors rules | C+ (rules only, no performance data) | Read |
| 16 | Guru Finance Insights, RSI(2) on 26 years of SPY | https://gurufinanceinsights.substack.com/p/i-backtested-the-classic-rsi2-mean | Blog backtest | C | Read free part (walk-forward paywalled) |
| 17 | Quantitativo, cumulative RSI | https://www.quantitativo.com/p/squeezing-more-profits-with-cumulative | Blog backtest | C | Read |
| 18 | Own SPY reproduction (yfinance + Ken French daily factors) | scratchpad, not in repo | Own computation | C+ (single instrument, vendor data, flat costs) | Ran it |
| 19 | Ken R. French Data Library, daily 3-factor file (CRSP 202608) | https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip | Academic data | A (data) | Downloaded and used |
| 20 | Connors and Alvarez book (2008/2009), Jegadeesh (JF 1990) | not accessed | Book; peer-reviewed | n/a | Not read: book not obtained, Jegadeesh paywalled |

## 12. Open questions

1. What exactly are Connors and Alvarez's original RSI(2) thresholds and sample, and do they survive a point-in-time replication? Partly narrowed: secondary sources say below 5 (or 10), 200-day filter, exit above SMA5 (or RSI 65 or 70), but I still did not read the book and the original sample and tables are unknown. My SPY replication supports a small positive effect for both thresholds; a point-in-time single-stock replication is still missing.
2. How much of RSI(2) index-ETF profit is just equity beta? Partly answered for SPY: beta is only 0.05 to 0.09 because exposure is 5% to 13%, alpha vs Mkt-RF is 1.4% to 3.4% a year, and a random-entry-in-uptrend control gives +0.14% per trade vs +0.68%. Still open for other ETFs and for stocks, and the random control ignores the exit rule.
3. Is the overnight-concentration finding (Lou-Polk-Skouras) true for the retail-signal subset and post-2019 data?
4. Does the large-cap reversal premium still scale with VIX after 2020, as in Nagel's 1998 to 2010 sample?
5. What is the realistic capacity before price impact kills the single-stock version?
6. Does the Connors-style trend filter add anything beyond what a simple market-neutral reversal strategy captures, or does it only reduce exposure to crashes?

## 13. Second-pass changelog (2026-10-07)

Read in full this pass: Lehmann NBER WP 2533 (1988 version); McLean-Pontiff working paper (2013 version); StockCharts RSI(2) page; Guru Finance Insights SPY test (free part); Quantitativo cumulative-RSI post; Ken French daily factors (data).
Tried and failed: Jegadeesh 1990 (publisher paywall; Semantic Scholar shows no open copy); Connors-Alvarez book (not obtained; I deliberately did not use unauthorised copies); Quantified Strategies RSI(2) and R3 pages (bot check or paywall); QuantifiedTrader RSI page (no RSI(2), no results shown).

Changes:
- Summary: removed the loose "20% to 35% of the time in market" claim for RSI(2); my SPY run shows 4.7% to 13.2% exposure for the below-5 and below-10 rules. The 20% to 35% figure belongs to the StockCharts RSI(5) test only.
- Section 2 and 4: Connors thresholds upgraded from "unverified" to "partly corroborated second-hand" (below 5 beats below 10; SMA5 exit; no stops), still not verified against the book. Added that variants use below 10 with exit 65 or 70.
- Section 5: Lehmann upgraded from secondary to full-text-read of the working-paper version; the earlier quoted weekly return ranges were confirmed, and added sample (NYSE/AMEX, 1962 to 1986), 90% positive weeks, and cost survival at 0.05% to 0.2% one-way for the two one-week strategies only. McLean-Pontiff: working-paper figures (82 characteristics, 10% and 35% decay) added; the published 97-predictor 26% and 58% remain snippet-level.
- Section 5: added two more practitioner tests (Guru Finance SPY, Quantitativo) and a new reproduction block (SPY 1993 to 2026, with and without 1 and 5 bp per side, close vs open fills, FF alpha, random-entry control, sub-periods).
- Judgement change: from "no evidence the retail rule has any edge" to "a small, real, decayed gross edge on SPY that is mostly a low-exposure, high-hit-rate profile; costs matter at 5 bp with open fills (alpha t falls to about 1.8 to 1.95)". Still no peer-reviewed RSI(2) test.
- Source grades: Lehmann A to A- (WP version); McLean-Pontiff split published vs WP; new sources 15 to 20 added. The Backtrex, substack and R-bloggers numbers were not re-checked this pass.
- Unchanged: section 7 twists (still untested and not covered by the reproduction), sections 8 to 10. The open-fill reproduction rows are plain next-open entries, not the overnight-capture twist.
- Still not done: Nagel, Lou-Polk-Skouras, Blitz et al., Avramov et al., Da et al., Hou-Xue-Zhang and Khandani-Lo were not re-read; their grades and the Blitz and Hou-Xue-Zhang figures remain snippet or summary level.
