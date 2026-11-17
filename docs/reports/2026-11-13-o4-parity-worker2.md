# O4 parity adversarial grade, worker 2

## Task
Unit 2026-11-13-o4-parity, bead Praxis_build-yra, rubric O4. Grade DECISIONS.md entry D-2026-11-13-A (lines 2389-2416, working tree, main @ cae83dc) cold. The worker-1 report and the manager report were not read.

## Mode
ADVERSARIAL

## Criterion
SPEC_RUBRIC O4 (verbatim in the brief): a written statement of whether the Block 2 backtest runs with breakers applied, without them, or both, and how the Block 4 gate is satisfiable if they differ. Standing S2 (no component reported above its evidence), S6 (cross-block conflicts named), D2 (four Amear-only items).

## Process log
1. Located the entry and confirmed its span and the index count.
2. Check 1: ran every cited quote against its cited line through a bash runner script (zsh `grep` is ugrep; the script uses /usr/bin/grep). All 30 quote checks return 1. Ran the prescribed term grep: Flat1559 returns 2.
3. Check 2: both O4 questions answered: "runs both, and is graded with breakers"; Block 4 gate against the with series only, with win rate as percentage points (at most 15) and average trade P&L as |paper mean - with mean| at most 0.25 x with mean; removed trades leave the with series, stay in the without series, and go in a removed-trades table. No ambiguity found on this check.
4. Check 3 (S2): the rule and Decision 2 carry CONDITIONAL with three assumptions and a void clause. One unmarked claim found in the S6 paragraph (defect 1). One sourcing defect (defect 4).
5. Check 4 (S6): read topology :52-64, Phase 3 spec :92-128 and :192-242, DECISIONS :186-192, :508-513, :755-765, :1554-1590, :1728-1750, :1771, :1834-1838, :2340-2352, plus the early-close record at :262, :328, :351, :944. Found defects 1, 2, 3.
6. Check 5 (D2, values, F3/F4): no D2 (a), (b), (d) mention; D2 (c) only referenced; no value set; F3/F4 explicitly not lifted and not depended on. Pass.
7. Check 6 (format): 28 lines, all sections present, closing sentence is the file's last line and appears once in the entry, forbidden strings 0, no deleted lines in the DECISIONS.md diff. Pass.

## Verification evidence

### Entry location and index count

```
$ cd /Volumes/Sensidine/Praxis.build && grep -n -F "## 2026-11-13 — D-2026-11-13-A" DECISIONS.md; wc -l DECISIONS.md
2389:## 2026-11-13 — D-2026-11-13-A: Backtest-vs-live breaker parity (rubric O4; master under D-2026-11-08-D D1)
    2416 DECISIONS.md
$ git rev-parse --short HEAD; git diff --cached --name-only | wc -l
cae83dc
       1
```

### Check 1: quotes (runner script /tmp/o4w2/q.sh, then its full output)

Script text (the `q` function prints the command it runs, then runs it; two quotes containing an apostrophe were passed in double quotes, so their printed form shows the apostrophe inside single quotes):

