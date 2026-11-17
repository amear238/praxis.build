# O4 parity adversarial worker 3 (bead Praxis_build-yra)

## Task
Grade DECISIONS.md D-2026-11-13-A (lines 2389-2416, working tree, main @ cae83dc) cold against rubric O4, standing S2 and S6, and D2. Read-only except this file. No other o4-parity report was read.

## Mode
ADVERSARIAL.

## Criterion
specs/SPEC_RUBRIC.md O4 (verbatim in the brief): a written statement of whether the Block 2 backtest runs with breakers applied, without them, or both, and how the Block 4 gate is satisfiable if they differ. S2: no component reported above its evidence. S6: cross-block conflicts named. D2: the entry must decide none of the four Amear-only items.

## Process log
1. Located the entry and confirmed its span and the staged-index count.
2. Check 1: byte-presence of every quoted string carrying a :line cite (33 rows by script, plus R6 design, bead, and the code grep the entry describes).
3. Check 2: read Decisions 1 and 2 against both O4 questions.
4. Check 3 and 4: read spec :94-102, :120-126, :196, :200-242; topology :55-62; DECISIONS.md :186-190, :345-352, :508-513, :755-765, :940-950, :1556-1590, :1730-1750, :826-833, :1486-1490; searched for Flat1559, early-close and arm-adoption records.
5. Check 5 and 6: format, banned strings (patterns built from parts), deletions, hash.

## Verification evidence

### E0. Entry location and index
```
$ grep -n -F "## 2026-11-13 — D-2026-11-13-A" DECISIONS.md
2389:## 2026-11-13 — D-2026-11-13-A: Backtest-vs-live breaker parity (rubric O4; master under D-2026-11-08-D D1)
$ wc -l DECISIONS.md
    2416 DECISIONS.md
$ git diff --cached --name-only | wc -l
       1
```

### E1. Check 1, quotes (script loop over a quote table; each line shown is the literal command it ran)
```
$ sed -n '98p' docs/specs/2026-11-05-phase3-build-specification.md | grep -c -F -- 'trade count hits daily max → disable order submission'
1
$ sed -n '99p' docs/specs/2026-11-05-phase3-build-specification.md | grep -c -F -- '2 consecutive losers in one session → identical to max trades'
1
$ sed -n '124p' docs/specs/2026-11-05-phase3-build-specification.md | grep -c -F -- 'within ±15% win rate and ±25% average trade P&L'
1
$ sed -n '205p' docs/specs/2026-11-05-phase3-build-specification.md | grep -c -F -- 'The system opens no new position from that flat time until 18:00 ET, when the next session begins.'
1
$ sed -n '224p' docs/specs/2026-11-05-phase3-build-specification.md | grep -c -F -- 'The system'\''s own trading is not disabled by this breaker'
1
$ sed -n '239p' docs/specs/2026-11-05-phase3-build-specification.md | grep -c -F -- 'New system entries between 15:00 and 16:00 are allowed under Rule F2-1, subject to breakers #1, #2, #3, #6, #7, #8 and #9.'
1
$ sed -n '196p' docs/specs/2026-11-05-phase3-build-specification.md | grep -c -F -- 'SPECIFIED ONLY — zero implemented, zero tested, zero tested under failure'
1
$ sed -n '212p' docs/specs/2026-11-05-phase3-build-specification.md | grep -c -F -- 'or the exchange'\''s early close on an early-close day if earlier'
1
$ sed -n '1560p' DECISIONS.md | grep -c -F -- 'a break-even trade counts as'
1
$ sed -n '1561p' DECISIONS.md | grep -c -F -- 'a break-even trade counts as'
0
$ sed -n '42p' DECISION_LOG.md | grep -c -F -- 'positions/session = reverse & re-enter on opposite-band cross (NOT one-position/session)'
1
$ sed -n '32p' ninjascript/PraxisNoiseAreaBreakout.cs | grep -c -F -- 'Positions/session = REVERSE & re-enter on an opposite-band cross'
1
$ sed -n '189p' ninjascript/PraxisNoiseAreaBreakout.cs | grep -c -F -- 'if (mod >= CloseMod)'
1
$ sed -n '191p' ninjascript/PraxisNoiseAreaBreakout.cs | grep -c -F -- 'FlattenAll("16:00 session flat");'
1
$ sed -n '108p' ninjascript/PraxisNoiseAreaBreakout.cs | grep -c -F -- 'IsExitOnSessionCloseStrategy              = true;'
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
$ sed -n '512p' DECISIONS.md | grep -c -F -- 'once they are built'
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
$ sed -n '944p' DECISIONS.md | grep -c -F -- '12:15 early-close exits'
1
$ sed -n '55p' docs/reports/2026-11-09-d6-drawdown-check-manager.md | grep -c -F -- 'every later trade that session is skipped'
1
```
The :1561 zero is not a defect: the entry cites the range :1560-1561 for a quote that sits on :1560 (and :1771 confirms the phrase is joined across the two lines, below).

