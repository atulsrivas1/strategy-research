# 36. Permanent Portfolio + Index Tilt — Twist: PERM-T

> **Library:** Sigmatiq Strategy Library V2 | **Bucket:** Long-term investing | **Style:** Strategic allocation
> **Instruments:** Index funds: stocks, bonds, gold, bills + factor tilts | **Typical holding period:** Decades (annual rebalance) | **Complexity (1–5):** 1 | **Evidence grade (A–C):** B
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise.

## 1. Origin & lineage

**Harry Browne (1981) → Bogle index bridge.** Browne *Fail-Safe Investing*: 25% stocks / 25% long Treasuries / 25% gold / 25% cash — survive any regime (prosperity/inflation/recession/deflation). Bogle (1975/Vanguard) supplies the implementation: cap-weighted index at near-zero cost. Bernstein/Swedroe 'tilt' literature adds small/value/profitability overweights. Our twist is Browne's survival frame + Bogle's cost engine + budgeted tilts.

## 2. The original rules (as published)

- **Browne:** 25/25/25/25 across stocks/long-bonds/gold/cash; rebalance annually; no forecasts.
- **Bogle:** own the market (cap-weighted total stock/bond index), minimize cost, stay the course for decades.
- **Tilt literature:** overweight small/value/profitability within the equity quarter for expected excess (Bernstein/Swedsoe/Fama-French practitioner bridge).
- **What varies:** gold share (0–25% debate), bond duration, tilt size.

## 3. Why it works — mechanism & evidence

**Mechanism.** Regime survival + cost minimization + rebalancing premium: one sleeve always offsets the prevailing shock (stocks in prosperity, gold in inflation, bonds in deflation/recession, cash in tight-money); index implementation removes fee/active drag; small factor tilts add expected excess without breaking the survival frame.

**Supporting evidence (all attributed, none ours):**

- Permanent-portfolio reconstructions show decades-long lower drawdowns vs 100% equity with moderate return give-up (author/replicator computations; period-sensitive).
- Bogle cost-matters arithmetic (fee drag compounding) is uncontroversial and large over decades.
- Factor-tilt sleeve evidence (Fama–French; see doc 29) supports modest expected excess for the tilted portion.

**Contradictory / decay evidence:**

- Gold's long-run real return ≈ zero with large drawdowns; 25% gold is a heavy insurance premium critics call dead weight.
- 2022 hit three sleeves at once (stocks/bonds/gold all down — cash alone held); 'any regime' framing overpromises.
- Cap-weighted equity quarter concentrates mega-cap/tech by construction (the Bogle concentration critics flag).

**Synthesis.** The permanent frame is the lowest-maintenance survival allocation; its honest costs are gold drag and return give-up vs equity. Our twist keeps the frame, budgets the tilts, and hard-codes rebalance so behavior, not forecasting, does the work.

## 4. The twist: PERM-T

1. **Core-40 tilt budget (targets dead-weight drift):** 60% of equity quarter in total-market index, 40% in small/value/profitability tilt funds (rarely re-argued).
2. **Duration-split bonds (targets long-bond cliffs):** bond quarter as intermediate/long barbell (not all long) — 2022-cliff dampener.
3. **Gold-band rebalancing (targets overtrading):** rebalance annually or on 10pp drift bands (whichever first); gold never traded tactically.
4. **Glidepath by age (targets static-risk mismatch):** under-40: stocks 35%/bonds 15% (tilt up); over-60: mirror (bonds 35%/stocks 15%); gold/cash 25/25 constant.
5. **Written investment policy (targets abandonment):** one-page IPS signed pre-launch (contribution rate, rebalance rule, no-forecast pledge); any change needs 90-day written wait.

## 5. Full specification of the twist variant

**Universe.** Total-stock/total-bond index funds, gold trust, T-bills; tilt funds (small/value/profitability) for the 40%.

**Data requirements.** Index fund NAVs + expense ratios, rebalance calendar, IPS document.

**Signal definitions (formulas).**

- Drift bands (10pp) + annual date + glidepath age bracket; no market signals (by design).

**Entries (accumulation).**

Contributions to most-underweight sleeve (mechanical value-averaging of attention); tilt funds on same rule.

**Exits (trim/sell discipline).**

Rebalance trims only (no tactical exits); glidepath shifts at decade birthdays (phased over 4 quarters).

**Position sizing.**

25/25/25/25 baseline ± glidepath; tilt 40% of equity quarter; cash never below 20% (emergency integrity).

**Risk limits.**

IPS hard; no leverage; no tactical overrides (90-day rule); fund-closure fallback list maintained.

**Cost model & capacity.**

Weighted expense < 0.10% target; turnover ~10%/year; taxes: rebalance in tax-advantaged first (disclosed).

**Parameters to validate (plateau, not peak):** Gold {10%, 15%, 25%}; tilt {0%, 40%, 60%}; bands {5pp, 10pp}; rebalance {annual, band-triggered}.

## 6. Failure modes & regime dependence

Multi-sleeve down years (2022 family — cash-only offsets); decades-long equity underperformance vs 100% stocks (the known give-up); gold's multi-decade flat stretches.

## 7. Validation protocol

**Status: no local backtest exists yet.** This library contains zero proprietary results; everything above is literature.

- **Data:** Index/fund total-return 1970–present (gold from 1971 float); expense histories; rebalance simulation with bands.
- **Splits:** chronological with point-in-time fundamentals (report dates, restatements vintaged); no random k-fold; must include full drawdown cycles.
- **Cost/slippage model:** 5–10 bps/side; taxes modeled (turnover matters more here than spreads); stress 2x.
- **Pitfalls:** survivorship (delisted included); look-ahead (period-end vs report-date); restatement handling (as-first-reported); corporate actions; index-constituent vintage honesty.
- **Robustness:** plateau checks; bootstrap CIs; placebo screens (~zero); yearly + valuation-regime sub-samples; best-decade removal.
- **Acceptance criteria:** OOS excess vs stated benchmark net of costs/taxes with lower or equal max DD; hit-rate on thesis milestones tracked; 10-year positive excess in >= 70% of vintages.

## 8. Sources read (annotated)

1. **Browne, *Fail-Safe Investing* (1999).** Publisher pages — 25/25/25/25 + regime logic. Book-level knowledge.
2. **Bogle, *Common Sense on Mutual Funds* / Vanguard principles.** https://www.vanguard.com — cost-matters + stay-the-course. Book/site-level knowledge.
3. **Bernstein/Swedroe tilt literature.** Publisher pages — small/value tilt bridge. Book-level knowledge.

## 9. Further reading

- Permanent-portfolio 2022 post-mortems.
- Golden-butterfly variant notes.
- IPS/behavioral-finance implementation guides.
