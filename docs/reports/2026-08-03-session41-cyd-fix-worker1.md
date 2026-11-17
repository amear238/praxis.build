# Session 41 — `Praxis_build-cyd` fix unit, worker 1 (transcription of EDITs 1–4)

## Task

Apply four pre-researched edits exactly as written in
`/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/b09d4cee-8199-4e31-b57b-e0df713d3c7c/scratchpad/cyd-fix-spec.md`:

- **EDIT 1a** — insert the `# CORRECTION FIRST` header block at the top of the body of
  `.claude/agent-memory/praxis-manager/project_commit_guard_bypass.md`.
- **EDIT 1b** — insert the `[IN-PLACE CORRECTION 2026-08-03]` block immediately after the
  "…because these four hooks do not." residue, leaving that residue byte-identical.
- **EDIT 2** — append the superseded-index block after line 4 of
  `.claude/agent-memory/praxis-worker/MEMORY.md`.
- **EDIT 3** — append the superseded-index block after line 9 of
  `.claude/agent-memory/praxis-manager/MEMORY.md`.
- **EDIT 4** — append ERRATA 2 to `docs/reports/2026-07-30-session41-cyd-four-hook-claim.md`,
  append-only, existing 421-line / 21718-byte body byte-unchanged.

## Mode

BUILD.

## Criterion

`specs/SPEC_RUBRIC.md` — S1 (every claim backed by pasted command output, not a description
of output) and S2 (nothing reported above the level the evidence supports).

Note on scope: per the brief's prohibitions I did **not** open or read `specs/SPEC_RUBRIC.md`
in this session, so the exact wording of S1/S2 is taken from the brief and is **UNVERIFIED
against the rubric file** by me.

## Process log

1. Read the spec in full. Read all four target files.
2. Captured baseline: staged numstat, HEAD, report `wc -l -c` + `head -c 21718 | shasum -a 256`,
   and a full `ls -la` of both agent-memory directories (before any write).
3. Rather than retype the blocks, I extracted every inserted block **verbatim from the spec
   file by line range** with a Python script
   (`/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/b09d4cee-8199-4e31-b57b-e0df713d3c7c/scratchpad/apply_cyd_fix.py`),
   so em-dashes, the `…` ellipsis, and the backtick nesting could not drift. I printed every
   block first (dry run) and compared it against the spec before writing anything.
   For EDIT 3's middle bullet I used the spec's literal-form line (spec `:87`) with each
   `BACKTICK` token replaced by a single `` ` `` character, as the spec directs.
4. Every write was an **insertion only**: each edit located a unique anchor (anchor uniqueness
   asserted, count must equal 1 or the script aborts) and replaced it with `anchor + block`
   or `block + anchor`. No `str` was ever removed. This is proved numerically below —
   for all four files the byte-size delta equals the inserted-block length exactly.
5. Ran the full 10-step verification.
6. Wrote this report. Nothing was staged; no git mutation command was run at any point.

## Verification evidence

### V1 — `git diff --cached --numstat` (unchanged: 6 paths / 1576 additions / 0 deletions)

```
$ git diff --cached --numstat
226	0	docs/reports/2026-07-26-session36-adversarial-actor-hunt.md
385	0	docs/reports/2026-07-26-session36-agent-key-audit.md
287	0	docs/reports/2026-07-26-session36-agent-key-lab.md
219	0	docs/reports/2026-07-26-session36-agent-key-s9-control.md
328	0	docs/reports/2026-07-26-session36-null-attack.md
131	0	docs/reports/2026-07-26-session36-worker-trigger-probe.md

$ git diff --cached --numstat | awk '{a+=$1; d+=$2; n++} END {print "paths="n" additions="a" deletions="d}'
paths=6 additions=1576 deletions=0
```

This is byte-for-byte the same listing captured at the start of the session, before any edit.

### V2 — `git rev-parse HEAD`

```
$ git rev-parse HEAD
c1dec30c6516edcf7c79a78fce5c655e007d7ba2
```

Matches the required commit.

### V3 — `git status --short` (no new staged entries)

```
$ git status --short
 M .claude/settings.json
 M .gitignore
 M AUDIT_LOG.md
 M DECISION_LOG.md
 M DISPATCH_LOG.md
 M HANDOFF.md
 M ISSUE_REGISTER.md
 M MANIFEST.md
 M STATUS.md
