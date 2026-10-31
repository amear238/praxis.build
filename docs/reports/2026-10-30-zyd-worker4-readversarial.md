# Praxis_build-zyd — worker 4 re-adversarial (after the fix pass)

## Task
ADVERSARIAL, read-only. Re-attack the unstaged working-tree edits after the fix pass: `DECISIONS.md` entry D-2026-10-30-A (DECISIONS.md:247-293), `config/backtest-cost-model.json` v1.1.0, and the 11 new MANIFEST rows (133-143). Criteria: bead zyd acceptance (a)(b)(c), rubric F3 (`specs/SPEC_RUBRIC.md:45-57`), S1/S2/S4/S5/S6/S8. The only file written is this report. Scratch files are in `.../scratchpad/w4r/` (chk.py, entry.md).

## Mechanical checks (pasted)
```
$ python3 -I -m json.tool config/backtest-cost-model.json >/dev/null && echo JSON_OK
JSON_OK
$ python3 -I .../w4r/chk.py
slippage_ticks_per_side 2 / slippage_usd_per_side 10.0 / slippage_round_turn_ticks 4 / slippage_round_turn_usd 20.0
total_cost_per_round_turn_usd 22.96 / total_cost_per_round_turn_ticks 4.592 / tick_value_usd 5.0
rt usd 22.96 rt ticks 4.592 comm ticks 0.592
rows 1
void identical: True 289 289          # DECISIONS void clause vs DECISION_LOG 00:10:00Z, byte-compared
21:36 copy identical: True
lim in config: True
entries count D-2026-10-30-A: 1
$ git diff DECISIONS.md MANIFEST.md | /usr/bin/grep -c '^-[^-]'
0
$ shasum -a 256 ninjascript/PraxisNoiseAreaBreakout.cs ; git show 719ab11:ninjascript/PraxisNoiseAreaBreakout.cs | shasum -a 256
35393823e9bc146e95dcb1d9f6fe5785a3c72ee3a3fb71287f33fe2242752265 (both)
$ /usr/bin/grep -nE 'Enter(Long|Short)|Exit(Long|Short)|Submit|SetStopLoss|SetProfitTarget|SetTrailStop|Limit|StopMarket' ninjascript/PraxisNoiseAreaBreakout.cs
211 ExitLong("XL","") / 219 ExitShort("XS","") / 224-225 comments / 227 EnterLong(Contracts,"L") / 229 EnterShort(Contracts,"S") / 288 ExitLong("FlatEOD","") / 290 ExitShort("FlatEOD","")
code :105 Calculate.OnBarClose; :108 IsExitOnSessionCloseStrategy = true; :189 if (mod >= CloseMod) FlattenAll; :196 isCheckpoint ...; :200 double price = Close[0];
$ head -1 / tail -1 / wc -l ~/praxis-signals/b2-data/NQ-continuous-1min.nt8import.txt
20210307 180100;16120.5;16167;16120.5;16154.75;17
20260720 112700;29005.5;29020.75;29003.5;29016;308
 1857362
```

