#!/bin/bash
# SubagentStart hook: writes the DISPATCH_LOG row mechanically.
# Write-ahead discipline stops depending on the agent remembering.
INPUT=$(cat)
AGENT=$(echo "$INPUT" | jq -r '.agent_type // "unknown"')
# ==== BEGIN agent_type safety gate (mirrored) ============================
# MUST STAY BYTE-IDENTICAL to the block of the same name in the other half of
# this pair: scripts/dispatch-log-writeahead.sh <-> scripts/dispatch-log-close.sh
# Verify with (expect TWO IDENTICAL HASHES and lines=62 on both). The line
# count is not decoration. The first version of this very command used
# UNANCHORED markers, so the command's own text contained both ends of the
# sed range, the range closed on the line that opened it, the extraction
# collapsed to 6 lines of comment, and the two hashes therefore agreed no
# matter what the gate code below said -- they would still have agreed if one
# file's gate had been deleted outright. If lines= is small, the check is
# lying to you; repair the markers before you believe the hash.
#   for f in scripts/dispatch-log-writeahead.sh scripts/dispatch-log-close.sh; do
#     b=$(sed -n '/^# ==== BEGIN agent_type safety gate/,/^# ==== END agent_type safety gate/p' "$f")
#     printf '%s  lines=%s  %s\n' "$(printf '%s\n' "$b" | shasum | cut -d' ' -f1)" \
#       "$(printf '%s\n' "$b" | wc -l | tr -d ' ')" "$f"
#   done
#
# WHY THIS EXISTS: agent_type is interpolated into the WHO: field of an
# append-only ledger row. It used to be read RAW while its sibling agent_id
# was gated, which made it the soft spot of the pair. Four attacks, all
# through agent_type alone, all reproduced against the ungated code:
#   (a) SILENT DENIAL-OF-CLOSE. An agent_type containing "corr=<victim>"
#       needs no newline: the substring lands in WHO: on a row that already
#       ends "| STATE: closed@unattributed", so the victim's own later
#       genuine stop reads it as "this token was already dispositioned",
#       no-ops, and the victim's open row stays STATE: dispatched forever
#       with nothing in the ledger to show a close was ever suppressed.
#   (b) ROW FORGERY. An embedded newline splits one physical row into
#       several; an attacker-chosen trailing segment ending
#       "| STATE: dispatched" manufactures an open row that never spawned.
#   (c) UNKEYED KEY POISONING. An agent_type containing "key=<hash>"
#       suppresses a later, genuinely different UNKEYED close the same way.
#   (d) FIELD FORGERY. An agent_type containing "|" invents field
#       boundaries and breaks the one-row / seven-field / six-pipe schema
#       every reader and every matcher in this pair assumes.
#
# The gate is the SAME strictness class this pair already applies to the
# sibling field agent_id: strict charset [A-Za-z0-9_-], 64-char cap. Nothing
# else is accepted. (The agent_id gate sits below this block in the writer
# and above it in the closer; only this block is required to be identical.)
#
# NOTE: this check must NOT use grep. grep is line-oriented, so a value whose
# FIRST LINE is valid passes a `grep -qE '^...$'` test -- which is exactly
# hostile case (b). `case` matches the whole string, newlines included.
#
# Rejection is LOUD, not silent. A rejected value is replaced with the fixed
# literal below, deliberately distinct from "unknown" so a reader can tell
# "the payload carried no agent_type" apart from "the payload carried an
# agent_type that was refused". The literal is 26 chars and inside the safe
# charset, so it can never itself re-trip the gate, and it adds no pipe and
# no newline, so the row stays exactly 7 fields / 6 pipes / 1 physical line.
if [ -z "$AGENT" ]; then
  AGENT="unknown"
else
  case "$AGENT" in
    *[!A-Za-z0-9_-]*) AGENT="agent-type-rejected-unsafe" ;;
  esac
  if [ "${#AGENT}" -gt 64 ]; then
    AGENT="agent-type-rejected-unsafe"
  fi
fi
# ==== END agent_type safety gate (mirrored) ==============================
# KEYED-correlation support (Praxis_build-43n): carry the same token the
# SubagentStart payload names as agent_id into the row itself, so a
# SubagentStop-side closer (scripts/dispatch-log-close.sh) can match its own
# corr token back to this exact row instead of guessing. When agent_id is
# absent (e.g. a main-thread --agent spawn, which carries no agent_id) this
# adds nothing and the row is byte-for-byte the old format.
CORR=$(echo "$INPUT" | jq -r '.agent_id // empty' 2>/dev/null)
# Token safety gate — must mirror the one in dispatch-log-close.sh exactly.
# An agent_id containing a newline would split this row into two physical
# lines (breaking the one-row-per-line schema every reader assumes); one
# containing a space or '|' would forge a field boundary. Anything outside the
# strict charset, or over 64 chars, is dropped and the row is written in the
# original corr-less format — the documented degrade, not a corrupt row.
# NOTE: must NOT use grep here — grep is line-oriented, so a token with an
# embedded newline passes whenever its first line is valid, which is precisely
# the row-splitting case this gate exists to stop. `case` matches the whole
# string. This must stay identical to the gate in dispatch-log-close.sh.
if [ -n "$CORR" ]; then
  case "$CORR" in
    *[!A-Za-z0-9_-]*) CORR="" ;;
  esac
fi
if [ -n "$CORR" ] && [ "${#CORR}" -gt 64 ]; then
  CORR=""
fi
TS=$(date -u +%Y-%m-%dT%H:%M:%SZ)
# PRAXIS_DISPATCH_LOG mirrors the override the closer already honours, so both
# halves of the pair can be exercised against a fixture instead of the real
# ledger. Unset in production, so the default path is the original one.
LOG="${PRAXIS_DISPATCH_LOG:-${CLAUDE_PROJECT_DIR:-.}/DISPATCH_LOG.md}"
[ -f "$LOG" ] || echo "# DISPATCH LOG" > "$LOG"
# Append-only newline guard — see the same block in dispatch-log-close.sh.
# Without it, a log not ending in a newline gets its LAST ROW FUSED with this
# one, silently altering a row and hiding it from every `STATE: dispatched$`
# matcher. This flaw predates the closer; it is repaired here in the same
# change that ships the counterpart.
if [ -s "$LOG" ] && [ -n "$(tail -c 1 "$LOG" 2>/dev/null)" ]; then
  printf '\n' >> "$LOG" 2>/dev/null
fi
WHERE="session $(git -C "${CLAUDE_PROJECT_DIR:-.}" rev-parse --short HEAD 2>/dev/null || echo no-git)"
[ -n "$CORR" ] && WHERE="$WHERE corr=$CORR"
echo "- [$TS] WHO: $AGENT | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: $WHERE | WHEN: spawn | HOW: awaiting terminal state | STATE: dispatched" >> "$LOG"
exit 0
