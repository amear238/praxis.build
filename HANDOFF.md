# HANDOFF — PRAXIS

Resume cards go here, newest on top.

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
