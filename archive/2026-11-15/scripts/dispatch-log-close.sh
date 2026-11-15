#!/bin/bash
# SubagentStop hook: closes the DISPATCH_LOG.md write-ahead row that
# dispatch-log-writeahead.sh opened at SubagentStart for the same spawn.
#
# Praxis_build-43n — S12 counterpart to the SubagentStart writer.
#
# HARD CONSTRAINTS (do not relax these when editing this file):
#   1. Append-only. This script must NEVER rewrite, edit, delete, or reorder
#      an existing DISPATCH_LOG.md line. The only write operation permitted
#      against the log is `>>`.
#   2. Always exit 0. A SubagentStop hook that exits non-zero blocks the
#      returning agent. Every branch below, including every error path,
#      falls through to the single `exit 0` at the bottom of this file.
#      Nothing in this script calls `exit` anywhere else.
#   3. Log path is overridable via PRAXIS_DISPATCH_LOG so this script is
#      testable without touching the real ledger.
#   4. Idempotent: running this script twice for the same stop event must
#      never append two closing rows for it.
#
# -----------------------------------------------------------------------
# CORR_JQ — BOUND AND CONFIRMED against real captured payloads, 2026-07-28,
# Claude Code 2.1.220. See docs/reports/2026-07-28-session39-dispatch-log-closer.md
# for the raw captures.
#
# The correlation field is `agent_id`. It is present on BOTH SubagentStart and
# SubagentStop and carries the identical value for the same spawn. Observed
# directly by registering a temporary unconditional raw-stdin capture hook on
# both events and reading what actually arrived — not inferred from docs, and
# not read out of the binary's string table.
#
# SubagentStart keys: agent_id agent_type cwd hook_event_name prompt_id
#                     session_id transcript_path
# SubagentStop  keys: agent_id agent_transcript_path agent_type
#                     background_tasks cwd effort hook_event_name
#                     last_assistant_message permission_mode prompt_id
#                     session_crons session_id stop_hook_active
#                     transcript_path
#
# Do NOT switch this to `prompt_id` or `session_id`. Both also appear on both
# events, but they are shared across every spawn in a prompt/session
# respectively, so they would correlate a stop to the wrong row. `agent_id` is
# the only per-spawn key observed.
#
# If a future Claude Code version renames or drops the field, this script does
# NOT start lying: it degrades to UNKEYED (see below), which records that a
# stop happened and explicitly claims no row. Nothing downstream assumes
# CORR_JQ resolves.
CORR_JQ='.agent_id // empty'

# -----------------------------------------------------------------------
LOG="${PRAXIS_DISPATCH_LOG:-${CLAUDE_PROJECT_DIR:-.}/DISPATCH_LOG.md}"
TS=$(date -u +%Y-%m-%dT%H:%M:%SZ 2>/dev/null)
[ -n "$TS" ] || TS="0000-00-00T00:00:00Z"

diag() {
  # Diagnostic-only. Never touches the log. Never affects exit status.
  echo "dispatch-log-close.sh: $*" >&2
}

# --- read stdin defensively -------------------------------------------
INPUT=$(cat 2>/dev/null)

# --- jq availability ----------------------------------------------------
JQ_BIN=$(command -v jq 2>/dev/null)
JQ_OK=0
[ -n "$JQ_BIN" ] && JQ_OK=1

# --- validate JSON, extract fields defensively --------------------------
AGENT="unknown"
TOKEN=""
REASON=""

if [ "$JQ_OK" -ne 1 ]; then
  REASON="jq-missing"
elif [ -z "$INPUT" ]; then
  REASON="empty-stdin"
elif ! printf '%s' "$INPUT" | "$JQ_BIN" -e . >/dev/null 2>&1; then
  REASON="non-json-stdin"
