#!/bin/bash
# progress-data.sh — deterministic snapshot feeding the /progress report.
# Read-only: no repo state is modified. Safe in headless/scheduled runs.
set -uo pipefail

REPO="${PRAXIS_REPO:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)}"
cd "$REPO" 2>/dev/null || { echo "ERROR: cannot cd to repo ($REPO)"; exit 1; }

section() { printf '\n=== %s ===\n' "$1"; }

section "STATUS.md — header / current phase / current step"
awk 'NR<=20' STATUS.md 2>/dev/null || echo "(STATUS.md missing)"

section "STATUS.md — Phase Progress"
awk '/^## Phase Progress/{f=1} f' STATUS.md 2>/dev/null || echo "(no Phase Progress section)"

section "beads — in_progress"
bd list --status=in_progress 2>/dev/null || echo "(bd unavailable)"

section "beads — open"
bd list --status=open 2>/dev/null || echo "(bd unavailable)"

section "beads — recently closed"
bd list --status=closed 2>/dev/null | head -30 || echo "(bd unavailable)"

section "AUDIT_LOG.md — last entries"
tail -25 AUDIT_LOG.md 2>/dev/null || echo "(AUDIT_LOG.md missing)"

section "git — recent commits"
git log --oneline -10 2>/dev/null || echo "(git unavailable)"
