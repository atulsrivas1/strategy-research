# 08. Graham Net-Current-Asset Value — Twist: NCAV-Q

> **Library:** Sigmatiq Strategy Library V3 | **Bucket:** Long-term investing | **Style:** Liquidation value
> **Instruments:** US common stocks trading below two-thirds of net current asset value | **Typical holding period:** 12 months, reformed each year | **Complexity (1–5):** 2 | **Evidence grade (A–C):** B
> **Status:** Research document. Figures are Carlisle, Mohanty, and Oxman's, plus what they attribute to Oppenheimer and to Graham. None are Sigmatiq backtests.

This is not a quality-compounder screen and not a magic-formula rank. Those start from earnings power. This one buys a stock only when the price is below a rough liquidation value of the current assets, and it expects most of the candidates to look like bad businesses.

## 1. Origin & lineage

**Benjamin Graham, Security Analysis (1934),** as summarized in the paper below: buy when the price is below net current asset value, because that figure is "a rough measure of liquidating value" and a stock should not sell continuously below it. Graham-Newman, 1930–1956, is reported by Oppenheimer (1986) as having earned about 20% a year on the rule. That sentence is Oppenheimer's claim, reached through Carlisle, Mohanty, and Oxman. Oppenheimer's FAJ paper was not fetched.

**The study read here is Tobias Carlisle, Sunil Mohanty, and Jeffrey Oxman, "Ben Graham's Net Nets: Seventy-Five Years Old and Outperforming," 24 June 2010.** They continue Oppenheimer's 1970–1983 test from 31 December 1983 through 31 December 2008.

## 2. The original rules (as published)

From the 2010 paper, read 2026-10-07:

- NCAV per share = (current assets − all liabilities − preferred) / common shares. This is the simplified screen. Graham and Dodd also haircut receivables, inventory, and fixed assets by hand; Martin Whitman adjusts further. The authors say the simplified screen likely *understates* what a case-by-case liquidation analysis would find, and they accept that.
- Buy if the November close is no more than two-thirds of NCAV. Portfolios are equal-weighted, purchased 31 December, held one year, then liquidated and rebuilt. A name can reappear if it is still cheap.
- Drop outliers whose price is under 1% of NCAV per share.
- Mean monthly return, 31 December 1983–31 December 2008: 2.55%. NYSE-AMEX index 0.85% (1.70% per month, which they annualize as 22.42%). Small-firm index 1.24% (1.31% per month, 16.90% annualized in their wording). A market-model excess return of 1.66% per month is in the abstract.
- Graham preferred a 30-month hold. On non-overlapping 30-month portfolios, the NCAV book beat NYSE-AMEX in 22 of 25 vintages, by 2.56% per month on average. Versus the small-firm index the margin is 1.86% per month.
- Oppenheimer had found that losing firms and non-dividend payers did slightly *better* than the "good" NCAV names Graham recommended. The 2010 paper says it could not find a factor that removes the excess return, then finds size, book-to-market, volume, dividend yield, liquidity, and distress (Altman Z) explain some of it. A January effect is large. An intercept remains.
- Price filters cut the raw return: excluding prices under $1 leaves 2.2% per month; under $5 leaves 1.6% per month. They still call the annual excess significant, "18% (9.8%) on the low end," depending on which risk model is used.
- Only 5 names in the sample delist for mergers and 9 for liquidation. The return is not a hidden merger premium.
- They do not charge commissions, and they argue benchmark turnover is higher than NCAV turnover so a commission haircut would favor NCAV. That argument is theirs. A modern test still has to charge the spread on a $1 stock.

A 2026 Review of Financial Economics abstract by Mohanty and Oxman (Ideas.repec.org, abstract only, not the paper) reports a 1969–2019 value-weighted NCAV portfolio at 1.94% per month, and an alpha of 1.09% per month after five Fama-French factors, a liquidity factor, and a January control, with the profit declining in 2004–2019. Abstract only. Not used as a specification input beyond the warning that the later window is weaker.

## 3. Why it works — mechanism & evidence

**Mechanism.** The buyer is paying less than a fire-sale value of cash, receivables, and inventory, after all debts. Either the assets are real and the price is wrong, or the assets are about to disappear (burn, write-off, fraud). The premium over a small-firm index, in their tables, is the part that is not just "you bought tiny stocks." Limits to arbitrage are their closing argument: the names are too small and too ugly for a mandate to hold, so the discount can sit there.

**What can kill it.** A $5 price filter already cuts the monthly mean from 2.55% to 1.6% in their test. That is the version a real book can trade. January does a lot of work. Distress explains some of the return and should, if the story is "these are broken firms." The 2004–2019 fade in the later abstract is the out-of-sample warning, and it was not verified against the full text.

**Synthesis.** Run the two-thirds rule on a liquidated balance sheet, hold a year, include delistings, and judge the book against a small-cap value baseline after spreads. The 2.55% monthly figure is the unfiltered academic portfolio.

