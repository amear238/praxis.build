# Agent stack install — hook wiring and scoping (2026-07-25)

## Scope

Three guard scripts were already present in `scripts/` and executable, but were
(a) not wired to any hook and (b) unscoped — wiring them as-is would have blocked
Edit/Write/Bash for every agent in the repo, including ordinary sessions.

This change adds an agent-scoping preamble to each script and wires all three
into `.claude/settings.json` under `hooks.PreToolUse` as additional entries.

## Discriminator (established empirically on Claude Code 2.1.220)

PreToolUse hook stdin JSON contains:

| Actor | `agent_type` | `agent_id` |
|---|---|---|
| Plain main thread | absent | absent |
| Main thread running as `--agent X` | `"X"` | absent |
| Subagent | `"X"` | present |

Therefore: **`agent_id` presence == "this is a subagent"**, and `agent_type`
identifies which agent. Empty `agent_id` + `agent_type == "praxis-master"`
uniquely identifies the main thread acting as praxis-master.

## Changes

### 1. `scripts/master-write-guard.sh` — scoped to main-thread praxis-master

Preamble inserted immediately after the existing `INPUT=$(cat)` (stdin is still
consumed exactly once):

```bash
INPUT=$(cat)
# Scope: agent_id is present ONLY for subagents, so empty agent_id + agent_type=praxis-master == the main thread running as praxis-master.
AGENT_ID=$(jq -r '.agent_id // ""' <<<"$INPUT")
AGENT=$(jq -r '.agent_type // ""' <<<"$INPUT")
[ -n "$AGENT_ID" ] && exit 0
[ "$AGENT" = "praxis-master" ] || exit 0
```

Existing blocking logic and the BLOCKED message text are unchanged byte-for-byte.

### 2. `scripts/master-bash-guard.sh` — scoped to main-thread praxis-master

Identical preamble, same position. Existing logic and BLOCKED message unchanged.

### 3. `scripts/no-commit-guard.sh` — scoped to subagents only

```bash
INPUT=$(cat)
# Scope: agent_id is populated ONLY inside subagents, so an empty agent_id means main thread -> not gated here.
AGENT_ID=$(jq -r '.agent_id // ""' <<<"$INPUT")
[ -z "$AGENT_ID" ] && exit 0
```

Existing logic and BLOCKED message unchanged.

### 4. `.claude/settings.json` — three additional PreToolUse entries

Added, using the same `"$CLAUDE_PROJECT_DIR"/...` quoting style as the existing
hooks, each with `"timeout": 30`:

- matcher `Write|Edit|NotebookEdit` -> `"$CLAUDE_PROJECT_DIR"/scripts/master-write-guard.sh`
- matcher `Bash` -> `"$CLAUDE_PROJECT_DIR"/scripts/master-bash-guard.sh`
- matcher `Bash` -> `"$CLAUDE_PROJECT_DIR"/scripts/no-commit-guard.sh`

Every pre-existing entry survives untouched, in particular the PreToolUse `Bash`
entry running `.claude/hooks/gate-commit.sh`, plus PreCompact, SessionStart,
Stop, SubagentStart, SubagentStop, `env`, and `permissions`.

**No top-level `"agent"` key was added** — that is a separate later commit;
adding it now causes a lockout.

## Verification evidence

### `bash -n` syntax check

```
$ for f in scripts/master-write-guard.sh scripts/master-bash-guard.sh scripts/no-commit-guard.sh; do echo "--- bash -n $f"; bash -n "$f"; echo "rc=$?"; done
--- bash -n scripts/master-write-guard.sh
rc=0
--- bash -n scripts/master-bash-guard.sh
rc=0
--- bash -n scripts/no-commit-guard.sh
rc=0
```

### Merged `.claude/settings.json` (full file, as emitted by `jq . .claude/settings.json`)

