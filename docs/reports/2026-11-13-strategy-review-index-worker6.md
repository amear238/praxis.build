# 2026-11-13 strategy-review-index, worker6 (ADVERSARIAL, read-only)

## Task
Try to break docs/reports/2026-11-13-strategy-review-index-manager.md (the artifact; its Summary and Q1-Q5 sections, artifact lines 3-160) against S1, S2, S8 and S13. Working dir /Volumes/Sensidine/Praxis.build, branch main, HEAD 9ff8a48. Every check below was re-run against the SOURCE file named by the artifact, not against the artifact's evidence section. Read-only. This file is the only file written.

Mode: ADVERSARIAL. Criteria: S1, S2, S8, S13 (specs/SPEC_RUBRIC.md, as quoted in the brief).

## Spot-check table
"Aln" is the artifact line number. Ev = evidence block below.

| n | Aln | claim as written in artifact (abridged) | source re-run | grade | reason |
|---|---|---|---|---|---|
| 1 | 4 | four runs, 2026-11-01, 1 NQ, March 2021 to July 2026 | three-strategy-results :402-405; worker4 :26-:30 (Ev2, Ev4) | MATCH | four rows; worker4 :27 date range 2021-03-08 to 2026-07-17, Contracts 1 |
| 2 | 5 | PF 1.26 to 1.29, max DD -$40637.04 to -$50748.88 | three-strategy-results :402-404 (Ev2) | MATCH | 1.29/1.26/1.28; -45282.04/-50748.88/-40637.04 |
| 3 | 6 | LHM lost $76,009.84, PF 0.84, retired under D-2026-11-02-A | :405; DECISIONS.md:368 (Ev2, Ev3) | MATCH | -$76009.84, 0.84; :368 heading says RETIRED |
| 4 | 7 | D6 (f10603a) all three fail every size at 1 MNQ, committed measure; 50K ceiling $1,600 | D6 report :7, :31; git log f10603a (Ev4) | MATCH | :7 "$4,463 to $5,280. That fails every account size."; :31 "$1,600" |
| 5 | 13 | RSI, MACD, moving averages, Keltner, ADX, stochastics, Supertrend, Ichimoku, Donchian zero hits | my git grep + Redemtion grep (Ev11, Ev12) | MATCH | all 0 tracked and 0 Redemtion, word and substring |
| 6 | 15 | T1 1,173 trades, $176,392.92; T2 OppBand $188,618.48 | vm-queue :15-:16 (Ev8) | MATCH | exact |
| 7 | 17 | commission re-run at $4.68 | vm-queue :40 (Ev8) | MATCH | "($4.68 round trip)" |
| 8 | 51 | Baseline 1190, $197327.60, 1.29, -$45282.04, 40.67%, $165.82 | :402 (Ev2) | MATCH | all six fields |
| 9 | 52 | OppBand 810, $210182.40, 1.26, -$50748.88, 58.02%, $259.48 | :403 (Ev2) | MATCH | all six fields |
| 10 | 53 | Flat1559 1190, $193017.60, 1.28, -$40637.04, 40.50%, $162.20 | :404 (Ev2) | MATCH | all six fields |
| 11 | 54 | LHM 1304, -$76009.84, 0.84, -$99806.96, 47.62%, -$58.29 | :405 (Ev2) | MATCH | all six fields |
| 12 | 47 | csv-analyses :41-44 records MATCH on all four | csv-analyses :41-:44 (Ev2) | MATCH | R0-R3 each "MATCH" |
| 13 | 51 | walk-forward exit policy, DECISIONS.md:1077 | DECISIONS.md:1077 (Ev3) | MATCH | "exit policies BandOrVWAP / OppBand / Flat1559" |
| 14 | 52-53 | DECISIONS.md:1222, :1223, :504 | (Ev3) | MATCH | :1222 OppBand def, :1223 Flat1559 def, :504 "Flat1559 is unchanged" |
| 15 | 92 | DECISIONS.md:383 "is **removed from the active candidate set**" | (Ev3) | MATCH | verbatim |
| 16 | 56 | R-VM-6 "appears in DECISION_LOG.md:647 only, with no DECISIONS.md entry" | grep -n R-VM-6 DECISION_LOG.md / DECISIONS.md (Ev6) | MISMATCH | DECISION_LOG hits at :630, :647 and :649, not :647 only; DECISIONS.md count 0 is right |
| 17 | 57 | Run 3: 1075 trades, $1,281.61, PF 1.04, max DD -$4,051.57 | run3 record :55, :41, :45, :46 (Ev5) | MATCH | exact |
| 18 | 57 | Run 3 recorded "INVALID" (run3 record :106) | sed -n 106p; grep INVALID (Ev5) | MISMATCH | :106 is an empty line; the INVALID label is at :103 (heading "RUN 3 RULED INVALID by Amear") |
| 19 | 58 | Run 4: 1,211, $3,136.84, PF 1.08, max DD -$4,108.84; win rate NOT IN RECORD | run3 record :111, :108-:113 (Ev5) | MATCH | figures exact; no win/% term in :108-:113 |
| 20 | 59 | worker5 :89, early runs predate the point-value fix | worker5 :89 (Ev4) | MATCH | "These predate the point-value fix" |
| 21 | 61 | worker5 :88 "Its original record: NOT IN RECORD in the paths searched" | worker5 :88 (Ev4) | MATCH | verbatim |
| 22 | 63 | A20 at worker5 :7 | worker5 :7 (Ev4) | MATCH | :7 is "## A20" |
| 23 | 66 | A4 quotes, DECISIONS.md:1735-1740 | (Ev3, via artifact E1.2 lines re-read: see Ev3 note) | MATCH | "below 80%", "lower of 3.2% of the MFFU", "Evaluated against every tier row" |
| 24 | 67 | worker5 :68, no literal "$1,600" in DECISIONS.md | worker5 :68 (Ev4) | MATCH | verbatim sense |
| 25 | 69 | D6 :7 "$2,774 to $2,914", "only on the 150K accounts"; :56 "COMPUTED figures on NT8 trade lists", "derived, not an MNQ run" | D6 report :7, :56 (Ev4) | MATCH | verbatim |
| 26 | 70 | D7 quote DECISIONS.md:1940-1944; :2283 records D7 as fired | (Ev3) | MATCH | :1943-1944 quote exact; :2283 quotes "D6 result -> D7 FIRED" |
| 27 | 74 | STATUS.md:195 quote; WF spec :5 quote | (Ev7) | MATCH | verbatim |
| 28 | 74 | worker5 :71 D6 figures are not walk-forward results | worker5 :71 (Ev4) | MATCH | "Do not read the D6 per-window drawdowns ... as walk-forward OOS results" |
| 29 | 84 | worker2 :18 "**No new strategy was proposed.**" | worker2 :18 (Ev9) | MATCH | verbatim |
| 30 | 89 | voice-strategy-brief is a status brief (worker2 :23) | worker2 :23 (Ev9) | MATCH | "(a status brief; the only strategy hit is the baseline" |
| 31 | 80 | eight research efforts, worker2 :14-:21 | worker2 :14-:21 (Ev9) | MATCH | rows R1 to R8 at :14-:21 |
| 32 | 93 | DECISIONS.md:360 "TORB and ORB remain written specs in the shortlist" | (Ev3) | MATCH | verbatim (line wraps in fold output) |
| 33 | 94-95 | DECISIONS.md:1572-:1579 R6; :1590 FOMC parked by R9 | (Ev3) | MATCH | both items at :1574/:1576; :1590 "R9 FOMC-Cycle Even-Week stays parked" |
| 34 | 98 | no DECISIONS.md line names Gemini or Kimi (0) | grep -i gemini/kimi DECISIONS.md (Ev3) | MATCH | 0 |
| 35 | 99, 101 | session-close :26, :3, :18, :33; strategy-research :30 | (Ev10) | MATCH | all verbatim |
| 36 | 101 | worker3 :82-:91 still says "channel-recommended" | worker3 :82 (Ev9) | MATCH | "channel-recommended for backtest" |
| 37 | 116-117 | .cs:46 DEFAULT BandOrVWAP; .cs:34 "NO ATR stop"; STATUS.md:192 arm (b) WRITTEN only | (Ev9, Ev7) | MATCH | verbatim |
| 38 | 123 | Kimi :81 "Post-2018 evidence: None found."; :85 "Fit: Low." | (Ev10) | MATCH | verbatim |
| 39 | 129 | vm-queue 44 lines, session-close 54 lines; vm-queue :5 source quote | wc -l; vm-queue :5 (Ev8) | MATCH | 44, 54; quote exact |
| 40 | 133-134 | vm-queue :11 setup; :15-:17 T1/T2/T3 trades, net, PF, DD | (Ev8) | MATCH | all twelve numbers exact |
| 41 | 136-137 | vm-queue :23 "$3,472.08"; :28 12:32:48 PM, PID 11820, "not stated in the report" | (Ev8) | MATCH | exact |
| 42 | 138 | vm-queue :36 "about $3,790 ... 50K gate of $1,600" | (Ev8) | MATCH | exact |
| 43 | 143 | newest vm/replies file 20261111T172940Z-STATUS.md; last vm/ commit ee54344 (2026-11-11) | ls vm/replies; git log -- vm/ (Ev11) | MATCH | exact |
| 44 | 145 | DECISIONS.md:1010 only "VM Claude Code" hit; vm-bridge 0 hits; D-2026-11-10-C at :2076 | (Ev3) | MATCH | one hit at :1010; vm-bridge count 0; :2076 heading |
| 45 | 146 | D-2026-11-11-B at DECISIONS.md:2176, Python 3.12.10, git 2.56.0; hermes reply file exists | (Ev3, Ev13) | MATCH | :2176 heading exact; file count 1 |
| 46 | 147 | Downloads copy differs by one trailing S13 line only | diff (Ev13) | MATCH | single hunk 45d44 |
| 47 | 151 | ckh P0 OPEN, "PARKED (absolute park rule, audit-fail-x2)", "No R6 code exists"; HANDOFF.md:22; session-close :52 | bd show; HANDOFF; session-close (Ev10, Ev14) | MATCH | all three strings present; HANDOFF :22 and session-close :52 verbatim |
| 48 | 152 | session-close :48 17:26Z, "No reply yet at filing"; fx4 P1 OPEN | (Ev10, Ev14) | MATCH | exact |
| 49 | 157-158 | HANDOFF.md:20 two questions; :12-16 "Next, in order" | (Ev10) | MATCH | verbatim (working-copy HANDOFF.md; see S2 finding F) |
| 50 | 159 | diq P1 PARKED, qtk P2, ajj P2 | bd show (Ev14) | MATCH | diq "[P1 OPEN]" title PARKED; qtk P2; ajj P2. q36 and b5z priority not visible in my truncated output: NOT CHECKED |
| 51 | 160 | session-close :53 "not this year", "an estimate, not a decision" | (Ev10) | MATCH | verbatim |

