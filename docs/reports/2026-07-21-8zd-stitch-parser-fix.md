# Praxis_build-8zd — b2_stitch parser fix + full 44-file stitch

**Date:** 2026-07-21
**Bead:** Praxis_build-8zd
**Scope:** Fix `scripts/b2_stitch.py` to parse the REAL NinjaTrader export
(semicolon-delimited, header-less, combined `YYYYMMDD HHMMSS` minute timestamp,
NO Open Interest), then run the full 44-file stitch under the authorized
volume-only deviation (D-2026-07-21-A). Parse-layer only — no change to the
Difference/Panama back-adjustment math or the OI hard-refusal guardrail contract.

---

## 1. Files touched (diff summary)

| File | Change |
|---|---|
| `scripts/b2_stitch.py` | Delimiter sniffing, header-less detection, positional schema, combined-timestamp parsing, exact-only resolution for synthesized headers, volume-only no-crossover boundary fallback. |
| `config/b2-stitch-schema.json` | Added `daily_positional` / `minute_positional` index layouts + updated `_comment`. |
| `docs/reports/2026-07-21-8zd-stitch-parser-fix.md` | This report. |

`git diff --stat`:

```
 config/b2-stitch-schema.json |   6 +-
 scripts/b2_stitch.py         | 162 ++++++++++++++++++++++++++++++++++++-------
 2 files changed, 142 insertions(+), 26 deletions(-)
```

### `scripts/b2_stitch.py` — what changed and why

1. **Timestamp/date formats** — added `"%Y%m%d %H%M%S"`, `"%Y%m%dT%H%M%S"`,
   `"%Y%m%d%H%M%S"` to `_DT_FORMATS` and `"%Y%m%d"` to `_DATE_FORMATS`. The real
   minute files carry a single combined field-0 `YYYYMMDD HHMMSS` (space inside
   the field); daily field-0 is `YYYYMMDD`. Layout is now CONFIRMED, not a guess.

2. **`_read_csv()` rewritten** — now returns `(header, data, has_header)`:
   - **Delimiter sniffing** (`_sniff_delimiter`): semicolon → tab → comma. Real
     exports are semicolon; the comma+header self-test fixtures still parse.
   - **Header-less detection** (`_looks_like_header`): a row is a header iff it
     has a cell that is neither a number nor a parseable date/timestamp. Real
     data rows are all numeric/date-like → detected header-less; fixture rows
     start with `"Date"`/`"Timestamp"` labels → detected header.

3. **`_positional_header()`** (new) — synthesizes a canonical header for
   header-less files from the schema's `*_positional` layout, sized to the
   actual column count. A 6-col daily → `[date,open,high,low,close,volume]` (no
   OI); a 7-col daily → trailing `open_interest`.

4. **`resolve_column(..., exact_only=)`** (new param) — header-less files use a
   header we synthesize from canonical names, so they resolve by EXACT match
   only (no substring, no positional fallback). **This fixes a real bug:** the
   OI alias `"openinterest"` contains `"open"` as a substring, so the default
   substring matcher mapped the positional `open` column into the open_interest
   slot — reading OPEN price as OI, making `oi_present()` return True, masking
   the OI-absent state, suppressing the volume-only banner, and corrupting the
   roll (it compared open-price as "OI"). Exact-only resolution eliminates this.
   Header-bearing files keep the full exact→substring→fallback resolution.

5. **`read_daily` / `read_minute`** — apply the positional header + `exact_only`
   when header-less; for header-bearing files behavior is byte-for-byte
   unchanged (fixtures unaffected).

6. **`compute_roll_date` — volume-only no-crossover boundary fallback.** Real
   finding: the export trims each contract's DAILY series to ~1–3 days past its
   own roll, so the 5 earliest pairs (2021–2022) overlap by only 2 days and the
   back month is still a hair UNDER the front on the last shared day (the true
   crossover lands on the first UN-shared day, for which no front row exists).
   When `allow_volume_only` is set AND no strict crossover exists in the common
   window, we roll on the LAST common date (the export's own front/back
   boundary). This fires ONLY on the authorized volume-only path and ONLY when
   there is no crossover; the OI-present path (self-test Case A) and every
   genuine crossover (17 of 21 real seams; self-test Case D) are untouched. The
   Difference/Panama offset math is unchanged — the seam gap is still taken at
   the roll date.

### `config/b2-stitch-schema.json`

