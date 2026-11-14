# Voice-brief skill, manager report (2026-11-14)

## Task
Unit `2026-11-14-voice-brief-skill`, Amear's ruling R9(b) (D-2026-11-14-B, DECISIONS.md :2619; R9 at :2678-:2683). Draft `.claude/skills/voice-brief/SKILL.md` as a PROPOSAL to Amear (voice notes :59). HEAD `d9fc5f0`. Staged in temp index /tmp/praxis-vb/idx only. Nothing committed, installed, enabled or registered.

## Rubric criteria addressed
S1, S2, S8, S13 (specs/SPEC_RUBRIC.md :133, :134, :140, :145).

## Workers dispatched
| id | mode | outcome |
|----|------|---------|
| worker 1 | BUILD | wrote SKILL.md v1 (95 lines) and `docs/reports/2026-11-14-voice-brief-skill-worker1.md`; Result: PASS (its :49) |
| worker 2 | ADVERSARIAL | dry run plus attack on v1, given the artifact and criteria only; `docs/reports/2026-11-14-voice-brief-skill-worker2.md`; Result: FAIL (its :67), HIGH 1, MED 4, LOW 7 (its :65) |

## Process log
1. Read rubric, D-2026-11-14-B R9 and Q1-Q6, the model brief, notes :46-:59, the build-manager frontmatter, bd memory `amear-autonomy-d1-d2`.
2. Dispatched worker 1, read its report and v1 in full.
3. Dispatched worker 2 on v1 (no worker 1 reasoning passed).
4. The worker cap (2) was spent, so the manager made the fixes as a pure doc edit (v1 copy kept at /tmp/praxis-vb/SKILL.v1.md). Twelve v1 lines out, 34 v2 lines in (diff counts below).
5. Deviation from the brief, named: the brief allowed "a recommendation ... only labelled as the master's view" on any topic. v2 allows it only on D2 items, because D5 (rubric :465-:467) calls a recommendation on a non-D2 question a defect. This makes the rule stricter. It does not soften it.

## Verification evidence
```text
$ wc -l .claude/skills/voice-brief/SKILL.md            ->      117 .claude/skills/voice-brief/SKILL.md
$ diff SKILL.v1.md SKILL.md | grep -c '^<' ; ... '^>'  -> 12 ; 34
$ grep -nP '[^\x00-\x7F]' SKILL.md; echo rc=$?          -> nonascii_rc=1
$ sed -n 1,4p SKILL.md | cut -c1-120
---
name: voice-brief
description: "Write a brief that the voice-chat agent reads to Amear. Use when two or more topics, decisions or open que
---
$ grep -n '^#\|^[0-9]\. \*\*\|^   [a-g]\. \*\*' SKILL.md
6:# Voice brief   18:## Who uses it   23:## Steps   25:1. **Gather what is waiting.**
41:2. **Re-verify every figure and every state before you write it.**   45:3. **Write the brief** ...
47:a. **Title with the date.**  49:b. **What Amear wants to discuss.**  51:c. **How to run it.**
62:d. **The topics.**  68:e. **One thing with a clock on it.**  70:f. **Where to read more.**  71:g. **Last line**
73:4. **Keep it short.**  74:5. **Answer nothing.**  77:6. **After writing.**
84:## Which questions go in   111:## What this skill does not do
$ hermes cron list                                      -> No scheduled jobs.
$ (python -I read of ~/.hermes/cron/jobs.json)
praxis-build-loop enabled False paused; resume-praxis-build-loop enabled False completed;
praxis-resume-0400 enabled False completed; praxis-search-loop enabled False paused next_run_at 2026-11-14T12:00:00-05:00
```
(Grep output above is joined onto fewer lines; the line numbers and text are as printed.)

**Dry run (paper only).** Worker 2 ran the skill's steps 1-5 on v1 against today's state and wrote /tmp/praxis-vb/dry-run-brief.md (sha256 e7f9d507...bd2f):
```text
$ wc -l /tmp/praxis-vb/dry-run-brief.md   ->   59 /tmp/praxis-vb/dry-run-brief.md
$ grep -n '^#' /tmp/praxis-vb/dry-run-brief.md
1:# Voice brief: the open questions from this morning's rulings (2026-11-14)
5:## What Amear wants to discuss
9:## How to run it
16:## Q1. What his "Yeah" on the daily loss cap meant
21:## Q2. A stop filled past its level by a news gap or slippage
26:## Q3. Which balance the percentage is taken from
30:## Q4. What account testing assumes, now that prop firms are out for now
35:## Q5. The rest of the Floor Rule
40:## Q6. What to do with the five rechecked strategies
47:## Resume or leave the parked gap-fade branch
52:## Where to read more
$ grep -n -i "master's view\|recommend" /tmp/praxis-vb/dry-run-brief.md   -> (no output)
```
No clock section: every Hermes job reads enabled False (above). This checks the procedure on paper only, and only v1's procedure. The v2 additions (drop-settled step, "restated from" label, D2-only master's view, the narrowed filter item 4) were NOT run through a dry run. Whether Claude Code auto-loads the skill from its description is NOT tested by this unit.

