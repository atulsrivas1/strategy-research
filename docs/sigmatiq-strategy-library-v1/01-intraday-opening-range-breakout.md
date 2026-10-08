# 01. Opening Range Breakout — Twist: ORB-VF

> **Library:** Sigmatiq Strategy Library | **Bucket:** Intraday | **Style:** Momentum / volatility-expansion breakout
> **Instruments:** US index futures (MNQ/NQ, MES/ES), QQQ/SPY, liquid large-caps | **Typical holding period:** 15 min – 3 h, flat by close | **Complexity (1–5):** 2 | **Evidence grade (A–C):** B
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise.

## 1. Origin & lineage

**Toby Crabel — the primary source.** The ORB was codified in Toby Crabel's *Day Trading With Short Term Price Patterns and Opening Range Breakout* (Traders Press, 1990, 288 pp., ISBN 0934380171). The book is out of print and trades for >$1,000 on the secondary market — a frequently cited sign of its durability (Trade Loss Tracker summary; time-price-research blog). Crabel was a systematic futures trader who later founded Crabel Capital Management; secondary sources describe him as having avoided a losing year from 1991–2002 and the *Financial Times* called him "the most well-known trader on the counter-trend side" (time-price-research blog, accessed via search excerpt). The book's premise: the first minutes of a session contain disproportionate predictive information about the rest of the day, because overnight order accumulation, institutional positioning, and news response all execute in a compressed window. Crabel tested his patterns statistically across multiple futures markets — unusual rigor for a 1990 trading book. Linda Bradford Raschke endorsed the book and incorporated its concepts (book foreword, per the Crabel PDF circulating online).

**Floor-trader practice and Market Profile.** The ORB is the same object as the "Initial Balance" in Auction Market Theory / Market Profile (CBOT, Pete Steidlmayer, 1980s): the range established in the first hour, whose extension signals "other-timeframe" initiative participation. Floor traders used the opening range as the day's reference frame long before it was published; Crabel's contribution was to quantify it (stretch, NR4/NR7 filters) and computer-test it.

**Mark Fisher — ACD.** Mark B. Fisher, founder of MBF Clearing Corp. (grew from <1% to ~20% of NYMEX clearing volume; the youngest-ever silver-pit trader at 21, Wharton 1982), published *The Logical Trader* (Wiley, 2002; foreword by Paul Tudor Jones). Per the publisher, Fisher taught the ACD method to 5,000+ traders including at Tudor Investments, and the system "is profitably implemented by many computer and floor traders at major New York exchanges" (Wiley-VCH book page). ACD is an ORB with explicit bias-reversal logic (A/C entry points, B/D exit points) and volatility-calibrated per-market offsets.

**Modern retail wave.** Andrew Aziz (*How to Day Trade for a Living*, 2015; Bear Bull Traders) popularized the 5-minute ORB on equities. Carlo Zarattini & Andrew Aziz's SSRN paper "Can Day Trading Really Be Profitable?" (April 2023, SSRN 4416622) gave the strategy academic-style packaging with a QQQ/TQQQ backtest 2016–2023 — and attracted replication attempts that are sharply less flattering (Sec. 3). A large retail education industry now sells ORB variants, including a viral "81% win rate" fixed-target version that independent testing shows is breakeven (tick-stream, Sec. 8).

**How it is actually used today.** Prop desks and systematic intraday funds use the opening range mostly as a *reference structure* (context for continuation/failure) rather than a standalone mechanical entry; retail uses it mechanically on 5/15/30/60-minute ranges. Our twist treats the ORB as a *regime-conditioned* continuation signal, not a universal entry.

## 2. The original rules (as published)

### 2.1 Crabel (1990)

