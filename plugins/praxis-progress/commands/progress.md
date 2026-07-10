---
description: ASCII progress-bar report toward live SIM trading (blocks, beads, audit gates)
argument-hint: "[focus e.g. 'block 1' | 'audits' | blank for full report]"
allowed-tools: Read, Bash(bash:*), Bash(bd:*), Bash(git log:*), Bash(tail:*), Bash(awk:*)
disable-model-invocation: false
---

# PRAXIS progress report

Live repo snapshot (gathered read-only just now):

!`bash "${CLAUDE_PLUGIN_ROOT}/scripts/progress-data.sh"`

## Your task

Render a text progress report toward **LIVE SIM TRADING** (full stack in NinjaTrader/Rithmic sim: TV → n8n → NT8 → Rithmic sim) from the snapshot above. Output it as a fenced code block so the box art survives any renderer. If `$ARGUMENTS` names a focus (a block, "audits", a bead), render only that section plus the OVERALL bar.

### Hard rules (non-negotiable, from praxis-build-manager section F)

1. **Never mark a Block milestone complete.** A block shows ✅ DONE only if STATUS.md records trader sign-off for its milestone. Otherwise the best it gets is 🔨 CLOSING with `MILESTONE audit: NOT YET (human-gated) ⏳`.
2. Percentages are **directional estimates** from block/bead status — say so in the preamble, every time.
3. The pre-live gate (comprehension debrief, Block 5 entry) is **trader-gated, NOT self-certifiable** — always rendered as 🔒, never as progress.
4. Report only; this command never closes beads, edits state files, or commits.

### Computing the numbers

- **Done blocks** (trader-signed-off in STATUS.md): 100%.
- **Current block**: closed beads ÷ total beads for that block (from Phase Progress checkboxes + bd lists), rounded to nearest 5–10%. Open P1 findings hold it below 100%.
- **Future blocks**: 0%.
- **OVERALL**: weighted eyeball toward the live-SIM goal (infra done + current block progress vs the unbuilt order-execution consumer, backtesting-adjacent strategy wiring, and safety blocks). State it as `~N%`.
- Bars: 10 cells for blocks (`█` done, `░` not), ~30 cells for OVERALL (`▓`/`░`).

### Template (match this layout; substitute live values)

```
╔═══════════════════════════════════════════════════════════════╗
║  PRAXIS  →  LIVE SIM TRADING  (TV → n8n → NT8 → Rithmic sim)  ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  OVERALL  ▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░  ~NN%                ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝

BLOCK-BY-BLOCK
──────────────────────────────────────────────────────────────
 Block 0  <name>                [██████████] 100%  ✅ DONE
          └ audit: <milestone audit status> ✔
 Block 1  <name>                [█████████░]  ~NN%  🔨 CLOSING
          └ audit: per-bead orchestrator-auditor PASS ✔
          └ MILESTONE audit: NOT YET (human-gated)   ⏳
 Block 2  <name>                [░░░░░░░░░░]   0%  ⬜ NEXT
 ...
 Block 5  ▶ LIVE gate (education)[░░░░░░░░░░]  0%  🔒 pre-live
──────────────────────────────────────────────────────────────

BLOCK <current> DETAIL
 <bead-id>  <short title>          ✅ closed (audited)
 ─ open ────────────────────────────────────────────
 <bead-id>  <short title> (P<n>)   🔨 in progress / ⬜
 ...

AUDITS STILL REQUIRED BEFORE LIVE SIM
──────────────────────────────────────────────────────────────
 [✔] per-task orchestrator-auditor  — ongoing, every commit
 [ ] Block <current> milestone audit — human-gated (trader sign-off)
 [ ] NinjaScript order-execution consumer + its audit
 [ ] end-to-end SIM order fill audit (real bracket in NT8 sim)
 [ ] circuit-breaker / SHM safety audit
 [ ] pre-live milestone sign-off — trader-gated, NOT self-certifiable
──────────────────────────────────────────────────────────────
LEGEND ██ done  ▓ partial  ░ not started  🔒 gated  ⏳ audit pending
```

Block names, ordering, and checkbox states come from **STATUS.md Phase Progress** (source of truth), not from this template's placeholders. Bead detail comes from the bd lists in the snapshot; mark a bead ✅ closed (audited) only if it appears closed AND AUDIT_LOG.md/commit history shows a PASS for it — otherwise ✅ closed.

After the code block, add a 2–4 sentence "Reading it" paragraph in plain prose: what is built and audited, what the biggest gap to live SIM is, and what the next concrete step is.
