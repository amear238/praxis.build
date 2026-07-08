#!/bin/bash
# Stop hook: in autonomous mode, block session end while unblocked beads remain.
# The iteration cap (max-iterations, default 25) is the runaway brake — it, not
# stop_hook_active, prevents infinite loops, because our block condition shrinks
# as beads close.
set -uo pipefail
INPUT=$(cat)
ROOT="${CLAUDE_PROJECT_DIR:-.}"
STATE="$ROOT/.claude/state"
[ -f "$STATE/orchestrator-active" ] || exit 0
[ "$(cat "$STATE/run-mode" 2>/dev/null || true)" = "autonomous" ] || exit 0

COUNT=$(cat "$STATE/iteration-count" 2>/dev/null || echo 0)
MAX=$(cat "$STATE/max-iterations" 2>/dev/null || echo 25)
case "$COUNT" in (*[!0-9]*|"") COUNT=0 ;; esac
case "$MAX"   in (*[!0-9]*|"") MAX=25  ;; esac

if [ "$COUNT" -ge "$MAX" ]; then
  "$ROOT/.claude/hooks/notify.sh" "max-iterations" "autonomous loop brake hit at $COUNT iterations" >/dev/null 2>&1 || true
  exit 0
fi

command -v bd >/dev/null 2>&1 || exit 0
READY=$(cd "$ROOT" && bd ready --json 2>/dev/null | python3 -c '
import json, sys
try:
    print(len(json.load(sys.stdin)))
except Exception:
    print(0)
' 2>/dev/null || echo 0)

if [ "$READY" -gt 0 ] 2>/dev/null; then
  echo $((COUNT + 1)) > "$STATE/iteration-count"
  printf '{"decision":"block","reason":"Autonomous run incomplete: %s unblocked task(s) in bd ready (iteration %s/%s). Continue the dispatch->audit->commit loop on the next bd ready item. Consult RUN_DECISIONS.md before considering any question for the user."}\n' \
    "$READY" "$((COUNT + 1))" "$MAX"
fi
exit 0
