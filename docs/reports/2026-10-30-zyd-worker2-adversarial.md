# Praxis_build-zyd — worker 2 ADVERSARIAL report

## Task
Unit Praxis_build-zyd. Mode: **ADVERSARIAL (read-only)**. The job was to break the unstaged F3 artifact: `DECISIONS.md` entry D-2026-10-30-A (lines 244-291), `config/backtest-cost-model.json` v1.1.0, and the 11 rows appended to `MANIFEST.md` (lines 133-143).
Criteria: the bead acceptance (a)(b)(c), F3 (`specs/SPEC_RUBRIC.md:45-57`), S1, S2, S4, S5, S6, S8, and the config's `$schema_note`.
I edited nothing except this file. I staged nothing.

## Attacks

### A. Does the entry decide anything that is Amear's? (S8) — **BREAKS** (findings B1, M1, M5)
SHM-4 re-basing, the F3 timing question and the slippage-unit readback all go to NEEDS AMEAR, which is correct. Three things are still decided or attributed on his behalf:
- The header and Status call the fill resolution **LOCKED (Amear)**. His own ruling made it conditional. See B1.
- The entry says 2 ticks "is meant to price" four residual risks. See M1.
- It sets a mandatory exact limitation sentence. See M5.

The ledger uses "LOCK" only for `[N]`, and row 347 says CONDITIONAL:
```
$ for n in 347 442 450 454; do sed -n ${n}p DECISION_LOG.md | grep -o -i -E '.{60}(LOCK|CONDITIONAL).{60}'; done
347: EARANCE PATH RULED — the assumption is to be committed as CONDITIONAL, carrying an explicit VOID CLAUSE, not as a decision. AMEAR -decided cold."* ...
442: ... er stress run at 3 ticks is ALLOWED and does not change the locked number | WHY: ...
450: ge is applied on every market fill. `[N]` STAYS 2 ticks — locked before results.** ...
454: (no LOCK hit on fill resolution)
```
The limitation sentence first appears in this artifact:
```
$ grep -rn -F 'Fills are optimistic;' --include='*.md' --include='*.json' .
./config/backtest-cost-model.json:27: ...
./docs/reports/2026-10-30-zyd-worker1-build.md:47: ...
./DECISIONS.md:265:- **Limitation sentence every backtest report must carry, exactly:** `Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/sid
$ grep -n -F 'Fills are optimistic' DECISION_LOG.md DISPATCH_LOG.md
DECISION_LOG.md:347 (the void clause only — "Fills are optimistic and the report states so.")
DECISION_LOG.md:442 (the same clause, quoted)
```

### B. Label upgrades (S2) — **BREAKS** (findings M2, M4; minor m4, m5)
3gm legend (`:5-8`): OBSERVED = read from a file and the output pasted; REPORTED BY AMEAR = from his hand-run; INFERRED = NT8 runtime behaviour, or reasoning with no on-disk observation behind it.

- **Config `fill_resolution_note`** states without a label: *"every strategy order is a managed Enter*/Exit* call with no price argument, evaluated OnBarClose at HH:00/HH:30 checkpoints (no touch-triggered order), so intrabar High/Low ordering does not decide entries/exits."*
  - The DECISIONS entry labels this same conclusion INFERRED: *"That NT8 realises these calls as market orders — and therefore that the Analyzer never needs the intrabar path — is INFERRED."*
  - 3gm §7 (`:1207`) also says: "That NT8 submits each as a market order is INFERRED."
- **(c)** states *"decisions are evaluated only at HH:00/HH:30 checkpoint bars (`:196-198`) … All OBSERVED in … D3 `:737-775` as corrected by Audit-1 §7."* §7 scoped that claim to **trailing stops** only: *"'Trailing stops' are conditions evaluated only at checkpoint bars (lines 196–198)."* For FlatEOD (`:288/:290`) the claim is false:
```
$ sed -n 185,195p ninjascript/PraxisNoiseAreaBreakout.cs
			// ---- 16:00 ET cash-close flat (spec §4 p.9/12; trader-locked). Applies before any entry. ----
			if (mod >= CloseMod)
			{
				FlattenAll("16:00 session flat");
				return;                          // never open a new position at/after the close
			}
			// ---- Act ONLY at semi-hourly checkpoints HH:00 / HH:30, strictly inside RTH (spec §2 p.9). ----
