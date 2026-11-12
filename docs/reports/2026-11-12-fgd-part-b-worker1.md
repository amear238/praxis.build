# Unit 2026-11-12-fgd-part-b — ADVERSARIAL worker 1

## Task

Try to break claims 1–9 about the uncommitted Amendment note 2 sections appended to `docs/specs/2026-11-10-live-signal-topology.md` (after :200) and `docs/specs/2026-11-10-f2-session-flat-proposal.md` (after :111), and about the last 4 rows of `MANIFEST.md`. Bead `Praxis_build-fgd` part B, docs only.

## Mode

ADVERSARIAL. Read-only on the repo, except this report file. Scratch files are under `/tmp/fgdb-neg/` only. Nothing staged, committed or pushed.

## Criterion

Graded against `specs/SPEC_RUBRIC.md` standing criteria S1 (pasted output), S2 (no over-claiming) and S6 (cross-block check), applied to claims 1–9 in the brief.

## Process log

1. Confirmed this report path did not exist, and HEAD = `5467031c0c36d969eba9956cedcf184dbd5383df`. Line counts: HEAD has 200 and 111 lines; the working tree has 222 and 137. There are 0 removed lines in either spec diff (E1).
2. Read both appended notes and the MANIFEST tail (E1, E2). Listed the `^#` headings at `5467031` and printed every cited range at `5467031` with `sed -n` (E3).
3. My first attempt at the old-vs-new comparison ran under zsh, which does not word-split `$pair`, so it produced no usable result. I dropped it and re-ran the comparison as a bash script (E4).
4. Byte-identity of the quotes, the `head -n` cmp checks, negative tests (a) and (b), and the claim 7 checks (E5). My first negative (b) on the topology file was vacuous: line 50 is 3 characters plus a newline and has no `a`, so `sed` changed nothing and cmp exited 0. I re-ran it with a guaranteed change to line 1, and cmp then exited 1 (E6). The F2 negative (b) was valid on the first run.
5. Claim 7 broke: DECISIONS.md differs from HEAD. I looked at the added content (E6, E7).
6. Claim 5 sweep: every line at HEAD of both files that names `SPEC_RUBRIC` or "rubric" and also has a `:N` (E6, E8, E9).
7. Status facts (F1/F2 PASSED@ shas, MANIFEST row references, :92 vs :8), de-identification counts (E10), and the DECISION_LOG 17:03Z item (c) (E11).
8. Cure by fix worker 2 (BUILD) at the manager's dispatch: E10 re-run as final2.sh with the medication list read from a scratch file outside the repo; truncated quotes at :47, :52, :476, :496 replaced. Findings and Result unchanged unless stated in item 9.

## Findings by claim

1. **Claim 1: HOLDS.**
   - At `5467031`, F1 is at :65, F2 at :81 and O4 at :114.
   - `## PASSED — closed criteria` covers :46–98 and `## OPEN — gradeable now` covers :99–122. So F1 and F2 are under PASSED and O4 is under OPEN, as the notes say.
   - :75–76 is F1's "**Unblocks when.**" text and :77 is F1's "**Blocks.**" line.
   - :87–92 is F2's "**Why frozen.**" text and :93–94 is F2's unblock clause.
   - :114–119 is the O4 heading plus its text. :120 is blank and :121 is `---`, so the range is complete (E3, E4).
2. **Claim 2: HOLDS.** All 4 fenced `text` blocks are one line each and cmp-match HEAD :7, :112 (topology) and :61, :69 (F2) (E5).
3. **Claim 3: HOLDS.** `head -n 200` and `head -n 111` cmp-match their HEAD blobs, with exit 0 (E5).
4. **Claim 4: HOLDS.** Each old range at `b4c3291` is cmp-identical to the new range at `5467031`: 28–29/75–76, 30/77, 108–113/114–119 and 37–42/87–92. So are 43–44/93–94, 32/81 and 19/65 (E4).
5. **Claim 5: HOLDS.**
   - The `SPEC_RUBRIC` citations at HEAD are topology :7 and :112, and F2 :8, :61, :69, :92 and :95. Each one is covered by a note (E6).
   - The other `:N` hits on lines that mention the rubric are not rubric line citations: times (topology :160, :168), self-file line refs (:105, :58–66, :75–78, :8 heading at F2 :89), and DECISIONS.md refs (:2108, :2205, :1744–1745) (E8, E9).
   - `SPEC_RUBRIC.md` is unchanged between `006a08b` and `5467031` (git diff exit 0) (E4).
   - At `e3323a8`, :30–31 is the F2 unblock clause under `### F2` (:19) (E4).
   - F2 :92 contains :8 verbatim (count 1) (E10).
6. **Claim 6: HOLDS for the two notes.** Every sentence either re-points a citation or states a fact I checked: F1 PASSED@b4c3291 at :66 and F2 PASSED@e3323a8 at :82 (E10).
   - Observation, not a break: the manager MANIFEST row (third-to-last) says "F-8 disposition (Flat1559.cs :31 not edited)". That row describes a disposition recorded in the manager report, which I was not given and did not check. Whether that disposition is a design choice is UNVERIFIED by me.
   - MANIFEST row refs 353/446 (topology) and 354/448 (F2) point at rows for the right paths (E10).
