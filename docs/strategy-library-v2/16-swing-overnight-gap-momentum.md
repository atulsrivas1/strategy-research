# 16. Overnight Gap / Night-Effect Momentum — Twist: GAP-N

> **Library:** Sigmatiq Strategy Library V2 | **Bucket:** Swing (1–10d) | **Style:** Overnight drift
> **Instruments:** US equities, SPY/QQQ, ES | **Typical holding period:** Overnight to 5 days | **Complexity (1–5):** 2 | **Evidence grade (A–C):** B
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise.

## 1. Origin & lineage

**Night-effect lineage.** Cooper–Cliff–Gulen (2008) and Lou–Polk–Skouras: US equity returns accrue disproportionately overnight (close-to-open) vs intraday; Heston intraday/overnight decomposition; practitioner gap-continuation desks (SMB gap-plays) and QQQ night-session studies. The trade: own the night, rent the day — long overnight / flat-or-short intraday variants.

## 2. The original rules (as published)

- **Academic:** long close-to-open / short open-to-close decomposition earns the documented night premium in US samples (authors' periods; magnitude debated).
- **Practitioner gap-continuation:** buy gap-ups holding above prior high into the first 30 min; short gap-downs failing; exit EOD (no overnight hold in the intraday rendering).
- **Practitioner gap-fade:** fade small gaps back to prior close (mean-reversion cousin — opposite rule, different gap size).
- **Disagreement:** which gaps continue (large + RVOL) vs fade (small, low RVOL); holding overnight vs EOD-flat.

## 3. Why it works — mechanism & evidence

**Mechanism.** Institutional rebalancing + news digestion happens at/after the close and into the open (low-liquidity, high-information window); intraday is dominated by liquidity provision and reversals. Gap direction encodes overnight information; continuation reflects slow digestion over days.

**Supporting evidence (all attributed, none ours):**

- Lou–Polk–Skouras and Cooper et al. document the overnight share of US equity returns across multi-decade samples (authors' claims; replication debates on magnitude, not sign).
- Gap-continuation desk stats show large-RVOL gaps continue more than small gaps (practitioner splits; unaudited).
- QQQ/SPY overnight-vs-intraday decompositions replicate the sign of the effect in retail data (indicative).

**Contradictory / decay evidence:**

- Night-effect magnitude shrinks in recent samples and varies by index/size (replication decay noted).
- Gap-continuation needs the gap to hold early — most gaps partially fill intraday first (whipsaw between fill and continuation).
- Overnight holds carry gap-through-stop risk (the exact tail the EOD-flat variant avoids).

**Synthesis.** The night premium is a documented statistical tilt, not a blank check: tradeable via large-RVOL gap continuation with early-hold confirmation, sized for overnight gap risk — or not at all.

## 4. The twist: GAP-N

1. **Gap-size fork (targets fade/continuation confusion):** >= 2% + RVOL >= 2x gaps → continuation sleeve; < 1% gaps → fade sleeve (separate spec, half size); 1–2% no-trade zone.
2. **Early-hold confirmation (targets immediate fills):** continuation entries only if gap holds (no fill beyond 50%) through 10:00 ET.
3. **Night-only expression (targets intraday giveback):** enter MOC, exit next open (pure overnight leg); optional intraday continuation leg only if 10:00 hold confirms.
4. **Earnings-night filter (targets binary gaps):** earnings gaps trade at quarter size with defined-risk options overlay (see PEAD doc) or not at all.
5. **Inverse-vol sizing (targets gap-through-stop):** size *= clip(1%-gap/2%, 0.25, 1.0); larger gaps get smaller, not larger.

## 5. Full specification of the twist variant

**Universe.** Top-500 equities + SPY/QQQ; earnings nights quarter-size only.

**Data requirements.** Daily + premarket/after-hours prints, gap catalog, RVOL, ATR, earnings calendar, options chain for overlay sleeve.

**Signal definitions (formulas).**

- Gap g = (open - prior close)/prior close; RVOL-premarket; 10:00 ET fill fraction = retrace/gap.
- Continuation: g >= 2%, RVOL >= 2x, fill <= 50% by 10:00. Fade sleeve: |g| < 1%, fade to prior close.

**Entries.**

MOC entry for overnight leg; 10:00-confirm add for intraday continuation; fade sleeve limits at prior close approach.

**Exits.**

Overnight leg exits next open; continuation leg targets 1.5R / EOD; fade exits at fill or EOD; all flat into weekends for event names.

**Position sizing.**

0.5% risk continuation; 0.25% fade; earnings 0.15%; gap-size inverse factor above.

**Risk limits.**

Overnight gap cap per name; weekend/event halt; max 6 overnight legs concurrent.

**Cost model & capacity.**

MOC slippage + spread; 5–10 bps/side; capacity large (overnight, liquid names).

**Parameters to validate (plateau, not peak):** Gap {1.5%, 2%, 3%}; RVOL {1.5, 2, 3}x; fill {33%, 50%, 66%}; hold {MOC-open, +1d, +3d}.

## 6. Failure modes & regime dependence

Morning-reversal days (fill then rip — worst for continuation entries); overnight news against the leg; earnings-secondary-offering nights.

## 7. Validation protocol

**Status: no local backtest exists yet.** This library contains zero proprietary results; everything above is literature.

- **Data:** Daily + intraday-confirm 2000–present; premarket volume where available; earnings timestamps point-in-time.
- **Splits:** chronological train / validation / test; no random k-fold. Purged/embargoed where labels overlap; walk-forward anchored.
- **Cost/slippage model:** $0.003–$0.005/share all-in or 5–10 bps per side; borrow costs on shorts; limit-fill haircut 70% on touches; stress 2x/3x.
- **Pitfalls:** survivorship (point-in-time universe incl. delisted); look-ahead in fundamentals/earnings timestamps; same-bar ambiguity (stop-first); corporate actions (splits/dividends adjusted with point-in-time factors).
- **Robustness:** plateau heatmaps; bootstrap CIs; placebo (randomized entries, same exits — must be ~zero); yearly + VIX-quintile sub-samples; best-year removal.
- **Acceptance criteria:** OOS Sharpe >= 0.8 net of 2x costs; PF >= 1.2; per-trade t >= 2; max DD <= 2x in-sample; positive in >= 60% of years.

## 8. Sources read (annotated)

1. **Lou, Polk & Skouras on overnight returns.** Search "A tug of war: overnight vs intraday" — night premium. Known via secondary citation.
2. **Cooper, Cliff & Gulen on overnight vs intraday.** Search "Return differences between trading and non-trading hours" — decomposition. Known via secondary citation.
3. **SMB gap-play literature.** https://www.smbcap.com — early-hold heuristics. Firm-authored.

## 9. Further reading

- Heston overnight/intraday decomposition updates.
- QQQ night-session retail studies.
- ETF creation-flow vs overnight move notes.
