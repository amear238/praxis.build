# Praxis_build-zyd — worker 1 BUILD report (F3 artifact paperwork)

## Task
BUILD, dispatched by praxis-manager. Criterion: rubric F3 (`specs/SPEC_RUBRIC.md:45-57`) written-assumption requirement; bead Praxis_build-zyd acceptance (a)(b)(c). Three deliverables: (A) append D-2026-10-30-A to `DECISIONS.md`; (B) `config/backtest-cost-model.json` → v1.1.0; (C) append 11 rows to `MANIFEST.md`. Nothing staged (manager stages). Nothing written under `.claude/`.

## Edits made
- `DECISIONS.md`: 48 lines appended after the last line (blank + `---` + blank + 45-line entry). Heading exactly as briefed. Void clause spliced programmatically from `DECISION_LOG.md` line 347 (byte-equal, check 6). No existing line touched (check 5: 0 deletions).
- `config/backtest-cost-model.json`: exactly the briefed field edits; `amended` inserted after `created`; 2-space indent and key order kept. Commission, instrument, `applies_to`, `bead`, `created` unchanged (see diff).
- `MANIFEST.md`: 11 rows appended after the 15 pre-staged rows (0 deletions).
- Facts re-checked this session (not just taken from the brief): strategy sha256 `35393823e9bc146e95dcb1d9f6fe5785a3c72ee3a3fb71287f33fe2242752265`; six call sites at :211/:219/:227/:229/:288/:290 and :105/:196-200 via grep/sed; import file first `20210307 180100`, last `20260720 112700`, `wc -l` 1857362; voice notes untracked (`git ls-files --error-unmatch` → "did not match"); webp sha256 matches; 3gm report is 1348 lines with `## Audit-1 corrections` at :1028; bead text contains "breakout enters on band-touch and exits on opposite-band/VWAP — both INTRABAR events" (`bd show`); ledger rows 00:10/00:35/21:36:30/22:17/22:22/22:28/22:40 exist.

