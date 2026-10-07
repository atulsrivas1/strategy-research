# 32. Lynch GARP (Growth at a Reasonable Price) — Twist: GARP-L

> **Library:** Sigmatiq Strategy Library V2 | **Bucket:** Long-term investing | **Style:** GARP
> **Instruments:** US/small-mid growth equities | **Typical holding period:** 1–5 years | **Complexity (1–5):** 2 | **Evidence grade (A–C):** B+
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise.

## 1. Origin & lineage

**Peter Lynch (1977–1990 Magellan).** *One Up on Wall Street* (1989) + *Beating the Street* (1993): ~29% annualized Magellan run (fund-reported) via bottom-up GARP — PEG ≤ 1, understandable growers, insider buying, boring names, 'tenbaggers' held for years. Practitioner bridge: PEG screens (Value Line/YCharts presets) + subjective 'cockroach theory' (one problem = more problems). Our twist freezes the folklore into gates.

## 2. The original rules (as published)

- **PEG:** P/E divided by growth ≤ 1 (Lynch's 'fair' line; < 0.5 = bargain in his telling).
- **Growth + health:** consistent earnings growth, low debt, cash-rich, dividend-raisers preferred.
- **Know what you own:** 6-category taxonomy (slow growers/stalwarts/fast growers/cyclicals/turnarounds/asset plays); buy understandable fast growers.
- **Watering flowers:** hold winners for years ('tenbaggers need time'); cut weeds fast (thesis-break, not price).
- **What is NOT rigorous:** growth-window (3 vs 5Y), PEG numerator (trailing vs forward), category lines — all fuzzy.

## 3. Why it works — mechanism & evidence

**Mechanism.** Growth-mispricing middle: pure value misses growers, pure momentum overpays; PEG sorts for growth the market has not yet capitalized; understandable mid-caps are under-followed (neglect premium) with insider/buyback confirmation of alignment.

**Supporting evidence (all attributed, none ours):**

- Magellan 1977–1990 ~29% annualized (fund-reported; era small-cap tailwinds + Lynch skill debated — weight as strong practitioner claim).
- PEG-screen practitioner studies show GARP cohorts beating pure value/growth blends in backtests (vendor/letter-reported; construction-sensitive).
- Academic cousins: earnings-growth persistence + neglect/small-cap attention effects (family evidence, not a PEG proof).

**Contradictory / decay evidence:**

- PEG gaming (one-time growth bursts, cyclical-peak E) creates value-trap 'cheap growers' that implode.
- Forward-E PEGs inherit analyst optimism bias (systematically flattering PEGs).
- Lynch-era small-cap coverage gaps have narrowed (more analysts, faster digestion).

**Synthesis.** GARP works as a quality-growth filter with valuation humility: freeze PEG/growth/health into gates, demand understandable businesses, hold for years — and police cyclical-peak E.

## 4. The twist: GARP-L

1. **Frozen PEG (targets E-gaming):** PEG on 3Y trailing EPS CAGR (not forward), require 0.5–1.2; cyclical-peak veto (shillerized-E check: P/10Y-avg-E must also be < 25x).
2. **Health gates (targets leveraged growers):** debt/EBITDA < 2.5x + FCF-positive + insider net-buy or buyback shrink in last year.
3. **Category discipline (targets story drift):** fast-grower + stalwart only; no turnarounds/cyclicals/asset-plays in this sleeve (separate specs).
4. **Watering schedule (targets early sells):** no full sells before 2 years except thesis-break; trims only above 3x cost (let tenbaggers run).
5. **Cockroach rule (targets hope-holds):** restatement, auditor resignation, or dividend cut = immediate full exit (no second chances).

## 5. Full specification of the twist variant

**Universe.** US $500M–$50B, price > $10, ADV > $3M; understandable sectors (no binary biotech).

**Data requirements.** Trailing fundamentals point-in-time, PEG engine, insider/buyback feed, restatement/div-calendar, category tags.

**Signal definitions (formulas).**

- PEG_3Ytrailing in [0.5, 1.2]; health booleans; Shiller-P/E veto; cockroach booleans.

**Entries (accumulation).**

Half on qualification, add half on first 10% dip with thesis intact (patience ladder); max 20 names entered per year (selectivity).

**Exits (trim/sell discipline).**

Thesis-break/cockroach full exits; trim 1/3 at 3x; hold-the-rest years; PEG > 2.5 on trailing (no longer reasonable) = staged exit over 4 quarters.

**Position sizing.**

3–6% per name, 15–25 names; sector 25% cap.

**Risk limits.**

Cockroach hard-exits; cyclical veto; 2-year minimum-hold discipline (except breaks); annual thesis review per name (written, dated).

**Cost model & capacity.**

Low turnover (~20%/year); taxes long-term favored; capacity moderate-large.

**Parameters to validate (plateau, not peak):** PEG {0.4–1.0, 0.5–1.2, 0.6–1.5}; growth window {3Y, 5Y}; trim {2x, 3x, 5x}; names {15, 20, 30}.

## 6. Failure modes & regime dependence

Cyclical-peak growers (E collapses, PEG explodes); growth-style bear markets (all GARP derates together); fraud through health screens.

## 7. Validation protocol

**Status: no local backtest exists yet.** This library contains zero proprietary results; everything above is literature.

- **Data:** Fundamentals point-in-time 1990–present incl. delisted; insider/buyback vintages; restatements.
- **Splits:** chronological with point-in-time fundamentals (report dates, restatements vintaged); no random k-fold; must include full drawdown cycles.
- **Cost/slippage model:** 5–10 bps/side; taxes modeled (turnover matters more here than spreads); stress 2x.
- **Pitfalls:** survivorship (delisted included); look-ahead (period-end vs report-date); restatement handling (as-first-reported); corporate actions; index-constituent vintage honesty.
- **Robustness:** plateau checks; bootstrap CIs; placebo screens (~zero); yearly + valuation-regime sub-samples; best-decade removal.
- **Acceptance criteria:** OOS excess vs stated benchmark net of costs/taxes with lower or equal max DD; hit-rate on thesis milestones tracked; 10-year positive excess in >= 70% of vintages.

## 8. Sources read (annotated)

1. **Lynch, *One Up on Wall Street* (1989).** Publisher: https://www.simonandschuster.com — PEG/taxonomy/tenbagger doctrine. Book-level knowledge.
2. **Magellan fund records (Fidelity).** https://www.fidelity.com — return context. Fund-reported.
3. **PEG-screen practitioner literature.** Vendor/letter backtests — construction-sensitive; illustrative weight only.

## 9. Further reading

- Lynch *Beating the Street* (portfolio cases).
- Cyclical-earnings normalization notes (Shiller P/E).
- Insider/buyback signal literature.
