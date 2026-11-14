# 2026-11-13 strategy-review-index — worker7 (round 2, ADVERSARIAL)

## Task
Unit 2026-11-13-strategy-review-index, round 2 adversary, read-only. Working dir /Volumes/Sensidine/Praxis.build, main, HEAD 9ff8a48. Artifact: `docs/reports/2026-11-13-strategy-review-index-manager.md` (587 lines). Criteria: S1, S2, S8 (specs/SPEC_RUBRIC.md). Mode: ADVERSARIAL. Job: (1) re-check the 8 round-1 fixes; (2) 12+ fresh spot-checks across Q1-Q5 and the Summary; (3) scan the Summary for S2/S8 overreach; (4) hygiene on the artifact and `-worker1.md`. Nothing edited, nothing staged. All commands were run through `/bin/bash` scripts in the session scratchpad (zsh `grep` is ugrep), with output piped through `sed 's/[Vv]erdict/[V]/g'`.

## Fix re-check table
| item | corrected text in artifact | source re-run | grade |
|---|---|---|---|
| MISMATCH 1 | :56 "(:630, :647, :649)" | `DECISION_LOG.md` R-VM-6 lines = 630 647 649; DECISIONS.md count 0 | FIXED |
| MISMATCH 2 | :57 "run3 record :103 ... and :107" | run3 record :103 = "## Addendum ... RUN 3 RULED INVALID by Amear"; :107 = Amear's ruling paragraph; :102, :104, :106 blank | FIXED |
| S2-A | Summary :8, Q1 :52, :53, :71 say DECISIONS.md does not state OppBand/Flat1559 status; extension is the channel's (vm-queue :36) | DECISIONS.md:1943-1944 and :1981 and D6 report :45 name only "The Noise-Area baseline"; DECISIONS.md:389 (filer's reading) puts both variants and baseline outside D-2026-11-02-A only; no `OppBand|Flat1559 ... for the record` line | FIXED |
| S2-B | Q1 :47 "shown in the screenshots, REPORTED BY AMEAR, and the baseline has no settings screenshot" | worker4 :27 "Shown in the screenshots (REPORTED BY AMEAR)"; :30 "The baseline has no settings screenshot (TSR :37)" | FIXED in Q1 (residue in Summary line 1, see Summary scan F1) |
| S2-C | Summary :7 "(MNQ derived from the NQ trade lists, not an MNQ run)" | D6 report :56 "The MNQ figures are derived, not an MNQ run." | FIXED |
| S2-D | Q4 :144 "is about the 2026-11-01 hand runs, not a VM-side run" | DECISION_LOG.md:905 "...those runs were OppBand/Flat1559/LH variants..." (2026-11-01 runs) | FIXED |
| S2-E | Q3 :116 cites "three-strategy-results :402, E1.1" before the VM rows | E1.1 :402 "BASELINE (`PraxisNoiseAreaBreakout`, BandOrVWAP)" | FIXED |
| S2-F | :151, :157, :158 each say "(working copy)"; :228 HANDOFF.md:289 is pinned "at `c29d08b`" | `git diff --quiet HEAD -- HANDOFF.md` exit=1; HEAD lines 12-16 differ from working-copy 12-16 (HEAD :13 "Next, in order", :14 "OPEN-A1 cure") | FIXED |

