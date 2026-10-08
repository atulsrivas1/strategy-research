# 02. VWAP Mean Reversion — Twist: AVWAP-Q

> **Library:** Sigmatiq Strategy Library | **Bucket:** Intraday | **Style:** Mean reversion / order-flow-confirmed fade
> **Instruments:** ES/NQ (MES/MNQ) futures, SPY/QQQ, liquid large-caps | **Typical holding period:** 15 min – 2 h, flat by close | **Complexity (1–5):** 3 | **Evidence grade (A–C):** B−
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise.

## 1. Origin & lineage

**VWAP as an execution benchmark (the institutional origin).** VWAP entered the literature as a *transaction-cost benchmark*, not a trading signal: Berkowitz, Logue & Noser, "The Total Cost of Transactions on the NYSE," *Journal of Finance* 43(1), March 1988, pp. 97–112. They proposed the day's volume-weighted average price as a market-impact measure "less biased than measures that use single prices, such as closes," and applied it to 14,000+ actual institutional trades (finding total costs averaging 23 bps of principal: 18 bps commissions + 5 bps execution). As Alphatrends paraphrases the paper: the VWAP "represents the price a 'naive' trader can expect to obtain"; a buy filled above VWAP is a bad fill, below VWAP a good one. The benchmark's simplicity made it the industry standard: in February 2021 congressional testimony (GameStop hearing), Citadel's Ken Griffin stated that "virtually all trades executed by institutional investors are in the form of program trades, such as VWAP and other algorithm trades" (quoted in the S&C interview with Brian Shannon). Modern TCA literature notes VWAP schedules are *gameable* — predictable participation makes large VWAP orders "easy prey for front-running by predatory high-frequency traders," and front-loading can game the benchmark (Bayesian TCA survey, arXiv:1904.01566, via search excerpt) — which matters to us mechanically: benchmarked flow is a large part of why price interacts with VWAP at all.

**Prop-desk / practitioner practice.** Because so much institutional flow is benchmarked to the day's VWAP, the session VWAP became the intraday "fair value" reference on equity and futures desks: above VWAP = buyers in control of the day, below = sellers. The fade variant — price stretched several standard deviations from VWAP tends to snap back on rotational days — is standard intraday practitioner lore, codified in countless desk playbooks and retail education (CrossTrade, satotrades, Traders Journal, HorizonAI — Sec. 8).

**Anchored VWAP (AVWAP).** The anchored variant — start the cumulative calculation at a user-chosen event instead of the session open — is credited by Brian Shannon to the late **Dr. Paul Levine**, whose work began in 1992. Shannon (CMT; Lehman broker from 1992; lead trader/director of research at MarketWise 1999–2006; founder of Alphatrends.net, 2010) popularized it: *Technical Analysis Using Multiple Timeframes* (2008), *Maximum Trading Gains With Anchored VWAP* (2023), and a 2015 push that got TC2000 to build point-and-click AVWAP ("anchored VWAP by Alphatrends"); it is now on a dozen+ platforms including TradingView. Shannon calls himself the "adoptive father" of AVWAP (CMT Fill The Gap interview, via search excerpt). His anchor doctrine: anchor to *supply/demand shocks* — earnings reports, FOMC meetings, the first trade of an IPO, price gaps, major swing highs/lows — plus time-based anchors (week/month/year-to-date).

**How it's actually used.** Two distinct camps: (a) *trend/continuation* — Shannon himself is a discretionary momentum trader who uses AVWAP to buy strength ("I'm not interested in buying the touch. I'm interested in buying the bounce"), entering when price reclaims an AVWAP with a higher high, stop under "the most recent and relevant higher low," scaling out a third quickly; (b) *mean reversion* — the intraday band-fade this document is about. Notable tension: the tool's most prominent advocate does **not** fade it mechanically and explicitly declines backtesting ("All my experience with VWAP/AVWAP comes from real-life trading... with the subjective nature of where to anchor the VWAP, it does not always lend itself well to backtesting" — S&C interview). Our twist therefore imports *confirmation* requirements from order-flow practice to make the fade systematic.

