# Project: PRAXIS — Automated NQ Futures Trading System
**Last updated:** 2026-07-15 (session 13 — Block 2 opened with 4 audited commits: **btb code LANDED** 59268a9 (OCO-reuse root-caused as NT8 managed-bracket cascade artifact — no OCO string in our code; fail-closed market-geometry gate added, bad-geometry signals journal REJECTED-GEOMETRY + rejected/, zero orders; bead stays open on 2 trader touches: VM sim test w/ tests/fixtures/btb-bad-geometry-long.json + journaling-convention ratification). **s1c Block-2 scope proposal** 113ef5b (docs/specs/2026-07-15-block2-backtesting-scope-proposal.md — 8 SHM PROPOSALS, CANDIDATE exit checklist, 9 spec-gap Qs; Q1 = TV strategy export vs re-implement is the Block-2 hard blocker). **qxd CLOSED** 31eb6cc (n8n false-failure: Validate emitted error:'' judged failed by n8n-core retry loop; fixed in prod workflow, webhook 200 now 0.043s/1 attempt/1 file; NEW trader-touch bead lhw — SIM-QXD-TEST-0001..0004 reached the running consumer, check Sim101). **01h CLOSED** 532f6da (harness no-fire = nothing was watching; RETIRED per DECISION_LOG 19:20Z) + **0s7 cleanup CLOSED** 0086e5a (VM report captured, share archived, live path verified). Prior session-12 note follows.) (session 12 — B1-f COMPLETE: trader confirmed the 11:12:45 ET standing bracket in the NT8 GUI (entry filled 29820, stop 29741.25 + target 29901.25 both working, OCO intact, no Log errors — transcribed evidence in docs/reports/2026-07-14-b1f-t1-t3-mac-run.md). T1-T4 all PASS; ct5 + 9tl closed. **BLOCK 1 MILESTONE TRADER-SIGNED-OFF 2026-07-15 (Amear)** on the independent evidence audit d405125; §6.2 OnTermination-journaling decline RATIFIED (D-2026-07-15-A); btb chosen post-milestone, next-session first dispatch. Current block is now Block 2 — Backtesting. ⚠️ Sim101 may still hold the long 1 NQ + working bracket; trader's call. Prior session-9 note follows.) (session 9 cont. — VM run hit an ENVIRONMENT blocker, root-caused + cleared: NT8 WPF DirectWrite glyph-metrics exception storm (bead 518, P2) prevented ANY new window rendering (human or automation) and burned 3.98 GB trace @231 MB/min; earlier "input injection broken" diagnosis was WRONG (clicks proven landing correctly). Trader NT8 restart cleared it — fresh pid 9672 storm-free 0 bytes/5 min, trace bloat cleaned. T1-T4 NOT RUN yet (honest NOT-RUN, not FAIL — strategy never reached Realtime); .cs installed hash-verified. Automated hybrid harness ARMED in VM: journal-file go-signal -> T1-T3 unattended -> NEEDS-TRADER-T4-RESTART.txt handshake -> report. Awaiting trader's 4 GUI steps. Blocked report collected: docs/reports/2026-07-12-b1f-t1-t4-vm-run-blocked.md)

## Current Phase
Block 2 of 6 — Backtesting (Block 1 milestone trader-signed-off 2026-07-15 — DECISIONS.md "Block 1 milestone" entry; evidence audit d405125)

## Current Step
**Block 1 delivery pipe COMPLETE on sim data:** webhook -> local n8n -> atomic outbox write -> persistent KeepAlive 1s-sweep daemon (bursts <5s, was WatchPaths; D-2026-07-12-A) -> ~/praxis-signals -> Parallels VM share. Latency + idempotency verified (B1-d), offline drill passed (B1-e), silent-loss gap closed by stuck-backlog detector (F-B1e-1, 3 launchd agents healthy). **B1-f NinjaScript FileSystemWatcher consumer SOURCE BUILT (ct5, ed2bc9e):** SIM-only account guard, in-file signal_id dedup journal (9tl contract, at-most-once), bracket orders; static audit PASS. **B1-f COMPLETE 2026-07-15:** T1-T4 all PASS (Mac-side runs sessions 10-11 after VM harness no-fire, bead 01h; T2 dedupe DUPLICATE-journaled, T3 malformed rejected, T4 no-replay across the 9:43 restart) and the corrected-geometry T1 bracket trader-confirmed standing in the NT8 GUI (fill 29820, stop 29741.25 + target 29901.25 working, no Log errors). ct5 + 9tl CLOSED. **Block-1 milestone TRADER-SIGNED-OFF 2026-07-15 (Amear)** on evidence audit d405125; §6.2 OnTermination-journaling decline ratified (D-2026-07-15-A). Current step is now **Block 2 planning** (first dispatch next session is btb, trader-chosen). Known-open bugs carried: btb (P2, OCO-reuse cascade + geometry pre-validation), 518 (P3 monitor-only), 01h (P3), qxd (P3).
**2026-07-10 concurrency incident CLOSED:** a commit race between two concurrent sessions briefly misattributed the /progress plugin diff to bead 22r (7f54ba9). Reconciled by single session per HANDOFF plan: e76f5c6 (jpe plugin) + 1c53a18 (22r detector), both freshly audited. Session 6: trader reviewed + ACCEPTED the incident; **v6y CLOSED at fec1722** — audit token now binds the staged tree hash and is re-verified at commit time, tokens strictly single-use, and commits are DENIED while another claude session has cwd in this repo (one-session-per-repo enforced by hook + runbook, no longer just policy).

