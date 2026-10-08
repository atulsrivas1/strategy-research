# 06. Pairs Trading / Statistical Arbitrage — Twist: KALMAN-BASKET

> **Library:** Sigmatiq Strategy Library | **Bucket:** Swing (1–10 days) | **Style:** Market-neutral relative-value mean reversion (long/short baskets)
> **Instruments:** US equities (long and short legs), GICS-industry-constrained | **Typical holding period:** 2–15 trading days (gated by spread half-life) | **Complexity (1–5):** 5 | **Evidence grade (A–C):** B for the base anomaly (peer-reviewed, replicated, decay documented); C for our specific enhancements (untested here)
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise. This library contains no local backtests yet.

---

## 1. Origin & lineage

**Practitioner origin (desk lore, documented in the academic paper).** Gatev, Goetzmann & Rouwenhorst (2006, *Review of Financial Studies* 19(3):797–827 — full text read for this document) open with the history: "In the mid-1980s, the Wall Street quant Nunzio Tartaglia assembled a team of physicists, mathematicians, and computer scientists to uncover arbitrage opportunities in the equities markets" at Morgan Stanley. The group traded pairs "with great success in 1987 — a year when the group reportedly made a $50 million profit for the firm," and disbanded in 1989 after two bad years. D.E. Shaw's David Shaw (a Tartaglia protégé) is quoted attributing his firm's edge partly to early entry — an early crowding observation. Tartaglia's own explanation was behavioral: "... Human beings don't like to trade against human nature, which wants to buy stocks after they go up not down" (Hansell 1989, as quoted in GGR).

**Academic canonization.** GGR (circulated 1999 as Yale ICF working paper / NBER w7032; published RFS 2006) is the reference implementation of the **distance method**: match stocks by minimum sum of squared deviations between normalized cumulative-total-return series over 12 months; trade the next 6 months; open at 2σ divergence; close at crossing. The SSRN page (abstract 141615) and NBER page (w7032) corroborate the versioning: the 1999 draft covered 1962–1997 with "up to 12 percent" annualized excess returns; the published version extends to 2002 and adds a true 1999–2002 holdout.

**Vidyamurthy (2004).** *Pairs Trading: Quantitative Methods and Analysis* (Wiley) — the standard practitioner text covering the cointegration framework, the error-correction view, and time-varying parameter estimation for hedge ratios. **Not accessed this session** (no open full text found); known via secondary citation. Flagged honestly; its role in our design (cointegration + time-varying hedge ratios) is implemented via the QuantStart/Chan lineage instead.

**Cointegration lineage.** GGR themselves interpret price-space matching through Bossaerts (1988) co-integration of security prices and Engle–Granger (1987): "certain assets are weakly redundant, so that any deviation of their price from a linear combination of the prices of other assets is expected to be temporary and reverting." They explicitly note that strategies on "trios, quadruples, and so on ... would presumably capture more co-integrated prices and would yield better profits" — a direct academic invitation to our basket construction.

**Decay literature.** Do & Faff (2010), "Does Simple Pairs Trading Still Work?", *Financial Analysts Journal* 66(4):83–95 — replicated GGR through June 2009 and documented the decline (§3). This is the paper that shapes our design more than any other.

## 2. The original rules (as published — GGR 2006)

**Universe/screen.** CRSP daily files; drop any stock with one or more no-trade days in the formation period (liquidity screen).

**Formation (12 months).** Build a cumulative total-return index per stock (dividends reinvested), normalized to 1 at formation start. Match each stock with the partner minimizing the sum of squared deviations (SSD) between the two normalized price series — "exhaustive matching in normalized daily price space." Sector-restricted variants match within S&P broad groups (Utilities, Transportation, Financials, Industrials by SIC).

**Trading (next 6 months).** Trade the top 5, top 20, and pairs 101–120 by smallest distance. Rules:

- Open a long–short position ($1 long the lower-priced / $1 short the higher-priced normalized series) when prices diverge by more than **2 historical standard deviations** (σ estimated over the formation period).
- Unwind at the **next crossing** of the normalized prices.
- If no crossing before period end, close at the last trading day of the trading interval.
- Delisting: close the pair using the delisting return or last available price. Robustness: under an extreme −100% long-delisting assumption the top-20 portfolio still earned 1.32%/mo with SD 1.9%.
- Panel A opens/closes at end of day of divergence/crossing; Panel B waits one day (bid-ask-bounce control).
- Overlapping 6-month portfolios started monthly and averaged (Jegadeesh–Titman style) — interpreted as a desk of six staggered traders.

