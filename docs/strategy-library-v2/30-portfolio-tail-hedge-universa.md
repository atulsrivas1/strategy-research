# 30. Tail Hedge / Universa-Style Convexity — Twist: TAIL-B

> **Library:** Sigmatiq Strategy Library V2 | **Bucket:** Portfolio / Macro | **Style:** Convexity / tail
> **Instruments:** SPX puts, VIX calls, long-duration Treasuries (barbell) | **Typical holding period:** Permanent hedge sleeve (years) | **Complexity (1–5):** 4 | **Evidence grade (A–C):** B
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise.

## 1. Origin & lineage

**Taleb → Spitznagel/Universa lineage.** Taleb *Black Swan*/*Antifragile* (insurance-asymmetric convexity) → Universa tail-hedge funds (reported 2008/2020 explosive months; firm letters) → academic: Bhansali active tail management; CBOE SKEW/PPUT benchmarks. Practitioner barbell: 90%+ productive risk + small permanent convexity sleeve monetized into dislocations (Spitznagel's 'monetize the hedge' rule).

## 2. The original rules (as published)

- **Universa rendering (from firm letters/interviews):** small (~1–3%/year spend) far-OTM put/VIX-convexity sleeve, rolled systematically; monetize spikes into dislocated risk assets (the barbell rebalance).
- **Bhansali:** active tail shape management (not buy-and-hold puts) keyed to skew/curve.
- **Retail mistranslation:** buying weeklies into every fear spike (negative expectancy without monetization rules).
- **What is NOT public:** exact strike/tenor ladders, monetization triggers, reinvestment splits.

## 3. Why it works — mechanism & evidence

**Mechanism.** Negative correlation in the left tail + convexity: far-OTM protection is systematically under-held (career/fee incentives punish drag); during jumps, convexity reprices explosively while linear hedges gap; the barbell converts the spike into cheap risk-asset accumulation — path-dependent put, not buy-and-hold insurance.

**Supporting evidence (all attributed, none ours):**

- Universa reported 2008/2020 spike months (firm letters; vehicle/fee specifics undisclosed — read as existence proof, not a return promise).
- CBOE tail-benchmarks (VXTH/SKEW-family) show convexity repricing in stress (index fact).
- Academic tail-risk literature documents left-tail option cheapness vs actuarial in select regimes (sample-dependent).

**Contradictory / decay evidence:**

- Permanent tail drag (~1–3%/year) compounds brutally in calm decades; most tail funds underperform cash for years between events.
- Monetization timing dominates results; buy-and-hold far-OTM without monetize-and-redeploy rules is documented negative expectancy.
- Counterparty/liquidity in true tails (wings gap, dealers pull) impairs textbook hedge math exactly when needed.

**Synthesis.** Tail hedging is a barbell discipline (spend + monetize + redeploy), not a product: size the drag explicitly, ladder the convexity, pre-commit monetization — or do not run it.

## 4. The twist: TAIL-B

1. **Laddered convexity (targets single-tenor expiry):** 3/6/12-month far-OTM puts + VIX-call wings laddered; never one expiry.
2. **Skew-timed spend (targets rich-premium drag):** spend 1% base, up to 3% when skew is cheap (< 30th percentile); cut to 0.5% when skew is rich (> 80th).
3. **Monetization ladder (targets round-trips):** sell 1/3 at +3x, 1/3 at +5x, trail 1/3; proceeds pre-split 50% redeploy to risk assets / 50% to next hedge ladder (no discretion).
4. **Barbell accounting (targets drag denial):** report hedge sleeve separately with explicit drag budget; core 97%+ runs its own mandate (no style drift to 'pay for the hedge').
5. **Liquidity governor (targets gap-illiquidity):** prefer listed SPX/VIX over OTC exotics; assume 2x spread stress in sizing (fills will be worse than marks).

## 5. Full specification of the twist variant

**Universe.** SPX puts, VIX calls/futures wings, long-duration Treasury barbell leg; listed only.

**Data requirements.** Options skew/curve surface, VIX futures curve, spike/monetization log, rebalance calendar.

**Signal definitions (formulas).**

- Skew percentile for spend rate; convexity ladder tenors; monetization multiples; redeploy split.

**Entries.**

Quarterly ladder rolls at budgeted spend; skew-timing adjusts the spend rate only (never the ladder structure).

**Exits.**

Monetization ladder on spikes; proceeds split mechanically; ladder rebuilt from the hedge half.

**Position sizing.**

1–3%/year drag budget (pre-committed); convexity notional sized by stress-spread assumption.

**Risk limits.**

Drag budget hard (no doubling down on cheap skew beyond 3%); listed-only; dealer-failure diversification (multi-clearer).

**Cost model & capacity.**

Option premia as budgeted drag + roll spreads; stress-spread 2x modeled; capacity large (index options).

**Parameters to validate (plateau, not peak):** Spend {0.5%, 1%, 2%, 3%}; strikes {5, 10, 15–20 delta}; monetize {2x/4x, 3x/5x}; split {50/50, 70/30}.

## 6. Failure modes & regime dependence

Decade-long calm (drag compounds); spike-then-melt (monetize too late); wing-liquidity gaps (marks not fills); regime where skew never cheapens (persistent bid).

## 7. Validation protocol

**Status: no local backtest exists yet.** This library contains zero proprietary results; everything above is literature.

- **Data:** Options/VIX history 2005–present; skew archives; spike episodes 2008/2010/2011/2015/2018/2020/2022.
- **Splits:** chronological across cycles (must include 2008, 2020, 2022); no random k-fold; walk-forward anchored.
- **Cost/slippage model:** ETF expense + 2–10 bps/rebalance; options spreads + borrow where used; futures roll costs; stress 2x/3x.
- **Pitfalls:** look-ahead in index/constituent vintages; survivorship; same-bar ambiguity on rotation days; corporate actions; options expiry/pin.
- **Robustness:** plateau heatmaps; bootstrap CIs; placebo allocations (~zero edge); yearly + VIX/inflation-regime sub-samples; best-year removal.
- **Acceptance criteria:** OOS risk-adjusted dominance vs stated benchmark net of 2x costs; max DD within 1.2x of in-sample; positive in >= 60% of 3-year windows.

## 8. Sources read (annotated)

1. **Taleb, *The Black Swan* / *Antifragile*.** Publisher pages — convexity-barbell philosophy. Book-level knowledge.
2. **Universa firm letters/interviews (Spitznagel).** Search "Universa tail hedge letter" — spend/monetize/barbell framing. Firm-authored; existence-proof weight only.
3. **Bhansali on active tail management.** Search "Bhansali tail risk" — shape-management overlay. Known via secondary citation.

## 9. Further reading

- CBOE SKEW/VXTH benchmark docs.
- 2008/2020 tail-fund performance debates.
- Dealer-liquidity-in-stress papers.
