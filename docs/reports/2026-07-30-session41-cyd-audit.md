# `Praxis_build-cyd` — narrow audit (Check A + Check B)

**Date:** 2026-07-30 · **Role:** praxis-auditor · **HEAD at audit:** `c1dec30c6516edcf7c79a78fce5c655e007d7ba2`

**Scope, as briefed — two checks only.** The hook count itself was NOT re-derived, the
`opsera-devsecops` plugin was NOT investigated, and no log corpus was searched. Everything in the
subject report outside lines 21–51 and 403–421 is **explicitly unexamined** and is so labelled below.

---

## Result: FAIL

- **Check A (memory correction): FAIL** — two named gaps (A-1, A-2). Two of the four files fully
  satisfy the pattern; two do not.
- **Check B (S2 sweep, verdict + result sections): FAIL** — the UNGRADED marking itself is honest and
  correctly scoped, but the same proposition is restated without hedge in two places (B-1, B-2), and a
  third claim (B-3) is contradicted by the artifact.

---

## Check A — the memory correction

Four files, read directly on disk. All four are under `.claude/agent-memory/`, ignored at
`.gitignore:26`, confirmed:

```
$ git check-ignore -v .claude/agent-memory/praxis-worker/MEMORY.md .claude/agent-memory/praxis-manager/MEMORY.md
.gitignore:26:.claude/agent-memory/	.claude/agent-memory/praxis-worker/MEMORY.md
.gitignore:26:.claude/agent-memory/	.claude/agent-memory/praxis-manager/MEMORY.md
```

### Per-file grade

| File | P1 opens by naming + superseding | P2 superseded text verbatim | P3 nothing deleted | Count reads three |
|---|---|---|---|---|
| `praxis-worker/project_commit-guards-block-scratch-repos.md` | **PASS** | **PASS** (byte-checked) | **PASS** as far as verifiable | **PASS** |
| `praxis-worker/MEMORY.md` | PARTIAL | **FAIL** | PASS (entry not removed) | **PASS** |
| `praxis-manager/project_commit_guard_bypass.md` | **FAIL** | **PASS** | PASS as far as verifiable | **PASS** |
| `praxis-manager/MEMORY.md` | PARTIAL | **FAIL** (UNVERIFIED prior text) | PASS (entry not removed) | **PASS** |

### PASS — the worker memory file

P1. The body opens with the correction and names the superseded claim in its first two lines:

```
  8: # THIRD CORRECTION — 2026-07-30 (`Praxis_build-cyd`). THE COUNT "FOUR" IS WITHDRAWN.
 10: **This file previously told you there were FOUR Bash hooks. There are THREE.** The
 11: superseded claims are preserved verbatim below and further down; nothing has been
 12: deleted.
```

P2. Three superseded passages are quoted (lines 14–15, 19–20, 22, 26–29). Where the quoted text also
survives further down the file, I compared it byte-for-byte after stripping the `> ` blockquote
prefix and normalising whitespace:

```
defensible-claim   occurrences=1  :: The defensible claim is present-tense and scoped: **as of the current script text (post-`8a872d9`), ...
four-matcher       occurrences=2  :: Four Bash-*matcher* hooks exist; **three of them gate commits**.
harness-para       occurrences=1  :: **A fourth hook exists and is outside this repo.** The enabled `opsera-devsecops` plugin registers ...
```

The lines 19–20 quote matches the retained text at 156–157; the line 22 quote matches 163–164; the
26–29 quote matches 222–225. Verbatim, confirmed.

P3. Every prior stratum is still present: first correction (95–121), second correction (122–190),
original scratch-repo observation (192–209), harness section (211–227) — including the now-refuted
"A fourth hook exists and is outside this repo" paragraph at 222–227.

Count: `description:` (line 3) says "only THREE Bash-matcher hooks are live here"; `MEMORY.md:4` says
"none of the 3 LIVE Bash hooks gate a quoted subcommand; the '4th' is a phantom". Consistent.

**UNVERIFIED:** the quote at lines 14–15 reproduces the file's *previous* `description:` frontmatter,
which was overwritten. The path is ignored and untracked, so no prior on-disk version exists to diff
against. Independent corroboration is partial only: `docs/reports/2026-07-28-session40-agent-memory-disposition.md:695`
records that frontmatter as `none of the four Bash PreToolUse hooks` — a substring match. The
parenthetical "(three of which gate commits)" is corroborated by nothing outside the file itself.

### A-1 (FAIL) — the manager memory file does not open with its correction, and one instance of the withdrawn count is left unmarked

`.claude/agent-memory/praxis-manager/project_commit_guard_bypass.md` places the correction at line 29,
mid-file. The body opens with the uncorrected original, and asserts the withdrawn count in live voice
at line 20, nine lines before any in-body correction marker:

```
  8: Under bead `Praxis_build-jcw` the commit-guard evasion lead was settled by
 ...
 20: name what enforces it, because these four hooks do not.
 22: **The inventory trap — this is the reusable part.** `.claude/settings.json`
 23: registers three Bash-matcher PreToolUse hooks. There is a **fourth**, from the
 ...
 29: > **CORRECTION 2026-07-30 (`Praxis_build-cyd`) — the paragraph immediately above is
 30: > WRONG on its specific, RIGHT on its lesson. It is preserved, not deleted.**
```

The correction scopes itself explicitly to "the paragraph immediately above" — lines 22–27. Line 20's
"these four hooks do not" falls outside that scope and is never withdrawn in the body. A reader who
reads the body top-down meets the superseded figure as a live claim.

Mitigation, stated for accuracy: the `description:` frontmatter at line 3 *does* lead with
`CORRECTED 2026-07-30 — ... THREE live Bash PreToolUse hooks (the count "four" is withdrawn ...)`, so
the file is not silent about changing its mind. The property as briefed is that the **file opens**
with that marking; the body does not, and the body carries an unmarked residue.

The subject report asserts the opposite. `docs/reports/2026-07-30-session41-cyd-four-hook-claim.md:385`
describes the worker file as "third correction **prepended**"; line 387 describes the manager file as
"Corrected in place by **the same pattern**." It is not the same pattern — the manager correction is
inserted, not prepended. **Artifact wins.**

P2 and P3 for this file are satisfied: the wrong paragraph (22–27) is preserved intact and explicitly
labelled "It is preserved, not deleted" (line 30), and the closing "over-counts the defence" paragraph
(58–61) and "How to apply" (63–67) are intact. Whether anything *else* was removed is **UNVERIFIED** —
no prior version exists on disk, and no report in `docs/reports/` quotes this file.

### A-2 (FAIL) — both `MEMORY.md` index lines were overwritten; the superseded index text is preserved nowhere

Current lines:

```
praxis-worker/MEMORY.md:4:  - [Commit guards: tripwire, not barrier](project_commit-guards-block-scratch-repos.md) — none of the 3 LIVE Bash hooks gate a quoted subcommand; the "4th" is a phantom; thrice corrected
praxis-manager/MEMORY.md:9: - [Commit-guard bypass](project_commit_guard_bypass.md) — `git 'commit'` evades all 3 LIVE Bash hooks; the "4th" plugin hook is a phantom (enabled ≠ loaded); frontmatter is the real extra source
```

The count reads **three** in both, which is the surface the brief singled out — that part passes.

But the prior worker index text is recorded in two earlier reports:

```
docs/reports/2026-07-28-session40-memory-correction-adversarial.md:85:  .../praxis-worker/MEMORY.md:4:- [Commit guards are a tripwire, not a barrier](...) — CORRECTED: a quoted subcommand bypasses all four Bash hooks (measured); the old "blocks through any route" claim is refuted
docs/reports/2026-07-28-session40-agent-memory-disposition.md:694:  ... reads `quoted subcommand gated by none of 4 Bash hooks (3 gate commits)`
```

Neither string survives anywhere under `.claude/agent-memory/`:

```
$ grep -rn "bypasses all four\|none of 4 Bash\|four Bash" .claude/agent-memory/
.../praxis-worker/project_commit-guards-block-scratch-repos.md:14:> "a quoted subcommand is matched by none of the four Bash PreToolUse hooks (three of
.../praxis-worker/project_commit-guards-block-scratch-repos.md:20:> (post-`8a872d9`), a quoted subcommand is matched by none of the four Bash hooks.**"
.../praxis-worker/project_commit-guards-block-scratch-repos.md:157:(post-`8a872d9`), a quoted subcommand is matched by none of the four Bash hooks.**
```

Three hits, all in the memory file, none reproducing the index line. The memory file preserves the old
`description:` frontmatter verbatim but not the old index line. The index line is one of exactly two
auto-loaded surfaces the brief named as where the false figure lived; its superseded text was replaced
without a preserved record. Property 2 is not met for either `MEMORY.md`, and the entry title was also
changed ("Commit guards are a tripwire, not a barrier" → "Commit guards: tripwire, not barrier").

The prior *manager* index line is **UNVERIFIED** — no report quotes it, and the path is untracked, so I
cannot confirm what it previously said or whether it carried the count at all.

---

## Check B — overclaim sweep, verdict and result sections only

Criteria read at source. `specs/SPEC_RUBRIC.md:108`:

> | S2 | No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure. |

`specs/SPEC_RUBRIC.md:159–166` (S9 note — ruling R3):

> **S9 note — ruling R3, 2026-07-26. Positive control extends to claims about mechanism, not only to
> config keys.** ... A claim of the form *"X is covered by mechanism Y"* gets the same treatment —
> toggle Y, hold everything else constant, and show the behaviour changes. If it does not change, Y
> was never the mechanism.

### What is honest

The UNGRADED marking itself is **sound**. Report lines 36–41 name the exact proposition, name the
deciding experiment, name why it was withheld, and refuse to round it up:

```
 36: **Explicitly UNGRADED:** the proposition *"its registration never enters the runtime registry."*
 37: Rubric ruling R3 grades a mechanism claim by **toggling** the mechanism. ... **mutates live plugin
 40: configuration.** Per the brief's hard stop that is Amear's call. **It was not run.** Strongly
 41: evidenced is not S9-proven, and I decline to round it up.
```

The Result section repeats it under "What PASS does NOT cover" (412–415), and the verdict table
(line 29) labels the "actually resolve and load = 0" row `Strongly evidenced, R3-UNGRADED`. Line 46
also volunteers that "three" holds "by coincidence, not by coverage." All of that is at the right level.

Four factual claims in those sections re-ran identically for me:

```
$ jq -r '[.hooks.PreToolUse[] | select(.matcher=="Bash")] | length' .claude/settings.json
3
$ grep -rn "hooks:" .claude/agents/          # supports the "frontmatter surface = 0" row (line 30)
(no output, exit 1)  — and .claude/agents/ contains exactly the six flat .md files listed at report:245
$ head -711 docs/reports/2026-07-28-session40-agent-memory-disposition.md | md5
4ded8b38c671b5208350472a2a26a883
$ wc -l -c docs/reports/2026-07-28-session40-agent-memory-disposition.md
     856   41819
$ git rev-parse HEAD
c1dec30c6516edcf7c79a78fce5c655e007d7ba2
$ git diff --cached --numstat | awk '{a+=$1; d+=$2; n++} END {print "paths="n" additions="a" deletions="d}'
paths=6 additions=1576 deletions=0
```

So the invariant, prefix-hash and frontmatter-surface claims in the Result section are supported at the
level stated.

### B-1 (S2 violation) — report line 33 states the UNGRADED proposition as fact

```
 33: The disputed fourth is a **phantom**: declared, enabled, present on disk, and never loaded. The chain
 34: that matters is **declared ≠ resolved ≠ loaded ≠ fired**, and `opsera-devsecops` breaks at *resolved*.
```

"never loaded" is the same proposition that line 29 labels `R3-UNGRADED` and line 36 declares
explicitly UNGRADED. It is asserted flat, four lines after the table hedges it and three lines before
the paragraph that withholds it. Under S2 the level actually reached is *strongly evidenced by
convergent read-only observation, toggle withheld* — which is what the file's own memory correction
says (`praxis-worker/project_commit-guards-block-scratch-repos.md:78–81`: "Treat the phantom finding as
strongly evidenced, not as S9-proven"). The verdict prose does not carry that qualifier.

### B-2 (S2 violation) — Result line 405 attributes the LIVE count to evidence that does not establish it

```
405: **What PASS covers:** the count is settled at **three** live Bash-matcher hooks, established by direct
406: read and independently re-run; ...
```

A direct read of `.claude/settings.json` establishes **three registered in that file** — nothing more.
The step from "three in settings.json" to "three **live**" requires (a) the plugin registration never
loading, which the same section marks UNGRADED, and (b) the frontmatter surface being empty, which is a
separate grep. Attaching "established by direct read and independently re-run" to the *live* total
reports it at a higher level than the cited evidence supports. The verdict table is more careful — row
31 (`Live Bash-matcher hooks gating this repo | 3 |`) deliberately leaves the status cell empty — but
the headline at line 23 ("**The four-hook figure is WRONG. The live count is THREE.**") and Result line
405 both drop the hedge. This is the failure mode S2 exists to prevent, and it is the same mechanism by
which "four" propagated in the first place.

### B-3 (S2 violation, cross-checked against Check A) — Result line 408 self-grades the memory correction

```
408: ... the frontmatter surface is enumerated and closed; the memory is corrected in place by the sanctioned
409: pattern; ...
```

Stated as established. Check A finds it false for one of the four files: the manager memory file's
correction is inserted at line 29, not prepended, and leaves the withdrawn count unmarked at line 20
(A-1); and both `MEMORY.md` index lines were overwritten without preserving their superseded text
(A-2). The report's own "Files touched" table repeats the claim at line 387 ("the same pattern"). The
artifact contradicts it.

### Not counted as violations

- Line 406 "established as declared-but-**unresolved**" — non-resolution is directly evidenced
  (marketplace grep with a positive control at report 177–190, plus the loader error line), and the
  wording stops short of "not loaded". Correct level.
- Line 407 "a live in-session control with three positive arms" — matches report 212–237, and its scope
  limit is stated in-place at 234–237.
- Line 419–421 "the escalation item is the R3 toggle ... not mine to authorise" — correct level, and
  consistent with S8.

---

## Explicitly unexamined

Report lines 52–402 (rubric table, workers dispatched, process log, all verification evidence beyond
the four re-runs above, adversarial findings, S6 section, files-touched table beyond lines 385–392).
The hook count derivation, the `opsera-devsecops` plugin, and all log corpora — excluded by brief.
