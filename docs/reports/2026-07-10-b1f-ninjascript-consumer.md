# B1-f — NinjaScript FileSystemWatcher consumer (bead Praxis_build-ct5)

**Date:** 2026-07-10
**Bead:** Praxis_build-ct5 (B1-f) — last Block-1 build item
**Author:** implementer subagent (repo-side; cannot compile or run NT8 — compile + enable + T1–T4 are TRADER-TOUCH per the runbook)
**Scope wall:** SIM ONLY — account-name guard is a `const` prefix check with no disabling parameter.

## What was built

- `ninjascript/PraxisSignalConsumer.cs` — NT8 Strategy (C# / .NET 4.8, `NinjaTrader.NinjaScript.Strategies`). Watches the Parallels-shared drop dir, dedupes on the in-file `signal_id`, places exactly one sim bracket per new signal, files everything into `processed/` / `processed/duplicates/` / `rejected/`.
- `docs/runbooks/2026-07-10-b1f-nt8-consumer-install.md` — install runbook + T1–T4 sim test plan with ready-to-paste drop payloads; every GUI step marked TRADER-TOUCH.
- `MANIFEST.md` — rows appended.

## Schema / path assumptions (with sources)

| Assumption | Value | Source |
|---|---|---|
| Drop-file JSON schema (flat) | `symbol, side(BUY\|SELL), qty(num>0), price(num), signal_id(string), ts(ISO)` | B1-d report §1 (validate-node contract) + B1-b report §4a verbatim file contents |
| Filename | `<ts ':'→'-'>-<sanitized signal_id>.json`, keyed on ts+signal_id | B1-d §1 — hence file-level dedup insufficient (Finding F2) |
| Mac-side drop dir | `/Users/admin/praxis-signals` | B1-c report (B1-c execution used the trader user, superseding the D-2026-07-09-C `praxispush` placeholder in practice) |
| In-VM path (parameter default) | `\\Mac\praxis-signals` | B1-c §Parallels scoping Option A names the scoped share `praxis-signals`; B1-c §A.4 cites `\\Mac\praxis-signals`. **FLAGGED:** scoping is a trader TODO that may not be applied yet; while the B1-0 whole-home share persists the working path is `Z:\praxis-signals` / `\\psf\Home\praxis-signals` (B1-0 §C4). The path is a strategy parameter, so this is a config choice at enable-time, not a code change. |
| stop/target fields | **Not in the current schema.** Consumer treats `stop`/`target` as optional in-file overrides; when absent it derives them from parameters `DefaultStopTicks`/`DefaultTargetTicks` (40/80) off the payload `price`, tick-rounded, side-sanity-checked. **FLAGGED assumption** — no report documents bracket levels; revisit when the TradingView alert payload is finalized. |
| JSON library | None assumed. B1-0/B1-d say nothing about Newtonsoft bundling in NT8 8.1.7.2, so per the bead instruction a **hand-rolled strict flat-JSON parser** is included (single object; string/number/bool/null; nested objects/arrays rejected; strict escapes; trailing-content rejected). Zero external dependencies. |

## Dedup design (the 9tl contract / B1-d F2)

- Key = in-file `signal_id`, never the filename.
- In-memory `HashSet<string>` + append-only journal `<signals dir>\praxis-processed-signals.log` (one line: `signal_id \t utc-ts \t filename \t status`), `AutoFlush` + explicit `Flush()` per line. Reloaded on startup (only field 0 is trusted), so restart does not replay — T4 covers this.
- Journal named `.log` deliberately so `*.json` FSW filter/rescans can never ingest it; it lives in the drop dir so it is Mac-visible and survives NT8 reinstalls. Retention: permanent (unbounded idempotency window); document says archive manually if ever needed.
- Ordering: journal write happens **before** order submission → **at-most-once**. A crash in the gap loses that one order but can never double-fire; for an order pipeline the double-fire is the worse failure. Submission failure after journaling is logged at Error with the signal_id and NOT auto-retried.
- Duplicates: logged with signal_id, journaled as `DUPLICATE`, file moved to `processed\duplicates\`. Rejects are NOT journaled (a corrected redelivery of a malformed signal may still trade).

## Threading approach

FSW `Created`/`Renamed` events and the rescan `System.Timers.Timer` fire on threadpool threads. Handlers only (a) enqueue the path into a lock-protected `Queue` + dedupe `HashSet`, then (b) call `TriggerCustomEvent(o => DrainQueue(), null)` — NT8's documented mechanism for synchronizing external events with the strategy thread — so all parsing, journal writes, and order methods run on the strategy thread. `OnBarUpdate` also drains as belt-and-braces. A `draining` flag prevents reentrancy; `FileSystemWatcher.Error` (buffer overflow) is logged and recovered by the periodic rescan; unreadable files are retried across rescans up to 5 attempts, then rejected.

## Missed-event insurance

Startup catch-up scan at `State.Realtime` + periodic full `*.json` rescan (default 15 s) — same philosophy as the launchd WatchPaths + StartInterval backstop (B1-b-fu). `signal-template.json` is explicitly skipped by name (it pre-exists in the drop dir and must never become an order).

## Order-pattern choice (justification)

**Managed approach**: `SetStopLoss(entrySignal, CalculationMode.Price, …)` + `SetProfitTarget(entrySignal, CalculationMode.Price, …)` before `EnterLong/EnterShort(qty, entrySignal)` (entrySignal = `PRX-<sanitized signal_id>`, ≤40 chars). NT8's managed engine submits the two exits as an OCO pair tied to the entry fill — this is the simplest fully documented bracket pattern and avoids hand-rolled unmanaged OCO/rejection/fill bookkeeping, which is where sim/live bugs breed. Entry is a **market** order: the payload `price` is the TradingView alert reference, not a guaranteed touchable limit; a resting limit that never fills would strand OCO state. `EntriesPerDirection=10` / `EntryHandling.AllEntries` so concurrent distinct signals each get their own bracket. Sim guard re-asserted inside `SubmitBracket` (defense in depth).

## Sim account guard

`const RequiredAccountPrefix = "Sim"` — checked at `State.DataLoaded` (refusal → `LogLevel.Error` + Print, watcher never starts) and again at every submission. Not exposed as a property; the only way to change it is editing source. Note: the B1-0 demo login account `DEMO1628771` is refused by design — the runbook directs the trader to attach **Sim101**.

## What remains trader-touch

1. Copy the `.cs` into the VM (`Documents\NinjaTrader 8\bin\Custom\Strategies`), F5-compile in the NinjaScript Editor, report any compile errors verbatim.
2. Confirm the actual in-VM share path (scoped `\\Mac\praxis-signals` vs legacy `Z:\praxis-signals`) and set the parameter.
3. Enable on an NQ chart against **Sim101**; run T1–T4 from the runbook; capture Output/Orders evidence for the bead's verify step.
4. (Outstanding from B1-c) apply the scoped-share change retiring the whole-home B1-0 share.

## Open items / caveats

- Compile is unverified from this side (no NT8 here) — API usage kept to conservative documented members (`OnStateChange`, `TriggerCustomEvent`, `Set*`/`Enter*`, `Instrument.MasterInstrument.{Name,TickSize,RoundToTickSize}`, `Account.Name`, `Log/Print`).
- Bracket-level derivation from tick offsets is a placeholder policy until the real TradingView alert schema lands (flagged above).
- If Parallels surfaces the Mac-side `mv` as neither Created nor Renamed for some edge case, the ≤15 s rescan still catches it (B1-d's 5 s webhook→drop budget was for the Mac-side path; in-VM pickup adds FSW ~0.2 s or worst-case one rescan period — acceptable for sim; tighten `RescanSeconds` if needed).
