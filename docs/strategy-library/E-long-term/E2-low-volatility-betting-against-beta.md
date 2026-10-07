# E2. Low Volatility and Betting Against Beta

Status: research dossier, not investment advice. Twists in section 7 are untested hypotheses. Dated 2026-10-07.

Source-access note (updated by second pass, 2026-10-07): the first pass could not read the JFE BAB tables. The second pass read in full the Frazzini-Pedersen JFE 2014 publisher's version (CBS portal PDF) and the Novy-Marx and Velikov "Betting Against Betting Against Beta" November 2018 draft (author page), and recomputed BAB, market and factor statistics from the AQR BAB dataset (monthly xlsx dated 31 Jul 2026) and the Ken French library (CRSP 202608 build), both retrieved 2026-10-07. Other items (Blitz-van Vliet, Baker et al., Ang et al., Driessen, COVID drawdowns) remain abstract or secondary-level as graded in section 11. See the "Second-pass changelog" at the end.

## 1. Summary, horizon, asset class, holding period

The low-risk anomaly: stocks (and bonds, futures) with low beta or low volatility have earned equal or higher returns than high-beta, high-volatility ones, so risk-adjusted returns are much better for the low-risk end. Implementations: (a) long-only low-vol or minimum-vol equity portfolios, (b) market-neutral Betting-Against-Beta (BAB), which levers low-beta longs up and de-levers high-beta shorts to a combined beta near zero. Asset class: equities mainly, with extensions to bonds and futures. Horizon: multi-year; rebalance monthly (BAB, academic) or semi-annually/quarterly (commercial low-vol indices). Typical holding per name: 6-12 months, since beta and volatility are persistent.

## 2. Origin and who uses it

- Black, Jensen, Scholes (1972): empirical security market line flatter than CAPM predicts, with higher intercept; NYSE 1926-1965 (secondary summary).
- Black (1972, J. Business 45(3)): restricted borrowing implies a flatter line, a theory for this.
- Ang, Hodrick, Xing, Zhang (J. Finance 2006): stocks with high idiosyncratic volatility had very low average returns. Fu (2005) disputed it, attributing it to lagged volatility estimates and short-term reversal among small high-volatility stocks.
- Blitz and van Vliet (JPM 2007), Robeco: global decile spread of about 12% in annual alpha, 1986-2006, across US, Europe and Japan; used three-year volatility, lower turnover than Ang et al.
- Baker, Bradley, Wurgler (FAJ 2011): benchmarks as a limit to arbitrage.
- Frazzini and Pedersen, "Betting Against Beta" (JFE 111, 2014): AQR principals.
- Novy-Marx and Velikov, "Betting Against Betting Against Beta" (JFE 2022): critique.
- Practitioners: Robeco (conservative equities), AQR (BAB funds), MSCI/S&P/Invesco (min-vol indices and ETFs such as USMV, SPLV). Berkshire-style quality-and-low-beta tilt via "Buffett's Alpha" (alpha insignificant after BAB and QMJ).

## 3. Economic rationale and who is on the other side

