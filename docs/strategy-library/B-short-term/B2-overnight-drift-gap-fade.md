# B2. Overnight Drift and Gap Fade

Status: research dossier, written 2026-10-07; second pass 2026-10-07 (section 13 lists changes). Research only, not investment advice. Section 7 twists are hypotheses I have NOT backtested; section 5 now includes my own plain-vanilla SPY reproduction of the overnight split and a simple index gap fade, which is not any of the twists. "Read" = I read the document text; "snippet" = only a search-result abstract or summary, so second-hand.

## 1. Summary, horizon, asset class, holding period

Two related ideas about splitting the close-to-close return into its overnight (close-to-open) and intraday (open-to-close) parts.

(a) Overnight drift: a large share of US equity-index returns accrues while the cash market is closed, so "buy the close, sell the open" looks far better than "buy the open, sell the close." Variants range from the whole overnight window in SPY to a narrow 2:00 to 3:00 a.m. ET window in E-mini futures.
(b) Gap fade: open-to-close trading that bets an opening price gap partially reverses during the session, especially for no-news, high-attention stocks.

Horizon: overnight (about 17.5 hours) to intraday (hours). Assets: US equity index ETFs/futures for (a); single stocks for (b). Holding period: one night or one session.

Critical headline: the overnight effect is well documented and appears in the academic record, but implementing it as a daily round trip is a cost-drag trade that independent tests say is wiped out after costs, and the narrow futures-window version has reportedly vanished since publication. Gap fading has almost no peer-reviewed support as a stand-alone profitable rule; the academic evidence supports reversal of overnight moves in specific stocks, not a generic "gaps fill" edge. Second-pass check on SPY (1993 to 2026, section 5): gross, the overnight/intraday split is still large (overnight CAGR 10.1% vs intraday 0.7%) and has not vanished post-2015 (8.9% overnight), but 1 bp per side cuts the overnight CAGR to 4.7% and 5 bp per side makes it deeply negative; and an index-level open-gap fade earns about zero gross (t below 1 for every threshold) and loses at 5 bp per side.

## 2. Origin and who uses it

- Cliff, Cooper and Gulen (working paper dated July 2007, "Return Differences between Trading and Non-trading Hours: Like Night and Day"): decompose returns using transaction-level intraday data for 1993 to 2006 into night (16:00 to 09:30), 09:30 to 10:30, mid-day, and 15:00 to 16:00. Second pass: I read the CXO Advisory summary of the paper (secondary; the SSRN page was blocked, so the paper itself is not read). Per that summary: average overnight return for individual S&P 500 stocks about 0.028% to 0.048% a day depending on averaging method vs daytime about -0.028% to +0.002%; overnight-minus-daytime spread about 0.068% for SPY, 0.061% for DIA and 0.18% for QQQQ; daytime returns negative for 12 of 14 ETFs; the first trading hour is the weakest. The summary says the authors tested and rejected earnings-announcement timing, ECN growth and decimalisation as explanations and found overnight returns less volatile than daytime ones. It says nothing about transaction costs. A co-author is quoted in a news item suggesting active after-hours trading by hedge funds; treat that as speculation. A later ETF study (Monteiro and Manso 2016, per a search summary I did not open) reportedly finds the effect fell sharply or vanished from about 2006; unverified.
- Kelly and Clark (2011, J. Asset Management, snippet) report the same pattern.
- Berkman, Koch, Tuttle and Zhang (2012 JFQA 47(4):715-741, "Paying Attention: Overnight Returns and the Hidden Cost of Buying at the Open"): overnight gains reverse during the trading day; concentrated in attention-grabbing, hard-to-value, costly-to-arbitrage stocks and stronger when retail sentiment is high; the 3,000 largest US stocks 1996 to 2008; retail buyers of high-attention stocks near the open pay implicit costs that often exceed the effective half spread. Second pass: I opened the Missouri State repository record and read the abstract (full text not obtained: the KU ScholarWorks PDF link returned only an app shell, and Cambridge shows the abstract only). The +10 bps overnight and -7 bps intraday daily means come from the earlier search summary and are not confirmed by anything I could open.
- Lou, Polk and Skouras (2019 JFE, read): the "tug of war" between overnight and intraday clienteles.
- Aboody, Even-Tov, Lehavy and Trueman (2018 JFQA, read): overnight returns as a firm-level sentiment measure.
- Hendershott, Livdan and Rosch (2020 JFE, snippet): beta is rewarded overnight and not intraday.
- Bogousslavsky (2021 JFE, snippet): arbitrageurs reduce positions before the close because of overnight margin and lending costs, which depresses late-day prices.
- Boyarchenko, Larsen and Whelan (2023 RFS, "The Overnight Drift"): dealer inventory explanation for returns in the 2:00 to 3:00 a.m. ET window. A July 2026 NY Fed Liberty Street post (read) shows it faded after 2020.
- Product: two "NightShares" ETFs launched in 2022 to capture overnight returns closed after about 14 months (Liberty Street post and an Elm Wealth note, both read).
- Retail/blog gap-fade: Trade Ideas-style playbooks (the daytradingtoolkit page, read, carries sponsored and affiliate links).
- Related academic context: the Lucca-Moench pre-FOMC drift is a cousin (not covered here).

