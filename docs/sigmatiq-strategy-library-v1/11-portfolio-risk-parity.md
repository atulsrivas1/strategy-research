# 11. Risk Parity / All-Weather Allocation — Twist: RP-REGIME

> **Library:** Sigmatiq Strategy Library | **Bucket:** Portfolio/Macro (months–years) | **Style:** Asset allocation / risk budgeting (equal risk contribution)
> **Instruments:** Equity index futures or ETFs, nominal Treasury futures/bonds, inflation-linked bonds (TIPS), commodity futures or broad commodity ETFs, gold; T-bills/cash as the de-risking asset | **Typical holding period:** Permanent strategic sleeve; monthly rebalancing | **Complexity (1–5):** 3 | **Evidence grade (A–C):** B+ (strong theoretical foundation and 25+ years of practitioner use; live track records mostly proprietary; 2020 exposed leverage/correlation fragility)
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise. This library contains no local backtests yet.

---

## 1. Origin & lineage

**Creator / popularizer.** Bridgewater Associates. The All Weather strategy was fully formed in **1996** by Ray Dalio, Bob Prince, Greg Jensen and colleagues, originally to manage Dalio's family trust assets — "the best portfolio Ray and his close associates could build without any requirement to predict future conditions" (Bridgewater, *The All Weather Story*, January 2012, read in full — §8). The intellectual trail documented there:

- **1971:** Dalio's "Nixon rally" surprise (stocks up ~4% the day after the gold window closed) → the doctrine of *expecting surprises* and studying the "economic machine" as cause-effect linkages.
- **1983:** the McDonald's McNugget hedge (synthetic corn + soymeal future) → any return stream decomposes into components; portfolios can be built from parts.
- **Late 1980s–1990:** the "Rusty Olson memo" — pairing equities with long-duration bonds of *equal risk* to hedge deflationary-contraction exposure: "Bonds will perform best during times of disinflationary recession, stocks will perform best during periods of … growth, and cash will be the most attractive when money is tight" (1990 memo, quoted in the 2012 paper). Two key ideas: **environmental bias** of asset classes and **risk-balancing** ("low-risk/low-return assets can be converted into high-risk/high-return assets" — leverage as an implementation tool).
- **Early 1990s:** Bob Prince's Excel experiments showed the best-performing portfolio was balanced to *inflation* surprises; Dalio extended it to *growth* → the four-box framework.
- **1997:** Bridgewater advised the US Treasury on the design of TIPS; inflation-linked bonds became a core All Weather ingredient (they fill the rising-inflation quadrant that stocks and nominal bonds both fail).
- **Post-2000:** after the tech crash and 2008, institutional adoption surged; "a clever consultant adopted the term 'Risk Parity' and created an asset allocation bucket" (the 2012 paper's phrasing; the term is widely credited to Edward Qian of PanAgora, 2005 — see §9).

**Academic treatment.**
- Qian (2005, 2006, PanAgora) — coined "risk parity"; showed risk contributions are good predictors of *ex post* loss contributions (cited in Maillard et al.).
- **Maillard, Roncalli & Teiletche (2010, *Journal of Portfolio Management* 36(4): 60–70)** — "The Properties of Equally Weighted Risk Contribution Portfolios": the canonical ERC formalization (read, §8).
- Roncalli (2013), *Introduction to Risk Parity and Budgeting* (Chapman & Hall) — the reference monograph (not fetched this session; the 2010 paper covers the core math — §9).
- Asness, Frazzini & Pedersen (2012, *FAJ* 68(1)) — "Leverage Aversion and Risk Parity": risk parity works because leverage aversion makes safer assets offer higher risk-adjusted returns; they report RP outperforming the market over a century (secondary citation via the Coastlight Capital reprint excerpt — §8).

**How it is actually used.** Institutional portfolios (the 2012 paper: one of the largest Canadian pension plans adopted All Weather as its *benchmark*; a 2012 survey cited there found 25% of institutional investors using it). Commercial risk-parity mutual funds and hedge-fund sleeves typically run 8–12% volatility targets with leverage applied to low-vol assets. The ECB (May 2020) estimated **~$300bn in ~100 risk-parity funds** and up to $2tn across all volatility-targeting strategies; Stefanova (2020) cites risk-parity AUM near **$1tn** at the 2019 peak, shrinking to ~$400bn within a month in March 2020.

## 2. The original rules (as published)

### 2.1 Bridgewater's All Weather (2012 paper)

The published framework is qualitative, not a parameter sheet:

1. **Decompose returns:** `return = cash + beta + alpha`. Betas are few, cheap, and beat cash over time; alpha is zero-sum. Fix the beta allocation first.
2. **Four environments:** all market surprises decompose into growth rising/falling × inflation rising/falling *relative to what is discounted*. "Investors are always discounting future conditions and they have equal odds of being right about any one scenario."
3. **Equal risk per box:** "The key was to put equal risk on each scenario to achieve balance." The published allocation maps asset classes onto the boxes with **25% of risk each**:
   - Growth rising: equities, commodities, corporate credit, EM credit.
   - Growth falling: nominal bonds, inflation-linked (IL) bonds.
   - Inflation rising: IL bonds, commodities, EM credit.
   - Inflation falling: equities, nominal bonds.
4. **Leverage to equalize risk:** "when viewed in terms of return per unit of risk, all assets are more or less the same"; low-risk assets are levered to stock-like risk so diversification doesn't cost return (the paper's footnote example: $10/$10 stocks/bonds is dominated by stock risk; $5 stocks / $15 bonds is balanced but lower return; the same $5/$15 *with a bit of leverage* has stock-like return with less risk).
5. **Passivity:** no forecasting; rebalance mechanically ("it was someone's part-time job to rebalance the portfolio from time to time" in the 1996 pilot).

