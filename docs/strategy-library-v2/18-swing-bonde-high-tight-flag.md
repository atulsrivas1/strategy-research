# 18. Bonde High-Tight-Flag Momentum — Twist: HTF-Q

> **Library:** Sigmatiq Strategy Library V2 | **Bucket:** Swing (1–10d) | **Style:** Momentum / pattern
> **Instruments:** High-growth small/mid caps, IPO leaders | **Typical holding period:** 3–15 days | **Complexity (1–5):** 3 | **Evidence grade (A–C):** C+
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise.

## 1. Origin & lineage

**Pradeep Bonde lineage.** Pennysleever/Tiny Titan / Pradeep Bonde swing-trading education + Oliver Kell (US Investing Champion) high-tight-flag (HTF) growth-momentum: tight sideways flags after 100%+ runs on the weekly, bought on daily-flag breaks with volume. Lineage: Darvas boxes (tight cousin) → O'Neil high-tight-flags → Bonde/Kell daily execution. Our spec freezes the notoriously eyeballed 'tightness'.

## 2. The original rules (as published)

- **Setup (Kell/Bonde rendering):** 100%+ run in <= 8 weeks, then 3–5 week sideways flag declining < 10–20%, volume drying.
- **Trigger:** daily break above flag high on volume; stop at flag low (~7–10% below).
- **Exit:** trailing 10-day / prior-flag-low; partials into extensions; ride leaders, cut laggards fast.
- **What is NOT fixed:** run-measurement window, tightness %, volume-dry threshold — all feel.

## 3. Why it works — mechanism & evidence

**Mechanism.** Power + digestion: a parabolic institutional-demand run pauses as weak hands take profits into strong-hand bids; tightness signals supply exhaustion; the break re-recruits momentum algos + human chase before the next leg — a slower EP-continuation.

**Supporting evidence (all attributed, none ours):**

- Kell contest-year returns (trader-reported, unaudited) + Bonde published trade reviews (illustrative).
- Momentum-persistence literature (Jegadeesh–Titman; 52-week-high, George–Hwang) supports continuation in winners (academic, broader rule).
- Practitioner HTF compilations show the pattern in historic leaders (-modal examples; survivorship-heavy).

**Contradictory / decay evidence:**

- HTFs are rare (a few per year market-wide); most 'flags' bought are loose late-stage bases that fail.
- Late-cycle HTFs precede blow-off tops; buying the break is buying near the high (left-tail event risk).
- Tightness eyeballing overfits; published examples are selected winners.

**Synthesis.** HTF is a valid but ultra-selective leader-continuation: trade a handful per year with small risk and fast failure exits, or do not trade it at all.

## 4. The twist: HTF-Q

1. **Frozen tightness (targets eyeball drift):** run >= 90% in <= 40 sessions; flag 10–25 sessions, depth <= 15%, weekly closes within 10% band, volume -30% vs run.
2. **Leader-only (targets laggard flags):** RS rating >= 90 (52-week-high proximity top decile) + price > $10 + ADV > $3M.
3. **Break-day gates (targets loose breaks):** volume >= 1.5x + close top 25% + market-regime pass (SPY > SMA50).
4. **Two-strike rule (targets repeated failures):** after two failed HTF breaks market-wide in a month, stand down 30 days (late-cycle flag season).
5. **Blow-off governor (targets tops):** half off at +25% from break; trail remainder at 10-day low; never add above +30%.

## 5. Full specification of the twist variant

**Universe.** US growth $500M+, RS top-decile, no earnings within 5d of entry.

**Data requirements.** Daily/weekly bars, RS ranker, volume normals, SMA50/200, market-regime feed.

**Signal definitions (formulas).**

- Run/flag geometry + volume-dry as above; break = close above flag high + gates.
- Two-strike counter market-wide; blow-off extension tracker.

**Entries.**

Break close/next open; stop flag low (cap 10%); one HTF per name per run.

**Exits.**

10-day-low trail; half at +25%; full exit on close below 10-day after profit or 10-day time-stop flat.

**Position sizing.**

0.75% risk (rare, fat-tail); max 3 concurrent HTFs.

**Risk limits.**

Late-cycle stand-down rule hard; earnings veto; no adds into extensions.

**Cost model & capacity.**

5–10 bps/side; capacity small (leaders scale, but flags are thin).

**Parameters to validate (plateau, not peak):** Run {80%, 90%, 100%}; flag {10–20, 10–25, 15–30}d; depth {10%, 15%, 20%}; volume-dry {20%, 30%, 40%}.

## 6. Failure modes & regime dependence

Late-cycle distribution flags; offering-after-break; market-break HTFs (all leaders fail together); thin-flag fake volume.

## 7. Validation protocol

**Status: no local backtest exists yet.** This library contains zero proprietary results; everything above is literature.

- **Data:** Daily/weekly 2000–present point-in-time; RS history reproducible; earnings; delisted included.
- **Splits:** chronological train / validation / test; no random k-fold. Purged/embargoed where labels overlap; walk-forward anchored.
- **Cost/slippage model:** $0.003–$0.005/share all-in or 5–10 bps per side; borrow costs on shorts; limit-fill haircut 70% on touches; stress 2x/3x.
- **Pitfalls:** survivorship (point-in-time universe incl. delisted); look-ahead in fundamentals/earnings timestamps; same-bar ambiguity (stop-first); corporate actions (splits/dividends adjusted with point-in-time factors).
- **Robustness:** plateau heatmaps; bootstrap CIs; placebo (randomized entries, same exits — must be ~zero); yearly + VIX-quintile sub-samples; best-year removal.
- **Acceptance criteria:** OOS Sharpe >= 0.8 net of 2x costs; PF >= 1.2; per-trade t >= 2; max DD <= 2x in-sample; positive in >= 60% of years.

## 8. Sources read (annotated)

1. **Kell/Bonde HTF education (practitioner).** Search "Oliver Kell high tight flag" / "Pradeep Bonde swing trading" — pattern rules. Practitioner-authored; illustrative.
2. **George & Hwang on 52-week-high momentum.** Journal of Finance — proximity predicts continuation. Known via secondary citation.
3. **O'Neil high-tight-flag base (cousin).** See doc 21 — same object in base taxonomy.

## 9. Further reading

- US Investing Championship HTF-year breakdowns.
- IBD high-tight-flag pattern guides.
- IPO-leader flag studies.
