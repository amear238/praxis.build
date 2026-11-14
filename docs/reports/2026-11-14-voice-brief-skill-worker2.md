# 2026-11-14 voice-brief skill — worker 2 (ADVERSARIAL)

## Task / Mode / Criterion
Unit `2026-11-14-voice-brief-skill`, for praxis-manager. ADVERSARIAL. Artifact: `.claude/skills/voice-brief/SKILL.md` (95 lines, HEAD `d9fc5f0`, untracked). Criteria: R9 of D-2026-11-14-B, D1/D2/D5 of D-2026-11-08-D, rubric S1, S2, S8, S13 and :470, model brief `docs/reports/2026-11-14-voice-brief-pivot.md`.

## Process log (dry run, skill steps 1-5; step 6 not done)
1. Gather. HANDOFF top card :20: `**Questions that are Amear's (listed, not answered):** resume or leave `vn4`; whether a Mac-side pre-screen is an acceptable first filter for the loop (D-2026-11-14-A draft); the earlier list in the cards below.` STATUS :9: `**Waiting on Amear:** resume or leave `vn4`; the NT8 commission set to $4.68 (hand step); earlier parked items; D2 items unchanged.` (STATUS has 10+ such lines; `grep -n 'Waiting on Amear'` hits :9, :18, :30, :38 ...). DECISIONS Q-list: `grep -n '^- \*\*Q[1-6],'` = :2687-:2692. Hermes, separately:
```
$ hermes cron list
No scheduled jobs.
jobs.json: praxis-build-loop enabled False state paused | resume-praxis-build-loop enabled False completed | praxis-resume-0400 enabled False completed | praxis-search-loop (73d67fad7ec9) enabled False state paused next_run_at 2026-11-14T12:00:00-05:00 paused_at 2026-11-14T09:49:09
```
Guesses forced: the top HANDOFF card is the 13:00Z run, written BEFORE the ~09:44 ET voice session; its "Mac-side pre-screen" question may already be settled by R5 (option C, "Screen candidates quickly in Python on the Mac", accepted, DECISIONS :2654, :2659; the same option says of D-2026-11-14-A "Amear has not ruled on it"), so I left it out on my own reading. The skill has no step for superseded items. "The earlier list in the cards below" is outside "top card". "The line" in STATUS is not unique. A paused job still shows `next_run_at` 12:00; I read it as not time-bound (enabled False).
2. Re-verify. Re-ran the R4 manager spot-check (no pycache written: `git status --porcelain | grep -c pycache` = 0):
```
BASE: n=1190 losers=712 largest=-542.40@2026-06-25 ... | OPPBAND: ... largest=-1960.90@2025-04-08 ...
FLAT1559: ... largest=-542.40@2026-06-25 | LHHM: ... largest=-555.40@2025-03-04 | GAPFADE_V2: ... largest=-472.90@2026-07-16
```
Stop logic YES/NO only re-read from the report :9-:13, not from source; marked UNVERIFIED in the brief. Skill :33 lets "re-read the cited file and line" count as verification, so a figure merely restated in a report would pass.
3-5. Wrote `/tmp/praxis-vb/dry-run-brief.md`. Options for Q3-Q6 had to be authored by me (the Q-list gives none); the commission hand step has no section to go in, so it was left out.
```
$ wc -l /tmp/praxis-vb/dry-run-brief.md
      59 /tmp/praxis-vb/dry-run-brief.md
$ grep -n '^#' /tmp/praxis-vb/dry-run-brief.md
1:# Voice brief: ... (2026-11-14)   5:## What Amear wants to discuss   9:## How to run it
16:## Q1. ...  21:## Q2. ...  26:## Q3. ...  30:## Q4. ...  35:## Q5. ...  40:## Q6. ...
47:## Resume or leave the parked gap-fade branch   52:## Where to read more
$ grep -c 'Fills are optimistic' /tmp/praxis-vb/dry-run-brief.md
1
```

