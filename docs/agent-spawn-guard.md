# `scripts/agent-spawn-guard.sh` — specification and control evidence

**Status:** permanent stack component (human ruling R1, 2026-07-26).
**Written:** 2026-07-26, against guard sha256 `6e186f9f5a3c2a3ab3f01c41db21dbf5b80eafb3aecc05ab89aa7426680cac0b`.
**Baseline commit:** `712a997ada09a5db87ce0cfbfa59b6055360ecb6`.
**Harness:** Claude Code 2.1.220.

> **UNVERIFIED MECHANISM — read before relying on the terminal-layer rule.**
> The guard script's own header (`scripts/agent-spawn-guard.sh:32-33`) names
> `disallowedTools: Agent` on `praxis-worker.md` as the worker's *own* control
> and calls this script "the second, independent mechanism." **That claim has
> never been tested.** No experiment in this project has shown that
> `disallowedTools` is honoured on a *spawned* subagent, and the one adjacent
> frontmatter field that was tested — `tools: Agent(...)` narrowing — turned out
> to be silently discarded on child spawn (ruling R2, rubric S10, `PATCH_NOTES.md`
> PN-001). Until the experiment below is run, treat the omitted-`subagent_type`
> bypass in §3.1 as **unguarded**, not as a defence-in-depth gap. Tracked as
> **`Praxis_build-1ys`** (P0, open — deliberately not repaired here, per ruling R6).
>
> **The toggle experiment that would settle it.** Same A/B shape as the S9
> control in §5, run on the mechanism instead of on a config key:
>
> 1. Spawn `praxis-worker` at real depth 2 (`master → manager → worker`), with
>    `disallowedTools: Agent` present in `praxis-worker.md` exactly as shipped.
>    Have the worker call `Agent` with `subagent_type` **omitted**. Record
>    whether the tool is refused, and record the worker's own visible tool list.
> 2. Remove **only** the `disallowedTools: Agent` line — change nothing else —
>    and repeat step 1 byte-for-byte.
> 3. Restore the line.
>
> Read it as: **different** behaviour between 1 and 2 ⇒ the field is honoured on a
> spawned child and the bypass is genuinely covered. **Identical** behaviour ⇒
> the field is inert on a spawned child (the S10 failure mode again), the guard
> is the only mechanism, and its omitted-`subagent_type` hole is a live bypass
> that must be closed in the script itself.
>
> This branch is a clean isolate: with `subagent_type` omitted, the guard exits 0
> either way (§3.1), so it cannot confound the result. What must also be recorded
> is whether the spawn *produced a real subagent* — a refusal that merely returns
> an error string is not the same as a blocked spawn, and the DISPATCH_LOG
> `SubagentStart` rows (hook-written, unforgeable by the agent) are the evidence
> that separates them.

## Why this document exists

`Agent(<type>)` frontmatter allowlist narrowing is dead as a scoping mechanism
(ruling R2, rubric S10): it is honoured on a main thread and discarded on child
spawn, where the child inherits the *parent's* roster. This script is therefore
**the only thing enforcing producer/grader separation.** It was written
mid-session under a live blocker and had no spec until now.

Three silently-ignored-config-field incidents have already occurred in this
project (`hooks:` frontmatter, `tools: Agent(...)` narrowing, and the shipped v2
settings wiring). Every field this script reads is therefore positive-controlled
below per rubric S9 — not documented from the script's own comments.

## 1. Registration

Registered in exactly one place:

```
/Volumes/Sensidine/Praxis.build/.claude/settings.json:95
  hooks.PreToolUse[] → { "matcher": "Agent",
                         "command": "\"$CLAUDE_PROJECT_DIR\"/scripts/agent-spawn-guard.sh" }
```

It is **project-scoped, not global.** `~/.claude/settings.json` has no `hooks`
key; `~/.claude/settings.local.json`, `.claude/settings.local.json`, and
`/Library/Application Support/ClaudeCode/managed-settings.json` do not exist.
The guard cannot fire in any repo other than this one. Behavioural confirmation
is in §5 (T9).

## 2. Payload fields it keys on

Captured live from a real `PreToolUse` / `Agent` payload, not inferred:

| Field path | Meaning | Read into |
|---|---|---|
| `.tool_name` | tool being invoked; `"Agent"` for a spawn | `TOOL` |
| `.agent_type` | **the CALLER's** agent type; absent on an ordinary main thread | `CALLER` |
| `.tool_input.subagent_type` | **the TARGET** type being spawned | `TARGET` |

`.agent_id` is *not* read by this guard (it is read by `no-commit-guard.sh` to
distinguish a main-thread master from a spawned one).

Live payload, unrelated-repo main thread, full and unedited:

```json
{
  "session_id": "dd35922e-f268-4a09-88e9-b732cec5184e",
  "cwd": "/private/tmp/.../scratchpad/t9-unrelated",
  "permission_mode": "bypassPermissions",
  "hook_event_name": "PreToolUse",
  "tool_name": "Agent",
  "tool_input": {
    "description": "Reply PONG",
    "prompt": "Reply with the single word PONG and nothing else.",
    "subagent_type": "general-purpose",
    "run_in_background": false
  },
  "tool_use_id": "toolu_01QFMjWEVk4rmZSXmgrCBCWv"
}
```

Note what is **absent**: there is no `agent_type` key on a main thread. That is
load-bearing for §4.

## 3. The deny condition

As a single predicate — deny (exit 2) if and only if:

```
  .tool_name == "Agent"
  AND  .agent_type            is present and non-empty
  AND  .tool_input.subagent_type is present and non-empty
  AND  (   .agent_type == "praxis-worker"
        OR (.agent_type == "praxis-manager" AND .tool_input.subagent_type == "praxis-auditor") )
```

