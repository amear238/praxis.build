# B1-c-fu — Signals Stale-Heartbeat Alert Live-Fire (bead Praxis_build-4hd)

**Date:** 2026-07-09
**Goal:** Fire ONE real stale-heartbeat Telegram alert end-to-end (send-side verified) and leave the sweep reloaded HEALTHY.
**Result:** PASS (send-side). Sweep reloaded and heartbeat advancing. Receive-side (phone) is trader-only — see note.

## Facts read from the runtime scripts (internal disk `~/Library/Application Support/Praxis/bin/`)
- Heartbeat file: `/Users/admin/praxis-signals/.heartbeat` (content = epoch seconds; age computed from the epoch INSIDE the file, not mtime).
- **Staleness threshold: 180s** (`PRAXIS_HEARTBEAT_THRESHOLD` default in `praxis-signals-stale-check.sh`).
- Latch file: `/Users/admin/praxis-signals/.stale-alerted` (created on fire, content = fire epoch; one alert per stale episode; auto-removed once heartbeat recovers).
- Notifier: `~/Library/Application Support/Praxis/bin/notify.sh` → `curl POST` to `ORCH_N8N_WEBHOOK`.
- Webhook (from `~/.praxis/signals.env`): `https://n8n.myzerker626.win/webhook/orchestrator-notify` → n8n workflow **`8l0cKKcLo25IIhpe` "Orchestrator-Mine Notify"** → Telegram chat `6156528469`.
- Log paths (launchd stdout/stderr): `/Users/admin/praxis-signals/logs/signals-stale-check.{out,err}.log`. NOTE: neither script writes a "fired" line to stdout on a successful alert, so the authoritative send-side evidence is the n8n execution + latch, not the log.

## Timeline (real timestamps; EDT / UTC)
| Step | Time (EDT) | Time (UTC) | Evidence |
|---|---|---|---|
| Pre-check: latch absent, both jobs loaded | 16:31:10 | 20:31:10Z | heartbeat content=1783629010→refreshed to 1783629070; latch NOT present |
| Boot out sweep (`launchctl bootout …signals-sweep`), rc=0 | 16:31:29 | 20:31:29Z | last heartbeat written content=**1783629070** (mtime 16:31:10Z); `launchctl list` showed only `signals-stale-check` |
| Heartbeat aged past threshold (sweep stopped) | 16:34:32 | 20:34:32Z | hb_content=1783629070, **age=202s > 180s** |
| **Fire:** invoked `praxis-signals-stale-check.sh` directly (rc=0) | 16:34:32 | 20:34:32Z | latch created: `/Users/admin/praxis-signals/.stale-alerted` content=**1783629272** (mtime 20:34:32Z) |
| n8n webhook execution | 16:34:32 | 20:34:32.529Z | exec **1069379**, status **success** |
| Telegram send | 16:34:32 | 20:34:33Z | Telegram API `ok:true`, **message_id 28** |
| Reload sweep (`bootstrap` + `kickstart`) | 16:35:19 | 20:35:19Z | heartbeat refreshed content=1783629319, mtime 20:35:19Z |
| Latch cleared; final health | 16:35:32 | 20:35:32Z | latch absent; hb age 13s and advancing; both jobs loaded |

## Send-side evidence (n8n execution 1069379)
- **Webhook input body** (from `notify.sh` via `curl/8.7.1`):
  - `event`: `praxis-signals-stale`
  - `project`: `Praxis.build`
  - `detail`: `signals-sweep heartbeat stale: 202s > 180s threshold (heartbeat=/Users/admin/praxis-signals/.heartbeat)`
- **Telegram node** `Send Telegram Ping`: executionStatus success, Telegram API returned `ok:true`, `message_id`: **28**, chat `6156528469` (Amear Bani Ahmad), text:
  `🤖 Orchestrator-Mine — praxis-signals-stale` / `Project: Praxis.build` / `signals-sweep heartbeat stale: 202s > 180s threshold (heartbeat=/Users/admin/praxis-signals/.heartbeat)`
- Execution: startedAt 2026-07-09T20:34:32.529Z, stoppedAt 2026-07-09T20:34:33.046Z, mode webhook, status success.

