# HANDOFF — PRAXIS

Resume cards go here, newest on top.

## Resume card — 2026-07-10 (session 6) — ✅ incident trader-ACCEPTED; v6y gate hardening SHIPPED; 30h flush one step from done

**HEAD:** wrap commit on top of `1ca57aa` (30h infra) ← `fec1722` (v6y) ← `f0da783`. Pushed. Block 1 (Foundation, Build-First).

**Trader gate cleared:** trader reviewed + ACCEPTED the session-4/5 concurrency incident (DECISION_LOG 2026-07-10T16:03Z row); all 5 parked beads unparked. Single-writer established FIRST: idle claude PID 88776 (cwd this repo) killed; PID 15918 belongs to another repo and was left alone.

**Shipped:**
- `fec1722` — **v6y CLOSED (P1):** audit token now embeds the staged tree hash (`git write-tree`) and the gate re-verifies it at commit time (mismatch/legacy token → deny + burn); tokens strictly single-use (consumed on allow; 2 stale tokens removed); commit DENIED while a foreign claude process has cwd in this repo (fail-closed, ancestry-walk excludes own session); runbook `docs/runbooks/2026-07-10-single-session-rule.md` + CLAUDE.md Do-Not line. 11/11 gate tests, auditor re-ran independently.
- `1ca57aa` — **30h infra (bead still OPEN):** sanctioned AUDIT_LOG flush path — `scripts/audit-log-flush-verify.sh` (classifies every staged row LANDED/SUPERSEDED/LANDED-WRAP/VOID-ANNOTATED/ANNOTATION, else exit 1), append-only `scripts/audit-log-annotate.sh` (VOID annotation for the 19927e89 incident row APPLIED), auditor FLUSH-MODE (staged set must be exactly AUDIT_LOG.md; staged AUDIT_LOG outside flush = auto-FAIL), runbook `docs/runbooks/2026-07-10-audit-log-flush.md`.

**▶ FIRST DISPATCH NEXT SESSION — finish 30h (trader halted session 6 right at this step):** `git add AUDIT_LOG.md` (alone) → dispatch orchestrator-auditor with the words **"flush mode"** + bead id 30h → it runs `scripts/audit-log-flush-verify.sh` + spot-checks → plain gated commit → `bd close Praxis_build-30h`. All 18 stranded rows already verified classifiable by both implementer and auditor in scratch clones.

**Open beads (5):** `30h` (P2, above) · `10i` (P2 — design doc ONLY; build stays trader-gated, external→shell control path) · `9tl` (P2 — F2 dedup, folds into the NinjaScript FileSystemWatcher consumer build, the remaining Block-1 item) · `587` (P3 NEW — gate form-check false-positive: armed gate denies unrelated Bash calls whose free text mentions the vcs name near the committing word; ATTENDED session, needs regression tests) · `8xf` (P3 burst latency).

**Operational notes:** One-session-per-repo is now ENFORCED by the gate, not just policy — a second claude session cwd'd here blocks all commits. Until 587 lands, phrase `bd`/`echo` free text to avoid "git … commit" adjacency or the armed gate false-positive-denies the call. AUDIT_LOG.md deliberately modified/unstaged (flush pending); RUN_DECISIONS.md untracked (session-4 ledger).

## Resume card — 2026-07-10 (session 5) — ✅ RECONCILED the session-4 halt; tip clean + pushed

**HEAD:** wrap commit on top of `1c53a18` (22r) ← `e76f5c6` (jpe) ← `5822420`. **Tip is clean and pushed.** Block 1 (Foundation, Build-First).

