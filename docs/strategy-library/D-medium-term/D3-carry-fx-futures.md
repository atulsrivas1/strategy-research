# D3. Carry in FX and futures (currency carry, roll yield, cross-asset carry)

Status: research dossier, not investment advice. Research date: 2026-10-07. Labels: [PR] peer-reviewed, [WP] working paper, [PC] practitioner/press claim, [UNV] unverified. TWIST sections are hypotheses NOT backtested. Second pass (2026-10-07): [OWN] = my own quick Python recomputation on free data (caveated in section 5); FT = full text read, abstract = abstract/landing page only.

## 1. Summary, horizon, asset class, holding period

Carry strategies hold the assets that pay the most "for waiting" and short those that pay the least, assuming prices do not change. In FX it means going long high-interest-rate currencies and short low-interest-rate currencies (via forwards); in commodity futures it means buying backwardated contracts (positive roll yield) and shorting contango; in bond, equity and credit markets it means yield/dividend/roll-down analogues. Horizon: monthly rebalancing, positions held weeks to months, effectively a slow, persistent signal (carry changes slowly). Asset classes: FX, commodities, government bonds, equity indices, credit, options. The empirical premium is large, the return profile is negatively skewed in FX, and losses cluster in global recessions and volatility spikes (August 1998, 2008, March 2020, August 2024).

## 2. Origin and who uses it

- Currency carry is a long-standing FX hedge-fund and bank-prop-desk strategy; the academic anchor is the "forward premium puzzle" (uncovered interest parity fails; Meese-Rogoff 1983 is a related reference noted in the Koijen et al. paper) [PR].
- Lustig, Roussanov and Verdelhan (2011), "Common Risk Factors in Currency Markets", Review of Financial Studies 24(11) [PR].
- Brunnermeier, Nagel and Pedersen (2008), "Carry Trades and Currency Crashes", NBER Macroeconomics Annual [PR].
- Menkhoff, Sarno, Schmeling and Schrimpf (2012), "Carry Trades and Global Foreign Exchange Volatility", Journal of Finance 67(2) [PR].
- Koijen, Moskowitz, Pedersen and Vrugt, "Carry" (NBER WP 19325, Aug 2013, revised Dec 2013; the NBER page, opened in the second pass, lists the published version as Journal of Financial Economics 2017, DOI 10.1016/j.jfineco.2017.11.002; I recall volume 127 of 2018 for the print issue but did not verify that) [PR].
- Users: global macro funds, AQR/other style-premia funds, bank "alternative risk premia" products, FX overlay managers, commodity index "roll-yield" strategies [PC].

## 3. Economic rationale and who is on the other side

- Risk compensation: high-carry currencies tend to fall in bad global states. LRV find a common "slope" factor (HML_FX) explains cross-sectional carry returns; Menkhoff et al. find a global FX volatility factor accounts for more than 90% of the cross-section of carry-portfolio excess returns (paper abstract; I did not re-derive) [PR]. The premium is thus plausibly insurance-selling: you earn a stream and suffer in crises.
- Crash risk/funding liquidity: Brunnermeier-Nagel-Pedersen link negative skewness to sudden unwinding when risk appetite and funding liquidity fall [PR].
- Koijen et al. show carry predicts returns in every asset class studied and that the diversified carry portfolio does badly during global recessions; they argue part of the premium may compensate for exposure to extreme recession states [PR].
- Commodity carry: backwardation can reflect scarce inventory (theory of storage, convenience yield) and hedgers' demand to sell forward (Keynes-Hicks normal backwardation). Second pass, full texts read: Gorton and Rouwenhorst (2004/2006) and Erb and Harvey (FAJ 2006) both present the evidence as favouring term-structure-based risk premia, but Erb-Harvey stress that individual commodity average excess returns were not statistically different from zero and that the result is "inconsistent with" long-only normal backwardation (contangoed commodities also had negative average excess returns). So the hedger-insurance story is a hypothesis, not established; the sorting-on-basis evidence is empirical regardless of its cause [PR].
- Constraints: central banks and policy regimes (rate-setting) create persistent differentials; limits to arbitrage and leverage constraints of carry traders allow it to persist.

Counterparties: hedgers, central banks, importers/exporters, investors seeking safe-haven currencies (JPY, CHF), and funding-constrained leveraged traders who are forced to unwind.

## 4. Canonical rules

