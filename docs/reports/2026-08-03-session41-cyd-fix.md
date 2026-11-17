# `Praxis_build-cyd` — fix unit

**Date:** 2026-08-03 · **Role:** praxis-manager · **HEAD:** `c1dec30c6516edcf7c79a78fce5c655e007d7ba2`

## Task

Repair four defects that an independent audit (`docs/reports/2026-07-30-session41-cyd-audit.md`,
`Result: FAIL`) found in how a previous dispatch corrected the four-hook claim. The hook count itself
(three) was settled and was NOT reopened.

## Rubric criteria addressed

Read at source, `specs/SPEC_RUBRIC.md:107,108,113`:

| # | Criterion |
|---|---|
| S1 | Every claim in a report has pasted command output, not a description of output. |
| S2 | No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure. |
| S7 | Nothing is committed while any audit box is unchecked. |

S7 discharged by staging nothing and committing nothing; see Files staged.

## Workers dispatched — 2 of a maximum 2

| id | mode | outcome |
|---|---|---|
| `a5f2fba395dedf0de` | BUILD | PASS — applied all four edits; self-flagged two premise mismatches |
| `aa372dd82171bf961` | ADVERSARIAL | **FAIL** — 7 defects, 2 substantive. All remediated by the manager (worker cap reached). |

## Divergences from the brief — found at source, reported as findings

**D-1 (material). The brief's central premise is FALSE: the prior `praxis-manager` index line is
NOT unrecoverable.** The brief and the audit concluded "quoted in no report, therefore UNRECOVERABLE."
The premise is true; the conclusion is not. The audit searched only `docs/reports/`. The line was
recovered **verbatim** from the session transcript corpus:

```
- [Commit-guard bypass](project_commit_guard_bypass.md) — `git 'commit'` evades all four Bash hooks (measured); settings.json is not a complete hook inventory, plugins add hooks.
```

Earliest occurrence `2026-07-27T20:30Z`, `.../d3643d42-.../subagents/agent-a09bf095bcde628fa.jsonl`.
Confirmed complete (not regex-truncated) — the raw JSONL shows the next character is the `\n`
terminator:

```
$ grep -oh "plugins add hooks\..\{0,12\}" .../agent-a09bf095bcde628fa.jsonl | sort -u
plugins add hooks.","+- [Worke
plugins add hooks.\n- [Workers
```

**It was declared lost by the brief; it is preserved verbatim instead.**

**D-2. The brief's two cited sources for the *worker* prior text do not agree, and the one it leads
with is not the immediate predecessor.** `...adversarial.md:85` and `...disposition.md:694` quote
different strings. `disposition.md:196` explains why — the line was edited *during session 40*:

```
`MEMORY.md`'s index line was also corrected: it had carried the inflated "bypasses all four Bash
hooks" and is now `quoted subcommand gated by none of 4 Bash hooks (3 gate commits); present-tense
only, twice corrected`
```

So `:85` is the prior-**prior** text. Four historical versions were recovered; all four are preserved.

**D-3. The audit's `:145` attribution is wrong.** It attributes the entry-title change
("Commit guards are a tripwire, not a barrier" → "Commit guards: tripwire, not barrier") to `cyd`.
The transcript record shows the immediate predecessor already carried the short title — the change was
made by the session-40 edit. Corrected in the file; does not disturb the audit's `Result: FAIL`.

**D-4. The audit's `:87` quote of the line-20 residue drops a leading word.** It quotes
`name what enforces it...`; the line reads `to name what enforces it...`. Immaterial to the finding.

**D-5. My own brief to worker 1 carried a wrong count** (manager memory dir "12 entries"; it holds 11).
The worker caught it and proved it pre-existing. Recorded as my error.

## Verification evidence

### Invariants — start and end identical

```
$ git diff --cached --numstat | awk '{a+=$1;d+=$2;n++} END {print n" paths / "a" additions / "d" deletions"}'
6 paths / 1576 additions / 0 deletions        <- at start
6 paths / 1576 additions / 0 deletions        <- at end
$ git rev-parse HEAD
c1dec30c6516edcf7c79a78fce5c655e007d7ba2
$ git status --short | grep -c '^A '
6
$ ls .claude/agent-memory/praxis-manager/ | wc -l ; ls .claude/agent-memory/praxis-worker/ | wc -l
11
5
```

