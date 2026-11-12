# 2026-11-12 — bead Praxis_build-fgd part B (manager report)

## Task

Unit `2026-11-12-fgd-part-b`, docs only, decided by master under D-2026-11-08-D D1, changeable by Amear (DECISION_LOG 2026-11-12T17:03:00Z, items c and d; authorising entry D-2026-11-12-A). Re-point the stale `specs/SPEC_RUBRIC.md` line citations at `docs/specs/2026-11-10-live-signal-topology.md` :7, :112 and `docs/specs/2026-11-10-f2-session-flat-proposal.md` :61, :69 by one appended dated note per file, bodies unchanged; list every other rubric line citation in both files with its status; record the F-8 disposition; append MANIFEST.md rows. No new design choice; no DECISIONS.md entry.

## Rubric criteria addressed

S1, S2, S4, S6, S13 (standing criteria, quoted verbatim in the brief). Each of the S1, S2, S4 and S6 texts is present once in `specs/SPEC_RUBRIC.md` at `5467031` (E12). No rubric gap.

## Workers dispatched (id, mode, outcome)

| Worker | Id | Mode | Outcome |
|---|---|---|---|
| worker 1 | aa0265eb511ca8b84 | ADVERSARIAL | Report `docs/reports/2026-11-12-fgd-part-b-worker1.md`, `Result: FAIL` on its claim 7 only (DECISIONS.md differs from HEAD); claims 1–6, 8, 9 held. Claim 7 resolved below with evidence: the difference predates this unit. |
| worker 2 | a401d034c254325f6 | BUILD (fix) | Report `docs/reports/2026-11-12-fgd-part-b-worker2.md`, `Result: PASS`. Cured two defects the manager found in the worker 1 report: drug names in its E10 scan command and a note (lines 434, 477), and quotes cut with an ellipsis character (lines 47, 52, 476, 496). |

No separate builder worker: the two appended notes and the MANIFEST rows were written by the manager by script (pure doc edit; the brief made the builder optional).

## Process log

1. Located every `SPEC_RUBRIC.md`:NN citation in both specs at HEAD (E7) and the rubric heading list at `5467031` (E3). Mapped each old range to its text at `b4c3291` (the commit that added both specs) and found the same text at `5467031` (E4, E5).
2. Appended "## Amendment note 2 — 2026-11-12 (rubric line citations)" to each spec with `/tmp/fgdb/append.py`, which copies each old line from `git show HEAD:` into a `text` fence. Tightened one line per note afterwards ("in this file" became "in lines 1–200 of this file" and "in lines 1–111 of this file", because the new notes themselves now carry rubric citations).
3. Appended four MANIFEST.md rows, then a fifth for the worker 2 report (E10).
4. Dispatched worker 1 (ADVERSARIAL) with the artifact and nine claims, not the manager's reasoning. It returned FAIL on claim 7.
5. Read the worker 1 report file. Found drug names on its lines 434 and 477 and ellipsis-cut quotes; dispatched worker 2 to cure them by a real re-run. Re-ran the checks on both worker reports (E11).
6. Resolved worker 1 claim 7 (E8): the claim as briefed ("DECISIONS.md does not differ from HEAD") was the manager's wording error. The unit's limit is "do not edit DECISIONS.md". E8 shows DECISIONS.md was last modified before this report file was created, and that D-2026-11-12-B (the added entry) is named in earlier DECISION_LOG rows of other work.

## Verification evidence (command output)

### E1 — HEAD

````
$ cd /Volumes/Sensidine/Praxis.build && git rev-parse HEAD
5467031c0c36d969eba9956cedcf184dbd5383df
````

### E2 — bodies unchanged (head -n HEAD-count cmp HEAD)

