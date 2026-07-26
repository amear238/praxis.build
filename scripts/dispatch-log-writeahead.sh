#!/bin/bash
# SubagentStart hook: writes the DISPATCH_LOG row mechanically.
# Write-ahead discipline stops depending on the agent remembering.
INPUT=$(cat)
AGENT=$(echo "$INPUT" | jq -r '.agent_type // "unknown"')
TS=$(date -u +%Y-%m-%dT%H:%M:%SZ)
LOG="${CLAUDE_PROJECT_DIR:-.}/DISPATCH_LOG.md"
[ -f "$LOG" ] || echo "# DISPATCH LOG" > "$LOG"
echo "- [$TS] WHO: $AGENT | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session $(git -C "${CLAUDE_PROJECT_DIR:-.}" rev-parse --short HEAD 2>/dev/null || echo no-git) | WHEN: spawn | HOW: awaiting terminal state | STATE: dispatched" >> "$LOG"
exit 0
