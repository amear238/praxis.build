# Project: PRAXIS — Automated NQ Futures Trading System
**Last updated:** 2026-07-08 (Jul 4 update integrated)

## Current Phase
Block 0 of 6 — Infrastructure Setup (Prerequisite)

## Current Step
0.7: n8n Telegram notification nodes added. Next: Coworker folder connection.

## Blockers
- None

## Next Action When Resuming
1. Read this file
2. Create Google Sheets dashboard (Step 0.4)
3. Configure n8n webhook (Step 0.5)
4. Configure n8n Telegram notifications (Step 0.6)
5. Verify Coworker folder connection (Step 0.7)
6. Run full-loop verification test (Step 0.8)

## Recent Decisions
- 2026-05-08 — Git repo initialized at /Volumes/Sensidine/Praxis.build/, pushed to GitHub as amear238/praxis.build (DECISIONS.md#decision-1)
- 2026-05-08 — Local server architecture confirmed over VPS. No cloud API in execution stack. (DECISIONS.md#decision-2)
- 2026-07-04 — D-2026-07-04-A: Build-first reorder. Education no longer a Block 1 prerequisite; comprehension gate moved to pre-live, gating Block 5 (recorded debrief pass/fail).
- 2026-07-04 — D-2026-07-04-B: Strategy Health Monitor added (docs/specs/STRATEGY_HEALTH_MONITOR_SPEC.md). Thresholds locked at Block 2 milestone; built in Block 3; live before Block 5 Phase A.

## Phase Progress
- [ ] Block 0 — Infrastructure Setup (current)
  - [x] 0.1 Git repo init + GitHub push
  - [x] 0.2 Template files created (CLAUDE.md, STATUS.md, DECISIONS.md, MANIFEST.md, README.md)
  - [x] 0.3 Beads installation + Claude Code hooks
  - [x] 0.4 Google Sheets dashboard
  - [x] 0.5 n8n webhook configuration
  - [x] 0.6 n8n Telegram notification workflow
  - [ ] 0.7 Coworker folder connection — Drive-side prep done — awaiting trader: Drive for Desktop install + folder selection (see docs/reports/2026-07-08-step-0.7-drive-folder.md)
  - [x] 0.8 Full-loop verification test (verified via remote /tmp/praxis-signals — local delivery is Block 1; see docs/reports/2026-07-08-step-0.8-full-loop.md)
- [ ] Block 1 — Foundation (Build-First — education runs parallel, gate moved to pre-live per D-2026-07-04-A)
- [ ] Block 2 — Backtesting
- [ ] Block 3 — Circuit Breakers (includes Strategy Health Monitor per D-2026-07-04-B)
- [ ] Block 4 — Paper Trading
- [ ] Block 5 — Graduated Live (comprehension gate: recorded debrief pass required before live — D-2026-07-04-A)
- [ ] Block 6 — Satellite Strategies