## Sweep restored HEALTHY (confirmed)
- `launchctl bootstrap` rc=0, `kickstart` rc=0; `launchctl list | grep praxis` shows BOTH `build.praxis.signals-sweep` and `build.praxis.signals-stale-check` loaded (status 0).
- Heartbeat advancing: content=1783629319, mtime 2026-07-09T20:35:19Z, age 13s at final check (was 202s stale during the fire).
- Latch `/Users/admin/praxis-signals/.stale-alerted` removed → a future real stale episode will alert again.

## Note on a pre-existing log line (not from this run)
`signals-stale-check.err.log` tail shows an old `Operation not permitted` line referencing the EXTERNAL-volume path `/Volumes/Sensidine/Praxis.build/scripts/praxis-signals-stale-check.sh` — that is a stale TCC error from a prior source-tree invocation, NOT this test. This run executed the internal-disk runtime copy and returned rc=0, and the fire is proven by the latch + n8n exec 1069379.

## RECEIVE-side caveat
**Verified SEND-side only.** The n8n execution + Telegram API `ok:true` (message_id 28) prove the message was accepted by Telegram for delivery. Whether the alert actually appeared on the trader's phone can ONLY be confirmed by the trader.

---

## Re-fire with raw evidence (2026-07-10)

**Why a re-fire:** The prior fire's only durable send-side handle was n8n execution `1069379`, which n8n PRUNED (regular executions drop in <1 day) — a `get_execution` on it now returns "not found", so no durable evidence survived the audit. This section RE-FIRES and embeds VERBATIM raw send-side evidence captured at fire time, plus adds a durable local fired-line trail (see "Durability improvement" below) so future fires no longer depend on n8n retention.

**Result:** PASS (send-side). One real stale alert fired. Sweep restored HEALTHY (both jobs loaded, heartbeat advancing, latch cleared).

### Fresh handles (auditor: re-query within minutes)
- **n8n execution id: `1087018`** (workflow `8l0cKKcLo25IIhpe`, status `success`).
- **Telegram `message_id: 29`**, chat `6156528469` (Amear Bani Ahmad), `ok:true`.

### Timeline — real timestamps (EDT = UTC−4)
| Step | Epoch | UTC | Evidence |
|---|---|---|---|
| Pre-check: latch absent, both jobs loaded | 1783689863 | 2026-07-10T13:24:23Z | `launchctl list` showed both jobs; latch NOT present |
| Boot out sweep (`launchctl bootout gui/$UID/build.praxis.signals-sweep`) rc=0 | ~1783689864 | 2026-07-10T13:24:24Z | `launchctl list \| grep praxis` then showed ONLY `build.praxis.signals-stale-check` |
| Heartbeat forced stale (content+mtime set to now−600) | 1783689264 | 2026-07-10T13:14:24Z (mtime) | heartbeat **content=1783689264** |
| Staleness confirmed | 1783689865 | 2026-07-10T13:24:25Z | **age = 1783689865 − 1783689264 = 601s > 180s** → STALE |
| **FIRE:** invoked `~/Library/Application Support/Praxis/bin/praxis-signals-stale-check.sh` directly, **rc=0** | 1783689865 | 2026-07-10T13:24:25Z | latch created content=**1783689865** (mtime 13:24:25Z) |
| n8n webhook execution | — | 2026-07-10T13:24:25.540Z (started) → 13:24:26.560Z (stopped) | exec **1087018** status **success** |
| Telegram send | 1783689866 | 2026-07-10T13:24:26Z | Telegram API `ok:true`, **message_id 29** |
| Restore sweep (`launchctl bootstrap` + `kickstart -k`) rc=0/rc=0 | ~1783689906 | 2026-07-10T13:25:06Z | heartbeat content refreshed to 1783689906 |
| Latch cleared; final health | 1783689912 | 2026-07-10T13:25:12Z | latch absent; heartbeat age 6s and advancing; both jobs loaded |

Staleness math (verbatim from the fire run):
```
AGE = NOW(1783689865) - HBcontent(1783689264) = 601s  (threshold 180s) -> STALE=YES
```

### VERBATIM raw n8n execution `1087018` (captured at fire time, before pruning)

Metadata (`get_execution` envelope):
```json
{"execution":{"id":"1087018","workflowId":"8l0cKKcLo25IIhpe","mode":"webhook","status":"success","startedAt":"2026-07-10T13:24:25.540Z","stoppedAt":"2026-07-10T13:24:26.560Z","retryOf":null,"retrySuccessId":null,"waitTill":null}}
```

