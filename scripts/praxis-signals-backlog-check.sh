#!/bin/bash
# praxis-signals-backlog-check.sh — F-B1e-1 (Praxis_build-22r)
# Fires a Telegram alert (via .claude/hooks/notify.sh -> ORCH_N8N_WEBHOOK) when signal
# files pile up UN-PROMOTED in the sweep's staging/outbox dirs — the "silent loss" gap
# found by the B1-e offline drill.
#
# WHY THIS EXISTS (the gap it closes):
#   The sweep relays OUTBOX/*.json -> DROP/incoming (rsync) -> mv incoming/*.json -> DROP/.
#   That final `mv` needs WRITE on the DROP dir itself; the heartbeat write only needs
#   write on the (already-existing) .heartbeat FILE. So when DROP is dir-unwritable
#   (chmod 500 / VM share offline) the mv fails, files pile up in DROP/incoming, yet the
#   heartbeat stays FRESH -> the stale-check NEVER fires and NT8 silently stops receiving
#   signals. This detector watches the BACKLOG directly, independent of heartbeat
#   semantics, so a promotion failure is always visible.
#
# STUCK measured by ctime, not mtime: `rsync -a` PRESERVES the source mtime, so a file's
# mtime reflects when n8n first wrote it (misleading). ctime is set to "now" whenever the
# inode is created/moved and cannot be back-dated by userland, so ctime is the true
# "arrived in this dir" time — exactly the age we want ("how long has it been stuck here").
#
# LATCH + LOG LIVE IN DROP/logs, NOT DROP: during the exact failure this detects, the DROP
# dir is unwritable, so a latch at DROP/.backlog-alerted could not be created. DROP/logs
# (and DROP/incoming) keep their own 755 perms and stay writable — the latch/log go there.
#
# Secrets: ORCH_N8N_WEBHOOK is NOT hardcoded. launchd agents get no interactive shell env,
# so this sources the optional git-ignored ~/.praxis/signals.env. If neither the file nor
# the ambient env provides it, notify.sh no-ops (alert path structural-only).
#
# A latch (.backlog-alerted) prevents alert-spam: one alert per backlog episode; cleared —
# with an optional recovery note — once the backlog drains.
set -uo pipefail

# Runtime deployment: COPIED to ~/Library/Application Support/Praxis/bin/ (internal disk)
# alongside notify.sh — repo scripts/ are SOURCE ONLY (macOS TCC blocks launchd from
# executing scripts on the external volume /Volumes/Sensidine). Default NOTIFY resolves to
# notify.sh next to this script's deployed location. Override with PRAXIS_NOTIFY for
# source-tree testing.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

DROP="${PRAXIS_DROP:-/Users/admin/praxis-signals}"
INCOMING="$DROP/incoming"
OUTBOX="${PRAXIS_OUTBOX:-/Users/admin/n8n-compose/local-files/outbox}"
# Long enough that a healthy sweep (WatchPaths ~1-2s, 60s backstop) has always drained the
# staging dir; short enough to alert fast. Paired with a 30s launchd interval -> worst-case
# detection ~= THRESHOLD + interval (~90s).
THRESHOLD="${PRAXIS_BACKLOG_THRESHOLD:-60}"
NOTIFY="${PRAXIS_NOTIFY:-$SCRIPT_DIR/notify.sh}"
ENV_FILE="${PRAXIS_ENV_FILE:-$HOME/.praxis/signals.env}"
# Latch + durable trail live in DROP/logs (stays writable when DROP itself is chmod 500).
LATCH="${PRAXIS_BACKLOG_LATCH:-$DROP/logs/.backlog-alerted}"
ALERT_LOG="${PRAXIS_ALERT_LOG:-$DROP/logs/signals-alerts.log}"

# Pull ORCH_N8N_WEBHOOK (and optional CLAUDE_PROJECT_DIR) from the git-ignored env file.
if [ -f "$ENV_FILE" ]; then
  set -a; . "$ENV_FILE"; set +a
fi

now=$(date +%s)

# Scan un-promoted signal files in staging (incoming) and source (outbox). The globs are
# iterated DIRECTLY (not via an intermediate array): macOS ships bash 3.2, where an empty
# array expansion "${arr[@]}" trips `set -u` ("unbound variable"). With nullglob, a
# no-match glob expands to nothing so the loop simply runs zero times — no unbound trap.
# *.json excludes rsync temp dotfiles, so half-written files are never counted.
stuck=0
oldest_age=0
oldest_file=""
shopt -s nullglob
for f in "$INCOMING"/*.json "$OUTBOX"/*.json; do
  ct=$(stat -f %c "$f" 2>/dev/null || echo "$now")
  case "$ct" in ''|*[!0-9]*) ct=$now;; esac
  age=$(( now - ct ))
  if [ "$age" -gt "$THRESHOLD" ]; then
    stuck=$(( stuck + 1 ))
    if [ "$age" -gt "$oldest_age" ]; then oldest_age=$age; oldest_file="$f"; fi
  fi
done
shopt -u nullglob

if [ "$stuck" -gt 0 ]; then
  if [ ! -f "$LATCH" ]; then
    "$NOTIFY" praxis-signals-backlog \
      "STUCK BACKLOG: ${stuck} signal file(s) un-promoted >${THRESHOLD}s (oldest ${oldest_age}s: ${oldest_file}) — sweep relay/promotion FAILING, NT8 not receiving signals; check DROP dir writability ($DROP)" || true
    fired=$(date +%s)
    mkdir -p "$(dirname "$LATCH")" 2>/dev/null || true
    echo "$fired" > "$LATCH" 2>/dev/null || true
    # Durable local evidence (append-only; failure-tolerant). The n8n execution id is NOT
    # available here (notify.sh discards the curl response); the authoritative send-side
    # proof is the n8n execution — this line is the durable local trail.
    fired_utc=$(date -u -r "$fired" +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || date -u +%Y-%m-%dT%H:%M:%SZ)
    mkdir -p "$(dirname "$ALERT_LOG")" 2>/dev/null || true
    printf 'BACKLOG ALERT FIRED %s (%s) stuck=%s threshold=%ss oldest=%ss file=%s\n' \
      "$fired" "$fired_utc" "$stuck" "$THRESHOLD" "$oldest_age" "$oldest_file" >> "$ALERT_LOG" 2>/dev/null || true
  fi
else
  # Backlog drained. If we had alerted, clear the latch and send a recovery note.
  if [ -f "$LATCH" ]; then
    "$NOTIFY" praxis-signals-backlog-recovered \
      "RECOVERED: signal backlog cleared — sweep relay/promotion healthy again ($DROP)" || true
    rm -f "$LATCH" 2>/dev/null || true
    rec=$(date +%s)
    rec_utc=$(date -u -r "$rec" +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || date -u +%Y-%m-%dT%H:%M:%SZ)
    printf 'BACKLOG RECOVERED %s (%s)\n' "$rec" "$rec_utc" >> "$ALERT_LOG" 2>/dev/null || true
  fi
fi
exit 0
