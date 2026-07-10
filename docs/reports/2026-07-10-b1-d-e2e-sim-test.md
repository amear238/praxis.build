# B1-d — End-to-End Sim Latency + Idempotency Test

**Bead:** Praxis_build-4wk (B1-d)
**Date:** 2026-07-10
**Type:** Report (test evidence)
**Signal path under test:** `curl webhook → n8n validate+atomic-write → outbox → launchd WatchPaths sweep → drop dir /Users/admin/praxis-signals/*.json`

---

## 1. Resolved webhook + payload contract

Read from workflow `EmMbN4sslwIx1ydn` ("PRAXIS — Signal Webhook (Block 0)") via n8n `get_workflow_details`.

- **Production webhook (confirmed):** `POST https://n8n.myzerker626.win/webhook/praxis-signal`
  (Response Mode: Respond-to-Webhook node; no auth. Bead's guess `/webhook/praxis-signal` was correct.)
- **Validation node ("Validate Signal Payload") required fields:** `symbol, side, qty, price, signal_id, ts`
  - `side` ∈ {BUY, SELL} (case-insensitive)
  - `qty` finite number > 0
  - `price` finite number
  - `ts` parseable ISO timestamp
- **Signal id field:** `signal_id` (in payload body; echoed into drop-file JSON content).
- **Drop filename is DETERMINISTIC:** validate node builds
  `fileName = <ts with ':'→'-'>-<signal_id sanitized [^A-Za-z0-9_.-]→_>.json`
  → i.e. the filename is keyed on **`ts` + `signal_id` together**, not on `signal_id` alone, and not on a uuid/random.
- The sweep (`praxis-signals-sweep.sh`) **preserves the outbox basename** end-to-end (`rsync … → incoming/ → mv -f → drop/`), and promotes with `mv -f` (overwrite).

Valid sim payload used:
```json
{"symbol":"NQ","side":"BUY","qty":1,"price":20000.25,"signal_id":"<id>","ts":"<iso>"}
```

---

## 2. LATENCY — webhook → file-in-drop-dir (accept < 5s)

Method: capture `date +%s.%N` immediately before `curl`; the workflow writes the file to the outbox *before* returning HTTP 200; poll the drop dir (20–50 ms granularity) for the deterministic filename; record arrival `date +%s.%N`; delta = arrival − pre-curl.

**Isolated single-signal runs (spaced > 12s apart — the realistic per-signal scenario):**

| Run | signal_id | curl resp | t0 (pre-curl) | t1 (file in drop) | delta (s) |
|-----|-----------|-----------|---------------|-------------------|-----------|
| 1 | B1D-ISO-1-1783692634 | `{"ok":true,...}` HTTP 200 | 1783692634.553386 | 1783692638.830098 | **4.277** |
| 2 | B1D-ISO-2-1783692652 | `{"ok":true,...}` HTTP 200 | 1783692652.877578 | 1783692657.177382 | **4.300** |
| 3 | B1D-ISO-3-1783692671 | `{"ok":true,...}` HTTP 200 | 1783692671.221464 | 1783692675.530046 | **4.309** |

(Warm-up run, discarded: 4.221s.)

**MAX measured latency = 4.309s < 5s → PASS.** All three runs passed. Every file landed with the exact deterministic name (e.g. `2026-07-10T14-01-00.000Z-B1D-ISO-1-1783692634.json`), confirming full-path delivery.

### FINDING F1 — thin margin + burst throttle (non-blocking, flagged)
- The steady per-signal latency is a **consistent ~4.3s**, leaving only ~0.7s of headroom under the 5s bound. The bulk of it is not the sweep relay itself (B1-b-fu measured the outbox→drop mv at 0.25s) but WatchPaths event dispatch + n8n round-trip under this host's VM load.
- **Back-to-back bursts fail 5s.** An initial burst of 3 signals fired ~2s apart measured **5.70s / 8.58s / 8.35s** (escalating) — launchd enforces a ~10s minimum respawn interval for a WatchPaths job, so rapid successive triggers coalesce and each later file waits for the next spawn (worst case the 60s StartInterval backstop). TradingView NQ signals are not expected at multi-per-10s cadence, so the isolated case is the representative acceptance measurement — but if signal cadence ever tightens, latency will exceed 5s. Recommend either a resident fswatch/kqueue daemon (no respawn throttle) or a shorter StartInterval if sub-5s under burst is later required.

---

## 3. IDEMPOTENCY (watcher-contract level)

The live NinjaScript watcher is not the object under test — this validates the **drop-layer behavior** and states the dedup contract the watcher must honor.

### Test A — identical redelivery (same `signal_id` AND same `ts`)
Delivered the byte-identical payload twice (signal_id `B1D-IDEM-1783692700`, ts `2026-07-10T15:00:00.000Z`), 6s apart. Both returned HTTP 200 with the same `"file"` path.

**Result: exactly ONE file in the drop dir (`count=1`).** The second delivery produced the same deterministic filename and `mv -f` overwrote it. No residue left in outbox or incoming.
→ **File-level idempotent** for exact redelivery.

### Test B — same `signal_id`, DIFFERENT `ts` (retry that regenerates its timestamp)
Delivered the same signal_id `B1D-SAMEID-1783692736` twice with `ts=15:10` then `ts=15:11`. Both HTTP 200.

**Result: TWO distinct files in the drop dir (`count=2`):**
```
2026-07-10T15-10-00.000Z-B1D-SAMEID-1783692736.json
2026-07-10T15-11-00.000Z-B1D-SAMEID-1783692736.json
```
→ Because the filename embeds `ts`, a same-id redelivery with a changed timestamp is **NOT** deduplicated at the file layer — it lands as a second, distinct drop file.

### FINDING F2 — filename idempotency is keyed on (ts + signal_id), not signal_id (BLOCKING for watcher design)
File-level idempotency only holds when the retry is byte-identical (same ts). A duplicate that regenerates `ts` (a live TradingView "resend" is not guaranteed to preserve the original alert timestamp) yields two drop files for one logical signal. **The filename cannot be the dedup key.**

### Stated dedup CONTRACT the downstream watcher MUST honor
> The NinjaScript FileSystemWatcher (or the order-placement stage) MUST dedupe on the **in-file `signal_id` field**, not on the filename. It maintains a set of already-actioned `signal_id`s over a dedup window W (W ≥ the max signal-retry span; a per-session persisted set is sufficient for sim). On a new drop file it parses `signal_id`; if that id is already in the set → **no-op** (log + delete/ignore the file, place no order). Otherwise it records the id and places exactly one bracket order.

**Is the contract satisfiable with the current payload/naming?** **YES.** The payload carries a stable, required `signal_id` and it is written verbatim into every drop file's JSON content, so the watcher has a reliable key. The current *naming* alone does NOT provide id-level idempotency (Finding F2), but the *contract* keyed on the in-file field is fully implementable. No blocker to B1-d — but F2 must be carried into the watcher-build bead as an explicit acceptance criterion ("dedup on in-file signal_id, not filename").

---

## 4. Cleanup / monitoring health
- All B1D-* test files removed from drop dir, outbox, and incoming. Drop dir restored to prior state (only pre-existing `2026-07-09T20-24-00Z-SIM-B1B-0001.json` + `signal-template.json` remain — not created by this test).
- Outbox and incoming empty. Heartbeat fresh (11s old at end). Both launchd jobs (`build.praxis.signals-sweep`, `build.praxis.signals-stale-check`) loaded. Monitoring healthy.

## 5. Verdict
- **LATENCY: PASS** — max 4.309s < 5s (isolated per-signal). Margin thin; burst caveat = Finding F1.
- **IDEMPOTENCY: PASS at contract level** — exact redelivery is file-idempotent; contract keyed on in-file `signal_id` is coherent and satisfiable. Finding F2 (filename keyed on ts+id) must be honored by the watcher build.
