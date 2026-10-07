# 31. Buffett Quality-Value Compounding — Twist: VALUE-Q

> **Library:** Sigmatiq Strategy Library V2 | **Bucket:** Long-term investing | **Style:** Quality value
> **Instruments:** Global equities (concentrated) | **Typical holding period:** Years to decades | **Complexity (1–5):** 3 | **Evidence grade (A–C):** A-
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise.

## 1. Origin & lineage

**Warren Buffett / Berkshire Hathaway (1965–present).** Graham (cigar butts) → Fisher/Munger (wonderful businesses at fair prices) → Buffett letters (1977–present): float-funded concentrated quality compounding — high ROE, owner-earnings, moats, honest managers, margin of safety. Lineage: Berkshire letters + *The Snowball* + Cunningham *Essays of Warren Buffett*. Pabrai/Spier 'clone' literature is the practitioner bridge.

## 2. The original rules (as published)

- **Circle of competence:** only businesses understood deeply enough to forecast 10-year cash generation.
- **Quality:** consistent high ROE/ROIC, owner earnings (reported + D&A - maintenance capex), pricing power, low debt.
- **Price:** margin of safety vs intrinsic value (DCF with humility, not precision); 'far more important than timing'.
- **Concentration + patience:** few big bets, decades-long holds, sell on thesis-break (moat loss, manager failure) not price wiggles.
- **What is NOT a rule:** no P/E cutoff, no screen — judgment over thresholds.

## 3. Why it works — mechanism & evidence

**Mechanism.** Mispricing of durable compounding + float leverage + behavior: markets underpay for slow compounding quality and overreact to transient disappointment; insurance float provides negative-cost leverage; patience harvests the compounding while turnover/taxes stay near zero.

**Supporting evidence (all attributed, none ours):**

- Berkshire book value ~20% CAGR 1965–2023 vs ~10% S&P (company-reported; share-price path lumpier — the headline fact).
- Frazzini–Kabiller–Pedersen ' explicitly attribute Buffett returns to quality/low-vol/leverage factors, replicable systematically (authors' claim).
- Value+quality academic family (Novy-Marx; Asness quality-minus-junk) supports the factorized cousin.

**Contradictory / decay evidence:**

- 2008–2020 Berkshire underperformed SPY stretches (size + value-tilt drag in growth decades).
- Float-leverage + concentration = drawdowns rival equity (-50% 2008/2020 episodes); 'safe' framing overstates smoothness.
- Replicating letters with hindsight overfits; real-time wonderful-at-fair-price identification is the hard part.

**Synthesis.** Buffett's codable core is systematic quality-at-reasonable-price with concentration and patience; the uncodable parts (manager judgment, float structure) become factor tilts + hold discipline in our version.

## 4. The twist: VALUE-Q

1. **Frozen quality-value screen (targets hindsight-picking):** ROIC > 15% 5Y median, FCF margin > 10%, debt/EBITDA < 3x, P/owner-earnings < 20x — all must pass, no exceptions.
2. **Moat proxy (targets story stocks):** gross margin > 40% + pricing-power test (revenue/employee growth with stable margins); fail either = excluded.
3. **Thesis-break sells only (targets price-wiggle sells):** sell on ROIC < 12% 2Y, dividend cut/raise-debt-for-buybacks, or accounting restatement — never on -20% price alone.
4. **Concentration ladder (targets diworsification):** 8–15 names, top-3 max 40%; new money to cheapest qualifier (mechanical rebalance of attention).
5. **Cash-as-call (targets fully-invested drawdowns):** hold 10–30% T-bills when qualifiers < 8 (no forcing mediocre ideas).

## 5. Full specification of the twist variant

**Universe.** Global developed equities, ADR-accessible; no leveraged financials, no pre-revenue, no state-controlled.

**Data requirements.** 10-K point-in-time fundamentals, owner-earnings worksheet, moat proxies, Berkshire-letter checklist, restatement feed.

**Signal definitions (formulas).**

- Quality/price gates as above; thesis-break booleans; cash-rule qualifier count.

**Entries (accumulation).**

Accumulate qualifiers on 10–20% drawdowns from 52-week high (patient limit ladder); starter 2%, add to 6–8% on thesis-confirm quarters.

**Exits (trim/sell discipline).**

Thesis-break sells (full); trim top position back to 10% on > 2x intrinsic sprint (valuation, not impatience); never sell clocks (no time-stops).

**Position sizing.**

8–15 names, 4–10% each; cash 10–30% by qualifier count; no leverage (float not replicated at retail).

**Risk limits.**

Thesis-break hard; restatement = immediate review-to-sell; sector 30% cap; cash floor 10% (dry powder).

**Cost model & capacity.**

Minimal turnover (single-digit %/year); taxes: hold > 1Y long-term treatment (disclosed); capacity large.

**Parameters to validate (plateau, not peak):** ROIC {12%, 15%, 18%}; P/OE {15x, 20x, 25x}; names {8, 12, 20}; cash {0–20%, 10–30%}.

## 6. Failure modes & regime dependence

Value-trap quality (melting moats that screen well for years); growth-decade underperformance testing patience; concentration drawdowns; accounting fraud through screens (hence restatement rule).

## 7. Validation protocol

**Status: no local backtest exists yet.** This library contains zero proprietary results; everything above is literature.

- **Data:** Fundamentals point-in-time 1990–present + prices incl. delisted; restatement vintages; Berkshire-letter checklist frozen.
- **Splits:** chronological with point-in-time fundamentals (report dates, restatements vintaged); no random k-fold; must include full drawdown cycles.
- **Cost/slippage model:** 5–10 bps/side; taxes modeled (turnover matters more here than spreads); stress 2x.
- **Pitfalls:** survivorship (delisted included); look-ahead (period-end vs report-date); restatement handling (as-first-reported); corporate actions; index-constituent vintage honesty.
- **Robustness:** plateau checks; bootstrap CIs; placebo screens (~zero); yearly + valuation-regime sub-samples; best-decade removal.
- **Acceptance criteria:** OOS excess vs stated benchmark net of costs/taxes with lower or equal max DD; hit-rate on thesis milestones tracked; 10-year positive excess in >= 70% of vintages.

## 8. Sources read (annotated)

1. **Berkshire Hathaway shareholder letters (1977–present).** https://www.berkshirehathaway.com/letters — quality/margin-of-safety doctrine. Primary source.
2. **Frazzini, Kabiller & Pedersen, "Buffett's Alpha."** https://papers.ssrn.com — factorized Buffett (quality/low-vol/leverage). Known via secondary citation.
3. **Cunningham, *The Essays of Warren Buffett*.** Publisher pages — curated letter doctrine. Book-level knowledge.

## 9. Further reading

- Graham *Intelligent Investor* (cigar-butt ancestor).
- Fisher *Common Stocks and Uncommon Profits* (quality ancestor).
- Pabrai/Spier cloning notes (practitioner bridge).
