# Session 53 — W1/Q1: What the ORIGINAL NT8 historical-import instructions actually specified

**Date:** 2026-08-29
**Mode:** BUILD (read-only research). No file edited, created or deleted except this report. Nothing staged.
**Criterion:** specs/SPEC_RUBRIC.md — S1 (pasted output, not description), S2 (no claim above its evidence level), S8 (no question of Amear's answered on his behalf).
**Scope:** the four files named in the brief, read from disk. Two supplementary reads (the source data file itself; one directory-scoped grep) are labelled as such.

---

## 0. PROVENANCE CHECK — are these four files independent sources?

### 0.1 Command: `ls -li`

```
$ ls -li /Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md /Users/admin/praxis-signals/b2-data/4uu-VM-brief.md /Users/admin/praxis-signals/b2-data/outbound/INSTRUCTIONS.md /Users/admin/praxis-signals/b2-data/outbound/4uu-VM-brief-v3.md
20348217 -rw-r--r--@ 2 admin  staff  16603 Aug 15 10:05 /Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md
15844527 -rw-r--r--@ 1 admin  staff   8742 Jul 24 09:54 /Users/admin/praxis-signals/b2-data/4uu-VM-brief.md
20318154 -rw-r--r--@ 1 admin  staff  16603 Aug 15 10:05 /Users/admin/praxis-signals/b2-data/outbound/4uu-VM-brief-v3.md
14928401 -rw-r--r--@ 1 admin  staff   8742 Jul 24 09:54 /Users/admin/praxis-signals/b2-data/outbound/INSTRUCTIONS.md
```

### 0.2 Command: `md5`

```
$ md5 <all four>
MD5 (/Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md) = bccfa2161fb3efbd840ba8a48dc7f49d
MD5 (/Users/admin/praxis-signals/b2-data/4uu-VM-brief.md) = 363048b0a525978c1a6b3cc6f48d1cd9
MD5 (/Users/admin/praxis-signals/b2-data/outbound/INSTRUCTIONS.md) = 363048b0a525978c1a6b3cc6f48d1cd9
MD5 (/Users/admin/praxis-signals/b2-data/outbound/4uu-VM-brief-v3.md) = bccfa2161fb3efbd840ba8a48dc7f49d
```

### 0.3 Commands: `stat` (link count), `cmp` (byte comparison)

```
$ stat -f '%i %l links  %z bytes  %N' <all four>
20348217 2 links  16603 bytes  /Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md
15844527 1 links  8742 bytes  /Users/admin/praxis-signals/b2-data/4uu-VM-brief.md
14928401 1 links  8742 bytes  /Users/admin/praxis-signals/b2-data/outbound/INSTRUCTIONS.md
20318154 1 links  16603 bytes  /Users/admin/praxis-signals/b2-data/outbound/4uu-VM-brief-v3.md

$ cmp b2-data/4uu-VM-brief.md outbound/INSTRUCTIONS.md && echo "IDENTICAL: brief.md == INSTRUCTIONS.md"
IDENTICAL: brief.md == INSTRUCTIONS.md

$ cmp b2-data/4uu-VM-brief-v3.md outbound/4uu-VM-brief-v3.md && echo "IDENTICAL: v3 == outbound/v3"
IDENTICAL: v3 == outbound/v3

$ cmp b2-data/4uu-VM-brief.md b2-data/4uu-VM-brief-v3.md || echo "(differ, as expected: v1 vs v3)"
/Users/admin/praxis-signals/b2-data/4uu-VM-brief.md /Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md differ: char 16, line 1
(differ, as expected: v1 vs v3)
```

### 0.4 Command: locate the second link to inode 20348217

```
$ find /Users/admin -inum 20348217 2>/dev/null
/Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md
/Users/admin/Library/Application Support/Claude/local-agent-mode-sessions/df2e3b79-4203-42ab-a8f4-3ac1dc7c0b33/3c56e144-bb5e-4ede-9a32-54cdb857e20d/local_1a1d9636-23f3-4224-8d23-de430eba6b5f/uploads/4uu-VM-brief-v3.md
```

### 0.5 CONCLUSION — stated explicitly

**There are TWO documents here, not four.**

- **NO PAIR AMONG THE FOUR IS A HARDLINK.** All four inodes are distinct (20348217 / 15844527 / 14928401 / 20318154). Each of the four paths is a separate copy on disk.
- `b2-data/4uu-VM-brief.md` and `outbound/INSTRUCTIONS.md` are **byte-identical copies** (same md5 `363048b0…`, same 8,742 bytes, same mtime Jul 24 09:54, `cmp` silent). **Therefore "the instructions" and "the v1 brief" are ONE document under two names. Agreement between them is NOT corroboration — it is the same text read twice.** Any future report that cites INSTRUCTIONS.md and 4uu-VM-brief.md as two agreeing sources is double-counting a single source.
- `b2-data/4uu-VM-brief-v3.md` and `outbound/4uu-VM-brief-v3.md` are likewise **byte-identical copies** (md5 `bccfa216…`, 16,603 bytes). Same conclusion: one document, two names. (Note: the v3 document itself *instructs* the reader to diff these two — v3 lines 9–11 — so this duplication is deliberate, an in-transit tamper check, not accidental aliasing.)
- The document itself corroborates the md5 result. v3 lines 8–11, verbatim:

```
**v3 supersedes v2** (`4uu-VM-brief.md` and `outbound\INSTRUCTIONS.md`, both dated 2026-07-24,
byte-identical to each other). v2 is still on the share for reference; **follow v3.** An identical
copy of this file is at `outbound\4uu-VM-brief-v3.md` — diff the two to confirm neither was
tampered with in transit, then proceed.
```

- **One genuine hardlink does exist**, but not between the four: `b2-data/4uu-VM-brief-v3.md` (nlink=2) shares inode 20348217 with an upload artifact under `~/Library/Application Support/Claude/local-agent-mode-sessions/.../uploads/4uu-VM-brief-v3.md`. Document/filesystem fact only; I make no claim about how that link came to exist.

**Naming caveat for the rest of this report.** The file called `4uu-VM-brief.md` is internally titled **v2**, not v1 — line 1: `# PRAXIS 4uu (v2) — task for the Cowork agent (NT8 VM)…`, and line 6: `**v2 supersedes the earlier brief.**` So the on-disk set is v2 and v3; the true v1 is *not* among the four files and is not on the share under these names. Below I call the 8,742-byte document **"v2/INSTRUCTIONS"** and the 16,603-byte document **"v3"**.

---

## Q1a — SOURCE FILE GRANULARITY

**Answer: 1-minute bars (OHLCV). Not tick. Not daily.** This is a document fact, corroborated by the data file on disk.

### Evidence — v2/INSTRUCTIONS

```
$ grep -n -E '1min|1-min|minute|nt8import|csv|bars|rows|yyyyMMdd' /Users/admin/praxis-signals/b2-data/4uu-VM-brief.md
19:| `NQ-continuous-1min.nt8import.txt` | the source data (NT8-native format) — you will COPY it to the correctly-named file in STEP 1 |
20:| `NQ-continuous-1min.csv` | source of record (comma+header+7th col); **do NOT feed to the importer** — it will bounce |
61:copy "C:\Mac\Home\praxis-signals\b2-data\NQ-continuous-1min.nt8import.txt" ^
73:- Leave the tick→minute/day generation checkboxes unchecked (this is already minute data).
76:The file is exactly what NT8's importer wants for 1-min data:
78:yyyyMMdd HHmmss;Open;High;Low;Close;Volume        (semicolon-delimited, no header)
81:1,857,362 bars · 2021-03-07 → 2026-07-20 · ET wall-clock · full ETH session (RTH is a
86:`%USERPROFILE%\Documents\NinjaTrader 8\db\minute\NQCONT\`. No new files there = import did
90:Our series stamps the RTH-open minute at **09:30:00**. NT8 sometimes treats a minute bar's
126:`New > Strategy Analyzer`. Add `PraxisNoiseAreaBreakout` on the imported **`NQCONT`** 1-min series.
```

The load-bearing passage, verbatim from v2/INSTRUCTIONS lines 76–82 (`sed -n '76,82p'`):

```
The file is exactly what NT8's importer wants for 1-min data:
​```
yyyyMMdd HHmmss;Open;High;Low;Close;Volume        (semicolon-delimited, no header)
20260717 093000;28608.75;28610.5;28581;28606.25;1813
​```
1,857,362 bars · 2021-03-07 → 2026-07-20 · ET wall-clock · full ETH session (RTH is a
downstream template filter, not pre-filtered).
```

### Evidence — v3

```
$ grep -n -E '1min|1-min|minute|nt8import|csv|bars|rows|yyyyMMdd' /Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md
81:- **Do NOT import `NQ-continuous-1min.csv`.** It is the source of record (comma-delimited, headered,
132:`NQ-continuous-1min.nt8import.txt`:
136:1,857,362 rows     2021-03-07 → 2026-07-20, ET wall-clock, semicolon-delimited, no header
144:copy "C:\Mac\Home\praxis-signals\b2-data\NQ-continuous-1min.nt8import.txt" ^
176:not by itself evidence. Just give Amear the three rows. **This matters because every backtest number
183:**`NQCONT` does not exist in NT8.** Confirmed 2026-07-25: `db\minute\NQCONT\` exists (created 7/24
190:Error on requesting bars series: 'Unknown instrument 'NQCONT''
230:| tick→minute/day generation | leave **unchecked** (already minute data) |
243:- **`%USERPROFILE%\Documents\NinjaTrader 8\db\minute\NQCONT\` must now be NON-EMPTY.**
251:Our series stamps the RTH-open minute at **09:30:00**. NT8 sometimes treats a minute bar's stamp as
280:`New > Strategy Analyzer` → add `PraxisNoiseAreaBreakout` on the imported **`NQCONT`** 1-min series.
320:3. STEP B1 (deleted / already gone) and B2 (three rows: size, mtime, SHA256).
321:4. Whether `NQCONT` now exists, and whether `db\minute\NQCONT\` is non-empty.
```

v3 lines 135–138, verbatim:

```
95,900,139 bytes   sha256 307c5e8af1da42b7606d666f14e4f34228feec50d19dd52d25396aae1b16e454
1,857,362 rows     2021-03-07 → 2026-07-20, ET wall-clock, semicolon-delimited, no header
first: 20210307 180100;16120.5;16167;16120.5;16154.75;17
last : 20260720 112700;29005.5;29020.75;29003.5;29016;308
```

### Supplementary — the data file itself (read-only, this session)

```
$ head -3 /Users/admin/praxis-signals/b2-data/NQ-continuous-1min.nt8import.txt
20210307 180100;16120.5;16167;16120.5;16154.75;17
20210307 180200;16164.25;16164.25;16144.75;16144.75;7
20210307 180300;16145.75;16145.75;16129.75;16134.5;5

$ head -5 /Users/admin/praxis-signals/b2-data/NQ-continuous-1min.nt8import.txt | cut -d';' -f1
20210307 180100
20210307 180200
20210307 180300
20210307 180400
20210307 180500

$ ls -l /Users/admin/praxis-signals/b2-data/
total 601920
-rw-r--r--@  1 admin  staff       7334 Jul 22 15:22 4uu-reconcile-checklist.md
-rw-r--r--@  2 admin  staff      16603 Aug 15 10:05 4uu-VM-brief-v3.md
-rw-r--r--@  1 admin  staff       8742 Jul 24 09:54 4uu-VM-brief.md
drwxr-xr-x@  6 admin  staff        192 Jul 25 10:41 inbound
drwxr-xr-x@  4 admin  staff        128 Jul 22 15:42 ninjascript
-rw-r--r--@  1 admin  staff  116331171 Jul 22 14:42 NQ-continuous-1min.csv
-rw-r--r--@  1 admin  staff   95900139 Jul 23 13:02 NQ-continuous-1min.nt8import.txt
-rw-r--r--@  1 admin  staff   95900139 Jul 23 13:02 NQCONT.Last.txt
drwxr-xr-x@  4 admin  staff        128 Aug 15 09:53 outbound
drwxr-xr-x@ 46 admin  staff       1472 Jul 21 14:04 raw
drwxr-xr-x@  7 admin  staff        224 Aug 15 10:38 reports
```

Consecutive stamps are exactly 60 seconds apart, each row carrying O/H/L/C/V. That is bar data at 1-minute granularity, not a tick stream. `NQCONT.Last.txt` exists and matches `NQ-continuous-1min.nt8import.txt` in size and mtime; **byte-identity of those two was NOT re-verified this session — UNVERIFIED.** v3 line 131 asserts it, and v3 STEP A2 asks the VM agent to recompute the sha256 rather than trust the brief.

---

## Q1b — TARGET DATA TYPE in the NT8 import dialog

**Answer: `Last`. Neither `Bid` nor `Ask` appears anywhere in any of the four files.** Document fact.

```
$ grep -n 'Last' /Users/admin/praxis-signals/b2-data/4uu-VM-brief.md /Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md
/Users/admin/praxis-signals/b2-data/4uu-VM-brief.md:62:     "C:\Mac\Home\praxis-signals\b2-data\NQCONT.Last.txt"
/Users/admin/praxis-signals/b2-data/4uu-VM-brief.md:65:`.Last` data-type token. `NQCONT.Last.txt` is the correct form.)
/Users/admin/praxis-signals/b2-data/4uu-VM-brief.md:68:`C:\Mac\Home\praxis-signals\b2-data\NQCONT.Last.txt`, with:
/Users/admin/praxis-signals/b2-data/4uu-VM-brief.md:70:- **Data Type:** `Last`  (must match the `.Last` in the filename)
/Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md:131:**A2 — Data staging.** `NQCONT.Last.txt` should already exist on the share, byte-identical to
/Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md:145:     "C:\Mac\Home\praxis-signals\b2-data\NQCONT.Last.txt"
/Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md:150:the copy was named `NQ 12-25.txt`, missing the `.Last` data-type token.
/Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md:164:continuous prices — **hard to notice, hard to undo.** It is fully superseded by `NQCONT.Last.txt`.
/Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md:223:`C:\Mac\Home\praxis-signals\b2-data\NQCONT.Last.txt`
/Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md:228:| Data Type | `Last` — must match the `.Last` in the filename |

$ grep -nw 'Bid' <all four>
grep exit=1 (1 = no match)

$ grep -nw 'Ask' <all four>
grep exit=1 (1 = no match)

$ grep -n 'Data Type' <v2> <v3>
/Users/admin/praxis-signals/b2-data/4uu-VM-brief.md:70:- **Data Type:** `Last`  (must match the `.Last` in the filename)
/Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md:228:| Data Type | `Last` — must match the `.Last` in the filename |

$ grep -n 'DataType' <v2> <v3>
/Users/admin/praxis-signals/b2-data/4uu-VM-brief.md:59:field. The name must be `<instrument>.<DataType>.txt`. So first make a correctly-named copy:
/Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md:149:instrument field. The form is `<instrument>.<DataType>.txt`. The 7/23–7/24 run failed partly because
```

**ZERO MATCHES for `Bid`. ZERO MATCHES for `Ask`.** The only data type ever named in this corpus is `Last`.

Both documents fix the **Format** and **Time Zone** fields alongside Data Type.

v2/INSTRUCTIONS lines 67–74, verbatim (`sed -n '67,74p'`):

```
Then: Control Center → **Tools → Historical Data → Import** section → select
`C:\Mac\Home\praxis-signals\b2-data\NQCONT.Last.txt`, with:
- **Format:** `NinjaTrader (end of bar timestamps)`
- **Data Type:** `Last`  (must match the `.Last` in the filename)
- **Time Zone of Imported Data:** **US Eastern (ET)** — the file's timestamps are ET
  wall-clock. ⚠️ Do **not** leave this on UTC; that would shift every bar 4–5 hours.
- Leave the tick→minute/day generation checkboxes unchecked (this is already minute data).
- Press **Import**.
```

v3 lines 225–230, verbatim (`sed -n '225,230p'`):

```
| Setting | Value |
|---|---|
| Format | `NinjaTrader (end of bar timestamps)` |
| Data Type | `Last` — must match the `.Last` in the filename |
| **Time Zone of Imported Data** | **US Eastern (ET)** |
| tick→minute/day generation | leave **unchecked** (already minute data) |
```

The four-setting import contract is **identical in v2 and v3** (Format / Data Type / Time Zone / generation-unchecked). v3 changed the emphasis — it promotes the time zone to the headline defect (v3 l.232: *"The time zone is the defect that killed the 7/24 run — it was left on UTC"*) — but changed none of the four values.

---

## Q1c — FILENAME CONVENTION

**Answer: `<instrument>.<DataType>.txt`, instantiated as `NQCONT.Last.txt`.** Document fact.

```
$ grep -n -E 'filename|file name|NQCONT\.Last\.txt|<instrument>|NQ 12-25\.txt|derives' <v2> <v3>
/Users/admin/praxis-signals/b2-data/4uu-VM-brief.md:7:the import filename was missing the data-type token, and a render fault was active.
/Users/admin/praxis-signals/b2-data/4uu-VM-brief.md:58:NT8 derives the target instrument **from the filename** — the Import panel has no instrument
/Users/admin/praxis-signals/b2-data/4uu-VM-brief.md:59:field. The name must be `<instrument>.<DataType>.txt`. So first make a correctly-named copy:
/Users/admin/praxis-signals/b2-data/4uu-VM-brief.md:62:     "C:\Mac\Home\praxis-signals\b2-data\NQCONT.Last.txt"
/Users/admin/praxis-signals/b2-data/4uu-VM-brief.md:64:(The earlier run failed partly because the copy was named `NQ 12-25.txt` — missing the
/Users/admin/praxis-signals/b2-data/4uu-VM-brief.md:65:`.Last` data-type token. `NQCONT.Last.txt` is the correct form.)
/Users/admin/praxis-signals/b2-data/4uu-VM-brief.md:68:`C:\Mac\Home\praxis-signals\b2-data\NQCONT.Last.txt`, with:
/Users/admin/praxis-signals/b2-data/4uu-VM-brief.md:70:- **Data Type:** `Last`  (must match the `.Last` in the filename)
/Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md:16:two defects that killed the 7/24 attempt (wrong import filename, wrong import time zone).
/Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md:50:| `copy <src> <dst>` | duplicates the data file under a corrected filename | STEP A2 (skip if the file already exists) |
/Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md:131:**A2 — Data staging.** `NQCONT.Last.txt` should already exist on the share, byte-identical to
/Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md:145:     "C:\Mac\Home\praxis-signals\b2-data\NQCONT.Last.txt"
/Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md:148:The name matters: NT8 derives the target instrument **from the filename** — the Import panel has no
/Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md:149:instrument field. The form is `<instrument>.<DataType>.txt`. The 7/23–7/24 run failed partly because
/Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md:150:the copy was named `NQ 12-25.txt`, missing the `.Last` data-type token.
/Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md:161:`C:\Users\amearbani-ahmad\Documents\NinjaTrader 8\NQ 12-25.txt` (95,900,139 bytes, from the 7/23–7/24
/Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md:162:run) is the *stitched continuous series* carrying the filename of the *real December-2025 contract*.
/Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md:164:continuous prices — **hard to notice, hard to undo.** It is fully superseded by `NQCONT.Last.txt`.
/Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md:193:**The empty folder is a decoy, not partial progress.** NT8 creates it from the import filename, then
/Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md:223:`C:\Mac\Home\praxis-signals\b2-data\NQCONT.Last.txt`
/Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md:228:| Data Type | `Last` — must match the `.Last` in the filename |
```

**Exact filename strings specified in the documents:**

| String | Role per the documents |
|---|---|
| `NQ-continuous-1min.csv` | source of record; **must NOT be fed to the importer** (v2 l.20; v3 l.81 — comma-delimited, headered, 7 columns) |
| `NQ-continuous-1min.nt8import.txt` | the NT8-native source data (v2 l.19; v3 l.132) |
| **`NQCONT.Last.txt`** | **the file actually selected in the Import panel** (v2 l.68; v3 l.223) |
| `NQ 12-25.txt` | the historic WRONG name that broke the 7/23–7/24 run (v2 l.64; v3 l.150, l.161) |

**Statements about how NT8 parses the filename — these are MECHANISM claims, graded in the Grading section.**

v2/INSTRUCTIONS lines 57–65, verbatim (`sed -n '57,65p'`):

```
## STEP 1 — Name the file correctly, then import
NT8 derives the target instrument **from the filename** — the Import panel has no instrument
field. The name must be `<instrument>.<DataType>.txt`. So first make a correctly-named copy:
​```
copy "C:\Mac\Home\praxis-signals\b2-data\NQ-continuous-1min.nt8import.txt" ^
     "C:\Mac\Home\praxis-signals\b2-data\NQCONT.Last.txt"
​```
(The earlier run failed partly because the copy was named `NQ 12-25.txt` — missing the
`.Last` data-type token. `NQCONT.Last.txt` is the correct form.)
```

v3 lines 148–150, verbatim:

```
The name matters: NT8 derives the target instrument **from the filename** — the Import panel has no
instrument field. The form is `<instrument>.<DataType>.txt`. The 7/23–7/24 run failed partly because
the copy was named `NQ 12-25.txt`, missing the `.Last` data-type token.
```

v3 line 193, verbatim:

```
**The empty folder is a decoy, not partial progress.** NT8 creates it from the import filename, then
```

Both documents therefore make the same two-part parsing claim: (a) the instrument name comes from the filename stem, and (b) the `.Last` token is the data-type field, which must agree with the Data Type dropdown.

---

## Q1d — EVERY mention of `Tick to Minute` / `Tick Replay` / `Tick-to-Minute` / bar generation / `Generate`

All greps run case-insensitively (`grep -in`) across **all four** files. Zero-match results are pasted as required.

```
GREP -in "Tick to Minute"
(no output) -- ZERO MATCHES across all four files

GREP -in "Tick Replay"
(no output) -- ZERO MATCHES across all four files

GREP -in "Tick-to-Minute"
(no output) -- ZERO MATCHES across all four files

GREP -in "bar generation"
(no output) -- ZERO MATCHES across all four files

GREP -in "Generate"
(no output) -- ZERO MATCHES across all four files
```

**Plainly stated: the exact phrases "Tick to Minute", "Tick Replay", "Tick-to-Minute", "bar generation", and the word "Generate" each return ZERO MATCHES in all four files.** These are required results, not failures.

The only near-miss — the complete match set for the substring `generation`:

```
$ grep -in "generation" <all four>
/Users/admin/praxis-signals/b2-data/4uu-VM-brief.md:73:- Leave the tick→minute/day generation checkboxes unchecked (this is already minute data).
/Users/admin/praxis-signals/b2-data/outbound/INSTRUCTIONS.md:73:- Leave the tick→minute/day generation checkboxes unchecked (this is already minute data).
/Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md:230:| tick→minute/day generation | leave **unchecked** (already minute data) |
/Users/admin/praxis-signals/b2-data/outbound/4uu-VM-brief-v3.md:230:| tick→minute/day generation | leave **unchecked** (already minute data) |
```

That is **four path-hits but only TWO distinct sentences**, because of the aliasing established in §0.5. The complete inventory of sentences in this corpus touching tick→minute generation is exactly:

1. **v2/INSTRUCTIONS line 73** — `- Leave the tick→minute/day generation checkboxes unchecked (this is already minute data).`
2. **v3 line 230** — `| tick→minute/day generation | leave **unchecked** (already minute data) |`

Both say the same thing: **leave it OFF.** Neither document ever asks for it to be enabled.

The `unchecked` and `minute data` greps return the same two distinct sentences and nothing further:

```
$ grep -in "unchecked" <all four>
/Users/admin/praxis-signals/b2-data/outbound/INSTRUCTIONS.md:73:- Leave the tick→minute/day generation checkboxes unchecked (this is already minute data).
/Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md:230:| tick→minute/day generation | leave **unchecked** (already minute data) |
/Users/admin/praxis-signals/b2-data/4uu-VM-brief.md:73:- Leave the tick→minute/day generation checkboxes unchecked (this is already minute data).
/Users/admin/praxis-signals/b2-data/outbound/4uu-VM-brief-v3.md:230:| tick→minute/day generation | leave **unchecked** (already minute data) |

$ grep -in "minute data" <all four>
/Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md:230:| tick→minute/day generation | leave **unchecked** (already minute data) |
/Users/admin/praxis-signals/b2-data/outbound/INSTRUCTIONS.md:73:- Leave the tick→minute/day generation checkboxes unchecked (this is already minute data).
/Users/admin/praxis-signals/b2-data/4uu-VM-brief.md:73:- Leave the tick→minute/day generation checkboxes unchecked (this is already minute data).
/Users/admin/praxis-signals/b2-data/outbound/4uu-VM-brief-v3.md:230:| tick→minute/day generation | leave **unchecked** (already minute data) |
```

Full case-insensitive `tick` match set, for completeness. Every remaining hit is "Tick size" / "tick value" (instrument spec) or "Kinetick" (the data vendor) — none is bar generation:

```
$ grep -in "tick" <all four>
/Users/admin/praxis-signals/b2-data/4uu-VM-brief.md:41:- **Tick size:** `0.25`
/Users/admin/praxis-signals/b2-data/4uu-VM-brief.md:42:- **Point value:** `$20`  (tick value = $5)
/Users/admin/praxis-signals/b2-data/4uu-VM-brief.md:73:- Leave the tick→minute/day generation checkboxes unchecked (this is already minute data).
/Users/admin/praxis-signals/b2-data/4uu-VM-brief.md:94:**Definitive check** — open two charts for **2026-07-17**: native `NQ 12-25` (has Kinetick
/Users/admin/praxis-signals/b2-data/outbound/INSTRUCTIONS.md:41:- **Tick size:** `0.25`
/Users/admin/praxis-signals/b2-data/outbound/INSTRUCTIONS.md:42:- **Point value:** `$20`  (tick value = $5)
/Users/admin/praxis-signals/b2-data/outbound/INSTRUCTIONS.md:73:- Leave the tick→minute/day generation checkboxes unchecked (this is already minute data).
/Users/admin/praxis-signals/b2-data/outbound/INSTRUCTIONS.md:94:**Definitive check** — open two charts for **2026-07-17**: native `NQ 12-25` (has Kinetick
/Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md:77:  through the Instruments GUI. A hand-written row with a wrong tick size or point value corrupts
/Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md:163:If anyone ever imports it, it contaminates genuine Kinetick `NQ 12-25` contract data with stitched
/Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md:204:| Tick size | `0.25` |
/Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md:205:| Point value | `$20` (tick value $5) |
/Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md:230:| tick→minute/day generation | leave **unchecked** (already minute data) |
/Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md:255:**Definitive check.** Open two charts for **2026-07-17**: native `NQ 12-25` (has Kinetick data) and
/Users/admin/praxis-signals/b2-data/outbound/4uu-VM-brief-v3.md:77:  through the Instruments GUI. A hand-written row with a wrong tick size or point value corrupts
/Users/admin/praxis-signals/b2-data/outbound/4uu-VM-brief-v3.md:163:If anyone ever imports it, it contaminates genuine Kinetick `NQ 12-25` contract data with stitched
/Users/admin/praxis-signals/b2-data/outbound/4uu-VM-brief-v3.md:204:| Tick size | `0.25` |
/Users/admin/praxis-signals/b2-data/outbound/4uu-VM-brief-v3.md:205:| Point value | `$20` (tick value $5) |
/Users/admin/praxis-signals/b2-data/outbound/4uu-VM-brief-v3.md:230:| tick→minute/day generation | leave **unchecked** (already minute data) |
/Users/admin/praxis-signals/b2-data/outbound/4uu-VM-brief-v3.md:255:**Definitive check.** Open two charts for **2026-07-17**: native `NQ 12-25` (has Kinetick data) and
```

**Supplementary and clearly labelled as beyond the four files** (it changes no answer above; it only guards against reading the zero-matches as broader than they are):

```
$ grep -rn -i -E 'tick to minute|tick-to-minute|tick replay|bar generation' /Users/admin/praxis-signals/b2-data/ --include='*.md'
grep exit=1 (1 = no match)
```

No `.md` file anywhere under `b2-data/` uses those phrases. I did NOT search outside `b2-data/`, so this is not a claim that the phrases appear nowhere on the machine.

---

## Q1e — Is a "Tick to Minute" generation step even APPLICABLE to a minute-bar import?

**Reasoning strictly from the text quoted above, and nothing else.**

Premises, each traceable to a quoted line:

- **P1 — the source is minute bars, one row per minute, OHLCV.** `yyyyMMdd HHmmss;Open;High;Low;Close;Volume` (v2/INSTRUCTIONS l.78); `1,857,362 bars` (v2/INSTRUCTIONS l.81) / `1,857,362 rows` (v3 l.136); `The file is exactly what NT8's importer wants for 1-min data` (v2/INSTRUCTIONS l.76).
- **P2 — both documents explicitly classify the input as already-minute.** `(this is already minute data)` (v2/INSTRUCTIONS l.73); `(already minute data)` (v3 l.230).
- **P3 — both documents instruct the generation checkboxes OFF.** `Leave the tick→minute/day generation checkboxes unchecked` (v2/INSTRUCTIONS l.73); `| tick→minute/day generation | leave **unchecked** |` (v3 l.230).
- **P4 — the selected format is a BAR format, not a trade format.** `Format: NinjaTrader (end of bar timestamps)` (v2/INSTRUCTIONS l.69; v3 l.227) — the timestamp semantic is per-bar.
- **P5 — the destination the documents expect is the minute store.** `db\minute\NQCONT\` (v2/INSTRUCTIONS l.86; v3 l.183, l.243).

**Conclusion, stated as a claim about the documents:** a tick→minute generation step has **no role at all** in this import as specified. Such a step is by name a conversion *from* tick input *to* minute output. Per P1/P2/P4 the input is not tick input — it is already at the granularity such a step would produce, in a format the documents describe as bar-stamped. There is therefore nothing for the conversion to consume. Per P3, both documents — and note from §0.5 that these are the *only two* distinct documents in this corpus, so this is two independent statements, not four — instruct that it be left unchecked. **Enabling a tick→minute generation step would be contrary to the written instructions in both v2 and v3.** No sentence in any of the four files asks for it, requests bar generation, or uses the word "Generate" at all (Q1d: zero matches).

**What this conclusion does NOT establish.** It establishes what the documents specify. It does **not** establish:

- what NT8 actually does if such a box is ticked;
- whether the box is even present or enabled in the 8.1.7.2 Import accordion given `NinjaTrader (end of bar timestamps)` + `Last`;
- whether ticking it would silently no-op, raise an error, produce duplicate bars, or corrupt the store.

Those are runtime questions. I did not run NinjaTrader and I cannot speak to its internals. See the grading table.

---

## EVIDENCE GRADING — NT8 runtime/mechanism claims

Nobody in this session ran NinjaTrader. Every mechanism claim below is graded. Document facts (what a file *says*) are cited above and are not re-graded here.

| # | Mechanism claim (what NT8 DOES) | Grade | The single observation that would settle it |
|---|---|---|---|
| M1 | NT8 derives the target instrument from the import filename; the Import panel has no instrument field (v2 l.58–59; v3 l.148–149) | **INFERRED** | A screenshot of the 8.1.7.2 Historical Data → Import accordion showing its full field list. |
| M2 | The form `<instrument>.<DataType>.txt` is what NT8 parses, and the `.Last` token supplies the data type (v2 l.59; v3 l.149) | **INFERRED** | One import of `NQCONT.Last.txt` vs one of `NQCONT.txt`, comparing which lands data and where. |
| M3 | NT8 created the empty `db\minute\NQCONT\` from the import filename and then failed on unknown instrument (v3 l.183–194) | **INFERRED** — strongest partial support in the corpus: v3 l.190 quotes `Error on requesting bars series: 'Unknown instrument 'NQCONT'''`, attributed to 7/24 logs and a 7/25 scan. I have not read those logs; they are on the Windows machine. | Reading `log\log.20260724.*` on the NT8 VM directly. |
| M4 | Leaving the tick→minute/day generation boxes unchecked is the correct / no-op choice for minute input | **INFERRED** | One import with the box unchecked and one with it checked, comparing resulting bar counts in `db\minute\NQCONT\`. |
| M5 | Those checkboxes exist at all in this install's Import panel | **INFERRED** — asserted only by v2 l.73 / v3 l.230; I have never seen the dialog | A screenshot of the Import accordion in 8.1.7.2. |
| M6 | Importing with Time Zone left on UTC shifts every bar 4–5 hours (v2 l.71–72; v3 l.232–233) | **INFERRED** | Import the same file twice, UTC and ET, and diff the stored bar timestamps. |
| M7 | NT8 "sometimes treats a minute bar's stamp as the bar's CLOSE", shifting the 09:30 anchor by one bar (v2 l.90–92; v3 l.251–253) | **INFERRED** — the documents themselves hedge it ("sometimes") and make it a mandatory pre-Analyzer check rather than a settled fact | The STEP 4 / STEP 1b two-chart comparison on 2026-07-17 against native `NQ 12-25`. |
| M8 | `UCEERR_RENDERTHREADFAILURE` causes dialogs to silently drop clicks (v2 l.32–33; v3 l.154) | **INFERRED** | Reproduce the fault and attempt a dialog interaction. |

**VERIFIED count: zero.** No claim in this report about NT8 runtime behaviour is graded VERIFIED, because no named human is recorded *in these four files* as having personally observed any of it at a named time in a form I could check from disk. The 2026-07-25 run report referenced at v3 l.13 (`inbound\4uu-VM-status-2026-07-25.md`) may contain first-hand observations that would upgrade M3 or M5; it was outside my read list and I did not open it — **UNVERIFIED whether it does.**

Two further UNVERIFIED items, flagged rather than assumed:

- Byte-identity of `NQCONT.Last.txt` and `NQ-continuous-1min.nt8import.txt` (size and mtime match; sha256 not computed this session).
- Every hash, byte count and row count quoted inside the briefs (`c22f38fa…`, `35393823…`, `307c5e8a…`, 14,630 / 14,318 bytes, 1,857,362 rows). These are quoted as document content only. I recomputed none of them, and v3 l.111–112 itself says `**Recompute them yourself.** … Do not accept any number pasted in this brief.`

---

## S8 — questions left to Amear, unanswered here

- Whether to enable or disable any import checkbox in an actual run: reported, not decided.
- Deletion of the misnamed 95 MB `NQ 12-25.txt` — v3 l.166: *"Do NOT delete it yourself — this is Amear's call and he has not yet made it."* Reported, not decided.
- The sqlite `.bak_praxis` files — v3 l.170: *"Report the sqlite backup situation; do NOT adjudicate it."* Reported, not adjudicated.
- **No trading-hours session template is proposed here.** The documents name `CME US Index Futures RTH` (v2 l.44, l.128; v3 l.207, l.284). I report that they say it. I propose nothing, and I treat that build work as frozen.
- I express no view on what should have been done during the 7/24 or 7/25 import attempts.

---

## Process note

One Bash call was blocked by the repo's `gate-commit.sh` PreToolUse hook because this report's own prose contains the word "commit" inside a heredoc. The hook matches the literal word anywhere in the command string, not only in a real VCS invocation. No VCS operation was attempted at any point in this task. The report was written with the Write tool instead. Recorded here so the block in the transcript is not later misread as an attempted VCS action.

## Files staged

**None.** Read-only research task. No file was created, modified or deleted except this report, which is left **unstaged**. No staging or VCS command was run.

## Result

**PASS** — four files read; provenance resolved (two distinct documents in four copies, no hardlinks among the four, so v2/INSTRUCTIONS agreement is not corroboration); Q1a–Q1e answered with pasted command output including the five required zero-match greps; all eight NT8 mechanism claims graded INFERRED with a settling observation named for each; zero VERIFIED runtime claims.
