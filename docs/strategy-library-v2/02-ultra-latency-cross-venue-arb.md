# 02. Cross-Venue Latency Arbitrage — Twist: LAT-X

> **Library:** Sigmatiq Strategy Library V2 | **Bucket:** Ultra-short / HFT & scalping | **Style:** Microstructure / arbitrage
> **Instruments:** Dual-listed equities, ETFs vs. basket, futures vs. ETF (ES vs. SPY) | **Typical holding period:** Milliseconds to seconds | **Complexity (1–5):** 5 | **Evidence grade (A–C):** C
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise.

## 1. Origin & lineage

**Latency-arbitrage lineage.** The public story is Michael Lewis *Flash Boys* (2014) and the IEX slow-bump response; the trading lineage is Tower Research, Hudson River Trading, Citadel Securities, and Jump — none publish rules. Academic proxies: Budish–Cramton–Shim on the high-frequency trading arms race (2015) framing latency arb as sniping stale quotes; Aquilina–Budish–O'Neill on latency-arbitrage tax estimates. Our spec is a reconstructed, slower, retail-feasible cousin: lead-lag, not microwave warfare.

## 2. The original rules (as published)

- **Canonical (unpublished) form:** detect a print/quote change on the fast venue, snipe the stale quote on the slow venue before it updates.
- **Published proxy (Budish et al.):** symmetric race — whoever sees the jump first takes the stale quote; speed decides the split.
- **Retail reconstruction:** lead-lag momentum — buy the laggard when the leader jumps beyond transaction-cost bounds, exit on convergence.
- **What is NOT public:** microwave/fiber maps, FPGA decode stacks, per-venue queue-priority behavior — the actual edge.

## 3. Why it works — mechanism & evidence

**Mechanism.** Fragmented markets update asynchronously; the same economic price prints at different times. A fast signal (leader) predicts the slow venue's next quote change over millisecond horizons, before fees wipe it out.

**Supporting evidence (all attributed, none ours):**

