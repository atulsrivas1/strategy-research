# 03. Larry Williams Oops Gap Fade — Twist: OOPS-N

> **Library:** Sigmatiq Strategy Library V3 | **Bucket:** Intraday | **Style:** Opening-gap failure
> **Instruments:** Liquid index futures first (ES, NQ); liquid commodities only as a later replication | **Typical holding period:** From the gap-fill trigger to the next session's first profitable open, often one session | **Complexity (1–5):** 2 | **Evidence grade (A–C):** C+
> **Status:** Research document. No audited performance is cited, because none was read from a primary source. This is not a Sigmatiq backtest.

This is not the overnight-gap continuation rule, and it is not an opening-range breakout. Those fade or follow a gap relative to the prior *close*. Oops fades a gap that has already cleared the prior session's *high or low*, and only if price comes back through that extreme.

## 1. Origin & lineage

**Larry Williams.** The pattern is described in his 1979 book *How I Made One Million Dollars Trading Commodities*. That book was not reproduced here. What was read is a secondary write-up that quotes the rule, plus a later interview that does not restate the pattern but does state his view of when a technical signal is allowed to count.

The name, as the secondary source tells it: a broker calling a stopped-out client says "oops." The trade is the other side of that phone call. A gap looks like strength or weakness. If it cannot hold beyond yesterday's range, the gap side is trapped.

## 2. The original rules (as published in the sources actually read)

From the Traders.com Advantage note that restates Williams, read via search excerpt on 2026-10-07, not from the 1979 book:

- If the session opens below the prior session's low, place a buy stop a few ticks above that prior low.
- If the session opens above the prior session's high, place a sell stop a few ticks below that prior high.
- If price never trades back through the prior extreme, there is no trade. That non-event is part of the rule.

From Andrea Unger's written description of the same setup, also read as a secondary page on 2026-10-07:

- The exit Williams used is the **first profitable open**: stay in the position until a later session opens on the profitable side of the entry, then get out. Unger attributes the reasoning to Williams: the open belongs to the public, the close to the professional, and a profitable open is the time to take the public's mistake off the table.

From Williams's July 1997 *Technical Analysis of Stocks & Commodities* interview with Thom Hartle (excerpt read, full interview page opened via search): a technical buy is not the same trade in a bullish fundamental backdrop and a bearish one. He does not give the Oops rule in the excerpt. The interview is used only for that conditioning statement.

**What is not in any source read here:** a tick offset that is universal, a stop, a market list, or an audited return.

## 3. Why it works — mechanism & evidence

**Mechanism.** The open can overshoot on overnight inventory. Coming back through yesterday's extreme means the overnight crowd could not find a follow-through trade. Stops on the gap side then add to the reversal. The first-profitable-open exit assumes the next open is the emotional print and should not be sat through if it is already a gain.

**Evidence grade is C+ on purpose.** No primary table was read. Unger describes a personal test with a 15-point minimum gap and a monetary stop; those numbers are contract-specific and are not adopted here. A gap-fade that works on a quiet day fails on a macro day, which is why the twist below refuses macro days. That refusal is motivated by the last-half-hour paper in this same library: Gao, Han, Li, and Zhou find *continuation*, not reversal, on major release days. Fading those opens fights their result.

**Synthesis.** Oops is a failed-auction rule with a strange but explicit exit. It is testable. It is not yet evidenced in this file.

## 4. The twist: OOPS-N

1. **ATR gap, not a point gap.** The open must clear the prior extreme by at least 0.15 times the 14-day ATR. A "few ticks" from 1979 does not transfer from pork bellies to the E-mini. The 0.15 figure is a starting plateau point, not a claim that Williams used it.
2. **Do not fade a macro open.** If the date is on a pre-declared CPI, GDP, or FOMC calendar, skip. Those opens are the continuation regime in Gao et al., which was read. Michigan sentiment can be added to that calendar without changing the logic.
3. **Trend filter from Williams's own 1997 remark.** A long Oops (fade a gap down) is allowed only when the prior close is above the 20-day average close. A short Oops is allowed only when the prior close is below it. A buy signal in a falling market is a different trade, and this rule declines it.
4. **Bounded loss.** Stop at the session open. The original rule, as read, has no stop other than the failure to trigger. A trend day that gaps and runs would otherwise be an unbounded position until some future profitable open that may never come.
5. **First profitable open stays.** Exit at the next session's open if that open is better than the entry. If the stop has not hit and two sessions have passed without a profitable open, flatten at that second open. The two-session cap is ours, so a forgotten position cannot become a swing trade by accident.

