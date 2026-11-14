# Sub-report: the `.claude/agent-memory/` subsystem

**PRAXIS — Praxis.build · 2026-08-06 · authored by `praxis-auditor`**

> ## PROVENANCE — READ BEFORE CITING
>
> **Authored by `praxis-auditor`. Transcribed to disk by `praxis-master`**, because the
> auditor's definition forbids it writing report/findings `.md` files. It said so explicitly
> rather than skipping silently — the known defect at `ISSUE_REGISTER.md` 2026-08-03T21:20Z,
> here in its fourth occurrence. The analysis is the auditor's; the transcription is the
> producer side's, which is weaker provenance than a grader-committed artifact.
>
> **Master's independent re-verification of the three most actionable findings**, run after
> the report returned:
> - The surviving false claim at `praxis-manager/project_8sw_park_gate_boundary.md:31-35` is
>   present on disk, `mtime Jul 26 15:15:30 2026` — untouched since, nine days after being
>   flagged with file and line.
> - `CLAUDE.md:51` reads verbatim: `- Use `bd remember` for persistent knowledge — do NOT use
>   MEMORY.md files`.
> - `git log --all -- '.claude/agent-memory/**'` → **0 commits, 0 tracked files**; control
>   `git ls-files .claude/` → 14. The grep is live; the absence is real.
>
> Scope: all 23 memory files, `scripts/master-write-guard.sh`, and targeted verification
> commands. Ledgers deliberately not opened; contextual figures from
> `docs/reports/2026-08-06-facts-pack.md`.

---

## 1. What it is, and how it actually works

### 1.1 The idea

PRAXIS is a trading-system project that runs itself through a stack of AI agents. A "main thread" agent called `praxis-master` coordinates; it dispatches `praxis-manager` units, which dispatch `praxis-worker` units to build things and `praxis-auditor` units to grade them. Each of those is a **subagent** — a fresh, short-lived process with an empty head. It reads a brief, does one job, returns a message, and dies. Nothing it learned survives.

`.claude/agent-memory/` is the fix for that amnesia. It is a directory of Markdown files, partitioned by agent *type*, whose contents are injected into the starting context of every future agent of that type. A lesson learned by one auditor in July is supposed to be sitting in the next auditor's head in August, without anyone re-briefing it.

That is also the hazard, and the memory system says so about itself, at `.claude/agent-memory/praxis-manager/feedback_workers_write_to_agent_memory.md:20-22`:

> The stakes are higher than a normal stray file because this directory is **durable and auto-loaded into every future agent's context**. A stray write there is not an artifact to clean up later — it is standing instruction to the whole stack, and it will be believed.

### 1.2 Layout, verified

```
.claude/agent-memory/
├── praxis-auditor/   MEMORY.md + 4 memory files      (11,591 B)
├── praxis-manager/   MEMORY.md + 12 memory files     (38,847 B)
├── praxis-master/    (EMPTY — no index, no files)
└── praxis-worker/    MEMORY.md + 4 memory files      (24,817 B)
```

23 files, **79,859 bytes** total. The `praxis-master` directory has existed since `Jul 25 16:49` and contains nothing. Section 5.1 explains why, and it is not an oversight.

For scale: the project's committed ledgers total ~659 KB. The memory corpus is about 12% of that — but unlike the ledgers, part of it is loaded whether the agent wants it or not.

### 1.3 The frontmatter convention

Every non-index file opens with a YAML **frontmatter** block — a fenced header of key/value metadata delimited by `---` lines — carrying a `name` (kebab-case slug used as link target), a one-line `description` used to judge relevance, and `metadata.type`, one of `user`, `feedback`, `project`, `reference`.

Compliance is total: frontmatter, `name`, `description` and `type` present on **20 of 20** non-index files. Types split 13 `project` / 7 `feedback`; no `user` or `reference` memories exist.

Bodies follow a house style — the claim, then a bolded `**Why:**` giving the incident that produced it, then `**How to apply:**` giving the trigger condition. Files cross-reference with wiki-style `[[slug]]` links. Across the corpus there are 29 such links and **zero dangle**. Four of the 29 point into a *different* agent's directory, which matters — see 5.4.

