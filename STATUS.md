# Project: PRAXIS — Automated NQ Futures Trading System
**Last updated:** 2026-07-09 (Block 0 milestone trader-signed-off; repo advanced to Block 1)

## Current Phase
Block 1 of 6 — Foundation (Build-First)

## Current Step
Block 1 kickoff. B1-0 (NT8-on-Parallels validation spike) and B1-a (WireGuard tunnel) are ready; both are hands-on-trader-machine setup. Block 0 milestone was trader-signed-off 2026-07-09 (independent audit 5 VERIFIED / 3 trader-confirmed / 0 FAIL) — the entry condition for Block 1 is met.

## Blockers
- B1-0/B1-a require trader-machine setup — Parallels + Windows 11 ARM + NinjaTrader 8 install (B1-0); WireGuard on n8n host + Mac (B1-a).

## Next Action When Resuming
1. Start B1-0: guide trader through Parallels + Windows 11 ARM + NT8 install, then validate NT8 launches, connects a sim feed, and reads a file from a Mac->VM shared folder.
2. B1-a: stand up the WireGuard tunnel (n8n host + Mac).

## Recent Decisions
- 2026-05-08 — Git repo initialized at /Volumes/Sensidine/Praxis.build/, pushed to GitHub as amear238/praxis.build (DECISIONS.md#decision-1)
- 2026-05-08 — Local server architecture confirmed over VPS. No cloud API in execution stack. (DECISIONS.md#decision-2)
- 2026-07-04 — D-2026-07-04-A: Build-first reorder. Education no longer a Block 1 prerequisite; comprehension gate moved to pre-live, gating Block 5 (recorded debrief pass/fail).
- 2026-07-04 — D-2026-07-04-B: Strategy Health Monitor added (docs/specs/STRATEGY_HEALTH_MONITOR_SPEC.md). Thresholds locked at Block 2 milestone; built in Block 3; live before Block 5 Phase A.
- 2026-07-08 — D-2026-07-08-A: Coworker visibility via GitHub read access, not Drive sync. Drive-for-Desktop dropped from Step 0.7; Google Sheets tracker retained.
- 2026-07-09 — D-2026-07-09-A: Block 1 tunnel = plain WireGuard (over Tailscale) — no third-party coordination plane, satisfies "no cloud API in execution stack". Applies to B1-a.
- 2026-07-09 — D-2026-07-09-B: NT8 host = Parallels Windows 11 ARM VM now (Apple Silicon = no Boot Camp) / dedicated native x64 Windows PC required before Block 5 live. NT8 x86-under-emulation UNPROVEN — validated by B1-0. Signals delivered into a folder shared into the VM.
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
- [ ] Block 1 — Foundation (current — Build-First; B1-0..B1-e queued; education runs parallel, gate moved to pre-live per D-2026-07-04-A)
- [ ] Block 2 — Backtesting
- [ ] Block 3 — Circuit Breakers (includes Strategy Health Monitor per D-2026-07-04-B)
- [ ] Block 4 — Paper Trading
- [ ] Block 5 — Graduated Live (comprehension gate: recorded debrief pass required before live — D-2026-07-04-A)
- [ ] Block 6 — Satellite Strategies