## Spot-check table (not in the round-1 list)
| # | section | artifact claim | source re-run | grade |
|---|---|---|---|---|
| 1 | Q1 :52 | walk-forward exit policy at DECISIONS.md:1077 | :1077 "...exit policies BandOrVWAP / OppBand / Flat1559..." | MATCH |
| 2 | Q1 :53 | Flat1559 fill accepted at :504 | DECISIONS.md:504 "...the fill at the 15:59:00 price ... is accepted" | MATCH |
| 3 | Q1 :52-:53 | definitions at :1222 / :1223 | :1222 "Q4 yes, OppBand = the paper's opposite band"; :1223 "Q5 yes, Flat1559 = BandOrVWAP exits, flatten on the 15:59 bar" | MATCH |
| 4 | Q1 :58 | Run 4: 1,211, $3,136.84, PF 1.08, DD −$4,108.84; win rate NOT IN RECORD | run3 record :111 has all four figures; its only "win" token is "winner $1,792.50" | MATCH |
| 5 | Q1 :59 | worker5 :89 point-value note | worker5 :89 "These predate the point-value fix ... '$1 point value'" | MATCH |
| 6 | Q1 :61 | worker5 :88 "NOT IN RECORD in the paths searched" for the 1,173 hand run | worker5 :88 "no primary record found in `docs/reports`, STATUS.md or HANDOFF.md" | MATCH |
| 7 | Q1 :67 | worker5 :68 no literal "$1,600" in DECISIONS.md | worker5 :68 "there is no literal "$1,600" in DECISIONS.md or the values spec" | MATCH |
| 8 | Q2 :80 | eight efforts at worker2 :14-:21 | worker2 :14-:21 rows R1 to R8 | MATCH |
| 9 | Q2 :84 | worker2 :18 "**No new strategy was proposed.**" | exact string on worker2 :18 | MATCH |
| 10 | Q2 :95 | FOMC even-week parked by R9, DECISIONS.md:1590 | :1590 "R9  FOMC-Cycle Even-Week stays parked while trading on MFFU" | MATCH |
| 11 | Q2 :99 | session-close :26 "**Neither found a viable new candidate.**" | exact string on session-close :26 | MATCH |
| 12 | Q3 :117 | `.cs:34` "NO ATR stop"; STATUS.md:192 "WRITTEN only" | .cs:34 and STATUS.md:192 lines as quoted | MATCH |
| 13 | Q3 :123 | Kimi :85 "Fit: Low." | Kimi :85 starts "Fit: Low." | MATCH |
| 14 | Q2 :101 | worker3 :82-:91 says "channel-recommended" | worker3 :82 "...rated low, channel-recommended for backtest..." | MATCH |
| 15 | Q4 :129 | vm-queue 44 lines, session-close 54 lines | `wc -l` 44 and 54 | MATCH |
| 16 | Q4 :145 | D-2026-11-10-C at DECISIONS.md:2076 "VM agent = Hermes over SSH" | :2076 heading as quoted | MATCH |
| 17 | Q4 :146 | D-2026-11-11-B at :2176, Python 3.12.10, git 2.56.0 | :2176 heading as quoted | MATCH |
| 18 | Q4 :139 | vm-queue :41 to-do quote | exact string on vm-queue :41 | MATCH |
| 19 | Q5 :151, :157 | HANDOFF.md:22 "the decision on `ckh`"; :20 Amear's two questions | working-copy :20 "**Questions that are Amear's..."; :22 "**For Amear's hands (not questions):** the decision on `ckh`" | MATCH |
| 20 | Q5 :152 | session-close :48 "No reply yet at filing." | exact string on :48 | MATCH |
| 21 | Q5 :160 | session-close :53 "not this year", "an estimate, not a decision" | both strings on :53 | MATCH |
| 22 | Q5 :156 | vm-queue :42 "Later, not today", "needs Amear's OK" | both strings on :42 | MATCH |
| 23 | Q5 :154 | vm-queue :43 open item | :43 "4. **Open:** what restarted NT8 at 12:32 PM." | MATCH |
| 24 | Summary 2 | PF 1.26 to 1.29; max DD -$40637.04 to -$50748.88 | three-strategy-results :402-:404 (E1.1): 1.29/1.26/1.28; -45282.04/-50748.88/-40637.04 | MATCH |
| 25 | Summary 3 | LHM lost $76,009.84, PF 0.84, retired by Amear under D-2026-11-02-A | :405 -$76009.84, 0.84; DECISIONS.md:371 "**Status:** RULED by Amear — R-VN3-1" | MATCH |
| 26 | Summary 7 | R6 strategies are "written specs or designs only, with no code" | live-signal-topology :20 "A PROPOSED research design on branch `r6/announcement-research`"; ckh note "No R6 code exists" (E5.1) | MATCH |
| 27 | Summary 10 | zero hits anywhere for RSI, MACD, Keltner, ADX, stochastic(s), Supertrend, Ichimoku, Donchian, moving average(s) | own re-run over 118 untracked non-ignored files (not covered by E3.2): 0 each; plural "moving averages" and "stochastics" in tracked files: 0 | MATCH |

