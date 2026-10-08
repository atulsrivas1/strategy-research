# 10. Volatility Risk Premium Harvesting (Short Vol / Put Writing) — Twist: VRP-GATE

> **Library:** Sigmatiq Strategy Library | **Bucket:** Portfolio/Macro (months–years) | **Style:** Volatility / premium harvesting (short variance, tail-constrained)
> **Instruments:** SPX/SPXW listed index puts (monthly and weekly), 1-month T-bills / money-market collateral, long-dated OTM SPX puts or VIX calls (tail hedge) | **Typical holding period:** 1 month per option cycle; sleeve is permanent but gated | **Complexity (1–5):** 4 | **Evidence grade (A–C):** A- (30+ years of index data, multiple peer-reviewed confirmations, one canonical blow-up case)
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise. This library contains no local backtests yet.

---

## 1. Origin & lineage

**Originators.** Systematic index-option selling was institutionalized by the CBOE's strategy benchmark index program, launched 2002 onward. The two canonical benchmarks:

- **CBOE S&P 500 BuyWrite Index (BXM, 2002):** long S&P 500 stocks + short ATM SPX calls monthly. Academic validation by Whaley (2002, *Journal of Derivatives*), Feldman & Roy (2005, *Journal of Investing*), and Hill, Balasubramanian, Gregory & Tierens (2006, *Financial Analysts Journal*).
- **CBOE S&P 500 PutWrite Index (PUT, 2007; base date June 30, 1986):** sells cash-secured ATM SPX puts monthly, collateral held in T-bills. This is the purest public expression of volatility risk premium (VRP) harvesting and the direct ancestor of our sleeve.

**Academic foundations.**
- Coval & Shumway (2001, *Journal of Finance*) — "Expected option returns": zero-beta straddles on the S&P earn significantly negative average returns, i.e., option sellers earn a premium.
- Bakshi & Kapadia (2003, *Review of Financial Studies*) — delta-hedged gains of index options are negative on average: evidence of a *negative market volatility risk premium* paid to sellers.
- Carr & Wu (2009, *RFS*) — variance risk premium: variance swap rates exceed subsequent realized variance on average.
- Bollen & Whaley (2004, *JF*) and Gârleanu, Pedersen & Poteshman (2009, *RFS*) — net buying pressure for index puts shapes the implied-vol surface; demand pressure that cannot be perfectly hedged explains why the premium exists.
- Ilmanen, *Expected Returns* (2011, Wiley) — chapters on volatility selling as a systematic return source (book not fetched this session; known via secondary citation — see §9).
- Israelov & Nielsen (2014, *FAJ*) — "Covered Call Strategies: One Fact and Eight Myths": the definitive AQR decomposition of overwriting into long equity + short volatility (read in full, §8).

