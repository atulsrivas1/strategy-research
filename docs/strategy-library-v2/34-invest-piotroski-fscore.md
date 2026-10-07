# 34. Piotroski F-Score Value Filter — Twist: FSCORE-T

> **Library:** Sigmatiq Strategy Library V2 | **Bucket:** Long-term investing | **Style:** Value quality filter
> **Instruments:** High book-to-market equities | **Typical holding period:** 1–2 years | **Complexity (1–5):** 2 | **Evidence grade (A–C):** B+
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise.

## 1. Origin & lineage

**Joseph Piotroski (2002, Chicago/Stanford).** 'Value Investing: The Use of Historical Financial Statement Information to Separate Winners from Losers' (Journal of Accounting Research): 9-binary-signal F-score (profitability 4, leverage/liquidity/source-of-funds 3, efficiency 2) applied to high-BM quintile; reported long-short high-minus-low F-score spread ~23% annualized 1976–1996 (author's sample). Practitioner: value-desk quality overlay + 'F-score > 7' screens (AAII/Quantpedia presets).

## 2. The original rules (as published)

- **Universe:** highest book-to-market quintile.
- **Score (1 point each):** ROA > 0; CFO > 0; ΔROA > 0; accruals (CFO > ROA); Δleverage < 0; Δcurrent-ratio > 0; no new equity; Δgross-margin > 0; Δasset-turnover > 0.
- **Trade:** long high F (8–9), short low F (0–1) within value; hold 1 year (author's 1–2Y variants).
- **What varies:** BM vs EY value anchor; 8–9 vs 7–9 long cutoff; hold length.

## 3. Why it works — mechanism & evidence

**Mechanism.** Financial-statement triage among cheap stocks: most high-BM names are cheap for good reason (distress); the nine signals isolate improving profitability, de-risking balance sheets, and efficiency gains — winners among losers — so the value premium is harvested without the distress tail.

**Supporting evidence (all attributed, none ours):**

- Piotroski reports high-minus-low F-score ~23%/year 1976–1996 value universe (author's sample; pre-cost, small-cap-tilted).
- Replications (US + international) confirm positive high-minus-low spreads, smaller post-2000 (decay consensus).
- Mohanram G-score (growth analogue) extends the triage logic to growth (family support).

**Contradictory / decay evidence:**

- Post-1996/2000 spreads compress materially; transaction costs on tiny high-BM names erase much of the paper long-short.
- Binary 9-signal coarseness loses information vs continuous quality composites (debated refinement).
- Financials/utilities need adjusted signals (accrual/leverage definitions differ) — naive screens misfire.

**Synthesis.** F-score is the correct value-quality gate rather than a standalone long-short for most books: use 7+ as the value filter (docs 31/33 overlays) and run the long-short only where borrow/prime supports it.

## 4. The twist: FSCORE-T

1. **Filter-first deployment (targets distress tails):** primary use is veto (F ≤ 3 excluded) + boost (F ≥ 7 gets 1.5x) inside value sleeves; standalone long-short is opt-in.
2. **Accrual-double-weight (targets earnings-quality failures):** CFO>ROA + ΔROA both required for full boost (not either/or) — earnings quality over level.
3. **No-new-equity hard veto (targets dilution traps):** any seasoned offering in the scoring year caps score at 6 regardless of other signals.
4. **Sector-relative BM (targets sector-value confusion):** high-BM defined within sector, not market-wide (banks/utilities scored on adjusted signals or excluded).
5. **Two-year confirmation hold (targets one-year whipsaw):** F ≥ 7 names held 2 years unless score falls ≤ 3 (patience overlay on triage).

## 5. Full specification of the twist variant

**Universe.** High-BM within-sector top quintile; ex financials/utilities in core (adjusted-spec sleeve optional).

**Data requirements.** Financial-statement point-in-time (ROA/CFO/accruals/leverage/liquidity/margin/turnover/equity-issuance), BM ranks, restatements.

**Signal definitions (formulas).**

- 9 binaries as published + issuance veto + sector-relative BM; boost/veto thresholds.

**Entries (accumulation).**

Annual formation (May, post-10-K season); long 8–9 (boost 7s at half); short 0–1 only in long-short variant with borrow check.

**Exits (trim/sell discipline).**

Annual roll; early exit on score ≤ 3 at interim statements or restatement/offering events.

**Position sizing.**

Equal-weight; value-sleeve 30–50% of book in filter deployment; long-short variant 130/30-capped.

**Risk limits.**

Issuance/restatement hard rules; sector-relative discipline; borrow-availability gate on shorts.

**Cost model & capacity.**

Low turnover (annual); borrow on short leg; taxes long-term favored on 2Y holds.

**Parameters to validate (plateau, not peak):** Long {7–9, 8–9}; hold {1Y, 2Y}; BM {quintile, decile}; sector {pooled, relative}.

## 6. Failure modes & regime dependence

Value-winter cohorts (all cheap stays cheap); restated-statement scores (garbage-in triage); microcap impact on formation days.

## 7. Validation protocol

**Status: no local backtest exists yet.** This library contains zero proprietary results; everything above is literature.

- **Data:** Statements + prices 1976–present point-in-time (restatements vintaged); BM reproducible; delisted included.
- **Splits:** chronological with point-in-time fundamentals (report dates, restatements vintaged); no random k-fold; must include full drawdown cycles.
- **Cost/slippage model:** 5–10 bps/side; taxes modeled (turnover matters more here than spreads); stress 2x.
- **Pitfalls:** survivorship (delisted included); look-ahead (period-end vs report-date); restatement handling (as-first-reported); corporate actions; index-constituent vintage honesty.
- **Robustness:** plateau checks; bootstrap CIs; placebo screens (~zero); yearly + valuation-regime sub-samples; best-decade removal.
- **Acceptance criteria:** OOS excess vs stated benchmark net of costs/taxes with lower or equal max DD; hit-rate on thesis milestones tracked; 10-year positive excess in >= 70% of vintages.

## 8. Sources read (annotated)

1. **Piotroski (2002), JAR.** Search "Value Investing: The Use of Historical Financial Statement Information" — 9 signals + 1976–1996 spread. Known via secondary citation.
2. **Mohanram G-score (growth analogue).** Search "Separating Winners from Losers among Low Book-to-Market" — family support. Known via secondary citation.
3. **AAII/Quantpedia F-score presets (practitioner).** Search "Piotroski F-score screen" — 7+ overlay convention. Practitioner-authored.

## 9. Further reading

- Post-2000 F-score replication/decay notes.
- Financial-firm adjusted-signal papers.
- Accrual-anomaly (Sloan) originals.
