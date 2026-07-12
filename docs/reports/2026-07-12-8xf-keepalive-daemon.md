# 8xf — Signals Relay: WatchPaths Sweep → Persistent KeepAlive Daemon (DEPLOYED)

**Bead:** Praxis_build-8xf
**Date:** 2026-07-12
**Decision:** D-2026-07-12-A (DECISIONS.md) — evidence in docs/reports/2026-07-12-8xf-latency-investigation.md
**Type:** Implementation + live deployment + verification

---

## TL;DR

The outbox→drop relay no longer depends on launchd WatchPaths respawns (which the 10s
minimum-runtime throttle pinned to ≥10s apart under bursts). A persistent daemon
(`build.praxis.signals-sweep-daemon`, KeepAlive=true) now runs the **unchanged** sweep
script in a 1s loop. Deployed live on this host; legacy WatchPaths job
`build.praxis.signals-sweep` unloaded and removed.

**Verified:** 6-file burst @1.8s spacing → 6/6 delivered <5s, **max 1.031s** (was 3/6
FAIL, max 9.15s pre-fix). Bonus 6 @1.0s → max 1.124s. Isolated signal 0.147s.
`kill -9` of the daemon → launchd restarted it in <1s (new PID), relay immediately
functional (0.061s). All TEST artifacts cleaned up.

---

## 1. Design

### What changed (and what deliberately did not)

