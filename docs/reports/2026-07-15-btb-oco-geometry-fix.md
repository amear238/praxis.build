# btb — OCO-Reuse Root Cause + Market-Relative Bracket-Geometry Gate

**Bead:** Praxis_build-btb (P2 bug) · **Date:** 2026-07-15 · **File:** `ninjascript/PraxisSignalConsumer.cs`
**Incident:** 2026-07-15 10:35:37 ET, Sim101, NQ 09-26 — schema-valid signal (payload `price` 29874, no in-file stop/target) → derived stop 29864 / target 29894, both ABOVE a long entry that filled 29826.75 → NT8 rejected the stop-market leg ("sell stop above market") → target limit leg rejected "OCO ID bb0a21acd0a4474da5595c3a56a8dfa1 cannot be reused" → strategy safety-flattened and self-terminated. Full narrative: `docs/reports/2026-07-14-b1f-t1-t3-mac-run.md` ("10:35 drop" section).

## 1. Root cause of the OCO-ID-reuse rejection — NT8 cascade artifact, NOT a code bug

Verdict: **artifact of NT8's managed-approach bracket engine; the consumer's code neither creates nor reuses any OCO id.**

Evidence from the pre-fix code (line numbers = pre-fix source, git blob at HEAD):

- The ENTIRE order surface of the strategy is `SubmitBracket` (pre-fix lines 579–618). It makes exactly three order-API calls: `SetStopLoss(entrySignal, CalculationMode.Price, sig.ResolvedStop, false)` (line 600), `SetProfitTarget(entrySignal, CalculationMode.Price, sig.ResolvedTarget)` (line 601), and `EnterLong/EnterShort(sig.Qty, entrySignal)` (lines 604/606).
- The string "OCO" (or any OCO-id construction, `SubmitOrderUnmanaged`, `ChangeOrder`, `Order` object handling) appears **nowhere** in the file — `Set*`/`Enter*` is NT8's *managed* approach, in which NT8 core itself submits the stop-loss and profit-target as an OCO pair after the entry fills. The 2026-07-15 ~12:05 ET GUI evidence for the later *successful* bracket confirms this: both legs were submitted by NT8 with OCO id `d7d5dbe…` — which is the entry **execution id**, generated inside NT8, never touched by our code.
- Mechanism of the 10:35 cascade: on entry fill, NT8 internally submitted both bracket legs tagged with one internally-generated OCO id. The sim engine rejected the stop leg (sell stop above market). An order rejection inside an OCO group causes NT8/sim to tear down (burn) that OCO group; the sibling target leg, already in flight with the same OCO string, then failed with "OCO ID … cannot be reused". Both rejects are downstream artifacts of one cause: **invalid bracket geometry relative to the live market**.
- Therefore there is nothing to "fix" in the submission path, and no cheap hardening of the "don't submit the second leg if the first errored" kind is *possible* here — leg submission happens inside NT8's managed engine after the fill, not in our code (our `Set*` calls at lines 600–601 only arm the bracket pre-entry; the try/catch at 594–617 already covers synchronous throws). The correct and only available intervention is to stop invalid-geometry signals **before** any order is submitted — implemented below.
- The safety-flatten + self-terminate that followed is NT8's default `RealtimeErrorHandling` (StopCancelClose) behavior. It worked exactly as intended and is **deliberately preserved** as the last-resort backstop (now documented in the `ValidateMarketGeometry` comment block); nothing in this change touches error handling.

## 2. Fix — pre-submit market-relative bracket-geometry gate

### Why the existing check missed it

`ValidateSignal` already enforced `stop < price < target` (BUY) / `target < price < stop` (SELL) — but only relative to **the payload's own `price` field** (pre-fix lines 547–550). The incident payload passed it perfectly (29864 < 29874 < 29894); the problem was that `price` itself sat ~47 pts above the live market. Schema-valid ≠ market-valid.

### Reference-price choice (rationale)

The entry is a **market order**, so its fill tracks the live inside market, not the payload price — the same session even showed a fill/reference delta on a *good* signal (fill 29820 vs reference 29821.25). The exact fill is unknowable pre-submit; the closest knowable proxy is the **entry-side inside quote at validation time**: `GetCurrentAsk()` for BUY (a market buy lifts the ask), `GetCurrentBid()` for SELL, with `Close[0]` as fallback if the quote is unusable (≤0/NaN/Inf), and **fail-closed rejection** if no usable reference exists at all. No slippage buffer is added (strict inequalities only, minimal change); NT8's own reject + safety-flatten remains the backstop for pathological slippage — preserved, per §1. The payload-relative check in `ValidateSignal` is kept too (belt and braces): a signal must now be sane against **both** its own price and the live market.

