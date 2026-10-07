# A1. Inventory-Skew Market Making (Avellaneda-Stoikov family)

Status: research dossier. Nothing in section 7 has been backtested by the author. Not investment advice.
Evidence labels used throughout: [PR] peer-reviewed, [WP] working paper / preprint, [PRAC] practitioner claim, [UNV] unverified.

## 1. Summary, horizon, asset class, holding period

Continuously post a bid and an ask around a model "fair" price, earn the spread (plus any maker rebate) when both sides fill, and control the risk of accumulating a one-sided position by shifting both quotes against the current inventory (the "skew") and by widening or narrowing the spread with volatility and fill intensity. The canonical formalisation is Avellaneda and Stoikov (A-S), extended by Gueant, Lehalle and Fernandez-Tapia (GLFT). Holding period is seconds to minutes; the strategy aims to end flat. Asset classes: listed equities and ETFs, futures, FX ECNs, and crypto perpetuals/spot. For a non-colocated trader the only realistic venues are those where tick size is wide relative to volatility, fees favour makers, and latency is not the whole game (some crypto venues, lower-liquidity futures, wide-tick stocks). In the most liquid US equities and index futures, this is a latency and queue-priority business that retail infrastructure cannot win.

## 2. Origin and who uses it

- Ho and Stoll (1981) set up the dealer inventory problem; Avellaneda and Stoikov (draft 2006, published in Quantitative Finance 2008) combined an exponential-utility inventory model with an order-arrival model borrowed from the econophysics literature of the limit order book. [PR for the published version; I read the 2006 draft text.]
- Gueant, Lehalle and Fernandez-Tapia (arXiv 1105.3115, 2011, later published) showed the HJB equations reduce to a system of linear ODEs, which makes inventory-constrained solutions tractable, and give closed-form approximations. [WP/PR - I verified the abstract only.]
- Fodra and Labadie (arXiv 1206.4810) extend to non-martingale (mean-reverting) mid-prices with directional bets. [WP]
- Cartea, Jaimungal and Penalva wrote the standard book treatment (Algorithmic and High-Frequency Trading); I did not read it for this dossier, so I cite it only as background [UNV in this dossier].
- Real-world practitioners: Virtu Financial is the best-known public example. Its 2014 S-1 reported a single losing day in 1,238 trading days (2009-2013); its CEO later said publicising this "backfired" (Bloomberg excerpt, paywalled). [PRAC / regulatory filing, but it is a marketing-flavoured statistic about a firm, not about the A-S model.] Others (Citadel Securities, Jane Street, Optiver, IMC, Jump) are known market makers, but I have no primary source on their quoting logic and the A-S model is an academic simplification of what they do.

## 3. Economic rationale: why an edge might exist, and who is on the other side

- Compensation for providing immediacy. Impatient liquidity takers pay the spread; the maker earns it, minus inventory risk and adverse selection. This is a payment for a service, not a free anomaly.
- Inventory risk premium. The A-S reservation price r = s - q * gamma * sigma^2 * (T - t) (s mid, q signed inventory, gamma risk aversion, sigma volatility, T-t remaining horizon) makes the quote pair lean toward reducing |q|. The optimal total spread in the paper is gamma * sigma^2 * (T - t) + (2/gamma) * ln(1 + gamma/k), where k is the decay rate of fill intensity with distance from mid. Spread is independent of inventory under their exponential-arrival assumption (the paper says so explicitly). The skew rather than the width does the inventory control.
- Exchange economics: maker rebates and fee tiers often dominate P&L. The hftbacktest GLFT tutorial notes its example was near break-even without rebates [PRAC, open-source documentation].
- Who is on the other side: (a) uninformed flow (retail via wholesalers, index/ETF rebalancing, hedgers) that pays the spread and is the true source of profit; (b) informed or faster flow that picks off stale quotes, which is the cost. The central economic fact: the maker's edge equals spread income minus adverse selection minus inventory cost minus fees, and the model's core weakness is that the original A-S mid-price is a driftless Brownian motion with no information content in flow.

## 4. Canonical rules (implementable)

Using the A-S/GLFT structure (parameters estimated on a rolling window):

