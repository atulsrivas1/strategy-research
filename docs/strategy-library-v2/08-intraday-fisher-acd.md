# 08. Fisher ACD Reference Levels — Twist: ACD-R

> **Library:** Sigmatiq Strategy Library V2 | **Bucket:** Intraday | **Style:** Breakout / reference levels
> **Instruments:** ES/NQ futures, liquid equities, commodities | **Typical holding period:** 30 min – 4 h, flat by close | **Complexity (1–5):** 3 | **Evidence grade (A–C):** B-
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise.

## 1. Origin & lineage

**Mark Fisher (2002).** *The Logical Trader* (Wiley; foreword Paul Tudor Jones): founder of MBF Clearing (<1% to ~20% of NYMEX clearing), youngest silver-pit trader at 21, Wharton 1982. Publisher states he taught ACD to 5,000+ traders including Tudor. ACD = ORB with bias-reversal logic (A/C entries, B/D exits) and per-market volatility offsets (A/C values). Fisher's stated belief: sharing levels makes them more effective (self-reinforcing reference points).

## 2. The original rules (as published)

- **OR:** first 5–30 min per market (15 min S&P example).
- **A entry:** price at ORH + A-value (A-up) or ORL - A-value (A-down) AND holding half the OR duration; one A per session. Example offsets: 3 pts S&P (2004 era), $0.27 Broadcom (era-specific — do not copy numbers).
- **B stop:** opposite OR boundary; failed A-up exits through ORL.
- **C reversal:** after A-up, break to ORL - C-value sustained half-OR duration reverses to short; C calibrated independently (book example 6–8 pts below ORL in a ~2575 market; later C = more intense move).
- **D stop:** 1 tick beyond opposite OR extreme. Pivot range + Macro ACD layer multi-day context.

## 3. Why it works — mechanism & evidence

**Mechanism.** Reference-point self-reinforcement: thousands of traders watching the same A/C levels turns them into coordination devices; volatility-calibrated offsets + time-confirmation filter out wick noise; C-reversal harvests failed-breakout inventory (same economics as sweep-fade, slower).

**Supporting evidence (all attributed, none ours):**

- Publisher/Fisher claim: profitable implementation by floor/computer traders at major NY exchanges (venue lore; unaudited).
- ORB-adjacent evidence in Sec. 07 (tick-stream/backtestsnotsignals continuation PF 1.1–1.3) supports the A-leg; C-leg is a failed-breakout rule with sweep-fade economics (weaker standalone statistics).
- Practitioner ACD-room literature reports consistency from selectivity (one A per day) rather than frequency.

**Contradictory / decay evidence:**

- A/C offsets are era- and market-specific; copying 2002/2004 point values to modern ES/NQ guarantees miscalibration (vol regimes differ by multiples).
- Time-confirmation (half-OR hold) lags fast markets; on trend days the A triggers late with poor reward:risk.
- No peer-reviewed ACD-specific profitability study we know of — evidence is practitioner-reported.

**Synthesis.** ACD is a disciplined ORB-plus-reversal checklist, not a magic level set: its durable parts are one-attempt selectivity, volatility-scaled offsets, and the failed-A reversal; its fragile parts are literal point values and rigid time-holds.

## 4. The twist: ACD-R

1. **ATR-scaled offsets (targets stale point values):** A = 0.15x ATR-micro, C = 0.30x ATR-micro, recomputed daily; never hard-code points.
2. **Volume-confirmed A (targets late/chop entries):** require RVOL-at-trigger >= 1.25 and pace (range/time) above median.
3. **Failed-A reversal only with reclaim (targets premature C):** C fires only after close back through OR extreme + absorption ratio > 2x (merge with SWEEP-F logic).
4. **Macro-pivot gate (targets counter-trend As):** skip A against the daily pivot-range side when Macro ACD bias opposes (stand down, do not flip to C either).
5. **One-and-done + time-stop (targets overtrading):** one A attempt; if C fails, day is over; flatten 15:30 ET if neither target nor stop.

## 5. Full specification of the twist variant

**Universe.** ES/NQ + 50 liquid equities; one A per name per day.

**Data requirements.** 1-min/5-min bars, ATR-micro + ATRd, RVOL time-of-day, daily pivot range (H+L+C)/3 band, VIX regime flag.

**Signal definitions (formulas).**

- OR 09:30–09:45; A_up = ORH + 0.15*ATRm; A_dn = ORL - 0.15*ATRm; C_up/down at ±0.30*ATRm beyond opposite extreme.
- Confirm: close beyond offset for >= half-OR duration (7–8 min for 15-min OR) AND RVOL >= 1.25.
- Macro gate: skip A-up if price < prior pivot range and pivot slope down (mirror down).

**Entries.**

Stop/limit at confirmed A (one per day); C reversal only on confirmed reclaim + absorption; no second C.

**Exits.**

B/D stops as published (opposite extreme + 1 tick); target 2R or VWAP-band edge; time-stop 15:30 ET; hard flat 15:55 ET.

**Position sizing.**

0.5% risk; width factor inverse to A-distance/ATRd; cap 4x notional.

**Risk limits.**

One A + optional one C per day; VIX-spike skip shared with 07; halt after one full C stop.

**Cost model & capacity.**

Same as 07 plus reclaim-entry spread cost on C legs; capacity intraday-fine.

**Parameters to validate (plateau, not peak):** A {0.10, 0.15, 0.20 ATRm}; C {0.25, 0.30, 0.40 ATRm}; RVOL {1.1, 1.25, 1.5}; hold {0.33, 0.5, 0.75 x OR}.

## 6. Failure modes & regime dependence

Offset miscalibration after vol-regime jumps; late-A entries on trend days; C into genuine initiative (the SWEEP-F failure repeated slower).

## 7. Validation protocol

**Status: no local backtest exists yet.** This library contains zero proprietary results; everything above is literature.

- **Data:** 1-min 2016–present + pivot history; futures roll-aware; equity point-in-time.
- **Splits:** chronological train / validation / test; no random k-fold. Walk-forward re-fit anchored annually.
- **Cost/slippage model:** commission + 1–2 ticks slippage per side (futures) or $0.003–$0.005/share all-in (equities); limit-target fills haircut to 70% touch-fill; stress at 2x and 3x costs.
- **Pitfalls:** look-ahead in same-bar high/low triggers (assume stop-first fills); survivorship in equity sleeves (point-in-time universe); session-time alignment (RTH vs ETH); event-day selection bias (flag, never drop).
- **Robustness:** plateau heatmaps; bootstrap CIs; placebo direction test (must be ~zero); VIX-quintile and yearly sub-samples; best-year removal test.
- **Acceptance criteria:** OOS PF >= 1.15 net of 2x costs; per-trade t >= 2; OOS Sharpe >= 0.8; max DD <= 2x in-sample; positive in >= 60% of years.

## 8. Sources read (annotated)

1. **Fisher, *The Logical Trader* publisher page (Wiley-VCH).** https://www.wiley-vch.de/en/areas-interest/finance-economics-law/the-logical-trader-978-0-471-21551-6 — bio, contents, teaching claim.
2. **Investopedia ACD primers (2004).** Search "Spotting Breakouts As Easy As ACD" — A/B/C/D mechanics, half-OR hold, worked offsets. Excerpt-level knowledge; fetch walls noted honestly.
3. **ORB evidence base (see doc 07 sources).** *Taken:* continuation PF/cost framing carries over to the A-leg.

## 9. Further reading

- Fisher (2002) full text — pivot range + Macro ACD chapters.
- Crabel (1990) stretch/OR comparison.
- Pivot-moving-average extensions in practitioner ACD rooms.