Webhook input node `Orchestrator Notify` — raw received body (from `notify.sh` via `curl/8.7.1`):
```json
{"json":{"headers":{"host":"n8n.myzerker626.win","user-agent":"curl/8.7.1","content-length":"177","accept":"*/*","accept-encoding":"gzip, br","cdn-loop":"cloudflare; loops=1","cf-connecting-ip":"99.239.66.230","cf-ipcountry":"CA","cf-ray":"a18fe37b8bb444b0-YYZ","cf-visitor":"{\"scheme\":\"https\"}","cf-warp-tag-id":"309cd22e-1b66-4c69-829c-01a6c89d5372","connection":"keep-alive","content-type":"application/json","x-forwarded-for":"99.239.66.230","x-forwarded-proto":"https"},"params":{},"query":{},"body":{"event":"praxis-signals-stale","project":"Praxis.build","detail":"signals-sweep heartbeat stale: 601s > 180s threshold (heartbeat=/Users/admin/praxis-signals/.heartbeat)"},"webhookUrl":"https://n8n.myzerker626.win/webhook/orchestrator-notify","executionMode":"production"}}
```

Telegram node `Send Telegram Ping` — raw HTTP response (`executionStatus":"success"`, `executionTime":1015`ms):
```json
{"json":{"ok":true,"result":{"message_id":29,"from":{"id":8344523288,"is_bot":true,"first_name":"orchastrator_bot","username":"orchastrator_Mine_bot"},"chat":{"id":6156528469,"first_name":"Amear","last_name":"Bani Ahmad","type":"private"},"date":1783689866,"text":"🤖 Orchestrator-Mine — praxis-signals-stale\nProject: Praxis.build\nsignals-sweep heartbeat stale: 601s > 180s threshold (heartbeat=/Users/admin/praxis-signals/.heartbeat)","entities":[{"offset":23,"length":20,"type":"bold"},{"offset":53,"length":12,"type":"url"}]}}}
```

`runData` node summary (verbatim): `Orchestrator Notify` → `executionStatus":"success"`; `Send Telegram Ping` → `executionStatus":"success"`, `lastNodeExecuted":"Send Telegram Ping"`.

### notify.sh / curl surface
`notify.sh` fires `curl -s -m 10 -X POST … >/dev/null 2>&1` and by contract discards the HTTP response (it must never fail its caller), so no curl status is surfaced locally. The stale-check runtime returned **rc=0** and the latch was created — the authoritative send-side proof is the n8n execution above (`1087018`, Telegram `ok:true`, `message_id 29`).

### Sweep restored HEALTHY (confirmed)
```
$ launchctl list | grep -i praxis
-	0	build.praxis.signals-stale-check
-	0	build.praxis.signals-sweep
```
- `launchctl bootstrap` rc=0, `kickstart -k` rc=0 → BOTH jobs loaded (status 0).
- Heartbeat advancing: content refreshed 1783689264 (stale) → 1783689906 → 1783689966; final age 6s→19s (was 601s during the fire).
- Latch `/Users/admin/praxis-signals/.stale-alerted` removed → next real stale episode will alert again.

### Durability improvement (repo source `scripts/praxis-signals-stale-check.sh`)
Root cause of the failed audit was that no durable send-side trail survives n8n pruning. Fix (append-only, failure-tolerant):
- Added `ALERT_LOG` (default `/Users/admin/praxis-signals/logs/signals-alerts.log`, override `PRAXIS_ALERT_LOG`).
- On each fire, after `notify.sh` and latch creation, the script now appends one line:
  `ALERT FIRED <epoch> (<UTC>) age=<age>s threshold=<threshold>s heartbeat=<path>`.
- The n8n execution id is intentionally NOT in this line — `notify.sh` discards the curl response, so the exec id is unavailable to the script; the authoritative send-side record stays the n8n execution (embedded verbatim above), and this line is the durable LOCAL trail that survives pruning.
- Re-deployed to the internal runtime copy via `scripts/praxis-signals-install.sh deploy` (copies only; does NOT reload launchd — the next 120s stale-check invocation reads the updated file). Verified: internal copy `diff`-identical to repo source; `bash -n` syntax OK; dry-run against a scratch dir wrote exactly one fired-line and the latch correctly suppressed a second line on re-run.
- NOTE: this run's fire (exec `1087018`) executed the PRE-improvement internal copy, so `signals-alerts.log` did not yet exist for it; the durable line applies to all FUTURE fires. This run's durable evidence is the verbatim n8n execution embedded above.
