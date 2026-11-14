# O4 reduce, worker 1: adversarial check of D-2026-11-13-A

## Task
Cold adversarial check of DECISIONS.md lines 2389-2416, entry D-2026-11-13-A (the last entry in the file), against rubric O4, using checks (a) to (f) from the brief. I edited no file other than this report. I staged nothing and ran no git write command.

## Mode
ADVERSARIAL. Read-only apart from this report.

## Criterion
Rubric O4, `specs/SPEC_RUBRIC.md:117-122` (re-read this session, block 2 below): "Deviation C permits reverse-and-re-enter. Breakers #2 and #3 cap trades and end the session after two consecutive losers. Block 4's gate compares live to backtest within ±15% win rate and ±25% average trade P&L. **Required:** a written statement of whether the Block 2 backtest runs with breakers applied, without them, or both — and how the Block 4 gate is satisfiable if they differ."

## Process log
1. Read the entry. My first call ran under zsh and failed on an `echo ===` separator (the `(eval)` error below). The `sed` output before that error is complete. Lines that carry the standing sentence are replaced with `[standing sentence cut]` in every pasted output, so the sentence appears in this report only once, as the last line.
2. Line map, from the `L+2384 n` prefix (file line = 2384 + n): 2389 heading, 2391 Status, 2393 Decision 1, 2395 Decision 1 rule, 2397 Decision 2, 2399 Sources heading, 2400 to 2408 Sources bullets, 2410 S6, 2412 Limits, 2414 S4 timing, 2416 standing sentence.
3. Ran the diff against the pre-edit copy and re-read O4 in the rubric (block 2).
4. Checked every quoted string in the entry at its cited line with a script that echoes each literal command and then runs it (block 3).
5. Read the context behind each attribution and mechanism claim (blocks 4 to 8).

## Verification evidence

