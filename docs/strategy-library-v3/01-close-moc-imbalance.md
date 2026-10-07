# 01. Closing-Auction Imbalance Fade — Twist: MOC-L

> **Library:** Sigmatiq Strategy Library V3 | **Bucket:** Close / overnight | **Style:** Liquidity-pressure reversal
> **Instruments:** US listed common stocks with a published closing imbalance | **Typical holding period:** From the published imbalance until the next regular open | **Complexity (1–5):** 3 | **Evidence grade (A–C):** B-
> **Status:** Research document. Performance figures below are the authors' claims from the papers cited. None are Sigmatiq backtests.

This note does not respecify opening-drive scalping, opening-range breakout, or cross-venue latency arbitrage. Those trades are already written elsewhere. The object here is the published market-on-close imbalance and the overnight reversal that follows it.

## 1. Origin & lineage

**David Cushing (ITG) and Ananth Madhavan (USC), January 2000 working paper "Stock Returns and Trading at the Close."** They study Russell 1000 names with TAQ transactions from June 1997 to July 1998 and the NYSE specialist record of market-on-close (MOC) imbalance indications. The economic user of the close is the indexer and the NAV accountant: portfolio returns, mutual-fund NAVs, and some after-hours crosses are struck off the official close. Their Safeway example (S&P 500 addition, 12 November 1998) is the desk story in one name: the specialist closed the stock at $55, up 11% from the prior trade, and the next regular close was $51.1875.

The mechanism they test is older than the modern electronic closing auction, but it is the same economic object: a one-sided liquidity order that must be filled at the official close, published late, and large relative to a normal day's volume.

## 2. The original evidence (as published)

Read from the working paper, not from a secondary summary:

- The last five minutes explain almost 18% of the variation in *portfolio* daily returns while accounting for 1.3% of trade time. In individual stocks the same window explains about 4%.
- Non-block order flow has a much larger price coefficient than block flow. Average stock, before 15:30: non-block coefficient 7.57 versus block 0.78. In the closing window those coefficients are 10.29 and 2.24.
- Pre-24 June 1998 imbalance publications: 1,910 stock-date events, almost all published on or after 15:50. 1,126 buy imbalances, mean size 13.29% of average daily volume (median 4.30%). 728 sell imbalances, mean 10.59% (median 5.49%).
- On index-expiration days, sell imbalances are followed by positive overnight and next-day returns, and buy imbalances by negative returns. Both are statistically different from zero in their tests. Off expiration, the sign pattern is the same, but only the sell-imbalance follow-through is significant.
- They reject "the order flow just kept going the same way" as the explanation. Their reading is that the close overreacts and the next open is sticky toward that close (they point to Madhavan and Panchapagesan 1999 for the sticky-open fact).

What they do **not** publish is a tradable rule with costs, a position size, or a result after the June 1998 NYSE rule change. The sample ends in July 1998.

## 3. Why it works — mechanism & evidence

**Mechanism.** Passive and expiry flow must print the official close. Market makers and other liquidity providers charge for taking the other side into an overnight inventory. If the imbalance is liquidity rather than information, the premium mean-reverts once the overnight book is free to trade. Cushing and Madhavan separate expiration days precisely because those imbalances are "almost surely liquidity-driven."

**Contradictory / decay evidence, from what was actually read.** The non-expiration buy-imbalance reversal is not significant in their table. The whole sample is one year and one market structure. A later Nasdaq-versus-NYSE closing-auction paper was opened only at abstract level on this pass (temporary impact reverses over roughly 3–5 days in that abstract). That abstract is not a replication of Cushing and Madhavan, and it is not a Sigmatiq result. Modern cutoff clocks, D-quote rules, and floor-broker late orders are a different mechanism and have to be tested as such.

**Synthesis.** The fade is a liquidity-premium trade, and only on days when the imbalance is plausibly non-informational. Treating every modern imbalance print as the 1998 specialist indication is a category error.

## 4. The twist: MOC-L

1. **Liquidity-day gate.** Trade the fade at full size only on index-expiration days and on pre-declared index-rebalance dates. Off those dates, sell imbalances may be traded at half size; buy imbalances are skipped. This follows their own split: expiration reversals are two-sided and significant; off-expiration, only sells are.
2. **Size gate.** Require published imbalance shares / 20-day average daily volume at or above that name's sample median (their medians were about 4–5% of ADV). The mean is pulled by extremes; the median is the tradeable bulk.
3. **Publication clock.** The order may be entered only after the imbalance message timestamp the exchange actually published. Their messages were on or after 15:50. A modern venue with an earlier cutoff uses that venue's clock. Using a print from later in the auction is look-ahead.
4. **Overnight leg only.** Flatten at the next regular-session open. Their next-day open-to-close continuation is a second hypothesis (sticky open), not part of this specification.
5. **Capacity cap.** Shares bought or sold are at most 10% of the published imbalance. The imbalance is the liquidity we are leaning against; we do not become the imbalance.

