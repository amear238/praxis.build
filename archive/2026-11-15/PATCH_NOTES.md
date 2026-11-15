# PATCH_NOTES

Corrections to shipped drops. **The original claim is reproduced verbatim first,
the correction beneath it.** A drop's claim is never edited or deleted here — a
document containing only the fixed version destroys the record the correction
exists to preserve.

This file shipped with the agent-stack v2 drop and was never committed. Created
2026-07-26 at commit `712a997`.

---

## PN-001 — agent-stack v2: `Agent(<type>)` allowlist narrowing does not work as written

**Drop:** agent-stack v2, `/Users/admin/Downloads/files (2)/`
**Installed:** 2026-07-26, session 32
**Affected files:** `.claude/agents/praxis-manager.md`, `.claude/agents/praxis-master.md`

### As shipped — verbatim

`.claude/agents/praxis-manager.md` frontmatter, exactly as the drop shipped it:

```yaml
---
name: praxis-manager
description: Spawns and supervises praxis-worker subagents for one unit of PRAXIS work. Decomposes, dispatches, stress-tests every step against the rubric, and returns a graded report. Cannot commit. Cannot reach the auditor.
model: opus
memory: project
skills:
  - orchestrator-mine
tools: Agent(praxis-worker), Read, Grep, Glob, Bash, Write, Edit, TodoWrite
maxTurns: 60
---
```

`.claude/agents/praxis-master.md`, same drop:

```yaml
tools: Agent(praxis-manager, praxis-auditor), Read, Grep, Glob, Bash, Write, Edit, TodoWrite, AskUserQuestion
```

The claim carried in that frontmatter is the phrase **"Cannot reach the
auditor."**, and the mechanism claimed to deliver it is the narrowed
`tools: Agent(praxis-worker)` line. The v2 install report restated the mechanism
as satisfied on inspection:

> The manager's `tools:` line reads exactly as required:
> `Agent(praxis-worker), Read, Grep, Glob, Bash, Write, Edit, TodoWrite`.
>
> — `docs/reports/2026-07-26-agent-stack-v2-install.md:186-187`

### Correction

**The narrowing is not honoured on a spawned subagent. The claim is false as
written.** `praxis-manager`, when spawned by `praxis-master`, *can* reach
`praxis-auditor`.

A subagent does not receive its own declared `Agent()` allowlist. It inherits
the **spawning parent's** roster. The same allowlist *is* enforced when the agent
runs as a main thread, which is why inspection of the file looks correct and
behaviour differs.

### Evidence and method

Control experiment, 2026-07-26, Claude Code 2.1.220, recorded in
`docs/reports/2026-07-26-agent-stack-v2-triptests.md` (T6, T7, and "Root cause").

Method: `praxis-master` spawned `praxis-manager`; the manager was asked to report
its own visible agent roster and then to attempt an auditor spawn.

1. **Roster observed.** The manager reported
   `Available agents: praxis-auditor, praxis-manager` — exactly the **master's**
   allowlist `Agent(praxis-manager, praxis-auditor)`, not its own declared
   `Agent(praxis-worker)`.
2. **T6 — containment breach.** The manager spawned `praxis-auditor`
   successfully. Expected: refusal. Producer/grader separation was policy-only,
   not enforced.
3. **T7 — corollary.** `praxis-worker` appeared in no parent's allowlist, so it
   was absent from every inherited roster and unspawnable:
   `Agent type 'praxis-worker' not found.` The agent file itself was valid —
   hexdump-clean frontmatter, and it loaded fine as a main thread
   (`--agent praxis-worker` → `WORKER ALIVE`, exit 0).

Both symptoms share the one defect. This is the same class as the already-
documented `hooks:` frontmatter key: **a field accepted without error and then
not honoured.**

### Disposition

- `Agent(<type>)` narrowing is dead as a scoping mechanism — ruling R2, rubric
  **S10**. It is not relied on anywhere in the stack.
- Producer/grader separation moved to a registered `PreToolUse` hook,
  `scripts/agent-spawn-guard.sh` — accepted as a permanent component under
  ruling R1, specified in `docs/agent-spawn-guard.md`.
- T7 was repaired by adding `praxis-worker` to **`praxis-master`**'s allowlist
  (`Agent(praxis-manager, praxis-auditor, praxis-worker)`), which the manager
  inherits. `praxis-manager.md`'s own `Agent(praxis-worker)` line remains in the
  file but is **inert** — it is not what makes worker spawning work.
- Nesting is depth-capped at master → manager → worker — rubric **S11**.

### Not silently fixed

The misleading `Agent(praxis-worker)` line is deliberately left in
`praxis-manager.md`. Removing it would make the file read as though the
narrowing had never been claimed. Its inertness is recorded here and in S10
instead.

---

## PN-002 — v2 install report: "neither was modified" is stale as of `712a997`

**Report:** `docs/reports/2026-07-26-agent-stack-v2-install.md:430-432`
**Written:** 2026-07-26, session 32, before the guard existed
**Corrected:** 2026-07-26, session 33, ruling R4 — **by append; the report's own
lines are left exactly as written.**
**Found by:** orchestrator-auditor, P0 baseline audit (staged sha `8e6fd1d7`,
verdict PASS, flagged non-blocking). Filed as `Praxis_build-9j4`.