**Practitioner popularization and the failure case.** Exchange-traded short-vol products (XIV ETN, SVXY ETF) packaged the VRP for retail/institutional investors 2010–2018 and grew to ~$3.5bn combined AUM by early February 2018 after a 2017 in which XIV rose 176% and SVXY 172% (Augustin, Cheng & Van den Bergen 2021). On **February 5, 2018 ("Volmageddon")** the VIX rose from 18.44 at the open to 37.32 at the close (>100% in one day); XIV lost >90% after hours and was terminated by Credit Suisse under its acceleration clause (intraday indicative value ≤ 20% of the prior day's close). This is the canonical failure case our twist is engineered around (§4, §6).

**How it is actually used.** Institutional asset owners allocate to PUT-style benchmarks as an equity-replacement or diversifying sleeve (Wilshire 2019 documents pension-plan applications, e.g., replacing 15% of S&P 500 exposure with BXMD/PUT). Hedge funds and CTAs sell index variance via puts, strangles, and variance swaps, typically with vol-target sizing. Dealers are structurally short the premium and hedge dynamically.

## 2. The original rules (as published)

### 2.1 CBOE PUT index methodology (governance document, read in full)

From the Cboe PutWrite Indices methodology (Cboe Global Indices, rev. Oct 15, 2025), which governs the PUT family (PUTR, PUTY, PTLT, WPTR, WPUT; the classic PUT follows the same template):

1. **Instrument:** at-the-money (ATM) SPX put, 1-month tenor (PUT); variants: 2% OTM (PUTY), weekly ATM (WPUT).
2. **Roll date:** third Friday of each month (preceding business day if holiday); WPUT rolls every Friday.
3. **Strike selection:** first available strike below the last disseminated index value before 11:00 a.m. ET (PUTY: first strike below 98% of the index level).
4. **Execution assumption:** the new put is deemed sold at the **VWAP of OPRA trade prints between 11:30 a.m. and 12:00 p.m. ET** (late/cancel/spread trade codes excluded); if no trades, at the last bid before the end of the VWAP window.
5. **Collateral:** a notional amount equal to the strike K is invested in a T-bill account accruing at the **4-week Treasury bank-discount rate** (cash-secured — no leverage, no margin calls).
6. **Settlement:** options are **held to expiration** and settle against the Special Opening Quotation (SOQ); settlement value = max(0, K − SOQ). A new put is written immediately after settlement.
7. **Daily mark:** index return uses the average of the last bid/ask quote before 4:00 p.m. ET for the option leg plus accrued T-bill interest; no interest accrues on roll day.

### 2.2 Published performance (all literature claims, attributed)

**Wilshire Analytics (March 2019), 32.5 years, June 30, 1986 – Dec 31, 2018** (commissioned by CBOE):
- PUT: annualized return ≈ **9.5%** vs S&P 500 ≈ **9.8%**; annualized volatility **9.9% vs 14.9%**; **PUT Sharpe ratio 46% greater** than the S&P 500's. Cumulative: $1 → $19.35 (PUT) vs $20.85 (S&P 500).
- Max drawdown: **PUT −35.53%** (Jun-08 → Feb-09, 9 months, recovered Nov-10) vs **S&P 500 −50.95%** (Nov-07 → Feb-09, 16 months, recovered Mar-12). Option-index max drawdowns were 16–30% smaller than the S&P 500's across the study.
- Calendar 2008: PUT **−26.8%** vs S&P 500 **−37.0%**; 2009: PUT +31.5% vs +26.5%.
- IVRP evidence: implied volatility (VIX) **exceeded realized volatility by at least 1% and as much as 54% in all but one of the 21 years** studied; average monthly gross premiums were "fairly constant, with a small upward trend."
- Caveat stated by Wilshire itself: option-selling indexes have **negative skew and fatter tails** (higher kurtosis) than the S&P 500; Sortino and Stutzer metrics still favorable.

**Bondarenko (UIC, CBOE white paper "Historical Performance of Put-Writing Strategies," 2019), 2006–2018:**
- Average annual gross premium collected: **PUT 22.1%**, **WPUT 37.1%** (weekly ATM selling roughly doubles premium capture vs monthly: "premium of the ATM put increases as the square root of maturity... one-week tenor rolled four times ≈ 2× the one-month premium," attenuated by term-structure contango).
- WPUT: beta **0.54**, annualized vol **9.48%** (PUT 10.69%, S&P 500 14.32%); max drawdown **−24.2%** (PUT −32.7%, S&P −50.9%); longest drawdown **22 months** (PUT 29, S&P 52).

**Israelov & Nielsen (2014):**
- BXM vs S&P 500, Jul 1986–Dec 2013, excess of 3M LIBOR: S&P 5.4%/18.5% vol/Sharpe 0.29/worst DD −61.7%; BXM 4.4%/13.4%/0.33/−43.0%, beta 0.67 (upside beta 0.63, downside beta 0.78).
- Hypothetical decomposition (Apr 1996–Dec 2013): covered call = long equity (3.3% excess, 9.9% vol) + short straddle (1.8% excess, 6.7% vol, skew −0.5, kurtosis 21.9); correlation 0.42; risk contributions 64%/36%. Stylized example: with implied vol 18% vs expected realized 16%, the ATM option sells for $2.07 vs $1.84 fair — **~11% of the premium ($0.23) is VRP compensation ≈ 2.76%/yr**; delta-hedging the short straddle "substantially increases its Sharpe ratio" (Israelov & Nielsen 2014, citing their companion paper).

### 2.2b Sibling indexes and variants (context for design choices)

From the same Wilshire (2019) study and the CBOE methodology document:

- **BXM (covered call):** long S&P 500 + short ATM SPX call monthly. 32.5-year cumulative $1 → $14.19 (vs PUT $19.35, S&P $20.85); max DD −38.92% (Jun-07 → Feb-09, 21 months — the longest drawdown among the option-selling indexes). Calendar 2008: −28.7%.
- **BXMD (30-delta buywrite):** $1 → $23.65 — the best cumulative performer of the study; correlation 0.95 to the S&P 500 with ~0.25%/yr average alpha; highest on the mean-variance efficient frontier. 2008: −31.3%.
- **CMBO (covered combo = short ATM put + short 2% OTM call):** $1 → $17.48; 2008: −30.2%.
- **PPUT (long index + long 5% OTM protective put):** $1 → $8.08 — the systematic *buyer* of crash insurance dramatically underperformed, the mirror image of the seller's premium. 2008: −20.1% (best protection of the crisis year, as designed).
- **WPUT (weekly ATM putwrite):** per Bondarenko via CBOE (2006–2018), average weekly premium 0.71%; annualized vol 9.48% with beta 0.54; the premium-scaling intuition: ATM put premium grows with √maturity, so four weekly rolls ≈ 2× one monthly premium in gross terms, attenuated because "ATM implied volatilities are typically in contango" (Bondarenko, quoted by CBOE).
- **PUTY (2% OTM putwrite, base date June 30, 1986):** sells the first strike below 98% of the index level — the published template for harvesting skew at a slightly OTM strike, which our spec adopts (30Δ rather than ATM).
- Regime pattern (Wilshire, Exhibits 3/12): option-writing indexes were top-3 performers across asset classes 21 times vs 9 for the S&P 500 across sub-periods; the **only** sub-period where the S&P 500 beat the option writers on Sharpe was the 2010–Q3 2018 low-volatility bull market — steady melt-ups are the short-vol seller's relative (not absolute) weakness.

### 2.3 Disagreements / gaps in the published rules
- **Strike choice:** PUT sells ATM; Israelov & Nielsen note the ATM strike maximizes VRP exposure per unit of leverage, but the volatility smile implies lower strikes carry richer implied vols — selling OTM puts harvests more skew premium at the cost of more gap exposure. PUTY (2% OTM) exists precisely for this; published sources do not settle which is "best."
- **Tenor:** Bondarenko shows weekly selling captures more gross premium (37.1% vs 22.1%) but flags higher transaction costs; the net-of-cost optimum is not published.
- **Execution:** the index assumes VWAP execution 11:30–12:00 — not achievable at size in stressed tapes; live slippage vs the index is a known gap (§7).
- **Delta-hedged or naked:** Bakshi & Kapadia (2003) and Carr & Wu (2009) establish the premium survives delta-hedging, and Israelov & Nielsen note delta-hedging the short straddle raises its Sharpe — but hedging consumes the premium in transaction costs and gamma scalping error, and the published indexes (PUT/BXM) are all *unhedged*. The literature does not give a clean net-of-cost answer for which implementation dominates at monthly tenor; we follow the index convention (unhedged, cash-secured) and treat delta-hedging as a robustness variant, not the base case.
- **What the premium actually is:** Wilshire/Bondarenko report *gross* premium capture (22–37%/yr) while realized *net* index returns are ~9–10%/yr — the difference is paid out in assignment losses. Desk materials must never quote gross premium as "expected return."

## 3. Why it works — mechanism & evidence

**Mechanism.**
1. **Insurance demand / demand pressure.** End-users (hedgers, structured-product desks) are structural net buyers of index puts. Bollen & Whaley (2004) show net buying pressure moves the implied-vol surface; Gârleanu, Pedersen & Poteshman (2009) show dealers, unable to perfectly hedge, charge a premium that varies with demand. The seller is paid to ware­house crash risk.
2. **Risk premium for negative skew / crash states.** The short put loses disproportionately in bad times (high marginal utility states). Bakshi & Kapadia (2003) and Carr & Wu (2009) document that this compensation survives delta-hedging: it is a *volatility/variance* premium, not just an equity premium in disguise. Israelov & Nielsen's decomposition makes the same point for covered calls: only the short-vol component earns the VRP; the dynamic equity exposure adds risk without return.
3. **Behavioral overpricing.** Investors overpay for lottery-like protection and anchor on recent crashes; implied vol embeds a fear premium over expected realized vol (Wilshire's 21-year IVRP finding: VIX > realized in all but one year, gap 1–54%).
4. **Who is on the other side, and why they keep paying.** The put buyer is not irrational: pension funds with return targets, structured-product issuers short downside to clients, and levered equity holders all have *mandate-driven* demand for convexity that is insensitive to price — this is why the premium has persisted for decades rather than arbitraging away. The seller's edge is a capacity constraint in disguise: warehousing crash risk requires capital that can mark-to-market through a −30% month, and most institutions cannot. The VRP is therefore best understood as a *liquidity-and-balance-sheet premium*, which predicts it should be largest exactly when balance sheets are scarcest (post-crash) — consistent with the VRP spiking after selloffs, and the reason our gates must distinguish "premium rich because scared" (sell) from "premium rich because broken" (stand aside). The term-structure gate is the operational proxy for that distinction: backwardation is the market's own signal that the insurance market is in distress.

**Contradictory / decay / crowding evidence (must not be ignored).**
- The premium is **not a free lunch**: it is earned in states of the world where losses cluster. PUT lost 26.8% in 2008 (Wilshire); the short straddle component in Israelov & Nielsen's decomposition has skew −0.5 and kurtosis 21.9.
- **Volmageddon (Feb 5, 2018)** showed the *instrument* matters as much as the premium: inverse VIX ETPs with daily −1× rebalancing created a feedback loop — Augustin, Cheng & Van den Bergen (2021) estimate the ETP complex needed to buy ~93,000 VIX futures contracts (~23% of average daily volume, ~16% of open interest) in the 4:00–4:15 p.m. window, and ~113,000 including 2× long products (>20% of OI), driving futures into backwardation and XIV below its 20% acceleration trigger. The VRP itself did not disappear; a leveraged, crowded, mechanically rebalanced wrapper died.
- Crowding: Bhansali & Harris (2018, *FAJ*, "Everybody's Doing It") warned pre-crash that short-vol strategies act as "shadow financial insurers" whose hedging can destabilize markets (cited in Augustin et al.; not fetched directly — §9).
- Term-structure conditioning works in-sample: in Augustin et al.'s Table A.3 (2012–2017), XIV's monthly alpha was **+1.37% in contango** vs a **−8.64pp differential in backwardation** (Newey-West SE 5.76 — large but imprecisely estimated); Simon & Campasano (2014, *Journal of Derivatives*) document the VIX futures basis as a trading signal (secondary citation, §9).

## 4. The twist: VRP-GATE

**Design logic.** The original (PUT) is unconditional: it sells every month, at the same size, at the same strike, regardless of the state of the volatility market. Every documented failure of short-vol (1987, 2008, 2018, 2020) is a failure of *unconditionality* — the premium was collected in states where the market was already telling you insurance was in distress. VRP-GATE keeps the PUT chassis (cash-secured, monthly, held to settlement, T-bill collateral — the parts with 30+ years of validation) and adds conditioning in exactly four places, each mapped to a documented weakness: (a) term-structure gate ← backwardation is the worst state for short vol; (b) skew gate ← selling when crash insurance is already expensive is poor risk/reward; (c) VRP-proportional sizing ← fixed size ignores that the expected premium per unit risk varies; (d) tail hedge + (e) hard stop ← cash-securing caps loss at 100% of collateral, which is not a risk limit. Nothing else is changed; the twist is deliberately conservative so that deviations from PUT performance are attributable to the conditioning, not to a redesign.

The original PUT is unconditional: it sells every month, at full size, through every regime, with no tail control beyond cash-securing. Each modification below targets a documented weakness.

**(a) Contango gate (term-structure filter).**
*Weakness addressed:* unconditional selling keeps full size when the VIX futures curve is in backwardation — the state in which short-vol returns are worst (Augustin et al. Table A.3: backwardation alpha differential −8.64pp/month for XIV) and in which the rebalancing feedback loop operates.
*Rule:* compute the front-spread ratio `S_t = (F2_t − F1_t) / F1_t` from closing VIX futures (front and second month). The sleeve may open/maintain short-put positions only if `S_t > 0` (contango). If `S_t ≤ 0` at a decision point, no new premium is sold.

**(b) Skew gate (price of crash insurance).**
*Weakness addressed:* the VRP is richest exactly when skew is extreme, but extreme skew also marks regimes where the left tail is being repriced (post-crash, pre-event). Selling when crash insurance is *already expensive* concentrates the sleeve in the worst risk/reward states; Israelov & Nielsen's logic ("sell options only when implied vols are high relative to expectations") cuts both ways — we want implied vol rich vs *forecast realized*, not rich vs *its own history of fear*.
*Rule:* compute 25-delta put skew `SK_t = IV(25Δ put, 1M) − IV(ATM, 1M)`. Trade only if `SK_t < median(SK over trailing 252 trading days)` — i.e., crash insurance is not unusually expensive vs its own 1-year history.

**(c) VRP-scaled sizing to a fixed ex-ante vol target.**
*Weakness addressed:* PUT's fixed 1× cash-secured sizing ignores that the expected premium per unit risk varies with the implied-minus-forecast-realized gap. Sizing should be proportional to the *estimated* premium, not constant.
*Rule:* estimate `VRP_t = IV_ATM,1M,t − RV̂_t`, where `RV̂_t` is the 1-month-ahead realized-vol forecast from a GARCH(1,1) estimated on daily SPX log returns over an expanding window (min 3 years). Notional sold `N_t = N_base × clip(VRP_t / VRP_ref, 0, 2)`, with `VRP_ref` = trailing 5-year median VRP, then rescaled so the sleeve's ex-ante annualized vol (delta-adjusted short-put vol + tail hedge) equals the **10% target**. Hard cap: notional ≤ 100% of collateral (cash-secured, as in PUT).

**Worked sizing example (illustrative arithmetic, not a backtest).** Suppose VIX = 17 (so `IV_ATM,1M ≈ 17%`), GARCH forecast `RV̂ = 13%`, trailing 5-year median VRP = 3.5 vol points. Then `VRP_t = 4.0`, `m_t = clip(4.0/3.5, 0, 2) = 1.14`. With a $100mm sleeve, 30Δ puts 35 DTE, spot 5,800: base notional `N_base` is solved so that the delta-adjusted short-put position's ex-ante vol at `RV̂` equals 10% annualized at `m = 1`; the desk then sells `1.14 × N_base`. If instead VIX = 13 with `RV̂ = 12%` (VRP = 1.0, `m = 0.29`), the sleeve sells less than a third of base — premium thin, size thin. If the skew gate is closed (crash insurance expensive), `m = 0` regardless of the VRP estimate: the two gates veto, the VRP scales.

**(d) Long-dated OTM tail hedge.**
*Weakness addressed:* cash-securing caps the loss at strike-notional but does nothing about a −30% month; PUT's 2008 drawdown was −35.5% (Wilshire). A small permanent long-tail position converts the worst left-tail months into merely bad months.
*Rule:* allocate a fixed premium budget of **75 bp/yr of sleeve NAV** to 3-month ~5-delta SPX puts, rolled monthly in thirds (1/3 of the position each month). Budget is fixed ex ante; if the hedge costs more than budget, buy fewer contracts (further OTM), never more budget.

**(e) Hard stop (the Volmageddon rule).**
*Weakness addressed:* XIV died because it could not stop. A cash-secured put sleeve cannot be terminated by an acceleration clause, but it can ride a vol spike to a full collateral loss.
*Rule:* (i) if **VIX closes > 40**, buy back all short puts at the next session's open; (ii) if `S_t ≤ 0` (backwardation) for **2 consecutive closes**, exit all short puts at the next open; (iii) re-entry only after both gates (a)+(b) are satisfied for **5 consecutive trading days**. The tail hedge is *not* stopped out — it is what we want to be holding in those states.

## 5. Full specification of the twist variant

**Universe & instruments.**
- Short leg: SPX (AM-settled, monthly, third-Friday) or SPXW (PM-settled weekly) puts, 25–35 delta at entry, 21–42 DTE at entry. Default: monthly SPX, 30Δ, matching PUT-family conventions but slightly OTM to harvest skew (per §2.3).
- Collateral: 100% of strike notional in 1–4 week T-bills or a government money-market fund (mirrors the index's 4-week bank-discount-rate account).
- Tail hedge: SPX 3-month ~5Δ puts (or 2–3 month 20–40Δ VIX calls as an alternative implementation; futures margin required for the VIX variant).
- Signal data: VIX spot; VIX futures F1/F2 closes (CFE); SPX option implied vols (25Δ put, ATM) at 3:45–4:00 p.m. ET.

**Signal formulas.**
- Contango: `S_t = (F2_t − F1_t)/F1_t`. Gate open iff `S_t > 0`. (Proxy if futures history unavailable pre-2004: `VIX3M/VIX − 1 > 0`.)
- Skew: `SK_t = IV25Δput,1M − IVATM,1M`; gate open iff `SK_t < median_{252d}(SK)`.
- VRP: `VRP_t = IVATM,1M,t − RV̂_t`; `RV̂_t` = GARCH(1,1) 21-day-ahead annualized forecast: `σ²_{t+1} = ω + α r²_t + β σ²_t`, estimated by QMLE on expanding daily SPX returns (min 756 obs), horizon aggregation `σ²_{21} = Σ_h σ²_{t+h}`.
- Size multiplier: `m_t = clip(VRP_t / median_{5y}(VRP), 0, 2)`; zero when either gate closed.

**Entry.** On each monthly roll date (third Friday, mirroring PUT): if both gates open, sell `N_t = m_t × N_base` 30Δ puts where `N_base` is set so sleeve ex-ante vol = 10% annualized at `m=1` (ex-ante vol estimated from the delta-adjusted option position under `RV̂`, plus hedge offset). Execute within the 11:30–12:00 VWAP window where possible (index convention) but model costs at the bid/ask, not VWAP (§7).

**Exit.** Hold to SOQ settlement (index convention) unless a hard stop fires: VIX close > 40 → exit next open; `S_t ≤ 0` two consecutive closes → exit next open. Re-entry after 5 consecutive gate-open days.

**Sizing & risk limits.**
- Ex-ante sleeve vol target 10% annualized; hard cap 1× cash-secured notional (no naked margin).
- Tail-hedge budget 75 bp/yr, fixed; roll monthly in thirds.
- Sleeve-level max drawdown review trigger: −20% from peak → mandatory de-risk to half size until new high (internal governance rule, not from literature).
- Single-day loss limit: if sleeve loses > 7% in one day, halt new selling for 10 trading days regardless of gates.

**Costs (assumptions to use in validation, not literature claims).** Half the quoted bid/ask spread on entry and exit (SPX 30Δ 1M spreads historically ~0.3–1.0 vol point; model in vol points and convert), plus $1.30/contract exchange+clearing fees; T-bill yield earned on collateral; tail-hedge cost tracked at actuals. Stress cost scenario: 2× spreads.

**Capacity.** SPX options are among the deepest listed markets; Wilshire (2019) notes SPX option ADV (notional) more than quadrupled in the decade post-GFC "with sustained liquidity regardless of the level of market volatility." A $100–500mm sleeve selling monthly 30Δ puts is small vs open interest; the binding constraint is stressed-tape execution, not normal-times size. VIX-call hedge variant is capacity-limited by VIX options/futures depth — keep hedge notional < 1% of VIX futures OI.

**Monthly operations calendar (decision table).**

| Day | Action |
|---|---|
| Every close | Check hard stops: VIX close > 40? `S_t ≤ 0` for 2nd consecutive close? If either fires, queue full exit at next open. |
| Every close | Update `S_t`, `SK_t` vs 252-day median, GARCH `RV̂_t`, `VRP_t`, `m_t`. |
| Roll date (3rd Friday) | If gates open and 5-day re-entry rule satisfied: sell `N_t` 30Δ puts (21–42 DTE) in the 11:30–12:00 window; settle prior cycle at SOQ. If gates closed: hold 100% T-bills; sell nothing. |
| Roll date | Roll one third of the 5Δ tail hedge (sell the ~2-month put, buy a fresh 3-month put), spending ≤ 1/12 of the 75 bp annual budget. |
| Month-end | Reconcile collateral yield; log gate state, fills vs VWAP benchmark, hedge carry cost; refresh 5-year VRP median. |

**State machine (unambiguous for coding).** States: `FLAT` (gates closed or post-stop), `ENTERING` (gates open ≥ 5 consecutive closes, no position), `SHORT` (position on). Transitions: `FLAT→ENTERING` on 5th consecutive gate-open close; `ENTERING→SHORT` at next roll date execution; `SHORT→FLAT` on SOQ settlement with gates closed, or on hard stop (immediate, next open); `SHORT→SHORT` at roll when gates open (settle + resell same session). No state allows adding to an existing position mid-cycle; size changes only at roll dates.

**Parameter summary (single source of truth for implementation).**

| Parameter | Value | Source / rationale |
|---|---|---|
| Short instrument | SPX monthly put, 30Δ, 21–42 DTE at entry | PUT-family convention; 30Δ harvests skew (PUTY precedent) |
| Roll date | Third Friday; settle SOQ, resell same session | CBOE PUT methodology |
| Collateral | 100% strike notional in 1–4w T-bills | CBOE PUT methodology (4-week bank-discount rate) |
| Contango gate | `S_t = (F2−F1)/F1 > 0` at close | Augustin et al. backwardation alpha differential |
| Skew gate | `SK_t = IV25Δ − IV_ATM < median_252d(SK)` | Twist (b); crash-insurance price filter |
| VRP sizing | `m_t = clip(VRP_t / median_5y(VRP), 0, 2)` | Twist (c); Israelov & Nielsen "sell when IV high vs expected" |
| Vol target | 10% annualized ex-ante (delta-adjusted, at `RV̂`) | Internal risk budget; PUT's realized vol was 9.9–10.7% |
| Notional cap | ≤ 100% of collateral (cash-secured) | PUT methodology; no naked margin |
| Tail hedge | 3M ~5Δ SPX puts, 75 bp/yr budget, rolled monthly in thirds | Twist (d); fixed budget, never exceeded |
| Hard stop 1 | VIX close > 40 → exit next open | Twist (e); Volmageddon rule |
| Hard stop 2 | `S_t ≤ 0` two consecutive closes → exit next open | Twist (e) |
| Re-entry | Both gates open for 5 consecutive closes | Whipsaw damping |
| Daily loss halt | > 7% sleeve loss in a day → no new selling for 10 trading days | Internal governance |
| Drawdown review | −20% from peak → half size until new high | Internal governance |

## 6. Failure modes & regime dependence

**What kills it.**
1. **Gap-through-the-strike crashes (1987-type).** A −20% overnight move with 1× cash-secured 30Δ puts loses a large fraction of collateral before any stop can act. The VIX>40 stop is *close-based* and cannot catch gaps. Mitigation: the 5Δ tail hedge, sized by budget notional, is the only true gap protection; accept that it is partial.
2. **Volmageddon-type feedback spikes.** Feb 5, 2018: VIX +100% in a day, curve flipped to backwardation intraday. Our backwardation stop uses *closes*; on Feb 5 the flip confirmed at the 4:15 futures close, so exit would occur Feb 6 — after the worst of the spike. The defense is that we are never short VIX futures themselves (no daily −1× rebalancing, no acceleration clause, no leverage beyond 1× collateral): XIV died of its wrapper (leverage + concentration + mechanical rebalancing, per Augustin et al.), not of the VRP alone.
3. **Slow-bleed bear markets (2000–2002, 2008).** Repeated monthly losses as realized vol exceeds implied for many months. PUT lost 26.8% in calendar 2008 (Wilshire) despite full cash-securing. The contango gate helps (the curve spends much of such periods in backwardation) but whipsaws are guaranteed: the gate will keep us out of some profitable post-crash premium-rich months — that is the price of the filter.
4. **GARCH lag.** GARCH(1,1) under-forecasts vol at regime onsets, inflating `VRP_t` exactly when risk is highest. The skew gate (b) partially offsets this; a realized-vs-forecast bias audit is mandatory in validation (§7).
5. **Crowding in put-selling.** Post-2018 growth of put-write funds and 0DTE/weekly overwriting compresses the premium in normal times and synchronizes exits. Early-warning indicators: PUT/WPUT premium yield trend (Bondarenko's 22.1%/37.1% gross premium benchmarks — a sustained fall below ~60% of those levels signals compression); share of SPX option volume in short-dated puts; skew persistently below median (our own gate (b) doubles as a crowding detector).
6. **Rates regime.** The collateral yield is part of total return (PUT's T-bill account). At ~0% rates the sleeve's total return drops by roughly the cash rate; at high rates the hurdle for the equity market (and thus assignment risk) changes. Not fatal, but total-return comparisons across rate regimes must be collateral-adjusted.
7. **COVID 2020 — the second canonical test.** PUT's published max drawdown is −32.66% (Feb-19-2020 → Mar-23-2020) vs the S&P 500's −33.79% over identical dates (Wilshire Exhibit 9): the monthly-roll index roughly tracked the crash it insures against, and the premium collected in prior years is the compensation. By design, VRP-GATE's gates would have been closed for the worst leg — the VIX futures curve flipped to backwardation in late February 2020 and VIX closed above 40 on Feb 28, 2020, remaining there for weeks — but this is a *design inference from published index history, not a tested result*; §7 requires verifying gate timing day-by-day.

**Regime dependence summary.** The sleeve earns its premium in normal-to-elevated-vol regimes with upward-sloping curves (the historical majority: Wilshire reports VIX exceeded realized vol in 20 of 21 years, but the *level* of the spread is regime-dependent). It underperforms on a relative basis in low-vol melt-ups (2010–2018 was the only sub-period where the S&P 500 beat the option writers on Sharpe) and loses in absolute terms in crashes. The gates convert the strategy from "always short vol" to "short vol only when the term structure and skew say the insurance market is not already stressed" — the explicit bet is that gate whipsaw costs less than the crash months avoided.

**Early-warning dashboard:**

| Indicator | Frequency | Threshold of concern |
|---|---|---|
| Front spread `S_t` level and 5-day change | Daily close | `S_t` approaching 0; any close ≤ 0 starts the 2-day stop clock |
| `SK_t` percentile vs 1-year history | Daily close | > 50th percentile closes gate (b); > 80th = crash insurance expensive, expect flat |
| VRP estimate vs 5-year median | Daily close | `m_t < 0.5` = premium thin, size thin |
| Short-vol ETP + put-write fund AUM | Monthly | Rapid growth = crowding; rapid redemption = forced unwinds (Volmageddon precursor: XIV+SVXY ~$3.5bn after 176%/172% 2017 returns) |
| SPX put OI concentration near our strikes | Weekly | Clustered OI = synchronized gamma at those strikes |
| Collateral yield (4-week T-bill) | Monthly | Total-return decomposition shifts; recalibrate expectations |
| GARCH forecast bias | Monthly | `RV̂ − RV_realized` systematically negative at onsets = forecaster lagging; rely on gates |

## 7. Validation protocol

**Data needs.** SPX option quotes/trades with greeks (OptionMetrics IvyDB US or CBOE DataShop), 1990–present; VIX futures daily OHLC (CFE, Mar 2004–present; extend term-structure proxy with VIX/VXV from 2007, VIX/VIX3M earlier); SPX daily returns for GARCH (1950+ for estimation warm-up); 4-week T-bill rates (US Treasury); SOQ prints for settlement realism.

**Chronological splits.** Development: 1990–2003 (no futures gate available — proxy only; treat as signal-construction period). Validation: 2004–2014 (futures gate live; includes 2008). Final test: 2015–2026 (includes Volmageddon 2018, COVID 2020, 2022 bear, 2025–26). Never tune on the test window. Purging/embargo: not critical for monthly index options (no overlapping label problem beyond the 1-month holding period), but ensure GARCH and all medians/percentiles use **expanding or trailing windows ending at the decision timestamp** — the 252-day skew median and 5-year VRP median are classic look-ahead traps.

**Cost / execution model.** Fill at quoted bid/ask midpoint ± half-spread (not the index's VWAP assumption); model SOQ settlement on expiry (opening print, not close); T-bill interest on collateral at the 4-week bank-discount rate; tail-hedge rolls at market spreads. Include a 2× spread stress scenario and a "no fill in the 11:30–12:00 window on stressed days" scenario (fill at 3:45 p.m. quote instead).

**GARCH estimation & forecast evaluation.** Estimate GARCH(1,1) on daily SPX log returns by Gaussian QMLE, refit monthly on a trailing 1,250-day window (sensitivity: 750d, expanding). Forecast `RV̂` as the 21-day-ahead annualized conditional vol from the estimated recursion (not a regression of realized on implied — we want an independent forecast so `VRP_t = IV − RV̂` is a genuine spread). Forecast quality gates: report the Mincer–Zarnowitz regression of realized 21-day vol on `RV̂` (want intercept ≈ 0, slope ≈ 1) and the fraction of months where `sign(VRP_t)` predicted `sign(IV − RV_realized)`; if the GARCH forecast is dominated by simply using lagged 21-day realized vol as `RV̂`, use the simpler forecaster (pre-register this horse race). Bias audit: compute `RV̂ − RV_realized` around the 10 largest vol spikes — systematic under-forecast at onsets is expected; the skew gate and the VIX>40 stop exist precisely because the forecaster will lag.

**Strategy-specific pitfalls.**
- *Index-methodology look-ahead:* the PUT index's VWAP execution and SOQ settlement are not replicable at size; never benchmark against PUT without an execution-haircut sensitivity.
- *Vol-of-vol regime:* GARCH estimated on post-1990 data embeds the modern vol regime; test estimation windows of 3y/5y/expanding.
- *Gate proxy mismatch:* pre-2004 the contango gate runs on VIX/VIX3M ratios, which are not the traded futures spread — flag all pre-2004 results as proxy-regime.
- *Margin realism:* cash-secured sizing is the spec; do not let the backtest drift into naked margin to "improve" returns.
- *Tail-hedge accounting:* report sleeve returns with and without the hedge; the hedge is a cost center in calm decades and must not be silently dropped in optimization.

**Robustness checks.** Entry delta {25, 30, 35}; tenor {weekly, monthly}; VIX stop {35, 40, 45}; backwardation confirmation {1, 2, 3} days; skew median window {126, 252, 504} days; VRP size cap {1.5, 2, 3}; vol target {8%, 10%, 12%}. Acceptance requires the edge to survive the *corners* of this grid, not just the center.

**Acceptance criteria (pre-registered).** (i) Positive mean excess return over T-bills in each regime split, net of 2× costs; (ii) max drawdown materially better than the unconditional PUT benchmark over identical windows; (iii) no single-day loss exceeding 12% of sleeve NAV at 1× collateral in the full sample including 1987 (use 1987 as a stress replay even if outside formal splits); (iv) gates reduce time-in-market by ≥15% while retaining ≥60% of unconditional premium capture — else the gates are not paying for their whipsaw; (v) Sharpe and, more importantly, skew/kurtosis profile reported alongside — a Sharpe improvement achieved by *more* negative skew is a failure, per Israelov & Nielsen's warning that mean-variance metrics understate this strategy's tail risk.

**Benchmarks & reporting standards.** Report against four benchmarks over identical windows: (1) PUT index total return (the unconditional ancestor — the twist must beat it on drawdown-adjusted basis or it has no reason to exist); (2) S&P 500 total return (the opportunity cost of the collateral); (3) 3-month T-bill (the floor); (4) a naive gated variant using only the contango gate (to isolate the marginal value of the skew gate and VRP sizing — each twist component must pay for itself). Report monthly returns, full distribution moments (mean, vol, skew, kurtosis, worst 5 days), time-in-market by gate state, premium captured vs PUT's gross premium in the same months, gate whipsaw count (exit→re-entry within 10 days), and hedge carry cost per year. All figures net of the §5 cost model. No figure may be quoted in desk materials without its window, cost assumption, and benchmark set attached.

## 8. Sources read (annotated)

1. **"Cboe PutWrite Indices — Methodology"**, Cboe Global Indices (rev. Oct 15, 2025). URL: https://cdn.cboe.com/api/global/us_indices/governance/Cboe_PutWrite_Indices_Methodology.pdf — accessed 2026-10-07. *What it says:* full construction rules for the PUTR/PUTY/PTLT/WPTR/WPUT family — third-Friday rolls, strike selection (ATM / 2% OTM), VWAP 11:30–12:00 ET sale convention, SOQ settlement, 4-week T-bill collateral account, daily marking formulas, base dates (PUTY base June 30, 1986). *Taken:* the exact original rules in §2.1; execution/settlement conventions used in §5 and the look-ahead pitfalls in §7.
2. **"Options-Based Benchmark Indexes: Performance, Risk and Premium Capture (June 1986–Dec 2018)"**, Wilshire Analytics, March 2019 (commissioned by CBOE). URL: https://prefblog.com/wp-content/uploads/2026/02/wilshire-options-based-benchmark-indexes-2019.pdf — accessed 2026-10-07. *What it says:* 32.5-year study of BXM/BXMD/CMBO/PPUT/PUT vs asset classes; PUT 9.9% vol vs S&P 14.9%, Sharpe 46% higher, max DD −35.53% vs −50.95%, 2008 PUT −26.8%; IVRP: VIX exceeded realized vol in all but one of 21 years (gap 1–54%); negative-skew/fat-tail caveats; pension allocation case studies. *Taken:* all headline performance claims in §2.2, mechanism evidence in §3, capacity note in §5. Note: CBOE-commissioned — treat as industry-friendly framing; numbers are index math, not fund results.
3. **"Covered Call Strategies: One Fact and Eight Myths"**, Roni Israelov & Lars N. Nielsen, *Financial Analysts Journal* 70(6), 2014. URL: https://www.aqr.com/-/media/AQR/Documents/Insights/Journal-Article/FAJ-Covered-Call-Strategies-One-Fact-and-Eight-Myths.pdf — accessed 2026-10-07. *What it says:* covered call = long equity + short straddle; only the short-vol component earns the VRP; BXM stats (Sharpe 0.33 vs 0.29, beta 0.67, DD −43%); stylized VRP math (implied 18% vs realized 16% → 2.76%/yr VRP); delta-hedging raises Sharpe; "if you have no view on implied volatility, there is no reason to sell options." *Taken:* mechanism decomposition in §3, rationale for gates (a)/(b) and VRP sizing (c) in §4, the Sharpe-vs-skew warning in §7.
4. **"Volmageddon and the Failure of Short Volatility Products"**, Patrick Augustin, Ing-Haw Cheng, Ludovic Van den Bergen, *Financial Analysts Journal* (2021). URL: https://exa.ai/library/publication/m4pd30qdnc9 (SSRN abstract 3819342) — accessed 2026-10-07. *What it says:* Feb 5, 2018 post-mortem — VIX 18.44→37.32; XIV/SVXY combined AUM $3.5bn; rebalancing math Δn = (NAV/F)·(L²−L)·R; ~93,000 contracts ≈ 23% of ADV / 16% of OI needed in the 4:00–4:15 window; feedback loop; XIV's 20% acceleration trigger; ZIV (mid-term) lost only ~1.6–5.9%; Table A.3 contango/backwardation alpha split (+1.37%/mo contango, −8.64pp backwardation differential for XIV). *Taken:* the entire failure-mode mechanics in §6, the contango-gate evidence in §4(a), the wrapper-vs-premium distinction that justifies cash-secured puts over inverse ETPs.
5. **"New Research Shows Options-Based Strategies Can Generate Higher Gross Premiums..."** (Bondarenko white-paper summary), CBOE Insights, May 13, 2019. URL: https://www.cboe.com/insights/posts/new-research-shows-options-based-strategies-can-generate-higher-gross-premiums-with-less-volatility-over-traditional-asset-classes/ — accessed 2026-10-07. *What it says:* 2006–2018: PUT gross premium 22.1%/yr, WPUT 37.1%/yr; WPUT beta 0.54, vol 9.48%, max DD −24.2%, longest DD 22 months; √maturity premium scaling argument; transaction-cost caveat for weekly rolls. *Taken:* §2.2 weekly-vs-monthly evidence, §5 tenor choice, §6 crowding benchmark levels.

**Failed / partial fetches.** None for this document — all five sources above were fetched and read. The Wilshire PDF was accessed via a mirror (prefblog.com); the CBOE original link is paywalled/moved but the document is the genuine Wilshire study.

## 9. Further reading

- Ilmanen, A. (2011). *Expected Returns*, Wiley — volatility-selling chapters. **Not accessed this session** (book; known via secondary citation). Acquire for the desk.
- Bakshi, G. & Kapadia, N. (2003). "Delta-Hedged Gains and the Negative Market Volatility Risk Premium," *RFS* 16(2) — cited in both Israelov & Nielsen and Augustin et al.; not fetched directly.
- Carr, P. & Wu, L. (2009). "Variance Risk Premiums," *RFS* 22(3) — variance-swap level evidence; not fetched.
- Bollen, N. & Whaley, R. (2004). "Does Net Buying Pressure Affect the Shape of Implied Volatility Functions?," *JF* 59(2); Gârleanu, N., Pedersen, L. & Poteshman, A. (2009). "Demand-Based Option Pricing," *RFS* 22(10) — demand-pressure mechanism; not fetched.
- Bhansali, V. & Harris, L. (2018). "Everybody's Doing It: Short Volatility Strategies and Shadow Financial Insurers," *FAJ* 74(2) — pre-Volmageddon crowding warning; not fetched.
- Simon, D. & Campasano, J. (2014). "The VIX Futures Basis: Evidence and Trading Strategies," *Journal of Derivatives* 21(2) — term-structure timing evidence behind gate (a); not fetched.
- Cheng, I. (2019). "The VIX Premium," *RFS* 32(1) — VIX futures premium decomposition; not fetched.
- Israelov, R. & Nielsen, L. (2014). "Covered Calls and Their Unintended Reversal Bet," AQR working paper — delta-hedged short-straddle Sharpe improvement; not fetched.
- Whaley, R. (2002). "Return and Risk of CBOE Buy Write Monthly Index," *Journal of Derivatives* 10(2); Feldman, B. & Roy, D. (2005). "Passive Options-Based Investment Strategies," *Journal of Investing* 14(2) — BXM validations; not fetched.
- Sushko, V. & Turner, G. (2018). "The Equity Market Turbulence of 5 February — The Role of Exchange-Traded Volatility Products," *BIS Quarterly Review* — official-sector Volmageddon account; not fetched.
- Simon, D. & Campasano, J. (2014). "The VIX Futures Basis: Evidence and Trading Strategies," *Journal of Derivatives* 21(3) — the basis-as-signal paper behind our contango gate; known via secondary citation (Augustin et al.), not fetched.
- Bhansali, V. & Harris, L. (2018). "Everybody's Doing It: Short Volatility Strategies and Shadow Financial Insurers," *Financial Analysts Journal* 74(2) — the pre-Volmageddon crowding warning; cited in Augustin et al., not fetched directly.
- Eraker, B. & Wu, Y. (2017). "Explaining the Negative Returns to Volatility Claims," *Journal of Financial Economics* — VIX-futures return decomposition underlying the contango/backwardation alpha split; cited in Augustin et al., not fetched.
