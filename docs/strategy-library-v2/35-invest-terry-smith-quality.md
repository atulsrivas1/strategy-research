# 35. Terry Smith Quality Compounding — Twist: QUAL-C

> **Library:** Sigmatiq Strategy Library V2 | **Bucket:** Long-term investing | **Style:** Quality compounding
> **Instruments:** Global quality equities (concentrated) | **Typical holding period:** Years (near-zero turnover) | **Complexity (1–5):** 2 | **Evidence grade (A–C):** B+
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise.

## 1. Origin & lineage

**Terry Smith / Fundsmith (2010–present).** 'Buy good companies, don't overpay, do nothing': high ROCE, cash conversion, low leverage compounders held with ~near-zero turnover; Fundsmith letters report long-run outperformance vs MSCI World with lower turnover (fund-reported; fee/share-class specifics matter). Lineage: Fisher/Munger quality → Smith's *Accounting for Growth* (forensic skepticism) → Fundsmith screen + 'do nothing' discipline. Terry Smith annual letters + shareholder meetings are the primary record.

## 2. The original rules (as published)

- **Buy good companies:** high return on capital, high cash conversion, strong moats, resilient demand.
- **Don't overpay:** reasonable FCF yield entry discipline (not deep value — 'fair price for wonderful').
- **Do nothing:** minimal trading; 'trading costs and taxes are certain, outperformance is not' (Smith's minimization mantra).
- **Avoid:** cyclicals, leveraged financials, binary tech, fads; sell on fundamental deterioration, not price.
- **What is NOT a screen:** no fixed ROCE/PE cutoffs published as a formula — principles over thresholds.

## 3. Why it works — mechanism & evidence

**Mechanism.** Compounder math + behavior: high-ROCE reinvestment compounds intrinsic value while the market underpays for steadiness; near-zero turnover eliminates the two certain taxes (costs + decisions); forensic accounting avoids the blow-ups that destroy buy-and-hold compounding.

**Supporting evidence (all attributed, none ours):**

- Fundsmith letters report since-inception excess vs MSCI World with single-digit turnover (fund-reported; survivorship of the narrative favors the winner — weight accordingly).
- Quality-minus-junk (Asness et al.) and profitability (Novy-Marx) academic premia support the factorized cousin.
- Low-turnover compounding arithmetic (cost/tax drag differentials) is uncontroversial.

**Contradictory / decay evidence:**

- Quality-at-any-price vintages (2020–2021) derated painfully in 2022 (duration-like drawdowns in 'safe' compounders).
- Single-manager narrative risk: Fundsmith's record is one realization; quality-fund cross-sections show wide dispersion.
- 'Do nothing' fails when moats erode (retail/consumer compounders disrupted) — inaction becomes the risk.

**Synthesis.** Smith's durable core is a frozen quality screen plus entry-yield discipline plus genuine inaction; our twist codes all three and adds a moat-erosion sell rule so 'do nothing' never means 'do nothing forever.'

## 4. The twist: QUAL-C

1. **Frozen quality (targets story drift):** ROCE > 20% 5Y median, cash conversion > 90%, interest cover > 8x — all required.
2. **Don't-overpay gate (targets 2021 vintages):** FCF yield at entry ≥ 3.5% (inverse of pay-anything); no adds below 3.0% current yield.
3. **Do-nothing charter (targets fidgeting):** 3-year minimum hold (except fraud/cut); max 15% turnover/year hard cap.
4. **Moat-erosion sells (targets disrupted compounders):** sell on ROCE < 15% 2Y, cash conversion < 80% 2Y, or dividend cut — price never triggers sells.
5. **Forensic veto (targets accounting compounders):** Smith-style red flags (capitalized costs growth > sales, acquisition-spree goodwill, pension fudges) = excluded at screen.

## 5. Full specification of the twist variant

**Universe.** Global developed quality, ADR-accessible; ex cyclicals/leveraged-financials/binary-biotech.

**Data requirements.** 5Y ROCE/cash-conversion/cover history point-in-time, FCF-yield engine, forensic-flag checklist, dividend feed.

**Signal definitions (formulas).**

- Quality booleans + entry-yield gate + erosion/sell booleans + forensic veto.

**Entries (accumulation).**

Accumulate qualifiers on 15%+ drawdowns (patience ladder); starter 3%, full 6–8% on confirming annuals.

**Exits (trim/sell discipline).**

Erosion/fraud/cut sells only; trim above 12% position size; no time-stops, no price-stops.

**Position sizing.**

12–20 names, 5–10% each; cash 0–20% when qualifiers scarce (do not force).

**Risk limits.**

Erosion rules hard; forensic veto pre-entry; single-name 12% cap; annual letter-style thesis review (written).

**Cost model & capacity.**

Near-zero turnover (~5–10%/year); taxes long-term; capacity large (mega-cap compounders).

**Parameters to validate (plateau, not peak):** ROCE {15%, 20%, 25%}; FCF yield {3%, 3.5%, 4%}; names {12, 16, 25}; turnover cap {10%, 15%, 20%}.

## 6. Failure modes & regime dependence

Quality-duration drawdowns (2022 family); disrupted compounders held via inaction (hence erosion rule); sustained overvaluation regimes with no qualifying entries (cash drag).

## 7. Validation protocol

**Status: no local backtest exists yet.** This library contains zero proprietary results; everything above is literature.

- **Data:** Fundamentals 2000–present point-in-time; prices incl. delisted; dividend/restatement vintages.
- **Splits:** chronological with point-in-time fundamentals (report dates, restatements vintaged); no random k-fold; must include full drawdown cycles.
- **Cost/slippage model:** 5–10 bps/side; taxes modeled (turnover matters more here than spreads); stress 2x.
- **Pitfalls:** survivorship (delisted included); look-ahead (period-end vs report-date); restatement handling (as-first-reported); corporate actions; index-constituent vintage honesty.
- **Robustness:** plateau checks; bootstrap CIs; placebo screens (~zero); yearly + valuation-regime sub-samples; best-decade removal.
- **Acceptance criteria:** OOS excess vs stated benchmark net of costs/taxes with lower or equal max DD; hit-rate on thesis milestones tracked; 10-year positive excess in >= 70% of vintages.

## 8. Sources read (annotated)

1. **Fundsmith annual letters/shareholder meetings.** https://www.fundsmith.co.uk — buy-good/don't-overpay/do-nothing doctrine. Firm-authored primary record.
2. **Smith, *Accounting for Growth* (1992).** Publisher pages — forensic veto lineage. Book-level knowledge.
3. **Asness et al. quality-minus-junk; Novy-Marx profitability.** Journals — academic cousins. Known via secondary citation.

## 9. Further reading

- Munger/Fisher quality originals (ancestors).
- Fundsmith sustainable-equity extensions.
- Quality-duration 2022 post-mortems.
