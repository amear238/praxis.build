#!/bin/bash
# praxis-b2data-watch-install.sh — Praxis_build-3q4 (b2-data-mailbox)
# Idempotent (un)installer for the b2-data mailbox watcher LaunchAgent.
#
# CRITICAL DEPLOYMENT MODEL (macOS TCC) — same as praxis-signals-install.sh:
#   macOS TCC blocks per-user launchd (gui/$UID) agents from *executing* scripts
#   on the EXTERNAL volume /Volumes/Sensidine ("Operation not permitted"). So the
#   repo scripts/ are SOURCE ONLY. This installer COPIES the watcher + validator +
#   notify hook to an INTERNAL-disk bin and the rendered plist's ProgramArguments
#   points at that internal copy — never at /Volumes/Sensidine/...
#
#     BIN_DIR      = ~/Library/Application Support/Praxis/bin   (internal disk, runtime)
#     MAILBOX_ROOT = ~/praxis-signals/b2-data                   (Parallels share; internal disk)
#     STATE_DIR    = ~/.praxis/state                            (internal disk, seen/settle state)
#
# This is a NEW, INDEPENDENT job (label build.praxis.b2data-watch). It NEVER
# touches the live signal-path daemons (build.praxis.signals-*).
#
#   ./scripts/praxis-b2data-watch-install.sh install    # scaffold + copy internal + load agent
#   ./scripts/praxis-b2data-watch-install.sh deploy     # scaffold + copy internal + render (NO launchctl)
#   ./scripts/praxis-b2data-watch-install.sh scaffold   # create the mailbox dirs + seeds only
#   ./scripts/praxis-b2data-watch-install.sh uninstall  # unload + remove this plist (keeps bin + data)
#   ./scripts/praxis-b2data-watch-install.sh status     # show this agent's launchd state
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TPL_DIR="$REPO_DIR/deploy/launchd"
LA_DIR="$HOME/Library/LaunchAgents"
BIN_DIR="$HOME/Library/Application Support/Praxis/bin"
MAILBOX_ROOT="${PRAXIS_B2DATA_ROOT:-$HOME/praxis-signals/b2-data}"
STATE_DIR="${PRAXIS_B2DATA_STATE:-$HOME/.praxis/state}"
LOG_DIR="$HOME/praxis-signals/logs"
NOTIFY_SRC="$REPO_DIR/.claude/hooks/notify.sh"
LABEL="build.praxis.b2data-watch"
SCRIPTS=(praxis-b2data-watch.sh b2data_raw_validate.py)
ACTION="${1:-install}"

scaffold() {
  # Bidirectional file mailbox under the Parallels share (design §2.1).
  mkdir -p "$MAILBOX_ROOT/outbound" "$MAILBOX_ROOT/inbound" \
           "$MAILBOX_ROOT/raw" "$MAILBOX_ROOT/reports" \
           "$STATE_DIR" "$LOG_DIR"

  # Seed the empty inbound status channel (coworker overwrites it in the VM).
  [ -f "$MAILBOX_ROOT/inbound/status.txt" ] || : > "$MAILBOX_ROOT/inbound/status.txt"

  # Seed the current export brief for the coworker (Mac -> VM channel). Overwrite
  # is safe: this is the authoritative brief, regenerated from STATUS / D-2026-07-17-A.
  cat > "$MAILBOX_ROOT/outbound/INSTRUCTIONS.md" <<'BRIEF'
# b2-data export brief — VM (NT8) -> Mac (raw/)

**Goal:** export every NQ quarterly whose liquid window overlaps 2021-07-15 -> 2026-07-14,
so the Mac can stitch the continuous 1-min series in Python (D-2026-07-17-A: Vol/OI-crossover
roll + Difference back-adjustment, built OUTSIDE NT8).

## The 22 contracts (drop TWO files each into this share's `raw/`)
06-21, 09-21, 12-21, 03-22, 06-22, 09-22, 12-22, 03-23, 06-23, 09-23, 12-23,
03-24, 06-24, 09-24, 12-24, 03-25, 06-25, 09-25, 12-25, 03-26, 06-26, 09-26

Per contract, export BOTH:
- `NQ-<MM-YY>_1min.csv`  — 1-minute OHLCV (Timestamp,Open,High,Low,Close,Volume)
- `NQ-<MM-YY>_daily.csv` — daily bars WITH Volume **and Open Interest**
  (Date,Open,High,Low,Close,Volume,OpenInterest)

Example filenames for the 03-22 contract: `NQ-03-22_1min.csv`, `NQ-03-22_daily.csv`.
That is 22 x 2 = **44 files** total.

## Chunking rule (Praxis_build-2vu — MUST follow)
Pull history in chunks of **<= ~18 months per request**. **NEVER request the full
multi-year span in one shot** — a single 2021-2026 request spawned 1,800+ NT8 error
dialogs, pegged CPU and froze the UI (force-restart required). Roughly one request per
calendar year (2022 / 2023 / 2024 / 2025) plus the edges.

## Open-Interest check (do this on the FIRST daily export)
Open the first `*_daily.csv` and **confirm the Open Interest column has real, non-zero
values**. If OI is blank/zero, STOP and say so in `inbound/status.txt` — the volume-only
crossover fallback is a documented deviation that needs trader sign-off + a DECISIONS
entry (D-2026-07-17-A OPEN RISK) BEFORE it is used.

## When done
Optionally `touch raw/_EXPORT-COMPLETE`. The Mac-side watcher auto-detects landings,
runs the OI gate + a raw-landing validation, and writes `reports/raw-landing-validation.md`.
Use `inbound/status.txt` for any free-text status / questions — it reaches the trader/Claude
with no manual relay.
BRIEF

  echo "scaffolded mailbox -> $MAILBOX_ROOT (outbound/INSTRUCTIONS.md + empty inbound/status.txt)"
}

