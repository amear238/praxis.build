# HANDOFF — PRAXIS

Resume cards go here, newest on top.

## Resume card — 2026-07-15 (session 15) — Block-2 kickoff: Q2–Q9 resolved, b2-data spec+cost landed, roll LOCKED

**HEAD:** wrap on top of `26ce939`. Shipped (all auditor-PASS): `89f04b9` **b2-spec-gaps (cd4 CLOSED)** — Block-2 gaps Q2–Q9 trader-resolved (Q2 adopt §4 candidate checklist · Q3 WFE≥0.5 hard gate · Q4 NT8 default-provider minute, no paid budget, ~5yr/16 OOS · Q5 $2.96 RT + 1-tick slippage High-fill · Q6 MFFU acct+trailing-DD basis · Q7 optimize {lookback,noise,stop-ATR,exit} in WFA 252/63/63 · Q8 both NT8-VM + Python-Mac MC · Q9 fixed SHM-4/SHM-5 bands) → DECISIONS.md **D-2026-07-15-B**. `26ce939` **b2-data (hlw, Mac-side)** — data-acquisition spec (NQ 1-min 2021-07-15→2026-07-14), `config/backtest-cost-model.json` (encodes Q5), VM operator runbook + objective validation gate.

**Trader decisions this session (AskUserQuestion, DECISION_LOG 22:05Z + 22:30Z):** Q2–Q9 all locked (above) · **roll convention LOCKED** = volume/OI-crossover + back-adjusted Difference.

**Open beads (8):** **hlw ◐ half-open** — ONLY the VM-gated NT8 physical minute pull + §4 validation remains (roll locked, cost committed; run spec §5 runbook then check §4 gate → close). **b2-signal-repro (4uu) P2 — next buildable, but carries a trader gap: canonical Noise-Area breakout ruleset (Zarattini-Aziz-Barbon) not sourced in-repo — locate/supply before dispatch.** b2-wfa (zi1) blocked on 4uu+hlw · b2-mc · b2-refdist (xdr — carries Q6 numeric sub-input: needs MFFU acct size + trailing-DD numbers) · plus trader-VM: lhw (Sim101 QXD-TEST cancel), btb (sim test on 9d25243), 10i (activation). 518 P3 · 6h7 P4.

**▶ NEXT SESSION first dispatch:** resolve the b2-signal-repro ruleset gap (scout in-repo for the paper/spec; if absent, trader supplies), then dispatch b2-signal-repro (NinjaScript re-impl). VM-touch queue unchanged: hlw pull, lhw, btb, 10i. ⚠️ Sim101 11:12 long 1 NQ + bracket still your call. AUDIT_LOG deliberately dirty (session-14 mint rows + session-15 rows; flush still deferred).

## Resume card — 2026-07-15 (session 14) — Q1 answered + confirmed, btb journaling reversed, 10i built; Block-2 unlocked

**HEAD:** wrap on top of `9905338`. Shipped (all auditor-PASS): `8e739e4` **b2-q1** — Block-2 Q1 answered: Noise-Area Breakout is NOT TV-exportable (no Pine source in-repo; live payload carries no strategy internals) → re-implement in NinjaScript + NT8 Strategy Analyzer; trader CONFIRMED direction. `9d25243` **btb** — geometry rejects now handled uniformly like parse rejects (Print+Log+rejected/, NO journal line; trader DECLINED the REJECTED-GEOMETRY journaling). `9905338` **10i** — Telegram→Claude read/report/status-ONLY channel BUILT (fixed-argv allowlist, no claude -p passthrough, sender-restricted twice; STAGED not activated; registered Stop hook untouched after audit caught a hot-patch attempt).

**Trader decisions this session (AskUserQuestion, all in DECISION_LOG 21:10Z):** Q1 toolchain CONFIRMED (re-implement in NT8) · 10i scope = Option A read/report/status-only · btb journaling DECLINED → uniform (no journal line).