else
  AGENT=$(printf '%s' "$INPUT" | "$JQ_BIN" -r '.agent_type // "unknown"' 2>/dev/null)
  TOKEN=$(printf '%s' "$INPUT" | "$JQ_BIN" -r "$CORR_JQ" 2>/dev/null)
  [ "$TOKEN" = "null" ] && TOKEN=""
  # Token safety gate. An agent_id is trusted input in practice, but a
  # correlation token is interpolated into a grep pattern and into a ledger
  # row, so it is validated rather than trusted. Anything outside a strict
  # charset, or longer than 64 chars, is treated as NO TOKEN and degrades to
  # UNKEYED — the honest path — instead of corrupting the row schema or
  # blowing up the matcher. Observed real ids are 17 lowercase hex chars.
  # Rejects: embedded newlines (would split a ledger row and inject a second
  # grep pattern), spaces and '|' (would forge field boundaries), and
  # multi-kilobyte tokens (grep -F exits "out of memory" and the miss is then
  # recorded as a false "no row matched" claim).
  # NOTE: this check must NOT use grep. grep is line-oriented, so a token
  # containing an embedded newline passes a `grep -qE '^...$'` test whenever
  # its FIRST LINE happens to be valid — which is exactly the hostile case.
  # `case` matches against the whole string, newlines included.
  if [ -n "$TOKEN" ]; then
    case "$TOKEN" in
      *[!A-Za-z0-9_-]*) TOKEN=""; REASON="token-unsafe" ;;
    esac
  fi
  if [ -n "$TOKEN" ] && [ "${#TOKEN}" -gt 64 ]; then
    TOKEN=""
    REASON="token-unsafe"
  fi
  [ -n "$TOKEN" ] || [ -n "$REASON" ] || REASON="token-absent"
fi

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

# --- row-matcher availability probe -------------------------------------
# The KEYED path makes a POSITIVE STATEMENT ABOUT THIS LOG: either "matched N
# open row(s)" or "no STATE: dispatched row in this log carries that token".
# Both of those are only true if the log was actually scanned. The scanner is
# awk. If awk cannot run, an uncounted result is "could not count", NOT
# "counted zero" — and asserting the latter writes a false claim into an
# append-only ledger, which is the exact class of failure this pair exists to
# prevent. So a missing matcher drops to the UNKEYED path, which claims
# nothing about any row and says why. Caught by the awk-absent probe in
# scripts/tests/test-dispatch-log-close.sh (case I10), not by inspection.
if [ -n "$TOKEN" ]; then
  if ! awk 'BEGIN { exit 0 }' </dev/null >/dev/null 2>&1; then
    TOKEN=""
    REASON="matcher-unavailable"
  fi
fi

# --- ensure the log exists (mirrors the writer's own init) --------------
LOGDIR=$(dirname "$LOG" 2>/dev/null)
[ -n "$LOGDIR" ] && mkdir -p "$LOGDIR" 2>/dev/null
if [ ! -f "$LOG" ]; then
  echo "# DISPATCH LOG" >> "$LOG" 2>/dev/null
fi

# --- append-only newline guard ------------------------------------------
# If the log does not end in a newline, a bare `>>` append FUSES the new row
# onto the last existing row. That silently alters a row this script is
# forbidden to touch, and it hides that row from every `STATE: dispatched$`
# matcher, so it can never be closed again. Appending one newline byte is
# itself strictly append-only: it adds a byte, it never rewrites content.
# `$(...)` strips trailing newlines, so this yields "" iff the last byte is
# already a newline.
if [ -s "$LOG" ] && [ -n "$(tail -c 1 "$LOG" 2>/dev/null)" ]; then
  printf '\n' >> "$LOG" 2>/dev/null
fi

