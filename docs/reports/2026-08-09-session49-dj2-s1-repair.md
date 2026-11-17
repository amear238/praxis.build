# Session 49 — `Praxis_build-dj2` S1 evidence repair

## Task

Repair the three S1 defects in `docs/reports/2026-08-09-session48-dj2-k7-insert-rescoped.md` recorded by the
audit at `docs/reports/2026-08-09-session48-dj2-rescoped-audit.md:86-108`. The artifact
(`docs/specs/2026-08-08-ledger-compaction-spec.md`) was found clean and was not to be touched. The failure was
entirely evidence discipline in the report: claims that were true and undemonstrated.

## Rubric criteria addressed

Quoted verbatim from `specs/SPEC_RUBRIC.md:107-114`:

| # | Criterion |
|---|---|
| S1 | Every claim in a report has pasted command output, not a description of output. |
| S2 | No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure. |
| S3 | Every gate claimed working has been deliberately tripped at least once, with the block observed. |
| S7 | Nothing is committed while any audit box is unchecked. |
| S8 | No question that belongs to Amear is answered on his behalf. |

No rubric gap. Every acceptance bar in the brief traces to one of these five lines.

## Workers dispatched

| id | mode | outcome |
|---|---|---|
| `a8c2d3c6a0768a9a0` | ADVERSARIAL | `VERDICT: PASS`. Given the artifact and the S1 criterion only; never given my reasoning. Five non-blocking findings, three of which I acted on. |

One worker of a permitted two. The BUILD half was not delegated: S1 requires that pasted output be output the
author actually observed, and a relayed paste is a description of someone else's output wearing a fence. Every
block in the repair was produced by a command I ran in this session or transcribed by me from the preserved
file. The one thing a second party can do that I cannot is disbelieve me, so the whole worker budget went to
the adversarial arm.

Its spawn is recorded in a hook-written `SubagentStart` row I cannot author:

```
$ grep -n 'hook-recorded at SubagentStart' DISPATCH_LOG.md | grep 'a8c2d3c6a0768a9a0'
320:- [2026-08-09T16:01:34Z] WHO: praxis-worker | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session c41a969 corr=a8c2d3c6a0768a9a0 | WHEN: spawn | HOW: awaiting terminal state | STATE: dispatched
```

## Process log

1. Read `specs/SPEC_RUBRIC.md` in full and confirmed all five cited criteria exist at the quoted lines.
2. Captured the pre-state invariants below **before** any edit: HEAD, index path count, spec sha256, preserved
   evidence sha256.
3. Read the preserved evidence file `docs/reports/2026-08-09-session48-dj2-w2-adversarial.md` end to end (485
   lines) rather than grepping it, so that every block transcribed was one I had seen in context.
4. Ran live re-runs for all three defect-3 measurements and for the defect-2 grep, each with a control.
5. Applied five edits by insertion only. Deleted nothing, reworded no existing conclusion.
6. Reconstructed the pre-edit file byte-exactly to produce a real diff (the report is untracked, so `git diff`
   is unavailable) and to prove the change is pure insertion.
7. Dispatched the adversarial worker on the result.
8. Acted on three of its five findings by **annotation**, not by correcting figures in place.
9. Re-verified every invariant after the edits.

## Verification evidence

### Pre-state, captured before any edit

```
$ git rev-parse HEAD && git diff --cached --name-only | wc -l && shasum -a 256 docs/specs/2026-08-08-ledger-compaction-spec.md docs/reports/2026-08-09-session48-dj2-w2-adversarial.md
c41a969296743ceeafc261280afeb98d87577733
       9
27ad8286fecad451fd5775dd8279a5f8a390d3a1792f707821218e3dbce0f5e6  docs/specs/2026-08-08-ledger-compaction-spec.md
6bbd831df22d81a2938070fe1472fb83a9c22754df4120b273c5db9374fb2171  docs/reports/2026-08-09-session48-dj2-w2-adversarial.md
```

### Post-state, after all edits

```
$ shasum -a 256 docs/specs/2026-08-08-ledger-compaction-spec.md
27ad8286fecad451fd5775dd8279a5f8a390d3a1792f707821218e3dbce0f5e6  docs/specs/2026-08-08-ledger-compaction-spec.md
$ git ls-files -s docs/specs/2026-08-08-ledger-compaction-spec.md
100644 55b417ee898f0a9394779f114eaf5a750ca3c157 0	docs/specs/2026-08-08-ledger-compaction-spec.md
$ git diff --cached --name-only | wc -l
       9
$ git rev-parse HEAD
c41a969296743ceeafc261280afeb98d87577733
$ shasum -a 256 docs/reports/2026-08-09-session48-dj2-w2-adversarial.md
6bbd831df22d81a2938070fe1472fb83a9c22754df4120b273c5db9374fb2171  docs/reports/2026-08-09-session48-dj2-w2-adversarial.md
```

The spec's worktree sha256 is byte-identical before and after (`27ad8286…`), and its staged blob is
`55b417ee…`, the value named in the brief. **The artifact was not touched.** The preserved evidence file's
sha256 still matches the brief's `6bbd831d…`.

The full index, unchanged at nine paths:

```
$ git diff --cached --name-only
DECISION_LOG.md
ISSUE_REGISTER.md
MANIFEST.md
docs/reports/2026-08-06-session42-r8j-phase3-import.md
docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
docs/reports/2026-08-07-session44-r8j-offset-correction-adversarial.md
docs/reports/2026-08-07-session44-r8j-offset-correction-worker1.md
docs/reports/2026-08-07-session44-r8j-offset-correction.md
docs/specs/2026-08-08-ledger-compaction-spec.md
```

Both report files remain untracked, per the repo convention the brief cites:

```
$ git status --porcelain docs/reports/2026-08-09-session48-dj2-k7-insert-rescoped.md
?? docs/reports/2026-08-09-session48-dj2-k7-insert-rescoped.md
```

### The diff

The rescoped report is untracked, so `git diff` cannot produce this. I reconstructed the pre-edit file by
reversing each of my six insertions and validated the reconstruction against the brief's stated pre-edit size:

```
$ python3 revert.py
bytes removed: 15889
$ wc -c pre-edit.md
   25497 .../scratchpad/pre-edit.md
```

**25,497 bytes — exactly the pre-edit size named in the brief.** The reconstruction is byte-perfect, so the
diff below is a real diff and not an approximation.

```
$ diff -u pre-edit.md docs/reports/2026-08-09-session48-dj2-k7-insert-rescoped.md | grep '^@@'
@@ -39,11 +39,94 @@
@@ -135,7 +218,44 @@
@@ -214,6 +334,48 @@
@@ -335,7 +497,261 @@
@@ -413,6 +829,38 @@
$ diff -u pre-edit.md …rescoped.md | grep '^-' | grep -v '^--- ' | wc -l
       0
$ diff -u pre-edit.md …rescoped.md | grep '^+' | grep -v '^+++ ' | wc -l
     448
$ wc -l pre-edit.md …rescoped.md
     454 pre-edit.md
     902 …rescoped.md
```

**Zero lines deleted, 448 added.** Pure insertion — the append-only discipline the brief mandated is not
asserted here, it is measured. Five hunks corresponding to the five edit sites (the worker-count and citation
edits are adjacent and merged into one hunk).

An empty deletion count is worthless without proof the detector fires, so the same pipeline against a copy
with one line removed:

```
$ sed '100d' pre-edit.md > mut.md
$ diff -u pre-edit.md mut.md | grep '^-' | grep -v '^--- ' | wc -l
       1
```

The detector reports 1 on a planted deletion and 0 on the artifact. The zero is a true null.

### Fenced-block counts, before and after