## 2. The original rules (as published)

### 2.1 Definitions

- **Session VWAP:** VWAP(t) = Σ(Pᵢ·Vᵢ) / ΣVᵢ, cumulative from the session open, reset daily. Shannon: "the total dollars traded for each transaction (price × volume) divided by the total shares traded. It builds from the first trade of the day and continues through the close." Use the shortest practical bar (tick data ideal; 1-minute adequate for all but scalpers — Alphatrends).
- **Volume-weighted SD bands (the standard practitioner construction, CrossTrade Pine v6):** variance = Σ(Pᵢ²·Vᵢ)/ΣVᵢ − VWAP² (using typical price HLC3 per bar); σ = √variance; bands = VWAP ± k·σ, k = 1/2/3. Bands widen when heavy volume trades away from the mean — correct behavior for a volume-weighted dispersion.
- **AVWAP:** identical recursion with the anchor bar chosen by the analyst; Shannon's accuracy note: compute from the shortest timeframe available.

### 2.2 The classic band-fade rule set (CrossTrade "VWAP Reversion," ES/NQ)

1. **Regime filter (mandatory):** skip days with FOMC/CPI/NFP/ISM releases; skip if ADX(14) on 5-min > 25; skip if opening-hour range > 2× its 20-day average.
2. **Setup:** price extends ≥ 2σ from session VWAP.
3. **Trigger:** rejection candle at the extreme — pin bar (wick > 2× body) or engulfing bar in the reversion direction, with a volume spike.
4. **Entry:** market order at next bar open after the trigger closes.
5. **Stop:** 1× ATR(14) beyond the trigger bar's high/low.
6. **Target:** VWAP itself (moving target, updated every bar); optionally half off at VWAP, trail the rest through to the far band.
7. **Session discipline:** RTH only (overnight volume too thin, bands noisy); flatten 15:55 ET. Best windows 10:00–11:30 and 13:30–14:30 ET; avoid 09:30–10:00 (opening momentum) and Friday afternoons (expiry flows).

### 2.3 Shannon's AVWAP usage (for contrast and for our anchor logic)

- AVWAP is "a zone for observation — a place to look for evidence, not a mechanical signal" (Alphatrends FAQ).
- Control logic: price above a rising AVWAP → buyers in control, "innocent until proven guilty"; below a declining AVWAP → "guilty until proven innocent"; oscillation across it → indecision/balance.
- Entry style: buy the *reclaim* (higher high back above the anchor AVWAP), never the touch; stop below the most recent relevant higher low; raise stops under successive higher lows; sell one-third quickly to de-risk.
- Volume doctrine: volume should expand in the trend direction, peak near turning points, and diminish on retracements; AVWAP "tells me with 100% certainty who has control from a certain start point" (S&C interview).

### 2.4 Where published practice disagrees

- **Band multiple:** 1σ (more, smaller reversions) vs. 2σ (working default) vs. 3σ (rare, extreme). CrossTrade warns 2σ→1.5σ "triples signal count and halves edge."
- **Touch vs. confirmation:** pure band-touch entries "fail frequently" (CrossTrade); rejection-bar confirmation is the standard fix; Shannon goes further and wants a full reclaim.
- **Session vs. anchored:** session VWAP for intraday fades; AVWAP from events/major pivots for swing context (CrossTrade FAQ: anchored fades become multi-day, lower win rate, higher R).
- **Trend-day behavior:** satotrades treats VWAP touches in trend days as *continuation* entries ("highest-hit-rate setup in the playbook") and band fades as rotation-only — the same level is a buy or a sell depending on day type. This is the central ambiguity our regime filter must resolve.

## 3. Why it works — mechanism & evidence

