# A4. Volume Profile, Market Profile and Order-Flow (Auction Market Theory)

Status: research dossier. Section 7 ideas are untested hypotheses. Not investment advice.
Labels: [PR] peer-reviewed, [WP] working paper/preprint, [PRAC] practitioner claim, [UNV] unverified.
Source depth: this is the thinnest of the four dossiers on primary practitioner material (see section 11). Second pass (2026-10-07): the academic OFI papers were read in full text (Cont-Kukanov-Stoikov, Cont-Cucuringu-Zhang, Andersen-Bondarenko); practitioner profile material and books are still not primary.

## 1. Summary, horizon, asset class, holding period

Two linked toolkits. (1) Profile-based auction analysis: Market Profile (TPO, time-price opportunity) and Volume Profile build a distribution of trading by price for a session or longer; the point of control (POC, busiest price), value area (conventionally about 70 percent of activity), high-volume nodes (HVN) and low-volume nodes (LVN) are used as reference levels for "balance" versus "imbalance" and for rules such as the "80 percent rule". (2) Order-flow tools: footprint charts, delta (volume traded at the ask minus at the bid) and cumulative volume delta (CVD), and book-based order-flow imbalance (OFI), used to read who is aggressing and whether a level is being absorbed. Horizon: seconds to hours intraday (scalping around levels) up to multi-day for composite profiles. Assets: index and commodity futures primarily, liquid equities, crypto perpetuals. The academic evidence supports one narrow thing well: short-horizon price changes are largely explained, contemporaneously, by order-flow imbalance at the touch. Second pass correction: contemporaneous explanation is not forecasting; in the one full-text paper that forecasts, one-minute-ahead out-of-sample R-squared of OFI models was slightly negative. It does not support footprint patterns, value-area rules or POC "magnets" as profitable rules; those remain practitioner claims.

## 2. Origin and who uses it

- Peter Steidlmayer developed Market Profile at the Chicago Board of Trade in the 1980s (dates in secondary sources range from mid-1980s; one patent filing cites 1986). Jim Dalton's Mind Over Markets (1990) and the earlier Profile Reports (Dalton Capital Management, 1987-1991) are credited as the source of the "80 percent rule" by a commentator I could not verify. I did not read either book. [PRAC, secondary descriptions only.]
- Auction market theory (AMT): price rotates to find fair value that satisfies both sides; balance is two-sided rotation around value, imbalance is directional search for new value; acceptance outside a range signals imbalance, a failed probe signals continued balance. The initial balance (first hour, later first 30 minutes in many definitions) is the early range, and extensions beyond it are read as longer-timeframe participants stepping in. [PRAC]
- Footprint/delta traders: the modern retail-visible example is Fabio Valentini, described in secondary summaries as a Robbins Cup / World Cup Trading Championship competitor trading Nasdaq futures with volume profile and CVD; I could not verify return claims (one summary says over 500 percent in a year) and sources disagree on details. [UNV]
- Academic order-flow work: Rama Cont and coauthors (price impact of order book events; cross-impact of OFI), Lipton, Pesavento and Sotiropoulos (quote imbalance and trade arrivals), Easley, Lopez de Prado and O'Hara (VPIN flow toxicity), Lee and Ready (trade classification). Firms such as market makers use order-flow signals in quoting (see A1); published trading rules based on footprints are rare.
- Vendors: ATAS, CQG, Bookmap and similar platforms supply the tools and the educational material, with obvious commercial bias.

## 3. Economic rationale and the other side

