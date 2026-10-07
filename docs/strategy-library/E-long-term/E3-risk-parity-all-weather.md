# E3. Risk Parity / All Weather

Status: research dossier, not investment advice. Twists in section 7 are untested hypotheses. Dated 2026-10-07.

Source-access note (updated by second pass, 2026-10-07): the second pass read in full Bridgewater's "The All Weather Story" (January 2012 PDF), Bridgewater's "The All Weather Strategy" (4Q09 paper, via a pension-board copy), and Asness-Frazzini-Pedersen "Leverage Aversion and Risk Parity" (AQR-hosted FAJ version, Table 2). Year-by-year Bridgewater returns are NOT in any Bridgewater document I could open; the 2020 and 2022 figures below come from press reports (Institutional Investor, Fortune), and 2019 is still unresolved. Other items remain abstract or secondary-level as graded in section 11. See the "Second-pass changelog" at the end.

## 1. Summary, horizon, asset class, holding period

A multi-asset portfolio (equities, nominal government bonds, inflation-linked bonds, commodities/gold) weighted so each asset class or economic-regime bucket contributes roughly equal risk, then levered so the total portfolio hits a target volatility (commonly 10% in the commercial products I saw referenced, e.g., HFR and PanAgora 10%-vol labels). Horizon: strategic, multi-year to decades; rebalance monthly to quarterly, with volatility estimates updated at least monthly. Asset class: global multi-asset via futures and liquid ETFs. Typical holding: continuous; asset-class positions are permanent, only weights change.

## 2. Origin and who uses it

