# 28. FX Carry (G10 + EM Select) — Twist: CARRY-F

> **Library:** Sigmatiq Strategy Library V2 | **Bucket:** Portfolio / Macro | **Style:** Carry
> **Instruments:** G10 + liquid EM FX forwards/futures | **Typical holding period:** 1–6 months | **Complexity (1–5):** 4 | **Evidence grade (A–C):** B+
> **Status:** Research document. All performance figures are literature claims attributed to their authors — NOT our backtest results — unless explicitly marked otherwise.

## 1. Origin & lineage

**Bank-desk lineage.** Bill Lipschutz (Salomon FX, 1980s) → Deutsche/Citi carry desks → academic canon: Lustig–Roussanov–Verdelhan carry factor; Burnside et al.; Brunnermeier–Nagel–Pedersen crash-risk framing; Jurek downside-hedged carry. Practitioner standard: long high-yield / short low-yield baskets, vol-scaled, with crash-hedge wings. Our twist is hedged carry, not naive high-yield chasing.

## 2. The original rules (as published)

- **Naive:** rank by 1M forward discount (interest differential); long top tercile, short bottom; monthly rebalance; equal-weight.
- **LRV factor:** high-minus-low carry portfolio (dollar-neutral construction variants).
- **Jurek:** crash-hedged carry via OTM FX puts (cuts left tail at insurance cost).
- **What varies:** G10-only vs EM-included, dollar-neutral vs dollar-allowed, hedge ratio.

## 3. Why it works — mechanism & evidence

**Mechanism.** Uncovered interest parity fails on average (forward-rate bias/Fama puzzle): high-yield currencies do not depreciate enough to erase the rate gap — risk-premium (crash/liquidity compensation) plus slow-moving capital plus central-bank smoothing sustain it until risk-off unwinds it violently.

**Supporting evidence (all attributed, none ours):**

- LRV and successors document positive carry-factor premia across decades/currencies (authors' samples; EM inclusion lifts mean and tail).
- Jurek reports hedged carry retains much of the mean with far smaller left tails (author's construction).
- Bank-desk lore + BIS turnover data confirm carry crowding into low-vol regimes (consistent).

**Contradictory / decay evidence:**

- 2008 (JPY-funded unwind), 2015 CHF shock, 2020 March: carry crashes erase years in weeks — the defining risk.
- Post-GFC rate compression thinned G10 differentials; naive G10 carry Sharpe roughly halved vs 1990s–2000s.
- Transaction-cost + forward-point realities cut retail carry vs paper (wide EM spreads).

**Synthesis.** Carry is a compensated crash-risk premium: harvest it diversified and hedged, sized by vol, never as concentrated EM high-yield bets.

## 4. The twist: CARRY-F

1. **Hedged carry (targets crash wipeouts):** every carry unit paired with 25-delta OTM crash-put wing (Jurek-style); hedge budget 15–25% of carry accrual.
2. **Vol-scaled pairs (targets fixed-weight blowups):** size each pair by 1/realized-3M-vol with 2% book-vol target; no static notionals.
3. **Rate-momentum filter (targets cutting-cycle traps):** require hiking/on-hold central-bank stance for longs (no longs into active cutting cycles, however high the trailing yield).
4. **Dollar-regime gate (targets broad-dollar trends):** halve carry when DXY 3M trend is one-sided (|z|>2) — carry dies in dollar juggernauts.
5. **EM-concentration cap (targets EM crises):** EM max 40% of carry risk; single EM max 10%; liquidity veto (bid-ask > 20 bps = excluded).

## 5. Full specification of the twist variant

**Universe.** G10 + 8 liquid EM (MXN, BRL, ZAR, KRW, SGD, PLN, CZK, INR NDF where allowed); forwards/futures; no pegged/frontier.

**Data requirements.** FX forwards/swaps (differentials), spot daily, central-bank calendar/stance tags, DXY trend, options wings for hedge legs, liquidity screen.

**Signal definitions (formulas).**

- Carry rank by 1M forward discount; vol-scale 1/sigma_3M; stance filter; DXY gate; EM caps.

**Entries.**

Monthly rebalance into hedged carry units; wings attached same ticket; liquidity veto applied pre-entry.

**Exits.**

Monthly rotation; hedge wings rolled on schedule; DXY-gate halves managed at next close (sole intra-month action).

**Position sizing.**

2% book-vol target; pair caps by vol-scale; EM caps as above.

**Risk limits.**

Hedge-always; DXY halt-halving; EM caps; weekend/event hold accepted via size (no weekend leverage-up).

**Cost model & capacity.**

Forward points + spreads (EM wider) + wing premia 15–25% of accrual; capacity institutional in G10, moderate in EM.

**Parameters to validate (plateau, not peak):** Rank {tercile, quintile}; vol window {1M, 3M, 6M}; hedge {10, 25 delta}; DXY z {1.5, 2.0, 2.5}.

## 6. Failure modes & regime dependence

Risk-off unwinds (all high-yield falls together); peg breaks/EM devals through wings; dollar-trend regimes; cutting-cycle longs (rate trap).

## 7. Validation protocol

**Status: no local backtest exists yet.** This library contains zero proprietary results; everything above is literature.

- **Data:** FX spot/forward 1995–present; central-bank dates; DXY; EM liquidity history; costs per era.
- **Splits:** chronological across cycles (must include 2008, 2020, 2022); no random k-fold; walk-forward anchored.
- **Cost/slippage model:** ETF expense + 2–10 bps/rebalance; options spreads + borrow where used; futures roll costs; stress 2x/3x.
- **Pitfalls:** look-ahead in index/constituent vintages; survivorship; same-bar ambiguity on rotation days; corporate actions; options expiry/pin.
- **Robustness:** plateau heatmaps; bootstrap CIs; placebo allocations (~zero edge); yearly + VIX/inflation-regime sub-samples; best-year removal.
- **Acceptance criteria:** OOS risk-adjusted dominance vs stated benchmark net of 2x costs; max DD within 1.2x of in-sample; positive in >= 60% of 3-year windows.

## 8. Sources read (annotated)

1. **Lustig, Roussanov & Verdelhan on the carry factor.** Journals — high-minus-low premia. Known via secondary citation.
2. **Jurek on crash-hedged carry.** Search "Crash-neutral currency carry trades" — OTM-hedge construction. Known via secondary citation.
3. **Brunnermeier, Nagel & Pedersen on carry crashes.** Search "Carry Trades and Currency Crashes" — crash-risk framing. Known via secondary citation.

## 9. Further reading

- BIS FX turnover/crowding notes.
- Lipschutz interviews (desk risk philosophy).
- EM deval case studies (1997/2015/2018).
