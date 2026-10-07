# B4. Pairs Trading and Statistical Arbitrage

Status: research dossier, written 2026-10-07. Research only, not investment advice. Section 7 twists are hypotheses I have NOT backtested. "Read" = I read the document text; "snippet" = only a search-result abstract or secondary summary, so second-hand.

## 1. Summary, horizon, asset class, holding period

Pairs trading buys the recent relative loser and shorts the recent relative winner of two historically co-moving stocks, expecting the gap to close. Statistical arbitrage generalises this: a stock is traded against a basket (sector ETFs or principal-component "eigenportfolios"), and the residual's deviation from its mean (an Ornstein-Uhlenbeck s-score) triggers trades. Machine-learning versions forecast next-day relative returns for the whole S&P 500 and trade the extremes. Asset class: liquid US equities (also ETFs, other markets). Horizon: days to a few weeks for pairs (Gatev et al. hold on average about two openings in a six-month window; Avellaneda and Lee residual half-lives are of order days to weeks); one day for the ML versions.

Critical headline: every serious study I read finds the profits large in the 1960s to 1990s, much smaller after costs, and weak or negative after about 2002 to 2010. Chen, Chen and Li (2019) argue pairs profits are largely explained by short-term reversal and one-month industry momentum, so "pairs trading" may be mostly the reversal premium of B1 repackaged. This is a strategy with a documented history of decay; treat it as research, not a ready alpha.

## 2. Origin and who uses it

- Practitioner origin: Gatev et al. report that interviews with pair traders say traders look for stocks whose prices "move together"; the strategy is commonly credited to Morgan Stanley quant desks in the mid-1980s (that attribution is not in the sources I read; treat as unverified folklore).
- Gatev, Goetzmann and Rouwenhorst (first draft 1998, RFS 2006): distance method (read).
- Avellaneda and Lee (2010 Quantitative Finance, circulated 2008): PCA and ETF residual stat arb (read).
- Khandani and Lo (2007 JIM): the August 2007 quant unwind, based on a simulated contrarian strategy (summary read).
- Do and Faff (2010 FAJ, 2012 JFR): does simple pairs trading still work, and robustness to costs (snippets).
- Chen, Chen, Chen and Li (2019 Management Science): empirical investigation of an equity pairs strategy using correlation-based pairs (snippet).
- Rad, Low and Faff (2016 Quantitative Finance): distance vs cointegration vs copula (read via BSIC and CXO summaries and the abstract).
- Krauss, Do and Huck (2017 EJOR): deep nets, gradient-boosted trees, random forests on S&P 500 (read the FAU discussion paper).
- Users: quant equity market-neutral hedge funds and prop desks; the academic papers argue capital in the style grew and the edge compressed (Khandani and Lo; Do and Faff).

## 3. Economic rationale and who is on the other side

- Temporary mispricing of close substitutes (Gatev et al.): two firms with similar fundamentals should have prices that do not drift apart; liquidity demand in one leg causes temporary divergence. The authors link profitability to a common factor in pairs returns.
- Liquidity provision / reversal. The strategy is long recent underperformers and short outperformers, which is what a liquidity provider does (Nagel; see B1). Chen et al. report the pairs return decomposes into short-term reversal plus pairs momentum, with the latter largely explained by one-month industry momentum (snippet).
- Inventory and volume: Avellaneda and Lee find that adjusting signals for trading volume helps (signals on low volume are more likely reversals; on high volume more likely information), consistent with liquidity-driven moves reverting.
- Counterparties: investors with short-term liquidity needs, momentum-chasing flow, and index/ETF creation-redemption flow that pushes constituents away from peers.
- Why the edge is dangerous: pairs can diverge because fundamentals changed. The trade has convergence, fundamental and "synchronisation" (crowding) risk (Do and Faff frame it as risky arbitrage, snippet).

## 4. Canonical rules

