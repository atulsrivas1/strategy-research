# 21. O'Neil CANSLIM Growth — Twist: CANSLIM-F

> **Library:** Sigmatiq Strategy Library V2 | **Bucket:** Position (weeks–months) | **Style:** Growth momentum + fundamentals
> **Instruments:** US growth equities | **Typical holding period:** 1–6 months | **Complexity (1–5):** 3 | **Evidence grade (A–C):** B
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise.

## 1. Origin & lineage

**William O'Neil (1933–2023).** *How to Make Money in Stocks* (1988; 4th ed 2009) + *Investor's Business Daily* (founded 1984): CANSLIM — Current earnings acceleration, Annual growth, New product/management/high, Supply/demand (volume + float), Leader/laggard, Institutional sponsorship, Market direction. O'Neil reported backtests of historic winners' shared traits (author's study, 1953–2008 examples). IBD 50 / Leaderboard is the live implementation.

## 2. The original rules (as published)

- **C:** quarterly EPS growth accelerating, >= 25% typical.
- **A:** annual earnings >= 25% 3–5 years.
- **N:** new product/management/52-week high.
- **S:** volume demand + tighter float; big up-volume on breakouts.
- **L:** relative-strength leaders (top decile), never laggards.
- **I:** rising institutional ownership (13F trend).
- **M:** market direction (follow-through day; no buys in corrections) — O'Neil called M half the system.
- **Sell:** -8% hard stop; round-trip/negative-reversal sells; climax-run exits.

## 3. Why it works — mechanism & evidence

**Mechanism.** Fundamental-acceleration + institutional-accumulation + market-timing compounding: earnings surprises re-rate leaders; volume confirms institutional sponsorship; the M-gate keeps the system out of bear-market growth bleed where bases systematically fail.

**Supporting evidence (all attributed, none ours):**

- O'Neil's historic-winner studies (author's sample; illustrative, selection-heavy — weight as pattern catalog, not RCT).
- IBD 50/Leaderboard published performance vs SPY in bull years (firm-published; fee/cost treatment varies — read skeptically).
- Academic cousins: earnings-momentum (Bernard–Thomas), RS leadership (George–Hwang), institutional-herding persistence.

**Contradictory / decay evidence:**

- CANSLIM letters are qualitative screens, not a coded system; replication Sharpe varies wildly with implementation choices.
- Growth-leader drawdowns in bears (-50%+ cohorts in 2000/2008/2022) overwhelm the -8% single-name story at portfolio level.
- I-following (13F) lags quarters; S-float screens miss offerings that print right after breakouts.

**Synthesis.** CANSLIM is a quality-growth screen plus a market-timing gate: its testable core is RS-leader + earnings-acceleration + follow-through-gated entries with hard stops. Our twist freezes each letter into thresholds.

## 4. The twist: CANSLIM-F

1. **Frozen letters (targets qualitative drift):** C: EPS accel 2 quarters >= 25%; A: 3-yr CAGR >= 25%; N: 52-week high within 10% or new-product tag; S: break vol >= 1.5x + float <$20B effective; L: RS >= 90; I: funds-own YoY up; M: follow-through gate.
2. **Follow-through gate (targets bear-market buys):** entries only after SPY follow-through day (Day 4–7 rally + volume) and SPY > SMA50; otherwise watchlist-only.
3. **Base-count cap (targets late bases):** first- or second-stage bases only (O'Neil base counting); third+ bases half size with 5% stop.
4. **-8% hard + round-trip rule (targets hope-holds):** -8% stop hard; round-trip (give back 2/3 of max gain) exits half.
5. **Sponsorship-quality veto (targets crowded laggards):** skip if funds-own flat/down 2 quarters or management sells > 20% of holdings into the base.

## 5. Full specification of the twist variant

**Universe.** US equities $1B+, price > $15, ADV > $5M; exclude biotech-binary pre-revenue and China ADRs (separate specs).

**Data requirements.** Quarterly/annual fundamentals point-in-time, RS ranker, 13F aggregates, base detector, follow-through calendar, insider filings.

**Signal definitions (formulas).**

- Letter thresholds as above; base = 5–15 week cup/flat 10–30% deep with handle option; follow-through = SPY rally day 4–7 + volume gate.

**Entries.**

Base-break close/next open with volume gate in M-pass; late bases half; stop -8% (late -5%).

**Exits.**

-8% hard; round-trip half; climax (+100% run or 3-week parabolic) partials; 10-week-line trail for leaders.

**Position sizing.**

1% risk; max 10 concurrent; late bases 0.5%; M-fail = no new entries.

**Risk limits.**

M-gate hard; earnings within 5d veto on new entries; sector max 3; round-trip rule automated (no overrides).

**Cost model & capacity.**

5–10 bps/side; capacity moderate-large (liquid growth).

**Parameters to validate (plateau, not peak):** EPS {20%, 25%, 30%}; RS {80, 90, 95}; base {4–12, 5–15, 7–20}w; stop {5%, 8%, 10%}.

## 6. Failure modes & regime dependence

Bear-market growth cohorts (all letters pass, market kills them — hence M); offering-after-break; biotech-binary N-traps; third-base blow-offs.

## 7. Validation protocol

**Status: no local backtest exists yet.** This library contains zero proprietary results; everything above is literature.

- **Data:** Fundamentals point-in-time 2000–present (report dates) + daily bars incl. delisted; 13F vintages; follow-through history.
- **Splits:** chronological train / validation / test across full market cycles (must include a bear); no random k-fold; walk-forward anchored.
- **Cost/slippage model:** 5–15 bps/side + borrow on shorts; dividends/splits point-in-time; stress 2x/3x.
- **Pitfalls:** survivorship (delisted included); look-ahead in fundamentals (report-date, not period-end); same-bar ambiguity (conservative fills); corporate actions.
- **Robustness:** plateau heatmaps; bootstrap CIs; placebo (random entries, same exits ~zero); yearly + drawdown-regime sub-samples; best-year removal.
- **Acceptance criteria:** OOS CAGR > benchmark with lower max DD (trend) or Sharpe >= 1.0 (drift); per-trade t >= 2; positive in >= 60% of years; survives 2008/2020/2022 sub-samples.

## 8. Sources read (annotated)

1. **O'Neil, *How to Make Money in Stocks* (4th ed 2009).** Publisher: https://www.investors.com — CANSLIM letters + sell rules. Book-level knowledge.
2. **IBD methodology pages.** https://www.investors.com — RS, base, follow-through definitions. Firm-authored.
3. **Bernard & Thomas / earnings-momentum (cousin C).** Known via secondary citation — acceleration persistence.

## 9. Further reading

- IBD Big Picture / follow-through archives.
- Cup-with-handle pattern studies.
- 13F-crowding vs sponsorship-quality notes.
