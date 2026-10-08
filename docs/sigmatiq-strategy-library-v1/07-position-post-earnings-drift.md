# 07. Post-Earnings Announcement Drift — Twist: PEAD-IV

> **Library:** Sigmatiq Strategy Library | **Bucket:** Position (weeks–months) | **Style:** Event-driven momentum (behavioral under-reaction)
> **Instruments:** US-listed common stocks (signal) + listed single-name options (expression) | **Typical holding period:** 1–20 trading days | **Complexity (1–5):** 4 | **Evidence grade (A–C):** A− for the anomaly's existence historically; B− for present-day large-cap profitability (contested, see §3)
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise. This library contains no local backtests yet.

## 1. Origin & lineage

PEAD is one of the oldest and most-studied anomalies in empirical finance:

- **Ball & Brown (1968)**, "An Empirical Evaluation of Accounting Income Numbers" — precursor. First to note that cumulative abnormal returns keep drifting up (down) for "good news" ("bad news") firms *after* earnings are announced. Known here via secondary citation in Bernard & Thomas (1989) and Martineau (2021); the original was not fetched this session.
- **Foster, Olsen & Shevlin (1984)** (FOS) — early systematic replication. They estimate that over the 60 trading days after an earnings announcement, a long position in the highest unexpected-earnings decile combined with a short in the lowest decile yields an **annualized abnormal return of about 25%, before transaction costs** (as quoted in the Bernard & Thomas 1989 abstract; independently restated in the 2025 "Resurgence" paper, §2.5 — both fetched this session).
- **Bernard & Thomas (1989)**, "Post-Earnings-Announcement Drift: Delayed Price Response or Risk Premium?", *Journal of Accounting Research* 27, 1–36 — the core paper. Tests whether drift is a delayed response to information or an unpriced risk premium; concludes the evidence is consistent with **delayed price response**, not risk.
- **Bernard & Thomas (1990)**, *Journal of Accounting & Economics* — shows stock prices do not fully reflect the implications of current earnings for *future* earnings (earnings are close to a seasonal random walk with drift, so a surprise predicts next-quarter same-quarter earnings). Not fetched directly; known via secondary citation in Martineau (2021) and the Resurgence paper.
- The **SUE (standardized unexpected earnings)** literature of the 1980s formalized the signal: surprise scaled by the historical dispersion of surprises, ranked into deciles.
- Later literature on **decay and institutional exploitation**: Chordia et al. (2014), Chordia & Miao (2020) (HFT erodes PEAD), Martineau (2021) ("Rest in Peace"), and a 2025 working paper claiming a post-2020 **resurgence** (all fetched this session — see §8).
- Options-market angle (basis for our twist): Gao, Xing & Zhang (2018, JFQA) on earnings straddles; Liu, Mao, Tang & Zhou on ex-ante earnings risk premia; and work on the option-implied earnings move (ATM straddle % of spot) as the market's own forecast of the announcement move.

In practice PEAD is traded by quant equity desks as a decile long/short signal (SUE or analyst-revision based) with 1–60 day horizons, and by event-driven options desks who compare the *implied* move (pre-earnings straddle) to the *realized* move. Our twist sits at the intersection: use the options market's own forecast to decide whether the cash market under-reacted.

## 2. The original rules (as published)

There is no single "trading rule" from the original papers — they are event studies. The canonical academic implementation, reconstructed from the sources read:

**Signal (SUE), per Foster, Olsen & Shevlin (1984) lineage and as operationalized in the 2025 Resurgence paper:**

```
SUE_i,q = (EPS_actual_i,q − EPS_expected_i,q) / σ_i
```

- `EPS_expected` = either the seasonal random-walk forecast (EPS of the same quarter last year, the FOS/Bernard-Thomas approach) or the latest analyst consensus before the announcement (I/B/E/S; the Resurgence paper keeps only the last forecast dated *before* the announcement).
- `σ_i` = standard deviation of past surprises; the Resurgence paper requires **≥10 earnings announcements per firm** in the lookback (they use 6+ years of I/B/E/S history), "in line with Foster et al. (1984)".
- SUE is then **ranked into deciles** cross-sectionally (DSUE linearly scaled to −0.5…+0.5 in the Resurgence regressions).

