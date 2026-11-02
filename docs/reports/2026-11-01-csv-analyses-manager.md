# Manager report: unit `2026-11-01-csv-analyses`

**Stated limitation (F3), carried by the deliverable:** Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

- **Date:** 2026-11-01. **Manager:** praxis-manager. **Deliverable:** `docs/reports/2026-11-01-csv-analyses.md`. **Grade:** ungraded at time of writing (the auditor is master-spawned; this report does not grade its own output beyond the manager's stress tests below).
- **Authorisation:** `DECISION_LOG.md` lines 463–464, both stamped 2026-11-01T21:20:40Z (Amear: "ok run them", read by the master as §6.A of `docs/reports/2026-11-01-voice-handoff-results-and-next-build.md`; master DISPATCH row).

## Task

Run the five CSV-only analyses of §6.A on the four Desktop trade lists (baseline PraxisNoiseAreaBreakout, _OppBand, _Flat1559, PraxisLastHalfHourMomentum): P&L by year (and year × side); results with top 5 / top 10 winners and top 5 losers removed; long vs short by year; drawdown profile (max DD dates and durations, five deepest, longest under water); slippage at 3 and 4 ticks/side by arithmetic. Facts and open questions only (R-1101-5). Add the MANIFEST rows (the new report and the owed voice-handoff-3 row). Leave everything unstaged.

## Rubric criteria addressed

| Criterion | How addressed | Evidence |
|---|---|---|
| S1 every claim has pasted output | Deliverable Appendix A pastes K01–K11; blocks identical to the canonical output files (blk.py, E08); each command re-runs to identical output and exit code (W4's chk.py, E09) | E08, E09 |
| S2 no claim above its evidence | Four soft spots found by the manager (file→strategy mapping, tick value, `n/a` rule, 2-tick premise) closed with new evidence K10/K11 or downgraded; W4's MAJOR and 9 MINORs corrected | E05, Adversarial findings |
| S3 gates tripped | Gate 0 tripped with swapped inputs; block checker, reconciliation script and W4's re-run checker each tripped by a mutation | E03, E07, E10, E17 |
| S8 Amear's questions not answered | Six questions in "§7 Open questions for Amear", none answered | E19, E12 (heading list); W4 attack 5 (worker-reported) |
| F3 stated limitation | Sentence verbatim at lines 3 and 59; line 286 states no claim F3 is unfrozen or satisfied | E12 |
| F2 frozen | Nothing about the trading-hours template or session flat changed, proposed or decided; no config file touched | E13 |
| R-1101-5 no ranking | Ranking-word grep on the prose (lines 1–299) hits only the "unfrozen" denial at line 286, which shows the grep is live | E12 |

## Workers dispatched

| id | agent id | mode | scope | outcome |
|---|---|---|---|---|
| W1 | a132f45de01b024a5 | BUILD | `analyze.py`, `run.sh`, catalogue K01–K09, outputs run twice and `diff -r` identical (E18) | PASS; Gate 0 MATCH on all four runs (E02) |
| W2 | a19e12d6d248dc4c9 | ADVERSARIAL | independent awk recomputation (integer cents) of totals, per-year net, top-5 removed, max-DD dates, 4-tick net; never saw W1 | PASS; 60 of 60 overlapping figures equal W1 (E06) |
| W3 | afddb492073207e63 | BUILD | writer: deliverable draft from the manager's re-run outputs | PASS |
| W3b | aa07f46db7a02b9e7 | BUILD | exact-text corrections E1–E8 (manager-found S2 gaps) + K10/K11 appendix blocks | PASS |
| W4 | a39f45c427e9de8ab | ADVERSARIAL | attack the installed deliverable: re-run checker, number tracing, grading, cites, S8/F2/F3/R-1101-5, raw-CSV spot checks | VERDICT: FAIL (1 MAJOR, 9 MINOR) |
| W5 | a5a882df1aca2d560 | BUILD | exact-text corrections F1–F10 for W4's findings | PASS |
| W6 | a9d16eee869959751 | ADVERSARIAL | attack this manager report draft and the planned return summary | VERDICT: FAIL (2 MAJOR, 7 MINOR); all fixed, see Adversarial findings |

## Process log

1. Read the DECISION_LOG authorisation rows, the voice handoff §0–§6, SPEC_RUBRIC S1/S2/S8/F2/F3, MANIFEST rows 175–185. Hashed the four inputs; all four match the brief (E01).
2. W1 and W2 dispatched in parallel, W2 isolated from W1's directory.
3. Manager read W1's outputs (not its summary). The pasted output labelled years "best year"/"worst year"; to keep R-1101-5 wording out of pasted evidence the manager changed that one print line to "highest-net year"/"lowest-net year" (E04) and re-ran the whole catalogue into `csva/mgr/out`. Only K03 (script hash) and K05 (the four label lines) changed (E05). `csva/mgr/out` is the canonical evidence.
4. Gate 0 negative test: R0/R1 inputs swapped → two MISMATCH lines, `GATE0: FAIL`, rc 1 (E03).
5. W3 wrote the draft. The manager read the prose and found four S2 soft spots. Added catalogue commands K10 (Strategy column per file; 0.25 price grid with a 0.50-grid firing control) and K11 (the script's share-of-net rule); W3b applied exact replacements.
6. Manager block checker `blk.py`: all embedded blocks identical to fresh outputs; a one-digit mutation of K05 reported `DIFFERENT` and the restored file `identical` (E17 repeats this trip against a copy of the canonical outputs; blk.py reports in text and exits 0 either way). E08 is the post-correction run.
7. Report copied to `docs/reports/2026-11-01-csv-analyses.md`; three MANIFEST rows appended (the brief's verbatim owed row, the deliverable, this manager report).
8. W4 attacked the installed copy: 1 MAJOR + 9 MINOR. W5 applied exact replacements F1–F10; manager re-installed and re-ran W4's own checker (E09).
9. Manager found one more defect: the appendix note said each command ran as `zsh -c '<command>'`, but K10 contains single quotes, so that literal form fails with a parse error; pasting into zsh at `/` reproduces K10 (E11). The manager corrected that note line twice (single-line edits): first to the mechanism, then to name the runner `( cd / && zsh -c "$cmd" )` exactly. After W6, the manager also corrected the deliverable's Author line (single line) to name W3b, W5 and the manager's edits.
10. Reconciliation of W1 against W2's raw `out.txt` scripted (`recon.py`): 60/60 MATCH; a one-cent mutation produces exactly one DIFF (E06, E07).
11. Protected paths: modified after the csva scratch dir's birth time are only the two reports, MANIFEST.md and DISPATCH_LOG.md (E13); DISPATCH_LOG.md's rows for this unit's worker ids are hook-recorded SubagentStart/SubagentStop rows, not manager writes (E15). None of this unit's paths are in the index (E14).
12. W6 attacked the draft of this report and the planned return summary: 2 MAJOR, 7 MINOR, all fixed (Adversarial findings). This report was then installed and every E-block re-captured after installation, so E13 lists it.

## Verification evidence (pasted output only)

Each block is the captured file, unedited: first line `$ <command>`, last line `[exit N]` (the runner's exit code for the whole command). Each command was run with `zsh -c` from cwd `/Volumes/Sensidine/Praxis.build`, with this prefix prepended (not shown in the `$` line): `S=/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/csva; R=docs/reports/2026-11-01-csv-analyses.md; D="$HOME/Desktop/NinjaTrader Grid 2026-11-01"; `. Scripts referenced live in the session scratchpad, not the repo.

### E01 — sha256 of the four input CSVs (read-only inputs unchanged)

```text
$ shasum -a 256 "$D 07-10 AM.csv" "$D 07-57 AM.csv" "$D 07-59 AM.csv" "$D 08-00 AM.csv"
421c44e6cd9d417b432be1a5b440b0861782a3bba7e1961beba5b5421e0534bd  /Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-10 AM.csv
4207ea99e7f1187b54ebe45c97822409629192ed12e7ee0dbaacb241c152b6e8  /Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-57 AM.csv
5a3c4d783a44b33a18c4eb77f50444af1d4cf65ed4190038becc4c2007c868e0  /Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-59 AM.csv
4efd8ce8e95cc408f82d494fcf55238c25b9980b030a39eb25f4eaa5fbd180d9  /Users/admin/Desktop/NinjaTrader Grid 2026-11-01 08-00 AM.csv
[exit 0]
```

### E02 — Gate 0 lines from the canonical K04 output

```text
$ grep -E "MATCH|GATE0" $S/mgr/out/K04.txt
R0 baseline NAB: trades=1190 net=197327.60 PF=1.29 maxDD=-45282.04 | ref 197327.60/1.29/-45282.04 -> MATCH
R1 NAB_OppBand: trades=810 net=210182.40 PF=1.26 maxDD=-50748.88 | ref 210182.40/1.26/-50748.88 -> MATCH
R2 NAB_Flat1559: trades=1190 net=193017.60 PF=1.28 maxDD=-40637.04 | ref 193017.60/1.28/-40637.04 -> MATCH
R3 LastHalfHourMomentum: trades=1304 net=-76009.84 PF=0.84 maxDD=-99806.96 | ref -76009.84/0.84/-99806.96 -> MATCH
GATE0: PASS
[exit 0]
```

### E03 — Gate 0 negative test: R0 and R1 inputs swapped

```text
$ python3 -I $S/w1/analyze.py gate0 "$D 07-57 AM.csv" "$D 07-10 AM.csv" "$D 07-59 AM.csv" "$D 08-00 AM.csv" | grep -E "MATCH|GATE0"; print "analyze.py rc=${pipestatus[1]}"
R0 baseline NAB: trades=810 net=210182.40 PF=1.26 maxDD=-50748.88 | ref 197327.60/1.29/-45282.04 -> MISMATCH
R1 NAB_OppBand: trades=1190 net=197327.60 PF=1.29 maxDD=-45282.04 | ref 210182.40/1.26/-50748.88 -> MISMATCH
R2 NAB_Flat1559: trades=1190 net=193017.60 PF=1.28 maxDD=-40637.04 | ref 193017.60/1.28/-40637.04 -> MATCH
R3 LastHalfHourMomentum: trades=1304 net=-76009.84 PF=0.84 maxDD=-99806.96 | ref -76009.84/0.84/-99806.96 -> MATCH
GATE0: FAIL
analyze.py rc=1
[exit 0]
```

### E04 — the manager's single-line label edit to analyze.py

```text
$ diff $S/mgr/analyze.py.orig $S/w1/analyze.py; print "diff rc=$?"
166c166
<             print("best year %s (%s); worst year %s (%s)" % (b, money(nets[b]), w, money(nets[w])))
---
>             print("highest-net year %s (%s); lowest-net year %s (%s)" % (b, money(nets[b]), w, money(nets[w])))
diff rc=1
[exit 0]
```

### E05 — W1's original outputs vs the manager's re-run (only K03, K05 change; K10, K11 added)

```text
$ diff -r $S/w1/out $S/mgr/out | grep -E "^(diff|Only|[<>])" | sed -E "s#$S/##g"
diff -r w1/out/K03.txt mgr/out/K03.txt
< 368f7e81c9c1676711a33d37855b849a4da42683124096a7d3f07061b47bf507  w1/analyze.py
> d3cd15e0c9f103906867f9b0125b07fcb4001950f6cb8bcbdc2ec6a036c26ab6  w1/analyze.py
diff -r w1/out/K05.txt mgr/out/K05.txt
< best year 2022 (81034.80); worst year 2026 (-3151.84)
> highest-net year 2022 (81034.80); lowest-net year 2026 (-3151.84)
< best year 2022 (95046.60); worst year 2021 (1609.20)
> highest-net year 2022 (95046.60); lowest-net year 2021 (1609.20)
< best year 2022 (75649.80); worst year 2026 (-3531.84)
> highest-net year 2022 (75649.80); lowest-net year 2026 (-3531.84)
< best year 2022 (17388.88); worst year 2025 (-38002.64)
> highest-net year 2022 (17388.88); lowest-net year 2025 (-38002.64)
Only in mgr/out: K10.txt
Only in mgr/out: K11.txt
[exit 0]
```

### E06 — W1 (canonical outputs) vs W2 (independent awk, raw out.txt): every overlapping figure

```text
$ python3 -I $S/mgr/recon.py $S/w2/out.txt $S/mgr/out
R0 net                  W1=197327.60      W2=197327.60      MATCH
R0 PF                   W1=1.29           W2=1.29           MATCH
R0 maxDD                W1=-45282.04      W2=-45282.04      MATCH
R0 net 2021             W1=13557.84       W2=13557.84       MATCH
R0 net 2022             W1=81034.80       W2=81034.80       MATCH
R0 net 2023             W1=39829.00       W2=39829.00       MATCH
R0 net 2024             W1=48603.28       W2=48603.28       MATCH
R0 net 2025             W1=17454.52       W2=17454.52       MATCH
R0 net 2026             W1=-3151.84       W2=-3151.84       MATCH
R0 top5 sum             W1=85960.20       W2=85960.20       MATCH
R0 net ex top5          W1=111367.40      W2=111367.40      MATCH
R0 DD peak date         W1=2025-04-10     W2=2025-04-10     MATCH
R0 DD trough date       W1=2026-06-03     W2=2026-06-03     MATCH
R0 DD recovery          W1=not recovered  W2=not recovered  MATCH
R0 net @4 ticks (model) W1=173527.60      W2=173527.60      MATCH
R1 net                  W1=210182.40      W2=210182.40      MATCH
R1 PF                   W1=1.26           W2=1.26           MATCH
R1 maxDD                W1=-50748.88      W2=-50748.88      MATCH
R1 net 2021             W1=1609.20        W2=1609.20        MATCH
R1 net 2022             W1=95046.60       W2=95046.60       MATCH
R1 net 2023             W1=22937.52       W2=22937.52       MATCH
R1 net 2024             W1=59367.12       W2=59367.12       MATCH
R1 net 2025             W1=19058.56       W2=19058.56       MATCH
R1 net 2026             W1=12163.40       W2=12163.40       MATCH
R1 top5 sum             W1=89810.20       W2=89810.20       MATCH
R1 net ex top5          W1=120372.20      W2=120372.20      MATCH
R1 DD peak date         W1=2025-04-10     W2=2025-04-10     MATCH
R1 DD trough date       W1=2026-03-11     W2=2026-03-11     MATCH
R1 DD recovery          W1=not recovered  W2=not recovered  MATCH
R1 net @4 ticks (model) W1=193982.40      W2=193982.40      MATCH
R2 net                  W1=193017.60      W2=193017.60      MATCH
R2 PF                   W1=1.28           W2=1.28           MATCH
R2 maxDD                W1=-40637.04      W2=-40637.04      MATCH
R2 net 2021             W1=14427.84       W2=14427.84       MATCH
R2 net 2022             W1=75649.80       W2=75649.80       MATCH
R2 net 2023             W1=36164.00       W2=36164.00       MATCH
R2 net 2024             W1=48353.28       W2=48353.28       MATCH
R2 net 2025             W1=21954.52       W2=21954.52       MATCH
R2 net 2026             W1=-3531.84       W2=-3531.84       MATCH
R2 top5 sum             W1=84795.20       W2=84795.20       MATCH
R2 net ex top5          W1=108222.40      W2=108222.40      MATCH
R2 DD peak date         W1=2025-04-10     W2=2025-04-10     MATCH
R2 DD trough date       W1=2026-06-03     W2=2026-06-03     MATCH
R2 DD recovery          W1=not recovered  W2=not recovered  MATCH
R2 net @4 ticks (model) W1=169217.60      W2=169217.60      MATCH
R3 net                  W1=-76009.84      W2=-76009.84      MATCH
R3 PF                   W1=0.84           W2=0.84           MATCH
R3 maxDD                W1=-99806.96      W2=-99806.96      MATCH
R3 net 2021             W1=-1934.24       W2=-1934.24       MATCH
R3 net 2022             W1=17388.88       W2=17388.88       MATCH
R3 net 2023             W1=-10656.12      W2=-10656.12      MATCH
R3 net 2024             W1=-23974.08      W2=-23974.08      MATCH
R3 net 2025             W1=-38002.64      W2=-38002.64      MATCH
R3 net 2026             W1=-18831.64      W2=-18831.64      MATCH
R3 top5 sum             W1=17070.20       W2=17070.20       MATCH
R3 net ex top5          W1=-93080.04      W2=-93080.04      MATCH
R3 DD peak date         W1=2022-05-04     W2=2022-05-04     MATCH
R3 DD trough date       W1=2026-07-17     W2=2026-07-17     MATCH
R3 DD recovery          W1=not recovered  W2=not recovered  MATCH
R3 net @4 ticks (model) W1=-102089.84     W2=-102089.84     MATCH
compared=60 differ=0
[exit 0]
```

### E07 — reconciliation trip: one cent altered in a copy of W2's output

```text
$ sed "s/net=-38002.64/net=-38002.65/" $S/w2/out.txt > $S/mgr/w2mut.txt; python3 -I $S/mgr/recon.py $S/mgr/w2mut.txt $S/mgr/out | grep -E "DIFF|compared"
R3 net 2025             W1=-38002.64      W2=-38002.65      DIFF
compared=60 differ=1
[exit 0]
```

### E08 — manager block checker: deliverable Appendix A blocks vs canonical outputs

```text
$ python3 -I $S/mgr/blk.py $R $S/mgr/out K01 K02 K03 K04 K05 K06 K07 K08 K09 K10 K11
K01 identical 765
K02 identical 544
K03 identical 641
K04 identical 3664
K05 identical 2826
K06 identical 7056
K07 identical 5202
K08 identical 4825
K09 identical 1523
K10 identical 1144
K11 identical 217
[exit 0]
```

### E09 — W4's independent re-run checker on the installed deliverable (runs every pasted command with zsh -c from /)

```text
$ python3 -I $S/w4/chk.py $R
K01 MATCH lines=4 exit=0
K02 MATCH lines=5 exit=0
K03 MATCH lines=2 exit=0
K04 MATCH lines=38 exit=0
K05 MATCH lines=45 exit=0
K06 MATCH lines=106 exit=0
K07 MATCH lines=45 exit=0
K08 MATCH lines=38 exit=0
K09 MATCH lines=21 exit=0
K10 MATCH lines=12 exit=0
K11 MATCH lines=1 exit=0
blocks=11 mismatches=0
[exit 0]
```

### E10 — W4's checker trip: last `[exit 0]` in a copy of the deliverable altered to `[exit 1]`

```text
$ python3 -I -c "import sys;t=open(sys.argv[1]).read();a,b=t.rsplit('[exit 0]',1);open(sys.argv[2],'w').write(a+'[exit 1]'+b)" $R $S/mgr/mut.md; python3 -I $S/w4/chk.py $S/mgr/mut.md | grep -E "MISMATCH|blocks="
K11 MISMATCH exit pasted=1 real=0
blocks=11 mismatches=1
[exit 0]
```

### E11 — K10 contains single quotes: paste-into-zsh form vs literal single-quote wrap

```text
$ awk 'substr($0,1,2)=="$ " && index($0,q){print NR": "substr($0,1,40)}' q="'" $R; sed -n 673p $R | cut -c3- > $S/mgr/k10cmd.txt; (cd / && zsh < $S/mgr/k10cmd.txt) > $S/mgr/k10stdin.out 2>&1; print "stdin form rc=$?"; sed -n '2,$p' $S/mgr/out/K10.txt | sed '$d' | cmp - $S/mgr/k10stdin.out && print "stdin form output == K10 block"; (cd / && eval "zsh -c '$(cat $S/mgr/k10cmd.txt)'") 2>&1 | head -1; print "literal single-quote wrap rc=${pipestatus[1]}"
673: $ for f in "$HOME/Desktop/NinjaTrader Gr
stdin form rc=0
stdin form output == K10 block
(eval):1: parse error near `)'
literal single-quote wrap rc=1
[exit 0]
```

### E12 — ranking-word grep on the prose (positive control: the "unfrozen" denial), F3 sentence lines, placeholder count, section headings

```text
$ awk 'NR<300' $R | /usr/bin/grep -n -i -w -E "best|worst|better|worse|outperform|recommend|prefer|superior|strongest|weakest|should|unfrozen" | cut -c1-90; /usr/bin/grep -n -F "Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed." $R | cut -c1-40; print "placeholder-token count: $(/usr/bin/grep -c -i -w 'T[B]D' $R)"; /usr/bin/grep -n "^## " $R
286:- It does not grade F3 and makes no claim that F3 is unfrozen or satisfied.
3:**Stated limitation (F3):** Fills are 
59:- **F3:** Fills are optimistic; Stand
placeholder-token count: 0
13:## Grading key
23:## Inputs and reproduction
57:## Limitations
66:## §1 P&L by year
91:## §2 Top winners removed
131:## §3 Long vs short by year
192:## §4 Drawdown profile
252:## §5 Slippage sensitivity (arithmetic model)
280:## §6 What this report does not do
288:## §7 Open questions for Amear
299:## Appendix A — Verification evidence (pasted command output)
[exit 0]
```

### E13 — files modified after the csva scratch dir's birth time (2026-11-01 16:22:28 local); git status of this unit's paths; MANIFEST diff

```text
$ print "csva birth: $(stat -f %SB $S)"; find . -newermt "2026-11-01 16:22:28" -type f -not -path "./.git/*" -not -path "./.beads/*"; git status --short MANIFEST.md $R docs/reports/2026-11-01-csv-analyses-manager.md; git diff MANIFEST.md | grep -E "^[-+]"
csva birth: Nov  1 16:22:28 2026
./docs/reports/2026-11-01-csv-analyses.md
./docs/reports/2026-11-01-csv-analyses-manager.md
./MANIFEST.md
./DISPATCH_LOG.md
 M MANIFEST.md
?? docs/reports/2026-11-01-csv-analyses-manager.md
?? docs/reports/2026-11-01-csv-analyses.md
--- a/MANIFEST.md
+++ b/MANIFEST.md
+| /docs/reports/2026-11-01-voice-handoff-results-and-next-build.md | Report | 2 | 2026-11-01 | voice-agent handoff: three-strategy results, backtest options, build backlog (2026-11-01); praxis-master |
+| /docs/reports/2026-11-01-csv-analyses.md | Report | 2 | 2026-11-01 | CSV-only analyses of the four 2026-11-01 runs (P&L by year, top 5/10 winners removed, long vs short by year, drawdown profile, slippage arithmetic model at 3/4 ticks/side); facts and open questions only; ungraded at time of row |
+| /docs/reports/2026-11-01-csv-analyses-manager.md | Report | 2 | 2026-11-01 | Manager report for unit 2026-11-01-csv-analyses; ungraded at time of row |
[exit 0]
```

### E14 — none of this unit's paths are staged

```text
$ git diff --cached --name-only | grep -E "csv-analyses|MANIFEST"; print "grep rc=$? (1 = none of this unit's paths staged)"; print "staged paths: $(git diff --cached --name-only | wc -l | tr -d " ")"
grep rc=1 (1 = none of this unit's paths staged)
staged paths: 12
[exit 0]
```

### E15 — DISPATCH_LOG.md rows for this unit's worker ids are hook-written

```text
$ for a in a132f45de01b024a5 a19e12d6d248dc4c9 afddb492073207e63 aa07f46db7a02b9e7 a39f45c427e9de8ab a5a882df1aca2d560 a9d16eee869959751; do print -r -- "$a rows=$(/usr/bin/grep -c "corr=$a" DISPATCH_LOG.md) hook-recorded=$(/usr/bin/grep "corr=$a" DISPATCH_LOG.md | /usr/bin/grep -c "hook-recorded at Subagent")"; done
a132f45de01b024a5 rows=2 hook-recorded=2
a19e12d6d248dc4c9 rows=2 hook-recorded=2
afddb492073207e63 rows=2 hook-recorded=2
aa07f46db7a02b9e7 rows=2 hook-recorded=2
a39f45c427e9de8ab rows=2 hook-recorded=2
a5a882df1aca2d560 rows=2 hook-recorded=2
a9d16eee869959751 rows=2 hook-recorded=2
[exit 0]
```

### E16 — the staged index as it stands (none of it this unit's)

```text
$ git diff --cached --name-status
M	ISSUE_REGISTER.md
A	docs/reports/2026-08-06-session42-r8j-phase3-import.md
A	docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
A	docs/reports/2026-08-07-session44-r8j-offset-correction-adversarial.md
A	docs/reports/2026-08-07-session44-r8j-offset-correction-worker1.md
A	docs/reports/2026-08-07-session44-r8j-offset-correction.md
A	docs/reports/2026-10-28-f4-davi-reply-filing.md
A	docs/reports/2026-10-28-nightly-checks-plan-review-note.md
A	docs/reports/2026-10-28-nightly-checks-plan-review-rebuild.md
A	docs/reports/evidence/2026-10-28-mffu-davi-reply-transcript.md
A	docs/reports/evidence/2026-10-28-mffu-davi-reply.png
M	docs/specs/2026-08-08-ledger-compaction-spec.md
[exit 0]
```

### E17 — manager block-checker trip: one digit altered in a copy of the canonical K05 (blk.py reports in text; it exits 0 either way)

```text
$ rm -rf $S/mgr/outmut; cp -R $S/mgr/out $S/mgr/outmut; sed -i "" "s/81034.80/81034.81/" $S/mgr/outmut/K05.txt; python3 -I $S/mgr/blk.py $R $S/mgr/outmut K04 K05 K06; print "blk.py rc=$?"
K04 identical 3664
K05 DIFFERENT 2826
K06 identical 7056
blk.py rc=0
[exit 0]
```

### E18 — W1's two runs of its catalogue (pre-label-edit script) compared

```text
$ diff -r $S/w1/out $S/w1/out2; print "diff -r rc=$?"
diff -r rc=0
[exit 0]
```

### E19 — count of numbered questions in the deliverable's §7

```text
$ awk '/^## §7 /{f=1;next} /^## /{f=0} f && /^[0-9]+\. /{n++} END{print "numbered questions in §7: " n}' $R
numbered questions in §7: 6
[exit 0]
```

### E20 — single-occurrence checks (`count(`) in the four correction scripts

```text
$ grep -n "count(" $S/w3/fix.py $S/w3/fix2.py $S/mgr/fix3.py $S/mgr/fix4.py | sed -E "s#$S/##" | cut -c1-110
w3/fix.py:6:    n = t.count(old)
w3/fix.py:15:    if t.count(m) != 1: sys.exit(f"FAIL E3: marker {m!r} occurs {t.count(m)} times")
w3/fix.py:20:if t.count(tv) != 1: sys.exit(f"FAIL E4: occurs {t.count(tv)}")
w3/fix2.py:28:    c = s.count(o)
w3/fix2.py:35:    assert s.count(n) >= 1
mgr/fix3.py:5:assert t.count(old)==1, t.count(old)
mgr/fix4.py:5:assert t.count(old)==1, t.count(old)
[exit 0]
```

### E22 — deliverable lines changed after W5: the manager's single-line edits (appendix note, Author line)

```text
$ diff $S/w3/report.pre-fix3.md $R | grep -E "^[0-9]"; print "lines changed after W5 (manager edits): see above"
10c10
301c301
lines changed after W5 (manager edits): see above
[exit 0]
```

### E21 — git tracking status of the voice-handoff file, the deliverable and the prior three-strategy report

```text
$ git ls-files --error-unmatch docs/reports/2026-11-01-voice-handoff-results-and-next-build.md $R docs/reports/2026-11-01-three-strategy-results.md 2>&1; print "rc=$?"
error: pathspec 'docs/reports/2026-11-01-voice-handoff-results-and-next-build.md' did not match any file(s) known to git
error: pathspec 'docs/reports/2026-11-01-csv-analyses.md' did not match any file(s) known to git
Did you forget to 'git add'?
docs/reports/2026-11-01-three-strategy-results.md
rc=1
[exit 0]
```

## Adversarial findings

**W2 (independent recomputation).** Built from scratch in awk with integer cents, without access to W1's directory. All four reference totals reproduced. Scripted reconciliation against W1's canonical outputs: 60 compared, 0 differ (E06); the reconciliation script reports a planted one-cent change (E07). Overlap covered: net, PF, max DD, net per year 2021–2026, top-5 sum and net without top 5, max-DD peak/trough dates and recovery status, net at 4 ticks/side (arithmetic model), for each of the four runs. No disagreement needed reconciling.

**Manager-found defects (before W4).**
- Pasted output carried "best year"/"worst year" labels: label line changed, catalogue re-run (E04, E05).
- S2 soft spots in the draft: the file→strategy mapping was UNVERIFIED (now OBSERVED from K10's Strategy column); the $5.00 tick value was UNVERIFIED (now INFERRED from K10's 0.25 grid, with a firing 0.50 control, plus K04's $20 re-derivation); the `n/a (net <= 0)` rule was UNVERIFIED (now OBSERVED from K11's source line); the 2-ticks/side premise was labelled OBSERVED from a script header (now traced to the F3 sentence and prior-report L51, UNVERIFIED for exits).

**W4 (adversary on the deliverable): VERDICT FAIL, 1 MAJOR + 9 MINOR.** Its checker re-ran all 11 pasted commands (11 MATCH) and its own trip produced mismatches; its raw-CSV spot checks all matched (worker-reported: its `spot.txt` holds the recomputed values; the comparison with the deliverable is W4's statement, not re-pasted here). Disposition:

| # | sev | finding | disposition |
|---|---|---|---|
| 1 | MAJOR | L206 "a span to the end of the data" is false for R0–R2 (last trade 2026-07-15) | fixed (W5 F4): span to each run's last trade exit, dates from K08 |
| 2 | MINOR | L63 "none launches a backtest" labelled OBSERVED | fixed (F2): INFERRED from the pasted commands |
| 3 | MINOR | k=2 check cannot fail | fixed (F7): INFERRED note that it checks summing only |
| 4 | MINOR | prior-report fill findings not scoped by run | fixed (F5, F6): baseline/Flat1559 entries at L51, LastHalfHourMomentum at L357, no OppBand finding cited |
| 5 | MINOR | "recorded at 2 ticks/side" unsupported for exits | fixed (F6, F9): premise attributed to the F3 sentence; UNVERIFIED for exits |
| 6 | MINOR | `sides=` called side totals | fixed (F3): side trade counts |
| 7 | MINOR | "adjacent" April-2025 dates are not adjacent | fixed (F10): nearby, 2025-04-01 to 2025-04-11 |
| 8 | MINOR | "the catalogue describes" — no catalogue in the report | fixed (F1): K04 `rows=` and `header_fields=` cited, INFERRED |
| 9a | MINOR | MANIFEST row names this manager report before it existed | not a defect at return: this file now exists (E13 is re-captured after this file was written) |
| 9b | MINOR | new MANIFEST rows lack the "untracked in git" note used at MANIFEST L185 | not applied: the owed row's text was given verbatim by the master. The voice-handoff file and the deliverable are untracked (E21), like the file whose row at MANIFEST L185 carries the note, so W4's precedent holds; whether to add the note is the master's call |
| 10 | MINOR | L285 omitted the manager report from "only repo writes" | fixed (F8), graded UNVERIFIED in the deliverable with a pointer here |

**Manager-found after W4.** The appendix note's literal `zsh -c '<command>'` recipe fails for K10, which contains single quotes (E11). The note was corrected, and the corrected deliverable passes both checkers (E08, E09).

**W6 (adversary on this report's draft and the planned return summary): VERDICT FAIL, 2 MAJOR + 7 MINOR.** It re-ran all 16 E-blocks then present; E01–E12 and E14–E16 matched. Disposition:

| # | sev | finding | disposition |
|---|---|---|---|
| 1 | MAJOR | E13 used `find -newer <dir>`, which keys on the directory's mtime; creating a sub-folder moved it, so the claim "since the scratch dir was created" was false and a re-run printed nothing | fixed: E13 now prints the dir's birth time and uses `-newermt "2026-11-01 16:22:28"` |
| 2 | MAJOR | row 9a and Files staged cited this file before it was installed | fixed: installed first, then every E-block re-captured |
| 3 | MINOR | blk.py trip claimed, not pasted | fixed: E17 |
| 4 | MINOR | S1 row said blk.py "re-runs" blocks; it compares stored files | fixed: S1 row reworded |
| 5 | MINOR | 9b reasoning wrong (the three-strategy report is tracked) | fixed: 9b now cites E21 |
| 6 | MINOR | unpasted claims: W4 spot checks, W1 `diff -r`, "six questions", single-occurrence checks | fixed: E18, E19, E20, E22; W4 spot checks labelled worker-reported |
| 7 | MINOR | Process log 11 cited E13 for hook-written rows | fixed: cites E15 |
| 8 | MINOR | return summary: R2 lacked "partial year", 4-tick figures lacked "arithmetic model", F3 sentence missing | fixed in the return |
| 9 | MINOR | deliverable Author line omitted W3b, W5 and the manager edits | fixed (single line); deliverable blocks re-checked (E08, E09) |

## S6 cross-block check

This unit is not a plan deviation and adds none, so there is no approved deviation to test against other blocks. It was checked against each frozen item it could touch: F1 (signal-path vs breaker placement) is not touched — no code, no signal-path or breaker text. F2: nothing about the trading-hours template or the session-flat rule was changed, proposed or decided; the deliverable mentions neither except to say so in its §6. F3: the limitation sentence is carried verbatim, and the deliverable says it makes no claim F3 is unfrozen or satisfied (E12). F4 (MFFU confirmation) is not touched. No `.cs`, config, DECISIONS.md, DECISION_LOG.md, HANDOFF.md, STATUS.md or SPEC_RUBRIC.md change (E13).

## Acceptance checklist

| # | item (from the brief) | status | evidence |
|---|---|---|---|
| 1 | Five analyses on all four runs | done | deliverable §1–§5; K05–K09 |
| 2 | Reference totals reproduced before anything else | done | E02; trip E03 |
| 3 | Inputs read-only, cited by path + sha256 | done | E01; deliverable K01 |
| 4 | F3 sentence verbatim near the top; F3 not claimed unfrozen | done | E12 (L3, L59, L286) |
| 5 | No ranking, no "best", no recommendation | done | E12; W4 attack 5 |
| 6 | Amear's questions listed, not answered | done | deliverable §7; W4 attack 5 |
| 7 | Every number traces to pasted output in the appendix (S1) | done | E08, E09; W4 number tracing (worker-reported) |
| 8 | Every command runs as pasted from `/` via `zsh -c`; each test-run | done, with one disclosed caveat: K10 must be pasted into zsh, not wrapped in single quotes | E09, E11 |
| 9 | Every statement graded OBSERVED / INFERRED / UNVERIFIED | done after W4/W5 corrections | Adversarial findings |
| 10 | Slippage labelled as a model each time | done | deliverable §5 (every 3/4-tick row carries "arithmetic model") |
| 11 | W2 independent: per-year net, top-5-removed net, max-DD dates, 4-tick net | done, 60/60 | E06, E07 |
| 12 | MANIFEST rows: the new report + the owed voice-handoff-3 row (verbatim) | done (plus a row for this manager report) | E13 |
| 13 | Nothing staged; nothing recorded in git; nothing else touched | done | E13, E14, E15 |
| 14 | Correction passes change only defective text | done | W3b and W5 diffs were exact OLD→NEW replacements asserted to occur once (E20 shows the `count(` checks); manager edits are single lines (E04; E22 shows the deliverable changed after W5 only at lines 10 and 301) |

## Files staged

None. The brief says leave everything unstaged; E14 shows none of this unit's paths in the index. The 12 staged paths (E16) are, by name, the staged entries in the session-start git status the harness supplied to this manager; that snapshot is not command output pasted here, so the comparison is INFERRED. Files this unit wrote, unstaged: `docs/reports/2026-11-01-csv-analyses.md` (new), `docs/reports/2026-11-01-csv-analyses-manager.md` (new, this file), `MANIFEST.md` (three appended rows) — E13.

## Open items for the master

- MANIFEST "untracked in git" note on the new rows (W4 9b): the master's call.
- The analysis scripts and evidence runner live only in the session scratchpad (`csva/w1/analyze.py`, sha256 `d3cd15e0c9f1…` in K03); once the scratchpad is cleared, Appendix A can no longer be re-run.
- The deliverable is ungraded: auditor run by the master.

**Result: PASS**

(This is the manager's step result after the stress tests above; it is not an audit grade.)