## 3. Economic rationale and who is on the other side

- Clientele / tug of war (Lou-Polk-Skouras). Different investors trade at different times. Retail and some momentum-style traders are active near the open; institutions trade during the day and close. A stock pushed up overnight by one clientele tends to be pushed back intraday by the other. The authors infer strategy profits split into overnight and intraday pieces, often with opposite signs.
- Attention and sentiment (Berkman, Aboody). Retail buying near the open of attention stocks pushes opening prices high relative to later prices; Aboody finds overnight returns persist for weeks (next-week overnight return spread between top and bottom deciles about 1.76 percentage points, falling to 1.21 by week 4, in their 1992 to 2013 data) while long-run returns reverse. The other side of the opening trade is the retail buyer paying a high opening price (Berkman estimate their added cost often exceeds the effective half spread).
- Inventory risk and dealer capacity (Boyarchenko et al.). Market selloffs generate robust positive overnight reversals; dealers who absorbed unbalanced end-of-day flow are paid as overseas buyers arrive. The other side is the end-of-day forced or impatient seller.
- Risk and funding. Elm Wealth lists risk, frictions and funding costs as candidate explanations and notes the effect is largely unexplained after 15+ years. Bogousslavsky's mechanism (overnight margin and borrowing costs push arbitrageurs out before the close) is a plausible supply-side story.
- Honest note: none of these explanations is settled, and several (retail attention) imply the edge is largest in small, hard-to-value stocks where costs are highest.

## 4. Canonical rules

A. Overnight drift (index):
- Buy SPY (or an index future) at the closing auction; sell at the next day's open (MOO). Hold zero intraday.
- Variant: hold only after down days or after high closing order imbalance (Boyarchenko suggests imbalance-driven reversals; rule not tested by me).
- Variant (futures): hold E-mini from about 2:00 to 3:00 a.m. ET only. This is the exact Boyarchenko window.

B. Gap fade (single stocks, discretionary-to-systematic):
- Universe: liquid stocks, price above $10, average dollar volume above $20 million.
- Gap = open / prior close - 1; gap-up above threshold (for example 1% to 3%, or a multiple of ATR) with no scheduled catalyst (no earnings, no 8-K, no analyst action) and thin pre-market volume.
- Short after price fails to hold the pre-market high or breaks the opening-range low (first 15 to 30 minutes), stop above the opening-range high, scale out near the midpoint of the gap, final target the prior close, invalidate if price reclaims and holds above the opening-range high. Mirror for gap-down. (Rule structure from the daytradingtoolkit page, read; it gives no statistics.)

## 5. Evidence

Peer-reviewed (P), working paper (W), practitioner/vendor (V), unverified (U).

