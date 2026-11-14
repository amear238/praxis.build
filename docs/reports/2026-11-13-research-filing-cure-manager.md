# Unit 2026-11-13-research-filing-cure, manager report

Date: 2026-11-13. Author: praxis-manager. Authority: DECISION_LOG.md row 2026-11-13T20:25:43Z (read with the rows at 19:40:54Z, 19:58:43Z, 20:21:12Z). HEAD 661e073. Real index: 1 staged path at start and end, not this unit's (count only, path not shown).

## Task

Cure audit FAIL 1, check 3 (de-identification) of unit 2026-11-13-research-filing: a private person's first name sat in 4 lines of two evidence reports, inside pasted command output listing the file name of an older uncommitted report (resume-manager :67, :83; worker2 :584, :594). Allowed edits: replace the name token with [rep] in those 4 lines only; one filer's note per report above its final S13 line; amend MANIFEST rows :481 and :483; rebuild /tmp/rf-manifest-blob.md. Throughout, the name was held only in a shell variable `N` derived from the F4 report's file name and never printed; every command below that touches it uses `$N` and prints counts or redacted text only.

## Rubric criteria addressed

- S1: every claim below has pasted command output.
- S2: claims are limited to what the pasted output shows (redaction of 4 lines, two inserted notes, two amended rows, blob rebuilt); no claim that the unit is audited.
- S13: the two edited reports and this report carry the S13 sentence once, as the last standalone line.

## Workers dispatched (id, mode, outcome)

| id | mode | outcome |
|---|---|---|
| worker 1 | ADVERSARIAL (cold; given the brief's Problem, Edits allowed, Proofs and the 20:25:43Z row, not the manager's reasoning) | 8 checks (a)-(h) PASS, Result: PASS, report docs/reports/2026-11-13-research-filing-cure-worker1.md (422 lines), one round |

No builder was dispatched: the three edits are line-addressed sed/awk commands, run by the manager so that no extra party handled the unredacted text. Recorded as the narrower option.

## Process log

