# 8xf — E2E Latency Investigation: where the ~4.2s goes, burst failure root cause

**Bead:** Praxis_build-8xf
**Date:** 2026-07-12
**Type:** Report (investigation only — no code changed, no jobs touched, all test artifacts cleaned up)
**Path under test:** `webhook (public CF tunnel + localhost) → n8n workflow EmMbN4sslwIx1ydn → /files/outbox → launchd WatchPaths sweep → /Users/admin/praxis-signals/` (NT8 consumer not installed — drops inert)

---

## TL;DR — the two root causes (both CONFIRMED, neither was the suspected one alone)

1. **~4.0s of the "4.2s" is an n8n bug, not transport:** the "Write Signal File" Code node
   *succeeds at writing the file in ~150 ms on its first attempt*, but n8n's task-runner
   layer marks attempts 1 and 2 as failed and re-runs the node under its
   `retryOnFail: maxTries=3, waitBetweenTries=2000ms` config. Node `executionTime` is a
   deterministic **4022–4035 ms on every execution** (= 2 × 2000 ms waits + ~25 ms of work).
   The file is physically (re)written 3 times, 2.0 s apart.
2. **launchd's default 10 s respawn throttle on the WatchPaths sweep job** (`ThrottleInterval`
   absent from the deployed plist; `launchctl print` shows `minimum runtime = 10`) pins sweep
   runs to ≥10 s apart under load. Because cause #1 makes *every* signal generate 3 outbox
   writes (plus the sweep's own removals re-fire WatchPaths), the throttle window is almost
   always hot — so even **isolated** signals sometimes wait for a throttled respawn
   (ISO-2 below: 7.36 s), and bursts reliably blow the 5 s budget.

Also: **the previously reported "consistent ~4.3s e2e" (B1-d) is partly a measurement
artifact.** The blocking `curl` (4.2 s, held open by the retry stall) ran *before* polling
began, so the first deliverable copy — swept to the drop dir in **as little as 0.5–0.9 s** —
was never observed. True delivery latency is bimodal: **~0.5–1 s when the sweep is
unthrottled, up to ~10.4 s when throttled.** The HTTP 200 back to TradingView is always
~4.2 s late regardless.

---

## 1. Deployed-vs-repo drift check (ground truth first)

| Deployed artifact | vs repo source | Result |
|---|---|---|
| `~/Library/Application Support/Praxis/bin/praxis-signals-sweep.sh` | `scripts/praxis-signals-sweep.sh` | byte-identical |
| `~/Library/Application Support/Praxis/bin/praxis-signals-{backlog,stale}-check.sh` | `scripts/...` | byte-identical |
| `~/Library/LaunchAgents/build.praxis.signals-*.plist` (×3) | `deploy/launchd/...` | identical modulo installer's `__BIN_DIR__` substitution |

**No drift.** Sweep plist: `WatchPaths=[outbox]`, `StartInterval=60` backstop, `RunAtLoad`,
**no `ThrottleInterval` key in any of the three plists** → 10 s default applies.
`launchctl print gui/501/build.praxis.signals-sweep`: `minimum runtime = 10`, runs = 2828.

## 2. Steady-state leg breakdown (isolated signals, ≥20 s apart)

Method: Python harness (10 ms pollers on outbox/incoming/drop + outbox dir-event watcher +
heartbeat watcher), TEST payloads per B1-d schema (`signal_id` prefix `TEST-8XF-`), public
URL `https://n8n.myzerker626.win/webhook/praxis-signal` (Cloudflare 403s non-curl
User-Agents — spoofed `curl/8.7.1`). Cross-checked against n8n execution runData and
`~/.n8n/n8nEventLog.log` inside the container.

Where each leg's time goes (composite of 5 isolated runs + n8n event-log timestamps):

| Leg | Measured |
|---|---|
| curl → webhook receipt (public, CF tunnel) | ~0.15 s (localhost: 0.003 s — tunnel exonerated) |
| webhook → Validate (Code) → IF | 3–5 ms |
| Write node attempt 1 → **file complete in outbox** | **t0 + ~0.15 s** (dir watcher: APPEAR at +0.151 s) |
| n8n spurious-retry stall (attempts 2, 3 at +2.0 s, +4.0 s) | **+4.02 s** (node executionTime 4022 / 4031 / 4035 ms) |
| HTTP 200 to caller | t0 + 4.19–4.37 s |
| WatchPaths fire → sweep spawn | 0.3–0.7 s unthrottled; **up to 10.2 s throttled** |
| sweep itself (rsync → incoming → mv → drop) | 0.03–0.25 s |

Isolated-run results (poll-after-response e2e vs true first-copy-in-drop from
mtime + heartbeat evidence):

| Run | HTTP resp | e2e (B1-d-style, post-curl poll) | TRUE first copy in drop |
|---|---|---|---|
| ISO-1 | 4.193 s | 4.193 s | **~0.50 s** (swept at +0.47 s) |
| ISO-2 | 4.189 s | 7.355 s | **7.36 s** (sweep throttled by ISO-1's duplicate-write chain) |
| ISO-3 | 4.368 s | 4.368 s | **~0.57 s** |

**ISO-2 is the smoking gun for the self-inflicted throttle:** its file hit the outbox 3.0 s
after a sweep spawn (triggered by ISO-1's duplicate rewrite), so it waited out the 10 s
throttle window. Even at 20 s signal spacing, <5 s is not guaranteed today.

### Write-node retry evidence (n8n event log, execution 1144747)
```
10:11:54.257 runner.task.requested  (attempt 1)   → response.received +5 ms   → judged FAILED
10:11:56.266 runner.task.requested  (attempt 2)   → response.received +11 ms  → judged FAILED
10:11:58.281 runner.task.requested  (attempt 3)   → response.received +10 ms  → SUCCESS, node.finished
```
- Every attempt's `writeFileSync + renameSync` **physically lands** (outbox dir watcher saw
  the file appear at +0.15 s / +2.17 s / +4.17 s; `.tmp` visible on some runs).
- Raw probe inside the container (`docker exec … node -e 'writeFileSync; renameSync'` to
  `/files/outbox`): **write 1 ms, rename 0 ms, no error** → filesystem/bind-mount is not
  the failure; the failure is in the n8n↔task-runner result path
  (`@n8n/task-runner` process confirmed running; `NODE_FUNCTION_ALLOW_BUILTIN=fs` set).
- The exact exception string is **not recoverable without touching prod** (event log has
  0 `node.error`/`task.error` events at info level; retried-then-succeeded attempts keep
  only the final runData). 30-second diagnostic for the fix bead: duplicate the workflow,
  set the Write node `maxTries=1`, execute once — the error surfaces in execution output.
- Side effect worth noting: each signal is promoted to the drop dir **2–3 times** (same
  filename, `mv -f`, byte-identical content). Benign under the 9tl in-file `signal_id`
  dedup contract, but the NT8 FileSystemWatcher will see multiple change events per signal.

## 3. Burst reproduction (6 signals, true 1.8 s spacing, concurrent senders)

| # | HTTP resp | e2e (post-resp poll) | TRUE first copy in drop | <5 s? |
|---|---|---|---|---|
| BURST2-1 | 4.267 s | 4.268 s | 0.86 s | PASS |
| BURST2-2 | 4.194 s | 9.153 s | 9.11 s | **FAIL** |
| BURST2-3 | 4.198 s | 7.374 s | 7.32 s | **FAIL** |
| BURST2-4 | 4.232 s | 5.589 s | 5.52 s | **FAIL** |
| BURST2-5 | 4.189 s | 4.189 s | 3.71 s | PASS |
| BURST2-6 | 4.285 s | 4.285 s | 2.02 s | PASS |

**3/6 FAIL; max 9.15 s.** An earlier semi-burst at ~6 s effective spacing also failed 3/6
(max 8.42 s) — the cadence assumption "safe if >5 s apart" is false.

**Throttle hypothesis CONFIRMED, with mechanism:** heartbeats show sweep spawns at
805.8 → 816.0 (exactly 10.2 s; earlier chain 726.3 → 737.0 → 747.1 → 757.2, i.e.
+10.7/+10.1/+10.1 s) while outbox events arrived continuously; all six queued files were
released in one batch sweep at 816.0. Per-signal penalty = time from its outbox write to
the next allowed spawn: 0–10.2 s. Worst case observed 9.15 s; theoretical worst
~0.15 + 10.2 + 0.25 ≈ **10.6 s** (the 60 s StartInterval backstop is never needed for this —
pending WatchPaths events do respawn the job once the throttle window expires).
Unified log (`log show`) returned nothing for launchd/sweep without sudo; the
`launchctl print` throttle value + measured 10 s spawn pinning stand as evidence.

## 4. Options analysis and recommendation

| Option | Worst-case relay leg | Complexity | Failure modes |
|---|---|---|---|
| (a) StartInterval short poll (e.g. 5 s) | interval + 0.25 s — **but** launchd still throttles respawns at 10 s unless `ThrottleInterval` is also lowered; at intervals ≤2 s it's a polling daemon with per-run spawn overhead | plist-only | constant respawn churn; still >5 s e2e once n8n's 4.2 s HTTP stall is added on bursts landing mid-interval |
| **(b) persistent KeepAlive daemon (1 s sweep loop)** ★ | **~1.3 s** (1 s sleep + 0.3 s sweep), no respawn ⇒ no throttle, immune to fsevents storms and duplicate rewrites | small: wrap existing sweep in `while :; do sweep; sleep 1; done`, plist gains `KeepAlive`, drops `WatchPaths`/`StartInterval` | daemon dies → KeepAlive respawns (≤10 s gap on crash-loop); daemon *hangs* → KeepAlive won't help, but heartbeat now updates every ~1 s so the existing stale-check alarm catches it fast; optional belt-and-braces: keep a separate 60 s StartInterval sweep (concurrent runs are safe: rsync `--remove-source-files` + `mv -f` are race-tolerant) |
| (c) accept + document cadence assumption | 10.6 s | none | **not viable today**: the n8n duplicate-write chain keeps the throttle window hot, so even isolated signals >20 s apart measured 7.36 s |

**RECOMMENDATION: (b) persistent KeepAlive watcher daemon (1 s sweep loop).**
It removes the launchd throttle from the equation entirely (no respawns), bounds the relay
leg at ~1.3 s regardless of burst cadence or the n8n duplicate writes, reuses the existing
sweep script and stale-check monitoring unchanged (heartbeat gets *fresher*), and its
failure mode (crash → KeepAlive restart, hang → stale-check alert) is strictly better than
today's silent 10 s coalescing.

**Required companion fix (file as separate bead):** the n8n "Write Signal File"
spurious-retry stall. Even with daemon relay it (i) delays the HTTP 200 to TradingView by
~4 s on every signal (webhook-timeout risk at TV's end), (ii) triples outbox writes /
drop-dir events, (iii) was the hidden cause of B1-d's thin margin. Diagnostic path:
clone workflow, `maxTries=1`, run once, read the error. Do not simply remove `retryOnFail`
on prod without knowing the error — attempt 1's write does succeed, so the retry config is
currently masking a false-negative failure signal, not a real write failure.

## 5. Cleanup / no-touch attestation
- 18 `TEST-8XF-*` files removed from the drop dir; outbox and incoming empty; drop dir
  restored to prior state (`2026-07-09T20-24-00Z-SIM-B1B-0001.json` + `signal-template.json`
  untouched). No launchd job, plist, workflow, or container was modified/restarted.
- Residue from tests while they ran: 12 Telegram "PRAXIS signal" notifications fired to the
  trader's channel (unavoidable — success path notifies); all payloads clearly marked TEST-8XF.
- Harness: `measure_8xf.py` in session scratchpad (not committed).