### FX carry (LRV style) [PR]
- Universe: developed and some emerging currencies with liquid one-month forwards (LRV: 9 countries at start of sample in 1983 up to 26).
- Each month, sort currencies by forward discount (equivalently interest differential vs USD) into six portfolios; go long the highest-carry portfolio, short the lowest (HML_FX), equal weighted.
- Hold one month, rebalance. Returns computed with bid-ask spreads on spot and forward.

### Cross-asset carry (KMPV) [PR]
- Define carry as the expected return of a security assuming prices do not change: FX = interest differential; commodity = futures-spot basis annualized (roll yield); bonds = yield spread plus roll-down; equity = expected dividend yield minus rate (futures basis).
- Within each asset class: long high-carry, short low-carry; weights proportional to the cross-sectional rank/deviation from the mean (the paper uses such a weighting; verify construction in Table 2 before replication).
- Diversified global carry factor: asset-class portfolios combined with inverse-volatility weighting.

### Time-series/level variants
- Take positions based on carry sign or magnitude of each instrument vs its own history (the KMPV "static vs dynamic" decomposition; they show carry has both a cross-sectional and a time-varying component).

## 5. Evidence

| Claim | Source (read?) | Sample | Costs | Grade |
|---|---|---|---|---|
| Carry long-short Sharpe about 0.7 on average within asset class; diversified carry across classes Sharpe 1.10 vs 0.47 for passive diversified long; passive exposure 0.21 on average | Koijen et al., NBER WP 19325 (read text) | FX from Nov 1983; various through Sep 2012 | Gross; paper itself warns of larger transaction costs and funding issues for the diversified strategy | PR/WP |
| Three biggest carry drawdowns: Aug 1972-Sep 1975, Mar 1980-Jun 1982, Aug 2008-Feb 2009, coinciding with global recession/macro events; all asset-class carry strategies do poorly together then | same | same | Gross | PR/WP |
| Diversified carry has less negative skew than single-asset currency carry but "potential for large negative returns appears pervasive" | same | same | Gross | PR/WP |
| FX HML (carry) long-short Sharpe 0.50 after bid-ask spreads; net spread between top and bottom portfolios 454 bps/year; six portfolios sorted on forward discount | LRV 2011 (read) | Nov 1983-Dec 2009 | Net of bid-ask (authors call their cost estimates conservative: Reuters quotes used, roughly double typical actual spreads) | PR |
| Carry-portfolio excess returns: global FX volatility innovations explain over 90% of cross-section; high-rate currencies perform badly when vol rises | Menkhoff et al. 2012 (abstract level from search summary) | sample not verified | not read | PR |
| Exchange-rate moves between high- and low-rate currencies are negatively skewed due to unwinding; risk of crash related to funding liquidity and VIX | Brunnermeier-Nagel-Pedersen (abstract/summary) | sample not verified | not read | PR |
| Commodity basis sorting: each month rank commodity futures on annualized (F1-F2)/F1 basis; the high-basis half beat the equal-weight index by 4.87% a year and the low-basis half lagged it by 5.17%; high minus low about 10.04% a year, standard deviation about 13.16%, Sharpe 0.76 (the table was garbled in text extraction but 10.04/13.16 = 0.76 is internally consistent) | Gorton and Rouwenhorst, NBER WP 10595 (FT read; Table 8) | Jul 1959-Dec 2004 | Gross; no transaction costs | PR/WP, upgraded from [UNV] |
| Roll returns explain 91.6% of the long-run cross-section of individual commodity excess returns; commodities with positive roll return averaged about 9 points a year more excess return than negative-roll ones (7.5 from roll, 1.4 from spot); but individual average excess returns were not statistically different from zero. GSCI long when backwardated earned 11.2% a year, when contangoed -5.0%; long-short by GSCI term structure earned 8.2% a year vs 2.68% long-only | Erb and Harvey, FAJ 62(2) 2006 (FT read) | Dec 1982-May 2004 | Gross; their indices are partly hypothetical before trading start (they flag construction bias) | PR |
| G10 currency carry: dollar-neutral equal-weighted carry Sharpe 0.49 (se 0.19), mean 1.61% a year (se 0.58) over the full sample, 0.52 in the later 1990-2013 sample; skewness about -0.47; the USD-based ("dollar carry") version has Sharpe 0.78 (se 0.19) but much of that is a dollar bet; alternative base currencies Sharpe 0.36 (JPY) to 0.71 (CAD) | Daniel, Hodrick, Lu, NBER WP 20433 / Critical Finance Review 2017 (FT read via downloaded PDF) | Jan 1976-Aug 2013 | Gross; the paper notes minimal costs for daily rebalancing and does not centre costs | PR; independent of LRV, gives a lower dollar-neutral Sharpe than KMPV |
| "Good carry" vs "bad carry" G10 trades: good trades have higher Sharpe ratios and sometimes positive skew; bad trades substantially lower Sharpe and highly negative skew; good trades avoid the classic AUD and JPY legs | Bekaert and Panayotov, NBER w25420 (abstract only; no sample or numbers on the page) | not stated | n/a | PR, abstract level |
| [OWN] FX carry on 9 USD crosses (EUR, GBP, AUD, NZD, JPY, CAD, CHF, NOK, SEK), monthly, long top 3 / short bottom 3 by 3-month interbank rate differential vs USD; Sharpe 0.43 (t 2.2) over Feb 1999-Dec 2025 gross, 0.42 with 2 bp per side; sub-periods 0.49 (1999-2008), 0.47 (2009-2019), 0.19 (2020-2025), 0.28 (2012-2025, t 1.0); worst month -10.5%, max drawdown -28%, skew -0.66 | my script (session scratchpad d2scripts/carry.py) on FRED daily spot rates and OECD monthly 3-month interbank rates via FRED | 1999-2026 | 0/2/5 bp per side on weight changes; no funding, margin or forward-points frictions | OWN, low grade (see caveats below) |
| Aug 5, 2024: yen rallied about 6% vs USD from Jul 29 to Aug 5, Nikkei fell about 12.4% in one session, VIX spiked to about 65; reported as a carry-trade unwind (causality is the press narrative) | News/blog summaries | Aug 2024 | n/a | PC |

