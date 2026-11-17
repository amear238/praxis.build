# Session 41 — C1 citation markers

## Task

Repair the dangling-citation half of the C1 audit FAIL:

1. Add the approved inline marker `[local-only — not in this repo by design]` at the two
   citation sites that point into the deliberately gitignored `.claude/agent-memory/`.
2. Stage `.gitignore` alongside the six already-staged `docs/reports/2026-07-26-session36-*.md`,
   so the "by design" assertion in the marker is backed by something the repository actually
   records.

Authority: this lineage is parked at audit FAIL 2 under the absolute park rule. It runs only
because Amear resumed it explicitly — `DECISION_LOG.md` `2026-08-04T18:33Z`, `WHO: amear`.
The applying ruling is `DECISION_LOG.md` `2026-08-04T17:50Z`. Both rows were read at source
before any work started. Nothing here commits, and nothing here mints a token.

## Rubric criteria addressed

Read at source in `specs/SPEC_RUBRIC.md`; line numbers verified this session.

| # | Line | Criterion |
|---|------|-----------|
| S1 | `:107` | Every claim in a report has pasted command output, not a description of output. |
| S2 | `:108` | No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure. |
| S7 | `:113` | Nothing is committed while any audit box is unchecked. |

## Workers dispatched

| id | mode | scope | outcome |
|----|------|-------|---------|
| `a5b85e845b5239f55` | BUILD | the two marker insertions; no git mutation, no staging | returned PASS — **independently re-verified by me, upheld on the artifact; one over-claim found in its report (below)** |

**Worker count: 1.** The brief caps this unit at 1 spawn, so the adversarial pass was run by
me directly rather than delegated to a second worker. That is a real reduction in independence
and is stated rather than papered over: the adversarial checks below were run by the same agent
that dispatched the build, though every one of them is a deterministic byte- or git-level check
whose output is reproducible by the auditor.

I did not perform the edits myself. Keeping production in the worker's hands preserves the one
separation still available under a 1-spawn cap — I review an artifact I did not author.

## Process log

1. Captured baseline: `HEAD` = `c1dec30`, index = 6 paths / 1,576 additions / 0 deletions.
2. Read `specs/SPEC_RUBRIC.md` and confirmed S1/S2/S7 verbatim at lines 107/108/113.
3. Read both `DECISION_LOG.md` rows (`17:50Z`, `18:33Z`) at source.
4. **Re-verified the brief's premises before editing.** Both cited line numbers and their
   surrounding text matched exactly — `null-attack.md:313`, `agent-key-s9-control.md:196`.
   No divergence to report.
5. Swept all six staged reports for `agent-memory` to test whether the brief's two sites were
   exhaustive. They are — see Finding A.
6. Inspected the full unstaged `.gitignore` diff before staging it, to be sure staging the
   whole file dragged nothing along. It did not — see Finding B.
7. Captured pre-edit SHA-256 and line counts of both target files.
8. Dispatched worker 1 (BUILD) with exact `old_string`/`new_string` pairs.
9. Re-ran every verification myself; added byte-level and pure-insertion proofs the worker
   was not asked for.
10. Staged `.gitignore` + the two edited reports. Verified the resulting index.
11. Ran the negative test and S6 cross-block check, each with a positive control arm.

## Verification evidence

### Baseline (before any change)

```
$ git rev-parse HEAD
c1dec30c6516edcf7c79a78fce5c655e007d7ba2

$ git diff --cached --numstat | awk '{a+=$1; d+=$2; n++} END {print n" paths / "a" additions / "d" deletions"}'
6 paths / 1576 additions / 0 deletions
```

```
$ shasum -a 256 docs/reports/2026-07-26-session36-null-attack.md docs/reports/2026-07-26-session36-agent-key-s9-control.md
70453b0a274df0aa6204804ad0ad375130bdc03feebaaba1cf87b17340ea1329  docs/reports/2026-07-26-session36-null-attack.md
fddd59b726dc1fbf326cc6432beedf04c657f24a1104a80c8eca487b24dc8620  docs/reports/2026-07-26-session36-agent-key-s9-control.md
```

### Premise re-verification (the brief's two sites, before editing)

```
$ sed -n '313p' docs/reports/2026-07-26-session36-null-attack.md
`/Volumes/Sensidine/Praxis.build/.claude/agent-memory/praxis-worker/project_agent-type-source.md`

$ sed -n '196p' docs/reports/2026-07-26-session36-agent-key-s9-control.md
`.claude/agent-memory/praxis-worker/project_agent-type-source.md` records the refuted null and
```

### Exhaustiveness sweep across all six staged reports

