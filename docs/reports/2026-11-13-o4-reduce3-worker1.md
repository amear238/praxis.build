# O4 reduce-3, worker 1: adversarial check of D-2026-11-13-A (DECISIONS.md:2389-2416)

**Task:** cold adversarial check of the edited entry, seven checks (a)-(g). Checks (a)-(e) are run as `docs/reports/2026-11-13-o4-reduce2-worker1.md` defines them. Check (f) is redefined for this round: the diff changes lines 2393, 2405 and 2410 only. Check (g) grades that report's three "Observations (not defects)". **Mode:** ADVERSARIAL, one round, read-only. **Criterion:** rubric O4, `specs/SPEC_RUBRIC.md:117-122`.

**Process log:** read the prior report in full; printed DECISIONS.md:2380-2416 and the rubric O4 text; ran the full diff against `/tmp/o4red3-pre-DECISIONS.md` and `wc -l` on both files; re-ran the quote byte check (29 records), the bf6fcc7:116, R4 :1560-1561, bead and zero-hit checks; extracted the entry's labels, CONDITIONAL marks and every "Amear" and "reading" occurrence; read R2-R8 (:1556-1590), SHM-4/SHM-5 (:189), D-2026-11-08-D D1/D2 (:1907-1916), A6 (:1774), spec Amendment 1 authority (:194) and breaker #5 text (:220-224); gathered evidence for each prior observation. No file other than this report was written. DECISIONS.md was not modified.

## Verification evidence (command output)

### E1: full diff and line counts (check f)
```
$ cd /Volumes/Sensidine/Praxis.build && diff /tmp/o4red3-pre-DECISIONS.md DECISIONS.md; echo "diff exit=$?"; wc -l /tmp/o4red3-pre-DECISIONS.md DECISIONS.md; diff /tmp/o4red3-pre-DECISIONS.md DECISIONS.md | /usr/bin/grep -E '^[0-9]'
2393c2393
< **Decision 1: the Block 2 backtest runs both, and is graded with breakers.** Every Block 2 run yields two series from one trade list. The *without* series is the raw list as the strategy emits it (reverse-and-re-enter, 16:00 flat, no trade cap, no loser stop). The *with* series is that list after breakers #2 and #3 are applied to it after the run, Mac-side, by the rule below. Every Block 2 pass-gate value (arm (a) gates 1-5; arm (b) gates 1-6 and PBO) is computed on the with series. The without series is a record of what the breakers cost or saved; it is never graded. The 2026-11-01 runs are without-series records only.
---
> **Decision 1: the Block 2 backtest runs both, and is graded with breakers.** Every Block 2 run yields two series from one trade list. The *without* series is the raw list as the strategy emits it (reverse-and-re-enter, 16:00 flat, no trade cap, no loser stop). The *with* series is that list after breakers #2 and #3 are applied to it after the run, Mac-side, by the rule below. Every Block 2 pass-gate value (arm (a) gates 1-5; arm (b) gates 1-6 and PBO) is computed on the with series. The without series is a record of what the breakers cost or saved; it is never graded.
2405c2405
< - Breakers on (DECISIONS.md): :512 "the backtest runs **with the breakers on, once they are built**"; R8 :1584 "#2 max 2 trades/day, #3 two-and-done" and :1588 "New values come back to Amear as".
---
> - Breakers on (DECISIONS.md): :512 "the backtest runs **with the breakers on, once they are built**" (the agent's reading, confirmed by Amear in voice only, :512); R8 :1584 "#2 max 2 trades/day, #3 two-and-done" and :1588 "New values come back to Amear as".
2410c2410
< **S6 cross-block.** Block 2: R2, R3, A7, A8 unchanged; gate values move to the with series; the values-spec §6 selection statistic is not changed, and whether arm (b) selects on the with series is left to the values-spec unit (named gap: selecting on one series and grading on the other). Block 3 breakers: assumption (iii) is a parity requirement on the later build, not an edit; it conflicts with topology :59 as written, which drops "the entry signal" whole, so a reversal sent as one SELL or BUY would leave the position open; neither #2 nor #3 has an approved value, and R8 says both are redone. Block 4 gate: spec :124 and the 25-trade minimum unchanged; Decision 2 fixes only the series and the arithmetic. R6 parked research: its first pass is a without series by its own design and is no Block 4 reference; nothing in R6 changes. SHM: SHM-4 and SHM-5's "backtest" is read as the with series, bands unchanged; SHM-4 is one-sided over 20 trades, the Block 4 gate is two-sided over the paper period, and neither replaces the other. #4 parity (the full-day flat's timing against the strategy's 16:00 bar-close flat, and early-close days) is not decided here. #5 (the session window) is an operator lockout with no effect on system trades; #1 and #6 to #9 are applied in neither series.
---
> **S6 cross-block.** Block 2: R2, R3, A7, A8 unchanged; gate values move to the with series; the values-spec §6 selection statistic is not changed, and whether arm (b) selects on the with series is left to the values-spec unit (named gap: selecting on one series and grading on the other). Block 3 breakers: assumption (iii) is a parity requirement on the later build, not an edit; it conflicts with topology :59 as written, which drops "the entry signal" whole, so a reversal sent as one SELL or BUY would leave the position open; neither #2 nor #3 has an approved value, and R8 says both are redone. Block 4 gate: spec :124 and the 25-trade minimum unchanged; Decision 2 fixes only the series and the arithmetic. R6 parked research: its first pass is a without series by its own design and is no Block 4 reference; nothing in R6 changes. SHM: SHM-4 and SHM-5's "backtest" is read as the with series (the master's reading under D1, changeable), bands unchanged; SHM-4 is one-sided over 20 trades, the Block 4 gate is two-sided over the paper period, and neither replaces the other. #4 parity (the full-day flat's timing against the strategy's 16:00 bar-close flat, and early-close days) is not decided here. #5 (the session window) is an operator lockout with no effect on system trades; #1 and #6 to #9 are applied in neither series.
diff exit=1
    2416 /tmp/o4red3-pre-DECISIONS.md
    2416 DECISIONS.md
    4832 total
2393c2393
2405c2405
2410c2410
```

