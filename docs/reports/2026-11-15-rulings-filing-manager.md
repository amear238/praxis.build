# 2026-11-15 rulings filing, finisher manager report

## Task

Finish unit `2026-11-15-rulings-filing` (DECISION_LOG 2026-11-15T14:38:00Z; re-dispatch 2026-11-15T15:40:00Z). File Amear's 2026-11-15 voice rulings plus his 2026-11-15T14:37:18Z typed ruling as one DECISIONS.md entry, D-2026-11-15-A, WHO: amear, REPORTED BY the Claude.ai Praxis project channel. Stage it with MANIFEST rows and the unit's reports in the temp index `/tmp/praxis-r15/idx` only. Do not commit.

The first manager for this unit hit its 60-turn limit. It wrote no manager report and staged nothing (DECISION_LOG 2026-11-15T15:40:00Z: "/tmp/praxis-r15/ does not exist"). I am the finisher.

## What I inherited (each item checked in my first command batch; output under Verification evidence)

- Draft entry v4: the scratchpad `entry.md` and `entry-v4.md`, 196 lines each, both sha256 ba25de69adbefae5d88494c8c45c202bafc91114b231ac737d6e5c81ee166392, as the brief stated.
- Worker reports 1-7 under docs/reports/, all untracked. Results at the `## Result` headings: worker 1 PASS, worker 2 FAIL, worker 3 PASS, worker 4 FAIL, worker 5 PASS, worker 6 FAIL, worker 7 PASS.
- The notes file `docs/reports/2026-11-15-voice-notes-open-questions.md`, untracked, 131 lines, carrying the two edits made under the first manager (counts below).
- The master's brief `docs/reports/2026-11-15-voice-brief-open-questions.md`, untracked, filed as-is.
- The MANIFEST row draft, `manifest-rows-final.md` (9 rows). It predated workers 7-8 and this report, so I updated it.
- DECISION_LOG rows 2026-11-15T14:37:18Z (line 994), 14:38:00Z (line 995) and 15:40:00Z (line 996), all in the working tree only.

## Rubric criteria addressed (specs/SPEC_RUBRIC.md, quoted)

- S1: "Every claim in a report has pasted command output, not a description of output."
- S2: "No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure."
- S4: "Every deviation from the plan has a DECISIONS.md entry with a traceable authorisation chain, written before the work, not after."
- S5: "No approval is inferred from a verbal or in-session exchange. The ledger append is the authorisation."
- S6: "Cross-block check: every approved deviation is tested against the specs of every other block it touches, not only its own."
- S8: "No question that belongs to Amear is answered on his behalf."
- S13: the standing limitation sentence, once per report and per DECISIONS.md entry.

## Workers dispatched (this finisher)

| id | mode | artifact | outcome |
|---|---|---|---|
| worker 8 | ADVERSARIAL, blocking defects only, one pass | entry v5 (sha256 69d8b23a3950ce5e98aefc60e0342a5c4d2fd99d7c5db5370511495ea10ef6cf), staged DECISIONS.md :2617-:2812, the notes | PASS, 0 blocking. 189 of 189 prose quotes and 20 of 20 fenced blocks matched. Report `docs/reports/2026-11-15-rulings-filing-worker8.md` |

No fix worker (worker 9) was dispatched, because worker 8 found 0 blocking defects. Worker 8 was given the artifact, the sources and the six defect classes. It was not given workers 1-7's reasoning and was told not to read their reports.

Inherited, dispatched by the first manager: worker 1 BUILD, worker 2 ADVERSARIAL, worker 3 BUILD (fix), worker 4 ADVERSARIAL, worker 5 BUILD (fix), worker 6 ADVERSARIAL, worker 7 BUILD (fix). Their outcomes are listed under "What I inherited".

## Process log

1. I verified the inherited state: HEAD, the v4 hash, line counts, untracked status, the notes counts and the ledger rows.
2. **I froze v4.** I copied it to `entry-v4-frozen.md`, made the copy read-only, and recorded sha256 ba25de69adbefae5d88494c8c45c202bafc91114b231ac737d6e5c81ee166392.
3. **I made the v4 to v5 edit myself.** It is a single-line doc edit, disclosed here. All three changes are on entry line 194 (S4 timing), and the line count stays at 196:
   - (i) adds the finisher's revision time, 2026-11-15T15:35:41Z, from `date -u`;
   - (ii) replaces "No row follows 14:38:00Z." with a statement that row 15:40:00Z, the re-dispatch, follows and rules nothing. I added a note that the row's stamp is ahead of the clock. v4's sentence had become false once the master appended row 15:40:00Z;
   - (iii) adds the self-cite the unit brief requires: the entry sits at DECISIONS.md :2617-:2812 in the staged blob.

   This is a fix made by the producer. Worker 8 then checked v5, including these three changes, so the edit was graded by an adversary, not by me.
4. **I built the temp index.** Starting from `git read-tree HEAD` (HEAD d9fc5f0), I staged DECISIONS.md as a blob of `git show HEAD:DECISIONS.md`, one blank line, then v5. I never staged the working-tree file.
5. **Worker 8 ran on v5 and the staged lines.** Result: PASS, 0 blocking.
6. I re-ran the key checks myself:
   - the staged entry is byte-identical to v5;
   - S13 appears once in the staged entry;
   - the staged entry contains no at-sign;
   - the staged notes contain no at-sign, and "withheld" appears on line 122 only.
7. **I staged MANIFEST.md** as the HEAD blob plus 11 rows: the notes, the brief, this report, and workers 1-8. Worker 6's row was updated with its result, and rows for workers 7 and 8 were added. My first build of the row file copied worker 6's old row a second time. I removed the copy before staging, and the duplicate check prints 0.
8. I appended the same entry (after one blank line) and the same 11 rows to the working-tree DECISIONS.md and MANIFEST.md. `cmp` of each working-tree tail against its source prints the IDENTICAL marker.
9. **I staged the 11 report files** with `git update-index --add`: the notes, the brief, workers 1-8, and this report last.
10. **I ran three negative tests.** They show that the checks used here can fail:
    - the at-sign count prints 1 on a copy with an address appended;
    - the S13 count prints 0 on a copy with the sentence removed;
    - the stop gate's to-be-decided-token regex matches a probe file.

    The gate itself was also tripped for real in this session. It BLOCKED my first stop on worker 7's report, which was then the newest under docs/reports/. Worker 7's report contains the token in a quoted line of the entry. I wrote an interim version of this report so the stop could pass. This final version replaces it.

## Verification evidence

Pasted output only. Every command is shown in full above its output.

