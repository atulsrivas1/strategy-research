# Research audit and D2 provenance correction

October 9, 2026. Agent self-audit requested by the owner; no independent review claimed. Existing D1/D2 protocols, saved inputs/results, source modules, registry and verification coverage were inspected. No new strategy variant, source-lake price query, protected final access or candidate search.

## Concrete correction: incomplete executed-source hash coverage

The D2 pre-run source manifest omitted `research/d2_exploratory.py`, the actual entry engine. It recorded the common D1 math module, D2 check script, normalizer and runner. The later source verifier iterated only that recorded list, so it could pass while missing the actual engine. Earlier claims that the entire D2 executed engine was bound by a pre-run checksum are too strong and are corrected here.

The current published D2 engine reproduces every saved engine output from the saved development inputs. The original separate arithmetic checks and this reproduction support the saved proxy calculations; they do **not** retroactively create a missing historical checksum. The current engine hash is retrospective evidence only. Delivered Git tree/archive verification remains valid as publication identity; it is a different claim from binding all modules to the original execution. Preserve the [original report](D2-exploratory-test.md), receipts, manifests, code and result hashes unchanged; do not add a fabricated pre-run hash.

Future run receipts must enumerate and assert coverage of the actual imported engine and required dependencies before input I/O. This audit identifies that requirement; no future runner fix or independent source certification is claimed delivered here.

## Cash feasibility adds a material qualification limit

We reconstructed a shadow ledger for the exact saved three-policy trades, initial capital normalized to 1, fractional quantities equal to weight/entry price, existing 0.10% per-side costs, exits before entries at a shared stored-open date, and no financing interest. No opportunity was resized, removed or chosen using its outcome. This diagnoses borrowing needs under declared assumptions, not a new funded strategy or observed execution.

| Existing policy | Minimum normalized cash | Dates with negative cash | Maximum marked gross position value |
|---|---:|---:|---:|
| D2 scanner | −0.008720 | 9 | 1.047906 |
| D2 scanner plus context | +0.065733 | 0 | 0.915492 |
| Equal-cohort benchmark | −0.001625 | 2 | 1.014007 |

Cash plus marked positions matches all 48 saved curve points for each arm: **144 conservation checks**. Terminal proxy contributions are unchanged. Static original reference exposure of 1 did not guarantee cash feasibility once entry fees and recycled proceeds were included. Financing costs/reservations were absent, so the earlier positive contributions remain unfunded proxy outcomes, not feasible cash-account returns. Candidate exposure reduction changes financing requirements; its failed incremental return criterion must not be relabeled a funded risk benefit without a new preregistered objective/accounting contract.

## What the results actually teach

The D2 veto removed ten selected opportunities: two losses and eight winners. The D1 breadth veto also sacrificed more weighted winning contribution than it avoided in losing contribution. These are failures of the **tested overlays**, not universal rejections of trend or momentum. D2 scanner-versus-benchmark remains inconclusive despite a positive exposed point estimate. Arithmetic/CI passing and market hypotheses failing are separate outcomes.

D2's 60 slots use eight distinct stocks over 20 decision dates; one selected stock appears 16 times. Overlap and concentration reduce diversity. The largest absolute stock contribution is 43.480136% of summed absolute scanner contributions (a concentration diagnostic, not a chosen exclusion). Twenty dates supply only four nonoverlapping five-date chunks; this is not an effective-sample-size estimate. The five-date circular bootstrap preserves within-date stock dependence but cannot establish performance over unseen regimes or remove adaptive-selection bias.

A fixed audit flag for adjacent stored-open/close moves of at least 10% finds three flags involving two securities. News, actions, valid moves and source problems have not been distinguished by this audit. No bars/stocks were excluded or corrected, and no flagged move was used to tune a policy. Source/session/action/arrival assumptions remain explicit and nonblocking for exploratory work, but require material-risk diagnostics before broader claims.

The 20-session formation/five-interval hold is a distinct stock adaptation. The [previously read primary momentum methodology](D2-source-qualification.md) uses substantially different horizons and portfolio construction; its documented effect cannot be transferred by naming this adaptation momentum. Market context was always unknown in both recent D1/D2 tests, so these runs do not test a market-regime filter. Existing missing-evidence policy is retained.

Additional implementation boundaries: the loader verifies a positive instrument identifier but drops it from saved normalized price rows, limiting retrospective identity-change checks. Normalized Decimal prices become floats before ranking converts them back to Decimal, so exact Decimal arithmetic on saved floats is not an assertion of lossless original-source precision. These are auditability/precision design gaps, not demonstrated causes of a changed historical rank. Missing/boundary-tied decisions skip both D2 scanner and benchmark and force an inconclusive verdict; current data had zero such decisions, but future comparisons should retain a independently defined benchmark schedule. Helper/calendar coverage and unresolved handling need stronger boundary tests before broader use. No actual future-price selection leak or altered ranking was found in the scoped saved-input audit.

D1 and D2 also use different preregistered verdict definitions: D1 rejects a nonpositive point criterion, while D2 requires its negative interval for overlay rejection. Preserve those historical definitions, but standardize future reporting of point-criterion failure, uncertainty, economic feasibility and strategy evidence separately.

## Next work before another strategy experiment

1. Correct future manifest coverage and preserve security identity and price precision.
2. Design normalized funded-accounting contracts under existing R07/SR025 responsibility: fees/reservations, entry/exit ordering, overlap, cash feasibility and explicit financing. This is research infrastructure, not a live capital mandate or automatic later-release execution.
3. Specify separate scanner-versus-simple-benchmark and required scanner/context questions, with mechanism-supported formation/holding choices.
4. Preregister broader temporal coverage, exposure labels, support/precision and stopping criteria. All already observed dates remain development; protected final access stays disabled.
5. Diagnose material price/session/action assumptions without dropping inconvenient outcomes or treating missing provenance as an automatic exploratory block.

Do not tune old gates or move to another family merely to find a positive result. No new experimental budget is created by this audit. Full SR040/SR041 and M7 remain open/unreleased. Original experiments/verdicts remain preserved, with this provenance correction attached. All 28 existing repository checks and CI remain delivery requirements; old data/producer jobs, releases, trial budgets and owner commit attribution are unchanged.
