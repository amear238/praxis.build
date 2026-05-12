# DECISION_LOG — PRAXIS

Append-only. Non-trivial orchestrator judgments.

---

- [2026-05-11T00:00Z] WHO: orchestrator | WHAT: Initialize three ledgers (DISPATCH_LOG, DECISION_LOG, ISSUE_REGISTER) at project root | WHY: Adopt orchestrator-auditor protocol per user invocation of /orchestrator-mine | WHERE: /Volumes/Sensidine/Praxis.build/{DISPATCH_LOG,DECISION_LOG,ISSUE_REGISTER}.md | WHEN: session start 2026-05-11 | HOW: Follow ~/.claude/protocols/orchestrator-auditor-protocol.md going forward | STATE: closed
- [2026-05-11T00:00Z] WHO: orchestrator | WHAT: Reports dir = docs/reports/; commit-gate = none configured; test cmd = N/A (infra phase) | WHY: Project-0 setup decisions per protocol | WHERE: docs/reports/ | WHEN: session start | HOW: Subagents write reports here; orchestrator audits before commit | STATE: closed
- [2026-05-11T00:00Z] WHO: orchestrator | WHAT: MCP verification — n8n, Google Drive, ClickUp, Gmail all responsive | WHY: User asked to confirm all MCPs work before dispatching | WHERE: live MCP responses logged in session | WHEN: session start | HOW: Hit one read-only endpoint per server | STATE: closed
