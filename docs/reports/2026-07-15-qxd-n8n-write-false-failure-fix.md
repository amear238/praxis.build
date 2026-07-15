# qxd — n8n "Write Signal File" false-failure retries: root cause + fix

**Bead:** Praxis_build-qxd (P3)
**Date:** 2026-07-15
**Type:** Implementer report — FIXED and verified live (prod n8n workflow `EmMbN4sslwIx1ydn`)
**Predecessor:** docs/reports/2026-07-12-8xf-latency-investigation.md (established: writes succeed on disk in ~1 ms, task-runner layer marks attempts failed, retryOnFail adds 2×2 s, every webhook HTTP 200 delayed ~4 s, every signal written 3×)

---

## TL;DR

- **There is no task-runner exception.** The 8xf hypothesis ("failure is in the n8n↔task-runner
  result path") was wrong in one detail: no error is ever thrown anywhere. The bug is a
  **payload-field-name collision with n8n-core's retryOnFail success check**.
- n8n 2.27.4's retry loop judges a node attempt *failed* if the **first output item has a
  `json.error` property** that is anything other than `undefined`/`null`/`false`. Our Validate
  node emits `error: ""` (empty string, from `errs.join('; ')`) on **valid** signals, and the
  Write node copies it through — so every *successful* write was judged failed and retried
  until the last permitted attempt, whose result is accepted unconditionally.
- **Fix (one line, Validate node):** only include the `error` key when the payload is invalid.
  Invalid-path behavior (Respond 400 / Telegram Rejected, both of which read `$json.error`)
  is unchanged; the invalid path never reaches the Write node.
- **After:** HTTP 200 in **0.043 s** (was 4.19–4.37 s), **1** Write-node attempt
  (executionTime 4 ms, was 4022–4035 ms), **exactly 1** outbox file per signal (was 3).
  `retryOnFail 3x/2s` retained as a genuine safety net for real write errors (real errors
  `throw`, which takes the catch path, not this heuristic).

## 1. Root cause (verbatim from deployed code)

`workflow-execute.js` in the running container
(`/usr/local/lib/node_modules/n8n/node_modules/.pnpm/n8n-core@file+packages+core_…/node_modules/n8n-core/dist/execution-engine/workflow-execute.js`, n8n 2.27.4, lines ~931–933 and ~977–984):

```js
const isErrorValue = (v) => v !== undefined && v !== null && v !== false;
const checkFailure = (data) => !(0, requests_response_1.isEngineRequest)(data) && isErrorValue(data.data?.[0]?.[0]?.json?.error);
...
let runNodeData = await this.runNode(workflow, executionData, this.runExecutionData, runIndex, this.additionalData, this.mode, this.abortController.signal, subNodeExecutionResults);
let nodeFailed = checkFailure(runNodeData);
while (nodeFailed && tryIndex !== maxTries - 1) {
    await (0, n8n_workflow_1.sleep)(waitBetweenTries);
    runNodeData = await this.runNode(...);
    nodeFailed = checkFailure(runNodeData);
    tryIndex++;
}
```

Chain of events per signal, before the fix:

1. Validate node (valid signal) outputs `{ valid: true, error: "", fileName, body }` —
   `error: ""` comes from `errs.join('; ')` with zero errors.
2. Write node succeeds in ~1–4 ms and returns `Object.assign({}, it.json, { written })`,
   **preserving `error: ""`**.
3. `isErrorValue("")` → `true` (empty string is not undefined/null/false) → `checkFailure`
   → `nodeFailed = true` → sleep 2000 ms → re-run → same result → sleep 2000 ms → re-run.
4. On the final permitted attempt the while-condition `tryIndex !== maxTries - 1` stops the
   loop and the (identical) result is **accepted as success** — which is why 8xf saw the
   deterministic fail/fail/succeed pattern with zero `node.error`/`task.error` events, and
   why the exact "exception" was unrecoverable: **there never was one**.

Why the 8xf 30-second diagnostic ("set maxTries=1, read the error") found no error either:
with `retryOnFail` off, `maxTries` is forced to 1, the while-loop never runs, and the node
succeeds immediately. The failure only exists while a retry remains — proof it is the retry
heuristic itself, not the write. (Note `checkFailure` runs even when `retryOnFail` is off,
but with `maxTries=1` it can never trigger a re-run.)

### Controlled confirmation matrix (test clone `O55pofWpaKU300WC`, deleted after)

| Exec | Write-node config | Validate emits `error:""`? | HTTP time | Write executionTime | Outbox writes (consumer journal) |
|---|---|---|---|---|---|
| 1245860 | retry 3x/2s (prod config) | yes | 4.044 s | 4016 ms | 3 (ACCEPTED + 2 DUPLICATE) |
| 1245865 | retryOnFail off | yes | 0.016 s | 2 ms | 1 |
| 1245871 | retry 2x/2s | yes | 2.026 s | 2011 ms | 2 (ACCEPTED + 1 DUPLICATE) |
| 1245891 | **retry 3x/2s (prod config)** | **no (fixed)** | 0.025 s | 3 ms | 1 |
| 1245892 | (invalid payload path) | n/a | 0.015 s HTTP 400 | — (0 runs, correct) | 0 |

"attempts = maxTries, delay = (maxTries−1)×2 s, last attempt always accepted" — exactly the
`checkFailure` signature, reproduced and then eliminated by removing the key alone.

## 2. The fix

Single line in the **Validate Signal Payload** Code node of workflow `EmMbN4sslwIx1ydn`
(applied via n8n REST API `PUT /api/v1/workflows/EmMbN4sslwIx1ydn`; no container restart,
no retry-config change, no other node touched):

```js
// before
const json = { valid, error: errs.join('; '), fileName, body };
// after
const json = valid ? { valid, fileName, body } : { valid, error: errs.join('; '), fileName, body };
```

- Valid path: no `error` key anywhere downstream → `checkFailure` false → no spurious retries.
- Invalid path: `error` key present exactly as before → Respond 400 body and Telegram
  Rejected text unchanged (verified live, see §3).
- `retryOnFail: true, maxTries: 3, waitBetweenTries: 2000` and
  `onError: continueErrorOutput` on the Write node are **retained**: a genuinely failing
  write throws inside `runNode`, which is handled by the `catch` path (real retry), not by
  this output-shape heuristic.

## 3. Verification (prod workflow, live)

Sweep daemon (`build.praxis.signals-sweep-daemon`) was **booted out for ~60 s** during the
prod test so the live NT8 consumer would not ingest the test signal (see §5 caution), then
bootstrapped back (state=running, pid 16305, heartbeat advancing same-second afterward).

Test: `POST http://127.0.0.1:5678/webhook/praxis-signal` with
`signal_id: SIM-QXD-TEST-0006` (NQ BUY 1 @ 20000, ts 2026-07-15T18:51:35Z).

| Check | Before (8xf / exec 1245860) | After (prod exec **1245936**) |
|---|---|---|
| HTTP status / time | 200 / 4.19–4.37 s | **200 / 0.043 s** |
| Write-node runs recorded | 1 (final only) | 1 |
| Write-node executionTime | 4022–4035 ms | **4 ms** |
| Task attempts | 3 (event log: requested at +0 s/+2 s/+4 s) | **1** |
| Outbox files for the signal | 3 physical writes | **1** file, mtime unchanged after 5 s re-check |
| Invalid-path regression | — | HTTP 400 in 0.015 s with correct joined error text (clone exec 1245892) |

Response body: `{"ok":true,"file":"/files/outbox/2026-07-15T18-51-35Z-SIM-QXD-TEST-0006.json"}`.

Knock-on wins: the TradingView-facing 200 is now ~40 ms (webhook-timeout risk gone); the
outbox/drop churn that kept the (since-replaced) launchd throttle window hot is gone; the
NT8 FileSystemWatcher sees one event per signal instead of 2–3.

## 4. Rollback

Exact pre-change state is committed at
`/Volumes/Sensidine/Praxis.build/workflows/EmMbN4sslwIx1ydn.before-qxd.json`
(post-change: `…after-qxd.json`; API-level diff = the one `jsCode` line in
"Validate Signal Payload" only, `active: true` both sides). To roll back:

```bash
# key: N8N_API_KEY in "…/war-room/Automations Personal /.env" (same key n8n-mcp uses)
python3 -c "import json; d=json.load(open('workflows/EmMbN4sslwIx1ydn.before-qxd.json')); \
  json.dump({k:d[k] for k in ('name','nodes','connections','settings')}, open('/tmp/rb.json','w'))"
curl -X PUT -H "X-N8N-API-KEY: $N8N_API_KEY" -H "Content-Type: application/json" \
  -d @/tmp/rb.json http://127.0.0.1:5678/api/v1/workflows/EmMbN4sslwIx1ydn
```

Takes effect immediately (no restart; webhook registration untouched — path/ID unchanged).

## 5. Cleanup / footprint attestation

- **No container restart.** n8n, traefik, gotenberg untouched; no env/compose change.
- Test workflow `O55pofWpaKU300WC` ("QXD TEST write-false-failure repro (DELETE ME)"):
  deactivated and **deleted**. Its webhook path (`praxis-qxd-test`) is gone with it.
- All `SIM-QXD-TEST-*` files removed: outbox (1, removed pre-daemon-restore),
  `praxis-signals/processed/` (4) and `processed/duplicates/` (3). Outbox empty; drop dir
  restored. Consumer journal lines (`praxis-processed-signals.log`) left in place as
  append-only audit records.
- Test executions (noted, not deletable via API without pruning): clone 1245860/65/71/91/92,
  prod 1245936.
- Telegram: prod verification fired **one** "✅ PRAXIS signal … SIM-QXD-TEST-0006"
  notification to the trader channel (success path notifies; unavoidable). Clone had no
  Telegram nodes.
- **CAUTION for trader:** the NT8 consumer on the VM was RUNNING (contrary to the dispatch
  assumption) and ACCEPTED four clone-phase test signals before the sweep-daemon pause was
  adopted: `SIM-QXD-TEST-0001/0002/0003/0004` (NQ BUY 1 @ 20000, journal 18:46:51–18:49:11Z).
  These may have placed **Sim101 bracket orders**. Please check NT8 (Sim101) and
  flatten/cancel any QXD-TEST positions/orders. The prod-phase signal (0006) was
  intercepted before the consumer saw it.

## 6. Upstream note

This looks like an n8n-core design hazard (undocumented magic `json.error` output field
turning retryOnFail into a false-failure loop) present in 2.27.4. Any future Code node used
with `retryOnFail` must not emit a `json.error` key in the first item of successful output
(`""`, `{}`, `0` all count as "error"; only `undefined`/`null`/`false` are safe). Worth an
upstream issue if it persists in newer releases; the HSAI "Write State File" node does not
set retryOnFail, so it is unaffected today.