| Piece | Before (B1-b-fu) | After (8xf) |
|---|---|---|
| Launch mechanism | launchd `WatchPaths` on outbox + `StartInterval=60` backstop; new process per event | Persistent process, `KeepAlive=true` + `RunAtLoad`; **no** WatchPaths / StartInterval |
| Label | `build.praxis.signals-sweep` | `build.praxis.signals-sweep-daemon` (new label so the legacy job's removal is explicit and verifiable) |
| Sweep logic | `scripts/praxis-signals-sweep.sh` | **Identical file, unchanged** — daemon invokes it as a child each iteration |
| Heartbeat / stale-check semantics | heartbeat touched per sweep run; stale-check @180s | Identical mechanism; heartbeat now refreshes every ~1s (fresher). stale-check + backlog-check jobs untouched |
| Worst-case relay leg | ~10.6s (throttled respawn) | ~1.3s (1s sleep + ≤0.3s sweep); throttle can never apply — the process never respawns per event |

### New daemon script — `scripts/praxis-signals-sweep-daemon.sh`

Loop: run `praxis-signals-sweep.sh` (resolved next to the deployed daemon copy,
overridable via `PRAXIS_SWEEP` / `PRAXIS_SWEEP_INTERVAL` for testing), then `sleep 1`.
Details:

- `"$SWEEP" || true` — one bad sweep iteration never kills the daemon (the sweep is
  itself failure-tolerant by design).
- `sleep 1 & wait $!` — the nap runs backgrounded so SIGTERM interrupts it immediately
  instead of being deferred to the end of a foreground sleep.
- `trap ... TERM INT → exit 0` — clean exit only on launchctl bootout/kill; any other
  death is restarted by KeepAlive.
- Start/stop lines (UTC + pid) to the daemon log; no per-iteration logging (no log growth).

Failure modes (per D-2026-07-12-A): crash → KeepAlive respawn (worst case one 10s
throttle penalty in a crash-loop); hang → KeepAlive can't help, but the heartbeat stops
refreshing and the existing 180s stale-check alerts — strictly better than the old silent
10s coalescing.

### New plist — `deploy/launchd/build.praxis.signals-sweep-daemon.plist`

`KeepAlive=true`, `RunAtLoad=true`, `ProcessType=Background`, same PATH env and log-dir
convention as the sibling jobs (`/Users/admin/praxis-signals/logs/signals-sweep-daemon.{out,err}.log`).
`__BIN_DIR__` template substitution as before — the TCC rule stands: repo files are
SOURCE ONLY, launchd executes only the internal-disk copies under
`~/Library/Application Support/Praxis/bin`.

The old template `deploy/launchd/build.praxis.signals-sweep.plist` is **deleted** from
the repo (retrievable at `git show HEAD~1:deploy/launchd/build.praxis.signals-sweep.plist`
after this lands; also embedded in §6 Rollback).

## 2. Installer changes — `scripts/praxis-signals-install.sh` (v3)

1. `SCRIPTS` gains `praxis-signals-sweep-daemon.sh` (sweep.sh stays — the daemon calls it).
2. `LABELS`: `build.praxis.signals-sweep` → `build.praxis.signals-sweep-daemon`.
3. New `LEGACY_LABELS=(build.praxis.signals-sweep)` + `remove_legacy()` — bootout + plist
   removal of the superseded WatchPaths job, run on `install` and `uninstall`; no-op when
   absent (idempotent).
4. **Race fix found during deployment:** `launchctl bootout` of a RUNNING service (which
   the KeepAlive daemon now always is on re-install) completes asynchronously; the
   immediately-following `bootstrap` raced it and failed with
   `Bootstrap failed: 5: Input/output error`. `render_and_load` now waits (bounded ~5s,
   polling `launchctl print`) for the service to be fully removed before bootstrapping,
   with one retry. Verified: two consecutive `install` runs both complete cleanly.

`deploy` mode remains launchctl-free by contract (copies + renders only); legacy-job
removal happens on `install`.

## 3. Deployment evidence (this host, 2026-07-12)

Installer run (`./scripts/praxis-signals-install.sh install`):

```
deployed scripts -> /Users/admin/Library/Application Support/Praxis/bin
removed legacy: build.praxis.signals-sweep
loaded: build.praxis.signals-sweep-daemon
loaded: build.praxis.signals-stale-check
loaded: build.praxis.signals-backlog-check
```

Old job gone:

```
$ launchctl print gui/501/build.praxis.signals-sweep
Could not find service "build.praxis.signals-sweep" in domain for user gui: 501
$ ls ~/Library/LaunchAgents | grep praxis
build.praxis.signals-backlog-check.plist
build.praxis.signals-stale-check.plist
build.praxis.signals-sweep-daemon.plist        # no legacy sweep plist
```

New daemon under launchd (`launchctl print gui/501/build.praxis.signals-sweep-daemon`):

```
active count = 1
path = /Users/admin/Library/LaunchAgents/build.praxis.signals-sweep-daemon.plist
state = running
program = /bin/bash
        /Users/admin/Library/Application Support/Praxis/bin/praxis-signals-sweep-daemon.sh
pid = 22058
properties = keepalive | runatload | inferred program
```

Heartbeat age at check time: 1s (was up to 60s between backstop runs). Outbox and
`incoming/` empty; stale/backlog latches clear; no new alert-log lines.

## 4. Verification against bead acceptance

Method: TEST files written directly into the outbox
(`/Users/admin/n8n-compose/local-files/outbox`) with atomic tmp+rename (mirroring the
n8n write node), 10ms poller running **concurrently** with the writes (a post-hoc poll
reproduces the B1-d measurement artifact — first run of the harness did exactly that and
showed phantom 9s latencies until fixed). Latency = outbox write → file present in the
final drop dir `/Users/admin/praxis-signals/` (i.e. already relayed *through*
`incoming/` staging and promoted — the strongest form of "landed"). This isolates the
relay leg; the n8n webhook→outbox leg is +0.15s and owned by bead qxd.

### Burst: 6 signals @ 1.8s spacing (the investigation's failing case)

| file | latency (s) | <5s? |
|---|---|---|
| TEST-8XF-DAEMON-102740-01.json | 1.031 | PASS |
| TEST-8XF-DAEMON-102740-02.json | 0.387 | PASS |
| TEST-8XF-DAEMON-102740-03.json | 0.863 | PASS |
| TEST-8XF-DAEMON-102740-04.json | 0.231 | PASS |
| TEST-8XF-DAEMON-102740-05.json | 0.752 | PASS |
| TEST-8XF-DAEMON-102740-06.json | 0.143 | PASS |

**6/6 PASS, max 1.031s** (pre-fix same scenario: 3/6 FAIL, max 9.15s).

### Bonus burst: 6 signals @ 1.0s spacing

Max **1.124s**, 6/6 PASS (0.261 / 0.429 / 0.604 / 0.798 / 0.956 / 1.124).

### Isolated single signal

**0.147s** PASS (pre-fix isolated signals hit 7.36s when the throttle window was hot).

### Kill-restart (KeepAlive proof)

```
pid before kill: 21176
$ kill -9 21176
pid after kill:  22058   (restarted in <1s)
runs = 2
relay check after restart: TEST file delivered in 0.061s  PASS
```

Daemon log corroborates: pid 21176 has a `start` line but no `stop` line (SIGKILL is
untrappable), followed immediately by pid 22058's `start` line at 14:28:19Z. Clean
TERM stops (installer bootouts) do log `stop` lines.

### Cleanup attestation

All harness runs delete their own TEST files. Post-verification listing: outbox empty,
`incoming/` empty, drop dir contains only the pre-existing
`2026-07-09T20-24-00Z-SIM-B1B-0001.json` + `signal-template.json`, zero `TEST*` residue.
No Telegram noise: the n8n workflow was bypassed (files written straight to outbox), so
the success-path notification never fired. No non-relay launchd job, workflow, or VM-side
component was touched.

## 5. Re-runnable auditor check

Save as `burst_check.py` anywhere on this host and run
`python3 burst_check.py 6 1.8` (exit 0 = all delivered <5s; prints per-file latency;
cleans up its own TEST files):

```python
#!/usr/bin/env python3
"""8xf burst check: inject N TEST signal files into the n8n outbox at SPACING s
apart and print per-file relay latency (outbox write -> file present in the
final drop dir /Users/admin/praxis-signals). Isolates the launchd relay leg
(bypasses n8n, whose leg is measured at +0.15s -- bead qxd).
Usage: python3 burst_check.py [N] [SPACING_S]   (defaults 6, 1.8)
Cleans up its own TEST files from outbox/incoming/drop at the end."""
import json, os, sys, threading, time

OUTBOX = "/Users/admin/n8n-compose/local-files/outbox"
DROP = "/Users/admin/praxis-signals"
N = int(sys.argv[1]) if len(sys.argv) > 1 else 6
SPACING = float(sys.argv[2]) if len(sys.argv) > 2 else 1.8
RUN = time.strftime("%H%M%S")

names, t0, lat = [], {}, {}
done = threading.Event()

def poller():
    # 10ms poll running CONCURRENTLY with the writes (a post-hoc poll would
    # mis-attribute early deliveries to the moment polling starts).
    while not done.is_set():
        for name in names[:]:
            if name not in lat and name in t0 and \
               os.path.exists(os.path.join(DROP, name)):
                lat[name] = time.monotonic() - t0[name]
        time.sleep(0.01)

threading.Thread(target=poller, daemon=True).start()
for i in range(1, N + 1):
    name = f"TEST-8XF-DAEMON-{RUN}-{i:02d}.json"
    payload = {"signal_id": f"TEST-8XF-DAEMON-{RUN}-{i:02d}", "test": True,
               "note": "8xf keepalive-daemon burst check - NOT A TRADE SIGNAL",
               "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    tmp = os.path.join(OUTBOX, "." + name + ".tmp")
    with open(tmp, "w") as f:
        json.dump(payload, f)
        f.flush(); os.fsync(f.fileno())
    os.rename(tmp, os.path.join(OUTBOX, name))  # atomic, like n8n's write node
    t0[name] = time.monotonic()
    names.append(name)
    if i < N:
        time.sleep(SPACING)

deadline = time.monotonic() + 30
while len(lat) < N and time.monotonic() < deadline:
    time.sleep(0.01)
done.set()

print(f"\n{'file':40s} {'latency_s':>9s}  <5s?")
worst = 0.0
for name in names:
    if name in lat:
        v = lat[name]; worst = max(worst, v)
        print(f"{name:40s} {v:9.3f}  {'PASS' if v < 5 else 'FAIL'}")
    else:
        print(f"{name:40s} {'NEVER':>9s}  FAIL")
print(f"max latency: {worst:.3f}s  ({N} files @ {SPACING}s spacing)")

# cleanup: remove ONLY this run's TEST files, wherever they landed
removed = 0
for d in (DROP, os.path.join(DROP, "incoming"), OUTBOX):
    for name in names:
        p = os.path.join(d, name)
        if os.path.exists(p):
            os.remove(p); removed += 1
print(f"cleanup: removed {removed} TEST file(s)")
sys.exit(0 if len(lat) == N and worst < 5 else 1)
```

Kill-restart re-check one-liner:

```bash
OLD=$(launchctl print gui/501/build.praxis.signals-sweep-daemon | awk '/^\tpid =/{print $3}'); \
kill -9 "$OLD"; sleep 2; \
NEW=$(launchctl print gui/501/build.praxis.signals-sweep-daemon | awk '/^\tpid =/{print $3}'); \
echo "old=$OLD new=$NEW"; [ -n "$NEW" ] && [ "$NEW" != "$OLD" ] && echo RESTARTED
```

## 6. Rollback (restore the WatchPaths job)

Only if the daemon must be reverted (accepting the known burst-latency failure):

1. Unload + remove the daemon:
   ```bash
   launchctl bootout gui/$UID/build.praxis.signals-sweep-daemon
   rm ~/Library/LaunchAgents/build.praxis.signals-sweep-daemon.plist
   ```
2. Recreate the old plist. Either render from git history:
   ```bash
   git show <pre-8xf-commit>:deploy/launchd/build.praxis.signals-sweep.plist \
     | sed "s|__BIN_DIR__|$HOME/Library/Application Support/Praxis/bin|g" \
     > ~/Library/LaunchAgents/build.praxis.signals-sweep.plist
   ```
   or write this verbatim (already `__BIN_DIR__`-substituted for this host):
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
     <key>Label</key>
     <string>build.praxis.signals-sweep</string>
     <key>ProgramArguments</key>
     <array>
       <string>/bin/bash</string>
       <string>/Users/admin/Library/Application Support/Praxis/bin/praxis-signals-sweep.sh</string>
     </array>
     <key>StartInterval</key>
     <integer>60</integer>
     <key>WatchPaths</key>
     <array>
       <string>/Users/admin/n8n-compose/local-files/outbox</string>
     </array>
     <key>RunAtLoad</key>
     <true/>
     <key>ProcessType</key>
     <string>Background</string>
     <key>StandardOutPath</key>
     <string>/Users/admin/praxis-signals/logs/signals-sweep.out.log</string>
     <key>StandardErrorPath</key>
     <string>/Users/admin/praxis-signals/logs/signals-sweep.err.log</string>
     <key>EnvironmentVariables</key>
     <dict>
       <key>PATH</key>
       <string>/usr/local/bin:/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin</string>
     </dict>
   </dict>
   </plist>
   ```
3. Load it:
   ```bash
   launchctl bootstrap gui/$UID ~/Library/LaunchAgents/build.praxis.signals-sweep.plist
   launchctl enable gui/$UID/build.praxis.signals-sweep
   ```
4. The sweep script itself needs nothing — `praxis-signals-sweep.sh` is unchanged and
   already deployed in BIN_DIR. stale-check/backlog-check are unaffected either way.
   Never leave BOTH mechanisms unloaded: the relay must always have one live job.

## 7. Files touched (repo)

| File | Change |
|---|---|
| `scripts/praxis-signals-sweep-daemon.sh` | NEW — 1s-loop daemon wrapping the unchanged sweep script |
| `deploy/launchd/build.praxis.signals-sweep-daemon.plist` | NEW — KeepAlive/RunAtLoad template, no WatchPaths |
| `deploy/launchd/build.praxis.signals-sweep.plist` | DELETED — superseded (rollback copy embedded above) |
| `scripts/praxis-signals-install.sh` | v3 — daemon in SCRIPTS/LABELS, legacy-job removal, bootout/bootstrap race fix |
| `MANIFEST.md` | rows appended for the above |
| `docs/reports/2026-07-12-8xf-keepalive-daemon.md` | this report |
