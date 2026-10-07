# E1. Value plus Quality (Magic Formula, Piotroski F-score, QMJ, HML, Gross Profitability)

Status: research dossier, not investment advice. Twists in section 7 are untested hypotheses. Dated 2026-10-07.

Source-access note (updated by second pass, 2026-10-07): the first pass relied on abstracts and secondary summaries. The second pass read in full: Piotroski (Chicago Booth Selected Paper 84, Jan 2002 working-paper version of the JAR 2000 paper), Asness-Frazzini-Pedersen QMJ (RAS 2019 published version), and Novy-Marx and Velikov "Taxonomy" (Aug 2015 author draft, not the RFS 2016 version). It also recomputed HML and market numbers from the Ken French data library (file built from the 202608 CRSP database, downloaded 2026-10-07) and QMJ from the AQR dataset (dated 31 Jul 2026, downloaded 2026-10-07). Greenblatt's book was NOT read; Greenblatt figures remain secondary-only. Anything still not seen in a primary source is marked "unverified". Changes are itemized in the "Second-pass changelog" at the end.

## 1. Summary, horizon, asset class, holding period

Long-only or long-short equity portfolios that buy cheap stocks (low price relative to book, earnings, or cash flow) and screen or tilt toward financially strong, profitable firms, to avoid "value traps". Asset class: single-name equities, developed markets (US primary). Horizon: multi-year; the premium is slow and arrives in lumps, with multi-year droughts. Typical holding period: 12 months per name (annual or semi-annual rebalance), turnover roughly 50-100% per year depending on the screen (turnover figures are my estimate, unverified). The core claim is that cheapness and quality are separately rewarded and that combining them is better than either alone. The core caveat is that the pure value leg went through the longest and deepest drawdown on record in 2007-2020 and the quality leg is largely a repackaging of exposures that are cheap to buy as ETFs.

## 2. Origin and who uses it

- Graham and Dodd value tradition (cheapness plus balance-sheet safety). Not read in this research; background only.
- Fama and French (1998, Journal of Finance), "Value versus Growth: The International Evidence": for 1975-1995 the global high-minus-low book-to-market spread was 7.68% per year, with value beating growth in 12 of 13 major markets (per abstract, via secondary record). They argued it was compensation for distress risk.
- Piotroski (2000, Journal of Accounting Research): nine binary accounting signals applied inside the high book-to-market universe.
- Greenblatt, "The Little Book That Beats the Market" (2005): rank by earnings yield and return on capital, hold about 20-30 names for a year. Gotham Capital / Gotham Asset Management is the associated practitioner firm (association from memory, unverified here).
- Novy-Marx (NBER w15940, 2010; JFE 108(1), 2013): gross profits-to-assets predicts returns about as well as book-to-market.
- Asness, Frazzini, Pedersen, "Quality Minus Junk" (Review of Accounting Studies 24(1), 2019): quality factor across 24 countries. All three are AQR principals, so this is also product research.
- Frazzini, Kabiller, Pedersen, "Buffett's Alpha" (FAJ 2018): Berkshire's alpha becomes statistically insignificant once Betting-Against-Beta and QMJ are controlled for; estimated average leverage about 1.7x in the published version (1.6x in earlier working papers). Authors are AQR principals.
- Arnott, Harvey, Kalesnik, Linnainmaa (FAJ 2021) and Israel, Laursen, Richardson / Asness (AQR 2020) on the value drawdown.
- Users: AQR, Research Affiliates, Dimensional (value/profitability tilts, from memory), Robeco, many smart-beta ETFs.

## 3. Economic rationale and who is on the other side

Rational-risk story: value firms are distressed or inflexible and do badly in bad states (Fama-French 1998 distress factor). Behavioral story: investors extrapolate recent growth and overpay for glamour, underreact to mean reversion (Lakonishok, Shleifer, Vishny 1994 are cited as the proponents in the Fama-French abstract summary). Quality add-on: Novy-Marx argues profitable firms are less distress-prone, with longer cash-flow duration and lower operating leverage, yet earn higher returns, which is hard to square with a pure risk story; this makes quality a cleaner "mispricing or neglected characteristic" case. Asness et al. argue quality stocks are priced only modestly above junk, so risk-adjusted return is high.

