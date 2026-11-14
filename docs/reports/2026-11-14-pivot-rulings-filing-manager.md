# Manager report: unit 2026-11-14-pivot-rulings-filing

## Task
File Amear's nine voice rulings of 2026-11-14 (R1-R9) as DECISIONS.md entry D-2026-11-14-B (WHO: amear, REPORTED BY the voice-chat agent). File the three untracked voice files and this unit's reports, with MANIFEST rows. Stage it all in temp index /tmp/praxis-pv/idx, built from 244cfc3. Dispatch: DECISION_LOG row 2026-11-14T15:08:00Z, item (a).

## Rubric criteria addressed
S1, S2, S4, S5, S6, S8, S13 (specs/SPEC_RUBRIC.md :133-:145).

## Workers dispatched
| id | mode | outcome |
|---|---|---|
| worker1 | BUILD | Drafted and staged the entry, S13 appends, 6 MANIFEST rows. Its own report Write was refused by a hook, so the manager filed the returned text (`-worker1.md`, filer line at :1). |
| worker2 | ADVERSARIAL, read-only | Result FAIL, with 2 MAJOR and 6 MINOR defects on the pre-cure entry. Returned inline; the manager filed it (`-worker2.md`, filer line at :1). |

## Process log
1. The manager read the rubric, the notes, the brief and DECISION_LOG :971-:974, then briefed worker1.
2. Worker1 returned. The manager re-ran its checks (E1-E3), then briefed worker2 with only the artifact and the criteria.
3. Worker2 returned FAIL. The cap of 2 workers was used up, so the manager cured defects 1-5 and 7 himself. Each cure was a doc-text edit at the end of the working-tree DECISIONS.md. The staged blob was rebuilt as HEAD + one blank line + the working-tree entry (E4). The cured lines have had no fresh independent adversary. The auditor is their first independent reader.
4. The worker reports were staged, then this report. The canonical hash is in the return to the master, because this file cannot contain the hash of an index that includes it.

