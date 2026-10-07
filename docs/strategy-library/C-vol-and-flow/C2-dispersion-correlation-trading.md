# C2. Dispersion and Correlation Trading: index volatility vs single-stock volatility

Status: research dossier, not investment advice. Section 7 variants are hypotheses I have NOT backtested. Prepared 2026-10-07; second pass 2026-10-07 (see section 13 changelog). Items marked [OWN-DATA] are simple descriptive statistics I recomputed from public data; they are not backtests.

Evidence key: [PR] peer-reviewed journal; [WP] working paper/thesis/preprint; [PRAC] practitioner, vendor or exchange material; [SEC] secondary summary I could not check against the primary text; [OWN] my own arithmetic or opinion.

---

## 1. Summary, horizon, asset class, holding period

Dispersion trading sells index volatility (options, variance swaps) and buys the volatility of the index's constituents, so the position profits when stocks move independently of each other (realised correlation low) and loses when they move together (realised correlation high). It is a short-implied-correlation position expressed in options. Asset class: equity-index and single-stock options and variance swaps (S&P 500, Euro Stoxx 50, S&P 100, Nasdaq-100, regional indices). Typical holding period: 1 to 3 months (swap/option tenor), often rolled; delta-hedging is daily. It is a relative-value trade that is marketed as market-neutral but is structurally short a joint tail: correlation spikes exactly when index volatility spikes. The central question for this dossier: is the historic profit a correlation risk premium that survives realistic costs, or a backtest artefact that dealers harvested and left little of for others?

## 2. Origin and who uses it

- Practitioners: described in the literature as practised by quantitatively sophisticated hedge funds and bank proprietary desks (the Cara Marshall paper "Dispersion Trading: Empirical Evidence from U.S. Options Markets", Queens College working paper 0004, says this in its abstract [WP; abstract only]). Banks sold correlation-short structured products (worst-of options, Everest, Himalaya) and so became natural buyers of correlation, i.e. the other side of a short-correlation dispersion book (Jacquier and Slaoui 2010, arXiv [WP]).
- Academic anchors: Driessen, Maenhout and Vilkov, "The Price of Correlation Risk: Evidence from Equity Options" (Journal of Finance 2009; S&P 100 index plus component options) [PR]; the extended version "Option-Implied Correlations and the Price of Correlation Risk" (working paper dated July 2013, S&P 500 and DJ30) [WP; read]. Carr and Wu (RFS 2009) first showed that the variance premium is large for indices and small for most single stocks [PR; read the 2004 draft]. Buraschi, Trojani and Vedolin, "When Uncertainty Blows in the Orchard" (Journal of Finance 2014): investor disagreement explains the index-vs-single-stock premium gap and the correlation premium [PR; abstract via search]. Faria and Kosowski (Netspar paper 2014) on correlation-swap term structure and hedging [WP; read]. Faria, Kosowski and Wang (Journal of Banking and Finance 2022) on the correlation premium internationally [PR; the July 2021 CEPR discussion-paper version read in full this pass]. Deng's 2008 working paper "Volatility Dispersion Trading" argued institutional changes in late 1999-2000 favour a market-inefficiency interpretation over a risk-based one (SSRN 1156620; summarised via Quantpedia) [WP/SEC]. Gea Carrasco, "Studying the properties of the correlation trades" (King's College London, 2007) [WP; read].
- Exchange infrastructure: Cboe S&P 500 Implied Correlation Index (COR3M family) and the Cboe S&P 500 Dispersion Index (DSPX) [PRAC; methodologies read/searched].

## 3. Economic rationale and who is on the other side

