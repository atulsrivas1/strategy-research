# D1. Trend following: Turtles, Donchian breakouts, TSMOM and the CTA industry

Status: research dossier, not investment advice. Date of research: 2026-10-07. Evidence labels used throughout: [PR] peer-reviewed, [WP] working paper/white paper by credible researchers, [PC] practitioner claim or secondary summary, [UNV] unverified (I could not read a primary source). "TWIST" items are hypotheses I have NOT backtested. Second pass (2026-10-07) adds [OWN] = my own quick Python recomputation on free data (heavily caveated, see section 5 and the changelog at the end) and marks sources as full text (FT) or abstract/snippet only.

## 1. Summary, horizon, asset class, holding period

Trend following goes long markets that have risen and short markets that have fallen over a lookback window, sized by volatility, across a diversified set of liquid futures and forwards (equity indices, rates, FX, commodities). Typical holding period is weeks to a few months; win rate is low (often cited around 35-45% by practitioners, [UNV]) and the payoff profile is positively skewed: many small losses, occasional large gains in sustained moves. Signals can be a price breakout (Donchian/Turtle), a moving-average crossover, or the sign of trailing 1-12 month return (time-series momentum, TSMOM). The academic claim is a century-long, multi-asset premium with crisis-period diversification. The honest modern summary: the long-run edge is real but smaller than the 1990s-era record, faster variants have decayed, and 2009-2019 was a long, painful stretch before 2022.

## 2. Origin and who uses it

- Richard Dennis and William Eckhardt ran the 1983-84 "Turtle" experiment: novices were taught a mechanical breakout system with explicit risk rules. Alumni include Curtis Faith (author of *Way of the Turtle*) and Jerry Parker (founder of Chesapeake Capital). The widely quoted Turtle return figures remain unaudited. Second pass: the Wikipedia page on Dennis (opened) says 23 people were trained in two groups (Dec 1983 and Dec 1984), that the Turtles "reportedly" earned an aggregate $175 million (it cites Investopedia), and that Dennis reportedly lost about $10 million on 19 Oct 1987 and about $50 million over 1987-88; it also cites a back-test showing a sharp drop in performance after 1986 [PC]. Faith's book blurb (seen only in a search snippet, not opened) claims an average of 80%+ a year and $100 million+ in profits [PC, marketing]. No audited record found; treat all Turtle return figures as [PC].
- Donchian channel breakouts (Richard Donchian, mid-20th century) are the ancestor of the Turtle entry rule [PC, from memory].
- Academic formalization: Moskowitz, Ooi and Pedersen (2012), "Time Series Momentum", J. Financial Economics 104 [PR]; Hurst, Ooi and Pedersen (2017), "A Century of Evidence on Trend-Following Investing", J. Portfolio Management 44(1) [PR, practitioner-authored].
- Industry: Winton (David Harding), Man AHL, Campbell & Company, Chesapeake, AQR, and many others; benchmarks include the SG CTA Index and SG Trend Index. Michael Covel's *Trend Following* books and podcast (including Jerry Parker episodes) are the main popular-press channel; they are advocacy, not evidence [PC].

## 3. Economic rationale and who is on the other side

Proposed sources of trends (none is proven; they are competing stories):
1. Under-reaction and slow information diffusion, followed by herding/over-reaction (behavioral; Hurst et al. cite anchoring and herding) [PR/WP].
2. Non-profit-maximizing participants: central banks smoothing FX and rates, corporate hedgers, and index/pension rebalancing, which create persistent flows [PR/WP].
3. Risk transfer: MOP (2012) find speculators' positions load positively on TSMOM and hedgers' negatively, i.e. trend followers are paid by hedgers for providing liquidity/insurance and "profit at the expense of hedgers" [PR].
4. Convexity: trend following resembles a long straddle on the market; it pays in extended bear markets and rallies, bleeds in range-bound reversals.

Counterparties: hedgers (commodity producers, corporates), mean-reversion/value investors who fade moves, and discretionary traders who exit winners early. Important caveat: if the premium is partly a compensation for hedgers' demand, it can shrink as trend capital grows.

## 4. Canonical rules