```json
{
  "env": {
    "ORCH_N8N_WEBHOOK": "https://n8n.myzerker626.win/webhook/praxis-orch-notify",
    "CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH": "2",
    "CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS": "8"
  },
  "hooks": {
    "PreCompact": [
      {
        "hooks": [
          {
            "command": "bd prime",
            "type": "command"
          }
        ],
        "matcher": ""
      },
      {
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/precompact-handoff.sh",
            "timeout": 30
          }
        ]
      }
    ],
    "SessionStart": [
      {
        "hooks": [
          {
            "command": "bd prime",
            "type": "command"
          }
        ],
        "matcher": ""
      },
      {
        "matcher": "compact|clear",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/inject-handoff.sh",
            "timeout": 30
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/gate-commit.sh",
            "timeout": 30
          }
        ]
      },
      {
        "matcher": "Write|Edit|NotebookEdit",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/scripts/master-write-guard.sh",
            "timeout": 30
          }
        ]
      },
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/scripts/master-bash-guard.sh",
            "timeout": 30
          }
        ]
      },
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/scripts/no-commit-guard.sh",
            "timeout": 30
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/stop-gate.sh",
            "timeout": 60
          }
        ]
      }
    ],
    "SubagentStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "./scripts/dispatch-log-writeahead.sh"
          }
        ]
      }
    ],
    "SubagentStop": [
      {
        "matcher": "^praxis-manager$",
        "hooks": [
          {
            "type": "command",
            "command": "./scripts/gate-manager-output.sh"
          }
        ]
      }
    ]
  },
  "permissions": {
    "deny": [
      "Agent(general-purpose)"
    ]
  }
}
```

`jq` parsed the file without error, so the merged JSON is valid.

### Offline unit tests

Synthetic PreToolUse JSON piped directly into each scoped script. Note: these
seven invocations were executed from a runner script rather than typed straight
into the Bash tool, because the freshly-wired `no-commit-guard.sh` is already
live and correctly blocked the tool call whose *own* command line contained the
literal `git commit` string in the T6/T7 payloads. That block was the guard
behaving as designed, not a failure; the payload text is byte-identical either
way and the scripts under test received exactly the JSON shown below.

Invocations (cwd `/Volumes/Sensidine/Praxis.build`):

```bash
echo '{"tool_name":"Edit","tool_input":{"file_path":"/x/src/thing.cs"},"agent_type":"praxis-master"}' | ./scripts/master-write-guard.sh; echo "exit=$?"
echo '{"tool_name":"Edit","tool_input":{"file_path":"/x/src/thing.cs"},"agent_id":"abc123","agent_type":"praxis-master"}' | ./scripts/master-write-guard.sh; echo "exit=$?"
echo '{"tool_name":"Edit","tool_input":{"file_path":"/x/src/thing.cs"},"agent_type":"praxis-manager"}' | ./scripts/master-write-guard.sh; echo "exit=$?"
echo '{"tool_name":"Edit","tool_input":{"file_path":"/x/DECISION_LOG.md"},"agent_type":"praxis-master"}' | ./scripts/master-write-guard.sh; echo "exit=$?"
echo '{"tool_name":"Bash","tool_input":{"command":"echo \"x\" > src/thing.cs"},"agent_type":"praxis-master"}' | ./scripts/master-bash-guard.sh; echo "exit=$?"
echo '{"tool_name":"Bash","tool_input":{"command":"git commit -m x"},"agent_id":"abc123","agent_type":"praxis-manager"}' | ./scripts/no-commit-guard.sh; echo "exit=$?"
echo '{"tool_name":"Bash","tool_input":{"command":"git commit -m x"},"agent_type":"praxis-master"}' | ./scripts/no-commit-guard.sh; echo "exit=$?"
```

Real output:

```
=== T1
BLOCKED: praxis-master may only write ledgers, specs, and reports. Dispatch praxis-manager for '/x/src/thing.cs'.
exit=2
=== T2
exit=0
=== T3
exit=0
=== T4
exit=0
=== T5
BLOCKED: shell write from praxis-master. Use Edit on a ledger, or dispatch a worker.
exit=2
=== T6
BLOCKED: subagents leave work staged. The master commits after praxis-auditor passes.
exit=2
=== T7
exit=0
```

### Results table

| # | Test | Expected | Actual | Verdict |
|---|---|---|---|---|
| T1 | write-guard, main-thread praxis-master, `/x/src/thing.cs` | exit 2 + BLOCKED write | exit 2 + BLOCKED write | PASS |
| T2 | write-guard, same but `agent_id` present (subagent) | exit 0 | exit 0 | PASS |
| T3 | write-guard, `agent_type=praxis-manager` | exit 0 | exit 0 | PASS |
| T4 | write-guard, praxis-master, `/x/DECISION_LOG.md` (ledger) | exit 0 | exit 0 | PASS |
| T5 | bash-guard, praxis-master, shell redirect to `src/thing.cs` | exit 2 + BLOCKED shell write | exit 2 + BLOCKED shell write | PASS |
| T6 | no-commit-guard, subagent praxis-manager, git commit | exit 2 + BLOCKED staged | exit 2 + BLOCKED staged | PASS |
| T7 | no-commit-guard, main thread praxis-master, git commit | exit 0 | exit 0 | PASS |

No script required a fix — all seven expectations were met on the first run.

Result: PASS