Index variance = weighted sum of constituent variances plus a cross term that depends on average correlation. If the market charges for index protection (as Carr and Wu and Bakshi-Kapadia document), but not equally for single-stock variance, then the gap is a correlation risk premium: investors pay up for index options to hedge the state in which diversification fails (all stocks fall together). Driessen et al. report average implied correlation of 39.5 percent for S&P 500 versus realised 32.5 percent, and 46.0 versus 35.5 for DJ30 (January 1996 to December 2012), and conclude that the index variance premium can be attributed to the price of correlation risk [WP]. Carr and Wu: the S&P and Dow variance premia are very large and the premium on the Nasdaq-100 and most individual stocks small; they link the stock-level premium to its covariance with market variance (variance-beta regression slope about 0.27, t about 2.7, R-squared about 16 percent) [PR/WP].

Why the edge might persist: structural demand for index puts from portfolio insurers; dealer short-correlation books from structured products require hedging (they buy correlation, which compresses dispersion returns when they are active, but they also leave a premium when they are not); limits to arbitrage because the trade is capital intensive and negatively skewed. Alternative explanations: net buying pressure on index options (Bollen-Whaley view, cited in secondary sources) and disagreement (Buraschi et al.). Who is on the other side: structured-product hedgers and index-protection buyers (buy index vol, i.e. long correlation); during stress, forced deleveraging also pushes realised correlation up against you.

Critical point: the 2009 Journal of Finance abstract of Driessen, Maenhout and Vilkov (S&P 100 options) says the correlation-risk trading strategy generates a high alpha and suits a CRRA investor without frictions, and then states that the premium cannot be exploited with realistic trading frictions (abstract opened on RePEc this pass) [PR; abstract only, I did not read the JF body]. The 2013 working paper I read in full is about the implied-realised correlation gap and contains no friction test I could find, so the frictions claim rests on the 2009 paper alone and is S&P 100 specific. That remains the most important sentence for anyone planning to trade this, and the popular dispersion backtests rarely engage with it.

## 4. Canonical rules (implementable)

**Implied correlation (average-correlation approximation).** With index implied vol sigma_I, constituent weights w_i, constituent implied vols sigma_i:
rho_impl = (sigma_I^2 - sum_i w_i^2 sigma_i^2) / (sum_{i != j} w_i w_j sigma_i sigma_j).
Cboe's COR3M is built on this logic, using ATM implied vols and the top 50 SPX components by market cap, with a 3-month tenor [PRAC; white paper read]. Cboe's DSPX is the square root of (weighted-average expected variance of the basket constituents, computed VIX-style at a 30-day horizon, minus VIX squared), floored at zero; the basket holds S&P 500 members with listed options expiring 10 to 120 days out [PRAC; S&P Dow Jones Indices methodology of July 2023 read in full this pass]. The COR3M white paper (Cboe, 2021 copyright) confirms the formula above: SPX ATM implied variance minus the implied variance of an uncorrelated top-50 basket, divided by the sum of pairwise weighted vol products, using delta-0.5 ATM implied vols from Hanweck [PRAC; read in full].

**Long dispersion (the classic trade):**
1. Universe: index (SPX, SX5E) and top N constituents by weight (N = 20 to 50; the thesis I read used 50 on Euro Stoxx 50 and 57 stocks on another sample).
2. Instruments: (a) variance swaps (cleanest), (b) delta-hedged ATM straddles or strangles, (c) listed options when swaps are unavailable.
3. Entry: 1-3 month tenor. Sell index vega; buy constituent vega. Weighting choices: vega-neutral (sum of constituent vega = index vega), variance-weighted, or correlation-weighted (weights proportional to w_i sigma_i), which the Gea Carrasco thesis found gives more pure correlation exposure.
4. Hedging: delta-hedge each leg daily; track net vega and gamma.
5. Exit: at expiry, or earlier when realised-minus-implied correlation convergence has paid.
6. Signal (optional): implied correlation level relative to trailing realised correlation; many practitioners enter when implied correlation is high relative to history.

**Reverse dispersion (long correlation)** is the mirror trade, used as a hedge by dealers and occasionally as a crisis trade.

