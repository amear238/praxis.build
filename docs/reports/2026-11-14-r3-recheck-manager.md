# 2026-11-14 R3 recheck — manager report (unit `2026-11-14-r3-recheck`, Amear's R4)

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## Summary (plain English, 1 MNQ; source labels below the table)

| strategy | stop rule as coded/written | max loss known before entry? | largest loss | longest losing run | worst day | most trades in a session |
|---|---|---|---|---|---|---|
| Noise-Area baseline (BandOrVWAP) | band/VWAP level, checked at HH:00/HH:30 bar closes, market exit | NO | −$542.40 | 10 | −$705.10 | 5 |
| Noise-Area OppBand | opposite-band level, same checkpoint check, market exit | NO | −$1,960.90 | 6 | −$1,894.80 | 2 (1 if same-timestamp reversals are merged) |
| Noise-Area Flat1559 | as baseline, plus a 15:59 flat | NO | −$542.40 | 10 | −$683.70 | 5 |
| Last-Half-Hour Momentum (retired) | none; time exit at 15:59 only | NO | −$555.40 | 10 | −$555.40 | 1 |
| Opening gap fade V2 (pre-screen) | stop = gap size in points, fixed at the 09:31 entry | YES, as written in a Python rule only | −$472.90 | 10 | −$472.90 | 1 |

Labels: NT8 rows = "Mac recomputation from the hand-run trade list, MNQ derived, not an MNQ run". Gap fade = "Mac recomputation from the Python pre-screen trade list, MNQ derived". The source of every figure in the table is pasted here, from three independent scripts (worker 1 `[7]`, manager spot-check, worker 2 table: 0 mismatches):
```
w1_out.txt [7]: PraxisNoiseAreaBreakout (baseline BandOrVWAP) | $-542.40 | 10 (2022-09-15..2022-09-26) $-802.00 | $-705.10 2022-10-13 | 5
w1_out.txt [7]: PraxisNoiseAreaBreakout_OppBand | $-1,960.90 | 6 (2021-11-17..2021-11-24) $-1,429.40 | $-1,894.80 2025-04-08 | 2
w1_out.txt [7]: PraxisNoiseAreaBreakout_Flat1559 | $-542.40 | 10 (2022-09-15..2022-09-26) $-815.50 | $-683.70 2025-04-16 | 5
w1_out.txt [7]: PraxisLastHalfHourMomentum (retired) | $-555.40 | 10 (2023-08-29..2023-09-12) $-339.50 | $-555.40 2025-03-04 | 1
w1_out.txt [7]: Gap fade V2 (pre-screen) | $-472.90 | 10 (2026-03-11..2026-04-10) $-1,951.50 | $-472.90 2026-07-16 | 1
mgr_spot.py: BASE: n=1190 losers=712 largest=-542.40@2026-06-25 avgloss=-97.26 streak=10 2022-09-15..2022-09-26 worstday=-705.10@2022-10-13 maxtrades/session=5 days_with_trade=792 avg=1.503 maxMAE=747.50
mgr_spot.py: OPPBAND: n=810 losers=346 largest=-1960.90@2025-04-08 avgloss=-232.61 streak=6 2021-11-17..2021-11-24 worstday=-1894.80@2025-04-08 maxtrades/session=2 days_with_trade=792 avg=1.023 maxMAE=2223.00
mgr_spot.py: FLAT1559: n=1190 losers=715 largest=-542.40@2026-06-25 avgloss=-96.45 streak=10 2022-09-15..2022-09-26 worstday=-683.70@2025-04-16 maxtrades/session=5 days_with_trade=792 avg=1.503 maxMAE=747.50
mgr_spot.py: LHHM: n=1304 losers=694 largest=-555.40@2025-03-04 avgloss=-71.82 streak=10 2023-08-29..2023-09-12 worstday=-555.40@2025-03-04 maxtrades/session=1 days_with_trade=1304 avg=1.000 maxMAE=694.00
mgr_spot.py: GAPFADE_V2: n=648 losers=324 largest=-472.90@2026-07-16 avgloss=-161.64 streak=10 2026-03-11..2026-04-10 worstday=-472.90@2026-07-16 maxtrades/session=1 days_with_trade=648 avg=1.000 maxMAE=471.00
worker2 :245: `=` means the artifact's value equals mine. **Figure mismatches: 0.**
```
Largest loss as % of balance. This is an illustration only: the percentage R3 uses has not been decided, and neither has which balance it is taken from (Q3).
```
w1_out.txt :43/:44 baseline 1.085% / 0.362% | :66/:67 OppBand 3.922% / 1.307% | :89/:90 Flat1559 1.085% / 0.362% | :112/:113 LHHM 1.111% / 0.370% | :155/:156 gap fade 0.946% / 0.315%   (of $50,000 / of $150,000)
```