## Prior-defect table
| id | state | evidence |
|---|---|---|
| B1 | RESOLVED | Title: `F3 backtest fill resolution (CONDITIONAL, void clause live) + band-edge slippage [N] = 2 ticks/side (locked by Amear)`. Status: `CONDITIONAL — committed per Amear's ruling DECISION_LOG 2026-08-29T00:10:00Z with its void clause live …; [N] = 2 ticks/side LOCKED by Amear at 2026-10-30T21:36:30Z, reaffirmed at 2026-10-30T22:22:00Z (WHO: amear)`. Only [N] is called LOCKED. Ledger 442: "`[N]` = 2 … does not change the locked number". Ledger 450: "`[N]` STAYS 2 ticks — locked before results." |
| M1 | RESOLVED (attribution residue, see m-new-1) | `Only the first is a slippage item; the ledger (2026-10-30T21:36:30Z) says 2 ticks prices stamp-to-next-open slippage, and no row says it prices the others`. Ledger 442: "so the number prices stamp-to-next-open slippage, not touch adverse selection". A grep of the ledger for "(2 ticks|[N]) … price" returns only 353 (Amear's 00:10 framing, quoted by the master) and 442. |
| M2 | RESOLVED (minor residue, see m-new-4) | Config note: "…no Set*/Submit*/limit/stop call — OBSERVED in code). That NT8 realises these calls as market orders, so intrabar High/Low ordering does not decide entries/exits, is INFERRED. Fill assumed at the next bar's open (INFERRED). CONDITIONAL under the void clause…" |
| M3 | RESOLVED | HEAD note ended "Python MC assumes fills already reflect this via the exported NT8 trade list." The new note carries the same sentence verbatim. `applies_to` is unchanged and still includes "Python Monte Carlo". |
| M4 | RESOLVED (one range off by two lines) | Entry (c): "the FlatEOD exits (`:288`, `:290`) run on any bar with mod >= CloseMod (`:189`), a clock condition". Code :189 matches. Cited ranges checked: D3 header at :737, but D4 starts at :774 (`## D4 — Run 1 …`), so `:737-775` overruns by two lines (m-new-5). Audit-1 §5 at :1164-1173 holds: "That `Close[0]` is then the close of a finished bar is NT8 runtime semantics (INFERRED…)". §7 at :1185-1207 holds: the corrected :752/:762 text with OBSERVED/INFERRED split. D2 at :688-735 holds. D2(a) at :710 holds: "expected to fill at the Open of the 10:01-stamped bar … (INFERRED…)". |
| M5 | RESOLVED at :265, CONTRADICTED at :293 (see MAJ-2) | :265 reads `Limitation sentence — PROPOSED wording, not ruled by Amear (his ruled requirement is only "Fills are optimistic and the report states so", …)`. NEEDS AMEAR 4 says "Approve or replace". |
| M6 | RESOLVED | S6 F4 bullet. f4 report :45 = "2. **Automated tools may not be built to exploit sim-environment fill favorability.**". :151 = "## 4. S6 cross-block check — MFFU restriction 2 couples to F3". |
| m1 | NOT RESOLVED (label fixed, file absent) | MANIFEST row now reads "Manager report … ungraded at time of row", but `ls docs/reports/2026-10-30-zyd-f3-artifact.md` gives `No such file or directory`. |
| m2 | RESOLVED in DECISIONS; NOT in MANIFEST | All 6 `22:22:00Z` cites in the entry carry `(WHO: amear)` (grep -o pasted by the manager; re-run: 6 hits, all followed by "(WHO: amear)"). The MANIFEST run-3 row still reads "(DECISION_LOG 2026-10-30T22:22:00Z)" with no WHO, and ledger rows 446 (master) and 450 (amear) share that timestamp. |
| m3 | RESOLVED | "The clause's trigger is "the VM measurement", which has not been run; the master's reading (2026-10-30T21:36:30Z) is that it is not exercised while no run sets High. Whether a High run is the trigger is Amear's." |
| m4 | RESOLVED | Context: "(INFERRED per 3gm D2(a) `:710`)". Line 710 is the correct Fill bullet; the earlier suggested :722 was wrong. |
| m5 | RESOLVED | "No Set*/Submit*/limit/stop call exists (OBSERVED); assuming the Enter*/Exit* calls are market orders (INFERRED), there is no resting or touch-triggered order" |
| m6 | RESOLVED | "plus (`:108`) IsExitOnSessionCloseStrategy = true — platform session-close exit, clock-triggered (INFERRED)". Code :108 matches. |
| m7 | RESOLVED | "Claude-written voice-session notes recording Amear's rulings (unaudited; …)". Ledger 21:36:00Z (WHO: amear) supports "his rulings": "Amear points at as his record". |

## New attacks
1. **Unlisted open ledger row bearing on (c).** Ledger 355:
   ```
   - [2026-08-29T00:40:00Z] WHO: praxis-master … A STRONGER F3 CLEARANCE PATH … the R3 Standard-vs-High control experiment. PROPOSED TO AMEAR; NOT ADOPTED, BECAUSE THE `00:10:00Z` RULING IS HIS … it converts "fill resolution is irrelevant here" from an argument into an observation … STATE: open — proposed to Amear; the `00:10:00Z` ruling stands until he amends it
   ```
   `grep -c '00:40' entry.md` → `0`. No later row disposes of it: a grep for `Standard-vs-High|00:40:00Z|control experiment` after line 355 returns nothing. The prior adversary's report has no hits either. → MAJ-1.
2. **"Resolves:" vs NEEDS AMEAR 2.** Entry :251 reads `**Resolves:** rubric F3's written-assumption requirement (specs/SPEC_RUBRIC.md:45-57); bead Praxis_build-zyd acceptance (a)(b)(c).` F3's criterion is "…stated in writing before the backtest runs" (rubric :46-48). NEEDS AMEAR 2 asks Amear "Does that satisfy F3's 'stated in writing before the backtest runs'?" The entry asserts the requirement is resolved and also asks Amear whether it is met. → MAJ-3.
3. **"the limitation sentence above" in Unblocks.** :293 reads `F3's unblock condition also requires each backtest report to carry the limitation sentence above`. Rubric :55-56: "the backtest report carries it as a stated limitation". The rubric requires the assumption, not a specific wording. The entry turns the PROPOSED wording into the unblock requirement. → MAJ-2.
4. **END-STAMPED label.** Entry (a): `END-STAMPED (REPORTED BY AMEAR; bar-time check PASS …:22-27…)`. Notes :22 heading: "Bar-time check (NT8 read by Amear; file read by Claude)". Notes :25: "Source convention: the file is **end-stamped**. It has 1,302 `17:00:00` rows …" — that conclusion is Claude's inference from the file. Amear read the 9:31/9:32 Opens. The 3gm D2 :690 label "REPORTED BY AMEAR, notes:23–27" carries the same imprecision. → m-new-2.
5. Arithmetic, JSON parse, void-clause byte identity, zero deleted lines: all HOLD (pasted above).
6. Import-file facts (first row, last row, 1,857,362 lines): HOLD (pasted). D-2026-07-17-A, D-2026-07-21-A and D-2026-07-04-B exist (DECISIONS.md:203, :222, :43). SHM-4 at `STRATEGY_HEALTH_MONITOR_SPEC.md:47-50` holds. O4 at rubric :94-99 holds. Q9 text at DECISIONS.md:189 holds. R-normalisation consumer is sourced from config `applies_to[2]`.
7. Zyd worker reports `2026-10-30-zyd-worker1-build.md`, `-worker2-adversarial.md` and `-worker3-fix.md` exist on disk with no MANIFEST rows. The six 3gm sub-reports got rows. → m-new-3.

## Findings

### BLOCKING
None.

### MAJOR
**MAJ-1 — Open, undisposed proposal 2026-08-29T00:40:00Z (the R3 Standard-vs-High control) is omitted (S4/S6/S8).** (c) is an INFERRED argument. The ledger holds an open, Amear-gated proposal to turn it into an observation, and running High is also what the void-clause status turns on ("no run has set High"). The entry closes the bead without naming it, which decides by omission that the control is not needed. Fix text:
- Add to (c), after "…is INFERRED.": `A falsifier for this argument was proposed and is open, not run: the R3 Standard-vs-High control (DECISION_LOG 2026-08-29T00:40:00Z, STATE open; a High run would also bear on the void clause). Its disposition is Amear's.`
- Add NEEDS AMEAR 5: `The R3 Standard-vs-High control proposed at 2026-08-29T00:40:00Z is open. Run it before F3 is unfrozen, or let (c) stand as INFERRED?`

**MAJ-2 — Unblocks line makes the PROPOSED wording mandatory (S8; contradicts :265 and NEEDS AMEAR 4).** Replace `F3's unblock condition also requires each backtest report to carry the limitation sentence above; this entry does not do that.` with `F3's unblock condition also requires the backtest report to carry the assumption as a stated limitation (specs/SPEC_RUBRIC.md:55-56); the wording is Amear's (NEEDS AMEAR 4); this entry does not do that.`

**MAJ-3 — "Resolves:" asserts F3's criterion (incl. timing) and bead acceptance are met, while NEEDS AMEAR 2 asks Amear exactly that (S8, S2; internal contradiction).** Replace the Resolves line with `**Addresses (for audit; not a grade):** rubric F3's written-assumption requirement (specs/SPEC_RUBRIC.md:45-57) and bead Praxis_build-zyd acceptance (a)(b)(c). Whether it satisfies F3 — including "before the backtest runs" — is Amear's (NEEDS AMEAR 2); F3 stays FROZEN until he changes specs/SPEC_RUBRIC.md.`

### MINOR
- **m-new-1 (attribution).** "the ledger (2026-10-30T21:36:30Z) says 2 ticks prices stamp-to-next-open slippage". That clause sits in the master's "What the master does not assert" text inside a WHO: amear row. It is INFERRED and "to be confirmed by 3gm". Amear's own framing (00:10:00Z) was stop-cluster adverse selection, and 00:35:00Z surfaced the mismatch to him without a re-ruling. Fix: `the master's note in row 2026-10-30T21:36:30Z (INFERRED from source, pending 3gm) says 2 ticks prices stamp-to-next-open slippage; Amear's own framing (00:10:00Z) was stop-cluster adverse selection, and 00:35:00Z surfaced the mismatch without his re-ruling; no row says it prices the others`.
- **m-new-2 (label).** (a) `END-STAMPED (REPORTED BY AMEAR; …)` → `END-STAMPED (INFERRED by Claude from the import file's row counts, notes :25; Amear's NT8 read of the 9:31/9:32 Opens REPORTED, notes :23; bar-time check PASS …)`.
- **m-new-3 (MANIFEST).** The `2026-10-30-zyd-f3-artifact.md` row registers a file that does not exist (prior m1 carried over). Either the file lands before staging or the row is withheld. The zyd worker1/2/3 reports have no rows. Add rows labelled "NOT authoritative; sub-report to the zyd manager report".
- **m-new-4 (config note).** "evaluated … on the 16:00 clock for FlatEOD" → `on any bar with minute-of-day >= 16:00 for FlatEOD`. It also omits the platform session-close exit (:108). Add `plus the platform session-close exit (IsExitOnSessionCloseStrategy, clock-triggered, INFERRED)`.
- **m-new-5 (citation).** `3gm D3 :737-775` → `:737-773`. D4 begins at :774.
- **m-new-6 (MANIFEST timestamp).** Run-3 row `(DECISION_LOG 2026-10-30T22:22:00Z)` → `(DECISION_LOG 2026-10-30T22:22:00Z, WHO: amear)`.

## NOT CHECKED
- The UNGRADED research `docs/reports/2026-08-07-f3-fill-resolution-research-UNGRADED.md`, cited by row 355, was not read.
- Whether any non-ledger channel disposed of row 00:40:00Z. Only the ledger was grepped.
- The run-3 screenshot image itself. I relied on ledger 449's transcription for "Standard (Fastest)".
- NT8 runtime semantics (fill timing, slippage application, clamp). None was observable from here.
- Staged-vs-unstaged interplay beyond MANIFEST. The staged MANIFEST adds 15 rows dated 2026-07-26 to 08-07, and none of them duplicates the 11 new rows (path grep counts: 3gm-fidelity-check 6 matches across the 3gm rows; voice notes 1; run3 record 1; config 2 = original + UPDATE row).
- The rest of DECISIONS.md / DECISION_LOG.md beyond the cited rows.

VERDICT: BREAK FOUND