## Verification evidence (pasted)
```
$ python3 -I -m json.tool config/backtest-cost-model.json | head -3
{
    "$schema_note": "PRAXIS Block-2 backtest cost + instrument model. ... Do NOT hand-edit numbers without a corresponding DECISIONS.md entry. v1.1.0 number changes are authorised by DECISIONS.md D-2026-10-30-A.",
    "version": "1.1.0",
$ ... | tail -3
        "R-multiple conversion: costs deducted before R normalization (Q6)"
    ]
}
$ git diff config/backtest-cost-model.json
@@ -1,8 +1,9 @@
-  "$schema_note": "... Do NOT hand-edit numbers without a corresponding DECISIONS.md entry.",
-  "version": "1.0.0",
+  "$schema_note": "... Do NOT hand-edit numbers without a corresponding DECISIONS.md entry. v1.1.0 number changes are authorised by DECISIONS.md D-2026-10-30-A.",
+  "version": "1.1.0",
   "created": "2026-07-15",
-  "decision_ref": "DECISIONS.md D-2026-07-15-B (Q5)",
+  "amended": "2026-10-30",
+  "decision_ref": "DECISIONS.md D-2026-07-15-B (Q5); amended by D-2026-10-30-A (slippage + fill resolution)",
@@ -18,15 +19,15 @@
-    "slippage_ticks_per_side": 1,
-    "slippage_usd_per_side": 5.0,
-    "slippage_round_turn_ticks": 2,
-    "slippage_round_turn_usd": 10.0,
-    "fill_resolution": "High",
-    "fill_resolution_note": "NT8 Strategy Analyzer 'Order fill resolution' = High (intrabar sub-bar granularity ...). Python MC assumes fills already reflect this via the exported NT8 trade list.",
-    "total_cost_per_round_turn_usd": 12.96,
-    "total_cost_per_round_turn_ticks": 2.592,
-    "total_cost_breakdown_note": "12.96 = 2.96 commission + 10.00 slippage (2 ticks x 5.00). In ticks: 0.592 commission-equivalent + 2.0 slippage = 2.592 ticks round-turn."
+    "slippage_ticks_per_side": 2,
+    "slippage_usd_per_side": 10.0,
+    "slippage_round_turn_ticks": 4,
+    "slippage_round_turn_usd": 20.0,
+    "fill_resolution": "Standard",
+    "fill_resolution_note": "NT8 Strategy Analyzer 'Order fill resolution' = Standard on 1-minute bars (no secondary series). Why: every strategy order is a managed Enter*/Exit* call with no price argument, evaluated OnBarClose at HH:00/HH:30 checkpoints (no touch-triggered order), so intrabar High/Low ordering does not decide entries/exits. Fill assumed at the next bar's open (INFERRED). Limitation every backtest report must carry: 'Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.' See DECISIONS.md D-2026-10-30-A.",
+    "total_cost_per_round_turn_usd": 22.96,
+    "total_cost_per_round_turn_ticks": 4.592,
+    "total_cost_breakdown_note": "22.96 = 2.96 commission + 20.00 slippage (4 ticks x 5.00). In ticks: 0.592 commission-equivalent + 4.0 slippage = 4.592 ticks round-turn."
$ python3 -c "print(2*5.0, 4*5.0, 2.96+20.0, 2.96/5.0+4.0)"
10.0 20.0 22.96 4.592
$ python3 -I -c "...consistency..."
True True
$ git diff DECISIONS.md   (hunk header; full entry is the 48 '+' lines, read back in the build session)
@@ -241,3 +241,51 @@
$ git diff DECISIONS.md | /usr/bin/grep -c '^-[^-]'
0
$ void byte-check (DECISION_LOG.md:347 vs DECISIONS.md D-2026-10-30-A)
True f9144cb50aab2885e28daecefb4c3e80a900963769bf396d92c3318629884a79 f9144cb50aab2885e28daecefb4c3e80a900963769bf396d92c3318629884a79
$ awk '/^## 2026-10-30 — D-2026-10-30-A/{f=1} f' DECISIONS.md | wc -l
      45
$ shasum -a 256 docs/reports/evidence/2026-10-30-run3-strategy-analyzer-summary.webp
8787483dcb41fbc0d52c023faeb32ff3606075a8fa518126749b1a4da90eac55  docs/reports/evidence/2026-10-30-run3-strategy-analyzer-summary.webp
$ git diff MANIFEST.md | /usr/bin/grep -c '^-[^-]'
0
$ git diff --stat MANIFEST.md
 MANIFEST.md | 11 +++++++++++
$ git status --short -- DECISIONS.md config/backtest-cost-model.json MANIFEST.md docs/reports/2026-10-30-zyd-worker1-build.md
 M DECISIONS.md
MM MANIFEST.md
 M config/backtest-cost-model.json
```
(`tail -n 12 MANIFEST.md` output: the last pre-existing row `/docs/reports/2026-08-07-f4-mffu-compliance-evidence.md` followed by the 11 new rows, in the order listed in the brief. Long rows elided here to keep this report compact; re-run to see them.) The schema_note / old fill note in the diff are elided with "..." in this report only; the diff was read in full in the session.

## Deviations from this brief (with reason)
1. Webp row Type = `Asset`, not `Evidence`. The brief also said to use the existing Type vocabulary; `Evidence` is not in it, and `Asset` is the type used for the existing PNG screenshot capture (MANIFEST :109). The word "Evidence:" opens the Purpose cell.
2. Cost-model UPDATE ROW Date Created = `2026-07-15` (the file's real creation date, matching row :96); the update date 2026-10-30 is in the Purpose cell. Swap if the manager prefers the row date.
3. `/docs/reports/2026-10-30-zyd-f3-artifact.md` row added as briefed, but the file does NOT exist yet (the manager has to write it). Until it does, that row points at a missing file.
4. (c) residual risks: same-bar exit+reverse and early-close days are labelled CANNOT-DETERMINE-STATICALLY, INFERRED, which follows fact 6's grouping. The brief listed them without a label.

## Self-grade limits
- I did not observe NT8 behaviour. Every OBSERVED/REPORTED/INFERRED label is copied from the cited rows or reports; none was upgraded.
- The quote of the bead premise is elided ("enters on band-touch … INTRABAR events"). The full bead text was checked via `bd show`.
- This report shows the DECISIONS diff only as its hunk header plus the line count. A grader should re-run `git diff DECISIONS.md` and read the full entry.
- Not checked: whether the Python MC or SHM code reads `fill_resolution` or depends on the exact old values. S6 is listed at the decision level only.

Result: PASS
