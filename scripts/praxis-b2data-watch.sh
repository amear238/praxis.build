#!/bin/bash
# praxis-b2data-watch.sh — Praxis_build-3q4 (b2-data-mailbox)
# VM<->Mac shared-folder mailbox watcher + raw-landing validation daemon.
#
# Clone of praxis-signals-sweep-daemon.sh: a persistent KeepAlive launchd job
# that loops a sweep. This is a NEW, INDEPENDENT daemon (label
# build.praxis.b2data-watch) — it does NOT touch the live signal-path daemons
# (build.praxis.signals-*). Interval 15s (data landing is not latency-sensitive).
#
# Runtime deployment: SOURCE ONLY in the repo. praxis-b2data-watch-install.sh
# COPIES this + b2data_raw_validate.py + notify.sh to the internal disk
# (~/Library/Application Support/Praxis/bin) and the plist ProgramArguments point
# there — macOS TCC blocks launchd from executing scripts on the external volume
# /Volumes/Sensidine. Data/state/report dirs live on the internal disk.
#
# Per-sweep behaviour (design §2.2):
#   1. new STABLE csv in raw/  -> landing-log + notify "landed <f> (N/44)"
#   2. first stable *_daily.csv -> OI-check; OI blank/zero -> loud STOP notice
#   3. inbound/status.txt mtime changed -> relay its contents (no human relay)
#   4. completion (44/44 stable OR _EXPORT-COMPLETE) -> full raw-landing battery
#      -> write reports/raw-landing-validation.md + notify the SUMMARY line
#
# Resilience: notify.sh (Telegram) is BEST-EFFORT (token rotation open). Every
# notification is ALSO written to reports/landing-log.txt FIRST, so the system
# works fully with Telegram down; a notify failure never crashes the sweep.
#
# Idempotency: a seen-files state file notifies each file exactly once; a
# settle-guard (size unchanged across two consecutive sweeps) never parses a
# half-written CSV; a completion signature notifies each complete-state once.
#
# Overrides (also used by scripts/tests/b2data-watch-selftest.sh):
#   PRAXIS_B2DATA_ROOT       mailbox root (default ~/praxis-signals/b2-data)
#   PRAXIS_B2DATA_STATE      state dir    (default ~/.praxis/state)
#   PRAXIS_NOTIFY            notifier     (default <script dir>/notify.sh)
#   PRAXIS_B2DATA_VALIDATOR  validator    (default <script dir>/b2data_raw_validate.py)
#   PRAXIS_B2DATA_INTERVAL   loop seconds (default 15)
# Arg `once` runs a single sweep and exits (used by the self-test).
set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="${PRAXIS_B2DATA_ROOT:-$HOME/praxis-signals/b2-data}"
STATE_DIR="${PRAXIS_B2DATA_STATE:-$HOME/.praxis/state}"
NOTIFY="${PRAXIS_NOTIFY:-$SCRIPT_DIR/notify.sh}"
VALIDATOR="${PRAXIS_B2DATA_VALIDATOR:-$SCRIPT_DIR/b2data_raw_validate.py}"
INTERVAL="${PRAXIS_B2DATA_INTERVAL:-15}"

RAW="$ROOT/raw"
REPORTS="$ROOT/reports"
INBOUND="$ROOT/inbound"
OUTBOUND="$ROOT/outbound"
LOG="$REPORTS/landing-log.txt"
SEEN="$STATE_DIR/b2data-seen.txt"
SIZES="$STATE_DIR/b2data-sizes.txt"
STATUS_MTIME="$STATE_DIR/b2data-status-mtime.txt"
COMPLETION_SIG="$STATE_DIR/b2data-completion.txt"

# 22 contracts x 2 files = 44 expected.
CONTRACTS="06-21 09-21 12-21 03-22 06-22 09-22 12-22 03-23 06-23 09-23 12-23 03-24 06-24 09-24 12-24 03-25 06-25 09-25 12-25 03-26 06-26 09-26"

ts() { date -u +%Y-%m-%dT%H:%M:%SZ; }

fsize() { stat -f%z "$1" 2>/dev/null || stat -c%s "$1" 2>/dev/null || echo 0; }
fmtime() { stat -f%m "$1" 2>/dev/null || stat -c%Y "$1" 2>/dev/null || echo 0; }

log_line() { printf '%s %s\n' "$(ts)" "$*" >> "$LOG" 2>/dev/null || true; }

# notify_and_log: write the notification to the durable log FIRST (guaranteed),
# THEN attempt best-effort Telegram. A notify failure must NEVER crash the sweep.
notify_and_log() {
  local event="$1"; shift
  local msg="$*"
  log_line "$msg"
  "$NOTIFY" "$event" "$msg" >/dev/null 2>&1 || true
}

