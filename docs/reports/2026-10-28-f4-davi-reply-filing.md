# F4 evidence filing — MFFU "Davi" reply (screenshot)

**Date.** 2026-10-28 · **Manager.** praxis-manager · **HEAD at start and end.** `fc77f36`
**Authorisation of record.** `DECISION_LOG.md` row `2026-10-28T20:54:29Z`, `WHO: amear`.
That row is in the worktree but **not in the index** (see V9). Staging it is a ledger
action outside this unit's brief and is flagged to the master.

## Task

File Amear's screenshot of an MFFU support reply ("Davi") as F4 evidence:
1. a byte-identical copy plus hashes;
2. a verbatim transcript, with an adversarial check;
3. an append-only addendum to `docs/reports/2026-08-07-f4-mffu-compliance-evidence.md`;
4. this report;
5. staging of those four paths only.

This unit does **not** grade F4, does **not** unfreeze it, and does not assess PRAXIS
against the reply's conditions. No email was touched and no URL was fetched.

## Rubric criteria addressed

Verbatim from `specs/SPEC_RUBRIC.md`:
- S1: "Every claim in a report has pasted command output, not a description of output."
- S2: "No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure."
- S7: "Nothing is committed while any audit box is unchecked."
- S8: "No question that belongs to Amear is answered on his behalf."

F4 is subject matter only: "Written confirmation from MFFU that this specific automation
pattern is permitted on a funded account." F4 is not graded here.

## Workers dispatched

| # | Mode | Scope | Outcome |
|---|---|---|---|
| W1 | BUILD | Copy the PNG and hash it; write the verbatim transcript | PASS. Report `docs/reports/2026-10-28-f4-davi-reply-worker1.md` |
| W2 | ADVERSARIAL | Transcript vs image, line by line | `VERDICT: DISCREPANCIES FOUND (2)`, both in prose outside the fence. Report `...-adversarial-transcript.md` |
| W3 | BUILD | Append the addendum (sections A–F) | PASS. Report `...-worker3.md` |
| W4 | ADVERSARIAL | Addendum vs criteria and required content | `DEFECTS FOUND (0 blocking, 4 minor)`. Report `...-adversarial-addendum.md` |
| W5 | BUILD (fix) | The 4 W4 defects | PASS. Report `...-worker5-fix.md` |
| W6 | ADVERSARIAL | Re-check of the W5 fixes | `DEFECTS FOUND (0 blocking, 5 minor)`. Report `...-adversarial-recheck.md` |
| W7 | BUILD (fix) | The 5 W6 defects | PASS. Report `...-worker7-fix.md` |
| W8 | ADVERSARIAL | Full final pass | `DEFECTS FOUND (1 blocking, 4 minor)`. Report `...-adversarial-final.md` |
| W9 | BUILD (fix) | The W8 blocking defect and 4 minor defects | PASS. Report `...-worker9-fix.md` |
| W10 | ADVERSARIAL | Confirmation pass | `DEFECTS FOUND (0 blocking, 4 minor)`, `Result: PASS`. Report `...-adversarial-confirm.md` |

All worker reports are in `docs/reports/` with the prefix `2026-10-28-f4-davi-reply-`.
They are untracked and **not staged**, because the brief limits staging to four paths.
Every adversarial worker received the artifact and the criteria only, never a builder's
reasoning.

## Process log

1. I read the rubric, viewed the image myself, and read F4 report §§0, 1, 3, 9 and the
   authorising row. I captured the baseline (V0).
2. I made independent zoomed crops of the preview line, the sender, the body and the URL
   to have my own reading before any worker returned.
3. **W1** returned. I re-ran the hashes and `cmp` and read the transcript (V1). Its summary
   rendered `&lt;`; I checked the file: 0 HTML entities.
4. **W2** found 2 discrepancies in the prose outside the fence:
   - the avatar was described as "grey", but the figure is green;
   - "ends mid-word" was an inference.

   I confirmed both on my own crops and fixed them as two single-line edits. The fence
   stayed byte-identical (V2).
5. I ran the vendor-term search with a positive control (V3) and hashed the F4 report
   before the append (V4).
6. **W3** appended the addendum. I re-ran the append-only proof and the search, and
   tripped three negative tests (V5).
