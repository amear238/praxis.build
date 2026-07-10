#!/bin/bash
# Machine verification for AUDIT_LOG "flush" commits (bead 30h).
#
# Why: audit-approve.sh appends its PASS row AFTER hashing + tree-binding the
# staged diff, so no commit can ever contain its own audit row — rows strand
# uncommitted in the working tree. The sanctioned fix (RUN_DECISIONS option a)
# is a dedicated flush commit that stages ONLY AUDIT_LOG.md; the auditor runs
# THIS script in FLUSH-MODE to prove every ADDED line maps to reality before
# minting. One row (the flush's own mint) always postdates the staged snapshot
# and rolls forward into the NEXT flush — accepted, perpetual.
#
# Checks:
#   * staged set is exactly AUDIT_LOG.md
#   * the staged AUDIT_LOG diff is append-only (no removed/edited lines)
#   * every added line classifies as exactly ONE of (first match wins):
#       VOID-ANNOTATED  a later "ANNOTATION VOID <hash-prefix>" line covers the
#                       row (written by audit-log-annotate.sh, citing a
#                       DECISION_LOG entry)
#       SUPERSEDED      same bead has a LATER PASS row (re-mint after FAIL or
#                       scope change; the earlier mint was never consumed)
#       LANDED          a commit citing the row's bead id — for session-wrap
#                       rows, any commit whose message contains "wrap" — is
#                       authored at/after the mint timestamp
#       LANDED-WRAP     no commit cites the bead, but the FIRST commit authored
#                       after the mint is a session-wrap commit inside the
#                       30-min token TTL: the wrap consumed a token minted
#                       under the bead it was closing (observed: 3i7 mint
#                       2026-07-09T15:40:27Z -> session-2 wrap 15:40:41Z)
#       ANNOTATION      the added line is itself an annotation line and
#                       references a PASS row that exists in the staged file
#   * any unclassifiable line is listed and the script exits 1
#
# Usage: bash scripts/audit-log-flush-verify.sh [repo-root]
# Exit 0 only if every added line classifies. Prints a per-row table.
set -uo pipefail

die() { echo "FLUSH-VERIFY FAIL: $1" >&2; exit 1; }

ROOT="${1:-$(git rev-parse --show-toplevel 2>/dev/null)}"
[ -n "$ROOT" ] && [ -d "$ROOT" ] || die "cannot resolve repo root (pass it as \$1 or run inside the repo)"
cd "$ROOT" || die "cannot cd to $ROOT"
git rev-parse --git-dir >/dev/null 2>&1 || die "$ROOT is not a git repo"

# --- flush shape: exactly AUDIT_LOG.md staged, append-only ---
STAGED_SET=$(git diff --cached --name-only)
[ -n "$STAGED_SET" ] || die "nothing is staged — stage AUDIT_LOG.md alone, then re-run"
[ "$STAGED_SET" = "AUDIT_LOG.md" ] || die "flush staged set must be EXACTLY AUDIT_LOG.md; got: $(printf '%s' "$STAGED_SET" | tr '\n' ' ')"
REMOVED=$(git diff --cached -- AUDIT_LOG.md | grep -cE '^-([^-]|$)')
[ "$REMOVED" = "0" ] || die "flush must be append-only — staged diff removes/edits $REMOVED existing line(s)"
ADDED=$(git diff --cached -- AUDIT_LOG.md | grep -E '^\+([^+]|$)' | cut -c2-)
[ -n "$ADDED" ] || die "staged AUDIT_LOG.md diff adds no lines — nothing to flush"

STAGED_LOG=$(git show :AUDIT_LOG.md)
TOKEN_TTL=1800   # audit tokens die at 30 min; a consuming commit cannot be later

ep() { date -j -u -f '%Y-%m-%dT%H:%M:%SZ' "$1" +%s 2>/dev/null; }
iso() { date -j -u -r "$1" +%Y-%m-%dT%H:%M:%SZ 2>/dev/null; }

N=0
UNCLASS=0
UNLIST=""
printf '%-3s %-21s %-26s %-9s %-15s %s\n' '#' 'MINTED(UTC)' 'BEAD/KIND' 'HASH' 'CLASS' 'EVIDENCE'
printf '%-3s %-21s %-26s %-9s %-15s %s\n' '--' '--------------------' '-------------------------' '--------' '--------------' '--------'

