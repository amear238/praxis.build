# Project: PRAXIS — Automated NQ Futures Trading System
**Last updated:** 2026-07-09 (Block 1 design finalized — WireGuard + Parallels decisions recorded)

## Current Phase
Block 0 of 6 — Infrastructure Setup (Prerequisite)

## Current Step
Block 1 design FINALIZED. Trader answered the 3 open questions (2026-07-09): Mac behind residential NAT; tunnel = plain WireGuard; NT8 host = Parallels Windows 11 ARM VM now / native x64 Windows PC before Block 5. Recorded as D-2026-07-09-A (WireGuard) and D-2026-07-09-B (Parallels/native-PC). Block 1 beads B1-0..B1-e queued and dependency-wired. Still planning/ledger only — no build dispatched.

## Blockers
- Block 0 milestone trader sign-off required before any Block 1 build dispatch (gate F-1/F-3). Block 0 milestone box stays UNCHECKED until signed.
- Explicit Block 1 design sign-off required (design is trader-parameter-confirmed but not yet build-authorized).

## Next Action When Resuming
1. Read this file + HANDOFF.md resume card
2. Trader: sign off Block 0 milestone (all 8 steps done) AND explicitly sign off the Block 1 delivery design
3. On both sign-offs: dispatch B1-0 first (NT8-on-Parallels validation spike — gates B1-c) and B1-a (WireGuard mesh — no deps) in parallel; downstream B1-b/B1-c/B1-d/B1-e unblock per dependency edges

## Recent Decisions
- 2026-05-08 — Git repo initialized at /Volumes/Sensidine/Praxis.build/, pushed to GitHub as amear238/praxis.build (DECISIONS.md#decision-1)
- 2026-05-08 — Local server architecture confirmed over VPS. No cloud API in execution stack. (DECISIONS.md#decision-2)
- 2026-07-04 — D-2026-07-04-A: Build-first reorder. Education no longer a Block 1 prerequisite; comprehension gate moved to pre-live, gating Block 5 (recorded debrief pass/fail).
- 2026-07-04 — D-2026-07-04-B: Strategy Health Monitor added (docs/specs/STRATEGY_HEALTH_MONITOR_SPEC.md). Thresholds locked at Block 2 milestone; built in Block 3; live before Block 5 Phase A.
- 2026-07-08 — D-2026-07-08-A: Coworker visibility via GitHub read access, not Drive sync. Drive-for-Desktop dropped from Step 0.7; Google Sheets tracker retained.
- 2026-07-09 — D-2026-07-09-A: Block 1 tunnel = plain WireGuard (over Tailscale) — no third-party coordination plane, satisfies "no cloud API in execution stack". Applies to B1-a.
- 2026-07-09 — D-2026-07-09-B: NT8 host = Parallels Windows 11 ARM VM now (Apple Silicon = no Boot Camp) / dedicated native x64 Windows PC required before Block 5 live. NT8 x86-under-emulation UNPROVEN — validated by B1-0. Signals delivered into a folder shared into the VM.

## Phase Progress
- [ ] Block 0 — Infrastructure Setup (current)
  - [x] 0.1 Git repo init + GitHub push
  - [x] 0.2 Template files created (CLAUDE.md, STATUS.md, DECISIONS.md, MANIFEST.md, README.md)
  - [x] 0.3 Beads installation + Claude Code hooks
  - [x] 0.4 Google Sheets dashboard
  - [x] 0.5 n8n webhook configuration
  - [x] 0.6 n8n Telegram notification workflow
  - [x] 0.7 Coworker visibility — via GitHub read access (trader confirmed 2026-07-08); Drive sync dropped per D-2026-07-08-A
  - [x] 0.8 Full-loop verification test (verified via remote /tmp/praxis-signals — local delivery is Block 1; see docs/reports/2026-07-08-step-0.8-full-loop.md)
- [ ] Block 1 — Foundation (Build-First — education runs parallel, gate moved to pre-live per D-2026-07-04-A)
- [ ] Block 2 — Backtesting
- [ ] Block 3 — Circuit Breakers (includes Strategy Health Monitor per D-2026-07-04-B)
- [ ] Block 4 — Paper Trading
- [ ] Block 5 — Graduated Live (comprehension gate: recorded debrief pass required before live — D-2026-07-04-A)
- [ ] Block 6 — Satellite Strategies
