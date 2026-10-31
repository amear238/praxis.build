# Praxis_build-zyd — F3 artifact: DECISIONS D-2026-10-30-A, cost model v1.1.0, MANIFEST rows (manager report)

Manager: praxis-manager. Dispatched by praxis-master, DECISION_LOG row `2026-10-30T22:28:00Z`. Branch `main`, HEAD `fc77f36`. Nothing committed. The commit is Amear's.

## Task

Produce the F3 artifact. Append DECISIONS.md entry D-2026-10-30-A, which amends D-2026-07-15-B Q5's slippage and fill-resolution terms. Bump `config/backtest-cost-model.json` to v1.1.0 (2 ticks/side, Standard, $22.96 / 4.592 ticks RT). Append MANIFEST rows. Stage the three files and the reports. Do not touch specs, DECISION_LOG, STATUS, HANDOFF or ninjascript.

## Rubric criteria addressed

- **F3** (`specs/SPEC_RUBRIC.md:45-57`): quoted in full under Verification evidence (E1).
- **S1:** every claim below sits on pasted output (E1–E9).
- **S2:** labels are carried from their sources, never upgraded. Four adversarial rounds hunted for upgrades (see Adversarial findings).
- **S4/S5:** the authorisation chain is given as DECISION_LOG row timestamps. Every row was read on disk this session (`:347`, `:353`, `:355`, `:441`, `:442`, `:449`, `:450`, `:454`).
- **S6:** see the S6 cross-block check.
- **S8:** six questions are routed to NEEDS AMEAR and none is answered. Nothing is said about F3's FROZEN/PASSED state.
- **Bead zyd acceptance (a)(b)(c):** mapped below. (c) is NOT fully met, and the entry says so.

## Workers dispatched

