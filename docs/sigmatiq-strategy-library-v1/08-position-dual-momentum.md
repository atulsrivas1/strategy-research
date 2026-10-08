# 08. Dual / Cross-Sectional Momentum — Twist: VMOM

> **Library:** Sigmatiq Strategy Library | **Bucket:** Position (weeks–months) | **Style:** Momentum / trend (factor)
> **Instruments:** Liquid ETFs (equity index, sector, rates, credit, commodity, FX proxy) | **Typical holding period:** 1–6 months (monthly rebalance) | **Complexity (1–5):** 3 | **Evidence grade (A–C):** A for cross-sectional and time-series momentum as phenomena; B for specific dual-momentum implementations (specification-sensitive, see §3/§6)
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise. This library contains no local backtests yet.

## 1. Origin & lineage

- **Jegadeesh & Titman (1993)**, "Returns to Buying Winners and Selling Losers: Implications for Stock Market Efficiency," *Journal of Finance* 48(1), 65–91 — the foundational cross-sectional momentum paper (full text fetched this session). Strategies buying past winners and selling past losers earn significant positive returns over 3–12-month holding horizons; not explained by systematic risk or lead-lag effects.
- Precursors noted by JT93 themselves: Levy (1967) relative-strength rule (discredited by Jensen & Bennington 1970 for selection bias); Value Line timeliness ranks built largely on 3–12-month relative strength; Grinblatt & Titman (1989, 1991) showing mutual funds tend to buy recent-quarter winners.
- **George & Hwang (2004)**, "The 52-Week High and Momentum Investing," *Journal of Finance* 59(5), 2145–2176 (full text fetched) — nearness to the 52-week high dominates past-return momentum as a predictor, and its profits do not reverse later.
- **Moskowitz, Ooi & Pedersen (2012)**, "Time Series Momentum," *JFE* 104(2), 228–250 (full text fetched) — an asset's *own* past 12-month return predicts its future return across 58 liquid futures; the AQR lineage that institutionalized trend as a factor.
- **Gary Antonacci** — *Dual Momentum Investing* (2014 book) and the papers "Risk Premia Harvesting Through Dual Momentum" (SSRN 2042750, 2012 NAAIM Wagner Award winner; full text fetched) and "Absolute Momentum" (SSRN 2244633, 2013; full text fetched). Popularized the combination: relative momentum to pick the asset, absolute (time-series) momentum vs T-bills as the on/off gate.
- **Barroso & Santa-Clara (2015)**, "Momentum Has Its Moments," *JFE* 116(1), 111–120 (full text fetched) — momentum's risk is time-varying and predictable; scaling the momentum portfolio by its own realized volatility "virtually eliminates crashes and nearly doubles the Sharpe ratio."

