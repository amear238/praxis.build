# o78 worker 4: adversarial review of the manager's synthesis report

**Task:** Attack `docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md` (the synthesis). Focus on claims the manager added beyond W1–W3.
**Mode:** ADVERSARIAL. Read-only. This file is the only one I wrote. Nothing staged, nothing committed. Nothing written under `.claude/agent-memory/`. No strategy replication or backtest was run.
**Criteria (verbatim, `specs/SPEC_RUBRIC.md`):** S1 "Every claim in a report has pasted command output, not a description of output." · S2 "No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure." · S6 "Cross-block check: every approved deviation is tested against the specs of every other block it touches, not only its own." · S8 "No question that belongs to Amear is answered on his behalf." · S9 "Any config field a guarantee depends on is positive-controlled … A field that parses is not a field that is honoured."

## Process log

1. Read the synthesis in full, plus `mgr_verify.py` and `mgr_verify2.py`, run-3 record `:36-40` (the column header that E3 omits), and the gate's `Result` regex.
2. Wrote `$S/w4r_rerun.py`. It pulls every fenced `$ ` block out of the synthesis, re-runs the command (cwd = repo, `S` = scratchpad) and diffs the output against the pasted text (W4-E1).
3. Wrote `$S/w4r_data.py` to test the import file: the 2025-04-09 context rows, whether the 1,792.50 match is unique on both sides, the alternative slippage split, the residues, the cost ratios and the Saturday rows (W4-E2).
4. Wrote `$S/w4r_bin.py`. It scans all 122 binary-type files in the rescued tree (.dll/.exe/.msi/…) for `slippage`/`TotalSlippage`/`Total slippage` in ASCII and UTF-16LE (W4-E3). This tests bottom line 3 beyond `grep -I`, which skips binaries.
5. Grepped the code for the flatten/checkpoint/session logic, and ran stat on the E10 files (W4-E4).
6. Traced the W3/W1/F3/3gm/voice-note citations (W4-E5).
7. Read the rescued trading-hours templates for the two template names that appear in the DB and in run 4's settings (W4-E6).

`$S` = `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad`.

## Findings