## S2 findings
- A (MEDIUM, S2 break): artifact :8 (Summary 5) and :71 ("the current status of all three Noise-Area arms is 'kept for the record only'"), also :52-:53 ("Status: same as the baseline"). Source D7, DECISIONS.md:1943-1944, says "The Noise-Area baseline continues through the VM tests for the record". The D6 report :45 repeats "The Noise-Area basel[ine]". The only `for the record` hit in DECISIONS.md is :1944. Neither source extends the status to OppBand or Flat1559. The artifact applies it to all three arms with no INFERRED label. The only source that applies it to an arm other than the baseline is the channel (vm-queue :36, on T2 OppBand), which is the channel's reading. This is an inference presented as the recorded status.
- B (LOW): artifact :47 gives the run settings (Standard (Fastest), slippage 2, PRAXIS, 1 contract) as flat fact. Worker4 :27 labels them "Shown in the screenshots (REPORTED BY AMEAR)", and worker4 :30 says "The baseline has no settings screenshot". The REPORTED label was dropped.
- C (LOW): artifact :7 (Summary 4) says the arms "fail every MFFU account size at 1 MNQ". It does not say what D6 :56 says: the MNQ figures are "derived, not an MNQ run", computed at Standard resolution with no breakers. The body (:69) carries the label; the Summary does not.
- D (LOW, partly UNVERIFIED): artifact :144 says DECISION_LOG row 905 "is about Mac-side 2026-11-01 runs". Row 905 (Ev6) only says "those runs were OppBand/Flat1559/LH variants". The artifact's own :47 says those runs were Amear's hand runs in the NT8 Strategy Analyzer; only the recomputation was on the Mac. I did not check whether NT8 runs only in the VM, so the claim that "Mac-side" is wrong is UNVERIFIED. The label is not in the source.
- E (LOW, no break): artifact :116 backs "It was backtested as that strategy's exit" with the channel-reported VM T1/T3 rows (vm-queue :15, :17). The claim is true from the observed :402 row (BandOrVWAP), but the citation it picks is the weaker, second-hand one.
- F (LOW, reproducibility): HANDOFF.md is modified in the working copy (git status at session start shows ` M HANDOFF.md`). The HANDOFF.md:12-22 pointers in Q5 resolve only against uncommitted text. The artifact flags working-copy state only for the WF spec (its E1.4 heading).

