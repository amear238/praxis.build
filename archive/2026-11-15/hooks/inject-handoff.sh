#!/bin/bash
# SessionStart hook (matcher: compact|clear): re-inject the PreCompact snapshot.
set -uo pipefail
INPUT=$(cat)
ROOT="${CLAUDE_PROJECT_DIR:-.}"
[ -f "$ROOT/.claude/state/orchestrator-active" ] || exit 0
HF="$ROOT/.claude/state/handoff-latest.md"
[ -f "$HF" ] || exit 0
SRC=$(printf '%s' "$INPUT" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("source",""))' 2>/dev/null || true)
case "$SRC" in
  compact|clear) ;;
  *) exit 0 ;;
esac
NOW=$(date +%s)
MT=$(stat -f %m "$HF")
[ $((NOW - MT)) -le 86400 ] || exit 0
python3 -c '
import json, sys
print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": open(sys.argv[1]).read()}}))
' "$HF"
exit 0
