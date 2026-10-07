# 06. Post-Spinoff Drift — Twist: SPIN-T

> **Library:** Sigmatiq Strategy Library V3 | **Bucket:** Position, up to two years | **Style:** Corporate-event drift
> **Instruments:** US parents and the spun-off common stock, after a completed tax-free spinoff | **Typical holding period:** 12–24 months from the distribution | **Complexity (1–5):** 3 | **Evidence grade (A–C):** B
> **Status:** Research document. Figures are Cusatis, Miles, and Woolridge's. None are Sigmatiq backtests.

This is not a buyout-rumor momentum trade and not Greenblatt's magic-formula screen. The event is a completed distribution of a subsidiary's shares, and the paper's own result is that the subsequent abnormal return sits in the names that later get taken over.

## 1. Origin & lineage

**Patrick J. Cusatis, James A. Miles, and J. Randall Woolridge, "Restructuring through spinoffs: The stock market evidence," Journal of Financial Economics 33 (1993), 293–311.** Sample: spinoffs from 1965 through 1988. They measure returns of the spinoff, the parent, and a value-weighted combination for up to three years after the distribution.

Earlier papers they cite (Hite and Owers 1983, Schipper and Smith 1983, Miles and Rosenfeld 1983) measure the parent's announcement return only. Cusatis, Miles, and Woolridge ask what happens after the shares actually trade.

## 2. The original findings (as published)

Read from the JFE PDF on 2026-10-07:

- Significantly positive abnormal returns for spinoffs, parents, and the combinations, out to three years.
- Both spinoffs and parents are taken over more often than control firms. The abnormal performance is limited to the firms that are later taken over. Firms that are not taken over do not carry the result.
- For the 18 parent firms that were taken over, mean matched-firm abnormal returns are 42.8%, 56.9%, and 69.6% over months 1–12, 1–24, and 1–36, significant at the 1% level in their tests. The 113 parents not taken over have much smaller figures; only the 24-month mean is significant, and only at the 10% level.
- They interpret the spinoff as a cheap way to move assets to a bidder who will pay more than the parent could realize inside the conglomerate.
- They are strict about the word "spinoff." Taxable distributions, partial stakes, split-offs, and equity carve-outs are different transactions. Their examples of a clean distribution include Kraft's Premark distribution and General Mills' 1985 spinoffs of Kenner Parker and Crystal Brands. Reasons management gives: no strategic fit, regulation, undervaluation of the sum of the parts, or a volatile subsidiary.

They do not publish a monthly rebalance rule, a size filter, or a costed portfolio Sharpe.

## 3. Why it works — mechanism & evidence

**Mechanism.** A subsidiary inside a conglomerate is hard to buy. Once it has its own ticker, a bidder can buy it without buying the rest of the parent. The announcement return capitalizes some of that, but not the bids that arrive one or two years later. Hence a drift that is really a takeover drift, visible only in hindsight among the names that receive a bid.

**The hindsight problem.** "Limited to firms involved in takeover activity" means a backtest that keeps only the names which later receive a bid is not a strategy. At purchase time the bid is unknown. The tradable rule is to buy the spinoff universe and accept that the average is a mix of bids and duds. Selecting ex post is how the table was built, not how the book is run.

**Age of the sample.** 1965–1988. The takeover market, tax law under Section 355, and the amount of event capital have all changed. This pass did not read a post-1988 replication.

**Synthesis.** Buy completed spinoffs, hold long enough for a bid to show up, and do not pretend the 69.6% figure is the expected return of the average name.

## 4. The twist: SPIN-T

1. **Tax-free full distribution only.** Match their clean definition: parent distributes at least 80% and does not keep control. Carve-outs, split-offs, and taxable dumps are excluded at the corporate-action record, not after seeing returns.
2. **Buy both, do not pick the winner.** Equal dollars in the parent and the spinoff at the first date both have a tradable close after the distribution. Their combination portfolio is the object. Dropping the parent because "the alpha is in the child" uses a split they did not find; both sides have the takeover effect.
3. **No ex-post takeover filter.** Hold every name that qualifies. Report the later takeover rate as a diagnostic, never as an entry rule.
4. **Two-year cap.** They show one-, two-, and three-year windows. The specification holds 24 months, which is where their parent takeover abnormal return is already large (56.9% in the taken-over subset) without requiring the third year of dead money in the names that will never get a bid. The 24-month choice is a horizon, and the 12- and 36-month alternatives are the plateau, not a search over exit rules fitted to winners.
5. **Liquidity and junk filter.** Price at least $5 and market cap at least $200 million at the first trade date, on both legs. Their 1965–88 sample includes names a modern book cannot trade. This filter will lower the raw return relative to the paper. That is intended.

## 5. Full specification of the twist variant

**Universe.** US parent and spinoff, both listed, both passing the price and size filter. If either leg fails, skip the pair. No ADRs.

**Data.** Distribution date, tax status, percent distributed, first tradable prices, delisting reason. A name acquired inside the hold is a successful exit at the offer, not a missing return.

**Entry.** First session on which both legs have traded for a full day. Buy the close, or the next open; pick one and keep it. Equal dollars.

**Exit.** 24 months later, at the close. If a leg is acquired, that leg exits on the offer terms and the cash stays in T-bills until the horizon. The other leg is not automatically sold. If a leg is liquidated for no value, the return is −100% on that leg.

**Sizing.** Each pair is 4% of equity (2% each leg). Max 15 pairs. Cash if fewer qualify. No leverage.

**Costs.** 15 basis points per side. Spinoffs are often thin in week one; stress at 40 basis points and with a rule that refuses the pair if day-one dollar volume is under $1 million on either leg.

**Parameters.** Horizon {12, 24, 36} months. Size floor {$100 million, $200 million, $500 million}. Tax-free requirement is not relaxed in the search.

## 6. Failure modes & regime dependence

A dead takeover market (the entire mechanism). Section 355 tax changes that reduce supply or change who spins. Buying the announcement pop instead of the distribution, which double-counts the event study they say is incomplete. Parents that spin off a liability. Early warning: the rolling five-year rate of subsequent bids in the book falls toward the rate of a size-matched control, which is the paper's own null.

## 7. Validation protocol

**No local backtest exists.**

- **Control.** For every pair, a size-and-industry match that did not spin off, held the same 24 months. The paper's claim is abnormal to a match, not raw return.
- **Splits.** 1965–1988 is their sample and is contaminated. Validation 1989–2009. Holdout 2010 onward.
- **Do not drop non-acquired names.** Report the acquired subset separately and labeled as conditional, not as the strategy.
- **Acceptance.** Validation matched abnormal return positive with t at least 2 after 40 basis point costs, and at least 40 pairs. A result that exists only inside the acquired subset fails.

## 8. Sources read (annotated)

1. **Cusatis, Miles, and Woolridge, JFE 1993.** https://longrunplan.com/wp-content/uploads/2018/09/restructuring-through-spinoffs.pdf — fetched 2026-10-07. Read the abstract, introduction, the definitional discussion of what counts as a spinoff, and the parent-firm takeover split including the 18-versus-113 counts and the 42.8% / 56.9% / 69.6% matched-firm figures. *Not read line by line:* every monthly-return table for the spinoff leg.

## 9. Further reading

- Hite and Owers (1983), Schipper and Smith (1983), Miles and Rosenfeld (1983), announcement-window studies. Not fetched.
- A post-1988 spinoff census with tax status. Required for the validation sample.
