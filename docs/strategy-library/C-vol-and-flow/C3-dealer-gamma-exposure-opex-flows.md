# C3. Dealer Gamma Exposure (GEX), vanna/charm and opex flows, 0DTE impact

Status: research dossier, not investment advice. Section 7 variants are hypotheses I have NOT backtested. Prepared 2026-10-07; second pass 2026-10-07 (see section 13 changelog). Items marked [OWN-DATA] are descriptive statistics I recomputed from public data; they are not backtests of a trading rule.

Evidence key: [PR] peer-reviewed journal; [WP] working paper; [PRAC] practitioner/vendor/exchange material; [SEC] secondary summary not checked against primary; [OWN] my own reasoning.

Headline verdict up front: the mechanism (hedgers who are short gamma amplify moves, long gamma dampen them) is theoretically sound and has genuine but modest peer-reviewed support in specific forms (intraday momentum into the close, pinning of single stocks at expiry). The popular retail-facing claim that a public GEX number computed from open interest tells you the sign of dealer positioning and reliably forecasts index direction or volatility is mostly vendor assertion, rests on an untested assumption about who is long and short, and is contradicted or heavily qualified by the most careful 0DTE research. I found no Federal Reserve paper that tests GEX directly (details in section 5). Second-pass update: the best direct evidence on dealer positions (Cboe trade data, July 2020 to June 2023, Vasquez et al., now read in full) says SPX market-maker gamma is typically positive and the largest volatility effect attributable to negative gamma is a few volatility points; and a descriptive check of SqueezeMetrics' own public GEX series (2011-2026) shows low-GEX days do precede larger next-day moves, with modest incremental explanatory power beyond VIX and lagged absolute returns. Both are consistent with "real but small and state-dependent", not with "tradable edge".

---

## 1. Summary, horizon, asset class, holding period

Dealer-gamma strategies infer the net gamma that option market makers hold from public open interest, then trade (or size risk) on the idea that hedging flows are stabilising when dealers are net long gamma and destabilising when net short. Variants: GEX regime filters (mean-reversion vs momentum depending on the sign), "gamma flip" level as support/resistance, vanna and charm flow timing around monthly expiry (opex), pinning to large strikes, and 0DTE-related intraday trades. Asset class: index/ETF/single-stock equity derivatives (SPX, SPY, QQQ, single names); also VIX. Holding period: intraday to a few days, clustered around the third Friday and the end of the day.

## 2. Origin and who uses it

- Academic roots: stock price clustering at strikes on expiry days (Ni, Pearson, Poteshman, JFE 2005) [PR]; the "pervasive impact" test of hedge rebalancing on volatility (Pearson, Poteshman, White 2006 draft, published as Ni, Pearson, Poteshman and White, RFS 2021) [PR/WP]; dynamic-hedging feedback theory (Frey and Stremme 1997; Avellaneda and Lipkin 2003; both cited by SqueezeMetrics) [PR, not read by me].
- Vendor origin: SqueezeMetrics (Prior Analytics LLC) "Gamma Exposure (GEX)", first dated March 2016, revised December 2017 [PRAC; read]. Followers and competitors: SpotGamma and others [PRAC vendors]. Sell-side and exchange commentary (Cboe 2023) [PRAC].
- Academic partial endorsement: Baltussen, Da, Lammers and Martens (JFE 2021), who thank SqueezeMetrics for data, link market intraday momentum to gamma hedging by option market makers and leveraged ETFs [PR; read].
- Users: systematic discretionary day traders, vol funds that condition on regime, market makers themselves (who know their own books), and risk teams. I could not verify any named hedge-fund track records.

## 3. Economic rationale and who is on the other side

Mechanism: a market maker who sells a put is short delta-hedging shares; as the price falls the put delta rises, so the maker must sell more stock (short gamma = trade with the move); a maker long options does the opposite (long gamma = trade against the move). Aggregate stabilisation or amplification depends on the aggregate sign and size of dealer gamma relative to market liquidity.

SqueezeMetrics' construction (as stated in the white paper I read) rests on four assumptions: every traded option is facilitated by a delta-hedger; investors sell calls and market makers buy them (call overwriting dominates); investors buy puts and market makers sell them (protective puts); and market makers hedge exactly to option delta. GEX per strike = gamma x open interest x 100 for calls and the negative for puts; summed across strikes. Positive GEX means volatility-suppressing hedging; negative means amplifying. The paper claims SPX one-day return standard deviations after the highest and second-highest GEX quartiles of 0.55 percent and 0.85 percent, and that VIX has weaker distinguishability at low levels (one-day SD 0.51 versus 0.66 percent in the lowest two VIX quartiles); it also says an unspecified screening of S&P 500 stocks with GEX near zero "yielded excess returns" [PRAC; unverified, no sample period or costs given in the document text].