## Verification evidence
E1. HEAD-only DECISIONS blob. The ckh heading is absent from the blob, and present in the working tree as a positive control (run before the cure; E4 repeats it after):
```
-- HEAD prefix
rc=0
-- ckh positive control (working tree) / blob / HEAD
1
0
0
```
E2. All 10 fences (24 lines) against their sources. The first run with zsh `echo` gave `cmp: EOF` / `rc=1`, which was a tool artifact. The run with files:
```
      24 .../scratchpad/fences.txt
      24 .../scratchpad/src.txt
concat cmp rc=0
```
E3. S13 negative control on the saved originals, and an unchanged prefix after the appends:
```
2026-11-14-voice-brief-overnight.md grep -cx=0
2026-11-14-voice-brief-pivot.md grep -cx=1
2026-11-14-voice-notes-pivot.md grep -cx=0
2026-11-14-voice-brief-overnight.md rc=0
2026-11-14-voice-notes-pivot.md rc=0
```
E4. After the cure: blob rebuilt and restaged. The entry is 89 lines (blob 2527-2615); the new quotes are each found, with a negative control:
```
wt heading line 2619
      89
blob 69c8608be25606f46a3a7bd70139944682784e90
    2615
HEAD-prefix rc=0
ckh in blob: 0 wt: 1
blob-entry vs wt-tail rc=0
fences vs sources rc=0
S13 in entry: 1; last: Fills are optimistic; Standard
-- new inline quotes
1
1
### Block 2: Backtesting (Requires Rithmic Data Connection)
What you’re doing: Validating the NQ Noise-Area strategy aga
The backtest itself: NinjaTrader Strategy Analyzer with the 
|A — Micro |1 MNQ ($2/point)                  |2 weeks + 10 
|B — Single|1 NQ ($20/point)                  |4 weeks + 20 
-- negative control
0
```
(The two `1` lines are: HEAD DECISIONS :2426 contains "the step 4 search loop and its backtests", and brief :34 contains "Amear has not ruled on it". The negative control is brief :35 for the second phrase.)
E5. The S4 stamp. The entry file's mtime is local time, and the local offset is -0500:
```
2026-11-14T10:14:01 /tmp/praxis-pv/entry.txt
-0500
```
Records of a skill, a first filter or a standard (working-tree DECISIONS.md, after the cure). `grep -n -i -e 'voice-brief skill' -e 'research-screen standard' -e 'first-filter' DECISIONS.md | cut -c1-60`, then `ls ~/.claude/skills .claude/skills | grep -ci voice`:
```
2683:Filer's reading: two instructions. (a) Anything ambiguo
2696:- D-2026-11-13-D: R1 holds the search loop of ruling 3 
2705:**S4 timing.** Written 2026-11-14T15:14:01Z, corrected 
0
```
All three hits are lines of the new entry.
E6. Scope, the name and email sweep (counts only), and S13, all before this report was staged:
```
M	DECISIONS.md
M	MANIFEST.md
A	docs/reports/2026-11-14-pivot-rulings-filing-worker1.md
A	docs/reports/2026-11-14-pivot-rulings-filing-worker2.md
A	docs/reports/2026-11-14-voice-brief-overnight.md
A	docs/reports/2026-11-14-voice-brief-pivot.md
A	docs/reports/2026-11-14-voice-notes-pivot.md
90	0	DECISIONS.md
6	0	MANIFEST.md
121	0	docs/reports/2026-11-14-pivot-rulings-filing-worker1.md
66	0	docs/reports/2026-11-14-pivot-rulings-filing-worker2.md
36	0	docs/reports/2026-11-14-voice-brief-overnight.md
49	0	docs/reports/2026-11-14-voice-brief-pivot.md
73	0	docs/reports/2026-11-14-voice-notes-pivot.md
b3f41e273ec9becc84f3799a71a65f85acdd76cfe7990b3bb7685b8a8555b916  -
DECISIONS.md email=0 tok=0 S13x=18
MANIFEST.md email=0 tok=2 S13x=0
docs/reports/2026-11-14-pivot-rulings-filing-worker1.md email=0 tok=0 S13x=1
docs/reports/2026-11-14-pivot-rulings-filing-worker2.md email=0 tok=0 S13x=1
docs/reports/2026-11-14-voice-brief-overnight.md email=0 tok=0 S13x=1
docs/reports/2026-11-14-voice-brief-pivot.md email=0 tok=0 S13x=1
docs/reports/2026-11-14-voice-notes-pivot.md email=0 tok=0 S13x=1
entry S13x=1
HEAD MANIFEST tok=2
-- real index
A	docs/reports/evidence/2026-10-28-mffu-<tok>-reply.png
```
`tok` is the MFFU rep's first name (bead c2w), taken from the evidence file name in the shell and never written down. The 2 MANIFEST hits equal HEAD's 2; the new rows add 0. DECISIONS S13x=18 counts the whole file; the entry's own count is 1. The real-index line is shown redacted.

## Adversarial findings (worker2) and disposition
1. MAJOR: the R5 reading credited the "starting point" line (notes :34) to Amear. CURED: that line is now labelled the voice agent's text, and the entry quotes "Amear has not ruled on it" (brief :34).
2. MAJOR: the S4 line said the entry was written before any work the rulings govern, but R1's pause and the R4 dispatch came first. CURED: the S4 line now names both as earlier acts. R1 rests on ledger row 14:49:30Z (S5), and no recheck result is used.
3. MINOR: "the search loop stays paused" was unobserved. CURED: the line now reads "paused at the 14:50:10Z readback", and resuming is Amear's.
4. MINOR: R9(b) "proposed, not self-certified" was not his words. CURED: it is attributed to the voice agent's handoff (notes :59).
5. MINOR: cross-block checks were missing. CURED: an S6 bullet for Block 2 (Phase 3 spec :62, :64, :76), Block 5 stages A-B (:138-:139), and the first-filter change against ruling 2 (:2426).
6. MINOR: the 6 MANIFEST rows pointed at unstaged reports. CURED: all three reports are staged. Six rows, not three: the master's brief to this unit asked for 3 rows plus one per unit report. The 15:08:00Z row says "plus 3 rows". That is for the master to reconcile.
7. MINOR: the sub-headings alter the notes' titles. CURED: the Status line now says the sub-headings shorten R4's and R9's titles and merge R5's and R6's.
8. MINOR (left for the master): the staged notes carry the sentence at :71 with a suffix and once standalone at :73. The brief's rule counts the standalone line, so the count is 1 (E6). The prior cna-filing trim shows files dropped only for two standalone copies.