```
  `FlattenAll` sits before the checkpoint gate and runs on any bar with `mod >= 960`, not only at HH:00/HH:30. The cited D3 and §7 ranges also do not contain the `:105` or `:200` claims. Those are in R1, Audit §5 and D2(a). §5 `:1173` labels the runtime half of OnBarClose INFERRED:
```
$ grep -n -E 'OnBarClose|\b105\b' docs/reports/2026-10-30-3gm-fidelity-check.md | head
72:| R1 | §A L16 — no look-ahead via OnBarClose | ... | 104,105 | FAITHFUL |
1164:### 5. :103 OnBarClose semantics (MINOR; S9/R3)
1173:**Corrected :103:** "... `Calculate = Calculate.OnBarClose` (line 105, OBSERVED). That `Close[0]` is then the close of a finished bar is NT8 runtime semantics (INFERRED; not observed on this install)..."
```
- **Context paragraph:** *"`2026-08-29T00:35:00Z` recorded that the strategy's order is a market order … filled at the next bar's open"*. This repeats row 353 without the downgrade at 3gm D2(a) `:722`: *"DECISION_LOG:353's 'filled at the next bar's open' is likewise INFERRED, not observed."* (minor m4, because (b) labels the next-open fill INFERRED further down.)
- **(c)** *"There is no resting or touch-triggered order, so Standard's intrabar High-vs-Low ordering assumption never decides an entry or exit."* This is stated flat. Its INFERRED qualifier only comes in the next sentence (m5).
- **These hold:**
  - "END-STAMPED (REPORTED BY AMEAR)" matches 3gm D2's label.
  - "Standard (Fastest)" is labelled OBSERVED for run 3 and REPORTED for run 4, which matches row 449 and the run-3 record `:28`.
  - The FlatEOD, reversal and early-close items are labelled CANNOT-DETERMINE-STATICALLY and INFERRED, which matches row 446 and D2(c).

### C. Arithmetic — **HOLDS**
```
$ python3 -I -c "t=5.0; print('slip/side',2*t,'rt ticks',2*2,'rt usd',4*t,'total',round(2.96+20,2),'comm ticks',round(2.96/t,4),'total ticks',round(4+2.96/t,4),'old',round(2.96+10,2),round(2+2.96/t,4))"
slip/side 10.0 rt ticks 4 rt usd 20.0 total 22.96 comm ticks 0.592 total ticks 4.592 old 12.96 2.592
$ wc -l < ~/praxis-signals/b2-data/NQ-continuous-1min.nt8import.txt ; head -1 ...; tail -1 ...; awk 'END{print NR}'
 1857362
20210307 180100;16120.5;16167;16120.5;16154.75;17
20260720 112700;29005.5;29020.75;29003.5;29016;308
1857362          (trailing byte 0a; 0 blank lines)
$ shasum -a 256 ninjascript/PraxisNoiseAreaBreakout.cs docs/reports/evidence/2026-10-30-run3-strategy-analyzer-summary.webp
35393823e9bc146e95dcb1d9f6fe5785a3c72ee3a3fb71287f33fe2242752265  ninjascript/PraxisNoiseAreaBreakout.cs
8787483dcb41fbc0d52c023faeb32ff3606075a8fa518126749b1a4da90eac55  docs/reports/evidence/2026-10-30-run3-strategy-analyzer-summary.webp
$ git log --oneline -1 -- ninjascript/PraxisNoiseAreaBreakout.cs ; git diff --stat HEAD -- (same)
719ab11 Praxis_build-4uu (b2-signal-repro): ...   (no working-tree diff)
webp size: 111376
```
The six call-site lines (`:211 :219 :227 :229 :288 :290`), `:105` and `:200` were each re-read with `sed -n`, and each matches its quoted fragment.

### D. Void clause — **HOLDS** (byte-identical). Status sentence: minor m3
```
$ python3 -I vc.py   (extracts *"We accept Standard…cold."* from row 2026-08-29T00:10:00Z, from D-2026-10-30-A and from row 21:36:30Z)
'We accept Standard resolution on 1-minute bars. Band-edge slippage widened to [N]. Fills are optimistic and the report states so. If the VM measurement shows NT8 errors or demands a secondary series rather than falling back silently, this row is void and the assumption is re-decided cold.'
entry==00:10 True 289 289
21:36==00:10 True
f9144cb50aab2885e28daecefb4c3e80a900963769bf396d92c3318629884a79
f9144cb50aab2885e28daecefb4c3e80a900963769bf396d92c3318629884a79
non-ascii in a: []
```
- "NOT triggered and NOT retired" plus the REPORTED BY AMEAR label is faithful to row 442.
- The added sentence *"It would be triggered by any run that sets High and errors or demands a secondary series"* appears in no ledger row. It reinterprets Amear's trigger: the clause names "the VM measurement", which has never been run. (m3)

### E. Authorisation chain (S4/S5) — **HOLDS**, one ambiguity (m2)
- All six cited timestamps exist: 347, 353, 442, 449, 446/450 and 454 (output in the Process log).
- **Ambiguity:** `2026-10-30T22:22:00Z` matches **two** rows. Row 446 (WHO praxis-master) is the 3gm return. Row 450 (WHO amear) is "`[N]` STAYS 2". The entry means 450 but cites only the timestamp (m2).
- **Timing is disclosed, not glossed:**
  - Pre-commitment bullet: "chosen 2026-10-28 … (REPORTED…)".
  - NEEDS AMEAR (2): "first ledger writing is the 21:36:30Z row, after runs 1–3 … this entry is written after run 4 (REPORTED). Does that satisfy F3…?"
- The entry cites ledger rows as the authorisation, not the verbal exchange. Row 442 itself says "APPROVED BY: amear, 2026-10-28 (voice session), reaffirmed in this session's opening message". Under S5 that row is the authorisation.
- S4 note, not graded as a break: the DECISIONS entry is written after the runs. The bead title says "BEFORE running". This is disclosed and is a fact the artifact cannot fix.

### F. S6 consumers — **BREAKS** (M3, M6)
```
$ python3 -I keys.py
removed keys: []
added keys: ['/amended']
CHANGED /$schema_note /cost_model/fill_resolution /cost_model/fill_resolution_note /cost_model/slippage_* (4) /cost_model/total_* (3) /decision_ref /version
applies_to: ["All P&L distributions (NT8 WFA fills + Python Monte Carlo)",
             "All Strategy Health Monitor (SHM) distributions and threshold derivations (D-2026-07-04-B)",
             "R-multiple conversion: costs deducted before R normalization (Q6)"]
