# Sigmatiq Strategy Library V2 — 36 Strategies Across 6 Horizons

Fresh encyclopedia. V1 (`strategy-library/`, 12 docs) is reference only and untouched.
Each V2 document names a real trader/desk lineage, states the published rules, explains mechanism plus decay,
then specifies our own codeable twist variant with validation protocol.

- Roster: [ROSTER.md](ROSTER.md)
- Template: [_TEMPLATE.md](_TEMPLATE.md)
- PDFs: [PDF availability note](IMPORT_NOTES.md#pdfs) — one per strategy plus `sigmatiq-strategy-library-v2.pdf` (combined)
- Build: `scripts/build_library.py` generates the markdown docs; `scripts/build_pdfs.py` builds PDFs

**Status:** Research documents. Every performance figure is a literature claim attributed to its author — none are Sigmatiq backtests.

## Buckets

- Ultra-short / HFT and scalping (01–06): QIM-R, LAT-X, TAPE-Q, SKEW-G, DRIVE-F, SWEEP-F
- Intraday (07–12): ORB-VF2, ACD-R, AVWAP-Q2, FLAG-V, TAYLOR-S, WYK-FP
- Swing 1–10 days (13–18): RSI2-VX2, EP-CAT2, KALMAN-B2, GAP-N, DARVAS-V, HTF-Q
- Position weeks–months (19–24): LIVER-P, TURTLE-X2, CANSLIM-F, SEPA-V, VMOM2, PEAD-IV2
- Portfolio / macro / vol (25–30): RP-REG2, VRP-G2, CTA-T, CARRY-F, FLEX2, TAIL-B
- Long-term investing (31–36): VALUE-Q, GARP-L, MAGIC-F, FSCORE-T, QUAL-C, PERM-T

## Document list

- [01-ultra-queue-imbalance-market-making.md](01-ultra-queue-imbalance-market-making.md)
- [02-ultra-latency-cross-venue-arb.md](02-ultra-latency-cross-venue-arb.md)
- [03-ultra-tape-reading-scalping.md](03-ultra-tape-reading-scalping.md)
- [04-ultra-inventory-skew-avellaneda-stoikov.md](04-ultra-inventory-skew-avellaneda-stoikov.md)
- [05-ultra-opening-drive-scalping.md](05-ultra-opening-drive-scalping.md)
- [06-ultra-liquidity-sweep-fade.md](06-ultra-liquidity-sweep-fade.md)
- [07-intraday-crabel-orb.md](07-intraday-crabel-orb.md)
- [08-intraday-fisher-acd.md](08-intraday-fisher-acd.md)
- [09-intraday-vwap-reversion.md](09-intraday-vwap-reversion.md)
- [10-intraday-aziz-bull-flag.md](10-intraday-aziz-bull-flag.md)
- [11-intraday-raschke-taylor-cycle.md](11-intraday-raschke-taylor-cycle.md)
- [12-intraday-wyckoff-orderflow.md](12-intraday-wyckoff-orderflow.md)
- [13-swing-connors-rsi2.md](13-swing-connors-rsi2.md)
- [14-swing-qullamaggie-episodic-pivots.md](14-swing-qullamaggie-episodic-pivots.md)
- [15-swing-pairs-stat-arb.md](15-swing-pairs-stat-arb.md)
- [16-swing-overnight-gap-momentum.md](16-swing-overnight-gap-momentum.md)
- [17-swing-darvas-box.md](17-swing-darvas-box.md)
- [18-swing-bonde-high-tight-flag.md](18-swing-bonde-high-tight-flag.md)
- [19-position-livermore-trend.md](19-position-livermore-trend.md)
- [20-position-turtle-trend.md](20-position-turtle-trend.md)
- [21-position-oneil-canslim.md](21-position-oneil-canslim.md)
- [22-position-minervini-sepa.md](22-position-minervini-sepa.md)
- [23-position-dual-momentum.md](23-position-dual-momentum.md)
- [24-position-pead-drift.md](24-position-pead-drift.md)
- [25-portfolio-dalio-allweather.md](25-portfolio-dalio-allweather.md)
- [26-portfolio-vrp-put-writing.md](26-portfolio-vrp-put-writing.md)
- [27-portfolio-managed-futures-cta.md](27-portfolio-managed-futures-cta.md)
- [28-portfolio-fx-carry.md](28-portfolio-fx-carry.md)
- [29-portfolio-multifactor-ensemble.md](29-portfolio-multifactor-ensemble.md)
- [30-portfolio-tail-hedge-universa.md](30-portfolio-tail-hedge-universa.md)
- [31-invest-buffett-value.md](31-invest-buffett-value.md)
- [32-invest-lynch-garp.md](32-invest-lynch-garp.md)
- [33-invest-greenblatt-magic-formula.md](33-invest-greenblatt-magic-formula.md)
- [34-invest-piotroski-fscore.md](34-invest-piotroski-fscore.md)
- [35-invest-terry-smith-quality.md](35-invest-terry-smith-quality.md)
- [36-invest-permanent-index-tilt.md](36-invest-permanent-index-tilt.md)

## How to download

- Markdown: each file above is directly downloadable.
- PDF: open `pdf/` for per-strategy PDFs and the combined encyclopedia.
- Rebuild: `python scripts/build_library.py` then `python scripts/build_pdfs.py` from the repo root.