P&L identity: Jacquier and Slaoui prove the P&L of a variance-swap dispersion trade equals the spread between implied and realised correlation times average component variance, plus a second-order "volga" term, and that the observed gap between dispersion-implied correlation and the correlation-swap strike is explained by that volga term [WP; read]. Practical meaning: the trade is not a clean correlation bet; it is short vol-of-vol.

## 5. Evidence

| Claim | Source | Sample | Costs | Grade |
|---|---|---|---|---|
| Implied correlation exceeds realised: 39.5 vs 32.5 (S&P 500), 46.0 vs 35.5 (DJ30) | Driessen, Maenhout, Vilkov 2013 WP | Jan 1996 - Dec 2012 | Not a tradable P&L | [WP] |
| Trading strategy exploiting priced correlation risk earns high alpha, attractive to a CRRA investor without frictions; not exploitable with realistic frictions | Driessen, Maenhout, Vilkov, JF 2009 (abstract) | S&P 100 options | Frictions are the finding | [PR] |
| Variance premium large for S&P/Dow indices, small for Nasdaq-100 and most stocks | Carr and Wu | Jan 1996 - Feb 2003 | None | [PR/WP] |
| Index-minus-stock premium explained by disagreement; disagreement factor prices option vol and correlation strategies | Buraschi, Trojani, Vedolin JF 2014 | See paper | See paper | [PR, abstract only] |
| Simple disagreement-sorted backtest: about 15.4 percent annualised after costs, 13.9 percent vol, Sharpe 0.82 (1996-2007), Quantpedia says drawdown figure "not stated" | Quantpedia summary of the source paper | 1996-2007 | Quantpedia says "after transaction costs"; assumptions unknown | [SEC], unverified |
| EuroStoxx 50 variance-swap dispersion: positive mean quarterly return, high skew, large losses in 2006 correction; authors note profits lower than historically as markets became more efficient; transaction costs set to zero | Gea Carrasco 2007 | Jan 2005 - Dec 2006 (2 years) | Zero | [WP] |
| Conditional correlation hedging: dispersion-trade returns and level of correlation risk factor are the best conditioning variables; CBOE Implied Correlation Indices do poorly; transaction costs ignored by authors | Faria and Kosowski 2014 | Jan 1996 - Jan 2013; correlation-swap quotes Mar 2000 - 2012 | Ignored | [WP] |
| Correlation risk premium significant and co-moves in Europe and US; 91-day premium (implied minus realised correlation) of 8.6 points for S&P 500, 6.7 for Euro Stoxx 50, 8.9 for FTSE 100; in 2002-2007 the Euro Stoxx 50 premium was insignificant while DAX was about 10.5 points; all significant in 2008-2012; option-return test explicitly ignores transaction costs and delta hedging | Faria, Kosowski, Wang (CEPR DP16389, July 2021 version of the JBF 2022 paper; full text read via archive.org copy) | Jan 2002 - Dec 2012 (CAC40 from May 2003, SMI from 2006) | Ignored | [WP full text; PR published version] |
| Sub-period decay of the S&P 500 implied-minus-realised correlation gap (30-day): 12.5 points in 1996-2001, 3.2 in 2002-2007, 4.5 in 2008-2012; 91-day: 16.2, 7.5, 7.7; DJ30 30-day 22.1, 6.6, 8.4 | Driessen, Maenhout, Vilkov 2013 WP, Table 6 (read in full this pass; the 91-day S&P figures are also quoted in FKW) | 1996-2012 | Not a tradable P&L | [WP] |
| [OWN-DATA] Cboe COR3M (top-50, 3M, cap-weighted) mean level by period: 46.5 (2006-09), 56.4 (2010-14), 37.0 (2015-19), 42.0 (2020-22), 19.2 (2023 to Oct 2026); all-time low 7.2 on 10 Jul 2026, 11.5 on 6 Oct 2026. Cboe DSPX (history from Jun 2014) mean 25.5, latest 35.1 | Cboe public index history (CDN CSVs) | 2006 - Oct 2026 | Index levels, no P&L | [OWN-DATA]; levels not comparable to Driessen's full-component correlations |
| [OWN-DATA] Gap between COR3M and my equal-weighted realised average pairwise correlation of a fixed set of 50 current large caps over the following 63 trading days: mean +1.5 points over Aug 2021 - Jul 2026 (yearly means +7.3, 0.0, +4.7, -1.5, -1.5, +5.7 for 2021 to 2026); negative on 37 percent of days | yfinance prices; Cboe COR3M | Aug 2021 - Jul 2026 | None; descriptive only. Big caveats: today's constituents (look-ahead/survivorship), equal weights vs Cboe's cap weights, no volatility weighting, overlapping windows | [OWN-DATA], low quality |

