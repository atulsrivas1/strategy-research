# C4. Crypto Funding-Rate and Basis Carry: perpetual funding arbitrage and cash-and-carry

Status: research dossier, not investment advice. Section 7 variants are hypotheses I have NOT backtested. Prepared 2026-10-07; second pass 2026-10-07 (see section 13 changelog). Items marked [OWN-DATA] are simple statistics I recomputed from public no-key APIs; they are descriptive, not backtests.

Evidence key: [PR] peer-reviewed journal; [WP] working paper/preprint; [PRAC] practitioner, vendor, exchange or consultancy material; [SEC] secondary summary I could not check against the primary text; [OWN] my own arithmetic or opinion.

---

## 1. Summary, horizon, asset class, holding period

Crypto carry harvests the gap between futures and spot prices in digital assets by being long spot and short a derivative: either a perpetual swap (earning the periodic funding payment when the perp trades above spot) or a dated future (earning the basis as it converges at expiry). The position is delta-neutral by construction: price risk cancels, leaving funding or basis, minus fees, financing and margin costs. Asset class: BTC, ETH and large altcoins on centralised exchanges (Binance, Bybit, OKX, others), DeFi perp venues (for example Hyperliquid), and CME futures plus spot ETFs for the regulated version. Holding period: days to months for perp carry (funding is typically paid every 8 hours), until expiry (1-3 months) for dated futures. The edge is a leveraged-demand premium paid by long speculators. The crucial feature: it looks like arbitrage in the data (very high Sharpe ratios) but is exposed to venue failure, margin liquidation and funding regime flips, none of which show up in ordinary Sharpe estimates.

## 2. Origin and who uses it

- Mechanism origin: the perpetual swap was introduced by BitMEX (creation noted in Christin et al.) with an 8-hour funding mechanism to tie the perp to spot. Cash-and-carry on dated futures is the classical commodity/financial futures basis trade.
- Academic literature: Schmeling, Schrimpf and Todorov, "Crypto carry" (BIS Working Paper 1087, first April 2023, revised October 2025; also Management Science reference list) [WP/PR]. Christin, Routledge, Soska and Zetlin-Jones, "The Crypto Carry Trade" (CMU working paper, August 2022) [WP; read]. He, Manela, Ross and von Wachter, "Fundamentals of Perpetual Futures" (arXiv 2212.06888, versions through August 2024) [WP; read]. Ackerer, Hugonnier and Jermann, "Perpetual Futures Pricing" (NBER w32936; Mathematical Finance) [WP/PR; theory; read the arXiv version header]. Borri, Liu, Tsyvinski and Wu, "Cryptocurrency as an Investable Asset Class: Coming of Age" (arXiv 2510.14435, v4 March 2026) [WP; read the carry section]. Cong, Li, Tang and Yang on crypto wash trading (Management Science) [PR]. Gornall, Rinaldi and Xiao on perpetual futures and stability (preliminary, 2025) [WP; abstract via search].
- Practitioners/users: market makers and arbitrage desks; hedge funds (Alameda Research and Three Arrows Capital are named in He et al. as having been in this activity, then moving to directional bets from late 2021 to early 2022 per news reports they cite); institutions using CME futures with spot ETFs (CF Benchmarks describes this structure) [PRAC]; yield products such as Ethena's USDe (delta-neutral staked ETH plus short ETH perps) [PRAC]. I could not verify individual trader claims beyond these.

## 3. Economic rationale and who is on the other side

BIS (Schmeling, Schrimpf, Todorov, WP 1087; full text of the 1 October 2025 version now read via an archive.org copy of the BIS PDF): carry on dated BTC and ETH futures (futures minus spot) averaged roughly 7 percent a year across exchanges from April 2019 to July 2024 (about 8 percent one-month on OKEx and 6.4 percent on CME; mean basis about 7.5 percent in the event-study sample), with peaks above 40 percent in the current abstract. Correction to the first pass: the BIS web page I used earlier still showed an older abstract ("averaging above 10 percent", "up to 60 percent"); the October 2025 PDF says about 7 percent and "sometimes exceeding 40 percent". Use the lower figures. Roughly 10 times the S&P 500 carry and more than 12 times the Treasury carry over February 2018 to July 2024. It is explained mainly by a volatile "inconvenience yield" on spot (interest rates explain very little), attributed to two forces: small, trend-chasing leveraged investors, and limited arbitrage capital because cash-and-carry is exposed to margin spikes and liquidations (no cross-margining between spot and futures venues). Carry is right-skewed, which the authors note implies a high risk of large drawdowns for the short-futures leg. A 10 percent rise in standardised carry predicts a 22 percent increase in short-futures liquidations (as a share of open interest) over the next month. The January 2024 spot BTC ETF launch lowered basis by about 3 percentage points on all exchanges and a further 5 points on CME (36 percent and 97 percent of the mean basis, difference-in-differences). The paper studies dated futures, not perpetuals; it has no strategy Sharpe table and says bid-ask and exchange fees are too small to explain carry, with no tradable net-of-cost backtest [WP; full text read]. Crash-predictability regressions exist in the paper but I did not extract coefficients. Christin et al. say the same economics in different words: the carry is the long side's willingness to pay for leverage; Binance cut maximum leverage from 125x to 50x in July 2021 and carry returns dropped; Tether-margined versus coin-margined contract differences line up with who wants levered longs versus shorts [WP; read]. He et al. show deviations from their no-arbitrage benchmark have a mean absolute size of about 60 to 90 percent a year, decline about 11 percent per year as arbitrage capital grows, and comove across coins, suggesting common funding/liquidity constraints [WP; read].

