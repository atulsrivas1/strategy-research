# D4. Equity seasonality and event-time effects: pre-FOMC drift, turn-of-month, Halloween, day-of-week

Status: research dossier, not investment advice. Research date: 2026-10-07. Labels: [PR] peer-reviewed, [WP] working paper, [PC] practitioner/blog claim, [UNV] unverified. TWIST sections are hypotheses NOT backtested. Second pass (2026-10-07): [OWN] = my own quick Python recomputation on free data (Ken French daily factors, Yahoo SPY, Fed FOMC calendar pages; caveats in section 5); FT = full text read, abstract = abstract/landing page only.

## 1. Summary, horizon, asset class, holding period

This family exploits calendar or event-time patterns in equity index returns: (a) the pre-FOMC announcement drift (hold the S&P 500 or futures for roughly the 24 hours before scheduled FOMC statements); (b) the turn-of-the-month (TOM) effect (hold the last trading day of a month plus the first three days of the next); (c) the Halloween / "Sell in May" effect (hold equities November-April, hold cash May-October); (d) day-of-week effects (historically weak Mondays). Holding periods range from hours to months; instruments are index futures/ETFs. These are low-capacity, long-only timing overlays that mostly capture the equity risk premium in selected windows, not market-neutral alpha. They are the strategies most exposed to data-mining and decay. My bottom line after the second pass: pre-FOMC drift is documented but contested after 2015 (Kurov et al. say it disappeared; a NY Fed update says it persisted at press-conference meetings through mid-2018; my rough daily-data check finds the FOMC-day close-to-close premium gone after 2015 but a positive overnight leg in 2020-2026) and I would not trade it; the TOM effect is strong in the 1926-2005 data but, in my own recomputation, has vanished since 2006, so it is no longer a profit engine; Halloween is borderline significant over a century (t about 1.8) and costs the equity premium in summer; the day-of-week (Monday) effect is gone.

## 2. Origin and who uses it

- Pre-FOMC: Lucca and Moench (2015), "The Pre-FOMC Announcement Drift", Journal of Finance; NY Fed Staff Report 512 (Sept 2011, rev. Aug 2013) [PR]. Follow-ups: Kurov, Wolfe, Gilbert (2021), "The Disappearing Pre-FOMC Announcement Drift", Finance Research Letters 40 [PR]; Lucca and Moench (Nov 2018), Liberty Street Economics, "The Pre-FOMC Announcement Drift: More Recent Evidence" (opened and read) [WP-level Fed blog]; Boguth et al. (2019), cited via a blog (unread) [UNV]. Theory: Cocoma (JFQA 2026, abstract only) models the drift as a premium for disagreement before announcements [PR, abstract].
- TOM: Lakonishok and Smidt (1988), DJIA 1897-1986 [PR, via secondary summary]; McConnell and Xu (2008) extend through 2006 [PR, via summary]; Ogden (1990) payment-date explanation [PR, via summary].
- Halloween: Bouman and Jacobsen (2002), American Economic Review 92(5) [PR]; Jacobsen and Zhang, "The Halloween Indicator: Everywhere and all the time" (SSRN 2154873) [WP, read].
- Day-of-week: French (1980), Gibbons-Hess (1981) (from memory, [UNV]); later decay evidence: Morey and Rosenberg, Smith and Robins (via search summaries) [PR/WP, unread].
- Users: retail "seasonality" traders, some tactical-allocation funds; bloggers selling "pre-FOMC" filters [PC]. Quantpedia catalogues these as strategies [PC].

## 3. Economic rationale and who is on the other side

