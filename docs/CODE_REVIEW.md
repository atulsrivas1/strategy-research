# Separate Codex PR review

Setup story SR-006 remains in Code review until the connected repository has an actual completed review on a concrete final head. Request `@codex review`; a posted request/reaction, self-review or CI is not completed hosted review. See [official setup guide](https://learn.chatgpt.com/docs/third-party/github).

Record reviewer login, response URL and reviewed SHA, actionable findings and disposition. Relevant changes need renewed final-head coverage. Missing configuration/access/quota blocks merge; preserve the failed request and retry after changed state. Do not invent an independent human reviewer or a required bot check.

Main now requires pull requests and the strict GitHub Actions `check` status, with force-pushes/deletion disabled, matching equity-features' protection model. Required human approving-review count is zero; the separate Codex response gate remains a documented requirement, not a claim that GitHub automatically enforces bot completion. Existing admin bypass behavior is preserved; do not use it to bypass the owner's review gate.

AGENTS.md Code Review Rules cover causal validity, unsupported performance/execution and public privacy. Numerical fixtures, data admission, costs, independent accounting and CI remain separate gates. No secret/API-key workflow or broad new access is introduced by these docs. Prior delivered foundation retains its honest historical self-review evidence; no retroactive hosted review is claimed.