1. Leverage constraints (Black 1972; Frazzini-Pedersen 2014): many investors (mutual funds, pensions, individuals) cannot or will not lever, so to reach higher expected return they overweight high-beta assets, bidding them up and lowering their returns. Low-beta assets are relatively cheap. Leverage-constrained investors must de-lever when margin tightens, so BAB returns are low when funding constraints tighten and betas compress toward one (paper's prediction and evidence, per abstract).
2. Benchmarking (Baker-Bradley-Wurgler 2011): managers measured by tracking error against a cap-weighted benchmark and who may not lever have little incentive to buy low beta (it adds tracking error and lowers expected excess return per unit tracking error) or to short high beta.
3. Behavioral: retail lottery preference and overconfidence push demand for volatile stocks (Baker et al.); this overlaps with Ang's idiosyncratic volatility result.
4. Alternative: part of the premium may be a disguised interest-rate exposure (Driessen et al.; see below) and part a quality/profitability and sector tilt.

Other side of the trade: leveraged speculative buyers of high-beta stocks, benchmarked long-only managers, and retail lottery buyers. Honest caveat: the same arguments imply the low-vol premium should shrink as low-vol products absorb assets, which is crowding.

## 4. Canonical rules

A. BAB (Frazzini-Pedersen), from the abstract-level description:
1. Universe: all liquid stocks (the paper also covers 20 global markets, Treasuries, corporate bonds, futures).
2. Estimate beta: monthly. Verified in the JFE paper (second pass): volatilities from a one-year window of daily returns, correlations from a five-year window of overlapping three-day log returns (at least six months of data for volatility, three years for correlation); the time-series beta is shrunk toward the cross-sectional mean of 1 with weight w = 0.6 on the estimate and 0.4 on 1 (the Vasicek factor averages about 0.61, the authors fix 0.6 for all periods and assets). Shrinkage does not change beta ranks but changes the scaling of the legs.
3. Rank by beta; split into low-beta and high-beta groups (weights proportional to the rank deviation from median).
4. Scale the low-beta leg by 1/beta_L and the high-beta leg by 1/beta_H so each has beta 1; long levered low-beta, short de-levered high-beta, self-financing with risk-free rate. The paper's example is $1.4 long low-beta and $0.7 short high-beta in US stocks (verified in the paper: US average $1.40 long and $0.70 short; international $1.40 long and $0.89 short). Weights are proportional to the rank of beta (lower-beta stocks get larger weights in the low-beta portfolio), which is the "non-standard" feature Novy-Marx and Velikov criticize.
5. Rebalance monthly.

B. Commercial low-vol: rank on trailing 1-3 year volatility; hold the lowest-volatility quintile (or optimize min-variance with sector/country caps); rebalance semi-annually; long-only.

## 5. Evidence

Peer-reviewed:
- Black-Jensen-Scholes: flat SML, 1926-1965; but measurement error in beta biases slopes toward zero (secondary).
- Ang et al. (2006): high idiosyncratic volatility earns very low returns. Disputed by Fu (2005).
- Blitz and van Vliet (2007): about 12% alpha spread, 1986-2006; effect not explained by value or size per their paper.
- Baker et al. (2011): 1968-2008 US; lower-risk quintiles had higher returns and smaller drawdowns; secondary report of annualized alphas about 2.6% (low beta) and 2.1% (low vol), unverified against the paper.
- Frazzini-Pedersen (2014), now read in full: BAB earns significant risk-adjusted returns in each asset class studied; BAB return is low when funding constraints tighten. Verified numbers: US stock BAB Sharpe ratio 0.78 for 1926 to March 2012 (about twice the value effect and 40% above momentum over the same period, per the authors); US BAB excess return 0.70%/month (t 7.12) with annualized volatility about 10.75% in Table 2 (some alpha cells garbled in extraction, so I quote only these); US Treasury BAB Sharpe 0.81 with abnormal return 0.17%/month (t 6.26); Sharpe ratios of beta-sorted Treasury portfolios fall from 0.73 (low beta) to 0.31 (high beta). Data: 20 international stock markets, Treasuries, credit, futures; futures data 1963-March 2012. Authors are AQR principals.
- Second-pass recompute on the AQR dataset (US BAB, monthly, dated 31 Jul 2026, retrieved 2026-10-07; AQR rebuilds history on each update and this file starts 1930-12, so values differ from the paper): Sharpe 0.70 and 8.1%/yr (vol 11.5%) for 1930-12 to 2012-03; Sharpe 0.82 for 1963-07 to 2012-03; Sharpe 0.93 for 1957-07 to 2016-12; full 1930-12 to 2026-07 Sharpe 0.70 (7.8%/yr, vol 11.1%). Recent and stress windows: 2007-2020 Sharpe 0.43; 2018-2020 Sharpe 0.23 (2.5%/yr), so BAB did not collapse in the value-drawdown window; 2013-01 to 2026-07 Sharpe 0.68; 2020-01 to 2026-07 Sharpe 0.15 (1.6%/yr). Regression on Fama-French five factors plus momentum (Ken French data, 1963-07 to 2026-07): alpha 0.30%/month (t 2.84), market loading 0.07, RMW 0.48, CMA 0.36, HML 0.21, UMD 0.18; for 2010-01 to 2026-07 alpha 0.43%/month (t 2.65). So gross BAB keeps a significant alpha in the long sample but loads heavily on profitability and investment, consistent with Novy-Marx and Velikov.
- Novy-Marx and Velikov (JFE 2022; figures below are from the November 2018 author draft, now read in full; the published version may differ): BAB construction is effectively equal-weighted and on average commits $1.05 per $1 of BAB to stocks in the bottom 1% of total market cap (about a third of that in the bottom 0.1%); after transaction costs profitability falls by more than 55%, leaving 48bp/month with t = 3.30; generalized alpha versus the Fama-French five-factor model is only 16bp/month, t = 1.20, insignificant. Value-weighted BAB earns 56bp/month (t 3.48) but its Sharpe ratio is 0.49 versus 1.08 for the original BAB, and it earns it by tilting to profitability and investment. In short: after costs a positive return survives, but it is mostly profitability/investment exposure. (The first-pass "roughly 55-60%" cost haircut is tightened to "more than 55%"; no 60% figure was found.)
- Driessen et al. (Tilburg): interest-rate exposure explains between 20% and 80% of unexplained low-vol excess return depending on assumptions (via Quantpedia summary); sign of exposure varies across versions I saw described. Man Group's work found weak links between rate changes and low-vol returns. Mixed.

Practitioner/market evidence:
- COVID 2020: Morningstar-reported maximum drawdowns, USMV 33.1%, SPLV 36.3%, broad market about 35%. So low-vol did not protect uniformly; MFS attributed the failure to normally low-vol sectors becoming volatile. MSCI noted min-vol lagged in the 2020 rebound.
- Crowding: conceptual (concentration into a few names, liquidity squeeze), not measured in the sources I read. Valuation spread data between low and high vol: I found none and make no claim.

Post-publication decay: not quantified by a source I read. The AFP/Novy-Marx debate suggests the arbitrage-resistant portion is in small, illiquid stocks that cost too much to trade.

My read: the low-risk pattern is old and robust in gross terms across markets, but the market-neutral, levered version is an academic object that is poorly investable, and the investable long-only version is a bundle of defensive-sector, rate, quality and size tilts with a spotty crash record. Do not assume the paper's Sharpe ratio is attainable.

## 6. Failure regimes and risks

- Sharp junk/beta rallies after crashes (March-April 2009 style; 2020 rebound) hurt BAB and low-vol; the Daniel-Moskowitz momentum-crash mechanism has a mirror here (my inference, unverified).
- Rising rates / bond-proxy unwinds: utilities, staples and REITs sensitivity; low-vol portfolios behave like long-duration assets in some regimes.
- Funding squeezes for levered BAB: margin calls force de-levering exactly when the spread blows out.
- Valuation: after inflows, low-vol stocks can become expensive; entry valuation matters (concept; no data cited).
- Sector concentration in long-only min-vol (defensives, financials/utilities depending on construction).
- Beta instability: ex-ante betas estimated from past data move; the 2020 episode shows "low vol" labels can be wrong in a regime shift.
- Capacity/cost per Novy-Marx and Velikov.

## 7. MY TWIST (hypotheses, NOT backtested)

Twist 1: Large-cap-only BAB with cost-aware weights and sector neutrality.
- Rationale: removes the micro-cap equal-weight artifact flagged by Novy-Marx and Velikov and the sector bets.
- Rules: universe = top 1,000 stocks by market cap; beta = shrunk (0.6/0.4) one-year-daily/five-year-correlation estimate; within each GICS sector rank by beta; long lowest-tercile, short highest-tercile with cap-weight-capped weights (max 2% per name); scale legs to beta 1 each; monthly with 30% turnover band; leverage cap 2.5x gross.
- Parameters: sector neutral vs not; tercile vs quintile; shrinkage weight 0.5-0.8; cap 1-3%.
- Expected effect: lower paper Sharpe, but higher net-of-cost and lower rate/sector bets.
- Falsification: if net five-factor + momentum alpha t-stat is below 2 over 1990-2025 using realistic costs, or net Sharpe below 0.3, reject.

Twist 2: Rate-hedged low-vol (neutralize duration).
- Rationale: if 20-80% of the premium is rate exposure, hedge it and see what remains; also reduces the 2013-style taper and 2022-style rate-shock risk.
- Rules: long-only low-vol quintile (3-year volatility); estimate rolling 3-year bond beta (10Y Treasury futures returns vs the portfolio, controlling for market); short Treasury futures to neutralize bond beta; reset quarterly.
- Parameters: window 2/3/5 years; hedge ratio 50%/100%; instrument 5y/10y/30y.
- Expected effect: lower correlation with rates; may lower returns in falling-rate periods and help in rising-rate ones.
- Falsification: if the hedged version does not reduce the beta to rate changes out-of-sample (R-squared of monthly returns on 10Y yield change not lower by 30%+ relative) or if its alpha vs FF5+MOM goes to zero, the hedge only removes the premium and the idea has no residual value (a finding, not a failure).

Twist 3: Funding-stress throttle for any levered BAB.
- Rationale: the model predicts low BAB returns when funding tightens; use observable proxies.
- Rules: scale leverage from 1.0x to 0.4x when TED-like or repo-style funding spreads and VIX both exceed their 80th percentile of trailing 10 years; restore with a 2-month lag.
- Parameters: percentile thresholds 70/80/90; lag 1-3 months; proxy choice (OIS-Treasury, FRA-OIS, cross-currency basis; availability varies).
- Expected effect: reduce left-tail months; might whipsaw.
- Falsification: if worst-month and maximum drawdown improve by less than 15% relative in out-of-sample while Sharpe falls, drop it.

## 8. Implementation spec

Data: daily total-return prices, market cap, sector, risk-free and Treasury futures; point-in-time constituents; delisting returns; optional funding spread data.
Signals: beta, volatility ranks as above.
Sizing (long-only): inverse-vol or equal weight within top quintile, 3% name cap, sector tilt limits of +/-10% versus universe; (BAB): leg scaling per section 4 with gross leverage cap.
Execution: monthly/quarterly rebalance, VWAP over 1-3 days, participation under 10% ADV; trade only when deviation exceeds band.
Stops: none at name level; portfolio rules in section 10.
Costs: half-spread by size (large 3-5bp, mid 8-15bp, small 25-60bp, illustrative) + impact k*sigma*sqrt(Q/ADV); shorting fee 0.3-1% general collateral, more for hard-to-borrow; financing at risk-free + 30-60bp for retail margin-style (assumption; check broker).

Pseudo-code:
```
monthly:
  U = top1000(t)
  beta_i = 0.6*corr_5y*vol_i/vol_m + 0.4*1   # shrinkage
  rank within sector
  L = lowest tercile ; H = highest tercile
  wL = clip(rank-weights, max=2%); wH likewise
  scale: wL /= beta_L ; wH /= beta_H
  hold net_beta ~ 0 ; apply gross cap
  throttle = f(funding_spread_pctile, vix_pctile)
  orders = band-filtered(diff(target*throttle, current))
```

## 9. Backtest plan

- Periods: 1963-2025 US; 1990-2025 developed international as out-of-sample; 2018-2025 untouched final hold-out.
- Walk-forward: choose shrinkage/window parameters on rolling 10-year windows; test following 3 years.
- Multiple testing: count variants; Deflated Sharpe; require t above 3 for new structural claims; SPA test.
- Controls: FF5 + momentum; separately regress against bond returns and a defensive-sector basket; report residual after QMJ.
- Costs: report gross, net with base cost model, net with 2x costs; capacity curve vs AUM.
- Metrics: net Sharpe, max drawdown, worst month, beta to market and to 10Y yield, tracking error, turnover, short-leg cost share, subperiod results (rising vs falling rates; crisis vs rebound months), crash analysis around March 2020 and 2009.

## 10. Risk management and kill-switch rules

- Net beta band for BAB: +/-0.1; gross leverage cap 3x; single-name 2%.
- Long-only: tracking error limit 6% vs cap-weighted benchmark (illustrative).
- Kill-switch: live drawdown above 1.5x backtest max, or realized correlation to the market above 0.4 for BAB for 3 consecutive months (indicates beta estimation failure), or realized cost > 2x model: halt and review.
- Funding: pre-arranged margin buffers of 2x expected 3-sigma month loss; no leverage reliant on short-notice financing.
- Rate shock: if 10Y yield rises 100bp in 3 months, review rate-beta of long-only book.
- Abandon the whole idea if falsification criteria in section 7 trigger.

## 11. Annotated sources (A/B/C)

1. Frazzini and Pedersen, Betting Against Beta (JFE 2014), publisher's version: https://research-api.cbs.dk/ws/portalfiles/portal/60082899/lasse_heje_pedersen_et_al_betting_against_beta_publishersversion.pdf ; draft https://www.johnhcochrane.com/s/BettingAgainstBeta.pdf ; Quantpedia: https://quantpedia.com/strategies/betting-against-beta-factor-in-stocks - A (publisher's version READ IN FULL in second pass; authors at AQR).
1b. AQR BAB data set: https://www.aqr.com/Insights/Datasets/Betting-Against-Beta-Equity-Factors-Monthly (xlsx dated 31 Jul 2026, retrieved 2026-10-07; recomputed) and Ken French library (https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/, CRSP 202608 build, retrieved 2026-10-07) - A/B.
2. Novy-Marx and Velikov: https://mysimon.rochester.edu/novy-marx/research/BABAB.pdf (Nov 2018 draft READ IN FULL in second pass); summary https://alphaarchitect.com/betting-against-beta-bab-construction/ - A (draft; published JFE 2022 version not read).
3. Baker, Bradley, Wurgler (FAJ 2011): https://papers.ssrn.com/abstract=1745108 ; https://alphaarchitect.com/2015/03/why-the-low-volatility-anomaly-exists - A/B.
4. Ang, Hodrick, Xing, Zhang (J. Finance 2006), NBER w10852: https://www.nber.org/system/files/working_papers/w10852/w10852.pdf - A.
5. Blitz and van Vliet (JPM 2007): https://papers.ssrn.com/abstract=980865 ; revisited https://hedgefundalpha.com/strategies/the-volatility-effect-revisited/ - A/B (Robeco-affiliated).
6. Driessen et al., interest rate exposure: https://research.tilburguniversity.edu/en/publications/does-interest-rate-exposure-explain-the-low-volatility-anomaly/ ; https://quantpedia.com/does-interest-rate-exposure-explain-the-low-volatility-anomaly - A/B.
7. Man Group, low vol: https://www.man.com/insights/low-vol - B (manager commentary).
8. Black, Jensen, Scholes (1972): https://papers.ssrn.com/abstract=908569 ; Black (1972): https://rasmusen.org/special/black/CapitalMarketEquilibrium72.pdf - A.
9. MSCI "A cycle too short for minimum volatility indexes": https://www.msci.com/documents/1296102/16931762/A+cycle+too+short+for+minimum+volatility+indexes.pdf/aef73489-2195-9401-2c1b-fd529ecc82a8 - B (index provider; not read in full).
10. Morningstar on low-vol drawdowns 2020: https://sg.morningstar.com/sg/news/202747/low-volatility-doesn%2339%3bt-mean-no-volatility-(part-1).aspx - B.
11. Frazzini, Kabiller, Pedersen, Buffett's Alpha: https://nber.org/papers/w19681 - A.
12. Top1000funds on low-vol: https://www.top1000funds.com/asset-classes/equities/is-low-volatility-equity-for-real/ - C/B.

