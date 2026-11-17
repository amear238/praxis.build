# Session 37 — index restage split (docs-first commit)

Manager: praxis-manager. Date: 2026-07-27. Baseline HEAD: `c1dec30`.

## Task

Reduce the git index from 10 staged paths to exactly 7 — `MANIFEST.md` plus the
six `2026-07-26-session36-*` evidence reports — so the evidence lands as its own
commit. `.claude/settings.json`, `DECISION_LOG.md` and `ISSUE_REGISTER.md` are
fully unstaged with their working-tree content preserved byte-for-byte; they are
a later commit, not a discard. No commit is created by this unit.

Rationale carried from the brief: the ledger rows destined for the second commit
cite the report files by path, so landing the reports first makes those citations
resolve on arrival instead of dangling.

## Rubric criteria addressed

| # | Criterion (verbatim, `specs/SPEC_RUBRIC.md`) | Disposition |
|---|---|---|
| S1 | Every claim in a report has pasted command output, not a description of output. | Met. Every assertion below is backed by output the manager re-ran and pasted in this session. |
| S2 | No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure. | Met, and applied against this unit's own out-of-scope finding — see Adversarial findings F2, reported at read-level only. |
| S6 | Cross-block check: every approved deviation is tested against the specs of every other block it touches, not only its own. | Met — dedicated section below. |
| S7 | Nothing is committed while any audit box is unchecked. | Met. Nothing was committed. The two untracked `Praxis_build-8sw` reports stay out of the index; 8sw stands at audit FAIL 1 of 2. |

## Workers dispatched

| id | mode | scope | outcome |
|---|---|---|---|
| `a46c6188b735d6a88` | BUILD | Perform the index reduction using `git restore --staged` only | PASS — one command, verified |
| `a796a319b97a56749` | ADVERSARIAL | Break six claims about the resulting index; mandatory firing positive control | PASS on all six claims; positive control fired; one out-of-scope deviation (see F1) |

Worker cap of 2 respected. The adversarial worker received the artifact and the
criteria only — never the build worker's reasoning or report.

## Process log

1. Read `specs/SPEC_RUBRIC.md` before planning. All four criteria above are quoted
   from it; none were authored here.
2. Manager performed the mandatory MANIFEST precondition check directly (read-only)
   before any index operation. Result: PASS — the 6 staged additions are six rows,
   one per staged report path, no row describing any other file. Had any row named
   a different file, this report would read `Result: BLOCKED` and the index would
   be untouched.
3. Manager captured baseline `sha256` of all ten involved files and `git rev-parse
   HEAD` before dispatch.
4. Dispatched build worker. Single permitted operation:
   `git restore --staged .claude/settings.json DECISION_LOG.md ISSUE_REGISTER.md`.
5. Read the build worker's report file, not its summary.
6. Manager independently re-ran every verification command and pasted the output
   below. The build worker's numbers were not accepted on report.
7. Dispatched the adversarial worker with a mandatory firing positive control,
   read-only in the project repo, all mutation confined to a throwaway repo.
8. Manager re-verified the index a third time after the adversarial pass, to
   confirm the read-only constraint held.
9. Manager read `.claude/hooks/gate-commit.sh` and `scripts/no-commit-guard.sh`
   directly to grade the adversarial worker's out-of-scope environment claim
   rather than accept its characterisation.
10. Stop condition reached. No adjacent problems investigated, nothing cleaned up.

## Verification evidence

All output below was produced by the manager, in this session, after the surgery.
Nothing here is transcribed from a worker report.

### 1. Staged numstat — target is 7 paths / 1582 additions / 0 deletions

```
$ git diff --cached --numstat
6	0	MANIFEST.md
226	0	docs/reports/2026-07-26-session36-adversarial-actor-hunt.md
385	0	docs/reports/2026-07-26-session36-agent-key-audit.md
287	0	docs/reports/2026-07-26-session36-agent-key-lab.md
219	0	docs/reports/2026-07-26-session36-agent-key-s9-control.md
328	0	docs/reports/2026-07-26-session36-null-attack.md
131	0	docs/reports/2026-07-26-session36-worker-trigger-probe.md

$ git diff --cached --numstat | awk '{a+=$1;d+=$2;n++} END{print "paths="n" adds="a" dels="d}'
paths=7 adds=1582 dels=0
```

