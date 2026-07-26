#!/bin/bash
# Restricts the master agent's Edit/Write to ledgers, handoff, specs, and reports.
# The master coordinates; it does not build. This is structural, not advisory.
INPUT=$(cat)
# Scope: agent_id is present ONLY for subagents, so empty agent_id + agent_type=praxis-master == the main thread running as praxis-master.
AGENT_ID=$(jq -r '.agent_id // ""' <<<"$INPUT")
AGENT=$(jq -r '.agent_type // ""' <<<"$INPUT")
[ -n "$AGENT_ID" ] && exit 0
[ "$AGENT" = "praxis-master" ] || exit 0
FILE=$(echo "$INPUT" | jq -r '.tool_input.file_path // .tool_input.path // empty')
[ -z "$FILE" ] && exit 0

case "$FILE" in
  *DISPATCH_LOG.md|*DECISION_LOG.md|*ISSUE_REGISTER.md|*HANDOFF.md|*STATUS.md) exit 0 ;;
  */specs/*|*/docs/reports/*) exit 0 ;;
esac

echo "BLOCKED: praxis-master may only write ledgers, specs, and reports. Dispatch praxis-manager for '$FILE'." >&2
exit 2