```
#!/bin/bash
cd /Volumes/Sensidine/Praxis.build
P=docs/specs/2026-11-05-phase3-build-specification.md
T=docs/specs/2026-11-10-live-signal-topology.md
S=ninjascript/PraxisNoiseAreaBreakout.cs
D=DECISIONS.md
q(){ local n="$1" f="$2" s="$3"; printf '%s\n' "\$ sed -n '${n}p' $f | grep -c -F -- '$s'"; sed -n "${n}p" "$f" | /usr/bin/grep -c -F -- "$s"; }
q 98 $P 'trade count hits daily max → disable order submission'
q 99 $P '2 consecutive losers in one session → identical to max trades'
q 124 $P 'within ±15% win rate and ±25% average trade P&L'
q 205 $P 'The system opens no new position from that flat time until 18:00 ET, when the next session begins.'
q 224 $P "The system's own trading is not disabled by this breaker"
q 239 $P 'New system entries between 15:00 and 16:00 are allowed under Rule F2-1, subject to breakers #1, #2, #3, #6, #7, #8 and #9.'
q 196 $P 'SPECIFIED ONLY — zero implemented, zero tested, zero tested under failure'
q 212 $P "or the exchange's early close on an early-close day if earlier"
q 42 DECISION_LOG.md 'positions/session = reverse & re-enter on opposite-band cross (NOT one-position/session)'
q 32 $S 'Positions/session = REVERSE & re-enter on an opposite-band cross'
q 189 $S 'if (mod >= CloseMod)'
q 191 $S 'FlattenAll("16:00 session flat");'
q 59 $T 'Deviation C reverse-and-re-enter counts as an entry'
q 58 $T 'must never be blocked by a closed gate'
q 59 $T 'the entry signal'
q 1556 $D 'GO requires arm (a) to pass.'
q 1746 $D 'R3 amends Q8: arm (a) is judged on gates 1-5 (WFE not'
q 1748 $D 'O1 is discharged by R2 + R3 + A7.'
q 1731 $D 'W / (W + L + 0.5 x B), B = trade exited at its entry price.'
q 1733 $D '"within +/-15% win rate" check, computed identically on backtest'
q 1836 $D 'win/loss judged by price'
q 512 $D 'the backtest runs **with the breakers on, once they are built**'
q 761 $D 'when the time comes ask agaian.'
q 1584 $D '#2 max 2 trades/day, #3 two-and-done'
q 1588 $D 'New values come back to Amear as'
q 189 $D 'SHM-4: win-rate >15 ppts below backtest OR slippage >2 ticks/side worse, over a 20-trade window.'
q 2350 $D 'without breakers as design :116 (O4) states'
q 55 docs/reports/2026-11-09-d6-drawdown-check-manager.md 'every later trade that session is skipped'
printf '%s\n' "\$ git show bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md | sed -n 116p | grep -c -F -- 'First pass runs without breakers (no approved values; D6 E4) and says so; a breakers-on run waits for F2.'"
git show bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md | sed -n 116p | /usr/bin/grep -c -F -- 'First pass runs without breakers (no approved values; D6 E4) and says so; a breakers-on run waits for F2.'
printf '%s\n' "\$ bd show Praxis_build-yra | grep -c -F 'the live-vs-backtest gate is structurally unmeetable.'"
bd show Praxis_build-yra | /usr/bin/grep -c -F 'the live-vs-backtest gate is structurally unmeetable.'
printf '%s\n' '$ grep -c -i -E "MaxTrades|TradeCount|tradesToday|consecutive|loser|LossStreak|early" ninjascript/PraxisNoiseAreaBreakout*.cs'
/usr/bin/grep -c -i -E "MaxTrades|TradeCount|tradesToday|consecutive|loser|LossStreak|early" ninjascript/PraxisNoiseAreaBreakout*.cs
```

