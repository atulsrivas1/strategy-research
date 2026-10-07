# 14. Qullamaggie Episodic Pivots — Twist: EP-CAT2

> **Library:** Sigmatiq Strategy Library V2 | **Bucket:** Swing (1–10d) | **Style:** Catalyst momentum
> **Instruments:** Small/mid-cap growth equities | **Typical holding period:** 1–10 days | **Complexity (1–5):** 4 | **Evidence grade (A–C):** C+
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise.

## 1. Origin & lineage

**Kristjan Qullamaggie (Qullamaggie).** 2020 US Investing Champion (+400%+ reported), trader interviews (Chat With Traders #244, Qullamaggie video education): episodic pivots — the first daily breakout after an earnings/guidance-driven gap on massive volume, bought as the trend-day high breaks with the catalyst fresh. Lineage: O'Neil gap logic + Livermore pivotal points + modern small-cap momentum rooms. Pradeep Bonde flag work is the slower cousin.

## 2. The original rules (as published)

- **Setup:** earnings/guidance/news gap + huge volume (RVOL 3–10x), prior base/flat consolidation.
- **Trigger:** first daily pivot — break of the gap-day high (or first flag) within 1–5 days; buy the tape break, not the gap open.
- **Stop:** gap-day low / pivot low (tight, ~5–10%).
- **Exit:** trailing via prior-day low / 10-day line; partials into extensions; no fixed target (ride the episode).
- **What is NOT codified:** 'episodic' judgment (which news qualifies), pivot-day vs first-flag choice, add rules — all discretionary.

## 3. Why it works — mechanism & evidence

**Mechanism.** Information + attention shock: a genuine fundamental surprise under-owned by institutions forces multi-day accumulation; the pivot marks supply absorption; first-flag continuation harvests the institutional follow-through before the parabolic blow-off.

**Supporting evidence (all attributed, none ours):**

- Qullamaggie published brokerage-style returns for contest years (trader-reported; unaudited but widely scrutinized).
- PEAD literature (Bernard–Thomas; DellaVigna–Pollet) supports multi-day drift after genuine surprises (academic, slower variant).
- Practitioner EP compilations show outsized right-tail examples (illustrative; survivorship-heavy).

**Contradictory / decay evidence:**

- No peer-reviewed EP-pivot profitability study; base rates are brutal (most gappers fade within 3 days).
- Small-cap gap liquidity is thin; slippage on pivot breaks exceeds paper assumptions by multiples.
- Parabolic-episode selection in education is survivorship showcase; failed pivots are under-displayed.

**Synthesis.** EP pivots are a fat-tail hunting system: most trades scratch/small-loss, a few episodes pay. Needs catalyst classification, RVOL gating, first-flag (not chase) entries, and ruthless failure-pattern exits.

## 4. The twist: EP-CAT2

1. **Catalyst classifier (targets junk gaps):** trade only earnings/guidance/contract/FDA surprises with quantified beat size; analyst-upgrade-only gaps excluded.
2. **RVOL >= 3x gate (targets thin gaps):** gap-day volume >= 3x 50-day average + dollar volume > $20M.
3. **First-flag entry (targets pivot-day chase):** prefer the first 2–4 day flag break over the gap-day high chase; gap-day entries capped at half size.
4. **Episode-quality score (targets hope-holds):** +1 each for: close in top 10% of range, up-volume > 80%, no prior parabolic in 3 months, short interest > 5% (squeeze fuel).
5. **Failure-pattern exits (targets round-trips):** exit all on close back below pivot day low OR two consecutive closes failing to make new highs after entry.

## 5. Full specification of the twist variant

**Universe.** US small/mid caps $300M–$20B, price > $5, gap-day dollar vol > $20M; no OTC/pinks, no China reverse-merger microcaps.

**Data requirements.** Daily bars + volume/RVOL, earnings/guidance calendar with surprise size, news classifier, short-interest, halt log.

**Signal definitions (formulas).**

- Episode: gap >= 8% on RVOL >= 3x with qualifying catalyst. Pivot: break of gap-day high within 5 days. Flag: 2–4 day contraction, range < 50% of gap-day range.
- Quality score 0–4 as above; require >= 2 for full size.

**Entries.**

Full size on first-flag break (limit/close-confirm); half size on gap-day pivot chase; stop at pattern low (~5–10%); one EP per name per episode.

**Exits.**

Trail prior-day low; partial 1/3 into +20% extension; full exit on failure pattern; max hold 10 days.

**Position sizing.**

1% risk standard; quality-4 episodes 1.5%; gap-day chases 0.5%; portfolio max 4 concurrent EPs.

**Risk limits.**

Earnings-continuation halt risk accepted via size; no adds below entry; parabolic +50% in 3 days forces half-off (blow-off guard).

**Cost model & capacity.**

10–20 bps slippage each side on small caps + borrow if shorting sympathy (long-only spec); capacity small — tens of thousands per name before impact.

**Parameters to validate (plateau, not peak):** Gap {5%, 8%, 12%}; RVOL {2, 3, 5}x; flag days {2–3, 2–4, 3–5}; quality cutoff {1, 2, 3}.

## 6. Failure modes & regime dependence

Gap-and-crap (news already priced); secondary offerings hours after the pivot; sector-wide reversal days; illiquid flags that break on 100 shares.

## 7. Validation protocol

**Status: no local backtest exists yet.** This library contains zero proprietary results; everything above is literature.

- **Data:** Daily + intraday-confirm 2010–present point-in-time; catalyst tags with timestamps; delisted included; halt-aware fills.
- **Splits:** chronological train / validation / test; no random k-fold. Purged/embargoed where labels overlap; walk-forward anchored.
- **Cost/slippage model:** $0.003–$0.005/share all-in or 5–10 bps per side; borrow costs on shorts; limit-fill haircut 70% on touches; stress 2x/3x.
- **Pitfalls:** survivorship (point-in-time universe incl. delisted); look-ahead in fundamentals/earnings timestamps; same-bar ambiguity (stop-first); corporate actions (splits/dividends adjusted with point-in-time factors).
- **Robustness:** plateau heatmaps; bootstrap CIs; placebo (randomized entries, same exits — must be ~zero); yearly + VIX-quintile sub-samples; best-year removal.
- **Acceptance criteria:** OOS Sharpe >= 0.8 net of 2x costs; PF >= 1.2; per-trade t >= 2; max DD <= 2x in-sample; positive in >= 60% of years.

## 8. Sources read (annotated)

1. **Chat With Traders #244 — Qullamaggie interview.** https://chatwithtraders.com — episodic-pivot philosophy. Interview-level knowledge.
2. **Bernard & Thomas / PEAD literature.** Search "Post-earnings-announcement drift" — drift mechanism cousin. Known via secondary citation.
3. **US Investing Championship records.** https://usinvestingchampionship.com — contest return context. Event records; unaudited trading detail.

## 9. Further reading

- Qullamaggie video EP breakdowns (pattern catalog).
- Bonde/Kell flag continuations (slower cousin).
- Small-cap offering-after-spike studies.
