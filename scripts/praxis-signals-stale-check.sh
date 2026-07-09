#!/bin/bash
# praxis-signals-stale-check.sh — B1-c (Praxis_build-dnt)
# Fires a Telegram alert (via .claude/hooks/notify.sh -> ORCH_N8N_WEBHOOK) when the
# signals-sweep heartbeat goes stale (sweep job died / Mac paused / volume unmounted).
#
# Secrets: ORCH_N8N_WEBHOOK is NOT hardcoded. launchd agents do not inherit an
# interactive shell env, so this script sources an optional, git-ignored env file
# (~/.praxis/signals.env) to pick up ORCH_N8N_WEBHOOK. If neither the env file nor
# the ambient env provides it, notify.sh no-ops (the alert path is then structural
# only — documented in the B1-c report).
#
# A latch file (.stale-alerted) prevents alert-spam: one alert per stale episode;
# cleared automatically once the heartbeat recovers.
set -uo pipefail

# Runtime deployment: this script is COPIED to ~/Library/Application Support/Praxis/bin/
# (internal disk) alongside notify.sh — the repo scripts/ are SOURCE ONLY because macOS
# TCC blocks launchd from executing scripts on the external volume /Volumes/Sensidine.
# Default NOTIFY resolves to notify.sh next to this script's deployed location (never the
# external volume). Override with PRAXIS_NOTIFY for source-tree testing.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

DROP="${PRAXIS_DROP:-/Users/admin/praxis-signals}"
HEARTBEAT="$DROP/.heartbeat"
THRESHOLD="${PRAXIS_HEARTBEAT_THRESHOLD:-180}"
NOTIFY="${PRAXIS_NOTIFY:-$SCRIPT_DIR/notify.sh}"
ENV_FILE="${PRAXIS_ENV_FILE:-$HOME/.praxis/signals.env}"
LATCH="$DROP/.stale-alerted"

# Pull ORCH_N8N_WEBHOOK (and optional CLAUDE_PROJECT_DIR) from the git-ignored env file.
if [ -f "$ENV_FILE" ]; then
  set -a; . "$ENV_FILE"; set +a
fi

now=$(date +%s)
if [ -f "$HEARTBEAT" ]; then
  hb=$(cat "$HEARTBEAT" 2>/dev/null || echo 0)
  case "$hb" in ''|*[!0-9]*) hb=0;; esac
  age=$(( now - hb ))
else
  age=999999
fi

if [ "$age" -gt "$THRESHOLD" ]; then
  if [ ! -f "$LATCH" ]; then
    "$NOTIFY" praxis-signals-stale "signals-sweep heartbeat stale: ${age}s > ${THRESHOLD}s threshold (heartbeat=$HEARTBEAT)" || true
    date +%s > "$LATCH" 2>/dev/null || true
  fi
else
  rm -f "$LATCH" 2>/dev/null || true
fi
exit 0