**Open beads (9):** btb ◐→blocked (VM sim test only) · lhw P2 (Sim101 QXD-TEST cancel — trader VM) · 10i blocked (trader activation) · **NEW Block-2 skeleton:** b2-spec-gaps P2 (Q2-Q9) → b2-signal-repro P2 (first buildable — NinjaScript re-impl) · b2-data · b2-wfa · b2-mc · b2-refdist (dep-wired) · 518 P3 · 6h7 P4.

**▶ NEXT SESSION — trader VM touches gate everything:** (1) lhw Sim101 cancel; (2) btb sim test on redeployed .cs (9d25243) → close btb; (3) 10i activation if wanted. **Your first Block-2 dispatch is now unlocked (Q1 confirmed):** b2-spec-gaps (resolve Q2-Q9) then b2-signal-repro. ⚠️ Sim101 11:12 long 1 NQ + bracket still your call. AUDIT_LOG deliberately dirty (4 session-14 mint rows; flush still deferred).

## Resume card — 2026-07-15 (session 13) — Block 2 opened: btb code landed, scope proposal in, qxd+01h+0s7 closed

**HEAD:** wrap on top of `0086e5a`. Shipped (all auditor-PASS): `59268a9` btb OCO root-cause (NT8 cascade artifact) + fail-closed geometry gate + fixture · `113ef5b` Block-2 scope proposal (8 SHM PROPOSALS, 9 spec-gap Qs, CANDIDATE exit checklist) · `31eb6cc` qxd n8n false-failure FIXED prod-verified (Validate error:'' → 0.043s/1 attempt/1 file) · `532f6da` 01h harness no-fire root-cause + RETIRE (DECISION_LOG 19:20Z) · `0086e5a` 0s7 share cleanup (VM report captured, 5 items archived, live path verified).

**Closed:** s1c, qxd, 01h, 0s7. **Open (6):** btb ◐ (code landed; blocked on trader VM sim test + journaling ratification) · **lhw P2 NEW trader-touch** (SIM-QXD-TEST-0001..0004 reached the RUNNING consumer during qxd testing — check Sim101, cancel/flatten) · 10i P2 (trader scope) · 518 P3 monitor-only · 6h7 P4.

**▶ NEXT SESSION:** everything front-of-queue is trader-gated — lhw Sim101 check, btb sim test (redeploy consumer from repo, share copy archived) + ratification, Block-2 Q1 (TV strategy export vs re-implement = toolchain hard blocker), PHASE 3 BUILD SPEC import, 10i scope. First orchestrator dispatches unlock after Q1: Block-2 execution beads per proposal §6.

**⚠️ Sim101:** 11:12 long 1 NQ + bracket still trader's call; plus possible QXD-TEST far-off limits (lhw).

## Resume card — 2026-07-15 (session 12) — 🏁 BLOCK 1 MILESTONE SIGNED OFF; Block 2 opens

**HEAD:** wrap commit on top of `d405125`. Shipped (all auditor-PASS): `228b586` ct5/9tl close evidence (trader GUI-confirmed the 11:12:45 bracket — fill 29820, OCO stop 29741.25/target 29901.25 working, no Log errors; screenshot transcribed, PNG OS-purged) · `d405125` Block-1 milestone evidence audit (all items VERIFIED / T1 TRADER-CONFIRMED / 0 FAIL).

**Trader decisions this session (all recorded):** Block 1 SIGNED OFF (DECISIONS.md entry + Sheets row via clipboard) · §6.2 OnTermination-journaling decline RATIFIED (D-2026-07-15-A) · btb = next-session first dispatch (post-milestone, his call). ct5+9tl CLOSED; 518 dropped to P3 monitor-only (probe negative 3 sessions).

**▶ FIRST DISPATCHES NEXT SESSION:** P0 **btb** (OCO-ID-reuse cascade fix + live-market bracket-geometry pre-validation; sim-test per runbook session-hours guard). P1 Block-2 planning (walk-forward OOS + Monte Carlo scope; SHM threshold PROPOSALS only — trader locks at milestone; PHASE 3 BUILD SPEC import still missing). P2 **10i** scope decision → qxd → 01h → 6h7.