Everything else exits 0.

Two rules ride that predicate:

- **Terminal layer.** `praxis-worker` may not spawn at all.
- **Producer/grader separation.** `praxis-manager` may not spawn
  `praxis-auditor`. The manager must never pick or brief its own grader; the
  master spawns the auditor independently.

### 3.1 Known bypass — omitted `subagent_type`

The two non-empty guards run **before** both deny rules. `subagent_type` is an
optional field on the Agent tool: *"If omitted, the general-purpose agent is
used."* So a `praxis-worker` that calls `Agent` while simply **omitting**
`subagent_type` still spawns a real `general-purpose` subagent, and the guard
allows it:

```
worker -> general-purpose (explicit)     exit=2 stderr_bytes=64 BLOCKED: praxis-worker is the terminal layer and may not spawn.
worker -> (omitted)                      exit=0 stderr_bytes=0
worker -> empty string                   exit=0 stderr_bytes=0
```

The terminal-layer rule is bypassable by omission. The producer/grader rule is
not (it requires `subagent_type == "praxis-auditor"`, which cannot be reached by
omitting the field).

The guard's header names `disallowedTools: Agent` on `praxis-worker.md` as the
second, independent mechanism covering this. **That mechanism is unverified.**
R2 established that `tools: Agent(...)` is silently discarded on child spawn;
whether `disallowedTools` survives child spawn has not been tested. If it does
not, this is an unguarded bypass rather than a defence-in-depth gap. Filed as
**`Praxis_build-1ys`** (P0, open); not repaired here, because repairing it is a
code change to the component this document was commissioned to describe. The
toggle experiment that settles it is written out in the header block above.

## 4. The fail-safe branch

**It fails OPEN — exit 0 — on anything it cannot positively identify.** This
matches the script's own header (`FAIL SAFE: exit 0 on anything not positively
identified as a forbidden spawn`) but the phrase "fail safe" is worth stating
unambiguously: *safe* here means *does not break unrelated work*, not *denies
when unsure*.

Observed, every branch, exit code and stderr byte count:

```
agent_type ABSENT (live unrelated-repo shape)              exit=0 stderr_bytes=0
agent_type empty string                                    exit=0 stderr_bytes=0
subagent_type ABSENT                                       exit=0 stderr_bytes=0
malformed JSON                                             exit=0 stderr_bytes=0
empty stdin                                                exit=0 stderr_bytes=0
non-Agent tool (Bash)                                      exit=0 stderr_bytes=0
```

Allowed spawns, confirmed silent:

```
master  -> auditor                                         exit=0 stderr_bytes=0
master  -> manager                                         exit=0 stderr_bytes=0
manager -> worker                                          exit=0 stderr_bytes=0
```

## 5. S9 positive control on every field it reads

Method, per field: (a) confirm the guard **fires** with the field present and
matching; (b) place an **invented key at the same position**, change nothing
else, and confirm **byte-identical silence**. Harness fed synthetic payloads to
the guard on stdin.

```
######## FIELD 1: .tool_name ########
P  tool_name=Agent      (worker spawn, must FIRE)          exit=2 stderr_bytes=64
    stderr: BLOCKED: praxis-worker is the terminal layer and may not spawn.
C  tool_nayme=Agent     (invented key, must be SILENT)     exit=0 stderr_bytes=0

######## FIELD 2: .agent_type ########
P  agent_type=praxis-worker         (must FIRE)            exit=2 stderr_bytes=64
    stderr: BLOCKED: praxis-worker is the terminal layer and may not spawn.
C  agent_tyme=praxis-worker         (invented, SILENT)     exit=0 stderr_bytes=0

######## FIELD 3: .tool_input.subagent_type ########
P  subagent_type=praxis-auditor     (mgr->auditor, FIRE)   exit=2 stderr_bytes=99
    stderr: BLOCKED: praxis-manager may not spawn the auditor. The master spawns praxis-auditor independently.
C  subagent_tyme=praxis-auditor     (invented, SILENT)     exit=0 stderr_bytes=0
```

All three fields are genuinely read. None is a silently-ignored key.

## 6. Which of T6 and T7 depend on this guard

The brief carried the claim that both do. Checked against the artifacts — **only
T6 does.**

- **T6** (*manager must be refused the auditor*) — depends on this guard
  **entirely and solely.** The allowlist that was supposed to enforce it is dead
  (S10). Nothing else in the stack blocks `manager → auditor`. If this guard is
  removed, unregistered, or its `.agent_type` read breaks, T6 silently regresses
  to the containment breach recorded in the v2 trip tests.

- **T7** (*nesting must name the type*) — **does not depend on it.** T7 failed
  with `Agent type 'praxis-worker' not found.` because `praxis-worker` appeared
  in no parent's `Agent()` allowlist and so was absent from every inherited
  roster. It was fixed by adding `praxis-worker` to **`praxis-master`**'s
  allowlist (`tools: Agent(praxis-manager, praxis-auditor, praxis-worker)`),
  which the manager then inherits. `praxis-manager.md`'s own
  `tools: Agent(praxis-worker)` line is inert per S10 and is not what fixed it.

  The guard's only obligation to T7 is **not to interfere**, confirmed above:
  `manager -> worker` exits 0 with 0 bytes on stderr.

## 7. Maintenance rule

Any change to this script, to its `settings.json` registration, or to the
harness's `PreToolUse`/`Agent` payload shape invalidates §2–§5. Re-run the S9
control harness and re-paste the output here. A change that leaves this document
un-updated should be treated as a failed change.