- (P, read) Lou-Polk-Skouras: 14 trading strategies decomposed; the four momentum variants (price, industry, earnings, time-series) and short-term reversal earn their premia overnight; nine others (value, profitability, investment, beta, idiosyncratic volatility, issuance, accruals, turnover, and a marginally insignificant size) earn it intraday; overnight and intraday components typically have opposite signs. Firm-level: value-weight decile spread on past overnight return has three-factor overnight alpha +3.47% per month and intraday alpha -3.02% per month; the equivalent on past intraday return gives intraday alpha +2.41% and overnight alpha -1.77%. The patterns persist when signals are lagged up to 60 months. The authors explicitly warn that transaction costs will make trading these patterns much less attractive, and the results are stronger for large-cap, high-price stocks per the working-paper abstract.
- (P, read) Aboody et al.: described above; sample about 1992 to 2013.
- (P, abstract read, full text not obtained) Berkman et al. 2012: 3,000 largest stocks 1996 to 2008; overnight rise then intraday reversal, concentrated in high-attention stocks. The +10 bps and -7 bps daily figures remain unconfirmed (search-summary only).
- (P, snippet) Hendershott et al., Bogousslavsky: see above.
- (P + Fed, read) Boyarchenko et al. / Liberty Street 2026: 1998 to 2020 the 2:00 to 3:00 a.m. window gave roughly 3.7% per annum, more than 60% of the E-mini's 5.9% annualised close-to-close return, 5,691 trading days. For January 2021 to December 2025 (1,245 days) it averaged close to zero in ES, NQ and YM. The authors attribute this mostly to a drop in dispersion of end-of-day order imbalance (standard deviation of relative signed volume from 6.5% to 2.9%), not to a change in VIX (19.4 vs 20.4) or overnight volume share (15% to 16%). Their prediction that the drift returns if imbalance dispersion widens is untested. The explanation rests on proxies.
- (V, read) QuantConnect strategy-library note: SPY buy-close/sell-open; the author says the gains disappear after costs; Interactive Brokers fee model gave fees of almost 25% of starting capital over a 20-year backtest. No dates or performance table were given.
- (V, read) Elm Wealth (2025): $1 in SPY over 30 years grows to $17.27 overnight vs $1.20 open-to-close; five years of 23 high-volatility, retail-popular stocks and ETFs show average growth of $1 of 31.7 overnight vs 0.8 daytime. The authors themselves say transaction costs including market impact would erase most or all of the gain. The stock list came from a ChatGPT-generated list filtered for volatility above 3%, which is a selection concern; the gross numbers are not net-of-cost.
- (V, full text read on second pass via a Nimble extract; WebFetch got 403) Alpha Architect / State Street Global Advisors (Bartolini, 16 June 2020): SPY, January 1993 to January 2020, close-to-open vs open-to-close, price returns only. Cumulative price return 717% overnight, 627% buy-and-hold, 12% intraday. Overnight beat intraday on only 53% of about 6,800 days; median day +0.05% overnight vs -0.04% intraday; paired t-test of overnight minus intraday t=1.90, p=0.06 (not significant at 5%); overnight kurtosis 17.7. After the dot-com bust (cut at 31 December 2002) the overnight strategy beat buy-and-hold in only 34% (rolling 1-year) and 32% (3-year) of windows vs 64% and 61% before. In earnings-heavy months the overnight-minus-intraday spread is bigger (t=2.1, p=0.03 over the whole sample) but not significant post Reg FD. Costs: using the historical daily bid-ask plus $0.01 a share commission, the all-days overnight strategy goes from +717% to -32% cumulative (earnings-heavy months: +177% to +12%). Single-author practitioner piece by an ETF-issuer employee; figures as given, not independently reproduced, though my own run below agrees on direction.
- (V, snippet only, 404 on fetch) An Efalken substack post argues the anomaly weakened after about 2009. Unverified.
- (V/U) Gap-fill statistics on broker blogs: one claims large gaps (above 1.2x the 14-day ATR) fill the same day only about 8% of the time in E-mini S&P futures 2014 to 2024; another claims about 60% of opening gaps fill on the day. Sources are unnamed; I treat them as unverified and mutually inconsistent.
- (V, read) Trade That Swing (Cory Mitchell) on SPY, using Edgeful statistics over a rolling last six months, snapshots dated August 2025 to October 2026: a "fill" means price touches the prior close during the session. Gaps of 0 to 0.19% fill 62% to 92% of the time, 0.2% to 0.39% fill 45% to 79%, and gaps above 0.4% fill at lower-bound rates of roughly 25% to 50%; the snapshots move a lot from one update to the next and no sample size is disclosed. Named data vendor, window and definition, but not auditable, and a fill is not a profitable trade.
- (U, search snippets only; ResearchGate and Taylor & Francis returned 403) Three academic-style gap papers exist: a DJIA-stocks intraday study reportedly finding 68.2% of up-gaps and 75.2% of down-gaps closed in-session but only 16.3% of down-gaps of 2% or more; "Price gap anomaly in the US stock market: the whole story" reportedly finding about 20% of gaps filled within five days; "Price gaps: another market anomaly?" (Taylor & Francis). I could not open any of them, so these figures are unverified leads, and the first two do not agree on what fraction of gaps fill (different horizons and gap definitions).

