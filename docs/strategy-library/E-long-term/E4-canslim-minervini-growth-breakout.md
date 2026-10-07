# E4. CANSLIM, Minervini SEPA/VCP, Darvas: Growth-Breakout Trading

Status: research dossier, not investment advice. Twists in section 7 are untested hypotheses. Dated 2026-10-07.

Source-access note (revised in second pass, 2026-10-07): I still have not read any of the primary books (O'Neil, Minervini, Darvas); the Darvas text on archive.org is lending-only and returned "not available" / 401 when I tried. What changed: I read in full (a) Novy-Marx's earnings-momentum paper, (b) AAII's 2016 summary of O'Neil's 4th edition (the best proxy for the book that I could open), and (c) a contest-history page that tabulates entrant counts. Rule thresholds are now labelled by provenance: [O'Neil via AAII] = AAII's paraphrase of the 4th edition; [secondary] = blogs/code implementations; [unverified] = could not be traced. Still the thinnest dossier on primary evidence. Grades in section 11.

## 1. Summary, horizon, asset class, holding period

Discretionary or rules-based long-only equity strategies that buy leading growth stocks with strong earnings and relative strength as they break out of consolidation bases in a confirmed market uptrend, cut losses fast (about 7-8%), and hold winners for weeks to a few months (occasionally longer). Asset class: US growth equities (small/mid-cap heavy). Horizon: weeks to months; the title "long-term" is stretched: this is intermediate-term trend/momentum trading with a concentrated book (often 4-10 names) and high turnover (AAII's CAN SLIM screen showed ~57% turnover and ~6 holdings as of end-2016, per AAII table via search). Includes Darvas box breakouts (1950s) as the historical antecedent.

## 2. Origin and who uses it

- William O'Neil: CAN SLIM (C current quarterly earnings, A annual earnings growth, N new product/management/price high, S supply and demand (shares/float), L leader not laggard, I institutional sponsorship, M market direction), published in "How to Make Money in Stocks" (first edition 1988; 4th edition 2011); AAII's 2016 article describes him as founder of Investor's Business Daily. His "model book" study of past winners was re-run for each edition, per AAII: 500 winners 1953-1993 (2nd ed., 1994), 600 winners 1953-2001 (3rd ed., 2002), 1,000 winners 1880-2009 (4th ed., 2011). So the empirical base is O'Neil's own hindsight selection of winners, enlarged over time, and the thresholds drift between editions. Reported: average relative strength of 87 before big moves (AAII's 4th-edition summary says 1950-2008; an earlier version of this dossier said 1953-1985 from a blog/search summary; the AAII dating is the better-sourced one); 95% of winners had a fundamental catalyst; median annual EPS growth of winners 36% at the early stage, 1980-2000 (both AAII). Other figures I previously listed (earnings up more than 70% for three of four winners; "87% had 30%+ growth") came from Globes and a blog and are not confirmed by AAII, so treat them as unverified.
- Mark Minervini: SEPA (Specific Entry Point Analysis), "Trade Like a Stock Market Wizard" (2013), "Think and Trade Like a Champion", Trend Template and VCP (volatility contraction pattern). Won the 1997 U.S. Investing Championship (155%) and the 2021 $1m+ stock division (+334.8%; runners-up Vibha Jha +100.4% and Hsiu-Ping Peng +11.4%, per a third-party contest-history page; the earlier record of +119.1% by George Tkaczuk in 2020 is from the first pass and was not re-verified).
- Nicolas Darvas: "How I Made $2,000,000 in the Stock Market" (1960), box theory.
- Others in the same lineage: David Ryan, Dan Zanger, Mark Ritchie II (claims via the book Momentum Masters marketing; contest wins by Ryan are promotional claims).
- Jack Schwager, Stock Market Wizards: interview with Minervini (see below).

## 3. Economic rationale and who is on the other side

