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
# Bind the token to the exact staged TREE (bead v6y): gate-commit.sh recomputes
# `git write-tree` at commit time and denies on mismatch, so anything staged in
# the mint→commit gap (2026-07-10 parallel-session incident) forces a re-audit.
TREE=$(cd "$ROOT" && git write-tree)
if [ -z "$TREE" ]; then
  echo "refusing to mint: git write-tree failed (unmerged index?)" >&2
  exit 1
fi
printf 'tree=%s\n' "$TREE" > "$STATE/audit-pass-$HASH"
printf '%s %s %s PASS\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$BEAD" "$HASH" >> "$ROOT/AUDIT_LOG.md"
echo "audit token minted for $BEAD ($HASH)"
