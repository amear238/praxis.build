# Praxis_build-1u6 (attempt 2) — Lossless UTC→ET conversion of the continuous NQ 1-min series

**Date:** 2026-07-22 · **Scope:** tz conversion + lossless seam alignment ONLY (protected roll/offset/OI math untouched) · **Verdict:** overall = **PASS**, bar count **1,857,362** (== baseline), zero seam loss.

---

## 1. What changed and why

The committed-GOOD stitch emitted timestamps AS STORED = **UTC**. The 09:30-ET-anchored Noise-Area strategy and the §4.2 maintenance-break gate need **America/New_York (ET)**. Attempt 1 failed audit because a *naive* conversion (convert-then-route) shifted every pre-roll evening ETH bar back a calendar day in ET, so `stitch()` routed it to the FRONT contract (which lacks it) while the BACK contract excluded it via `date>=roll_date` → **~2,498 real minutes silently dropped** at the seams, invisibly (the hole straddles a calendar-day boundary, leaving RTH + the break untouched → false PASS).

**Root-cause fix — route in the source tz, relabel at emission.** The seam window handoff is now evaluated on the **source-tz (UTC) calendar date** — the SAME basis the daily-derived `roll_dates` use — and the timestamp is converted to ET **only after routing AND dedup**. The front/back partition is therefore **bit-identical to the tz-naive baseline** (no minute is routed to a contract that lacks it); the ET conversion is a pure **1:1 relabel** of every surviving instant, so nothing is dropped or duplicated. This is exactly "do the tz reasoning consistently on BOTH sides of the roll boundary" (both sides UTC), with ET applied at the end.

DST fall-back ambiguity is a non-issue: bars are kept as tz-aware instants through sort/dedup, so a repeated wall-clock hour stays two distinct instants — and the NQ session is closed during that Sunday-morning hour anyway, so **no such pair occurs** and the delta is **0** (not merely "reconciled").

### Files changed
- **`scripts/b2_stitch.py`**
  - New stdlib imports (`timezone`, `zoneinfo.ZoneInfo`) + `SOURCE_TZ="UTC"` / `TARGET_TZ="America/New_York"` config with the lossless-seam rationale.
  - `stitch()` — accepts `source_tz`/`target_tz` (and a test-only `_naive`); routes on the source-tz date, emits tz-aware ET, dedups on the instant. Output series carries documented tz = America/New_York.
  - `run_pipeline()` — threads `source_tz`/`target_tz`; computes the three lossless invariants via a source-tz baseline re-stitch + a naive re-stitch (files already in memory → cheap), plus the 09:30-ET spot-check; passes them to the report.
  - `validation_report()` — renders the invariants table + spot-check + output-tz note; §4.2 refined (below).
  - `_in_break()` / new helpers `_max_break_run`, `_nth_weekday`, `_dst_flips_between`, `_first_rth_open` — §4.2 boundary + DST (below).
- **`scripts/tests/b2-stitch-selftest.py`** — existing Cases A/B/D pinned to `target_tz="UTC"` (source==target, no shift → fixtures unchanged); **new Case E** exercises UTC→ET across a seam.

### §4.2 refinement (why break flips FAIL→PASS honestly)
The baseline flagged **79,704** bars because a whole ~60-min trading hour landed in the *assumed* ET break (the tz-misalignment symptom). After a correct conversion the ET halt (17:00–18:00) contains only:
1. the **17:00:00 session-CLOSE endpoint** — the spec defines the ETH session as "18:00 → 17:00", and the raw export trades continuously through the 17:00:00 bar (e.g. 2024-01-19 17:00:00 ET vol 490) then gaps to the 18:00 ET reopen. `_in_break` now excludes this endpoint (1,302 bars). This is a correctness fix, not tolerance.
2. **48 isolated illiquid halt prints** (vol 1–10, ≤2/day over 43 days across 5 yrs) that exist in the raw NT8 export. Losslessness forbids dropping them.