Critical reading:
- The strongest peer-reviewed message is the existence of the correlation premium, not the profitability of dispersion after costs. The only paper I found that tests frictions directly (Driessen et al.) says the premium vanishes under realistic frictions.
- The positive backtests I found are short samples (two years), cost-free, in-sample (Gea Carrasco), or vendor summaries without cost detail (Quantpedia). I have no published, audited, live track record to cite.
- Sample-period dependence (now quantified): the S&P 500 30-day implied-minus-realised correlation gap was 12.5 points in 1996-2001 but only 3.2 and 4.5 points in 2002-2007 and 2008-2012 (DMV Table 6). The premium is front-loaded; after 2001 it is a few points, which is small next to option bid-ask on 20 to 50 single stocks. Faria et al. find similar sizes in Europe (about 7 to 9 points at 91 days, 2002-2012, insignificant for Euro Stoxx 50 in 2002-07). Nothing I found covers 2013 onward with a published test; my crude [OWN-DATA] comparison against COR3M for 2021-2026 suggests a gap near 1.5 points on average, negative in 2024 and 2025, with the strong caveats listed in the table. Decay since publication is plausible but still not cleanly measured.
- Post-publication decay: not measured in any source I read. Dealers' growing short-correlation hedging demand cuts both ways. Cboe's launch of DSPX (document dated November 2024) indicates demand for a tradable dispersion benchmark but says nothing about returns.
- The Cboe COR3M sentence, resolved: I re-read the white paper (Cboe, 2021 copyright). The text says the implied correlation index is a signal of the relative cheapness or richness of index options versus components, and that a long dispersion trade (sell ATM index straddles, buy ATM component straddles) "would perform profitably under a high correlation regime." The P&L identity (Jacquier-Slaoui, section 4) says a long dispersion position gains when realised correlation comes in below the implied correlation it was sold at, so it loses when realised correlation is high. Verdict: the sentence is not a clean inversion of the maths but it is ambiguous and, read literally as high realised correlation, wrong. It is only correct if "high correlation regime" means entering when implied correlation is high (index options rich). Do not rely on that wording; use the identity. This is an exchange marketing document, not a test of anything.

## 6. Failure regimes and risks, with tail and ruin analysis

- Correlation spike (crash, macro shock, index-level liquidation): index realised vol jumps, single-stock vol rises less than the index, short index variance loses more than long component variance gains. The Gea Carrasco thesis documents large losses during the 2006 correction and notes the loss driver was realised correlation rising above the implied "bet" level. The Montreal Exchange note (M-X) states that correlation rises in sell-offs and falls in calm markets, with S&P/TSX 60 inter-stock correlation falling to about 10 percent before Feb 2018 and rising to about 40 percent in later turmoil [PRAC].
- Short volga: the trade is short vol-of-vol (Jacquier-Slaoui; a Moontower note says the same, though I could not extract the text, [SEC]), so it loses on volatility shocks even if correlation barely changes.
- Idiosyncratic event risk: single-stock gaps (earnings, M&A, fraud) hurt the short-index/long-stock sleeve less than the reverse, but a one-stock event can distort component vol and the correlation measure. Earnings seasons inflate component implied vols (rich to buy).
- Execution/capacity: buying 20-50 stock option legs plus index requires wide bid-ask crossing; this is where Driessen's friction result bites.
- Credit-correlation analogy (not equity, do not conflate): the May 2005 GM/Ford downgrades produced large mark-to-market losses for funds long equity/short mezzanine tranches in credit correlation books (press and ECB commentary; one trade publication estimated 15 to 30 percent losses for some funds, [SEC]). It illustrates that correlation books can lose from idiosyncratic single-name events, not just macro shocks.
- Model risk: average-correlation approximation assumes a single pairwise correlation and ignores skew and dividends.