Own reproduction on SPY (second pass; Python, scripts and data in the session scratchpad, not in the repo)
- Data and definitions: Yahoo Finance daily SPY via yfinance, dividend-adjusted open and close (so ex-dividend days sit in the overnight leg), 29 January 1993 to 30 September 2026, 8,475 days. "Overnight" = adjusted open over previous adjusted close; "intraday" = adjusted close over adjusted open. Costs are flat per side: 0, 1 and 5 bp. Yahoo's open is a consolidated-feed print I cannot verify as an auction fill, so overnight rows are optimistic about getting the open print.
- Overnight vs intraday (SPY, full sample): mean daily overnight 4.03 bp vs intraday 0.73 bp. Gross CAGR: overnight-only 10.06% (Sharpe with rf=0 of 0.96, max drawdown -32.8%), intraday-only 0.69% (Sharpe 0.12, drawdown -68.5%), close-to-close buy-and-hold 10.83% (Sharpe 0.65, drawdown -55.2%). Sub-periods, overnight gross CAGR: 13.31% (Sharpe 1.51) 1993 to 2006, 6.23% (0.55) 2007 to 2014, 8.93% (0.81) 2015 to 2026. Net of costs: 1 bp per side gives 4.65% CAGR (Sharpe 0.48, drawdown -38.9%), 5 bp per side gives -14.46% CAGR (Sharpe -1.42, drawdown -99.5%). So the split is real in SPY and survived 2015 to 2026 gross, but the daily round trip is eaten by anything above about 1 to 2 bp per side, agreeing in direction with Alpha Architect and QuantConnect.
- Index gap fade (short gap-up, long gap-down at the open, exit at the close; one trade per qualifying day): gap above 0.25%: 4,558 trades (54% of days), gross mean -0.2 bp per trade (t -0.09), 49% hit; at 1 bp per side -2.2 bp; at 5 bp per side -10.2 bp (t -6.1). Gap above 0.5%: 2,297 trades, gross -1.9 bp (t -0.69), 5 bp per side -11.9 bp (t -4.3). Gap above 1.0%: 727 trades, gross -2.7 bp (t -0.40), 5 bp per side -12.7 bp (t -1.9). By period the gross fade made +4.8 to +9.9 bp per trade in 1993 to 2006 (t 1.4 to 1.75), lost 6 to 18 bp in 2007 to 2014 (t about -1.4 to -1.8), and was about zero in 2015 to 2026. Same-session fills (price touches the prior close): gap above 0.25% filled 51% (up) and 54% (down); above 0.5% 42% and 44%; above 1.0% 30% and 40%. Asymmetry: after a gap above 1.0% the mean intraday move was +16.9 bp after gap-ups (continuation, so a fade loses) and +10.9 bp after gap-downs (bounce, so a fade wins), consistent with SPY's upward drift; these are means over 355 and 372 events and I did not test them.
- Caveats (heavy): SPY only (an index, not the single-name attention stocks where Berkman and Aboody locate the reversal); flat cost assumptions; no pre-market or news filter, so this is the generic gap fade the section 1 headline says has no support, not twist 1; thresholds were fixed ahead (0.25%, 0.5%, 1.0%) and all were reported; fill rates depend heavily on gap definition and size; Yahoo opens are consolidated-feed prints that nobody can reliably trade at.
- Absence of evidence: I found no peer-reviewed paper that backtests a tradable gap-fade rule with costs. The daytradingtoolkit page names Berkman, Aboody and Akbas et al. as support but supplies no numbers.

