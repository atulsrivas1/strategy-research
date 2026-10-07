# Strategy Library V2 — Roster (36 strategies, 6 horizons)

Fresh library. V1 (`strategy-library/`, 12 docs) is untouched reference only.
All V2 output lives in `strategy-library-v2/`.

| # | File | Bucket | Lineage | Style | Twist codename |
|---|------|--------|---------|-------|----------------|
| 01 | 01-ultra-queue-imbalance-market-making.md | Ultra-short / HFT | Virtu / Citadel Securities electronic market making | Microstructure / inventory | QIM-R |
| 02 | 02-ultra-latency-cross-venue-arb.md | Ultra-short / HFT | Tower Research / HRT cross-venue latency | Microstructure / arb | LAT-X |
| 03 | 03-ultra-tape-reading-scalping.md | Ultra-short / HFT | John Grady (No BS Day Trading) / Jigsaw tape reading | Discretionary microstructure | TAPE-Q |
| 04 | 04-ultra-inventory-skew-avellaneda-stoikov.md | Ultra-short / HFT | Avellaneda–Stoikov / Guéant–Lehalle optimal market making | Microstructure / stochastic control | SKEW-G |
| 05 | 05-ultra-opening-drive-scalping.md | Ultra-short / HFT | SMB Capital opening-drive / Lance Breitstein tape | Intraday microstructure | DRIVE-F |
| 06 | 06-ultra-liquidity-sweep-fade.md | Ultra-short / HFT | ICT liquidity-sweep / Michael Huddleston concepts, practitioner fade | Microstructure mean reversion | SWEEP-F |
| 07 | 07-intraday-crabel-orb.md | Intraday | Toby Crabel ORB (1990) | Breakout / momentum | ORB-VF2 |
| 08 | 08-intraday-fisher-acd.md | Intraday | Mark Fisher ACD (2002) | Breakout / reference levels | ACD-R |
| 09 | 09-intraday-vwap-reversion.md | Intraday | Institutional VWAP / Berkowitz-Logan-VanderLinden impact | Mean reversion | AVWAP-Q2 |
| 10 | 10-intraday-aziz-bull-flag.md | Intraday | Andrew Aziz / Bear Bull Traders momentum | Momentum / pattern | FLAG-V |
| 11 | 11-intraday-raschke-taylor-cycle.md | Intraday | Linda Raschke / George Taylor 3-day cycle | Short-term rhythm | TAYLOR-S |
| 12 | 12-intraday-wyckoff-orderflow.md | Intraday | Wyckoff / SMB / Wyckoff spring + footprint | Microstructure / auction | WYK-FP |
| 13 | 13-swing-connors-rsi2.md | Swing (1–10d) | Larry Connors / Cesar Alvarez short-term mean reversion | Mean reversion | RSI2-VX2 |
| 14 | 14-swing-qullamaggie-episodic-pivots.md | Swing (1–10d) | Kristjan Qullamaggie episodic pivots | Catalyst momentum | EP-CAT2 |
| 15 | 15-swing-pairs-stat-arb.md | Swing (1–10d) | Tartaglia / Morgan Stanley pairs; Gatev-Goetzmann-Rouwenhorst | Relative value | KALMAN-B2 |
| 16 | 16-swing-overnight-gap-momentum.md | Swing (1–10d) | Overnight-vs-intraday anomaly (Cooper-Cliff-Gulen; Lou-Polk-Skouras) | Overnight drift | GAP-N |
| 17 | 17-swing-darvas-box.md | Swing (1–10d) | Nicolas Darvas box (1956) | Breakout / box | DARVAS-V |
| 18 | 18-swing-bonde-high-tight-flag.md | Swing (1–10d) | Pradeep Bonde / Oliver Kell high-tight-flag | Momentum / pattern | HTF-Q |
| 19 | 19-position-livermore-trend.md | Position (wks–mos) | Jesse Livermore / Reminiscences; Wyckoff lineage | Trend / pivotal points | LIVER-P |
| 20 | 20-position-turtle-trend.md | Position (wks–mos) | Richard Dennis / William Eckhardt Turtles | Trend / Donchian | TURTLE-X2 |
| 21 | 21-position-oneil-canslim.md | Position (wks–mos) | William O'Neil CANSLIM / IBD | Growth momentum + fundamentals | CANSLIM-F |
| 22 | 22-position-minervini-sepa.md | Position (wks–mos) | Mark Minervini SEPA | Growth momentum / VCP | SEPA-V |
| 23 | 23-position-dual-momentum.md | Position (wks–mos) | Gary Antonacci dual momentum | Cross-sectional + time-series momentum | VMOM2 |
| 24 | 24-position-pead-drift.md | Position (wks–mos) | Ball-Brown / Bernard-Thomas PEAD | Event drift | PEAD-IV2 |
| 25 | 25-portfolio-dalio-allweather.md | Portfolio / Macro | Ray Dalio / Bridgewater All Weather | Risk parity / allocation | RP-REG2 |
| 26 | 26-portfolio-vrp-put-writing.md | Portfolio / Macro | CBOE PUT literature; Israelov / Nielsen VRP | Volatility carry | VRP-G2 |
| 27 | 27-portfolio-managed-futures-cta.md | Portfolio / Macro | Hurst-Ooi-Pedersen; SG CTA / AHL lineage | Time-series momentum | CTA-T |
| 28 | 28-portfolio-fx-carry.md | Portfolio / Macro | Lipschutz / bank FX desks; Lustig-Roussanov-Verdelhan | Carry | CARRY-F |
| 29 | 29-portfolio-multifactor-ensemble.md | Portfolio / Macro | Fama-French / Asness AQR value-momentum-quality | Factor | FLEX2 |
| 30 | 30-portfolio-tail-hedge-universa.md | Portfolio / Macro | Spitznagel / Universa; Taleb barbell | Convexity / tail | TAIL-B |
| 31 | 31-invest-buffett-value.md | Long-term investing | Warren Buffett / Berkshire; Graham lineage | Quality value | VALUE-Q |
| 32 | 32-invest-lynch-garp.md | Long-term investing | Peter Lynch GARP / Magellan | GARP | GARP-L |
| 33 | 33-invest-greenblatt-magic-formula.md | Long-term investing | Joel Greenblatt Magic Formula | Value + quality systematic | MAGIC-F |
| 34 | 34-invest-piotroski-fscore.md | Long-term investing | Joseph Piotroski F-score (2002) | Value quality filter | FSCORE-T |
| 35 | 35-invest-terry-smith-quality.md | Long-term investing | Terry Smith / Fundsmith quality compounding | Quality compounding | QUAL-C |
| 36 | 36-invest-permanent-index-tilt.md | Long-term investing | Browne permanent portfolio; Bogle index + tilts | Strategic allocation | PERM-T |

- Final roster: 36 files as listed above, one line per strategy with lineage trader, style, instruments, holding period, evidence grade (see each doc header for full fields).