```
$ /bin/bash /tmp/o4w2/q.sh 2>&1
$ sed -n '98p' docs/specs/2026-11-05-phase3-build-specification.md | grep -c -F -- 'trade count hits daily max → disable order submission'
1
$ sed -n '99p' docs/specs/2026-11-05-phase3-build-specification.md | grep -c -F -- '2 consecutive losers in one session → identical to max trades'
1
$ sed -n '124p' docs/specs/2026-11-05-phase3-build-specification.md | grep -c -F -- 'within ±15% win rate and ±25% average trade P&L'
1
$ sed -n '205p' docs/specs/2026-11-05-phase3-build-specification.md | grep -c -F -- 'The system opens no new position from that flat time until 18:00 ET, when the next session begins.'
1
$ sed -n '224p' docs/specs/2026-11-05-phase3-build-specification.md | grep -c -F -- 'The system's own trading is not disabled by this breaker'
1
$ sed -n '239p' docs/specs/2026-11-05-phase3-build-specification.md | grep -c -F -- 'New system entries between 15:00 and 16:00 are allowed under Rule F2-1, subject to breakers #1, #2, #3, #6, #7, #8 and #9.'
1
$ sed -n '196p' docs/specs/2026-11-05-phase3-build-specification.md | grep -c -F -- 'SPECIFIED ONLY — zero implemented, zero tested, zero tested under failure'
1
$ sed -n '212p' docs/specs/2026-11-05-phase3-build-specification.md | grep -c -F -- 'or the exchange's early close on an early-close day if earlier'
1
$ sed -n '42p' DECISION_LOG.md | grep -c -F -- 'positions/session = reverse & re-enter on opposite-band cross (NOT one-position/session)'
1
$ sed -n '32p' ninjascript/PraxisNoiseAreaBreakout.cs | grep -c -F -- 'Positions/session = REVERSE & re-enter on an opposite-band cross'
1
$ sed -n '189p' ninjascript/PraxisNoiseAreaBreakout.cs | grep -c -F -- 'if (mod >= CloseMod)'
1
$ sed -n '191p' ninjascript/PraxisNoiseAreaBreakout.cs | grep -c -F -- 'FlattenAll("16:00 session flat");'
1
$ sed -n '59p' docs/specs/2026-11-10-live-signal-topology.md | grep -c -F -- 'Deviation C reverse-and-re-enter counts as an entry'
1
$ sed -n '58p' docs/specs/2026-11-10-live-signal-topology.md | grep -c -F -- 'must never be blocked by a closed gate'
1
$ sed -n '59p' docs/specs/2026-11-10-live-signal-topology.md | grep -c -F -- 'the entry signal'
1
$ sed -n '1556p' DECISIONS.md | grep -c -F -- 'GO requires arm (a) to pass.'
1
$ sed -n '1746p' DECISIONS.md | grep -c -F -- 'R3 amends Q8: arm (a) is judged on gates 1-5 (WFE not'
1
$ sed -n '1748p' DECISIONS.md | grep -c -F -- 'O1 is discharged by R2 + R3 + A7.'
1
$ sed -n '1731p' DECISIONS.md | grep -c -F -- 'W / (W + L + 0.5 x B), B = trade exited at its entry price.'
1
$ sed -n '1733p' DECISIONS.md | grep -c -F -- '"within +/-15% win rate" check, computed identically on backtest'
1
$ sed -n '1836p' DECISIONS.md | grep -c -F -- 'win/loss judged by price'
1
$ sed -n '512p' DECISIONS.md | grep -c -F -- 'the backtest runs **with the breakers on, once they are built**'
1
$ sed -n '761p' DECISIONS.md | grep -c -F -- 'when the time comes ask agaian.'
1
$ sed -n '1584p' DECISIONS.md | grep -c -F -- '#2 max 2 trades/day, #3 two-and-done'
1
$ sed -n '1588p' DECISIONS.md | grep -c -F -- 'New values come back to Amear as'
1
$ sed -n '189p' DECISIONS.md | grep -c -F -- 'SHM-4: win-rate >15 ppts below backtest OR slippage >2 ticks/side worse, over a 20-trade window.'
1
$ sed -n '2350p' DECISIONS.md | grep -c -F -- 'without breakers as design :116 (O4) states'
1
$ sed -n '55p' docs/reports/2026-11-09-d6-drawdown-check-manager.md | grep -c -F -- 'every later trade that session is skipped'
1
$ git show bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md | sed -n 116p | grep -c -F -- 'First pass runs without breakers (no approved values; D6 E4) and says so; a breakers-on run waits for F2.'
1
$ bd show Praxis_build-yra | grep -c -F 'the live-vs-backtest gate is structurally unmeetable.'
1
$ grep -c -i -E "MaxTrades|TradeCount|tradesToday|consecutive|loser|LossStreak|early" ninjascript/PraxisNoiseAreaBreakout*.cs
ninjascript/PraxisNoiseAreaBreakout.cs:0
ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:2
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:0
```

The two Flat1559 hits:

```
$ /usr/bin/grep -n -i -E "MaxTrades|TradeCount|tradesToday|consecutive|loser|LossStreak|early" ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs
37:// EARLY-CLOSE DAYS (INFERRED): a session that ends before 15:59 ET never reaches mod 959, so this
91:		private const int FlattenMod = CloseMod - 1;   // 959 = 15:59 ET — variant 7zq: submit the flat one bar early
```

Every quoted string checked is byte-present at its cited line (30 of 30).

### Checks 3 and 4: evidence for defects (runner scripts /tmp/o4w2/e.sh and /tmp/o4w2/e2.sh; each line prefixed `$` is the command run, followed by its full output, including one regex error that e2.sh re-ran)

```
$ /bin/bash /tmp/o4w2/e.sh 2>&1
$ sed -n '2410p' DECISIONS.md | /usr/bin/grep -o -E 'on an early-close day amended #4.{0,330}'
grep: maximum repetition exceeds 255
$ sed -n '108,109p' ninjascript/PraxisNoiseAreaBreakout.cs
				IsExitOnSessionCloseStrategy              = true;   // backstop; explicit 16:00 flat is primary
				ExitOnSessionCloseSeconds                 = 30;
$ sed -n '944p' DECISIONS.md | cut -c1-140
  - reading (voice agent, notes-4): 33 missing sessions and the 12:15 early-close exits are accepted as is. No fix before results are judged
$ sed -n '351p' DECISIONS.md
3. **Early-close handling:** once the template's early-close rows (3gm R4) and the early-close trades (R6) are read, should a session-aware flat be built, and where?
$ sed -n '2410p' DECISIONS.md | /usr/bin/grep -c -E 'IsExitOnSessionClose|:108|:944|:351'
0
$ sed -n '2395p' DECISIONS.md | /usr/bin/grep -o -E '#2: once.{0,120}|#3: once.{0,200}'
#2: once the session's entry count reaches the #2 maximum in the Phase 3 spec at run time, every later entry is dropped. #3: onc
$ sed -n '2412p' DECISIONS.md | /usr/bin/grep -o -E 'none can be produced until #2.{0,110}'
none can be produced until #2 has an approved value (R8: PROPOSED; D2 (c) once real money is at stake); this entry sets none. If R8's redo 
$ sed -n '1584,1588p' DECISIONS.md
    for the automated book: #2 max 2 trades/day, #3 two-and-done,
    #4 flat at 11:30, #5 as a disable of the system's own trading
    15:00–18:00, #8 inter-trade interval under 5 minutes.
    KEEP: #1 daily loss limit; #5 as a lockout on Amear's own
    interaction 15:00–18:00. New values come back to Amear as
$ sed -n '1745,1746p' DECISIONS.md
    when Amear approves the proposed values.
A7  R3 amends Q8: arm (a) is judged on gates 1-5 (WFE not
$ sed -n '1560,1561p' DECISIONS.md
    - Win rate: no-trade days excluded; a break-even trade counts as
      half a loss.
$ sed -n '2389,2416p' DECISIONS.md | /usr/bin/grep -c -E 'R4|half a loss|A6'
0
$ sed -n '2402p' DECISIONS.md | /usr/bin/grep -o -E 'No trade cap.{0,170}'
No trade cap and no loser-streak stop: zero hits for those terms in all three `PraxisNoiseAreaBreakout*.cs` (manager report). Implemented: reverse and 16:00 flat. Not implemented: #2
```

```
$ /bin/bash /tmp/o4w2/e2.sh 2>&1
$ sed -n '2410p' DECISIONS.md | /usr/bin/grep -o -E 'on an early-close day amended #4.{0,250}'
on an early-close day amended #4 flattens "or the exchange's early close on an early-close day if earlier" (spec :212) and the strategy has no early-close rule (code :189 tests 16:00 only), so live differs from both series on those days (named conflict, not resolved here; whether t
$ sed -n '2395p' DECISIONS.md | /usr/bin/grep -o -E '#3: once.{0,200}'
#3: once the session's run of consecutive losing closed trades reaches the #3 count in the Phase 3 spec at run time (2 at :99), every later entry is dropped; a loser is L as A3 and C5 (i) define it (by price)
$ sed -n '1744,1745p' DECISIONS.md
A6  FLAG 6: R8 starts the breaker PROPOSAL unit. F2's state changes
    when Amear approves the proposed values.
```

