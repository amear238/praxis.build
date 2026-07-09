# B1-b — n8n LOCAL file-write node (bead Praxis_build-p7s)

**Date:** 2026-07-09
**Workflow:** `EmMbN4sslwIx1ydn` — "PRAXIS — Signal Webhook (Block 0)"
**n8n:** local Docker on this Mac (D-2026-07-09-D). Base URL `https://n8n.myzerker626.win/`.
**Status:** DONE — happy path and error path both live-verified.

---

## 1. In-container outbox path

Host outbox: `/Users/admin/n8n-compose/local-files/outbox`

Derived from the docker compose file `/Users/admin/n8n-compose/docker-compose.yml`, the `n8n` service:

```yaml
    environment:
      - N8N_RESTRICT_FILE_ACCESS_TO=/files;/home/node/.n8n-files
      - NODE_FUNCTION_ALLOW_BUILTIN=fs
    volumes:
      - n8n_data:/home/node/.n8n
      - ./local-files:/files
```

- The bind mount `./local-files:/files` maps host `.../local-files` → container `/files`.
  Therefore host `.../local-files/outbox` → **in-container `/files/outbox`** (the path used in the node).
- `N8N_RESTRICT_FILE_ACCESS_TO=/files;...` — `/files` is whitelisted, so the write is permitted.
- `NODE_FUNCTION_ALLOW_BUILTIN=fs` — the Code node may `require('fs')` (only `fs`; **not** `path`, so the code
  derives the directory via string ops, not `require('path')`). This env was added originally for the hsai-state
  atomic write, and the same tmp+rename technique is reused here.

## 2. What changed

The workflow already contained the scaffold from Block 0 (a `Write Signal File` Code node with `onError:
continueErrorOutput`, wired to `Respond 200 OK` on success and `Respond 500 Write Error` → `Telegram Notify Write
Failed` on error). Block 0 wrote **non-atomically** to `/tmp/praxis-signals` with no retry. B1-b re-targeted it to
the outbox and made it atomic + retrying. Two nodes edited via `update_workflow` (3 operations), then published.

### 2a. `Validate Signal Payload` (Code v2, runOnceForAllItems)
Only the target directory changed: `/tmp/praxis-signals` → `/files/outbox` (both the pre-`mkdirSync` and the
`fileName` construction). Filename is deterministic and unique per signal:
`/files/outbox/<ts-with-colons-as-dashes>-<sanitized signal_id>.json`
(e.g. `2026-07-09T20-24-00Z-SIM-B1B-0001.json`). Deterministic on purpose — a retried identical signal overwrites
its own file rather than creating duplicates.

### 2b. `Write Signal File` (Code v2, runOnceForAllItems) — atomic write
```javascript
const fs = require('fs');
const results = [];
for (const it of $input.all()) {
  const finalPath = it.json.fileName;                 // /files/outbox/<name>.json
  const dir = finalPath.substring(0, finalPath.lastIndexOf('/'));
  fs.mkdirSync(dir, { recursive: true });
  const tmpPath = finalPath + '.tmp';
  fs.writeFileSync(tmpPath, JSON.stringify(it.json.body, null, 2), 'utf-8');
  fs.renameSync(tmpPath, finalPath);                  // atomic same-fs rename
  results.push({ json: Object.assign({}, it.json, { written: finalPath }) });
}
return results;
```
Writes `<name>.json.tmp` then `renameSync` → `<name>.json`. Both paths are inside `/files/outbox` (same
filesystem) so the rename is atomic. The sweep globs only `outbox/*.json`, so a partially-written `.tmp` is never
picked up.

### 2c. Retry / error wiring (node settings on `Write Signal File`)
- `retryOnFail: true`, `maxTries: 3`, `waitBetweenTries: 2000` (2s) → 3 attempts, 2s backoff between them.
- `onError: continueErrorOutput` → on final failure the item is emitted on the node's **second output (index 1)**.
- Output index 1 is wired (pre-existing, preserved) to `Respond 500 Write Error` → **`Telegram Notify Write
  Failed`** (the existing Telegram error node). This is the required error routing.