7. **W4** found 4 minor defects:
   - a quote-provenance sentence was false;
   - a Tradovate reading was stated as fact;
   - there were unobservable "no agent" universals;
   - the middle opener was omitted.

   I re-verified all four. **W5** fixed them.
8. **W6** found 5 minor defects:
   - the universals were still unscoped;
   - there was a "most natural reading" judgment;
   - "opens twice" sat next to three quoted openers;
   - a quoted string was not in the transcript;
   - "never mentions" overreached hidden content.

   I re-verified all five. **W7** fixed them. I then fixed one leftover row-1
   inconsistency myself, a single line: "is a **general** permission" became a reading
   left to Amear.
9. **W8** found **1 blocking** defect: "one explicit grant" settled Amear's S8 reading. It
   also found 4 minor ones:
   - "New conditions";
   - §1.1 attributed to Frank;
   - unattested non-fetch and non-draft claims;
   - the pattern line was not CLAUDE.md's wording.

   I re-verified all five. **W9** fixed them with exact replacement text.
10. **W10** found 0 blocking and 4 minor:
    - grant-counting wording;
    - the row-1 "either reading" logic;
    - unlabelled non-fetch claims;
    - "preceding message" against the position disclaimer.

    **I fixed these four myself as single-line edits** (V6). **Disclosure:** that last
    set of manager edits got mechanical verification only. No further adversarial pass
    ran on it. The master's auditor is the next independent check.
11. I staged the three evidence paths, then this report (V8).
12. **Stop-gate race (observed, not repaired).** `scripts/gate-manager-output.sh` grades
    the newest `.md` in `docs/reports/` (`ls -t ... | head -1`). With a concurrent
    manager and workers writing reports, it twice graded files that were not mine. One
    was `...nightly-checks-plan-review-note.md`, which I am forbidden to touch. The other
    was a worker's adversarial report. I did not edit either one. I kept this report the
    newest file instead.

## Verification evidence

### V0. Baseline (start of unit)

```
$ git rev-parse --short HEAD && git diff --cached --name-only && echo "COUNT: $(git diff --cached --name-only | wc -l)"
fc77f36
DECISION_LOG.md
ISSUE_REGISTER.md
MANIFEST.md
docs/reports/2026-08-06-session42-r8j-phase3-import.md
docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
docs/reports/2026-08-07-session44-r8j-offset-correction-adversarial.md
docs/reports/2026-08-07-session44-r8j-offset-correction-worker1.md
docs/reports/2026-08-07-session44-r8j-offset-correction.md
docs/specs/2026-08-08-ledger-compaction-spec.md
COUNT:        9
$ ls -l /Users/admin/Desktop/Screenshot\ 2026-10-28\ at\ 4.53.23*
-rw-r--r--@ 1 admin  staff  254350 Oct 28 16:53 /Users/admin/Desktop/Screenshot 2026-10-28 at 4.53.23 PM.png
$ shasum -a 256 /Users/admin/Desktop/Screenshot\ 2026-10-28\ at\ 4.53.23*
15af54100ba44ddfe67dda5698c4a80ba6a93f5470c5e148cd6043dc92302992  /Users/admin/Desktop/Screenshot 2026-10-28 at 4.53.23 PM.png
```

### V1. Copy is byte-identical; transcript has no HTML entities (manager re-run after W1)

```
15af54100ba44ddfe67dda5698c4a80ba6a93f5470c5e148cd6043dc92302992  /Users/admin/Desktop/Screenshot 2026-10-28 at 4.53.23 PM.png
15af54100ba44ddfe67dda5698c4a80ba6a93f5470c5e148cd6043dc92302992  docs/reports/evidence/2026-10-28-mffu-davi-reply.png
-rw-r--r--@ 1 admin  staff  254350 Oct 28 16:53 /Users/admin/Desktop/Screenshot 2026-10-28 at 4.53.23 PM.png
-rw-r--r--@ 1 admin  staff  254350 Oct 28 16:53 docs/reports/evidence/2026-10-28-mffu-davi-reply.png
IDENTICAL
$ grep -c '&lt;\|&gt;\|&amp;' docs/reports/evidence/2026-10-28-mffu-davi-reply-transcript.md
0
```

### V2. Transcript fence unchanged by the prose fixes

`fence.txt` was extracted right after W1. `fence6.txt` was extracted at the end of the
unit.