```
$ grep -c '^```' pre-edit.md
30
$ awk '/^## Adversarial findings/,/^## S6 cross-block check/' pre-edit.md | grep -c '^```'
0
$ grep -c '^```' docs/reports/2026-08-09-session48-dj2-k7-insert-rescoped.md
90
$ sed -n '490,769p' docs/reports/2026-08-09-session48-dj2-k7-insert-rescoped.md | grep -c '^```'
32
```

| scope | before | after |
|---|---|---|
| Adversarial findings section | 0 fence lines / **0 blocks** | 32 fence lines / **16 blocks** |
| report as a whole | 30 fence lines / **15 blocks** | 90 fence lines / **45 blocks** |

**A unit discrepancy I am flagging rather than smoothing.** The audit wrote "**30** in the report as a whole".
Measured, the pre-edit file contains 30 *fence lines*, which is 15 *blocks* — so the audit's "30 fenced
blocks" is a fence-line count labelled as a block count. The brief itself distinguishes the two units for the
preserved file ("24 fenced blocks (48 lines matching `^```)"), so the ambiguity is real and I am not resolving
it by choosing the reading that flatters the delta. Both units are given above. Under either reading the
Adversarial section went from **zero** to sixteen blocks, which is the defect the audit actually named.

### Defect 2 — the DISPATCH_LOG grep, with the self-matching hazard controlled

```
$ grep -n 'hook-recorded at SubagentStart' DISPATCH_LOG.md | grep -E 'a828c806e8bf79a3e|ad4a783f9fa880d7c'
312:- [2026-08-09T15:12:40Z] WHO: praxis-worker | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session c41a969 corr=a828c806e8bf79a3e | WHEN: spawn | HOW: awaiting terminal state | STATE: dispatched
314:- [2026-08-09T15:18:32Z] WHO: praxis-worker | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session c41a969 corr=ad4a783f9fa880d7c | WHEN: spawn | HOW: awaiting terminal state | STATE: dispatched
```

Rows at **312 and 314**, inside the `312-318` range the brief cited. Every query is scoped by the
discriminator `hook-recorded at SubagentStart`; the hazard the brief warned about is demonstrated, not
assumed:

```
$ grep -c 'a828c806e8bf79a3e' DISPATCH_LOG.md docs/reports/2026-08-09-session48-dj2-k7-insert-rescoped.md
DISPATCH_LOG.md:2
docs/reports/2026-08-09-session48-dj2-k7-insert-rescoped.md:1
```

An unscoped grep matches the prose describing the grep. Controls on the scoped pattern:

```
$ grep -c 'hook-recorded at SubagentStart.*corr=a4f0b0686801f32a1' DISPATCH_LOG.md
1
$ grep -c 'hook-recorded at SubagentStart.*corr=deadbeefdeadbeef0' DISPATCH_LOG.md
0
```

Real corr id at that position fires; invented one at the same position is silent. Exhaustive worker count with
a window control:

```
$ grep 'WHO: praxis-worker | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart' DISPATCH_LOG.md | grep -c '2026-08-09T15:[12][0-9]'
2
$ grep 'WHO: praxis-worker | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart' DISPATCH_LOG.md | grep -c '2026-08-09T'
4
```

### A dead check I hit, and did not delete

```
$ grep -c 'WHO: praxis-worker | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart.*2026-08-09T15:[12][0-9]' DISPATCH_LOG.md
0
```

That `0` is false. The timestamp precedes `WHO:` on every row, so the single pattern demanded an ordering that
never occurs and could not have matched anything. It is carried into the repaired report rather than binned —
a zero from a check that cannot fire is exactly what the positive controls exist to catch, and deleting it
would remove the only demonstration that they were needed.

### Defect 3 — the three relayed measurements, re-run live

```
$ git init -q . ; printf 'hello\n' > a.txt
$ find .git/objects -type f | wc -l
       0
$ git add a.txt
$ find .git/objects -type f | wc -l
       1