Connection excerpt from `workflows/EmMbN4sslwIx1ydn.after-b1-b.json`:
```json
"Write Signal File": { "main": [
  [{ "node": "Respond 200 OK",          "type": "main", "index": 0 }],
  [{ "node": "Respond 500 Write Error", "type": "main", "index": 0 }]
]},
"Respond 500 Write Error": { "main": [[{ "node": "Telegram Notify Write Failed", "type": "main", "index": 0 }]] }
```

## 3. No separate delete step (AC #3 — confirmed)

Confirmed by reading the installed sweep script
`~/Library/Application Support/Praxis/bin/praxis-signals-sweep.sh`:
`rsync -a --remove-source-files "$OUTBOX"/*.json "$INCOMING"/` removes the outbox copy on a complete transfer, then
an atomic `mv` promotes it from `incoming/` into the drop dir `/Users/admin/praxis-signals/`. So the write node
does **not** need a delete step — the 60s sweep relays and removes the outbox copy. Verified live in §4.

---

## 4. VERIFY — real evidence

### 4a. Happy path (production execution `1068760`)
Executed via `execute_workflow` (production/webhook) with pinned sim payload
`{symbol:NQ, side:BUY, qty:1, price:20125.5, signal_id:SIM-B1B-0001, ts:2026-07-09T20:24:00Z}`.

Outbox immediately after execute:
```
$ ls -la /Users/admin/n8n-compose/local-files/outbox/
-rw-r--r--  1 admin  staff  132  Jul  9 16:23  2026-07-09T20-24-00Z-SIM-B1B-0001.json
```
(No `.tmp` file present — rename completed.)

File contents:
```
$ cat .../outbox/2026-07-09T20-24-00Z-SIM-B1B-0001.json
{
  "symbol": "NQ",
  "side": "BUY",
  "qty": 1,
  "price": 20125.5,
  "signal_id": "SIM-B1B-0001",
  "ts": "2026-07-09T20:24:00Z"
}
```

Execution node output (`Write Signal File`): `executionStatus: success`, `main[0]` item has
`"written":"/files/outbox/2026-07-09T20-24-00Z-SIM-B1B-0001.json"`, `main[1]` (error output) empty.

After the 60s sweep (waited 65s):
```
$ ls -la /Users/admin/n8n-compose/local-files/outbox/      # outbox drained
total 0
$ ls -la /Users/admin/praxis-signals/ | grep SIM-B1B       # landed in final drop dir
-rw-r--r--  1 admin  staff  132  Jul  9 16:23  2026-07-09T20-24-00Z-SIM-B1B-0001.json
```
→ sweep relayed the file to the VM-visible drop dir and removed the outbox copy. Confirms AC #3.

### 4b. Error path — LIVE-FIRED (test execution `1068786`)
Fed `Write Signal File` a non-writable path via pinned `Validate Signal Payload` output
(`fileName: /root/praxis-denied/...` — the `node` container user cannot `mkdir` under `/root`).

Node results from the execution:
- `Write Signal File`: `executionTime: 4034ms` (≈ 3 tries + 2×2s backoff — confirms the 3×/2s retry), `main[0]`
  empty, **`main[1]` (error output)** = `{"error":"EACCES: permission denied, mkdir '/root/praxis-denied'"}`.
- `Respond 500 Write Error`: executed, `source.previousNodeOutput: 1` (i.e. driven by the error output).
- `Telegram Notify Write Failed`: executed and **actually sent a real Telegram message** — response
  `{"ok":true,"result":{"message_id":27, ... "text":"❌ PRAXIS file write FAILED: file write failed"}}`.

→ The write node's error output is both wired to and live-drives the existing Telegram error node.

---

## 5. Artifacts
- `workflows/EmMbN4sslwIx1ydn.before-b1-b.json` — pre-change export (reversible).
- `workflows/EmMbN4sslwIx1ydn.after-b1-b.json` — post-change export (published active version `78e893e2`).
- Live workflow updated and **published** (active version = new code).

## 6. Notes for next session
- Change is published/active on the production webhook `/webhook/praxis-signal`.
- One real test signal (`SIM-B1B-0001`) now sits in the drop dir `/Users/admin/praxis-signals/` — a downstream
  consumer (NT8 FileSystemWatcher) or cleanup may want to clear it.
- Two real Telegram messages were sent during VERIFY: the success notify (happy path) and message_id 27 (error path).
