# Release-based planning and continuous pull

Follow the equity-features delivery approach: numbered parent epics and child stories, one milestone per story, concrete plans before implementation, independent relevant verification, documentation with each story and exact delivery receipts. Research releases deliver evidence, not library packages or live trading.

Pull the highest-ranked dependency-satisfied Ready story, starting with one active implementation. Finish active work before adding more; record urgent interruptions and displaced work. No mandatory sprints, deadlines or automatic schedules. Weekly review during active work is a manual planning practice, not an unattended worker.

GitHub Project owns current lifecycle status. Ranked backlog owns scope, dependencies and relevance; epic acceptance aggregates children. Release milestones M0–M3 have evidence gates, not dates. M4 is deferred future scope excluded from this pass. Each story has one release assignment and a defined delivery channel. A favorable result is not necessary for a complete research delivery.

Use Backlog -> Ready -> In progress -> Code review -> Test -> Ready to release -> Released -> Done. Blocked/exploratory/deferred are scope/readiness labels, not invented lifecycle stages. Actual completed Codex review covers final head before merge; self-review/CI do not substitute. Tests may run earlier, but formal acceptance is Test. A merged implementation awaiting declared release stays Ready to release; only verified delivered artifacts permit Released/Done.

Create tags/GitHub releases only when assigned scope is reconciled, acceptance/review/checks complete and artifacts ready. Release receipt records exact source and artifacts, included stories, verdicts, reviewer/head coverage, checks, limitations and post-publication verification. Publish no empty completion release to satisfy planning.
