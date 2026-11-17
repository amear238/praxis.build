# C1 false-quotation correction — session 41, 2026-08-04

## Task

Two staged reports attribute a direct quotation to
`.claude/agent-memory/praxis-worker/project_agent-type-source.md` and then demand
correction of the quoted line. The target contains no such sentence. Add an
approved bracketed inline correction at each site, **preserving the original
claim** (`wx7` precedent), re-stage exactly those two paths, commit nothing.

Authority: Amear's human park resumption, `DECISION_LOG.md 2026-08-04T18:33Z`,
extended to this specific repair at `2026-08-04T18:44Z`. Both rows read at source
before starting. Scope held to the brief; every additional defect found is
**reported, not fixed**.

## Rubric criteria addressed (read at source, `specs/SPEC_RUBRIC.md:107,108,113`)

| # | Criterion | Disposition |
|---|---|---|
| S1 | Every claim in a report has pasted command output, not a description of output. | Met — all evidence below is pasted, including both arms of every null test. |
| S2 | No component is reported at a higher level than the evidence supports. | Met — the repair is reported as *staged and additive* (proven), not as *committed* or *audited*. One unresolved downstream defect is stated as blocking rather than absorbed. |
| S7 | Nothing is committed while any audit box is unchecked. | Met — `HEAD` unmoved at `c1dec30`, no commit attempted. |

## Workers dispatched

| id | mode | outcome |
|---|---|---|
| `a492860c7c0ca6581` | ADVERSARIAL | `VERDICT: BREAK FOUND` — item 6 (dangling citation). Items 1–5 survive. |

**Count: 1 of 1 permitted.** The cap was spent on the adversarial pass; the edit
itself (two single-line insertions) I made directly. **All verification after the
worker returned was performed by me on my own artifact.** That is a real reduction
in independence and is stated plainly rather than glossed: no second party checked
my re-verification of the worker's findings.

## Process log

1. Verified `HEAD`, captured baseline `git diff --cached --numstat`.
2. Read both `DECISION_LOG` authority rows in full at source.
3. Reproduced the liveness control (both arms) rather than trusting the brief.
4. Verified both sites and the marker's own citation target before editing.
5. Two purely additive `Edit` insertions.
6. `git add` on exactly the two paths (the re-stage trap — both were already staged).
7. Dispatched the adversarial worker; then independently re-verified its claims.

## Verification evidence (pasted output only)

### Liveness control — the quotation is absent

```
=== CONTROL ARM ===
8
exit=0
=== TEST ARM ===
exit=1
=== SECOND TEST ARM (settings key phrase) ===
exit=1
=== FILE EXISTS/SIZE ===
      78 .claude/agent-memory/praxis-worker/project_agent-type-source.md
```

Flag-matched control (identical flags to the test arm, `grep -in`) — proves the
`-i`/`-n` path is live, not merely `grep -c`:

```
3:description: CORRECTED — the root `agent` key in .claude/settings.json DOES set agent_type ...
11:`"agent": "<name>"` key in `.claude/settings.json` **does** set `agent_type` in PreToolUse hook
14:warning, no stderr, and a payload with no `agent_type` at all. `claude --help` corroborates that
...
exit=0
```

Control fires (8 matches / exit 0); test arm returns nothing (exit 1). The file,
path and pattern engine are all demonstrably live. A bare zero would have been
worthless here.

### Additivity — proven mechanically, not by eye

`git diff --cached` **cannot** establish this: both files are `new file mode`, so
the staged diff is against `/dev/null` and structurally cannot show a deletion.
Proof is instead by stripping the inserted marker from the staged blob and
comparing bytes to the prior blob:

```
--- null-attack ---
  correction markers present in staged blob : 1
  staged bytes=14596  prior bytes=14445  stripped bytes=14445
  STRIPPED == PRIOR (byte-identical, no original text lost) : True

s9-control: strip ONLY my correction marker
  markers stripped : 1
  staged=10858 prior=10749 stripped=10749
  STRIPPED == PRIOR (my edit was purely additive): True
  POSITIVE CONTROL (delete one word too): False <- must be False
```

The positive control fires (False when one word is deleted), so the test can
detect non-additivity. No original character was deleted, reworded or moved.

### Index — before and after

Before:

```
8	0	.gitignore
226	0	docs/reports/2026-07-26-session36-adversarial-actor-hunt.md
385	0	docs/reports/2026-07-26-session36-agent-key-audit.md
287	0	docs/reports/2026-07-26-session36-agent-key-lab.md
219	0	docs/reports/2026-07-26-session36-agent-key-s9-control.md
328	0	docs/reports/2026-07-26-session36-null-attack.md
131	0	docs/reports/2026-07-26-session36-worker-trigger-probe.md
```

After — **identical**, 7 paths:

```
8	0	.gitignore
226	0	docs/reports/2026-07-26-session36-adversarial-actor-hunt.md
385	0	docs/reports/2026-07-26-session36-agent-key-audit.md
287	0	docs/reports/2026-07-26-session36-agent-key-lab.md
219	0	docs/reports/2026-07-26-session36-agent-key-s9-control.md
328	0	docs/reports/2026-07-26-session36-null-attack.md
131	0	docs/reports/2026-07-26-session36-worker-trigger-probe.md
paths: 7
```

**Deviation from the brief, flagged not glossed:** the brief expected "only those
two files' line counts may move." They did **not** move (219/219, 328/328). This
is not a failed edit — the correction was inserted *inline into existing lines*,
adding zero new lines, and these are new files so numstat reports total added
lines. The staged diff confirms the text landed:

```
+advises "do not propose the settings key as a way to set `agent_type`." [correction 2026-08-04: this quotation is absent from the target file; see ISSUE_REGISTER 2026-08-04T18:45Z] **That guidance is now
+key as a way to set `agent_type`." [correction 2026-08-04: this quotation is absent from the target file; see ISSUE_REGISTER 2026-08-04T18:45Z] That guidance is wrong and should be corrected by
```