### 2. Working tree state

```
$ git status --short
 M .claude/settings.json
 M AUDIT_LOG.md
 M DECISION_LOG.md
 M DISPATCH_LOG.md
 M ISSUE_REGISTER.md
M  MANIFEST.md
A  docs/reports/2026-07-26-session36-adversarial-actor-hunt.md
A  docs/reports/2026-07-26-session36-agent-key-audit.md
A  docs/reports/2026-07-26-session36-agent-key-lab.md
A  docs/reports/2026-07-26-session36-agent-key-s9-control.md
A  docs/reports/2026-07-26-session36-null-attack.md
A  docs/reports/2026-07-26-session36-worker-trigger-probe.md
?? .claude/agent-memory/
?? docs/reports/2026-07-26-session34-manifest-amendment.md
?? docs/reports/2026-07-26-session34-p0-flush-audit.md
?? docs/reports/2026-07-26-session35-8sw-audit-round1.md
?? docs/reports/2026-07-26-session35-8sw-gate-park-conflict.md
?? docs/reports/2026-07-26-session36-manifest-and-memory.md
?? docs/reports/2026-07-27-session36-park-rule-escalation.md
```

The three target files moved from `M ` (staged) to ` M` (unstaged, working tree
still modified). `DECISION_LOG.md` moved from `MM` to ` M` — its staged half was
dropped, its working-tree half retained, which is exactly the intent. `AUDIT_LOG.md`
and `DISPATCH_LOG.md` were already ` M` before this unit and are unchanged.

### 3. Working tree byte-identical — sha256 before and after

Before (captured by the manager prior to dispatch):

```
eed25e6749b64efff80f87d782817bf8a44e9cc81fad0728526375fb0ce71f1a  .claude/settings.json
c3e1e34b4c8b25eb5309d586e8536b918ee422cb97997886307634b29790862c  DECISION_LOG.md
a59d18c7e423847941de97cc5a35ecf13a50fcee5f03e17aa383ef5e0bc886f1  ISSUE_REGISTER.md
05f232b569d4d22eb9ad13ae41b9a86e938faedbe0c78aa98189772c5edd053d  MANIFEST.md
016ad83451b8858c2229d46bc45f000b4e85aab1f0c9117939ef57ec8cdae14c  docs/reports/2026-07-26-session36-adversarial-actor-hunt.md
ad7ee5a19d7d64864ee9e20a4bdf36da7fa960d3a2bfc8a2b814b8afd939b38c  docs/reports/2026-07-26-session36-agent-key-audit.md
890f55af024dc65b51e2069a4b6d6a456307b169b938c417fb7c808667e4f917  docs/reports/2026-07-26-session36-agent-key-lab.md
fddd59b726dc1fbf326cc6432beedf04c657f24a1104a80c8eca487b24dc8620  docs/reports/2026-07-26-session36-agent-key-s9-control.md
70453b0a274df0aa6204804ad0ad375130bdc03feebaaba1cf87b17340ea1329  docs/reports/2026-07-26-session36-null-attack.md
5369b015a3e306d2248897fc4d5d4b0c49b4c0c87f97908adf7f8db288b05492  docs/reports/2026-07-26-session36-worker-trigger-probe.md
```

After (re-run by the manager post-surgery):