```
$ for f in $(git diff --cached --name-only); do echo "--- $f"; grep -n "agent-memory" "$f" || echo "   (none)"; done
--- docs/reports/2026-07-26-session36-adversarial-actor-hunt.md
   (none)
--- docs/reports/2026-07-26-session36-agent-key-audit.md
42:?? .claude/agent-memory/
--- docs/reports/2026-07-26-session36-agent-key-lab.md
259:?? .claude/agent-memory/
--- docs/reports/2026-07-26-session36-agent-key-s9-control.md
196:`.claude/agent-memory/praxis-worker/project_agent-type-source.md` records the refuted null and
--- docs/reports/2026-07-26-session36-null-attack.md
313:`/Volumes/Sensidine/Praxis.build/.claude/agent-memory/praxis-worker/project_agent-type-source.md`
--- docs/reports/2026-07-26-session36-worker-trigger-probe.md
   (none)
```

### The edit — full diff

```
$ git diff --stat -- docs/reports/2026-07-26-session36-null-attack.md docs/reports/2026-07-26-session36-agent-key-s9-control.md
 docs/reports/2026-07-26-session36-agent-key-s9-control.md | 2 +-
 docs/reports/2026-07-26-session36-null-attack.md          | 2 +-
 2 files changed, 2 insertions(+), 2 deletions(-)
```

```
$ git diff -- docs/reports/2026-07-26-session36-null-attack.md docs/reports/2026-07-26-session36-agent-key-s9-control.md
diff --git a/docs/reports/2026-07-26-session36-agent-key-s9-control.md b/docs/reports/2026-07-26-session36-agent-key-s9-control.md
index ac53d5a..ed0edb9 100644
--- a/docs/reports/2026-07-26-session36-agent-key-s9-control.md
+++ b/docs/reports/2026-07-26-session36-agent-key-s9-control.md
@@ -193,7 +193,7 @@ per the single-session rule; not acted on.

 ## 10. Stale artifact flagged, NOT edited

-`.claude/agent-memory/praxis-worker/project_agent-type-source.md` records the refuted null and
+`.claude/agent-memory/praxis-worker/project_agent-type-source.md` [local-only — not in this repo by design] records the refuted null and
 advises "do not propose the settings key as a way to set `agent_type`." **That guidance is now
 false.** It is another agent's memory namespace; flagged for the master, not edited by me.
 `docs/reports/2026-07-26-session36-agent-key-lab.md` is its cited evidence base and carries the
diff --git a/docs/reports/2026-07-26-session36-null-attack.md b/docs/reports/2026-07-26-session36-null-attack.md
index de38b27..c8029e2 100644
--- a/docs/reports/2026-07-26-session36-null-attack.md
+++ b/docs/reports/2026-07-26-session36-null-attack.md
@@ -310,7 +310,7 @@ the only way to set `agent_type`.

 ## 9. Stale artifact flagged (NOT edited — outside my write scope)

-`/Volumes/Sensidine/Praxis.build/.claude/agent-memory/praxis-worker/project_agent-type-source.md`
+`/Volumes/Sensidine/Praxis.build/.claude/agent-memory/praxis-worker/project_agent-type-source.md` [local-only — not in this repo by design]
 records the now-refuted null as a project memory and advises "do not propose the settings
 key as a way to set `agent_type`." That guidance is wrong and should be corrected by
 whoever owns write access to it. Same for
```

### The two edited lines as they now read

```
$ sed -n '313p' docs/reports/2026-07-26-session36-null-attack.md
`/Volumes/Sensidine/Praxis.build/.claude/agent-memory/praxis-worker/project_agent-type-source.md` [local-only — not in this repo by design]

$ sed -n '196p' docs/reports/2026-07-26-session36-agent-key-s9-control.md
`.claude/agent-memory/praxis-worker/project_agent-type-source.md` [local-only — not in this repo by design] records the refuted null and
```

### Line counts unchanged

```
$ wc -l docs/reports/2026-07-26-session36-null-attack.md docs/reports/2026-07-26-session36-agent-key-s9-control.md
     328 docs/reports/2026-07-26-session36-null-attack.md
     219 docs/reports/2026-07-26-session36-agent-key-s9-control.md
     547 total
```

### Marker byte-identity (em dash is U+2014, not a hyphen)

```
$ sed -n '313p' docs/reports/2026-07-26-session36-null-attack.md | tail -c 45 | hexdump -C
00000000  20 5b 6c 6f 63 61 6c 2d  6f 6e 6c 79 20 e2 80 94  | [local-only ...|
00000010  20 6e 6f 74 20 69 6e 20  74 68 69 73 20 72 65 70  | not in this rep|
00000020  6f 20 62 79 20 64 65 73  69 67 6e 5d 0a           |o by design].|
0000002d

$ [ "$m1" = "$m2" ] && echo "IDENTICAL markers: $m1"
IDENTICAL markers: [local-only — not in this repo by design]
```