- Why order flow matters (strong evidence): Cont, Kukanov and Stoikov show that over short intervals price changes are largely explained by net imbalance of buy/sell activity at the best quotes, with a linear relation whose slope is inversely related to market depth. Informed or urgent traders consume liquidity; market makers revise quotes; the price moves. The other side is the liquidity provider, who is adversely selected, and the passive resting orders that get consumed.
- Why levels might matter (weak evidence): prior high-volume prices may attract resting orders, anchor memories and algorithmic references; LVNs have little resting interest so price may travel quickly through them. Proposed, not demonstrated. One commentator's explanation of the 70 percent value-area convention is its resemblance to one standard deviation; price-volume distributions are not normal, so this is a heuristic.
- Absorption (practitioner): a large passive order soaks up aggressive volume without price moving, shown as heavy delta with little movement; the aggressor is then trapped. Plausible mechanism (iceberg orders exist), but no test found.
- Who is on the other side of a level trade: stops and breakout traders on the failed probe; trend followers when the fade is wrong. Profile levels are public and widely watched, which reduces edge if anything.

## 4. Canonical rules

### 4a. Value-area / "80 percent rule" (Dalton lineage, as described by secondary sources)
1. Build the prior session's profile; mark value area high (VAH), value area low (VAL), POC (value area = the region around POC holding about 70 percent of TPOs or volume; CQG's study uses 68 percent, showing the convention varies).
2. Setup: today opens outside the prior value area, then trades back inside it and holds for two consecutive 30-minute periods (two TPO brackets, "A" and "B" in the standard lettering).
3. Expected target: rotation to the opposite edge of the prior value area. Entry is typically after the second bracket closes inside; stop and exact entry are not specified in the sources I read (an educational article said so explicitly). Exception: if price opens outside and never returns, treat as a directional day and do not fade.
4. Variants: opening inside value then leaving and returning.

### 4b. Initial balance and range extension
Define IB as the first 30-60 minutes' range. Wide IB suggests range-bound trading; narrow IB suggests potential for extension (per one description; the logic is debated). Trade extensions with acceptance beyond IB edges, or fade failed extensions.

### 4c. HVN/LVN rotation
Treat HVNs as magnets/acceptance zones and LVNs as fast-travel zones; enter on acceptance beyond a node toward the next node, or fade at an HVN edge. Exact rules are discretionary.

### 4d. Footprint/delta confirmation (discretionary patterns)
Typical: stacked bid/ask imbalances (a cell where volume at ask exceeds the bid at the adjacent lower price by a ratio, commonly 3:1), absorption (high delta, no price progress), delta divergence (new price high with lower CVD), exhaustion at bar extremes. Thresholds vary by vendor and trader.

### 4e. Quantitative OFI signal (academic definition)
OFI over an interval = sum of changes in bid-size at the best bid (when the bid is unchanged or rises) minus changes in ask-size at the best ask (when the ask is unchanged or falls), with the standard price-change conditions per Cont et al.; the integrated multi-level OFI of Cont, Cucuringu and Zhang combines top levels into one variable. Forecast the next mid-price change with a regression on OFI normalised by depth.

## 5. Evidence

