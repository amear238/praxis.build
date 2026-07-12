#!/bin/bash
# praxis-signals-sweep-daemon.sh — 8xf (D-2026-07-12-A)
# Persistent KeepAlive daemon: runs the existing sweep script in a 1s loop.
# Replaces the WatchPaths-triggered launch of build.praxis.signals-sweep —
# launchd's 10s minimum-runtime throttle delayed WatchPaths respawns under
# bursts, blowing the <5s webhook->incoming budget
# (docs/reports/2026-07-12-8xf-latency-investigation.md). A persistent process
# never respawns per event, so the throttle never applies; relay leg is bounded
# at ~1.3s (1s sleep + sweep time).
#
# Sweep logic and heartbeat/stale-check semantics live UNCHANGED in
# praxis-signals-sweep.sh (invoked as a child each iteration). The heartbeat now
# refreshes every ~1s, so the existing stale-check (180s threshold) also catches
# a HUNG daemon, which KeepAlive alone cannot.
#
# Exits 0 only on SIGTERM/SIGINT (launchctl bootout / kill). Any other death is
# restarted by launchd KeepAlive=true (worst case one 10s throttle penalty on a
# crash-loop — accepted in D-2026-07-12-A).
#
# Runtime deployment: this script is COPIED to ~/Library/Application Support/
# Praxis/bin/ (internal disk) by scripts/praxis-signals-install.sh — the repo
# scripts/ are SOURCE ONLY because macOS TCC blocks launchd from executing
# scripts on the external volume /Volumes/Sensidine. Override PRAXIS_SWEEP /
# PRAXIS_SWEEP_INTERVAL for source-tree testing.
set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SWEEP="${PRAXIS_SWEEP:-$SCRIPT_DIR/praxis-signals-sweep.sh}"
INTERVAL="${PRAXIS_SWEEP_INTERVAL:-1}"

echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) sweep-daemon start pid=$$ sweep=$SWEEP interval=${INTERVAL}s"

trap 'echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) sweep-daemon stop pid=$$"; exit 0' TERM INT

while :; do
  # Sweep is itself failure-tolerant (set -uo, no -e; every step || true);
  # never let one bad iteration kill the daemon.
  "$SWEEP" || true
  # Background sleep + wait so SIGTERM interrupts the nap immediately instead
  # of being deferred until the foreground sleep finishes.
  sleep "$INTERVAL" &
  wait $! || true
done