1. Fair price s: mid (baseline) or micro-price (see twist).
2. Volatility sigma: rolling standard deviation of mid changes over a window (e.g. 1-5 minutes), scaled to the quote-update interval.
3. Fill intensity: fit lambda(delta) = A * exp(-k * delta) to observed market-order arrivals by distance delta from mid. Fit only the near-touch range where you will actually quote; a global fit is poor [PRAC, hftbacktest tutorial].
4. Reservation price: r = s - q * gamma * sigma^2 * tau, tau = remaining horizon (use a rolling or stationary infinite-horizon variant so tau does not collapse to zero at an arbitrary end of day).
5. Total spread: gamma * sigma^2 * tau + (2/gamma) * ln(1 + gamma/k). Bid = r - spread/2, ask = r + spread/2, rounded to tick, never crossing the touch unintentionally.
6. Hard inventory limit |q| <= Qmax: beyond it, quote only the reducing side.
7. Refresh on each book update or timer; cancel and replace if the new quote differs by at least one tick (to protect queue position, see below).
8. Optional grid: multiple levels spaced about half a spread apart (hftbacktest example).

Practical note: raw A-S skew is often too strong, leaving the bot unwilling to hold any position; the tutorial scales skew and half-spread by separate factors [PRAC].

## 5. Evidence

What the primary sources actually show:

- A-S paper simulations (mid-price s=100, T=1, sigma=2, k=1.5, A=140, 1000 paths, own draft text) [PR for published form; the numbers are synthetic]. With gamma=0.1 the inventory strategy produced mean profit 62.94 with profit std 5.89 and final-inventory std 2.80, versus a symmetric quoting strategy with the same spread: 67.21, std 13.43, inventory std 8.66. With gamma=0.5 the inventory strategy's profit fell to 33.92 against 66.20 for symmetric. Read this correctly: the model reduces variance at the cost of mean P&L, on simulated Brownian prices with no informed traders. It is a risk-control demonstration, not evidence of profit in real markets.
- Fodra-Labadie report, in simulation on a mean-reverting mid, one parameterisation raising average P&L by more than 15 percent with much larger inventory/P&L risk, and another giving up about 5 percent of benchmark P&L while more than doubling Sharpe. [WP, simulated.]
- Cont, Kukanov and Stoikov (J. Financial Econometrics 2014; NYSE TAQ, 50 US stocks) show short-horizon price changes are largely linear in order flow imbalance with slope inversely related to depth. [PR] This is the empirical reason a symmetric-around-mid maker is exposed: flow carries information about the next price move.
- Moallemi and Yuan (queue position valuation, working paper 2016/2017, read only via a search summary): position in the FIFO queue has a value that combines spread earned and an adverse-selection cost that grows toward the back of the queue, plus option value of early position. [WP, secondary read.]
- Easley, Lopez de Prado and O'Hara (RFS 2012) define VPIN as a flow-toxicity measure. Andersen and Bondarenko disputed that it gave early warning of the 2010 Flash Crash; the authors replied. [PR vs. WP dispute; I did not read the critique itself.] Treat VPIN as unproven; use fill markouts instead (section 8).
- Virtu S-1 single-losing-day statistic [regulatory filing, firm-level, survivorship by nature, reflects massive infrastructure].

What I could not find: any independent, out-of-sample, cost-inclusive live or tick-replay evidence that a plain A-S bot earns money for a non-colocated participant. Post-publication decay: the model's ideas are fully absorbed by professional makers; I have no quantitative decay estimate [UNV]. Capacity is bounded by quoted size, tick-constrained queues and exchange limits.

Honest verdict: the strategy class is real (market makers exist and are profitable), but the textbook A-S model alone is a teaching model. Backtests that fill your orders whenever price touches your level, or that ignore queue position and latency, will show profit that does not exist.

## 6. Failure regimes and risks

- Adverse selection in trends and news: all fills on one side, inventory accumulates against you. Skew slows but does not stop this.
- Volatility jumps and gaps: quotes become stale faster than cancels land.
- Latency and queue position: quotes at the back of the queue are filled mostly when price is about to move through them (the worst fills). Without queue modelling, backtests overstate fills.
- Fee-tier dependence: profitability can flip sign with a rebate change. Test with and without rebates.
- Model misspecification: exponential intensity may not hold across depth; mid as fair value ignores short-term signals.
- Exchange/venue risk (crypto): outages, API rate limits, auto-deleveraging, socialised losses.
- Self-trade, wash-trade and order-to-trade ratio rules; regulatory registration questions for the entity.
- Tail risk: stuck inventory in a halted or one-way market.

