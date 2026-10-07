# C1. Variance Risk Premium (VRP) Harvesting: short vol, put-writing, variance swaps, tail overlays

Status: research dossier, not investment advice. Nothing in section 7 has been backtested by me. Figures are quoted from the cited sources and are labelled by evidence grade. Anything I could not verify is marked "unverified". Prepared 2026-10-07; second pass 2026-10-07 verified the flagged secondary figures and added descriptive own-data checks (see section 13 changelog). Items marked [OWN-DATA] are descriptive statistics I recomputed from public data; they are not backtests of a trading rule.

Evidence key used throughout: [PR] = peer-reviewed journal paper; [WP] = working paper or preprint; [PRAC] = practitioner, vendor, exchange-sponsored or index-provider material; [SEC] = secondary summary I could not check against the primary text; [OWN] = my arithmetic or opinion.

---

## 1. Summary, horizon, asset class, holding period

The VRP strategy family sells equity-index volatility (implied minus subsequently realised) and keeps the premium that buyers of crash insurance pay. Implementations: (a) cash-secured put-writing (CBOE PUT / WPUT indices), (b) covered calls / buy-writes (BXM), which are the same risk with an equity beta added, (c) short variance or volatility swaps and delta-hedged short straddles, (d) short front-month VIX futures or inverse VIX ETPs (XIV, SVXY), and (e) any of these combined with a tail-risk overlay (long wings or long VIX calls). Asset class: US equity-index derivatives (SPX, VIX), with analogues in single stocks, FX and rates. Typical holding period: 1 week to 1 month (the option or swap tenor), rolled continuously; 0DTE versions hold hours. The return stream is high Sharpe in calm samples, strongly negatively skewed, and exposed to one-month loss events that can be many multiples of the average monthly gain. The premium is real in the data (see section 5) but the instrument chosen determines whether you survive collecting it.

## 2. Origin and who uses it

- Academic origin: Bakshi and Kapadia (Review of Financial Studies 2003) showed that delta-hedged S&P 500 option positions earn on average less than zero, i.e. a negative market volatility risk premium [PR; abstract read, full text paywalled]. Carr and Wu (RFS 2009) gave the model-free way to measure it by comparing a synthetic variance-swap rate (a strip of options) with later realised variance [PR; I read the 2004 working-paper version]. Bollerslev, Tauchen and Zhou (RFS 2009) showed the premium also forecasts aggregate returns [PR; I read the July 2008 working paper abstract]. Bondarenko's "Why are put options so expensive?" (Quarterly Journal of Finance 2014) argued that no model in a broad class can rationalise historical S&P 500 put prices [PR; abstract via secondary summary].
- Index and product origin: CBOE launched BXM (buy-write) first and later the PUT index (monthly ATM cash-secured put-write; history back-filled to mid-1986) and WPUT (weekly; data from January 2006) [PRAC]. Much of the PUT history is reconstructed retroactively, not live.
- Practitioner users: dealers (who are structurally on the other side, see section 3), volatility hedge funds, structured-product issuers, covered-call and put-write ETF managers, and, in the retail space, the XIV/SVXY holders. Academic-practitioner voices: Roni Israelov and Lars Nielsen (AQR) on covered calls and protective puts [PR]; Oleg Bondarenko (UIC) on PUT/WPUT, with Cboe sponsorship [PRAC/WP]; Antti Ilmanen's work places volatility selling among carry-type styles (secondary only, I could not access the book chapter) [SEC].
- I could not verify named star-trader attributions (for example to individual fund managers) from sources I read, so I do not list them.

## 3. Economic rationale and who is on the other side

Buyers of index options pay for protection against joint bad states (high volatility coincides with low wealth and tight liquidity). The VRP is therefore a risk premium, not a free lunch: Carr and Wu interpret the negative premium as investors paying to hedge upward moves in variance. Bollerslev et al. embed this in a model where time-varying economic uncertainty drives both the premium and future returns. Mechanisms commonly offered: (i) insurance demand from institutions (puts for portfolio protection, structured-product hedging, regulatory capital), (ii) dealers who are short options require compensation for unhedgeable gap, volatility and jump risk, (iii) limits to arbitrage: the strategy has crash exposure and capital constraints, and Sharpe ratios on derivative strategies overstate attractiveness because of non-normality (Carr and Wu themselves warn about this, citing Goetzmann et al.). Israelov and Nielsen add a decomposition point: a covered call is long equity beta plus short volatility, and in their stylised data roughly two-thirds of covered-call risk comes from the equity exposure and one-third from the short-straddle leg, with beta cut to about 0.64 [PR; from the AQR-hosted FAJ text].