```
$ cmp $S/fence.txt $S/fence6.txt && echo FENCE-UNCHANGED
FENCE-UNCHANGED
8e14a6904fbdcdc85cc3b264a462c3a474fa309ca26942fa7430cfbcd7932dd3  .../scratchpad/fence6.txt
```

### V3. Vendor-term search on the transcript fence, with a positive control

`grep -c` counts lines, not occurrences.

```
      25
NinjaTrader	0
NT8	0
Ninja	0
Rithmic	0
webhook	0
n8n	0
TradingView	0
Tradovate	2
API	2
Tradovate occurrences in fence:        3
positive-control NinjaTrader  CLAUDE.md lines=2
positive-control Rithmic      CLAUDE.md lines=3
positive-control webhook      CLAUDE.md lines=1
positive-control n8n          CLAUDE.md lines=4
```

### V4. F4 report before the append

```
$ wc -l < F; shasum -a 256 F; git show :F | shasum -a 256; git diff --quiet -- F && echo WORKTREE==INDEX
     537
ffda2e095083802c59c951ed72da79bb978acb7cdd38e6437578b09b42c84cb1  docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
ffda2e095083802c59c951ed72da79bb978acb7cdd38e6437578b09b42c84cb1  -
WORKTREE==INDEX
```

### V5. Negative tests: each check trips on a planted defect

```
--- NEGATIVE TEST 1: append-only check trips on a one-byte edit above line 537
0993020b8be4fd0ce5f7d3d4ce448f3061ffdd52e4b8f0e80f4805a24c11600d  -
expected ffda2e095083802c59c951ed72da79bb978acb7cdd38e6437578b09b42c84cb1
--- NEGATIVE TEST 2: forbidden-wording sweep fires on a planted sentence
760:This reply effectively confirms the PRAXIS pattern.
--- same sweep on the real file:
(end; empty = no hits)
--- NEGATIVE TEST 3: fence cmp trips on a one-char change
.../mgrfence.txt .../negfence.txt differ: char 280, line 7
cmp DETECTED CHANGE
```

### V6. Final state of the addendum (manager re-run after the last edits)

```
== append-only
ffda2e095083802c59c951ed72da79bb978acb7cdd38e6437578b09b42c84cb1  -
     776
239	0	docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
== fence
FENCE-UNCHANGED
8e14a6904fbdcdc85cc3b264a462c3a474fa309ca26942fa7430cfbcd7932dd3  .../scratchpad/fence6.txt
== quote lines after 537 (count of fence hits : number of quotes)
  17 1
== heading present
541:## Addendum 2026-10-28 — MFFU "Davi" reply (screenshot)
== stale/forbidden (expect none)
(end)
== verdict rows
| F4 "this specific automation pattern" (and §3.5, specific vs general) | **DOES NOT ADDRESS**
| F4 "on a funded account" | **PARTLY ADDRESSES**
| §3.2 effective date | **DOES NOT ADDRESS**
| §3.2 retroactivity / "on this account" | **DOES NOT ADDRESS**
== hashes
15af54100ba44ddfe67dda5698c4a80ba6a93f5470c5e148cd6043dc92302992  /Users/admin/Desktop/Screenshot 2026-10-28 at 4.53.23 PM.png
15af54100ba44ddfe67dda5698c4a80ba6a93f5470c5e148cd6043dc92302992  docs/reports/evidence/2026-10-28-mffu-davi-reply.png
IDENTICAL
```

The forbidden and stale sweep pattern:
`one explicit grant|only grant in|unqualified|On either reading|preceding message|New conditions|from Frank's relay|most natural|opens twice|<placeholder>|effectively|confirms the PRAXIS|satisfies F4|F4 is (met|satisfied|cleared)`

Here `<placeholder>` stands for the three-letter "to be determined" token. It is spelled
out in the actual command but omitted from this report, because the stop gate rejects any
report that contains it.

The sweep is restricted to lines after 537. Line 142, which is frozen history about
Frank's relay, still says "a **general** permission". That is correct and untouched.

### V7. SPEC_RUBRIC.md not touched by this unit

```
$ stat -f '%Sm %N' -t '%Y-%m-%dT%H:%M:%S' specs/SPEC_RUBRIC.md DECISION_LOG.md docs/reports/evidence/2026-10-28-mffu-davi-reply.png; date
2026-07-30T11:50:39 specs/SPEC_RUBRIC.md
2026-10-28T17:13:45 DECISION_LOG.md
2026-10-28T16:53:29 docs/reports/evidence/2026-10-28-mffu-davi-reply.png
2026-10-28T17:24:08 now
```