$ find .git/objects -type f
.git/objects/ce/013625030ba8dba906f756967f9e9ca394464a
$ test -f .git/index && echo YES || echo NO
YES
```

Object path `ce/013625030ba8dba906f756967f9e9ca394464a` — identical to both C-9's figure and the session-48
worker's. "Same object hash" is now a hash.

```
$ git show HEAD:docs/specs/2026-08-08-ledger-compaction-spec.md | grep -c '^[[:space:]]*$'
21
$ grep -c '^[[:space:]]*$' docs/specs/2026-08-08-ledger-compaction-spec.md
22
```

```
$ git diff --name-only -- docs/specs/2026-08-08-ledger-compaction-spec.md
$ echo "[exit $?]"
[exit 0]
$ git diff --name-only | head -5
.claude/settings.json
AUDIT_LOG.md
DECISION_LOG.md
DISPATCH_LOG.md
HANDOFF.md
```

Empty for the spec; non-empty without the pathspec. The command is live in this tree, so the empty return is a
finding and not a broken invocation.

### Defect 1 — the Adversarial findings section

Sixteen blocks inserted, each attached to the specific claim it backs, each transcribed from
`docs/reports/2026-08-09-session48-dj2-w2-adversarial.md` at a cited line range: the verdict token (`:482-484`),
zero whitespace-only deletions (`:33-41`), the §3 blank (`:78-89`), K7 byte equality with its one-byte mutant
control (`:223-234`) and row ordering (`:240-247`), the five-word diff (`:145-146`) and whole-body relocation
detector (`:179-197`), the `gate-commit.sh:167-176` range read out (`:292-303`) and its mint-side counterpart
(`:311`), the constraint-8 checks with the `26` mutant control (`:319-332`), the stale figures left stale
(`:359-366`), C-7 untouched (`:372-374`), the tag census (`:381-386`), HEAD and the staged set (`:398-416`),
the seven acceptance checks (`:96-116`), and the protected-paragraph hash with its mutation control
(`:124-132`).

## Adversarial findings

Worker `a8c2d3c6a0768a9a0`, ADVERSARIAL, given the artifact and the S1 criterion and never my reasoning.
Returned an explicit **`VERDICT: PASS`** — a real verdict token, not a truncated partial return.

Blocking defects: **none**. Its fabrication hunt is the finding that matters most: it verified all 20 quoted
blocks byte-for-byte against their cited line ranges in the preserved file and found no fabricated block, no
bad range, no orphan output. It independently confirmed the preserved file is byte-identical to the ephemeral
original (`6bbd831d…` on both), so nothing was altered on the way into the repo. It re-ran every live command
and reproduced every figure. It confirmed via the pre-edit copy that the change deletes and softens nothing,
with its own positive control on the deletion detector.

Five non-blocking findings. **Three I acted on, all by annotation rather than by correcting a figure in
place**, because a pasted block records what a command emitted and editing it to match a later re-run is the
prose-fitting this unit exists to remove:

1. **The `:1` self-match figure is now stale at `4`.** Pasting that block into the report added three further
   occurrences of the corr id. An annotation now states the observer effect and notes the direction: 4 > 1
   strengthens the claim the block was making. The block itself is unedited.
2. **The whole-day count `4` is now `5`** — the fifth row is the adversarial worker's own spawn, appended by
   the hook mid-review. Annotated as a time-of-capture figure with the mechanism named. The session-48 window
   count of 2 is bounded by a closed range and does not move.
3. **A citation to "the session-49 repair report" resolved to nothing.** Replaced with the full repo-relative
   path `docs/reports/2026-08-09-session49-dj2-s1-repair.md`, per the binding citation rule.

Two I did not act on, both pre-existing and outside this unit's scope:

4. **`…rescoped.md:249`** shows `$ sed -n '160,180p' …gate-commit.sh` above ten line-numbered lines; that
   command emits 21 unnumbered lines, so the shown command cannot have produced the shown output. The content
   is accurate (it matches `sed -n '167,176p'`). This is a real S1 defect, but it is present in the pre-edit
   copy and is not one of the three the audit named. **Flagged, not fixed** — repairing an unnamed defect
   inside a last-shot unit widens scope, and the brief's instruction was to fix the report's three defects and
   nothing else. It belongs in a follow-up bead.
5. **Worker 1's report is not preserved in-repo** the way w2's now is; claims sourced to it still rest on a
   scratch path. Same disposition: named, not fixed, because preserving it is a new artifact and this unit was
   scoped to evidence transcription.

## S6 cross-block check

The change is confined to one untracked report file. Tested against the specs of every block it touches:

- **Against the artifact block.** The spec is the thing this unit must not disturb. Its worktree sha256 is
  identical pre and post (`27ad8286…`) and its staged blob is `55b417ee…`, pasted above. No contact.
- **Against the commit-gate block (`.claude/hooks/gate-commit.sh`).** The gate binds an audit token to the
  exact staged tree. Editing an *untracked* file leaves the index untouched, so no mint→commit binding is
  disturbed. Confirmed by the index staying at nine paths with the spec blob unchanged. This is the same
  mechanism C-9 residual 2 documents, and it cuts the other way here: had I staged anything, the tree would
  have moved and any live token would have been invalidated.
- **Against the park-rule block (`specs/SPEC_RUBRIC.md:237-251`).** `dj2` stands at FAIL 1 of 2, so the rule
  fires on the next adverse verdict. I hold no authority to grade my own output and did not attempt to reach
  the auditor. Nothing here amends or reinterprets the rule — it is a session-49 unit and the rule is amended
  cold, by a human, per `SPEC_RUBRIC.md:276-308`.
- **Against S12 (ledger writers).** This unit adds no ledger writer and appends no rows by hand. The one
  `DISPATCH_LOG.md` row it caused (`:320`) was written by the `SubagentStart` hook, not by me.

## Files staged

**None.** The index is unchanged at nine paths, verified above. Nothing was committed; HEAD remains
`c41a969296743ceeafc261280afeb98d87577733`.

Files modified in the worktree, both untracked:

- `docs/reports/2026-08-09-session48-dj2-k7-insert-rescoped.md` — 25,497 → 42,777 bytes, 454 → 902 lines,
  448 lines added, 0 deleted.
- `docs/reports/2026-08-09-session49-dj2-s1-repair.md` — this file, new.

## What I could NOT demonstrate

Stated explicitly rather than omitted:

1. **A `git diff` of the repaired report.** The file is untracked, so git holds no prior version. The diff
   above is against a reconstruction. Its fidelity is evidenced — it lands at exactly 25,497 bytes, the size
   the brief independently states — but it is a reconstruction, and a reader should know that.
2. **Re-running the session-48 adversarial work.** Those experiments ran on scratch copies that no longer
   exist. Sixteen of the blocks are transcriptions from the preserved file, not live re-runs. This is disclosed
   inline in the repaired report. Mitigation: the preserved file's sha256 is verified against the brief's
   value, and an independent worker confirmed every transcribed block byte-for-byte against its cited range.
   That is corroboration, not reproduction, and I am not claiming otherwise.
3. **That `gate-commit.sh` blocks.** Not tripped in this unit. S3 asks that every gate *claimed working* have
   been tripped; I make no claim that it is working. The report reads its source and says so.
4. **That the audit's "30" meant blocks rather than fence lines.** Unresolvable from the artifacts. Both
   readings are given above.
5. **Defects 4 and 5 in the adversarial list are real and remain unrepaired**, by scope decision, not because
   they were shown to be harmless.

## Result: PASS

---

# SECOND PASS

**Unit:** `Praxis_build-dj2` — S1 repair, second pass. Appended, not overwriting: the first pass above stands
as written, including the parts this pass corrects.

## Task

Repair the two S1 defects the first pass declined to fix, after the master re-derived the true count as
**six**, not two. Scope was expanded by the master under a human ruling — not by me.

## Rubric criteria addressed

Quoted from `specs/SPEC_RUBRIC.md:107-114`:

| S1 | Every claim in a report has pasted command output, not a description of output. |
| S2 | No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure. |
| S3 | Every gate claimed working has been deliberately tripped at least once, with the block observed. |
| S7 | Nothing is committed while any audit box is unchecked. |
| S8 | No question that belongs to Amear is answered on his behalf. |

## Declared line set — stated BEFORE editing

Declared against the pre-edit file at sha256
`017dd4518a9c4823e447210404cec54f599a1582710e05b17cfeeba05ded6b03` (902 lines, 42,777 bytes). Four sites:

| # | Pre-edit lines | Change |
|---|---|---|
| D1 | 262 | Replace the mis-attributed command string. |
| D2 | insert after 275 | Record the original wrong command, its three failure modes, the live re-run. |
| D3 | 118–128 | Extend the session-49 citation correction to cover **both** worker reports. |
| D4 | insert after 900 | Cross-reference the durable paths at the adversarial-findings site. |

## Post-edit diff — proving only the declared set was touched

The target file is **untracked**, so `git diff` yields nothing for it. I snapshotted it before editing and
diffed against that snapshot. Snapshot fidelity is proven by identical sha256 at capture time:

```
$ shasum -a 256 "$S/pre-secondpass.md" docs/reports/2026-08-09-session48-dj2-k7-insert-rescoped.md
017dd4518a9c4823e447210404cec54f599a1582710e05b17cfeeba05ded6b03  .../scratchpad/pre-secondpass.md
017dd4518a9c4823e447210404cec54f599a1582710e05b17cfeeba05ded6b03  docs/reports/2026-08-09-session48-dj2-k7-insert-rescoped.md
```

```
$ diff -u "$S/pre-secondpass.md" "$F" | grep -cE '^@@'
4
$ diff -u "$S/pre-secondpass.md" "$F" | grep -E '^@@'
@@ -117,16 +117,28 @@
@@ -259,7 +271,7 @@
@@ -273,7 +285,46 @@
@@ -899,4 +950,9 @@
```

Four hunks, at 117 (D3), 259 (D1), 273 (D2), 899 (D4). **No hunk outside the declared set.** Every deletion:

```
$ diff -u "$S/pre-secondpass.md" "$F" | grep '^-' | grep -v '^---'
-pointed at storage that expires. It cost two rounds of dispute. The adversarial worker's full output is now
-preserved in-repo and every reference to it in this report resolves to that repo-relative path:
-$ shasum -a 256 docs/reports/2026-08-09-session48-dj2-w2-adversarial.md
-$ wc -c docs/reports/2026-08-09-session48-dj2-w2-adversarial.md
-$ sed -n '160,180p' .claude/hooks/gate-commit.sh
```

```
$ diff -u "$S/pre-secondpass.md" "$F" | diffstat
 1 file changed, 61 insertions(+), 5 deletions(-)
$ wc -lc "$S/pre-secondpass.md" "$F"
     902   42777  .../scratchpad/pre-secondpass.md
     958   46676  docs/reports/2026-08-09-session48-dj2-k7-insert-rescoped.md
```

## The `:262` resolution — re-run, not reconciled

The master's three-way defect reproduces exactly. Live, this session:

```
$ sed -n '160,180p' .claude/hooks/gate-commit.sh | wc -l
      21
$ sed -n '160,180p' .claude/hooks/gate-commit.sh | head -3
    exit 2
  fi
  if ! grep -q "$HASH PASS" "$ROOT/AUDIT_LOG.md" 2>/dev/null; then
$ wc -l .claude/hooks/gate-commit.sh
     180 .claude/hooks/gate-commit.sh