Post-publication decay: for the narrow futures window, the evidence above shows an apparent disappearance. For the broad SPY overnight/intraday split, Alpha Architect (read) finds the overnight advantage much less persistent after the dot-com bust, and my own run shows a weaker 2007 to 2014 (6.2% gross CAGR) but a partial recovery in 2015 to 2026 (8.9%), so "vanished" is not supported for SPY gross; it is the net-of-cost version that has no edge. The McLean-Pontiff prior (working paper, read: about 35% average post-publication decay across 82 characteristics; published version about 58% across 97, snippet) is a reasonable baseline.

## 6. Failure regimes and risks

- Costs: a daily round trip at the close and the open pays two auctions per day, about 500 trades a year; any edge under a few bps per side vanishes.
- Gap risk: you carry overnight event risk (earnings, geopolitical, macro) without being able to react; sizing must reflect that the overnight variance is not small.
- Regime dependence: the Boyarchenko drift needs dispersed, large end-of-day imbalances; when they shrink (2021 to 2025) it disappears.
- Gap-fade failure: news-driven gaps continue (PEAD, see B3); strong trend days; short squeezes and borrow constraints on small caps.
- Cross-effects: overnight persistence (Aboody) means a stock with a large gap tends to keep gapping over the next days even while reversing intraday. A naive fade of the gap-up stock can be right intraday and wrong overnight.
- Crowding/timing: a published effect with cheap vehicles (ETFs) attracts flow, then closure of the vehicle (NightShares).
- Data: open prices on the primary-exchange auction vs consolidated first print differ; backtests that use consolidated "open" fill unrealistically.

## 7. MY TWIST (hypotheses, NOT backtested)

Twist 1: Attention-filtered, market-neutral gap fade.
- Rationale: Berkman and Aboody indicate reversal is strongest in high-attention, hard-to-value stocks; a generic gap fade mixes in news-driven gaps that continue.
- Rule: universe = top 1,500 US stocks by dollar volume. Each day compute gap, pre-market volume relative to 20-day average, a news flag (earnings, 8-K, press release, analyst action in the last 24 hours), and a retail attention proxy (for example abnormal retail-proxied volume or social/Google-trend rank, proxy to be specified). Enter short at 10:00 (not at the open) on gap-ups above 2% with no news flag, high attention proxy, and pre-market volume under 1.5x normal; hold to 15:55. Long side mirrors gap-downs. Dollar-neutral, equal-weight, max 40 names per side.
- Parameters: gap threshold {1%, 2%, 3%}; entry time {open, 09:45, 10:00, 10:30}; attention quantile {top 20%, top 33%}; exit {close, VWAP touch, 13:00}.
- Expected effect: positive gross intraday alpha of a few bps per name per day concentrated in the no-news, high-attention subset; likely eaten by costs for small names, so net edge, if any, in the top 500.
- Falsification: reject if, over the untouched final third of the data, the net-of-cost Sharpe of the filtered strategy is below 0.5 or not better than the unfiltered fade at p<0.10 after multiple-testing correction, or if the subset's edge disappears when restricted to the top 500 names.

Twist 2: Tug-of-war pair: own overnight, fade intraday, in large caps.
- Rationale: Aboody's overnight persistence plus Lou-Polk-Skouras's opposite intraday sign suggests stocks with strong recent overnight returns continue overnight and reverse intraday.
- Rule: each day at the close rank stocks by trailing 5-day cumulative overnight return; go long the top decile at the close, exit at the next open (overnight leg); at the open go short the same top decile and cover at the close (intraday leg), and do the reverse for the bottom decile. Run overnight-only, intraday-only, and combined versions. Universe: top 500 by market cap.
- Parameters: lookback {1, 5, 20 days}; decile vs quintile; sector-neutralise yes/no.
- Expected effect: positive in gross terms because it mirrors documented patterns, but turnover is 100% daily; the question is whether anything survives costs in large caps.
- Falsification: reject if net Sharpe (costs at least 5 bps per side per leg) is not positive with t>2 in the 2013 to 2026 out-of-sample period, or if the gross edge in the top 500 is below 2x round-trip cost.

