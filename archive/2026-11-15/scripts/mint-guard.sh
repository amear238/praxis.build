#!/bin/bash
# mint-guard.sh — PreToolUse tripwire (Bash|Write|Edit|NotebookEdit). D-2026-11-04-B item 5.
#
# Purpose: a praxis-* caller (master, manager, worker, auditor, tutor; main thread
# or subagent) must not mint a commit-gate token by hand. Denies the NAIVE routes:
#   Bash  — a command naming audit-approve, auditor-mint, audit-provenance or
#           audit-pass-; or naming AUDIT_LOG together with a write form.
#   Write/Edit/NotebookEdit — a path ending AUDIT_LOG.md or containing
#           .claude/state/audit-pass-
# W8 fix F (2026-11-04, attack A6: deleting the arming file disarms the gate):
#   Bash  — a command naming orchestrator-active (any mention); a command
#           naming last-allowed or mint-log together with a write form (the
#           AUDIT_LOG forms, plus rm/unlink/shred/touch/rmdir).
#   Write/Edit/NotebookEdit — a path containing orchestrator-active, or a path
#           under .claude/state/ named last-allowed* or mint-log*.
# W13 fix (2026-11-04, attacks A9 / A4 / A4b):
#   Write/Edit/NotebookEdit paths are NORMALISED before matching (A9:
#   `.claude/./state/last-allowed`, `.claude/hooks/../state/audit-pass-x`,
#   `.claude//state/mint-log` used to pass): a relative path is joined to the
#   payload .cwd (else $CLAUDE_PROJECT_DIR, else $PWD), then python3
#   os.path.normpath; the realpath of that is matched as well (symlinked dirs).
#   Both forms are matched case-insensitively against every pattern.
#   Added targets (tripwire): any path under .beads/hooks/ (the repo's
#   core.hooksPath — a git hook there runs inside the commit, A4) and any path
#   containing shell-snapshots (the harness's per-call shell init, A3b/A4b).
#   Bash: a command naming .beads/hooks or shell-snapshots together with a write
#   or delete form (same forms as last-allowed / mint-log).
#
# THIS IS A TRIPWIRE, NOT A WALL. Plain string matching on the command text;
# any string obfuscation evades it (variable splicing "aud""it-approve", base64,
# globbing audit-appr?ve.sh, a script file that does the write, eval, etc.).
# Every actor runs as the same uid with Bash; see D-2026-11-04-B "What this does
# NOT prevent".
#
# Matching is case-insensitive: this repo's volume is case-insensitive APFS, so
# `>> audit_log.md` writes the real AUDIT_LOG.md.
#
# Callers whose agent_type does not start with "praxis-" (empty agent_type =
# ordinary session, orchestrator-auditor = legacy audit-approve.sh route) are
# untouched: exit 0.
#
# FAIL-OPEN: empty or unparseable stdin makes jq yield "" for agent_type, which
# falls through to exit 0 (matches house style in master-*-guard.sh and
# no-commit-guard.sh). Recorded as a known fail-open.
INPUT=$(cat)
AGENT=$(jq -r '.agent_type // ""' <<<"$INPUT" 2>/dev/null)
case "$AGENT" in
  praxis-*) ;;
  *) exit 0 ;;
esac
TOOL=$(jq -r '.tool_name // ""' <<<"$INPUT" 2>/dev/null)
CMD=$(jq -r '.tool_input.command // ""' <<<"$INPUT" 2>/dev/null)
FILE=$(jq -r '.tool_input.file_path // ""' <<<"$INPUT" 2>/dev/null)
NB=$(jq -r '.tool_input.notebook_path // ""' <<<"$INPUT" 2>/dev/null)

deny() {
  echo "BLOCKED: mint-guard: $AGENT ($TOOL) $1 — audit tokens and AUDIT_LOG are written only by the minter, and the gate's state files (orchestrator-active, last-allowed, mint-log) only by the hooks (D-2026-11-04-B)." >&2
  exit 2
}

