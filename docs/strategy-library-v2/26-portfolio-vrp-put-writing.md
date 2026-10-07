# 26. Volatility Risk Premium Put Writing — Twist: VRP-G2

> **Library:** Sigmatiq Strategy Library V2 | **Bucket:** Portfolio / Macro | **Style:** Volatility carry
> **Instruments:** SPX/SPY options, VIX futures hedge | **Typical holding period:** Weekly to monthly cycles | **Complexity (1–5):** 4 | **Evidence grade (A–C):** A-
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise.

## 1. Origin & lineage

**CBOE PUT lineage.** CBOE PUT BuyWrite indices (PUT, BXM) + academic VRP (Bollerslev–Tauchen–Zhou; Carr–Wu variance risk premium; Israelov–Nielsen put-write timing): systematically short index volatility earns the gap between implied and realized. Practitioner: put-write funds + 1%-OTM SPX put-write literature. Taleb/Universa is the other side (long tails) — our twist holds both: short VRP funded, tail hedge owned.

## 2. The original rules (as published)

- **PUT index:** monthly short 1-ATM SPX put, cash-secured, roll monthly (CBOE methodology).
- **Academic VRP:** short variance when VRP (IV - RV forecast) is high; scale by VRP level (Israelov timing).
- **Practitioner:** 5–10 delta weeklies/montlies, 30–45 DTE, manage at 50% profit or 21 DTE.
- **What kills the naive version:** short-gamma tails (2008/2020) — unhedged put-write drawdowns rival equity.

## 3. Why it works — mechanism & evidence

**Mechanism.** Insurance premium: institutions overpay for downside protection (mandates, career risk, leverage constraints); realized vol undershoots implied on average; the writer harvests the spread — until the insured event arrives, which is why sizing + hedges define the strategy, not the premium alone.

**Supporting evidence (all attributed, none ours):**

- CBOE PUT reports long-run equity-like returns with lower vol/drawdowns vs SPY (index fact; pre-fee, roll-assumed).
- Carr–Wu / Bollerslev et al. document positive variance risk premia across US/European indices (academic core).
- Israelov–Nielsen report VRP-timed put writing improves risk-adjusted capture vs static (authors' sample).

**Contradictory / decay evidence:**

- 2008/2020 put-write drawdowns (-25–35% sleeves) show the tail is equity-like when it matters most.
- Post-2010 VRP compressed vs 1990s–2000s (more sellers, listed-vol competition).
- Weekly-put variants bleed on whipsaw (short gamma, frequent rolls); monthly 30–45 DTE survives better in replications.

**Synthesis.** VRP is a real carry with equity-like left tails: trade it gated (contango + skew), VRP-sized, tail-hedged, with a hard VIX stop — never as naked weeklies for yield.

## 4. The twist: VRP-G2

1. **Contango + skew gates (targets bad-vintage selling):** sell only when VIX futures 1M-2M in contango AND 25-delta put skew below 80th percentile (cheap tails = do not sell naked).
2. **VRP-sized notional (targets fixed-notional blowups):** notional *= clip(VRP_now/VRP_median, 0.25, 1.5); rich premium = bigger, thin = smaller.
3. **Tail-hedge overlay (targets 2008/2020):** spend 10–20% of collected premium on far-OTM puts / VIX-call wings (Universa-lite, always on).
4. **Hard VIX stop (targets hope-holds):** no new writes VIX > 30; existing managed at 2x premium-stop; book halt VIX > 40.
5. **DTE/settlement discipline (targets weekly bleed):** 30–45 DTE monthlies only; close at 50% profit or 21 DTE; never hold into final week unhedged.

## 5. Full specification of the twist variant

**Universe.** SPX/SPY monthlies; VIX futures/calls for hedge wings; cash/T-bill collateral.

**Data requirements.** Options chains (IV surface, skew, VRP estimator), VIX futures curve, RV forecast, expiry calendar.

**Signal definitions (formulas).**

- VRP = IV_30d - RVforecast_30d; contango boolean; skew percentile; VIX levels.

**Entries.**

Monthly short 5–10 delta puts when gates pass, VRP-sized; hedge wings attached same day.

**Exits.**

50%/21-DTE take-profit; 2x premium stop; VIX-stop management; monthly roll (no holding to expiry pin).

**Position sizing.**

5–10% portfolio notional per cycle max, VRP-scaled; premium-spend 10–20% on hedges (budgeted, not optional).

**Risk limits.**

VIX halt hard; per-cycle loss cap 2% book; hedge-always rule (no naked override).

**Cost model & capacity.**

Option spreads + roll slippage; hedge drag 10–20% of premium (modeled as cost); capacity large (SPX).

**Parameters to validate (plateau, not peak):** Delta {5, 8, 10}; DTE {30, 40, 45}; profit-take {25%, 50%}; VIX halt {25, 30, 35}.

## 6. Failure modes & regime dependence

Vol-spike with skew explosion (hedges help, premium-stop still hit); 2022-style grind (contango gate keeps selling into slow bleed); hedge-basis failure (wings underperform the tail).

## 7. Validation protocol

**Status: no local backtest exists yet.** This library contains zero proprietary results; everything above is literature.

- **Data:** Options + VIX futures 2005–present; CBOE PUT methodology replication; expiry/pin-aware fills.
- **Splits:** chronological across cycles (must include 2008, 2020, 2022); no random k-fold; walk-forward anchored.
- **Cost/slippage model:** ETF expense + 2–10 bps/rebalance; options spreads + borrow where used; futures roll costs; stress 2x/3x.
- **Pitfalls:** look-ahead in index/constituent vintages; survivorship; same-bar ambiguity on rotation days; corporate actions; options expiry/pin.
- **Robustness:** plateau heatmaps; bootstrap CIs; placebo allocations (~zero edge); yearly + VIX/inflation-regime sub-samples; best-year removal.
- **Acceptance criteria:** OOS risk-adjusted dominance vs stated benchmark net of 2x costs; max DD within 1.2x of in-sample; positive in >= 60% of 3-year windows.

## 8. Sources read (annotated)

1. **CBOE PUT / BXM methodology + data.** https://www.cboe.com/indices — index rules + long-run facts. Index-authored.
2. **Bollerslev, Tauchen & Zhou / Carr & Wu on VRP.** Journals — variance premium existence. Known via secondary citation.
3. **Israelov & Nielsen on put-write timing.** Search "Still not cheap" / put-write timing — VRP scaling. Known via secondary citation.

## 9. Further reading

- Tastytrade put-write management statistics (practitioner).
- Universa tail-hedge whitepapers (hedge-leg design).
- VIX-ETN decay notes (what NOT to hold).
