# 2026-11-14 dirty-tree-sort — manager report (READ-ONLY unit, step 2(c))

This is a sort only. Nothing was filed, staged, moved or edited. The master decides what gets filed.
Baseline: `git rev-parse HEAD origin/main` = `9ff8a48f8ff74bad7b81c08b52f66cf063db76bd` twice.

## Summary table

Classes: CF = CLEAR-FILE, CNA = CLEAR-BUT-NEEDS-AUDIT, U = UNCLEAR. "n" is the name count (`grep -ci "$N"`).

| # | group | paths | owner | audit status | class | evidence pointer |
|---|---|---|---|---|---|---|
| T1 | .claude/settings.json (+10/-0) | 1 | session 39 closer, bead 43n (open) | none; hunks excluded from the 2026-11-06 batch | U (config, no graded PASS) | DECISION_LOG :543; :117; W7 C7 |
| T2 | scripts/dispatch-log-writeahead.sh (+102/-2) | 1 | bead 43n | none; producer self-FAIL, audit not spawned | U (script, no PASS) | DECISION_LOG :117 (2026-07-28T16:25Z) |
| T3 | docs/specs walk-forward spec + values (5/5, 21/21) | 2 | wf-spec-amendment, bead diq | FAIL 2, PARKED | U | `bd show Praxis_build-diq` |
| T4 | modified F4 reply-filing report | 1 | 2026-10-28 F4 reply filing | appended auditor PASS section, left out of 18d94a5 | U (n=3 in added lines; also deletes 2 lines that 18d94a5 added under D9) | W7 C10; blame below |
| T5 | modified nightly-checks review report | 1 | 2026-10-28 nightly-checks review | re-audit PASS at :1335-1400, never committed | U (added n=0; committed part n=4, not listed in c2w) | DECISION_LOG :439 |
| T6 | AUDIT_LOG.md, rows 90-92 (mid-file) | 3 rows | minter (o3d, y9c) | no row explains the insertion | U | W6 A1 |
| T7 | AUDIT_LOG.md, rows 104-153 (tail) | 50 rows | minter; each records a committed unit | rows are audit output and were never themselves audited; rows 112/113 are two PASSes on one index with different hashes | U (manager overrides W6's CF) | W6 A2; W7 C3 |
| T8 | DECISIONS.md, the 92 pre-existing lines | 92 lines | R6 step 2 entry D-2026-11-12-B, bead ckh | FAIL x2, PARKED; byte-copy on parked/Praxis_build-ckh @ 9bf0516 | U | DECISION_LOG :865, :866 |
| T9 | DECISION_LOG.md rows 13:44:24Z-17:43:11Z | 12 rows | gfx close flush | FAIL x2, PARKED | U | DECISION_LOG :932, :933 |
| T10 | DISPATCH_LOG.md rows 13:42:23Z, 13:43:52Z | 2 rows | b64ff1a's auditor hook rows | not in b64ff1a; the next flush (gfx) is parked | U | DISPATCH_LOG :2770-:2771 |
| T11 | DISPATCH_LOG.md rows 17:03:10Z-17:42:39Z | 20 rows | gfx | PARKED | U | stamp list below |
| T12 | HANDOFF.md (+27), STATUS.md (+8) | 2 | gfx 17:00Z-run cards | FAIL x2, PARKED | U | `bd show Praxis_build-gfx` |
| T13 | MANIFEST.md M1 (8 rows, diq) and M2 (6 rows, ckh) | 14 rows | diq / ckh | PARKED | U | W6 M1, M2 |
| T14 | MANIFEST.md M3, O3 rows | 6 rows | O3, bead p3l | 2 rows (manager, worker1) were in the FAILed idx-o3; 4 correction rows never audited | 2 U + 4 CNA | DECISION_LOG :880, :881, :886 |
| T15 | MANIFEST.md M4 (o4-parity-manager row) | 1 row | O4, yra | report has `Result: RESULT_LINE` | U | DECISION_LOG :912 |
| T16 | MANIFEST.md M5 (open-a1 manager, worker1 rows) | 2 rows | OPEN-A1, fgd | in the FAILed idx-oa1 | U (manager overrides W6's CNA) | DECISION_LOG :918, :919 |
| T17 | ISSUE_REGISTER.md (line 63 changed; 3 entries added) | 1 | session 42 / sessions 51, 53 | none; line 63 undoes D9 de-identification | U | W6 I1, I2; token count below |
| T18 | the staged evidence PNG for the F4 reply | 1 | 2026-10-28 F4 reply | held out of 18d94a5 (third-party full-name address) | U (n=1 in its path; c2w) | 18d94a5 subject |
| U1 | session36 reports | 2 | session 36 | agent-key unit HELD; y9c PARKED | U | DECISION_LOG :71; `bd show Praxis_build-y9c` |
| U2 | session37 restage reports | 2 | session 37 restage | restage-audit `Result: FAIL`; y9c PARKED | U | Result lines below |
| U3 | session38 guard-evasion-test | 1 | session 38, bead jcw | jcw BLOCKED; its auditor returned no verdict | U | DECISION_LOG :99 |
| U4 | session39 agents-dir-write-path | 1 | session 39, bead s8g (open P0) | no audit found | CNA (least traced: s8g history not fully read) | DECISION_LOG :121 |
| U5 | session39 closer reports + closer script + test | 5 + 2 | bead 43n | self-FAIL; closer edited at 16:46Z, after the FAIL report; live as a SubagentStop hook from the uncommitted settings | U | DECISION_LOG :117; W7 C8 |
| U6 | session40 reports | 4 | beads cbf, cyd | cbf-audit `Result: FAIL`; cyd says the disposition claim is false | U | Result lines; `bd show` |
| U7 | session41 cyd reports | 8 | bead cyd (open bug) | none | U | `bd show Praxis_build-cyd` |
| U8 | session41 c1 reports | 3 | C1 unit, y9c lineage | y9c title "PARKED ... audit FAIL 2", though 5067d32 landed under y9c | U | DISPATCH_LOG :157, :159 |
| U9 | 2026-08-06 facts pack, assessment, subreport | 3 | session 42 (master transcribing the auditor) | no mint after 2026-08-05 | CNA | DECISION_LOG :165; AUDIT_LOG |
| U10 | 2026-08-07 f3 research UNGRADED | 1 | filed by master; written by an external research agent | self-declared ungraded; must not be cited for F3 | CNA | its header |
| U11 | dj2 reports (session48 x5, session49 x1) | 6 | bead dj2 | FAIL 1 of 2, HELD; the stop decision is Amear's | U | DECISION_LOG :291, :325, :331 |
| U12 | session52 x5 + session53 x9 | 14 | ambiguous: the seat says it did not write 13 of them | vu8 FAIL on the corpus read | U | DECISION_LOG :389 |
| U13 | session53-parallel-handoff | 1 | the 2026-08-29 orchestrator seat | none | CNA | DECISION_LOG :389 item (3) |
| U14 | F4 reply reports (rep in path) | 10 | 2026-10-28 F4 reply | 3 of them FAIL; all hold the name | U (c2w) | W4 |
| U15 | wf-spec-amendment reports + u7 patch | 5 + 1 | diq | FAIL 2, PARKED | U | W4; DECISION_LOG :750 |
| U16 | scrub-forward-c1-adversarial | 1 | scrub-forward unit (16c7bfe) | own `Result: FAIL`; n=1 | U | DECISION_LOG :794 |
| U17 | hermes-replies-grading manager + w1, w2, w4, w6 | 5 | grading unit, which died with no close | manager "(pending)"; 3 workers FAIL; 2 hold the name | U | DECISION_LOG :823, :824 |
| U18 | singles: 10-26 review, 10-28 review-note, 10-31 voice handoff, two 11-01 manager records, c7-probe-fresh-manifest | 6 | one each | none for filing; 11-01 and c7 kept out by master decision | CNA (re-including them is the master's call under D1) | DECISION_LOG :616, :622, :776 |
| U19 | vm/replies (four files of 2026-11-10) | 4 | written by Hermes; the grading unit was to file them | none; one stamp is 59 min later than its file time (not explained) | CNA | W4 E3 |
| U20 | O3 manager + worker1 | 2 | O3, p3l | in the FAILed idx-o3 | U | DECISION_LOG :880, :881 |
| U21 | O3 correction-1 pair, correction-2 pair, evidence.md | 5 | O3, p3l | never in an audited index; kept out by master | CNA (manager applies the literal rule, as for O4; W5 had U) | DECISION_LOG :883, :886 |
| U22 | O3 cure3 pair | 2 | O3 | none for filing | CNA | DECISION_LOG :897 |
| U23 | R6 engine-entry reports | 5 | ckh | FAIL x2, PARKED; byte-identical on the parked branch | U | W5 cmp; my cmp below |
| U24 | o4-parity-manager | 1 | O4, yra | `Result: RESULT_LINE` placeholder | U | DECISION_LOG :912 |
| U25 | other O4 reports (parity w1-w4, reduce, reduce2, repoint, cure1) | 12 | O4, yra (closed) | adversary FAILs only, never in an audit index | CNA | DECISION_LOG :913, :915; W5 |
| U26 | open-a1 manager + worker1 | 2 | OPEN-A1, fgd | in the FAILed idx-oa1 | U | DECISION_LOG :918, :919 |
| U27 | open-a1-cure-worker1 | 1 | OPEN-A1 | never audited | CNA | DECISION_LOG :925 |
| U28 | open-a2-worker1 | 1 | OPEN-A2 | n=1; its last Result is FAIL | U (c2w) | `bd show Praxis_build-c2w` |
| X | out of scope | 15 reports + flush rows + post-01:27Z lines | units (a) and (b), and the end-of-session flush | — | not classified | DECISION_LOG :943 |

**Tallies.**
- CLEAR-FILE: 0 items. No PASS in AUDIT_LOG covers exactly any dirty content that was never committed.
- CLEAR-BUT-NEEDS-AUDIT: 36 untracked files (U4 1, U9 3, U10 1, U13 1, U18 6, U19 4, U21 5, U22 2, U25 12, U27 1; no code or config file is in this class) and 4 MANIFEST rows (T14).
- UNCLEAR: everything else in scope.
- Untracked total in scope: 116 = 51 (July to August) + 27 (Oct 26 to Nov 11) + 31 (Nov 12 to 13) + 7 (patch, closer script, closer test, four vm replies).

## Task
Step 2(c) of `docs/reports/2026-11-13-hermes-handoff-strategy-search.md` (:47): sort the dirty tree into units with a clear owner and audit, and list the unclear items. Master scope rows are DECISION_LOG 2026-11-14T01:25:40Z (:942) and 01:27:05Z (:943). This unit sorts only; the master decides what is filed.

## Rubric criteria addressed
- S1: every claim below rests on pasted output, either here or in a worker report that I re-checked.
- S2: classes are no higher than the evidence. Where the evidence is thin, I say so (U4, T7, U19).
- S7: nothing committed or staged by this unit.
- S8: Amear's questions are listed, not answered.
- S13: the closing line.

## Workers dispatched (id, mode, outcome)
| worker | mode | scope | outcome |
|---|---|---|---|
| W1 | BUILD | 8 ledger files | hit 40-turn cap, no report; re-scoped as W6 plus my own captures |
| W2 | BUILD | code, config, specs, modified reports | hit 40-turn cap, no report; manager captured scope directly |
| W3 | BUILD | July to August reports (51) | hit 40-turn cap, no report; manager captured scope directly |
| W4 | BUILD | Oct 26 to Nov 11 reports + vm replies (31) | `Result: PASS`; -worker4.md |
| W5 | BUILD | Nov 12 to 13 reports (31) | `Result: PASS`; -worker5.md |
| W6 | BUILD | AUDIT_LOG, DECISIONS, MANIFEST, ISSUE_REGISTER | `Result: PASS`; -worker6.md |
| W7 | ADVERSARIAL | 17 classifications (C1-C17) | 1 refuted, 5 partly, 11 confirmed; -worker7.md |

There are no -worker1, -worker2 or -worker3 report files. Those three workers wrote nothing. Several other dispatch attempts were refused by the session-wide cap ("Concurrent subagent limit reached. You can run 8 subagents at once."), because the concurrent units' agents count against it.

## Process log
1. Read specs/SPEC_RUBRIC.md S1 to S13 and the master scope rows :942 and :943.
2. Inventory and partition: 131 untracked, 15 excluded (unit (a)), 116 in scope, split into 4 groups (`wc -l`: g2 7, g3 51, g4 27, g5 31).
3. Dispatched W1. W2 to W5 were refused by the cap and retried as slots freed. W1, W2 and W3 died at the turn cap, so I re-scoped W1 as W6 and did W2's and W3's scopes with batched commands.
4. Checked worker claims myself before folding them in. Then sent W7 the artifacts and claims only, without the workers' reasoning.
5. Reconciled the class conflicts between W5 and W6 with one rule. A file that sat in an index an audit FAILed is UNCLEAR. A never-audited round report of a unit that is not parked is CNA, even if the master kept it out of the commit (that exclusion is the master's to lift under D1).
6. Hook hazards observed:
   - mint-guard denied two read-only commands that named the audit ledger ("BLOCKED: mint-guard: praxis-manager (Bash) command writes AUDIT_LOG").
   - no-commit-guard denied a read-only `git branch --contains` / `merge-base` chain.
   - gate-commit denied a scratchpad heredoc whose text contained flag words.
   - gate-manager-output.sh (Stop) blocked me on other units' files ("'.../2026-11-14-evening-rulings-worker5.md' has no Verification evidence section", and the same for -worker6.md). It grades `ls -t docs/reports/*.md | head -1` (script :6), which is whatever file is newest across all concurrent units.

## Verification evidence

Inventory (pasted):
```
$ git diff --numstat   (at unit start; [rep] substituted)
10 0 .claude/settings.json | 54 0 AUDIT_LOG.md | 92 0 DECISIONS.md | 23 0 DECISION_LOG.md | 68 0 DISPATCH_LOG.md
27 0 HANDOFF.md | 7 1 ISSUE_REGISTER.md | 23 0 MANIFEST.md | 8 0 STATUS.md
73 2 docs/reports/2026-10-28-f4-[rep]-reply-filing.md | 66 1 docs/reports/2026-10-28-nightly-checks-plan-review-rebuild.md
5 5 docs/specs/2026-11-05-walk-forward-spec.md | 21 21 docs/specs/2026-11-06-walk-forward-values.md | 102 2 scripts/dispatch-log-writeahead.sh
$ git diff --numstat   (at report time; growth is concurrent units and the flush)
DECISIONS.md 252 0 | DECISION_LOG.md 26 0 | DISPATCH_LOG.md 109 0 | MANIFEST.md 38 0 | others unchanged
$ git diff --cached --name-only | wc -l ; git diff --cached --name-only | grep -ci "$N"
1
1
$ wc -l untracked.txt inscope.txt ; wc -l g2 g3 g4 g5
131 untracked.txt | 116 inscope.txt | 7 g2 | 51 g3 | 27 g4 | 31 g5
```

Ledger windows (pasted):
```
$ git diff -U0 -- DECISION_LOG.md | grep '^+' | grep -oE '^\+- \[[0-9TZ:-]+\]'
13:44:24 17:02:02 17:12:19 17:15:15 17:18:24 17:19:15 17:22:34 17:33:15 17:37:20 17:38:10 17:41:08 17:43:11   (2026-11-13; 12 rows, gfx)
19:40:54 19:58:43 20:21:12 20:25:43 20:34:10 20:36:45 21:03:55 ; 2026-11-14 01:23:10 01:25:40 01:27:05 01:28:05 01:29:25 ...   (flush, out of scope)
$ (DISPATCH_LOG added stamps before 19:40Z)
2026-11-13T13:42:23Z 2026-11-13T13:43:52Z 2026-11-13T17:03:10Z ... 2026-11-13T17:42:39Z (20 rows)
$ grep -n '2026-11-13T13:4[23]' DISPATCH_LOG.md
2770: [13:42:23Z] WHO: praxis-auditor | subagent spawned | WHERE: session 4ffce95 corr=a4797abd6f144fbcc
2771: [13:43:52Z] WHO: praxis-auditor | subagent closed | closes corr=a4797abd6f144fbcc
$ git show b64ff1a --format='%h %ci'  ->  b64ff1a 2026-11-13 08:43:58 -0500
$ sed -n '932p;933p' DECISION_LOG.md
932: [17:41:08Z] Close-flush audit FAIL 1 (praxis-auditor a090df765a1674235 ...)
933: [17:43:11Z] Close-flush audit FAIL 2 (praxis-auditor af2e9b6c15d9672bd): PARKED per the absolute park rule
```

HANDOFF and STATUS added lines (trimmed):
```
+## Resume card — 2026-11-13 run (from 17:00Z, timer prompt) — `main` = `origin/main` = `661e073` plus this close flush ...
+## 2026-11-13 (timer run 17:00Z) — short status by praxis-master
```

Code and config (one line each, plus audit):
```
$ git diff -- .claude/settings.json   ->  index 5ecfc80..1fe2b09; +"agent": "praxis-master"; + SubagentStop hook "$CLAUDE_PROJECT_DIR"/scripts/dispatch-log-close.sh timeout 30
$ sed -n 543p DECISION_LOG.md | grep -o 'settings.json[^;]*'  ->  settings.json surgical `5ecfc80d…` (pre-existing hunks excluded
$ git diff -- scripts/dispatch-log-writeahead.sh  ->  +"# ==== BEGIN agent_type safety gate (mirrored)" ... "MUST STAY BYTE-IDENTICAL to ... scripts/dispatch-log-close.sh"
$ head scripts/dispatch-log-close.sh  ->  "SubagentStop hook: closes the DISPATCH_LOG.md write-ahead row ... Praxis_build-43n"; wc -l 340 (test file 674)
$ bd show Praxis_build-43n | head -1  ->  ○ Praxis_build-43n [BUG] · S12 v1 remediation: ... no SubagentStop closer ... [● P1 · OPEN]
$ sed -n 117p DECISION_LOG.md  ->  [2026-07-28T16:25Z] AUDIT DELIBERATELY NOT SPAWNED on `Praxis_build-43n` ... the producer returned `Result: FAIL` against itself
$ stat ... dispatch-log-close.sh / session39-dispatch-log-closer.md  ->  2026-07-28T12:46:12 / 2026-07-28T12:16:32 (local, EDT)
$ grep -c 'hook-recorded at SubagentStop' DISPATCH_LOG.md  ->  894
$ git diff -U0 -- docs/specs/2026-11-05-walk-forward-spec.md  ->  "+... **Changelog.** 2026-11-08, unit `2026-11-08-wf-spec-amendment` ..."; "+- Max drawdown ≤ 4% of equity — as imported ... Gate in force: A4 (D-2026-11-08-B)"
$ git diff -U0 -- docs/specs/2026-11-06-walk-forward-values.md  ->  "-... version 2.1" "+... version 2.2 ... unit `2026-11-08-wf-spec-amendment`"; "+- **Gate 2 "OOS Sharpe ≥ 1.0"** — RULED (A2, D-2026-11-08-B ..."
$ bd show Praxis_build-diq | head -1  ->  ○ Praxis_build-diq · PARKED: wf-spec-amendment (values spec v2.2 + WF spec A4) - audit FAIL 2, absolute park rule fired
$ sed -n 750p DECISION_LOG.md  ->  "... byte-exact evidence file `docs/reports/evidence/2026-11-09-u7-diff-of-record.patch` (sha `b06ee494…369e`) ..."
```
One-line summaries:
- settings.json: names the session agent praxis-master and registers the uncommitted closer as a SubagentStop hook. Ungraded.
- dispatch-log-writeahead.sh: adds a mirrored agent_type safety gate block. Ungraded (43n).
- dispatch-log-close.sh and its test: the 43n closer and its 674-line test. Self-FAIL, then edited after the FAIL, never audited, and live every session.
- The two specs: the values spec v2.2 and WF spec A4 amendment. diq is PARKED after FAIL 2.

Modified reports:
```
$ git diff -U0 -- "$F" | grep '^+' | grep -v '^+++' | grep -ci "$N" ; ... '^-' | grep -v '^---' ...   (F4 filing report)
added-excl-header=3 deleted-excl-header=1
$ git blame -L 393,394 HEAD -- "$F" | cut -c1-30
18d94a55 (Amear Bani-Ahmad 202
18d94a55 (Amear Bani-Ahmad 202
$ git diff -U0 -- "$F" | grep -E '^\+(#|Result)'  ->  "+## Audit (praxis-auditor, 2026-10-28T21:29:28Z)" ... "+Result: PASS"
$ (nightly) git diff -U0 | grep '^@@'  ->  @@ -1335 +1335,66 @@ ; HEAD wc -l 1335, worktree 1400; HEAD-count=4; added=0
$ sed -n 439p DECISION_LOG.md  ->  "RE-AUDIT PASS: nightly-checks review note ... The grade is at `...plan-review-rebuild.md:1335-1400`, ending `Result: PASS`"
```

DECISIONS.md, R6 and ISSUE_REGISTER (my re-checks of W6 and W5):
```
$ git diff -U0 -- DECISIONS.md | grep -E '^@@|^\+#'  ->  @@ -2279,0 +2280,92 @@ ; "+## 2026-11-12 — D-2026-11-12-B: R6 step 2 backtest engine authorised ..."
$ git show 9bf0516:DECISIONS.md | sed -n '2280,2371p' | diff - dec_added.txt  ->  "0a1 > ++ b/DECISIONS.md" (my grep artefact) and "91a93 > (blank)"
$ git branch -a --contains 9bf0516  ->  parked/Praxis_build-ckh ; remotes/origin/parked/Praxis_build-ckh
$ for f in r6-engine-entry-*.md; git show parked/Praxis_build-ckh:$f | cmp -s - $f  ->  identical-to-park-branch x5
$ echo HEAD=$(git show HEAD:ISSUE_REGISTER.md | grep -c 'de-identified 2026-11-10, D9') WT=$(grep -c ... ISSUE_REGISTER.md)
HEAD=1 WT=0
$ sed -n 912p DECISION_LOG.md | grep -o '...parity-manager row...'  ->  "the parity-manager row :468 stays out"
$ grep -n '^Result' docs/reports/2026-11-13-o4-parity-manager.md  ->  156:Result: RESULT_LINE
$ sed -n 880p | grep -o '...the 2 reports...'  ->  "temp index `/tmp/idx-o3` = HEAD `a411e17` + DECISIONS.md blob ... + the 2 reports + MANIFEST blob"
$ sed -n 919p | grep -o ...  ->  "two open-a1 reports, which stay on disk uncommitted"
```

W4 spot checks (pasted fragments):
```
616: "Excluded: `2026-11-01-csv-analyses-fix-manager-record.md` (gate artefact), root `F`, the old staged set."
622: "the manager wrote `docs/reports/2026-11-01-three-strategy-results-s2-fix-manager-record.md` to pass it ... excluded from the commit and MANIFEST."
776: "`docs/reports/2026-11-09-c7-probe-fresh-manifest-manager.md` stays out of this commit and untracked (it has no MANIFEST row; it goes to housekeeping D9)."
794: "(1) report :430 points to the c1-adversarial worker report, which stays out and untracked"
824: "Session-start drift: the 14:47Z timer run ended mid-unit with no close. ... Unit 2 (Hermes replies grading) manager ..."
```

July to August (manager-collected). Result lines:
```
session36-manifest-and-memory 310:**Result: PASS** | session36-park-rule-escalation <none> | session37-restage-audit 7:**Result: FAIL** — S1, S2, S3, S6. No commit token minted.
session37-restage-split 360:**Result: PASS** | session38-guard-evasion-test 13:**Result: PASS.** | session39-agents-dir-write-path 430:Result: PASS
session39-dispatch-log-closer 852:Result: FAIL | session40-agent-memory-disposition 563:Result: PASS | session40-cbf-audit 234:Result: FAIL
session41-c1-false-quote 235:**Result: PASS** | session48-dj2-k7-insert 6:**Result: PASS** | session53-nqcont-resolution-and-rth-corpus-read 566:**Result: PASS**
(the other 39: no Result line)
```
Beads and ledger rows:
```
y9c: ○ PARKED: restage/C1 commit composition — audit FAIL 2, absolute park rule fired [P1 OPEN]
jcw: ● [BUG] guard-evasion payload test + correct the read-only worker memory [P0 BLOCKED]
dj2: ○ k7-ratification-spec-insert [P0 OPEN]
s8g: ○ [BUG] Unguarded write path to .claude/agents/ ... [P0 OPEN]
vu8: ○ session-53 NQCONT/RTH corpus read — audited FAIL 1 on S1/S2
71: [2026-07-27T00:35Z] ... All work on the agent-key unit is HELD pending the ruling — no commit, no re-audit, no further dispatch
99: [2026-07-27T20:39Z] the praxis-auditor dispatched on `Praxis_build-jcw` RETURNED NO VERDICT
325: [2026-08-09T19:40:00Z] `dj2` IS HELD AT FAIL 1 OF 2 WITH ITS SHOT UNSPENT ... THE STOPPING DECISION IS AMEAR'S
389: [2026-08-30T19:55:00Z] ... `docs/reports/` gained **13 files** it did not write, including `…-session53-w1-q1-import-instructions.md` through `…-session53-w4-adversarial-q4-designs.md`, `…-session53-vm-checks-A-and-B.md`, `…-session53-coworker-*`, `…-session52-blank-chart-diagnosis.md` ... (3) Wrote `docs/reports/2026-08-29-session53-parallel-handoff.md` (untracked)
f3 header: "UNGRADED RESEARCH INPUT — NOT A RUBRIC ARTIFACT. ... It does NOT discharge frozen criterion F3 and must not be cited as a finding."
$ git show HEAD:AUDIT_LOG.md | wc -l  ->  100 ; AUDIT_LOG (Read) has no rows between 2026-07-26T16:51:05Z and 2026-08-04T20:41:17Z (y9c), and none after 2026-08-05 until 2026-11-06
```

## Name counts (step 4)
N comes from the brief's derivation; this output uses `cut -d- -f5`, which gives the same value. Every dirty path, with `[rep]` substituted. 126 are zero and 19 are non-zero:
```
$ { git diff --name-only; git status --porcelain --untracked-files=all | grep '^??' | cut -c4- | grep -v '2026-11-14-'; } | while read f; do printf '%s %s\n' "$(grep -ci "$N" "$f")" "$f"; done | sed "s/$N/[rep]/Ig"   (non-zero lines)
7 DECISION_LOG.md | 3 HANDOFF.md | 2 MANIFEST.md | 23 docs/reports/2026-10-28-f4-[rep]-reply-filing.md | 4 docs/reports/2026-10-28-nightly-checks-plan-review-rebuild.md
6 ...-f4-[rep]-reply-adversarial-addendum.md | 7 ...-adversarial-confirm.md | 6 ...-adversarial-final.md | 4 ...-adversarial-recheck.md | 9 ...-adversarial-transcript.md
10 ...-f4-[rep]-reply-worker1.md | 19 ...-worker3.md | 5 ...-worker5-fix.md | 2 ...-worker7-fix.md | 6 ...-worker9-fix.md
1 docs/reports/2026-11-10-scrub-forward-c1-adversarial.md | 14 docs/reports/2026-11-11-hermes-replies-grading-worker1.md | 2 docs/reports/2026-11-11-hermes-replies-grading-worker4.md | 1 docs/reports/2026-11-13-open-a2-worker1.md
$ grep -c '^0 ' counts2.txt ; grep -v '^0 ' counts2.txt | wc -l
126
19
```
Name count in the added lines only (`grep '^+' | grep -v '^+++'`) is 0 for DECISION_LOG, HANDOFF, MANIFEST, DISPATCH_LOG, STATUS, DECISIONS, ISSUE_REGISTER and the nightly report, and 3 for the F4 filing report. `grep -ciw` (whole word) gives the same or one or two lower; for example `ci=19 ciw=17` on f4 worker3.

Gaps in bead c2w: it does not list the nightly report (4 in committed lines), scrub-forward-c1-adversarial (1), hermes-replies-grading-worker1 (14) or -worker4 (2), or the 10 rep-named F4 reports by content.

## Full path lists
(Path prefix `docs/reports/` unless shown. Every path is untracked unless marked M for modified.)

- **T1 to T5 (M):** .claude/settings.json; scripts/dispatch-log-writeahead.sh; docs/specs/2026-11-05-walk-forward-spec.md; docs/specs/2026-11-06-walk-forward-values.md; 2026-10-28-f4-[rep]-reply-filing.md; 2026-10-28-nightly-checks-plan-review-rebuild.md
- **T6 to T17 (M):** AUDIT_LOG.md; DECISIONS.md; DECISION_LOG.md; DISPATCH_LOG.md; HANDOFF.md; STATUS.md; MANIFEST.md; ISSUE_REGISTER.md
- **T18:** the staged evidence PNG for the F4 reply
- **U1:** 2026-07-26-session36-manifest-and-memory.md; 2026-07-27-session36-park-rule-escalation.md
- **U2:** 2026-07-27-session37-restage-audit.md; 2026-07-27-session37-restage-split.md
- **U3:** 2026-07-27-session38-guard-evasion-test.md
- **U4:** 2026-07-28-session39-agents-dir-write-path.md
- **U5:**
  - reports: 2026-07-28-session39-closer-negative-tests.md; 2026-07-28-session39-dispatch-log-closer-adversarial.md; 2026-07-28-session39-dispatch-log-closer-build.md; 2026-07-28-session39-dispatch-log-closer.md; 2026-07-28-session39-live-vs-piped-attack.md
  - code: scripts/dispatch-log-close.sh; scripts/tests/test-dispatch-log-close.sh
- **U6:** 2026-07-28-session40-agent-memory-disposition.md; 2026-07-28-session40-cbf-audit.md; 2026-07-28-session40-ignore-and-citation-adversarial.md; 2026-07-28-session40-memory-correction-adversarial.md
- **U7:** 2026-07-30-session41-cyd-audit.md; 2026-07-30-session41-cyd-four-hook-claim.md; 2026-07-30-session41-cyd-worker1-hook-experiment.md; 2026-07-30-session41-cyd-worker2-adversarial.md; 2026-08-03-session41-cyd-fix-adversarial.md; 2026-08-03-session41-cyd-fix-audit.md; 2026-08-03-session41-cyd-fix-worker1.md; 2026-08-03-session41-cyd-fix.md
- **U8:** 2026-08-04-session41-c1-citation-markers.md; 2026-08-04-session41-c1-false-quote.md; 2026-08-04-session41-c1-marker-worker1.md
- **U9:** 2026-08-06-facts-pack.md; 2026-08-06-praxis-assessment.md; 2026-08-06-subreport-agent-memory.md
- **U10:** 2026-08-07-f3-fill-resolution-research-UNGRADED.md
- **U11:** 2026-08-09-session48-dj2-k7-insert-rescoped.md; 2026-08-09-session48-dj2-k7-insert.md; 2026-08-09-session48-dj2-rescoped-audit.md; 2026-08-09-session48-dj2-w1-report.md; 2026-08-09-session48-dj2-w2-adversarial.md; 2026-08-09-session49-dj2-s1-repair.md
- **U12:**
  - session 52: 2026-08-29-session52-blank-chart-diagnosis.md; -session52-compile-verification-correction.md; -session52-handoff-planning-chat.md; -session52-nqcont-continuous-instrument-investigation.md; -session52-nt8-voice-walkthrough.md
  - session 53: -session53-coworker-brief-continuous-series.md; -session53-coworker-halt-and-preserve.md; -session53-coworker-revised-capture-and-retry.md; -session53-nqcont-resolution-and-rth-corpus-read.md; -session53-vm-checks-A-and-B.md; -session53-w1-q1-import-instructions.md; -session53-w2-q2-nqcont-definition.md; -session53-w3-q3-rth-timezone.md; -session53-w4-adversarial-q4-designs.md
  - all prefixed 2026-08-29
- **U13:** 2026-08-29-session53-parallel-handoff.md
- **U14:** 2026-10-28-f4-[rep]-reply-adversarial-addendum.md; -adversarial-confirm.md; -adversarial-final.md; -adversarial-recheck.md; -adversarial-transcript.md; -worker1.md; -worker3.md; -worker5-fix.md; -worker7-fix.md; -worker9-fix.md (all prefixed 2026-10-28-f4-[rep]-reply)
- **U15:** 2026-11-08-wf-spec-amendment-manager.md; 2026-11-08-wf-spec-amendment-correction-1-manager.md; -correction-2-manager.md; -correction-3-manager.md; 2026-11-09-wf-spec-amendment-resume-manager.md; evidence/2026-11-09-u7-diff-of-record.patch
- **U16:** 2026-11-10-scrub-forward-c1-adversarial.md
- **U17:** 2026-11-11-hermes-replies-grading-manager.md; -worker1.md; -worker2.md; -worker4.md; -worker6.md
- **U18:** 2026-10-26-nightly-spec-request-review.md; 2026-10-28-review-note-delivery.md; 2026-10-31-voice-handoff-future-row-walkthrough.md; 2026-11-01-csv-analyses-fix-manager-record.md; 2026-11-01-three-strategy-results-s2-fix-manager-record.md; 2026-11-09-c7-probe-fresh-manifest-manager.md
- **U19:** vm/replies/20261110T214542Z-STATUS.md; vm/replies/20261110T214834Z-self-report.md; vm/replies/20261110T215014Z-STATUS.md; vm/replies/20261110T224920Z-2b-skill-job.md
- **U20:** 2026-11-12-o3-block1-scope-manager.md; 2026-11-12-o3-block1-scope-worker1.md
- **U21:** 2026-11-12-o3-block1-scope-correction-1-manager.md; -correction-1-worker1.md; -correction-2-manager.md; -correction-2-worker2.md; 2026-11-12-o3-block1-scope-evidence.md
- **U22:** 2026-11-13-o3-cure3-manager.md; 2026-11-13-o3-cure3-worker1.md
- **U23:** 2026-11-12-r6-engine-entry-manager.md; -worker1.md; -worker2.md; -correction-1-manager.md; -correction-1-worker1.md
- **U24:** 2026-11-13-o4-parity-manager.md
- **U25:** 2026-11-13-o4-parity-worker1.md; -o4-parity-worker2.md; -o4-parity-worker3.md; -o4-parity-worker4.md; -o4-reduce-manager.md; -o4-reduce-worker1.md; -o4-reduce2-manager.md; -o4-reduce2-worker1.md; -o4-repoint-manager.md; -o4-repoint-worker1.md; -o4-cure1-manager.md; -o4-cure1-worker1.md
- **U26:** 2026-11-13-open-a1-manager.md; 2026-11-13-open-a1-worker1.md
- **U27:** 2026-11-13-open-a1-cure-worker1.md
- **U28:** 2026-11-13-open-a2-worker1.md
- **X (excluded):** 2026-11-13-strategy-review-index-manager.md and -worker1..7; 2026-11-13-voice-handoff-strategy-review.md; 2026-11-13-hermes-handoff-strategy-search.md; 2026-11-13-research-filing-manager.md; -resume-worker1.md; -resume-worker2.md; -cure-manager.md; -cure-worker1.md; all 2026-11-14-* files

## Adversarial findings (W7 against C1-C17; I re-checked the ones I folded in)
- **C10 REFUTED.** My first count of 4 name hits in the F4 report's added lines included the `+++` path header. The true count is 3 (re-run above: `added-excl-header=3`). The working tree also deletes the two lines that 18d94a5 added (blame above). Filing the working copy would undo D9 work. Corrected in T4.
- **C3 PARTLY.**
  - Rows 109 and 119 record commits on side branches (c16f85f, bf6fcc7), not on main.
  - Rows 112 and 113 hold two PASS hashes for one index; W7 infers from the hashes that row 112 covers a diff that was never committed.
  - This supports T7 = UNCLEAR.
- **C5 PARTLY.** Row 13:42:23Z was written at spawn, not after the audit. The class stays U. The reason is that the flush that would carry these rows (gfx) is parked.
- **C8 PARTLY.** The closer was edited after its FAIL report (mtimes above), so the current closer has no verdict at all. It is live (894 SubagentStop rows).
- **C14 PARTLY.** The seat-close row counts 13 foreign files, but 14 session 52/53 files are untracked. Which file is the extra one is UNVERIFIED. Class U is unchanged.
- **C16 PARTLY.** Only 2 session-36 files are dirty; the other 6 are committed clean. The path list was already 2.
- **C1, C2, C4, C6, C7, C9, C11, C12, C13, C15, C17 CONFIRMED.**
  - C2 gap: ISSUE_REGISTER's 3 added entries (in T17).
  - C4 gap: pushed commits 9bf653a and 661e073 cite DECISION_LOG rows that exist only in the uncommitted, gfx-parked working tree.
- My own cross-checks of W4, W5 and W6, all pasted above: DECISION_LOG :616, :622, :776, :794, :824, :880, :886, :912, :919; R6 cmp x5; ISSUE_REGISTER token HEAD=1 WT=0; DECISIONS block against 9bf0516.
- Two conflicts settled by the manager, by rule and with no criterion softened:
  - T7 is U, not W6's CF.
  - T16 and M3's manager and worker1 rows are U, not CNA.
  - U21 is CNA, where W5 had U. The literal rule applies, the same as O4's U25.

## S6 cross-block check
This unit approves no deviation, so S6 has no deviation to test. Cross-unit hazards seen while sorting, for the master:
1. gate-manager-output.sh grades the newest report in docs/reports across all units. Concurrent managers block one another's Stop on files they may not touch. This happened to me twice, on the evening-rulings worker 5 and worker 6 files.
2. Nine dirty files share mtime 2026-11-13T12:37:18 local (17:37:18Z), 2 seconds before 661e073. An mtime-against-PASS test tells us nothing for them (W6, W7).
3. An uncommitted, unaudited SubagentStop hook (the 43n closer) writes DISPATCH_LOG rows in every session, including this one. Rows under audit are produced by ungraded code. It falls under guard work frozen at DECISION_LOG :165.
4. Two working-tree files lack D9 edits that HEAD carries: ISSUE_REGISTER :63 and the F4 filing report's 2 deleted lines. Any filing from the working tree rolls them back. Build blobs from HEAD plus hunks, never from the file.
5. Two pushed commits (9bf653a, 661e073) cite DECISION_LOG rows that only the parked gfx flush would commit.

## Questions that belong to Amear (S8, not answered here)
1. ckh: resume or leave parked? This covers T8, M2 and U23, all byte-identical on parked/Praxis_build-ckh.
2. diq: resume or leave parked? This covers T3, M1 and U15.
3. gfx: the human resume of the parked close flush (T9 to T12). This also decides T10's two rows.
4. The live, unverdicted closer hook (T1, T2, U5): keep it registered, or not? This is guard work under the 2026-08-06 freeze.
5. c2w: how to treat the name-bearing files. This covers U14, U16, U17, U28, T4, T5 and T18, plus the four files listed under the gaps in bead c2w.
6. dj2: the stop decision is already his (DECISION_LOG :325).

These are the master's under D1, not Amear's: whether to file CNA items, and whether to lift its own exclusions (:616, :622, :776, :883, :886, :897, :912, :913, :915, :919, :925).

## Files staged
None. This unit wrote only its own reports: -manager.md, -worker4.md, -worker5.md, -worker6.md and -worker7.md. All are untracked. The real index is unchanged at one path: the staged evidence PNG for the F4 reply.

Name check on every report of this unit, and the index:
```
$ for f in docs/reports/2026-11-14-dirty-tree-sort-*.md; do echo "$(grep -ci "$N" "$f") $f"; done; git diff --cached --name-only | wc -l
0 docs/reports/2026-11-14-dirty-tree-sort-manager.md
0 docs/reports/2026-11-14-dirty-tree-sort-worker4.md
0 docs/reports/2026-11-14-dirty-tree-sort-worker5.md
0 docs/reports/2026-11-14-dirty-tree-sort-worker6.md
0 docs/reports/2026-11-14-dirty-tree-sort-worker7.md
       1
```

Result: PASS

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