## 12. Open questions

- What is the actual net-of-cost alpha of a large-cap, sector-neutral BAB after FF5 + momentum?
- Is the low-vol premium after 2010 smaller because of crowding or because of the long falling-rate sample? No source I read measures crowding directly.
- Does a rate hedge strip the premium?
- Are betas stable enough in regime shifts to hold levered versions through 2020-type events?
- How much of the effect is the profitability/quality tilt (Novy-Marx-Velikov) rather than risk itself?
- Which funding proxy actually predicts BAB drawdowns out-of-sample?

## Second-pass changelog (2026-10-07)

Method: primary PDFs read via pdftotext (full text, not abstract); AQR BAB monthly xlsx (dated 31 Jul 2026) and Ken French data (CRSP 202608 build) both downloaded 2026-10-07 and analysed in Python. AQR rebuilds its history on each update, so recomputed Sharpe ratios differ from the paper's.

CHANGED
- Source-access note rewritten (tables now read).
- Novy-Marx-Velikov cost haircut: "roughly 55-60%" changed to "more than 55%" (paper text); added value-weighted BAB result (56bp/month, t 3.48, Sharpe 0.49 vs 1.08).
- Sharpe "not verified" replaced by paper figures (US stocks 0.78, 1926-Mar 2012; Treasuries 0.81).
- Source 1 and 2 grades/read status updated; source 1b added.