A. Distance method (GGR). From the paper (read) and Quantpedia (read):
- Universe: liquid CRSP stocks (the paper eliminates stocks with a no-trade day in the formation period; I did not capture all details).
- Formation: 12 months of daily data; build a cumulative total-return index for each stock normalised to 1 at the start; for each stock find the partner that minimises the sum of squared differences of normalised prices; rank pairs by distance.
- Trade the top 5 or top 20 pairs (also pairs 101 to 120) over the next 6 months.
- Open: long the lower-priced leg, short the higher-priced leg when normalised prices diverge by more than 2 historical standard deviations of the formation-period spread; $1 long, $1 short.
- Close at first crossing (spread reaches zero); positions open at the end of 6 months are closed; pairs can reopen. Trading signals use closing prices; the authors also test waiting one day to trade, to approximate bid-ask costs.
- Excess return computed both on fully-invested capital and on committed capital (the conservative one).

B. Cointegration variant (Rad-Low-Faff, BSIC summary read): rank closest pairs, test cointegration (for example Engle-Granger), estimate the hedge ratio, trade the normalised spread with plus/minus 2 entry and zero exit.

C. Avellaneda-Lee PCA stat arb (read):
- Universe: stocks with market cap above $1 billion at the trade date; 60-day trailing window for parameter estimation (about one earnings cycle).
- Residuals: regress each stock's returns on market-cap-weighted sector ETFs, or on the top PCA eigenportfolios of the correlation matrix.
- Model each residual's cumulative process as an OU process; compute the s-score (distance from equilibrium in standard deviations).
- Entry: buy when s-score is below about -1.25, short when above +1.25; exit longs near -0.50; exit shorts near +0.75 (the paper's values: sbo = sso = 1.25, sbc = 0.75, ssc = 0.50 as printed).
- Costs in the back-test: the main text states 5 bps per trade (10 bps round trip); a later passage mentions 10 bps per trade as a friction coefficient; I could not reconcile them from my reading (check the paper).
- Variant: use "trading time" (volume-weighted) instead of calendar time.

D. ML stat arb (Krauss-Do-Huck, read): S&P 500 constituents, point-in-time (survivor-bias removed); features = lagged returns over many horizons; train models to predict probability of outperforming the cross-sectional median next day; go long the top k and short the bottom k (k = 10 gives 10 longs and 10 shorts), hold one day; cost 0.05% per share per half-turn.

## 5. Evidence

Label: P = peer-reviewed; W = working paper; V = vendor/practitioner; U = unverified.

- (P, read) Gatev-Goetzmann-Rouwenhorst, daily CRSP data 1962 to 2002. Top-20 pairs, positions opened and closed on the signal day (no delay): 1.44% per month fully invested (t=11.56), 0.81% per month on committed capital; top-5: 1.31% and 0.78%. Waiting one day to trade cuts the top-20 return from 1.44% to 0.90% per month; the authors treat that gap as an estimate of bid-ask and cost per round trip (about 162 bps per pair round trip in their reading). Sub-period: after 1988 raw top-20 excess return fell from about 118 to about 38 bps per month, while risk-adjusted returns fell by about a third (67 to 42 bps per month, t of 4.41 and 3.77). Hold-out 1999 to 2002 (circulated first draft in 1999, so a genuine out-of-sample test of the original model): fully invested top-20 excess return about 10.4% per annum with 3.8% annual standard deviation. Short-recall stress: about 85 bps per month for the top-20. Not stated as certain: the paper notes that 71% of the stocks in the top-20 pairs are utilities in the unrestricted version (concentration risk). Costs: effective spread estimates from the one-day delay are about 70 to 81 bps per trade, larger than modern large-cap spreads, so the cost handling is conservative for large caps today but uses 1962 to 2002 market structure.
- (V, read) Quantpedia: top-20 pairs net of the paper's cost estimate, 0.81% per month gives 11.16% annualised, volatility 5.85%, Sharpe 1.22 (these are derived from the paper's committed-capital figure; Quantpedia's own max drawdown entry is labelled "not stated").
- (P, snippet) Do and Faff (2010 FAJ): profitability kept declining; strong in prolonged turbulence like the GFC; within narrower industry groups adds about 22 bps per month for bank stocks. (P, read abstract) Do and Faff (2012 JFR), 1963 to 2009: after commissions, market impact and short-selling fees, profits are "much more modest"; risk-adjusted return of about 30 bps per month for well-matched pairs in refined industry groups; about 24 bps per month alpha in the largest 30% of stocks; both pairs and industry-relative reversal are largely unprofitable after 2002.
- (P, read via summaries) Rad-Low-Faff, July 1962 to December 2014: average monthly excess return 91 (distance), 85 (cointegration), 43 (copula) bps before costs and 38, 33, 5 bps after time-varying costs; net Sharpe ratios 0.33, 0.34, 0.08; maximum net drawdown -12%, -17%, -20%. Performance peaked around 1990 and faded to unattractive levels after about 2000; opportunities fell about 40% (distance) and 35% (cointegration) between 2007 to 2011 and 2012 to 2014; returns are negatively related to market liquidity; strategies did better in the worst 20% of market years. About 62.5% (distance) and 61.4% (cointegration) of trades converged within a month; open, non-converged trades hurt returns and fatten the left tail. The authors warn about data snooping (multiple methods tried on the same data) and note borrowing costs may be understated.
- (P, snippet) Chen, Chen, Chen, Li (2019): correlation-based pairs strategy yields abnormal returns, but they come from short-term reversal and a one-month industry momentum version of pairs momentum.
- (P, read) Avellaneda-Lee: after costs (10 bps round trip per their stated back-test assumption in the introduction), PCA-based strategies had an average annual Sharpe ratio of 1.44 over 1997 to 2007, but only 0.9 in 2003 to 2007; ETF-based strategies 1.1 over 1997 to 2007 with a similar degradation after 2002; volume-adjusted ETF strategies reached 1.51 in 2003 to 2007. Back-tests with actual ETFs were only possible from 2002. Their own admission: simulations are out-of-sample in the sense of rolling estimation, and they stay simple to avoid data mining, but they are still simulations on 1996 to 2007 data and don't include borrow costs explicitly in what I read.
- (P/W, read) Khandani-Lo: the simulated Lehmann/Lo-MacKinlay contrarian strategy showed decaying average daily returns as industry assets grew (low of 0.13% in 2006 per a secondary reading), managers added leverage, and the strategy lost heavily in the week of 6 August 2007 then rebounded on 10 August. This is the best-documented crowding failure for this family.
- (P/W, read) Krauss-Do-Huck: S&P 500, December 1992 to October 2015, k=10: ensemble 0.45% per day before costs and 0.25% per day after 0.05% per share half-turn costs; annualised Sharpe before costs about 4.7 for the ensemble over the full period (their table); but in January 2010 to October 2015 all base learners and the ensemble returned negative annualised returns between about -14% and -25% after costs, with Sharpe ratios roughly -0.2 to -0.3 (table 4); they note returns were still positive before costs and attribute the decline to the spread of ML tools and cheaper compute. Feature importance in their models concentrates on the last 4 to 5 daily returns, which says the ML models largely rediscover short-term reversal (my interpretation of their ranking).
- (U) Hedge-fund anecdotes about current stat-arb performance are not in my sources.
- Generic prior: McLean and Pontiff (JF 2016, snippet): average anomaly return fell about 58% post-publication.

Net judgement: classical simple pairs trading is dead or marginal for retail-scale net-of-cost trading after about 2002; the surviving edge, if any, is in more sophisticated, higher-frequency, volume-aware, risk-controlled implementations run with institutional cost structures, and it is probably mostly reversal.

## 6. Failure regimes and risks

- Crowded unwinds (August 2007; also March 2020 and momentum-reversal episodes): correlated losses across all stat-arb books, spreads widen further after stopping out, then rebound.
- Structural breaks: mergers, litigation, fraud, regulatory change, index inclusions turn a divergence permanent; non-converging trades produce fat left tails (Rad et al.).
- Costs and short constraints: borrow fees, recalls, hard-to-borrow names, uptick/short-sale bans; the gap between gross and net is large (Rad et al.: 91 to 38 bps).
- Regime dependence: the strategy tends to do better in volatile/bear years (Rad et al.), but fails in liquidity crises when everyone deleverages.
- Pair instability: pairs formed on 12 months of prices often stop being substitutes in the next six months (Quantpedia reading of Chen et al.).
- Overfitting: hundreds of thousands of potential pairs; the best-looking spread in formation is selected on noise.
- Model risk for PCA: eigenportfolios rotate; the number of factors is a parameter.
- Data snooping inherent in ML: Krauss et al. show a deep-learning edge that disappeared within 15 years.

## 7. MY TWIST (hypotheses, NOT backtested)

Twist 1: News-filtered, volume-aware PCA residual reversal with a convergence stop.
- Rationale: Avellaneda-Lee find volume weighting helps; the BSIC summary of Rad et al. suggests avoiding positions opened on days with firm-specific news and adding stop-losses; Da-Liu-Schaumburg (B1) indicate news-free reversal is cleaner.
- Rule change: implement Avellaneda-Lee on a $2B+ universe with s-score entry at 1.25 but (a) skip any residual signal when the stock had earnings, an 8-K, or an analyst revision in the last 2 days; (b) scale the s-score by relative volume (signal on volume below the 20-day average gets more weight); (c) exit if |s| exceeds 3 or after 2x the estimated OU half-life without convergence.
- Parameters: window {40, 60, 90 days}; entry {1.0, 1.25, 1.5}; volume weighting on/off; news filter on/off; stop {2.5, 3, none}; number of PCA factors {5, 10, 15}.
- Expected effect: fewer trades, higher win rate and thinner left tail than the baseline; Sharpe improvement of unknown size, plausibly modest.
- Falsification: reject if, in 2012 to 2026 out-of-sample with 2x costs stress, the filtered variant does not beat the plain baseline in net Sharpe with a block-bootstrap p<0.10, or if the net Sharpe of either is below 0.5 for large caps.

Twist 2: Cointegration persistence gate with rolling pair retirement.
- Rationale: only about 62% of trades converge in Rad et al.; relationships break. A live test of the relationship can retire dead pairs earlier.
- Rule: pick candidate pairs within the same industry group (narrower groups helped in Do and Faff) using distance rank, require an Engle-Granger p-value below 0.05 in the formation window and an OU half-life between 3 and 20 trading days; re-test every 20 days on the trailing 120 days and retire the pair (close and ban for 6 months) if the p-value exceeds 0.20 or the half-life leaves the band.
- Parameters: p-value thresholds {0.01, 0.05, 0.10}; half-life band; retest interval {10, 20, 40}; formation {120, 252 days}.
- Expected effect: lower non-convergence share and a thinner left tail; fewer tradable pairs; more turnover from retirements.
- Falsification: reject if the share of converged trades does not exceed the baseline distance method's share by at least 5 percentage points out of sample, or if net Sharpe is not higher than the ungated distance method in 2 of 3 non-overlapping sub-periods after 2002.

Twist 3: Crowding-aware deleveraging.
- Rationale: Khandani-Lo describe an unwind with sharp losses then rebound; Nagel shows reversal returns are highest and most volatile in stress.
- Rule: compute a daily crowding gauge: the return of a simple market-neutral short-term reversal factor (long 10 percent losers, short 10 percent winners over 5 days) and the cross-sectional average pairwise residual correlation. If the factor loses more than 2 trailing-year standard deviations over 3 days, cut gross exposure by 50% for 5 days and block new entries until the gauge normalises; do not add risk on the rebound until the factor recovers half of the loss.
- Parameters: loss trigger {1.5, 2, 3 sigma}; cut size {25, 50, 75%}; cooldown {3, 5, 10 days}.
- Expected effect: lower max drawdown in unwind events at the cost of missing the rebound; must be weighed against lost return.
- Falsification: reject if max drawdown is not reduced by at least 20% relative to baseline while Sharpe falls by no more than 10% over the sample including 2007, 2008, 2020, and 2022; or if the rule produces fewer than 3 independent trigger events (inconclusive, not accepted).

## 8. Implementation spec

Data: adjusted daily (and for execution, intraday) prices with dividends, point-in-time constituents and delistings; sector/industry classification (GICS or SIC) with history; ETF prices for sector hedges; volume; corporate actions and news/earnings calendars; borrow availability and fees by name; short-interest.
Signals: distance (SSD of normalised prices), cointegration test and hedge ratio (OLS or total least squares), OU parameters (AR(1) fit: kappa, mean, sigma, half-life), s-score; PCA eigenportfolios from the trailing 252-day correlation matrix; volume-adjusted time scaling.
Sizing: dollar-neutral per pair (or beta-neutral to sector ETF); position risk equal across pairs using spread volatility; gross cap 4x for market-neutral with at most 100 live pairs, each at most 0.5% of NAV risk; sector net exposure within 2%; total beta near zero.
Execution: trade at close or next open using limit orders; for entry use the signal-bar's last price only as a reference; do not assume fills at the signal price (GGR's own one-day delay cut returns by about a third in their sample).
Stops: spread stop (|s| above 3 or loss of 2x spread std), time stop at 2x half-life or 40 days, pair retirement on cointegration failure, corporate-action stop.
Costs: for $2B+ names assume 2 to 5 bps half-spread plus square-root impact; borrow 25 to 300 bps annualised, with hard-to-borrow excluded; commissions; double all costs in stress. Avellaneda and Lee use 5 to 10 bps per trade; GGR's effective spreads (about 70 to 81 bps) represent a pessimistic bound for large caps.

