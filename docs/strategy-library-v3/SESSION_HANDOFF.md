# V3 session handoff

Date: 2026-10-07.

## Objective

A fresh strategy library across horizons, with a codeable twist on each lineage, written only from sources opened in this session. Existing `strategy-library/` and `strategy-library-v2/` notes were not to be redone.

## What was finished

Eight research notes in this folder, plus the roster, index, and source log. No backtest was run. No holdout was opened. PDFs are produced by `scripts/build_pdfs.py` when that script has been executed in this environment.

## What was not done

- The Williams 1979 book, Oppenheimer 1986, the 2006 Gorton–Rouwenhorst roll appendix, and the Cohen–Malloy–Pomorski year-count integer.
- Any local performance test.
- Swensen's individual portfolio, analyst-revision drift, and activist 13D filings. They were candidates, then dropped so this pass would not outrun the papers actually read. They sit below as optional later notes, not as started work.

## Data / engine

Not selected. Notes 01 and 02 need intraday timestamps. Note 04 needs Form 4 filing times. Note 05 needs a deal tape. Note 08 needs point-in-time fundamentals. Note 07 needs two contract months per commodity.

## Next command

Do not start a backtest until the acceptance rule in that note's section 7 is copied into an experiment record with the split dates frozen. Preferred first experiments, in order: note 02 (SPY last half hour), then note 01 (closing imbalances), then note 08 (NCAV) if fundamentals are point-in-time.

## Unresolved choices

Market default in the notes is US listed equities, SPY or ES/NQ, and listed commodity futures. No account, cost schedule, or data vendor has been chosen by the user.