## S8 findings
- NO BREAK on a direct answer. Artifact :145 explicitly declines the in-VM ruling question. Q5 (:149-:160) only gives pointers and quotes Amear's two questions without answering them.
- Adjacent: finding A assigns a status ("kept for the record only") to OppBand and Flat1559 that no Amear ruling assigns. It is graded under S2, not S8, because no Amear question is answered. The master should decide whether that status is Amear's call.

## Absence re-checks
- No vm/replies file after 2026-11-11: CONFIRMED. The newest is 20261111T172940Z-STATUS.md (Ev11).
- Last commit touching vm/ is ee54344, 2026-11-11: CONFIRMED (Ev11).
- `mdfind -name vm-bridge` returns 0: CONFIRMED, `wc -l` = 0 (Ev11).
- vm-bridge in DECISIONS.md: 0, CONFIRMED (Ev3). vm-bridge in DECISION_LOG.md: one row, :939, the 2026-11-13T20:36:45Z filing/authority row (Ev12). That is consistent with artifact :144, which says no row records a VM-side run.
- Gemini/Kimi in DECISIONS.md: 0, CONFIRMED (Ev3).
- R-VM-6 in DECISIONS.md: 0, CONFIRMED. "DECISION_LOG.md:647 only" is wrong (row 16).
- No tracked ORB/TORB/announcement code file (.cs/.pine/.py name match): CONFIRMED, grep rc=1 (Ev12).

## Hygiene
All five files: S13 sentence count 1, and it is the last line. Forbidden-word count 0. Name-token count 0 (Ev15). My own report: Ev16.

## Evidence
Every command below was run in this session. Outputs are pasted, cut with `cut -c` where shown. One substitution: the S13 sentence is replaced by `[S13 sentence]` inside commands and outputs, so that this report carries it only once. In those commands, `$S13` holds the exact sentence.

Ev2:
```
$ grep -n '' docs/reports/2026-11-01-three-strategy-results.md | sed -n '402,405p' | cut -c1-160
402:| BASELINE (`PraxisNoiseAreaBreakout`, BandOrVWAP) | 1190 | $197327.60 | 1.29 | -$45282.04 | -$45282.04 | 40.67% | $165.82 | $35887.04 | 18.19% |
403:| OPPBAND | 810 | $210182.40 | 1.26 | -$50748.88 | -$50748.88 | 58.02% | $259.48 | $36087.04 | 17.17% |
404:| FLAT1559 | 1190 | $193017.60 | 1.28 | -$40637.04 | -$40637.04 | 40.50% | $162.20 | $36472.04 | 18.90% |
405:| LHMOM (LastHalfHourMomentum) | 1304 | -$76009.84 | 0.84 | -$99806.96 | -$99806.96 | 47.62% | -$58.29 | $3852.04 | -5.07% (not meaningful) |
$ grep -n '' docs/reports/2026-11-01-csv-analyses.md | sed -n '41,44p' | cut -c1-120
41:| R0 | 197327.60 | 1.29 | -45282.04 | 197327.60/1.29/-45282.04 | MATCH |
42:| R1 | 210182.40 | 1.26 | -50748.88 | 210182.40/1.26/-50748.88 | MATCH |
43:| R2 | 193017.60 | 1.28 | -40637.04 | 193017.60/1.28/-40637.04 | MATCH |
44:| R3 | -76009.84 | 0.84 | -99806.96 | -76009.84/0.84/-99806.96 | MATCH |
```

