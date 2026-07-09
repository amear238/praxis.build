# Build Manifest — PRAXIS

| File Path | Type | Phase | Date Created | Purpose |
|-----------|------|-------|-------------|---------|
| /.gitignore | Config | 0 | 2026-05-08 | Git ignore patterns |
| /CLAUDE.md | Config | 0 | 2026-05-08 | Agent context injection — read every session |
| /STATUS.md | State | 0 | 2026-05-08 | Current project state — rewritten each session |
| /DECISIONS.md | Log | 0 | 2026-05-08 | Append-only architectural decision record |
| /MANIFEST.md | Log | 0 | 2026-05-08 | Append-only file creation registry |
| /README.md | Docs | 0 | 2026-05-08 | Project overview and quick links |
| /signals/ | Data | 0 | 2026-05-11 | TradingView signal drop dir; gitignored payloads |
| /docs/reports/2026-05-11-sess2-step-0.5-webhook.md | Report | 0 | 2026-05-11 | Block 0 step 0.5 subagent report |
| /docs/reports/2026-05-11-sess2-step-0.6-telegram.md | Report | 0 | 2026-05-11 | Block 0 step 0.6 subagent report |
| /docs/specs/STRATEGY_HEALTH_MONITOR_SPEC.md | Spec | 3 | 2026-07-08 | Strategy Health Monitor spec (D-2026-07-04-B); thresholds locked at Block 2 milestone |
| /docs/specs/praxis-build-manager_SKILL_outline.md | Spec | 1 | 2026-07-08 | praxis-build-manager skill outline (build-first reorder, D-2026-07-04-A) |
| /.claude/hooks/ | Config | 0 | 2026-07-08 | Orchestrator-mine v3 enforcement hooks (commit gate, audit, notify, handoff, stop gate) |
| /.claude/agents/orchestrator-auditor.md | Config | 0 | 2026-07-08 | Read-only auditor agent — grades diffs, mints commit tokens |
| /AUDIT_LOG.md | Log | 0 | 2026-07-08 | Append-only audit trail, written by audit-approve.sh only |
| /.claude/skills/praxis-build-manager/SKILL.md | Skill | 1 | 2026-07-08 | PRAXIS build orchestration skill, DRAFT v0.1 — live after trader dry-run sign-off |
| /docs/design/2026-07-08-block1-signal-delivery.md | Design | 1 | 2026-07-08 | Block 1 signal delivery proposal (SFTP push recommended); "Resolved — 2026-07-09" section appended (WireGuard + Parallels VM target, D-2026-07-09-A/B) — pending Block 1 sign-off |
| /docs/reports/2026-07-09-block1-design-finalized.md | Report | 1 | 2026-07-09 | Block 1 design finalization report (bead elo) — WireGuard/Parallels decisions recorded, beads B1-0..B1-e queued |
| /docs/reports/2026-07-09-block0-milestone-audit.md | Report | 0 | 2026-07-09 | Block 0 milestone independent audit (bead 9m3) — 5 VERIFIED / 3 trader-confirmed / 0 FAIL; informed trader Block 0 sign-off |
| /docs/reports/2026-07-08-integrate-jul4-update.md | Report | 0 | 2026-07-08 | Jul 4 update integration report (bead 8jq) |
| /docs/reports/2026-07-08-orch-notify.md | Report | 0 | 2026-07-08 | Orchestrator Telegram notify path report (bead w7b) |
| /docs/reports/2026-07-08-step-0.7-drive-folder.md | Report | 0 | 2026-07-08 | Step 0.7 Drive-side prep report (bead rnu) |
| /docs/reports/2026-07-08-step-0.8-full-loop.md | Report | 0 | 2026-07-08 | Step 0.8 full-loop verification report (bead v5h) |
| /docs/reports/2026-07-08-build-manager-skill-draft.md | Report | 1 | 2026-07-08 | Skill draft report (bead e8c) |
| /docs/reports/2026-07-08-block1-delivery-design.md | Report | 1 | 2026-07-08 | Block 1 delivery design report (bead amd) |
| /docs/briefs/2026-07-09-b1-0-coworker.md | Brief | 1 | 2026-07-09 | Coworker dispatch brief for B1-0 (bead 3i7) — NT8-on-Parallels validation, C2/C3/C4 checkpoints |
| /docs/design/2026-07-09-b1-a-wireguard-ssh-runbook.md | Design | 1 | 2026-07-09 | B1-a prep runbook (bead dgt.1) — copy-paste WireGuard wg0.conf templates (VPS + Mac) + scoped SSH forced-command (rrsync/internal-sftp) + macOS sshd tunnel-bind; placeholders only, no live keys |
| /docs/reports/2026-07-09-b1-a-prep-runbook.md | Report | 1 | 2026-07-09 | B1-a prep implementer report (bead dgt.1) — design choices, rrsync-vs-internal-sftp recommendation, macOS caveats, 3-step VERIFY checklist mapping to B1-a acceptance |
