# 07. Crabel Opening Range Breakout — Twist: ORB-VF2

> **Library:** Sigmatiq Strategy Library V2 | **Bucket:** Intraday | **Style:** Breakout / momentum
> **Instruments:** MNQ/NQ, MES/ES, QQQ/SPY, liquid large caps | **Typical holding period:** 15 min – 3 h, flat by close | **Complexity (1–5):** 2 | **Evidence grade (A–C):** B
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise.

## 1. Origin & lineage

**Toby Crabel (1990).** *Day Trading With Short Term Price Patterns and Opening Range Breakout* (Traders Press; out of print, secondary prices >$1,000) codified the ORB: the first minutes contain disproportionate information because overnight accumulation executes in a compressed window. Crabel founded Crabel Capital Management; secondary sources describe no losing year 1991–2002. Floor-trader cousin: CBOT Market Profile Initial Balance (Steidlmayer). Modern mechanical packaging: Zarattini–Aziz 5-min QQQ ORB (SSRN 2023). Prop desks today use the OR mostly as reference structure; retail trades it mechanically — our twist conditions it on regime.

## 2. The original rules (as published)

- **Crabel:** OR = high–low of initial interval (1/5/10/15/30 min tested). Buy-stop above ORH / sell-stop below ORL; opposite side is the stop; hold intraday to next-day close variants. Stretch entry: open ± 10-day average noise. NR4/NR7/inside-day contraction filters precede the best ORBs.
- **Zarattini–Aziz (2023):** 5-min OR on QQQ; direction = first-candle sign; enter second-candle open; stop at first-candle extreme; target 10R or EOD; 1% risk, 4x leverage cap; $0.0005/share, no slippage (material caveat).
- **Disagreements:** OR length (5 vs 15 vs 30/60), trigger (stretch vs OR break vs first-candle sign), stop (opposite extreme vs first-candle extreme), target (close vs 10R vs 2R).

## 3. Why it works — mechanism & evidence

**Mechanism.** Order-flow concentration at the open plus anchoring on the OR reference plus volatility cycling (contraction then expansion) plus intraday continuation once morning-range commitment prints.

**Supporting evidence (all attributed, none ours):**

- Zarattini–Aziz (2023) report QQQ 5-min ORB 2016–Feb 2023: 675% total vs 169% buy-hold, alpha 33% (p=0.0025), Sharpe ~1.12, win 24% over 1,795 trades (their computation, no slippage).
- tick-stream (2026, NQ 2019–2026, real costs, train/holdout): 15-min breakout +2R target +$205,612 (t=2.09), PF ~1.1 — thin, stable continuation edge.
- backtestsnotsignals (2026, MNQ/Databento): IS Sharpe 1.37 PF 1.43; OOS Sharpe 1.10 PF 1.32 with SMA-200 filter + one-loss-per-day.

**Contradictory / decay evidence:**

- Fading the OR loses at every range length (tick-stream 15-min fade t=-4.0); viral fixed-small-target breakouts are ~breakeven (PF ~1.01).
- Zarattini replication (mohitbgupta75): breakeven at ~2.2c/share slippage; NQ-confirmation filter lifts edge but 76% of filtered PnL comes from 2022 alone — regime effect, not structure.
- paperswithbacktest replication: 16-yr Sharpe -0.06; post-publication -0.84. QuantifiedStrategies: simple S&P ORB 'does not work very well anymore' (~0.04%/trade).

**Synthesis.** Continuation under the ORB is real but thin (PF 1.1–1.3 honest), regime-concentrated, cost-fragile, and exit-sensitive (let winners run; small fixed targets destroy it). Justifies a filtered, regime-conditioned variant.

## 4. The twist: ORB-VF2

1. **Gap-agreement/gap-fade gate (targets false breaks on gap shocks):** long only if material gap agrees OR gap already filled pre-trigger; mirror for shorts.
2. **Relative-volume gate (targets dead-day chop):** RVOL30 >= 1.5 vs 20-session same-window median.
3. **VIX-spike skip (targets disorderly opens):** skip if VIX(09:35) > 1.10x prior close or >= 35; level regimes still trade, day-over-day shocks do not.
4. **Inverse range-width sizing (targets wide-range stop-outs):** size *= clip(0.5*ATRd/ORW, 0.25, 1.5); narrow post-contraction ranges get full size.
5. **Time-stop + run-to-target (targets let-it-run without overnight risk):** target 2.0x ORW (grid 1.5–3.0); flatten 11:30 ET if untriggered; hard flat 15:55 ET.

## 5. Full specification of the twist variant

**Universe.** MNQ/NQ + MES/ES front month; QQQ/SPY secondary; optional mega-cap sleeve. One instrument per signal; no pyramiding.

