# 04. Opportunistic Insider Purchases — Twist: INS-R

> **Library:** Sigmatiq Strategy Library V3 | **Bucket:** Swing, about one month | **Style:** Filing-based event
> **Instruments:** US common stocks with Form 4 open-market purchases | **Typical holding period:** One month from the filing, not from the trade | **Complexity (1–5):** 3 | **Evidence grade (A–C):** B+
> **Status:** Research document. Return figures are Cohen, Malloy, and Pomorski's. None are Sigmatiq backtests.

This is not a quality-factor screen and not a post-earnings drift trade. The signal is a specific insider's purchase, after the filing is public, and only if that insider's own history does not show a calendar habit.

## 1. Origin & lineage

**Lauren Cohen, Christopher Malloy, and Lukasz Pomorski, "Decoding Inside Information," Journal of Finance 67 (2012), 1009–1043.** NBER working paper 16454, October 2010, was the text fetched and read. The published citation is given in the NBER page: JF 2012.

They start from a fact earlier papers already had: insider *purchases* forecast returns, insider *sales* mostly do not (they cite Jeng, Metrick, and Zeckhauser 2003 for the "sales don't work" summary). Their contribution is to split insiders, not firms, into routine and opportunistic, using only the insider's past calendar.

## 2. The original rules (as published in the pages read)

From the NBER working paper introduction and data section, read 2026-10-07:

- Data: Thomson Reuters Form 4 open-market purchases and sales, January 1986–December 2007. Officers, directors, and beneficial owners over 10%. Options exercises and private transactions are excluded.
- In that era, Section 16 required reporting by 10 days after the month-end of the trade. That lag is part of the result. A test that trades on the transaction date, before the filing, is not their strategy.
- A routine trader is an insider who traded in the same calendar month for at least "a certain number of years" in the past. The introduction uses that phrase and does not put the integer in the paragraphs read. Opportunistic traders are everyone else. Labels are assigned at the start of each calendar year from past history only, then applied to subsequent trades.
- About 55% of trades are routine and about 45% opportunistic under their split.
- A portfolio long opportunistic buys and short opportunistic sells earns value-weight abnormal returns of 82 basis points per month (9.8% annualized, t = 2.15) and equal-weight abnormal returns of 180 basis points per month (21.6% annualized, t = 6.07).
- The same construction on routine trades earns value-weight −20 basis points per month (t = −0.57) and equal-weight 43 basis points (t = 1.73).
- More than half the improvement versus routine comes from opportunistic *sales*, which is their contrast with the older "sales don't work" result.
- Abnormal returns keep rising for about six months after the opportunistic month and then flatten. They do not report a reversal.
- A one-standard-deviation increase in the count of opportunistic buys predicts +35 basis points of abnormal return the next month (t = 4.56). The same increase in opportunistic sells predicts −29 basis points (t = 4.97). Routine counts do essentially nothing.
- The opportunistic-versus-routine gap holds in large and small stocks, heavy and light trading, and inside and outside blackout windows, in the robustness section they summarize.

The year-count cutoff that turns "a certain number of years" into code sits in the section that defines the classification. This pass read the definition in words and did not copy an integer out of a table. Implementation must take that integer from the paper, not invent one.

## 3. Why it works — mechanism & evidence

**Mechanism.** Insiders trade for liquidity, diversification, and bonus-month stock plans, and they also trade because they know something. A purchase every March for a decade is a plan. A purchase in a month that person has not used is the residual, and the residual carries the forecast. The count effect says agreement across opportunistic insiders is more informative than a single print.

**Limits they already flag.** Value-weight results are much smaller than equal-weight results, so a large-cap book should expect something closer to 82 basis points than to 180, and that is before the modern two-business-day Form 4 regime, which is faster than the 10-day month-end rule in their sample. Faster disclosure can shrink the edge. Their sample ends in 2007.

**Synthesis.** The usable signal is the opportunistic purchase, observed when the form is public, sized with the count, and not mixed with routine selling plans.

## 4. The twist: INS-R

