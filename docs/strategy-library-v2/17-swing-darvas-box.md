# 17. Darvas Box Breakout — Twist: DARVAS-V

> **Library:** Sigmatiq Strategy Library V2 | **Bucket:** Swing (1–10d) | **Style:** Breakout / box
> **Instruments:** Growth equities, momentum ETFs | **Typical holding period:** 5–30 days | **Complexity (1–5):** 2 | **Evidence grade (A–C):** C+
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise.

## 1. Origin & lineage

**Nicolas Darvas (1956–59).** *How I Made $2,000,000 in the Stock Market*: the Ballroom-dancer-turned-trader boxed consolidations (high/low bounds) and bought breaks into new boxes with rising volume, trailing box-lows as stops — while traveling the world on telegrams. Lineage: Livermore pivotal points → Darvas boxes → O'Neil cup/base → Minervini VCP (same object, modern volatility lens).

## 2. The original rules (as published)

- **Box:** consolidation high/low bounds; buy the break above box top on increased volume.
- **Stop:** below box top (new support) or box low; raise box as new boxes form (trailing box system).
- **Selection (Darvas):** earnings/growth stories, new highs, increasing volume; ignore tips and news noise.
- **What is NOT rigorous:** box-drawing rules (how many touches, timeframe) are eyeballed; volume-confirmation thresholds unstated.

## 3. Why it works — mechanism & evidence

**Mechanism.** Accumulation under resistance: overhead supply absorbs over weeks; the break marks supply exhaustion; box-low stops define the invalidation where the thesis (accumulation) is wrong. Trend + attention compounding does the rest.

**Supporting evidence (all attributed, none ours):**

- Darvas reported $2M 1957–59 (trader-reported; era markets, unaudited by modern standards — weight as narrative, not statistics).
- Box/breakout momentum family evidence (O'Neil/Minervini practitioner records; Jegadeesh–Titman 6–12M momentum academically) supports the slower cousins.
- Practitioner box-breakout screens show the pattern persists in growth leaders (illustrative).

**Contradictory / decay evidence:**

- Box-drawing subjectivity makes backtests irreproducible; results swing with box-definition choices.
- False-breakout rate on boxes is high in range-bound markets (the documented bleed).
- Darvas-era telegram-delay markets differ structurally from today's algo-breakout-front-running.

**Synthesis.** Darvas is the simplest valid breakout prototype: its value is the trailing-box risk system, not box-picking genius. Needs frozen box rules, volume gating, and a failed-break abort.

## 4. The twist: DARVAS-V

1. **Frozen box (targets eyeball drift):** box = 15–40 day consolidation, width 8–25%, >= 2 touches each side, volume contracting 20%+ into the box.
2. **Volume-confirmed break (targets false breaks):** break-day volume >= 1.5x 50-day average + close in top 20% of range.
3. **Failed-break abort (targets hope-holds):** close back inside box within 3 days = exit all (no second chance).
4. **Box-trail Risk system (targets giveback):** stop = box-top (tight) after +5%, then prior-box low; never wider than 8% from entry.
5. **Market-regime gate (targets bear-market boxes):** no new boxes when SPY < 200-day SMA or VIX > 30 (breakouts fail under distribution).

## 5. Full specification of the twist variant

**Universe.** US growth equities $1B+, price > $15, ADV > $5M; IBD-style earnings/RS pre-screen optional.

**Data requirements.** Daily bars + volume/RVOL, box detector, SMA200, VIX, earnings calendar.

**Signal definitions (formulas).**

- Box geometry + touches as above; break = close above box top + volume + range-position gates.
- Regime: SPY position vs SMA200 + VIX level.

**Entries.**

Buy break close (or next open); stop at box-top then trailed boxes; one box per name; max 6 concurrent.

**Exits.**

Box-trail (systematic); abort on 3-day close-back-inside; partial 1/3 at +20%; hard 8% stop always.

**Position sizing.**

1% risk; regime-off = no new entries (existing trailed).

**Risk limits.**

Earnings within 5d veto; sector concentration max 3 per sector; abort rule hard (no overrides).

**Cost model & capacity.**

5–10 bps/side; capacity moderate (growth mid-caps).

**Parameters to validate (plateau, not peak):** Box {10–30, 15–40, 20–50}d; width {5–20%, 8–25%, 10–30%}; volume {1.25, 1.5, 2.0}x; abort {2, 3, 5}d.

## 6. Failure modes & regime dependence

Range-bound false-break clusters; bear-market box season; offering-after-break (growth classic); volume-fake breaks on low-float names.

## 7. Validation protocol

**Status: no local backtest exists yet.** This library contains zero proprietary results; everything above is literature.

- **Data:** Daily 2000–present point-in-time incl. delisted; earnings dates; splits/dividends.
- **Splits:** chronological train / validation / test; no random k-fold. Purged/embargoed where labels overlap; walk-forward anchored.
- **Cost/slippage model:** $0.003–$0.005/share all-in or 5–10 bps per side; borrow costs on shorts; limit-fill haircut 70% on touches; stress 2x/3x.
- **Pitfalls:** survivorship (point-in-time universe incl. delisted); look-ahead in fundamentals/earnings timestamps; same-bar ambiguity (stop-first); corporate actions (splits/dividends adjusted with point-in-time factors).
- **Robustness:** plateau heatmaps; bootstrap CIs; placebo (randomized entries, same exits — must be ~zero); yearly + VIX-quintile sub-samples; best-year removal.
- **Acceptance criteria:** OOS Sharpe >= 0.8 net of 2x costs; PF >= 1.2; per-trade t >= 2; max DD <= 2x in-sample; positive in >= 60% of years.

## 8. Sources read (annotated)

1. **Darvas, *How I Made $2,000,000 in the Stock Market* (1960).** Publisher pages (e.g. https://www.harpercollins.com) — box rules + narrative. Book-level knowledge.
2. **O'Neil base/breakout literature (cousin).** See doc 21 sources — same object, slower.
3. **Jegadeesh & Titman momentum (family evidence).** Known via secondary citation — 6–12M continuation supports breakout family.

## 9. Further reading

- Livermore pivotal-point originals (ancestor).
- Minervini VCP (volatility-contracted cousin).
- IBD box/base pattern catalogs.