## Blockers
- None hard. B1-c-fu (P2): stale-heartbeat Telegram alert verified dry-run only — live-fire pending (ties to open Telegram token rotation). Parallels prlctl share-config is Pro/Business-only; this Mac runs Standard, so VM-share changes are GUI-only (documented).

## Next Action When Resuming
1. **Trader touches (nothing else is blocked on the orchestrator):** (a) **lhw (P2):** check NT8 Sim101 for SIM-QXD-TEST-0001..0004 brackets (NQ BUY 1 @20000, far-off limits) placed during the qxd clone-phase test — cancel/flatten; (b) **btb close-out:** attended VM sim test — F5 compile the new consumer (repo sha 8ce01991 post-btb; the old e4581f4a share copy is archived — redeploy from repo), drop tests/fixtures/btb-bad-geometry-long.json, expect REJECTED-GEOMETRY + zero orders (procedure: docs/reports/2026-07-15-btb-oco-geometry-fix.md) + ratify the journaling-of-geometry-rejects convention change; (c) ⚠️ Sim101 11:12 long 1 NQ + bracket (stop 29741.25 / target 29901.25) still trader's call.
2. **Block-2 spec-gap answers (trader):** Q1 — is the TradingView strategy exportable as a signal series or must entry logic be re-implemented for backtesting? (hard blocker for the whole toolchain) + PHASE 3 BUILD SPEC import (verbatim Block-2 milestone text) + pinned cost model. Full list: docs/specs/2026-07-15-block2-backtesting-scope-proposal.md §5.
3. **10i trader decision:** Telegram inbound channel authority scope — Option A (read/report/status only, recommended) vs B/C — docs/design/2026-07-10-10i-telegram-inbound-control.md; record in DECISIONS.md, then the build bead can open.
4. Then: first Block-2 execution beads per the proposal §6 sketch (open after Q1 answered); 6h7 (P4 stale signal-template.json); VM-side harness cleanup items in ~/praxis-signals/VM-CLEANUP-NOTE-2026-07-15.md at next attended VM session; AUDIT_LOG flush when stranded rows accumulate (runbook: docs/runbooks/2026-07-10-audit-log-flush.md).

