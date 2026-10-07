# Strategy Document Template V2 — Sigmatiq Strategy Library V2

Target: 200–350 lines per doc. Dense, codeable, honest. Extends V1 with horizon-specific fields.

```markdown
# {NN}. {Strategy Name} — Twist: {CODENAME}

> **Library:** Sigmatiq Strategy Library V2 | **Bucket:** {...} | **Style:** {...}
> **Instruments:** {...} | **Typical holding period:** {...} | **Complexity (1–5):** {...} | **Evidence grade (A–C):** {...}
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results.

## 1. Origin & lineage
Who created/traded it, desks, books, papers, interviews, talks. How it is actually used in practice.

## 2. The original rules (as published)
Exact entry/exit/sizing as documented. Quote/cite precisely. Note disagreements and what was never public.

## 3. Why it works — mechanism & evidence
Economic/behavioral/structural mechanism. Supporting findings (attributed) + contradictory/decay evidence. Close with synthesis.

## 4. The twist: {CODENAME}
One bullet per modification: what changed + which weakness it addresses.

## 5. Full specification of the twist variant
Universe, data requirements, signal definitions with formulas, entries, exits, sizing, risk limits, cost model, capacity, parameter validation grid.
Horizon extras: HFT docs add queue/latency/fee schedule; investing docs add fundamentals/rebalance/tax.

## 6. Failure modes & regime dependence
When it loses, what kills it, early-warning indicators.

## 7. Validation protocol
Data needs, splits, costs, pitfalls (look-ahead, survivorship, same-bar ambiguity), robustness checks, acceptance criteria. Pre-registered: no capital before passing.

## 8. Sources read (annotated)
Title, author, URL, what it says, what was taken. Mark paywalled/abstract-only/not-directly-fetched honestly.

## 9. Further reading
Known but unaccessed sources, honestly marked.
```

## Honesty rules (mandatory)

1. NEVER invent our own backtests, Sharpes, or win rates. Attribute: "X reports ... (source)".
2. Every URL cited must be real and plausibly fetchable. If not directly fetched in this pass, mark "not directly fetched — known via secondary citation".
3. Separate author claims from local evidence. V2 contains no local backtests yet — say so.
4. V1 stays untouched. V2 files live only under `strategy-library-v2/`.
