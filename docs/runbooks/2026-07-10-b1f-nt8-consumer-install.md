# B1-f — NT8 PraxisSignalConsumer install + sim test plan (bead Praxis_build-ct5)

**Date:** 2026-07-10
**Applies to:** NinjaTrader 8 (8.1.7.2) inside the Parallels Win11-ARM VM (D-2026-07-09-B)
**Source file:** `ninjascript/PraxisSignalConsumer.cs` (this repo — SOURCE ONLY; runtime copy lives inside the VM)
**Scope:** SIM ONLY. The strategy hard-refuses any account whose name does not start with `Sim`.
Every GUI step below is **TRADER-TOUCH** — the build agent cannot reach into the VM.

---

## 1. Prerequisites (verify before install)

1. **TRADER-TOUCH** — VM running, NT8 launched, connected (Simulated Data Feed or Kinetick login is fine; orders will go to the internal Sim account).
2. **TRADER-TOUCH** — Signals share visible in Windows. Two possible states:
   - **Scoped share applied** (B1-c trader TODO done): `\\Mac\praxis-signals` shows the drop dir.
   - **Whole-home B1-0 share still active**: use `Z:\praxis-signals` (or `\\Mac\Home\praxis-signals`).
   Open File Explorer and confirm the chosen path lists the drop dir (you should see `signal-template.json` and any leftover `*.json`). Note the exact path — it is the strategy's `Signals directory` parameter.
3. **TRADER-TOUCH** — The account you will attach must be the internal simulator, e.g. **Sim101** (Control Center → Accounts). The NT demo login account `DEMO1628771` will be **refused** by the guard (name does not start with `Sim`) — this is intentional.

## 2. Install the strategy

1. **TRADER-TOUCH** — In the VM, copy `PraxisSignalConsumer.cs` into:
   `Documents\NinjaTrader 8\bin\Custom\Strategies\PraxisSignalConsumer.cs`
   (Get the file into the VM via the shared folder, e.g. temporarily copy it into the drop dir from the Mac — it is a `.cs`, the consumer ignores non-`.json` files — then move it out of the drop dir once copied.)
2. **TRADER-TOUCH** — NT8 Control Center → **New → NinjaScript Editor**. Press **F5** (or the compile button). Expect: `Compile successful`. If errors appear, capture the exact error text back to the repo (do not hand-edit beyond obvious path typos).
3. **TRADER-TOUCH** — Open a chart: **New → Chart → NQ** (front month, e.g. NQ SEP26), any timeframe (1-min is fine).
4. **TRADER-TOUCH** — Right-click chart → **Strategies…** → add **PraxisSignalConsumer**. Configure:
   - **Signals directory (in-VM share path):** the path confirmed in §1.2 (default `\\Mac\praxis-signals`).
   - **Rescan interval:** 15 s (default).
   - **Default stop/target distance:** 40 / 80 ticks (defaults; only used when a drop file has no `stop`/`target` fields — the current n8n schema has none).
   - **Max qty per signal:** 5 (default).
   - **Account:** **Sim101** (Strategy parameters → General → Account).
   - Set **Enabled** = true. OK.
5. **TRADER-TOUCH** — Confirm startup line in **New → NinjaScript Output** window:
   `PRAXIS-B1f STARTED on account 'Sim101', dir '...', N journaled signal_ids loaded, rescan every 15s.`

## 3. Where things appear

| What | Where |
|---|---|
| Accept/duplicate/reject lines (every line carries `signal_id=`) | Control Center → **New → NinjaScript Output** |
| Errors / non-sim refusal / order-submit failures | Control Center → **Log** tab |
| Orders / positions | Control Center → **Orders** / **Positions** (account Sim101); chart markers |
| Consumed files | `<signals dir>\processed\` (duplicates in `processed\duplicates\`) |
| Rejected files | `<signals dir>\rejected\` |
| Dedup journal (append-only; one line per actioned signal_id) | `<signals dir>\praxis-processed-signals.log` |

Journal retention: permanent within the file (the idempotency window never expires). Sim volume keeps it tiny; archive manually if it ever matters. It is visible from the Mac at `/Users/admin/praxis-signals/praxis-processed-signals.log`.

## 4. Sim test plan (T1–T4)

Create test files **from the Mac** by writing into `/Users/admin/praxis-signals/` directly (fastest), or fire the real webhook (`POST https://n8n.myzerker626.win/webhook/praxis-signal`) and let the sweep deliver. Direct-write must be atomic-ish: write to a `.tmp` name then `mv` to the final `.json` name.