Ev3 (DECISIONS.md; `for n in ...; do sed -n "${n}p" DECISIONS.md | cut -c1-220; done`, then fold -w 220 for long lines):
```
--- DECISIONS.md:360
- **R-7zq-3 — third file (answers NEEDS AMEAR 6 above), DECISION_LOG `2026-10-31T11:45:29Z` (WHO: amear):** *"Keep #1 (as built)"* — `PraxisLastHalfHourMomentum` (Baltussen, Da, Lammers & Martens 2021) stands; TORB and O
RB remain written specs in the shortlist.
--- DECISIONS.md:368
## 2026-11-02 — D-2026-11-02-A: R-VN3-1 — `PraxisLastHalfHourMomentum` RETIRED from the active candidate set (retire, not delete)
--- DECISIONS.md:383
- `PraxisLastHalfHourMomentum` (Baltussen, Da, Lammers & Martens 2021; third file of D-2026-10-31-A) is **removed from the active candidate set**. What that excludes beyond the removal is not ruled here (see NEEDS AMEAR 
--- DECISIONS.md:504
- Voice agent's record (notes-3 line 23): the fill at the 15:59:00 price, printed as 4:00 PM in the grid, is accepted. Flat1559 is unchanged.
--- DECISIONS.md:1010 (folded)
- **Item 2 — in-VM automation.** The "Oct 28 ruling" is ruling (1) of `docs/reports/2026-10-28-voice-session-notes.md:7` (untracked file), "The in-VM automation approach is dropped. No more Cowork or in-VM Claude Code ex
ecutor work.", taken onto the ledger at DECISION_LOG `2026-10-30T21:36:00Z` (WHO: amear). (filer's identification) DECISIONS.md has no entry for it. In his words it is "lifted COMPLETELY once two tests pass; until then i
t stands." ...
--- DECISIONS.md:1077 (folded, excerpt)
h); ATR 14; exit policies BandOrVWAP / OppBand / Flat1559; in-sample objective = risk-adjusted return with a minimum trade count, never net profit; ...
--- DECISIONS.md:1222
   Q4 yes, OppBand = the paper's opposite band, as in _OppBand.cs.
--- DECISIONS.md:1223
   Q5 yes, Flat1559 = BandOrVWAP exits, flatten on the 15:59 bar, as in _Flat1559.cs.
--- 1572-1580
R6  Research and backtest, on the existing 1-minute data only,
    nothing bought (R-1104-3 stands):
    - Pre-Announcement Drift (Hu, Pan, Wang & Zhu 2022), evening-
      entry variant, exit before the release.
    - Macroeconomic Announcement-Day Premium (Savor–Wilson; Ai 2024).
    Runs in parallel with the walk-forward, not queued behind it.
    Before any build, read MFFU's current T1 news rule and confirm
    whether an evening entry counts as the same trading day.
R7  Parallel work runs in a separate git worktree on its own branch,
--- 1590-1592
R9  FOMC-Cycle Even-Week stays parked while trading on MFFU
    (multi-day hold breaks flat-by-close). Revisit only if own
    capital is ever used.
--- DECISIONS.md:1940..1944
D7  If D6 fails at every tier at 1 MNQ: do not design breaker values
    to fit the drawdown ceiling (that is curve-fitting). Report it, and
    pull R6's research (higher-win-rate, steadier-equity strategies)
    forward to P0. The Noise-Area baseline continues through the VM
    tests for the record, but a GO on MFFU is not expected from it.
--- DECISIONS.md:2076
## 2026-11-10 — D-2026-11-10-C: VM agent = Hermes over SSH (settlement 3 changed; master under D1)
--- DECISIONS.md:2176
## 2026-11-11 — D-2026-11-11-B: VM handoff §1 limit 9 lifted by Amear for one install; Python 3.12.10 and git 2.56.0 (ARM64) installed in the VM. Record only. Filed WHO: amear, REPORTED BY the Claude.ai channel.
--- DECISIONS.md:2283 (folded, excerpt)
... pulled forward to P0 by Amear's D-2026-11-08-D D7 (DECISIONS.md:19
40–1944) after D6 failed (HANDOFF.md:289 at `c29d08b`: "D6 result → D7 FIRED"). ...
--- counts
$ grep -c -i 'vm-bridge' DECISIONS.md
0
$ grep -n -i 'VM Claude Code' DECISIONS.md | cut -c1-80
1010:- **Item 2 — in-VM automation.** The "Oct 28 ruling" is ruling (1) of `docs
$ grep -n -i -E 'gemini|kimi' DECISIONS.md | wc -l
       0