- OFI and price impact (second pass, full texts read). Cont, Kukanov, Stoikov (arXiv v3; JFEC 2014) [PR]: sample is one month (April 2010, 21 trading days) of NYSE TAQ level-1 data for 50 randomly chosen S&P 500 stocks, 10-second grid, regressions per half-hour (about 180 observations each). Price change on OFI has an average R-squared of 65 percent (35 to 79 percent across stocks); on trade imbalance alone 32 percent; adding trade imbalance to OFI lifts it only to 67 percent. For absolute price changes, OFI gives 58 percent and traded volume 23 percent. The slope falls with depth, as claimed. Authors' own limits: level-1 data only, one month, OFI includes price-changing events which makes part of the fit tautological (R-squared falls to roughly 35 to 60 percent when excluded), and trade direction uses a heuristic. Crucially, these are contemporaneous fits within the same interval, not forecasts. Cont, Cucuringu, Zhang (arXiv 2112.13213) [WP]: top 100 S&P 500 stocks, Nasdaq ITCH via LOBSTER, 2017-2019; integrated multi-level OFI raises contemporaneous in-sample R-squared from about 71 percent (best-level) to about 87 percent; out-of-sample about 65 percent versus 83 percent. But for one-minute-ahead returns, out-of-sample R-squared of the OFI-based models is slightly negative (about -0.37 percent for own best-level OFI, -0.10 percent when lagged cross-asset OFIs are added), and the forecast-implied trading PnL table explicitly ignores trading costs and is only relative. So the first-pass claim that cross-asset OFIs "help forecast" holds only in a relative, cost-free sense. Kolm, Turiel, Westray (Mathematical Finance 2023) [PR, abstract level via RePEc]: deep learning on OFI features for 115 Nasdaq stocks beats models on raw order books; the effective horizon of stock-specific forecasts is about two average price changes; I could not read the body, so no net-of-cost result is known. Lipton et al. and Bugaenko remain abstract-only (not re-opened). Net: OFI is a strong contemporaneous explainer, the forecast edge is short-lived and unproven net of costs; the winners are fast participants.
- Trade-sign dependence: delta/CVD require buy/sell classification. Where the venue supplies an aggressor flag this is reliable; otherwise tick/Lee-Ready rules are used. Reported accuracy varies a lot: early studies about 85 percent, a later study cited 20-30 percent misclassification on 2005 data, and a direct test found Lee-Ready roughly equal to the tick test and biased for effective spread and signed volume; a 2020 study on fast markets found Lee-Ready did at least as well as in slower periods [PR but I read secondary summaries; Theissen 2001 abstract was unavailable]. Implication: on equities with inferred sides, delta is noisy; on futures with aggressor flags, less so.
- VPIN (second pass): I read Andersen and Bondarenko's full 2013 working-paper text (E-mini S&P 500, flash crash of 6 May 2010) [WP version of a JFM 2014 paper]. Their four findings: the time-bar VPIN of Easley et al. is not a useful volatility predictor (VIX and similar are far better); it is mechanically tied to trading intensity because of how time bars are formed; it did not reach a historical high before the crash but after it subsided; and it is noisy depending on where the volume clock starts. Fixed-volume-bin and tick-rule versions gave opposite results (negative association with volatility), and the bulk-volume-classification version behaves like realized volatility. The Easley, Lopez de Prado, O'Hara rejoinder (not read, only described in search snippets) says the critique attacks a method they do not advocate, so the dispute is not resolved by my reading; but the critique is specific and empirical, and I now lean to treating VPIN as unproven as a trading signal. Retraction Watch coverage of an earlier-version withdrawal was seen only in a search snippet. [PR vs WP dispute]
- Value-area rules: I found no peer-reviewed or independently audited test. Forum anecdotes: one trader reported a TradeStation test with completion near 62 percent; another thread recorded 120 setup days (about 12 percent of days) of which 75 reached the other edge (62.5 percent); a reply said their own test was nowhere close [PRAC, unverified forum posts]. The commonly cited "80 percent" has no sample, instrument or period attached, and an educational article admitted that. Treat as folklore. Second pass: I searched again for academic, thesis or open-source backtests of value-area, POC or volume-profile levels and found none; results were vendor pages, TradingView scripts and forum posts (search snippets only). The only code-level material is TradingView Pine tools that build the 80 percent setup (one open-source script requires price to hold inside value for 45 minutes on 15-minute charts) with no published statistics, and a QuantConnect forum question about implementing developing POC in Python without results. I also could not find CME Group's own Market Profile education page: CME's 'FX Market Profile' hit is an unrelated order-book dashboard. A vendor article attributes 'about 68 percent within one standard deviation of POC' to CME research; I could not trace it, so it is not used. Own small check below. Even 62 percent completion says nothing about edge without entry price, stop and costs: a fade to the far edge of value can be a good trade at a 62 percent hit rate only if the stop is much smaller than the average target.
- Own small sanity check, second pass (NOT proof): 12 liquid ETFs and megacaps (SPY, QQQ, IWM, DIA, AAPL, MSFT, NVDA, AMZN, META, TSLA, JPM, XOM), yfinance 5-minute regular-hours bars, 15 July to 7 Oct 2026 (60 sessions). Prior-day profile built from 5-minute bars by assigning each bar's volume to its typical price (H+L+C)/3 in bins of 0.05 percent of price; value area expanded from the POC to 70 percent of volume. Setup: today opens outside the prior value area, then two consecutive 30-minute closes land inside it; enter at the second close, target the opposite edge. Of 499 ticker-days opening outside value, 140 produced a setup (28 percent). The far edge was reached (on 5-minute closes, by the session close) in 65 of 140 cases, 46.4 percent. A mirror placebo (same distance, opposite direction) was reached in 74 of 140, 52.9 percent; a binomial test of real versus mirror rate gave p about 0.13. With a 2:1 payoff (stop at half the target distance) the real direction hit the target first 38 times and the stop 82 times (20 neither); the mirror direction hit 51 and stopped 66. Holding to the close: mean signed return minus 5.9 bp gross, minus 7.9 bp after an assumed 2 bp round trip (t about -1.2). Reading: in this one quarter the setup completed less than half the time, no better than going the opposite way, so the '80 percent' figure was not reproduced; the sample is small, tickers are correlated, the profile is approximated from 5-minute bars of ETF/stock volume rather than futures TPO profiles, and bins and bracket definitions were my choices. This weakens, but does not test, the rule on index futures.
- POC/value-area as support or resistance: no empirical study found in two searches; sources are brokers, platforms and forums (re-checked in the second pass with the same result). A broker page's POC "magnet" example is a single chart. [UNV]
- Footprint/delta patterns: no peer-reviewed or audited test found; claims are from vendors, YouTube/blog summaries and competition-winner profiles. Vendor arguments that trade-based delta is harder to spoof than book depth are plausible but untested.
- Post-publication decay/capacity: unmeasurable for rules without tests. For OFI, decay is by construction rapid; capacity is tiny (top-of-book size) and the winners are faster participants.