Other side of the trade: growth/momentum buyers, retail lottery demand, benchmark-hugging institutions who cannot hold cheap, ugly, small names, and index funds that are price-insensitive. Who pays for the quality edge is less clear; the argument is that investors under-weight "boring" profitability and that analysts anchor on earnings, not on gross profitability.

Critical point: Fama and French (2015, five-factor) report that, in their sample, HML becomes redundant once profitability (RMW) and investment (CMA) factors are included. Hou, Xue, Zhang and others dispute details, and results differ in Chinese data. So "value" and "quality" are not clean independent bets; much of the value premium may be a profitability/investment premium in disguise. This cuts against selling "value plus quality" as two diversifying edges.

## 4. Canonical rules

A. Magic Formula (Greenblatt), as commonly described:
1. Universe: US stocks above a market-cap floor (book suggests $50m; liquidity floor should be much higher in practice), exclude financials and utilities, exclude ADRs.
2. Rank all by earnings yield (EBIT / enterprise value). Rank all by return on capital (EBIT / (net working capital + net fixed assets)).
3. Sum the two ranks; buy the 20-30 lowest-sum names, staging purchases over the year.
4. Hold roughly one year; sell losers shortly before 12 months for tax reasons and winners just after (tax rule is from the book as I recall it; unverified).

B. Piotroski F-score: within the highest book-to-market quintile, score 1 point each for: positive net income; positive ROA; positive operating cash flow; operating cash flow greater than net income; lower long-term debt/assets than last year; higher current ratio; no new share issuance; higher gross margin; higher asset turnover. Buy 8-9 (original paper: long the high scores; short the 0-1 scores in the spread results). Hold 12 months.

C. QMJ (AFP): composite z-score of profitability (gross profit, ROE, ROA, cash-flow-based, margin, low accruals), growth (5-year growth in those measures), safety (low beta, low leverage, low earnings volatility, low bankruptcy risk), and payout (net equity and debt issuance, net payout ratio). Long top-tercile/half and short bottom, size-segmented, rebalanced monthly in the academic version. Exact definitions: verify against the paper.

D. Gross-profitability (Novy-Marx): sort on gross profits (revenue minus COGS) divided by total assets; long high, short low; often combined with book-to-market sorts. Annual rebalance in the original.

E. HML: Fama-French 2x3 sorts on size and book-to-market, long high-B/M and short low-B/M, rebalanced each June.

## 5. Evidence