Block 1: reading the entry (zsh; the error at the end is from the separator, not from `sed`).
```
$ sed -n '2385,2420p' /Volumes/Sensidine/Praxis.build/DECISIONS.md | cat -n | sed 's/^/L+2384 /'; echo ===; [cut: rest of the compound command]
L+2384      1	**S6 cross-block.** Touches Block 0 (Step 0.8, commit `2582531`, whose body records "Webhook->validate->file write (/tmp/praxis-signals on n8n host)"; nothing in Block 0 is re-graded), Block 1 (the reach of the 2026-07-15 sign-off), Block 2 (`docs/specs/2026-11-05-phase3-build-specification.md` :180, "When Block 1’s milestone is hit, Block 2 starts. Not before."), Block 4 and Block 5 (where D-2026-07-09-D places the deferred ingress question; nothing is moved there) and rubric F1 / the live-signal topology `docs/specs/2026-11-10-live-signal-topology.md` (:112, cross-reference only). One conflict, recorded, not resolved: the Phase 3 spec's Block 1 milestone (:60, "fire a fake signal from TradingView") includes TradingView ingress; the milestone signed off on 2026-07-15 did not; the sign-off records "Block 2 (Backtesting) entry condition now satisfied" (:175). This entry records the gap; it does not re-grade the sign-off, re-open Block 1 or stop Block 2 (decided by master under D-2026-11-08-D D1, DECISION_LOG 2026-11-12T21:41Z, changeable by Amear). Evidence: `docs/reports/2026-11-12-o3-block1-scope-evidence-2.md` (S6 section).
L+2384      2	
L+2384      3	[standing sentence cut]
L+2384      4	
L+2384      5	## 2026-11-13 — D-2026-11-13-A: Backtest-vs-live breaker parity (rubric O4; master under D-2026-11-08-D D1)
L+2384      6	
L+2384      7	**Status:** Decided by master under D-2026-11-08-D D1 (DECISION_LOG 2026-11-13T05:45:00Z), changeable by Amear. Not Amear's ruling. A written statement only (bead `Praxis_build-yra`). Parts marked CONDITIONAL rest on a mechanism nobody has observed and carry a void clause.
L+2384      8	
L+2384      9	**Decision 1: the Block 2 backtest runs both, and is graded with breakers.** Every Block 2 run yields two series from one trade list. The *without* series is the raw list as the strategy emits it (reverse-and-re-enter, 16:00 flat, no trade cap, no loser stop). The *with* series is that list after breakers #2 and #3 are applied to it after the run, Mac-side, by the rule below. Every Block 2 pass-gate value (arm (a) gates 1-5; arm (b) gates 1-6 and PBO) is computed on the with series, the version closest to live (R-VN3-5, R-1104-3). The without series is a record of what the breakers cost or saved; it is never graded. The 2026-11-01 runs are without-series records only.
L+2384     10	
L+2384     11	**Decision 1 rule (CONDITIONAL).** Per session, trades are taken in entry order; a trade is one entry, and a reversal is the close of one trade plus the entry of the next. A reversal is processed close leg first: the closed trade's result is counted, then the entry leg meets the gate. #2: once the session's entry count reaches the approved #2 maximum, every later entry is dropped. #3: once the session's run of consecutive losing closed trades reaches the approved #3 count, every later entry is dropped. Neither value is approved for the automated book (R8, A6); spec :98 gives #2 no number and :99 gives #3 as 2. A loser is L as A3 and C5 (i) define it (by price). That a B trade is not a loser and breaks the run is the master's reading under D1, changeable; R4's "a break-even trade counts as" half a loss (DECISIONS.md:1560-1561) scores win rate, not the #3 run (named difference). A dropped entry leg's close leg still executes at the same bar and fill as in the raw list, so the trade it closes keeps its recorded exit. Removed trades leave the with series, stay in the without series, and are listed in a removed-trades table (count and net P&L per session) in the Block 2 report. Assumptions: (i) #2 and #3 gate new entries only and never block a closing order; (ii) in the backtest engine, a reversal's close leg fills at the price a stand-alone exit at that bar would; (iii) Block 3 builds live #2 and #3 to this same rule. Void if any one is observed false (for example, a built gate drops a whole reversal signal and leaves the position open, or a reversal's close fill differs from a stand-alone exit's fill at the same bar): the with series is then produced by re-simulating with the gate inside the bar loop, not by deleting trades, and an amending entry replaces this rule and Decision 2's paper-side counting.
L+2384     12	
L+2384     13	**Decision 2: how the Block 4 gate is satisfiable (CONDITIONAL on assumptions (i) and (iii) above; same void clause).** The gate compares Block 4 paper trades against the with series only: the with series of the arm whose parameters trade in Block 4 (arm (a), which R2 says GO requires; that an adopted arm (b) set would replace it is the master's reading under D1, changeable), over its full test span, at the cost model in force. Win rate is A3's quantity, computed identically on the with series and on all Block 4 paper trades; it passes if the two differ by at most 15 percentage points. Average trade P&L is the mean net P&L per trade per contract after commission and slippage; it passes if |paper mean − with mean| ≤ 0.25 × with mean, a positive with mean being presupposed (R5: net positive after costs). Trades the breakers removed enter neither term; on paper, entries #2 or #3 block make no trade and are logged, not counted. The gate is never re-run on the without series to rescue a failure. Reading "±15%" as percentage points and "±25%" as relative to the with mean is the master's, under D1, changeable.
L+2384     14	
L+2384     15	**Sources (quoted byte-exact; DECISIONS.md lines are the working tree).**
L+2384     16	- Phase 3 spec `docs/specs/2026-11-05-phase3-build-specification.md`: :98 "trade count hits daily max → disable order submission"; :99 "2 consecutive losers in one session → identical to max trades"; :124 "within ±15% win rate and ±25% average trade P&L"; Amendment 1 :205 "The system opens no new position from that flat time until 18:00 ET, when the next session begins."; :224 "The system's own trading is not disabled by this breaker"; :239 "New system entries between 15:00 and 16:00 are allowed under Rule F2-1, subject to breakers #1, #2, #3, #6, #7, #8 and #9."; :196 "SPECIFIED ONLY — zero implemented, zero tested, zero tested under failure".
L+2384     17	- Deviation C: no DECISIONS.md entry is titled Deviation C (DECISIONS.md:511 quotes the rubric; :2072 names it in an S6 list). Its authority is DECISION_LOG.md:42: "positions/session = reverse & re-enter on opposite-band cross (NOT one-position/session)".
L+2384     18	- Strategy `ninjascript/PraxisNoiseAreaBreakout.cs`: :32 "Positions/session = REVERSE & re-enter on an opposite-band cross"; :189 "if (mod >= CloseMod)" and :191 `FlattenAll("16:00 session flat");`. No trade cap and no loser-streak stop: zero hits for `MaxTrades|TradeCount|tradesToday|consecutive|loser|LossStreak` in all three `PraxisNoiseAreaBreakout*.cs` (`docs/reports/2026-11-13-o4-parity-manager.md`). Implemented: reverse and 16:00 flat. Not implemented: #2, #3.
L+2384     19	- Topology `docs/specs/2026-11-10-live-signal-topology.md`: :59 "Deviation C reverse-and-re-enter counts as an entry"; :58 "must never be blocked by a closed gate".
L+2384     20	- Block 2 gates (DECISIONS.md): :1556 "GO requires arm (a) to pass."; :1746 "R3 amends Q8: arm (a) is judged on gates 1-5 (WFE not"; :1748 "O1 is discharged by R2 + R3 + A7."; A3 :1731 "W / (W + L + 0.5 x B), B = trade exited at its entry price." and :1733 `"within +/-15% win rate" check, computed identically on backtest` (pointer :1771); C5 :1836 "win/loss judged by price".
L+2384     21	- Breakers on (DECISIONS.md): :512 "the backtest runs **with the breakers on, once they are built**"; R8 :1584 "#2 max 2 trades/day, #3 two-and-done" and :1588 "New values come back to Amear as".
L+2384     22	- SHM-4, DECISIONS.md:189: "SHM-4: win-rate >15 ppts below backtest OR slippage >2 ticks/side worse, over a 20-trade window."
L+2384     23	- R6 (read-only): DECISIONS.md:2350 (parked D-2026-11-12-B) "without breakers as design :116 (O4) states"; `bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md`:116 "First pass runs without breakers (no approved values; D6 E4) and says so; a breakers-on run waits for F2."
L+2384     24	- After-the-run precedent: `docs/reports/2026-11-09-d6-drawdown-check-manager.md`:55 "every later trade that session is skipped" (breaker #1 sensitivity). Bead `Praxis_build-yra` (`bd show`): "the live-vs-backtest gate is structurally unmeetable."
L+2384     25	
L+2384     26	**S6 cross-block.** Block 2: R2, R3, A7, A8 unchanged; gate values move to the with series; the values-spec §6 selection statistic is not changed, and whether arm (b) selects on the with series is left to the values-spec unit (named gap: selecting on one series and grading on the other). Block 3 breakers: assumption (iii) is a parity requirement on the later build, not an edit; it conflicts with topology :59 as written, which drops "the entry signal" whole, so a reversal sent as one SELL or BUY would leave the position open; neither #2 nor #3 has an approved value, and R8 says both are redone. Block 4 gate: spec :124 and the 25-trade minimum unchanged; Decision 2 fixes only the series and the arithmetic. R6 parked research: its first pass is a without series by its own design and is no Block 4 reference; nothing in R6 changes. SHM: SHM-4 and SHM-5's "backtest" is read as the with series, bands unchanged; SHM-4 is one-sided over 20 trades, the Block 4 gate is two-sided over the paper period, and neither replaces the other. #4 parity (the full-day flat's timing against the strategy's 16:00 bar-close flat, and early-close days) is not decided here. #5 (the session window) is an operator lockout with no effect on system trades; #1 and #6 to #9 are applied in neither series.
L+2384     27	
L+2384     28	**Limits.** No code, no strategy file, no breaker value and no spec body is changed. The nine breakers stay SPECIFIED ONLY: zero implemented, zero tested; a with series is a simulation of specified text, not evidence that a breaker works. No with series exists yet, and none can be produced until #2 and #3 have approved values (R8: PROPOSED; D2 (c) once real money is at stake); this entry sets none. If an approved #2 or #3 value later changes, the with series is re-derived and every gate value on it is recomputed. It does not lift F3 or F4 and depends on neither: the fill resolution of any run is whatever F3 settles. It does not decide parity for #1, #4 or #6 to #9, and does not mark O4 passed.
L+2384     29	
L+2384     30	**S4 timing.** Written 2026-11-13, before the work it governs: no with series, no breaker code and no Block 4 paper trade exists. Chain: D-2026-11-08-D D1 → DECISION_LOG 2026-11-13T05:45:00Z (WHO: praxis-master).
L+2384     31	
L+2384     32	[standing sentence cut]
(eval):1: == not found
```