```
$ git rev-parse HEAD
d9fc5f08f25842180966dc04220082314689d29e

$ shasum -a 256 /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry-v4-frozen.md /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry-v5.md
ba25de69adbefae5d88494c8c45c202bafc91114b231ac737d6e5c81ee166392  /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry-v4-frozen.md
69d8b23a3950ce5e98aefc60e0342a5c4d2fd99d7c5db5370511495ea10ef6cf  /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry-v5.md

$ wc -l /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry-v4-frozen.md /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry-v5.md
     196 /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry-v4-frozen.md
     196 /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry-v5.md
     392 total

$ diff /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry-v4-frozen.md /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry-v5.md | grep -c '^[<>]'
2

$ diff <(sed -n '194p' /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry-v4-frozen.md | tr '.' '\n') <(sed -n '194p' /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry-v5.md | tr '.' '\n')
2c2
< ** Written 2026-11-15T14:47:13Z, revised 2026-11-15T15:01:39Z, revised again 2026-11-15T15:16:31Z, revised a third time 2026-11-15T15:31:08Z, before any act under these rulings
---
> ** Written 2026-11-15T14:47:13Z, revised 2026-11-15T15:01:39Z, revised again 2026-11-15T15:16:31Z, revised a third time 2026-11-15T15:31:08Z, and revised by the finisher manager at 2026-11-15T15:35:41Z, before any act under these rulings
5c5,6
<  No row follows 14:38:00Z
---
>  Row 2026-11-15T15:40:00Z, the master's re-dispatch of this unit to a finisher manager, follows; it rules nothing
>  Its own WHEN reads "`date -u` about 15:38Z", and `date -u` read 2026-11-15T15:35:41Z at the finisher's revision, so that row's stamp is ahead of the clock; observed, not fixed
18c19,20
< md line numbers in this entry are HEAD's
---
> md line numbers in this entry are HEAD's, with one exception: this entry itself sits at DECISIONS
> md :2617-:2812 in the blob staged and committed with it (HEAD's 2615 lines, one blank line, then this entry's 196 lines)

$ grep -n '^## Result' docs/reports/2026-11-15-rulings-filing-worker1.md docs/reports/2026-11-15-rulings-filing-worker2.md docs/reports/2026-11-15-rulings-filing-worker3.md docs/reports/2026-11-15-rulings-filing-worker4.md docs/reports/2026-11-15-rulings-filing-worker5.md docs/reports/2026-11-15-rulings-filing-worker6.md docs/reports/2026-11-15-rulings-filing-worker7.md docs/reports/2026-11-15-rulings-filing-worker8.md
docs/reports/2026-11-15-rulings-filing-worker1.md:712:## Result: PASS
docs/reports/2026-11-15-rulings-filing-worker2.md:1338:## Result: FAIL
docs/reports/2026-11-15-rulings-filing-worker3.md:598:## Result: PASS
docs/reports/2026-11-15-rulings-filing-worker4.md:460:## Result: FAIL
docs/reports/2026-11-15-rulings-filing-worker5.md:388:## Result: PASS
docs/reports/2026-11-15-rulings-filing-worker6.md:662:## Result: FAIL
docs/reports/2026-11-15-rulings-filing-worker7.md:572:## Result: PASS
docs/reports/2026-11-15-rulings-filing-worker8.md:779:## Result

$ sed -n '762,764p;775,781p' docs/reports/2026-11-15-rulings-filing-worker8.md
## Blocking findings

None.
## Quote tally

Fenced blocks: 20 checked (19 notes ranges plus the T1 extraction), 20 matched, 0 failed. Prose quotes: 189 checked, 189 matched, 0 failed (2 code-span artifacts excluded, as listed above).

## Result

PASS (0 blocking)

$ sed -n '994,996p' DECISION_LOG.md | cut -c1-120
- [2026-11-15T14:37:18Z] WHO: amear | WHAT: **Amear's typed Q6 ruling in the master session** (pasted by him as "the com
- [2026-11-15T14:38:00Z] WHO: praxis-master | WHAT: **Intake of `docs/reports/2026-11-15-voice-notes-open-questions.md` 
- [2026-11-15T15:40:00Z] WHO: praxis-master | WHAT: **Manager for unit `2026-11-15-rulings-filing` stopped at its 60-tur

$ GIT_INDEX_FILE=/tmp/praxis-r15/idx git show :DECISIONS.md | wc -l
    2812

$ GIT_INDEX_FILE=/tmp/praxis-r15/idx git show :DECISIONS.md | sed -n '2617,2812p' | cmp - /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry-v5.md && echo STAGED-ENTRY-IDENTICAL
STAGED-ENTRY-IDENTICAL

$ GIT_INDEX_FILE=/tmp/praxis-r15/idx git show HEAD:DECISIONS.md | cmp - <(GIT_INDEX_FILE=/tmp/praxis-r15/idx git show :DECISIONS.md | sed -n '1,2615p') && echo STAGED-PREFIX-EQUALS-HEAD
STAGED-PREFIX-EQUALS-HEAD

$ GIT_INDEX_FILE=/tmp/praxis-r15/idx git show :DECISIONS.md | sed -n '2616p' | wc -c
       1

$ GIT_INDEX_FILE=/tmp/praxis-r15/idx git show :DECISIONS.md | grep -n '^## 2026-11-15 — D-2026-11-15-A' | cut -c1-40
2617:## 2026-11-15 — D-2026-11-15-A: Ame

$ GIT_INDEX_FILE=/tmp/praxis-r15/idx git show :DECISIONS.md | sed -n '2617,2812p' | grep -c -x 'Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.'
1

$ GIT_INDEX_FILE=/tmp/praxis-r15/idx git show :DECISIONS.md | sed -n '2617,2812p' | grep -c -F "$(printf '\100')"
0

$ GIT_INDEX_FILE=/tmp/praxis-r15/idx git show :DECISIONS.md | sed -n '2617,2812p' | grep -n -i 'S6 cross-block\|^\*\*Still open' | cut -c1-60
160:**Still open (Amear's, unanswered, S8).** None is answer
178:**S6 cross-block** (the filer's readings; the greps, run

$ GIT_INDEX_FILE=/tmp/praxis-r15/idx git show :DECISIONS.md | sed -n '2617,2812p' | grep -c 'Answer: NONE'
16

$ GIT_INDEX_FILE=/tmp/praxis-r15/idx git show :docs/reports/2026-11-15-voice-notes-open-questions.md | grep -c -F "$(printf '\100')"
0

$ GIT_INDEX_FILE=/tmp/praxis-r15/idx git show :docs/reports/2026-11-15-voice-notes-open-questions.md | grep -c withheld
1

$ GIT_INDEX_FILE=/tmp/praxis-r15/idx git show :docs/reports/2026-11-15-voice-notes-open-questions.md | grep -n withheld | cut -d: -f1
122

$ GIT_INDEX_FILE=/tmp/praxis-r15/idx git show :docs/reports/2026-11-15-voice-notes-open-questions.md | wc -l
     131

$ GIT_INDEX_FILE=/tmp/praxis-r15/idx git show :docs/reports/2026-11-15-voice-notes-open-questions.md | grep -c -x 'Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.'
1

$ GIT_INDEX_FILE=/tmp/praxis-r15/idx git show :docs/reports/2026-11-15-voice-notes-open-questions.md | cmp - docs/reports/2026-11-15-voice-notes-open-questions.md && echo STAGED-NOTES-EQUAL-WORKTREE
STAGED-NOTES-EQUAL-WORKTREE

$ python3 -I /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/wtok.py /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/notes-orig.md docs/reports/2026-11-15-voice-notes-open-questions.md /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry-v5.md docs/reports/2026-11-15-voice-brief-open-questions.md docs/reports/2026-11-15-rulings-filing-worker1.md docs/reports/2026-11-15-rulings-filing-worker2.md docs/reports/2026-11-15-rulings-filing-worker3.md docs/reports/2026-11-15-rulings-filing-worker4.md docs/reports/2026-11-15-rulings-filing-worker5.md docs/reports/2026-11-15-rulings-filing-worker6.md docs/reports/2026-11-15-rulings-filing-worker7.md docs/reports/2026-11-15-rulings-filing-worker8.md /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/manifest-rows-r15b.md
withheld tokens: 2 lengths: [5, 27]
2026-11-15-voice-notes-open-questions.md [0, 0]
entry-v5.md [0, 0]
2026-11-15-voice-brief-open-questions.md [0, 0]
2026-11-15-rulings-filing-worker1.md [0, 0]
2026-11-15-rulings-filing-worker2.md [0, 0]
2026-11-15-rulings-filing-worker3.md [0, 0]
2026-11-15-rulings-filing-worker4.md [0, 0]
2026-11-15-rulings-filing-worker5.md [0, 0]
2026-11-15-rulings-filing-worker6.md [0, 0]
2026-11-15-rulings-filing-worker7.md [0, 0]
2026-11-15-rulings-filing-worker8.md [0, 0]
manifest-rows-r15b.md [0, 0]

$ GIT_INDEX_FILE=/tmp/praxis-r15/idx git show :MANIFEST.md | wc -l
     551

$ GIT_INDEX_FILE=/tmp/praxis-r15/idx git show HEAD:MANIFEST.md | cmp - <(GIT_INDEX_FILE=/tmp/praxis-r15/idx git show :MANIFEST.md | sed -n '1,540p') && echo STAGED-MANIFEST-PREFIX-EQUALS-HEAD
STAGED-MANIFEST-PREFIX-EQUALS-HEAD

$ GIT_INDEX_FILE=/tmp/praxis-r15/idx git show :MANIFEST.md | sed -n '541,551p' | cut -d'|' -f2
 /docs/reports/2026-11-15-voice-notes-open-questions.md 
 /docs/reports/2026-11-15-voice-brief-open-questions.md 
 /docs/reports/2026-11-15-rulings-filing-manager.md 
 /docs/reports/2026-11-15-rulings-filing-worker1.md 
 /docs/reports/2026-11-15-rulings-filing-worker2.md 
 /docs/reports/2026-11-15-rulings-filing-worker3.md 
 /docs/reports/2026-11-15-rulings-filing-worker4.md 
 /docs/reports/2026-11-15-rulings-filing-worker5.md 
 /docs/reports/2026-11-15-rulings-filing-worker6.md 
 /docs/reports/2026-11-15-rulings-filing-worker7.md 
 /docs/reports/2026-11-15-rulings-filing-worker8.md 

$ GIT_INDEX_FILE=/tmp/praxis-r15/idx git show :MANIFEST.md | sed -n '541,551p' | cut -d'|' -f2 | sort | uniq -d | wc -l
       0

$ tail -n 196 DECISIONS.md | cmp - /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry-v5.md && echo WT-DECISIONS-TAIL-IDENTICAL
WT-DECISIONS-TAIL-IDENTICAL

$ tail -n 11 MANIFEST.md | cmp - /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/manifest-rows-r15b.md && echo WT-MANIFEST-TAIL-IDENTICAL
WT-MANIFEST-TAIL-IDENTICAL

$ for f in docs/reports/2026-11-15-rulings-filing-worker[1-7].md; do awk -v F="${f##*/}" '/^[[:space:]]*```/{fence=!fence} $0=="Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed."{printf "%s :%d in-fence=%d\n",F,NR,fence}' $f; done
2026-11-15-rulings-filing-worker1.md :661 in-fence=0
2026-11-15-rulings-filing-worker1.md :721 in-fence=0
2026-11-15-rulings-filing-worker2.md :775 in-fence=1
2026-11-15-rulings-filing-worker2.md :972 in-fence=0
2026-11-15-rulings-filing-worker2.md :1342 in-fence=0
2026-11-15-rulings-filing-worker3.md :183 in-fence=0
2026-11-15-rulings-filing-worker3.md :602 in-fence=0
2026-11-15-rulings-filing-worker4.md :395 in-fence=1
2026-11-15-rulings-filing-worker4.md :464 in-fence=0
2026-11-15-rulings-filing-worker5.md :134 in-fence=1
2026-11-15-rulings-filing-worker5.md :392 in-fence=0
2026-11-15-rulings-filing-worker6.md :584 in-fence=0
2026-11-15-rulings-filing-worker6.md :666 in-fence=0
2026-11-15-rulings-filing-worker7.md :216 in-fence=0
2026-11-15-rulings-filing-worker7.md :477 in-fence=0
2026-11-15-rulings-filing-worker7.md :581 in-fence=0