## 6. Failure regimes and risks

- Trend days: fading the value area or an HVN is run over; the "80 percent" logic itself carves out directional days after the fact, making the rule hard to falsify.
- Definition drift: value area 68 vs 70 percent, TPO vs volume profile, session boundaries (RTH vs 24h), profile bin size (tick vs multiple ticks), composite vs daily; each choice changes levels.
- Hindsight and pareidolia: patterns on footprints are easy to find ex post. The multiple-testing problem is acute because of discretion.
- Data issues: trade aggressor ambiguity, exchange differences in how "bid" and "ask" volume is printed, spoofed book depth, and stale or consolidated-feed latency for OFI.
- Latency: OFI is a seconds-scale signal; a retail connection reacts after the move.
- Volume fragmentation: equities trade across venues and dark pools; a single-venue profile misleads. Futures are more centralised, hence their popularity here.
- Event risk: news releases produce one-way flow and book vacuum.
- Behavioural: discretionary order-flow trading invites overtrading and rule drift.

## 7. MY TWIST (hypotheses, NOT backtested)

### Twist 1: Placebo-controlled, absorption-confirmed value-area fade
- Rationale: the 80 percent rule has an unverified hit rate and no stop definition; an order-flow confirmation might separate real rejection from continuation.
- Rule change: take the 4a setup only when, during the two brackets inside value, signed volume (delta) at the re-entry shows net aggression against the prior excursion direction (for example, a down-excursion followed by positive CVD) and the OFI over the last N events is non-adverse. Enter on the second bracket close; stop at the opening-extreme or the excursion extreme plus one tick buffer; target the opposite value edge, scale out at the POC.
- Parameters: bracket length (15/30 minutes), confirmation threshold (CVD z-score 0.5-1.5), stop buffer (1-4 ticks), VA percent (68/70).
- Expected effect: fewer trades, improved reward/risk.
- Falsification: compute, on the same days, results for random-level placebo setups (same entry timing, random "value area" edges of equal width) and for the unconfirmed 4a rule; if the confirmed version does not beat both with a bootstrap confidence interval above zero net of costs out of sample, reject. Also reject if the unconfirmed rule's far-edge completion rate across 5+ years of one liquid futures contract is not clearly above a driftless-random-walk baseline.

