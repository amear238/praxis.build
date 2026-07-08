# HANDOFF — PRAXIS

Resume cards go here, newest on top.

## Resume card — 2026-07-08

**HEAD:** `2032bc1` (+ session-wrap commit after this card)

**Shipped this session (autonomous run, 6 commits, 0 gate violations):**
- `291826f` — orchestrator-mine v3 scaffold self-installed, enforcement live-verified; bd reinstalled (1.1.0)
- `d18df54` — Jul 4 update integrated: D-2026-07-04-A/B into DECISIONS.md, SHM spec + skill outline into docs/specs/
- `6b776a8` — Telegram notify path live (n8n workflow Wq90beq5oysV1bpe, /webhook/praxis-orch-notify, ORCH_N8N_WEBHOOK in settings env — loads next session)
- `323e692` — Step 0.7 Drive-side prep: PRAXIS folder 1_59Pz_vdgxuPeMmp0yfuVHGDcbF1c9fU
- `8e82010` — praxis-build-manager SKILL.md DRAFT v0.1 (NOT live until trader dry-run sign-off)
- `2582531` — Step 0.8 PASSED: full loop webhook→file(/tmp/praxis-signals on n8n host)→200→Telegram + 400-reject path, verified live by implementer AND auditor
- `2032bc1` — Block 1 delivery design PROPOSAL (SFTP push over private tunnel, 31/35)

**Open beads (2, both blocked on trader):**
1. `Praxis_build-rnu` (0.7) — Amear: drag tracker sheet 12XNBvD6… into PRAXIS Drive folder; optional coworker share; optional Full Disk Access for local verification (Drive for Desktop confirmed installed)
2. `Praxis_build-amd` (Block 1 design) — Amear: sign off docs/design/2026-07-08-block1-signal-delivery.md + answer its 3 open questions; then DECISIONS.md entry + beads B1-a..e

**Next 3 dispatches once unblocked:** B1-a tunnel + scoped SSH key → B1-b n8n push node → B1-c launchd reconciliation sweep.

**Blockers / notes:** Block 0 = 0.7 trader-half only. Telegram token rotation decision still open (ISSUE_REGISTER 2026-05-12). Test signals block0-verify-001 / audit-verify-002 were fake (sim verification, no live trading surface exists yet).

## Resume card — 2026-05-12

**HEAD:** `4b2c0b9`

**Shipped this session (Block 0):**
- `f231b4f` — Step 0.4: Google Sheets dashboard + orchestrator ledgers initialized
- `936d7e4` — Step 0.5: n8n signal webhook published (workflow EmMbN4sslwIx1ydn @ https://n8n.myzerker626.win/webhook/praxis-signal)
- `4b2c0b9` — Step 0.6: Telegram notification nodes wired (post-audit fix included)

**Open issues (ISSUE_REGISTER.md — 3 actionable):**
1. **Open** — User must create n8n credential `PRAXIS xarq5bot` (Telegram API, token from BotFather) and rebind 3 Telegram nodes in workflow EmMbN4sslwIx1ydn before activating draft version a8400246.
2. **Open** — Telegram bot token leaked in chat transcript; decide rotate vs keep (token NOT in repo).
3. **Open (ARCH)** — n8n is on remote box; webhook writes to `/Volumes/Sensidine/Praxis.build/signals/` which doesn't exist on the remote host. Block 0 verification (0.8) must retarget write path to a remote-host-valid dir. Production delivery (remote → local NinjaTrader) is a Block 1 design decision.

**Next 3 dispatches (in order):**
1. **P0 — Step 0.7** (Praxis_build-rnu): subagent preps Drive 'PRAXIS' folder, moves the Build Tracker sheet into it, sets sharing perms; user installs Google Drive for Desktop and points it at the folder.
2. **P0 — Step 0.8** (Praxis_build-v5h): after user binds Telegram credential, subagent retargets the n8n write path to a valid remote-host dir, then curls a sample payload at `https://n8n.myzerker626.win/webhook/praxis-signal`, confirms HTTP 200, asks user to confirm Telegram fired. Closes Block 0.
3. **P1 — Block 1 kickoff design doc**: decide signal delivery mechanism (remote n8n → local Mac for NinjaTrader watcher). Options: SFTP push, rsync cron, return signal in HTTP response with local poller, or relocate n8n local.

**Quota / blockers:**
- None this session. User wrapped intentionally to continue server-side work.
- All MCPs (n8n, Drive, ClickUp, Gmail) verified working at session start.