1. 20:26:28Z: captured worker1 report sha256 before any edit.
2. Derived `N`; length 4; located the name at exactly resume-manager :67, :83 and worker2 :584, :594 (line numbers only); all occurrences lower case as derived (case-sensitive and -i counts both 2 per file).
3. Pre-copies to /tmp/rfc-pre/ (resume-manager.md, worker2.md, MANIFEST.md), sha256 equal to the working files.
4. Edit 1: `sed -i '' -e "67s/$N/[rep]/" -e "83s/$N/[rep]/"` on resume-manager; `sed -i '' -e "584s/$N/[rep]/" -e "594s/$N/[rep]/"` on worker2. Step-1 copies saved as /tmp/rfc-pre/*.step1.md.
5. Edit 2: awk inserted the note and a blank line before the final S13 line (resume-manager :695, worker2 :613 at the time), matching the files' blank-line style. Note now at resume-manager :695 (S13 :697) and worker2 :613 (S13 :615).
6. Edit 3: line-addressed sed on MANIFEST.md :481 and :483 before "; ungraded at time of row" (anchor occurs once in each row, checked).
7. Rebuilt the blob; ran all proofs; negative control on the pre-copies.
8. Dispatched the cold adversary.

Brief-conflict note: the brief says not to paste file lists over tracked modified files, and also says to paste `diff ... | grep '^>'`. The new side of worker2 :584 is itself a stat command over tracked modified files (name shown as [rep]). The specific instruction was followed; that line already exists in the edited report and the paste adds no information beyond it.

The cure manager report and the adversary report get no MANIFEST row (brief: no other MANIFEST byte changes; this report stays uncommitted).

## Verification evidence (command output)

Worker1 report sha256 at start (20:26:28Z):

```
$ shasum -a 256 docs/reports/2026-11-13-research-filing-worker1.md
ba25d8e935a9e192eed38911fdcf8f9ed92a4cb664a380eef8ee37b6628a8707  docs/reports/2026-11-13-research-filing-worker1.md
```

Pre-copies:

```
$ mkdir -p /tmp/rfc-pre && cp -p "$R" /tmp/rfc-pre/resume-manager.md && cp -p "$W" /tmp/rfc-pre/worker2.md && cp -p MANIFEST.md /tmp/rfc-pre/MANIFEST.md
$ shasum -a 256 /tmp/rfc-pre/resume-manager.md /tmp/rfc-pre/worker2.md /tmp/rfc-pre/MANIFEST.md "$R" "$W" MANIFEST.md
6ea3b42bcd458e8341d5fd1f47377844943c79d84cc780e1a48551ea774dca7b  /tmp/rfc-pre/resume-manager.md
b3bce04f2d7ef9add528756fce4990e2d9cf4dcfa255a6db3ecab82640828ea9  /tmp/rfc-pre/worker2.md
5e36b13f389c2990dbc3c649662a4f0983bd16f8a5bf23e6c0d11c32ef38593a  /tmp/rfc-pre/MANIFEST.md
6ea3b42bcd458e8341d5fd1f47377844943c79d84cc780e1a48551ea774dca7b  docs/reports/2026-11-13-research-filing-resume-manager.md
b3bce04f2d7ef9add528756fce4990e2d9cf4dcfa255a6db3ecab82640828ea9  docs/reports/2026-11-13-research-filing-worker2.md
5e36b13f389c2990dbc3c649662a4f0983bd16f8a5bf23e6c0d11c32ef38593a  MANIFEST.md
```

Edit 1 diff (pre-copy vs after edit 1; old side counted, not shown):

```
== diff /tmp/rfc-pre/resume-manager.md $R
67c67
83c83
diff ... | grep -c '^<' -> 2
>  docs/reports/2026-10-28-f4-[rep]-reply-filing.md    |  75 ++++++++++++++-
> SHA2-256(docs/reports/2026-10-28-f4-[rep]-reply-filing.md)= 222b33c2ee2bfc85a367a0691fb5872a08e02db9cf7d62394aaa14d1f13cbc69
== diff /tmp/rfc-pre/worker2.md $W
584c584
594c594
diff ... | grep -c '^<' -> 2
> $ cd /Volumes/Sensidine/Praxis.build && TZ=UTC stat -f '%Sm %N' -t '%Y-%m-%dT%H:%M:%SZ' .claude/settings.json AUDIT_LOG.md DECISIONS.md DECISION_LOG.md DISPATCH_LOG.md HANDOFF.md ISSUE_REGISTER.md MANIFEST.md STATUS.md docs/reports/2026-10-28-f4-[rep]-reply-filing.md docs/reports/2026-10-28-nightly-checks-plan-review-rebuild.md docs/specs/2026-11-05-walk-forward-spec.md docs/specs/2026-11-06-walk-forward-values.md scripts/dispatch-log-writeahead.sh /tmp/rf-diffstat-before.txt; date -u +%Y-%m-%dT%H:%M:%SZ
> 2026-11-13T17:37:18Z docs/reports/2026-10-28-f4-[rep]-reply-filing.md
docs/reports/2026-11-13-research-filing-worker2.md:0
docs/reports/2026-11-13-research-filing-resume-manager.md:0
     695 docs/reports/2026-11-13-research-filing-resume-manager.md
     613 docs/reports/2026-11-13-research-filing-worker2.md
    1308 total
```

(The last five output lines are `grep -c -i "$N" $R $W; wc -l $R $W` after edit 1.)

Edit 2 diff (after edit 1 vs final):

```
final S13 line: resume-manager :695 worker2 :613
== diff step1 -> step2 resume-manager
693a694,695
> 
> Filer's note (unit 2026-11-13-research-filing-cure, DECISION_LOG 2026-11-13T20:25:43Z): a private person's name in a file name inside pasted command output at :67 and :83 was replaced by [rep] after the output was captured; no other byte of the output changed.
== diff step1 -> step2 worker2
611a612,613
> 
> Filer's note (unit 2026-11-13-research-filing-cure, DECISION_LOG 2026-11-13T20:25:43Z): a private person's name in a file name inside pasted command output at :584 and :594 was replaced by [rep] after the output was captured; no other byte of the output changed.
```

(diff aligns the pre-existing blank line differently; the resulting order is: prior line, blank, note, blank, S13 sentence.)

```
$ grep -n -F "Filer's note (unit 2026-11-13-research-filing-cure" <two reports> | cut -c1-90
docs/reports/2026-11-13-research-filing-resume-manager.md:695:Filer's note (unit 2026-11-1
docs/reports/2026-11-13-research-filing-worker2.md:613:Filer's note (unit 2026-11-13-resea
```

Edit 3 (MANIFEST):

```
$ grep -n -F '| /docs/reports/2026-11-13-research-filing-resume-manager.md |' MANIFEST.md | cut -d: -f1; grep -n -F '| /docs/reports/2026-11-13-research-filing-worker2.md |' MANIFEST.md | cut -d: -f1
481
483
== diff /tmp/rfc-pre/MANIFEST.md MANIFEST.md
481c481
< | /docs/reports/2026-11-13-research-filing-resume-manager.md | Report | 3 | 2026-11-13 | Manager report written by praxis-manager for unit 2026-11-13-research-filing-resume (DECISION_LOG 2026-11-13T19:58:43Z), standing as the manager report of unit 2026-11-13-research-filing (DECISION_LOG 2026-11-13T19:40:54Z) after the power outage: the rebuild of the two lost received copies with sha256 compared to worker 1's pre-copy hashes, diffs of the two Downloads copies against their filed twins, S13 line counts, a PII scan, the MANIFEST row changes and blob cmp checks, the tracked-file diff comparison, and the cold adversary's grades; ungraded at time of row |
---
> | /docs/reports/2026-11-13-research-filing-resume-manager.md | Report | 3 | 2026-11-13 | Manager report written by praxis-manager for unit 2026-11-13-research-filing-resume (DECISION_LOG 2026-11-13T19:58:43Z), standing as the manager report of unit 2026-11-13-research-filing (DECISION_LOG 2026-11-13T19:40:54Z) after the power outage: the rebuild of the two lost received copies with sha256 compared to worker 1's pre-copy hashes, diffs of the two Downloads copies against their filed twins, S13 line counts, a PII scan, the MANIFEST row changes and blob cmp checks, the tracked-file diff comparison, and the cold adversary's grades; a private name in pasted output at :67 and :83 replaced by [rep] with a filer's note at :695 (unit 2026-11-13-research-filing-cure, DECISION_LOG 2026-11-13T20:25:43Z); ungraded at time of row |
483c483
< | /docs/reports/2026-11-13-research-filing-worker2.md | Report | 3 | 2026-11-13 | ADVERSARIAL worker 2 report written by praxis-worker for unit 2026-11-13-research-filing (DECISION_LOG 2026-11-13T19:40:54Z): checks (a)-(f) on worker 1's edits to the four return-handoff files, the five MANIFEST rows and the blob, including diffs against the received copies, S13 line counts, a PII scan and a diff-stat comparison; ungraded at time of row |
---
> | /docs/reports/2026-11-13-research-filing-worker2.md | Report | 3 | 2026-11-13 | ADVERSARIAL worker 2 report written by praxis-worker for unit 2026-11-13-research-filing (DECISION_LOG 2026-11-13T19:40:54Z): checks (a)-(f) on worker 1's edits to the four return-handoff files, the five MANIFEST rows and the blob, including diffs against the received copies, S13 line counts, a PII scan and a diff-stat comparison; a private name in pasted output at :584 and :594 replaced by [rep] with a filer's note at :613 (unit 2026-11-13-research-filing-cure, DECISION_LOG 2026-11-13T20:25:43Z); ungraded at time of row |
     483 MANIFEST.md
```

(The old rows contain no name; their pre-edit tail-7 count was 0.)

Blob:

```
$ git show HEAD:MANIFEST.md > /tmp/rf-manifest-blob.md && tail -n 7 MANIFEST.md >> /tmp/rf-manifest-blob.md
$ wc -l /tmp/rf-manifest-blob.md; git show HEAD:MANIFEST.md | wc -l
     460 /tmp/rf-manifest-blob.md
     453
$ head -n 453 /tmp/rf-manifest-blob.md | cmp - <(git show HEAD:MANIFEST.md); echo "cmp exit $?"
cmp exit 0
$ tail -n 7 MANIFEST.md | shasum -a 256; tail -n 7 /tmp/rf-manifest-blob.md | shasum -a 256
89909cd16815325619e82ccfb5f8ee3e856808e74ff82bc530526cc40d4dfb64  -
89909cd16815325619e82ccfb5f8ee3e856808e74ff82bc530526cc40d4dfb64  -
$ shasum -a 256 /tmp/rf-manifest-blob.md
1569e2e474e77166b93c27fbd50bd54a21434a23f5ca3d15e808461a20d9333b  /tmp/rf-manifest-blob.md
```

Zero-count, unchanged-file and S13 proofs (P=docs/reports/2026-11-13-return-handoff-claude-ai-, S= the S13 sentence):

```
$ grep -c -i "$N" <7 files>
docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md:0
docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md:0
docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md:0
docs/reports/2026-11-13-research-filing-worker2.md:0
docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md:0
docs/reports/2026-11-13-research-filing-resume-manager.md:0
docs/reports/2026-11-13-research-filing-worker1.md:0
$ tail -n 7 MANIFEST.md | grep -c -i "$N"
0
$ tail -n 7 /tmp/rf-manifest-blob.md | grep -c -i "$N"
0
$ shasum -a 256 <4 channel files> worker1
6b283621f61f8db60052bbf379bb83336de802f199c130321cc0e6931df3b306  docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md
1efd9485762cc2944e47d3be6a5249161a4d3c301ea1caf439561a40b002bde3  docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md
4ac03c59ad9197b0f2a8449983f858be4939b343e46706453e7b505d9cba43c2  docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md
ba2d8613698bfd555b8d274e9f3c9f76c753bf8ba075d86b8fdb87d47c18345a  docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md
ba25d8e935a9e192eed38911fdcf8f9ed92a4cb664a380eef8ee37b6628a8707  docs/reports/2026-11-13-research-filing-worker1.md
$ grep -n -x -F "$S" docs/reports/2026-11-13-research-filing-resume-manager.md | cut -d: -f1; wc -l < docs/reports/2026-11-13-research-filing-resume-manager.md
697
     697
$ awk -v s="$S" '/^[[:space:]]*(```|~~~)/{f=!f; next} !f && $0==s{print NR}' docs/reports/2026-11-13-research-filing-resume-manager.md; awk 'END{print "fence-lines-total", c+0} /^[[:space:]]*(```|~~~)/{c++}' docs/reports/2026-11-13-research-filing-resume-manager.md
697
fence-lines-total 34
$ grep -n -x -F "$S" docs/reports/2026-11-13-research-filing-worker2.md | cut -d: -f1; wc -l < docs/reports/2026-11-13-research-filing-worker2.md
615
     615
$ awk -v s="$S" '/^[[:space:]]*(```|~~~)/{f=!f; next} !f && $0==s{print NR}' docs/reports/2026-11-13-research-filing-worker2.md; awk 'END{print "fence-lines-total", c+0} /^[[:space:]]*(```|~~~)/{c++}' docs/reports/2026-11-13-research-filing-worker2.md
615
fence-lines-total 22
$ shasum -a 256 <two edited reports> MANIFEST.md
d4f4cd736a68b57c4b7951a6a5bf963ac2ef11ccbf640ec1e2df411c97829124  docs/reports/2026-11-13-research-filing-resume-manager.md
f8acdad9fca62496ce6a6196a878a9155a32f013031023c159e3ecc7f69395ac  docs/reports/2026-11-13-research-filing-worker2.md
af41ceb256ace6920ab06347ad5cbc9fb900225a808cb7d4ea06f92748455759  MANIFEST.md
```

(The first run of grep -n -x -F, without `cut`, printed "697:" and "615:" followed by the S13 sentence, one line each; the `| cut -d: -f1` lines above are from a second run, pasted as output, so that the S13 sentence stands once in this report. The fence counts are even, so no fence is left open.)

Negative control (the probe finds the name where it still is):

```
$ echo ${#N}; grep -c -i "$N" /tmp/rfc-pre/resume-manager.md /tmp/rfc-pre/worker2.md /tmp/rfc-pre/resume-manager.step1.md /tmp/rfc-pre/worker2.step1.md
4
/tmp/rfc-pre/worker2.md:2
/tmp/rfc-pre/worker2.step1.md:0
/tmp/rfc-pre/resume-manager.md:2
/tmp/rfc-pre/resume-manager.step1.md:0
$ git diff --cached --name-only | wc -l
       1
```

Manager stress test of the adversary's return (20:33:04Z), reading its report file:

```
$ grep -c -i "$N" $A; grep -c -i -E "$B" $A; grep -n -x -F "$S" $A | cut -d: -f1; wc -l < $A   # B = the three banned words, built with printf
0
0
422
     422
$ git show HEAD:MANIFEST.md | grep -n -i "$N" | cut -d: -f1; grep -c -i "$N" /tmp/rf-manifest-blob.md docs/reports/2026-11-13-open-a2-worker1.md
327
328
docs/reports/2026-11-13-open-a2-worker1.md:1
/tmp/rf-manifest-blob.md:2
$ git diff --cached --name-only | grep -c -i "$N"
1
$ shasum -a 256 worker1 report; channel files
ba25d8e935a9e192eed38911fdcf8f9ed92a4cb664a380eef8ee37b6628a8707  docs/reports/2026-11-13-research-filing-worker1.md
d4f4cd736a68b57c4b7951a6a5bf963ac2ef11ccbf640ec1e2df411c97829124  docs/reports/2026-11-13-research-filing-resume-manager.md
f8acdad9fca62496ce6a6196a878a9155a32f013031023c159e3ecc7f69395ac  docs/reports/2026-11-13-research-filing-worker2.md
af41ceb256ace6920ab06347ad5cbc9fb900225a808cb7d4ea06f92748455759  MANIFEST.md
1569e2e474e77166b93c27fbd50bd54a21434a23f5ca3d15e808461a20d9333b  /tmp/rf-manifest-blob.md
```

(The echo label on the shasum line is inexact: the command hashed the worker1 report, the two edited reports, MANIFEST.md and the blob, as the output shows. The worker1 report sha256 equals its 20:26:28Z value.)

Out-of-scope writes since edit 2 (reference file /tmp/rfc-pre/r.new, written by redirect, not cp -p):

```
20:27:20Z
agent-memory files newer:        0
reports newer:
docs/reports/2026-11-13-research-filing-resume-manager.md
docs/reports/2026-11-13-research-filing-worker2.md
docs/reports/2026-11-13-research-filing-cure-worker1.md
docs/reports/2026-11-13-research-filing-cure-manager.md
```

(The first two are this unit's edit 2, written by `cat > file` just after r.new; their sha256 above equal the post-edit values.)

## Adversarial findings

Cold adversary (worker 1, one round, no fix needed): checks (a) redaction, (b) filer's notes, (c) S13, (d) MANIFEST, (e) blob, (f) zero name hits with negative control, (g) unchanged files, (h) index untouched: all PASS. Blob sha256 it reported: 1569e2e474e77166b93c27fbd50bd54a21434a23f5ca3d15e808461a20d9333b (equal to the manager's).

Outside the unit's scope, raised by the adversary and confirmed by the manager with counts above (escalated to the master, not acted on):

1. HEAD:MANIFEST.md carries the name at :327 and :328 (committed rows; the working tree shows them at :335 and :336 per the adversary). The blob's HEAD prefix therefore carries it twice (`grep -c` 2 on the blob). The brief's proof covered only the last 7 lines; those are 0.
2. Untracked docs/reports/2026-11-13-open-a2-worker1.md carries the name once (count 1). Not in this unit's file set.
3. The one path staged in the real index (not this unit's) has the name in its file name (count 1 from `git diff --cached --name-only | grep -c -i "$N"`).

## S6 cross-block check

No code, hook, order path or strategy file is touched. The unit changes bytes in two uncommitted evidence reports and two uncommitted MANIFEST rows, and rebuilds /tmp/rf-manifest-blob.md. No cross-block effect.

## Files staged

None. The real index was not touched (1 staged path at start and end, not this unit's). Working-tree changes by this unit: docs/reports/2026-11-13-research-filing-resume-manager.md, docs/reports/2026-11-13-research-filing-worker2.md, MANIFEST.md (:481, :483), this report, and the adversary report docs/reports/2026-11-13-research-filing-cure-worker1.md; /tmp/rf-manifest-blob.md and /tmp/rfc-pre/ outside the repo.

Result: PASS

The PASS covers the brief's edits and proofs only; the three out-of-scope items under Adversarial findings remain open for the master.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