```

21 lines, not 10; starts `    exit 2`, not at 167; unnumbered, where the block shows a right-aligned `%6d`+tab
column. All three confirmed.

**The command that genuinely produces the shown output** — found by running candidates and comparing bytes,
never by rewording the command to fit:

```
$ cat -n .claude/hooks/gate-commit.sh | sed -n '167,176p' > "$S/live.txt"
$ sed -n '275,284p' docs/reports/2026-08-09-session48-dj2-k7-insert-rescoped.md > "$S/rpt.txt"
$ cmp "$S/live.txt" "$S/rpt.txt" && echo "CMP rc=0 BYTE-IDENTICAL (FINAL)"
CMP rc=0 BYTE-IDENTICAL (FINAL)
```

The `cat -n` hypothesis the master offered as untested was **tested, and it holds** at `rc=0`. The output was
always genuine — lines 167–176 of the real file. The defect was in the attribution, not the evidence. The
original wrong string is preserved in-report beside its correction, not silently swapped out.

**Observer effect, and it bit twice.** The self-citation range moved as I edited above it: `263,272` →
`272,281` → `275,284`. Each drift was caught by `cmp` **failing**, not by inspection. Recorded in the report
rather than smoothed over.

## All five citation sites — before and after

| Line | Before | Classification | After |
|---|---|---|---|
| 113 | "Worker reports were written to the session scratchpad, not to `docs/reports/`…" | **PROSE** — narrates history, nothing resolves through it | Untouched; annotation below it extended |
| 115 | `/private/tmp/.../56cafa79-.../scratchpad/w1-report.md` | **CITATION** — a reader must follow it | Left standing as historical record; superseded by the in-repo path in the correction block directly beneath |
| 136 (now 145) | "ran a throwaway `git add` in the scratchpad" | **PROSE** — states where an experiment ran | Untouched, explicitly classified in-report |
| 241 (now 250) | "in a fresh throwaway repo in the scratchpad" | **PROSE** — states where an experiment ran | Untouched, explicitly classified in-report |
| 897 (now 943) | "Worker reports were written to the scratchpad, not `docs/reports/`" | **PROSE** — narrates the original reading | Untouched; answered directly beneath with both durable paths |

Both durable targets verified present and byte-unchanged:

```
$ shasum -a 256 docs/reports/2026-08-09-session48-dj2-w1-report.md docs/reports/2026-08-09-session48-dj2-w2-adversarial.md
1f5af984b46338d5a355db740e5f234d2ddbda83e0c79ca896fad5f9e469d473  docs/reports/2026-08-09-session48-dj2-w1-report.md
6bbd831df22d81a2938070fe1472fb83a9c22754df4120b273c5db9374fb2171  docs/reports/2026-08-09-session48-dj2-w2-adversarial.md
```

**The grep count rose from 5 to 7, and I caused it.** Justified line by line:

```
$ grep -cE "scratchpad|/private/tmp" docs/reports/2026-08-09-session48-dj2-k7-insert-rescoped.md
7
```

- `113`, `145`, `250`, `943` — **PROSE**, permitted.
- `115` — historical record, superseded in place, correction adjacent.
- `135` — **new, mine.** Meta-commentary classifying the other mentions.
- `295` — **new, mine. PASTED-EVIDENCE**: a `$S=` assignment inside pasted `cmp` output. It is scratch
  *workspace* for a byte-comparison, not a pointer; nothing in the report resolves through it. The compared
  artifacts are both repo-relative.

## Adversarial sweep — the required two counts

One `praxis-worker` in ADVERSARIAL mode, given the artifact and S1 only, never my reasoning.

```
COUNT_A: 37/42     (command/output pairs re-run and confirmed to reproduce)
COUNT_B: 38/38     (citations resolving to a repo-relative path)
VERDICT: FAIL
```

Count B is clean: all 38 followable citations resolve, including 20 `w2-adversarial.md:N-M` ranges each
checked with `sed -n`. **Count A is not**, and the sweep found substantially more than the six named defects.

## Adversarial findings — verified by me independently

I re-ran the three load-bearing claims myself rather than accepting the worker's summary.

**1. Five blocks do not reproduce as written** (report lines 443/445/447/456/458): they dereference `$SPEC`,
assigned nowhere in the report.

```
$ grep -n 'SPEC=' docs/reports/2026-08-09-session48-dj2-k7-insert-rescoped.md
$ sed -n '443p' docs/reports/2026-08-09-session48-dj2-k7-insert-rescoped.md
$ L=$(grep -n '^Acceptance: STATE.md within K1' "$SPEC" | cut -d: -f1); echo "starts at line $L (was 58)"
--- run verbatim ---
ugrep: warning: : No such file or directory
starts at line  (was 58)
```

The report shows `starts at line 58`. Verbatim execution yields an error and an empty value. Confirmed.

**2. The "scratch copies are gone" premise at L553-554 is false.**

```
$ ls -l /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/56cafa79-.../scratchpad/ | head -6
total 360
-rw-r--r--@ 1 admin  wheel    237 Aug  9 10:50 acc_head.txt
-rw-r--r--@ 1 admin  wheel    237 Aug  9 10:50 acc_work.txt
-rw-r--r--@ 1 admin  wheel    106 Aug  9 10:49 actual_k7.txt
-rw-r--r--@ 1 admin  wheel    569 Aug  9 10:51 after.txt
-rw-r--r--@ 1 admin  wheel    619 Aug  9 10:54 before.txt
```

The directory survives. This premise is **load-bearing**: it is what licenses roughly fifteen blocks to be
transcriptions instead of live re-runs. It is an S2 problem as much as an S1 one.

I corrected the one instance of this inside my own declared hunk — I had written "expired" at L135 — and left
L553-554 alone as out of scope. That asymmetry is deliberate and is disclosed here rather than resolved
quietly.

**3. Blocks presenting figures with no command shown at all**, verified by direct read: L177 substitutes the
parenthetical `(empty)` for output; L178-186 give seven pre-state figures with no command; L427-436 give seven
post-state figures with no command; L472-526 is a 55-line six-trip block with zero commands; L218-225 shows
xtrace with no `$` command and no disclosure it cannot be re-run; L863 appends a right-aligned `path count =
9` inside a `numstat` block that cannot emit it.

The sweep also notes L20 cites `SPEC_RUBRIC.md:107-113` as the source of a criteria table that silently drops
S4 and S5.

## S6 cross-block check

This unit edits one untracked report. It adds no mechanism, changes no gate, touches no spec, and stages
nothing, so it has no cross-block surface. Specifically checked and confirmed unchanged: the compaction spec
(hash, staged blob, and numstat all below), the commit gate (read only, never invoked), and the index.

Against the **park rule** (`SPEC_RUBRIC.md:237-251`): `dj2` stands at FAIL 1 of 2. The master's brief records
that `Praxis_build-8sw` leaves the absolute park rule with **no sanctioned commit path**, so a second FAIL
parks this unit somewhere with no exit. That is the reason this report ends in escalation rather than in a
submission. Nothing here amends or reinterprets the rule — absolutes are amended cold, by a human
(`SPEC_RUBRIC.md:276-308`).

Against **S12**: this unit adds no ledger writer and appends no rows by hand.

## Invariant checks — all re-run this session

```
$ git rev-parse HEAD
c41a969296743ceeafc261280afeb98d87577733
$ git diff --cached --name-only | wc -l
       9