count_present() {
  local n=0 c
  for c in $CONTRACTS; do
    [ -f "$RAW/NQ-${c}_1min.csv" ]  && n=$((n+1))
    [ -f "$RAW/NQ-${c}_daily.csv" ] && n=$((n+1))
  done
  echo "$n"
}

process_new_file() {
  local f="$1" base="$2"
  local present; present="$(count_present)"
  notify_and_log b2data-landed "landed $base ($present/44)"
  case "$base" in
    *_daily.csv)
      local oi; oi="$(python3 "$VALIDATOR" --oi-file "$f" 2>/dev/null)"
      case "$oi" in
        OI_BLANK*)
          notify_and_log b2data-oi-stop "OI BLANK — STOP: $base has blank/zero Open Interest. Volume-only crossover fallback needs trader sign-off + a DECISIONS entry (D-2026-07-17-A OPEN RISK) BEFORE use. [$oi]"
          ;;
        OI_PRESENT*)
          notify_and_log b2data-oi-ok "OI present in $base [$oi]"
          ;;
      esac
      ;;
  esac
}

# status.txt relay: notify once per mtime change (idempotent across sweeps).
check_status_change() {
  local sf="$INBOUND/status.txt"
  [ -f "$sf" ] || return 0
  local m prev
  m="$(fmtime "$sf")"
  prev="$(cat "$STATUS_MTIME" 2>/dev/null || echo '')"
  [ "$m" = "$prev" ] && return 0
  echo "$m" > "$STATUS_MTIME" 2>/dev/null || true
  local content
  content="$(tr '\n' ' ' < "$sf" 2>/dev/null | cut -c1-400)"
  # skip an empty status (e.g. the initial seed) — nothing to relay.
  [ -n "${content// /}" ] || return 0
  notify_and_log b2data-status "coworker status.txt update: $content"
}

# completion battery: fire once per distinct complete-state (44/44 stable OR the
# _EXPORT-COMPLETE marker). A signature over (present-count, marker, seen-set)
# de-dupes so an unchanged raw/ never re-notifies.
check_completion() {
  local present; present="$(count_present)"
  local marker=""
  [ -f "$RAW/_EXPORT-COMPLETE" ] && marker="1"
  if [ "$present" -lt 44 ] && [ -z "$marker" ]; then
    return 0
  fi
  local sig prevsig
  sig="present=$present marker=${marker:-0} seen=$(sort "$SEEN" 2>/dev/null | tr '\n' ',')"
  prevsig="$(cat "$COMPLETION_SIG" 2>/dev/null || echo '')"
  [ "$sig" = "$prevsig" ] && return 0
  echo "$sig" > "$COMPLETION_SIG" 2>/dev/null || true
  local summary
  summary="$(PRAXIS_B2DATA_ROOT="$ROOT" python3 "$VALIDATOR" --root "$ROOT" 2>/dev/null | grep -m1 '^SUMMARY')"
  notify_and_log b2data-validation "raw-landing validation complete: ${summary:-SUMMARY unavailable} (report: reports/raw-landing-validation.md)"
}

sweep() {
  mkdir -p "$RAW" "$REPORTS" "$INBOUND" "$OUTBOUND" "$STATE_DIR" 2>/dev/null || true
  touch "$SEEN" 2>/dev/null || true

  local newsizes="$STATE_DIR/.b2data-sizes.tmp.$$"
  : > "$newsizes" 2>/dev/null || true

  shopt -s nullglob
  local f base cur prev
  for f in "$RAW"/*.csv; do
    base="$(basename "$f")"
    cur="$(fsize "$f")"
    printf '%s\t%s\n' "$base" "$cur" >> "$newsizes" 2>/dev/null || true

    # already notified? -> skip (idempotency)
    grep -qxF "$base" "$SEEN" 2>/dev/null && continue
    # empty/not-yet-written -> skip
    [ "$cur" -gt 0 ] 2>/dev/null || continue
    # settle-guard: require a previous size AND size unchanged since last sweep
    prev="$(awk -F'\t' -v n="$base" '$1==n{print $2}' "$SIZES" 2>/dev/null)"
    [ -n "$prev" ] || continue          # first sighting -> wait one sweep
    [ "$prev" = "$cur" ] || continue     # still growing -> wait
    # STABLE + NEW -> act exactly once
    process_new_file "$f" "$base"
    echo "$base" >> "$SEEN" 2>/dev/null || true
  done
  shopt -u nullglob

  mv -f "$newsizes" "$SIZES" 2>/dev/null || rm -f "$newsizes" 2>/dev/null || true

  check_status_change
  check_completion
}

if [ "${1:-}" = "once" ]; then
  sweep
  exit 0
fi

echo "$(ts) b2data-watch start pid=$$ root=$ROOT interval=${INTERVAL}s"
trap 'echo "$(ts) b2data-watch stop pid=$$"; exit 0' TERM INT

while :; do
  sweep || true
  sleep "$INTERVAL" &
  wait $! || true
done