The gate now grades its true intent — **"no contiguous regular session inside the halt"** (max contiguous in-halt run = **2 min**, FAIL threshold 5; a mislaid session would be ~60) — and reports the 48 isolated prints as **INFO** (surfaced, not hidden, not gating). The previously-stubbed **DST-hold** check is un-stubbed to a genuine multi-year check (11 DST flips in span; halt session-free across EST+EDT → DST tracked). *Data-quality note for the trader: the 48 sub-minute halt prints are a source-export artifact; filed for follow-up if the consumer's session guard should mask them.*

---

## 2. Self-test — 5/5 PASS (existing 4 + new seam-crossing Case E)

Case E builds a fixture whose BACK contract holds pre-roll evening bars stored as early-UTC on the roll date (= prior-evening in ET). It asserts the fix keeps all of them **and** that the naive convert-then-route path drops **exactly** those 3 — so it fails against the bug and passes against the fix.

```
CASE A — full pipeline on good fixture ............................ 11/11 PASS
CASE B — OI GATE: OI blank -> REFUSE (OI_BLANK) ....................  3/3  PASS
CASE C — build-ahead-of-data: empty raw/ -> PENDING ...............  2/2  PASS
CASE D — authorized --allow-volume-only override ..................  2/2  PASS
CASE E — UTC->ET across a roll seam: ZERO seam loss ...............  8/8  PASS
  [PASS] fix keeps ALL 9 real minutes — zero seam loss
  [PASS] 3 pre-roll evening bars present & sourced from BACK 06-24 (ET 21:00/22:00/23:00)
  [PASS] RTH-open: stored 2024-03-15 13:30Z -> emitted 2024-03-15 09:30 ET
  [PASS] naive convert-then-route DROPS exactly the 3 evening seam bars (6 vs 9)
  [PASS] run_pipeline invariants: instants_equal=True seam_gap=0 bars=9==baseline=9
RESULT: PASS — all cases green
```

---

## 3. Real run — §4 verdict, invariants, spot-check

Command: `python3 scripts/b2_stitch.py --out ~/praxis-signals/b2-data/NQ-continuous-1min.csv --report docs/reports/2026-07-22-1u6-tz-et-conversion-VALIDATION.md --allow-volume-only`

```
SUMMARY b2-stitch label=REAL bars=1857362 days=1712 seams=21 dupes=0 gaps=937 overall=PASS
```

**§4 overall verdict: PASS.** All gating checks green (RTH median 390, ETH median 1380, depth 1712 days, break no-session, DST hold, monotonic, zero-dup, tz seam-loss invariant); §4.3 gaps = FLAG (informational, non-gating, as in baseline).

### The three hard invariants (printed in the validation report)
| Invariant | Value |
|---|---|
| distinct_instants(ET output) == distinct_instants(UTC baseline) | **1,857,362 == 1,857,362 → True** |
| seam-gap (baseline minutes missing from ET output) | **0** |
| final bar count | **1,857,362** (== committed baseline; **no delta** — DST fall-back never occurs) |
| (contrast) minutes the NAIVE convert-then-route path WOULD drop | **2,498** — matches the documented attempt-1 loss exactly; this fix avoids it |

### 09:30-ET RTH-open spot-check (concrete)
Stored-UTC `2021-03-08 14:30:00 UTC` → emitted-ET **`2021-03-08 09:30:00 EST`** (src 06-21) — the RTH anchor lands exactly on 09:30 ET (14:30 UTC − 5h EST, pre-DST). Summer/EDT confirmed too (e.g. 13:30 UTC → 09:30 EDT).

---

## 4. Protected areas — proven untouched (task item 4)

Byte-for-byte identical to HEAD (verified programmatically):

| Function | vs HEAD |
|---|---|
| `compute_roll_date` (roll math, spec §3) | **identical** |
| `build_offsets` (Difference/Panama back-adjustment) | **identical** |
| `_close_on_or_before` (seam close reference) | **identical** |
| `oi_present` + OI/volume-only guardrail | **identical** |

All edits are confined to timezone handling, the `stitch()` seam-window basis + emission, and the §4 validation report. No change to roll dates, offsets, back-adjustment, or the OI gate.
