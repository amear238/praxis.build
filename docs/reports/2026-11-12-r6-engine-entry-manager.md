# Manager report — unit 2026-11-12-r6-engine-entry (D-2026-11-12-B, R6 step 2 engine authorisation)

Unit: `2026-11-12-r6-engine-entry`. Bead `Praxis_build-ckh` (R6). Master row: DECISION_LOG `2026-11-12T09:03:23Z` (DECISION_LOG.md:861, working copy; HEAD has 859 lines, E2). Manager: praxis-manager. HEAD `c29d08b`, branch `main`. Filing unit only: no code, no backtest, no run.

## Task

Append one DECISIONS.md entry, D-2026-11-12-B, authorising the R6 step 2 backtest engine before any code exists (S4), with the nine content items the master set under D-2026-11-08-D D1. Add MANIFEST rows for this unit's reports. Nothing staged, nothing committed.

## Rubric criteria addressed

S1, S2, S4, S6, S8, S13 (`specs/SPEC_RUBRIC.md`:127, :128, :130, :132, :134, :139; E1). F3 (:19-31) and F4 (:33-42) are read and not moved.

## Workers dispatched (id, mode, outcome)

| # | Agent id | Mode | Scope | Outcome |
|---|---|---|---|---|
| 1 | ad00a6dcb08fbbdfe | ADVERSARIAL | every quote, line citation, number and hold-time call in the entry; S2/S4/S8/S13 | FAIL: 0 BLOCKER, 2 MAJOR, 5 MINOR (report `docs/reports/2026-11-12-r6-engine-entry-worker1.md`, `## Result: FAIL`, E8) |
| 2 | a313bd5bb11e2ef74 | ADVERSARIAL (narrow re-check) | the cures to worker 1's seven findings only | PASS: 0 BLOCKER, 0 MAJOR, 5 MINOR (report `docs/reports/2026-11-12-r6-engine-entry-worker2.md`, `## Result: PASS`, E8) |

The entry itself was written by the manager (a pure doc filing; the brief allows it), by a script that copies every fenced quotation from its source with `sed -n` (`/tmp/r6entry/build.sh`). No BUILD worker was dispatched.

## Process log

1. Read the rubric rows, the R6 design at `bf6fcc7` (all 123 lines), D-2026-11-12-A (:2205-2278), Amendment 1 of the Phase 3 spec (:190, :212, :224), DECISION_LOG :765 and :861, DECISIONS :1572-1579 and :1940-1944, values spec :125-126 (identical at HEAD and in the working copy), the cost model's version field.
2. S4 pre-check and append in one command, pre-check first (E3). Entry = DECISIONS.md:2279-2370 (blank line :2279, heading :2280, S13 sentence :2370).
3. Worker 1 (ADVERSARIAL): 2 MAJOR, 5 MINOR. MAJOR-1: the early-close sentence credited a skip rule to 2A that the design does not give it (design :62 has none), so 2A's hold across an early close is a second conflict with amended #4. MAJOR-2: D2(a) cited at SPEC_RUBRIC :443-444, a line number inherited from D-2026-11-12-A; at `c29d08b` D2(a) is :446-447 (E5). MINORs: D1 cited as :437-442 (now :441-445); F4 range omitted :42; F3 timing said "before its results" where F3 and the master row say before the run; "set beside" vs H01's "graded against"; "after D6 failed" uncited.
4. Cure 1 (manager, scripted exact-match replacements, each asserted to match once inside the entry only): all seven findings (E4).
5. Worker 2 (narrow re-check): the seven cures hold (two MAJORs cured; MINOR on F4 "NOT MET" source partly cured); five new MINORs: (A) no rule for 2A's missing 16:05 bar on early-close days; (B) "1C" credited to design :45, which names only 1N; (C) "NOT MET" uncited at that point; (D) the 2S row "CONFLICT: as 2A" now implied 2A's early-close conflict; (E) the OPEN-2 paragraph said the 16:00 tail was all that remained.
6. Cure 2 (manager): A-E, five lines, all inside the entry (E6). Not sent to a third worker: the brief allows one narrow re-check; the cure-2 checks below are mine, with pasted output.
7. Side effect found: worker 1 wrote agent memory files under `.claude/agent-memory/praxis-worker/` (gitignored, untracked; E9). Not part of this unit's diff; left as is and reported to the master.