### Re-stage trap cleared, with a live residue detector

```
-- positive arm: a file known to have unstaged mods --
AUDIT_LOG.md
-- negative arm: the two corrected files --
(empty above = no residue)
```

```
A  docs/reports/2026-07-26-session36-agent-key-s9-control.md
A  docs/reports/2026-07-26-session36-null-attack.md
```

### HEAD unmoved

```
c1dec30c6516edcf7c79a78fce5c655e007d7ba2
```

## Adversarial findings

**BREAK (worker item 6), independently re-verified by me — REPORTED, NOT FIXED.**
The correction marker cites `ISSUE_REGISTER 2026-08-04T18:45Z`. That row exists in
the **worktree** but not in the **commit payload**:

```
=== is ISSUE_REGISTER.md staged? ===
 M ISSUE_REGISTER.md
-- test arm: the 18:45Z row in HEAD --
0
test exit=1
-- POSITIVE CONTROL: same command, pattern known to be in HEAD --
19
control exit=0
-- and the row IS in the worktree --
1
```

Control fires (19), test arm zero. So the C1 payload would ship two reports whose
correction marker resolves to nothing for any reader of the committed repo — the
same defect class the marker repairs. **I did not fix this.** The worker's
suggested fix (`git add ISSUE_REGISTER.md`) would make the index 8 paths, breaching
the brief's explicit 7-path constraint and the narrow terms of the human
resumption. This is precisely the "report it, do not fix it" case. **Escalated:
resolve before the C1 payload commits.**

**Worker claim that did NOT reproduce.** The worker reported blob deltas as
"deletions=0 insertions=2" / "deletions=0 insertions=1". Raw diff shows 2 and 1
deletion-marked lines respectively — line-modification pairs, the normal
representation of an inline insertion. Its *conclusion* (additive) is correct; its
*stated numbers* are not, and blob `de38b272` predates the earlier citation-marker
unit, so that comparison conflates two units. I replaced it with the byte-level
strip test above rather than relaying a number I could not reproduce.

**Additional defects found — all REPORTED, NOT FIXED:**

1. `ISSUE_REGISTER.md:55` states `grep -in "settings key"` returns one hit at `:56`.
   It does not — literal match is exit 1 / zero. Only a regex matches:
   `grep -in "settings.*key"` → `56:**How to apply:** treat the settings \`agent\` key AND ...`.
   The row's substantive point (line 56 is unrelated content) holds; the command it
   states does not produce the result it reports. Append-only ledger, out of scope.
2. `ISSUE_REGISTER.md:55` argues "this project's correction pattern preserves
   superseded text verbatim and deletes nothing." The target file refutes that at
   line 8: "**This file previously recorded the opposite claim. That claim is
   REFUTED. Do not act on it.**" — no verbatim preservation. The argument is
   overstated as applied to this file. The marker's own present-tense wording
   ("this quotation is absent") is correctly scoped and stands regardless.
3. Brief line-number precision: in `null-attack.md` the quotation **spans 314–315**
   (begins at 314); in `s9-control.md` it sits wholly on 197 as stated.
4. The false quotation also appears in five other reports (session-40 and today's
   C1 marker reports). Those are secondary quotation *about* the defect and are
   untracked, not staged. Not touched — outside this brief.
5. The worker reported a third false-null mechanism encountered live: `tr` aborting
   with `Illegal byte sequence` and silently skipping ~20 files until `LC_ALL=C`
   was forced. Recorded for the project's false-null catalogue.

## S6 cross-block check

**Not applicable, with reason.** No `PreToolUse` deny fired during this unit and no
gated operation was attempted — no commit, no guarded path written. The parallel-
deny masking hazard (only the last deny message surfaces) requires at least one
deny to be at risk of misattribution; none occurred. No trip test was run, and none
is claimed.

## Files staged

Exactly two paths re-staged, both pre-existing in the index:

- `docs/reports/2026-07-26-session36-null-attack.md`
- `docs/reports/2026-07-26-session36-agent-key-s9-control.md`

Index unchanged at 7 paths. Nothing rode along. **This report is deliberately NOT
staged**, per the brief.

## Result

**Result: PASS** — for the unit as briefed. The correction landed at both sites, is
provably additive, is correctly staged, the index is exactly 7 paths and `HEAD` is
unmoved at `c1dec30`.

**With one escalated blocker that is not mine to fix:** the correction marker's own
citation does not resolve in the commit payload (`ISSUE_REGISTER.md` unstaged; row
absent from `HEAD`). Fixing it requires an 8th path and therefore a decision from
the master or Amear. The C1 payload should not commit until that is settled.

---

# Addendum — 2026-08-04: escalation resolved by self-containment

**The body above stands unaltered.** It is the reason this addendum exists and is
deliberately not rewritten.

## Task

The escalated blocker was accepted by the master, who recorded the authorship of
the defect as his own (`DECISION_LOG.md 2026-08-04T18:58Z`) and independently
re-verified the dangling citation before directing the repair. The directed fix is
the smallest possible change: delete exactly this 38-byte substring from each of
the two markers, making each marker self-contained rather than making its citation
resolve.

```
; see ISSUE_REGISTER 2026-08-04T18:45Z
```

**Why self-containment and not resolution:** making the citation resolve requires
staging `ISSUE_REGISTER.md` as an 8th path, breaching both the 7-path constraint
and the terms of Amear's resumption. A self-contained correction needs no citation.
The `ISSUE_REGISTER` row still exists in the worktree and lands with a later commit.

## Rubric criteria addressed (read at source, `specs/SPEC_RUBRIC.md:107,108,113`)

