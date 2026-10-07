# 05. Opening-Drive Scalping — Twist: DRIVE-F

> **Library:** Sigmatiq Strategy Library V2 | **Bucket:** Ultra-short / HFT & scalping | **Style:** Intraday microstructure / momentum
> **Instruments:** Large-cap equities, QQQ/SPY, MNQ/MES | **Typical holding period:** 1–15 minutes, morning only | **Complexity (1–5):** 2 | **Evidence grade (A–C):** C+
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise.

## 1. Origin & lineage

**Prop-desk opening-drive lineage.** SMB Capital (Mike Bellafiore/Sharma) tape-reading lore — 'the opening drive' as the first directional commitment off the open — plus Lance Breitstein-style intraday momentum scalping narratives and Andrew Aziz opening-momentum chapters. Academic cousin: Gao–Han intraday momentum (first-half-hour predicts last-half-hour) and Heston–Korajczyk–Sadka intraday seasonality. Our spec turns desk lore ('trade the drive, not the chop') into gates.

## 2. The original rules (as published)

- **Desk lore:** if the stock drives out of the opening range with pace and holds, join the first micro-pullback; if it chops inside the first-minute range, stand down.
- **Aziz variant:** 5-min opening-range momentum with volume confirmation; stop at first-candle extreme.
- **SMB variant:** tape confirms (offers lifting, no reload on the offer) before the add; scratch fast on stall.
- **What is NOT published:** pace thresholds, pullback definitions, scratch rules — all feel-based.

## 3. Why it works — mechanism & evidence

**Mechanism.** Overnight inventory plus opening auction imbalance resolves directionally in the first minutes; pace (volume per unit time + range expansion) separates committed drives from two-sided chop. Joining the first pullback harvests the continuation before late-morning mean reversion sets in.

**Supporting evidence (all attributed, none ours):**

- Gao–Han–Zhou intraday momentum (authors report first-30-min return predicts last-30-min US equity returns; widely cited, debated magnitude).
- Heston–Korajczyk–Sadka document intraday return seasonality persisting at half-hour lags (authors' claim).
- Prop-desk published blotters show opening-drive concentration of intraday PnL (firm/trader-published; unaudited).

**Contradictory / decay evidence:**

- Intraday momentum effects are small and cost-sensitive; retail slippage on marketable drive entries erases the paper edge in several replications.
- Opening-drive frequency is low (1–3 clean drives per name per month); overtrading marginal opens is the documented failure mode.
- 2022-style gap-and-go regimes inflate drive statistics; low-vol grinds starve them.

**Synthesis.** The drive is real but rare: edge comes from selectivity (pace + range + tape agreement) and fast scratches, not from trading every open.

## 4. The twist: DRIVE-F

1. **Pace gate (targets chop entries):** require 5-min volume >= 2x 20-day same-window median AND 5-min range >= 1.5x median first-5-min range.
2. **Drive-vs-exhaustion filter (targets late entries):** skip if price already extended > 1.0 ATR-micro from VWAP; only first pullback within 0.5 ATR-micro qualifies.
3. **Tape confirmation (targets blind momentum):** require offer-lift dominance (ask-side volume share > 60%) into the pullback low for longs.
4. **Two-bar scratch (targets hope-holds):** scratch at cost if no new extreme within 2 bars (10 min on 5-min chart); no time-average losers.
5. **Morning-only throttle (targets afternoon giveback):** entries 09:35–10:30 ET only; flat by 11:00 ET regardless.

## 5. Full specification of the twist variant

**Universe.** Top-100 dollar-volume equities + QQQ/SPY/MNQ/MES. One drive per name per day.

**Data requirements.** 1-min bars + time-of-day volume history (20d), VWAP, ATR-micro, tape/delta where available.

**Signal definitions (formulas).**

- Pace: `RVOL5 >= 2.0` AND `range5 >= 1.5*median_range5_20d`.
- Extension: `|price - VWAP| <= 1.0*ATR_micro` at pullback; pullback depth <= 0.5*ATR_micro from drive extreme.
- Tape: `ask_share_5m > 0.60` (longs; mirror for shorts).

**Entries.**

Limit-join first micro-pullback after pace-confirmed drive; stop 1 tick beyond pullback extreme; one entry per name per day.

**Exits.**

Target 1.5x pullback-risk or VWAP-band edge; scratch after 2 bars without new extreme; hard flat 11:00 ET.

**Position sizing.**

0.5% risk per drive; width factor inverse to pullback depth; skip if size < 1 lot at 0.25x.

**Risk limits.**

Daily halt after 2 full stops; news-day skip (earnings/FOMC open); no adds to stalled drives.

**Cost model & capacity.**

1-tick slippage + commission each side; capacity fine at retail/prop size; edge is frequency-capped (selectivity is the point).

**Parameters to validate (plateau, not peak):** RVOL {1.5, 2.0, 2.5}; range mult {1.25, 1.5, 2.0}; hold {5m, 10m, 15m}; target {1.0R, 1.5R, 2.0R}.

## 6. Failure modes & regime dependence

Exhaustion drives (buy-the-close of the move); low-volume fake pace on half-days; tape spoofing into the pullback; gap-fill reversals that look like drives for 3 minutes.

## 7. Validation protocol

**Status: no local backtest exists yet.** This library contains zero proprietary results; everything above is literature.

- **Data:** 1-min bars 2016–present + time-of-day volume normals; tape replay where available; event calendar.
- **Splits:** chronological only; train / validation / test by date, never random k-fold on time series. Walk-forward re-fit anchored annually.
- **Cost/slippage model:** fees + rebates at the venue fee schedule, queue-position-aware fill simulation, adverse-selection haircut on marketable fills; stress at 2x and 3x costs.
- **Pitfalls:** look-ahead in signal timestamps (exchange sequence numbers, not wall-clock); survivorship of symbols; same-event ambiguity (both quotes updating in one packet — assume worst fill); latency distribution, not a point estimate.
- **Robustness:** parameter-plateau heatmaps; bootstrap CIs on trade PnL; placebo (randomized signal with identical throttles must be ~zero net of costs); regime sub-samples by spread/volatility quintile and by year; Monte Carlo over queue-position draws.
- **Acceptance criteria:** OOS net Sharpe >= 0.8 after 2x costs; per-trade t >= 2; max intraday drawdown <= 2x in-sample; positive expectancy in >= 60% of months; edge survives removal of the single best month.

## 8. Sources read (annotated)

1. **Gao, Han & Zhou on intraday momentum.** Search SSRN for "Intraday Momentum" — first-half-hour predicts last-half-hour (authors' claim). *Taken:* pace-continuation mechanism. Known via secondary citation.
2. **Heston, Korajczyk & Sadka on intraday seasonality.** https://papers.ssrn.com (search "Intraday Seasonality") — half-hour return persistence. *Taken:* morning-drive timing. Known via secondary citation.
3. **SMB Capital / Bellafiore desk literature.** https://www.smbcap.com — opening-drive tape concepts. *Taken:* pullback/scratch heuristics. Firm-authored; illustrative.
4. **Andrew Aziz, *How to Day Trade for a Living* (2015).** Publisher: https://www.bearbulltraders.com — opening momentum chapters. *Taken:* retail momentum baseline. Book-level knowledge.

## 9. Further reading

- Lance Breitstein interview/blotter breakdowns (video).
- Heston intraday-volume seasonality follow-ups.
- Prop-firm opening-drive video libraries (for pattern catalog, not statistics).
