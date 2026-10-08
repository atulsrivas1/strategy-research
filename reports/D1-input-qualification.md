# D1 source and input qualification — October 8, 2026

Related story: [SR-040](../docs/stories/SR-040_PLAN.md), planned [M7](../docs/releases/M7_PLAN.md). Accepted common design: [M6 receipt](../docs/releases/M6_RECEIPT.md). This bounded qualification delivers an ingredient contract and source/data disposition. Empirical admission is blocked. Zero historical comparisons, zero final evaluations, no source-owner job. Full SR-040 remains open; M7 is unreleased.

## Source boundaries

[Moskowitz, Ooi and Pedersen, Time Series Momentum](https://fairmodel.econ.yale.edu/ec439/jpde.pdf), introduction and sections 3–4, were read directly. The focal strategy uses twelve-month past returns, one-month holding, long/short futures/forwards and lagged volatility sizing across asset classes. It does not establish the proposed individual-stock, long-only, five-session breakout.

[Lemperiere et al., Two centuries of trend following](https://arxiv.org/pdf/1404.3274), sections 1–2, were read directly. Its monthly-price trend indicator uses a five-month decay and risk scaling. The reported simulated P&L excludes realistic implementation costs. This is source evidence about a different scope, not a local stock result.

Original Turtle-rule PDF attempts at originalturtles.org and turtletrader.com failed to return readable documents. Archived 20/55-day entries, stops, sizing, pyramiding and last-breakout filters remain attributed, unverified claims. Differing imported rules are preserved. Livermore and CTA dossier claims have not received new primary verification. No canonical Turtle replication claim is made.

## Proposed adaptation and contract

The local hypothesis uses a completed close strictly greater than the maximum high of the prior 20 exact completed exchange sessions. Exclude signal-day and future highs. Require all 20 observations and a consistent point-in-time price basis. Proposed next-session-open entry and five-session hold remain unregistered; there is no selected overlay, cost/support threshold, allocation, chronological split or empirical trial allowance.

[Ingredient implementation](../fixtures/d1_inputs.py) requires explicit qualified calendar, universe, adjustment, historical availability and source-parity authority. Missing, modeled or reconstructed authority blocks eligibility. Its output is an ingredient calculation, never empirical admission. [Independent hand-derived boundary checks](../scripts/check_d1_inputs.py) exercise strict comparison, decimal precision, signal/future exclusion, ordering, duplicate/missing observations, clocks, invalid prices and every authority gate. Synthetic dates are not an exchange calendar; checks do not certify production-engine/package parity.

## Bounded private input audit

One previously exposed development reference artifact for September 11, 2025 was read; only AAPL history strictly before that date was selected. The reference SHA-256 is `a9c93a545669945986363cf321eca3fc614a72af44124457d37f1f51c41f7591`, matching the producer manifest. The private audit retains commands, source metadata, selected ingredients and hashes; underlying data is not published.

The embedded sample contains 130 ordered, unique daily OHLCV observations from March 6 through September 10. The last 20 observations satisfy basic OHLC bounds. Exact exchange-session completeness, raw-source numeric parity and adjusted price basis have not been independently qualified. This is one ingredient sample, not a universe-wide coverage result. No signal-day close, entry, exit, forward return, candidate or outcome table was inspected.

The artifact was completed on September 25, 2026. That reconstruction timestamp cannot prove historical availability in 2025. The associated corporate-action source explicitly reports `unavailable_not_configured` and predictive authority false. Producer readiness and strictly-prior input flags do not repair these authority gaps.

## Usable, buildable and blocked

| Requirement | Evidence now | Next bounded work / owner story |
| --- | --- | --- |
| Daily OHLCV / prior highs | Past sample exists; ordered and internally consistent | Research-only normalizer and raw-source parity, qualified calendar and per-name completeness; SR-008 / SR-010 |
| Historical universe and actions | Existing metadata/imports do not certify contemporaneous membership or price adjustment | Versioned membership/action basis with effective and available clocks; SR-008 |
| Decision-time availability | Reconstructed artifact; no observed historical arrival qualification | Availability ledger separating observed, modeled and unknown; SR-022. Prospective recording may be feasible; coding cannot recreate missing historical arrival evidence |
| Scanner machinery | Fail-closed synthetic ingredient contract implemented | Connect only qualified inputs after parity; no market scanner replay yet |
| Stock/market context | No new policy or evidence selected | Preregister one mechanism-specific policy and matched baseline; SR-022. Previous rejected gates and exhausted budget remain unchanged |
| Execution | OHLC alone cannot certify executable fills/spreads/slippage | Qualify quotes/entry-exit clocks or explicitly bounded proxy scope; SR-004 |
| Accounting / funded capital | Prior restricted receipts do not qualify this strategy | Fixed opportunities/weights, vetoed cash, costs and capital assumptions; SR-025 and shared R24 |
| Empirical protocol | Unfrozen; historical budget zero, final disabled | Freeze numeric acceptance, support, costs, splits and finite budget after applicable inputs qualify; SR-040 / SR-010 |

Start next with the research-side daily input normalizer/calendar/parity specification, coordinated with SR-008 and SR-022 authority evidence. Existing stories cover the missing shared work; this report does not create new stories, an execution session or a producer task. Missing historical evidence may require capture/acquisition or an explicitly accepted restricted scope; it must not be synthesized into observed authority.

## Delivery limits

Relevant independent numerical verification is the hand-derived synthetic oracle, plus the bounded ingredient integrity audit. Agent inspected its own source/evidence; separate PR review is optional under the owner waiver. No independent hosted approval is claimed. Publication requires CI and exact source readback. Scientific status remains untested; missing contracts block feasibility, not disprove the proposed mechanism. Original source dossiers, M0/M1 receipts, M2 negative evidence, M4 deferral and M5 frozen predecessors remain unchanged.
