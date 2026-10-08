# Strategy Document Template — Sigmatiq Strategy Library

Every strategy document in this library follows this exact structure. Target length: 250–450 lines. Dense and specific — exact formulas, thresholds, parameters. No filler.

---

```markdown
# {NN}. {Strategy Name} — Twist: {CODENAME}

> **Library:** Sigmatiq Strategy Library | **Bucket:** {horizon bucket} | **Style:** {momentum / mean reversion / carry / volatility / microstructure / factor}
> **Instruments:** {...} | **Typical holding period:** {...} | **Complexity (1–5):** {...} | **Evidence grade (A–C):** {...}
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise.

## 1. Origin & lineage
Who created/popularized it (traders, researchers, desks), with links to primary sources: books, papers, interviews, talks. How it has actually been used in practice.

## 2. The original rules (as published)
Exact entry/exit/sizing rules as documented in primary sources. Quote/cite precisely. Note where sources disagree or rules were never fully public.

## 3. Why it works — mechanism & evidence
Economic / behavioral / structural mechanism. What peer-reviewed and practitioner research finds (citations), including contradictory findings, decay, and crowding evidence.

## 4. The twist: {CODENAME}
Each modification with its rationale — which specific weakness of the original it addresses. Modified rules must be unambiguous enough to code.

## 5. Full specification of the twist variant
Universe, data requirements, signal definitions (formulas), entries, exits, position sizing, risk limits, cost assumptions, capacity notes.

## 6. Failure modes & regime dependence
When it loses, what kills it, early-warning indicators.

## 7. Validation protocol
How to backtest honestly: data needs, chronological splits, purging/embargo, cost/slippage model, strategy-specific pitfalls (look-ahead, survivorship, same-bar ambiguity), robustness checks, acceptance criteria.

## 8. Sources read (annotated)
For each source: title, author, URL, date accessed, what it says, what was taken from it. Mark paywalled / abstract-only / inaccessible sources honestly.

## 9. Further reading
```

---

## Honesty rules (mandatory)

1. NEVER invent backtest results, Sharpe ratios, or win rates as our own. Literature-reported numbers must be attributed: "X reports ... (source)".
2. Every URL cited must have been actually fetched and read during the research pass. If a fetch fails, find an alternate or mark it "not accessed — known via secondary citation".
3. Separate the author's claim from local empirical evidence. This library contains no local backtests yet — say so where relevant.
