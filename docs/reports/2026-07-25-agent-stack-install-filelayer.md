# Agent Stack — File Layer Install

Date: 2026-07-25
Source: `/Users/admin/Downloads/files (1)/` (flat)
Scope: file layer only. Everything staged (`git add`); **nothing committed**.

## What was done

1. Created directories: `.claude/agents`, `scripts`, `specs`, `docs/reports` (`mkdir -p`; only `specs/` did not previously exist).
2. Copied 3 agent definitions → `.claude/agents/`: `praxis-master.md`, `praxis-manager.md`, `praxis-auditor.md`. No name collision with the pre-existing `orchestrator-auditor.md` / `praxis-tutor.md`.
3. Copied 5 hook scripts → `scripts/`: `dispatch-log-writeahead.sh`, `gate-manager-output.sh`, `master-bash-guard.sh`, `master-write-guard.sh`, `no-commit-guard.sh`. Each `chmod +x`'d and syntax-checked with `bash -n` — all 5 silent (pass). No name collision with existing scripts.
4. Copied `SPEC_RUBRIC.md` → `specs/SPEC_RUBRIC.md` byte-identical. Contents not edited. Verified by both `shasum -a 256` (matching digests) and `diff` (no output).
5. Ledger files — **all four already existed; none were touched or overwritten**:

   | File | State |
   |---|---|
   | `DISPATCH_LOG.md` | pre-existing (2715 B, May 11) — untouched |
   | `DECISION_LOG.md` | pre-existing (43015 B, Jul 25) — untouched |
   | `ISSUE_REGISTER.md` | pre-existing (6257 B, Jul 25) — untouched |
   | `HANDOFF.md` | pre-existing (65813 B, Jul 25) — untouched |

   Zero files created in this step.
6. Merged `settings.json` into `.claude/settings.json` — additive only.

## Settings merge

**No key collided.** Every added path was absent from the existing file:

- `env.CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` — absent → added `"2"`
- `env.CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` — absent → added `"8"`
- `hooks.SubagentStart` — absent → added, command `./scripts/dispatch-log-writeahead.sh`
- `hooks.SubagentStop` — absent → added, matcher `^praxis-manager$`, command `./scripts/gate-manager-output.sh`
- `permissions` — the entire top-level key was absent → added with `deny: ["Agent(general-purpose)"]`

Preserved untouched: `env.ORCH_N8N_WEBHOOK`, and all four existing hook events (`PreCompact`, `SessionStart`, `PreToolUse`, `Stop`) with their commands, matchers and timeouts.

Deliberately **NOT** done, per instruction:

- Top-level `"agent": "praxis-master"` was **not** added (it is present in the source file; it is installed later in its own commit — adding it now would lock the session out).
- `master-write-guard.sh`, `master-bash-guard.sh`, `no-commit-guard.sh` are copied and executable but **not wired** into any `PreToolUse` entry — a separate dispatch handles their scoping.

Additive-only was proven mechanically: stripping the five added paths from the merged file and diffing (sorted) against the pre-merge backup produced no differences.

## Verification evidence

### `ls -l .claude/agents/ scripts/*.sh specs/`

