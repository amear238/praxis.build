# Praxis_build-zyd — worker6 final ADVERSARIAL re-attack (after fix pass 2)

## Task
Try to break D-2026-10-30-A (DECISIONS.md, unstaged), the `config/backtest-cost-model.json` v1.1.0 diff, and the MANIFEST rows appended after line 132. Criteria: the bead zyd (a)/(b)/(c) acceptance, rubric F3 (`specs/SPEC_RUBRIC.md:45-57`), and S2/S4/S5/S6/S8.

## Mode
ADVERSARIAL, read-only. The only file written is this report. Nothing was staged.

## Attacks with pasted output (abridged to the load-bearing lines)

### 1. DECISION_LOG timestamps
I grepped all eight cited timestamps. All exist. The WHO values are: 347 `00:10:00Z` master/APPROVED BY amear, 353 `00:35:00Z` master, 355 `00:40:00Z` master, 442 `21:36:30Z` **WHO: amear**, 449 `22:17:00Z` master, 446 `22:22:00Z` master, 450 `22:22:00Z` **WHO: amear**, 454 `22:28:00Z` master, 452 `22:40:00Z` master. All six `22:22:00Z` cites in the entry carry `(WHO: amear)`:
```
22:22:00Z (WHO: amear) / 22:22:00Z` (WHO: amear) kep / ...(WHO: amear)) / ...(WHO: amear) / ...(WHO: amear) (`[ / ...(WHO: amear) (no
```
The attributed content matches: 450 has "`[N]` STAYS 2 ticks — locked before results" and asks the build side to "CONFIRM the unit and that slippage is applied on every market fill". 449 has "Order fill resolution "Standard (Fastest)", Slippage 2". 442 has "Void-clause status (REPORTED BY AMEAR …) … NOT triggered; it is also NOT retired, since no run has set High", plus the master's "prices stamp-to-next-open slippage (INFERRED from source …)". 355 has the R3 control "PROPOSED TO AMEAR; NOT ADOPTED".

### 2. Line and section citations
- 3gm `:710`: "The resulting market order is expected to fill at the Open of the 10:01-stamped bar … (INFERRED …). DECISION_LOG:353's "filled at the next bar's open" is likewise INFERRED". ✓
- 3gm `:737-773` (D3) ✓. `:1164-1173` (§5 OnBarClose: "runtime half is INFERRED") ✓. `:1185-1207` (§7: market-order realisation INFERRED) ✓. `:688-735` (D2) ✓. D2(c) at `:716`: "CANNOT-DETERMINE-STATICALLY … next day's 09:31 (INFERRED)" ✓.
- `.cs` file: sha256 `35393823e9bc…2242752265`; `git log -1` = `719ab11`; no diff vs HEAD. `:105` `Calculate.OnBarClose`, `:108` `IsExitOnSessionCloseStrategy = true`, `:189` `if (mod >= CloseMod)`, `:196` checkpoint, `:200` `double price = Close[0];`, `:211/:219/:227/:229/:288/:290` exactly as quoted, `CloseMod = 16 * 60; // 960` (`:58`). ✓ A broad grep `Set[A-Z][A-Za-z]*\(|Submit|Limit|StopMarket|StopLimit|ChangeOrder|CancelOrder` returns exit 1 (no match). ✓
- Voice notes `:22-27` (bar-time check, "Bar times: **PASS.**"), `:23` (Amear's 9:31/9:32 Opens), `:25` (end-stamped from row counts) ✓. `git ls-files --error-unmatch` → "did not match any file(s) known to git", so the file is untracked ✓.
- Import file: first `20210307 180100;…`, last `20260720 112700;…`, `wc -l` 1857362 ✓.
- Rubric `:45-57` is F3 and `:55-56` is "Unblocks when …" ✓. `:94-99` is O4 ±15%/±25% ✓. The working-tree rubric diff hunk is `@@ -265,0 +266,10 @@`, so no line shift ✓.
- SHM `:47-50`: SHM-4 Metric includes slippage, Trigger `[TBD]` ✓. D-2026-07-15-B Q9: "SHM-4: … slippage >2 ticks/side worse" ✓.
- F4 `:45` "Automated tools may not be built to exploit sim-environment fill favorability." ✓ `:151` "## 4. S6 cross-block check — MFFU restriction 2 couples to F3" ✓.

### 3. Labels
I checked every one of these against its source: INFERRED on fill-at-next-open; INFERRED on OnBarClose runtime and market-order realisation; CANNOT-DETERMINE on D2(c), same-bar reverse and early-close; REPORTED for run 4; UNCONFIRMED for "2 ticks on every fill". None is stated flatly in the entry. The exceptions are F-3 and F-4 below.

### 4–5. Contradictions and S8
Statements checked: Status CONDITIONAL; Addresses "not a grade" (and F3 satisfaction is Amear's, NEEDS 2); limitation wording PROPOSED (NEEDS 4); R3 disposition Amear's (NEEDS 5); SHM-4 re-basing Amear's (NEEDS 1); void-clause trigger Amear's. None says F3 is FROZEN, PASSED or unfrozen. The exceptions are F-2 and F-4.

### 6. Mechanical checks
```
JSON_OK
added {'amended'} removed set()
commission 2.96 2.96 True True
2.96+20 = 22.96 2.96/5+4 = 4.592
cfg 22.96 4.592 True True True
instrument True / applies_to True / bead True / created True
entry==00:10 row: True 289 289      (void clause, byte compare)
21:36 copy == 00:10: True
deleted lines: 0
 DECISIONS.md | 51 +++ ; MANIFEST.md | 16 +++  (67 insertions)
```
No `.py`, `.sh` or `.js` file in the repo references `backtest-cost-model`, so the added key breaks no parser.

### 7. MANIFEST
Every appended path exists except `docs/reports/2026-10-30-zyd-f3-artifact.md`, which is excluded per the brief. The evidence sha256 = `8787483dcb41…a90eac55` matches the row. `Report`, `Config` and `Asset` are all already in use (61/19/2). The 3gm `:1028` line is "## Audit-1 corrections (2026-10-30)" and the file has 1348 lines ✓.

## Findings

**F-1 MAJOR (S2, part (c)). The entry leaves out a contrary hypothesis from the source it cites.** 3gm D4 `:784` (INFERRED, ranked hypothesis 5):
```
5. **Order fill resolution** High vs Standard. This could change how same-bar exit+reverse pairs and the 16:00 orders resolve.
```
D4 #2 (`:780`) adds that a changed carried position "changes whether entries fire". So the graded source says the fill-resolution setting could change how two of the entry's own residuals resolve, and through them later entries. The entry's (c) heading says "Why the fill-resolution choice does not decide this strategy's entries/exits". It lists "same-bar exit+reverse" and "the 16:00 FlatEOD fill path" only as residual risks and never links them to fill resolution. The config note's "intrabar High/Low ordering does not decide entries/exits, is INFERRED" has the same gap. The label is INFERRED, but the inference is shown without the opposing inference from the same report. Prior workers did not catch this (grep for `784` across the zyd worker reports returns nothing).
**Fix text:** append to (c), after the R3 sentence: "Counter-inference on record: 3gm D4 hypothesis 5 (`docs/reports/2026-10-30-3gm-fidelity-check.md:784`, INFERRED) states that Order fill resolution High vs Standard 'could change how same-bar exit+reverse pairs and the 16:00 orders resolve'. The second and third residual risks below are therefore also fill-resolution items, and (c) holds only for the checkpoint decision itself, not for how those two order pairs execute. The R3 control tests both." In the config `fill_resolution_note`, after "…is INFERRED.", add: "3gm D4 :784 (INFERRED) notes resolution may change how same-bar exit+reverse and 16:00 orders resolve."

**F-2 MAJOR (S8). An open question that a cited, graded source reserves for Amear is missing from NEEDS AMEAR.** 3gm `:949`:
```
DECISION_LOG:442 locks `[N]` as **band-edge** slippage. Whether that lock was meant to cover session-close and stop-out exits as well is Amear's scope question; it is not decided here
```
`:966`: "F8: the 2-tick scope was stated as fact. Now INFERRED, and its scope is put to Amear." The entry applies $22.96 RT to "All P&L distributions" with no carve-out. Its NEEDS AMEAR 3 asks only the NT8 readback ("does NT8 apply Slippage 2 on every market fill"), not his intent. Mitigation: Amear's own row 442 computes "≈ $22.96 per round trip". The caller may downgrade to MINOR on that basis.
**Fix text:** add as NEEDS AMEAR 6: "3gm `:949` leaves open, as yours: was the band-edge `[N]` = 2 lock meant to cover the session-close (FlatEOD / Exit-on-session-close) and checkpoint stop-out exits as well as band-breakout entries? The config applies 2 ticks to every side of every round turn pending your answer."

**F-3 MINOR (S2/S4). The void-clause Status attributes "not exercised while no run sets High" to the master, when the source labels it Amear's report.** In row 442 (WHO: amear) that inference sits inside the block labelled "Void-clause status (REPORTED BY AMEAR, not observed by the master)". The entry also states without a label "the VM measurement, which has not been run", which rests only on that REPORTED fact.
**Fix text:** replace "the master's reading (2026-10-30T21:36:30Z) is that it is not exercised while no run sets High" with "row 2026-10-30T21:36:30Z records, in its REPORTED BY AMEAR block, that it is not triggered and not retired since no run has set High". Replace "which has not been run" with "which has not been run (REPORTED: no run has set High, 21:36:30Z)".

**F-4 MINOR (S8, F3 state).** The Status line reads "CONDITIONAL — committed per Amear's ruling…". The artifact is unstaged and uncommitted, and row 454 says "Commit is Amear's". "The assumption is committed" is half of F3's unblock condition (`SPEC_RUBRIC.md:55`).
**Fix text:** "CONDITIONAL — in the form ruled by Amear at DECISION_LOG 2026-08-29T00:10:00Z, void clause live (see below); the commit is Amear's."

**F-5 MINOR (scope-of-change completeness).** "Scope of change (explicit)" does not mention that a new key `amended` was added (`added {'amended'}`), nor the edits to `$schema_note`, `decision_ref`, `fill_resolution_note` and `total_cost_breakdown_note`. The brief asked for "key set unchanged vs HEAD", and that check fails by one added key. No code consumer exists, so there is no functional break.
**Fix text:** add a bullet: "Added key `amended: 2026-10-30`; `$schema_note`, `decision_ref`, `fill_resolution_note` and `total_cost_breakdown_note` text updated. No key removed."

**F-6 MINOR (S2, MANIFEST).** The worker4 row says "BREAK FOUND, fixed by worker5", but this re-attack is the grading of worker5's fix. The worker2 row's "fixed by worker3" was graded by worker4 as RESOLVED with residues.
**Fix text:** worker4 row → "BREAK FOUND; fix pass by worker5, re-attacked by worker6". worker2 row → "BREAK FOUND; fixes graded RESOLVED (with residues) by worker4".

## NOT CHECKED
- Run-4 figures beyond the ledger row (REPORTED; no screenshot on disk).
- Whether the run-3 screenshot itself shows "Standard (Fastest)". I relied on the row 449 transcription and did not open the image.
- 3gm `:1028-1348` correction contents beyond §5/§7.
- The full text of the 3gm worker sub-reports behind the "NOT authoritative; superseded" wording.
- Whether the MANIFEST column-3 value `2` is the right Phase for each row.

VERDICT: BREAK FOUND
