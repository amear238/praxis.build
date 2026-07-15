#!/bin/bash
# praxis-inbound-control-watch.sh — Praxis_build-10i
# Telegram -> Claude inbound CONTROL CHANNEL runner (host side of the n8n file-drop).
#
# AUTHORITY (LOCKED — DECISION_LOG 2026-07-15T21:10Z, design §5 Option A):
#   READ / REPORT / STATUS ONLY. The only repo/state mutation possible through this
#   channel is toward LESS autonomy (pause/stop a run). No write, no commit, no
#   credential access, NO free-form prompt / arbitrary shell. Every verb maps to a
#   FIXED argv command below — there is deliberately NO `claude -p` passthrough, so
#   the LLM-prompt-injection surface described in the design sketch does not exist.
#
# FLOW (reuses the B1-c signals-sweep + notify.sh discipline wholesale):
#   n8n Telegram Trigger  (GUARD 1: sender allowlist)  writes
#     /Users/admin/n8n-compose/local-files/tg-inbox/cmd-<update_id>.json  (.tmp->rename)
#   -> launchd build.praxis.tg-inbound (WatchPaths + 60s poll) runs THIS script
#   -> claim file -> guards 2..5 -> fixed read-only action -> reply via notify.sh
#   -> notify.sh -> ORCH_N8N_WEBHOOK -> n8n orchestrator-notify -> Telegram reply.
#
# Message text is DATA ONLY: parsed with python3 (json), matched against an exact
# verb allowlist, never string-interpolated into a shell line.
#
# DEPLOYMENT (macOS TCC): this file is SOURCE ONLY. scripts/praxis-inbound-control-
# install.sh COPIES it (+ notify.sh) to ~/Library/Application Support/Praxis/bin
# (internal disk) and the plist ProgramArguments point THERE — launchd cannot exec
# scripts on the external volume /Volumes/Sensidine ("Operation not permitted").
# Override any path via env for source-tree testing (see defaults below).
set -uo pipefail

# ---- config / paths (all overridable via env for testing) -------------------
ENV_FILE="${PRAXIS_ENV_FILE:-$HOME/.praxis/signals.env}"
[ -f "$ENV_FILE" ] && . "$ENV_FILE" 2>/dev/null || true

REPO_DIR="${PRAXIS_REPO:-/Volumes/Sensidine/Praxis.build}"
INBOX="${PRAXIS_TG_INBOX:-/Users/admin/n8n-compose/local-files/tg-inbox}"
TG_DIR="${PRAXIS_TG_DIR:-/Users/admin/praxis-tg}"
WORK="$TG_DIR/work"; DONE="$TG_DIR/done"; FAILED="$TG_DIR/failed"
LOGS="$TG_DIR/logs"; CONTROL="$TG_DIR/control"
PROCESSED="$TG_DIR/processed-ids"          # dedupe ledger (append-only update_ids)
RATE_LEDGER="$TG_DIR/logs/rate.ledger"     # epoch seconds of recent EXECs
AUDIT="$LOGS/inbound-audit.log"            # append-only, OUTSIDE the repo
DISABLED="$TG_DIR/DISABLED"                # kill switch (layer a)
LOCKDIR="$TG_DIR/.runner.lock.d"           # mkdir-based lock (macOS has no flock)
LOCK_STALE_SECS="${PRAXIS_TG_LOCK_STALE_SECS:-300}"

# Sender allowlist (chat_id is NOT a secret — the outbound Telegram node already
# carries it literally; kept in signals.env so both ids live in one 0600 file).
TRADER_CHAT_ID="${PRAXIS_TG_CHAT_ID:-6156528469}"
TRADER_FROM_ID="${PRAXIS_TG_FROM_ID:-6156528469}"

STALE_SECS="${PRAXIS_TG_STALE_SECS:-900}"  # §6.9 reject steering older than 15 min
RATE_MAX="${PRAXIS_TG_RATE_MAX:-6}"        # §6.4 max EXEC/min
REPLY_MAX="${PRAXIS_TG_REPLY_MAX:-3200}"   # Telegram-friendly reply truncation
BD="${PRAXIS_BD:-bd}"
NOTIFY="${PRAXIS_NOTIFY:-$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/notify.sh}"

mkdir -p "$WORK" "$DONE" "$FAILED" "$LOGS" "$CONTROL" "$INBOX" 2>/dev/null || true
touch "$PROCESSED" 2>/dev/null || true

now_utc() { date -u +%Y-%m-%dT%H:%M:%SZ; }

audit() { # <update_id> <from_id> <verdict> <verb> <exit> <reply-bytes>
  printf '%s %s %s %s %s %s %s\n' "$(now_utc)" "${1:--}" "${2:--}" "${3:-?}" "${4:--}" "${5:--}" "${6:-0}" \
    >> "$AUDIT" 2>/dev/null || true
}

