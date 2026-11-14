# 2026-11-13 O4 parity, worker 4 (adversarial)

## Task
Grade DECISIONS.md entry D-2026-11-13-A cold against rubric O4, S2, S6, D2 and the format rules. Bead Praxis_build-yra.

## Mode
ADVERSARIAL

## Criterion
specs/SPEC_RUBRIC.md O4 (verbatim in brief), standing S2 and S6, D2.

## Process log
Entry located at DECISIONS.md:2389 (28 lines, 2389-2416). Checks run in the order of the brief. All commands below are pasted literally with full output.

Check 1 (quotes) run via a bash runner that prints each literal command then its output. Runner:

```
#!/bin/bash
cd /Volumes/Sensidine/Praxis.build
while IFS= read -r c; do printf '$ %s\n' "$c"; bash -c "$c" 2>&1; done < "$1"
```

Output of `/bin/bash /tmp/o4w4/run.sh /tmp/o4w4/cmds1.txt`:

```
$ sed -n '98p' docs/specs/2026-11-05-phase3-build-specification.md | /usr/bin/grep -c -F -- 'trade count hits daily max → disable order submission'
1
$ sed -n '99p' docs/specs/2026-11-05-phase3-build-specification.md | /usr/bin/grep -c -F -- '2 consecutive losers in one session → identical to max trades'
1
$ sed -n '124p' docs/specs/2026-11-05-phase3-build-specification.md | /usr/bin/grep -c -F -- 'within ±15% win rate and ±25% average trade P&L'
1
$ sed -n '205p' docs/specs/2026-11-05-phase3-build-specification.md | /usr/bin/grep -c -F -- 'The system opens no new position from that flat time until 18:00 ET, when the next session begins.'
1
$ sed -n '224p' docs/specs/2026-11-05-phase3-build-specification.md | /usr/bin/grep -c -F -- "The system's own trading is not disabled by this breaker"
1
$ sed -n '239p' docs/specs/2026-11-05-phase3-build-specification.md | /usr/bin/grep -c -F -- 'New system entries between 15:00 and 16:00 are allowed under Rule F2-1, subject to breakers #1, #2, #3, #6, #7, #8 and #9.'
1
$ sed -n '196p' docs/specs/2026-11-05-phase3-build-specification.md | /usr/bin/grep -c -F -- 'SPECIFIED ONLY — zero implemented, zero tested, zero tested under failure'
1
$ sed -n '212p' docs/specs/2026-11-05-phase3-build-specification.md | /usr/bin/grep -c -F -- "or the exchange's early close on an early-close day if earlier"
1
$ sed -n '11p' docs/specs/2026-11-05-phase3-build-specification.md | /usr/bin/grep -c -F -- 'SPECIFIED ONLY'
1
$ sed -n '42p' DECISION_LOG.md | /usr/bin/grep -c -F -- 'positions/session = reverse & re-enter on opposite-band cross (NOT one-position/session)'
1
$ sed -n '511p' DECISIONS.md | /usr/bin/grep -c -F -- 'Deviation C'
1
$ sed -n '2072p' DECISIONS.md | /usr/bin/grep -c -F -- 'Deviation C'
1
$ sed -n '32p' ninjascript/PraxisNoiseAreaBreakout.cs | /usr/bin/grep -c -F -- 'Positions/session = REVERSE & re-enter on an opposite-band cross'
1
$ sed -n '189p' ninjascript/PraxisNoiseAreaBreakout.cs | /usr/bin/grep -c -F -- 'if (mod >= CloseMod)'
1
$ sed -n '191p' ninjascript/PraxisNoiseAreaBreakout.cs | /usr/bin/grep -c -F -- 'FlattenAll("16:00 session flat");'
1
$ sed -n '108p' ninjascript/PraxisNoiseAreaBreakout.cs | /usr/bin/grep -c -F -- 'IsExitOnSessionCloseStrategy              = true;'
1
$ sed -n '59p' docs/specs/2026-11-10-live-signal-topology.md | /usr/bin/grep -c -F -- 'Deviation C reverse-and-re-enter counts as an entry'
1
$ sed -n '58p' docs/specs/2026-11-10-live-signal-topology.md | /usr/bin/grep -c -F -- 'must never be blocked by a closed gate'
1
$ sed -n '59p' docs/specs/2026-11-10-live-signal-topology.md | /usr/bin/grep -c -F -- 'the entry signal'
1
$ sed -n '1556p' DECISIONS.md | /usr/bin/grep -c -F -- 'GO requires arm (a) to pass.'
1
$ sed -n '1746p' DECISIONS.md | /usr/bin/grep -c -F -- 'R3 amends Q8: arm (a) is judged on gates 1-5 (WFE not'
1
$ sed -n '1748p' DECISIONS.md | /usr/bin/grep -c -F -- 'O1 is discharged by R2 + R3 + A7.'
1
$ sed -n '1731p' DECISIONS.md | /usr/bin/grep -c -F -- 'W / (W + L + 0.5 x B), B = trade exited at its entry price.'
1
$ sed -n '1733p' DECISIONS.md | /usr/bin/grep -c -F -- '"within +/-15% win rate" check, computed identically on backtest'
1
$ sed -n '1836p' DECISIONS.md | /usr/bin/grep -c -F -- 'win/loss judged by price'
1
$ sed -n '512p' DECISIONS.md | /usr/bin/grep -c -F -- 'the backtest runs **with the breakers on, once they are built**'
1
$ sed -n '512p' DECISIONS.md | /usr/bin/grep -c -F -- 'once they are built'
1
$ sed -n '761p' DECISIONS.md | /usr/bin/grep -c -F -- 'when the time comes ask agaian.'
1
$ sed -n '1584p' DECISIONS.md | /usr/bin/grep -c -F -- '#2 max 2 trades/day, #3 two-and-done'
1
$ sed -n '1588p' DECISIONS.md | /usr/bin/grep -c -F -- 'New values come back to Amear as'
1
$ sed -n '189p' DECISIONS.md | /usr/bin/grep -c -F -- 'SHM-4: win-rate >15 ppts below backtest OR slippage >2 ticks/side worse, over a 20-trade window.'
1
$ sed -n '2350p' DECISIONS.md | /usr/bin/grep -c -F -- 'without breakers as design :116 (O4) states'
1
$ sed -n '1490p' DECISIONS.md | /usr/bin/grep -c -F -- "early-close cut where NT8 cuts (12:00/12:15/14:03 vs the file's 13:15/13:00)"
1
$ sed -n '944p' DECISIONS.md | /usr/bin/grep -c -F -- '12:15 early-close exits'
1
$ sed -n '832p' DECISIONS.md | /usr/bin/grep -c -F -- "Is R-1104-3's judged version arm (a), arm (b) or both?"
1
$ sed -n '1560,1561p' DECISIONS.md | tr '\n' ' ' | /usr/bin/grep -c -F -- 'a break-even trade counts as'
1
$ sed -n '1771p' DECISIONS.md | /usr/bin/grep -c -F -- 'A3'
1
$ sed -n '351p' DECISIONS.md | /usr/bin/grep -c -F -- 'NEEDS AMEAR'
0
$ git show bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md | sed -n 116p | /usr/bin/grep -c -F -- 'First pass runs without breakers (no approved values; D6 E4) and says so; a breakers-on run waits for F2.'
1
$ sed -n '55p' docs/reports/2026-11-09-d6-drawdown-check-manager.md | /usr/bin/grep -c -F -- 'every later trade that session is skipped'
1
$ bd show Praxis_build-yra | /usr/bin/grep -c -F -- 'the live-vs-backtest gate is structurally unmeetable.'
1
$ /usr/bin/grep -c -E 'MaxTrades|TradeCount|tradesToday|consecutive|loser|LossStreak' ninjascript/PraxisNoiseAreaBreakout*.cs
ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:0
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:0
ninjascript/PraxisNoiseAreaBreakout.cs:0
$ ls ninjascript/PraxisNoiseAreaBreakout*.cs
ninjascript/PraxisNoiseAreaBreakout.cs
ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs
```

