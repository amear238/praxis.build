# F-B1e-1 — Stuck-Backlog Detector (fix for the B1-e SILENT-LOSS gap)

**Bead:** Praxis_build-22r (F-B1e-1)
**Date:** 2026-07-10
**Topology:** LOCAL (D-2026-07-09-D) — n8n Docker + macOS launchd, NT8 on Parallels
**Author:** implementer subagent

## The gap this closes (proven by B1-e)

The sweep relays `OUTBOX/*.json` → `DROP/incoming` (rsync `--remove-source-files`) →
`mv incoming/*.json → DROP/`. The final `mv` needs **write on the `DROP` directory
itself**; the heartbeat write only needs write on the already-existing `.heartbeat`
**file**. So when `DROP` is dir-unwritable (`chmod 500` / VM share offline) the `mv` fails
silently (`|| true`) while `date +%s > $HEARTBEAT` still succeeds — signals pile up in
`DROP/incoming`, the heartbeat stays **fresh**, the stale-check **never fires**, and NT8
silently stops receiving signals. B1-e proved this Class-A failure fired **nothing**.

## Design (option a — stuck-backlog detector; decoupled from heartbeat semantics)

New LaunchAgent `build.praxis.signals-backlog-check` runs
`praxis-signals-backlog-check.sh` every **30s**. It scans `DROP/incoming/*.json` **and**
`OUTBOX/*.json`; if any file has been present longer than the **60s** threshold it fires a
Telegram alert via `notify.sh` (webhook from `~/.praxis/signals.env`), latches to prevent
spam, and — when the backlog drains — clears the latch and fires a recovery note. Mirrors
the stale-check's env-loading, notify path, durable append-only alert log
(`logs/signals-alerts.log`), and error tolerance.

### Key design decisions

1. **Age measured by `ctime`, not `mtime`.** `rsync -a` *preserves* the source mtime, so a
   file's mtime reflects when n8n first wrote it (misleading — a signal that sat in the
   outbox could look "stuck" the instant it lands in incoming). `ctime` is set to "now"
   whenever the inode is created/moved and cannot be back-dated by userland, so it is the
   true "arrived in this directory" time. Uses `stat -f %c`.

2. **Latch + alert log live in `DROP/logs/`, NOT `DROP/`.** During the exact failure this
   detects, the `DROP` dir is unwritable — a latch at `DROP/.backlog-alerted` could not be
   created (creating a file needs write on the parent dir). `DROP/logs` and `DROP/incoming`
   keep their own 755 perms and stay writable (that is *why* files spool into incoming), so
   the latch (`logs/.backlog-alerted`) and the durable log go there.

3. **Threshold 60s / interval 30s.** 60s is longer than a healthy sweep ever holds the
   staging dir (WatchPaths relays in ~1-2s; 60s StartInterval backstop) yet short enough to
   alert fast. Paired with the 30s launchd interval, worst-case detection ≈ threshold +
   interval ≈ **90s** (observed: 71s).

4. **bash 3.2 empty-array fix.** macOS `/bin/bash` is 3.2.57, where an empty-array
   expansion `"${arr[@]}"` trips `set -u` ("unbound variable"). First drill run exposed
   this in the err log — it fired the alert fine (array non-empty) but on the healthy/empty
   case the script died before the recovery branch (latch would never clear). Fixed by
   iterating the globs **directly** under `nullglob`
   (`for f in "$INCOMING"/*.json "$OUTBOX"/*.json`) so a no-match simply loops zero times —
   the same idiom the sweep already uses. Verified under bash 3.2 in isolation (exit 0,
   latch cleared, recovery note emitted).

## Installer changes

`scripts/praxis-signals-install.sh` — added the new script to `SCRIPTS=(...)` and the new
label to `LABELS=(...)`. Those two arrays drive every action (deploy copy loop, render+load,
deploy-only render, uninstall bootout+rm, status grep), so all actions now handle the new
detector idempotently with no other edits. Header comment updated ("load all agents").

## Files

- `scripts/praxis-signals-backlog-check.sh` (SOURCE ONLY; runtime copy at
  `~/Library/Application Support/Praxis/bin/`)