**Open beads (6):** btb P2 · 10i P2 · 518 P3 (monitor-only) · 01h P3 · qxd P3 · 6h7 P4.

**⚠️ Sim101:** the 11:12 long 1 NQ + working bracket may still be live — trader flattens or lets it work (sim-only, untracked).

## Resume card — 2026-07-15 (session 11) — B1-f test matrix GREEN except one trader glance; milestone ask ARMED

**HEAD:** `ec10f58` + this wrap commit. Block 1. Shipped (all auditor-PASS): `d78e6ef` di9 runbook §6 session-hours guard · `5a05a67` T2-DUPLICATE/T3/T4-no-replay evidence · `ec10f58` corrected-geometry T1 ACCEPTED + honest 10:35 bracket-failure record. (07-14: `b17d1c4`, `ae1da60`.)

**Scoreboard:** T2 dedupe PASS · T3 PASS · T4 no-replay PASS (NT8 restarted 9:43, enable 10:31:58, zero replays) · T1 ACCEPTED 15:12:45Z with correct geometry (29821.25 / stop 29741.25 / target 29901.25) — **GUI standing-bracket confirm is the SOLE remaining ct5 evidence** (trader never answered before close).

**⚠️ OPEN SIM POSITION:** long 1 NQ 09-26 + working bracket likely still LIVE on Sim101 from 11:12 ET. First thing: trader flattens or lets it work. Sim-only, no real risk.

**▶ FIRST DISPATCHES NEXT SESSION:** P0 ask trader: "did the 11:12 bracket stand — entry + stop 29741.25 + target 29901.25, no Log errors?" → on YES close **ct5** then **9tl** (dep order; 9tl evidence already audited), un-dep ct5 from 518 → **Block-1 milestone ask (trader-gated, never self-certify)**. P1 **btb** (P2 bug: OCO-ID-reuse cascade after stop-leg reject + add bracket-geometry pre-validation; not dep-linked to ct5). P2 **10i** trader scope decision, then qxd/6h7/01h; AUDIT_LOG flush still overdue (unstaged working-tree rows, grew again this session).

**Open beads (8):** ct5 (blocked: 1 trader answer) · 9tl (closes right after ct5) · btb P2 · 518 P2 (probe negative, near monitor-only) · 10i P2 · 01h P3 (VM harness no-fire) · qxd P3 · 6h7 P4. Closed this session: 8tz, di9.

**Ratification pending:** runbook §6.2 OnTermination-journaling DECLINE recommendation (trader yes/no).

## Resume card — 2026-07-14 (session 10) — ✅ B1-f consumer STARTED on Sim101; T1–T4 in the harness's hands

**HEAD:** session-10 wrap on top of `63aa234`. Block 1. Docs+ledger session; no repo code changed.

**What happened:** attended GUI session, trader driving NT8, orchestrator step-coaching. Consumer went from never-started to RUNNING (journal `praxis-processed-signals.log` + `processed/`, `rejected/` dirs created 15:23 ET = StartConsumer on a Sim account). Four faults cleared in sequence — all config, zero code defects: clipboard-corrupt paste (file-replace fix, sha `e4581f4a`), DEMO1628771 display-renamed as "sim101" (wall REFUSED correctly, rename undone), chart on MNQ not NQ (switched to NQ 09-26), and the root of "no Sim101 exists": **Multi-provider mode was OFF** (Tools>Options>General; forum-confirmed) — enabled + restart made Sim101 appear. Bead **518 storm probe NEGATIVE** all session (~107KB traces vs GBs on 07-12). VM coworker did read-only forensics only — **NT8 was granted at read-only tier**; its blocked report overwrote-in-spirit `b1f-t1-t4-report-2026-07-14.md` (pre-STARTED findings).

