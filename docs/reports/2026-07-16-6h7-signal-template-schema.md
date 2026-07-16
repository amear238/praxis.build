# 6h7 — Signal-Template Schema Refresh (P4)

**Date:** 2026-07-16
**Bead:** Praxis_build-6h7 (P4)
**Goal:** Replace the PRE-B1-b stale signal-template schema with the authoritative
B1-d contract read straight from the consumer parser, version-control it in-repo,
and regenerate the operational copy on the build Mac.

## Authoritative source
`ninjascript/PraxisSignalConsumer.cs` — `ValidateSignal` (~L503) + `ParsedSignal`
class (~L487). The parser is a strict flat-JSON reader. Fields extracted below are
exactly and only what the code reads.

## Field-by-field diff (stale template → consumer parser)

| Stale key (old template) | Consumer field | Disposition |
|--------------------------|----------------|-------------|
| `action` ("BUY")         | `side` ("BUY"\|"SELL") | RENAMED (semantics kept; must be BUY/SELL, normalized upper) |
| `qty` (1)                | `qty` (number, +int, ≤MaxQty) | KEPT (tightened: positive integer, ≤ sim MaxQty) |
| `symbol` ("NQ")          | `symbol` (must match chart instrument) | KEPT |
| `timestamp` (ISO)        | `ts` (ISO-8601) | RENAMED |
| `source` ("TradingView") | —              | REMOVED (not read) |
| `strategy` ("PRAXIS-NQ-test") | —         | REMOVED (not read) |
| `test` (true)            | —              | REMOVED (no `test` flag exists in parser) |
| — (absent)               | `signal_id` (non-empty string) | ADDED (required; dedup key) |
| — (absent)               | `price` (finite >0) | ADDED (required; reference/entry price) |
| — (absent)               | `stop` (number >0) | ADDED (optional override; else DefaultStopTicks) |
| — (absent)               | `target` (number >0) | ADDED (optional override; else DefaultTargetTicks) |

**Final required set:** `signal_id`, `symbol`, `side`, `qty`, `price`, `ts`.
**Optional:** `stop`, `target`. Bracket sanity enforced (BUY: stop<price<target;
SELL: target<price<stop). Processed/dedup filename keyed on `ts` + `signal_id`.

## Consumer vs. brief summary
No disagreements. The brief's field set matched the code exactly. Confirmed there
is NO `test` flag in the parser (the stale template's `test:true` was never read).

## Paths written
- **In-repo (staged, not committed):**
  - `/Volumes/Sensidine/Praxis.build/signals/signal-template.json` (canonical)
  - `/Volumes/Sensidine/Praxis.build/signals/signal-template.README.md` (semantics)
  - `.gitignore` — added `!signals/signal-template.json` negation
  - `MANIFEST.md` — 2 new entries
- **Operational (out-of-repo, internal disk):**
  - `~/praxis-signals/signal-template.json` — regenerated from canonical

## Verification
- `diff signals/signal-template.json ~/praxis-signals/signal-template.json` → identical.
- First 3 bytes of operational copy = `7b 0a 20` (`{`) → no UTF-8 BOM.
- Stale keys `action`/`source`/`timestamp`/`strategy`/`test` GONE from both copies.