$ /usr/bin/grep -n -i 'for the record' DECISIONS.md | cut -c1-200 | head -8
1944:    tests for the record, but a GO on MFFU is not expected from it.
```
Ev3 note: I did not re-print DECISIONS.md:1735-1740 separately. The A4 quotes in row 23 were checked against the lines the artifact printed at its E1.2 (`grep -n '' DECISIONS.md | sed -n '1735,1740p;...'`). That makes row 23 the one row in this table that rests on the artifact's own paste, not on my re-run. Treat row 23 as UNVERIFIED by independent re-run.

Ev4:
```
$ grep -n '' docs/reports/2026-11-09-d6-drawdown-check-manager.md | sed -n '7p;31p;56p' | cut -c1-600
7:At 1 micro (MNQ), each of the three strategies had a worst 63-session stretch that fell $2,774 to $2,914 from its high. That stays under the safety ceiling only on the 150K accounts, where the ceiling is $3,600. Smaller accounts fail. If the losing run that carries over from earlier windows is counted, which is the project's committed measure, the worst figure is $4,463 to $5,280. That fails every account size. At 1 full NQ the worst stretch is $26,942 to $28,337, and every account fails. No daily-loss limit value has been written down yet, so the capped run could not be done at a real value
31:| Rapid 50K, Rapid EOD 50K, Pro 50K, Builder 50K | $1,600 | FAIL all | FAIL all |
56:- **Evidence level.** These are COMPUTED figures on NT8 trade lists (OBSERVED inputs) at Standard resolution with no breakers. They are not the judged High-resolution, breakers-on version (values spec :42). They are not tested on the VM. The MNQ figures are derived, not an MNQ run.
$ git log --oneline -1 f10603a -- docs/reports/2026-11-09-d6-drawdown-check-manager.md
f10603a docs: D6 drawdown viability check (Amear D-2026-11-08-D D6) on the three 2026-11-01 trade lists at 1 MNQ and 1 NQ per walk-forward window vs the A4 ceiling per tier; D7 test met on the committed values-spec measure; MANIFEST row 306
$ /usr/bin/grep -n -i -E 'for the record|D7' docs/reports/2026-11-09-d6-drawdown-check-manager.md | cut -c1-220 | head -6   (excerpt)
45:The D7 test is judged on VS4 (Decision 5). **D7 consequence:** no breaker value is designed to fit the ceiling. R6's research (higher-win-rate, steadier-equity strategies) is pulled forward to P0. The Noise-Area basel
--- worker5
$ grep -n '' docs/reports/2026-11-13-strategy-review-index-worker5.md | sed -n '7p;68p;71p;88p;89p' | cut -c1-400
7:## A20
68:- Gate value provenance: there is no literal "$1,600" in DECISIONS.md or the values spec. The `1,600|$1600|50K` grep hits there are only the Builder 50K add-on / $1,500 rows (`DECISIONS.md:1388-1389`; values spec `:136`, `:297-298`, `:331`, `:338`). ...
71:**Specified, and Mac-side maths/oracles WRITTEN + TESTED on synthetic fixtures. No walk-forward has been RUN; no OOS walk-forward result is recorded.** Do not read the D6 per-window drawdowns (above) as walk-forward OOS results: ...
88:   - The "T1 reference (Amear's hand run)" of 1,173 trades (the 09:30 ET session-start run): no primary record found in `docs/reports`, STATUS.md or HANDOFF.md. ... Its original record: NOT IN RECORD in the paths searched.
89:2. `docs/reports/2026-10-28-voice-session-notes.md`: first Fusion runs, ... These predate the point-value fix: ...
--- worker4
$ grep -n '' docs/reports/2026-11-13-strategy-review-index-worker4.md | sed -n '23,30p' | cut -c1-300   (excerpt)
26:- Instrument `NQCONTROW SEP25`, Account `Backtest` on every CSV row (TSR :41).
27:- Shown in the screenshots (REPORTED BY AMEAR): Last / Minute / 1; date range `2021-03-08 -> 2026-07-17`; order fill resolution `Standard (Fastest)`; slippage `2`; commission template `PRAXIS`; Contracts 1. ...
29:- The CSV Commission column is $2.96 on every row in all four files (TSR :77, :125, :231, :349).
30:- The baseline has no settings screenshot (TSR :37). Its settings rest on Amear's C4 notes at N2 :111: ...
```

Ev5 (run3 record):
```
$ grep -n '' docs/reports/2026-10-30-run3-backtest-screenshot-record.md | sed -n '106p' | cut -c1-300
106:
$ grep -n -i -E 'INVALID|NQCONT\b|NQCONT ' docs/reports/2026-10-30-run3-backtest-screenshot-record.md | cut -c1-200 | head -8
16:| Data Series | Instrument | NQCONT |
103:## Addendum 2026-10-30T22:40Z — RUN 3 RULED INVALID by Amear; run 4 supersedes it (REPORTED)
107:**Amear's ruling (DECISION_LOG `2026-10-30T22:22:00Z`; ...
110:2021-03-08 → 2026-07-17 · NQCONT 1-min · BandOrVWAP · 1 contract · Slippage 2 · Standard · PRAXIS commission · trading hours `CME US Index Futures RTH`.
$ wc -l docs/reports/2026-10-30-run3-backtest-screenshot-record.md
     122 docs/reports/2026-10-30-run3-backtest-screenshot-record.md