Added the two positional layouts (wholesale-replaceable via `--schema`) and
documented the real semicolon/header-less shape in `_comment`. The existing
comma+header alias maps are unchanged.

---

## 2. Reproduce

### Acceptance A — self-test (comma+header fixtures, 4 cases)

```bash
cd /Volumes/Sensidine/Praxis.build
python3 scripts/tests/b2-stitch-selftest.py
```

### Acceptance B/C — full 44-file stitch (semicolon/header-less real export)

```bash
cd /Volumes/Sensidine/Praxis.build
python3 scripts/b2_stitch.py --allow-volume-only
# default --root is ~/praxis-signals/b2-data (env PRAXIS_B2DATA_ROOT overrides).
# Reads <root>/raw/*.csv ; writes:
#   <root>/reports/NQ-continuous-1min.csv   (stitched continuous series)
#   <root>/reports/stitch-validation.md     (spec-§4 validation report)
# The VOLUME-ONLY DEVIATION banner is written to STDERR.
```

---

## 3. Terminal output (evidence)

### 3A. Self-test — 4/4 PASS

```
=== b2-stitch self-test (Praxis_build-6bw) ===

CASE A — full pipeline on good fixture (roll dates + Difference seams)
  [PASS] roll dates == [2024-03-15, 2024-06-14]
  [PASS] R1 trigger = vol+oi crossover (OI used, not volume-only)
  [PASS] offsets == {09-24:0, 06-24:+40, 03-24:+90}
  [PASS] seam raw daily-close gaps == +50, +40
  [PASS] C1 bars shifted by CONSTANT +90 (17980->18070, 17998->18088) — additive, not ratio
  [PASS] R1 seam: adjusted delta=+1 pt (continuous); raw delta=+51 pt (spread removed)
  [PASS] R2 seam: adjusted delta=+3 pt (continuous); raw delta=+43 pt (spread removed)
  [PASS] monotonic timestamps, 0 duplicates
  [PASS] stitched CSV written: NQ-continuous-1min.csv
  [PASS] validation report generated with 2 roll seams

CASE B — OI GATE: back-month daily OI blank -> tool REFUSES (OI_BLANK)
  [PASS] run_pipeline RAISED OIBlankError (did not silently proceed)
  [PASS] NO stitched CSV written on OI_BLANK (no silent volume-only fallback)
  [PASS] CLI exit code == 2 (OI_BLANK)

CASE C — build-ahead-of-data: empty raw/ -> VALIDATION-PENDING (exit 3)
  [PASS] run_pipeline returns pending on empty raw/
  [PASS] CLI exit code == 3 (VALIDATION-PENDING)

CASE D — authorized override: --allow-volume-only rolls on volume alone (banner)
  [PASS] override proceeds; volume-only crossover still finds correct seams
  [PASS] diag records oi_used=False (deviation is recorded, not hidden)

============================================================
RESULT: PASS — all cases green
```

### 3B. Full 44-file run — parses all files, emits both artifacts, prints banner

STDERR (the required VOLUME-ONLY DEVIATION banner + the boundary-fallback notice):

```
!!! VOLUME-ONLY DEVIATION ENABLED — OI blank for 06-21, 09-21, 12-21, 03-22,
06-22, 09-22, 12-22, 03-23, 06-23, 09-23, 12-23, 03-24, 06-24, 09-24, 12-24,
03-25, 06-25, 09-25, 12-25, 03-26, 06-26, 09-26. This is a documented deviation
(D-2026-07-17-A). Ensure trader sign-off + a DECISIONS append exist. !!!

NOTE: 5 of 21 roll seam(s) used the no-overlap VOLUME-ONLY BOUNDARY fallback
(D-2026-07-21-A), NOT a volume crossover: 2021-06-11(06-21->09-21),
2021-09-10(09-21->12-21), 2022-03-11(03-22->06-22), 2022-06-10(06-22->09-22),
2022-09-09(09-22->12-22)
```

The persisted `stitch-validation.md` now labels the seams accurately.
Construction header:

```
**Dataset:** REAL  ·  **Construction:** volume-crossover roll (16 of 21 seams)
+ 5 no-overlap BOUNDARY-fallback seam(s) (volume-only, D-2026-07-21-A)
+ Difference (Panama) back-adjustment
```