reply() { # <text> -> Telegram via notify.sh; echoes byte count
  local text="$1"
  [ ${#text} -gt "$REPLY_MAX" ] && text="${text:0:$REPLY_MAX}
...[truncated]"
  "$NOTIFY" "tg-reply" "$text" >/dev/null 2>&1 || true
  printf '%s' "${#text}"
}

# ---- kill switch (layer a) --------------------------------------------------
if [ -f "$DISABLED" ]; then
  audit - - DISABLED - - 0
  exit 0
fi

# ---- single-flight lock (§6.4; mkdir is atomic — macOS has no flock) --------
if ! mkdir "$LOCKDIR" 2>/dev/null; then
  # Reap a stale lock left by a crashed runner, then retry once.
  if [ -d "$LOCKDIR" ]; then
    lock_age=$(( $(date +%s) - $(stat -f %m "$LOCKDIR" 2>/dev/null || stat -c %Y "$LOCKDIR" 2>/dev/null || echo 0) ))
    if [ "$lock_age" -gt "$LOCK_STALE_SECS" ]; then
      rmdir "$LOCKDIR" 2>/dev/null || true
      mkdir "$LOCKDIR" 2>/dev/null || exit 0
    else
      exit 0    # another runner is draining; that one handles the queue
    fi
  else
    exit 0
  fi
fi
trap 'rmdir "$LOCKDIR" 2>/dev/null || true' EXIT

# ---- rate limiter helper (§6.4) --------------------------------------------
rate_ok() {
  local nows cutoff cnt=0 line
  nows=$(date +%s); cutoff=$((nows - 60))
  if [ -f "$RATE_LEDGER" ]; then
    # keep only entries within the last 60s
    awk -v c="$cutoff" '$1 >= c' "$RATE_LEDGER" > "$RATE_LEDGER.tmp" 2>/dev/null && mv -f "$RATE_LEDGER.tmp" "$RATE_LEDGER"
    cnt=$(wc -l < "$RATE_LEDGER" 2>/dev/null | tr -d ' ')
  fi
  [ "${cnt:-0}" -lt "$RATE_MAX" ]
}
rate_note() { date +%s >> "$RATE_LEDGER" 2>/dev/null || true; }

# ---- fixed read-only ACTION TABLE (allowlist) -------------------------------
# Each verb -> a deterministic argv command run with cwd=REPO_DIR. No verb takes a
# free-form argument (Option A). Output captured; never mutates the repo.
run_action() { # <verb> ; sets ACTION_OUT / returns exit code
  local verb="$1"
  case "$verb" in
    bead|current)
      ACTION_OUT=$(cd "$REPO_DIR" && "$BD" list --status in_progress 2>&1); return $? ;;
    ready)
      ACTION_OUT=$(cd "$REPO_DIR" && "$BD" ready 2>&1); return $? ;;
    status|run)
      # Read-only autonomous-run status from .claude/state (no writes).
      local st="$REPO_DIR/.claude/state" active mode iter max readyc
      if [ -f "$st/orchestrator-active" ]; then active="ACTIVE"; else active="idle"; fi
      mode=$(cat "$st/run-mode" 2>/dev/null || echo "-")
      iter=$(cat "$st/iteration-count" 2>/dev/null || echo 0)
      max=$(cat "$st/max-iterations" 2>/dev/null || echo "-")
      readyc=$(cd "$REPO_DIR" && "$BD" ready 2>/dev/null | grep -c '^○\|^◐\|Praxis_build-' 2>/dev/null || echo "?")
      ACTION_OUT="run: $active mode=$mode iter=$iter/$max ready-beads=$readyc"; return 0 ;;
    pause)
      : > "$CONTROL/PAUSE" 2>/dev/null
      ACTION_OUT="PAUSE flag set ($CONTROL/PAUSE). An in-flight autonomous run stops requesting the next bead at its next stop-gate; already-dispatched work finishes."
      return 0 ;;
    stop)
      : > "$CONTROL/STOP" 2>/dev/null
      ACTION_OUT="STOP flag set ($CONTROL/STOP). The autonomous loop will not continue past its current step. Remove the flag to resume."
      return 0 ;;
    help)
      ACTION_OUT="PRAXIS inbound (read/report/status only). Commands: bead | ready | status | run | pause | stop | help"
      return 0 ;;
    *)
      ACTION_OUT="unknown command: '$verb' — allowed: bead ready status run pause stop help"
      return 127 ;;
  esac
}

