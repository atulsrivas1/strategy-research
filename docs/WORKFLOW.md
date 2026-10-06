# Research delivery workflow

Adopted October 5, 2026 from [equity-features](https://github.com/atulsrivas1/equity-features/blob/main/docs/PUBLIC_DEVELOPMENT.md).

Owner instruction: all commits attributed to Atul Srivastava; Codex is the separate PR reviewer. Use linked short-lived branches and PRs. Require a completed Codex review covering the final PR head, with findings resolved or explicitly dispositioned, before merge. If hosted review is unavailable, retain Code review with the blocker; author self-review cannot substitute. Activation is only established by actual settings and a completed representative review, never by this document alone. Request with `@codex review` following [official setup guidance](https://learn.chatgpt.com/docs/third-party/github).

Use stable SR story IDs, linked experiment IDs and evidence milestones. Pull the highest-priority dependency-satisfied Ready story, one active implementation initially. Rank uncertainty resolved, objective relevance and feasible data before adding complexity. No mandatory sprints, artificial deadlines or unattended worker.

| Stage | Gate |
|---|---|
| Backlog | Bounded question proposed; dependencies/decisions unresolved |
| Ready | Written scope, hypothesis, acceptance criteria, prerequisites and evidence plan available |
| In progress | Actual bounded work started and artifacts tracked |
| Code review | Concrete implementation/design and documentation self-reviewed or independently reviewed; actual reviewer identified |
| Test | Relevant independent correctness, data or empirical checks executed and assessed |
| Ready to release | Required checks, outputs, interpretation, limitations and documentation complete |
| Released | Sanitized result delivered through the declared repository channel |
| Done | Delivered source/evidence/links verified, acceptance reconciled and next work recorded |

Blocked reasons/dependencies are attached to the actual stage. Scientific verdict (invalid, rejected, inconclusive, promising, replicated) is separate from story status. Completion requires trustworthy evidence, not positive returns. Never claim acceptance from a merge alone or fabricate historical transitions.

Before each experiment define formulas/units/timing/availability/missingness/adjustments; data version/exposure; baseline/splits/costs; finite search budget; success/rejection criteria and independent tests. Source claims are not local results. A bug invalidates a run, while a negative result rejects only its tested scope. Keep every variant/correction with provenance locally and publish sanitized conclusions.

Milestones: M0 reliable stock inputs and machinery; M1 bounded stock comparisons; M2 execution plus independent evaluation; M3 bought calls conditional on stock evidence. No release dates promised. Documentation accompanies each story: issue acceptance, relevant methods/report, research index, scope backlog and next-step continuity. Do not publish private data or logs. Final artifacts, exact source and actual review/test evidence must be verified. Tests should be relevant to the change; documentation does not require a numerical backtest.