Who is on the other side: in the vendor story, call overwriters and put buyers are the clients and dealers are the hedgers; for a trader acting on GEX signals, the counterparty is anyone selling when dealers are expected to buy, which is a weak identification of edge. If a flow is predictable and known, informed participants including the dealers themselves pre-empt it.

Critical weakness: the sign assumption. Evidence from datasets that actually observe positions is mixed by product and era. Garleanu, Pedersen and Poteshman (NBER WP 11843, full text read; data 1996-2001) find end users net long S&P 500 index options, especially out-of-the-money puts, so dealers were short index options, while end users were net short single-stock options, so dealers were long them; the sign therefore differs between index and stock options and the "customers buy puts, dealers sell them" template is an index-specific, early-sample fact [WP; later published RFS 2009]. For 2020-2023, Vasquez, Amaya, Pearson and Garcia-Ares (full text read, Cboe SPX/SPXW trade data with customer/market-maker flags, July 2020 to June 2023) find the market-maker aggregate gamma is typically positive, with a standard deviation of the daily mean almost as large as the mean, negative at some point on at least a quarter of days and negative all day on about 1 percent of days [WP]. Cboe's own SPX 0DTE study reports that market makers' net position on a heavy-volume put strike was only about 3 percent of gross volume, and its May 2025 note says net market-maker gamma hedging is at most about 0.2 percent of SPX daily liquidity, retail is roughly 50 to 60 percent of 0DTE volume and over 95 percent of 0DTE trades are limited-risk [PRAC; Cboe has a vested interest]. So a fixed "dealers are short puts, long calls" sign is the weak link, and the true sign in SPX has mostly been long gamma with episodic negative spells. Dim, Eraker and Vilkov note that one cannot identify the effect of open-interest gamma on volatility without knowing the aggregate gamma of delta-hedgers (citing Ni et al. 2021), and that in recent years investors have increasingly sold volatility for yield, which would leave hedgers net long gamma and therefore stabilising [WP]. Vendors that infer direction from trade data admit that every public GEX figure depends on modelling assumptions.

## 4. Canonical rules (implementable)

1. Compute per-contract dollar gamma = Gamma(S, K, T, sigma) x OI x multiplier(100) x S^2 x 0.01 (the vendor-style dollar normalisation: gamma exposure per 1 percent move) with sign +1 calls, -1 puts under the SqueezeMetrics convention. Sum over strikes and expiries to get total GEX; also by strike for "walls".
2. Regime: GEX > 0 means expect lower realised volatility, mean reversion and pinning; GEX < 0 means expect higher realised volatility, momentum, wider ranges.
3. Gamma flip: the underlying price level where cumulative GEX crosses zero; above is stabilising, below is destabilising (vendor heuristic).
4. Trade expressions (all vendor/practitioner folklore, not tested by peers): (a) when GEX is high and positive, sell short-dated premium or fade intraday extremes; (b) when GEX is negative, avoid mean-reversion, trade with the intraday trend, buy convexity; (c) around monthly opex, expect pinning to heavy strikes and "vanna/charm tailwind" after expiry as charm decay and vol decline remove put hedges (mechanism only: vanna = delta sensitivity to implied vol, charm = delta sensitivity to time; magnitudes require dealer-side positions that are not observed).
5. Intraday momentum rule (this one has peer-reviewed support): go with the sign of the return from the previous close to 30 minutes before the close, enter at that time, exit at the close (Baltussen et al.).

## 5. Evidence

Peer-reviewed / working-paper evidence:

| Claim | Source | Sample | Notes | Grade |
|---|---|---|---|---|
| Rest-of-day return positively predicts the last 30 minutes' return in 60+ futures; reverts over following days; stronger when a proxy for option-market-maker negative gamma exposure is more negative; no momentum when makers are net long gamma; leveraged ETF rebalancing contributes | Baltussen, Da, Lammers, Martens JFE 2021 | 1974-2020 (S&P net gamma proxy from OptionMetrics data, 1996-May 2020) | A simple strategy reports Sharpe ratios of 0.87 to 1.73 at the asset-class level. The paper states explicitly that it does not consider transaction costs and only remarks that exploiting the S&P 500 futures effect yields a positive net Sharpe at a one-tick cost (no number given); it also notes the effect was especially strong in the last four months of the sample (February to May 2020). Sign of dealer gamma is itself a proxy (re-read this pass). | [PR] |
| Closing prices of optionable stocks cluster at strikes on expiry; average return alteration at least 16.5 bp per expiry; ascribed to dealer hedge rebalancing and to manipulation by firm proprietary traders | Ni, Pearson, Poteshman JFE 2005 | See paper | Abstract level; stock-level, not index-level. | [PR] |
| Negative relation between stock volatility and net purchased option positions of likely hedgers (i.e. when hedgers are short gamma, volatility is higher) | Pearson, Poteshman, White (2006 draft); Ni, Pearson, Poteshman, White RFS 2021 | US stocks | Supports mechanism for stocks with proprietary positioning data. The draft marks itself preliminary. | [WP/PR] |
| 0DTE open-interest gamma does not propagate past volatility; for options with more than one day to expiry, open-interest gamma is associated with lower realised intraday volatility; average daily OI gamma did not grow after 2016; 0DTE volume shocks do not amplify recent index returns; 0DTE vs underlying volume correlation rose from about 0.25-0.30 before 2021 to 0.59 in 2023; the incremental volatility response to 0DTE shocks is about 0.15 SD | Dim, Eraker, Vilkov (May 2024 WP) | SPX/SPY, 2012 to mid-2023 | Careful, includes caveats about dealer sign; cites that makers rebalance 0DTE positions directly rather than via the underlying. | [WP] |
| Presence of 0DTE dampens volatility via a shift in market makers' hedging needs; effect comes from positions accumulated earlier in longer-dated options that become 0DTE; intraday variation in hedging needs predicts stronger order-flow reversals, lower momentum returns and lower volatility | Adams, Dim, Eraker, Fontaine, Ornthanalai, Vilkov (SSRN 5641974; posted 23 Oct 2025, written 17 Oct 2025) | SPX; identification uses the 2022 staggered introduction of Tuesday/Thursday SPXW expiries (as described by Vasquez et al.) | Abstract now read in full (archive.org copy of the SSRN page; direct SSRN returned 403); body not read | [WP, abstract read] |
| 0DTE share of volume correlates with higher S&P 500 ETF volatility; one-SD rise in 0DTE volume raises daily volatility by "almost 14 percent" per Bloomberg coverage (the first-pass figure of 9.1 percent of the mean came from a different summary; the two are unreconciled); Vasquez et al. describe the paper as showing a correlation, and Brogaard has described himself as leaning to the "amplifies" view | Brogaard, Han, Won | Uses staggered introductions of weekly options as instrument (per first-pass summary) | I could not locate the SSRN abstract; press and secondary only | [WP/SEC] |
| Maximum impact of market-maker gamma on S&P 500 volatility: typical effect is to reduce realised volatility by about 0.2 percentage points; worst-case (negative-gamma) effect is to raise annualised daily realised volatility by 3.3 points and 30-minute volatility by 6.4 points; market-maker gamma typically positive but negative at some point on at least 25 percent of days | Vasquez, Amaya, Pearson, Garcia-Ares (Jan 2025; full text read via the Cboe-hosted PDF) | July 2020 - June 2023; Cboe SPX/SPXW trade data with participant flags | Not a trading test; the effect is an upper bound from a GARCH counterfactual | [WP, full text] |
| Dealers' aggregate gamma imbalance (stock-level proxy built from OptionMetrics, assuming customers are net long puts / short calls, citing Garleanu et al.) is linked to intraday momentum when negative and reversal when positive, strongest for illiquid stocks, and to the frequency and size of flash crashes | Barbon and Buraschi, Gamma Fragility (March 2021 version; full text read) | Stocks, 1996-2017 for the intraday autocorrelation figure; flash-crash events 1997-2015 | Proxy is noisy by the authors' own admission; no trading test | [WP, full text] |
| End users net long SPX options (especially OTM puts), so dealers short index options; end users net short single-stock options (dealers long) | Garleanu, Pedersen, Poteshman (NBER 11843) | 1996-2001 | n/a | [WP, full text; RFS 2009] |
| Closing prices of optionable stocks cluster at strikes on expiry; shifts returns by at least 16.5 bp per expiry (about USD 9bn market cap) attributed to market-maker hedging and firm proprietary-trader manipulation | Ni, Pearson, Poteshman JFE 2005 | See paper | Abstract (HKBU record) re-read; body unread | [PR, abstract] |
| [OWN-DATA] SqueezeMetrics' own public GEX series (backfilled from May 2011): SPX next-day return standard deviation by GEX quartile (lowest to highest) 1.69, 0.90, 0.71, 0.73 percent (full sample); lowest quartile higher than highest in every sub-period (2011-15: 1.48 vs 0.53; 2016-19: 1.24 vs 0.47; 2020-22: 2.57 vs 0.89; 2023-26: 1.34 vs 0.61). GEX below zero on only 8.9 percent of days. In a regression of next-day absolute return on lagged absolute return, its 5- and 22-day means and VIX, adding the trailing-252-day GEX percentile gives a coefficient of about -0.0025 (Newey-West t about -4.0), R-squared up from 0.307 to 0.314, similar sign and size in 2012-19 (t -5.1) and 2020-26 (t -2.8) | Public SqueezeMetrics DIX.csv; Yahoo VIX and S&P 500 | 2 May 2011 - 6 Oct 2026, 3,881 days | Descriptive and in-sample on vendor's definition (history backfilled; methodology may have changed); absolute close-to-close return rather than intraday RV; VIX already contains much of the information; no trading rule, no costs, no placebo | [OWN-DATA] |
| BIS Quarterly Review March 2024, Box B (Todorov and Vilkov): 0DTE options were over half of SPX option volume in August 2023 (from about 5 percent in 2016); the authors doubt 0DTE explains the low VIX and suggest dealers hedging yield-enhancement structured products (covered calls) dampen volatility; BIS QR September 2024 (via search summary): the August 2024 VIX spike appears amplified by purchases of equity index options and by hedging of structured products | BIS (central bank affiliated), not Fed | 2016-2024 | Suggestive, no test | [PRAC/central bank; Box B read, September 2024 via summary] |
| Cboe: average intraday net market-maker gamma of about $170m to $670m in 2023, i.e. 0.04 to 0.17 percent of about $400bn daily S&P futures notional; interquartile at 3:30 pm roughly -$1.1bn to +$2.4bn; no increase in sudden 2-sigma one-minute moves; example day (Aug 15, 2023) makers long about $2bn gamma during a decline, turned short about -$500m only near 3:30 pm | Cboe Insights, Sept 2023 | 2023 | Exchange with commercial interest; SPX only; admits makers may hedge in other expiries/products | [PRAC] |
| Bank of America estimate that delta hedging cut S&P 500 volatility by about 2.7 points over one month | Via a search summary of broker commentary | One month | Not peer-reviewed; unverified | [SEC] |

