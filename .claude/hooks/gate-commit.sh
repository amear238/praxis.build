#!/bin/bash
# PreToolUse gate (matcher: Bash). Denies `git commit` in an ARMED repo unless a
# fresh single-use audit token exists for the CURRENT staged diff AND a matching
# AUDIT_LOG PASS row proves the orchestrator-auditor minted it. Armed only while
# .claude/state/orchestrator-active exists — normal sessions are unaffected.
#
# Hardened 2026-07-10 (bead v6y) after a parallel session polluted the shared
# .git/index between token-mint and commit:
#   1. staged-TREE binding — token carries `tree=<git write-tree>` from mint time;
#      commit is denied unless the index still produces that exact tree.
#   2. single-session rule — commit is denied while any OTHER live claude
#      process (outside this session's own process tree) has its cwd inside
#      this repo. Check errors fail CLOSED.
#   3. orphaned-token sweep — tokens >30 min old are deleted even if their hash
#      never matches again (previously they lingered forever).
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

# --- Single-session check: deny while another live claude process (outside this
# session's own process tree) is cwd'd inside this repo. Runs BEFORE token lookup
# so it never consumes the token — close the other session and retry. Any failure
# of the check itself denies (fail CLOSED); the trader can rerun. ---
deny_session() {
  echo "Commit denied: $1" >&2
  echo "Single-session rule: exactly ONE Claude session per repo working tree (docs/runbooks/2026-07-10-single-session-rule.md). Close the other session (or move it to its own git worktree) and re-run the commit." >&2
  exit 2
}
REPO=$(cd "$ROOT" 2>/dev/null && pwd -P) || deny_session "cannot resolve repo root '$ROOT' for the single-session check"
# argv[0] basename starts with "claude" → it is a claude session process
is_claude_pid() {
  _c=$(ps -o command= -p "$1" 2>/dev/null) || return 1
  _first=${_c%% *}
  case "${_first##*/}" in claude*) return 0 ;; *) return 1 ;; esac
}
# our own claude ancestor: walk PPID up from this hook shell
MY_CLAUDE=""
_p=$$
while [ -n "$_p" ] && [ "$_p" != "0" ] && [ "$_p" != "1" ]; do
  if is_claude_pid "$_p"; then MY_CLAUDE="$_p"; break; fi
  _p=$(ps -o ppid= -p "$_p" 2>/dev/null | tr -d ' ')
done
# is pid our own session's process (== our claude ancestor, or descends from it)?
descends_from_mine() {
  [ -n "$MY_CLAUDE" ] || return 1
  _q=$1 _hops=0
  while [ -n "$_q" ] && [ "$_q" != "0" ] && [ "$_q" != "1" ] && [ "$_hops" -lt 64 ]; do
    [ "$_q" = "$MY_CLAUDE" ] && return 0
    _q=$(ps -o ppid= -p "$_q" 2>/dev/null | tr -d ' ')
    _hops=$((_hops + 1))
  done
  return 1
}
# every process with a cwd, as -Fpn records (p<pid> / n<path>); command names are
# NOT trusted here — lsof truncates/mangles them (observed "claude.ex", "2.1.206")
LSOF_OUT=$(lsof -a -d cwd -Fpn 2>/dev/null)
[ -n "$LSOF_OUT" ] || deny_session "single-session check failed: lsof produced no data"
FOREIGN=""
CUR=""
while IFS= read -r LINE; do
  case "$LINE" in
    p*) CUR="${LINE#p}" ;;
    n*) DIR="${LINE#n}"
        case "$DIR" in
          "$REPO"|"$REPO"/*)
            [ -n "$CUR" ] || continue
            descends_from_mine "$CUR" && continue
            is_claude_pid "$CUR" && FOREIGN="$FOREIGN $CUR"
            ;;
        esac ;;
  esac
done <<EOF_LSOF
$LSOF_OUT
EOF_LSOF
if [ -n "$FOREIGN" ]; then
  deny_session "another live claude session (pid$FOREIGN) has its cwd inside this repo — it can pollute the shared .git/index between audit and commit (2026-07-10 incident)"
fi

# --- Token + AUDIT_LOG checks: only a fresh token whose hash also appears as a
# PASS row in AUDIT_LOG.md is honored (a bare `touch`ed token is forgery). ---
# Sweep orphaned tokens first: a token whose staged diff drifted (re-audit minted
# a new hash) previously lingered forever; anything >30 min old is dead either way.
find "$STATE" -name 'audit-pass-*' -mmin +30 -exec rm -f {} + 2>/dev/null
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
  # staged-TREE binding: the index must still produce the exact tree the token
  # was minted against — extra/missing/changed paths in the mint→commit gap deny.
  MINT_TREE=$(sed -n 's/^tree=//p' "$TOKEN" | head -1)
  NOW_TREE=$(cd "$ROOT" && git write-tree 2>/dev/null)
  if [ -z "$MINT_TREE" ] || [ -z "$NOW_TREE" ] || [ "$MINT_TREE" != "$NOW_TREE" ]; then
    rm -f "$TOKEN"
    echo "Commit denied: staged tree no longer matches the tree the audit token was minted against (minted tree=${MINT_TREE:-missing/legacy-token}, current tree=${NOW_TREE:-unresolvable}). Something changed the index after mint — re-stage exactly the audited set and re-dispatch the orchestrator-auditor." >&2
    exit 2
  fi
  rm -f "$TOKEN"   # single-use: consumed at allow time, before the commit runs
  exit 0
fi
echo "Commit denied: no audit PASS token for this exact staged diff (the staged set may have changed since mint). Dispatch the orchestrator-auditor agent; it mints the token on PASS. Never run audit-approve.sh yourself." >&2
exit 2
