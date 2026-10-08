# SR-022 / R03 local availability recorder v1 — October 8, 2026

The [capture contract](../docs/contracts/SR-022_AVAILABILITY_CAPTURE.md) now has an [offline recorder and validator](../research/availability_recorder.py). This is research machinery tested on temporary synthetic files only. No provider/source capture, network acquisition, source-owner job or original market payload was accessed. [Historical source recovery](D1-recovery-disposition.md) remains blocked.

The recorder binds a logical object to an observed byte digest/count and local UTC collection interval. Re-reading identical bytes preserves first-seen; changed or reverted bytes retain earlier versions and revision links. SQLite transactions serialize observations before collection, preserving unique receipt order under concurrent calls. Source changes and interrupted writes return errors without a successful appended receipt. Existing unrelated databases are rejected. Validation opens the ledger read-only.

Every v1 receipt fixes provider publication/event clocks to null, source qualification to unknown and availability to observed-local-only. There is no caller-supplied historical observation date in the CLI. A decision-time admission consumer is not implemented; the recorder cannot qualify an original feed, historical provider release, official-session close, actions, universe, fills or accounting. Local clock accuracy and provider authenticity are not certified. Hash chains detect inconsistency, not malicious resealing, removal of the final tail or external authenticity.

Eleven [independent synthetic checks](../scripts/check_availability_recorder.py) cover a fixed known digest, repeat reads, changed/reverted versions, unknown clocks, missing/unstable files, interrupted transactions, concurrent receipt order, unrelated database preservation and backdated chronology. Additional resealed corruptions verify rejection of a false qualified clock, impossible interval, overwritten first-seen and wrong revision link; raw hash corruption is also rejected. These are eleven test cases with multiple assertions, not eleven sources or empirical trials.

The first test run failed with five Windows cleanup errors from test helper connections. Explicit closing corrected them; the failed run is retained privately and the final tests pass. Agent inspected evidence under the owner waiver; no separate independent approval claimed. Frozen reports/design/imports and exhausted M2 comparisons remain unchanged.

Run locally against an explicitly authorized synthetic file and a separate private ledger:

```text
python research/availability_recorder.py observe --ledger <private-ledger.sqlite> --file <synthetic-file> --source-id <logical-object-id>
python research/availability_recorder.py validate --ledger <private-ledger.sqlite>
python scripts/check_availability_recorder.py
```

Paths, receipts and source identities stay local; do not publish an actual ledger or arbitrary original bytes. An unsuccessful operation must be retained by its caller; inability to write is not represented as a successful receipt. Source reads are bounded to16MiB. Observation receipts are append-only through the API, but direct database access can alter records; this is not a tamper-proof service.

Full SR-022 remains open partial Test under M2. This delivers the bounded v1 recorder, not empirical context usefulness or full R03 historical qualification. All ten M7 stories remain open partial Test, M7 unreleased, zero market rows/strategy trials/final evaluations and final access disabled. Next preregister a provider-metadata adapter and its source/clock qualification before any actual capture or decision-time consumption; retain absent historical clocks as unknown. No new comparison budget, source production, later release, session or schedule follows from this build.
