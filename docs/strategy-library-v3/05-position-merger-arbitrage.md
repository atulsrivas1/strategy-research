# 05. Merger Arbitrage, Calendar Time — Twist: MNA-D

> **Library:** Sigmatiq Strategy Library V3 | **Bucket:** Position, deal life | **Style:** Event / risk arbitrage
> **Instruments:** Announced US cash mergers; stock-for-stock deals only in a hedged sleeve | **Typical holding period:** From the day after announcement until completion or break | **Complexity (1–5):** 4 | **Evidence grade (A–C):** A-
> **Status:** Research document. Figures are Mitchell and Pulvino's. None are Sigmatiq backtests.

This is not a pairs trade and not a generic event-drift book. The position is the deal spread, held in calendar time, with an explicit bet that the merger closes.

## 1. Origin & lineage

**Mark Mitchell and Todd Pulvino, "Characteristics of Risk and Return in Risk Arbitrage," Journal of Finance 56 (2001), 2135–2175.** They build a calendar-time risk-arbitrage portfolio (they call it RAIM) from 4,750 cash mergers, stock mergers, and cash tender offers, 1963–1998, and they check it against active risk-arbitrage hedge funds from 1990–1998.

The practitioner lineage is the merger desk: buy the target at a discount to the offer, and if the offer is stock, short the acquirer in the exchange ratio. They are explicit that earlier academic numbers, often above 100% annualized, came from annualizing a few days of event time and assuming the book could be fully invested in those few days forever.

## 2. The original rules (as published)

Read from the journal PDF on 2026-10-07:

- **Cash deal.** Buy the target. Profit if it is delivered at the offer. Dividends on the target are a secondary source.
- **Stock deal.** Buy the target and short the acquirer. Profit sources: the spread, the dividend differential, and, for institutions, interest on the short proceeds. They note that a retail short often earns zero rebate.
- **Primary risk.** The deal breaks. In their Figure 1, the median spread on deals that ultimately fail stays wide and then jumps from about 15% to more than 30% on the termination day. Successful deals grind tighter into the completion date.
- **Calendar time, not event time.** They simulate a portfolio that is only in a deal while the deal is alive. They give the Zycon example (December 1996): a three-day competing-bid gain of 9.5% annualizes to 1,903%, which is not a return a book can earn continuously.
- **Payoff shape.** In flat and rising markets their RAIM portfolio earns about 50 basis points per month (about 6.2% annualized) over the risk-free rate with a market beta near zero. In months when the market falls 4% or more, beta rises to about 0.50. They describe the payoff as similar to writing uncovered index puts.
- **Excess return after the right model.** A contingent-claims adjustment with no costs implies about 10.3% excess a year, which is *higher* than their CAPM alpha of about 9.25%, not lower. After transaction costs and practical limits, the same adjustment implies about 4% a year. Their conclusion: the large alphas in earlier papers are mostly costs and event-time annualization, and the remaining 4% is what is left once the put-like downside is acknowledged.
- Hedge-fund returns, 1990–1998, show the same nonlinear shape. They also warn, citing Fung and Hsieh, that hedge-fund databases have survival bias.

## 3. Why it works — mechanism & evidence

**Mechanism.** The spread is payment for bearing a jump loss if the deal breaks, and for supplying a bid when the target holder wants out. In ordinary markets that jump is idiosyncratic. In a falling market the acquirer's willingness and financing both deteriorate, so the jumps arrive together. Shleifer and Vishny (1997), whom they cite, add the funding channel: outside capital leaves the strategy in the drawdown, which is when the spread is widest.

**What the 4% is not.** It is not a reason to lever the book as if beta were always zero. The months that produce the 0.50 beta are the months that matter.

**Synthesis.** Run the book in calendar time, charge real borrow and commissions, and cut new risk when the market is already in the left tail they measured.

## 4. The twist: MNA-D

