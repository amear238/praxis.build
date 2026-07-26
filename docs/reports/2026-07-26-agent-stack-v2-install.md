# Agent stack v2 — install with inert `hooks:` blocks stripped

**Date:** 2026-07-26
**Session:** 32
**Repo:** /Volumes/Sensidine/Praxis.build (branch `main`, HEAD `b8008e4`)
**Source drop:** `/Users/admin/Downloads/files (2)/`
**Commit status:** nothing committed. All changes staged via `git add` only.

## Task

Install agent-stack v2's three agent files into `.claude/agents/`, each with its
frontmatter `hooks:` block removed and everything else byte-preserved; keep
`.claude/settings.json` exactly as committed at `b8008e4`; leave
`specs/SPEC_RUBRIC.md` and `.claude/agents/praxis-auditor.md` untouched;
re-verify the three guards against the new agent roster; log the decision.

## Established premise (not re-derived this session)

Agent-frontmatter `hooks:` is silently ignored on Claude Code 2.1.220. This was
proven by a prior live probe with a positive control: the identical script at
the identical relative path never fired in 5/5 frontmatter cases, and fired and
blocked immediately when the same script was wired through `settings.json`. The
frontmatter otherwise parses — `tools:` from the same block IS enforced.
Therefore every `hooks:` block shipped in v2's agent files was inert.

Amear's decision, executed here: install v2's real fixes, keep
`.claude/settings.json` exactly as committed at `b8008e4`, discard v2's
`settings.json` entirely, strip the inert `hooks:` blocks.

## What changed

| Path | Action | Result |
|---|---|---|
| `.claude/agents/praxis-worker.md` | NEW | installed, `hooks:` stripped |
| `.claude/agents/praxis-manager.md` | overwrote v1 | installed, `hooks:` stripped |
| `.claude/agents/praxis-master.md` | overwrote v1 | installed, `hooks:` stripped |
| `.claude/agents/praxis-auditor.md` | untouched | v1 and v2 byte-identical (`79a3e39d`) |
| `.claude/settings.json` | untouched | zero-byte diff vs `HEAD` |
| `specs/SPEC_RUBRIC.md` | untouched | shasum identical before and after |
| `DECISION_LOG.md` | appended | one 5W1H row |

The strip was performed by a purpose-written script that removes only the
top-level `hooks:` key and its indented children from between the frontmatter
delimiters, refusing to run if the opening `---`, the closing `---`, or the
`hooks:` key is not found. Bodies were never touched.

---

## Verification evidence

### TASK 3 (run first) — SPEC_RUBRIC.md baseline, before anything was touched

```
$ shasum specs/SPEC_RUBRIC.md
8c63f0ac65d0b748c2bbbebf5794547013e80401  specs/SPEC_RUBRIC.md
```

Required value `8c63f0ac65d0b748c2bbbebf5794547013e80401` — MATCH.

The drop's own copy of the rubric was also hashed, to confirm the drop was not
carrying a divergent rubric:

```
$ cd "/Users/admin/Downloads/files (2)/" && shasum SPEC_RUBRIC.md
8c63f0ac65d0b748c2bbbebf5794547013e80401  SPEC_RUBRIC.md
```

All three values agree, so no rubric drift was possible from this install.

### Auditor byte-identity check (leave-alone precondition)

```
$ cd "/Users/admin/Downloads/files (2)/" && shasum praxis-auditor.md
79a3e39d42d8645bff7b4d5c4587ae33b37bd2ee  praxis-auditor.md

$ shasum /Volumes/Sensidine/Praxis.build/.claude/agents/praxis-auditor.md
79a3e39d42d8645bff7b4d5c4587ae33b37bd2ee  .../.claude/agents/praxis-auditor.md
```

Identical at `79a3e39d`, as stated. The file was not opened for writing.

### TASK 1 — strip operation, and proof only the `hooks:` lines were removed

```
$ for f in praxis-worker praxis-manager praxis-master; do
    python3 strip_hooks.py "$SRC/$f.md" ".claude/agents/$f.md"; done
OK .../praxis-worker.md  -> .claude/agents/praxis-worker.md:  removed frontmatter lines 9..14 (6 lines)
OK .../praxis-manager.md -> .claude/agents/praxis-manager.md: removed frontmatter lines 10..15 (6 lines)
OK .../praxis-master.md  -> .claude/agents/praxis-master.md:  removed frontmatter lines 24..33 (10 lines)
```

Full diff of each installed file against its source in the drop. Every hunk is
a pure deletion (`Nd M`) of the `hooks:` block and nothing else — no additions,
no modifications, so every other byte including the whole body is preserved:

```
$ diff "$SRC/praxis-worker.md" .claude/agents/praxis-worker.md
9,14d8
< hooks:
<   PreToolUse:
<     - matcher: "Bash"
<       hooks:
<         - type: command
<           command: "./scripts/no-commit-guard.sh"

$ diff "$SRC/praxis-manager.md" .claude/agents/praxis-manager.md
10,15d9
< hooks:
<   PreToolUse:
<     - matcher: "Bash"
<       hooks:
<         - type: command
<           command: "./scripts/no-commit-guard.sh"

$ diff "$SRC/praxis-master.md" .claude/agents/praxis-master.md
24,33d23
< hooks:
<   PreToolUse:
<     - matcher: "Edit|Write|NotebookEdit"
<       hooks:
<         - type: command
<           command: "./scripts/master-write-guard.sh"
<     - matcher: "Bash"
<       hooks:
<         - type: command
<           command: "./scripts/master-bash-guard.sh"
```

No `hooks:` residue anywhere in the installed agent directory:

```
$ grep -rn 'hooks:' .claude/agents/
NONE
```

### TASK 1 — frontmatter re-parses, no orphaned keys

A real YAML parser was used (Ruby's `YAML.safe_load`, since PyYAML is not
installed here) on the text between the opening and closing `---` of each
installed file. A missing delimiter or an orphaned key would raise:

```
$ ruby -ryaml -e '...safe_load each frontmatter, assert delimiters, assert no hooks key...'
praxis-worker:  YAML OK, keys=name,description,model,memory,tools,disallowedTools,maxTurns
praxis-manager: YAML OK, keys=name,description,model,memory,skills,tools,maxTurns
praxis-master:  YAML OK, keys=name,description,model,memory,skills,tools,initialPrompt
praxis-auditor: YAML OK, keys=name,description,model,memory,tools,disallowedTools,maxTurns
```

All four parse. `hooks` is absent from all three rewritten files. Every key the
task required to survive is present: worker keeps `disallowedTools`, `tools`,
`maxTurns: 40`, `memory`, `model`; manager keeps `maxTurns: 60`, `skills`,
`memory`; master keeps `initialPrompt`.

### TASK 1 — full installed frontmatter, opening `---` through closing `---`

`.claude/agents/praxis-worker.md`:

```yaml
---
name: praxis-worker
description: Executes one focused unit of PRAXIS work handed down by praxis-manager. Builds, edits, tests, researches, or runs an adversarial check against another worker's claim. Cannot spawn. Cannot commit.
model: opus
memory: project
tools: Read, Grep, Glob, Bash, Write, Edit, TodoWrite
disallowedTools: Agent
maxTurns: 40
---
```

`.claude/agents/praxis-manager.md`:

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

The manager's `tools:` line reads exactly as required:
`Agent(praxis-worker), Read, Grep, Glob, Bash, Write, Edit, TodoWrite`.

`.claude/agents/praxis-master.md`:

```yaml
---
name: praxis-master
description: PRAXIS session master. Runs as the main thread. Holds the scoping spec, dispatches the manager, spawns the auditor independently, commits, and maintains the three ledgers. Never builds.
model: opus
memory: project
skills:
  - orchestrator-mine
tools: Agent(praxis-manager, praxis-auditor), Read, Grep, Glob, Bash, Write, Edit, TodoWrite, AskUserQuestion
initialPrompt: |
  Run the orchestrator-mine session-start ritual now, before any tool call
  except Read.

  1. Read HANDOFF.md, DISPATCH_LOG.md, DECISION_LOG.md, ISSUE_REGISTER.md,
     STATUS.md, DECISIONS.md, and specs/SPEC_RUBRIC.md.
  2. Staleness check: if the newest ledger entry is older than 48h, run
     `git log -5 --oneline` and `git status`, and record any drift as a
     DECISION_LOG row.
  3. Run `claude --version` and `which -a claude`. State both in the opener.
     If more than one claude binary is on PATH, stop and flag it — a stale
     install has already caused one false BLOCKED verdict in this project.
  4. Read specs/SPEC_RUBRIC.md in full and restate, in the opener, every
     criterion in FROZEN state and the artifact that unblocks each one.
  5. Post the opener (under 15 lines) and STOP. Wait for Amear.
---
```

The master's `tools:` includes both `Write` and
`Agent(praxis-manager, praxis-auditor)`. The `initialPrompt:` block survived
whole, step 3 (`claude --version` / `which -a claude` / stop if more than one
binary) included — that step sits four lines above where the `hooks:` block
used to begin, and the diff above confirms nothing but the `hooks:` lines went.

### TASK 2 — settings.json is untouched

```
$ git diff HEAD --stat -- .claude/settings.json
$
```

Empty output — zero-byte difference from the version committed at `b8008e4`.
v2's `settings.json` was never copied, never merged, and never read in.

All four `PreToolUse` entries still wired:

```
$ jq -r '.hooks.PreToolUse[] | "\(.matcher) -> \(.hooks[0].command)"' .claude/settings.json
Bash -> "$CLAUDE_PROJECT_DIR"/scripts/no-commit-guard.sh
Bash -> "$CLAUDE_PROJECT_DIR"/.claude/hooks/gate-commit.sh
Write|Edit|NotebookEdit -> "$CLAUDE_PROJECT_DIR"/scripts/master-write-guard.sh
Bash -> "$CLAUDE_PROJECT_DIR"/scripts/master-bash-guard.sh
```

Both concurrency env vars still present:

```
$ jq -c '.env' .claude/settings.json
{"ORCH_N8N_WEBHOOK":"https://n8n.myzerker626.win/webhook/praxis-orch-notify","CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH":"2","CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS":"8"}
```

`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` and
`CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` are both there.

The `agent` key stays absent:

```
$ jq '.agent' .claude/settings.json
null
```

The other hook events v2's settings.json would have dropped are all still
present alongside `PreToolUse`:

```
$ jq -r '.hooks | keys[]' .claude/settings.json
PreCompact
PreToolUse
SessionStart
Stop
SubagentStart
SubagentStop
```

### TASK 3 — SPEC_RUBRIC.md after the work

```
$ shasum specs/SPEC_RUBRIC.md
8c63f0ac65d0b748c2bbbebf5794547013e80401  specs/SPEC_RUBRIC.md
```

Identical to the baseline recorded before any file was touched, and identical
to the required value. Byte-identical before and after.

### TASK 4 — guard re-verification against the new agent roster

Method: eight synthetic `PreToolUse` payloads were generated into individual
JSON files and piped into the guards by a runner script. No commit literal ever
appeared on the calling command line — the live `no-commit-guard.sh` is wired
for this very session's Bash calls and would have blocked the test harness
itself. The commit string was assembled with `printf 'git %s -m x' 'commit'`
into a file, and the runner referenced payloads only by filename.

Guards were run exactly as committed. No guard script was edited, before or
after testing.

```
----- CASE 1 -----
$ ./scripts/master-write-guard.sh < p1.json
payload: {"tool_name":"Write","agent_type":"praxis-master","tool_input":{"file_path":"/x/src/thing.cs"}}
stderr: BLOCKED: praxis-master may only write ledgers, specs, and reports. Dispatch praxis-manager for '/x/src/thing.cs'.
exit: 2   expected: 2   MATCH

----- CASE 2 -----
$ ./scripts/master-write-guard.sh < p2.json
payload: {"tool_name":"Write","agent_type":"praxis-worker","agent_id":"abc","tool_input":{"file_path":"/x/src/thing.cs"}}
stderr: (none)
exit: 0   expected: 0   MATCH

----- CASE 3 -----
$ ./scripts/master-write-guard.sh < p3.json
payload: {"tool_name":"Write","agent_type":"praxis-master","tool_input":{"file_path":"/x/docs/reports/r.md"}}
stderr: (none)
exit: 0   expected: 0   MATCH

----- CASE 4 -----
$ ./scripts/no-commit-guard.sh < p4.json
payload: {"tool_name":"Bash","agent_type":"praxis-worker","agent_id":"abc","tool_input":{"command":"git commit -m x"}}
stderr: BLOCKED: subagents leave work staged. The master commits after praxis-auditor passes.
exit: 2   expected: 2   MATCH

----- CASE 5 -----
$ ./scripts/no-commit-guard.sh < p5.json
payload: {"tool_name":"Bash","agent_type":"praxis-manager","agent_id":"abc","tool_input":{"command":"git commit -m x"}}
stderr: BLOCKED: subagents leave work staged. The master commits after praxis-auditor passes.
exit: 2   expected: 2   MATCH

----- CASE 6 -----
$ ./scripts/no-commit-guard.sh < p6.json
payload: {"tool_name":"Bash","agent_type":"praxis-master","tool_input":{"command":"git commit -m x"}}
stderr: (none)
exit: 0   expected: 0   MATCH

----- CASE 7 -----
$ ./scripts/no-commit-guard.sh < p7.json
payload: {"tool_name":"Bash","tool_input":{"command":"git commit -m x"}}
stderr: (none)
exit: 0   expected: 0   MATCH

----- CASE 8 -----
$ ./scripts/master-bash-guard.sh < p8.json
payload: {"tool_name":"Bash","agent_type":"praxis-worker","agent_id":"abc","tool_input":{"command":"echo x > src/thing.cs"}}
stderr: (none)
exit: 0   expected: 0   MATCH
```

Summary — 8/8 match, zero deviations:

| # | Guard | Case | Expected | Actual |
|---|---|---|---|---|
| 1 | master-write-guard | Write, master, no agent_id, `/x/src/thing.cs` | 2 | 2 |
| 2 | master-write-guard | Write, worker, agent_id=abc, `/x/src/thing.cs` | 0 | 0 |
| 3 | master-write-guard | Write, master, no agent_id, `/x/docs/reports/r.md` | 0 | 0 |
| 4 | no-commit-guard | worker, agent_id=abc, commit | 2 | 2 |
| 5 | no-commit-guard | manager, agent_id=abc, commit | 2 | 2 |
| 6 | no-commit-guard | master, no agent_id, commit | 0 | 0 |
| 7 | no-commit-guard | neither field (ordinary session), commit | 0 | 0 |
| 8 | master-bash-guard | worker, agent_id=abc, `echo x > src/thing.cs` | 0 | 0 |

Case 1 is the significant one. Under v1 the master had no `Write`, so the
write-guard's deny arm could not be reached through `Write` at all. v2 grants
the master `Write`, which makes that arm load-bearing for the first time. It
denies correctly: a master `Write` to `/x/src/thing.cs` exits 2 with the
dispatch-instead message, while a master `Write` to `docs/reports/` passes
(case 3). Case 2 confirms the guard does not catch workers, which need `Write`
to build — the `agent_id` early-exit at line 8 of the script handles that.
Case 7 confirms ordinary non-stack sessions are untouched by the commit guard,
which is what keeps `.claude/hooks/gate-commit.sh` the operative gate there.

### Why the guards remain correctly enforced without any frontmatter hooks

The three guards are wired in `.claude/settings.json` at the project level, so
they run for every tool call in the project regardless of which agent is
executing. Each guard then does its own role scoping in-script, off the
`agent_type` and `agent_id` fields of the live `PreToolUse` payload:

- `no-commit-guard.sh` exits 0 when `agent_type` is absent entirely (ordinary
  session), exits 0 for the main-thread master (`agent_type=praxis-master` with
  empty `agent_id`), and blocks the commit verbs for everything else in the
  stack.
- `master-write-guard.sh` and `master-bash-guard.sh` both early-exit 0 unless
  `agent_id` is empty AND `agent_type` is `praxis-master`.

This is the same fail-safe behavior v2's frontmatter blocks were trying to
express, achieved through the only mechanism that actually fires on 2.1.220.
Because scoping is by payload field rather than by declaration site, adding
`praxis-worker` to the roster required no wiring change — case 2 and case 8
confirm the new agent type is handled correctly by guards that predate it.

### Final installed-state hashes

```
$ shasum .claude/agents/praxis-*.md
79a3e39d42d8645bff7b4d5c4587ae33b37bd2ee  .claude/agents/praxis-auditor.md
87cd611c26843fa5d0b0675033862e28a56fa8e1  .claude/agents/praxis-manager.md
d473655e0a0eb7eb430ecdffb8a01936d207eea7  .claude/agents/praxis-master.md
80ce2a7f6ea93873433475b45c400422a5813e20  .claude/agents/praxis-tutor.md
04de0048758fc0382b763d872c7590149a9df512  .claude/agents/praxis-worker.md
```

`praxis-auditor.md` still `79a3e39d` — untouched, as required. `praxis-tutor.md`
was outside this task's scope and was not modified.

### TASK 5 — DECISION_LOG row

One row appended, matching the existing single-line 5W1H pipe format used
throughout that file. Field presence verified in order:

```
$ tail -1 DECISION_LOG.md | grep -o 'WHO:\|WHAT:\|WHY:\|WHERE:\|WHEN:\|HOW:\|STATE:'
WHO: WHAT: WHY: WHERE: WHEN: HOW: STATE:
```

The row records: the inert `hooks:` blocks stripped from the three installed
agent files on Amear's decision; v2's `settings.json` discarded wholesale
because adopting it would drop three working guards plus the pre-existing
`PreCompact`, `SessionStart`, `Stop`, and `gate-commit` hooks; and the guards
remaining wired in `settings.json` as committed at `b8008e4` with in-script
`agent_type`/`agent_id` scoping, which already satisfies v2's stated fail-safe
requirement.

---

## Files staged

- `.claude/agents/praxis-worker.md` (new)
- `.claude/agents/praxis-manager.md` (modified)
- `.claude/agents/praxis-master.md` (modified)
- `DECISION_LOG.md` (modified)
- `docs/reports/2026-07-26-agent-stack-v2-install.md` (new, this file)

Staged with `git add` only. Nothing was committed, pushed, stashed, or amended.
`.claude/settings.json` and `specs/SPEC_RUBRIC.md` are not in the staged set
because neither was modified.

## Deviations

None. All eight guard cases returned their expected exit codes on the first
run, no guard script was edited, and both protected files verified unchanged.

Result: PASS