$ shasum -a 256 docs/specs/2026-08-08-ledger-compaction-spec.md
27ad8286fecad451fd5775dd8279a5f8a390d3a1792f707821218e3dbce0f5e6  docs/specs/2026-08-08-ledger-compaction-spec.md
$ git ls-files -s docs/specs/2026-08-08-ledger-compaction-spec.md
100644 55b417ee898f0a9394779f114eaf5a750ca3c157 0	docs/specs/2026-08-08-ledger-compaction-spec.md
$ git diff --cached --numstat -- docs/specs/2026-08-08-ledger-compaction-spec.md
12	2	docs/specs/2026-08-08-ledger-compaction-spec.md
```

HEAD unchanged, index at exactly 9 paths, spec byte-identical on all three measures, both preserved evidence
files at their stated sha256s (pasted in the citation section above). **Nothing committed, nothing staged.**

## Files staged

**None.** The two files modified in the worktree, both untracked:

- `docs/reports/2026-08-09-session48-dj2-k7-insert-rescoped.md` — 902 → 958 lines, 42,777 → 46,676 bytes.
- `docs/reports/2026-08-09-session49-dj2-s1-repair.md` — this file, appended to.

## What I could NOT demonstrate

1. **A `git diff` of the repaired report.** It is untracked; git holds no prior version. The diff above is
   against a snapshot I took this session, with matching sha256 as evidence of fidelity. That is weaker than a
   git diff and I am not presenting it as equivalent.
2. **That `gate-commit.sh` blocks.** Not tripped in this unit. S3 asks that every gate *claimed working* have
   been tripped; I make no such claim. The report reads its source and says only what the source says.
3. **That the audit's "30" meant blocks rather than fence lines.** Still unresolvable from the artifacts; both
   readings stand above.
4. **That the newly-found defects are the last ones.** The first self-check said 2 when the answer was 6; this
   sweep says the remaining count is at least 12. I do not claim the sweep is exhaustive, and the trend across
   three counts is the opposite of reassuring.
5. **The six-trip block at L472-526 cannot be adjudicated.** Same-named scratch files survive but contradict
   it (`grep -c dispatched trip4.md` returns 6, not the block's 5), with mtimes suggesting they belong to the
   halted attempt. I can neither confirm nor refute that block, and I did not edit it.

## Result: BLOCKED — escalated to the master, not submitted for grading

The four declared repairs are complete and verified. **But the adversarial sweep returned FAIL**, and the
defects it found lie outside both my declared line set and the master's six. Under the ruling that widening
scope inside a last-shot unit is not a producer's call, I am not fixing them and I am not submitting.

Requested: a **third pass** with explicit scope, per Condition 1 — editing does not spend the shot, grading
does. The scope decision belongs to the master and to Amear (S8), not to me.

---

## THIRD PASS

Unit `Praxis_build-dj2`, S1 repair, third pass. Target artifact:
`/Volumes/Sensidine/Praxis.build/docs/reports/2026-08-09-session48-dj2-k7-insert-rescoped.md`
(958 lines / 46,676 bytes at the start of this pass).

### Rubric criteria addressed

Quoted from `specs/SPEC_RUBRIC.md:107-114`. The range is stated as 107-114 because that is what actually
contains the eight criteria named in the brief; `107-113` stops at S7 and excludes S8.

| # | Criterion |
|---|---|
| S1 | Every claim in a report has pasted command output, not a description of output. |
| S2 | No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure. |
| S3 | Every gate claimed working has been deliberately tripped at least once, with the block observed. |
| S4 | Every deviation from the plan has a DECISIONS.md entry with a traceable authorisation chain, written before the work, not after. |
| S5 | No approval is inferred from a verbal or in-session exchange. The ledger append is the authorisation. |
| S7 | Nothing is committed while any audit box is unchecked. |
| S8 | No question that belongs to Amear is answered on his behalf. |

### Declared line set — stated BEFORE editing

Against the 958-line pre-edit artifact, the intended edit sites were exactly the master's five:

| id | declared lines | repair |
|---|---|---|
| D1 | 448, 450, 452, 461, 463 | `$SPEC` dereferenced, assigned nowhere — re-run live with the literal path |
| D2 | 432-441 | seven bare figures — supply the generating commands, run live |
| D3 | 534-536, 539 | retract two S3 claims; annotate block 477-531 UNADJUDICABLE, do not delete |
| D4 | 559 | "scratch copies are gone" is false and self-contradictory |
| D5 | 20-30 | restore the dropped S4 and S5 rows; correct the completeness assertion |

A pre-edit snapshot was taken so the diff could be computed mechanically rather than by inspection
(the artifact is untracked, so `git diff` does not cover it):

```
$ cp docs/reports/2026-08-09-session48-dj2-k7-insert-rescoped.md "$S/pre-edit-rescoped.md"
$ shasum -a 256 "$S/pre-edit-rescoped.md"
46334e07fef078b21f53fac58910c0f5b43643496976e9cf27820d500cc0d112  .../pre-edit-rescoped.md
```

### Post-edit diff — and a declared OVERRUN

Every removed line mapped back to its pre-edit line number mechanically:

```
$ awk '/^@@/{split($2,a,","); old=substr(a[1],2)+0; next}
       /^-/{ if(substr($0,1,2)!="--"){printf "OLD %d | %s\n", old, substr($0,2); old++} next }
       /^\+/{ next } { old++ }' "$S/postedit.diff"
OLD 30 | No rubric gap. Every acceptance bar in the brief traces to one of these five lines.
OLD 447 | ```
OLD 448 | $ L=$(grep -n '^Acceptance: STATE.md within K1' "$SPEC" | cut -d: -f1); echo "starts at line $L (was 58)"
OLD 449 | starts at line 58 (was 58)
OLD 450 | $ sed -n "${L},$((L+1))p" "$SPEC" | shasum -a 256
OLD 452 | $ sed -n "${L},$((L+1))p" "$SPEC" | wc -c
OLD 461 | $ H=$(grep -n '^## 3. Constraints and acceptance' "$SPEC" | cut -d: -f1); echo "heading at line $H"
OLD 463 | $ sed -n "${H},$((H+2))p" "$SPEC" | od -c | head -6
OLD 533 | Trip 3 is the important one: it reproduces the exact defect that got the first attempt halted, and shows the blank-line
OLD 534 | accounting reports `1` rather than `0` when it occurs. The gate that this unit claims to satisfy has been observed
OLD 535 | blocking.
OLD 537 | Trips 5 and 6 exist because two zeros/ones in the acceptance set are only meaningful if the greps producing them are
OLD 538 | live. Both were made to fire. Per the standing false-null hazard in this project, a silent check is not evidence until
OLD 539 | its positive arm has been observed.
OLD 559 | scratch copies are gone — so the preserved file is the evidence of record. Everything that *could* be re-run
OLD 560 | live has been, and is marked as such.
```

Six of these sixteen lines are **outside the declared numbers**: 447, 449, 533, 537, 538, 560. Per the
binding process this is a **self-halt, not a silent inclusion**, so it is declared here rather than absorbed.
Each was tested mechanically for whether it was re-added byte-identical:

```
$ for n in 447 449 533 537 538 560; do
    t=$(sed -n "${n}p" "$S/pre-edit-rescoped.md")
    if grep -Fxq -- "$t" "$S/added.txt"; then r="RE-ADDED VERBATIM"; else r="NOT re-added -> real content change"; fi
    printf "OLD %s : %s\n" "$n" "$r"; done
OLD 447 : RE-ADDED VERBATIM
OLD 449 : RE-ADDED VERBATIM
OLD 533 : NOT re-added -> real content change
OLD 537 : NOT re-added -> real content change
OLD 538 : NOT re-added -> real content change
OLD 560 : NOT re-added -> real content change
```

- **447, 449** carry no semantic change. 447 is the opening fence, displaced downward because explanatory
  prose was inserted above it; 449 is an output line reproduced identically by the live re-run.
- **533, 537, 538, 560** are real changes. All four are wrapped continuation lines of the very sentences the
  master declared. The struck claim "The gate ... has been observed blocking" physically spans 533-535, not
  534-536; the sentence ending at 539 begins at 537; the sentence at 559 ends at 560. A sentence that wraps
  across three lines cannot be struck by editing two of them.

**This is reported, not ruled on.** Whether the declared set should be read as sentence-scoped or
strictly line-scoped is the master's call, not the producer's. No line outside defects D1/D3/D4 was touched,
and no newly-found defect was repaired.

Change volume: 81 lines added, 16 removed. Final artifact 1,037 lines / 51,775 bytes.

### D1 — live re-runs with the literal path

Not reconciled. The blocks were re-executed this session with `$SPEC` replaced by the literal repo-relative
path; no retroactive `SPEC=` line was added above stale output.

```
$ L=$(grep -n '^Acceptance: STATE.md within K1' docs/specs/2026-08-08-ledger-compaction-spec.md | cut -d: -f1); echo "starts at line $L (was 58)"
starts at line 58 (was 58)
$ sed -n "${L},$((L+1))p" docs/specs/2026-08-08-ledger-compaction-spec.md | shasum -a 256
c1d0c8c4466a5b9a2ff20fe72a0e28bbb8f2a4896d91cdc7f4c41ed09184948d  -
$ sed -n "${L},$((L+1))p" docs/specs/2026-08-08-ledger-compaction-spec.md | wc -c
     237
$ H=$(grep -n '^## 3. Constraints and acceptance' docs/specs/2026-08-08-ledger-compaction-spec.md | cut -d: -f1); echo "heading at line $H"
heading at line 46
$ sed -n "${H},$((H+2))p" docs/specs/2026-08-08-ledger-compaction-spec.md | od -c | head -6
0000000    #   #       3   .       C   o   n   s   t   r   a   i   n   t
0000020    s       a   n   d       a   c   c   e   p   t   a   n   c   e
0000040   \n  \n   |       #       |       C   o   n   s   t   r   a   i
0000060    n   t       |       T   a   g       |  \n
0000073
```

Every value reproduces what the blocks previously asserted. The defect was that the blocks could not execute,
not that they were wrong.