### Repair 4 — append-only proven by prefix hash

```
$ head -c 21718 docs/reports/2026-07-30-session41-cyd-four-hook-claim.md | shasum -a 256
75e1f31c0764c315847d0edcecdcce55c36692effedd3d2ab0f1900c9ecc5d58  -     <- BEFORE
75e1f31c0764c315847d0edcecdcce55c36692effedd3d2ab0f1900c9ecc5d58  -     <- AFTER
$ wc -l -c docs/reports/2026-07-30-session41-cyd-four-hook-claim.md
421 21718   -> 484 27994
$ sed -n '403p' docs/reports/2026-07-30-session41-cyd-four-hook-claim.md
## Result: PASS
```

Independent corroboration that the prefix is unchanged (the audit, written 2026-07-30 *before* this
session, quoted these lines verbatim; they still match):

```
  :33   present in audit verbatim = 1
  :405  present in audit verbatim = 1
  :408  present in audit verbatim = 1
```

### Negative test — the gate actually blocks

Not a simulation. While running the guard diagnostic, my own Bash call was **denied in flight** because
its command string contained the literal commit form:

```
PreToolUse:Bash hook error: ["$CLAUDE_PROJECT_DIR"/.claude/hooks/gate-commit.sh]: Commit denied: no
audit PASS token for this exact staged diff (the staged set may have changed since mint).
```

Exactly one of the three hooks' messages surfaced — consistent with the known parallel-deny masking.

### Trip test with a FIRING positive control (this is what produced the new defect)

First attempt was a **false null**: all three hooks returned rc=0, *including* the positive-control
arm. Reading `scripts/master-bash-guard.sh:7-8` showed why — the payload lacked `agent_type`, so the
script exits 0 before any matching. Re-run with correct payload shape:

```
=== POSITIVE CONTROL: master-bash-guard vs redirection, as praxis-master ===
  redirect/master        rc=2  BLOCKED: shell write from praxis-master. Use Edit on a ledger, o
=== NEGATIVE ARM: master-bash-guard vs plain commit, SAME identity ===
  plain-commit/master    rc=0
=== no-commit-guard.sh across identities, plain commit ===
  identity=praxis-master    rc=0
  identity=praxis-manager   rc=2  BLOCKED: subagents leave work staged. The master com
  identity=praxis-worker    rc=2  BLOCKED: subagents leave work staged. The master com
  identity=<none>           rc=0
=== gate-commit.sh, plain commit ===
  gate-commit            rc=2  Commit denied: no audit PASS token for this exact st
```

Positive arm fires, negative arm silent, identity held constant — so the rc=0 results are real nulls.

### Residue sweep — every occurrence of the withdrawn count, after repair

```
$ grep -n "four\|fourth\|three of them" .claude/agent-memory/praxis-manager/project_commit_guard_bypass.md
 3: description: CORRECTED 2026-07-30 — ... (the count "four" is withdrawn ...)   [marked]
11: THREE.** The count "four" is WITHDRAWN. Every superseded passage is preserved   [marker]
20: "exit 2 from three of them" count), at the "Why this matters" paragraph        [marker]
31: three of them. Quoted binary (`"git" commit`), split token (`git com'mit'`)    [residue -> corrected at :36]
36: > preserved verbatim, and its phrase "the plain form returns exit 2 from three of them"  [marker]
56: to name what enforces it, because these four hooks do not.                     [residue -> corrected at :59]
59: > above is preserved verbatim and ends "because these four hooks do not."      [marker]
65: registers three Bash-matcher PreToolUse hooks. There is a **fourth**, from the [residue -> corrected at :74]
74: > **Wrong:** there is no live fourth hook. `opsera-devsecops` is installed and  [marker]
89: > coverage**, and that surface is trust-gated — a fourth hook can appear        [forward-looking, not the count]
```

Every residue now has a marker preceding or immediately adjacent to it, plus a top-of-file header.

```
$ grep -c 'hash-object workaround for scratch positive controls' .claude/agent-memory/praxis-worker/MEMORY.md
1
$ grep -c 'evades all four Bash hooks (measured); settings.json is not a complete hook inventory, plugins add hooks.' .claude/agent-memory/praxis-manager/MEMORY.md
1
```

## Adversarial findings

