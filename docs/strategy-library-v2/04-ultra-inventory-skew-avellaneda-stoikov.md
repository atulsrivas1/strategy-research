# 04. Optimal Inventory-Skew Quoting (Avellaneda–Stoikov) — Twist: SKEW-G

> **Library:** Sigmatiq Strategy Library V2 | **Bucket:** Ultra-short / HFT & scalping | **Style:** Microstructure / stochastic control
> **Instruments:** Equity options market making, liquid ETFs, futures | **Typical holding period:** Seconds to minutes | **Complexity (1–5):** 5 | **Evidence grade (A–C):** B
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise.

## 1. Origin & lineage

**Stochastic-control lineage.** Avellaneda–Stoikov (2008) formalized Ho–Stoll inventory intuition into optimal bid/ask curves; Guéant–Lehalle–Fernandez-Tapia (2013) generalized with closed-form approximations now embedded in bank/CFD internalizers and options market-making engines. Cartea–Jaimungal's *Algorithmic and High-Frequency Trading* (2015, Cambridge) made it the textbook chapter every HFT trainee reads. The desk reality is Jane Street/SIG/Optiver-style options/ETF quoting — same math, hardened with volatility-surface and pin-risk overlays.

## 2. The original rules (as published)

- **Reservation price:** `r = s - q * gamma * sigma^2 * T` (mid minus inventory * risk-aversion * variance * horizon).
- **Optimal spread:** `delta_b + delta_a = gamma*sigma^2*T + (2/gamma)*ln(1 + gamma/k)` (risk + adverse-selection/market-order-arrival terms).
- **Quotes:** bid `r - delta_b`, ask `r + delta_a`; skew deepens automatically as |q| grows.
- **Textbook, not desk-ready:** assumes Poisson order arrival, constant vol, no queue, no fees — every live engine relaxes all four.

## 3. Why it works — mechanism & evidence

**Mechanism.** Inventory is risk: a long book loses if price falls before the round trip completes. The reservation price internalizes that risk so quotes lean against inventory, trading off spread income against variance; the spread term prices order-flow uncertainty (arrival intensity k).

**Supporting evidence (all attributed, none ours):**