**Ruin illustration [OWN].** Take a vega-neutral dispersion book scaled to earn a hypothetical 4 percent a year at 2x gross notional. If a stress month pushes realised correlation from 35 to 75 percent while index vol doubles, P&L over the month is dominated by the index-short leg; with index vega notional V and index vol moving 15 points more than the long-constituent offset, a loss of 15 V is plausible (vega-equivalent; magnitude is illustrative only). If V is set to 1 percent of capital per vol point, that is a 15 percent loss, about 4 years of the hypothetical edge. Leverage above 2-3x on this book is a ruin path even though the carry looks smooth.

## 7. MY TWIST (hypotheses, not backtested)

**Twist 1: Tail-capped dispersion (long index wings).**
- Rationale: the dominant loss is a correlation-plus-volatility spike; buying cheap OTM index puts (or VIX calls) caps the short-index leg without paying for ATM index vol.
- Rule: long dispersion as in section 4, plus a long 90-95 percent put strip or VIX call sleeve with premium budget b percent of the dispersion book's expected premium.
- Parameters: b in {10, 20, 30 percent}; put strike {90, 95 percent}; VIX call strike {+10, +15 vol points above spot}.
- Expected effect: shrinks the worst-month tail by an amount close to the hedge payoff; reduces mean P&L by about b; improves ratio of mean to CVaR.
- Falsification: reject if CVaR(5 percent) after hedge does not improve by at least 25 percent while mean falls by less than 40 percent, in at least 4 of 6 market regimes defined by realised correlation terciles.

**Twist 2: Gated entry on implied-minus-realised correlation and dispersion regime.**
- Rationale: the premium is not constant (front-loaded 1996-2001 in Driessen et al.); enter only when implied correlation is well above a forecast of realised correlation and the VIX term structure is in contango.
- Rule: spread_t = rho_impl_t (3M) - forecast_rho_real_t (EWMA of 1-month and 3-month realised average pairwise correlation of top-50 constituents). Enter only if spread_t above its trailing 1-year 70th percentile and VIX3M/VIX > 1.02; otherwise be flat.
- Parameters: percentile {50, 60, 70, 80}; EWMA half-life {10, 21, 63 days}; N constituents {20, 30, 50}.
- Expected effect: fewer, better trades; lower cost drag; possibly fewer active months (turnover down 30-60 percent, unverified).
- Falsification: reject if the gated strategy's net Sharpe is not above the ungated by 0.2, or if gating shifts the entire edge into a single sub-period.

**Twist 3: Sector-ETF dispersion to cut frictions.**
- Rationale: option bid-ask on 20-50 single stocks is the friction killer; using the 11 sector SPDR ETFs vs SPX (short SPX variance, long sector variance) cuts legs to 11-12 but gives only partial correlation exposure.
- Rule: weights by sector index weight; variance-weighted; delta-hedge with futures.
- Parameters: tenor {1M, 2M, 3M}; weighting {vega, variance, correlation-weighted}; sectors {all 11, top 6}.
- Expected effect: much lower costs, but the premium may be mostly absent in sector ETFs (Carr-Wu found small premia outside the index).
- Falsification: reject if the sector-based correlation premium (implied minus realised sector correlation) is not statistically above zero in a 10-year sample at 95 percent, or net P&L after costs is below cash.

## 8. Implementation spec

