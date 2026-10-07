# 24. Post-Earnings Announcement Drift — Twist: PEAD-IV2

> **Library:** Sigmatiq Strategy Library V2 | **Bucket:** Position (weeks–months) | **Style:** Event drift
> **Instruments:** US equities + listed options | **Typical holding period:** 2 days – 8 weeks | **Complexity (1–5):** 4 | **Evidence grade (A–C):** A-
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise.

## 1. Origin & lineage

**Ball–Brown (1968) → Bernard–Thomas (1989) PEAD.** The oldest event anomaly: prices drift in the surprise direction for weeks after earnings. Foster–Olsen–Shevlin; DellaVigna–Pollet (inattention Fridays); Chordia et al. on liquidity. Practitioner: earnings-continuation desks (Qullamaggie EP is the fast-twitch cousin; this doc is the slower defined-risk drift). Options overlay lineage: Ni–Pearson–Poteshman on post-earnings vol crush.

## 2. The original rules (as published)

- **Academic:** sort by standardized unexpected earnings (SUE = surprise / stdev); long top decile, short bottom; hold 60 trading days; hedge-adjusted (authors' construction).
- **SUE definitions vary:** analyst-consensus vs time-series vs revenue-surprise variants.
- **Practitioner:** buy earnings winners holding the gap + first flag; defined-risk call spreads into the print for lottery-ticket upside.
- **What is NOT stable:** SUE-decile cutoffs, hold length (30/60/90d), value-vs-growth interaction.

## 3. Why it works — mechanism & evidence

**Mechanism.** Underreaction + inattention + limits-to-arbitrage: investors anchor on priors, Friday/late prints get ignored, short-sale constraints slow the short leg; options-implied moves systematically misprice the surprise distribution — drift plus vol-crush mispricing.

**Supporting evidence (all attributed, none ours):**

- Bernard–Thomas and successors document 60-day drift spreads ~ several % per quarter pre-costs across decades (authors' samples; magnitude debated post-2010).
- DellaVigna–Pollet find Friday announcements drift more (inattention mechanism test).
- Options literature documents implied-move overpricing on average with fat right tails (the short-vol edge + tail risk).

**Contradictory / decay evidence:**

- PEAD magnitude decayed post-2000s (automation + faster digestion); recent estimates are fractions of 1990s spreads.
- Transaction costs + short borrow on small-cap losers erase much of the short-leg paper edge.
- Earnings-timing selection (late announcers differ) confounds naive SUE sorts.

**Synthesis.** PEAD persists as a weakened drift plus an options-mispricing edge: trade it surprise-scaled, defined-risk, with drift-curve exits — never as naked weeklies.

## 4. The twist: PEAD-IV2

1. **Implied-move standardization (targets raw-surprise noise):** SUE_IV = price surprise / options-implied earnings move (not analyst stdev); trade only |SUE_IV| > 1.0 (surprise exceeded what vol priced).
2. **Defined-risk expression (targets gap-through-stop):** drift leg via stock + protective structure or call/put verticals; no naked weeklies, ever.
3. **Drift-curve exits (targets fixed-60d rigidity):** exit half at +10 sessions, trail remainder on 10-day low; cap 40 sessions (drift decays, theta does not wait).
4. **Friday/inattention boost (targets uniform sizing):** Friday/late prints get 1.5x size (inattention predicts longer drift).
5. **Revision-m подтвержд (targets one-offs):** require analyst-revision drift same-direction within 5 sessions for full size (confirms surprise quality).

## 5. Full specification of the twist variant

**Universe.** US equities with liquid weekly options (spread <= 5c, OI adequate); price > $10.

**Data requirements.** Earnings dates/times point-in-time, consensus + implied moves, options chains (IV, Greeks), revision feed, borrow rates.

**Signal definitions (formulas).**

- SUE_IV = (actual - consensus)/|consensus| scaled by implied move; revision-confirm boolean; Friday flag.

**Entries.**

Post-print session: stock + vertical (drift direction) when |SUE_IV| > 1.0; revis-confirm sizes full, else half; Friday 1.5x overlay.

**Exits.**

Half at +10 sessions; 10-day-low trail; 40-session cap; vol-crush leg exits into first IV-mean-reversion (typically 3–7 sessions).

**Position sizing.**

1% risk per name; verticals sized by defined max-loss, not notional; max 8 concurrent drifts.

**Risk limits.**

Defined-risk only; earnings-night gap accepted via structure; no adds into adverse drift; Friday sizing disclosed as higher-tail.

**Cost model & capacity.**

Option spreads + stock slippage; borrow on short-drift puts; capacity moderate (liquid-option names).

**Parameters to validate (plateau, not peak):** SUE_IV {0.75, 1.0, 1.5}; hold {20, 40, 60}d; half-take {5, 10, 15}d; Friday mult {1.25, 1.5, 2.0}x.

## 6. Failure modes & regime dependence

Guide-lower prints (beat-and-cut drifts reverse); offering-after-beat; sector-earnings-season reversals; vol-crush timing (IV stays bid into follow-ups).

## 7. Validation protocol

**Status: no local backtest exists yet.** This library contains zero proprietary results; everything above is literature.

- **Data:** Earnings + options history 2010–present point-in-time; revision vintages; borrow; delisted included.
- **Splits:** chronological train / validation / test across full market cycles (must include a bear); no random k-fold; walk-forward anchored.
- **Cost/slippage model:** 5–15 bps/side + borrow on shorts; dividends/splits point-in-time; stress 2x/3x.
- **Pitfalls:** survivorship (delisted included); look-ahead in fundamentals (report-date, not period-end); same-bar ambiguity (conservative fills); corporate actions.
- **Robustness:** plateau heatmaps; bootstrap CIs; placebo (random entries, same exits ~zero); yearly + drawdown-regime sub-samples; best-year removal.
- **Acceptance criteria:** OOS CAGR > benchmark with lower max DD (trend) or Sharpe >= 1.0 (drift); per-trade t >= 2; positive in >= 60% of years; survives 2008/2020/2022 sub-samples.

## 8. Sources read (annotated)

1. **Ball & Brown (1968); Bernard & Thomas (1989) PEAD.** Journal of Accounting Research — drift existence + 60-day construction. Known via secondary citation.
2. **DellaVigna & Pollet on Friday inattention.** Journal of Finance — Friday drift amplification. Known via secondary citation.
3. **Ni–Pearson–Poteshman on options around earnings (vol crush).** Search "Stock price clustering on option expiration" authors' earnings work — implied-move framing. Known via secondary citation.

## 9. Further reading

- Foster–Olsen–Shevlin SUE refinements.
- Chordia et al. liquidity-and-PEAD.
- CBOE earnings implied-move studies.
