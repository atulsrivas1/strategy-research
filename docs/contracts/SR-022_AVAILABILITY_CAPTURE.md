# SR-022 / R03 prospective availability capture contract

Prepared design, not implemented capture, historical clock qualification or strategy efficacy. Extends the accepted [R03 requirement](../design/BUILD_REGISTER.md) under existing [SR-022](../stories/SR-022_PLAN.md). The [recovery disposition](../../reports/D1-recovery-disposition.md) explains why prospective observation machinery now has greater information value than repeating searches of unchanged missing paths. SR-022 retains M2 and its exhausted comparison budget; this contract adds no market replay or later release.

The first build should be a research-local, offline receipt recorder and validator, using synthetic files for correctness. No network acquisition, source-owner write, producer job, credential handling or price/outcome parsing. Actual source capture remains separately scoped after its access rules and input identity qualify. Source authority and clock authority are explicit, independent fields.

| Field | Required meaning |
|---|---|
| Receipt ID/schema version | Stable identity of the append-only observation, separate from an experiment ID |
| Source identity and byte digest | Exact object/version and observed bytes; integrity is not provider provenance or coverage |
| Event time | What occurred in the market, if the source defines it; unknown otherwise |
| Provider publication/acceptance time | Provider-declared dissemination clock with its evidence and qualification; never substituted from a report period |
| Retrieval start/end | Local collection interval, UTC and its local clock basis; not proof of earlier release |
| First-seen | Earliest recorded local observation of this exact object/version; preserve it on idempotent reads |
| Revision/parent digest | Same logical object with changed bytes receives a new version, linked to prior receipt; preserve all versions |
| Availability basis/status | Observed local, qualified provider clock, modeled or unknown; recording an object does not make availability qualified |
| Source/access/clock limitations | Missing lineage, coverage or clock authority persists in the receipt and downstream admission decision |

Recorder time comes from the recording operation, not a user-supplied historical date. Unknown provider/event clocks stay null. Re-reading identical bytes preserves first-seen; an observation can append a later last-seen record. Changed bytes retain earlier versions rather than overwrite them. Concurrent observations must not lose an earlier receipt or assign duplicate IDs. A partial/failed write is detectable and cannot create a successful receipt. The recorder must avoid certifying stability when input bytes change during collection.

Receipt validation rejects unsupported schemas, inconsistent identities/digests, impossible observation intervals, missing evidence for a claimed qualified clock and a revision link that does not match retained records. Hash chains may detect accidental inconsistency; they do not authenticate provider claims or prove a local clock's accuracy. No secret, internal path or original payload is published by the recorder.

A later decision-time adapter can admit only explicitly qualified evidence available by the decision, with a preregistered latency/freshness policy. Event time, a reconstruction date, file mtime, current inspection and modeled latency must not masquerade as historical first-seen. No recorder output automatically promotes original-feed lineage, official-session semantics, corporate actions, universe, fills or accounting. Unknown evidence yields unknown context under the scanner/context protocol.

Independent correctness acceptance for the first build: known digest of hand-authored bytes; identical re-observation preserving first-seen; changed bytes preserving a revision; missing/changed source and failed write retaining honest status; unknown clocks preserved; impossible/falsely qualified clocks rejected; deterministic collision/concurrency policy tested. Use synthetic files only. Do not duplicate market scanner fixtures or evaluate context returns. Freeze a specific implementation plan before code; documentation alone does not move the full SR-022 story to Done.
