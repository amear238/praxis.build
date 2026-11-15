#!/bin/bash
# PreCompact hook: snapshot orchestrator state so compaction loses nothing.
set -uo pipefail
INPUT=$(cat) || true
ROOT="${CLAUDE_PROJECT_DIR:-.}"
STATE="$ROOT/.claude/state"
[ -f "$STATE/orchestrator-active" ] || exit 0
mkdir -p "$STATE"
{
  echo "# Orchestrator handoff — $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "## run-mode"
  cat "$STATE/run-mode" 2>/dev/null || echo "interactive"
  echo "## current bead"
  cat "$STATE/current-bead" 2>/dev/null || echo "(none recorded)"
  echo "## bd ready"
  (cd "$ROOT" && bd ready 2>/dev/null) || echo "(bd unavailable — check DISPATCH_LOG.md fallback)"
  echo "## last 3 decisions"
  grep '^- \[' "$ROOT/DECISION_LOG.md" 2>/dev/null | tail -3 || true
  echo "## resume instruction"
  echo "You are mid-orchestrator-run. Re-read RUN_DECISIONS.md (if autonomous) and HANDOFF.md, then continue the dispatch->audit->commit loop from the bd ready queue above."
} > "$STATE/handoff-latest.md"
exit 0