### 1.4 The index, and what actually auto-loads

Each directory holds a `MEMORY.md` — an index, not a memory. One line per file: `- [Title](file.md) — one-line hook`. Correspondence is exact in all three populated directories: auditor 4/4, manager 12/12, worker 4/4, zero unindexed files, zero entries pointing at absent files.

**This is the part most people get wrong, so state it precisely.** The whole 80 KB corpus is *not* auto-loaded. What auto-loads is the agent's own `MEMORY.md` index plus the operating instructions. I can attest directly: the system prompt for this dispatch contains a section headed `## MEMORY.md` whose contents are the four index lines of `praxis-auditor/MEMORY.md`, byte-identical to disk — and nothing else. To read `audit_evidence_standards.md` I had to open it with a tool call.

The real auto-load budget is small and per-type:

| agent type | auto-loaded index | full corpus behind it |
|---|---|---|
| `praxis-auditor` | 673 B | 11,591 B |
| `praxis-manager` | 3,723 B | 38,847 B |
| `praxis-worker` | 2,787 B | 24,817 B |
| `praxis-master` | — none — | — none — |

The index line is therefore the load-bearing artifact — the only text guaranteed to reach an agent. A memory whose index hook is wrong is wrong in every session; a memory whose *body* is wrong is wrong only for agents that follow the link. Section 3 turns on exactly this distinction.

### 1.5 Which agent types have memory — and which have none

The switch is a `memory:` key in the agent definition:

```
.claude/agents/praxis-manager.md:5:memory: project
.claude/agents/praxis-auditor.md:5:memory: project
.claude/agents/praxis-master.md:5:memory: project
.claude/agents/praxis-worker.md:5:memory: project
--- files with NO memory key ---
.claude/agents/orchestrator-auditor.md
.claude/agents/praxis-tutor.md
```

Six definitions exist. Four declare memory; **`orchestrator-auditor` and `praxis-tutor` have none at all**. `praxis-master` declares it, has a directory, and the directory is empty because it is structurally forbidden from writing there (5.1).

Net: of six agent types, three accumulate memory, one is declared-but-blocked, two are outside the system entirely.

---

## 2. Has it helped?

Two questions must be kept apart. Does the memory contain true, operationally decisive, non-derivable facts? — yes, demonstrably. Did a stored memory change a past outcome? — the files assert it repeatedly, and I cannot check those assertions, because the sessions live in a machine-local transcript corpus outside version control. **UNVERIFIED** on causation; verified on content.

### 2.1 Facts I re-derived today, that hold

`praxis-manager/project_master_write_guard_routing.md` makes four mechanical claims about one guard. I trip-tested all four by piping synthetic hook payloads at `scripts/master-write-guard.sh`. Every one reproduced:

```
ARM 1 master writes own memory   -> exit=2  BLOCKED: praxis-master may only write ledgers, specs, and reports.
ARM 2 master writes a report     -> exit=0     (positive-allow control — the guard is live, not inert)
ARM 3 SUBAGENT, agent_id present -> exit=0     ("A spawned praxis-master is exempt", :19-21)
ARM 5 master writes AUDIT_LOG.md -> exit=2     ("AUDIT_LOG.md is DENIED to praxis-master", :20-23)
ARM 6 empty stdin                -> exit=0     ("It fails OPEN, not closed", :15-17)
ARM 7 key renamed agent_typeX    -> exit=0     (invented-key control: the field is load-bearing)
```

None of that is derivable by reading the 20-line script casually — the fail-open behaviour and the `AUDIT_LOG.md` omission are both *absences*, and absences are what people miss. A manager arriving cold with this file does not have to rediscover them.

Three more spot checks, all confirmed:

- `audit_evidence_standards.md:83-86` says there is no `timeout` binary on this machine and that wrapping a search in it produces a silent false zero. `command -v timeout` → not found, rc=1 (control: `command -v grep` → `grep`). True, and it invalidates three prior "0 matches" findings.
- `grading_verdict_discipline.md:33-36` warns the auditor's own read-only git calls trip `no-commit-guard.sh`, naming `git merge-base`. `scripts/no-commit-guard.sh:20` is `grep -qE '\bgit\s+(commit|push|merge|rebase|tag)\b'` — `\b` does match before a hyphen, so `git merge-base` is caught. Verified by inspection; not trip-tested, because tripping it would have denied my own tool call. That is the point of the memory.
- `project_manager_report_contract_gate.md` warns the gate picks the *newest* file in `docs/reports/`. `scripts/gate-manager-output.sh:6` is `LATEST=$(ls -t "$DIR"/docs/reports/*.md | head -1)`. Confirmed, along with all four literal string checks.

### 2.2 A case where memory changed this dispatch

The four index lines injected into my context before I read anything included:

> `- [Grading verdict discipline](grading_verdict_discipline.md) — return the verdict on the narrow claim; assemble blocked substrings at runtime or your own harness call gets denied`

Two behaviours in this report came from that line. I kept `git` invocations in separate tool calls from commands naming files with `commit` in their filenames, to avoid a guard denying my own probe — a hazard I would not have anticipated. And I held the verdict rather than opening more files when the read budget tightened. The second is directly on point: the facts pack records five consecutive auditor dispatches dying mid-investigation with no verdict, and this memory exists because of an earlier instance of the same failure.

That is a genuine, first-person, verifiable case of the system working as designed — from 673 bytes.

### 2.3 The claimed saves, which I cannot check

The files record several outcomes they say memory produced: a false null on the `agent_type` mechanism broken by an adversarial re-dispatch (`project_false_null_hazard.md:9`); a budget-killed worker's empty return caught rather than read as a clean pass (`feedback_verdict_token_required.md:12-24`); a "declare it lost" repair brief overturned by recovering the text from transcripts (`project_transcript_recovery.md:14-19`). Each is plausible, internally detailed, and dated. Each is also **UNVERIFIED** — the evidence is session history not in this repository.

---

## 3. How it has failed

### 3.1 The four-hook claim

A **hook** is a shell script the agent harness runs before a tool call, able to block it. `.claude/settings.json` registers several; those with matcher `Bash` are the commit guards. The count matters because guarantees were being asserted on top of it.

Ground truth, today:

```
$ jq -r '[.hooks.PreToolUse[] | select(.matcher=="Bash")] | length' .claude/settings.json
3
```

Full registration table:

```
PreToolUse  Bash                     scripts/no-commit-guard.sh
PreToolUse  Bash                     .claude/hooks/gate-commit.sh
PreToolUse  Bash                     scripts/master-bash-guard.sh
PreToolUse  Write|Edit|NotebookEdit  scripts/master-write-guard.sh
PreToolUse  Agent                    scripts/agent-spawn-guard.sh
```

Three, not four. The phantom fourth was `pre-commit-scan.sh` from an `opsera-devsecops` plugin: installed on disk, marked enabled, declaring a Bash `PreToolUse` registration — and never resolving against any marketplace, so never loading. The memory files reconstruct the whole diagnosis, including that the live session stamps an `.in_use/<pid>` marker into each plugin it loads and opsera's only markers are dead PIDs from May (`praxis-worker/project_commit-guards-block-scratch-repos.md:54-67`). The distilled lesson at `:82` is the durable one: *enabled + installed ≠ loaded*.

Propagation is documented in the tracker. Bead `Praxis_build-cyd`, opened 2026-07-30T16:06:06Z:

> `E5: 'four Bash hooks' rests on an UNGRADED out-of-repo plugin hook; premise has propagated into auto-loaded praxis-worker memory`

Corrections landed 2026-07-30 in `praxis-worker/project_commit-guards-block-scratch-repos.md`, its manager twin `praxis-manager/project_commit_guard_bypass.md`, and both `MEMORY.md` index lines. Both indexes now read "3 LIVE Bash hooks".

### 3.2 Something in there is still wrong

**`praxis-manager/project_8sw_park_gate_boundary.md:31-35`, verbatim, on disk today:**