| # | Criterion | Disposition |
|---|---|---|
| S1 | Every claim in a report has pasted command output, not a description of output. | Met — every arm below is pasted, including a positive control for every zero-returning test. |
| S2 | No component is reported at a higher level than the evidence supports. | Met — reported as *staged and byte-verified*, not as committed or audited. The one genuine side effect of this unit is stated rather than absorbed. |
| S3 | Every gate claimed working has been deliberately tripped at least once. | **No hook gate is claimed working in this unit.** See the S6 section — the instrument that *was* negative-tested is the verification tooling, not a hook. |
| S7 | Nothing is committed while any audit box is unchecked. | Met — `HEAD` unmoved at `c1dec30`, no commit attempted. |

## Workers dispatched

| id | mode | outcome |
|---|---|---|
| `a2752e7acbd25fbcb` | ADVERSARIAL | `VERDICT: HOLDS` — byte-identity, adjacency, residue and line counts all attacked; no break. |
| `a97826da80919b98b` | ADVERSARIAL | `VERDICT: BREAK FOUND` — 3 items. 1 in-scope-but-misattributed, 1 soft and already adjudicated, 1 self-classified pre-existing. Adjudication below. |

Neither worker was shown the other's reasoning, and neither was shown mine. Both
were given the artifact and the criterion only. Both were explicitly barred from
writing anywhere, and `.claude/agent-memory/` was named off-limits in both briefs
(a documented prior failure mode in this project); neither wrote to it — see the
mtime table below, where both memory files retain their 14:41 birth time.

## Process log

1. Verified the brief's premise before acting rather than trusting it: `HEAD`, the
   7-path index, and the presence of the dangling substring in the *index* blobs.
2. Snapshotted the pre-edit staged blobs and recorded their object SHAs.
3. Two substring deletions, made directly. This is the documented exception —
   the change is smaller than a single line, in prose files.
4. `git add` on exactly the two paths (the re-stage trap; both were already staged
   with the dangling text, so an unstaged edit would have shipped the old bytes).
5. Byte-level verification against the pre-edit blobs, with positive controls.
6. Two independent adversarial workers on disjoint axes, dispatched in parallel.
7. Re-ran both workers' in-scope claims myself before accepting or rejecting them.

## Verification evidence (pasted output only)

### The corrected passages, read from the index

```
----- :docs/reports/2026-07-26-session36-agent-key-s9-control.md
197:advises "do not propose the settings key as a way to set `agent_type`." [correction 2026-08-04: this quotation is absent from the target file] **That guidance is now
----- :docs/reports/2026-07-26-session36-null-attack.md
315:key as a way to set `agent_type`." [correction 2026-08-04: this quotation is absent from the target file] That guidance is wrong and should be corrected by
```

### Index blob SHAs moved — proof the re-stage actually happened

Before:

```
100644 a699aaffd4d1e8acc8d9e7e376dac16173ca8666 0	docs/reports/2026-07-26-session36-agent-key-s9-control.md
100644 eaf5b8987c1d365462daa5a81e62185885b6dfa6 0	docs/reports/2026-07-26-session36-null-attack.md
```

After:

```
100644 903f4dd8babd76dbaed4ee21757a7c6014ee3264 0	docs/reports/2026-07-26-session36-agent-key-s9-control.md
100644 bd26551c4f4f326b31507a0c6567facd7509269f 0	docs/reports/2026-07-26-session36-null-attack.md
```

The pre-edit blobs remain retrievable from the object store, which is what let the
adversarial workers reconstruct the baseline without trusting my scratchpad:

```
a699aaff type=blob size=10929
eaf5b898 type=blob size=14654
```

### Byte-exact deletion — nothing else moved

Reconstruction test: prior blob with exactly one occurrence of the substring
removed, compared byte-for-byte against the current staged blob.

```
substring being deleted = '; see ISSUE_REGISTER 2026-08-04T18:45Z'  (len=38 bytes)

----- docs/reports/2026-07-26-session36-agent-key-s9-control.md
  occurrences of substring  pre=1  post=0   (want 1 -> 0)
  bytes                     pre=10929 post=10891  delta=38 (want 38)
  lines                     pre=219 post=219  (want equal)
  POST == PRE minus exactly that substring, byte-identical : True
  POSITIVE CONTROL a (post vs untouched pre) must be False  : False
  POSITIVE CONTROL b (drop one extra byte) must be False    : False
  self-contained marker present                             : True
  local-only citation marker preserved                      : 1

----- docs/reports/2026-07-26-session36-null-attack.md
  occurrences of substring  pre=1  post=0   (want 1 -> 0)
  bytes                     pre=14654 post=14616  delta=38 (want 38)
  lines                     pre=328 post=328  (want equal)
  POST == PRE minus exactly that substring, byte-identical : True
  POSITIVE CONTROL a (post vs untouched pre) must be False  : False
  POSITIVE CONTROL b (drop one extra byte) must be False    : False
  self-contained marker present                             : True
  local-only citation marker preserved                      : 1

ALL CHECKS PASS: True
script exit=0
```

Both positive controls return `False` as required, so the equality test is capable
of failing. A `True` from a comparison that can never return `False` is not evidence.

### Residue null test, with a live control arm

```
=== NULL TEST: dangling substring anywhere in the 7 staged blobs ===
-- TEST ARM (want 0 everywhere) --
0  .gitignore
0  docs/reports/2026-07-26-session36-adversarial-actor-hunt.md
0  docs/reports/2026-07-26-session36-agent-key-audit.md
0  docs/reports/2026-07-26-session36-agent-key-lab.md
0  docs/reports/2026-07-26-session36-agent-key-s9-control.md
0  docs/reports/2026-07-26-session36-null-attack.md
0  docs/reports/2026-07-26-session36-worker-trigger-probe.md
-- POSITIVE CONTROL: same loop, same engine, pattern known present (want nonzero on the two) --
0  .gitignore
0  docs/reports/2026-07-26-session36-adversarial-actor-hunt.md
0  docs/reports/2026-07-26-session36-agent-key-audit.md
0  docs/reports/2026-07-26-session36-agent-key-lab.md
1  docs/reports/2026-07-26-session36-agent-key-s9-control.md
1  docs/reports/2026-07-26-session36-null-attack.md
0  docs/reports/2026-07-26-session36-worker-trigger-probe.md
```