Peer-reviewed:
- Fama-French (1998) international value spread, 7.68%/yr, 1975-1995 (abstract-level, secondary).
- Piotroski (2000), now read in full (Chicago Booth Selected Paper 84 version; sample 1976-1996, 14,043 high-B/M firm-years, Table 3 one-year market-adjusted buy-and-hold returns): the average high-B/M firm earned +5.9%; high F-score (8-9) firms +13.4%, i.e. +7.5 points over all high-B/M firms (the abstract says "at least 7.5%"; t = 3.14); low F-score (0-1) firms about -9.6%, so the long-short spread is 23.0% (t = 5.59), matching the abstract's 23%. CORRECTION: the "-8.3% a year for low scores" in the first pass is not in the paper; the low-score leg is about -9.6% market-adjusted, roughly -15.5 points versus all high-B/M firms (my derivation from Table 3; the minus signs were lost in text extraction, so the sign is inferred from High-Low = 0.230 and High = 0.134). Only 43.7% of all high-B/M firms had positive market-adjusted returns, so more than half were negative, as claimed. The paper itself says the benefit is concentrated in small and medium firms (high-minus-low mean 27.0% small, 17.3% medium, 15.2% large per the size-partition table as extracted; large-firm median spread only about 2%, column alignment imperfect) and the high-B/M quintile's median market cap was $14.37m, confirming the microcap critique. Returns are not net of transaction costs. Independent cost check: Novy-Marx and Velikov (Aug 2015 draft, value-weighted deciles, NYSE breakpoints, 1963-2012) report the Lyandres-Sun-Zhang-style F-score strategy at 0.20%/month gross (t 1.04), costs 0.11%/month, 0.09%/month net (t 0.45); four-factor net alpha 0.24%/month (t 1.37). So in large-cap-weighted form the F-score is not significant even before costs. Same table: value (B/M) 0.47 gross to 0.42 net per month but net four-factor alpha -0.02 (t -0.17); gross profitability 0.40 gross to 0.37 net, net four-factor alpha 0.51 (t 3.77).
- Novy-Marx (2013): gross profitability has roughly the same power as book-to-market; adding it improves value strategies, especially among large liquid stocks (abstract).
- Asness-Frazzini-Pedersen (2019), now read in full (published RAS version, Table 4): US long sample (7/1957-12/2016) QMJ excess return 0.29%/month (t 3.62), four-factor alpha 0.60%/month (t 9.95), Sharpe 0.47; global broad sample (7/1989-12/2016) excess return 0.38%/month (t 3.33), four-factor alpha 0.61%/month, Sharpe 0.64. Sub-periods (Table 15, US): Sharpe 0.41 (1957-88), 0.62 (1989-2005), 0.41 (2006-2016); the 2006-2016 US excess return is not significant on its own (t 1.35) though alpha is. The QMJ factor loads negatively on HML (-0.37 US) and positively on the profitability/safety legs, so it is not a value proxy. Authors are AQR principals. My recompute on the current AQR dataset (US QMJ, dated 31 Jul 2026, downloaded 2026-10-07): 1957-07 to 2016-12 Sharpe 0.58 and 4.3%/yr (higher than the paper's 0.47 because AQR reconstructs history on each update); full 1957-07 to 2026-07 Sharpe 0.49; 2013-01 to 2026-07 Sharpe 0.29 and 3.0%/yr; 2018-2020 Sharpe -0.17. Regression on Fama-French five factors plus momentum (1963-07 to 2026-07): alpha 0.29%/month (t 5.6) with RMW loading 0.63 and market loading -0.19, so much of QMJ is profitability (RMW) exposure with low beta; alpha stays significant after 2010 (0.33%/month, t 2.75).
- Frazzini-Kabiller-Pedersen (2018): Berkshire Sharpe 0.76 to 0.79 depending on version, alpha insignificant after BAB and QMJ.
- Fama-French (2015): HML redundant in the five-factor model, in their sample.
- Arnott et al. (FAJ 2021): value drawdown was driven by widening valuation spreads, and intangibles-adjusted book value handles it better. Reported HML drawdown figures: about 42% from January 2017 to March 2020 on one measure, about 51% from 2007 on another, and Research Affiliates cites 55% since 2007 as of mid-2020. Windows and constructions differ, so use a range. Second-pass recompute from the Ken French library (monthly Fama-French HML, US, file built from 202608 CRSP data, retrieved 2026-10-07; my own arithmetic): cumulative HML -42.9% from 2017-01 to 2020-03 (matches the ~42%), -50.5% from 2007-01 to 2020-03 (matches ~51%), -55.8% from 2007-01 to 2020-12 (matches ~55%), with maximum peak-to-trough drawdown -57.5% (peak 2007-01, trough 2020-09). Annualized 2007-2020: HML mean -5.3%/yr, vol 10.0%, Sharpe -0.53, while the market excess return was +10.1%/yr (Sharpe 0.62). 2018-2020: HML -17.9%/yr arithmetic (cumulative -43.0%), Sharpe -1.51, versus market excess +14.9%/yr. Calendar HML: 2017 -10.8%, 2018 -10.5%, 2019 -8.1%, 2020 -30.7%, then +22.2% (2021) and +31.7% (2022), -11.1% (2023), -7.0% (2024), +6.6% (2025). Long-run: 1926-07 to 2026-07 HML mean 4.3%/yr, vol 12.3%, Sharpe 0.35; 1963-07 to 2012-03 Sharpe 0.46; 2010-01 to 2026-07 Sharpe -0.03 (mean -0.4%/yr). So value's whole post-2010 record is zero in this construction; 2021-2022 recovered part of the loss but not all. Also confirms Fama-French (2015): regressing HML on MKT, SMB, RMW, CMA gives alpha -0.01%/month (t -0.09) for 1963-07 to 2013-12 and -0.02%/month (t -0.25) through 2026-07, so HML is redundant in the five-factor model in this data.
- Schwartz and Hanauer, "Formula Investing" (1963-2022, via Alpha Architect summary Jan 2025): each of four formulas (including Magic Formula, F-score) earns significant raw and risk-adjusted returns largely via value and quality exposure; Magic Formula showed the highest residual alpha and was strongest after 2000 in concentrated long-only form; F-score and Acquirer's Multiple had positive small-size tilts. Peer-review status unverified.

Practitioner/unverified:
- Greenblatt's book backtest: 30.8% a year (1988-2004) versus 12.4% for the S&P 500, before costs. Second pass: the 30.8%/12.4% pair is repeated by several secondary sources (Motley Fool book review, which also reports annual formula returns ranging from -4.4% to +79.9% against -22.1% to +37.6% for the index; Nasdaq and Validea pieces). I did not find the "33%" figure anywhere in this pass, so that inconsistency is not corroborated. The book itself was not read, and no source says whether the averages are arithmetic or compounded (the Fool review's dollar figures imply compounding). Still secondary-only, so unverified as a primary claim, and in any case a gross, pre-publication backtest.
- Alpha Architect (2011) replication attempt found outperformance but nowhere near the book's ~31% CAGR and suggested the strategy is unstable to small implementation choices (second pass: the page returned HTTP 403 to my fetch, so this still rests on a search-result summary of the post; a July 2011 follow-up reportedly attributes part of the gap to universe choice). Blog, not peer-reviewed. A 2003-2015 independent backtest summarized on Wikipedia (Robert Andrew Martin, 2020) reports 11.4% versus 8.7% for the S&P 500 with a flat spell in 2007-2011; not opened by me.
- Oslo Stock Exchange master's thesis (2003-2022): four-factor alpha about 0.5% per month, significant at 5% before costs and only at 10% after costs. Brazil thesis (2016): outperformed but could not rule out luck. Both low-grade (student theses).
- Seeking Alpha piece claiming the original long-short F-score lost money over the last 10 and 20 years: one author's analysis, unverified.
- AQR is an interested party in QMJ, BAB and Buffett papers.