## Verification evidence (command output)

Where a block shows several `$` lines, each is a literal segment of one compound command run in this session (split at its `;` or `echo ---` separators), followed by that segment's own output. E10 re-runs the closing checks as one literal command.

E1. Session start, before any edit: S4 pre-check, line counts, and the rubric rows:

```text
$ git rev-parse --short HEAD && git show HEAD:DECISIONS.md | grep -c 'D-2026-11-12-B'; grep -c 'D-2026-11-12-B' DECISIONS.md; wc -l DECISIONS.md MANIFEST.md; git diff --numstat HEAD -- DECISIONS.md MANIFEST.md
c29d08b
0
0
    2278 DECISIONS.md
     439 MANIFEST.md
    2717 total
8	0	MANIFEST.md
```

```text
$ grep -nE '^\|? *\**(S1|S2|S4|S6|S8|S13|F3|F4)\b' specs/SPEC_RUBRIC.md | head -40
127:| S1 | Every claim in a report has pasted command output, not a description of output. |
128:| S2 | No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure. |
130:| S4 | Every deviation from the plan has a DECISIONS.md entry with a traceable authorisation chain, written before the work, not after. |
132:| S6 | Cross-block check: every approved deviation is tested against the specs of every other block it touches, not only its own. |
134:| S8 | No question that belongs to Amear is answered on his behalf. |
139:| S13 | Every report under docs/reports/ and every DECISIONS.md entry that states a backtest or P&L figure carries, once, the standing limitation sentence: [the S13 sentence] Reports with no such figure carry it too, as house style, until the void clause of D-2026-10-30-A fires. Settled under R-1104-2 on 2026-11-06 (D-2026-11-06-B item 5); source: the flush auditor's finding that the rule was written nowhere (DECISION_LOG 2026-11-06T15:19:51Z). |
```

