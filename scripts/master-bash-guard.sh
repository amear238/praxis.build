#!/bin/bash
# Blocks the master from using shell redirection to bypass the write guard.
INPUT=$(cat)
# Scope: agent_id is present ONLY for subagents, so empty agent_id + agent_type=praxis-master == the main thread running as praxis-master.
AGENT_ID=$(jq -r '.agent_id // ""' <<<"$INPUT")
AGENT=$(jq -r '.agent_type // ""' <<<"$INPUT")
[ -n "$AGENT_ID" ] && exit 0
[ "$AGENT" = "praxis-master" ] || exit 0
CMD=$(echo "$INPUT" | jq -r '.tool_input.command // empty')
[ -z "$CMD" ] && exit 0

if echo "$CMD" | grep -qE '(^|[^>])>{1,2}[[:space:]]*[^&]|(^|\s)(sed|tee|patch|dd)\s+.*-i|\bcat\s*<<'; then
  case "$CMD" in
    *DISPATCH_LOG.md*|*DECISION_LOG.md*|*ISSUE_REGISTER.md*|*HANDOFF.md*|*/specs/*|*/docs/reports/*) exit 0 ;;
  esac
  echo "BLOCKED: shell write from praxis-master. Use Edit on a ledger, or dispatch a worker." >&2
  exit 2
fi
exit 0