The control fires on exactly the two files that should carry a marker, through the
identical loop and engine. The all-zero test arm is therefore a real negative.

### Re-stage trap cleared — no unstaged residue

```
-- positive arm: a path known modified but unstaged --
 M .claude/settings.json
 M AUDIT_LOG.md
 M DECISION_LOG.md
-- negative arm: the two corrected paths (empty = no residue) --
(no unstaged residue)
-- their porcelain status --
A  docs/reports/2026-07-26-session36-agent-key-s9-control.md
A  docs/reports/2026-07-26-session36-null-attack.md
```

### Index before and after — unchanged, as required

Before:

```
8	0	.gitignore
226	0	docs/reports/2026-07-26-session36-adversarial-actor-hunt.md
385	0	docs/reports/2026-07-26-session36-agent-key-audit.md
287	0	docs/reports/2026-07-26-session36-agent-key-lab.md
219	0	docs/reports/2026-07-26-session36-agent-key-s9-control.md
328	0	docs/reports/2026-07-26-session36-null-attack.md
131	0	docs/reports/2026-07-26-session36-worker-trigger-probe.md
paths=7 additions=1584 deletions=0
```

After:

```
8	0	.gitignore
226	0	docs/reports/2026-07-26-session36-adversarial-actor-hunt.md
385	0	docs/reports/2026-07-26-session36-agent-key-audit.md
287	0	docs/reports/2026-07-26-session36-agent-key-lab.md
219	0	docs/reports/2026-07-26-session36-agent-key-s9-control.md
328	0	docs/reports/2026-07-26-session36-null-attack.md
131	0	docs/reports/2026-07-26-session36-worker-trigger-probe.md
paths=7 additions=1584 deletions=0
```

Identical. No count moved, which is the required outcome: the substring sits inside
existing lines, so a moved line count would have meant something else changed.

### HEAD unmoved

```
c1dec30c6516edcf7c79a78fce5c655e007d7ba2
```

## Adversarial findings

### Worker `a2752e7acbd25fbcb` — VERDICT: HOLDS

Attacked byte-identity, adjacency damage, residual fragments, `local-only` marker
counts, line counts and trailing bytes. It independently confirmed baseline
fidelity by re-hashing the retrieved blobs back to the quoted SHAs. Its residual
scan for `ISSUE_REGISTER`, `18:45`, `T18:45`, `18:45Z`, `; see`, `REGISTER` and
`see ISSUE` returned 0 in both staged files, each paired with a control on the
prior blobs returning 1 — so every zero is a demonstrated negative. Adjacency
evidence, which is the check most likely to catch a sloppy deletion:

```
A_prior:  ...target file; see ISSUE_REGISTER 2026-08-04T18:45Z] **That guidance is now...
A_staged: ...target file] **That guidance is now...
B_prior:  ...target file; see ISSUE_REGISTER 2026-08-04T18:45Z] That guidance is wrong...
B_staged: ...target file] That guidance is wrong...
```

The closing `]` survives in both. Nothing adjacent was eaten. I reproduced this
result independently before accepting it.

### Worker `a97826da80919b98b` — VERDICT: BREAK FOUND, adjudicated

**Item 1 — "new files created as a side effect." REJECTED as stated, but it
surfaced a real one.** The worker attributed four file creations and four ledger
modifications to this unit on the strength of a shared time window. The mtimes
refute the attribution: every flagged artifact predates my edits.

```
=== NOW ===
2026-08-04 15:09:09

birth=15:00:05  mod=15:00:05  docs/reports/2026-07-26-session36-agent-key-s9-control.md
birth=15:00:06  mod=15:00:06  docs/reports/2026-07-26-session36-null-attack.md
birth=14:37:04  mod=14:37:04  docs/reports/2026-08-04-session41-c1-marker-worker1.md
birth=14:40:38  mod=14:40:38  docs/reports/2026-08-04-session41-c1-citation-markers.md
birth=14:56:33  mod=14:56:33  docs/reports/2026-08-04-session41-c1-false-quote.md
birth=14:41:00  mod=14:41:00  .claude/agent-memory/praxis-manager/project_citation_vs_pasted_evidence.md
birth=14:41:09  mod=14:41:09  .claude/agent-memory/praxis-manager/MEMORY.md
birth=14:58:33  mod=14:58:33  DECISION_LOG.md
birth=14:43:05  mod=14:43:05  ISSUE_REGISTER.md
birth=14:44:24  mod=15:08:37  DISPATCH_LOG.md
```

All flagged artifacts are 14:37–14:58; my edits are 15:00:05 and 15:00:06. They
belong to the **prior** C1 marker unit, not this one. The two `.claude/agent-memory/`
files are the manager's own namespace, written at 14:41 in the prior unit, and are
untouched here — which also disposes of any suggestion that a worker wrote there.

**But the worker's mechanism was sound even though its attribution was wrong, and
it caught one thing I would otherwise have missed:** `DISPATCH_LOG.md` has
`mod=15:08:37`, which is *after* my edits and therefore genuinely inside this unit.
I traced the cause rather than assuming it:

```
=== who writes DISPATCH_LOG.md? hook registration ===
118:            "command": "./scripts/dispatch-log-writeahead.sh"
137:            "command": "\"$CLAUDE_PROJECT_DIR\"/scripts/dispatch-log-close.sh",
```