### What was added (current source line references)

- Header doc block: "GEOMETRY GATE" paragraph (lines ~35–40).
- `ProcessFile`: gate inserted **after** the dedup check and **before** the ACCEPTED journal write (lines ~416–428). Ordering rationale: a replayed signal_id still lands as DUPLICATE (dedup contract untouched), and a geometry-rejected signal_id is never added to `processedSignals` nor journaled ACCEPTED — so a **corrected redelivery of the same signal_id may still trade**, matching the file's existing "rejects don't burn ids" convention.
- On failure: the existing `RejectFile(...)` path (Print + Log warning with the specific geometry reason string, move to `rejected/`) — identical in shape to a parse/schema reject. **No journal line is written and no orders of any kind are submitted.**
- `ValidateMarketGeometry(ParsedSignal)` (new, Validation region, before `TryGetString`): BUY requires `ResolvedStop < ref < ResolvedTarget`; SELL requires `ResolvedTarget < ref < ResolvedStop`; strict, on the tick-rounded resolved levels.
- `LoadJournal`: unchanged from ct5 — splits each line on tab and arms dedup from the signal_id in field 0. No REJECTED lines are ever written, so no reload-time exclusion is needed. Journal-region comment simply notes that all rejects (parse/schema/geometry) are un-journaled.

### Journaling-convention note (trader DECLINED, 2026-07-15)

An earlier revision of this fix journaled geometry rejects with a `REJECTED-GEOMETRY: …` status. The trader DECLINED that convention (DECISION_LOG 2026-07-15T21:10Z): geometry rejects are now handled **uniformly**, exactly like parse/schema rejects — Print + Log warning + move to `rejected/`, with NO journal line at all. Rationale: the file at rest in `rejected/` already provides the filesystem audit trace, journaling near-order events is unwanted, and uniform reject-handling is simpler.

## 3. Unit-style case walk (through `ValidateMarketGeometry`, ref = market reference)

Assume tick-rounded resolved levels; ref = ask (BUY) / bid (SELL), say 29800.

| # | Case | Inputs | Predicate | Outcome |
|---|------|--------|-----------|---------|
| 1 | LONG, stop above market (the incident) | stop 29864, target 29894, ref 29800 | `29864 < 29800` false | REJECTED (Print+Log+move to rejected/), NO journal line, zero orders |
| 2 | LONG, target below market | stop 29700, target 29750, ref 29800 | `29800 < 29750` false | REJECTED (Print+Log+move to rejected/), NO journal line, zero orders |
| 3 | LONG, both legs below market | stop 29700, target 29760, ref 29800 | second conjunct false | REJECTED (Print+Log+move to rejected/), NO journal line, zero orders |
| 4 | LONG, stop == market | stop 29800, ref 29800 | strict `<` fails | REJECTED (Print+Log+move to rejected/), NO journal line, zero orders |
| 5 | LONG, target == market | target 29800, ref 29800 | strict `<` fails | REJECTED (Print+Log+move to rejected/), NO journal line, zero orders |
| 6 | LONG, valid | stop 29700 < ref 29800 < target 29900 | both true | pass → journal ACCEPTED → SubmitBracket |
| 7 | SHORT, stop below market | stop 29750, ref 29800 | `29800 < 29750` false | REJECTED (Print+Log+move to rejected/), NO journal line, zero orders |
| 8 | SHORT, target above market | target 29850, ref 29800 | `29850 < 29800` false | REJECTED (Print+Log+move to rejected/), NO journal line, zero orders |
| 9 | SHORT, stop == market / target == market | equality | strict `<` fails | REJECTED (Print+Log+move to rejected/), NO journal line, zero orders |
| 10 | SHORT, valid | target 29700 < ref 29800 < stop 29900 | both true | pass |
| 11 | stop == target (either side) | — | cannot satisfy `ValidateSignal`'s own `stop < price < target` (still runs first) | rejected earlier, un-journaled schema reject |
| 12 | No usable reference (ask/bid ≤0 or NaN, `CurrentBar < 0` so no `Close[0]`) | — | fail-closed branch | REJECTED (Print+Log+move to rejected/) "bracket geometry unverifiable", NO journal line, zero orders |

