# B1-b-fu (Praxis_build-3m8) — Event-driven sweep via WatchPaths

**Date:** 2026-07-10
**Bead:** Praxis_build-3m8 (B1-b-fu)
**Goal:** Make the outbox→drop relay event-driven so webhook→file-in-VM stays < 5s (B1-d prerequisite).

## Problem

The B1-c sweep LaunchAgent `build.praxis.signals-sweep` ran on `StartInterval=60` only,
with no `WatchPaths`. A file written to the n8n outbox could wait up to 60s before the
sweep relayed it to the VM-shared drop dir. n8n's Docker container mounts only
`./local-files:/files`, so it cannot write the VM drop dir `/Users/admin/praxis-signals`
directly — the sweep is the required bridge, and its latency gated B1-d.

## Fix

Added a `WatchPaths` key to the sweep LaunchAgent pointing at the outbox dir. launchd
now fires the job within ~1-2s of any change to the outbox contents. `StartInterval=60`
is retained as a backstop.

### Source plist diff (`deploy/launchd/build.praxis.signals-sweep.plist`)

```diff
   <key>StartInterval</key>
   <integer>60</integer>
+  <!-- Event-driven trigger (B1-b-fu): launchd fires the sweep within ~1-2s of any
+       change to the outbox dir contents, so an n8n outbox write relays to the drop
+       dir well under 5s. StartInterval above is retained as a 60s backstop. This is
+       a fixed data path (not the internal BIN_DIR), so it is a literal — the
+       installer's __BIN_DIR__ sed pass leaves it untouched. -->
+  <key>WatchPaths</key>
+  <array>
+    <string>/Users/admin/n8n-compose/local-files/outbox</string>
+  </array>
   <key>RunAtLoad</key>
   <true/>
```

### Installer handling (`scripts/praxis-signals-install.sh`)

No installer change required. The outbox path is a fixed data path (already hardcoded
as `OUTBOX` in the installer), not the internal runtime dir. The installer renders
plists with a single substitution — `sed -e "s|__BIN_DIR__|$BIN_DIR|g"` — which only
touches the `__BIN_DIR__` placeholder in `ProgramArguments`. The literal WatchPaths
`<string>` passes through the sed render untouched. The TCC deployment model
(external-volume repo = SOURCE ONLY; runtime scripts copied to internal-disk BIN_DIR;
plist `ProgramArguments` point at internal copies) is fully preserved.

Reload performed via `bash scripts/praxis-signals-install.sh install`, which
bootout+bootstraps both agents so the new plist is live.

## VERIFY — real timestamps

Reload confirmed:

```
$ launchctl list | grep -i praxis
-	0	build.praxis.signals-stale-check
-	0	build.praxis.signals-sweep

# Loaded internal plist (~/Library/LaunchAgents/build.praxis.signals-sweep.plist):
$ PlistBuddy -c "Print :WatchPaths"     -> Array { /Users/admin/n8n-compose/local-files/outbox }
$ PlistBuddy -c "Print :StartInterval"  -> 60          # backstop intact
```

Relay timing (wrote a valid-JSON test file into the outbox, polled the drop dir):

```
WRITE_TS=1783690349.374260000  file=/Users/admin/n8n-compose/local-files/outbox/watchtest-1783690349-3812.json
ARRIVE_TS=1783690349.623965000
DELTA_SECONDS=.249705000        # 0.25s — well under the 5s budget

=== ls drop ===
-rw-r--r--  1 admin  staff  55 Jul 10 09:32 /Users/admin/praxis-signals/watchtest-1783690349-3812.json
```

**Measured relay latency: 0.25s** (budget < 5s; PASS).

## Cleanup / monitoring health

Test file removed from drop, outbox, and incoming (verified 0 remaining in each).
Heartbeat healthy and advancing — the WatchPaths-triggered sweep updated it:

```
heartbeat=1783690349 now=1783690355 age=6s
```

Both agents remain loaded (status 0). Both `WatchPaths` and the `StartInterval=60`
backstop are present in the loaded plist. Monitoring is healthy.