### D2 — the seven figures, generating commands supplied and run live

```
$ SPECFILE=docs/specs/2026-08-08-ledger-compaction-spec.md
$ CONF=$(grep -n '^## CONFORMANCE' "$SPECFILE" | cut -d: -f1); echo "CONF=$CONF"
CONF=61
$ echo "body    : $((CONF-1))"
body    : 60
$ echo "C1      : $(grep -o 'dispatched' "$SPECFILE" | wc -l)"
C1      :        6
$ echo "C2      : $(tr '\n' ' ' < "$SPECFILE" | tr -s '[:space:]' ' ' | grep -c 'since the last compaction')"
C2      : 1
$ echo "C3a     : $(sed -n "${CONF},\$p" "$SPECFILE" | grep -c 'tokenizer')"
C3a     : 1
$ echo "C3b     : $(sed -n "${CONF},\$p" "$SPECFILE" | tr '\n' ' ' | tr -s '[:space:]' ' ' | grep -c 'byte')"
C3b     : 1
$ echo "neg     : $(tr '\n' ' ' < "$SPECFILE" | tr -s '[:space:]' ' ' | grep -c 'zzz-phrase-not-present')"
neg     : 0
$ echo "C4      : $(tr '\n' ' ' < "$SPECFILE" | tr -s '[:space:]' ' ' | grep -c 'one run late')"
C4      : 1
```

Resolved as a live run, not as a transcription. All seven values identical to the bare figures they replace.

### D3 — retraction, block preserved intact

Block 477-531 of the pre-edit artifact is **not deleted**. It stands verbatim and is annotated
**UNADJUDICABLE**. Two claims resting on it are struck: *"The gate that this unit claims to satisfy has been
observed blocking"* and the implied claim that trips 5 and 6 discharged the positive-arm requirement. The
principle behind the latter — a silent check is not evidence until its positive arm fires — is a standing
project rule and is retained as such; what is retracted is that this unit demonstrated it.

The retraction's premise, verified independently rather than taken on report:

```
$ D=/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/56cafa79-b440-441b-a568-103cc8dc6984/scratchpad
$ grep -c dispatched "$D"/trip4.md
6
```

The block prints `C1 = 5` with the annotation `(pre was 6; must now be 5 => check would block)`. The
preserved file returns **6**. The block does not reproduce. Re-running six trips is new work inside a
last-shot unit and is forbidden, so the figure is left as written and marked unresolved.

**Consequence stated plainly: S3 is NOT satisfied by this unit.** No gate is claimed working on the strength
of the trip block. This lowers the report's claim rather than manufacturing support for it.

### D4 — before / after

Before: *"These are transcriptions of a run that cannot be repeated — the worker's scratch copies are gone"*.
That was false, and it contradicted the artifact's own process-log line stating the paths had not expired.

```
$ D=/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/56cafa79-b440-441b-a568-103cc8dc6984/scratchpad
$ ls "$D" | wc -l
      29
$ ls "$D" | head -8
acc_head.txt
acc_work.txt
actual_k7.txt
after.txt
before.txt
bt
c9.txt
c9mut.txt
```

After: the reason is corrected to the true one — the directory is outside the repo and not version-controlled,
so no later reader can rely on it. Expiry was never the reason. The two passes no longer contradict.

### D5 — before / after

Before: the table cited `specs/SPEC_RUBRIC.md:107-113`, reproduced S1, S2, S3, S6, S7, and asserted *"No
rubric gap. Every acceptance bar in the brief traces to one of these five lines."* The cited range contains
seven criteria, not five:

```
$ sed -n '107,113p' specs/SPEC_RUBRIC.md | cut -c1-8
| S1 | E
| S2 | N
| S3 | E
| S4 | E
| S5 | N
| S6 | C
| S7 | N
```

After: S4 and S5 restored verbatim from the cited range, count corrected to seven, and the omission recorded
in place rather than quietly repaired.

### Adversarial sweep — two counts

Worker `a3716041b8812498e`, ADVERSARIAL, given the artifact and S1 only, never this manager's reasoning.
Returned the literal token **`VERDICT: FAIL`** — a real verdict, not a truncated partial return.

The worker was required to run a control falsifiable in **both** directions, against the three detector
errors that have already inflated counts on this artifact (`grep -c CITED` also matching `UNCITED`; a
backtick-only pattern missing prose-form citations; a too-narrow context window). Its control returned
exact on every arm — neither more nor fewer — and caught two of its own detector bugs before any figure was
reported:

```
=== (a) FENCED BLOCKS TOTAL: 4 ===
=== (a) BLOCKS CONTAINING A COMMAND LINE: 2 ===
=== (b) OUTSIDE FENCES (candidate citations): 4 ===
=== (b) INSIDE FENCES (evidence, excluded): 2 ===
=== (b2) BARE-FILE / BARE-RANGE CITATIONS OUTSIDE FENCES: 2 ===
```

- **(a) command/output pairs re-run and confirmed to reproduce: 21/23.** Four blocks classified
  NOT-RE-RUNNABLE and excluded from the denominator (one observer-effect block, two pre-state captures, one
  block explicitly marked an unrepeatable transcription).
- **(b) citations resolving to a repo-relative path: 40/42.** All 42 resolve; two are `/private/tmp/...`
  scratch paths which resolve on disk but are not repo-relative, and which the artifact already withdraws in
  favour of in-repo copies.

### Defects found OUTSIDE D1-D5 — reported, NOT repaired

Per the binding process, newly-found defects are reported to the master rather than fixed. Both were
re-verified by this manager rather than accepted on the worker's word.

**N1 — a figure dressed as command output.** The block at current lines 936-948 shows the command
`git diff --cached --numstat` followed by nine numstat lines and then a tenth line `path count =        9`.
That command cannot emit that line:

```
$ git diff --cached --numstat | wc -l
       9
$ git diff --cached --numstat | grep -c 'path count'
0
```

The *value* is true — there are nine staged paths — but it is attributed to a command that did not produce
it. That is the S1 signature exactly. Not in D1-D5, therefore not repaired.

**N2 — a self-citation range that MY OWN D5 EDIT broke.** The block at current lines 304-310 cites
`this report:275,284` against `gate-commit.sh:167-176` and asserts `CMP rc=0 BYTE-IDENTICAL`. D5 inserted
seven lines above it, so as written it now fails:

```
$ cat -n .claude/hooks/gate-commit.sh | sed -n '167,176p' > "$S/live.txt"
$ sed -n '275,284p' docs/reports/2026-08-09-session48-dj2-k7-insert-rescoped.md > "$S/rpt275.txt"
$ cmp "$S/live.txt" "$S/rpt275.txt" && echo "CMP rc=0 BYTE-IDENTICAL" || echo "CMP FAILED rc=$?"
.../live.txt .../rpt275.txt differ: char 1, line 1
CMP FAILED rc=1
$ sed -n '282,291p' docs/reports/2026-08-09-session48-dj2-k7-insert-rescoped.md > "$S/rpt282.txt"
$ cmp "$S/live.txt" "$S/rpt282.txt" && echo "CMP rc=0 BYTE-IDENTICAL" || echo "CMP FAILED rc=$?"
CMP rc=0 BYTE-IDENTICAL
```

The shift is fully accounted for: exactly one diff hunk precedes line 275, and it adds seven lines
(`@@ -24,11 +24,18 @@`), so 275 → 282. The evidence is intact; only the pointer drifted. The correct range
is **282,291**. I have **not** applied it — it is outside D1-D5, and the artifact itself pre-declares the
policy that such drift is "recorded rather than adjusted away". Flagged because I caused it.

### S6 cross-block check

S6 is not among this unit's acceptance criteria and no deviation was approved in this pass. The repairs are
confined to one untracked report file; they touch no block spec, no hook, and no shared artifact, so there is
no other block's spec for them to be tested against. Stated rather than silently omitted.

### Invariants — all re-run this pass