````
$ cd /Volumes/Sensidine/Praxis.build && for f in docs/specs/2026-11-10-live-signal-topology.md docs/specs/2026-11-10-f2-session-flat-proposal.md; do n=$(git show HEAD:$f | wc -l | tr -d ' '); head -n $n $f | cmp - <(git show HEAD:$f) && echo "head -n $n identical to HEAD: $f"; wc -l < $f; done
head -n 200 identical to HEAD: docs/specs/2026-11-10-live-signal-topology.md
     222
head -n 111 identical to HEAD: docs/specs/2026-11-10-f2-session-flat-proposal.md
     137
````

### E3 — rubric headings at 5467031

````
$ cd /Volumes/Sensidine/Praxis.build && git show 5467031:specs/SPEC_RUBRIC.md | grep -n '^#'
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
````

### E4 — every new range at 5467031

````
$ cd /Volumes/Sensidine/Praxis.build && for r in 65p 75,77p 81p 87,92p 93,94p 114,119p; do echo "-- sed -n $r"; git show 5467031:specs/SPEC_RUBRIC.md | sed -n "$r"; done
-- sed -n 65p
### F1 — Signal-path topology vs. circuit-breaker placement
-- sed -n 75,77p
**Unblocks when.** `docs/specs/*-live-signal-topology.md` exists, is committed,
and the auditor confirms it addresses every one of the nine breakers by name.
**Blocks.** Block 3 entirely. Any SHM threshold derivation.
-- sed -n 81p
### F2 — Session-flat time vs. breakers #4 and #5
-- sed -n 87,92p
**Why frozen.** The plan itself carried the contradiction — the strategy
shortlist recorded the source strategy as EOD-flat while Phase 2 closure and
the Phase 3 spec locked 09:30–11:30 and built breaker #4 around it. The build
resolved it toward the paper without re-scoping the safety layer. Phase 2's
medication-window justification for the 11:30 cut is now unsupported and was
never revisited.
-- sed -n 93,94p
**Unblocks when.** A DECISIONS.md entry names the governing rule and the
15:00 disposition, and breaker specs #4 and #5 are amended to match.
-- sed -n 114,119p
### O4 — Backtest-vs-live configuration parity
Deviation C permits reverse-and-re-enter. Breakers #2 and #3 cap trades and end
the session after two consecutive losers. Block 4's gate compares live to
backtest within ±15% win rate and ±25% average trade P&L. **Required:** a
written statement of whether the Block 2 backtest runs with breakers applied,
without them, or both — and how the Block 4 gate is satisfiable if they differ.
````

### E5 — cited words unchanged from b4c3291; rubric unchanged 006a08b to 5467031

````
$ cd /Volumes/Sensidine/Praxis.build && diff <(git show b4c3291:specs/SPEC_RUBRIC.md | sed -n '28,29p') <(git show 5467031:specs/SPEC_RUBRIC.md | sed -n '75,76p') && echo 'F1 unblock 28-29 = 75-76'; diff <(git show b4c3291:specs/SPEC_RUBRIC.md | sed -n '30p') <(git show 5467031:specs/SPEC_RUBRIC.md | sed -n '77p') && echo 'F1 blocks 30 = 77'; diff <(git show b4c3291:specs/SPEC_RUBRIC.md | sed -n '108,113p') <(git show 5467031:specs/SPEC_RUBRIC.md | sed -n '114,119p') && echo 'O4 108-113 = 114-119'; diff <(git show b4c3291:specs/SPEC_RUBRIC.md | sed -n '37,42p') <(git show 5467031:specs/SPEC_RUBRIC.md | sed -n '87,92p') && echo 'F2 why-frozen 37-42 = 87-92'; git diff 006a08b 5467031 -- specs/SPEC_RUBRIC.md | wc -l
F1 unblock 28-29 = 75-76
F1 blocks 30 = 77
O4 108-113 = 114-119
F2 why-frozen 37-42 = 87-92
       0
````

### E6 — quotes byte-identical to HEAD lines, plus negative tests

