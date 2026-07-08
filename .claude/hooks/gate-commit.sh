#!/bin/bash
# PreToolUse gate (matcher: Bash). Denies `git commit` in an ARMED repo unless a
# fresh single-use audit token exists for the CURRENT staged diff AND a matching
# AUDIT_LOG PASS row proves the orchestrator-auditor minted it. Armed only while
# .claude/state/orchestrator-active exists — normal sessions are unaffected.
#
# The commit match is deliberately broad (`*git*commit*`): it also catches
# `git -C <dir> commit`, `git --work-tree=... commit`, and chained forms
# (`cd x && git commit ...`). Over-match is intentional and fail-closed — a
# non-commit command that trips it just gets re-issued clean; a
# `cd otherrepo && git commit` burns THIS armed repo's token (fail-safe for the
# armed repo, not a bypass). Non-git commands (git status, ls, echo) pass through.
set -uo pipefail
INPUT=$(cat)
CMD=$(printf '%s' "$INPUT" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("tool_input",{}).get("command",""))' 2>/dev/null || true)
case "$CMD" in
  *git*commit*) ;;
  *) exit 0 ;;
esac
ROOT="${CLAUDE_PROJECT_DIR:-.}"
STATE="$ROOT/.claude/state"
[ -f "$STATE/orchestrator-active" ] || exit 0

# --- Form checks: run BEFORE token lookup so a form denial never consumes the
# token. Fail-closed; the model just re-issues a clean commit. ---
deny_form() {
  echo "Commit denied: $1" >&2
  echo "Commit exactly the staged diff with a plain \`git commit -m \"...\"\` — no -a/--all/--include/--amend, no pathspec after ' -- ', and run it as the sole command in its own Bash call." >&2
  exit 2
}
# short-flag cluster containing 'a' ( -a, -am, -sam, ... ) sweeps the working tree
if printf '%s' "$CMD" | grep -Eq '(^|[[:space:]])-[A-Za-z]*a[A-Za-z]*([[:space:]]|$)'; then
  deny_form "a '-a'-style short flag sweeps unstaged working-tree changes into the commit"
fi
if printf '%s' "$CMD" | grep -Eq '(^|[[:space:]])--(all|include|amend)([[:space:]]|=|$)'; then
  deny_form "--all/--include/--amend changes the committed set out from under the audit"
fi
if printf '%s' "$CMD" | grep -Eq '[[:space:]]--[[:space:]]'; then
  deny_form "a pathspec after ' -- ' commits a different set than what was audited"
fi
# one git commit per Bash call — no staging in the same call, no double commit
if printf '%s' "$CMD" | grep -Eq 'git[[:space:]]+add'; then
  echo "Commit denied: one git commit per Bash call — stage in a separate call first." >&2
  exit 2
fi
if [ "$(printf '%s' "$CMD" | grep -oE 'git[[:space:]]+commit' | wc -l | tr -d ' ')" -gt 1 ]; then
  echo "Commit denied: one git commit per Bash call — stage in a separate call first." >&2
  exit 2
fi

# --- Token + AUDIT_LOG checks: only a fresh token whose hash also appears as a
# PASS row in AUDIT_LOG.md is honored (a bare `touch`ed token is forgery). ---
HASH=$(cd "$ROOT" && git diff --cached | shasum -a 256 | awk '{print $1}')
TOKEN="$STATE/audit-pass-$HASH"
if [ -f "$TOKEN" ]; then
  NOW=$(date +%s)
  MT=$(stat -f %m "$TOKEN")
  if [ $((NOW - MT)) -gt 1800 ]; then
    rm -f "$TOKEN"
    echo "Commit denied: audit token expired (>30 min old). Re-dispatch orchestrator-auditor to re-grade the staged diff." >&2
    exit 2
  fi
  if ! grep -q "$HASH PASS" "$ROOT/AUDIT_LOG.md" 2>/dev/null; then
    rm -f "$TOKEN"
    echo "Commit denied: token has no AUDIT_LOG PASS row — forged or corrupted; re-dispatch the orchestrator-auditor." >&2
    exit 2
  fi
  rm -f "$TOKEN"   # single-use
  exit 0
fi
echo "Commit denied: no audit PASS token for this exact staged diff. Dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself." >&2
exit 2
