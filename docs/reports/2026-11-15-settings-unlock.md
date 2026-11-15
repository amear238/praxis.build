# 2026-11-15 settings unlock

Result: PASS

## Task
Archive the working-tree `.claude/settings.json`, then remove the top-level `agent` line and every hook entry except the two `bd prime` entries, keeping `env` and `permissions` as they are. Authority: DECISION_LOG row 2026-11-15T19:16:18Z, WHO: amear, his words "Yes, remove the locks" (read in DECISION_LOG.md line 1031 this session). Settings file only; no agent file or script moved.

## What was done
- Done by the manager directly, as the master's brief allowed. No worker dispatched.
- Removed: `"agent": "praxis-master"`; `precompact-handoff.sh` (PreCompact); `inject-handoff.sh` (SessionStart); all of `PreToolUse`, `PostToolUse`, `Stop`, `SubagentStart`, `SubagentStop`.
- Kept as they were: `env`, `permissions` (deny `Agent(general-purpose)`), both `bd prime` entries.
- No hook blocked any step. Nothing staged; no git write command run.

## Files touched
- `.claude/settings.json` (edited, unstaged)
- `archive/2026-11-15/settings.json.working-tree-before-unlock` (new, untracked)
- `docs/reports/2026-11-15-settings-unlock.md` (this report, untracked)

## Verification evidence (command output)

Step 1:

```
$ mkdir -p archive/2026-11-15 && cp -p .claude/settings.json archive/2026-11-15/settings.json.working-tree-before-unlock && openssl dgst -sha256 .claude/settings.json archive/2026-11-15/settings.json.working-tree-before-unlock
SHA2-256(.claude/settings.json)= 98ac1ec8802cd6c02a04d8f24382c72a53162bfac41ca41ccff13bf199d92115
SHA2-256(archive/2026-11-15/settings.json.working-tree-before-unlock)= 98ac1ec8802cd6c02a04d8f24382c72a53162bfac41ca41ccff13bf199d92115
```

Step 3 (run from the repo root; `A=archive/2026-11-15/settings.json.working-tree-before-unlock`, `S=.claude/settings.json`):

```
$ jq . $S >/dev/null && echo PARSE_OK
PARSE_OK
$ jq -r '.agent // "absent"' $S
absent
$ jq -r '.agent // "absent"' $A
praxis-master
$ jq '.hooks | keys' $S
[
  "PreCompact",
  "SessionStart"
]
$ jq '[.hooks[][] | .hooks[] | .command]' $S
[
  "bd prime",
  "bd prime"
]
$ diff <(jq '.hooks.PreCompact[0]' $A) <(jq '.hooks.PreCompact[0]' $S) && echo SAME
SAME
$ diff <(jq '.hooks.SessionStart[0]' $A) <(jq '.hooks.SessionStart[0]' $S) && echo SAME
SAME
$ jq .env $S
{
  "ORCH_N8N_WEBHOOK": "https://n8n.myzerker626.win/webhook/praxis-orch-notify",
  "CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH": "2",
  "CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS": "8"
}
$ jq .env $A
{
  "ORCH_N8N_WEBHOOK": "https://n8n.myzerker626.win/webhook/praxis-orch-notify",
  "CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH": "2",
  "CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS": "8"
}
$ diff <(jq .env $A) <(jq .env $S) && echo ENV_SAME
ENV_SAME
$ jq .permissions $S
{
  "deny": [
    "Agent(general-purpose)"
  ]
}
$ jq .permissions $A
{
  "deny": [
    "Agent(general-purpose)"
  ]
}
$ diff <(jq .permissions $A) <(jq .permissions $S) && echo PERM_SAME
PERM_SAME
$ jq -c keys $S
["env","hooks","permissions"]
$ openssl dgst -sha256 archive/2026-11-15/settings.json.working-tree-before-unlock .claude/settings.json
SHA2-256(archive/2026-11-15/settings.json.working-tree-before-unlock)= 98ac1ec8802cd6c02a04d8f24382c72a53162bfac41ca41ccff13bf199d92115
SHA2-256(.claude/settings.json)= b843d66ce5bf22d0486b768e6a848ca44574b2bfd87748f17395899632ef787a
```

The last check shows the archive copy still matches the pre-edit hash after the edit.

Final full text of `.claude/settings.json`:

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

## Notes
- The running session loaded hooks when it started. Removing them from the file may not take effect until a new session starts. Not tested here.
- MANIFEST.md not updated, because the brief limited edits to these three files. The master should add rows for the archive copy and this report.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
