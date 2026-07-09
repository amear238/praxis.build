# B1-c — Signals layout + launchd sweep/heartbeat (Praxis_build-dnt)

Date: 2026-07-09
Bead: Praxis_build-dnt (B1-c)
Author: implementer subagent (runs ON the target Mac, macOS Apple-Silicon)

## Summary
Built the internal-disk signal drop layout, a 60s launchd sweep (outbox → drop dir +
heartbeat), and a stale-heartbeat Telegram alert. Corrected the prior agent's fatal
deployment error: launchd agents were pointed at scripts on the **external** volume
`/Volumes/Sensidine`, which macOS TCC blocks (`Operation not permitted`). Runtime scripts
are now **copied to internal disk** and the plists point there. Sweep and stale-alert
logic verified end-to-end by running the deployed internal-disk scripts directly. The
launchd jobs themselves are **staged, not loaded** — loading is a trader/verify step.

## The internal-vs-external deployment model (WHY)
macOS TCC denies per-user launchd (`gui/$UID`) agents permission to *execute* scripts
located on the external volume `/Volumes/Sensidine`, even while it is mounted. The prior
agent's plists ran `__REPO_DIR__/scripts/*.sh` (external) and both failed — captured in
`/Users/admin/praxis-signals/logs/signals-*.err.log`:
```
/bin/bash: /Volumes/Sensidine/Praxis.build/scripts/praxis-signals-sweep.sh: Operation not permitted
/bin/bash: /Volumes/Sensidine/Praxis.build/scripts/praxis-signals-stale-check.sh: Operation not permitted
```
Correction: the repo `scripts/` are **SOURCE ONLY**. `praxis-signals-install.sh` copies
them (plus the notify hook) to an **internal** location and renders the plists to that
path. Data/logs/heartbeat under `/Users/admin/praxis-signals` are already internal and are
referenced directly.

| Role | Path | Disk |
|------|------|------|
| Source scripts (committed) | `/Volumes/Sensidine/Praxis.build/scripts/` | external — never a runtime path |
| Runtime scripts + notify.sh | `~/Library/Application Support/Praxis/bin/` | internal (deployed copy) |
| Plist templates (committed) | `deploy/launchd/*.plist` (`__BIN_DIR__` placeholder) | external — source |
| Installed plists | `~/Library/LaunchAgents/build.praxis.signals-*.plist` | internal |
| Drop dir / staging / logs / heartbeat | `/Users/admin/praxis-signals/{,incoming/,logs/,.heartbeat}` | internal |
| Outbox (sweep source) | `/Users/admin/n8n-compose/local-files/outbox/` | internal |
| Webhook env (git-ignored) | `~/.praxis/signals.env` | internal |

## Files created / modified
- `scripts/praxis-signals-install.sh` — rewritten. Now copies scripts+notify.sh to
  `~/Library/Application Support/Praxis/bin/`, seeds `~/.praxis/signals.env` from the
  ambient `ORCH_N8N_WEBHOOK`, renders plists with `__BIN_DIR__`. New `deploy` action
  copies + renders WITHOUT `launchctl` (used for this verification); `install` also loads.
- `scripts/praxis-signals-sweep.sh` — unchanged logic (already correct/internal-safe):
  rsync `--remove-source-files` outbox `*.json` → `incoming/`, atomic `mv` → drop dir,
  `date +%s > .heartbeat`. Outbox is the dedicated `outbox/` subdir (not the `local-files`
  root, which holds unrelated n8n exports).
- `scripts/praxis-signals-stale-check.sh` — fixed default `NOTIFY` to resolve to
  `notify.sh` **next to the script's deployed location** (was hardcoded to the external
  volume). Sources `~/.praxis/signals.env` for `ORCH_N8N_WEBHOOK`; latch file prevents
  alert-spam; threshold 180s.
- `deploy/launchd/build.praxis.signals-sweep.plist` — `__REPO_DIR__/scripts/…` →
  `__BIN_DIR__/praxis-signals-sweep.sh`; `StartInterval` 60s, `RunAtLoad`, Background.
- `deploy/launchd/build.praxis.signals-stale-check.plist` — same fix;
  `StartInterval` 120s (evaluates the 180s threshold).
- `docs/reports/2026-07-09-b1-c-signals-layout-launchd.md` — this report.
- `MANIFEST.md` — appended new-file rows.

## VERIFY — commands + captured output (SAFE; launchd NOT loaded)
Deployment (copies internal, renders plists, does NOT load):
```
bash scripts/praxis-signals-install.sh deploy
# -> deployed scripts -> ~/Library/Application Support/Praxis/bin
# -> wrote ~/.praxis/signals.env (from ambient ORCH_N8N_WEBHOOK)
# -> rendered (not loaded) both plists ; launchctl list | grep praxis => NONE loaded
```
Rendered ProgramArguments now internal:
```
~/Library/LaunchAgents/build.praxis.signals-sweep.plist:
  <string>/Users/admin/Library/Application Support/Praxis/bin/praxis-signals-sweep.sh</string>
~/Library/LaunchAgents/build.praxis.signals-stale-check.plist:
  <string>/Users/admin/Library/Application Support/Praxis/bin/praxis-signals-stale-check.sh</string>
```

