# D2. Cross-sectional (relative-strength) momentum

Status: research dossier, not investment advice. Research date: 2026-10-07. Labels: [PR] peer-reviewed, [WP] working paper, [PC] practitioner claim, [UNV] unverified. TWIST sections are hypotheses I have NOT backtested.

## 1. Summary, horizon, asset class, holding period

Cross-sectional momentum ranks securities (classically US stocks) by past return over about 12 months excluding the most recent month ("12-1"), buys the top decile/quintile and shorts the bottom, and holds for about 1-6 months with monthly rebalancing. It is market-neutral by construction. Horizon: medium term (months). Asset class: individual equities first; the same logic is applied to country indices, currencies, commodities and bonds. It is one of the most replicated anomalies in finance, but with three honest caveats: it has deep, rare crashes; it is high turnover and shorting-heavy; and a large part of the gross premium is sensitive to implementation (size, shorting costs, rebalancing rule).

## 2. Origin and who uses it

- Jegadeesh and Titman (1993), "Returns to Buying Winners and Selling Losers", Journal of Finance [PR]. Sample: NYSE/AMEX stocks, 1965-1989.
- Carhart (1997) added the momentum factor (UMD/WML) to the Fama-French model to evaluate mutual funds [PR; I did not fetch the paper, cited from memory].
- Asness (1994 thesis) and Asness, Moskowitz, Pedersen (2013), "Value and Momentum Everywhere", J. Finance [PR].
- Daniel and Moskowitz (2016), "Momentum Crashes", J. Financial Economics 122 [PR].
- Blitz, Huij and Martens (2011), "Residual Momentum", J. Empirical Finance 18 [PR].
- Users: quant equity funds (AQR, Robeco/Blitz's group, many multi-factor managers), index providers (MSCI/S&P momentum indices), and factor ETFs [PC].

## 3. Economic rationale and the other side

Competing explanations (unresolved):
- Behavioral under-reaction to news, slow diffusion, disposition effect, herding and later over-reaction (Jegadeesh-Titman discuss under-reaction/delayed reaction as the interpretation of their profits) [PR].
- Risk-based: time-varying exposures to market and size/value factors; the Daniel-Moskowitz result that losers behave like call options in panic rebounds supports a conditional-risk story, but the authors report that hedging the option-like exposure with variance swaps did not restore profits in bear markets [PR].
- Limits to arbitrage: short-side costs, funding-liquidity risk (Asness-Moskowitz-Pedersen link value and momentum to funding liquidity) [PR].

Counterparties: investors who sell winners early (disposition effect), contrarian/value traders, and liquidity-constrained shorts forced to cover in rebounds.

## 4. Canonical rules

1. Universe: US common stocks on NYSE/AMEX/NASDAQ; exclude price below a floor (commonly $5 or the bottom NYSE size decile, practitioner convention [PC]).
2. Signal: cumulative return from t-12 to t-2 months (12-1). Jegadeesh-Titman's original strategies use formation periods J and holding periods K in {3, 6, 9, 12} months, and compare versions that skip a week between formation and holding to avoid bid-ask bounce and short-term reversal.
3. Portfolio: top decile (winners) minus bottom decile (losers); equal- or value-weighted. Overlapping K-month holding portfolios rebalanced monthly.
4. Output: long-short WML (or UMD) factor.
Alternative implementations to compare: skip-month vs not; residual (factor-adjusted) returns; industry-adjusted returns; 12-7 "intermediate" lookback (Novy-Marx; I did not read this paper, [UNV]).

## 5. Evidence

| Claim | Source (read?) | Sample | Costs | Grade |
|---|---|---|---|---|
| Best strategy (12-month formation, 3-month hold) earned about 1.3% per month, about 1.5% per month with a one-week gap; all 32 variants positive, nearly all significant; about 1% per month for most variants | Jegadeesh-Titman 1993 (read primary) | NYSE/AMEX, Jan 1965-Dec 1989 | Gross; the paper does not net out realistic trading costs | PR |
| Momentum robust out-of-sample: WML 1927-2013 Sharpe about 0.5; spread of winners over losers averaged 8.3%/year vs 4.7% value and 2.9% size | Asness-Frazzini-Israel-Moskowitz, "Fact, Fiction, and Momentum Investing", JPM 2014 (read primary) | 1927-2013; also 1963-2013 and 1991-2013 | Gross for factor data; for costs they cite their own real-trade study | PC/PR hybrid, authors are AQR principals and defend the factor |
| Momentum survives costs: Frazzini-Israel-Moskowitz trading-cost study using over a trillion dollars of live AQR trades | cited in Fact/Fiction (the study itself not read) | 1998-2013, 19 developed markets | Real execution costs, patient trading, tracking error allowed | PC (conflict of interest: study of own trading) |
| 1991-2013 Sharpe: small caps 0.45 vs large caps 0.24; authors argue the size difference is sample-specific | Fact/Fiction | 1991-2013 | Gross | PC |
| Momentum crashes: worst months July-August 1932 (losers +232%, winners +32% over the two months); March-May 2009 (losers +163%, winners +8%) | Daniel-Moskowitz (read NBER WP) | 1927-2013 | Gross | PR |
| Static WML: annualized excess return about 17.9%, vol about 30%, monthly skew -4.7; momentum portfolio beta -0.58; text states Sharpe 0.71 but the table column reads 0.60 (the extracted draft is inconsistent; assume 0.6-0.7) | Daniel-Moskowitz | 1927-2013 | Gross | PR |
| Dynamic variance-scaled momentum "approximately doubles" alpha and Sharpe of static; across markets/assets Sharpe 1.18 | Daniel-Moskowitz | 1927-2013 and international | Gross | PR; in-sample estimation caveat, authors use ex-ante forecasts |
| Residual momentum: risk-adjusted profits about twice total-return momentum, more consistent, less dependent on extreme stocks | Blitz-Huij-Martens abstract (primary body not read) | sample not verified (abstract only) | Not read | PR (abstract only) |
| Value and momentum: negatively correlated across asset classes; combined portfolio Sharpe higher than either | Asness-Moskowitz-Pedersen 2013 (primary text searched, not fully read) | multiple markets 1972-2011 | Gross | PR |
| Multiple-testing hurdle: new factors need t-ratios above about 3.0, not 2.0 | Harvey-Liu-Zhu, "...and the Cross-Section of Expected Returns" (read abstract/introduction) | n/a | n/a | PR |

Critical assessment:
- Original Jegadeesh-Titman profits are gross. Academic momentum portfolios are high turnover (monthly recomputation of extremes) and short the most volatile, most expensive-to-borrow stocks. Whether the net premium survives is contested; the strongest "yes" comes from authors who run such strategies (AQR). Treat net-of-cost claims as unverified until reproduced with your own execution costs and borrow fees.
- Post-publication: the AQR defence points to positive out-of-sample results in 1991-2013 (the post-JT/Asness period). I have not read primary data for 2014-2025 in this dossier; recent decades include sharp momentum reversals (2009; periods like Nov 2020) that I could not source here, so the post-2013 record is [UNV].
- The long-run Sharpe of roughly 0.5-0.7 for a single-factor L/S with -4.7 monthly skewness and 30% vol means drawdowns of decades-scale in terms of recovery (1932-1939 and 2009-2013 identified by Daniel-Moskowitz as the two largest underperformance stretches).
- The "momentum works equally on the short side and in large caps" claim of Fact/Fiction is plausible but comes from a defender; independent replication is advisable.

## 6. Failure regimes and risks

- Panic rebounds: after market declines with high volatility, past losers (high beta, option-like) surge and the short leg is crushed (Daniel-Moskowitz) [PR].
- Time-varying beta: WML beta is strongly negative after bear markets; the portfolio is effectively short the market during rebounds.
- Crowding/deleveraging: funding-liquidity shocks hit both legs (AMP).
- Short-side frictions: borrow fees, recalls, squeezes in small illiquid losers.
- Tax and turnover drag; capacity limited in small caps.
- Data pitfalls: survivorship bias, delisting returns for losers (large negative), price-limit stocks, lookahead in fundamentals used for residuals.

## 7. MY TWIST (hypotheses, NOT backtested)

### Twist A: Residual 12-1 momentum with crash-state de-risking
- Rationale: Blitz et al. argue residual ranking reduces time-varying factor exposure; Daniel-Moskowitz show crashes are partly forecastable from bear-market state and volatility.
- Rule: each month regress 36 months of stock excess returns on market, size, value (and optionally industry returns) to get residuals; rank on the cumulative 12-1 residual return divided by residual volatility; go long top decile / short bottom decile. Scale the portfolio by (target vol)/(forecast WML vol), where forecast vol uses 126-day daily WML returns; set weight to 0.5x when trailing 24-month market return is negative AND market realized vol is in its top quintile.
- Parameters: residual regression window {24, 36, 60}; vol-normalized rank vs raw; bear-state threshold {market 24m return <0, <-10%}; vol quintile {top 20%, top 30%}.
- Expected effect: lower skew penalty and smaller worst months at the cost of some upside; slightly lower turnover.
- Falsification: if worst-month return and max drawdown are not improved (bootstrap 95% CI) vs plain 12-1 value-weighted decile momentum in both 1927-1980 and 1981-2025 samples, or if net Sharpe falls, reject.

### Twist B: Turnover-buffered rank (hysteresis) to cut costs
- Rationale: monthly decile re-sorting churns marginal names whose edge is smallest.
- Rule: enter at top 10% rank, exit only when rank drops below top 25%; same for shorts; position cap by liquidity (1% ADV).
- Parameters: entry/exit bands {10/20, 10/25, 10/30}.
- Expected effect: turnover reduced materially (magnitude to be measured); gross return slightly lower, net higher.
- Falsification: if net-of-cost Sharpe under a 2x cost multiplier is not higher than baseline, reject.

### Twist C: Industry-neutral momentum blended with value as a risk partner
- Rationale: AMP document negative value/momentum correlation; industry momentum drives much of raw momentum and creates concentrated sector bets.
- Rule: rank within industry (e.g. 49 Fama-French industries) with industry-adjusted 12-1 returns; combine 60% value / 40% momentum score as in the AQR illustration of a 60/40 HML/UMD mix; keep sector-neutral.
- Parameters: weights {50/50, 60/40}; industry grouping.
- Expected effect: smoother returns, reduced crash exposure.
- Falsification: if the combo's worst drawdown in 2009 and 2020-21 value/momentum episodes is not lower than momentum alone, reject.

## 8. Implementation spec

Data: CRSP-quality daily/monthly prices with delisting returns; point-in-time shares/market cap; borrow-fee/availability data (or proxy by size and short-interest); Fama-French factors; industry classifications; ADV.

Universe: market cap above NYSE 20th percentile, price above $5, ADV above a threshold.

Signal: 12-1 cumulative (raw or residual); skip the most recent month. Winsorize at 1/99.

Sizing: long and short books each 100% gross (50/50 allocation) equal-weight within decile, capped per name 1% of NAV and 5% of ADV; then volatility scaling per Twist A.

Execution: rebalance monthly; split into 3-5 day trading windows with limit orders; avoid trading the last/first minutes. Stops: no per-name price stops; use portfolio-level.

Costs model: commission ~1 bp; half-spread (use TAQ-based by size bucket, e.g. 5-10 bps for mid caps, higher for small caps); market impact via square-root model 0.1-0.5 x sigma x sqrt(trade/ADV); short borrow 25-500+ bps/yr by bucket; financing at benchmark + spread; report net at 1x/2x.

```
each month-end:
  universe = filter(stocks)
  R = cum_return(t-12, t-2)         # skip last month
  if residual: R = cum(resid_ret(t-12..t-2)) / resid_vol
  rank, apply hysteresis bands vs prior holdings
  longs, shorts = top, bottom
  w = equal weight, cap by liquidity
  scale = target_vol / forecast_vol(WML_daily, 126d)
  if bear_state and high_vol: scale *= 0.5
  trade to w*scale over next 3-5 days
```

## 9. Backtest plan

- Sample: 1927-2025 in two halves (1927-1980 and 1981-2025), plus international developed markets as independent out-of-sample (the finding Daniel-Moskowitz and AMP both lean on).
- Walk-forward: estimate residual regressions and vol forecast using only past data; fix hyperparameters by 1963-1990, freeze for 1991-2025; repeat with rolling re-selection.
- Multiple testing: log all variants (lookbacks, skip, weights, bands); apply Harvey-Liu-Zhu style adjusted t-statistics (hurdle around 3) or the deflated Sharpe ratio / White's Reality Check on the trial set.
- Controls: placebo tests with random ranks, with 1-month lag, with the signal shifted forward 6 months.
- Metrics: net Sharpe, CAGR, volatility, skewness, kurtosis, worst month, max drawdown and recovery time, turnover, average holding period, exposure to market/SMB/HML/RMW/CMA, 2009 and 2020-21 case studies, long vs short leg decomposition, capacity at 0.5/1/5% ADV.
- Report both value-weighted and equal-weighted; show results excluding bottom size quintile.

## 10. Risk management and kill-switch rules

- Vol target (e.g. 10-12% annualized) with daily forecast; cap leverage at 2x gross per side.
- Crash guard per Twist A; additionally, flatten the short book partially if the market rises more than 10% in 20 days while the market's trailing 24-month return is negative (hypothesis, to be tested; not a validated rule).
- Per-name 1% NAV cap, sector net exposure within +/-5%, borrow-recall monitoring.
- Drawdown rules: -10% review, -15% halve risk, -25% stop and audit; remember the unconditional history includes -50% or worse drawdowns for static WML in some episodes (exact figure not extracted here; [UNV]).
- Kill switch: breach of model beta bands, data-quality alarm, or net-of-cost live Sharpe below 0 over 5 years.

## 11. Annotated sources

| # | Source | URL | Type | Grade |
|---|---|---|---|---|
| 1 | Jegadeesh and Titman 1993, J. Finance | https://www.bauer.uh.edu/rsusmel/phd/jegadeesh-titman93.pdf | Peer-reviewed, read | A |
| 2 | Daniel and Moskowitz, Momentum Crashes (NBER 20439; JFE 2016) | https://www.nber.org/papers/w20439 | Peer-reviewed/WP, read | A |
| 3 | Asness, Frazzini, Israel, Moskowitz, Fact, Fiction, and Momentum Investing (JPM 2014) | https://www.aqr.com/-/media/AQR/Documents/Journal-Articles/JPM-Fact-Fiction-and-Momentum-Investing.pdf | Practitioner-authored journal article, read; authors have commercial interest | B+ |
| 4 | Asness, Moskowitz, Pedersen, Value and Momentum Everywhere (J. Finance 2013) | https://pages.stern.nyu.edu/~lpederse/papers/ValMomEverywhere.pdf | Peer-reviewed, partly read | A |
| 5 | Blitz, Huij, Martens, Residual Momentum (JEF 2011) | https://repub.eur.nl/pub/22252 | Peer-reviewed, abstract only | B+ |
| 6 | Harvey, Liu, Zhu, ...and the Cross-Section of Expected Returns (NBER 20592) | https://www.nber.org/papers/w20592 | Peer-reviewed/WP, partly read | A |
| 7 | CXO Advisory summaries of residual momentum | https://www.cxoadvisory.com/momentum-investing/stripping-risks-from-a-stock-momentum-strategy/ | Blog summary, snippet only | C |
| 8 | Carhart 1997, On Persistence in Mutual Fund Performance | (not fetched) | Peer-reviewed, cited from memory | B (unread) |
| 9 | Novy-Marx, Is momentum really momentum? | (not fetched) | Peer-reviewed, cited from memory | B (unread) |
| 10 | Frazzini, Israel, Moskowitz, Trading costs of asset pricing anomalies | (not fetched; known only via citation in source 3) | WP | B (unread) |

## 12. Open questions

1. What is the net-of-cost, net-of-borrow Sharpe of long-short momentum after 2013, using independent (non-AQR) execution assumptions?
2. Does residual momentum's advantage survive after the 2010s and in non-US markets?
3. Can crash states be forecast ex ante in real time with enough lead time, or are Daniel-Moskowitz results partly in-sample?
4. How much of "momentum" is really industry momentum or earnings momentum?
5. What is the right rank-skip convention (12-1 vs 12-2 vs 11-1) and is the one-month skip merely a microstructure fix?
6. Is the factor capacity-limited as factor ETFs and quant funds scale?
