# 10. Aziz Intraday Bull-Flag Momentum — Twist: FLAG-V

> **Library:** Sigmatiq Strategy Library V2 | **Bucket:** Intraday | **Style:** Momentum / pattern
> **Instruments:** High-RVOL large/mid caps, QQQ/SPY | **Typical holding period:** 5–60 min, flat by close | **Complexity (1–5):** 2 | **Evidence grade (A–C):** C+
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise.

## 1. Origin & lineage

**Andrew Aziz lineage.** *How to Day Trade for a Living* (2015) + Bear Bull Traders room + Zarattini–Aziz SSRN (2023): the 5-min ORB/bull-flag momentum canon for retail — high-RVOL gappers, first-pullback entries, 2R-ish targets. SMB intraday momentum lore is the prop cousin (stricter selection, faster scratches). Our spec keeps Aziz's pattern but replaces fixed risk/targets with volatility-adaptive versions and adds the RVOL + float gates the replication literature demands.

## 2. The original rules (as published)

- **Aziz:** trade gappers/RVOL leaders; bull-flag / flat-top breakout entries on 5-min; stop at pullback low; target ~2R; max 1–2% risk; done after daily goal or two stops.
- **SSRN mechanical cousin:** first-candle direction, second-candle entry, 10R/EOD (academic extreme of the same impulse).
- **SMB overlay:** tape must confirm (no offer reload); scratch fast; grade-A setups only.
- **What is NOT rigorous:** 'high RVOL' and 'clean flag' are eyeballed; published win-rates are room-reported, not audited.

## 3. Why it works — mechanism & evidence

**Mechanism.** Gap + RVOL sorts for overnight information + retail/institutional attention; the first flag consolidates the opening impulse with shrinking range/volume; the break re-recruits momentum algos and late retail — a micro continuation cascade before lunch mean-reversion.

**Supporting evidence (all attributed, none ours):**

- Zarattini–Aziz headline QQQ momentum numbers (Sec. 07) — same impulse family, same slippage caveats.
- Prop-room leaderboards show flag-breakout concentration in morning RVOL leaders (firm-published; unaudited).
- Heston/Gao intraday momentum seasonality supports morning-impulse continuation timing.

**Contradictory / decay evidence:**

- Retail flag-breakout replications net of realistic slippage are marginal (see 07 replication notes: breakeven ~2.2c/share).
- Afternoon flags fail far more than morning flags (time-of-day decay documented in practitioner stats).
- Low-float flags are manipulation-prone; several 'textbook' examples in education precede halts.

**Synthesis.** Morning high-RVOL first-flag breaks are the only sub-variant with any honest support; everything else (afternoon, low-RVOL, third-flag) is overtrading. Edge is selectivity + scratch discipline.

## 4. The twist: FLAG-V

1. **RVOL + float gates (targets junk flags):** RVOL-premarket >= 3x and float > 20M shares (or index/ETF); penny/low-float flags excluded entirely.
2. **First-flag-only (targets late-break chop):** only the first consolidation after the opening impulse qualifies; second+ flags are stand-down.
3. **Volume-shape confirmation (targets flat breakouts):** flag volume must contract >= 30% vs impulse leg and expand on the break bar.
4. **Adaptive target (targets fixed-2R rigidity):** target = prior impulse length x 0.5 extension, capped at 2.5R, floored at 1.0R; partial 50% at 1R.
5. **Morning window + goal-stop (targets afternoon giveback):** entries 09:35–11:00 ET; halt after +3R day or -1.5R day.

## 5. Full specification of the twist variant

**Universe.** US common stocks > $10, float > 20M, premarket RVOL >= 3x; plus QQQ/SPY momentum sleeve.

**Data requirements.** Premarket volume + float catalog, 1-min/5-min bars, impulse/flag auto-detector, ATRm, halt calendar.

**Signal definitions (formulas).**

- Impulse: >= 1.0 ATRm in <= 15 min on RVOL >= 3x. Flag: 3–5 bar contracting range (each bar range < prior) with volume -30%.
- Break: close beyond flag extreme + volume expansion vs flag median. Morning window only.

**Entries.**

Stop-entry beyond flag extreme post-contraction; stop at flag extreme opposite + 1 tick/0.1 ATRm; first flag only.

**Exits.**

50% at 1R, runner to impulse-extension target (cap 2.5R); scratch if no follow-through in 3 bars; hard flat 15:30 ET; goal-stop day.

**Position sizing.**

0.5% risk; gap-day size halved if opening range > 0.6 ATRd (extended already).

**Risk limits.**

Float/RVOL gates hard; halt-calendar respected; two-stop day halt; no averaging into flag failures.

**Cost model & capacity.**

$0.003–$0.005/share all-in assumed; 70% limit-fill haircut on break entries; capacity retail/prop-fine, institutional-irrelevant.

**Parameters to validate (plateau, not peak):** RVOL {2, 3, 5}; flag bars {3, 5}; contraction {20%, 30%, 40%}; target cap {2.0R, 2.5R, 3.0R}.

## 6. Failure modes & regime dependence

Second-flag/late-day breaks; low-float manipulation flags; halt-resumption flags that gap through stops; news-reversal flags (headline fade).

## 7. Validation protocol

**Status: no local backtest exists yet.** This library contains zero proprietary results; everything above is literature.

- **Data:** 1-min + premarket volume 2016–present; float point-in-time; halt log; same-bar ambiguity handled stop-first.
- **Splits:** chronological train / validation / test; no random k-fold. Walk-forward re-fit anchored annually.
- **Cost/slippage model:** commission + 1–2 ticks slippage per side (futures) or $0.003–$0.005/share all-in (equities); limit-target fills haircut to 70% touch-fill; stress at 2x and 3x costs.
- **Pitfalls:** look-ahead in same-bar high/low triggers (assume stop-first fills); survivorship in equity sleeves (point-in-time universe); session-time alignment (RTH vs ETH); event-day selection bias (flag, never drop).
- **Robustness:** plateau heatmaps; bootstrap CIs; placebo direction test (must be ~zero); VIX-quintile and yearly sub-samples; best-year removal test.
- **Acceptance criteria:** OOS PF >= 1.15 net of 2x costs; per-trade t >= 2; OOS Sharpe >= 0.8; max DD <= 2x in-sample; positive in >= 60% of years.

## 8. Sources read (annotated)

1. **Aziz, *How to Day Trade for a Living* (2015).** https://www.bearbulltraders.com — flag/ORB momentum canon. Book-level knowledge.
2. **Zarattini & Aziz SSRN 4416622 (2023).** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4416622 — mechanical momentum baseline + cost caveats.
3. **SMB Capital momentum literature.** https://www.smbcap.com — selectivity/scratch overlay. Firm-authored.

## 9. Further reading

- Bear Bull Traders webinar flag taxonomy (pattern catalog).
- Prop-firm morning-leader statistics pages.
- Halt/resumption microstructure notes per exchange.