**Portfolio rule (FOS / Bernard & Thomas):** long the top unexpected-earnings decile, short the bottom decile, hold for the **60 trading days** after the announcement. FOS estimate ≈ **25% annualized abnormal return, gross of costs** (quoted in the BT-1989 abstract).

**Key empirical regularities from Bernard & Thomas (1989/1990), as summarized in the sources read:**

- Drift is concentrated in the days immediately after the announcement but persists for weeks; a large fraction of the 60-day drift occurs around the *next* quarterly earnings announcements (BT1990, via secondary citation).
- Drift is larger for small firms and for firms with high transaction costs / low analyst coverage.
- The drift is not explained by conventional risk measures (beta, size) — BT1989 explicitly reject the risk-premium explanation.

**Worked SUE example (illustrative, our construction — not a literature result):**

```
Trailing 12 quarterly surprises (actual − consensus, $/sh): mean path ignored, σ = 0.11
This quarter: consensus 1.42, actual 1.61  →  surprise = +0.19
SUE = 0.19 / 0.11 = +1.73  →  cross-sectional rank vs all names reporting that week
If SUE ≥ 80th percentile of that week's cross-section → top-quintile candidate (long side)
```

**Drift-curve shape (what "front-loaded" means numerically).** The event-study literature's cumulative-abnormal-return (CAR) curve for extreme SUE deciles, as characterized across the fetched sources:

- Day −1…+1 (announcement window): the largest single move — and in the Martineau (2021) sample, an increasing share of the *total* adjustment over time (announcement-date responsiveness up 6× for all-but-microcaps between 1984–1990 and 2016–2019).
- Days +2…+20: the classic drift segment; FOS's ~25%-annualized figure is measured over the full 60-day window, and BT1990's evidence (secondary) says a disproportionate share lands around the *subsequent* earnings dates.
- Days +20…+60: decelerating tail; this is why our exit is at 20 trading days or 50%-of-expected-drift, not at the academic 60-day mark.

**Disagreement matrix (profitability after costs, by source):**

| Source | Sample | Verdict |
|---|---|---|
| FOS 1984 (via BT89 abstract) | 1970s–80s | ~25% ann. gross, extreme deciles, 60 days |
| Battalio et al. 2011 | their sample period | ≥ 14%/yr *net* of costs, hedged |
| Ng, Rusticus & Verdi 2008 | modern microstructure | profits "significantly reduced" by costs |
| RQFA practical simulation 2014 | 1974–2007 | **no net alpha** after realistic costs |
| Martineau 2021 | to 2019 | gone since 2006 (large) / 2016 (micro) |
| Resurgence paper 2025 | 2005–2024 | post-2020: large-cap drift +280%, >8%/yr hedge |

These span different universes, cost models, and decades; they are not directly comparable, and the honest summary is: gross drift is real and persistent in *some* segment nearly always; net exploitability in liquid large-caps is regime-dependent.

**Where sources disagree:**

- *Magnitude today.* Battalio, Lerman, Livnat & Mendenhall (2011, *Financial Review*) claim that under a wide range of timing and cost assumptions "over our sample period the PEAD was highly profitable after trading costs — an incremental investor could have earned hedged-portfolio returns of **at least 14% per year after costs**." Ng, Rusticus & Verdi (2008, *JAR*) find transaction costs "significantly reduce" PEAD profits and that high-cost firms drive the returns. A 2014 practical-simulation study (*Review of Quantitative Finance and Accounting*, 1974–2007 US data) finds **no abnormal return (alpha) at all** once realistic costs and timing are modeled. Martineau (2021) finds PEAD **gone since 2006** for all-but-microcap stocks and since ~2016 for microcaps. The 2025 Resurgence paper finds the opposite post-2020 (see §3). These cannot all be true simultaneously for the same universe and period — universe, cost model, and sample period explain most of the disagreement.
- *Surprise measure.* Random-walk SUE (FOS) vs analyst-consensus surprise (most modern work). Martineau (2021) shows random-walk surprises are much noisier and only predicted drift pre-1990 for all-but-microcaps; analyst surprises are the sharper instrument but halve the sample.

## 3. Why it works — mechanism & evidence

**Mechanisms proposed in the literature (with the evidence read this session):**