## 7. MY TWIST (hypotheses, NOT backtested by me)

### Twist 1: Signal-shifted reservation price (micro-price / OFI)
- Rationale: A-S assumes a driftless mid. Stoikov's micro-price (Quantitative Finance 2018, abstract read via a secondary listing: reported to be a better short-term predictor than mid and weighted mid) and Cont et al.'s OFI result suggest the fair price should lean toward imbalance.
- Rule change: r = micro_price + beta * OFI_z - q * gamma * sigma^2 * tau, where OFI_z is order-flow imbalance over the last N events, standardised by rolling depth. Widen the quote on the side opposite the OFI sign.
- Parameters to test: OFI window (5-50 events or 1-10 s), beta (0 to 1 in units of tick), micro-price built from top 1 vs top 3 levels.
- Expected effect: lower 1-5 s adverse markout per fill; modest loss in fill count.
- Falsification: if average 1 s and 5 s markout per fill (out of sample, after fees) does not improve versus the plain-mid baseline by a margin larger than its bootstrap standard error, or improvement vanishes when beta is set by walk-forward rather than in-sample, discard.

### Twist 2: Queue-aware quote suppression
- Rationale: back-of-queue fills are disproportionately toxic (queue-position literature above).
- Rule change: estimate queue ahead Q_ahead and expected consumption rate; post only when estimated probability of fill before adverse move exceeds a threshold, and cancel when queue imbalance turns against the quote. Otherwise stay out of the book.
- Parameters: threshold p* (0.3-0.7), imbalance cancel threshold, minimum order lifetime to avoid losing queue by over-cancelling.
- Expected effect: fewer fills, better average markout; net effect on P&L uncertain because lost spread capture may outweigh it.
- Falsification: if net P&L per day after fees falls versus baseline in at least 3 of 4 walk-forward folds, or Sharpe does not rise, reject.

### Twist 3: Markout-driven dynamic spread
- Rationale: use realised toxicity per venue/time-of-day instead of a theoretical measure like VPIN (contested).
- Rule change: maintain an EWMA of signed 5 s markout of the maker's own fills, by side; add a spread premium proportional to the negative part of that average; pause quoting if it breaches a limit.
- Parameters: EWMA half-life (1-30 min), premium multiplier, pause threshold.
- Expected effect: cuts the losing tails during informed-flow episodes.
- Falsification: if the premium does not reduce the worst-decile 10-minute P&L windows out of sample (versus a matched constant spread widening costing the same fills), reject.

## 8. Implementation spec

Data: L2/L3 order book with exchange timestamps, trade prints with aggressor flag where the venue supplies it, own order/fill/cancel log with latencies. Prefer full-depth event data to snapshots.

Signals: mid, micro-price, OFI (Cont et al. definition from best bid/ask size and price changes), rolling sigma, A and k fit, own-fill markouts.

Sizing: quote size = fixed lot at each level; Qmax from loss budget (Qmax * sigma * sqrt(flatten time) <= risk limit). Gamma chosen so that typical |q| stays within Qmax/2.

Execution: post-only limit orders; replace only when quote moves at least one tick (protect queue); flatten with marketable orders only past a hard limit or at session end.

Stops: per-instrument inventory limit, per-day loss limit, max adverse markout limit (twist 3), connectivity watchdog that cancels all on disconnect.

Cost/slippage model: maker/taker fee and rebate by tier, exchange fees, cancel costs where charged, latency distribution replayed from measurement, and a fill model in which a resting order fills only when (a) trades occur at your price after the estimated queue ahead has been consumed (use a conservative probabilistic queue model, e.g. a power-law share of cancels ahead of you) and (b) partial fills are possible.

Pseudo-code:
```
every book/trade event:
  s = micro_price(book) ; sig = rolling_sigma ; (A,k) = rolling_fit
  r = s + beta*OFI_z - q*gamma*sig^2*tau
  half = 0.5*(gamma*sig^2*tau + (2/gamma)*ln(1+gamma/k)) * (1+toxicity_premium)
  bid = round_down(r-half); ask = round_up(r+half)
  if |q|>=Qmax: suppress adding side
  if queue_filter_fails(bid) cancel bid ; same for ask
  replace orders only if tick-level change
```