Block 2: the diff (check f) and O4 in the rubric.
```
$ bash -c 'cd /Volumes/Sensidine/Praxis.build; wc -l DECISIONS.md; echo "-----"; diff /tmp/o4red-pre-DECISIONS.md DECISIONS.md; echo "diff rc=$?"; echo "-----"; sed -n "115,123p" specs/SPEC_RUBRIC.md'
    2416 DECISIONS.md
-----
2397c2397
< **Decision 2: how the Block 4 gate is satisfiable (CONDITIONAL on assumptions (i) and (iii) above; same void clause).** The gate compares Block 4 paper trades against the with series only: the with series of the arm whose parameters trade in Block 4 (arm (a), which R2 says GO requires; that an adopted arm (b) set would replace it is the master's reading under D1, changeable; open item D-2026-11-04-A NEEDS AMEAR 4, DECISIONS.md:832, "Is R-1104-3's judged version arm (a), arm (b) or both?"), over its full test span, at the cost model in force. Win rate is A3's quantity, computed identically on the with series and on all Block 4 paper trades; it passes if the two differ by at most 15 percentage points. Average trade P&L is the mean net P&L per trade per contract after commission and slippage; it passes if |paper mean − with mean| ≤ 0.25 × with mean, a positive with mean being presupposed (R5: net positive after costs). Trades the breakers removed enter neither term; on paper, entries #2 or #3 block make no trade and are logged, not counted. The gate is never re-run on the without series to rescue a failure. Reading "±15%" as percentage points and "±25%" as relative to the with mean is the master's, under D1, changeable.
---
> **Decision 2: how the Block 4 gate is satisfiable (CONDITIONAL on assumptions (i) and (iii) above; same void clause).** The gate compares Block 4 paper trades against the with series only: the with series of the arm whose parameters trade in Block 4 (arm (a), which R2 says GO requires; that an adopted arm (b) set would replace it is the master's reading under D1, changeable), over its full test span, at the cost model in force. Win rate is A3's quantity, computed identically on the with series and on all Block 4 paper trades; it passes if the two differ by at most 15 percentage points. Average trade P&L is the mean net P&L per trade per contract after commission and slippage; it passes if |paper mean − with mean| ≤ 0.25 × with mean, a positive with mean being presupposed (R5: net positive after costs). Trades the breakers removed enter neither term; on paper, entries #2 or #3 block make no trade and are logged, not counted. The gate is never re-run on the without series to rescue a failure. Reading "±15%" as percentage points and "±25%" as relative to the with mean is the master's, under D1, changeable.
2405c2405
< - Breakers on (DECISIONS.md): :512 "the backtest runs **with the breakers on, once they are built**"; :761 "when the time comes ask agaian."; R8 :1584 "#2 max 2 trades/day, #3 two-and-done" and :1588 "New values come back to Amear as".
---
> - Breakers on (DECISIONS.md): :512 "the backtest runs **with the breakers on, once they are built**"; R8 :1584 "#2 max 2 trades/day, #3 two-and-done" and :1588 "New values come back to Amear as".
2410c2410
< **S6 cross-block.** Block 2: R2, R3, A7, A8 unchanged; gate values move to the with series; the values-spec §6 selection statistic is not changed, and whether arm (b) selects on the with series is left to the values-spec unit (named gap: selecting on one series and grading on the other). Block 3 breakers: assumption (iii) is a parity requirement on the later build, not an edit; it conflicts with topology :59 as written, which drops "the entry signal" whole, so a reversal sent as one SELL or BUY would leave the position open; neither #2 nor #3 has an approved value, and R8 says both are redone. Block 4 gate: spec :124 and the 25-trade minimum unchanged; Decision 2 fixes only the series and the arithmetic. R6 parked research: its first pass is a without series by its own design and is no Block 4 reference; nothing in R6 changes. SHM: SHM-4 and SHM-5's "backtest" is read as the with series, bands unchanged; SHM-4 is one-sided over 20 trades, the Block 4 gate is two-sided over the paper period, and neither replaces the other. Amear's words: R-VN3-5 says "once they are built"; the with series simulates specified text before any breaker exists (named difference); D-2026-11-04-A (ii) re-ask binds before a High run, and this entry plans no run. #4: both series carry the strategy's 16:00 flat, so on a full trading day #4 does not split them. Early-close days are a named parity gap, not decided here: amended #4 flattens "or the exchange's early close on an early-close day if earlier" (spec :212); the strategy's explicit flat tests 16:00 only (code :189), its early-close exit is the platform backstop `IsExitOnSessionCloseStrategy              = true;` (code :108), and the record already shows an "early-close cut where NT8 cuts (12:00/12:15/14:03 vs the file's 13:15/13:00)" (DECISIONS.md:1490) and "12:15 early-close exits" accepted as is (DECISIONS.md:944). Whether the backtest's early-close exit matches amended #4's time is not established; early-close sessions are reported apart in Block 2 and Block 4, and whether they enter the gate is left open with early-close handling (D-2026-10-31-A NEEDS AMEAR 3, DECISIONS.md:351); #5 (the session window) is an operator lockout with no effect on system trades; #1 and #6 to #9 are applied in neither series.
---
> **S6 cross-block.** Block 2: R2, R3, A7, A8 unchanged; gate values move to the with series; the values-spec §6 selection statistic is not changed, and whether arm (b) selects on the with series is left to the values-spec unit (named gap: selecting on one series and grading on the other). Block 3 breakers: assumption (iii) is a parity requirement on the later build, not an edit; it conflicts with topology :59 as written, which drops "the entry signal" whole, so a reversal sent as one SELL or BUY would leave the position open; neither #2 nor #3 has an approved value, and R8 says both are redone. Block 4 gate: spec :124 and the 25-trade minimum unchanged; Decision 2 fixes only the series and the arithmetic. R6 parked research: its first pass is a without series by its own design and is no Block 4 reference; nothing in R6 changes. SHM: SHM-4 and SHM-5's "backtest" is read as the with series, bands unchanged; SHM-4 is one-sided over 20 trades, the Block 4 gate is two-sided over the paper period, and neither replaces the other. #4 parity (the full-day flat's timing against the strategy's 16:00 bar-close flat, and early-close days) is not decided here. #5 (the session window) is an operator lockout with no effect on system trades; #1 and #6 to #9 are applied in neither series.
2412c2412
< **Limits.** No code, no strategy file, no breaker value and no spec body is changed. The nine breakers stay SPECIFIED ONLY: zero implemented, zero tested; a with series is a simulation of specified text, not evidence that a breaker works. No with series exists yet, and none can be produced until #2 and #3 have approved values (R8: PROPOSED; D2 (c) once real money is at stake); this entry sets none. If an approved #2 or #3 value later changes, the with series is re-derived and every gate value on it is recomputed. It does not lift F3 or F4 and depends on neither: the fill resolution of any run is whatever F3 settles. It does not decide parity for #1 or #6 to #9, and does not mark O4 passed.
---
> **Limits.** No code, no strategy file, no breaker value and no spec body is changed. The nine breakers stay SPECIFIED ONLY: zero implemented, zero tested; a with series is a simulation of specified text, not evidence that a breaker works. No with series exists yet, and none can be produced until #2 and #3 have approved values (R8: PROPOSED; D2 (c) once real money is at stake); this entry sets none. If an approved #2 or #3 value later changes, the with series is re-derived and every gate value on it is recomputed. It does not lift F3 or F4 and depends on neither: the fill resolution of any run is whatever F3 settles. It does not decide parity for #1, #4 or #6 to #9, and does not mark O4 passed.
diff rc=1
-----
A security requirement that stopped being mentioned is not a resolved one.

### O4 — Backtest-vs-live configuration parity
Deviation C permits reverse-and-re-enter. Breakers #2 and #3 cap trades and end
the session after two consecutive losers. Block 4's gate compares live to
backtest within ±15% win rate and ±25% average trade P&L. **Required:** a
written statement of whether the Block 2 backtest runs with breakers applied,
without them, or both — and how the Block 4 gate is satisfiable if they differ.
```