## Summary scan (S2 / S8)
No S8 overreach found: Q5 lists only, Q4 :145 and S6 :178 explicitly leave the VM-ruling question open. S2 findings, all low:
- F1 (Summary 1, residue of S2-B): "all hand-run by Amear in NT8 on 2026-11-01 at 1 NQ, March 2021 to July 2026" states the settings as plain fact. worker4 :27 "Shown in the screenshots (REPORTED BY AMEAR)"; worker4 :30 "The baseline has no settings screenshot". The Q1 fix was not carried into the Summary. Also "Four strategy runs have recorded backtests" reads as a total, while run 4 is a recorded backtest too (run3 record :111) and T1-T3 are recorded second-hand.
- F2 (Summary 6): "two April shortlists". worker2 :14 and :15 say "Undated in the text"; the April date is the folder name only. R2 is described as "Higher-frequency NQ strategies to pair with Noise-Area", which is not a shortlist.
- F3 (Summary 14): "Waiting on Amear: ... what restarted NT8, the Sim feed check". vm-queue :43 "Open: what restarted NT8 at 12:32 PM." names no owner. vm-queue :41 lists the Sim feed check as the VM agent's to-do ("the VM agent still lists..."). Neither source assigns these to Amear.
- F4 (Summary 13 against Q4 :139): "no repo file records the 11-12 AddOn load itself". vm-queue :41 quotes "...when the AddOn loaded yesterday", and the 11-12 date in this line comes from that same record. Q4 :139 goes further and says no file records "its date", which vm-queue :41 contradicts (second-hand).
- F5 (Summary 12): "T1 matched a hand run" carries no channel label on that line. The hand run has no primary record (worker5 :88). Line 13 adds "Those figures are second-hand", which partly cures it.

Artifact-level (not a figure): :173 "Round 2: see the Round 2 line below." points to nothing. No Round 2 line exists, and :586 reads "Result: PENDING". This is expected while round 2 is still open, but as written the pointer is dangling.

## Hygiene
| check | manager.md | worker1.md |
|---|---|---|
| S13 sentence count | 1 | 1 |
| `tail -1` is the sentence | yes | yes |
| forbidden words count | 0 | 0 |
| name-token check | 0 | 0 |
Own report name check: see the last Evidence block.