- `deploy/launchd/build.praxis.signals-backlog-check.plist` (`__BIN_DIR__` placeholder,
  StartInterval 30, RunAtLoad, ProcessType Background)
- `scripts/praxis-signals-install.sh` (arrays extended)

## VERBATIM re-drill evidence (the exact thing that was SILENT before)

### 1. Baseline / injection
```
ORIGINAL PERMS:  drwxr-xr-x /Users/admin/praxis-signals   (incoming 755, logs 755)
inject:          chmod 500 /Users/admin/praxis-signals  ->  dr-x------
```
3 sim signals dropped into OUTBOX; after ~6s:
```
OUTBOX:   empty (rsync removed source)
INCOMING: 3 STUCK files (DRILL-0001/0002/0003.json)
DROP:     no drill files (mv blocked, as expected)
HEARTBEAT: 1783694560  (now 1783694566) — THE GAP: still FRESH despite backlog
LATCH:    absent (age < 60s threshold)
```

### 2. Detector FIRES (old behavior fired NOTHING here)
```
LATCH APPEARED after 71s   (fired epoch 1783694644)
logs/signals-alerts.log:
  BACKLOG ALERT FIRED 1783694644 (2026-07-10T14:44:04Z) stuck=3 threshold=60s oldest=84s file=.../incoming/2026-07-10T14-42-40Z-SIM-F-B1E1-DRILL-0001.json
```
Send-side (n8n MCP): **execution 1088936** (wf 8l0cKKcLo25IIhpe), status success,
started 2026-07-10T14:44:04.881Z. Telegram `Send Telegram Ping` output:
```
ok: true   message_id: 45   chat.id: 6156528469
text: "🤖 Orchestrator-Mine — praxis-signals-backlog
        Project: /
        STUCK BACKLOG: 3 signal file(s) un-promoted >60s (oldest 84s: .../DRILL-0001.json)
        — sweep relay/promotion FAILING, NT8 not receiving signals; check DROP dir
        writability (/Users/admin/praxis-signals)"
```
(Prior baseline latest exec was 1088642 — 1088936 is strictly newer, i.e. a fresh fire.)

### 3. Fix redeployed, no spam, err log clean
After redeploying the bash-3.2-fixed script and running 35s against the still-stuck
backlog: err log **0 lines** (no more `unbound variable`), latch held single
(`1783694644`), alert log still one FIRED line (no dup).

### 4. Replay + recovery (restore perms)
```
restore:  chmod 755 /Users/admin/praxis-signals  ->  drwxr-xr-x
kickstart sweep -> 3 files REPLAYED into DROP; incoming drained; heartbeat advancing
LATCH CLEARED after ~9s
logs/signals-alerts.log:
  BACKLOG RECOVERED 1783694825 (2026-07-10T14:47:05Z)
```
Recovery send-side: **execution 1088984** (success). Telegram output:
```
ok: true   message_id: 46   chat.id: 6156528469
text: "🤖 Orchestrator-Mine — praxis-signals-backlog-recovered
        RECOVERED: signal backlog cleared — sweep relay/promotion healthy again
        (/Users/admin/praxis-signals)"
```

### 5. Cleanup + monitoring left EXACTLY healthy
```
launchctl list | grep praxis:
  28273  0  build.praxis.signals-stale-check
  -      0  build.praxis.signals-sweep
  28280  0  build.praxis.signals-backlog-check
perms: 755 / 755 / 755   latches: none   drill files: removed
```
Full idempotent reinstall via `praxis-signals-install.sh install` re-loaded all three
agents cleanly (fixed script 5742 bytes deployed to internal bin).

### 6. Happy path still works (post-reinstall)
1 sim signal OUTBOX → DROP in **~2s**, outbox+incoming drained, heartbeat advancing
(1783695198), **no false backlog latch**, backlog err log 0 lines. Sweep + stale-check +
backlog-check all green.

## Outcome

The B1-e SILENT-LOSS gap is closed: a promotion-only failure that previously left the
operator un-alerted now fires a real Telegram alert within ~90s (observed 71s) and a
recovery note on drain — proven live with n8n execution ids and Telegram message ids.
Spool + replay were already correct; this is the visibility fix. All three launchd jobs
status 0, heartbeat advancing, perms restored, happy path intact.
