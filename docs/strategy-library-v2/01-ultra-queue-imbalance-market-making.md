# 01. Queue-Imbalance Market Making — Twist: QIM-R

> **Library:** Sigmatiq Strategy Library V2 | **Bucket:** Ultra-short / HFT & scalping | **Style:** Microstructure / inventory
> **Instruments:** Liquid US equities, equity options, index futures (ES/NQ) | **Typical holding period:** Seconds to minutes, flat EOD | **Complexity (1–5):** 5 | **Evidence grade (A–C):** B
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise.

## 1. Origin & lineage

**Electronic market-making lineage.** Virtu Financial and Citadel Securities are the canonical modern market makers; Virtu's S-1/10-K filings and founder Vincent Viola's interviews describe spread capture across thousands of symbols with sub-second inventory control. Academic lineage: Ho–Stoll (1981) dealer inventory model; Avellaneda–Stoikov (2008) optimal quotes; empirical order-book imbalance work by Cont–Kukanov–Stoikov (2014). Practitioner bridge: how-to literature on level-2 quoting (Jigsaw, Bookmap education) shows the same object — lean on the heavier book side, fade prints against thin liquidity.

## 2. The original rules (as published)

- **Signal (Cont–Kukanov–Stoikov framing):** order-book imbalance `OBI = (Q_bid - Q_ask) / (Q_bid + Q_ask)` over top N levels predicts the next mid-price move; quote passively on the heavy side, avoid lifting the thin side.
- **Quotes:** two-sided limit quotes at touch or one tick inside; skew by inventory (Ho–Stoll): lower both quotes when long, raise when short.
- **Cancel/replace:** on every top-of-book change or inventory breach; hard flatten into halts and the close.
- **What is NOT public:** exact venue routing tables, queue-priority tricks, per-symbol skew curves, and toxicity filters — all proprietary.

## 3. Why it works — mechanism & evidence

**Mechanism.** Adverse selection vs. uninformed flow: passive quotes earn the spread from impatient retail/ETF flow and lose to informed sweeps. Imbalance proxies short-horizon informed direction, so conditioning quotes on it cuts the toxic-fill rate while keeping queue priority in calm flow.

**Supporting evidence (all attributed, none ours):**

