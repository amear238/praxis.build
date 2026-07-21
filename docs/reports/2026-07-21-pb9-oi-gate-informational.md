# Praxis_build-pb9 — OI gate: HARD STOP → INFORMATIONAL

**Date:** 2026-07-21
**Bead:** Praxis_build-pb9
**Authority:** D-2026-07-21-A (volume-only crossover roll AUTHORIZED; resolves the
former D-2026-07-17-A OPEN RISK). OI is structurally absent from every NT8 daily
export — a HARD platform limitation, not a config miss.

## Problem

The b2data-watch raw-landing validation treated absent Open Interest as a HARD
STOP. A COMPLETE, usable 44/44 dataset read as failed:

```
SUMMARY present=44/44 oi=BLANK ready=NO stop=OI_BLANK
```

Per-file it also logged `OI BLANK — STOP … needs sign-off (D-2026-07-17-A)`.
That risk was resolved by D-2026-07-21-A, so this is stale noise.

## Change summary (diff)

| File | Change |
|---|---|
| `scripts/b2data_raw_validate.py` | `ready` no longer requires `oi_verdict == "PRESENT"` — now `ready = (present == EXPECTED) and (not hard_failures)`. Summary drops the `stop=OI_BLANK` suffix. `OI_BLANK` removed from the human blocker list. Report VERDICT reads "volume-only per D-2026-07-21-A" when OI absent; the former `> **STOP — OI_BLANK.**` block replaced with `> **OI absent — volume-only per D-2026-07-21-A (informational).**`. |
| `scripts/praxis-b2data-watch.sh` | Per-daily `OI_BLANK*` notification changed from `b2data-oi-stop "OI BLANK — STOP … (D-2026-07-17-A OPEN RISK)"` to `b2data-oi-absent "OI absent — volume-only per D-2026-07-21-A (informational) … does NOT block"`. |
| `scripts/tests/b2data-watch-selftest.sh` | Scenario B updated to the new semantics: blank-OI first daily now expects `ready=YES`, asserts the summary does **NOT** carry `stop=OI_BLANK`, asserts the report carries **no** STOP notice and **does** carry the informational OI-absent line. Header comment updated. Scenarios A/C/D/E (the real gates) unchanged. |

**Gates NOT weakened:** file-completeness (44/44), per-file sanity (zero-byte /
truncated → `hard_failures`), column-count and coverage warnings all still set
`ready=NO` for real problems. Only the OI-absent condition moved from blocking to
informational.

## Reproduce commands

```bash
# A — real 44 files
python3 scripts/b2data_raw_validate.py --root "$HOME/praxis-signals/b2-data"

# B — daemon self-test
bash scripts/tests/b2data-watch-selftest.sh

# C — real failure still trips ready=NO (scratch copy; real raw/ untouched)
SCR=/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/1581da32-3d52-435e-92cf-f6c148c159d2/scratchpad
rm -rf "$SCR/badroot" && mkdir -p "$SCR/badroot/raw"
cp "$HOME"/praxis-signals/b2-data/raw/*.csv "$SCR/badroot/raw/"
rm "$SCR/badroot/raw/NQ-12-23_1min.csv"          # missing file -> 43/44
: > "$SCR/badroot/raw/NQ-06-24_daily.csv"         # zero-byte    -> hard sanity fail
python3 scripts/b2data_raw_validate.py --root "$SCR/badroot"
```

## Evidence

### A — real 44 files: `present=44/44 ready=YES`, informational OI line

```
SUMMARY present=44/44 oi=BLANK ready=YES
--- report ---
**VERDICT: READY TO STITCH** — complete set, volume-only per D-2026-07-21-A, no sanity failures.
> **OI absent — volume-only per D-2026-07-21-A (informational).** One or more daily files carry
  blank/zero Open Interest; OI is structurally absent from NT8 daily exports. The volume-only
  crossover roll trigger is trader-authorized (D-2026-07-21-A resolves the former D-2026-07-17-A
  OPEN RISK), so this does NOT block stitching.
```

No `OI BLANK — STOP` and no `stop=OI_BLANK`.

### B — daemon self-test: ALL SCENARIOS PASS

```
[A good ]  SUMMARY present=44/44 oi=PRESENT ready=YES
PASS: A: present=44/44 / oi=PRESENT / ready=YES
[B blank]  SUMMARY present=44/44 oi=BLANK ready=YES
PASS: B: oi=BLANK
PASS: B: ready=YES (OI-absent is informational)
PASS: B: summary drops stop=OI_BLANK
PASS: B: report carries no OI STOP notice
PASS: B: report carries the informational OI-absent line
[C miss ]  SUMMARY present=40/44 oi=PRESENT ready=NO
PASS: C: present=40/44 / ready=NO
PASS: D: settle-guard + idempotency (sweep1=0, sweep2=44, sweep3=44, seen=44)
PASS: D: completion battery wrote ready=YES report
PASS: E: sweep exits 0 despite failing notifier (rc1/rc2) + log written + status relayed

RESULT: ALL SCENARIOS PASS
```

### C — real failure still trips ready=NO (OI-absent alone does not)

```
SUMMARY present=43/44 oi=BLANK ready=NO
**VERDICT: NOT READY** (blockers: incomplete 43/44, 1 file-sanity failure(s))
--- confirm real raw/ untouched: 44 files ---
```

Even with OI blank, a missing file and a zero-byte daily both drive `ready=NO`
via the completeness and hard-failure gates — proving OI-absent no longer masks,
nor causes, a real failure.