```
- [2026-08-04T19:01:56Z] WHO: praxis-worker | WHAT: subagent spawned | ... corr=a2752e7acbd25fbcb | STATE: dispatched
- [2026-08-04T19:02:16Z] WHO: praxis-worker | WHAT: subagent spawned | ... corr=a97826da80919b98b | STATE: dispatched
- [2026-08-04T19:03:27Z] WHO: praxis-worker | WHAT: subagent closed | ... corr=a2752e7acbd25fbcb | STATE: closed
- [2026-08-04T19:08:37Z] WHO: praxis-worker | WHAT: subagent closed | ... corr=a97826da80919b98b | STATE: closed
```

The corr IDs match my two dispatched workers exactly. These rows are written
automatically by the registered `SubagentStart`/`SubagentStop` hooks, by design, and
`DISPATCH_LOG.md` was already modified before this unit began. **It is not staged:**

```
=== is DISPATCH_LOG.md staged? (want: NOT staged) ===
0
-- positive control: same pipeline, pattern known present in staged set --
1
```

So the commit payload is unaffected. Stated here rather than absorbed, because
"this unit modified no file outside the two" would have been false.

**Item 2 — 4 unresolvable filenames inside staged blobs. REJECTED, on an already
adjudicated rule.** The worker itself flagged this as soft. I verified the context
directly:

```
--- docs/reports/2026-07-26-session36-agent-key-audit.md
39- M DECISION_LOG.md
40- M DISPATCH_LOG.md
41- M ISSUE_REGISTER.md
42-?? .claude/agent-memory/
43:?? docs/reports/2026-07-26-session34-manifest-amendment.md
--- docs/reports/2026-07-26-session36-agent-key-lab.md
256- M DECISION_LOG.md
257- M DISPATCH_LOG.md
258- M ISSUE_REGISTER.md
259-?? .claude/agent-memory/
260:?? docs/reports/2026-07-26-session34-manifest-amendment.md
```

Those filenames appear only inside pasted `git status --porcelain` output. A path
inside pasted command output is **evidence, not a citation** — annotating it would
corrupt the transcript of a real command and breach S1, which requires pasted output
to be pasted output. This is the project's settled position on the distinction, and
the worker rediscovered it independently from a cold start, which corroborates the
rule rather than challenging it. No change made.

**Item 3 — pre-existing untracked clutter (the root file `F`, ~25 stale report
files).** Correctly self-classified by the worker as not caused by this unit.
Confirmed. Untouched, and none of it is staged.

## S6 cross-block check

**No hook gate was tripped, and none is claimed working.** No `PreToolUse` deny
fired during this unit; no commit was attempted and no guarded path was written.
The parallel-deny masking hazard — where only the last of several concurrent deny
messages surfaces, so a trip test can display the wrong block string — requires at
least one deny to be at risk of misattribution. None occurred, so it is not
implicated.

**I deliberately declined to trip the commit gate as a negative test.** Doing so
would mean attempting a commit, and if the gate failed open the result would be the
precise outcome this brief forbids: a moved `HEAD`. A gate whose failure mode is
indistinguishable from the prohibited action cannot be safely probed inside a unit
constrained to leave `HEAD` at `c1dec30`. That is a real, unclosed gap in this
unit's evidence, stated as a gap rather than papered over.

**What *was* negative-tested is the verification instrument**, which is where the
risk actually sat in this unit: the byte-equality test carries two positive controls
that must return `False` and do; the residue scan carries a control arm that fires
on the prior blobs; the residue detector carries a positive arm on a known-modified
file. Every zero reported above comes from a method demonstrated capable of
returning non-zero.

## Files staged

Exactly two paths re-staged, both already present in the index:

- `docs/reports/2026-07-26-session36-agent-key-s9-control.md`
- `docs/reports/2026-07-26-session36-null-attack.md`

Index unchanged at 7 paths / 1584 additions / 0 deletions. Nothing rode along.
**This report remains deliberately unstaged**, per the brief.

## Result

**Result: PASS.** The dangling citation is gone from both markers in the index; each
marker is now self-contained. The deletion is provably exactly the 38-byte substring
and nothing else, verified byte-for-byte against the pre-edit blobs and independently
re-derived by an adversarial worker from the git object store. Line counts held at
219 and 328, the index is unchanged at 7 paths / 1584 / 0, and `HEAD` is unmoved at
`c1dec30`.

The escalation recorded in the body above is **resolved**: the marker no longer makes
a claim the committed payload cannot support. The `ISSUE_REGISTER` row it formerly
cited remains in the worktree and lands with a later commit, which is now a
scheduling detail rather than a correctness defect.

One residual gap is carried forward rather than closed: the commit gate itself was
not trip-tested, for the reason given in the S6 section.

---

# Appendix A — two unrecorded findings, held for transplant

Both were encountered live in this unit's predecessor and in this unit. Neither has
been written to `.claude/agent-memory/`, because the governing brief forbade it and
a later brief confirmed that was the correct call. They are recorded here in
transplantable form. **The master is seeking the grant to persist them.** If it is
granted, the two fenced blocks below can be moved verbatim into
`.claude/agent-memory/praxis-manager/` as complete memory files, with one index line
each added to `MEMORY.md`.

## A.1 — `tr` returns a false null under `Illegal byte sequence`