## Attack
(a) Order and content: every required element is present (trigger :3; gather :24-:30; UNVERIFIED :34; sections a-g :37-:58 in model-brief order; four D2 items :49-:51; ONE notes file :46-:47; <80 lines :59; answer nothing :60; after-writing :64-:68; does-not-do :91-:95). Nothing missing.
(c) Filter negative tests (skill :79-:86):
- "Should the manager report be under 100 lines?": not D2 (:79), no waiver (:80), no ruling citation (:81), no unit flag (:83) -> FAILS at :84, D1 at :85.
- "Which temp index path to use?": same four no's -> FAILS at :84.
- Q3 "which balance R3 uses": ADMITTED at :81-:82, citation DECISIONS.md :2689.
- "Resume or leave vn4": rubric :274 says "A human resumes it", not Amear. :81 forced a guess (I admitted it).
- Back door: EXISTS at :83. Once any unit flags the 100-line question as "ambiguous" (R9(a): "if anything seems ambiguous"), :83 asks only "Name why". It sets no test that only Amear can settle it, so any non-Amear question gets in.
(e) Frontmatter, both :1-:4:
```
praxis-build-manager: ---/name: praxis-build-manager/description: "PRAXIS build orchestration. Use for ANY session ... milestones are human-gated."/---
voice-brief:          ---/name: voice-brief/description: "Write a brief that the voice-chat agent reads to Amear. Use when two or more topics ... DRAFT until Amear approves it."/---
```
Same shape (name + quoted description). No finding.

## Findings
- **HIGH-1 (:53, :61-:62 vs :87, :93; D5 at DECISIONS :1925-:1927).** :53 "If the master has a view, label it 'the master's view'" and :62 "A recommendation may appear only labelled as the master's view" apply to EVERY topic, including the non-D2 items the filter admits (Q1-Q6, waivers, R9(a)). D5: "A message to Amear that asks a question with a recommendation attached, on a non-D2 item, is a defect under D1." :87 bans this only for items that FAIL the filter, so the skill contradicts itself and D5. The model brief :16 ("The master's view: he is right ...") has the same pattern. Following the model reproduces the defect.
- **MED-1 (:72-:83 vs rubric :470, D1 :1911).** The filter admits waivers, reserved choices, left-open questions and R9(a) items. Rubric :470 reads Amear's list as "the D2 list", and D1 says "No unit waits on Amear except for D2 items". The skill does not label its wider list as a reading under R9, and does not say whether work waits on a briefed non-D2 item.
- **MED-2 (:83, back door).** See (c). "Name why" can be satisfied by anything. :83 also narrows R9(a)'s "anything" to "only he can settle", unlabelled.
- **MED-3 (:24-:26).** No step drops items that a newer ruling settled or that a stale card lists. "The line" in STATUS is not unique. The "cards below" pointer is not covered. Dry run: the top card predates R5.
- **MED-4 (:33-:34, :43-:44; S2).** Re-reading a report counts as re-verifying a figure. The label list has no "UNVERIFIED" and no "restated from a report" label, so a brief can present a restated figure as verified.
- LOW-1 (:81): a rule naming "a human" (rubric :274) is not handled.
- LOW-2 (:23-:31): hand steps on STATUS "Waiting on Amear" (NT8 commission) have no slot.
- LOW-3 (:12-:14; S2): R9(a)/(b) is the filer's reading (DECISIONS :2683 "Filer's reading: two instructions"), stated without that label.
- LOW-4 (:52): the master must write the options A/B/C where Amear's Q-list gives none. Writing the options frames the choice (S8-adjacent).
- LOW-5 (:91 vs :67-:68): the does-not-do list leaves out "the manager" from the filing chain.
- LOW-6 (:3 vs :19): the trigger includes "a unit hits something ambiguous", but :19 says "Not a unit". The route from a unit to the master is not stated.
- LOW-7 (:25): "newest entries" does not say HEAD or working tree. The working tree adds an uncommitted D-2026-11-12-B.
- No S2 overclaim found at :9, :29 or :68. Checked: notes :59 reads "Propose it to Amear for approval; do not self-certify." `hermes cron list` = "No scheduled jobs." now. DECISION_LOG :977 shows an auditor and :981 a gated commit for D-2026-11-14-B.

## Files staged
None. Written: `/tmp/praxis-vb/dry-run-brief.md` and this report. Neither is staged.

Counts: HIGH 1, MED 4, LOW 7.

Result: FAIL

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
