# ISSUE_REGISTER — PRAXIS

Append-only. Bugs, blockers, unresolved questions, deferred items.

---

- [2026-05-11T00:05Z] WHO: orchestrator | WHAT: Telegram bot token leaked into chat transcript by user | WHY: User pasted full token in answer to setup question | WHERE: conversation transcript (not git) | WHEN: discovered 2026-05-11 at dispatch planning | HOW: User to decide rotate-vs-keep; either way token NEVER committed to repo, stored only in n8n credential vault | STATE: open
- [2026-05-11T00:05Z] WHO: orchestrator | WHAT: Need Telegram chat_id to wire 0.6 | WHY: Token alone insufficient — bot must know where to send | WHERE: Step 0.6 (Praxis_build-8n6) | WHEN: blocks 0.6 dispatch | HOW: User messages @xarq5bot then we call getUpdates, OR user pastes chat_id directly in n8n UI | STATE: open
- [2026-05-11T00:05Z] WHO: orchestrator | WHAT: Block 0 step "Configure n8n Host-Side Webhook" — confirm exact path layout (/signals/ subdir to be created) | WHY: Dispatch needs concrete write target | WHERE: /Volumes/Sensidine/Praxis.build/signals/ | WHEN: before 0.5 dispatch | HOW: Subagent creates dir + .gitkeep + .gitignore for *.json | STATE: closed (done in 0.5 commit)
- [2026-05-11T00:20Z] WHO: orchestrator | WHAT: n8n write path assumes n8n process can see /Volumes/Sensidine/Praxis.build/signals/ on its own host fs | WHY: If n8n runs in Docker, this path is inside the container and won't land in the repo dir unless bind-mounted | WHERE: n8n workflow EmMbN4sslwIx1ydn "Write Signal File" node; will block Step 0.8 verification if mismatched | WHEN: surface to user before 0.8 verification test | HOW: User confirms n8n deployment topology — if Docker, add `-v /Volumes/Sensidine/Praxis.build/signals:/Volumes/Sensidine/Praxis.build/signals` to compose/run config; if native, no action | STATE: open