Worker `aa372dd82171bf961` returned **VERDICT: FAIL** with 7 defects. It was given the artifacts and
the three properties only — never worker 1's reasoning or report. Disposition:

| # | Defect | Verified by me? | Disposition |
|---|---|---|---|
| 1 | `:25` "exit 2 from three of them" is an unmarked residue of the withdrawn count | **YES — and worse than stated.** Worker said "two of three"; measurement shows **one** for `praxis-master` | **FIXED** — marked in place with the exit-code table above |
| 2 | Oldest worker index line elided under a false "unrecoverable" label | **YES** — recovered verbatim | **FIXED** — full line restored |
| 3 | Dangling citation to `2026-08-03-session41-cyd-fix.md` | YES — did not exist | **RESOLVED** — this file |
| 4 | "These four defects are repaired" overclaims | YES | **FIXED** — reworded; E2-5 added |
| 5 | Transcript occurrence count does not reproduce | YES — corpus grows as sessions run; my count already included this unit's echoes | **FIXED** — count removed, instability disclosed |
| 6 | Preserved text's provenance is out-of-repo and unversioned | YES | **FIXED** — caveat written into both files |
| 7 | "ERRATA 2" with no ERRATA 1 | YES | **FIXED** — renamed, naming note added |

Defect 1 is the substantive one and was **not reached by the original audit**. The correction pattern
was applied to a file that still contained a second false figure; repairing only what the audit named
would have left it. It is now the E2-5 erratum.

## S6 cross-block check

The repair touches memory files auto-loaded into *other* agent types, so it was checked against blocks
other than its own:

- **Worker block.** `praxis-worker/MEMORY.md` is auto-loaded into every worker. Its entry now carries
  three superseded lines plus a provenance caveat. Count still reads three. No worker-facing claim was
  changed except by addition.
- **Guard/hook block.** No hook, guard script, `settings.json`, agent definition, or `SPEC_RUBRIC.md`
  was read-modified. Confirmed: the only writes were to the four briefed paths.
- **Commit/gate block.** The unit deliberately tripped `gate-commit.sh` (in flight) and exercised all
  three guards by synthetic payload. No guard was modified; no commit was attempted.
- **Report block.** The append-only edit to the session-41 report leaves its `Result: PASS` standing
  and contradicts it in an appended erratum rather than rewriting history, so any reader arriving from
  the audit sees both.

## Files staged

**NONE.** Nothing was staged, committed, deleted, or moved. The pre-existing staged index carrying a
separate pending unit is untouched at 6 paths / 1,576 additions / 0 deletions, and `HEAD` remains
`c1dec30`. Modified in the working tree only:

- `.claude/agent-memory/praxis-manager/project_commit_guard_bypass.md` (gitignored)
- `.claude/agent-memory/praxis-worker/MEMORY.md` (gitignored)
- `.claude/agent-memory/praxis-manager/MEMORY.md` (gitignored)
- `docs/reports/2026-07-30-session41-cyd-four-hook-claim.md` (append-only, untracked)
- `docs/reports/2026-08-03-session41-cyd-fix-worker1.md`, `...-cyd-fix-adversarial.md`, this file (new)

## Declared limits (S2)

1. **Byte-level immutability of the report prefix is not independently provable.** The file is
   untracked, so no git baseline exists; my BEFORE hash was recorded in-session. An equal-length
   in-place substitution inside the first 21718 bytes would evade the hash-and-line checks. Mitigated,
   not closed, by the audit's pre-session verbatim quotes of `:33`/`:405`/`:408` still matching.
2. **Preserved prior index text is recovered from a machine-local, unversioned corpus.** Verbatim and
   sourced, but not reproducible from the repo alone. Disclosed inside both memory files.
3. **P3 ("nothing deleted") remains partly unfalsifiable for the memory files** — they are gitignored
   with no prior on-disk version. Evidence is additive-only size deltas and the audit's pre-fix line
   quotes landing byte-identical at shifted offsets.
4. **The hook count was not re-derived**, per brief.

## Result: PASS

All four briefed repairs applied; all seven adversarial defects remediated; both invariants byte-identical
start to end. The brief's "UNRECOVERABLE" premise was falsified and the text preserved instead of declared
lost. One defect beyond the audit's reach was found and fixed. Limits above are declared, not papered over.