A  docs/reports/2026-07-26-session36-adversarial-actor-hunt.md
A  docs/reports/2026-07-26-session36-agent-key-audit.md
A  docs/reports/2026-07-26-session36-agent-key-lab.md
A  docs/reports/2026-07-26-session36-agent-key-s9-control.md
A  docs/reports/2026-07-26-session36-null-attack.md
A  docs/reports/2026-07-26-session36-worker-trigger-probe.md
 M scripts/dispatch-log-writeahead.sh
 M specs/SPEC_RUBRIC.md
?? F
?? docs/reports/2026-07-26-session34-manifest-amendment.md
?? docs/reports/2026-07-26-session34-p0-flush-audit.md
?? docs/reports/2026-07-26-session35-8sw-audit-round1.md
?? docs/reports/2026-07-26-session35-8sw-gate-park-conflict.md
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
?? scripts/dispatch-log-close.sh
?? scripts/tests/test-dispatch-log-close.sh
```

Staged set (`A `) is exactly the same 6 paths. The EDIT 4 target appears as `??` (untracked,
unstaged). The three agent-memory files do **not** appear at all — they are gitignored, which
I verified rather than assumed:

```
$ git check-ignore -v .claude/agent-memory/praxis-manager/MEMORY.md .claude/agent-memory/praxis-worker/MEMORY.md .claude/agent-memory/praxis-manager/project_commit_guard_bypass.md
.gitignore:26:.claude/agent-memory/	.claude/agent-memory/praxis-manager/MEMORY.md
.gitignore:26:.claude/agent-memory/	.claude/agent-memory/praxis-worker/MEMORY.md
.gitignore:26:.claude/agent-memory/	.claude/agent-memory/praxis-manager/project_commit_guard_bypass.md
```

So their absence from `git status` is an ignore rule, not evidence that they were unmodified;
the modification evidence for those files is V6–V9 and the byte arithmetic below.

### V4 — EDIT 4 body hash, before and after (MUST be identical — they are)

```
BEFORE:
$ head -c 21718 docs/reports/2026-07-30-session41-cyd-four-hook-claim.md | shasum -a 256
75e1f31c0764c315847d0edcecdcce55c36692effedd3d2ab0f1900c9ecc5d58  -

AFTER:
$ head -c 21718 docs/reports/2026-07-30-session41-cyd-four-hook-claim.md | shasum -a 256
75e1f31c0764c315847d0edcecdcce55c36692effedd3d2ab0f1900c9ecc5d58  -
```

Identical. The script also compared the full original byte prefix directly:

```
$ python3 .../apply_cyd_fix.py
EDIT4 pre_hash(head -c 21718) : 75e1f31c0764c315847d0edcecdcce55c36692effedd3d2ab0f1900c9ecc5d58
EDIT4 post_hash(head -c 21718): 75e1f31c0764c315847d0edcecdcce55c36692effedd3d2ab0f1900c9ecc5d58
EDIT4 hashes match           : True
EDIT4 prefix byte-identical  : True
all four edits applied
```

### V5 — `wc -l -c` on the report, before and after

```
BEFORE:
$ wc -l -c docs/reports/2026-07-30-session41-cyd-four-hook-claim.md
     421   21718 docs/reports/2026-07-30-session41-cyd-four-hook-claim.md

AFTER:
$ wc -l -c docs/reports/2026-07-30-session41-cyd-four-hook-claim.md
     467   24617 docs/reports/2026-07-30-session41-cyd-four-hook-claim.md
```

Lines 421 → 467 (grew), bytes 21718 → 24617 (grew).

Boundary between the untouched body and the appended errata:

```
$ sed -n '415,467p' docs/reports/2026-07-30-session41-cyd-four-hook-claim.md
to Amear. The experiment is written up in the errata and above; it was not run. Two supporting
arguments encountered along the way — one from each worker — were found **unsound** (false-null
reasoning over log corpora) and are recorded as defects even though the verdict does not rest on them.

**For the master:** the escalation item is the R3 toggle. It is the only remaining step that would move
the phantom finding from *strongly evidenced* to *proven*, and it is not mine or the manager layer's to
authorise.

---

## ERRATA 2 — 2026-08-03, `Praxis_build-cyd` fix unit (append-only; body above byte-unchanged)

