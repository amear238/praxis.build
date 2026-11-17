# Scrub-forward Correction 1: adversarial check (A-D)

## Task
Attack Correction 1 of unit 2026-11-10-scrub-forward (bead Praxis_build-8ux): A the pointer note in the rulings-filing report, B the in-place edits to two bead descriptions, C three MANIFEST rows, D the real index.

## Mode
ADVERSARIAL. Read-only on the repo apart from this report. No git writes, no bd writes. The term was read at runtime into a shell variable and never printed. All text output went through the mask helper M. Counts only.

## Criterion
S1, S2, S6 (specs/SPEC_RUBRIC.md, verbatim in the brief).

## Process log
1. Read the term at runtime: `TERM-nonempty`. The helper is a 2-line shell function. It masks upper case too (`M-upper: 1`, `M-lower: 1`).
2. A: compared the file with HEAD as a prefix, compared the landing blob, counted the term, and checked the cited lines 113-121, DECISION_LOG :47 at 0eea766, HEAD and the working copy, 7d9be8e:HANDOFF, V5, and whether SRC is gitignored.
3. B: ran `bd list --all --json` (129 beads, 5 statuses), `bd show --json` for all 129 and `bd comments --json` for the 11 beads with comments. Counted with grep and again on JSON-decoded strings, with positive controls. Compared every field of every bead against /tmp/c1-bd-all.json. Rebuilt the expected descriptions from /tmp/c1-bd-before. Scanned all 262 files under .beads and ran `bd history` on both edited beads.
4. C: diffed against /tmp/c1-manifest-pre.md, checked rows 307-314, the column count, the term count, and each claim in the new rows.
5. D: ran `git diff --cached --name-only`.
6. S6: checked hooks and scripts for dependencies on the bead ids, the report path and the Result line. Checked the 5 reports that reuse tokprobe2 and how the gate picks LATEST.

## Verification evidence (command output)
```
# A
450 (HEAD lines) / 454 (working copy)
L1-450-IDENT
BYTEPREFIX-IDENT
BLOB-EQ-WC
452:## Pointer note 2026-11-10 (filer's note, not a ruling)
note term=0   whole file term=0   HEAD file term=0   pos-control(upper)=1
lines 113-121: 113 "**De-identification probe.**", 114 seeds from HEAD:DECISION_LOG.md:47,
  116 "Liveness: ... the two known locations", 120 "LIVENESS HEAD:DECISION_LOG.md ... lines=47,77,89,...",
  121 "LIVENESS 7d9be8e:HANDOFF.md ..."
0eea766:47 1
HEAD:47 1
WC:47 0
WC-DL-all 0
7d9be8e:HANDOFF 1
SRC-ignored
SRC-untracked
SRC-in-repo: yes
V5 header (:352): "extracted at runtime from the gitignored source into $TERM"; first command reads `sed -n 48p` of that source
791:- [2026-11-10T09:08:00Z] ... D11 CLOSURE before unit 1 (S4 record) ... (contains 8ux)
# B
list-rc=0 bytes=250929 / n_beads 129 / statuses ['blocked','closed','deferred','in_progress','open']
list term count: 0
show n=129 fail=0 bytes=309077 term=0
comments n=11 fail=0 bytes=16239 term=0
pos-lower: 1 / pos-upper: 1 / pos-list: 1
decoded all.json objs 129 term 0 (poscontrol 1); show.all 129 term 0 (1); com.all 30 term 0 (1)
pre n 129 cur n 129 ids equal True / added [] removed []
changed Praxis_build-ax4 ['description', 'updated_at']
changed Praxis_build-r8j ['description', 'updated_at']
Praxis_build-r8j status closed prio 0 ; Praxis_build-ax4 status open prio 1
Praxis_build-r8j before: term-ci=1 ; expect==cur True (len 978/978)
Praxis_build-ax4 before: term-ci=2 ; expect==cur True (len 963/963)
.beads scan (262 files): issues.jsonl 0, interactions.jsonl 0;
HIT 1 .beads/backup/5cn3utnm5n0eg0vo3fci5js78je941ut.darc
HIT 2 .beads/backup/b2ndvltk7jal75pc4tni415pc9p2gimn.darc
HIT 1 .beads/backup/nideqti1dhh990ug2tep1jhvlse3f2nc.darc
HIT 1 .beads/backup/34uifqtnomecfg6fl7fqc5652ug7htrg.darc
HIT 6 .beads/embeddeddolt/Praxis_build/.dolt/noms/vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
Praxis_build-r8j history rc=0 bytes=291107 term-ci=156
Praxis_build-ax4 history rc=0 bytes=241017 term-ci=310
backup ignored-rc=0 / embeddeddolt ignored-rc=0
remotes ['origin'] backups ['backup_export']
# C
344 / 341 ; diff: 341a342,344 ; diff-lines: 3 ; PREFIX-IDENT ; R307-314-IDENT
term-342-344: 0 term-all: 0 ; pipes: 7 7 7 7
worker1 exists=y term=0 8ux=1 scrubfinal=8 ; adversarial exists=y term=0 8ux=2 ; Praxis_build-8ux in bead ids: 1
adversarial report :33 "| 8 | S6: ..." ; :176 "### Check 8 (S6)" ; :258 "1. **S6 dependency: ...**" (under ## Findings)
792-has-pointer=1 ("Correction 1 to the same unit: (a) append a dated pointer note at the END of ...rulings-fi...")
# D
D: docs/reports/evidence/2026-10-28-mffu-davi-reply.png
D-count: 1
# S6
scripts/gate-manager-output.sh:6: LATEST=$(ls -t "$DIR"/docs/reports/*.md 2>/dev/null | head -1)
gate-manager-output.sh:23: if ! grep -qiE 'Result:\s*(PASS|FAIL|BLOCKED)' "$LATEST"; then
mtime order: 04:17:54 rulings-filing-manager.md ; 04:17:37 scrub-forward-manager.md ; 04:13:22 scrub-forward-adversarial.md
hooks/scripts/agents grep for Praxis_build-(r8j|ax4) and rulings-filing-manager: no hits
scratchpad/tokprobe2.sh: "No such file or directory" (the method exists only as text)
reusers citing rulings:113 = 4 of 5; none cite DECISION_LOG.md:47 directly
```