Critical assessment:
- Headline Sharpe ratios of 0.7-1.1 (KMPV) are gross; FX carry's net Sharpe of 0.5 (LRV) is more believable and comes from a sample ending 2009. Second pass: Daniel-Hodrick-Lu (1976-2013, full text) put the dollar-neutral G10 carry Sharpe at about 0.5, well below the dollar-based 0.78, so even pre-2013 the "0.7-1.1" headlines depend on dollar exposure and on diversification choices. My own quick check (OWN, below) gives a gross Sharpe of 0.4-0.5 over 1999-2025 with only 0.19-0.28 in 2012-2025, but the t-statistics (1.0 or less in the late windows) do not separate a decayed premium from a quiet period.
- The KMPV diversified Sharpe depends on volatility-weighting across asset classes and on equity-option carry, which has very high volatility and execution complexity; discount the diversified headline for retail implementation.
- The "free" part of carry is partly returned in crashes: the strategy is closer to selling insurance than to arbitrage. The sample contains few independent recession/crash events (three major drawdowns in about 40 years per KMPV), so tail estimates are statistically weak.
- Post-publication decay: LRV (2008 WP) and KMPV (2013 WP) overlap with the crisis and low-rate era. I still found no systematic independent post-2013 carry performance study (searches for BIS/ECB/Bank of England work returned nothing relevant; a search snippet mentioned a student dissertation reporting Sharpe 0.49 over 1990-2020, not opened). The only post-2012 evidence I have is my own rough check, so decay remains [UNV] as a literature claim and "unproven, weakly suggested" from the OWN numbers.
- Commodity carry costs: Gorton-Rouwenhorst and Erb-Harvey are gross and end in 2004; neither addresses post-2008 financialization of commodity index flows (not read), so a net, post-2010 commodity carry Sharpe is still unknown.

### Own quick check [OWN]: FX carry on 9 USD crosses (caveated)
- Data: FRED daily spot (DEX series) sampled at month-end; 3-month interbank rates (OECD series on FRED, monthly averages). Euro-area and GBP rate series end January 2026, so the test stops at Dec 2025. Sample Feb 1999-Dec 2025 (323 months) so the euro exists.
- Construction: rank currencies at the end of month t-1 by rate minus USD rate; long top 3, short bottom 3, equal weight; excess return = spot change + rate differential/12 (assumes covered interest parity holds; post-2008 cross-currency basis deviations and forward points are ignored); costs 0, 2, 5 bp per side on weight changes; turnover is low (about 0.11 of notional a month). No financing, margin or EM currencies, no NDFs.
- Results: see the OWN row in the evidence table. Top-2/bottom-2 gives a similar Sharpe (0.44) with a deeper drawdown (-35%). The 2009-2019 window has positive skew (+0.24) and a worst month of -4.6%, the opposite of the pre-2008 crash profile, which shows how window-dependent the negative-skew story is.
- Limits: monthly-average rates versus month-end spot introduces timing noise; only G10; OECD rate series have changed definitions over time; nothing here tests KMPV's cross-asset diversification or commodity carry. I skipped commodity carry because futures curves were not obtainable quickly from free sources.
- Roll yield in commodities is mixed with spot-price expectations: carry is predictive in KMPV tests, but the historical sign of premia varies by commodity regime.

