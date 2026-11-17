# `Praxis_build-cyd` — fix-unit audit — **TRANSCRIBED BY praxis-master**

> ## ⚠️ PROVENANCE — READ BEFORE CITING THIS FILE
>
> **The auditor did not write this file. praxis-master did.**
>
> The audit brief instructed `praxis-auditor` to write its findings to this path. It
> **declined**, reporting that its own agent definition prohibits it from writing
> report or findings `.md` files and directs it to return the audit as its message.
> That is a genuine conflict between the brief and the agent definition, not a
> refusal to grade — the grading itself was returned in full.
>
> The verdict below is therefore a **verbatim transcription by the producer-side
> master of a message returned by the grader.** It is not an artifact the grader
> committed to disk, and it carries the weaker provenance that implies: nothing on
> disk independently attests that the auditor authored this text.
>
> It is transcribed at all because the alternative was worse. `specs/SPEC_RUBRIC.md`
> opens by stating that "context windows compact and reasoning held only in a session
> is reasoning that will be lost." A PASS verdict existing nowhere but in a master's
> context window is exactly that failure. The structural defect is filed in
> `ISSUE_REGISTER.md` (2026-08-03) rather than worked around silently.
>
> **Date:** 2026-08-03 · **Bead:** `Praxis_build-cyd` (fix unit) · **HEAD:** `c1dec30`

---

## Verdict

**Check A: PASS** · **Check B: PASS** · **`Result: PASS`**

## Invariants — auditor's own re-run

```
$ git rev-parse HEAD
c1dec30c6516edcf7c79a78fce5c655e007d7ba2
$ git diff --cached --numstat | awk '{a+=$1;d+=$2;n++} END {print n" paths / "a" adds / "d" dels"}'
6 paths / 1576 adds / 0 dels
```

All six staged paths are the pre-existing session-36 reports. The fix unit staged and
committed nothing.

## A methodological finding that changed two verdicts

The auditor's first three corpus searches returned "0 matches." Both causes were its
own tooling, not the artifact:

```
$ timeout 60 grep -cF "settings.json is not a complete hook inventory" "$F"
(eval):1: command not found: timeout
exit=127
```

`timeout` does not exist on this box. Wrapped in a pipeline to `wc -l`, exit 127 with
no stdout prints `0`. Second cause: the JSONL corpus stores text JSON-encoded, so a
target containing `"` lives on disk as `\"` — a literal `grep -F` for a string
containing quotes returned 0 files while the string was present 28 times.

**Had it stopped at either zero it would have graded both of the fix unit's disputes
as unsupported.** This is a false-null mechanism, the recurring failure class in this
project, caught by the grader against itself.

## Per-criterion

| # | Criterion | Verdict | Evidence / gap |
|---|---|---|---|
| S1 | Every claim in a report has pasted command output, not a description of output. | **PASS, with one stale paste** | Fix report: 20 code fences / 237 lines. Load-bearing claim independently reproduced: `head -c 21718 … \| shasum -a 256` → `75e1f31c0764c315847d0edcecdcce55c36692effedd3d2ab0f1900c9ecc5d58`, byte-identical to its pasted AFTER value. **Gap:** its pasted `wc -l -c` says `484 27994`; the file is now **489 lines / 26197 bytes**. Artifact wins — the pasted output no longer reproduces. |
| S2 | No component is reported at a higher level than the evidence supports. | **PASS** | Errata E2-1 (`:437-442`) downgrades "never loaded" to "strongly evidenced… R3 toggle withheld." E2-2 (`:444-451`) concedes direct read establishes only three `matcher=Bash` registrations in settings.json, not three *live* hooks. Memory `:92-94` keeps the R3 UNGRADED caveat. Fix report `:223-224` self-limits the hash proof and names the residual equal-length-substitution attack. Manager `MEMORY.md:12` caveats the corpus as machine-local, unversioned, growing, and declines to quote occurrence counts. |
| S7 | Nothing is committed while any audit box is unchecked. | **PASS** | HEAD unmoved; staged set unchanged at 6/1576/0; memory files gitignored (`.gitignore:26`), reports untracked. Nothing from the fix unit entered the index. |

## Check A — the correction pattern

**`praxis-manager/project_commit_guard_bypass.md`** — prior defect (i) **REPAIRED**.

P1: body line 8 is now `# CORRECTION FIRST — READ BEFORE ACTING ON ANYTHING BELOW`;
`:10-12` name the prior FOUR-hook claim and withdraw it. Pre-fix state confirmed
independently from the prior audit's own line-anchored quotes: pre-fix `:8` was the
`Praxis_build-jcw` opening paragraph and pre-fix `:20` was
`name what enforces it, because these four hooks do not.` Those now sit at `:27` and
`:56`, both behind the header and both marked (`:35-50`, `:58-62`). **The unmarked
residue the prior audit found is gone.**

P2/P3: all five passages the prior audit recorded as present pre-fix are still present
verbatim. Beyond that record, **UNVERIFIED** — no baseline on disk. The fix unit
exceeded the prior audit's finding: E2-5 marks a *second* residue ("exit 2 from three
of them") with an exit-code table at `:43-47` whose `master-bash-guard.sh` exit 0 is
licensed by a firing positive-control arm.

**`praxis-worker/MEMORY.md`** and **`praxis-manager/MEMORY.md`** — prior defect (ii)
**REPAIRED**.

