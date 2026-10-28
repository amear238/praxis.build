# a20 Kinetick research: correction worker (CW2) report

**Task:** correction by append to `docs/reports/2026-10-20-a20-kinetick-research.md` after its failed audit (bead Praxis_build-a20). **Mode:** BUILD. **Criterion:** S1/S2/S6/S8 per the manager's brief; append-only, no staging, no ledger touched.

**Process log.** Checked the pristine copy's sha256 (`747b5084…`) and that the artifact was byte-equal to it. Read the 14 evidence blocks in `ev2/`. Drafted `appended.md` in the scratchpad, embedding every block with `cat` (none retyped). Built the artifact with the brief's exact one-liner. Banned-word and `Result:` counts in the draft were 0 before the build.

**Verification evidence** (run by CW2 after the build):
```
$ diff $SP/a20-original.md docs/reports/2026-10-20-a20-kinetick-research.md | /usr/bin/grep -E '^[0-9]'
1a2
491a493,1148
$ wc -l $SP/a20-original.md docs/reports/2026-10-20-a20-kinetick-research.md
     491 $SP/a20-original.md
    1148 docs/reports/2026-10-20-a20-kinetick-research.md
    1639 total
$ /usr/bin/grep -c -w -i 'T[B]D' docs/reports/2026-10-20-a20-kinetick-research.md
0
$ git diff --cached --name-only | wc -l
       9
```

**Files staged:** none by this worker (the count of 9 is pre-existing staged work). The artifact and this report are untracked.

**Not done / for the manager:**
- MANIFEST.md was not updated for this new report file (ledgers were off-limits per the brief).
- §1's B1/B2/M1–M4 descriptions are the manager's relay; the audit file was not read.
- §3's "the manager carried it in unverified (S2)" is stated as the brief framed it, resting on o1's :85/:119 versus :257/:261/:303.
- No `Result:` line was written in the artifact or here. Grading is left to CW3 and the manager.

## CW4 fix pass

**Task:** fix the appended section after CW3's FAIL (F1–F8) plus the manager's M-a…M-d. **Mode:** BUILD. Edited `$SP/appended.md` only (one scripted pass, each replacement asserted to match exactly once; o6/o7/o8 read from `ev2/` byte-for-byte, each embedded once). Rebuilt with the brief's one-liner. Lines 1 and 3–492 untouched.

| Fix | Artifact line now carrying it |
|---|---|
| F1 (A and D both add no connection; A alone changes nothing) | :756 |
| F2 (hedge restored on B and C; §5–§8 scanned, no other unhedged scope sentence found) | :757 |
| F3 10-16 rule 1, o6 pasted | :587 (bullet (0)), :662 (o6 block) |
| F3 10-19 allowance = SDF plus "Simulation" | :588 (end of (i)) |
| F3 §3 (iii) rewritten | :590 |
| F3 "Where it stands now" (narrowing, wording match) | :596 |
| F3 C4 second layer | :683 |
| F3 §8 (a) Sim101 / (c) "Simulation" auto-connect; "Three places" | :778 / :780; :777 |
| F3 optional "Simulation only" line (INFERRED) | :587 |
| F4 (row B, original-D-071 column) | :746 |
| F5 (483 matches; 135 matches = 129 lines), o8 | :928, :930 |
| F6 (o3a label; CW1 line names o3a) | :801; :1177 |
| F7 (register row :124; §5 header) | :494; :741 |
| F8 (`~/Windows-migration/` prefixes) | :588 |
| M-a (§1 cites `DECISION_LOG.md:428`, o7 embedded) | :502, :508 |
| M-b (M2 replacement adds E9) | :1056 |
| M-c (Part 5/6 swap a PLAN; restore REPORTED, update 2 `:62`) | :684 |
| M-d (summary line 5 first and last sentences) | :769 |
| Index (o6, o7, o8) / Workers (CW3, CW4, CW5) | :1164, :1168, :1172 / :1179–:1181 |

**Also changed (reported, smallest accurate change):** with o7 embedded, `:428` records M4 as "E5 pastes only the count 26", while §1's M4 bullet described the "connected to" wording. §1's M4 bullet (:505) now quotes `:428`'s M4 and says §10 M4 pastes all 26 lines (o4a) and also corrects the wording. Not in F1–F8/M-a…M-d; the manager should check it.

**Verification evidence** (run by CW4 after the build; the final rebuild below reproduces it byte-for-byte):
```
$ diff $SP/a20-original.md docs/reports/2026-10-20-a20-kinetick-research.md | /usr/bin/grep -E '^[0-9]'
1a2
491a493,1191
$ wc -l docs/reports/2026-10-20-a20-kinetick-research.md
    1191 docs/reports/2026-10-20-a20-kinetick-research.md
$ /usr/bin/grep -c -w -i 'T[B]D' docs/reports/2026-10-20-a20-kinetick-research.md
0
$ git diff --cached --name-only | wc -l
       9
```

The staged count is still 9, so the artifact's "Files staged" block was left as is. **Files staged:** none by CW4. No `Result:` line written.