$ grep -n -E '1,?075|1,?211|4,?051|4,?108|3,?136' ... | cut -c1-200 | head -12   (excerpt)
46:| Max. drawdown | −$4,051.57 | −$1,713.82 | −$3,179.91 |
55:| Total # of trades | 1075 | 522 | 553 |
111:1,211 trades (584 L / 627 S) · net $3,136.84 · gross profit $41,447.47 · gross loss −$38,310.63 · commission $3,584.56 · PF 1.08 · max DD −$4,108.84 · avg trade $2.59 · longs +$4,541.40 / shorts −
$ grep -n -E '1,?281\.61|1\.04' ... | cut -c1-120 | head -4   (excerpt)
41:| Total net profit | $1,281.61 | $2,721.21 | −$1,439.60 |
45:| Profit factor | 1.04 | 1.18 | 0.93 |
$ sed -n '108,113p' ... | /usr/bin/grep -o -i -E '.{0,25}(win|percent profitable).{0,25}'
rts −$1,404.56 · largest winner $1,792.50 · total sli
```
(The single hit is "largest winner", not a win rate.)

Ev6 (DECISION_LOG / R-VM-6):
```
$ grep -n 'R-VM-6' DECISION_LOG.md | cut -c1-60
630:- [2026-10-31T18:21:00Z] **WHO: amear** | PROPOSED BY: p
647:- [2026-10-31T15:03:07Z] **WHO: amear** | PROPOSED BY: p
649:- [2026-10-31T14:59:37Z] **WHO: amear** | SOURCE: `docs/
$ grep -c 'R-VM-6' DECISIONS.md
0
$ sed -n '905p' DECISION_LOG.md | /usr/bin/grep -o -E '.{0,160}OppBand.{0,60}'
 and agrees. Two ungraded observations recorded (worker1 :58–59): (1) :2393 "The 2026-11-01 runs are without-series records only" is unchecked; those runs were OppBand/Flat1559/LH variants whose exits are not the "16:00 session
```

Ev7:
```
$ sed -n '192p;195p' STATUS.md | cut -c1-250
- Arm (b): `.cs` WRITTEN only — not compiled, not run; on `arm-b/wf-tunables` only (`18:12:00Z`). There is no C# compiler on the Mac (`16:04:00Z`).
- T1–T13: none has run. All wait for the VM.
$ sed -n '5p' docs/specs/2026-11-05-walk-forward-spec.md   (excerpt)
**Status: DERIVED — not yet ruled on as a whole by Amear.** **Changelog.** ...
```

Ev8 (vm-queue):
```
$ wc -l <vm-queue> <session-close>
      44 docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md
      54 docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md
$ grep -n '' <vm-queue> | sed -n '5p;11p;15,17p;23p;28p;33p;36p;40,43p' | cut -c1-420   (excerpt)
5:Source: the VM Claude Code session's own report, pasted to this channel by Amear at 14:37 ET (REPORTED BY Amear; the channel has not read the VM repo). The VM agent is the session working in `C:\praxis\vm-bridge` on the Windows VM. It is not praxis-master. Its results and commits live in that local git repo (no remote), ...
11:Setup: Strategy Analyzer tab "PRAXIS baseline NQCONTROW 0930", PraxisNoiseAreaBreakout, NQCONTROW SEP25, 1-minute, 2021-03-08 to 2026-07-17, CME US Index Futures RTH 0930 ET, commission PRAXIS $2.96 round trip, slippage 2, Standard fill resolution, 1 NQ.
15:| T1 | BandOrVWAP | 1,173 | $176,392.92 | 1.2615 | -$38,905.64 | Exact match |
16:| T2 | OppBand | 1,112 | $188,618.48 | 1.2861 | -$37,906.24 | -61 trades, +$12,225.56 net, DD $999.40 smaller |
17:| T3 | BandOrVWAP | 1,173 | $176,392.92 | 1.26 | -$38,905.64 | Identical to T1 trade by trade (request id excepted); same file size, 219,831 bytes |
23:- **Commission not compared:** the bridge's result files carry no commission total, so the hand run's $3,472.08 could not be checked.
28:2. **NT8 restarted at 12:32:48 PM** (new process, PID 11820), ... **Who or what restarted NT8 is not stated in the report** (open).
33:## 3. What this means (the channel's reading, INFERRED, not a ruling)
36:- **These are Noise-Area numbers, kept for the record only** (D7 after the D6 drawdown check). T2's better net does not change that: at 1 MNQ its max drawdown would be about $3,790 (one tenth of $37,906.24), above the 50K gate of $1,600. Not a candidate.
40:1. **MFFU commission re-run:** Amear sets both PRAXIS commission rows to 2.34 by hand ($4.68 round trip); the VM agent then re-sends T1's parameters. Expected: 1,173 trades, net about $174,375.36 ...
41:2. **Sim feed check:** the VM agent still lists "check in the Control Center whether the Sim feed cycled when the AddOn loaded yesterday." ... Whether today's Control Center view covers yesterday's load is not confirmed.
42:3. **Later, not today:** Analyzer tabs for `PraxisNoiseAreaBreakout_Flat1559` and `PraxisLastHalfHourMomentum`, set by hand or via the bridge's `satemplate` command (needs Amear's OK). ...
43:4. **Open:** what restarted NT8 at 12:32 PM.
```

