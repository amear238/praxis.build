# Project: PRAXIS — Automated NQ Futures Trading System
**Last updated:** 2026-07-09 (session 3 — TOPOLOGY PIVOT to local n8n [D-2026-07-09-D]; B1-c signals layout + launchd + scoped VM share DONE + closed)

## Current Phase
Block 1 of 6 — Foundation (Build-First)

## Current Step
**Topology pivot (D-2026-07-09-D):** n8n runs LOCALLY on the Mac (Docker) for Block-1 build-first; public-ingress (VPS+WireGuard vs tunnel) deferred to pre-live. B1-a WireGuard work is therefore DEFERRED (no remote host to push from); B1-b re-scoped to a local file-write node.
**B1-c CLOSED (commit dc5216c, audited PASS):** ~/praxis-signals layout (incoming/ + final root) + launchd 60s rsync backstop (n8n outbox -> drop dir) + heartbeat + stale-alert, deployed to INTERNAL disk (macOS TCC blocks launchd from the external Sensidine volume — see bd memory). Parallels VM share scoped to /Users/admin/praxis-signals ONLY; whole-home 'admin' share unchecked — B1-0 over-share finding RETIRED (prlctl-confirmed). Sweep live-verified end-to-end (file swept + visible in VM). Next up: B1-b (wire n8n workflow EmMbN4sslwIx1ydn to write signal JSON into the outbox).

## Blockers
- None hard. B1-c-fu (P2): stale-heartbeat Telegram alert verified dry-run only — live-fire pending (ties to open Telegram token rotation). Parallels prlctl share-config is Pro/Business-only; this Mac runs Standard, so VM-share changes are GUI-only (documented).

## Next Action When Resuming
1. **B1-b** (re-scoped, Praxis_build-p7s): point n8n workflow EmMbN4sslwIx1ydn at the local outbox (/Users/admin/n8n-compose/local-files/outbox) so it drops signal JSON there; the launchd sweep relays into ~/praxis-signals for the VM. No SSH/scp.
2. **B1-c-fu**: live-fire the stale-heartbeat alert to confirm Telegram delivery (resolve Telegram creds first if needed).
3. **B1-d**: end-to-end sim latency + idempotency once B1-b lands.
4. Optional: import PHASE 3 BUILD SPEC + reconcile Google Sheet Block-1 naming.

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
  - [~] B1-a WireGuard tunnel + scoped SSH — DEFERRED per D-2026-07-09-D (n8n local; no remote host). Runbook preserved for pre-live ingress.
  - [ ] B1-b n8n LOCAL file-write node (re-scoped; writes into outbox — no scp)
  - [x] B1-c Mac signals layout + scoped VM share + launchd reconciliation (DONE 2026-07-09 — commit dc5216c; whole-home over-share retired)
  - [ ] B1-d end-to-end sim latency + idempotency test
  - [ ] B1-e offline failure drill
- [ ] Block 2 — Backtesting
- [ ] Block 3 — Circuit Breakers (includes Strategy Health Monitor per D-2026-07-04-B)
- [ ] Block 4 — Paper Trading
- [ ] Block 5 — Graduated Live (comprehension gate: recorded debrief pass required before live — D-2026-07-04-A)
- [ ] Block 6 — Satellite Strategies

## Tooling
- 2026-07-10 — `/progress` Claude Code plugin (praxis-progress@praxis-local, bead jpe) installed user-scope: ASCII progress report toward live SIM from STATUS.md + bd + AUDIT_LOG + git. Report-only; milestones stay human-gated. Source: `plugins/praxis-progress/`; after edits run `claude plugin update praxis-progress`. Spec: docs/specs/2026-07-10-praxis-progress-plugin.md
