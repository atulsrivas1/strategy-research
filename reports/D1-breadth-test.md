# D1 breadth test: fixed veto fails the incremental criterion

SR040 / M7, D1-BREADTH-2, October9,2026. One prospective fixed paired comparison after [the inconclusive pilot](D1-exploratory-pilot.md); the original rule was not tuned. **Rejected incremental criterion for this cohort/window and price-proxy assumptions.** This is not a statistically established universal rejection of trend following: the uncertainty interval includes zero.

## Scope fixed before new prices

18 additional convenience stocks: AMZN,GOOGL,META,NVDA,JPM,BAC,XOM,CVX,JNJ,PFE,PG,KO,HD,WMT,CAT,UNH,DIS,CSCO. The pilot's AAPL/MSFT are excluded, with no price-ranked substitution. Same48 canonical prepared daily partitions July15–September19,2025,20 decision dates August13–September10 excluding September1.864 selected rows, zero input exclusions, no unresolved outcomes. Development/exposed dates; no historical eligibility, new market regime or fresh holdout claim. Cross-stock observations share market dependence.

Unchanged PR110 engine: close[t] strictly above prior20 highs; veto when close[t] is above prior20 close population mean plus2 standard deviations (equality tolerance1e-10). Aligned/neutral/unknown admitted; market always unknown. Modeled bar availability t+1 09:00 Eastern, decision09:15, stored-open entry[t+2]/exit[t+7]. Stored UTC-day bars and prices are proxies, not observed historical arrival or qualified session/fills. Assume USD/unadjusted common-share identity and no unseen actions; original source/request/session/action/arrival authority remains unverified under [owner evidence policy](../docs/EVIDENCE_POLICY.md).

Each original opportunity retains fixed reference weight0.1, veto zero/cash, no survivor rescaling. Five open intervals, overlaps allowed. Net unit return exit/entry−1−f×(1+exit/entry), primary f=.001 per side, stresses .002/.003. **Unfunded event-study accounting**: baseline reference exposure reaches1.2; these aggregates are not attainable portfolio returns. Missing inputs/outcomes would remain disclosed and force inconclusive as preregistered, rather than being silently replaced.

## Result and diagnostics

29 original opportunities, all filled as price proxies,16 distinct dates,25 vetoes. At primary cost the veto avoided14 losses but sacrificed11 winners. Avoided weighted loss contribution +2.764236% is smaller than sacrificed winner contribution4.437853% of reference notional. Four opportunities were admitted; the resulting candidate contribution is negative.

| Cost per side | Baseline contribution | Candidate contribution | Paired improvement | Avoided losses / sacrificed winners |
|---|---:|---:|---:|---:|
| 0.10% | +0.710019% | −0.963598% | −1.673616 percentage points | 14 / 11 |
| 0.20% | +0.128727% | −1.042713% | −1.171441 percentage points | 15 / 10 |
| 0.30% | −0.452564% | −1.121829% | −0.669265 percentage points | 16 / 9 |

Weighted primary delta per original opportunity is −0.057711 percentage points. More avoided trades at higher cost do not rescue net contribution. Control/candidate always share original opportunities, inputs, weights, timing and costs.

Circular paired moving-block bootstrap aggregates stock deltas by each of20 decision dates, preserving contemporaneous co-movement: block5,1000 draws,seed4001,percentile indices24/974.95% interval **[−5.270415,+1.009068] percentage points**. The frozen decision rule rejects when primary incremental contribution<=0, irrespective of interval; the interval prevents a claim of a confidently negative population effect. Support improved over the pilot, but the point criterion failed.

| Opportunity state | Aligned | Conflicting | Neutral | Unknown |
|---|---:|---:|---:|---:|
| Stock | 4 | 25 | 0 | 0 |
| Market | 0 | 0 | 0 | 29 |
| Joint | 0 | 25 | 0 | 4 |

Predeclared before-Aug27 / on-or-after subwindows:9/20 opportunities,7/18 vetoes,5/9 avoided losses,2/9 sacrificed winners; paired +0.418002/−2.091618 percentage points. Do not choose the favorable subwindow afterward.

Primary proxy drawdowns2.050905%/0.963598%; maximum reference exposure1.2/0.2; turnover5.812913/0.791155 baseline/candidate. Lower candidate drawdown comes with lost opportunity/gains and reduced exposure; it does not satisfy the frozen improvement criterion or establish a funded risk improvement.

Predeclared concentration diagnostic: largest absolute symbol delta is58.198945% of sum absolute symbol deltas. Leave-one-symbol-out paired total ranges from−2.649802 to+1.996847 percentage points. This sensitivity reinforces limited generality. No stock is dropped or promoted from that diagnostic, and no alternative strategy is selected.

## Verification and disposition

Budget1/1, one completed market attempt, no alternate threshold/exit/cohort trials or failed market run. Cumulative D1 exploratory questions now2, on different stock cohorts; the old exhausted M2 comparisons remain unchanged. Five existing independent synthetic mechanics cases pass;69 independent actual Decimal/identity checks plus12 avoided/sacrificed-count/value checks pass. All27 repository checks and hosted CI are delivery requirements. Agent inspection uses owner separate-review waiver; no independent approval claimed. Source rows/manifests/paths/ledgers remain private; published engine and prior reports are frozen.

[AQR author summary](https://www.aqr.com/Insights/Research/Journal-Article/Time-Series-Momentum), lines53–67, reopened October9, motivates persistence broadly in futures/longer horizons. It does not validate this stock/five-interval overextension hypothesis. Full paper and original Turtle rules remain unqualified. No source fidelity or replication claim.

Park this fixed veto for the tested short-stock adaptation; do not optimize it to recover sacrificed winners. Full SR040 retains broader family/input qualification scope; M7 is planned/unreleased. Next M7 research question is D2 under its own new prospective protocol/budget. [R07 funded portfolio accounting](../docs/design/BUILD_REGISTER.md) stays a separate requirement under SR025; this report does not complete it or infer a live capital/risk mandate. No final access, source-owner changes, paid/live work, new session or schedule.