**IMPORTANT:** replace `"price"` in each payload with a value near the CURRENT NQ price (entry is a market order; the bracket is priced off the payload — a far-off price makes the stop/target land illogically against the fill).

### T1 — valid drop → exactly ONE bracket order
Mac:
```bash
cd /Users/admin/praxis-signals
cat > .t1.tmp <<'EOF'
{"symbol":"NQ","side":"BUY","qty":1,"price":29874.00,"signal_id":"B1F-T1-0001","ts":"2026-07-10T21:00:00.000Z"}
EOF
mv .t1.tmp 2026-07-10T21-00-00.000Z-B1F-T1-0001.json
```
**TRADER-TOUCH — expect:** within ~1 s (FSW) or ≤15 s (rescan): Output shows `signal_id=B1F-T1-0001 ACCEPTED`; Orders tab shows ONE market entry `PRX-B1F-T1-0001` filling on Sim101 plus an OCO'd stop-loss and profit-target; file lands in `processed\`; journal gains one `B1F-T1-0001 ... ACCEPTED` line. Flatten the position afterward if desired (Positions → right-click → Close).

### T2 — same signal_id, NEW ts/filename → NO second order (the 9tl contract)
```bash
cd /Users/admin/praxis-signals
cat > .t2.tmp <<'EOF'
{"symbol":"NQ","side":"BUY","qty":1,"price":29874.00,"signal_id":"B1F-T1-0001","ts":"2026-07-10T21:05:00.000Z"}
EOF
mv .t2.tmp 2026-07-10T21-05-00.000Z-B1F-T1-0001.json
```
**TRADER-TOUCH — expect:** Output shows `signal_id=B1F-T1-0001 DUPLICATE ... no order placed`; **no** new order in Orders tab; file lands in `processed\duplicates\`; journal gains a `DUPLICATE` line. This is the B1-d Finding-F2 case: new filename (new ts), same in-file signal_id.

### T3 — malformed JSON → rejected, NO order
```bash
cd /Users/admin/praxis-signals
printf '{"symbol":"NQ","side":"BUY","qty":' > .t3.tmp
mv .t3.tmp 2026-07-10T21-10-00.000Z-B1F-T3-BROKEN.json
```
Also test a missing-field variant:
```bash
cat > .t3b.tmp <<'EOF'
{"symbol":"NQ","side":"HOLD","qty":1,"price":29874.00,"signal_id":"B1F-T3-0002","ts":"2026-07-10T21:11:00.000Z"}
EOF
mv .t3b.tmp 2026-07-10T21-11-00.000Z-B1F-T3-0002.json
```
**TRADER-TOUCH — expect:** Output shows `REJECTED ... malformed JSON` / `invalid 'side'`; both files land in `rejected\`; NO orders; journal unchanged (rejects are not journaled, so a corrected redelivery may still trade).

### T4 — NT8 restart → NO replay of journaled signals
1. **TRADER-TOUCH** — Disable the strategy, close NT8 entirely, relaunch, re-enable the strategy on the same chart/Sim101.
2. **TRADER-TOUCH — expect:** startup line reports `N journaled signal_ids loaded` (N ≥ 1 from T1/T2); NO new orders fire (T1/T2 files are already in `processed\`, and even if a stale copy of a T1-id file were re-dropped, the journal-loaded HashSet dedupes it).
3. Optional stronger probe: re-drop the T2 file content under a THIRD ts/filename after the restart — expect `DUPLICATE`, no order.

### Cleanup
**TRADER-TOUCH** — Flatten Sim101, disable strategy if not continuing, optionally clear `processed\`/`rejected\` test files. Leave the journal in place (it IS the dedup memory) unless intentionally resetting the idempotency window — in that case archive/delete `praxis-processed-signals.log` while the strategy is disabled.

## 5. Known behaviors / cautions

- **Non-sim account:** guard fires at DataLoaded — Log-tab error `REFUSED: account '...' is not a Sim account`, watcher never starts, zero signals processed. There is no parameter to bypass this.
- **Symbol mismatch:** a drop whose `symbol` ≠ the chart's instrument (`NQ`) is rejected — run the strategy on an NQ chart.
- **Share unreachable at enable-time:** strategy logs a start failure to the Log tab; fix the path parameter and re-enable.
- **Entry is a market order** priced off live sim data; the payload `price` only anchors the derived stop/target when no explicit `stop`/`target` fields exist. See implementer report for rationale.
- **Order-submit failure after journaling:** by design NOT auto-retried (at-most-once bias); Log-tab error names the signal_id, file goes to `rejected\`.

## 6. Session-hours guard (bead Praxis_build-di9; added 2026-07-15)

**Rule: NO order-generating test drops (T1, T2, T4's optional probe — anything that could submit an order) during the CME equity-index futures daily maintenance halt, 17:00–18:00 ET (Mon–Thu).** Also observe the weekly close: market closes **Friday 17:00 ET** and does not reopen until **Sunday 18:00 ET** — no order-generating drops in that window either.

Why: on 2026-07-14 the T1 order was submitted at 17:05 ET, inside the halt. The prime suspect (per `docs/reports/2026-07-14-b1f-t1-t3-mac-run.md`, "Rerun after NQ remount") is that the sim engine rejected the order asynchronously and NT8's default realtime-error handling **auto-disabled the strategy ~17 s after the signal was ACCEPTED**, killing the consumer mid-suite (see §6.1).

**Exempt:** malformed/reject-path tests (T3-style probes) produce no order and may run any time.

**Operator pre-drop check (run on the Mac before any order-generating drop):**

```bash
TZ=America/New_York date '+%a %H:%M ET'
```

Do NOT drop if the output shows **17:00–17:59** on any day, or anywhere between **Fri 17:00** and **Sun 18:00**.

### 6.1 NT8 auto-disable on order rejection

- **Symptom (Mac side):** the consumer goes silent — FSW stops picking up new files, the 15 s rescan stops, the journal stops growing, files sit untouched in the drop-dir root. This is **indistinguishable from idle** on the Mac; the only positive signal is a fresh drop that never gets processed (07-14: T2 untouched >3.5 min, malformed T3 probe untouched >80 s).
- **Diagnosis (TRADER-TOUCH):** Control Center → **Log** tab — look for the strategy disable entry (order-rejection error naming the strategy, followed by the strategy being disabled). NinjaScript Output may also show the last lines before termination.
- **Recovery (TRADER-TOUCH):** re-enable PraxisSignalConsumer on the correct chart (NQ front month) and account (Sim101), **outside the halt window**. The consumer's startup catch-up scan then processes files that arrived while it was down — no manual re-drop needed. Evidence from 07-14: T1's ACCEPTED journal line survived the death, so restart will NOT replay T1; the leftover T2/T3 files in the root are expected to be consumed on re-enable (T2 → DUPLICATE, no order; T3 probe → `rejected\`).

### 6.2 Operator note — OnTermination journaling: recommendation DECLINE (pending ratification)

**Recommendation (recorded here per bead Praxis_build-di9; NOT yet ratified — decision belongs to the orchestrator/trader):** DECLINE adding a terminal/DISABLED journal line in `OnTermination` for now. Rationale: it means a code change to `PraxisSignalConsumer.cs` plus a retest of the whole consumer (T1–T4) during Block-1 close-out — disproportionate to the benefit. The existing detection layer is the Mac-side `.heartbeat` / stale-alert daemon (`scripts/praxis-signals-sweep-daemon.sh` + `scripts/praxis-signals-stale-check.sh` → Telegram); consumer-death detection beyond that (e.g. a journal-growth watchdog) can be revisited post-Block-1 if silent deaths recur. If ratified, log the decision in DECISIONS.md through the normal channel; this note is not that log entry.