```
$ git rev-parse HEAD
c41a969296743ceeafc261280afeb98d87577733
$ git diff --cached --name-only | wc -l
       9
$ shasum -a 256 docs/specs/2026-08-08-ledger-compaction-spec.md
27ad8286fecad451fd5775dd8279a5f8a390d3a1792f707821218e3dbce0f5e6  docs/specs/2026-08-08-ledger-compaction-spec.md
$ git ls-files -s docs/specs/2026-08-08-ledger-compaction-spec.md
100644 55b417ee898f0a9394779f114eaf5a750ca3c157 0	docs/specs/2026-08-08-ledger-compaction-spec.md
$ git diff --cached --numstat docs/specs/2026-08-08-ledger-compaction-spec.md
12	2	docs/specs/2026-08-08-ledger-compaction-spec.md
$ shasum -a 256 docs/reports/2026-08-09-session48-dj2-w1-report.md docs/reports/2026-08-09-session48-dj2-w2-adversarial.md
1f5af984b46338d5a355db740e5f234d2ddbda83e0c79ca896fad5f9e469d473  docs/reports/2026-08-09-session48-dj2-w1-report.md
6bbd831df22d81a2938070fe1472fb83a9c22754df4120b273c5db9374fb2171  docs/reports/2026-08-09-session48-dj2-w2-adversarial.md
$ git status --porcelain -- docs/reports/2026-08-09-session48-dj2-k7-insert-rescoped.md docs/reports/2026-08-09-session49-dj2-s1-repair.md
?? docs/reports/2026-08-09-session48-dj2-k7-insert-rescoped.md
?? docs/reports/2026-08-09-session49-dj2-s1-repair.md
```

HEAD unmoved. Index exactly 9 paths. Spec byte-unchanged on all three measures. Both preserved evidence files
unchanged. Both edited reports untracked — nothing staged, nothing committed. Worker spawns used: **1 of 2**.

### What I could NOT demonstrate

Stated explicitly rather than left to inference:

1. **S3 is not demonstrated by this unit.** The six-trip block is unadjudicable and its claims are retracted.
   No gate was observed blocking by anything re-runnable this session.
2. **Trip 4's `C1 = 5` is unexplained.** The preserved file returns 6. I did not determine what produced the
   5, because doing so requires re-running six trips, which is forbidden here.
3. **Trips 5 and 6 cannot be confirmed to have fired.** Their positive arms are asserted only by the
   unadjudicable block.
4. **N1 and N2 remain live S1 defects in the artifact.** Both are verified, located, and left unrepaired by
   rule. N2's correct range (282,291) is supplied so the master need not re-derive it.
5. **The declared line set was overrun by four substantive lines** (533, 537, 538, 560). Declared above; the
   scope ruling is the master's.

### Files staged

None. Nothing was staged and nothing was committed by this pass. Two untracked files were modified:
`docs/reports/2026-08-09-session48-dj2-k7-insert-rescoped.md` (the artifact) and this report.

### Result: BLOCKED

The five declared repairs D1-D5 are complete, verified live, and evidenced above. The unit is **BLOCKED**
rather than PASS on three grounds, none of which a producer may resolve for itself:

- The adversarial sweep returned `VERDICT: FAIL` on two S1 defects (N1, N2) that lie outside D1-D5. Rule 4
  forbids me from fixing them; a producer that fixes what it was told not to fix has chosen its own scope.
- The declared line set was overrun on four lines. Rule 1 makes that a self-halt.
- S3 is now explicitly not satisfied, by design, following the D3 retraction.

Editing does not spend the shot; grading does. Nothing here is submitted for grading. The scope decision on
N1, N2 and the four overrun lines belongs to the master and to Amear, per S8.

### Process note on this report's own D5 block

The `sed -n '107,113p' specs/SPEC_RUBRIC.md | cut -c1-8` block in the D5 section was drafted from a
previously read file and then verified by running it, rather than pasted from a run in the first instance.
It reproduces exactly as shown, and `sed -n '114p'` returns `| S8 | N`, which confirms the `107-114` range
used in this pass's criteria table. Recorded because "drafted then confirmed" and "pasted from a run" are
not the same provenance, and S1 is a claim about provenance.

## FOURTH PASS

### Task

Repair exactly two authorised S1 defects — N1 and N2 — in the artifact
`docs/reports/2026-08-09-session48-dj2-k7-insert-rescoped.md`, then run a whole-report adversarial S1 sweep.
Nothing else in scope. Rule 4 binding: any further defect is reported, not fixed.

**Locational correction, stated because it changes what the brief pointed at.** The brief cited "report line
937 / 947" and "line 307". Those are lines of the **artifact**, not of this repair report. This report is 984
lines pre-append; the artifact is 1,037. Both sites were located by CONTENT, not by the cited numbers, and the
content matched the brief's description exactly at artifact 937/947 and 307. The brief's "1,037 lines" figure
is the artifact's, and is correct for it.

### Rubric criteria addressed

S1 (the repair itself), S7 (nothing committed), S8 (scope questions returned, not self-answered). S3 remains
**explicitly not satisfied** by this unit, by design, following the D3 retraction — a lowered claim, not a
regression. S2 governs the disposition below: the repairs are reported at "verified live", and the sweep at
"one worker, findings independently re-verified by me", not higher.

### Workers dispatched

| id | mode | outcome |
|---|---|---|
| `a9296c855479392d9` | ADVERSARIAL — whole-artifact S1 sweep, given the artifact and the criterion only, never my reasoning | returned explicit **`VERDICT: FAIL`** (a real verdict token, not a truncated partial) |

Spawns used: **1 of 2**. The auditor was not reached and no attempt was made to reach it.

### Declared line set — declared BEFORE editing

Against the artifact at pre-edit sha256 `f08bed274474ab2867e25b395f4b0e3526a5e0e5bc3fe4793d4f975dee8ae7fe`:

- **N2a** — L307, the range string `275,284p`.
- **N2b** — L312-317, the observer-effect note recording that range's drift history. Included because it
  *states the value of the same pointer*; correcting L307 while leaving L312-317 asserting `275,284` would
  substitute an internal contradiction for a stale range. Declared, not absorbed.
- **N1a** — L947, the orphan line `path count =` + right-aligned `9` (removal).
- **N1b** — insertion immediately after the closing fence at L948.

Nothing above L307 was touched, so the self-cited span 282-291 could not shift.

### Post-edit diff — proving only the declared set moved

The artifact is untracked, so `git diff` cannot show it and no pre-edit copy of this state existed on disk. I
proved containment the other way: by **inverting** my three edits and hashing the reconstruction. If the
inverse reproduces the declared pre-edit hash exactly, the edits were exactly those three and nothing else.

```
$ python3 invert4.py
reconstructed sha256: f08bed274474ab2867e25b395f4b0e3526a5e0e5bc3fe4793d4f975dee8ae7fe
declared pre-edit   : f08bed274474ab2867e25b395f4b0e3526a5e0e5bc3fe4793d4f975dee8ae7fe
MATCH
```

Two hunks, both inside the declared set:

```
$ diff -u recon-pre4.md <artifact> | grep '^@@'
@@ -304,17 +304,20 @@
@@ -944,9 +947,28 @@
```

### N1 — live resolution, and an unresolved attribution left unresolved

The block showed `$ git diff --cached --numstat` followed by nine numstat rows and a tenth line
`path count =` + right-aligned `9`. That command cannot emit that line:

```
$ git diff --cached --numstat | wc -l
       9
$ git diff --cached --numstat | grep -c 'path count'
0
```

The value is true; the attribution was false. **I did not reconstruct a producing command, because the
provenance is underdetermined.** Three structurally different commands emit that byte string *exactly* —
verified against the literal 22-byte target this session:

```
$ od -c target.txt
0000000    p   a   t   h       c   o   u   n   t       =
0000020                    9  \n
0000026
A: BYTE-IDENTICAL      (echo with command substitution)
B: BYTE-IDENTICAL      (printf 'path count = %8d\n')
C: BYTE-IDENTICAL      (git diff --cached --numstat | awk 'END{printf ...NR}')
```

Because three candidates fit, naming any one would be a manufactured match — the precise failure this unit
exists to remove. The orphan line was removed from the block and replaced with the live evidence above plus an
explicit note that the original producer is unrecoverable. **An honest unresolved attribution, per instruction.**