# --- Bash command text (checked whenever present, whatever tool_name says) ---
# write_form: 0 if $CMD contains a write form (shared by AUDIT_LOG and the
# fix-F state files). `|` alone is NOT one (cat AUDIT_LOG.md | head passes).
# `>`: any redirection, including >> and >|; fd-dup forms (2>&1, >&2) and
# redirections to /dev/null are dropped first so `grep x AUDIT_LOG.md 2>/dev/null` passes.
write_form() {
  local STRIPPED
  STRIPPED=$(sed -E 's/[0-9]*>{1,2}[[:space:]]*\/dev\/null//g; s/[0-9]*>&[0-9-]+//g' <<<"$CMD")
  grep -qE '>' <<<"$STRIPPED" \
    || grep -qiE '(^|[^[:alnum:]_-])(tee|dd|truncate|perl|python[0-9.]*|ruby|g?awk|install)([^[:alnum:]_-]|$)' <<<"$CMD" \
    || grep -qiE '(^|[^[:alnum:]_-])(cp|mv|ln)[[:space:]]' <<<"$CMD" \
    || grep -qE '(^|[[:space:]])(-[[:alpha:]]*i|-i[[:alpha:]]*|--in-place)([[:space:]=.]|$)' <<<"$CMD"
  # ^ in-place flag: -i, -i.bak, -Ei, -ni, -ie, --in-place. A short-flag
  #   cluster starting or ending in i; so `grep -i x AUDIT_LOG.md` is a
  #   known false positive (use `grep -n`/`-F`), `find -print` is not.
}
# delete_form: rm/unlink/shred/touch/rmdir as a word (fix-F state files only;
# AUDIT_LOG's set is unchanged).
delete_form() {
  grep -qiE '(^|[^[:alnum:]_-])(rm|unlink|shred|touch|rmdir)([^[:alnum:]_-]|$)' <<<"$CMD"
}
if [ -n "$CMD" ]; then
  if grep -qiE 'audit-approve|auditor-mint|audit-provenance|audit-pass-' <<<"$CMD"; then
    deny "command names a token-minting script or token file"
  fi
  if grep -qi 'AUDIT_LOG' <<<"$CMD"; then
    if write_form; then
      deny "command writes AUDIT_LOG"
    fi
  fi
  # fix F: the gate is armed only while .claude/state/orchestrator-active exists;
  # any Bash mention of it by a praxis-* caller trips (deleting it disarms the gate).
  if grep -qi 'orchestrator-active' <<<"$CMD"; then
    deny "command names the commit gate's arming file orchestrator-active"
  fi
  if grep -qiE 'last-allowed|mint-log' <<<"$CMD"; then
    if write_form || delete_form; then
      deny "command writes or deletes a commit-gate state file (last-allowed / mint-log)"
    fi
  fi
  # W13: git hooks dir (core.hooksPath) and the harness shell snapshots
  if grep -qiE '\.beads/hooks|shell-snapshots' <<<"$CMD"; then
    if write_form || delete_form; then
      deny "command writes or deletes a git hook under .beads/hooks or a harness shell snapshot"
    fi
  fi
fi

# --- Write/Edit/NotebookEdit target paths ---
# norm_paths <path>: prints the normalised absolute path and its realpath (one
# per line). Relative paths are joined to payload .cwd, else CLAUDE_PROJECT_DIR,
# else $PWD. On any python failure the raw path is printed (still matched).
PCWD=$(jq -r '.cwd // ""' <<<"$INPUT" 2>/dev/null)
[ -n "$PCWD" ] || PCWD="${CLAUDE_PROJECT_DIR:-$PWD}"
norm_paths() {
  python3 -I -c '
import os, sys
p, base = sys.argv[1], sys.argv[2]
if not os.path.isabs(p):
    p = os.path.join(base, p)
n = os.path.normpath(p)
print(n)
print(os.path.realpath(n))
' "$1" "$PCWD" 2>/dev/null || printf '%s\n' "$1"
}
for P in "$FILE" "$NB"; do
  [ -z "$P" ] && continue
  while IFS= read -r NP; do
    for Q in "$P" "$NP"; do
      LP=$(tr '[:upper:]' '[:lower:]' <<<"$Q")
      case "$LP" in
        *audit_log.md) deny "targets $P" ;;
        *.claude/state/audit-pass-*) deny "targets $P" ;;
        *orchestrator-active*) deny "targets $P" ;;
        *.claude/state/last-allowed*|*.claude/state/mint-log*) deny "targets $P" ;;
        *.beads/hooks/*) deny "targets $P (git hooks dir — a hook runs inside the commit)" ;;
        *shell-snapshots*) deny "targets $P (harness shell snapshot)" ;;
      esac
    done
  done < <(norm_paths "$P")
done
exit 0