### As written — verbatim

> Staged with `git add` only. Nothing was committed, pushed, stashed, or amended.
> `.claude/settings.json` and `specs/SPEC_RUBRIC.md` are not in the staged set
> because neither was modified.

### Correction

**`.claude/settings.json` was modified.** In commit `712a997` its blob went
`e83e561 → 4521f90`, **+10 lines, 0 deletions**, adding the `PreToolUse` entry
that registers `scripts/agent-spawn-guard.sh` on the `Agent` matcher:

```
$ git show --stat 712a997 -- .claude/settings.json
 .claude/settings.json | 10 ++++++++++
 1 file changed, 10 insertions(+)
```

The sentence was true when written — the guard did not yet exist, and the
registration was added later in the same session. It is stale, not false-at-
authorship. `specs/SPEC_RUBRIC.md` likewise gained S9–S11 after that sentence
was written.

The change is documented correctly in two other places
(`docs/reports/2026-07-26-agent-stack-v2-triptests.md` Step 3, and the
`DECISION_LOG.md` 15:05Z row, both carrying the exact diff). The defect is that
the install report **reads as though no change occurred** to a reader who stops
there.

### Why it is not edited in place

Ruling R4: fix by append, not rewrite. Editing line 432 would erase the evidence
that the v2 install was reported against a pre-guard state — which is the whole
reason the S9/S10 work happened afterwards. A pointer to this entry is appended
at the end of that report.

---

## PN-003 — two 14:50Z ledger rows cite a path that was deliberately deleted

**Rows:** `DECISION_LOG.md:51` and `ISSUE_REGISTER.md:31`, both
`[2026-07-26T14:50Z]`
**Cited path:** `reports/2026-07-26-harness-auditor-spawn-payload.md`
**Corrected:** 2026-07-26, session 33, ruling R4 — **by append; both ledgers are
append-only and neither row is touched.**
**Found by:** orchestrator-auditor, same audit. Filed as `Praxis_build-9j4`.

### As written — verbatim (the `WHERE:` field of each row)

`DECISION_LOG.md:51`:

> WHERE: reports/2026-07-26-harness-auditor-spawn-payload.md; ISSUE_REGISTER row
> [2026-07-26T14:50Z]

`ISSUE_REGISTER.md:31`:

> WHERE: .claude/agents/praxis-manager.md:8;
> reports/2026-07-26-harness-auditor-spawn-payload.md

### Correction

**That file does not exist and will not be restored.** It was written to a
non-conventional top-level `reports/` directory (project convention is
`docs/reports/`) during the Step 1 instrumentation run, was confirmed untracked
via `git ls-files --others --exclude-standard`, and was deleted as stray during
trip-tests Step 6. It was never committed, so there is no version to restore.
Its deletion is itself documented:

> One stray was found and removed: an untracked top-level `reports/` directory
> containing `2026-07-26-harness-auditor-spawn-payload.md` […] It was confirmed
> untracked via `git ls-files --others --exclude-standard` before deletion, so
> nothing tracked was lost.
>
> — `docs/reports/2026-07-26-agent-stack-v2-triptests.md`, Step 6

**Surviving evidence for the claims those two rows rest on**, none of which
depended on the deleted file:

| Claim in the 14:50Z rows | Where the evidence actually lives |
|---|---|
| manager spawned auditor with no denial (3rd reproduction) | `DISPATCH_LOG.md` hook-written `SubagentStart` rows, `14:50:20Z praxis-manager` → `14:50:28Z praxis-auditor`; prior pairs 14:16:47→14:16:50 and 14:34:15→14:34:23 |
| child inherits the parent's roster | `docs/reports/2026-07-26-agent-stack-v2-triptests.md`, T6/T7 "Root cause"; `PATCH_NOTES.md` PN-001 |
| no hook fired on that path | superseded by `712a997`, which registered `scripts/agent-spawn-guard.sh` on the `Agent` matcher; guard behaviour is specified in `docs/agent-spawn-guard.md` §5 |

The probe file's own content was a payload capture; the payload shape it was
meant to record is now captured live, in full and unedited, in
`docs/agent-spawn-guard.md` §2.

### Why the rows are not repointed in place

`DECISION_LOG.md` and `ISSUE_REGISTER.md` are append-only. Rewriting a `WHERE:`
field would be a silent history edit of exactly the kind those ledgers exist to
prevent — and it would hide that the master wrote a report to the wrong
directory, which the 14:50Z DECISION_LOG row records against itself on purpose.
Correction rows are appended to both ledgers pointing here.

### Effect on `Praxis_build-9j4`'s verify line

9j4's verification reads "no ledger row cites a nonexistent path (grep the cited
paths and confirm each resolves)." **That criterion is not satisfiable under
ruling R4** — an append cannot make a deleted, never-committed path resolve. It
is superseded by: *every dangling citation carries an appended correction row
that resolves to surviving evidence.* Recorded here rather than by editing the
bead's acceptance text.
