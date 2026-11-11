# 2026-11-11 v-rulings-filing Correction 2 - manager report

Result: PASS

## Task
Unit `2026-11-11-v-rulings-filing-correction-2`, bead Praxis_build-n1y (resumed by Amear, DECISION_LOG 2026-11-11T22:08:30Z, WHO: amear). The second audit of the filing unit for rulings V1-V7 failed on S1 only (DECISION_LOG 2026-11-11T19:45:30Z). The correction-1 worker1 report's section 8 and Findings claimed the name is in "at least 11 report filenames", with 2 rows pasted and a described tail. Its section 7 claimed "All nine sections read `(pending)`", with 3 of 27 lines pasted. The correction-1 manager report :228 repeated the first claim. The audit also had two MINOR findings: stale S13 self-check output, and MANIFEST row numbers cited at working-tree positions. This unit re-runs every count and set claim with full output and corrects both reports append-only.

## Rubric criteria addressed
- S1 "Every claim in a report has pasted command output, not a description of output." (specs/SPEC_RUBRIC.md:124)
- S2 "No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure." (:125) Evidence taken from session transcripts is labelled RECOVERED. The staged MANIFEST positions are labelled INFERRED.
- S7 "Nothing is committed while any audit box is unchecked." (:130) Nothing was staged or committed. The index check is below.
- S13 (:136): every report written or corrected ends with the S13 sentence once, as a standalone line.

## Workers dispatched (id, mode, outcome)
| id | mode | outcome | report |
|----|------|---------|--------|
| worker1 | BUILD | Re-ran every claim and inserted Correction 2 into both reports. Wrote one memory file under .claude/agent-memory/ (out of scope), then deleted it; see Adversarial findings. | docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md |
| worker2 | ADVERSARIAL | FAIL: 1 MAJOR (the skeleton could be recovered from the session transcript, so "not re-runnable" was wrong and the "nine sections" claim was never corrected) and 6 MINOR. Stopped at its 40-turn limit before its self-check, which I ran (below). | docs/reports/2026-11-11-v-rulings-filing-correction-2-worker2.md |
| worker3 | BUILD (fix) | Fixed all 7 worker2 findings: skeleton and S13 outputs RECOVERED, a new (b) item C2.4 for the `tail -3` block, exact quotes, distinct masked rows, an addendum to the worker1 report. | docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md |
| worker4 | ADVERSARIAL | FAIL: 4 MINOR, 0 MAJOR | docs/reports/2026-11-11-v-rulings-filing-correction-2-worker4.md |
| worker5 | BUILD (fix) | Fixed the 4 worker4 findings | docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md |
| worker6 | ADVERSARIAL (narrow) | FAIL: 4 MINOR, 0 MAJOR, all in the worker3 and worker5 reports. I answered them with appended manager notes. | docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md |

## Process log
1. Before any edit, I copied the two correction-1 reports and MANIFEST.md to /tmp/c2pre/ and checked their sha256 (block E1).
2. Wrote the skeleton of this report, then dispatched worker1 (BUILD).
3. Read worker1's inserted sections and its report. Re-ran the append-only diffs and the key counts myself (block E2).
4. Dispatched worker2 (ADVERSARIAL). I gave it the artifacts and criteria, not worker1's reasoning. It stopped at its turn limit and left the literal line `SELFCHECK_PLACEHOLDER` at its report's :985. I replaced that one line with a note pointing here (block E3).
5. Ran negative controls on the gates (block E4).
6. Dispatched worker3 (fix) for the worker2 findings, then worker4 (ADVERSARIAL), worker5 (fix) and worker6 (ADVERSARIAL, narrow).
7. Answered worker6's 4 MINOR findings myself, a pure doc edit: one appended manager note in each of the worker3 and worker5 reports, pasting the qcheck.py source and the variable definitions and flagging the stale self-check values. The current values are in block E6 (diff in block E5).
8. Appended 9 MANIFEST rows. Ran the final checks (blocks E5-E7).

## Verification evidence (command output)

### E1. Pre-edit snapshot (taken before any edit)
```
cc00cc5edd2035b26ad6e0c247de1ffbaf9d08dc2c8fe9be1d864feba6d222ed  /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md
24932bddc8402421df8a3304d9dd5b2875a0eec21f1d8d205735146ac2c12049  /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md
82f3395dd8df1fd40c4d027201c7164815669436eaaf3ef8c32a2a5aef608546  /tmp/c2pre/MANIFEST.md
24932bddc8402421df8a3304d9dd5b2875a0eec21f1d8d205735146ac2c12049  docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md
cc00cc5edd2035b26ad6e0c247de1ffbaf9d08dc2c8fe9be1d864feba6d222ed  docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md
82f3395dd8df1fd40c4d027201c7164815669436eaaf3ef8c32a2a5aef608546  MANIFEST.md
     242 /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md
     265 /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md
     405 /tmp/c2pre/MANIFEST.md
     912 total
2026-11-11T17:08:51-0500
```

