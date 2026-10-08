# D2 source, cohort and ranking qualification

October 8, 2026. Related [SR-041](../docs/stories/SR-041_PLAN.md), planned [M7](../docs/releases/M7_PLAN.md). Outcome-free qualification following accepted M6 design; scientific status untested, no historical stock ranking or strategy replay.

## Primary method and correction

[Jegadeesh and Titman (1993)](https://www.bauer.uh.edu/rsusmel/phd/jegadeesh-titman93.pdf), introduction, section I and the transaction-cost discussion on printed page 77, were read directly. Their rules use three-to-twelve-month formation and holding, ranked deciles, winner/loser positions and overlapping portfolios, with an additional skip-week version. These are distinct from a proposed long-only five-session stock adaptation.

**Correction to the imported dossier:** its blanket claim that the original paper does not account for costs is inaccurate. The paper includes an assumed 0.5% one-way transaction-cost analysis. That is an author-reported assumption, not observed execution or local net performance. Preserve the original dossier/hash and attach this correction rather than rewrite historical provenance.

[Daniel and Moskowitz's NBER listing](https://www.nber.org/papers/w20439) supplied an abstract-level description of momentum crash risk. Full-text retrieval attempts failed, including the NBER PDF and an attempted author URL; detailed methods and dynamic-policy claims remain unverified here. No crash filter is adopted from the abstract. Other imported residual/industry/turnover variations remain distinct untested proposals. Equal long/short dollars do not by themselves certify zero market beta.

## What was built

[Complete-cohort ranking contract](../fixtures/relative_strength.py) requires explicit outcome-blind eligible security identities, qualified universe/price/action/calendar/availability authority, identical past formation endpoints and complete input coverage. Any missing, invalid, duplicate or unexpected member blocks ranking, preserving the intended denominator. The score is a split-adjusted endpoint **price return**, not a dividend-inclusive total return or a ready trading signal.

Equal scores receive equal competition ranks. Lexical identity order is display-only; a top-k cutoff splitting tied scores blocks selection. [33 hand-derived checks](../scripts/check_relative_strength.py) verify known returns, order invariance, ties, cohort incompleteness, invalid identity/prices/clocks and authority failure. No market constituent, price, score, rank or forward outcome was inspected for this story.

## Existing data and empirical blockers

Two selected source metadata files match their producer receipt hashes. The membership receipt explicitly says it was reconstructed backwards from current constituents and a change log. The change receipt is a September 2026 backfill for a September 2025 date and reports zero rows on that selected day. These metadata facts do not establish a complete contemporaneously known common-stock universe, event-absence coverage, historical delisting treatment or observed 2025 arrivals. No member identities were read or used to choose a cohort.

The D1 [stored-price/calendar qualification](D1-daily-inputs.md) and [minute-proxy feasibility](D1-session-feasibility.md) supply bounded ingredients only; their session, action and arrival limitations also apply here. A current or reconstructed survivor list cannot silently become the denominator of historical cross-sectional momentum.

Before empirical work, qualify the historical eligible universe/non-survivors, identity changes, split/dividend accounting, exact session and available-at clocks, and a justified frozen formation/skip convention. Then freeze the long-only scanner, allocation, one stock/market context policy, holding/entry/exit, matched funding/cost/support/uncertainty criteria, chronological splits and finite budget. Existing rejected context gates and exhausted M2 budget remain unchanged; final access stays disabled.

## Disposition

Source-method, correction, complete-denominator machinery and blocked data disposition are delivered as bounded qualification. Full SR-041 remains open with partial evidence; M7 is unreleased. Missing contracts block an experiment, not disprove leadership persistence. The restricted M0 cohort is not broad universe certification and its closed acceptance is preserved. Existing shared stories retain capability lineage; no automatic reopening, new story, source-owner job or paid acquisition. Next sequential qualification is E4's causal contraction versus hindsight-pattern and fundamental-vintage requirements.

Agent source/evidence inspection under the owner waiver; no independent approval claimed. CI, original import identity and exact publication readback remain required.