**▶ FIRST ACTIONS NEXT SESSION:**
1. Check `~/praxis-signals/b1f-t1-t4-report-2026-07-14.md` + journal contents: journal appearance was the armed harness go-signal → T1–T3 should have run unattended; T4 needs an NT8 restart (trader, or raise coworker NT8 permission from read-only to full control — briefs already on the share authorize it).
2. On T2/T4 PASS: close **ct5+9tl**, un-dep ct5 from 518 (drop 518 to monitor-only) → **Block-1 milestone ask** (trader-gated).
3. Then: **10i** trader scope decision → **qxd** (P3) → **6h7** (P4) → AUDIT_LOG flush (overdue, ~11 stranded rows).

**Open beads (6):** `ct5` (in_progress, consumer LIVE, awaiting T1–T4 evidence) · `9tl` (closes with ct5) · `518` (P2, probe negative — near monitor-only) · `10i` · `qxd` · `6h7`.

**Operational notes:** AUDIT_LOG.md deliberately dirty (flush next session). Trader-workflow memory saved: anything he must hand off goes to clipboard via pbcopy automatically. Coworker briefs live at `~/praxis-signals/BRIEF-2026-07-14-*.md`.

## Resume card — 2026-07-12 (session 9 cont.) — 🔬 NT8 WPF storm root-caused + cleared (518); VM harness ARMED, awaiting trader GUI steps

**HEAD:** session-9-cont wrap on top of `2294d0e`. Block 1. Docs+ledger session; no code.

**What happened after the first session-9 wrap:**
- VM coworker aborted its run correctly: NT8 WPF layout was throwing `NotSupportedException` in DirectWrite `GetDesignGlyphMetrics` on EVERY layout pass since 11:20 → no new window/menu/dialog could render for ANYONE (human included), trace storm 231 MB/min (3.98 GB total). The prior "input injection broken" diagnosis was wrong — bead **518 rescoped** (P2) with full stack signature; ct5 dep-linked to it. T1–T4 honestly recorded NOT RUN (never FAIL — strategy never started). Blocked report collected: `docs/reports/2026-07-12-b1f-t1-t4-vm-run-blocked.md` (+ MANIFEST row).
- Trader restarted NT8 → **STORM CLEAR** (pid 9672, 0 bytes trace in 5 min vs 231 MB/min; process-state fault, not VM-level). Coworker deleted 23 storm trace files (3.98 GB freed) and re-armed the automated harness: journal-file go-signal → T1–T3 unattended → `NEEDS-TRADER-T4-RESTART.txt` handshake → final report to the share.
- Unknown trigger remains: storm began at the first Connections click — trader's GUI session is the recurrence probe (518 notes).

**▶ FIRST ACTIONS NEXT SESSION (trader wants to discuss before executing):**
1. Check `~/praxis-signals/b1f-t1-t4-report-2026-07-12.md` — if the run completed: collect → verify → close **ct5+9tl** on T2/T4 pass → un-dep ct5, drop 518 to monitor-only → **Block-1 milestone ask**. If storm re-ignited: 518 becomes critical path (font-stack investigation).
2. **TRADER DECISION (10i):** scope A/B/C → DECISIONS.md.
3. Dispatchable: **qxd** (P3 n8n retry bug), **6h7** (P4 template), **518** follow-up per outcome.

**Open beads (6):** `ct5` (in_progress, blocked-by 518 dep — remove after clean GUI run) · `9tl` · `10i` · `qxd` · `6h7` · `518` (P2, monitor/investigate per outcome).

**Operational notes:** AUDIT_LOG.md still deliberately dirty (~10 stranded rows incl. two session-9 wraps) — flush is getting due. VM harness logs: `%TEMP%\praxis-phase0-watch.log` in the VM. Warp TCC lockout fix (session-9 card) held all session.

## Resume card — 2026-07-12 (session 9) — 🔄 B1-f T1-T4 delegated to VM Claude coworker, run IN FLIGHT; no code shipped

