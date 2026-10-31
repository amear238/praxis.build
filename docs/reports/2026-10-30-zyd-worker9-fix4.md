# Praxis_build-zyd — fix pass 4 (praxis-worker 9)

## Task
Make fixes K1–K7 to the D-2026-10-30-A entry in DECISIONS.md (from line 247 to EOF), to `cost_model.fill_resolution_note` in config/backtest-cost-model.json, and to MANIFEST.md lines 133 onward. Nothing else.

## Mode
BUILD (fix pass 4). No git add or commit.

## Criterion
Manager brief K1–K7 (the S2 / S5 traceability fixes to the F3 artifact).

## Process log
- Checked K3 before applying. `sed -n '441p' DECISION_LOG.md | /usr/bin/grep -o -E '.{0,80}2 ticks.{0,80}' | head -3` printed:
  ` The "Trend" box item is DROPPED and will not be investigated. (3) F3 `[N]` = **2 ticks per side** — recorded in its own row below. (4) The NT8 8.1.8.4 update is SKI`
  Line 441 starts `- [2026-10-30T21:36:00Z] **WHO: amear** | ... | WHAT: **INTAKE OF FIVE RULINGS ...`. It holds the 2-tick ruling, so K3 was applied.
- Wrote `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/w9f/apply.py`, based on worker7's w7f/apply.py. Every old string must match exactly once, and all asserts run before any file is written. It printed `APPLIED`.
- K1: the (c) label, the "would not decide" clause and the R3 sentence were replaced in DECISIONS, plus the config note. K2: the void-clause sentences. K3 (i) and (ii). K4: the residual sub-bullet. K5: the UNVERIFIED point-value sentence in (b). K6: Unblocks. K7: two new MANIFEST rows before the zyd-f3-artifact row, and the worker6 row amended.

## Verification evidence
V1
```
a0c8fbeea8dcafd72f7385c2b1c50594a6cf7349c8bd49032531cb4491d5234a  -   (head -n 243 DECISIONS.md)
a0c8fbeea8dcafd72f7385c2b1c50594a6cf7349c8bd49032531cb4491d5234a  -   (git show HEAD:DECISIONS.md)
ccb7c2898b679e4abb78e20fceb166b9cd58ee6d32db387e6efe2e3422a06abf  -   (head -n 132 MANIFEST.md)
ccb7c2898b679e4abb78e20fceb166b9cd58ee6d32db387e6efe2e3422a06abf  -   (git show :MANIFEST.md | head -n 132)
0
```
V2: `PARSE_OK`
V3 (counts in the entry, lines 247 to EOF)
```
checkpoint order logic => 1
given a position state, whether an entry or exit order is sent => 0   <-- see Deviations
not for the trade set as a whole => 1
does not establish the bead => 1
the ledger records only that no run has set High => 1
21:36:00Z => 2
early-close days (CANNOT-DETERMINE-STATICALLY, INFERRED). => 1
UNVERIFIED => 1
closure is not decided here => 1
which has not been run => 0
review and closure => 0
which orders this strategy sends => 0
```
The exact K1 text, `at a checkpoint with a given position state, whether an entry or exit order is sent`, counts 1.
V4: `True f9144cb50aab2885 f9144cb50aab2885`
V5: the sections are pasted in the SubagentHandback report to the manager. MANIFEST check: `worker6; BREAK FOUND; fix pass by worker7, re-attacked by worker8)` is present.

## Deviations
- V3 presence string 2 returns 0. The brief's string `given a position state, whether ...` does not occur in the brief's own K1 replacement text, which reads `with a given position state, whether ...`. I applied K1 exactly as written. The prescribed text is present (count 1).
- Not fixed (out of scope): the **Rationale** paragraph still says "`[N]` = 2 was set by Amear at `21:36:30Z`". The **Pre-commitment** bullet still cites rows `00:10:00Z` and `21:36:30Z` only. After K3, both places differ from the intake row `21:36:00Z` (WHO: amear) as the first ledger writing. Reported for the manager.

## Files modified (unstaged, as instructed)
- /Volumes/Sensidine/Praxis.build/DECISIONS.md
- /Volumes/Sensidine/Praxis.build/config/backtest-cost-model.json
- /Volumes/Sensidine/Praxis.build/MANIFEST.md
- /Volumes/Sensidine/Praxis.build/docs/reports/2026-10-30-zyd-worker9-fix4.md (this report)

## Result: PASS
All of K1–K7 applied. V1, V2 and V4 pass. V3 passes, except the one presence string whose wording does not match the brief's own K1 text (see Deviations).