Opex / vanna / charm: I found no peer-reviewed study of vanna or charm flows or of an S&P 500 monthly-opex seasonal driven by them. The strongest related evidence is stock-level pinning (Ni et al. 2005). The search for such studies returned vendor and TradingView material, in which flow magnitudes require unobservable dealer positions.

Federal Reserve evidence: I searched Fed Board, NY Fed, BIS, BoE and IMF domains and found no FEDS note or staff report testing dealer GEX or 0DTE hedging flows. The closest Fed item is Yang-Ho Park, "Variance Disparity and Market Frictions" (FEDS 2019-059), which relates to VIX derivatives versus SPX options, funding and market illiquidity, and notes market makers' net SPX option positions tend to be negative with limited hedging capital [Fed WP; peripheral; I read only the abstract]. Dim et al. cite a BIS (2024) observation about yield-seeking volatility selling; that is now identified and read as BIS Quarterly Review March 2024 Box B (Todorov and Vilkov), summarised in the table above. Two further searches this pass (Fed, then BIS/ECB/IMF/BoE) again found no Fed Board, NY Fed, ECB, IMF or Bank of England paper testing GEX or dealer gamma; the BIS items are short commentary, not tests. So "central-bank evidence on whether GEX is real" is: none found; the closest are BIS commentary pieces that assume dealers are long gamma through structured-product hedging (March 2024) or amplifying (September 2024, via summary), which themselves disagree.