What Bridgewater deliberately did **not** publish: exact vol/correlation estimation windows, leverage caps, or rebalance bands. Any "original All Weather backtest" circulating online is a third-party reverse-engineering, not the fund.

**History as told in the paper.** The framework grew out of Dalio's 1990 memo "The Big Picture" (asset classes' environmental biases), a 1996 pilot funded with Dalio's family trust money ("it was someone's part-time job to rebalance the portfolio from time to time"), and the 2003 naming of "All Weather." The paper claims the design was stress-tested back to 1925 and that live performance since 1996 behaved as designed through surprises *different in kind* from those in the backtest (their words: the strategy was not fitted to any particular period). These are Bridgewater's own claims about a proprietary track record — treat as marketing-grade evidence, not audited results.

### 2.2 ERC mathematics (Maillard, Roncalli & Teiletche 2010)

For portfolio weights `x = (x_1,…,x_n)`, covariance `Σ`, portfolio vol `σ(x) = √(x′Σx)`:

- Marginal risk contribution: `∂_i σ(x) = (Σx)_i / σ(x)`.
- Total risk contribution: `RC_i = x_i · (Σx)_i / σ(x)`, with `Σ_i RC_i = σ(x)` (Euler decomposition).
- **ERC portfolio:** find `x` with `0 ≤ x_i ≤ 1`, `Σx_i = 1`, such that `RC_i = RC_j` for all `i,j` — equivalently `x_i(Σx)_i = x_j(Σx)_j`.
- **Two-asset closed form:** `x* = (σ_1^{-1}, σ_2^{-1}) / (σ_1^{-1} + σ_2^{-1})` — independent of correlation.
- **Equal-correlation case** (`ρ_ij = ρ`): `x_i ∝ 1/σ_i` (inverse-volatility weighting is ERC under constant correlation).
- **General case:** weights are inversely proportional to each asset's beta with the portfolio: `x_i ∝ 1/β_i` (endogenous — β depends on x — so solve numerically).
- **Numerical solution:** minimize `f(x) = Σ_i Σ_j [x_i(Σx)_i − x_j(Σx)_j]²` by SQP; ERC exists iff `f(x*) = 0`. Equivalent formulation: minimize `√(y′Σy)` s.t. `Σ ln y_i ≥ c` (a variance-minimization with a diversification constraint).
- **Ordering theorem:** `σ_MV ≤ σ_ERC ≤ σ_1/n` — ERC sits between minimum-variance and equal-weight in absolute risk.
- **Optimality:** ERC coincides with the maximum-Sharpe portfolio iff all assets have the same Sharpe ratio *and* constant pairwise correlation.
- Worked example from the paper (vols 10/20/30/40%, constant correlation): ERC weights **48/24/16/12%** vs 25% each for 1/n; with a mixed correlation matrix, ERC vol 10.3% vs MV 8.6% (concentrated 74.5% in asset 1) and 1/n 11.5% (47.2% of risk from asset 4).

**Worked 5-sleeve example with realistic vols (illustrative, not a backtest).** Take annualized vols: equities 16%, nominal bonds 7%, IL bonds 6%, commodities 18%, gold 15%, and assume (heroically) equal pairwise correlation ρ. Then ERC = inverse-vol weights ∝ (1/16, 1/7, 1/6, 1/18, 1/15) = (0.0625, 0.1429, 0.1667, 0.0556, 0.0667), normalized: **equities 12.6%, nominal bonds 28.9%, IL bonds 33.7%, commodities 11.2%, gold 13.5%** — the bond-heavy shape that makes risk parity look like "levered bonds plus decoration" to critics. Unlevered portfolio vol ≈ 4–5%; scaling to an 8% target requires ~1.7–2.0× gross leverage — exactly the ECB-documented pre-2020 level. This example makes the two structural facts concrete: (i) the bond legs carry most of the *weight* while each sleeve carries equal *risk*; (ii) the vol target, not the ERC solve, is what sets leverage — so the leverage cap and the vol floor on estimates are the real risk controls. With unequal correlations (bonds negatively correlated to equities in growth scares), the solve shifts further into bonds; with 2022-style positive stock-bond correlation, it shifts out — the estimator chases the correlation regime, which is why §4(b) tilts and §4(a) ratchet exist.

### 2.3 Disagreements across sources
- **What "risk" is:** Bridgewater balances *economic-scenario* risk (four boxes); MRT balance *statistical* risk contributions from a covariance matrix. The two coincide only if the covariance structure faithfully encodes scenario exposures — exactly what breaks in crises (§6).
- **Leverage:** Bridgewater frames leverage as neutral implementation ("a moderately-levered, highly-diversified portfolio is less risky than an unleveraged, un-diversified portfolio"). Critics (Stefanova 2020) treat the leverage itself as the fragility.
- **Expected returns:** ERC ignores expected returns entirely (a feature per MRT — robustness to estimation error, Merton [1980] cited therein); Asness et al. (2012) supply the missing return justification via leverage aversion.
- **Passive doctrine vs regime reality:** Bridgewater's published doctrine is strict passivity ("equal odds of being right about any one scenario"), yet the same firm's flagship Pure Alpha is an active macro fund — Bridgewater itself separates beta (All Weather) from alpha (Pure Alpha). Critics argue the four-box "balance" is itself an implicit bet on the post-1982 correlation regime; defenders reply that the boxes are defined by *surprises relative to what's discounted*, not by realized macro, so no regime forecast is embedded. Our tilt (b) is a deliberate, bounded departure from the passive doctrine — documented as such, not smuggled in.
- **What to hold in the inflation-rising box:** the 2012 paper maps IL bonds, commodities *and* EM credit there; our 5-sleeve simplification drops EM credit and corporate credit entirely (spread products embed equity-like growth risk that double-counts the growth boxes). This is a documented simplification, not a claim that the original mapping is wrong.