- Avellaneda–Stoikov closed forms reproduce intuitive desk behavior (wider in vol, skew with inventory) and are the baseline every quoting paper benchmarks against (theory consensus).
- Guéant–Lehalle–Fernandez-Tapia extensions report tractable multi-asset quoting with similar structure (authors' derivations).
- Cartea–Jaimungal textbook adoption signals practitioner relevance (pedagogical, not a PnL proof).

**Contradictory / decay evidence:**

- Poisson-arrival and constant-vol assumptions fail exactly when quoting matters most (jumps, halts, earnings) — model spreads are too tight in stress.
- No queue priority: textbook fills assume arrival-rate execution, overstating fill rates vs. real queues by multiples.
- Parameter k (order-arrival sensitivity) is unstable intraday; mis-estimated k inverts the spread prescription.

**Synthesis.** The reservation-price idea is the correct inventory engine; the closed-form spread is a starting guess to be overridden by toxicity and queue reality. Value here is discipline (automatic skew + flatten), not the literal formula PnL.

## 4. The twist: SKEW-G

1. **Volatility-oracle override (targets constant-vol failure):** replace sigma with max(model sigma, 1-min realized sigma, options-implied micro-sigma) — widest wins.
2. **Queue-aware spread floor (targets fill illusion):** floor half-spread at max(formula, 1 tick + expected queue-cost) where queue-cost is calibrated per symbol from join-to-fill data.
3. **k-adaptive throttle (targets arrival instability):** estimate k per 15-min bucket; halve quote size when k estimate confidence is low instead of trusting the spread.
4. **Pin/expiry overlay (targets options desks):** within 2 days of expiry, add gamma-proximity widening `+ c*|gamma|*sigma*sqrt(T)` for options books.
5. **Stress flatten (targets jump inventory):** if 1-min absolute move > 4 sigma, cancel to flat-only (bid-only if short, ask-only if long) until vol normalizes.

## 5. Full specification of the twist variant

**Universe.** Options on top-100 single names + SPY/QQQ/ETF options; futures quoting sleeve (ES/NQ).

**Data requirements.** Options quotes/greeks feed, underlying L1/L2, realized-vol oracle (1-min), fee/rebate schedule, expiry/pin calendar.

**Signal definitions (formulas).**

- Reservation `r = mid - q*gamma*maxvar*T`, `maxvar = max(sigma_model, sigma_1m, sigma_iv_micro)^2`.
- Half-spreads `hb, ha = base/2 ± skew(q)` with floor `max(formula_half, 1 tick + queue_cost)`.
- Stress flag `|ret_1m|/sigma_1m > 4` forces flat-only side.

**Entries.**

Two-sided limits at `r ± half` when no stress flag; join only if expected queue time < threshold; size scaled by k-confidence.

**Exits.**

Inventory mean-reversion via skew (automatic); delta-hedge underlying on greek breach schedule; full flatten into expiry pin window and EOD.

**Position sizing.**

q-target bands per symbol (e.g. +/- 200 delta-adjusted lots); gamma-scaled: size *= clip(base_gamma/gamma_now, 0.3, 1.0).

**Risk limits.**

Inventory hard cap; vega cap per expiry; stress-flatten trigger; data-staleness halt; per-day loss halt.

**Cost model & capacity.**

Rebate-aware net spread accounting; hedge-slippage on delta rebalances (1–2 ticks); capacity moderate — edge is per-contract and scales with quoting breadth, not size per quote.

**Parameters to validate (plateau, not peak):** gamma {0.01, 0.05, 0.2}; base spread mult {1.0, 1.5}; stress sigma {3, 4, 5}; k window {5m, 15m, 30m}.

## 6. Failure modes & regime dependence

Volatility-regime misfire (oracle lags true jump vol); pin-week gamma blowups; mis-estimated k that over-quotes into toxic flow; correlated book (all names skewed same way into index jump).

## 7. Validation protocol

**Status: no local backtest exists yet.** This library contains zero proprietary results; everything above is literature.

- **Data:** Options+underlying synchronized replay 12+ months incl. one expiry cycle per name; greeks point-in-time; fee schedules.
- **Splits:** chronological only; train / validation / test by date, never random k-fold on time series. Walk-forward re-fit anchored annually.
- **Cost/slippage model:** fees + rebates at the venue fee schedule, queue-position-aware fill simulation, adverse-selection haircut on marketable fills; stress at 2x and 3x costs.
- **Pitfalls:** look-ahead in signal timestamps (exchange sequence numbers, not wall-clock); survivorship of symbols; same-event ambiguity (both quotes updating in one packet — assume worst fill); latency distribution, not a point estimate.
- **Robustness:** parameter-plateau heatmaps; bootstrap CIs on trade PnL; placebo (randomized signal with identical throttles must be ~zero net of costs); regime sub-samples by spread/volatility quintile and by year; Monte Carlo over queue-position draws.
- **Acceptance criteria:** OOS net Sharpe >= 0.8 after 2x costs; per-trade t >= 2; max intraday drawdown <= 2x in-sample; positive expectancy in >= 60% of months; edge survives removal of the single best month.

## 8. Sources read (annotated)

1. **Avellaneda & Stoikov (2008).** https://arxiv.org/abs/0805.3822 — reservation price + optimal spread. *Taken:* formulas. Known via secondary citation in this pass.
2. **Guéant, Lehalle & Fernandez-Tapia (2013).** https://arxiv.org/abs/1106.3279 — closed-form extensions. *Taken:* multi-asset intuition. Known via secondary citation.
3. **Cartea & Jaimungal, *Algorithmic and High-Frequency Trading* (2015).** https://www.cambridge.org — textbook quoting chapters. *Taken:* desk-hardening checklist. Book-level knowledge.

## 9. Further reading

- Lehalle–Laruelle *Market Microstructure in Practice*.
- Bank single-dealer platform papers on internalization skew.
- Options pin-risk literature (e.g. Ni–Pearson–Poteshman).