- Pre-FOMC: Lucca-Moench find no satisfying explanation. Candidates they discuss: a risk premium (but the announcement-minute return is about zero and volatility/volume are low pre-announcement), reduced participation of inattentive investors (Duffie 2010 slow-moving capital), good-news surprises or "government put" (none fits why the gain accrues only pre-announcement), and informational frictions [PR]. Kurov et al. suggest reduced uncertainty explains the disappearance after 2015 [PR]. Honest reading: unexplained, therefore fragile.
- TOM: month-end cash flows (salaries, pensions, funds' inflows), window dressing; Ogden's payment-dates theory was tested and rejected in tests per the Quantpedia summary [PC]. Counterparties would be forced/institutional flow-driven sellers or demand-insensitive flows.
- Halloween: no accepted theory; proposed vacation-season risk aversion and liquidity (Jacobsen-Zhang note a lack of a proper explanation) [WP].
- Day-of-week: settlement and information-release timing, bad news released on weekends, trader mood; none robust.
Who is on the other side: unclear for all of these. If you cannot name the counterparty and the constraint, the prior should be that it is a statistical artifact or a one-sample feature.

## 4. Canonical rules

1. Pre-FOMC drift (Lucca-Moench): buy S&P 500 (or futures) at the close of the day before a scheduled FOMC announcement and sell right before the announcement (the paper defines the 24 hours before the announcement; since 1994 announcements occur about 2:15pm ET). Only scheduled meetings; unscheduled ones excluded. Before 1994 they use close-to-close returns on days of scheduled meetings.
2. TOM: buy at the close of the day before the last trading day of the month (i.e. hold the last trading day plus the first three trading days of the next month, about four days); exit at the close of day +3. Quantpedia's simple version buys SPY one day before month-end and sells at the third trading day [PC].
3. Halloween: long the equity index from end of October to end of April; cash or T-bills May-October.
4. Day-of-week: avoid or short Monday close-to-close; most studies simply report average returns by weekday.

## 5. Evidence

| Claim | Source (read?) | Sample | Costs | Grade |
|---|---|---|---|---|
| S&P 500 rose on average 49 bp in 24h before scheduled FOMC announcements; about 80% of annual realized excess stock returns since 1994 accounted for by this window; holding only in that window annualized Sharpe above 1.1; no effect in Treasuries; not due to outliers; robust to data-snooping adjustment in their tests; 20 bp on meeting days 1980-1993; no pre-1980 effect; about half of excess returns Jan 1980-Mar 2011 | Lucca-Moench NY Fed SR 512 (read) | Sep 1994-Mar 2011 (main), 1980-2011 | Gross; no transaction cost deduction in the headline | PR |
| Drift tends to be higher when yield curve slope is low and VIX is high; strongly serially correlated | same | same | n/a | PR |
| Verified from the primary text: 49 bp average over the 24 hours before scheduled announcements, t above 4.5; "about 80%" of realized excess stock returns since 1994; Sharpe 1.14 for holding only in that window, where the paper annualizes by 8 times the per-meeting Sharpe (event-time exposure, not calendar time); 20 bp on meeting days 1980-1993 | Lucca-Moench NY Fed SR 512 (FT re-read in second pass) | 1994-Mar 2011 | Gross | PR |
| Drift "essentially vanished" after 2015, both for announcements with and without press conferences; authors suggest reduced uncertainty (VIX decline) | Kurov, Wolfe, Gilbert 2021 (abstract plus search-result snippets only; the Skidmore working-paper PDF now returns a 404 page and SSRN 3134546 returned 403, so the body is still unread) | Sep 1994-Dec 2019 | n/a | PR |
| Contrary/qualifying evidence: after March 2011 the drift persisted only at meetings with a press conference: about 40 bp from the prior day's open to around lunchtime on announcement day, plus roughly 30 bp more by the end of the press conference; no pre-statement excess return at meetings without press conferences; the drift now begins in the morning of the day before; authors suggest arbitrage may be pulling it earlier and note all meetings have press conferences from 2019 | Lucca and Moench, Liberty Street Economics 16 Nov 2018 (opened, read; no t-statistics given) | Apr 2011-Jun 2018 | n/a | WP-level, Fed blog |
| [OWN] Pre-FOMC proxies from daily SPY data (not the 2pm-to-2pm window): close-to-close return on FOMC days minus other days was +34.9 vs +2.8 bp (t 3.15, n=136) in 1994-2010, +28.7 vs +4.4 bp (t 1.21, n=40) in 2011-2015, +3.0 vs +6.3 bp (t -0.27, n=85) in 2016-Sep 2026; the overnight leg (prior close to FOMC-day open) was +16.4 vs +2.9 bp (t 2.71) in 2016-2026, concentrated in 2020-2026 (+23.1 vs +2.7, t 2.71, n=53), while open-to-close on FOMC days was negative (-13.4 bp, t -1.60) | my scripts (scratchpad d2scripts/cal.py) on Yahoo SPY adjusted/unadjusted OHLC and 261 scheduled meeting dates parsed from federalreserve.gov calendar pages (a few cross-month dates patched by hand; unscheduled calls and the March 2020 emergency meeting excluded) | 1994-2026 | none applied | OWN; the overnight t of 2.7 comes from about 15 comparisons I looked at, so it is not significant after multiplicity |
| Claimed profitable "technical filters" still work | TradeMachine Substack | unspecified | none reported | PC, no data, paywalled product |
| TOM: last day plus first three days of month contain almost all of the DJIA's positive returns; persisted 1987-2005 and through 2006 (McConnell-Xu) | Lakonishok-Smidt, McConnell-Xu via secondary summaries | DJIA 1897-1986; CRSP 1987-2005/06 | n/a | PR (unread primary) |
| TOM in U.S. equities 1926-2005 strong enough that, per the authors, there was no market-risk reward outside the turn-of-month days; present in 31 of 35 countries; not confined to small stocks or year/quarter ends; trading volume and fund flows do not explain it | McConnell and Xu, FAJ 64(2) 2008 (CFA Institute page opened: abstract only; paywalled) | 1926-2005; 35 countries | n/a | PR, abstract level |
| [OWN] TOM window (last trading day plus first 3 of next month, about 4 days a month) on the French CRSP value-weighted market: mean 16.3 bp/day vs 1.3 outside (t 7.4) in 1926-1986; 15.7 vs 2.2 (t 3.6) in 1987-2005; 4.2 vs 3.6 (t 0.1) in 2006-2015; 5.1 vs 6.5 (t -0.2) in 2016-2025; whole 1926-2025 13.8 vs 2.2 (t 7.0). SPY gives the same picture: 11.5 vs 2.8 bp (t 1.7) 1993-2005, 4.3 vs 3.5 (t 0.1) 2006-2015, 5.3 vs 6.3 (t -0.2) 2016-2025 | my scripts (d2scripts/cal.py), Ken French daily Mkt-RF plus RF (total market) and SPY adjusted close | 1926-2025 / 1993-2025 | see next row | OWN; t-statistics are Welch tests on daily returns, not clustered, so overstated |
| [OWN] Cost-aware TOM strategy (in market during the window, T-bills otherwise; Sharpe computed on excess returns including idle days) vs buy-and-hold: at 2.5 bp per switch (about 24 switches a year), 1926-2025 Sharpe 0.74 vs 0.46, but 2006-2015 0.14 vs 0.40 and 2016-2025 0.18 vs 0.72; at 10 bp per switch, 1926-2025 0.49 and 2016-2025 -0.05; 1926-2025 annual return 8.3% vs 9.8% buy-and-hold at 2.5 bp (time in market is only about 4/21) | same | same | 2.5 and 10 bp per one-way switch; no taxes | OWN; cash treatment affects the Sharpe comparison |
| [OWN] Halloween (Nov-Apr stock, May-Oct bills) on French monthly market returns: Nov-Apr mean 1.23%/month vs 0.67% May-Oct over 1927-2025 (difference about 3.35% per half-year, t 1.8); by sub-period t 0.5 (1927-1969), 2.0 (1970-1998), 1.0 (1999-2025). Strategy annual return 8.6% vs 10.2% buy-and-hold over 1927-2025 (no costs), 7.1% vs 8.9% over 1999-2025. Dropping Oct 1987 and Aug 1998 leaves 1.23% vs 0.74%/month | same | 1927-2025 | none | OWN; the gap persists but is only borderline significant, and bills in summer lowered the compound return in every sub-period except 1970-1998 |
| [OWN] Day-of-week, French market, mean daily return in bp (se): Monday -17.7 (2.5) in 1926-1969 (that sample includes Saturday sessions), -11.3 (3.6) in 1970-1989, +2.8 (4.2) in 1990-2009, +4.0 (4.3) in 2010-2025; other weekdays +2 to +14 throughout | same | 1926-2025 | n/a | OWN; confirms the Monday effect is gone since 1990 |
| TOM simple strategy: about 0.15% average daily return in the 4-day window, about 7.2%/yr, Sharpe 1.04 (Quantpedia's derived estimate from a source paper; max drawdown figure on the page flagged as unsourced) | Quantpedia (read) | 1926-2005 | No costs/taxes quantified; notes calendar effects tend to weaken or shift | PC, derived numbers |
| Possible decay after publication: one master's thesis finds abnormal TOM returns shrank after Lakonishok-Smidt | search summary | DJIA/S&P | n/a | C (single thesis) |
| Halloween: winter (Nov-Apr) returns higher than summer in 36 of 37 countries; 1970-1998 | Bouman-Jacobsen 2002 (abstract via search; not fully read) | 37 countries, 1970-1998 | n/a | PR |
| Halloween "everywhere": 108 markets, 319 years, 55,425 monthly observations; Nov-Apr exceeds May-Oct by 4.52% (t = 9.69); 6.25% over past 50 years; Sell-in-May strategy beats the market in over 80% of 5-year windows | Jacobsen-Zhang (read abstract/intro) | 108 markets, longest histories | Not net of costs | WP (authors are the effect's main proponents) |
| Skeptics: Maberly-Pierce say Halloween results are driven by outliers (Oct 1987, Aug 1998 LTCM) | Search summary / cited in Jacobsen-Zhang | US | n/a | PR (unread primary) |
| Grimbacher et al.: US premium of 7.2% (1963-2008) when both Halloween and TOM apply vs -2.8% otherwise | footnote in Jacobsen-Zhang | 1963-2008 | n/a | WP (via footnote) |
| Monday effect: dissipated by mid-1990s (Morey-Rosenberg, 1966-2007); Smith-Robins say it disappeared around 1974-75 using CRSP 1926-2014; some find reversals in large caps post-1987 | Search summaries | various | n/a | PR/C, unread |
| Combined walk-forward seasonal/announcement model Sharpe 0.77 on S&P 500 since 1975 | Hull, Bakosova, Kment via Quantpedia | since 1975 | unknown | PC/WP, unread |

Critical assessment:
- Data-mining risk is high. There are dozens of calendar slices (weekday, week of month, month, holidays, FOMC, CPI, payrolls, opex). Each reported anomaly is the survivor of many looks. Harvey-Liu-Zhu argue new discoveries need t-ratios of at least 3.0 because of multiple testing; this applies a fortiori to calendar effects, whose test-family size is unknowable.
- The largest-sample defence (Jacobsen-Zhang, 108 markets) addresses sample selection, but the markets are cross-correlated, the authors are the original proponents, and no transaction costs or taxes are applied. A strategy that sits in cash six months a year sacrifices the equity premium in summer; Bouman-Jacobsen style conclusions rely on summer returns being near zero or negative on average, a statement with wide confidence intervals.
- Second-pass correction to the framing below: the evidence on pre-FOMC after 2011 is contested rather than settled. Kurov et al. (abstract level) say it vanished after 2015; the NY Fed authors' own 2018 update says it persisted at press-conference meetings (about 40 bp, starting earlier, which looks like what a partially arbitraged anomaly would do); my daily proxies show the FOMC-day premium gone in 2016-2026 but a positive overnight leg. Different windows, samples and definitions explain the split, and nobody has shown a tradable net edge after 2015. I treat it as "fragile, possibly relocated, not tradable on current evidence".
- Pre-FOMC is the clearest case of decay: a Fed staff paper's strong in-sample result (Sharpe above 1.1 gross) followed by disappearance after about 2015 per Kurov et al. This pattern (strong paper, then vanishing) is what an anomaly that was a sample feature, or that was arbitraged away after publication, looks like. Also note changing Fed communication (press conferences from 2011) alters the information environment.
- Second pass on TOM: my recomputation reproduces the classic result (about 14-16 bp a day in the window vs about 1-2 outside, t 3.6-7.4 up to 2005) and then shows it gone in 2006-2025 (about 4-5 bp vs 4-7 bp). With roughly 480 window-days per decade the standard error is about 5 bp a day, so the 2006-2025 numbers cannot rule out a modest remaining effect, but they rule out the old magnitude. Combined with the cost-aware rows, a stand-alone TOM trade has no demonstrated post-2005 net edge. This pattern is also what post-publication decay looks like (Lakonishok-Smidt 1988, McConnell-Xu 2006-08), though I cannot separate that from a sample artifact.
- TOM and Halloween have endured longer in academic work, but with no costs, no reliable explanation, and long-only equity beta in the position. A TOM strategy is invested only about 4/21 of the time, so its Sharpe estimates depend on how cash is treated.
- Day-of-week: effectively dead or reversed in modern samples per multiple studies [unread primaries].

## 6. Failure regimes and risks

- Anomaly decay/arbitrage after publication (pre-FOMC: Kurov et al.).
- Regime changes in Fed communication, scheduling (8 meetings/yr), intermeeting actions and QE periods.
- Equity bear markets: all of these are long-only beta strategies; a winning "window" can still lose in a crash (e.g. a Halloween winter containing October-April crashes, TOM windows in 2008 or 2020).
- Overfitting via "filters" (VIX, yield curve, press-conference flags) that raise in-sample Sharpe but reduce sample size to a few dozen events (about 8 meetings a year).
- Costs: futures round-trips every 6 weeks (FOMC) or monthly (TOM) are small per trade (a few bps) but large relative to an edge of 10-50 bps per event once the edge decays.
- Tax: frequent short-term gains for ETF versions.
- Event and timing risk: executing "right before the announcement" requires precision around 2:00-2:15pm ET, auction/liquidity; leakage of earlier information.

## 7. MY TWIST (hypotheses, NOT backtested)

### Twist A: Single pre-registered composite equity-exposure tilt instead of separate trades
- Rationale: testing each calendar effect separately maximizes snooping; one tilt applied to an existing beta position limits degrees of freedom and costs.
- Rule: baseline exposure 100% to broad equity index futures (vol-targeted); add +25% exposure when two of three flags hold (TOM window, Nov-Apr, scheduled FOMC pre-announcement day), subtract 25% when none hold. No stand-alone leverage.
- Parameters (pre-register only these): tilt size {0, 15, 25%}; flag count threshold {1, 2, 3}.
- Expected effect: tiny improvement in Sharpe versus buy-and-hold if the effects are real; roughly zero if not. This is intentionally modest.
- Falsification: if the tilt's excess return versus constant-exposure beta, after 2 bps per trade cost, has a t-statistic below 2 in a held-out period starting after the specification date (use 2016-2025, since pre-FOMC reportedly died in 2015), or fails in at least two of three non-US markets (Europe, Japan, UK), reject and stop.

### Twist B: Treat pre-FOMC as a conditional signal only when uncertainty is high
- Rationale: Lucca-Moench show higher drift when VIX is high and curve slope is low; Kurov et al. propose reduced uncertainty explains disappearance.
- Rule: take the pre-FOMC long only if VIX at the prior close is above its trailing 3-year 75th percentile and the meeting has a press conference; otherwise stay out. Second-pass note: the NY Fed update says every meeting has a press conference from 2019, so the press-conference condition is degenerate after 2018 and the rule reduces to the VIX condition alone; also the NY Fed finds the drift starting the morning of the day before, so the 24-hour entry timing is itself in question.
- Parameters: VIX percentile {60, 75, 90}; trailing window {2, 3, 5 years}.
- Expected effect: a handful of trades per year with an uncertain edge; this is likely dead too, which the test is meant to reveal quickly.
- Falsification: fewer than 30 qualifying events in 2016-2025 means untestable (abandon). Otherwise reject if the mean event return is not positive with a bootstrap 95% interval excluding zero, relative to the same-hour non-event return distribution (placebo days).

### Twist C: Placebo-calendar audit as a pre-trade gate
- Rationale: to estimate how impressive an anomaly is relative to the family of calendars that could have been chosen.
- Rule/process: before deploying any calendar rule, generate all alternative rules in the same family (every k-day window starting at day j of the month, every weekday, every month-pair split) and compute the distribution of the best-performing rule in each of 1,000 block-bootstrapped pseudo-histories; require the real rule to rank above the 95th percentile of the best-of-family distribution (a White Reality Check / Hansen SPA style test).
- Falsification: if the real rule fails this gate, do not trade it.

## 8. Implementation spec

Data: S&P 500 (or other index) futures and cash, with intraday bars (1-minute) for FOMC windows; official FOMC calendar with scheduled/unscheduled flags and press-conference flags; trading-day calendar for TOM; VIX; T-bill rates; non-US index data for validation.

Signals: binary window flags (see Twist A). For pre-FOMC: entry at prior-day close or 24 hours before the statement, exit about 1-5 minutes before 2:00-2:15pm ET (the statement time has been about 2:15pm ET for many years in the paper; confirm current times).

Sizing: unlevered 100% notional of a vol-targeted index position for stand-alone windows; Twist A uses +/-25% tilt on a core position.

Execution: use micro/e-mini futures; limit orders near the close; avoid trading in the minute of the release; no stops inside a 24-hour window (the stop would be arbitrary) except a disaster limit at about 3 daily sigma.

Costs model: 0.5-1 tick slippage each side plus commissions (about 1 bp round trip for liquid index futures; add 2x sensitivity); financing/cash carry when the position is flat versus invested (T-bill return on idle cash).

```
calendar = load(fomc_dates, trading_days)
for each trading day t:
    flags = [is_tom(t), month(t) in {11,12,1,2,3,4}, is_prefomc(t)]
    tilt = +0.25 if sum(flags) >= 2 else (-0.25 if sum(flags)==0 else 0)
    target_exposure = core_exposure * (1 + tilt)
    rebalance at close (limit orders), apply buffer 5%
# Pre-FOMC stand-alone (research only):
#   enter at close(t-1) or 24h before; exit at statement_time - 2 minutes
```

## 9. Backtest plan

- Define each rule exactly before looking at the post-2015 data; store a spec hash and date.
- Splits: in-sample = original publication windows (Lucca-Moench 1994-2011; Lakonishok-Smidt era); post-publication out-of-sample = 2012-2025; sub-split 2016-2025 for pre-FOMC (post-disappearance).
- Multiple-testing control: enumerate the family size (all calendar rules examined), apply Harvey-Liu-Zhu adjusted thresholds (t above 3) and a White Reality Check / Hansen SPA across the family; report the number of rules tried.
- Placebo tests: shifted windows (+/-1 to 5 days), random-date events with matching frequency (8/yr), non-FOMC macro releases (Lucca-Moench report none show the effect), other countries' central bank dates.
- Event study: mean, median, hit-rate, t-statistics with clustered/bootstrapped errors by year; leave-out-top-5-events test for outlier dependence.
- Metrics: per-event return, annualized Sharpe (state treatment of cash), exposure-adjusted alpha vs buy-and-hold, max drawdown, time in market, break-even cost, subperiod table by decade, bootstrap CI.
- Cost stress: 1x/2x/3x.

## 10. Risk management and kill-switch rules

- Max risk per stand-alone event 0.5-1% of equity; never leverage a calendar signal above 1x.
- Kill switch: stop a calendar rule after 12 consecutive events with cumulative negative result beyond 2 times the in-sample standard deviation, or if rolling 5-year t-statistic falls below 1 for pre-FOMC (given the documented disappearance, require positive evidence to trade it at all).
- Overall: calendar tilts must be capped at 25% of portfolio risk; they never override the core risk limits.
- Review annually; delete any rule that lost statistical support out-of-sample.

## 11. Annotated sources

| # | Source | URL | Type | Grade |
|---|---|---|---|---|
| 1 | Lucca and Moench, The Pre-FOMC Announcement Drift (NY Fed SR 512; JF 2015) | https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr512.pdf | Peer-reviewed/WP, read | A |
| 2 | Kurov, Wolfe, Gilbert, The Disappearing Pre-FOMC Announcement Drift (FRL 2021) | https://ideas.repec.org/a/eee/finlet/v40y2021ics1544612320315956.html | Peer-reviewed, abstract read | A- |
| 3 | Kurov, Sancetta, Strasser, Wolfe, Price drift before US macroeconomic news (JFQA 2019) | https://www.skidmore.edu/economics/documents/KSSW2017-PriceDriftBeforeUSMacroeconomicNews.pdf | Peer-reviewed, link failed to download, only seen in search results | B (unread) |
| 4 | TradeMachine Substack, Pre-FOMC Announcement Drift | https://trademachine.substack.com/p/pre-fomc-announcement-drift | Commercial blog, read | C |
| 5 | Bouman and Jacobsen, The Halloween Indicator (AER 2002) | https://pure.eur.nl/en/publications/the-halloween-indicator-sell-in-may-and-go-away-another-puzzle/ | Peer-reviewed, abstract via search only | B+ |
| 6 | Jacobsen and Zhang, The Halloween Indicator: Everywhere and all the time | https://www.bnains.org/backtest/periode/The_Halloween_Indicator_everywhere_and_all_the_time_-_Ben_Jacobsen_%26_Cherry_Y._Zhang.pdf (SSRN 2154873) | WP, partly read | B+ |
| 7 | Quantpedia, Turn of the Month in Equity Indexes | https://quantpedia.com/strategies/turn-of-the-month-in-equity-indexes | Aggregator summary, read | B- |
| 8 | MPRA 36566, Turn-of-the-month effect on the Bucharest stock exchange | https://mpra.ub.uni-muenchen.de/36566/1/MPRA_paper_36566.pdf | Working paper, small market, skimmed only | C |
| 9 | Day-of-week decay literature (Morey-Rosenberg; Smith-Robins; Steeley) | https://news.wpcarey.asu.edu/20171204-research-debunks-myth-stock-market-weekend-effect | University news summary of a paper | C |
| 10 | Harvey, Liu, Zhu, ...and the Cross-Section of Expected Returns | https://www.nber.org/papers/w20592 | WP, partly read | A |
| 11 | Lakonishok and Smidt 1988 (RFS 1(4), 403-425, DOI 10.1093/rfs/1.4.403); Ogden 1990; French 1980 | https://doi.org/10.1093/rfs/1.4.403 (not opened; paywalled; only a search-result description: 90 years of DJIA data, anomalies around turn of week, month, year and holidays) | Peer-reviewed, secondary description only | B (unread) |
| 12 | McConnell and Xu, Equity Returns at the Turn of the Month (FAJ 2008) | https://rpc.cfainstitute.org/research/financial-analysts-journal/2008/equity-returns-at-the-turn-of-the-month | Peer-reviewed, abstract page opened (full text gated) | B+ |
| 13 | Lucca and Moench, The Pre-FOMC Announcement Drift: More Recent Evidence (Liberty Street Economics, 16 Nov 2018) | https://libertystreeteconomics.newyorkfed.org/2018/11/the-pre-fomc-announcement-drift-more-recent-evidence.html | Fed blog, opened and read | B+ |
| 14 | Cocoma, Disagreement and Scheduled Announcements (JFQA 61(4), 2026) | https://www.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/abs/disagreement-and-scheduled-announcements-explaining-the-preannouncement-drift/D95FE7194D48A9430B26876EDEBBA9C3 | Abstract page opened; theory, not an out-of-sample test | B (abstract) |
| 15 | Data for the OWN checks: Fed FOMC calendar pages (federalreserve.gov/monetarypolicy/fomchistorical*.htm and fomccalendars.htm), Ken French daily factors, Yahoo Finance SPY, FRED | various | Free data | data |

Search results also surfaced a 2024 Applied Economics paper ("The pre-FOMC announcement drift: short-lived or long-lasting?", DOI 10.1080/00036846.2024.2322573) and a 2026 Journal of Futures Markets paper; the first page returned 403 and the second was not opened, so I make no claim about their findings.

## 12. Open questions

1. Is the pre-FOMC drift permanently gone, or conditional on uncertainty and communication regime? Kurov et al. suggest uncertainty, but more events are needed.
2. What happens in the pre-announcement hours for non-FOMC central banks (ECB, BoE, BoJ)? Lucca-Moench note foreign indices had similar returns around US FOMC; independent central-bank tests are a good out-of-sample.
3. Are TOM and Halloween independent after controlling for flows (monthly fund flows, 401(k) contributions)?
4. How large is the true test-family size for calendar rules, and what does the Reality Check imply for Halloween/TOM significance?
5. Net of costs and taxes, is any of this better than staying invested? For Halloween the opportunity cost of summer cash is large unless summer returns are truly flat.
6. Does the day-of-week effect have any residual conditional form (e.g. reversal after Monday declines per one summary) or is that also a sample artifact?

Sources were thinnest for this strategy group: I read the Lucca-Moench paper and Jacobsen-Zhang in primary text, and in the second pass the Lucca-Moench 2018 update, but the Kurov et al. (working-paper PDF gone, SSRN 403), Bouman-Jacobsen, Lakonishok-Smidt, McConnell-Xu (abstract only) and day-of-week papers are still read only through abstracts or secondary summaries. The OWN recomputations partly substitute for the missing primaries but are rough: daily rather than intraday data, Welch t-tests that ignore clustering, and about 15 pre-FOMC comparisons examined.

## Second-pass changelog (2026-10-07)

- Read/opened: Lucca-Moench SR 512 (re-verified 49 bp, t above 4.5, 80%, Sharpe 1.14 with 8x per-meeting annualization, 20 bp 1980-93), Lucca-Moench 2018 Liberty Street update, McConnell-Xu abstract page, Cocoma JFQA abstract page. Failed/unavailable: Kurov-Wolfe-Gilbert full text (Skidmore PDF now 404, SSRN 403, ScienceDirect not opened), Lakonishok-Smidt (paywalled), Bouman-Jacobsen (not retried), 2024 Applied Economics paper (403).
- Changed conclusions: pre-FOMC moves from "dead since 2015" to "contested after 2015, not tradable on current evidence" (NY Fed 2018: persists with press conferences, starts earlier; Kurov: gone; OWN: FOMC-day premium gone 2016+, overnight leg positive 2020-26 but not significant after multiplicity). TOM now shown by OWN data to have vanished since 2006 (about 4-5 bp/day vs 14-16 bp before 2006), and cost-aware Sharpe in 2006-2025 is below buy-and-hold. Halloween: century-level t about 1.8, summer-in-bills lowered compound return in 3 of 4 sub-periods. Monday effect confirmed gone after 1990.
- Grades: TOM evidence B- to B (OWN confirms classic effect, but only as a pre-2006 phenomenon); pre-FOMC A- to B+ on persistence (original paper still A; post-2015 contested); Halloween B+ to B; day-of-week C to B (own data) but conclusion is that it is dead.
- Corrected: Twist B's press-conference condition is degenerate after 2018. Twists A, B, C remain hypotheses, NOT backtested; Twist A's 2016-2025 held-out window now looks harder to pass given the OWN results (TOM leg and Halloween leg contribute little recently; pre-FOMC leg uncertain).
- Remaining [UNV]: Boguth et al. (2019); French/Gibbons-Hess day-of-week claims; Ogden payment-date rejection; the 0.15% TOM Quantpedia derivations; Hull-Bakosova-Kment Sharpe 0.77.
