# B2 §4.3 anomalous-gap fraction — measurement and positive control

**Date:** 2026-08-15 · **Session:** 51 · **Seat:** praxis-manager
**Unit type:** read-only measurement + positive control. Nothing was fixed, and no
disposition is proposed — the ruling on what to do about this belongs to Amear.

---

## Findings first

1. **The corrected series is `/Users/admin/praxis-signals/b2-data/NQ-continuous-1min.csv`**
   (1,857,362 bars). Established by bit-exact derivation, not by bar-count coincidence:
   reformatting it into NT8 layout reproduces `NQCONT.Last.txt` byte-for-byte, while the
   superseded `reports/` copy yields a different digest. The peer's trap was avoided.

2. **The control reproduces exactly.** The §4.3 detector, lifted verbatim from
   `scripts/b2_stitch.py:746-762`, yields **937** anomalous gaps — matching the published
   `SUMMARY ... gaps=937 overall=PASS`. First run, nothing tuned.

3. **The fraction the spec gates on is ~1.6%, against a ceiling of `< ~0.1%`.**
   At the tool's threshold: 937 gaps, 30,112 missing minutes = **1.6212%** of bars
   (1.5954% of bars+missing). At the spec's ">~3 min" wording: 263 gaps, 29,305 minutes
   = **1.5778%** / 1.5533%. Adversarial denominator sweep puts the full defensible
   envelope at **0.84% – 2.31%**, i.e. **8.4× to 23× the ceiling**. No denominator
   reachable by physical argument brings it near 0.1%.

4. **The §4.3 FAIL branch is unreachable — confirmed by experiment, not by reading.**
   A 1,010-date fixture carrying **316,890 anomalous gaps (30.27% of bars)** grades
   `overall=PASS`, exit 0, with every other check green. The same fixture plus **10**
   maintenance-halt bars on one date flips to `overall=FAIL`, exit 1 — while §4.3 still
   reads `FLAG`. **Ten halt bars flip the verdict; 316,890 gaps do not.**

5. **Nothing downstream rescues the gate.** No other script implements the fraction test;
   the sibling validator explicitly disclaims it. And there is **no automated caller of
   `b2_stitch.py` at all** — no Makefile, no CI, no shell script, no n8n workflow. The
   b2 → b2-wfa handoff is manual, so the gate has no enforcement point to live at.

6. **The arithmetic was never done at acceptance time.** `0.1%` appears in no report
   predating this session; the acceptance record carries a bare count with no denominator.

### Two findings the adversarial pass added that the original measurement missed

7. **The detector measures wall-clock, not elapsed time.** `b2_stitch.py:752` subtracts two
   aware datetimes sharing one `ZoneInfo`; Python then ignores the common tzinfo and returns
   the *naive* difference. Two gaps are consequently wrong by ±60 min across DST
   transitions, and they cancel to zero only by coincidence.

8. **The five largest "gaps" are a stitch artifact, not a provider hole.** All five sit on
   contract-change dates, and the raw *back* contract holds 1,058–1,139 real bars inside
   each one. ~5,995 of the 30,112 missing minutes (~20%) are recoverable from data already
   on disk. The arithmetic of finding 3 is unaffected; the *characterisation* of what those
   minutes represent changes materially.

---

## Rubric criteria addressed

| # | Criterion (verbatim from `specs/SPEC_RUBRIC.md`) | Where |
|---|---|---|
| S1 | Every claim in a report has pasted command output, not a description of output. | throughout |
| S2 | No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure. | T4, and "does NOT establish" |
| S3 | Every gate claimed working has been deliberately tripped at least once, with the block observed. | T4 liveness arm |
| S9 + R3 | Positive control extends to claims about mechanism, not only to config keys. | T4 toggle arm |

---

## Workers dispatched

| id | mode | scope | outcome |
|---|---|---|---|
| W1 | BUILD | T1–T3 locate, control, fractions | PASS |
| W2 | BUILD | T4 positive control | PASS |
| W3 | ADVERSARIAL | attack T1–T3 numbers | NO BREAK on claims 1–5; claim 6 QUALIFIED |
| W4 | ADVERSARIAL | attack T4 unreachability (wide) | **NO RESULT** — budget-killed, no verdict, no evidence file |
| W5 | ADVERSARIAL | T4 downstream enforcement (reduced) | CLAIM QUALIFIED |

