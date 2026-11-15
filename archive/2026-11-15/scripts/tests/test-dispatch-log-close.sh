#!/bin/bash
# Self-contained test harness for scripts/dispatch-log-close.sh
# (Praxis_build-43n). Every fixture is created under mktemp -d and pointed
# to via PRAXIS_DISPATCH_LOG. This suite NEVER writes to the real
# DISPATCH_LOG.md in the repo.
set -u

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

# Scripts under test are resolved from the environment, DEFAULTING to the repo
# copies, so default behaviour is unchanged. The override exists so the FAILING
# pre-fix baseline stays reproducible on demand rather than surviving only as a
# captured log:
#   CLOSER_BIN=/path/to/dispatch-log-close.sh.PRISTINE \
#   WRITER_BIN=/path/to/dispatch-log-writeahead.sh.PRISTINE \
#     ./scripts/tests/test-dispatch-log-close.sh
CLOSER="${CLOSER_BIN:-$REPO_ROOT/scripts/dispatch-log-close.sh}"
WRITER="${WRITER_BIN:-$REPO_ROOT/scripts/dispatch-log-writeahead.sh}"

PASS=0
FAIL=0
FAILED_NAMES=()

note() { echo "    $*"; }

pass() {
  PASS=$((PASS + 1))
  echo "PASS - $1"
}

fail() {
  FAIL=$((FAIL + 1))
  FAILED_NAMES+=("$1")
  echo "FAIL - $1"
  shift
  for line in "$@"; do note "$line"; done
}

new_fixture_dir() {
  mktemp -d "${TMPDIR:-/tmp}/dlc-test.XXXXXX"
}

# run_closer <log_path> <stdin_payload> [extra_path_prepend]
# sets globals: RC (exit code), OUT (stdout), ERR (stderr)
run_closer() {
  local log="$1" payload="$2" pathoverride="${3:-}"
  local errfile
  errfile=$(mktemp "${TMPDIR:-/tmp}/dlc-test.err.XXXXXX")
  if [ -n "$pathoverride" ]; then
    OUT=$(printf '%s' "$payload" | PRAXIS_DISPATCH_LOG="$log" PATH="$pathoverride" /opt/homebrew/bin/bash "$CLOSER" 2>"$errfile")
  else
    OUT=$(printf '%s' "$payload" | PRAXIS_DISPATCH_LOG="$log" /opt/homebrew/bin/bash "$CLOSER" 2>"$errfile")
  fi
  RC=$?
  ERR=$(cat "$errfile")
  rm -f "$errfile"
}

# run_writer <log_path> <stdin_payload>
# Same contract as run_closer. CLAUDE_PROJECT_DIR is pinned to the fixture dir
# (not a git repo) so the WHERE: sha component is deterministically "no-git"
# and the writer can never be pointed at the real ledger by accident.
run_writer() {
  local log="$1" payload="$2"
  local errfile
  errfile=$(mktemp "${TMPDIR:-/tmp}/dlc-test.err.XXXXXX")
  OUT=$(printf '%s' "$payload" \
    | PRAXIS_DISPATCH_LOG="$log" CLAUDE_PROJECT_DIR="$(dirname "$log")" \
      /opt/homebrew/bin/bash "$WRITER" 2>"$errfile")
  RC=$?
  ERR=$(cat "$errfile")
  rm -f "$errfile"
}

count_lines_matching() {
  # count_lines_matching <file> <fixed-string>
  grep -F "$2" "$1" 2>/dev/null | wc -l | tr -d ' '
}

linecount() { wc -l < "$1" 2>/dev/null | tr -d ' '; }

last_line() { tail -n 1 "$1" 2>/dev/null; }

pipe_count() {
  # pipe_count <string> -> number of '|' characters
  printf '%s' "$1" | tr -cd '|' | wc -c | tr -d ' '
}

who_field() {
  # who_field <line> -> the WHO: value, i.e. field 1 after "] "
  printf '%s' "$1" | sed -e 's/ | .*$//' -e 's/^.*] WHO: //'
}

# The fixed literal the gate substitutes for a refused agent_type. Must match
# the literal in BOTH scripts.
REJECT_LITERAL='agent-type-rejected-unsafe'

# -------------------------------------------------------------------------
echo "=== test-dispatch-log-close.sh ==="
echo "CLOSER: $CLOSER"
echo "WRITER: $WRITER"
echo

# make_tool_farm <dir> <tool>...
# Builds an isolated PATH containing ONLY the named tools, for the
# "dependency X is missing" cases.
#
# Uses `type -P`, NOT `command -v`. `command -v grep` returns the bare word
# "grep" when grep is a shell FUNCTION — which it is under Claude Code's shell
# snapshot on this machine (`type -a grep` => "grep is a shell function from
# .../shell-snapshots/snapshot-zsh-*.sh"). The old code then ran
# `ln -s grep <farm>/grep`, producing a symlink pointing at itself: the farm
# silently lacked grep, so a case labelled "jq absent" was really testing
# "jq AND grep absent" and nobody could tell. `type -P` searches PATH for an
# executable file only and skips functions, builtins and aliases.
#
# Every link is then verified to resolve. A farm that is missing a tool it
# claimed to provide is a SETUP FAILURE, announced loudly, never silent —
# a test that passes because the environment was wrong is worse than no test.
make_tool_farm() {
  local dir="$1"; shift
  local tool real missing=""
  for tool in "$@"; do
    real=$(type -P "$tool" 2>/dev/null)
    if [ -n "$real" ] && [ -x "$real" ]; then
      ln -s "$real" "$dir/$tool"
      [ -x "$dir/$tool" ] || missing="$missing $tool(broken-link)"
    else
      missing="$missing $tool(unresolved)"
    fi
  done
  if [ -n "$missing" ]; then
    echo "SETUP FAILURE: tool farm $dir could not provide:$missing" >&2
    return 1
  fi
  return 0
}

