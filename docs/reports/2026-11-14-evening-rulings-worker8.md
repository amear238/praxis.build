# Worker 8: adversarial review of D-2026-11-13-D / -E (v2 -> v3 delta)

## Task
Find where the v3 changes to /tmp/praxis-rl/entries.md (vs entries.v2.md) fail items 1-4 of the brief. Fix nothing.

## Mode
ADVERSARIAL

## Criterion
S1 (quotes byte-present, evidence pasted), S2/S8 (no over-credit, no answering Amear's questions, inferences labelled), referenced files exist, staging mechanics exact.

## Defects

1. **BLOCKING (mechanics, item 4). HEAD moved during this review.** The brief names HEAD 9ff8a48. Current HEAD is `b1815d2` (committed 2026-11-13T20:58:01-05:00, "docs: file the 2026-11-13 strategy-review evidence index"). It adds docs/reports/2026-11-13-hermes-handoff-strategy-search.md and 14 other reports, plus 15 MANIFEST rows. /tmp/praxis-rl/idx was built at 20:56:50 on 9ff8a48. Run as written (against HEAD), `--cached --name-status` is NOT `M	DECISIONS.md` alone. It shows `M MANIFEST.md` plus 15 `D` rows. Committing this index would revert b1815d2. Against 9ff8a48 the index is exact (`M	DECISIONS.md`, `160	0`). b1815d2 does not touch DECISIONS.md (count 0), so the blob and entries still fit. The index needs a rebuild on b1815d2 before any commit. That is the manager's call.
2. **MINOR (item 1/S1, line 78 pointer).** Line 78 says the 2a/2b greps' "commands and output" are in worker5 "Q5". The `## Q5` section (worker5 :573-:579) has findings only and no commands. The commands are in `### Batch 6 (Q5 tests 2a/2b, NEEDS AMEAR 6)` (:390): `git grep ... HEAD -- DECISIONS.md docs/reports vm` at :407 and `grep ... DECISION_LOG.md` at :439. So the four paths named are covered. The pasted output is truncated, though: `head -30` of 115 hits, and `tail -15` for DECISION_LOG. I re-ran the HEAD grep and read hits 31-115. None of them records a pass, so the "found none" claim holds for DECISIONS/docs/reports/vm. I did not grep DECISION_LOG beyond :942-:944, per the brief.
3. **MINOR (item 1, line 82).** The D7 quote "pull R6's research (higher-win-rate, steadier-equity strategies) forward to P0" wraps across a line break at DECISIONS.md :1942-:1943 (`strategies)\n    forward`). It is present only after whitespace normalisation, not byte-for-byte.
4. **MINOR (S2, line 70).** "A separately named 0930 template on the VM ... its hours have not been read back" states as fact two things that are not labelled. (a) The template's existence is REPORTED BY Amear through vm-queue :11, which the previous sentence attributes. (b) The absence of a readback is an absence claim with no OBSERVED label. It is supported: `git grep 'RTH 0930' HEAD` hits only vm-queue :11, and worker5 F2 says "No T7 hours readback exists".
5. **Reviewer's own breach, disclosed.** My check command ran `git write-tree` with `GIT_INDEX_FILE=/tmp/praxis-rl/idx`. That rewrote the index file: mtime 20:56:50 -> 20:58:34, the cache-tree extension. The entries did not change: still 524 paths, and DECISIONS.md is still `2ff4d360ac279e21b317cf7125990cc3a05b3e1c`. The diff and hashes below are unaffected. It also wrote one tree object to the object DB.

## Per-item results

- **Delta scope: PASS.** `diff <(diff entries.v2.md entries.md) v2-v3.diff` gives SAME. Changed lines: 4, 68, 70, 78, 80, 82, 154. Both files are 160 lines.
- **Item 1 quotes: PASS with MINOR 2 and 3.** All of these are byte-present at the cited source: DECISION_LOG :944 "The rulings as the handoff lists them at :40-:45" and "which Amear pasted into this session and then approved here". vm-queue :5 "the VM Claude Code session's own report" and "VM Claude Code session". :11 "PRAXIS baseline NQCONTROW 0930" and "CME US Index Futures RTH 0930 ET". :29 "is not installed on the VM" and `claude`. DECISIONS :1010 "The in-VM automation approach". :1015 "no record of either being run". :2076 D-2026-11-10-C. R1 :1552-:1553 "live" and "CME US Index Futures RTH". `bd show Praxis_build-ckh` (normalised) "D-2026-11-08-D D7 fired on D6 (f10603a)" and "A human resumes". D7 holds after normalisation only. The handoff's ruling list is at :41-:45, with :40 as the list header, so the entry's ":41-:45" and its quote of DLOG's ":40-:45" are both accurate.
- **Item 2 S2/S8: PASS with MINOR 4.** Line 68 labels its tension reading and adds INFERRED. Line 78 labels "binding every agent" INFERRED and leaves the :1010-vs-:2076 tension and the session-rerun question to Amear. "D-2026-11-10-C treats driving the VM over SSH as distinct from an agent inside the VM" is supported by D-2026-11-10-C's "in place of the Claude agent inside the VM". No changed sentence credits Amear beyond his quoted words.
- **Item 3 files: PASS.** worker2, worker5 and worker6 exist. The manager report does not exist, and entries.md has 0 references to it.
- **Item 4 mechanics: FAIL against current HEAD b1815d2 (defect 1). PASS against stated base 9ff8a48.** Blob prefix vs HEAD DECISIONS: EMPTY (2365 lines). Blob tail = entries: EQUAL. Working-tree tail 160 = entries: EQUAL. Working-tree prefix vs DECISIONS.wt.before: IDENTICAL (cmp). Blob hash = index entry: 2ff4d360... Each entry ends with the fills line once (lines 92 and 160, entry headers at 2 and 94). Rep-name count: 0 in entries, 0 in the diff.

## Verification evidence (pasted)

```
$ GIT_INDEX_FILE=/tmp/praxis-rl/idx git diff --cached --name-status      # vs HEAD = b1815d2
M	DECISIONS.md
M	MANIFEST.md
D	docs/reports/2026-11-13-hermes-handoff-strategy-search.md
... (14 more D rows: research-filing-cure-manager/-worker1, research-filing-manager, research-filing-resume-worker1/-worker2, strategy-review-index-manager, -worker1..-worker7, voice-handoff-strategy-review)
numstat: 160 0 DECISIONS.md | 0 15 MANIFEST.md | 0 113 hermes-handoff ...
$ GIT_INDEX_FILE=/tmp/praxis-rl/idx git diff --cached --no-ext-diff --no-textconv --no-color --text --ignore-submodules=none --no-relative | shasum -a 256
09da6189824df9773c4b3f35b219bef258e4b21c147fe8040f194ce8b15b626b  -
$ ... same with base 9ff8a48:
M	DECISIONS.md
160	0	DECISIONS.md
4c95a61b00a03abdf4c0d1146628985e1b95bdc2cc6245cbd8484b79317ac678  -
$ git log -2 --format='%h %cI'
b1815d2 2026-11-13T20:58:01-05:00
9ff8a48 2026-11-13T15:36:25-05:00
$ stat idx (before my write-tree): Nov 13 20:56:50 2026
$ git hash-object /tmp/praxis-rl/DECISIONS.blob
2ff4d360ac279e21b317cf7125990cc3a05b3e1c
100644 2ff4d360ac279e21b317cf7125990cc3a05b3e1c 0	DECISIONS.md
$ git grep -n -i -E 'test 2a|test 2b|2a and 2b|tests 2a|2a pass|2b pass' HEAD -- DECISIONS.md docs/reports vm | wc -l
115
```

## Files staged
None. The only file written is this report, and it is not staged.

## Result: FAIL
FAIL on defect 1 only: the index base is stale against the moved HEAD. The text of the v3 delta has no blocking defect.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
