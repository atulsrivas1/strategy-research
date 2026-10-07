# 06. Liquidity-Sweep Fade — Twist: SWEEP-F

> **Library:** Sigmatiq Strategy Library V2 | **Bucket:** Ultra-short / HFT & scalping | **Style:** Microstructure mean reversion
> **Instruments:** ES/NQ, liquid large caps, FX majors | **Typical holding period:** Seconds to minutes | **Complexity (1–5):** 3 | **Evidence grade (A–C):** C
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise.

## 1. Origin & lineage

**Stop-hunt lineage.** Practitioner lineage is ICT (Inner Circle Trader / Michael Huddleston) liquidity-sweep concepts — equal highs/lows raided then reversed — plus classic floor lore ('stops get run before the real move') and academic stop-clustering evidence (Osler on stop-loss orders clustering at round numbers; Cavallo–Kreuser on FX stop hunts). Our spec strips the ICT mystique into a testable sweep-and-reclaim rule.

## 2. The original rules (as published)

- **ICT rendering:** price raids equal highs/lows (buy-side/sell-side liquidity), displaces, then closes back inside — the sweep is the entry trigger.
- **Floor rendering:** run of stops through an obvious level that fails to hold = fade back to value.
- **Academic cousin:** Osler documents stop clustering; price overreacts through clusters then mean-reverts (sample-specific).
- **What is NOT rigorous:** ICT displacement/fair-value-gap definitions are visual, not coded; no published hit-rate survives costs in independent tests we know of.

## 3. Why it works — mechanism & evidence

**Mechanism.** Stale stops cluster at obvious levels; a sweep triggers cascading market orders that exhaust against resting limit supply. Post-sweep, the order-flow impulse is spent and inventory mean-reverts — the fade harvests the snap-back, not the breakout.

**Supporting evidence (all attributed, none ours):**

- Osler (2003/2005) documents FX stop clustering and rapid reversal after cluster triggers (author's sample; often cited).
- Practitioner sweep-reversal compilations show textbook examples on index futures around equal highs/lows (illustrative, unaudited).
- Limit-order-book resilience literature finds spreads/depth snap back within seconds-to-minutes after sweeps (market-dependent).

**Contradictory / decay evidence:**

- ICT-style concepts have no peer-reviewed profitability evidence; independent retail tests of sweep-fades net of costs are flat-to-negative.
- Real breakouts also start as sweeps — fading every raid is fading genuine initiative flow (the failure mode).
- Equal-high/low identification is subjective; backtest definitions rarely match live eyeballing.

**Synthesis.** Sweep-fades are a low-win-rate timing overlay at best: only tradeable with strict reclaim confirmation, tiny risk, and a breakout-abort rule — otherwise it is catching falling knives at liquidity events.

## 4. The twist: SWEEP-F

1. **Reclaim confirmation (targets premature fades):** enter only after price reclaims the swept level AND closes back inside on the entry timeframe (no wick-only entries).
2. **Sweep-quality gate (targets random wicks):** require sweep extreme to exceed level by >= 0.2 ATR-micro but <= 1.0 ATR-micro (real raid, not a trend break).
3. **Absorption corroboration (targets breakout confusion):** require post-sweep absorption ratio > 2x median (aggressor exhausted) before fading.
4. **Trend-day abort (targets initiative days):** no fades when daily range already > 1.5x ATRd or VWAP trend is one-sided (|z| > 2); sweeps on trend days are breakouts.
5. **One-shot rule (targets revenge fading):** one fade per level per day; after a failed fade, that level is off-limits (it is now a breakout level).

## 5. Full specification of the twist variant

**Universe.** ES/NQ front month; EURUSD/GBPUSD; top-50 equities. Equal-high/low and round-number levels only.

**Data requirements.** Tick/1-min with highs/lows catalog (equal-high tolerance 2 ticks), ATR-micro, ATRd, VWAP z-score, absorption ratio feed.

**Signal definitions (formulas).**

- Sweep: extreme pokes level by `s` ticks where `0.2*ATRm <= s <= 1.0*ATRm`.
- Reclaim: close back through level on entry timeframe within 3 bars.
- Absorption: `ABS_post > 2*median`; trend abort if `daily_range > 1.5*ATRd` or `|VWAPz| > 2`.

**Entries.**

Limit at reclaimed level (fade direction); stop beyond sweep extreme + 1 tick; one attempt per level per day.

**Exits.**

Target mid-range/VWAP or 1.5R; time-stop 10 min; abort to scratch if level re-breaks within 2 bars.

**Position sizing.**

0.25% risk (half standard) — explicitly a low-edge timing trade; no scaling.

**Risk limits.**

Per-day fade-stop cap (2); trend-day blanket ban; event blackout around scheduled prints.

**Cost model & capacity.**

Marketable reclaim entries cost the spread; assume 1–2 ticks slippage; capacity small by design (opportunistic overlay).

**Parameters to validate (plateau, not peak):** Sweep depth {0.15, 0.2, 0.3 ATRm}; reclaim bars {2, 3, 5}; ABS {1.5, 2.0, 3.0}; trend abort {1.25, 1.5, 2.0 ATRd}.

## 6. Failure modes & regime dependence

Trend-day sweeps that keep going (initiative); spoofed levels with no real stops behind them; double-sweep chop that stops both sides.

## 7. Validation protocol

**Status: no local backtest exists yet.** This library contains zero proprietary results; everything above is literature.

- **Data:** Tick replay 24+ months incl. trend and range regimes; level catalog rules frozen pre-test; cost stress 2–3x.
- **Splits:** chronological only; train / validation / test by date, never random k-fold on time series. Walk-forward re-fit anchored annually.
- **Cost/slippage model:** fees + rebates at the venue fee schedule, queue-position-aware fill simulation, adverse-selection haircut on marketable fills; stress at 2x and 3x costs.
- **Pitfalls:** look-ahead in signal timestamps (exchange sequence numbers, not wall-clock); survivorship of symbols; same-event ambiguity (both quotes updating in one packet — assume worst fill); latency distribution, not a point estimate.
- **Robustness:** parameter-plateau heatmaps; bootstrap CIs on trade PnL; placebo (randomized signal with identical throttles must be ~zero net of costs); regime sub-samples by spread/volatility quintile and by year; Monte Carlo over queue-position draws.
- **Acceptance criteria:** OOS net Sharpe >= 0.8 after 2x costs; per-trade t >= 2; max intraday drawdown <= 2x in-sample; positive expectancy in >= 60% of months; edge survives removal of the single best month.

## 8. Sources read (annotated)

1. **Osler on stop-loss clustering (FX).** Search: https://papers.ssrn.com "Stop-loss orders and price cascades" — clustering evidence. *Taken:* clustering premise. Known via secondary citation.
2. **ICT liquidity concepts (practitioner).** Search "Inner Circle Trader liquidity sweep" — equal-high/low raid framing. *Taken:* level taxonomy only; no profitability claim accepted. Practitioner-authored.
3. **Limit-order-book resiliency literature.** E.g. Degryse et al. on resiliency; exchange microstructure papers — spreads snap back post-sweep. *Taken:* snap-back mechanism. Abstract-level knowledge.

## 9. Further reading

- Cavallo–Kreuser FX stop-hunt case studies.
- Floor-trader stop-run anecdotes (Schwager *Market Wizards* interviews).
- Exchange depth-resiliency empirical papers per venue.
