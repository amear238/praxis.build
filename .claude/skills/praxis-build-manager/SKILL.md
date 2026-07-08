---
name: praxis-build-manager
description: "PRAXIS build orchestration. Use for ANY session working in the Praxis.build repo: any mention of a build block (Block 0-6), a step number (0.7, 1.2, ...), STATUS.md, MANIFEST.md, DECISIONS.md, Beads/bd tasks, milestones, the signal path (TradingView -> n8n -> NinjaTrader -> Rithmic -> MFFU), circuit breakers, the Strategy Health Monitor (SHM), or n8n-triggered headless build/audit runs. Loads current block state, enforces the build -> verify -> record -> report loop, routes verification to the auditor subagent, and refuses milestone self-certification — milestones are human-gated."
---

# praxis-build-manager

**Status: DRAFT v0.1 — not live until trader dry-run sign-off (outline section 3 step 4).**

Source outline: `docs/specs/praxis-build-manager_SKILL_outline.md` (v0.1).
This skill encodes the PRAXIS block definitions, the per-step execution discipline, and
the audit protocol so every Claude Code session — interactive or headless — executes the
build the same way, resumes from Git-tracked state, and cannot self-certify its own work.
It supplements CLAUDE.md; where CLAUDE.md is stricter, CLAUDE.md wins.

---

## A — Session Boot Sequence (every session, no exceptions)

Run these four steps before doing anything else:

1. **Read `STATUS.md`** — current block, current step, blockers, last verified state.
2. **Read the `DECISIONS.md` tail** (last 5 entries) — pick up any locked constraints
   added since the last session. As of this draft the locked constraints are:
   - **D-2026-07-04-A** — Build-first reorder: Block 1 builds immediately on free sim
     data; education runs in parallel; the comprehension gate moves to pre-live (gates
     Block 5). See section F for the verbatim gate text.
   - **D-2026-07-04-B** — Strategy Health Monitor added: thresholds locked at the
     Block 2 milestone, built in Block 3, live before Block 5 Phase A. Spec:
     `docs/specs/STRATEGY_HEALTH_MONITOR_SPEC.md`.
3. **`bd list`** (Beads) — open tasks for the current block, in order. Use `bd ready`
   to find available work, `bd show <id>` for detail.
4. **State the session plan in <=5 lines, before any other tool call.** If the plan
   exceeds the current block's scope: stop, flag it to the trader, and wait. Do not
   quietly expand scope.

---

## B — Block Definitions (reference table)

> **Provenance note:** exit-milestone wording is supposed to be verbatim from the
> PHASE 3 BUILD SPECIFICATION, which is **not in this repo**. Everything below is
> reconstructed from STATUS.md + DECISIONS.md + the SHM spec. Items marked
> **TBD — needs PHASE 3 BUILD SPECIFICATION import** must be filled from that document
> before this skill goes live; do not invent them.

| Block | Name | Entry condition | Exit milestone | Key decisions applied |
|---|---|---|---|---|
| 0 | Infrastructure Setup (prerequisite) | Project start | All steps 0.1–0.8 verified; full-loop test passes (verbatim milestone text: TBD — needs PHASE 3 BUILD SPECIFICATION import) | — |
| 1 | Foundation | Block 0 milestone trader-verified in STATUS.md | Full Block 1 signal path built and running on free **sim** data (verbatim milestone text: TBD — needs PHASE 3 BUILD SPECIFICATION import) | D-2026-07-04-A: build immediately; education is parallel, NOT a prerequisite |
| 2 | Backtesting | Block 1 milestone trader-verified | Walk-forward OOS distribution + Monte Carlo envelope produced; **SHM thresholds locked via DECISIONS.md entry**; `shm/reference_distributions.json` generated (further milestone text: TBD — needs PHASE 3 BUILD SPECIFICATION import) | D-2026-07-04-B: SHM threshold lock happens here |
| 3 | Circuit Breakers + SHM | Block 2 milestone trader-verified | Nine circuit breakers + Strategy Health Monitor built and each trigger intentionally fired on synthetic data with demotion + notification verified (verbatim milestone text: TBD — needs PHASE 3 BUILD SPECIFICATION import) | D-2026-07-04-B: SHM built here, alongside breakers |
| 4 | Paper Trading | Block 3 milestone trader-verified | Minimum paper sample completed (candidate: 25 trades per SHM spec; exact criteria: TBD — needs PHASE 3 BUILD SPECIFICATION import) | — |
| 5 | Graduated Live | Block 4 milestone trader-verified **AND comprehension gate passed** (recorded debrief, pass/fail — see section F) **AND SHM live** | Graduation phases (Phase A = 1 MNQ, no skipping) per kill criteria (verbatim phase/kill-criteria text: TBD — needs PHASE 3 BUILD SPECIFICATION import) | D-2026-07-04-A comprehension gate; D-2026-07-04-B SHM live before Phase A |
| 6 | Satellite Strategies | Block 5 milestone trader-verified | Replacement-candidate pipeline operating (verbatim milestone text: TBD — needs PHASE 3 BUILD SPECIFICATION import) | SHM retirements draw replacements from here |