```
$ git show bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md | sed -n 116p
| O4 | Backtest-vs-live parity (OPEN) | First pass runs without breakers (no approved values; D6 E4) and says so; a breakers-on run waits for F2. | First pass [D1]; parity OPEN with O4 |
$ git show bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md | sed -n 116p | grep -c -F -- "First pass runs without breakers (no approved values; D6 E4) and says so; a breakers-on run waits for F2."
1
$ bd show Praxis_build-yra | grep -c -F "the live-vs-backtest gate is structurally unmeetable."
1
$ ls ninjascript/PraxisNoiseAreaBreakout*.cs
ninjascript/PraxisNoiseAreaBreakout.cs
ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs
$ grep -c -E "MaxTrades|TradeCount|tradesToday|consecutive|loser|LossStreak" ninjascript/PraxisNoiseAreaBreakout*.cs
ninjascript/PraxisNoiseAreaBreakout.cs:0
ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:0
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:0
$ grep -n -i -E "MaxTrades|TradeCount|tradesToday|consecutive|loser|LossStreak" ninjascript/PraxisNoiseAreaBreakout*.cs
exit=1
$ sed -n 1771p DECISIONS.md
- **A3.** *Answers:* FLAG 3 (:1642). *Bears on:* O4 (`specs/SPEC_RUBRIC.md:94-99`; the Block 4 "within ±15% win rate", :96-97, joined) and R4's win-rate line (DECISIONS.md:1560–1561, "a break-even trade counts as half a loss", joined). O4's "**Required:**" statement (whether the Block 2 backtest runs with breakers applied, without them, or both; :97-99) is not addressed by A3, and O4 is not discharged here (INFERRED, the filer's, not his word). *Left for a later unit:* any O4 write-up; NEEDS AMEAR (i) below.
$ sed -n 511p DECISIONS.md | grep -c -F "Deviation C"
1
$ sed -n 2072p DECISIONS.md | grep -c -F "Deviation C"
1
$ grep -n -E "^## .*Deviation C" DECISIONS.md
exit=1
$ awk 'NR>=308 && NR<=352 && /^## /{print NR": "$0}' DECISIONS.md | cut -c1-120
308: ## 2026-10-31 — D-2026-10-31-A: 7zq scope extension — two Noise-Area backtest variants (OppBand, Flat1559) + one ne
$ sed -n 348p DECISIONS.md
**NEEDS AMEAR (questions only):**
$ sed -n 351p DECISIONS.md
3. **Early-close handling:** once the template's early-close rows (3gm R4) and the early-close trades (R6) are read, should a session-aware flat be built, and where?
$ sed -n 11p docs/specs/2026-11-05-phase3-build-specification.md | grep -c -F "SPECIFIED ONLY"
1
```
Check 1 result: every cited quote is byte-present at its cited line; the described code grep reproduces (zero hits, also case-insensitive); "no entry titled Deviation C" reproduces; :351 is item 3 of D-2026-10-31-A's NEEDS AMEAR list.