Dedup interplay: duplicate id → DUPLICATE (gate never reached). A bad-geometry id is never journaled, so it is never burned — a corrected redelivery of the SAME id trades normally: first drop is rejected (moved to `rejected/`, no journal line, id not in `processedSignals`), second drop trades.

## 4. Test payload + attended sim-test instructions (trader / Win11 VM — cannot be run from the Mac orchestrator)

**Fixture:** `tests/fixtures/btb-bad-geometry-long.json` — field names verified against the consumer's actual parser/`ValidateSignal` (NOT the stale `signal-template.json`, bead 6h7):

```
{"symbol":"NQ","side":"BUY","qty":1,"price":99874.00,"stop":99864.00,"target":99894.00,"signal_id":"SIM-BTB-GEOMBAD-20260715-T1","ts":"2026-07-15T00:00:00.000Z"}
```

Design: passes every `ValidateSignal` check including the payload-relative bracket check (99864 < 99874 < 99894) — so it specifically exercises the NEW market gate — while both legs sit impossibly far above any plausible NQ market (incident shape, exaggerated). Zero order risk even on regression: if the gate somehow passed it, NT8 would reject the same way as the incident and safety-flatten with no position (sim-only, qty 1).

**Procedure (after the updated .cs is deployed and F5-compiled in NT8 on the VM, consumer enabled on NQ / Sim101, market open, outside the 17:00–18:00 ET halt per runbook §6):**

1. Copy the fixture, set a FRESH `signal_id` (e.g. `SIM-BTB-GEOMBAD-<yyyymmdd-hhmmss>`) and a current `ts`; write to `~/praxis-signals/` (Mac) via atomic `.tmp` → `mv`, filename per convention e.g. `2026-07-15T18-00-00.000Z-SIM-BTB-GEOMBAD-<id>.json`.
2. Expect within ~1 s (≤15 s rescan worst case): file → `rejected/`; a Log Warning entry `PRAXIS-B1f rejected signal_id=… : BUY bracket geometry invalid vs live market: need stop < market < target (stop=99864 market=<live> target=99894)`; and **NO new journal line** (the `rejected/` file is the only at-rest trace — uniform with parse/schema rejects).
3. NT8 GUI (trader-touch): Control Center → Log shows the `PRAXIS-B1f signal_id=… REJECTED … — NO order.` line and the Warning log entry; Orders tab shows **zero** new orders; strategy stays enabled (no disable, no flatten).
4. Regression pair: drop a fresh VALID signal (explicit stop ~80 pts below / target ~80 pts above live NQ, per the 11:12:45 ET corrected-T1 shape) → ACCEPTED journal line + exactly one bracket, proving the gate does not block good geometry.
5. Restart probe (journal semantics): restart NT8, re-enable; startup line's "N journaled signal_ids loaded" is unchanged by the geometry reject (no journal line was ever written for it); optionally redrop the bad id with corrected geometry/live-market prices → it must trade (id not burned).

## 5. Compilation sanity (this file compiles only inside NT8 — cannot build here)

Final diff re-read line-by-line; checked: balanced braces/regions; C# 5-compatible syntax only (no string interpolation, no `?.` added); `GetCurrentAsk()`/`GetCurrentBid()`/`Close[0]`/`CurrentBar` are standard NinjaScript `StrategyBase`/`NinjaScriptBase` members available in this class scope; `Close[0]` guarded by `CurrentBar >= 0` (avoids the out-of-range throw before the first bar); `string.Split('\t')` char overload valid; `StartsWith(string, StringComparison)` overload valid on .NET 4.8; new method is non-static (needs instance market accessors) matching `ValidateSignal`'s placement in the Validation region; string concatenation of doubles matches the file's existing style (pre-fix lines 548–550); no new usings needed. Cannot execute — attended VM compile (F5) is step 0 of §4.

## 6. Files changed

| File | Change |
|---|---|
| `ninjascript/PraxisSignalConsumer.cs` | v4: geometry gate (header block, ProcessFile gate, ValidateMarketGeometry); geometry rejects handled uniformly like parse/schema rejects — Print+Log+move to rejected/, NO journal line (trader DECLINED REJECTED-GEOMETRY journaling, 2026-07-15); LoadJournal unchanged from ct5 |
| `tests/fixtures/btb-bad-geometry-long.json` | NEW — bad-geometry attended-sim-test payload |
| `docs/reports/2026-07-15-btb-oco-geometry-fix.md` | NEW — this report |
| `MANIFEST.md` | rows appended for the three files above |