## Recent Decisions
- 2026-05-08 — Git repo initialized at /Volumes/Sensidine/Praxis.build/, pushed to GitHub as amear238/praxis.build (DECISIONS.md#decision-1)
- 2026-05-08 — Local server architecture confirmed over VPS. No cloud API in execution stack. (DECISIONS.md#decision-2)
- 2026-07-04 — D-2026-07-04-A: Build-first reorder. Education no longer a Block 1 prerequisite; comprehension gate moved to pre-live, gating Block 5 (recorded debrief pass/fail).
- 2026-07-04 — D-2026-07-04-B: Strategy Health Monitor added (docs/specs/STRATEGY_HEALTH_MONITOR_SPEC.md). Thresholds locked at Block 2 milestone; built in Block 3; live before Block 5 Phase A.
- 2026-07-08 — D-2026-07-08-A: Coworker visibility via GitHub read access, not Drive sync. Drive-for-Desktop dropped from Step 0.7; Google Sheets tracker retained.
- 2026-07-09 — D-2026-07-09-A: Block 1 tunnel = plain WireGuard (over Tailscale) — no third-party coordination plane, satisfies "no cloud API in execution stack". Applies to B1-a.
- 2026-07-09 — D-2026-07-09-B: NT8 host = Parallels Windows 11 ARM VM now (Apple Silicon = no Boot Camp) / dedicated native x64 Windows PC required before Block 5 live. **NT8 x86-under-emulation now PROVEN VIABLE — B1-0 validation PASS (docs/reports/2026-07-09-b1-0-nt8-parallels-validation.md).** Signals delivered into a folder shared into the VM.
- 2026-07-09 — D-2026-07-09-C: Signals drop dir = dedicated low-priv path (`/Users/admin/praxis-signals` at execution; praxispush user dropped for local-Docker build-first). Structural least-privilege / clean VM-share boundary.
- 2026-07-09 — D-2026-07-09-D: n8n runs LOCALLY on the Mac for Block-1 build-first; public-ingress topology (VPS+WireGuard vs tunnel) DEFERRED to pre-live. Re-scopes B1-a (deferred) + B1-b (local file-write). Keeps D-2026-07-09-A intact for when ingress returns.
- 2026-07-09 — Block 0 milestone — trader sign-off (Amear), 2026-07-09. Independent audit 5 VERIFIED / 3 trader-confirmed / 0 FAIL. Evidence: docs/reports/2026-07-09-block0-milestone-audit.md.
- 2026-07-12 — D-2026-07-12-A: signals relay moved from launchd WatchPaths (10s respawn throttle broke bursts) to persistent KeepAlive 1s-sweep daemon. B1-d's "~4.3s e2e" reclassified as measurement artifact; true unthrottled delivery ~0.5–1.3s.

## Phase Progress
- [x] Block 0 — Infrastructure Setup (milestone trader-signed-off 2026-07-09)
  - [x] 0.1 Git repo init + GitHub push
  - [x] 0.2 Template files created (CLAUDE.md, STATUS.md, DECISIONS.md, MANIFEST.md, README.md)
  - [x] 0.3 Beads installation + Claude Code hooks
  - [x] 0.4 Google Sheets dashboard
  - [x] 0.5 n8n webhook configuration
  - [x] 0.6 n8n Telegram notification workflow
  - [x] 0.7 Coworker visibility — via GitHub read access (trader confirmed 2026-07-08); Drive sync dropped per D-2026-07-08-A
  - [x] 0.8 Full-loop verification test (verified via remote /tmp/praxis-signals — local delivery is Block 1; see docs/reports/2026-07-08-step-0.8-full-loop.md)
- [x] Block 1 — Foundation (milestone trader-signed-off 2026-07-15; evidence audit docs/reports/2026-07-15-block1-milestone-audit.md, d405125)
  - [x] B1-0 NT8-on-Parallels validation spike (PASS 2026-07-09 — commit 6909b96)
  - [~] B1-a WireGuard tunnel + scoped SSH — DEFERRED per D-2026-07-09-D (n8n local; no remote host). Runbook preserved for pre-live ingress.
  - [x] B1-b n8n LOCAL file-write node (DONE 2026-07-09 — commit b5e022e; atomic .tmp->.json into outbox, 3x/2s retry, Telegram error route)
  - [x] B1-c Mac signals layout + scoped VM share + launchd reconciliation (DONE 2026-07-09 — commit dc5216c; whole-home over-share retired)
  - [x] B1-c-fu stale-heartbeat alert live-fired (7420ae5) · B1-b-fu WatchPaths <5s relay (c19531b)
  - [x] B1-d end-to-end sim latency + idempotency test (PASS 2026-07-10 — d24537c; 4.2-4.3s <5s; findings F1/F2 filed)
  - [x] B1-e offline failure drill (PASS 2026-07-10 — 5822420; spool+replay OK; found F-B1e-1 silent-loss gap — FIXED by stuck-backlog detector, 1c53a18, deployed live)
  - [x] B1-f NinjaScript FileSystemWatcher consumer (DONE 2026-07-15 — source ed2bc9e; T1/T2/T3/T4 all PASS in NT8 sim, standing bracket trader-confirmed in GUI; ct5+9tl closed; evidence docs/reports/2026-07-14-b1f-t1-t3-mac-run.md)
  - [x] **Block 1 MILESTONE — trader-signed-off 2026-07-15 (Amear)** — evidence audit d405125; §6.2 OnTermination-journaling decline RATIFIED (D-2026-07-15-A); known-open carried: btb P2 (next-session dispatch, trader-chosen), 10i P2, 518/01h/qxd P3, 6h7 P4
- [ ] Block 2 — Backtesting (current — entry condition satisfied; planning next session)
- [ ] Block 3 — Circuit Breakers (includes Strategy Health Monitor per D-2026-07-04-B)
- [ ] Block 4 — Paper Trading
- [ ] Block 5 — Graduated Live (comprehension gate: recorded debrief pass required before live — D-2026-07-04-A)
- [ ] Block 6 — Satellite Strategies

## Tooling
- 2026-07-10 — `/progress` Claude Code plugin (praxis-progress@praxis-local, bead jpe) installed user-scope: ASCII progress report toward live SIM from STATUS.md + bd + AUDIT_LOG + git. Report-only; milestones stay human-gated. Source: `plugins/praxis-progress/`; after edits run `claude plugin update praxis-progress`. Spec: docs/specs/2026-07-10-praxis-progress-plugin.md