7. **Claim 7: BREAKS.**
   - These parts hold: `ninjascript/` gives diff exit 0 with 0 untracked files, and `specs/SPEC_RUBRIC.md` gives diff exit 0.
   - **`DECISIONS.md` differs from HEAD (diff exit 1).** The diff adds 62 lines and removes 0. It adds one new `## ` heading, "D-2026-11-12-B: R6 step 2 backtest engine authorised, first pass only (Mac-side Python event simulator on the 1-minute file; master under D-2026-11-08-D D1)", and 0 added lines contain "fgd" (E5, E7, E12).
   - So the content does not look like this unit's. Attributing it to other parked work is my inference: UNVERIFIED as to when or by whom it was written. Still, claim 7 as stated is false.
8. **Negative tests: all three fail as expected.**
   - (a) Quotes checked against the wrong lines (:8, :68) report MISMATCH (E5).
   - (b) A one-byte change gives cmp exit 1 for both files. This counts the topology re-run in E6; the first topology mutation was vacuous (see Process log 4).
   - (c) At `5467031`, :28–29 is F3 text ("optimism is invisible in the output.", then F3's "Unblocks when"), and 0 lines contain "nine breakers" (E3, E12).
9. **Claim 9: de-identification on the 52 added lines.**
   - Email addresses: 0. Medication names: 0, and the word "medication" appears 0 times.
   - Rep-name pattern: built by script from the single matching PNG's basename (match count 1, pattern length 4). It occurs 0 times. A self-test of the same pattern on a scratch line returned 1.
   - "Amear" occurs 2 times.
   - Method for other person-like names: take capitalised words outside backtick spans, list the distinct ones, and remove a project-vocabulary stoplist. The only word left was "Any", so 0 person-like names other than Amear (E10).
   - Item (c) of the 2026-11-12T17:03Z DECISION_LOG row exists and matches the unit's scope (E11).

## Verification evidence (command output)

### E1

````
$ cd /Volumes/Sensidine/Praxis.build && ls docs/reports/2026-11-12-fgd-part-b-worker1.md 2>&1; git rev-parse HEAD; for f in docs/specs/2026-11-10-live-signal-topology.md docs/specs/2026-11-10-f2-session-flat-proposal.md; do echo "=== $f"; git show HEAD:$f | wc -l; wc -l < $f; git diff HEAD -- $f | grep '^[-+]' | grep -v '^+++\|^---' | grep -c '^-'; done; echo; sed -n '201,$p' docs/specs/2026-11-10-live-signal-topology.md
ls: docs/reports/2026-11-12-fgd-part-b-worker1.md: No such file or directory
5467031c0c36d969eba9956cedcf184dbd5383df
=== docs/specs/2026-11-10-live-signal-topology.md
     200
     222
0
=== docs/specs/2026-11-10-f2-session-flat-proposal.md
     111
     137
0


## Amendment note 2 — 2026-11-12 (rubric line citations)

> ***Added 2026-11-12; not part of the text above.*** Body lines 1–200 above are unchanged, including the amendment note at :116–200. Unit `2026-11-12-fgd-part-b` (bead `Praxis_build-fgd`, part B), decided by master under D-2026-11-08-D D1, changeable by Amear (DECISION_LOG 2026-11-12T17:03:00Z, item c). `specs/SPEC_RUBRIC.md` has been edited since this file was committed at `b4c3291`, so the rubric line numbers cited at :7 and :112 no longer point at the cited text. Each corrected citation below names the rubric criterion, its section and its line range at the pinned sha `5467031`. This note makes no new design choice, writes no DECISIONS.md entry and changes no rubric state. Each old line below is copied by script from this file at HEAD `5467031`, byte-identical.

### :7 — rubric F1 unblock clause

```text
This document does not clear F1. F1 clears when this file is committed and the auditor confirms it addresses every one of the nine breakers by name (`specs/SPEC_RUBRIC.md`:28–29). It builds nothing, changes no code, no workflow and no account.
```

Corrected citation: rubric F1, section "## PASSED — closed criteria" (subsection "### F1 — Signal-path topology vs. circuit-breaker placement", :65), `specs/SPEC_RUBRIC.md`:75–76 at `5467031`. The cited clause is F1's "**Unblocks when.**" text; it was at :28–29 at `b4c3291` and its words are unchanged.

### :112 — rubric F1 "Blocks" line

```text
This topology touches: Block 1 (the emitter changes from TradingView to NT8; the TESTED pipe is reused; Deviation G's ingress question leaves the anchor's live path); Block 2 (the emitter must reproduce the backtest strategy's decisions, so O4 parity now also covers emitter-vs-backtest equality); Block 3 (all nine breakers, Redis, PostgreSQL, the fallback script); Block 4 (the paper pass on MFFU sim runs on this path, D8(8)); Block 5 (live, D2(b)); Deviation A (strategy logic in NinjaScript, kept; now also the emitter); Deviation C (reversals are entries for #2, bead `Praxis_build-yra`); Deviation G (D-2026-07-09-D); D-2026-11-10-A (bypass B1); rubric F2 (the flat time and session boundary for #4/#5); rubric F4 (MFFU automation, FROZEN); rubric O2 (`praxispush`); rubric O4 (parity); the SHM thresholds that F1 blocks (`specs/SPEC_RUBRIC.md`:30).
```

Corrected citation: rubric F1, section "## PASSED — closed criteria" (subsection "### F1 — Signal-path topology vs. circuit-breaker placement", :65), `specs/SPEC_RUBRIC.md`:77 at `5467031`. The cited line is F1's "**Blocks.**" line ("Block 3 entirely. Any SHM threshold derivation."); it was at :30 at `b4c3291` and its words are unchanged. At `5467031` F1 is PASSED@b4c3291; the line stays in F1's text.

No other `specs/SPEC_RUBRIC.md` line citation appears in lines 1–200 of this file.
````


### E2

````
$ cd /Volumes/Sensidine/Praxis.build && sed -n '112,$p' docs/specs/2026-11-10-f2-session-flat-proposal.md; echo ====MANIFEST; tail -n 4 MANIFEST.md
Exit code 1

## Amendment note 2 — 2026-11-12 (rubric line citations)

> ***Added 2026-11-12; not part of the text above.*** Body lines 1–111 above are unchanged, including the amendment note at :83–111. Unit `2026-11-12-fgd-part-b` (bead `Praxis_build-fgd`, part B), decided by master under D-2026-11-08-D D1, changeable by Amear (DECISION_LOG 2026-11-12T17:03:00Z, item c). `specs/SPEC_RUBRIC.md` has been edited since this file was committed at `b4c3291`, so the rubric line numbers cited at :61 and :69 no longer point at the cited text. Each corrected citation below names the rubric criterion, its section and its line range at the pinned sha `5467031`. This note makes no new design choice, writes no DECISIONS.md entry and changes no rubric state. Each old line below is copied by script from this file at HEAD `5467031`, byte-identical.

### :61 — rubric O4 citation

```text
| Block 4 parity gate (rubric O4, `specs/SPEC_RUBRIC.md`:108–113) | Rule F2-1 removes the 11:30 cut and the 15:00 system disable, so a breakers-on backtest and the live run use the same session clock as the current 16:00-flat backtests. O4's question (breakers on, off, or both) is not answered here. |
```

Corrected citation: rubric O4, section "## OPEN — gradeable now" (subsection "### O4 — Backtest-vs-live configuration parity"), `specs/SPEC_RUBRIC.md`:114–119 at `5467031` (heading :114, text :115–119). It was at :108–113 at `b4c3291`; the words are unchanged.

### :69 — rubric F2 "Why frozen" citation

```text
| Rubric F2 "Why frozen" (`specs/SPEC_RUBRIC.md`:37–42) | The operator-schedule justification for the 11:30 cut named there is retired by Rule F2-1, not repaired. |
```

Corrected citation: rubric F2, section "## PASSED — closed criteria" (subsection "### F2 — Session-flat time vs. breakers #4 and #5", :81), `specs/SPEC_RUBRIC.md`:87–92 at `5467031`. The cited text is F2's "**Why frozen.**" paragraph; it was at :37–42 at `b4c3291` and its words are unchanged. At `5467031` F2 is PASSED@e3323a8; the paragraph stays in F2's text.

### Other `specs/SPEC_RUBRIC.md` line citations in lines 1–111 of this file

- :8 cites :43–44 (rubric F2 unblock clause). Stale at `5467031`; already re-pointed by the amendment note above (:95) to :93–94 at `006a08b`. `specs/SPEC_RUBRIC.md` is unchanged between `006a08b` and `5467031`, so :93–94 (section "## PASSED — closed criteria", subsection "### F2 — Session-flat time vs. breakers #4 and #5", :81) also holds at `5467031`.
- :92 is the copy of :8 inside that amendment note; its :43–44 is quoted old text, not a live citation.
- :95 cites :93–94 at `006a08b`, :81, and :30–31 at `e3323a8`. Each points at the cited text at the sha it names; :93–94 and :81 also hold at `5467031`.
(eval):1: ===MANIFEST not found
````

The zsh error came from `echo ====MANIFEST`, because zsh `=` expansion stopped the chain before `tail` ran. The MANIFEST tail is printed in E3.

### E3

```
$ cd /Volumes/Sensidine/Praxis.build && tail -n 4 MANIFEST.md; printf '%s\n' '--- headings 5467031'; git show 5467031:specs/SPEC_RUBRIC.md | grep -n '^#'; for r in 65p 75,76p 77p 81p 87,92p 93,94p 114,119p; do printf '%s\n' "--- 5467031 $r"; git show 5467031:specs/SPEC_RUBRIC.md | sed -n "$r"; done
| /docs/specs/2026-11-10-live-signal-topology.md | Spec | 3 | 2026-11-12 | AMENDMENT ROW (append-only registry — adds to rows 353 and 446 for this path). Unit 2026-11-12-fgd-part-b (bead Praxis_build-fgd part B; master under D-2026-11-08-D D1, DECISION_LOG 2026-11-12T17:03:00Z item c): section "Amendment note 2 — 2026-11-12 (rubric line citations)" appended after line 200; body lines 1–200 unchanged. Stale rubric citations at :7 (:28–29) and :112 (:30) re-pointed to rubric F1, section "## PASSED — closed criteria", `specs/SPEC_RUBRIC.md`:75–76 and :77 at 5467031; no new design choice |
| /docs/specs/2026-11-10-f2-session-flat-proposal.md | Spec | 3 | 2026-11-12 | AMENDMENT ROW (append-only registry — adds to rows 354 and 448 for this path). Unit 2026-11-12-fgd-part-b (bead Praxis_build-fgd part B; master under D-2026-11-08-D D1, DECISION_LOG 2026-11-12T17:03:00Z item c): section "Amendment note 2 — 2026-11-12 (rubric line citations)" appended after line 111; body lines 1–111 unchanged. Stale rubric citations at :61 (:108–113) and :69 (:37–42) re-pointed to rubric O4 ("## OPEN — gradeable now", :114–119) and rubric F2 ("## PASSED — closed criteria", :87–92) at 5467031; :8, :92, :95 statuses listed; no new design choice |
| /docs/reports/2026-11-12-fgd-part-b-manager.md | Report | 3 | 2026-11-12 | Manager report for unit 2026-11-12-fgd-part-b (bead Praxis_build-fgd part B; master under D-2026-11-08-D D1): rubric line citation re-pointing in the topology and F2 proposal specs by appended notes, pinned-sha range checks, F-8 disposition (Flat1559.cs :31 not edited), de-identification counts; ungraded at time of row |
| /docs/reports/2026-11-12-fgd-part-b-worker1.md | Report | 3 | 2026-11-12 | ADVERSARIAL worker 1 report for unit 2026-11-12-fgd-part-b: independent re-check of every corrected rubric citation against 5467031, byte-identity of quoted old lines, head -n cmp of both specs against HEAD, no-new-design-choice check, de-identification counts; ungraded at time of row |
--- headings 5467031
1:# PRAXIS — SPEC RUBRIC
17:## FROZEN — nothing downstream may proceed until these clear
19:### F3 — Backtest fill resolution vs. acquired data granularity
33:### F4 — MFFU automation compliance
46:## PASSED — closed criteria
50:### O1 — Walk-forward gate set for the replication arm
65:### F1 — Signal-path topology vs. circuit-breaker placement
81:### F2 — Session-flat time vs. breakers #4 and #5
99:## OPEN — gradeable now
101:### O2 — `praxispush` provisioning
109:### O3 — Block-1 milestone scope statement
114:### O4 — Backtest-vs-live configuration parity
123:## Standing criteria — graded on every dispatch
256:## Process rulings — binding on the orchestrator
434:## Autonomy — D1–D5, 2026-11-08 human ruling (D-2026-11-08-D; DECISION_LOG 2026-11-08T19:57:00Z, WHO: amear)
--- 5467031 65p
### F1 — Signal-path topology vs. circuit-breaker placement
--- 5467031 75,76p
**Unblocks when.** `docs/specs/*-live-signal-topology.md` exists, is committed,
and the auditor confirms it addresses every one of the nine breakers by name.
--- 5467031 77p
**Blocks.** Block 3 entirely. Any SHM threshold derivation.
--- 5467031 81p
### F2 — Session-flat time vs. breakers #4 and #5
--- 5467031 87,92p
**Why frozen.** The plan itself carried the contradiction — the strategy
shortlist recorded the source strategy as EOD-flat while Phase 2 closure and
the Phase 3 spec locked 09:30–11:30 and built breaker #4 around it. The build
resolved it toward the paper without re-scoping the safety layer. Phase 2's
medication-window justification for the 11:30 cut is now unsupported and was
never revisited.
--- 5467031 93,94p
**Unblocks when.** A DECISIONS.md entry names the governing rule and the
15:00 disposition, and breaker specs #4 and #5 are amended to match.
--- 5467031 114,119p
### O4 — Backtest-vs-live configuration parity
Deviation C permits reverse-and-re-enter. Breakers #2 and #3 cap trades and end
the session after two consecutive losers. Block 4's gate compares live to
backtest within ±15% win rate and ±25% average trade P&L. **Required:** a
written statement of whether the Block 2 backtest runs with breakers applied,
without them, or both — and how the Block 4 gate is satisfiable if they differ.
```

Negative (c): the zsh run of the same session also printed `5467031` :28–29. The output, pasted from that run (`R() { git show "$1":specs/SPEC_RUBRIC.md | sed -n "$2"; }` defined in the same command line):

```
$ R 5467031 28,29p; R 5467031 28,29p | grep -c 'nine breakers'
optimism is invisible in the output.
**Unblocks when.** The assumption is committed and the backtest report carries
0
```

### E4 — `/tmp/fgdb-neg/cmp.sh` (run with `bash /tmp/fgdb-neg/cmp.sh`)

```
#!/bin/bash
cd /Volumes/Sensidine/Praxis.build
R() { git show "$1":specs/SPEC_RUBRIC.md | sed -n "$2"; }
for pair in "28,29p 75,76p" "30p 77p" "108,113p 114,119p" "37,42p 87,92p" "43,44p 93,94p" "32p 81p" "19p 65p"; do
  set -- $pair
  if cmp -s <(R b4c3291 $1) <(R 5467031 $2); then echo "b4c3291 $1 vs 5467031 $2: IDENTICAL"; else echo "b4c3291 $1 vs 5467031 $2: DIFFER"; diff <(R b4c3291 $1) <(R 5467031 $2); fi
done
echo "--- 5467031 120,122p (vis)"; R 5467031 120,122p | sed -n l
echo "--- b4c3291 113,116p (vis)"; R b4c3291 113,116p | sed -n l
echo "--- 006a08b vs 5467031 rubric"; if git diff --quiet 006a08b 5467031 -- specs/SPEC_RUBRIC.md; then echo "rubric unchanged 006a08b..5467031 (exit 0)"; else echo "rubric CHANGED"; fi
echo "--- e3323a8 30,31p"; R e3323a8 30,31p
echo "--- e3323a8 headings 1-8"; git show e3323a8:specs/SPEC_RUBRIC.md | grep -n '^#' | sed -n 1,8p
```

Output:

```
b4c3291 28,29p vs 5467031 75,76p: IDENTICAL
b4c3291 30p vs 5467031 77p: IDENTICAL
b4c3291 108,113p vs 5467031 114,119p: IDENTICAL
b4c3291 37,42p vs 5467031 87,92p: IDENTICAL
b4c3291 43,44p vs 5467031 93,94p: IDENTICAL
b4c3291 32p vs 5467031 81p: IDENTICAL
b4c3291 19p vs 5467031 65p: IDENTICAL
--- 5467031 120,122p (vis)
$
---$
$
--- b4c3291 113,116p (vis)
without them, or both — and how the Block 4 gate is satisfi\
able if they differ.$
$
---$
$
--- 006a08b vs 5467031 rubric
rubric unchanged 006a08b..5467031 (exit 0)
--- e3323a8 30,31p
**Unblocks when.** A DECISIONS.md entry names the governing rule and the
15:00 disposition, and breaker specs #4 and #5 are amended to match.
--- e3323a8 headings 1-8
1:# PRAXIS — SPEC RUBRIC
17:## FROZEN — nothing downstream may proceed until these clear
19:### F2 — Session-flat time vs. breakers #4 and #5
34:### F3 — Backtest fill resolution vs. acquired data granularity
48:### F4 — MFFU automation compliance
61:## PASSED — closed criteria
65:### O1 — Walk-forward gate set for the replication arm
80:### F1 — Signal-path topology vs. circuit-breaker placement
```

### E5 — `/tmp/fgdb-neg/quotes.sh` (run with `bash /tmp/fgdb-neg/quotes.sh`)

````
#!/bin/bash
cd /Volumes/Sensidine/Praxis.build
T=docs/specs/2026-11-10-live-signal-topology.md
F=docs/specs/2026-11-10-f2-session-flat-proposal.md
# extract Nth fenced text block from appended note region
blk() { sed -n "$2,\$p" "$1" | awk -v n="$3" '/^```text$/{c++;on=(c==n);next} /^```$/{on=0;next} on'; }
chk() { if cmp -s <(blk "$1" "$2" "$3") <(git show HEAD:"$1" | sed -n "$4p"); then echo "$1 block$3 vs HEAD :$4 MATCH"; else echo "$1 block$3 vs HEAD :$4 MISMATCH"; fi; }
for f in $T $F; do echo "$f fenced text blocks in note: $(sed -n '1,$p' $f | grep -c '^```text$') total; lines per block:"; done
echo "T b1 lines: $(blk $T 201 1 | wc -l) T b2: $(blk $T 201 2 | wc -l) F b1: $(blk $F 112 1 | wc -l) F b2: $(blk $F 112 2 | wc -l)"
chk $T 201 1 7; chk $T 201 2 112; chk $F 112 1 61; chk $F 112 2 69
echo "--- NEG 8a (wrong line numbers)"; chk $T 201 1 8; chk $F 112 2 68
echo "--- claim 3 head -n cmp"
cmp <(head -n 200 $T) <(git show HEAD:$T) && echo "topology head -n 200 == HEAD blob (cmp exit 0)"
cmp <(head -n 111 $F) <(git show HEAD:$F) && echo "f2 head -n 111 == HEAD blob (cmp exit 0)"
echo "--- NEG 8b"
cp $T /tmp/fgdb-neg/topo.md; cp $F /tmp/fgdb-neg/f2.md
sed -i '' '50s/a/X/' /tmp/fgdb-neg/topo.md; sed -i '' '30s/e/Q/' /tmp/fgdb-neg/f2.md
cmp <(head -n 200 /tmp/fgdb-neg/topo.md) <(git show HEAD:$T); echo "topo neg cmp exit $?"
cmp <(head -n 111 /tmp/fgdb-neg/f2.md) <(git show HEAD:$F); echo "f2 neg cmp exit $?"
echo "--- claim 7"
git diff --quiet HEAD -- ninjascript/; echo "ninjascript diff exit $?"
git diff --quiet HEAD -- specs/SPEC_RUBRIC.md; echo "SPEC_RUBRIC diff exit $?"
git diff --quiet HEAD -- DECISIONS.md; echo "DECISIONS diff exit $?"
git ls-files --others --exclude-standard -- ninjascript/ | wc -l | sed 's/^/untracked under ninjascript: /'
````


The "10 total" and "5 total" counts are for whole files (the HEAD bodies hold their own text fences). The four note blocks are blocks 1 and 2 after :201 and after :112.

Output:

````
docs/specs/2026-11-10-live-signal-topology.md fenced text blocks in note: 10 total; lines per block:
docs/specs/2026-11-10-f2-session-flat-proposal.md fenced text blocks in note: 5 total; lines per block:
T b1 lines:        1 T b2:        1 F b1:        1 F b2:        1
docs/specs/2026-11-10-live-signal-topology.md block1 vs HEAD :7 MATCH
docs/specs/2026-11-10-live-signal-topology.md block2 vs HEAD :112 MATCH
docs/specs/2026-11-10-f2-session-flat-proposal.md block1 vs HEAD :61 MATCH
docs/specs/2026-11-10-f2-session-flat-proposal.md block2 vs HEAD :69 MATCH
--- NEG 8a (wrong line numbers)
docs/specs/2026-11-10-live-signal-topology.md block1 vs HEAD :8 MISMATCH
docs/specs/2026-11-10-f2-session-flat-proposal.md block2 vs HEAD :68 MISMATCH
--- claim 3 head -n cmp
topology head -n 200 == HEAD blob (cmp exit 0)
f2 head -n 111 == HEAD blob (cmp exit 0)
--- NEG 8b
topo neg cmp exit 0
/dev/fd/63 /dev/fd/62 differ: char 2954, line 30
f2 neg cmp exit 1
--- claim 7
ninjascript diff exit 0
SPEC_RUBRIC diff exit 0
DECISIONS diff exit 1
untracked under ninjascript:        0
````

### E6 — `/tmp/fgdb-neg/more.sh` (run with `bash /tmp/fgdb-neg/more.sh`)

```
#!/bin/bash
cd /Volumes/Sensidine/Praxis.build
T=docs/specs/2026-11-10-live-signal-topology.md
F=docs/specs/2026-11-10-f2-session-flat-proposal.md
echo "--- NEG 8b redo (topology line 50 visible before change)"; sed -n 50p /tmp/fgdb-neg/topo.md | wc -c
cp $T /tmp/fgdb-neg/topo.md; printf '1s/^./Z/\nw\nq\n' | ed -s /tmp/fgdb-neg/topo.md
cmp <(head -n 200 /tmp/fgdb-neg/topo.md) <(git show HEAD:$T); echo "topo neg cmp exit $?"
echo "--- DECISIONS.md diff vs HEAD: added/removed line counts, mentions of fgd-part-b / 17:03"
git diff HEAD -- DECISIONS.md | grep -c '^+[^+]'; git diff HEAD -- DECISIONS.md | grep -c '^-[^-]'
git diff HEAD -- DECISIONS.md | grep '^+[^+]' | grep -ci 'fgd'
git diff HEAD -- DECISIONS.md | grep '^+[^+]' | grep -c '2026-11-12'
git diff HEAD -- DECISIONS.md | grep '^+[^+]' | grep -o '^+## [^—]*' | head -5
echo "--- claim 5 sweep: SPEC_RUBRIC citations in HEAD lines"
for f in $T $F; do echo "== $f"; git show HEAD:$f | grep -n 'SPEC_RUBRIC' | grep -o '^[0-9]*:\|SPEC_RUBRIC.md`*:[0-9–-]*' | tr '\n' ' '; echo; done
echo "--- rubric-word citations without SPEC_RUBRIC path (rubric + :N)"
for f in $T $F; do echo "== $f"; git show HEAD:$f | grep -n -i 'rubric' | grep -v 'SPEC_RUBRIC' | grep -n ':[0-9][0-9]*' | cut -c1-12; done
```

Output:

```
--- NEG 8b redo (topology line 50 visible before change)
       4
/dev/fd/63 /dev/fd/62 differ: char 1, line 1
topo neg cmp exit 1
--- DECISIONS.md diff vs HEAD: added/removed line counts, mentions of fgd-part-b / 17:03
62
0
0
6
+## 2026-11-12 
--- claim 5 sweep: SPEC_RUBRIC citations in HEAD lines
== docs/specs/2026-11-10-live-signal-topology.md
7: SPEC_RUBRIC.md`:28–29 112: SPEC_RUBRIC.md`:30 
== docs/specs/2026-11-10-f2-session-flat-proposal.md
8: SPEC_RUBRIC.md`:43–44 61: SPEC_RUBRIC.md`:108–113 69: SPEC_RUBRIC.md`:37–42 92: SPEC_RUBRIC.md`:43–44 95: SPEC_RUBRIC.md`:93–94 
--- rubric-word citations without SPEC_RUBRIC path (rubric + :N)
== docs/specs/2026-11-10-live-signal-topology.md
2:160:Aligne
3:168:Aligne
4:200:**F1 b
== docs/specs/2026-11-10-f2-session-flat-proposal.md
1:89:### :8 
2:103:Aligne
3:111:That s
```

### E7

```
$ cd /Volumes/Sensidine/Praxis.build && T=docs/specs/2026-11-10-live-signal-topology.md; F=docs/specs/2026-11-10-f2-session-flat-proposal.md; git diff HEAD -- DECISIONS.md | grep '^+## ' | cut -c1-120
+## 2026-11-12 — D-2026-11-12-B: R6 step 2 backtest engine authorised, first pass only (Mac-side Python event simulator 
```

The same command line also ran a fragment extraction that failed: the zsh `grep` is ugrep, which hit "exceeds complexity limits". I re-ran that part in E8 with `/usr/bin/grep`.

### E8 — `/tmp/fgdb-neg/frag.sh` (run with `bash /tmp/fgdb-neg/frag.sh`)

```
#!/bin/bash
cd /Volumes/Sensidine/Praxis.build
T=docs/specs/2026-11-10-live-signal-topology.md; F=docs/specs/2026-11-10-f2-session-flat-proposal.md
for spec in "$F 89 95 103 111" "$T 160 168 200"; do set -- $spec; f=$1; shift
 for n in "$@"; do printf '%s :%s> ' "$(basename $f)" "$n"; git show HEAD:$f | sed -n "${n}p" | /usr/bin/grep -o -E '(`specs/SPEC_RUBRIC.md`)?:[0-9]+(–[0-9]+)?( at `[0-9a-f]{7}`)?' | tr '\n' ' '; echo; done; done
echo "--- any other line in HEAD of either file with a bare :N citation near 'rubric'"
for f in $T $F; do git show HEAD:$f | /usr/bin/grep -n -i 'rubric' | /usr/bin/grep -E ':[0-9]+(–[0-9]+)?' | cut -d: -f1 | tr '\n' ' '; echo " <- $(basename $f) rubric lines with :N"; done
echo "--- F2 :95 full"; git show HEAD:$F | sed -n 95p
```

Output:

```
2026-11-10-f2-session-flat-proposal.md :89> :8 
2026-11-10-f2-session-flat-proposal.md :95> `specs/SPEC_RUBRIC.md`:93–94 :81 :30–31 at `e3323a8` :1744–1745 
2026-11-10-f2-session-flat-proposal.md :103> :2108 :2205 
2026-11-10-f2-session-flat-proposal.md :111> :75–78 
2026-11-10-live-signal-topology.md :160> :00 :00 :00 :00–18 :00 :10 
2026-11-10-live-signal-topology.md :168> :00–16 :00 :30 :00 :00 :105 
2026-11-10-live-signal-topology.md :200> :58–66 
--- any other line in HEAD of either file with a bare :N citation near 'rubric'
7 112 160 168 200  <- 2026-11-10-live-signal-topology.md rubric lines with :N
8 61 69 89 92 95 103 111  <- 2026-11-10-f2-session-flat-proposal.md rubric lines with :N
--- F2 :95 full
Aligned reading: the F2 unblock clause quoted here is at `specs/SPEC_RUBRIC.md`:93–94 at HEAD `006a08b`, inside the section "### F2 — Session-flat time vs. breakers #4 and #5" (:81), which now sits under "## PASSED — closed criteria". It was at :30–31 at `e3323a8` (D-2026-11-12-A); the rubric change at `c29d08b` moved F2 into PASSED. The quoted words are unchanged. The second citation on this line, DECISIONS.md:1744–1745 (A6), is unchanged. The line's "changes no rubric state" is true of this file; rubric F2's state was moved at `c29d08b`, not by this file.
```

### E9 — `/tmp/fgdb-neg/ctx.sh` (run with `bash /tmp/fgdb-neg/ctx.sh`)

```
#!/bin/bash
cd /Volumes/Sensidine/Praxis.build
T=docs/specs/2026-11-10-live-signal-topology.md; F=docs/specs/2026-11-10-f2-session-flat-proposal.md
c() { git show HEAD:$1 | sed -n "$2p" | /usr/bin/grep -o -E ".{0,90}$3.{0,40}"; }
c $F 103 ':2108'; c $F 103 ':2205'; c $F 111 ':75–78'; c $T 168 ':105'; c $T 200 ':58–66'
```

Output:

```
mn names now has a record: Amear's approval of Rule F2-1 (D-2026-11-11-A, V2, DECISIONS.md:2108); a DECISIONS.md entry (D-2026-11-12-A,
D-2026-11-11-A, V2, DECISIONS.md:2108); a DECISIONS.md entry (D-2026-11-12-A, DECISIONS.md:2205); the amended #4/#5 text in the breaker
 rubric F2 is PASSED@e3323a8. The rest of this file is unchanged; OPEN-F2-1 to OPEN-F2-4 (:75–78) stay open.
e stands: the lockout cannot sit on this path (bypass B3); how it is enforced is OPEN-T8 (:105), not decided here. "Depends on: F2" re
1) asks that this document address "every one of the nine breakers by name". The table at :58–66 still names all nine by the import's bo
```

### E10 — `/tmp/fgdb-neg/final2.sh` (run with `bash /tmp/fgdb-neg/final2.sh`)

```
#!/bin/bash
cd /Volumes/Sensidine/Praxis.build
T=docs/specs/2026-11-10-live-signal-topology.md; F=docs/specs/2026-11-10-f2-session-flat-proposal.md
echo "--- F2 :92 contains :8 verbatim?"; a=$(git show HEAD:$F | sed -n 8p); git show HEAD:$F | sed -n 92p | /usr/bin/grep -cF -- "$a"
echo "--- rubric PASSED@ status lines at 5467031"; git show 5467031:specs/SPEC_RUBRIC.md | /usr/bin/grep -n -o -E '(F1|F2)[^|]{0,20}PASSED@[0-9a-f]{7}' | head -4
git show 5467031:specs/SPEC_RUBRIC.md | sed -n '65,98p' | /usr/bin/grep -n -o -E 'PASSED@[0-9a-f]{7}'
echo "--- MANIFEST rows 353 354 446 448 path field"; for n in 353 354 446 448; do printf '%s: ' $n; sed -n "${n}p" MANIFEST.md | cut -d'|' -f2; done
echo "--- de-id on added lines"
{ git diff HEAD -- $T $F | /usr/bin/grep '^+' | /usr/bin/grep -v '^+++'; tail -n 4 MANIFEST.md; } > /tmp/fgdb-neg/added.txt
wc -l < /tmp/fgdb-neg/added.txt
printf 'emails: '; /usr/bin/grep -c -E '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' /tmp/fgdb-neg/added.txt
printf 'medication list size (lines): '; wc -l < /tmp/fgdb/meds.txt
printf 'medication names: '; /usr/bin/grep -c -i -f /tmp/fgdb/meds.txt /tmp/fgdb-neg/added.txt
printf 'medication-window (not a drug): '; /usr/bin/grep -c -i 'medication' /tmp/fgdb-neg/added.txt
P=$(find docs/reports/evidence -maxdepth 1 -name '2026-10-28-*-reply.png' | wc -l | tr -d ' '); printf 'matching PNG count: %s\n' "$P"
REP=$(basename "$(find docs/reports/evidence -maxdepth 1 -name '2026-10-28-*-reply.png')" | sed -E 's/^[0-9]{4}-[0-9]{2}-[0-9]{2}-//; s/-reply\.png$//; s/^mffu-//')
printf 'rep pattern length: %s\n' "${#REP}"
printf 'rep name count (grep -ci): '; /usr/bin/grep -ci -- "$REP" /tmp/fgdb-neg/added.txt
printf 'rep pattern self-test on a scratch line (expect 1): '; printf 'x %s y\n' "$REP" > /tmp/fgdb-neg/rep-pos.txt; /usr/bin/grep -ci -- "$REP" /tmp/fgdb-neg/rep-pos.txt; rm -f /tmp/fgdb-neg/rep-pos.txt
printf 'Amear count: '; /usr/bin/grep -o 'Amear' /tmp/fgdb-neg/added.txt | wc -l | tr -d ' '
echo "--- capitalised words outside backticks, minus a known-vocabulary stoplist, distinct"
sed -E 's/`[^`]*`//g' /tmp/fgdb-neg/added.txt | /usr/bin/grep -o -E '\b[A-Z][a-z]{2,}\b' | sort -u | /usr/bin/grep -v -x -E 'Amear|Added|Amendment|Block|Blocks|Body|Corrected|Deviation|Each|Other|Rubric|Session|Signal|Spec|Report|Stale|Unblocks|Unit|This|The|It|At|No|Why|Manager|Backtest|Rule|Redis|Flat|Path|Topology|Parity|Note|None|Already|Breakers|Phase|Mac|Python|Block-1|Walk|Signal-path|Session-flat|Backtest-vs-live|Configuration|Independent|Lines|Line|Copied|Exact|Each' | tr '\n' ' '; echo
```

Output:

```
--- F2 :92 contains :8 verbatim?
1
--- rubric PASSED@ status lines at 5467031
2:PASSED@b4c3291
18:PASSED@e3323a8
--- MANIFEST rows 353 354 446 448 path field
353:  /docs/specs/2026-11-10-live-signal-topology.md 
354:  /docs/specs/2026-11-10-f2-session-flat-proposal.md 
446:  /docs/specs/2026-11-10-live-signal-topology.md 
448:  /docs/specs/2026-11-10-f2-session-flat-proposal.md 
--- de-id on added lines
      52
emails: 0
medication list size (lines):       63
medication names: 0
medication-window (not a drug): 0
matching PNG count: 1
rep pattern length: 4
rep name count (grep -ci): 0
rep pattern self-test on a scratch line (expect 1): 1
Amear count: 2
--- capitalised words outside backticks, minus a known-vocabulary stoplist, distinct
Any 
```

Notes on E10:

- The `(F1|F2)[^|]{0,20}PASSED@` grep printed nothing. The `PASSED@` lines come from the second grep, numbered relative to :65. So 2 means :66, under F1 (:65), and 18 means :82, under F2 (:81).
- The list is held outside the repo at /tmp/fgdb/meds.txt so that no drug name appears in a report; its size is printed above.
- Limit of the person-name check: it finds capitalised words of 3 or more letters. A lower-case name, or a name inside backticks, would not be counted.

### E11

```
$ cd /Volumes/Sensidine/Praxis.build && /usr/bin/grep -c '2026-11-12T17:03' DECISION_LOG.md; /usr/bin/grep '2026-11-12T17:03' DECISION_LOG.md | /usr/bin/grep -o -E '\(c\)[^;]{0,160}' | head -2
1
(c) Unit 1 = bead `fgd` part B, docs only: re-point the stale rubric line citations at topology :7, :112 and F2 proposal :61, :69 by appended dated notes that cite
```

### E12

```
$ cd /Volumes/Sensidine/Praxis.build && git diff HEAD -- DECISIONS.md | /usr/bin/grep '^+## '; git show 5467031:specs/SPEC_RUBRIC.md | sed -n 28p
+## 2026-11-12 — D-2026-11-12-B: R6 step 2 backtest engine authorised, first pass only (Mac-side Python event simulator on the 1-minute file; master under D-2026-11-08-D D1)
optimism is invisible in the output.
```

## Files staged

None. I wrote only this report, which is unstaged. Scratch files are under `/tmp/fgdb-neg/`.

## Result

Result: FAIL

1. Claim 7 breaks. `git diff --quiet HEAD -- DECISIONS.md` exits 1. The working tree adds 62 lines (0 removed) holding the entry "D-2026-11-12-B: R6 step 2 backtest engine authorised, first pass only (Mac-side Python event simulator on the 1-minute file; master under D-2026-11-08-D D1)" (E12), and 0 added lines mention "fgd". So the change does not look like this unit's. Whether it is other parked work is UNVERIFIED, but the claim "DECISIONS.md does not differ from HEAD" is false as stated. The `ninjascript/` and `specs/SPEC_RUBRIC.md` parts of claim 7 hold.
2. No break in claims 1–6, 8 or 9. One observation on claim 6, not a break: the manager MANIFEST row mentions an "F-8 disposition (Flat1559.cs :31 not edited)". I did not check that disposition.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