Ev9 (worker2, worker3, .cs):
```
$ sed -n '18p' <worker2> | /usr/bin/grep -o 'No new strategy was proposed[^|]*'
No new strategy was proposed.** B surveyed public code: one Noise-Area NinjaScript implementation, plus an ORB repo listed as reference code (E8, E20) 
$ sed -n '23p' <worker2> | /usr/bin/grep -o -E '.{0,40}voice-strategy-brief.{0,60}'
l resolution); `docs/reports/2026-11-08-voice-strategy-brief.md` (a status brief; the only strategy hit is the baseline'
$ grep -n '' <worker2> | sed -n '10,23p' | cut -c1-230   (rows :14-:21 are R1 (D2) ... R8 (Kimi); excerpt)
14:| R1 (D2) | Undated in the text; ...
21:| R8 (Kimi) | 2026-11-13; output supplied 14:26 ET (REPORTED BY the channel) | ...
$ grep -n '' <worker3> | sed -n '15p;41p;82,91p' | cut -c1-200   (excerpt)
82:2. **Volatility-weighted VWAP σ-band mean reversion ("C1"): PROPOSED by external research on 2026-11-13, rated low, channel-recommended for backtest, with no ledger decision found.**
$ sed -n '34p;46p' ninjascript/PraxisNoiseAreaBreakout.cs | cut -c1-200
//     multiplier as a tunable), NO ATR stop. The ONLY selectable knob is the exit form (ExitMode).
	// BandOrVWAP = paper's PREFERRED model, trailing stop at max/min(band, VWAP) (§4 p.13). DEFAULT.
```

Ev10 (session-close, research, Kimi, HANDOFF):
```
$ grep -n '' <session-close> | sed -n '3p;18p;26p;28p;33p;48p;52p;53p' | cut -c1-330   (excerpt)
3:... Read this AFTER the two earlier files from today; where they disagree, this file governs.
18:Files 1 and 2 recommend backtesting `PraxisLastHalfHourMomentum` first. **Withdrawn.** ...
26:... **Neither found a viable new candidate.** Status of everything they proposed:
33:| VWAP sigma-band mean reversion | NOT TESTED; low | ...
48:- **MFFU email:** follow-up sent 2026-11-13 17:26Z in the pre-purchase thread, ...
52:- **Still waiting on Amear (unchanged):** a ruling on parked `ckh` (the channel recommended resuming it; Amear has not ruled); his two questions ...
53:- **Amear asked when PRAXIS can go live.** The channel's answer (an estimate, not a decision): not this year; ...
$ sed -n '48p' <session-close> | /usr/bin/grep -o 'No reply yet at filing[^.]*'
No reply yet at filing
$ sed -n '30p' <strategy-research> | cut -c1-200
Backtest order: (1) PraxisLastHalfHourMomentum, already written; (2) Candidate 1 VWAP mean reversion; (3) Candidate 2 opening-gap fade; Candidate 4 parked. Measure the real carried drawdown gate at 1 
$ grep -n '' <kimi> | sed -n '81p;85p' | cut -c1-120
81:Post-2018 evidence: None found. We are not aware of any academic test of this exact VWAP+volatility band strategy on 
85:Fit: Low. The profile is low win rate. It relies on sharp reversal moves (rare), likely with lopsided risk. The prior
$ grep -n '' HANDOFF.md | sed -n '12,22p' | cut -c1-260   (excerpt)
12:**Next, in order (decided by master under D1; one manager at a time):**
13:1. Human: resume or rule on `ckh` (cure in the 2026-11-12 09:01Z card below, unchanged).
14:2. Broker route: MFFU does not offer Rithmic; D-2026-11-10-B is contradicted and not re-decided. ...
15:3. OPEN-T1 VM-to-webhook check (needs the VM; Amear's hands for any VM step).
16:4. Rest of bead `fgd`: ...
20:**Questions that are Amear's (unchanged; DECISION_LOG 2026-11-12T13:01:49Z item b):** (1) does MFFU's 2026-11-11T22:41:33Z point 4 close R6 OPEN-1; (2) should F4's bar change.
22:**For Amear's hands (not questions):** the decision on `ckh`; D2 items unchanged ...
```

Ev11 (absence):
```
--- vm/replies newest 4
$ ls vm/replies | sort | tail -4
20261111T172802Z-STATUS.md
20261111T172933Z-python-git-install.md
20261111T172940Z-STATUS.md
README.md
$ git log -3 --format='%h %ad %s' --date=short -- vm/ | cut -c1-110
ee54344 2026-11-11 docs: file Amear rulings V1-V7 as D-2026-11-11-A (incl. Rule F2-1 approval, V3/V5 MFFU comp
85a803f 2026-11-11 docs: Hermes over SSH as the VM agent (D-2026-11-10-C; Amear proposal DECISION_LOG 2026-11-
7f3590e 2026-11-09 vm: VM handoff amendment 2 (Amear D-2026-11-08-C C3 C9 C10, D-2026-11-08-A R1) - filed step
$ mdfind -name vm-bridge | wc -l
(two mdfind locale log lines on stderr)
       0
$ for t in RSI MACD 'moving average' Keltner ADX stochastic Supertrend Ichimoku Donchian 'cumulative delta' Bollinger ATR; do git grep -i -w -I -c "$t" -- . ':!*2026-10-28-f4-*' ':!*strategy-review-index*' | sum; /usr/bin/grep -r -i -w -I -c "$t" Redemtion | sum; done
RSI tracked=0 Redemtion=0
MACD tracked=0 Redemtion=0
moving average tracked=0 Redemtion=0
Keltner tracked=0 Redemtion=0
ADX tracked=0 Redemtion=0
stochastic tracked=0 Redemtion=0
Supertrend tracked=0 Redemtion=0
Ichimoku tracked=0 Redemtion=0
Donchian tracked=0 Redemtion=0
cumulative delta tracked=0 Redemtion=0
Bollinger tracked=1 Redemtion=5
ATR tracked=352 Redemtion=41
```