**Data:** option chains (bid/ask, OI) for SPX and constituents (OptionMetrics for history; OPRA live); dividend and borrow data; daily constituent weights; realised returns (daily and 5-minute); VIX and VIX3M; CBOE COR3M and DSPX as cross-checks; correlation-swap or variance-swap quotes if you have dealer access.

**Signals:** rho_impl, rho_realised forecast, spread, term-structure slope, dispersion of single-stock implied vols (cross-sectional std).

**Sizing:** vega-neutral base; scale so that the 99th percentile one-month stress (realised correlation to 0.8 and index vol +15 points) loses no more than 8-10 percent of NAV; cap gross vega per name at 5 percent of book; limit number of legs by liquidity (options with spread above 8 percent of mid excluded).

**Execution:** work orders as packages (index leg vs stock basket) with limit prices; trade away from earnings dates where possible; use variance swaps through a dealer when size justifies it (spread unverified).

**Stops:** none inside tenor on gamma trades beyond exposure caps; instead structural wings. Daily check on net vega and gamma drift.

**Cost model:** per leg cost = fill factor f x half quoted spread x contracts x multiplier, f in {0.3, 0.5, 1.0}; delta-hedge cost = 0.5-1.0 bp of notional per rebalance for futures-hedged index leg, 1-2 bp for single stocks (my assumption; unverified); borrow and dividend uncertainty; financing on margin.

**Pseudo-code:**
```
each roll date t:
    w = index_weights(t); sig = atm_iv_3m(stocks) ; sig_I = atm_iv_3m(SPX)
    rho_impl = (sig_I**2 - sum(w**2 * sig**2)) / (sum_pairs(w_i*w_j*sig_i*sig_j))
    spread = rho_impl - rho_real_forecast(t)
    if gate(spread, term_slope):
        V = vega_budget(NAV, stress_loss_cap)
        short  SPX straddle/var swap with vega V
        long   stock straddles with vega V * w_i*sig_i / sum(w*sig)   # correlation-weighted
        optional: buy index wing sleeve (twist 1)
    daily: delta-hedge each leg; recompute net vega/gamma; check kill-switch
    at expiry: settle; log realised rho vs implied; costs by leg
```

## 9. Backtest plan

- Build the implied-correlation series first and validate against Cboe COR3M (they differ by constituent set and tenor).
- Start with the cleanest instrument: synthetic variance swaps from option strips on SPX and the top 50 names, 1-3 month tenor; then straddle versions; then ETF-sector version.
- Data: 1996 onward (OptionMetrics) with explicit sub-samples 1996-2001, 2002-2007, 2008-2012, 2013-2019, 2020-present to test decay.
- Walk-forward: choose N, weighting and gate thresholds on expanding windows; final 3 years held out.
- Multiple testing: count every variant (N, weighting, tenor, gate); report deflated Sharpe, SPA/reality-check p-values, stationary block bootstrap with block length of at least one tenor.
- Costs: report at f = 0.3, 0.5, 1.0 and with and without delta-hedge costs; the headline result is the f = 0.5 net figure. Test explicit Driessen-style frictions.
- Metrics: mean, vol, Sharpe, Sortino, skew, kurtosis, CVaR, worst month, max drawdown, correlation with S&P returns and with VIX changes, exposure to short-vol factor (regress on PUT-style short-vol returns from C1 to see whether dispersion is just short vol).
- Pass criteria (pre-set): net Sharpe above 0.4 at f = 0.5, alpha versus C1 short-vol benchmark t-stat above 2, worst month above -10 percent at planned size.

## 10. Risk management and kill-switch rules

1. Stress budget: nightly revaluation under (rho -> 0.8, index vol +15 points, stock vol +8 points); position must lose less than the cap.
2. Hard gross-vega cap and per-name cap; no more than 20 percent of book in any one sector.
3. Drawdown breaker: reduce 50 percent at -6 percent, flat at -12 percent.
4. Regime kill: flat when realised 1-month average pairwise correlation exceeds 0.6 or VIX above its 252-day 90th percentile, until the 21-day correlation falls below 0.5 for 5 days.
5. Earnings: do not carry short single-stock gamma (if the book flips) or long single-stock gamma beyond an earnings-adjusted limit.
6. Counterparty: variance swaps with at least two dealers, CSA with daily margin; no unsecured exposure.
7. Model kill: if realised costs run above 2x modelled for 2 rolls, stop.