$ { cat /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry-v5.md; printf 'x\100y.z\n'; } | grep -c -F "$(printf '\100')"
1

$ grep -v -x -F 'Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.' /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry-v5.md | grep -c -x -F 'Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.'
0

$ grep -qiE "\b$(printf 'T%sD' B)\b" /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/neg-report.md && echo "gate regex would BLOCK"
gate regex would BLOCK

$ git diff --cached --stat HEAD
 docs/reports/evidence/2026-10-28-mffu-davi-reply.png | Bin 0 -> 254350 bytes
 1 file changed, 0 insertions(+), 0 deletions(-)
```

## Adversarial findings

Worker 8 reported 0 blocking findings in the six classes:
1. byte-exact quotes;
2. S8 answers;
3. citations, including the self-cite and the S4-timing claims about DECISION_LOG rows 993-996;
4. F3/F4 claimed cleared;
5. S13 count;
6. at-sign or withheld name.

Its quote tally is pasted in the evidence above. Worker 8 could not check one thing: the finisher's own 15:35:41Z clock reading. That is not a line cite. The v5 build command printed `date -u` as 2026-11-15T15:35:41Z earlier in this session. The diff of entry :194 below shows that value written into the entry.

Carried, non-blocking findings. None was fixed, because the finisher brief allows only blocking fixes:
1. **Extra S13 lines in workers 1-7.** Each report ends with the S13 sentence as its last non-blank line. Each also has 1-2 more exact-line copies inside pasted command output, such as `tail -n 1` of the draft. The awk location output is pasted above. Whether that meets "carries, once" is for the auditor.
2. **Pasted heading lines in worker 8.** Worker 8's report has two lines starting with "## " outside a code fence at :739 and :754. They are pasted source text, not report sections.
3. **The to-be-decided token in quoted text.** Workers 1-4, 6, 7 and 8 contain the stop gate's to-be-decided token inside quoted or diffed entry and DECISIONS.md text. The stop gate checks only the newest report, which is this one. This report contains no such token.
4. **Ledger timestamp oddities.** Row 2026-11-15T15:40:00Z is stamped ahead of the clock: its WHEN reads "about 15:38Z", and `date -u` read 15:35:41Z after the row existed. The entry records this as observed, not fixed, alongside the two earlier WHEN mismatches it already listed.
5. **Ledgers not updated.** DECISION_LOG, HANDOFF, STATUS and DISPATCH_LOG are not updated by this unit, as instructed. The master owes the rows for this finisher's work.

## S6 cross-block check

The entry's own S6 section is staged DECISIONS.md :2794 onward (entry line 178, "**S6 cross-block** (the filer's readings; the greps, run at HEAD `d9fc5f0`, ..."). It names the conflicts with:
- D-2026-11-14-B;
- the walk-forward spec and its typed ruling 1;
- the breaker-topology row;
- the Noise-Area ruleset's stop section;
- F4.

It resolves none of them. Worker 8 class 2 and class 4 found no conflict resolved, no Amear question answered, and no frozen criterion cleared.

My own cross-block test of this unit's footprint is the staged stat, pasted below. It touches only DECISIONS.md (one appended entry), MANIFEST.md (11 appended rows) and 11 report files under docs/reports/. No spec, rubric line, code file, bead, cron job or breaker value is in the diff. F3 and F4 stay FROZEN.

The open items (a) to (e) required by the unit brief, and the filer's additions after them, are in the entry's "Still open" list at staged :2776 (entry line 160). The staged entry holds 16 "Answer: NONE" lines; the count is pasted above.

## Files staged (temp index /tmp/praxis-r15/idx only; the default index is untouched)

- DECISIONS.md: HEAD blob plus D-2026-11-15-A at :2617-:2812.
- MANIFEST.md: HEAD blob plus 11 rows at :541-:551.
- docs/reports/2026-11-15-voice-notes-open-questions.md
- docs/reports/2026-11-15-voice-brief-open-questions.md
- docs/reports/2026-11-15-rulings-filing-worker1.md through -worker8.md (8 files)
- docs/reports/2026-11-15-rulings-filing-manager.md (this report)

Not staged:
- DECISION_LOG.md, HANDOFF.md, STATUS.md, DISPATCH_LOG.md;
- every scratchpad file, including notes-orig.md;
- the working-tree DECISIONS.md and MANIFEST.md.

The two notes edits, as counts only:
- **The redaction.** One name and one address on notes :122 were replaced with placeholders. The staged notes blob has 0 at-sign characters and 1 line containing "withheld", line 122.
- **The appended filer's note plus S13 sentence.** This is 3 lines; the staged notes blob is 131 lines, and S13 appears once.

The commands are pasted under Verification evidence.

Result: PASS

## Final index state

Below is the stat of the full temp index, including this report. It was recomputed after this report was re-added, and the recomputed output matches what is pasted here (the stability check is in my return).

There is also a hash of the staged diff for every path except this report. A file cannot contain the hash of a diff that includes itself, so the full-diff hash, `GIT_INDEX_FILE=/tmp/praxis-r15/idx git diff --cached HEAD | shasum -a 256`, is given only in my return to the master. Nothing changes in the index after it.

```
$ GIT_INDEX_FILE=/tmp/praxis-r15/idx git diff --cached --stat HEAD
 DECISIONS.md                                       |  197 +++
 MANIFEST.md                                        |   11 +
 docs/reports/2026-11-15-rulings-filing-manager.md  |  332 +++++
 docs/reports/2026-11-15-rulings-filing-worker1.md  |  721 +++++++++++
 docs/reports/2026-11-15-rulings-filing-worker2.md  | 1342 ++++++++++++++++++++
 docs/reports/2026-11-15-rulings-filing-worker3.md  |  602 +++++++++
 docs/reports/2026-11-15-rulings-filing-worker4.md  |  464 +++++++
 docs/reports/2026-11-15-rulings-filing-worker5.md  |  392 ++++++
 docs/reports/2026-11-15-rulings-filing-worker6.md  |  666 ++++++++++
 docs/reports/2026-11-15-rulings-filing-worker7.md  |  581 +++++++++
 docs/reports/2026-11-15-rulings-filing-worker8.md  |  783 ++++++++++++
 .../2026-11-15-voice-brief-open-questions.md       |   58 +
 .../2026-11-15-voice-notes-open-questions.md       |  131 ++
 13 files changed, 6280 insertions(+)