## Findings
1. **C (factual error in row 343).** The row says "(finding 8: the tokprobe2 method depends on HEAD:DECISION_LOG.md:47)". The adversarial report files that dependency as Check 8 (:176, table row :33) and as Finding **1** (:258). It has no "finding 8". The row's claim is false as written and should say "check 8".
2. **B (history retains the term; a scoping fault, not a fault in the current fields).** Every current field in all 129 beads holds 0 occurrences, and the edits match byte for byte. But `bd history`, a read-only subcommand, still returns the term (156 hits for r8j, 310 for ax4). The Dolt noms store and 4 gitignored backup .darc files also hold it, and the Dolt DB has an `origin` remote. The in-place edit is forward-only, the same as the git side under D-2026-08-06-A. Any statement that "beads hold 0 occurrences" without the words "current fields" goes beyond the evidence (S2). I did not check whether any report makes that statement (UNVERIFIED).
3. **S6 (gate cross-effect).** gate-manager-output.sh checks the newest-mtime report in docs/reports. Correction 1 touched the rulings-filing report, which made it the newest (04:17:54, newer than the scrub-forward manager report at 04:17:37). Its old line 450 `Result: PASS` would satisfy that gate on behalf of the manager report. This holds until a newer report lands. This report lands later, so the window has now closed. The risk comes back whenever an old report is appended to.
4. **A (minor imprecision, no false fact).** The note says the liveness arm "runs on that location" (:47). Line 120 shows it runs on the whole HEAD:DECISION_LOG.md. The advice still holds, because the working-copy DECISION_LOG.md holds 0 and 0eea766's holds 1. The other cited facts check out: line numbers 113/114/116, the two LIVENESS lines, 0eea766:47=1, WC:47=0, the 7d9be8e arm pinned (count 1), V5 extracting from the gitignored source, SRC gitignored and untracked, bead 8ux, row 09:08 contains 8ux, and lines 1-450 unchanged.

## Per-check
- A PASS: byte-identical prefix and blob, 0 occurrences of the term, cited facts true (imprecision noted in finding 4).
- B PASS on current fields (0 occurrences across list, show and comments, controls 1, only description and updated_at changed). The history finding (2) stands.
- C FAIL: shape, rows 307-314, format and term count are all correct, but row 343 misnames "finding 8".
- D PASS: the index holds only the PNG.

## Files staged
None. The only write was this report.

Result: FAIL
