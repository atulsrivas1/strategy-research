# SR-002 — Explain missing daily references and close conventions

Bounded question: can existing input provenance explain stock-specific missing daily history and determine which closing-price convention represents the intended observation?

Why: the first pilot has material missingness and close-field disagreement, while its estimated incremental effect is uncertain. Resolve trustworthy observations before adding signals or optimizing exits. Required data are available privately; no purchase or producer rebuild assumed.

Trace the first unavailable dates for two affected stocks, prior available dates and one control; select three largest input-only close discrepancies deterministically. Examples are selected for anomaly diagnosis, not outcomes or representative estimation. Compare existing derived records with authoritative supplied reference/price definitions and source dates, units, action/identity evidence and version.

Pass when the observation maps to evidenced semantics and agrees within documented precision, or when an unavailable/unresolved classification is honestly documented. Unresolved cases gate dependent replay. If a correction is required, independently test prior/current/stale date boundaries, missing-history handling and any actually implicated adjustment/identity rule; version a corrected study before market outcomes. Do not force missing fields to zero or change strategy thresholds.

Acceptance: source-linked sanitized findings; local exact manifests/commands/logs including failures; reusable field/clock contract or unresolved gate; scoped lesson; refreshed index/backlog/continuity. Complexity provisional 3 points, not days or velocity. No new strategy run, live order or change to the library project in this story.