### Twist 2: Integrated-OFI timing filter for level trades
- Rationale: use the one academically supported signal (OFI) as a short-horizon timing gate for any level-based entry (profile edges, round numbers) rather than trusting footprint pictures.
- Rule change: compute multi-level integrated OFI (top 3-5 levels) over a short window; enter at a profile level only when OFI over the last 1-5 seconds points in the trade direction, and exit or tighten the stop when OFI flips sign beyond a threshold; use limit orders at the level, not market orders, to avoid paying the spread.
- Parameters: levels used (1/3/5), window (1-10 s), threshold in depth-normalised units, maximum holding (1-10 minutes).
- Expected effect: small per-trade edge in ticks; viability depends on spread and latency.
- Falsification: if mean forward 5-60 second return conditional on OFI sign, net of half-spread plus fees at realistic latency (replayed), is not significantly above zero, or the OFI gate does not improve an ungated entry set, abandon.

### Twist 3: LVN acceptance run
- Rationale: the idea that price travels fast through low-volume nodes is mechanical (little resting liquidity) and testable.
- Rule change: after a 30-minute close beyond a composite-profile LVN edge (acceptance), enter in the break direction targeting the next HVN, stop on re-entry back inside the LVN; require OFI to agree.
- Parameters: LVN threshold (percent of average bin volume, 25-60), profile lookback (5-20 sessions), bin size (1-4 ticks), acceptance (one or two closes).
- Expected effect: positive expectancy only if price speed through LVNs exceeds that through equal-width random zones.
- Falsification: compare time-to-traverse and forward return across LVN zones to matched-width random price zones using the same bars; if no significant difference or no net profit after costs in out-of-sample years, reject.

## 8. Implementation spec