The rubric's pre-existing worktree diff (` M` at session start) predates this unit.

**Observation, not diagnosed:** DECISION_LOG.md was modified at 17:13:45, during this
unit. Neither I nor any brief in this unit wrote to it; every brief forbade ledger
writes. The writer is not established here. It may have been the master or the
concurrent manager.

### V8. Staging: before and after

The brief expected 9 paths before staging. **I observed 11.** The concurrent manager had
staged its two `nightly-checks-plan-review` files during this unit; I did not touch them.

```
== BEFORE
DECISION_LOG.md
ISSUE_REGISTER.md
MANIFEST.md
docs/reports/2026-08-06-session42-r8j-phase3-import.md
docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
docs/reports/2026-08-07-session44-r8j-offset-correction-adversarial.md
docs/reports/2026-08-07-session44-r8j-offset-correction-worker1.md
docs/reports/2026-08-07-session44-r8j-offset-correction.md
docs/reports/2026-10-28-nightly-checks-plan-review-note.md
docs/reports/2026-10-28-nightly-checks-plan-review-rebuild.md
docs/specs/2026-08-08-ledger-compaction-spec.md
COUNT:       11
$ git add -- docs/reports/evidence/2026-10-28-mffu-davi-reply.png docs/reports/evidence/2026-10-28-mffu-davi-reply-transcript.md docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
== AFTER (manager report not yet added)
...(11 above) + docs/reports/evidence/2026-10-28-mffu-davi-reply-transcript.md, docs/reports/evidence/2026-10-28-mffu-davi-reply.png
COUNT:       13
F4 report: worktree==index
ffda2e095083802c59c951ed72da79bb978acb7cdd38e6437578b09b42c84cb1  -   (index copy, head -n 537)
15af54100ba44ddfe67dda5698c4a80ba6a93f5470c5e148cd6043dc92302992  -   (index copy of the PNG)
```

The F4 report was already staged at 537 lines. Its worktree-vs-index diff before
`git add` was `239 0`, all of it this addendum. So staging the path added nothing from
any other unit.

The final list, captured after this report was staged, is in V10.

### V9. Authorising row not in the index

```
index: 0
worktree: 1
259	0	DECISION_LOG.md      (unstaged worktree diff)
118	0	DECISION_LOG.md      (staged diff)
```

### V10. Final staged list (captured after this report was staged)

Count: 11 observed before, plus 3 new paths, gives 14. The F4 report was already staged.

```
$ git add -- docs/reports/2026-10-28-f4-davi-reply-filing.md && git diff --cached --name-only && echo "COUNT: ..."
DECISION_LOG.md
ISSUE_REGISTER.md
MANIFEST.md
docs/reports/2026-08-06-session42-r8j-phase3-import.md
docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
docs/reports/2026-08-07-session44-r8j-offset-correction-adversarial.md
docs/reports/2026-08-07-session44-r8j-offset-correction-worker1.md
docs/reports/2026-08-07-session44-r8j-offset-correction.md
docs/reports/2026-10-28-f4-davi-reply-filing.md
docs/reports/2026-10-28-nightly-checks-plan-review-note.md
docs/reports/2026-10-28-nightly-checks-plan-review-rebuild.md
docs/reports/evidence/2026-10-28-mffu-davi-reply-transcript.md
docs/reports/evidence/2026-10-28-mffu-davi-reply.png
docs/specs/2026-08-08-ledger-compaction-spec.md
COUNT:       14
all 4: worktree==index
fc77f36
```

This report was re-staged after V10 was added to it.

## Adversarial findings and their disposition