# --- fixture for a jq-absent PATH (symlink farm, deliberately missing jq) -
NOJQ_BIN=$(mktemp -d "${TMPDIR:-/tmp}/dlc-test.nojq.XXXXXX")
make_tool_farm "$NOJQ_BIN" awk tr cksum git wc sed mktemp cat date mkdir grep tail dirname
# Sanity: jq must NOT be resolvable from this isolated PATH.
if PATH="$NOJQ_BIN" command -v jq >/dev/null 2>&1; then
  echo "SETUP FAILURE: jq is still visible inside the isolated no-jq PATH; aborting jq test setup." >&2
fi
# Sanity: everything else the closer needs MUST be resolvable, or the case
# is testing the wrong absence.
for t in awk grep tr wc cksum; do
  PATH="$NOJQ_BIN" command -v "$t" >/dev/null 2>&1 \
    || echo "SETUP FAILURE: $t is NOT visible inside the no-jq PATH; case 8 would be testing the wrong thing." >&2
done

# =========================================================================
# Case 1: clean KEYED close
# =========================================================================
D1=$(new_fixture_dir)
LOG1="$D1/DISPATCH_LOG.md"
cat > "$LOG1" <<'EOF'
# DISPATCH LOG
- [2026-07-28T10:00:00Z] WHO: praxis-worker | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session abc1234 corr=TOKEN-CASE1 | WHEN: spawn | HOW: awaiting terminal state | STATE: dispatched
EOF
run_closer "$LOG1" '{"agent_id":"TOKEN-CASE1","agent_type":"praxis-worker","hook_event_name":"SubagentStop"}'
CLOSED=$(count_lines_matching "$LOG1" 'STATE: closed')
if [ "$RC" -eq 0 ] && [ "$CLOSED" = "1" ] && grep -qF 'corr=TOKEN-CASE1' "$LOG1" && grep -qE '\| STATE: closed$' "$LOG1"; then
  pass "1 clean KEYED close appends exactly one closed row"
else
  fail "1 clean KEYED close appends exactly one closed row" "rc=$RC closed_rows=$CLOSED" "$(cat "$LOG1")"
fi

# Idempotency: run the SAME stop payload again, must not add a second closing row.
run_closer "$LOG1" '{"agent_id":"TOKEN-CASE1","agent_type":"praxis-worker","hook_event_name":"SubagentStop"}'
CLOSED2=$(count_lines_matching "$LOG1" 'STATE: closed')
if [ "$RC" -eq 0 ] && [ "$CLOSED2" = "1" ]; then
  pass "1b KEYED close is idempotent (second run adds no row)"
else
  fail "1b KEYED close is idempotent (second run adds no row)" "rc=$RC closed_rows_after_second_run=$CLOSED2" "$(cat "$LOG1")"
fi

# =========================================================================
# Case 2: UNKEYED path (no agent_id field at all in the stop payload)
# =========================================================================
D2=$(new_fixture_dir)
LOG2="$D2/DISPATCH_LOG.md"
cat > "$LOG2" <<'EOF'
# DISPATCH LOG
- [2026-07-28T10:00:00Z] WHO: praxis-master | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session abc1234 | WHEN: spawn | HOW: awaiting terminal state | STATE: dispatched
EOF
PAYLOAD2='{"agent_type":"praxis-master","hook_event_name":"SubagentStop"}'
run_closer "$LOG2" "$PAYLOAD2"
if [ "$RC" -eq 0 ] && grep -qE '\| STATE: closed@unattributed$' "$LOG2" && ! grep -q 'STATE: closed$' "$LOG2"; then
  pass "2 UNKEYED stop (no agent_id) closes with closed@unattributed, claims no specific row"
else
  fail "2 UNKEYED stop (no agent_id) closes with closed@unattributed, claims no specific row" "rc=$RC" "$(cat "$LOG2")"
fi
UNATTR_BEFORE=$(count_lines_matching "$LOG2" 'STATE: closed@unattributed')
run_closer "$LOG2" "$PAYLOAD2"
UNATTR_AFTER=$(count_lines_matching "$LOG2" 'STATE: closed@unattributed')
if [ "$RC" -eq 0 ] && [ "$UNATTR_BEFORE" = "1" ] && [ "$UNATTR_AFTER" = "1" ]; then
  pass "2b UNKEYED close is idempotent for byte-identical repeat stdin"
else
  fail "2b UNKEYED close is idempotent for byte-identical repeat stdin" "rc=$RC before=$UNATTR_BEFORE after=$UNATTR_AFTER" "$(cat "$LOG2")"
fi

# =========================================================================
# Case 3: log file missing entirely
# =========================================================================
D3=$(new_fixture_dir)
LOG3="$D3/nested/does-not-exist/DISPATCH_LOG.md"
[ ! -e "$LOG3" ] || fail "3 setup sanity" "fixture unexpectedly pre-existed"
run_closer "$LOG3" '{"agent_type":"praxis-worker","hook_event_name":"SubagentStop"}'
if [ "$RC" -eq 0 ] && [ -f "$LOG3" ] && grep -qE '\| STATE: closed@unattributed$' "$LOG3"; then
  pass "3 missing log file: created, exit 0, honest unattributed close appended"
else
  fail "3 missing log file: created, exit 0, honest unattributed close appended" "rc=$RC exists=$([ -f "$LOG3" ] && echo yes || echo no)" "$(cat "$LOG3" 2>&1)"
