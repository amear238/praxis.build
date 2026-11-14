# 2026-11-14 evening rulings: worker 9 adversarial review (v4 entries)

## Task
Adversarial review of /tmp/praxis-rl/entries.md (v4, D-2026-11-13-D and D-2026-11-13-E), checked against v3 (/tmp/praxis-rl/entries.v3.md), the stored change set (/tmp/praxis-rl/v3-v4.diff) and HEAD b1815d2.

## Mode
ADVERSARIAL, read-only. I edited no tracked file, did not touch /tmp/praxis-rl/*, did not run `git write-tree` and made no commit. Every command that could print the rep's name was piped through a sed mask. Counts only.

## Criterion
Brief items 1 (the changed lines' claims are true, and nothing inferred is stated as fact without a label) and 2 (mechanics on the current HEAD).

## Process log
- Call 1: all mechanical checks, the stored diff and the handoff, DECISION_LOG, worker5 and DECISIONS checks.
- Call 2: report skeleton.
- Call 3: where the handoff was committed, the unit name, leftover `9ff8a48` strings, the handoff quotes, worker5 headings and Batch 3.
- Call 4: the scope of worker5's Batch 3 and Batch 4 searches, the Batch 6 commands, and the Q4/Q5 findings.
- Call 5: the DECISION_LOG :942-:944 quotes, the truncation of worker5's T7 grep, and DECISIONS :1010/:1015.

## Verification evidence (pasted output, rep name masked as [REP]; none occurred)

### Item 1
```
$ git rev-parse HEAD
b1815d2bb8d9df74f94f262a4cdaa1a2f5da8767
$ diff /tmp/praxis-rl/entries.v3.md /tmp/praxis-rl/entries.md > d.out; echo rc=$?; cmp d.out /tmp/praxis-rl/v3-v4.diff && echo STORED_DIFF_EQUAL
diff rc=1
STORED_DIFF_EQUAL
(hunks: 6c6, 70c70, 76c76, 78c78, 82c82, 98c98)
$ git show b1815d2:docs/reports/2026-11-13-hermes-handoff-strategy-search.md | cmp - docs/reports/2026-11-13-hermes-handoff-strategy-search.md && echo HANDOFF_IDENTICAL
HANDOFF_IDENTICAL
$ git log --format="%h %s" --diff-filter=A -- docs/reports/2026-11-13-hermes-handoff-strategy-search.md
b1815d2 docs: file the 2026-11-13 strategy-review evidence index (...), the Claude.ai channel Hermes handoff, ...
$ git show -s --format=%B b1815d2 | grep -c "strategy-review-filing"
1
$ git show b1815d2:DECISION_LOG.md | wc -l
     921
$ git show --stat --format= b1815d2 | grep -c DECISIONS.md
0
$ grep -n "9ff8a48" /tmp/praxis-rl/entries.md
(no output)
$ sed -n 390p docs/reports/2026-11-14-evening-rulings-worker5.md
### Batch 6 (Q5 tests 2a/2b, NEEDS AMEAR 6)
$ grep -n "Batch 3" docs/reports/2026-11-14-evening-rulings-worker5.md
199:### Batch 3 (VM queue results, session close, T7)
$ git show HEAD:DECISIONS.md | sed -n 1940,1944p
D7  If D6 fails at every tier at 1 MNQ: do not design breaker values
    to fit the drawdown ceiling (that is curve-fitting). Report it, and
    pull R6's research (higher-win-rate, steadier-equity strategies)
    forward to P0. The Noise-Area baseline continues through the VM
    tests for the record, but a GO on MFFU is not expected from it.
handoff quotes: "changed the parameters ... 9:30 a.m. onwards" => 13; "the back tests from November the first ... 8:30 a.m." => 13;
"I didn't lift it." => 14; "Those rules are for you, not for me." => 14 45; "I just manually put it in there." => 14
DECISION_LOG working copy: 942 [2026-11-14T01:25:40Z] WHO: amear; 943 [2026-11-14T01:27:05Z] WHO: praxis-master;
944 [2026-11-14T01:28:05Z] WHO: amear | REPORTED BY: the Claude.ai channel
quotes "go from here ... i have approved" => 942; "The contender bar and the overfitting guard (handoff :71-:88) are PROPOSED BY the channel, not Amear" => 944;
"(b) the five 2026-11-13 evening rulings ..." => 942; "start the strategy search loop (step 4)" => 942
worker5 Batch 6 commands: git grep ... 'test 2a|test 2b|...' HEAD -- DECISIONS.md docs/reports vm | head -30 ; grep ... DECISION_LOG.md
worker5 Batch 3 T7 grep (git grep -n -i 'T7' HEAD -- DECISIONS.md docs/reports | grep ... | head): HEAD: hits printed = 10
```

### Item 2
```
$ diff <(git show HEAD:DECISIONS.md) <(head -n 2365 /tmp/praxis-rl/DECISIONS.blob) && echo HEAD_PREFIX_EMPTY_DIFF
HEAD_PREFIX_EMPTY_DIFF
line counts: HEAD:DECISIONS.md 2365; blob 2525; entries.md 160; working DECISIONS.md 2617; DECISIONS.wt.before 2457
$ diff <(tail -n +2366 /tmp/praxis-rl/DECISIONS.blob) /tmp/praxis-rl/entries.md && echo BLOB_TAIL_EQ_ENTRIES
BLOB_TAIL_EQ_ENTRIES
$ diff <(tail -n 160 DECISIONS.md) /tmp/praxis-rl/entries.md && echo WT_TAIL_EQ_ENTRIES
WT_TAIL_EQ_ENTRIES
$ diff <(head -n 2457 DECISIONS.md) /tmp/praxis-rl/DECISIONS.wt.before && echo WT_HEAD_EQ_BEFORE
WT_HEAD_EQ_BEFORE
$ cmp <(head -c $(wc -c < DECISIONS.wt.before) DECISIONS.md) DECISIONS.wt.before && echo WT_BYTE_PREFIX_EQ
WT_BYTE_PREFIX_EQ
last byte of wt.before, entries.md and DECISIONS.md: 0a, 0a, 0a
$ GIT_INDEX_FILE=/tmp/praxis-rl/idx git diff --cached --name-status | od -c
0000000    M  \t   D   E   C   I   S   I   O   N   S   .   m   d  \n
$ GIT_INDEX_FILE=/tmp/praxis-rl/idx git diff --cached --numstat
160	0	DECISIONS.md
$ GIT_INDEX_FILE=/tmp/praxis-rl/idx git diff --cached --no-ext-diff --no-textconv --no-color --text --ignore-submodules=none --no-relative | shasum -a 256
15a82622361b5ae5187f7ce78038cee81d408ca39db8c225bafd8f6f7b6b3842  -
$ git hash-object /tmp/praxis-rl/DECISIONS.blob
a25ff42f504f8b3fb5f03b348bdc69cc9b57e577
$ GIT_INDEX_FILE=/tmp/praxis-rl/idx git ls-files -s DECISIONS.md
100644 a25ff42f504f8b3fb5f03b348bdc69cc9b57e577 0	DECISIONS.md
$ git grep -n -E "D-2026-11-13-[DE]" HEAD | wc -l
       0
rep-name count: entries.md 0; DECISIONS.blob 0; HEAD:DECISIONS.md 0
fills lines in entries.md: line 92 (ends D-2026-11-13-D, next heading at 94) and line 160 (ends D-2026-11-13-E, the last line); one per entry
```

## Per-item results
- 1a. The diff equals the stored diff: PASS.
- 1b. The HEAD `b1815d2` claims (hunks 6 and 98): 921 lines, and the handoff is committed in b1815d2 under the named unit and byte-identical to the working copy: PASS. No `9ff8a48` remains.
- 1c. The worker5 citations (hunks 70 and 78): Batch 6 is at :390 and Batch 3 at :199, with findings under Q5 at :573: PASS, but see defect 1.
- 1d. The D7 joins (hunks 76 and 82): the whitespace-joined text of :1942-:1943 and :1943-:1944 matches both quotes: PASS. The quotes start partway through line :1943, so the joins hold only once the four-space indent is stripped. "Joined with one space" is accurate under that reading. This is not a defect.
- 1e. Inference labels: PASS, except for defect 1.
- 2. Mechanics: PASS on every check.

## Defects
1. MINOR (ruling 4, hunk 70). The new sentence reads "No readback of its hours was found in the record searched (OBSERVED for those paths; worker5 Batch 3)". It has three weaknesses:
   - (a) The entry never names "those paths". A reader has to open worker5 to learn the scope of the OBSERVED label.
   - (b) Batch 3's T7 search (`git grep -n -i 'T7' HEAD -- DECISIONS.md docs/reports | grep -i -E 'template|readback|08:30|09:30' | head`) printed exactly 10 hits. That is the `head` limit, so its output was truncated, and an absence on those paths was not fully observed. The template-hours search was keyword-bound ('session template|trading hours template|template hours') and limited to `docs/reports/2026-11-13*.md` and `vm`.
   - (c) worker5's own finding (Q4 item 4) covers "the live template's hours". Applying it to the separately named 0930 template is the filer's step, and it carries no label.
   The claim is hedged ("in the record searched"), so this does not block. Suggested fix, not applied: name the paths, or add "(search truncated at 10 hits; INFERRED for the 0930 template)".

No BLOCKING defects.

## Files staged
None. The only file written is this report. It is untracked and not added to the index.

Result: PASS

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