Post-publication decay and capacity: The value spread itself was hugely negative for over a decade to 2020. Piotroski-type returns are concentrated in small, illiquid stocks (Podgorski review, via search summary), so capacity is low and net returns are sensitive to spreads. I found no clean, independently reproduced post-2010 net-of-cost live track record for the Magic Formula.

My read: the factor evidence is real in aggregate but weaker, lumpier and more cost-sensitive than the marketing, and "value" cannot be separated from quality/investment. Treat Greenblatt's headline number as dead as a forecast.

## 6. Failure regimes and risks

- Long value droughts: growth-led, falling-rate, mega-cap-tech regimes (2007-2020 episode). Mean-reversion in valuation spreads is the only recovery mechanism, and timing is unknowable.
- Value traps and sector concentration (financials, energy, cyclicals dominate low P/B and high earnings yield).
- Accounting measurement: book value misses intangibles; EBIT yield is distorted by cyclical peaks, one-offs, and R&D/SG&A capitalization differences. Arnott et al. argue this explains part of the "value is dead" debate.
- Small-cap illiquidity: Piotroski-type spreads live in names that cost 1-3%+ round trip to trade (my estimate, unverified).
- Factor crowding and quality drawdowns in junk rallies (e.g., high-short-interest, low-quality rallies; specific episodes not verified here).
- Tax drag and turnover for taxable holders.

## 7. MY TWIST (hypotheses, NOT backtested)

Twist 1: Intangibles-adjusted value x gross profitability, large-cap only.
- Rationale: Arnott et al. say capitalizing intangibles repaired value; Novy-Marx says profitability helps most in liquid large stocks. Combining targets the part of the edge least eaten by costs.
- Rules: universe = top 1,000 US by market cap; value = (book equity + capitalized R&D at 5-year straight-line + 30% of SG&A capitalized over 3 years) / market cap; quality = gross profit / assets; composite = average of cross-sectional ranks within sector; hold top quintile equal-weight with 3% single-name cap; rebalance semi-annually with a no-trade band (hold names until rank falls below 40th percentile).
- Parameters to test: SG&A capitalization share 0/30/50%; R&D life 3/5/7 yrs; weight on quality 25/50/75%; band 30/40/50th percentile.
- Expected effect: lower turnover than Magic Formula, smaller growth-factor drag than raw B/M, lower tracking-error spikes. Magnitude: none claimed.
- Falsification: if net of 20bp/side costs the strategy's annualized excess return over the cap-weighted universe is below 1% in out-of-sample years 2012-2025 or its five-factor (including RMW, CMA) alpha t-stat is under 2 after the multiple-testing haircut in section 9, drop it.

