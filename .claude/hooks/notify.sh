#!/bin/bash
# Fire-and-forget notification to n8n (-> Telegram). Never fails the caller.
# Usage: notify.sh <event> [detail...]   Env: ORCH_N8N_WEBHOOK, ORCH_NOTIFY_DRYRUN=1
set -uo pipefail
EVENT="${1:-unknown}"
shift 2>/dev/null || true
DETAIL="${*:-}"
PROJECT=$(basename "${CLAUDE_PROJECT_DIR:-$PWD}")
PAYLOAD=$(python3 -c '
import json, sys
print(json.dumps({"event": sys.argv[1], "project": sys.argv[2], "detail": sys.argv[3]}))
' "$EVENT" "$PROJECT" "$DETAIL" 2>/dev/null) || exit 0
if [ "${ORCH_NOTIFY_DRYRUN:-0}" = "1" ]; then
  echo "$PAYLOAD"
  exit 0
fi
[ -n "${ORCH_N8N_WEBHOOK:-}" ] || exit 0
curl -s -m 10 -X POST "$ORCH_N8N_WEBHOOK" -H 'Content-Type: application/json' -d "$PAYLOAD" >/dev/null 2>&1 || true
exit 0
