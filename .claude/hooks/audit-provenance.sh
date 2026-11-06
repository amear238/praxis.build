#!/bin/bash
# audit-provenance.sh — shared library, SOURCED by auditor-mint.sh (SubagentStop
# minter) and gate-commit.sh (PreToolUse commit gate). D-2026-11-04-B item 3.
# Defines four functions and nothing else: no side effects on source, no shell
# options changed, safe under `set -u`.
#
#   ap_index_norm <ROOT> <INDEX>   -> prints REAL or the realpath of INDEX
#   ap_diff_hash  <ROOT> <INDEX>   -> prints sha256 of the CANONICAL cached diff under INDEX:
#                                     git diff --cached --no-ext-diff --no-textconv --no-color --text --ignore-submodules=none --no-relative
#   ap_tree       <ROOT> <INDEX>   -> prints `git write-tree` under INDEX
#   ap_verify <agent_id> <agent_transcript> <parent_transcript> <hash> [mint]
#                                  -> 0 iff the transcript provenance holds
#
# The optional 5th argument, when it is exactly `mint`, skips check 6 ONLY (the
# agent transcript must carry the `COMMIT-DIFF-SHA256: <hash>` assistant line).
# Why: auditor-mint.sh runs on SubagentStop, and it is UNVERIFIED whether the
# harness has flushed the auditor's final message to agent-<id>.jsonl by the
# time that hook fires; the minter already parses the same line from the
# payload's last_assistant_message. The commit gate calls ap_verify WITHOUT
# `mint`, so check 6 is still enforced at commit time, when the transcript has
# certainly been written. Any other value of the 5th argument changes nothing.
#
# INDEX is the literal word REAL (the repo's own index, GIT_INDEX_FILE unset)
# or an absolute path to an index file. `grep` in this environment can be a
# ugrep wrapper that skips gitignored paths, so /usr/bin/grep is used explicitly.
#
# What this does NOT prevent: every actor runs as the same uid. Anyone who
# fabricates the meta file, the subagent transcript AND the tool_use record in
# the parent transcript passes ap_verify. It turns a one-call forgery into a
# multi-file forgery of harness-owned files; it is not a wall.

_ap_realpath() {
  # Resolve a path that must exist. Prints the canonical path; returns 1 on failure.
  local p="${1:-}" out
  [ -n "$p" ] || return 1
  if [ -x /bin/realpath ]; then
    out=$(/bin/realpath "$p" 2>/dev/null) || return 1
  else
    out=$(python3 -c 'import os,sys;print(os.path.realpath(sys.argv[1]))' "$p" 2>/dev/null) || return 1
    [ -e "$out" ] || return 1
  fi
  [ -n "$out" ] || return 1
  printf '%s\n' "$out"
}

_ap_git() {
  # _ap_git <ROOT> <INDEX> <git args...> — run git at ROOT under the named index.
  local root="$1" idx="$2"
  shift 2
  if [ "$idx" = "REAL" ]; then
    (cd "$root" && env -u GIT_INDEX_FILE git "$@")
  else
    (cd "$root" && GIT_INDEX_FILE="$idx" git "$@")
  fi
}