## 6. Failure regimes and risks

- Global risk-off: funding liquidity dries up, high-yield currencies collapse, safe-haven currencies (JPY, CHF) surge. Examples: 1998, 2008, 2015 CHF unpeg (event risk), March 2020, August 2024 [PC for 2015-2024 details; not read primary].
- Central bank pivots: sudden narrowing of rate differentials (BOJ July 2024 surprise reported as a catalyst).
- Low-vol complacency raising leverage, then violent reversal (negative skewness).
- Roll yield sign flips and inventory shocks in commodities; storage/financing costs.
- Capital controls, EM gaps, forward-market liquidity, NDF basis, prime-broker margin.
- Crowding: many alt-risk-premia funds hold the same carry factor.
- Parameter/definition risk: carry measured by forward discount ignores credit/convertibility risk.

## 7. MY TWIST (hypotheses, NOT backtested)

### Twist A: Vol-regime-conditioned carry (global FX-volatility throttle)
- Rationale: Menkhoff et al. tie carry returns to global FX volatility innovations; Brunnermeier et al. tie crashes to VIX and funding liquidity.
- Rule: scale positions by min(1, vol_target_ratio) and by a regime multiplier m_t = 0.5 if 1-month change in a global FX volatility index (average realized FX vol across G10, or implied vol such as a currency VIX) is above its 80th percentile of the past 5 years AND the carry portfolio's own 20-day return is negative; else 1.
- Parameters: percentile {70, 80, 90}; multiplier {0, 0.5}; lookback for vol change {5, 20, 60 days}.
- Expected effect: cuts left-tail months and lessens skew; reduces average return modestly; may whipsaw out of recoveries.
- Falsification: if the worst-month loss and max drawdown do not fall by at least a bootstrap-significant amount, or net Sharpe falls, over 1990-2025 (with parameters frozen from 1983-2005 data), reject.

### Twist B: Carry plus trend confirmation (don't hold carry against the price)
- Rationale: carry crashes begin with price reversals; a trend filter could exit before the worst of the move. Related to the practice of combining carry and momentum in macro funds [PC].
- Rule: hold currency carry positions only when the 3-month price trend of the currency vs USD agrees in sign with the carry position; otherwise halve it (do not reverse).
- Parameters: trend lookback {1, 3, 6, 12 months}; halve vs zero.
- Expected effect: lower drawdown, lower turnover than reversing; somewhat lower average carry.
- Falsification: no reduction in drawdown or no net-Sharpe improvement over plain carry across at least three disjoint 8-year windows.

### Twist C: Roll-yield carry with term-structure shape and inventory/vol filter in commodities
- Rationale: KMPV show commodity carry predicts returns but backwardation can be extreme and short-lived in spikes.
- Rule: rank 20-25 commodity futures on annualized basis between first and second contract; long top third, short bottom third; cap each position by volatility; exclude when 20-day realized vol is above its 90th percentile.
- Parameters: basis maturity pairs, tercile vs quintile, vol filter.
- Expected effect: smaller tails with similar average roll yield.
- Falsification: if the filter lowers net Sharpe in more than half of 5-year sub-periods vs unfiltered, reject.

## 8. Implementation spec

Data: spot and 1-month (or 3-month) forward rates with bid/ask (Reuters/WM/Bloomberg), overnight/OIS or deposit rates, NDF data for restricted currencies; futures curves for 20-30 commodities with first and second contract prices and open interest; global FX vol (realized from daily spot or implied vol); VIX/MOVE; margin requirements.

Signals: FX carry = (forward - spot)/spot annualized or interest rate differential; commodity carry = (F1/F2 - 1) annualized scaled by days between expiries. Rank within asset class.

Sizing: risk weight proportional to carry rank (demeaned), scaled so each leg targets equal volatility (inverse of 60-day vol); portfolio target vol 8-10%; cap single currency at 15% of risk; overall leverage cap.

Execution: month-end rebalancing using forwards or futures; roll FX forwards monthly; for small accounts use FX futures (CME) or spot with swap points; stagger trades across a few days.

