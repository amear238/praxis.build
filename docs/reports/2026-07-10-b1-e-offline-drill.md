# B1-e — Offline Failure Drill (LOCAL topology) — bead Praxis_build-63b

Date: 2026-07-10
Scope: RE-SCOPED to the LOCAL topology per D-2026-07-09-D (no WireGuard tunnel in
build-first). Drill on the LIVE monitoring path. Goal: prove the three
failure-visibility / no-silent-loss guarantees by injecting a relay-path failure.

Runtime under test (internal-disk deployment):
- Sweep:  `~/Library/Application Support/Praxis/bin/praxis-signals-sweep.sh`
- Stale:  `~/Library/Application Support/Praxis/bin/praxis-signals-stale-check.sh`
- LaunchAgents: `build.praxis.signals-sweep` (WatchPaths outbox + 60s), `build.praxis.signals-stale-check` (120s) — both loaded, status 0.
- OUTBOX `/Users/admin/n8n-compose/local-files/outbox` ; DROP `/Users/admin/praxis-signals` ; staging `DROP/incoming` ; heartbeat `DROP/.heartbeat`.

---

## 1. KEY QUESTION — is the heartbeat touched UNCONDITIONALLY on a drop-path failure?

**YES — unconditionally, and this is the critical finding.** The sweep's promotion
step swallows failure, then writes the heartbeat regardless. Verbatim from the
deployed `praxis-signals-sweep.sh`:

```bash
# 2. staging -> final drop dir (atomic rename; *.json glob excludes rsync temp dotfiles)
for f in "$INCOMING"/*.json; do
  mv -f "$f" "$DROP/$(basename "$f")" 2>/dev/null || true   # <-- mv failure SWALLOWED
done

shopt -u nullglob

# 3. heartbeat
date +%s > "$HEARTBEAT" 2>/dev/null || true                  # <-- written UNCONDITIONALLY
exit 0
```

The heartbeat write is decoupled from step-2 success. Because `HEARTBEAT` is the
**pre-existing** file `$DROP/.heartbeat` (mode 644, owned by admin), the redirect
`> $HEARTBEAT` needs only *file*-write permission on that file — NOT *directory*-write
permission on `$DROP`. The `mv` into `$DROP/<name>`, by contrast, needs *directory*-write
on `$DROP`. These two permissions are decoupled, so a class of drop-path failure exists
where **the promotion fails but the heartbeat still refreshes** — the sweep looks alive
while it is silently dropping the backlog into limbo.

---

## 2. Injection method (least-destructive, reversible)

Two failure classes tested, distinguished by whether the heartbeat can still be written:

- **Class A — "drop dir read-only / promotion fails, heartbeat file still writable":**
  `chmod 500 $DROP` (remove dir-write, KEEP traverse). rsync can still stage into
  `incoming/`; `mv` into `$DROP` fails; `> $DROP/.heartbeat` still succeeds. This is the
  silent-failure case.
- **Class B — "sweep dead / share unmounted, heartbeat cannot advance":** simulated its
  downstream effect by aging `$DROP/.heartbeat` to `now-1000s`. This is the case the
  stale-check is designed to catch.

Baseline perms recorded for exact restore:
```
drwxr-xr-x 40755 admin:staff  /Users/admin/praxis-signals
drwxr-xr-x 40755 admin:staff  /Users/admin/praxis-signals/incoming
-rw-r--r-- 100644 admin:staff  /Users/admin/praxis-signals/.heartbeat
```
Restored perms (verified identical): 755 / 755 / 644. No data deleted; DROP dir and its
contents never removed.

---

## 3. Evidence

### Class A — chmod 500 (silent-failure hypothesis)

Dropped `drill-1.json`, `drill-2.json`, `drill-3.json` (valid JSON) into OUTBOX, injected
`chmod 500 $DROP`, ran the deployed sweep (identical to what launchd WatchPaths fires):

- **Where files landed:** rsync staged all 3 OUTBOX -> `DROP/incoming/` (incoming still
  writable); `mv incoming -> DROP` **FAILED** -> all 3 files **retained in `DROP/incoming/`**.
  OUTBOX empty. DROP root received none. **No loss.**
- **Heartbeat:** advanced despite the mv failure — `hb_pre=1783693309 -> hb_post=1783693341`,
  age `0s`. **FRESH.**
- **Alert:** ran `praxis-signals-stale-check.sh` — heartbeat fresh (age < 180s) so it took
  the recovery branch: **no notify, no latch, no alert-log line.** `stale-check exit=0`,
  `.stale-alerted` absent. **NO ALERT FIRED.**

