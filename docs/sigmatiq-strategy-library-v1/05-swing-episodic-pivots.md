# 05. Episodic Pivots / Momentum Bursts — Twist: EP-CAT

> **Library:** Sigmatiq Strategy Library | **Bucket:** Swing (1–10 days) | **Style:** Catalyst-driven momentum (post-event continuation)
> **Instruments:** US common stocks (long-only), optionally liquid ADRs | **Typical holding period:** 2–10 trading days (runners may extend) | **Complexity (1–5):** 4 | **Evidence grade (A–C):** C+ (strong academic PEAD foundation; practitioner rules are unaudited; no systematic public backtest of the full setup)
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise. This library contains no local backtests yet.

---

## 1. Origin & lineage

**Pradeep Bonde (Stockbee).** The Episodic Pivot (EP) concept was developed and named by Pradeep Bonde on his Stockbee blog (stockbee.blogspot.com), active since the mid-2000s. The canonical primary post, "What are Episodic Pivots and how to find them" (Feb 12, 2010), was read in full for this document, including its comment thread (which contains Bonde's own entry/stop/exit answers). Bonde's definition: a stock makes "a significant gap in price for a catalyst-worthy event. The market completely re-evaluates its view of the stock." He explicitly grounds the setup in the academic anomaly **PEAD (post-earnings-announcement drift)**, crediting Ball & Brown (1968) as the first documentation and noting "every year at least 50 new papers are published on PEAD and its persistence."

Bonde tracks ~20 episodic catalyst types daily (his list, verbatim categories): Earnings Growth 100%+, Earnings 40%+, Earnings Beats by wide margin, Earnings Other, Sales 100%+ but no earnings, IPO Breakout, Retail, Top Sector, New order or contract / rumor, Buyout / rumor / mergers / tie-ups / division sale, New product launch / news, Regulatory Changes, Drug Approval, Drug / marketing Tie-Up, Natural disaster / war / disease, Shortages, Rate Increase, Media Mention, Analyst upgrade/downgrade, Declares Dividend, Financial Engineering, Junk-of-the-bottom rally.

**Kristjan Kullamägi (Qullamaggie).** Swedish independent swing trader (US equities since 2011) who learned the EP from Bonde and popularized it via his blog (qullamaggie.com), streams, and *Chat With Traders* episode 212 ("Breakouts, Home Runs & Exponential Returns", Feb 26, 2021). His posts "3 TIMELESS setups that have made me TENS OF MILLIONS!" (Jan 8, 2021) and "How to master a setup: Episodic Pivots" (Nov 2, 2021) were read in full. He states the EP is one of his three core setups (with daily-chart breakouts and parabolic shorts) and claims it "has rewarded me several tens of millions in profits over the past couple of years alone" — a practitioner claim, unaudited, treated here as motivation rather than evidence. He also claims to have built an Evernote database of thousands of historical setup instances over 7–8 years ("1000+ hours"), which is his evidence-gathering method: manual deep-dives, not backtests.

**Momentum-burst framing.** Both practitioners describe stocks moving in "stair steps" / "momentum bursts" (Bonde's term, adopted by Kullamägi on CWT 212: "that's how stocks move, they move in momentum bursts ... and I verified it myself"): a 20–50%+ impulse, an orderly tightening consolidation "surfing" the rising 10/20-day moving averages, then range expansion into the next leg. The EP is the catalyst-ignited first step; the bull-flag breakout is the continuation entry. This document's twist merges the two: catalyst-classified EP as the *signal*, flag breakout as the *entry*.

**Academic anchor.** PEAD: stocks with the largest positive earnings surprises drift upward for weeks-to-months post-announcement (Ball & Brown 1968, cited in Bonde's post; Bernard & Thomas 1989 — not directly accessed, known via secondary citation). Bonde's scan is essentially a retail-implementable PEAD + volume-confirmation screen. Note the horizon mismatch: PEAD drift is measured over 60+ days academically; both practitioners harvest the first days-to-weeks, which is where our swing bucket sits.

## 2. The original rules (as published)

### 2.1 Bonde's EP scan and criteria (Stockbee, 2010, verbatim logic)

Telechart scan published in the post:

```text
((C - C1) >= 5 AND V > 10000 AND C >= 62.50 AND V > V1)
OR
((100*(C - C1)/C1) >= 8 AND V > 3000 AND (100*V/AVGV100) >= 300 AND C > 1)
```

i.e., either a ≥ $5 one-day price jump on volume above 100k (Telechart volume units) and above yesterday's volume, or a ≥ 8% day on volume ≥ 300% of the 100-day average. Then a *discretionary* filter:

- Context of the earnings — is this a first major acceleration?
- What caused the acceleration — one-time or likely to persist?
- Does the earnings trend represent a structural change in the industry or the company's position?
- Is the surprise already reflected in the current price level?

Bonde's stated preferences and observations (from the post):

- Earnings acceleration ≥ 100% YoY for no-analyst-coverage names (EPS at least $0.05); sales growth ≥ 5% (secondary coverage of his method cites sales growth 39%+ in consecutive quarters for the highest-conviction variant).
- The stock has *not* rallied into earnings — neglect: no news flow for months, no/low analyst coverage, low mutual-fund ownership. "Even better is stock which has no analyst coverage and is neglected."
- Volume on the EP day for the biggest winners is "typically 10 times or more compared to average volume ... in many cases the volume on earnings day might be the highest volume in the history of the stock or multi year high volume."
- Low float amplifies: float < 25M ideal, < 10M best for explosive moves; 100M+ float tends to pull back; 500M+ float only interesting near historic lows or single-digit prices.
- Covered (analyst-followed) companies' EPs "do not do as well as the first kind" — genuine surprises are rare, expectations are managed, and secondaries are often timed into strength, so "you find the EP on such stocks tend to have a pullback."

**Entry/exit (Bonde, from the post's comment thread — primary source):** "Because we track earnings daily most of the time we enter these kind of trades in pre market or at open. In such cases the stop is the low of last 2 days before entry. The exits are in 4 parts with profit target of 20% plus." He stresses the scan is not mechanical: "I buy less than 1% stocks from that scan. There are additional criteria like eps growth, sales growth, extent of neglect, nature of catalyst which are used to narrow the scan candidates further."

### 2.2 Kullamägi's EP rules (qullamaggie.com, 2021)

- **Definition:** "a gap up of 10% or more" (he notes this may differ from Bonde's). Massive volume near the open is mandatory — "ideally the stock should trade the average daily volume the first 15-20 minutes or even quicker"; best if huge volume is already present in after-hours/pre-market.
- **Catalyst types he lists:** political and regulatory (e.g., banks and prison stocks when Trump won), FDA and biotech, contracts and partnerships, earnings and earnings guidance, sector EP (a red-hot sector moving stocks in gaps without stock-specific news). "I have personally found most success in earnings EP as they are easy to find and easy to understand. Biotech EPs are the most difficult and I studied biomedicine for 3 years."
- **Earnings EP quality bar:** ideally triple-digit YoY EPS *and* sales growth (mid/high double-digit works; sales-only growth "worked really well" in the recent cycle "just as they did in the late 1990s"); ideally a big analyst beat and a big guidance raise; smaller stocks may have no analyst coverage — "you just have to trust the numbers and volume." "Volume is the #1 thing to focus on."
- **Prior price action:** "The best EPs are on stocks ones that have gone sideways for 3-6 months or more. Many times you get EP on stocks that have already made a big move from a previous EP and these can work but the failure rate is higher and the move probably won't be as big."
- **Entry:** opening-range highs (ORH) of the first 1-, 5-, or 60-minute candle; may add on 5-minute highs after a 1-minute ORH entry; "Often I miss the 1-minute opening range and I will buy the 5-minute highs or 60-minute highs. No need to be first in."
- **Stop:** "Stop is always at the lows of the day ... Make sure your stop is no more than 1x, or maximum 1.5x the average daily range or the average true range."
- **Management (from 3 TIMELESS setups):** trail with the 10- or 20-day MA once they rise above the initial stop; sell some into strength after the first momentum burst (3–5 days); risk 0.25–1% per trade ("I rarely risk more than 1% of my account on any trade"); position 10–20% of account, never more than 30% overnight; targets 5–20×+ initial risk on good selections; "You can be wildly profitable with having just a 25-30% winrate, it's all about having small losses and big winners."
- **Learning curve:** "It will take you 3-4 earnings seasons to get good at trading EP, 5-6 if you are a moron. For me it probably took 7 or 8 earnings seasons."

### 2.3 Kullamägi's breakout (momentum-burst continuation) rules

From "3 TIMELESS setups" — the three steps:

1. A big move higher sometime in the past 1–3 months, anywhere from 30–100%+, usually lasting a few days to a few weeks.
2. An orderly pullback and consolidation with higher lows and tightening range; consolidation usually 2 weeks to 2 months; price "surfs" the rising 10- and 20-day (sometimes 50-day) moving averages.
3. A range expansion (breakout) out of that consolidation.

Trading it: watchlist ready before the open with alerts and share counts pre-computed; enter on ORH (1/5/60-minute) or daily-chart breakout ("I don't anticipate breakouts"); stop at low of the day, never wider than ATR/ADR ("if the ADR of the stock is 5%, your stop shouldn't be wider than 5%"); sell 1/3–1/2 after 3–5 days and move stop to breakeven; trail the rest with the 10-day (beginners) or 20-day MA, exiting on the first *close* below it. Market context: "The best time to trade breakouts is after a market pullback or correction," in an uptrending or sideways market; "You don't get breakouts in a downtrending market (and even if you do see the odd setup, the breakout will almost certainly fail)." Universe scan: top 1–2% of stocks by 1-, 3-, and 6-month gains; wants both relative strength vs the market and big absolute momentum ("a stock that doubled over the past three months").

### 2.4 Disagreements across sources (explicit)

- **Gap threshold:** Bonde's scan triggers at 8% (or $5); Kullamägi defines an EP as ≥ 10%. Our twist uses 4% with a volume/range-expansion cross-requirement (§4b) — deliberately looser on gap, stricter on participation, because we trade the *flag*, not the gap day.
- **Entry timing:** both originators enter on the pivot day itself (pre-market/open/ORH). Bonde's own commenter (ppmoore, on the 2010 post) reported a mechanical Amibroker test of the raw scan at ~6% CAR, but ~50% CAR when modified to buy the *subsequent flag* (Bulkowski "earnings flag" pattern, 2000–2010) — anecdotal, unverified, but the direct motivation for our flag-entry twist. TraderLion's "delayed reaction" write-up of Bonde's method documents the four-stage pattern (big gap up → 1–2 day rally → stagnation/pullback → delayed second move after days/weeks/months) and advises waiting for the base rather than chasing.
- **Stops:** Bonde uses the low of the last 2 days; Kullamägi uses low of entry day capped at 1–1.5× ADR/ATR. We adopt the flag low (structurally tighter, later entry).
- **Sales vs earnings primacy:** Bonde (per secondary coverage) now weights sales growth over EPS ("earnings, in today's market conditions, don't matter. What matters ... is sales growth"); Kullamägi wants both, ideally triple-digit. Unresolved practitioner disagreement — our catalyst classifier keeps the cohorts separate so the data can answer it.
- **Exit scaling:** Bonde exits in 4 parts at 20%+ targets (position-trading horizon); Kullamägi trims 1/3–1/2 at 3–5 days then trails (swing horizon). We follow Kullamägi — the bucket is 1–10 days.

## 3. Why it works — mechanism & evidence

**Mechanism.**

1. **PEAD / underreaction:** genuine surprises are not fully priced on day one. Bonde: "If a company announces a big earnings surprise and if it is not currently priced in to the stock it will go up ... it leads to a rally lasting 2 to 3 months." We harvest only the first momentum burst(s) of that drift.
2. **Institutional accumulation takes time:** Kullamägi: "when institutions buy, they don't buy in one day. It can take many months for them to get to their desired allocation." Day-one volume is the footprint; the flag is the pause; the breakout is the resumption.
3. **Neglect + float amplify:** no analyst coverage and low float mean slow information diffusion and thin supply — the revaluation overshoots. Bonde: many current market leaders "were neglected small companies which market noticed when they announced big earnings acceleration."
4. **Attention / herding:** the gap day creates a "stock in play" that short-term momentum flows pile into for days (Bonde's "Stocks in Play" variant).

**Evidence (honestly graded).**

- *Academic (A-grade for the base anomaly):* PEAD is among the most replicated anomalies in finance (Ball & Brown 1968 via Bonde's post; Bernard & Thomas 1989 via secondary citation). It establishes that earnings-surprise drift exists; it does **not** validate the specific gap/volume/flag trading rules.
- *Practitioner (C-grade, unaudited):* Kullamägi's tens-of-millions claim and 25–30%-win-rate economics; Bonde's two decades of practice. No audited track records exist in public.
- *Independent mechanical tests (C-grade):* the commenter on Bonde's 2010 post reports ~6% CAR for the raw scan vs ~50% CAR for scan+flag (2000–2010, Amibroker) — unverified, sparse on detail, but directionally consistent with the delayed-reaction doctrine. This is the only quasi-quantitative public evidence on the *flag entry vs pivot-day entry* question we found; treat as a hypothesis to test, not a result.
- *Contradictory / cautionary:* Kullamägi himself notes high failure rates ("None of them work all the time, the failure rate is high, but they all provide excellent risk rewards") and that second EPs on already-moved stocks fail more; Bonde notes big-float and heavily-covered names tend to pull back post-EP; breakouts broadly fail in downtrending markets (Kullamägi quote in §2.3). Bonde also warns the raw scan is not a system ("I buy less than 1% stocks from that scan").

**The four-stage post-EP pattern (TraderLion's summary of Bonde) mapped to our rules:**

| Stage | Description (per source) | EP-CAT action |
| --- | --- | --- |
| 1. Big gap up | Immediate post-catalyst surge | Detect + tag only; never enter |
| 2. Short-term rally | May continue 1–2 days | Watch; flag may be forming |
| 3. Stagnation / pullback | Stock stops moving up or drops | Validate flag geometry (§4c) |
| 4. Delayed reaction | Second strong move after days/weeks | Our entry zone: buy-stop above flag high |

## 4. The twist: EP-CAT (Catalyst-Classified Episodic Pivot with flag entry)

Four modifications, each tied to a documented weakness.

### (a) Catalyst classification with an evidence gate

The original treats "a catalyst-worthy event" as discretionary judgment. We make it a typed field assigned at scan time (exactly one class per EP):

| Class | Definition (mechanical) | Default disposition |
| --- | --- | --- |
| `EARN_SURPRISE` | EPS or revenue beat vs consensus + YoY acceleration, earnings within ±1 session | KEEP (PEAD-backed; both practitioners' core) |
| `GUIDANCE_RAISE` | Forward guidance raised, with or without EPS beat | KEEP |
| `SECTOR_SYMPATHY` | No stock-specific news; sector index up ≥ 2% on the day | KEEP only if sector index > its 20-day MA |
| `SHORT_SQUEEZE` | Short interest > 15% of float AND no fundamental news, or squeeze-dominant tape | EXCLUDE until event study proves follow-through |
| `OTHER_NEWS` | M&A, contracts, FDA, regulatory, macro/political, media mention | EXCLUDE by default (Bonde: story stocks "can make bigger moves" but are unverifiable; Kullamägi found biotech/FDA hardest) |

Rule: trade only classes with demonstrated follow-through in our own event study (§7, Phase 0). The classification is re-scored quarterly on rolling data — this feedback loop is the "CAT" in EP-CAT. A class whose trailing 20-trade expectancy ≤ 0 is auto-demoted at the next re-score.

### (b) Hard participation and quality filters

- RVOL ≥ 3× (full-day volume / 100-day average volume ≥ 3 — Bonde's scan floor; the biggest winners show 10×+).
- Price > $5 (both practitioners).
- Gap > 4% (open vs prior close) **OR** range-expansion equivalent: day range ≥ 2 × ATR(20) AND close-location-value CLV = ((C − L) − (H − C)) / (H − L) ≥ 0.5 (close in top quartile) AND one-day return ≥ +3%. The range-expansion clause catches non-gap EPs (news released intraday) that a pure gap filter misses; it operationalizes Bonde's "out-sized price move on high volume."
- Base/neglect gate: prior 60-session return < +30% (Kullamägi's "sideways 3–6 months" made mechanical). Relax to < +60% only if RVOL ≥ 10, and demote size one step.

### (c) Enter the first bull-flag / inside-day consolidation AFTER the pivot day — never the pivot day itself

*Weakness addressed:* pivot-day entries pay the widest spreads, the worst slippage, and the highest first-hour failure rate; the only public mechanical comparison (§2.4) favors the flag entry by a wide margin; TraderLion's delayed-reaction note describes the same structure.

Flag definition (all must hold), monitored on sessions 1–5 after the EP day:

1. Each flag day's high ≤ EP-day high; each flag day's low ≥ EP-day low (inside the pivot range).
2. Contraction: average daily range of flag days < 60% of EP-day range.
3. Hold: every flag-day close ≥ EP-day midpoint = (EP high + EP low) / 2.
4. Volume dry-up: average flag-day volume < 50% of EP-day volume.
5. An inside day (H ≤ prior H and L ≥ prior L) counts as a valid 1-day flag.

Entry: buy-stop at flag high + $0.01 (or +0.1% for stocks > $100), resting for 2 sessions after flag completion; cancel if price breaks the EP-day midpoint first, or if session 7 post-EP arrives unfilled.

### (d) Risk 0.5–1% with stop below the flag low; trail with 10/20 EMA

- Stop = flag low − 0.25 × ATR(14) buffer. If stop distance > 1.5 × ATR(14), skip the trade (Kullamägi's ADR cap, applied to the flag).
- Size = risk budget / stop distance. Risk budget = 0.5% of equity base; 1.0% only for the conviction cell: `EARN_SURPRISE` or `GUIDANCE_RAISE` AND RVOL ≥ 5× AND 3–6-month sideways base (the highest-quality cell per both practitioners).
- Management: sell 1/3 at +1R or after 3 sessions (whichever first); move stop to breakeven on the remainder; first *close* below the 10-EMA exits half of the remainder; first close below the 20-EMA exits all (Kullamägi's 10/20-day logic, EMA instead of SMA for faster response inside the swing bucket).
- Hard time stop: 10 sessions for the full position (bucket constraint; longer runners belong to a position-trading variant, out of scope here).

## 5. Full specification of the twist variant

**Universe.** All US-listed common stocks (NYSE/Nasdaq/AMEX): price > $5, 100-day ADV ≥ $5M, float data available, ≥ 6 months listed history. Exclude leveraged/inverse ETFs and pre-deal SPACs. Include delisted names in backtests.

**Data.** Daily OHLCV + volume; point-in-time float/shares; earnings and guidance timestamps with consensus (must be point-in-time to avoid look-ahead); timestamped news feed (Benzinga/MT Newswires class) for catalyst classification; biweekly exchange short interest for `SHORT_SQUEEZE`; sector index prices for the sympathy gate. RVOL uses full-day volume (intraday RVOL is a refinement, not required).

**Signal chain (daily, after close).**

1. EP-day detection: 1-day return ≥ +3% AND (gap > 4% OR (range ≥ 2 × ATR(20) AND CLV ≥ 0.5)) AND RVOL ≥ 3 AND close > $5.
2. Catalyst tag from news/earnings data timestamped within [prior close, EP close + 1h].
3. Class gate per §4a (currently-approved classes only; sector gate for `SECTOR_SYMPATHY`).
4. Base gate per §4b (60-session return < +30%, or < +60% with RVOL ≥ 10 at reduced size).
5. Flag formation per §4c on sessions 1–5 post-EP.
6. Entry: buy-stop above flag high, valid sessions 2–7 post-EP.

**Exits.** Per §4d: initial stop flag low − 0.25 × ATR(14); +1R/3-session 1/3 trim; breakeven after trim; 10-EMA close exits half the remainder; 20-EMA close exits all; hard stop at 10 sessions. Overnight gap below stop → exit at open (modeled with slippage, §7).

**Sizing & risk limits.** Risk per trade 0.5% (1.0% conviction cell); position notional ≤ 10% of equity (conservative end of Kullamägi's 10–20% band) and ≤ 5% of 100-day ADV; max 8 concurrent EP positions; max 2 per GICS industry group; portfolio heat ≤ 4%; no new entries when S&P 500 < its 50-day MA (Kullamägi's "breakouts fail in downtrends" rule, made mechanical).

**Worked sizing example.** Equity $5M; flag high $42.10, flag low $39.60, ATR(14) $1.90. Stop = 39.60 − 0.475 ≈ $39.13; stop distance = 42.11 − 39.13 ≈ $2.98 (1.57 × ATR → borderline; if it exceeded 1.5 × ATR = $2.85 we would skip — here it fails the cap, so skip or re-size the entry trigger tighter). Clean case: entry $41.00, stop $39.13, distance $1.87; base risk 0.5% × $5M = $25,000 → 13,368 shares ≈ $548k notional (11% of equity → capped at 10% = $500k → 12,195 shares); ADV check: $500k ≤ 5% of 100-day ADV required.

**Catalyst tagging procedure (operational).** Tag assignment runs after close on the EP day, in this precedence order (first match wins):

1. `EARN_SURPRISE` — earnings release within [prior close, EP close + 1h] AND (EPS beat vs consensus ≥ 10% OR revenue beat ≥ 3% OR YoY EPS acceleration ≥ 40%). If no consensus exists (uncovered name — Bonde's preferred case), substitute reported YoY EPS growth ≥ 100% with EPS ≥ $0.05, or sales growth ≥ 39% (Bonde's high-conviction sales bar per secondary coverage).
2. `GUIDANCE_RAISE` — forward guidance raised within the window, with or without an EPS beat (Kullamägi: "a big guidance higher" is part of the ideal earnings EP).
3. `SECTOR_SYMPATHY` — no stock-specific news item found, and the stock's GICS industry-group index rose ≥ 2% on the day (Kullamägi's "sector EP ... stocks in that sector can move in gaps and make big moves without any specific news").
4. `SHORT_SQUEEZE` — latest exchange short interest > 15% of float AND no fundamental news item; or a news item but price/volume signature dominated by squeeze behavior (gap > 15% on RVOL ≥ 5 with no earnings in window).
5. `OTHER_NEWS` — everything else: M&A/buyout rumors, contracts, FDA/biotech, regulatory, macro/political, media mentions, dividends, financial engineering (Bonde's remaining catalyst types land here).

Ambiguous or missing news data → `OTHER_NEWS` (excluded by default — conservative direction). Every tag stores its evidence pointer (news ID / earnings release ID) for the quarterly re-score audit.

**Worked lifecycle (illustrative mechanics, not a result).** Patterned on Kullamägi's NVDA 2016 case (EPS +126% YoY, revenue +48%, 85c vs 67c consensus beat, 4-month sideways base — his numbers). Day 0: gap +11%, RVOL 6.2, close in top decile of range → EP detected, tagged `EARN_SURPRISE`, base gate passes (60-day return +4%). Days 1–3: inside ranges, flag range 38% of EP-day range, flag volume 31% of EP-day volume, all closes above EP midpoint → flag complete day 3. Day 4: buy-stop at flag high + $0.01 fills at 10:12 ET. Stop = flag low − 0.25×ATR(14); risk 1.0% (conviction cell: EARN_SURPRISE + RVOL ≥ 5 + base). Day 7: +1R reached → sell 1/3, stop to breakeven. Day 9: first close below 10-EMA → sell half of remainder. Day 12: first close below 20-EMA → flat (position-trading variant would hold; our bucket does not).

**Costs.** Commission $0.005/share; slippage: 10 bps/side on stop entries (buy-stops on momentum names slip), 15 bps on stop-loss exits, 5 bps on EMA exits; gap-through-stop modeled at open ± 20 bps.

**Capacity.** The binding constraint: EP names are small/mid caps on event days. At 5% ADV participation and 8 positions, realistic capacity is $5–25M. Beyond that, entry/exit slippage consumes the 5–20R tail that drives the economics.

**Scan pseudocode.**

```text
for each stock s in universe, after close of day t:
    if is_EP_day(s, t):                       # §5 step 1
        tag <- classify_catalyst(s, t)        # news/earnings within window
        if tag not in APPROVED_CLASSES: skip
        if tag == SECTOR_SYMPATHY and sector_index < MA20: skip
        if ret60(s, t-1) >= 30% and not (RVOL >= 10 and ret60 < 60%): skip
        watchlist.add(s, ep_high, ep_low, ep_mid, ep_range, ep_vol)
for each s on watchlist (days 1..5 post-EP):
    update flag state per §4c
    if flag_complete: place buy_stop(flag_high + tick), ttl = 2 sessions
    if close < ep_mid: cancel and drop
for each open EP position:
    apply §4d exit ladder; hard exit at session 10
```

## 6. Failure modes & regime dependence

1. **Bear / chop markets:** breakout failure rate spikes; Kullamägi is explicit that the setup needs an up or sideways tape. Our 50-day-MA index gate addresses this but will go dark for months (2022-style) — opportunity cost, not losses.
2. **Gap-fade regimes:** in distribution phases, high-RVOL gaps are sold into — the EP day *is* the top. Early warning: rising share of EPs closing in the bottom 25% of their day range; flag breakouts failing within 2 sessions at > 60% rate over a rolling 20-trade window.
3. **Catalyst misclassification:** news timestamp errors or ambiguous multi-catalyst days corrupt the class gate. Mitigation: manual review queue for the first 6 months of live tagging; ambiguous → `OTHER_NEWS` (excluded by default).
4. **Crowding:** post-2021, EP/ORH entries are widely known (Kullamägi's own audience is large). The flag entry is our structural answer; if flag breakouts degrade to pivot-day-entry economics, the edge is gone.
5. **Single-name event risk:** secondary offerings timed into strength (Bonde: established companies "often time secondaries and other capital raising events to time with such surprises and so often you find the EP on such stocks tend to have a pullback"), guidance walk-backs, trial failures. Stops are the only defense; overnight gaps through stops will exceed 1R periodically — size for it.
6. **Low-float manipulation:** sub-10M-float names can be orchestrated pumps. Bonde loves them; we cap participation and require RVOL to look organic (no single-print spikes) — a soft discretionary override in v1, to be mechanized in v2.
7. **Early-warning dashboard:** rolling 50-trade win rate < 25% (below Kullamägi's stated viable floor); avg winner < 2.5R; EP frequency collapse (< 5 qualifying EPs/month — regime starvation); approval-class drift (a kept class's trailing 20-trade expectancy ≤ 0 → auto-demote at next quarterly re-score).

## 7. Validation protocol

**Phase 0 — event study (before any strategy backtest).** Build the EP event set 2010–2026 (survivorship-free). For each catalyst class: distribution of forward returns at +1/+2/+5/+10/+20 days from the EP-day close and from the flag-breakout price; follow-through rate (max favorable excursion ≥ +5% within 10 sessions); failure rate (close below EP-day midpoint within 5 sessions). Approve/demote classes on this evidence — this *is* the EP-CAT gate — computed on 2010–2020 data only, reserving 2021–2026 for confirmation.

**Phase 1 — strategy backtest.** Chronological splits: train 2010–2018; validation 2019–2021 (includes the 2020–21 momentum bubble — expect inflated numbers; do not tune to them); test 2022–2026 (bear, recovery, 2026 tape). Walk-forward with annually frozen parameters.

**Cost/slippage model.** As §5, plus a stress pass at 2× slippage and a "pessimistic fill" pass where buy-stops fill at post-trigger VWAP rather than stop price.

**Strategy-specific pitfalls.**

- *Look-ahead:* earnings timestamps (AMC vs BMO), consensus databases restated after the fact, news-feed latency; float and short interest must be point-in-time. A 2015-era EP list built from today's universe still needs the *historical* universe to avoid selection bias.
- *Survivorship:* EP strategies pick future winners disproportionately; a survivor-only test will massively overstate the edge. Delisted names mandatory.
- *Flag-definition overfit:* the 60% / 50% / midpoint parameters are priors from practitioner descriptions, not optima; sweep ±50% around each and demand a plateau.
- *Small-sample class inference:* some catalyst classes will have < 100 events; use hierarchical shrinkage toward the all-EP mean before approving/demoting.
- *Fill realism:* buy-stops on halting/gapping names; assume no fills during halts; first-minute fills disallowed (our entry is daily-bar based by design).

**Robustness checks.** Gap threshold {3%, 4%, 6%, 8%}; RVOL {2, 3, 5}; flag length {1–3, 1–5, 2–7}; midpoint vs EP-day-low hold rule; EMA pair {8/21, 10/20, 10/50}; risk {0.5%, 0.75%, 1.0%}; entry {flag high, ORH of breakout day, close of breakout day}. Acceptance requires the spec cell to sit on a plateau, not a peak.

**Acceptance criteria (pre-registered).** On 2022–2026 test, net of stress costs: ≥ 100 trades; win rate ≥ 25%; avg win / avg loss ≥ 2.5R; expectancy ≥ +0.4R/trade; profit factor ≥ 1.4; max DD ≤ 12% at base risk; positive expectancy in each kept catalyst class individually. Plus the twist's core claim: the flag-entry variant must beat a pivot-day-entry variant (same filters, ORH entry, low-of-day stop) on expectancy by ≥ 0.15R — otherwise the twist fails and we revert to studying the original.

## 8. Sources read (annotated)

1. **Bonde, P., "What are Episodic Pivots and how to find them", Stockbee (Feb 12, 2010).** URL: https://stockbee.blogspot.com/2010/02/what-are-episodic-pivots-and-how-to.html — accessed 2026-10-07. Read in full including comment thread. Taken: the verbatim Telechart scan; PEAD grounding and Ball & Brown (1968) attribution; the first-acceleration / persistence / structural-change checklist; 10× volume observation on big winners; analyst-coverage dichotomy and secondary-timing pullback warning; float guidance (<25M ideal, <10M best, >500M avoid); the ~20-catalyst list; entry "pre market or at open", stop "low of last 2 days", exits "in 4 parts with profit target of 20% plus"; "I buy less than 1% stocks from that scan"; commenter ppmoore's mechanical test (raw scan ~6% CAR vs scan+flag ~50% CAR, Amibroker 2000–2010 — unverified, hypothesis-generating); Bonde's 8%-threshold rationale ("a stock which makes 8% plus kind of move on earnings tend to do well") and his monthly EP scan / 50%-surprise screen variants.
2. **Kullamägi, K., "How to master a setup: Episodic Pivots", qullamaggie.com (Nov 2, 2021).** URL: https://qullamaggie.com/how-to-master-a-setup-episodic-pivots/ — accessed 2026-10-07. Read in full. Taken: ≥10% gap definition; ADV-in-first-15–20-minutes volume rule; ORH (1/5/60-min) entry with adds; stop at low of day capped at 1–1.5× ADR/ATR; catalyst taxonomy (political/regulatory, FDA/biotech, contracts, earnings/guidance, sector EP); earnings-EP quality bar (triple-digit YoY EPS+sales ideal, big beat, big guidance); 3–6-month sideways-base preference and second-EP failure warning; "institutions don't buy in one day"; his tens-of-millions claim (attributed, unaudited); 3–8 earnings-seasons learning curve; AFRM double-EP stopped-out-twice case study (his own losses, useful honesty anchor).
3. **Kullamägi, K., "3 TIMELESS setups that have made me TENS OF MILLIONS!", qullamaggie.com (Jan 8, 2021).** URL: https://qullamaggie.com/my-3-timeless-setups-that-have-made-me-tens-of-millions/ — accessed 2026-10-07. Read in full. Taken: breakout setup steps (30–100%+ move in 1–3 months; orderly tightening consolidation 2wk–2mo surfing 10/20-day MAs; range expansion); ORH entry; stop ≤ ATR/ADR; sell 1/3–1/2 after 3–5 days then breakeven; trail with 10/20-day MA, exit on first close below; risk 0.25–1%, position 10–20%, max 30% overnight; 5–20×R targets; 25–30% win-rate viability; NVDA 2016/2017 EP case study (EPS +126%, revenue +48%, 85c vs 67c beat, 4-month base, 6-month near-double); FSLR 2007 and BBRY 2004 historical EPs; the EP-day counter-example (gap up that sold off = not an EP).
4. **Chat With Traders ep. 212, "Kristjan Kullamägi – Breakouts, Home Runs & Exponential Returns" (Feb 26, 2021).** Episode page: https://chatwithtraders.com/episode/212-kristjan-kullamagi-breakouts-home-runs-exponential-returns — accessed 2026-10-07. Read via the episode page plus two full secondary renderings: Trading Resource Hub interview notes part 1 (https://tradingresourcehub.substack.com/p/interview-qullamaggie-chat-with-traders-part1) and the Pickscribe transcript (https://pickscribe.com/v/K0F73Sq90j0/). Taken: momentum-burst/staircase model credited to Stockbee ("that's how stocks move ... and I verified it myself"); "buy just as the stock is about to break out into the next step"; best breakouts after market pullbacks/corrections; relative + absolute momentum requirement; ORH mechanics across 1/5/60-minute candles; 10/20-day trailing stops; selling into the first burst; day→swing transition rationale.
5. **TraderLion, "Pradeep Bonde: Episodic Pivots Delayed Reactions".** URL: https://traderlion.com/profile/pradeep-bonde/episodic-pivots-delayed-reaction/ — accessed 2026-10-07 (via search extract). Taken: the four-stage post-earnings pattern (big gap up → short-term rally 1–2 days → stagnation/pullback → delayed reaction after days/weeks/months) and the two-phase entry doctrine (trade the initial move OR wait for the base and confirmed second move) — direct support for the flag-entry twist.
6. **Retail Traders Repository, "Pradeep Bonde: The Art of Swing Trading Episodic Pivots".** URL: https://retailtradersrepository.substack.com/p/pradeep-bonde-episodic-pivots — accessed 2026-10-07 (via search extract). Taken: Bonde's MA/N framework elements (Massive Acceleration in profit growth — double/triple-digit or massive beats, e.g., 50c vs 10c expected; Neglect across price action, fund ownership, news flow), sales-over-earnings weighting, the 2.5% stop variant, re-entry behavior after stop-outs, "story stocks can make bigger moves than real-catalyst stocks" caveat. Secondary summary — used only where consistent with the primary post.
7. **Qullamaggie mirror, "Stockbee on trading Episodic Pivots" (qullamaggie.net).** URL: https://qullamaggie.net/stockbee-on-trading-episodic-pivots/ — accessed 2026-10-07 (via search extract). Taken: Bonde's screening detail (earnings up 100%+ QoQ and ≥ $0.05; sales up 5%+; 65-day price action check for neglect; "Most of these breakouts will have minor pullback at best and just go up for 2 to 6 weeks"; "you cannot anticipate a surprise").

## 9. Further reading

- Ball, R. & Brown, P. (1968), "An Empirical Evaluation of Accounting Income Numbers", *Journal of Accounting Research* — the PEAD origin (cited via Bonde's post; not directly accessed).
- Bernard, V. & Thomas, J. (1989), "Post-Earnings-Announcement Drift: Delayed Price Response or Risk Premium?", *Journal of Accounting & Economics* — known via secondary citation; not accessed.
- Bulkowski, T., *Encyclopedia of Chart Patterns* — "earnings flag" pattern statistics (referenced by the Stockbee commenter; not accessed).
- Stockbee member-site materials: Trend Intensity breakouts, Dollar Breakouts, 9-million-share EPs, "Sugar Babies", Night-Time-is-Right-Time (paywalled; not accessed).
- Kullamägi's streams/Discord archives (referenced throughout his blog; not systematically accessible).
- O'Neil, W., *How to Make Money in Stocks* — CAN SLIM lineage for earnings acceleration + breakout logic (not accessed this session).
- Minervini, M., *Trade Like a Stock Market Wizard* — VCP contraction logic adjacent to our flag definition (known via secondary citation; not accessed).