Critical assessment:
- What is probably real: end-of-day momentum linked to hedging demand; stock-level pinning; a state-dependent relationship between inventory sign and volatility in datasets where dealer positions are observed (Pearson et al. used a proprietary customer-position dataset).
- What is weak: using public open interest plus a fixed sign assumption to estimate dealer net gamma. The two sides of the 0DTE literature disagree on the sign of the effect (dampening vs amplifying), which itself tells you the identification is hard. Second-pass reconciliation: the disagreement is partly about what is measured. Adams et al., Dim et al. and Vasquez et al. all find the average effect of market-maker gamma is stabilising (gamma mostly positive); Vasquez et al. and the Brogaard-type results concern the conditional tail when gamma turns negative or when 0DTE volume is high. They are not necessarily contradictory, but only the first group conditions on observed dealer positions; Brogaard et al. (secondary only) work with volume.
- What my own descriptive check adds [OWN-DATA]: the vendor's public GEX series does line up with next-day volatility in the direction the theory implies and survives control for VIX, but the incremental R-squared is under one percentage point, the series is a backfilled vendor product, and it says nothing about whether a trader can earn money from it. It does soften my first-pass stance that GEX was "mostly vendor assertion": the correlation with volatility is real in their data; the causal story (dealer hedging) and tradability remain unsupported.
- Magnitude: Cboe's numbers imply dealer gamma is a tiny share of futures liquidity on most days; the tail days (outer whiskers 1.3 to 1.9 percent of notional) are where effects, if any, would be visible.
- Capacity and costs: no costed backtest of GEX trading exists in the sources. Vendor performance claims are unverifiable. Baltussen's intraday strategy requires trading futures at the close/30 minutes before; costs in index futures are small, so it is the one component that may survive; it is also public since 2021, so decay is plausible and untested here.
- Crowding: GEX levels are now widely published, which may turn them into self-fulfilling levels or into a signal that is already arbitraged.

## 6. Failure regimes and risks, including tail and ruin analysis

- Wrong sign: when customers are net sellers of options (covered-call and put-selling ETFs, retail 0DTE spread selling), dealers are net long what customers sold, and actual dealer gamma is opposite to the vendor assumption. A strategy that sells premium on "positive GEX" would then be selling vol exactly when real dealers are short gamma. That is the main hidden failure mode.
- Event days: macro prints, FOMC, earnings: realised moves ignore the GEX regime. Selling premium in a "positive-GEX, low-vol" regime into a gap is short-vol (see C1) in disguise.
- Intraday level trading: stops placed at "gamma walls" are crowded; gap-through risk.
- Ruin arithmetic [OWN]: if a trader sells 0DTE premium whenever GEX is high, each trade loses a multiple of premium collected on a 2 to 3 percent day. With 0DTE ATM straddles worth roughly 0.5 to 0.8 percent of index at open on a normal day (my approximation, unverified), an unhedged short straddle loses up to the full excess of move over premium; a 3 percent gap day costs roughly 2.2 to 2.5 percent of notional, i.e. several months of average captured premium. Defined-risk spreads cap this.
- Data risks: OI is published once daily after the fact, so intraday positioning shifts (new 0DTE trades) are invisible to an OI-based GEX; vendors estimate it with trade data and models; staleness; contract adjustments; assumptions about customer vs firm vs market-maker classification.
- Regulatory/structural: exchange rule changes (new expiries), index inclusion, and shifts in dealer risk appetite change the regime.

## 7. MY TWIST (hypotheses, not backtested)

**Twist 1: Realised-gamma validation gate instead of assumed sign.**
- Rationale (second-pass note: still UNTESTED; my descriptive check suggests vendor GEX carries some information, so the gate would test whether the sign assumption adds value beyond VIX, not whether GEX is useless): the sign assumption is the weak link. Instead of trusting vendor GEX sign, test whether the market behaves as if dealers are long or short gamma, using realised intraday return autocorrelation and the Baltussen momentum coefficient over the trailing 20 days.
- Rule: compute rolling 20-day coefficient b of last-30-minute return on rest-of-day return in ES/SPY. Use vendor GEX only when sign(GEX) agrees with sign(b) (b > 0 with GEX < 0; b < 0 with GEX > 0). When they disagree, ignore GEX.
- Parameters: window {10, 20, 40 days}; agreement threshold |b| > {0, 0.05, 0.1}; product {ES, SPY}.
- Expected effect: fewer signals, cleaner regime definition, lower exposure to sign-error days.
- Falsification: reject if, over a 5+ year sample, conditioning on agreement does not reduce next-day realised-volatility forecast error versus HAR-RV by at least 5 percent (Diebold-Mariano p < 0.10), or if the effect lives entirely in 2020.

**Twist 2: Close-window momentum with a GEX/inventory filter and event exclusions.**
- Rationale: the best-evidenced piece (intraday momentum into the close) should be strongest on negative-gamma days and weak on long-gamma days (Baltussen et al.). Combine with exclusion of days with scheduled macro at 14:00 or 16:00.
- Rule: at T-30 min, if rest-of-day return exceeds k x trailing intraday vol and the gamma proxy NGE < 0, take a position in the direction of the move, exit at the close. Skip FOMC, CPI and quad-witching days (test separately).
- Parameters: k in {0.25, 0.5, 1.0}; entry time {T-60, T-30, T-15}; NGE threshold percentile {50, 70}; position size 0.25-1 x vol-targeted.
- Expected effect: positive edge in negative-NGE regimes, near zero otherwise; needs cost check at 0.5-1 tick slippage per side in ES.
- Falsification: reject if net Sharpe over the last 5 years of data is below 0.4 at 1 tick per side slippage, or if the NGE-negative subset is not statistically better than NGE-positive at 90 percent.