**Mechanism.** (a) *Benchmark gravity:* a large share of institutional execution is VWAP-benchmarked program flow (Griffin testimony, Sec. 1); execution algos buy below VWAP and sell above it, creating responsive flow that pushes price back toward the day's volume-weighted mean on days without directional information. (b) *Fair-value rotation:* in balanced (two-sided) auctions, price oscillates around the day's consensus value; a 2.5–3σ extension is statistically extreme given the day's own volume distribution, so marginal participation thins at the bands. (c) *Order-flow exhaustion:* if the push to the band is driven by aggressive market orders, cumulative delta should confirm it; when price prints a new extreme but CVD does not, the move is "drifting on inertia" (datanalyste, TradingView CVD excerpt) — aggressive flow is being absorbed by passive liquidity, the classic absorption setup (dhawal.org order-flow chapter). (d) *Anchored memory:* from an event anchor, the AVWAP is the average price of everyone positioned since the shock; touches put the average participant at breakeven, triggering defensive flow (Shannon's "who is trapped" framing).

**Evidence (all attributed, none ours):**

- CrossTrade (practitioner, ES/NQ): with filters (ADX, news, session timing) "55–65% win rate is realistic"; without filters "closer to 45% — reversion fails badly on trend days, and those failures dominate." Avg winner 0.8–1.2× avg loser; PF 1.2–1.6; 2–5 signals/day on ES in good regimes, often zero on trend days. Cost sensitivity flagged: "$2 round-trip on ES is meaningful when average winners are $75–$150."
- CuteMarkets (practitioner backtest blog; direct fetch failed with HTTP 500 — excerpt via search): a constrained VWAP-residual z-score model with slope/sigma/relative-volume filters made money on the "quality" settings (+16,004 PnL, 15 trades, DSR 0.64) but **failed their portfolio admission bar on trade frequency** (`trades_per_week_ok`) — the selectivity/density tradeoff: clean VWAP fades are rare.
- tick-stream's NQ ORB tests (doc 1 sources) independently corroborate the regime dependence from the other side: *fading* strong opening moves on NQ loses significantly (15-min fade t = −4.0) because "NQ trends intraday" — band fades must therefore be gated to balanced days, exactly as practitioners warn.
- dhawal.org order-flow chapter: "Order flow is confirmation, not trigger... at structure with order-flow confirmation, expected reaction rate substantially exceeds either signal alone"; BVC-estimated delta correlates ~0.85–0.95 with true tick-rule delta on liquid 5-min bars (Easley, López de Prado & O'Hara 2012 BVC method) — relevant to our data choices.
- No peer-reviewed study isolating a VWAP band-fade edge was found in this research pass; the academic VWAP literature is about execution benchmarking, not alpha. Say this plainly in the file: the fade edge is practitioner-documented only. Evidence grade B−.

**Decay/crowding.** VWAP bands are on every retail platform; the naive 2σ touch fade is heavily marketed. Practitioner consensus (CrossTrade, Traders Journal) is that the naive version is ~breakeven-to-negative and only regime + confirmation filters keep it alive — consistent with crowding at the obvious level and residual edge in the *selection*, not the level.

## 4. The twist: AVWAP-Q

AVWAP-Q = Anchored-VWAP fade, **Q**ualified by order flow and regime. Each component targets a documented failure of the naive fade:

1. **CVD / order-flow divergence required at the band (targets: fading a real institutional drive).** The naive fade's killer is the trend day where 2.5σ is "the trend, not an extension" (HorizonAI). We require *disagreement* between price and aggressive flow at the band: price prints a new session extreme at/beyond the 2.5σ band while session CVD prints a lower high (short) / higher low (long), or a footprint absorption signature appears (heavy aggressive delta into the band with no price progress — dhawal's "delta divergence within bar"). No divergence → no trade, however stretched price looks.
2. **Balanced-day regime gate (targets: trend-day bleed).** Two-part: (a) ADX(14, 5-min) < 20 at signal time (stricter than CrossTrade's 25); (b) opening-drive classification = "balanced": the first 60 min produced an opening range ≤ 0.75× its 20-day median AND price has re-crossed session VWAP ≥ 2 times since 10:00 AND |session CVD| / session volume < 10% (no one-sided flow day). All three must hold; otherwise the day is classified "driven" and fades are forbidden (on driven days, VWAP touches are continuation entries — satotrades — which is a different strategy, not this one).
3. **Anchor selection with event awareness (the "A" in AVWAP-Q).** Default anchor = session open (classic VWAP). On gap days (|gap| ≥ 0.5× ATRd) add a second AVWAP anchored at the prior day's close; on scheduled-event days (FOMC 14:00, CPI 08:30) anchor at the event bar. Trade only touches of the *active* anchor's band — the one whose band has already been respected intraday (first touch that produced ≥ 0.5σ reaction). This mechanizes Shannon's "anchor to supply/demand shocks" while removing his discretionary anchor choice.
4. **Band at 2.5–3.0σ, not 2.0σ (targets: crowding at the obvious level).** The marketed default is 2σ; we trade only 2.5σ+ touches (validation grid 2.5/2.75/3.0). Fewer, more extreme dislocations — accepting the CuteMarkets density warning: this strategy will have low trade frequency by design, and we size the book accordingly.
5. **Time exclusions and trade-frequency caps (targets: opening momentum and close flows).** No entries 09:30–10:00 or 15:30–16:00 ET. Max 2 entries/day; stop for the day after 1 loser. Flat 15:55 ET.
6. **Stop placement beyond the band + 1× ATR(14, 5-min) (targets: wick-through stop hunts).** The stop sits beyond the extreme *and* a volatility buffer, so a marginal new extreme that fails (the classic final flush) doesn't stop us out before the reversion works.

## 5. Full specification of the twist variant

**Universe.** Primary: MES/ES and MNQ/NQ futures (RTH). Secondary: SPY/QQQ. Single-name extension only for mega-caps with tight spreads and reliable tick-side delta.

**Data.** 1-minute bars (signal computation on 1-min, risk math on 5-min); tick-side trade classification for true delta if available, else BVC estimate (document the ~0.85–0.95 correlation caveat); 20 sessions of intraday history for medians; economic calendar feed.

**Formulas (session anchor a = first RTH bar; all cumulative from a):**

- VWAP(t) = Σ(Pᵢ·Vᵢ)/ΣVᵢ, Pᵢ = HLC3 of bar i.
- σᵥ(t) = sqrt( Σ(Pᵢ²·Vᵢ)/ΣVᵢ − VWAP(t)² ). Bands: U/L(k) = VWAP ± k·σᵥ, k = 2.5.
- z(t) = (Close(t) − VWAP(t)) / σᵥ(t).
- CVD(t) = Σ delta(i), delta(i) = volume_at_ask − volume_at_bid (or BVC: Vᵢ·(2Φ(rᵢ/σ_r) − 1)).
- ADX(14) on 5-min bars. ATR5 = ATR(14) on 5-min bars. ATRd = ATR(14) daily.
- Balanced-day test (evaluated continuously after 10:30 ET): ADX < 20 AND OR60 ≤ 0.75 × median(OR60, 20d) AND VWAP recrosses since 10:00 ≥ 2 AND |CVD| / ΣV < 0.10.

**Entry (short symmetric):**

- Setup: High(t) ≥ U(2.5) (touch or exceed) while balanced-day test passes.
- Divergence requirement: the session high at the band has CVD below its value at the prior session high (bearish regular divergence), OR the touch bar shows absorption (bar delta ≤ −1.5× median |bar delta| while closing in the upper third — aggressive selling absorbed at the highs; mirror for longs).
- Trigger: a 1-min close back **below** U(2.5) (rejection/reclaim of the band) within 10 bars of the touch. Enter short at market on the next bar open.
- No divergence or no reclaim within 10 bars → setup expires.

**Exits:**

- Stop: max(High since entry, band extreme) + 1.0 × ATR5. (One volatility unit beyond the extreme.)
- Target 1 (50%): VWAP(t) (moving; resting limit, updated per bar).
- Target 2 (50%): VWAP ∓ 0.5σ overshoot to the far side, or time-stop.
- Time-stop: 90 minutes after entry, or 15:30 ET, whichever first — reversion that hasn't worked by then is fighting something. Hard flat 15:55 ET.

**Sizing & risk:**

- Risk 0.40% of equity per trade: contracts = floor(0.004 × equity / (stop_distance × point_value)).
- Day stop: 1 losing trade or −0.6% equity, whichever first. Week stop: −1.5%.
- Cap: max 2 trades/day/instrument; no correlated doubling (ES and NQ signals same direction → take one, the higher RVOL).

**Costs & capacity.** Model $1.24–$4.50 RT commission (micro/mini) + 1 tick slippage on entry, 2 on stops, 0 on limits with 75% fill assumption. Note CrossTrade's warning: average winners are small ($75–150/contract on ES) — costs are first-order here, unlike in ORB. Capacity: high (fades provide liquidity; entries are into strength); micros unconstrained at desk size.

**Validation grid:** k ∈ {2.5, 2.75, 3.0}; ADX cap {15, 20, 25}; divergence lookback {prior session extreme vs. prior 2 extremes}; stop buffer {0.75, 1.0, 1.5} × ATR5.

## 6. Failure modes & regime dependence

- **Trend days (the killer):** unfiltered fades go from ~55–65% win to ~45% (CrossTrade); on NQ, tick-stream showed fading strong moves is a *significant* loser. Our ADX + balanced-day + divergence stack is the defense; if all three leak (strong day that looks balanced until noon), the day-stop caps the damage at one trade.
- **News shocks:** scheduled releases blow up reversion (CrossTrade, Traders Journal). Event-anchor logic handles the *aftermath*; entries within 15 min of a major release are forbidden.
- **Density/opportunity cost:** at 2.5–3.0σ with all gates, expect 0–3 signals/week/instrument (CuteMarkets' quality variant failed a trades-per-week admission bar). This is a *sleeve*, not a standalone business; measure it on per-trade expectancy, not utilization.
- **BVC delta noise:** without tick-side data, divergence signals are estimates (0.85–0.95 correlation); on low-volume bars the estimate degrades. Prefer true tick-side feeds (Rithmic/CME data via Databento) for production.
- **Anchor ambiguity:** the "active anchor" rule can still pick wrong on days respecting neither anchor. Log both anchors in research; if anchor-selection accuracy < 60%, simplify to session VWAP only.
- **Late-day trend resumption:** 15:30+ flows (MOC, rebalancing) trend hard; hence the entry cutoff and 15:55 hard flat.
- **Early-warning indicators:** rolling 40-trade win rate < 50%; avg loser > 1.5× avg winner (target logic failing); divergence-then-continuation rate > 40% (order-flow confirmation decaying — crowding of CVD signals); band touches per week collapsing (vol regime shift — reduce activity, not standards).

## 7. Validation protocol

**Status: no local backtest exists yet.** All numbers above are attributed practitioner claims.

- **Data:** 1-min bars + tick-side trades (or BVC with documented error), 2018–present, RTH; economic calendar; 20-day rolling intraday medians computed strictly from prior sessions.
- **Splits:** chronological — train 2018–2021, validation 2022–2023, test 2024–present; walk-forward annual re-fit of the gate thresholds only (band multiple stays fixed to avoid the 2σ→1.5σ overfitting trap CrossTrade warns about).
- **Cost model:** as Sec. 5; report edge in ticks/trade and demand survival at 2× costs. Given small average winners, also report expectancy per unit of *time in market* (capital is free when flat).
- **Strategy-specific pitfalls:**
  - *Path dependence:* VWAP/σᵥ are cumulative — any bug that leaks future volume into the day's bands is fatal; unit-test the recursion against a known-good platform (e.g., TradingView `ta.vwap`) bar-by-bar.
  - *Divergence repainting:* define divergences only on *confirmed* pivots (pivot confirmed by N×ATR reaction, per the datanalyste/BT indicator discipline) — never on live forming pivots in backtest.
  - *Same-bar stop/target:* stop-first conservative fills; report both orderings.
  - *Anchor-selection look-ahead:* "the anchor that was respected" must be determined from data available at signal time only.
  - *Survivorship:* none for futures; point-in-time universe for the equity sleeve.
- **Robustness:** plateau check across the validation grid; regime sub-samples (VIX quintiles, trend/balanced day split by an *ex-post* classifier to measure gate leakage); bootstrap CIs on per-trade R; placebo (fade at random intraday times with same exits — must be ~zero).
- **Acceptance criteria:** OOS win rate ≥ 55% with avg winner ≥ 0.8× avg loser (the practitioner-claimed shape), PF ≥ 1.3 net of 2× costs, per-trade t ≥ 2, ≤ 1 losing day in 3, and the balanced-day gate must demonstrably reduce trend-day losses (report gate-on vs. gate-off).

## 8. Sources read (annotated: title, author, URL, date accessed, what it says, what was taken)

1. **"When, Where, Why to Set Anchored VWAP,"** Brian Shannon, Alphatrends. https://alphatrends.net/when-where-why-to-set-anchored-vwap/ — accessed 2026-10-07. VWAP definition and 1988 origin (Berkowitz/Logue/Noser); AVWAP definition; anchor doctrine (earnings, Fed, IPO first trade, gaps, swing H/L, WTD/MTD/YTD); control rules ("innocent until proven guilty"); "zone for observation, not a mechanical signal"; compute from shortest timeframe. *Taken:* Sec. 1 lineage, Sec. 2.1/2.3 rules, anchor logic for the twist.
2. **"A Conversation With Brian Shannon,"** Leslie N. Masonson, *Stocks & Commodities* V41:07 (April 2023). https://technical.traders.com/free/V41C07645INTE.pdf — accessed 2026-10-07. Career bio; VWAP calculation in his words; Ken Griffin congressional quote on program/VWAP trading; Paul Levine credited with AVWAP (1992); TC2000 2015 implementation; "buy strength after the dip," stop under most recent relevant higher low, one-third scale-out; his explicit refusal of backtesting. *Taken:* Sec. 1 lineage and quotes, Sec. 2.3, the honesty note that AVWAP's champion is anti-mechanical.
3. **"The Total Cost of Transactions on the NYSE,"** Berkowitz, Logue & Noser, *Journal of Finance* 43(1):97–112, March 1988 (Wiley page). https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.1988.tb02591.x — accessed 2026-10-07. The VWAP benchmark's origin; 14,000-trade sample; 23 bps total cost (18 commission + 5 impact); VWAP as less-biased impact measure. *Taken:* Sec. 1 origin story and benchmark mechanics.
4. **"VWAP Reversion,"** CrossTrade learn series (April 2026). https://crosstrade.io/learn/trading-strategies/vwap-reversion — accessed 2026-10-07. The most complete published mechanical fade spec found: news/ADX(>25)/opening-range regime filters, 2σ setup, rejection-candle trigger, 1×ATR stop, VWAP target, 15:55 flatten, best/worst session windows, full Pine v6 code with volume-weighted variance, realistic performance claims (55–65% filtered vs ~45% unfiltered, PF 1.2–1.6), and the 2σ→1.5σ overfitting warning. *Taken:* the baseline rules of Sec. 2.2, evidence of Sec. 3, cost warning, several twist targets.
5. **"Order Flow: Footprint, Delta, CVD, Absorption,"** dhawal.org, *Technical Analysis for Futures Traders*, ch. 11. https://dhawal.org/research/futures-ta/chapters/ch11-order-flow — accessed 2026-10-07. Delta/CVD math with true tick-side data; BVC estimation (Easley–López de Prado–O'Hara 2012) with 0.85–0.95 correlation on liquid 5-min bars; absorption and delta-divergence patterns; "order flow is confirmation, not trigger"; range-day fade-with-sweep setup. *Taken:* divergence/absorption definitions in Sec. 4–5, data-caveat in Sec. 6–7.
6. **"Build a VWAP Mean Reversion Strategy in Pine Script v6,"** HorizonAI. https://www.horizontrading.ai/learn/build-a-vwap-mean-reversion-strategy-in-pine-script-v6 — page fetched 2026-10-07 (saved); key content via search excerpt: session-anchored `ta.vwap` bands, 2.0 SD default, reversal-close trigger, ATR stop fixed at entry, moving VWAP target, ADX(14)<25 gate, "price touching 2 SD on a strong trend day isn't an extension, it's the trend." *Taken:* corroboration of Sec. 2.2 and the trend-day failure framing — flagged as excerpt-sourced.
7. **"VWAP Trading Strategy for ES/NQ Futures (2026),"** satotrades. https://satotrades.com/guides/vwap-trading-strategy — page fetched 2026-10-07 (saved); key content via search excerpt: trend-day VWAP pullbacks as continuation entries ("highest-hit-rate setup"), rotational-day ±2σ fades with delta divergence or absorption, CVD divergence at VWAP bands as "one of the highest-hit-rate mean-reversion signals in intraday futures." *Taken:* the same-level-opposite-trade ambiguity in Sec. 2.4 and twist rationale #1 — flagged as excerpt-sourced.
8. **"VWAP Mean Reversion Backtest,"** CuteMarkets. https://cutemarkets.com/blog/vwap-mean-reversion-backtest-edge-and-failure-modes — direct fetch **failed** (HTTP 500, 2026-10-07); via search excerpt: constrained z-score model, quality vs. opportunity variants, quality variant profitable (+16,004 PnL, DSR 0.64) but failed a trades-per-week portfolio admission bar. *Taken:* the density/selectivity tradeoff in Sec. 3 and Sec. 6 — flagged as excerpt-sourced.
9. **"Bayesian Trading Cost Analysis and Ranking of Broker Algorithms,"** arXiv:1904.01566. https://ar5iv.labs.arxiv.org/html/1904.01566 — page fetched 2026-10-07 (saved); VWAP-benchmark discussion via search excerpt: VWAP as fair price, gaming by front-loading, predictability making VWAP orders "easy prey for front-running." *Taken:* benchmark-flow mechanics in Sec. 1/3 — flagged as excerpt-sourced.
10. **TradingView CVD indicators** (datanalyste "CVD Divergence Scalper," bangtrades "BT CVD Divergence") and **United Daytraders CVD guide** — not fetched directly; search excerpts provided the confirmed-pivot anti-repainting discipline and "divergence as filter, not trigger" framing used in Sec. 5/7. Flagged as excerpt-sourced.

## 9. Further reading

- Brian Shannon, *Maximum Trading Gains With Anchored VWAP* (2023) — the definitive AVWAP text; buy for the desk.
- Brian Shannon, *Technical Analysis Using Multiple Timeframes* (2008) — stage analysis + trend alignment behind his anchor choices.
- Berkowitz, Logue & Noser (1988), full paper — execution-benchmark foundations.
- Easley, López de Prado & O'Hara, "Flow Toxicity and Liquidity in a High-frequency World" (2012) — BVC and VPIN foundations (also primary lineage for doc 03).
- Bouchaud, Mézard & Potters, *Trades, Quotes and Prices* — microstructure context for why fair-value rotation exists.
- CMT Association "Fill The Gap" interview with Brian Shannon (Alphatrends podcast archive) — seen via search excerpt; listen for anchor-selection nuance.
- Kearns/Nevmyvaka execution-benchmark lecture notes (cis.upenn.edu impshort.pdf, fetched this session) — arrival price vs. VWAP vs. close benchmarks; useful when we extend to execution-aware variants.