Block 3: check (a), every quoted string at its cited line. The script `/tmp/o4w1/chk.sh` prints each command with bash `%q` quoting (a literal, runnable form), then runs it. The `chk` lines below are the script's call list; the output follows them.
```
$ cat /tmp/o4w1/chk.sh   (function and call list)
chk(){ printf '$ sed -n %sp %s | grep -c -F -- %q\n' "$2" "$1" "$3"; sed -n "${2}p" "$1" | grep -c -F -- "$3"; }
S=docs/specs/2026-11-05-phase3-build-specification.md  C=ninjascript/PraxisNoiseAreaBreakout.cs  T=docs/specs/2026-11-10-live-signal-topology.md  D=DECISIONS.md
$ bash /tmp/o4w1/chk.sh 2>&1
$ sed -n 98p docs/specs/2026-11-05-phase3-build-specification.md | grep -c -F -- trade\ count\ hits\ daily\ max\ →\ disable\ order\ submission
1
$ sed -n 99p docs/specs/2026-11-05-phase3-build-specification.md | grep -c -F -- 2\ consecutive\ losers\ in\ one\ session\ →\ identical\ to\ max\ trades
1
$ sed -n 124p docs/specs/2026-11-05-phase3-build-specification.md | grep -c -F -- within\ ±15%\ win\ rate\ and\ ±25%\ average\ trade\ P\&L
1
$ sed -n 124p docs/specs/2026-11-05-phase3-build-specification.md | grep -c -F -- ±15%
1
$ sed -n 124p docs/specs/2026-11-05-phase3-build-specification.md | grep -c -F -- ±25%
1
$ sed -n 205p docs/specs/2026-11-05-phase3-build-specification.md | grep -c -F -- The\ system\ opens\ no\ new\ position\ from\ that\ flat\ time\ until\ 18:00\ ET\,\ when\ the\ next\ session\ begins.
1
$ sed -n 224p docs/specs/2026-11-05-phase3-build-specification.md | grep -c -F -- The\ system\'s\ own\ trading\ is\ not\ disabled\ by\ this\ breaker
1
$ sed -n 239p docs/specs/2026-11-05-phase3-build-specification.md | grep -c -F -- New\ system\ entries\ between\ 15:00\ and\ 16:00\ are\ allowed\ under\ Rule\ F2-1\,\ subject\ to\ breakers\ #1\,\ #2\,\ #3\,\ #6\,\ #7\,\ #8\ and\ #9.
1
$ sed -n 196p docs/specs/2026-11-05-phase3-build-specification.md | grep -c -F -- SPECIFIED\ ONLY\ —\ zero\ implemented\,\ zero\ tested\,\ zero\ tested\ under\ failure
1
$ sed -n 42p DECISION_LOG.md | grep -c -F -- positions/session\ =\ reverse\ \&\ re-enter\ on\ opposite-band\ cross\ \(NOT\ one-position/session\)
1
$ sed -n 32p ninjascript/PraxisNoiseAreaBreakout.cs | grep -c -F -- Positions/session\ =\ REVERSE\ \&\ re-enter\ on\ an\ opposite-band\ cross
1
$ sed -n 189p ninjascript/PraxisNoiseAreaBreakout.cs | grep -c -F -- if\ \(mod\ \>=\ CloseMod\)
1
$ sed -n 191p ninjascript/PraxisNoiseAreaBreakout.cs | grep -c -F -- FlattenAll\(\"16:00\ session\ flat\"\)\;
1
$ sed -n 59p docs/specs/2026-11-10-live-signal-topology.md | grep -c -F -- Deviation\ C\ reverse-and-re-enter\ counts\ as\ an\ entry
1
$ sed -n 58p docs/specs/2026-11-10-live-signal-topology.md | grep -c -F -- must\ never\ be\ blocked\ by\ a\ closed\ gate
1
$ sed -n 59p docs/specs/2026-11-10-live-signal-topology.md | grep -c -F -- the\ entry\ signal
1
$ sed -n 1556p DECISIONS.md | grep -c -F -- GO\ requires\ arm\ \(a\)\ to\ pass.
1
$ sed -n 1746p DECISIONS.md | grep -c -F -- R3\ amends\ Q8:\ arm\ \(a\)\ is\ judged\ on\ gates\ 1-5\ \(WFE\ not
1
$ sed -n 1748p DECISIONS.md | grep -c -F -- O1\ is\ discharged\ by\ R2\ +\ R3\ +\ A7.
1
$ sed -n 1731p DECISIONS.md | grep -c -F -- W\ /\ \(W\ +\ L\ +\ 0.5\ x\ B\)\,\ B\ =\ trade\ exited\ at\ its\ entry\ price.
1
$ sed -n 1733p DECISIONS.md | grep -c -F -- \"within\ +/-15%\ win\ rate\"\ check\,\ computed\ identically\ on\ backtest
1
$ sed -n 1836p DECISIONS.md | grep -c -F -- win/loss\ judged\ by\ price
1
$ sed -n 512p DECISIONS.md | grep -c -F -- the\ backtest\ runs\ \*\*with\ the\ breakers\ on\,\ once\ they\ are\ built\*\*
1
$ sed -n 1584p DECISIONS.md | grep -c -F -- \#2\ max\ 2\ trades/day\,\ #3\ two-and-done
1
$ sed -n 1588p DECISIONS.md | grep -c -F -- New\ values\ come\ back\ to\ Amear\ as
1
$ sed -n 189p DECISIONS.md | grep -c -F -- SHM-4:\ win-rate\ \>15\ ppts\ below\ backtest\ OR\ slippage\ \>2\ ticks/side\ worse\,\ over\ a\ 20-trade\ window.
1
$ sed -n 2350p DECISIONS.md | grep -c -F -- without\ breakers\ as\ design\ :116\ \(O4\)\ states
1
$ sed -n 55p docs/reports/2026-11-09-d6-drawdown-check-manager.md | grep -c -F -- every\ later\ trade\ that\ session\ is\ skipped
1
$ sed -n 1560p DECISIONS.md | grep -c -F -- a\ break-even\ trade\ counts\ as
1
$ sed -n 1561p DECISIONS.md | grep -c -F -- a\ break-even\ trade\ counts\ as
0
$ git show bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md | sed -n 116p | grep -c -F -- First\ pass\ runs\ without\ breakers\ \(no\ approved\ values\;\ D6\ E4\)\ and\ says\ so\;\ a\ breakers-on\ run\ waits\ for\ F2.
1
```
The `0` at :1561 is expected: the cite is the range :1560-1561 and the quoted fragment sits whole on :1560 (block 5 shows :1561 = "half a loss."). The bead quote and the word "backtest" (SHM-5) are checked in blocks 4 and 6. Result for (a): every quoted string is present at its cited line.