**Twist 3: Opex pin fade only where dealer sign is observable (single stocks with proprietary-style proxies).**
- Rationale: pinning evidence is stock-level. Caution from Garleanu et al. (1996-2001): end users were net short single-stock options, i.e. dealers long, so the dealer-gamma sign for single stocks may be the opposite of the index case; the pinning mechanism in Ni et al. is hedge rebalancing by market makers plus manipulation, not a simple GEX sign. Test on high-OI single stocks and on high-OI strikes with clearly one-sided customer flow (e.g. high volume of customer-bought options), not on SPX.
- Rule: on monthly expiry day, for stocks with OI at the nearest strike in the top decile and spot within 1 percent of that strike at T-60 min, enter a delta-hedged short straddle at that strike or a strike-pinning trade in the stock; exit at the close.
- Parameters: OI percentile {80, 90, 95}; distance {0.5, 1, 2 percent}; liquidity filter.
- Expected effect: small, costly; may disappear after costs.
- Falsification: reject if abnormal pinned-close frequency (versus a strike-lattice null) is not significant at 95 percent over 5 years, or if net of option spreads it does not beat zero.

## 8. Implementation spec

**Data:** daily OI by strike/expiry (OCC/OPRA), end-of-day option quotes for IV and Greeks, intraday SPX/ES/SPY 1-minute bars, 0DTE trade-and-quote files if available (Cboe DataShop with customer/firm/market-maker flags is the closest to observed positioning), VIX, economic calendar. Vendor GEX series (SqueezeMetrics DIX/GEX or SpotGamma) as a benchmark, not the signal.

**Signals:** GEX_total, GEX_by_strike, gamma flip, NGE (Baltussen-style proxy), trailing intraday momentum coefficient, 0DTE share of volume.

**Sizing:** futures notional scaled to vol target (for example 0.5 percent daily risk budget); option sleeve limited by defined-risk loss cap.

**Execution:** futures at the close window with limit orders; avoid trading in the last 2 minutes if spread explodes; options defined-risk only.

**Stops:** time stop at the close for intraday trades; hard max loss per day of 0.5 to 1 percent of NAV.

**Cost model:** ES slippage 0.25 to 1 tick per side plus commission; SPX option spreads at 25-50 percent of half spread for SPXW 0DTE ATM in calm markets, 100 percent in stress; stock option spreads wider; assume f varies by liquidity decile.

**Pseudo-code:**
```
daily: compute GEX_total, flip, b_20 (rolling momentum coef)
if signal_conflict(sign(GEX_total), sign(b_20)): regime = UNKNOWN -> no trade
at T-30min:
    r_rod = ret(prev_close -> T-30)
    if NGE<0 and abs(r_rod) > k*sigma_intraday and not event_day:
        pos = sign(r_rod) * size_vol_target
        enter ES at limit; exit at close (MOC or last 1 min)
log: gross, slippage, GEX regime, event flags
```

## 9. Backtest plan

- Reproduce the stylised facts before any trading rule: (a) intraday momentum into the close for ES, 2010 to present, in-sample and out-of-sample, with and without 2020; (b) the unconditional relation between lagged vendor-style GEX (computed by me from OI) and next-day realised volatility, controlling for VIX and lagged RV (SqueezeMetrics argues GEX beats VIX; test whether it adds to HAR-RV).
- Walk-forward: expanding windows, 1-year step, parameters frozen out of sample; final 2 years held out.
- Multiple testing: count all variants; deflated Sharpe, SPA test; stationary bootstrap; report t-stats with Newey-West.
- Costs: slippage grid (0.25, 0.5, 1.0 tick); option fill factor grid.
- Compare to benchmarks: intraday-momentum without GEX; random-day placebo (shuffle GEX sign); pre- and post-publication splits (2016, 2021).
- Metrics: hit rate, mean per trade, Sharpe, Sortino, worst day, drawdown, regime-conditional performance, stability across years. Emphasise whether any result is driven by March 2020 or 2022.
- Pass criteria (pre-set): placebo-adjusted edge significant at 95 percent, net Sharpe above 0.5 at 0.5 tick slippage, stable sign across at least 6 of 8 calendar years.

## 10. Risk management and kill-switch rules