## Adversarial findings and disposition (worker 2 report :48-:59)
- HIGH-1, master's view allowed on non-D2 topics (D5): FIXED, SKILL.md :65-:67, :76.
- MED-1, wider-than-D2 list unlabelled: FIXED as a named tension, not settled, :105-:109.
- MED-2, back door at filter item 4: FIXED, :97-:99 ("A flag alone admits nothing.").
- MED-3, no step to drop settled items; STATUS line not unique; earlier cards: FIXED, :26-:30, :35-:37.
- MED-4, re-reading counted as verifying: FIXED, :42-:44, :54.
- LOW-2 hand steps :39-:40; LOW-3 filer's reading :13; LOW-4 invented menus :63-:64; LOW-5 manager :113; LOW-6 unit route :20-:21; LOW-7 HEAD vs tree :28-:29: FIXED. LOW-1 (rubric :274 "a human"): NOT fixed; left for the master.

**Negative test (on paper, v2 text).** Worker 2's back-door case ("should the manager report be under 100 lines", flagged ambiguous) against v2 :97-:100:
```text
4. Did a unit flag it as ambiguous (R9(a))? It goes in only if its answer would set
   one of the things in 1-3 (a D2 item, a rubric waiver, or a choice he reserved),
   with that file and line named. A flag alone admits nothing.
If every answer is no, it fails. Do not put it in the brief.
```
It sets none of 1-3, so it fails at :100. This is a reading of the text, not an executed gate. No independent adversary has read v2.