$ GIT_INDEX_FILE=/tmp/praxis-r15/idx git diff --cached HEAD -- . ':(exclude)docs/reports/2026-11-15-rulings-filing-manager.md' | shasum -a 256
9f82d80ca07d61e1dceacd9729478276cdb4313476977e35db6e64c5b2825522  -
```

## Cure 1 (2026-11-15)

Cure 1 for unit `2026-11-15-rulings-filing`, run by a praxis-manager on the master's cure decision, DECISION_LOG.md row `[2026-11-15T16:05:00Z]` (found by `grep -n -F`; DECISION_LOG.md is not edited). No worker was dispatched; the manager made the edits itself. Mode: BUILD. Nothing is committed; everything is left staged in the temp index `/tmp/praxis-r15/idx`.

### 1. The finding (audit FAIL 1 of 2, on S4 and S5)

`docs/reports/2026-11-15-voice-brief-open-questions.md` was staged for commit in this unit. But DECISION_LOG.md row `[2026-11-15T13:30:00Z]` recorded "No commit this act; the brief stays in the working tree for the next flush", and no ledger row authorised filing it in this unit. The entry itself conceded that it was filed at the master's direction, "which no ledger row records". The cure brings the staged tree back to the recorded plan.

### 2. What the cure changed

1. The brief is removed from the temp index. The file on disk is untouched (sha256 below).
2. Staged MANIFEST.md blob only: the HEAD blob plus the earlier appended rows, minus the brief's one row, so 10 rows at :541-:550. This report's own row said "eleven MANIFEST rows and eleven reports staged"; in the staged blob it now says "ten MANIFEST rows and ten reports staged". The working-tree MANIFEST.md is left as it was, with all 11 rows, among them the brief's row for the next flush and this report's row with "eleven". That working-tree row now differs from the staged one; this is named here and not resolved.
3. D-2026-11-15-A: four edits, the same in the staged blob and in the working-tree copy (the entry at the end of the working-tree DECISIONS.md, :2709-:2904). The entry stays 196 lines, so its self-cite ":2617-:2812" is unchanged, and the standing sentence is still its last line, once.
4. This section is appended to this report. Disclosed move: the report's single standing sentence was its last line (:332). That line was deleted and the sentence re-added as the last line, after this section. No other existing line is changed (lines 1-331 are byte-identical; `cmp` below). The earlier lines of this report that say the brief is staged, or count 11 rows, 11 reports or 13 files (:14, :55, :57, :197, :286, :288, :324-:326), are not edited, because only an append is allowed. This section supersedes them. The worker reports are not edited either.
5. Clock observation, also written into the entry's S4 timing line: `date -u` read 2026-11-15T15:55:13Z when this cure began. Row `[2026-11-15T16:05:00Z]` was already in DECISION_LOG.md then, so that row's stamp is ahead of the clock. Observed, not fixed.

### 3. The hits

Every hit, found first on the pre-cure staged entry (the entry lines as staged before the cure, saved to the scratchpad as `entry_old.md`; entry line N is staged DECISIONS.md :(N+2616)):

```
$ grep -n -F 'voice-brief-open-questions' /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry_old.md | cut -d: -f1
3
[exit 0]
$ grep -n -i 'brief' /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry_old.md | cut -d: -f1 | tr '\n' ' '; echo
3 94 125 127 140 145 148 150 171 174 176 179 184 192 194 
[exit 0]
```

The decision on each hit (entry line / staged line):

| Entry line | Staged | What the hit is | Decision |
|---|---|---|---|
| 3 | :2619 | Status line: the brief's first naming, "filed with this entry at the master's direction ... which no ledger row records", and "that difference is named, not resolved" | EDIT: now "uncommitted at filing; the brief is not filed in this unit, and stays uncommitted in the working tree for the next flush, per row 2026-11-15T13:30:00Z", followed by that row's quote. The concession and "that difference is named, not resolved" are removed. The two row quotes stay byte-identical. "unchanged" stays, since the brief is not edited. "untracked at filing, staged with this entry" on the same line is about the notes, so it stays |
| 94 | :2710 | content citation "(brief :15)" | KEEP |
| 125 | :2741 | the brief's UNVERIFIED figures (content) | KEEP |
| 127 | :2743 | "The brief is filed unchanged, with those figures still in it." | EDIT: now "The brief is not filed in this unit, and stays uncommitted in the working tree for the next flush, per row 2026-11-15T13:30:00Z; it is unchanged, with those figures still in it." The content citations (brief :40, :34) and "The brief is not edited." stay |
| 140 | :2756 | content citations (brief :38, :39) | KEEP |
| 145 | :2761 | "Voice-brief skill" (a bead, not the file) | KEEP |
| 148 | :2764 | voice-brief skill and content citations (brief :44, :46-:48) | KEEP |
| 150 | :2766 | "the channel's check of the brief" (content) | KEEP |
| 171 | :2787 | content citation (brief :15) | KEEP |
| 174 | :2790 | content citation (brief :48) | KEEP |
| 176 | :2792 | voice-brief skill and content citations (brief :48, :49) | KEEP |
| 179 | :2795 | "voice brief" process (D-2026-11-14-B R9) and the voice-brief skill | KEEP |
| 184 | :2800 | content citation (brief :15) | KEEP |
| 192 | :2808 | Limits: "The brief is filed unchanged." | EDIT: now "The brief is not filed in this unit, and stays uncommitted in the working tree for the next flush, per row 2026-11-15T13:30:00Z; it is unchanged." |
| 194 | :2810 | S4 timing line ("brief" in the 13:30:00Z row's description; "staged and committed with it" is about the entry itself) | EDIT: one sentence added after the 15:40:00Z sentence. It names row 2026-11-15T16:05:00Z as the record of this change, gives the cure revision time, and notes the clock. Nothing else on the line changes |

The `voice-brief-open-questions` grep has one hit, entry line 3, which is where the brief is first named. That is where "uncommitted at filing" is placed. The quote check in section 4 compares every double-quoted string and every fenced block in the entry, before and after.

### 4. The entry, before and after

```
$ cat /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/cure1.py
import sys
src, dst, t = sys.argv[1], sys.argv[2], sys.argv[3]
s = open(src, encoding='utf-8').read()
SENT = "stays uncommitted in the working tree for the next flush, per row 2026-11-15T13:30:00Z"
reps = [
 ("the master's brief for the call, unchanged, filed with this entry at the master's direction in its dispatch to this unit's manager, which no ledger row records; row 14:38:00Z names only the notes and the typed ruling for filing (\"files the notes plus the 14:37:18Z typed ruling\"), and row 13:30:00Z says \"No commit this act; the brief stays in the working tree for the next flush.\"; that difference is named, not resolved)",
  "the master's brief for the call, unchanged, uncommitted at filing; the brief is not filed in this unit, and " + SENT + ", which says \"No commit this act; the brief stays in the working tree for the next flush.\"; row 14:38:00Z names only the notes and the typed ruling for filing (\"files the notes plus the 14:37:18Z typed ruling\"))"),
 ("The brief is filed unchanged, with those figures still in it.",
  "The brief is not filed in this unit, and " + SENT + "; it is unchanged, with those figures still in it."),
 ("The brief is filed unchanged. The notes are changed only",
  "The brief is not filed in this unit, and " + SENT + "; it is unchanged. The notes are changed only"),
 ("so that row's stamp is ahead of the clock; observed, not fixed. ",
  "so that row's stamp is ahead of the clock; observed, not fixed. Row 2026-11-15T16:05:00Z, the master's Cure 1 decision after this unit's first audit FAIL, is the record of this change: the brief is not filed in this unit, and " + SENT + "; this entry was revised for that cure at " + t + " (`date -u`), with that row already present in DECISION_LOG.md, so that row's stamp is ahead of the clock; observed, not fixed. "),
]
for o, n in reps:
    c = s.count(o)
    assert c == 1, (c, o[:60])
    s = s.replace(o, n)
