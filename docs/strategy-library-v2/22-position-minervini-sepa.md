# 22. Minervini SEPA Growth Momentum — Twist: SEPA-V

> **Library:** Sigmatiq Strategy Library V2 | **Bucket:** Position (weeks–months) | **Style:** Growth momentum / VCP
> **Instruments:** US growth equities | **Typical holding period:** 1–4 months | **Complexity (1–5):** 4 | **Evidence grade (A–C):** B
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise.

## 1. Origin & lineage

**Mark Minervini.** 1997 US Investing Champion (+155% reported), *Trade Like a Stock Market Wizard* (2013) + *Think & Trade Like a Champion* (2016): SEPA — Specific Entry Point Analysis: Stage-2 uptrends + Volatility Contraction Pattern (VCP) + RS leaders + earnings acceleration, with ATR-based risk staging. Lineage: O'Neil bases → Minervini VCP (volatility-contracted cousin) → Kell/Bonde daily execution. Minervini publishes audited-style contest returns and ongoing performance commentary (trader-reported).

## 2. The original rules (as published)

- **Trend template:** price > SMA50/150/200, SMA50 > SMA150 > SMA200, 52-week-high proximity, RS top decile.
- **VCP:** 2–4 contractions, each pullback shallower, volume drying (-30–50%), pivot at contraction extreme.
- **Entry:** VCP pivot break + volume; stop below pivot/false-break low (typically 5–10%).
- **Risk staging:** small starters, adds on follow-through, cut losers at ~5–7%, winners trailed via moving averages.
- **What is NOT fixed:** contraction counting and dryness thresholds are eyeballed.

## 3. Why it works — mechanism & evidence

**Mechanism.** Institutional accumulation with declining supply: each contraction shakes weak holders while strong bids absorb; drying volume marks supply exhaustion; the pivot break re-recruits momentum algos + human trend funds — a slower EP-continuation with fundamentals underneath.

**Supporting evidence (all attributed, none ours):**

- Minervini contest + published track snapshots (trader-reported; scrutinized publicly, not independently audited — weight as strong practitioner claim).
- VCP/basing practitioner studies show contraction-then-expansion sequencing in leaders (illustrative).
- Academic cousins: volatility-contraction precedes directional expansion (Crabel NR4/ID family); RS-leader persistence (George–Hwang).

**Contradictory / decay evidence:**

- VCP identification is subjective; backtest VCP definitions rarely match live eyeballing (reproducibility gap).
- Stage-2 template fails in rotations (growth-to-value) where leaders become laggards for quarters.
- Small-starter/adds ladder underperforms buy-and-hold leaders in straight-up tapes (activity cost).

**Synthesis.** SEPA is O'Neil with a volatility lens: its codable core is the Stage-2 template + frozen VCP geometry + staged risk. Value is selectivity (few true VCPs) + fast cuts.

## 4. The twist: SEPA-V

1. **Frozen VCP (targets eyeball drift):** 2–4 contractions over 4–12 weeks, each pullback <= 0.7x prior depth, volume -30% trough-to-trough, pivot = last contraction high.
2. **Stage-2 gate (targets laggard VCPs):** all five trend-template conditions required (no partial credit).
3. **Contraction-count sizing (targets uniform bets):** 2-contraction 0.5x, 3-contraction 1.0x, 4-contraction 1.25x (tighter = bigger, capped).
4. **Cheat-vs-pivot fork (targets late entries):** entries inside the final contraction ('cheat') at half size allowed; full size only on pivot break + volume 1.5x.
5. **Stage-break kill (targets round-trips):** exit all on close below SMA50 after entry (stage violation), not just pattern-low stops.

## 5. Full specification of the twist variant

**Universe.** US growth $1B+, RS >= 90, price > $15, ADV > $5M; earnings accel preferred (Cousin of 21).

**Data requirements.** Daily/weekly bars, SMA50/150/200, RS ranker, VCP detector, volume normals, fundamentals optional overlay.

**Signal definitions (formulas).**

- Stage-2 booleans; VCP geometry + dryness as above; pivot break + volume gate.

**Entries.**

Cheat half inside final contraction; full on pivot break + 1.5x vol; stop pivot-low (cap 8%).

**Exits.**

SMA50 stage-break full exit; 10-week trail for runners; partial 1/3 at +30%; failed-pivot (close back inside) = immediate exit.

**Position sizing.**

0.75–1.25% by contraction count; max 8 concurrent; cheat legs half.

**Risk limits.**

Stage gate hard; earnings veto 5d; sector max 3; no adds below entry.

**Cost model & capacity.**

5–10 bps/side; capacity moderate-large.

**Parameters to validate (plateau, not peak):** Contractions {2, 3, 4}; dryness {20%, 30%, 40%}; pivot vol {1.25, 1.5, 2.0}x; stop cap {6%, 8%, 10%}.

## 6. Failure modes & regime dependence

Rotation regimes (Stage-2 universe inverts); loose-VCP late-stage bases; offering-after-pivot; cheat entries in chop (death by small cuts).

## 7. Validation protocol

**Status: no local backtest exists yet.** This library contains zero proprietary results; everything above is literature.

- **Data:** Daily/weekly 2000–present point-in-time incl. delisted; RS reproducible; earnings dates.
- **Splits:** chronological train / validation / test across full market cycles (must include a bear); no random k-fold; walk-forward anchored.
- **Cost/slippage model:** 5–15 bps/side + borrow on shorts; dividends/splits point-in-time; stress 2x/3x.
- **Pitfalls:** survivorship (delisted included); look-ahead in fundamentals (report-date, not period-end); same-bar ambiguity (conservative fills); corporate actions.
- **Robustness:** plateau heatmaps; bootstrap CIs; placebo (random entries, same exits ~zero); yearly + drawdown-regime sub-samples; best-year removal.
- **Acceptance criteria:** OOS CAGR > benchmark with lower max DD (trend) or Sharpe >= 1.0 (drift); per-trade t >= 2; positive in >= 60% of years; survives 2008/2020/2022 sub-samples.

## 8. Sources read (annotated)

1. **Minervini, *Trade Like a Stock Market Wizard* (2013).** Publisher: https://www.minervini.com — SEPA/VCP + risk staging. Book-level knowledge.
2. **Minervini, *Think & Trade Like a Champion* (2016).** Same — position management detail. Book-level knowledge.
3. **O'Neil base literature (ancestor).** See doc 21 — base/VCP mapping.

## 9. Further reading

- US Investing Championship Minervini-year breakdowns.
- VCP contraction-count studies (practitioner).
- Stage-analysis (Weinstein) originals.