```
- All three `applies_to` items are named, plus SHM-4/Q9, O4 ±15%/±25% and the Python MC layer.
- **Dropped information (M3):** the old note's consumer instruction *"Python MC assumes fills already reflect this via the exported NT8 trade list."* is not in the new `fill_resolution_note` (see `git diff config/backtest-cost-model.json`). The MC layer is a named consumer of this file. Its "do not re-apply fill/cost modelling" instruction is now gone.
- **Missing coupling (M6):** the F4 coupling is already on disk and is not named:
```
$ sed -n 151,157p docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
## 4. S6 cross-block check — MFFU restriction 2 couples to F3
... MFFU's restriction that **automated tools may not be built to exploit sim-environment fill favorability** touches **F3 — Backtest fill resolution ...
```
  The entry hard-codes "Fills are optimistic", which is the shared failure mode that section names. Its S6 list does not mention F4.

### G. Bead (a)(b)(c) — (a)/(b) **HOLD**; (c) **BREAKS** in part (M1, M4)
```
$ bd show Praxis_build-zyd
... enters on band-touch and exits on opposite-band/VWAP — both INTRABAR events ... ACCEPTANCE: ... (a) bar/data resolution ... (b) the intrabar fill assumption NT8 will use, (c) why that does not bias the entry/exit of THIS strategy.
```
- **(a)** NQCONT 1-min with the file pinned: holds.
- **(b)** Standard, 2 ticks, next-open INFERRED: holds.
- **(c)** correctly refutes the band-touch premise against the code, and says outright that it is not a claim the backtest is unbiased. Two problems remain:
  - Its premise sentence ("decisions … only at checkpoint bars", labelled OBSERVED) is false for 2 of the 6 call sites (M4).
  - It then says the residual risks are what 2 ticks "is meant to price" (M1). Row 442 gives only "the number prices stamp-to-next-open slippage". A slippage tick count cannot price an overnight hold (FlatEOD next-day 09:31 per D2(c) S2/S3) or an early-close carry. This both overclaims and attributes a purpose to Amear's number.

### H. Config — **HOLDS** (apart from F)
```
$ python3 -I -m json.tool config/backtest-cost-model.json >/dev/null && echo PARSE_OK
PARSE_OK
cost_model: {'commission_round_turn_usd': 2.96, 'commission_basis': 'round_turn', 'slippage_ticks_per_side': 2, 'slippage_usd_per_side': 10.0, 'slippage_round_turn_ticks': 4, 'slippage_round_turn_usd': 20.0, 'fill_resolution': 'Standard', 'total_cost_per_round_turn_usd': 22.96, 'total_cost_per_round_turn_ticks': 4.592}
instrument: {'symbol': 'NQ', ..., 'tick_size': 0.25, 'point_value_usd': 20.0, 'tick_value_usd': 5.0, 'ticks_per_point': 4}
```
No key was removed. Commission, `commission_note`, instrument, `applies_to`, `bead` and `created` are unchanged.

### I. Edits outside the declared line sets — **HOLDS**
```
$ git diff --stat DECISIONS.md config/backtest-cost-model.json MANIFEST.md
 DECISIONS.md                    | 48 +++++
 MANIFEST.md                     | 11 ++++
 config/backtest-cost-model.json | 25 ++++-----
