# Strategy Library: Index and Cross-Strategy Verdicts

Built 2026-10-07. 20 dossiers, five horizon groups, each researched in a first pass and (for 15 of them) a second verification pass.

**Read this first**
- This is research, not investment advice.
- Every "twist" (section 7 of each dossier) is an untested hypothesis. Nothing here has been properly backtested.
- Figures tagged `[OWN]` or `[OWN-DATA]` are small sanity checks run during the second pass on free data: short samples, simple costs, correlated tickers. They show mechanics, not proof.
- Many primary papers were blocked (SSRN 403s, paywalls). Anything still marked `unverified` / `[UNV]` is exactly that.
- The verdicts below are my synthesis of the agents' reports, not independent audit results. Spot-check before relying on any single number.

## Verdict table

Evidence grade = how well the *edge after costs* is supported by sources actually read (A strong, D weak). "Pass" = whether a second verification pass was run.

| ID | Strategy | Horizon | Evidence grade | Verdict from the research | Pass |
|---|---|---|---|---|---|
| A1 | Inventory-skew market making | Intraday | C+ | Solid theory (Avellaneda-Stoikov). Numbers come from simulations on synthetic prices. Real edge depends on queue position, fees and latency, not on the model. | 1 |
| A2 | Opening-range breakout / intraday momentum | Intraday | B- | Better covered than other intraday ideas, but several key papers read only as abstracts or secondary summaries. | 1 |
| A3 | VWAP / anchored-VWAP reversion | Intraday | D+ | No peer-reviewed test of reversion to VWAP. Zarattini-Aziz trend rule has a 17% hit ratio and no out-of-sample split. Own 2-sigma fade test not significant. | 2 |
| A4 | Volume profile / order flow | Intraday | D | No audited test of value-area, POC or footprint rules. 80% value-area rule not reproduced (46% vs 53% placebo). OFI explains contemporaneous moves, does not forecast. | 2 |
| B1 | RSI(2) short-term reversal | Days | B- | Small, real, decayed gross edge on SPY. Roughly halved after 2007. A low-exposure overlay (about 5% in market), not a standalone strategy. | 2 |
| B2 | Overnight drift / gap fade | Days | C+ | Overnight drift is real gross but costs erase it (1 bp per side halves it, 5 bp kills it). Gap fade about zero gross, negative after costs. | 2 |
| B3 | Post-earnings drift (PEAD) | Days-weeks | C | Contested. Three sources disagree; none gives a net-of-cost post-2015 test. No drift in large stocks since 2006 per Martineau. Foundational papers unread. | 2 |
| B4 | Pairs / stat arb | Days | C+ | Simple pairs weak since about 2002. Krauss et al. ML version negative after costs for 2010-2015. | 1 |
| C1 | Variance risk premium harvesting | Weeks | B | Premium is real (VIX minus realised about 4 points) but tail risk is severe, and PUT's long-run edge is concentrated in the reconstructed early period (2006-2018 Sharpe 0.50 vs 0.51 for S&P). | 2 |
| C2 | Dispersion / correlation | Weeks | C | Correlation premium decayed (12.5 to 3.2 to 4.5 points across sub-periods). Peer-reviewed source says not exploitable after frictions. No costed live track record found. | 2 |
| C3 | Dealer gamma / opex flows | Intraday-days | C- | No central-bank or peer-reviewed test of GEX. Public GEX data correlates with larger next-day moves but adds under 1 point of R² over VIX. Causality and tradability unproven. 0DTE literature disagrees on direction. | 2 |
| C4 | Crypto funding / basis carry | Days-months | B- | Carry is real but smaller than first reported (about 7% average, not over 10%). Counterparty risk dominates. Funding-sign kill switch would not have caught Oct 2025. | 2 |
| D1 | Trend following (Turtles, CTA) | Months | B | Strong long-history evidence (gross Sharpe 0.8 since 1960), but CTA decade returns fell to 0.8% (Barclay) in the 2010s. My ETF check: 12-month trend gross Sharpe 0.39; Donchian 20/10 negative after 5 bp. | 2 |
| D2 | Cross-sectional momentum | Months | B | Well-documented; momentum crashes are the main risk. Read mostly in full for the primary papers. Not second-passed. | 1 |
| D3 | Carry (FX / futures) | Months | B- | Commodity carry has primary support. G10 dollar-neutral FX carry Sharpe about 0.5 (not 0.7-1.1). Own test: 0.28 for 2012-2025. | 2 |
| D4 | Seasonality / FOMC / turn-of-month | Days | C | Turn-of-month strong before 2006, gone since (cost-aware Sharpe 0.18 vs 0.72 buy-and-hold, 2016-2025). Pre-FOMC drift contested after 2015. Monday effect gone. | 2 |
| E1 | Value + quality | Years | B+ | Piotroski and QMJ verified from papers. HML drawdown to -57.5%; HML Sharpe 2010 to Jul 2026 is -0.03. F-score not significant net of costs in the draft cited. | 2 |
| E2 | Low-vol / betting against beta | Years | B | Original paper verified (Sharpe 0.78). Recent decay: 0.43 for 2007-2020, 0.15 from 2020 to Jul 2026. Costs cut returns by more than 55%. | 2 |
| E3 | Risk parity / All Weather | Years | B- | AQR levered vs unlevered figures verified. Bridgewater's own figures are promotional. 2019 return and 2022 drawdown unresolved. | 2 |
| E4 | CANSLIM / Minervini / Darvas | Months | D+ | Headline returns are self-reported or promotional; survivorship cannot be quantified. Earnings-surprise leg has academic support; O'Neil's specific thresholds do not. Primary books unread. | 2 |

## Cross-cutting findings

1. **Most of the classic anomalies are weaker now than their reputation.** Turn-of-month, naive pairs, PEAD in large caps, BAB, HML, momentum-adjacent short-term reversal all show decay in post-publication or recent samples.
2. **Costs decide a lot.** Overnight drift (B2), Donchian breakouts (D1) and the BAB premium (E2) each swing from attractive to negative as the cost assumption moves from zero to realistic.
3. **Strategies with a structural risk-transfer story hold up best.** Variance premium, carry and trend following are paid for bearing tail, crash or crowding risk. They have the strongest evidence, and their problem is drawdowns, not existence.
4. **Technical-lore strategies have the weakest evidence.** A3, A4 and E4 rest mostly on vendor pages, forums and self-reported results. Weak evidence is not proof of no edge, but nothing here supports one.
5. **Evidence is missing where it matters most for practitioners:** costed live track records, intraday data with realistic fills, and independent replications.

## What the twists add

Each dossier proposes one to three variants with exact rule changes, parameters to test, and a falsification criterion. They are the only original contribution in this library and the only part not drawn from sources. Treat them as a test plan, not a result. Known issue: D4 twist B (press-conference condition) is degenerate after 2018 and should be dropped or redone.

## Not covered

Merger arbitrage, discretionary macro (Soros/Druckenmiller style), index-rebalance and inclusion trades, convertible arbitrage, and credit/rates relative value. These are candidates for a second batch.

## Files

- `A-intraday/` A1-A4
- `B-short-term/` B1-B4
- `C-vol-and-flow/` C1-C4
- `D-medium-term/` D1-D4
- `E-long-term/` E1-E4

Each file has 12 base sections; second-passed files add "13. Second-pass changelog" listing what was corrected, confirmed or left unverified.