### 4a. Turtle System (as commonly reproduced; secondary sources disagree on small details)
I still could not retrieve Faith's original document: second-pass attempts at trendfollowing.com, tradingwithrayner.com and oxfordstrat.com returned error or HTML pages rather than the PDF, and the search results offering "free PDFs" were on spam-looking domains that I did not open. The rules below come from secondary reproductions plus my memory; verify against *Way of the Turtle* before coding. Second pass: I read the full MQL5 implementation article (opened; it says it follows Faith's book). It confirms N as a 20-day ATR with Wilder smoothing, 1% of equity per unit, 2N stop from the latest entry, a four-unit cap per market, a 12-unit cap in one direction across correlated markets (that cap is stated but not implemented in the article), and the skip rule for System 1. It adds units at one additional N, which conflicts with the 0.5N interval in Faith's free PDF as reported by a forum thread (a search snippet) [PC]. The pyramiding interval is therefore genuinely disputed in secondary sources and must be settled from the primary text.
- N = 20-day average true range (exponential smoothing in the original).
- Unit size: 1% of account equity / (N x dollar value per point). Risk caps: about 4 units per market and 12 in one direction are corroborated by the MQL5 article [PC]; the 6 per closely correlated group and 10 per loosely correlated group (from memory) remain [UNV].
- System 1: enter on a 20-day high/low breakout; exit on a 10-day opposite extreme. Skip rule: ignore a System 1 entry if the previous System 1 breakout would have been profitable; a 55-day failsafe breakout is taken regardless.
- System 2: enter on 55-day breakout; exit on 20-day opposite extreme; no skip rule.
- Add one unit every 0.5N favorable move (Faith's free PDF per a forum report) or every 1N (Covel; the MQL5 article), up to the unit cap; stop at 2N from the most recent entry (stops ratchet). Disputed, see above.
- Universe: liquid futures across rates, FX, metals, energy, softs, grains, indices.

### 4b. TSMOM (Moskowitz-Ooi-Pedersen) [PR]
- Signal: sign of the excess return over the past 12 months (MOP also examine 1-60 month lookbacks/holding periods).
- Size: each position scaled to constant ex-ante volatility (MOP target 40% annualized per instrument, from my reading of the paper's design; the exact target is not critical), using exponentially weighted lagged squared daily returns.
- Hold one month, rebalance monthly. 58 liquid futures/forwards; pooled regression sample Jan 1985-Dec 2009.

### 4c. Hurst-Ooi-Pedersen century version [PR]
- Equal-weight combination of 1-, 3-, and 12-month sign signals on 67 markets (29 commodities, 11 equity indices, 15 bonds, 12 currency pairs), monthly rebalance, each market scaled to equal risk and the portfolio to 10% ex-ante annualized vol, 1880-2016; simulated costs and a 2%/20% fee layer are shown separately.

## 5. Evidence

| Claim | Source | Sample | Costs | Grade |
|---|---|---|---|---|
| TSMOM profitable in every one of 58 instruments; diversified portfolio Sharpe above 1 annually, about 2.5x the equity market; little correlation to standard factors | MOP 2012, JFE (read primary text) | 1985-2009 (returns data from 1965) | Returns shown mostly gross; paper discusses but does not centre costs | PR |
| Speculators profit from TSMOM at hedgers' expense (CFTC positions) | MOP 2012 | 1986-2009 positions data | n/a | PR |
| Positive average return in each market with average per-market Sharpe about 0.4 over 1880-2016; positive in each decade at 1/3/12-month horizons (authors' description); 1-month-lagged signals degrade, especially short signals | Hurst et al. 2017 (read text) | 1880-2016 | Simulated transaction costs and 2/20 fee shown; costs based on recent estimates and flagged as uncertain historically | PR, but the earliest data are reconstructed and sparse |
| Strong in extreme equity years ("smile"); positive on average in 60/40 drawdowns | Hurst et al. | 1880-2016 | net of costs | PR |
| Fast (about 1-week turnover) trend systems decayed: gross Sharpe by decade 1.85 (1984-93), 0.85 (1994-03), 0.00 (2004-13); medium 1.54/1.18/0.70; slow 0.95/0.94/0.57 | Winton, Duke-Harding-Land, Dec 2013 (read table) | 1984-2013, 20 markets | Explicitly GROSS of costs and fees | WP, from a firm that sells trend following |
| 30-year gross Sharpe 0.87 / 1.12 / 0.81 for fast/medium/slow | same | same | gross | WP |
| TSMOM alpha 1.27%/month with vol-scaled weights vs 0.41% unscaled; outperformance concentrated pre-2001; vanishes 2009-2013; beat buy-and-hold in only 29 of 55 contracts unscaled | Kim, Tse, Wald (2016) via Quantpedia summary (did not read primary) | 55 futures, 1985-2013 | n/a | PR (summary only read) |
| Post-2008 weakness explained by higher cross-asset correlation; correlation-adjusted leverage helps | Baltas and Kosowski (SSRN/Wiley chapter), via search summary (primary not read) | to 2013 | claims lower turnover from better vol/trend estimators | WP |
| SG Trend Index: +20.9% in 2008, +27.4% in 2022; second-largest drawdown since 2000 of 20.4% (May 2024-May 2025); 16 drawdowns above 10% since 2000, about every 18-24 months | Cambridge Associates insight (read) | 2000-2025 | index, net of fund fees | PC (allocator commentary) |
| SocGen CTA Index annualized 1.6% for 2010-2019; Barclay CTA Index annualized by decade: 20.3% (1980s), 7.1% (1990s), 5.9% (2000s), 0.8% (2010s) | Institutional Investor, 6 Dec 2022 (opened and read; article gives no fee discussion) | 1980-2019 | index returns, net of underlying fund fees; Barclay index is equal-weighted and hypothetical | PC, now sourced (upgraded from "snippet") |
| SG CTA Index about +20.1-20.2% in 2022 (record since 2000), SG Trend Index +27.3% in 2022 (Cambridge Associates, read, says 27.4%); SG CTA roughly -3% in 2023; Barclay CTA Index +7.13% in 2022, +3.45% 2024, +3.10% 2025 | search-result snippets only (Hedgeweek, thefullfx, StoneX; a promotional site for the Barclay figures) | 2022-2025 | net of fees | PC, still unverified; the official SG factsheet URL I tried returned 404 and the BarclayHedge page redirected to a gated site |
| Trend following Sharpe 0.8 (t = 5.9; de-biased for the market's own drift t = 5.0) on a diversified futures pool since 1960 with a 5-month EWMA trend signal; by decade Sharpe 0.66 (1960s), 1.15 (1970s), 1.05 (1980s), 1.12 (1990s), 0.75 (post-2000, de-biased t = 1.9); about 200 years of spot+futures data give Sharpe 0.72, t = 10.5; 10-year performance never negative since the 1800s; strategy about flat since 2011; very short (about 3-day) trends decayed since 1990, long trends did not; typical drawdown length about 1/Sharpe^2 years | Lemperiere, Deremble, Seager, Potters, Bouchaud (CFM), "Two centuries of trend following", arXiv 1404.3274, April 2014 (FT read) | 1960-2013 futures; 1800-2013 spot | "without costs" per the paper; monthly bars | WP by a trend-following firm; independent of AQR/Winton data, supports Twist A rationale |
| Harding (2018): long-run Sharpe outlook for trend about 0.5; faster models crowded, slower more consistent | Top Traders Unplugged summary of a Winton podcast, 2023 | n/a | n/a | PC, second-hand |

Critical reading:
- The strongest evidence (a century of data) rests on a monthly, volatility-scaled, diversified construction. Kim-Tse-Wald show much of TSMOM's "alpha" disappears without volatility scaling, which means part of the premium is a leverage/risk-parity effect, not pure directional prediction.
- Pre-1960s data in Hurst et al. use sparse, high/low-price-based, partly constructed series; treat the early decades as indicative.
- Winton's own data show the decay of fast trend before costs; costs would make fast systems worse.
- Turtle-style single-system results are mostly marketing: the original Turtle returns are unverified, and the 20/55-day parameters were fit to 1970s-80s futures, a period of strong inflation/rate trends.
- Post-publication: the 2009-2019 period (SG CTA about 1.6% a year) is the live out-of-sample for the TSMOM paper, and it is poor. 2020-2022 recovered sharply, then 2023-2025 was weak again. This is consistent with "positive but small, volatile Sharpe", not a decisive death or revival.
- Second-pass cross-check: Lemperiere et al. (full text) find the long-trend premium statistically unchanged through 2013 and attribute the post-2011 flat spell to ordinary Sharpe-0.7 drawdowns, but also find short trends withered, which agrees with Winton's decay table; the Institutional Investor decade figures (Barclay CTA 0.8% a year in the 2010s versus 5.9% in the 2000s) show the live CTA industry did much worse than the 0.7-0.8 backtest Sharpe suggests, a gap that fees, the end of the bond bull, and implementation explain only in part. Neither paper's backtest is net of costs.

### Own quick check [OWN]: trend rules on nine liquid ETFs (not futures; heavily caveated)
- Data/sample: Yahoo Finance adjusted closes for SPY, EFA, EEM, TLT, IEF, GLD, DBC, VNQ, UUP; common sample 2007-03-01 to 2026-10-07 (about 19.6 years, 4,933 days). Script and outputs live in the session scratchpad (d2scripts/trend.py, trend_out.txt), not in the repo.
- Construction: long/short, each asset scaled to 10% vol (EWMA, 40-day half-life), averaged over 9 assets with no diversification multiplier (so portfolio vol is only about 4.7%; Sharpe is scale-free). Positions lagged one day. Costs 0/5/10 bp of traded notional. Short-ETF borrow, financing and futures-roll effects not modelled. No Turtle sizing, pyramiding, stops or skip rule, so the Donchian rows are close-only breakout proxies, not the Turtle system.
- Results (Sharpe, gross / 5 bp / 10 bp): 12-month sign TSMOM, monthly rebalance 0.39 (t 1.7) / 0.35 / 0.31, max drawdown about -14%; Donchian 20/10 daily 0.01 / -0.20 / -0.40 (turnover about 20x/yr); Donchian 55/20 0.28 / 0.18 / 0.08; 50/200 moving-average cross 0.41 / 0.37 / 0.33. Sub-periods for TSMOM (gross): 0.46 in 2008-2014, 0.36 in 2015-2026. Benchmarks over the same window: SPY buy-and-hold Sharpe 0.64 (max drawdown -55%), equal-risk long-only basket 0.91 (flattered by the bond/gold run).
- Reading: slow trend rules are weakly positive, fast breakouts are wiped out by modest costs, which matches Winton and Lemperiere on speed decay. With t about 1.7 the TSMOM result cannot be distinguished from zero or from a true Sharpe of 0.5. This does not replicate a diversified 58-market futures TSMOM and says nothing about the 1985-2009 MOP sample; it is a sanity check, not evidence for deployment.

## 6. Failure regimes and risks

- Trendless, mean-reverting, central-bank-suppressed markets (2009-2013 low-vol rate repression; 2023-2025 chop).
- V-shaped reversals after a trend is established (April 2025 tariff whipsaw cited by Cambridge; bond reversals cited for 2023).
- Rising cross-asset correlation: diversification across 50+ markets collapses to a few bets (Baltas-Kosowski).
- Crowding in fast variants (Winton 2013 data).
- Concentration risk: long bonds contributed heavily during the 1980s-2020 bond bull; a regime where bond trends are absent removes a historic profit source [PC].
- Costs and roll: futures roll cost, bid-ask, and slippage in thin markets (softs, some metals).
- Behavioural risk: an investor typically must tolerate multi-year drawdowns; the Turtle-era "love your losses" ethos (Parker/Covel) is psychological advice, not a risk model.
- Leverage on Sharpe 0.3-0.5 is fragile; target volatility is a model assumption.

## 7. MY TWIST (hypotheses, NOT backtested)

### Twist A: Slow-tilted, forecast-scaled multi-speed trend with a hard cost budget
- Rationale: Winton's table shows fast systems' Sharpe decayed to zero gross while slow held at 0.57; costs hurt fast systems most.
- Rule changes vs 4c: replace sign signals with continuous EWMA-crossover forecasts, capped at +/-2 standard units, across three speeds with weights 20% fast (8/32 days), 30% medium (32/128), 50% slow (64/256) instead of equal; trade only when the target position differs from current by more than a 10-20% buffer.
- Parameters to test: speed weights {equal, 20/30/50, 0/30/70}; buffer {0, 10, 20%}; forecast cap {1, 2}.
- Expected effect: lower turnover and cost drag, modestly lower gross Sharpe but equal or higher net Sharpe in 2004-2023.
- Falsification: if after realistic costs the 20/30/50 variant's net Sharpe does not exceed the equal-weight version by more than one standard error in a 2010-2023 out-of-sample (holding parameters fixed from pre-2010 selection), reject.

### Twist B: Correlation-aware portfolio leverage plus sector risk caps
- Rationale: Baltas-Kosowski attribute post-2008 weakness partly to rising pairwise signed correlation; Hurst notes heavy bond exposure.
- Rule: scale gross leverage by target_vol / sqrt(w' C w), where C is a 120-day rolling correlation of signal-weighted returns, capped; limit any one sector (rates, equity, FX, energy, metals, ags) to 30% of risk.
- Parameters: correlation window {60, 120, 250}; sector cap {25, 30, 40%}; max leverage multiplier {2, 3}.
- Expected effect: shallower drawdowns during correlation spikes; may reduce upside in genuine crisis trends (2008, 2022).
- Falsification: no reduction of max drawdown (stationary bootstrap, 95% interval) versus the plain vol-scaled version, or a loss of more than 25% of the 2008 and 2022 crisis-alpha.

### Twist C: Trend-signal "agreement" filter for entries only
- Rationale: whipsaw losses cluster when slow and fast trends disagree.
- Rule: scale the position by 0.5 when the 8-day and 128-day signals have opposite signs; full size when they agree.
- Parameters: disagreement scale {0, 0.5, 0.75}.
- Expected effect: lower hit rate on reversal chop; slight lag at turning points.
- Falsification: no improvement in net Sharpe or no reduction in the longest drawdown versus Twist A alone in out-of-sample years.

## 8. Implementation spec

Data: continuous futures (back-adjusted ratio or difference, document which) for about 40-60 liquid contracts; daily OHLC; contract specs, point values, margins; roll calendars; FX conversion; bid-ask and commission schedule; CFTC COT optional.

Signals: choose Twist A baseline (EWMA crossover forecasts) or the Turtle breakout as a reference. Always compute signals from data available at the prior close; trade next open or close with a one-bar lag.

Sizing: instrument risk weight w_i = target_vol_portfolio x IDM / (N x sigma_i) with IDM (instrument diversification multiplier) estimated from rolling correlations, capped at about 2.5. Per-instrument vol: EWMA with 30-60 day half-life blended with a long-run floor to avoid under-estimating in calm periods.

Execution: trade at the close or via VWAP in the last session hour; roll by volume crossover several days before expiry; apply the position buffer.

Stops: trend followers usually do not need a price stop beyond the signal exit; keep a portfolio-level and a per-trade disaster stop (e.g. 3N) for operational protection only.

Costs model: per-contract commission + half bid-ask + slippage proportional to size/ADV, plus roll cost (two crossings per roll); assume at least 1-3 bps of notional per side for liquid financial futures and larger for commodities; sensitivity test at 2x.

```
for each day t after close:
    for each instrument i:
        sigma_i = ewma_vol(returns_i, halflife=40)
        f_i = sum_k wk * clip(ewmac(price_i, fast_k, slow_k)/sigma_price_i * scale_k, -2, 2)
        target_i = f_i * (target_vol * IDM) / (sqrt(252) * sigma_i * n_instruments^0.5-ish weight)
        if abs(target_i - pos_i) > buffer * abs(target_i): trade to target_i
    apply sector caps and correlation leverage scaler
    send orders for t+1
```

## 9. Backtest plan

- Walk-forward: choose speed weights/buffer on 1990-2009, freeze, test on 2010-2025; also reverse-split (train late, test early) to check stability.
- Multiple-testing control: count every variant tried; use the Harvey-Liu-Zhu style hurdle (t above roughly 3.0 for new discoveries) or a deflated Sharpe/Reality Check across the trial set. Report number of trials.
- Out-of-sample: also evaluate on markets not used in selection (hold out a random 30% of contracts) and on pre-1985 constructed data with a low weight of belief.
- Robustness: parameter-plateau plots, sub-period decade table, cost multipliers 1x-3x, one-month signal lag.
- Metrics: net Sharpe with bootstrap CI, skew, max drawdown and time-to-recovery, Calmar, hit rate, turnover, correlation to equities, performance in the worst 10% equity months, 60/40 overlay benefit.
- Benchmarks: SG Trend Index replication check (should correlate if universe is sound), plain 12-month TSMOM.

## 10. Risk management and kill-switch rules

- Portfolio target vol 10% (study 8-15%); hard cap on leverage and per-instrument risk 1-2% of equity at 2N.
- Drawdown governor: halve risk at -10% from peak, review at -15%, pause new signals and audit data/execution at -20% unless drawdown is within the strategy's backtested 95th percentile.
- Kill switches: execution slippage over 3x model for 20 days; data-feed error flag; margin utilisation over 50%; rolling 36-month net Sharpe below -0.3 triggers a formal review (not auto-liquidation, because trend Sharpe is noisy: standard error of a 3-year Sharpe is about 0.58).
- Do not judge the system on fewer than 8-10 years of live returns.

## 11. Annotated sources

| # | Source | URL | Type | Grade |
|---|---|---|---|---|
| 1 | Moskowitz, Ooi, Pedersen, Time Series Momentum (JFE 2012) | https://fairmodel.econ.yale.edu/ec439/jpde.pdf (SSRN 2089463) | Peer-reviewed paper, read | A |
| 2 | Hurst, Ooi, Pedersen, A Century of Evidence on Trend-Following Investing (JPM 2017) | https://fairmodel.econ.yale.edu/ec439/hurst.pdf ; https://www.aqr.com/Insights/Research/Journal-Article/A-Century-of-Evidence-on-Trend-Following-Investing | Journal article, read (exhibit values are images, not extracted) | A- |
| 3 | Duke, Harding, Land, Historical Performance of Trend Following (Winton, 2013) | https://www.TrendFollowing.com/whitepaper/d.pdf | Firm white paper, read, gross of costs | B |
| 4 | Kim, Tse, Wald, Time series momentum and volatility scaling (J. Financial Markets 2016) | https://quantpedia.com/deconstructing-the-time-series-momentum-strategy/ | Summary of peer-reviewed paper | B (primary still unread; not attempted again) |
| 5 | Baltas and Kosowski, Demystifying Time-Series Momentum Strategies | https://papers.ssrn.com/abstract=2140091 (Imperial and CME copies exist; my fetches of both failed) | Working paper, search summary only (versions differ: 2015 covers 1974-2013, CME 2017 version 1984-2013; reported turnover cut of more than a third) | B- (primary still unread) |
| 12 | Lemperiere, Deremble, Seager, Potters, Bouchaud, Two centuries of trend following | https://arxiv.org/pdf/1404.3274 | Working paper (CFM), full text read; gross of costs | B+ |
| 13 | Institutional Investor, Managed futures are working but investors aren't benefitting (6 Dec 2022) | https://www.institutionalinvestor.com/article/2azcn7pt0hfyiv0pdqrr4/portfolio/managed-futures-are-working-but-investors-arent-benefitting | Trade press, opened; decade returns for Barclay and SocGen CTA indices | C+ |
| 14 | Wikipedia, Richard Dennis (Turtle experiment facts, cited to Investopedia, NYT, Time) | https://en.wikipedia.org/wiki/Richard_Dennis | Secondary, opened | C |
| 15 | AQR page for Hurst-Ooi-Pedersen | https://www.aqr.com/Insights/Research/Journal-Article/A-Century-of-Evidence-on-Trend-Following-Investing | Landing page, opened: abstract only (strategy built from 1880, profitable over about 110 years); no exhibits | B (exhibits still unread as numbers) |
| 6 | Cambridge Associates, Does trend following's recent struggle signal... | https://www.cambridgeassociates.com/insight/does-trend-followings-recent-struggle-signal-that-the-strategy-is-structurally-broken/ | Allocator commentary, read | B |
| 7 | Top Traders Unplugged, The Trend was Never in Doubt (Aug 2023) | https://www.toptradersunplugged.com/?p=13535 | Second-hand podcast summary of Winton CIO | C |
| 8 | Covel, Trend Following Radio, Jerry Parker episodes | https://www.trendfollowing.com/2013/04/12/ep-116-jerry-parker-interview-with-michael-covel-on-trend-following-radio/ | Episode listings only; audio not heard | C |
| 9 | MQL5 article, Original Turtle Trading Rules; TradingView scripts | https://www.mql5.com/en/articles/23448 | Secondary implementation of the rules; MQL5 article opened and read in the second pass (1N pyramid, 4-unit and 12-unit caps) | C+ |
| 10 | Trade-press coverage of SG CTA Index 2022 | https://www.hedgeweek.com/flat-december-sees-ctas-complete-record-year-2022/ | Trade press, snippet only; the official SG factsheet was not obtained | C |
| 11 | Man Group / AHL commentary on 2009-2019 (Hedge Fund Journal, hedgeweek) | https://thehedgefundjournal.com/man-ahl-marks-30-years/ | Marketing/commentary, snippets only | C |

I still have not read Faith's *Way of the Turtle*, Covel's book, or any Campbell & Company, Man AHL or Winton post-2013 primary research (searches returned no public white papers for those firms covering 2019-2025); claims attributed to them are secondhand.

## 12. Open questions

1. How much of TSMOM's post-1985 Sharpe is vol-scaling leverage versus directional prediction (Kim-Tse-Wald), and does it survive on an unlevered basis?
2. Is the 2009-2019 weakness a regime (repressed rates, QE) or permanent crowding? 2022 supports regime; 2023-2025 chop supports ambiguity.
3. What are the true net Sharpe values after realistic fees, financing, and roll costs for retail-size accounts (probably much smaller than index headlines)?
4. Can trend premia exist independently of the bond bull market of 1981-2020?
5. How reliable are pre-1960 reconstructed series in Hurst et al.?
6. What capacity does the strategy have before hedger-provided premia are competed away?
7. (Second pass) Why did live CTA indices return 0.8% a year in the 2010s (Barclay) when century-scale backtests show gross Sharpe 0.7-0.8? Fees, cost drag, a smaller bond tailwind and post-2008 correlation (Baltas-Kosowski) are candidate answers; I could not quantify the split.

## Second-pass changelog (2026-10-07)

- Read in full text: Lemperiere et al. (arXiv 1404.3274), the MQL5 Turtle article, the Institutional Investor CTA decade article, Wikipedia (Richard Dennis), AQR landing page. Not obtained despite attempts: Faith's original Turtle rules (error/HTML pages), the official SG CTA Index factsheet (404), BarclayHedge data (redirect to gated site), Baltas-Kosowski PDFs (fetch failed), Kim-Tse-Wald primary, Campbell/AHL/Winton post-2013 white papers (none found), Hurst-Ooi-Pedersen exhibit numbers.
- Resolved/changed: SocGen CTA 1.6% (2010-2019) now sourced to an opened article (was snippet); added Barclay decade series (20.3/7.1/5.9/0.8%); 2022 SG CTA stated as 20.1-20.2% and SG Trend 27.3-27.4% (was "about 20%"); Turtle 4-unit and 12-unit caps partially corroborated, pyramid interval flagged as disputed (0.5N vs 1N) instead of asserting 0.5N; Turtle return claims now carry named secondary sources and are still unaudited.
- Added: Lemperiere et al. row (Sharpe 0.8 since 1960, decay in post-2000 de-biased t of 1.9, no decay of long trends, short trends withered) and an [OWN] ETF check (slow rules weakly positive, 20/10 Donchian negative after 5 bp).
- Grades: Lemperiere added at B+; MQL5 C to C+; Baltas-Kosowski stays B-; Hurst-Ooi-Pedersen stays A- (exhibits unread). Overall dossier grade effect: the case for slow trend is slightly stronger on independent data, the case for the Turtle system as specified is no better supported, and the case for fast variants weaker.
- Twists A, B, C remain hypotheses, NOT backtested; Lemperiere and my ETF check are consistent with the Twist A rationale (slow-tilt) but are not tests of it.
- Remaining [UNV]: 35-45% win rate; Turtle correlated-group caps (6 and 10 units); exact Turtle returns; Faith vs Covel pyramid rule.