1. **Investor under-reaction / limited attention.** Prices incorporate earnings news slowly because investors underweight the information content of earnings (the BT1989 "delayed price response" conclusion). Behavioral support: retail investors systematically trade *against* earnings news — Kaniel et al. and Barber et al. (cited in the Resurgence paper) show retail are contrarians around announcements, selling positive surprises and buying negative ones; Luo et al. (2022) find retail net flows predict PEAD magnitude.
2. **Transaction-cost / arbitrage frictions.** Ng, Rusticus & Verdi (2008): earnings response coefficients are lower for high-transaction-cost firms and their post-announcement drift is higher — costs both explain persistence and bound exploitation. Chordia & Miao (2020, cited in Resurgence §2.5): the 60-day return spread between extreme surprise deciles is **4.7% in low-HFT stocks vs −0.8% in high-HFT stocks** — arbitrage capital with low latency erodes the anomaly exactly where it is cheapest to trade.
3. **Risk-premium explanation (partial rehabilitation).** Liu, Mao, Tang & Zhou ("Ex-Ante Risk Premia on Earnings Announcements", fetched via SSRN/AFA pages): the average ex-ante earnings announcement risk premium is ~**13 bp**, and — critically for us — **"PEAD is present only when the risk premia are high"; after controlling for the announcement risk premia, the literature's PEAD factor no longer has abnormal returns.** This says raw SUE drift may be compensation for announcement uncertainty, not free money — and motivates conditioning on the options-implied move.
4. **Options market under-estimates earnings uncertainty.** Gao, Xing & Zhang (2018, JFQA): ATM straddles bought 3 days before the announcement and held to the announcement earn a highly significant average **3.34%** — i.e., on average the *realized* move exceeds what option prices implied, especially for small, volatile, noisy, less-covered firms. A 2023 study of weekly options (MDPI *IJRFM*) defines the **option-implied earnings move = price of the ATM straddle as a proportion of the stock price**, and finds straddle returns are higher when historical earnings moves exceed the implied move — weekly straddles are "not optimally efficient."

**Decay / crowding evidence (must be weighed honestly):**

- Martineau (2021, *Critical Finance Review*): announcement-date prices are **6× (all-but-microcap) / 3× (microcap) more responsive** to surprises in 2016–2019 than in 1984–1990; since 2006 analyst surprises fail to predict post-announcement 60-day returns for all-but-microcaps; since 2016 for microcaps. "PEAD, as it has long been studied, may now rest in peace."
- McLean & Pontiff (2016, cited in Resurgence): anomaly returns decay ~50% in the decade after publication — the generic publication-decay benchmark.
- **Counter-evidence:** the 2025 Resurgence paper (220,228 announcements, 6,958 firms, 2005–2024, CRSP/Compustat/I/B/E/S) finds the average **60-day drift for large-caps increased ~280% post-2020**, with a zero-cost hedge portfolio earning **>8% annualized** post-2020; full-sample ~6% annualized gross, small-caps ~28%, large-caps ~3.48% (search-result synthesis of the fetched paper). They attribute the resurgence to retail-flow growth (2023 retail flows 84% above 2019 per Vanda Research, cited therein) and passive-driven inelasticity (Gabaix & Koijen: $1 of inflow moves market value ~$5).

**Net read:** the *unconditional, all-comers* PEAD trade in liquid large-caps was arbitraged away between ~2006 and ~2016, but the *conditional* question — which announcements are followed by drift — is alive. The two most actionable conditioners from the literature are (a) announcement uncertainty/risk premia (Liu et al.) and (b) realized-vs-implied move (Gao et al.; MDPI 2023). PEAD-IV is built directly on those two conditioners.

## 4. The twist: PEAD-IV

**Core idea.** Standardize the earnings surprise by the **options-implied move** (pre-earnings ATM straddle as % of spot) instead of by historical surprise dispersion alone, and trade only when the market *demonstrably under-reacted*: fundamental surprise sign is clear, but the realized announcement move is small relative to what the options market priced.