Block 4: the bead quote, the chain row, and whether any entry is titled Deviation C.
```
$ bash -c 'cd /Volumes/Sensidine/Praxis.build; bd show Praxis_build-yra 2>&1 | grep -c -F "the live-vs-backtest gate is structurally unmeetable."; grep -n -F "2026-11-13T05:45:00Z" DECISION_LOG.md | cut -c1-700; grep -n -E "^#+ .*Deviation C" DECISIONS.md; echo "count=$?"'
1
899:- [2026-11-13T05:45:00Z] WHO: praxis-master | WHAT: **Rubric O3 → PASSED@cae83dc written in `specs/SPEC_RUBRIC.md` (filer's note + moved block; working tree, 8+ / 5−); it rides in this run's close flush, as the F2 move did at `c29d08b` (no MANIFEST row, same precedent).** **Decided by master under D-2026-11-08-D D1: Unit 2 = rubric O4 filing** (bead `Praxis_build-yra`): a manager drafts ONE DECISIONS.md entry D-2026-11-13-A answering O4's two questions (does the Block 2 backtest run with breakers applied, without, or both; how the Block 4 live-vs-backtest gate is satisfiable if they differ), grounded in the Phase 3 spec's breaker #2/#3 and Block 4 gate text, Deviation C, amended #4/#5, t
count=1
(bd show, the wrapped line that holds the quote:)
  over 20 trades, no ±25% term. If the backtest has no breakers but live is   
  truncated by #2/#3, the live-vs-backtest gate is structurally unmeetable.   
```
(`grep` exit status 1 means no match: no heading in DECISIONS.md names Deviation C. The 700-character cut of row 899 is mine. The command shown is the part of my actual call that matters here. That call also printed the first 40 lines of `bd show`, and the two wrapped lines above come from that print. In blocks 5 and 6, the line-189 read and the joined `sed` ranges were re-run with these exact ranges before I finished the report.)