Rationale: (1) Earnings momentum and post-earnings drift: investors underreact to accelerating fundamentals, so leaders keep rising. (2) Price momentum (Jegadeesh-Titman 1993: buying winners and selling losers gives significant returns over 3-12 months holding periods; not explained by systematic risk per their conclusion). (3) Nearness to 52-week high predicts returns better than past returns (George and Hwang 2004; explains a large portion of momentum profits, effect does not reverse long-run per abstract). A breakout from a base near a high is a practical form of this. (3b) Earnings drift, and a challenge to the price-only reading: Chan, Jegadeesh and Lakonishok (1996, abstract read) found past returns and past earnings surprises each predict drift after controlling for the other. Novy-Marx (NBER w20984, full text read; sample Jan 1975 to Dec 2012) argues the CJL test was too coarse (3x3 sorts) and that earnings surprises subsume past performance in cross-sectional regressions, with price momentum's time-series returns explained by earnings-momentum strategies; purging past performance from earnings momentum removes the crashes without lowering average return. Implication for this dossier: the "C" (earnings) leg of CAN SLIM probably carries much of the momentum premium, which supports testing it (twist 2), but the academic measure is a standardized earnings surprise, not O'Neil's year-over-year EPS growth percentage, so the paper does not validate the 18-25% EPS-growth thresholds. (4) Cutting losers at 7-8% and market-timing filters (M) are meant to avoid momentum crashes.