$ git diff DECISIONS.md | grep -c '^-[^-]'      -> 0
$ git diff MANIFEST.md | grep -c '^-[^-]'       -> 0
$ git diff -U0 MANIFEST.md | grep '^@@'         -> @@ -132,0 +133,11 @@
$ git diff -U0 DECISIONS.md | grep '^@@'        -> @@ -243,0 +244,48 @@
$ git diff --numstat ...                        -> 48 0 DECISIONS.md / 11 0 MANIFEST.md / 13 12 config
```
**MANIFEST check (m1):**
```
$ ls -la docs/reports/2026-10-30-zyd-f3-artifact.md
ls: docs/reports/2026-10-30-zyd-f3-artifact.md: No such file or directory
```
MANIFEST row 142 registers this file as "AUTHORITATIVE manager report", but the file is not on disk and has not been graded.

## Process log (key reads)
- `git diff` on all three artifact files.
- DECISION_LOG rows located: 347, 353, 442, 446, 449, 450, 452, 454.
- 3gm report `:5-8`, `:688-735`, `:737-775`, `:1028-1083`, `:1164-1173`, `:1185-1207`.
- `.cs` lines 105, 185-200, 205-229, 285-291.
- DECISIONS `:178-194`; SHM spec `:40-55`; rubric `:45-57` and `:94-99`.
- Voice notes `:1-12`, `:20-30`, `:49`; run-3 record (grep); F4 evidence report `:151-190`; `bd show`.

## Findings

### BLOCKING
**B1 — "LOCKED (Amear)" upgrades a CONDITIONAL ruling (S2, S8).**
- Row 347 (Amear) says: "the assumption is to be committed as CONDITIONAL, carrying an explicit VOID CLAUSE, not as a decision. AMEAR REJECTED THE MASTER'S OWN FRAMING AND THE REJECTION IS THE SUBSTANCE OF THIS ROW."
- Row 442 "FILLS the conditional" and locks only the number `[N]`.
- The entry's title ("F3 backtest fill resolution + band-edge slippage LOCKED") and its Status line ("LOCKED (Amear; …)") attribute a lock on the fill-resolution assumption to Amear. No row gives one.
- DECISIONS.md is append-only, so this status line cannot be corrected later without a new entry.

**Fix text:**
- Title: `## 2026-10-30 — D-2026-10-30-A: F3 backtest fill resolution (CONDITIONAL, void clause live) + band-edge slippage [N] = 2 ticks/side (locked by Amear); amends D-2026-07-15-B Q5 slippage/fill terms`
- Status: `**Status:** CONDITIONAL — committed per Amear's ruling DECISION_LOG 2026-08-29T00:10:00Z with its void clause live (see below); [N] = 2 ticks/side LOCKED by Amear at 2026-10-30T21:36:30Z, reaffirmed at 2026-10-30T22:22:00Z (WHO: amear).`

### MAJOR
**M1 — "Residual risks that remain, and that 2 ticks is meant to price:" (S8, S2).**
- The only ledger statement of what 2 ticks prices is row 442: "stamp-to-next-open slippage, not touch adverse selection". That is the master's wording, not Amear's.
- Overnight-hold and early-close risks cannot be priced by a per-fill tick count.

Fix: `Residual risks that remain. Only the first is a slippage item; the ledger (2026-10-30T21:36:30Z) says 2 ticks prices stamp-to-next-open slippage, and no row says it prices the others:`

**M2 — Config `fill_resolution_note` drops the INFERRED label that the DECISIONS entry carries (S2).**
Fix: replace `(no touch-triggered order), so intrabar High/Low ordering does not decide entries/exits.` with `(no Set*/Submit*/limit/stop call — OBSERVED in code). That NT8 realises these calls as market orders, so intrabar High/Low ordering does not decide entries/exits, is INFERRED.`

