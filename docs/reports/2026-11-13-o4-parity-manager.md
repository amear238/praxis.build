# 2026-11-13 o4-parity: manager report

## Task
Unit 2026-11-13-o4-parity, bead Praxis_build-yra, rubric O4. Master under D-2026-11-08-D D1, DECISION_LOG 2026-11-13T05:45:00Z. Draft one DECISIONS.md entry, D-2026-11-13-A, answering both O4 questions. Add one MANIFEST row for it and one for this report. Nothing staged and nothing committed by this unit.

## Rubric criteria addressed
O4, plus standing criteria S1, S2, S4, S6 and S13.

```
$ sed -n 116,121p specs/SPEC_RUBRIC.md
### O4 — Backtest-vs-live configuration parity
Deviation C permits reverse-and-re-enter. Breakers #2 and #3 cap trades and end
the session after two consecutive losers. Block 4's gate compares live to
backtest within ±15% win rate and ±25% average trade P&L. **Required:** a
written statement of whether the Block 2 backtest runs with breakers applied,
```

## Manager's recommendation
Run both series from one trade list. The with-breakers series is #2 and #3 applied after the run, by a CONDITIONAL rule with a void clause. It is the only series that is graded, for the Block 2 gates and for the Block 4 ±15% / ±25% gate. The without series is kept as a record and is never graded. The entry adopts this option as decided by master under D-2026-11-08-D D1, changeable by Amear. Basis: Amear's R-VN3-5 and R-1104-3 point at breakers on (quoted in the entry at DECISIONS.md:512 and :761), and with no breakers in the code the without-only option leaves the gate structurally unmeetable:

```
$ grep -c -i -E "MaxTrades|TradeCount|tradesToday|consecutive|loser|LossStreak" ninjascript/PraxisNoiseAreaBreakout*.cs
ninjascript/PraxisNoiseAreaBreakout.cs:0
ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:0
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:0
```

## Workers dispatched
| id | mode | outcome |
|---|---|---|
| worker1 | ADVERSARIAL | see Adversarial findings |

## Process log
I read the sources and wrote the entry myself, because it is a pure doc edit. A single adversary then checked it. One finding came from the brief: it names a "Deviation C entry in DECISIONS.md", but no such entry exists. The entry records this and cites the ledger row instead:

```
$ grep -n -F "Deviation C" DECISIONS.md | cut -c1-40
511:- **O4 criterion** (`specs/SPEC_RUBR
2072:**S6 cross-block (from topology doc
2401:- Deviation C: no DECISIONS.md entr
2403:- Topology `docs/specs/2026-11-10-l
```

## Verification evidence (command output)

```
$ grep -n -F "## 2026-11-13 — D-2026-11-13-A" DECISIONS.md
2389:## 2026-11-13 — D-2026-11-13-A: Backtest-vs-live breaker parity (rubric O4; master under D-2026-11-08-D D1)
```

```
$ sed -n '2389,2416p' DECISIONS.md | wc -l
      28
```

```
$ sed -n '2389,2416p' DECISIONS.md
## 2026-11-13 — D-2026-11-13-A: Backtest-vs-live breaker parity (rubric O4; master under D-2026-11-08-D D1)

**Status:** Decided by master under D-2026-11-08-D D1 (DECISION_LOG 2026-11-13T05:45:00Z), changeable by Amear. Not Amear's ruling. A written statement only (bead `Praxis_build-yra`). Parts marked CONDITIONAL rest on a mechanism nobody has observed and carry a void clause.

**Decision 1: the Block 2 backtest runs both, and is graded with breakers.** Every Block 2 run yields two series from one trade list. The *without* series is the raw list as the strategy emits it (reverse-and-re-enter, 16:00 flat, no trade cap, no loser stop). The *with* series is that list after breakers #2 and #3 are applied to it after the run, Mac-side, by the rule below. Every Block 2 pass-gate value (arm (a) gates 1-5; arm (b) gates 1-6 and PBO) is computed on the with series, the version closest to live (R-VN3-5, R-1104-3). The without series is a record of what the breakers cost or saved; it is never graded. The 2026-11-01 runs are without-series records only.

**Decision 1 rule (CONDITIONAL).** Per session, trades are taken in entry order; a trade is one entry, and a reversal is the close of one trade plus the entry of the next. A reversal is processed close leg first: the closed trade's result is counted, then the entry leg meets the gate. #2: once the session's entry count reaches the #2 maximum in the Phase 3 spec at run time, every later entry is dropped. #3: once two consecutive closed trades are losers, every later entry is dropped; a loser is L as A3 and C5 (i) define it (by price), and a B trade is not a loser and breaks the run. A dropped entry leg's close leg still executes at the same bar and fill as in the raw list, so the trade it closes keeps its recorded exit. Removed trades leave the with series, stay in the without series, and are listed in a removed-trades table (count and net P&L per session) in the Block 2 report. Assumptions: (i) #2 and #3 gate new entries only and never block a closing order; (ii) in the backtest engine, a reversal's close leg fills at the price a stand-alone exit at that bar would; (iii) Block 3 builds live #2 and #3 to this same rule. Void if any one is observed false (for example, a built gate drops a whole reversal signal and leaves the position open, or a reversal's close fill differs from a stand-alone exit's fill at the same bar): the with series is then produced by re-simulating with the gate inside the bar loop, not by deleting trades, and an amending entry replaces this rule.

**Decision 2: how the Block 4 gate is satisfiable.** The gate compares Block 4 paper trades against the with series only: the with series of the arm whose parameters trade in Block 4 (R2: arm (a) unless an arm (b) set is adopted), over its full test span, at the cost model in force. Win rate is A3's quantity, computed identically on the with series and on all Block 4 paper trades; it passes if the two differ by at most 15 percentage points. Average trade P&L is the mean net P&L per trade per contract after commission and slippage; it passes if |paper mean − with mean| ≤ 0.25 × with mean, a positive with mean being presupposed (R5: net positive after costs). Trades the breakers removed enter neither term; on paper, entries #2 or #3 block make no trade and are logged, not counted. The gate is never re-run on the without series to rescue a failure. Reading "±15%" as percentage points and "±25%" as relative to the with mean is the master's, under D1, changeable.

**Sources (quoted byte-exact; DECISIONS.md lines are the working tree).**
- Phase 3 spec `docs/specs/2026-11-05-phase3-build-specification.md`: :98 "trade count hits daily max → disable order submission"; :99 "2 consecutive losers in one session → identical to max trades"; :124 "within ±15% win rate and ±25% average trade P&L"; Amendment 1 :205 "The system opens no new position from that flat time until 18:00 ET, when the next session begins."; :224 "The system's own trading is not disabled by this breaker"; :239 "New system entries between 15:00 and 16:00 are allowed under Rule F2-1, subject to breakers #1, #2, #3, #6, #7, #8 and #9."; :196 "SPECIFIED ONLY — zero implemented, zero tested, zero tested under failure".
- Deviation C: no DECISIONS.md entry carries that name (DECISIONS.md:511 only quotes the rubric). Its authority is DECISION_LOG.md:42: "positions/session = reverse & re-enter on opposite-band cross (NOT one-position/session)".
- Strategy `ninjascript/PraxisNoiseAreaBreakout.cs`: :32 "Positions/session = REVERSE & re-enter on an opposite-band cross"; :189 "if (mod >= CloseMod)" and :191 `FlattenAll("16:00 session flat");`. No trade cap and no loser-streak stop: zero hits for those terms in all three `PraxisNoiseAreaBreakout*.cs` (manager report). Implemented: reverse and 16:00 flat. Not implemented: #2, #3.
- Topology `docs/specs/2026-11-10-live-signal-topology.md`: :59 "Deviation C reverse-and-re-enter counts as an entry"; :58 "must never be blocked by a closed gate".
- Block 2 gates (DECISIONS.md): :1556 "GO requires arm (a) to pass."; :1746 "R3 amends Q8: arm (a) is judged on gates 1-5 (WFE not"; :1748 "O1 is discharged by R2 + R3 + A7."; A3 :1731 "W / (W + L + 0.5 x B), B = trade exited at its entry price." and :1733 `"within +/-15% win rate" check, computed identically on backtest` (pointer :1771); C5 :1836 "win/loss judged by price".
- Breakers on (DECISIONS.md): :512 "the backtest runs **with the breakers on, once they are built**"; :761 "when the time comes ask agaian."; R8 :1584 "#2 max 2 trades/day, #3 two-and-done" and :1588 "New values come back to Amear as".
- SHM-4, DECISIONS.md:189: "SHM-4: win-rate >15 ppts below backtest OR slippage >2 ticks/side worse, over a 20-trade window."
- R6 (read-only): DECISIONS.md:2350 (parked D-2026-11-12-B) "without breakers as design :116 (O4) states"; `bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md`:116 "First pass runs without breakers (no approved values; D6 E4) and says so; a breakers-on run waits for F2."
- After-the-run precedent: `docs/reports/2026-11-09-d6-drawdown-check-manager.md`:55 "every later trade that session is skipped" (breaker #1 sensitivity). Bead `Praxis_build-yra` (`bd show`): "the live-vs-backtest gate is structurally unmeetable."

**S6 cross-block.** Block 2: R2, R3, A7, A8 unchanged; gate values move to the with series; the values-spec §6 selection statistic is not changed, and whether arm (b) selects on the with series is left to the values-spec unit (named gap: selecting on one series and grading on the other). Block 3 breakers: assumption (iii) is a parity requirement on the later build, not an edit; it conflicts with topology :59 as written, which drops "the entry signal" whole, so a reversal sent as one SELL or BUY would leave the position open; #2 has no value (spec :98), #3's 2 is in spec :99, and R8 says both are redone. Block 4 gate: spec :124 and the 25-trade minimum unchanged; Decision 2 fixes only the series and the arithmetic. R6 parked research: its first pass is a without series by its own design and is no Block 4 reference; nothing in R6 changes. SHM: SHM-4 and SHM-5's "backtest" is read as the with series, bands unchanged; SHM-4 is one-sided over 20 trades, the Block 4 gate is two-sided over the paper period, and neither replaces the other. Amear's words: R-VN3-5 says "once they are built"; the with series simulates specified text before any breaker exists (named difference); D-2026-11-04-A (ii) re-ask binds before a High run, and this entry plans no run. #4: both series carry the strategy's 16:00 flat, so #4 does not split them; #5 (the session window) is an operator lockout with no effect on system trades; #1 and #6 to #9 are applied in neither series.

**Limits.** No code, no strategy file, no breaker value and no spec body is changed. The nine breakers stay SPECIFIED ONLY: zero implemented, zero tested; a with series is a simulation of specified text, not evidence that a breaker works. No with series exists yet, and none can be produced until #2 has an approved value (R8: PROPOSED; D2 (c) once real money is at stake); this entry sets none. It does not lift F3 or F4 and depends on neither: the fill resolution of any run is whatever F3 settles. It does not decide parity for #1 or #6 to #9, and does not mark O4 passed.

**S4 timing.** Written 2026-11-13, before the work it governs: no with series, no breaker code and no Block 4 paper trade exists. Chain: D-2026-11-08-D D1 → DECISION_LOG 2026-11-13T05:45:00Z (WHO: praxis-master).

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
```

```
$ sed -n '2389,2416p' DECISIONS.md | shasum -a 256
54ff8a84eacf234b8b0748a377f0f1eec839e18f945eff0e73f2e75f289eaf55  -
```

```
$ tail -n 2 MANIFEST.md
| /DECISIONS.md | Log | 3 | 2026-11-13 | AMENDMENT ROW (append-only registry). Unit 2026-11-13-o4-parity (rubric O4, bead Praxis_build-yra; master under D-2026-11-08-D D1, DECISION_LOG 2026-11-13T05:45:00Z): appends entry D-2026-11-13-A, "Backtest-vs-live breaker parity", stating that every Block 2 run yields a without-breakers series and a with-breakers series (#2 and #3 applied after the run, CONDITIONAL rule with a void clause), that Block 2 gates and the Block 4 ±15% / ±25% gate are computed on the with series only, and what happens to removed trades. No code, no breaker value, no spec body changed; breakers stay SPECIFIED ONLY; F3 and F4 untouched. |
| /docs/reports/2026-11-13-o4-parity-manager.md | Report | 3 | 2026-11-13 | Manager report for unit 2026-11-13-o4-parity (rubric O4, bead Praxis_build-yra; master under D-2026-11-08-D D1, DECISION_LOG 2026-11-13T05:45:00Z): source quotes, entry D-2026-11-13-A line range and sha256, manager's recommendation, S6 cross-block check, adversary grade line, index count. |
```

```
$ wc -l DECISIONS.md MANIFEST.md
    2416 DECISIONS.md
     468 MANIFEST.md
    2884 total
```

```
$ git diff --cached --name-only | wc -l
       1
```

```
$ git diff HEAD -- DECISIONS.md | grep -c '^-[^-]'
0
```

```
$ sed -n '2389,2416p' DECISIONS.md | grep -c -i -E 'verdict|COMMIT-INDEX|COMMIT-DIFF-SHA256|\.\.\.|…|@[a-z0-9-]+\.[a-z]'
0
```

Negative control for the quote check. The real quote matches; changing its arrow to ASCII gives no match:

```
$ grep -n -F "trade count hits daily max → disable order submission" docs/specs/2026-11-05-phase3-build-specification.md
98:2. Max trades per day — trade count hits daily max → disable order submission
$ grep -n -F "trade count hits daily max -> disable order submission" docs/specs/2026-11-05-phase3-build-specification.md; echo "exit=$?"
exit=1
```

Adversary grade line:

ADV_GRADE_BLOCK

## Adversarial findings
ADV_FINDINGS

## S6 cross-block check
The entry's S6 section is DECISIONS.md:2410:

```
$ sed -n 2410p DECISIONS.md | grep -o -E "Block 2|Block 3|Block 4|R6|SHM-4|R-VN3-5|D-2026-11-04-A|#4|#5" | sort | uniq -c
   2 #4
   1 #5
   1 Block 2
   1 Block 3
   3 Block 4
   1 D-2026-11-04-A
   1 R-VN3-5
   2 R6
   2 SHM-4
```

## Files staged
None by this unit. The index still holds the single pre-existing path (count pasted above). The working-tree edits are DECISIONS.md (append), MANIFEST.md (two rows), and this report plus docs/reports/2026-11-13-o4-parity-worker1.md.

Result: RESULT_LINE

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
