# Sigmatiq Strategy Library

A curated library of 12 trading strategies spanning four time horizons — from intraday order flow to multi-year portfolio allocation. Each entry documents a strategy with a known public lineage (who traded it, where the rules were published, what the research says), then develops our own proprietary variant ("twist") with exact, codeable rules.

**Status:** Research documents. Every performance figure in these files is a *literature claim attributed to its author* — none are Sigmatiq backtest results. Each document includes a validation protocol (§7) defining how the strategy must be tested before any capital is considered.

**Compiled:** 2026-10-07 · **Template:** [`_TEMPLATE.md`](_TEMPLATE.md)

---

## The roster

| # | Document | Bucket | Style | Twist | Complexity | Evidence |
|---|----------|--------|-------|-------|:----------:|:--------:|
| 01 | [Opening Range Breakout](01-intraday-opening-range-breakout.md) | Intraday | Breakout / momentum | **ORB-VF** — gap-agreement + relative-volume filter, VIX-spike skip, inverse range-width sizing | 2 | B |
| 02 | [VWAP Mean Reversion](02-intraday-vwap-mean-reversion.md) | Intraday | Mean reversion | **AVWAP-Q** — anchored-VWAP sigma bands faded only with order-flow divergence in balanced regimes | 3 | B− |
| 03 | [Order-Flow Imbalance / Micro-Price](03-intraday-order-flow-imbalance.md) | Intraday | Microstructure | **MIC-Q** — micro-price deviation signal, queue-aware passive entries, toxicity kill-switch | 5 | B |
| 04 | [RSI-2 Mean Reversion](04-swing-rsi2-mean-reversion.md) | Swing (1–10d) | Mean reversion | **RSI2-VX** — VIX term-structure position scaling, ATR trailing exits, 0.75% risk cap | 2 | B |
| 05 | [Episodic Pivots / Momentum Bursts](05-swing-episodic-pivots.md) | Swing (1–10d) | Catalyst momentum | **EP-CAT** — catalyst classification, RVOL ≥ 3× gate, first-flag entry instead of pivot-day chase | 4 | C+ |
| 06 | [Pairs Trading / Stat-Arb](06-swing-pairs-statistical-arbitrage.md) | Swing (1–10d) | Relative value | **KALMAN-BASKET** — sector-neutral baskets, Kalman hedge ratios, half-life regime gate | 5 | B |
| 07 | [Post-Earnings Announcement Drift](07-position-post-earnings-drift.md) | Position (wks–mos) | Event drift | **PEAD-IV** — surprise standardized by options-implied move, defined-risk spreads, drift-curve exits | 4 | A− |
| 08 | [Dual / Cross-Sectional Momentum](08-position-dual-momentum.md) | Position (wks–mos) | Momentum | **VMOM** — volatility-managed sizing, 52-week-high quality filter, crash flag | 3 | A |
| 09 | [Turtle Trend Following](09-position-turtle-trend-following.md) | Position (wks–mos) | Trend | **TURTLE-X** — adaptive Donchian length, correlation-cluster heat caps, equity-curve circuit breaker | 4 | B+ |
| 10 | [Volatility Risk Premium](10-portfolio-volatility-risk-premium.md) | Portfolio/Macro | Volatility carry | **VRP-GATE** — contango + skew gates, VRP-sized put writing, tail-hedge overlay, hard VIX stop | 4 | A− |
| 11 | [Risk Parity / All-Weather](11-portfolio-risk-parity.md) | Portfolio/Macro | Asset allocation | **RP-REGIME** — ERC core + CPPI drawdown control + growth/inflation nowcast tilts | 3 | B+ |
| 12 | [Multi-Factor Ensemble](12-portfolio-multifactor-ensemble.md) | Portfolio/Macro | Factor | **FLEX-ENS** — vol-regime sleeve weighting, crowding overlay, constant ex-ante vol | 5 | A− |

---

## How to read these documents

Every document follows the same nine sections:

1. **Origin & lineage** — who created and traded it, with primary-source links (papers, books, interviews).
2. **The original rules** — as actually published, noting where sources disagree.
3. **Why it works** — mechanism plus the honest state of the evidence, including contradictory findings and decay.
4. **The twist** — each modification and the specific weakness it addresses.
5. **Full specification** — universe, formulas, entries, exits, sizing, risk limits, costs. Unambiguous enough to code.
6. **Failure modes** — when it loses and what kills it.
7. **Validation protocol** — the backtest design required before this strategy may be considered tested: splits, costs, pitfalls, acceptance criteria.
8. **Sources read** — annotated access log (what was actually fetched and read on 2026-10-07, what was paywalled or abstract-only).
9. **Further reading** — known but unaccessed sources, honestly marked.

**Honesty conventions.** Literature numbers are always attributed ("Connors reports…", "Gatev et al. find…"). Nothing in this library has been backtested locally yet. Evidence grades: **A** = multiple peer-reviewed confirmations across decades/markets; **B** = solid published evidence with documented decay or mixed replication; **C** = practitioner-documented, unaudited.

## Design themes across the twists

The twists are not random embellishments; they apply the same six desk principles to every horizon:

1. **Regime gating** — every strategy has a state filter that says *when not to trade* (VIX term structure, trend regime, spread half-life, vol state).
2. **Volatility-aware sizing** — size scales inversely with current vs normal volatility, from opening-range width (01) to Barroso–Santa-Clara vol management (08).
3. **Crowding / toxicity awareness** — kill-switches and overlays for when the trade gets crowded or flow turns toxic (03, 10, 12).
4. **Defined-risk expression** — where the tail can kill you, use structures that bound it (07's spreads, 10's tail hedge).
5. **Portfolio-level risk accounting** — heat caps and equity-curve circuit breakers, not just per-trade stops (09, 11).
6. **Pre-registered validation** — each §7 freezes acceptance criteria *before* any local backtest runs.

## Next steps

1. Prioritize 2–3 strategies for local backtesting against the Sigmatiq data stack (see each document's §7 for data requirements and acceptance criteria).
2. Candidates with the best evidence-to-complexity ratio for a first pass: **04 (RSI2-VX)**, **08 (VMOM)**, **10 (VRP-GATE)**.
3. Intraday strategies (01–03) require intraday/L2 data validation before any backtest is meaningful — check data availability first.