1. No naked short premium based on GEX alone; defined-risk only.
2. Max daily loss 1 percent of NAV; weekly 2.5 percent; monthly 5 percent: then flat for the rest of the period.
3. Stand down on FOMC/CPI/jobs days and in the first 30 minutes after a gap larger than 1.5 percent.
4. If the rolling 60-day hit rate of the filter falls below 48 percent (for a binary rule) or the realised Sharpe falls below 0 over 60 days, halve size and re-validate.
5. Dependency kill: if the vendor changes methodology or data licensing, freeze signals until reconciled with in-house computation.
6. Never size by "walls" alone: treat as zones with fat tails.

## 11. Annotated sources

| # | Source | URL | Type | Grade | Note |
|---|---|---|---|---|---|
| 1 | SqueezeMetrics, Gamma Exposure (GEX) white paper, rev. Dec 2017 | https://squeezemetrics.com/monitor/download/pdf/white_paper.pdf | Vendor (read) | C+ | Primary definition; no sample/costs |
| 2 | Baltussen, Da, Lammers, Martens, Hedging demand and market intraday momentum (JFE 2021) | https://www3.nd.edu/~zda/intramom.pdf | PR (read) | A | Best-evidenced gamma-related effect |
| 3 | Ni, Pearson, Poteshman, Stock price clustering on option expiration dates (JFE 2005) | https://academicnewsletter.sufe.edu.cn/info/357561 | PR (abstract via search) | A | Stock-level pinning |
| 4 | Pearson, Poteshman, White, Does option trading have a pervasive impact on underlying stock prices? (2006 draft) | https://ou.edu/dam/price/Finance/CFS/paper/pearsonPoteshmanWhite.pdf | WP (read abstract, intro) | B+ | Preliminary |
| 5 | Ni, Pearson, Poteshman, White (RFS 2021) | https://ideas.repec.org/a/oup/rfinst/v34y2021i4p1952-1986..html | PR (abstract via search) | A | Noninformational channel |
| 6 | Dim, Eraker, Vilkov, 0DTEs: Trading, Gamma Risk and Volatility Propagation | https://westernfinance-portal.org/viewpaper?n=950096 | WP (read) | B+ | Contrary to amplification story |
| 7 | Adams et al., Do S&P500 Options Increase Market Volatility? Evidence from 0DTEs | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5641974 (direct: 403; abstract read from an archive.org copy of the same page) | WP (abstract read, body not) | B+ | Abstract now verified |
| 8 | Brogaard, Han, Won, 0DTE and intraday volatility | https://www.bnnbloomberg.ca/zero-day-options-are-reordering-the-way-the-stock-market-behaves-1.1921930 ; https://quantpedia.com/do-sp500-0dtes-options-increase-market-volatility/ | Press/summary (SSRN abstract not found) | C+ | Opposite finding; figures differ between summaries |
| 9 | Vasquez, Amaya, Pearson, Garcia-Ares, 0DTE Index Options and Market Volatility | https://cdn.cboe.com/resources/education/research_publications/gammasqueezes.pdf (full text); https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5113405 (abstract via archive.org) | WP (full text read) | A- | Observed dealer gamma, Jul 2020-Jun 2023; Cboe supplied data |
| 15 | Barbon and Buraschi, Gamma Fragility (March 2021) | http://www.abarbon.com/assets/Barbon_Buraschi_2021_Gamma_Fragility.pdf | WP (full text read) | B+ | Proxy-based; intraday momentum/reversal, flash crashes |
| 16 | Garleanu, Pedersen, Poteshman, Demand-Based Option Pricing (NBER 11843) | https://www.nber.org/papers/w11843.pdf | WP (full text opened; abstract and introduction used) | A- | Dealers short index options, long single-stock options, 1996-2001 |
| 17 | Todorov and Vilkov, BIS Quarterly Review March 2024, Box B | https://www.bis.org/publ/qtrpdf/r_qt2403x.htm | Central-bank commentary (read) | B | Dealers hedging structured products dampen vol; no test |
| 18 | Cboe, 0DTEs Decoded (May 2025) | https://www.cboe.com/insights/posts/0-dt-es-decoded-positioning-trends-and-market-impact | Exchange (read) | B- | Net MM gamma hedging at most 0.2% of SPX daily liquidity; conflict of interest |
| 19 | SqueezeMetrics public DIX/GEX history | https://squeezemetrics.com/monitor/static/DIX.csv | Vendor data (downloaded) | C+ | Used for own descriptive test; backfilled |
| 20 | Ni, Pearson, Poteshman JFE 2005 (HKBU record) | https://scholars.hkbu.edu.hk/en/publications/stock-price-clustering-on-option-expiration-dates-3/ | PR (abstract) | A | 16.5 bp, about USD 9bn |
| 10 | Cboe, Much Ado About 0DTEs (Sept 2023) | https://www.cboe.com/insights/posts/volatility-insights-evaluating-the-market-impact-of-spx-0-dte-options | Exchange (read) | B- | Conflict of interest |
| 11 | Park, Variance Disparity and Market Frictions (FEDS 2019-059) | https://www.federalreserve.gov/econres/feds/files/2019059pap.pdf | Fed WP (abstract) | B | Peripheral; not a GEX test |
| 12 | SpotGamma commentary (vendor) | https://spotgamma.com/zombie-market-faces-a-triple-witching-opex/ | Vendor blog | C | Via search summary only |
| 13 | rtgamma Substack on open vs real-time gamma | https://rtgamma.substack.com/p/open-gamma-vs-real-time-gamma-which | Practitioner blog | C | Via search summary |
| 14 | Princeton senior thesis on 0DTE intraday volatility | https://theses-dissertations.princeton.edu/entities/publication/61115cd1-cb09-4a8b-9230-ff488fc2a386 | Thesis | C | Literature survey via search summary |