**Data requirements.** 1-min bars (5-min signals), RTH + prior-day H/L/C, ETH gap context, VIX 1-min, 20-session time-of-day volume, ATR(14) daily.

**Signal definitions (formulas).**

- OR 09:30–09:45: ORH/ORL/ORW. ATRd = ATR(14) daily RTH.
- Gap g = (open - prior close)/prior close; material if |g| >= 0.25*ATRd/close. Faded = traded at/beyond prior close pre-trigger.
- RVOL30 = vol(09:30–10:00)/median20. VIX spike as above. Skip if ORW > 0.60 ATRd or < 0.05 ATRd.

**Entries.**

Resting stops 09:45: long >= ORH+1 tick, short <= ORL-1 tick; window 09:45–11:00 ET; direction + RVOL + VIX + sanity gates; one entry per direction; stop trading after one full stop-out.

**Exits.**

Stop opposite OR (mid-OR if ORW > 0.35 ATRd); target entry + 2.0 ORW (optional 50% at 1.5x); time-stop 11:30 ET; hard flat 15:55 ET.

**Position sizing.**

Base 0.5% equity risk; width factor w as above; contracts = floor(R*w/(stop_dist*point_value)); 4x notional cap; skip if < 1 micro at 0.25x.

**Risk limits.**

One stop-out per day then done; event-calendar flag (FOMC/CPI/NFP) as sub-sample, never a post-hoc drop; width sanity gates.

**Cost model & capacity.**

Micros $0.68–$1.50/side; model $4.50 RT + 2-tick entry + 1 extra tick on stops; target limits at 70% touch-fill. Capacity fine to mid-7-figures intraday.

**Parameters to validate (plateau, not peak):** OR {10,15,20,30}; RVOL {1.25,1.5,2.0}; target {1.5,2.0,2.5,3.0}; VIX {1.08,1.10,1.15}.

## 6. Failure modes & regime dependence

Low-vol grinds (2017/2023-type quarters flat-to-down); regime concentration (2022-style bears carry PnL — monitor VIX-quintile attribution); post-publication crowding on 5-min QQQ; gap-shock whipsaw accepted as cost; same-bar stop/target ambiguity (use stop-first fills).

## 7. Validation protocol

**Status: no local backtest exists yet.** This library contains zero proprietary results; everything above is literature.

- **Data:** 1-min 2016–present (Databento/similar) + VIX 1-min; futures roll handled (back-adjusted context, unadjusted trade prices); equity sleeve point-in-time.
- **Splits:** chronological train / validation / test; no random k-fold. Walk-forward re-fit anchored annually.
- **Cost/slippage model:** commission + 1–2 ticks slippage per side (futures) or $0.003–$0.005/share all-in (equities); limit-target fills haircut to 70% touch-fill; stress at 2x and 3x costs.
- **Pitfalls:** look-ahead in same-bar high/low triggers (assume stop-first fills); survivorship in equity sleeves (point-in-time universe); session-time alignment (RTH vs ETH); event-day selection bias (flag, never drop).
- **Robustness:** plateau heatmaps; bootstrap CIs; placebo direction test (must be ~zero); VIX-quintile and yearly sub-samples; best-year removal test.
- **Acceptance criteria:** OOS PF >= 1.15 net of 2x costs; per-trade t >= 2; OOS Sharpe >= 0.8; max DD <= 2x in-sample; positive in >= 60% of years.

## 8. Sources read (annotated)

1. **Zarattini & Aziz, "Can Day Trading Really Be Profitable?" SSRN 4416622 (2023).** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4416622 — 5-min QQQ ORB rules + headline claims + no-slippage caveat. Known via secondary citation + prior V1 read.
2. **tick-stream, "Does the NY Opening-Range Breakout Actually Work?" (June 2026).** https://tick-stream.xyz/blog/does-opening-range-breakout-work-backtest-nq — full-matrix NQ test, costs, train/holdout, same-bar bug tale. Known via secondary citation + prior V1 read.
3. **Trade Loss Tracker extended summary of Crabel (1990).** https://tradelosstracker.com/library/book/141-day-trading-with-short-term-price-patterns-and-opening/extended — NR4/NR7/ID frequencies, stretch ambiguity. Known via secondary citation.
4. **Fisher, *The Logical Trader* publisher page (Wiley).** https://www.wiley-vch.de/en/areas-interest/finance-economics-law/the-logical-trader-978-0-471-21551-6 — ACD lineage context. Publisher page.

## 9. Further reading

- Crabel (1990) primary text — desk library copy.
- Steidlmayer Market Profile / Initial Balance literature.
- Raschke–Connors *Street Smarts* (1995) NR4/inside-day practice.
