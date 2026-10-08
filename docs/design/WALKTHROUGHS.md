# Design walkthroughs — synthetic evidence only

Toy expected values were frozen in the private design amendment before checker implementation. These are meaningful independent hand calculations and boundary examples; they do not verify market data or a production research engine. [Executable checks](../../scripts/check_design.py) compare these expectations with separate toy computations and validate the full design mapping. Zero historical comparisons and final evaluations.

## D1: completed-bar range and clocks

Prior 20 completed-session highs are 1 through 20. Signal close 21 strictly exceeds prior maximum20: admit. Close20 equals maximum: reject. Signal-day high999 must not enter the previous-20 range. Future high9999 must not alter the past decision. Nineteen valid prior observations block warmup; they are not silently accepted as 20. A field available at time11 cannot enter decision10; exact10 can enter only under the declared feasible decision/order convention. Missing availability blocks the observed-clock claim even if an event timestamp exists.

The toy test establishes the specified exclusion/causal boundary, not a qualified daily source or actual close/auction fill. Real D1 remains a long-stock/five-session adaptation requiring exact input/execution/context qualification and a separately frozen protocol/budget. Future outcome mutation tests past scanner invariance; later outcomes may affect evaluation, never causal admission.

## D2: ranking, fixed weights and veto accounting

Toy past formation prices A100→110, B100→105, C100→99 imply returns +10%, +5%, −1%, rank A>B>C. The three-observation toy illustration does NOT select the real formation window. Adding future prices cannot change this past ranking. Ties need a registered deterministic tie rule; absent eligible-universe clocks block historical ranking admission.

Separate accounting example: immutable scanner weights A=.5/B=.3/C=.2; toy gross holding returns A=.10/B=−.05/C=.02 and roundtrip cost .001 per participating allocation. Hand calculations: scanner=.5×.099+.3×−.051+.2×.019=.0380. Context retains A and vetoes B/C: candidate=.5×.099=.0495, cash=.5. Avoided net loss B=.0153; sacrificed net winner C=.0038. Improvement=.0115=.0153−.0038. Candidate cannot be .099 by rescaling A to full weight. The gate loses a winner as well as avoiding a loser.

Missing B exit leaves scanner economics partially censored; report known subtotal/censored weight, not total return .0533 or missing B=0. Unknown context is neither neutral nor a retrospectively chosen veto; frozen policy must say retain/veto. Explicit cash earns zero only under this declared toy convention, not a general funded cash-return rule. This test does not establish funded reservations/integer/overlap/real execution validity or filter efficacy.

## Deferred family: inventory market making / SR-028

Daily bars and trade-triggered BBO cannot establish continuous individual orders, queue priority, cancels or maker-fill latency. R19 order-level evidence and R20 hedge/borrow needs remain named, along with common contracts. M4 scope is deferred regardless of existing files. Admission fails without both an owner scope amendment and the required qualified evidence; even supplied synthetic order-level evidence cannot itself activate M4.

A source-specific mapping test binds every original dossier hash and story/release; source overlap does not merge hypotheses. The deferred case demonstrates requirements are preserved even when unavailable, rather than dropped to declare readiness. Future scope changes require bounded protocol/dependencies and acquisition permissions; no new feed purchase or upstream producer job follows from this design.

## Relationship and scientific boundary checks

76 unique dossier versions across 20+36+8+12 libraries map to exactly SR-028–067; ten M7 and thirty M4 families. All R01–R24 requirements have feasibility/owner/acceptance; all family requirements resolve. Every version links to original canonical/source-support sections and byte identity. Existing M2 rejected/exhausted budget, restricted M0/M1 claims, final-null/disabled and conditional calls remain explicit. Original frozen scientific reports/fixtures and imported source bytes are unchanged by this design publication.
