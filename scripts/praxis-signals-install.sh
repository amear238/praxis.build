#!/bin/bash
# praxis-signals-install.sh — B1-c (Praxis_build-dnt)
# Idempotent (un)installer for the PRAXIS signals launchd agents.
#
# CRITICAL DEPLOYMENT MODEL (macOS TCC):
#   macOS TCC blocks per-user launchd (gui/$UID) agents from *executing* scripts that
#   live on the EXTERNAL volume /Volumes/Sensidine — they fail with
#   "Operation not permitted" even while the volume is mounted. Therefore the repo
#   scripts/ are SOURCE ONLY. This installer COPIES them (plus the notify hook) to an
#   INTERNAL-disk location and the rendered plists' ProgramArguments point at those
#   internal copies — never at /Volumes/Sensidine/...
#
#     BIN_DIR = ~/Library/Application Support/Praxis/bin   (internal disk, runtime path)
#     DROP    = /Users/admin/praxis-signals                (internal disk, data/logs)
#     ENV     = ~/.praxis/signals.env                      (git-ignored, ORCH_N8N_WEBHOOK)
#
#   ./scripts/praxis-signals-install.sh install    # copy scripts internal, load all agents
#   ./scripts/praxis-signals-install.sh deploy     # copy scripts internal only (NO launchctl)
#   ./scripts/praxis-signals-install.sh uninstall  # unload + remove installed plists (keeps bin)
#   ./scripts/praxis-signals-install.sh status     # show loaded praxis agents
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TPL_DIR="$REPO_DIR/deploy/launchd"
LA_DIR="$HOME/Library/LaunchAgents"
BIN_DIR="$HOME/Library/Application Support/Praxis/bin"
DROP="/Users/admin/praxis-signals"
OUTBOX="/Users/admin/n8n-compose/local-files/outbox"
ENV_DIR="$HOME/.praxis"
ENV_FILE="$ENV_DIR/signals.env"
NOTIFY_SRC="$REPO_DIR/.claude/hooks/notify.sh"
SCRIPTS=(praxis-signals-sweep.sh praxis-signals-sweep-daemon.sh praxis-signals-stale-check.sh praxis-signals-backlog-check.sh)
LABELS=(build.praxis.signals-sweep-daemon build.praxis.signals-stale-check build.praxis.signals-backlog-check)
# 8xf (D-2026-07-12-A): the WatchPaths-triggered sweep job is SUPERSEDED by the
# persistent KeepAlive sweep daemon (launchd's 10s respawn throttle broke burst
# latency). install/uninstall remove the legacy job if present (idempotent).
LEGACY_LABELS=(build.praxis.signals-sweep)
ACTION="${1:-install}"

deploy_bin() {
  # Copy runtime scripts + notify hook from the external-volume repo to internal disk.
  mkdir -p "$BIN_DIR" "$DROP/incoming" "$DROP/logs" "$OUTBOX" "$LA_DIR" "$ENV_DIR"
  for s in "${SCRIPTS[@]}"; do
    cp -f "$REPO_DIR/scripts/$s" "$BIN_DIR/$s"
    chmod +x "$BIN_DIR/$s"
  done
  cp -f "$NOTIFY_SRC" "$BIN_DIR/notify.sh"
  chmod +x "$BIN_DIR/notify.sh"
  echo "deployed scripts -> $BIN_DIR"

  # Seed the git-ignored env file from the ambient webhook, if present and not already set.
  if [ ! -f "$ENV_FILE" ]; then
    if [ -n "${ORCH_N8N_WEBHOOK:-}" ]; then
      umask 077
      printf 'ORCH_N8N_WEBHOOK=%s\n' "$ORCH_N8N_WEBHOOK" > "$ENV_FILE"
      echo "wrote $ENV_FILE (from ambient ORCH_N8N_WEBHOOK)"
    else
      echo "NOTE: ORCH_N8N_WEBHOOK unset and $ENV_FILE absent -> stale alert path is structural-only until the trader creates it"
    fi
  fi
}

remove_legacy() {
  # Unload + remove superseded jobs (e.g. the pre-8xf WatchPaths sweep). Safe to
  # re-run when nothing is present.
  for label in "${LEGACY_LABELS[@]}"; do
    if launchctl print "gui/$UID/$label" >/dev/null 2>&1 || [ -f "$LA_DIR/$label.plist" ]; then
      launchctl bootout "gui/$UID/$label" 2>/dev/null || true
      rm -f "$LA_DIR/$label.plist"
      echo "removed legacy: $label"
    fi
  done
}

render_and_load() {
  for label in "${LABELS[@]}"; do
    # __BIN_DIR__ -> internal bin dir; '|' delimiter because BIN_DIR contains spaces.
    sed -e "s|__BIN_DIR__|$BIN_DIR|g" "$TPL_DIR/$label.plist" > "$LA_DIR/$label.plist"
    launchctl bootout   "gui/$UID/$label" 2>/dev/null || true
    # 8xf: bootout of a RUNNING service (the KeepAlive daemon) completes
    # asynchronously — bootstrap racing it fails with EIO. Wait (bounded ~5s)
    # until launchd has fully removed the service, then load; one retry.
    for _ in $(seq 1 25); do
      launchctl print "gui/$UID/$label" >/dev/null 2>&1 || break
      sleep 0.2
    done
    launchctl bootstrap "gui/$UID" "$LA_DIR/$label.plist" || {
      sleep 1
      launchctl bootstrap "gui/$UID" "$LA_DIR/$label.plist"
    }
    launchctl enable    "gui/$UID/$label" 2>/dev/null || true
    echo "loaded: $label"
  done
}

case "$ACTION" in
  install)
    deploy_bin
    remove_legacy
    render_and_load
    ;;
  deploy)
    deploy_bin
    # Render installed plists (internal paths) but do NOT launchctl load them.
    for label in "${LABELS[@]}"; do
      sed -e "s|__BIN_DIR__|$BIN_DIR|g" "$TPL_DIR/$label.plist" > "$LA_DIR/$label.plist"
      echo "rendered (not loaded): $LA_DIR/$label.plist"
    done
    echo "deploy complete; load with: launchctl bootstrap gui/\$UID $LA_DIR/<label>.plist"
    ;;
  uninstall)
    for label in "${LABELS[@]}"; do
      launchctl bootout "gui/$UID/$label" 2>/dev/null || true
      rm -f "$LA_DIR/$label.plist"
      echo "unloaded: $label"
    done
    remove_legacy
    ;;
  status)
    launchctl list 2>/dev/null | grep -i praxis || echo "no praxis agents loaded"
    ;;
  *)
    echo "usage: $0 {install|deploy|uninstall|status}" >&2
    exit 1
    ;;
esac
