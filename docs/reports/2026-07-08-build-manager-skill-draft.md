# Report — praxis-build-manager SKILL.md draft (Bead Praxis_build-e8c)
**Date:** 2026-07-08
**File created:** `.claude/skills/praxis-build-manager/SKILL.md` (the only new implementation file; left unstaged)
**Source:** `docs/specs/praxis-build-manager_SKILL_outline.md` v0.1

## How each outline section was handled

- **Section 1 (frontmatter):** `name` + `description` only, as valid skill frontmatter.
  Description expanded beyond the outline draft to trigger on block/step numbers,
  state-file names, bd/Beads, the signal-path components, circuit breakers, and SHM —
  tuned for PRAXIS build sessions. Hardcoded repo path from the outline draft dropped
  (repo lives at `/Volumes/Sensidine/Praxis.build`, and path-based triggering is
  unreliable in descriptions).
- **§A Session boot:** implemented verbatim as a 4-step sequence (STATUS.md,
  DECISIONS.md tail with the two locked D-2026-07-04 decisions summarized inline,
  `bd list`, <=5-line plan with scope-stop rule).
- **§B Block definitions:** implemented as a summary table plus per-block subsections
  for Blocks 0–6 with entry conditions, scope walls, and platform-annotation rule.
  Build-first reorder encoded per D-2026-07-04-A (Block 1 builds on sim immediately;
  comprehension gate at Block 5). SHM sequencing encoded per D-2026-07-04-B
  (thresholds locked at Block 2 milestone; built Block 3; live before Block 5 Phase A).
  Block 0 step list taken from STATUS.md (0.1–0.8, current step 0.7).
- **§C Step execution loop:** build -> verify (auditor) -> record (STATUS.md rewrite,
  MANIFEST.md append, bd close, commit with bead ID) -> report (Telegram via
  ORCH_N8N_WEBHOOK). Added a note that the installed gate-commit.sh token protocol
  governs commits while the orchestrator gate is armed.
- **§D Auditor:** the outline's proposed `.claude/agents/praxis-auditor.md` was NOT
  created. The skill references the existing `.claude/agents/orchestrator-auditor.md`
  (read-only, mints the single-use token via audit-approve.sh) and states the outline's
  separate auditor is superseded.
- **§E Hooks:** NOT implemented, per task instruction — documented as already covered
  by the installed orchestrator-mine hook set (gate-commit.sh, stop-gate.sh,
  inject-handoff.sh, precompact-handoff.sh, notify.sh, bd prime). The outline's own
  hook ideas (PostToolUse lint/test, STATUS-updated Stop check, headless write
  restriction) are explicitly marked as a separate later bead that must compose with,
  not replace, the installed hooks.
- **§F Human gates:** all four hard refusals encoded: no milestone completion (trader
  sign-off only), DECISIONS.md append-only, no block advance without entry condition,
  SHM thresholds only via the D-2026-07-04-B protocol (baseline + append-only entry +
  5-day cooling, never in drawdown — quoted from SHM spec section 2). Comprehension
  gate included verbatim from D-2026-07-04-A. CLAUDE.md's no-live-trading rule
  restated.
- **§G Headless mode:** read/report only; /audits/ output directory as sole write
  exception; nightly consistency audit + weekly progress report jobs; explicit list of
  actions headless runs never take. Noted that deterministic enforcement of the write
  restriction awaits the hooks bead.
- **Outline section 3 (build order):** encoded as the file-header status line:
  "Status: DRAFT v0.1 — not live until trader dry-run sign-off (outline section 3
  step 4)."

## Gaps marked TBD (all "TBD — needs PHASE 3 BUILD SPECIFICATION import")

The PHASE 3 BUILD SPECIFICATION is not in this repo, so the following were NOT
invented and are marked explicitly in section B:
1. Verbatim exit-milestone text for all Blocks 0–6.
2. Block 1 task-level breakdown.
3. Block 2 task-level breakdown.
4. The nine circuit breaker definitions (Block 3).
5. Block 4 exit criteria (25-trade sample noted only as the SHM spec's "candidate").
6. Block 5 graduation phase ladder and kill criteria (only Phase A = 1 MNQ is known).
7. Block 6 detail.

## Conflict check against orchestrator-mine hooks

Read `.claude/settings.json` and all six `.claude/hooks/*.sh` plus
`.claude/agents/orchestrator-auditor.md`. **No conflicts found.**
- No hooks were added or modified; settings.json untouched.
- The skill's §C commit step is written to be compatible with gate-commit.sh's rules
  (plain `git commit -m`, staged-diff token, no `-a`/`--amend`, one commit per call).
- The skill never instructs running audit-approve.sh directly (auditor-only, matching
  the hook's forgery check).
- §G headless rules do not contradict stop-gate.sh (which only acts in autonomous
  orchestrator mode).
- No `praxis-auditor` agent introduced, avoiding a duplicate-auditor conflict.

## Constraints honored
- Exactly one new implementation file + this report. Nothing staged, nothing committed.
- STATUS.md, MANIFEST.md, DECISIONS.md, and all existing files untouched.
- Skill marked DRAFT; per outline section 3 it goes live only after hooks bead,
  dry-run of a completed Block 0 task, and trader sign-off in Sheets.

## Follow-ups (for orchestrator to file/track)
- Later bead: outline §E hook ideas (compose with installed hooks).
- Import PHASE 3 BUILD SPECIFICATION milestone text into SKILL.md §B.
- Dry-run + trader sign-off (outline section 3 steps 3–4); MANIFEST.md entry for the
  new skill file belongs to whoever commits it.