Stops: no stops at position level (carry is a slow signal); use portfolio governor (see 10). 

Costs model: half bid-ask per trade per currency (G10 roughly 0.5-2 bps of notional per side, EM many times more; LRV reports spreads and turnover; use their conservative methodology and test 2x); swap/financing costs; futures commissions and slippage; margin carry.

```
monthly:
  for each ccy c: carry_c = fwd_discount(c)   # or rate differential
  rank, weight_c = (rank_c - mean_rank)/sum|rank - mean|
  scale each leg to equal vol (60d EWMA)
  m = regime_multiplier(global_fx_vol_change, carry_pnl_20d)   # Twist A
  target = weight * vol_scale * m
  trade to target at month-end forward fixing
```

## 9. Backtest plan

- Data period: 1983-2025 for FX; 1970s onward for commodity futures where data exist; keep post-2009 as a separate low-rate/zero-bound era.
- Walk-forward: parameters from 1983-2005, tested 2006-2025; then reverse (late train, early test).
- Multiple testing: record all signals/filters/vol percentiles tested; adjust with deflated Sharpe or Reality Check; a t-statistic threshold near 3 for any new overlay (Harvey-Liu-Zhu).
- Out-of-sample: emerging-market currencies and new contracts not used for tuning; cross-check with KMPV published returns.
- Stress tests: 1998, 2008, 2015 CHF, 2020, 2024 episodes; carry drawdown windows from KMPV as a bench.
- Metrics: net Sharpe with bootstrap CI, skew/kurtosis, max drawdown, 1st percentile monthly return, correlation to equity and to VIX changes, turnover, cost sensitivity 1x/2x/3x, contribution by currency, cross-asset correlation of carry drawdowns.
- Benchmarks: plain HML_FX, DBV-style index, KMPV global carry factor if data are available.

## 10. Risk management and kill-switch rules

- Portfolio vol target 8-10%; leverage cap; per-currency risk cap; no more than 40% of risk in one funding currency or one region.
- Drawdown rules: -8% reduce to half, -12% to flat for at least one month and re-enter only after volatility normalizes; treat the Twist A switch as a hypothesis, not a rule, until tested.
- Event risk: avoid unhedged exposure to pegged currencies (CHF 2015-style unpeg), and cap EM exposure with options hedges if available.
- Liquidity: stop adding positions if bid-ask widens above 3x normal; weekend gap policy.
- Kill switch: net-of-cost rolling 60-month Sharpe below -0.2 or any single-day loss above 4x model daily vol triggers a manual halt.

## 11. Annotated sources

| # | Source | URL | Type | Grade |
|---|---|---|---|---|
| 1 | Koijen, Moskowitz, Pedersen, Vrugt, Carry (NBER WP 19325) | https://www.nber.org/papers/w19325 (PDF: https://www.nber.org/system/files/working_papers/w19325/w19325.pdf) | WP/paper, read | A |
| 2 | Lustig, Roussanov, Verdelhan, Common Risk Factors in Currency Markets (RFS 2011) | https://dspace.mit.edu/bitstream/1721.1/66103/1/Verdelhan_Common%20Risk.pdf | Peer-reviewed, read (via Cochrane-hosted copy) | A |
| 3 | Menkhoff, Sarno, Schmeling, Schrimpf, Carry Trades and Global FX Volatility (JF 2012) | https://openaccess.city.ac.uk/id/eprint/3391/ | Peer-reviewed, abstract/summary only | A- (unread body) |
| 4 | Brunnermeier, Nagel, Pedersen, Carry Trades and Currency Crashes (NBER 14473) | https://www.nber.org/papers/w14473 | Peer-reviewed/WP, summary only | A- (unread body) |
| 5 | Moskowitz, Ooi, Pedersen 2012 (roll yield vs spot discussion) | https://fairmodel.econ.yale.edu/ec439/jpde.pdf | Peer-reviewed, partly read | A |
| 6 | Press/blog on August 2024 yen carry unwind (HDFC, RBC, CS Monitor, Envestnet) | https://www.envestnet.com/financial-intel/august-market-volatility-and-importance-yen | Practitioner/press, snippets only | C |
| 7 | Harvey, Liu, Zhu (NBER 20592) for testing hurdles | https://www.nber.org/papers/w20592 | WP, partly read | A |
| 8 | Gorton and Rouwenhorst, Facts and Fantasies about Commodity Futures (NBER WP 10595) | https://www.nber.org/system/files/working_papers/w10595/w10595.pdf | WP (published FAJ 2006), full text read | A- |
| 9 | Erb and Harvey, The Strategic and Tactical Value of Commodity Futures (FAJ 2006) | https://faculty.fuqua.duke.edu/~charvey/Research/Published_Papers/P91_The_strategic_and.pdf | Peer-reviewed, full text read | A- |
| 10 | Daniel, Hodrick, Lu, The Carry Trade: Risks and Drawdowns (NBER 20433; Critical Finance Review 2017) | https://www.nber.org/system/files/working_papers/w20433/w20433.pdf | WP/peer-reviewed, full text read (PDF saved by the fetch tool, text extracted locally) | A- |
| 11 | Bekaert and Panayotov, Good Carry, Bad Carry (NBER w25420) | https://www.nber.org/papers/w25420 | WP, abstract page only | B+ |
| 12 | NBER page for Koijen et al. (publication details) | https://www.nber.org/papers/w19325 | Landing page, opened | n/a (metadata only) |
| 13 | FRED daily FX (DEX series) and OECD 3-month interbank rate series; used for the OWN check | https://fred.stlouisfed.org/ (graph CSV endpoints) | Free data | data |

