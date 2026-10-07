# 33. Greenblatt Magic Formula — Twist: MAGIC-F

> **Library:** Sigmatiq Strategy Library V2 | **Bucket:** Long-term investing | **Style:** Value + quality systematic
> **Instruments:** Top-3500 US equities (ex-financials/utilities) | **Typical holding period:** 1 year per tranche (staggered) | **Complexity (1–5):** 2 | **Evidence grade (A–C):** B+
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise.

## 1. Origin & lineage

**Joel Greenblatt (2005).** *The Little Book That Beats the Market*: Magic Formula — rank by earnings yield (EBIT/EV) + return on capital (EBIT/(NWC + NFA)), buy top 20–30, hold 1 year, roll staggered tranches. Reported 1988–2004 backtest ~30% annualized (author's computation; costs/taxes lightly modeled). Practitioner: magicformulainvesting.com portfolios + 'value composite' literature (Gray–Carlisle *Quantitative Value*).

## 2. The original rules (as published)

- **Universe:** top 3500 by market cap, ex financials/utilities; min $50M (author's screen).
- **Rank:** EY + ROC ranks summed; buy top 20–30 equally weighted.
- **Hold:** 1 year per tranche; stagger (e.g. quarterly tranches) for diversification across vintages.
- **Tax variant:** sell losers in December, winners in January (loss-harvesting overlay).
- **What varies:** EY/ROC definitions, tranche count, size floor.

## 3. Why it works — mechanism & evidence

**Mechanism.** Cheap + good systematically: EY captures mispriced earnings power, ROC captures franchise quality; combined rank avoids value traps (cheap junk) and quality overpays (great-but-expensive); 1-year holds harvest the re-rating while turnover stays mechanical and emotion-free.

**Supporting evidence (all attributed, none ours):**

- Greenblatt reports 1988–2004 ~30% annualized vs ~12% S&P (author's backtest; small-cap tilt + pre-cost — weight accordingly).
- Gray–Carlisle and practitioner replications confirm long-run excess with large drawdowns (replication consensus: positive, lumpier than marketed).
- Academic cousins: value + profitability premia (Fama–French 5-factor; Novy-Marx) support the two ranks.

**Contradictory / decay evidence:**

- Post-2005 live/decayed estimates are far below 30% (decay + crowding + growth-regime headwinds for value).
- Formula suffers multi-year underperformance (2007–2020 value winter tested adherence severely).
- Tax-loss-selling overlay helps taxable but complicates the 'simple' story; small-cap names carry impact costs.

**Synthesis.** Magic Formula is valid systematic value-quality with marketed numbers from a friendly era: run it staggered, tax-aware, expecting decade-long faith tests — never as the whole portfolio.

## 4. The twist: MAGIC-F

1. **Staggered tranches (targets vintage risk):** 4 quarterly tranches of 25 names (100 total) so no single rebalance date defines the year.
2. **Quality floor (targets cheap-junk tail):** exclude Piotroski F-score <= 3 (merge with doc 34) even if ranked top — cheap fraud is not value.
3. **Size/liquidity floor (targets impact bleed):** min $500M cap + $2M ADV (above Greenblatt's $50M — capacity honesty).
4. **Tax-harvest calendar (targets taxable erosion):** December-loss / January-gain realization codified per tranche (US taxable note).
5. **Value-winter governor (targets abandonment):** pre-commit 10-year mandate letter + 50% Formula / 50% quality-compounding barbell (doc 35) so no single-factor winter forces capitulation.

## 5. Full specification of the twist variant

**Universe.** US top-3500 ex financials/utilities, >= $500M, ADV >= $2M.

**Data requirements.** Fundamentals point-in-time (EBIT, EV, NWC, NFA), F-score feed, price/volume, tax calendar.

**Signal definitions (formulas).**

- EY = EBIT/EV; ROC = EBIT/(NWC+NFA); summed ranks; F-score veto; tranche calendar.

**Entries (accumulation).**

Quarterly tranche formation (25 names equal-weight); no mid-quarter trading.

**Exits (trim/sell discipline).**

1-year tranche roll (December/January tax-aware for taxable); intra-year exits only on delisting/fraud-events.

**Position sizing.**

Equal-weight; 100 names across tranches; Formula sleeve 50% of value-barbelled book.

**Risk limits.**

F-score veto; size floor; 10-year mandate letter signed pre-launch (behavioral, disclosed); delisting-review rule.

**Cost model & capacity.**

100%/year turnover on the sleeve (~25%/quarter); 5–10 bps/side; taxes modeled (harvest overlay).

**Parameters to validate (plateau, not peak):** Names {20, 25, 30}/tranche; size floor {$100M, $500M, $1B}; hold {1Y}; barbell {30/70, 50/50}.

## 6. Failure modes & regime dependence

Value winters (multi-year underperformance); small-cap impact in thin names (hence floor); formula-crowding compressing the rank spread.

## 7. Validation protocol

**Status: no local backtest exists yet.** This library contains zero proprietary results; everything above is literature.

- **Data:** Fundamentals + prices 1990–present point-in-time; F-score reproducible; delisted included; tax lots modeled.
- **Splits:** chronological with point-in-time fundamentals (report dates, restatements vintaged); no random k-fold; must include full drawdown cycles.
- **Cost/slippage model:** 5–10 bps/side; taxes modeled (turnover matters more here than spreads); stress 2x.
- **Pitfalls:** survivorship (delisted included); look-ahead (period-end vs report-date); restatement handling (as-first-reported); corporate actions; index-constituent vintage honesty.
- **Robustness:** plateau checks; bootstrap CIs; placebo screens (~zero); yearly + valuation-regime sub-samples; best-decade removal.
- **Acceptance criteria:** OOS excess vs stated benchmark net of costs/taxes with lower or equal max DD; hit-rate on thesis milestones tracked; 10-year positive excess in >= 70% of vintages.

## 8. Sources read (annotated)

1. **Greenblatt, *The Little Book That Beats the Market* (2005).** Publisher: https://www.wiley.com — formula + 1988–2004 backtest. Book-level knowledge.
2. **magicformulainvesting.com methodology.** https://www.magicformulainvesting.com — screen + tranche mechanics. Site-authored.
3. **Gray & Carlisle, *Quantitative Value*.** Publisher pages — value-composite replication context. Book-level knowledge.

## 9. Further reading

- Fama–French 5-factor (value/profitability cousins).
- Piotroski F-score overlay papers.
- Tax-loss-harvesting implementation notes.