Context reads used for the S6 hunt (outputs not pasted in full, because the source text contains sequences this report may not reproduce; the lines relied on are re-run narrowly above): `sed -n '1554,1590p' DECISIONS.md`, `sed -n '1728,1750p' DECISIONS.md`, `sed -n '2340,2352p' DECISIONS.md`, `sed -n '52,64p' docs/specs/2026-11-10-live-signal-topology.md`, `sed -n '192,242p' docs/specs/2026-11-05-phase3-build-specification.md`. The early-close record search:

```
$ cd /Volumes/Sensidine/Praxis.build && /usr/bin/grep -n -i -E "early.close" DECISIONS.md | cut -c1-200 | head -12
262:  - same-bar exit+reverse resolution (CANNOT-DETERMINE-STATICALLY, INFERRED) — fill resolution may bear on this (3gm `:784`, INFERRED); early-close days (CANNOT-DETERMINE-STATICALLY, INFERRED).
328:  - *Limits:* on early-close sessions ending before 15:59 ET the decision logic that day is identical to the base (backstop only; 3gm `:733`/`:842`), but the position/state carried into that day c
333:- **Third file — one new researched NQ intraday strategy, built in milestone M2:** **`PraxisLastHalfHourMomentum`** (`ninjascript/PraxisLastHalfHourMomentum.cs`, class and strategy name `PraxisLas
351:3. **Early-close handling:** once the template's early-close rows (3gm R4) and the early-close trades (R6) are read, should a session-aware flat be built, and where?
363:- **Still open (NEEDS AMEAR):** 3gm Q1 sizing (b) vs (c) (item 2 above); 3gm Q2, what OppBand means for the base (item 1 above); early-close handling (item 3 above); adoption of the 15:59 decision
506:- **Leaves open:** F2 (session-flat time vs breakers #4 and #5) is not touched by this ruling and stays FROZEN; the early-close stamp question (handoff §5 item 1) is separate and not ruled.
536:6. Not ruled (notes-3 line 40): how does Amear rule on handoff §5 items 1 (early-close stamps, F2), 5 (settings not visible in the screenshots), 6 (baseline settings screenshot), 7 (VM hash-check 
694:26. Line 63: *"§3.3 items (strategy-file hash check, template early-close readback): do them or not?"* Same as C-6 (11-01 handoff §5 items 7 and 1). The 11-02 handoff §3.3 (lines 56–58) puts them 
944:  - reading (voice agent, notes-4): 33 missing sessions and the 12:15 early-close exits are accepted as is. No fix before results are judged. Basis: baseline shape matches the published NQ replica
969:- (ii) R-VN4-3 and R-VN4-5 with D-2026-11-05-A (DECISIONS.md:803) and D-2026-11-05-C (DECISIONS.md:881): walk-forward on the existing minute data; the data is used as is (33 missing sessions, 12:1
1360:| Data | Used as is; each window reports its hole dates and early-close sessions | SETTLED; alternative: no per-window count ((B) 37) | §5 |
```

### Checks 5 and 6: D2, F3/F4, format (runner script /tmp/o4w2/f.sh)

Script text:

```
#!/bin/bash
cd /Volumes/Sensidine/Praxis.build
run(){ printf '%s\n' "\$ $1"; eval "$1"; }
run "sed -n '2389,2416p' DECISIONS.md | wc -l"
run "sed -n '2389,2416p' DECISIONS.md | /usr/bin/grep -c -E '^\*\*(Status|Decision 1|Decision 2|Sources|S6 cross-block|Limits|S4 timing)'"
run "sed -n '2389,2416p' DECISIONS.md | /usr/bin/grep -o -E '^\*\*(Status|Decision [12][^*]*|Sources[^*]*|S6 cross-block|Limits|S4 timing)'"
run "tail -n 1 DECISIONS.md"
run "tail -n 1 DECISIONS.md | /usr/bin/grep -c -x -F 'Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.'"
run "sed -n '2389,2416p' DECISIONS.md | /usr/bin/grep -c -F 'Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.'"
V=$(printf 'ver%s' 'dict'); CI=$(printf 'COMMIT-%s' 'INDEX'); CD=$(printf 'COMMIT-DIFF-%s' 'SHA256'); DOTS=$(printf '\x2e\x2e\x2e'); ELL=$(printf '\xe2\x80\xa6')
for pat in V CI CD DOTS ELL; do printf '%s\n' "\$ sed -n '2389,2416p' DECISIONS.md | grep -c -i -F -- \"\$$pat\""; sed -n '2389,2416p' DECISIONS.md | /usr/bin/grep -c -i -F -- "${!pat}"; done
run "git diff HEAD -- DECISIONS.md | /usr/bin/grep -c '^-[^-]'"
run "sed -n '2389,2416p' DECISIONS.md | shasum -a 256"
run "git diff --cached --name-only | wc -l"
run "sed -n '2389,2416p' DECISIONS.md | /usr/bin/grep -c -E 'D2 ?\(a\)|D2 ?\(b\)|D2 ?\(d\)'"
run "sed -n '2389,2416p' DECISIONS.md | /usr/bin/grep -o -E '.{60}F[34].{60}'"
```

```
$ /bin/bash /tmp/o4w2/f.sh 2>&1
$ sed -n '2389,2416p' DECISIONS.md | wc -l
      28
$ sed -n '2389,2416p' DECISIONS.md | /usr/bin/grep -c -E '^\*\*(Status|Decision 1|Decision 2|Sources|S6 cross-block|Limits|S4 timing)'
8
$ sed -n '2389,2416p' DECISIONS.md | /usr/bin/grep -o -E '^\*\*(Status|Decision [12][^*]*|Sources[^*]*|S6 cross-block|Limits|S4 timing)'
**Status
**Decision 1: the Block 2 backtest runs both, and is graded with breakers.
**Decision 1 rule (CONDITIONAL).
**Decision 2: how the Block 4 gate is satisfiable (CONDITIONAL on assumptions (i) and (iii) above; same void clause).
**Sources (quoted byte-exact; DECISIONS.md lines are the working tree).
**S6 cross-block
**Limits
**S4 timing
$ tail -n 1 DECISIONS.md
Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
$ tail -n 1 DECISIONS.md | /usr/bin/grep -c -x -F 'Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.'
1
$ sed -n '2389,2416p' DECISIONS.md | /usr/bin/grep -c -F 'Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.'
1
$ sed -n '2389,2416p' DECISIONS.md | grep -c -i -F -- "$V"
0
$ sed -n '2389,2416p' DECISIONS.md | grep -c -i -F -- "$CI"
0
$ sed -n '2389,2416p' DECISIONS.md | grep -c -i -F -- "$CD"
0
$ sed -n '2389,2416p' DECISIONS.md | grep -c -i -F -- "$DOTS"
0
$ sed -n '2389,2416p' DECISIONS.md | grep -c -i -F -- "$ELL"
0
$ git diff HEAD -- DECISIONS.md | /usr/bin/grep -c '^-[^-]'
0
$ sed -n '2389,2416p' DECISIONS.md | shasum -a 256
16303ca54337fce8b558c71a58e34ab01b576cea4d6ec75836cef058e6ca9fe3  -
$ git diff --cached --name-only | wc -l
       1
$ sed -n '2389,2416p' DECISIONS.md | /usr/bin/grep -c -E 'D2 ?\(a\)|D2 ?\(b\)|D2 ?\(d\)'
0
$ sed -n '2389,2416p' DECISIONS.md | /usr/bin/grep -o -E '.{60}F[34].{60}'
 and every gate value on it is recomputed. It does not lift F3 or F4 and depends on neither: the fill resolution of any ru
```

Ledger row named in Status exists and dispatches this unit:

```
$ cd /Volumes/Sensidine/Praxis.build && /usr/bin/grep -n -F "2026-11-13T05:45:00Z" DECISION_LOG.md | cut -c1-400
899:- [2026-11-13T05:45:00Z] WHO: praxis-master | WHAT: **Rubric O3 → PASSED@cae83dc written in `specs/SPEC_RUBRIC.md` (filer's note + moved block; working tree, 8+ / 5−); it rides in this run's close flush, as the F2 move did at `c29d08b` (no MANIFEST row, same precedent).** **Decided by master under D-2026-11-08-D D1: Unit 2 = rubric O4 filing** (bead `Praxis_build-yra`): a manager drafts ONE DE
```

## Defects

1. **S2 and S6: the early-close conflict is stated as fact on an incomplete read and an unobserved mechanism, with no CONDITIONAL marking.** DECISIONS.md:2410 says "the strategy has no early-close rule (code :189 tests 16:00 only), so live differs from both series on those days". The same strategy file sets `IsExitOnSessionCloseStrategy = true` with `ExitOnSessionCloseSeconds = 30` at :108-109, an exit-at-session-end backstop, and DECISIONS.md:944 records that the baselines already show "12:15 early-close exits", accepted as is. So the backtest series may already flatten at the early close, as amended #4 does. Whether they differ depends on NT8 session-template behaviour that the entry has not observed. The claim carries no assumption and no void observation. It also does not name the open early-close item, D-2026-10-31-A item 3 (DECISIONS.md:351, still NEEDS AMEAR at :363). The search for `IsExitOnSessionClose|:108|:944|:351` on line 2410 returns 0.
2. **S6: breaker values #2 and #3 are treated inconsistently.** The rule uses #3's count from the spec "at run time (2 at :99)" as live input (DECISIONS.md:2395). But it treats #2 as having no value, so no with series exists "until #2 has an approved value" (:2412). R8 (:1584) lists both "#2 max 2 trades/day, #3 two-and-done" as manual-trading values to be redone, with new values "PROPOSED" (:1588). A6 (:1744-1745) says F2's state changes only "when Amear approves the proposed values". R6 design :116 says "no approved values". Neither #2 nor #3 has an approved automated-book value. The entry gates on approval for one and not the other, and it does not name A6.
3. **S6: break-even handling in #3 is an interpretation that is not flagged, and the conflict with R4 is not named.** The rule says "a B trade is not a loser and breaks the run" (DECISIONS.md:2395). This is not derived from A3 or C5 (i): A3 defines only B, and C5 (i) only judges by price. R4 (DECISIONS.md:1560-1561) says "a break-even trade counts as half a loss". The entry does not name R4 or that conflict (the count for `R4|half a loss|A6` in the entry is 0). It does not mark the B rule as the master's reading, and none of assumptions (i) to (iii) covers it. Through assumption (iii), the rule then binds the Block 3 build.
4. **S2 sourcing: the "zero hits" claim cannot be reproduced.** DECISIONS.md:2402 says "zero hits for those terms in all three `PraxisNoiseAreaBreakout*.cs` (manager report)". The entry does not list the terms or give a path to the report. The term set prescribed for this grade returns `PraxisNoiseAreaBreakout_Flat1559.cs:2`. Both hits are "early" comment hits (:37, :91), not trade-cap or loser-streak logic. The underlying point, that #2 and #3 are not implemented, holds when the code is read. But the measurement as written ("zero hits") is not something a reader can re-run, and with the prescribed terms it is false.

Checks with no defect: check 1 (30 of 30 quotes byte-present), check 2 (both O4 questions answered without ambiguity), check 5 (no D2 item decided, no value set, F3/F4 not lifted or depended on), check 6 (format, closing line, forbidden strings, no deleted lines).

## Files staged
None by this worker. Index count unchanged at 1 (pasted above). Only this report file was written.

## Result
FAIL (4 defects). Entry sha256 at grading: 16303ca54337fce8b558c71a58e34ab01b576cea4d6ec75836cef058e6ca9fe3.

Grade: FAIL (4 defects)
Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
