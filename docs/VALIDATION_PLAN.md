# Independent verification plan

Relevant fixtures are specified before implementation; use hand-derived expected outcomes independent of the production algorithm. SR-009 covers prior/current/stale references, timestamp units, completed-bar decisions, warmup, split-crossing labels, future-input invariance, missingness, action/identity boundaries, duplicate/order rules and same-bar target/stop ambiguity. SR-004 adds reservations, integer sizing, cash/position/overlap, dividends/actions and unknown exits. SR-015 adds option contract/rules, clocks/quote ages/sizes and expiry.

Declare exact category/timestamp identities and numeric tolerances by units; no generic tolerance inferred after failure. Small correctness checks precede long replay. All failures retained; bug invalidates affected results. SR-010 protects chronology/trial registry; SR-003 compares fixed controls net of explicit proxy costs and uncertainty; SR-020 confirms once on truly unused/prospective evidence only when justified.

For documentation use UTF-8, local-link/privacy, required structure, unique story/backlog mappings, acyclic dependencies and native GitHub relationship checks. No market-backtest tests are required to verify planning. CI is not a hosted review or numerical feed certification.

## AQuA-informed checks

[Source and applicability](sources/AQUA.md). SR-009 adds prefix/future-perturbation cases including current-day volume denominators, daily aggregation, normalization fitting and multi-resolution branches. SR-019 applies independently expected cases to the accepted package and adapter. SR-010 fixes evaluator/configuration identities, rejects undeclared contract changes and logs trial/selection/holdout access. These are bounded existing-story acceptance additions; exact tolerances and commands must precede execution. No data or strategy certification is implied by this planning update.
