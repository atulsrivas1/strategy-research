# 09. Turtle Trend Following — Twist: TURTLE-X

> **Library:** Sigmatiq Strategy Library | **Bucket:** Position (weeks–months) | **Style:** Trend following / time-series momentum (systematic CTA)
> **Instruments:** Exchange-traded futures (equity index, rates, FX, energy, metals, ags) | **Typical holding period:** weeks to many months (pyramided) | **Complexity (1–5):** 4 | **Evidence grade (A–C):** B+ (extraordinary documented origin record; mixed modern replication — see §3)
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise. This library contains no local backtests yet.

## 1. Origin & lineage

- **Richard Dennis & William Eckhardt, 1983.** Dennis ("Prince of the Pit") bet Eckhardt that trading could be *taught*. From 1,000+ applicants to a classified ad (Barron's, WSJ, NYT) they interviewed 80, selected ~13 (later ~23 across classes), trained them for two weeks in December 1983, and funded them with $500K–$2M accounts from February 1984. The name came from Dennis's remark about growing traders "like they grow turtles in Singapore" (Stanley Angrist, WSJ 09/05/1989, quoted in the rules document).
- **The record.** Curtis Faith (an original Turtle) states the group earned an **average annual compound return of ~80% over the four years** of the experiment (Original Turtle Rules, Introduction — full text fetched). Jerry Parker recalls "most of the Turtles making 150% per year, four years in a row, with big risk, volatility and drawdowns" (The Hedge Fund Journal interview, fetched). Dennis reportedly staked the group and kept a share of profits.
- **Publication of the rules.** After the 10-year secrecy pact expired (end of 1993), a former Turtle and a marketing site (turtletrader.com) sold versions of the rules. In response, **Curtis Faith published the complete rules free at OriginalTurtles.org in 2003** — the primary source for §2 (full text fetched). Faith's book *Way of the Turtle* (2007) adds memoir context (book itself not fetched). Michael Covel's *Trend Following* and turtletrader.com popularized the story (site summary page fetched; note Faith's foreword is scathing about turtletrader.com's seller — "a guy who doesn't even trade his own rules" — so treat that site as secondary).
- **Descendants.** The Turtles effectively seeded the managed-futures/CTA industry: Jerry Parker founded **Chesapeake Capital (1988)** — RealVision's notes (fetched) state Chesapeake compounded **over 10% annually for 32 years with only 7 down years**, peaking near $2.5B AUM (THFJ). Other Turtles founded or joined notable CTAs. In the broader industry, Dunn Capital, Winton, and Mulvaney Capital represent the same long-term trend-following style at scale (context via the THFJ/TTU interviews fetched; their audited track records were not separately fetched this session — marked as secondary).
- **Academic validation.** Moskowitz, Ooi & Pedersen (2012) time-series momentum (full text fetched — see document 08) is the peer-reviewed backbone: sign-of-past-12-months trend with 1/σ sizing across 58 futures, positive in every asset class, "performs best during extreme markets," speculators profit at hedgers' expense. The Turtle system is a Donchian-breakout parametrization of exactly this phenomenon.

## 2. The original rules (as published)

Source: *The Original Turtle Trading Rules*, Curtis Faith / OriginalTurtles.org (2003), fetched in full. Numbers below are quoted from that document.

**Markets.** Liquid US futures only: CBOT 30-yr Bond and 10-yr Note; CME S&P 500, Eurodollar, 90-day T-Bill, Swiss Franc, Deutschmark, British Pound, French Franc, Japanese Yen, Canadian Dollar; CSCE Coffee, Cocoa, Sugar, Cotton; COMEX Gold, Silver, Copper; NYMEX Crude Oil, Heating Oil, Unleaded Gas. Excluded: grains (Dennis's own position limits) and meats (pit corruption). Liquidity was the primary criterion.

**Volatility unit N.**
```
TR = max(H − L, |H − PDC|, |PDC − L|)        # PDC = previous day's close
N  = (19 × PDN + TR) / 20                    # 20-day EMA of TR (≈ ATR20);
                                             # seed with 20-day simple average
```

**Position sizing — the Unit.**
```
Dollar Volatility = N × Dollars per Point
Unit = (1% of Account) / Dollar Volatility    # 1 N of adverse move = 1% of equity
```
Example from the document: Heating Oil, N = 0.0141, $1M account, $42,000/point ⇒ Unit = 0.01×1,000,000/(0.0141×42,000) = 16.88 → **16 contracts** (truncate). Unit sizes were recomputed weekly.

**Entries (two systems; Turtles could allocate between them at discretion):**
- **System 1:** enter 1 Unit when price exceeds by one tick the high/low of the preceding **20 days** — intraday, at the breakout, not the close. **Filter:** skip the signal if the *last* breakout (taken or not) would have been a winner (a breakout counts as a loss if price moved 2N against it before a profitable 10-day exit). **Failsafe:** if a signal was skipped because the last trade was a winner, enter anyway at a **55-day** breakout.
- **System 2:** enter 1 Unit on a **55-day** breakout, every signal taken regardless of the previous outcome.

**Adding (pyramiding).** Add 1 Unit every **½ N** in favor, measured from the *actual fill* of the previous unit (slippage compounds into the ladder), up to **4 Units** per market. Worked example in the document: Crude, N = 1.20, 55-day breakout 28.30 → units at 28.30 / 28.90 / 29.50 / 30.10.

**Stops.** **2 N** from the most recent entry, for every unit; on each add, all stops move to 2N from the newest fill (so total position risk stays ≈ 2% at 4 units... in practice slightly more with gap fills — the document's gap example shows the 4th unit's stop 1.6N from its fill). No trade may risk more than 2% of equity. Stops were *mental* (not resting orders) to avoid revealing size. **Alternate "Whipsaw" stop:** ½ N stops (½% risk per unit), re-enter at the original entry price if stopped; better profitability per the document, lower win rate, harder to execute.

**Exits.** System 1: **10-day** opposite breakout (10-day low for longs). System 2: **20-day** opposite breakout. All units out at once. The document stresses these exits are the hardest part — "watching 20%, 40% even 100% of significant profits evaporate."

**Worked examples quoted from the rules document (Faith's own numbers):**

*Add ladder (Gold):* N = 2.50, 55-day breakout at 310 → units at 310.00 / 311.25 / 312.50 / 313.75 (each +½N from the prior *fill*).

*Stop ladder (Crude Oil):* N = 1.20, breakout 28.30:

| Unit | Entry fill | Stop after this add |
|---|---|---|
| 1 | 28.30 | 25.90 (= 28.30 − 2N) |
| 2 | 28.90 | 26.50 for both (= 28.90 − 2N) |
| 3 | 29.50 | 27.10 for all three |
| 4 | 30.10 | 27.70 for all four |

Gap case: if the 4th unit fills at 30.80 on an opening gap, its stop is 28.40 while units 1–3 keep 27.70 — total risk slightly exceeds the 2%-per-position ideal; the document accepts this as the cost of fast markets.

*Whipsaw alternate (same Crude example):* stops at ½N from each unit's own fill (28.30→27.70, 28.90→28.30, 29.50→28.90, 30.10→29.50), each unit re-entered if price returns to its original entry; aggregate risk never exceeds 2% at four units; "better profitability… lower win/loss ratio… harder to execute," and only "a few Turtles traded this method with good success."

*Unit-size truncation:* with a $100K account the Heating-Oil example truncates 1.688 → 1 contract — Faith's point that small accounts cannot diversify properly because unit granularity is too coarse. This matters for our sleeve minimum size (§5).

**Portfolio heat limits (units):**
| Level | Scope | Max |
|---|---|---|
| 1 | Single market | 4 |
| 2 | Closely correlated markets (e.g., HO/CL, GC/SI, CHF/DEM, T-bill/Eurodollar) | 6 |
| 3 | Loosely correlated markets (e.g., GC/CU) | 10 |
| 4 | Single direction, total | 12 |

**Drawdown de-risking.** Notional account cut **20% for every 10% drawdown** from the yearly starting equity (e.g., $1M → down $100K → trade as $800K; down another $80K → $640K), restored at the yearly reset.

**Tactics.** Limit orders preferred; don't panic in fast markets — wait for stabilization; on simultaneous signals in a correlated group, buy the *strongest* / sell the *weakest* (strength measured in N-terms or 3-month change ÷ N); roll contracts a few weeks before expiry, only into months whose price action would already justify a position.

**Disagreements/ambiguities across sources:** (a) Faith's document is the authoritative rule set; turtletrader.com's summary (fetched) matches on S1/S2/N/units but is a marketing site — use Faith. (b) The MQL5 implementation article (fetched) notes the rules are "rarely implemented correctly" in code despite being simple — operational details (fill-based add ladders, mental stops, roll judgment) are where implementations diverge. (c) George Pruitt (fetched) notes "several operational choices — position sizing nuances, market selection, roll/contract handling — were left to judgment," which explains why published Turtle backtests diverge so widely.

## 3. Why it works — mechanism & evidence

**Mechanism.** Long-run positive autocorrelation in futures returns (MOP 2012: significant continuation at 1–12-month lags across all four asset classes, then reversal) harvested with asymmetric payoff: many small 2N losses, few enormous trend wins. Faith: "most of the profits in a given year might come from only two or three large winning trades." The breakout entry is deliberately naive; the edge lives in sizing (vol-normalized units), pyramiding, and *not* exiting early. Structurally, MOP's CFTC evidence says trend speculators are paid by hedgers — a risk-transfer premium, not just a behavioral anomaly, which helps explain persistence across a century of data.

**Evidence — origin record.** ~80%/yr average compound over 4 years for the class (Faith); ~150%/yr per Parker's recollection (THFJ) — these two figures conflict by 2×; treat "80% class average" as the more sober claim and Parker's as the best-students memory. Either way it was a leveraged, high-drawdown profile, not a smooth one.

**Evidence — descendants.** Chesapeake: >10%/yr over 32 years, 7 down years (RealVision notes); "made money ten years in a row" early (Parker, THFJ and Better System Trader). Parker is explicit that the industry has decayed: "liquid futures markets not trending as well as they used to… we know of no CTA that has recently come close to the types of returns generated in the 1980s, or even the 1990s" (THFJ, fetched). He also warns against over-optimization from his own live failure trying to smooth the equity curve (Better System Trader, fetched) — directly relevant to our twist design (§4).

**Evidence — modern replications of the literal rules (all fetched; treat as illustrative blogs, not peer review):**
- TradingWithRayner (2000–2019, his market set, $10/trade cost, no pyramiding): original 20-day system — **−0.38%/yr, −95.38% max DD, 36.8% win rate**. His modified 200-day-breakout/1%-risk variant: **+32.12%/yr, −41.51% DD, 41% win rate**; 189- and 227-day breakouts similar (robust plateau). Conclusion: "the original turtle trading rules don't work anymore… the principles still work."
- Loomi.ai (NQ futures 2010–2026, simplified, no pyramiding): 55-day long PF 4.56 (41 trades), 20-day long PF 1.89; **short side catastrophic at both lengths** (PF 0.16–0.21) — a single-asset, long-bias-regime result.
- RogueQuant (43 futures, 2007–2025, long-side 20/10 with ATR sizing): aggregate profit $1.15M across markets with wide dispersion — diversification is doing the work.
- MQL5 article: expects 30–40% win rates; edge is winner/loser asymmetry.
- George Pruitt's "Turtle thermometer": trend following "doing well" into late 2025 post-pandemic, after a long doldrums — regime dependence confirmed by a practitioner.

**Net read.** The *style* (diversified, vol-scaled, long-vol trend) has both a documented origin record and academic support (MOP). The *literal 1983 parameters* show badly degraded standalone performance in modern replications. Any adoption must be as a portfolio-level, risk-managed sleeve — which is what TURTLE-X specifies.

**Context on the two Turtle classes and the secrecy pact.** Faith's document records that the first class trained in December 1983 and began trading January 1984 with small accounts before the $500K–$2M allocations in February; a second class followed. The 10-year confidentiality agreement expired at the end of 1993 — which is why the 1990s saw rule-selling (the trigger for Faith's free 2003 publication) and why the 1984–1988 window is the only period with an authoritative, contemporaneous P&L claim. Everything after is descendant funds (Chesapeake et al.) running *evolved* versions, so "the Turtles made X%" and "the Turtle rules make X%" are different claims — only the first is directly documented.

**Trend's longer-run evidence base (secondary citations, not fetched this session).** The fetched MOP paper covers 1965–2009 across 58 instruments; the AQR "Century of Evidence on Trend-Following Investing" (Hurst, Ooi, Pedersen) extends monthly trend to 1880; Greyserman & Kaminski argue trend-like payoffs appear in centuries of commodity data. These are listed in §9 as priority fetches; we deliberately anchor TURTLE-X's *parameters* on the fetched primary rules and its *style warrant* on the fetched MOP paper only.

## 4. The twist: TURTLE-X

Three modifications, each tied to a documented weakness. Deliberately conservative in number — Parker's over-optimization warning (§3) is taken as a design constraint: every added rule must defend itself against a specific, named failure mode.

**Modification A — Adaptive breakout length via Efficiency Ratio (ER).**
*Weakness addressed:* fixed 20/55 lengths are regime-blind. Rayner's replication shows the 20-day system bleeding in modern chop while longer breakouts stayed profitable; Pruitt notes trendiness itself is cyclical. A market in a clean trend wants a fast channel; a noisy market wants a slow one.
*Rule:* for each market, monthly, compute Kaufman's Efficiency Ratio over the trailing 120 trading days for each candidate lookback L ∈ {20, 55, 100}:
```
ER(L) = |Close(t) − Close(t−L)| / Σ_{i=t−L+1..t} |Close(i) − Close(i−1)|
```
averaged over all L-windows inside the 120-day evaluation window (i.e., mean ER of rolling L-day windows). Select the L with the highest mean ER, with hysteresis: switch only if the challenger beats the incumbent's ER by ≥ 0.05. Exit channel = ½ the selected entry lookback, rounded to {10, 20, 50} (mapping 20→10, 55→20, 100→50), preserving the original ~2:1–2.75:1 entry/exit asymmetry. The System-1 "last breakout was a winner → skip, with 55-day failsafe" filter is **retained only for L = 20** signals (its original context); L = 55/100 signals are always taken (their original System-2 behavior).

**Modification B — Correlation-cluster portfolio heat.**
*Weakness addressed:* the original 4/6/10/12 unit limits use 1983's static, judgment-based correlation groups ("heating oil and crude oil; gold and silver…"). Modern macro regimes correlate whole asset classes (2022: bonds+equities together); a static 6-unit "closely correlated" cap can hide far more than 6 units of true factor risk.
*Rule:* define 8 fixed clusters: {Equity indices}, {STIR}, {Bonds}, {FX-USD majors}, {Energy}, {Metals}, {Grains/Softs}, {Crypto}. Risk is measured in units as before (1 unit = 1% of equity per 1N). Caps: **4 units per market** (unchanged); **8 units per cluster per direction** (= 2× single-market risk, replacing the 6/10 distinction); **12 units total per direction** (unchanged); plus a *measured* overlay: if a cluster's average pairwise 63-day correlation of daily returns exceeds 0.7, its cap drops to 6 units (the original "closely correlated" level) until correlation falls below 0.55.

**Modification C — Equity-curve circuit breaker.**
*Weakness addressed:* the original de-risking (−20% size per −10% DD, reset yearly) is slow, calendar-anchored, and can leave full size on through a year-long bleed — Faith documents multi-month to 1–2-year losing stretches as normal. A trend system whose own equity is *in a downtrend* is statistically likely to be in an unfavorable regime (Pruitt's thermometer logic).
*Rule:* track the strategy sleeve's daily equity curve E(t) and its 100-day simple moving average MA100(E). When E(t) < MA100(E): halve unit size (1 unit = 0.5% of equity per 1N) for all *new* entries and adds; existing positions keep their stops/exits unchanged (no forced liquidation — trend followers get killed whipsawing out of positions). Restore full unit size when E(t) closes back above MA100(E) for 5 consecutive sessions. The original −20%-per−10%-DD rule is **retained as a hard overlay** on top (it caps what the circuit breaker might miss in a fast crash).

## 5. Full specification of the twist variant

**Universe (~45 markets, all USD-denominated, min $100M daily notional on the traded contract).**
- Equity index: ES, NQ, RTY, FESX (EuroStoxx), FDX (DAX), FTSE, TOPIX
- Bonds/STIR: ZN, ZB, UB, Bund, Gilt, JGB, SOFR 3M (SR3), SONIA
- FX: 6E (EUR), 6J (JPY), 6B (GBP), 6A (AUD), 6C (CAD), 6S (CHF), DX-adjacent EM via MSCI or BRL/MXN where liquid
- Energy: CL, HO, RB, NG, Brent, Gasoil
- Metals: GC, SI, HG, PL
- Ags/softs: ZC, ZW, ZS, KC, CT, SB, CC
- Crypto: CME BTC, ETH futures (own cluster; capped hard, see below)

**Data.** Daily OHLC on individual contracts; continuous back-adjusted series for signal computation (ratio-adjusted); volume/OI for roll timing; contract specs for dollars-per-point.

**Signals & entries.**
- N = 20-day EMA of TR per the original formula, recomputed daily; unit size recomputed weekly (as the Turtles did).
- Entry: stop order 1 tick beyond the L-day high/low, L ∈ {20,55,100} per Modification A, evaluated intraday (original behavior) — in backtest, assume fill at the stop price + slippage.
- S1-style skip filter applies only when L = 20; failsafe = next longer candidate lookback's breakout.
- Adds: 1 unit per ½N from actual fills, max 4 units/market.
- Stops: 2N from latest add, all units; Whipsaw variant (½N, re-entry at original price) tested as a robustness variant only.
- Exits: opposite breakout at the mapped exit length {10, 20, 50}; all units out.

**Sizing & risk.**
- Base unit = 1% of current (circuit-breaker-adjusted: 0.5%) sleeve equity per 1N.
- Cluster caps per Modification B; total 12 units/direction; crypto cluster hard-capped at 2 units total regardless.
- Portfolio vol overlay: if sleeve 21-day realized vol exceeds 15% annualized, scale all new unit risk by 15%/realized (floor 0.5×) — this is the one concession to modern CTA practice (Parker discusses using vol in sizing on TTU145).

**Costs & execution model.** $2.50/contract/side commissions + fees; slippage = 1 tick for STIR/bonds/FX majors, 2 ticks equity index/energy/metals, 3 ticks ags/crypto; roll on the earlier of (volume flip to next contract) or 10 calendar days before first notice; back-adjusted signals, actual-contract P&L.

**Cluster membership (Modification B):**

| Cluster | Members | Cap (normal / high-ρ) |
|---|---|---|
| Equity indices | ES, NQ, RTY, FESX, FDX, FTSE, TOPIX | 8 / 6 units |
| STIR | SR3, SONIA, (Eurodollar legacy) | 8 / 6 |
| Bonds | ZN, ZB, UB, Bund, Gilt, JGB | 8 / 6 |
| FX majors | 6E, 6J, 6B, 6A, 6C, 6S, MXN, BRL | 8 / 6 |
| Energy | CL, HO, RB, NG, Brent, Gasoil | 8 / 6 |
| Metals | GC, SI, HG, PL | 8 / 6 |
| Grains/softs | ZC, ZW, ZS, KC, CT, SB, CC | 8 / 6 |
| Crypto | BTC, ETH (CME) | 2 / 2 (hard) |

High-ρ state: cluster-average pairwise 63-day return correlation > 0.70 (enter) / < 0.55 (exit). Correlations computed on daily log returns of the back-adjusted series, measured weekly.

**Worked trade example (illustrative, hypothetical — not a result):**

```
Market: CL (crude). Sleeve equity $50M. Circuit breaker: equity > MA100 → full units.
N = 1.20 ($1,000/point × 1,000 bbl contract → dollar vol = 1.20 × 1,000 = $1,200/contract)
Unit = 1% × 50M / 1,200 = 416 → 416 contracts (vs Faith's 1983 sheets: same math, bigger equity)
ER selection (monthly): mean ER over trailing 120d — ER(20) = 0.21, ER(55) = 0.34, ER(100) = 0.29
→ L = 55 (incumbent was 20; challenger beats by 0.13 ≥ 0.05 hysteresis band → switch)
Entry: stop-buy 1 tick above 55-day high 78.40 → filled 78.42 (2-tick slippage model)
Adds: 78.42 + 0.60 = 79.02, 79.62, 80.22 (½N ladder from fills); stops ratchet: 76.02 → 76.62 → 77.22
Exit channel for L=55: 20-day low. Position rides; stopped flat at 20-day low 81.10 six weeks later.
Cluster check at entry: Energy cluster already long 4 units HO + 2 units RB → adding 4 CL = 10 > 8 cap
→ CL position capped at 2 units until HO exits or correlation state changes.
```

**Minimum sleeve size.** Faith's truncation example (§2) applies to us: below ~$10M sleeve equity, 1%-units in high-dollar-vol markets (ZB, NG, BTC) truncate to 0–1 contracts and the diversification math breaks. Minimum viable sleeve: $10M; comfortable: $25M+.

**Capacity.** At 1% risk per unit and 12 units max per direction, a $50M sleeve risks ≤ $6M per direction — small vs CTA scale; capacity is a non-issue to ~$500M in the listed universe except ags/softs (position limits) and crypto (CME OI).

## 6. Failure modes & regime dependence

- **Trendless chop (the killer).** Rayner's 2000–2019 result (−0.38%/yr, −95% DD on his implementation) is what a long chop regime does to fast breakout systems. Modification A (adaptive length) and C (circuit breaker) exist precisely for this; expect them to *reduce*, not eliminate, bleed. Early warning: sleeve-level average ER across markets (our own "thermometer," Pruitt-style) in the bottom quintile of its 5-year history → expect flat-to-negative quarters.
- **Crowded exits / gap risk.** Mental stops were fine for $2M accounts in 1984; gaps through 2N stops happen (Faith's own example: Turtles long rates into the 1987 crash lost 20–40% of equity *in a day* despite limits). Defined-risk is impossible in futures; the cluster caps and vol overlay are the mitigations.
- **Long-bias regimes end.** Loomi's NQ test shows shorts catastrophic in a one-way bull asset; diversified futures books need two-sided trends. A decade of CB-put-supported risk assets (2010s) degrades short-side trend quality — monitor short-side expectancy separately; if negative over rolling 3 years across ≥ 60% of markets, consider long-biasing the equity-index cluster only (a documented, pre-registered exception, not a discretionary call).
- **Correlation regime shifts.** Modification B's correlation overlay can clamp the book exactly when trends are strongest (macro crises correlate everything *and* trend beautifully — 2008, 2022). This is the known cost of the rule; accept it. The 0.7/0.55 hysteresis band limits flutter.
- **Circuit-breaker whipsaw.** MA100 on the equity curve will halve size near the bottom of some drawdowns and restore it after recovery has begun — locking in a slower recovery. That is the price of regime protection; Parker's warning about "improving" trend systems applies — do not tune the 100-day length in-sample.
- **Adaptive-length selection risk.** ER-based selection can systematically arrive *late* — switching to L = 100 after the fast trend is over, or to L = 20 just as chop begins. The 0.05 hysteresis band and monthly (not daily) re-selection are the dampers; the acceptance protocol (§7) forces the adaptive variant to beat fixed-55 out-of-sample or be reverted.
- **Crypto cluster tail risk.** CME BTC/ETH futures gap over weekends; 2N stops are not executable when the market is closed. Hence the hard 2-unit cap and the standing rule that crypto stops are treated as "first tradable price" in backtests, with gap slippage modeled at 3× normal.
- **Roll/back-adjustment artifacts.** Signal series (ratio-adjusted) vs traded series diverge in backwardated/contango'd commodities; a breakout on the adjusted series may not exist on the traded contract. Rule: signals computed on the *traded* contract's own history once it has ≥ L+10 days of data; else map from adjusted series with a documented transform.

**Monitoring dashboard (weekly, live):**

1. Sleeve "thermometer": cross-market average ER(55), percentile vs 5-year history (Pruitt-style regime gauge); bottom quintile = expect chop bleed.
2. Circuit-breaker state and days-in-state; if the breaker spends > 60% of trailing 2 years active, the base unit risk is too high for the regime — review, don't re-tune.
3. Cluster heat utilization and correlation-state flips per quarter (> 4 flips/cluster/year = hysteresis too tight).
4. Short-side expectancy by cluster, rolling 3 years (the Loomi diagnostic).
5. Add-ladder fill quality: realized slippage vs the 1/2/3-tick model; persistent 150%+ ⇒ downgrade liquidity assumptions for that market.
6. Win rate and payoff ratio vs the 30–40% / asymmetric-win expectation (MQL5/Faith); a rising win rate with falling payoff = we are secretly becoming a mean-reversion book.
7. Open-risk aggregation: total 2N-stop distance across the book as % of equity (the 1987 scenario metric; Faith reports 20–40% single-day losses *with* the original limits — know our number before the gap).

## 7. Validation protocol

**Data.** Individual-contract daily data 1975–present where available (CSI/Norgate/Barchart class), including delisted/dead contracts (e.g., DEM, FRF — the original Turtle FX set) to avoid survivor tilt; contract specs history (tick sizes, multipliers change — e.g., US bond futures); volume/OI for rolls.

**Splits.** Chronological: 1975–1994 in-sample (the era the rules were built in — expect them to work; this is a sanity check, not evidence), 1995–2009 validation, 2010–present out-of-sample (the regime where Rayner's replication failed — the decision window). Report per-decade and per-cluster attribution.

**Futures-specific hygiene.** (a) Back-adjusted vs traded-contract signal consistency check on every trade; (b) roll-cost model from actual calendar spreads, not zero-cost assumption; (c) margin/equity accounting — futures P&L is not fully invested capital; report return on margin *and* on notional equity; (d) limit-locked days (ags) — unfilled stops must gap to the next tradable price; (e) the 1987-style gap scenario as a standing stress test.

**Strategy-specific pitfalls.** (a) Look-ahead in ER lookback selection (use only data up to t−1; monthly re-selection); (b) fill assumption at exact breakout price — always add slippage; (c) the S1 skip filter's dependence on hypothetical untaken trades (must track virtual trades — a classic implementation bug, flagged in the MQL5 article); (d) unit-size truncation effects at small equity (Faith's $100K example truncates 1.688 → 1 contract — granularity matters; test at realistic sleeve sizes); (e) equity-curve MA computed on mark-to-market including open P&L (define it; don't let it be ambiguous at test time).

**Robustness.** L grid {20,55,100} vs fixed-55 baseline vs fixed-20/55 dual system (the original); ER threshold {0.03, 0.05, 0.10}; cluster caps {6, 8, 10}; MA ∈ {75, 100, 150} days for the breaker (report, don't select); Whipsaw vs standard stops; with/without crypto cluster.

**Acceptance criteria (pre-registered).** OOS (2010+): positive expectancy per unit-risked at t ≥ 2; max DD ≤ 35% at 1%-unit risk; MAR (CAGR/maxDD) ≥ 0.5; correlation to SG Trend Index ≥ 0.6 (we *want* to be the style, honestly) with tracking differences explained by the three modifications; the adaptive-length variant must beat fixed-55 on MAR in OOS or Modification A is reverted to fixed 55 (Parker's anti-overfitting rule: simpler wins ties).

**Kill criteria.** Two consecutive calendar years of negative gross P&L with the thermometer (§6) in its bottom quintile AND short-side expectancy negative in ≥ 60% of markets ⇒ sleeve halved pending research review. Three consecutive years negative ⇒ retired to research. No parameter may be changed live to avoid a kill criterion being hit — that is exactly Parker's over-optimization trap, and it is named here so the rule survives contact with a drawdown.

## 8. Sources read (annotated)

All accessed 2026-10-07.

1. **"The Original Turtle Trading Rules" — Curtis Faith / OriginalTurtles.org (2003).** Full PDF fetched (https://c.mql5.com/3/131/Curtis_Faith_-_Original_Turtle_Rules.pdf; identical copies seen at tradingwithrayner.com and pipsologie.com). *Taken:* every rule in §2 — N formula and seeding, unit formula and the Heating-Oil worked example, S1/S2 entries with the last-breakout filter and 55-day failsafe, ½N add ladder from actual fills, 2N stops with stop-raising, Whipsaw alternate stops, 10/20-day exits, 4/6/10/12 heat limits, −20%-per−10% equity adjustment, order tactics, roll guidance, buy-strongest/sell-weakest, the 80%/yr class record, and the 1987 crash loss anecdote (20–40% of equity in a day). Also the foreword's warnings about turtletrader.com and the unnamed former Turtle selling rules.
2. **"The Original Turtle Trading Rules — Taught by Richard Dennis in 1983" — turtletrader.com/rules.** Fetched (https://www.turtletrader.com/rules/). *Taken:* cross-check of S1/S2/N/unit descriptions (consistent with Faith); treated as secondary per Faith's foreword.
3. **TradingBlox — "The Original Turtle Rules" page.** Fetched (https://www.tradingblox.com/originalturtles/originalturtlerules.htm). *Taken:* confirmation of the document's provenance and that the rules were published "unambiguously, so that it can be tested"; note on 20 years of forum testing including the last-trade-winner filter.
4. **"Chesapeake Capital's Jerry Parker" — The Hedge Fund Journal.** Fetched (https://thehedgefundjournal.com/chesapeake-capitals-jerry-parker/). *Taken:* $1M accounts Jan 1984; "most of the Turtles making 150% per year, four years in a row"; Chesapeake founded 1988 with $3M; "made money ten years in a row"; peak ~$2.5B AUM; CTA industry return decay quote; "when I overrode the models to reduce risk, it rarely worked out."
5. **"Jerry Parker — Follow the Rules" — RealVision (interview notes).** Fetched (https://www.realvision.com/jerry-parker-follow-the-rules-lessons-on-systematic-trend-following). *Taken:* Chesapeake >10%/yr compounded over 32 years with 7 down years; 23 participants in the experiment; Parker as rule-follower case study.
6. **"TTU145: Jerry Parker" — Top Traders Unplugged.** Fetched (https://www.toptradersunplugged.com/podcast/ttu145-jerry-parker-founder-of-chesapeake-capital/). *Taken:* post-program founding narrative; 10 straight winning years; drawdown/vol as the classic trend-following cost; Parker's use of volatility in sizing; "trend following plus nothing."
7. **"Jerry Parker: The Dangers of Over-Optimization" — Better System Trader.** Fetched (https://bettersystemtrader.com/trading-triumphs-jerry-parker-3-the-dangers-of-optimization/). *Taken:* the live over-optimization failure story; "one entry rule, one exit rule, a stop. No more"; advice to start with one medium/long-term trend system; "the one thing you need… large sustained trends, is completely outside your control." Design constraint for §4.
8. **"Turtle trading rules: Does it still work today?" — TradingWithRayner.** Fetched (https://www.tradingwithrayner.com/turtle-trading-rules/). *Taken:* 2000–2019 replication of the literal rules (−0.38%/yr, −95.38% DD, 36.83% win, 4,322 trades, $10/trade cost) and the 200-day variant (+32.12%/yr, −41.51% DD) with 189/227-day robustness plateau; "principles still work" conclusion. Practitioner blog — illustrative, not peer-reviewed.
9. **"Turtle Trading Rules: Donchian Breakout Backtest" — Loomi.ai.** Fetched (https://www.loomiai.io/learn/turtle-trading-rules-donchian-backtest/). *Taken:* NQ 2010–2026 simplified test: 55-day long PF 4.56 vs short PF 0.16; long-side decadal consistency, short-side collapse; regime asymmetry evidence.
10. **"I Backtested The Legendary Turtle Trading Strategy Across 40 Futures Markets" — RogueQuant (Substack).** Fetched (https://roguequant.substack.com/p/i-backtested-the-legendary-turtle). *Taken:* 43 markets, 2007–2025, unoptimized long-side 20/10 + ATR sizing; $1.15M aggregate with wide cross-market dispersion — diversification as the engine.
11. **"A Turtle Thermometer for Trend-Following: 2025 Results" — George Pruitt.** Fetched (https://georgepruitt.com/using-turtle-to-gauge-state-of-trend-following-2025/). *Taken:* mechanical bare-bones Turtle as a trendiness gauge; post-pandemic trend recovery into 2025; note that operational choices were left to judgment, explaining divergent Turtle results.
12. **"Automating Classic Market Methods (Part 5): The Original Turtle Trading Rules" — MQL5.com.** Fetched (https://www.mql5.com/en/articles/23448). *Taken:* implementation pitfalls (virtual-trade tracking for the S1 filter); expected 30–40% win rate; System-2 larger-but-rarer winners.
13. **"Time Series Momentum" — Moskowitz, Ooi & Pedersen (2012), JFE.** Full PDF fetched (https://w4.stern.nyu.edu/facdir/lpederse/papers/TimeSeriesMomentum.pdf). *Taken:* the academic warrant for the style (see document 08 §8.3 for the full annotation).

**Not accessed (secondary citation only):** Faith, *Way of the Turtle* (2007); Covel, *Trend Following*; Schwager, *Market Wizards* (the Dennis "publish my rules in the newspaper" quote is reproduced inside source 1); audited Dunn/Winton/Mulvaney track records; Angrist WSJ 1989 original article.

## 9. Further reading

- Curtis Faith, *Way of the Turtle* (2007) — memoir + the "Rsi2"/optimization discussions.
- Michael Covel, *Trend Following* — industry context; read critically (marketing tilt per Faith's foreword).
- Greyserman & Kaminski, *Trend Following with Managed Futures* — 700-year trend evidence.
- Hurst, Ooi & Pedersen, "A Century of Evidence on Trend-Following Investing" (AQR).
- Daniel & Moskowitz (2016) — crash dynamics of momentum/trend factors.
- Della Corte, Kosowski & Papanikolaou — trend following with volatility scaling.
- OriginalTurtles.org archive — Turtle Q&A and the charity-donation proviso of the free rules.
- Covel's *Trend Following* (updated editions) — for the Dunn/Winton/Mulvaney track-record chapters; verify any quoted CAGRs against audited BarclayHedge/NilssonHedge data before citing internally.
- Kaminski & Lo, "When do stop-loss rules stop losses?" (J. Financial Markets) — the academic treatment of stop/exit rules like our 2N and 10/20-day channels.
- Seykota, Carr, and other Market-Wizards trend interviews — trader-discretion context around mechanical cores.
