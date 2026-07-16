# PRAXIS Signal Payload Schema

Canonical drop-file schema consumed by `ninjascript/PraxisSignalConsumer.cs`
(`ValidateSignal` / `ParsedSignal`). Authoritative contract is B1-d resolved.
The parser is a strict flat-JSON reader (one flat object, no nesting, no comments).
`signal-template.json` in this directory is the version-controlled sample; the
operational copy on the build Mac lives at `~/praxis-signals/signal-template.json`
and must match this file byte-for-byte (no UTF-8 BOM).

## Required fields
| Field       | Type                | Rule |
|-------------|---------------------|------|
| `signal_id` | string (non-empty)  | Dedup key; one bracket per unique id (journal-enforced) |
| `symbol`    | string (non-empty)  | Must match the strategy's chart instrument (e.g. `NQ`) |
| `side`      | string              | `BUY` or `SELL` (case-insensitive, normalized upper) |
| `qty`       | number              | Positive integer, `> 0`, `<= MaxQty` sim cap |
| `price`     | number              | Finite, `> 0` — reference/entry price |
| `ts`        | string (ISO-8601)   | Must parse as a date-time (e.g. `2026-07-16T14:30:00Z`) |

## Optional fields (in-file bracket overrides)
| Field    | Type   | Rule |
|----------|--------|------|
| `stop`   | number | Finite `> 0`; absent → derived `DefaultStopTicks` off `price` |
| `target` | number | Finite `> 0`; absent → derived `DefaultTargetTicks` off `price` |

Bracket sanity is enforced: BUY needs `stop < price < target`; SELL needs
`target < price < stop`.

## Notes
- The consumer keys the processed/dedup filename on `ts` + `signal_id`.
- No other keys are read. Legacy pre-B1-b keys (`action`, `source`,
  `timestamp`, `strategy`, `test`) are NOT part of the schema and are ignored.
