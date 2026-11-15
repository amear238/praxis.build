#!/bin/bash
# audit-log-annotate.sh — the ONLY sanctioned writer of AUDIT_LOG.md besides
# audit-approve.sh (bead 30h; standing rule: AUDIT_LOG.md is never edited by
# hand). APPENDS — never edits, never deletes — exactly one annotation line:
#
#   <utc-ts> ANNOTATION VOID <row-hash-prefix> <reason...>
#
# marking an existing PASS row as void (e.g. minted against wrong staged
# content, 2026-07-10 concurrency incident). audit-log-flush-verify.sh treats
# a VOID-annotated row as accounted-for without a landed commit. The reason
# MUST cite the DECISION_LOG entry that declared the row void.
#
# Usage: bash scripts/audit-log-annotate.sh VOID <row-hash-prefix(8-64 hex)> <reason...>
set -uo pipefail

die() { echo "annotate REFUSED: $1" >&2; exit 1; }

ROOT="${CLAUDE_PROJECT_DIR:-$(git rev-parse --show-toplevel 2>/dev/null)}"
[ -n "$ROOT" ] || die "cannot resolve repo root"
LOG="$ROOT/AUDIT_LOG.md"
[ -f "$LOG" ] || die "$LOG not found"

[ "$#" -ge 3 ] || die "usage: audit-log-annotate.sh VOID <row-hash-prefix> <reason...>"
VERB="$1"; PREFIX="$2"; shift 2
REASON="$*"

# append-only guard rails: one verb, one line, nothing that can impersonate a
# PASS row or an audit token hash
[ "$VERB" = "VOID" ] || die "only the VOID verb is sanctioned (got '$VERB') — a new verb needs its own bead + auditor sign-off"
printf '%s' "$PREFIX" | grep -Eq '^[0-9a-f]{8,64}$' || die "row-hash-prefix must be 8-64 lowercase hex chars (got '$PREFIX')"
[ -n "$REASON" ] || die "a reason is required — cite the DECISION_LOG row that voids the mint"
case "$REASON" in
  *$'\n'* | *$'\r'*) die "reason must be a single line — an embedded newline could forge additional log rows" ;;
esac
printf '%s' "$REASON" | LC_ALL=C grep -q '[^ -~]' && die "reason must be printable ASCII (no control chars)"
printf '%s' "$REASON" | grep -Eq '[0-9a-f]{64}' && die "reason may not embed a full 64-hex digest — it could collide with token/PASS-row matching"

# the prefix must resolve to exactly ONE existing PASS row
MATCHES=$(awk -v p="$PREFIX" '$4 == "PASS" && index($3, p) == 1 { print $3 }' "$LOG")
COUNT=$(printf '%s' "$MATCHES" | grep -c .)
[ "$COUNT" = "1" ] || die "row-hash-prefix must match exactly ONE PASS row in AUDIT_LOG.md (matched $COUNT)"
HASH="$MATCHES"

# append-only means no second opinion: refuse to annotate the same row twice
if awk -v h="$HASH" '$2 == "ANNOTATION" && $3 == "VOID" && index(h, $4) == 1 { found = 1 } END { exit found ? 0 : 1 }' "$LOG"; then
  die "row ${HASH:0:12}... already carries a VOID annotation (append-only — no re-edits, no retractions)"
fi

LINE="$(date -u +%Y-%m-%dT%H:%M:%SZ) ANNOTATION VOID $PREFIX $REASON"
printf '%s\n' "$LINE" >> "$LOG"
echo "appended: $LINE"