## 4. The twist: NCAV-Q

1. **Tradable floor.** Price at least $5 and average daily dollar volume at least $200,000 at the December formation. Their own $5 filter is the precedent. Names under that floor stay in a research ledger and out of the book.
2. **Point-in-time statements.** NCAV uses the latest 10-Q or 10-K filed before 30 November. A November price divided by a December filing is look-ahead. The 2010 paper's "November close" has to be paired with information that existed in November.
3. **Two-thirds stays.** No rank-the-cheapest-decile substitute. The rule is a hard discount to liquidation value. Softening it to "cheap on book" turns it into the value factor this note is not.
4. **Hold 12 months, report 30.** The book rebalances annually, which matches their main table. A parallel 30-month ledger is reported and not traded, because Graham's horizon and their tradable horizon disagree and both should be visible.
5. **January is disclosed, not stripped.** They find a January effect. The strategy does not skip January to manufacture a smoother line, and it does not lever January. The validation reports January and non-January separately.

## 5. Full specification of the twist variant

**Universe.** US common stocks with a filed balance sheet. No ADRs, no funds, no shells with current assets that are a related-party receivable. That last exclusion is a data rule: if current assets are entirely a receivable from an affiliate, NCAV is not liquidation value. Implementing it requires the receivable footnote; if the footnote is missing, the name is out.

**Data.** Point-in-time current assets, total liabilities, preferred stock, shares, price, volume, delisting returns.

**Entry.** Form on the first session of December using the last filing dated on or before 30 November and the price that day. Their paper uses the November close and a 31 December purchase; we buy at the December formation close so the signal price and the accounting date are the same month. Equal weight. If fewer than 10 names qualify, hold the qualifiers and leave the rest in T-bills. Do not force a full book.

**Exit.** Sell at the close one year later, or at the delisting return if sooner. A name that still qualifies is a new purchase, not a free hold.

**Sizing.** Equal weight among qualifiers, max 40 names. If more than 40 qualify, keep the 40 with the lowest price / NCAV. Cash residual earns T-bills and is reported.

**Costs.** 40 basis points per side base, 100 basis points stress. These names are the ones their market-impact paragraph calls cheap to trade in theory and painful in a $5 filter world.

**Parameters.** Discount {1/2, 2/3, 3/4} of NCAV is the plateau. The $5 floor is not removed in order to recover the 2.55% figure.

## 6. Failure modes & regime dependence

Fraudulent current assets. Cash burn that empties NCAV before the year is over; the annual rebalance is slow relative to a quarterly cash burn. A bull market in which nothing trades below liquidation value and the book sits in T-bills, which is correct and will look like a tracking error. The post-2004 fade flagged in the 2026 abstract. Early warning: median price / NCAV of the book rises through 0.9, which means the two-thirds rule is being filled with names that barely qualify.

## 7. Validation protocol

**No local backtest exists.**

- **Baseline.** Small-cap value index, and the unfiltered NCAV book (including sub-$5) reported beside the tradable book so the cost of the floor is visible.
- **Splits.** 1984–2008 is their sample. Validation 2009–2018. Holdout 2019 onward. The 2026 abstract's 2004–2019 decline overlaps validation; do not drop those years.
- **Pitfalls.** Restated balance sheets used as if they were original. Dropping delists. Buying in November on a statement filed in December.
- **Acceptance.** Tradable book, after 100 basis point round-trip costs, beats the small-cap value baseline by at least 3% a year in validation, with a t-statistic on the annual difference at least 2, and at least eight names in the median year. A book that is usually in T-bills fails even if the few trades win.

## 8. Sources read (annotated)

1. **Carlisle, Mohanty, and Oxman, 24 June 2010.** https://sabercapitalmgt.com/wp-content/uploads/2013/03/75-Years-and-Outperforming-Graham-Strategy.pdf — fetched 2026-10-07. Read the abstract, the Graham rule, the portfolio construction, the 2.55% / 0.85% / 1.24% results, the 30-month 22-of-25 result, the earnings-and-dividend discussion, and the price-filter and delisting paragraphs.
2. **Mohanty and Oxman, Review of Financial Economics (2026), abstract only.** https://ideas.repec.org/a/wly/revfec/v44y2026i1ne70034.html — abstract read 2026-10-07. *Taken as a warning, not as a table:* later-window decay and a 1.09% monthly alpha claim that was not verified in the paper.
3. **Oppenheimer, FAJ 1986.** Not fetched. Numbers attributed to him are secondhand through the 2010 paper.
4. **Graham and Dodd, Security Analysis (1934).** Not read. The liquidation quote is via the 2010 paper.

## 9. Further reading

- Vu (1988), whom they cite. Not fetched.
- Whitman’s Third Avenue letters on haircutting NCAV. Not fetched.
- The 2026 Mohanty and Oxman full text, before anyone treats 1.09% a month as a planning number.