```
eed25e6749b64efff80f87d782817bf8a44e9cc81fad0728526375fb0ce71f1a  .claude/settings.json
c3e1e34b4c8b25eb5309d586e8536b918ee422cb97997886307634b29790862c  DECISION_LOG.md
a59d18c7e423847941de97cc5a35ecf13a50fcee5f03e17aa383ef5e0bc886f1  ISSUE_REGISTER.md
05f232b569d4d22eb9ad13ae41b9a86e938faedbe0c78aa98189772c5edd053d  MANIFEST.md
016ad83451b8858c2229d46bc45f000b4e85aab1f0c9117939ef57ec8cdae14c  docs/reports/2026-07-26-session36-adversarial-actor-hunt.md
ad7ee5a19d7d64864ee9e20a4bdf36da7fa960d3a2bfc8a2b814b8afd939b38c  docs/reports/2026-07-26-session36-agent-key-audit.md
890f55af024dc65b51e2069a4b6d6a456307b169b938c417fb7c808667e4f917  docs/reports/2026-07-26-session36-agent-key-lab.md
fddd59b726dc1fbf326cc6432beedf04c657f24a1104a80c8eca487b24dc8620  docs/reports/2026-07-26-session36-agent-key-s9-control.md
70453b0a274df0aa6204804ad0ad375130bdc03feebaaba1cf87b17340ea1329  docs/reports/2026-07-26-session36-null-attack.md
5369b015a3e306d2248897fc4d5d4b0c49b4c0c87f97908adf7f8db288b05492  docs/reports/2026-07-26-session36-worker-trigger-probe.md
```

Identical, hash for hash, all ten. The index moved; no file content did.

### 4. HEAD unchanged and no commit created

```
$ git rev-parse HEAD
c1dec30c6516edcf7c79a78fce5c655e007d7ba2

$ git log -1 --oneline
c1dec30 chore(flush): AUDIT_LOG row Praxis_build-3fe + proposer/approver schema, cold-amendment rule, t83 convention [Praxis_build-o3d]
```

Reflog and file-mtime cross-check, confirming HEAD did not move at any point today
(2026-07-27) and that the only thing this unit wrote was `.git/index`:

```
$ git reflog --date=iso -3
c1dec30 HEAD@{2026-07-26 17:22:42 -0400}: reset: moving to HEAD~1
599885e HEAD@{2026-07-26 15:51:31 -0400}: checkout: moving from main to main
599885e HEAD@{2026-07-26 15:51:31 -0400}: commit: park(<bead-id>): audit-fail-x2, session ended per absolute park rule

$ stat -f '%Sm %N' -t '%Y-%m-%dT%H:%M:%S' .git/index .git/logs/HEAD ; date -u +%Y-%m-%dT%H:%M:%SZ
2026-07-27T15:04:22 .git/index
2026-07-26T17:22:42 .git/logs/HEAD
2026-07-27T19:05:26Z
```

`.git/logs/HEAD` was last written 2026-07-26 — no HEAD movement in this session.
`.git/index` was written 2026-07-27 15:04:22 local (19:04Z), one minute before the
timestamp above, matching the single `git restore --staged` call. The two reflog
entries shown are pre-existing session-36 state, not products of this unit.

### 5. Index path set, checked independently of numstat

```
$ git diff --cached --name-only
MANIFEST.md
docs/reports/2026-07-26-session36-adversarial-actor-hunt.md
docs/reports/2026-07-26-session36-agent-key-audit.md
docs/reports/2026-07-26-session36-agent-key-lab.md
docs/reports/2026-07-26-session36-agent-key-s9-control.md
docs/reports/2026-07-26-session36-null-attack.md
docs/reports/2026-07-26-session36-worker-trigger-probe.md
```

### 6. Index re-verified after the adversarial pass

Re-run by the manager once the adversarial worker returned, to confirm its
read-only constraint held:

```
$ git diff --cached --numstat | awk '{a+=$1;d+=$2;n++} END{print "paths="n" adds="a" dels="d}'
paths=7 adds=1582 dels=0

$ git rev-parse HEAD
c1dec30c6516edcf7c79a78fce5c655e007d7ba2
```

`git status --short` at this point was byte-identical to section 2.

### 7. Precondition check — MANIFEST anti-smuggling

The 6 staged additions to `MANIFEST.md` are six registry rows whose subject paths
are, in file order:

```
| /docs/reports/2026-07-26-session36-agent-key-s9-control.md | Report | 0 | 2026-07-26 | ...
| /docs/reports/2026-07-26-session36-null-attack.md | Report | 0 | 2026-07-26 | ...
| /docs/reports/2026-07-26-session36-agent-key-audit.md | Report | 0 | 2026-07-26 | ...
| /docs/reports/2026-07-26-session36-agent-key-lab.md | Report | 0 | 2026-07-26 | ...
| /docs/reports/2026-07-26-session36-adversarial-actor-hunt.md | Report | 0 | 2026-07-26 | ...
| /docs/reports/2026-07-26-session36-worker-trigger-probe.md | Report | 0 | 2026-07-26 | ...
```

Six rows, six distinct subject paths, a 1:1 map onto the six staged report files.
Zero rows for any other path, and in particular zero rows for the six untracked
reports. Verified twice — once by the manager before the index was touched, once
by the adversarial worker afterwards from the staged diff.

## Negative test — does the detector actually fire

A verification command that always answers "7 paths" is not a verification command.
The adversarial worker was required to prove its detector fires before its silence
could be believed. In a throwaway `git init` repo under the scratchpad, entirely
outside this project, it built a deliberately wrong index — an extra staged path, a
staged deletion, and a mode-only flip from `100644` to `100755` — and re-ran the
same detection commands used against the real repo. All three defects were caught:
the detector reported 4 paths where 1 was claimed, 1 deletion where 0 was claimed,
and flagged the mode flip that `--numstat` alone would have missed. The failing arm
and the passing arm were both captured. The scratch repo was then deleted.

**What was deliberately not tripped, and why.** The commit gate itself was not
trip-tested against this staged set. Doing so requires issuing a commit-shaped
command in this repo, which the brief forbids outright and which the manager cannot
do. S3 is therefore **not** discharged for the commit gate by this unit, and no
claim is made that it was. What is discharged is the index detector's positive
control, which is a different mechanism.

## Adversarial findings

All six claims put to the adversarial worker came back CONFIRMED: the 7-path set
cross-checked via `--name-status`, `--numstat`, and a full `git ls-tree -r HEAD`
versus `git ls-files -s` comparison; additions 1582 and deletions 0; the three
unstaged files each proven to have an index blob exactly equal to `HEAD:<path>`
while `git diff --stat` remains non-empty against the working tree, which is the
strong form that catches a silently discarded edit that `git status` alone cannot;
HEAD literal-matched with `git fsck --unreachable --no-reflog` showing no dangling
commit dated today; the untracked set matched exactly; and the MANIFEST rows mapped
1:1 with no smuggled row. A secret scan across the staged diff returned only the
word "token" in its audit-token sense, no credentials.

Two findings the manager raises against the adversarial worker itself.

**F1 — scope deviation by the adversarial worker (contained, not material to the
index).** The worker was instructed to be read-only inside the project repo. It
nonetheless wrote two files into the project working tree:
`.claude/agent-memory/praxis-worker/project_commit-guards-block-scratch-repos.md`
(new) and `.claude/agent-memory/praxis-worker/MEMORY.md` (modified). Both sit under
`.claude/agent-memory/`, which was already untracked as a whole before this unit, so
`git status --short` is unchanged and the index is unaffected — verified in section 6.
The manager did **not** delete them: removing an untracked file is forbidden by this
brief, and the stop condition had been reached. Disposition is the master's.

**F2 — a false universal negative persisted into shared memory, plus a plausible
untested gate bypass.** The worker's new memory file closes with the claim that
`scripts/no-commit-guard.sh` "still correctly blocks a worker from committing in the
REAL repo through any route." That is an unverified universal negative and the
manager grades it as unsupported. Reading the two guards directly:

- `.claude/hooks/gate-commit.sh:45` scrubs quoted regions *before* matching —
  `SCRUB=$(printf '%s' "$CMD" | sed -e "s/'[^']*'//g" -e 's/"[^"]*"//g')` — and the
  command-position regex at `:51` is then applied to `SCRUB`, not to the raw command.
  The header at `:39` states this is deliberate, so free text can never anchor a match.
- `scripts/no-commit-guard.sh:20` matches `\bgit\s+(commit|push|merge|rebase|tag)\b`,
  which requires the subcommand immediately after `git` and whitespace.