| id | report location | severity | pasted evidence | exact replacement text |
|---|---|---|---|---|
| W4-1 | Bottom line 1, third bullet: "The short-side loss therefore has to come from the market, the data, or the engine, not from the rule code." | **MAJOR** (S2; contradicts the report's own A1 row 2, H3 and H4) | A1 row 2 (same report): "In price space the upper band sits \|gap\|·σ further from its own reference … the long trigger closer on 53–57% of days". W3 `:109,:111`: `share days long-trigger closer to open 0.53` / `0.567`. H3 and H4 are mechanisms that work *through* the rules: stops at :00/:30 and the VWAP trail. The code has no mirror asymmetry, but a symmetric rule can still pass on or amplify an asymmetric input. | "No mirror asymmetry exists in the rule code. A side-asymmetric result must therefore originate in an asymmetric input (market drift, gap mix, data) or in engine handling. It may act *through* symmetric rules (the gap-dependent band distance in A1 row 2, the stop/trail mechanics in H3/H4). Which one is not established." |
| W4-2 | H9 candidate list, and NEEDS AMEAR 1 (no mention of the on-disk trading-hours template) | **MAJOR** (S9/S6: an on-disk config fact the code's 09:30 anchor depends on, left out) | W4-E6: rescued `templates/TradingHours/CME US Index Futures RTH.xml` = `TimeZone ['Eastern Standard Time']`, sessions `('Monday', '830', 'Monday', '1600')` … Friday, mtime `Aug 29 11:52:00 2026` (later than the stock ETH file's `Jul 9`). Run 4 used "Trading hours = CME US Index Futures RTH" (voice notes `:52`, REPORTED). The code anchors `todayOpen = Open[0]` and resets VWAP on `Bars.IsFirstBarOfSession` (`:147,:152,:158-159`; the comment says "09:30 open"). With an 08:30 ET session start, the first bar of the session is 08:31, not 09:31 (INFERRED). | Add to H9's candidates: "The rescued (Parallels) `CME US Index Futures RTH` template is Mon–Fri **08:30–16:00 Eastern** (OBSERVED on disk, W4-E6). If Fusion's copy is the same, `IsFirstBarOfSession` lands on 08:31: `todayOpen` and the VWAP anchor would be the 08:31 bar, not 09:30 as the spec requires (INFERRED; Fusion's copy UNVERIFIED)." Add to NEEDS AMEAR 1: "Also read `Tools > Trading Hours > CME US Index Futures RTH`: time zone and each session's begin and end time." |
| W4-3 | H9 "6 bars dated Saturday 2024-01-20"; NEEDS AMEAR 6 "it holds 6 bars dated Saturday 2024-01-20" | **MAJOR** (S2 underclaim: the scope is understated about 20×) | W4-E3: `Saturday dates: 66 rows: 127 rows in 09:31-16:00: 58`, `2024-01-20 rows: 6 in RTH window: 6`, `dates in run window 20210308-20260717 with RTH-window Saturday rows: 44`. | "The import file holds **127 rows dated Saturday across 66 dates** (58 rows inside 09:31–16:00, on 44 dates within the run window). 6 of them are on 2024-01-20, one printing 3,100 (W3 F9; W4-E3). The rescued RTH templates list Mon–Fri sessions only (W4-E6), so they would probably be excluded (INFERRED; Fusion's copy UNVERIFIED)." |
| W4-4 | H9: "598–599 vs 627 trades" | MINOR (wrong number) | E8 (same report): shorts `599`, `597`, `598`. W4-E2: `min 597 max 599`. | "597–599 vs 627 trades" |
| W4-5 | E8 block rendering | MINOR (S1 fidelity of the rendered form) | W4-E1: line 354 is `pasted 6 lines, fresh 24 lines`. The sed output contains its own ```` ``` ```` lines, so the report's fence closes after 6 lines. The replication output renders as body text and the manager-style parenthetical renders as code. The bytes are all present (lines 355–378 match the fresh output). | Wrap E8 in a four-backtick fence (```` ```` ````) so the nested fences in the sed output stay inside the block. |
| W4-6 | E4 header "Observer effect: …" (E7 not flagged) | MINOR (S1) | W4-E1: line 336 `DIFFERS … pasted 13 lines, fresh 19 lines`. E7 matches itself: its own pasted lines contain the search phrase, so no re-run can reproduce it. | Add before the E7 block: "Observer effect: this grep matches its own pasted lines in this report, so a re-run returns more self-hits. The non-self hits (W2 `:36,:296`, 3gm-worker2 `:60`, voice notes `:42`, DECISION_LOG `:444`) are the evidence." |
| W4-7 | E10 prose: "STATUS/DECISION_LOG/HANDOFF (mtime 08:42:03) … skeleton created (local 08:42:52)" | MINOR (S1: the times are stated with no pasted output; I checked and they are true) | W4-E4: `STATUS.md mtime=08:42:03 birth=08:42:03` … `…o78-short-side-and-slippage-unit.md mtime=09:11:53 birth=08:42:52`. | Paste `stat -f '%N mtime=%Sm birth=%SB' -t '%H:%M:%S' STATUS.md DECISION_LOG.md HANDOFF.md docs/reports/2026-10-31-o78-*.md` and its output under E10. |
| W4-8 | B2 row 1: "The locked F3 assumption ("2 ticks/side, $10/side") was therefore **not** what was simulated." | MINOR (S2: stated without a condition; the quotation is a paraphrase) | W4-E5: the exact string does not appear in the F3 artifact or in DECISION_LOG. F3 artifact `:226` reads "slippage 1 → 2 ticks/side ($5 → $10/side; …)". DECISION_LOG `:442` locks "**band-edge** slippage = 2 ticks per side". | "If the best reading holds (INFERRED), what was simulated is 0.02 pt/side, not the locked F3 assumption (2 ticks/side = $10/side at $20/pt; F3 artifact `:226`, DECISION_LOG `:442`)." |
| W4-9 | H5: "**Not a cause.** Run 3: commission $2.96/trade and slippage 0.04/trade on both sides (E5)." | MINOR (S2: run-3 INVALID-template evidence used for run 4 without saying so) | E3/E5 (same report): run-4 totals `commission $3,584.56 (= 1,211 × 2.96 ✓)`, `total slippage 48.44` = 1,211 × 0.04. The by-side figures exist for run 3 only. | "**Not supported as a cause.** Run 3 by side (INVALID template): $2.96 and 0.04 per trade on both sides (E5). Run 4 totals (REPORTED): $3,584.56 = 1,211 × 2.96 and 48.44 = 1,211 × 0.04, so the per-trade cost is flat on aggregate. Run-4 by-side costs are not on record." |
| W4-10 | H4 falsifier: "exit reason by side (`XS`/`XL` trail vs `FlatEOD` vs reversal)"; NEEDS AMEAR 2 "exit ≈ 20,486.73 at 16:00" | MINOR (S2: leaves out a likely exit category) | W4-E4: `:108 IsExitOnSessionCloseStrategy = true; // backstop`; `:189 if (mod >= CloseMod)` with `CloseMod = 960`. The rescued RTH template ends at 1600 (W4-E6). `FlatEOD` is submitted on the 16:00 bar's close, and under Standard fill it would fill at the next bar. The 1,792.50 match needs a fill at the **16:00 bar's Close** (W4-E2: the 16:01 Open is `20487.75`, not `20486.75`). That fits NT8's exit-on-session-close fill, not `FlatEOD` (INFERRED). | H4: "(`XS`/`XL` trail vs `FlatEOD` vs NT8 'Exit on session close' vs reversal)". NEEDS AMEAR 2: add "Also read the exit name (`FlatEOD` or 'Exit on session close'), and whether the exit price carries the −0.02." |
| W4-11 | Report contract: "Stress-test Result: PASS (all six checks run; W3 findings folded in; W4 below)" | MINOR (S1/S2: PASS issued while W4 was pending; the six checks are not listed) | Same report `:421`: "W4 (adversarial on this report): pending at build time." No list of the six checks appears anywhere in the report. The gate regex (`scripts/gate-manager-output.sh:23`, `Result:\s*(PASS|FAIL|BLOCKED)`) is satisfied by this line. | After folding W4 in: "Stress-test Result: PASS (checks: <list the six>; W3 VERDICT BROKEN on the pre-correction synthesis, F1/F2 accepted; W4 VERDICT SURVIVED-WITH-CORRECTIONS, W4-1…W4-12 dispositioned)". |
| W4-12 | B1 rank 1 "✓ Stock NQCONT 1.0 / 0.01"; bottom line 2 "Stock-typed" | MINOR (S2: the type mapping was already relabelled for W2, but not in the synthesis table) | E5: the DB column `InstrumentType` = `1`. The mapping 1 → Stock is INFERRED (W3 F7, accepted). | "✓ NQCONT with InstrumentType 1 (INFERRED Stock), point value 1.0, tick 0.01, `US Equities RTH`, in all three old-DB copies (E5)" |

No CRITICAL finding. No S8 breach: every decision is routed to Amear ("Which of them to pursue is Amear's decision"; "What to do about them is Amear's decision"; "Whether to clean the file is his call"). Nothing in NEEDS AMEAR decides or recommends.

## Claims that survived (with re-run output)

- **E-block fidelity.** 12 of 15 `$ ` blocks re-run IDENTICAL byte-for-byte: E1, E2, E3 ×2, E4 ×2, E5, E6 ×2, E9, E10-find, Files staged. Three differ: E7 is self-matching (W4-6), E8 is a fence-nesting artifact with identical content (W4-5), and E10-diff shows the expected observer effect (my own spawn row `corr=ae73270cb6e608184`).
- **H6 arithmetic.** It holds: commission 20×, slippage 25×, ratio 2.613, −4,867.12 and +112,459.36 (E6 re-ran identical). Signs unchanged. W3's F1/F2 corrections are correctly folded in.
- **H7.** 4541.40 − 1792.50 = 2,748.90.
- **Readback-2 prices.** A long exit slipped down 0.02 is correct for a sell. (20,486.75 − 0.02) − (18,691.25 + 0.02) − 2.96 = **1,792.50**. Caveat: an entry-only 0.04 also gives 1,792.50, so the 1,792.50 alone does not fix the 0.02/0.02 split. The expected .27/.73 follows from "2 ticks every fill", which the report itself labels UNVERIFIED, so it is coherent.
- **12:30 stamp → 12:31 Open.** The code uses `Calculate.OnBarClose` (`:105`), the checkpoint is `Time[0].Minute == 30` (`:196`), and the signal is read on the bar stamped 12:30 (it closes at 12:30). The managed market order fills at the next bar's (12:31) Open = 18,691.25. Consistent.
- **Uniqueness of the 1,792.50 match.** In the whole import file only one bar-Open → same-day-16:00-Close pair gives +1,795.50 (`[('20250409', '123100')]`), and no short pair gives −1,795.50. Only two days have an RTH range ≥ 1,795.5 (2025-04-09, plus 2024-01-20, which is the bad print). The match is stronger than the report claims.
- **Bottom line 3** ("No NT8 text on disk defines the unit"). It also survives a binary scan: 122 binary-type files, including 103 DLLs, searched in ASCII and UTF-16LE, `total hits: 0` (W4-E3). Scope caveat: the rescued tree is the user-documents tree, not Program Files.
- **Residues.** Run 4 0.09 and run 3 0.11 confirmed. B3 and the bottom line's "residues are not zero" do not contradict each other.
- **S6.** True: only the four o78 reports and DISPATCH_LOG are newer than the window (re-run identical), and STATUS/DECISION_LOG/HANDOFF were born at 08:42:03, before the 08:42:30 window.
- **Citations traced.** "8 of 8" = W3 `:187` "8/8 pasted blocks are byte-identical". The brute-force grid = W3 `:125`. A1 row-2 numbers = W3 `:95,:97,:98,:109,:111`. W3 `VERDICT: BROKEN` at `:215`. The "Claude's estimate" origin = voice notes `:42`. 3gm D3 "market fill (INFERRED type)" = `3gm-fidelity-check.md:949`.

## Not tested

- Whether the import file is back-adjusted (which would make H2's yearly % something other than NQ returns). I have a suspicion from price levels; it is UNVERIFIED and not checked on disk, so it is not raised as a finding.
- NT8's Trades-tab execution-time convention for next-bar-Open fills (12:30 vs 12:31): UNVERIFIED. NEEDS AMEAR 2's "around 12:31" is hedged enough.

## Verification evidence

**W4-E1. Re-run and diff of every pasted block** (`python3 -I "$S/w4r_rerun.py"`)
```
#### line 167 | IDENTICAL | shasum -a 256 ninjascript/PraxisNoiseAreaBreakout.cs; wc -l ninjascrip | pasted 2 lines, fresh 2 lines
#### line 174 | IDENTICAL | /usr/bin/grep -n "price > curUpper\|price < curLower\|Math.Max(curUppe | pasted 21 lines, fresh 21 lines
#### line 200 | IDENTICAL | sed -n '53p' docs/reports/2026-10-28-voice-session-notes.md | pasted 1 lines, fresh 1 lines
#### line 204 | IDENTICAL | sed -n '40,77p' docs/reports/2026-10-30-run3-backtest-screenshot-recor | pasted 38 lines, fresh 38 lines
#### line 247 | IDENTICAL | /usr/bin/grep -rIl --ignore-case "total slippage\|totalslippage" --exc | pasted 18 lines, fresh 18 lines
#### line 268 | IDENTICAL | /usr/bin/grep -rIl --ignore-case "slippage" --include="*.cs" --include | pasted 4 lines, fresh 4 lines
#### line 277 | IDENTICAL | python3 -I "$S/mgr_verify.py" | pasted 27 lines, fresh 27 lines
#### line 309 | IDENTICAL | python3 -I "$S/mgr_verify2.py" | pasted 18 lines, fresh 18 lines
#### line 330 | IDENTICAL | python3 -I -c "print('longs without the 1792.50 outlier:', round(4541. | pasted 1 lines, fresh 1 lines
#### line 336 | DIFFERS | /usr/bin/grep -rIn --ignore-case --exclude-dir=.git "market and stop f | pasted 13 lines, fresh 19 lines
    --- pasted
    +++ fresh
    @@ -5,2 +5,8 @@
    -./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:338:./docs/reports/2026-10-31-o78-worker2-slippage-unit.md:36:7. **"Applies to market and stop fills, not limit fills" has no NT8 source 
    -./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:339:./docs/reports/2026-10-31-o78-worker2-slippage-unit.md:296:## Origin of "NT8 Analyzer slippage applies to market and stop fills, not 
    +./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:337:./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:42:3. **No NT8 text on disk defines the unit, or says which order types
    +./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:338:./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:112:2. The claim "the Analyzer slippage applies to market and stop fill
    +./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:339:./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:334:**E7. Origin of "market and stop fills, not limit fills"**
    +./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:340:./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:336:$ /usr/bin/grep -rIn --ignore-case --exclude-dir=.git "market and s
    +./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:341:./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:338:./docs/reports/2026-10-31-o78-worker2-slippage-unit.md:36:7. **"App
    +./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:342:./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:339:./docs/reports/2026-10-31-o78-worker2-slippage-unit.md:296:## Origi
    +./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:344:./docs/reports/2026-10-31-o78-worker2-slippage-unit.md:36:7. **"Applies to market and stop fills, not limit fills" has no NT8 source 
    +./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:345:./docs/reports/2026-10-31-o78-worker2-slippage-unit.md:296:## Origin of "NT8 Analyzer slippage applies to market and stop fills, not 
#### line 354 | DIFFERS | sed -n '127,150p' docs/reports/2026-10-31-o78-worker3-adversarial.md | pasted 6 lines, fresh 24 lines
    --- pasted
    +++ fresh
    @@ -6,0 +7,18 @@
    +```
    +SIM slip/side 0.02 window 20210308 20260717
    +  all  n, gross_pts(entry-slipped), net$ at $1/pt: (1180, '9230.25', '5690.25')
    +  long  (581, '5683.00', '3940.00')
    +  short (599, '3547.25', '1750.25')
    +  largest win 1 1792.50 20250409 123100 -> 160000 | largest loss 1 -325.75 20260702
    +  REPORTED run 4: n 1211 (L 584 / S 627), net 3136.84, L +4541.40, S -1404.56, largest win 1792.50
    +SIM[reversal-entry-IGNORED variant] slip/side 0.02 window 20210308 20260717
    +  all  n, gross_pts(entry-slipped), net$ at $1/pt: (1177, '9300.25', '5769.25')
    +  long  (580, '5635.25', '3895.25')
    +  short (597, '3665.00', '1874.00')
    +SIM[flat-at-last-bar-of-every-session variant] slip/side 0.02 window 20210308 20260717
    +  all  n, gross_pts(entry-slipped), net$ at $1/pt: (1179, '9895.50', '6358.50')
    +  long  (581, '6028.75', '4285.75')
    +  short (598, '3866.75', '2072.75')
    +  largest win 1 1792.50 20250409 123100 -> 160000 | largest loss 1 -325.75 20260702
    +```
    +(The column label "gross_pts(entry-slipped)" is stale. After the patch, gross is raw bar-price points, and net = gross − 0.04·n − 2.96·n. Check: 9230.25 − 1180×3.00 = 5690.25.)
#### line 383 | IDENTICAL | for f in "/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/s | pasted 2 lines, fresh 2 lines
#### line 390 | IDENTICAL | find . -path ./.git -prune -o -path ./.beads -prune -o -type f -newerm | pasted 5 lines, fresh 5 lines
#### line 398 | DIFFERS | git diff -U0 -- DISPATCH_LOG.md | tail -4 | cut -c1-200 | pasted 4 lines, fresh 4 lines
    --- pasted
    +++ fresh
    @@ -1 +0,0 @@
    -+- [2026-10-31T12:48:41Z] WHO: praxis-worker | WHAT: subagent closed | WHY: hook-recorded at SubagentStop, keyed close for corr=a1cd68e1526d6589d, matched 1 open row(s) | WHERE: closes corr=a1cd68e15
    @@ -4,0 +4 @@
    ++- [2026-10-31T13:12:14Z] WHO: praxis-worker | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session 0ced412 corr=ae73270cb6e608184 | WHEN: spawn | HOW: awaiting terminal stat
#### line 430 | IDENTICAL | git diff --cached --name-status -- 'docs/reports/2026-10-31-o78*' | pasted 4 lines, fresh 4 lines
```

**W4-E2. Import-file and arithmetic checks** (`python3 -I "$S/w4r_data.py"`)
```
file first/last row: ('20210307', '180100') ('20260720', '112700') n 1857362
first 2021 RTH-window row used by mgr_verify2: 20210308 093100 16032.75
  20250409 093000 18429.25 18453 18429.25 18443.5
  20250409 093100 18443.5 18511.75 18437.25 18481.75
  20250409 122900 18727.75 18741 18697.25 18700
  20250409 123000 18699.75 18707 18684.25 18693.25
  20250409 123100 18691.25 18702 18664.5 18698.25
  20250409 123200 18698.75 18711.25 18688.25 18696.25
  20250409 155900 20534 20555.75 20508.5 20515.75
  20250409 160000 20516 20552.5 20481.5 20486.75
  20250409 160100 20487.75 20600.5 20483.25 20559.75
count of stamps 093000: 1354 093100: 1355 160000: 1306 160100: 1305 000000: 1356
RTH days with H-L range >= 1795.50 pts: [('20240120', Decimal('16851.5')), ('20250409', Decimal('2184.50'))]
bar Open -> same-day 16:00 Close == +1795.50 (long): [('20250409', '123100')]
bar Open -> same-day 16:00 Close == -1795.50 (short): []
profit with entry+0.02/exit-0.02: 1792.50
profit with entry+0.04/exit+0.00: 1792.50
4541.40-1792.50 = 2748.90
run4 residue (3136.84+3*1211)%0.25 = 0.09
run3 residue (1281.61+3*1075)%0.25 = 0.11
cost ratios: comm pts $1 model 2.96 vs NQ 2.96/20 = 2E+1 | slip 0.04 vs NQ 20/20 = 25
Saturday rows: 127 [('20210320', '121100', Decimal('16241.5')), ('20210403', '122200', Decimal('16760.25')), ('20210403', '234700', Decimal('16760.25')), ('20210417', '131300', Decimal('17440')), ('20210501', '140800', Decimal('17281.25')), ('20210508', '155500', Decimal('17131.5')), ('20210515', '190500', Decimal('16814')), ('20210612', '101300', Decimal('17409.5'))]
E8 short n across 3 variants: 599, 597, 598 -> min 597 max 599
```

**W4-E3. Binary scan of the rescued tree, and the Saturday breakdown** (`python3 -I "$S/w4r_bin.py"`)
```
binary-type files scanned: 122
top extensions: [('.ncd', 9389), ('', 930), ('.png', 659), ('.cs', 632), ('.xml', 305), ('.xaml', 224), ('.flbx', 127), ('.hyb', 104), ('.dll', 103), ('.txt', 43), ('.par', 43), ('.contexttree', 42), ('.old', 40), ('.json', 30), ('.dat', 29)]
total hits: 0
Saturday dates: 66 rows: 127 rows in 09:31-16:00: 58
  2024-01-20 rows: 6 in RTH window: 6
  dates in run window 20210308-20260717 with RTH-window Saturday rows: 44
```

**W4-E4. Code timing and session logic; E10 file times**
```
$ /usr/bin/grep -n "CloseMod\|IsExitOnSessionClose\|int mod\|mod = \|CheckpointMin\|% 30\|Calculate\|BarsRequiredToTrade\|Slippage" ninjascript/PraxisNoiseAreaBreakout.cs
39:// NO LOOK-AHEAD: Calculate.OnBarClose + the 14-day σ lookback reads only COMPLETED prior sessions
58:		private const int CloseMod = 16 * 60;       // 960
105:				Calculate                                 = Calculate.OnBarClose;
108:				IsExitOnSessionCloseStrategy              = true;   // backstop; explicit 16:00 flat is primary
112:				BarsRequiredToTrade                       = 20;
143:			int mod = Time[0].Hour * 60 + Time[0].Minute;   // minute-of-day of THIS (closed) bar
168:			if (mod == CloseMod)
189:			if (mod >= CloseMod)
196:			bool isCheckpoint = (Time[0].Minute == 0 || Time[0].Minute == 30) && mod > OpenMod && mod < CloseMod;
238:		private void BuildBand(int mod)
$ /usr/bin/grep -n "OpenMod\|IsFirstBarOfSession\|todayOpen *=\|vwapCumPV *= \|vwapCumVol *= 0\|SessionIterator\|sessionStart\|== OpenMod" ninjascript/PraxisNoiseAreaBreakout.cs | cut -c1-170
57:		private const int OpenMod  = 9 * 60 + 30;   // 570
147:			if (Bars.IsFirstBarOfSession)
152:				todayOpen = Open[0];            // Open_{t,09:30} (spec §1) — first RTH bar's open
158:				vwapCumPV  = 0.0;              // re-anchor VWAP at the 09:30 open (spec §4 p.13 fn.2)
159:				vwapCumVol = 0.0;
196:			bool isCheckpoint = (Time[0].Minute == 0 || Time[0].Minute == 30) && mod > OpenMod && mod < CloseMod;
$ stat -f '%N mtime=%Sm birth=%SB' -t '%H:%M:%S' STATUS.md DECISION_LOG.md HANDOFF.md docs/reports/2026-10-31-o78-*.md
STATUS.md mtime=08:42:03 birth=08:42:03
DECISION_LOG.md mtime=08:42:03 birth=08:42:03
HANDOFF.md mtime=08:42:03 birth=08:42:03
docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md mtime=09:11:53 birth=08:42:52
docs/reports/2026-10-31-o78-worker1-symmetry.md mtime=09:07:53 birth=08:48:28
docs/reports/2026-10-31-o78-worker2-slippage-unit.md mtime=09:07:53 birth=08:53:24
docs/reports/2026-10-31-o78-worker3-adversarial.md mtime=09:06:16 birth=09:06:16
```

**W4-E5. Citation traces** (excerpts; `cut -c1-230/240`)
```
$ /usr/bin/grep -n "VERDICT\|brute\|8 of 8\|8/8\|F9\|Saturday\|Result:" docs/reports/2026-10-31-o78-worker3-adversarial.md
102:### E5. Exact match, band distance from the open, synthesis arithmetic, model brute force
125:The brute force covered point value {20, 5, 2, 1} × tick {0.25, 0.01} × slippage {0, 1, 2} ticks/side, with a $2.96 commission.
167:--- 2024-01-20 Saturday rows (bad prints)
184:| F9 | Out of scope (reported, not fixed): the import file | MINOR | E7: there are 6 rows dated **Saturday 2024-01-20**, one at `3100` (13:58) while real prices are ~17,500, giving an RTH range of 16,851.5 pts (E4). Harmless if the RTH template excludes Sa
187:- **W1 code-level symmetry (S).** 8/8 pasted blocks are byte-identical (E1). My own read of lines 138–291 found no long/short asymmetry. I checked:
215:VERDICT: BROKEN
216:Result: PASS
$ /usr/bin/grep -rn "2 ticks/side, \$10/side\|\$10/side" docs/reports/2026-10-30-zyd-f3-artifact.md DECISION_LOG.md
docs/reports/2026-10-30-zyd-f3-artifact.md:210:+- **(b) Intrabar fill assumption:** Strategy Analyzer `Order fill resolution` = **Standard**, set explicitly (explicitness REPORTED BY AMEAR, `2026-10-30T21:36:30Z`; the value OBSERVED on the 
docs/reports/2026-10-30-zyd-f3-artifact.md:226:+- `config/backtest-cost-model.json` → v1.1.0: slippage 1 → 2 ticks/side ($5 → $10/side; 2 → 4 ticks / $10 → $20 RT); `fill_resolution` High → Standard; total $12.96 / 2.592 ticks �
DECISION_LOG.md:442:- [2026-10-30T21:36:30Z] **WHO: amear** | PROPOSED BY: amear | APPROVED BY: amear, 2026-10-28 (voice session), reaffirmed in this session's opening message | WHAT: **F3 `[N]` IS SET: band-edge slippage = 2 ticks per side
docs/reports/2026-10-30-3gm-fidelity-check.md:949:- **F3 (FROZEN, fill resolution and slippage).** D3 shows every fill is a market fill (INFERRED type), so the Analyzer's 2-tick setting is applied to every market fill (INFERRED). DECISION_L
$ sed -n '52p' docs/reports/2026-10-28-voice-session-notes.md
- Settings are the same as run 3 except **Trading hours = CME US Index Futures RTH**. Amear is re-saving the "Praxis Backtest" default template with the corrected session.
$ sed -n '36,40p' docs/reports/2026-10-30-run3-backtest-screenshot-record.md   (E3 omits the header; columns confirmed All / Long / Short)
| Performance | All trades | Long trades | Short trades |
|---|---|---|---|
$ /usr/bin/grep -n "Result" scripts/gate-manager-output.sh | head -30
23:if ! grep -qiE 'Result:\s*(PASS|FAIL|BLOCKED)' "$LATEST"; then
```

**W4-E6. Rescued trading-hours templates** (regular Sessions block; the first entries in each file are holiday partials)
```
-----CME US Index Futures RTH
TimeZone ['Eastern Standard Time']
[('Monday', '830', 'Monday', '1600'), ('Tuesday', '830', 'Tuesday', '1600'), ('Wednesday', '830', 'Wednesday', '1600'), ('Thursday', '830', 'Thursday', '1600'), ('Friday', '830', 'Friday', '1600')]
-----US Equities RTH
TimeZone ['Eastern Standard Time']
[('Monday', '930', 'Monday', '1600'), ('Tuesday', '930', 'Tuesday', '1600'), ('Wednesday', '930', 'Wednesday', '1600'), ('Thursday', '930', 'Thursday', '1600'), ('Friday', '930', 'Friday', '1600')]
$ stat -f '%N mtime=%Sm' ".../templates/TradingHours/CME US Index Futures RTH.xml" ".../CME US Index Futures ETH.xml"
.../CME US Index Futures RTH.xml mtime=Aug 29 11:52:00 2026
.../CME US Index Futures ETH.xml mtime=Jul  9 10:37:20 2026
```

## Files staged

None. This report is unstaged by instruction (no `git add`).

VERDICT: SURVIVED-WITH-CORRECTIONS

Result: PASS