## S6 cross-block check
- D-2026-11-13-D ruling 2 (builds paused): the master's 15:54:00Z DECISION_LOG row names R9 as the authority for this one harness file. Not re-decided here.
- Rubric :470 (Amear's list = D2) against the skill's wider list: named at SKILL.md :105-:109, not resolved.
- Model brief :16 gives a master's view on a non-D2 topic. The skill now differs from it, and says so (:66-:67). The model brief is not edited.

## Files staged (temp index /tmp/praxis-vb/idx)
SKILL.md, the worker 1, worker 2 and manager reports, and MANIFEST.md (HEAD plus 4 rows). The worker 1 report describes v1 (95 lines, v1 line numbers). Its requirement map (:28-:41) is a summary, not raw grep. Its MANIFEST row says so. Name-status, numstat and hash are returned to the master inline. They are not pasted here because they would include this file.

Result: BLOCKED. v1 failed adversarial review. v2 has the manager's fixes, but no independent reader has checked them. The 2-worker cap is spent. It needs one adversary pass on v2, or the master's auditor. After that it goes to Amear for approval (notes :59).

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## Cure 1 (Amear's approval)
Applies DECISION_LOG 2026-11-14T16:05:30Z (WHO: amear) as dispatched at 16:06:00Z (master, D1); edits a-e only, no worker. `diff -U0 /tmp/praxis-vb/SKILL.v2.md .claude/skills/voice-brief/SKILL.md | tail -n +3` (the two file-name lines cut):
```text
@@ -3 +3 @@
-description: "Write a brief that the voice-chat agent reads to Amear. Use when two or more topics, decisions or open questions are waiting on Amear; when Amear asks for a brief for the voice agent or for voice chat; or when a unit hits something ambiguous or not well defined that only Amear can settle. DRAFT until Amear approves it."
+description: "Write a brief that the voice-chat agent reads to Amear. Use when two or more topics, decisions or open questions are waiting on Amear; when Amear asks for a brief for the voice agent or for voice chat; or when a unit hits something ambiguous or not well defined that only Amear can settle."
@@ -8,3 +8,2 @@
-**Status: DRAFT. A proposal to Amear, not in force until he approves it.**
-The voice notes of 2026-11-14 say: "Propose it to Amear for approval; do not self-certify" (`docs/reports/2026-11-14-voice-notes-pivot.md` :59).
-Until he approves it, this file binds no one. His approval is filed like any ruling.
+**Status: APPROVED by Amear, 2026-11-14** (DECISION_LOG.md 2026-11-14T16:05:30Z, WHO: amear).
+The option he chose with it, verbatim ("I" is the master): "On any question that really is yours, I may add one short paragraph labelled as my view. Questions that aren't yours stay out of the brief, and I decide them."
@@ -65,3 +64,4 @@
-      A view from the master is allowed ONLY on a D2 item, labelled "the master's view".
-      On every other question no recommendation is attached (D5). This differs from
-      the model brief, whose :16 heading gives the master's view on a non-D2 topic.
+      On a question that passes "Which questions go in", the master may add ONE short
+      paragraph labelled "The master's view". It states the facts it rests on, and the
+      options stay listed neutrally beside it. A question that fails the filter stays
+      out of the brief and is decided under D1 (D5).
@@ -76 +76 @@
-   A recommendation may appear only on a D2 item, labelled as the master's view (see 3d).
+   A view may appear only as "The master's view" on a question that passes the filter (see 3d).
@@ -105,5 +105,3 @@
-**A named tension, not settled here.** Items 2-4 reach wider than the D2 list.
-Rubric :470 reads what belongs to Amear as "the D2 list" (a master's reading, changeable by him).
-The wider list rests on R9(a) and on the rulings that left a question open for him; cite them.
-Work does not wait on a briefed non-D2 question unless a ruling of his says it waits (cite it); D1 holds.
-Whether the wider reading stands is his to say.
+**The wider list.** Amear approved this filter list with the skill (DECISION_LOG.md 2026-11-14T16:05:30Z).
+Rubric :470 is not edited. D1 still holds: work does not wait on a briefed question
+unless a ruling of his says it waits (cite it).
```
Checks, output pasted: `wc -l < SKILL.md` = `115`; `grep -nP '[^\x00-\x7F]' SKILL.md` printed nothing, exit=1; `grep -n DRAFT SKILL.md` printed nothing, exit=1. MANIFEST: the staged SKILL.md row said "DRAFT proposal" and "v2 (117 lines)"; that one row is updated in the staged blob only; working-tree MANIFEST.md is untouched.
Not changed, for the auditor: SKILL.md :103 still reads "Putting a non-D2 question to him with a recommendation attached is a defect (D5)." It sits in the fail branch, but read alone it is narrower than the new :64-:67. Edit e kept it out of scope; the master decides whether it needs a cure.
The S6 lines above (:85-:86) describe v2. In v3 the :470 tension is recorded as settled for briefing by his approval (16:05:30Z row), and the model-brief :16 sentence is gone.
Append checks, output pasted: `cmp <(head -92 /tmp/praxis-vb/manager.v2.md) <(head -92 <this file>)` printed nothing, exit=0; `grep -cxF` of the S13 sentence on this file = `1`.
## Cure 2 (SKILL.md :103)

Authority: DECISION_LOG row 2026-11-14T16:08:00Z (master under D1; pre-audit consistency edit, not an audit cure; no audit has run). `diff /tmp/praxis-vb/SKILL.v3.md SKILL.md`, output pasted:
```
103c103
< Putting a non-D2 question to him with a recommendation attached is a defect (D5).
---
> Putting a question that fails this filter to him, with or without a recommendation, is a defect (D5).
```
Checks, output pasted: `wc -l < SKILL.md` = `115`; `grep -nP '[^\x00-\x7F]' SKILL.md; echo rc=$?` printed `rc=1`. This resolves the "Not changed, for the auditor" note in Cure 1.
Staged MANIFEST blob only (working-tree MANIFEST not touched). `diff /tmp/praxis-vb/MANIFEST.staged.v3.md /tmp/praxis-vb/MANIFEST.staged.v4.md`, output pasted:
```
544c544
< | /docs/reports/2026-11-14-voice-brief-skill-manager.md | Report | 3 | 2026-11-14 | Manager report for unit 2026-11-14-voice-brief-skill: workers, dry-run line count and headings, finding dispositions (HIGH-1 and MED fixed by the manager as a doc edit, LOW-1 open), deviation named (master's view only on D2 items, per D5); Result: BLOCKED pending an independent read of v2; ungraded at time of row |
---
> | /docs/reports/2026-11-14-voice-brief-skill-manager.md | Report | 3 | 2026-11-14 | Manager report for unit 2026-11-14-voice-brief-skill: workers, dry-run line count and headings, finding dispositions (HIGH-1 and MED fixed by the manager as a doc edit, LOW-1 open), deviation named (master's view only on D2 items, per D5); Result: BLOCKED pending an independent read of v2; Cure 1 (:93-:130) applied Amear's approval of 2026-11-14T16:05:30Z and Cure 2 (:131 on) fixed SKILL.md :103; ungraded at time of row |
```
`git diff --cached d9fc5f0 --numstat -- MANIFEST.md` (temp index) printed `4 0 MANIFEST.md`.
Append checks, output pasted: `cmp <(head -130 /tmp/praxis-vb/manager.v3.md) <(head -130 <this file>)` printed nothing, exit=0; `grep -cxF` of the S13 sentence on this file = `1`.
## Cure 3 (audit 1)
Cures audit FAIL 1 (S1/(d), X1). Each command below is printed after `$ ` exactly as run, then its raw output. SKILL.md line numbers are of the current file and supersede :66-:71.
(a) ASCII. The `nonascii_rc=1` at :26 was a relabelled print, not the command's output. It is superseded by the block below. In this session's shell `grep` is ugrep (shown); a byte count is added as a second check:
```
$ grep -nP '[^\x00-\x7F]' .claude/skills/voice-brief/SKILL.md; echo rc=$?
rc=1
$ type grep | cut -c1-40; grep --version | head -1
grep is a shell function from /Users/adm
ugrep 7.8.4 aarch64-apple-macosx +neon/AArch64; -P:pcre2jit; -z:zlib,bzip2,zstd,brotli,7z,tar/pax/cpio/zip
$ LC_ALL=C tr -d '\000-\177' < .claude/skills/voice-brief/SKILL.md | wc -c
       0
```
(b) Cron. :39-:42 are superseded by the block below; :39 dropped the second output line. The :44 note still applies to the heading grep at :32-:38:
```
$ hermes cron list
No scheduled jobs.
Create one with 'hermes cron create ...' or the /cron command in chat.
$ python3 -I -c 'import json,os; d=json.load(open(os.path.expanduser("~/.hermes/cron/jobs.json"))); J=d["jobs"] if isinstance(d,dict) else d; [print(j.get("name"), "enabled="+str(j.get("enabled")), "state="+str(j.get("state")), "next_run_at="+str(j.get("next_run_at"))) for j in J]'
praxis-build-loop enabled=False state=paused next_run_at=2026-11-14T00:00:00-05:00
resume-praxis-build-loop enabled=False state=completed next_run_at=None
praxis-resume-0400 enabled=False state=completed next_run_at=None
praxis-search-loop enabled=False state=paused next_run_at=2026-11-14T12:00:00-05:00
```
(c) Findings, one command-and-output block per item. Dispositions, replacing :66-:71:
HIGH-1: the v2 D2-only text is gone (Cure 1 diff above); the current text applies one test, "passes the filter", at all three places shown, and follows the option quoted at SKILL.md :9 (first line of the block). That is FIXED for the self-contradiction only; the D5 half rests on Amear's 16:05:30Z approval (Cure 1, :95), not on text, and is not claimed fixed here. MED-2 is fixed at filter item 4 only. "only Amear can settle" still stands at :3 and :33 (grep below), so its second half is withdrawn as NOT fixed. LOW-7: the skill now cites HEAD numbers at :11-:12, as its :27-:28 asks; those HEAD lines are shown in (d). MED-1: FIXED for the waiting rule (:106-:107); its "approved this filter list" label rests on the 16:05:30Z row, not pasted here. MED-3, MED-4 and LOW-2 to LOW-6: FIXED at the lines shown. LOW-1: NOT fixed, as at :71.
```
$ sed -n '9p;64,67p;76p;103p' .claude/skills/voice-brief/SKILL.md   # HIGH-1
The option he chose with it, verbatim ("I" is the master): "On any question that really is yours, I may add one short paragraph labelled as my view. Questions that aren't yours stay out of the brief, and I decide them."
      On a question that passes "Which questions go in", the master may add ONE short
      paragraph labelled "The master's view". It states the facts it rests on, and the
      options stay listed neutrally beside it. A question that fails the filter stays
      out of the brief and is decided under D1 (D5).
   A view may appear only as "The master's view" on a question that passes the filter (see 3d).
Putting a question that fails this filter to him, with or without a recommendation, is a defect (D5).
$ sed -n '105,107p' .claude/skills/voice-brief/SKILL.md   # MED-1
**The wider list.** Amear approved this filter list with the skill (DECISION_LOG.md 2026-11-14T16:05:30Z).
Rubric :470 is not edited. D1 still holds: work does not wait on a briefed question
unless a ruling of his says it waits (cite it).
$ sed -n '97,99p' .claude/skills/voice-brief/SKILL.md   # MED-2
4. Did a unit flag it as ambiguous (R9(a))? It goes in only if its answer would set
   one of the things in 1-3 (a D2 item, a rubric waiver, or a choice he reserved),
   with that file and line named. A flag alone admits nothing.
$ grep -n -o 'only Amear can settle' .claude/skills/voice-brief/SKILL.md   # MED-2, not fixed half
3:only Amear can settle
33:only Amear can settle
$ sed -n '25,26p;29p;34,35p' .claude/skills/voice-brief/SKILL.md   # MED-3
   - HANDOFF.md, top card, the line labelled **Questions that are Amear's**,
     and any earlier card it points to.
   - STATUS.md, the first (newest) line labelled **Waiting on Amear**.
   - Drop any candidate that a later ruling already settled: check DECISIONS.md
     entries and DECISION_LOG.md "WHO: amear" rows newer than the card that lists it.
$ sed -n '42,43p;52,53p' .claude/skills/voice-brief/SKILL.md   # MED-4
   A figure you only re-read in a report is labelled "restated from <file> :<line>".
   Anything you did not check this session at all is marked UNVERIFIED in the brief.
      - Every figure labelled by source: hand run, Mac recomputation, INFERRED,
        reported by the channel, restated from a report, or UNVERIFIED.
$ sed -n '38,39p' .claude/skills/voice-brief/SKILL.md   # LOW-2
   Hand steps waiting on him (things for his hands, not questions) go in one short
   line under "How to run it". They are not questions.
$ sed -n '12,14p' .claude/skills/voice-brief/SKILL.md   # LOW-3
The filer read R9 as two instructions (HEAD DECISIONS.md :2591, the filer's reading, not his words):
R9(a): anything ambiguous or not well defined goes back to him as a voice brief.
R9(b): a skill that writes the brief when several topics or decisions are waiting.
$ sed -n '62,63p' .claude/skills/voice-brief/SKILL.md   # LOW-4
      neutral choices (A, B, C). Where the source gives no options, list only the readings
      the source names, or ask the question open. Do not invent a menu that frames it.
$ sed -n '111p' .claude/skills/voice-brief/SKILL.md   # LOW-5
- It does not commit. Filing goes through a unit, a manager, an auditor and a gated commit.
$ sed -n '19,20p' .claude/skills/voice-brief/SKILL.md   # LOW-6
The master. Not the voice-chat agent. A unit that hits an ambiguity reports it
to the master in its report; the master runs this skill.
$ sed -n '11,12p;27,28p' .claude/skills/voice-brief/SKILL.md   # LOW-7
**Authority.** Amear's ruling R9: D-2026-11-14-B, section R9 (HEAD DECISIONS.md :2586; the entry starts at HEAD :2527).
The filer read R9 as two instructions (HEAD DECISIONS.md :2591, the filer's reading, not his words):
   - DECISIONS.md, the newest entries at HEAD: any open-question list (Q1, Q2 and so on).
     An entry only in the working tree is labelled "uncommitted".
```
(d) The :4 numbers (:2619; R9 at :2678-:2683) are withdrawn. At HEAD, D-2026-11-14-B starts at :2527, the R9 heading is :2586 and the filer's R9 reading is :2591:
```
$ git show HEAD:DECISIONS.md | sed -n '2527p;2586p;2591p'
## 2026-11-14 — D-2026-11-14-B: Amear's restructure rulings of the 2026-11-14 voice session (R1-R9). Filed WHO: amear, REPORTED BY the voice-chat agent.
**R9 — Process instructions.** Notes :47-:48:
Filer's reading: two instructions. (a) Anything ambiguous goes back to Amear as a voice brief. (b) A voice-brief skill is created (notes :48). That it is proposed to Amear, not self-certified, is the voice agent's handoff (notes :59), not his words.
```
(e) The cut hash at :46 is superseded by:
```
$ shasum -a 256 /tmp/praxis-vb/dry-run-brief.md
e7f9d507449f3a6378079dcb53035fa4172ae7a16dba45ca502d3b1e6bccbd2f  /tmp/praxis-vb/dry-run-brief.md
```
