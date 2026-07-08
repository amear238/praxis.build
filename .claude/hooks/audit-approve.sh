#!/bin/bash
# Mints a single-use audit token keyed to the CURRENT staged diff.
# ONLY the orchestrator-auditor agent may run this, and only on VERDICT: PASS.
set -uo pipefail
BEAD="${1:-}"
if [ -z "$BEAD" ]; then
  echo "usage: audit-approve.sh <bead-or-task-id>" >&2
  exit 1
fi
ROOT="${CLAUDE_PROJECT_DIR:-$(git rev-parse --show-toplevel)}"
STATE="$ROOT/.claude/state"
mkdir -p "$STATE"
# Refuse to mint on an empty staged diff. `git diff --cached --quiet` exits 0 when
# nothing is staged; this also guards against silently hashing empty input if the
# diff command itself fails.
(cd "$ROOT" && git diff --cached --quiet) && { echo "refusing to mint: staged diff is empty" >&2; exit 1; }
HASH=$(cd "$ROOT" && git diff --cached | shasum -a 256 | awk '{print $1}')
touch "$STATE/audit-pass-$HASH"
printf '%s %s %s PASS\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$BEAD" "$HASH" >> "$ROOT/AUDIT_LOG.md"
echo "audit token minted for $BEAD ($HASH)"