Counterparties: portfolio hedgers and structured-product desks (long vol, price-insensitive), and tail-risk funds. You are paid for being the one who absorbs their convexity. Be sceptical when the premium is cited as "alpha": a lot of the put-write return is equity beta (Bondarenko reports beta of about 0.56 for PUT versus the S&P 500, and a small monthly alpha near 0.2 percent [PRAC/WP, Cboe-hosted]).

## 4. Canonical rules (implementable)

**A. PUT-style put-writing (monthly).** On the standard monthly expiry day, sell one-month ATM SPX puts with notional equal to the cash balance, hold T-bills as collateral (fully secured, no leverage), let the option cash-settle at expiry, repeat. WPUT is the same with weekly expiries. Index methodology treats premium as paid at sale and holds to settlement; the published indices are gross of fees and costs.

**B. BXM-style buy-write.** Hold the S&P 500 portfolio; sell a slightly out-of-the-money one-month SPX call each cycle; hold to settlement. Per Cboe commentary the call is slightly OTM, and PUT has historically beaten BXM by roughly a percentage point a year ("BXM-PUT conundrum"; the single figure comes from a blog summarising Cboe, so treat as [SEC]).

**C. Short 30-day variance swap (OTC) or its listed proxy.** Sell a variance swap at strike SW (the VIX-style fair strike) with variance notional N_var = vega notional / (2 x strike volatility). Payoff at expiry = N_var x (SW - RV), RV = annualised realised variance of daily log returns. Proxy: short a delta-hedged ATM straddle, rebalanced daily, or a strip of OTM options per Carr-Wu replication (puts below the forward, calls above).

**D. Short VIX futures / inverse ETP.** Short a constant-maturity one-month VIX futures exposure (the XIV/SVXY design). Daily-reset exposure target of -1x the S&P 500 VIX Short-Term Futures index. Rule family: stay short while the curve is in contango, flat or long otherwise.

**E. Tail-overlaid variants.** Any of A-D plus a fixed budget (for example 10-30 percent of gross premium) spent on OTM puts or VIX calls. The PPUT index (long S&P 500 plus monthly 5 percent OTM put) is the listed reference for the opposite, insurance-buying side.

## 5. Evidence

All numbers below are as reported by the source, gross of the costs stated.