**Published results (all GGR claims, 1963–2002, 474 months).**

| Portfolio | Fully invested excess return | t-stat (NW) | Committed capital | Months < 0 |
| --- | --- | --- | --- | --- |
| Top 5 (no wait) | 1.31%/mo | 8.84 | 0.78%/mo | 26% |
| Top 20 (no wait) | 1.44%/mo | 11.56 | 0.81%/mo | 15% |
| Pairs 101–120 | 1.08%/mo | 11.54 | 0.68%/mo | 21% |
| Top 20 (1-day wait) | 0.90%/mo | 9.29 | 0.52%/mo | 23% |

- Headline: "average annualized excess returns of up to 11% for self-financing portfolios of pairs."
- One-day wait costs 30–55 bp/month (fully invested) — "a nontrivial portion of the profits ... may be due to bid–ask bounce."
- Implied transaction-cost estimate from the wait-a-day haircut: 162 bp per pair per round trip (≈ 81 bp effective spread); net profits after conservative costs: 113–225 bp per pair per 6 months — "economically and statistically significant."
- Trading stats: average 2σ trigger = 4.76% price divergence (top 5); ~2.02 round trips per pair per 6 months; average open duration **3.75 months** — note: the original is a *medium-term* strategy, far longer than our swing bucket; our variant deliberately re-horizons it.
- Composition: top pairs skew large-cap (74% of top-20 in top-3 size deciles; 91% in top-5) and heavily to **Utilities (71% of top-20)** — low-vol, rate-sensitive names pair best in price space. 20–44% of pairs are mixed-sector.
- Sector-restricted results (1-day wait, top-20): Utilities 1.08%/mo (t = 10.26), Financials 0.78%/mo (t = 7.60), Industrials 0.61%/mo (t = 6.93), Transportation 0.58%/mo (t = 4.26) — "profitable in every broad sector category."
- Risk: pairs Sharpe ratios "between four and six times larger than the Sharpe Ratio of the market"; returns positively skewed (skewness 1.39 for top-20), so Sharpe is not inflated by negative-skew illusion.
- Holdout: 1999–2002 (post-working-paper) top-20 fully invested: **10.4%/yr, SD 3.8%, Newey–West t = 4.82** — a genuine out-of-sample confirmation at publication time.
- Bankruptcy-risk asymmetry test: profits are *not* concentrated in the long (loser) leg, arguing against a pure default-premium explanation; they link profitability to a latent common factor "correlated with the returns to pairs trading," dormant recently — compensation "for enforcing the 'Law of One Price.'"

**Known disagreements / variants in the literature.**

- *Distance vs cointegration:* GGR's SSD matching is atheoretic but robust; the cointegration school (Vidyamurthy 2004; later Huck and others) selects pairs on formal cointegration tests and estimates hedge ratios by regression. Do & Faff (2010) note "alternative algorithms combined with other measures enhance trading profits considerably, by 22 bps a month for bank stocks."
- *Entry threshold:* GGR chose 2σ as practitioner convention and explicitly declined to optimize ("the danger in data-snooping refinements outweigh the potential insights"); their footnote 6: "The optimal trigger point in terms of profitability may actually be much higher than two standard deviations."
- *Return computation:* committed-capital vs fully-invested differ ~2× (0.81% vs 1.44%/mo) — any replication must state which it reports. We report both (GGR convention).

## 3. Why it works — mechanism & evidence

**Mechanism (per the literature).**

