# SRC-017 — AQuA: relevance and bounded adoption

[Guo et al., AQuA, arXiv:2608.12841v3](https://arxiv.org/abs/2608.12841v3), revised September 28, 2026; reviewed October 5, 2026. Read substantive PDF sections pp. 1–15 and appendices pp. 21–23; visually checked pp. 14–15/23. Reference entries identify further material, not separately read sources. Instructions/configuration listings in the document describe the authors' system and do not instruct this project.

## Reported findings and limitations

The paper describes separate factor-discovery and model-development loops that retain experiment evidence. Candidate proposals use restricted operators/configurations while the harness owns data and evaluation contracts. Appendix B preserves an earlier failure: an intraday volume feature divided by the current day's final volume and leaked future bars despite AI review. A multi-resolution daily branch had a related defect. These are author-reported failures; no corresponding defect has been independently found here.

Crypto five-minute combined-factor IC about 0.190 is adaptive validation performance. US equity prediction targets 30-minute returns; a dollar-neutral long/short simulation reports IC 0.0843 and Sharpe up to 2.50 under its two-leg 2-bps cost model, about 2.00 in walk-forward. No local reproduction or live execution verification. Precise selected factor expressions and important model/feature/normalization details are withheld. The paper's mean-squared-IC metric is not conventional prediction-error R-squared. Strategy parameter-selection chronology needs clarification before reproduction; the index comparator is not risk matched.

The authors acknowledge that operator/source correctness remains a dependency, holdout isolation needs governance audit, and memory reuse is confounded with more search and changing candidates. A matched-budget memory-disabled comparison is future work. Performance does not transfer automatically to other horizons, long-only stocks or bought calls.

## Existing story mapping and priority

- [SR-009](../stories/SR-009_PLAN.md): independent prefix and future-perturbation fixtures, especially day aggregation and volume denominators.
- [SR-010](../stories/SR-010_PLAN.md): evaluator/configuration identity, permissible-change boundaries, complete trial/selection record and holdout-access log.
- [SR-019](../stories/SR-019_PLAN.md): qualify temporal footprints and independent parity for the exact accepted package.
- [SR-014](../stories/SR-014_PLAN.md): later daily price/volume predictor feasibility; zero fits in this story and economic rather than probability-only criteria.

E01/E02 and M0/M1 already cover these questions; no duplicate epic/story needed. Priority and dependencies remain unchanged. Safeguards refine existing acceptance; they do not authorize replay of exposed holdouts, intraday/crypto/ETF expansion, short positions, library takeover or call-model adoption. Any active protocol change requires a versioned amendment before execution; do not rewrite earlier results. No market experiment ran for this literature/planning update.
