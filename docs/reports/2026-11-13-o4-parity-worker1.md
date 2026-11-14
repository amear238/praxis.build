# O4 parity adversarial, worker 1 (bead Praxis_build-yra)

## Task
Adversarial check of DECISIONS.md entry D-2026-11-13-A (lines 2389-2416, working tree, main @ cae83dc) against rubric O4, standing S2 and S6, and the D2 four-item list. Unit 2026-11-13-o4-parity.

## Mode
ADVERSARIAL. Read-only except this report. Nothing staged, edited or committed by this worker.

## Criterion
specs/SPEC_RUBRIC.md O4 as quoted in the brief: a written statement of whether the Block 2 backtest runs with breakers applied, without them, or both, and how the Block 4 gate is satisfiable if they differ. S2: no component reported above its evidence. S6: cross-block conflicts named. D2: (a) money, (b) live trading or a funded order path, (c) breaker values with real money at stake, (d) keys, credentials or agent permissions.

## Process log
1. Located the entry and its line span; printed it.
2. Ran a byte-presence script for every quoted string in Sources (and two in the S6 section), plus the R6 design at bf6fcc7, the bead, the DECISION_LOG row and the strategy-term grep.
3. Read the topology rows for breakers #1 to #7, R-VN3-5, D-2026-11-04-A, SHM-4/5, R2 to R9, A3 to A8, C5, parked R6, and Phase 3 spec :1-15, :94-126, :194-245.
4. Checked the strategy for early-close handling (amended #4 now flattens at an exchange early close).
5. Ran the format, banned-word, ellipsis and diff checks.
6. Wrote defects.

## Verification evidence

### E1. Entry location, file length, staged count
```
$ cd /Volumes/Sensidine/Praxis.build && grep -n -F "## 2026-11-13 — D-2026-11-13-A" DECISIONS.md; wc -l DECISIONS.md; git diff --cached --name-only | wc -l
2389:## 2026-11-13 — D-2026-11-13-A: Backtest-vs-live breaker parity (rubric O4; master under D-2026-11-08-D D1)
    2416 DECISIONS.md
       1
```
(The first call also printed lines 2385-2416; the entry text is read from that print and is not repasted here.)

### E2. Check 1, quotes (script run with bash, /usr/bin/grep to avoid the zsh ugrep alias)
```
$ cd /Volumes/Sensidine/Praxis.build && cat > /tmp/o4q.sh <<'EOF'
#!/bin/bash
P=docs/specs/2026-11-05-phase3-build-specification.md
T=docs/specs/2026-11-10-live-signal-topology.md
S=ninjascript/PraxisNoiseAreaBreakout.cs
D=DECISIONS.md
q(){ printf '%s:%s [%s] -> ' "$1" "$2" "$3"; sed -n "${2}p" "$1" | /usr/bin/grep -c -F -- "$3"; }
q $P 98 'trade count hits daily max → disable order submission'
q $P 99 '2 consecutive losers in one session → identical to max trades'
q $P 124 'within ±15% win rate and ±25% average trade P&L'
q $P 205 'The system opens no new position from that flat time until 18:00 ET, when the next session begins.'
q $P 224 "The system's own trading is not disabled by this breaker"
q $P 239 'New system entries between 15:00 and 16:00 are allowed under Rule F2-1, subject to breakers #1, #2, #3, #6, #7, #8 and #9.'
q $P 196 'SPECIFIED ONLY — zero implemented, zero tested, zero tested under failure'
q $P 11 'SPECIFIED ONLY'
q DECISION_LOG.md 42 'positions/session = reverse & re-enter on opposite-band cross (NOT one-position/session)'
q $S 32 'Positions/session = REVERSE & re-enter on an opposite-band cross'
q $S 189 'if (mod >= CloseMod)'
q $S 191 'FlattenAll("16:00 session flat");'
q $T 59 'Deviation C reverse-and-re-enter counts as an entry'
q $T 58 'must never be blocked by a closed gate'
q $T 59 'the entry signal'
q $D 1556 'GO requires arm (a) to pass.'
q $D 1746 'R3 amends Q8: arm (a) is judged on gates 1-5 (WFE not'
q $D 1748 'O1 is discharged by R2 + R3 + A7.'
q $D 1731 'W / (W + L + 0.5 x B), B = trade exited at its entry price.'
q $D 1733 '"within +/-15% win rate" check, computed identically on backtest'
q $D 1836 'win/loss judged by price'
q $D 512 'the backtest runs **with the breakers on, once they are built**'
q $D 512 'once they are built'
q $D 761 'when the time comes ask agaian.'
q $D 1584 '#2 max 2 trades/day, #3 two-and-done'
q $D 1588 'New values come back to Amear as'
q $D 189 'SHM-4: win-rate >15 ppts below backtest OR slippage >2 ticks/side worse, over a 20-trade window.'
q $D 2350 'without breakers as design :116 (O4) states'
q docs/reports/2026-11-09-d6-drawdown-check-manager.md 55 'every later trade that session is skipped'
q $D 2399 'When Block 1’s milestone is hit'
printf 'R6 bf6fcc7:116 -> '; git show bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md | sed -n 116p | /usr/bin/grep -c -F -- 'First pass runs without breakers (no approved values; D6 E4) and says so; a breakers-on run waits for F2.'
printf 'bead -> '; bd show Praxis_build-yra | /usr/bin/grep -c -F 'the live-vs-backtest gate is structurally unmeetable.'
printf 'DECISION_LOG 05:45 -> '; /usr/bin/grep -c -F '2026-11-13T05:45:00Z' DECISION_LOG.md
printf 'Deviation C in DECISIONS.md lines: '; /usr/bin/grep -n -F 'Deviation C' $D | cut -c1-140
echo '--- strategy grep'
grep -c -i -E "MaxTrades|TradeCount|tradesToday|consecutive|loser|LossStreak" ninjascript/PraxisNoiseAreaBreakout*.cs
EOF
bash /tmp/o4q.sh
docs/specs/2026-11-05-phase3-build-specification.md:98 [trade count hits daily max → disable order submission] -> 1
docs/specs/2026-11-05-phase3-build-specification.md:99 [2 consecutive losers in one session → identical to max trades] -> 1
docs/specs/2026-11-05-phase3-build-specification.md:124 [within ±15% win rate and ±25% average trade P&L] -> 1
docs/specs/2026-11-05-phase3-build-specification.md:205 [The system opens no new position from that flat time until 18:00 ET, when the next session begins.] -> 1
docs/specs/2026-11-05-phase3-build-specification.md:224 [The system's own trading is not disabled by this breaker] -> 1
docs/specs/2026-11-05-phase3-build-specification.md:239 [New system entries between 15:00 and 16:00 are allowed under Rule F2-1, subject to breakers #1, #2, #3, #6, #7, #8 and #9.] -> 1
docs/specs/2026-11-05-phase3-build-specification.md:196 [SPECIFIED ONLY — zero implemented, zero tested, zero tested under failure] -> 1
docs/specs/2026-11-05-phase3-build-specification.md:11 [SPECIFIED ONLY] -> 1
DECISION_LOG.md:42 [positions/session = reverse & re-enter on opposite-band cross (NOT one-position/session)] -> 1
ninjascript/PraxisNoiseAreaBreakout.cs:32 [Positions/session = REVERSE & re-enter on an opposite-band cross] -> 1
ninjascript/PraxisNoiseAreaBreakout.cs:189 [if (mod >= CloseMod)] -> 1
ninjascript/PraxisNoiseAreaBreakout.cs:191 [FlattenAll("16:00 session flat");] -> 1
docs/specs/2026-11-10-live-signal-topology.md:59 [Deviation C reverse-and-re-enter counts as an entry] -> 1
docs/specs/2026-11-10-live-signal-topology.md:58 [must never be blocked by a closed gate] -> 1
docs/specs/2026-11-10-live-signal-topology.md:59 [the entry signal] -> 1
DECISIONS.md:1556 [GO requires arm (a) to pass.] -> 1
DECISIONS.md:1746 [R3 amends Q8: arm (a) is judged on gates 1-5 (WFE not] -> 1
DECISIONS.md:1748 [O1 is discharged by R2 + R3 + A7.] -> 1
DECISIONS.md:1731 [W / (W + L + 0.5 x B), B = trade exited at its entry price.] -> 1
DECISIONS.md:1733 ["within +/-15% win rate" check, computed identically on backtest] -> 1
DECISIONS.md:1836 [win/loss judged by price] -> 1
DECISIONS.md:512 [the backtest runs **with the breakers on, once they are built**] -> 1
DECISIONS.md:512 [once they are built] -> 1
DECISIONS.md:761 [when the time comes ask agaian.] -> 1
DECISIONS.md:1584 [#2 max 2 trades/day, #3 two-and-done] -> 1
DECISIONS.md:1588 [New values come back to Amear as] -> 1
DECISIONS.md:189 [SHM-4: win-rate >15 ppts below backtest OR slippage >2 ticks/side worse, over a 20-trade window.] -> 1
DECISIONS.md:2350 [without breakers as design :116 (O4) states] -> 1
docs/reports/2026-11-09-d6-drawdown-check-manager.md:55 [every later trade that session is skipped] -> 1
DECISIONS.md:2399 [When Block 1’s milestone is hit] -> 0
R6 bf6fcc7:116 -> 1
bead -> 1
DECISION_LOG 05:45 -> 1
Deviation C in DECISIONS.md lines: 511:- **O4 criterion** (`specs/SPEC_RUBRIC.md:94-99`, verbatim): *"Deviation C permits reverse-and-re-enter. Breakers #2 and #3 cap trades a
2072:**S6 cross-block (from topology doc §7, :112).** Block 1 (emitter changes from TradingView to NT8; the TESTED pipe is reused; Deviation
2401:- Deviation C: no DECISIONS.md entry carries that name (DECISIONS.md:511 only quotes the rubric). Its authority is DECISION_LOG.md:42: 
2403:- Topology `docs/specs/2026-11-10-live-signal-topology.md`: :59 "Deviation C reverse-and-re-enter counts as an entry"; :58 "must never 
--- strategy grep
ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:0
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:0
ninjascript/PraxisNoiseAreaBreakout.cs:0
```
The shell exit code was 1 because the last grep -c returned 0 counts. The `DECISIONS.md:2399` row with 0 is my own negative control, not an entry cite: that string belongs to the previous entry (line 2385), and the 0 shows the check can fail. Every quote the entry cites returned 1. Result for check 1: all quotes byte-present; strategy has zero trade-cap or loser-streak terms in all three files.

### E3. Check 2, both O4 questions answered
From the E1 print. Question 1: "Decision 1: the Block 2 backtest runs both, and is graded with breakers." Question 2: Decision 2 names the series (with series of the arm trading in Block 4, full test span), the arithmetic (win rate within 15 percentage points; |paper mean − with mean| ≤ 0.25 × with mean, positive with mean presupposed) and removed trades ("enter neither term"; listed in a removed-trades table). Both are unambiguous. One gap: no rule is stated for a with mean ≤ 0 beyond "presupposed"; I do not count this as a defect because R5 requires net positive after costs.

### E4. Check 4 evidence, topology and spec text used for the S6 hunt
```
$ cd /Volumes/Sensidine/Praxis.build && T=docs/specs/2026-11-10-live-signal-topology.md; P=docs/specs/2026-11-05-phase3-build-specification.md; sed -n 59p $T | /usr/bin/grep -o -E 'Count of entries submitted this session[^|]*'; sed -n 60p $T | /usr/bin/grep -o -E 'Redis counter of consecutive losing closed trades this session'; sed -n 212p $P | /usr/bin/grep -o -F "clock reaches 16:00:00 ET, or the exchange's early close on an early-close day if earlier"; sed -n 509p DECISIONS.md | /usr/bin/grep -o -F 'If they'"'"'re not live, then they'"'"'re not live.'; sed -n 1584,1588p DECISIONS.md; sed -n 2350p DECISIONS.md | /usr/bin/grep -o -F 'Early close: amended #4 flattens at the exchange'"'"'s early close if earlier.'; sed -n 2402p DECISIONS.md | /usr/bin/grep -o -F 'zero hits for those terms in all three'
Count of entries submitted this session (from the consumer's journal or fills); the session boundary; the max value. 
Redis counter of consecutive losing closed trades this session
clock reaches 16:00:00 ET, or the exchange's early close on an early-close day if earlier
If they're not live, then they're not live.
    for the automated book: #2 max 2 trades/day, #3 two-and-done,
    #4 flat at 11:30, #5 as a disable of the system's own trading
    15:00–18:00, #8 inter-trade interval under 5 minutes.
    KEEP: #1 daily loss limit; #5 as a lockout on Amear's own
    interaction 15:00–18:00. New values come back to Amear as
zero hits for those terms in all three
```
(The 2350 probe printed nothing because that sentence is on line 2348, see E6.)

### E5. Strategy has no early-close flatten; the entry never mentions early close
```
$ cd /Volumes/Sensidine/Praxis.build && echo "== strategy 160-195"; sed -n '160,195p' ninjascript/PraxisNoiseAreaBreakout.cs; echo "== early-close grep across strategies"; grep -c -i -E 'early|halfday|half-day|IsLastBarOfSession|SessionIterator' ninjascript/PraxisNoiseAreaBreakout*.cs; echo "== early close in O4 entry"; sed -n '2389,2416p' DECISIONS.md | /usr/bin/grep -c -i 'early'
== strategy 160-195
				haveDay    = true;
			}

			if (!haveDay)
				return;                         // haven't seen a session open yet in this run

			// ---- Per-bar bookkeeping: record this minute's close + advance session VWAP. ----
			today.Closes[mod] = Close[0];       // minute-of-day -> close (spec §1: Close_{t,HH:MM})
			if (mod == CloseMod)
				today.Close1600 = Close[0];

			double vol = Volume[0];
			if (vol > 0)
			{
				vwapCumPV  += ((High[0] + Low[0] + Close[0]) / 3.0) * vol;   // typical-price VWAP
				vwapCumVol += vol;
			}

			// ---- Build the band for THIS bar's minute-of-day (for plots every bar; orders only at checkpoints). ----
			BuildBand(mod);
			if (haveBand)
			{
				Values[0][0] = curUpper;
				Values[1][0] = curLower;
			}
			if (vwapCumVol > 0)
				Values[2][0] = curVwap;

			// ---- 16:00 ET cash-close flat (spec §4 p.9/12; trader-locked). Applies before any entry. ----
			if (mod >= CloseMod)
			{
				FlattenAll("16:00 session flat");
				return;                          // never open a new position at/after the close
			}

			// ---- Act ONLY at semi-hourly checkpoints HH:00 / HH:30, strictly inside RTH (spec §2 p.9). ----
== early-close grep across strategies
ninjascript/PraxisNoiseAreaBreakout.cs:0
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:0
ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:4
== early close in O4 entry
0
```
(Shell exit 1 came from the final grep -c printing 0.)

### E6. Early-close context, the D-2026-11-10-B entry, #3 wording, Decision 2 marker
```
$ cd /Volumes/Sensidine/Praxis.build && sed -n '37,40p' ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs; echo "== amended #4 early-close cite"; /usr/bin/grep -n -F "or the exchange's early close on an early-close day if earlier" docs/specs/2026-11-05-phase3-build-specification.md | cut -c1-60; echo "== 2072 owning entry"; awk 'NR<=2072 && /^## /{h=NR": "$0} END{print h}' DECISIONS.md | cut -c1-120; echo "== #3 run-time wording in entry"; sed -n '2395p' DECISIONS.md | /usr/bin/grep -o -E '#2: once[^.]*\.|#3: once[^;]*;'; echo "== Decision 2 CONDITIONAL marker"; sed -n '2397p' DECISIONS.md | /usr/bin/grep -c -i 'CONDITIONAL'; sed -n '2397p' DECISIONS.md | /usr/bin/grep -o -F 'on paper, entries #2 or #3 block make no trade and are logged, not counted.'
// EARLY-CLOSE DAYS (INFERRED): a session that ends before 15:59 ET never reaches mod 959, so this
//   variant's decision logic on that day is identical to the base. The position/state carried into
//   that day can still differ, because earlier days flattened differently (INFERRED; 3gm S2/S3).
//   There is no explicit flatten, only the
== amended #4 early-close cite
212:> 4. Session flat gate — clock reaches 16:00:00 ET, or t
== 2072 owning entry
2047: ## 2026-11-10 — D-2026-11-10-B: live-signal topology adopted as the working design (rubric F1; bead Praxis_build-1
== #3 run-time wording in entry
#2: once the session's entry count reaches the #2 maximum in the Phase 3 spec at run time, every later entry is dropped.
#3: once two consecutive closed trades are losers, every later entry is dropped;
== Decision 2 CONDITIONAL marker
0
on paper, entries #2 or #3 block make no trade and are logged, not counted.
```
```
$ cd /Volumes/Sensidine/Praxis.build && /usr/bin/grep -n -o -F "Early close: amended #4 flattens at the exchange's early close if earlier." DECISIONS.md; /usr/bin/grep -n -o -F 'without breakers as design :116 (O4) states, and the R6 report labels every 2A and 2S result as conflicting with amended breaker #4' DECISIONS.md
2348:Early close: amended #4 flattens at the exchange's early close if earlier.
2350:without breakers as design :116 (O4) states, and the R6 report labels every 2A and 2S result as conflicting with amended breaker #4
```

### E7. Check 6, format, banned words, ellipsis, no removed lines
```
$ cd /Volumes/Sensidine/Praxis.build && echo "entry lines: $(sed -n '2389,2416p' DECISIONS.md | wc -l)"; sed -n '2389,2416p' DECISIONS.md | /usr/bin/grep -n -E '^\*\*(Status|Decision|Sources|S6 cross-block|Limits|S4 timing)' | cut -c1-40; echo "last line of file:"; tail -n 1 DECISIONS.md | od -c | tail -n 3; tail -n 1 DECISIONS.md | /usr/bin/grep -c -x -F 'Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.'; printf 'limitation line count in entry: '; sed -n '2389,2416p' DECISIONS.md | /usr/bin/grep -c -F 'Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.'; printf 'removed lines vs HEAD: '; git diff HEAD -- DECISIONS.md | grep -c '^-[^-]'; printf 'added lines vs HEAD: '; git diff HEAD -- DECISIONS.md | grep -c '^+[^+]'; git diff HEAD -- DECISIONS.md | grep '^@@'; printf 'staged count: '; git diff --cached --name-only | wc -l
entry lines:       28
3:**Status:** Decided by master under D-
5:**Decision 1: the Block 2 backtest run
7:**Decision 1 rule (CONDITIONAL).** Per
9:**Decision 2: how the Block 4 gate is 
11:**Sources (quoted byte-exact; DECISIO
22:**S6 cross-block.** Block 2: R2, R3, 
24:**Limits.** No code, no strategy file
26:**S4 timing.** Written 2026-11-13, be
last line of file:
0000100    c   k   s   /   s   i   d   e       s   l   i   p   p   a   g
0000120    e       a   s   s   u   m   e   d   .  \n                    
0000133
1
limitation line count in entry: 1
removed lines vs HEAD: 0
added lines vs HEAD: 81
@@ -2277,6 +2277,98 @@ This entry names the governing rule (Rule F2-1) and the 15:00 disposition, and r
@@ -2293,3 +2385,32 @@ Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippag
staged count:        1
```
The banned-word and ellipsis checks were rerun with patterns built from parts, so this report does not carry the strings themselves:
```
$ cd /Volumes/Sensidine/Praxis.build && a=ver; b=dict; c=COMMIT-IN; d=DEX; e=COMMIT-DIFF-SHA; f=256; E=$(printf '\342\200\246'); printf 'banned words in entry: '; sed -n '2389,2416p' DECISIONS.md | /usr/bin/grep -c -i -E "$a$b|$c$d|$e$f"; printf 'three dots or ellipsis in entry: '; sed -n '2389,2416p' DECISIONS.md | /usr/bin/grep -c -E "[.]{3}|$E"
banned words in entry: 0
three dots or ellipsis in entry: 0
```
(Shell exit 1 because the last grep -c printed 0.) The E7 command above is the first run minus those two checks, which in the first run also printed 0 and 0.

Check 6: PASS (28 lines; all six sections; exact last line, once; 0 banned words; 0 three-dot or ellipsis; 0 removed lines). Note: the working-tree diff also carries a second, earlier hunk (D-2026-11-12-C and others, lines 2277-2388) that is not this entry; the 81 added lines are not all this entry's.

### E8. Check 5, D2 / values / code / F3 / F4
From the E1 print: no D2 item decided (no spend, no live path, no credential; #2's value is left to R8 / D2 (c)); "No code, no strategy file, no breaker value and no spec body is changed"; "It does not lift F3 or F4 and depends on neither". Check 5: PASS, with the caveat in defect 3 (the rule fixes #3 at 2, taken from spec :99, while R8 says #3 is redone).

## Defects

1. S6, unnamed conflict: early close. Amended breaker #4 (Phase 3 spec :212, E6) flattens "at the exchange's early close on an early-close day if earlier". The graded strategy flattens only at `mod >= CloseMod` (16:00; E5) and has 0 early-close terms; Flat1559.cs:37 records (INFERRED) that an early-close session never reaches the flat minute. The entry has 0 hits for "early" (E5) and asserts "#4: both series carry the strategy's 16:00 flat, so #4 does not split them". That is true between the two series, but on an early-close day in the Block 4 window, live #4 flattens at the early close while both backtest series hold the position, so the with series is not the live-equivalent that Decision 2 grades paper trades against. The parked R6 entry names this same conflict for its own strategies (DECISIONS.md:2348, E6); this entry does not.

2. S2, unmarked reliance on how Block 3 will build a breaker. Decision 2 states "on paper, entries #2 or #3 block make no trade and are logged, not counted." It carries no CONDITIONAL marker (count 0, E6) and no void clause. It rests on assumptions (i) and (iii), which live only in the Decision 1 rule, and the void clause there replaces only "this rule". The entry's own S6 section says the topology as written drops the reversal signal whole and leaves the position open. In that case the blocked reversal's open trade is not closed at the reversal bar on paper, so the paper trade list and Decision 2's arithmetic diverge from the with series, and nothing marks or voids Decision 2.

3. Internal inconsistency on #3's value. The rule sets #2 to "the #2 maximum in the Phase 3 spec at run time" but fixes #3 at "two consecutive closed trades" (E6). The S6 section says "R8 says both are redone", and R8 returns new values as PROPOSED (E4). Limits says "none can be produced until #2 has an approved value" and leaves #3 out. So a with series can be produced and graded with #3 = 2 before the redone #3 value is approved. If the redone value differs, the rule is wrong without notice, and no void condition covers it.

4. Sources, negative claim contradicted (minor). "Deviation C: no DECISIONS.md entry carries that name (DECISIONS.md:511 only quotes the rubric)". DECISIONS.md:2072, inside D-2026-11-10-B (header at :2047), names "Deviation C (bead `Praxis_build-yra`)" in its S6 list (E2, E6). If "carries that name" means "is titled Deviation C" the claim holds, but the sentence as written implies :511 is the only mention, and it is not.

Not counted as defects: every quote checks out (E2). Both O4 questions are answered (E3). Format passes (E7). Defining a #3 loser by price (A3/C5) while the topology's live #3 reads a P&L feed is covered by assumption (iii) and its void clause.

## Files staged
None by this worker. This report is untracked and unstaged. Staged count unchanged at 1 (E7).

Grade: FAIL (4 defects)
Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
