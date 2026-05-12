# DECISION_LOG — PRAXIS

Append-only. Non-trivial orchestrator judgments.

---

- [2026-05-11T00:00Z] WHO: orchestrator | WHAT: Initialize three ledgers (DISPATCH_LOG, DECISION_LOG, ISSUE_REGISTER) at project root | WHY: Adopt orchestrator-auditor protocol per user invocation of /orchestrator-mine | WHERE: /Volumes/Sensidine/Praxis.build/{DISPATCH_LOG,DECISION_LOG,ISSUE_REGISTER}.md | WHEN: session start 2026-05-11 | HOW: Follow ~/.claude/protocols/orchestrator-auditor-protocol.md going forward | STATE: closed
- [2026-05-11T00:00Z] WHO: orchestrator | WHAT: Reports dir = docs/reports/; commit-gate = none configured; test cmd = N/A (infra phase) | WHY: Project-0 setup decisions per protocol | WHERE: docs/reports/ | WHEN: session start | HOW: Subagents write reports here; orchestrator audits before commit | STATE: closed
- [2026-05-11T00:00Z] WHO: orchestrator | WHAT: MCP verification — n8n, Google Drive, ClickUp, Gmail all responsive | WHY: User asked to confirm all MCPs work before dispatching | WHERE: live MCP responses logged in session | WHEN: session start | HOW: Hit one read-only endpoint per server | STATE: closed
- [2026-05-11T00:25Z] WHO: orchestrator | WHAT: Defer prod signal-delivery design (remote n8n -> local NinjaTrader) to Block 1 | WHY: Block 0 is infrastructure setup; choosing SFTP/rsync/poller now is premature without NT8 watcher built. User's stated goal: "finish Block 0". | WHERE: ISSUE_REGISTER entry tracks; will be lifted at Block 1 kickoff | WHEN: 2026-05-11 | HOW: For 0.8 verification, retarget webhook write to /tmp/praxis-signals/<file>.json on remote n8n host; confirm file lands; verification = pipeline plumbing works end-to-end. Prod delivery handled in Block 1 design. | STATE: closed