### E2: quote byte check, 29 records (check a)
```
$ cd /Volumes/Sensidine/Praxis.build && bash <<'EOF'
p=0; m=0
S=docs/specs/2026-11-05-phase3-build-specification.md
T=docs/specs/2026-11-10-live-signal-topology.md
N=ninjascript/PraxisNoiseAreaBreakout.cs
D=DECISIONS.md
while IFS='|' read -r f l s; do
  [ -z "$f" ] && continue
  case $f in S) f=$S;; T) f=$T;; N) f=$N;; D) f=$D;; esac
  if sed -n "${l}p" "$f" | /usr/bin/grep -qF -- "$s"; then p=$((p+1)); else m=$((m+1)); echo "MISS $f:$l [$s]"; fi
done <<'R'
S|98|trade count hits daily max → disable order submission
S|99|2 consecutive losers in one session → identical to max trades
S|124|within ±15% win rate and ±25% average trade P&L
S|205|The system opens no new position from that flat time until 18:00 ET, when the next session begins.
S|224|The system's own trading is not disabled by this breaker
S|239|New system entries between 15:00 and 16:00 are allowed under Rule F2-1, subject to breakers #1, #2, #3, #6, #7, #8 and #9.
S|196|SPECIFIED ONLY — zero implemented, zero tested, zero tested under failure
DECISION_LOG.md|42|positions/session = reverse & re-enter on opposite-band cross (NOT one-position/session)
N|32|Positions/session = REVERSE & re-enter on an opposite-band cross
N|189|if (mod >= CloseMod)
N|191|FlattenAll("16:00 session flat");
T|59|Deviation C reverse-and-re-enter counts as an entry
T|58|must never be blocked by a closed gate
T|59|the entry signal
D|1556|GO requires arm (a) to pass.
D|1746|R3 amends Q8: arm (a) is judged on gates 1-5 (WFE not
D|1748|O1 is discharged by R2 + R3 + A7.
D|1731|W / (W + L + 0.5 x B), B = trade exited at its entry price.
D|1733|"within +/-15% win rate" check, computed identically on backtest
D|1836|win/loss judged by price
D|512|the backtest runs **with the breakers on, once they are built**
D|1584|#2 max 2 trades/day, #3 two-and-done
D|1588|New values come back to Amear as
D|189|SHM-4: win-rate >15 ppts below backtest OR slippage >2 ticks/side worse, over a 20-trade window.
D|2350|without breakers as design :116 (O4) states
docs/reports/2026-11-09-d6-drawdown-check-manager.md|55|every later trade that session is skipped
D|511|Deviation C
D|2072|Deviation C
D|1771|within +/-15% win rate
R
echo "present=$p missing=$m"
EOF
MISS DECISIONS.md:1771 [within +/-15% win rate]
present=28 missing=1
```
The one miss is my own probe record, not an entry quote: the entry cites :1771 only as "(pointer :1771)" with no quoted string, and I guessed ASCII "+/-". Line 1771 carries the Unicode form (E3, first output line `1`):
```
$ cd /Volumes/Sensidine/Praxis.build && sed -n '1771p' DECISIONS.md | cut -c1-400; echo ---; sed -n '1733p' DECISIONS.md | cut -c1-400; echo ---; sed -n '511,512p' DECISIONS.md | cut -c1-600; echo ---; sed -n '2072p' DECISIONS.md | cut -c1-300
- **A3.** *Answers:* FLAG 3 (:1642). *Bears on:* O4 (`specs/SPEC_RUBRIC.md:94-99`; the Block 4 "within ±15% win rate", :96-97, joined) and R4's win-rate line (DECISIONS.md:1560–1561, "a break-even trade counts as half a loss", joined). O4's "**Required:**" statement (whether the Block 2 backtest runs with breakers applied, without them, or both; :97-99) is not addressed by A3, and O4 is not discha
---
    "within +/-15% win rate" check, computed identically on backtest
---
- **O4 criterion** (`specs/SPEC_RUBRIC.md:94-99`, verbatim): *"Deviation C permits reverse-and-re-enter. Breakers #2 and #3 cap trades and end the session after two consecutive losers. Block 4's gate compares live to backtest within ±15% win rate and ±25% average trade P&L. **Required:** a written statement of whether the Block 2 backtest runs with breakers applied, without them, or both — and how the Block 4 gate is satisfiable if they differ."*
- **Settles (against O4):** in the agent's reading, confirmed by Amear in voice only and entered at the ledger row above: the backtest runs **with the breakers on, once they are built** (notes-3 line 29). Filer's mapping, not part of the ruling: O4 asks this of the Block 2 backtest. The ruling says nothing about any other run (see Leaves open).
---
**S6 cross-block (from topology doc §7, :112).** Block 1 (emitter changes from TradingView to NT8; the TESTED pipe is reused; Deviation G's ingress question leaves the anchor's live path); Block 2 (emitter-vs-backtest parity under O4); Block 3 (all nine breakers, Redis, PostgreSQL, the fallback scri
```

