# SR-027 - Create research feedback and participation tasks

## Problem and value

Users should be able to contribute a useful question or critique without providing code or private data.

Parent: https://github.com/atulsrivas1/strategy-research/issues/42
Release: M5 - Research community onboarding (C1). Provisional complexity: 3 points, not a time estimate.

## Plan before implementation

Define public channels/templates for reproduction questions, methodology critique and source clarification. Curate 2-3 bounded non-code tasks that add evidence rather than repeat old experiments.

## Acceptance

- [ ] Templates request only public/sanitized information and route market-data/privacy questions appropriately.
- [ ] Two to three concrete tasks have source links, acceptance and evidence owners, covering documentation, synthetic reproduction or methodology critique.
- [ ] Contributor credit, response expectations and triage rules are documented; proposals remain proposals until normal research qualification gates are met.

## Dependencies and entry

SR-026; EQ-133; existing-release gate.

Owner direction October 7, 2026: queue community work after existing releases. Before execution, verify acceptance receipts and reconciled scope for the existing library release sequence R5-R13 and research M2/M3, including companion I/O/worker delivery. Closed milestone status alone is insufficient. Already deferred research M4 is excluded and stays deferred. A formally owner-approved no-go/defer outcome may satisfy a conditional existing release; unfinished work cannot be silently skipped. New future scope does not automatically extend this frozen dependency list. No due date, automatic restart, new chat or recurring schedule. One explicitly assigned release owner and one active implementation when qualified.

## Validation

Walk through a sample public feedback submission and task without sending messages or exposing private data; verify routing and research gate preservation.

## Documentation and completion

Publish linked story plan, guide/examples/templates as relevant, checks and failures, delivery receipt and continuity update. Use Backlog -> Ready -> In progress -> Code review -> Test -> Ready to release -> Released -> Done. All stories start Backlog; plans are not releases. Public changes use linked draft PRs, owner commit identity, completed separate final-head Codex review and findings disposition, relevant checks, and actual published-source/artifact verification before Done. Documentation accompanies every story. Preserve existing release owners. Public materials use synthetic or explicitly licensed inputs and sanitized evidence. No new strategy trial, private data publication, paid acquisition, live trading or unsupported efficacy claim. Preparation of outreach material does not authorize sending invitations, posting to external communities or collecting private participant information.

## Sources

- [GitHub contribution guidance](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions)
- [Finding users](https://opensource.guide/finding-users/)
- [Welcoming communities](https://opensource.guide/building-community/)
- [Existing installed example delivery EQ-040](https://github.com/atulsrivas1/equity-features/issues/46)
- [Existing focused developer assessment EQ-117](https://github.com/atulsrivas1/equity-features/issues/223)

These sources motivate the proposal; community growth has not been measured locally. Reuse existing examples and assessments rather than duplicating their implementation.