# =========================================================================
# KEYED mode: TOKEN is present and non-empty.
# =========================================================================
if [ -n "$TOKEN" ]; then

  # Idempotency: has ANY closing row already recorded an outcome for this
  # exact token? (Covers both the matched and the unmatched-token outcome —
  # either way, this token has already been dispositioned once.)
  #
  # FIELD-ANCHORED, not substring, and not merely boundary-anchored.
  # History of this one line, both defects real:
  #   1. `grep -F "corr=abc"` also matched a row carrying `corr=abcdef`, so a
  #      closing row for the LONGER token falsely satisfied this check for a
  #      genuinely different spawn and silently suppressed its close.
  #   2. Boundary anchoring fixed that but still matched corr= ANYWHERE on the
  #      line, including inside WHO: — which is fed from agent_type. That is
  #      attack (a) in the gate note above: any row whose WHO: carried
  #      "corr=<victim>" satisfied this check for the victim.
  # So the lookup is now pinned to the FIELD that legitimately carries the
  # token, per row variant. Two variants carry a corr for a token, and they do
  # NOT agree on where:
  #   STATE: closed                -> corr= in WHY: and in WHERE: (WHERE: is
  #                                   exactly "WHERE: closes corr=<tok>")
  #   STATE: closed@unmatched-token-> corr= in WHY: ONLY; its WHERE: is the
  #                                   fixed "n/a - no row is claimed closed".
  # Anchoring to WHERE: alone would therefore silently lose idempotency for
  # the unmatched-token variant and let it append a second row on every retry,
  # so both anchors are checked. NF==7 is itself an anchor: a value that
  # forged a " | " would shift every field index, and such a row is refused
  # rather than counted. All 117 rows of the live ledger are exactly 7 fields
  # (measured 2026-07-28), so this rejects forgeries, not real history.
  # The token is passed through the environment, not `awk -v`, because -v
  # applies escape-sequence processing to its value; ENVIRON does not.
  ALREADY=$(DLC_TOK="$TOKEN" awk -F ' \\| ' '
    BEGIN { tok = ENVIRON["DLC_TOK"] }
    NF == 7 && $7 ~ /^STATE: closed/ {
      if ($4 == "WHERE: closes corr=" tok) { n++ }
      else if (index($3, "WHY: SubagentStop carried corr=" tok " ") == 1) { n++ }
    }
    END { print n + 0 }
  ' "$LOG" 2>/dev/null)
  # awk does not run END if it cannot open the file, so an empty result means
  # "could not count", not "counted zero". Fall back to 0 (append an honest
  # row) rather than to no-op (silently swallow the stop).
  [ -n "$ALREADY" ] || ALREADY=0

  if [ "${ALREADY:-0}" != "0" ]; then
    diag "idempotent no-op: corr=$TOKEN already has a closing row"
  else
    # How many open (STATE: dispatched) rows carry this exact token?
    # FIELD-ANCHORED — see the note on ALREADY above. With a plain substring
    # match, closing `corr=abc` counted a DIFFERENT, still-running `corr=abcdef`
    # spawn as matched and appended a row asserting "matched 2 open row(s)",
    # which a reader takes as both being accounted for. That is a false claim
    # written into an append-only ledger. And with a merely line-wide match, a
    # WHO: field carrying "corr=<tok>" counted as an open row.
    # An open row is written by exactly one thing — dispatch-log-writeahead.sh
    # — and its WHERE: is "session <sha>" with " corr=<tok>" appended, so the
    # token is required to be the SUFFIX of WHERE: (space-anchored on the left,
    # end-of-field on the right) on a 7-field row whose STATE: is exactly
    # "dispatched". Nothing in WHO:, WHAT:, WHY:, WHEN: or HOW: can satisfy it.
    MATCHES=$(DLC_TOK="$TOKEN" awk -F ' \\| ' '
      BEGIN { suf = " corr=" ENVIRON["DLC_TOK"]; sl = length(suf) }
      NF == 7 && $7 == "STATE: dispatched" && index($4, "WHERE: session ") == 1 &&
      length($4) > sl && substr($4, length($4) - sl + 1) == suf { n++ }
      END { print n + 0 }
    ' "$LOG" 2>/dev/null)
    MATCHES="${MATCHES:-0}"

    if [ "$MATCHES" = "0" ]; then
      # Token present, but nothing open carries it. Never guess which row
      # this was. Record the miss honestly, make no closing claim.
      echo "- [$TS] WHO: $AGENT | WHAT: subagent stop recorded, no open row matched | WHY: SubagentStop carried corr=$TOKEN but no STATE: dispatched row in this log carries that token (already reconciled, writer patch not in effect for that spawn, or token mismatch) | WHERE: n/a - no row is claimed closed | WHEN: stop | HOW: KEYED - token present, lookup miss | STATE: closed@unmatched-token" >> "$LOG"
    else
      # One or more open rows carry this exact token. All of them describe
      # the same spawn instance the token identifies (a duplicate write-ahead
      # row is still about the one spawn that token names) so closing all of
      # them under one row is a true statement of the count, not a guess
      # about which one "really" ended.
      echo "- [$TS] WHO: $AGENT | WHAT: subagent closed | WHY: hook-recorded at SubagentStop, keyed close for corr=$TOKEN, matched $MATCHES open row(s) | WHERE: closes corr=$TOKEN | WHEN: stop | HOW: KEYED - matched via CORR_JQ token | STATE: closed" >> "$LOG"
    fi
  fi

else
  # =======================================================================
  # UNKEYED mode: no usable correlation token (reason in $REASON).
  # Conservative behaviour: NEVER guess which open row this stop belongs to.
  # Record that an unattributed stop occurred, and nothing more. This does
  # not resolve any specific STATE: dispatched row — it cannot, honestly —
  # so those rows remain exactly as open as they were before this ran. That
  # is a pre-existing gap (no correlation data available), not a new one
  # created here.
  # =======================================================================
  [ -n "$REASON" ] || REASON="unknown"

  # Idempotency key: since there is no token, hash the raw payload bytes.
  # Two hook firings for the very same stop event will carry byte-identical
  # stdin, so this still dedupes correctly for repeat invocations of a
  # single event. It cannot distinguish two genuinely different UNKEYED
  # stop events whose payloads happen to be byte-identical (documented
  # limitation, not silently assumed away).
  HASH=$(printf '%s' "$INPUT" | cksum 2>/dev/null | awk '{print $1"-"$2}')
  [ -n "$HASH" ] || HASH="nohash-$$"

  # FIELD-ANCHORED for the same reason as the KEYED lookup above. A bare
  # `grep -F "key=$HASH"` matched the hash ANYWHERE on the line, so an
  # agent_type containing "key=<hash of the victim payload>" landed that
  # string in WHO: and permanently suppressed a later, genuinely different
  # UNKEYED close (attack (c) in the gate note). The only field that
  # legitimately carries this key is HOW:, in the fixed shape
  # "HOW: UNKEYED - reason=<reason>, key=<hash>", so the hash is required to
  # be the suffix of HOW: after ", key=" on a 7-field closing row.
  # Anchoring on the ", key=" suffix rather than on the whole HOW: string is
  # deliberate: $REASON is not purely a function of the payload (jq-missing
  # depends on PATH), so the same event re-fired under a different PATH must
  # still dedupe on its payload hash.
  ALREADY=$(DLC_HASH="$HASH" awk -F ' \\| ' '
    BEGIN { suf = ", key=" ENVIRON["DLC_HASH"]; sl = length(suf) }
    NF == 7 && $7 ~ /^STATE: closed/ && index($6, "HOW: UNKEYED - reason=") == 1 &&
    length($6) > sl && substr($6, length($6) - sl + 1) == suf { n++ }
    END { print n + 0 }
  ' "$LOG" 2>/dev/null)
  # See the note on the KEYED ALREADY: empty means "could not count".
  [ -n "$ALREADY" ] || ALREADY=0

  if [ "${ALREADY:-0}" != "0" ]; then
    diag "idempotent no-op: key=$HASH already has a closing row"
  else
    echo "- [$TS] WHO: $AGENT | WHAT: subagent stop recorded, correlation unavailable | WHY: no usable correlation token ($REASON) - no claim made about which open row this closes | WHERE: n/a - no row is claimed closed | WHEN: stop | HOW: UNKEYED - reason=$REASON, key=$HASH | STATE: closed@unattributed" >> "$LOG"
  fi
fi

exit 0
