# 07. Commodity Futures Basis — Twist: CURVE-B

> **Library:** Sigmatiq Strategy Library V3 | **Bucket:** Portfolio / macro | **Style:** Curve, not trend
> **Instruments:** Collateralized commodity futures | **Typical holding period:** One month, rolled | **Complexity (1–5):** 3 | **Evidence grade (A–C):** B+
> **Status:** Research document. Figures are Gorton, Rouwenhorst, and coauthors'. None are Sigmatiq backtests.

This is not a managed-futures trend system and not a risk-parity sleeve that happens to contain a commodity ETF. The decision variable is the slope of the futures curve.

## 1. Origin & lineage

**Gary Gorton and K. Geert Rouwenhorst, "Facts and Fantasies about Commodity Futures," Financial Analysts Journal 62 (2006).** The text read for the update is **Bhardwaj, Gorton, and Rouwenhorst, NBER working paper 21243, June 2015, "Facts and Fantasies about Commodity Futures Ten Years Later,"** which restates the 2006 construction and extends the sample through December 2014.

The economic role they assign the investor is the insurance counterparty. Producers hedge. The futures investor holds that price risk and posts collateral.

## 2. The original evidence (as published)

From the 2015 NBER paper, read 2026-10-07. The index is the equally weighted, fully collateralized portfolio from the 2006 paper, rebalanced monthly. Construction details of the roll sit in the 2006 paper; this pass did not re-read that PDF line by line, and the 2015 paper says the construction is unchanged.

Risk premium, annualized from monthly returns (their Table 3):

| Window | Commodity futures | Stocks | Bonds |
| --- | --- | --- | --- |
| 1959-07 to 2004-12 | 5.23% (t = 2.92), vol 12.10%, Sharpe 0.43 | 5.65%, Sharpe 0.38 | 2.22%, Sharpe 0.26 |
| 1959-07 to 2014-12 | 4.95% (t = 2.90), vol 12.71%, Sharpe 0.39 | 5.91%, Sharpe 0.40 | 2.93%, Sharpe 0.33 |
| 2005-01 to 2014-12 | 3.67% (t = 0.76), vol 15.23%, Sharpe 0.24 | 7.09%, Sharpe 0.48 | 6.17%, Sharpe 0.56 |

The out-of-sample commodity premium is lower, and the difference versus 1959–2004 is not significant (t = −0.35). It is also not significant versus zero in that decade (t = 0.76). They say ten years is not enough to call the premium dead, and that part of the drop is the collateral yield in a low-rate decade, not the futures excess alone.

**Basis, their definition, read from Section 3.** If F1 is the front futures price and F2 the next, basis = [(F1 − F2) / F1] × 365 / (T2 − T1), with T in days. A positive basis is backwardation (front above the next). They distinguish this observable slope from "normal backwardation," which is the unobservable gap between the futures price and expected future spot. Scarcity of inventories bids the spot and the front up relative to later contracts. They state that the basis has been reliably correlated with the cross-section of futures risk premiums, and they point to Fama and French (1987) and Erb and Harvey (2006) for that link. This pass did not extract a long-short Sharpe from their basis table. The specification below therefore does not quote one.

## 3. Why it works — mechanism & evidence

**Mechanism.** Backwardation is a convenience yield: holders of the physical commodity will not lend it cheaply when stocks are tight. The long futures position in a scarce commodity is paid, via the roll, for insuring the producer. Contango is the opposite: the market pays to store a surplus, and the long pays that storage. Sorting on the slope is a bet on scarcity, not on the recent price change.

**What the equal-weight index is not.** It is a long-only insurance portfolio. It was paid about the same as equities from 1959 to 2004 in their table, with a low correlation to stocks and bonds and a positive correlation to inflation (the inflation claim is in their introduction and was not re-tabulated here). The 2005–2014 decade paid less and was noisier. A trend overlay on the same markets is a different strategy and is already specified elsewhere in this repo; it is not added here.

**Synthesis.** Hold collateralized futures, prefer backwardated markets, and do not describe the 1959–2004 Sharpe as the expected Sharpe of the next decade. Their own out-of-sample t-statistic will not support that.

## 4. The twist: CURVE-B