Check 1 note on :351: the entry cites "D-2026-10-31-A NEEDS AMEAR 3, DECISIONS.md:351" as a pointer, not a quote. Line 351 is item 3 ("Early-close handling") of the NEEDS AMEAR list of D-2026-10-31-A (header :308); the 0 above only shows the item line itself does not carry the words NEEDS AMEAR. Pointer correct. Every quoted string carrying a cite returned 1.

Check 1, the entry's code grep re-run case-insensitively as well (exit status 1 because every count is 0):

```
$ /usr/bin/grep -c -i -E 'MaxTrades|TradeCount|tradesToday|consecutive|loser|LossStreak' ninjascript/PraxisNoiseAreaBreakout*.cs
ninjascript/PraxisNoiseAreaBreakout.cs:0
ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:0
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:0
```

Check 1, the uncited "25-trade minimum" in the S6 paragraph (`/bin/bash /tmp/o4w4/run.sh /tmp/o4w4/cmds3.txt`). It exists at spec :117:

```
$ /usr/bin/grep -rn -i -E '(25|twenty-five)[^0-9%].{0,40}trade|trade.{0,40}[^0-9.±$](25|twenty-five)([^0-9%]|$)' docs/specs/2026-11-05-phase3-build-specification.md specs/SPEC_RUBRIC.md | cut -c1-300
docs/specs/2026-11-05-phase3-build-specification.md:117:Minimum duration: 6 weeks or 25 triggered trades, whichever comes later. Must span at least one FOMC day, one NFP day, and one NQ contract rollover.
$ /usr/bin/grep -rln -i -E 'minimum of 25|25-trade|25 trades|at least 25|≥ ?25 trades|>= ?25 trades' docs/specs specs DECISIONS.md DECISION_LOG.md
docs/specs/2026-07-15-block2-backtesting-scope-proposal.md
DECISIONS.md
DECISION_LOG.md
$ /usr/bin/grep -n -i -E 'paper.{0,60}(minimum|at least)|(minimum|at least).{0,60}paper' docs/specs/2026-11-05-phase3-build-specification.md | cut -c1-300
```

