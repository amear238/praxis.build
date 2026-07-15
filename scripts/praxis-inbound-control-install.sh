#!/bin/bash
# praxis-inbound-control-install.sh — Praxis_build-10i
# Idempotent (un)installer for the Telegram inbound CONTROL CHANNEL launchd agent.
# Companion to scripts/praxis-signals-install.sh; identical deployment model.
#
# CRITICAL DEPLOYMENT MODEL (macOS TCC):
#   macOS TCC blocks per-user launchd (gui/$UID) agents from *executing* scripts on
#   the EXTERNAL volume /Volumes/Sensidine ("Operation not permitted") even while
#   mounted. So repo scripts/ are SOURCE ONLY. This installer COPIES the runner
#   (plus the notify hook) to INTERNAL disk and the rendered plist's
#   ProgramArguments point at those internal copies.
#
#     BIN_DIR = ~/Library/Application Support/Praxis/bin   (internal, runtime path)
#     TG_DIR  = /Users/admin/praxis-tg                     (internal, data/logs/control)
#     INBOX   = /Users/admin/n8n-compose/local-files/tg-inbox (n8n-writable mount)
#     ENV     = ~/.praxis/signals.env                      (git-ignored, 0600)
#
#   ./scripts/praxis-inbound-control-install.sh deploy     # copy internal + render plist (NO launchctl) — DEFAULT-SAFE
#   ./scripts/praxis-inbound-control-install.sh install    # deploy + launchctl load (TRADER STEP)
#   ./scripts/praxis-inbound-control-install.sh uninstall  # unload + remove installed plist (keeps bin/data)
#   ./scripts/praxis-inbound-control-install.sh status     # show loaded agent
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TPL_DIR="$REPO_DIR/deploy/launchd"
LA_DIR="$HOME/Library/LaunchAgents"
BIN_DIR="$HOME/Library/Application Support/Praxis/bin"
TG_DIR="/Users/admin/praxis-tg"
INBOX="/Users/admin/n8n-compose/local-files/tg-inbox"
ENV_DIR="$HOME/.praxis"
ENV_FILE="$ENV_DIR/signals.env"
NOTIFY_SRC="$REPO_DIR/.claude/hooks/notify.sh"
RUNNER="praxis-inbound-control-watch.sh"
LABEL="build.praxis.tg-inbound"
ACTION="${1:-deploy}"

deploy_bin() {
  mkdir -p "$BIN_DIR" "$LA_DIR" "$ENV_DIR" "$INBOX" \
           "$TG_DIR/work" "$TG_DIR/done" "$TG_DIR/failed" "$TG_DIR/logs" "$TG_DIR/control"
  cp -f "$REPO_DIR/scripts/$RUNNER" "$BIN_DIR/$RUNNER"; chmod +x "$BIN_DIR/$RUNNER"
  # notify.sh may already be present from the signals installer; keep it fresh.
  cp -f "$NOTIFY_SRC" "$BIN_DIR/notify.sh"; chmod +x "$BIN_DIR/notify.sh"
  touch "$TG_DIR/processed-ids" 2>/dev/null || true
  echo "deployed runner -> $BIN_DIR/$RUNNER"

  # Sender-allowlist ids live in the same 0600 env file (chat_id is not a secret;
  # the outbound Telegram node already carries it literally). Seed only if absent.
  if [ -f "$ENV_FILE" ] && ! grep -q '^PRAXIS_TG_CHAT_ID=' "$ENV_FILE" 2>/dev/null; then
    umask 077
    { echo 'PRAXIS_TG_CHAT_ID=6156528469'
      echo 'PRAXIS_TG_FROM_ID=6156528469'; } >> "$ENV_FILE"
    echo "appended PRAXIS_TG_CHAT_ID/FROM_ID to $ENV_FILE"
  elif [ ! -f "$ENV_FILE" ]; then
    echo "NOTE: $ENV_FILE absent — runner falls back to built-in trader id default (6156528469); create the env file to override"
  fi
}

render() {
  # __BIN_DIR__ -> internal bin dir; '|' delimiter because BIN_DIR contains spaces.
  sed -e "s|__BIN_DIR__|$BIN_DIR|g" "$TPL_DIR/$LABEL.plist" > "$LA_DIR/$LABEL.plist"
}

case "$ACTION" in
  deploy)
    deploy_bin
    render
    echo "rendered (not loaded): $LA_DIR/$LABEL.plist"
    echo "deploy complete; TRADER loads with: launchctl bootstrap gui/\$UID $LA_DIR/$LABEL.plist"
    ;;
  install)
    deploy_bin
    render
    launchctl bootout   "gui/$UID/$LABEL" 2>/dev/null || true
    launchctl bootstrap "gui/$UID" "$LA_DIR/$LABEL.plist"
    launchctl enable    "gui/$UID/$LABEL" 2>/dev/null || true
    echo "loaded: $LABEL"
    ;;
  uninstall)
    launchctl bootout "gui/$UID/$LABEL" 2>/dev/null || true
    rm -f "$LA_DIR/$LABEL.plist"
    echo "unloaded + removed plist: $LABEL (bin/data kept)"
    ;;
  status)
    launchctl list 2>/dev/null | grep -i "tg-inbound" || echo "tg-inbound agent not loaded"
    ;;
  *)
    echo "usage: $0 {deploy|install|uninstall|status}" >&2
    exit 1
    ;;
esac