### E3: remaining quote, bead, zero-hit and heading checks (check a)
```
$ cd /Volumes/Sensidine/Praxis.build && sed -n '1771p' DECISIONS.md | /usr/bin/grep -cF 'within ±15% win rate'; sed -n '512p' DECISIONS.md | /usr/bin/grep -cF "the agent's reading, confirmed by Amear in voice only"; git show bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md | sed -n '116p' | /usr/bin/grep -cF 'First pass runs without breakers (no approved values; D6 E4) and says so; a breakers-on run waits for F2.'; sed -n '1560,1561p' DECISIONS.md | tr -s ' \n' ' ' | /usr/bin/grep -cF 'a break-even trade counts as half a loss'; bd show Praxis_build-yra 2>&1 | /usr/bin/grep -cF 'the live-vs-backtest gate is structurally unmeetable.'; /usr/bin/grep -cE 'MaxTrades|TradeCount|tradesToday|consecutive|loser|LossStreak' ninjascript/PraxisNoiseAreaBreakout*.cs | tr '\n' ' '; echo; /usr/bin/grep -c '^## .*Deviation C' DECISIONS.md; /usr/bin/grep -c '2026-11-13T05:45:00Z' DECISION_LOG.md; ls docs/reports/2026-11-13-o4-parity-manager.md
1
1
1
1
1
ninjascript/PraxisNoiseAreaBreakout.cs:0 ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:0 ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:0 
0
1
docs/reports/2026-11-13-o4-parity-manager.md
```

