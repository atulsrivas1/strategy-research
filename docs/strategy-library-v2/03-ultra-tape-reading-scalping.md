# 03. Tape-Reading / Order-Flow Scalping — Twist: TAPE-Q

> **Library:** Sigmatiq Strategy Library V2 | **Bucket:** Ultra-short / HFT & scalping | **Style:** Discretionary microstructure, systematized
> **Instruments:** ES/NQ futures, CL/GC, liquid large-cap equities | **Typical holding period:** Seconds to minutes, flat EOD | **Complexity (1–5):** 3 | **Evidence grade (A–C):** C+
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise.

## 1. Origin & lineage

**Tape-reading lineage.** Richard Wyckoff and Jesse Livermore read the ticker tape; the modern screen version is John Grady (No BS Day Trading / Jigsaw) — ex-floor trader turned order-flow educator — plus Jigsaw daytradr/Bookmap heatmap tools, and Axia/Trader Dante footprint education. SMB Capital's tape-reading desk lore (Lance Breitstein's documented audited-style runs aside) shows the discretionary apex: absorb-and-reverse prints at known levels. Our version systematizes the discretionary checklist into codeable gates.

## 2. The original rules (as published)

- **Grady/Jigsaw checklist (practitioner):** trade absorption (large resting passive vs. aggressive market orders that fail to move price), failed auction at prior high/low, delta flip with price holding, iceberg reloads.
- **Entry:** join the absorbing side after the aggressive side exhausts (second push fails), stop one tick beyond the extreme.
- **Exit:** first liquidity pocket (prior single-print / unfinished auction), or stop on fresh sweep.
- **What is NOT published as code:** exact size thresholds, absorption ratios, and heatmap parameters — all eyeballed in the education.

## 3. Why it works — mechanism & evidence

**Mechanism.** Informed/aggressive flow leaves footprints (delta, stacked imbalances, reloads). Absorption means a larger passive participant is warehousing the aggressive flow; when the aggressive side exhausts, price snaps toward the absorber's intent over seconds.

**Supporting evidence (all attributed, none ours):**

- Practitioner track records and funded-desk evaluations show tape-trained traders passing with absorption-style playbooks (firm marketing + trader-published blotters; unaudited — weight accordingly).
- Academic footprint: Easley–O'Hara VPIN/OFI literature finds order-flow toxicity predicts short-horizon moves (authors' claims on futures/equities samples).
- Tool-vendor case studies (Jigsaw/Bookmap) document absorption-reversal examples tick by tick (vendor-authored; illustrative, not statistical).

**Contradictory / decay evidence:**

- No peer-reviewed RCT shows discretionary tape reading beats algos net of costs; survivorship in education marketing is extreme.
- Iceberg/spoofing detection by eye has poor inter-rater reliability; what one trader calls absorption another calls distribution.
- HFT quoting engines lean on the same signals faster — manual speed is structurally second.

**Synthesis.** Tape reading is a real microstructure lens with weak public statistics; its value here is as a confirma­tion layer (absorption + level confluence) for short holds, not a standalone manual franchise.

## 4. The twist: TAPE-Q

1. **Absorption ratio rule (targets eyeball subjectivity):** define `ABS = aggressive_volume / adverse_price_progress_ticks` over 60s; require `ABS > 3x` 20-day median with price range < 0.25 ATR-micro.
2. **Level-confluence gate (targets random-scalp noise):** only trade absorption within 2 ticks of prior day high/low, overnight high/low, or unfinished-auction single prints.
3. **Delta-flip confirmation (targets early entries):** require cumulative delta to flip sign post-absorption before entry; no pre-flip front-running.
4. **Two-push exhaustion (targets first-push traps):** enter only after the second aggressive push fails to take the extreme (not the first touch).
5. **Volatility throttle (targets chop bleed):** max 3 attempts per level per session; stand down after two full stops.

## 5. Full specification of the twist variant