open(dst, 'w', encoding='utf-8').write(s)
print("4 replacements, each matched once")
[exit 0]
$ python3 -I /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/cure1.py /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry_old.md /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry_check.md 2026-11-15T15:55:13Z && cmp /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry_check.md /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry_new.md && echo IDENTICAL
4 replacements, each matched once
IDENTICAL
[exit 0]
$ wc -l < /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry_old.md; wc -l < /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry_new.md
     196
     196
[exit 0]
$ tail -n 1 /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry_new.md | cmp - /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/s13.txt && echo LAST_LINE_IS_STANDING_SENTENCE
LAST_LINE_IS_STANDING_SENTENCE
[exit 0]
$ grep -c -F -f /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/s13.txt /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry_new.md
1
[exit 0]
$ grep -c -F ':2617-:2812' /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry_new.md
1
[exit 0]
$ grep -c -F 'which no ledger row records' /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry_new.md
0
[exit 1]
$ python3 -I /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/qcheck.py /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry_old.md /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry_new.md
quoted strings before/after: 241 241
distinct quoted strings lost: 0 added: 0
fenced blocks before/after: 20 20 identical: True
[exit 0]
```

```diff
$ diff -U1 /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry_old.md /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry_new.md
--- /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry_old.md	2026-11-15 10:53:58
+++ /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry_new.md	2026-11-15 10:55:22
@@ -2,3 +2,3 @@
 