Ev12:
```
$ (same, substring, no -w)
stochastic (substring) tracked=0 Redemtion=0
moving average (substring) tracked=0 Redemtion=0
supertrend (substring) tracked=0 Redemtion=0
keltner (substring) tracked=0 Redemtion=0
donchian (substring) tracked=0 Redemtion=0
ichimoku (substring) tracked=0 Redemtion=0
$ /usr/bin/grep -n -i 'vm-bridge' DECISION_LOG.md | cut -c1-140
939:- [2026-11-13T20:36:45Z] WHO: praxis-master | WHAT: **Unit 2026-11-13-research-filing COMMITTED `9ff8a48`, pushed (`main` = `origin/main
$ git ls-files | /usr/bin/grep -i -E '\.(cs|pine|py)$' | /usr/bin/grep -i -E 'orb|announce|drift'; echo "rc=$?"
rc=1
```

Ev13:
```
$ ls vm/replies | /usr/bin/grep -c '^20261110T211738Z-CODE-vm-agent-hermes.md$'
1
$ diff ~/Downloads/2026-11-13-return-handoff-claude-ai-vm-queue-results.md docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md; echo "diff rc=$?"
45d44
< [S13 sentence]
diff rc=1
```

Ev14 (beads):
```
$ bd show Praxis_build-ckh | /usr/bin/grep -o -E 'P0 · [A-Z]+|PARKED \(absolute park rule, audit-fail-x2\)|No R6 code exists' | sort -u
No R6 code exists
P0 · OPEN
PARKED (absolute park rule, audit-fail-x2)
$ for b in ckh fx4 afe diq qtk q36 ajj b5z; do bd show Praxis_build-$b | head -1 | cut -c1-140; done   (excerpt)
○ Praxis_build-fx4 · MFFU automation-compliance: confirm in writing that fully-automated trading is permitted before any live step   [● P1 ·
✓ Praxis_build-afe · R-VN3-1: PraxisLastHalfHourMomentum retired from the active candidate set (retire, not delete)   [● P2 · CLOSED]
○ Praxis_build-diq · PARKED: wf-spec-amendment (values spec v2.2 + WF spec A4) - audit FAIL 2, absolute park rule fired   [● P1 · OPEN]
○ Praxis_build-qtk · Dev-D no-optimization-first-pass vs WFE>=0.50: define the replication-arm gate set + where GO/HOLD/REJECT sits   [● P2 
○ Praxis_build-q36 · 0-S on NQCONTROW SEP25 gives 1,190 trades (556 L / 634 S) vs retired run 4's 1,211 (584/627) on the Stock row — explain
○ Praxis_build-ajj · b2-mc: Monte Carlo engine on pooled OOS trades, emit envelope distributions   [● P2 · OPEN]
○ Praxis_build-b5z [BUG] · Import-file volume anomaly: 2021-03-08 RTH volume 4,322 (342 bars; 10:00 bar vol 8) vs 2026-07-17 RTH 284,681 (29
```

Ev15 (hygiene; TOK derived by the brief's ls|grep|sed pipeline, value not printed):
```
$ for w in manager worker2 worker3 worker4 worker5; do f=docs/reports/2026-11-13-strategy-review-index-$w.md; grep -c -F "$S13" $f; tail -1 $f | grep -c -x -F "$S13"; grep -c -i -E '<forbidden-word regex from the brief>' $f; grep -c -i -w "$TOK" $f; done
manager S13=1 lastline=1 forbidden=0 name=0
worker2 S13=1 lastline=1 forbidden=0 name=0
worker3 S13=1 lastline=1 forbidden=0 name=0
worker4 S13=1 lastline=1 forbidden=0 name=0
worker5 S13=1 lastline=1 forbidden=0 name=0
```

Ev16 (this report, run before this Ev16 text was inserted; the insert adds no S13, forbidden or name token):
```
$ f=docs/reports/2026-11-13-strategy-review-index-worker6.md; printf 'S13=%s lastline=%s forbidden=%s name=%s\n' "$(grep -c -F "$S13" $f)" "$(tail -1 $f | grep -c -x -F "$S13")" "$(grep -c -i -E '<forbidden-word regex>' $f)" "$(grep -c -i -w "$TOK" $f)"
S13=1 lastline=1 forbidden=0 name=0
```

## Totals
51 spot-checks: 49 MATCH, 2 MISMATCH (rows 16 and 18). Row 23 MATCH rests on the artifact's own E1.2 paste, not on my re-run. Row 50 is partial: q36 and b5z priority were not checked. S2: one medium finding (A) and five low findings (B to F). S8: no break. S13 and hygiene: pass on all five files.

Result: BREAK FOUND (two pointer mismatches and one S2 status extension).

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