Data: tick-level trades with aggressor flags (for CME futures use the exchange's trade-direction fields where available; otherwise classify by quote/tick rule and track misclassification), L2/L3 order book updates with exchange timestamps, contract roll calendar, session definitions. Store both TPO-style 30-minute brackets and volume-at-price histograms.

Signals: prior-session POC/VAH/VAL, composite profile HVN/LVN, IB range, delta/CVD per bar, OFI (best level and multi-level integrated), spread, depth.

Sizing: risk-based (fixed ticks at stop); small initial size because of untested rules; cap contracts at a fraction of top-of-book depth.

Execution: passive limit entries at levels (risk of adverse fills; log fill-conditional markouts); stops as stop-market or stop-limit with slippage assumption; avoid trading in the first seconds after scheduled news.

Costs: exchange and clearing fees, commission, half-spread for market exits, slippage on stops (at least 1-2 ticks in fast markets), data fees; latency distribution measured from your own infrastructure.

Pseudo-code:
```
build_profile(prior_session): volume_at_price -> POC, VAH, VAL (expand from POC until 70% of volume)
on 30-min bracket close b in {A,B}:
  if open < VAL or open > VAH: track excursions
  if two consecutive brackets closed inside [VAL,VAH] and confirm(delta, OFI):
     direction = toward opposite edge ; entry = bracket close
     stop = excursion_extreme +/- buffer ; target = opposite edge ; scale 50% at POC
risk: max loss/day, max trades/day, no trade within 2 min of scheduled news
```

## 9. Backtest plan

- Reproduce profile construction deterministically (bin size, rounding, RTH session) and publish the definitions before testing; freeze them.
- Step 1 is a descriptive study, not a strategy: for 5-10 years of one or two liquid futures, measure the unconditional far-edge completion frequency for the 80 percent setup, the baseline from random-edge placebos, and OFI predictive R-squared versus horizon (1 s to 5 min) in rolling out-of-sample windows. Only proceed if the descriptive edge exists.
- Step 2: trade simulation with tick replay, latency, queue-position for passive entries, stop slippage; walk-forward with parameter choice on training windows and an untouched final hold-out.
- Multiple-testing control: log every definition choice (VA percent, bracket length, bin size, thresholds); deflated Sharpe, SPA/reality check, and Benjamini-Hochberg for the many pattern tests; any discretionary footprint pattern must be coded rigidly before testing.
- Trade-sign robustness: rerun with a deliberately noisier classifier (tick rule) to see sensitivity.
- Metrics: setup frequency, completion rate with confidence interval, expectancy per trade in ticks net of costs, payoff ratio, Sharpe, drawdown, time in market, markout of passive fills, regime split (balanced vs trend days), turnover.

## 10. Risk management and kill-switch

- Max loss per trade in ticks fixed in advance; no widening of stops; max 2-3 setups per day; daily loss limit.
- Auto-disable profile fades on days flagged as directional (open outside value and no re-entry by the second bracket, or IB extension beyond a set multiple).
- Data kill-switch: stop if feed gaps, timestamps jump, aggressor-flag ratio changes abnormally (sign of feed/classification fault).
- Strategy kill: stop trading a rule if live net expectancy over 100 trades is below zero with statistical confidence, or fill markouts are consistently negative (adverse selection).
- Restrict leverage while the rules are unvalidated; paper trade first.

## 11. Annotated sources

| # | Source | Type | Grade | Note |
|---|---|---|---|---|
| 1 | Cont, Kukanov, Stoikov, The Price Impact of Order Book Events https://arxiv.org/abs/1011.6402 (full text via https://arxiv.org/html/1011.6402v3) | Paper (JFEC 2014) | A | Full text read; strongest evidence here but contemporaneous, one month, 50 stocks |
| 2 | Cont, Cucuringu, Zhang, Cross-Impact of OFI https://arxiv.org/pdf/2112.13213 | Preprint | B+ (was B) | Full text read; contemporaneous R-squared high, one-minute forecast R-squared slightly negative, PnL ignores costs |
| 3 | Lipton, Pesavento, Sotiropoulos https://arxiv.org/abs/1312.0514 | Preprint | B | Abstract only; no numbers seen |
| 4 | Bugaenko, Market impact conditional on OFI https://arxiv.org/abs/2004.08290 | Preprint | C | Single-author, abstract only |
| 5 | Andersen and Bondarenko, VPIN and the Flash Crash (full text, Aarhus mirror) https://repec.econ.au.dk/repec/creates/rp/11/rp11_50.pdf ; Easley et al. 2012 and comment https://papers.ssrn.com/abstract=2062450 (not opened) | Paper / dispute | B | Critique read in full; original paper and rejoinder not read this pass; contested |
| 6 | Lee-Ready accuracy literature (Theissen 2001 https://ideas.repec.org/a/eee/intfin/v11y2001i2p147-165.html; other tests via search summary) | Papers | B | Unchanged: not re-verified in the second pass |
| 7 | Market Profile overview https://en.wikipedia.org/wiki/Market_profile and ATAS explainer https://atas.net/blog/how-to-improve-trading-using-the-market-profile/ | Encyclopedic / vendor | C | Descriptions, no tests; vendor bias |
| 8 | MarketCalls, 80 percent rule article https://www.marketcalls.in/market-profile/market-profile-how-to-play-80-percentage-rule.html | Educational | C | Rules only; says no stats or stop given |
| 9 | NexusFi 80 percent rule thread https://nexusfi.com/a/concepts/80-percent-rule | Forum | C | Fetch blocked; forum completion rates seen via search snippet |
| 10 | CQG Market Profile Value Areas primer https://news.cqg.com/workspaces/2026/06/cqg-primer-market-profile-value-areas-mpva | Vendor | C | Shows 68 vs 70 percent definitional variation |
| 11 | Valentini profile summaries https://blog.pickmytrade.trade/fabio-valentini-pro-scalper-nasdaq-scalping-strategy/ | Blog | C | Secondary, return claim unverified |
| 12 | Dalton, Mind Over Markets (1990); Steidlmayer materials | Books | n/a | Not read; cited only as secondary attributions |
| 13 | Kolm, Turiel, Westray, Deep order flow imbalance (Math. Finance 2023) https://ideas.repec.org/a/bla/mathfi/v33y2023i4p1044-1081.html | Paper | B | Abstract only (RePEc page); body not read |
| 14 | Own sanity check, scripts and yfinance 5-minute data (60 sessions, 12 tickers), section 5 | Own computation | D (illustrative) | Small sample, approximated volume profile; not evidence |
| 15 | Searches for CME Market Profile education, open-source value-area backtests, theses | Negative result | n/a | Nothing usable found; only vendor/forum/Pine-script material, search snippets only |

Thin spots (still true after the second pass): no primary trader interview with transcript on footprints, no book read (Dalton and Steidlmayer material not obtained), no CME education text, and no independent audited test of profile or footprint rules. Treat sections 4a-4d as descriptions of folklore, not validated rules.

## 12. Open questions

1. What is the actual far-edge completion rate and expectancy of the 80 percent setup across instruments and decades, relative to random-edge placebos?
2. Does the 80 percent label come from any documented sample? (Primary check of the Profile Reports / Mind Over Markets is still needed; not obtained in the second pass.) A 60-session ETF/megacap check found about 46 percent far-edge completion, no better than the mirror placebo.
3. Is delta/CVD divergence predictive beyond OFI and returns, once trade-sign errors are controlled?
4. Do HVN/LVN levels differ from equal-width random zones in speed of traversal or reversal probability?
5. What is the minimum latency and fee structure at which OFI-timed entries have positive net expectancy? (Cont-Cucuringu-Zhang's one-minute forecast R-squared is negative and its PnL ignores costs, so even the gross edge at one minute is doubtful; seconds-scale tests are needed.)
6. Does VPIN or any toxicity measure add out-of-sample value beyond realized volatility and spreads?

## Second-pass changelog

Date: 2026-10-07. What changed and why:
- Cont-Kukanov-Stoikov upgraded from abstract level to full text: concrete sample (one month, 50 stocks), R-squared numbers (OFI 65 percent versus trade imbalance 32 percent, volume 23 percent for absolute changes) and the authors' own caveats added. Key correction: the evidence is contemporaneous explanation, not forecasting.
- Cont-Cucuringu-Zhang read in full: high contemporaneous R-squared but slightly negative one-minute out-of-sample R-squared and a cost-free PnL; the first-pass wording that cross-asset OFIs help forecasting is now qualified. Grade B to B+.
- Andersen-Bondarenko critique read in full text; specific findings listed. The Easley et al. originals and rejoinder were not read, so I lean towards the critique but keep the dispute labelled unresolved; VPIN treated as unproven.
- Kolm-Turiel-Westray located (abstract level only) and noted; no net-of-cost result known.
- Added an own small check of an 80-percent-style value-area setup (section 5): 140 setups, 46.4 percent far-edge completion versus 52.9 percent for a mirror placebo, 2:1 payoff mostly stopped; heavily caveated, approximated volume profile, one quarter.
- Negative results: no CME Market Profile education text, no academic or audited open-source value-area/POC test, and no footprint/delta test found despite additional searches; no Dalton or Steidlmayer text obtained. Trader interviews/podcast transcripts not found this pass.
- Not changed: Lee-Ready accuracy numbers (still secondary), Valentini claims (still unverified), all section 7 twists (still untested hypotheses).