## Evidence (literal commands and outputs; excerpts are verbatim lines)
```
$ grep -n 'R-VM-6' DECISION_LOG.md | cut -d: -f1 | sort -u | tr '\n' ' '; echo
630 647 649 
$ grep -c 'R-VM-6' DECISIONS.md
0
$ grep -n '' docs/reports/2026-10-30-run3-backtest-screenshot-record.md | sed -n '102,108p' | cut -c1-200
102:
103:## Addendum 2026-10-30T22:40Z — RUN 3 RULED INVALID by Amear; run 4 supersedes it (REPORTED)
104:
105:Appended by praxis-master after the body above was written. The body stands unedited as the transcription of what the Analyzer displayed.
106:
107:**Amear's ruling (DECISION_LOG `2026-10-30T22:22:00Z`; `docs/reports/2026-10-28-voice-session-notes.md:45-60`):** discrepancy (A) was real. Run 3 ran on `CME FX Futures RTH`. The strategy anchors 
108:
$ grep -n '' docs/reports/2026-11-09-d6-drawdown-check-manager.md | sed -n '45p' | cut -c1-300
45:The D7 test is judged on VS4 (Decision 5). **D7 consequence:** no breaker value is designed to fit the ceiling. R6's research (higher-win-rate, steadier-equity strategies) is pulled forward to P0. The Noise-Area baseline continues through the VM tests for the record, but a GO on MFFU is not expec
$ grep -n '' DECISIONS.md | sed -n '389p;1981p' | cut -c1-420
389:- Filer's reading, not a ruling: notes-3 line 10 names only "the last half hour", so the two Noise-Area variants (OppBand, Flat1559) and the baseline are outside this entry.
1981:- **D7** (:50–54). *(paraphrase)* If D6 fails at every tier at 1 MNQ, breaker values are not designed to fit the drawdown ceiling ("that is curve-fitting"). It is reported, and "R6's research (higher-win-rate, steadier-equity strategies)" is pulled forward to P0. "The Noise-Area baseline continues through the VM tests for the record, but a GO on MFFU is not expected from it."
$ grep -n '' docs/reports/2026-11-13-strategy-review-index-worker4.md | sed -n '27p;30p' (excerpt of the 23,30p run)
27:- Shown in the screenshots (REPORTED BY AMEAR): Last / Minute / 1; date range `2021-03-08 -> 2026-07-17`; order fill resolution `Standard (Fastest)`; slippage `2`; commission template `PRAXIS`; Contracts 1. Sources: the OppBand settings table at TSR :86-:10
30:- The baseline has no settings screenshot (TSR :37). Its settings rest on Amear's C4 notes at N2 :111: "NQCONTROW SEP25 · Last · Minute 1 · 2021-03-08 → 2026-07-17 · CME US Index Futures RTH · ... · Standard (Fastest) · ... · Slippage 2 · ... · BandOrVWAP ·
$ grep -n '' DECISION_LOG.md | sed -n '905p' | grep -o -E '.{200}OppBand.{40}'
ne; master read worker1 :45–46 and :2410 and agrees. Two ungraded observations recorded (worker1 :58–59): (1) :2393 "The 2026-11-01 runs are without-series records only" is unchecked; those runs were OppBand/Flat1559/LH variants whose exits are no
$ sed -n '144p' docs/reports/2026-11-13-strategy-review-index-manager.md | grep -o -E 'row \(905\).{0,120}'
row (905) that matches a run term (OppBand) is about the 2026-11-01 hand runs, not a VM-side run.
$ git diff --quiet HEAD -- HANDOFF.md; echo exit=$?
exit=1
$ git show HEAD:HANDOFF.md | grep -n '' | sed -n '12,22p' | cut -c1-120 (excerpt)
13:**Next, in order (decided by master under D1; one manager at a time):**
14:1. OPEN-A1 cure exactly as DECISION_LOG 2026-11-13T13:37:42Z items (i)–(iv): delete one clause at :2422, add one name
$ grep -n '' DECISIONS.md | sed -n '1077p' | grep -o -E '.{0,80}(OppBand|Flat1559).{0,80}' | head -3
e paper's published values (no wide search); ATR 14; exit policies BandOrVWAP / OppBand / Flat1559; in-sample objective = risk-adjusted return with a minimum trade cou
$ grep -n -i -E 'OppBand|Flat1559' DECISIONS.md | sed -n '1,40p' | cut -c1-140 (excerpt)
504:- Voice agent's record (notes-3 line 23): the fill at the 15:59:00 price, printed as 4:00 PM in the grid, is accepted. Flat1559 is uncha
1222:   Q4 yes, OppBand = the paper's opposite band, as in _OppBand.cs.
1223:   Q5 yes, Flat1559 = BandOrVWAP exits, flatten on the 15:59 bar, as in _Flat1559.cs.
$ grep -n -E '1,211|3,136.84|1\.08|4,108.84' docs/reports/2026-10-30-run3-backtest-screenshot-record.md | cut -c1-200 | head -8
111:1,211 trades (584 L / 627 S) · net $3,136.84 · gross profit $41,447.47 · gross loss −$38,310.63 · commission $3,584.56 · PF 1.08 · max DD −$4,108.84 · avg trade $2.59 · longs +$4,541.40 / shorts −
118:- Commission = 1,211 × $2.96 ✓. Net = gross profit − gross loss ✓ = longs + shorts ✓. Avg trade $2.59 ✓. Largest winner = 57% of net.
$ grep -n '' docs/reports/2026-10-30-run3-backtest-screenshot-record.md | sed -n '111p' | grep -o -i -E 'win[^·]{0,30}' ; echo exit=$?
winner $1,792.50 
exit=0
$ grep -n '' docs/reports/2026-11-13-strategy-review-index-worker5.md | sed -n '89p' | grep -o -i -E '.{0,120}(point value|not comparable).{0,80}'
.84**". These predate the point-value fix: `docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:30`: "With a $1 point value, points and dollars are the same number." Superseded as figures; historical onl
$ grep -n '' docs/reports/2026-11-13-strategy-review-index-worker5.md | sed -n '68p;88p;89p' | cut -c1-300 (excerpt)
68:- Gate value provenance: there is no literal "$1,600" in DECISIONS.md or the values spec. The `1,600|$1600|50K` grep hits there are only the Builder 50K add-on / $1,500 rows (`DECISIONS.md:1388-1389`; values spec `:136`, `:297-298`, `:331`, `:338`). Values spec `:136` (excerpt): "**The Phase 3 sp
88:   - The "T1 reference (Amear's hand run)" of 1,173 trades (the 09:30 ET session-start run): no primary record found in `docs/reports`, STATUS.md or HANDOFF.md. The `1,173|176,392` grep (Evidence E11) hits only the 2026-11-13 handoffs and the research-filing workers that copy them. Its original r
$ grep -n '' docs/reports/2026-11-13-strategy-review-index-worker2.md | sed -n '18p' | grep -o -F '**No new strategy was proposed.**'
**No new strategy was proposed.**
$ grep -n '' docs/reports/2026-11-13-strategy-review-index-worker2.md | sed -n '14,15p' | cut -c100-330
r name only) | **NOT IN RECORD.** 0 model-name hits in the text (E15) | NQ/ES strategy shortlist with behavioural screening | `Redemtion/Intitialization-April 2026/Verified Trading-Strategy Shortlist for NQ : Index Futures.rtf` | E
er-frequency NQ strategies to pair with Noise-Area | `Redemtion/Intitialization-April 2026/Systematic, Higher-Frequency NQ Strategies to Pair with the Noise-Area Breakout .rtf` | E2, E15 |
$ grep -n '' docs/reports/2026-11-13-strategy-review-index-worker2.md | sed -n '14,21p' | cut -c1-110 (excerpt)
14:| R1 (D2) | Undated in the text; the file sits in `Redemtion/Intitialization-April 2026/` (folder name only
15:| R2 (D8) | Undated in the text; same folder | **NOT IN RECORD.** 0 model-name hits (E15) | Higher-frequenc
21:| R8 (Kimi) | 2026-11-13; output supplied 14:26 ET (REPORTED BY the channel) | Amear ran Kimi Deep Research
$ grep -n '' DECISIONS.md | sed -n '1590p'; grep -n '' docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md | sed -n '3p;26p' | cut -c1-200 (excerpt)
1590:R9  FOMC-Cycle Even-Week stays parked while trading on MFFU
26:Two deep-research runs (Gemini, then Kimi) were asked for a steady, high-win-rate intraday NQ strategy that survives an MFFU trailing drawdown at 1 MNQ. **Neither found a viable new candidate.** St
$ grep -n '' ninjascript/PraxisNoiseAreaBreakout.cs | sed -n '34p'; grep -n '' STATUS.md | sed -n '192p' | cut -c1-80
34://     multiplier as a tunable), NO ATR stop. The ONLY selectable knob is the exit form (ExitMode).
192:- Arm (b): `.cs` WRITTEN only — not compiled, not run; on `arm-b/wf-tunables
$ grep -n '' docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md | sed -n '85p' | cut -c1-40
85:Fit: Low. The profile is low win rate
$ grep -n '' docs/reports/2026-11-13-strategy-review-index-worker3.md | sed -n '82p' | cut -c100-260
6-11-13, rated low, channel-recommended for backtest, with no ledger decision found.**
$ grep -n '' DECISIONS.md | sed -n '2076p;2176p' | cut -c1-120
2076:## 2026-11-10 — D-2026-11-10-C: VM agent = Hermes over SSH (settlement 3 changed; master under D1)
2176:## 2026-11-11 — D-2026-11-11-B: VM handoff §1 limit 9 lifted by Amear for one install; Python 3.12.10 and git 2.56.
$ wc -l < docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md; wc -l < docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md; grep -n '' docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md | sed -n '41p' | grep -o -F 'check in the Control Center whether the Sim feed cycled when the AddOn loaded yesterday.'
      44
      54