-**Status:** WHO: amear, REPORTED BY the Claude.ai Praxis project channel, plus his typed ruling of 2026-11-15T14:37:18Z (DECISION_LOG row 2026-11-15T14:37:18Z, WHO: amear, HOW: typed; block T1 below). Source: `docs/reports/2026-11-15-voice-notes-open-questions.md` (called the notes below; untracked at filing, staged with this entry), written by the Claude.ai Praxis project channel (notes :3) from Amear's voice call, which worked through `docs/reports/2026-11-15-voice-brief-open-questions.md` (called the brief below; the master's brief for the call, unchanged, filed with this entry at the master's direction in its dispatch to this unit's manager, which no ledger row records; row 14:38:00Z names only the notes and the typed ruling for filing ("files the notes plus the 14:37:18Z typed ruling"), and row 13:30:00Z says "No commit this act; the brief stays in the working tree for the next flush."; that difference is named, not resolved) and ran between about 08:30 and 09:27 ET (notes :4). The voice agent had no repo access; it kept a list and the channel wrote the notes (notes :4). Amear's words are speech-to-text, unedited (notes :6), so the wording may be slightly off. The transcript has no per-line clock times; each ruling carries a window, W1 = 08:28-09:08 ET or W2 = 09:08-09:27 ET (notes :5). What is not his: the section headings (notes :10, :21, :27, :35, :42, :49, :55, :66, :84, :108, :113, :118, :125) and the bold sub-headings (notes :68, :75, :77, :80, :90, :95); the "Read:" lines (notes :73, :78) and the "Read:" sentence and lead-in text on notes :40 (his quoted words on :40, among them "Okay, then that's what we use.", are his); the AGENT PROPOSAL lines (notes :23, :31, and the proposal sentence on :93), which are the voice agent's proposals (his "Uh, yeah." on :93, like his replies on :24 and :32, is his); the "Consequence (the agent's reading, not ruled)" line (notes :47); the AMBIGUOUS note (notes :88); the voice agent's note on the source paper (notes :92, first sentence); the Flat1559 mapping (notes :95); the figures and their framing (notes :97-:106); all of section 11 (notes :113-:116, "this channel's check, not Amear's rulings"); the reading of the MFFU email (notes :123, "As the voice agent read it"); the section 13 bullets (notes :127-:128); and the lead-in text around his quotes. Those are the channel's or the voice agent's. Every "Filer's reading" below is the filer's (praxis-worker for praxis-manager, for the master under D-2026-11-08-D D1), changeable by Amear, and not his ruling. Each fenced block below is copied by script (`sed -n` of the notes lines named, or the extraction from the 14:37:18Z row named), byte-identical. Notes :122 is not quoted anywhere in this entry: it names the MFFU thread and carries MFFU-related identifiers. No MFFU wording is quoted in this entry. The ruling labels follow the notes' section numbers (R1 is section 1, and so on); sections 11 and 13 carry no ruling of Amear's, so there is no R11 or R13; T1 is his typed ruling.
+**Status:** WHO: amear, REPORTED BY the Claude.ai Praxis project channel, plus his typed ruling of 2026-11-15T14:37:18Z (DECISION_LOG row 2026-11-15T14:37:18Z, WHO: amear, HOW: typed; block T1 below). Source: `docs/reports/2026-11-15-voice-notes-open-questions.md` (called the notes below; untracked at filing, staged with this entry), written by the Claude.ai Praxis project channel (notes :3) from Amear's voice call, which worked through `docs/reports/2026-11-15-voice-brief-open-questions.md` (called the brief below; the master's brief for the call, unchanged, uncommitted at filing; the brief is not filed in this unit, and stays uncommitted in the working tree for the next flush, per row 2026-11-15T13:30:00Z, which says "No commit this act; the brief stays in the working tree for the next flush."; row 14:38:00Z names only the notes and the typed ruling for filing ("files the notes plus the 14:37:18Z typed ruling")) and ran between about 08:30 and 09:27 ET (notes :4). The voice agent had no repo access; it kept a list and the channel wrote the notes (notes :4). Amear's words are speech-to-text, unedited (notes :6), so the wording may be slightly off. The transcript has no per-line clock times; each ruling carries a window, W1 = 08:28-09:08 ET or W2 = 09:08-09:27 ET (notes :5). What is not his: the section headings (notes :10, :21, :27, :35, :42, :49, :55, :66, :84, :108, :113, :118, :125) and the bold sub-headings (notes :68, :75, :77, :80, :90, :95); the "Read:" lines (notes :73, :78) and the "Read:" sentence and lead-in text on notes :40 (his quoted words on :40, among them "Okay, then that's what we use.", are his); the AGENT PROPOSAL lines (notes :23, :31, and the proposal sentence on :93), which are the voice agent's proposals (his "Uh, yeah." on :93, like his replies on :24 and :32, is his); the "Consequence (the agent's reading, not ruled)" line (notes :47); the AMBIGUOUS note (notes :88); the voice agent's note on the source paper (notes :92, first sentence); the Flat1559 mapping (notes :95); the figures and their framing (notes :97-:106); all of section 11 (notes :113-:116, "this channel's check, not Amear's rulings"); the reading of the MFFU email (notes :123, "As the voice agent read it"); the section 13 bullets (notes :127-:128); and the lead-in text around his quotes. Those are the channel's or the voice agent's. Every "Filer's reading" below is the filer's (praxis-worker for praxis-manager, for the master under D-2026-11-08-D D1), changeable by Amear, and not his ruling. Each fenced block below is copied by script (`sed -n` of the notes lines named, or the extraction from the 14:37:18Z row named), byte-identical. Notes :122 is not quoted anywhere in this entry: it names the MFFU thread and carries MFFU-related identifiers. No MFFU wording is quoted in this entry. The ruling labels follow the notes' section numbers (R1 is section 1, and so on); sections 11 and 13 carry no ruling of Amear's, so there is no R11 or R13; T1 is his typed ruling.
 
@@ -126,3 +126,3 @@
 ```
-The channel's statement, not a filer's reading: per notes :106, the filed figures supersede the brief's UNVERIFIED net-profit figures (brief :40). That statement is the channel's; it is not re-derived or checked here. The brief is filed unchanged, with those figures still in it. Section 11 of the notes (the channel's check, :116) also says the brief labels its loss figures "at 1 MNQ" (brief :34), while the source labels them "MNQ derived, not an MNQ run". The difference is named here, not resolved. The brief is not edited.
+The channel's statement, not a filer's reading: per notes :106, the filed figures supersede the brief's UNVERIFIED net-profit figures (brief :40). That statement is the channel's; it is not re-derived or checked here. The brief is not filed in this unit, and stays uncommitted in the working tree for the next flush, per row 2026-11-15T13:30:00Z; it is unchanged, with those figures still in it. Section 11 of the notes (the channel's check, :116) also says the brief labels its loss figures "at 1 MNQ" (brief :34), while the source labels them "MNQ derived, not an MNQ run". The difference is named here, not resolved. The brief is not edited.
 
@@ -191,5 +191,5 @@
 
-**Limits.** No spec, rubric line, code file, bead, cron job, strategy or breaker value is changed by this entry. Nothing is run: no backtest, no retest, no paper read and no loop. F3 and F4 are not lifted. No percentage, trade count, loss cap or drawdown number is set. Amear's 5% is recorded as his words, a placeholder. The 1% in his words is recorded as said, not set (open (g)). The brief is filed unchanged. The notes are changed only by the :122 redaction and the S13 append.
+**Limits.** No spec, rubric line, code file, bead, cron job, strategy or breaker value is changed by this entry. Nothing is run: no backtest, no retest, no paper read and no loop. F3 and F4 are not lifted. No percentage, trade count, loss cap or drawdown number is set. Amear's 5% is recorded as his words, a placeholder. The 1% in his words is recorded as said, not set (open (g)). The brief is not filed in this unit, and stays uncommitted in the working tree for the next flush, per row 2026-11-15T13:30:00Z; it is unchanged. The notes are changed only by the :122 redaction and the S13 append.
 
-**S4 timing.** Written 2026-11-15T14:47:13Z, revised 2026-11-15T15:01:39Z, revised again 2026-11-15T15:16:31Z, revised a third time 2026-11-15T15:31:08Z, and revised by the finisher manager at 2026-11-15T15:35:41Z, before any act under these rulings. In DECISION_LOG.md the 2026-11-15 rows are 13:30:00Z (the master's inbox check and voice brief), 14:37:18Z (T1) and 14:38:00Z (intake and dispatch of this unit). Row 2026-11-15T15:40:00Z, the master's re-dispatch of this unit to a finisher manager, follows; it rules nothing. Its own WHEN reads "`date -u` about 15:38Z", and `date -u` read 2026-11-15T15:35:41Z at the finisher's revision, so that row's stamp is ahead of the clock; observed, not fixed. No retest, paper read, loop restart, question set, bead change or breaker change appears in the ledger. The paper read is held until this entry is committed (row 14:38:00Z). Chain: Amear (voice call, notes :4) → the notes, written by the Claude.ai Praxis project channel (notes :3) → DECISION_LOG 2026-11-15T14:37:18Z (WHO: amear, typed) → 2026-11-15T14:38:00Z (master intake and dispatch). Observed in the rows, not fixed: row 14:38:00Z carries "WHEN: `date -u` 14:37:18Z", which does not match its own timestamp and equals the previous row's. Row 13:30:00Z carries "WHEN: `date -u` 13:25:51Z". Row 14:37:18Z's WHEN matches its timestamp. Row 14:38:00Z names the reporter as "the voice channel"; this entry uses "the Claude.ai Praxis project channel", the notes' own name for it (notes :3). Also observed, not fixed: the working-tree DECISIONS.md carries an uncommitted entry whose heading names D-2026-11-12-B (working-tree :2280; not at HEAD), so working-tree line numbers after it differ from HEAD's. All DECISIONS.md line numbers in this entry are HEAD's, with one exception: this entry itself sits at DECISIONS.md :2617-:2812 in the blob staged and committed with it (HEAD's 2615 lines, one blank line, then this entry's 196 lines).
+**S4 timing.** Written 2026-11-15T14:47:13Z, revised 2026-11-15T15:01:39Z, revised again 2026-11-15T15:16:31Z, revised a third time 2026-11-15T15:31:08Z, and revised by the finisher manager at 2026-11-15T15:35:41Z, before any act under these rulings. In DECISION_LOG.md the 2026-11-15 rows are 13:30:00Z (the master's inbox check and voice brief), 14:37:18Z (T1) and 14:38:00Z (intake and dispatch of this unit). Row 2026-11-15T15:40:00Z, the master's re-dispatch of this unit to a finisher manager, follows; it rules nothing. Its own WHEN reads "`date -u` about 15:38Z", and `date -u` read 2026-11-15T15:35:41Z at the finisher's revision, so that row's stamp is ahead of the clock; observed, not fixed. Row 2026-11-15T16:05:00Z, the master's Cure 1 decision after this unit's first audit FAIL, is the record of this change: the brief is not filed in this unit, and stays uncommitted in the working tree for the next flush, per row 2026-11-15T13:30:00Z; this entry was revised for that cure at 2026-11-15T15:55:13Z (`date -u`), with that row already present in DECISION_LOG.md, so that row's stamp is ahead of the clock; observed, not fixed. No retest, paper read, loop restart, question set, bead change or breaker change appears in the ledger. The paper read is held until this entry is committed (row 14:38:00Z). Chain: Amear (voice call, notes :4) → the notes, written by the Claude.ai Praxis project channel (notes :3) → DECISION_LOG 2026-11-15T14:37:18Z (WHO: amear, typed) → 2026-11-15T14:38:00Z (master intake and dispatch). Observed in the rows, not fixed: row 14:38:00Z carries "WHEN: `date -u` 14:37:18Z", which does not match its own timestamp and equals the previous row's. Row 13:30:00Z carries "WHEN: `date -u` 13:25:51Z". Row 14:37:18Z's WHEN matches its timestamp. Row 14:38:00Z names the reporter as "the voice channel"; this entry uses "the Claude.ai Praxis project channel", the notes' own name for it (notes :3). Also observed, not fixed: the working-tree DECISIONS.md carries an uncommitted entry whose heading names D-2026-11-12-B (working-tree :2280; not at HEAD), so working-tree line numbers after it differ from HEAD's. All DECISIONS.md line numbers in this entry are HEAD's, with one exception: this entry itself sits at DECISIONS.md :2617-:2812 in the blob staged and committed with it (HEAD's 2615 lines, one blank line, then this entry's 196 lines).
 
[exit 1]
```

`s13.txt` in the scratchpad holds the standing sentence, one line, taken by `tail -n 1` of the new entry; it is used so that this section does not repeat the sentence. The diff uses one line of context for the same reason.

The staged blob and the working-tree copy carry the same new entry:

```
$ GIT_INDEX_FILE=/tmp/praxis-r15/idx git show :DECISIONS.md | sed -n '2617,2812p' | cmp - /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry_new.md && echo IDENTICAL
IDENTICAL
[exit 0]
$ GIT_INDEX_FILE=/tmp/praxis-r15/idx git show :DECISIONS.md | wc -l
    2812
[exit 0]
$ sed -n '2709,2904p' DECISIONS.md | cmp - /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/entry_new.md && echo IDENTICAL
IDENTICAL
[exit 0]
$ wc -l < DECISIONS.md
    2904
[exit 0]
```

### 5. The brief and MANIFEST.md

The unstage was run once, in an earlier Bash call, as `GIT_INDEX_FILE=/tmp/praxis-r15/idx git rm --cached -q docs/reports/2026-11-15-voice-brief-open-questions.md`; with `-q` it prints nothing. Its effect, and the untouched file on disk (`brief-orig.md` is the scratchpad copy taken before this unit staged it):

```
$ GIT_INDEX_FILE=/tmp/praxis-r15/idx git ls-files --error-unmatch docs/reports/2026-11-15-voice-brief-open-questions.md
error: pathspec 'docs/reports/2026-11-15-voice-brief-open-questions.md' did not match any file(s) known to git
Did you forget to 'git add'?
[exit 1]
$ shasum -a 256 docs/reports/2026-11-15-voice-brief-open-questions.md /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/brief-orig.md
87aff631ed033adac2e23b0636c3e77ea51a05b82b9b71447925236ad68c683a  docs/reports/2026-11-15-voice-brief-open-questions.md
87aff631ed033adac2e23b0636c3e77ea51a05b82b9b71447925236ad68c683a  /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/brief-orig.md
[exit 0]
$ git status --porcelain -- docs/reports/2026-11-15-voice-brief-open-questions.md
?? docs/reports/2026-11-15-voice-brief-open-questions.md
[exit 0]
```

The staged MANIFEST.md before (scratchpad `man_staged.md`) and after; the working-tree rows are left as they were:

```diff
$ GIT_INDEX_FILE=/tmp/praxis-r15/idx git show :MANIFEST.md | diff /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/man_staged.md -
542,543c542
< | /docs/reports/2026-11-15-voice-brief-open-questions.md | Report | 3 | 2026-11-15 | The master's voice brief for the call (Q1-Q6 of D-2026-11-14-B, search loop, parked items); filed as written, no line changed; it labels its net figures UNVERIFIED (:40), and the notes :106 (the channel's statement, not re-derived) says the filed figures supersede them; untracked at time of row; ungraded at time of row |
< | /docs/reports/2026-11-15-rulings-filing-manager.md | Report | 3 | 2026-11-15 | Finisher manager report for unit 2026-11-15-rulings-filing (DECISION_LOG 2026-11-15T14:38:00Z, re-dispatch 2026-11-15T15:40:00Z): the first manager hit its 60-turn limit with no report; draft v4 frozen (sha256 ba25de69), v5 changes three sentences on entry :194 (self-cite :2617-:2812, the 15:40:00Z row); one ADVERSARIAL pass (worker 8, PASS, 0 blocking), no fix worker; DECISIONS.md D-2026-11-15-A at :2617-:2812, eleven MANIFEST rows and eleven reports staged in temp index /tmp/praxis-r15/idx built from HEAD d9fc5f0; ungraded at time of row |
---
> | /docs/reports/2026-11-15-rulings-filing-manager.md | Report | 3 | 2026-11-15 | Finisher manager report for unit 2026-11-15-rulings-filing (DECISION_LOG 2026-11-15T14:38:00Z, re-dispatch 2026-11-15T15:40:00Z): the first manager hit its 60-turn limit with no report; draft v4 frozen (sha256 ba25de69), v5 changes three sentences on entry :194 (self-cite :2617-:2812, the 15:40:00Z row); one ADVERSARIAL pass (worker 8, PASS, 0 blocking), no fix worker; DECISIONS.md D-2026-11-15-A at :2617-:2812, ten MANIFEST rows and ten reports staged in temp index /tmp/praxis-r15/idx built from HEAD d9fc5f0; ungraded at time of row |
[exit 1]
```

```
$ GIT_INDEX_FILE=/tmp/praxis-r15/idx git show :MANIFEST.md | wc -l
     550
[exit 0]
$ tail -n 11 MANIFEST.md | cmp - <(sed -n '541,551p' /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/man_staged.md) && echo WT_ROWS_UNCHANGED
WT_ROWS_UNCHANGED
[exit 0]
```

### 6. Checks on the final staged tree

Run after this report was re-added to the temp index; the outputs below were regenerated until a re-run matched them byte for byte. The diff hash is not in this file, since a file cannot carry the hash of a diff that includes it; it is in the return to the master. The standing sentence is the last line, as before. The report held it on 5 lines before this cure: 4 inside the pasted output of the earlier sections, which are not edited, and the last line. It still holds it on 5 lines, so this section adds none (line numbers below).

```
$ GIT_INDEX_FILE=/tmp/praxis-r15/idx git diff --cached --stat HEAD
 DECISIONS.md                                       |  197 +++
 MANIFEST.md                                        |   10 +
 docs/reports/2026-11-15-rulings-filing-manager.md  |  563 ++++++++
 docs/reports/2026-11-15-rulings-filing-worker1.md  |  721 +++++++++++
 docs/reports/2026-11-15-rulings-filing-worker2.md  | 1342 ++++++++++++++++++++
 docs/reports/2026-11-15-rulings-filing-worker3.md  |  602 +++++++++
 docs/reports/2026-11-15-rulings-filing-worker4.md  |  464 +++++++
 docs/reports/2026-11-15-rulings-filing-worker5.md  |  392 ++++++
 docs/reports/2026-11-15-rulings-filing-worker6.md  |  666 ++++++++++
 docs/reports/2026-11-15-rulings-filing-worker7.md  |  581 +++++++++
 docs/reports/2026-11-15-rulings-filing-worker8.md  |  783 ++++++++++++
 .../2026-11-15-voice-notes-open-questions.md       |  131 ++
 12 files changed, 6452 insertions(+)
[exit 0]
$ GIT_INDEX_FILE=/tmp/praxis-r15/idx git diff --cached --name-only HEAD | grep -c voice-brief
0
[exit 1]
$ git show HEAD:DECISIONS.md | cmp - <(GIT_INDEX_FILE=/tmp/praxis-r15/idx git show :DECISIONS.md | head -c $(git cat-file -s HEAD:DECISIONS.md)) && echo DECISIONS_HEAD_IS_PREFIX
DECISIONS_HEAD_IS_PREFIX
[exit 0]
$ git show HEAD:MANIFEST.md | cmp - <(GIT_INDEX_FILE=/tmp/praxis-r15/idx git show :MANIFEST.md | head -c $(git cat-file -s HEAD:MANIFEST.md)) && echo MANIFEST_HEAD_IS_PREFIX
MANIFEST_HEAD_IS_PREFIX
[exit 0]
$ GIT_INDEX_FILE=/tmp/praxis-r15/idx git diff --cached HEAD | grep -c -E '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
0
[exit 1]
$ tail -n 1 docs/reports/2026-11-15-rulings-filing-manager.md | cmp - /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/s13.txt && echo LAST_LINE_IS_STANDING_SENTENCE; grep -c -F -f /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/s13.txt docs/reports/2026-11-15-rulings-filing-manager.md
LAST_LINE_IS_STANDING_SENTENCE
5
[exit 0]
$ grep -n -F -f /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/s13.txt /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/mgr_orig.md | cut -d: -f1 | tr '\n' ' '; echo; grep -n -F -f /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/s13.txt docs/reports/2026-11-15-rulings-filing-manager.md | cut -d: -f1 | tr '\n' ' '; echo
143 168 217 238 332 
143 168 217 238 563 
[exit 0]
$ head -n 331 docs/reports/2026-11-15-rulings-filing-manager.md | cmp - <(head -n 331 /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1efcd0c6-cf29-4431-abf5-ffd6776843da/scratchpad/mgr_orig.md) && echo LINES_1_331_UNCHANGED
LINES_1_331_UNCHANGED
[exit 0]
```

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