### E2. Manager re-run after worker1 (key figures the corrections rest on)
```
$ /tmp/vrf-c2/repogrep.sh w | wc -l
      43
$ /tmp/vrf-c2/repogrep.sh nw | wc -l
      46
$ find docs/reports -path docs/reports/evidence -prune -o -type f -iname "*$N*" -print | wc -l
      11
$ grep -n -F correction-1-manager.md MANIFEST.md | cut -d"|" -f1-2; grep -n -F correction-1-worker1.md MANIFEST.md | cut -d"|" -f1-2
310:| /docs/reports/2026-11-08-wf-spec-amendment-correction-1-manager.md 
372:| /docs/reports/2026-11-11-vm-agent-hermes-correction-1-manager.md 
379:| /docs/reports/2026-11-11-mffu-investigation-correction-1-manager.md 
404:| /docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md 
373:| /docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker1.md 
380:| /docs/reports/2026-11-11-mffu-investigation-correction-1-worker1.md 
405:| /docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md 
$ git show HEAD:MANIFEST.md | wc -l
     379
```
In the working tree, the correction-1 rows were at 404 and 405 before this unit's rows were appended. The staged positions will differ: the master stages HEAD plus this bead's rows, and the 8 older diq rows stay out. Under that assumption, the (b) Correction 2 item C2.2 computes 396 and 397. That figure is INFERRED, not observed.

### E3. Worker2 placeholder line replaced (the only change I made to worker2's file)
```
985c985
< SELFCHECK_PLACEHOLDER
---
> (Not completed: worker2 stopped at its 40-turn limit before running this self-check. The manager ran the check on this file; the output is in docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md, Verification evidence.)
```