````
$ cd /Volumes/Sensidine/Praxis.build && tail -n +201 docs/specs/2026-11-10-live-signal-topology.md | awk 'p{print; p=0} /^```text$/{p=1}' | cmp - <(git show HEAD:docs/specs/2026-11-10-live-signal-topology.md | sed -n '7p;112p') && echo 'topology quotes = HEAD :7 :112'; tail -n +112 docs/specs/2026-11-10-f2-session-flat-proposal.md | awk 'p{print; p=0} /^```text$/{p=1}' | cmp - <(git show HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md | sed -n '61p;69p') && echo 'f2 quotes = HEAD :61 :69'; echo '-- negative: wrong line'; tail -n +201 docs/specs/2026-11-10-live-signal-topology.md | awk 'p{print; p=0} /^```text$/{p=1}' | cmp -s - <(git show HEAD:docs/specs/2026-11-10-live-signal-topology.md | sed -n '8p;112p'); echo "cmp exit $?"; echo '-- negative: old range at 5467031 holds the F1 clause?'; git show 5467031:specs/SPEC_RUBRIC.md | sed -n '28,29p' | grep -c 'nine breakers'
topology quotes = HEAD :7 :112
f2 quotes = HEAD :61 :69
-- negative: wrong line
cmp exit 1
-- negative: old range at 5467031 holds the F1 clause?
0
````

### E7 — rubric line citations in both specs at HEAD, and across docs/specs