Per-block detail:

### Block 0 — Infrastructure Setup (current, per STATUS.md)
- Ordered tasks: 0.1 Git repo init + GitHub push [done]; 0.2 template files [done];
  0.3 Beads + Claude Code hooks [done]; 0.4 Google Sheets dashboard [done];
  0.5 n8n webhook [done]; 0.6 n8n Telegram notifications [done];
  0.7 Coworker folder connection [in progress — **trader-touch task**: Drive for
  Desktop install + folder selection happens on the trader's machine];
  0.8 full-loop verification test.
- Platform annotations (mandatory on every trader-touch task): where the task is
  performed (trader's desktop / n8n UI / Google Sheets) and where output is stored
  (repo report under `docs/reports/`, Sheets row, n8n workflow).
- Scope wall: NO strategy code, NO NinjaScript, NO order routing in Block 0.

### Block 1 — Foundation (build-first)
- Build the full signal path immediately: TradingView alert -> webhook -> n8n workflow
  -> JSON file drop -> NinjaScript FileSystemWatcher -> bracket order — running on
  **sim data only**. The trader learns against the live artifact (D-2026-07-04-A).
- Scope wall: NO live or funded accounts, NO real orders, NO comprehension-gate
  enforcement here (that gate is at Block 5). Task-level breakdown:
  TBD — needs PHASE 3 BUILD SPECIFICATION import.

### Block 2 — Backtesting
- Produce walk-forward out-of-sample distribution and Monte Carlo drawdown/duration
  envelopes. At milestone: lock SHM-1..SHM-5 numeric thresholds via an append-only
  DECISIONS.md entry and generate `shm/reference_distributions.json` (git-tracked,
  immutable). Task-level breakdown: TBD — needs PHASE 3 BUILD SPECIFICATION import.
- Scope wall: threshold values are proposed here and locked by the trader; Claude does
  not lock them unilaterally.

### Block 3 — Circuit Breakers + Strategy Health Monitor
- Build the nine circuit breakers (per-order/intraday operational safety) and the SHM
  (n8n daily post-session workflow, deterministic arithmetic, no LLM in the loop) in
  the same deterministic-safety build slot (D-2026-07-04-B, SHM spec section 5).
- Testing gate: every breaker and every SHM trigger fired intentionally on synthetic
  trade-log data; demotion + Telegram notification verified.
- Scope wall: SHM consumes Block 2 reference distributions; it does not recompute or
  adjust them. Breaker definitions: TBD — needs PHASE 3 BUILD SPECIFICATION import.

### Block 4 — Paper Trading
- Run the full stack on paper; accumulate the minimum sample (candidate 25 trades).
- Scope wall: paper performance, however green, does NOT loosen the comprehension gate
  (named risk in D-2026-07-04-A). Exit criteria: TBD — needs PHASE 3 BUILD
  SPECIFICATION import.

### Block 5 — Graduated Live
- Entry requires ALL of: Block 4 milestone trader-verified; comprehension gate passed
  (section F, verbatim); SHM live and verified. Phase A = 1 MNQ; re-promotions after
  SHM demotion always restart at Phase A, no skipping (SHM spec section 4).
- Phase ladder and kill criteria: TBD — needs PHASE 3 BUILD SPECIFICATION import.

### Block 6 — Satellite Strategies
- Candidate pipeline supplying replacements when SHM review concludes decay and a
  strategy is retired (retirement is a normal lifecycle event).
- Detail: TBD — needs PHASE 3 BUILD SPECIFICATION import.

---

## C — Step Execution Loop (the core discipline)

For every build step, in order, no skipping:

1. **Build** — the smallest complete unit of work for the current step.
2. **Verify** — hand off to the auditor subagent (section D). The builder never grades
   its own work. No auditor PASS on record, no step 3.
3. **Record** — update STATUS.md (rewrite), append to MANIFEST.md, `bd close <id>`,
   commit with a conventional message referencing the Beads ID. Note: while the
   orchestrator gate is armed (`.claude/state/orchestrator-active` exists), the
   installed `gate-commit.sh` hook additionally requires the auditor's single-use
   token for the exact staged diff — stage first, commit plain (`git commit -m`),
   no `-a`/`--amend`.
4. **Report** — one-line Telegram note via the n8n webhook (`ORCH_N8N_WEBHOOK`,
   `.claude/hooks/notify.sh`) on step completion.

Enforcement is deterministic (hooks), not aspirational (instructions) — see section E.

---

## D — Auditor Handoff

This repo already ships an auditor subagent: **`.claude/agents/orchestrator-auditor.md`**.
Use it. Do NOT create or reference a `praxis-auditor` agent — the outline's separate
auditor is superseded by the installed orchestrator-auditor pattern.

- The orchestrator-auditor is read-only (Write/Edit/NotebookEdit disallowed); its only
  permitted state change is minting the single-use commit token via
  `.claude/hooks/audit-approve.sh` on PASS.
- Dispatch it after every build step with: the bead/task ID, the step's acceptance
  criteria / verification checklist (from section B and the bead), the verification
  command(s), and the implementer report path. Incomplete dispatch input is an
  automatic FAIL.
- Output: `VERDICT: PASS | FAIL` with evidence/defects. On FAIL, the builder fixes the
  defects and the auditor re-runs. Never run `audit-approve.sh` yourself.

---

## E — Hooks (deterministic enforcement layer)

**Already installed — do not re-implement.** The orchestrator-mine hook set lives in
`.claude/settings.json` and `.claude/hooks/`:

- `PreToolUse (Bash)` -> `gate-commit.sh`: blocks `git commit` in an armed repo without
  a fresh single-use audit token matching the exact staged diff plus an AUDIT_LOG.md
  PASS row.
- `Stop` -> `stop-gate.sh`: in autonomous mode, blocks session end while unblocked
  beads remain (iteration-capped).
- `SessionStart` / `PreCompact`: `bd prime` + handoff injection
  (`inject-handoff.sh`, `precompact-handoff.sh`).
- Telegram notification: `notify.sh` -> `ORCH_N8N_WEBHOOK`.

The outline's own section-E hook ideas (PostToolUse lint/test runner, STATUS.md-updated
Stop check, headless write-restriction hook) are **deliberately NOT implemented in this
draft**. They are a separate later bead. If that bead lands, its hooks must compose
with — never replace or weaken — the hooks listed above.

---

## F — Human Gates (hard-coded refusals)

Refuse the following even if asked mid-session, by anyone, in any phrasing:

1. **Never mark any Block milestone complete.** Milestone completion is trader
   sign-off — recorded in Google Sheets and STATUS.md, by Amear, only. Claude may
   report that all exit criteria appear satisfied; it may not certify the milestone.
2. **Never modify DECISIONS.md except by appending.** No edits, no deletions, no
   rewording of prior entries.
3. **Never advance to the next block without the entry condition satisfied** (prior
   milestone trader-verified in STATUS.md — see section B table). "It's basically
   done" is not an entry condition.
4. **Never touch SHM thresholds outside the D-2026-07-04-B adjustment protocol.**
   Per SHM spec section 2, thresholds are locked pre-deployment and adjustable only:
   (1) while the strategy is at or above its rolling performance baseline, AND
   (2) via an append-only DECISIONS.md entry, AND
   (3) with a mandatory 5-trading-day cooling period between the proposed change and
   its activation. No threshold is adjusted while the strategy is in drawdown. Ever.

Verbatim comprehension gate (from D-2026-07-04-A, LOCKED):

> **COMPREHENSION GATE (pre-live, hard):** Block 5 (Graduated Live Deployment) does
> not open until Amear can explain, unprompted and without reference material,
> (1) what determines an entry, (2) what determines an exit, and (3) what trips each
> circuit breaker. Verified in a recorded debrief session with Praxis. Pass/fail.
> No partial credit.

The gate does not loosen on paper performance (named Success-Triggered Relapse risk).

Additionally, per CLAUDE.md: never trade or execute orders on live accounts without
explicit trader authorization.

---

## G — Headless / Scheduled Mode (n8n integration)

For n8n-cron-triggered `claude -p "<prompt>"` runs:

- **Read/report only.** Headless runs make no writes to repo state files, code, or
  ledgers. The single exception is a designated `/audits/` output directory for run
  reports. (Deterministic hook enforcement of this restriction belongs to the later
  hooks bead — section E; until then this is an instruction-level rule.)
- Two scheduled jobs:
  1. **Nightly repo audit** — state-file consistency check: STATUS.md vs MANIFEST.md
     vs Beads vs `git log`. Discrepancies reported to Telegram via the n8n webhook.
  2. **Weekly block progress report** — summary to Telegram + a Google Sheets row.
- Headless runs never: close beads, commit, update STATUS.md/MANIFEST.md, mark steps
  done, or dispatch implementer subagents. If a headless run finds work needing
  action, it reports it; a human-attended session acts on it.
- All section F refusals apply unchanged in headless mode.

---

*End SKILL.md DRAFT v0.1 — pending: PHASE 3 BUILD SPECIFICATION import (section B
milestone text), hooks bead (section E ideas), dry-run + trader sign-off before live.*