1. **Cash core, stock sleeve.** The core book is cash deals only: long the target, no short. Stock deals are allowed only with the short hedge on at the announced ratio, and they are capped at one-third of gross. A "long the target in a stock deal" position is not merger arbitrage; it is equity beta plus a spread.
2. **Downside gate.** Add no new deals in a month after the trailing 21-day market return is −4% or worse, matching the threshold where their beta jumps. Existing deals are held to completion or break; the gate stops fresh risk, it does not force a fire sale into the widest spreads.
3. **Loss bound.** At entry, if the downside to a plausible break (they show spreads blowing from ~15% to ~30%) would cost more than 0.50% of equity, cut the shares until it does not. The spread collected is not the risk; the break is.
4. **No event-time marketing.** Report monthly book returns on capital deployed and on total equity. A three-day 9% deal is a three-day 9% deal.
5. **Rebate honesty.** Do not credit interest on short proceeds unless the account actually receives it. They separate retail (often zero) from institutional (near the risk-free rate).

## 5. Full specification of the twist variant

**Universe.** US public targets, offer price at least $5, announced definitive or tender offer. Skip rumored deals. Skip deals with an unhedgeable non-traded acquirer if the consideration is stock.

**Data.** Announcement date and time, consideration type, offer terms, completion and break dates, target and acquirer prices, dividend calendar, borrow fee. Point-in-time: a deal enters the book the session after the announcement is public.

**Entry.** Next open after the announcement session, if the gate is open and the spread is at least 1% (cash) or 2% (stock, after the hedge). Spread = (offer − target) / target for cash. For stock, offer is the ratio times the acquirer price.

**Exit.** Completion: deliver into the offer. Break: exit at the next open after the termination announcement. Also exit if the spread goes negative by more than 1% (the market is pricing a topping bid; staying is a different bet). No "average down" after a break.

**Sizing.** Each deal's break-loss cap is 0.50% of equity, as above. Max 20 deals. Gross long cap 100% of equity. Stock-sleeve shorts do not count as extra long risk beyond the spread, but borrow cost is charged daily.

**Costs.** Commission 5 basis points per side, plus half the spread on entry and on a break exit. Borrow fee as quoted; if unknown, assume 50 basis points a year and stress at 300. No short rebate unless the book is institutional, and then only the rate the prime broker posts.

**Parameters.** Market-gate threshold {−3%, −4%, −5%} and minimum entry spread {0.5%, 1%, 2%} are the plateau. The 0.50% break-loss cap is a risk limit, not a searched alpha parameter.

## 6. Failure modes & regime dependence

A cluster of breaks in a −4% month, which is the feature, not a bug: the gate reduces new entries and does not erase deals already on. Financing deals in 2008-style credit freezes. Antitrust delays that turn a 30-day spread into a one-year position with the same dollars of risk. Revised offers that look like alpha and are actually a new deal; reset the spread and the risk cap rather than keeping the old size. Early warning: average entry spreads compress below 1% while deal count stays high, which means the book is being paid nothing for the put it is short.

## 7. Validation protocol

**No local backtest exists.**

- **Ledger.** Monthly return on equity and on deployed capital, separately. Deal count, fraction of months in the −4% regime, and break rate.
- **Splits.** Their 1963–1998 sample is contaminated. Validation 1999–2012. Holdout 2013 onward.
- **Baseline.** Cash-only, always invested, no downside gate, same costs. The twist has to improve the left tail (worst 5% of months) without giving up the entire 4% they attribute to the costed strategy. Beating them on Sharpe by hiding in cash is not success; report time in the market.
- **Pitfalls.** Event-time annualization. Dropping broken deals. Using the completion price on names that delisted for other reasons. Assuming yesterday's borrow.
- **Acceptance.** Validation annualized excess over T-bills at least 2% after the stress borrow, worst month better than −8%, and beta in up months below 0.2. A strategy that is flat because the gate is always shut fails.

## 8. Sources read (annotated)

1. **Mitchell and Pulvino, JF December 2001.** https://andreisimonov.com/N4106/pdf/MitchellPulvinoJFDec2001.pdf — fetched 2026-10-07. Read the abstract pages, the investment-description section, the review of prior event-time studies including the Zycon example, and the piecewise-beta discussion. *Taken:* the 4,750-deal sample, the 50 bp / 6.2% / beta 0.50 at −4% facts, the 10.3% versus 4% cost split, and the spread behavior on breaks. *Not read line by line:* every table in Sections V and VI.

## 9. Further reading

- Baker and Savasoglu (2002), whom they cite at about 1% per month. Not fetched.
- Shleifer and Vishny (1997) on forced liquidation of arbitrageurs. Not fetched.
- A post-2001 deal database with borrow fees. Required for the validation, and not a substitute for their calendar-time result.
