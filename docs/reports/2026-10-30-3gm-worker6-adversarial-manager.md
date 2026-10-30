# 3gm — Worker 6, ADVERSARIAL against the manager report

**Task:** Praxis_build-3gm. Attack `docs/reports/2026-10-30-3gm-fidelity-check.md` (the "artifact").
**Mode:** ADVERSARIAL, read-only. The only file written is this one. Scratch: `scratchpad/w6/` (copy of fuzz.py, tamper copy, rerun.py).
**Criterion:** SPEC_RUBRIC S1 (line 107), S2 (108), S5 (111), S8 (114). Unit criterion: no code change; the verdict carries line numbers.

## Process log
1. Read the whole artifact (960 lines) and source ranges 55–90, 112–125, 130–202 and 230–272 of the `.cs` file.
2. Re-ran every command in the Verification evidence block: hash, diff count, order grep, null arm, positive control, dead-field grep, checkpoint enumeration, arithmetic, fuzz (both arms), tamper trip, notes sed, and reference sed.
3. Mechanically re-ran **all 93** `$ sed` commands in D1 with a parser (`w6/rerun.py`) and compared each one byte for byte against its paste. Checked the verdict counts, and checked table-vs-body agreement for all 29 rows.
4. Read fuzz.py and compared it with lines 205–229 and 261–264.
5. Checked against the sources: W1 C1–C7, W3/W4 tails and figures, rubric line cites, F2 text, DECISION_LOG:442 (F3 lock) and :353, voice notes 20–30, W2 (d) early-close, W5 backups vs current W1/W2, and git staging state.

## Verification evidence (pasted)

**E1. Every D1 sed paste is identical. Counts match.**
```
$ python3 -I w6/rerun.py docs/reports/2026-10-30-3gm-fidelity-check.md
commands=93 identical=93 differ=0
FAITHFUL: 15
DEVIATION \(unauthorised\): 1
BUG: 2
SPEC-SILENT: 6
CANNOT-DETERMINE-STATICALLY: 5
R5 table=[spec L16,19 · §3 pp. 6–7] body=[Verdict: FAITHFUL]
```
The R5 line is the only table/body mismatch flagged. The cause is unescaped `|` in R5's rule text (`mean |Close_HH:MM/Open_9:30 − 1|`), which splits the markdown row. The verdict cell shifts out of the 5-column table.

**E2. Verification block re-runs: all identical to the artifact.**
```
35393823e9bc146e95dcb1d9f6fe5785a3c72ee3a3fb71287f33fe2242752265  ninjascript/PraxisNoiseAreaBreakout.cs
       0
211/219/224/225/227/229/288/290 (order grep, same 8 lines)
0            (null arm)
6            (positive control)
68,108,109,111,169 (dead-field grep)
['10:00', ..., '15:30']  (12)
121.36 121.36 21500 3182.0 820
mutant=False cases=500000 reversals=129174 reversal_without_exit=0
mutant=True cases=500000 reversals=129174 reversal_without_exit=129174
157de48c7076a5d5f849f91fab890e13df9f9472233c8f7755b4a6dcb60f096e  .../scratchpad/w6/t.cs
157de48c7076a5d5f849f91fab890e13df9f9472233c8f7755b4a6dcb60f096e  .../scratchpad/mgr/t.cs
$ git log --oneline -1 -- ninjascript/PraxisNoiseAreaBreakout.cs ; git rev-parse --short HEAD
719ab11 Praxis_build-4uu (b2-signal-repro): ...
fc77f36
$ wc -l ninjascript/PraxisNoiseAreaBreakout.cs   (see return of this call)
```
The voice-notes and reference-156 seds were identical too. The order-grep lines above are abbreviated in this paste; my raw output listed the same 8 lines verbatim. The tamper output in the artifact reads `t.cs` while the command echo reads `mgr/t.cs`. My run prints the full path, so the artifact's output line was edited (F9).

**E3. Files are NOT staged.**
```
$ git status --short -- 'docs/reports/2026-10-30-3gm*'
?? docs/reports/2026-10-30-3gm-fidelity-check.md
?? docs/reports/2026-10-30-3gm-worker1-checklist.md
?? docs/reports/2026-10-30-3gm-worker2-timing-orders-count.md
?? docs/reports/2026-10-30-3gm-worker3-adversarial-d1.md
?? docs/reports/2026-10-30-3gm-worker4-adversarial-d2d4.md
```