## 12. Open questions

1. Can a public-data GEX estimate beat a plain HAR-RV forecast of next-day volatility out of sample, with VIX in the regression? Partial answer: the vendor's backfilled GEX adds under one point of R-squared over VIX plus lagged absolute returns in my in-sample check (2011-2026, coefficients stable across halves). Still open: out-of-sample, intraday RV targets, GEX computed by me from raw OI, and whether it adds anything over HAR-RV plus VIX.
2. What is the real sign of aggregate dealer gamma in SPX over time? Only exchange or dealer data can tell; Cboe says it is balanced.
3. Does the 0DTE effect flip sign depending on regime (Adams et al. vs Brogaard et al.)? Adams et al. abstract and Vasquez et al. full text now read; Brogaard et al. still not located on SSRN, and the Adams body was not read. Vasquez et al. suggest the mean effect is stabilising and the tail effect (negative gamma) is bounded at a few volatility points.
4. Has the Baltussen intraday momentum effect decayed since publication in 2021?
5. Is there any vanna/charm opex effect after controlling for ordinary expiry-week seasonality and dividends? I found no study.
6. Where is the Fed evidence? I found none directly on GEX, again after two more searches; BIS commentary exists (QR March and September 2024) but is not a test. A targeted search of FEDS Notes and NY Fed Liberty Street posts by someone with domain access is still worth doing.

## 13. Second-pass changelog (2026-10-07)

- Obtained the Adams et al. abstract (archive.org copy of the SSRN page; direct SSRN still 403) and the Vasquez et al. full text (Cboe-hosted PDF). Replaced the "unread" Vasquez row with its findings (typical gamma-induced volatility effect about -0.2 points; worst-case +3.3 points daily, +6.4 points 30-minute; gamma typically positive but negative on at least a quarter of days). Brogaard-Han-Won remains secondary only; the 9.1 percent and "almost 14 percent" figures from two summaries are unreconciled and flagged.
- Read Barbon-Buraschi (March 2021) and Garleanu-Pedersen-Poteshman full text; added the product- and era-specific dealer sign evidence (index: dealers short; single stocks: dealers long; 1996-2001) and rewrote the sign-assumption paragraph; added Cboe's May 2025 note.
- Corrected the Baltussen et al. entry: the paper does not include transaction costs, and its Sharpe ratios of 0.87 to 1.73 are gross (the "may survive costs" statement stays a judgement, not a result). Grade A for the mechanism evidence unchanged; grade for tradability stays low.
- Added [OWN-DATA] descriptive test of SqueezeMetrics' public GEX series versus next-day volatility; partly softens the first-pass "mostly vendor assertion" language for the correlation with volatility but not for the causal or tradable claims.
- Fed/central-bank search repeated: still no Fed paper testing GEX; BIS QR March 2024 Box B and September 2024 are commentary. Closest Fed item (Park, FEDS 2019-059) unchanged and peripheral.
- Not done: SpotGamma/vendor material not upgraded; Ni-Pearson-Poteshman-White RFS 2021 body, Dim-Eraker-Vilkov and Adams bodies not re-read; no vanna/charm or opex test found, so that part of the strategy stays at "mechanism only". Twists remain UNTESTED.
- Overall grade: GEX as a regime descriptor upgraded slightly (some stable correlation with next-day volatility); GEX as a trading signal unchanged (no cost-aware test exists); sign-assumption risk now better documented.