Block 5: the Amear-side records behind the entry's citations (R-VN3-5, R-1104-3, the deferred re-ask, R2, R4, R5, R8, A3, C5).
```
$ bash -c 'cd /Volumes/Sensidine/Praxis.build; for n in 508 509 510 512 513 752 753 754 761 832; do printf "%s: " $n; sed -n "${n}p" DECISIONS.md | cut -c1-600; done'
508: **R-VN3-5 — O4, backtest vs breakers.**
509: - Amear's words (notes-3 line 28): *"If they're not live, then they're not live."* [cut: an ellipsis character] *"Yeah, once uh, once it goes through."* Between the two quotes the voice agent recorded, in brackets, what Amear was told: *"[told breakers will be live, built in Block 3, required before paper and live]"* — the agent's words, not Amear's.
510: - Agent's reading, confirmed by Amear in voice only (notes-3 line 29): the backtest runs **with the breakers on, once they are built**. That raises the priority of `r8j`, the Phase 3 spec import, because the breaker definitions live there.
512: - **Settles (against O4):** in the agent's reading, confirmed by Amear in voice only and entered at the ledger row above: the backtest runs **with the breakers on, once they are built** (notes-3 line 29). Filer's mapping, not part of the ruling: O4 asks this of the Block 2 backtest. The ruling says nothing about any other run (see Leaves open).
513: - **Leaves open (against O4):** whether a without-breakers run is also kept (the "or both" option); how the Block 4 gate is satisfiable if the backtest and live configurations differ — the ruling does not address it; the breakers are not defined in the repo (`Praxis_build-r8j`, description: the nine breakers are *"TBD — needs PHASE 3 BUILD SPECIFICATION import"*) and are not built. This entry does not mark O4 cleared; that is the auditor's grade.
752: **R-1104-3 — judged go/no-go version; tick-data purchase condition.** [standing sentence cut]
753: - Amear's words: *"Yeah"*. Brief's framing: *"Yeah"* = High fill resolution with circuit breakers on as the judged go/no-go version, confirming R-VN3-6. The row does not record the question he answered.
754: - Closes D-2026-11-02-C NEEDS AMEAR 14 (DECISIONS.md:544). That closure label is in the ledger row's framing. Amear's own word is "Yeah".
761: - (ii) R-VN3-5 (DECISIONS.md:508-513): the breakers are not built and not defined in the repo; they wait for `Praxis_build-r8j`. Amear, DECISION_LOG `2026-11-03T18:45:00Z` item (4): *"when the time comes ask agaian."* = DEFERRED. The master must re-ask before any High run is planned.
832: 4. Is R-1104-3's judged version arm (a), arm (b) or both?
$ grep -n -F "2026-11-03T18:45:00Z" DECISION_LOG.md   (row 598, item (4) only; the rest of the row is cut, and it holds ellipsis characters)
598: [cut] (4) asked "wait for `r8j`, or go ahead as measurement-only?" → **"when the time comes ask agaian."** = DEFERRED; no reading taken; master must re-ask before any High run is planned. [cut]
$ sed -n '1556,1569p;1583,1589p;1730,1735p;1744,1745p;1836,1837p' DECISIONS.md
R2  GO requires arm (a) to pass. Arm (b) can only add confidence or
    block a GO; it can never carry a GO on its own (§4 item 3).
R3  Gate 6 (WFE) applies to arm (b) only (§4 item 3).
R4  Scoring, hybrid (§4 item 3, gate 2):
    - Win rate: no-trade days excluded; a break-even trade counts as
      half a loss.
    - Sharpe: daily returns, every trading day counted (no-trade
      days = 0), equity base = the account size actually traded.
    Check against the values-spec §6/§8 wording; flag any conflict
    back to Amear, do not resolve it.
R5  The fixed R:R shape filter (3:1 partial plus runner; 1.5:1) is
    retired for all automated-strategy research, including the
    higher-win-rate brief. A strategy qualifies if it is fully
    rule-based, net positive after costs, and survives every MFFU
R8  F2 unfreezes. Breaker values set for manual trading are redone
    for the automated book: #2 max 2 trades/day, #3 two-and-done,
    #4 flat at 11:30, #5 as a disable of the system's own trading
    15:00–18:00, #8 inter-trade interval under 5 minutes.
    KEEP: #1 daily loss limit; #5 as a lockout on Amear's own
    interaction 15:00–18:00. New values come back to Amear as
    PROPOSED.
A3  FLAG 3: Win rate is not a Block 2 pass gate. Per trade:
    W / (W + L + 0.5 x B), B = trade exited at its entry price.
    No-trade sessions excluded. It is the quantity for O4's Block 4
    "within +/-15% win rate" check, computed identically on backtest
    and paper.
A4  FLAG 4: Max-DD gate = backtest max drawdown must stay below 80%
A6  FLAG 6: R8 starts the breaker PROPOSAL unit. F2's state changes
    when Amear approves the proposed values.
C5  D-2026-11-08-B (i) win/loss judged by price, consistent with
    B = exit at entry price; (ii) Studio Static rows use the stricter
```
(These came from several `sed` calls this session; I joined their outputs here for space. Line 832 sits under the heading at :803, "D-2026-11-05-A: Walk-forward design rulings", not under D-2026-11-04-A. The pre-edit text called it "D-2026-11-04-A NEEDS AMEAR 4", and the edit removed that pointer.)