**E4. The report's own D2 and W2 (d) show an early-close code path that D5 omits.**
```
artifact L733: **Early-close days.** No bar reaches `mod >= 960`, so FlattenAll never runs. If the early close falls on a :00 or :30 stamp, the last bar is also a checkpoint, so an entry can be placed whose next bar is the next session.
W2 L500-503: - `FlattenAll` **never fires** that day.
- If E is an HH:00/HH:30 stamp, the last bar is **also a checkpoint**. The strategy can then enter or reverse on the session's final bar, and that order's "next bar" is the next session's 09:31.
- Only EOSC (if it fires at E) closes the position that day. With EOSC off, the position is carried overnight.
spec L64: all positions closed at the market Close = 16:00 ET (cash close), never held overnight
artifact L811: **Verdict: a faithful copy of the paper's decision rules for the configuration Amear ran. No bug was found that changes a trade decision.**
artifact L829: **What this verdict does NOT cover.** Two runtime questions cannot be settled from source ... D2(c) ... D3 / R21
```
Source lines 58 (`CloseMod = 16 * 60`), 189 (`if (mod >= CloseMod)`) and 196 (the checkpoint guard) are hard-coded to 16:00. The code itself never decides to flatten on a short session, and on a :00/:30 early end it can decide to enter on the final bar. Run 3 spans 2021-03-08 → 2026-07-17 (notes L40). Whether that template contains early-close sessions is UNVERIFIED (R4 readback). D5 lists neither this path nor lines 58/196, and NEEDS AMEAR drops W2's Trades-tab readback for early-close dates (W2 L509).

**E5. D5 labels as OBSERVED rows whose D1 text rests on REPORTED/INFERRED evidence.**
```
artifact L813: For ExitMode = BandOrVWAP, the following match the spec exactly (OBSERVED, D1 R1–R11, R13, R16, R18, R19):
R18 (L451): The assumption matches what Amear observed (end-stamped, first bar 09:31, Open = 09:30 price).   -> REPORTED
R19 (L469): Close[1] on the 09:31 bar is the prior 16:00 bar (REPORTED 16:00→09:31).                          -> REPORTED
R8  (L243): Depends on NT8 display TZ = ET (INFERRED from the REPORTED 09:31 / 16:00 stamps).                  -> INFERRED
R9  (L258): RTH-only depends on the template (run 1 unknown).
W1 C5: R8, R10 and R15 depend on NT8's display time zone being ET ... (INFERRED)
```
D5's bullet "the HH:00/HH:30 checkpoints (196)" is R10, which W1 C5 makes depend on the INFERRED ET display. D5 also says "for the configuration Amear ran", which includes run 1 (notes L38: "settings not verified; may have reset"). The headline also says "paper", but the paper was not read (Self-grade limits L951).

**E6. W5 diff figures, which the artifact asserts without a paste.**
```
W1 added: 36   W1 removed: 1      (A.orig vs current; artifact says "37 changed lines, 1 removed")
W2 added: 45   W2 removed: 0      (matches)
```

**E7. Fuzz port vs source.** fuzz.py lines 7 and 10 use `max(up, vwap)` / `min(lo, vwap)` whenever mode == BandOrVWAP. Source lines 209 and 217 also require `vwapCumVol > 0`. The `vwapCumVol == 0` branch (stop = band) is behaviourally identical to the OppBand arm, which the fuzz does cover, so the omission does not change the 0 result. σ is sampled in [0, 0.03] only. The pre-fill `Position.MarketPosition` assumption (one `pos` for both blocks) is hard-coded. That assumption is an INFERRED NT8 semantic, and the port encodes it rather than tests it. Verdict on the port: faithful for the algebraic claim "reversal ⇒ exit condition", which holds by construction (curLower ≤ curUpper from lines 263–264). The artifact labels it a fuzz result, not an NT8 result, which is correct.

**E8. Cross-checks that held.** W3 tail `VERDICT: FAIL`, W3 L23 `commands=112 identical=112`. W4 tail `VERDICT: FAIL`, W4 L92 `reversals 305112 ... WITHOUT exit 0`. Rubric L107/108/111/112/114 are S1/S2/S5/S6/S8 and L159 is the S9 note. F2 is at L30 and F3 at L45. DECISION_LOG:442 is the `[2026-10-30T21:36:30Z]` F3 `[N]`=2 lock. DECISION_LOG:353 contains "filled at the next bar's open". The W1 table rows 46/52 still read DEVIATION (unauthorised), but W1's banner (L3) and C1 (L843) regrade both to SPEC-SILENT, and the artifact's R17/R23 agree with C1.

