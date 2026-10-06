# M0 post-merge review reconciliation — October 6, 2026

M0 remains partial and unreleased. Owner merged [PR30](https://github.com/atulsrivas1/strategy-research/pull/30) at 03:52:04 UTC and [PR31](https://github.com/atulsrivas1/strategy-research/pull/31) at 03:52:44 UTC on October 6. Current integrated source is [e3ee3edfa939fb53f98f336e82aebee1dbd731f4](https://github.com/atulsrivas1/strategy-research/commit/e3ee3edfa939fb53f98f336e82aebee1dbd731f4). This updates prior preparation snapshots; it does not retroactively satisfy review-before-merge.

## Verified publication versus outstanding acceptance

The integrated main tree equals prepared PR31 head 2cc64c473870a948350b647e4e96c38632506820 exactly: all 58 blob identities match. Its [main check](https://github.com/atulsrivas1/strategy-research/actions/runs/37411048672/job/112099342406) passed. Original final-head PR checks and scoped private Gates 1–3 remain linked in the [qualification report](M0-qualification.md). No new numerical research or strategy/holdout run occurred in this reconciliation.

Fresh PR31 API inspection finds no reviews, inline comments, non-owner response or reaction to its final request. Owner merge and passing CI are not completed Codex review. PR30 is also merged; no duplicate implementation PR or revert/reapply is needed. Existing SR-006/007/008/009/010/019 delivery requirements remain unsatisfied where actual review/release is required; live Project remains authoritative. No new epic/story, Done state or release is claimed.

The prepared implementation commit 2cc64c4 has Atul Srivastava as both author and committer, associated with atulsrivas1. The GitHub-generated main merge e3ee3ed has Atul Srivastava as author and GitHub/web-flow as committer. That service-committer exception is disclosed; it does not meet the literal all-commits owner-committer rule. Existing history is preserved. New agent-created commits retain the owner as author and committer. No history rewrite or attribution-policy waiver is inferred.

## Required retrospective review scope

An actual completed hosted review must explicitly cover the integrated M0 implementation at e3ee3ed, not merely this new status document. Inspect the PR31 change from e9b71b3 to 2cc64c4 and the integrated repository files: fixtures/reference_machinery.py, scripts/check_reference_fixtures.py, fixtures/chronology.py, scripts/check_chronology.py, scripts/check_planning.py, the CI workflow, reports/M0-qualification.md, applicable story plans and M0 plan/receipt. Include incorporated PR30 AQuA safeguards and this reconciliation. Record reviewer login, response URL, exact reviewed source and findings disposition. An unspecified review scope is insufficient. Retrospective review can identify current defects but cannot erase the historical pre-merge exception.

Particular checks: future availability/censoring is never an ex-ante trade filter; embargo/purge does not make exposed windows fresh; disabled confirmation guard never invokes a loader; reference marks reject invalid cent values; private qualification counts are scoped reported local evidence, not publicly reproduced market results; modeled availability/fills and retrospective exclusions remain explicit; all unsuccessful runs and broader-source/M2 dependencies are retained.

After review, resolve the service-committer acceptance exception explicitly without rewriting protected history, reconcile every assigned story and publish/verify an exact evidence snapshot only after readiness. Do not release merely because merged. No later release, market trial, protected outcome access, paid data or live configuration is authorized by this record.

## Setup source and limits

[Official OpenAI GitHub review guidance](https://learn.chatgpt.com/docs/third-party/github) was read October 6, sections setup, manual requests and troubleshooting. It requires a connected repository; settings administration needs GitHub push/admin permission. Manual @codex review should receive a reaction and review; personal automatic preferences govern automatic requests. Prior visible settings showed the target present but controls disabled for the signed-in account. Fresh connection checks are distinct from successful review; no quota/account/root-cause claim is inferred solely from an unanswered request.