Twist 2: Valuation-spread timing as a sizing overlay, not a switch.
- Rationale: Arnott et al. say the drawdown was explained by the widening of the growth-value valuation gap; spread is observable. Gradual sizing avoids binary timing mistakes.
- Rules: compute the value-minus-growth spread in B/M (or intangibles-adjusted) percentile versus its own 20-year history; gross exposure to the factor sleeve scales 0.75x to 1.25x linearly across the 20th-80th percentile of spread; no more than 25% change per quarter.
- Parameters: history window 15/20/30 yrs; scale range; smoothing.
- Expected effect: modestly larger sleeve in cheap-spread regimes; may add no value. Valuation-based timing historically has low power over short horizons (my caution, unverified).
- Falsification: if overlay sleeve Sharpe minus unscaled sleeve Sharpe is not positive in at least 3 of 4 non-overlapping 5-year blocks, or the difference has a bootstrap p-value above 0.10, discard.

Twist 3: Quality as a filter on a distress screen (F-score-lite with market-cap floor).
- Rationale: keep Piotroski's accrual and issuance signals (which are cheap and defensible) while removing the microcap capacity illusion.
- Rules: universe above the 30th NYSE size percentile; B/M in top 40%; require F-score >= 7 and no net equity issuance greater than 3%; max 40 names; equal weight; rebalance annually.
- Parameters: F threshold 6/7/8; size cutoff; B/M cutoff.
- Expected effect: smaller headline return than the paper but investable; test whether the signal survives a size floor.
- Falsification: if the signal's information coefficient or top-minus-bottom spread is statistically indistinguishable from zero above the size floor in 2005-2025, conclude the published effect is a microcap artifact.

## 8. Implementation spec

Data: point-in-time fundamentals (Compustat PIT, Sharadar, or Norgate/FactSet equivalents), lag annual data 4 months and quarterly 2 months to avoid look-ahead; delisting returns; GICS sector; daily prices and volume; borrow cost data if shorting.
Signals: as in section 4 or Twist 1.
Sizing: equal weight capped 3-5% per name, or inverse-volatility; sector deviation from universe within +/-5%.
Execution: staged purchases over 5-10 trading days; limit orders; avoid quarter-end days; maximum 10% of 20-day ADV per name per day.
Stops: none at name level (value is mean-reversion; stops fight the thesis); portfolio-level drawdown rule in section 10.
Cost model: half-spread by size bucket (illustrative, calibrate to real data: large-cap 3-5bp, mid 8-15bp, small 25-60bp) plus impact = k * sigma * sqrt(trade/ADV), k about 0.5-1 (my starting assumption, unverified); commissions near zero; add 0.3-0.5%/yr for tax/withholding on international.

Pseudo-code:
```
each rebalance date t:
  U = universe(t) filtered by mcap>floor, adv>floor, exclude fin/util if MF
  X = point_in_time_fundamentals(U, lag)
  v = zscore_within_sector(adj_book_to_price(X))
  q = zscore_within_sector(gross_profit_over_assets(X))
  s = w_v*v + w_q*q
  target = top_quintile(s) with hysteresis vs current holdings
  w = cap(equal_weight(target), 0.03)
  orders = diff(w, current) ; skip if |dw|<0.25*w
  execute with participation cap; record costs
```

## 9. Backtest plan

- Period: 1990-2025 (US) with 1963-1989 as a held-out earlier period; international developed as second out-of-sample.
- Design lock: freeze definitions and parameter grid before running; log every variant tried (count N for multiple testing).
- Walk-forward: choose parameters on rolling 10-year windows, evaluate next 3 years; also a pure hold-out 2018-2025 never touched during design.
- Multiple testing: report Deflated Sharpe Ratio and a Harvey-Liu-Zhu style hurdle (t-stat above about 3 as a rule of thumb); White's reality check or Hansen SPA across variants.
- Controls: regress on Fama-French 5 + momentum + QMJ + BAB; require alpha after factors, and report the loading breakdown (the honest question is whether you are just buying RMW/CMA).
- Metrics: net CAGR, vol, Sharpe, Sortino, max drawdown and duration, worst rolling 3-year excess return, turnover, capacity (AUM at which impact costs halve alpha), hit rate by calendar year, tracking error, information ratio, subperiod stability (decade splits), performance in 2007-2020 specifically.
- Robustness: size floors, sector neutral versus not, delisting-return handling, announcement-lag shifts.