P1 as applied: for an index the pattern is per-entry; the supersession marker sits
directly under the entry (`worker:5`, `manager:10`), legible in place. On a strict
literal reading, neither *file* opens with it — line 1 of each is an unrelated entry.
**The auditor graded the applied reading and said so.**

P2 — all four preserved lines verified byte-exact by the auditor itself, not by
citation:

| line | corpus files / occurrences | earliest timestamp | in-repo corroboration |
|---|---|---|---|
| worker `:6` (07-30) | 9 / 50 | 2026-07-28T20:35:57.401Z | description quoted at `…agent-memory-disposition.md:195-197` |
| worker `:7` (07-28) | 9 / 72 | 2026-07-27T20:27:27.535Z | **byte-exact containment** at `…memory-correction-adversarial.md:85` |
| worker `:8` (07-27) | 6 / 28 | 2026-07-27T19:09:52.955Z | none |
| manager `:11` (07-30) | 8 / 39 | 2026-07-27T20:30:03.507Z | none |

**Dispute 1 — title change was session-40, not `cyd`: SUPPORTED**, on evidence the fix
unit did not itself cite. The fix unit rested on the transcript record; the auditor
found in-repo corroboration at `docs/reports/2026-07-28-session40-cbf-audit.md:142`,
which quotes the post-session-40-edit line carrying the short title, in a session-40
document, two days before `cyd`. **The prior audit's attribution at `:145` is wrong.**
Caveat recorded by the auditor: `cbf-audit.md` is itself untracked, so it is not a
version-controlled baseline; it is however a distinct pre-existing document, not the
fix unit's own product.

**Dispute 2 — prior manager index line recoverable: SUPPORTED.** Exact string present,
8 files / 39 occurrences, earliest `2026-07-27T20:30:03.507Z`, in the very file the
memory names, which exists with mtime `Jul 27 16:30` (= 20:30Z). **The prior audit's
`:147` "unrecoverable" is wrong**; its stated *ground* (nothing under `docs/reports/`
quotes it) is correct, and the fix unit concedes exactly that.

**How the auditor weighed the unversioned corpus**, in its own framing: not as a
baseline of record. It is machine-local, rotatable, and grows with each session, so it
can never establish *absence* and its counts are unstable. Credited only for the narrow
positive claim it is used for — "this exact string existed at this timestamp" — where
the timestamps are load-bearing: all predate the fix unit by five to seven days, so the
unit could not have manufactured them by echoing its own text.

**Both disputes are correctly scoped: neither disturbs the prior audit's `Result: FAIL`,
which stands.**

## Check B — the errata

Present at `:425-489`, positioned last. Corrects all three overclaims: **E2-1** → `:33`
(`:437-442`), **E2-2** → `:405` (`:444-451`), **E2-3** → `:408` (`:453-461`, also
catching `:387`). Records the prior audit outcome at `:431-433` — "returned
**`Result: FAIL`**" — naming the path and both check verdicts.

**Body unmodified — what the auditor could and could not verify.** Six line-anchored
quotes recorded by the *prior auditor* before the fix ran reproduce byte-identically at
the same line numbers today: audit`:171`→report`:36`, `:173`→`:40`, `:174`→`:41`,
`:204`→`:33`, `:205`→`:34`, `:218`→`:405`. Because these span `:33` to `:405` with no
line drift, nothing was inserted or deleted anywhere above `:405`. Prefix hash over
bytes 1–21718 (= the entire pre-errata body) matches.

**Cannot verify:** byte-identity of the lines the prior audit never quoted. The file is
UNTRACKED, so the BEFORE hash rests on producer self-report and is credited no higher.

**Named defect:** the fix report's pasted `wc` shows `484 27994`; the file is now
`489 26197` — **+5 lines, −1797 bytes**, all beyond the hash boundary, i.e. inside the
errata region itself. The errata was revised after the fix report measured it, and net
*lost* content. The body-unchanged property is unaffected. **What was removed is
UNVERIFIED** — no baseline.

## Auditor's own disclosures, transcribed verbatim in substance

1. It did **not** create this file; its operating instructions prohibit writing
   report/findings `.md` files and direct it to return the audit as its message.
2. It updated its own gitignored memory at
   `.claude/agent-memory/praxis-auditor/audit_evidence_standards.md` and that index,
   recording the two false-zero mechanisms. No tracked file touched; HEAD and the
   staged set unchanged.

## Master's independent re-verification, run after the audit returned

```
$ git rev-parse --short HEAD
c1dec30
$ git diff --cached --numstat | awk '{a+=$1;d+=$2;n++} END {print n" paths / "a" additions / "d" deletions"}'
6 paths / 1576 additions / 0 deletions
$ wc -l -c docs/reports/2026-07-30-session41-cyd-four-hook-claim.md
     489   26197
$ head -c 21718 docs/reports/2026-07-30-session41-cyd-four-hook-claim.md | shasum -a 256
75e1f31c0764c315847d0edcecdcce55c36692effedd3d2ab0f1900c9ecc5d58  -
$ git ls-files --error-unmatch docs/reports/2026-07-30-session41-cyd-four-hook-claim.md
error: pathspec ... did not match any file(s) known to git
tracked-exit=1
```

The master independently confirms: the invariants held, the prefix hash reproduces, the
stale-paste defect is real (`489 26197`, not `484 27994`), and the file is untracked so
no independent baseline exists. **The stale paste and the unverified errata-region
deletion are carried forward as known, unresolved limits — they are not cured by this
PASS.**