### E4. Negative controls (the gates trip)
```
$ diff -d $PA $T/altered.md | grep -v "^>"   (negative control: one original line altered)
242c242
< The blank counts on the `2026-10-28-f4-<NAME>-reply-*.md` rows come from a bug in my loop: I fed masked filenames back into grep, which then printed "No such file or directory". The rows still prove that at least 11 report **filenames** in docs/reports/ contain the name. I did not check whether a 4-letter whole-word match in the agent-memory files is the name itself or a common English word.
---
263a264,523
$ diff -d $PA $T/altered.md | grep -c "^<"
1
$ python3 -I /tmp/vrf-c1/s13.py $T/s13twice.md   (negative control: S13 line duplicated)
s13twice.md standalone_outside_fence=2 at=[525, 526] in_fence=0 last_nonblank_line=526 is_last=False substring_lines=2
$ /tmp/vrf-c2/selfcheck.sh $T/named.md | sed s#$T#\$T#   (negative control: name planted, never printed)
$T/named.md: name_ci=1 V1_HIT_lines=1 S13_containing=1 S13_standalone=1 at=[525] last_nonblank_line=526 last_nonblank_is_S13=NO lines=526
V1 positive control (hyphen-split synthetic line): HIT_lines=1
tmp removed rc=0
```
($T was a mktemp copy of the worker1 report as it stood after worker1's insertion. The diff line the control quotes is an original line, with the name masked.)

### E5. Final append-only and MANIFEST checks
```
$ for f in correction-1-worker1 correction-1-manager; do diff -d /tmp/c2pre/${P#docs/reports/}$f.md $P$f.md | grep -v "^>"; diff -d /tmp/c2pre/${P#docs/reports/}$f.md $P$f.md | grep -c "^<"; done
264a265,874
0
241a242,683
0
$ cmp <(head -n 264 /tmp/c2pre/...-correction-1-worker1.md) <(head -n 264 $P"correction-1-worker1.md") && echo a-body-identical; cmp <(head -n 241 /tmp/c2pre/...-correction-1-manager.md) <(head -n 241 $P"correction-1-manager.md") && echo b-body-identical
a-body-identical
b-body-identical
$ diff -d /tmp/c2mgr/${P#docs/reports/}correction-2-worker3.md ${P}correction-2-worker3.md | grep -v "^>"; diff -d /tmp/c2mgr/${P#docs/reports/}correction-2-worker5.md ${P}correction-2-worker5.md | grep -v "^>"
407a408,427
357a358,369
$ diff /tmp/c2pre/MANIFEST.md MANIFEST.md | grep -v "^>"; diff /tmp/c2pre/MANIFEST.md MANIFEST.md | grep -c "^>"; wc -l MANIFEST.md
405a406,414
9
     414 MANIFEST.md
$ sed -n 406,414p MANIFEST.md | cut -d"|" -f2 | nl -v406 -ba
   406	 /docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md 
   407	 /docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md 
   408	 /docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md 
   409	 /docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md 
   410	 /docs/reports/2026-11-11-v-rulings-filing-correction-2-worker2.md 
   411	 /docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md 
   412	 /docs/reports/2026-11-11-v-rulings-filing-correction-2-worker4.md 
   413	 /docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md 
   414	 /docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md 
$ sed -n 406,414p MANIFEST.md | grep -ci -- "$N"
0
$ git diff --cached --name-only -- MANIFEST.md "docs/reports/2026-11-11-v-rulings-filing-*" | wc -l
       0
$ find .claude -newer /tmp/c2pre/worker2.as-returned.md | wc -l
       0
```
Rows 406 and 407 are UPDATE rows for the two corrected reports. The existing UPDATE ROW convention (for example MANIFEST.md:318) is to cite "the earlier row for this path" without a row number. Rows 406-414 are working-tree positions. The staged positions will differ, because the master stages HEAD plus this bead's rows. They are therefore not stated here as observed.

### E6. Name count, split detector and S13, every report of this unit and both corrected reports
```
$ /tmp/vrf-c2/selfcheck.sh ${P}correction-1-worker1.md ${P}correction-1-manager.md ${P}correction-2-worker{1,2,3,4,5,6}.md | M
docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[875] last_nonblank_line=875 last_nonblank_is_S13=YES lines=875
docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[684] last_nonblank_line=684 last_nonblank_is_S13=YES lines=684
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[577] last_nonblank_line=577 last_nonblank_is_S13=YES lines=577
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker2.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[987] last_nonblank_line=987 last_nonblank_is_S13=YES lines=987
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[428] last_nonblank_line=428 last_nonblank_is_S13=YES lines=428
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker4.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[712] last_nonblank_line=712 last_nonblank_is_S13=YES lines=712
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[370] last_nonblank_line=370 last_nonblank_is_S13=YES lines=370
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[207] last_nonblank_line=207 last_nonblank_is_S13=YES lines=207
V1 positive control (hyphen-split synthetic line): HIT_lines=1
$ /tmp/vrf-c2/selfcheck.sh ... | M | wc -l
       9
```
This block is also the self-check of the worker2 report that worker2 never ran, and the current self-check values for the worker5 report (its own block is stale, as the manager note in that report says). The check of this report is in E8.

### E7. Other personal data
```
$ python3 -I /tmp/c2mgr/pii.py <the two corrected reports, six worker reports, this report>
docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md ipv4_not_loopback=0 email=0 mac=0 keypath=0 mac_or_key_lines=
docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md ipv4_not_loopback=0 email=0 mac=0 keypath=0 mac_or_key_lines=
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md ipv4_not_loopback=0 email=0 mac=0 keypath=0 mac_or_key_lines=
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker2.md ipv4_not_loopback=0 email=0 mac=0 keypath=4 mac_or_key_lines=909
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md ipv4_not_loopback=0 email=0 mac=0 keypath=0 mac_or_key_lines=
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker4.md ipv4_not_loopback=0 email=0 mac=0 keypath=0 mac_or_key_lines=
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md ipv4_not_loopback=0 email=0 mac=0 keypath=2 mac_or_key_lines=347
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md ipv4_not_loopback=0 email=0 mac=0 keypath=12 mac_or_key_lines=159,171,172,173,174,175,198
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md ipv4_not_loopback=0 email=0 mac=0 keypath=0 mac_or_key_lines=
$ grep -cE "[A-Za-z0-9_~]/\.ssh/|\.ssh/[A-Za-z0-9_]|[A-Za-z0-9_-]+\.pem" <worker2, worker5, worker6 reports>
2026-11-11-v-rulings-filing-correction-2-worker2.md: 0
2026-11-11-v-rulings-filing-correction-2-worker5.md: 0
2026-11-11-v-rulings-filing-correction-2-worker6.md: 0
$ sed -n '171,175p' docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | cut -c1-160
$ grep -noE "id_(rsa|ed25519|ecdsa)|\.ssh/|\.pem\b" $W5
347:.ssh/
347:.pem
$ grep -nE "id_(rsa|ed25519|ecdsa)|\.ssh/|\.pem\b" $W5 | cut -c1-70
347:$ grep -ciE "id_(rsa|ed25519|ecdsa)|\.ssh/|\.pem\b" $A $C $D3 $W5
```
Each keypath hit is a bare `.ssh/`, `.pem`, `id_rsa` or `id_ed25519` token inside a pasted grep pattern. None of them is preceded or followed by a path component (second command: 0 in all three files). The first line of the block above is the `sed` command I ran; the next four lines are its own output (worker6's :171-175, which paste worker6's grep of the worker5 report).

### E8. Self-check of this report
Run after this report was written. The output is in the "Self-check run" line at the end of Files staged.

## Adversarial findings
- worker2 MAJOR 1. The section 7 skeleton was not gone. Its full content is in the session transcript, as the Write call of 2026-11-11T19:33:58Z. Disposition: fixed by worker3. (a) C2.1 now restricts the negative to /tmp, /private/tmp and git, and pastes the RECOVERED content: 27 lines, 8 `## ` lines, 8 `(pending)` lines. The original ":218 All nine sections" is corrected as WRONG (8). Worker4 confirmed those three counts with its own parser and found no break on the substance.
- worker2 MINOR 2-7 (recovered S13 outputs, the `$R` definition, unpasted process-log claims, indistinguishable masked rows, inexact quotes, the `tail -3` block at (b):213). Disposition: all fixed by worker3.
- worker4 MINOR 1-4 (wrong list of labelled lines, stale "current" figures, quote-check coverage, an untested assertion). Disposition: all fixed by worker5. Worker6 re-ran the new figures and found that they match.
- worker6 MINOR 1-4 (stale self-check values in the worker5 report, the unpasted qcheck.py source in the worker3 erratum, undefined variables in the worker5 report). Disposition: answered by the manager notes at worker3 :408-427 and worker5 :358-369 (diff in E5), with current values in E6. These two notes are my own edits, and no adversarial worker re-checked them. They paste a script listing and a grep output, and claim nothing else.
- Out of scope, reported and not fixed. Worker1 wrote one memory file under .claude/agent-memory/ and later deleted it. That directory is gitignored (.gitignore:26), so git cannot show the state before or after. What can be observed now: .claude/agent-memory/praxis-worker/MEMORY.md has mtime 2026-11-11T17:19:58, and each of its links resolves to one of the 5 memory files in the directory, with no orphan entry. Restoration to the exact prior bytes is UNVERIFIED (not re-runnable), because no pre-edit copy exists. Since worker2 returned, nothing under .claude/ has changed (E5, last command: 0).
- Disclosed limitation: the RECOVERED evidence depends on machine-local session transcripts, which are not under version control.

## S6 cross-block check
Not applicable. This unit approves no deviation. It touches no block spec, code, hook or setting. It is a set of append-only text corrections in two unit reports, plus new reports and MANIFEST rows.

## Files staged
None (S7; E5 index check = 0). Written or edited in the working copy only:
- docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md: lines 265-874 inserted (Correction 2). Original lines 1-264 and the final line, now :875, are unchanged.
- docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md: lines 242-683 inserted (Correction 2). Original lines 1-241 and the final line, now :684, are unchanged.
- docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md: new, 577 lines, including the worker3/worker5 addendum before its final line.
- docs/reports/2026-11-11-v-rulings-filing-correction-2-worker2.md: new, 987 lines. Line 985 was replaced by me (E3).
- docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md: new, 428 lines. Worker5 erratum and manager note at :408-427.
- docs/reports/2026-11-11-v-rulings-filing-correction-2-worker4.md: new, 712 lines.
- docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md: new, 370 lines. Manager note at :358-369.
- docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md: new, 207 lines.
- docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md: this report, new.
- MANIFEST.md: rows 406-414 appended (working-tree positions).
- Outside the repo: helper copies and scripts in /tmp/c2pre, /tmp/vrf-c2, /tmp/c2fix, /tmp/c2w5 and /tmp/c2mgr.

Self-check run (`/tmp/vrf-c2/selfcheck.sh` and `/tmp/c2mgr/pii.py` on this report, output joined on one line): docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[206] last_nonblank_line=206 last_nonblank_is_S13=YES lines=206 V1 positive control (hyphen-split synthetic line): HIT_lines=1 docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md ipv4_not_loopback=0 email=0 mac=0 keypath=15 mac_or_key_lines=163,168,169,170,171,172,174 

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
