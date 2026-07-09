#!/bin/bash
# praxis-signals-sweep.sh — B1-c (Praxis_build-dnt)
# Sweeps leftover signal files from the n8n OUTBOX into the VM-visible drop dir,
# via a two-stage staging (incoming/) -> final promotion, and writes a heartbeat.
#
# Flow: n8n writes JSON -> OUTBOX (a dedicated subdir; NOT the whole local-files
# root, which holds unrelated n8n workflow exports). This job is a safety net for
# files the primary write path (B1-b) leaves behind, and it guarantees NT8's
# FileSystemWatcher only ever sees fully-formed files in the final drop dir.
#
#  1. rsync --remove-source-files  OUTBOX/*.json  -> DROP/incoming/  (atomic per file,
#     source removed only on a complete transfer; safe across filesystems)
#  2. mv (atomic, same fs) each staged file  DROP/incoming/*.json -> DROP/   (the
#     final location NT8 watches — rsync temp dotfiles never match *.json so a
#     half-written file is never promoted)
#  3. touch heartbeat (epoch seconds) so the stale-check job can detect a dead sweep
#
# Idempotent, re-runnable, no secrets. Override paths via env for testing.
set -uo pipefail

OUTBOX="${PRAXIS_OUTBOX:-/Users/admin/n8n-compose/local-files/outbox}"
DROP="${PRAXIS_DROP:-/Users/admin/praxis-signals}"
INCOMING="$DROP/incoming"
HEARTBEAT="$DROP/.heartbeat"
RSYNC="${PRAXIS_RSYNC:-/usr/bin/rsync}"

mkdir -p "$OUTBOX" "$INCOMING" 2>/dev/null || true
shopt -s nullglob

# 1. OUTBOX -> staging
outfiles=("$OUTBOX"/*.json)
if (( ${#outfiles[@]} )); then
  "$RSYNC" -a --remove-source-files "${outfiles[@]}" "$INCOMING"/ 2>/dev/null || true
fi

# 2. staging -> final drop dir (atomic rename; *.json glob excludes rsync temp dotfiles)
for f in "$INCOMING"/*.json; do
  mv -f "$f" "$DROP/$(basename "$f")" 2>/dev/null || true
done

shopt -u nullglob

# 3. heartbeat
date +%s > "$HEARTBEAT" 2>/dev/null || true
exit 0