**Universe.** ES/MES and NQ/MNQ front month; optional AAPL/NVDA/MSFT equity tape sleeve. One level at a time.

**Data requirements.** Time-and-sales with aggressor flags, footprint/volume-delta per price (1-min or tick), prior-day/overnight levels, ATR-micro (20-period 1-min range).

**Signal definitions (formulas).**

- Absorption: `ABS_60s > 3*median_20d` AND `range_60s < 0.25*ATR_micro`.
- Confluence: `min distance to {PDH, PDL, ONH, ONL, single_print} <= 2 ticks`.
- Delta flip: `cumdelta_5m` crosses zero toward absorber side after absorption window.

**Entries.**

Limit-join absorber side post-flip, 1-tick confirmation; stop 2 ticks beyond extreme; max hold 5 minutes.

**Exits.**

Limit at next liquidity pocket (nearest single-print edge or 0.5x ATR-micro); time-stop 5 min; scratch if delta flips back within 60s.

**Position sizing.**

Fixed fractional: 0.25% equity risk per scalp; size = risk / (2-tick stop value); daily halt after -1% day.

**Risk limits.**

Per-level attempt cap (3); per-day stop count cap (4); news blackout 2 min around prints; no adds to losers.

**Cost model & capacity.**

Commissions + 1-tick slippage each side assumed; micros capacity fine at desk size; equity sleeve add $0.003/share all-in stress.

**Parameters to validate (plateau, not peak):** ABS multiple {2, 3, 4}; confluence {1, 2, 3 ticks}; delta window {3m, 5m, 10m}; hold {3m, 5m, 10m}.

## 6. Failure modes & regime dependence

Spoof-driven fake absorption; trend-day absorption that keeps reloading (absorber is distributing); low-volume lunchtime chop with no follow-through.

## 7. Validation protocol

**Status: no local backtest exists yet.** This library contains zero proprietary results; everything above is literature.

- **Data:** Tick/footprint replay 12+ months (Databento/similar), level catalog point-in-time, fee schedule.
- **Splits:** chronological only; train / validation / test by date, never random k-fold on time series. Walk-forward re-fit anchored annually.
- **Cost/slippage model:** fees + rebates at the venue fee schedule, queue-position-aware fill simulation, adverse-selection haircut on marketable fills; stress at 2x and 3x costs.
- **Pitfalls:** look-ahead in signal timestamps (exchange sequence numbers, not wall-clock); survivorship of symbols; same-event ambiguity (both quotes updating in one packet — assume worst fill); latency distribution, not a point estimate.
- **Robustness:** parameter-plateau heatmaps; bootstrap CIs on trade PnL; placebo (randomized signal with identical throttles must be ~zero net of costs); regime sub-samples by spread/volatility quintile and by year; Monte Carlo over queue-position draws.
- **Acceptance criteria:** OOS net Sharpe >= 0.8 after 2x costs; per-trade t >= 2; max intraday drawdown <= 2x in-sample; positive expectancy in >= 60% of months; edge survives removal of the single best month.

## 8. Sources read (annotated)

1. **John Grady, No BS Day Trading / Jigsaw education.** https://www.nobsdaytrading.com ; https://www.jigsawtrading.com — absorption/auction curriculum. *Taken:* checklist concepts. Not directly re-fetched — known via secondary citation; vendor-authored.
2. **Easley, López de Prado & O'Hara on VPIN/flow toxicity.** Search: https://papers.ssrn.com — toxicity predicts short-horizon stress. *Taken:* mechanism analogy only. Abstract-level knowledge; marked honestly.
3. **Wyckoff schematics (accumulation/distribution, springs).** https://www.wyckoffanalytics.com — absorption as modern spring. *Taken:* level-confluence mapping. Educational source.

## 9. Further reading

- Trader Dante footprint/scalping curriculum.
- Axia Futures order-flow desk interviews.
- Bookmap heatmap absorption case library.
