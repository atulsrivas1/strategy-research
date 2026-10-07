# 12. Wyckoff–Footprint Intraday Auction — Twist: WYK-FP

> **Library:** Sigmatiq Strategy Library V2 | **Bucket:** Intraday | **Style:** Microstructure / auction
> **Instruments:** ES/NQ, CL/GC, BTC/ETH perps | **Typical holding period:** 10 min – 2 h, flat by close | **Complexity (1–5):** 4 | **Evidence grade (A–C):** C+
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise.

## 1. Origin & lineage

**Richard Wyckoff (1908–1930s) → modern footprint.** Wyckoff schematics (accumulation/distribution, springs/upthrusts, SOS/SOW) via *Wyckoff Analytics* (Roman Bogomazov) meet footprint/volume-delta tooling (Jigsaw/Bookmap/ATAS) and SMB tape-reading. Academic cousins: Kyle (1985) informed-flow impact; Hasbrouck microstructure; unfinished-auction/single-print concepts from Market Profile (Steidlmayer/Dalton). Our spec codes springs/upthrusts as footprint-confirmed events.

## 2. The original rules (as published)

- **Wyckoff:** spring = false breakdown of trading-range low on reduced spread/volume that returns inside; upthrust = mirror; SOS/SOW = sign of strength/weakness (widening spread + volume in the markup direction).
- **Footprint overlay:** spring confirmed by delta divergence + excess tail; upthrust by stacked ask imbalances failing to hold.
- **Market Profile overlay:** single prints/unfinished auction = acceptance gaps the auction revisits.
- **What is NOT coded in the literature:** spread/volume thresholds, confirmation bars, and failure definitions — all chart-read.

## 3. Why it works — mechanism & evidence

**Mechanism.** Composite-operator inventory: absorption at range edges (spring) or distribution at highs (upthrust) precedes markup/markdown; footprint shows the absorption quantitatively (delta vs price), and single prints mark where the auction was interrupted — the revisit level.

**Supporting evidence (all attributed, none ours):**

- Wyckoff Analytics case library documents spring/upthrust sequences across futures/FX (educational, illustrative).
- Kyle/Hasbrouck impact logic supports absorption-then-continuation sequencing (theory, not a Wyckoff PnL proof).
- Market Profile single-print revisit behavior is widely reported by auction-market practitioners (consistent anecdote).

**Contradictory / decay evidence:**

- Wyckoff schematics are Rorschach patterns: inter-rater reliability is low and published examples are selected.
- No peer-reviewed Wyckoff-spring profitability study net of costs; footprint-confirmation adds precision but no published Sharpe.
- Springs fail in trend-accumulation transitions (range is actually re-accumulation for continuation — faded wrong).

**Synthesis.** Wyckoff gives a useful event vocabulary (spring/upthrust/SOS) and footprint gives the measurement; together they form a disciplined range-edge timing system — but only with frozen event definitions and a trend/re-accumulation filter.

## 4. The twist: WYK-FP

1. **Frozen spring/upthrust (targets eyeball drift):** spring = low pokes range low by 0.1–0.3 ATRm, closes back inside within 2 bars, bar range < 0.75x median; footprint requires delta-divergence (price low < prior low, delta low > prior delta low).
2. **Range-quality gate (targets trend-mistakes):** range must be >= 20 bars and <= 1.0 ATRd wide with flat 20-bar slope (|slope| < 0.2 ATRd); sloping ranges excluded (likely re-accumulation).
3. **Single-print magnet (targets random targets):** targets are the nearest unfinished-auction/single-print edge or range opposite third — never fixed R.
4. **SOS/SOW continuation guard (targets faded breakouts):** if post-spring SOS prints (close in top 10% + volume > 1.5x median), add half; if SOW instead, scratch immediately.
5. **Session throttle (targets overnight holds):** intraday ranges only (ETH/range formed 02:00–09:30 ET or RTH morning); flat EOD, never carry a range trade.

## 5. Full specification of the twist variant

**Universe.** ES/NQ, CL/GC, BTC/ETH perps (24/7 adapted session windows); one range at a time per symbol.

**Data requirements.** Tick/footprint or 1-min with delta, range detector, Market Profile single-print catalog, ATRm/ATRd, session clock.

**Signal definitions (formulas).**

- Range: 20+ bars, width <= 1.0 ATRd, slope filter. Spring/upthrust geometry + 2-bar reclaim as above.
- Divergence: delta-low vs price-low comparison over spring window. SOS: close position + volume gate.

**Entries.**

Limit at range-edge reclaim post-divergence; stop beyond spring extreme + 0.05 ATRm; one spring + one add max.

**Exits.**

Single-print magnet or opposite third; SOS-add exits at range measured-move (range width); scratch on SOW; hard flat EOD/session end.

**Position sizing.**

0.4% initial, +0.2% SOS add; no adds beyond range width extension.

**Risk limits.**

Range-quality gate hard; sloping-range ban; daily stop cap 2; crypto sleeve uses funding-aware sizing (halve into high funding).

**Cost model & capacity.**

Futures ticks + commission; crypto perps add funding + wider spread stress; 70% limit-fill haircut.

**Parameters to validate (plateau, not peak):** Poke {0.05–0.15, 0.10–0.30, 0.20–0.40 ATRm}; reclaim {1, 2, 3 bars}; range bars {15, 20, 30}; SOS vol {1.25, 1.5, 2.0}x.

## 6. Failure modes & regime dependence

Re-accumulation ranges (spring fades the continuation); crypto funding cascades through range edges; thin-session fake ranges with no composite behind them.

## 7. Validation protocol

**Status: no local backtest exists yet.** This library contains zero proprietary results; everything above is literature.

- **Data:** Tick/footprint 24+ months per venue; range rules frozen; crypto funding history; cost stress 2–3x.
- **Splits:** chronological train / validation / test; no random k-fold. Walk-forward re-fit anchored annually.
- **Cost/slippage model:** commission + 1–2 ticks slippage per side (futures) or $0.003–$0.005/share all-in (equities); limit-target fills haircut to 70% touch-fill; stress at 2x and 3x costs.
- **Pitfalls:** look-ahead in same-bar high/low triggers (assume stop-first fills); survivorship in equity sleeves (point-in-time universe); session-time alignment (RTH vs ETH); event-day selection bias (flag, never drop).
- **Robustness:** plateau heatmaps; bootstrap CIs; placebo direction test (must be ~zero); VIX-quintile and yearly sub-samples; best-year removal test.
- **Acceptance criteria:** OOS PF >= 1.15 net of 2x costs; per-trade t >= 2; OOS Sharpe >= 0.8; max DD <= 2x in-sample; positive in >= 60% of years.

## 8. Sources read (annotated)

1. **Wyckoff Analytics education.** https://www.wyckoffanalytics.com — schematics, springs/upthrusts, SOS/SOW. Educational; illustrative examples.
2. **Kyle (1985) on informed flow / Hasbrouck microstructure.** Journal of Finance surveys — impact/absorption mechanism. Known via secondary citation.
3. **Dalton *Mind Over Markets* / Market Profile single prints.** Book-level knowledge — unfinished-auction revisit premise. Practitioner literature.

## 9. Further reading

- Jigsaw/ATAS footprint spring case libraries.
- Steidlmayer/Dalton auction-market texts.
- Crypto footprint adaptations (perp-specific absorption).