```markdown
---
name: false-null-locale-tr
description: tr/sed/awk abort on UTF-8 input with "Illegal byte sequence" and silently skip the rest, manufacturing a false zero; force LC_ALL=C.
metadata:
  type: project
---

On macOS/BSD, `tr` (and `sed`/`awk` in the same family) abort with
`tr: Illegal byte sequence` when they meet a byte the current locale cannot
decode. The abort is **per-invocation and non-fatal to the surrounding loop**:
inside a `for` loop over files, the tool dies on the first offending file and the
loop marches on, so the aggregate result looks like a clean zero. Observed live
while scanning this repo's reports, where ~20 files were silently skipped before
`LC_ALL=C` was forced. The repo's markdown is full of UTF-8 em-dashes (`—`,
`\xe2\x80\x94`), so this is the normal case here, not an edge case.

**Why:** a zero from an aborted scan is indistinguishable from a zero from a
completed scan unless exit status is checked per-file — and in a pipeline the
exit status that survives is the *last* command's, not `tr`'s. This is the third
distinct false-null mechanism catalogued in this project, after the two recorded
in [[false-null-hazard]].

**How to apply:** prefix `LC_ALL=C` on any `tr`/`sed`/`awk` that touches repo
markdown, and prefer `python3` byte-level comparison for anything load-bearing
(byte-identity, additivity, residue scans). When a text-tool scan returns zero,
require a positive control arm through the identical pipeline before believing
it. If a run printed `Illegal byte sequence` anywhere, treat every zero from that
run as unproven and re-run under `LC_ALL=C`. Related: [[false-null-hazard]],
[[citation-vs-pasted-evidence]].
```

## A.2 — `git diff --cached` cannot prove additivity for a new file

```markdown
---
name: new-file-diff-cannot-prove-additivity
description: For a `new file mode` path, the staged diff is against /dev/null, so it structurally cannot show a deletion — additivity must be proven against the prior blob.
metadata:
  type: project
---

`git diff --cached` on a path staged as `new file mode` diffs the blob against
`/dev/null`. Every line is therefore rendered as an addition, and **no deletion
can ever appear**, no matter what was removed from the file since it was last
staged. `--numstat` on such a path reports `<total-lines> 0 <path>` — the `0`
deletions column is a structural artefact of the `/dev/null` baseline, not a
finding about the edit. Re-staging a new-file path after silently deleting half
its content produces a diff that still looks purely additive.

**Why:** this defeats the obvious check. "The staged diff shows 0 deletions,
therefore my edit was additive" is invalid reasoning for any untracked-then-staged
file, which in this project is every report under `docs/reports/`. The trap is
worse when a constraint is expressed as a numstat target (e.g. "1584 additions, 0
deletions"), because the numbers can be fully satisfied by a payload that lost
text.

**How to apply:** to prove additivity or byte-exactness for a `new file mode`
path, compare against the **prior blob**, not the diff. `git add` writes blobs
into the object store, so the pre-edit version survives at its old SHA
(`git ls-files -s <path>` before editing; `git cat-file -p <sha>` after) even
though no commit references it. Reconstruct — `prior.replace(expected_change)` —
and assert byte-equality against `git show :<path>`, with a positive control that
must return `False`. Give an adversarial worker the prior SHA so it can rebuild
the baseline without trusting the producer's scratchpad. Related:
[[false-null-locale-tr]], [[citation-vs-pasted-evidence]].
```

---

# ADDENDUM — C1 expansion 7 → 11 paths (staging only)

## Task

`git add` four existing untracked report files identified by the master's
path-space bidirectional citation check as **dangling citations of the second
class**: the cited reports exist on disk and were simply never committed. This
is distinct from the `agent-memory` class already handled in the body above.

Authorisation: `DECISION_LOG.md` `2026-08-04T20:10Z`, `WHO: amear`, expanding
C1 from 7 paths to 11. **Staging only — no content edits to any file.**

## Rubric criteria addressed

- **S1** — every claim below is pasted command output.
- **S4** — the expansion is a deviation from the 7-path C1 plan and carries a
  pre-written `DECISION_LOG.md` entry with `WHO: amear`. I did not author it.
- **S5** — the authorisation is the ledger append, not the brief's prose.
- **S7** — nothing committed; `HEAD` verified unmoved.

## Workers dispatched

**None.** Brief set `MAX 0 praxis-worker spawns`. Four `git add`s and a
verification do not decompose. No worker was spawned.

## Process log

1. Captured baseline `HEAD`, `git status --short`, `git diff --cached --numstat`.
2. Verified the premise per-file: existence, tracked state, ignore state.
3. Staged the four paths in a single `git add --` with explicit pathspecs.
4. Verified final index, per-path line counts, totals, and `HEAD`.
5. Ran scope/secret/mode/blob-integrity checks on the newly staged blobs.

## Verification evidence (pasted output only)

### Premise check — before staging

```
$ git rev-parse HEAD
c1dec30c6516edcf7c79a78fce5c655e007d7ba2

=== docs/reports/2026-07-26-session34-manifest-amendment.md
exists: YES
ls-files(tracked): (untracked)
ignored?: (not ignored)
=== docs/reports/2026-07-26-session34-p0-flush-audit.md
exists: YES
ls-files(tracked): (untracked)
ignored?: (not ignored)
=== docs/reports/2026-07-26-session35-8sw-audit-round1.md
exists: YES
ls-files(tracked): (untracked)
ignored?: (not ignored)
=== docs/reports/2026-07-26-session35-8sw-gate-park-conflict.md
exists: YES
ls-files(tracked): (untracked)
ignored?: (not ignored)
```

All four: present, untracked, not ignored. **Premise held.** No divergence.

### `git diff --cached --numstat` — BEFORE (7 paths)

```
8	0	.gitignore
226	0	docs/reports/2026-07-26-session36-adversarial-actor-hunt.md
385	0	docs/reports/2026-07-26-session36-agent-key-audit.md
287	0	docs/reports/2026-07-26-session36-agent-key-lab.md
219	0	docs/reports/2026-07-26-session36-agent-key-s9-control.md
328	0	docs/reports/2026-07-26-session36-null-attack.md
131	0	docs/reports/2026-07-26-session36-worker-trigger-probe.md
```