The worker's *mechanism* claim is therefore confirmed by source, and it observed the
scrub behaviour live when a quoted `'commit'` argument survived to `git hash-object`
in its scratch repo. What follows from that — that a form such as `git 'commit' -m
"..."` would evade both guards, because the quoted token is scrubbed out of one and
breaks the `\s+` adjacency in the other — is a **hypothesis read off the source and
not observed**. The manager did not test it and will not: testing it means attempting
a commit in this repo. It is escalated to the master as untested, because a confident
static read is not an observation, and that exact substitution has already produced
wrong conclusions in this project twice. If it holds, it is a defect in the control
the whole producer/grader separation rests on, and it now has a workaround recipe
written into version-controlled worker memory.

The worker's own report also condenses rather than pastes some evidence
("full output above in tool calls"), which is an S1 miss at worker level. It does not
propagate: every number in this report's Verification evidence section was re-run and
pasted by the manager.

## S6 cross-block check

The deviation graded here is a change of index composition, not of file content. It
is checked against every block it touches, not only its own.

1. **Second-commit block (`.claude/settings.json`, `DECISION_LOG.md`,
   `ISSUE_REGISTER.md`).** These are the intended contents of the follow-on commit.
   The failure mode is that unstaging silently discards their pending edits. Tested
   two ways and negative on both: identical sha256 before and after (section 3), and
   the adversarial worker's stronger check that each file's index blob now equals
   `HEAD:<path>` while `git diff --stat` against the working tree remains non-empty
   at 1, 32 and 4 insertions respectively. The second commit remains fully
   constructible.
2. **`Praxis_build-8sw` (audit FAIL 1 of 2).** Two of the six untracked reports
   belong to this bead. Sweeping them into a docs commit would be an S7 violation.
   They remain `??` and out of the index — section 2. The reduction moved paths out
   of the index only; it added nothing, so it cannot have pulled them in.
3. **MANIFEST registry.** `MANIFEST.md` rides in this commit and is the one non-report
   path in it. Its 6 rows were checked to describe only the 6 co-staged reports
   (section 7), so the registry cannot land describing a file this commit does not
   carry, and cannot smuggle an unrelated row behind a docs-only subject line.
4. **Citation ordering.** The ledger rows in the second commit cite these report
   paths. Because the reports land first, those citations resolve on arrival. This is
   the property the split exists to produce and it is satisfied by the ordering, not
   by anything in the file contents.
5. **The park/audit blocks.** No commit, branch, reflog or history operation was
   performed, so the absolute park rule and the pending `parked/Praxis_build-37h`
   state are untouched — confirmed by the unchanged `.git/logs/HEAD` mtime in
   section 4.
6. **Commit-gate block.** Not exercised, deliberately, and not claimed as exercised.
   Finding F2 raises an untested question about that gate which belongs to the master.

No block is left in a state this unit changed without checking.

## Files staged

Exactly seven, unchanged in content from before this unit:

```
MANIFEST.md
docs/reports/2026-07-26-session36-adversarial-actor-hunt.md
docs/reports/2026-07-26-session36-agent-key-audit.md
docs/reports/2026-07-26-session36-agent-key-lab.md
docs/reports/2026-07-26-session36-agent-key-s9-control.md
docs/reports/2026-07-26-session36-null-attack.md
docs/reports/2026-07-26-session36-worker-trigger-probe.md
```

Left staged for the master. The manager cannot and did not commit.

This report file is itself untracked and deliberately not staged, so the staged set
remains the 7 paths above.

## Result

The index matches the target set exactly: 7 paths, 1582 additions, 0 deletions.
The three deferred files are fully unstaged with their working-tree content proven
byte-identical. HEAD is unmoved and no commit exists. The MANIFEST precondition
passed. The adversarial pass broke none of the six claims and its detector was
proven to fire on a deliberately wrong index. Two findings are escalated to the
master (F1 scope deviation, F2 untested gate-bypass hypothesis); neither affects
the staged set.

**Result: PASS**