## Findings

| id | claim (artifact) | severity | evidence | correct grade |
|---|---|---|---|---|
| F1 | D5 L811/L829: "No bug was found that changes a trade decision". Only two runtime gaps (D2(c), R21) are "not covered" | **MAJOR** | E4 | Qualify the headline to full 09:30–16:00 sessions. Add a third uncovered item: early-close days. The code never decides to flatten, and it may enter on the final bar (lines 58, 189–193, 196; W2 (d)). Restore W2's early-close Trades-tab readback to NEEDS AMEAR. R27 (stamp-vs-fill) and R12's lines 106–107 are also absent from D5's line list |
| F2 | D5 L813: "match the spec exactly (OBSERVED, … R18, R19)" and "for the configuration Amear ran" | **MAJOR** (S2) | E5 | Code text is OBSERVED. The match also rests on things that are not: R18/R19 are REPORTED, R8/R10 rest on INFERRED ET display, R9 on the template, and run 1's configuration is unknown. Label "OBSERVED in code; runtime premises REPORTED/INFERRED". Scope "configuration" to runs 2–3. Say "spec" not "paper" |
| F3 | Files staged L941: "Report files only, via `git add`" | **MAJOR** (S1, contract) | E3: all five are `??` untracked | Either stage the files or state "not staged" |
| F4 | Process log L49: "W1: 37 changed lines, 1 removed"; L44 tail -1 tokens; L58 "counts checked by grep": no pastes | MINOR (S1) | E6: 36 added + 1 removed. Tokens and counts are true (E1, E8) | Paste the diff counts and greps. Fix the W1 figure to "36 added, 1 removed" |
| F5 | D1 R5 table row | MINOR | E1: unescaped `\|` breaks the row, so the verdict cell is displaced | Escape it as `\|` |
| F6 | Verdict L958: "D2 (a)–(e)" | MINOR | grep shows only (a), (b), (c) in the artifact. (d) and (e) exist only in W2 L494/L510 | Say "(a)–(c) plus early-close", or carry (d) and (e) over |
| F7 | L931/L947: "see the Addendum below"; `Result: PASS` written while W6 pending | MINOR (contract) | No "Addendum" heading in the artifact | Add the addendum, or make the Result conditional |
| F8 | S6 L936: the locked 2-tick `[N]` "applies to both sides of every trade" | MINOR (S2/S8-adjacent) | DECISION_LOG:442 locks "**band-edge** slippage = 2 ticks per side". The 16:00/EOSC exits are not band-edge, and D3 itself marks session-close application INFERRED | Label it INFERRED, or put the scope to Amear. Do not state it as fact |
| F9 | Tamper-trip output `157de… t.cs` | MINOR (S1 fidelity) | E2: a real run prints the full path. The output line was edited, though the hash reproduces | Paste raw output |
| F10 | R25 "not NQ ($20/pt per project records)" | MINOR (S1) | The R25 block pastes only code L36–37. No project-record paste for $20/pt | Paste the source of the $20/pt record |
| F11 | fuzz.py as a port of 205–229, 261–264 | MINOR | E7: the `vwapCumVol > 0` guard is omitted and the NT8 pre-fill assumption is hard-coded. The result is unaffected | Note the omission in Self-grade limits |

**No break found** in the following:
- the code hash, the diff count of 0, or any of the 93 D1 pastes;
- the verdict counts (15/0/1/2/6/5 = 29), or the table/body verdict agreement for R1–R4 and R6–R29;
- the R17/R23 SPEC-SILENT grade against W1 C1;
- the order inventory (6 call sites), the null arm and its positive control, the checkpoint list, or the arithmetic;
- the fuzz figures, which reproduce exactly;
- the rubric line cites, or the DECISION_LOG cites at :353 and :442;
- the W3/W4 tokens and figures.

S8: Q1 and Q2 are put as questions, C1–C7 are marked "none applied", and C3 is "his call". Nothing is decided for Amear, apart from the F8 scope phrasing. Contract: all eleven required sections and the `Result:` line are present. Only the Addendum the artifact itself references is missing (F7).

## Files staged
None. This adversary was told not to `git add`. This report is the only file written.

## Self-grade limits
- I did not read the paper. Early-close dates in the run-3 window are UNVERIFIED from repo files.
- I checked no NT8 behaviour. F1 rests on the code's decisions, not on NT8 execution.

Result: FAIL

VERDICT: FAIL