### Staging command

```
$ git add -- "docs/reports/2026-07-26-session34-manifest-amendment.md" \
             "docs/reports/2026-07-26-session34-p0-flush-audit.md" \
             "docs/reports/2026-07-26-session35-8sw-audit-round1.md" \
             "docs/reports/2026-07-26-session35-8sw-gate-park-conflict.md"
ADD-EXIT: 0
```

### `git diff --cached --numstat` — AFTER (11 paths)

```
8	0	.gitignore
419	0	docs/reports/2026-07-26-session34-manifest-amendment.md
614	0	docs/reports/2026-07-26-session34-p0-flush-audit.md
172	0	docs/reports/2026-07-26-session35-8sw-audit-round1.md
3036	0	docs/reports/2026-07-26-session35-8sw-gate-park-conflict.md
226	0	docs/reports/2026-07-26-session36-adversarial-actor-hunt.md
385	0	docs/reports/2026-07-26-session36-agent-key-audit.md
287	0	docs/reports/2026-07-26-session36-agent-key-lab.md
219	0	docs/reports/2026-07-26-session36-agent-key-s9-control.md
328	0	docs/reports/2026-07-26-session36-null-attack.md
131	0	docs/reports/2026-07-26-session36-worker-trigger-probe.md
```

```
$ git diff --cached --numstat | awk '{a+=$1; d+=$2; n++} END {print "paths="n"  added="a"  deleted="d}'
paths=11  added=5825  deleted=0

$ git diff --cached --shortstat
 11 files changed, 5825 insertions(+)
```

**Path count: 11.** Target met.

### The seven pre-existing paths are byte-for-byte unmoved

| Path | Required | Observed |
|---|---|---|
| `.gitignore` | 8 | 8 |
| `…session36-adversarial-actor-hunt.md` | 226 | 226 |
| `…session36-agent-key-audit.md` | 385 | 385 |
| `…session36-agent-key-lab.md` | 287 | 287 |
| `…session36-agent-key-s9-control.md` | 219 | 219 |
| `…session36-null-attack.md` | 328 | 328 |
| `…session36-worker-trigger-probe.md` | 131 | 131 |

All seven match. Nothing rode along. No finding.

### `git status --short` — AFTER

```
 M .claude/settings.json
M  .gitignore
 M AUDIT_LOG.md
 M DECISION_LOG.md
 M DISPATCH_LOG.md
 M HANDOFF.md
 M ISSUE_REGISTER.md
 M MANIFEST.md
 M STATUS.md
A  docs/reports/2026-07-26-session34-manifest-amendment.md
A  docs/reports/2026-07-26-session34-p0-flush-audit.md
A  docs/reports/2026-07-26-session35-8sw-audit-round1.md
A  docs/reports/2026-07-26-session35-8sw-gate-park-conflict.md
A  docs/reports/2026-07-26-session36-adversarial-actor-hunt.md
A  docs/reports/2026-07-26-session36-agent-key-audit.md
A  docs/reports/2026-07-26-session36-agent-key-lab.md
A  docs/reports/2026-07-26-session36-agent-key-s9-control.md
A  docs/reports/2026-07-26-session36-null-attack.md
A  docs/reports/2026-07-26-session36-worker-trigger-probe.md
 M scripts/dispatch-log-writeahead.sh
 M specs/SPEC_RUBRIC.md
?? F
?? docs/reports/2026-07-26-session36-manifest-and-memory.md
?? docs/reports/2026-07-27-session36-park-rule-escalation.md
?? docs/reports/2026-07-27-session37-restage-audit.md
?? docs/reports/2026-07-27-session37-restage-split.md
?? docs/reports/2026-07-27-session38-guard-evasion-test.md
?? docs/reports/2026-07-28-session39-agents-dir-write-path.md
?? docs/reports/2026-07-28-session39-closer-negative-tests.md
?? docs/reports/2026-07-28-session39-dispatch-log-closer-adversarial.md
?? docs/reports/2026-07-28-session39-dispatch-log-closer-build.md
?? docs/reports/2026-07-28-session39-dispatch-log-closer.md
?? docs/reports/2026-07-28-session39-live-vs-piped-attack.md
?? docs/reports/2026-07-28-session40-agent-memory-disposition.md
?? docs/reports/2026-07-28-session40-cbf-audit.md
?? docs/reports/2026-07-28-session40-ignore-and-citation-adversarial.md
?? docs/reports/2026-07-28-session40-memory-correction-adversarial.md
?? docs/reports/2026-07-30-session41-cyd-audit.md
?? docs/reports/2026-07-30-session41-cyd-four-hook-claim.md
?? docs/reports/2026-07-30-session41-cyd-worker1-hook-experiment.md
?? docs/reports/2026-07-30-session41-cyd-worker2-adversarial.md
?? docs/reports/2026-08-03-session41-cyd-fix-adversarial.md
?? docs/reports/2026-08-03-session41-cyd-fix-audit.md
?? docs/reports/2026-08-03-session41-cyd-fix-worker1.md
?? docs/reports/2026-08-03-session41-cyd-fix.md
?? docs/reports/2026-08-04-session41-c1-citation-markers.md
?? docs/reports/2026-08-04-session41-c1-false-quote.md
?? docs/reports/2026-08-04-session41-c1-marker-worker1.md
?? scripts/dispatch-log-close.sh
?? scripts/tests/test-dispatch-log-close.sh
```

The only status transitions are the four target paths, `??` → `A `. Every
worktree-modified path (`.claude/settings.json`, the seven ledgers,
`scripts/dispatch-log-writeahead.sh`, `specs/SPEC_RUBRIC.md`) remains ` M` —
unstaged, untouched. This report itself remains `??` — **not staged**, as
required.

### `HEAD` unmoved