- Budish–Cramton–Shim (2015) argue latency arbitrage is a persistent mechanical tax on stale quotes (theory + ES/ETF jump evidence; authors' framing).
- Practitioner lead-lag studies on SPY/ES report sub-second quote leadership (venue/data dependent; treat as indicative, not a promise).
- IEX marketing/whitepapers claim their speed bump reclaims part of the race (venue-authored; read skeptically).

**Contradictory / decay evidence:**

- After the IEX bump, inverted venues, and SIP reforms, textbook cross-venue sniping margins compressed for anyone without top-tier speed.
- Retail data is consolidated/aggregated and delayed tens of milliseconds — the exact signal the HFT version monetizes is invisible on retail stacks.
- Most public 'latency arb' backtests ignore queue position and assume lifting the stale quote in full size; live fills are partial at best.

**Synthesis.** True latency sniping is inaccessible without HFT infrastructure; the tradeable residue for us is slower lead-lag (seconds, not microseconds) around ETFs, futures, and dual listings — a thin statistical edge, not an arb.

## 4. The twist: LAT-X

1. **Leader-jump gate (targets noise trades):** act only on leader jumps > 3x trailing 1-min noise and confirmed by a second correlated leader (e.g. ES + NQ agree).
2. **Cost-band filter (targets fee death):** require predicted convergence >= 2x round-trip fees plus half-spread before firing.
3. **Slow-lane execution (targets infrastructure mismatch):** hold seconds-to-a-minute prediction (laggard drift), entered passively, never marketable into the jump.
4. **Event blackout (targets macro jumps):** no new exposure 60s around scheduled releases (CPI/FOMC) when jumps are adverse-selection, not staleness.
5. **Fill-aware sizing (targets partial-fill illusion):** size to displayed depth at the stale quote minus a 50% haircut; model residual as limit-on-laggard, not a fill.

## 5. Full specification of the twist variant

**Universe.** 40 most liquid ETFs + their futures/components (SPY/ES, QQQ/NQ, IWM/R2000 proxy); 20 dual-listed large caps. One pair per signal.

**Data requirements.** Two synchronized direct-ish feeds (or best available timestamps with measured delay); venue fee schedules; event calendar; latency distribution log per route.

**Signal definitions (formulas).**

- Leader jump `J = (P_lead_now - P_lead_1s) / sigma_1min`; fire if `|J| > 3` and second leader agrees in sign.
- Mispricing `z = (P_lag - beta*P_lead) / rolling_sd_5min`; enter when `|z| > 2` post-jump in the convergence direction.
- Cost band: `|z|*price > 2*(fees + half_spread)` required.

**Entries.**

Passive limit on the laggard at the stale-side quote after leader jump; cancel if leader mean-reverts > 50% before fill; one attempt per jump.

**Exits.**

Limit at converged level (`z` back inside 0.5); time-stop 60s; scratch on fees if convergence stalls; flat EOD (intraday) or roll-aware for futures legs.

**Position sizing.**

Depth-capped: min(model size, 0.5x displayed depth); vol-scaled by 1/sigma_now; daily loss halt at 3x expected per-trade edge.

**Risk limits.**

Pair gross cap; venue-concentration cap; data-staleness halt (>500ms skew between feeds); no adds to a diverging leg.

**Cost model & capacity.**

Taker fees on both legs assumed (conservative); half-spread slippage on exits; capacity tiny — tens of contracts/shares per signal before the quote updates.

**Parameters to validate (plateau, not peak):** Jump threshold {2.5, 3, 4}; z entry {1.5, 2.0, 2.5}; time-stop {30s, 60s, 120s}; cost multiple {1.5, 2.0, 3.0}.

## 6. Failure modes & regime dependence

Feed-delay regime where our 'leader' is itself stale; fee-hike or rebate-cut months; macro-jump days where divergence keeps widening; single-venue halts leaving one leg stranded.

## 7. Validation protocol

**Status: no local backtest exists yet.** This library contains zero proprietary results; everything above is literature.

- **Data:** Dual-feed synchronized replay 12+ months with per-message timestamps; fee schedules point-in-time; halt/event logs.
- **Splits:** chronological only; train / validation / test by date, never random k-fold on time series. Walk-forward re-fit anchored annually.
- **Cost/slippage model:** fees + rebates at the venue fee schedule, queue-position-aware fill simulation, adverse-selection haircut on marketable fills; stress at 2x and 3x costs.
- **Pitfalls:** look-ahead in signal timestamps (exchange sequence numbers, not wall-clock); survivorship of symbols; same-event ambiguity (both quotes updating in one packet — assume worst fill); latency distribution, not a point estimate.
- **Robustness:** parameter-plateau heatmaps; bootstrap CIs on trade PnL; placebo (randomized signal with identical throttles must be ~zero net of costs); regime sub-samples by spread/volatility quintile and by year; Monte Carlo over queue-position draws.
- **Acceptance criteria:** OOS net Sharpe >= 0.8 after 2x costs; per-trade t >= 2; max intraday drawdown <= 2x in-sample; positive expectancy in >= 60% of months; edge survives removal of the single best month.

## 8. Sources read (annotated)

1. **Budish, Cramton & Shim, "The high-frequency trading arms race" (2015).** https://www.jstor.org/stable/43611036 (working paper: https://faculty.chicagobooth.edu/eric.budish/research/hft-arms-race.pdf) — latency arb as sniping. *Taken:* race framing. Not directly re-fetched — known via secondary citation.
2. **Michael Lewis, *Flash Boys* (2014).** Publisher page: https://wwnorton.com/books/9780393351590 — narrative of cross-venue speed advantage. *Taken:* venue-fragmentation context only. Not a strategy manual.
3. **IEX speed-bump materials.** https://iextrading.com — venue-authored claims of race mitigation. *Taken:* existence of countermeasure only; read skeptically.

## 9. Further reading

- Aquilina–Budish–O'Neill latency-arbitrage tax estimates.
- Hasbrouck–Saar low-latency market design papers.
- ETF creation/redemption mechanics for basket-lead-lag extensions.