**HEAD:** session-9 wrap commit on top of `bf25592` (session-8 wrap). Block 1 (Foundation, Build-First). Docs-only session.

**What happened:**
- Session opened locked out: Warp lost TCC access to /Volumes (all external volumes "Operation not permitted"); trader re-granted Full Disk Access — if it recurs, that's the fix.
- **B1-f T1-T4 delegated** (trader-directed) to a Claude coworker agent controlling the Win11 VM; brief = runbook rewritten agent-executable (this session's transcript + DECISION_LOG 2026-07-12T18:25Z).
- Coworker preflight caught 3 real issues, all resolved: (1) `.cs` wasn't staged (orchestrator omission) — staged to `~/praxis-signals/` at 11:17 (sha `e4581f4a`, git-clean source) and pulled into the VM by the coworker ~11:20, share copy deleted per brief Step 2.1; (2) stale B1-b signal `SIM-B1B-0001.json` would have fired an unplanned Sim101 order on first scan — archived to `~/praxis-signals/archive/`; (3) suspected 1s sweep-daemon race — REFUTED by reading deployed sweep source (outbox → incoming/ → drop ROOT; root is final, never swept). Daemon untouched.
- New bead **6h7** (P4): `signal-template.json` stale schema.

**▶ FIRST ACTIONS NEXT SESSION:**
1. Collect `~/praxis-signals/b1f-t1-t4-report-2026-07-12.md` → docs/reports/; verify vs runbook; on T2/T4 pass close **ct5 + 9tl** → Block-1 milestone ask (trader-gated).
2. **TRADER DECISION (10i):** scope A/B/C → DECISIONS.md → open build bead.
3. Dispatchable: **qxd** (P3, n8n write-node false-failure retry; test workflow first).

**Open beads (5):** `ct5` (in_progress, VM run in flight) · `9tl` (closes with ct5) · `10i` (trader decision) · `qxd` (P3) · `6h7` (P4 template nit).

**Operational notes:** AUDIT_LOG.md still deliberately dirty (~8 stranded rows + this wrap row) — flush per runbook when convenient. Sim101 was not visible in the VM because NT8 wasn't connected — coworker instructed to connect Simulated Data Feed first.

## Resume card — 2026-07-12 (session 8) — ✅ bug backlog swept: 587 + fz6 + 8xf CLOSED; relay re-architected + deployed live; qxd filed

**HEAD:** wrap commit on top of `a6ce1c4` (8xf daemon) ← `294287d` (fz6) ← `8a872d9` (587) ← `a91cee9`. Pushed. Block 1 (Foundation, Build-First).

**Shipped:**
- `8a872d9` — **587 CLOSED:** gate form-check matcher anchored at command position (BINPRE path/backslash prefix); no more free-text false denials; 27/27 gate tests. One audit-FAIL round: first fix opened `/usr/bin/git`-style bypasses, auditor caught it, J8–J11 regression class added.
- `294287d` — **fz6 CLOSED:** B1-f nits — readAttempts purged on all 7 terminal dispositions (MoveTo chokepoint); entrySignal >40ch gets FNV-1a-32 hash suffix (no prefix collisions; ≤40ch ids byte-identical). T1–T4 in the VM will exercise this updated source.
- `a6ce1c4` — **8xf CLOSED (D-2026-07-12-A):** relay re-architected WatchPaths → persistent KeepAlive 1s-sweep daemon, DEPLOYED LIVE (installer v3, legacy job removed, kill-restart verified). Bursts 6/6 <5s, max ~1.0s (was 3/6 FAIL, max 9.15s). Investigation report reclassified B1-d's ~4.3s as a blocking-curl artifact — real cause was n8n write-node false-failure retry (2×2s + triple writes) → filed as **qxd** (P3).

**▶ FIRST ACTIONS NEXT SESSION:**
1. **TRADER-TOUCH (ct5/9tl):** in-VM compile + T1–T4 per docs/runbooks/2026-07-10-b1f-nt8-consumer-install.md → close ct5+9tl → Block-1 milestone ask.
2. **TRADER DECISION (10i):** scope A/B/C → DECISIONS.md → open build bead.
3. **Dispatchable: qxd** (P3, n8n write-node false-failure retry) — prod n8n workflow edit; verify on a test workflow first; 30s diagnostic in docs/reports/2026-07-12-8xf-latency-investigation.md.

**Open beads (4):** `ct5` (in_progress, trader-touch) · `9tl` (P2, closes with ct5) · `10i` (P2, trader decision) · `qxd` (P3, above).

**Operational notes:** relay is now the KeepAlive daemon (`build.praxis.signals-sweep-daemon`, internal-disk deploy, rollback in report §6). AUDIT_LOG.md carries ~8 stranded rows through session 8 — flush per runbook when convenient. Session 8 fired 12 clearly-TEST-marked Telegram notifications during latency probes — ignore them. RUN_DECISIONS.md (07-09 autonomous-run record) committed in this wrap.

## Resume card — 2026-07-10 (session 7) — ✅ 30h flush LANDED; 10i design doc SHIPPED; B1-f consumer source BUILT — Block 1 build work done, trader-touch remains

**HEAD:** wrap commit on top of `ed2bc9e` (ct5 consumer) ← `b3dbb99` (10i design) ← `562e7bd` (30h flush) ← `19b324f`. Pushed. Block 1 (Foundation, Build-First).

**Shipped:**
- `562e7bd` — **30h CLOSED:** first AUDIT_LOG flush — 19 rows through 2026-07-10T19:38:09Z, auditor FLUSH-MODE PASS (flush-verify exit 0, 3 row spot-checks, VOID 19927e89 annotation verified). The rolling-row pattern works as designed.
- `b3dbb99` — **10i design doc** (bead OPEN, `human`-labeled): docs/design/2026-07-10-10i-telegram-inbound-control.md — B1-c launchd pattern reuse, JSON command-file spec, scope options A/B/C with TRADER DECISION REQUIRED (A = read/report/status only, recommended), 10 security controls, TCC internal-disk layout. Build bead opens only after the trader records the scope choice in DECISIONS.md.
- `ed2bc9e` — **B1-f consumer source (bead ct5 OPEN, `human`-labeled):** ninjascript/PraxisSignalConsumer.cs — SIM-only account guard (re-asserted at submit), FSW + startup scan + 15s rescan, strict hand-rolled parser, 9tl in-file signal_id dedup (journal-before-submit = at-most-once, restart-safe), bracket orders both sides, rejected/+processed/ dispositions. Static audit PASS. Install runbook + T1-T4 test plan: docs/runbooks/2026-07-10-b1f-nt8-consumer-install.md.

**▶ FIRST ACTIONS NEXT SESSION (both trader-touch/trader-decision):**
1. In the NT8 VM: compile PraxisSignalConsumer.cs, run T1-T4 per the runbook → close ct5 + 9tl → Block-1 milestone ask.
2. 10i scope decision (A recommended) → DECISIONS.md entry → open the build bead.

**Open beads (6):** `ct5` (P2, trader-touch T1-T4) · `9tl` (P2, closes with ct5 T2/T4) · `10i` (P2, trader scope decision) · `587` (P3, attended gate fix) · `8xf` (P3) · `fz6` (P4 NEW — B1-f nits: readAttempts purge on reject; entrySignal 40-char truncation collision).

**Operational notes:** consumer assumes in-VM path `Z:\praxis-signals` (parameterized; scoped-share `\\Mac\praxis-signals` still an unapplied trader TODO) and default 40/80-tick stop/target when the payload has none — placeholder until the TV alert schema lands. AUDIT_LOG.md again carries stranded rows by design (session-7 mints); flush per runbook when they accumulate. 587 phrasing caution still applies.

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
