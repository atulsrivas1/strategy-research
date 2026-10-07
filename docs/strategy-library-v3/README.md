# Sigmatiq Strategy Library V3

A new set of strategy notes. Libraries already in this repo (`strategy-library/` and `strategy-library-v2/`) were left unchanged. V3 does not rewrite those trades.

Each note names a lineage that was not the subject of those earlier documents, states what the source actually says, and then writes a codeable variant. The variant is a hypothesis. Nothing here has been backtested on Sigmatiq data.

- Roster: [ROSTER.md](ROSTER.md)
- Research index: [INDEX.md](INDEX.md)
- Sources actually opened: [SOURCES.md](SOURCES.md)
- Handoff: [SESSION_HANDOFF.md](SESSION_HANDOFF.md)
- PDFs: [PDF availability note](IMPORT_NOTES.md#pdfs) after `python scripts/build_pdfs.py`

## Documents

| # | Note | Horizon | Lineage |
| --- | --- | --- | --- |
| 01 | [Closing-auction imbalance](01-close-moc-imbalance.md) | Close to next open | Cushing and Madhavan (2000) |
| 02 | [Last half hour](02-intraday-last-half-hour.md) | 15:30–16:00 | Gao, Han, Li, and Zhou (2018) |
| 03 | [Oops gap fade](03-intraday-williams-oops.md) | About one session | Larry Williams (1979), secondary sources |
| 04 | [Opportunistic insider buys](04-swing-opportunistic-insiders.md) | About one month | Cohen, Malloy, and Pomorski (2012) |
| 05 | [Merger arbitrage](05-position-merger-arbitrage.md) | Life of the deal | Mitchell and Pulvino (2001) |
| 06 | [Spinoff drift](06-position-spinoff-drift.md) | 12–24 months | Cusatis, Miles, and Woolridge (1993) |
| 07 | [Commodity basis](07-portfolio-commodity-basis.md) | Monthly roll | Gorton and Rouwenhorst; 2015 update |
| 08 | [Graham net-nets](08-invest-graham-ncav.md) | One year | Graham (1934) via Carlisle, Mohanty, and Oxman (2010) |

## How to read a note

Author claims and local results are different things. These files contain author claims only. Where a book or a later paper was not opened, the note says so. Where a number was not in the pages read, it is not in the specification.

## Download

Markdown files in this folder are the source. PDFs, once built, are one file per note plus `pdf/sigmatiq-strategy-library-v3.pdf`.