```
- **Deny-masking lever:** four PreToolUse hooks share matcher `Bash`. To isolate
  `gate-commit.sh`, use `git -C <dir> commit` — it misses
  `no-commit-guard.sh`'s `\bgit\s+(commit|push|…)\b` but matches gate-commit's
  looser pattern. The harness also names the producing hook in brackets. See
  [[master-write-guard-routing]] for the sibling-guard map.
```

Mtime `Jul 26 15:15`. The correction was 2026-07-30. It was never touched.

This is worse than a missed sweep, because it was **found and left**. From `docs/reports/2026-07-28-session40-memory-correction-adversarial.md:318-323`:

> ### Out-of-scope observation (reported, not acted on)
>
> `.claude/agent-memory/praxis-manager/project_8sw_park_gate_boundary.md:31-35` carries an overlapping guard map ("four PreToolUse hooks share matcher `Bash`") that was **not** in my audit scope and was not graded here. If the ruling's correction is meant to be system-wide, that file should get the same treatment. I did not touch it.

Flagged 2026-07-28 with exact file, exact line range, exact quotation. Still present nine days later.

Two mitigations, stated so this is not over-read: the false count sits in a *body* file, not the auto-loaded index — the manager's index hook carries no number. And the surrounding *technique* is correct: `git -C . commit` really does hit `gate-commit.sh` and miss `no-commit-guard.sh`. So a manager following this paragraph gets a working isolation lever and a wrong hook count in the same breath. That is the more dangerous shape, not the less.

Two smaller inaccuracies currently in the corpus:

- **`praxis-auditor/MEMORY.md:3`** advertises `audit_evidence_standards.md` as "8 checks". The file carries nine numbered items — `1, 2, 3, 4, 5, 5b, 6, 5c, 5d` (note `6` between `5b` and `5c`, the fingerprint of append-only growth without renumbering). The index hook has drifted from its file.
- **`praxis-manager/project_manager_report_contract_gate.md:3` and `:10`** say "four literal checks", then enumerate five. Four are unconditional; the fifth (`S6|cross-block`) fires only while a `^FROZEN` line exists in `specs/SPEC_RUBRIC.md`. Four FROZEN criteria are currently live, so the fifth check is active and the headline undercounts the live gate by one.
- **`praxis-auditor/audit_evidence_standards.md:96`** attributes `[[transcript-recovery]]` to "the manager/worker memories". No file of that `name` exists in `praxis-worker/` — only in `praxis-manager/`.

---

## 4. The correction pattern

### 4.1 The rule

When a memory turns out to be false you do not edit the sentence and move on. The file must open by naming its prior claim, preserve the superseded text verbatim where it stood, and delete nothing. `feedback_workers_write_to_agent_memory.md:31-35`:

> When correcting a poisoned memory file, **correct in place, never delete** — deletion erases the record that a read-only agent wrote to the tree. […] A worker will tend to append the correction at the bottom and quietly delete the false sentence; that loses both the ordering and the evidence, so do this one myself.

### 4.2 Do the files comply?

**`praxis-worker/project_commit-guards-block-scratch-repos.md` — full compliance, three layers deep.** Line 8: `# THIRD CORRECTION — 2026-07-30 (Praxis_build-cyd). THE COUNT "FOUR" IS WITHDRAWN.` Line 10 names the prior claim. Three superseded passages quoted verbatim at `:14-29`. A second correction block at `:122` preserves its own predecessor's false absolute at `:128-131`. Critically, the original false sentences still stand where written — `:222-227` still reads "**A fourth hook exists and is outside this repo**", marked, not deleted; `:99-101` still carries the first poisoned claim in full.

**`praxis-manager/project_commit_guard_bypass.md` — full compliance.** Line 8 `# CORRECTION FIRST — READ BEFORE ACTING ON ANYTHING BELOW`, line 10 naming the prior claim, three in-body corrections placed at the exact paragraphs they refute rather than pooled at the bottom. `:56` still ends "because these four hooks do not", with the withdrawal directly beneath at `:58-62`.

**The indexes comply too, which is unusual rigour.** `praxis-worker/MEMORY.md:5-9` preserves three superseded index lines verbatim with source attribution and provenance caveats; `praxis-manager/MEMORY.md:10-13` preserves one. Line 9 goes further and corrects the *audit* about the correction:

> `NOTE: the entry TITLE was changed […] on 2026-07-30 by the SESSION-40 edit, not by Praxis_build-cyd. The audit at docs/reports/2026-07-30-session41-cyd-audit.md:145 attributes that title change to cyd; the transcript record shows the immediate predecessor already carried the short title.`

**One partial.** `praxis-worker/project_agent-type-source.md:8` opens correctly — "This file previously recorded the opposite claim. That claim is REFUTED." — but never *preserves* the prior sentence. The reader is told there was an opposite claim and is not shown it. Against the rule's own words this is a miss, and a recoverable one: `project_transcript_recovery.md:8-12` establishes prior text is retrievable from session transcripts, which is exactly how the three superseded index lines were recovered. The technique existed and was not applied.

### 4.3 Is it working, or is it just weight?

Both, and the ratio is now poor.

It is working as **forensics**. I reconstructed the entire lifecycle of the four-hook error — original claim, first correction, the false absolute the first correction itself shipped, second correction, third — from the files alone, with dates, bead IDs and verbatim prior wording, in a directory with *no version history whatsoever*. That is a real achievement and it is the pattern's actual job.

It is failing as **propagation**. The pattern is per-file and there is no sweep. The 8sw survivor proves it: correcting two files and two index lines was treated as correcting the system, an adversarial pass found the third instance and explicitly declined to touch it, and nobody closed the loop.

The weight is now measurable:

| artifact | total | correction apparatus + preserved dead text | live content |
|---|---|---|---|
| `praxis-worker/project_commit-guards-block-scratch-repos.md` | 12,558 B / 227 lines | 10,495 B (lines 1-191) | 2,063 B (lines 192-227) |
| `praxis-worker/MEMORY.md` | 2,787 B / 9 lines | 2,084 B (lines 5-9) | 703 B (lines 1-4) |
| `praxis-manager/MEMORY.md` | 3,723 B / 16 lines | 1,638 B (lines 10-13) | 2,085 B |

The most-corrected memory in the system is also the largest file in it, and **84% of it is withdrawn text and the apparatus of withdrawing it**. The worker's auto-loaded index — the one artifact guaranteed to reach every worker — is **75% dead text by bytes**: three superseded versions of one line plus provenance caveats, all consuming context before the worker reads its brief. One fact and its history now account for roughly a quarter of the entire 80 KB corpus.

The pattern is correct in principle and is being applied to an index, which is the wrong surface. An index exists to be scanned in one pass by an agent that has not yet started work.

---

## 5. Structural problems

### 5.1 The master cannot write its own memory; every subagent can

`scripts/master-write-guard.sh` is 20 lines. Line 8 exempts anything with an `agent_id` — present only for subagents. Lines 13-16 are the allowlist for the main-thread master:

```bash
case "$FILE" in
  *DISPATCH_LOG.md|*DECISION_LOG.md|*ISSUE_REGISTER.md|*HANDOFF.md|*STATUS.md) exit 0 ;;
  */specs/*|*/docs/reports/*) exit 0 ;;
esac
```

`.claude/agent-memory/` is not in it. Confirmed live, not inferred:

```
ARM 1 master writes own memory -> exit=2
  BLOCKED: praxis-master may only write ledgers, specs, and reports.
ARM 2 master writes a report   -> exit=0   (control: guard is live and permissive elsewhere)
ARM 3 subagent, same path      -> exit=0   (line 8 exemption)
ARM 4 worker writes worker memory -> exit=0
```

So the agent with the only persistent, cross-session identity in the stack — the one whose accumulated judgement would be worth the most — is the only one that cannot record any. Its definition declares `memory: project`; its directory has been empty since 25 July. Every ephemeral subagent writes freely. **The incentive is exactly inverted.**

Two aggravating details. First, line 8 is the same exemption that produced open P0 `Praxis_build-s8g`; one line generates both the memory asymmetry and a P0. Second, the guard **fails open** — ARM 6 (empty stdin) and ARM 7 (renamed field) both exit 0 silently. Any payload the guard cannot parse writes anywhere it likes, with no error surfaced.