## S6 cross-block check
The entry's S6 section names these touches: the search loop and D-2026-11-13-D rulings 2-3; D-2026-11-13-E bar items 2-3; A4; the walk-forward spec and values; breakers #1 and #2 (Phase 3 :97-:98, topology :58-:59, D-2026-11-08-A R8); the per-trade sizing in Blocks 1 and 5; Block 2's Analyzer and data path; F3; F4. Worker2's attack 2 found every cite as claimed (worker2 report). The named tensions are R7 against R8's breaker #2 rework, and R3 against Block 5 :140. None is resolved. No file outside the staged list was changed.

## Files staged (/tmp/praxis-pv/idx only)
The 7 paths in E6, plus this report. The working-tree DECISIONS.md and MANIFEST.md each got the same tail as their blobs (pure appends). The real index was not touched (E6). HANDOFF, STATUS, ISSUE_REGISTER, AUDIT_LOG, specs, scripts and .claude were not touched.

## Decisions for the master
- The cured lines (working-tree DECISIONS :2621, :2662, :2683, :2696, :2699-:2700, :2705) were checked by manager commands (E4), not by a fresh adversary.
- Finding 8 (the notes' :71 suffix copy) and the 3-versus-6 rows note (finding 6).
- Worker1's report gives the entry as blob 2527-2614 and hash f2a896a7...; both were superseded by the cure (E4, E6).

Result: PASS

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## Cure 1 (S1, S2)
Appended after an independent audit FAIL on S1 and S2. Lines :1-:135 above are byte-identical to the 135-line file as it stood before this section, which was copied to the scratchpad first (`S` below). Every git command further down ran with `GIT_INDEX_FILE=/tmp/praxis-pv/idx`, before this file was restaged.
```
$ head -n 135 docs/reports/2026-11-14-pivot-rulings-filing-manager.md | cmp - $S/mgr-orig.md; echo head-cmp-rc=$?
head-cmp-rc=0
```

**(1) Untouched files (:123 last sentence, :126 last sentence).** Restated: the staged diff contains none of HANDOFF, STATUS, ISSUE_REGISTER, AUDIT_LOG, specs, scripts or .claude. This output covers the temp index only and says nothing about the working tree.
```
$ git diff --cached --name-status 244cfc3
M	DECISIONS.md
M	MANIFEST.md
A	docs/reports/2026-11-14-pivot-rulings-filing-manager.md
A	docs/reports/2026-11-14-pivot-rulings-filing-worker1.md
A	docs/reports/2026-11-14-pivot-rulings-filing-worker2.md
A	docs/reports/2026-11-14-voice-brief-overnight.md
A	docs/reports/2026-11-14-voice-brief-pivot.md
A	docs/reports/2026-11-14-voice-notes-pivot.md
```
**(2) The S6 cites (:123, "Worker2's attack 2 found every cite as claimed").** Withdrawn as evidence: the worker2 report has no output behind it. The manager re-ran the check. Each line of input is `rev|path|line|phrase`. rev is `244cfc3`, or `idx` (the staged blob) for the notes and the brief, which are not in 244cfc3 (first block). For each cite in the entry's S6 bullets, the phrase is the part of the entry's claim that the cited line must carry (second block; its last row is a negative control, phase3 :53).
```
$ for f in docs/reports/2026-11-14-voice-notes-pivot.md docs/reports/2026-11-14-voice-brief-pivot.md; do git cat-file -e 244cfc3:$f 2>/dev/null; echo "$f in-244cfc3-rc=$?"; done
docs/reports/2026-11-14-voice-notes-pivot.md in-244cfc3-rc=128
docs/reports/2026-11-14-voice-brief-pivot.md in-244cfc3-rc=128
```
```
$ while IFS='|' read r f n k; do [ $r = idx ] && rv= || rv=$r; printf '%s\t%s\t%s\t%s\t%s\n' $r $(basename $f .md) $n "$k" $(git show $rv:$f | sed -n "${n}p" | grep -cF -- "$k"); done < cites.txt | awk -F'\t' '{g=$1" "$2; if(g!=p){if(p!="")print l; l=g; p=g} l=l" :"$3"["$4"]="$5} END{print l}'
244cfc3 DECISIONS :2426[carry on: the step 2 filing, the step 4 search loop]=1 :2433[Ruling 3: the search loop]=1 :1583[redone]=1 :1584[#2 max 2 trades/day]=1 :1587[KEEP: #1 daily loss limit]=1 :1589[PROPOSED]=1
idx 2026-11-14-voice-notes-pivot :57[first filter in the search loop]=1 :60[until steps 2 to 4 are done]=1
244cfc3 2026-11-05-walk-forward-spec :31[Revisit if a personal account is used.]=1 :32[MFFU]=1 :67[no added stop. — INFERRED]=1
244cfc3 2026-11-06-walk-forward-values :51[m × ATR(14)]=1 :73[m × ATR(14)]=1
244cfc3 2026-11-05-phase3-build-specification :54[stop-loss + take-profit]=1 :62[Block 2: Backtesting]=1 :64[MFFU connection]=1 :76[Order Fill Resolution = High]=1 :97[Daily loss limit]=1 :98[Max trades per day]=1 :138[1 MNQ]=1 :139[1 NQ]=1 :140[0.5% per trade]=1
244cfc3 2026-11-10-live-signal-topology :58[Daily loss limit]=1 :59[Max trades per day]=1
idx 2026-11-14-voice-brief-pivot :14[changing circuit-breaker values while real money is at stake]=1 :35[full audit gates for anything that can place an order]=1
244cfc3 2026-11-05-phase3-build-specification :53[stop-loss + take-profit]=0
```
What this shows: each of the 26 cited lines in the output above carries its phrase (=1), and the control does not (=0). It does not show that the entry reads each line correctly. The phrases are the manager's choice.

**(3) Email sweep (E6 :98-:104; S2).** E6 :98 `DECISIONS.md email=0` was wrong. So was worker1 :69:
```
$ sed -n '69p' docs/reports/2026-11-14-pivot-rulings-filing-worker1.md | cut -c1-70
:DECISIONS.md                                        email=0 tok=0
```
The corrected figure (block below) is 2 in the staged file, both inside the unchanged HEAD part (E4 :51 `HEAD-prefix rc=0`; HEAD is 2525 lines; the hits are on lines 569 and 1188), with 0 on added lines. Counts only:
```
$ R='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'; for p in $(git diff --cached --name-only 244cfc3); do a=$(git show :$p | grep -E -o "$R" | wc -l | tr -d ' '); b=$(git diff --cached 244cfc3 -- $p | grep '^+' | grep -v '^+++' | grep -E -o "$R" | wc -l | tr -d ' '); echo "$p file=$a added=$b"; done
DECISIONS.md file=2 added=0
MANIFEST.md file=0 added=0
docs/reports/2026-11-14-pivot-rulings-filing-manager.md file=0 added=0
docs/reports/2026-11-14-pivot-rulings-filing-worker1.md file=0 added=0
docs/reports/2026-11-14-pivot-rulings-filing-worker2.md file=0 added=0
docs/reports/2026-11-14-voice-brief-overnight.md file=0 added=0
docs/reports/2026-11-14-voice-brief-pivot.md file=0 added=0
docs/reports/2026-11-14-voice-notes-pivot.md file=0 added=0
$ echo "HEAD DECISIONS.md file=$(git show 244cfc3:DECISIONS.md | grep -E -o "$R" | wc -l | tr -d ' ') lines=$(git show 244cfc3:DECISIONS.md | wc -l | tr -d ' '); staged hit lines: $(git show :DECISIONS.md | grep -n -E -o "$R" | cut -d: -f1 | tr '\n' ' ')"
HEAD DECISIONS.md file=2 lines=2525; staged hit lines: 569 1188
```
The manager-report row counts the 135-line blob from before this section was added. The count over the restaged blob is in the return to the master, because this file cannot contain its own restaged state.