## 10. Risk management and kill-switch rules

- Position cap 3-5%; sector cap relative to benchmark +/-5%; beta band 0.8-1.2.
- Strategy-level: if rolling 36-month net excess return vs benchmark is below -8% annualized AND the realized tracking error exceeds 1.5x its backtest median, cut factor sleeve to half and review (thresholds are illustrative; calibrate to backtest).
- Hard stop: live drawdown beyond 1.5x the worst historical backtest drawdown triggers a full halt and review.
- Pre-commitment: a value strategy must be judged over at least 5-7 years; do not abandon on 2-3 year underperformance alone, but do abandon on falsification criteria in section 7.
- Cost slippage check: if realized costs exceed 2x model for two consecutive rebalances, reduce size.
- Data-integrity kill: any point-in-time violation discovered voids the backtest.

## 11. Annotated sources (grade: A peer-reviewed/primary, B credible practitioner, C weak/promotional/secondary only)

1. Asness, Frazzini, Pedersen, Quality Minus Junk (RAS 2019): https://research-api.cbs.dk/ws/portalfiles/portal/60211462/lasse_heje_pedersen_et_al_quality_minus_junk_publishersversion.pdf (published version; READ IN FULL in second pass via pdftotext) - A, authors AQR-affiliated.
2. AQR working paper PDF (unparseable): https://www.aqr.com/-/media/AQR/Documents/Insights/Working-Papers/Quality-Minus-Junk.pdf - A, not read (superseded by item 1). AQR data set: https://www.aqr.com/Insights/Datasets/Quality-Minus-Junk-Factors-Monthly (xlsx dated 31 Jul 2026, downloaded 2026-10-07; recomputed) - A/B, AQR-maintained, history is reconstructed on each update.
2b. Ken French Data Library, Fama/French 3 factors, 5 factors (2x3) and momentum, monthly CSV from mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/ (CRSP 202608 build, retrieved 2026-10-07; recomputed) - A.
2c. Novy-Marx and Velikov, A Taxonomy of Anomalies and Their Trading Costs (RFS 2016; Aug 2015 author draft read): https://mysimon.rochester.edu/novy-marx/research/ToAatTC.pdf - A (draft, not the published version).
2d. Piotroski, Value Investing: The Use of Historical Financial Statement Information (JAR 2000; Chicago Booth Selected Paper 84, Jan 2002 version READ IN FULL): https://www.chicagobooth.edu/~/media/FE874EE65F624AAEBD0166B1974FD74D.pdf - A. Note: a "test2.ivey.uwo.ca" copy returned HTML, not the paper.
2e. Motley Fool book review of Greenblatt (opened): https://www.fool.com/investing/general/2007/03/23/foolish-book-review-the-little-book-that-beats-the.aspx - C (secondary for the 30.8%/12.4% figures).
3. Novy-Marx, The Other Side of Value, NBER w15940: https://nber.org/papers/w15940 and https://www.nber.org/system/files/working_papers/w15940/w15940.pdf - A (abstract-level read via search).
4. Piotroski F-score summaries: https://blog.validea.com/joseph-piotroski-separating-winners-from-losers-in-value-investing/ , https://www.cxoadvisory.com/fundamental-valuation/piotroskis-efficient-value-investing , https://www.chicagobooth.edu/review/separating-winners-losers - B/C (secondary; their "-8.3% for low scores" is not supported by the paper, see item 2d).
5. Fama-French 1998 international value record: https://econpapers.repec.org/RePEc:wop:chispw:341 - A (abstract).
6. Fama-French 2015 five-factor discussion (secondary): https://www.etf.com/sections/index-investor-corner/swedroe-improving-fama-french - C/B.
7. Arnott et al., Reports of Value's Death May Be Greatly Exaggerated (FAJ 2021): https://www.researchaffiliates.com/insights/journal-papers/reports-of-values-death-may-be-greatly-exaggerated and https://ideas.repec.org/a/taf/ufajxx/v77y2021i1p44-67.html - A/B (Research Affiliates is interested party).
8. Alpha Architect, interest rates and value: https://alphaarchitect.com/do-interest-rates-explain-values-underperformance/ - B.
9. Frazzini, Kabiller, Pedersen, Buffett's Alpha: https://nber.org/papers/w19681 and https://papers.ssrn.com/abstract=3197185 - A, authors AQR.
10. Schwartz and Hanauer Formula Investing via Alpha Architect: https://alphaarchitect.com/formulaic-investing/ and https://quantpedia.com/out-of-sample-test-of-formula-investing-strategies/ - B (primary paper status unverified).
11. Alpha Architect 2011 Magic Formula replication: https://alphaarchitect.com/909/ - B.
12. NHH Oslo thesis: https://openaccess.nhh.no/nhh-xmlui/handle/11250/3052180 ; Brazil thesis: https://gupea.ub.gu.se/handle/2077/48253 - C (student work).
13. Seeking Alpha F-score decay: https://seekingalpha.com/article/4407684-why-piotroskis-f-score-no-longer-works - C. Investing Daily critique: https://investingdaily.com/16238/value-investing-and-value-traps-separating-winners-from-losers - C.
14. Invesco value note: https://invesco.com/content/dam/invesco/emea/en/pdf/IQS%20HarvestingValuePremia%202020_11%20EMEA.pdf - B (asset manager marketing flavor).

