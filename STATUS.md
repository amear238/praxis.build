# Project: PRAXIS — Automated NQ Futures Trading System
**Last updated:** 2026-07-09 (B1-0 NT8-on-Parallels validation PASS + closed; B1-a prep runbook shipped)

## Current Phase
Block 1 of 6 — Foundation (Build-First)

## Current Step
B1-0 closed — NT8-on-Parallels validated (C2/C3/C4 all PASS; commit 6909b96). NT8 8.1.7.2 runs under x64 emulation, streams real-time data, FSW file-drop detection 130-264ms at 100%. D-2026-07-09-B (build-first on Parallels) is now confirmed viable; native x64 mini-PC stays a pre-Block-5 item, not escalated. Next up: B1-a (WireGuard tunnel — turnkey runbook ready) and B1-c (Mac signals layout + scoped VM share), both hands-on live-machine work.

## Blockers
- B1-a and B1-c require live-machine access (WireGuard on n8n host + Mac; Parallels share config + launchd on the Mac). Not autonomously runnable — need trader/coworker at the machines.

## Next Action When Resuming
1. Execute B1-a: stand up the WireGuard tunnel + scoped SSH using docs/design/2026-07-09-b1-a-wireguard-ssh-runbook.md (both wg0.conf templates, keygen, sshd tunnel-bind, rrsync forced-command). Fill in the placeholder table (VPS IP, WG port, 4 keys, signals dir).
2. B1-c: create ~/praxis-signals/ on the Mac and scope the Parallels VM share to THAT dir only (the B1-0 spike shared the whole home dir via \\psf\Home — tighten it); add launchd reconciliation.
3. Optional: import PHASE 3 BUILD SPEC + reconcile the Google Sheet's Block-1 naming (Education/Build split vs beads' Build-First).

## Recent Decisions
- 2026-05-08 — Git repo initialized at /Volumes/Sensidine/Praxis.build/, pushed to GitHub as amear238/praxis.build (DECISIONS.md#decision-1)
- 2026-05-08 — Local server architecture confirmed over VPS. No cloud API in execution stack. (DECISIONS.md#decision-2)
- 2026-07-04 — D-2026-07-04-A: Build-first reorder. Education no longer a Block 1 prerequisite; comprehension gate moved to pre-live, gating Block 5 (recorded debrief pass/fail).
- 2026-07-04 — D-2026-07-04-B: Strategy Health Monitor added (docs/specs/STRATEGY_HEALTH_MONITOR_SPEC.md). Thresholds locked at Block 2 milestone; built in Block 3; live before Block 5 Phase A.
- 2026-07-08 — D-2026-07-08-A: Coworker visibility via GitHub read access, not Drive sync. Drive-for-Desktop dropped from Step 0.7; Google Sheets tracker retained.
- 2026-07-09 — D-2026-07-09-A: Block 1 tunnel = plain WireGuard (over Tailscale) — no third-party coordination plane, satisfies "no cloud API in execution stack". Applies to B1-a.
- 2026-07-09 — D-2026-07-09-B: NT8 host = Parallels Windows 11 ARM VM now (Apple Silicon = no Boot Camp) / dedicated native x64 Windows PC required before Block 5 live. **NT8 x86-under-emulation now PROVEN VIABLE — B1-0 validation PASS (docs/reports/2026-07-09-b1-0-nt8-parallels-validation.md).** Signals delivered into a folder shared into the VM.
- 2026-07-09 — Block 0 milestone — trader sign-off (Amear), 2026-07-09. Independent audit 5 VERIFIED / 3 trader-confirmed / 0 FAIL. Evidence: docs/reports/2026-07-09-block0-milestone-audit.md.

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
- [ ] Block 1 — Foundation (current — Build-First; education runs parallel, gate moved to pre-live per D-2026-07-04-A)
  - [x] B1-0 NT8-on-Parallels validation spike (PASS 2026-07-09 — commit 6909b96)
  - [ ] B1-a WireGuard tunnel + scoped SSH (prep runbook done; live bring-up pending)
  - [ ] B1-b n8n SCP-push node (blocked on B1-a)
  - [ ] B1-c Mac signals layout + scoped VM share + launchd reconciliation (unblocked)
  - [ ] B1-d end-to-end sim latency + idempotency test
  - [ ] B1-e offline failure drill
- [ ] Block 2 — Backtesting
- [ ] Block 3 — Circuit Breakers (includes Strategy Health Monitor per D-2026-07-04-B)
- [ ] Block 4 — Paper Trading
- [ ] Block 5 — Graduated Live (comprehension gate: recorded debrief pass required before live — D-2026-07-04-A)
- [ ] Block 6 — Satellite Strategies