Sources were thinner here than for D1/D2. Second pass closed the commodity-carry gap (two full-text papers, both ending 2004) and added one independent FX paper to 2013. Still missing: any independent post-2013 carry performance study, a net-of-cost commodity carry study, central-bank (BIS/ECB/BoE) carry papers, and practitioner interviews; those gaps are flagged inline. I did not fetch Menkhoff et al. or Brunnermeier et al. bodies again, so they stay abstract-level.

## 12. Open questions

1. What is the net-of-cost, post-2012 Sharpe of FX carry and of the KMPV diversified factor, independent of the authors?
2. Does the cross-asset carry diversification benefit survive in drawdowns, given that all classes perform badly together in global recessions (KMPV)?
3. Can the vol-regime switches improve tails out-of-sample or are they data-snooped to 2008?
4. How much of commodity carry is compensation for inventory/hedging risk versus a pure forecast of spot price?
5. Does ZLB/negative-rate history (2009-2021) bias the FX carry estimates downward?
6. How do FX futures vs forwards vs spot-plus-swap compare in realized carry after financing and margin?
7. (Second pass) Is the 0.19-0.28 gross Sharpe my rough check shows for 2012-2025 a real decay or noise (t about 1)? A proper test needs real forward points, more currencies and a decade of live ARP-fund returns, none of which I obtained.

## Second-pass changelog (2026-10-07)

- Read in full text: Gorton-Rouwenhorst, Erb-Harvey, Daniel-Hodrick-Lu; opened NBER landing pages for Koijen et al. and Bekaert-Panayotov (abstract only). Not obtained: Koijen et al. update beyond the JFE metadata, an independent post-2013 carry study, any BIS/ECB/BoE carry paper, Menkhoff and Brunnermeier bodies.
- Resolved: KMPV publication details (JFE 2017 online, per NBER page); the commodity-carry [UNV] (now two primary papers; basis-sorted high-low about 10% a year gross, Sharpe 0.76, 1959-2004; Erb-Harvey 91.6% of cross-sectional excess return explained by roll return, with the caution that individual-commodity averages were statistically insignificant and hedger-insurance theory is not confirmed).
- Downgraded: the "headline Sharpe 0.7-1.1" (KMPV) further, because DHL find dollar-neutral G10 carry at about 0.5 (se 0.19) and the 0.78 dollar-based figure includes a dollar bet; my [OWN] check gives 0.43 gross over 1999-2025 and 0.19-0.28 in 2012-2025. Net-of-cost FX carry Sharpe stays about 0.4-0.5 (LRV 0.50 net of spreads to 2009; OWN 0.42 with 2 bp), not above.
- Upgraded: commodity carry from "[UNV]" to B/A- evidence for the existence of a basis-sorting premium to 2004; no upgrade for post-2004 persistence.
- Twists A, B, C remain hypotheses, NOT backtested; the OWN check includes no regime filters. Observation relevant to Twist A: the 2009-2019 window had positive skew and a worst month of -4.6%, so a crash-throttle would have had little to do in that window and its value rests on a handful of events (1998, 2008, 2020, 2024).
- Remaining [UNV]: post-publication decay as a literature fact; the Aug 2024 yen-carry causal narrative (press only).