## 3. Why it works — mechanism & evidence

**Mechanism.**
1. **Diversification across economic regimes.** Asset classes have structural environmental biases (1990 memo). Equal-risk weighting across regimes means no single macro surprise dominates P&L; "the environmental exposures cancel each other out, which leaves just the risk premium to collect" (2012 paper).
2. **Leverage aversion anomaly.** Asness, Frazzini & Pedersen (2012): because many investors cannot or will not lever, safer assets offer higher risk-adjusted returns; a levered low-risk portfolio harvests this. This is the *return* engine; ERC is the *risk* engine.
3. **Estimation robustness.** MRT: mean-variance weights are hyper-sensitive to expected-return inputs; ERC uses only the covariance matrix (more estimable) and never concentrates like minimum-variance.
4. **The engineering framing.** Bridgewater's own description is deliberately non-oracular: "investors are always discounting future conditions and they have equal odds of being right about any one scenario" — so the only defensible *unconditional* allocation is equal risk per scenario. This is an agnosticism argument, not a forecasting claim: the strategy's edge is collecting multiple risk premia simultaneously with minimal covariance between the collection processes. It follows that the strategy has no view and no timing — which is precisely what makes it fragile to *correlation-level* regime change (when the premia's bad states coincide, as in inflation shocks) and what motivates our regime overlay. Note the honest tension: Bridgewater says the quadrants are equally likely ex ante; our tilt (b) says they are *slightly* predictable at monthly frequency. We keep the tilt small (±20%) because the evidence for macro nowcast predictability is modest, and §7 requires it to prove itself or be dropped.

**Evidence (attributed).**
- MRT's empirical illustrations confirm the volatility ordering and show ERC delivering middle-ground risk with balanced contributions (their §4 backtests, rolling monthly rebalancing). The ordering theorem `σ_MV ≤ σ_ERC ≤ σ_1/n` has a practical reading: ERC is *insurance against concentration in either direction* — it can never be as concentrated as minimum-variance (which loads on the lowest-vol asset) nor as risk-unbalanced as equal-weight (which lets the highest-vol asset dominate).
- Asness et al. (2012) report RP beating the market portfolio over ~a century "by a statistically and economically significant amount" (their claim; not independently re-verified here).
- Bridgewater's live All Weather track is proprietary; the 2012 paper claims the strategy "weathered" post-1996 surprises of different kinds than those it was designed on.
- The four-box logic has a testable implication the desk should exploit: in any given episode, the sleeves mapped to the prevailing quadrant should carry the P&L. If post-hoc episode analysis repeatedly shows the "wrong" sleeves paying (e.g., nominal bonds rallying through an inflation surprise), the mapping — not just the parameters — needs revision. This is a built-in falsifiability check, run as part of the 1970s side-analysis and every crisis replay.

**Contradictory / critical evidence.**
- **March 2020.** Stefanova (Hedge Fund Journal, June/July 2020): the **S&P Risk Parity Index fell 28% peak-to-trough vs 18% for BlackRock's 60/40 fund**; VIX spiked to 85 (March 18); "correlations among assets converged to 1, with the price of equities, treasuries and even gold, falling simultaneously." Her structural critique: (i) risk parity assumes stable correlations/vol — both break in crises; (ii) Treasuries at ~0% yields have asymmetric (limited upside / large downside) payout; (iii) ~$1tn AUM made it an overcrowded long; (iv) procyclical leverage — "as volatility kept going down, leverage kept going up... in a deleveraging cycle when vol spikes, risk parity has to sell off assets, which further exacerbates their losses."
- **ECB Financial Stability Review (May 2020), stylized daily-rebalanced RP model** (4 asset classes, 8% vol target): pre-March, low vols and low correlations allowed **leverage up to ~2× AUM**; when vols and cross-asset correlations spiked together, the rule required selling **assets worth ~225% of capital**, ending with a **~25% cash share** — selling extended to *all* asset classes including the supposedly safe ones. The ECB concludes RP "probably contributed to price movements" but the aggregate impact is hard to quantify.
- **Regime dependence:** the strategy's long-run success coincided with the 1982–2019 bond bull market and (per Stefanova) "the largest liquidity expansion the world has ever seen" — a falling-yield tailwind to the levered bond leg that cannot repeat from ~0% (her 2020 view; note that 2022's inflation shock subsequently delivered exactly the stocks+bonds-down-together scenario she flagged — our general knowledge, not a fetched source).

## 4. The twist: RP-REGIME

