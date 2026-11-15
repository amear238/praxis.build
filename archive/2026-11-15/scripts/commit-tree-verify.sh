#!/bin/bash
# commit-tree-verify.sh — PostToolUse hook (matcher: Bash). D-2026-11-04-B,
# W8 fix E (adversarial attacks A1/A3), 2026-11-04.
#
# DETECTION ONLY. THIS HOOK CANNOT UNDO A COMMIT. It runs after the Bash call
# has finished; by then the commit (if any) is already in the object store and
# on the branch. It only tells the model, loudly, that what landed is not what
# the gate allowed, so a human can revert.
#
# Why it exists: .claude/hooks/gate-commit.sh (PreToolUse) checks the index
# BEFORE the commit runs. Anything that changes the index between that check
# and git's own write-tree is invisible to the gate — e.g. a git pre-commit
# hook that `git add`s a file (this repo has core.hooksPath=.beads/hooks with a
# pre-commit that runs `bd hooks run pre-commit`), or a background job.
#
# Protocol: when the gate ALLOWS a commit it writes .claude/state/last-allowed:
#   tree=<tree the audit token was minted for>   index=<REAL|abs path>
#   hash=<diff sha256>   head_before=<HEAD sha or none>   ts=<epoch>
#   cmd_sha256=<sha256 of the allowed Bash command text>
# This hook, on every Bash PostToolUse:
#   - no last-allowed file                        -> exit 0, silent
#   - cmd_sha256 present and != this call's command -> exit 0, file LEFT in
#     place (a different, parallel Bash call finished first)
#   - otherwise read it, DELETE it, then:
#       HEAD == head_before -> the commit did not land; say so (exit 2)
#       HEAD^{tree} != tree -> `COMMIT TREE MISMATCH: ...` + diff --stat on
#                              stderr, same line appended to mint-log (exit 2)
#       else                -> exit 0, silent
# ROOT = $CLAUDE_PROJECT_DIR (same as the gate), else ".".
#
# Known limits: if the allowed Bash call never produces a PostToolUse event
# (e.g. it is blocked by a later hook, or the harness does not fire PostToolUse
# for a failing command — UNVERIFIED), the record lingers until the gate's next
# allow overwrites it. Every actor runs as the same uid: deleting last-allowed
# first silences this hook (scripts/mint-guard.sh trips on the naive forms only).
set -u
INPUT=$(cat)
ROOT="${CLAUDE_PROJECT_DIR:-.}"
ST="$ROOT/.claude/state"
LA="$ST/last-allowed"
[ -f "$LA" ] || exit 0

CMD=$(jq -r '.tool_input.command // ""' <<<"$INPUT" 2>/dev/null)
REC=$(cat "$LA" 2>/dev/null)
field() { printf '%s\n' "$REC" | sed -n "s/^$1=//p" | head -1; }
WANT_CSHA=$(field cmd_sha256)
if [ -n "$WANT_CSHA" ]; then
  HAVE_CSHA=$(printf '%s' "$CMD" | shasum -a 256 | awk '{print $1}')
  [ "$HAVE_CSHA" = "$WANT_CSHA" ] || exit 0
fi
rm -f "$LA"

TREE=$(field tree)
IDX=$(field index)
HASH=$(field hash)
HB=$(field head_before)
TS=$(date -u +%Y-%m-%dT%H:%M:%SZ)
logline() { mkdir -p "$ST" 2>/dev/null; printf '%s %s\n' "$TS" "$1" >> "$ST/mint-log" 2>/dev/null; }

NOW=$(cd "$ROOT" 2>/dev/null && git rev-parse -q --verify HEAD 2>/dev/null) || NOW=none
[ -n "$NOW" ] || NOW=none
if [ "$NOW" = "${HB:-none}" ]; then
  L="COMMIT NOT RECORDED: the gate allowed a commit of tree ${TREE:-?} (index ${IDX:-?}, hash ${HASH:-?}) but HEAD did not move (still ${NOW}). The commit failed or was aborted (e.g. by a pre-commit hook); the audit token is already consumed — re-audit before retrying."
  echo "$L" >&2
  logline "$L"
  exit 2
fi
HT=$(cd "$ROOT" && git rev-parse -q --verify 'HEAD^{tree}' 2>/dev/null) || HT=""
if [ -z "$TREE" ] || [ -z "$HT" ] || [ "$HT" != "$TREE" ]; then
  L="COMMIT TREE MISMATCH: the gate allowed tree ${TREE:-missing} (index ${IDX:-?}, hash ${HASH:-?}) but the new HEAD ${NOW} has tree ${HT:-unresolvable}"
  {
    echo "$L"
    echo "git diff --stat ${TREE:-?} HEAD^{tree}:"
    if [ -n "$TREE" ] && [ -n "$HT" ]; then
      (cd "$ROOT" && git diff --no-ext-diff --no-textconv --no-color --stat "$TREE" "$HT" 2>&1)
    fi
    echo "This hook cannot undo the commit. Something changed the index after the gate allowed it (git pre-commit hook, background job). Do not push; report to the trader and revert the unaudited content."
  } >&2
  logline "$L"
  exit 2
fi
exit 0