| id | mode | report | outcome |
|---|---|---|---|
| w1 | BUILD | `docs/reports/2026-10-30-zyd-worker1-build.md` | 3 edits made; self-reported PASS |
| w2 | ADVERSARIAL | `…-zyd-worker2-adversarial.md` | BREAK FOUND: 1 BLOCKING (entry said "LOCKED"; Amear ruled CONDITIONAL), 6 MAJOR, 7 MINOR |
| w3 | BUILD (fix) | `…-zyd-worker3-fix.md` | fixes F1–F12 applied |
| w4 | ADVERSARIAL | `…-zyd-worker4-readversarial.md` | BREAK FOUND: 3 MAJOR (R3 control row `00:40:00Z` omitted; Unblocks made the proposed wording mandatory; "Resolves:" contradicted NEEDS AMEAR 2) |
| w5 | BUILD (fix) | `…-zyd-worker5-fix2.md` | fixes G1–G8 applied |
| w6 | ADVERSARIAL | `…-zyd-worker6-final-adversarial.md` | BREAK FOUND: 2 MAJOR (3gm `:784` contrary hypothesis omitted; `[N]` scope question `:949` missing from NEEDS AMEAR) |
| w7 | BUILD (fix) | `…-zyd-worker7-fix3.md` | fixes H1–H6 applied |
| w8 | ADVERSARIAL | `…-zyd-worker8-final2-adversarial.md` | BREAK FOUND: 1 MAJOR (position-state path to later entries hidden) + 5 MINOR |
| w9 | BUILD (fix) | `…-zyd-worker9-fix4.md` | fixes K1–K7 applied |
| w10 | ADVERSARIAL | `…-zyd-worker10-closing-adversarial.md` | BREAK FOUND: 1 MAJOR, a mis-cited line (`:780` should be `:781`; the error was the manager's, in the K1 brief) + MINORs. Sentence-by-sentence pass; everything else HOLDS |

Every adversary got the artifact and the criteria, never the producer's reasoning. Every adversarial report ends in an explicit VERDICT line.

## Process log

1. Read the rubric (`:1-60`, F3 at `:45-57`) and the eight cited DECISION_LOG rows. Read `bd show Praxis_build-zyd`, the config at HEAD, DECISIONS `:170-243`, and the 3gm report (D2, D3, D4, Audit-1 §1/§5/§7, S6 `:949`). Read the voice notes and the run-3 record. Grepped the order calls in the `.cs` file.
2. **Two facts beyond the brief were found and carried into the entry:**
   - Run 3 was ruled INVALID by Amear (`2026-10-30T22:22:00Z`, line 450).
   - Whether NT8 applies Slippage 2 on every fill is UNCONFIRMED (same row).
3. Noted that `docs/reports/2026-10-28-voice-session-notes.md` is UNTRACKED in git (`git ls-files` → 0).
4. w1 built. Before trusting w1, the manager re-ran its checks and ran two negative arms (E7).
5. Four adversary → fix cycles (w2→w3, w4→w5, w6→w7, w8→w9). Each fix brief carried exact replacement text, and the manager confirmed each finding on disk before dispatching the fix:
   - B1 against `:347`;
   - M4 against `.cs:189`;
   - MAJ-1 by grepping DECISION_LOG after line 355 for any disposal of the `00:40:00Z` proposal (none);
   - F-1 against 3gm `:774-786`;
   - F-3 against `:441`.
6. After w10, the manager made five single-line edits itself (allowed: single-line doc edits). Each was applied by a script that requires its old string to match exactly once, and each quote was checked against its source (E8):
   - (i) `:780` → `:781` in (c);
   - (ii) the config note re-attributes the position-state path to 3gm D4 hypothesis 2;
   - (iii) one S6 bullet naming two spec texts that still carry the superseded Q5 terms;
   - (iv) "set explicitly" relabelled REPORTED BY AMEAR (the screenshot shows only the value);
   - (v) the SHM-4 range `:47-50` → `:48-51`.
7. **Defect found in our own check:** `grep -c '^-[^-]'` was used by every worker and by the manager to prove "no deleted lines". It is BLIND to a deleted markdown bullet, because the diff renders a deleted `- ` bullet as `-- `. Shown by a positive arm (E7b). The corrected form, `grep '^-' | grep -vc '^---'`, fires. All deletion counts below use the corrected form. The DECISIONS proof of record is the HEAD hash match on lines 1–243 (E4).
8. Staged the three files and the ten worker reports, then re-staged DECISIONS.md after edits (iv) and (v). Evidence was re-captured after the final stage.

**Deviations from the master's brief, each forced by a rubric line:**
- **Heading/Status:** the brief dictated "…slippage LOCKED (Amear…)". Row `2026-08-29T00:10:00Z` rules the assumption "CONDITIONAL, carrying an explicit VOID CLAUSE, not as a decision", and only `[N]` was locked (`21:36:30Z`). The heading now reads "fill resolution (CONDITIONAL, void clause live) + band-edge slippage [N] = 2 ticks/side (locked by Amear)". (S2/S8.)
- **Limitation sentence:** the brief's exact wording is marked PROPOSED, not Amear's. His ruled requirement is only "Fills are optimistic and the report states so". It goes to NEEDS AMEAR 4. (S8.)
- **END-STAMPED label:** the brief said REPORTED BY AMEAR, but voice notes `:22`/`:25` show it is Claude's inference from the file. Amear's NT8 read (`:23`) is the REPORTED part.
- **MANIFEST:**
  - The webp row's Type is `Asset`, the file's existing vocabulary, not `Evidence`.
  - The config UPDATE row keeps Date Created = 2026-07-15 (the file's creation date), with the update date in Purpose.
  - Rows were added for the ten zyd worker sub-reports.

## Verification evidence (pasted output only)

### E0 HEAD

```text
$ git rev-parse --short HEAD
4d7ca80
```

### E1 Rubric F3, specs/SPEC_RUBRIC.md

```text
$ sed -n '45,57p' specs/SPEC_RUBRIC.md
### F3 — Backtest fill resolution vs. acquired data granularity
**Criterion.** The fill resolution the Strategy Analyzer will actually run at,
and the slippage assumption applied at the band edge, stated in writing before
the backtest runs.
**Why frozen.** The Block 2 spec requires Order Fill Resolution = High with a
1-tick resolution series, 1-tick slippage, $2.96 round-trip. Deviation F
delivered 1-minute bars. High-resolution fill modelling needs a finer intrabar
series. A band-touch strategy backtested on 1-minute bars with no intrabar
resolution produces optimistic fills exactly where the edge lives, and the
optimism is invisible in the output.
**Unblocks when.** The assumption is committed and the backtest report carries
it as a stated limitation.
**Blocks.** `4uu`. Everything downstream of `4uu`.
$ git diff --stat specs/SPEC_RUBRIC.md   # unstaged edit by another party, hunk at :263+, not F3
 specs/SPEC_RUBRIC.md | 10 ++++++++++
 1 file changed, 10 insertions(+)
```

### E2 Bead acceptance

```text
$ bd show Praxis_build-zyd | sed -n '1,22p'
○ Praxis_build-zyd · b2 backtest fill-resolution: pin the intrabar fill/bar-resolution assumption BEFORE running the 4uu Strategy Analyzer backtest   [● P1 · OPEN]
Owner: Amear Bani-Ahmad · Type: task
Created: 2026-07-25 · Updated: 2026-07-25

DESCRIPTION

  GATE raised 2026-07-25 by the Claude.ai master/scoping agent. The Noise-Area
  breakout enters on band-touch and exits on opposite-band/VWAP — both        
  INTRABAR events. Decided data is NT8 default-provider MINUTE bars (D-2026-  
  07-15-B Q4) with $2.96 RT + 1-tick-slippage High fill (Q5). On minute bars  
  the NT8 Strategy Analyzer must ASSUME an intrabar High-vs-Low touch order;  
  for an intrabar entry+exit strategy that assumption can flip P&L sign.      
  UNRESOLVED: is minute resolution + a defined fill assumption adequate, or   
  does 4uu need tick/second data or an explicit intrabar-fill rule?           
  ACCEPTANCE: a written decision (DECISIONS.md) fixing (a) bar/data resolution
  for the backtest, (b) the intrabar fill assumption NT8 will use, (c) why    
  that does not bias the entry/exit of THIS strategy. Master-agent rationale: 
  'a backtest built on the wrong fill resolution, feeding SHM thresholds never
  checked against the breakers that will truncate them, is worse than no      
  backtest — it produces a number you will believe.' BLOCKS 4uu.              


```

### E3 Config diff (cached), JSON parse, arithmetic, key set

```text
$ git diff --cached config/backtest-cost-model.json
diff --git a/config/backtest-cost-model.json b/config/backtest-cost-model.json
index 38dc268..6fdd9eb 100644
--- a/config/backtest-cost-model.json
+++ b/config/backtest-cost-model.json
@@ -1,8 +1,9 @@
 {
-  "$schema_note": "PRAXIS Block-2 backtest cost + instrument model. Single source of truth consumed by BOTH the NT8 Strategy Analyzer (VM) backtest config and the Python (Mac) Monte Carlo layer. Encodes trader-locked decision D-2026-07-15-B (Q5). Do NOT hand-edit numbers without a corresponding DECISIONS.md entry.",
-  "version": "1.0.0",
+  "$schema_note": "PRAXIS Block-2 backtest cost + instrument model. Single source of truth consumed by BOTH the NT8 Strategy Analyzer (VM) backtest config and the Python (Mac) Monte Carlo layer. Encodes trader-locked decision D-2026-07-15-B (Q5). Do NOT hand-edit numbers without a corresponding DECISIONS.md entry. v1.1.0 number changes are authorised by DECISIONS.md D-2026-10-30-A.",
+  "version": "1.1.0",
   "created": "2026-07-15",
-  "decision_ref": "DECISIONS.md D-2026-07-15-B (Q5)",
+  "amended": "2026-10-30",
+  "decision_ref": "DECISIONS.md D-2026-07-15-B (Q5); amended by D-2026-10-30-A (slippage + fill resolution)",
   "bead": "Praxis_build-hlw",
   "instrument": {
     "symbol": "NQ",
@@ -18,15 +19,15 @@
     "commission_round_turn_usd": 2.96,
     "commission_basis": "round_turn",
     "commission_note": "Applied once per completed round-turn (entry+exit) per contract. If the backtest engine expresses commission per-side, use 1.48 USD/side.",
-    "slippage_ticks_per_side": 1,
-    "slippage_usd_per_side": 5.0,
-    "slippage_round_turn_ticks": 2,
-    "slippage_round_turn_usd": 10.0,
-    "fill_resolution": "High",
-    "fill_resolution_note": "NT8 Strategy Analyzer 'Order fill resolution' = High (intrabar sub-bar granularity for stop/target/entry fills; reduces optimistic same-bar fill artifacts). Python MC assumes fills already reflect this via the exported NT8 trade list.",
-    "total_cost_per_round_turn_usd": 12.96,
-    "total_cost_per_round_turn_ticks": 2.592,
-    "total_cost_breakdown_note": "12.96 = 2.96 commission + 10.00 slippage (2 ticks x 5.00). In ticks: 0.592 commission-equivalent + 2.0 slippage = 2.592 ticks round-turn."
+    "slippage_ticks_per_side": 2,
+    "slippage_usd_per_side": 10.0,
+    "slippage_round_turn_ticks": 4,
+    "slippage_round_turn_usd": 20.0,
+    "fill_resolution": "Standard",
+    "fill_resolution_note": "NT8 Strategy Analyzer 'Order fill resolution' = Standard on 1-minute bars (no secondary series). Every strategy order is a managed Enter*/Exit* call with no price argument, evaluated OnBarClose at HH:00/HH:30 checkpoints or on any bar with minute-of-day >= 16:00 for FlatEOD, plus the platform session-close exit (IsExitOnSessionCloseStrategy, clock-triggered, INFERRED) (no Set*/Submit*/limit/stop call — OBSERVED in code). That NT8 realises these calls as market orders, so intrabar High/Low ordering does not decide, at a checkpoint with a given position state, whether an order is sent, is INFERRED; 3gm D4 hypothesis 5 (INFERRED) holds that fill resolution could still change how same-bar exit+reverse pairs and the 16:00 orders resolve; via position state (3gm D4 hypothesis 2, INFERRED) that could change which later entries fire. Fill assumed at the next bar's open (INFERRED). CONDITIONAL under the void clause of DECISION_LOG 2026-08-29T00:10:00Z. Proposed limitation wording for backtest reports: 'Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.' Python MC assumes fills already reflect this via the exported NT8 trade list. See DECISIONS.md D-2026-10-30-A.",
+    "total_cost_per_round_turn_usd": 22.96,
+    "total_cost_per_round_turn_ticks": 4.592,
+    "total_cost_breakdown_note": "22.96 = 2.96 commission + 20.00 slippage (4 ticks x 5.00). In ticks: 0.592 commission-equivalent + 4.0 slippage = 4.592 ticks round-turn."
   },
   "applies_to": [
     "All P&L distributions (NT8 WFA fills + Python Monte Carlo)",
$ python3 -I -m json.tool config/backtest-cost-model.json | head -3
{
    "$schema_note": "PRAXIS Block-2 backtest cost + instrument model. Single source of truth consumed by BOTH the NT8 Strategy Analyzer (VM) backtest config and the Python (Mac) Monte Carlo layer. Encodes trader-locked decision D-2026-07-15-B (Q5). Do NOT hand-edit numbers without a corresponding DECISIONS.md entry. v1.1.0 number changes are authorised by DECISIONS.md D-2026-10-30-A.",
    "version": "1.1.0",
$ python3 -c "print(2*5.0, 4*5.0, 2.96+20.0, 2.96/5.0+4.0)"
10.0 20.0 22.96 4.592
$ (key-set diff HEAD vs worktree, commission + totals)
removed set() added {'amended'}
commission 2.96 sum_ok True ticks_ok True
```

### E4 DECISIONS.md diff (cached) in full, corrected deletion count, HEAD hash on lines 1-243

```text
$ git diff --cached DECISIONS.md
diff --git a/DECISIONS.md b/DECISIONS.md
index c5ceb36..e93c909 100644
--- a/DECISIONS.md
+++ b/DECISIONS.md
@@ -241,3 +241,57 @@ Q1 was closed session 14 (re-implement in NT8, D 21:10Z). The remaining Block-2
 **Note on prior verbal approval:** the coworker's report that the trader verbally approved volume-only in the VM was NOT sufficient to authorize the change — a roll-convention deviation requires an in-ledger, append-only DECISIONS entry. This entry supplies it; the earlier verbal is now formalized here, not relied upon.
 
 **Unblocks:** Praxis_build-6bw real-data validate+run (in volume-only mode, once raw/ is fully populated) → NT8 re-import → 4uu reconcile → zi1 (WFA) → ajj (MC) → xdr (refdist).
+
+---
+
+## 2026-10-30 — D-2026-10-30-A: F3 backtest fill resolution (CONDITIONAL, void clause live) + band-edge slippage [N] = 2 ticks/side (locked by Amear); amends D-2026-07-15-B Q5 slippage/fill terms
+
+**Date:** 2026-10-30
+**Status:** CONDITIONAL — in the form ruled by Amear at DECISION_LOG 2026-08-29T00:10:00Z, void clause live (see below); the commit is Amear's; [N] = 2 ticks/side LOCKED by Amear at 2026-10-30T21:36:30Z, reaffirmed at 2026-10-30T22:22:00Z (WHO: amear).
+**Addresses (for audit; not a grade):** rubric F3's written-assumption requirement (`specs/SPEC_RUBRIC.md:45-57`) and bead Praxis_build-zyd acceptance (a)(b)(c). Whether it satisfies F3 — including "before the backtest runs" — is Amear's (NEEDS AMEAR 2).
+**Bead:** Praxis_build-zyd (P1).
+
+**Context:** D-2026-07-15-B Q5 locked "1 tick/side slippage + High fill resolution". DECISION_LOG `2026-08-29T00:10:00Z` ruled a conditional form with `[N]` unfilled and a void clause. `2026-08-29T00:35:00Z` recorded that the strategy's order is a market order submitted OnBarClose at a semi-hourly stamp and filled at the next bar's open (INFERRED per 3gm D2(a) `:710`), so the touch-triggered / stop-cluster adverse-selection premise does not apply. `2026-10-30T21:36:30Z` set `[N]` = 2 ticks per side; `2026-10-30T22:22:00Z` (WHO: amear) kept `[N]` at 2 after run 4.
+
+**Decision:**
+- **(a) Bar / data resolution:** 1-minute bars of `NQCONT`, the Python-stitched continuous series (volume-only crossover roll + Difference back-adjustment, D-2026-07-17-A / D-2026-07-21-A), END-STAMPED (INFERRED by Claude from the import file's row counts, notes `:25`; Amear's NT8 read of the 9:31/9:32 Opens REPORTED, notes `:23`; bar-time check PASS 2026-10-30, `docs/reports/2026-10-28-voice-session-notes.md:22-27`, a file untracked in git). Import file `~/praxis-signals/b2-data/NQ-continuous-1min.nt8import.txt` (OBSERVED): first row `20210307 180100`, last row `20260720 112700`, 1,857,362 lines. Run-4 range 2021-03-08 → 2026-07-17 (REPORTED). No tick or second series.
+- **(b) Intrabar fill assumption:** Strategy Analyzer `Order fill resolution` = **Standard**, set explicitly (explicitness REPORTED BY AMEAR, `2026-10-30T21:36:30Z`; the value OBSERVED on the run-3 screenshot as "Standard (Fastest)", `2026-10-30T22:17:00Z`; REPORTED for run 4). No secondary / 1-tick series. Slippage **2 ticks per side** ($10/side; 4 ticks / $20 round turn) on top of the unchanged $2.96 RT commission = **$22.96 / 4.592 ticks per round turn**. Dollar figures assume NQCONT honours the $20 point value / $5 tick, which 3gm `:949` records as UNVERIFIED. Fill is assumed at the next bar's open after the signal bar — INFERRED, not observed. Whether NT8 applies the 2 ticks on every market fill is UNCONFIRMED (`2026-10-30T22:22:00Z` (WHO: amear)).
+- **(c) Why the fill-resolution choice does not decide the checkpoint order logic of this strategy, and where it may still bias the backtest:** the bead's premise ("enters on band-touch … INTRABAR events") does not match the code. `ninjascript/PraxisNoiseAreaBreakout.cs` (sha256 35393823…2752265, commit 719ab11) has six order call sites — `:211` ExitLong("XL",""), `:219` ExitShort("XS",""), `:227` EnterLong(Contracts,"L"), `:229` EnterShort(Contracts,"S"), `:288` ExitLong("FlatEOD",""), `:290` ExitShort("FlatEOD","") — each a managed Enter*/Exit* call with no price argument — plus (`:108`) IsExitOnSessionCloseStrategy = true — platform session-close exit, clock-triggered (INFERRED); no Set*/Submit*/limit/stop call exists; entry and checkpoint-exit decisions (`:211`, `:219`, `:227`, `:229`) are evaluated only at HH:00/HH:30 checkpoint bars (`:196-198`); the FlatEOD exits (`:288`, `:290`) run on any bar with mod >= CloseMod (`:189`), a clock condition, not a price touch. Calculate.OnBarClose is set at `:105` and the decision price is Close[0] at `:200` (code OBSERVED; OnBarClose runtime semantics INFERRED per 3gm Audit-1 §5 `:1164-1173`). Sources: 3gm D3 `:737-773`, Audit-1 §5 `:1164-1173`, §7 `:1185-1207`, D2 `:688-735`. No Set*/Submit*/limit/stop call exists (OBSERVED); assuming the Enter*/Exit* calls are market orders (INFERRED), there is no resting or touch-triggered order, so Standard's intrabar High-vs-Low ordering assumption would not decide, at a checkpoint with a given position state, whether an entry or exit order is sent. That NT8 realises these calls as market orders — and therefore that the Analyzer never needs the intrabar path — is INFERRED. A falsifier for this argument was proposed and is open, not run: the R3 Standard-vs-High control (DECISION_LOG 2026-08-29T00:40:00Z; a High run would also bear on the void clause). Its disposition is Amear's. Contrary hypothesis on record, not resolved: 3gm D4 hypothesis 5 (`:784`, INFERRED) holds that Order fill resolution High vs Standard could change how same-bar exit+reverse pairs and the 16:00 orders resolve. So the fill-resolution choice may still bias how NT8 fills those two cases. Because order decisions read position state (`Position.MarketPosition` at `:201`, `:226`, `:228`, `:287`, `:289`, OBSERVED, 3gm Audit-1 §1 `:1032-1083`), a different resolution of those fills would change later position state and, through it, which later entries fire (3gm `:781`, `:784`, INFERRED — fill resolution is listed among the candidate causes of the run-1 vs run-2 trade-count difference). (c) therefore holds only for the checkpoint decision given a position state, not for the trade set as a whole. This entry does not establish the bead's (c) in full; the R3 control (NEEDS AMEAR 5) is what would settle it. This is NOT a claim that the backtest is unbiased overall. Residual risks that remain. Only the first is a slippage item; the master's note in row 2026-10-30T21:36:30Z (INFERRED from source, pending 3gm) says 2 ticks prices stamp-to-next-open slippage; Amear's own framing (2026-08-29T00:10:00Z) was stop-cluster adverse selection, and 2026-08-29T00:35:00Z surfaced the mismatch without his re-ruling; no row says it prices the others:
+  - stamp-to-next-open slippage (not touch adverse selection; `2026-08-29T00:35:00Z`);
+  - the 16:00 FlatEOD fill path, whose "next bar" may be the next day's 09:31 (CANNOT-DETERMINE-STATICALLY, INFERRED; 3gm D2(c)) — fill resolution may bear on this (3gm `:784`, INFERRED);
+  - same-bar exit+reverse resolution (CANNOT-DETERMINE-STATICALLY, INFERRED) — fill resolution may bear on this (3gm `:784`, INFERRED); early-close days (CANNOT-DETERMINE-STATICALLY, INFERRED).
+- **Pre-commitment:** `[N]` was chosen 2026-10-28, before any backtest output existed (REPORTED; first Analyzer run 2026-10-30; rows `2026-08-29T00:10:00Z`, `2026-10-30T21:36:30Z`). A later 3-tick stress run is ALLOWED and does not change the locked number.
+- **Void clause (VERBATIM, DECISION_LOG `2026-08-29T00:10:00Z`):** *"We accept Standard resolution on 1-minute bars. Band-edge slippage widened to [N]. Fills are optimistic and the report states so. If the VM measurement shows NT8 errors or demands a secondary series rather than falling back silently, this row is void and the assumption is re-decided cold."* **Status:** NOT triggered and NOT retired (`2026-10-30T21:36:30Z`, REPORTED BY AMEAR: Standard was set explicitly in Analyzer template "Praxis Backtest", so the High-with-no-tick-data fallback was never exercised; no run has set High). The clause's trigger is "the VM measurement"; the ledger records only that no run has set High (REPORTED BY AMEAR, 2026-10-30T21:36:30Z). Whether a High run is the trigger is Amear's.
+- **Limitation sentence — PROPOSED wording, not ruled by Amear (his ruled requirement is only "Fills are optimistic and the report states so", 2026-08-29T00:10:00Z):** `Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.`
+
+**Rationale:** Amear's ruling, ledgered. Standard on 1-minute bars was accepted in the `00:10:00Z` conditional; `[N]` = 2 was set by Amear at `21:36:30Z` and reaffirmed at `2026-10-30T22:22:00Z` (WHO: amear). The master does not assert 2 ticks is correct (`21:36:30Z`); this entry does not either.
+
+**Authorisation chain (S5 — the ledger rows are the authorisation):** DECISION_LOG `2026-08-29T00:10:00Z` → `2026-08-29T00:35:00Z` → `2026-08-29T00:40:00Z` (R3 control proposed; open) → `2026-10-30T21:36:00Z` (WHO: amear; intake of the rulings) → `2026-10-30T21:36:30Z` → `2026-10-30T22:22:00Z` (WHO: amear) (`[N]` stays 2) → `2026-10-30T22:28:00Z` (dispatch).
+
+**Config pointer:** this entry IS the DECISIONS.md entry that `config/backtest-cost-model.json`'s `$schema_note` requires for the v1.1.0 number change.
+
+**Scope of change (explicit):**
+- `config/backtest-cost-model.json` → v1.1.0: slippage 1 → 2 ticks/side ($5 → $10/side; 2 → 4 ticks / $10 → $20 RT); `fill_resolution` High → Standard; total $12.96 / 2.592 ticks → $22.96 / 4.592 ticks RT.
+- Added key `amended: 2026-10-30`; `$schema_note`, `decision_ref`, `fill_resolution_note` and `total_cost_breakdown_note` text updated. No key removed.
+- Commission ($2.96 RT), instrument block, `applies_to`, `bead`, `created` unchanged.
+
+**S6 cross-block — consumers and what changes for each:**
+- All P&L distributions (NT8 WFA fills + Python Monte Carlo): now carry $22.96 RT.
+- R-multiple conversion (Q6): the new $22.96 RT cost is deducted before R normalisation.
+- All SHM distributions and threshold derivations (D-2026-07-04-B): derive from the 2-tick base. SHM-4 (`docs/specs/STRATEGY_HEALTH_MONITOR_SPEC.md:48-51`) includes slippage in its metric; its band numbers live in D-2026-07-15-B Q9 — see NEEDS AMEAR (1).
+- Rubric O4 Block-4 gate (`specs/SPEC_RUBRIC.md:94-99`, ±15% win rate / ±25% average trade P&L): compares live to a 2-tick backtest.
+- Analyzer template "Praxis Backtest": already at Slippage 2 / Standard (REPORTED); no change.
+- Spec text still carrying the superseded Q5 terms (not edited here; superseded on slippage and fill resolution by this entry): `docs/specs/2026-07-15-block2-backtesting-scope-proposal.md:129` ("High fill res, 1-tick series, 1-tick slippage", attributed there to the Phase 3 Build Spec) and `docs/specs/2026-07-15-b2-data-acquisition-spec.md:53` ("Q5, 1 tick/side" and "the High-resolution intrabar path").
+- F4 (MFFU automation compliance): `docs/reports/2026-08-07-f4-mffu-compliance-evidence.md` §4 (`:151`) couples MFFU restriction 2 (no automated tools built to exploit sim-environment fill favorability, `:45`) to F3's optimistic-fill failure mode. Named, not resolved; F4's disposition is Amear's.
+
+**NEEDS AMEAR (questions only):**
+1. Is SHM-4's "slippage >2 ticks/side worse" band (D-2026-07-15-B Q9) re-read against the new 2-tick base?
+2. `[N]` was chosen 2026-10-28 (REPORTED); its first ledger writing is the `2026-10-30T21:36:00Z` (WHO: amear) intake row, restated at `2026-10-30T21:36:30Z`, both after runs 1–3 had run; this entry is written after run 4 (REPORTED). Does that satisfy F3's "stated in writing before the backtest runs"?
+3. Readback, open from `2026-10-30T22:22:00Z` (WHO: amear) (not a decision): does NT8 apply Slippage 2 on every market fill, and what is the unit of the Summary's "Total slippage" cell?
+4. Approve or replace the proposed limitation sentence.
+5. The R3 Standard-vs-High control proposed at 2026-08-29T00:40:00Z is open. Is it run before F3 is graded, or does (c) stand as INFERRED?
+6. Scope of the `[N]` lock (3gm `:949`, reserved for Amear): row `2026-10-30T21:36:30Z` sets `[N]` as band-edge slippage and states it per round trip ($22.96); the Analyzer's Slippage setting applies to every market fill (INFERRED). Was the lock meant to cover session-close and stop-out exits as well?
+
+**Supersedes:** D-2026-07-15-B Q5's "1 tick/side slippage" and "High fill resolution" terms ONLY. Q5's $2.96 round-turn commission and "Applies to ALL P&L / SHM distributions" stand. D-2026-07-15-B's text is not edited.
+
+**Unblocks:** audit of this artifact under Praxis_build-zyd; closure is not decided here (NEEDS AMEAR 5 bears on it). F3's unblock condition also requires the backtest report to carry the assumption as a stated limitation (`specs/SPEC_RUBRIC.md:55-56`); the wording is Amear's (NEEDS AMEAR 4); this entry does not do that.
$ git diff --cached DECISIONS.md | grep '^-' | grep -vc '^---'    # corrected deletion count (the earlier '^-[^-]' form is blind to deleted '- ' bullets)
0
$ head -n 243 DECISIONS.md | shasum -a 256 ; git show HEAD:DECISIONS.md | shasum -a 256 ; git show HEAD:DECISIONS.md | wc -l
a0c8fbeea8dcafd72f7385c2b1c50594a6cf7349c8bd49032531cb4491d5234a  -
a0c8fbeea8dcafd72f7385c2b1c50594a6cf7349c8bd49032531cb4491d5234a  -
     243
```

### E5 Void clause byte check (DECISION_LOG row 2026-08-29T00

```text
$ python3 -I scratchpad/mgr_vc.py DECISIONS.md      # void clause: DECISION_LOG row 2026-08-29T00:10:00Z vs entry
True f9144cb50aab2885 f9144cb50aab2885
```

### E7 Negative arms (void-clause mutation; cost-sum mutation)

```text
$ python3 -I scratchpad/mgr_vc.py DECISIONS.md      # void clause: DECISION_LOG row 2026-08-29T00:10:00Z vs entry
True f9144cb50aab2885 f9144cb50aab2885
$ (negative arm: same check on a copy with "re-decided cold" -> "re-decided anew")
AttributeError: 'NoneType' object has no attribute 'group'
$ (negative arm: total_cost set to 22.95 in memory)
sum_ok False
```

### E7b Positive arm

```text
$ git diff --no-index old.md new.md (one '- ' bullet deleted)  | grep -c '^-[^-]'  vs  grep '^-' | grep -vc '^---'
0
1
```

### E8 Source checks for the manager's single-line edits and for cited facts

```text
$ sed -n '129p' docs/specs/2026-07-15-block2-backtesting-scope-proposal.md | grep -c -F 'High fill res, 1-tick series, 1-tick slippage'
1
$ sed -n '53p' docs/specs/2026-07-15-b2-data-acquisition-spec.md | grep -c -F -e 'Q5, 1 tick/side' ; ... -F 'the High-resolution intrabar path'
1
1
$ sed -n '780,781p;784p' docs/reports/2026-10-30-3gm-fidelity-check.md | cut -c1-140
1. **Trading-hours template** was not CME US Index Futures RTH in run 1 (`<Use instrument settings>`, ETH, or 24×7). That moves `IsFirstBar
2. **Exit on session close** or **Time in force** differed. Both are Analyzer-editable, and they decide D2(c). A position carried overnight 
5. **Order fill resolution** High vs Standard. This could change how same-bar exit+reverse pairs and the 16:00 orders resolve.
$ sed -n '48,51p' docs/specs/STRATEGY_HEALTH_MONITOR_SPEC.md | cut -c1-60
### SHM-4 — Live-vs-Backtest Divergence
- **Metric:** Per-trade comparison of live fills against the
- **Trigger:** Divergence beyond [T.B.D] on a rolling 20-trade
- **Interpretation:** Distinguishes "edge is dying" from "ex
$ sed -n '442p' DECISION_LOG.md | grep -o -F 'set EXPLICITLY'
set EXPLICITLY
$ awk '/D-2026-10-30-A: F3/{f=1} f' DECISIONS.md | grep -c -F ':780'
0
$ sed -n '441p' DECISION_LOG.md | grep -o -E '.{0,30}2 ticks per side.{0,40}'
nvestigated. (3) F3 `[N]` = **2 ticks per side** — recorded in its own row below. (4
$ ~/praxis-signals/b2-data/NQ-continuous-1min.nt8import.txt: head -1 / tail -1 / wc -l
20210307 180100;16120.5;16167;16120.5;16154.75;17
20260720 112700;29005.5;29020.75;29003.5;29016;308
 1857362
$ shasum -a 256 ninjascript/PraxisNoiseAreaBreakout.cs ; git log -1 --format=%h -- ninjascript/PraxisNoiseAreaBreakout.cs
35393823e9bc146e95dcb1d9f6fe5785a3c72ee3a3fb71287f33fe2242752265  ninjascript/PraxisNoiseAreaBreakout.cs
719ab11
$ grep -n -E 'Enter(Long|Short)|Exit(Long|Short)|Set[A-Z][a-zA-Z]*\(|Submit|Calculate\s*=' ninjascript/PraxisNoiseAreaBreakout.cs
105:				Calculate                                 = Calculate.OnBarClose;
211:					ExitLong("XL", "");
219:					ExitShort("XS", "");
224:			//     EnterLong while short closes the short and goes long). Position.MarketPosition here is
225:			//     the pre-fill state, so an ExitLong above followed by Close<Lower still reverses correctly.
227:				EnterLong(Contracts, "L");       // long breakout / reverse-to-long (spec §2)
229:				EnterShort(Contracts, "S");      // short breakout / reverse-to-short (spec §2)
288:				ExitLong("FlatEOD", "");
290:				ExitShort("FlatEOD", "");
$ git ls-files docs/reports/2026-10-28-voice-session-notes.md | wc -l
       0
```

### E9 MANIFEST diff (cached) in full, tail, deletion count, stat

```text
$ git diff --cached MANIFEST.md   # first 15 + rows are other units' pre-staged rows; this unit's 21 rows follow
diff --git a/MANIFEST.md b/MANIFEST.md
index b09de40..8fd675a 100644
--- a/MANIFEST.md
+++ b/MANIFEST.md
@@ -115,3 +115,39 @@
 | /specs/SPEC_RUBRIC.md | Spec | 0 | 2026-07-25 | Grading rubric every dispatch is scored against. Per-block criteria + standing criteria S1-S11 (S1 pasted output not descriptions; S2 specified≠implemented≠tested≠tested-under-failure; S3 every gate deliberately tripped; S4 deviations logged before the work; S5 the ledger append IS the authorisation; S6 cross-block — the one that failed, six deviations approved in isolation broke four downstream components; S7 nothing committed with an audit box unchecked; S8 no question of Amear's answered on his behalf; S9 positive control on any config field a guarantee depends on — PENDING Amear's ratification, transcribed from the brief's standing rule 5; S10 Agent(<type>) narrowing is not a scoping mechanism; S11 nesting is depth-capped at master→manager→worker). Session-33 rulings appended: R2 amendment to S10 (allowlist dead as a RESTRICTION, live as a GRANT — the inherited parent roster is load-bearing for reachability, so praxis-worker must NOT be removed from praxis-master's allowlist) and R3 note under S9 (positive control extends to claims about MECHANISM, not only config keys; cites session 33's three-assumption chain) |
 | /specs/SPEC_RUBRIC.md | Spec | 0 | 2026-07-26 | AMENDMENT ROW (append-only registry — supersedes the description in the earlier row for this path). Session-33 flush commit adds: S12 (a ledger writer ships with its closing/flushing counterpart in the same change; violations named = scripts/dispatch-log-writeahead.sh, which writes `STATE: dispatched` rows that no SubagentStop hook ever closes — the sole SubagentStop registration is gate-manager-output.sh, an output gate — and AUDIT_LOG mint rows, stranded by construction since audit-approve.sh appends after the staged diff is hashed; neither repaired). REPLACES the S9 note's cited triple: the reconstructed three-assumption chain is withdrawn in favour of the orchestrator's three UNOBSERVED ASSERTIONS about agent-spawn-guard.sh (registered globally -> false, project-scoped; fails safe as deny -> false, fails open; T6+T7 both depend on it -> false, T6 solely), per 2026-07-26 human ruling. ADDS a "Process rulings" section: the park rule is now ABSOLUTE — on audit-fail-x2 the orchestrator commits to parked/<bead>, fires notify.sh, ENDS THE SESSION, and only a human resumes; supersedes orchestrator-mine v3's "park it blocked, move on", with the DECISION_LOG 17:55Z deviation row standing unedited as the record. The global skill file still carries the weaker wording and is deliberately NOT edited from this repo |
 | /specs/SPEC_RUBRIC.md | Spec | 0 | 2026-07-26 | AMENDMENT ROW 2 (append-only registry — supersedes both earlier rows for this path). Session-33 flush #2 adds three Process rulings: (a) DECISION_LOG row schema splits `WHO:` into `PROPOSED BY:` / `APPROVED BY:`, effective 2026-07-26 FORWARD with no retro-edit, Praxis (claude.ai scoping agent) recorded as proposer and Amear as approver for rulings originating with Praxis — carrying the explicit caveat that this is LEGIBILITY not verification (an orchestrator can author either field; threat model is DRIFT, not forgery; S4/S5 remain the only authorisation control and are records, not proofs); (b) absolutes are amended BETWEEN SESSIONS ONLY — hit an absolute, park, amend cold, by a human, in an unblocked session, citing the SHM pre-commitment precedent (STRATEGY_HEALTH_MONITOR_SPEC.md section 2, no threshold adjusted while in drawdown, 5-day cooling period, "the decision 'is the edge dead or am I scared' is never made live"), and NAMING the e785ca4 park-rule amendment as an instance of what it now forbids rather than exempting it; (c) Praxis_build-t83 approved as convention — flush commits name every carried AUDIT_LOG row's bead id in the subject line, because the grep test returned nothing for the lnb+nj1 row at e785ca4 and the auditor had to map it by timestamp window |
+| /docs/reports/2026-07-26-session36-agent-key-s9-control.md | Report | 0 | 2026-07-26 | HIGHEST-STANDING SESSION-36 ARTEFACT and the record of the session's one established finding — praxis-manager's S9 positive control on the root `"agent"` key in `.claude/settings.json`, verdict DECISIVE POSITIVE, re-run directly by the manager rather than accepted on worker report (§3 records worker 4's finding as re-run by the manager directly, per §6, and not accepted on report — paraphrase, not a quotation). Two-arm control in a lab replica, `--agent` never passed in either arm, `.claude/agents/praxis-master.md` present in BOTH arms (the precondition the earlier lab omitted): ARM X first root key `agent` → dumped payload, reproduced from the source bytes at report line 96 rather than re-rendered: `{"agent_type_present":true,"agent_type":"praxis-master","agent_id_present":false,"cmd":"echo hello > …/probeX.txt"}` (the `…` is the report's own elision), real `scripts/master-bash-guard.sh` denied 3x with the verbatim string "BLOCKED: shell write from praxis-master. Use Edit on a ledger, or dispatch a worker.", probe file never created; ARM Y identical position and value with the key renamed `zzz_bogus_agent_key` → `agent_type` absent, 0 BLOCKED, probe file written. Both halves of S9 discharged, and ARM Y's silence is informative ONLY because a content-independent liveness hook (`HOOK_RAN`) fired in both arms and stream-line counts (10 vs 11, empty stderr) rule out TRUNCATION — a separate failure mode that looks identical to a hook that never fired. Three distinct things, not one: the task's only SIGPIPE is a `head -c` recorded in /docs/reports/2026-07-26-session36-adversarial-actor-hunt.md §4.4, and it produced a truncated transcript, not a null; the task's two ACTUAL false nulls (§7.4, "Two of the four workers hit a false null in this one task") came from worker 3's unresolvable agent name (§7.1) and from macOS having no `timeout` binary (/docs/reports/2026-07-26-session36-null-attack.md §8.3). FINDING: the key IS a mechanism that sets `agent_type` in PreToolUse payloads on CC 2.1.220 (version verified in-session), CONDITIONAL on the name resolving to an existing `.claude/agents/<name>.md`; a missing definition makes the key a silent no-op — no warning, no stderr, exit 0. Supersedes the confounded null in /docs/reports/2026-07-26-session36-agent-key-lab.md and adopts the refutation in /docs/reports/2026-07-26-session36-null-attack.md. S2 CAVEAT CARRIED, NOT DISCHARGED (§12, "Scope caveat (S2)" — §7 is Adversarial findings): shown in a lab replica with cwd OUTSIDE the repo plus read-only confirmation that the repo holds both halves; behaviour in the repo's own directory is INFERRED, never directly observed, because CLAUDE.md:30 forbids a second session against this tree — closing it needs a human session or a `git worktree`. `master-write-guard.sh` armed by the same field was NOT separately re-tripped by THIS control (§9 verbatim: "Confirmed by reading, **not** separately trip-tested") — that is a statement about this control run's scope, NOT the guard's overall level: the guard is separately trip-tested live on Edit and Write (/docs/reports/2026-07-26-agent-stack-v2-triptests.md:54, :128, verdict :142) and S9 invented-key-controlled at script level (/docs/reports/2026-07-26-session34-manifest-amendment.md:198-206). Repo settings sha256 unchanged (eed25e67…), staged diff still `1 0`, nothing staged by the task; §10 flags `.claude/agent-memory/praxis-worker/project_agent-type-source.md` as now-false guidance, deliberately not edited — that describes the REPORT'S state at time of writing, not current repo state: the memory was corrected later in session 36 and now opens "This file previously recorded the opposite claim. That claim is REFUTED." and agrees with this report |
+| /docs/reports/2026-07-26-session36-null-attack.md | Report | 0 | 2026-07-26 | ADVERSARIAL worker report that REFUTED the null result of /docs/reports/2026-07-26-session36-agent-key-lab.md — headline "RESULT: THE NULL IS FALSE. COUNTEREXAMPLE PRODUCED", result line "BREAK FOUND". Standing: a genuine break whose causal claim was independently re-run by praxis-manager before being relied on, so it is evidence of record rather than an unreviewed sub-report — but the authoritative write-up of the finding is /docs/reports/2026-07-26-session36-agent-key-s9-control.md, not this file. Twelve arms in a fresh lab, all payloads dumped raw and verbatim: arm 0 baseline `agent_type` genuinely absent; ARM 2 THE COUNTEREXAMPLE — project `.claude/settings.json` `"agent": "labmaster"` with NO `--agent` flag → `"agent_type":"labmaster"`; arms 3/4 unresolvable names (`ghostagent`; `praxis-master` with no definition in that lab) → absent, arm 4 exactly reproducing the earlier null AND explaining it; arms 8/9 the decisive A/B/A causal isolation — settings file byte-identical, the ONLY variable being whether `praxis-master.md` exists → absent then present, so toggled by a file and not by key spelling; arms 10/11 the chain run out to the real `master-bash-guard.sh` BLOCK; arms 6/7 the same key working from `.claude/settings.local.json` and from `--settings`, so the claimed flag-vs-settings asymmetry does not exist. Mechanism = key AND resolvable definition; an unresolvable name is dropped silently, which is the perfect null-manufacturing condition. The lead came from `claude --help` read in-session — "Overrides the 'agent' setting". Records the near-miss where macOS has no `timeout` binary, the first arm produced zero dumps, and only an independent liveness log stopped it reading as another confirming null. Own limits kept intact: real-repo behaviour INFERRED from the replica plus read-only config inspection, not observed (CLAUDE.md:30); user-level settings scope and the `agentType` / `defaultAgent` / `agent`-as-object spellings UNVERIFIED; malformed-but-present definitions never separated from absent ones |
+| /docs/reports/2026-07-26-session36-agent-key-audit.md | Report | 0 | 2026-07-26 | Cold praxis-auditor grade of the staged one-path index at HEAD c1dec30 — the `"agent": "praxis-master"` insert in `.claude/settings.json`, producer reasoning deliberately not read. AUTHORITATIVE AS AN AUDIT VERDICT: report line 5 verbatim — "**Result: FAIL** — S1, S2, S4, S5, S7, S9. No token minted." QUOTATION CONVENTION, this row: quotations reproduce the source bytes exactly, `**` emphasis preserved rather than stripped or added, and where a quote is cut from a line-wrapped source sentence the wrap is flagged. Nothing was edited, fixed, staged or committed by it, and `.claude/state/` carries no token. Independent checks that PASS and are credited: JSON valid (`jq` exit 0), `agent` purely additive at root position 0 with `env`/`hooks`/`permissions` byte-unchanged, column-0 indentation cosmetic and also a provenance tell, the 8sw report confirmed `??` and out of the index, and S4's timing sub-claim VERIFIED TRUE from pasted mtimes (ledger written 5s before the index). Fails: S1 — no producer report existed and the claim-bearing DECISION_LOG row describes rather than pastes, citing `git diff .claude/settings.json` (empty by construction, worktree-vs-index) for a staged-content claim only `git diff --cached` can establish; S5/S4 — the authorising 21:36Z row is neither staged nor in HEAD, so the commit would carry the act without the authorisation and against committed HANDOFF.md:5 and :18, with both PROPOSED BY and APPROVED BY filled from one transcribed verbal; S2 — the producer's "no guarantee here rests on the key" falsified by toggle, `master-bash-guard.sh` and `master-write-guard.sh` moving exit 0 → exit 2 on that field alone; S7 — 8sw at FAIL, Praxis_build-sk8 P1 open, 599885e disposition open, `parked/Praxis_build-37h` unresolved (the auditor itself marks S7 least clear-cut and does not rest the verdict on it). SUPERSEDED IN ONE PART ONLY, AND ONLY AT LAB LEVEL: its §1.4 "The positive control has not been run, by anyone" was true when written and is now discharged IN A LAB REPLICA by /docs/reports/2026-07-26-session36-agent-key-s9-control.md — §1.4 asked for "a live main-thread session with the key installed and a hook trip observed", while the control ran with cwd OUTSIDE the repo (its §12 scope caveat), so IN-REPO sufficiency remains the open spec question. Reported at the level the evidence supports: given a resolvable definition the key arms `master-bash-guard.sh`, which was TRIP-TESTED through the real hook path (ARM X denied 3x, probe file never created), while `master-write-guard.sh` keys on the same field and was not re-tripped by that control — s9-control §9 verbatim, "Confirmed by reading, **not** separately trip-tested", a hedge scoped to THAT control run (§9 contains no "never"). THE GUARD ITSELF IS TRIP-TESTED LIVE: PreToolUse denials naming scripts/master-write-guard.sh on Edit (/docs/reports/2026-07-26-agent-stack-v2-triptests.md:54) and on Write (:128, verdict :142, quoted as that line's leading fragment because the verdict sentence wraps onto :143 — "**PASS** — `master-write-guard.sh` fires on the `Write` tool"), armed in both by `--agent praxis-master`; plus a direct-stdin trip carrying the S9 invented-key control at /docs/reports/2026-07-26-session34-manifest-amendment.md:198-206 (`agent_type` exit 2 / 142 B stderr vs `agent_typeX` exit 0 / 0 B). CAVEAT CARRIED from triptests:61 — only the last hook to finish surfaces its message, so a live trip alone cannot show master-write-guard.sh was the ONLY denier; the session-34 stdin invocation is what makes attribution unambiguous — the source phrase is line-wrapped across session-34-manifest-amendment.md:163-164, so only the fragment that resolves on a single line is quoted, "no other hook was in", with "the path" carried onto :164. What session 36 did NOT separately re-test is whether the SETTINGS `agent` key, as opposed to the `--agent` flag, arms THIS guard — only `master-bash-guard.sh` was tripped through the key. Every other finding stands ungraded and unrepaired |
+| /docs/reports/2026-07-26-session36-agent-key-lab.md | Report | 0 | 2026-07-26 | SUPERSEDED INTERMEDIATE — worker sub-report (worker 3) whose headline result was REFUTED; it is NOT an authoritative finding and must be read only alongside /docs/reports/2026-07-26-session36-null-attack.md, which broke it, and /docs/reports/2026-07-26-session36-agent-key-s9-control.md, which replaces it. Its headline reads "NULL RESULT. The hypothesis is refuted by direct measurement" and its result line records "PASS" on what it calls a decisive negative answer; arms A (`"agent"`), B (`"zzz_bogus_agent_key"`) and C (key absent) came back indistinguishable on every measured dimension with `agent_type` absent in all three. THE NULL WAS CONFOUNDED: the lab held no `.claude/agents/praxis-master.md`, so the name could not resolve and the key was dropped silently — a state indistinguishable on disk from an ignored key. That defect was reproduced as arm 4 of the null-attack and broken by its arms 8/9 definition-file A/B/A, and the opposite result was then obtained in the manager's two-arm control. Its own limits item 1 named ONLY the directory difference (a different project directory, so the result "does not transfer automatically"); the confounder itself — the missing agent-definition file — is never mentioned in this report at all (grep for definition/resolve/praxis-master.md returns zero matches). The judgment that a hedge named "the confounder without recognizing it as one" belongs to /docs/reports/2026-07-26-session36-null-attack.md §8.4, where it is made about a different artefact and quotes a sentence that does not appear here. What survives is method, not conclusion: harness self-tests run BEFORE any arm, an arm-differs-only-in-key-name diff, and an ARM P wrapper control proving the second hooks-array entry executes and the real guard denies with the probe file uncreated. THIS REPORT'S OWN MECHANISM CONCLUSION IS FALSE AND MUST NOT BE CITED — and that falsity is scoped to the report. The memory derived from it, `.claude/agent-memory/praxis-worker/project_agent-type-source.md`, was CORRECTED later in session 36: it now opens "This file previously recorded the opposite claim. That claim is REFUTED." and agrees with /docs/reports/2026-07-26-session36-agent-key-s9-control.md, so it is current guidance to be read, not avoided. Also the first artefact to record the concurrent-index anomaly on the 8sw report path (staged at snapshot, untracked later, no index op run by it) |
+| /docs/reports/2026-07-26-session36-adversarial-actor-hunt.md | Report | 0 | 2026-07-26 | INTERMEDIATE WORKING ARTEFACT — adversarial worker sub-report (worker 2). NOT superseded as a finding: /docs/reports/2026-07-26-session36-agent-key-s9-control.md ADOPTED it rather than replacing it — that report's §5 rests one of its three "Observed, not inferred" bullets on worker 2's dumped payloads, and §7.5 credits it — and the question worker 2 answers is a different one, still unrefuted. Its lasting contributions are that finding plus the nested-`claude` harness the later control reused. Result line: FAIL (claim broken), "The claim's conclusion is falsified; its premise is not." Established live: a subagent's Bash tool CAN launch a nested main-thread session running as `praxis-master` whose PreToolUse dispatch executes the real `scripts/master-bash-guard.sh` (sha256 2dd67afc…) and emits the real BLOCKED string at exit 2 with `probeF.txt` never created, against a payload observed in the same dispatch to carry `agent_type == "praxis-master"` and NO `agent_id`; and the repo's own settings PreToolUse/Bash block does dispatch on subagent calls (`no-commit-guard.sh` fired on a free-text probe). NOT established, and the report says so: the attacked premise SURVIVED — every subagent shape it could build, depth-1 and depth-2 with `agent_type` exactly `praxis-master`, carried a non-empty 17-hex `agent_id` and produced byte-identical silence, which it records as "I could not find one", not "none exists"; it never observed its own payload; `--bg`, `--resume`/`--fork-session`, SDK/stream-json input and MCP-initiated calls untested; no run combined the real script WITH the repo's real registration; and the S9 second half was NOT run at config-key level — its Attack-D silences are field-VALUE controls, not invented-KEY controls. Attack E stopped rather than worked around, on CLAUDE.md:30. LEAVES AN OPEN SPEC-INTERPRETATION QUESTION FOR THE MASTER, unanswered here: whether an out-of-tree harness executing the real script under a real PreToolUse dispatch satisfies S9, or whether S9 demands the in-repo registration. Surprises recorded: hook denials surface as `"non_execution_kind":"permission-rule"` and fire even under `bypassPermissions`; `--settings` will execute a hook script outside the session's project dir, so the guard is not bound to the repo it lives in; a `head -c` SIGPIPE truncation looks exactly like "the hook never fired" |
+| /docs/reports/2026-07-26-session36-worker-trigger-probe.md | Report | 0 | 2026-07-26 | LOWEST-STANDING SESSION-36 ARTEFACT — purely observational worker sub-report (worker 1), four Bash probes with output pasted verbatim; NOT an authoritative finding about `agent_type` or about the settings key, and it makes no such claim. It answers one narrow question — did `scripts/master-bash-guard.sh` emit its BLOCKED string on this worker's calls — with NO: both write probes returned `exit=0`, no hook deny text, files written. ITS SILENCE IS UNINFORMATIVE BY CONSTRUCTION and the report disclaims it in its own scope note — the hook payload itself (`agent_id`, `agent_type`) was not captured in this probe, call 3 is shell environment only, and "Payload shape remains UNVERIFIED." (the full sentence is line-wrapped in the source, so only this fragment is quoted). THE PROBE'S OWN `agent_type` WAS NOT OBSERVED — not in this report, and worker 2 records the same limit of ITSELF ("I never observed **this** session's own PreToolUse payload."). Scoped to the dispatched workers' OWN payloads: worker-shaped payloads WERE captured in session 36 — s9-control §5 pastes worker 2's dumps of subagents it spawned whose `agent_type` was exactly `praxis-master`, each with a non-empty 17-hex `agent_id` (`a530cc121d2d37552`, `aea6ef2edb28e8096`), so what is missing is the capturing agent's own payload, not any subagent payload. The short-circuit that IS isolated is `scripts/master-bash-guard.sh:7`, `[ -n "$AGENT_ID" ] && exit 0`, which fires on the non-empty `agent_id` observed on every subagent shape examined and runs BEFORE the `agent_type` test on line 8 (s9-control §5). /docs/reports/2026-07-26-session36-agent-key-s9-control.md logs this probe as worker 1, "Guard silent, exit 0. Payload not observed", and that silence is ONE OF THREE "Observed, not inferred" observations behind the manager's refusal to run the briefed control on the real settings file — the refusal rests principally on worker 2's dumped payloads, not on this silence. Residual value is environmental, captured live and not inferred: `CLAUDE_CODE_VERSION=2.1.220 (Claude Code)`, `CLAUDE_CODE_CHILD_SESSION=1`, `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=2`, `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS=8`, session id `2488feec-…`, and a parent process of `claude --dangerously-skip-permissions` |
+| /scripts/dispatch-log-close.sh | Script | 0 | 2026-07-28 | Praxis_build-43n (S12 v1) SubagentStop counterpart to dispatch-log-writeahead.sh — the closing half S12 requires. APPEND-ONLY BY DESIGN: never edits an existing row, so "is this row closed?" is a JOIN on the `corr=` token, not a field read (tradeoff accepted so the mechanism never writes over the primary record). Correlation key `CORR_JQ='.agent_id // empty'`, BOUND AND CONFIRMED against real captured SubagentStart/SubagentStop payloads 2026-07-28 (identical `agent_id` on both events; `prompt_id`/`session_id` rejected as keys — concurrent spawns from one prompt share them). Always exits 0, so it can neither block a lifecycle nor mask another SubagentStop hook's deny. Degrades honestly rather than guessing: `closed@unattributed` (+`reason=`) when no token, `closed@unmatched-token` when the token matches no open row, and it reports `matched N open row(s)` rather than picking one when N>1. Token safety gate uses `case`, NOT `grep` — grep is line-oriented, so an embedded newline passes `grep -qE '^…$'` whenever its FIRST line is valid, which is exactly the hostile case; rejects charset violations, `\|`, spaces and >64-char tokens by degrading to UNKEYED. Log path overridable via `PRAXIS_DISPATCH_LOG` (line 51) so the script is testable without touching the real ledger; unset in the CLI process env, so in production it resolves to `$CLAUDE_PROJECT_DIR/DISPATCH_LOG.md`. **PROVEN LIVE IN PRODUCTION CONFIGURATION 2026-07-28T16:08:24Z and 16:12:20Z** — two genuine keyed closes appended to the real DISPATCH_LOG.md by the runtime firing the hook, no human involved (an earlier 15:49:07Z firing was real but `PRAXIS_DISPATCH_LOG`-REDIRECTED to a scratchpad fixture, and must not be cited as a real-ledger close). **KNOWN UNREPAIRED DEFECT, graded FAIL — do not treat this script as hardened:** `agent_type` is read raw at line 80 into `WHO: $AGENT` with NONE of the three gates applied to `agent_id`, so a hostile `agent_type` forges arbitrary rows AND, by planting a row carrying `corr=<victim>` plus `| STATE: closed`, makes the victim's genuine stop hit the idempotency gate — 0 honest closes, victim row left `STATE: dispatched` permanently and silently, the exact S12 failure this script exists to prevent. Reproduced independently by the manager; see /docs/reports/2026-07-28-session39-closer-negative-tests.md. Whether the runtime can itself emit such an `agent_type` is UNVERIFIED. NOT retroactive: the hook config in force for a stop appears to be the one bound AT SPAWN TIME (INFERRED from four firings, not confirmed), so rows from spawns predating registration never close |
+| /scripts/tests/test-dispatch-log-close.sh | Test | 0 | 2026-07-28 | Praxis_build-43n harness for dispatch-log-close.sh (verification cmd: `./scripts/tests/test-dispatch-log-close.sh`). 13 cases, all against TEMP fixtures — the real DISPATCH_LOG.md is never a test target, confirmed by sha256 before/after (byte-identical across an independent manager re-run and an independent master re-run). Covers: clean KEYED close + idempotency; UNKEYED close + idempotency for byte-identical repeat stdin; missing log file created; zero open rows with a token present; malformed/truncated row present; token matching no open row with the unrelated open row left untouched (append-only assertion); two open rows sharing one token → honest `matched 2`; jq absent from PATH → `reason=jq-missing`; empty stdin; non-JSON stdin. Exit 0 iff all pass. Verified 13 passed / 0 failed 2026-07-28. GAP THE HARNESS DOES NOT COVER, and the reason the unit was graded FAIL: no case exercises a hostile `agent_type`, which is the field carrying the unrepaired row-forgery and silent-close-suppression defect |
+| /scripts/dispatch-log-writeahead.sh | Script | 0 | 2026-07-28 | BACKFILL ROW — this pre-existing SubagentStart hook had NO MANIFEST row of any kind before 2026-07-28 (the only earlier mentions are inside the /specs/SPEC_RUBRIC.md rows naming it as S12 violation 1); registering it here closes that gap and records the same-day modification. Appends one DISPATCH_LOG.md row per spawn reading `HOW: awaiting terminal state | STATE: dispatched`. Praxis_build-43n change: adds `corr=<agent_id>` to the existing `WHERE:` field (7-column schema unchanged, so no consumer breaks — no component in this repo parses row structure), adds a `PRAXIS_DISPATCH_LOG` override for testability, and repairs a REAL PRE-EXISTING DEFECT found by the manager and missed by the build worker — the writer did not guarantee a trailing newline, so a row appended to a file lacking one FUSED two rows onto a single line. Its S12 counterpart is /scripts/dispatch-log-close.sh |
+| /docs/reports/2026-07-28-session39-dispatch-log-closer.md | Report | 0 | 2026-07-28 | AUTHORITATIVE manager report for Praxis_build-43n (S12 v1 closer), superseding both worker sub-reports below. Settles by CAPTURE, not inference, the previously-open question of whether SubagentStop carries a field correlating back to SubagentStart: YES, `agent_id`, with both raw payloads pasted verbatim. Resolved on resume: its own headline "real payload closes" is CORRECTED to distinguish a real-runtime-but-redirected firing (15:49:07Z, fixture) from real-ledger production closes (16:08:24Z / 16:12:20Z), the S2 distinction the brief demanded. Result: FAIL — S2 headline overclaim plus an unrepaired silent-close-suppression defect in the artifact; S1 and the append-only contract pass. Records that the manager authored production code itself (two rounds, the second unattacked) and that a worker breached its brief by naming a forbidden directory |
+| /docs/reports/2026-07-28-session39-dispatch-log-closer-build.md | Report | 0 | 2026-07-28 | BUILD worker sub-report (worker 1) for Praxis_build-43n — SUPERSEDED as a statement of the artifact's current state and NOT to be cited for the correlation key. Built the closer parameterised over an UNKNOWN correlation key, correctly labelling `.agent_id` a STATIC-READ guess from the installed binary because no SubagentStop payload existed yet; the manager's later capture confirmed the guess, but the guess is not the evidence. Its own `CORR_JQ` header comment ("UNBOUND PLACEHOLDER… nobody has observed an actual SubagentStop JSON payload") was true when written, false by ship time, and was rewritten by the manager. Missed the row-fusion defect in the writer |
+| /docs/reports/2026-07-28-session39-dispatch-log-closer-adversarial.md | Report | 0 | 2026-07-28 | ADVERSARIAL worker sub-report (worker 2) for Praxis_build-43n, round 1 — attacks 1-10 against the closer, of which 7-10 forced real repairs (token safety gate, boundary-anchored matching). SUPERSEDED IN COVERAGE by /docs/reports/2026-07-28-session39-closer-negative-tests.md, which broke the artifact on a field this round never probed. Its spawn/stop is also the physical driver of the 15:49:07Z redirected firing. Self-disclosed a literal brief breach: it named the forbidden `.claude/agent-memory/` path once, in a negative assertion that nothing was written there; it did not write there |
+| /docs/reports/2026-07-28-session39-live-vs-piped-attack.md | Report | 0 | 2026-07-28 | ADVERSARIAL grade of the closer's "real payload closes" headline against S2 and ruling G-2 (piped payload ≠ live end-to-end). Verdict: CLAIM OVERSTATED. Recovered VERBATIM from the manager transcript the hook registration in force at 15:49:07Z — `PRAXIS_DISPATCH_LOG=<scratchpad>/live-fixture/DISPATCH_LOG.md "$CLAUDE_PROJECT_DIR"/scripts/dispatch-log-close.sh` — proving that firing was runtime-driven but REDIRECTED, and ruled out all four alternative producers (sync-loop.sh structurally cannot write a closing row). Independently establishes that mid-session hook registration IS live in an already-running CLI process (PID 85132 started 15:04:26Z; four later firings) but is NOT retroactive — manager `a4914` stopped 2 minutes after the production entry was registered and produced no row. Observed the real-ledger close land mid-run at 16:08:24Z and correctly rated it a capability that arrived after, and is not, the demonstration the claim cited |
+| /docs/reports/2026-07-28-session39-closer-negative-tests.md | Report | 0 | 2026-07-28 | ADVERSARIAL negative-test battery against dispatch-log-close.sh — 25 invocations, all on scratch fixtures, real ledger sha unchanged. Verdict: CONTRACT VIOLATED, and the single most load-bearing artifact in the FAIL grade. CONFIRMS what holds: append-only across 25/25 runs (first-N-bytes sha256 identical, including the no-trailing-newline fusion case), exit 0 on every branch, honest `closed@unmatched-token` / `closed@unattributed` degradation, idempotent 0-byte repeats, honest `matched 2` under ambiguity, and an `agent_id` gate that resisted newline, pipe, `.*` and 5000-char tokens. BREAKS IT on `agent_type`, which bypasses all three of those gates: row forgery, plus a silent denial-of-close in which a planted `corr=<victim>` + `STATE: closed` row traps the victim's genuine stop in the idempotency gate, leaving it `STATE: dispatched` forever. Also reachable without any newline via a JSON-array `agent_type` (jq -r pretty-prints multi-line) and via a concatenated JSON stream on stdin. Both attacks independently reproduced by the manager before the finding was accepted. Marks as UNVERIFIED whether the runtime can emit such an `agent_type` |
+| /docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | Report | 0 | 2026-08-07 | F4 (MFFU automation compliance) evidence artifact — lands Amear's prop-firm automation outreach on disk as a gradeable record. Carries the MFFU human-rep confirmation verbatim with thread metadata, and the full eight-firm result table with SOURCE QUALITY preserved per firm (human/written vs AI-generated vs no-reply vs bounced), deliberately NOT collapsed into confirmed/denied. RELAYED, NOT INDEPENDENTLY CONFIRMED — neither master nor manager read the source Gmail thread; every assertion about its contents is Amear-pasted text. WHAT IT DOES NOT ESTABLISH: MFFU issued no signed policy document (its "yes" points to a revisable help-center article), and the broader "no firm issued one" claim is IN TENSION with OneUp Trader's relayed "two policy docs" — recorded, not resolved; the "now permitted" phrasing implies a recent policy change whose effective date and retroactivity are UNCONFIRMED with a follow-up open; The Trading Pit's conditional yes is AI-agent-generated and links a Japanese-locale rules page against an English inquiry, so it is recorded low-confidence, not as a determination. S6 CROSS-BLOCK: MFFU's restriction against building automated tools that exploit sim-environment fill favorability bears directly on F3 (backtest fill resolution, FROZEN) — the coupling is named, and F3 is NOT resolved or opined on. This report DOES NOT UNFREEZE F4; `specs/SPEC_RUBRIC.md` is Amear's alone to change. Authorised by DECISION_LOG row `2026-08-07T16:13:58Z` (Amear, 2026-08-07) |
+| /docs/reports/2026-10-30-3gm-fidelity-check.md | Report | 2 | 2026-10-30 | AUTHORITATIVE manager report for Praxis_build-3gm (fidelity check of PraxisNoiseAreaBreakout.cs vs the noise-area ruleset); re-audit PASS (DECISION_LOG 2026-10-30T22:40:00Z), strike one on record; Audit-1 corrections at :1028-1348 |
+| /docs/reports/2026-10-30-3gm-worker1-checklist.md | Report | 2 | 2026-10-30 | Praxis_build-3gm worker sub-report (worker1, checklist). NOT authoritative; superseded by the manager report 2026-10-30-3gm-fidelity-check.md |
+| /docs/reports/2026-10-30-3gm-worker2-timing-orders-count.md | Report | 2 | 2026-10-30 | Praxis_build-3gm worker sub-report (worker2, timing / orders / count). NOT authoritative; superseded by the manager report 2026-10-30-3gm-fidelity-check.md |
+| /docs/reports/2026-10-30-3gm-worker3-adversarial-d1.md | Report | 2 | 2026-10-30 | Praxis_build-3gm adversarial sub-report (worker3, D1). NOT authoritative; superseded by the manager report 2026-10-30-3gm-fidelity-check.md |
+| /docs/reports/2026-10-30-3gm-worker4-adversarial-d2d4.md | Report | 2 | 2026-10-30 | Praxis_build-3gm adversarial sub-report (worker4, D2-D4). NOT authoritative; superseded by the manager report 2026-10-30-3gm-fidelity-check.md |
+| /docs/reports/2026-10-30-3gm-worker6-adversarial-manager.md | Report | 2 | 2026-10-30 | Praxis_build-3gm adversarial sub-report (worker6, against the manager report). NOT authoritative; superseded by the manager report 2026-10-30-3gm-fidelity-check.md |
+| /docs/reports/2026-10-30-run3-backtest-screenshot-record.md | Report | 2 | 2026-10-30 | Master transcription of the run-3 Strategy Analyzer Summary screenshot; run 3 ruled INVALID by Amear (DECISION_LOG 2026-10-30T22:22:00Z, WHO: amear) |
+| /docs/reports/evidence/2026-10-30-run3-strategy-analyzer-summary.webp | Asset | 2 | 2026-10-30 | Evidence: run-3 Strategy Analyzer Summary screenshot supplied by Amear, sha256 8787483dcb41fbc0d52c023faeb32ff3606075a8fa518126749b1a4da90eac55 |
+| /docs/reports/2026-10-28-voice-session-notes.md | Report | 2 | 2026-10-28 | Claude-written voice-session notes recording Amear's rulings (unaudited; incl. bar-time check PASS 2026-10-30 at :22-27). NOTE: untracked in git at the time of this row |
+| /docs/reports/2026-10-30-zyd-worker1-build.md | Report | 2 | 2026-10-30 | Praxis_build-zyd BUILD worker sub-report (worker1). NOT authoritative; sub-report to the zyd manager report |
+| /docs/reports/2026-10-30-zyd-worker2-adversarial.md | Report | 2 | 2026-10-30 | Praxis_build-zyd ADVERSARIAL sub-report (worker2; BREAK FOUND; fixes graded RESOLVED with residues by worker4). NOT authoritative; sub-report to the zyd manager report |
+| /docs/reports/2026-10-30-zyd-worker3-fix.md | Report | 2 | 2026-10-30 | Praxis_build-zyd fix-pass sub-report (worker3). NOT authoritative; sub-report to the zyd manager report |
+| /docs/reports/2026-10-30-zyd-worker4-readversarial.md | Report | 2 | 2026-10-30 | Praxis_build-zyd ADVERSARIAL re-attack sub-report (worker4; BREAK FOUND; fix pass by worker5, re-attacked by worker6). NOT authoritative; sub-report to the zyd manager report |
+| /docs/reports/2026-10-30-zyd-worker5-fix2.md | Report | 2 | 2026-10-30 | Praxis_build-zyd fix-pass-2 sub-report (worker5). NOT authoritative; sub-report to the zyd manager report |
+| /docs/reports/2026-10-30-zyd-worker6-final-adversarial.md | Report | 2 | 2026-10-30 | Praxis_build-zyd ADVERSARIAL re-attack sub-report (worker6; BREAK FOUND; fix pass by worker7, re-attacked by worker8). NOT authoritative; sub-report to the zyd manager report |
+| /docs/reports/2026-10-30-zyd-worker7-fix3.md | Report | 2 | 2026-10-30 | Praxis_build-zyd fix-pass-3 sub-report (worker7). NOT authoritative; sub-report to the zyd manager report |
+| /docs/reports/2026-10-30-zyd-worker8-final2-adversarial.md | Report | 2 | 2026-10-30 | Praxis_build-zyd ADVERSARIAL re-attack sub-report (worker8; BREAK FOUND; fix pass by worker9, re-attacked by worker10). NOT authoritative; sub-report to the zyd manager report |
+| /docs/reports/2026-10-30-zyd-worker9-fix4.md | Report | 2 | 2026-10-30 | Praxis_build-zyd fix-pass-4 sub-report (worker9). NOT authoritative; sub-report to the zyd manager report |
+| /docs/reports/2026-10-30-zyd-worker10-closing-adversarial.md | Report | 2 | 2026-10-30 | Praxis_build-zyd ADVERSARIAL closing sub-report (worker10; BREAK FOUND on one mis-cited line, :780 → :781; fixed by the manager as single-line edits). NOT authoritative; sub-report to the zyd manager report |
+| /docs/reports/2026-10-30-zyd-f3-artifact.md | Report | 2 | 2026-10-30 | Manager report for Praxis_build-zyd (F3 artifact); ungraded at time of row |
+| /config/backtest-cost-model.json | Config | 2 | 2026-07-15 | UPDATE ROW 2026-10-30 (append-only registry; supersedes the earlier row's numbers): v1.1.0, slippage 2 ticks/side, fill_resolution Standard (CONDITIONAL, void clause live), total $22.96 / 4.592 ticks RT; authorised by DECISIONS.md D-2026-10-30-A |
$ tail -n 12 MANIFEST.md | cut -c1-200
| /docs/reports/2026-10-30-zyd-worker1-build.md | Report | 2 | 2026-10-30 | Praxis_build-zyd BUILD worker sub-report (worker1). NOT authoritative; sub-report to the zyd manager report |
| /docs/reports/2026-10-30-zyd-worker2-adversarial.md | Report | 2 | 2026-10-30 | Praxis_build-zyd ADVERSARIAL sub-report (worker2; BREAK FOUND; fixes graded RESOLVED with residues by worker4). NOT au
| /docs/reports/2026-10-30-zyd-worker3-fix.md | Report | 2 | 2026-10-30 | Praxis_build-zyd fix-pass sub-report (worker3). NOT authoritative; sub-report to the zyd manager report |
| /docs/reports/2026-10-30-zyd-worker4-readversarial.md | Report | 2 | 2026-10-30 | Praxis_build-zyd ADVERSARIAL re-attack sub-report (worker4; BREAK FOUND; fix pass by worker5, re-attacked by worker6
| /docs/reports/2026-10-30-zyd-worker5-fix2.md | Report | 2 | 2026-10-30 | Praxis_build-zyd fix-pass-2 sub-report (worker5). NOT authoritative; sub-report to the zyd manager report |
| /docs/reports/2026-10-30-zyd-worker6-final-adversarial.md | Report | 2 | 2026-10-30 | Praxis_build-zyd ADVERSARIAL re-attack sub-report (worker6; BREAK FOUND; fix pass by worker7, re-attacked by wor
| /docs/reports/2026-10-30-zyd-worker7-fix3.md | Report | 2 | 2026-10-30 | Praxis_build-zyd fix-pass-3 sub-report (worker7). NOT authoritative; sub-report to the zyd manager report |
| /docs/reports/2026-10-30-zyd-worker8-final2-adversarial.md | Report | 2 | 2026-10-30 | Praxis_build-zyd ADVERSARIAL re-attack sub-report (worker8; BREAK FOUND; fix pass by worker9, re-attacked by wo
| /docs/reports/2026-10-30-zyd-worker9-fix4.md | Report | 2 | 2026-10-30 | Praxis_build-zyd fix-pass-4 sub-report (worker9). NOT authoritative; sub-report to the zyd manager report |
| /docs/reports/2026-10-30-zyd-worker10-closing-adversarial.md | Report | 2 | 2026-10-30 | Praxis_build-zyd ADVERSARIAL closing sub-report (worker10; BREAK FOUND on one mis-cited line, :780 → :781; 
| /docs/reports/2026-10-30-zyd-f3-artifact.md | Report | 2 | 2026-10-30 | Manager report for Praxis_build-zyd (F3 artifact); ungraded at time of row |
| /config/backtest-cost-model.json | Config | 2 | 2026-07-15 | UPDATE ROW 2026-10-30 (append-only registry; supersedes the earlier row's numbers): v1.1.0, slippage 2 ticks/side, fill_resolution Standa
$ git diff --cached MANIFEST.md | grep '^-' | grep -vc '^---'
0
$ git diff --cached --stat -- DECISIONS.md MANIFEST.md config/backtest-cost-model.json
 DECISIONS.md                    | 54 +++++++++++++++++++++++++++++++++++++++++
 MANIFEST.md                     | 36 +++++++++++++++++++++++++++
 config/backtest-cost-model.json | 25 ++++++++++---------
 3 files changed, 103 insertions(+), 12 deletions(-)
```

### E9b Staged set

```text
$ git status --short DECISIONS.md MANIFEST.md config/backtest-cost-model.json docs/reports/2026-10-30-zyd-*   (captured before the manager report was added)
M  DECISIONS.md
M  MANIFEST.md
M  config/backtest-cost-model.json
A  docs/reports/2026-10-30-zyd-worker1-build.md
A  docs/reports/2026-10-30-zyd-worker10-closing-adversarial.md
A  docs/reports/2026-10-30-zyd-worker2-adversarial.md
A  docs/reports/2026-10-30-zyd-worker3-fix.md
A  docs/reports/2026-10-30-zyd-worker4-readversarial.md
A  docs/reports/2026-10-30-zyd-worker5-fix2.md
A  docs/reports/2026-10-30-zyd-worker6-final-adversarial.md
A  docs/reports/2026-10-30-zyd-worker7-fix3.md
A  docs/reports/2026-10-30-zyd-worker8-final2-adversarial.md
A  docs/reports/2026-10-30-zyd-worker9-fix4.md
```


## Bead acceptance → DECISIONS.md lines

Bead text (E2): "a written decision (DECISIONS.md) fixing (a) bar/data resolution for the backtest, (b) the intrabar fill assumption NT8 will use, (c) why that does not bias the entry/exit of THIS strategy."

| Part | DECISIONS.md line | Met? |
|---|---|---|
| (a) | `:257` | **Met.** 1-minute NQCONT, end-stamped (INFERRED by Claude from the file plus Amear's REPORTED NT8 read). Import file range OBSERVED this session: first row `20210307 180100`, last row `20260720 112700`, 1,857,362 lines. No tick or second series. |
| (b) | `:258` | **Met.** Standard: value OBSERVED on the run-3 screenshot, explicitness REPORTED. 2 ticks/side; $22.96 / 4.592 ticks RT; next-bar-open fill INFERRED. Per-fill application UNCONFIRMED. NQCONT point value UNVERIFIED (3gm `:949`). |
| (c) | `:259-262` | **NOT fully met, and the entry says so** (`:259`: "This entry does not establish the bead's (c) in full"). What it shows: at a checkpoint with a given position state, intrabar High/Low ordering does not decide whether an order is sent (code OBSERVED, market-order type INFERRED). What it does not show: that the trade set is unaffected. 3gm D4 hypothesis 5 (`:784`) with hypothesis 2 (`:781`) gives an INFERRED path by which fill resolution changes later position state and so later entries. The settling experiment is the R3 Standard-vs-High control (row `2026-08-29T00:40:00Z`, open), and its disposition is Amear's (NEEDS AMEAR 5). |

Also present:
- pre-commitment `:263`;
- void clause verbatim plus status `:264` (byte check E5);
- proposed limitation sentence `:265`;
- authorisation chain `:269`;
- config pointer `:271`;
- S6 `:278-285`;
- NEEDS AMEAR `:287-293`;
- Supersedes `:295`.

## Adversarial findings

Four adversarial rounds. Every BLOCKING and MAJOR finding was confirmed on disk by the manager and then fixed with exact replacement text. Each fix was re-attacked by the next round, except the manager's final five single-line edits, which were verified only mechanically (E8).

**Brief-specified attacks:**
- **Does it decide anything that is Amear's?** Round 1 found two: B1 (LOCKED vs CONDITIONAL) and M5 (the limitation wording). Round 2 found two more: the "Resolves:" line, and the Unblocks line making the wording mandatory. Round 3 found the `[N]` scope question. All fixed. Round 4 (w10) reports nothing of Amear's decided.
- **Does it upgrade an INFERRED claim?**
  - Round 1: M2 (config note), M4 (FlatEOD not checkpoint-gated), m4 (Context 00:35 claim), m5 ("no resting order").
  - Round 3: the `:784` contrary hypothesis.
  - Round 4: the hidden position-state path.
  - All fixed.
- **Does the arithmetic hold?** Every round recomputed it and it holds (E3).
- **Is the void clause verbatim against row `00:10:00Z`?** Every round compared it programmatically: byte-identical, same sha256 `f9144cb5…4a79` (E5).

**MINOR, open, not fixed (none is against a criterion; listed so the auditor sees them):**
1. Config `fill_resolution_note` says "evaluated OnBarClose" without the entry's split (setting OBSERVED in code, runtime semantics INFERRED).
2. The void-clause bullet `:264` states "not triggered and not retired" in its Status and again implicitly in the next sentence. This is redundancy, not contradiction.
3. The corrected deletion check `grep '^-' | grep -vc '^---'` is itself blind to a deleted literal `---` separator line. For DECISIONS the HEAD hash on lines 1–243 covers this. For MANIFEST, rows start with `|`.

## S6 cross-block check

Consumers of the cost model, each named in the entry's S6 section (`:278-285`):
- **The JSON's `applies_to` (three items):**
  - P&L distributions (NT8 WFA plus Python MC) now carry $22.96 RT.
  - R-multiple conversion (Q6) deducts the new cost before normalisation.
  - SHM distributions and thresholds (D-2026-07-04-B) derive from the 2-tick base.
- **SHM-4** (`docs/specs/STRATEGY_HEALTH_MONITOR_SPEC.md:48-51`; band numbers in D-2026-07-15-B Q9 "slippage >2 ticks/side worse"): whether the band is re-read against a 2-tick base is **NEEDS AMEAR 1**, not answered.
- **Rubric O4 Block-4 gate** (`specs/SPEC_RUBRIC.md:94-99`, ±15% win rate / ±25% average trade P&L): it now compares live to a 2-tick backtest.
- **Analyzer template "Praxis Backtest":** already Slippage 2 / Standard (REPORTED).
- **F4:** `docs/reports/2026-08-07-f4-mffu-compliance-evidence.md:151` couples MFFU restriction 2 (`:45`) to F3's optimistic-fill failure mode. Named, not resolved.
- **Spec texts that still carry the superseded Q5 terms**, not edited and named so they are not read as current:
  - `docs/specs/2026-07-15-block2-backtesting-scope-proposal.md:129`: "High fill res, 1-tick series, 1-tick slippage", attributed there to the Phase 3 Build Spec.
  - `docs/specs/2026-07-15-b2-data-acquisition-spec.md:53`: "Q5, 1 tick/side", "the High-resolution intrabar path".
- **Not checked:** whether any code in the Python MC/SHM layers reads `fill_resolution` or the slippage keys. w1 and w10 noted that no code consumer was found, but no exhaustive code grep is pasted here.

## NEEDS AMEAR (as written in the entry, `:288-293`; none answered)

1. SHM-4 band re-read against the 2-tick base?
2. Does the timing satisfy F3's "stated in writing before the backtest runs"? `[N]` was chosen 2026-10-28 (REPORTED). It was first ledgered at `2026-10-30T21:36:00Z`/`21:36:30Z`, after runs 1–3, and this entry is written after run 4.
3. Readback: does NT8 apply Slippage 2 on every market fill, and what unit is the Summary's "Total slippage" in?
4. Approve or replace the proposed limitation sentence.
5. The R3 Standard-vs-High control (`2026-08-29T00:40:00Z`, open): run it before F3 is graded, or let (c) stand as INFERRED?
6. Scope of the `[N]` lock: was it meant to cover session-close and stop-out exits too (3gm `:949`)?

## Notes for the master (commit pathspec hazards)

- `MANIFEST.md`'s index already held **15 rows staged by other units** (F4/r8j/etc.) before this unit. Staging MANIFEST.md carries them, so a pathspec on `MANIFEST.md` will commit them with this unit (E9 shows all 36 added lines).
- `docs/reports/2026-10-28-voice-session-notes.md` is **untracked**. The entry cites it at `:257`, and it has a MANIFEST row. If it is not in Amear's pathspec, both citations dangle.
- `DECISION_LOG.md` was not touched. Its staged lines from other units are unchanged by this unit.
- `specs/SPEC_RUBRIC.md` has an unstaged 10-line edit by another party (hunk at `:263+`, not F3). It was not touched (E1).
- The scratch file `scratchpad/vc.py` was overwritten by w2 mid-unit. The manager's evidence uses its own `scratchpad/mgr_vc.py`.
- Every worker and the manager used the deletion check `grep -c '^-[^-]'` to prove "no deleted lines". It is blind to deleted markdown bullets (E7b). Other units in this repo may rely on the same check.

## Files staged

E9 is the staged set, captured before this report was added. This report, `docs/reports/2026-10-30-zyd-f3-artifact.md`, is then staged as a new file:
- `DECISIONS.md`: +54 lines, 0 deleted; lines 1–243 hash-identical to HEAD.
- `config/backtest-cost-model.json`: v1.1.0, 13 insertions / 12 deletions.
- `MANIFEST.md`: +36 in the index. 15 rows are other units' (pre-staged); 21 rows are this unit's.
- Ten worker sub-reports `docs/reports/2026-10-30-zyd-worker{1..10}-*.md`.
- This report.

Nothing outside the brief's allowed set was edited. Nothing is committed.

## Verdict

- (a) is met; (b) is met.
- The config v1.1.0 numbers and arithmetic hold (E3).
- The void clause is verbatim (E5).
- The authorisation chain cites only ledger rows that exist (E8, w10 table).
- S6 names every consumer.
- Six Amear questions are routed and none is answered.

**Bead zyd's (c) is NOT fully met.** The entry shows only that fill resolution does not decide the checkpoint order logic given a position state. Its own source (3gm `:781`, `:784`, INFERRED) leaves an open path by which fill resolution changes later position state and so the trade set. The entry states this at `:259`. Settling it needs the R3 Standard-vs-High control run (row `2026-08-29T00:40:00Z`), which is a VM action, or Amear's ruling that (c) may stand as INFERRED. Both are Amear's (NEEDS AMEAR 5). Paperwork cannot clear (c), and marking the unit PASS on two of three acceptance parts would be the partial-progress PASS the contract forbids.

**Result: BLOCKED** — artifact complete and staged for audit; bead (c) blocked on Amear (NEEDS AMEAR 5: run the R3 control, or rule that (c) stands as INFERRED).

## Self-grade limits

- This is the producer's own reading. It is not a grade; the auditor grades.
- The manager's five single-line edits after w10 (E8) were verified mechanically (quotes, hashes, exact-once replacement). They were not re-attacked by a fresh adversary.
- NT8 behaviour is not observed anywhere in this unit:
  - Standard's intrabar model;
  - per-fill slippage application;
  - next-bar-open fills;
  - the NQCONT point value.
  Every such claim is INFERRED or REPORTED.
- Run 4's settings and numbers are REPORTED BY AMEAR; no Claude has seen run 4.
- Whether any code consumer reads the config keys was not checked exhaustively.
- The import file read (E8) is of the Mac-side file. That NT8's NQCONT was built from exactly this file rests on the voice notes' one-date bar-for-bar match.