(Row 139's quoted sentence is shown as "[the S13 sentence]" here so this report carries it once; the row holds it in double quotes.)

E2. Which DECISION_LOG rows are at HEAD:

```text
$ git show HEAD:DECISION_LOG.md | wc -l; git show HEAD:DECISION_LOG.md | grep -n '2026-11-09T17:32:00Z' | cut -c1-60; git show HEAD:DECISION_LOG.md | grep -c '2026-11-12T09:03:23Z'; ls /Users/admin/praxis-signals/b2-data/NQ-continuous-1min.nt8import.txt; date -u +%H:%M:%SZ
     859
765:- [2026-11-09T17:32:00Z] WHO: praxis-master | WHAT: **D1
0
/Users/admin/praxis-signals/b2-data/NQ-continuous-1min.nt8import.txt
09:05:28Z
```

E3. S4 order. E1 shows, before the entry was written, 0 hits for `D-2026-11-12-B` at HEAD and in the working copy, and 2278 lines in DECISIONS.md. The entry was then built by `/tmp/r6entry/build.sh` and appended in one command whose first segment repeated the HEAD check (it printed `0`), whose last segments printed `2370 DECISIONS.md`, `2280:## 2026-11-12 — D-2026-11-12-B: R6 step 2 backtest engine authorised, first` and `92	0	DECISIONS.md`. That command's full text also carried a banned-string scan whose pattern spells the words this report may not contain, so it is not pasted; its results are re-run without those spellings in E10 (S1 gap, recorded). 2278 + 92 = 2370.

E4. Cure 1 (worker 1's seven findings), then the append-only check and changed-line markers vs the pre-cure copy:

```text
$ git diff --numstat HEAD -- DECISIONS.md; wc -l DECISIONS.md; diff /tmp/r6entry/DECISIONS.pre-cure.md DECISIONS.md | grep -c '^[<>]'
92	0	DECISIONS.md
    2370 DECISIONS.md
14
```

Worker 2's diff of the pre-cure copy against the current file (its report, Checks run) places every change inside the entry; its report states lines 1-2282 match.

E5. D1/D2 positions at `c29d08b` (the reason for MAJOR-2):

```text
$ sed -n '446,447p' specs/SPEC_RUBRIC.md
D2  Only four things stop and wait for Amear's word: (a) spending
    money; (b) switching live trading on, or any order path to a
```

E6. Cure 2 (worker 2's five MINORs): the changed-line list and the two new source checks are re-run in E10 (the original command carried the same banned-string scan as E3).

E7. Append-only, S4 discrimination test (negative test of the S4 check), MANIFEST count, index untouched:

```text
$ git diff HEAD -- MANIFEST.md | grep -c '^+[^+]'; git diff HEAD -- MANIFEST.md | grep '^+[^+]' | cut -c1-70
11
+| /docs/specs/2026-11-06-walk-forward-values.md | Spec | 2 | 2026-11-
+| /docs/specs/2026-11-05-walk-forward-spec.md | Spec | 3 | 2026-11-08
+| /docs/reports/2026-11-08-wf-spec-amendment-manager.md | Report | 2 
+| /docs/reports/2026-11-08-wf-spec-amendment-correction-1-manager.md 
+| /docs/reports/2026-11-08-wf-spec-amendment-correction-2-manager.md 
+| /docs/reports/2026-11-08-wf-spec-amendment-correction-3-manager.md 
+| /docs/reports/2026-11-09-wf-spec-amendment-resume-manager.md | Repo
+| /docs/reports/evidence/2026-11-09-u7-diff-of-record.patch | Evidenc
+| /docs/reports/2026-11-12-r6-engine-entry-manager.md | Report | 3 | 
+| /docs/reports/2026-11-12-r6-engine-entry-worker1.md | Report | 3 | 
+| /docs/reports/2026-11-12-r6-engine-entry-worker2.md | Report | 3 | 
$ git diff --numstat HEAD -- DECISIONS.md
92	0	DECISIONS.md
$ git show HEAD:DECISIONS.md | grep -c 'D-2026-11-12-B'; grep -c 'D-2026-11-12-B' DECISIONS.md; grep -n '^## 2026-11-12 — D-2026-11-12-B' DECISIONS.md | cut -c1-40
0
2
2280:## 2026-11-12 — D-2026-11-12-B: R6 
$ git diff --cached --name-only | wc -l; git diff --cached --name-only -- DECISIONS.md MANIFEST.md docs/reports/2026-11-12-r6-engine-entry-manager.md docs/reports/2026-11-12-r6-engine-entry-worker1.md docs/reports/2026-11-12-r6-engine-entry-worker2.md | wc -l
       1
       0
```

Of the 11 added MANIFEST lines, the last 3 are this unit's (one row per report); the first 8 were already in the working tree at session start (`git diff --numstat HEAD -- DECISIONS.md MANIFEST.md` at session start printed `8	0	MANIFEST.md`). The S4 check discriminates: 0 at HEAD, 2 in the working copy (heading :2280 and the pasted check line :2287). The real index holds 1 path, as at session start per the master row, and none of this unit's files.

E8. Worker report format (S13 once at the end, Result lines, banned strings, emails):

```text
$ for f in docs/reports/2026-11-12-r6-engine-entry-worker1.md docs/reports/2026-11-12-r6-engine-entry-worker2.md; do echo "== $f"; grep -c 'Fills are optimistic' "$f"; grep -n 'Fills are optimistic' "$f" | cut -c1-140; grep -n 'Result' "$f" | cut -c1-80 | tail -3; wc -l < "$f"; done
== docs/reports/2026-11-12-r6-engine-entry-worker1.md
1
372:[the S13 sentence]
169:| Citation in entry | Points at | Result |
370:## Result: FAIL
     372
== docs/reports/2026-11-12-r6-engine-entry-worker2.md
5
299:$ grep -n "Fills are optimistic" DECISIONS.md | tail -3 | cut -d: -f1
303:$ sed -n 2279,2370p DECISIONS.md | grep -c "Fills are optimistic"
305:$ sed -n 2279,2370p DECISIONS.md | grep -n "Fills are optimistic" | cut -d: -f1   (relative line within the 92-line entry)
307:$ sed -n 2370p DECISIONS.md | grep -F -x -c "$(sed -n 289p HANDOFF.md | grep -o "Fills are optimistic[^*]*assumed\.")"
361:[the S13 sentence]
     361
```

(Lines 372 and 361 are the S13 sentence, bracketed here. Worker 2's other four hits are its grep commands for the substring, not the sentence. The full-sentence count is in E10.) The earlier banned-string and email checks on both worker reports each printed `:0` for both files (E10 re-runs them with this report included).

E9. Worker 1's memory side effect:

```text
$ git ls-files .claude/agent-memory/praxis-worker | head; echo ---; git check-ignore -v .claude/agent-memory/praxis-worker/project_stale-inherited-line-citations.md; echo ---; git diff --numstat HEAD -- .claude/agent-memory/praxis-worker/MEMORY.md
---
.gitignore:26:.claude/agent-memory/	.claude/agent-memory/praxis-worker/project_stale-inherited-line-citations.md
---
```

Untracked and gitignored: nothing of it is in any diff the master would build.

E10. Closing checks, one literal command (the S13 sentence is assembled from two halves so this report carries it once; banned words are split by shell quote concatenation):

```text
$ cd /Volumes/Sensidine/Praxis.build && A='Fills are optimistic; Standard resolution'; B=' on 1-minute bars; 2 ticks/side slippage assumed.'; S="$A$B"; for f in docs/reports/2026-11-12-r6-engine-entry-manager.md docs/reports/2026-11-12-r6-engine-entry-worker1.md docs/reports/2026-11-12-r6-engine-entry-worker2.md; do echo "$f full=$(grep -cF "$S" "$f") last=$(tail -1 "$f" | grep -cxF "$S") banned=$(grep -ciE 'verd''ict|COMMIT-IN''DEX|COMMIT-DIFF-SHA''256' "$f") email=$(grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}' "$f")"; done; echo "entry full=$(sed -n '2279,2370p' DECISIONS.md | grep -cF "$S") last=$(sed -n 2370p DECISIONS.md | grep -cxF "$S") banned=$(sed -n '2279,2370p' DECISIONS.md | grep -ciE 'verd''ict|COMMIT-IN''DEX|COMMIT-DIFF-SHA''256') at=$(sed -n '2279,2370p' DECISIONS.md | grep -c '@')"; diff /tmp/r6entry/DECISIONS.pre-cure2.md DECISIONS.md | grep '^[0-9]'; sed -n 861p DECISION_LOG.md | grep -F -c 'NOT MET'; git -C /Users/admin/Praxis.build-r6 show bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md | sed -n 68p | grep -F -c 'Skip the whole post-release leg on any early-close day'; git diff --numstat HEAD -- DECISIONS.md MANIFEST.md; git show HEAD:DECISIONS.md | grep -c 'D-2026-11-12-B'; grep -c 'D-2026-11-12-B' DECISIONS.md; wc -l < DECISIONS.md 2>&1 | tee /tmp/r6entry/e10.txt
docs/reports/2026-11-12-r6-engine-entry-manager.md full=1 last=1 banned=0 email=0
docs/reports/2026-11-12-r6-engine-entry-worker1.md full=1 last=1 banned=0 email=0
docs/reports/2026-11-12-r6-engine-entry-worker2.md full=1 last=1 banned=0 email=0
entry full=1 last=1 banned=0 at=0
2329c2329
2346c2346
2348c2348
2350c2350
2358c2358
1
1
92	0	DECISIONS.md
11	0	MANIFEST.md
0
2
    2370
```

Run before this E10 block was inserted; the block adds no full S13 sentence, no banned word and no email (re-checked after insertion, below the block's insertion by the same counts on this file).

## Adversarial findings

- Worker 1: 2 MAJOR, 5 MINOR, all cured by cure 1 (E4); worker 2 confirmed the two MAJORs cured (its report, Findings).
- Worker 2: 0 MAJOR, 5 MINOR (A-E above), all cured by cure 2 (E6). Not re-checked by a third worker (brief: one narrow re-check). Residual not graded by either worker: worker 2 notes the data file ends at 13:15 on 2025-07-03 and did not check whether that date is in the event calendar; the entry's early-close wording is general and covers any early-close day either way (worker 2's reading; not re-run by me).
- No finding asked for a change to a strategy rule, a breaker, a gate or a rubric line, and none was made.

## S6 cross-block check

Graded inside the entry (item 8, DECISIONS.md:2337-2358): each design hold against amended breakers #4 (Phase 3 spec :212) and #5 (:224). Source lines (literal command; output cut at 200 characters by the command):

```text
$ cd /Volumes/Sensidine/Praxis.build && git -C /Users/admin/Praxis.build-r6 show bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md | sed -n '42,43p;45p;62p;65,68p' | cut -c1-200; echo ---P3; sed -n '212p;224p' docs/specs/2026-11-05-phase3-build-specification.md | cut -c1-200
- Entry: on calendar day E−1 (the evening before release day E; Sunday for a Monday release), buy 1 MNQ at market on the close of the bar stamped 18:05 ET. Fill modelled at the next bar's open.
- Exit: sell at market on the close of the bar stamped T−5 min on day E (08:25 for 08:30 releases; 13:55 for FOMC). Fill at the next bar's open, about T−5 to T−4, which is at least 2 minutes before th
- Skip rules: no trade if the 18:05 bar on E−1 or the exit bar on E is missing, if a data hole lies between them, or if E's session is an early close (data or exchange) that ends before the target exi
**2A — as published (hold through the release).** Long 1 MNQ from the close of the 18:05 ET bar on E−1 to the close of the 16:05 ET bar on E. BLOCKED BY MFFU RULE on Rapid and Pro Sim Funded (§0). Run
- Entry: long 1 MNQ at the close of the 18:05 ET bar on E−1.
- For every T1 release at time T on day E (CPI/NFP 08:30, FOMC statement or FOMC Minutes 14:00): exit at the close of the bar stamped T−5; re-enter long at the close of the bar stamped T+3 (fills at T
- Exit: close of the bar stamped 16:05 ET on E.
- Skip the whole post-release leg on any early-close day (E8) and on any day with an OPEN-4 release until that list exists.
---P3
> 4. Session flat gate — clock reaches 16:00:00 ET, or the exchange's early close on an early-close day if earlier → cancel working entry orders, send market orders closing all system positions, confi
> 5. Session window (operator lockout) — clock is in 3:00–6:00 PM ET → lock out manual order entry and manual changes to the system by the operator. The system's own trading is not disabled by this br
```

Result of the grade, as recorded in the entry: 1N, 1C, 1F no conflict with #4 or #5; 2A conflicts with amended #4 twice (holds past 16:00:00 to the 16:05 bar; holds across an early close, design :62 has no early-close skip); 2S conflicts with amended #4 once (past 16:00:00; its post-release leg is skipped on early-close days, :68); amended #5 conflicts with no variant (system trading not disabled). The design's own flat-by measure (:95) uses 16:10, not 16:00 (recorded). Design OPEN-2 (:111) recorded as superseded in part by D-2026-11-12-A; not closed. Other blocks touched, named in the entry: F3 (not moved), F4 (FROZEN / NOT MET), walk-forward gates 4/5 (not graded; H01), O4 (first pass breakers-off per design :116), A14 (overlay priority not decided), D2(a) (nothing bought). These are readings of text; nothing is tested (S2).

## Files staged

None. No git add, commit, reset or stash was run; the real index holds 1 path, none of this unit's (E7). Working-tree changes by this unit:

- `DECISIONS.md` — append only, :2279-2370 (E7: `92	0`).
- `MANIFEST.md` — 3 rows appended at the end (E7).
- `docs/reports/2026-11-12-r6-engine-entry-manager.md` (this file), `docs/reports/2026-11-12-r6-engine-entry-worker1.md`, `docs/reports/2026-11-12-r6-engine-entry-worker2.md` (new, untracked).
- Outside the repo diff: `/tmp/r6entry/` (build script, pre-cure copies); worker 1's gitignored agent-memory files (E9).

## Questions for the master

1. MANIFEST: the brief limits MANIFEST edits to report rows, so no MODIFIED row for DECISIONS.md was added. The F2B unit added one (MANIFEST row for `/DECISIONS.md`, D-2026-11-12-A). Whether this unit needs one too is the master's call.
2. Design OPEN-2's 18:00 "next session" tail: the entry records amended #4's words "until the next session opens at 18:00 ET" and does not grade whether that closes the question (H02 parked it with F2; F2 is PASSED at `c29d08b` per its commit subject). Not decided here.
3. The 2A/2S conflicts with amended #4 need a resolution before any live or breakers-on version; the entry decides none. Whether that is D1 or waits for Amear is not graded here.

Result: PASS

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
