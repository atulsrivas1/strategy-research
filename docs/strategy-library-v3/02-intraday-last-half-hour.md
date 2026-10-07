# 02. Last-Half-Hour Market Momentum — Twist: IHM-A

> **Library:** Sigmatiq Strategy Library V3 | **Bucket:** Intraday | **Style:** Time-series momentum, one bar
> **Instruments:** SPY first; other broad ETFs only as a pre-declared replication set | **Typical holding period:** 15:30–16:00 ET, flat at the close | **Complexity (1–5):** 2 | **Evidence grade (A–C):** B
> **Status:** Research document. Figures are Gao, Han, Li, and Zhou's claims. None are Sigmatiq backtests.

An earlier note in this repo mentions this paper as a cousin of opening-drive scalping. That note never specified this trade. This document is the trade: hold the sign of the morning return into the last half hour, and only that.

## 1. Origin & lineage

**Lei Gao, Yufeng Han, Sophia Zhengzi Li, and Guofu Zhou, "Market intraday momentum," Journal of Financial Economics 129 (2018), 394–414.** Working paper dated 19 June 2017; published version received 20 June 2017. They use TAQ trades in SPY from 1 February 1993 through 31 December 2013, dropping days with fewer than 500 trades.

The question is not cross-sectional stock momentum (Jegadeesh and Titman) and not twelve-month time-series momentum (Moskowitz, Ooi, Pedersen). It is whether the market's own first half hour predicts its own last half hour on the same day.

## 2. The original rules (as published)

They do not hand a broker a checklist. The tradable version is in their economic-value section, and it is simple:

- Thirteen half-hour returns. `r1` runs from the prior cash close (16:00 ET) to 10:00 ET, so it includes the overnight. `r13` is 15:30–16:00. `r12` is 15:00–15:30.
- Predictive regression: `r13 = a + b * r1 + e`. Slope on `r1` is 6.94 (scaled by 100), significant at 1%, in-sample R-squared 1.6%. Adding `r12` raises R-squared to 2.6%.
- Out-of-sample R-squared is 1.4% with `r1` alone and 2.0% with `r1` and `r12`.
- A sign rule: go with the sign of `r1` over the last half hour. They report an average return of 6.67% per annum, standard deviation 6.19%, Sharpe ratio 1.08. A daily buy-and-hold of the same ETF in their comparison has average return 6.04%, standard deviation 20.57%, Sharpe 0.29.
- A mean-variance investor with risk aversion 5 earns a certainty-equivalent gain of 6.02% per annum from `r1`, and 6.18% if `r12` is added. These are the authors' calculations on 1993–2013.
- Predictability is stronger on high first-half-hour volatility (R-squared 3.3% with both predictors), high volume, recession days, and days with major macro releases (they list Michigan sentiment, GDP, CPI, and FOMC minutes).
- They say the result survives "reasonable" transaction costs after decimalization, and that it shows up in ten other active ETFs. The internet appendix, which this pass did not read, is where the futures and cash-index variants sit.

## 3. Why it works — mechanism & evidence

**Mechanism, as they state it.** Two stories, both consistent with the regression. Bogousslavsky (2016): some institutions rebalance in the first half hour and others, or the same institutions, finish in the last half hour, in the same direction. Late-informed trading: anyone who is slow to process the overnight news prefers the liquid last half hour and does not want the overnight gap. Both predict that `r13` has the same sign as `r1`.

**What would reject it.** A last-half-hour return that is unrelated to `r1` once costs and the bid-ask bounce at 15:30 and 16:00 are modeled. A result that exists only in the 2008 window, which they partially address by saying `r1` is significant in and out of the crisis while `r12` is mostly a crisis fact. This pass did not re-read their subperiod table line by line; that sentence is from their introduction, which was read.

**Synthesis.** The published edge is a once-a-day, thirty-minute position in the most liquid ETF in the country. That is why costs matter more than the R-squared looks. One round trip every day will eat a 1-cent edge. Their Sharpe of 1.08 is an author claim on a sample that ends in 2013.

## 4. The twist: IHM-A