| Claim | Source | Period | Costs? | Grade |
|---|---|---|---|---|
| Delta-hedged S&P index option returns below zero; effect smaller for OTM, larger when vol high | Bakshi and Kapadia 2003 | S&P 500 options (period not in abstract I read) | Not in abstract | [PR] |
| Synthetic variance swap vs realised variance: very large negative premium on S&P and Dow indices; mean log premium over -50 percent per month on S&P 500 indices; premium is small and mostly insignificant for Nasdaq-100 and for 32 of 35 individual stocks; short-swap raw information ratio above 3 on S&P/Dow, lower after Newey-West adjustment | Carr and Wu (2004 WP of RFS 2009) | Jan 1996 to Feb 2003 (option data) | No transaction costs in that analysis; authors warn Sharpe on derivative strategies is unreliable | [PR/WP] |
| Variance risk premium predicts aggregate returns, strongest at roughly quarterly horizon; needs model-free implied variance and high-frequency realised variance | Bollerslev, Tauchen, Zhou | post-1990 | n/a (predictability, not a strategy) | [PR/WP] |
| PUT index, June 1986 to Dec 2018: compound return 9.54 percent vs 9.80 for the S&P 500; annual vol 9.95 vs 14.93 percent; Sharpe 0.65 vs 0.49; beta 0.56; monthly alpha about 0.2 percent; PUT monthly skewness -2.09; average VIX 19.3 vs realised vol 15.1 (1990-2018), gap 4.2 points. Verified this pass in the Cboe-hosted PDF (the first-pass "S&P skewness about -0.81" could not be cleanly extracted from the garbled table and is dropped) | Bondarenko, Cboe-hosted white paper (2019), full text opened | 1986-2018 | Gross index, no costs; history before the 2006 weekly-option era and the PUT launch is reconstructed | [PRAC, verified] |
| Over the live-ish window Jan 2006 to Dec 2018 the advantage disappears: compound return 5.97 percent (PUT), 4.51 (WPUT), 7.59 (S&P 500); Sharpe 0.50 (PUT), 0.40 (WPUT), 0.51 (S&P 500); annual vol 10.69, 9.48, 14.32 percent. Average gross premium collected 22.1 percent a year (PUT) and 37.1 percent (WPUT). The long-run Sharpe edge (0.65 vs 0.49) therefore comes mainly from the earlier, reconstructed period | Same white paper | 2006-2018 | Gross | [PRAC, verified] |
| Max drawdown: PUT -32.7 percent, WPUT -24.2 percent, S&P 500 -50.9 percent (monthly, Jan 2006 to Dec 2018); longest drawdown 29, 22 and 52 months | Same white paper | 2006-2018 | Gross | [PRAC, verified; upgraded from SEC] |
| [OWN-DATA] Cboe PUT daily index history vs S&P 500 total return (SPY adjusted close): 2007 to 6 Oct 2026 PUT compound return 7.3 percent, vol 13.8 percent, max drawdown -37.1 percent (trough 9 Mar 2009), worst day -11.5 percent, worst month -17.7 percent; SPY(TR) 2006 to Oct 2026 11.1 percent, vol 19.2 percent, max drawdown -55.2 percent. Since Jan 2010: PUT 8.3 percent, vol 12.0, max drawdown -28.9 percent (trough 23 Mar 2020); SPY(TR) 14.2 percent, vol 17.0, max drawdown -33.7 percent. Return per unit vol (no risk-free subtracted) 2007 on: PUT about 0.53, SPY about 0.58. Weekly beta of PUT to SPY since 2006 about 0.59 (daily 0.63), consistent with Bondarenko's 0.56. BXM 2010-2026 7.5 percent, vol 12.4, max drawdown -30.3 percent | Cboe CDN index CSVs; Yahoo Finance | 2007 - Oct 2026 | Gross index, no costs | [OWN-DATA] |
| [OWN-DATA] VIX minus subsequent 21-day close-to-close realised vol of the S&P 500 (daily, overlapping): mean VIX 19.4 vs realised 15.4, mean gap 4.1 points (median 4.7), realised exceeded VIX on 14.7 percent of days; by period 1990-99 gap 5.4, 2000-09 3.2, 2010-19 3.7, 2020-26 3.8; lowest VIX decile (VIX at or below 12.2) mean gap 2.4 points, realised above VIX 13 percent of days; largest negative gap -69.9 points (entered 19 Feb 2020). Consistent with Bondarenko (4.2) and with Israelov-Nielsen's positive-88-percent figure for 1990-2014 | Yahoo Finance ^VIX and ^GSPC | 2 Jan 1990 - 8 Sep 2026 (9,238 days) | Close-to-close realised vol, not 5-minute; VIX is not a swap strike | [OWN-DATA] |
| [OWN-DATA] Proxy short-variance-swap P&L per unit of vega, strike = VIX, realised = next-21-day close-to-close variance, non-overlapping 21-day samples (n = 440): mean +2.65 vol points per month, standard deviation 8.1, best +15.3, worst -91.5 (entered 5 Mar 2020), then -57.5 (28 Aug 2008), -54.6 (29 Sep 2008), -35.7 (29 Jul 2011), -31.4 (4 Feb 2020). The worst month equals about 35 average months of gains; the sample start offset affects which days are drawn | Yahoo Finance | 1990-2026 | No costs, VIX not the exact swap strike, sampling-offset dependent | [OWN-DATA] |
| Covered-call decomposition: long equity plus short vol; downside "protection" is the equity underweight in disguise | Israelov and Nielsen, FAJ 2014 | BXM 1986-2013; hypothetical 1996-2013 | Stylised | [PR] |
| Israelov and Nielsen "Still Not Cheap" (JPM Summer 2015), per the AQR-hosted Practical Applications summary (not the paper itself): VIX minus realised volatility positive 88 percent of the time with an average of 3.4 points, January 1990 to June 2014; a protective strategy (long S&P 500 plus 5 percent OTM front-month puts, unit leverage) earns 5.2 percent of annualised excess return from passive equity exposure, loses 0.9 percent from the dynamic equity exposure of the puts and 2.0 percent from the long-volatility component; options are expensive on average in all volatility regimes; a 1987-style crash would have to occur about every 10 years on average for puts to break even (every 21 years in the lowest VIX decile, every 4 years in the highest) | AQR Practical Applications summary of the JPM paper (this pass) | 1990 - Jun 2014 | Hypothetical, per the summary's own disclaimer | [SEC], summary read; paper body not |
| The first-pass figures (puts cut returns about 2.5 points a year and Sharpe from 0.37 to 0.21 for Mar 2006 to Jun 2014; realised VRP about 2.5 percent in the lowest VIX decile) came from a Swedroe column and I could not find them in the AQR summary. They are not contradicted (the summary's -0.9 and -2.0 components add to about -2.9 points a year on a different construction) but remain unverified; do not cite them | Swedroe column via first pass | 2006-2014 | Unknown | [SEC], unverified |
| Constant-maturity one-month VIX-futures portfolio lost about 30 percent per year | Eraker and Wu, JFE 2017 (abstract via search) | 2006-2013 | Abstract level | [PR/SEC] |

Reading the evidence critically:
- The premium is robust in sign across studies and samples, but the Sharpe ratios are not trustworthy as sized. Carr and Wu themselves flag it; skewness of -2 for PUT means the standard Sharpe flatters. Bondarenko's own Stutzer figure is only slightly below the Sharpe, which tells you the sample contains few extreme tail events relative to what a 1987 or 2020-type month produces. A 32-year sample has maybe three or four genuine tail months.
- Cost realism: all CBOE index numbers are gross. Real ATM SPX bid-ask is small relative to premium for monthlies but weekly and 0DTE rolling multiplies turnover by 4 to 250 times; a Substack summary I could not verify claims volatility and skewness option strategies break even at daily intervals before costs and lose after costs. [SEC, unverified]. Duarte and Jones (via secondary search result) report that bid-ask spread effects can bias measured option returns materially. [SEC]
- Post-publication: no clean decay study found. Indirect signs: the 2018 XIV termination, the shift of premium to shorter tenors (Dim-Eraker-Vilkov report that 0DTEs earn an exceptionally high variance premium before costs, see C3), and growth of yield-oriented option-selling products. I cannot quantify capacity.
- Equity beta confound: PUT is a levered-low-beta equity exposure with a negative-skew profile. Any "alpha" claim should be tested against a beta-scaled S&P 500 plus cash benchmark, which neither Cboe nor most vendors do.

## 6. Failure regimes and risks, including tail and ruin analysis

**Regimes where it fails:** (1) volatility spikes with gap risk (Oct 1987 style, Aug 2015, Feb 2018, Mar 2020; I did not verify 1987 or 2020 magnitudes from sources I read, so I give none), (2) liquidity-vacuum days where the hedge cannot be placed at modelled prices, (3) products with mechanical rebalancing that makes the short vol exposure larger as losses accumulate, (4) dealer or exchange constraints (margin hikes force liquidation precisely at the worst point).

**XIV / SVXY case (Feb 5, 2018):** Short-vol ETPs lost more than 90 percent in a day per Augustin, Cheng and Van den Bergen (FAJ 2021) [PR; I read the CFA Institute summary page]. [OWN-DATA] From Yahoo's SVXY series: VIX closed at 17.3 on 2 Feb, 37.3 on 5 Feb and 30.0 on 6 Feb 2018 (13.5 on 31 Jan); SVXY fell about 13 percent on 2 Feb, 32 percent on 5 Feb and 83 percent on 6 Feb, and about 92.6 percent peak to trough between 26 Jan and 12 Feb. The one-day figure for SVXY in my data is therefore about 83 percent (on the trading day after the spike), and above 90 percent only over a few sessions; the "more than 90 percent in a day" statement applies to the indicative value of the terminated XIV per the paper summary and I did not verify it. In March 2020 SVXY (then -0.5x) lost about 61 percent between 14 Feb and the March low, and the PUT index drew down about 29 percent to 23 Mar 2020; the PUT index lost about 7.6 percent peak to trough in Jan-Mar 2018 (BXM 7.7 percent), so the cash-secured put form came through February 2018 far better than the ETPs. The mechanism: inverse products must buy VIX futures into the close as the index rises to restore -1x exposure; because those products were a large share of the futures market, that buying pushed futures higher, shrinking fund assets and forcing more buying. The authors compare it to portfolio-insurance dynamics and argue for disclosure of issuer market share and liquidity checks on leveraged products. Credit Suisse terminated XIV (acceleration date reported as Feb 21, 2018) and ProShares cut SVXY target exposure from -1x to -0.5x effective Feb 27, 2018. Litigation over whether the bank trades contributed was allowed to proceed in 2021 (press report; not a finding). A 2024 paper (Nielsen and Posselt, International Review of Financial Analysis) finds long-VIX ETP investors, in aggregate, sell after VIX rises [PR/WP; abstract only], consistent with persistent demand for the other side.

**Ruin arithmetic [OWN, illustrative, not from a source].** For a short variance swap with vega notional V per volatility point: payoff = V/(2K) x (K^2 - RV^2) with vol in points. If the strike is K = 17 and the next month realises 37 vol, loss = V x (1369 - 289)/34 = about 31.8 V. If instead the premium is the Bondarenko-style average (implied 19.3, realised 15.1), average gain = V x (372.5 - 228.0)/38.6 = about 3.7 V. So one such month wipes out roughly 8 to 9 average months, and if V is sized at 1 percent of capital per point the loss is about 32 percent of capital in a month while the average monthly gain is about 3.7 percent. Doubling leverage turns the same event into a 64 percent loss; with leverage near 3x, a month at 37 vol is ruin. For a cash-secured put the loss is bounded by notional (a -20 percent market month on ATM puts costs roughly 20 percent minus premium), and for inverse VIX ETPs the loss can approach 100 percent in one session. This is why exposure form matters more than the signal. [OWN-DATA calibration] My illustrative K = 17 / RV = 37 month is milder than history: using the VIX-strike proxy, the entry of 5 March 2020 produced a loss of about 91 vega points (an eventual realised vol far above 37) against an average monthly gain of 2.65, so the worst observed month was about 35 average months, not 8 to 9. At 1 percent of capital per vol point that single month would be a loss on the order of 90 percent of capital, which is why the dossier's size limits (section 10) must be read as hard caps, not suggestions.

**Other risks:** model/replication error for variance swaps with truncated strips (Carr-Wu discuss jump error in the replication), basis between listed proxies and OTC swaps, counterparty and margin risk, crowding with vol-targeting and risk-parity funds, and rule/index risk (index methodology changes; reconstructed history).

## 7. MY TWIST (hypotheses, NOT backtested by me)

**Twist 1: Term-structure and VRP-gated put-writing.**
- Rationale: the premium is state-dependent; selling when the forecast VRP is thin or the term structure is inverted is selling insurance when it is cheap or when stress has already started. Sources suggest the premium is positive even in the lowest VIX decile (Israelov-Nielsen, secondary), so gating must be tested not assumed.
- Rule: each cycle estimate VRP_t = VIX_t minus forecast 21-day realised vol (HAR-type model on 5-minute realised vol). Sell the ATM put only if (VIX3M/VIX > 1 i.e. contango) AND VRP_t > theta; otherwise hold T-bills or reduce size to 25 percent.
- Parameters to test: theta in {0, 1, 2, 3} vol points; contango threshold {1.00, 1.03, 1.05}; HAR window {1, 5, 22 days}; reduced size {0, 25, 50 percent}.
- Expected effect: slightly lower mean, materially lower worst-month loss and drawdown; Sharpe up modestly. Risk: regime filters often lag crises (VIX inversion arrives after the first move).
- Falsification: reject if, out of sample, the gated version does not reduce worst-month loss or CVaR(1%) by at least 20 percent versus the ungated PUT replica at equal average exposure, or if net Sharpe is not higher with a block-bootstrap p-value below 0.10 after the multiple-testing correction in section 9.

**Twist 2: Defined-risk short vol with fixed loss budget.**
- Rationale: ruin analysis shows leverage plus convexity is the killer; cap per-cycle loss by construction.
- Rule: sell ATM or 25-delta put spread: short put at K1, long put at K2 = K1 x (1 - w); size so max loss per cycle = b percent of NAV. Optional: add an OTM call/VIX-call sleeve costing c percent of premium.
- Parameters: w in {3, 5, 8, 10 percent}; b in {0.5, 1, 2 percent}; c in {0, 10, 20 percent}; tenors {1 week, 1 month}.
- Expected effect: lower skewness penalty and no ruin path, but the long wing gives back a large share of the premium; the net may be close to zero if the wings are priced at the same VRP.
- Falsification: reject if the spread's net annualised return after modelled bid-ask costs is not above cash by at least 2 points with Sharpe > 0.5 over any 10-year slice, or if the premium retained after buying the wing is below 40 percent.

**Twist 3: Vol-of-vol scaling.**
- Rationale: losses concentrate when vol-of-vol rises; scale exposure down when trailing VVIX-like or realised-vol-of-vol is high.
- Rule: size_t = size_0 x min(1, z / VVIX_pct_t) where VVIX_pct_t is the trailing 252-day percentile of VVIX (or realised vol of VIX).
- Parameters: percentile cutoffs {70, 80, 90}; size floor {0, 25 percent}; lag 1 day.
- Expected effect: smaller drawdown clustering; subject to the usual vol-timing caveat that the signal is autocorrelated but not predictive of jumps.
- Falsification: reject if drawdown depth is not reduced by 15 percent and the Calmar ratio does not improve in at least 3 of 4 disjoint sub-periods.

## 8. Implementation spec

**Data:** SPX/SPXW option chains with bid/ask (OPRA, CBOE DataShop, or OptionMetrics for history); VIX, VIX3M, VIX futures curve; VVIX; 5-minute SPX returns for realised variance; T-bill rates; for ETPs, official NAVs and the index.

**Signals:** VRP_t, term-structure slope, VVIX percentile, calendar flags (FOMC/CPI/earnings clusters; test only, do not assume).

**Sizing:** cash-secured notional <= 1.0 x NAV for A; for B-D, define a loss budget: NAV_loss_cap = L percent per cycle and solve notional = L x NAV / worst_case_move, where worst_case_move is the 99.9th percentile one-cycle adverse move estimated from a heavy-tailed fit and floored at -20 percent for index puts. Never size by trailing volatility alone.

**Execution:** trade monthlies by limit orders near mid at a fixed time; model fills at mid minus 25-50 percent of the quoted half-spread for index options in calm markets and 100 percent plus slippage in stress; avoid trading settle-day closes with large size; for variance swaps, use dealer RFQs (cost typically a few vega-points of spread; unverified).

**Stops/exits:** no stop-loss on a short option inside its cycle by default (stops convert tail into realised, gap-prone losses); instead hard exposure caps and a structural wing. Portfolio-level kill-switch in section 10.

**Costs model:** per roll, cost = 0.5 x quoted spread x contracts x multiplier x fill factor f; f in {0.25, 0.5, 1.0}; plus commissions/fees; collateral earns T-bill minus 25 bps for haircut. Run results across f.

**Pseudo-code:**
```
for each expiry cycle t:
    vrp = VIX[t] - HAR_forecast_RV[t]
    slope = VIX3M[t] / VIX[t]
    scale = gate(vrp, slope, vvix_pct[t])          # twist 1/3; else 1
    notional = min(scale * NAV[t] , loss_budget[t] / worst_move)
    if scale > 0:
        sell put(K=ATM, T=cycle) x notional/strike/multiplier
        buy put(K=K*(1-w)) if defined_risk
    mark daily; settle at expiry; log premium, fill factor, margin used
    apply kill-switch checks (section 10)
```

## 9. Backtest plan

- Data period: 2005-present for listed daily options; use PUT/WPUT index histories only as sanity checks (reconstructed before launch).
- Replicate PUT from raw chains first; if my replica deviates from the published index by more than a few bps per month, fix the settlement, strike selection and collateral handling before anything else.
- Walk-forward: expanding window for HAR and thresholds, retrain annually, 1-cycle embargo. Hold out the most recent 3 years untouched until the final run. Separately, report sub-periods 2008-09, 2011, 2015, 2018, 2020, 2022.
- Multiple-testing control: log every variant tried (gates x thresholds x tenors); report deflated Sharpe ratio and White/Hansen reality-check or SPA p-values; use stationary block bootstrap (block length at least 1 quarter) because overlapping weekly cycles are serially dependent.
- Metrics: annual return, vol, Sharpe, Sortino, Stutzer, skew, kurtosis, worst day/week/month, CVaR(1%, 5%), max drawdown and time-under-water, Calmar, beta and alpha against an S&P 500 plus cash benchmark scaled to equal beta, net-of-cost versions at fill factors 0.25/0.5/1.0, turnover, margin utilisation.
- Pass criteria set before running: net Sharpe above 0.5 at f = 0.5, beta-adjusted alpha t-stat above 2 after multiplicity adjustment, worst month no worse than -15 percent at planned size.

## 10. Risk management and kill-switch rules

1. Exposure cap: gross short-vega-equivalent such that a repeat of a 20-vol-point one-day VIX spike plus 10 percent index gap costs no more than 10 percent of NAV; compute daily.
2. Leveraged/rebalancing products (inverse ETPs): do not hold overnight as a core position; if used at all, cap at 1 to 2 percent of NAV and treat as a premium that can go to zero.
3. Stand down (flat or defined-risk only) when VIX3M/VIX < 1 for 3 consecutive days, or VIX closes above its 252-day 90th percentile, until a re-entry rule (term structure back above 1.03 for 5 days) is met.
4. Drawdown breaker: halve size at -8 percent from peak; flat at -15 percent; require manual review to restart.
5. Counterparty/margin: keep 100 percent initial margin as cash/T-bills; no portfolio-margin leverage; broker diversification above a size threshold.
6. Data/model kill: if realised fills deviate from model costs by more than 2x for two cycles, pause.
7. Never add to a loss to "average down the premium".

## 11. Annotated sources

| # | Source | URL | Type | Grade | Note |
|---|---|---|---|---|---|
| 1 | Carr and Wu, Variance Risk Premia (2004 WP of RFS 2009) | https://econwpa.ub.uni-muenchen.de/econ-wp/fin/papers/0409/0409015.pdf | WP (read) | A | Measurement method, index vs stock premia, caution on Sharpe |
| 2 | Bakshi and Kapadia, Delta-Hedged Gains and the Negative Market Volatility Risk Premium (RFS 2003) | https://ideas.repec.org/a/oup/rfinst/v16y2003i2p527-566.html | PR (abstract) | A | Full text not read |
| 3 | Bollerslev, Tauchen and Zhou, Expected Stock Returns and Variance Risk Premia | https://repec.econ.au.dk/repec/creates/rp/08/rp08_48.pdf | WP/PR (abstract read) | A | Predictability, not a strategy test |
| 4 | Israelov and Nielsen, Covered Call Strategies: One Fact and Eight Myths (FAJ 2014) | https://www.aqr.com/-/media/AQR/Documents/Insights/Journal-Article/FAJ-Covered-Call-Strategies-One-Fact-and-Eight-Myths.pdf | PR (read) | A- | Author firm sells related products |
| 5 | Israelov and Nielsen, Still Not Cheap (JPM 2015) | https://www.aqr.com/-/media/AQR/Documents/Insights/Interviews/PA--Still-Not-Cheap--Portfolio-Protection-in-Calm-Markets-vF.pdf (Practical Applications summary, read); paper page https://www.aqr.com/Insights/Research/Journal-Article/Still-Not-Cheap-Portfolio-Protection-in-Calm-Markets-Supplement | PR (summary read; paper body not) | B | Swedroe-sourced numbers replaced by summary figures |
| 6 | Bondarenko, Historical Performance of Put-Writing Strategies (Cboe white paper 2019) | https://cdn.cboe.com/resources/education/research_publications/PutWriteCBOE19_v14_by_Prof_Oleg_Bondarenko_as_of_June_14.pdf (full PDF read); summary page https://www.cboe.com/insights/posts/white-paper-shows-volatility-risk-premium-facilitated-higher-risk-adjusted-returns-for-put-index | PRAC (full text read) | B+ | Exchange-sponsored, gross of costs; 2006-2018 Sharpe edge disappears |
| 15 | Cboe PUT, BXM, WPUT, PPUT daily history CSVs | https://cdn.cboe.com/api/global/us_indices/daily_prices/PUT_History.csv (and BXM, WPUT, PPUT) | Index data (downloaded) | B | PUT file has sparse pre-2007 dates; Yahoo's ^PUT had a bad print on 13 Mar 2020, so Cboe file used |
| 16 | Yahoo Finance ^VIX, ^GSPC, SPY, SVXY via yfinance | https://finance.yahoo.com/ | Aggregator (downloaded) | C+ | Used for own-data checks; FRED VIXCLS request timed out |
| 7 | Bondarenko, Why Are Put Options So Expensive? (QJF 2014) | https://ideas.repec.org/a/wsi/qjfxxx/v04y2014i03ns2010139214500153.html | PR (abstract) | A | |
| 8 | Cboe: Bondarenko 2016 PUT/WPUT study announcement | https://ir.cboe.com/news/news-details/2016/New-Study-On-Weekly-Monthly-SP-500-PutWrite-Indexes-Released-01-27-2016/default.aspx | PRAC | B | Premium income and skew numbers |
| 9 | Augustin, Cheng, Van den Bergen, Volmageddon and the Failure of Short Volatility Products (FAJ 2021) | https://rpc.cfainstitute.org/research/financial-analysts-journal/2021/volmageddon-failure-short-volatility-products | PR (summary read) | A | Feedback-loop mechanism |
| 10 | Eraker and Wu, Explaining the negative returns to volatility claims (JFE 2017) | https://academicnewsletter.sufe.edu.cn/info/356257 | PR (abstract) | A | About -30 percent per year for constant-maturity VIX futures 2006-2013 |
| 11 | Nielsen and Posselt, Betting on mean reversion in the VIX? (IRFA 2024) | https://pure.au.dk/ws/files/443099436/1-s2.0-S1057521924003533-main.pdf | PR (abstract) | B | Flow behaviour of long-VIX ETP holders |
| 12 | Rauch and Alexander, Tail Risk Premia for Long-Term Equity Investors | https://arxiv.org/pdf/1602.00865 | WP (skimmed) | B | Moment-swap premia; variance premium responds to size/growth factors |
| 13 | ProShares SVXY leverage change coverage (CNBC) | https://www.cnbc.com/2018/02/27/firm-swoops-in-to-ensure-volatility-is-a-trade-for-another-day.html | Press | C | Via search result only |
| 14 | Asset Consulting Group BXM/PUT update | https://acgnet.com/getattachment/845363f3-97c7-4ac9-be31-762e60b9143d/BXM-PUT-Update;.aspx | PRAC | C | Via search snippet; 10.1 vs 10.3 percent, about 66 percent of risk (1986-2017) unverified |

## 12. Open questions

1. What is the net-of-cost alpha of PUT-style selling after adjusting for equity beta and using realistic fills, 2010 to date? No source I read answers this.
2. Has the VRP migrated to 0DTE/weekly tenors (Dim-Eraker-Vilkov say 0DTE premium is the largest before costs), and does it survive costs there?
3. Does the VRP gating in twist 1 survive out of sample, or is it a restatement of "avoid short vol after a spike", which costs the rebound premium?
4. How much of the bid-ask bias in measured option returns (Duarte-Jones, secondary) applies to index ATM options?
5. What is the true crowding level in short-vol today (listed put-write ETFs, vol-selling structured products) and is capacity falling?
6. Is a defined-risk spread actually cheaper than the tail-hedge budget it replaces once skew is priced?
7. Partly resolved: Mar 2020 and 2008 magnitudes are now estimated from public data (variance-swap proxy worst months -91.5 and -57.5 vega points; PUT max drawdown -37.1 percent in 2009, -28.9 percent in 2020). Oct 1987 is still not checked (the Cboe PUT file has sparse early dates and I did not use it).
8. The 2006-2018 live-ish window shows PUT and WPUT Sharpe at or below the S&P 500 (0.50 / 0.40 vs 0.51) while the 1986-2018 figure favours PUT (0.65 vs 0.49). How much of the long-sample edge is reconstruction and 1990s richness (my own VIX-RV gap by decade: 5.4 in the 1990s vs about 3.2 to 3.8 since)?

## 13. Second-pass changelog (2026-10-07)

- Opened the full Bondarenko/Cboe white paper and verified the flagged figures: 9.54 vs 9.80 percent compound return, 9.95 vs 14.93 volatility, Sharpe 0.65 vs 0.49, beta 0.56, alpha about 0.2 percent a month, PUT skew -2.09, VIX 19.3 vs realised 15.1, drawdowns -32.7 / -24.2 / -50.9 percent. Upgraded the drawdown row from [SEC] to [PRAC verified] and source 6 from B to B+. Dropped the unverifiable "S&P skewness about -0.81".
- New material fact from the same paper: over 2006-2018 PUT Sharpe was 0.50, WPUT 0.40, S&P 500 0.51, i.e. no risk-adjusted advantage; the long-run edge is concentrated in the reconstructed earlier period. This lowers my confidence in the "PUT beats equities on a risk-adjusted basis" headline and is reflected in the grade of the family as an implementable edge (down one notch for the plain PUT replica).
- "Still Not Cheap": found the AQR Practical Applications summary; replaced the Swedroe-sourced numbers (2.5 points, Sharpe 0.37 to 0.21, 2.5 percent in lowest decile) with the summary's figures (88 percent positive, 3.4 points, -0.9 and -2.0 point components, break-even crash frequencies) and marked the Swedroe numbers unverified. Paper body still unread.
- Added [OWN-DATA] checks: VIX minus subsequent realised vol (1990-2026), variance-swap proxy distribution and worst months (Mar 2020, Aug-Sep 2008, Jul 2011), PUT/BXM return and drawdown vs SPY total return, and SVXY Feb 2018 and Mar 2020 episodes. These reproduce Bondarenko's VRP gap (4.1 vs 4.2) and quantify the left tail more severely than the dossier's illustrative K = 17 / RV = 37 month. Corrected the Feb 2018 wording: SVXY -83 percent on 6 Feb and about -93 percent peak to trough in my data; the ">90 percent in a day" statement is not reproduced for SVXY.
- Not done: Bakshi-Kapadia, Carr-Wu, Bollerslev et al. not re-read (first-pass reading stands); Duarte-Jones and the Substack cost claim still secondary; no costed live PUT replica built. Twists remain UNTESTED hypotheses.
- Overall: premium existence confirmed again on public data; implementable-edge grade for the plain put-write unchanged-to-lower, short-vol ETPs unchanged (worst), defined-risk and gated variants remain hypotheses.