Block 6: SHM-4 and SHM-5 at :189, the spec's Block 4 gate and minimum, and rubric D2.
```
$ sed -n 189p DECISIONS.md
- **Q9 SHM band form:** FIXED pre-declared bands. SHM-4: win-rate >15 ppts below backtest OR slippage >2 ticks/side worse, over a 20-trade window. SHM-5: monthly trade count within [0.5×, 2.0×] of backtest mean; breach = 2 consecutive months. (Coarse + transparent chosen over fitted statistical test.)
$ grep -n -E "\b25\b" docs/specs/2026-11-05-phase3-build-specification.md | cut -c1-250
117:Minimum duration: 6 weeks or 25 triggered trades, whichever comes later. Must span at least one FOMC day, one NFP day, and one NQ contract rollover.
124:- Strategy performance vs. backtest: within ±15% win rate and ±25% average trade P&L
$ sed -n '449,453p' specs/SPEC_RUBRIC.md
D2  Only four things stop and wait for Amear's word: (a) spending
    money; (b) switching live trading on, or any order path to a
    funded account; (c) changing circuit-breaker values while real
    money is at stake; (d) installing keys, credentials or agent
    permissions. Everything else is D1.
```

Block 7: the strategy code behind "Implemented: reverse and 16:00 flat", and the zero-hits claim re-run.
```
$ bash -c 'cd /Volumes/Sensidine/Praxis.build; C=ninjascript/PraxisNoiseAreaBreakout.cs; grep -n -E "Calculate *=|CloseMod *=|CloseMod;" $C; sed -n "106,109p;187,192p;221,225p" $C; for f in ninjascript/PraxisNoiseAreaBreakout*.cs; do printf "%s: " "$f"; /usr/bin/grep -c -E "MaxTrades|TradeCount|tradesToday|consecutive|loser|LossStreak" "$f"; done; ls -la docs/reports/2026-11-13-o4-parity-manager.md'
58:		private const int CloseMod = 16 * 60;       // 960
105:				Calculate                                 = Calculate.OnBarClose;
196:			bool isCheckpoint = (Time[0].Minute == 0 || Time[0].Minute == 30) && mod > OpenMod && mod < CloseMod;
				EntriesPerDirection                       = 1;
				EntryHandling                             = EntryHandling.AllEntries;
				IsExitOnSessionCloseStrategy              = true;   // backstop; explicit 16:00 flat is primary
				ExitOnSessionCloseSeconds                 = 30;

			// ---- 16:00 ET cash-close flat (spec §4 p.9/12; trader-locked). Applies before any entry. ----
			if (mod >= CloseMod)
			{
				FlattenAll("16:00 session flat");
				return;                          // never open a new position at/after the close

			// (2) ENTRY / REVERSAL — long above the Upper Bound, short below the Lower Bound (spec §2 p.9).
			//     A cross to the OPPOSITE bound while holding flips the position (NT8 managed reverse:
			//     EnterLong while short closes the short and goes long). Position.MarketPosition here is
			//     the pre-fill state, so an ExitLong above followed by Close<Lower still reverses correctly.
ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs: 0
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs: 0
ninjascript/PraxisNoiseAreaBreakout.cs: 0
-rw-r--r--@ 1 admin  staff  14160 Nov 13 00:23 docs/reports/2026-11-13-o4-parity-manager.md
```