VERIFY 1 — stray outbox file swept within one sweep, removed from outbox, heartbeat bumped:
```
printf '{...}' > outbox/verify-stray-$$.json
bash ~/Library/Application\ Support/Praxis/bin/praxis-signals-sweep.sh
# before: outbox=1  drop_json=1   heartbeat=1783618902
# after:  outbox=0  drop_json=2   heartbeat=1783619384
# swept file present in /Users/admin/praxis-signals/ ; removed from outbox  -> PASS
```

VERIFY 2 — stale heartbeat fires the alert (isolated temp DROP, `ORCH_NOTIFY_DRYRUN=1`
so nothing is POSTed to the trader's live Telegram):
```
# 2a stale (age 999s > 180s): notify payload emitted, latch created -> PASS
{"event":"praxis-signals-stale","project":"Praxis.build","detail":"signals-sweep heartbeat stale: 999s > 180s threshold (...)"}
# 2b second run: no payload (latch suppresses spam) -> PASS
# 2c heartbeat fresh: latch cleared, no alert -> PASS
# 2d source ~/.praxis/signals.env: ORCH_N8N_WEBHOOK resolved -> live alert path ENABLED
```

## ORCH_N8N_WEBHOOK status
**SET.** Value present in the build env and captured into `~/.praxis/signals.env`
(mode 0600) by the installer, so the stale alert's live POST path is **enabled** — not
structural-only. Verify 2 used DRYRUN to avoid sending a real alert; the non-DRYRUN path
would `curl` the webhook (`https://n8n.myzerker626.win/webhook/orchestrator-notify`).

## Parallels shared-folder scoping — TRADER-RUN (read-only inspected; NOT executed)
The VM is running the trader's live NT8 session. **Do not stop/restart the VM.** Read-only
inspection confirmed the over-broad B1-0 share is still active:
```
VM: "Windows 11"  UUID {e65d3127-f103-4e84-8a17-67568129f0a0}  STATUS running
Host Shared Folders: enabled
Host defined sharing: User home directory        <-- whole-home share to RETIRE
Shared Profile: disabled   SmartMount: disabled   Shared cloud: off
```
Goal: retire whole-home sharing, expose ONLY `/Users/admin/praxis-signals`.

### Option A — GUI (authoritative; recommended while VM is live)
Parallels Desktop → (VM "Windows 11") Actions/Control menu → **Configure…** →
**Options** tab → **Sharing**:
1. Under *Share Mac* set **Share folders with Windows** to **None** (this removes the
   "User home directory" mapping). Leave *Share Windows* untouched.
2. Click **Manage Folders…** → **+** (add) → choose `/Users/admin/praxis-signals`,
   Name it e.g. `praxis-signals`, Permissions **Read & Write**, Enabled. OK.
3. Confirm no other custom folders remain enabled; close config.
4. In Windows, confirm `\\Mac\praxis-signals` (or the mapped drive) shows only the drop
   dir and NT8's FileSystemWatcher still sees files.

### Option B — prlctl (may apply live; verify NT8 not disrupted before relying on it)
```
PRLCTL="/Applications/Parallels Desktop.app/Contents/MacOS/prlctl"
VM="{e65d3127-f103-4e84-8a17-67568129f0a0}"

# 1. retire whole-home ("User home directory") predefined sharing:
"$PRLCTL" set "$VM" --shf-host-defined off

# 2. add ONLY the drop dir as a named read-write share:
"$PRLCTL" set "$VM" --shf-host-add praxis-signals --path /Users/admin/praxis-signals --mode rw

# 3. keep the host-shared-folders feature enabled (so the named share mounts):
"$PRLCTL" set "$VM" --shf-host on

# verify:
"$PRLCTL" list --info "$VM" | grep -iE "Host defined sharing|Host Shared Folders|praxis-signals"
```
NOTE: exact flag spelling can vary by Parallels build; this build's `prlctl set --help`
does not expand the `shared_folders` sub-options. Confirm with
`"$PRLCTL" set "$VM" --help | grep -i shf` first, and prefer Option A (GUI) if the flags
differ. Do NOT reboot the VM to apply.

## Still needs the trader
1. **Load the launchd jobs** (internal-disk, TCC-safe). One-time:
   ```
   bash /Volumes/Sensidine/Praxis.build/scripts/praxis-signals-install.sh install
   # or, if already deployed, just:
   launchctl bootstrap gui/$UID ~/Library/LaunchAgents/build.praxis.signals-sweep.plist
   launchctl bootstrap gui/$UID ~/Library/LaunchAgents/build.praxis.signals-stale-check.plist
   launchctl list | grep praxis   # expect both labels, exit code 0
   ```
   (Left unloaded by design — the implementer must not load launchd jobs.)
2. **Scope the Parallels share** per the GUI (Option A) or prlctl (Option B) steps above,
   retiring the whole-home B1-0 share.
3. **Confirm the live sweep** after load: drop a file in the outbox, confirm it lands in
   `/Users/admin/praxis-signals/` within 60s and `.heartbeat` advances; optionally
   `launchctl bootout` the sweep for >180s and confirm a real Telegram alert arrives.
4. If the machine is ever re-imaged / the env lacks `ORCH_N8N_WEBHOOK`, recreate
   `~/.praxis/signals.env` with the webhook line, else the stale alert no-ops.