check in the Control Center whether the Sim feed cycled when the AddOn loaded yesterday.
$ grep -n '' HANDOFF.md | sed -n '20p;22p' | cut -c1-90
20:**Questions that are Amear's (unchanged; DECISION_LOG 2026-11-12T13:01:49Z item b):** (
22:**For Amear's hands (not questions):** the decision on `ckh`; D2 items unchanged (Sim-o
$ grep -n '' docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md | sed -n '48p' | grep -o -F 'No reply yet at filing.'; grep -n '' docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md | sed -n '53p' | grep -o -E 'not this year|an estimate, not a decision'
No reply yet at filing.
an estimate, not a decision
not this year
$ grep -n '' docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md | sed -n '42p' | grep -o -E 'Later, not today|needs Amear.s OK'
Later, not today
needs Amear's OK
$ grep -n '' docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md | sed -n '43p'
43:4. **Open:** what restarted NT8 at 12:32 PM.
$ grep -n '' DECISIONS.md | sed -n '368,376p' | grep -n -i -E 'WHO|amear' | cut -c1-200 | head -4 (excerpt)
4:371:**Status:** RULED by Amear — R-VN3-1. Ledger authorisation (S5): DECISION_LOG row `2026-11-02T21:23:45Z` (WHO: amear). Appended 2026-11-02 by praxis-manager, unit `2026-11-02-r-vn3-1-filing`.
$ grep -n -i -o -E '.{0,90}pre-announcement drift.{0,90}' docs/specs/2026-11-10-f2-session-flat-proposal.md docs/specs/2026-11-10-live-signal-topology.md | head -4
docs/specs/2026-11-10-f2-session-flat-proposal.md:64:| R6 evening-entry strategy (Pre-Announcement Drift) | Entries at 18:05 fall after the 18:00 next-session start, so they are allowed. Variant
docs/specs/2026-11-10-live-signal-topology.md:20:| 1.4 | R6 Pre-Announcement Drift, evening entry | A PROPOSED research design on branch `r6/announcement-research` (`bf6fcc
$ for t in RSI MACD Keltner ADX stochastic supertrend ichimoku donchian 'moving average'; do printf '%s: ' "$t"; git ls-files -z --others --exclude-standard | grep -z -v -E '2026-11-13-strategy-review-index-|2026-10-28-f4-|/evidence/' | xargs -0 /usr/bin/grep -i -w -h -e "$t" 2>/dev/null | wc -l; done
RSI:        0
MACD:        0
Keltner:        0
ADX:        0
stochastic:        0
supertrend:        0
ichimoku:        0
donchian:        0
moving average:        0
$ git ls-files --others --exclude-standard | grep -v -E '2026-10-28-f4-|/evidence/' | wc -l
     118
$ for t in 'moving averages' stochastics 'exponential moving' ...; do ... git grep -i -h -F -e "$t" ... | wc -l; done (excerpt; the ' EMA'/' SMA' probes matched ordinary words and were discarded)
moving averages:        0
stochastics:        0
exponential moving:        0
```

Hygiene block (verbatim):
```
$ grep -c -F '[the S13 sentence]' docs/reports/2026-11-13-strategy-review-index-manager.md
1
$ tail -1 docs/reports/2026-11-13-strategy-review-index-manager.md
[the S13 sentence]
$ grep -c -i -E 'v[e]rdict|COMMIT-I[N]DEX|COMMIT-D[I]FF-SHA256' docs/reports/2026-11-13-strategy-review-index-manager.md
0
$ grep -c -i -w "$(ls docs/reports | grep ^2026-10-28-f4- | head -1 | sed ...)" docs/reports/2026-11-13-strategy-review-index-manager.md
0
$ grep -c -F '[the S13 sentence]' docs/reports/2026-11-13-strategy-review-index-worker1.md
1
$ tail -1 docs/reports/2026-11-13-strategy-review-index-worker1.md
[the S13 sentence]
$ grep -c -i -E 'v[e]rdict|COMMIT-I[N]DEX|COMMIT-D[I]FF-SHA256' docs/reports/2026-11-13-strategy-review-index-worker1.md
0
$ grep -c -i -w "$(ls docs/reports | grep ^2026-10-28-f4- | head -1 | sed ...)" docs/reports/2026-11-13-strategy-review-index-worker1.md
0
```
(In this block the S13 sentence is shown as [the S13 sentence] and the three forbidden words with one bracketed letter, so this report holds the sentence once and none of the words. The commands that ran used the literal strings; see the scratchpad script hyg.sh.)

Own-report name check: pasted to the manager in the return message (run after this file was final).

## Totals
- Fix re-check: 8 FIXED, 0 NOT FIXED. S2-B is fixed in Q1 but carries a residue into Summary line 1 (F1).
- Spot-checks: 27 MATCH, 0 MISMATCH (Q1 7, Q2 5, Q3 2, Q4 4, Q5 5, Summary 4; #14 is a Q2 pointer to worker3 and is counted under Q2).
- Summary scan: 5 low S2 findings (F1 to F5), 0 S8.
- Artifact-level: 1 dangling pointer (:173 "Round 2 line below"; :586 "Result: PENDING").
- Hygiene: clean on manager.md and worker1.md.
- Files staged: none. File written: this report only.
- Result: BREAKS FOUND (low severity only; no figure or pointer mismatch).

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
