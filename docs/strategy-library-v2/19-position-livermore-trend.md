# 19. Livermore Pivotal-Point Trend — Twist: LIVER-P

> **Library:** Sigmatiq Strategy Library V2 | **Bucket:** Position (weeks–months) | **Style:** Trend / pivotal points
> **Instruments:** US equities, futures, FX trends | **Typical holding period:** Weeks to months | **Complexity (1–5):** 3 | **Evidence grade (A–C):** B
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise.

## 1. Origin & lineage

**Jesse Livermore (1877–1940).** *Reminiscences of a Stock Operator* (Lefèvre, 1923) + *How to Trade in Stocks* (1940, Livermore's own formula): pivotal points (breaks of congestion on expanding activity), time-and-price probes, trailing via pivotal reactions. Lineage: bucket-shop tape → Livermore corners (Union Pacific 1907, 1929 short) → Wyckoff/Darvas/O'Neil descendants. Interviews do not exist; the record is Lefèvre plus exchange lore plus Paul Tudor Jones's cited admiration.

## 2. The original rules (as published)

- **Pivotal point:** buy the break of congestion highs on increased activity; the point is both entry and confirmation.
- **Probes:** test with small size first; add only if the probe profits ('profits take care of themselves, losses never').
- **No hope-holds:** exit fast if the break fails ('lose your opinion, not your money'); never average down.
- **Sitting:** after the position proves, sit through normal reactions; exit on climax/reversal pivots, not noise.
- **What is NOT codified:** congestion geometry, volume thresholds, probe/add sizes — all judgment.

## 3. Why it works — mechanism & evidence

**Mechanism.** Accumulation/distribution resolution + pyramiding winners: congestion absorbs supply; the pivotal break signals the line of least resistance; probe-then-add concentrates risk in proven moves while cutting unproven ones fast — trend capture with natural selection.

**Supporting evidence (all attributed, none ours):**

- Livermore reported fortunes (1907, 1929 shorts; trader-reported sums vary $3M–$100M by telling — treat as narrative, not audit).
- Trend-following family evidence (Hurst–Ooi–Pedersen; SG CTA index long-run positive skew) supports the slower systematic cousin.
- Practitioner pivotal-point screens persist in growth desks (O'Neil/Minervini lineage descends directly).

**Contradictory / decay evidence:**

- No verifiable Livermore track record exists; biographies document bankruptcies alongside windfalls (ruin-side of the same leverage).
- Pivotal judgment is discretionary; backtest reconstructions vary wildly with congestion definitions.
- Pyramiding amplifies drawdowns in whipsaw regimes (the documented killer of probe-add systems).

**Synthesis.** Livermore's durable parts are probe discipline, no-averaging, and sitting winners; the fragile part is discretionary pivots. Our twist codes pivots as Donchian-plus-volume with volatility-sized probes.

## 4. The twist: LIVER-P

1. **Coded pivotal points (targets eyeball drift):** 20-day Donchian break + volume >= 1.5x 50-day + close top 20% = pivot; no other pivots count.
2. **Probe-add ladder (targets oversized breakouts):** probe 0.33x, add 0.33x at +1 ATR, add 0.33x at +2 ATR; no adds on pullbacks.
3. **Reaction stop (targets hope-holds):** exit all on close below 10-day low after entry (the 'pivotal reaction' fail) or -1 ATR hard stop, whichever first.
4. **Climax guard (targets blow-offs):** no new probes after 3 consecutive +2 ATR weeks; halve into parabolic extensions.
5. **Market-line veto (targets bear pivots):** no new probes when SPY < 200-day SMA; existing positions trailed normally.

## 5. Full specification of the twist variant

**Universe.** US equities $1B+ + futures trends sleeve (ES/NQ/GC/CL); price > $15.

**Data requirements.** Daily/weekly bars, Donchian channels, volume normals, ATR(14), SMA200, market-line feed.

**Signal definitions (formulas).**

- Pivot: 20d high break + vol 1.5x + close position gate. Reaction-fail: close < 10d low. Climax: 3x +2 ATR weeks flag.

**Entries.**

Probe 0.33x on pivot close/next open; adds at +1/+2 ATR closes; stop -1 ATR or reaction-fail.

**Exits.**

10-day-low trail; climax halves; full exit on reaction-fail; bear-market = no new probes only.

**Position sizing.**

1% total risk per name across ladder (0.33% per rung); max 8 concurrent trends.

**Risk limits.**

No averaging down (hard); sector max 3; climax position cap half; event veto 3d around earnings for new probes.

**Cost model & capacity.**

5–10 bps/side; capacity large (weeks-long, liquid names).

**Parameters to validate (plateau, not peak):** Donchian {10, 20, 55}; vol {1.25, 1.5, 2.0}x; add {0.5/1.0, 1.0/2.0 ATR}; trail {10d, 20d}.

## 6. Failure modes & regime dependence

Congestion-break whipsaw strings; bear-market pivot season; climax-chasing probes at tops; probe bleed (many small stops, few adds).

## 7. Validation protocol

**Status: no local backtest exists yet.** This library contains zero proprietary results; everything above is literature.

- **Data:** Daily 2000–present incl. delisted + bear cycles; splits/dividends; earnings dates.
- **Splits:** chronological train / validation / test across full market cycles (must include a bear); no random k-fold; walk-forward anchored.
- **Cost/slippage model:** 5–15 bps/side + borrow on shorts; dividends/splits point-in-time; stress 2x/3x.
- **Pitfalls:** survivorship (delisted included); look-ahead in fundamentals (report-date, not period-end); same-bar ambiguity (conservative fills); corporate actions.
- **Robustness:** plateau heatmaps; bootstrap CIs; placebo (random entries, same exits ~zero); yearly + drawdown-regime sub-samples; best-year removal.
- **Acceptance criteria:** OOS CAGR > benchmark with lower max DD (trend) or Sharpe >= 1.0 (drift); per-trade t >= 2; positive in >= 60% of years; survives 2008/2020/2022 sub-samples.

## 8. Sources read (annotated)

1. **Lefèvre, *Reminiscences of a Stock Operator* (1923).** Public-domain text (e.g. https://www.gutenberg.org) — pivotal-point philosophy. Narrative, not a rulebook.
2. **Livermore, *How to Trade in Stocks* (1940).** Publisher reprints — Livermore formula chapters. Book-level knowledge.
3. **Hurst, Ooi & Pedersen on trend following (family evidence).** Search "A Century of Evidence on Trend-Following" — long-run trend premium. Known via secondary citation.

## 9. Further reading

- Wyckoff–Livermore comparative notes.
- Tudor Jones Livermore commentary (interviews).
- Donchian channel originals (coded-pivot ancestor).