### E2. Check 2, the two O4 questions
Read from the entry (lines 2393 and 2397, located in E0's print): Decision 1 says "runs both, and is graded with breakers"; the with series is the raw list after #2 and #3 are applied post-run; the without series is never graded. Decision 2 names the series (with series only, of the arm that trades in Block 4), the arithmetic (win rate within 15 percentage points; |paper mean minus with mean| at most 0.25 times the with mean), and removed trades (enter neither term; listed in a removed-trades table; paper entries the gates block are logged, not counted). Both questions are answered unambiguously. The two readings of "±15%" and "±25%" are labelled as the master's under D1:
```
$ sed -n 2389,2416p DECISIONS.md | grep -o -E "master.s (reading|interpretation)|the master.s, under D1|master.s reading under D1"
master's reading under D1
the master's, under D1
$ sed -n 2389,2416p DECISIONS.md | grep -c -F "CONDITIONAL"
4
```

### E3. Check 3 and 4, the early-close assumption against the record
The entry (S6 paragraph) cites :944's "12:15 early-close exits" as the platform backstop seen in the baselines, then assumes "that exit falls at amended #4's early-close time", void "if the backtest's early-close exit time is observed to differ from the exchange's early close". The record:
```
$ sed -n 944p DECISIONS.md
  - reading (voice agent, notes-4): 33 missing sessions and the 12:15 early-close exits are accepted as is. No fix before results are judged. Basis: baseline shape matches the published NQ replication (lower win rate, bigger winners), weaker.
$ sed -n 1490p DECISIONS.md
- **Oracle inputs carried into the spec** (the same row, quoted): "Also carried into the spec as oracle inputs (no code change): weekend-dated bars in the data file (141 dates; RTH template drop INFERRED), early-close cut where NT8 cuts (12:00/12:15/14:03 vs the file's 13:15/13:00), enum numeric order {BandOrVWAP 0, OppBand 1, Flat1559 2} vs the base's — bridge must send by name."
$ sed -n 2389,2416p DECISIONS.md | grep -c -F -- "1490"
0
$ sed -n 359p DECISIONS.md
- **R-7zq-2 — Flat1559 fill (answers NEEDS AMEAR 7 above), DECISION_LOG `2026-10-31T11:04:20Z` (WHO: amear):** *"Yes — test it as built."* The 15:59-bar submission / 16:00-bar-open fill (~15:59 price, flat by 16:00) is accepted as the backtest realisation; the Trades-tab readback decides whether the base's own flat was landing next-day.
```

### E4. Check 3, the R2 attribution in Decision 2
```
$ sed -n 1556,1562p DECISIONS.md | cut -c1-420
R2  GO requires arm (a) to pass. Arm (b) can only add confidence or
    block a GO; it can never carry a GO on its own (§4 item 3).
R3  Gate 6 (WFE) applies to arm (b) only (§4 item 3).
R4  Scoring, hybrid (§4 item 3, gate 2):
    - Win rate: no-trade days excluded; a break-even trade counts as
      half a loss.
    - Sharpe: daily returns, every trading day counted (no-trade
$ sed -n 1556,1557p DECISIONS.md | grep -c -E "unless|adopted"
0
$ sed -n 2397p DECISIONS.md | grep -c -F -- "(R2: arm (a) unless an arm (b) set is adopted)"
1
$ sed -n 826,833p DECISIONS.md | cut -c1-200
- **F1** (`specs/SPEC_RUBRIC.md:17`), **F2** (`:30`), **F3** (`:45`), **F4** (`:59`): untouched. No code, template or config changed. Nothing here claims any F advanced.

**NEEDS AMEAR (questions only, not answered):**
1. Which MFFU account size and which tier limits are to be used for items 3 and 4, given that item 5 defers the account-tier decision until backtest and paper results exist?
2. Does arm (b) run on minute data, given its stop (report C NEEDS AMEAR 11)?
3. What is the candidate set for the exit-policy parameter in item 1(b)?
4. Is R-1104-3's judged version arm (a), arm (b) or both?

```

### E5. Check 4, other S6 sources read (R8, A3 to A8, amended #5)
```
$ sed -n 1580,1590p DECISIONS.md | cut -c1-420
R7  Parallel work runs in a separate git worktree on its own branch,
    never in the same working directory (v6y). NT8 runs on the VM
    take turns.
R8  F2 unfreezes. Breaker values set for manual trading are redone
    for the automated book: #2 max 2 trades/day, #3 two-and-done,
    #4 flat at 11:30, #5 as a disable of the system's own trading
    15:00–18:00, #8 inter-trade interval under 5 minutes.
    KEEP: #1 daily loss limit; #5 as a lockout on Amear's own
    interaction 15:00–18:00. New values come back to Amear as
    PROPOSED.
R9  FOMC-Cycle Even-Week stays parked while trading on MFFU
$ sed -n 1730,1750p DECISIONS.md | cut -c1-420
A3  FLAG 3: Win rate is not a Block 2 pass gate. Per trade:
    W / (W + L + 0.5 x B), B = trade exited at its entry price.
    No-trade sessions excluded. It is the quantity for O4's Block 4
    "within +/-15% win rate" check, computed identically on backtest
    and paper.
A4  FLAG 4: Max-DD gate = backtest max drawdown must stay below 80%
    of the ruled limit, i.e. below the lower of 3.2% of the MFFU
    account size and 80% of MFFU's trailing drawdown limit. This
    amends D-2026-11-05-A item 3 with a safety buffer for model error.
    Evaluated against every tier row; tier pick stays Q9. Closes the
    notes-4 DD equity-base item.
A5  FLAG 5: For arms (a)/(b), "trading day" = session i of §6
    (09:30-16:00 ET per R1). For R6 evening-entry research, "trading
    day" = MFFU's own definition from its current terms.
A6  FLAG 6: R8 starts the breaker PROPOSAL unit. F2's state changes
    when Amear approves the proposed values.
A7  R3 amends Q8: arm (a) is judged on gates 1-5 (WFE not
    applicable). Arm (b) on gates 1-6 plus PBO < 0.05.
A8  O1 is discharged by R2 + R3 + A7. Gate 6 formula (Pardo WFE):
    annualised OOS net profit / annualised IS net profit of the
    selected parameter set, pooled across all windows; pass >= 0.50.
$ sed -n 224p docs/specs/2026-11-05-phase3-build-specification.md | grep -c -F "operator lockout"
1
```
#2 and #3 are treated consistently with spec :98-99 and topology :59-60 (entry counter and closed-loser run, both session-terminal, neither value approved). R-VN3-5 ("once they are built"), D-2026-11-04-A (ii) re-ask, SHM-4/SHM-5, R6's without-first-pass and the topology :59 whole-signal drop are all named in the entry.

### E6. Check 5 and 6, D2, F3/F4, format, banned strings, deletions, hash
```
$ sed -n 2389,2416p DECISIONS.md | grep -o -F -e "No code, no strategy file, no breaker value and no spec body is changed." -e "this entry sets none" -e "It does not lift F3 or F4 and depends on neither" -e "does not mark O4 passed"
No code, no strategy file, no breaker value and no spec body is changed.
this entry sets none
It does not lift F3 or F4 and depends on neither
does not mark O4 passed
$ sed -n 2389,2416p DECISIONS.md | wc -l
      28
$ sed -n 2389,2416p DECISIONS.md | grep -c -F -- "**Status:**"
1
$ sed -n 2389,2416p DECISIONS.md | grep -c -F -- "**Decision 1:"
1
$ sed -n 2389,2416p DECISIONS.md | grep -c -F -- "**Decision 2:"
1
$ sed -n 2389,2416p DECISIONS.md | grep -c -F -- "**Sources"
1
$ sed -n 2389,2416p DECISIONS.md | grep -c -F -- "**S6 cross-block.**"
1
$ sed -n 2389,2416p DECISIONS.md | grep -c -F -- "**Limits.**"
1
$ sed -n 2389,2416p DECISIONS.md | grep -c -F -- "**S4 timing.**"
1
$ tail -n 1 DECISIONS.md
Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
$ tail -n 1 DECISIONS.md | od -c | tail -n 3
0000100    c   k   s   /   s   i   d   e       s   l   i   p   p   a   g
0000120    e       a   s   s   u   m   e   d   .  \n                    
0000133
$ sed -n 2389,2416p DECISIONS.md | grep -c -x -F -- "Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed."
1
$ sed -n 2389,2416p DECISIONS.md | grep -o -F -- "Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed." | wc -l
       1
$ V=$(printf "%s%s" "verd" "ict"); sed -n 2389,2416p DECISIONS.md | grep -c -i -F -- "$V"
0
$ C1=$(printf "%s%s" "COMMIT-" "INDEX"); sed -n 2389,2416p DECISIONS.md | grep -c -F -- "$C1"
0
$ C2=$(printf "%s%s" "COMMIT-DIFF-" "SHA256"); sed -n 2389,2416p DECISIONS.md | grep -c -F -- "$C2"
0
$ D=$(printf "%s%s" ".." "."); printf "%s" "$D" | od -c | head -n 1; sed -n 2389,2416p DECISIONS.md | grep -c -F -- "$D"
0000000    .   .   .                                                    
0
$ U=$(printf "\xe2\x80\xa6"); sed -n 2389,2416p DECISIONS.md | grep -c -F -- "$U"
0
$ git diff HEAD -- DECISIONS.md | grep -c "^-[^-]"
0
$ sed -n 2389,2416p DECISIONS.md | shasum -a 256
214a85ec9703c36f80793922752a2eb314382fef1224015ad40ece0da1f2e125  -
```
Check 5 and 6 pass: no D2 item decided, no breaker value set, no code or spec body changed, F3 and F4 neither lifted nor relied on; 28 lines; all sections present; the closing line is the file's last line, exact, once in the entry; no banned strings; zero deleted lines.

## Defects

1. S6 and S2, early-close assumption against an existing record. The entry's early-close CONDITIONAL cites :944's "12:15 early-close exits" as the platform backstop's footprint and treats "the backtest's early-close exit time is observed to differ from the exchange's early close" as a future void observation. The repo already records, at DECISIONS.md:1490, "early-close cut where NT8 cuts (12:00/12:15/14:03 vs the file's 13:15/13:00)", and :944 itself files the 12:15 exits next to "33 missing sessions" as a data gap "accepted as is", not as exits at the session's close. The entry does not name :1490 (E3, count 0) and does not say why that record does not already trigger its void clause. That is an unnamed cross-block conflict (Block 2 data record against the Block 3/4 parity assumption), and the assumption is presented as unobserved when a record bearing on it exists. Whether the exchange's actual early-close time matches the file's or NT8's values is UNVERIFIED by me; the defect is that the record is not named, not that the void has definitely fired.
2. S2, an interpretation not labelled. Decision 2 picks which arm's with series the Block 4 gate uses and attributes the rule to R2: "(R2: arm (a) unless an arm (b) set is adopted)". R2 (DECISIONS.md:1556-1557) says only that GO requires arm (a) and that arm (b) can never carry a GO on its own; it has no "unless" clause and says nothing about an arm (b) set being adopted to trade (E4, count 0). The "unless an arm (b) set is adopted" branch is the master's reading and is not labelled as one, unlike the entry's other two readings. It also bears on the open question D-2026-11-04-A NEEDS AMEAR 4 ("Is R-1104-3's judged version arm (a), arm (b) or both?", :832, under "questions only, not answered"), which the entry cites R-1104-3 beside but does not name. Whether R2 later answered that question in part is not stated in the entry.

## Non-defects (style notes)
- The Decision 2 header says CONDITIONAL on (i) and (iii), but the with series it grades against also rests on (ii). The shared void clause ("Void if any one is observed false") covers it.
- The :1560-1561 cite holds a quote that sits wholly on :1560; acceptable as a range.
- "Implemented: reverse and 16:00 flat" is a code-level claim and holds (E1). Whether the base's own 16:00 flat fills the same day is open in the record (:359, "the Trades-tab readback decides whether the base's own flat was landing next-day"), but both series share the raw list, so it does not split them and the entry does not claim otherwise.
- The #5 statement ("an operator lockout with no effect on system trades") follows amended spec :224 (E5); topology's #5 row predates that amendment. Not a conflict the entry creates.

## Files staged
None by this worker. This report is written, not staged. Index count unchanged at 1 (E0).

## Result
FAIL (2 defects)

Grade: FAIL (2 defects)
Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