Pseudo-code:
```
daily after close:
   R = residuals(returns[universe], factors=PCA(corr_252d, n=k))   # or sector ETFs
   for s in universe where mcap>2e9 and borrow_ok(s):
       (kappa, m, sigma) = fit_OU(cumsum(R[s][-60:]))
       if kappa<252/30: continue                                   # require half-life under ~30 days
       sc = (X_t - m)/sigma_eq
       if news_flag(s,2) or vol_ratio(s) high: sc *= 0.5           # twist 1 filter/weighting
       if flat and sc < -1.25: go_long(s, hedge=factor_betas)
       if flat and sc >  1.25: go_short(s, hedge=factor_betas)
       if long and sc > -0.5 or short and sc < 0.75: close(s)
       if abs(sc)>3 or days_held>2*halflife: stop(s)
```

## 9. Backtest plan

- Data/universe: US stocks 1996 to 2026, $1B+ and later $2B+ point-in-time universe; ETFs from 2002.
- Out-of-sample design: freeze rules on 1996 to 2007 (matches Avellaneda-Lee), validate on 2008 to 2016, final untouched test 2017 to 2026. Report each sub-period separately because the literature shows regime breaks around 1988, 2002, 2007 and 2010.
- Multiple-testing control: log all variants; report deflated Sharpe and probability of backtest overfitting (CSCV); Benjamini-Hochberg across the parameter grid; require parameter plateaus; apply a higher t-statistic hurdle (about 3) for the final candidate. Separately run a placebo with randomly permuted pair assignments.
- Costs: time-varying spreads and impact, borrow fees; test fills at next open and VWAP with delay; run 1x, 2x, 3x cost stress and find the breakeven cost.
- Baselines: GGR distance, Avellaneda-Lee PCA, a plain short-term reversal factor (B1), and a market-neutral equal-weight index; check whether the strategy has alpha after controlling for 1-week and 1-month reversal and industry momentum (given Chen et al.).
- Metrics: net Sharpe, Sortino, max drawdown, drawdown duration, hit rate, convergence share, average holding days, turnover, cost as a percentage of gross, beta and factor loadings, tail metrics (VaR/ES), capacity (percent of ADV), performance by VIX regime and in named stress events (Aug 2007, Oct 2008, Mar 2020, 2022).