Two modifications to the plain ERC core, each tied to a documented 2020-style failure. Equally important is what the twist deliberately does **not** do: no expected-return optimization (Merton-estimation fragility), no daily vol-target deleveraging (the ECB's 225%-of-capital pathology), no leverage above 2× (the pre-2020 industry level, adopted as a ceiling), no additional asset classes beyond five liquid sleeves (TIPS and commodity liquidity are the binding constraints), and no machine-learning regime model (a two-signal nowcast is auditable; a black box is not). Every added rule below is cheap to compute, fully specified, and individually ablatable in validation.

**(a) CPPI-style drawdown control (de-risking ratchet).**
*Weakness addressed:* plain ERC with a vol target de-leverages *after* vol has spiked — procyclically, into falling markets (the ECB's 225%-of-capital fire sale). A drawdown-based overlay acts on *realized losses* rather than estimated vol, is state-dependent on our own equity curve (not on market-wide estimates that gap), and pre-commits the de-risking path so it cannot be negotiated away mid-crisis.
*Rule:* track sleeve drawdown `DD_t` from the trailing peak. If `DD_t > 10%`: shift **25% of total risk budget** to T-bills/cash (implemented as a proportional scale-down of all risky sleeves, preserving internal ERC proportions). If `DD_t > 15%`: shift a further 25% (50% total). **Restore in steps:** when `DD_t < 7.5%`, restore half the first tranche; when `DD_t < 5%`, restore fully; never restore more than one step per month (anti-whipsaw). Rationale for levels: 10% is ~1.25× the sleeve's 8% vol target (a >1-sigma annual event); the asymmetric restore path mirrors CPPI cushion logic.

**(b) Growth/inflation nowcast tilts (±20% risk-budget tilt).**
*Weakness addressed:* Bridgewater's own premise is that the four quadrants are equally likely *ex ante* — but the strategy's worst episodes are sustained regimes (2020 liquidity spiral; 2022-style inflation) where one quadrant dominates for quarters. A modest, bounded tilt toward the currently prevailing quadrant converts the static framework into a slow regime-follower without abandoning balance (the tilt is ±20% of base budget, never a quadrant bet).
*Rule:* monthly nowcast vector from three public, unrevised-at-use signals:
- Growth direction: `G = sign(PMI_t − PMI_{t−3})` (ISM manufacturing PMI 3-month change; +1 rising, −1 falling).
- Inflation direction: `I = sign(CPI^{3m ann.}_t − CPI^{3m ann.}_{t−3})` (CPI momentum change).
- Curve confirmation: `C = sign(10y − 2y slope change over 3m)` used only to break ties (if G or I is 0/ambiguous).
Quadrant → risk-budget multipliers (applied multiplicatively to the base 20% per asset, then renormalized to sum to the post-drawdown-control budget):
- G=+1, I=−1 (goldilocks): equities ×1.2, nominal bonds ×1.1, IL bonds ×1.0, commodities ×0.9, gold ×0.9.
- G=+1, I=+1 (reflation): commodities ×1.2, IL bonds ×1.1, equities ×1.1, gold ×1.0, nominal bonds ×0.8.
- G=−1, I=−1 (deflationary bust): nominal bonds ×1.2, gold ×1.1, IL bonds ×1.0, equities ×0.8, commodities ×0.8.
- G=−1, I=+1 (stagflation): gold ×1.2, commodities ×1.1, IL bonds ×1.1, nominal bonds ×0.8, equities ×0.8.
All multipliers clipped to [0.8, 1.2] — the tilt can never zero a sleeve or double it.

**(c) Rebalancing discipline:** monthly calendar rebalance, plus **5% drift bands** (rebalance early only if any sleeve's actual risk contribution drifts > 5% of target, measured as `|RC_i/σ_p − b_i| > 0.05·b_i`). Bands cut turnover and reduce the procyclical churn the ECB documented in daily-rebalanced implementations.

**Worked tilt example (illustrative arithmetic, not a backtest).** Suppose the nowcast reads G=−1, I=+1 (stagflation: PMI falling for 3 months, CPI momentum rising). Base budgets per sleeve = 20% each. Multipliers: gold ×1.2, commodities ×1.1, IL bonds ×1.1, nominal bonds ×0.8, equities ×0.8 → tilted budgets (24, 22, 22, 16, 16) summing to 100 — no renormalization needed by construction of the multiplier table (each table row sums to 5.0). If the drawdown ratchet is simultaneously in its first state (DD > 10%), the risky budget is 75%: scale all five budgets by 0.75 → (18, 16.5, 16.5, 12, 12) with 25% of risk budget in T-bills. The ERC solver then finds weights whose *risk contributions* match these budgets — the tilt moves risk, not nominal weight directly. Composition note: the two overlays are deliberately orthogonal — (a) scales the total risk budget down on our own equity curve, (b) reallocates the remaining budget across sleeves on macro state; (a) never changes relative sleeve budgets, (b) never changes total risk.

## 5. Full specification of the twist variant

**Universe (5 sleeves, liquid instruments).**
1. Equities: S&P 500 (ES futures or SPY/IVV).
2. Nominal bonds: US 10–30y Treasuries (TY/US futures or IEF/TLT).
3. Inflation-linked bonds: US TIPS (SCHP/TIP; pre-1997 history must be synthesized — §7).
4. Commodities: diversified basket (BCOM/GSCI excess-return futures or broad ETF).
5. Gold: GC futures or GLD/IAU.
Cash/de-risking leg: 1–3m T-bills or government MMF.

**Data requirements.** Daily total/excess returns per sleeve; EWMA covariance; ISM PMI (first business day monthly), CPI (mid-month), 10y–2y Treasury slope (daily). All macro signals used with **publication-lag-aware timestamps** (PMI available same-day; CPI ~2-week lag — use the release date, not the reference month).

**Estimation.**
- Vols: EWMA of daily returns, λ = 0.94, minimum 60-day history, floor each sleeve vol at its 5-year 25th percentile (prevents leverage blow-up in dead-calm regimes — the 2019 trap).
- Correlations: EWMA λ = 0.97 shrunk 50% toward the sample average correlation matrix (stabilizes the matrix without imposing a factor model).
- ERC solve: minimize `f(x) = Σ_iΣ_j [x_i(Σx)_i b_j − x_j(Σx)_j b_i]²` where `b` = tilted risk budgets (base 0.20 each × quadrant multipliers, renormalized), by SQP; long-only `x_i ≥ 0`.

**Leverage & vol target.** Scale the ERC portfolio so ex-ante vol = **8% annualized**; leverage cap **2.0× gross** (the ECB-documented pre-2020 level — we adopt it as a *ceiling*, not a target); financing at T-bill + 25bp (futures) in the cost model.

**Entries/exits.** Not applicable in the trade sense — this is a standing allocation. Position changes occur at: monthly rebalance, drift-band breach, drawdown-control triggers (§4a), nowcast tilt updates (§4b, applied only at monthly rebalance to avoid mid-month signal noise).

**Risk limits.** Max 2× gross; per-sleeve weight cap 60% of NAV; drawdown ratchet as in §4a; if the sleeve's *realized* 60-day vol exceeds 1.5× target for 10 consecutive days, de-risk to target at the next rebalance regardless of drawdown state (covers the case where losses haven't yet triggered the ratchet but vol has exploded — the March 2020 sequence).

**Costs (assumptions for validation, not literature claims).** Futures: 1–3 bp per side per contract class + roll costs at actuals (quarterly rolls, use volume-weighted roll window); ETFs: expense ratios at actuals + 2–5 bp spread; financing spread 25bp over T-bill on levered notional; TIPS liquidity haircut in stress windows (Stefanova flags TIPS market thinness as a real constraint for RP managers).

**Capacity.** Futures implementation: effectively unconstrained at desk scale ($100mm–$1bn); the binding constraints are TIPS and commodity-basket liquidity in stressed rolls — keep TIPS sleeve < 5% of daily TIPS ETF/futures volume at rebalance.

**Parameter summary (single source of truth for implementation).**

| Parameter | Value | Source / rationale |
|---|---|---|
| Sleeves | Equities, nominal bonds, IL bonds, commodities, gold (+ T-bill cash leg) | Bridgewater four-box mapping, simplified to 5 liquid sleeves |
| Base risk budgets | 20% per sleeve | Bridgewater "equal risk on each scenario"; 5-sleeve ERC |
| Vol/corr estimation | EWMA λ=0.94 (vols), λ=0.97 shrunk 50% to trailing-average corr | RiskMetrics convention; shrinkage for stability |
| Vol floor | 5-year 25th percentile per sleeve | Prevents 2019-style leverage blow-up in dead-calm regimes |
| Vol target | 8% annualized ex-ante | ECB model used 8%; mid-range institutional target |
| Leverage cap | 2.0× gross (ceiling, not target) | ECB-documented pre-2020 level, adopted as hard cap |
| Financing | T-bill + 25 bp on levered notional | Cost-model assumption |
| Drawdown ratchet | DD>10% → 25% of risk budget to T-bills; DD>15% → 50% | Twist (a); 10% ≈ 1.25× vol target |
| Ratchet restore | DD<7.5% → restore half of first tranche; DD<5% → full; ≤1 step/month | Anti-whipsaw; CPPI cushion logic |
| Vol-explosion override | Realized 60d vol > 1.5× target for 10 days → de-risk at next rebalance | Covers losses-not-yet-realized case (Mar 2020 sequence) |
| Nowcast signals | G = sign(Δ3m ISM PMI); I = sign(Δ3m CPI 3m-ann. momentum); curve tiebreak | Twist (b); release-date timestamps only |
| Tilt bound | Multipliers ∈ [0.8, 1.2], quadrant tables sum to 5.0 | Bounded tilt; never a quadrant bet |
| Rebalance | Monthly + 5% risk-contribution drift bands | Anti-procyclicality (ECB critique) |
| Per-sleeve weight cap | 60% of NAV | Concentration limit |

**Monthly operations calendar.**

| Day | Action |
|---|---|
| Daily | Update EWMA vols/correlations; compute drawdown vs ratchet levels; check vol-explosion override; log drift-band status. |
| PMI release (1st business day) | Update growth nowcast `G` (release-date timestamp). |
| CPI release (mid-month) | Update inflation nowcast `I` (release-date timestamp, first-release print). |
| Month-end rebalance | Re-solve ERC with tilted budgets and post-ratchet total budget; scale to 8% vol target subject to 2× cap; trade the delta; log turnover and tilt/ratchet state. |
| Drift-band breach (any day) | If any `|RC_i/σ_p − b_i| > 0.05·b_i`, rebalance early (full solve, same rules). |
| Ratchet breach (any day) | On DD crossing 10%/15%: execute the 25% risk-budget shift to T-bills within 1 trading day (proportional scale-down of all sleeves). On recovery through 7.5%/5%: restore one step, max one per month. |
| Quarterly | Review crowding gauges (RP-complex AUM/leverage), TIPS liquidity, financing spread; refresh vol floors. |

## 6. Failure modes & regime dependence

**What kills it.**
1. **Inflation shock with positive stock-bond correlation (2022-type).** The framework's core diversification bet is that bonds offset equity growth risk. When inflation is the shock, stocks and nominal bonds fall *together* and the levered bond leg amplifies losses. Our quadrant tilt (b) is the designed mitigation — it shifts budget toward IL bonds/commodities/gold in the G=−1,I=+1 and G=+1,I=+1 quadrants — but it reacts monthly and will be late by weeks in a fast repricing. The drawdown ratchet (a) is the backstop.
2. **Liquidity spirals / procyclical deleveraging (March 2020).** ECB: the strict rule would have sold 225% of capital into the worst liquidity of the decade. Mitigations: monthly (not daily) rebalancing, drift bands, the 2× leverage *ceiling*, and the vol floor. Residual risk: our own ratchet adds to crowded selling if many RP managers share similar triggers — an unavoidable crowding externality; keep the sleeve small relative to the RP complex.
3. **Bond-bull dependence.** If the 1982–2019 yield decline was a one-way tailwind, forward returns of the levered bond leg are structurally lower (Stefanova's "asymmetric payout" argument). Honest consequence: at low starting yields, either accept lower sleeve return or lower the vol target — do **not** reach for return by raising leverage past the cap.
4. **Nowcast whipsaw.** PMI/CPI momentum flip sign around turning points; ±20% tilts will be wrong at exactly the regime boundaries that matter most. The tilt is deliberately small so that being wrong costs little; validate that the tilt adds value net of turnover (§7) — if not, drop it and keep (a) alone.
5. **TIPS-specific traps.** TIPS carry equity-like drawdowns when real yields spike (2022, general knowledge) and their liquidity thins in crises (Stefanova). The IL sleeve is the most fragile leg operationally.
6. **Ratchet lock-down.** After a deep drawdown, the 50% cash state can persist for months, missing the recovery (CPPI's known "cash-lock" pathology). The stepped restore (half at DD<7.5%, full at DD<5%, max one step/month) is the compromise; a time-based override (begin restoring after 6 months if DD is no longer deepening) is a documented alternative to test in validation.
7. **Taper-tantrum type rate shocks (2013).** When the shock is *rates* rather than growth or inflation, nominal bonds and IL bonds sell off together, gold falls (real-rate sensitive), and only commodities partially offset. The four-box framework has no "rates rising because term premium" box — a blind spot of the growth×inflation taxonomy worth acknowledging honestly: the strategy is balanced against *macro surprise* as Bridgewater defines it, not against every possible shock. The vol target and ratchet are the generic defenses.
8. **Slow erosion via negative carry.** In a flat, low-vol, range-bound regime (2015–16 style), the levered bond leg earns little, financing costs ~25bp over T-bills, and the tilt whipsaws. Not fatal — a multi-year flat Sharpe — but the acceptance criteria (§7) must tolerate long flat stretches rather than tuning them away.

**Regime dependence summary.** The strategy's center of gravity is the claim that growth and inflation surprises are the two master shocks and that five liquid sleeves span them. It thrives in regimes where the stock-bond correlation is negative (growth-scare regimes: 2000–02, 2008, and most of 1982–2019) and struggles when inflation is the master shock (1970s, 2022) or when liquidity itself is the shock (March 2020). The two overlays are aimed precisely at those two failure regimes: the tilt follows the prevailing quadrant slowly, and the ratchet caps the damage when correlations converge to one faster than any monthly process can adapt. Neither overlay makes the strategy antifragile — the honest design goal is *less fragile than plain ERC at the same vol target*, which is what §7's acceptance criteria test.

**Early-warning indicators.**

| Indicator | Frequency | Threshold of concern |
|---|---|---|
| Stock-bond 60-day correlation | Weekly | Positive *and* rising for 2+ months = the core diversification bet is degrading (2022 pattern) |
| Cross-asset vol correlation | Weekly | Vols spiking *together* across sleeves (the ECB's Chart A pattern) precedes forced deleveraging |
| 10y yield vs 5-year range | Monthly | Near the bottom = asymmetric bond payout (Stefanova's argument); near the top after a fast rise = rate-shock regime |
| Realized 60d sleeve vol vs target | Daily | > 1.5× for 10 days triggers the vol-explosion override |
| Drawdown vs ratchet levels | Daily | Approaching 10% / 15% — pre-position the de-risking orders, don't discover them at the breach |
| RP-complex AUM and estimated leverage | Quarterly | Crowding gauge: Stefanova's $1tn→$400bn March 2020 collapse is the reference event |
| TIPS ETF flows and real yields | Monthly | IL-leg fragility gauge (2022 real-yield spike) |
| Nowcast flip frequency | Monthly | > 4 quadrant changes/yr = tilt is whipsawing; check tilt P&L attribution |

## 7. Validation protocol

**Data needs.** Daily sleeve returns as far back as possible: equities 1926+ (Ibbotson/CRSP), 10y Treasuries 1926+ (Ibbotson long-gov series), commodities 1960+ (GSCI/BCOM), gold 1968+ (London fix), TIPS 1997+ — **before 1997 synthesize an IL proxy** (e.g., nominal bonds minus realized inflation accrual) and flag all pre-1997 results as proxy-regime, or start the formal test in 1997 and use earlier decades only for qualitative regime checks (1970s inflation is the key stress episode and deserves a dedicated side-analysis even with proxy data). PMI 1948+, CPI 1913+, curve 1976+ (2y note).

**Chronological splits.** Development: 1973–1996 (oil shocks, 1980–82 Volcker disinflation, 1987). Validation: 1997–2013 (TIPS live; dot-com, GFC). Test: 2014–2026 (taper, 2018, COVID 2020, 2022 inflation, 2025–26). All estimation (EWMA, shrinkage, quadrant multipliers, ratchet levels) frozen before the test window.

**Cost / roll / margin model.** Futures rolls at actual term-structure cost (not zero); financing at T-bill + 25bp on levered notional; ETF expense ratios at actuals; TIPS liquidity haircut 2× in 2008/2020 windows. Margin: futures margin at exchange historicals; verify the 2× cap is compatible with margin + a 30% buffer through 2020-style vol.

**Strategy-specific pitfalls.**
- *Look-ahead in macro signals:* use release dates, never reference months; PMI/CPI get revised — use vintage data where available (ALFRED) or first-release prints.
- *Correlation-regime look-ahead:* EWMA is causal by construction, but any "average correlation" shrinkage target must be trailing/expanding, never full-sample.
- *Bond bull survivorship:* a 1982–2019-only backtest is marketing, not evidence; require the 1970s side-analysis.
- *Leverage realism:* check margin, financing, and forced-deleveraging behavior in Mar 2020 specifically; the ECB's 225%-of-capital turnover figure is the benchmark our smoother rules must beat by an order of magnitude.
- *Ratchet gaming:* do not tune the 10%/15% levels on the test window; perturb {8/10/12%} × {12/15/18%} and report the grid.

**The 1970s side-analysis (mandatory).** The 1973–1982 decade is the strategy's most important stress test and the hardest to run honestly: no TIPS existed, gold was re-legalized for US ownership only in 1975, and commodity futures data are thin. Protocol: run the sleeve with the four available legs (equities, nominal bonds, commodities from GSCI backfill, gold from London fix) plus a *synthetic* IL proxy (nominal bonds minus trailing realized inflation accrual, clearly flagged); report 1973–74 (oil shock, stocks −40%+ real), 1977–80 (inflation spiral, gold/commodities moon, bonds collapse), and 1980–82 (Volcker disinflation, everything reverses) as separate episodes with the tilt and ratchet states logged month by month. The question is not "does it make money" but "does the risk-budget machinery keep any single episode from dominating the decade." If the proxy regime is too fragile to support even that qualitative judgment, say so in the write-up rather than manufacturing precision — a flagged proxy analysis is evidence; an unflagged one is marketing.

**Robustness checks.** Vol target {6, 8, 10%}; leverage cap {1.5, 2, 2.5×}; tilt bound {±10, ±20, ±30%}; EWMA λ {0.92, 0.94, 0.97}; rebalance {monthly, monthly+bands, weekly}; nowcast variants (PMI-only, CPI-only, with/without curve tiebreak). Report tilt-on vs tilt-off and ratchet-on vs ratchet-off as 2×2 ablation — each overlay must justify itself.

**Acceptance criteria (pre-registered).** (i) Test-window Sharpe ≥ 60/40 benchmark with max DD ≤ 60/40's; (ii) March 2020 and 2022 replay: sleeve DD at least one-third smaller than plain ERC at the same vol target; (iii) turnover ≤ 150%/yr all-in (vs the ECB's implied daily-rebalance pathology); (iv) ratchet restores to full risk within 9 months of a trough in ≥80% of historical episodes; (v) tilt adds ≥0 net-of-cost Sharpe in validation or is dropped (honesty over complexity).

**Benchmarks & reporting standards.** Report against: (1) 60/40 S&P 500 / US Agg total return (the allocator's alternative); (2) plain ERC at the same 8% vol target with no overlays (the ancestor — both overlays must beat it on drawdown-adjusted basis or be dropped); (3) the S&P Risk Parity Index family (8/10/12% vol targets) where licensing permits, as the industry reference whose 2020 drawdown Stefanova documented; (4) T-bills + 4% (an absolute-return hurdle). Report monthly returns, rolling 3-year Sharpe, max DD with dates and recovery time, realized leverage through time (the chart the ECB's critique implies every RP manager should publish), risk-contribution stability (realized RC_i vs target b_i), and overlay attribution: P&L decomposed into plain-ERC core, ratchet effect, tilt effect. All figures net of the §5 cost model with the 2× stress-cost scenario alongside.

## 8. Sources read (annotated)

1. **"The All Weather Story"**, Bridgewater Associates, January 2012. URL: https://www.bridgewater.com/resources/all-weather-story.pdf — accessed 2026-10-07. *What it says:* authorized history — Nixon rally, McNugget hedge, Rusty Olson memo ("Bonds will perform best during times of disinflationary recession..."), Prince's inflation-balance Excel experiments, the four-box diagram with 25% of risk per box and the asset-class mapping, TIPS design role (1997), 1996 launch for Dalio's trust, Britt Harris's $200mm first institutional allocation, "return = cash + beta + alpha," leverage-as-tool footnote ($5 stocks/$15 bonds example), "a clever consultant adopted the term 'Risk Parity'." *Taken:* everything in §1 and §2.1; the mechanism framing in §3.
2. **"On the Properties of Equally-Weighted Risk Contributions Portfolios"**, Maillard, Roncalli & Teiletche, *JPM* 36(4), 2010 (working-paper PDF). URL: http://www.thierry-roncalli.com/download/erc.pdf — accessed 2026-10-07. *What it says:* ERC definitions (`RC_i = x_i(Σx)_i/σ`), two-asset closed form, inverse-vol equivalence under constant correlation, `x_i ∝ 1/β_i`, SQP algorithms, `σ_MV ≤ σ_ERC ≤ σ_1/n`, MSR equivalence conditions, worked 4-asset example (48/24/16/12). *Taken:* all of §2.2 and the solver spec in §5.
3. **"Volatility-targeting strategies and the market sell-off"** (FSR box), Vassallo, Hermans & Kostka, ECB Financial Stability Review, May 2020. URL: https://www.ecb.europa.eu/press/financial-stability-publications/fsr/focus/2020/html/ecb.fsrbox202005_02~f6616db9be.nl.html — accessed 2026-10-07. *What it says:* ~$300bn in ~100 RP funds, ~$2tn in vol strategies; stylized 4-asset, 8%-vol-target, daily-rebalanced RP model: leverage reached ~2× AUM in calm markets; March 2020 forced sales of ~225% of capital; ~25% ending cash share; selling hit even safe assets; RP "probably contributed" to price moves, magnitude uncertain. *Taken:* the procyclicality evidence in §3 and §6, the 2× ceiling and turnover benchmark in §5/§7.
4. **"The End of The Golden Era for Risk Parity"**, Katina Stefanova (CEO/CIO Marto Capital), *The Hedge Fund Journal*, June/July 2020 issue. URL: https://thehedgefundjournal.com/the-end-of-the-golden-era-for-risk-parity/ — accessed 2026-10-07. *What it says:* S&P Risk Parity Index −28% peak-to-trough vs BlackRock 60/40 −18% (Jan–Mar 2020); VIX 85 on Mar 18; RP AUM ~$1tn → ~$400bn in under a month; structural critiques — unstable correlations, expensive/asymmetric bonds, central banks out of ammunition, crowding, TIPS liquidity, procyclical leverage. *Taken:* the 2020 failure-mode narrative and critique inventory in §3/§6. Caveat: a practitioner polemic with a viewpoint to sell; numbers cross-checked against the ECB box where possible.
5. **"Risk Parity" page (Dalio 2004 article reprint + Asness-Frazzini-Pedersen excerpt)**, Coastlight Capital. URL: http://www.coastlightcapital.com/risk-parity — accessed 2026-10-07 via search-result excerpt (full page not separately re-fetched). *What it says:* reprints Dalio's 2004 "Engineering Targeted Returns and Risks" principles (target 10% return at 10–12% risk) and summarizes Asness, Frazzini & Pedersen (2012) "Leverage Aversion and Risk Parity" (RP beat the market over a century). *Taken:* the leverage-aversion mechanism citation in §1/§3. Marked as excerpt-level access.

**Failed / partial fetches.** Forbes version of the Stefanova article (forbes.com/sites/katinastefanova/2020/03/23/) returned empty content on fetch — the identical text was read at The Hedge Fund Journal (source 4). Bloomberg's March 12, 2020 risk-parity article is subscriber-paywalled (headline/snippet only — not cited as read).

## 9. Further reading

- Roncalli, T. (2013). *Introduction to Risk Parity and Budgeting*, Chapman & Hall/CRC. **Not accessed this session** (book); the 2010 MRT paper covers the core math. Acquire for the desk.
- Qian, E. (2005/2006). "Risk Parity Portfolios" / "On the Financial Interpretation of Risk Contribution," PanAgora. Origin of the term; not fetched.
- Asness, C., Frazzini, A. & Pedersen, L. (2012). "Leverage Aversion and Risk Parity," *FAJ* 68(1): 47–59. Primary version of the leverage-aversion evidence; not fetched directly (excerpt via source 5).
- Dalio, R. (2004/2010). "Engineering Targeted Returns and Risks," Bridgewater Daily Observations reprint. The 10%/10–12% target framing; not fetched directly.
- Bloomberg (Justina Lee), "Risk Parity Trade Made Famous by Ray Dalio Is Now Ringing Alarms," Mar 12, 2020 — paywalled, not read.
- FSB (Nov 2020). "Holistic Review of the March Market Turmoil" — official-sector account of the March 2020 liquidity spiral including levered NBFI Treasury sales; fetched in search but not read in depth; listed for the desk.
- Choueifaty & Coignard (2008). "Toward Maximum Diversification," *JPM* — the MDP alternative to ERC; not fetched.
- Qian, E. (2005/2006). PanAgora risk-parity papers — the coining of the term and the risk-contribution-as-loss-predictor argument; cited in Maillard et al., not fetched directly.
- Merton, R. (1980). "On Estimating the Expected Return on the Market," *JFE* — the estimation-error result that justifies ignoring expected returns in allocation; cited in Maillard et al., not fetched.
- Ilmanen, A. (2011). *Expected Returns*, Wiley — chapters on alternative betas and the institutional case for diversification across risk premia; not fetched this session.
- Dalio, R. (2017). *Principles*, Simon & Schuster — the popular account of the 1996 All Weather origin; consistent with but less technical than the 2012 paper; not fetched.
- Asness, Frazzini & Pedersen (2019). "Quality Minus Junk," *RAS* — the defensive-quality leg that some RP implementations add as a sixth sleeve; considered and deferred (see doc 12 for our quality treatment); not fetched for this document.
- Roncalli, T. & Weisang, G. (2016). "Risk Parity Portfolios with Risk Factors," *Quantitative Finance* — extending ERC from assets to risk factors; relevant if the desk later replaces the 5 sleeves with underlying growth/inflation factor mimicking portfolios; not fetched.
- Doeswijk, Lam & Swinkels (2014/2019). "The Global Multi-Asset Market Portfolio" — the market-cap-weighted benchmark that risk parity is implicitly judged against; useful for the §7 benchmark set; not fetched.
- Black, F. (1972). "Capital Market Equilibrium with Restricted Borrowing," *Journal of Business* — the original leverage-aversion model underlying Asness et al.'s RP justification; not fetched.