W4 returned a partial message with no verdict token and never wrote its evidence file.
Under the no-verdict ruling (R-A/R-B/R-C) that is **NO RESULT — never a pass, and never a
no-finding**. It was re-dispatched as W5 only after material reduction: the two
fixture-generation attacks were dropped (already covered by the manager's own re-runs) and
only the three search-based questions were kept.

---

## T1 — Locate and identify the corrected series

Four candidates exist; the repo tree contains none. A widened search (any `NQ*` file >10 MB
across `/Users/admin` and `/Volumes`) returned the same four and no others.

```
$ find /Users/admin /Volumes -maxdepth 6 -type f -size +10M \( -iname 'NQ*' \) 2>/dev/null | head -50
/Users/admin/praxis-signals/b2-data/NQCONT.Last.txt
/Users/admin/praxis-signals/b2-data/NQ-continuous-1min.csv
/Users/admin/praxis-signals/b2-data/NQ-continuous-1min.nt8import.txt
/Users/admin/praxis-signals/b2-data/reports/NQ-continuous-1min.csv
```

```
=== bar counts (lines minus header where present) ===
FILE                                          HEADER   LINES      BARS
NQ-continuous-1min.csv                        yes      1857363    1857362
reports/NQ-continuous-1min.csv                yes      1855412    1855411
NQCONT.Last.txt                               no       1857362    1857362
NQ-continuous-1min.nt8import.txt              no       1857362    1857362
```

The decisive basis — reformat each CSV candidate into NT8 layout and compare digests:

```
$ cd /Users/admin/praxis-signals/b2-data && for f in NQ-continuous-1min.csv reports/NQ-continuous-1min.csv; do
>   awk -F, 'NR>1{split($1,a," "); gsub(/-/,"",a[1]); gsub(/:/,"",a[2]); print a[1]" "a[2]";"$2";"$3";"$4";"$5";"$6}' "$f" > "$W/derived.txt"
>   echo -n "$f -> "; md5 -q "$W/derived.txt"
> done; echo -n "NQCONT.Last.txt              -> "; md5 -q NQCONT.Last.txt
NQ-continuous-1min.csv -> dee62ee90bbb75ff15dc1617ef45d4aa
reports/NQ-continuous-1min.csv -> 4ad45a7362c3331cea53fbcb4edf15d0
NQCONT.Last.txt              -> dee62ee90bbb75ff15dc1617ef45d4aa
```

Manager's independent confirmation that the two NT8 exports are the same file:

```
$ cd /Users/admin/praxis-signals/b2-data && md5 NQCONT.Last.txt NQ-continuous-1min.nt8import.txt
MD5 (NQCONT.Last.txt) = dee62ee90bbb75ff15dc1617ef45d4aa
MD5 (NQ-continuous-1min.nt8import.txt) = dee62ee90bbb75ff15dc1617ef45d4aa
```

**Reading.** Only the root CSV derives `NQCONT.Last.txt`. The `reports/` copy is short by
1,951 bars and produces a different digest — it is the superseded attempt-1 output and was
**not** measured for T2/T3. `NQ-continuous-1min.nt8import.txt` is a byte-identical duplicate
of the NT8 export, not a distinct series. Note that first and last timestamps are identical
across both CSVs, so timestamp span does **not** discriminate — only the digest and the bar
count do. This is why the trap caught the peer.

---

## T2 — CONTROL. Reproduce the 937

The detector was lifted by byte range rather than retyped, and `_in_break` was imported from
the live module with a source-equality assertion, so instrument drift is excluded by
construction.

```
$ python3 harness.py
FIDELITY: imported b2_stitch._in_break source == file lines 615-621  OK
FIDELITY: b2_stitch.TARGET_TZ = 'America/New_York'
FIDELITY: detector block lines 746-762 lifted verbatim (961 bytes, 17 lines)
ROWS: 1857362 bars from /Users/admin/praxis-signals/b2-data/NQ-continuous-1min.csv
ROWS: first=2021-03-07 18:01:00-05:00  last=2026-07-20 11:27:00-04:00
DST: bars in an AMBIGUOUS (fall-back repeated) wall-clock hour: 0
DST: bars at a NON-EXISTENT (spring-forward) wall clock: 0
DST: rows monotonic non-decreasing after tz attach: True

=== T2 CONTROL ===
add_check -> §4.3 anomalous intra-session gaps        FLAG   937 anomalous gap(s)
len(gaps) = 937
CONTROL vs target 937: PASS
```

**Reading.** 937 exactly, matching the published SUMMARY. The tz-reconstruction risk is
*measured* rather than assumed: zero bars fall in an ambiguous or non-existent wall clock, so
the localisation method has an empty divergence set on this data. The control passing is what
licenses T3. An independent adversarial re-derivation (W3, own detector, not a copy) also
returned 937.

---

## T3 — The fraction the spec asks for and the tool never computes

```
=== T3 ===
BARS (denominator, present bars) = 1857362
(a) tool threshold delta > 1.0   : gaps=937  missing_minutes=30112
(b) spec wording  delta > 3.0    : gaps=263  missing_minutes=29305
(b') sensitivity  delta >= 3.0   : gaps=396  missing_minutes=29571

(c) FOUR COMBINATIONS  (missing/bars ; missing/(bars+missing))
    delta>1.0 (tool)   missing=30112    /bars = 30112/1857362 = 1.6212%   /(bars+missing) = 30112/1887474 = 1.5954%
    delta>3.0 (spec)   missing=29305    /bars = 29305/1857362 = 1.5778%   /(bars+missing) = 29305/1886667 = 1.5533%
```

`missing = delta - 1` (the count of absent 1-min bars). All deltas measured integral, so
exact-float, rounded and floored arithmetic agree.

### (d) Distribution — the part that discriminates

```
(d) DISTRIBUTION — top 10 anomalous gaps by duration (delta > 1.0 set)
    #    prev_ts                    cur_ts                      delta_min    missing
    1    2021-06-10 00:00:00-04:00  2021-06-10 20:00:00-04:00      1200.0       1199
    2    2022-06-09 00:00:00-04:00  2022-06-09 20:00:00-04:00      1200.0       1199
    3    2022-09-08 00:00:00-04:00  2022-09-08 20:00:00-04:00      1200.0       1199
    4    2025-03-17 00:00:00-04:00  2025-03-17 20:00:00-04:00      1200.0       1199
    5    2025-09-15 00:00:00-04:00  2025-09-15 20:00:00-04:00      1200.0       1199
    6    2023-10-15 00:33:00-04:00  2023-10-15 16:10:00-04:00       937.0        936
    7    2023-11-05 02:15:00-05:00  2023-11-05 15:54:00-05:00       819.0        818
    8    2021-04-03 12:22:00-04:00  2021-04-03 23:47:00-04:00       685.0        684
    9    2023-03-18 12:04:00-04:00  2023-03-18 21:59:00-04:00       595.0        594
    10   2022-04-03 01:43:00-04:00  2022-04-03 11:30:00-04:00       587.0        586

    n gaps                = 937
    median gap length     = 2.0 min  (median missing = 1.0)
    mean gap length       = 33.137 min
    min / max gap length  = 2 / 1200 min
```

```
    BUCKETS (gap length in minutes, inclusive ranges)
    bucket           n_gaps    %gaps    missing_min  %missing
    2-2                 541   57.74%            541     1.80%
    3-3                 133   14.19%            266     0.88%
    4-5                  78    8.32%            259     0.86%
    6-10                 43    4.59%            287     0.95%
    11-30                26    2.77%            423     1.40%
    31-60                18    1.92%            795     2.64%
    61-180               46    4.91%           4751    15.78%
    181-600              44    4.70%          14357    47.68%
    601+                  8    0.85%           8433    28.01%

    CONCENTRATION (gaps sorted by duration, descending)
    top 5    gaps carry    5995 / 30112 missing minutes =  19.91%
    top 50   gaps carry   22428 / 30112 missing minutes =  74.48%
    top 100  gaps carry   27659 / 30112 missing minutes =  91.85%
```

**Reading.** The distribution is sharply bimodal and top-heavy. By *count* it is dominated by
trivia — 57.74% of gaps are a single missing minute. By *mass* it is dominated by a handful of
long outages: 52 gaps of ≥181 min carry 75.7% of all missing minutes, and the top 100 gaps
carry 91.85%. This is the shape of a small number of discrete outages plus a long tail of
one-minute prints, **not** a uniformly thin series.

### Adversarial denominator sweep (W3)

```
$ python3 denom.py
=== D: DENOMINATOR SENSITIVITY (numerator = 30112 missing minutes) ===
  bars (claim 3)                         den=     1857362  ->  1.6212%  (16x the 0.1% ceiling)
  bars + missing (claim 3)               den=     1887474  ->  1.5954%  (16x the 0.1% ceiling)
  calendar dates x 1380 (ETH sess/day)   den=     2362560  ->  1.2745%  (13x the 0.1% ceiling)
  weekday dates x 1380                   den=     1894740  ->  1.5892%  (16x the 0.1% ceiling)
  weekday dates x 1440 (24h)             den=     1977120  ->  1.5230%  (15x the 0.1% ceiling)
  total WALL-CLOCK minutes in span       den=     2823446  ->  1.0665%  (11x the 0.1% ceiling)

  denominator needed to reach exactly 0.1%: 30112000 minutes = 10.7x the wall-clock span
```

```
MOST-FAVOURABLE CORNER (smallest defensible numerator / largest defensible denominator)
  numerator 30112 - 5995 (five roll-routing gaps) - 531 (halt minutes) = 23586
    /full wall-clock span   = 0.8354%   (8.4x the 0.1% ceiling)
LEAST-FAVOURABLE CORNER (benign classes 1-4 re-admitted)
    42819 / bars           = 2.3054%   (23.1x)
FULL ENVELOPE ACROSS ALL ATTACKS: 0.8354% .. 2.3054%  -> 8.4x .. 23.1x the 0.1% ceiling
```

**Reading.** `bars` is defensible but slightly generous to the finding; `calendar dates × 1380`
is the better "session minutes" model and gives 1.2745%. The headline figures 1.6212% /
1.5954% are therefore **QUALIFIED** — but the conclusion they support is robust. Reaching
0.1% would require a denominator 10.7× the entire wall-clock span of the dataset, weekends
and nights included.

Threshold sensitivity (W3): `>1` 1.6212% · `>2` 1.5921% · `>=3` 1.5921% · `>3` 1.5778% ·
`>4` 1.5692% · `>5` 1.5638%. The gap **count** is fragile to threshold choice; the ~1.6%
**fraction** is not.

---

## T4 — POSITIVE CONTROL on the unreachability claim

Two confounds in the source had to be cleared first, or the experiment would be void:
`b2_stitch.py:792` short-circuits any non-`REAL` label to `SYNTHETIC-FIXTURE`, and line 706
makes a shallow fixture return `PENDING` on depth. Both were handled by building a
1,010-trading-date fixture graded at `--label REAL`.

### Arm 1 — catastrophic gap fraction, every other check green (manager's own re-run)

```
$ python3 gen_fixture.py --outdir MGR30 --days 1010 --damaged 503
FIXTURE outdir=MGR30
  dates=1010  damaged=503 (49.8% of dates)  span=2021-01-04..2024-11-15
  bars=1046730  ETH median=1380  RTH median=390
  anomalous gaps (predicted)=316890   gap-count/bars=30.2743%
  anomalous MISSING minutes=316890  missing/expected-session-minutes=22.7357%

$ python3 /Volumes/Sensidine/Praxis.build/scripts/b2_stitch.py --root MGR30 --label REAL --out MGR30/out/c.csv --report MGR30/out/r.md
INVARIANTS (1u6): bars=1046730 baseline=1046730 equal=True seam-gap=0 naive-would-drop=0
SUMMARY b2-stitch label=REAL bars=1046730 days=1010 seams=0 dupes=0 gaps=316890 overall=PASS
EXIT=0
=== graded check lines ===
| §4.1 RTH median == 390 | PASS | measured=390 over 1010 days |
| §4.1 ETH median in [1350,1380] | PASS | measured=1380 over 1010 days |
| §1.1 depth >= ~1008 trading days | PASS | trading days = 1010 |
| §4.2 no regular session inside 17:00-18:00 ET halt | PASS | max contiguous in-halt run = 0 min (FAIL threshold 5); 17:00:00 session-close endpoint excluded |
| §4.2 DST boundary hold (both flips/yr) | PASS | 8 DST flip(s) in 2021-01-04..2024-11-15; ... -> DST tracked |
| §4.3 anomalous intra-session gaps | FLAG | 316890 anomalous gap(s) |
| §4.4 monotonic non-decreasing ts | PASS | 1046730 rows |
| §4.4 zero duplicate timestamps | PASS | removed 0 duplicate(s) |
| §4.2 tz seam-loss == 0 (distinct instants preserved) | PASS | ET instants=1046730, baseline instants=1046730, seam-gap=0, bars=1046730 vs baseline=1046730 |
```

**Reading.** At 30.27% anomalous gaps — 227× the spec ceiling — the tool returns
`overall=PASS` and exit 0. It accepts the series for WFA.

### Arm 2 — S3 liveness: the FAIL machinery is alive (manager's own re-run)

Same fixture, same gap load, plus 10 maintenance-halt bars on one single date:

```
$ python3 gen_fixture.py --outdir MGRLIVE --days 1010 --damaged 503 --halt-run 10
$ python3 /Volumes/Sensidine/Praxis.build/scripts/b2_stitch.py --root MGRLIVE --label REAL --out MGRLIVE/out/c.csv --report MGRLIVE/out/r.md
SUMMARY b2-stitch label=REAL bars=1046740 days=1010 seams=0 dupes=0 gaps=316890 overall=FAIL
EXIT=1
| §4.2 no regular session inside 17:00-18:00 ET halt | FAIL | max contiguous in-halt run = 10 min (FAIL threshold 5); ... |
| §4.3 anomalous intra-session gaps | FLAG | 316890 anomalous gap(s) |
```

**Reading.** This is the S3 arm and it is the decisive contrast. The tool *can* emit FAIL and
*can* exit 1. **Ten halt bars flip the verdict; 316,890 anomalous gaps do not.** Without this
arm, "never FAIL" would be indistinguishable from a broken invocation.

### Arm 3 — sweep across magnitude (W2)

```
| cell | damaged dates | gap-count / bars | §4.3 status line | `overall=` | exit |
| S0  |   0 | 0.0000 %  | §4.3 ... | PASS | 0 anomalous gap(s)      | PASS | 0 |
| S1  |  22 | 1.0054 %  | §4.3 ... | FLAG | 13860 anomalous gap(s)  | PASS | 0 |
| S10 | 199 | 9.9778 %  | §4.3 ... | FLAG | 125370 anomalous gap(s) | PASS | 0 |
| S30 | 503 | 30.2743 % | §4.3 ... | FLAG | 316890 anomalous gap(s) | PASS | 0 |
| S60 | 801 | 59.9957 % | §4.3 ... | FLAG | 504630 anomalous gap(s) | **FAIL** | 1 |
```

**Honest nuance, carried rather than hidden.** At 60% damage `overall` *does* read FAIL. The
FAIL tokens in that report are `§4.1 RTH median | FAIL | measured=195` and
`§4.1 ETH median | FAIL | measured=690` — **§4.3 still reads FLAG**. What fired is the
collateral effect of deleting so many minutes that the per-day bar-count medians collapsed.
§4.1 is **not** a backstop for §4.3: concentrate identical damage in under half the dates and
the medians recover and `overall` returns to PASS. It is blind to the shape that matters most
— a provider hole that spares half the dates.

### Arm 4 — S9(R3) mechanism toggle (W2)

An instrumented **copy** differing from the repo file by exactly one token, run on the same
fixture bytes:

```
<     add_check("§4.3 anomalous intra-session gaps", "PASS" if not gaps else "FLAG",
>     add_check("§4.3 anomalous intra-session gaps", "PASS" if not gaps else "FAIL",

SUMMARY b2-stitch label=REAL bars=1046730 days=1010 seams=0 dupes=0 gaps=316890 overall=FAIL
| §4.3 anomalous intra-session gaps | FAIL | 316890 anomalous gap(s) |
```

**Reading.** This is the R3 toggle: hold everything constant, change only the mechanism under
test, show the behaviour changes. `overall` **is** wired to that slot. Therefore the PASS in
Arm 1 is caused **solely by the literal `"FLAG"`**, not by the check being unwired or the
fixture being unrepresentative. Reading the source and concluding unreachability would have
been the inspection-instead-of-experiment failure R3 forbids; this is the experiment.

### Arm 5 — no enforcement point downstream (W5, verified by manager)

```
$ grep -rn 'b2_stitch' --include='*.sh' --include='*.py' --include='*.json' --include='*.yml' --include='*.yaml' --include='Makefile' .
config/b2-stitch-schema.json:2:  "_comment": ... DEFAULT column schema for b2_stitch.py ...
scripts/b2_stitch.py:2:# b2_stitch.py — Praxis_build-6bw (b2-stitch)
scripts/b2_stitch.py:1066:USAGE = """usage: b2_stitch.py [--root DIR] ...
scripts/tests/b2-stitch-selftest.py:4:# Runs the FULL b2_stitch pipeline end-to-end ...
scripts/tests/b2-stitch-selftest.py:31:import b2_stitch as S  # noqa: E402
scripts/tests/b2-stitch-selftest.py:213:        rc = S.main(["b2_stitch.py", "--root", root, "--label", "SYNTHETIC-FIXTURE"])
scripts/tests/b2-stitch-selftest.py:226:        rc = S.main(["b2_stitch.py", "--root", root])
(exit 0)
=== POSITIVE CONTROL: same search finds the file itself by name ===
scripts/b2_stitch.py
```

**Reading.** Three non-doc references exist: the tool, its own selftest, and a column-alias
config. **No Makefile, no CI, no shell script, no n8n workflow invokes it.** There is no
automated consumer that could block on `FLAG`, because there is no automated consumer.
W5 further confirmed the sibling validator disclaims the check in its own header
(`scripts/b2data_raw_validate.py:7-9`: *"It does NOT run b2-data spec §4 continuous-series
checks (bar-count medians, roll seams, gaps)"*).

Manager's own check that the tool computes no fraction anywhere:

```
$ grep -n -i -E 'fraction|percent|0\.1' scripts/b2_stitch.py | grep -i -E 'gap|fraction|0\.1'
53:OI_NONZERO_FRACTION = 0.5  # OI "present" if non-zero for a MAJORITY of daily rows
379:    validator's OI_NONZERO_FRACTION convention)."""
384:    return (nonzero / n) > OI_NONZERO_FRACTION
```

**Reading.** The only `FRACTION` in the tool is the Open-Interest constant. No gap fraction is
computed. The grep matched (exit 0), so this is a live search returning a real negative, not a
false zero.

### Arm 6 — was the fraction ever evaluated historically? (W5, verified by manager)

```
$ git log -1 --format=%H HEAD
c41a969296743ceeafc261280afeb98d87577733
$ echo -n "committed HEAD:DECISION_LOG.md 1.62 count = "; git show HEAD:DECISION_LOG.md | grep -c '1\.62'
committed HEAD:DECISION_LOG.md 1.62 count = 0
$ echo -n "working tree DECISION_LOG.md 1.62 count = "; grep -c '1\.62' DECISION_LOG.md
working tree DECISION_LOG.md 1.62 count = 1
```

**Reading.** Zero occurrences in committed history; one in the working tree, authored by this
session's own audit. The acceptance-time record carries a bare count with no denominator
(`1u6-VALIDATION.md:21: | §4.3 anomalous intra-session gaps | FLAG | 937 anomalous gap(s) |`).

---

## Adversarial findings

- **W3, claims 1–5: NO BREAK FOUND.** Independent re-derivation with a separately written
  detector also returned 937. `missing = delta - 1` verified against 0 non-integral deltas.
- **W3, claim 6: QUALIFIED.** Arithmetic exact; characterisation wrong. See findings 7 and 8.
- **W3 denominator attack: conclusion robust**, envelope 0.84%–2.31%.
- **W5: CLAIM QUALIFIED.** B and D hold outright, D more strongly than stated (no caller
  exists at all rather than merely none that blocks). E is the qualification — "never
  evaluated" is true of the entire acceptance history but is no longer *literally* true as of
  2026-08-15, because this session's own audit did the arithmetic. That computation is
  self-referential, uncommitted, and self-declared UNVERIFIED, so it does not rescue the gate.
- **W4: NO RESULT**, recorded as such and not counted as a pass.

### Methodological hazard observed and corrected

W5 reported that its first two greps returned `(eval):1: no matches found: --include=*.py` —
zsh glob-expanded the unquoted patterns and grep never ran. **That failure mode is
indistinguishable from a real negative.** Every negative result in this report is accompanied
by a positive control demonstrating the search was live.

### Observer effect on Arm 6

W5's search `grep -rln '0.1%' docs/reports/` returned nothing at the time it ran. **This
report contains the string `0.1%` and lives in `docs/reports/`, so that figure is stale the
moment this file lands.** The figure is annotated rather than edited: it was true of the
corpus as it stood before this report existed.

---

## S6 cross-block check

The finding is a measurement, not a deviation, so S6 is applied to what the measured gate
*touches* rather than to an approval chain.

- **Block 2 → `zi1` (b2-wfa).** §4.5 is the acceptance gate on the WFA input series. Since the
  §4.3 leg cannot fire and no caller enforces it, any WFA run on this series inherits a
  data-quality gate that was never evaluated in the form the spec states. This is the S2
  shape — *specified ≠ implemented* — sitting on the input to the core Block-2 evidence.
- **F3 (FROZEN) — backtest fill resolution vs data granularity.** F3 already concerns the
  adequacy of 1-minute bars for fill modelling. The gap measurement is a *second, independent*
  question about the same series: F3 asks whether 1-min resolution is fine enough, this asks
  whether the 1-min series is complete. Neither subsumes the other, and clearing F3 would not
  clear this.
- **O1 — walk-forward gate set.** O1 asks which gate set applies to the replication arm. §4.5
  is upstream of that question: it decides whether the series reaches the arm at all.
- **Block 4 / F4.** No interaction found. The gate is a data-acquisition gate and terminates
  before any live path.

No other block was found to consume `b2_stitch.py` output, consistent with Arm 5's finding
that it has no automated caller.

---

## What this measurement does NOT establish

Stated by the producer so the boundary is not left to the grader to infer.

1. **It does not establish that the series is unfit for WFA.** ~1.6% anomalous-gap minutes is
   far above the written ceiling. Whether that ceiling is the *right* ceiling for 1-minute
   futures data is a separate question this unit did not test and takes no position on.
2. **It does not establish that the detector is correct.** Finding 7 shows it measures
   wall-clock rather than elapsed time, and W3 found the benign-exclusion heuristic suppresses
   214 gaps / 12,707 minutes not plausibly halt- or Sunday-related. The 937 is faithful to
   *the tool as written*, which is what the control demanded — not to a corrected detector.
3. **It does not establish that 30,112 minutes of market data are missing from the source.**
   Finding 8 shows ~5,995 of them exist in the raw back contract and were dropped by roll
   routing. The true provider-hole figure is smaller and was not separately quantified.
4. **It does not establish that the fixture in T4 resembles the real series.** The fixture is
   synthetic and uniform. It proves reachability of a code branch, not realism of a scenario.
5. **It does not establish that `overall=PASS` is never correct.** Arm 3 shows `overall` *can*
   reach FAIL at extreme magnitudes via §4.1 collateral damage. The precise claim is narrower:
   **the §4.3 check itself never emits FAIL at any magnitude**, and §4.1 is not a reliable
   backstop for it.
6. **It does not establish what should be done.** Three readings remain open — the ~0.1% bar
   may be wrong for this data class; the detector may be over-broad; the series may need a
   re-pull. Selecting among them is Amear's ruling. No disposition is proposed here.
7. **It does not audit the b2-wfa output.** Whether any WFA run has already consumed this
   series, and what that would imply, was not examined.

---

## Files staged

- `docs/reports/2026-08-15-session51-b2-gap-fraction-measurement.md` (this file) — the only
  file written.

No tracked file was modified. `scripts/b2_stitch.py`, `docs/specs/**` and all other
`docs/reports/**` files are untouched. All fixtures, harnesses and instrumented copies live
outside the repo under the session scratch directory. Verified:

```
$ find . -path ./.git -prune -o -newermt '-90 minutes' -type f -print
(no output)
```

The two untracked files `scripts/dispatch-log-close.sh` and
`scripts/tests/test-dispatch-log-close.sh` carry mtimes of 2026-07-28 and are **pre-existing
from a prior session**, not debris from this unit.

Nothing is committed. The report is staged only.

---

## Result: PASS

The control reproduced exactly (937, untuned). The fraction is measured with the arithmetic
shown, and survives an adversarial denominator sweep at 8.4×–23× the spec ceiling. The
unreachability claim is established by experiment with a firing positive arm, a mechanism
toggle, and a liveness contrast — not by reading the source. Two material qualifications
found by the adversarial pass are carried in the findings rather than suppressed.