**This report's `Result: PASS` above did not survive audit.** An independent audit of
this report returned **`Result: FAIL`** and is at
`docs/reports/2026-07-30-session41-cyd-audit.md` (Check A FAIL, Check B FAIL). The PASS
line at `:403` and the Result section at `:405–:409` are left byte-unchanged for the
record and are corrected here.

**E2-1 — `:33` overclaims the UNGRADED proposition.** The line reads "declared, enabled,
present on disk, and never loaded." "Never loaded" is the exact proposition this same
report marks `R3-UNGRADED` at `:29` and declares explicitly UNGRADED at `:36`. Correct
level: *declared and enabled, but unresolved against every installed marketplace, with
zero observed runtime firings — strongly evidenced by convergent read-only observation,
R3 toggle withheld.* Not "never loaded" as a flat assertion.

**E2-2 — `:405` attributes the LIVE count to evidence that does not reach it.** A direct
read of `.claude/settings.json` establishes **three `matcher=Bash` registrations in that
file**, nothing more. The step to three *live* hooks additionally requires the plugin
registration never loading — which this report itself marks UNGRADED — and the
frontmatter surface being empty, which is a separate grep. "Established by direct read
and independently re-run" is correct for the settings.json count and overclaims the live
total. The verdict table at `:31` is more careful and deliberately leaves that status
cell empty.

**E2-3 — `:408` self-grades the memory correction, and the artifact contradicts it.**
"The memory is corrected in place by the sanctioned pattern" was falsified by the audit:
`praxis-manager/project_commit_guard_bypass.md` placed its correction mid-file at `:29`
with the withdrawn count left live at `:20`, and both `MEMORY.md` index lines were
rewritten rather than superseded. `:387`'s "the same pattern" is wrong for the same
reason. These four defects are repaired under the `Praxis_build-cyd` fix unit; see
`docs/reports/2026-08-03-session41-cyd-fix.md`.

**E2-4 — one audit finding is itself corrected, in the report's favour and against it.**
The audit records the prior `praxis-manager/MEMORY.md` index line as UNVERIFIED and
unrecoverable (`:147`), on the ground that no file under `docs/reports/` quotes it. That
ground is correct; the conclusion is not. The line was recovered verbatim from the
session transcript corpus and is preserved in the memory file. Separately, the audit
attributes the worker entry's title change to this unit (`:145`); the transcript record
shows it was made by the session-40 edit. Neither correction disturbs the audit's
`Result: FAIL`, which stands.

**What is NOT changed by this errata:** the hook count. Three live Bash-matcher hooks
remains correct and is not reopened here.
```

### V6 — `sed -n '1,35p'` of `project_commit_guard_bypass.md` (file now OPENS with the correction header)

```
$ sed -n '1,35p' .claude/agent-memory/praxis-manager/project_commit_guard_bypass.md
---
name: commit-guard-bypass
description: CORRECTED 2026-07-30 — a quoted subcommand (`git 'commit'`) bypasses all THREE live Bash PreToolUse hooks (the count "four" is withdrawn; the opsera plugin hook is a phantom that never loads). The inventory lesson SURVIVES and is strengthened: settings.json is not a complete hook inventory, but the real extra source is agent-frontmatter `hooks:`, not the plugin.
metadata:
  type: project
---

# CORRECTION FIRST — READ BEFORE ACTING ON ANYTHING BELOW

**This file previously told you there were FOUR live Bash PreToolUse hooks. There are
THREE.** The count "four" is WITHDRAWN. Every superseded passage is preserved verbatim
below and marked where it stands; nothing has been deleted.

Two things survive the correction intact: (a) `git 'commit'` really does evade every
live Bash guard, and (b) `.claude/settings.json` really is not a complete hook
inventory. What was wrong was only the *source* of the extra hook — the real extra
surface is agent-definition frontmatter `hooks:`, not the `opsera-devsecops` plugin,
which is declared and enabled but never resolves. See the in-body corrections at the
"Why this matters" paragraph and at "The inventory trap".

Under bead `Praxis_build-jcw` the commit-guard evasion lead was settled by
experiment: **CONFIRMED**. Piping synthetic payloads into each guard separately
(exit 0 = not gated, exit 2 = gated) showed `git 'commit' -m "…"` returns exit 0
from every live Bash PreToolUse hook, while the plain form returns exit 2 from
three of them. Quoted binary (`"git" commit`), split token (`git com'mit'`), and
backslash-newline between `git` and the subcommand all behave the same way.
`git -C . commit` is caught by `gate-commit.sh` alone.

