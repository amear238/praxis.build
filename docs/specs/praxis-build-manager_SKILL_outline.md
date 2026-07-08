# `praxis-build-manager` — CLAUDE CODE SKILL OUTLINE v0.1
**Location in repo:** `.claude/skills/praxis-build-manager/SKILL.md`
**Purpose:** Encode the PRAXIS block definitions, per-step verification checklists, and audit protocol so every Claude Code session — interactive or headless — executes the build the same way, resumes from Git-tracked state, and cannot self-certify its own work.

---

## 1. SKILL.md FRONTMATTER (draft)

```yaml
---
name: praxis-build-manager
description: "PRAXIS build orchestration. Trigger on any session touching the
  /Volumes/Sensidine/Praxis repo, any mention of a build block (Block 0–6),
  STATUS.md, MANIFEST.md, Beads tasks, or n8n-triggered headless build/audit
  runs. Loads current block state, enforces the step→verify→record loop, and
  routes verification to the auditor subagent. Never marks a milestone
  complete — milestones are human-gated."
---
```

## 2. SKILL BODY — SECTIONS

### §A — Session Boot Sequence (every session, no exceptions)
1. Read `STATUS.md` → current block, current step, last verified state.
2. Read `DECISIONS.md` tail (last 5 entries) → any locked constraints since last session.
3. `bd list` (Beads) → open tasks for current block, in order.
4. State the plan for this session in ≤5 lines **before** any tool call. If the plan exceeds the current block's scope: stop, flag, wait.

### §B — Block Definitions (embedded reference table)
One subsection per block (0–6), each containing:
- Entry condition (prior milestone verified by trader — checked in STATUS.md)
- Ordered task list with **platform annotations** (where performed / where output stored) — mandatory on every task the trader physically touches
- Exit milestone definition, verbatim from PHASE 3 BUILD SPECIFICATION
- Explicit list of what the block does NOT include (scope wall)

### §C — Step Execution Loop (the core discipline)
For every build step:
1. **Build** — smallest complete unit.
2. **Verify** — hand off to auditor (see §D). Builder never grades itself.
3. **Record** — update STATUS.md (rewrite), append MANIFEST.md, `bd close` the task, commit with conventional message referencing the Beads ID.
4. **Report** — one-line Telegram note via n8n webhook on step completion.
No step 3 without step 2 passing. Enforced by hook (see §E), not by instruction.

### §D — Auditor Subagent
- Separate subagent definition: `.claude/agents/praxis-auditor.md`
- **Read-only tool access** (Read, Grep, Glob, Bash restricted to test commands).
- Input: the step's verification checklist from §B + the diff.
- Output: PASS / FAIL + findings summary. On FAIL, builder loops; auditor re-runs. Isolation keeps audit noise out of the main thread.

### §E — Hooks (deterministic enforcement layer)
Shipped in `.claude/settings.json` alongside the skill:
- **PreToolUse (Bash):** block dangerous patterns (`rm -rf`, force-push to main, edits outside repo scope).
- **PostToolUse (Edit/Write):** auto-run linter/tests on touched files; log to session record.
- **Stop:** block session end if STATUS.md was not updated this session, or if any step was marked done without an auditor PASS on record. The agent cannot claim completion until the record proves it.
- **SessionStart:** inject STATUS.md summary into context automatically.

### §F — Human Gates (hard-coded refusals)
The skill instructs Claude Code to **refuse** the following even if asked mid-session:
- Marking any Block milestone complete (trader sign-off in Google Sheets + STATUS.md, by Amear, only)
- Modifying DECISIONS.md except by appending
- Advancing to the next block without the entry condition satisfied
- Touching SHM thresholds outside the D-2026-07-04-B adjustment protocol

### §G — Headless / Scheduled Mode (n8n integration)
- n8n cron → `claude -p "<audit prompt>"` headless runs.
- Two scheduled jobs: **nightly repo audit** (state-file consistency: STATUS vs MANIFEST vs Beads vs git log — discrepancies reported to Telegram) and **weekly block progress report** (summary to Telegram + Google Sheets row).
- Headless runs are **read/report only**. No writes outside a designated `/audits/` directory. Enforced by hook.

---

## 3. BUILD ORDER FOR THE SKILL ITSELF
1. Draft SKILL.md from this outline (Claude Code session, ~1 session).
2. Write auditor subagent + hooks; test hooks fire correctly on synthetic violations.
3. Dry-run: execute one already-completed Block 0 task through the full §C loop to validate the machinery against known-good output.
4. Trader reviews the dry-run record → sign-off in Sheets → skill goes live for Block 0 completion.

*Note: consider running the official skill-creator against this outline for structure/triggering optimization before finalizing.*

---
*End outline v0.1*