Twist 3: Imbalance-conditioned index overnight hold (futures).
- Rationale: Boyarchenko's drift is explained by end-of-day imbalance times variance divided by dealer capacity; the drift faded as imbalance dispersion fell.
- Rule: hold ES/MES from the close to the next open only when (a) the S&P fell on the day and (b) a proxy for closing sell imbalance (published NYSE/Nasdaq closing imbalance feed, or signed volume in the last 30 minutes) is in the bottom decile of its trailing 3-year range; otherwise flat.
- Parameters: down-day threshold {-0.5%, -1%}; imbalance percentile {10, 20}; window {close to open, 2:00 to 3:00 a.m.}.
- Expected effect: a few trades a month with higher conditional expectation than the unconditional overnight return; low frequency also reduces cost drag.
- Falsification: reject if the conditional overnight return is not significantly above the unconditional one (t<2, block bootstrap) in 2021 to 2026 data, or if fewer than 40 qualifying events exist (insufficient power, record as inconclusive).

## 8. Implementation spec

Data: tick or 1-minute bars with auction prints; official opening and closing auction prices for each primary exchange; corporate actions; earnings calendar and news timestamps; pre-market volume; closing imbalance feeds (NYSE, Nasdaq) if available; borrow availability and fees; futures data (ES/MES, NQ, YM) with 24-hour sessions.
Signals: described per twist. Compute returns using auction prices for overnight legs; never mix consolidated and primary prints.
Sizing: overnight index: fixed vol target (for example 10% annualised, scale by trailing 20-day overnight vol); stock fade: equal dollar risk with 1R = distance to the stop; per-name cap 0.5% of NAV; gross cap 2x.
Execution: MOC and MOO/LOO orders for overnight legs; marketable limits within the first minutes for gap fades; avoid the first 5 minutes for illiquid names.
Stops: gap fade: stop above opening-range high (cap loss 1R); time stop at 15:55; index overnight: no stop but size to a worst-case gap of 3x average overnight move.
Costs: ETFs: 1 bp half-spread each auction plus commission; futures: 0.5 tick plus fee; stocks top 500: 3 to 6 bps per side plus impact; small caps higher; borrow 25 to 500 bps annualised, with hard-to-borrow names excluded; stress at 2x.

Pseudo-code (gap fade):
```
for each stock s at 10:00:
  gap = open[s]/close_prev[s]-1
  if gap>g and not news[s] and attn[s]>q and premkt_vol[s]<1.5*norm[s] and open_range_broken_down[s]:
      short(s, size=risk_size(s, stop=orh[s]))   # exits: stop, 13:00 optional, 15:55
```

## 9. Backtest plan

- Data: 2003 to 2026; index overnight tested separately from 1993 for context but evaluated mainly post-2010; stocks tested with point-in-time universe and delistings.
- Walk-forward: freeze design on 2003 to 2012; validate 2013 to 2019; hold out 2020 to 2026 untouched. Report sub-period results explicitly because the literature shows regime change (2009 and 2021 for overnight drift).
- Fills: assume auction fills for MOC/MOO; for the intraday fade fill at the next bar's VWAP plus slippage, never at the signal bar's price.
- Multiple testing: log all variants; report deflated Sharpe, Benjamini-Hochberg across the parameter grid, and a placebo test shifting the gap date randomly.
- Controls: compare to unconditional overnight, intraday, and close-to-close; market-neutralise; check performance net of beta.
- Metrics: net Sharpe, annualised net return after costs, hit rate, average win/loss, max drawdown, turnover, cost as percentage of gross P&L, capacity (percentage of auction volume), P&L by market cap, by year, by event type (news vs no news).

## 10. Risk management and kill-switch rules

- Overnight exposure limit: gross overnight exposure no more than a fixed multiple of daily vol target; no overnight positions through scheduled binary events (FOMC, CPI, earnings of held names) unless the strategy is designed for them.
- Kill-switches (my thresholds): (1) stop trading the overnight strategy if the trailing 12-month net return is negative and cost-to-gross P&L ratio exceeds 80%; (2) halt the gap fade if the trailing 60-day hit rate drops below 45% together with average loss above 1.2R; (3) halt if the closing-auction share of volume changes structurally (exchange rule changes) until fills are re-verified; (4) hard daily loss limit of 1.5% of NAV; (5) hard borrow-fee or recall limit: exit any short with fee above 300 bps or recall notice.
- Data-integrity guard: stop if auction price feed latency or missing prints exceed a set count per day.