- **Opening range (OR):** high–low of a chosen initial interval. Crabel tested 1, 5, 10, 15, and 30-minute opening ranges; modern practice uses 5/15/30/60 (Trade Loss Tracker summary; BigShort help center via search excerpt).
- **Basic ORB entry:** buy stop above the opening-range high, sell stop below the opening-range low; first side triggered is the position; the opposite side of the range is the protective stop. Hold for a predetermined period (Crabel tested intraday through next-day close).
- **Stretch variant:** enter at Open + Stretch (long) or Open − Stretch (short). **Stretch** = 10-day average of the daily adverse excursion from the open. *Sources disagree on the exact formula:* the common rendering is "average of the *smaller* of (High − Open) and (Open − Low) each day, over 10 days" (time-price-research blog excerpt); the Trade Loss Tracker summary renders it as "for up days (close > open): Open − Low; for down days: High − Open," averaged over 10 days. These are not identical; treat the exact definition as a parameter to pin down in replication. Both versions measure "normal rotational noise around the open."
- **ORBP (ORB with Preference):** if other indicators show a strong trend, place the stop-to-open only on the trend side (open ± stretch), protective stop on the other side.
- **Volatility-contraction filters (the core of the book):**
  - **NR4:** today's range is the narrowest of the last 4 sessions (~20–25% of days).
  - **NR7:** narrowest of the last 7 (~10–15% of days; larger subsequent expansions, lower false-signal rate).
  - **ID (inside day):** today's range inside yesterday's (~20% of days).
  - Combos: ID+NR4 (~8–10%), ID+NR7 (~4–5%), ID+NR4+NR7 (~2–3%) — progressively stronger as next-day ORB filters. Crabel's tests showed ORB performance is significantly better after contraction days than on random days (all frequencies from the Trade Loss Tracker summary).