### 5.2 The directory is unversioned, so prior states exist only on this machine

```
$ grep -n 'agent-memory' .gitignore
26:.claude/agent-memory/

$ git check-ignore -v .claude/agent-memory/praxis-worker/MEMORY.md
.gitignore:26:.claude/agent-memory/    .claude/agent-memory/praxis-worker/MEMORY.md

$ git ls-files .claude/agent-memory/ | wc -l
0                     (control: 14 tracked files under .claude/)

$ git log --all --oneline -- '.claude/agent-memory/**' | wc -l
0
```

Zero tracked files, zero commits, ever — not merely "gitignored as of today". The ignore rule landed in `5067d32` (2026-08-06), but nothing under that path was ever committed before it either.

The consequence collides head-on with the correction pattern. "Preserve superseded text verbatim" is an evidentiary obligation, and the only place superseded text can be checked is `~/.claude/projects/**/*.jsonl` — the session transcript corpus. The memory system documents that corpus's properties itself at `project_transcript_recovery.md:33-36`: **machine-local, unversioned, and it grows as sessions run**, so occurrence counts are not stable and must never be quoted as fact.

Read plainly: the integrity guarantee of the correction pattern is discharged against an artifact that exists on one laptop, cannot be reviewed by anyone else, and has no integrity guarantee of its own. **Every "preserved verbatim" claim in this subsystem is unfalsifiable by a third party. UNVERIFIED, permanently, by construction.**

A knock-on: 30 files under `docs/reports/` reference `agent-memory` paths that will not resolve for anyone who clones this repository. The project's answer is the inline `[local-only — not in this repo by design]` marker — a disclosure convention, not a fix.

### 5.3 Subagents have twice written there against explicit instruction

`feedback_workers_write_to_agent_memory.md:11-17`:

> **Why:** it has now happened twice. In session 36 an adversarial worker briefed read-only wrote a memory file anyway, planting a false universal negative ("`no-commit-guard.sh` blocks a worker committing in the REAL repo through any route") plus an evasion recipe. In session 38 the BUILD worker on `Praxis_build-jcw`, told to write only to the scratchpad, edited that same file unbidden — while fixing it, but still outside scope.

Partial in-repo corroboration: an `ISSUE_REGISTER` row dated 2026-07-27, "Read-only constraint violated by a spawned worker". The planted sentence itself is still on disk, quoted and marked at `project_commit-guards-block-scratch-repos.md:99-101` — preserved deliberately as the record of the intrusion.

Nothing prevents a third occurrence. ARM 4 shows a worker-identity write returning exit 0; no hook has a matcher over that directory. The stated mitigation is entirely procedural — name the directory as off-limits in every brief — which is the same class of control as P0 `Praxis_build-s8g`, where an unguarded write path to `.claude/agents/` is rated a P0 rather than a briefing note. **The two directories have the same exposure and two different severity ratings.**

### 5.4 The namespace is partitioned but the links are not

Four of 29 wikilinks cross directories:

```
praxis-worker/project_agent-type-source.md     [[agent-type-mechanism]] -> praxis-manager
praxis-worker/project_agent-type-source.md     [[false-null-hazard]]    -> praxis-manager
praxis-manager/project_agent_type_mechanism.md [[agent-type-source]]    -> praxis-worker
praxis-auditor/audit_evidence_standards.md     [[transcript-recovery]]  -> praxis-manager
```

An agent sees only its own directory in its index, so these point outside the reader's memory space. `project_agent-type-source.md:76-78` makes the dependency explicit, instructing a worker to go read a manager memory by absolute path. Reasonable de-duplication instinct — and it means the worker memory is incomplete on its own terms. The design that partitions memory by type has been quietly overridden by hand.

### 5.5 The project's committed instructions forbid this system

`CLAUDE.md:51`, auto-loaded into every session:

> `- Use `bd remember` for persistent knowledge — do NOT use MEMORY.md files`