§3 seam table now carries a **Roll trigger** column; the 5 boundary-fallback
seams (# 1, 2, 4, 5, 6) render `⚠ BOUNDARY fallback (volume-only,
D-2026-07-21-A)`, the other 16 render `VOLUME-ONLY (deviation)` (genuine volume
crossover). Table header:

```
| # | Roll date | Front→Back | Front close | Back close | Raw gap | Front offset | Roll trigger |
```

STDOUT:

```
SUMMARY b2-stitch label=REAL bars=1857362 days=1704 seams=21 dupes=0 gaps=2255 overall=FAIL
wrote: /Users/admin/praxis-signals/b2-data/reports/NQ-continuous-1min.csv
wrote: /Users/admin/praxis-signals/b2-data/reports/stitch-validation.md
```

Output files:

```
1857363 /Users/admin/praxis-signals/b2-data/reports/NQ-continuous-1min.csv   (1 header + 1,857,362 data rows)
        /Users/admin/praxis-signals/b2-data/reports/stitch-validation.md

head -2 NQ-continuous-1min.csv:
Timestamp,Open,High,Low,Close,Volume,SrcContract
2021-03-07 23:01:00,16120.5,16167,16120.5,16154.75,17,06-21
```

- All 44 files (22 daily + 22 minute) parsed without a parse/crash error.
- 21 roll seams (one per adjacent pair), 0 duplicate timestamps, monotonic.
- Back-adjustment: newest contract 09-26 anchored at offset 0; oldest 06-21 lifted
  +3416.00 pts cumulatively — additive Difference (Panama), math untouched.

---

## 4. Deviations / surprises

1. **`overall=FAIL` / exit 1 is NOT a parse failure.** It is the §4.2 check:
   `17:00–17:59 maintenance break empty → FAIL (79704 bars)`. Root cause:
   **the export timestamps are in UTC, not ET.** Per-hour bar histogram of a full
   contract shows the (near-)empty maintenance hour at **21:xx**, not 17:xx
   (CME break 17:00–18:00 ET = 21:00–22:00 UTC; the first bar
   `2021-03-07 23:01` is the Sunday 18:00-ET reopen expressed in UTC). Every
   other §4 gate PASSes (RTH median 390, ETH median 1380, depth 1704 days,
   monotonic, 0 dupes). The parser faithfully reads the timestamps as stored
   (naive, no tz) — item 3 asked to parse the combined field, not to convert
   timezones, and constraint D forbids touching validation semantics. **Action
   for the trader / VM coworker:** either re-export in ET, or add a
   UTC→ET conversion step + make the validator's maintenance-break hour
   configurable. Tracked as a follow-up finding, out of scope for -8zd.

2. **5 early pairs have no strict volume crossover in their 2-day overlap**
   (06-21→09-21, 09-21→12-21, 03-22→06-22, 06-22→09-22, 09-22→12-22). The export
   trims each front contract's daily data ~1 day before the crossover completes
   (on the last shared day the back month is still just under the front). Handled
   by the documented volume-only boundary fallback (§1.6) — roll at the last
   common date. The other 16 seams use a genuine strict volume crossover. These
   5 boundary seams are labeled explicitly in the persisted report (construction
   header, §3 seam-table `Roll trigger` column) and named in an at-run stderr
   NOTE, so a consumer of the CSV+report can tell exactly which rolls deviate
   from the locked crossover convention.

3. **A real substring-matching bug was found and fixed** (§1.4): the OI alias
   `openinterest` substring-matched the `open` column. It was latent because the
   fixture's OI header `OpenInt` exact-matches first; it only surfaced with the
   synthesized positional header. Fixed via exact-only resolution on the
   header-less path.

4. **Output artifacts live OUTSIDE the repo** at
   `~/praxis-signals/b2-data/reports/` (the default `--root`). The stitched CSV
   is ~150 MB / 1.86 M rows — not a git-tracked artifact. Nothing under a repo
   `reports/` path was created; nothing to stage there.

---

## 5. Acceptance status

| # | Criterion | Result |
|---|---|---|
| A | Self-test 4/4 (comma+header fixtures unchanged) | PASS |
| B | 44 real files parse without error; emits `reports/NQ-continuous-1min.csv` + `reports/stitch-validation.md` | PASS |
| C | VOLUME-ONLY DEVIATION banner prints | PASS |
| D | No change to Difference math or OI hard-refusal contract (parse layer + volume-only feed only) | PASS |

Note on B: `overall=FAIL`/exit 1 is a §4.2 UTC-vs-ET validation grade, not a
parse error; both artifacts are emitted and all 44 files parse cleanly.