In practice: cross-sectional momentum runs as a stock-selection factor at every large quant shop (AQR's UMD lineage); dual momentum runs as retail/RIA tactical allocation (GEM — Global Equities Momentum) and as published index products; time-series momentum is the backbone of the CTA/managed-futures industry (see document 09 for that lineage).

## 2. The original rules (as published)

**Jegadeesh & Titman (1993) — cross-sectional momentum.** At the beginning of each month t, rank all NYSE/AMEX stocks on returns over the past J months (J ∈ {3, 6, 9, 12}, implemented as 1–4 quarters); form ten equal-weighted decile portfolios; buy the winner decile, sell the loser decile; hold K months (K ∈ {3, 6, 9, 12}) with overlapping cohorts (each month revise 1/K of the portfolio). A second set of 16 strategies **skips one week** between formation and holding to avoid bid-ask bounce / short-term reversal contamination. Reported results (1965–1989, CRSP): all 32 zero-cost portfolios positive; the best, 12-month/3-month, earns **1.31%/month** (no skip) and **1.49%/month** (1-week skip, t = 4.28); the 6-month formation produces ~1%/month regardless of holding period. The 6/6 portfolio's ~9.5% cumulative 12-month return **loses more than half over the following 24 months** — momentum is a medium-horizon phenomenon, then reverses.

**George & Hwang (2004) — 52-week-high rule.** Rank stocks by `P_i,t−1 / High_i,t−1` (current price over the highest price of the prior 12 months); top 30% = winners, bottom 30% = losers, hold 6 months, equal-weighted, CRSP 1963–2001. Headline (6,6) comparison: JT momentum 0.48%/mo (t = 2.35), industry momentum 0.45%/mo (t = 3.43), 52-week-high 0.45%/mo (t = 2.00) — but **excluding Januaries**: JT 1.07% (t = 6.97), 52-week-high **1.23% (t = 7.06)**, industry 0.50%. In nested head-to-head tests the 52-week-high measure retains profitability inside JT winner/loser groups while JT's measure does not retain profitability inside 52-week-high groups — "nearness to the 52-week high dominates and improves upon the forecasting power of past returns." Crucially, 52-week-high-based returns **do not reverse** at long horizons, unlike JT momentum.

**Moskowitz, Ooi & Pedersen (2012) — time-series momentum.** For each of 58 liquid futures/forwards (24 commodities, 12 currency pairs, 9 equity indices, 13 bond futures; Jan 1965–Dec 2009): go long if the excess return over the past k months is positive, short if negative; hold h months; **size each position inversely to ex-ante volatility** `1/σ_i,t−1`, where σ² is an exponentially weighted variance of daily returns with center of mass 60 days. Volatility-scaled panel regressions show positive continuation for lags 1–12 months (all 12 positive, 9 significant) then reversal over the following ~4 years. Trading-strategy alphas (vs MSCI World, Barclays Agg, GSCI, SMB/HML/UMD) are significant across (k,h); e.g., 12-month lookback/1-month hold t = 6.61 across all assets; positive in every asset class panel. TSMOM "performs best during extreme markets"; CFTC positioning shows **speculators profit from TSMOM at hedgers' expense**.

**Antonacci — dual momentum.** Two building blocks (from "Risk Premia Harvesting Through Dual Momentum," fetched): *relative momentum* — hold whichever of two assets appreciated more over the lookback (12 months; Antonacci does **not** skip the most recent month for multi-asset momentum, noting non-equity assets suffer less from microstructure contamination — this disagrees with the JT skip-month convention); *absolute momentum* — hold the selected asset only if its excess return over **Treasury bills** is positive over the lookback, else hold T-bills ("Treasury bill returns serve as both a hurdle rate and an alternative asset"). Reported for his equity module (MSCI US vs EAFE+, 1974–2011): momentum **15.79%/yr, 12.77% vol, Sharpe 0.73, max DD −23.0%** vs index averages ~11.7%/16.8%/0.34/−54%; without the T-bill hurdle: 13.46%/16.17%/0.45/−54.6% — i.e., Antonacci attributes most of the drawdown/vol reduction to the *absolute* filter. His 2013 "Absolute Momentum" paper extends the overlay to 60/40 and risk-parity portfolios and reports it "can effectively identify regime change." The retail-facing GEM variant: each month, compare US vs ex-US equities on 12-month relative momentum; hold the winner only if it beats T-bills over 12 months, else hold aggregate bonds.

**Barroso & Santa-Clara (2015) — volatility-managed momentum.** Estimate momentum (WML) risk as the **realized variance of daily WML returns over the prior ~6 months**; scale the position each month to target constant volatility (12% annualized in their headline). Momentum variance is highly predictable (out-of-sample R² = 57.8%, ~19pp above the market's own variance predictability). Reported: **Sharpe 0.53 → 0.97**; worst month **−78.96% → −28.40%**; max drawdown **−96.69% → −45.20%**; excess kurtosis 18.24 → 2.68; left skew −2.47 → −0.42; turnover barely changes. "Risk-managed momentum is a much greater puzzle than the original version."

**Antonacci's other modules (from the fetched dual-momentum paper, 1974–2011 unless noted):**

| Module | Return | Vol | Sharpe | Max DD | vs. underlying |
|---|---|---|---|---|---|
| Equity (US/EAFE+ rotation + bills) | 15.79% | 12.77% | 0.73 | −23.0% | indices ~11.5–11.9%, Sharpe ~0.34, DD −51…−57% |
| Credit (HY vs intermediate credit + bills) | 10.49% | 4.74% | 0.97 | −8.2% | HY alone 10.29%, DD −33.2% |
| REITs (equity vs mortgage REIT + bills) | 16.78% | 13.24% | 0.77 | −23.7% | equity REIT 14.6%, DD −68.3% |
| Economic stress (gold vs 20+yr Treasury + bills) | (reported in paper) | — | — | — | Fama-French 3-factor alphas of the four modules: 8.9 / 4.2 / 8.7 / 10.64 (per the paper's abstract page) |

Note the pattern that drives our design: in every module, removing the T-bill absolute filter ("Momentum exT Bills" columns in his tables) restores most of the volatility and drawdown — e.g., equity module ex-bills: 13.46% return but 16.17% vol, Sharpe 0.45, DD −54.6%. Antonacci's own decomposition therefore credits the **absolute** gate, not the relative rotation, with the risk reduction; relative momentum contributes the return enhancement. His 1980–2011 comparison vs the AQR large/small-cap momentum indices (top-third Russell 1000/2000 by 12-month momentum, quarterly rebalance): equity module 16.43%/13.13% vol/0.75 Sharpe/−23.0% DD vs AQR large-cap 14.75%/18.68%/0.45/−51.0% — with Antonacci noting AQR estimates ~0.7%/yr additional transaction-cost drag on their indices.

**JT93 design grid (for completeness).** The 32 strategies = {J ∈ 3,6,9,12-month formation} × {K ∈ 3,6,9,12-month holding} × {contiguous, 1-week skip}. Every zero-cost winner-minus-loser portfolio was positive; only the 3/3 no-skip variant was insignificant. This grid — not a single lucky (6,6) — is why the result was taken seriously, and why our robustness protocol (§7) demands a lookback grid rather than one magic number.

**Where sources disagree:** (a) skip-month — JT skip a week/month for microstructure reasons; Antonacci explicitly does not skip for multi-asset momentum and reports results are *better* without skipping; (b) lookback — academic sweet spot 12-month formation (with 1-month skip ⇒ "12-2"), but Newfound's fragility study (fetched) shows 6–12-month specifications diverge by hundreds of bps/yr and 10-month GEM whipsawed in 2011 when others didn't; (c) whether momentum profits survive costs at all (Lesmond, Schill & Zhou 2004, cited within Barroso–Santa-Clara, argue stock-level momentum is not exploitable after costs — a key reason our twist runs on ETFs, not single stocks).

## 3. Why it works — mechanism & evidence

**Mechanisms.**

1. **Behavioral under-reaction + delayed over-reaction.** MOP (2012) explicitly read their evidence as "consistent with sentiment theories of initial under-reaction and delayed over-reaction": continuation for ~12 months, partial reversal thereafter (matches JT93's year-2 give-back).
2. **Anchoring.** George & Hwang interpret the 52-week high as an anchor: investors under-react to good news as price nears the anchor (grudging adjustment), so nearness predicts continuation; and their returns don't reverse — they argue short-term momentum and long-term reversal are largely *separate* phenomena.
3. **Flow/positioning transfer.** MOP's CFTC analysis: speculators are positioned with the trend and profit at hedgers' expense — a structural transfer, not just a behavioral glitch.
4. **Time-varying risk.** Barroso–Santa-Clara: momentum crashes (e.g., 1932, 2009: WML −78.96% worst month) occur when momentum's realized vol spikes — predictable, hence manageable. Momentum's "moments" are vol regimes.

**Evidence for persistence and decay (honestly weighed).**

- Momentum is one of the most replicated anomalies: JT93 (1965–89 US), MOP (58 futures, 1965–2009, every asset class), George–Hwang (1963–2001), plus the JT93 out-of-sample backtest to 1927–1964 inside their own paper.
- **Decay/crowding:** McLean & Pontiff (2016, cited in our PEAD research) — ~50% anomaly decay post-publication, generic warning. For dual momentum specifically, the strongest recent evidence is the **Petit (2026) replication of GEM on audited free data, 1971–2026** (fetched via globalequitymomentum.com and the author's GitHub): full-period GEM CAGR 15.18%, vol 12.91%, Sharpe 0.83, max DD −21.66%, annualized alpha 6.61% (t = 4.31, Newey–West) — **but** 2010–2026 GEM *loses* 4.8%/yr to the S&P 500, with ~3/4 of the shortfall from bond-sleeve whipsaws (defensive months since 2010 coincided with 34.1% annualized S&P returns vs 5.3% during 1971–2009 defensive months) and ~1/4 from holding non-US while the US kept winning. Petit's line, quoted in the fetched article: "the strategy's published record was established almost entirely before it was published."
- **Specification fragility:** Newfound/Flirting with Models (fetched): GEM outcomes vary by hundreds–thousands of bps/yr across reasonable specifications; "risk cannot be destroyed, only transformed"; distinguishes *specification whipsaw* (2011, 10-month variant) from *style whipsaw* (late 2015/early 2016, nearly all variants).
- **Counterpoint:** SVRN's replication (fetched) found GEM robust to lookback perturbations, stale windows (GEM6-6), and extension back to 1926 for stock/bond timing — while warning the 12-month window may itself be data-mined. Alpha Architect's book review (fetched) found Antonacci's backtests credible but "breezy and imprecise" in places.

**Net read:** momentum-the-phenomenon is grade A. Any *specific* dual-momentum recipe is grade B at best — edge concentrated pre-2010, fragile to specification, and the defensive sleeve is exactly where it has bled since. VMOM is designed against those two specific failure points.

**Why ETFs and not single stocks (the capacity/cost argument, made explicit).** JT93's ~1%/month is measured on equal-weighted deciles of all NYSE/AMEX common stocks — thousands of names, monthly rebalancing of overlapping cohorts, gross of costs. Lesmond, Schill & Zhou (2004, cited within Barroso–Santa-Clara, not fetched directly) argue the stock-level anomaly is not exploitable after realistic costs; Barroso–Santa-Clara themselves flag that they "do not address" the Lesmond critique beyond noting turnover-neutrality of vol scaling. The cross-sectional *factor* is real; the *tradable* version at desk scale is the index/ETF rotation (Antonacci's module approach, which also dodges single-stock gap risk and short-side borrow). What we give up: cross-sectional breadth (5 positions vs 300-stock deciles) — partially compensated by the multi-asset universe's lower pairwise correlation. What we keep: the 12-month formation economics, the absolute gate, and vol management, all of which have asset-class-level evidence (MOP, Antonacci, BS) independent of stock-picking.

**Cross-link to PEAD (document 07).** JT93 themselves document that past winners earn higher returns around their earnings announcements for ~7 months post-formation (and losers lower) — i.e., earnings news is one of the *channels* through which momentum realizes. A name can therefore be simultaneously a VMOM hold and a PEAD-IV candidate; the desk-level rule is that PEAD-IV positions are options-defined-risk and sit in a separate sleeve, so no netting is applied, but combined exposure to one underlying across sleeves is capped at 1.5% NAV at risk.

## 4. The twist: VMOM

**Core idea.** A cross-sectional 12-2 relative-strength rotation over a liquid multi-asset ETF universe, gated by Antonacci-style absolute momentum, with Barroso–Santa-Clara volatility management applied to the *sleeve's own* realized vol, a George–Hwang 52-week-high proximity filter as an entry-quality gate, and an explicit crash flag.

**Modification-to-weakness map (summary):**

| # | Modification | Original weakness it addresses | Key evidence |
|---|---|---|---|
| 1 | 12-2 on 28 ETFs, top-5 rotation | stock-level costs/capacity; GEM's 2-asset concentration | JT93; Lesmond et al. (secondary); Petit decomposition |
| 2 | Absolute gate vs T-bills per asset | relative momentum holds least-bad asset in crashes | Antonacci module tables (exT-Bills columns) |
| 3 | 52w-high proximity ≥ 0.95 on entries | dead-cat entries far below highs | George & Hwang dominance tests |
| 4 | Sleeve vol scaling to 12% target | momentum crashes are vol-regime events | Barroso & Santa-Clara 0.53→0.97 |
| 5 | Crash flag at 2× median σ_21 | monthly BS scaling is too slow for 2009-style crashes | BS worst-month data; Newfound whipsaw taxonomy |

**Modification 1 — 12-2 signal on total-return ETFs, monthly.**
*Weakness addressed:* single-stock momentum's cost/capacity problems (Lesmond et al. critique) and GEM's two-asset concentration (Petit's decomposition shows GEM's asset basket was a *handicap* — a static 46/28/25 mix returned 124bp *less* than the S&P; all excess came from timing). A 20–30 ETF universe diversifies the relative bet across equity regions, sectors, rates, credit, commodities.
*Rule:* `MOM_i(t) = TR_i(t−21) / TR_i(t−252) − 1` (total return, skip the last ~21 trading days). Rank descending.

**Modification 2 — Absolute-momentum gate per sleeve (dual momentum).**
*Weakness addressed:* pure relative momentum holds the *least-bad* asset in a crash. Antonacci's tables (fetched) attribute the drawdown halving (−54.6% → −23.0% on his equity module) to the T-bill hurdle.
*Rule:* asset i is investable only if `TR_i(t−21)/TR_i(t−252) > TR_bill(t−21)/TR_bill(t−252)` (12-2 excess return over T-bills > 0). If fewer than 3 assets pass, the residual weight goes to a cash/T-bill sleeve (BIL/SHV or 13-week bill ladder).

**Modification 3 — 52-week-high proximity filter (George & Hwang).**
*Weakness addressed:* relative-strength rotation buys "least bad" bounces deep below highs (dead-cat entries) — the names whose momentum is mean-reversion noise. GH show nearness to the 52w high is the dominant predictor and its returns don't reverse.
*Rule:* new entries require `P_i(t) / High252_i(t) ≥ 0.95`. Existing holdings are *not* force-sold on breaching 0.95 (avoid whipsaw); the filter gates entries and re-entries only. If a top-5 ranked asset fails the filter, skip to the next ranked asset that passes.

**Modification 4 — Sleeve-level volatility management (Barroso & Santa-Clara).**
*Weakness addressed:* momentum crashes are vol-regime events; BS show scaling by realized vol removed the worst crashes historically (worst month −79% → −28% in their stock-factor study).
*Rule:* compute the VMOM sleeve's own daily-return realized vol `σ_s` over the trailing 126 days, annualized. Scale gross exposure by `min(1.5, σ_target / σ_s)` with `σ_target = 12%` (BS's target), floor 0.25. Position-level sizing within the sleeve is inverse-vol: `w_i ∝ 1/σ_i` (σ_i = 63-day EWMA vol, λ = 0.94), normalized so Σw = current gross exposure.

**Modification 5 — Crash flag.**
*Weakness addressed:* BS scaling reacts at monthly rebalance; 2009-style momentum crashes unfold in weeks.
*Rule:* compute the sleeve's 21-day realized vol `σ_21` daily. If `σ_21 > 2 × median(σ_21, trailing 252 days)`, halve gross exposure within 1 trading day; restore to the Modification-4 level when `σ_21 < 1.5 ×` that median (hysteresis to avoid flag flutter).

## 5. Full specification of the twist variant

**Universe (28 ETFs, all US-listed, ADV > $50M, options-listed for tail hedging if desired).**
- US equity beta: SPY, QQQ, IWM, IWD (value), IWF (growth)
- US sectors: XLE, XLF, XLK, XLV, XLI, XLP
- Intl equity: EFA, EEM, EWJ, FXI
- Rates: TLT, IEF, SHY/BIL (cash sleeve benchmark)
- Credit: LQD, HYG
- Real assets: VNQ, GLD, SLV, DBC, USO, UUP
Universe reviewed annually; additions require 3 years of history.

**Data.** Daily adjusted total-return series (dividend-inclusive) for all ETFs; 13-week T-bill total return (or BIL) as the cash benchmark; no fundamentals needed.

**Signals (all computed at month-end close t):**

```
MOM12-2_i  = TR_i(t−21)/TR_i(t−252) − 1            # relative rank key
ABS_i      = MOM12-2_i  >  MOM12-2_bill            # absolute gate
H52_i      = P_i(t) / max(P_i, trailing 252 days)  # proximity; entry requires ≥ 0.95
σ_i        = EWMA vol of daily returns, λ=0.94, 63-day min window
σ_sleeve   = annualized stdev of sleeve daily returns, trailing 126d
σ_21       = annualized stdev of sleeve daily returns, trailing 21d
```

**Portfolio construction (monthly, at close, trade next open):**
1. Eligible = assets passing ABS gate.
2. Rank eligible by MOM12-2; tentatively select top 5.
3. Apply H52 entry filter: a tentatively selected asset already held is kept regardless of H52; a *new* entrant must have H52 ≥ 0.95, else take the next-ranked passer.
4. Base weights `w_i ∝ 1/σ_i` across the 5 selected.
5. Gross exposure `G = min(1.5, 0.12 / σ_sleeve)`, floored at 0.25; if crash flag active, `G ← G/2`.
6. Cash sleeve receives `1 − G×Σw` (and 100% when fewer than 3 assets pass ABS).
7. Trade only if the target weight differs from current by > 2pp or > 20% relative (banding to cut turnover); always trade on gate/flag changes.

**Risk limits.** Max 40% NAV per ETF at target; max 60% aggregate US-equity-beta (SPY/QQQ/IWM/IWD/IWF/sectors) weight; leverage cap 1.5×; crash flag as above; no single-day rebalance > 50% of NAV except crash-flag de-risking.

**Costs.** Assume 2 bp per side for the mega-liquid ETFs, 5 bp for SLV/USO/DBC/VNQ/sector funds, 10 bp stress; monthly rebalance with banding ⇒ expected turnover ~15–30%/month one-way in volatile regimes, < 10% in quiet ones (estimate — to be measured, not asserted).

**Worked rebalance example (illustrative, hypothetical — not a result):**

```
Month-end t. MOM12-2 ranks: QQQ +21.3%, XLK +19.8%, GLD +14.2%, EEM +9.1%, TLT +6.4%, SPY +5.9%, …
ABS gate (vs BIL +4.9% over the same 12-2 window): QQQ ✓, XLK ✓, GLD ✓, EEM ✓, TLT ✓, SPY ✓
Top-5 tentative: QQQ, XLK, GLD, EEM, TLT
H52 entry filter: QQQ 0.99 ✓ (held), XLK 0.97 ✓ (held), GLD 0.93 ✗ but already held → kept,
   EEM 0.91 ✗ and NOT held → skip to next ranked passer: TLT 0.96 ✓ enters, then SPY 0.98 ✓ enters
Final sleeve: QQQ, XLK, GLD, TLT, SPY
Inverse-vol base weights (σ: 22%, 24%, 15%, 9%, 17%) → w ∝ 1/σ ≈ 0.24, 0.22, 0.35, 0.58, 0.31 →
   normalized: 17%, 16%, 24%, 27%, 16%  (check: US-equity aggregate 49% ≤ 60% cap ✓; TLT 27% ≤ 40% ✓)
Sleeve vol σ_sleeve(126d) = 13.8% → G = min(1.5, 0.12/0.138) = 0.87
Crash flag: σ_21 = 19% vs 2× median(σ_21, 252d) = 2×8.1% = 16.2% → 19% > 16.2% → G ← 0.435
Final invested ≈ 43.5% of NAV across the five names; 56.5% to cash sleeve
```

**Parameter summary (pre-registered; all taken from the cited literature, none optimized):**

| Parameter | Value | Source |
|---|---|---|
| Relative signal | 12-2 total return (skip ~21 days) | JT93 skip convention; Antonacci no-skip noted as disagreement |
| Absolute gate | 12-2 excess over T-bills > 0 | Antonacci 2012/2013 |
| Selection | top 5 of 28 ETFs | desk choice; robustness {3,7} |
| Entry quality filter | P/High252 ≥ 0.95, entries only | George & Hwang 2004 |
| Sleeve vol target | 12% annualized, 126-day realized | Barroso & Santa-Clara 2015 |
| Leverage cap / floor | 1.5× / 0.25× | desk choice |
| Crash flag | σ_21 > 2× median(σ_21, 252d); restore < 1.5× | BS vol-spike logic, desk parametrization |
| Rebalance | monthly, next open; 2pp/20% bands | desk choice |
| Concentration caps | 40%/ETF, 60% US-equity aggregate | desk choice |

**Capacity.** Effectively unconstrained at desk scale ($100M+) given the instruments; the binding constraint is tracking error vs the signal, not market impact.

## 6. Failure modes & regime dependence

- **Bond-sleeve whipsaw (the post-2010 GEM disease).** Petit's replication: since 2010 the defensive months were exactly when the S&P ripped (34.1% annualized during GEM's defensive months). Fast V-shaped bears (2011, 2018, 2020, 2022 cited in the fetched article) recover before a 12-month signal can react. *Mitigation in VMOM:* the crash flag and vol scaling cut exposure faster than the absolute gate re-enters; the 5-asset relative sleeve means "defense" is often another risk asset, not just bills. *Early warning:* hit rate of ABS-gate switches (fraction of switches profitable after 3 months) < 45% over rolling 2 years.
- **Specification fragility.** Newfound: hundreds of bps/yr ride on 10- vs 12-month lookback. *Mitigation:* we pre-register 12-2 and accept it; robustness checks (§7) must show the result is not a single-lookback artifact, but we do not optimize the lookback in-sample.
- **Momentum crashes.** BS's −78.96% month (their raw WML) is the archetype: sharp reversals after crashes when the short/loser leg rips. Our long-only-ETF variant has no short leg, but rotation into last year's winners at the moment of regime turn (e.g., long energy into an oil collapse) is the analogous wound. *Early warning:* σ_21/σ_126 ratio > 1.5 (vol term-structure inversion of the sleeve) has historically preceded the worst momentum drawdowns — monitor even below the 2× crash-flag trigger.
- **Crowding/publication decay.** Momentum is the most crowded factor; McLean–Pontiff-style decay and the post-2010 GEM experience are consistent with a thinner edge. Assume the forward edge is *smaller* than any published backtest; size accordingly.
- **Rates/correlation regime.** A 2022-style joint stock-bond decline breaks both the relative sleeve (everything falls) and the defensive sleeve (bills fine, but IEF/TLT/LQD fail the ABS gate together with equities — that part worked in 2022 per the GEM replication narrative; the failure was re-entry timing). Correlation spikes make the 5-asset sleeve effectively 1–2 bets; the 60% US-equity cap exists for this.
- **Cash-sleeve drag in bull tapes.** With G frequently < 1 (vol scaling + crash flag), the strategy structurally underperforms a straight bull market in SPY — by design. This is a client-expectations failure mode more than a P&L one: document it, benchmark against 60/40 and the SG Trend Index, not against SPY alone.
- **Signal-skip interaction.** The 12-2 skip assumes the last month is reversal-prone; Antonacci reports non-equity assets do better *without* the skip. Our compromise (skip for all, since the universe is equity-heavy) is a known, pre-registered simplification; the no-skip variant is a mandatory robustness cell, and if it dominates persistently OOS, the skip rule is revisited at the annual review — never mid-year.
- **Trendless chop.** The worst regime: 2015–2016-style style whipsaw (Newfound) — repeated ABS flips with no follow-through. Expect 2–4% annual bleed in such years; the strategy must survive it, not avoid it.

**Monitoring dashboard (monthly, live):**

1. ABS-gate switch hit rate (fraction of gate flips profitable after 3 months), rolling 2 years — below 45% = the 2010s disease.
2. σ_21/σ_126 sleeve vol ratio — sustained > 1.5 is the pre-crash posture even below the 2× flag.
3. Realized turnover vs the 15–30%/month planning band; persistent excess ⇒ widen bands, don't tighten signals.
4. Sleeve composition concentration: effective number of bets (1/Σw²) < 2.5 ⇒ the "diversified" sleeve is one macro bet.
5. Tracking difference vs the unfiltered 12-2 top-5 benchmark (isolates what H52 + ABS + vol management each add).
6. Defensive-month opportunity cost: S&P return during cash-sleeve months, cumulative — the Petit diagnostic.
7. Crash-flag flutter count (flags per year; > 6 ⇒ hysteresis band too tight).
8. H52-filter rejection rate (share of top-5 ranks skipped for failing the 0.95 gate); a rate persistently > 40% means the filter, not momentum, is driving the book — review at annual meeting.
9. Cross-sleeve overlap with PEAD-IV and TURTLE-X books (same underlying exposure across strategies), reported to risk weekly.

## 7. Validation protocol

**Data.** Total-return ETF series back to inception, extended with underlying index total-return series for pre-inception history (document the splice; e.g., MSCI EAFE TR for EFA pre-2001); T-bill TR from Ibbotson/French library; delisting-free (ETFs rarely delist, but include dead ones — e.g., former universe members — to avoid selection bias in universe construction).

**Splits.** Chronological: 1993–2006 in-sample (parameter sanity only — parameters are *not* optimized, they are taken from the literature: 12-2, 0.95, 12%, 2×, 100-day equivalents), 2007–2016 validation, 2017–today out-of-sample. Report 2010–2026 separately to replicate the Petit failure window honestly — if VMOM also loses to SPY by ~5%/yr there, the document must say so.

**Pitfalls specific to this strategy.** (a) Index-splice look-ahead (using today's index methodology for 1990s data); (b) universe-selection survivorship (choosing 28 ETFs because they survived); (c) month-end execution assumption — trade at next open or VWAP, not the signal close; (d) dividend-timing errors in TR series; (e) the skip-month convention interacting with monthly rebalance dates (align t−21 to the rebalance date, not calendar month); (f) silent leverage — G up to 1.5 must be explicit in the equity curve.

**Robustness.** Lookback {6-1, 12-1, 12-2}; H52 threshold {0.90, 0.95, 1.00 (off)}; σ_target {10%, 12%, 15%}; top-N {3, 5, 7}; crash-flag multiple {1.75×, 2×, 2.5×}; rebalance monthly vs weekly; equal-weight vs inverse-vol. Acceptance requires the *median* variant to work, not just the headline.

**Additional mandatory robustness checks:**

- Subperiod grid: 1993–1999 / 2000–2009 / 2010–2019 / 2020–present, each reported standalone.
- Ex-US-only and ex-equities variants (does the edge survive without US mega-cap beta?).
- Signal decay curve: performance of entries as a function of days-since-signal (1, 5, 10, 21) — quantifies how stale a signal can get before the edge is gone.
- Vol-of-vol stress: re-run 2008–2009 and 2020 with the crash flag disabled to isolate its contribution.
- Randomized-entry placebo: same universe, same sizing, random eligible assets — the strategy must beat its own placebo distribution at the 95th percentile, not just beat zero.

**Acceptance criteria (pre-registered).** OOS (2017+) Sharpe ≥ SPY Sharpe − 0.1 with max DD ≤ 60% of SPY's; full-sample (1993+) positive alpha vs 60/40 at t ≥ 2; turnover ≤ 400%/yr; no single calendar year contributing > 35% of cumulative excess return; performance in 2010–2026 reported and explained, not hidden.

**Pre-registration checklist (freeze before any backtest run):**

1. Universe list and annual-review rule frozen (28 ETFs above; no cherry-picked additions).
2. All parameters frozen at the literature-sourced defaults (table in §5); robustness grid defined *around* them, not searched *for* them.
3. Execution assumption frozen: next-open fills, cost schedule as §5.
4. The four ablations defined in advance: (a) relative-only, (b) +ABS gate, (c) +H52 filter, (d) +vol management & crash flag — so each modification's marginal contribution is measured, not asserted.
5. The Petit failure window (2010–2026) designated a mandatory reporting segment.
6. Kill criteria defined: two consecutive calendar years with ABS-switch hit rate < 40% AND Sharpe < 0 ⇒ strategy retired to research, not re-tuned live.

## 8. Sources read (annotated)

All accessed 2026-10-07.

1. **"Returns to Buying Winners and Selling Losers" — Jegadeesh & Titman (1993), JF 48(1).** Full PDF fetched (https://www.bauer.uh.edu/rsusmel/phd/jegadeesh-titman93.pdf). *Taken:* the 16+16 strategy design (J,K, skip-week); 1.31%/mo (12/3) and 1.49%/mo with skip (t = 4.28); ~1%/mo for 6-month formation; 9.5% 12-month gain losing >half over months 13–36; earnings-announcement return pattern of winners/losers; the Levy (1967)/Jensen–Bennington selection-bias history.
2. **"The 52-Week High and Momentum Investing" — George & Hwang (2004), JF 59(5).** Full PDF fetched (https://www.bauer.uh.edu/tgeorge/papers/gh4-paper.pdf). *Taken:* the P/High52 ranking variable; Table I (0.45–0.48%/mo parity across JT/MG/52wH) and Table II ex-January numbers (1.23%/mo, t = 7.06, vs JT 1.07%); nested-dominance result; no long-run reversal; January tax-loss interpretation.
3. **"Time Series Momentum" — Moskowitz, Ooi & Pedersen (2012), JFE 104(2).** Full PDF fetched (https://w4.stern.nyu.edu/facdir/lpederse/papers/TimeSeriesMomentum.pdf). *Taken:* 58-instrument universe and data table; the EWMA ex-ante vol estimator (center of mass 60 days, applied t−1 to t — their no-look-ahead convention we adopt); 1/σ position sizing; sign-based TSMOM rule; alpha t-stat table (12-month/1-month t = 6.61 all-assets); continuation-then-reversal term structure; speculators-profit-at-hedgers'-expense; best-in-extreme-markets.
4. **"Momentum Has Its Moments" — Barroso & Santa-Clara (2015), JFE 116(1).** Full PDF fetched (http://www.snifferquant.com/gyantal/Incode/papers/Momentum%20Has%20Its%20Moments(scaling%20Momentum%20by%20vol),2014.pdf) plus SSRN page (https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2041429). *Taken:* 6-month realized-vol scaling to a 12% target; Sharpe 0.53→0.97; worst month −78.96%→−28.40%; max DD −96.69%→−45.20%; kurtosis/skew numbers; variance OOS R² 57.82%; turnover-neutrality claim; the Lesmond et al. cost caveat they flag.
5. **"Risk Premia Harvesting Through Dual Momentum" — Antonacci (SSRN 2042750).** Full PDF fetched (https://www.trendfollowing.com/whitepaper/SSRN-id2042750.pdf). *Taken:* relative vs absolute momentum definitions; T-bill hurdle/alternative-asset mechanic; the no-skip-month choice and its justification; equity module table (15.79%/12.77%/0.73/−23.01% vs indices); credit/REIT/stress module numbers; the four public 12-month momentum products note.
6. **"Absolute Momentum: A Simple Rule-Based Strategy and Universal Trend-Following Overlay" — Antonacci (2013, SSRN 2244633).** Full PDF fetched (https://www.naaim.org/wp-content/uploads/2013/10/00D_Absolute-Momentum_gary_antonacci.pdf). *Taken:* absolute momentum as regime-change identifier; lookback as the sole parameter; overlay usage on 60/40 and risk parity; Cowles & Jones 1937 lineage note.
7. **"Is Gary Antonacci's Global Equity Momentum Strategy Robust?" — SVRN blog (2015).** Fetched (https://www.svrn.co/blog/2015/8/2/is-gary-antonaccis-global-equity-momentum-strategy-robust). *Taken:* independent replication success; robustness to stale/lagged windows (GEM1-12, GEM6-6); extension to 1926; the data-mining caveat on the 12-month window; author's live-since-2011 experience.
8. **"Fragility Case Study: Dual Momentum GEM" — Newfound / Flirting with Models (2019).** Fetched (https://blog.thinknewfound.com/2019/01/fragility-case-study-dual-momentum-gem/). *Taken:* model-specification-risk framing; 2011 specification whipsaw vs late-2015/early-2016 style whipsaw distinction; "risk cannot be destroyed, only transformed."
9. **"GEM Replicated for 1971–2026: What Held Up, What Didn't" — globalequitymomentum.com (2026)** (https://www.globalequitymomentum.com/articles/petit-gem-replication-1971-2026) and the underlying **Petitmarius/Backtest_Strategies GitHub** (https://github.com/Petitmarius/Backtest_Strategies), both fetched. *Taken:* Petit replication numbers (CAGR 15.18%, Sharpe 0.83, max DD −21.66%, alpha 6.61% t = 4.31); 2010–2026 −4.8%/yr vs S&P 500; 34.1% vs 5.3% defensive-month asymmetry; ~75%/25% bond-whipsaw/non-US decomposition; "published record established almost entirely before publication" quote.
10. **"Book Review: Dual Momentum Investing" — Alpha Architect.** Fetched (https://alphaarchitect.com/book-review-dual-momentum-investing/). *Taken:* credibility assessment of Antonacci's backtests and factor-regression alphas; the "breezy and imprecise" critique.

**Not accessed (secondary citation only):** Lesmond, Schill & Zhou (2004); Moskowitz & Grinblatt (1999); McLean & Pontiff (2016); Daniel & Moskowitz (2016) momentum-crashes paper (recommended next).

## 9. Further reading

- Daniel & Moskowitz (2016, JFE), "Momentum Crashes" — the deep dive behind BS's crash numbers.
- Novy-Marx (2012), "Is momentum really momentum?" — intermediate-horizon decomposition (relevant to the 12-2 choice).
- Asness, Moskowitz & Pedersen (2013, JF), "Value and Momentum Everywhere."
- Della Corte, Kosowski & Papanikolaou — momentum with volatility scaling extensions.
- Greyserman, *Trend Following with Managed Futures* — bridge to document 09.
- Antonacci, *Dual Momentum Investing* (2014) — the book itself for the GEM retail spec.
- Rouwenhorst (1998, JF), "International Momentum Strategies" — cross-country replication.
- Chabot, Ghysels & Jagannathan — momentum in pre-CRSP (Victorian-era) data.
- Israelov & Nielsen (AQR), "Covered Call Strategies: One Fact and Eight Myths" — unrelated topic but its vol-scaling framing is a useful cross-check on our σ_target choice.