- **Exit:** opposite side of OR as stop; alternately midpoint of the inside-day range; profit target 1.5–2× the inside-day range, or hold to close (per the summary's reconstruction).

### 2.2 Fisher ACD (2002)

- **OR:** first 5–30 minutes depending on the market (e.g., 15 min for S&P futures in the book's era).
- **Point A (entry):** price trades at OR high + A-value (A-up) or OR low − A-value (A-down) **and stays there for half the OR duration** (e.g., ~2.5 min for a 5-min OR; 7.5 min for a 15-min OR). A-values are market-specific volatility offsets: e.g., 3 points for the S&P 500 in the 2004 Investopedia example, $0.27 for Broadcom. Only one A per session.
- **Point B (stop):** the opposite boundary of the OR. A failed A-up is exited when price trades back through the OR low.
- **Point C (bias reversal):** if after an A-up the market breaks the OR and sustains at OR low − C-value for half the OR duration, reverse to short. C offsets are independently calibrated per market (book example: A-up ≈ +2.5–3 pts above OR high, C-down ≈ 6–8 pts below OR low in a ~2575-priced market; the Investopedia S&P example used C-down 0.5 pt below OR low — the offsets are per-market and per-era, do not copy numbers across instruments). "The later in the day a C occurs, the more intense the move" (Investopedia excerpt) — less time to exit reversals, more urgency.
- **Point D (stop on C):** 1 tick beyond the opposite OR extreme.
- **Pivot range:** daily pivot = (H + L + C)/3; pivot range = (2·Pivot − Low) to (2·Pivot − High); used as a multi-day reference with larger A/C values ("Macro ACD"). Fisher also layers pivot moving averages.
- Fisher's stated belief, unusual among system sellers: he shared the system freely because "the more people there are using it, the more effective it will be" (Investopedia excerpt) — i.e., he viewed ACD levels as self-reinforcing reference points.

### 2.3 Zarattini & Aziz (2023) — the modern mechanical version

- 5-minute OR on QQQ. Direction = sign of the first 5-min candle; enter at the **open of the second candle**; skip if the first candle is a doji (open = close).
- Stop: low of the first candle (long) / high of the first candle (short). Risk $R = entry − stop.
- Target: **10R** or end-of-day, whichever first. No partials.
- Sizing: risk 1% of account per trade, subject to a 4× leverage cap: Shares = int[min(A·0.01/$R, 4·A/P)]. $25,000 start, commission $0.0005/share, **no slippage assumed** (their Table 1 — a material caveat, see Sec. 3).
- Data: Interactive Brokers aggregated bars, MATLAB backtest, Jan 2016 – Feb 17, 2023.

### 2.4 Where published rules disagree

- **Entry trigger:** Crabel's stretch (open-relative) vs. OR-high/low break (modern) vs. sign-of-first-candle (Zarattini). These are materially different signals; the first-candle version enters much earlier and wider.
- **OR length:** 5 min (Zarattini, most retail), 15 min (Fisher S&P example; best robustness in the tick-stream NQ test), 30/60 min (fewer, more significant ranges).
- **Stop placement:** opposite OR extreme (Crabel/Fisher) vs. first-candle extreme (Zarattini) vs. mid-range (some practitioners).
- **Targets:** none/close (Crabel ride-it), fixed small target (viral retail), 10R (Zarattini), 2R (tick-stream's best). Evidence (Sec. 3) strongly favors letting winners run over small fixed targets.

## 3. Why it works — mechanism & evidence

**Mechanism.** (a) *Order-flow concentration:* the open aggregates market-on-open orders, overnight limits, and news response — the day's clearest read on net imbalance (Crabel's structural argument). (b) *Anchoring:* the OR is an objective reference; a break signals the opening consensus is challenged, triggering commitments from previously neutral participants — Fisher's self-reinforcement argument. (c) *Volatility cycling:* contraction (NR4/NR7/ID) stores energy; expansion follows contraction — the ORB is the directional trigger for the release. (d) *Intraday continuation:* equity indices exhibit positive intraday momentum once a real move out of the morning range commits (tick-stream's interpretation of their NQ results).

**Supporting evidence (all attributed, none ours):**

- Zarattini & Aziz (2023): 5-min ORB on QQQ 2016–Feb 2023 — total return 675% vs. 169% buy-and-hold; annualized alpha 33% net of commissions (p = 0.0025), beta ≈ 0, Sharpe 1.12–1.13, win rate 24%, avg +0.13R/trade over 1,795 trades (51% long). On TQQQ (to bypass the 4× leverage cap): 1,484% total return, alpha 48% (p = 0.0013), Sharpe 1.19, MDD 28%. They report the unconstrained-leverage QQQ version would have returned 1,630%.
- tick-stream (June 2026, NQ 5-min bars 2019–2026, lookahead-free, $4.50 + 2 ticks slippage, train 2019–2023 / holdout 2024–2026): 15-min OR breakout ridden to close +$176,402 (t = 1.69); 15-min breakout with 2R target +$205,612 (t = 2.09); 60-min breakout with gap-trend filter +$100,321 (t = 1.75). Profit factor ~1.1 — "a thin, real, out-of-sample-stable edge... plain intraday trend-following."
- backtestsnotsignals (Mar 2026, MNQ 2019–2026, Databento data, backtesting.py, $0.68/side, 150-tick stop cap, SMA-200 trend filter, one-loss-per-day rule): in-sample Sharpe 1.37, PF 1.43, win rate 30.4% (451 trades); out-of-sample Sharpe 1.10, PF 1.32, win rate 24.9% (474 trades), MDD −12.8%. Edge persists OOS but does not consistently beat buy-and-hold in absolute terms.
- sam-bateman/trading-orb (GitHub, 20 US stocks, 5-min bars 2016–2026, walk-forward, volume filter): 4,292 trades, win rate 50.3%, PF 1.31, Sharpe 2.47, CAGR 2.71% at $400 risk/trade, beta ≈ 0; 19/20 tickers profitable; survives 3× slippage (author-reported; accessed via search excerpt — treat as unverified).

**Contradictory / decay evidence (the important part):**

- tick-stream: **fading** the opening range loses at every range length, significantly at 15 min (−$77,361, t = −4.0). The viral fixed-10-point-target breakout wins ~88% of the time but avg win ~$185 vs. avg loss ~$1,400 → PF ≈ 1.01, "a coin flip with commissions. High win rate is the hook, not the edge."
- QuantifiedStrategies (S&P 500, via search excerpt; direct fetch 403): "opening range breakout trading strategies don't work very well anymore"; best simple variant ~0.04%/trade; one filtered variant 198 trades, 0.27%/trade, 65% win, PF 2 — they attribute the difference to undisclosed filters.
- Independent replication of Zarattini & Aziz (mohitbgupta75 GitHub, accessed via search excerpt + repo page): paper replicates at $0.070/share edge with no slippage, but **break-even at ~2.2¢/share slippage**; with realistic slippage the edge shrinks to $0.020/share (t = 0.52, n.s.). An NQ 09:25-bar confirmation filter lifts it to $0.125/share (t = 2.05) — but **76% of the filtered PnL comes from 2022 alone**; the filter loses in 2017, 2020, early 2023. "ORB edges [look like] a volatility-regime effect, not a structural one."
- paperswithbacktest.com replication (accessed via search excerpt, not fetched directly): 16-year full-sample Sharpe **−0.06**; in-sample-to-publication 0.16; **post-publication Sharpe −0.84** over ~11 months. "The replication does not reproduce the paper's headline claim... leverage multiplies a negative expected return as faithfully as a positive one."
- Makeph/honest-backtest (GitHub, via search excerpt): intraday Donchian/breakout variants on MES/MNQ collapse out-of-sample (TRAIN PF 1.4–19, TEST negative) — the "textbook overfit signature" warning for breakout parameter tuning.

**Synthesis.** The continuation effect underneath ORB appears real but thin (PF ~1.1–1.3 in honest futures tests), is regime-dependent (concentrated in high-volatility periods like 2022), decays with publicity, and is extremely sensitive to costs/slippage and to exit design (letting winners run is essential; small fixed targets destroy it). This is exactly the profile that justifies a *filtered, regime-conditioned* variant rather than the mechanical original.

## 4. The twist: ORB-VF

ORB-VF = Opening Range Breakout with **V**olatility/**V**olume/**F**low-conditioning. Each modification targets a documented weakness:

1. **Gap-agreement / gap-fade gate (targets: false breaks on gap-shock days).** The replication literature shows ORB PnL concentrates in trending, high-vol regimes, and the tick-stream gap-trend filter helped (60-min + filter, t = 1.75). We formalize: trade the breakout only if (a) the overnight gap direction agrees with the breakout direction, **or** (b) the gap has been *faded back into the prior day's range* (gap fill) before the trigger — i.e., the opening auction has already absorbed the shock and re-established the prior value area. Breakouts against an unfilled gap are skipped: they are fighting the overnight information flow.
2. **Relative-volume gate (targets: dead-day chop).** Require RVOL-30 (first-30-min volume vs. 20-session median of the same window) ≥ 1.5. Rationale: continuation needs participation; the sam-bateman equity ORB attributes much of its robustness to a volume filter, and low-volume breakouts are the classic bull/bear trap.
3. **Opening VIX-spike skip (targets: disorderly opens).** Skip the day if VIX at 09:35 ET > 1.10 × prior VIX close (opening vol shock > 10%) or VIX ≥ 35 absolute. Rationale: on shock days the first hour is dominated by de-risking flow, stops are hunted, and slippage on stop entries is worst. *Honest tension:* the replication evidence says 2022-style high-vol regimes produced most ORB PnL — so this filter targets the *day-over-day spike* (shock), not the level regime. It is a validation target: if it removes more good days than bad, downgrade it to a size-reduction rule instead of a skip.
4. **Inverse range-width sizing (targets: wide-range stop-outs).** Size inversely to OR width relative to ATR(14, daily): wide opening ranges have less headroom left in the day and worse reward:risk to the opposite-side stop; narrow ranges (post-contraction, Crabel's NR4/ID days) get full size. This mechanizes Crabel's contraction insight at the intraday level.
5. **Time-stop by late morning + run-to-target exit (targets: the "let it run" requirement without overnight risk).** tick-stream and the Zarattini replication both show the edge is continuation; the fixed-small-target version is breakeven. We use a target at a multiple of the OR (default 2× OR) with a hard time-stop at 11:30 ET — if continuation hasn't materialized by late morning, the day's energy is spent; all flat by 15:55 ET regardless.

## 5. Full specification of the twist variant

**Universe.** Primary: MNQ/NQ and MES/ES futures (continuous front month, roll 5 days before expiry or on volume crossover). Secondary: QQQ/SPY; optional single-stock sleeve (mega-caps with tight spreads). One instrument per signal; no pyramiding.

**Data.** 1-minute bars (aggregate to 5-min for signals), RTH session 09:30–16:00 ET plus prior-day RTH high/low/close and settlement; ETH session for gap context; VIX 1-min; 20 sessions of time-of-day volume history; ATR(14) on daily bars.

**Definitions (all times ET):**

- OR window: 09:30–09:45 (15 min). ORH = high, ORL = low, ORW = ORH − ORL.
- ATRd = ATR(14) of daily RTH ranges.
- Gap g = (today's open − prior RTH close) / prior close. Gap direction = sign(g); material gap: |g| ≥ 0.25 × ATRd/prior close.
- Gap faded: after the open, price trades at or beyond the prior RTH close (gap fill) *before* the breakout trigger.
- RVOL30 = vol(09:30–10:00) / median[vol(09:30–10:00) over prior 20 RTH sessions].
- VIX spike: VIX(09:35) > 1.10 × VIX(prior close), or VIX(09:35) ≥ 35.

**Entry (stop orders, resting from 09:45:00):**

- Long trigger: price ≥ ORH + 1 tick. Short trigger: price ≤ ORL − 1 tick.
- Direction gate: take the long only if (g > 0 material) OR (g ≤ 0 and gap faded) OR (g immaterial); mirror for short.
- Participation gate: RVOL30 ≥ 1.5 (validation range 1.25–2.0).
- Vol-shock gate: no trades if VIX-spike condition true.
- Range sanity gates: skip if ORW > 0.60 × ATRd (day's range mostly spent; stop too wide) or ORW < 0.05 × ATRd (noise range).
- Entry window: triggers only between 09:45 and 11:00 ET. One entry per direction per day; **stop trading for the day after one full stop-out** (per backtestsnotsignals' fixed risk rule).

**Exits:**

- Stop: opposite side of the OR (long: ORL − 1 tick). If ORW > 0.35 × ATRd, use mid-OR instead (cap risk).
- Target: entry + 2.0 × ORW (validation grid 1.5–3.0). Scale out 50% at 1.5 × ORW, runner to target or time-stop (optional; default single exit).
- Time-stop: flatten at 11:30 ET if neither stop nor target hit. Hard flat 15:55 ET.

**Sizing:**

- Base risk: 0.5% of equity per trade (R_dollars).
- Width factor w = clip(0.5 × ATRd / ORW, 0.25, 1.5).
- Contracts = floor(R_dollars × w / (stop_distance × point_value)). Respect margin cap 4× equity notional.
- Skip the trade if computed size < 1 contract at w = 0.25.

**Costs & capacity.** Commission $0.68–$1.50/side (micros) or $4.50 round-trip + 2-tick slippage assumption on entries, extra 1 tick on stops (per tick-stream's conservative model). Capacity: micros/QQQ — effectively unconstrained at desk size; ES/NQ fine to mid-7-figures intraday.

**Parameters to validate (not optimize to a point):** OR length {10, 15, 20, 30}, RVOL30 {1.25, 1.5, 2.0}, target multiple {1.5, 2.0, 2.5, 3.0}, VIX-spike {1.08, 1.10, 1.15}, width-factor slope. Require a plateau, not a peak.

## 6. Failure modes & regime dependence

- **Low-volatility grind regimes (2017, 2023-type):** continuation weakens; the replication found the filtered ORB lost in 2017, 2020, early 2023. Expect the strategy to go flat-to-negative for quarters; the RVOL gate helps but does not eliminate this.
- **Volatility-regime concentration:** if most PnL comes from 2022-style bears, the strategy is short-vol-regime-long-gamma in disguise. Monitor rolling 120-day PnL attribution by VIX quintile.
- **Crowding/decay:** post-publication decay documented (paperswithbacktest: post-pub Sharpe −0.84). The 5-min ORB on QQQ is the most crowded variant; our 15-min + gates variant is less standard, which helps marginally.
- **Gap-shock whipsaw:** days with large gaps that *don't* fill and then break out against the gap are skipped by design — this will miss some huge trend days (e.g., news-driven repricing). Accept it; that's the cost of avoiding the trap days.
- **Same-bar stop/target ambiguity:** with 2× OR target and opposite-side stop, both can be inside one 5-min bar on violent days — backtests must use conservative stop-first fills (tick-stream caught a 33-sigma fake edge from exactly this class of bug).
- **Overnight-event days (FOMC, CPI, NFP):** 09:30 open after a scheduled 08:30 data release behaves differently; consider an event-calendar flag as a separate gate in validation.
- **Early-warning indicators:** rolling 60-trade PF < 1.0; false-break rate (trigger then close back inside OR within 15 min) rising above ~55%; RVOL gate pass-rate collapsing (regime shift to low participation); slippage realized > 1.5× model.

## 7. Validation protocol

**Status: no local backtest exists yet.** This library contains zero proprietary results; everything above is literature.

- **Data:** 1-min bars 2016–present for MNQ/NQ (or QQQ as proxy), Databento or equivalent; VIX 1-min; official RTH session times; handle futures roll explicitly (back-adjusted continuous for daily ATR/SMA context, unadjusted for trade prices — trades never span rolls since we're flat daily).
- **Splits:** chronological only. Train 2016–2021, validation 2022–2023, test 2024–present. No random k-fold (intraday autocorrelation leaks). Walk-forward re-fit of gates annually, anchored.
- **Cost/slippage model:** commission + 2 ticks per entry, 3 ticks on stops, target fills at limit (0 slippage but fill-risk haircut: assume 70% fill rate on target touches). Stress at 2× and 3× costs (the replication breakeven was ~2.2¢/share on QQQ — know our number).
- **Pitfalls specific to this strategy:**
  - *Look-ahead in gap-fill:* the "gap faded" condition must use only ticks before the trigger bar.
  - *Same-bar ambiguity:* stop-first fill assumption; report results under both orderings.
  - *First-candle doji / halts:* define behavior for halted opens and doji OR windows.
  - *Survivorship:* none for futures; for the equity sleeve use point-in-time universe.
  - *News-day selection bias:* do not exclude event days post-hoc; flag them as a sub-sample.
- **Robustness:** parameter-plateau heatmaps (reject single-point optima); bootstrap trade resampling CIs; placebo test (random direction with same gates — must be ~zero); regime sub-sampling by VIX quintile and by year; Monte Carlo of trade order for drawdown distribution.
- **Acceptance criteria:** OOS PF ≥ 1.15 and per-trade t ≥ 2 net of 2× costs; OOS Sharpe ≥ 0.8; max DD ≤ 2× in-sample DD; positive expectancy in ≥ 60% of calendar years; edge must survive removal of the single best year (regime-concentration test).

## 8. Sources read (annotated: title, author, URL, date accessed, what it says, what was taken)

1. **"Day Trading with Short Term Price Patterns and Opening Range Breakout — Extended Summary,"** Trade Loss Tracker (summary of Toby Crabel, 1990). https://tradelosstracker.com/library/book/141-day-trading-with-short-term-price-patterns-and-opening/extended — accessed 2026-10-07. PhD-level reconstruction of Crabel's full framework: OR definition and tested intervals, stretch calculation, NR4/NR7/inside-day definitions with approximate frequencies, ID+NR4 combo stats, ORB mechanics, AMT/Initial-Balance mapping. *Taken:* Crabel rule set in Sec. 2.1, pattern frequencies, volatility-cycle mechanism in Sec. 3, stretch-formula ambiguity note.
2. **"Does the NY Opening-Range Breakout Actually Work? We Tested Every Version on 7 Years of NQ,"** tick-stream blog, June 26, 2026. https://tick-stream.xyz/blog/does-opening-range-breakout-work-backtest-nq — accessed 2026-10-07. Full-matrix ORB test on NQ 2019–2026 with train/holdout, real costs, conservative fills. Fade loses (15-min t = −4.0); fixed-10pt target ~88% win but PF 1.01; 15-min breakout ridden/2R is the thin real edge (t ≈ 1.7–2.1, PF ~1.1); gap-trend filter helped the 60-min variant. *Taken:* evidence table in Sec. 3, exit-design rationale, cost model, same-bar-bug cautionary tale, 15-min OR choice.
3. **"Opening Range Breakout: Real Edge or Backtest Illusion?"** Ale, *Backtests Not Signals* Substack, Mar 4, 2026. https://backtestsnotsignals.substack.com/p/opening-range-breakout-real-edge — accessed 2026-10-07. MNQ ORB with SMA-200 trend filter, one-loss-per-day rule, 150-tick stop cap, margin modeling, Databento data. IS Sharpe 1.37 / OOS Sharpe 1.10, PF 1.43→1.32, win ~25–30%. *Taken:* trend-filter and one-loss-per-day precedents, stop-cap rationale, honest IS/OOS framing, futures backtest engineering notes (roll handling, point-value sizing).
4. **"Can Day Trading Really Be Profitable?"** Carlo Zarattini & Andrew Aziz, SSRN 4416622 (April 2023, rev. Feb 2024), full-text PDF via Concretum Group. https://concretumgroup.com/wp-content/uploads/2026/02/Can-Day-Trading-Really-Be-Profitable.pdf (SSRN page: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4416622) — accessed 2026-10-07. The 5-min ORB QQQ/TQQQ study: full strategy definition (first-candle direction, second-candle entry, 10R/EOD exit, 1% risk, 4× leverage cap, $0.0005/share commission, no slippage), results (675%/1,484% total returns, alpha 33%/48%, Sharpe 1.12–1.19, win 24%). *Taken:* complete published rule set in Sec. 2.3, headline claims in Sec. 3, and the no-slippage caveat that the replications attack.
5. **"The Logical Trader" publisher page,** Wiley-VCH (Mark B. Fisher, Wiley Trading Series, 2002). https://www.wiley-vch.de/en/areas-interest/finance-economics-law/the-logical-trader-978-0-471-21551-6 — accessed 2026-10-07. Book description, author bio (MBF Clearing, NYMEX, Wharton, 5,000+ students incl. Tudor traders), table of contents (Know Your ACDs; Pivot Concept; Macro ACD; Pivot Moving Averages). *Taken:* Fisher lineage and bio in Sec. 1, book structure.
6. **"Spotting Breakouts As Easy As ACD"** and **"Gauging the Strength of a Market Move With the ACD System,"** Investopedia (2004). https://www.investopedia.com/articles/technical/04/032404.asp and .../04/040704.asp — direct fetch **failed** (bot-wall / timeout, 2026-10-07); content accessed via search-engine excerpts. A/C entry and B/D exit definitions, 15-min S&P OR example (A-up +3 pts, C-down −0.5 pt), Broadcom $0.27 A-value, "later C = more intense move," Fisher's more-users-more-effective quote. *Taken:* ACD worked examples in Sec. 2.2 — flagged as excerpt-sourced.
7. **"The Logical Trader" full text,** idoc.pub mirror. https://idoc.pub/documents/the-logical-trader-vlr0rrp8pvlz — page fetched 2026-10-07 but only the overview shell rendered; substantive excerpts (Point C/D mechanics, half-OR time requirement, 2570s worked example) obtained via search-engine excerpt of the same document. *Taken:* ACD C/D rules in Sec. 2.2 — flagged as excerpt-sourced.
8. **Independent replication of Zarattini & Aziz,** mohitbgupta75/zarattini-2023-orb-qqq (GitHub). https://github.com/mohitbgupta75/zarattini-2023-orb-qqq — repo page fetched 2026-10-07 (README partially rendered); key figures also from search excerpt: breakeven ~2.2¢/share slippage; NQ 09:25 filter $0.125/share, t = 2.05; 76% of filtered PnL from 2022; placebo control n.s. *Taken:* decay/regime evidence in Sec. 3, cost-sensitivity framing in Sec. 7.
9. **"ORB Trading Strategy: What Replication Shows,"** paperswithbacktest.com. https://paperswithbacktest.com/strategies/orb-trading-strategy — **not fetched directly**; figures via search excerpt: full-sample 16-yr Sharpe −0.06, in-sample-to-publication 0.16, post-publication −0.84. *Taken:* post-publication decay claim in Sec. 3 — flagged as excerpt-sourced.
10. **"Opening Range Breakout Strategy (ORB): Backtest,"** QuantifiedStrategies.com. https://www.quantifiedstrategies.com/opening-range-breakout-strategy/ — direct fetch **failed** (403, 2026-10-07); via search excerpt: simple S&P ORB variants ~0.04%/trade, "don't work very well anymore," one filtered variant PF 2. *Taken:* disagreement note in Sec. 3 — flagged as excerpt-sourced.

## 9. Further reading

- Toby Crabel, *Day Trading With Short Term Price Patterns and Opening Range Breakout* (1990) — the primary text; a circulating PDF was located (buysidedigest.com) but not fetched (binary/PDF unsupported by our fetch tool); obtain a copy for the desk library.
- Mark B. Fisher, *The Logical Trader* (Wiley, 2002) — full ACD methodology including pivot ranges and "Macro ACD."
- J. Peter Steidlmayer, *Markets & Market Logic* — Initial Balance / Auction Market Theory foundation underlying the opening range.
- Linda Bradford Raschke & Laurence Connors, *Street Smarts* (1995) — NR4/inside-day patterns in professional practice.
- Andrew Aziz, *How to Day Trade for a Living* (2015) — the retail 5-min ORB canon.
- BigShort help center, "Opening Range Breakout (ORB) Strategies" — modern practitioner taxonomy incl. "Golden Trend Day" (seen via search excerpt; fetch for the desk wiki).
- Makeph/honest-backtest (GitHub) — negative-result discipline for intraday breakouts on micros; read before any ORB parameter tuning.
- Carlo Zarattini's follow-up ORB work (Concretum Group) and community replications — track for post-2024 decay updates.