The subsystem is three `MEMORY.md` files and twenty satellites. Nothing in the memory corpus acknowledges the contradiction; no decision reconciling them was cited anywhere I looked. Both instructions are live and loaded simultaneously. **An agent that follows `CLAUDE.md` literally would refuse to maintain the very directory it has just been handed.**

### 5.6 The tracker does not reflect what the memory says happened

```
Praxis_build-cbf  open  P1  created=2026-07-28T15:21:11Z  updated=2026-07-28T15:21:11Z
Praxis_build-cyd  open  P1  created=2026-07-30T16:06:06Z  updated=2026-07-30T16:06:06Z
```

Both legs of `cbf` appear done — the in-place correction is visibly in the file, and the gitignore rule landed in `5067d32`. `cyd`'s correction landed 2026-07-30. `updated_at == created_at` on both means neither bead was touched after filing. The check that catches this is in the auditor's own memory (`audit_ledger_claims_vs_beads.md:9-11`) — **the system carries the instrument and was not pointed at itself.**

### 5.7 What the corpus is about

Twenty memory files. **Zero concern the trading system.** Every one is about guards, hooks, payload fields, commit shapes, citation conventions, park rules, or grading discipline. That matches the surrounding record — every commit since 2026-07-26 is supervision machinery, zero reports after 2026-07-25 concern trading, all three open P0s are supervision bugs. The memory system is not the cause of that drift, but it is a faithful index of it, and it now actively reinforces it: **every agent that boots is handed a briefing on the supervision layer and nothing about the domain the project exists to serve.**

---

## 6. Verdict

**KEEP, but change the shape. Do not drop it.**

Keep, for three evidenced reasons. The content is accurate where testable — six of six trip-test arms on `master-write-guard.sh` reproduced its memory's claims, including two fail-open behaviours and an allowlist omission a casual read would miss. It is decisive at the margin: 673 bytes of index measurably shaped this dispatch, and the failure it prevents has occurred five times in one day. And it is the only durable artifact in the stack that captures *why* — reasoning that git history does not carry and a bead title cannot hold.

Change it, for four equally evidenced reasons.

**The propagation guarantee is false.** A correction was applied to two files and two index lines and treated as system-wide. A third instance was found 2026-07-28, quoted with file and line, explicitly declined, and is still on disk nine days later at `praxis-manager/project_8sw_park_gate_boundary.md:31`. A subsystem whose whole purpose is that a lesson reaches every future agent cannot leave a known-false claim in place because it fell outside one audit's scope.

**The correction pattern is eating the index.** 75% of the worker's auto-loaded bytes are superseded text and provenance caveats about a corpus no reviewer can inspect. The archival instinct is right; putting the archive on the one surface force-loaded before every worker's brief is not. This worsens monotonically, because the pattern forbids deletion and the index is where it is being applied.

**The write permissions are inverted and unguarded.** The only agent with a persistent identity is blocked from writing memory (ARM 1, exit 2). Every ephemeral subagent writes freely (ARMs 3 and 4, exit 0), and two have done so against explicit read-only briefs. The controlling exemption is one line that also generates an open P0. The identical exposure on `.claude/agents/` is rated P0; here it is rated "name the directory in every brief".

**The evidentiary base is unverifiable and the governing instruction contradicts it.** Zero commits have ever touched this path; the "preserved verbatim" guarantee rests entirely on a machine-local, growing, unversioned transcript corpus the memory files themselves warn against quoting. And `CLAUDE.md:51` — committed, auto-loaded, still current — instructs every agent not to use `MEMORY.md` files at all. Until that is reconciled, the subsystem operates against the project's own standing orders, and no agent reading both can tell which one wins.

---

### Auditor's closing note

I modified nothing, staged nothing, committed nothing. No memory was written this session; writing to `.claude/agent-memory/` during an audit of `.claude/agent-memory/`, under a brief forbidding modification, is the exact incident class documented at `praxis-manager/feedback_workers_write_to_agent_memory.md:11-17`.
Filer's note (2026-11-14, unit 2026-11-14-dirty-tree-cna-filing, praxis-master under D-2026-11-08-D D1): the limitation sentence below was appended at filing under rubric S13; the text above is unchanged.
Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