## 11. Annotated sources

| # | Source | URL | Type | Grade | Note |
|---|---|---|---|---|---|
| 1 | Driessen, Maenhout, Vilkov, Option-Implied Correlations and the Price of Correlation Risk (2013 WP) | https://www.netspar.nl/wp-content/uploads/061_Driessen.pdf | WP (read) | A- | Main numbers; sample 1996-2012 |
| 2 | Driessen, Maenhout, Vilkov, The Price of Correlation Risk (JF 2009) | https://ideas.repec.org/a/bla/jfinan/v64y2009i3p1377-1406.html | PR (abstract) | A | Frictions conclusion |
| 3 | Carr and Wu, Variance Risk Premia (2004 WP) | https://econwpa.ub.uni-muenchen.de/econ-wp/fin/papers/0409/0409015.pdf | WP (read) | A | Index vs stock premium |
| 4 | Buraschi, Trojani, Vedolin, When Uncertainty Blows in the Orchard (JF 2014) | https://researchonline.lse.ac.uk/id/eprint/37440 | PR (abstract) | A | Disagreement explanation |
| 5 | Faria and Kosowski, The Correlation Risk Premium: Term Structure and Hedging (2014) | https://www.netspar.nl/wp-content/uploads/038_Kosowski.pdf | WP (read) | B+ | Correlation swaps, dispersion returns as conditioning variable |
| 6 | Faria, Kosowski, Wang, The Correlation Risk Premium: International Evidence (JBF 2022) | https://repositorio.ucp.pt/entities/publication/8b10df1b-d15c-4833-98b8-b81da9f3a994/full (abstract); full text read from an archive.org copy of https://repec.cepr.org/repec/cpr/ceprdp/DP16389.pdf (CEPR DP16389, July 2021) | PR (published) / WP (full text read) | A- | Sample 2002-2012; costs ignored; premium 7-9 points at 91d |
| 7 | Jacquier and Slaoui, Variance Dispersion and Correlation Swaps | https://arxiv.org/pdf/1004.0125 | WP (read abstract and intro) | B+ | P&L decomposition, volga |
| 8 | Gea Carrasco, Studying the Properties of the Correlation Trades | https://mpra.ub.uni-muenchen.de/22318/1/MPRA_paper_22318.pdf | WP/thesis (read parts) | B- | Short sample, zero costs |
| 9 | Cboe Implied Correlation Index white paper | https://cdn.cboe.com/resources/indices/documents/Implied_Correlation-WhitePaper-v1.0.5.pdf | PRAC (read in full again) | B | Methodology verified; the long-dispersion sentence is ambiguous (see section 5) |
| 10 | Cboe S&P 500 Dispersion Index methodology (S&P DJI, July 2023) | https://cdn.cboe.com/resources/indices/documents/methodology-the-dispersion-index.pdf | PRAC (read) | B+ | Formula and basket rules verified |
| 16 | Cboe index history CSVs (COR3M, DSPX) | https://cdn.cboe.com/api/global/us_indices/daily_prices/COR3M_History.csv ; .../DSPX_History.csv | Index data (downloaded) | B | Used for own-data levels |
| 17 | Cboe DSPX product page | https://www.cboe.com/us/indices/dispersion/ | Exchange (read) | B- | 30-day expected dispersion; uses VIX and VIXEQ |
| 11 | Quantpedia, Dispersion Trading | https://quantpedia.com/strategies/dispersion-trading/ | Aggregator (read) | C | Backtest figures unverified |
| 12 | Montreal Exchange, Index options and correlation trading | https://m-x.ca/f_publications_en/index_options_correlation_en.pdf | PRAC (read) | C+ | Intuition, stylised facts |
| 13 | Marshall, Dispersion Trading: Empirical Evidence from U.S. Options Markets (WP) | https://ideas.repec.org/p/quc/wpaper/0004.html | WP (abstract) | C | |
| 14 | Moontower note on correlation swaps | https://notion.moontowermeta.com/correlation-swap-trades-below-implied-corr | Practitioner blog | C | Page text not extracted; claims via search summary |
| 15 | ECB FSR box on May 2005 credit correlation shock | https://ECB.eu/pub/financial-stability/fsr/focus/2005/pdf/ecb~6b24c206ff.fsrbox200512_09.pdf | Central bank | B (credit, not equity) | Analogy only |