## 9. Backtest plan

- Event-driven tick replay with latency and queue modelling (an open-source engine such as hftbacktest is one option; I read its documentation only, not its accuracy audits).
- Walk-forward: calibrate A, k, sigma, beta on a trailing window (e.g. 5 days), trade next day; roll. Keep an untouched final hold-out period (at least 20 percent of data) used once.
- Multiple-testing control: count every parameter combination tried; apply deflated Sharpe or White's reality check / Hansen SPA on daily P&L; report the number of trials.
- Sensitivity: queue-model choice, latency (x1, x2, x5), fee tier, rebate on/off. If profit exists only under optimistic queue/latency assumptions, it does not exist.
- Metrics: P&L per fill, markout curves (1 s, 5 s, 30 s, 5 min), fill ratio, inventory distribution, max inventory, daily Sharpe, worst day, P&L attribution (spread capture, adverse selection, inventory, fees).

## 10. Risk management and kill-switch

- Hard caps: |q|, notional, order rate, order-to-trade ratio, daily loss, 5-minute loss.
- Kill (cancel all and flatten) on: stale market data beyond a threshold, order-ack latency over threshold, inventory beyond Qmax for more than a set time, realised markout beyond limit, spread blowout or volatility more than a set multiple of its trailing median, exchange status message.
- Operational: exchange-side cancel-on-disconnect where available; independent heartbeat process; manual flatten runbook.
- Paper trade or minimum size live before scaling; scale only if live markouts match backtest within tolerance.

## 11. Annotated sources

| # | Source | Type | Grade | Note |
|---|---|---|---|---|
| 1 | Avellaneda and Stoikov, High-frequency trading in a limit order book (draft PDF) https://people.orie.cornell.edu/sfs33/LimitOrderBook.pdf | Paper | A | Read full text; simulations are synthetic |
| 2 | Gueant, Lehalle, Fernandez-Tapia https://arxiv.org/abs/1105.3115 | Paper | A- | Abstract read only |
| 3 | Fodra and Labadie https://arxiv.org/abs/1206.4810 | Preprint | B | Abstract read; simulated |
| 4 | Cont, Kukanov, Stoikov, Price impact of order book events https://arxiv.org/abs/1011.6402 | Paper | A | Abstract read |
| 5 | Moallemi and Yuan, queue position valuation https://arxiv.org/pdf/1610.00261.pdf | Working paper | B | Only via search summary (PDF unreadable to tool) |
| 6 | Easley, Lopez de Prado, O'Hara, Flow toxicity https://papers.ssrn.com/sol3/Delivery.cfm/5120927.pdf and comment https://papers.ssrn.com/abstract=2062450 | Paper/dispute | B | Fetch blocked; read via search summaries |
| 7 | Stoikov, micro-price https://ideas.repec.org/a/taf/quantf/v18y2018i12p1959-1966.html | Paper listing | B | Abstract level only |
| 8 | hftbacktest GLFT tutorial https://hftbacktest.readthedocs.io/en/latest/tutorials/GLFT%20Market%20Making%20Model%20and%20Grid%20Trading.html | Open-source docs | B | Good realism checklist; example near break-even |
| 9 | Virtu Financial S-1 (2014) https://www.sec.gov/Archives/edgar/data/0001592386/000104746914002070/a2218589zs-1.htm | Regulatory filing | B | Statistic read via search summary, not the filing |
| 10 | Bloomberg, Virtu CEO on disclosure https://www.bloomberg.com/news/articles/2014-06-04/virtu-touting-near-perfect-record-of-profits-backfired-ceo-says | News | C | Paywalled excerpt |

## 12. Open questions

1. Can any non-colocated participant earn positive net markout on liquid instruments, or only on wide-tick/rebate venues? Needs live small-size testing.
2. How much of an A-S bot's historical P&L is rebate rather than spread?
3. Does micro-price add value over OFI-shifted mid once latency is realistic?
4. Which queue-position model best matches real fill rates on the chosen venue? Needs calibration against own live fills.
5. Is there a robust, non-contested toxicity indicator (own-fill markout) that adds out-of-sample value?
6. What is the realistic capacity per instrument before own quotes move the book?