## 12. Open questions

- How much of Magic Formula alpha survives after controlling for RMW, CMA and size at investable market-cap floors?
- Is the 2007-2020 drawdown a structural change (intangibles, rates, competition) or a spread-widening that mean-reverts? Arnott et al. and AQR disagree on mechanism but agree it is not terminal; neither is a forecast.
- What are the true net-of-cost, point-in-time results for F-score above a $500m floor?
- Do QMJ results survive independent replication outside AQR (the published literature includes disputes I have not read)?
- Capacity: at what AUM does a 30-name value/quality book lose half its edge?
- Is combining value and quality diversifying, or are they one latent factor measured twice?

## Second-pass changelog (2026-10-07)

Method: primary PDFs read via pdftotext; data recomputed in Python 3 (pandas/numpy, scripts kept outside the download directories). Datasets: Ken French library (CRSP 202608 build, retrieved 2026-10-07) and AQR QMJ monthly xlsx (dated 31 Jul 2026, retrieved 2026-10-07). Full text vs abstract is stated per item.

CHANGED
- Piotroski low-score leg: first pass "-8.3%/yr" is not in the paper; Table 3 gives about -9.6% market-adjusted (about -15.5 points vs all high-B/M firms; sign inferred, see section 5). Grade of the Piotroski evidence upgraded from C (secondary) to A (primary, full text).
- Piotroski sample detail added: 14,043 firm-years, median market cap of the high-B/M quintile $14.37m (critic's "under $15m" is correct).
- QMJ: "Sharpe not verified" replaced by paper figures (US 0.47, global 0.64; four-factor alphas 0.60 and 0.61 per month).
- Greenblatt "33% elsewhere" inconsistency: not corroborated; only 30.8% vs 12.4% found.
- Source-access note rewritten; sources 1, 2 re-graded; sources 2b-2e added.

CONFIRMED
- Piotroski: high F-score beats all high-B/M by 7.5 points (paper: "at least 7.5%", t 3.14), long-short 23% a year 1976-1996 (t 5.59). Full text.
- Piotroski F-score rule (nine signals, high = 8-9, low = 0-1). Full text.
- Piotroski effect concentrated in small and medium firms. Full text.
- HML drawdown range: -42.9% (2017-01 to 2020-03), -50.5% (2007-01 to 2020-03), -55.8% (2007-01 to 2020-12), max drawdown -57.5%. Recomputed from Ken French data, replacing the "42% / 51% / 55%" secondary figures.
- Fama-French (2015) HML redundancy: confirmed in the current data (alpha about zero, t -0.09 to -0.25).
- Novy-Marx and Velikov net-cost picture for value, profitability and F-score (new, Aug 2015 draft).

STILL UNVERIFIED
- Greenblatt 30.8% vs 12.4% (1988-2004): secondary only; book not read; arithmetic vs compound unknown.
- Alpha Architect 2011 replication numbers (page blocked, summary only).
- Oslo and Brazil thesis results, Seeking Alpha F-score decay claim, Schwartz-Hanauer peer-review status, Fama-French 1998 7.68% (abstract-level only), Magic Formula tax-timing rule, all turnover and cost-bucket assumptions marked "my estimate".
- Whether the Novy-Marx-Velikov figures in this section survive in the published RFS 2016 version (I read the 2015 draft).
