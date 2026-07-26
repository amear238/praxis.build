# Agent-Stack Install — 2026-07-25

**Result: BLOCKED at P0 (feature-availability gate). No files installed. Nothing staged.**

---

## Task

Install a three-layer master/manager/auditor agent stack in this repo from the
artifacts dropped at `/Users/admin/Downloads/files (1)/` (agents/*.md,
scripts/*.sh, specs/SPEC_RUBRIC.md, settings.json, INSTALL.md), then trip every
guard to prove each one actually blocks. INSTALL.md and the task both mandate a
P0 feature-availability check FIRST, because several fields the stack depends on
"landed in the 2.1.19x–2.1.21x range and are SILENTLY IGNORED on older builds. A
silently ignored field is a guard that isn't there." Instruction: **if any field
is unsupported, STOP** — do not install, do not substitute a prompt instruction
for a missing hook.

Build: `claude --version` → `2.1.206 (Claude Code)`.

---

## Version-support matrix

Fields 7 and 8 were independently confirmed by me against the official doc
(`code.claude.com/docs/en/env-vars.md`) with the literal source marker pasted
below. Fields 1–6 are per documentary citations from the `claude-code-guide`
subagent against `code.claude.com/docs/en/sub-agents.md`.

| # | Field | Verdict on 2.1.206 | Evidence |
|---|-------|--------------------|----------|
| 1 | `agent` key in `.claude/settings.json` (main-thread agent) | SUPPORTED | settings.md: "Run the main thread as a named subagent" |
| 2 | `initialPrompt` frontmatter field | SUPPORTED | sub-agents.md: "Auto-submitted as the first user turn when this agent runs as the main session agent (via `--agent` or the `agent` setting)" |
| 3 | `skills:` frontmatter (preload) | SUPPORTED | sub-agents.md: "Skills to preload into the subagent's context at startup. The full skill content is injected" |
| 4 | `memory:` frontmatter | SUPPORTED | sub-agents.md: "Persistent memory scope: `user`, `project`, or `local`" |
| 5 | `Agent(type)` allowlist syntax in `tools:` | SUPPORTED | sub-agents.md: "use `Agent(agent_type)` syntax in the `tools` field" |
| 6 | `SubagentStart` / `SubagentStop` hooks with name matchers | SUPPORTED | sub-agents.md: "Both events support matchers to target specific agent types by name. The matcher value is the agent's frontmatter `name`" |
| 7 | `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` | **NOT SUPPORTED** | doc marker `{/* min-version: 2.1.217 */}` — "Requires Claude Code v2.1.217 or later" |
| 8 | `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` | **NOT SUPPORTED** | doc marker `{/* min-version: 2.1.217 */}` — "Requires Claude Code v2.1.217 or later" |

### Literal doc evidence for the two blocking fields

```
| `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` | {/* min-version: 2.1.217 */}Number of
subagent layers allowed below the main conversation (default: 1). At the default,
subagents can't spawn their own subagents; set `2` or higher to allow it. Accepts
a positive whole number in plain digits; anything else is ignored, so the limit
can be raised but not turned off. Requires Claude Code v2.1.217 or later
```

```
| `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` | {/* min-version: 2.1.217 */}How many
subagents can be running in one session before the Agent tool refuses to spawn
another (default: 20). ... Requires Claude Code v2.1.217 or later
```

### Bonus finding (relevant if/when unblocked)

`claude-code-guide` also confirmed, from sub-agents.md line 610:
> "Frontmatter hooks fire when the agent is spawned as a subagent through the
> Agent tool or an @-mention, and when the agent runs as the main session via
> `--agent` or the `agent` setting."

This means once the version gate is cleared, guards 1–3 (the master
write/bash guards and the manager no-commit guard, all defined in agent
frontmatter) can be tripped by dispatching the agent as a subagent — the
frontmatter `PreToolUse` hooks apply in that path.

---

## Why this is a hard STOP, not a warning

The stack's core promise is structural separation: **master coordinates →
manager decomposes → workers build**, three distinct contexts. That third layer
(manager spawning a worker) exists ONLY if `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`
is honored. INSTALL.md § Nesting states it plainly:

> "Depth is off by default in Claude Code — subagents cannot spawn subagents.
> The setting `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH: "2"` is what makes
> master → manager → worker possible. Without it the manager silently does the
> work itself and the whole separation collapses into one context."

On 2.1.206 the setting is silently ignored (default depth = 1). The manager
would do the work itself, in one context — precisely the single-context spec
drift this stack was built to prevent. The task's own nesting check specifies
this outcome as "a FAIL, not a warning." Proceeding to install and running the
five trip-tests would produce a green-looking two-layer install while the
load-bearing third layer is absent — a decorative guard. The task forbids
substituting a prompt instruction for the missing control, so there is no
in-build workaround.

---

## Files installed

**None.** Halted at P0 before any copy, chmod, settings merge, or `agent`-key
install. The install artifacts remain untouched in
`/Users/admin/Downloads/files (1)/`.

Preconditions that WERE verified (read-only recon, in case they shorten the
re-run after upgrade):
- `jq` present: `/usr/bin/jq`, jq-1.7.1-apple.
- No filename collisions between the 5 new hook scripts and existing `scripts/`.
- settings.json merge would be **purely additive** — new keys `agent`, two
  `CLAUDE_CODE_*` env vars, `SubagentStart`, `SubagentStop`, `permissions.deny`;
  none collide with the existing `.claude/settings.json` (which holds
  `env.ORCH_N8N_WEBHOOK`, PreCompact/SessionStart/PreToolUse(Bash→gate-commit)/Stop
  hooks). No conflict to resolve.
- `.claude/agents/` exists; `docs/reports/` exists; all four ledgers exist;
  `specs/` does NOT yet exist (would be created on install).

---

## Trip-test evidence (5 guards + nesting)

**Not run.** All five trip-tests and the nesting check require the stack to be
installed first (agent key active, SubagentStart/Stop hooks wired,
`MAX_SUBAGENT_SPAWN_DEPTH=2` honored). Running them on a build where the depth
control is a no-op would either fail outright (nesting) or give false assurance
for the layers that happen to work. Per the task, four of five firing is a FAIL;
a two-layer install cannot honestly pass the deliverable. Deferred until the
version gate clears.

---

## Files staged

**None.**

---

## Result: BLOCKED

Root cause: Claude Code **2.1.206** on this machine; the stack requires
**>= 2.1.217** for `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` (and
`CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`).

Remedy: upgrade Claude Code to >= 2.1.217, confirm with `claude --version`, then
restart this install from P0. Do not substitute a prompt instruction for the
missing depth control. Gap logged in ISSUE_REGISTER.md
(row dated 2026-07-25T16:33Z).