Check 2 (both O4 questions). Answered without ambiguity: the backtest runs both; every Block 2 pass-gate value is computed on the with series; the without series is never graded. The Block 4 gate is computed against the with series of the arm that trades in Block 4 (arm (a), with the arm (b) case labelled the master's reading), win rate within 15 percentage points, average trade P&L passes if |paper mean - with mean| <= 0.25 x with mean; removed trades leave the with series, stay in the without series and are tabled; paper entries blocked by #2 or #3 are logged, not counted. No defect against check 2.

Check 3 (S2). The trade-deletion rule and Decision 2 are marked CONDITIONAL with assumptions (i) to (iii) and a void clause; engine fill behaviour (ii) and Block 3 build (iii) are covered; early-close behaviour is named as a gap. Master's readings are labelled for: B not a loser; arm (b) replacing arm (a); percentage points and relative-to-mean. Paraphrases checked against the ruling text read this session: R2 (:1556), R4 (:1560-1561), R8 (:1584-1588), A3 (:1730-1734), A6 (:1744-1745), A7 (:1746-1747), C5 (:1836), D-2026-11-04-A (ii) (:761) match. R-VN3-5 does not (defect 2). The D-2026-11-04-A locator for :832 is wrong (defect 1). The full-day #4 claim relies on unobserved NT8 fill timing without a CONDITIONAL mark (defect 3).

Check 4 (S6). Named by the entry: topology :59 versus assumption (iii); values-spec selection statistic; R6 first pass; SHM-4/SHM-5; early-close days. #2 and #3 are treated the same way throughout (both gate new entries only, both "every later entry is dropped", both without approved values, both "redone" under R8), and this matches topology rows #2 and #3. Not named: the full-day 16:00 flat timing conflict between the base strategy and amended #4 / Rule F2-1 (defect 3).

Check 5 (D2, values, code, F3/F4). The entry sets no breaker value (it states spec :99's 2 as spec text and says neither value is approved), decides no D2 item, changes no code or spec body, and states it neither lifts nor depends on F3 or F4. The DECISIONS.md diff against HEAD has 0 removed lines (below). No defect against check 5.

Checks 5 and 6 commands (`/bin/bash /tmp/o4w4/run.sh /tmp/o4w4/cmds2.txt`). Search patterns for the banned strings are built with printf from parts:

```
$ /usr/bin/grep -rn -E '25[- ]trade|25 trades|25 paper' docs/specs/2026-11-05-phase3-build-specification.md specs/SPEC_RUBRIC.md DECISIONS.md | cut -c1-260
DECISIONS.md:2410:**S6 cross-block.** Block 2: R2, R3, A7, A8 unchanged; gate values move to the with series; the values-spec §6 selection statistic is not changed, and whether arm (b) selects on the with series is left to the values-spec unit (named gap: sele
$ /usr/bin/grep -c -F '2026-11-13T05:45:00Z' DECISION_LOG.md
1
$ /usr/bin/grep -n -F '2026-11-13T05:45:00Z' DECISION_LOG.md | cut -c1-400
899:- [2026-11-13T05:45:00Z] WHO: praxis-master | WHAT: **Rubric O3 → PASSED@cae83dc written in `specs/SPEC_RUBRIC.md` (filer's note + moved block; working tree, 8+ / 5−); it rides in this run's close flush, as the F2 move did at `c29d08b` (no MANIFEST row, same precedent).** **Decided by master under D-2026-11-08-D D1: Unit 2 = rubric O4 filing** (bead `Praxis_build-yra`): a manager drafts ONE DE
$ sed -n '2389,2416p' DECISIONS.md | wc -l
      28
$ sed -n '2389,2416p' DECISIONS.md | /usr/bin/grep -c -E '^\*\*(Status|Decision 1|Decision 2|Sources|S6 cross-block|Limits|S4 timing)'
8
$ sed -n '2389,2416p' DECISIONS.md | /usr/bin/grep -o -E '^\*\*[A-Za-z0-9 ]+'
**Status
**Decision 1
**Decision 1 rule 
**Decision 2
**Sources 
**S6 cross
**Limits
**S4 timing
$ tail -n 1 DECISIONS.md | od -c | tail -n 3
0000100    c   k   s   /   s   i   d   e       s   l   i   p   p   a   g
0000120    e       a   s   s   u   m   e   d   .  \n                    
0000133
$ tail -n 1 DECISIONS.md | /usr/bin/grep -c -x -F 'Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.'
1
$ sed -n '2389,2416p' DECISIONS.md | /usr/bin/grep -c -F 'Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.'
1
$ sed -n '2389,2416p' DECISIONS.md | /usr/bin/grep -c -i -F "$(printf '%s%s' verd ict)"
0
$ sed -n '2389,2416p' DECISIONS.md | /usr/bin/grep -c -F "$(printf '%s%s' COMMIT- INDEX)"
0
$ sed -n '2389,2416p' DECISIONS.md | /usr/bin/grep -c -F "$(printf '%s%s' COMMIT-DIFF- SHA256)"
0
$ sed -n '2389,2416p' DECISIONS.md | /usr/bin/grep -c -F "$(printf '%s%s' '..' '.')"
0
$ sed -n '2389,2416p' DECISIONS.md | /usr/bin/grep -c -F "$(printf '\342\200\246')"
0
$ git diff HEAD -- DECISIONS.md | grep -c '^-[^-]'
0
$ git diff HEAD -- DECISIONS.md | grep -c '^+[^+]'
81
$ git diff HEAD -- DECISIONS.md | grep '^@@'
@@ -2277,6 +2277,98 @@ This entry names the governing rule (Rule F2-1) and the 15:00 disposition, and r
@@ -2293,3 +2385,32 @@ Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippag
$ sed -n '2389,2416p' DECISIONS.md | shasum -a 256
4883026d469379ddff0da53c9e6fe4ca61b6746d072830656aa03ffcab23b6de  -
$ git diff --cached --name-only | wc -l
       1
```

Format: 28 lines (under 40); sections Status, Decision 1, Decision 1 rule, Decision 2, Sources, S6 cross-block, Limits, S4 timing present; last line exact and once in the entry; banned strings all 0. Index holds 1 path. The DECISION_LOG 2026-11-13T05:45:00Z row cited in Status exists (count 1).

## Verification evidence for the defects

`/bin/bash /tmp/o4w4/run.sh /tmp/o4w4/cmds4.txt` (its first command used a wrong line number, 2399, and printed nothing; corrected in cmds5 below):

```
$ sed -n '2399p' DECISIONS.md | /usr/bin/grep -o -F -- 'open item D-2026-11-04-A NEEDS AMEAR 4, DECISIONS.md:832'
$ awk 'NR<=832 && /^## /{h=NR": "substr($0,1,90)} NR==832{print h}' DECISIONS.md
803: ## 2026-11-05 — D-2026-11-05-A: Walk-forward design rulings (Amear, voice 2026-11-05)
$ sed -n '832p' DECISIONS.md
4. Is R-1104-3's judged version arm (a), arm (b) or both?
$ sed -n '769,773p' DECISIONS.md | cut -c1-120
**NEEDS AMEAR (questions only, not answered):** Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side
1. What counts as "proof of concept"? (His words name no test; the brief's framing ties it to Standard-resolution result
2. `Praxis_build-r8j` is at P0, the master's choice (D-2026-11-02-C, DECISIONS.md:489; NEEDS AMEAR 13). Is P0 the level 

## 2026-11-04 — D-2026-11-04-B: R-1104-1 — commit gate accepts a praxis-auditor PASS (SubagentStop minter, provenance-ch
$ sed -n '2410p' DECISIONS.md | /usr/bin/grep -c -F -- "Amear's words: R-VN3-5 says \"once they are built\""
1
$ sed -n '510p' DECISIONS.md | /usr/bin/grep -c -F -- "If they're not live, then they're not live."
0
$ sed -n '510p' DECISIONS.md | /usr/bin/grep -c -F -- 'once they are built'
1
$ sed -n '512p' DECISIONS.md | cut -c1-150
- **Settles (against O4):** in the agent's reading, confirmed by Amear in voice only and entered at the ledger row above: the backtest runs **with the
$ sed -n '2410p' DECISIONS.md | /usr/bin/grep -o -F -- "#4: both series carry the strategy's 16:00 flat, so on a full trading day #4 does not split them"
#4: both series carry the strategy's 16:00 flat, so on a full trading day #4 does not split them
$ sed -n '2410p' DECISIONS.md | /usr/bin/grep -c -F -- '3gm C3'
0
$ sed -n '2410p' DECISIONS.md | /usr/bin/grep -c -F -- 'Flat1559'
0
$ sed -n '2412p' DECISIONS.md | /usr/bin/grep -o -F -- 'It does not decide parity for #1 or #6 to #9'
It does not decide parity for #1 or #6 to #9
$ sed -n '105p;108p;189,192p' ninjascript/PraxisNoiseAreaBreakout.cs
				Calculate                                 = Calculate.OnBarClose;
				IsExitOnSessionCloseStrategy              = true;   // backstop; explicit 16:00 flat is primary
			if (mod >= CloseMod)
			{
				FlattenAll("16:00 session flat");
				return;                          // never open a new position at/after the close
$ sed -n '22,26p' ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs
// CHANGE: the flatten decision moves from the 16:00-stamped bar (mod >= 960) to mod >= 959
//   (FlattenMod = CloseMod - 1). The managed market exit is then submitted on the close of the
//   15:59-stamped 1-min bar, so it fills at the 16:00 bar's open on the same day (INFERRED:
//   Calculate.OnBarClose + end-stamped bars + next-bar-open fill; base behaviour is 3gm S1-S5).
// SESSION-AWARE API: no NT8 documentation of SessionIterator behaviour for this use was found;
$ sed -n '352p' DECISIONS.md
4. **3gm C3:** if Flat1559 shows same-day 16:00 fills, does the 15:59 decision become how the replication realises the 16:00 flat, or stay a test variant? (It changes "act at the stamp" semantics, 3gm `:866`.)
$ sed -n '363p' DECISIONS.md | cut -c1-230
- **Still open (NEEDS AMEAR):** 3gm Q1 sizing (b) vs (c) (item 2 above); 3gm Q2, what OppBand means for the base (item 1 above); early-close handling (item 3 above); adoption of the 15:59 decision into the base as the replication'
$ /usr/bin/grep -n -o -F -- 'The closing order for every open system position is submitted no later than 16:00:00 ET' docs/specs/2026-11-05-phase3-build-specification.md
205:The closing order for every open system position is submitted no later than 16:00:00 ET
$ sed -n '117p' docs/specs/2026-11-05-phase3-build-specification.md
Minimum duration: 6 weeks or 25 triggered trades, whichever comes later. Must span at least one FOMC day, one NFP day, and one NQ contract rollover.
```

`/bin/bash /tmp/o4w4/run.sh /tmp/o4w4/cmds5.txt`:

```
$ sed -n '2397p' DECISIONS.md | /usr/bin/grep -o -F -- 'open item D-2026-11-04-A NEEDS AMEAR 4, DECISIONS.md:832'
open item D-2026-11-04-A NEEDS AMEAR 4, DECISIONS.md:832
$ sed -n '509p' DECISIONS.md | /usr/bin/grep -c -F -- "- Amear's words (notes-3 line 28): *\"If they're not live, then they're not live.\"*"
1
$ sed -n '509p' DECISIONS.md | /usr/bin/grep -c -F -- 'once they are built'
0
$ sed -n '510p' DECISIONS.md | cut -c1-80
- Agent's reading, confirmed by Amear in voice only (notes-3 line 29): the backt
$ sed -n '512p' DECISIONS.md | cut -c1-80
- **Settles (against O4):** in the agent's reading, confirmed by Amear in voice 
```

## Defects

1. Wrong source entry for an open item. Decision 2 (DECISIONS.md:2397) says "open item D-2026-11-04-A NEEDS AMEAR 4, DECISIONS.md:832". Line 832 is item 4 of the NEEDS AMEAR list of D-2026-11-05-A (header :803). D-2026-11-04-A's NEEDS AMEAR list (:769-771) has only items 1 and 2. The quoted words are byte-present at :832, but the ruling they are attributed to is the wrong entry.
2. R-VN3-5 paraphrase labelled as Amear's words. The S6 paragraph (:2410) says "Amear's words: R-VN3-5 says "once they are built"". Amear's words for R-VN3-5 are at :509 and do not contain that phrase (count 0). Both :510 and :512 grade it as the agent's reading, confirmed by Amear in voice only. That breaks S2 and the brief's rule to check every paraphrase against the ruling's actual words.
3. Full-day #4 parity: a conflict nobody named, and a mechanism nobody observed, with no CONDITIONAL mark. The entry says "#4: both series carry the strategy's 16:00 flat, so on a full trading day #4 does not split them". It names only early-close days as a gap, and its Limits list of undecided parity ("#1 or #6 to #9") leaves #4 out. But the base strategy only decides to flatten on the close of the 16:00-stamped bar under Calculate.OnBarClose (code :105, :189-191). The Flat1559 header (:22-25) gives the 15:59 move as the way to make the fill land "on the same day", graded INFERRED, which means the base's fill comes later. Meanwhile Rule F2-1 / amended #4 (spec :205) needs the closing order "submitted no later than 16:00:00 ET". Whether the 15:59 decision becomes the base's way of making the 16:00 flat is still NEEDS AMEAR (DECISIONS.md:352 3gm C3; :363 still open). So on a full day, live #4 built to the amended text and the backtest's flat may exit at different times and prices on every trade held to the close. That hits the average-trade-P&L term of the Block 4 gate. The S6 paragraph has 0 hits for 3gm C3 and for Flat1559.

## Non-defects (style notes)

- Decision 1 cites R-1104-3 for "the version closest to live". The "breakers on" content of R-1104-3 is the brief's framing; Amear's word is "Yeah" (DECISIONS.md:752-753). It is used as a pointer and the Status line labels the whole as the master's decision, so it is not graded as a defect.
- The average-trade-P&L term does not say where the paper-side commission comes from: the cost model, or MFFU sim deductions (the latter is unverified per DECISIONS.md:946).
- "a positive with mean being presupposed" does not say what happens if the with mean is 0 or negative. Then the relative band cannot be met.
- Spec :128 ("What you're NOT measuring: P&L") sits beside :124's average-trade-P&L gate. This tension was already in the spec and the entry did not introduce it.

## Files staged
None by this worker. Only this report file was written. `git diff --cached --name-only | wc -l` reads 1 (pasted in check 6 output).

## Result
FAIL

Grade: FAIL (3 defects)
Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