## 12. Open questions

1. What is the net-of-cost return of a real, implementable SPX/top-50 dispersion book from 2010 to now? I found no source answering this with realistic costs.
2. How much of dispersion P&L is simply the short-volatility factor of C1 in disguise (Jacquier-Slaoui volga term suggests a large share)?
3. Did the premium decline after structured-product dealers shifted their correlation books, and after 2012?
4. Sector-ETF or factor-based dispersion: does any correlation premium survive outside constituent options?
5. Does DSPX/COR3M carry predictive information for dispersion P&L, or is it contemporaneous only (Faria-Kosowski found the Cboe indices performed poorly as hedge conditioners)?
6. I could not read the bank research notes (JPMorgan, Goldman, SocGen style dispersion reports); my search did not surface any accessible one. That is a source gap that persists after the second pass (no bank note, no audited or costed live track record found).
7. Why is COR3M at record lows in 2026 (7.2 in July, 11.5 now) while DSPX (35.1) is above its 2014-2026 mean (25.5)? Likely mega-cap concentration in the top-50 basket plus high single-stock dispersion, but I did not test it. A rich-dispersion signal does not by itself say the trade pays after costs.
8. Does a proper cap-weighted, point-in-time constituent calculation of realised minus implied correlation reproduce the small gap (about 1.5 points) my crude check found for 2021-2026?

## 13. Second-pass changelog (2026-10-07)

- Read Driessen-Maenhout-Vilkov 2013 WP (Table 6 sub-periods) and extracted the decay: S&P 500 30-day gap 12.5, 3.2, 4.5 points for 1996-2001, 2002-2007, 2008-2012. Replaced the "unquantified decay" statement with the numbers; confirmed against Faria et al.'s quotation of the 91-day figures.
- Read Faria-Kosowski-Wang (CEPR July 2021 version) in full: sample 2002-2012, premium 7-9 points at 91 days, costs ignored, Euro Stoxx 50 premium insignificant in 2002-07. Source grade A- kept; evidence is old (ends 2012).
- Re-read the Cboe COR3M white paper and resolved the inverted-sentence issue: the sentence is ambiguous rather than cleanly inverted; correct only if it means implied correlation is high at entry; read literally as high realised correlation it is wrong. Documented and flagged do-not-rely.
- Verified the DSPX formula and basket rules from the S&P DJI methodology (July 2023); upgraded that source from B (search summary) to B+ (read).
- Verified that the "cannot be exploited with realistic trading frictions" sentence is in the 2009 JF abstract (opened RePEc); noted it is S&P 100, abstract-only, and the 2013 WP has no friction test. Not upgraded: positive backtests (Gea Carrasco, Quantpedia) remain short, cost-free or unverified.
- Added [OWN-DATA] COR3M/DSPX level history and a crude realised-correlation comparison for 2021-2026 (mean gap +1.5 points; negative in 2024-25); heavy caveats stated. Not used to change any grade.
- Overall: evidence for the existence of a correlation risk premium is confirmed; evidence for a net-of-cost tradable edge is not improved and the premium size after 2001 (3 to 8 points) is the strongest reason for caution. Confidence in the strategy as a retail-implementable edge: lowered one notch. Twists remain UNTESTED hypotheses.