### E4: labels, CONDITIONAL marks, attributions and readings in the entry (checks b, c, d, e)
```
$ cd /Volumes/Sensidine/Praxis.build && sed -n '2389,2415p' DECISIONS.md | /usr/bin/grep -oE "master's reading[^;.)]*|is the master's[^.]*|read as the with series \([^)]*\)|CONDITIONAL[^.]*|Void if any one is observed false|this entry sets none|No code, no strategy file, no breaker value and no spec body is changed|runs both, and is graded with breakers|The gate compares Block 4 paper trades against the with series only|never re-run on the without series|named gap[^)]*|No with series exists yet|conflicts with topology :59" | sort | uniq -c; echo ---AMEAR---; sed -n '2389,2415p' DECISIONS.md | /usr/bin/grep -noE ".{0,60}Amear.{0,60}"; echo ---READ---; sed -n '2389,2415p' DECISIONS.md | /usr/bin/grep -noE ".{0,50}(read as|Reading|reading).{0,60}"
   1 CONDITIONAL on assumptions (i) and (iii) above; same void clause)
   1 CONDITIONAL rest on a mechanism nobody has observed and carry a void clause
   1 CONDITIONAL)
   1 No code, no strategy file, no breaker value and no spec body is changed
   1 No with series exists yet
   1 The gate compares Block 4 paper trades against the with series only
   1 Void if any one is observed false
   1 conflicts with topology :59
   1 is the master's reading under D1, changeable), over its full test span, at the cost model in force
   1 is the master's reading under D1, changeable; R4's "a break-even trade counts as" half a loss (DECISIONS
   1 is the master's, under D1, changeable
   1 named gap: selecting on one series and grading on the other
   1 never re-run on the without series
   1 read as the with series (the master's reading under D1, changeable)
   1 runs both, and is graded with breakers
   1 this entry sets none
---AMEAR---
3:-08-D D1 (DECISION_LOG 2026-11-13T05:45:00Z), changeable by Amear. Not Amear's ruling. A written statement only (bead `Praxis
17:, once they are built**" (the agent's reading, confirmed by Amear in voice only, :512); R8 :1584 "#2 max 2 trades/day, #3 two
17:-and-done" and :1588 "New values come back to Amear as".
---READ---
7:is not a loser and breaks the run is the master's reading under D1, changeable; R4's "a break-even trade counts as" h
9:pted arm (b) set would replace it is the master's reading under D1, changeable), over its full test span, at the cost
9:re-run on the without series to rescue a failure. Reading "±15%" as percentage points and "±25%" as relative to the w
17: breakers on, once they are built**" (the agent's reading, confirmed by Amear in voice only, :512); R8 :1584 "#2 max 
22: R6 changes. SHM: SHM-4 and SHM-5's "backtest" is read as the with series (the master's reading under D1, changeable)
```
(Relative line numbers above: 3 = :2391, 7 = :2395, 9 = :2397, 17 = :2405, 22 = :2410.)

### E5: source text behind paraphrases (checks c, e)
```
$ cd /Volumes/Sensidine/Praxis.build && sed -n '189,191p' DECISIONS.md | cut -c1-300; echo ---R; sed -n '1556,1590p' DECISIONS.md | /usr/bin/grep -nE '^\s*-?\s*\**R[2-8]|PROPOSED|redo|redone|net positive|after costs' | cut -c1-300; echo ---224; sed -n '220,225p' docs/specs/2026-11-05-phase3-build-specification.md | cut -c1-250; echo ---D2; sed -n '1907,1916p' DECISIONS.md | /usr/bin/grep -oE '.{0,80}real money.{0,80}'; echo ---A6; /usr/bin/grep -nE '^\- \*\*A6\.' DECISIONS.md | cut -c1-400
- **Q9 SHM band form:** FIXED pre-declared bands. SHM-4: win-rate >15 ppts below backtest OR slippage >2 ticks/side worse, over a 20-trade window. SHM-5: monthly trade count within [0.5×, 2.0×] of backtest mean; breach = 2 consecutive months. (Coarse + transparent chosen over fitted statistical test

**Unblocks:** b2-data (Praxis_build-hlw) and b2-wfa (Praxis_build-zi1) now have their data source, cost model, gate, and optimize scope. b2-refdist carries the Q6 numeric sub-input gap.
---R
1:R2  GO requires arm (a) to pass. Arm (b) can only add confidence or
3:R3  Gate 6 (WFE) applies to arm (b) only (§4 item 3).
4:R4  Scoring, hybrid (§4 item 3, gate 2):
11:R5  The fixed R:R shape filter (3:1 partial plus runner; 1.5:1) is
14:    rule-based, net positive after costs, and survives every MFFU
17:R6  Research and backtest, on the existing 1-minute data only,
25:R7  Parallel work runs in a separate git worktree on its own branch,
28:R8  F2 unfreezes. Breaker values set for manual trading are redone
34:    PROPOSED.
---224
### Breaker #5 — amended

Amended text, copied by script from the proposal :38:

> 5. Session window (operator lockout) — clock is in 3:00–6:00 PM ET → lock out manual order entry and manual changes to the system by the operator. The system's own trading is not disabled by this breaker; the system's no-entry period 16:00–18:00 ET

---D2
---A6
1774:- **A6.** *Answers:* FLAG 6 (:1645). Master's reading, changeable by Amear (Correction 1, DECISIONS.md:1676): the breaker PROPOSAL unit (U4) is authorised, and F2's state in `specs/SPEC_RUBRIC.md` (:30-43) changes only on his approval of the proposed values. *FLAG 6 RESIDUAL:* D-2026-11-08-A Correction 1 (DECISIONS.md:1669) records that FLAG 6 also asks whether R8's words on #4 and #5 name F2
```
The `---D2` grep is empty because "real money" wraps across lines; E6 shows the text.

### E6: R5, R8 in full; D-2026-11-08-D D1/D2; Amendment 1 authority (checks c, e)
```
$ cd /Volumes/Sensidine/Praxis.build && sed -n '1566,1572p;1583,1590p' DECISIONS.md; echo ---D; sed -n '1905,1918p' DECISIONS.md | cut -c1-500
R5  The fixed R:R shape filter (3:1 partial plus runner; 1.5:1) is
    retired for all automated-strategy research, including the
    higher-win-rate brief. A strategy qualifies if it is fully
    rule-based, net positive after costs, and survives every MFFU
    condition, including the EOD trailing drawdown and the
    consistency rule.
R6  Research and backtest, on the existing 1-minute data only,
R8  F2 unfreezes. Breaker values set for manual trading are redone
    for the automated book: #2 max 2 trades/day, #3 two-and-done,
    #4 flat at 11:30, #5 as a disable of the system's own trading
    15:00–18:00, #8 inter-trade interval under 5 minutes.
    KEEP: #1 daily loss limit; #5 as a lockout on Amear's own
    interaction 15:00–18:00. New values come back to Amear as
    PROPOSED.
R9  FOMC-Cycle Even-Week stays parked while trading on MFFU
---D

STANDING RULE CHANGE — AUTONOMY
D1  Default-decide. When a unit or the master reaches a question that
    would otherwise go to Amear, it takes the recommended option, logs
    it as "decided by master under D-2026-11-08-D D1", and continues.
    Amear may reverse any such decision later; the reversal is filed
    like any ruling. No unit waits on Amear except for D2 items.
D2  Only four things stop and wait for Amear's word: (a) spending
    money; (b) switching live trading on, or any order path to a
    funded account; (c) changing circuit-breaker values while real
    money is at stake; (d) installing keys, credentials or agent
    permissions. Everything else is D1.
D3  The Telegram commit-approval step in the Hermes setup is removed.
    Commits land on an audit PASS. Telegram informs; it does not ask.
```
```
$ cd /Volumes/Sensidine/Praxis.build && sed -n '194p' docs/specs/2026-11-05-phase3-build-specification.md
**Authority.** `DECISIONS.md` entry D-2026-11-12-A (DECISIONS.md:2205), decided by master under D-2026-11-08-D D1, changeable by Amear; DECISION_LOG row 2026-11-12T05:29:00Z (WHO: praxis-master). Rule F2-1 was approved by Amear in the words of a summary (D-2026-11-11-A, V2, DECISIONS.md:2108); the #4/#5 text below is the master's adoption of the F2 proposal's replacement text (`docs/specs/2026-11-10-f2-session-flat-proposal.md`:36, :38), not Amear's words.
```

### E7: evidence for the three prior observations (check g)
```
$ cd /Volumes/Sensidine/Praxis.build && echo "obs1:"; sed -n '2389,2416p' DECISIONS.md | /usr/bin/grep -c '2026-11-01'; /usr/bin/grep -c 'The 2026-11-01 runs are without-series records only' /tmp/o4red3-pre-DECISIONS.md DECISIONS.md; echo "obs2:"; sed -n '2405p' DECISIONS.md | /usr/bin/grep -oF "(the agent's reading, confirmed by Amear in voice only, :512)"; sed -n '512p' DECISIONS.md | /usr/bin/grep -oE "in the agent's reading, confirmed by Amear in voice only[^:]*"; sed -n '2391p' DECISIONS.md | /usr/bin/grep -oE "Decided by master under D-2026-11-08-D D1|Not Amear's ruling"; sed -n '2393p' DECISIONS.md | /usr/bin/grep -cE ':512|R-VN3-5|R-1104-3'; echo "obs3:"; sed -n '250p' ninjascript/PraxisNoiseAreaBreakout_OppBand.cs | /usr/bin/grep -oE '.{0,80}CANNOT-DETERMINE-STATICALLY.{0,40}'; sed -n '2395p' DECISIONS.md | /usr/bin/grep -oE "Decision 1 rule \(CONDITIONAL\)|\(ii\) in the backtest engine, a reversal's close leg fills at the price a stand-alone exit at that bar would|Void if any one is observed false"
obs1:
0
/tmp/o4red3-pre-DECISIONS.md:1
DECISIONS.md:0
obs2:
(the agent's reading, confirmed by Amear in voice only, :512)
in the agent's reading, confirmed by Amear in voice only and entered at the ledger row above
Decided by master under D-2026-11-08-D D1
Not Amear's ruling
0
obs3:
			//     (INFERRED; same-bar exit+reverse resolution is CANNOT-DETERMINE-STATICALLY, 3gm R12/R21 —
Decision 1 rule (CONDITIONAL)
(ii) in the backtest engine, a reversal's close leg fills at the price a stand-alone exit at that bar would
Void if any one is observed false
```

## (a) Quotes byte-present: PASS
E2 gives 28 of 29 records present. The one miss is a probe record I wrote for :1771 with an ASCII "+/-" string. The entry quotes nothing at :1771; it gives a bare "(pointer :1771)". E3 shows :1771 does carry "within ±15% win rate". Every quoted string in the entry is present at its cited line. E3 also confirms the bf6fcc7:116 quote, the R4 :1560-1561 joined quote, the bead text and the DECISION_LOG 05:45:00Z row. Zero hits holds in all three strategy files, and the cited parity-manager report exists. No `## ` heading contains Deviation C, which matches :2401. The new :2405 parenthetical matches :512's own text (E3 line 2 = `1`, E7).

## (b) Both O4 questions answered: PASS
E4: :2393 still says "runs both, and is graded with breakers", which answers the first O4 question. :2397 answers the second: "The gate compares Block 4 paper trades against the with series only" and it is "never re-run on the without series". That line also fixes the arithmetic for both bands. Removing the 2026-11-01 sentence (E1) does not touch either answer.

## (c) No over-attribution; master's readings labelled: PASS
Last round's defect was the unlabelled :2410 SHM reading. It now carries "(the master's reading under D1, changeable)" (E1 2410 hunk, E4 line 22). E4 lists every "reading" or "read as" in the entry. Each one is labelled: the master's at :2395, :2397 (twice) and :2410, and the agent's, voice-confirmed, at :2405. The entry names Amear only in "changeable by Amear. Not Amear's ruling" (:2391) and in :2405. Both match their sources (E6 R8; E2/E3 :512).
Probe, no defect found: :2410 says "#5 (the session window) is an operator lockout with no effect on system trades". R8 (E6) says "#5 as a disable of the system's own trading 15:00–18:00", which conflicts. But the entry's statement matches the amended spec :224 (E5), and that amendment is labelled at its own :194 as the master's D1 adoption, "not Amear's words" (E6). So the entry restates current spec text and attributes nothing to Amear. The R8-vs-Amendment-1 split belongs to D-2026-11-12-A, not to this entry. It is recorded here as an observation only.

## (d) Unobserved mechanisms CONDITIONAL with void clause or named gap: PASS
E4: "Decision 1 rule (CONDITIONAL)" and "Void if any one is observed false" (:2395). Decision 2 reads "CONDITIONAL on assumptions (i) and (iii) above; same void clause". The Status line states the CONDITIONAL convention. "conflicts with topology :59" and "named gap: selecting on one series and grading on the other" appear at :2410, and "No with series exists yet" at :2412. None of these changed in the diff (E1).

## (e) No D2 item decided: PASS
E6 lists the four D2 items. The entry spends no money and opens no live or funded order path. It installs no key, credential or permission. It changes no breaker value: E4 shows "this entry sets none" and "No code, no strategy file, no breaker value and no spec body is changed". The #2/#3 rule fixes only the processing order against "the approved #2 maximum" and "the approved #3 count". It sets neither number. The three edited lines add no D2 matter (E1).

## (f) Diff changes lines 2393, 2405, 2410 only: PASS
E1 gives exactly three hunks, `2393c2393`, `2405c2405` and `2410c2410`, and both files are 2416 lines. Hunk 2393 removes one sentence. Hunk 2405 adds one parenthetical. Hunk 2410 adds one parenthetical.

## (g) Prior observations graded against the edited entry: PASS
- **Obs 1 (2026-11-01 runs called without-series records): resolved.** E7: the sentence occurs once in the pre-edit file and zero times in DECISIONS.md, and "2026-11-01" now appears zero times in :2389-2416. The entry no longer makes the claim.
- **Obs 2 (Decision 1 cites no ruling; :512 qualifier missing): resolved.** E7: :2405 now carries "(the agent's reading, confirmed by Amear in voice only, :512)", and :512 itself says "in the agent's reading, confirmed by Amear in voice only". :2393 cites no ruling (count `0`). But :2391 labels the whole entry "Decided by master under D-2026-11-08-D D1" and "Not Amear's ruling", so Decision 1 does not need to cite one. Residual, not graded as a defect: :512's ruling is "once they are built", while Decision 1's with series is a post-run simulation of breakers that do not exist yet. :2412 states this openly ("a with series is a simulation of specified text, not evidence that a breaker works"), so the gap is declared, not hidden.
- **Obs 3 (OppBand :250 CANNOT-DETERMINE-STATICALLY supports keeping (ii) CONDITIONAL): not a defect.** E7: OppBand :250 contains "CANNOT-DETERMINE-STATICALLY" for same-bar exit+reverse. :2395 still has "Decision 1 rule (CONDITIONAL)", assumption (ii) word for word, and the void clause. The entry is consistent with the code comment.

## Files staged
None. Read-only round; this report is the only file written. No git add, no commit, no bd writes. DECISIONS.md was not modified.

## Result: PASS

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
