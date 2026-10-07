# 27. Managed-Futures CTA Time-Series Trend — Twist: CTA-T

> **Library:** Sigmatiq Strategy Library V2 | **Bucket:** Portfolio / Macro | **Style:** Time-series momentum
> **Instruments:** 60+ futures: equity, rates, FX, commodities | **Typical holding period:** 1–12 months per position | **Complexity (1–5):** 5 | **Evidence grade (A–C):** A-
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise.

## 1. Origin & lineage

**CTA lineage.** Bill Dunn / John Henry 1970s → AHL/Man (adaptive/ML trend) → Winton → Hurst–Ooi–Pedersen academic canon (*A Century of Evidence*, 2017) + SG CTA index standard. Moskowitz–Ooi–Pedersen (2012) time-series momentum is the academic engine; Baltas–Kosowski trend-factor work is the risk overlay. Our twist is the textbook CTA with vol-targeting + correlation-gated breadth.

## 2. The original rules (as published)

- **Signal (MOP/HOP):** 12-month (or 1/3/6/12 composite) time-series momentum per market: long if trailing excess positive, short if negative.
- **Sizing:** volatility-targeted (e.g. 40–60 bps ex-ante vol per market, 10–12% book).
- **Rebalance:** monthly (or weekly for faster sleeves); roll-aware; crisis-alpha narrative (long bonds/short commodities into deflation scares).
- **What varies:** lookback composites, vol target, breadth (20 vs 100 markets), execution smoothing.

## 3. Why it works — mechanism & evidence

**Mechanism.** Slow information diffusion + herding + risk-management feedback loops create multi-month trends; cross-asset breadth diversifies whipsaw; vol-targeting keeps ex-ante risk constant so calm-period leverage and stress-period deleveraging happen mechanically; crisis alpha arrives via flight-to-quality trends (long duration, short cyclicals).

**Supporting evidence (all attributed, none ours):**

- HOP report trend premia across 100+ years and 60+ markets (authors' construction; widely cited, debated costs).
- SG CTA index long-run positive skew + 2008/2020 crisis-alpha episodes (index fact).
- MOP document time-series momentum across asset classes 1985–2009 (academic core).

**Contradictory / decay evidence:**

- 2011–2019 CTA drought (fees vs flat gross) is the documented near-death; crowded medium-term lookbacks whipsawed together.
- Replication net of realistic roll/slippage + fees roughly halves paper Sharpe (cost honesty matters more here than anywhere).
- Single-lookback CTAs crash on V-reversals (2020 March–April whipsaw both directions).

**Synthesis.** CTA trend is the portfolio diversifier with the longest academic pedigree and the most honest drought record: trade it broad, vol-targeted, composite-signal — and expect multi-year flat stretches.

## 4. The twist: CTA-T

1. **Composite signal (targets single-lookback whipsaw):** vote 3/6/12-month formation; require 2-of-3 for full size (half on 1-of-3).
2. **Ex-ante vol budgeting (targets risk drift):** 50 bps per market, 10% book target; leverage floats with 1/realized-vol (mechanical, no committee).
3. **Correlation-breadth gate (targets crowded whipsaw):** cap 40% of risk in any 0.6+ correlated cluster; add markets (target 60+) rather than size when breadth allows.
4. **Crisis-alpha sleeve protection (targets pro-cyclical cuts):** duration-short-commodity tails exempt from fast-exit rules during equity-stress flags (let crisis alpha run).
5. **Fee-aware execution (targets turnover bleed):** signal-change buffer (1-vol hysteresis) + roll-optimized calendar; turnover budget 4x book/year max.

## 5. Full specification of the twist variant

**Universe.** 60+ liquid futures + FX forwards; no single-name equities (index/factor only); no crypto in core (separate sleeve).

**Data requirements.** Futures daily (back-adjusted signals, unadjusted PnL), vol estimator, correlation matrix, roll calendar, fee schedule.

**Signal definitions (formulas).**

- Formation excess per lookback; 2-of-3 vote; per-market vol for sizing; cluster map; stress flag (equity drawdown > 2 sigma).

**Entries.**

Monthly (+ weekly fast sleeve) into voted direction at vol-budgeted size; hysteresis buffer avoids micro-flips.

**Exits.**

Signal-vote flip or vol-stop; crisis sleeve uses slower exit during stress flag; roll-aware transitions.

**Position sizing.**

50 bps/market, 10% book; cluster caps; fast sleeve 20% of risk max.

**Risk limits.**

Cluster caps; turnover budget; stress-flag exit-slowdown rules frozen (no discretion); delivery never held.

**Cost model & capacity.**

Commissions + roll + 1-tick/side; 2% management + 20% incentive modeled for fund rendering (disclosed); capacity institutional (futures breadth).

**Parameters to validate (plateau, not peak):** Lookbacks {1/3/6/12 composite variants}; vol {8%, 10%, 12%}; hysteresis {0.5, 1.0, 1.5} vol; breadth {30, 60, 100}.

## 6. Failure modes & regime dependence

Correlated-whipsaw years; V-reversals; fee-drag in flat years; roll-curve shifts (contango/backwardation flips) altering carry-adjusted trends.

## 7. Validation protocol

**Status: no local backtest exists yet.** This library contains zero proprietary results; everything above is literature.

- **Data:** Futures 1990–present back-adjusted + rolls; SG CTA methodology for benchmark; costs per era.
- **Splits:** chronological across cycles (must include 2008, 2020, 2022); no random k-fold; walk-forward anchored.
- **Cost/slippage model:** ETF expense + 2–10 bps/rebalance; options spreads + borrow where used; futures roll costs; stress 2x/3x.
- **Pitfalls:** look-ahead in index/constituent vintages; survivorship; same-bar ambiguity on rotation days; corporate actions; options expiry/pin.
- **Robustness:** plateau heatmaps; bootstrap CIs; placebo allocations (~zero edge); yearly + VIX/inflation-regime sub-samples; best-year removal.
- **Acceptance criteria:** OOS risk-adjusted dominance vs stated benchmark net of 2x costs; max DD within 1.2x of in-sample; positive in >= 60% of 3-year windows.

## 8. Sources read (annotated)

1. **Hurst, Ooi & Pedersen, "A Century of Evidence on Trend-Following."** https://papers.ssrn.com — long-run CTA evidence. Known via secondary citation.
2. **Moskowitz, Ooi & Pedersen (2012), "Time Series Momentum."** Journal of Financial Economics — signal engine. Known via secondary citation.
3. **SG CTA Index methodology.** https://www.sgmarkets.com (search SG CTA) — benchmark + crisis-alpha episodes. Index-authored.

## 9. Further reading

- Baltas–Kosowski trend-factor overlays.
- AHL adaptive-trend whitepapers.
- CTA drought post-mortems (2011–2019).
