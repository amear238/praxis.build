# Manager report — unit `2026-11-07-rulings-filing` (praxis-manager, 2026-11-07)

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## Task
File Amear's ten morning rulings (`docs/reports/2026-11-07-amear-rulings-morning.md`:9–31) into DECISIONS.md as D-2026-11-04-B addendum 6 (ratification of addendum 5's timing) and D-2026-11-07-A (the ten rulings, verbatim, plus a per-ruling record and the master's Q3 settlement under R-1104-2). Fix MANIFEST. Append ruling 10's first go-live item to the Fusion walkthrough. Run a de-identification probe over every file the commit will carry. Stage nothing. Authorisation (S5): DECISION_LOG `2026-11-07T12:55:00Z` (**WHO: amear**) and dispatch row `2026-11-07T13:00:54Z` (WHO: praxis-master). Both rows are in the working tree and not yet in a commit.

## Rubric criteria addressed
S1, S2, S4, S5, S6, S8, S13 (`specs/SPEC_RUBRIC.md`, quoted verbatim in the brief). No criterion was authored by this unit.

## Workers dispatched (id, mode, outcome)
| # | id | mode | outcome |
|---|---|---|---|
| W1 | a7debd004d4fb9ac4 | BUILD: DECISIONS.md insert and MANIFEST.md append | Returned PASS. 98 lines at 1192–1289 and 6 rows at 259–264. Its report-file Write was refused, so its findings came back as text. |
| W2 | a86ae364fa7037562 | BUILD: walkthrough line, plus an independent probe re-run | Returned PASS. Walkthrough line 38 appended. It found that my v1 probe's liveness arm was tautological (fixed in v2, below). |
| W3 | adcc29c9e58c02f6d | ADVERSARIAL on the entries, MANIFEST rows and walkthrough line | `VERDICT: NOT REFUTED`, with 8 MINOR findings. All 8 were fixed by the manager. |
| W4 | ae79d0bef0a1cbfd1 | ADVERSARIAL on the post-W3 fixed text | `VERDICT: REFUTED`: 2 MAJOR, 5 MINOR. All 7 were fixed by the manager. **The post-W4 text has not had a fresh adversarial pass** (see Result). |

The adversaries were given the artifact, the sources and the criteria. They were not given any worker's reasoning.

## Process log
1. 13:04:25Z: read the dispatch row, the rulings file, the rubric, the DECISIONS form models (1052–1117, 1165–1190), MANIFEST 244–258, the walkthrough and VM handoff §8. Took baseline hashes.
2. De-identification probe, STOP condition first. The category-word probe was 0 on the notes file. Its positive arm, however, read 0 at a known title location (HEAD:DECISION_LOG.md:47). So that probe cannot see the breaker #5 source title itself. I built a superset token probe instead, which prints counts and line numbers only (described in Verification evidence). It got one hit in the notes file at :47. The token is common: it appears in 36 tracked files. The two tokens confined to the two known locations hit nothing. **Not a STOP.**
3. Dispatched W1 and W2 in parallel on disjoint files.
4. Re-ran the workers' checks myself and read the inserted text in full. I fixed one stale claim myself, in one line (ruling 10: "REPORTED BY the dispatch row" became the line actually observed at :38).
5. Dispatched W3 (adversary) → NOT REFUTED, 8 MINOR. Applied 9 exact-match replacements with asserts (8 in DECISIONS.md, 1 in MANIFEST row 259).
6. Dispatched W4 (fresh adversary on the fixed lines) → REFUTED, 2 MAJOR. Applied 6 exact-match replacements in DECISIONS.md (the Status-line change covers 2 lines) and 1 on walkthrough line 38. Checked every newly introduced quote by script against its source.
7. During the unit, DISPATCH_LOG.md gained hook-written spawn and close rows for W1–W4 (`scripts/dispatch-log-writeahead.sh`, SubagentStart/Stop). Neither I nor any worker edited it (pasted below).
8. Deviations from the brief, all disclosed:
   - The brief's addendum-5 line numbers are one off. OBSERVED: heading :1165, Timing :1167, ratification request :1169.
   - MANIFEST gained rows (v) `/DECISIONS.md` and (vi) the walkthrough, beyond the brief's four. Reason: the CLAUDE.md rule "Update MANIFEST.md when creating or modifying files", and house practice (row 248).
   - The walkthrough line sits at :38 (see W4 finding 2 and its resolution).

## Verification evidence
All blocks below are pasted command output from this session.

**Placement and invariants (final state):**
~~~
$ grep -n "^## " DECISIONS.md | tail -5
1131:## 2026-08-06 — D-2026-08-06-A: Phase 3 build specification imported DE-IDENTIFIED (medication reference only)
1165:## 2026-11-06 — D-2026-11-04-B addendum 5: third hand-back shape (task-notification) — WRITTEN AFTER THE WORK; S4 timing NOT met; ratification requested (WHO: amear)
1192:## 2026-11-07 — D-2026-11-04-B addendum 6: ratification (WHO: amear) of addendum 5's timing
1203:## 2026-11-07 — D-2026-11-07-A: Amear's ten morning rulings (typed, 2026-11-07) — filed WHO: amear
1290:## 2026-11-06 — D-2026-11-06-D: walk-forward values proposed under ruling 4 and arm (b) code design (PROPOSAL — awaiting Amear's confirmation)
$ sed -n '/^## 2026-11-06 — D-2026-11-06-D/,$p' DECISIONS.md | shasum -a 256
9a83e55d1e56942f80273d9b52721ea6852cf7e5b58cac67d12b876395693683  -
$ sed -n 1,1190p DECISIONS.md | shasum -a 256
0ba9af57078bd0ce6b41589e5781c427c73bafa4749fcb6a79804989b008339f  -
$ git diff HEAD -- DECISIONS.md MANIFEST.md <walkthrough> | grep -c '^-[^-]'
0
$ git diff -U0 HEAD -- DECISIONS.md | grep '^@@'
@@ -1163,0 +1164,167 @@ Master's readings, flagged as readings: (i) "Handoff NEEDS AMEAR 1, 3–10, 15
~~~
Two independent checks on the invariants:
- The D-2026-11-06-D block hash equals W1's before-edit value (`9a83e55d…`, REPORTED BY W1).
- W3 found the same block hash in the earlier `commit-idx-wfv` temp index, and the same lines 1–1190 hash (`0ba9af57…8339f`) in `commit-idx-add5` (REPORTED BY W3).

**Copy check (paste = rulings 9–31), with a negative test:**
~~~
$ sed -n 9,31p docs/reports/2026-11-07-amear-rulings-morning.md | shasum -a 256
b6b954347cc2e35a3b2f2ad63d1e49c084a5ceeb236a913384ec3668635656d7  -
$ grep -n '^```' DECISIONS.md | awk -F: '$1>1191'
1213:```text
1237:```
$ sed -n 1214,1236p DECISIONS.md | shasum -a 256
b6b954347cc2e35a3b2f2ad63d1e49c084a5ceeb236a913384ec3668635656d7  -
NEGATIVE TEST (copy check must catch a 1-byte change):
$ sed -n 1214,1236p DECISIONS.md | sed '3s/RATIFIED/RATIFIEd/' | shasum -a 256
1e3d7158d283d52a29629b27284a98ef251d48dfe5c23376d421625a613154a8  -
~~~

**10-28 notes file is unedited (sha256 at unit start 13:04:25Z, and final):**
~~~
7999c03410ffd0e83253100ea76714b80f0f211a1e363470965231edaeb6cb48  docs/reports/2026-10-28-voice-session-notes.md
7999c03410ffd0e83253100ea76714b80f0f211a1e363470965231edaeb6cb48  docs/reports/2026-10-28-voice-session-notes.md
~~~
The rulings file (`975f9c48…1c78`) and the addendum-5 report (`f09fed9e…5256`) are also unchanged from unit start to final.

**Walkthrough: one line appended, nothing above edited:**
~~~
$ git diff --numstat HEAD -- docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md
1	0	docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md
$ head -37 <walkthrough> | shasum -a 256      (whole-file sha at unit start was the same value)
3ec11d03d7c13afb04be7c372605ed32be2d4b576416cbc84fc4fa10a6a19063  -
$ tail -1 <walkthrough>
- [ ] **Go-live checklist addendum 2026-11-07, his words (ruling 10):** "remove the unauthenticated bridge request folders (or add auth) before real money" (verbatim at `docs/reports/2026-11-07-amear-rulings-morning.md`:29; ledger DECISION_LOG 2026-11-07T12:55:00Z, WHO: amear; D-2026-11-07-A). His second item, "unmap Z: and turn off the SMB share", is already covered at :35; not duplicated.
~~~
Verified after the final fix: the sha256 of the pasted tail line above equals the sha256 of `tail -1` of the walkthrough (`ce2855ff7c8092b0205d4a7536ccc4a8a33e3b60bc04929e4b1547128494248b` both).

**MANIFEST:**
~~~
$ git diff --numstat HEAD -- MANIFEST.md
8	0	MANIFEST.md
$ sed -n 254,255p MANIFEST.md | shasum -a 256       (W1 before-edit value: same)
00b7e89357980786c291024464e09368cb291b928ff99eba5d64925d011beea2  -
$ wc -l MANIFEST.md
     264 MANIFEST.md
~~~
Rows 259–264 hold, in order:
1. (i) the notes-file UPDATE ROW superseding row 244: "to be carried in the next gated commit as a one-file exception (untracked at time of row)", sha256 `7999c034…cb48` before and after.
2. (ii) the rulings file.
3. (iii) the addendum-5 manager report.
4. (iv) this report.
5. (v) `/DECISIONS.md` (addendum 5 :1165–1190, addendum 6 :1192–1201, D-2026-11-07-A :1203–1288; D-2026-11-06-D not included).
6. (vi) the walkthrough UPDATE ROW.

**S13 count per entry:**
~~~
S13 1192,1201 = 1
S13 1203,1288 = 1
~~~

**De-identification probe.** Superset token probe v2: `scratchpad/tokprobe2.sh`.
- **Candidate set:** alpha tokens of length ≥ 4 on HEAD:DECISION_LOG.md:47, which is one known location per D-2026-08-06-A. From these it removes the tokens of HEAD:DECISIONS.md and HEAD:SPEC_RUBRIC.md, intersects with 7d9be8e:HANDOFF.md (the other introducing commit), and removes the tokens of `a42038e^`:DECISION_LOG.md.
- **Storage:** the candidates are held in a shell variable only.
- **Liveness:** the liveness arm runs the same per-file loop on the two known locations.
- **Output:** counts and line numbers only.
~~~
candidates=13
LIVENESS HEAD:DECISION_LOG.md tokens_hit=13 confined_tokens_hit=2 lines=47,77,89,143,259,464,500,501,535,640,47,83,89,95,97,107,111,153,335,345,365,367,450,473,653,47,153,317,496,47,47,47,161,47,47,119,47,47,61,47,47,47,
LIVENESS 7d9be8e:HANDOFF.md tokens_hit=13 confined_tokens_hit=2 lines=9,14,80,7,9,302,9,23,277,24,426,20,9,14,9,9,15,20,
DECISIONS.md[1192,1289] tokens_hit=0 confined_tokens_hit=0 lines=none
MANIFEST.md[259,264] tokens_hit=0 confined_tokens_hit=0 lines=none
docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md tokens_hit=0 confined_tokens_hit=0 lines=none
docs/reports/2026-10-28-voice-session-notes.md tokens_hit=1 confined_tokens_hit=0 lines=47,
docs/reports/2026-11-07-amear-rulings-morning.md tokens_hit=0 confined_tokens_hit=0 lines=none
docs/reports/2026-11-06-gate-addendum-5-manager.md tokens_hit=0 confined_tokens_hit=0 lines=none
~~~
The notes-file hit at :47, classified per candidate (counts only):
~~~
cand02 tracked_files_at_HEAD=36 notes_hit=1
cand12 tracked_files_at_HEAD=2 notes_hit=0
cand13 tracked_files_at_HEAD=2 notes_hit=0
~~~
The other 10 candidates are in 3–26 tracked files each, with notes_hit=0.
- The hit token's spread across 36 files makes it a common word. That classification is INFERRED from the spread.
- That the two confined tokens do not hit the notes file is OBSERVED.
- W2 re-ran the probe and got the same numbers (REPORTED BY W2).

Category and form-hint probe, after fixing a zsh word-splitting false zero in my first loop (that loop printed `sed: … No such file` and its zeros were void):
~~~
DECISIONS.md[1192,1289]: medication=0 drug=0 pill=0 dose=0 prescri=0 brand=0 letter=0 character=0 syllable=0 spell=0 begins with=0 starts with=0 long name=0 short name=0 abbreviat=0
MANIFEST.md[259,264]: medication=0 drug=0 pill=0 dose=0 prescri=0 brand=0 letter=0 character=0 syllable=0 spell=0 begins with=0 starts with=0 long name=0 short name=0 abbreviat=0
positive arm DECISIONS[1192,1289] ruling=26
docs/reports/2026-10-28-voice-session-notes.md: medication=0 drug=0 pill=0 dose=0 prescri=0 brand=0
docs/reports/2026-11-07-amear-rulings-morning.md: medication=0 drug=0 pill=0 dose=0 prescri=0 brand=0
docs/reports/2026-11-06-gate-addendum-5-manager.md: medication=0 drug=0 pill=0 dose=0 prescri=0 brand=0
docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md: medication=0 drug=0 pill=0 dose=0 prescri=0 brand=0
~~~
Probe limits (S2):
- **Short or non-alpha forms:** the probe misses tokens under 4 letters and forms that contain digits or hyphens.
- **Unconfirmed premise:** it assumes HEAD:DECISIONS.md and HEAD:SPEC_RUBRIC.md are clean. That is the rule's premise, not something verified here.
- **Temp-file exposure:** probe v1 wrote the candidate list to a temp file and then deleted it (W2 finding). v2 does not write it to disk.

This report is probed after it is written; the result is at the end of the report.

**Quote check on every string the fix rounds introduced:**
~~~
Fusion walkthrough `## Go-live (R-VN4-14)` section: append ruling 10's in DL677                  1
as a dated addendum line below the existing checklist                  in DL677                  1
every remaining PROPOSED value                                         in rulings9-31            1
flatten on the 15:59 bar                                               in rulings9-31            1
or STOP                                                                in rulings9-31            1
a hard STOP condition for the VM session                               in rulings35-44           1
Fix MANIFEST.md:244 to match                                           in rulings9-31            1
Append-only file creation registry                                     in MANIFEST:9             1
you propose them                                                       in rulings9-31            1
unmap Z: and turn the share off before real money                      in walkthrough:35         1
remove the unauthenticated bridge request folders (or add auth) before in rulings:29             1
breaker #4 closes positions at 11:30 ET                                in rubric:31              1
breaker #5 disables everything 15:00–18:00 ET                        in rubric:31-32           1
Deviation B flattens at 16:00 ET                                       in rubric:32-33           1
~~~
W3 checked every quote in the pre-fix text by script: 70+ strings, all present in their sources (REPORTED BY W3 and W4).

**Protected paths: no edits by this unit:**
~~~
$ git diff --numstat HEAD -- DECISION_LOG.md DISPATCH_LOG.md AUDIT_LOG.md STATUS.md HANDOFF.md ISSUE_REGISTER.md
4	0	AUDIT_LOG.md
6	0	DECISION_LOG.md
13	0	DISPATCH_LOG.md
4	0	HANDOFF.md
41	0	ISSUE_REGISTER.md
1	1	STATUS.md
$ TZ=UTC stat -f '%Sm %N' ...
2026-11-07T13:02:05Z DECISION_LOG.md
2026-11-07T13:24:19Z DISPATCH_LOG.md
2026-11-07T00:39:48Z AUDIT_LOG.md
2026-11-07T00:18:50Z STATUS.md
2026-11-07T00:18:50Z HANDOFF.md
2026-08-29T16:33:09Z ISSUE_REGISTER.md
2026-11-06T22:50:06Z vm/2026-11-06-vm-handoff.md
2026-11-06T23:50:21Z docs/specs/2026-11-06-walk-forward-values.md
2026-11-06T00:33:46Z .claude/settings.json
2026-07-28T16:46:11Z scripts/dispatch-log-writeahead.sh
2026-11-06T20:19:10Z specs/SPEC_RUBRIC.md
$ git diff HEAD -- DISPATCH_LOG.md | grep '^+' | tail -5   (hook rows for this unit's workers)
+- [2026-11-07T13:12:09Z] WHO: praxis-worker | WHAT: subagent closed | WHY: hook-recorded at SubagentStop, keyed close for corr=a7debd004d4fb9ac4, matched 1 open row(s) | ...
+- [2026-11-07T13:13:10Z] WHO: praxis-worker | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session 3ef528c corr=adcc29c9e58c02f6d | ...
+- [2026-11-07T13:19:12Z] WHO: praxis-worker | WHAT: subagent closed | WHY: hook-recorded at SubagentStop, keyed close for corr=adcc29c9e58c02f6d, matched 1 open row(s) | ...
+- [2026-11-07T13:20:27Z] WHO: praxis-worker | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session 3ef528c corr=ae79d0bef0a1cbfd1 | ...
+- [2026-11-07T13:24:19Z] WHO: praxis-worker | WHAT: subagent closed | WHY: hook-recorded at SubagentStop, keyed close for corr=ae79d0bef0a1cbfd1, matched 1 open row(s) | ...
~~~
- **DECISION_LOG.md:** its 13:02:05Z mtime predates this unit's first command (13:04:25Z). That this was the master's own append is INFERRED.
- **Pre-existing modifications:** `.claude/settings.json`, `scripts/` and `specs/SPEC_RUBRIC.md` were already modified at session start (session git status), and their mtimes predate this unit.
- **VM handoff and walk-forward spec:** their mtimes are from 2026-11-06. Neither was edited by this unit.

## Adversarial findings
**W3: NOT REFUTED, 8 MINOR, all fixed:**
1. The "in parallel" wording understated the order: the walkthrough line was on disk before the entry.
2. The MANIFEST "house practice" claim was only partly true: `69ec506` edited a row in place.
3. Ruling 7(7) "the VM session stops" went past his words.
4. Q1's routing under Q10 had no INFERRED label.
5. Q3's settling authority was not separated from proposing.
6. Ruling 6's partial pass read as current state.
7. Ruling 5 claimed to answer NEEDS AMEAR 6 whole.
8. Three precision issues:
   - "Go-live section" was imprecise about the line's location.
   - MANIFEST row 259 said "committed" for an untracked file.
   - The S6 paragraph named no Q5-vs-F2 interaction.

**W4: REFUTED, 2 MAJOR and 5 MINOR, all fixed by the manager:**
- **MAJOR 1:** the S4 paragraph cited DECISIONS.md's own mtime, a value that goes stale on every save. It now cites only the walkthrough's mtime (unchanged since 13:08:15Z) and states why this file's own mtime is not cited.
- **MAJOR 2:** the entry contradicted the dispatch row on placement. The ruling-10 bullet now quotes the row ("`## Go-live (R-VN4-14)` section … below the existing checklist"). It also states three things:
  - The brief gives that section as lines ~26–37, and :38 is the end of that range.
  - A strictly literal reading of the heading would put the line after :27.
  - Placement is the master's choice, not Amear's word, and the master may move the line.
- **MINORs:**
  - Ruling 10(ii) "not duplicated" is now labelled the master's choice.
  - Walkthrough :38 now points to the rulings file :29 for the verbatim text (the 12:55 row only paraphrases it).
  - The Q3 settling authority is labelled INFERRED.
  - The F2 sentence names all three F2 terms.
  - Both Status lines now say "First written 13:08:18Z; revised by the same unit before its return…".

**Adversarial result on the final text: none yet.** W4's fixes were made by the manager and checked by script (quotes, invariants, probes, S13). No fresh adversary has attacked them, because this unit's 4-worker cap is spent. Each fix round produced new MINOR findings, and that pattern is likely to continue.

## S6 cross-block check
- **F1–F4:** not modified. No code, config, hook or spec was edited (the protected-path evidence above shows no edit by this unit).
- **F2 (`specs/SPEC_RUBRIC.md`:30):** ruling 4 Q5 (Flat1559, "flatten on the 15:59 bar") bears on all three F2 terms (breaker #4 at 11:30 ET, breaker #5 15:00–18:00 ET, Deviation B at 16:00 ET). This is recorded in D-2026-11-07-A and not resolved.
- **O1 (:74):** ruling 4 Q8 bears on O1's required gate-set statement. This is recorded and not resolved; it is left to D-2026-11-07-B and its audit.
- **O4:** untouched.
- **VM handoff §8:** rows 4, 5, 7, 9, 10, 11 and 12 are recorded as answered, to be APPLIED by a later unit. Rows 1, 2, 3 and 8, and the route half of row 11, stay Amear's (S8).

## Files staged
Nothing staged; working tree only, per brief.
~~~
$ git diff --cached --stat | tail -1          (the pre-existing old as-is index, unchanged)
 12 files changed, 5726 insertions(+), 2 deletions(-)
$ git diff --cached --name-only | grep -c -e DECISIONS.md -e MANIFEST.md -e fusion-shared -e 2026-10-28-voice -e amear-rulings -e gate-addendum-5 -e rulings-filing-manager
0
$ git diff --numstat HEAD -- DECISIONS.md MANIFEST.md docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md
167	0	DECISIONS.md
8	0	MANIFEST.md
1	0	docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md
$ git status --porcelain -- <the seven commit-set paths>
 M DECISIONS.md
 M MANIFEST.md
 M docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md
?? docs/reports/2026-10-28-voice-session-notes.md
?? docs/reports/2026-11-06-gate-addendum-5-manager.md
?? docs/reports/2026-11-07-amear-rulings-morning.md
~~~
This report (`docs/reports/2026-11-07-rulings-filing-manager.md`) is also `??`; it did not exist when the status above was taken. DECISIONS.md's +167 is this unit's 98 lines plus the 69 that were already in the working tree (addendum 5 and the D-2026-11-06-D draft). The blob the master builds should end at line 1289.

## Result
**Result: BLOCKED.** All five deliverables are on disk and mechanically verified. What the work still needs is one fresh ADVERSARIAL pass on the post-W4 text: the S4 timing paragraph, the ruling 10 and Q3 bullets, the S6 F2 sentence, both Status lines, and walkthrough :38. That would be a 5th worker, above this unit's cap of 4. The master's auditor may serve as that pass. No PASS is claimed for text no adversary has seen.

Post-write probe of this report (token probe v2 and category probe on this file) follows on the next line.
~~~
docs/reports/2026-11-07-rulings-filing-manager.md tokens_hit=0 confined_tokens_hit=0 lines=none
drug=6 pill=6 dose=6 prescri=6 brand=6
~~~
The category counts of 6 are self-matches (observer effect): each is one of the six pasted probe-output lines above, which read `drug=0`, `pill=0` and so on. No other line in this report contains those words. The token-probe line is unaffected, because it contains no tokens.

**Disclosure (after Result was written):** at 13:3xZ the manager wrote one memory file and one index line under `.claude/agent-memory/praxis-manager/`, which this brief forbids ("Do NOT edit … `.claude/`"). Both were removed by the manager straight away (file deleted; index line removed; `grep -c deid_probe MEMORY.md` = 0). The lesson, that the category-word probe cannot see the title, is in this report instead, for the master to file if wanted.

## Correction 1 (after audit FAIL 1)

Unit `2026-11-07-rulings-filing-correction-1` (praxis-manager). Authorisation: DECISION_LOG `2026-11-07T13:36:00Z` (WHO: praxis-master), items (a), (b), (c), (e); item (d) left as is. Mode: the manager made the edits (each is one paragraph or one/two lines); 2 ADVERSARIAL workers. Nothing staged. Nothing above this section was edited.

### Audit findings corrected (REPORTED BY praxis-auditor, via the `13:36:00Z` row)
1. S1 / check f: DECISIONS.md:1282 and this report's :223 claim the walkthrough mtime was "unchanged since" 13:08:15Z. Not pasted, and false (`stat` reads 13:25:12Z; line 38 was rewritten in the W4 round, :27). :223 stays as written; this section supersedes it.
2. S13: the standing limitation sentence appeared 0 times in `docs/reports/2026-10-28-voice-session-notes.md` and in `docs/reports/2026-11-07-amear-rulings-morning.md`.
3. MINOR: DECISIONS.md:1262 and :1280 say "the last block of this file". That is true of the working tree and false of the blob to be committed.

### Process log
1. 13:37:52Z: took the walkthrough `stat` before touching anything (pasted below). Took pre-edit hashes.
2. (a) inserted the Correction 1 paragraph as DECISIONS.md :1290 (blank :1289 and :1291). (b) appended the two S13 lines to both files. (c) edited MANIFEST row 259 in place.
3. ADVERSARIAL W-A (given the artifacts and S1/S4/S8/S13 only) → REFUTED: 2 MAJOR, 3 MINOR (table below).
4. Fix round. At 13:43:51Z both files were truncated back to their bodies (hashes equal to Amear's originals, pasted). At 13:44:03Z the :1290 paragraph was replaced so that the S13 append and its void clause are recorded in DECISIONS.md. At 13:44:12Z both files were re-appended. Then row 260 got both hashes.
5. ADVERSARIAL W-B (fresh; not given W-A's reasoning) → REFUTED: 0 MAJOR, 4 MINOR. MINORs 2–4 were fixed in the :1290 paragraph at 13:47:43Z (labels and a quote only). MINOR 1 is left open: it is outside the brief's line set.
6. Deviations from the brief, all disclosed here: the :1290 paragraph is the third version of this unit's own uncommitted text, and v3 was not attacked again because the worker cap is 2. The rulings-file addendum says "not part of Amear's rulings" where the brief's form says "notes" (W-A MINOR 5). Row 260 carries both hashes beyond the brief's wording; the `13:36:00Z` row says "row 260 likewise".

### Verification evidence
`$SF` is a scratch file holding the 90-byte sentence. It is used with `grep -cFf` so that no command pasted here contains the sentence (this keeps the observer effect out).
~~~
$ TZ=UTC stat -f '%Sm' -t '%Y-%m-%dT%H:%M:%SZ' docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md   (first command of the unit, 13:37:52Z)
2026-11-07T13:25:12Z
$ (same command, just before this section was written)
2026-11-07T13:25:12Z
$ grep -n "^## " DECISIONS.md | tail -4 | cut -c1-70
1165:## 2026-11-06 — D-2026-11-04-B addendum 5: third hand-back shap
1192:## 2026-11-07 — D-2026-11-04-B addendum 6: ratification (WHO: a
1203:## 2026-11-07 — D-2026-11-07-A: Amear's ten morning rulings (ty
1292:## 2026-11-06 — D-2026-11-06-D: walk-forward values proposed un
$ head -1288 DECISIONS.md | shasum -a 256          (pre-edit; identical after every edit)
b393eb8cd59eef300e8bec2bb32a2f395ad0ac7dced3c3959e4057f9d54132c4  -
$ tail -n +1289 DECISIONS.md | shasum -a 256       (pre-edit: blank line + D-2026-11-06-D block)
1cf4abafda06928afe8689564f9da91a1d4bf4123f0f3de6a22959ed086bc98a  -
$ tail -n +1291 DECISIONS.md | shasum -a 256       (after the final edit, 13:47:43Z)
1cf4abafda06928afe8689564f9da91a1d4bf4123f0f3de6a22959ed086bc98a  -
$ git rev-parse --short HEAD; git show HEAD:DECISIONS.md | wc -l
3ef528c
    1163
~~~
(b) notes file, final append (13:44:12Z):
~~~
$ shasum -a 256 docs/reports/2026-10-28-voice-session-notes.md; wc -l (before)
7999c03410ffd0e83253100ea76714b80f0f211a1e363470965231edaeb6cb48  docs/reports/2026-10-28-voice-session-notes.md
      56
$ head -56 docs/reports/2026-10-28-voice-session-notes.md | shasum -a 256
7999c03410ffd0e83253100ea76714b80f0f211a1e363470965231edaeb6cb48  -
$ shasum -a 256 docs/reports/2026-10-28-voice-session-notes.md; wc -l (after)
e749117f85383409cf53849e93d0e98467a96dadf88dc207256d238aeba93420  docs/reports/2026-10-28-voice-session-notes.md
      58
~~~
(b) rulings file, final append (13:44:12Z):
~~~
$ shasum -a 256 docs/reports/2026-11-07-amear-rulings-morning.md; wc -l (before)
975f9c483ed8d1b19d719c461c611c369be97e20b58ef38abdfdc7e3d4031c78  docs/reports/2026-11-07-amear-rulings-morning.md
      44
$ head -44 docs/reports/2026-11-07-amear-rulings-morning.md | shasum -a 256
975f9c483ed8d1b19d719c461c611c369be97e20b58ef38abdfdc7e3d4031c78  -
$ shasum -a 256 docs/reports/2026-11-07-amear-rulings-morning.md; wc -l (after)
64cdf8bcf2bcc777c332b306938db7c36e842085daee1b3b72a2cc8f9f2fa4e6  docs/reports/2026-11-07-amear-rulings-morning.md
      46
~~~
The truncation at 13:43:51Z (fix round) showed `7999c034…cb48` / 56 and `975f9c48…1c78` / 44. The notes file's first append gave the same whole-file hash, `e749117f…3420`.

(c) MANIFEST:
~~~
$ git diff --numstat HEAD -- MANIFEST.md
8	0	MANIFEST.md
$ sed -n 254,255p MANIFEST.md | shasum -a 256
00b7e89357980786c291024464e09368cb291b928ff99eba5d64925d011beea2  -
$ sed -n 1,258p MANIFEST.md | shasum -a 256        (pre-edit and post-edit)
783f9b4129f25207d51d4f848f4e3acdbfade2f7cb066ea842a120aa34ca03d7  -
$ tail -n +261 MANIFEST.md | shasum -a 256         (pre-edit and post-edit)
6b8412fbbca4e57f93032c95599936c3882a49b1bc1c8b2306887be7a010d1a4  -
~~~
$ sed -n 259,260p MANIFEST.md
| /docs/reports/2026-10-28-voice-session-notes.md | Report | 2 | 2026-10-28 | UPDATE ROW 2026-11-07 (append-only registry; supersedes row 244's "proposed for commit … (master's settlement…)"): to be carried in the next gated commit as a one-file exception (untracked at time of row) to the as-is rule by Amear's ruling 2 (DECISION_LOG 2026-11-07T12:55:00Z, WHO: amear; D-2026-11-07-A); body (lines 1–56) byte-identical to Amear's file, sha256 7999c03410ffd0e83253100ea76714b80f0f211a1e363470965231edaeb6cb48; one two-line S13 addendum appended by unit 2026-11-07-rulings-filing-correction-1 (whole-file sha256 e749117f85383409cf53849e93d0e98467a96dadf88dc207256d238aeba93420) |
| /docs/reports/2026-11-07-amear-rulings-morning.md | Report | 2 | 2026-11-07 | Amear's ten morning rulings (typed, 2026-11-07) filed verbatim at lines 9–31 by praxis-master (DECISION_LOG 2026-11-07T12:55:00Z, WHO: amear), followed by the master's filing notes (not rulings); source of D-2026-11-07-A and D-2026-11-04-B addendum 6; S13 addendum (two lines) appended by unit 2026-11-07-rulings-filing-correction-1 (body lines 1–44 sha256 975f9c483ed8d1b19d719c461c611c369be97e20b58ef38abdfdc7e3d4031c78; whole-file sha256 64cdf8bcf2bcc777c332b306938db7c36e842085daee1b3b72a2cc8f9f2fa4e6) |
~~~

S13 counts across the seven commit-set files (addendum 5, :1165–1190, is added for completeness):
~~~
$ wc -c < "$SF"; shasum -a 256 "$SF" | cut -c1-64
      90
816836b085174d186c602ff95da9035d47853b4ca4e4447c6c4d4b711afcce30
$ sed -n 1165,1190p DECISIONS.md | grep -cFf "$SF"
1
$ sed -n 1192,1201p DECISIONS.md | grep -cFf "$SF"
1
$ sed -n 1203,1290p DECISIONS.md | grep -cFf "$SF"
1
$ grep -cFf "$SF" docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md
1
$ grep -cFf "$SF" docs/reports/2026-10-28-voice-session-notes.md
1
$ grep -cFf "$SF" docs/reports/2026-11-07-amear-rulings-morning.md
1
$ grep -cFf "$SF" docs/reports/2026-11-06-gate-addendum-5-manager.md
1
$ grep -cFf "$SF" MANIFEST.md   (not applicable; a registry)
0
$ grep -cFf "$SF" docs/reports/2026-11-07-rulings-filing-manager.md   (before this section was appended)
1
~~~

Numstat for every path this unit touched:
~~~
$ git diff --numstat HEAD -- DECISIONS.md MANIFEST.md docs/reports/2026-10-28-voice-session-notes.md docs/reports/2026-11-07-amear-rulings-morning.md docs/reports/2026-11-07-rulings-filing-manager.md
169	0	DECISIONS.md
8	0	MANIFEST.md
$ git status --porcelain -- (same paths)
 M DECISIONS.md
 M MANIFEST.md
?? docs/reports/2026-10-28-voice-session-notes.md
?? docs/reports/2026-11-07-amear-rulings-morning.md
?? docs/reports/2026-11-07-rulings-filing-manager.md
$ git diff HEAD -- DECISIONS.md MANIFEST.md | grep -c "^-[^-]"
0
$ git diff --cached --name-only | grep -c -e DECISIONS.md -e MANIFEST.md -e fusion-shared -e 2026-10-28-voice -e amear-rulings -e gate-addendum-5 -e rulings-filing-manager
0
$ shasum -a 256 docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md docs/reports/2026-11-06-gate-addendum-5-manager.md   (pre-edit and post-edit: equal)
64571309cc933ef5f23ba09e09ea890654f75d8751c6575802098d0d9eca3c35  docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md
f09fed9ee284b0c196fbff3746dba45cd40bd9c2f8130181a11a6f9641975256  docs/reports/2026-11-06-gate-addendum-5-manager.md
~~~
The three untracked files print nothing under `git diff --numstat HEAD`. Their line counts are: notes 56 → 58 and rulings 44 → 46 (above). For this report, the counts are in the last evidence block.

### Adversarial findings
| # | Worker | Sev | Finding (REPORTED BY the worker) | Disposition |
|---|---|---|---|---|
| 1 | W-A | MAJOR | :1244 "The file is carried unedited" became false after the append, and no DECISIONS.md text recorded the append or its void clause | Fixed. :1290 now narrows :1244 to the body and records the master's decision and void clause. The files were truncated back before that text was written and re-appended after it (timestamps above). |
| 2 | W-A | MAJOR | v1 called the whole :1282 sentence "false"; `stat` disproves only "unchanged since" | Fixed. The 13:08:15Z first-append time is now labelled UNVERIFIED, and the same-unit admission is kept |
| 3 | W-A | MINOR | "committed blob" was wrong against HEAD (1163 lines) | Fixed. It now reads "the blob the master's gated commit is to carry" |
| 4 | W-A | MINOR | row 260 carried no hashes | Fixed. Both hashes are in the row |
| 5 | W-A | MINOR | the rulings-file label said "Amear's notes" | Fixed. It now says "Amear's rulings" |
| 6 | W-B | MINOR | MANIFEST.md:263 still points to `DECISIONS.md:1203-1288`; the entry now ends at :1290 | OPEN. The brief says "touch NO other line", so this is left for the master |
| 7 | W-B | MINOR | the forward claim about the commit blob is unlabelled | Fixed. It is now labelled INFERRED |
| 8 | W-B | MINOR | the :1244 quote was not verbatim | Fixed. The quote is now "The file is carried unedited" |
| 9 | W-B | MINOR | "unedited" was not labelled as the master's word | Fixed. It is labelled, REPORTED BY the `13:36:00Z` row |

W-B confirmed (REPORTED BY W-B): the body hashes hold, the S13 counts are 1, `head -1288` and `tail -n +1291` match, and both `---` lines follow list items, so each renders as a rule, not a heading underline.

This report's own S13 count. It was taken after everything above was appended and before this block and the Result line were added. Neither of those contains the sentence.
~~~
$ grep -cFf "$SF" docs/reports/2026-11-07-rulings-filing-manager.md; wc -l < docs/reports/2026-11-07-rulings-filing-manager.md
1
     418
~~~
Result: PASS

### Correction 2 (MANIFEST.md:263 pointer)

Authorised by DECISION_LOG.md `[2026-11-07T13:52:00Z] WHO: praxis-master` (master cannot write MANIFEST.md; routed to this manager).
Change: one token on one line — MANIFEST.md:263 (`/DECISIONS.md` row) `1203-1288` → `1203-1290`; all other lines byte-identical to the pre-edit copy (diff of both with line 263 deleted printed `OTHER_LINES_IDENTICAL`).
Checks, pasted (first command is the precondition: rows 257+ uncommitted):

~~~
$ git show HEAD:MANIFEST.md | wc -l
     256
$ sed -n 263p MANIFEST.md
| /DECISIONS.md | Log | 2 | 2026-11-07 | D-2026-11-04-B addendum 5 (DECISIONS.md:1165-1190, written 2026-11-06 after the work; S4 not met), D-2026-11-04-B addendum 6 (DECISIONS.md:1192-1201; ratification of addendum 5's timing, WHO: amear, DECISION_LOG 2026-11-07T12:55:00Z; unblocking artifact for Praxis_build-uqb) and D-2026-11-07-A (DECISIONS.md:1203-1290; Amear's ten morning rulings verbatim, Q3 stop multipliers as the master's decision under R-1104-2) appended; the parked D-2026-11-06-D draft (last block) not included |
$ git diff --numstat HEAD -- MANIFEST.md
8	0	MANIFEST.md
$ sed -n 254,255p MANIFEST.md | shasum -a 256
00b7e89357980786c291024464e09368cb291b928ff99eba5d64925d011beea2  -
$ sed -n 1,258p MANIFEST.md | shasum -a 256
783f9b4129f25207d51d4f848f4e3acdbfade2f7cb066ea842a120aa34ca03d7  -
$ grep -n "^## " DECISIONS.md | tail -3 | cut -c1-70
1192:## 2026-11-07 — D-2026-11-04-B addendum 6: ratification (WHO: a
1203:## 2026-11-07 — D-2026-11-07-A: Amear's ten morning rulings (ty
1292:## 2026-11-06 — D-2026-11-06-D: walk-forward values proposed un
$ sed -n 1290p DECISIONS.md | cut -c1-60
**Correction 1 (before commit, after audit FAIL 1 on S1/S13/
~~~

Result: PASS

## Pointer note 2026-11-10 (filer's note, not a ruling)

The "superset token probe v2" method at lines 113-118 above seeds its candidate set from `HEAD:DECISION_LOG.md:47` (line 114). Its liveness arm (line 116) runs on the whole of `HEAD:DECISION_LOG.md` and on `7d9be8e:HANDOFF.md`, as the two LIVENESS lines at 120-121 show; in `HEAD:DECISION_LOG.md` the withheld term is on line 47 only. From the scrub-forward commit on (bead Praxis_build-8ux; DECISION_LOG row 2026-11-10T09:08:00Z), `DECISION_LOG.md:47` no longer carries the withheld term. A re-run must therefore read `0eea766:DECISION_LOG.md:47` for the seed and `0eea766:DECISION_LOG.md` for the liveness arm, instead of the `HEAD:` forms, or extract the term from the gitignored source, as docs/reports/2026-11-10-d9-housekeeping-manager.md V5 does. The `7d9be8e:HANDOFF.md` arm is pinned to a commit and is not affected. No line above this note was changed.