```
$ git rev-parse HEAD
c1dec30c6516edcf7c79a78fce5c655e007d7ba2
```

Identical to the baseline. No commit. No token minted — `.claude/state/`
contains only `current-bead`, `iteration-count`, `max-iterations`,
`orchestrator-active`, `run-mode`; there is no audit-token file:

```
$ ls -la .claude/state/
total 32
drwxr-xr-x@ 7 admin  staff  224 Jul 27 16:26 .
drwxr-xr-x@ 8 admin  staff  256 Jul 28 16:10 ..
-rw-r--r--@ 1 admin  staff   17 Jul 27 16:26 current-bead
-rw-r--r--@ 1 admin  staff    2 Jul 10 11:05 iteration-count
-rw-r--r--@ 1 admin  staff    3 Jul  9 16:18 max-iterations
-rw-r--r--@ 1 admin  staff    0 Jul 26 09:53 orchestrator-active
-rw-r--r--@ 1 admin  staff   12 Jul 26 09:53 run-mode
```

### Scope, mode, and secret checks on the newly staged blobs

```
$ git ls-files -s -- <the four paths>
100644 a5b19b0a38f7f6cbd4ab176705c8a64ee8c21db9 0	docs/reports/2026-07-26-session34-manifest-amendment.md
100644 ae9ccdf8825257685e03bc6182db12f1a59bff67 0	docs/reports/2026-07-26-session34-p0-flush-audit.md
100644 b687998e78000cefd227e9f6335406fd3959a875 0	docs/reports/2026-07-26-session35-8sw-audit-round1.md
100644 cb60251ead0790e744f7f1ca1e332d75464616e0 0	docs/reports/2026-07-26-session35-8sw-gate-park-conflict.md

SECRET-SCAN-HITS: 0
```

All four are regular `100644` blobs at stage 0 — no mode bits, no merge
conflict stages, no symlinks. Secret scan (private-key headers, `sk-`, `AKIA`,
`ghp_`, `xox[baprs]-`) returns zero hits.

### Proof no content was edited

The body of this report establishes that a `new file mode` numstat cannot
show deletions, so "0 deletions" proves nothing about content preservation.
The correct check for a **staging-only** operation is different and stronger:
the staged blob SHA must equal the worktree file's hash, which proves the index
holds exactly the bytes on disk and that nothing was rewritten en route.

```
MATCH (unmodified): docs/reports/2026-07-26-session34-manifest-amendment.md
MATCH (unmodified): docs/reports/2026-07-26-session34-p0-flush-audit.md
MATCH (unmodified): docs/reports/2026-07-26-session35-8sw-audit-round1.md
MATCH (unmodified): docs/reports/2026-07-26-session35-8sw-gate-park-conflict.md
```

(`git hash-object <file>` vs `git ls-files -s <file>` blob SHA, per path.)

## Adversarial findings

No adversarial worker was dispatched — the brief set MAX 0 spawns, and the
operation has no artefact to attack: it produces no code, no logic, and no
content change. I ran the adversarial checks myself instead:

1. **Did anything else enter the index?** No — `git status --short` diffed
   against baseline shows exactly four ` ?? → A ` transitions and no others.
2. **Did the seven prior paths shift?** No — all seven line counts identical.
3. **Was content silently altered by staging?** No — blob SHA equals worktree
   hash for all four (the `new file mode` numstat trap does not apply, because
   the check is hash equality, not diff shape).
4. **Was a commit or token produced?** No — `HEAD` unmoved, `.claude/state/`
   holds no token file.

**One observation worth flagging, not a defect:**
`2026-07-26-session35-8sw-gate-park-conflict.md` is **3036 lines** — larger
than the other ten staged paths combined minus one. It dominates the 5825-line
total. I did not edit it and the brief forbids doing so, but the master should
know that C1's payload is now majority one file, and that if any size or
review-scope limit applies to the eventual commit, this is the path that
triggers it.

## S6 cross-block check

Staging touches the index only. Blocks that could plausibly interact:

- **Commit gate** (`gate-commit.sh`, `no-commit-guard.sh`) — not invoked; no
  commit attempted. The index growing from 7 to 11 paths does not arm or
  disarm any gate; the gates key on the command string, not on index size.
- **Citation integrity (C1's own block)** — the four paths were dangling
  *targets*. Staging them converts them from "cited but never committed" to
  "cited and staged for commit", which is the intended repair direction and
  cannot create a new dangling citation, since no citation text changed.
- **`.gitignore`** (staged, 8 lines) — confirmed via `git check-ignore -v`
  that none of the four paths is ignored, so the ignore change and the staging
  change do not conflict.
- **MANIFEST.md** — remains ` M` and unstaged. Per project rules, new files
  warrant a MANIFEST entry; these four are pre-existing reports being staged,
  and MANIFEST is outside this brief's scope. **Flagged to the master** rather
  than silently actioned.
- **`.claude/agent-memory/`, guard scripts, `.claude/agents/*`,
  `specs/SPEC_RUBRIC.md`, hooks** — untouched; all remain unstaged, and
  `SPEC_RUBRIC.md` was read only.

No cross-block breakage.

## Files staged

Newly staged by this addendum (4):

- `docs/reports/2026-07-26-session34-manifest-amendment.md` (419)
- `docs/reports/2026-07-26-session34-p0-flush-audit.md` (614)
- `docs/reports/2026-07-26-session35-8sw-audit-round1.md` (172)
- `docs/reports/2026-07-26-session35-8sw-gate-park-conflict.md` (3036)

Already staged, unchanged (7): `.gitignore` (8) and the six session-36 reports
(226 / 385 / 287 / 219 / 328 / 131).

**Index total: 11 paths, 5825 insertions, 0 deletions.**

This report is **not** staged and remains untracked, per the brief.

## Result: PASS
