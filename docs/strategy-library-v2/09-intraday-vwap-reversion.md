# 09. VWAP Mean Reversion — Twist: AVWAP-Q2

> **Library:** Sigmatiq Strategy Library V2 | **Bucket:** Intraday | **Style:** Mean reversion
> **Instruments:** Large-cap equities, QQQ/SPY, ES/MES | **Typical holding period:** 15 min – 2 h, flat by close | **Complexity (1–5):** 3 | **Evidence grade (A–C):** B-
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise.

## 1. Origin & lineage

**Institutional VWAP lineage.** VWAP (Berkowitz–Logan–VanderLinden implementation-shortfall literature; institutional best-execution) is the day's volume-weighted fair price; deviations invite institutional rebalancing flow. Practitioner mean-reversion: Bella/Spencer SMB VWAP-fade tape, Aziz VWAP-breakdown shorts, statistical literature on intraday reversal (Heston intraday seasonality; Grant–Wolf–Yu on VWAP reversion). Anchored VWAP (Brian Shannon) extends the anchor to events — our twist's core.

## 2. The original rules (as published)

- **Classic VWAP fade:** short 2+ sigma above VWAP (sigma = rolling volume-weighted stdev) with RVOL confirmation; cover at VWAP; stop beyond the extreme.
- **Institutional version:** VWAP is execution benchmark, not a signal — deviations are traded only as implementation-shortfall reduction (patient, passive).
- **Shannon AVWAP:** anchor VWAP to gap/event bars; fade the stretch from the anchored line, not the day-session line.
- **Disagreement:** band width (1.5 vs 2 vs 3 sigma), sigma lookback, whether to trade with-trend VWAP breaks (momentum) or only fades.

## 3. Why it works — mechanism & evidence

**Mechanism.** Liquidity provision around the institutional benchmark: deviations reflect transient imbalance (opening auction, ETF flows); benchmark-chasing algos and VWAP-targeted parent orders lean the tape back toward VWAP; bands mark statistically stretched liquidity demand.

**Supporting evidence (all attributed, none ours):**

- Intraday reversal around VWAP is a staple of prop-desk playbooks (firm-published examples; unaudited but ubiquitous).
- Execution literature finds VWAP-tracking flow is a large share of institutional volume (author estimates vary 30–50% of US equity volume VWAP-linked; treat as indicative).
- AVWAP event-anchoring is widely reported to hold better than session VWAP on gap/event days (practitioner consensus).

**Contradictory / decay evidence:**

- Trend days ride VWAP bands for hours — naive fades bleed all day (the documented failure; VWAP-reversion Sharpe collapses in |VWAPz|>2 regimes).
- Band sigma is backward-looking; opening-drive volatility understates true stretch and overtrades the first 30 minutes.
- Transaction-cost analyses show aggressive VWAP-fade entries pay the spread at the worst moment (Figure: fade entries cluster at peak adverse selection).

**Synthesis.** VWAP fade is a balanced-regime liquidity trade, not an all-day rule: it needs a trend/balance classifier plus event-anchoring, otherwise trend days destroy months of fade income.

## 4. The twist: AVWAP-Q2

1. **AVWAP-first (targets session-VWAP failure on gap days):** anchor to the gap/event bar; session VWAP is secondary confirmation only.
2. **Balanced-regime gate (targets trend-day bleed):** trade fades only when |VWAP z| < 1.5 and opening-range width < 0.5 ATRd; otherwise stand down (no momentum flip — different strategy).
3. **Order-flow divergence (targets blind fades):** require delta/volume to diverge (price makes new extreme, delta does not) before fading.
4. **Sigma-adaptive bands (targets static-band overtrading):** band = VWAP ± k * realized-micro-sigma * sqrt(elapsed fraction); k=2.0 default, widened 1.5x in first 30 min.
5. **Scale-and-scratch exits (targets hope-holds):** 50% at VWAP, runner to opposite micro-band; scratch if not halfway home in 30 min.

## 5. Full specification of the twist variant

**Universe.** Top-200 US equities + QQQ/SPY/ES; exclude earnings-day names from fade sleeve (momentum sleeve only).

**Data requirements.** 1-min bars with volume, VWAP + AVWAP engine, rolling volume-weighted sigma, delta/footprint where available, ATRd, event calendar.

**Signal definitions (formulas).**

- VWAPz = (price - AVWAP)/band_sigma; fade trigger |VWAPz| >= 2.0 in balanced regime (|VWAPz_daily| < 1.5 pre-trigger, ORW < 0.5 ATRd).
- Divergence: price extreme beyond prior 30-min extreme while 5-min cum-delta fails to exceed its prior extreme.
- Morning band multiplier 1.5x before 10:00 ET.

**Entries.**

Passive limit at band touch post-divergence; stop beyond trigger extreme + 0.1 ATRm; one fade per direction per name per day.

**Exits.**

50% at AVWAP, runner to opposite 1.0-sigma band; scratch at -30 min without halfway progress; hard flat 15:55 ET.

**Position sizing.**

0.4% risk per fade; vol-scaled by band width/ATRm (wide bands = smaller).

**Risk limits.**

Balanced-regime gate is hard (no override); trend-day blanket ban; daily halt after 2 fade stops.

**Cost model & capacity.**

Passive entries earn/cross minimally; assume 1-tick + commission; haircut limit fills 70%; capacity intraday-fine.

**Parameters to validate (plateau, not peak):** k {1.5, 2.0, 2.5}; regime z {1.0, 1.5, 2.0}; divergence window {15m, 30m}; scratch {20m, 30m, 45m}.

## 6. Failure modes & regime dependence

Trend-day persistence (bands ridden); event-day AVWAP anchor misplacement; delta-feed latency that confirms divergence late.

## 7. Validation protocol

**Status: no local backtest exists yet.** This library contains zero proprietary results; everything above is literature.

- **Data:** 1-min+volume 2016–present; AVWAP history reproducible from bar data; event calendar point-in-time.
- **Splits:** chronological train / validation / test; no random k-fold. Walk-forward re-fit anchored annually.
- **Cost/slippage model:** commission + 1–2 ticks slippage per side (futures) or $0.003–$0.005/share all-in (equities); limit-target fills haircut to 70% touch-fill; stress at 2x and 3x costs.
- **Pitfalls:** look-ahead in same-bar high/low triggers (assume stop-first fills); survivorship in equity sleeves (point-in-time universe); session-time alignment (RTH vs ETH); event-day selection bias (flag, never drop).
- **Robustness:** plateau heatmaps; bootstrap CIs; placebo direction test (must be ~zero); VIX-quintile and yearly sub-samples; best-year removal test.
- **Acceptance criteria:** OOS PF >= 1.15 net of 2x costs; per-trade t >= 2; OOS Sharpe >= 0.8; max DD <= 2x in-sample; positive in >= 60% of years.

## 8. Sources read (annotated)

1. **Berkowitz, Logan & VanderLinden on implementation shortfall / VWAP.** Search "The Total Cost of Transactions on the NYSE" — VWAP as institutional benchmark. Known via secondary citation.
2. **Brian Shannon, *Technical Analysis Using Multiple Timeframes* / AVWAP.** Publisher/education pages — event-anchored VWAP. Book-level knowledge; practitioner source.
3. **SMB / Aziz VWAP chapters (practitioner).** https://www.smbcap.com ; Bear Bull Traders education — VWAP fade/breakdown tactics. Firm-authored; illustrative.

## 9. Further reading

- Grant–Wolf–Yu intraday VWAP-reversion notes.
- Heston intraday seasonality (timing of fades).
- Exchange VWAP-cross volume share studies.