deploy_bin() {
  mkdir -p "$BIN_DIR" "$LA_DIR"
  for s in "${SCRIPTS[@]}"; do
    cp -f "$REPO_DIR/scripts/$s" "$BIN_DIR/$s"
    chmod +x "$BIN_DIR/$s"
  done
  # notify.sh is shared with the signals install; copy is idempotent (same content).
  cp -f "$NOTIFY_SRC" "$BIN_DIR/notify.sh"
  chmod +x "$BIN_DIR/notify.sh"
  echo "deployed scripts -> $BIN_DIR"
}

render() {
  # __BIN_DIR__ -> internal bin; __MAILBOX_ROOT__ -> share mailbox root.
  # '|' delimiter because both contain spaces.
  sed -e "s|__BIN_DIR__|$BIN_DIR|g" \
      -e "s|__MAILBOX_ROOT__|$MAILBOX_ROOT|g" \
      "$TPL_DIR/$LABEL.plist" > "$LA_DIR/$LABEL.plist"
  echo "rendered: $LA_DIR/$LABEL.plist"
}

load() {
  launchctl bootout "gui/$UID/$LABEL" 2>/dev/null || true
  # bootout of a RUNNING KeepAlive daemon completes asynchronously; wait
  # (bounded ~5s) until launchd removes the service, then bootstrap (one retry).
  for _ in $(seq 1 25); do
    launchctl print "gui/$UID/$LABEL" >/dev/null 2>&1 || break
    sleep 0.2
  done
  launchctl bootstrap "gui/$UID" "$LA_DIR/$LABEL.plist" || {
    sleep 1
    launchctl bootstrap "gui/$UID" "$LA_DIR/$LABEL.plist"
  }
  launchctl enable "gui/$UID/$LABEL" 2>/dev/null || true
  echo "loaded: $LABEL"
}

case "$ACTION" in
  install)
    scaffold
    deploy_bin
    render
    load
    ;;
  deploy)
    scaffold
    deploy_bin
    render
    echo "deploy complete; load with: launchctl bootstrap gui/\$UID $LA_DIR/$LABEL.plist"
    ;;
  scaffold)
    scaffold
    ;;
  uninstall)
    launchctl bootout "gui/$UID/$LABEL" 2>/dev/null || true
    rm -f "$LA_DIR/$LABEL.plist"
    echo "unloaded + removed: $LABEL (bin + mailbox data kept)"
    ;;
  status)
    launchctl list 2>/dev/null | grep -i b2data || echo "b2data-watch agent not loaded"
    ;;
  *)
    echo "usage: $0 {install|deploy|scaffold|uninstall|status}" >&2
    exit 1
    ;;
esac