Other side: value/contrarian sellers, early holders taking profits, anchoring investors who sell near 52-week highs (George-Hwang's behavioral reading, from memory, unverified), and short sellers fading extended stocks. In a competitive view the edge is compensation for momentum-crash risk (Daniel and Moskowitz 2016: crashes occur in "panic" states after market declines when volatility is high, coincident with market rebounds, because past losers have option-like payoffs and high betas).

## 4. Canonical rules

Provenance rule: nothing below is from a book I read. [O'Neil via AAII] means AAII's Nov 2016 paraphrase of the 4th edition (read in full); it is the closest I got to the primary author.

CAN SLIM [O'Neil via AAII, 4th edition unless noted]:
- C: current quarterly EPS at least 18-20% above the same quarter a year earlier (the earlier version of this dossier said >=25% from unnamed secondary sources; that number matches the annual criterion below, not C), accelerating; quarterly sales growth 25% or accelerating over three quarters; exclude one-time items; two straight quarters of material slowdown is a sell signal.
- A: annual EPS up in each of the last three years, 25%+ compound growth (range stated 25-50%), ROE 17%+, positive cash flow.
- N: new product/management/industry change, and new price highs out of a properly formed base on higher volume (95% of winners had some catalyst, per O'Neil's study).
- S: smaller share count and larger insider ownership favored; buybacks favored; low debt-to-equity.
- L: relative strength rank (IBD) of 80+, avoid anything below 70; buy the top two or three stocks in a strong group.
- I: AAII reports "20 might be a reasonable minimum" institutional owners, preferring rising sponsorship and avoiding over-owned names. The earlier "about 10 holders" figure is a parameter of AAII's own screen, not O'Neil's rule; thresholds may differ in the earlier editions the AAII screens were built from.
- M: judge the market from daily price/volume of three or four indexes; AAII's summary says go roughly 25% to cash when the market peaks and a major reversal begins. Follow-through-day and distribution-day counts are not in the AAII summary, so remain unverified here.
- Sell: cut losses at 7-8% below purchase; take profits around 20-25% (the 3:1 profit-to-loss framing, with an exception for unusually strong stocks that O'Neil says can be held; wait at least 13 weeks before judging a stock as not advancing). Confirmed by AAII, still not by the book.
- Caveat: AAII's screens are its own operationalisation (for example, price at least 90% of the 52-week high, RS above 80, EPS growth 20%+, sales growth 25%+, at least 10 institutional owners in the "revised" screen); they are not O'Neil's thresholds.

Minervini Trend Template [secondary only; I could not open any Minervini primary text]: Implementations I opened agree on these core conditions: price above 150- and 200-day SMAs; 150-day above 200-day; 200-day rising (one-month lookback in the TrendSpider code, which also splits 50>150>200 into separate tests); 50-day above 150- and 200-day; price above 50-day; within 25% of the 52-week high; and a relative-strength floor (TrendSpider code uses a relative performance score above 70, other write-ups say a top-percentile rank). The conflict is the distance above the 52-week low: the first pass of this dossier said 25%; the TrendSpider code I opened says 30%; a search-result snippet of a TradingView script also said 30%. I have no primary source, so I now state 30% as the more commonly implemented value but flag it as unresolved. One snippet (ProRealCode, unopened) says Minervini prefers the 200-day rising for 4-5 months, so the one-month version is probably a minimum. The count of "eight criteria" is consistent across sources; the list of what the eighth is varies (RS rank vs 52-week-high distance).
VCP [secondary]: successive pullbacks each shallower than the previous (one source gave illustrative depths 20-35%, then 10-20%, 5-15%, 3-8%), volume drying up in contractions, entry on breakout of the last pivot on volume; avoid chasing more than about 10% above pivot. Stop: a promotional Substack post attributes "usually 5-8% max" to Minervini; earlier sources said 7-8%. Treat as 5-8% [secondary]. Risk 1-2% of capital per trade: first-pass secondary figure, not re-verified.
Fundamental filter: strong quarterly EPS growth (one source 20-50%+); not traceable to Minervini directly.

Darvas box [secondary; original text not accessible]: define box high/low from consolidation; buy when price breaks above the box top in an uptrend on strong volume; Wikipedia's account says the stop-loss goes just below the purchase price (the first-pass wording "just below the box" is a common secondary reading; the two conflict slightly and only the book can settle it); trail stops as new boxes form; he said he did not short, and he picked stocks with rising volume and favorable fundamentals.

## 5. Evidence

Peer-reviewed supporting the underlying anomalies (not CAN SLIM per se):
- Jegadeesh and Titman (1993): momentum profits 3-12 months.
- George and Hwang (2004, J. Finance 59): abstract-level only (via a mirror site and a search summary; the publisher page was not opened). Claims: 52-week-high proximity forecasts returns better than past returns, with no long-run reversal. The "1963-2001" sample dates in the first pass are from memory/secondary and unconfirmed. Later work (per a search summary, not opened) found the 52-week-high strategy weaker than plain momentum in international index data, so the result is not universal.
- Chan, Jegadeesh and Lakonishok (1996): abstract read (RePEc): price and earnings momentum each carry independent drift; not explained by market risk, size or book-to-market.
- Novy-Marx (NBER w20984, full text read, sample 1975-2012): earnings surprise subsumes past-return momentum; relevant to the C/A legs. Caveat: the headline is a long-short factor result, not a long-only breakout strategy with stops.
- Daniel and Moskowitz (2016, NBER w20439, abstract read): crashes follow market declines in high-volatility states and coincide with rebounds; dynamic momentum roughly doubles alpha and Sharpe versus static; robust across periods, international equities and other asset classes.

Direct tests of CAN SLIM / O'Neil rules:
- Lutey and Rayome, Journal of Accounting and Finance 22(2), April 2022 (publisher page opened, abstract only; DOI 10.33423/jaf.v22i2.5134): paper-traded portfolio holding only five stocks, built from O'Neil (1988) fundamentals screen then proximity to technical buy points, July 2014 to Feb 2017, outperformance of about 20% vs S&P 500, 9% vs Nasdaq, 17% vs Dow (cumulative over the period, as I read it; the page is not explicit). The page does not discuss costs, universe or number of trades; it says tracking stopped in 2017 and the authors claim later results would be better, which is unaudited. Five names over 2.5 years is not statistical evidence; a bull-market window for growth stocks; "live" means paper trading by the authors themselves, with the rules chosen by them. Weight: anecdote-plus.
- Nelson, Olson, Witt, Mossman, "A test of the Investor's Daily stock ranking system", The Financial Review 33(2), May 1998 (the journal attribution comes from an issue index and the numbers from a search-result paraphrase of the abstract; I did not open the abstract page successfully and did not read the paper): best IBD-ranking system gave about 1.81% market-adjusted abnormal monthly return buying S&P 500 stocks and 3.18% on an arbitrage portfolio; the selected stocks were more volatile; the authors note abnormal returns were lower in the second half of their sample and the effect may be temporary. This is the closest thing to an independent test of IBD's own rankings, and it suggests decay. Costs not known. The first-pass author order and year citation "(1998)" is consistent with this.
- IBD's own published studies and critics: I did not find a peer-reviewed critique of O'Neil's model-book method or an independent audit of IBD's rating performance. The model-book method (selecting winners ex post and listing common traits) has no control group of non-winners with the same traits, so it cannot estimate the hit rate; this is a methodological point of mine, not a published critique I found.
- AAII CAN SLIM screens (AAII articles opened): (a) "Revised" screen (Feb 2008 article): hypothetical portfolio Jan 1998 to end-2007, cumulative 743.8% (about 23.8% a year) vs 51.3% for the S&P 500 and 118.1% for the S&P SmallCap 600 as stated by AAII; the S&P 500 figure looks like it may be price-only or otherwise mismatched with total-return history, so I do not trust the comparison until recomputed. Screen criteria were published after the 2002 3rd edition, so a 1998-2007 test is partly in-sample. (b) From the first pass (not re-opened): 24.4% average annual return since 1997 with risk index 1.89, 16 of 183 months with no passing companies. AAII itself says results exclude transaction costs and spreads and are not achievable by individuals.
- Student backtests (WPI MQP 2008, 559 stocks in 2007): not peer-reviewed, no weight.

Evidence from practitioner results:
- Contest mechanics (from a third-party contest-history page, completetradersedge.com, which links but whose primary links I could not follow; organiser releases on Business Wire returned 403 to me): entrants nominate a brokerage account before the year starts (it need not be their own); results are time-weighted and checked against brokerage statements, with live walkthroughs on request; monthly standings are optional, so entrants can surface only in quarterly/final lists; four boards with different instrument rules and account bands (so records are not comparable); not a GIPS audit; no cash prize; the organiser's firm was the subject of an SEC cease-and-desist order in 1998 (unregistered securities and books-and-records; the page cites SEC Release 33-7560 but I did not open it) and the principal runs a commercial education business. The page's entrant counts: 96 (2019), 124 (2020), 338 (2021), 326 (2022), 352 (2023), 451 (2024), 579 (2025). The 338 matches the first-pass figure.
- Minervini 1997: +155%, stock division, reported as about $250,000 of his own money, long-only against leveraged futures/option entrants (the same contest-history page; originates from Minervini's own account and the organiser's restatement; not independently audited by me). 2021: +334.8% in the $1m+ stock division (second +100.4%). An eleven-month release had shown +325.2% (first pass). Contest verification is the best available check, but I found no independent audit of the specific accounts.
- "220% average annual return", "36,000% / 33,554% total return", "one losing quarter": Schwager's Stock Market Wizards blurb/quotes (220% average annual over about five to five and a half years, worst year +128%, one down quarter of a fraction of a percent) as relayed by search results and a blog; the total-return figure conflicts by source (33,554% vs 36,000%, consistent with different end dates or rounding, not reconcilable here). I did not read Schwager's chapter. These are Minervini-supplied, unaudited, and the period (late 1990s) was a speculative growth-stock bull market. I found no transcript where he gives a maximum drawdown or confirms leverage use in 1997 beyond the contest-page description.
- Ryan and Zanger claims (consecutive championships, $11,000 to $18 million) remain promotional and unverified; the contest-history page itself says the Ryan year assignments (1985-1987) are not settled.
- Darvas: the claim is roughly $2 million (book title) or about $2.45 million (Wikipedia, citing his later 1971 book) over 18 months in the 1957-58 bull market. Wikipedia reports that in 1960 Time carried New York's Attorney General calling the story false and finding only about $216,000 in provable profits, and that a court later blocked the probe (I did not read Time; this is via Wikipedia). So even the headline return is contested by an official body, though not resolved; no rigorous test exists. The earlier "$10k or $36k starting capital" variants remain unverified.

Critical assessment (survivorship and self-reporting):
- Quantifying survivorship and self-report bias: it cannot be done for Minervini's record with the evidence available, and I will not give a number. What the evidence does allow: (1) The only published success-rate figures are the organiser's: 26 of 316 (about 8%) reported a profit at ten months of 2022 (S&P 500 down 19.4% that year) and 115 of 688 (about 17%) at mid-2026 (S&P up 10.2%). Both count voluntary reporters, so the true profitable share is unknown, and they are for the whole contest (all styles), not growth-breakout traders. (2) Leaders fade: the contest-history page lists monthly leaders who fell back a lot by year-end (+960.4% at eleven months to +409.6% final; +1,358.2% to +969.8%), which shows that interim self-reported leaderboards overstate final outcomes. (3) There is no style-level breakdown of entrants (how many used CAN SLIM/SEPA), so nothing reveals the denominator for this strategy. (4) The best-documented analogue, hedge fund databases, shows survivorship and backfill biases of roughly 3% and 1.3-1.4% a year in Fung-Hsieh (2000) per secondary tables; the FAJ 2009 update page I opened gives only a qualitative abstract. These numbers are not transferable to a contest of retail accounts and are given only to show that self-reported data typically add a few points a year, not hundreds. (5) Qualitative selection logic: with several hundred entrants, a top finisher at several times the median is expected from dispersion alone; the one-year winner's return is therefore weak evidence of edge. Only persistence across years for the same person would be informative, and Minervini's two wins are 24 years apart with a self-reported record between them.
- The CME-trading-challenge literature I found (persistence among non-professionals) does not tell us about this particular contest. The distribution of failures is unobservable.
- A 2021 record (+334.8%) occurred in a speculative small-cap retail mania year; this is consistent with a high-beta momentum regime, not necessarily a general edge. Minervini's own multi-year track record is self-reported.
- Book authors have incentives (books, courses, newsletters), so selection of examples (winners charts) is guaranteed.
- Academic support exists for momentum and 52-week-high effects, but not for the specific bundle of discretionary rules; the evidence for the combined CAN SLIM screen is thin, partly in-sample, and costs are ignored in AAII's backtests.
- Capacity: the strategy depends on small/mid-cap liquidity; the sources show concentrated books, so scalability is limited.

## 6. Failure regimes and risks

- Choppy or bear markets: breakouts fail; whipsaw; the M filter helps only if it works in real time (late).
- Momentum crashes at market rebounds after declines (Daniel-Moskowitz).
- Crowding of breakout entries around well-known pivots (stop runs); my inference, unverified.
- Gap risk through 7-8% stops, particularly around earnings.
- Earnings-report concentration: a CAN SLIM universe tends to be high-multiple growth; when rates rise or growth multiples compress (a plausible regime; not verified from sources), drawdowns can be severe.
- Discretion: patterns like VCP are subjective; hindsight bias in chart studies is severe.
- Few passing names in downturns (AAII screen had no picks 9% of months): the system is inherently intermittent.
- High turnover and tax drag.

## 7. MY TWIST (hypotheses, NOT backtested)

Twist 1: Rules-based "VCP-lite" with a systematic market filter.
- Rationale: remove subjectivity so the idea can actually be tested; keep the 52-week-high and trend components that have academic support.
- Rules: universe = US stocks with price > $10, 50-day dollar ADV > $10m; trend template (price > 50 > 150 > 200 day MAs, 200-day rising 21 days, within 25% of 52-week high, >=30% above the 52-week low); RS = percentile of 12-1 month return > 80th; contraction test: 20-day ATR/price below its 60-day median and 3 successively smaller swing ranges (zigzag 5%); entry = close above the 20-day high on volume >= 1.5x 50-day average; initial stop = min(7%, 2xATR below entry); market filter: S&P 500 above 200-day MA and 10-day breadth positive.
- Parameters: RS cutoff 70/80/90; volume multiple 1.2/1.5/2; stop 6/7/8%; market filter variants.
- Expected effect: fewer trades, lower drawdown versus buy-and-hold momentum; edge unknown.
- Falsification: if net of costs the strategy does not beat both (a) a plain 12-1 momentum long-only portfolio with the same market filter and (b) cap-weighted index on risk-adjusted terms (Sharpe difference bootstrap p > 0.10) over 2000-2025, the "pattern" adds nothing beyond momentum.

Twist 2: Add earnings acceleration (C and A) as a rank, test what fundamentals add.
- Rationale: separate the contributions of price and fundamental criteria; most CAN SLIM claims bundle them.
- Rules: rank by quarterly EPS growth acceleration (YoY growth this quarter minus last quarter) and sales growth; combine with RS rank; test 2x2 (high/low fundamentals x high/low RS) breakouts.
- Parameters: acceleration definition, earnings surprise inclusion (second pass: Novy-Marx's standardized earnings surprise is the academically supported variable, so test it as a separate arm against O'Neil-style YoY EPS growth of 18/20/25%), lag for reporting (use point-in-time). Still an untested hypothesis.
- Expected effect: if fundamentals matter, high-fundamental breakouts outperform; if not, there will be no difference.
- Falsification: if the high-fundamental cell's mean forward 3-month net return minus the low-fundamental cell is not > 0 at t >= 2 over 2000-2025, drop the "C/A" part from the system.

Twist 3: Volatility-managed momentum sizing (Daniel-Moskowitz-inspired).
- Rationale: the dynamic scaling in the abstract reportedly doubles momentum Sharpe; apply to book exposure.
- Rules: gross exposure = min(1, target_vol / realized 60-day vol of the strategy's equal-weight paper index); halve exposure when S&P is >10% below its 52-week high and 1-month realized vol > 1.5x median.
- Parameters: target vol 15/20/25%; window 20/60; drawdown threshold.
- Expected effect: avoid rebound crashes, lower tail loss, at cost of lag.
- Falsification: if worst monthly drawdown and max drawdown do not improve at least 20% relative in out-of-sample years while Sharpe drops, discard.

## 8. Implementation spec

Data: point-in-time daily OHLCV with split/dividend adjustment and delistings; point-in-time quarterly fundamentals with report dates; institutional ownership (13F) optional with lag (13F delay up to 45 days); index and breadth data; float data.
Signals: as in section 4 / twist 1.
Sizing: risk per trade 0.5-1.0% of equity (stop distance x shares), max position 15-20%, max 8-12 positions, max sector 30%; scale in 1/3 at pivot, 1/3 on first add, etc. (the pyramiding detail is commonly described; verify).
Execution: buy-stop orders at pivot with limit 1-2% above; avoid first 15 minutes; limit entries when gap > 5% over pivot; sell stops as stop-limit or market-on-open to handle gaps.
Stops: initial 7% or 2 ATR; trail to break-even after +10%; exit on close below 50-day MA on heavy volume or after climactic run (rule-based version).
Costs: half-spread 5-25bp depending on liquidity + impact; commission ~0; gap slippage on stops 1-3% beyond stop price on bad gaps (assumption, calibrate); plus short-term capital gains taxes if applicable.

Pseudo-code:
```
daily after close:
  mkt_ok = spx>sma200 and breadth_ok
  for s in universe:
    if trend_template(s) and rs(s)>0.8 and vcp_lite(s) and eps_ok(s):
      watch[s] = pivot(s)
next day:
  if mkt_ok and price>pivot and vol>1.5*avg50: buy size=risk/(entry-stop)
  for p in positions: update trailing stop; exit rules
```

## 9. Backtest plan

- Universe/Period: 1995-2025 US with delisted names (survivorship-free data mandatory); split 1995-2008 design, 2009-2019 validation, 2020-2025 final hold-out.
- Control for the obvious: benchmark against (a) buy-and-hold index, (b) simple 12-1 momentum long-only with the same exposure, (c) random entries with same stop/exit logic and same holding-time distribution (Monte Carlo) to measure if the "pattern" has any edge.
- Multiple testing: log all variants; Deflated Sharpe, SPA test; do not tune stop and pattern jointly on the same data without penalty.
- Risk of ruin analysis: simulate position sizing with measured win rate/payoff and gap losses; report probability of 30% drawdown.
- Metrics: net CAGR, Sharpe, max drawdown, expectancy (R-multiple), win rate, payoff, profit factor, turnover, exposure time, performance by market regime and by year (specifically 2000-2002, 2008, 2020, 2022), exposure to momentum and size factors, capacity.
- Check regime dependency: report 2020-2021 separately to see if results depend on the speculative boom.

## 10. Risk management and kill-switch rules

- Risk per trade <= 1%; portfolio open risk <= 6-8% (assumption).
- Daily loss limit 3% of equity: stop new entries for the day; weekly 6%.
- Drawdown: at -10% from peak halve trade size; at -20% stop trading and review; resume only after market filter is positive and a paper-trade period passes.
- Strategy-level: if expectancy over trailing 50 trades is negative with t < -1 and win rate falls under 60% of backtest, pause.
- Market filter fail -> no new longs, tighten stops.
- Concentration: no more than 30% in any sector or correlated theme.
- Earnings events: reduce or hedge positions before earnings if gap risk exceeds 2x stop distance.
- Never use margin beyond 1.25x without separate approval.

## 11. Annotated sources (A/B/C)

Read-status key: FULL = full text read in second pass; ABS = abstract/landing page only; NOT RE-OPENED = cited in first pass, not re-checked.
1. Jegadeesh and Titman 1993 via Wharton/summary: https://knowledge.wharton.upenn.edu/article/recognizing-an-investing-signal-that-defied-wisdom-and-endured/ - A/B (NOT RE-OPENED).
2. George and Hwang 2004: https://alphaarchitect.com/the-secret-to-momentum-is-the-52-week-high/ ; https://www.cxoadvisory.com/1284/technical-trading/the-52-week-high-as-a-momentum-indicator-for-individual-stocks/ - B (ABS via search; RePEc and mirror pages failed to open for me; paper A, not read).
3. Daniel and Moskowitz, Momentum Crashes: https://www.nber.org/papers/w20439 - A (ABS, opened). https://www.chicagobooth.edu/review/understanding-momentum-crashes (NOT RE-OPENED).
3b. Novy-Marx, Fundamentally, Momentum is Fundamental Momentum, NBER w20984: https://mysimon.rochester.edu/novy-marx/research/FMFM.pdf - A (FULL; working-paper version, 1975-2012).
3c. Chan, Jegadeesh, Lakonishok 1996: https://ideas.repec.org/a/bla/jfinan/v51y1996i5p1681-1713.html - A (ABS).
4. Lutey and Rayome, JAF 2022: https://articlegateway.com/index.php/JAF/article/view/5134 - B- (ABS; five-stock, 2.5-year, author-run paper trade; downgraded from A/B).
4b. Nelson, Olson, Witt, Mossman, Financial Review 1998: https://business.louisville.edu/faculty-research/research-publications/a-test-of-the-investors-daily-stock-ranking-system - B- (listing page opened but showed no abstract; numbers from a search paraphrase; paper not read).
5. AAII screens: https://www.aaii.com/journal/article/investing-in-proven-growth-using-can-slim-revised (FULL, Feb 2008 screen and results) - B (hypothetical backtest, no costs, partly in-sample); https://www.aaii.com/journal/article/a-can-slim-screen-with-no-float-but-plenty-of-lift ; https://www.aaii.com/journal/article/building-a-stock-screen-on-oneils-fourth-edition-of-the-can-slim-approach (NOT RE-OPENED).
6. O'Neil rules via AAII (Bajkowski, Nov 2016): https://www.aaii.com/files/journal/pdf/9874_william-oneil-can-slim-approach-to-selecting-growth-stocks.pdf - B (FULL; best available paraphrase of the 4th edition, upgraded from B/C for rules, still not the book). https://seekingalpha.com/article/4371844-a-stock-pickers-guide-to-william-oneils-can-slim-system ; https://en.globes.co.il/en/article-1000291569 - C (NOT RE-OPENED; Globes figures now marked unverified).
7. Contest-history and rules page (third party, with caveats section; commercial site): https://completetradersedge.com/?p=234478 and https://completetradersedge.com/?p=234484 - B-/C+ (FULL; entrant counts, rules, 1998 SEC order cited; its primary links not followed by me). Organiser's Business Wire releases (https://www.businesswire.com/news/home/20211026005502/en ; https://www.businesswire.com/news/home/20211222005142/en ; https://www.businesswire.com/news/home/20220124005241/en/...) returned 403 or were not re-opened - B (promotional elements, now unverified by me this pass). https://kyodonewsprwire.jp/index.php/release/202201256538 - NOT RE-OPENED.
8. Minervini profile pages: https://caseystubbs.substack.com/p/how-mark-minervini-won-the-us-investing (opened: only the 155% figure and "5-8% max" stop; promotional) - C; https://wallstreettrader.substack.com/p/how-mark-minervini-won-us-investing ; michaelsincere.com interview (404 on the new URL; NOT RE-OPENED) ; Audible bio - C. No Minervini primary text or Schwager chapter was read.
9. Minervini rule implementations: https://trendspider.com/trading-tools-store/indicators/68cda6-minervini-trend-template/ (opened; code with 30%-above-low and RP>70) - C+; https://skills.cat/skills/copyleftdev/sk1llz/minervini-swing-trading ; https://de.tradingview.com/script/ff3xze6y-Mark-Minervini-SEPA-Balanced - C (NOT RE-OPENED).
10. Darvas: https://en.wikipedia.org/wiki/Nicolas_Darvas (opened; reports Time 1960 and NY AG dispute; Time not read) - C+; https://tradethatswing.com/the-technical-foundations-of-nicolas-darvass-trading-strategy/ ; https://shortform.com/books/blog/box-theory-nicolas-darvas.html - C (NOT RE-OPENED). The book on archive.org (identifier howimade2000000i0000darv) is borrow-only; text not obtainable.
10b. Hedge fund bias context: https://rpc.cfainstitute.org/research/financial-analysts-journal/2009/measurement-biases-in-hedge-fund-performance-data-an-update - B (ABS, qualitative); the 3% / 1.3-1.4% figures for Fung-Hsieh 2000 are from a search-result summary of secondary tables - C, indirect relevance only.
11. Momentum Masters listing (marketing): https://opencourser.com/book/a3fvlr/momentum-masters - C.
12. CME trading challenge persistence study: https://emerald.com/insight/content/doi/10.1108/RBF-09-2019-0122 ; survivorship in trading https://alphaarchitect.com/survivorship-biases/ - B (indirect relevance).
13. Quantified Strategies CANSLIM backtest: https://quantifiedstrategies.substack.com/p/the-canslim-method-does-it-work-backtest - C (not read in detail).

## 12. Open questions

- Net of costs, with survivorship-free data, does a systematic CAN SLIM / Trend Template implementation beat plain momentum with a market filter?
- How much of the contest results are leverage/concentration luck versus repeatable edge? Entrant-level contest data would be needed and I found none.
- Does the earnings-acceleration filter add to price momentum after controls?
- Are VCP shapes predictive beyond ATR contraction near highs?
- What exact O'Neil thresholds can be verified from the book editions? (Second pass narrowed this: C 18-20%, A 25%, RS 80, I about 20 owners, sell 7-8% per AAII's 4th-edition summary; M follow-through/distribution-day rules and the edition-by-edition drift are still open.)
- What are the Minervini trend-template cutoffs in the book (30% vs 25% above the 52-week low; RS floor; 200-day slope)? Needs the 2013 book or his published materials.
- Can the 1997 and 2021 contest accounts be checked beyond the organiser's say-so, and is there entrant-level data by style?
- Capacity: at what account size does the approach stop working in small caps?

## Second-pass changelog (2026-10-07)

- Read in full: Novy-Marx (NBER w20984, 1975-2012), AAII 2016 summary of O'Neil 4th edition, AAII Feb 2008 revised screen, contest-history pages, TrendSpider Trend Template code. Abstract-only: Daniel-Moskowitz, Chan-Jegadeesh-Lakonishok, Lutey-Rayome, George-Hwang (via secondary). Not obtainable: all three primary books (Darvas is borrow-only on archive.org), Schwager chapter, Minervini transcripts, Business Wire releases (403), Nelson et al. (1998) text.
- Rules corrected: C threshold 18-20% (was ">=25%"); A is where 25% belongs; institutional owners about 20 (was about 10, which is an AAII screen parameter); RS 80 floor, avoid below 70; sell rules (7-8% stop, 20-25% profit, two-quarter earnings slowdown) now sourced to AAII's 4th-edition summary; RS-87 study dated 1950-2008 (was 1953-1985); model-book samples listed by edition. Globes/blog earnings statistics downgraded to unverified.
- Trend Template: 25%-above-low changed to 30% (flagged unresolved; secondary code only); Darvas stop placement conflict noted; Minervini stop stated as 5-8% (secondary, promotional).
- Evidence: added Novy-Marx and CJL (earnings drift likely drives much of momentum, so C leg matters); Lutey-Rayome downgraded to B- (five stocks, author-run, no costs on page); Olson et al. identified as Financial Review 1998 with decay noted; AAII 1998-2007 screen result added with a flag on its S&P comparison and in-sample risk; no peer-reviewed critic of IBD/O'Neil's model-book method found.
- Contest: rules, verification method, entrant counts 2019-2025, reported-profit rates (8% in 2022, 17% mid-2026), fading leaders, 1998 SEC order against the organiser's firm, and "not a GIPS audit" added. Darvas: NY Attorney General dispute of his gains added (via Wikipedia).
- Survivorship/self-report bias: explicitly judged not quantifiable for Minervini or the contest; only the organiser's reported-profit rates and hedge-fund analogues (indirect) available.
- Source grades revised in section 11 with read-status; twists unchanged apart from a note in twist 2; all 12 sections kept and all twists remain untested hypotheses.