| Round | Finding | Severity | Manager re-verified | Disposition |
|---|---|---|---|---|
| W2 | Avatar "grey"; the figure is green | minor | yes (crop) | fixed (manager, 1 line) |
| W2 | "ends mid-word" is an inference | minor | yes (crop) | fixed (manager, 1 line) |
| W4 | Provenance said every quote came from the fence, but Frank's §1 line did not | minor | yes (`grep -Fc` = 0) | fixed (W5) |
| W4 | The Tradovate reading of "Tradovate evaluation and funded accounts" was stated as fact | minor | yes | fixed (W5); W7 then removed the remaining "most natural" judgment |
| W4 | "No agent …" universals | minor | yes | scoped (W5, W7), then made an attested basis (W9) |
| W4 | Middle opener omitted | minor | yes | fixed (W5, W7) |
| W6 | "Gmail connector unavailable" unattributed | minor | yes | attributed to the master's brief (W7, and manager on transcript line 6) |
| W6 | "Opens twice" next to three openers | minor | yes | fixed (W7) |
| W6 | A quoted string not in the transcript | minor | yes (`grep` = 0) | replaced with backtick fragments, each `grep -Fc` = 1 (W7) |
| W6 | "never mentions" / "anywhere" overreach possible hidden content | minor | yes (transcript line 70) | scoped to the visible text, and an UNVERIFIED bullet added (W7) |
| W8 | "one explicit grant" settles Amear's S8 reading | **BLOCKING** | yes | fixed (W9), then tightened (manager) |
| W8 | "New conditions" heading; §1.1 attributed to Frank; unattested claims; pattern not verbatim from CLAUDE.md | minor | yes (CLAUDE.md:21; §1.1 has 0 "Frank") | fixed (W9); both CLAUDE.md strings `grep -Fc` = 1 |
| W10 | Grant-counting; row-1 "either reading" logic; unlabelled non-fetch claims; "preceding message" | minor | yes | fixed (manager, single lines); **no adversarial re-pass** |
| W4/W8/W10 (out of scope) | Authorising DECISION_LOG row unstaged; evidence files were untracked | — | yes (V9) | evidence files now staged (V8). DECISION_LOG row left for the master (brief: no ledger writes, stage four paths only) |

The adversarial workers' reports agree that the verdicts were never too generous. No
round found wording that says or implies F4 is met. No round found PRAXIS assessed
against the conditions.

## S6 cross-block check

This unit files evidence. It approves no deviation and changes no spec, so there is no
approved deviation to cross-test.

The reply restates conditions that touch other blocks:
- HFT prohibited;
- no exploiting favourable sim fills, which couples to F3 and Block 2 as the existing
  F4 report §4 already records;
- CME guidelines on live accounts, which bears on Blocks 4 and 5.

Per the brief, these are recorded in addendum §D and **not assessed**. F1, F2, F3 and
O1–O4 are untouched.

## Not claimed

- F4 is not discharged, satisfied or unfrozen. `specs/SPEC_RUBRIC.md` is untouched (V7).
- Whether a general or Tradovate-framed permission covers the NinjaTrader 8 / Rithmic
  path is Amear's ruling (S8). He has ruled to send MFFU a follow-up naming NinjaTrader 8
  + Rithmic (`DECISION_LOG.md` `2026-10-28T20:54:29Z`). This unit did not draft or send
  it.
- The reply's date, headers, sender authenticity and thread position are UNVERIFIED.
- MANIFEST.md was **not** updated for the two new evidence files. The brief limited
  staging to four paths, and MANIFEST.md is already staged by another unit (surgical
  staging hazard). This is flagged to the master.

## Files staged by this unit

- `docs/reports/evidence/2026-10-28-mffu-davi-reply.png` (new)
- `docs/reports/evidence/2026-10-28-mffu-davi-reply-transcript.md` (new)
- `docs/reports/2026-08-07-f4-mffu-compliance-evidence.md` (already staged; +239 lines appended)
- `docs/reports/2026-10-28-f4-davi-reply-filing.md` (this report, new)

Nothing was committed (S7). HEAD is unchanged at `fc77f36`.

## Result: PASS

This is the manager's result against the brief's deliverables and S1, S2, S7 and S8. It
is subject to the master's auditor; it is not a self-grade of F4. The caveats are
disclosed above: the last manager edits had no adversarial re-pass; the authorising row
is unstaged; MANIFEST.md was not updated.

Note 2026-11-10 under D9 (decided by manager under D-2026-11-08-D D1): the PNG named above, docs/reports/evidence/2026-10-28-mffu-davi-reply.png, is not committed, because it shows a support representative's name-bearing address; its hashes above describe a file kept off the repo. The committed transcript has that address replaced on its line 18, so the fence hash 8e14a690... above no longer matches the committed transcript. Itemised in docs/reports/2026-11-10-d9-housekeeping-manager.md.
Appended 2026-11-10 under D9 (S13): Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
