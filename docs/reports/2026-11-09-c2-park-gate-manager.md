# C2 park-commit gate exemption — manager report (unit 2026-11-09-c2-park-gate, bead Praxis_build-8sw)

Standing limitation: Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

(This unit states no backtest or P&L figure; the sentence is carried because the brief requires it once per report.)

## Task

Amear ruling C2 (D-2026-11-08-C, DECISIONS.md:1826): "a park commit to parked/ branches is exempt from the audit-token gate, because it never touches main." Build the exemption in `.claude/hooks/gate-commit.sh`, trip-test it with synthetic PreToolUse payloads in a throwaway clone, report (do not build) on the "never touches main" mechanism, append one filer's paragraph to `specs/SPEC_RUBRIC.md` and three rows to `MANIFEST.md`. Bead `Praxis_build-8sw` stays open (master closes).

## Rubric criteria addressed

S1, S2, S3, S4, S6, S9, S13 (quoted in the brief from specs/SPEC_RUBRIC.md). Graded per criterion below.

## Process log

- Read the gate (714 lines), the park rule and C2 block of SPEC_RUBRIC (lines 252-300), the PreToolUse registrations in `.claude/settings.json` (working-tree copy, which carries 10 uncommitted insertions), `scripts/no-commit-guard.sh`, `scripts/master-bash-guard.sh`, `scripts/mint-guard.sh`, head of `scripts/commit-tree-verify.sh`.
- The gate itself never writes the mint log (only `auditor-mint.sh` and `commit-tree-verify.sh` reference it). So, per the brief, the exemption appends nothing to it; it prints one stderr line only.
- Design (decided by manager under D-2026-11-08-D D1): see "What was built".

(in progress)