1. **Law of One Price / near-LOP:** close substitutes should be priced alike; temporary deviations revert. GGR frame pairs trading as a test of near-LOP under stationarity, with arbitrageurs paid for enforcing it: "the marginal profits to be had from risk arbitrage of these temporary deviations is crucial to the maintenance of first-order efficiency."
2. **Co-integrated prices with common nonstationary factors:** long and short legs share factor exposures; the residual spread is (weakly) stationary. This grounds the reversion expectation without claiming market inefficiency (Bossaerts 1988; Engle–Granger 1987, as cited in GGR).
3. **Behavioral overreaction to idiosyncratic news:** Tartaglia's human-nature quote; GGR link to Jegadeesh–Titman (1995) contrarian profits from overreaction to company-specific shocks. GGR's bootstrap against random pairs shows the effect differs from plain reversal profits.
4. **Limits to arbitrage sustain the premium:** fundamental risk, noise-trader risk, synchronization risk (Do & Faff's decomposition).

**Decay / crowding evidence (the part that shapes our design).**

- Do & Faff (2010), FAJ 66(4), extended GGR to June 2009: top-20 mean excess return fell **0.86%/mo (1962–1988) → 0.37%/mo (1989–2002) → 0.24%/mo (2003–2009)**.
- Their attribution: the hedge-fund-competition ("market efficiency") story is "only partly to blame"; **worsening arbitrage risks — especially more frequent non-convergence — explain up to 70% of the drop in profits.**
- Regime finding: pairs trading performed *particularly strongly* during the 2000–02 bear market and the 2007–09 GFC — "the increase in arbitrage risks during these periods of panic was outweighed by a corresponding decrease in market efficiency."
- Design implication: the binding problem is **pair breakage / non-convergence**, not signal crowding. Our twist attacks exactly this: baskets dilute single-name structural breaks, Kalman hedge ratios track drifting relationships, and the half-life gate refuses spreads that are not currently reverting.

**Evidence on our enhancement components (honestly mixed).**

- *Kalman dynamic hedge ratio:* QuantStart (Chan 2012 lineage; article read in full) demonstrates on TLT/IEI that the regression slope "changes dramatically over the 2011 to 2016 period, dropping from around 1.38 in 2011 to around 0.9 in 2016. It is not difficult to see that utilising a fixed hedge ratio in a pairs trading strategy would be far too rigid." Their rules: trade the Kalman forecast error e_t against ±√Q_t (prediction standard deviation), exit on reversion; parameters δ = 1e-4 (system noise), v_t = 1e-3 (measurement noise), 2-day burn-in.
- *Counter-evidence:* an independent 2017–2025 ETF-pairs study (IvanKostyuk94/pairs-trading-kalman, repository read) found dynamic hedge ratios give only *pair-specific* benefits — rolling OLS beat Kalman on GDX/IAU (Sharpe −0.03 vs −0.11); Kalman produced higher cumulative PnL but *lower Sharpe* on SLV/GLD (2025 silver-squeeze drawdown); plain static OLS dominated KBE/XLF; the hypothesis that Kalman helps most where β is unstable was *not* supported; a GARCH signal overlay underperformed a simple rolling z-score. We therefore treat the Kalman layer as a hypothesis to validate per-industry, not an established improvement.
- *Half-life / Hurst gating:* practitioner references (Quantt; QuanterLab; Hudson & Thames — all read) converge on: OU half-life t½ = ln2/θ (discrete AR(1): t½ = −ln2/ln(1+β)); tradable sweet spot ≈ 5–30 daily bars; < 5 bars is microstructure noise; 30–100 is capital-intensive; > 100 or negative = walk away; H < 0.5 required for mean reversion (H = 0.5 random walk, H > 0.5 trending). Hudson & Thames warn θ estimators are *biased upward* in finite samples ("the model is often too optimistic, because faster mean-reversion indicates more profit") and unreliable with < ~1 year of daily data or < ~20 mean-crossings — our gate uses 2–20 days, but *estimation* uses 252-day windows and we demand ≥ 15 crossings in-window.

## 4. The twist: KALMAN-BASKET

Four modifications, each mapped to a documented weakness.

### (a) Sector-neutral baskets replace single pairs (5–10 names per side within one GICS industry)

*Weakness addressed:* single-pair breakage — the dominant decay driver per Do & Faff (non-convergence = one leg's structural break: M&A, bankruptcy, business-model change). GGR's composition table shows the method's concentration (71% utilities in top-20) and their own remark that trios/quadruples should capture more co-integration.

Construction: within each GICS industry group (24 groups), each formation date:

1. Compute 252-day residual returns per name: r̃_i,t = r_i,t − β̂_i,mkt · r_mkt,t − β̂_i,sec · r_sec,t (rolling 252-day betas).
2. Rank by 21-day cumulative residual: the **long basket** = the 5–10 most negative names; the **short basket** = the 5–10 most positive. n = min(10, floor(N_industry / 4)), floor 5; skip the industry that cycle if N < 12.
3. Equal-volatility weights within each basket (w_i ∝ 1/σ_i,20d).

One industry = one spread = industry-neutral by construction. Baskets keep the GGR "close substitutes" logic but make the substitute a *portfolio*, which is far harder to break structurally.

### (b) Dynamic hedge ratio via Kalman filter (replaces static OLS / $1:$1)

*Weakness addressed:* GGR's $1-long/$1-short and OLS-based variants freeze the relative-pricing relation for 6 months while it drifts (QuantStart's TLT/IEI slope moved 1.38 → 0.9).

State-space model per industry spread (QuantStart/Chan formulation):

- State: θ_t = [intercept_t, slope_t]′, random-walk transition: θ_t = θ_{t−1} + w_t, with W_t = (δ / (1−δ)) · I, δ = 1e-4 (sweep {1e-5, 1e-4, 1e-3}).
- Observation: y_t = F_t θ_t + v_t, where y_t = log P_long-basket,t, F_t = [1, x_t], x_t = log P_short-basket,t, measurement noise v_t, Var = V = 1e-3.
- Kalman recursions (strictly causal — filter, never smoother):
  - Prediction: θ_{t|t−1} = θ_{t−1}; R_t = C_{t−1} + W_t.
  - Forecast error: e_t = y_t − F_t θ_{t|t−1}.
  - Prediction variance: Q_t = F_t R_t F_t′ + V.
  - Kalman gain: A_t = R_t F_t′ / Q_t.
  - Update: θ_t = θ_{t|t−1} + A_t e_t; C_t = R_t − A_t F_t R_t.
- Outputs used for trading: hedge ratio β_t = θ_t[1]; spread series s_t = y_t − β_t x_t (log space); 60-day burn-in per vintage before trading.

Per the counter-evidence (§3), we benchmark Kalman against rolling-60-day OLS and static-252-day OLS per industry and keep the winner per industry chosen on *training* data only — no ex-post cherry-picking.

### (c) Hurst / half-life regime gate

*Weakness addressed:* entering spreads that are not currently mean-reverting (Do & Faff's non-convergence). Gate per industry spread, computed on the past 252 days of Kalman residuals, refreshed daily:

- AR(1) fit on s_t: Δs_t = a + b · s_{t−1} + ε_t → half-life t½ = −ln 2 / ln(1 + b). Trade only if **2 ≤ t½ ≤ 20 trading days** (swing-bucket bounds, inside the 5–30 practitioner sweet spot, allowing fast institutional spreads).
- Hurst exponent (R/S on residuals): **H < 0.5** required.
- ≥ 15 mean-crossings in the window (Hudson & Thames reliability floor).
- ADF test on residuals, p < 0.10 (loose threshold per practitioner guidance; strict 0.05 discards genuinely reverting noisy spreads).
- Gate failure while flat → no entries. Gate failure while in a position → exit at next close ("half-life breach" exit).

### (d) Z-score bands with a hard stop: enter ±2.0, exit ∓0.5, stop ±3.5

*Weakness addressed:* GGR's exit-at-crossing can hold losers for months (avg 3.75 months) — incompatible with the swing bucket and with risk control; their 2σ entry has no disaster stop.

- z_t = (s_t − mean_60(s)) / std_60(s) on Kalman residuals.
- Enter long-spread (long long-basket / short short-basket) at z ≤ −2.0; short-spread at z ≥ +2.0.
- Exit at z ≥ −0.5 (long spread) / z ≤ +0.5 (short spread) — not waiting for the full crossing harvests the reliable middle of the reversion.
- Hard stop at z = ∓3.5 (the spread blew out another 1.5σ against us — statistically, most such continuations are structural breaks, not noise) OR half-life breach OR 15-session time stop (≈ 3× the max gated half-life).
- Re-entry allowed after 5 sessions if the gate re-passes.

## 5. Full specification of the twist variant

**Universe.** US common stocks, top ~1,500 by market cap; price > $5; 60-day ADV ≥ $10M; GICS industry-group membership with ≥ 12 eligible names (else the industry is skipped that cycle); ≥ 260 days of history. Exclude announced M&A targets and hard-to-borrow names (borrow rate > 2%/yr or utilization > 80%). Point-in-time index membership and GICS codes mandatory.

**Data.** Daily OHLCV total-return-adjusted; point-in-time GICS; shares/market cap; borrow rates and utilization (cost model and exclusions); delisting returns.

**Formation & signals (daily close).**

1. Per industry: residual returns per §4a step 1.
2. Basket ranking per §4a step 2; weights per step 3; re-formed every 21 days on a staggered schedule — 3 staggered vintages per industry (GGR-style overlapping portfolios).
3. Kalman filter per industry spread per §4b → β_t, e_t, Q_t, s_t. 60-day burn-in per new vintage.
4. Gate per §4c: t½ ∈ [2, 20], H < 0.5, ≥ 15 crossings, ADF p < 0.10.
5. z_t per §4d on a 60-day window of s_t; entries/exits/stops per §4d.

**Sizing & risk limits.** Dollar-neutral per industry spread (long notional = short notional, β-adjusted via the Kalman slope). Per-spread risk budget: 0.5% of equity at the 3.5σ stop distance (spread vol from Q_t). Max 12 concurrent industry spreads; gross ≤ 6× equity (0.5× per spread); net ≤ 10% (baskets are industry-neutral but not factor-perfect); single-name cap 3% of equity per leg; borrow cost charged daily on short legs.

**Worked trade lifecycle (illustrative mechanics, not a result).** Industry spread s_t gated at t½ = 6 days, H = 0.41, 22 crossings. z falls to −2.1 → enter long-spread: $5M long the underperforming basket, $5M × β_t short the outperforming basket. Day 4: z = −0.4 → exit at the ∓0.5 band (harvested ≈ 1.6σ of reversion). Counter-case: day 2, z = −3.6 → hard stop; loss ≈ 1.5σ × spread vol = the 0.5% risk budget. Counter-case 2: day 9, gate recomputes t½ = 26 days → half-life breach exit at market regardless of z.

**Original vs twist — side-by-side register.**

| Dimension | GGR 2006 (as published) | KALMAN-BASKET (this spec) |
| --- | --- | --- |
| Unit of trade | Single stock pair (min-SSD match) | Industry basket vs basket (5–10 names/side) |
| Matching space | Normalized cum-total-return price space | Residual-return space (market + sector removed) |
| Hedge ratio | $1 long / $1 short (implicitly static) | Kalman β_t (or bake-off winner), updated daily |
| Formation | 12 months, then trade 6 months | 252-day estimation, baskets re-formed every 21 days, 3 staggered vintages |
| Regime gate | None | t½ ∈ [2,20] days, H < 0.5, ≥ 15 crossings, ADF p < 0.10 |
| Entry | divergence > 2σ (formation σ) | z ≤ −2.0 / z ≥ +2.0 (60-day residual z) |
| Exit | next crossing of normalized prices | z band ∓0.5; stop ±3.5; half-life breach; 15-session time stop |
| Expected hold | 3.75 months average (their Table 2) | 2–15 sessions by construction |
| Return basis | committed vs fully invested (report both) | same convention retained |
| Key published result | 1.44%/mo top-20 fully invested, 1963–2002 (GGR); 0.24%/mo by 2003–09 (Do & Faff) | none — no local backtest yet |

**Kalman parameter register (freeze before any run).**

| Parameter | Value | Source / rationale |
| --- | --- | --- |
| δ (system noise scale) | 1e-4 (sweep {1e-5, 1e-4, 1e-3}) | QuantStart/Chan default; controls β_t responsiveness |
| V (measurement noise) | 1e-3 | QuantStart/Chan default |
| Burn-in | 60 days per vintage | QuantStart used 2 days on ETFs; baskets need longer (state variance stabilization) |
| z window | 60 days | swing-bucket horizon match |
| Gate window | 252 days | Hudson & Thames reliability floor (≥ ~1yr daily data) |
| Crossing floor | 15 per gate window | Hudson & Thames (≥ ~20 recommended; 15 chosen, swept in robustness) |
| Vintage spacing | 21 days × 3 | GGR-style staggered overlapping portfolios, re-horizoned |

**Costs.** Commissions $0.005/share/side; slippage 3 bps/side large-cap; **borrow: actual rate per name per day (median large-cap general-collateral ≈ 30–50 bp/yr; stress pass at 200 bp/yr on all shorts)**; 21-day vintage-roll rebalance costs. GGR's own estimate (162 bp/round trip in their era) is the stress-case sanity anchor; modern large-cap explicit costs are far lower, but borrow is the real P&L leak.

**Capacity.** Baskets of large caps: $100–500M realistic before spread impact erodes the ~0.5–1σ harvested move; the 21-day re-formation is the capacity-binding turnover, not the entries.

**Daily loop pseudocode.**

```text
for each trading day t:
    for each industry g with active vintages v:
        update residual returns, basket membership (on roll dates)
        step Kalman filter -> beta_t, e_t, Q_t, s_t
        if burn-in < 60 days: continue
        recompute gate: half_life, H, crossings, ADF
        z <- (s_t - mean60(s)) / std60(s)
        if position open in (g, v):
            if gate fails: exit at close            # half-life breach
            elif |z| >= 3.5: exit at close          # hard stop
            elif long_spread and z >= -0.5: exit    # target band
            elif short_spread and z <= 0.5: exit
            elif days_held == 15: exit at close     # time stop
        else:
            if gate passes and z <= -2.0: enter long-spread
            elif gate passes and z >= 2.0: enter short-spread
```

## 6. Failure modes & regime dependence

1. **Structural breaks / non-convergence (the #1 killer, per Do & Faff):** M&A on one leg, bankruptcy, regulatory regime change for an industry. Baskets dilute but do not eliminate — an industry-level shock hits all names on one side (e.g., a bank-crisis spread). The ±3.5σ stop and half-life breach exit exist for exactly this.
2. **Arbitrage-risk regimes:** Do & Faff show profits *rise* in panics (2000–02, 2007–09) but so does variance; margin/borrow recalls in crises can force exits at the worst z. Borrow monitoring is a first-class risk feed, not an afterthought.
3. **Kalman mis-specification:** δ too large → the hedge ratio chases noise and the spread is non-stationary by construction; δ too small → effectively static OLS. The 2017–2025 independent study found no uniform Kalman advantage — hence the per-industry bake-off (§4b) rather than blind adoption.
4. **Half-life estimation bias:** θ overestimated in finite samples (Hudson & Thames) → the gate passes spreads whose true half-life is longer → slow bleeds. Mitigation: the 15-crossing floor, 252-day windows, and the 15-session time stop.
5. **Sector drift / factor crashes:** industry-neutral is not factor-neutral; a momentum crash or rate shock can move both baskets asymmetrically (growth vs value tilt inside an industry). Monitor per-spread factor residuals; kill-switch if aggregate net factor exposure exceeds 2× its historical 95th percentile.
6. **Crowding 2.0:** stat-arb baskets are standard industry practice; our edge claim is execution + gating, not novelty. Expect capacity-limited, modest Sharpe; the literature's 11%/yr era is over (0.24%/mo by 2003–2009 for the naive version, per Do & Faff).
7. **Early-warning indicators:** rolling 6-month per-spread hit rate < 45%; stopped trades (±3.5σ) > 25% of exits (regime of breaks); median gated half-life drifting > 15 days across the book (reversion slowing); aggregate short-book borrow > 150 bp/yr; z-crossing count per spread per quarter falling (spreads trending, not oscillating).

## 7. Validation protocol

**Data needs.** Survivorship-free US equities with delisting returns (CRSP-class), 1990–2026; point-in-time GICS; borrow rates (2010–; before that, proxy by utilization deciles); corporate actions. No ETF substitution for the stock legs in validation (basket behavior differs).

**Chronological splits (designed to replicate the published decay curve first).**

- **Replication gate:** reproduce GGR's distance-method top-20 on 1962–2002 (or 1990–2002 given data availability) and Do & Faff's 2003–2009 decline *qualitatively* before trusting the engine on our variant. Targets: top-20 fully-invested ≈ 1.4%/mo in-sample era, falling to ≈ 0.2–0.4%/mo post-2003.
- **Train:** 2000–2012. **Validation:** 2013–2019. **Test:** 2020–2026 (includes the 2020 crash — where the literature says pairs should do *well* — and the 2022 rate shock).
- **Walk-forward:** parameters (δ, z-bands, gate bounds) frozen per 2-year fold.

**Cost/slippage model.** As §5, with three borrow regimes (actual / flat 100 bp / flat 300 bp stress) and a "no-borrow-alpha" report separating short-leg alpha from long-leg alpha (GGR's asymmetry check is the template).

**Strategy-specific pitfalls.**

- *Look-ahead:* GICS reclassifications, index additions, betas and residuals from trailing windows only; the Kalman state must be strictly causal (filter, never smoother).
- *Survivorship/delisting:* mandatory; repeat GGR's −100% long-delisting robustness test on our variant.
- *Borrow feasibility:* a backtest that shorts hard-to-borrow names at GC rates is fiction; exclude or charge actual rates.
- *Multiple comparisons across industries:* 24 industries × parameter grid invites selection; use the bake-off protocol (per-industry model selection on train only) and report the cross-industry distribution, not the best industry.
- *Overlapping vintages:* GGR-style staggered portfolios induce autocorrelation — Newey–West or block-bootstrap all t-stats.
- *z-band data-snooping:* GGR deliberately did not optimize the 2σ trigger; we pre-register {±2.0 / ∓0.5 / ±3.5} and report the plateau around it.

**Robustness checks.** Entry z {1.5, 2.0, 2.5}; exit z {0, 0.5, 1.0}; stop z {3.0, 3.5, 4.5}; half-life gate {[2,20], [3,15], [5,30], off}; basket size {5, 7, 10}; formation {126, 252, 504} days; hedge model {Kalman, rolling-OLS-60, static-OLS-252} per industry; vintage spacing {10, 21, 42} days.

**Acceptance criteria (pre-registered).** Test period 2020–2026, net of stress borrow: Sharpe ≥ 1.0 on committed capital; max DD ≤ 8%; ≥ 300 spread-trades; hit rate ≥ 55%; average hold ≤ 12 sessions; positive P&L in ≥ 60% of industries traded; and the gated variant must beat the ungated variant on Sharpe by ≥ 0.2 (else the gate is dead weight). Report committed-capital and fully-invested returns separately (GGR convention).

## 8. Sources read (annotated)

1. **Gatev, E., Goetzmann, W.N., Rouwenhorst, K.G., "Pairs Trading: Performance of a Relative-Value Arbitrage Rule", RFS 19(3):797–827, 2006 (full PDF).** URL: http://stat.wharton.upenn.edu/~steele/Courses/434/434Context/PairsTrading/PairsTradingGGR.pdf — accessed 2026-10-07. Read in full (Sections 1–3 incl. all tables). Taken: Tartaglia/Morgan Stanley history ($50M in 1987, disbanded 1989, Shaw and Tartaglia quotes); exact formation/trading rules (12m/6m, SSD matching, 2σ open, crossing close, delisting handling, one-day-wait variant, monthly-staggered portfolios); full results (1.44%/mo top-20 fully invested, t = 11.56; 0.81% committed; 0.90% with wait; 162 bp implied round-trip cost; net 113–225 bp/pair/6mo; 3.75-month avg holding; 4.76% avg trigger; 71% utilities; size-decile composition; sector-restricted results); risk analysis (Sharpe 4–6× market; positive skewness 1.39); 1999–2002 holdout 10.4%/yr, t = 4.82; co-integration interpretation (Bossaerts 1988; trios/quadruples remark); bankruptcy-risk asymmetry test; −100% delisting robustness footnote. Corroborating pages read: SSRN abstract https://papers.ssrn.com/sol3/papers.cfm?abstract_id=141615 and NBER w7032 https://www.nber.org/papers/w7032 (version history; the 1999 draft covered 1962–1997 with "up to 12 percent").
2. **Do, B.H. & Faff, R., "Does Simple Pairs Trading Still Work?", FAJ 66(4):83–95, 2010.** URLs: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1656954 and https://ideas.repec.org/a/taf/ufajxx/v66y2010i4p83-95.html — accessed 2026-10-07 (abstracts plus full synthesis text). Taken: the decay series 0.86% → 0.37% → 0.24%/mo across 1962–88 / 1989–2002 / 2003–09; the attribution finding that worsening arbitrage risks (non-convergence frequency) explain up to 70% of the decline, with hedge-fund competition only partly to blame; strong performance in 2000–02 and 2007–09; the +22 bp/mo enhancement note for bank-stock algorithms.
3. **QuantStart, "Kalman Filter-Based Pairs Trading Strategy In QSTrader".** URL: https://www.quantstart.com/articles/kalman-filter-based-pairs-trading-strategy-in-qstrader/ — accessed 2026-10-07. Read in full. Taken: the complete causal Kalman pairs machinery (state θ_t = [intercept, slope]; forecast error e_t; prediction variance Q_t; entries at e_t < −√Q_t / e_t > +√Q_t; exits on reversion; δ = 1e-4, v_t = 1e-3; burn-in; TLT/IEI implementation; attribution to Ernest Chan 2012 and Aidan O'Mahony's Quantopian test; the full Python class skeleton). Companion article "Dynamic Hedge Ratio Between ETF Pairs Using the Kalman Filter" (https://www.quantstart.com/articles/Dynamic-Hedge-Ratio-Between-ETF-Pairs-Using-the-Kalman-Filter/) — **direct fetch failed (502 Bad Gateway)**; its key content (TLT/IEI slope drifting 1.38 → 0.9 over 2011–2016; "fixed hedge ratio far too rigid"; δ responsiveness-vs-noise trade-off) was read via search-extracted text and is cited with that caveat.
4. **IvanKostyuk94, "pairs-trading-kalman" (GitHub repository, 2025).** URL: https://github.com/IvanKostyuk94/pairs-trading-kalman — accessed 2026-10-07 (repository README read). Taken: counter-evidence — on IAU/GDX, GLD/SLV, XLF/KBE, SPY/IVV (2017–2025), dynamic hedge ratios help only pair-specifically; Kalman higher PnL but lower Sharpe on SLV/GLD (2025 silver squeeze); rolling OLS best on GDX/IAU; static OLS best on KBE/XLF; "Kalman helps where β unstable" hypothesis not supported; GARCH signal overlay underperforms a rolling z-score. This is why §4b mandates a per-industry bake-off.
5. **Quantt, "Testing for Mean Reversion: ADF, Hurst Exponent and Half-Life".** URL: https://www.quantt.co.uk/resources/mean-reversion-testing — accessed 2026-10-07 (full search extract read). Taken: the three-test screen (ADF, Hurst, half-life); OU/AR(1) half-life identities (t½ = ln2/θ; discrete t½ = −ln2/ln(1+β); ρ = e^{−θΔt}); regime-break warnings (Zivot–Andrews, Bai–Perron) motivating our gate refresh and breach exit.
6. **QuanterLab, "The Ornstein-Uhlenbeck Process: Mean-Reversion Math, Half-Life, and Trading Use".** URL: https://quanterlab.com/articles/stochastic-ou-process — accessed 2026-10-07 (full search extract read). Taken: half-life interpretation bands (< 5 bars noise; 5–30 tradable sweet spot; 30–100 capital-intensive; > 100 suspect; negative = walk away) — the basis for our [2, 20]-day gate; "always verify stationarity (ADF, KPSS, Hurst) before trusting OU output"; regression residuals between correlated stocks as the natural OU application.
7. **Hudson & Thames, "Caveats in Calibrating the OU Process".** URL: https://hudsonthames.org/caveats-in-calibrating-the-ou-process/ — accessed 2026-10-07 (full search extract read). Taken: θ estimators biased upward in finite samples ("the model is often too optimistic, because faster mean-reversion indicates more profit"); reliability floors (≥ ~1 year of daily data; ≥ ~20 mean crossings) — implemented as our 252-day window and 15-crossing rule; MLE ≡ AR(1) with known mean.

## 9. Further reading

- Vidyamurthy, G., *Pairs Trading: Quantitative Methods and Analysis* (Wiley, 2004) — cointegration framework, error-correction models, time-varying hedge-ratio estimation. **Not accessed** (no open text found); known via secondary citation. Priority acquisition for the desk.
- Bossaerts, P. (1988), "Common Nonstationary Components of Asset Prices", *Journal of Economic Dynamics and Control* — the co-integration foundation GGR cite (not accessed).
- Engle, R. & Granger, C.W.J. (1987), "Co-integration and Error Correction", *Econometrica* (not accessed).
- Huck, N. & Afawubo, K. (2015), "Pairs trading and selection methods: is cointegration superior?", *Applied Economics* — distance vs cointegration horse race (known via secondary citation; not accessed).
- Chan, E., *Algorithmic Trading* (2013) — the Kalman pairs example QuantStart implements (book not accessed; the QuantStart implementation was read).
- Do, B., Faff, R. & Hamza, K. (2006), "A New Approach to Modeling and Estimation for Pairs Trading" — pairs selection beyond distance/cointegration (known via secondary citation; not accessed).
- Avellaneda, M. & Lee, J.H. (2010), "Statistical arbitrage in the US equities market", *Quantitative Finance* — PCA/ETF residual stat-arb, the basket-relative of our design (known via secondary citation; not accessed).
- Jegadeesh, N. & Titman, S. (1995), "Overreaction, Delayed Reaction, and Contrarian Profits", *RFS* — the behavioral mechanism GGR cite (not accessed).