ap_index_norm() {
  local root="${1:-}" idx="${2:-}" nl rp real realrp
  nl=$'\n'
  [ -n "$root" ] && [ -n "$idx" ] || return 1
  case "$idx" in *"$nl"*) return 1 ;; esac
  if [ "$idx" = "REAL" ]; then
    printf 'REAL\n'
    return 0
  fi
  case "$idx" in /*) ;; *) return 1 ;; esac
  [ -f "$idx" ] || return 1
  rp=$(_ap_realpath "$idx") || return 1
  real=$(env -u GIT_INDEX_FILE git -C "$root" rev-parse --git-path index 2>/dev/null) || return 1
  [ -n "$real" ] || return 1
  case "$real" in /*) ;; *) real="$root/$real" ;; esac
  realrp=$(_ap_realpath "$real" 2>/dev/null) || realrp="$real"
  if [ "$rp" = "$realrp" ]; then
    printf 'REAL\n'
  else
    printf '%s\n' "$rp"
  fi
  return 0
}

ap_diff_hash() {
  local root="${1:-}" idx="${2:-}" rc h
  [ -n "$root" ] && [ -n "$idx" ] || return 1
  # Canonical form (attack A10, W6 2026-11-04): with diff.external, a textconv
  # driver or color.diff=always configured, plain `git diff --cached` prints
  # whatever the producer's config wants, so the auditor could review a decoy
  # whose hash still matched. --no-ext-diff/--no-textconv/--no-color force git's
  # own patch.
  # Attacks A1a/A2d/A2c (W10, 2026-11-04): `.git/info/attributes` `binary` /
  # `-diff`, or `diff.<driver>.binary=true`, turned a text file into a base85
  # "GIT binary patch" the auditor cannot read (--binary made that worse, not
  # better); `diff.ignoreSubmodules=all` (or submodule.<name>.ignore) dropped a
  # newly staged gitlink from the diff entirely. --text forces a line patch for
  # every file whatever the attributes say; --ignore-submodules=none --no-relative overrides
  # every config-level submodule ignore. --binary is dropped.
  # --quiet: 0 = empty diff (refuse), 1 = non-empty, anything else = git failure.
  _ap_git "$root" "$idx" diff --cached --quiet --no-ext-diff --no-textconv --no-color --text --ignore-submodules=none --no-relative >/dev/null 2>&1
  rc=$?
  [ "$rc" -eq 1 ] || return 1
  # Hash the exact bytes of the same command the auditor runs; pipefail in a
  # subshell so a git failure is not masked by shasum's exit status.
  h=$( (set -o pipefail; _ap_git "$root" "$idx" diff --cached --no-ext-diff --no-textconv --no-color --text --ignore-submodules=none --no-relative 2>/dev/null | shasum -a 256 | awk '{print $1}') ) || return 1
  [[ "$h" =~ ^[0-9a-f]{64}$ ]] || return 1
  printf '%s\n' "$h"
}

ap_tree() {
  local root="${1:-}" idx="${2:-}" t
  [ -n "$root" ] && [ -n "$idx" ] || return 1
  t=$(_ap_git "$root" "$idx" write-tree 2>/dev/null) || return 1
  [[ "$t" =~ ^[0-9a-f]{40,64}$ ]] || return 1
  printf '%s\n' "$t"
}

ap_verify() {
  local aid="${1:-}" at="${2:-}" pt="${3:-}" hash="${4:-}" mode="${5:-}"
  local proj at_rp pt_rp adir meta tuid want hit line
  if ! [[ "$aid" =~ ^[A-Za-z0-9_-]{1,64}$ ]]; then
    echo "ap_verify: agent_id malformed" >&2; return 1
  fi
  if ! [[ "$hash" =~ ^[0-9a-f]{64}$ ]]; then
    echo "ap_verify: hash malformed" >&2; return 1
  fi
  # 2. agent transcript location
  proj=$(_ap_realpath "${HOME:-}/.claude/projects") || { echo "ap_verify: \$HOME/.claude/projects does not resolve" >&2; return 1; }
  at_rp=$(_ap_realpath "$at") || { echo "ap_verify: agent transcript does not resolve" >&2; return 1; }
  case "$at_rp" in
    "$proj"/*) ;;
    *) echo "ap_verify: agent transcript not under \$HOME/.claude/projects" >&2; return 1 ;;
  esac
  [ -f "$at_rp" ] || { echo "ap_verify: agent transcript not a regular file" >&2; return 1; }
  if [ "$(basename "$at_rp")" != "agent-$aid.jsonl" ]; then
    echo "ap_verify: agent transcript basename is not agent-$aid.jsonl" >&2; return 1
  fi
  adir=$(dirname "$at_rp")
  if [ "$(basename "$adir")" != "subagents" ]; then
    echo "ap_verify: agent transcript parent dir is not subagents" >&2; return 1
  fi
  # 3. sibling meta.json
  meta="$adir/agent-$aid.meta.json"
  [ -f "$meta" ] || { echo "ap_verify: meta.json missing" >&2; return 1; }
  if ! jq -e '.agentType == "praxis-auditor" and .spawnDepth == 1 and ((.toolUseId // "") | type == "string" and length > 0)' "$meta" >/dev/null 2>&1; then
    echo "ap_verify: meta.json fails agentType/spawnDepth/toolUseId check" >&2; return 1
  fi
  tuid=$(jq -r '.toolUseId' "$meta" 2>/dev/null)
  [ -n "$tuid" ] || { echo "ap_verify: toolUseId empty" >&2; return 1; }
  # 4. parent transcript == <slug>/<session>.jsonl
  pt_rp=$(_ap_realpath "$pt") || { echo "ap_verify: parent transcript does not resolve" >&2; return 1; }
  want="$(dirname "$adir").jsonl"
  if [ "$pt_rp" != "$want" ]; then
    echo "ap_verify: parent transcript is not the session transcript of the agent" >&2; return 1
  fi
  [ -f "$pt_rp" ] || { echo "ap_verify: parent transcript not a regular file" >&2; return 1; }
  # 5. parent has the Agent tool_use that spawned a praxis-auditor with that id
  hit=$(/usr/bin/grep -F -- "$tuid" "$pt_rp" 2>/dev/null \
    | jq -R --arg id "$tuid" 'fromjson? | select(type == "object" and .type == "assistant")
        | .message.content? | select(type == "array") | .[]
        | select(type == "object" and .type == "tool_use" and .id == $id and .name == "Agent"
                 and ((.input.subagent_type? // "") == "praxis-auditor"))
        | 1' 2>/dev/null | head -n 1)
  if [ "$hit" != "1" ]; then
    echo "ap_verify: parent transcript has no Agent tool_use $tuid for praxis-auditor" >&2; return 1
  fi
  # 6. agent transcript carries the COMMIT-DIFF-SHA256 line in assistant text.
  # Skipped ONLY at mint time (5th arg exactly `mint`) — see the header comment.
  [ "$mode" = "mint" ] && return 0
  line="COMMIT-DIFF-SHA256: $hash"
  if ! /usr/bin/grep -F -- "$line" "$at_rp" 2>/dev/null \
    | jq -R -r 'fromjson? | select(type == "object" and .type == "assistant")
        | .message.content? | if type == "string" then . elif type == "array" then (.[] | select(type == "object" and .type == "text") | .text) else empty end' 2>/dev/null \
    | sed -e 's/\r$//' -e 's/[[:space:]]*$//' \
    | /usr/bin/grep -qxF -- "$line"; then
    echo "ap_verify: agent transcript has no assistant line '$line'" >&2; return 1
  fi
  return 0
}
