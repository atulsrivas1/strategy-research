# 11. Raschke–Taylor 3-Day Cycle Rhythm — Twist: TAYLOR-S

> **Library:** Sigmatiq Strategy Library V2 | **Bucket:** Intraday | **Style:** Short-term rhythm
> **Instruments:** ES/NQ, YM, liquid index ETFs | **Typical holding period:** Intraday to 2 days | **Complexity (1–5):** 3 | **Evidence grade (A–C):** C+
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise.

## 1. Origin & lineage

**George Taylor (1950s) → Linda Raschke.** Taylor's *Taylor Trading Technique* (Book Bond, 1950s; 3-day Buy/Sell/Short cycle around prior-day extremes) was systematized for modern screens by Linda Raschke (*Street Smarts*, 1995, with Connors; *Trading Sardines*). Raschke's reported approach: Taylor-cycle day-labeling plus opening-range + Taylor-count entry timing on S&P futures. Academic cousin: short-horizon time-series reversal/continuation oscillation (Jegadeesh weekly reversal; Heston intraday seasonality).

## 2. The original rules (as published)

- **Taylor:** label each day Buy day / Sell day / Short day by position vs prior day; buy the Buy-day decline, sell the Sell-day rally, cover/reverse the Short day.
- **Raschke rendering:** buy first test of prior-day low on a Buy day (or sell first test of prior high on Sell day); 80-20/Taylor-count timing variants; stops beyond the extreme.
- **What is NOT fixed:** day-label rules differ across interpreters (close-based vs range-based); intraday timing filters are practitioner overlays.

## 3. Why it works — mechanism & evidence

**Mechanism.** 3-day inventory/positioning rhythm: declines get bought on Buy days (short-cover + dip flow), rallies get sold on Sell days; prior-day extremes act as reference magnets. The edge, if any, is a labeled conditional reversal, not unconditional mean reversion.

**Supporting evidence (all attributed, none ours):**

- Raschke's long practitioner record and *Street Smarts* pattern statistics (author-reported examples; not an audited track record of this rule alone).
- Weekly/daily short-horizon reversal literature (Jegadeesh 1990; Lehmann) supports conditional snap-backs at short lags (different lag than Taylor, same family).
- Floor-trader interviews describe buying Buy-day breaks as standard practice (anecdotal, consistent).

**Contradictory / decay evidence:**

- No peer-reviewed Taylor-cycle profitability study with modern costs we know of; reconstructions are interpreter-dependent (label rules change results).
- Trend regimes (persistent Buy-day failures in bears) break the rhythm for quarters.
- Raschke herself layers discretionary context (opening range, trend) — the bare cycle alone is weaker than the marketed rendering.

**Synthesis.** Taylor labeling is a useful conditioning variable (which day-type is it?) rather than a standalone system; value appears when combined with reference-level tests and a trend filter.

## 4. The twist: TAYLOR-S

1. **Frozen label rules (targets interpreter drift):** Buy day = close in top 25% of prior range; Sell day = close in bottom 25%; else Short/neutral day — no discretion.
2. **Reference-test entries (targets blind cycle trades):** Buy-day longs only at first test of prior-day low ± 0.1 ATRd; Sell-day shorts only at first test of prior-day high.
3. **Trend veto (targets bear-market Buy days):** skip Buy-day longs if price < 20-day SMA slope-down; skip Sell-day shorts if above slope-up.
4. **80-20 timing overlay (targets all-day holds):** entries only in first 90 min or last 60 min (Raschke timing windows); midday tests ignored.
5. **Cycle-failure flip (targets stubborn rhythm):** if a labeled test fails (close through + hold 15 min), flip to breakout side with half size (failed-cycle momentum).

## 5. Full specification of the twist variant

**Universe.** ES/NQ/YM front month; SPY/QQQ ETF sleeve.

**Data requirements.** Daily bars for labels + SMA(20), prior-day H/L/C, intraday 5-min for test timing, ATRd.

**Signal definitions (formulas).**

- Label from prior close position in prior range (quartiles). Test = wick into prior extreme ±0.1 ATRd in timing window.
- Veto: SMA20 slope sign. Flip: 15-min hold beyond extreme post-test.

**Entries.**

Limit at reference test in window with trend-veto pass; stop 0.15 ATRd beyond extreme; one test per day-type per day; flip once at half size.

**Exits.**

Target opposite reference third (prior high third for Buy-day longs) or 1.5R; time-stop EOD+1 for swing leg, intraday flat option 15:55 ET; flip leg uses breakout target 1.0 ATRd.

**Position sizing.**

0.4% risk; flip legs 0.2% (explicitly lower edge).

**Risk limits.**

Trend-veto hard; max one flip per day; event-day tests skipped (FOMC/CPI).

**Cost model & capacity.**

Standard intraday/swing costs; capacity fine at prop size.

**Parameters to validate (plateau, not peak):** Quartile {20%, 25%, 30%}; test tolerance {0.05, 0.10, 0.15 ATRd}; stop {0.10, 0.15, 0.20 ATRd}; window {60m, 90m}.

## 6. Failure modes & regime dependence

Trending quarters where Buy-day lows keep breaking; label whipsaw in inside-day clusters; flip legs in chop (double-loss days).

## 7. Validation protocol

**Status: no local backtest exists yet.** This library contains zero proprietary results; everything above is literature.

- **Data:** Daily + 5-min 2000–present (one full cycle of regimes); SMA/labels reproducible; event flags.
- **Splits:** chronological train / validation / test; no random k-fold. Walk-forward re-fit anchored annually.
- **Cost/slippage model:** commission + 1–2 ticks slippage per side (futures) or $0.003–$0.005/share all-in (equities); limit-target fills haircut to 70% touch-fill; stress at 2x and 3x costs.
- **Pitfalls:** look-ahead in same-bar high/low triggers (assume stop-first fills); survivorship in equity sleeves (point-in-time universe); session-time alignment (RTH vs ETH); event-day selection bias (flag, never drop).
- **Robustness:** plateau heatmaps; bootstrap CIs; placebo direction test (must be ~zero); VIX-quintile and yearly sub-samples; best-year removal test.
- **Acceptance criteria:** OOS PF >= 1.15 net of 2x costs; per-trade t >= 2; OOS Sharpe >= 0.8; max DD <= 2x in-sample; positive in >= 60% of years.

## 8. Sources read (annotated)

1. **Taylor, *The Taylor Trading Technique* (1950s, Book Bond).** Out-of-print classic — 3-day cycle premise. Book-level knowledge; no URL (print).
2. **Raschke & Connors, *Street Smarts* (1995).** Publisher: https://www.wiley.com — Taylor-cycle and 80-20 patterns. Book-level knowledge.
3. **Jegadeesh (1990) on short-horizon reversal.** Journal of Finance — conditional reversal family. Known via secondary citation.

## 9. Further reading

- Raschke *Trading Sardines* interviews (cycle application).
- Heston intraday seasonality (timing windows).
- Floor-trader Taylor-cycle oral histories.