1. **Cross-section, not the index.** Each month, rank the eligible commodities on the basis formula above, using prices known at the roll decision. Long the top half (more backwardated), flat the bottom half. No shorts in the first book: a short in a scarce commodity is the opposite of the insurance they describe, and it needs a separate test.
2. **Equal risk, not equal dollars.** Size each long so that trailing 63-day futures volatility contributes the same ex-ante volatility. The 2006 index is equal-weighted and therefore lets a wild market dominate. This change is ours.
3. **Collateral is T-bills, reported separately.** Total return = futures excess + collateral. Do not mix them into one "Sharpe" and then compare it with an uncollateralized equity number. Their Table 3 risk premiums are excess returns; keep that definition.
4. **No trend filter.** A commodity can be in contango and trending up, or backwardated and trending down. Adding a moving average turns this into the trend system this library is not rewriting.
5. **Roll on the calendar they imply.** Hold the nearest contract that will not expire during the next month, and roll on a fixed day. Do not roll on a day chosen because it backtests well.

## 5. Full specification of the twist variant

**Universe.** The liquid set that can actually be rolled: WTI crude, Brent, heating oil, gasoline, natural gas, gold, silver, copper, corn, wheat, soybeans, soybean oil, sugar, coffee, cotton, live cattle, lean hogs. A name enters only after it has 36 months of front and second prices. No commodity ETFs in the first test; ETF roll methodology is a different instrument.

**Data.** Settlement prices of the front two contracts, expiration dates, point values, and a T-bill total-return series for the collateral. Signals use settlements. Fills use the next session's settlement plus a slippage assumption, so the signal settlement is not the fill.

**Signal.** Basis as defined above. Long if the commodity's basis is at or above the cross-sectional median that month. Weights proportional to 1 / vol_63, renormalized to a 10% ex-ante portfolio volatility using the trailing covariance of the selected names. If the covariance is short, use a diagonal matrix and say so.

**Rebalance.** Monthly, on the first business day. Positions are the next contract that survives the "will not expire this month" rule.

**Risk.** Ex-ante vol target 10%. Gross notional of futures can exceed equity; collateral stays in T-bills at 100% of face. No borrowing. If a limit move prevents the roll, flag the day and fill the next session.

**Costs.** 1 tick per roll as the base, 2 ticks as the stress, plus exchange and commission. Report roll count. Natural gas and hogs will dominate costs; show results with and without them.

**Parameters.** Median split is the rule. A top-quartile variant is a robustness check, not the spec. Vol lookback {42, 63, 126} is the plateau.

## 6. Failure modes & regime dependence

A decade like 2005–2014, where the average premium's t-statistic was 0.76. Financialization: index investors all long the front month can flatten the basis that the sort needs. Limits and squeezes in softs. Using a total-return ETF as a proxy and attributing the ETF's roll to this formula. Early warning: the median basis of the "long" half stays negative for a year, which means the book is long contango and calling it a scarcity book.

## 7. Validation protocol

**No local backtest exists.**

- **Splits.** The 1959–2004 window is their discovery sample. The 2005–2014 window is their published out-of-sample check of the *index*, not of this long-only basis sort; treat 2005–2014 as validation for the sort, and hold out 2015 onward.
- **Baseline.** Their equal-weight collateralized index, same universe, same costs. The sort has to beat the index on excess return per unit of volatility after 2-tick rolls. If it only wins by dropping natural gas after the fact, reject.
- **Pitfalls.** Filling at the signal settlement. Back-adjusting the curve so the basis uses a stitched price. Survivorship of commodities that stopped trading.
- **Acceptance.** Validation excess Sharpe at least 0.2 above the equal-weight index, and the 2015+ holdout excess return not negative. A failure to beat the index means the sort is not earning its complexity and the index itself remains the thing to test, not this twist.

## 8. Sources read (annotated)

1. **Bhardwaj, Gorton, and Rouwenhorst, NBER WP 21243, June 2015.** https://www.nber.org/system/files/working_papers/w21243/w21243.pdf — fetched 2026-10-07. Read the abstract, introduction, Table 3, and the basis definition in Section 3. *Taken:* the three-window risk premiums and Sharpes, the t-test on the out-of-sample difference, and the basis formula. *Not taken:* a numerical long-short basis premium, which was not copied out of a later table.
2. **Gorton and Rouwenhorst, FAJ 2006.** A PDF was fetched (Wharton faculty copy) during the search. This note relies on the 2015 paper's restatement of that index rather than a second pass through the 2006 tables.

## 9. Further reading

- Fama and French (1987) and Erb and Harvey (2006) on the basis and the risk premium. Cited by the 2015 paper. Not fetched this pass.
- The 2006 paper's appendix on roll construction. Required before the backtest is coded.
