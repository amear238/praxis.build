# HANDOFF — PRAXIS

Resume cards go here, newest on top.

## Resume card — 2026-07-09

**HEAD:** `be920c1` (+ a session-wrap commit lands right after this card)

**Shipped this session (2 audited commits, 0 gate violations):**
- `82b7cf1` — Block 1 design LOCKED: WireGuard tunnel (D-2026-07-09-A) + Parallels NT8 host (D-2026-07-09-B). Beads B1-0..B1-e queued with dependency graph.
- `be920c1` — **Block 0 milestone TRADER-SIGNED-OFF (Amear, 2026-07-09)** after an independent read-only audit (5 VERIFIED / 3 trader-confirmed / 0 FAIL). Repo advanced to **Block 1 — Foundation (Build-First)**. Evidence: `docs/reports/2026-07-09-block0-milestone-audit.md`.

**Decisions locked this session (append-only):**
- **D-2026-07-09-A** — Block 1 tunnel = plain WireGuard (no third-party cloud coordinator; fits 'no cloud API in execution stack').
- **D-2026-07-09-B** — NT8 host = Parallels Win11-ARM VM on the Mac Studio for build-first sim NOW; a dedicated **native x64 Windows PC is a REQUIRED pre-Block-5 purchase**; NT8-on-Parallels viability gated by B1-0. (Boot Camp is impossible on Apple Silicon.)

**Current block:** Block 1 — Foundation. Open beads: 6 (B1-0..B1-e). `bd ready` = B1-0 (in progress) + B1-a. B1-c blocked on B1-0; B1-b on B1-a; B1-d on B1-b+B1-c; B1-e on B1-d.

**B1-0 (`Praxis_build-3i7`) pickup point — IN PROGRESS, trader-executed:** Parallels is already installed on the Mac Studio. Trader was handed Checkpoint 1 (install Windows 11 ARM) + Checkpoint 2 (install + launch NT8, confirm responsive under x64 emulation, connect a free NT sim account). **NEXT SESSION STARTS BY ASKING the trader's Checkpoint 2 result:** did NT8 launch cleanly / is it responsive or sluggish / any errors. NOT yet started: C3 (connect sim data feed + stream a chart), C4 (Parallels shared folder Mac->VM + test .json drop + measure latency). On results -> write `docs/reports/<date>-b1-0-nt8-parallels-validation.md`, audit, close B1-0. If NT8 is unviable under emulation -> escalate the native-mini-PC purchase now.

**Next 3 dispatches (P0->P2):** (1) finish B1-0 from the trader's checkpoint results; (2) B1-a WireGuard tunnel n8n-host<->Mac + scoped SSH key (trader-machine + n8n host work); (3) B1-b n8n SCP-push node into the VM shared folder (blocked until B1-a).

**Notes:** (a) NT8 is Windows-only — Linux/Wine considered and rejected as unsupported (trader asked; answered inline, NOT appended to DECISIONS). (b) `AUDIT_LOG.md` carries the normal rolling +1 PASS row uncommitted between commits — expected, folds into the next commit. (c) PHASE 3 BUILD SPECIFICATION still not in-repo; Block-0 milestone was judged against reconstructed criteria — consider importing the source spec. (d) No blockers, no quota issues.

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

**Post-run updates (2026-07-08, later commits):**
- `2a423c5` — D-2026-07-08-A: coworker visibility via GitHub read access, Drive sync dropped. Step 0.7 CLOSED (trader confirmed access). Drive-for-Desktop no longer needed; empty PRAXIS Drive folder is optional scratch.
- **Block 0: all 8 steps DONE.** Not marked complete as a block milestone — that is a trader sign-off gate.

**Open beads (1, blocked on trader):**
1. `Praxis_build-amd` (Block 1 design) — Amear: sign off docs/design/2026-07-08-block1-signal-delivery.md + answer its 3 open questions (Mac NAT reality; Tailscale vs plain WireGuard under no-cloud-API rule; where NT8 actually runs). On sign-off → DECISIONS.md entry + create beads B1-a..e.

**Next 3 dispatches once Block 1 design is signed off:** B1-a tunnel + scoped SSH key → B1-b n8n push node → B1-c launchd reconciliation sweep.

**Also pending trader:** (a) Block 0 milestone sign-off; (b) praxis-build-manager SKILL.md dry-run sign-off before it goes live; (c) Telegram token rotation decision still open (ISSUE_REGISTER 2026-05-12).

**Notes:** Test signals block0-verify-001 / audit-verify-002 were fake (sim verification, no live trading surface exists yet).

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