**Why this matters beyond the bug:** S7 ("nothing is committed while any audit box
is unchecked") has been read as if a mechanism enforces it. It does not. The
guards are a tripwire against an accidental commit, not a control against a
re-spelling. Any future claim that producer/grader separation is *enforced* needs
to name what enforces it, because these four hooks do not.

> **[IN-PLACE CORRECTION 2026-08-03 (`Praxis_build-cyd` fix)] — the sentence immediately
```

The first body line after the frontmatter `---` is now the correction header. The
pre-existing frontmatter block (lines 1–6) is untouched.

### V7 — in-place correction sits adjacent to the residue

```
$ grep -n -A6 "these four hooks do not" .claude/agent-memory/praxis-manager/project_commit_guard_bypass.md
33:to name what enforces it, because these four hooks do not.
34-
35-> **[IN-PLACE CORRECTION 2026-08-03 (`Praxis_build-cyd` fix)] — the sentence immediately
36:> above is preserved verbatim and ends "because these four hooks do not." THE FIGURE
37-> "FOUR" IS WITHDRAWN: there are THREE live Bash-matcher PreToolUse hooks. The sentence's
38-> point is unaffected — the three live hooks do not enforce S7 either, so the demand that
39-> any "enforced" claim name its enforcer stands. Only the count is wrong. Nothing deleted.**
40-
41-**The inventory trap — this is the reusable part.** `.claude/settings.json`
42-registers three Bash-matcher PreToolUse hooks. There is a **fourth**, from the
```

The residue at `:33` is preserved verbatim; the correction begins one blank line later at `:35`.

### V8 — `cat -n` of BOTH `MEMORY.md` files, in full

```
$ cat -n .claude/agent-memory/praxis-manager/MEMORY.md
     1	- [S13 Task-vs-Agent open question](project_s13_task_vs_agent.md) — S13 forbids a `Task` tool that does not exist here; only Amear may correct the rubric.
     2	- [master-write-guard routing](project_master_write_guard_routing.md) — why MANIFEST writes bounce to the manager; the guard fails OPEN and denies AUDIT_LOG.md.
     3	- [8sw park/gate boundary](project_8sw_park_gate_boundary.md) — park step 1 needs a human; gate-commit keys only on the command string; deny-masking isolation lever.
     4	- [Manager report-contract gate](project_manager_report_contract_gate.md) — the four literal checks that block a manager return, and the no-self-grade conflict.
     5	- [Park-commit paste hazard](project_park_commit_paste_hazard.md) — the hand-typed park commit misfired twice; verify HEAD and staged set, never trust a brief's premise.
     6	- [agent_type mechanism](project_agent_type_mechanism.md) — settings `agent` key + resolvable agent def; lab evidence, per-guard levels differ.
     7	- [Verdict token required](feedback_verdict_token_required.md) — a budget-killed adversarial worker returns a partial message with no verdict; that is NO RESULT, never a pass.
     8	- [False-null hazard](project_false_null_hazard.md) — 2 of 4 workers manufactured false nulls; demand liveness proof + a firing positive arm before believing silence.
     9	- [Commit-guard bypass](project_commit_guard_bypass.md) — `git 'commit'` evades all 3 LIVE Bash hooks; the "4th" plugin hook is a phantom (enabled ≠ loaded); frontmatter is the real extra source.
    10	  <!-- SUPERSEDED INDEX TEXT for the entry above — preserved per the correction pattern (`Praxis_build-cyd` fix, 2026-08-03). Nothing deleted. -->
    11	  - superseded 2026-07-30 (immediate predecessor): `- [Commit-guard bypass](project_commit_guard_bypass.md) — `git 'commit'` evades all four Bash hooks (measured); settings.json is not a complete hook inventory, plugins add hooks.`
    12	  <!-- RECOVERY NOTE: the audit (docs/reports/2026-07-30-session41-cyd-audit.md:147) recorded this prior line as UNVERIFIED/unrecoverable because no file under docs/reports/ quotes it. That is true of docs/reports/ and FALSE overall — the line was recovered verbatim from the session transcript corpus, earliest occurrence 2026-07-27, in .../subagents/agent-a09bf095bcde628fa.jsonl (3 further occurrences in 3 other transcripts). It is NOT lost. -->
    13	- [Workers write to agent-memory](feedback_workers_write_to_agent_memory.md) — twice now; name the directory as off-limits in every brief, and correct poisoned files in place, never delete.

$ cat -n .claude/agent-memory/praxis-worker/MEMORY.md
     1	- [S9 positive-control harness](project_s9-positive-control-harness.md) — how to make a real PreToolUse guard fire from a subagent without editing repo config; guard silence is never evidence
     2	- [agent_type source](project_agent-type-source.md) — settings `agent` key sets it only with a resolvable agent def; lab-proven, in-repo inferred
     3	- [Scoped hedge vs universal negative](feedback_scoped-hedge-vs-universal-negative.md) — never turn "not tested in THIS run" into "never tested"; underclaim breaks S2 too
     4	- [Commit guards: tripwire, not barrier](project_commit-guards-block-scratch-repos.md) — none of the 3 LIVE Bash hooks gate a quoted subcommand; the "4th" is a phantom; thrice corrected
     5	  <!-- SUPERSEDED INDEX TEXT for the entry above — preserved per the correction pattern (`Praxis_build-cyd` fix, 2026-08-03). Nothing deleted. Recovered verbatim from the session transcript corpus; report cites where each was previously quoted. -->
     6	  - superseded 2026-07-30 (immediate predecessor): `- [Commit guards: tripwire, not barrier](project_commit-guards-block-scratch-repos.md) — quoted subcommand gated by none of 4 Bash hooks (3 gate commits); present-tense only, twice corrected`
     7	  - superseded 2026-07-28 (prior-prior; also quoted at `docs/reports/2026-07-28-session40-memory-correction-adversarial.md:85`): `- [Commit guards are a tripwire, not a barrier](project_commit-guards-block-scratch-repos.md) — CORRECTED: a quoted subcommand bypasses all four Bash hooks (measured); the old "blocks through any route" claim is refuted`
     8	  - superseded earlier (oldest recovered, PARTIAL — tail not recovered verbatim): `- [Commit guards block scratch repos](project_commit-guards-block-scratch-repos.md) — gate-commit.sh/no-commit-guard.sh match word …`
     9	  <!-- NOTE: the entry TITLE was changed from "Commit guards are a tripwire, not a barrier" to "Commit guards: tripwire, not barrier" on 2026-07-30 by the SESSION-40 edit, not by `Praxis_build-cyd`. The audit at docs/reports/2026-07-30-session41-cyd-audit.md:145 attributes that title change to cyd; the transcript record shows the immediate predecessor already carried the short title. -->
```

Both pre-existing anchor lines (manager `:9`, worker `:4`) are byte-identical to their
pre-edit state; every other pre-existing line is unchanged and in its original order.

### V9 — the recovered manager line appears exactly once

```
$ grep -c "evades all four Bash hooks (measured); settings.json is not a complete hook inventory, plugins add hooks." .claude/agent-memory/praxis-manager/MEMORY.md
1
```

### V10 — `ls -la` of both agent-memory directories (no new files)

BEFORE any edit:

```
$ ls -la .claude/agent-memory/praxis-manager/ .claude/agent-memory/praxis-worker/
.claude/agent-memory/praxis-manager/:
total 104
drwxr-xr-x@ 13 admin  staff   416 Jul 30 12:47 .
drwxr-xr-x@  6 admin  staff   192 Jul 26 10:18 ..
-rw-r--r--@  1 admin  staff  2156 Jul 26 19:20 feedback_verdict_token_required.md
-rw-r--r--@  1 admin  staff  2067 Jul 27 16:29 feedback_workers_write_to_agent_memory.md
-rw-r--r--@  1 admin  staff  1708 Jul 30 12:47 MEMORY.md
-rw-r--r--@  1 admin  staff  2259 Jul 26 15:15 project_8sw_park_gate_boundary.md
-rw-r--r--@  1 admin  staff  6703 Jul 26 19:18 project_agent_type_mechanism.md
-rw-r--r--@  1 admin  staff  4325 Jul 30 12:47 project_commit_guard_bypass.md
-rw-r--r--@  1 admin  staff  1951 Jul 26 18:21 project_false_null_hazard.md
-rw-r--r--@  1 admin  staff  2097 Jul 26 18:22 project_manager_report_contract_gate.md
-rw-r--r--@  1 admin  staff  1763 Jul 26 14:20 project_master_write_guard_routing.md
-rw-r--r--@  1 admin  staff  2133 Jul 26 16:38 project_park_commit_paste_hazard.md
-rw-r--r--@  1 admin  staff  1834 Jul 26 14:20 project_s13_task_vs_agent.md

.claude/agent-memory/praxis-worker/:
total 72
drwxr-xr-x@ 7 admin  staff    224 Jul 30 12:47 .
drwxr-xr-x@ 6 admin  staff    192 Jul 26 10:18 ..
-rw-r--r--@ 1 admin  staff   1806 Jul 26 19:16 feedback_scoped-hedge-vs-universal-negative.md
-rw-r--r--@ 1 admin  staff    703 Jul 30 12:47 MEMORY.md
-rw-r--r--@ 1 admin  staff   5804 Jul 26 19:17 project_agent-type-source.md
-rw-r--r--@ 1 admin  staff  12558 Jul 30 12:46 project_commit-guards-block-scratch-repos.md
-rw-r--r--@ 1 admin  staff   1862 Jul 26 18:04 project_s9-positive-control-harness.md
```

AFTER:

```
$ ls -la .claude/agent-memory/praxis-manager/ .claude/agent-memory/praxis-worker/
.claude/agent-memory/praxis-manager/:
total 104
drwxr-xr-x@ 13 admin  staff   416 Jul 30 12:47 .
drwxr-xr-x@  6 admin  staff   192 Jul 26 10:18 ..
-rw-r--r--@  1 admin  staff  2156 Jul 26 19:20 feedback_verdict_token_required.md
-rw-r--r--@  1 admin  staff  2067 Jul 27 16:29 feedback_workers_write_to_agent_memory.md
-rw-r--r--@  1 admin  staff  2543 Aug  3 16:52 MEMORY.md
-rw-r--r--@  1 admin  staff  2259 Jul 26 15:15 project_8sw_park_gate_boundary.md
-rw-r--r--@  1 admin  staff  6703 Jul 26 19:18 project_agent_type_mechanism.md
-rw-r--r--@  1 admin  staff  5550 Aug  3 16:52 project_commit_guard_bypass.md
-rw-r--r--@  1 admin  staff  1951 Jul 26 18:21 project_false_null_hazard.md
-rw-r--r--@  1 admin  staff  2097 Jul 26 18:22 project_manager_report_contract_gate.md
-rw-r--r--@  1 admin  staff  1763 Jul 26 14:20 project_master_write_guard_routing.md
-rw-r--r--@  1 admin  staff  2133 Jul 26 16:38 project_park_commit_paste_hazard.md
-rw-r--r--@  1 admin  staff  1834 Jul 26 14:20 project_s13_task_vs_agent.md

.claude/agent-memory/praxis-worker/:
total 72
drwxr-xr-x@ 7 admin  staff    224 Jul 30 12:47 .
drwxr-xr-x@ 6 admin  staff    192 Jul 26 10:18 ..
-rw-r--r--@ 1 admin  staff   1806 Jul 26 19:16 feedback_scoped-hedge-vs-universal-negative.md
-rw-r--r--@ 1 admin  staff   2167 Aug  3 16:52 MEMORY.md
-rw-r--r--@ 1 admin  staff   5804 Jul 26 19:17 project_agent-type-source.md
-rw-r--r--@ 1 admin  staff  12558 Jul 30 12:46 project_commit-guards-block-scratch-repos.md
-rw-r--r--@ 1 admin  staff   1862 Jul 26 18:04 project_s9-positive-control-harness.md

$ echo "manager entries: $(ls -1 .claude/agent-memory/praxis-manager/ | wc -l)  worker entries: $(ls -1 .claude/agent-memory/praxis-worker/ | wc -l)"
manager entries:       11  worker entries:        5
```

Same filename set before and after; only the three sanctioned files changed mtime/size.
`project_commit-guards-block-scratch-repos.md` (worker) is 12558 bytes with a Jul 30 12:46
mtime in both listings — untouched, as required.

**Discrepancy against the brief, reported not papered over:** the brief predicted the manager
directory would hold "11 .md files + MEMORY.md = 12 entries total". It holds **10 memory .md
files + MEMORY.md = 11 entries**, and it held exactly those same 11 entries in the BEFORE
listing captured prior to any write. So the count is a pre-existing mismatch in the brief's
premise, not something this unit caused. The worker directory matches the brief exactly
(4 .md + MEMORY.md = 5).

### V11 (extra) — proof that all four edits were purely additive

Each file's byte-size delta equals exactly the length of the block inserted into it. If any
existing byte had been removed, these would not match.

```
$ python3 -c "... recompute block lengths from the spec, compare to observed size deltas ..."
EDIT1 inserted bytes = 1225  size delta 4325->5550 = 1225
EDIT2 inserted bytes = 1464       size delta  703->2167 = 1464
EDIT3 inserted bytes = 835        size delta 1708->2543 = 835
EDIT4 inserted bytes = 2899       size delta 21718->24617 = 2899
```

## Files staged

**None.** Nothing was staged, and no staging, commit, checkout, reset, stash, rm or mv command
was run at any point in this session. The index is unchanged at 6 paths / 1576 additions /
0 deletions (V1) and HEAD is unchanged at `c1dec30` (V2).

Files modified on disk (all four are in the spec's writable set):

- `/Volumes/Sensidine/Praxis.build/.claude/agent-memory/praxis-manager/project_commit_guard_bypass.md` (EDIT 1a + 1b)
- `/Volumes/Sensidine/Praxis.build/.claude/agent-memory/praxis-worker/MEMORY.md` (EDIT 2)
- `/Volumes/Sensidine/Praxis.build/.claude/agent-memory/praxis-manager/MEMORY.md` (EDIT 3)
- `/Volumes/Sensidine/Praxis.build/docs/reports/2026-07-30-session41-cyd-four-hook-claim.md` (EDIT 4, append-only)

File created: this report,
`/Volumes/Sensidine/Praxis.build/docs/reports/2026-08-03-session41-cyd-fix-worker1.md`.
Scratch-only (outside the repo):
`/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/b09d4cee-8199-4e31-b57b-e0df713d3c7c/scratchpad/apply_cyd_fix.py`.

No file under `.claude/agent-memory/` other than the three named was written, and no new file
was created there (V10, before/after listings).

## Limits of this evidence (S2)

- I verified that the inserted text matches the **spec** character-for-character (extracted
  programmatically from it). I did **not** independently verify the spec's factual claims —
  the transcript-corpus recovery of the superseded index lines, the earliest-occurrence date
  of 2026-07-27, the `agent-a09bf095bcde628fa.jsonl` filename, the "3 further occurrences",
  the `:145`/`:147` audit line numbers, or the attribution of the title change to session 40.
  Those are the manager's findings, transcribed as instructed and **UNVERIFIED by me**.
- The line-number citations inside the appended ERRATA 2 text (`:33`, `:403`, `:405`, `:408`,
  `:387`, `:29`, `:31`, `:36`) are the spec's; I did not check them against the report body.
- The EDIT 4 errata references `docs/reports/2026-08-03-session41-cyd-fix.md`, which is a
  different path from this report. I did not create it; producing it is not in my scope.
- I did not read `specs/SPEC_RUBRIC.md` (prohibited by the brief), so my restatement of
  S1/S2 comes from the brief only.
- MANIFEST.md was not updated for this report. Repo convention (CLAUDE.md) calls for it, but
  MANIFEST.md is outside my writable set, so I left it alone and flag it here for the manager.

## Result: PASS

All four edits applied exactly as specified. The EDIT 4 body hash is unchanged
(`75e1f31c…c5d58` before and after), both memory index anchor lines are byte-identical,
the residue at `project_commit_guard_bypass.md:33` is preserved verbatim with the correction
adjacent at `:35`, the recovered manager line appears exactly once, no file was deleted or
created under `.claude/agent-memory/`, the staged index is untouched at 6 paths / 1576
additions / 0 deletions, and HEAD is still `c1dec30c6516edcf7c79a78fce5c655e007d7ba2`.

One deviation from the brief is recorded rather than smoothed over: the manager memory
directory contains 11 entries, not the 12 the brief predicted, and it contained those same
11 before I made any change.