**What happened:** This session started from the trader's request to build the `/progress` plugin (bead `Praxis_build-jpe`). Mid-flight it collided with session 4's F-B1e-1 commit — the shared-index race session 4 documented (its 15:00:22Z token was minted while THIS session's plugin files were staged; 7f54ba9 recorded plugin files under the 22r message). Session 5 executed session 4's RECONCILE PLAN as the single active writer:
1. `git reset --soft` on 7f54ba9; split-staged by pathspec.
2. Plugin diff re-audited (token 297c68d4) → committed `e76f5c6`, bead jpe CLOSED.
3. F-B1e-1 diff re-staged + re-audited (token c072de2c; auditor re-verified deployed runtime + drill logs) → committed `1c53a18`, bead 22r CLOSED.
4. STATUS.md drift repaired (B1-b/d/e checked with commit refs), ledgers appended, wrap committed + PUSHED.

**Shipped by session 5 itself:** `praxis-progress` local plugin — `/progress` renders the ASCII progress report toward live SIM (STATUS.md + bd + AUDIT_LOG + git; report-only, milestones stay human-gated). Installed user-scope (`praxis-progress@praxis-local`); source `plugins/praxis-progress/`; after source edits run `claude plugin update praxis-progress`.

**Parked beads (5) — unpark after trader reviews the incident:** `v6y` (P1 gate hardening — ATTENDED session only; do not hot-patch gate hooks autonomously), `30h` (AUDIT_LOG flush; note the VOID 15:00:22Z 22r row, hash 19927e89), `10i` (design doc only; build trader-gated), `9tl` (F2 dedup contract — fold into the NinjaScript consumer build), `8xf` (P3 burst latency).

**Hygiene notes:** AUDIT_LOG.md remains modified/unstaged by design (30h). RUN_DECISIONS.md left untracked (session-4 run ledger). 5 other idle `claude` procs existed at wrap — trader should close them before the next session (v6y root cause).

## Resume card — 2026-07-10 (session 4, autonomous) — ⚠️ HALTED on concurrent-session repo corruption

**HEAD:** `7f54ba9` — ⚠️ **CONTAMINATED tip, LOCAL only, NOT pushed.** 5 clean audited commits sit below it. Block 1 (Foundation, Build-First).

**🚨 READ FIRST — WHY THIS SESSION HALTED:** `ps` showed **6 concurrent `claude` processes** sharing this repo. A parallel session authored a `praxis-progress` Claude plugin (`plugins/**`, `docs/specs/2026-07-10-praxis-progress-plugin.md`) + a `STATUS.md` edit and **staged them into the shared `.git/index`** during my F-B1e-1 audit window. My no-pathspec tip write (`7f54ba9`) recorded **their 7 files under my "Praxis_build-22r (F-B1e-1)" message**, and my own audited F-B1e-1 files were **dropped from the write** (they sit untracked/staged in the working tree). The audit gate mints a token but does not re-bind the staged tree at write time, so the concurrent injection slipped through (filed `Praxis_build-v6y`, P1). I did **NOT** rewrite history (unsafe while other sessions can wake) and **did not push**. Full detail: DECISION_LOG `2026-07-10T15:20Z`.

**RECONCILE PLAN (do this FIRST next session, as the ONLY session on the repo):**
1. Confirm no other `claude` procs are touching the repo (`ps aux | grep claude`); if any, stop them / use a git worktree.
2. Decide the fate of `7f54ba9`: it holds a legitimate but mis-attributed `praxis-progress` plugin. Cleanest = `git reset --soft HEAD~1`, then unstage plugin/STATUS/docs-specs, re-stage ONLY the F-B1e-1 files, re-audit (fresh token), and record them under the 22r message; separately record the plugin work under its own message/bead. My audited F-B1e-1 source is backed up at `scratchpad/f-b1e-1-backup/` and also live in the working tree.
3. Then close `Praxis_build-22r` (fix already deployed+audited — see below).
4. Only push AFTER the tip is clean.

**Shipped this session (5 CLEAN audited commits, in the repo, pushable once tip is fixed):**
- `b5e022e` — **B1-b (p7s) CLOSED:** n8n local file-write node in workflow `EmMbN4sslwIx1ydn` — atomic `.tmp`→`.json` into `/files/outbox`, 3×/2s retry, error→existing Telegram node. Happy+error paths live-fired.
- `7420ae5` — **B1-c-fu (4hd) CLOSED:** stale-heartbeat alert live-fired end-to-end (heartbeat 601s → n8n exec 1087018 → Telegram msg 29); raw evidence embedded (survives n8n's <1-day pruning); durable `ALERT FIRED` log line added.
- `c19531b` — **B1-b-fu (3m8) CLOSED:** event-driven sweep via launchd **WatchPaths** on outbox (relay ~0.25–0.6s, was up to 60s), 60s poll kept as backstop — required for B1-d's <5s.
- `d24537c` — **B1-d (4wk) CLOSED:** e2e sim latency 4.18–4.31s (<5s PASS, auditor re-ran 4.18s) + idempotency at contract level (same signal_id+ts → 1 drop file). Findings F1/F2 filed.
- `5822420` — **B1-e (63b) CLOSED:** local offline failure drill (re-scoped off the dead WireGuard wording). Spool+replay PASS; found a **HIGH silent-loss gap** → F-B1e-1.

**F-B1e-1 (22r) — DEPLOYED LIVE + audited PASS, but NOT in the repo (the contamination):** a new **stuck-backlog detector** launchd job (`praxis-signals-backlog-check.sh` + plist, 30s, 60s threshold) fires a Telegram alert when `*.json` persists in `incoming/`/outbox — closing the gap where a drop-promotion failure was SILENT (sweep touched `.heartbeat` unconditionally). The detector **is running now** (3 praxis launchd jobs healthy) and the auditor independently re-ran the drill (exec 1089263/msg47). Only the repo record is missing — reconcile per plan above.

**All beads terminal-stated. Open work = 6 PARKED blocked (unpark after reconciliation):**
- `Praxis_build-22r` (P1) — record the F-B1e-1 fix in the repo + close (fix already live).
- `Praxis_build-v6y` (P1) — gate/concurrency gap: bind audit token to the staged tree hash + enforce one-session-per-repo (or worktrees).
- `Praxis_build-30h` (P2) — AUDIT_LOG rolling-row flush path (still stranding rows; AUDIT_LOG.md stays modified).
- `Praxis_build-10i` (P2) — Telegram→Claude inbound control channel: **design-doc-only was the plan; build stays PARKED (never-default external→shell control path, needs trader authority-scope sign-off).** Not started this session.
- `Praxis_build-9tl` (P2) — F2: NT8 watcher must dedupe on in-file `signal_id` (drop filename is ts+signal_id).
- `Praxis_build-8xf` (P3) — F1: relay burst latency >5s under ~2s bursts (launchd WatchPaths ~10s throttle); also investigate why steady is ~4.2s vs ~0.6s raw relay.

**Next 3 dispatches (P0→P2):** (1) reconcile tip `7f54ba9` + close 22r (above); (2) `v6y` gate/concurrency hardening so this can't recur; (3) `10i` design doc (build parked pending trader). Telegram blocker already sent to trader re: stop the other sessions.

**Notes:** ORCH_N8N_WEBHOOK live all session (blockers+safe-defaults delivered). Safe-defaults logged: WatchPaths sweep (3m8), B1-e re-scope. AUDIT_LOG.md + DECISION_LOG.md remain modified/unstaged (30h + this session's rows). RUN_DECISIONS.md (untracked) documents the autonomous-run scope.

## Resume card — 2026-07-09 (session 3)

**HEAD:** `dc5216c` (+ a ledger/wrap commit lands right after this card) · Block 1 (Foundation, Build-First).

**Big move this session — TOPOLOGY PIVOT (D-2026-07-09-D):** trader has no VPS and n8n already runs LOCALLY on the Mac (Docker), so public-ingress (VPS+WireGuard vs tunnel) is DEFERRED to pre-live. Block-1 build-first now runs fully local + free. Re-scoped: **B1-a → DEFERRED** (runbook + `/Users/admin/praxis-wg` scaffold parked, not deleted); **B1-b → local file-write node**.

**Shipped/closed:**
- `dc5216c` — **B1-c CLOSED (audited PASS):** `~/praxis-signals` layout + launchd 60s rsync backstop (n8n outbox→drop dir) + heartbeat + stale-alert. Deployed to INTERNAL disk — macOS TCC blocks launchd from the external Sensidine volume (saved as bd memory). Parallels VM share scoped to `/Users/admin/praxis-signals` ONLY; **whole-home over-share (B1-0 finding) RETIRED** (prlctl-confirmed). Sweep live-verified end-to-end (file swept + visible in VM).
- Decisions logged: **D-2026-07-09-C** (signals dir owner) + **D-2026-07-09-D** (local n8n / defer ingress). Drift row: a parallel stale session was reconciled (its `~/Downloads/files/` D-C draft is NOT applied — in-repo ledgers are authoritative).

**Next 3 dispatches (P0→P2):** (1) **B1-b** (`Praxis_build-p7s`) — point n8n workflow `EmMbN4sslwIx1ydn` at `/Users/admin/n8n-compose/local-files/outbox`; sweep relays to VM. (2) **B1-c-fu** — live-fire the stale-alert to confirm Telegram delivery (ties to open Telegram token rotation). (3) **B1-d** — end-to-end sim latency + idempotency.

**Open housekeeping:** bug `30h` (AUDIT_LOG rolling-row path — resolution chosen: option (a) dedicated flush change; not yet built, rows still strand, AUDIT_LOG.md stays modified). PHASE 3 BUILD SPEC still not in-repo. praxis-build-manager SKILL.md still DRAFT. Parallels prlctl share-config is Pro-only (this Mac = Standard → VM-share is GUI-only).

## Resume card — 2026-07-09 (session 2)

**HEAD:** `6909b96` · Block 1 (Foundation, Build-First) · 6 open beads (0 in progress)

**Shipped this session (5 audited commits, 0 gate violations after the audit caught 1 scope defect and I fixed it):**
- `e586aff` / `370841c` — B1-0 coworker dispatch brief + clarified installer/no-login sim (`docs/briefs/2026-07-09-b1-0-coworker.md`).
- `4680386` — **B1-a prep runbook** (`docs/design/2026-07-09-b1-a-wireguard-ssh-runbook.md`): both wg0.conf templates, keygen, macOS sshd tunnel-bind, rrsync `-wo` forced-command (internal-sftp fallback), verify checklist mapping 1:1 to B1-a. Placeholders only. Bead `dgt.1` closed.
- `6909b96` — **B1-0 CLOSED: NT8-on-Parallels validation PASS.** C2/C3/C4 all pass (NT8 8.1.7.2 installs/launches/streams real-time data under x64 emulation; FSW file-drop 130–264ms, 100% detection 13/13). Trader-executed, independently audited. Evidence: `docs/reports/2026-07-09-b1-0-nt8-parallels-validation.md`. **D-2026-07-09-B (build-first on Parallels) now confirmed viable; native x64 mini-PC stays pre-Block-5, NOT escalated.**

**▶ START NEXT SESSION — B1-a and B1-c are the ready live-machine work (need trader/coworker at the Mac + n8n host):**
1. **B1-a** (`Praxis_build-dgt`) — bring up the WireGuard tunnel from the runbook; fill the placeholder table (VPS public IP, WG port, 4 keys, signals dir). Verify: scp-into-signals succeeds / scp-elsewhere denied / off-tunnel sshd times out. Then B1-b (n8n SCP-push node, workflow EmMbN4sslwIx1ydn) unblocks.
2. **B1-c** (`Praxis_build-dnt`) — create `~/praxis-signals/` and **scope the Parallels VM share to THAT dir only.** SECURITY FINDING from the B1-0 spike: C4 shared the **entire Mac home** into the VM (`\\psf\Home` / `Z:\`) — tighten before any real signal flows. Add launchd reconciliation.

**Next 3 dispatches (P0→P2):** (1) B1-a live bring-up → (2) B1-b n8n push node → (3) B1-c scoped share + launchd. Dep graph: B1-b←B1-a; B1-c unblocked (B1-0 closed); B1-d←B1-b+B1-c; B1-e←B1-d.

**Open housekeeping:**
- `Praxis_build-30h` (P2 bug) — **AUDIT_LOG rolling-row recording path unresolved.** A strict auditor pass rejected folding the prior commit's rolling PASS row into a feature commit (looks like a smuggled self-approval). So audit-trail rows now **strand uncommitted** — `AUDIT_LOG.md` shows as modified in the working tree at session end (3–4 rows), which is EXPECTED until 30h is resolved. Local trail is intact; they just aren't in git. Decide the sanctioned flush path (see bead).
- Gate over-matches any Bash command containing "git"…"commit" as substrings (e.g. the word "uncommitted", or "commit" in a bd description) — documented fail-closed behavior; pass such text via a file or reword.
- PHASE 3 BUILD SPEC still not in-repo (Block-0 milestone judged on reconstructed criteria); Google Sheet still splits Block 1 into Education/Build rows vs the beads' single Build-First — reconcile when the spec lands.
- praxis-build-manager SKILL.md still DRAFT (pending trader dry-run sign-off); Telegram token rotation still open.

**Notes:** Google Sheet Block-0 row was reconciled to Complete + trader sign-off this session; Block-1 rows set In Progress. No quota issues. The coworker brief is on GitHub for pickup, but B1-0 ended up trader-executed directly so the coworker hand-off may be moot.

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