- Cont–Kukanov–Stoikov (2014) report imbalance predicts next mid-move across NYSE stocks (authors' claim, widely replicated in practitioner tests).
- Virtu 10-K filings report market-making profitability in the overwhelming majority of trading days over multi-year windows (company filing; venue mix and risk undisclosed).
- Avellaneda–Stoikov (2008) derive closed-form optimal bid/ask spreads rising in volatility and inventory (theory, not a PnL claim).

**Contradictory / decay evidence:**

- Tick-size regime changes (Tick Size Pilot) moved queue dynamics materially; published imbalance coefficients do not transfer across tick regimes without refit.
- Retail wholesaler internalization (PFOF) skims the most uninformed flow before it reaches lit books, thinning the exact flow this strategy wants.
- Queue-position reality: backtests assuming touch fills overstate edge 2–5x vs. queue simulation (practitioner consensus, e.g. Jigsaw/Bookmap education).

**Synthesis.** Spread capture conditioned on imbalance is a real but infrastructure-grade edge: it survives only with co-location, queue simulation honesty, and inventory discipline. Retail-style 'always quote both sides' without toxicity gating is negative expectancy after fees.

## 4. The twist: QIM-R

1. **Regime-gated quoting (targets toxic fills):** quote only when trailing 5-min realized vol is inside its 20-day interquartile range and spread <= 2 ticks; otherwise widen 2x or stand down.
2. **Imbalance + microprice agreement (targets false leans):** require OBI and microprice deviation to agree in sign; microprice `M = (Q_a*P_b + Q_b*P_a)/(Q_a+Q_b)` must deviate >= 0.15 ticks from mid in the lean direction.
3. **Toxicity kill-switch (targets informed sweeps):** halt quoting 30s after any 1-min sweep > 4x median trade size or VPIN-style volume-bucket spike.
4. **Inventory urgency curve (targets overnight/disaster holds):** skew `delta = gamma * inv * sigma^2 * T` with hard flatten at +/- K shares; no adds into a losing inventory beyond the cap.
5. **Fee-aware venue choice (targets rebate illusion):** route passive adds only to venues where expected rebate exceeds modeled adverse-selection cost for that symbol/decile.

## 5. Full specification of the twist variant

**Universe.** Top 500 US equities by dollar volume + ES/MES front month. Exclude hard-to-borrow, halted, ex-div/takeover names, and tick > 5c relative names during learning.

**Data requirements.** L2/MBO or L3 feed with exchange sequence numbers and queue-position reconstruction; trade prints with aggressor flags; venue fee schedules; corporate-action calendar; colocation latency logs.

**Signal definitions (formulas).**

- `OBI_3 = (sum bid sizes L1–L3 - sum ask sizes L1–L3) / (sum both)`; z-scored per symbol over trailing 30 min.
- Microprice deviation `d = (M - mid) / tick`; entry gate `|d| >= 0.15` with sign(OBI_3) == sign(d).
- Toxicity `TOX = sweep_volume_1m / median_20d`; halt if `TOX > 4`.
- Reservation skew `r = mid - gamma * inv * sigma^2 * T_close`; quotes `r ± (spread_base/2 + k*sigma)`.

**Entries.**

Post bid at `r - half_spread` and ask at `r + half_spread` when gates pass; join touch only if modeled queue time < 3s; never cross the spread to initiate.

**Exits.**

Fill-to-fill round trips; inventory mean-reverts via skew (no stop in the directional sense); emergency market-out if inventory cap breached or halt/event flag fires; flat by 15:55 ET.

**Position sizing.**

Per-quote size = base lots * vol_factor where vol_factor = clip(median_sigma/sigma_now, 0.25, 1.5); symbol cap by ADV participation (< 0.5% ADV per side).

**Risk limits.**

Per-symbol inventory cap; book gross cap; per-day loss halt at 2x expected daily spread income; quoting halt on data staleness > 200ms or sequence gap.

**Cost model & capacity.**

Model maker rebate minus taker fee on emergency exits; queue-slippage via simulated position (conservative: assume back-of-queue on joins); capacity is infrastructure-bound — edge decays steeply above a few thousand shares per symbol per day without tiered routing.

**Parameters to validate (plateau, not peak):** OBI levels {1, 3, 5}; d threshold {0.10, 0.15, 0.25}; spread multiplier {1.0, 1.5, 2.0}; gamma {0.01, 0.05, 0.1}; halt windows {15s, 30s, 60s}.

## 6. Failure modes & regime dependence

TOX regime shifts (news-driven informed share spikes); tick-regime changes; rebate cuts; latency jitter that turns joins into adverse fills; correlated inventory across symbols in a market-wide sweep.

## 7. Validation protocol

**Status: no local backtest exists yet.** This library contains zero proprietary results; everything above is literature.

- **Data:** L2 replay 12+ months with sequence numbers, venue fees as of each date, corporate actions point-in-time.
- **Splits:** chronological only; train / validation / test by date, never random k-fold on time series. Walk-forward re-fit anchored annually.
- **Cost/slippage model:** fees + rebates at the venue fee schedule, queue-position-aware fill simulation, adverse-selection haircut on marketable fills; stress at 2x and 3x costs.
- **Pitfalls:** look-ahead in signal timestamps (exchange sequence numbers, not wall-clock); survivorship of symbols; same-event ambiguity (both quotes updating in one packet — assume worst fill); latency distribution, not a point estimate.
- **Robustness:** parameter-plateau heatmaps; bootstrap CIs on trade PnL; placebo (randomized signal with identical throttles must be ~zero net of costs); regime sub-samples by spread/volatility quintile and by year; Monte Carlo over queue-position draws.
- **Acceptance criteria:** OOS net Sharpe >= 0.8 after 2x costs; per-trade t >= 2; max intraday drawdown <= 2x in-sample; positive expectancy in >= 60% of months; edge survives removal of the single best month.

## 8. Sources read (annotated)

1. **Avellaneda & Stoikov, "High-frequency trading in a limit order book" (2008).** https://arxiv.org/abs/0805.3822 — optimal market-making quotes under inventory risk. *Taken:* reservation-price skew and spread formulas. Not directly re-fetched in this pass — known via secondary citation.
2. **Cont, Kukanov & Stoikov, "The price impact of order book events" (2014).** https://arxiv.org/abs/1207.0325 — imbalance predicts next mid-move. *Taken:* OBI definition and predictive claim. Not directly re-fetched — known via secondary citation.
3. **Virtu Financial 10-K filings.** https://ir.virtu.com/financial-information/sec-filings — profitable-days disclosure. *Taken:* existence claim only; no strategy parameters. Not directly re-fetched — known via secondary citation.
4. **Ho & Stoll, "Optimal dealer pricing under transactions and return uncertainty" (1981).** Journal of Financial Economics — inventory-skew foundation. *Taken:* skew intuition. Paywalled/abstract-level knowledge; marked honestly.

## 9. Further reading

- Guéant–Lehalle–Fernandez-Tapia optimal quoting extensions.
- Virtu S-1 narrative on technology and risk controls.
- Exchange fee-schedule archives for rebate modeling.