Block 8: topology :58 to :59 (what "the entry signal" refers to) and the precedent's context.
```
$ sed -n 59p docs/specs/2026-11-10-live-signal-topology.md
| 2 | Max trades per day | n8n gate node, before Write Signal File: Redis counter of entries this session; gate closes when count = max. | Same as #1: the entry signal is dropped before the file write. | Count of entries submitted this session (from the consumer's journal or fills); the session boundary; the max value. | SPECIFIED | A fill/entry feed back to Redis (unbuilt); session boundary (F2 proposal, H02); value (R8 says "redone", PROPOSED). Deviation C reverse-and-re-enter counts as an entry (O4, bead `Praxis_build-yra`). |
$ sed -n 58p docs/specs/2026-11-10-live-signal-topology.md | grep -o -F "the consumer only knows BUY/SELL"
the consumer only knows BUY/SELL
$ sed -n 55p docs/reports/2026-11-09-d6-drawdown-check-manager.md | cut -c1-200
- **Daily-loss cap rule (sensitivity only).** Trades in a session are taken in exit order. After a trade closes, if the day's realised net is at or below −cap, every later trade that session is skippe
```
(The `grep -o` line at :58 is a substring of the :58 text printed in full this session. The `cut` at :55 is mine.)

## Checks

(a) Quotes byte-present: PASS. 31 of 31 cited-line checks return 1. The `0` at :1561 belongs to a two-line range whose fragment is all on :1560. The bead quote returns 1 and "backtest" is on :189.

(b) Both O4 questions answered: PASS. "Both" is answered at 2393 ("the Block 2 backtest runs both, and is graded with breakers"). How the gate is satisfiable is answered at 2397 (Decision 2: paper trades against the with series only, with the arithmetic stated, CONDITIONAL on (i) and (iii)).

(c) Nothing attributed to Amear beyond his words: FAIL. See defect 1.

(d) Mechanisms are CONDITIONAL or named as gaps: PASS. Cases I tried:
- The removal rule and the paper-side counting sit under CONDITIONAL headings with a void clause.
- "Implemented: reverse and 16:00 flat" (2402) is backed by code :189-191 and :221-225, read this session.
- "16:00 bar-close flat" (2410) agrees with `Calculate.OnBarClose` (:105) and `CloseMod = 16 * 60` (:58).
- The early-close exit through the platform backstop (code :108) is no longer described, but early-close days are named as not decided at 2410.
- "a reversal sent as one SELL or BUY would leave the position open" (2410) is a hypothetical framed as a conflict with topology :59 "as written". Topology :58 records that the consumer only knows BUY/SELL.

(e) No D2 item decided: PASS. The entry sets no breaker value (2412, "this entry sets none"). It spends nothing, touches no live path and changes no key or permission. The Block 4 gate is a paper gate (spec :124, Block 4 on sim).

(f) The diff stays inside 2389-2416: PASS. The hunks are 2397, 2405, 2410 and 2412 only (block 2).

Cases tried that do not break the entry:
- "the 25-trade minimum" (2410) is a paraphrase. Spec :117 says "6 weeks or 25 triggered trades, whichever comes later". It is not a quote, so it is imprecise but not a defect under (a) to (f).
- "an adopted arm (b) set would replace it" (2397) is labelled as the master's reading. It sits in tension with R2's "it can never carry a GO on its own", but nothing is attributed to Amear there.
- "R5: net positive after costs" matches R5 at :1569.
- "R8 says both are redone" matches :1583.
- "(R8, A6)" matches A6 at :1744-1745.

## Defect list

1. Entry line 2393 (Decision 1). Quoted text: "is computed on the with series, the version closest to live (R-VN3-5, R-1104-3)". The two Amear rulings are cited as grounds for grading on the with series. His recorded words do not carry that.
   - R-VN3-5 (:510, :512) is "the agent's reading, confirmed by Amear in voice only": the backtest runs "with the breakers on, **once they are built**". This entry's with series is a Mac-side deletion of trades after the run, from specified text, before any breaker exists. The entry says so itself: "a with series is a simulation of specified text" (2412), and only approved values are needed, not a build (2412, "none can be produced until #2 and #3 have approved values").
   - This edit deleted the only sentence that named the gap, at old 2410: "Amear's words: R-VN3-5 says "once they are built"; the with series simulates specified text before any breaker exists (named difference)". The edit also removed the :761 citation of Amear's later DEFERRED, "when the time comes ask agaian.", on the related question "wait for `r8j`, or go ahead as measurement-only?" (DECISION_LOG.md:598, "master must re-ask before any High run is planned"). Its bounding clause went with it: "D-2026-11-04-A (ii) re-ask binds before a High run, and this entry plans no run".
   - R-1104-3 (:753): "Amear's words: *"Yeah"*". The "circuit breakers on as the judged go/no-go version" part is "Brief's framing", and "The row does not record the question he answered." The entry cites R-1104-3 with no framing label.
   - The generic "Not Amear's ruling" at 2391 does not cure this. The parenthetical at 2393 still presents R-VN3-5 and R-1104-3 as support that his words do not give: R-VN3-5 says "once they are built", and R-1104-3 is a bare "Yeah" under someone else's framing.

Grade: FAIL (1 defect)

## Files staged
None. This report is unstaged. I ran no `git add`.

## Result
FAIL

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