## 5. Full specification of the twist variant

**Universe.** ES and NQ front month, one signal per market per session. No stocks in the first test: cash equities gap for dividends and auctions, and the 1979 rule was a commodity-session rule.

**Data.** Regular trading hours only for the "session," with the overnight gap measured from the prior RTH high and low to the RTH open. ETH prints do not redefine the prior high and low. ATR(14) on RTH daily bars.

**Signal.**

- Long setup: RTH open < prior RTH low − 0.15 * ATR(14), and prior close > SMA(20).
- Short setup: RTH open > prior RTH high + 0.15 * ATR(14), and prior close < SMA(20).
- Trigger: buy stop at prior RTH low, or sell stop at prior RTH high. If not filled by 12:00 ET, cancel.

**Exit.** Stop at the RTH open. Otherwise, exit at the next RTH open if it is profitable versus the fill, else exit at the open of the session after that.

**Sizing.** Risk 0.35% of equity to the stop distance (entry to the open). If that distance is under 2 ticks, skip; the stop is inside the noise.

**Costs.** 1 tick per side plus commission on the base case; 2 ticks on the stress. Stops pay the extra tick.

**Parameters.** ATR multiple {0.10, 0.15, 0.25}. SMA length is not searched; 20 is the rule. Macro skip is not searched.

## 6. Failure modes & regime dependence

Trend days after a real overnight information shock, which the macro filter only partly removes. Contract rolls that look like gaps. Using the electronic overnight high as "yesterday's high," which makes the setup almost never trigger and then triggers on noise. The first-profitable-open exit can give back a large intraday gain if the next open gaps back; that is the published exit, and the backtest has to keep it.

## 7. Validation protocol

**No local backtest exists.**

- **Splits.** Train 2012–2017, validation 2018–2021, holdout 2022 onward. ES and NQ reported separately before any claim that "index futures" work.
- **Baseline.** Flat, and the opposite rule (go with the gap if it extends, rather than fading the failure).
- **Pitfalls.** Same-bar stop and target: if the fill and the open-stop can both be touched in one bar, assume the stop. Session definition must be written down before the run.
- **Acceptance.** Validation profit factor at least 1.2 at 2-tick stress, at least 100 fills, and the holdout not negative. A pass on NQ and a fail on ES is a fail for a pooled book.

## 8. Sources read (annotated)

1. **Traders.com Advantage, "Larry Williams And The OOPS Signal."** https://technical.traders.com/tradersonline/display.asp?art=2471 — excerpt read via search on 2026-10-07. *Taken:* the buy-stop and sell-stop wording. Full article page was not separately fetched.
2. **Unger Academy, "How to Trade Larry Williams' Oops Setup."** https://ungeracademy.com/blog/larry-williams-oops-setup — excerpt read via search on 2026-10-07. *Taken:* first-profitable-open exit and the public-versus-professional open story, as Unger's attribution to Williams.
3. **Hartle interview, Stocks & Commodities, July 1997.** http://traders.com/documentation/FEEDbk_docs/1997/07/0797Williams.html — excerpt read via search. *Taken:* only the statement that a buy signal depends on the fundamental backdrop.
4. **Williams, *How I Made One Million Dollars Trading Commodities* (1979).** Not read. Not quoted.

## 9. Further reading

- The 1979 book, desk copy, for the original tick language and any stop he actually printed.
- Unger's separate test write-up with a 15-point filter. Useful as a warning that point filters do not transfer, not as a result to copy.