## 10. Risk management and kill-switch rules

- Per pair: stop on spread blowout (|s| above 3), time stop, pair retirement, and a hard cap on any one name or pair; avoid names with pending M&A.
- Portfolio: sector neutrality, beta neutrality, gross cap, correlation of residual books monitored; daily loss limit 1.5% NAV; weekly loss limit 4%.
- Kill-switches (my thresholds): (1) halve gross exposure on the crowding trigger (Twist 3); (2) suspend new entries if the rolling 60-day realised Sharpe is below -1 or live drawdown exceeds 1.5x the worst out-of-sample backtest drawdown; (3) suspend if the converged share of trades over the last 100 falls under 50%; (4) suspend if borrow cost or recall rate exceeds assumptions by 2x; (5) suspend on any detected data or corporate-action error until reconciled; (6) mandatory annual review: if the live net Sharpe over 3 years is below 0.3, retire.

## 11. Annotated sources

| # | Source | URL | Type | Grade | Read? |
|---|---|---|---|---|---|
| 1 | Gatev, Goetzmann, Rouwenhorst, Pairs Trading (RFS 2006; Yale ICF WP 08-03) | https://c.mql5.com/forextsd/forum/208/Pairs Trading - Performance of a Relative Value Arbitrage Rule.pdf | Peer-reviewed | A | Read |
| 2 | Avellaneda and Lee, Statistical Arbitrage in the US Equities Market | https://math.nyu.edu/~avellane/AvellanedaLeeStatArb071108.pdf | Peer-reviewed (Quant. Finance 2010) | A | Read |
| 3 | Krauss, Do, Huck, DNN/GBT/RF stat arb (EJOR 2017; FAU DP 03/2016) | https://www.iwf.rw.fau.de/files/2016/03/03-2016.pdf | Peer-reviewed | A | Read |
| 4 | Rad, Low, Faff (Quant. Finance 2016) | https://research.bond.edu.au/en/publications/the-profitability-of-pairs-trading-strategies-distance-cointegrat/ | Peer-reviewed | A | Abstract read; details via BSIC and CXO |
| 5 | BSIC, Are simple pairs trading strategies still profitable? | https://bsic.it/are-simple-pairs-trading-strategies-still-profitable/ | Student fund research summary | B- | Read |
| 6 | CXO Advisory, best stock pairs trading method | https://cxoadvisory.com/technical-trading/best-stock-pairs-trading-method | Secondary summary | B- | Read |
| 7 | Do and Faff, Are pairs trading profits robust to trading costs? (JFR 2012) | https://strathprints.strath.ac.uk/41722/ | Peer-reviewed | A | Abstract read |
| 8 | Do and Faff, Does simple pairs trading still work? (FAJ 2010) | https://rpc.cfainstitute.org/research/financial-analysts-journal/2010/does-simple-pairs-trading-still-work | Peer-reviewed | A | Snippet |
| 9 | Chen, Chen, Chen, Li (Mgmt Sci 2019) | https://ideas.repec.org/a/inm/ormnsc/v65y2019i1p370-389.html | Peer-reviewed | A | Snippet |
| 10 | Khandani and Lo (JIM 2007) | https://web.mit.edu/Alo/www/Papers/august07.html | Peer-reviewed | A- | Abstract read |
| 11 | Quantpedia, Pairs trading with stocks | https://quantpedia.com/strategies/pairs-trading-with-stocks | Aggregator | B- | Read |
| 12 | CXO Advisory on Gatev et al. | https://www.cxoadvisory.com/technical-trading/classic-paper-matched-pairs-trading/ | Secondary summary | B- | Read |
| 13 | Krauss, Statistical arbitrage pairs trading strategies: review and outlook (slides) | https://finance.lab.nycu.edu.tw/Students/105莊凱臣/STATISTICAL-ARBITRAGE-PAIRS-TRADING-STRATEGIES-REVIEW-AND-OUTLOOK.pdf | Slides summarising a review | B | Read (partial) |
| 14 | McLean and Pontiff (JF 2016) | https://ivey.uwo.ca/media/3775549/pontiff.pdf | Peer-reviewed | A | Snippet |

## 12. Open questions

1. How much of any residual pairs/stat-arb profit survives after controlling for 1-week/1-month reversal and industry momentum (the Chen et al. critique)?
2. What are realistic live Sharpe ratios for institutional stat arb after 2015? I found no verifiable public data; hedge-fund claims are unverified.
3. Do volume-based time scaling and news filters survive out of sample, or were they tuned on 2002 to 2007?
4. Can cointegration tests on a rolling basis retire dying pairs early enough to matter, given multiple-testing noise in the tests themselves?
5. How should hedge ratios be estimated (OLS vs total least squares vs Kalman) with a stable out-of-sample benefit?
6. Do ETF pairs, ADR/local pairs or cross-asset relative-value (not covered here) have more durable convergence than stock pairs?
7. Why exactly did Krauss et al.'s models stop working after 2010: crowding, regime change, or the end of a reversal premium?