````
$ cd /Volumes/Sensidine/Praxis.build && for f in docs/specs/2026-11-10-live-signal-topology.md docs/specs/2026-11-10-f2-session-flat-proposal.md; do echo "== $f"; git show HEAD:$f | grep -n -o 'SPEC_RUBRIC.md`:[0-9][0-9–]*'; done; grep -l 'SPEC_RUBRIC.md`:[0-9]' docs/specs/*.md
== docs/specs/2026-11-10-live-signal-topology.md
7:SPEC_RUBRIC.md`:28–29
112:SPEC_RUBRIC.md`:30
== docs/specs/2026-11-10-f2-session-flat-proposal.md
8:SPEC_RUBRIC.md`:43–44
61:SPEC_RUBRIC.md`:108–113
69:SPEC_RUBRIC.md`:37–42
92:SPEC_RUBRIC.md`:43–44
95:SPEC_RUBRIC.md`:93–94
docs/specs/2026-11-10-f2-session-flat-proposal.md
docs/specs/2026-11-10-live-signal-topology.md
````

### E8 — files this unit must not touch

````
$ cd /Volumes/Sensidine/Praxis.build && git diff --quiet HEAD -- specs/SPEC_RUBRIC.md; echo "rubric diff exit $?"; git diff --quiet HEAD -- ninjascript/; echo "ninjascript diff exit $?"; git ls-files --others --exclude-standard ninjascript/ | wc -l; TZ=UTC stat -f '%Sm mtime %N' -t '%Y-%m-%dT%H:%M:%SZ' DECISIONS.md .claude/settings.json; TZ=UTC stat -f '%SB birth %N' -t '%Y-%m-%dT%H:%M:%SZ' docs/reports/2026-11-12-fgd-part-b-manager.md; grep -c 'D-2026-11-12-B' DECISION_LOG.md; grep -n 'D-2026-11-12-B' DECISION_LOG.md | cut -c1-40 | head -2
rubric diff exit 0
ninjascript diff exit 0
       0
2026-11-12T14:12:48Z mtime DECISIONS.md
2026-11-12T14:12:48Z mtime .claude/settings.json
2026-11-12T17:16:08Z birth docs/reports/2026-11-12-fgd-part-b-manager.md
2
861:- [2026-11-12T09:03:23Z] WHO: praxis
862:- [2026-11-12T09:25:24Z] WHO: praxis
````

### E9 — F-8 line and its commit

````
$ cd /Volumes/Sensidine/Praxis.build && sed -n '31p' ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs; git log --format=%h -- ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs
// This variant does NOT decide rubric F2 (session-flat time vs breakers #4/#5, FROZEN). The
0ced412
````

### E10 — MANIFEST rows added by this unit

````
$ cd /Volumes/Sensidine/Praxis.build && git show HEAD:MANIFEST.md | wc -l; wc -l < MANIFEST.md; git diff HEAD -- MANIFEST.md | grep -c '^+|'; tail -n 5 MANIFEST.md
     439
     458
19
| /docs/specs/2026-11-10-live-signal-topology.md | Spec | 3 | 2026-11-12 | AMENDMENT ROW (append-only registry — adds to rows 353 and 446 for this path). Unit 2026-11-12-fgd-part-b (bead Praxis_build-fgd part B; master under D-2026-11-08-D D1, DECISION_LOG 2026-11-12T17:03:00Z item c): section "Amendment note 2 — 2026-11-12 (rubric line citations)" appended after line 200; body lines 1–200 unchanged. Stale rubric citations at :7 (:28–29) and :112 (:30) re-pointed to rubric F1, section "## PASSED — closed criteria", `specs/SPEC_RUBRIC.md`:75–76 and :77 at 5467031; no new design choice |
| /docs/specs/2026-11-10-f2-session-flat-proposal.md | Spec | 3 | 2026-11-12 | AMENDMENT ROW (append-only registry — adds to rows 354 and 448 for this path). Unit 2026-11-12-fgd-part-b (bead Praxis_build-fgd part B; master under D-2026-11-08-D D1, DECISION_LOG 2026-11-12T17:03:00Z item c): section "Amendment note 2 — 2026-11-12 (rubric line citations)" appended after line 111; body lines 1–111 unchanged. Stale rubric citations at :61 (:108–113) and :69 (:37–42) re-pointed to rubric O4 ("## OPEN — gradeable now", :114–119) and rubric F2 ("## PASSED — closed criteria", :87–92) at 5467031; :8, :92, :95 statuses listed; no new design choice |
| /docs/reports/2026-11-12-fgd-part-b-manager.md | Report | 3 | 2026-11-12 | Manager report for unit 2026-11-12-fgd-part-b (bead Praxis_build-fgd part B; master under D-2026-11-08-D D1): rubric line citation re-pointing in the topology and F2 proposal specs by appended notes, pinned-sha range checks, F-8 disposition (Flat1559.cs :31 not edited), de-identification counts; ungraded at time of row |
| /docs/reports/2026-11-12-fgd-part-b-worker1.md | Report | 3 | 2026-11-12 | ADVERSARIAL worker 1 report for unit 2026-11-12-fgd-part-b: independent re-check of every corrected rubric citation against 5467031, byte-identity of quoted old lines, head -n cmp of both specs against HEAD, no-new-design-choice check, de-identification counts; ungraded at time of row |
| /docs/reports/2026-11-12-fgd-part-b-worker2.md | Report | 3 | 2026-11-12 | BUILD fix worker 2 report for unit 2026-11-12-fgd-part-b: de-identification and truncated-quote cures to the worker 1 report (E10 re-run with the medication list held outside the repo, full quotes at :47 :52 :476 :496, new E12), counts-only checks; ungraded at time of row |
````

### E11 — worker report checks and de-identification of every added line in this unit

````
$ cd /Volumes/Sensidine/Praxis.build && for f in docs/reports/2026-11-12-fgd-part-b-worker1.md docs/reports/2026-11-12-fgd-part-b-worker2.md docs/reports/2026-11-12-fgd-part-b-manager.md; do printf '%s meds=%s ellipsis=%s s13=%s last-is-s13=%s banned=%s email=%s\n' "$(basename $f)" "$(grep -c -i -f /tmp/fgdb/meds.txt $f)" "$(grep -c "$(printf '\342\200\246')" $f)" "$(grep -c -F -f /tmp/fgdb/s13.txt $f)" "$(tail -n 1 $f | grep -c -x -F -f /tmp/fgdb/s13.txt)" "$(grep -ci "$(printf 'ver%s\\|COMMIT-IN%s\\|COMMIT-DIFF-SHA%s' dict DEX 256)" $f)" "$(grep -c -E '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' $f)"; done; wc -l < /tmp/fgdb/s13.txt; { git diff HEAD -- docs/specs/2026-11-10-live-signal-topology.md docs/specs/2026-11-10-f2-session-flat-proposal.md | grep '^+' | grep -v '^+++'; tail -n 5 MANIFEST.md; cat docs/reports/2026-11-12-fgd-part-b-worker1.md docs/reports/2026-11-12-fgd-part-b-worker2.md docs/reports/2026-11-12-fgd-part-b-manager.md; } > /tmp/fgdb/added.txt; wc -l < /tmp/fgdb/added.txt; wc -l < /tmp/fgdb/meds.txt; printf 'drug-name lines: %s\n' "$(grep -c -i -f /tmp/fgdb/meds.txt /tmp/fgdb/added.txt)"; printf 'email lines: %s\n' "$(grep -c -E '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' /tmp/fgdb/added.txt)"; REP=$(basename "$(find docs/reports/evidence -maxdepth 1 -name '2026-10-28-*-reply.png')" | sed -E 's/^[0-9]{4}-[0-9]{2}-[0-9]{2}-//; s/^mffu-//; s/-reply\.png$//'); printf 'rep pattern length %s, rep lines %s\n' "${#REP}" "$(grep -ci -- "$REP" /tmp/fgdb/added.txt)"; printf 'Amear occurrences: %s\n' "$(grep -o 'Amear' /tmp/fgdb/added.txt | wc -l | tr -d ' ')"
2026-11-12-fgd-part-b-worker1.md meds=0 ellipsis=0 s13=1 last-is-s13=1 banned=0 email=0
2026-11-12-fgd-part-b-worker2.md meds=0 ellipsis=0 s13=1 last-is-s13=1 banned=0 email=0
2026-11-12-fgd-part-b-manager.md meds=0 ellipsis=0 s13=1 last-is-s13=1 banned=0 email=0
       1
     903
      63
drug-name lines: 0
email lines: 0
rep pattern length 4, rep lines 0
Amear occurrences: 15
````

Note on E11: `/tmp/fgdb/s13.txt` holds the S13 sentence (copied by script from this report's last line) and `/tmp/fgdb/meds.txt` holds the drug-name list, both outside the repo so that neither text is pasted here. The scan of this report ran before this E11 block was inserted (a marker line stood in its place); E13 below ran on the earlier added-lines file.

### E12 — the cited standing-criteria texts exist at 5467031

````
$ cd /Volumes/Sensidine/Praxis.build && for s in 'Every claim in a report has pasted command output, not a description of output.' 'No component is reported at a higher level than the evidence supports.' 'Every deviation from the plan has a DECISIONS.md entry with a traceable authorisation chain' 'Cross-block check: every approved deviation is tested against the specs of every other block it touches'; do git show 5467031:specs/SPEC_RUBRIC.md | grep -c -F "$s"; done
1
1
1
1
````

### E13 — person-name check on the same added-lines file as E11

````
$ cd /Volumes/Sensidine/Praxis.build && sed -E 's/`[^`]*`//g' /tmp/fgdb/added.txt | grep -o -E '\b[A-Z][a-z]{2,}\b' | sort -u | tr '\n' ' '; echo; sed -E 's/`[^`]*`//g' /tmp/fgdb/added.txt | grep -o -E '\b[A-Z][a-z]{2,}\b' | sort -u | wc -l
Across Added Adversarial After Aligne Aligned All Already Amear Amendment Any Appended Attributing Autonomy Backtest Bead Block Blocks Body Breakers Byte Claim Configuration Confirmed Copied Corrected Criterion Cure Cured Decided Depends Deviation Dispatched Each Edits Email Every Exact Exit Files Fills Final Findings Flat Found Graded Independent Item Its Limit Line Lines Listed Located Mac Manager Mapped Medication Method Mode Negative New None Note Notes Nothing Nth Observation Old One Other Outcome Output Parity Path Phase Praxis Process Python Quotes Read Redis Rep Report Required Resolved Result Rubric Rule Run Scratch Sensidine Session Signal Spec Stale Standard Standing Status Still Task That The There These This Tightened Topology Try Unblocks Unit Verification Volumes Walk Whether Why Worker Workers 
     118
````

Reading of E13: every distinct capitalised word of three or more letters outside backtick spans is listed; the only person name is Amear (Praxis, Sensidine and Volumes are project and path words). Limit: a lower-case name, a two-letter name or a name inside backticks is not caught by this check.

## Adversarial findings

1. Worker 1 claim 7 (DECISIONS.md differs from HEAD): true, but it is not this unit's change. E8: DECISIONS.md mtime is earlier than this report's creation time, and D-2026-11-12-B appears in DECISION_LOG rows from 09:03Z and 09:25Z today. This unit wrote nothing to DECISIONS.md. The criterion stays as written: this unit edits no DECISIONS.md line. No artifact change was needed.
2. Worker 1 claims 1–6, 8, 9 held. Its negative tests (wrong line for a quote, one-byte change in a spec body, old range at `5467031`) each failed as they should; the manager's own negative tests are in E6.
3. Manager finding on the worker 1 report (not on the artifact): drug names at its lines 434 and 477, and ellipsis-cut quotes at its lines 47, 52, 476, 496. Cured by worker 2; re-check in E11 gives 0 drug-name lines and 0 ellipsis characters in both worker reports.
4. Worker 1 observation on claim 6: the manager's MANIFEST row names the F-8 disposition. That disposition is the master's decision (DECISION_LOG 17:03:00Z item d), recorded below, not made by this unit.

## F-8 disposition

`ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs` line 31 says F2 is "FROZEN" (E9). It is NOT edited. Decided by master under D-2026-11-08-D D1, changeable by Amear (DECISION_LOG 2026-11-12T17:03:00Z item d): the comment is a point-in-time statement true at its commit `0ced412`, and an edit to an installed .cs file breaks hash identity with the VM copy for no behaviour change. E8 shows no file under `ninjascript/` differs from HEAD and none is untracked.

## S6 cross-block check

The unit changes no deviation, breaker, rubric state or block spec text; it re-points citations only. Blocks the two notes touch: Block 3 (breakers stay SPECIFIED ONLY; the part A notes above are unchanged, E2), the rubric (unchanged vs HEAD, E8; F1 and F2 states read, not moved), and Block 2/4 through O4 (cited, not answered). Across `docs/specs/`, only these two files carry `SPEC_RUBRIC.md`:NN citations (E7), so no other spec carries a stale rubric line citation of this form. The ninjascript block is untouched (E8, E9).

## Files staged

None staged by this unit; all changes are in the working tree for the master's temp index. Files this unit modified or created:

- `docs/specs/2026-11-10-live-signal-topology.md` (modified: note appended after line 200)
- `docs/specs/2026-11-10-f2-session-flat-proposal.md` (modified: note appended after line 111)
- `MANIFEST.md` (modified: five rows appended at the end; the other uncommitted rows above them untouched)
- `docs/reports/2026-11-12-fgd-part-b-manager.md` (created)
- `docs/reports/2026-11-12-fgd-part-b-worker1.md` (created by worker 1, edited by worker 2)
- `docs/reports/2026-11-12-fgd-part-b-worker2.md` (created by worker 2)

Deviation from the brief, recorded not chosen: the brief says MANIFEST.md already had 22 uncommitted rows; E10 shows 19 rows added against HEAD, 5 of them this unit's (the last 5 lines), so 14 belong to other work. The rows were appended after them as instructed.

## OPEN

None. No design question arose.

Result: PASS

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