1. **Agreement gate.** Trade only when `r1` and `r12` have the same sign. They show `r12` adds fit, and they also show `r12`'s power is crisis-heavy. Requiring agreement keeps the crisis helper from flipping a morning signal that has already reversed by 15:30.
2. **Macro and volatility are scalers, not excuses to add parameters.** On days in a pre-declared macro calendar (CPI, GDP, Michigan, FOMC) or when first-half-hour realized volatility is in the top training-set quintile, size is 1.0x. Otherwise size is 0.5x. We do not retune the quintile after seeing validation returns.
3. **No overnight hold.** The paper's forecast target is `r13`, which ends at 16:00. Holding through the close into the next `r1` is a different trade (the overnight premium) and is out of scope.
4. **Cost hurdle.** Skip the day if the ETF's quoted spread at 15:29 is wider than the training median of the absolute last-half-hour return. A wide-spread day cannot pay for a 30-minute sign bet.
5. **One instrument.** SPY (or the E-mini, in a separate pre-declared book). No basket of the "ten other ETFs" until SPY has passed the protocol below. Those ETFs are a replication set, not a diversification free lunch inside the first test.

## 5. Full specification of the twist variant

**Universe.** SPY. Optional second book: ES front month, same clock, not mixed into the SPY ledger.

**Data.** One-minute trades or NBBO midpoint. Prior official close. Macro calendar frozen before the test. Days with fewer than 500 trades are dropped, matching them.

**Signals.**

- `r1 = P_10:00 / P_prior_close - 1`
- `r12 = P_15:30 / P_15:00 - 1`
- First-half-hour realized variance from one-minute returns between 9:30 and 10:00.
- Trade sign = sign(`r1`) if sign(`r1`) = sign(`r12`) and `r1` is not zero. Else flat.

**Entry.** At 15:30:00, a marketable limit at the 15:29 NBBO, buying if the sign is positive and selling if negative. If the spread hurdle fails, send nothing.

**Exit.** Flatten with a marketable limit at 15:59, or at the closing auction if that auction is the intended 16:00 print. The research ledger must say which. Do not mix auction fills and continuous fills in one Sharpe number.

**Sizing.** Book volatility target is not used. Notional is 100% of the sleeve on scaler = 1, and 50% on scaler = 0.5. No leverage in the first test. Shorts are allowed because the paper's sign rule is symmetric; locate is not an issue in SPY or ES.

**Risk.** One position. Stop is not discretionary. If the position loses 0.75% from the 15:30 fill before 15:59, flatten. That stop is ours, not theirs; it exists so a halted or news-break last half hour cannot become an unbounded loss. It must be in the costed backtest, and it will mechanically reduce their reported Sharpe.

**Costs.** SPY: 0.5 cent per share per side as the base case, 1 cent as the stress. ES: 1 tick per side plus exchange and commission. Report turnover: this rule can trade about 252 round trips a year.

**Parameters.** Agreement on/off is not a search; agreement is the rule. The volatility quintile is frozen on training data. The stop {0.50%, 0.75%, 1.00%} is a plateau check, not a peak pick.

## 6. Failure modes & regime dependence

A structural break after 2013 is the obvious one: the paper's sample ends then, and this pass did not compute a post-publication result. Decimalization and tighter spreads helped them; a regime of constant last-hour hedging by options dealers can dominate a 30-minute sign. `r12` disagreement days are exactly the days their second predictor says the close is doing something else. The 0.75% stop will fire on event spikes and should be reported as a separate exit reason, not buried in the average.

## 7. Validation protocol

**No local backtest exists.**

- **Clock.** Decision time is 15:30 using prices known at 15:30. `r1` uses the prior close and the 10:00 print. No same-bar high.
- **Splits.** Train through 2007, validation 2008–2013 (their published sample, already mined by the authors — treat it as contaminated), holdout 2014 to the latest complete year, unread until the rule above is frozen. A pass on 2008–2013 alone is not acceptance.
- **Baseline.** Flat, and buy-and-hold SPY over the same days, and the unsigned version (always long the last half hour). The sign rule has to beat always-long after costs.
- **Acceptance.** Holdout Sharpe of the daily last-half-hour PnL, annualized with 252, at least 0.5 net of the 1-cent stress, with at least 500 trades, and positive in more than half of holdout years. If the edge is only the 2020 window, reject.

## 8. Sources read (annotated)

1. **Gao, Han, Li, and Zhou, JFE 2018.** Fetched 2026-10-07 from the court-listener copy of the published PDF: https://storage.courtlistener.com/recap/gov.uscourts.nysd.590344/gov.uscourts.nysd.590344.161.2.pdf . Read the abstract, introduction, data section, and the start of the predictive-regression section. *Taken:* sample window, return definitions, R-squared figures, the sign-rule Sharpe comparison, the certainty-equivalent figures, and the two mechanisms. *Not read this pass:* the internet appendix and every subperiod table.

## 9. Further reading

- Bogousslavsky (2016) infrequent-rebalancing model. Not fetched.
- Any post-2013 replication. Not fetched. Required before the holdout is interpreted, and not a reason to peek at the holdout early.