`e2 80 94` confirms U+2014 EM DASH, matching the approved form in the `17:50Z` ruling.

### Pure-insertion proof (stronger than the diff: proves no character was deleted)

Deleting the marker substring from each new line must restore the staged original byte-for-byte.

```
$ python3 (compare index blob vs working tree, line by line)
marker len = 42 chars (incl leading space)

docs/reports/2026-07-26-session36-null-attack.md:313
  marker occurs exactly once: True
  removing marker restores byte-identical original: True
  all OTHER lines byte-identical: True

docs/reports/2026-07-26-session36-agent-key-s9-control.md:196
  marker occurs exactly once: True
  removing marker restores byte-identical original: True
  all OTHER lines byte-identical: True
```

```
$ git diff -- <the two files> | grep -nE '^\+.*[ \t]+$'
none
```

No trailing whitespace introduced.

### Index after staging

```
$ git diff --cached --numstat
8	0	.gitignore
226	0	docs/reports/2026-07-26-session36-adversarial-actor-hunt.md
385	0	docs/reports/2026-07-26-session36-agent-key-audit.md
287	0	docs/reports/2026-07-26-session36-agent-key-lab.md
219	0	docs/reports/2026-07-26-session36-agent-key-s9-control.md
328	0	docs/reports/2026-07-26-session36-null-attack.md
131	0	docs/reports/2026-07-26-session36-worker-trigger-probe.md
TOTAL: 7 paths / 1584 additions / 0 deletions
```

Delta from baseline: `+1 path, +8 additions` — `.gitignore` and nothing else.

```
$ git diff --cached -- .gitignore
diff --git a/.gitignore b/.gitignore
index b2f75d1..280f86e 100644
--- a/.gitignore
+++ b/.gitignore
@@ -16,3 +16,11 @@ signals/*.json
 # ...except the version-controlled canonical schema template (bead 6h7)
 !signals/signal-template.json
 .claude/state/
+
+# Agent memory — LOCAL ONLY, deliberately never committed (human ruling
+# 2026-07-28, Praxis_build-cbf). Auto-loaded into the context of each agent type.
+# Held out of the repo because this repo is PUBLIC and these notes carry working
+# guard-evasion detail. Consequence, accepted knowingly: any report citing a path
+# under here cites a DECLARED LOCAL-ONLY artifact — it will not resolve for
+# anyone who clones this repo, by design, not by accident.
+.claude/agent-memory/
```

```
$ git diff --name-only -- docs/reports/2026-07-26-session36-null-attack.md docs/reports/2026-07-26-session36-agent-key-s9-control.md
(empty)
```

No unstaged remainder on either edited file — the index holds the marked versions, not a
half-staged state.

### Negative test — is the citation genuinely dangling? (both arms)

The marker asserts the path is not in the repo. Testing that assertion rather than trusting it.

```
$ git ls-files -- .claude/agent-memory/
  ^ tracked files under agent-memory (empty = citation truly dangles)
--- POSITIVE ARM: same command shape on a path that IS tracked ---
$ git ls-files -- .gitignore
.gitignore

$ git log --all --oneline -- .claude/agent-memory/
  ^ (empty = never committed on any branch)
--- POSITIVE ARM ---
$ git log --all --oneline -- .gitignore
de46c56 Praxis_build-6h7 (signal-template schema): regenerate to live consumer contract
291826f Orchestrator scaffold self-install + Jul 6 ledger reconciliation
936d7e4 Step 0.5: n8n signal webhook published
```

Both nulls carry a firing positive arm, so neither is a false null. The path is in no ref on
any branch — the citation really does dangle, and the marker is warranted rather than
decorative.

```
$ git check-ignore -v .claude/agent-memory/praxis-worker/project_agent-type-source.md
.gitignore:26:.claude/agent-memory/	.claude/agent-memory/praxis-worker/project_agent-type-source.md
```

The staged rule is at `.gitignore:26` — matching the line the ruling cites — and it does in
fact match the cited path. The rule is not merely present, it fires on this exact path.

### Negative test NOT run, and why

**The commit gate was not tripped.** My standing protocol asks for a negative test proving the
gate blocks, but the only way to trip `gate-commit.sh` here is to attempt a real commit, and
hard limit 1 of this brief requires `HEAD` to remain `c1dec30`. If the hooks did not fire, the
attempt would succeed and breach the resumption terms irreversibly — an unacceptable trade for
a test whose result is already recorded elsewhere in this project. Stated plainly rather than
skipped silently: **the commit gate is untested in this unit.** S7 is satisfied here by
construction (nothing was committed; `HEAD` verified unmoved at start and end), not by
demonstrating that the gate would have stopped one.