CONFIRMED (full text)
- Beta estimation: one-year daily volatilities, five-year overlapping three-day correlations, shrinkage w = 0.6 toward 1 (Vasicek mean 0.61). Previously "from memory".
- $1.40 long / $0.70 short for US stocks (international $1.40 / $0.89).
- Novy-Marx-Velikov: $1.05 per $1 in bottom-1% market-cap stocks; 48bp/month net, t 3.30; generalized alpha 16bp/month, t 1.20 (Nov 2018 draft).
- BAB return and alpha statistics: US excess return 0.70%/month, t 7.12; Treasury BAB abnormal 0.17%/month, t 6.26.

NEW (own recompute, AQR dataset and Ken French)
- US BAB Sharpe 0.70 (1930-12 to 2012-03), 0.82 (1963-07 to 2012-03), 0.43 (2007-2020), 0.23 (2018-2020), 0.68 (2013 to Jul 2026), 0.15 (2020 to Jul 2026).
- BAB alpha vs FF5 + momentum: 0.30%/month (t 2.84) 1963-2026; RMW loading 0.48, CMA 0.36.

STILL UNVERIFIED
- "Dropping the smallest decile gave similar net returns" (appendix discussion, first pass): not checked.
- Blitz and van Vliet 12% alpha spread; Baker-Bradley-Wurgler 2.6% and 2.1% alphas; Driessen 20-80% rate-exposure range; COVID-2020 drawdowns for USMV/SPLV (33.1%, 36.3%): all still abstract- or secondary-level.
- Published JFE 2022 version of Novy-Marx-Velikov (numbers may differ from the 2018 draft).
- Crowding and post-publication decay of low-vol: no data source used.