## 11. Annotated sources

| # | Source | URL | Type | Grade | Read? |
|---|---|---|---|---|---|
| 1 | Lou, Polk, Skouras (JFE 2019) | https://personal.lse.ac.uk/polk/research/TugOfWar.pdf | Peer-reviewed | A | Read |
| 2 | Aboody et al. (JFQA 2018) | https://anderson-review.ucla.edu/wp-content/uploads/2021/03/Aboody-et-al_overnight_returns_and_firmspecific_investor_sentiment_JFQA2018.pdf | Peer-reviewed | A | Read |
| 3 | Berkman, Koch, Tuttle, Zhang (JFQA 2012) | https://bearworks.missouristate.edu/articles-cob/576 | Peer-reviewed | A | Abstract read; full text not obtained (KU PDF link returned an empty app shell, Cambridge abstract-only) |
| 4 | Boyarchenko, Larsen, Whelan (RFS 2023) and NY Fed SR 917 | https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr917.pdf | Peer-reviewed / Fed paper | A | Snippet |
| 5 | NY Fed Liberty Street, "The Disappearing Overnight Drift" (July 2026) | https://libertystreeteconomics.newyorkfed.org/2026/07/the-disappearing-overnight-drift/ | Central-bank blog by authors | B+ | Read |
| 6 | Hendershott, Livdan, Rosch (JFE 2020) | https://ideas.repec.org/a/eee/jfinec/v138y2020i3p635-662.html | Peer-reviewed | A | Snippet |
| 7 | Bogousslavsky (JFE 2021) | https://ideas.repec.org/a/eee/jfinec/v141y2021i1p172-194.html | Peer-reviewed | A | Snippet |
| 8 | Cliff, Cooper, Gulen (working paper, July 2007) via CXO Advisory summary; Kelly-Clark (2011) | https://www.cxoadvisory.com/?p=1377 ; https://ideas.repec.org/a/pal/assmgt/v12y2011i2d10.1057_jam.2011.2.html | WP (via secondary summary) / journal | B- (paper not read; summary read) / B (Kelly-Clark, snippet) | CXO summary read; paper blocked (SSRN) and Kelly-Clark restricted |
| 9 | QuantConnect overnight anomaly | https://www.quantconnect.com/tutorials/strategy-library/overnight-anomaly | Vendor | C+ | Read |
| 10 | Elm Wealth, Night Shift (2025) | https://elmwealth.com/night-shift/ | Practitioner note | C+ | Read |
| 11 | Alpha Architect, trading costs and overnight anomaly (2020) | https://alphaarchitect.com/trading-costs-wipe-out-the-overnight-return-anomaly/ | Practitioner (ETF-issuer author) | B | Read in full (via Nimble extract; WebFetch 403) |
| 12 | daytradingtoolkit gap fade page | https://daytradingtoolkit.com/strategies/gap-fill-gap-fade-strategy | Vendor/affiliate | C | Read |
| 13 | Broker-blog gap-fill statistics (VT Markets, tastylive, etc.) | https://www.vtmarkets.com/en-eu/discover/gap-trading-overnight-price-gaps-in-shares-indices/ | Vendor blog | C- | Snippet |
| 14 | Trade That Swing, SPY gap-fill statistics (Edgeful data) | https://tradethatswing.com/sp-500-spy-es-gap-fill-strategy-and-statistics/ | Vendor/blog with named data source, undisclosed n | C | Read |
| 15 | DJIA intraday gap-fill study; "Price gap anomaly in the US stock market: the whole story"; "Price gaps: another market anomaly?" | https://www.researchgate.net/publication/336073716_Filling_Open_Price_Gap_on_Intraday_Timeframe_A_Case_Study_for_DJIA_Index_Stocks ; https://www.researchgate.net/publication/339811620_Price_gap_anomaly_in_the_US_stock_market_The_whole_story ; https://www.tandfonline.com/doi/full/10.1080/10293523.2017.1333563 | Academic-style papers (venues/peer review not verified) | U (leads only) | Not read: 403 on fetch; figures from search snippets |
| 16 | Own SPY reproduction (yfinance daily) | scratchpad, not in repo | Own computation | C+ (single instrument, vendor data, flat costs) | Ran it |
| 17 | McLean and Pontiff working paper (2013) | https://ivey.uwo.ca/media/3775549/pontiff.pdf | Working paper | A- | Read full text (decay prior only) |

