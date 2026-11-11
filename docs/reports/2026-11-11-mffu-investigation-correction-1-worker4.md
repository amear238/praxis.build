# MFFU investigation Correction 1 — worker 4 (Fix 6, Fix 8)

## Task
Unit `2026-11-11-mffu-investigation-correction-1`, worker 4, mode BUILD. Authority: DECISION_LOG 2026-11-11T17:32:05Z, decided by the master under D-2026-11-08-D D1. HEAD 85a803f.

The target was read only: `/tmp/mffu-orig.md`, a pristine copy of `docs/reports/2026-11-11-mffu-connection-investigation.md`. All line numbers below are that copy's. The paste text for the target's `## Correction 1` is in `/tmp/mffu-corr/w4.md`, items C4.1-C4.14.

## Rubric criteria
- **S1:** every claim in w4.md is backed by a command run in this session, with its real output pasted.
- **S2:** each grade states what was checked and what was not. The rows not checked are listed in C4.2. The ruling label "R-VN4-6" at line 133 and the D2(b) claim at line 183 were not checked.

## Process log
1. Wrote skeletons of both files first.
2. Read the target's §1, §3, §4.3, §4.4 and §8.1 with the rep-name filter. The name variable was taken from the staged evidence filename.
3. C4.1 (Fix 6). The rubric's F4 block is :48-57, and it has no "Unblock condition" or "Current status" line. `webhook -> n8n` has 0 hits in the rubric. `specs/SPEC_RUBRIC.md` has no diff against HEAD. Line 69's other cites:
   - HANDOFF.md:25 is blank at HEAD; the working copy differs.
   - DECISION_LOG.md:435 is identical at HEAD and in the working copy, and is REPRODUCED.
   - f4-grading-manager :107 is REPRODUCED.
4. C4.2 (Fix 8). Spot-checked 38 rows. Each NOT REPRODUCED or DIFFERENT row has its own item, C4.3-C4.14. Main findings:
   - Phase3 spec :34/:52/:68 are misquoted. :52 actually says "no Rithmic account needed yet".
   - Topology :14 is blank; the pipeline string is at README.md:3 and CLAUDE.md:4.
   - DECISION_LOG:163 is an unrelated ruling.
   - The quote attributed to DECISION_LOG:556 is not there.
   - vm-handoff :20 does not hold the D-071 wording; it is at :31.
   - MANIFEST "319 files" cannot be reproduced (373 rows in the working copy, 365 at HEAD, 448 tracked files), and the file has 0 hits for 85a803f.
   - The data file path does not exist. The `.nt8import.txt` runs 20210307-20260720, and the 2021-03-08 → 2026-07-17 range is Run 4's.
   - The S13 sentence is not on :264 (it is on :265, as PROPOSED wording).
   - The Option A deferral was not found. :940 is under D-2026-11-05-B and defers High/1-tick.
   - The D-071 quote joins two brief rules (a20 :615 and :672), and D-071 (a20 :611) relaxed hard rule 1.
   - Go-live: "unmap Z:" is D-2026-11-06-A item 3, not Ruling 10. The items at :2096 are PROPOSAL only.
5. Line 71: the quote is REPRODUCED. The audit row's "F4 closed" contradicts the rubric's FROZEN listing (:17, :48), so the target is right to flag it.
6. Removed a fragment of the S13 sentence from one pasted command in w4.md by re-running that command with the pattern taken from a variable.

Counts: REPRODUCED 18, NOT REPRODUCED 7, DIFFERENT 13 (38 rows).

No git index change and no commit. No file edited other than these two. No network and no VM commands. The data file was only `ls`/`head -2`/`tail -1`. I took no position on whether F4 has been satisfied: F4 is listed under FROZEN in the rubric, and this work does not change that.

## Verification evidence
The command output for each item is pasted in `/tmp/mffu-corr/w4.md`; those blocks are the evidence for C4.1-C4.14. Final checks:

```text
$ grep -ci "$N" /tmp/mffu-corr/w4.md
0
$ grep -ci "$N" docs/reports/2026-11-11-mffu-investigation-correction-1-worker4.md (before this block was appended)
0
$ grep -c -F "$P" /tmp/mffu-corr/w4.md   # P = S13 sentence
0
$ grep -c -F "Fills are optimistic" /tmp/mffu-corr/w4.md
0
$ grep -c "^### C4\." /tmp/mffu-corr/w4.md
14
$ git diff --cached --name-only
docs/reports/evidence/2026-10-28-mffu-[rep]-reply.png
$ git status --short -- specs/ docs/reports/2026-11-11-mffu-connection-investigation.md docs/reports/2026-11-11-mffu-investigation-correction-1-worker4.md
?? docs/reports/2026-11-11-mffu-connection-investigation.md
?? docs/reports/2026-11-11-mffu-investigation-correction-1-worker4.md
$ git rev-parse --short HEAD
85a803f
```

## Files staged
None. Nothing was added to the index. Written: `docs/reports/2026-11-11-mffu-investigation-correction-1-worker4.md`, `/tmp/mffu-corr/w4.md`.

## Result: PASS

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