```
total 64
-rw-r--r--@ 1 admin  staff  4137 Jul 10 12:35 orchestrator-auditor.md
-rw-------@ 1 admin  staff  1986 Jul 25 16:40 praxis-auditor.md
-rw-------@ 1 admin  staff  3488 Jul 25 16:40 praxis-manager.md
-rw-------@ 1 admin  staff  4130 Jul 25 16:40 praxis-master.md
-rw-r--r--@ 1 admin  staff  7033 Jul 24 12:55 praxis-tutor.md

-rwxr-xr-x@ 1 admin  staff   2707 Jul 10 12:33 scripts/audit-log-annotate.sh
-rwxr-xr-x@ 1 admin  staff   7361 Jul 10 12:34 scripts/audit-log-flush-verify.sh
-rwx--x--x@ 1 admin  staff    619 Jul 25 16:40 scripts/dispatch-log-writeahead.sh
-rwx--x--x@ 1 admin  staff   1067 Jul 25 16:40 scripts/gate-manager-output.sh
-rwx--x--x@ 1 admin  staff    546 Jul 25 16:40 scripts/master-bash-guard.sh
-rwx--x--x@ 1 admin  staff    569 Jul 25 16:40 scripts/master-write-guard.sh
-rwx--x--x@ 1 admin  staff    355 Jul 25 16:40 scripts/no-commit-guard.sh
-rwxr-xr-x@ 1 admin  staff   6614 Jul 20 11:51 scripts/praxis-b2data-watch-install.sh
-rwxr-xr-x@ 1 admin  staff   7499 Jul 21 15:26 scripts/praxis-b2data-watch.sh
-rw-r--r--@ 1 admin  staff   3997 Jul 15 15:57 scripts/praxis-inbound-control-install.sh
-rw-r--r--@ 1 admin  staff  11059 Jul 15 15:58 scripts/praxis-inbound-control-watch.sh
-rw-r--r--@ 1 admin  staff   5742 Jul 10 10:45 scripts/praxis-signals-backlog-check.sh
-rwxr-xr-x@ 1 admin  staff   5270 Jul 12 10:26 scripts/praxis-signals-install.sh
-rwxr-xr-x@ 1 admin  staff   2999 Jul 10 09:25 scripts/praxis-signals-stale-check.sh
-rw-r--r--@ 1 admin  staff   2095 Jul 12 10:24 scripts/praxis-signals-sweep-daemon.sh
-rwxr-xr-x@ 1 admin  staff   1828 Jul  9 13:40 scripts/praxis-signals-sweep.sh
-rwxr-xr-x@ 1 admin  staff   8664 Jul 12 09:46 scripts/test-gate-hardening.sh

total 16
-rw-------@ 1 admin  staff  6469 Jul 25 16:40 SPEC_RUBRIC.md
```

Note: the copied files inherit the source's restrictive mode (`600` → `711` for the scripts after `chmod +x`). The executable bit is set on all five scripts as required. Modes were not otherwise normalized, as that was outside the instructed scope.

### `bash -n` on each hook script (silence = pass)

```
scripts/dispatch-log-writeahead.sh: (silent = pass)
scripts/gate-manager-output.sh: (silent = pass)
scripts/master-bash-guard.sh: (silent = pass)
scripts/master-write-guard.sh: (silent = pass)
scripts/no-commit-guard.sh: (silent = pass)
```

All five produced no output. 5/5 pass.

### SPEC_RUBRIC.md byte-identity

```
$ shasum -a 256 "/Users/admin/Downloads/files (1)/SPEC_RUBRIC.md" specs/SPEC_RUBRIC.md
10a0d8d2b55b4e567cf0ee4cfcd77e5fde4a5523f8ce13c6e99280137f5bc324  /Users/admin/Downloads/files (1)/SPEC_RUBRIC.md
10a0d8d2b55b4e567cf0ee4cfcd77e5fde4a5523f8ce13c6e99280137f5bc324  specs/SPEC_RUBRIC.md

$ diff "/Users/admin/Downloads/files (1)/SPEC_RUBRIC.md" specs/SPEC_RUBRIC.md
diff: identical (no output)
```

Digests match; `diff` empty. Copy is byte-identical.

### `jq . .claude/settings.json` (full merged file, validates clean)

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

Guard checks:

```
$ jq '.agent' .claude/settings.json
null                                    # top-level "agent" key correctly ABSENT

$ jq -r '.env.ORCH_N8N_WEBHOOK' .claude/settings.json
https://n8n.myzerker626.win/webhook/praxis-orch-notify    # survived untouched

$ jq 'del(<the 5 added paths>)' merged | diff - pre-merge-backup
IDENTICAL — merge was purely additive
```

### `git status --short`

```
A  .claude/agents/praxis-auditor.md
A  .claude/agents/praxis-manager.md
A  .claude/agents/praxis-master.md
M  .claude/settings.json
 M AUDIT_LOG.md
M  ISSUE_REGISTER.md
A  docs/reports/2026-07-25-agent-stack-install-filelayer.md
A  docs/reports/2026-07-25-agent-stack-install.md
A  scripts/dispatch-log-writeahead.sh
A  scripts/gate-manager-output.sh
A  scripts/master-bash-guard.sh
A  scripts/master-write-guard.sh
A  scripts/no-commit-guard.sh
A  specs/SPEC_RUBRIC.md
```

`AUDIT_LOG.md`, `ISSUE_REGISTER.md` and `docs/reports/2026-07-25-agent-stack-install.md` were already modified/staged before this dispatch began and are **not** this dispatch's work; they were left exactly as found. Everything this dispatch created or modified is staged. No `git commit`, `git push`, or `git stash` was run.

Result: PASS