Who is on the other side: leveraged retail and directional funds long the perp. You are the supplier of leverage. When the crowd flips to net short (bear markets, crises), funding turns negative and the carry trade turns into a payer.

Why the edge persists (or not): limits to arbitrage (capital, margin, counterparty exposure, jurisdiction), and the gap between exchange-specific margining and holding the spot leg in custody. Why it decays: more arbitrage capital, ETF-enabled institutional basis trade, lower retail leverage. Evidence of decay is in section 5.

## 4. Canonical rules (implementable)

**A. Perpetual funding arbitrage**
1. Choose an asset with deep spot and perp liquidity (BTC, ETH, then top-10 by volume).
2. Position: buy X units of spot; short X units (equal USD notional) of the USDT- or USDC-margined perp on the same or another venue. Perp margin posted in stablecoins (or coin margin for coin-margined contracts, which adds beta to the collateral).
3. Funding (now checked against official documentation): Binance's support page gives F = average premium index P plus clamp(I minus P, -0.05%, +0.05%), with the interest rate I fixed by default at 0.03 percent per day (0.01 percent per 8 hours; 0 for ETHBTC), the premium index sampled every 5 seconds against impact bid/ask, a default 8-hour interval (00:00, 08:00, 16:00 UTC) that Binance may shorten to 4 or 1 hour in extreme conditions [PRAC; official page read]. Bybit's help centre describes the same structure (I = 0.03 percent per day, clamp 0.05 percent, plus a symbol-specific cap and floor tied to margin rates) [PRAC; via search-result summary of Bybit's page; the page itself timed out for me]. BitMEX's instrument endpoint for XBTUSD shows a funding rate of 0.0001 (0.01 percent) built from base, quote and premium symbols, 8-hour interval [PRAC; official API read]; I did not obtain BitMEX's prose contract guide. Practical consequence [OWN]: when the premium sits inside the band the funding rate equals the 0.01 percent interest component, which annualises to about 10.95 percent (0.0001 x 3 x 365). In my data about 46 percent of BitMEX XBTUSD 8-hour prints over the last two years are exactly 0.01 percent. So "funding of 8 to 11 percent" in calm markets is largely the exchange's built-in USD interest term, not a premium; the excess over T-bills is what you are actually paid for taking venue and margin risk. When funding is positive, longs pay shorts, so a short perp earns it.
4. Entry rule: enter when the trailing average annualised funding (for example 3-7 days) exceeds the cost hurdle H = (round-trip fees + expected slippage)/expected holding period + financing cost of spot capital + safety premium.
5. Exit: funding below hurdle for k periods, or funding negative, or basis dislocation > threshold, or venue risk trigger.
6. Rebalance: keep hedge ratio at 1.0 within a band of 0.5 to 1 percent; top up margin when perp margin ratio falls under the buffer.

**B. Dated-futures cash-and-carry**
1. Buy spot (or a spot ETF) and short the dated future of equal notional. Lock the basis at entry, hold to expiry, converge at settlement. CF Benchmarks's illustration: a USD 1,000 basis on a USD 100,000 position is about 12.2 percent annualised, and with leverage the net depends on funding cost [PRAC].
2. Annualised basis = (F/S - 1) x 365/days to expiry. Enter above an after-cost hurdle (financing + fees + margin carry); roll or close 1-2 weeks before expiry.

**C. Reverse carry**: when the perp trades at a persistent discount (negative funding), long perp and short spot (needs borrow); rarely stable and borrow is costly, so generally skip.

## 5. Evidence

| Claim | Source | Sample | Costs | Grade |
|---|---|---|---|---|
| BTC/ETH dated-futures carry about 7 percent a year on average (6.4 percent CME, about 8 percent OKEx, 1-month), peaks above 40 percent; right-skewed; high carry predicts short-futures liquidations (+22 percent of OI per +10 percent standardised carry) and crashes; spot ETF cut basis about 3 points (5 more on CME); arbitrage capital scarce. Supersedes the first-pass figures of "above 10 percent / up to 60 percent", which came from an older abstract | Schmeling, Schrimpf, Todorov, BIS WP 1087 (1 Oct 2025 version, full text) | Apr 2019 - Jul 2024 | Argues fees/spreads too small to explain carry; no net-of-cost strategy P&L | [WP] |
| [OWN-DATA] Hyperliquid BTC perp funding (hourly rates summed to days, annualised): mean 13.9 percent, median 10.95 percent, 5th percentile -6.8 percent, 95th 51 percent, 12 percent of days negative. By year: 2023 (from 12 May) 13.5, 2024 24.1, 2025 10.6, 2026 to 6 Oct 5.2 percent. Last 12 months mean 5.8 percent. ETH similar (last 12 months 6.4 percent). Funding-only compounding of a constantly short perp: about 14.9 percent a year, funding-curve max drawdown about 1 percent | Public Hyperliquid info API (no key) | 12 May 2023 - 6 Oct 2026 (1,244 days) | Funding only: excludes spot/perp basis P&L, fees (one 0.35 percent round trip would barely matter over 3.4 years), margin, spot financing, venue failure | [OWN-DATA]; venue is a DeFi perp, not Binance |
| [OWN-DATA] BitMEX XBTUSD (inverse perp) 8-hour funding summed to days: mean 4.5 percent, median 7.9 percent, 30 percent of days negative, 5th percentile -37.7 percent. By year: 2018 -7.9, 2019 6.8, 2020 6.9, 2021 15.4, 2022 -3.4, 2023 3.9, 2024 11.2, 2025 6.2, 2026 to 16 Sep 0.1 percent. March 2020 month mean -54 percent annualised (worst day about -411 percent annualised, i.e. roughly -1.1 percent in a day); November 2022 (FTX) month mean -18 percent; February-March 2021 +45 percent. Worst rolling 30-day mean -71 percent (ending April 2018) | Public BitMEX REST API (no key) | 1 Jan 2018 - 16 Sep 2026 (XBTUSD contract settled 16 Sep 2026) | Funding only; BitMEX is a single, older, lower-volume venue now; 2018 reflects a different funding design/market | [OWN-DATA] |
| [OWN-DATA] CME BTC front-month vs BTC-USD spot, crude annualised basis proxy (Yahoo continuous series, assumed last-Friday expiry, non-synchronous closes): median 4.9 (2021), -4.7 (2022), 6.1 (2023), 9.8 (2024), 5.0 (2025), 5.6 percent (2026 to date); last observation 3.9 percent; daily values swing by more than +/-100 percent on bad rolls/timing | Yahoo Finance | Jan 2021 - Oct 2026 | Very noisy; use medians only. Consistent with the 3 to 6 percent range in secondary sources, not a substitute for CME BasisWatch | [OWN-DATA], low quality |
| In-sample annual Sharpe 7 to 10 for short perp + long spot on Binance; BTC contracts 12.8 and 7.0 (Tether vs coin settled); carry largely decoupled from BTC trend; drop coincided with leverage cut 125x to 50x in July 2021 | Christin et al. 2022 | 11 Aug 2020 to 20 Jun 2022 (before FTX) | Funding and basis measured; transaction costs not the focus | [WP] |
| Random-maturity arbitrage strategy: BTC Sharpe 1.8 under high (retail-tier) Binance costs and up to 3.5 for market makers with no fees (6.7 for BTC with zero trading costs); better for ETH and altcoins; abnormal returns vs crypto factor models; mean absolute deviation from no-arbitrage price about 60 to 90 percent a year, shrinking about 11 percent a year; authors report a structural break from 2022 (smaller, less volatile deviations, strategy less active, lower returns) | He, Manela, Ross, von Wachter (arXiv v6, Aug 2024; numbers rechecked in full text) | BTC/ETH data from 2020-01-08 to 2024-03-11 (covers FTX) | Explicit Binance fee tiers | [WP] |
| Annualised Sharpe of crypto carry (short perp, long spot) 6.45 over 2020-2025; 4.06 from 2024; negative in 2025; funding mean about 8 percent with 0.8 percent volatility over the full sample | Borri, Liu, Tsyvinski, Wu v4 | 2020-2025 | As in the paper's Schmeling et al. construction; I did not check cost assumptions | [WP] |
| CME BTC annualised basis approached 25 percent (Feb 2024), above 20 percent (Nov 2024), briefly below zero (Mar 2025), near 10 percent by May 2025; momentum/sentiment correlations 0.50 and 0.54 with basis | CF Benchmarks | 2024-2025 | Educational; backtests on a single year | [PRAC] |
| CME basis compressed to roughly 3 to 6 percent by late 2025/2026 depending on measure; ETF outflows may reflect basis unwinds | Aggregator / CryptoSlate type reports | Late 2025 | Attribution is inference | [SEC] |
| Perpetuals now dominate volume (93 percent of crypto derivatives in a Cornell-reported study) and may reduce arbitrage drawdowns and improve stability | Cornell article; Gornall, Rinaldi, Xiao | 2025 | n/a | [WP/SEC] |
| Wash trading averages over 70 percent of reported volume on unregulated exchanges | Cong, Li, Tang, Yang | 29 exchanges | n/a | [PR] |

Critical assessment:
- The headline Sharpe ratios (7 to 10, 12.8, 6.45) are not credible as forward estimates. They are computed on a basis series whose daily volatility is tiny, over short samples with a single large venue failure absent (Christin ends June 2022, before FTX) or treated as a data feature. A Sharpe ratio is the wrong risk measure for a strategy whose main risk is a discrete counterparty event.
- He et al. show the sensible version: under realistic, retail-tier fee levels, the Sharpe falls to about 1.8 for BTC, and deviations decline about 11 percent a year. Borri et al. show the decay to negative in 2025. The trade was most lucrative when retail leverage was highest and arbitrage capital scarce; both have eased.
- Own-data check of the "Sharpe 7 to 10" headline [OWN-DATA]: a funding-only curve for BTC on Hyperliquid has a naive daily-return Sharpe of about 14 (not subtracting cash) and a 1 percent maximum drawdown over 3.4 years, which illustrates exactly why Sharpe is the wrong yardstick: the curve contains no venue event and no basis P&L. The informative numbers are the tails of the funding series (negative-funding episodes of -54 percent annualised in March 2020 on BitMEX, -18 percent in the FTX month) and the downtrend in average funding to about 5 to 6 percent over the last 12 months on Hyperliquid, which is roughly where US T-bills sit, i.e. little or no excess carry for the perp leg in the latest year (T-bill level not downloaded; check).
- Binance and Bybit public APIs returned a restricted-location block from this machine, so my funding statistics use Hyperliquid (DeFi) and BitMEX (legacy) rather than the venues most carry traders use. I did not attempt to circumvent the block. Treat the figures as indicative of the asset-level funding regime, not of Binance execution.
- CME basis: institutions have commoditised the regulated version (spot ETF plus short CME future). Compression to the mid-single digits by late 2025, in secondary sources, means after financing costs the trade is close to a Treasury-bill substitute with extra risk. I could not obtain CME's own BasisWatch series.
- Survivorship in yield products: Ethena-type designs advertise funding yield but their disclosed risks include negative funding, exchange counterparty exposure and a finite reserve fund [PRAC]. Figures for the reserve vary by source and date; unverified.

## 6. Failure regimes and risks, including tail and ruin analysis

1. **Exchange/counterparty failure (the dominant tail).** FTX (November 2022): the debtor-in-possession interim report states FTX commingled customer deposits and corporate funds from inception and that customers were owed about USD 8.7bn at petition, about USD 7bn of which had been recovered by the time of the second interim report [press report of a court filing; [SEC]]. He et al. document the FTX collapse in funding data: the BTC perp was priced far above spot at FTX but below spot on other exchanges as clients dumped FTX exposure, and funding turned negative on solvent exchanges [WP; read]. A carry trader with the short leg or the spot leg (or both) on FTX lost the leg on the failed venue while the other leg remained exposed to a falling market. If both legs were on FTX, nearly the whole position could be impaired subject to recovery; if the short perp collateral was lost but the spot was held in cold storage, the hedge disappears and you are simply long a falling asset.
2. **Margin/liquidation and ADL.** On October 10, 2025, reports put total crypto liquidations near USD 19 to 20 billion in about a day (estimates vary widely by tracker and window; one counter-count was about USD 9.9bn in 14 hours). FTI Consulting reports BTC top-of-book depth collapsed by more than 90 percent on key venues and spreads widened from single-digit basis points to double-digit percentages at extremes; USDe traded in the mid-60-cent range on Binance at the worst point while staying much closer to par on other venues, which FTI attributes to venue-specific pricing feeding margin engines [PRAC consultancy; read]. BitMEX argues auto-deleveraging closed delta-neutral hedges while spot fell, forcing market makers to withdraw [claim from an exchange with commercial interest; via search summary, [SEC]]. Lesson: even a "hedged" book can be broken when the exchange socialises losses by closing profitable shorts. [OWN-DATA] Funding itself did not signal this: Hyperliquid BTC funding averaged about 9.5 percent annualised over 10 to 12 October 2025 and about 10.7 percent for the month, and BitMEX XBTUSD about 6.5 percent for October, so a funding-sign kill switch would not have fired; the loss channel was margin, depth and venue-specific pricing. The liquidation and USDe figures remain press/consultancy/exchange-blog sourced (FTI read; BitMEX, trackers via summaries) and I did not obtain a primary exchange post-mortem.
3. **Funding flips.** Funding turns negative in crises (He et al. note March 2020 COVID liquidity episode and FTX). [OWN-DATA] On BitMEX XBTUSD the March 2020 monthly mean was about -54 percent annualised (worst single day about -1.1 percent of notional), November 2022 about -18 percent, and 30 percent of all days since 2018 were negative; on Hyperliquid BTC 12 percent of days since May 2023 were negative and the worst rolling 30-day mean was about -11 percent annualised (September 2023). The short side then pays. A position sized on trailing positive funding loses carry quickly; in a drawdown, margin top-ups are needed on the short if price rallies, but the spot sits elsewhere.
4. **Basis blowout and mark-to-market.** The perp or future can move against the hedge intraday due to dislocation; with leveraged cash, mark-to-market losses can force closure at the worst basis (He et al. stress that funding rate arbitrage is not risk-free even ignoring margin and costs because there is no fixed unwind date).
5. **Stablecoin and collateral risk:** USDT/USDC depeg; collateral haircuts; coin-margined contracts add beta.
6. **Operational:** API outages, withdrawal freezes, key custody, delisting, tax and regulatory change (jurisdiction risk for offshore venues).
7. **Fake volume / execution quality:** Cong et al. show widespread wash trading on unregulated exchanges, so quoted liquidity and volume may overstate real depth.

**Ruin illustration [OWN, assumed numbers].** Suppose capital C is split half into spot (held at a venue or custodian) and half into perp margin, with the short perp matching the spot notional (so the perp runs at 1x on its own margin; book-level leverage is 1x). Case A: venue holding both legs fails: loss = 100 percent of C minus recovery (FTX recoveries are claim-based and slow). Case B: spot in cold storage, perp venue fails: you lose the margin (50 percent of C in this example) plus you are unhedged; a further -30 percent price drop costs 30 percent of the spot half = 15 percent of C, total about 65 percent. Case C: a +40 percent squeeze in hours with insufficient margin top-up speed: the short perp liquidates; you keep spot gains but lose the hedge, and if price then reverses -40 percent you give back the gain. Annual carry of 8 to 10 percent therefore needs about a decade of uninterrupted harvest to compensate for a single Case B event; even the "good" BIS-average figure of 10 percent is not safe at 50 percent single-venue concentration. Cross-venue split and strict margin buffers are survival tools.

## 7. MY TWIST (hypotheses, not backtested)

**Twist 1: Venue-risk-capped, regime-gated carry.**
- Rationale: the dominant risk is a discrete venue event, not volatility; diversify venue exposure and exit before negative-funding regimes. Second-pass caution: because default funding already embeds about 10.95 percent a year of interest term (section 4), an entry hurdle H below that level (6 to 10 percent) would be met mechanically in quiet markets; define H as funding minus the stablecoin/T-bill financing rate, and test excess carry, not raw funding.
- Rule: allocate at most v percent of capital per venue; require at least 3 venues; hold spot with qualified custody, not on the perp exchange; enter only if trailing 7-day annualised funding > H and 30-day funding standard deviation < s; exit if 3-day funding < 0 or cross-venue funding spread > d (the He et al. FTX signature).
- Parameters: v in {20, 25, 33 percent}; H in {6, 8, 10 percent annualised}; s thresholds; d in {20, 40, 60 percent annualised spread}; perp leverage {1x, 2x, 3x}.
- Expected effect: lower net carry (venue split costs capital efficiency) but eliminates single-venue ruin; an earlier exit in negative regimes.
- Falsification: reject if, on the 2020-2026 sample including FTX and October 2025, the gated and venue-capped version has worst drawdown more than 10 percent, or if net return after realistic costs does not exceed 3-month T-bills plus 2 percent.

**Twist 2: Calendar rotation between perp funding and dated basis (including CME/ETF) with cost-aware switching.**
- Rationale: perp funding and dated basis co-move but diverge; capital should sit where the net carry is highest after costs, and regulated-venue basis lowers counterparty risk.
- Rule: each week compute net annualised carry for (a) perp funding (7-day average minus fee amortisation), (b) 1-3 month dated futures on offshore venues, (c) CME future vs spot ETF. Move capital if the best option beats the current one by more than a switching cost c.
- Parameters: switching cost c in {1, 2, 3 percent annualised}; rebalance weekly/monthly; min tenor for dated futures.
- Expected effect: smoother carry, more regulated exposure; may be dominated by compression in the regulated leg (CME basis near 3 to 6 percent in late 2025 per secondary sources).
- Falsification: reject if rotation net carry (after switching costs) is not above the best single static strategy by at least 1 point annualised, or the added turnover erodes it.

**Twist 3: Funding-volatility-aware sizing (anti-ADL).**
- Rationale: October 2025 ADL events hit hedged shorts; reduce leverage and shift hedge to venues/instruments that are less ADL-exposed when stress indicators rise.
- Rule: scale perp leverage with a stress score S combining (i) open interest / market cap, (ii) 7-day change in funding > x, (iii) orderbook depth drop > y percent, (iv) stablecoin peg deviation > 20 bps. When S crosses threshold, halve gross and move margin to excess buffers (at least 30 percent free margin) and consider closing both legs gradually.
- Parameters: thresholds x, y; leverage ladder; buffer 30 to 50 percent.
- Expected effect: some missed carry in melt-up phases; much smaller tail in cascades.
- Falsification: reject if, in historical stress episodes (Mar 2020, Nov 2022, Oct 2025), the stress score fails to flag at least 2 of the 3 before the main loss, or if false positives cost more carry than the avoided losses.

## 8. Implementation spec

**Data:** perp and spot prices, mark/index price, funding rate history and predicted funding (venue APIs; Kaiko, Amberdata, Coinglass as aggregators), orderbook depth, open interest, venue margin ratios, ADL queue indicators where exposed, stablecoin prices across venues, dated futures curves (CME and offshore), ETF NAV/premium, borrowing rates.

**Signals:** trailing funding mean and volatility, annualised basis, cross-venue funding spread, depth drop, OI/market cap, peg deviation, custody and withdrawal latency tests.

**Sizing:** notional per venue capped; perp margin buffer >= 30 to 50 percent free margin; max leverage on perp leg 2x for core; total hedged notional <= capital x L_max; spot leg in segregated custody/ETF.

**Execution:** enter via two-leg limit orders (post-only where possible) within a short window; leg risk managed by trading the less liquid leg first; unwind symmetrically; slippage cap.

**Stops:** structural (venue, margin ratio) rather than price stops; close if margin ratio < 150 percent of maintenance; unwind on risk triggers in section 10.

**Cost model:** per round trip = spot fee + perp fee + slippage on both legs, expressed in bp; for the example only, assume taker 10 bp spot + 5 bp perp each side = 30 bp round trip plus 5 bp slippage [assumed, unverified; actual Binance tiers are volume-dependent per He et al.]; breakeven holding period at 10 percent annualised funding (about 2.7 bp/day) is about 13 days [OWN]. Include financing cost of capital (T-bill or stablecoin yield), withdrawal/transfer fees, and funding timing (use the actual settlement timestamps).

**Pseudo-code:**
```
every 8h:
    for asset in universe:
        f7  = mean(funding[-21:]) * 3 * 365          # annualised
        fsd = std(funding[-90:]) * sqrt(3*365)
        spread = max_venue_funding - min_venue_funding
        stress = score(OI/mcap, dfunding, depth_drop, peg_dev)
        if open_pos(asset):
            if f3 < 0 or spread > d or stress > S_max or margin_ratio < m_min:
                unwind(asset)
        else:
            if f7 > H and fsd < s and venue_ok and stress < S_entry:
                size = min(cap_venue, cap_asset, risk_budget/maxloss_estimate)
                buy spot (custody/ETF), short perp (post-only)
    rebalance hedge ratio to 1.0 +- band; top up margin from reserve
```

## 9. Backtest plan

- Data: 2019/2020 to present, perp and spot at 1-minute or 8-hour (funding) frequency, by venue, with historical fee schedules; include FTX (Nov 2022), the mid-2022 3AC collapse (July 2022 per liquidator coverage), March 2020, the 2021 leverage-cut period, and Oct 2025 as named stress windows (Oct 2025 figures from FTI/BitMEX/trackers).
- Model venue failure explicitly: Monte Carlo of venue-default events with annual probability p (scenarios 0.5, 1, 2, 5 percent) and recovery rate R (0 to 70 percent); report net expected return and ruin probability per allocation rule. A simple historical backtest cannot price this.
- Walk-forward on thresholds (H, s, d); parameters frozen out of sample; final 18 months held out. Compare to a naive "always on" carry baseline.
- Multiple-testing: log all parameter variants; deflated Sharpe, but headline metrics should be drawdown, CVaR, ruin probability, and net carry vs T-bills, not Sharpe.
- Costs: grid of fee tiers (retail, mid, MM) as in He et al.; slippage grid; funding timing; include transfer costs.
- Pass criteria (pre-set): net carry >= T-bill + 3 percent after costs in the post-2023 subsample; worst drawdown <= 10 percent including venue-failure scenarios at p = 2 percent and R = 40 percent; stable performance across at least 3 of 4 calendar years.

## 10. Risk management and kill-switch rules

1. Venue caps: <= 25 percent of capital on any one offshore venue; unregulated venues combined <= 50 percent; prefer venues with segregated custody and proof-of-reserves (verify independently).
2. Spot leg in qualified custody or regulated ETF, never left idle on the perp exchange.
3. Margin: maintain free margin >= 30 to 50 percent of perp notional; pre-funded stablecoin reserve; auto top-up rules; never rely on moving spot in a crisis.
4. Funding kill: exit if 3-day average funding < 0 or if realised 7-day carry drops below the hurdle; cross-venue funding spread > d triggers de-risking.
5. Stress kill: halve gross when stress score crosses threshold; flat when two of four stress indicators breach (depth drop > 70 percent, peg deviation > 100 bps, OI/mcap at 1-year high with funding spike, exchange withdrawal delays).
6. Counterparty watch: withdrawal latency tests weekly; monitor news and on-chain flows to exchanges; exit on delays > 24 hours or reserve-attestation failure.
7. Stablecoin: diversify USDT/USDC; cap single-stablecoin share at 50 percent; exit on 50 bps depeg.
8. Operational: duplicate API keys, kill-switch script, daily reconciliation of positions across venues and ledgers.
9. Position sizing never allows a Case B event (section 6) to exceed 20 percent of capital.

## 11. Annotated sources

| # | Source | URL | Type | Grade | Note |
|---|---|---|---|---|---|
| 1 | Schmeling, Schrimpf, Todorov, Crypto carry (BIS WP 1087), 1 Oct 2025 version | https://www.bis.org/publ/work1087.htm (abstract page, older abstract text); full text read from an archive.org copy of https://www.bis.org/publ/work1087.pdf (direct curl returned HTML) | WP (full text read) | A- | Main academic carry paper; dated futures only; corrects first-pass 10/60 percent to about 7/40+ percent |
| 2 | Christin, Routledge, Soska, Zetlin-Jones, The Crypto Carry Trade | https://www.andrew.cmu.edu/user/azj/files/CarryTrade.v1.0.pdf | WP (read) | B+ | Sharpe 7-10 in-sample, pre-FTX, Binance |
| 3 | He, Manela, Ross, von Wachter, Fundamentals of Perpetual Futures | https://arxiv.org/pdf/2212.06888v6 | WP (read) | A- | Costs-explicit; covers FTX; strategy Sharpe 1.8 retail fees |
| 4 | Ackerer, Hugonnier, Jermann, Perpetual Futures Pricing | https://arxiv.org/pdf/2310.11771v2 | WP/PR theory | A | No-arbitrage pricing; differs from traded designs |
| 5 | Borri, Liu, Tsyvinski, Wu, Cryptocurrency as an Investable Asset Class: Coming of Age | https://arxiv.org/pdf/2510.14435 | WP (read section) | B+ | Carry Sharpe decay to negative in 2025 |
| 6 | Cong, Li, Tang, Yang, Crypto Wash Trading (Management Science) | https://pubsonline.informs.org/doi/10.1287/mnsc.2021.02709 | PR (abstract via search) | A | Volume integrity |
| 7 | Gornall, Rinaldi, Xiao, perpetual futures and stability (prelim.) | https://afajof.org/management/viewp.php?n=169764 | WP (fetch failed; via search summary) | C+ | Verify |
| 8 | CF Benchmarks, Revisiting the Bitcoin Basis | https://www.cfbenchmarks.com/blog/revisiting-the-bitcoin-basis-how-momentum-sentiment-impact-the-structural-drivers-of-basis-activity | Index provider (read) | B- | Basis levels 2024-2025; vendor interest |
| 9 | FTI Consulting, The Crypto Crash of October 2025 | https://fticonsulting.com/insights/articles/crypto-crash-october-2025-leverage-met-liquidity | Consultancy (read) | B- | Liquidation, depth, USDe figures |
| 10 | BitMEX, State of Crypto Perps 2025 | https://www.bitmex.com/blog/state-of-crypto-perps-2025 | Exchange blog (fetch 404 at the URL I tried; via search summary) | C | ADL claims; conflict of interest |
| 11 | Ethena docs (underlying derivatives) | https://docs.ethena.fi/protocol-overview/underlying-derivatives.md | Protocol docs (read) | C+ | Hedging design; risks not detailed |
| 12 | Press coverage of FTX debtor interim report | https://www.theblock.co/amp/post/236507/latest-ftx-bankruptcy-report-provides-lurid-details-into-alleged-fraud | Press | C+ | Commingling statements; not the filing itself |
| 13 | 3AC liquidator claims coverage | https://decrypt.co/146542/three-arrows-capital-liquidators-demand-1-3b-from-bankrupt-vc-funds-co-founders | Press | C | Allegations only |
| 14 | Amberdata on Oct 2025 deleveraging | https://blog.amberdata.io/leverage-liquidations-the-31b-deleveraging | Data vendor | C+ | Via search; numbers differ from other trackers |
| 15 | Binance, Introduction to Binance Futures Funding Rates | https://www.binance.com/en/support/faq/introduction-to-binance-futures-funding-rates-360033525031 | Exchange docs (read) | B+ | Official formula, 0.01% per 8h interest term, clamp, interval changes |
| 16 | Bybit help centre, funding rate | https://www.bybit.com/en/help-center/article/What-is-funding-rate-and-predicted-rate | Exchange docs (page timed out; content via search summary) | B- | Same structure; verify page |
| 17 | BitMEX instrument API (XBTUSD) and funding API | https://www.bitmex.com/api/v1/instrument?symbol=XBTUSD ; https://www.bitmex.com/api/v1/funding | Exchange API (read) | B+ | Funding parameters and 2018-2026 history; contract settled 16 Sep 2026 |
| 18 | Hyperliquid info API (fundingHistory) | https://api.hyperliquid.xyz/info | Exchange API (read) | B | Hourly funding BTC/ETH from May 2023 |
| 19 | Yahoo Finance BTC=F and BTC-USD (via yfinance) | https://finance.yahoo.com/ | Aggregator (read) | C | Crude CME basis proxy only |
| 20 | Binance and Bybit public market-data APIs (attempted) | https://fapi.binance.com ; https://api.bybit.com | Exchange API | n/a | Returned location-restricted errors; not used |

## 12. Open questions

1. What are the real, audited returns of institutional carry books (net of fees, financing, collateral haircuts) in 2023-2026? No source gives this.
2. How large is the true annual probability of a venue-level loss event for the top 10 venues, and what is the recovery distribution? FTX is one data point; Terra/Celsius/3AC affected lenders and funds more than exchanges.
3. Do ADL mechanics differ enough across venues (and DeFi perps) to rank venues by hedge reliability? BitMEX's account is self-interested; I found no neutral post-mortem.
4. Is the post-2024 carry decay (Borri et al.) cyclical (bear/chop) or structural (ETF-driven institutionalisation)?
5. Does CME basis relative to T-bills (3 to 6 percent late 2025 per secondary sources) leave any after-cost premium for the regulated version?
6. BIS WP 1087 full text is now read (resolved), but I did not extract the crash-predictability coefficients or the margin-friction tables in detail; and the paper has no strategy Sharpe or net-of-cost P&L, so the question "what does a margin-aware, cost-aware cash-and-carry earn" is still open.
7. Gornall et al. and the Cornell perp-halt study: unread beyond abstracts.
8. Is the post-2024 decline in average perp funding (Hyperliquid last 12 months about 5.8 percent, BitMEX 2026 about 0 percent) a venue artefact or the same ETF/institutional compression BIS documents for dated futures? Binance/Bybit data, which I could not reach, would settle it.

## 13. Second-pass changelog (2026-10-07)

- Read BIS WP 1087 (1 Oct 2025 version) full text through an archive.org copy. Corrected the headline: average carry about 7 percent (not "above 10"), peaks above 40 percent (not 60); added ETF difference-in-differences (-3 points, -5 more on CME), the liquidation regression (+22 percent of OI per +10 percent standardised carry), and that the paper covers dated futures and reports no strategy Sharpe or costed P&L. Source grade stays A- (WP, full text now read).
- Funding formula: replaced the secondary-source formula by Binance's official page (P plus clamp(I minus P, +/-0.05%), I = 0.01% per 8h, interval can drop to 4h or 1h). Bybit confirmed only via search summary; BitMEX via its API. Added the implication that default funding embeds about 10.95 percent annualised interest, and rewrote the Twist 1 hurdle caution accordingly (Twist stays UNTESTED).
- Added [OWN-DATA] funding statistics from Hyperliquid (May 2023 - Oct 2026) and BitMEX XBTUSD (2018 - Sep 2026), including March 2020, FTX month and October 2025, and a crude CME basis proxy. Binance/Bybit APIs were location-blocked and not circumvented. All own-data statistics are funding-only, descriptive, not backtests, and exclude fees, margin, venue failure.
- Rechecked He et al. (v6): 1.8 / 3.5 / 6.7 Sharpe levels, 11 percent a year decay and 60 to 90 percent mean absolute deviation confirmed; added the 2022 structural-break remark.
- Exchange failure and liquidation figures (FTX, October 2025, USDe) remain press/consultancy/exchange-blog sourced; unchanged grade B- to C. No neutral post-mortem found.
- Not done: Schmeling et al. crash coefficients, Borri et al. cost assumptions, Gornall et al., Christin re-read (first-pass reading stands).
- Overall grade of the strategy as a retail-implementable edge: downgraded one notch in confidence (decay evidence from BIS ETF event study, He et al. break, and own funding data showing about 5 to 6 percent latest-12-month funding on the venues I could reach).