**Modification 1 — Implied-move standardization.**
*Weakness addressed:* raw SUE treats a 2% surprise move in a stock the options market expected to move 2% the same as one it expected to move 8%. The first is full price discovery (no drift left — consistent with Martineau's announcement-date efficiency); the second is plausibly incomplete adjustment. Liu et al. (2023) show PEAD concentrates in high-ex-ante-uncertainty names; the implied move is the cleanest market-based measure of that ex-ante uncertainty.
*Rule:* compute `IM_i = (C_ATM + P_ATM) / S_spot` at the close of the last trading day before the announcement, using the nearest listed expiry after the announcement (weekly if available). Compute the realized announcement move `RM_i = |S(T+1)/S(T−1) − 1|` (close-to-close around the announcement date T; use T = announcement day if BMO, T = next trading day if AMC). Trade only if `RM_i ≤ 0.75 × IM_i` (under-reaction gate).

**Modification 2 — Sign alignment gate.**
*Weakness addressed:* drift follows the *fundamental* surprise, not the price wiggle. A stock can gap up on a bad quarter (guidance games) and the drift then goes *down* — naive announcement-return momentum gets the sign wrong.
*Rule:* require `sign(SUE_i) = +1` (top-quintile SUE) for longs / `−1` (bottom-quintile) for shorts, AND the announcement-window return must not contradict the SUE sign by more than 1% (i.e., drop the trade if the market's first reaction disagrees with the fundamental sign beyond a tolerance band — ambiguous information content, skip).

**Modification 3 — Defined-risk options expression.**
*Weakness addressed:* stock-level PEAD carries market/sector beta and gap risk through the holding period; the classic long/short decile portfolio needs hundreds of names to diversify. A debit vertical spread isolates the drift with bounded loss and no tail beyond the premium, and monetizes the post-announcement IV crush rather than suffering it (spreads are roughly vega-neutral vs long straddles).
*Rule:* for aligned under-reactions, buy a 30–45 DTE debit call spread (positive surprise) or debit put spread (negative surprise): long leg ≈ ATM (50Δ), short leg at the strike nearest to `S × (1 + E[drift])` where `E[drift]` is the expected 20-day drift from the drift curve (§5). Max loss = debit paid.

**Modification 4 — Drift-curve exit discipline.**
*Weakness addressed:* the literature's 60-day window is an average; holding the full window exposes the position to the next-event cycle and to drift reversal. Published drift curves (FOS/BT lineage) are front-loaded.
*Rule:* exit at the earlier of (a) **20 trading days**, or (b) the underlying having realized **≥50% of E[drift]** in the trade direction. Hard risk exit: close the spread if its mark falls to 50% of the debit paid (time + adverse move stop).

## 5. Full specification of the twist variant

**Universe.** US common stocks (NYSE/NASDAQ/AMEX): price ≥ $5; market cap ≥ $1B; 60-day median daily dollar volume ≥ $10M; listed options with ≥ $0.10-wide-quotable ATM weekly/monthly markets and ATM open interest ≥ 500 contracts; announcement confirmed on a known calendar (no same-day surprises). Exclude: pending-M&A targets, ADRs without listed weekly options, names within 60 days of a prior announcement (overlapping-event exclusion, as in the Resurgence paper).

**Data requirements.** Point-in-time analyst consensus + actuals (I/B/E/S or equivalent) with *timestamps*; announcement date/time (BMO vs AMC) from a calendar vendor; OPRA/CBOE option quotes (EOD sufficient); CRSP-equivalent delisting-adjusted equity data.

**Signals (computed at close of T−1, announcement at T):**

```
SUE_i      = (EPS_actual − EPS_consensus_last) / σ(surprises, trailing 12 quarters, min 8 obs)
IM_i       = (C_ATM(T−1) + P_ATM(T−1)) / S(T−1)          # nearest post-announcement expiry
RM_i       = |S(T+1) / S(T−1) − 1|                        # T = announcement session (BMO) or next session (AMC)
UnderReact = RM_i ≤ 0.75 × IM_i
Aligned    = sign(SUE_i) == sign(CAR_i(announcement window) tolerance ±1%)
Eligible   = |SUE decile| in top/bottom quintile AND UnderReact AND Aligned
```

**Expected drift curve (for targets/exits).** Estimate on a trailing 5-year rolling estimation window, out-of-sample only: cross-sectional regression of `CAR(2,60)` on SUE decile, separately by cap bucket; store the decile-conditional curve `D(d, h)` = expected CAR from day +2 to day +h (h = 1…60). `E[drift]_i = D(decile_i, 20)`. Literature priors for sanity-checking only: FOS extreme-decile spread ≈ 25% annualized over 60 days (gross, 1974–83 era); Resurgence full-sample ≈ 6% annualized gross, large-caps ≈ 3.5% — i.e., expect single-digit *per-quarter* per-name drift for extreme deciles in modern data, less for large-caps.

**Drift-curve estimation protocol (detail).**

1. Estimation universe = all universe-eligible announcements in the trailing 5 years, whether or not options were traded (avoids conditioning the curve on our own filter).
2. Abnormal returns vs a 25-portfolio size/BM benchmark (the Resurgence paper's approach, using the French-library portfolios) — not raw returns; the drift claim is about abnormal return.
3. Fit `CAR(2,h) ~ decile dummies` per cap bucket per h ∈ {5, 10, 20, 40, 60}; store the full surface; interpolate linearly for intermediate h.
4. Floor: if `D(d, 20)` for the triggered decile is below 1.5× the expected round-trip option cost, skip the trade regardless of gates — the expected edge must clear the cost hurdle.
5. Re-estimate monthly; never intra-month (avoids conditioning on partially-realized drift of open trades).

**Entry.** At the close of T+1 (or T+2 open in the aggressive variant), buy:
- Positive: 30–45 DTE call debit spread, long 50Δ call, short call at strike nearest `S(T+1) × (1 + E[drift])`, targeting debit ≤ 55% of spread width.
- Negative: symmetric put debit spread.
- No entry if the spread's implied move to target offers < 1.3:1 max-gain:debit.

**Sizing.** Risk budget 75 bp of sleeve NAV per trade at max loss: `contracts = floor(0.0075 × NAV / (debit × 100))`, capped at 10% of the option's open interest and 25% of its average daily volume. Portfolio caps: ≤ 20 concurrent positions; ≤ 4 positions per GICS sector; aggregate premium-at-risk ≤ 8% of NAV; no new entries in the 5 sessions around FOMC/CPI if aggregate book delta would exceed ±0.30 × NAV per 1% index move.

**Exits.** (1) 20 trading days elapsed; (2) realized move in trade direction ≥ 50% of `E[drift]`; (3) spread mark ≤ 50% of debit; (4) underlying gaps through the short strike with < 7 DTE remaining (take the defined-risk off early rather than ride pin/assignment risk); (5) new material company event (guidance withdrawal, M&A rumor). Whichever first. No averaging down, ever.

**Costs.** Assume crossing 50% of the quoted bid/ask spread per leg plus $0.65/contract commissions; stress at 100% of spread. Model early-assignment risk on short ITM legs into dividends.

**Worked trade example (illustrative, hypothetical — not a result):**

```
Name: XYZ, $1B+ cap, reports AMC Tuesday (= announcement T; T+1 = Wednesday close)
T−1 close: S = 100.00; nearest Friday expiry ATM straddle = 3.40 + 3.10 = 6.50 → IM = 6.5%
SUE = +2.1 (top quintile). Wednesday close S(T+1) = 102.20 → RM = 2.2%
Gate: RM 2.2% ≤ 0.75 × 6.5% = 4.9% → under-reaction confirmed; sign aligned (+1.2% window return ≥ −1% tolerance)
Drift curve: D(top-quintile, 20d) from trailing 5-yr estimation = +3.0% → E[drift] = 3.0%
Structure: 37-DTE call debit spread — buy 100C (50Δ), sell 103C (≈ spot × 1.03), debit 1.55, width 3.00
Debit/width = 52% ≤ 55% ✓; max-gain:debit = (3.00 − 1.55)/1.55 = 0.94:1 … fails the 1.3:1 rule →
   re-strike short leg to 105C (debit 1.90, width 5.00, ratio 1.63:1 ✓) or skip if not achievable
Sizing (NAV $40M): 0.0075 × 40M / (1.90 × 100) = 1,578 → cap at 10% OI / 25% ADV, say 400 spreads
Exits: day 20; or XYZ ≥ 101.5 + 50%×3.0% move from entry reference; or spread mark ≤ 0.95
```

**Parameter summary (pre-registered defaults; robustness ranges in §7):**

| Parameter | Value | Source of prior |
|---|---|---|
| SUE lookback | 12 quarters, min 8 | FOS lineage / Resurgence construction |
| Surprise eligibility | top/bottom quintile | classic decile relaxed for optionable universe |
| Under-reaction gate κ | RM ≤ 0.75 × IM | between full-discovery (1.0) and strict (0.5) |
| Sign tolerance | announcement return ≥ −1% vs SUE sign | desk convention, to be validated |
| Tenor | 30–45 DTE | covers the 20-day drift window + theta cushion |
| Long leg / short leg | 50Δ / strike at spot×(1+E[drift]) | drift-targeted |
| Entry timing | close of T+1 | avoids announcement-day microstructure noise |
| Max hold | 20 trading days | front-loaded drift curve |
| Profit exit | 50% of E[drift] realized | half the expected move captures the front-loaded bulk |
| Risk exit | spread ≤ 50% of debit | time/adverse-move stop |
| Per-trade risk | 75 bp of sleeve NAV | desk risk budget |
| Book caps | ≤20 names, ≤4/sector, ≤8% NAV premium | correlation control |

**Earnings-season rhythm.** Expect ~65–70% of annual entries inside the four quarterly earnings windows (roughly weeks 2–5 of Jan/Apr/Jul/Oct for US reporters). Capacity planning, margin, and review cadence should follow that calendar; do not force trades in the off-season to smooth the trade count.

**Capacity.** Single-name equity options in ≥ $1B caps: realistically $25–75M sleeve NAV before spread-crossing costs degrade the edge; the constraint is the 10%-of-OI rule in the 30–45 DTE tenor.

## 6. Failure modes & regime dependence

- **Announcement-date efficiency (the Martineau regime).** If prices fully reflect surprises on day 0, the under-reaction gate rarely triggers in liquid names and triggers *falsely* in names where the implied move was simply wrong about direction. Early warning: share of triggered trades where day-2..5 follow-through matches SUE sign falls below ~52% over a rolling 6-month window.
- **The implied move is not a clean forecast.** Gao et al. (2018) show straddles *under*-price earnings uncertainty on average (their +3.34%) — so `RM ≤ 0.75×IM` will often be satisfied by chance in high-uncertainty names where no drift exists. The SUE-alignment gate is the defense; monitor gate-pass rates by SUE quintile.
- **Risk-premium confound.** Liu et al.: controlling for ex-ante announcement risk premia kills the PEAD factor's alpha. Our filter explicitly selects high-uncertainty names, which is where they say the drift *is* — but it may be compensation for bearing residual announcement risk, i.e., it can vanish or invert in risk-off regimes. Early warning: sleeve P&L correlation to short-vol factors rising above 0.4.
- **Earnings-season clustering.** Entries cluster in ~6-week quarterly windows → correlated sector bets and correlated theta. Mitigated by sector caps; expect feast/famine in trade count.
- **IV regime shifts.** A vol-market regime change (e.g., 2020-style) inflates IM mechanically, loosening the under-reaction gate exactly when realized moves are also huge — gate is relative, so it partially self-corrects, but monitor the distribution of RM/IM vs its trailing median.
- **Options microstructure.** Wide weekly spreads in mid-caps, pin risk near short strikes at expiry, assignment into ex-div dates. All bounded by defined risk, but transaction costs are the difference between the literature's gross numbers and any net reality (Ng et al. 2008; the 2014 RQFA simulation finding zero net alpha).
- **Regime dependence summary.** Works best: high retail participation, rising passive share, elevated but not crisis-level vol (the Resurgence paper's post-2020 regime). Works worst: hyper-efficient large-cap tape with dominant HFT market-making (Chordia & Miao's high-HFT −0.8% spread), and crisis tapes where "drift" is just beta.

**Monitoring dashboard (weekly, live):**

1. Gate-pass rate and its 26-week trend (collapsing pass rate = Martineau regime re-asserting).
2. RM/IM ratio distribution vs trailing 1-year median (regime shift detector).
3. Fraction of triggered trades with day-2…5 follow-through in SUE direction (target > 52%).
4. Sleeve P&L attribution: drift capture vs IV-crush mark vs directional beta (beta share should be < 25%).
5. Correlation of daily sleeve returns to a short-strangle index (rising toward 0.4 = we are secretly short vol).
6. Realized cost vs model (spread-crossing share); slippage drift > 25% over model ⇒ cut size.
7. Per-season P&L concentration (any season > 40% of cumulative = fragility).

## 7. Validation protocol

**Data.** Point-in-time I/B/E/S (or equivalent) consensus with estimate timestamps — never restated consensus; confirmed announcement timestamps (BMO/AMC matters: a BMO announcement's "T" is that session, an AMC announcement's "T" is the next session — getting this wrong is the classic PEAD backtest bug); CRSP delisting-adjusted returns; OPRA EOD option quotes with greeks; corporate actions.

**Splits.** Chronological only. Suggested: 2005–2014 in-sample for gate parameters (κ = 0.75, quintile cutoff), 2015–2019 validation, 2020–2024 true out-of-sample (this also straddles the Martineau "dead" regime and the Resurgence "alive again" regime — report both separately; a strategy that only works post-2020 is a regime bet, say so).

**Event-study hygiene.** Purge overlapping events (60-day exclusion, as Resurgence); embargo ±5 days around split boundaries for the 20-day holding period; cluster standard errors by calendar week (earnings cluster); report decile-monotonicity, not just the extreme spread.

**Options backtest realism.** Fill at mid ± 50% of spread, stress 100%; never assume fills at last-sale; model early assignment on short legs into dividends; exclude quotes failing arbitrage sanity checks; capacity analysis vs OI/ADV per name.

**Strategy-specific pitfalls.** (a) Look-ahead via restated consensus or revised announcement dates; (b) survivorship via dropping delisted names mid-holding-period; (c) earnings-calendar misalignment (BMO/AMC); (d) using the announcement-day return to define the surprise *and* to gate the trade (circularity — our SUE gate is fundamental-only, keep it that way); (e) silent selection bias from requiring listed options (options-listed names are larger/healthier — quantify vs the full SUE universe).

**Robustness.** κ ∈ {0.5, 0.75, 1.0}; SUE quintile vs decile; random-walk SUE vs analyst SUE; hold 10/20/40 days; stock-only expression vs spreads; exclude top-100 mega-caps; subperiod by VIX tercile.

**Acceptance criteria (pre-registered).** Net-of-costs (100%-of-spread stress) t-stat ≥ 2.5 on per-trade returns in 2020–2024 OOS; positive mean per-trade P&L in *both* 2015–2019 and 2020–2024 (regime robustness); max sleeve drawdown ≤ 12%; gate-pass rate ≥ 60 trades/year (statistical power); performance not concentrated in a single earnings season (no season contributing > 40% of cumulative P&L).

## 8. Sources read (annotated)

All accessed 2026-10-07.

1. **"Post-Earnings-Announcement Drift: Delayed Price Response or Risk Premium?" — Bernard & Thomas (1989), JAR 27:1–36.** Via RePEc/IDEAS listing (https://ideas.repec.org/a/bla/joares/v27y1989ip1-36.html) and OpenAIRE record (https://oamonitor.ireland.openaire.eu/rfo/sfi_rfo/search/publication?pid=10.2307%2F2491062). Bibliographic record + long abstract excerpt. *Taken:* correct citation; the FOS 25%-annualized-60-day figure as quoted in the abstract; the delayed-response vs risk-premium framing; confirmation Ball & Brown (1968) is the precursor. Full JSTOR PDF not fetched (paywall-adjacent); abstract-level only.
2. **"Rest in Peace Post-Earnings Announcement Drift" — Martineau (2021), Critical Finance Review.** Full text fetched (https://cfr.ivo-welch.org/forthcoming/papers/martineau2021rest.pdf). *Taken:* PEAD gone since 2006 (all-but-microcap) / ~2016 (microcap); 6×/3× announcement-date responsiveness gain 1984–1990 → 2016–2019; random-walk vs analyst surprise comparison; the adaptive-markets framing; 183-paper publication-count figure.
3. **"The Resurgence of Post-Earnings Announcement Drift" — 2025 working paper (Handelshögskolan i Stockholm repository).** Full text fetched (http://arc.hhs.se/download.aspx?MediumId=6317). *Taken:* sample construction (220,228 announcements, 6,958 firms, 2005–2024; ≥10-announcement requirement per FOS; 60-day overlap exclusion; $1 price floor); SUE/DSUE definitions; large-cap 60-day drift +280% post-2020, >8% annualized hedge return; retail-contrarian and passive-inelasticity mechanisms; Chordia & Miao 4.7% vs −0.8% HFT split; McLean & Pontiff ~50% decay.
4. **"Implications of Transaction Costs for the Post-Earnings-Announcement Drift" — Ng, Rusticus & Verdi (2008), JAR.** Abstract fetched (https://onlinelibrary.wiley.com/doi/10.1111/j.1475-679X.2008.00290.x). *Taken:* costs significantly reduce PEAD profits; lower ERCs and higher drift for high-cost firms; costs as an explanation for both existence and persistence.
5. **"Post-Earnings Announcement Drift: Bounds on Profitability for the Marginal Investor" — Battalio, Lerman, Livnat & Mendenhall (2011), Financial Review.** Abstract fetched (https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6288.2011.00310.x). *Taken:* the ≥14%/year-after-costs claim — the strongest pro-profitability evidence; noted sample-period dependence.
6. **"The profitability, costs and systematic risk of the PEAD trading strategy" — (2014), Review of Quantitative Finance and Accounting 43:605–625.** Abstract fetched (https://ideas.repec.org/a/kap/rqfnac/v43y2014i3p605-625.html). *Taken:* practical-simulation finding of **no net alpha** 1974–2007 after costs; event-study methods overstate return and understate risk.
7. **"Anticipating Uncertainty: Straddles around Earnings Announcements" — Gao, Xing & Zhang (2018), JFQA 53(6).** Abstract fetched (https://www.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/abs/anticipating-uncertainty-straddles-around-earnings-announcements/7B34877AD5E06304BA3C55FBA3219FDD). *Taken:* ATM straddles −3d→announcement earn +3.34% on average; investors underestimate earnings uncertainty; effect concentrated in small/noisy/expensive-to-trade names.
8. **"Ex-Ante Risk Premia on Earnings Announcements: Evidence from the Options Market" — Liu, Mao, Tang & Zhou.** SSRN page (https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4342267) and AFA conference page (https://afajof.org/management/viewp.php?n=55300) fetched. *Taken:* ~13 bp average ex-ante announcement premium; **PEAD present only when risk premia are high; PEAD factor alpha vanishes controlling for them**; conditional straddle-selling 0.56%/announcement-day figure. Direct motivation for the implied-move conditioning.
9. **"The Efficiency of Weekly Option Prices around Earnings Announcements" — (2023), MDPI Int. J. Financial Studies 16(5):270.** Full text fetched (https://www.mdpi.com/1911-8074/16/5/270). *Taken:* the exact implied-move definition used in §5 (ATM straddle price / stock price, expiry nearest the announcement); historical-vs-implied move gap predicts straddle returns; weekly straddle prices "not optimally efficient."

**Not accessed (known via secondary citation only):** Ball & Brown (1968); Foster, Olsen & Shevlin (1984) original; Bernard & Thomas (1990); Chordia et al. (2014); Chordia & Miao (2020); Luo et al. (2022); DellaVigna & Pollet (2009); Hirshleifer et al. (2009). Claims attributed to these are as quoted inside sources 1–3 above.

## 9. Further reading

- Bernard & Thomas (1990), JAE — earnings-implication chain (priority fetch next).
- Foster, Olsen & Shevlin (1984), *The Accounting Review* — original SUE construction.
- DellaVigna & Pollet (2009, JF) — investor inattention and Friday announcements.
- Hirshleifer, Lim & Teoh (2009, JF) — limited attention and information overload.
- Livnat & Mendenhall (2006, JAR) — SUE vs analyst-surprise methodology comparison.
- Chordia, Goyal, Sadka, Sadka & Shivakumar (2009, JF) — liquidity and momentum/PEAD interplay.
- Dubinsky, Johannes, Kaeck & Seeger (2019, RFS) — option pricing of earnings announcement risk.
- Atilgan (2014, JFE) — volatility spreads and earnings announcement returns.
- DellaVigna & Pollet (2007, JF) — investor inattention, Friday announcements (mechanism support).
- Ke & Ramalingegowda (2005, JAE) — institutional exploitation of drift; transient institutions trade it actively.
- Battalio & Mendenhall (2005, JFE) — earnings-surprise response by investor size.