## Adversarial findings

**Finding A — the brief's two sites are exhaustive, and two look-alikes must NOT be marked.**
`agent-key-audit.md:42` and `agent-key-lab.md:259` also contain `.claude/agent-memory/`, but as
`?? .claude/agent-memory/` **inside pasted `git status --short` output**. Those are evidence,
not citations. Marking them would edit pasted command output and would itself violate S1, which
requires reports to carry command output verbatim. Correctly excluded. `adversarial-actor-hunt.md`
and `worker-trigger-probe.md` contain zero occurrences.

**Finding B — staging `.gitignore` whole-file drags nothing along.** Its entire unstaged diff
was the agent-memory block, `+8 / −0`. Verified before staging, not assumed.

**Finding C — over-claim in worker 1's own report (S2). Not corrected in place; recorded here.**
`docs/reports/2026-08-04-session41-c1-marker-worker1.md` lines 185-188 state that *"the other
four `docs/reports/2026-07-26-session36-*.md` files also reference the same gitignored path in
places"* while in the same sentence conceding they were *"not inspected for similar citations."*
That is an assertion above its evidence, and per Finding A it is also **factually wrong** — two
of the four contain no occurrence at all, and the other two contain only pasted status output.
My sweep was run *before* dispatch, so it is independent of the worker rather than a re-reading
of its conclusion. The worker's report is not staged and does not enter the commit; the artifact
it produced is unaffected and remains correct. Left unedited because this unit's write scope is
two lines, and because reports in this project carry audit history and are corrected by
annotation rather than rewriting.

**Finding D — worker's own account of its edit mechanism, checked not trusted.** The worker
noted it needed extra context lines to disambiguate the `Edit` match. That is exactly the shape
of a change that quietly reflows neighbouring text, so it was not taken on its word: the
pure-insertion proof above reconstructs the original line byte-for-byte by deleting only the
marker, and confirms every other line in both files is unchanged. The account holds.

## S6 cross-block check

The change touches two blocks beyond its own: the ignore rules (repo-wide tracking behaviour)
and the six-report payload.

- **Does the new rule capture any file already tracked?** If it did, the rule and the index
  would disagree and the "never committed" claim would be false.

```
$ git ls-files | git check-ignore --stdin -v | grep 'agent-memory'
none — no tracked file is caught by the new rule
```

- **Does it collide with the adjacent `.claude/state/` rule?** No. The two patterns are
  disjoint prefixes; `check-ignore -v` attributes the match to `.gitignore:26` alone.
- **Does it disturb the negation rule above it** (`!signals/signal-template.json`)? No — the
  block is appended after it, and `git check-ignore` still resolves the template path to its
  own rule. The `+8 / −0` numstat confirms no existing line was modified.
- **Effect on the other four staged reports:** none. They are byte-identical to their prior
  staged blobs; the numstat rows for all four are unchanged from baseline.
- **Effect on the audit lineage:** none claimed. This unit does not reset any FAIL count, does
  not unpark `Praxis_build-y9c`, and does not mint or reference a token.

## Files staged

| path | numstat | change |
|------|---------|--------|
| `.gitignore` | `8 / 0` | **newly staged this unit** — the load-bearing half |
| `docs/reports/2026-07-26-session36-null-attack.md` | `328 / 0` | marker added at `:313` |
| `docs/reports/2026-07-26-session36-agent-key-s9-control.md` | `219 / 0` | marker added at `:196` |
| `docs/reports/2026-07-26-session36-adversarial-actor-hunt.md` | `226 / 0` | unchanged |
| `docs/reports/2026-07-26-session36-agent-key-audit.md` | `385 / 0` | unchanged |
| `docs/reports/2026-07-26-session36-agent-key-lab.md` | `287 / 0` | unchanged |
| `docs/reports/2026-07-26-session36-worker-trigger-probe.md` | `131 / 0` | unchanged |

**Total: 7 paths / 1,584 additions / 0 deletions.**

Deliberately NOT staged: this report, worker 1's report, all ledgers, `.claude/settings.json`,
`specs/SPEC_RUBRIC.md`, `scripts/`, and every other untracked report.

## Result: PASS

The two markers are in place in the approved form, byte-verified as pure insertions with every
other byte of both files unchanged. `.gitignore` is staged with them, so the marker's "by
design" claim is backed by text the commit will actually carry. `HEAD` is `c1dec30`, unmoved.
Nothing was committed and no token was minted or referenced.

Scoped honestly: the commit gate itself is untested in this unit (see above), and the
adversarial pass was run by the dispatching manager rather than an independent second worker,
because the brief caps this unit at one spawn.
