# B3. Post-Earnings-Announcement Drift (PEAD)

Status: research dossier, written 2026-10-07; second pass 2026-10-07 (section 13 lists changes). Research only, not investment advice. Section 7 twists are hypotheses I have NOT backtested. No reproduction was attempted for this strategy: free point-in-time earnings-surprise data (I/B/E/S, Compustat report dates) was not available. "Read" = I read the document text; "snippet" = only a search-result abstract or secondary summary, so second-hand.

## 1. Summary, horizon, asset class, holding period

PEAD is the tendency of a stock's abnormal returns to keep drifting in the direction of an earnings surprise for weeks to months after the announcement. The classic trade: measure the surprise (standardised unexpected earnings, SUE, or the announcement-window return, EAR), go long the best surprises and short the worst starting one or two days after the release, and hold for about one quarter (about 60 trading days) until the next report. Asset class: US (and international) equities. Horizon: days to three months; the "short-term (days)" slice is the first 5 to 20 days, where the drift is steepest.

Critical headline: this is the oldest published anomaly (Ball and Brown 1968) and the best-documented decay story. Evidence says that for non-microcap stocks the classic SUE drift is gone or statistically unreliable since the mid-2000s (Martineau's abstract: non-existent for large stocks since 2006), though there is a live academic dispute (Kettell et al. find a smaller but still positive hedge return through 2020, and Katz et al. find a 5.1% three-month risk-adjusted hedge return for 1985 to 2014 while arguing it is an aggregation artifact), and the surviving drift, if any, sits in illiquid names that are costly to trade. I still have not read Bernard and Thomas or Foster-Olsen-Shevlin; the founding numbers remain secondary.

## 2. Origin and who uses it

- Ball and Brown (1968) first documented it; Bernard and Thomas (1989 JAR vol. 27, page range disputed between sources, 1990 JAE 13(4):305-340, December 1990 confirmed via Crossref) established the SUE-based design and the underreaction explanation. Second pass: I tried to read both and could not. The University of Michigan Deep Blue copy of the 1990 JAE paper sits behind a bot wall (WebFetch 403; Nimble extract returned only page chrome), Unpaywall lists the 1990 DOI as closed access, and the 1989 JAR paper is on JSTOR/Wiley only. What I did read: Katz-McCubbins-McMullin (2018 working paper) and Martineau, both of which cite the pair and quote the 1989 conclusion that investors fail to recognise fully the implications of current earnings for future earnings. A search-engine summary of the 1990 paper (not the paper) says quarter-t earnings predict three-day announcement reactions in quarters t+1 to t+4, consistent with a seasonal-random-walk expectation. So the underreaction mechanism is corroborated second-hand; the drift magnitudes are still not from a primary source.
- Foster, Olsen and Shevlin (1984, The Accounting Review 59:574-603) are listed by Martineau (read) among the foundational drift studies. Second pass: the only thing I could open was the Stanford GSB working-paper listing page (title, authors, 1984; the abstract was not in the page text I downloaded). A search-engine summary of that listing said the sample is over 56,000 observations for 1974 to 1981 and that drift appears only for a subset of the expectation models tested; I treat that as unverified. The paper itself is not read.
- Practitioners: systematic equity long/short funds use earnings surprise and revision signals as a component of "quality/momentum/sentiment" alpha (generic statement, not tied to a named fund in my sources). Quantpedia, QuantConnect and sell-side "earnings momentum" products reproduce the strategy.
- Recent academic debate: Martineau (2022, Critical Finance Review, "Rest in Peace Post-Earnings Announcement Drift", read in its CFR draft form) argues it disappeared; Kettell, McInnis and Zhao (2022, working paper, read) argue the decline reflects falling SUE persistence; Katz, McCubbins and McMullin (2018 working paper, "The Post-Earnings Announcement Drift: An Anomalous Anomaly", read) replicate the portfolio drift but argue it is an aggregation artifact at the firm level. Correction from the UCLA Anderson summary (read): the two 2025 papers I had listed as PEAD-disagreement papers are, per that summary, Dickerson-Julliard-Mueller, "The co-pricing factor zoo" (JFE, in press; a joint stock-and-bond factor-zoo paper that uses an announcement-return-based earnings-drift factor) and Hirshleifer-Peng-Wang, "News diffusion in social networks and stock market reactions" (RFS 38(3):883-937, 2025). Neither is primarily a PEAD-existence paper; they matter because Subrahmanyam (SSRN 5930255, working paper, February 2001 to December 2024 US sample) criticises them for not filtering microcaps and for using price-based rather than accounting-based surprises. I have read none of the three papers, only the UCLA summary.

## 3. Economic rationale and who is on the other side

- Underreaction to persistence. Bernard and Thomas attribute the drift to investors who fail to appreciate how current earnings imply future earnings (the earnings-change autocorrelation pattern: positive at the first three seasonal lags, negative at the fourth), per a Wikipedia summary of their 1990 work (secondary). The "fail to recognize fully the implications of current earnings for future earnings" conclusion is also quoted by Katz et al. (read) from the 1989 paper.
- Limited attention and distraction (Hung-Li-Wang 2015 RFS, snippet: drift shrinks after a reporting-quality shock, most among firms with fewer simultaneous announcements, more institutional holders, and lower limits to arbitrage).
- Limits to arbitrage. Mendenhall (2004, snippet): drift magnitude relates strongly to arbitrage risk; Livnat (2003 working paper, read): the drift is stronger when the revenue surprise agrees with the earnings surprise and when earnings persistence is greater. Illiquidity, low institutional ownership and thin analyst coverage matter (Wikipedia, Quantpedia summaries).
- Risk-based alternatives (secondary): unpriced risks such as expected-growth exposure or liquidity risk; the evidence that long-short PEAD profits are positive in most down markets argues against a simple risk premium (Bernard and Thomas figure: spread positive in 41 of 48 quarters 1974 to 1985, 11 of 16 quarters with falling NYSE, secondary).
- Counterparties: slow-to-update investors, retail traders and benchmarked institutions that incorporate earnings news over weeks; informed institutions who trade ahead of the release (Martineau cites evidence that sophisticated traders trade on information before the announcement, leaving less drift after).

## 4. Canonical rules

Quantpedia's description of the Brandt-Kishore-Santa-Clara-Venkatachalam design (read), the closest thing to a precise canonical recipe I found:
- Universe: NYSE, AMEX, Nasdaq stocks, excluding financials, utilities and stocks priced under $5.
- Signals: SUE = (actual EPS minus seasonal-random-walk-with-drift expected EPS) divided by the standard deviation of surprises. EAR = three-day abnormal return centred on the announcement date, versus a risk-matched portfolio.
- Sort into quintiles on each signal using prior-quarter breakpoints (avoids look-ahead), equal-weight.
- Long the intersection of top SUE and top EAR quintiles, short the intersection of bottom quintiles.
- Enter on the second day after the announcement, hold about 60 working days, rebalance quarterly.
- Variants: analyst-forecast surprise rather than time-series SUE (Livnat and Mendenhall 2006 find bigger drift with analyst-based surprises, snippet; combining both is better than either, per the FAJ follow-up, snippet); revenue-confirmation filter (Livnat 2003); long-only.
- Martineau's measure (read): buy-and-hold abnormal returns from day 2 to day 60 after the announcement, by analyst-surprise quintile; he uses a market-cap split at the NYSE 20th percentile (microcap vs "all-but-microcap").

## 5. Evidence

Label: P = peer-reviewed, W = working paper, V = practitioner/vendor, U = unverified.

- (P/W, read in CFR draft form) Martineau 1984 to 2019 (abstract: for large stocks the drift has been non-existent since 2006 and only disappeared for microcaps recently): announcement-day price response to earnings surprise is much larger now: for all-but-microcap (microcap) stocks the BHAR[0,1] coefficient on surprise rank rose from about 20 (30) bps in 1984 to 1990 to about 120 (100) bps in 2016 to 2019, and R-squared rose from 1.7% to 11.7% (2.4% to 9.2%). The relation between analyst surprise rank and post-announcement BHAR[2,60] is not significant for all-but-microcap stocks after 2005, and for microcaps only from 2016. From 2011 there are no pronounced drifts in his quintile plots. Pre-announcement drifts also weakened, so "more leakage" does not explain it. Caveat: his preferred surprise is analyst-based and he conditions on analyst coverage; others dispute the design.
- (W, read) Kettell-McInnis-Zhao (sample 1974Q2 to 2020): hedge PEAD (top vs bottom SUE decile BHAR from day 2 to the next announcement +1) has a regression intercept of 6.24% (t 8.49) at the start of the sample and a trend of -0.020 percentage points per quarter (t -3.06), about 2 bp per quarter. Their five-year moving-average plot is described as staying above 2% throughout and falling from about 5% in the 1980s to 1990s to about 4% in the 2000s and early 2010s to 3% or lower in the late 2010s; the introduction separately says the hedge return is indistinguishable from zero after 2017. Second-pass reading: these two statements are reconcilable only as "small positive moving average, not statistically distinguishable from zero in the last years", so I would not quote either as a clean number. Once they control for declining SUE persistence, the downward trend is no longer significant, and this survives controls for arbitrage proxies. The published version in the Journal of Accounting, Auditing and Finance (2026) reportedly reaches the same conclusion (search summary, snippet).
- (W, read via UCLA summary; paper not read; SSRN page blocked) Subrahmanyam (SSRN 5930255, working paper): using US data February 2001 to December 2024, the earnings-drift factor has t-stat 2.18 with all stocks and 1.43 excluding microcaps (bottom 20% of NYSE market cap by his definition), which he reads as no significant drift in non-microcaps. He argues the 2025 papers that find drift (t about 14 in Hirshleifer et al.) include microcaps and use price-based, not accounting-based, surprise measures. Microcaps are about 3% of market value.
- (V, read) Quantpedia: long/short SUE+EAR quintile intersection, 1987 to 2004 source sample, about 15% per year indicative, max drawdown -11.2%, most return from the long side, small caps drive performance, hypothetical and not cost-adjusted. The source paper (Brandt et al., working paper) reports average abnormal return of about 7.55% per year for EAR and about 12.5% per year combined with SUE (via Quantpedia; I did not read the paper). Quantpedia also notes an FAJ study (not identified in what I read) finding that transaction costs consume 70% to 100% of paper profits of a long-short earnings-momentum strategy; treat as secondary.
- (V, read) Sojka-based Quantpedia review "50 Years in PEAD": reported abnormal returns vary from about 2.6% to 9.37% per quarter across studies; Dechow et al. (2013) estimate about 6% over 60 days with a third of the earnings reaction delayed; returns have been lower and riskier since the mid-1990s. Cross-study comparability is poor (different surprise definitions and universes).
- (W/secondary, read) Wikipedia summary: spread between high- and low-SUE portfolios fell from about 5% in the 1980s to 1990s to 3% or less by the late 2010s (this matches the Kettell et al. five-year moving-average description, which I read); Bernard-Thomas 1990 zero-investment portfolios "8 to 9% per quarter (about 35% annualized)". The per-quarter versus annualised wording is internally inconsistent and I could not check it against the paper; I do not rely on those figures. Katz et al. (read) say the PEAD hedge literature reports annual returns of roughly 10% to 25%, and cite a range of 8.76% (Sadka 2006) to 43.08% (Battalio-Mendenhall 2007) per year; those ranges are second-hand, and the wide spread shows the headline magnitude depends on surprise definition and universe.
- (W, read) Katz, McCubbins and McMullin (November 2018 working paper): sample 1985Q1 to 2014Q2, 243,826 firm-quarters from CRSP, Compustat and I/B/E/S, SUE deciles with cut-offs from the prior quarter. Their portfolio replication finds a risk-adjusted hedge return (good-news decile minus bad-news decile) of 5.1% over the three months after the announcement, over 20% annualised, so for their sample the drift shows up in the classic portfolio analysis; their point is that when portfolios are disaggregated to percentiles and by time the monotone pattern breaks down and the drift may be an artifact of aggregation. In the passages I read I saw no microcap exclusion, so their result is not in direct conflict with Martineau's all-but-microcap finding; I did not check whether size-weighted or equal-weighted. Treat as a dissent on design, not a refutation of the decay evidence.
- (P, abstract-level via search results of Deakin and RePEc records; full paper not obtained) Chordia and Shivakumar (2006 JFE 80(3):627-656): price momentum is captured by the systematic component of earnings momentum (a zero-investment SUE portfolio subsumes past returns), so PEAD and price momentum are not independent edges. Search results also point to Novy-Marx (a Rochester working paper I did not open) reaching a similar time-series result while noting it is identified mainly off small caps, and to a 2013 MIT Sloan thesis disputing the subsumption claim; both secondary and unverified.
- (P, abstract-level via search results; full paper not obtained) Livnat-Mendenhall (2006 JAR, pages 177-205, DOI 10.1111/j.1475-679X.2006.00196.x): drift is significantly larger when the surprise is built from I/B/E/S analyst forecasts and actuals than from a Compustat time-series model, and the gap is attributed to analyst-vs-time-series forecast differences, not to restatement or special items. The Lerman-Livnat-Mendenhall FAJ piece (2007, "double surprise", snippet via CFA Institute) reports combining both measures predicts returns better than either alone.
- (P, snippet) McLean and Pontiff: working-paper version (read) has 10% out-of-sample and 35% post-publication average decay across 82 characteristics; in the text I searched it does not break out PEAD. Published JF 2016 figures (97 predictors) remain snippet-level. Use only as a decay prior.
- (P, secondary) McLean and Pontiff-style decay is the right prior: published, simple, high-attention anomalies lose much of their return (see the working-paper figures above).

Net judgment: the "classic SUE PEAD" is a decayed, microcap-concentrated effect. The honest range for a post-2010, non-microcap, cost-aware implementation is roughly zero to small; I would not put capital behind it on published evidence alone. The residual, if any, may be in names with weak information environments. Second-pass refinement: the sources I could read split into (a) Martineau and Subrahmanyam, who find no significant drift in non-microcaps after about 2005 to 2006 (Subrahmanyam: t 1.43 ex-microcap vs 2.18 all stocks for 2001 to 2024), (b) Kettell et al., who find a smaller but not fully gone hedge return that depends on SUE persistence, and (c) Katz et al., who still find a 5.1% quarterly hedge return in 1985 to 2014 but question what it means. None of these is a net-of-cost, size-restricted, post-2015 replication using a method I can reproduce, so the question in section 12 item 1 stays open and the founding-paper magnitudes (Bernard-Thomas, Foster et al.) are still unchecked.

## 6. Failure regimes and risks

- Microcap dependence: the apparent drift lives in names that are expensive to trade, hard to short and low in capacity.
- Time variation: the factor is weak after 2005; periods of market stress (2008 to 2009, March 2020) cause large factor volatility and reversals.
- Gaps: you enter after the announcement, but the next-day continuation can be small relative to spread and slippage; extreme surprises can reverse (overreaction).
- Data traps: look-ahead in announcement timestamps (after-close vs pre-open), restated earnings, analyst data (I/B/E/S) coverage bias (Martineau shows analyst coverage excludes many microcaps), survivorship.
- Overlap with momentum/quality: PEAD loads on momentum (Chordia-Shivakumar); momentum crashes then hurt (see Daniel-Moskowitz momentum crash literature, not covered here).
- Crowding and event risk: concentrated entry days after reporting seasons create cluster risk and sector concentration.
- Short side: borrow cost and recalls are highest for bad-news small caps.

## 7. MY TWIST (hypotheses, NOT backtested)

Twist 1: Persistence-gated PEAD in non-microcaps.
- Rationale: Kettell et al. say the drift tracks how persistent earnings news is; Livnat (2003) says revenue-confirmed and more persistent surprises drift more.
- Rule change: from the standard SUE decile strategy, only trade a firm if (a) its SUE extreme is confirmed by a same-sign revenue surprise, and (b) its own history shows high SUE persistence (for example, correlation of consecutive-quarter SUE over the last 12 quarters above a threshold, or last quarter's SUE already in an extreme decile in the same direction). Universe: above the NYSE 20th percentile of market cap, price above $5.
- Parameters: persistence lookback {8, 12, 16 quarters}; correlation threshold {0.2, 0.3, 0.4}; revenue confirmation on/off; holding {20, 40, 60 days}.
- Expected effect: recover a modest positive drift in a smaller tradable subset; lower breadth and capacity; Sharpe better than the ungated version.
- Falsification: reject if, in 2010 to 2026 out-of-sample, the gated long-short spread is not significant (Newey-West t<2) after costs, or if it is not larger than the ungated spread with a bootstrap p<0.10, adjusted for the number of gates tested.

Twist 2: Underreaction filter (SUE high, announcement return muted).
- Rationale: if drift is underreaction, drift should be largest where the immediate price response is smallest relative to surprise size; Martineau shows the announcement response has grown, so residual drift may only exist where it has not.
- Rule: compute residual = EAR rank minus SUE rank. Go long stocks in top SUE quintile with EAR rank at most the median; short bottom SUE with EAR rank at least the median. Enter close of day +1 and hold 20 days.
- Parameters: EAR window {1, 3 days}; residual cutoffs {median, tercile}; hold {10, 20, 40}.
- Expected effect: concentrated, smaller basket; in exchange, higher per-trade drift; also reduces overlap with price momentum.
- Falsification: reject if the interaction between SUE and low EAR is statistically insignificant (t<2) in Fama-MacBeth regressions on post-2010 non-microcaps, or if the subset's net return after costs is below the full-sample SUE spread.

Twist 3: Text-based surprise add-on (speculative).
- Rationale: Meursault et al. (2021, via the Wikipedia summary only) report a text-based measure from earnings calls produces larger drift than classic PEAD. I have not read it.
- Rule: add an earnings-call tone/guidance surprise (for example from an LLM-scored transcript or a lexicon) as a third gate to Twist 1.
- Parameters: scoring method; delay (transcripts arrive hours after release, so enter day +1 close).
- Expected effect: unknown; text has information not in numeric SUE, but the result is also exposed to the "everyone reads transcripts now" decay.
- Falsification: reject if adding the text gate does not raise the post-2015 net information ratio of Twist 1 by at least 0.2 with a bootstrap p<0.10, or if the gain disappears out of sample.

## 8. Implementation spec

Data: point-in-time quarterly EPS and revenue (Compustat with report dates, or vendor with first-print values), analyst consensus (I/B/E/S), exact announcement timestamps (before-open, after-close), daily prices and volumes, shares outstanding, short interest and borrow fee, delisting returns, sector and factor returns, earnings call transcripts (twist 3).
Signals: SUE (seasonal random walk with drift, standardised by trailing 8-quarter surprise standard deviation); analyst surprise (actual minus consensus, scaled by price or by dispersion); EAR (three-day market-adjusted abnormal return, with the window set around the first tradable session); revenue surprise sign.
Sizing: equal-risk across names, 20 to 60 names per leg; cap 1% of NAV per name; sector neutral within 5%; beta-hedge with index futures; gross 1.5x to 2x for market-neutral.
Execution: entry at the close of day +1 (or open of day +2) to avoid the announcement spread blowout; stagger entries across the reporting season; limit participation to 5% of ADV.
Stops/exits: time exit at the earlier of day +60 or day -1 before the next announcement; stop on -12% from entry or 3x median daily vol; exit if a subsequent revision reverses the surprise sign.
Costs: half-spread 5 to 15 bps for non-microcaps (higher for small caps), market impact via square-root law, borrow 30 to 500 bps, commissions; stress 2x. Account for post-announcement spread widening explicitly.

Pseudo-code:
```
on each announcement e for stock s with ann_time t_e:
   entry_t = first_close_after(t_e + 1 trading day)
   if mcap[s] >= NYSE_p20 and px[s] >= 5 and adv_ok[s]:
       sue = SUE(s, e); rev = revenue_surprise_sign(s, e); ear = EAR(s, e)
       gate = persistence_ok(s) and sign(sue)==rev          # twist 1
       if decile(sue)==10 and gate: schedule_long(s, entry_t, exit=min(entry_t+60d, next_ann(s)-1d))
       if decile(sue)==1  and gate: schedule_short(s, entry_t, exit=...)
portfolio: beta-hedge, sector-neutral, cap names, size by inverse vol
```

## 9. Backtest plan

- Period/universe: 1984 to 2026 (analyst data) with sub-periods 1984 to 1999, 2000 to 2009, 2010 to 2026; separate microcap and non-microcap results (NYSE 20th percentile breakpoint as in Martineau and Subrahmanyam).
- Walk-forward: design gates on 1984 to 2009, validate on 2010 to 2018, untouched test 2019 to 2026; also run with expanding window.
- Controls: Fama-MacBeth with SUE, EAR, momentum, size, B/M, revisions; factor alphas (FF5 + momentum + liquidity); placebo with announcement dates shifted.
- Multiple testing: log every gate/threshold; use deflated Sharpe, Benjamini-Hochberg, and white-reality-check style bootstrap; report t-stats against a hurdle of about 3 (Harvey-Liu-Zhu style) for the final candidate.
- Costs: time-varying spreads and impact, borrow; compare gross vs net; reject if net drift is not positive in the 2010 to 2026 non-microcap subset.
- Metrics: net CAGR, Sharpe, max drawdown, hedge return by decile (monotonicity), holding-period profile (cumulative return by day since announcement), turnover, capacity, factor loadings, hit rate by season.

## 10. Risk management and kill-switch rules

- Position: 1% NAV max; sector and beta neutrality; hard stop as above; no new entries in names with halted/pending corporate actions.
- Portfolio: gross cap; daily loss limit 1.5% NAV; max 25% of risk in any reporting-week cohort.
- Kill-switches (my thresholds): (1) suspend if the rolling 8-quarter net hedge return is negative at a Newey-West t below -1, (2) suspend if factor loading on momentum exceeds 0.6 and momentum drawdown exceeds 15%, (3) suspend if realised slippage is 2x the model for two consecutive weeks, (4) suspend if the share of P&L from names below the NYSE 20th percentile exceeds 50% (the strategy has drifted into the untradable zone), (5) review quarterly against the latest published evidence (the academic debate is unresolved).

## 11. Annotated sources

| # | Source | URL | Type | Grade | Read? |
|---|---|---|---|---|---|
| 1 | Martineau, Rest in Peace PEAD (CFR 2022) | https://cfr.ivo-welch.org/published/papers/martineau2021rest.pdf | Peer-reviewed | A | Read |
| 2 | Kettell, McInnis, Zhao, Why Has PEAD Declined? (2022 WP) | https://business.columbia.edu/sites/default/files-efs/imce-uploads/CEASA/Events%20Page/PEAD_Declined_over_time.pdf | Working paper | B+ | Read |
| 3 | UCLA Anderson research brief on Dickerson et al. (co-pricing factor zoo), Hirshleifer et al. (news diffusion), Subrahmanyam | https://anderson-review.ucla.edu/is-post-earnings-announcement-drift-a-thing-again/ | Academic summary | B | Read (re-read second pass to fix paper titles) |
| 4 | Subrahmanyam, Keeping it Simple: How Can Post-Earnings Return Drift Exist and Not Exist Simultaneously? (SSRN 5930255, working paper per UCLA summary) | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5930255 (blocked); earlier cited https://sciencepublishinggroup.com/journal/179/archive/1791501 (not re-opened; venue unconfirmed) | Working paper | B- | Numbers via UCLA summary only; paper not read |
| 5 | Livnat, PEAD: role of revenue surprises and persistence (2003 WP) | https://archive.nyu.edu/bitstream/2451/27572/2/SSRN-id416302.pdf | Working paper | B | Read (abstract and introduction) |
| 6 | Livnat and Mendenhall (JAR 2006) | https://academicnewsletter.sufe.edu.cn/info/413468 | Peer-reviewed | A | Abstract-level via search results; full text not obtained |
| 7 | Mendenhall, Arbitrage risk and PEAD (J Business 2004) | https://ideas.repec.org/a/ucp/jnlbus/v77y2004i4p875-894.html | Peer-reviewed | A | Snippet |
| 8 | Hung, Li, Wang (RFS 2015) | https://ideas.repec.org/a/oup/rfinst/v28y2015i4p1242-1283..html | Peer-reviewed | A | Snippet |
| 9 | Chordia and Shivakumar (JFE 2006) | https://ideas.repec.org/a/eee/jfinec/v80y2006i3p627-656.html | Peer-reviewed | A | Abstract-level via search results (Deakin, RePEc); full text not obtained |
| 10 | Quantpedia, Post-Earnings Announcement Effect | https://quantpedia.com/strategies/post-earnings-announcement-effect/ | Aggregator | B- | Read |
| 11 | Quantpedia, 50 Years in PEAD research (Sojka) | https://quantpedia.com/?p=4238 | Review summary | B- | Read |
| 12 | Wikipedia, Post-earnings-announcement drift | https://en.wikipedia.org/wiki/Post%E2%80%93earnings-announcement_drift | Encyclopedia | C+ | Read |
| 13 | Bernard and Thomas (JAR 1989) | https://www.jstor.org/stable/2491063 | Peer-reviewed | A | Not read (paywalled; secondary only) |
| 14 | Bernard and Thomas (JAE 1990, 13(4):305-340) | https://deepblue.lib.umich.edu/handle/2027.42/28288 | Peer-reviewed | A | Not read: Deep Blue blocked (403 / bot wall); Unpaywall says closed access |
| 15 | Katz, McCubbins, McMullin, PEAD: An Anomalous Anomaly (2018 WP) | https://jkatz.caltech.edu/documents/28622/peads.pdf | Working paper | B | Read |
| 16 | Foster, Olsen, Shevlin (Accounting Review 1984), Stanford GSB WP listing | https://www.gsb.stanford.edu/faculty-research/working-papers/earnings-releases-anomalies-behavior-security-returns | Peer-reviewed / WP listing | A (paper) | Listing page only; paper not read |
| 17 | McLean and Pontiff working paper (2013), decay prior | https://ivey.uwo.ca/media/3775549/pontiff.pdf | Working paper | A- | Read full text |
| 18 | Crossref and Unpaywall records for Bernard-Thomas 1990 | https://api.crossref.org/works/10.1016/0165-4101(90)90008-R | Bibliographic metadata | A (metadata) | Read |

## 12. Open questions

1. Is there any net-of-cost, tradable drift left in stocks above the NYSE 20th percentile after 2010? Martineau and Subrahmanyam say no; Kettell et al. find a smaller, persistence-dependent hedge return; Katz et al. still find a 5.1% quarterly hedge return in 1985 to 2014 on an unrestricted-looking sample. (The 2025 Hirshleifer et al. and Dickerson et al. papers are not mainly PEAD tests; see section 2.) Needs my own replication with a point-in-time pipeline.
2. How much of the decline is falling SUE persistence (Kettell et al.) vs more arbitrage vs faster announcement-day pricing (Martineau)? The tests are not mutually exclusive.
3. Does earnings-call text or revenue confirmation add independent information after 2015?
4. Is the post-announcement window already traded pre-announcement (informed trading), as Martineau suggests, making a pre-announcement strategy more promising?
5. How do international markets behave post-2010?
6. What is the actual capacity at 5% ADV and realistic spreads in the tradable subset?

## 13. Second-pass changelog (2026-10-07)

Read in full this pass: Martineau CFR draft (re-opened to confirm the abstract and the BHAR[0,1] 20/30 to 120/100 bp and R-squared 1.7% to 11.7% / 2.4% to 9.2% figures; they hold); Kettell-McInnis-Zhao working paper (re-opened); Katz-McCubbins-McMullin 2018 working paper (new); McLean-Pontiff 2013 working paper (new, decay prior); UCLA Anderson summary (re-read); Crossref and Unpaywall metadata for Bernard-Thomas 1990.
Tried and failed: Bernard-Thomas 1990 (Deep Blue 403 and bot wall, Nimble returned empty page chrome, Unpaywall closed access); Bernard-Thomas 1989 (JSTOR/Wiley); Foster-Olsen-Shevlin 1984 (listing page only); Chordia-Shivakumar and Livnat-Mendenhall (no open full text found; abstract-level via search results); Subrahmanyam SSRN 5930255 (blocked); Hirshleifer-Peng-Wang and Dickerson-Julliard-Mueller (not opened); Berkman et al. is a B2 source and not relevant here.

Changes:
- Bernard-Thomas: the Wikipedia-derived figures stay demoted; added exact citation data and the access failures so the next pass does not repeat them. Mechanism (underreaction to implications of current earnings) now corroborated via two read papers that quote it, but no primary drift magnitudes obtained. Sample-period inconsistency (1974 to 1985 vs 1986) and 41-of-48 quarters remain unverified.
- Foster-Olsen-Shevlin: listing page opened; 56,000-observation and 1974 to 1981 details are from a search summary only and flagged unverified.
- Correction: the "Dickerson-Julliard-Mueller (2025 JFE)" and "Hirshleifer-Peng-Wang (2025 RFS)" PEAD-dispute framing was wrong or at best loose. Per the UCLA summary their titles are "The co-pricing factor zoo" and "News diffusion in social networks and stock market reactions", and they enter the PEAD debate via Subrahmanyam's critique. Subrahmanyam is an SSRN working paper (5930255), not a confirmed journal article; the earlier sciencepublishinggroup link was not re-verified.
- Kettell et al.: resolved the apparent inconsistency as far as the text allows (regression trend of -0.020 pp per quarter from a 6.24% intercept, moving average still above 2%, introduction says indistinguishable from zero after 2017); added sample 1974Q2 to 2020.
- Added Katz et al. as a dissenting-design source (1985Q1 to 2014Q2, 5.1% three-month risk-adjusted hedge return, aggregation-bias critique) and the 8.76% to 43.08% literature range they cite.
- Martineau: added the abstract's headline (large stocks, no drift since 2006); figures re-confirmed.
- Livnat-Mendenhall and Chordia-Shivakumar: stay abstract-level; added citation details and the Novy-Marx and MIT thesis caveats (secondary, unopened).
- Source grades: Subrahmanyam B to B-; Chordia-Shivakumar and Livnat-Mendenhall relabelled abstract-level; new rows 14 to 18.
- Judgement change: from "decayed, microcap-concentrated" to "contested: three read sources disagree on whether any size-restricted drift survives, and none gives a net-of-cost post-2015 test". Still no capital recommendation.
- Unchanged: section 7 twists (still untested), sections 8 to 10. No reproduction run for B3 (no free earnings-surprise data).