### N2 — range re-derived AFTER the final edit, not before

Ordered last, as instructed, because this pointer has drifted three times already. Derived by exhaustive scan
rather than by arithmetic, so a unique match is proved rather than assumed:

```
$ for st in 1..(EOF-9): cmp <(cat -n .claude/hooks/gate-commit.sh | sed -n '167,176p') <(sed -n "st,st+9p" artifact)
MATCH at 282,291
total matching ranges: 1
$ sed -n '282,291p' docs/reports/2026-08-09-session48-dj2-k7-insert-rescoped.md > "$S/rpt.txt"
$ cmp "$S/live.txt" "$S/rpt.txt" && echo "CMP rc=0 BYTE-IDENTICAL"
CMP rc=0 BYTE-IDENTICAL
```

`282,291` is the unique match and remains correct at the artifact's final byte state. This independently
confirms the master's relayed number rather than trusting it.

### Adversarial findings — the sweep, and why it is still not clean

Worker `a9296c855479392d9`. It found and fixed **two bugs in its own detector** before reporting figures (a
BARERANGE/PATH double-count, and a backtick-only pattern that missed prose-form citations), and ran the
required bidirectional control — a positive arm that must fire and an over-match arm that must stay low.
Its over-match arm correctly rejected `$SPECFILE`/`$SPEC`, `CITED`/`UNCITED`, and indented `$ `.

- **(a) command/output pairs reproducing: 23/24.**
- **(b) citations repo-relative: 40/44.**

**Excluded as not re-runnable — 3 blocks, each justified:**

1. **L62-66** — observer-effect block, disclosed in-place at L68-74. The disclosure *predicts* the re-run
   returns 4; the live re-run returned 4. A prediction that verifies is a stronger exclusion than an assertion.
2. **L79-84, second command only** — `grep -c '2026-08-09T'` on a hook-appended ledger, monotonically rising
   (pasted 4, live 8), disclosed at L89-92. The *first* command of that block is a closed time window, was
   **not** excluded, and reproduced live as 2.
3. **L211-219** — pre-state capture, explicitly headed as pre-edit, corroborated byte-exact against
   `git show HEAD:`.

**These four defects are OUTSIDE N1/N2 — reported, NOT fixed, per rule 4.** I re-verified every one myself
live rather than accepting the worker's word:

- **N3 — L182-196, the FAIL driver.** A block shows three commands, then `(empty)` on its own line, then eight
  figures with no command line above them at all. `(empty)` is a *description of output standing where output
  goes* — S1's exact prohibition. Confirmed it was not produced by the report's own measurement block: that
  block emits `CONF=61`, whereas L188 reads `CONF line = 61`, a string occurring exactly once in the file
  (`grep -c 'CONF line'` → 1, positive arm `grep -c 'CONF'` → 10, near-miss `grep -c 'CONF lines'` → 0). This
  is the same defect class this report repairs twice elsewhere, surviving in the pre-state block.
  *Correction to the worker:* it reported "nine figures at 188-196"; there are **eight**, at L188-195. The
  defect stands; the count does not.
- **N4 — L155 and L1042** cite `gate-commit.sh:160-180` and `gate-commit.sh:167-176`. Verified:
  `gate-commit.sh` is ABSENT at repo root; only `.claude/hooks/gate-commit.sh` exists. L375 uses the correct
  full path, so the file is internally inconsistent. Neither site is flagged anywhere.
- **N5 — L151** still reads "Confirmed all five cited criteria exist" after D5 restored the table to seven
  rows. An uncorrected residual of the very defect D5 repaired.
- **N6 — L614** claims "30 fenced blocks elsewhere in the report" with no pasted output. The file contains 100
  fence markers → 50 blocks; 30 is not reproducible by any grouping I tried.

**On the count discrepancy across passes.** Third pass reported 21/23 and 40/42; this pass 23/24 and 40/44.
The denominators differ because the detectors differ, not because the artifact regressed. I flag this rather
than present the newer figures as an improvement, because a changed denominator is not a measurement of the
same thing.

### S6 cross-block check

The change is confined to one untracked report file and touches no shared block.

- **Against the artifact block (the spec).** Untouched on all three measures — worktree sha256 `27ad8286…`,
  staged blob `55b417ee…`, numstat `12 2`, all pasted below. The ≤60 body cap was not altered and no proposal
  to alter it was acted on.
- **Against the commit-gate block.** Editing an *untracked* file leaves the index untouched, so no
  mint→commit tree binding is disturbed; the index stayed at nine paths throughout.
- **Against the park-rule block.** `dj2` stands at FAIL 1 of 2. Nothing here amends or reinterprets that rule,
  and I hold no authority to grade my own output.

### Invariants — all re-run this pass

```
$ git rev-parse HEAD
c41a969296743ceeafc261280afeb98d87577733
$ git diff --cached --name-only | wc -l
       9
$ shasum -a 256 docs/specs/2026-08-08-ledger-compaction-spec.md
27ad8286fecad451fd5775dd8279a5f8a390d3a1792f707821218e3dbce0f5e6  docs/specs/2026-08-08-ledger-compaction-spec.md
$ git ls-files -s docs/specs/2026-08-08-ledger-compaction-spec.md
100644 55b417ee898f0a9394779f114eaf5a750ca3c157 0	docs/specs/2026-08-08-ledger-compaction-spec.md
$ git diff --cached --numstat -- docs/specs/2026-08-08-ledger-compaction-spec.md
12	2	docs/specs/2026-08-08-ledger-compaction-spec.md
$ shasum -a 256 docs/reports/2026-08-09-session48-dj2-w1-report.md docs/reports/2026-08-09-session48-dj2-w2-adversarial.md
1f5af984b46338d5a355db740e5f234d2ddbda83e0c79ca896fad5f9e469d473  docs/reports/2026-08-09-session48-dj2-w1-report.md
6bbd831df22d81a2938070fe1472fb83a9c22754df4120b273c5db9374fb2171  docs/reports/2026-08-09-session48-dj2-w2-adversarial.md
$ git status --porcelain -- <artifact> <this report>
?? docs/reports/2026-08-09-session48-dj2-k7-insert-rescoped.md
?? docs/reports/2026-08-09-session49-dj2-s1-repair.md
```

HEAD unmoved. Index exactly 9 paths. Spec byte-unchanged on all three measures. Both preserved evidence files
unchanged. Both edited reports untracked. The worker altered nothing: re-running the inversion after its run
still returns MATCH, and it made no writes to `.claude/agent-memory/`.

### What I could NOT demonstrate

1. **I did not independently re-run all 24 command/output pairs.** I verified the FAIL driver and every named
   defect live, and I verified the worker's detector control. The 23/24 and 40/44 figures rest on one worker's
   run, cross-checked at the defect sites but not exhaustively re-derived by me. Reported at that level.
2. **N1's original producing command is unrecoverable.** Three candidates fit byte-for-byte; the attribution is
   left explicitly unresolved in the artifact rather than repaired into something plausible.
3. **S3 is not demonstrated by this unit**, by design. No gate was observed blocking by anything re-runnable
   this session. Trip 4's `C1 = 5`, and whether trips 5 and 6 fired, remain undetermined.
4. **N3-N6 remain live S1 defects in the artifact**, verified and located, left unrepaired by rule 4.

### Files staged

None. Nothing staged, nothing committed. Two untracked files modified: the artifact and this report.

### Result: BLOCKED

N1 and N2 are repaired, verified live, and provably contained to the declared line set. The unit is **BLOCKED**
rather than PASS on one ground only, and it is the same structural bind as last pass:

**The authorised scope and the clean-sweep trigger are still unsatisfiable together.** The precondition is
"audit only after the sweep returns clean." The sweep now returns `VERDICT: FAIL` on N3-N6 — four defects
outside N1/N2 that rule 4 forbids me from fixing. Widening scope to reach the trigger is what happened last
pass; doing it again on each new sweep is an unbounded regress, and the decision to widen, to accept the
artifact with N3-N6 recorded, or to stop, is not a producer's to make. Escalated per S8.

Editing does not spend the shot; grading does. **Nothing here is submitted for grading.**