1. **Filing clock.** Enter the next session after the Form 4 *filing* timestamp, never the trade date. Their own data section says the market did not have to know until days after the month. Using the trade date is look-ahead relative to the rule that produced their t-statistics.
2. **Long purchases only.** The short side of opportunistic sales is real in their tables and is a separate book. This specification does not borrow stock against an insider sale. The sales result is recorded so it is not forgotten; it is not silently added.
3. **Cluster.** Require at least two distinct opportunistic insiders with open-market purchases filed in the same firm over a rolling 21 calendar days. Their count regression says the number matters. One lone Form 4 is the weak end of that regression.
4. **Routine exclusion is per insider, recomputed each January from prior years only.** A March purchase by someone whose history is March is not opportunistic because the stock is "cheap."
5. **One-month hold from the entry session.** They show drift out to six months. The one-month hold is the horizon of the monthly portfolio they actually tabulate. Extending to six months is a second experiment with a pre-declared overlap rule, not a free upgrade.

## 5. Full specification of the twist variant

**Universe.** US common stocks, price at least $5, market cap at least $300 million, average daily dollar volume at least $2 million. Point-in-time. No OTC.

**Data.** Form 4 filings with insider identifier, transaction code (open-market purchase only), transaction date, filing timestamp, and share count. CRSP-style returns including delistings. A blackout calendar is *not* a filter; they say the result survives blackouts, so dropping them would be a different strategy.

**Signal.** At each January, label each insider routine or opportunistic from their own prior filings using the paper's year-count rule once that integer is copied from Section III. A name enters when two such opportunistic purchase filings arrive inside 21 days.

**Entry.** Next regular open after the second filing's public timestamp.

**Exit.** Close at the open 21 trading days later. Exit early on a delisting at the delisting return. No discretionary "thesis break."

**Sizing.** Equal weight, max 25 names, 4% of equity each. If more than 25 qualify, keep the 25 with the largest count of opportunistic buying insiders, tie-break by smaller market cap (their equal-weight edge is the small-cap one; this tie-break makes that explicit rather than accidental).

**Costs.** 10 basis points per side base, 25 basis points stress. Impact matters more on the small names that dominate equal-weight results.

**Parameters.** Cluster window {10, 21, 42} calendar days and minimum insiders {2, 3} are the plateau. The routine year-count is not a search target; it is taken from the paper.

## 6. Failure modes & regime dependence

10b5-1 plans and option-related selling disguised as open-market codes. Cluster buying into a secondary offering. A filing backlog that releases many forms on one date and creates a false cluster. Post-2007 disclosure speed. Equal-weight results that die once a $300 million floor and 25 basis point costs are applied. Early warning: the gap between opportunistic and routine purchase returns in a rolling three-year window compresses toward zero.

## 7. Validation protocol

**No local backtest exists.**

- **Point in time.** Insider labels at 1 January use filings dated before that day. Entry uses the filing timestamp. Returns use the open after that timestamp.
- **Splits.** Train labels and costs on 1996–2007 (their sample, contaminated by the paper). Validation 2008–2016. Holdout 2017 onward, unread.
- **Baseline.** All insider purchases with no routine split, same cluster and hold. The twist has to beat that naive book after costs. Also report routine-only purchases, which they say should be flat.
- **Acceptance.** Validation net monthly alpha versus the market, value-weight as a check and equal-weight as the spec, t-statistic at least 2 on the equal-weight book after 25 basis point costs, and the value-weight book not negative. If only the equal-weight micro-cap residue works, the $300 million floor has failed and the strategy is rejected rather than quietly lowered.

## 8. Sources read (annotated)

1. **Cohen, Malloy, and Pomorski, NBER WP 16454, October 2010.** https://www.nber.org/system/files/working_papers/w16454/w16454.pdf — fetched 2026-10-07. Read the introduction through the data section's opening, including the portfolio numbers and the count regression. *Not read line by line:* the full robustness tables. The "certain number of years" phrase is theirs; the integer was not copied in this pass.
2. **Journal of Finance 2012 version.** Citation confirmed on the NBER page. The JF PDF was not the file read; the NBER working paper was.

## 9. Further reading

- Jeng, Metrick, and Zeckhauser (2003) on purchases versus sales. Not fetched.
- Jagolinzer (2009) and Sen (2008) on 10b5-1 plans, which they discuss. Not fetched.
- The JF 2012 section that states the exact year-count. Required before code is written.