while IFS= read -r LINE; do
  [ -n "$LINE" ] || continue
  N=$((N + 1))
  TS=$(printf '%s' "$LINE" | awk '{print $1}')
  F2=$(printf '%s' "$LINE" | awk '{print $2}')
  F3=$(printf '%s' "$LINE" | awk '{print $3}')
  CLASS="" EV=""

  if printf '%s' "$LINE" | grep -Eq '^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z ANNOTATION VOID [0-9a-f]{8,64} .+'; then
    # an annotation line being flushed: must reference a real PASS row
    PFX=$(printf '%s' "$LINE" | awk '{print $4}')
    REF=$(printf '%s\n' "$STAGED_LOG" | awk -v p="$PFX" '$4 == "PASS" && index($3, p) == 1 { print $3; exit }')
    if [ -n "$REF" ]; then
      CLASS="ANNOTATION"; EV="covers PASS row ${REF:0:8}"
    else
      CLASS="UNCLASSIFIED"; EV="annotation references no PASS row in the staged log"
    fi

  elif printf '%s' "$LINE" | grep -Eq '^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z [A-Za-z0-9._-]+ [0-9a-f]{64} PASS$'; then
    BEAD="$F2" HASH="$F3"
    ROWEP=$(ep "$TS")
    if [ -z "$ROWEP" ]; then
      CLASS="UNCLASSIFIED"; EV="unparseable timestamp"
    fi

    # 1) VOID-ANNOTATED — an annotation prefix-matches this row's hash
    if [ -z "$CLASS" ]; then
      VTS=$(printf '%s\n' "$STAGED_LOG" | awk -v h="$HASH" '$2 == "ANNOTATION" && $3 == "VOID" && index(h, $4) == 1 { print $1; exit }')
      [ -n "$VTS" ] && { CLASS="VOID-ANNOTATED"; EV="annotation @ $VTS"; }
    fi

    # 2) SUPERSEDED — a later PASS row for the same bead (re-mint)
    if [ -z "$CLASS" ]; then
      LATER=$(printf '%s\n' "$STAGED_LOG" | awk -v b="$BEAD" -v ts="$TS" '$2 == b && $4 == "PASS" && $1 > ts { print $1; exit }')
      [ -n "$LATER" ] && { CLASS="SUPERSEDED"; EV="re-mint @ $LATER"; }
    fi

    # 3) LANDED — a commit citing the bead (or any wrap commit, for wrap rows)
    #    authored at/after the mint. Desc git-log order: last hit >= ts is earliest.
    if [ -z "$CLASS" ]; then
      case "$BEAD" in
        *wrap*) HIT=$(git log -i --grep='wrap' --pretty='%h %at' | awk -v t="$ROWEP" '$2 >= t { h = $1; e = $2 } END { if (h) print h, e }') ;;
        *)      HIT=$(git log --fixed-strings --grep="$BEAD" --pretty='%h %at' | awk -v t="$ROWEP" '$2 >= t { h = $1; e = $2 } END { if (h) print h, e }') ;;
      esac
      if [ -n "$HIT" ]; then
        CLASS="LANDED"; EV="commit ${HIT%% *} @ $(iso "${HIT##* }")"
      fi
    fi

    # 4) LANDED-WRAP — first commit after the mint is a wrap commit within TTL
    if [ -z "$CLASS" ]; then
      FIRST=$(git log --pretty='%h|%at|%s' | awk -F'|' -v t="$ROWEP" '$2 >= t { h = $1; e = $2; s = $3 } END { if (h) print h "|" e "|" s }')
      if [ -n "$FIRST" ]; then
        FH=${FIRST%%|*}; REST=${FIRST#*|}; FE=${REST%%|*}; FS=${REST#*|}
        if printf '%s' "$FS" | grep -iq 'wrap' && [ $((FE - ROWEP)) -le "$TOKEN_TTL" ]; then
          CLASS="LANDED-WRAP"; EV="wrap commit $FH @ $(iso "$FE") consumed mint (+$((FE - ROWEP))s)"
        fi
      fi
    fi

    if [ -z "$CLASS" ]; then
      CLASS="UNCLASSIFIED"; EV="no citing commit at/after mint, no later re-mint, no VOID annotation"
    fi
  else
    CLASS="UNCLASSIFIED"; EV="unrecognized line format (not a PASS row or annotation)"
  fi

  if [ "$CLASS" = "UNCLASSIFIED" ]; then
    UNCLASS=$((UNCLASS + 1))
    UNLIST="$UNLIST
  line $N: $LINE
    -> $EV"
  fi
  HP=$(printf '%s' "$F3" | grep -Eq '^[0-9a-f]{8}' && printf '%.8s' "$F3" || echo '-')
  printf '%-3s %-21s %-26s %-9s %-15s %s\n' "$N" "$TS" "$F2" "$HP" "$CLASS" "$EV"
done <<EOF_ADDED
$ADDED
EOF_ADDED

echo
if [ "$UNCLASS" = "0" ]; then
  echo "FLUSH-VERIFY PASS: all $N added line(s) classified — safe to audit as a flush commit"
  exit 0
else
  echo "FLUSH-VERIFY FAIL: $UNCLASS of $N added line(s) UNCLASSIFIED:$UNLIST" >&2
  exit 1
fi