Result: relay path broken, 3-signal backlog stuck in `incoming/`, monitoring shows GREEN.
**Failure is INVISIBLE.**

### Replay (after restore)

`chmod 755 $DROP` (restore), re-ran sweep: all 3 `drill-*.json` promoted from `incoming/`
into `DROP` root; `incoming/` empty; OUTBOX empty. Backlog replayed intact.

### Class B — heartbeat aged to 1000s (alert mechanism validation)

Aged `.heartbeat` to `now-1000s`, ran stale-check LIVE (real notify path):

- Latch `.stale-alerted` created; durable line appended to `logs/signals-alerts.log`:
  `ALERT FIRED 1783693401 (2026-07-10T14:23:21Z) age=1000s threshold=180s ...`
- **n8n execution:** workflow `8l0cKKcLo25IIhpe` (Orchestrator-Mine Notify), execution
  **`1088642`**, status `success`, `2026-07-10T14:23:21.324Z`. Webhook body:
  `{"event":"praxis-signals-stale","project":"Praxis.build","detail":"signals-sweep heartbeat stale: 1000s > 180s threshold ..."}`.
- **Telegram:** `Send Telegram Ping` node returned `ok:true`, **`message_id: 44`**, chat
  `6156528469` (Amear), text `"🤖 Orchestrator-Mine — praxis-signals-stale ... heartbeat stale: 1000s > 180s threshold ..."`.

The alert path is LIVE and correct **when the heartbeat actually goes stale.**

---

## 4. Guarantee verdicts

| # | Guarantee | Verdict | Basis |
|---|-----------|---------|-------|
| 1 | **Spool (no silent loss)** | **PASS** | Under both failure classes signals are retained — Class A: 3 files held in `incoming/`; upstream failures leave them in OUTBOX. Never deleted. |
| 2 | **Alert / failure VISIBLE** | **CONDITIONAL — FAIL for the promotion-only class** | Class B (heartbeat stale) fires a real Telegram alert (exec 1088642, msg 44). Class A (promotion fails, heartbeat file still writable) fires **NOTHING** — see Finding F-B1e-1. |
| 3 | **Replay on restore** | **PASS** | After perm restore, the spooled backlog promoted from `incoming/` to the drop root on the next sweep, intact. |

---

## 5. FINDING F-B1e-1 (SEVERITY: HIGH) — promotion failure is SILENT

**A relay-path failure that leaves `$DROP/.heartbeat` writable but blocks promotion into
`$DROP` (dir made read-only, quota/ENOSPC on the rename target while the small heartbeat
write still fits, an SMB/VM share remounted read-only where the inode stays writable, or a
per-file mv error) is INVISIBLE to the monitoring path.** The sweep's `mv ... 2>/dev/null || true`
swallows the error and the *unconditional* heartbeat write keeps the heartbeat fresh, so
`stale-check` never fires. Signals silently accumulate in `incoming/` (not lost, but never
delivered to NT8) with zero alert. For an automated trading system this means live signals
can stop reaching the platform while every monitor reads healthy.

The stale-heartbeat mechanism only covers failures that ALSO stop the heartbeat (sweep
process dead, Mac asleep, whole DROP path unreachable/unwritable-including-`.heartbeat`,
`chmod 000`). It does not cover promotion-only failures.

**Recommended fix (file a follow-up bead, not done here):** make the heartbeat conditional
on the relay actually being healthy — e.g. only `touch` the heartbeat after a successful
mv (or when `incoming/` is empty post-sweep), and/or add a distinct alert branch when
`incoming/*.json` files persist across N consecutive sweeps (backlog-stuck detector).
The n8n write-error branch on workflow `EmMbN4sslwIx1ydn` only covers the *upstream* write
to OUTBOX failing — it does not see a stuck sweep promotion.

---

## 6. Restore / final health (drill on the LIVE path — verified healthy)

- Perms restored EXACTLY: `$DROP` 755, `incoming` 755, `.heartbeat` 644.
- All `drill-*.json` removed from OUTBOX, `incoming/`, and DROP root (`find` confirms none).
- Latch `.stale-alerted` cleared (auto-cleared by stale-check on heartbeat recovery, then
  confirmed absent).
- Drill-created `logs/signals-alerts.log` removed (did not exist at baseline); pre-existing
  launchd `.out/.err` logs in `logs/` untouched.
- Heartbeat fresh and advancing under live launchd (age < 30s, threshold 180s).
- Both LaunchAgents loaded, status 0.
- DROP dir contents identical to baseline (`.heartbeat`, `2026-07-09T20-24-00Z-SIM-B1B-0001.json`,
  `incoming/`, `logs/`, `signal-template.json`).

Monitoring left EXACTLY healthy.