- Bridgewater, All Weather (launched 1996 per Bridgewater's own "All Weather Story", Jan 2012, read in full; originally for Ray Dalio's trust assets, never conceived as a product; the Story says a consultant adopted the label "Risk Parity", which sits alongside PanAgora's claim that Qian coined it, so credit for the term is disputed). The design splits environments into four by growth and inflation rising or falling and balances risk across them. The popular "55% bonds / 30% stocks / 15% gold and commodities" mix is a simplified Dalio-interview allocation, not Bridgewater's institutional portfolio. The strategy is regarded as the foundation of risk parity.
- Edward Qian (PanAgora), "On the Financial Interpretation of Risk Contribution: Risk Budgets Do Add Up" (Journal of Investment Management 4(4), 2006): gave risk contribution a financial meaning as expected contribution to loss, and PanAgora's bio credits him with coining the term "risk parity". PanAgora launched risk parity portfolios in the early 2000s (per their own bio). Du Plooy (2019) tested the result with fat tails.
- Asness, Frazzini, Pedersen, "Leverage Aversion and Risk Parity" (FAJ 68(1), 2012): AQR principals; AQR sells risk parity funds.
- Critics and sceptics: Anderson, Bianchi, Goldberg (FAJ Nov/Dec 2012) "Will My Risk Parity Strategy Outperform?"; Inker (GMO, 2010) cited as the case against; follow-up exchanges 2013-2014.
- Recent: State Street and Bridgewater launched an All Weather ETF (ticker ALLW) in 2025 with a gross expense ratio of 0.85% and inception 5 March 2025 (State Street product page, opened 2026-10-07; net ratio not stated). Leverage: the issuer page states no target; its listed exposures as of 6 Oct 2026 (global nominal bonds 69.18%, global equities 43.55%, inflation-linked bonds 40.98%, commodities 32.62%) sum to about 186% of NAV by my addition, consistent with the earlier "approximately 1.8x" claim, which is therefore a holdings snapshot, not a stated target. Issuer-reported performance to 30 Sep 2026: NAV return 7.63% over one year and 12.08% since inception, versus 16.61% and 21.24% for MSCI ACWI IMI. RPAR is another risk parity ETF.

## 3. Economic rationale and who is on the other side

Core logic: a 60/40-style portfolio holds roughly 90% of its risk in equities (verified as Bridgewater's own claim: the 4Q09 paper says equities contribute about 90% of risk for a conventional portfolio with about 60% in equities, and elsewhere in the same paper about 80% for a 60%-equity fund and more than 75% for typical institutions; the 2012 Story says "almost all of its risk"; promotional, not independent), so it is an equity bet. If bonds and commodities have comparable Sharpe ratios to equities and low correlation, equalizing risk and levering the diversified mix raises Sharpe and return per unit of risk.

Leverage-aversion explanation (AFP 2012): investors who cannot or will not use leverage overpay for high-risk assets to hit return targets, so safer assets have higher risk-adjusted returns; risk parity buys the cheap safe assets and uses leverage. AQR's figures, now confirmed against the paper (Table 2, panel A, US stocks and bonds, January 1926 to 2010, excess returns over T-bills): unlevered risk parity excess return 2.20% (volatility 4.25%, Sharpe 0.52), value-weighted market portfolio 3.84% (volatility 15.08%, Sharpe 0.25), 60/40 4.65% (Sharpe 0.40), and levered risk parity 7.99% when scaled to the market's realized volatility of 15.08%, with a Sharpe ratio of 0.53. The paper's broad sample (global stocks, bonds, credit, commodities, 1973-2010): levered risk parity 6.15% excess return vs 4.31% for the value-weighted portfolio (volatility 10.10%), unlevered 3.39%, Sharpe 0.62 unlevered vs 0.43 for the market. Weights are inverse volatility from three-year monthly returns. The note on the "2.20 / 3.84 / 7.99" figures from the FA Magazine summary was correct. Authors are AQR principals.

Other side: the same leverage-constrained investors (pensions, endowments, retail), who overweight equities; central banks and liability-driven investors who hold bonds for non-return reasons.

Critical points: (1) The edge depends heavily on the multi-decade fall in yields and on the negative stock-bond correlation during the 1998-2021 period (my characterization; the 2022 evidence in section 5 supports the dependence). (2) Anderson-Bianchi-Goldberg show outcome depends on sample dates and on financing/transaction costs; in 1946-1982 value-weighted and 60/40 beat risk parity in their data. (3) AQR/Asness argue that risk parity is levering a whole diversified portfolio, not a "levered bond bet", but concede leverage must be applied with care ("Yes, Lever, But With Care", 2015).

## 4. Canonical rules

Naive risk parity (inverse volatility):
1. Asset sleeves: global equities, nominal Treasuries (or global government bonds), inflation-linked bonds, commodities/gold (All Weather's four-regime mapping, per the 2012 Story, 25% of risk per box: rising growth = equities, commodities, corporate credit, EM credit; falling growth = nominal bonds, inflation-linked bonds; rising inflation = inflation-linked bonds, commodities, EM credit; falling inflation = equities, nominal bonds. So the real Bridgewater mapping also uses credit, which this simplified four-sleeve version omits).
2. Estimate volatilities (and optionally correlations) from trailing 1-3 years of daily/weekly returns.
3. Weight w_i proportional to 1/sigma_i, normalized (equal risk contribution when correlations are equal). Full ERC: solve for w such that w_i * (Sigma w)_i is equal across i (Qian-style risk contributions).
4. Apply leverage L = target_vol / sigma_portfolio (e.g., target 10%).
5. Implement with futures (equity index, Treasury, commodity) and cash collateral; rebalance monthly or when weights drift by threshold.
Bridgewater's actual implementation details are proprietary; not verifiable.

## 5. Evidence

Peer-reviewed / academic:
- AFP (2012): evidence consistent with leverage aversion being one factor behind risk parity's performance; robustness across countries and asset classes; numbers above unconfirmed. Interested authors.
- Anderson, Bianchi, Goldberg (FAJ 2012): CRSP data Jan 1926 - Dec 2010; four strategies compared (value weighted, 60/40, unlevered and levered risk parity); levered RP had the highest cumulative return under frictionless assumptions, but not in every long subperiod, and 1946-1982 favoured value-weighted/60/40; realistic frictions can reverse the ordering. A published comment and author response followed.
- Qian (2006): theory of risk contribution, not performance evidence.

Practitioner and event evidence:
- March 2020 (ECB Financial Stability Review box): until mid-March low vol/correlation allowed risk parity investors to lever to about twice assets; vol and correlations spiked and, in the ECB's stylized model, selling worth about 225% of capital was needed to meet a vol target; ECB concluded such strategies probably amplified market moves but size is unquantifiable for lack of data. S&P reported all its risk parity index vol targets posted double-digit Q1 2020 losses. Institutional Investor: many managers cut leverage in March and missed the rebound.
- 2022: RPAR ETF about 32% below its November 2021 high in October 2022 (Bloomberg data via BNN); another snapshot had RPAR down about 28.5% YTD versus -23.95% for the S&P 500 and -20.85% for a 60/40 (date of snapshot unclear). CAIA analysis: the HFR Risk Parity 10% Vol index lost -19.5% versus -16.1% for global 60/40 in 2022, and AQR's Multi-Asset Fund -10.5%. All Weather's 2022 loss: -22% for the 10%-volatility version, according to Fortune (April 2024), which attributes it to slides Bridgewater presented to the Indiana Public Retirement System; I could not open the slides, so this is secondary. The "drawdown about 24%" claim was not found and stays unverified. Fortune also puts realized volatility since launch at about 10.7%.
- Bridgewater All Weather in 2019: still UNRESOLVED. No Bridgewater document or opened article gave the figure; first-pass sources conflicted (16-16.6% vs 18.2%) and I could not reopen them (CNBC returned 403, Institutional Investor 2019 content paywalled). A modeled series on MyPlanIQ shows about 12.2% for 2019 but it is not Bridgewater's fund. Do not use any 2019 number.
- Bridgewater All Weather in 2020: 9.47% for the 10%-vol version and 10.16% for the 12%-vol version, per Institutional Investor (opened; cites sources familiar with the firm, not a fund document), against 3.6% for the HFR risk parity 10% index, 11.5% for the S&P risk parity 10% index and 13.4% for PanAgora 10%. Secondary.
- Bridgewater's own long-run claim (4Q09 paper, read in full): since June 1996 inception about 8.4% annualized, about 11% volatility, Sharpe 0.43, gross of fees; the paper also shows hypothetical, simulated back-extension (1970-1996) with the standard simulated-performance disclaimer. A separate Bridgewater 2015 paper summarized by The Idea Farm claims All Weather beat a global 60/40 in 80% of rolling 20-year and 72% of rolling 10-year periods since 1925, which is simulated, not live.
- Expense/leverage: ALLW 0.85% gross expense ratio and about 186% of NAV in listed exposures (see section 2).

Takeaway: the long-sample (1926-2010) Sharpe advantage is real in frictionless backtests, depends on the era and on financing; the live record across two stress events (March 2020, 2022) shows leverage plus positively correlated stock/bond drawdowns is dangerous, and the fund-level outcomes diverged widely (AQR -10.5% vs index -19.5%), meaning construction details (commodity share, inflation-linked, trend overlays) dominated.

## 6. Failure regimes and risks

- Positive stock-bond correlation / inflation and rate shock (2022; also the 1946-1982 era per ABG).
- Volatility spikes with vol-targeting: forced de-leveraging at lows, then missed rebounds (2020).
- Financing: futures margin and repo costs rise when you most need leverage; Asness's own warning that wrong-form financing plus illiquid assets is the "death combination" applies.
- Estimation error in correlations during regime changes.
- Crowding / flows from vol-target funds (ECB: effect unquantifiable).
- Bond-heavy weighting concentrates in duration; real yields rising hurts both bonds and equities.
- Commodity roll yield and gold's lack of cash flow; limited diversification when everything is liquidated together.
- Fees: levered ETFs charge fees around 0.85% (if ALLW is representative) which eats a modest premium.

## 7. MY TWIST (hypotheses, NOT backtested)

Twist 1: Regime-aware correlation buffer (stock-bond correlation throttle).
- Rationale: the strategy's failure in 2022 was a correlation sign flip; leverage should shrink when the rolling stock-bond correlation turns positive.
- Rules: compute 126-day correlation between equity and 10Y Treasury futures returns; leverage multiplier m = 1.0 if corr < 0; m declines linearly to 0.6 as corr goes from 0 to +0.5; also cap bond-sleeve risk share at 35% when corr > 0.3.
- Parameters: window 63/126/252; slope; thresholds.
- Expected effect: less loss in 1970s-style/2022-style regimes, some cost in rebounds.
- Falsification: if over available history including 2022, the maximum drawdown does not fall by at least 15% relative and Sharpe worsens, discard. Needs long-run proxies (pre-2000 bond index data); results over the post-1998 sample alone are not enough.

Twist 2: Inflation-aware 4-bucket risk parity with explicit TIPS/commodity/gold buckets and a trend overlay.
- Rationale: the all-weather logic lacks an inflation sleeve large enough in 2022; AQR's multi-asset fund outcome (-10.5% vs -19.5% for the index) hints that construction matters, but I do not know its construction; I do not claim causation.
- Rules: buckets = {equity, nominal bonds, inflation-linked bonds, commodities+gold}; equal risk across the 4 buckets; per-asset 12-1 month time-series trend filter reduces the weight to 50% when asset trend is negative AND the asset's contribution to bucket is above target.
- Parameters: bucket risk shares (25/25/25/25 vs 30/30/20/20), trend lookback 6/9/12 months, filter strength 25-100%.
- Expected effect: shallower drawdowns in inflation/rate shocks; cost: whipsaw and trend lag.
- Falsification: if vs plain ERC the strategy fails to cut the worst 12-month loss by 20% or reduces long-run Sharpe by >0.1 net of costs in walk-forward testing, reject.

Twist 3: Financing-risk-first leverage cap.
- Rationale: leverage risk, not asset allocation, hurt in March 2020 (ECB).
- Rules: set maximum gross leverage so that a 3-sigma (using stressed vol = max(current, 2x median)) one-month loss stays under 40% of margin buffer; cap at 1.5x for retail-style accounts.
- Parameters: stress multiplier, margin buffer.
- Expected effect: lower returns in calm periods; no forced liquidation.
- Falsification: if the capped version underperforms the uncapped by more than the drawdown it avoids across historical stress windows (1987, 1994, 2008, 2013, 2020, 2022), the cap is too tight.

## 8. Implementation spec

Data: daily futures or ETF total returns for S&P/global equity, 10Y and 30Y Treasury, TIPS, gold and broad commodities; T-bill rate; futures margin schedules; repo/financing rates.
Signals: rolling volatility (EWMA, half-life ~60 days or 1-year window); correlation matrix (shrunk toward constant correlation).
Sizing: ERC or inverse-vol weights, leverage to target vol 8-10%; cap leverage per section 10.
Execution: monthly rebalance with 20% relative drift tolerance; use futures for efficiency; roll rules; avoid trading at major data releases.
Stops: no asset stops; use portfolio vol/drawdown controls.
Costs: futures commissions and spreads of ~1bp-few bp per unit notional (illustrative; calibrate); financing = T-bill + spread; ETF fee; roll costs for commodities; slippage in stressed months 3-5x normal.

Pseudo-code:
```
monthly:
  r = returns[lookback]
  S = shrink(cov(r))
  w = solve_ERC(S) or 1/sigma
  L = target_vol / sqrt(w' S w)
  m = corr_throttle(stock_bond_corr) ; L = min(L*m, L_cap)
  target = L*w
  if max|target-current|/target > 0.2: trade
  mark margin; if margin_utilization>60%: reduce to 0.7*target
```

## 9. Backtest plan

- Data: back-extend with long-run proxies (US stocks since 1926, Treasuries since 1926, gold post-1970 convertible era, commodity indices since ~1970) to include 1946-1982; flag proxy quality.
- Splits: design on 1970-2009, walk-forward evaluation 2010-2025 including 2013, 2018, 2020, 2022; hold out 2022-2025 for the final check.
- Variants kept few; count all trials; Deflated Sharpe; paired block bootstrap versus 60/40 and versus unlevered inverse-vol.
- Frictions: model financing at T-bill + 50bp, futures costs, forced de-leveraging with 1-day lag; include realistic margin calls.
- Metrics: net CAGR, vol, Sharpe, max drawdown and recovery time, worst 12 months, correlation to 60/40 and to bonds, rolling stock-bond correlation sensitivity, risk contribution drift, leverage distribution, turnover, performance in rising-rate vs falling-rate regimes, 2020 and 2022 attribution.
- Compare with ABG's finding: ranking depends on sample and costs, so report results by decade.

## 10. Risk management and kill-switch rules

- Target vol 8-10% maximum; gross leverage cap (suggest 1.5-2.0x; pick via twist 3).
- Margin utilization limit 60%; automatic de-risking to 70% of target at 60%.
- Drawdown trigger: -15% from peak halves leverage until recovery to -7%; -25% triggers full review.
- Correlation trigger: stock-bond rolling correlation > +0.4 for 3 months -> cap leverage at 1.0x pending review.
- Counterparty/broker risk: multiple clearing brokers; avoid portfolio margin dependency on a single venue.
- Fee check: if all-in fees + financing exceed expected premium (in the backtest) -> do not run.
- Abandon criteria: twist falsifications above.

## 11. Annotated sources (A/B/C)

1. Bridgewater, The All Weather Story: https://www.bridgewater.com/resources/all-weather-story.pdf (also https://www.bridgewater.com/research-and-insights/the-all-weather-story) - B (primary but promotional; READ IN FULL in second pass: 9 pages, no performance numbers, gives launch year 1996 and the 25%-risk four-box mapping).
1b. Bridgewater, The All Weather Strategy 4Q09: https://sdcera.granicus.com/MetaViewer.php?view_id=4&clip_id=75&meta_id=9141 (pension-board copy; READ IN FULL) - B (promotional; gross of fees; contains simulated results).
1c. Fortune, 23 Apr 2024: https://fortune.com/2024/04/23/lackluster-returns-ray-dalio-investing-strategy-investors-pull-billions/ (opened; -22% in 2022 for 10%-vol All Weather) - B/C (press, slides not opened). Institutional Investor 2020 article (opened, URL in item 8): 9.47% / 10.16% for 2020 - B/C. State Street ALLW page: https://www.ssga.com/us/en/intermediary/etfs/state-street-bridgewater-all-weather-etf-allw (opened) - B.
2. Qian, JOIM 2006: https://www.panagora.com/assets/JOIM-On-the-Financial-Interpretation-of-Risk-Contribution.pdf ; https://joim.com/financial-interpretation-risk-contribution-risk-budgets-add - A (author at PanAgora).
3. Asness, Frazzini, Pedersen, Leverage Aversion and Risk Parity: https://www.aqr.com/-/media/AQR/Documents/Insights/Journal-Article/Leverage-Aversion-and-Risk-Parity.pdf ; https://rpc.cfainstitute.org/research/financial-analysts-journal/2012/leverage-aversion-and-risk-parity ; FA Magazine summary https://www.fa-mag.com/news/risk-parity-funds--a-look-at-their-complexity--structure-13463.html - A (AQR-hosted PDF READ IN FULL in second pass; Table 2 numbers confirmed) / C (FA Magazine secondary, no longer needed).
4. Anderson, Bianchi, Goldberg: https://cdar.berkeley.edu/sites/default/files/2012_Anderson-et-al.-WillRiskStrategyOutperfom.pdf ; comment https://research.cbs.dk/en/publications/will-my-risk-parity-strategy-outperform-a-comment/ - A.
5. Asness, "Risk Parity: Why We Lever": https://www.aqr.com/cliffs-perspective/risk-parity-why-we-fight-lever ; "Yes, Lever, But With Care": https://www.aqr.com/cliffs-perspective/yes-lever-but-with-care - B (interested party).
6. ECB FSR box on vol-targeting: https://www.ecb.europa.eu/pub/financial-stability/fsr/focus/2020/html/ecb.fsrbox202005_02~f6616db9be.en.html - A (central bank; stylized model).
7. S&P Q1 2020 risk parity indices: https://www.spglobal.com/en/research-insights/market-insights/q1-2020-performance-review-for-the-sp-risk-parity-indices - B.
8. Institutional Investor on risk parity 2020: https://www.institutionalinvestor.com/article/2bswpyzz05fjtwnke2qdc/portfolio/not-all-risk-parity-strategies-sucked-last-year - B.
9. BNN Bloomberg on RPAR 32% drop: https://ampvideo.bnnbloomberg.ca/risk-parity-strategy-disappoints-as-etf-posts-record-32-drop-1.1825008 ; ETFCentral https://www.etfcentral.com/news/risk-parity-etfs-effective-2022 ; CAIA https://caia.org/node/7312 - B/C (not read in full).
10. CNBC on Bridgewater March 2020: https://www.cnbc.com/2020/03/13/bridgewater-hedge-funds-post-mixed-results-amid-market-turmoil.html - B.
11. ALLW ETF coverage: https://www.etf.com/sections/features/bridgewaters-all-weather-etf-gains-traction-can-it-deliver ; https://www.tipranks.com/news/ray-dalios-bridgewater-will-launch-all-weather-etf-with-state-street-stt - B/C.
12. Dalio portfolio explainers: https://ofdollarsanddata.com/ray-dalio-all-weather-portfolio/ ; https://www.evidenceinvestor.com/post/the-all-weather-portfolio-explained - C (popular blogs, mixed accuracy).
13. Du Plooy (2019) on fat tails: https://repository.nwu.ac.za/items/ae350a38-4f37-46b0-84a8-b06394f360e1/full - B.

## 12. Open questions

- Why did AQR's multi-asset fund hold up better than the risk-parity index in 2022? (Construction unknown to me.)
- Does the long-run advantage survive realistic financing costs (ABG) when rates are not near zero?
- Is the stock-bond correlation regime predictable enough to use as a throttle without hindsight?
- How much of historical risk parity return is just the 40-year bond bull market?
- What are the verified numbers for All Weather in 2019, 2020 and 2022? (Second pass: 2020 = 9.47% / 10.16% and 2022 = -22% from press only; 2019 unresolved; Bridgewater or client-board disclosures are still needed, e.g. the INPRS slides behind the Fortune figure, which I could not locate.)
- Capacity and market-impact of vol-targeting flows (ECB: unquantifiable).

## Second-pass changelog (2026-10-07)

Method: Bridgewater PDFs and the AFP FAJ paper read in full via pdftotext; press articles and the issuer page opened via fetch (some returned HTTP 403: CNBC, etf.com, Alpha Architect). No free dataset exists for All Weather itself, so nothing was recomputed for this document.

CONFIRMED (primary, full text)
- AFP 1926-2010 US stocks/bonds: unlevered RP excess return 2.20%, market 3.84%, levered RP 7.99% (at 15.08% vol). Sharpe 0.52 unlevered, 0.25 market, 0.53 levered, 0.40 for 60/40 (60/40 excess return 4.65%).
- All Weather launched 1996, originally for Dalio's trust assets (Bridgewater Story, Jan 2012).
- Equities about 90% of risk in a conventional roughly 60% equity portfolio (Bridgewater 4Q09, promotional).
- ALLW: gross expense ratio 0.85%, inception 5 Mar 2025 (issuer page, 2026-10-07).

CHANGED
- ALLW "about 1.8x leverage": no stated target on the issuer page; listed exposures sum to about 186% of NAV (my addition, 6 Oct 2026 holdings), so the claim is reframed as a holdings snapshot.
- "Term risk parity": Bridgewater says a consultant adopted it; PanAgora credits Qian; flagged as disputed.
- Four-box mapping corrected to include credit (Story diagram); 25% of risk per box.
- 2020 All Weather return: was "unresolved", now 9.47% (10% vol) and 10.16% (12% vol) per Institutional Investor (secondary).
- 2022 All Weather: -22% (10% vol) per Fortune/INPRS slides (secondary); "drawdown about 24%" not found.
- Bridgewater long-run record added: about 8.4% a year, 11% vol, Sharpe 0.43 since 1996, gross of fees (4Q09 paper).

STILL UNVERIFIED
- 2019 All Weather return (16-16.6% vs 18.2% conflict unresolved; no number is endorsed).
- All Weather 2022 maximum drawdown (about 24%) and any net-of-fee figures.
- 2020 and 2022 figures lack a Bridgewater primary document.
- RPAR 2022 figures (-28.5% YTD snapshot, 32% drop, -22.8% calendar year in a different source), HFR/CAIA 2022 numbers, ECB and S&P 2020 numbers: not rechecked this pass.
- Anderson-Bianchi-Goldberg findings: the Berkeley PDF URL in section 11 was not downloadable in this pass (request failed), so still abstract/secondary.
- Whether the 1946-1982 reversal in ABG survives realistic costs.