## 12. Open questions

1. How much of the overnight premium in single stocks is bid-ask/auction microstructure vs real drift? Auction-based vs consolidated opens may change the answer.
2. Does the overnight pattern in SPY survive after 2021 as the futures window did not? Partly answered gross: my SPY run gives 8.9% gross overnight CAGR for 2015 to 2026 (end September 2026) vs 0.7% full-sample intraday, so it has not disappeared gross; I did not split out 2021 to 2026 separately, and net of even 1 bp per side the return is roughly halved.
3. Is there a net-of-cost, tradable cut (large caps, no-news) of the gap fade at all, or is it only an attention-stock phenomenon in names that are costly to trade?
4. Are the Aboody overnight-persistence spreads (1.76 pp next week) concentrated in microcaps? I did not see a size-split in what I read.
5. What data sources provide a clean, point-in-time news/catalyst flag at the open?
6. Can the Boyarchenko imbalance mechanism be proxied with public closing imbalance data, and does it predict reversals at the stock level?

## 13. Second-pass changelog (2026-10-07)

Read in full this pass: Alpha Architect overnight article (via Nimble extract); Trade That Swing SPY gap-fill page; CXO Advisory summary of Cliff-Cooper-Gulen; McLean-Pontiff working paper (decay prior); Missouri State abstract record for Berkman et al.
Tried and failed: Cliff-Cooper-Gulen paper itself (SSRN blocked, no free PDF found); Berkman et al. full text (KU PDF link returned an app shell; Cambridge abstract only); Kelly-Clark (restricted); ResearchGate and Taylor & Francis gap papers (403); Monteiro-Manso ETF paper (not opened).

Changes:
- Cliff-Cooper-Gulen: upgraded from "snippet" to "secondary summary read": added sample, interval design, per-asset spreads (SPY 0.068%, DIA 0.061%, QQQQ 0.18%), rejected explanations; paper still unread.
- Berkman et al.: abstract now read; the +10 bps/-7 bps daily figures are demoted to unconfirmed.
- Alpha Architect: from "403, snippet only, no numbers" to read in full; added t=1.90/p=0.06 on overnight vs intraday, 53% of days, pre/post-dot-com persistence, Reg FD split, and cost result (+717% to -32%).
- Gap-fill statistics: replaced "unnamed broker blogs" with one named-vendor source (Edgeful via Trade That Swing, undisclosed n) plus three academic-style leads that I could not open; still no gap-fill study with auditable data and methodology that I have actually read. My own SPY run gives same-session touch rates of 51%/54% (gap above 0.25%), 42%/44% (0.5%), 30%/40% (1.0%).
- New own reproduction: SPY overnight vs intraday 1993 to 2026 with 0, 1, 5 bp per side; index gap fade at three thresholds with sub-periods. Headline findings: gross overnight edge persists in SPY (including 2015 to 2026) but dies by 5 bp per side and halves at 1 bp; generic index gap fade is about zero gross and negative net.
- Corrected a prior claim: "pre-2009 data reportedly dominates (U)" replaced by measured sub-periods; the broad SPY effect weakened in 2007 to 2014 but did not vanish gross in 2015 to 2026.
- Source grades: Alpha Architect B- to B; Cliff-Cooper-Gulen B to B- (summary only); Berkman now abstract-read; new rows 14 to 17.
- Unchanged: section 7 twists (still untested; the reproduction does not test attention filters, intraday entry timing or the imbalance-conditioned hold), sections 8 to 10. Boyarchenko et al. (RFS 2023 / NY Fed SR 917), Hendershott et al., Bogousslavsky, Lou-Polk-Skouras, Aboody et al. and the Liberty Street post were not re-read this pass.
