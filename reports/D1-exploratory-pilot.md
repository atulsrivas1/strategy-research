# D1 exploratory breakout/context pilot

SR-040 / M7; D1-EXPLORATORY-1, preregistered October 8, delivered October 9, 2026. **Inconclusive.** This is an exploratory stock adaptation with declared assumptions, not original Turtle replication or executable-performance qualification. Missing evidence is retained under the [owner policy](../docs/EVIDENCE_POLICY.md).

## Frozen question and inputs

Does a fixed overextension veto improve a 20-session high breakout's five-interval stored-open price-proxy outcome? The scanner uses close[t] > max(high[t-20:t]); context compares close[t] with the population mean plus two standard deviations of the preceding 20 closes. Conflicting stock context is vetoed; aligned/neutral/unknown is admitted. Market context is always unknown. No retrospectively chosen threshold, exit, cohort or cost scenario.

AAPL and MSFT were chosen before price reads as a convenience cohort. There are 48 fixed daily partitions, July 15–September 19, 2025, 96 selected market rows, 20 decision dates August 13–September 10, and no input exclusions. Weekdays exclude September 1. These are development data, not a historical membership universe or fresh holdout. No final evaluation was designated or accessed.

Before price reads, two recorded amendments corrected entry timing to stored open[t+2], exit open[t+7] (five open-to-open intervals), and made empty/unresolved outcomes inconclusive. A stored UTC-day open[t+1] could precede the modeled decision at t+1 09:15 Eastern; using it would violate the declared ordering. Daily availability at t+1 09:00 and the decision clock are modeled, not observed receipt times. Equality tolerance is 1e-10 USD. Neither superseded entry timing nor any other strategy variant was run.

Each original opportunity has fixed reference weight 0.1. Vetoed opportunities contribute zero, with no rescaling. Overlaps are allowed. Net unit return is exit/entry − 1 − f×(1+exit/entry), with f = 0.001 per side and prespecified stresses 0.002 and 0.003. These are fixed-notional event-study contributions, not funded portfolio returns or attainable fills. Stored prices are assumed USD, unadjusted common-share proxies with stable identities and no unseen actions over this window.

## Results

Three scanner opportunities on three distinct decision dates; all three had proxy entry/exit outcomes, zero unresolved. The veto removed two net losers and sacrificed zero net winners. The admitted opportunity also lost. The candidate remained negative.

| Cost per side | Baseline contribution | Candidate contribution | Paired improvement |
|---|---:|---:|---:|
| 0.10% | −0.938817% | −0.468519% | +0.470298 percentage points |
| 0.20% | −0.997937% | −0.488070% | +0.509868 percentage points |
| 0.30% | −1.057058% | −0.507621% | +0.549437 percentage points |

Percentages are contributions relative to the fixed reference notional. Higher cost makes avoiding turnover look better here; it does not establish execution quality. Primary improvement divided by all three original opportunities is 0.156766 percentage points of weighted contribution per original opportunity.

Paired circular moving-block bootstrap uses all 20 decision dates, including zeros: length 5, 1,000 resamples, seed 4001, percentile indices 24/974. The primary 95% interval is **[0, +1.062842] percentage points**. Sparse events and dependence limit its interpretation. The frozen promising criterion requires at least 20 filled opportunities, five vetoes, ten distinct signal dates, a strictly positive interval lower endpoint and positive stress deltas; support and uncertainty fail that criterion. The verdict is inconclusive, with no threshold retuning.

| Opportunity state | Aligned | Conflicting | Neutral | Unknown |
|---|---:|---:|---:|---:|
| Stock | 1 | 2 | 0 | 0 |
| Market | 0 | 0 | 0 | 3 |
| Joint | 0 | 2 | 0 | 1 |

Prespecified subwindows before August 27 / on-or-after: 1 / 2 original opportunities, 1 / 1 avoided losses, no sacrificed winners, paired contributions +0.354281 / +0.116018 percentage points. These were not selected after observing outcomes.

Primary stored-close/exit-open proxy drawdowns are 1.447275% baseline and 0.560220% candidate; maximum reference exposure 0.2 / 0.1; turnover 0.591203 / 0.195510. These curves do not account for funded cash, rounded shares, capacity, dividends or executable session prices.

## Evidence and delivery

Original source/request authority, historical arrival, official session meaning and action basis remain unverified. Prepared-file hashes were frozen before selected-row reads and checked again afterward. No evidence flags were upgraded; no market breadth was invented. Source rows, private paths, manifests and detailed ledgers remain local. All dates remain development/exposed, and this experiment does not reopen exhausted M2 comparisons.

The [AQR author research summary](https://www.aqr.com/Insights/Research/Journal-Article/Time-Series-Momentum) was actually read for general persistence motivation. Its futures/longer-horizon findings do not validate this short stock rule. The full paper and original Turtle source were not independently qualified here. The mechanism hypothesis is that extreme prior-close extension may exhaust demand; this sample is too small to substantiate it.

One fixed paired comparison was attempted and completed. Five independent synthetic mechanics cases and 17 independent Decimal/identity checks of actual outcomes passed, including all three cost totals and proxy terminal conservation. Agent evidence inspection uses the owner's separate-review waiver; no independent approval is claimed. The public engine has no source loader or optimizer. All 27 repository CI checks are required before delivery.

This bounded pilot can be delivered with its limitations. SR-040 remains open for broader family/input qualification; M7 remains planned and unreleased. Next useful question is whether the unchanged rule has adequate support over a broader preregistered cohort/window. That requires a new prospective protocol and finite budget before additional outcomes; missing corroboration alone is not a blocker.