fi

# =========================================================================
# Case 4: log file exists, header only, zero open rows -- KEYED payload
# =========================================================================
D4=$(new_fixture_dir)
LOG4="$D4/DISPATCH_LOG.md"
echo "# DISPATCH LOG" > "$LOG4"
run_closer "$LOG4" '{"agent_id":"TOKEN-CASE4","agent_type":"praxis-worker","hook_event_name":"SubagentStop"}'
if [ "$RC" -eq 0 ] && grep -qE '\| STATE: closed@unmatched-token$' "$LOG4" && ! grep -qE '\| STATE: closed$' "$LOG4"; then
  pass "4 zero open rows + KEYED token: honest unmatched-token close, no false claim"
else
  fail "4 zero open rows + KEYED token: honest unmatched-token close, no false claim" "rc=$RC" "$(cat "$LOG4")"
fi

# =========================================================================
# Case 5: malformed / truncated row mixed into the log
# =========================================================================
D5=$(new_fixture_dir)
LOG5="$D5/DISPATCH_LOG.md"
cat > "$LOG5" <<'EOF'
# DISPATCH LOG
this line is not a dispatch row at all
- [BROKEN TIMESTAMP WHO praxis-worker no pipes no schema
- [2026-07-28T10:00:00Z] WHO: praxis-worker | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session abc1234 corr=TOKEN-CASE5 | WHEN: spawn | HOW: awaiting terminal state | STATE: dispatched
EOF
run_closer "$LOG5" '{"agent_id":"TOKEN-CASE5","agent_type":"praxis-worker","hook_event_name":"SubagentStop"}'
if [ "$RC" -eq 0 ] && grep -qE '\| STATE: closed$' "$LOG5" && grep -qF 'matched 1 open row' "$LOG5"; then
  pass "5 malformed/truncated row present: script does not crash, still matches the one real open row"
else
  fail "5 malformed/truncated row present: script does not crash, still matches the one real open row" "rc=$RC" "$(cat "$LOG5")"
fi

# =========================================================================
# Case 6: correlation token present but matches no open row (distinct from
# case 4 -- here there IS an open row, just for a different token)
# =========================================================================
D6=$(new_fixture_dir)
LOG6="$D6/DISPATCH_LOG.md"
cat > "$LOG6" <<'EOF'
# DISPATCH LOG
- [2026-07-28T10:00:00Z] WHO: praxis-worker | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session abc1234 corr=SOME-OTHER-TOKEN | WHEN: spawn | HOW: awaiting terminal state | STATE: dispatched
EOF
run_closer "$LOG6" '{"agent_id":"TOKEN-NOT-PRESENT","agent_type":"praxis-worker","hook_event_name":"SubagentStop"}'
if [ "$RC" -eq 0 ] && grep -qE '\| STATE: closed@unmatched-token$' "$LOG6" && ! grep -qE '\| STATE: closed$' "$LOG6"; then
  pass "6 token present, matches no open row: honest miss, open row for SOME-OTHER-TOKEN left untouched"
else
  fail "6 token present, matches no open row: honest miss, open row for SOME-OTHER-TOKEN left untouched" "rc=$RC" "$(cat "$LOG6")"
fi
# Confirm append-only: the original open row must be byte-identical still present.
ORIG_ROW6='- [2026-07-28T10:00:00Z] WHO: praxis-worker | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session abc1234 corr=SOME-OTHER-TOKEN | WHEN: spawn | HOW: awaiting terminal state | STATE: dispatched'
if grep -qF -- "$ORIG_ROW6" "$LOG6"; then
  pass "6b original open row is untouched (append-only honoured)"
else
  fail "6b original open row is untouched (append-only honoured)" "$(cat "$LOG6")"
fi

# =========================================================================
# Case 7: multiple open rows share the same correlation token
# =========================================================================
D7=$(new_fixture_dir)
LOG7="$D7/DISPATCH_LOG.md"
cat > "$LOG7" <<'EOF'
# DISPATCH LOG
- [2026-07-28T10:00:00Z] WHO: praxis-worker | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session abc1234 corr=DUPTOKEN | WHEN: spawn | HOW: awaiting terminal state | STATE: dispatched
- [2026-07-28T10:00:01Z] WHO: praxis-worker | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session abc1234 corr=DUPTOKEN | WHEN: spawn | HOW: awaiting terminal state | STATE: dispatched
EOF
run_closer "$LOG7" '{"agent_id":"DUPTOKEN","agent_type":"praxis-worker","hook_event_name":"SubagentStop"}'
CLOSEROWS7=$(count_lines_matching "$LOG7" 'STATE: closed')
if [ "$RC" -eq 0 ] && [ "$CLOSEROWS7" = "1" ] && grep -qF 'matched 2 open row(s)' "$LOG7"; then
  pass "7 multiple open rows same token: one closing row, honestly states matched=2 (no per-row guess)"
else
  fail "7 multiple open rows same token: one closing row, honestly states matched=2 (no per-row guess)" "rc=$RC closing_rows=$CLOSEROWS7" "$(cat "$LOG7")"
fi

# =========================================================================
# Case 8: jq absent (isolated PATH with no jq resolvable at all)
# =========================================================================
D8=$(new_fixture_dir)
LOG8="$D8/DISPATCH_LOG.md"
cat > "$LOG8" <<'EOF'
# DISPATCH LOG
- [2026-07-28T10:00:00Z] WHO: praxis-worker | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session abc1234 corr=TOKEN-CASE8 | WHEN: spawn | HOW: awaiting terminal state | STATE: dispatched
EOF
run_closer "$LOG8" '{"agent_id":"TOKEN-CASE8","agent_type":"praxis-worker","hook_event_name":"SubagentStop"}' "$NOJQ_BIN"
if [ "$RC" -eq 0 ] && grep -qF 'reason=jq-missing' "$LOG8" && grep -qE '\| STATE: closed@unattributed$' "$LOG8"; then
  pass "8 jq absent from PATH: falls back to UNKEYED reason=jq-missing, exit 0, no crash"
else
  fail "8 jq absent from PATH: falls back to UNKEYED reason=jq-missing, exit 0, no crash" "rc=$RC" "$(cat "$LOG8")" "err=$ERR"
fi

# =========================================================================
# Case 9: empty stdin
# =========================================================================
D9=$(new_fixture_dir)
LOG9="$D9/DISPATCH_LOG.md"
echo "# DISPATCH LOG" > "$LOG9"
run_closer "$LOG9" ''
if [ "$RC" -eq 0 ] && grep -qF 'reason=empty-stdin' "$LOG9"; then
  pass "9 empty stdin: exit 0, recorded as UNKEYED reason=empty-stdin"
else
  fail "9 empty stdin: exit 0, recorded as UNKEYED reason=empty-stdin" "rc=$RC" "$(cat "$LOG9")"
fi

# =========================================================================
# Case 10: non-JSON stdin
# =========================================================================
D10=$(new_fixture_dir)
LOG10="$D10/DISPATCH_LOG.md"
echo "# DISPATCH LOG" > "$LOG10"
run_closer "$LOG10" 'this is not json at all { [ garbage'
if [ "$RC" -eq 0 ] && grep -qF 'reason=non-json-stdin' "$LOG10"; then
  pass "10 non-JSON stdin: exit 0, recorded as UNKEYED reason=non-json-stdin"
else
  fail "10 non-JSON stdin: exit 0, recorded as UNKEYED reason=non-json-stdin" "rc=$RC" "$(cat "$LOG10")"
fi

# #########################################################################
# INJECTION CLASS (I*) — agent_type is attacker-influenced and was read RAW
# by both halves of the pair while its sibling agent_id was gated.
#
# These cases were written to FAIL against the pre-fix scripts and are kept
# as regressions. Reproduce the failing baseline at any time with:
#   CLOSER_BIN=<pristine closer> WRITER_BIN=<pristine writer> \
#     ./scripts/tests/test-dispatch-log-close.sh
# #########################################################################

OPEN_ROW_PREFIX='WHAT: subagent spawned | WHY: hook-recorded at SubagentStart'

# =========================================================================
# I1: single-line agent_type carrying "corr=<victim>" must not silently
# deny the victim its own genuine close. NO NEWLINE IS NEEDED for this: the
# substring lands in WHO: on a row that already ends "| STATE:
# closed@unattributed", which satisfies the closer's own idempotency test.
# =========================================================================
DI1=$(new_fixture_dir)
LOGI1="$DI1/DISPATCH_LOG.md"
cat > "$LOGI1" <<EOF
# DISPATCH LOG
- [2026-07-28T10:00:00Z] WHO: praxis-worker | $OPEN_ROW_PREFIX | WHERE: session abc1234 corr=VICTIM1 | WHEN: spawn | HOW: awaiting terminal state | STATE: dispatched
EOF
# Attacker stop: no agent_id at all (UNKEYED), token smuggled through agent_type.
run_closer "$LOGI1" '{"agent_type":"x corr=VICTIM1","hook_event_name":"SubagentStop"}'
RC_I1_ATTACK=$RC
# Victim's own, genuine, keyed stop.
run_closer "$LOGI1" '{"agent_id":"VICTIM1","agent_type":"praxis-worker","hook_event_name":"SubagentStop"}'
HONEST_I1=$(grep -cE '\| WHERE: closes corr=VICTIM1 \| WHEN: stop \| HOW: KEYED - matched via CORR_JQ token \| STATE: closed$' "$LOGI1" | tr -d ' ')
if [ "$RC_I1_ATTACK" -eq 0 ] && [ "$RC" -eq 0 ] && [ "$HONEST_I1" = "1" ]; then
  pass "I1 agent_type carrying corr=<victim> does not suppress the victim's genuine keyed close"
else
  fail "I1 agent_type carrying corr=<victim> does not suppress the victim's genuine keyed close" \
    "rc_attack=$RC_I1_ATTACK rc_victim=$RC honest_keyed_close_rows=$HONEST_I1 (want 1)" "$(cat "$LOGI1")"
fi
if ! grep -qF 'WHO: x corr=VICTIM1' "$LOGI1"; then
  pass "I1b hostile agent_type is not written verbatim into the ledger"
else
  fail "I1b hostile agent_type is not written verbatim into the ledger" "$(cat "$LOGI1")"
fi

# =========================================================================
# I2: agent_type with an embedded newline crafted so one of the resulting
# physical lines ends "| STATE: dispatched" — a forged open row for a spawn
# that never happened, visible to the closer's own matcher.
# =========================================================================
NL_PAYLOAD_CLOSER='{"agent_type":"x\n- [2026-01-01T00:00:00Z] WHO: ghost | WHAT: forged open row | WHY: injected via agent_type | WHERE: session deadbee corr=FORGED2 | WHEN: spawn | HOW: none | STATE: dispatched\ntrailer","hook_event_name":"SubagentStop"}'
DI2=$(new_fixture_dir)
LOGI2="$DI2/DISPATCH_LOG.md"
echo "# DISPATCH LOG" > "$LOGI2"
BEFORE_I2=$(linecount "$LOGI2")
run_closer "$LOGI2" "$NL_PAYLOAD_CLOSER"
AFTER_I2=$(linecount "$LOGI2")
DELTA_I2=$((AFTER_I2 - BEFORE_I2))
FORGED_I2=$(grep -cE '\| STATE: dispatched$' "$LOGI2" | tr -d ' ')
if [ "$RC" -eq 0 ] && [ "$DELTA_I2" = "1" ] && [ "$FORGED_I2" = "0" ] && ! grep -qF 'corr=FORGED2' "$LOGI2"; then
  pass "I2 closer: newline in agent_type appends exactly ONE physical line and forges no open row"
else
  fail "I2 closer: newline in agent_type appends exactly ONE physical line and forges no open row" \
    "rc=$RC lines_appended=$DELTA_I2 (want 1) forged_dispatched_rows=$FORGED_I2 (want 0)" "$(cat "$LOGI2")"
fi

# =========================================================================
# I3: same embedded-newline payload through the WRITER half of the pair.
# =========================================================================
NL_PAYLOAD_WRITER='{"agent_id":"WRITERI3","agent_type":"x\n- [2026-01-01T00:00:00Z] WHO: ghost | WHAT: forged open row | WHY: injected via agent_type | WHERE: session deadbee corr=FORGED3 | WHEN: spawn | HOW: none | STATE: dispatched\ntrailer","hook_event_name":"SubagentStart"}'
DI3=$(new_fixture_dir)
LOGI3="$DI3/DISPATCH_LOG.md"
echo "# DISPATCH LOG" > "$LOGI3"
BEFORE_I3=$(linecount "$LOGI3")
run_writer "$LOGI3" "$NL_PAYLOAD_WRITER"
AFTER_I3=$(linecount "$LOGI3")
DELTA_I3=$((AFTER_I3 - BEFORE_I3))
PIPES_I3=$(pipe_count "$(last_line "$LOGI3")")
DISPATCHED_I3=$(grep -cE '\| STATE: dispatched$' "$LOGI3" | tr -d ' ')
if [ "$RC" -eq 0 ] && [ "$DELTA_I3" = "1" ] && [ "$PIPES_I3" = "6" ] && [ "$DISPATCHED_I3" = "1" ] && ! grep -qF 'corr=FORGED3' "$LOGI3"; then
  pass "I3 writer: newline in agent_type appends exactly ONE physical line with exactly 6 pipes"
else
  fail "I3 writer: newline in agent_type appends exactly ONE physical line with exactly 6 pipes" \
    "rc=$RC lines_appended=$DELTA_I3 (want 1) pipes=$PIPES_I3 (want 6) dispatched_rows=$DISPATCHED_I3 (want 1)" "$(cat "$LOGI3")"
fi

# =========================================================================
# I4: agent_type carrying "key=<hash>" must not poison the UNKEYED
# idempotency check and suppress a later, genuinely different UNKEYED close.
# =========================================================================
DI4=$(new_fixture_dir)
LOGI4="$DI4/DISPATCH_LOG.md"
echo "# DISPATCH LOG" > "$LOGI4"
VICTIM_PAYLOAD_I4='{"agent_type":"praxis-worker","hook_event_name":"SubagentStop","session_id":"victim-i4"}'
VICTIM_HASH_I4=$(printf '%s' "$VICTIM_PAYLOAD_I4" | cksum | awk '{print $1"-"$2}')
run_closer "$LOGI4" "{\"agent_type\":\"x key=$VICTIM_HASH_I4\",\"hook_event_name\":\"SubagentStop\",\"session_id\":\"attacker-i4\"}"
RC_I4_ATTACK=$RC
run_closer "$LOGI4" "$VICTIM_PAYLOAD_I4"
VICTIM_ROWS_I4=$(grep -cF "HOW: UNKEYED - reason=token-absent, key=$VICTIM_HASH_I4 | STATE: closed@unattributed" "$LOGI4" | tr -d ' ')
if [ "$RC_I4_ATTACK" -eq 0 ] && [ "$RC" -eq 0 ] && [ "$VICTIM_ROWS_I4" = "1" ]; then
  pass "I4 agent_type carrying key=<hash> does not suppress a later distinct UNKEYED close"
else
  fail "I4 agent_type carrying key=<hash> does not suppress a later distinct UNKEYED close" \
    "rc_attack=$RC_I4_ATTACK rc_victim=$RC victim_rows=$VICTIM_ROWS_I4 (want 1) victim_hash=$VICTIM_HASH_I4" "$(cat "$LOGI4")"
fi

# =========================================================================
# I5: agent_type containing '|' forges field boundaries. The row must stay
# at exactly 6 pipes / 7 fields in BOTH halves of the pair.
# =========================================================================
PIPE_AGENT='evil | WHAT: forged | WHY: forged'
DI5=$(new_fixture_dir)
LOGI5="$DI5/DISPATCH_LOG.md"
echo "# DISPATCH LOG" > "$LOGI5"
run_closer "$LOGI5" "{\"agent_type\":\"$PIPE_AGENT\",\"hook_event_name\":\"SubagentStop\"}"
PIPES_I5A=$(pipe_count "$(last_line "$LOGI5")")
WHO_I5A=$(who_field "$(last_line "$LOGI5")")
if [ "$RC" -eq 0 ] && [ "$PIPES_I5A" = "6" ] && [ "$WHO_I5A" = "$REJECT_LITERAL" ]; then
  pass "I5a closer: '|' in agent_type - appended row still has exactly 6 pipes, WHO: shows refusal"
else
  fail "I5a closer: '|' in agent_type - appended row still has exactly 6 pipes, WHO: shows refusal" \
    "rc=$RC pipes=$PIPES_I5A (want 6) who=[$WHO_I5A] (want [$REJECT_LITERAL])" "$(cat "$LOGI5")"
fi
DI5B=$(new_fixture_dir)
LOGI5B="$DI5B/DISPATCH_LOG.md"
echo "# DISPATCH LOG" > "$LOGI5B"
run_writer "$LOGI5B" "{\"agent_id\":\"WRITERI5\",\"agent_type\":\"$PIPE_AGENT\",\"hook_event_name\":\"SubagentStart\"}"
PIPES_I5B=$(pipe_count "$(last_line "$LOGI5B")")
WHO_I5B=$(who_field "$(last_line "$LOGI5B")")
if [ "$RC" -eq 0 ] && [ "$PIPES_I5B" = "6" ] && [ "$WHO_I5B" = "$REJECT_LITERAL" ]; then
  pass "I5b writer: '|' in agent_type - appended row still has exactly 6 pipes, WHO: shows refusal"
else
  fail "I5b writer: '|' in agent_type - appended row still has exactly 6 pipes, WHO: shows refusal" \
    "rc=$RC pipes=$PIPES_I5B (want 6) who=[$WHO_I5B] (want [$REJECT_LITERAL])" "$(cat "$LOGI5B")"
fi

# =========================================================================
# I6: degenerate agent_type values. Over the length cap must be REFUSED
# (distinct literal); empty / absent / JSON null must degrade to "unknown".
# The two literals must stay distinguishable: a reader has to be able to
# tell "no agent_type was supplied" from "an agent_type was refused".
# =========================================================================
LONG_AGENT=$(printf 'A%.0s' $(seq 1 100))
DI6=$(new_fixture_dir)
LOGI6="$DI6/DISPATCH_LOG.md"
echo "# DISPATCH LOG" > "$LOGI6"
run_closer "$LOGI6" "{\"agent_type\":\"$LONG_AGENT\",\"hook_event_name\":\"SubagentStop\"}"
WHO_I6A=$(who_field "$(last_line "$LOGI6")")
if [ "$RC" -eq 0 ] && [ "$WHO_I6A" = "$REJECT_LITERAL" ]; then
  pass "I6a closer: over-cap agent_type (100 chars) refused, WHO: is the fixed literal, exit 0"
else
  fail "I6a closer: over-cap agent_type (100 chars) refused, WHO: is the fixed literal, exit 0" \
    "rc=$RC who=[$WHO_I6A] (want [$REJECT_LITERAL])" "$(cat "$LOGI6")"
fi
DI6B=$(new_fixture_dir)
LOGI6B="$DI6B/DISPATCH_LOG.md"
echo "# DISPATCH LOG" > "$LOGI6B"
run_writer "$LOGI6B" "{\"agent_id\":\"WRITERI6\",\"agent_type\":\"$LONG_AGENT\",\"hook_event_name\":\"SubagentStart\"}"
WHO_I6B=$(who_field "$(last_line "$LOGI6B")")
if [ "$RC" -eq 0 ] && [ "$WHO_I6B" = "$REJECT_LITERAL" ]; then
  pass "I6b writer: over-cap agent_type (100 chars) refused, WHO: is the fixed literal, exit 0"
else
  fail "I6b writer: over-cap agent_type (100 chars) refused, WHO: is the fixed literal, exit 0" \
    "rc=$RC who=[$WHO_I6B] (want [$REJECT_LITERAL])" "$(cat "$LOGI6B")"
fi
# empty string / absent / JSON null, closer
I6_OK=1
I6_DETAIL=""
for spec in 'empty:{"agent_type":"","hook_event_name":"SubagentStop"}' \
            'absent:{"hook_event_name":"SubagentStop"}' \
            'null:{"agent_type":null,"hook_event_name":"SubagentStop"}'; do
  name="${spec%%:*}"; pl="${spec#*:}"
  d=$(new_fixture_dir); lg="$d/DISPATCH_LOG.md"; echo "# DISPATCH LOG" > "$lg"
  run_closer "$lg" "$pl"
  w=$(who_field "$(last_line "$lg")")
  p=$(pipe_count "$(last_line "$lg")")
  if [ "$RC" -ne 0 ] || [ "$w" != "unknown" ] || [ "$p" != "6" ]; then
    I6_OK=0; I6_DETAIL="$I6_DETAIL [$name rc=$RC who=[$w] pipes=$p]"
  fi
done
if [ "$I6_OK" = "1" ]; then
  pass "I6c closer: empty / absent / JSON-null agent_type all degrade to WHO: unknown, exit 0, 6 pipes"
else
  fail "I6c closer: empty / absent / JSON-null agent_type all degrade to WHO: unknown, exit 0, 6 pipes" "$I6_DETAIL"
fi
# empty string, writer
DI6D=$(new_fixture_dir)
LOGI6D="$DI6D/DISPATCH_LOG.md"
echo "# DISPATCH LOG" > "$LOGI6D"
run_writer "$LOGI6D" '{"agent_id":"WRITERI6D","agent_type":"","hook_event_name":"SubagentStart"}'
WHO_I6D=$(who_field "$(last_line "$LOGI6D")")
if [ "$RC" -eq 0 ] && [ "$WHO_I6D" = "unknown" ]; then
  pass "I6d writer: empty-string agent_type degrades to WHO: unknown (not an empty WHO: field)"
else
  fail "I6d writer: empty-string agent_type degrades to WHO: unknown (not an empty WHO: field)" \
    "rc=$RC who=[$WHO_I6D] (want [unknown])" "$(cat "$LOGI6D")"
fi

# =========================================================================
# I7: REGRESSION GUARD. The fix must not mangle legitimate input. These must
# pass BEFORE and AFTER the fix — they are the control, not the exploit.
# =========================================================================
DI7=$(new_fixture_dir)
LOGI7="$DI7/DISPATCH_LOG.md"
echo "# DISPATCH LOG" > "$LOGI7"
run_closer "$LOGI7" '{"agent_id":"TOKENI7","agent_type":"praxis-worker","hook_event_name":"SubagentStop"}'
WHO_I7A=$(who_field "$(last_line "$LOGI7")")
if [ "$RC" -eq 0 ] && [ "$WHO_I7A" = "praxis-worker" ]; then
  pass "I7a closer: real agent_type 'praxis-worker' still lands verbatim in WHO:"
else
  fail "I7a closer: real agent_type 'praxis-worker' still lands verbatim in WHO:" \
    "rc=$RC who=[$WHO_I7A]" "$(cat "$LOGI7")"
fi
DI7B=$(new_fixture_dir)
LOGI7B="$DI7B/DISPATCH_LOG.md"
echo "# DISPATCH LOG" > "$LOGI7B"
run_writer "$LOGI7B" '{"agent_id":"TOKENI7B","agent_type":"praxis-worker","hook_event_name":"SubagentStart"}'
WHO_I7B=$(who_field "$(last_line "$LOGI7B")")
if [ "$RC" -eq 0 ] && [ "$WHO_I7B" = "praxis-worker" ] && grep -qF 'corr=TOKENI7B' "$LOGI7B"; then
  pass "I7b writer: real agent_type 'praxis-worker' still lands verbatim in WHO:, corr still carried"
else
  fail "I7b writer: real agent_type 'praxis-worker' still lands verbatim in WHO:, corr still carried" \
    "rc=$RC who=[$WHO_I7B]" "$(cat "$LOGI7B")"
fi
# Boundary: exactly 64 chars is AT the cap and must be accepted, not refused.
CAP_AGENT=$(printf 'B%.0s' $(seq 1 64))
DI7C=$(new_fixture_dir)
LOGI7C="$DI7C/DISPATCH_LOG.md"
echo "# DISPATCH LOG" > "$LOGI7C"
run_closer "$LOGI7C" "{\"agent_type\":\"$CAP_AGENT\",\"hook_event_name\":\"SubagentStop\"}"
WHO_I7C=$(who_field "$(last_line "$LOGI7C")")
if [ "$RC" -eq 0 ] && [ "$WHO_I7C" = "$CAP_AGENT" ]; then
  pass "I7c closer: agent_type of exactly 64 chars (at the cap) is accepted verbatim, not refused"
else
  fail "I7c closer: agent_type of exactly 64 chars (at the cap) is accepted verbatim, not refused" \
    "rc=$RC who_len=${#WHO_I7C}" "$(cat "$LOGI7C")"
fi

# =========================================================================
# I8: the closed@unmatched-token variant carries its corr= in WHY: ONLY —
# its WHERE: is the fixed "n/a - no row is claimed closed". Anchoring the
# idempotency lookup to WHERE: alone would silently lose idempotency for
# this variant and append a duplicate on every retry. Guard it explicitly.
# =========================================================================
DI8=$(new_fixture_dir)
LOGI8="$DI8/DISPATCH_LOG.md"
echo "# DISPATCH LOG" > "$LOGI8"
run_closer "$LOGI8" '{"agent_id":"TOKEN-I8","agent_type":"praxis-worker","hook_event_name":"SubagentStop"}'
run_closer "$LOGI8" '{"agent_id":"TOKEN-I8","agent_type":"praxis-worker","hook_event_name":"SubagentStop"}'
UNMATCHED_I8=$(count_lines_matching "$LOGI8" 'STATE: closed@unmatched-token')
if [ "$RC" -eq 0 ] && [ "$UNMATCHED_I8" = "1" ]; then
  pass "I8 closed@unmatched-token stays idempotent (its corr= lives in WHY:, not WHERE:)"
else
  fail "I8 closed@unmatched-token stays idempotent (its corr= lives in WHY:, not WHERE:)" \
    "rc=$RC unmatched_rows=$UNMATCHED_I8 (want 1)" "$(cat "$LOGI8")"
fi

# =========================================================================
# I9: DEFENSE IN DEPTH, independent of the charset gate. These rows are
# seeded DIRECTLY into the fixture, not produced through agent_type, so they
# test the matchers alone: a corr=/key= sitting in a field that does not
# legitimately carry it must not be able to forge a match even if some
# future ungated field lets it through.
# =========================================================================
DI9=$(new_fixture_dir)
LOGI9="$DI9/DISPATCH_LOG.md"
cat > "$LOGI9" <<EOF
# DISPATCH LOG
- [2026-07-28T10:00:00Z] WHO: praxis-worker | $OPEN_ROW_PREFIX | WHERE: session abc1234 corr=VICTIM9 | WHEN: spawn | HOW: awaiting terminal state | STATE: dispatched
- [2026-07-28T10:00:01Z] WHO: praxis-worker | WHAT: note mentioning corr=VICTIM9 | WHY: hand-written reconciliation note | WHERE: n/a - no row is claimed closed | WHEN: stop | HOW: manual | STATE: closed@unattributed
EOF
run_closer "$LOGI9" '{"agent_id":"VICTIM9","agent_type":"praxis-worker","hook_event_name":"SubagentStop"}'
HONEST_I9=$(grep -cE '\| WHERE: closes corr=VICTIM9 \| WHEN: stop \| HOW: KEYED - matched via CORR_JQ token \| STATE: closed$' "$LOGI9" | tr -d ' ')
if [ "$RC" -eq 0 ] && [ "$HONEST_I9" = "1" ]; then
  pass "I9a corr= planted OUTSIDE WHERE:/WHY: cannot forge a keyed-idempotency match"
else
  fail "I9a corr= planted OUTSIDE WHERE:/WHY: cannot forge a keyed-idempotency match" \
    "rc=$RC honest_keyed_close_rows=$HONEST_I9 (want 1)" "$(cat "$LOGI9")"
fi
DI9B=$(new_fixture_dir)
LOGI9B="$DI9B/DISPATCH_LOG.md"
VICTIM_PAYLOAD_I9='{"agent_type":"praxis-worker","hook_event_name":"SubagentStop","session_id":"victim-i9"}'
VICTIM_HASH_I9=$(printf '%s' "$VICTIM_PAYLOAD_I9" | cksum | awk '{print $1"-"$2}')
cat > "$LOGI9B" <<EOF
# DISPATCH LOG
- [2026-07-28T10:00:01Z] WHO: praxis-worker | WHAT: note mentioning key=$VICTIM_HASH_I9 | WHY: hand-written reconciliation note | WHERE: n/a - no row is claimed closed | WHEN: stop | HOW: manual | STATE: closed@unattributed
EOF
run_closer "$LOGI9B" "$VICTIM_PAYLOAD_I9"
VICTIM_ROWS_I9=$(grep -cF "HOW: UNKEYED - reason=token-absent, key=$VICTIM_HASH_I9 | STATE: closed@unattributed" "$LOGI9B" | tr -d ' ')
if [ "$RC" -eq 0 ] && [ "$VICTIM_ROWS_I9" = "1" ]; then
  pass "I9b key= planted OUTSIDE HOW: cannot forge an UNKEYED-idempotency match"
else
  fail "I9b key= planted OUTSIDE HOW: cannot forge an UNKEYED-idempotency match" \
    "rc=$RC victim_rows=$VICTIM_ROWS_I9 (want 1) victim_hash=$VICTIM_HASH_I9" "$(cat "$LOGI9B")"
fi

# =========================================================================
# I10: HONEST DEGRADATION. The row matcher is awk. If awk cannot run, the
# closer must NOT assert "no STATE: dispatched row carries that token" —
# it never looked. Asserting a miss it did not measure is a false claim in
# an append-only ledger. It must drop to the UNKEYED path instead, which
# claims nothing about any row and records why.
#
# This case exists because the awk-based field anchoring INTRODUCED this
# regression: the pre-anchoring code scanned with grep, so an awk-only
# outage produced a false miss that no earlier test would have caught.
# =========================================================================
NOAWK_BIN=$(mktemp -d "${TMPDIR:-/tmp}/dlc-test.noawk.XXXXXX")
make_tool_farm "$NOAWK_BIN" jq tr cksum git wc sed mktemp cat date mkdir grep tail dirname
# awk must be the ONLY thing missing, otherwise this case is not what it says.
if PATH="$NOAWK_BIN" command -v awk >/dev/null 2>&1; then
  echo "SETUP FAILURE: awk is still visible inside the isolated no-awk PATH." >&2
fi
for t in jq grep tr wc; do
  PATH="$NOAWK_BIN" command -v "$t" >/dev/null 2>&1 \
    || echo "SETUP FAILURE: $t is NOT visible inside the no-awk PATH; case I10 would be testing the wrong absence." >&2
done
DI10=$(new_fixture_dir)
LOGI10="$DI10/DISPATCH_LOG.md"
cat > "$LOGI10" <<EOF
# DISPATCH LOG
- [2026-07-28T10:00:00Z] WHO: praxis-worker | $OPEN_ROW_PREFIX | WHERE: session abc1234 corr=NOAWKTOK | WHEN: spawn | HOW: awaiting terminal state | STATE: dispatched
EOF
run_closer "$LOGI10" '{"agent_id":"NOAWKTOK","agent_type":"praxis-worker","hook_event_name":"SubagentStop"}' "$NOAWK_BIN"
FALSE_MISS_I10=$(count_lines_matching "$LOGI10" 'STATE: closed@unmatched-token')
HONEST_I10=$(count_lines_matching "$LOGI10" 'reason=matcher-unavailable')
PIPES_I10=$(pipe_count "$(last_line "$LOGI10")")
if [ "$RC" -eq 0 ] && [ "$FALSE_MISS_I10" = "0" ] && [ "$HONEST_I10" = "1" ] && [ "$PIPES_I10" = "6" ]; then
  pass "I10 awk absent: no false 'no open row matched' claim, degrades to UNKEYED reason=matcher-unavailable"
else
  fail "I10 awk absent: no false 'no open row matched' claim, degrades to UNKEYED reason=matcher-unavailable" \
    "rc=$RC false_miss_rows=$FALSE_MISS_I10 (want 0) honest_rows=$HONEST_I10 (want 1) pipes=$PIPES_I10 (want 6)" "$(cat "$LOGI10")"
fi
rm -rf "$NOAWK_BIN"

# -------------------------------------------------------------------------
rm -rf "$NOJQ_BIN"

echo
echo "=== TALLY: $PASS passed, $FAIL failed (of $((PASS + FAIL)) cases) ==="
if [ "$FAIL" -ne 0 ]; then
  echo "Failed cases:"
  for n in "${FAILED_NAMES[@]}"; do echo "  - $n"; done
  exit 1
fi
exit 0