## Task
For each of the five strategies, answer R3 (`docs/reports/2026-11-14-voice-notes-pivot.md` :18-:24) per R4 (:26-:29) and handoff step 3 (:56): (a) stop logic from source, plus YES/NO; (b) loss figures at 1 MNQ; (c) the MNQ conversion; (d) a verdict line; and trades per session for R7. No percentage, cap or keep/drop view is offered (S8; Q2, Q3, Q6 are Amear's).

## Rubric criteria addressed
S1, S2, S8 and S13 (quoted in the brief, from `specs/SPEC_RUBRIC.md`).

## Workers dispatched
| id | mode | outcome |
|---|---|---|
| worker 1 | BUILD, `/tmp/praxis-r3/w1_r3.py` sha256 `8a8251cb…a45a0c` | all figures produced; verdicts proposed; three MED grading defects (below) |
| worker 2 | ADVERSARIAL, own script `/tmp/praxis-r3/w2_adv.py` sha256 `cc29f8e6…10ffb8` | 0 figure mismatches; Result FAIL on grading (F1-F3 MED, 7 LOW) |

## Process log
1. Read the rubric, voice notes, D6 manager report, results report and the four `.cs` sources. Wrote the manager spot-check `/tmp/praxis-r3/mgr_spot.py` before either worker returned.
2. Dispatched worker 1. Re-ran its script myself and diffed the output against its file. Dispatched worker 2 without worker 1's script or reasoning. Re-ran both of worker 2's scripts.
3. Worker 1 added a late "Limits" note after worker 2 had started. No figure changed. Its :335 reads: `A whole-disk find / -name 'trades_V*' -not -path '*/System/*' finished after the report was first written (background task, exit 0). It found exactly two files, both trades_V2_full.csv ...`
4. Worker 2's first run wrote `scripts/wf/__pycache__`. Worker 2 deleted it (`ls` output below). The worker cap is two, so worker 1's report was not re-issued. Its three MED defects are corrected in this report, and worker 1's file still carries them.

## Verification evidence
Inputs: the committed grid CSVs hash the same as the results report :29-:32, and line :1063 reads the same at HEAD:
```
421c44e6…0534bd  docs/reports/evidence/2026-11-01-ninjatrader-grid-0710am.csv   (w1_out: 07-10 AM match=True; likewise 0757am, 0759am, 0800am match=True)
LINE1063_SAME_AT_HEAD
Fees: apply MFFU's published round trip — NQ $4.68, MNQ $1.90
```
(a) Stop logic. No resting stop-order API in any NinjaScript source; Noise-Area exits act only at checkpoints, at market:
```
ninjascript/PraxisNoiseAreaBreakout.cs:0  PraxisLastHalfHourMomentum.cs:0  _Flat1559.cs:0  _OppBand.cs:0   (grep -c SetStopLoss|SetProfitTarget|SetTrailStop|StopMarket)
ninjascript/PraxisNoiseAreaBreakout.cs:196:  bool isCheckpoint = (Time[0].Minute == 0 || Time[0].Minute == 30) && mod > OpenMod && mod < CloseMod;   (also OppBand :219, Flat1559 :234)
ninjascript/PraxisNoiseAreaBreakout.cs:208-209: double stop = (ExitMode == PraxisNoiseExitMode.BandOrVWAP && vwapCumVol > 0) ? Math.Max(curUpper, curVwap) : curUpper;
ninjascript/PraxisNoiseAreaBreakout.cs:211:  ExitLong("XL", "");     (OppBand :235, Flat1559 :249)
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:232-233: ... : (ExitMode == PraxisNoiseExitMode.OppBand ? curLower : curUpper);
ninjascript/PraxisLastHalfHourMomentum.cs:206: if (mod >= FlatMod)   :209: ExitLong("LHFlat1559", "LHMomLong");
research/search-loop/c1-gap-fade/RULES.md:20: - Stop: distance = |O - PC|. Short stop = O + |O - PC|; long stop = O - |O - PC|. Hit when short high >= stop, long low <= stop. Exit fill = stop worsened by 0.5 points.
w1_out [5]: stop distance |O-PC| points: min 28.75 | median 80.125 | max 234.5
w1_out [5]: stop distance at 1 MNQ ($2/pt, from O): min $57.50 | median $160.25 | max $469.00
```
Kinds of stop. Noise-Area: a band- or VWAP-based level, recomputed through the day and checked only at the half-hour bar close with a market exit, so the loss is not capped. LHHM: no stop at all. Gap fade: a price stop in points, fixed at the 09:31 entry. Its size is set by the gap, so it differs every day.

(b)/(R7) Per-session figures. Trades per session with at least one trade: baseline 1.503, OppBand 1.023, Flat1559 1.503, LHHM 1.000, gap fade 1.000 (from mgr_spot above). Per calendar session:
```
w1_out :123-:126  baseline 1190 / N 1352 = 0.8802 | OppBand 810 / N 1352 = 0.5991 | Flat1559 1190 / N 1352 = 0.8802 | LHHM 1304 / N 1352 = 0.9645
w1_out :162       trades / summary.json trading_days = 648 / 1354 = 0.4786
```
(c) MNQ conversion. MNQ net = (NQ Profit + NQ Commission) / 10 − $1.90. Slippage is not added again because it is already in the fill prices: 1 NQ tick = 0.25 pt, which is $0.50 at MNQ, so 2 ticks/side = $2.00 round trip inside gross/10. The row checks and the worked trade:
```
w1_out :25/:54/:77/:100  Commission != $2.96: 0 rows | Profit != round((exit-entry)*side*20 - 2.96, 2): 0 rows []
    points = (16297.25 - 16270.25) x -1 = -27.00
    NQ gross = Profit + Commission = -542.96 + 2.96 = -540.00  (= points x 20 = -540.00)
    MNQ net = NQ gross / 10 - 1.90 = -540.00 / 10 - 1.90 = -55.90
w1_out [5]  mnq_net != points*2 - 1.90: 0 []      (gap fade; fills carry 0.5 pt worsening: "entry_fill != O worsened 0.5 pt: 0 []")
```
Slippage by exit type is now OBSERVED for every exit type, not only for entries and session-close exits. Worker 2 tested it against the bar file. Of all fills, 384 carry less than 2 ticks, and the worst-loss trades carry the full 2 ticks:
```
fills 8988 less_than_2_ticks 384
OppBand trade 627 MNQ -1960.90 | entry L px 19483.25 ref 19482.75 slip 2t ; exit XL px 18503.75 ref 18504.25 slip 2t
Baseline (NoiseArea BandOrVWAP) trade 1182 MNQ -542.40 | entry S px 29316.25 ref 29316.75 slip 2t ; exit XS px 29586.50 ref 29586 slip 2t
```
Largest MAE at 1 MNQ is in the mgr_spot lines above (maxMAE): 747.50, 2223.00, 747.50, 694.00 and 471.00. For the NT8 lists that is NT8's MAE/10 (method UNVERIFIED, D6 :54); for the gap fade it is mae_points × $2, which is bar-based.

Re-runs and negative test:
```
diff w1_out.txt mgr_rerun_w1.txt -> only line 1 (run timestamp) differs
W2EXTRA_RERUN_IDENTICAL
W2_RERUN_IDENTICAL_EXCEPT_TIMESTAMP
ls: /Volumes/Sensidine/Praxis.build/scripts/wf/__pycache__: No such file or directory
MUTANT_BASE: n=1190 losers=712 largest=-635.40@2022-10-13 avgloss=-97.40 ... worstday=-805.10@2022-10-13     (one row Profit -$5337.96 -> -$6337.96)
REAL_BASE:   n=1190 losers=712 largest=-542.40@2026-06-25 avgloss=-97.26 ... worstday=-705.10@2022-10-13
```

## (d) Verdict lines
- Noise-Area baseline: **Fails R3 as tested.** No per-trade maximum loss. The level is checked only at HH:00/HH:30 closes and exited at market. The largest NT8 MAE is $747.50 at 1 MNQ.
- Noise-Area OppBand: **Fails R3 as tested.** Same as the baseline. Its largest MAE is $2,223.00 and its largest loss −$1,960.90 at 1 MNQ.
- Noise-Area Flat1559: **Fails R3 as tested.** Same as the baseline.
- Last-Half-Hour Momentum: **Fails R3 as tested.** No stop of any kind; only the holding time is bounded.
- Gap fade V2: **Meets R3's structure, size undecided.** The evidence level is SPECIFIED, plus a pre-screen simulation. It was never a platform order and never tested under failure. Whether a fill past the stop level still counts as the cost of the trade is Amear's Q2, and this verdict does not answer it. The other variants are also out of scope here: V2 was "for the record, not selected" (`summary.json` selection: `{"qualifying": [], "variant": "V2", "label": "for the record, not selected"}`).

## Adversarial findings (worker 2; dispositions are the manager's)
- F1 MED (S1/S2): worker 1 called slippage "already in fills" for every exit type. The cited lines cover only entries and session-close exits. Disposition: worker 2's bar-file test (above) now observes it on every exit type, as "up to 2 ticks". The figures are unchanged.
- F2 MED (S2): in the gap fade, "no loss exceeded the stop" is true by construction. Disposition: carried, with the overshoot evidence below. The fill model books every stop at the level plus 0.5 pt, yet the bar traded past the stop on 273 of 286 stop exits:
```
stop exits 286 | overshoot >0: 273 | >=5pt: 113 | >=10pt: 52 | max 45.50
max pre-open bound (0.008*PC + 1pt)*2 + 1.90 over trades = 497.92 ; trades whose realized loss exceeds own pre-open bound: 0
```
- F3 MED (S8): worker 1 labelled Q2 as "the percentage". Q2 actually asks whether a fill past the level is still the cost of the trade (voice notes :65). Disposition: corrected in this report. Q2 is not answered here.
- LOW items:
  - OppBand's most trades in a session falls from 2 to 1 if same-timestamp reversals are merged.
  - OppBand's worst-summed losing run is larger than the sum of its longest run (−$1,429.40, w1_out [7] above).
  - The `Exit on session close` exits are NT8's backstop. The source comment calls it that: the strategy's own flat is the primary exit.
```
w2_extra [X4] OppBand handoffs 18 [...] | max trades/session 2 | max exposure-episodes/session (reversal legs merged) 1
w2_out.txt:51: (worst-summed run by trade number: length 2 trades 626..627 2025-04-07..2025-04-08 sum -2415.80)
ninjascript/PraxisNoiseAreaBreakout.cs:108: IsExitOnSessionCloseStrategy = true;   // backstop; explicit 16:00 flat is primary
```
  - The remaining LOW items are in `docs/reports/2026-11-14-r3-recheck-worker2.md` :353-:382.

Filer's note, not a ruling: a rerun under R3 would need a stop placed as a resting order at entry, a stop distance converted to contracts from the account percentage (once Amear sets it), a fill model that books a gap-through at the bar's price instead of at the level, and the reporting of R7/R8 figures (most setups, average setups, worst day at that cost).

## S6 cross-block check
This unit is read-only research and introduces no deviation, so S6 has nothing to test here. R3 and R8 will touch breaker #1 (daily loss) and the Block 3 breaker specs once Amear sets the numbers. Nothing in those specs was changed or graded in this unit.

## Files staged
None. Untracked reports: this file, `-worker1.md` and `-worker2.md`. Scratch files are under `/tmp/praxis-r3/`. Index state, from `git diff --cached --name-status`: `A docs/reports/evidence/2026-10-28-mffu-davi-reply.png`. That was the only staged entry at session start, so this unit added nothing.

Gate note for the master: `scripts/gate-manager-output.sh` grades only the newest `docs/reports/*.md`. It blocked while that file was the voice notes and then worker 2's report, both of which contain the word it rejects inside quotations of Amear's ruling.

Result: PASS