**M3 — Config edit drops the Python MC consumer instruction (S6).**
Fix: append to `fill_resolution_note`: ` Python MC assumes fills and slippage already reflect this via the exported NT8 trade list (do not re-apply).`
Whether "and slippage" is true for the MC layer is UNVERIFIED by me. Restoring the original sentence verbatim is the minimum fix.

**M4 — "decisions are evaluated only at HH:00/HH:30 checkpoint bars (`:196-198`) … All OBSERVED in D3 … as corrected by §7" is false for `:288/:290` and miscites its source (S1, S2).**
- `FlattenAll` (`:189`, `mod >= CloseMod`) runs before and outside the checkpoint gate.
- §7 scoped the claim to trailing stops.
- `:105` and `:200` are in R1, §5 `:1173` and D2(a), not in D3 or §7.

Fix: `entry and checkpoint-exit decisions (:211, :219, :227, :229) are evaluated only at HH:00/HH:30 checkpoint bars (:196-198); the FlatEOD exits (:288, :290) are evaluated on any bar with mod >= CloseMod (:189), a clock condition, not a price touch. Calculate.OnBarClose is set at :105 and the decision price is Close[0] at :200 (code OBSERVED; OnBarClose runtime semantics INFERRED per 3gm Audit-1 §5 :1173). Sources: 3gm D3 :737-775, Audit-1 §5 :1164-1173, §7 :1185-1207, D2 :688-735.`
Mirror the change in the config note: `evaluated OnBarClose at HH:00/HH:30 checkpoints, or on the 16:00 clock for FlatEOD`.

**M5 — The mandatory exact limitation sentence was not ruled by Amear (S8).** No ledger row contains it (grep above).
Fix: `**Limitation sentence — PROPOSED wording, not ruled by Amear (Amear's ruled requirement is only "Fills are optimistic and the report states so", 2026-08-29T00:10:00Z):** ...`
Then add a NEEDS AMEAR item: `4. Approve or replace the proposed limitation sentence.`

**M6 — S6 omits the F4 coupling already on disk.**
Fix: add an S6 bullet: `F4 (MFFU automation compliance): docs/reports/2026-08-07-f4-mffu-compliance-evidence.md §4 couples MFFU restriction 2 (no tools exploiting sim fill favorability) to F3's optimistic-fill failure mode. Named, not resolved; F4 stays as Amear rules it.`

### MINOR
- **m1** — MANIFEST row 142 registers `docs/reports/2026-10-30-zyd-f3-artifact.md`, which does not exist, as "AUTHORITATIVE" before audit. Fix: land the file before staging. Change "AUTHORITATIVE" to "manager report (ungraded at time of row)".
- **m2** — The cited `2026-10-30T22:22:00Z` is ambiguous between two rows (446 master, 450 amear). Fix: write `2026-10-30T22:22:00Z (WHO: amear)` in Context, Rationale, the auth chain and NEEDS AMEAR (3).
- **m3** — The void-clause trigger sentence reinterprets Amear's clause. Fix: `The clause's trigger is "the VM measurement", which has not been run; the master's reading (21:36:30Z) is that it is not exercised while no run sets High. Whether a High run is the trigger is Amear's.`
- **m4** — Context sentence on 00:35. Fix: add `(INFERRED per 3gm D2(a) :722)` after "filled at the next bar's open".
- **m5** — (c) "There is no resting or touch-triggered order" is flat. Fix: prefix with `No Set*/Submit*/limit/stop call exists (OBSERVED); assuming the Enter*/Exit* calls are market orders (INFERRED), there is no resting …`.
- **m6** — D3's seventh order source (platform "Exit on session close", `:108`) is left out of (c)'s inventory. Fix: add it as `(:108) IsExitOnSessionCloseStrategy — platform session-close exit, clock-triggered (INFERRED)`.
- **m7** — MANIFEST row 141 calls the voice notes "Amear's rulings". The file's header says it was written by Claude and is not audited. Fix: `Claude-written voice-session notes recording Amear's rulings (unaudited)`.

## NOT CHECKED
- What NT8 Standard resolution actually does intrabar (no NT8 here; no web fetch). Any statement about it remains INFERRED.
- Whether NQCONT in NT8 was built from this exact import file, beyond the voice notes' bar-for-bar match on one date. `NQCONT.Last.txt` has the same size (95,900,139 bytes); I did not hash it.
- The content of the 15 staged MANIFEST rows above line 133 (out of scope).
- Whether D-2026-07-04-B defines threshold derivations that read the cost model directly (I read only the heading at `DECISIONS.md:43`).

VERDICT: BREAK FOUND
