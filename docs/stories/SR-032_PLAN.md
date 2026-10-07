# SR-032 — Qualify B1: RSI(2) and Short-Term Reversal

Parent: [E08](https://github.com/atulsrivas1/strategy-research/issues/46). Release plan: [M6](../releases/M6_PLAN.md).
State: Exploratory: individual-stock adaptation; original ETF evidence excluded. Priority rank 5/20; medium information value; small design, medium implementation effort. Scientific status: untested locally.

## Hypothesis and information value

Temporary liquidity pressure may reverse after an extreme decline. Testability matters because published/canonical performance may not transfer to US long-only stocks over 2–10 sessions. One proposed RSI(2) oversold long scanner with five-session exit; do not retry M1 loser ranks unchanged. Expected benefit is a cost-surviving effect or useful rejection; no performance promise.

## Sources and prior lessons

[Imported dossier](../strategy-library/B-short-term/B1-rsi2-short-term-reversal.md) sections 3–7, 9, 11–12 and any second-pass corrections; [import provenance and limitations](../strategy-library/IMPORT_NOTES.md). Annotated primary URLs and access grades are retained verbatim. This project has not independently reread/reproduced those claims. [Prior unsuccessful joint context comparisons](../../reports/M2-context-proxy.md) and [exclusive veto diagnosis](../../reports/M2-veto-diagnosis.md) prohibit rescuing the same failed gate by retrospective tuning. ETF, overnight, months/years and long-short results do not establish this stock adaptation.

## Dependencies and required data

Required: adjusted daily prices, RSI initialization, sessions, stock/market context and costs. [SR-008](https://github.com/atulsrivas1/strategy-research/issues/14) universe/actions; [SR-010](https://github.com/atulsrivas1/strategy-research/issues/16) chronology/exposure; [SR-022](https://github.com/atulsrivas1/strategy-research/issues/35) context clocks; [SR-025](https://github.com/atulsrivas1/strategy-research/issues/38) matched accounting; [SR-004](https://github.com/atulsrivas1/strategy-research/issues/4) applicable execution evidence. Existing restricted proxy assumptions are not observed-fill certification. Source/readiness and adaptation specification may proceed; empirical readiness must be documented separately.

## Baseline and experiment

First read/verify primary source claims and source contracts without forward outcomes. One proposed RSI(2) oversold long scanner with five-session exit; do not retry M1 loser ranks unchanged. Before replay freeze exact scanner rules, decision/entry/exit clocks, one stock/market policy, causal input versions, support thresholds, costs and chronological splits. Current planning budget is zero historical strategy trials; select one experiment and explicitly register its bounded budget before outcomes.

For any eligible future adaptation, preserve scanner-only as matched control against scanner plus decision-time stock/market context, states aligned/conflicting/neutral/unknown, vetoed weights cash, no rescaling. Use identical opportunity/weight denominators and count avoided losses and sacrificed winners. Report five-session primary return, drawdown, exposure, turnover, sample support, dependence-aware paired uncertainty and incremental-cost stresses. The +2–3% move frequency is descriptive, not the selection objective. Existing exposed periods remain development; final access disabled.

## Acceptance and rejection

Readiness succeeds when scope, rules, source access, field lineage/clocks and applicable checks are auditable; otherwise preserve blocked/rejected feasibility with precise cause. Empirical promotion requires preregistered positive net incremental benefit, adequate declared support, a dependence-aware interval above zero and survival of differential-cost stress; numeric support/cost/uncertainty/search choices must be frozen before any outcome access. Nonpositive net benefit rejects only the tested scope; intervals spanning zero are inconclusive; bugs invalidate results. Missing contracts block a test, not disprove a market mechanism. Preserve all variants, unsuccessful runs and inaccessible sources. No unchanged negative retry without documented new evidence/mechanism/data/correction. No separate research PR reviewer required under owner waiver; CI, independent relevant numerical checks, sanitized publication and exact delivered-source verification still apply.

## Deliverables and resume

Source qualification note, scoped specification or honest blocker, exact manifests/commands, trial registry, independent correctness checks and all results if later run; update lessons/index/backlog/handoff and live tracking. Current delivery is import/planning only. Resume source/rule qualification in M6 priority order; M4 stays deferred. No worker, new chat, paid data, live orders or final holdout.