## 5. Full specification of the twist variant

**Universe.** NYSE and Nasdaq common stocks in the Russell 1000 (or the current large-cap index that publishes a closing imbalance). No ETFs in the first test. One name, one side, one day.

**Data requirements.** Official imbalance messages with exchange timestamp, side, and paired shares; RTH open and close; 20-day ADV; a calendar of index expirations and index reconstitutions built before looking at returns.

**Signal.**

- `imb_pct = published_imbalance_shares / ADV_20`.
- Side: a published buy imbalance is faded by selling; a published sell imbalance is faded by buying.
- Full size if the date is on the expiration or reconstitution calendar and `imb_pct` is at least the training-set median. Half size if it is a non-expiration sell imbalance above the median. Otherwise flat.

**Entries.** Marketable limit in the direction of the fade after the publication timestamp and before the auction cutoff, limit no worse than the last continuous-market mid plus/minus one spread. Unfilled orders cancel at the cutoff. No chase into the auction print.

**Exits.** Exit with a marketable limit at the next regular open. No discretion to "see the open." If the name is halted through the next open, exit at the first print after the halt and flag the trade.

**Position sizing.** Dollar risk is not a stop distance; the risk is the gap from entry to the next open. Cap notional so that a 2% adverse open costs at most 0.25% of book equity on a full-size name and 0.125% on a half-size name. Then apply the 10% of published-imbalance share cap. The tighter of the two binds.

**Risk limits.** Max 15 names per day. Gross overnight notional cap 20% of equity. No single name above 2% of equity. Skip names with a same-day earnings release or a merger announcement; those are information, and the paper's identifying assumption fails.

**Cost model.** Pay the closing spread plus 1 cent of impact on liquid names, and stress at 2x. Auction fees as published by the venue. No assumption of midpoint fills inside the auction.

**Parameters to validate, as a plateau.** Median multiple {0.75, 1.0, 1.5} times the training median of `imb_pct`. Overnight-only versus a forbidden open-to-close add (the add is a separate experiment, not a free parameter of this one).

## 6. Failure modes & regime dependence

Information imbalances (earnings, deal announcements, index *additions* where the demand is permanent) do not revert; the Safeway print itself only partially reverted. A rule change that lets late informed orders join the auction, which Cushing and Madhavan were already watching in June 1998, can turn a liquidity fade into an adverse-selection trade. Expiration-day crowding is the other failure: if every liquidity provider fades the same print, the premium is gone before we can trade. Early warning: the fade's average open-gap shrinks toward zero for a quarter while imbalance sizes stay large.

## 7. Validation protocol

**No local backtest exists.**

- **Data.** Imbalance messages and trades from a vendor that timestamps the publication, not just the auction print. Start no earlier than the modern auction rules of the venue being tested. Do not stitch 1997–98 specialist indications to 2020s electronic auctions and call it one sample.
- **Splits.** Freeze the calendar and the median on a training window. Validation is the next block of years. A final holdout stays unread until the rule is frozen.
- **Costs.** Spread plus 1 cent, then 2x and 3x. Report the fraction of days the limit never fills.
- **Pitfalls.** Using the auction price as both the signal and the fill. Using imbalance updates printed after our decision time. Dropping "bad" expiration days after seeing them. Survivorship in the Russell membership (use point-in-time constituents).
- **Robustness.** Expiration versus non-expiration, buy versus sell, and NYSE versus Nasdaq reported separately. A placebo that fades a random side on the same names should be near zero after costs.
- **Acceptance, declared before any run.** On the validation block, net overnight return per trade positive with a t-statistic at least 2, profit factor at least 1.15 at 2x costs, and the edge not confined to a single expiration quarter. Failure on non-expiration buy imbalances is expected and is not a reason to retune.

## 8. Sources read (annotated)

1. **Cushing and Madhavan, "Stock Returns and Trading at the Close," 18 January 2000.** http://chesler.us/resources/academia/trading_at_the_close.pdf — fetched 2026-10-07. Read the abstract, introduction, the order-flow regression discussion in Section 6, the MOC imbalance results (Sections 6.1–6.3), and the conclusion. *Taken:* the 18% / 1.3% / 4% variance facts, the block versus non-block coefficients, the imbalance counts and ADV ratios, and the expiration versus non-expiration reversal split. *Not taken as a trading system:* they never publish a costed rule.
2. **Closing auctions, Nasdaq versus NYSE** (ScienceDirect abstract page only). https://www.sciencedirect.com/science/article/abs/pii/S0304405X21005092 — abstract read 2026-10-07. Temporary closing impact reverses over a few days in that abstract. Full text not read. Not used as a numerical input to the specification.

## 9. Further reading

- Madhavan and Panchapagesan (1999) on the sticky open. Not fetched.
- The June 1998 NYSE imbalance-rule release. Not fetched.
- Current NYSE and Nasdaq closing-auction specs (cutoff times, D orders, floor-broker late interest). Required before a modern data pull, and not a substitute for the 2000 paper.