# ---- process one claimed command file --------------------------------------
process_file() { # <path-in-work>
  local f="$1" json uid cid fid text ts verb rc rb parsed
  json=$(cat "$f" 2>/dev/null)

  # GUARD: parse JSON (data only). Emits: update_id|chat_id|from_id|ts|text
  parsed=$(printf '%s' "$json" | python3 -c '
import json,sys
try:
    d=json.load(sys.stdin)
    uid=d.get("update_id"); cid=d.get("chat_id"); fid=d.get("from_id")
    ts=d.get("ts",""); text=(d.get("text") or "")
    if uid is None or cid is None or fid is None:
        print("__BADFIELDS__"); sys.exit(0)
    # first whitespace token only; strip anything non [a-z0-9] to a safe verb
    verb=text.strip().split()[0].lower() if text.strip() else ""
    import re
    verb=re.sub(r"[^a-z0-9]","",verb)
    print("\t".join([str(uid),str(cid),str(fid),str(ts),verb]))
except Exception:
    print("__BADJSON__")
' 2>/dev/null)

  if [ "$parsed" = "__BADJSON__" ] || [ "$parsed" = "__BADFIELDS__" ] || [ -z "$parsed" ]; then
    rb=$(reply "REJECTED: unparseable command")
    audit - - ERROR - 1 "$rb"
    mv -f "$f" "$FAILED/" 2>/dev/null || true
    return 0
  fi

  uid=$(printf '%s' "$parsed" | cut -f1)
  cid=$(printf '%s' "$parsed" | cut -f2)
  fid=$(printf '%s' "$parsed" | cut -f3)
  ts=$(printf  '%s' "$parsed" | cut -f4)
  verb=$(printf '%s' "$parsed" | cut -f5)

  # GUARD 2: sender allowlist re-check (defense in depth; host never trusts n8n)
  if [ "$cid" != "$TRADER_CHAT_ID" ] || [ "$fid" != "$TRADER_FROM_ID" ]; then
    rb=$(reply "REJECTED: unauthorized sender ($fid/$cid)")
    audit "$uid" "$fid" REJECT - 1 "$rb"
    mv -f "$f" "$FAILED/" 2>/dev/null || true
    return 0
  fi

  # GUARD 3: dedupe on update_id
  if grep -qxF "$uid" "$PROCESSED" 2>/dev/null; then
    audit "$uid" "$fid" DEDUPE "$verb" 0 0
    mv -f "$f" "$DONE/" 2>/dev/null || true
    return 0
  fi

  # GUARD 4: staleness window
  if [ -n "$ts" ]; then
    local msg_epoch nows age
    msg_epoch=$(python3 -c 'import sys,datetime
try:
    print(int(datetime.datetime.fromisoformat(sys.argv[1].replace("Z","+00:00")).timestamp()))
except Exception:
    print(-1)' "$ts" 2>/dev/null)
    nows=$(date +%s)
    if [ "${msg_epoch:-*-1}" -gt 0 ] 2>/dev/null; then
      age=$((nows - msg_epoch))
      if [ "$age" -gt "$STALE_SECS" ]; then
        echo "$uid" >> "$PROCESSED"
        rb=$(reply "REJECTED: stale command (${age}s old > ${STALE_SECS}s); not replaying steering after a backlog/sleep")
        audit "$uid" "$fid" STALE "$verb" 1 "$rb"
        mv -f "$f" "$DONE/" 2>/dev/null || true
        return 0
      fi
    fi
  fi

  # GUARD 5: rate limit (only counts real EXEC; rejects above don't burn budget)
  if ! rate_ok; then
    mv -f "$f" "$INBOX/" 2>/dev/null || true   # defer, not drop (§6.4)
    audit "$uid" "$fid" DEFER "$verb" 0 0
    return 1   # signal caller to stop draining this wake
  fi

  # ---- execute fixed action ----
  ACTION_OUT=""
  run_action "$verb"; rc=$?
  echo "$uid" >> "$PROCESSED"
  rate_note

  if [ "$verb" != "bead" ] && [ "$verb" != "current" ] && [ "$verb" != "ready" ] \
     && [ "$verb" != "status" ] && [ "$verb" != "run" ] && [ "$verb" != "pause" ] \
     && [ "$verb" != "stop" ] && [ "$verb" != "help" ]; then
    rb=$(reply "REJECTED: $ACTION_OUT")
    audit "$uid" "$fid" REJECT "${verb:--}" "$rc" "$rb"
    mv -f "$f" "$DONE/" 2>/dev/null || true
    return 0
  fi

  rb=$(reply "$verb -> $ACTION_OUT")
  audit "$uid" "$fid" EXEC "$verb" "$rc" "$rb"
  mv -f "$f" "$DONE/" 2>/dev/null || true
  return 0
}

# ---- drain: claim oldest cmd-*.json, process, repeat ------------------------
shopt -s nullglob
# oldest first by name (cmd-<monotonic update_id>.json sorts chronologically)
for src in $(ls -1 "$INBOX"/cmd-*.json 2>/dev/null | sort); do
  [ -f "$src" ] || continue
  claimed="$WORK/$(basename "$src")"
  mv -f "$src" "$claimed" 2>/dev/null || continue   # atomic claim
  process_file "$claimed" || break                  # break on rate-limit defer
done
shopt -u nullglob
exit 0
