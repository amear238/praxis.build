# Housekeeping part 2a — manager report (unit 2026-11-10-housekeeping-2a; beads Praxis_build-trn, Praxis_build-75n; rubric C2 filer's sentence)

Standing limitation: Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

(This unit states no backtest or P&L figure; the sentence is carried as house style under S13.)

## Task

Scope is the "NEXT UNIT" text of DECISION_LOG row 2026-11-10T07:19:00Z (line 787), decided by master under D-2026-11-08-D D1: (a) bead `trn`: move the uncommitted DISPATCH_LOG row 2026-11-07T22:17:00Z so HEAD is a byte prefix of the working tree; (b) bead `75n`: append a dated pointer note for the stale rubric line cites in DECISIONS.md D-2026-11-08-C/-D, never editing the entries; (c) one appended filer's sentence in the rubric C2 paragraph citing the live trip row 06:12:00Z (A11, C2). Filing only. Start stamp `date -u` = 2026-11-10T07:19:07Z. HEAD = origin/main = `18d94a5`.

Not done here, owed to the master: the DISPATCH_LOG flush (a commit), and the bead `trn` text "record the move in DECISION_LOG" (DECISION_LOG is the master's ledger). Beads stay open; only the master closes them.

## Rubric criteria addressed

S1, S2, S12, S13 (specs/SPEC_RUBRIC.md :121, :122, :132, :133 at HEAD).
- S1: every claim below has pasted output in "Verification evidence (command output)".
- S2: levels stated as reached. Item A: the move is DONE in the working tree and verified by `cmp`; the flush is NOT done (no commit). Item B: a filer's note, not a ruling. Item C: the rubric sentence reports the master's live trip as recorded in DECISION_LOG; the manager did not re-run the trip. The identification of the July hunk at HEAD :335–344 is by position (labelled so in the note).
- S12: this unit is the flush side for DISPATCH_LOG: it removes the mid-file row that made every flush fail the append-only check. It adds no writer.
- S13: the sentence is carried once, at the top.

## Workers dispatched (id, mode, outcome)

| id | agent | mode | outcome |
|---|---|---|---|
| ADV1 | a94724bbc96e42cbb | ADVERSARIAL (artifacts and criteria only; foreground, Rule Zero) | 1 break (report was a skeleton when it read it), 3 minors; items A and C and B checks (1)–(5) held |

No BUILD worker: the three edits were done by the manager with scripts (filing edits, each a pure append or a byte-preserving move); decided by manager under D-2026-11-08-D D1, to keep the one-adversary budget for the check. ADV1 could not write `/tmp/hk2a-adv/report.md` (it says the tool refused the file), so its findings exist only in its returned message; they are quoted in "Adversarial findings".

## Process log

- 07:19:07Z baseline: HEAD `18d94a5` = origin/main; real index holds only the PNG; DISPATCH_LOG 2344 lines.
- 07:20:29Z item A: `/tmp/hk2a/move_row.py` dry-run, then real run. It reads the file and rewrites, in the same open handle, only the first 2020 lines (same byte length); it does not truncate, so hook rows appended at the end are not touched. Asserts: the row is at line 2012, lines 1–2011 equal HEAD, lines 2013–2020 equal HEAD 2012–2019, the stamp occurs once, and the old and new regions have the same length and the same multiset of lines.
- Item B: mapped every rubric cite in DECISIONS.md :1808–2007 from `6c4c109` (the rubric the entries cite; filed in `ec73ba8`) to `18d94a5` using `/tmp/hk2a/map.sh` (exact-line `grep -x -F`) and block `cmp`. Appended the note at the end of DECISIONS.md.
- Item C: `/tmp/hk2a/rubric_c2.py` inserted the paragraph after the blank line at :332, asserting the anchors.
- MANIFEST: one row appended at the end for this report.
- ADV1 dispatched (foreground) 07:23Z, returned 07:27Z. Fixes from its minors: (1) item C "never pushed" replaced by the observation in the row (`git ls-remote --heads origin | grep -c c2trip` printed 0); the rewrap made the paragraph 10 text lines, so the insert is 11 lines; (2) the note's shift text corrected to 11 lines after `:332`; (3) "wrong" for MANIFEST row 308 replaced by "does not match the committed file", with the 413-before-Correction-1 explanation. The break (skeleton report) is closed by this report.
- Negative tests run after the move (below, V-NEG).

## Verification evidence (command output)

V0 — start state.
```
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-11-10T07:19:07Z
$ git rev-parse --short HEAD; git rev-parse --short origin/main
18d94a5
18d94a5
$ git diff --cached --name-status
A	docs/reports/evidence/2026-10-28-mffu-davi-reply.png
$ wc -l DISPATCH_LOG.md
    2344 DISPATCH_LOG.md
```

V-A1 — DISPATCH_LOG before the move.
```
$ git show HEAD:DISPATCH_LOG.md | wc -l
    2019
$ git diff HEAD -U0 -- DISPATCH_LOG.md | grep '^@@'
@@ -2011,0 +2012 @@ Append-only. Every Agent dispatch + outcome. Row schema:
@@ -2019,0 +2021,324 @@ Append-only. Every Agent dispatch + outcome. Row schema:
```

V-A2 — the move (dry run, then real run, then checks).
```
$ python3 -I /tmp/hk2a/move_row.py --dry
lines_before_write 2344
row_sha256_before a25a64209b1738fce46e36bcc20f4c1a05265349961ee9b54093e6c022504e8f bytes 1326
DRY: no write
$ date -u ...; python3 -I /tmp/hk2a/move_row.py && wc -l DISPATCH_LOG.md && cmp <(git show HEAD:DISPATCH_LOG.md) <(head -n 2019 DISPATCH_LOG.md); echo "cmp exit $?"; git diff HEAD -U0 -- DISPATCH_LOG.md | grep '^@@'; sed -n 2020p DISPATCH_LOG.md | shasum -a 256
2026-11-10T07:20:29Z
lines_before_write 2344
row_sha256_before a25a64209b1738fce46e36bcc20f4c1a05265349961ee9b54093e6c022504e8f bytes 1326
lines_after_write 2344
row_sha256_after a25a64209b1738fce46e36bcc20f4c1a05265349961ee9b54093e6c022504e8f bytes 1326
    2344 DISPATCH_LOG.md
cmp exit 0
@@ -2019,0 +2020,325 @@ Append-only. Every Agent dispatch + outcome. Row schema:
a25a64209b1738fce46e36bcc20f4c1a05265349961ee9b54093e6c022504e8f  -
```

V-A3 — line count before and after, explained by hook rows newer than the start stamp (run 07:28:39Z).
```
$ wc -l DISPATCH_LOG.md
    2346 DISPATCH_LOG.md
$ awk '... stamp > "2026-11-10T07:19:07Z" ...' DISPATCH_LOG.md
2345: - [2026-11-10T07:23:19Z] WHO: praxis-worker | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | W
2346: - [2026-11-10T07:27:52Z] WHO: praxis-worker | WHAT: subagent closed | WHY: hook-recorded at SubagentStop, keye
$ cmp <(git show HEAD:DISPATCH_LOG.md) <(head -n 2019 DISPATCH_LOG.md); echo "cmp exit $?"
cmp exit 0
$ sed -n 2020p DISPATCH_LOG.md | shasum -a 256
a25a64209b1738fce46e36bcc20f4c1a05265349961ee9b54093e6c022504e8f  -
$ grep -c '^- \[2026-11-07T22:17:00Z\]' DISPATCH_LOG.md ; grep -n ... | cut -c1-40
1
2020:- [2026-11-07T22:17:00Z] WHO: praxi
```
2344 at start, 2344 right after the move, 2346 now: +2 = the two rows newer than 07:19:07Z (ADV1's spawn and close), both at the end.

V-NEG — negative tests (the checks do fire).
```
$ python3 -I /tmp/hk2a/move_row.py --dry      # re-run after the move: refuses
AssertionError: b'- [2026-11-07T21:48:46Z] WHO: praxis-man'
$ # copy of HEAD with the row re-inserted at the old position 2012:
$ cmp <(git show HEAD:DISPATCH_LOG.md) <(head -n 2019 /tmp/hk2a/neg.md); echo "neg cmp exit $?"
/dev/fd/63 /dev/fd/62 differ: char 678093, line 2012
neg cmp exit 1
$ git diff --no-index -U0 <(git show HEAD:DISPATCH_LOG.md) /tmp/hk2a/neg.md | grep "^@@"
@@ -2011,0 +2012 @@ Append-only. Every Agent dispatch + outcome. Row schema:
```

V-B1 — every rubric cite in D-2026-11-08-C (:1808–1890) and D-2026-11-08-D (:1891–2007).
```
$ grep -n -o 'SPEC_RUBRIC\.md`\?:[0-9][0-9–-]*' DECISIONS.md | awk -F: '$1>=1808'
1857:SPEC_RUBRIC.md`:252
1858:SPEC_RUBRIC.md`:246–260
1862:SPEC_RUBRIC.md`:77
1881:SPEC_RUBRIC.md`:19
1887:SPEC_RUBRIC.md`:121
1989:SPEC_RUBRIC.md`:122
$ grep -n -o -E 'rubric[^.;]{0,20}:[0-9]+(–[0-9]+)?' DECISIONS.md | awk -F: '$1>=1808'
1858:rubric :285–289
1858:rubric :3–6
1862:rubric's own label at :81–82
1862:rubric :76–88
1881:rubric :121, :123
2003:rubric :122
$ awk 'NR>=1808 && NR<=2007 && /[Rr]ubric|SPEC_RUBRIC/ {print NR}' DECISIONS.md | paste -sd' ' -
1845 1857 1858 1862 1864 1872 1875 1877 1881 1885 1887 1961 1986 1989 1997 2003
```
Lines 1845, 1872, 1875, 1877, 1885, 1961, 1986, 1997 were read in context: they name the rubric or a rubric unit but cite no rubric line. The full texts of 1858, 1862, 1864, 1881, 1887 and 2003 were read; the bare cites in them (1862: `:74`, `:89`, `:17`, `:111`, `:244`, `:12–13`; 1864: "working tree :275–284"; 1881: `:32, :47, :61`, `(:17)`, `(:76–88)`; 1887: `(:252)`; 1858: "working tree :287, HEAD :277", ":275–279 at HEAD") are all in the note. The other `:NN` cites in those lines point to the answers files, DECISION_LOG or DECISIONS.md.

V-B2 — the entries cite `6c4c109`'s rubric (filed in `ec73ba8`, between `6c4c109` and `cec36b8`).
```
$ git log --format='%h %ad %s' --date=iso -- specs/SPEC_RUBRIC.md | head -4 | cut -c1-60
23556aa 2026-11-10 01:09:41 -0500 hooks: C2 park-commit gate
cec36b8 2026-11-09 09:24:43 -0500 specs: SPEC_RUBRIC rubric u
6c4c109 2026-11-08 11:10:57 -0500 specs: SPEC_RUBRIC lines 3-
69ec506 2026-11-06 17:08:54 -0500 D-2026-11-06-B: Amear's eve
$ git log --format='%h %ad %s' --date=iso -- DECISIONS.md | head -1 | cut -c1-60
ec73ba8 2026-11-09 00:53:19 -0500 docs: D-2026-11-08-C (Amear
$ git show 6c4c109:specs/SPEC_RUBRIC.md | wc -l ; git show cec36b8:specs/SPEC_RUBRIC.md | wc -l ; git show 23556aa:specs/SPEC_RUBRIC.md | wc -l
     345
     416
     447
```

V-B3 — old line → same text at `18d94a5` (`/tmp/hk2a/map.sh`: exact-line match, `grep -n -x -F`).
```
6c4c109:3 -> HEAD:3 | Authority: the scoping agent (Claude.a
6c4c109:6 -> HEAD:6 | 2026-11-08T15:05:00Z, WHO: amear).
6c4c109:12 -> HEAD:12 | State values: `FROZEN` (blocks depen
6c4c109:13 -> HEAD:13 | `PASSED@<sha>` (graded and closed) ·
6c4c109:17 -> HEAD:17 | ## FROZEN — nothing downstream may p
6c4c109:19 -> HEAD:19 | ### F1 — Signal-path topology vs. ci
6c4c109:32 -> HEAD:32 | ### F2 — Session-flat time vs. break
6c4c109:47 -> HEAD:47 | ### F3 — Backtest fill resolution vs
6c4c109:61 -> HEAD:61 | ### F4 — MFFU automation compliance
6c4c109:74 -> HEAD:93 | ## OPEN — gradeable now
6c4c109:76 -> HEAD:78 | ### O1 — Walk-forward gate set for t
6c4c109:77 -> HEAD:79 | **State:** PASSED@a2f1067. Amear's r
6c4c109:81 -> HEAD:83 | (iii)). Marking O1 PASSED, and the s
6c4c109:82 -> HEAD:84 | are the master's reading (filing not
6c4c109:89 -> HEAD:95 | ### O2 — `praxispush` provisioning
6c4c109:111 -> HEAD:117 | ## Standing criteria — graded on e
6c4c109:121 -> HEAD:127 | | S7 | Nothing is committed while 
6c4c109:122 -> HEAD:128 | | S8 | No question that belongs to
6c4c109:123 -> HEAD:129 | | S9 | Any config field a guarante
6c4c109:244 -> HEAD:250 | ## Process rulings — binding on th
6c4c109:246 -> HEAD:252 | **Park rule — amended to ABSOLUTE,
6c4c109:252 -> HEAD:258 | 1. Commit the work to a branch `pa
6c4c109:260 -> HEAD:266 | same change by the time the rule f
6c4c109:275 -> HEAD:345 | **Absolutes are amended between se
6c4c109:277 -> HEAD:347 | A rule declared absolute is **neve
6c4c109:279 -> HEAD:349 | a human, in a session that is not 
$ # block compare of cited ranges
6c4c109:76,88 == 18d94a5:78,90 (cmp silent)
6c4c109:246,260 == 18d94a5:252,266 (cmp silent)
6c4c109:275,279 == 18d94a5:345,349 (cmp silent)
6c4c109:3,6 == 18d94a5:3,6 (cmp silent)
6c4c109:12,13 == 18d94a5:12,13 (cmp silent)
6c4c109:81,82 == 18d94a5:83,84 (cmp silent)
$ git show HEAD:specs/SPEC_RUBRIC.md | shasum -a 256     # the file map.sh read
20ba6a34395e1173b3b788ade765dadc5bf3d2669f9838814a1f76b1791c0e36  -
$ grep -n '^## ' (HEAD rubric)
17:## FROZEN — nothing downstream may proceed until these clear
74:## PASSED — closed criteria
93:## OPEN — gradeable now
117:## Standing criteria — graded on every dispatch
250:## Process rulings — binding on the orchestrator
417:## Autonomy — D1–D5, 2026-11-08 human ruling (D-2026-11-08-D; DECISION_LOG 2026-11-08T19:57:00Z, WHO: amear)
$ sed -n 335,336p; sed -n 344,345p (HEAD rubric)
**No-verdict returns — R-A / R-B / R-C, ruled 2026-07-27. Source: DECISION_LOG
row `2026-07-27T18:15Z`.**

**Absolutes are amended between sessions only — 2026-07-26 human ruling.**
```
The July hunk (C8 entry: working tree :275–284, hunk `@@ -274,0 +275,10 @@`, so the absolutes heading was at working-tree :285) is placed at HEAD :335–344 by position: the ten lines directly above the absolutes heading at HEAD :345. MANIFEST row 308 states the hunk landed byte-for-byte; the manager did not re-hash it.

V-B4 — MANIFEST row 308 and the cec36b8 line count.
```
$ git show HEAD:MANIFEST.md | sed -n 308p | python3 -I -c '...print(repr(s[i-80:i+40]))'
'8-C; D1-D5 of D-2026-11-08-D): specs/SPEC_RUBRIC.md edited (HEAD 345 lines, now 413): the July R-A/R-B/R-C hunk landed b'
$ git show cec36b8:specs/SPEC_RUBRIC.md | wc -l
     416
$ sed -n 691p docs/reports/2026-11-09-rubric-unit-manager.md (excerpt)
... `wc -l` printed 413 for the pre-file and 416 for the current file. ...
```

V-B5 — pure append.
```
$ git diff HEAD -U0 -- DECISIONS.md | grep '^@@'
@@ -2007,0 +2008,17 @@ Nothing else.
```

V-C1 — the row the sentence reports (DECISION_LOG.md:783, excerpts as in the file).
```
$ grep -n '06:12:00Z' DECISION_LOG.md | cut -c1-80
783:- [2026-11-10T06:12:00Z] WHO: praxis-master | WHAT: **C2 LIVE TRIP, OBSERVED
(a) Positive: local branch `parked/Praxis_build-c2trip` at `23556aa` ... bare `GIT_INDEX_FILE=/tmp/idx-trip git commit -m …` with NO audit run → git printed `[parked/Praxis_build-c2trip a27250f] … 1 file changed`. The gate's exemption stderr line is not shown on exit 0, so that the exemption arm (not another allow) admitted it is INFERRED by elimination from (b). Then `git checkout -q main`, `git branch -D` → `Deleted branch parked/Praxis_build-c2trip (was a27250f)`; `git ls-remote --heads origin | grep -c c2trip` = 0 (never pushed). (b) Negative: on `main`, `/tmp/idx-neg` = HEAD + `c2-negative-trip.txt`, no audit → DENIED: "Commit denied: no audit PASS token for this exact staged diff under index '/private/tmp/idx-neg' …".
```

V-C2 — rubric diff, and the +11 shift.
```
$ git diff HEAD -- specs/SPEC_RUBRIC.md
diff --git a/specs/SPEC_RUBRIC.md b/specs/SPEC_RUBRIC.md
index 290102b..f03a4d6 100644
--- a/specs/SPEC_RUBRIC.md
+++ b/specs/SPEC_RUBRIC.md
@@ -330,6 +330,17 @@ subagent callers); and GitHub reports the remote's `main` branch as not
 protected, with no rulesets. So "never touches main" is held by the park
 procedure, not by any enforced mechanism (observed in that report).
 
+Filer's note, not a ruling (2026-11-10, under C2 and A11): the master's live
+trip is recorded in DECISION_LOG 2026-11-10T06:12:00Z: on a local
+`parked/Praxis_build-c2trip` branch a commit with no audit run was allowed
+(git printed `[parked/Praxis_build-c2trip a27250f] … 1 file changed`; the
+branch was then deleted, and `git ls-remote --heads origin | grep -c c2trip`
+printed 0), and on `main` a commit with no audit run was denied ("Commit
+denied: no audit PASS token for this exact staged diff …"); that the
+exemption arm, not another allow, admitted the first is inferred by
+elimination from the second, because the gate's exemption stderr line is
+not shown on exit 0.
+
 Filer's note, not a ruling: this ruling lands under Amear's C8, "The July SPEC_RUBRIC R-A/R-B/R-C hunk lands as written." (D-2026-11-08-C; DECISION_LOG 2026-11-08T19:12:30Z, WHO: amear; docs/reports/2026-11-08-amear-answers-park-card.md :38).
 
 **No-verdict returns — R-A / R-B / R-C, ruled 2026-07-27. Source: DECISION_LOG
$ wc -l specs/SPEC_RUBRIC.md
     458 specs/SPEC_RUBRIC.md
$ cmp HEAD:1-332 WT:1-332 ; cmp HEAD:333-end WT:344-end
1-332 equal
HEAD 333-end == WT 344-end (+11)
$ grep -n (working tree)
356:**Absolutes are amended between sessions only — 2026-07-26 human ruling.**
346:**No-verdict returns — R-A / R-B / R-C, ruled 2026-07-27. Source: DECISION_LOG
358:A rule declared absolute is **never amended inside the session that hits it.**
```
The older sentence "Live trip by the master pending." (in the 2026-11-09/10 filer's note above) is left unedited, as the brief requires; the new paragraph records that the trip is now on file.

## Adversarial findings

ADV1 (a94724bbc96e42cbb, ADVERSARIAL, given the artifacts and criteria only). Its returned message, quoted:
- "Break (B, S1): `DECISIONS.md:2010` says the line-for-line match has its "evidence in `docs/reports/2026-11-10-housekeeping-2a-manager.md`". That file is an untracked 636-byte skeleton ..." — CLOSED: this report now carries that evidence (V-B1 to V-B5).
- "Minor: `DECISIONS.md:2022` says the rubric insert is a "ten-line filer's paragraph … after `:331`". It is 9 text lines plus 1 blank line, at 333–342, after the blank line 332." — FIXED, and re-checked after the item C rewrap (now 10 text lines + 1 blank at :333–343; note says eleven lines after `:332`, shift +11; V-C2).
- "Minor: `:2024` calls row 308's "now 413" "wrong". It was true before Correction 1 ... "Stale" is more precise." — FIXED: the note now says "does not match the committed file" and gives the 413-before-Correction-1 count. The brief's word was "wrong"; the softer wording is more exact, and the 416 fact the brief asked for is unchanged.
- "Minor, inherited: the rubric paragraph's "never pushed" copies the 06:12:00Z row. That row's only evidence is `ls-remote … | grep -c c2trip` = 0" — FIXED: the sentence now gives the observation, not the conclusion.
- Held (its words): A: "`cmp` was silent ... one hunk ... Line 2020 matches the given sha256 at 1326 bytes and its stamp appears once ... Lines 2020–2345 have no duplicates. Lines 2021+ have 12 time inversions; each follows a hand-written praxis-master row, and HEAD has 13 of the same kind, so nothing looks displaced." B (1)–(5): "the note covers every one"; "All 27 old→new line pairs match by text, the full ranges are equal, and the July hunk equals line 335–344 at 18d94a5"; "345, 447 and 416"; "says it is a filer's note, not a ruling"; "+10 shift holds" (since changed to +11 by the item C fix; re-checked by the manager in V-C2). C: "Every factual phrase matches DECISION_LOG.md line 783"; "under C2 and A11" has the same form as the note at :302–303.
- Not re-adversaried after the fixes (one-adversary budget). The fixed text was re-checked by the manager only (V-C2, V-B5, block F).

## S6 cross-block check

- F1–F4 (rubric :19, :32, :47, :61) are not touched; the rubric diff is one 11-line insert at :333–343 (V-C2).
- DISPATCH_LOG hooks: the move rewrote only the first 2020 lines with the same byte length, with no truncation; hook appends during the unit survived (V-A3: rows 2345, 2346).
- The DECISIONS.md cites above `:333` keep their HEAD targets after item C lands; those at `:333` or below move by +11, as the note states.
- Not touched: hooks, settings, scripts, walk-forward spec/values, U7 / Praxis_build-diq files, `.claude/agent-memory/`, the real index.

## Files staged

None. Nothing staged by this unit; the real index is unchanged (block F). Working-tree changes by this unit: DISPATCH_LOG.md (row moved), DECISIONS.md (append), specs/SPEC_RUBRIC.md (one paragraph), MANIFEST.md (one row at the end), this report (new, untracked). MANIFEST's earlier hunk `@@ -306,0 +307,8 @@` was there before this unit.

Result: PASS

## F. Final evidence (pasted last, after every edit)
```
$ git diff HEAD -U0 -- DISPATCH_LOG.md | grep '^@@'
@@ -2019,0 +2020,327 @@ Append-only. Every Agent dispatch + outcome. Row schema:
$ git diff HEAD -U0 -- DECISIONS.md | grep '^@@'
@@ -2007,0 +2008,17 @@ Nothing else.
$ git diff HEAD -U0 -- specs/SPEC_RUBRIC.md | grep '^@@'
@@ -332,0 +333,11 @@ procedure, not by any enforced mechanism (observed in that report).
$ git diff HEAD -U0 -- MANIFEST.md | grep '^@@'
@@ -306,0 +307,8 @@
@@ -331,0 +340 @@
$ tail -1 MANIFEST.md
| /docs/reports/2026-11-10-housekeeping-2a-manager.md | Report | 2 | 2026-11-10 | Manager report for unit 2026-11-10-housekeeping-2a (master under D-2026-11-08-D D1): DISPATCH_LOG row 2026-11-07T22:17:00Z moved byte-for-byte so HEAD is a byte prefix (bead Praxis_build-trn); DECISIONS.md pointer note for stale rubric cites in D-2026-11-08-C/-D plus MANIFEST row 308 line-count correction (bead Praxis_build-75n); rubric C2 filer's sentence citing the live trip row DECISION_LOG 2026-11-10T06:12:00Z |
$ git diff --cached --name-status
A	docs/reports/evidence/2026-10-28-mffu-davi-reply.png
$ bash -c 'cmp <(git show HEAD:DISPATCH_LOG.md) <(head -n 2019 DISPATCH_LOG.md); echo cmp exit $?'
cmp exit 0
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-11-10T07:30:17Z
$ grep -c '^Result:' docs/reports/2026-11-10-housekeeping-2a-manager.md
1
$ grep -c -F "$S13" docs/reports/2026-11-10-housekeeping-2a-manager.md   # $S13 = the full standing limitation sentence
1
$ wc -l docs/reports/2026-11-10-housekeeping-2a-manager.md
     281 docs/reports/2026-11-10-housekeeping-2a-manager.md
```

The `wc -l` above was taken before this block was appended; with this block the report is 308 lines.
