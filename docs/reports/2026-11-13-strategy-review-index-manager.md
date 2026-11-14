# 2026-11-13 strategy review index (manager report)

## Summary (plain English, 15 lines)
1. Q1: Four strategy runs have recorded backtests, all hand-run by Amear in NT8 on 2026-11-01; settings as he reported them: 1 NQ, 2021-03-08 to 2026-07-17.
2. Three are Noise-Area breakout arms (baseline, OppBand, Flat1559): each made money at 1 NQ, profit factor 1.26 to 1.29, max drawdown -$40637.04 to -$50748.88 as written.
3. The fourth, Last-Half-Hour Momentum, lost money (net "-$76009.84", profit factor 0.84, three-strategy-results :405) and was retired by Amear under D-2026-11-02-A.
4. The D6 drawdown check (f10603a) found all three Noise-Area arms fail every MFFU account size at 1 MNQ on the committed measure (MNQ derived from the NQ trade lists, not an MNQ run); the 50K ceiling is $1,600.
5. D7 says "The Noise-Area baseline continues through the VM tests for the record, but a GO on MFFU is not expected from it"; DECISIONS.md does not say whether OppBand and Flat1559 share that status. No walk-forward has been run, and A20 was a connection check, not a backtest.
6. Q2: Eight research efforts are on record: two undated research files in a folder named April 2026 (a shortlist and a pairing list), a May three-agent search, the 7zq shortlist (Oct 31), set A/B/C (Nov 4, no new strategy), the Nov 8 filter audit, and today's Gemini and Kimi runs.
7. Only two research ideas were ever backtested (Noise-Area and Last-Half-Hour Momentum); TORB/ORB and the R6 announcement strategies are written specs or designs only, with no code.
8. Today's Gemini and Kimi runs found no viable new candidate; the channel's session-close withdrew their "test Last-Half-Hour Momentum first" advice.
9. Several ideas keep coming back across runs: last-half-hour momentum, gap fade, VWAP reversion, opening range breakout, overnight and pre-FOMC drift.
10. Q3: No systematic look at indicator strategies exists; RSI, MACD, moving averages, Keltner, ADX, stochastics, Supertrend, Ichimoku and Donchian have zero hits in the tracked files and the Redemtion text.
11. Indicators appear only inside Noise-Area (VWAP is its coded exit; an ATR stop is written, not run) and as a few screened-out ideas (VWAP/Bollinger reversion, standalone ORB, order flow).
12. Q4: The only VM record of 11-12 and 11-13 is two channel files; as reported there, the VM agent ran three bridge backtests (T1 said to match a hand run with no primary record here, 1,173 trades, $176,392.92; T2 OppBand $188,618.48).
13. Those figures are second-hand; the VM's result files, bridge log and commits live in a local repo on the VM and are not in Praxis.build; the 11-12 AddOn load appears only as one quoted to-do line.
14. Q5: Recorded for Amear: the ckh decision, two open questions, and the hand step of setting $4.68 commission; also open: MFFU's reply, what restarted NT8 (no owner named), and the VM agent's Sim feed check.
15. Nothing here is decided; every figure is quoted from the files named below.

## Task
Unit 2026-11-13-strategy-review-index, read-only. Authority DECISION_LOG.md row 2026-11-13T20:36:45Z.

## Rubric criteria addressed
S1 (pasted output: the Verification evidence section and each worker's evidence section); S2 (status words kept at the level the source states: specified, written, tested, retired, channel-reported); S8 (no question of Amear's is answered: Q5 lists only); S13 (the sentence once, as the last line).

## Workers dispatched
| id | mode | scope | outcome |
|---|---|---|---|
| worker1 | BUILD | Q1 whole | stopped at its 40-turn limit; report left as a 12-line skeleton (`-worker1.md`); scope re-split to worker4 and worker5 |
| worker2 | BUILD | Q2 | turn limit reached after writing a complete report (`-worker2.md`, 423 lines); used |
| worker3 | BUILD | Q3 | finished (`-worker3.md`); used, with one reading corrected in Q2 above |
| worker4 | BUILD | Q1 part A (2026-11-01 runs) | finished (`-worker4.md`) |
| worker5 | BUILD | Q1 part B (A20, D6 gate, walk-forward, other results) | finished (`-worker5.md`) |
| worker6 | ADVERSARIAL | spot-check of this report | see Adversarial findings |

## Process log
- Read DECISION_LOG.md last row (2026-11-13T20:36:45Z) and specs/SPEC_RUBRIC.md S1, S2, S8, S13 (:133, :134, :140, :145).
- Skill note: the session invoked the orchestrator skill, whose first step arms hooks under .claude/state; the brief forbids writing under .claude/, so nothing was armed. Recorded here, not escalated.
- Q4 and Q5 were done by the manager directly (E4, E5). Q1 to Q3 went to workers; Q1 was re-split after worker1 hit its turn limit.
- Manager re-ran each worker's key lines (E1 to E3) before folding them in; pointer errors found in this report's own drafts (HANDOFF line numbers, worker5 line numbers) were corrected before the adversary round.
- Hygiene: name-token check and forbidden-word check run on every unit report (see Adversarial findings).

## Q1. Strategies tested in this repo

Sources: worker4's report `docs/reports/2026-11-13-strategy-review-index-worker4.md` (findings table :23-:45, status lines :46-:61) and worker5's report `docs/reports/2026-11-13-strategy-review-index-worker5.md` (A20 :7, D6 and gate :19-:69, walk-forward :70-:82, other results :83-:98). The manager re-ran the key figures in E1.1 to E1.4.

Common settings for the four 2026-11-01 runs (worker4 :25-:30; shown in the screenshots, REPORTED BY AMEAR, and the baseline has no settings screenshot, so its settings rest on his C4 notes): NQCONTROW SEP25, 1-minute, 2021-03-08 to 2026-07-17, Standard (Fastest) fill resolution, slippage 2, PRAXIS commission template ($2.96 per row in the CSVs), 1 contract (1 NQ). All four are Amear's hand runs in the NT8 Strategy Analyzer, exported to CSV. They were then recomputed on the Mac by praxis workers, and `docs/reports/2026-11-01-csv-analyses.md:41-44` records MATCH on all four.

Figures, quoted from `docs/reports/2026-11-01-three-strategy-results.md:402-405` (E1.1). Column order: trades, net, PF, max DD, win %, avg trade.

- Baseline `PraxisNoiseAreaBreakout`, BandOrVWAP, :402: 1190, $197327.60, 1.29, -$45282.04, 40.67%, $165.82. Status: no DECISIONS.md entry retires or adopts it. It is listed as a walk-forward exit policy (DECISIONS.md:1077). D7 names it: "The Noise-Area baseline continues through the VM tests for the record" (DECISIONS.md:1943-1944).
- OppBand `PraxisNoiseAreaBreakout_OppBand`, :403: 810, $210182.40, 1.26, -$50748.88, 58.02%, $259.48. Status: no DECISIONS.md entry retires or adopts it; listed as a walk-forward exit policy (DECISIONS.md:1077); definition ruled at :1222. Whether D7's "for the record" covers it is NOT stated in DECISIONS.md; the channel reads T2 OppBand as "Noise-Area numbers, kept for the record only" (vm-queue :36), the channel's reading.
- Flat1559 `PraxisNoiseAreaBreakout_Flat1559`, BandOrVWAP exits, flat on the 15:59 bar, :404: 1190, $193017.60, 1.28, -$40637.04, 40.50%, $162.20. Status: no DECISIONS.md entry retires or adopts it; fill accepted at :504, definition ruled at :1223, exit policy at :1077. Whether D7's "for the record" covers it is NOT stated in DECISIONS.md.
- `PraxisLastHalfHourMomentum`, :405: 1304, -$76009.84, 0.84, -$99806.96, 47.62%, -$58.29. Status: RETIRED, D-2026-11-02-A (DECISIONS.md:368). Bead `afe` CLOSED (E5.4).

Earlier runs, context only (worker4 rows 5-6, from `docs/reports/2026-10-30-run3-backtest-screenshot-record.md`). Both were on the old `NQCONT` row and are retired as baselines by R-VM-6, which appears in DECISION_LOG.md (:630, :647, :649) only, with no DECISIONS.md entry.
- Run 3: 1075 trades, $1,281.61, PF 1.04, max DD −$4,051.57. Recorded INVALID (run3 record :103, "RUN 3 RULED INVALID by Amear", and :107).
- Run 4: 1,211 trades, $3,136.84, PF 1.08, max DD −$4,108.84. Win rate NOT IN RECORD.
- Worker5 :89 notes that these early runs predate the point-value fix ($1 point value), so their dollar figures are not comparable.

VM bridge runs T1 to T3, 2026-11-13: see Q4. The figures are channel-reported. The 1,173-trade "Amear's hand run" that T1 matched has no primary record in this repo. Worker5 :88: "Its original record: NOT IN RECORD in the paths searched". The 2026-11-01 baseline is 1190 trades, and T1 is 1,173 on a tab named "PRAXIS baseline NQCONTROW 0930". This index does not explain the difference; it was not investigated.

A20 (`docs/reports/2026-10-20-a20-results.md`) is NOT a strategy backtest. It is a hand-read check of Fusion time zones and Kinetick connections, with no trades, net, PF or drawdown (worker5 :7-:17).

### The drawdown gate and how a strategy is judged (worker5 :31-:69; E1.2, E1.3)
- Gate rule A4, DECISIONS.md:1735-1740: "backtest max drawdown must stay below 80%" of the ruled limit, "i.e. below the lower of 3.2% of the MFFU" account size "and 80% of MFFU's trailing drawdown limit". It is "Evaluated against every tier row".
- The 50K ceiling is $1,600 at 1 MNQ (D6 report :31). That figure is computed from A4 in the D6 report, and no literal "$1,600" appears in DECISIONS.md (worker5 :68). INFERRED: 3.2% x $50,000 = $1,600.
- D6 (DECISIONS.md:1930-1939) ordered a Mac-only drawdown check on the three 2026-11-01 Noise-Area trade lists, per walk-forward window, at 1 MNQ and 1 NQ. It was committed in `f10603a` (`docs/reports/2026-11-09-d6-drawdown-check-manager.md`).
- D6 result (D6 report :7), at 1 MNQ: worst within-window stretch "$2,774 to $2,914", under the ceiling "only on the 150K accounts". On the committed four-measure basis it is "$4,463 to $5,280. That fails every account size." At 1 NQ, "every account fails." The D6 report :56 labels these "COMPUTED figures on NT8 trade lists", with MNQ "derived, not an MNQ run".
- D7 (DECISIONS.md:1940-1944) applies if D6 fails at every tier at 1 MNQ: do not fit breaker values to the ceiling; pull R6 research forward to P0; "The Noise-Area baseline continues through the VM tests for the record, but a GO on MFFU is not expected from it." DECISIONS.md:2283 records D7 as fired.
- Status after D6/D7: D7 and the D6 report (:45) name only "The Noise-Area baseline" as continuing "through the VM tests for the record". DECISIONS.md does not state the status of OppBand and Flat1559 after D7. No retirement entry exists for any of the three. Extending "for the record" to all three arms is the channel's reading (vm-queue :36), not a recorded ruling.

### Walk-forward (worker5 :70-:82)
SPECIFIED, with Mac-side tooling written and tested on synthetic data. No walk-forward has been RUN, and no out-of-sample result is recorded. STATUS.md:195: "T1–T13: none has run. All wait for the VM." The walk-forward spec :5 reads "**Status: DERIVED — not yet ruled on as a whole by Amear.**" The values-spec v2.2 amendment is parked under bead `diq` (E5.4). The D6 per-window figures are not walk-forward results (worker5 :71).

## Q2. Research runs

Source: worker2's report, `docs/reports/2026-11-13-strategy-review-index-worker2.md` (research-runs table :10-:23, proposal-fate table :25-:64, cross-run repeats :66-:79, evidence E0-E22). The manager re-ran the key ledger lines (E2.1 to E2.4 below).

Eight research efforts are on record (worker2 :14-:21):
- R1 and R2 (April 2026, gitignored RTFs in `Redemtion/Intitialization-April 2026/`). R1 is an NQ/ES shortlist; R2 covers higher-frequency strategies to pair with Noise-Area. The model that produced them is NOT IN RECORD.
- R3, the Phase 2 three-agent search (prompts and compiled results dated May 6, 2026, in `Redemtion/Research Prompts/` and `Redemtion/Research Results/`). It covered commodities, FX and cross-instrument ideas.
- R4, the 7zq M2 shortlist (2026-10-31, Claude Code).
- R5, research set A/B/C (reports dated 2026-11-04, landed in `84b1a58`): tick data, comparable builds, proof-of-concept standard. Worker2 :18: "**No new strategy was proposed.**"
- R6, the strategy filter audit (2026-11-08, Claude.ai channel).
- R7, Gemini Deep Research (2026-11-13).
- R8, Kimi Deep Research (2026-11-13).

`docs/reports/2026-11-08-voice-strategy-brief.md` is a status brief with no strategy proposals (worker2 :23, E17).

What happened to the proposals (worker2 fate table; the manager re-ran the DECISIONS lines in E2.1):
- Only two ideas were ever backtested, both in the 2026-11-01 hand runs. One is Noise-Area with its variants. The other is Last-Half-Hour Momentum (Baltussen et al. 2021), retired by D-2026-11-02-A (DECISIONS.md:368, :383 "is **removed from the active candidate set**").
- TORB and 5-min ORB (R4) are SPECIFIED only. DECISIONS.md:360: "TORB and ORB remain written specs in the shortlist".
- Pre-Announcement Drift and Announcement-Day Premium are ruled for research under D-2026-11-08-A R6 (DECISIONS.md:1572-:1579). They sit in parked bead `ckh`, and the bead note says "No R6 code exists" (E5.1).
- FOMC even-week is parked by R9 (DECISIONS.md:1590).
- FX Fixings, Overnight Drift and CL EIA are deferred to Phase 3 Block 6 (worker2 rows 9-11).
- Every other R3 item is NOT TESTED with no record.
- The 2026-11-13 Gemini and Kimi candidates are all NOT TESTED or DROPPED. Their status column is the channel's, not Amear's: session-close :28-:35 (E5.3). No DECISIONS.md line names Gemini or Kimi (E2.4: 0).
- Session-close :26 sums it up: "**Neither found a viable new candidate.**"

Correction carried into this index (not a worker error, but a reading to avoid): the Gemini file's channel backtest order at strategy-research :30 (E2.2) put "(1) PraxisLastHalfHourMomentum ... (2) Candidate 1 VWAP mean reversion". That order is superseded. Session-close :3 says "where they disagree, this file governs". Session-close :18 withdraws the LHM recommendation, and :33 rates VWAP sigma-band reversion "NOT TESTED; low". Worker3's report (b)2 and its return still describe VWAP reversion as "channel-recommended" (worker3 :82-:91). That describes strategy-research :30 accurately, but it is not the channel's final position.

Ideas proposed in more than one run (worker2 :66-:79):
- Last-half-hour momentum: 5 appearances (count INFERRED by worker2). Tested once and retired. Re-recommended by both 2026-11-13 runs, then withdrawn.
- First-half-hour to last-half-hour threshold momentum: R2, R3, R4, R7, R8. Never tested.
- Opening gap fade: excluded in R2 and R3, re-proposed in R7 and R8. Never tested.
- VWAP/Bollinger mean reversion: excluded in R2 and R3, re-proposed in R7 and R8. Never tested.
- Opening range breakout: eliminated in R3, short-listed in R4, now SPECIFIED.
- Overnight drift, pre-FOMC drift, Pre-Announcement Drift and FOMC even-week each recur; their fates are in worker2's table.

## Q3. Indicators

Source: worker3's report, `docs/reports/2026-11-13-strategy-review-index-worker3.md` (term-count table :11-:49, (a) :51-:70, (b) :72-:105, conclusion :107-:115). The manager re-ran the key lines (E3.1 to E3.3).

(a) Indicators used inside existing strategies:
- Session VWAP is CODED as the default exit of `PraxisNoiseAreaBreakout`. `.cs:46`: "BandOrVWAP = paper's PREFERRED model, trailing stop at max/min(band, VWAP) (§4 p.13). DEFAULT." (E3.1). It was backtested as that strategy's exit: the 2026-11-01 table row reads "BASELINE (`PraxisNoiseAreaBreakout`, BandOrVWAP)" (three-strategy-results :402, E1.1); Flat1559 also uses BandOrVWAP exits (worker4 table). The VM T1/T3 rows (vm-queue :15, :17, channel-reported) say ExitMode BandOrVWAP too.
- ATR(14) stop multipliers for walk-forward arm (b): WRITTEN only. STATUS.md:192: "Arm (b): `.cs` WRITTEN only — not compiled, not run" (E3.1). The main-branch strategy has "NO ATR stop" (`.cs:34`).

(b) Indicator-driven strategies:
- Standalone VWAP/Bollinger reversion on NQ: "**EXCLUDED** — no peer-reviewed NQ evidence post-2018" (Redemtion Phase 2 table :47, E3.3).
- 5-minute standalone ORB on NQ: "**ELIMINATED** — no robust standalone edge on NQ without filters" (:38). TORB and ORB were later short-listed and are SPECIFIED only (DECISIONS.md:360).
- Order-flow imbalance: "**EXCLUDED** — 2-price-change horizon, requires co-location" (:45).
- VWAP sigma-band reversion (Kimi C1): PROPOSED 2026-11-13. Kimi :81: "Post-2018 evidence: None found." Kimi :85: "Fit: Low." Session-close :33: "NOT TESTED; low". No code.

Plain answer: the record has NO systematic look at indicator-driven strategies. The manager's re-run over all tracked files plus the Redemtion text returned 0 hits each for moving average, RSI, MACD, Keltner, ADX, stochastic, Supertrend, cumulative delta, Ichimoku and Donchian (E3.2). Worker3's area-by-area counts agree (worker3 :15-:41). Screening in the research runs was by published post-2018 NQ evidence, and indicator-style entries were excluded on that ground (E3.3). No indicator-driven strategy has been coded or backtested.

## Q4. VM code agent activity 2026-11-12 and 2026-11-13

The master's finding is CONFIRMED by this manager's own search (evidence blocks E4.1 to E4.8): the only record in this repo of what the VM-side agent did on 2026-11-12 and 2026-11-13 is the two Claude.ai channel files filed at `9ff8a48`, `docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md` (44 lines) and `docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md` (54 lines). Both are second-hand. vm-queue :5 says the source is "the VM Claude Code session's own report, pasted to this channel by Amear at 14:37 ET (REPORTED BY Amear; the channel has not read the VM repo)". So these figures are channel-reported, not observed by any Mac-side agent.

What the record says (all from vm-queue unless marked):
- Who: vm-queue :5, "The VM agent is the session working in `C:\praxis\vm-bridge` on the Windows VM. It is not praxis-master."
- Setup: vm-queue :11, tab "PRAXIS baseline NQCONTROW 0930", PraxisNoiseAreaBreakout, NQCONTROW SEP25, 1-minute, 2021-03-08 to 2026-07-17, RTH 0930, commission $2.96 round trip, slippage 2, Standard fill resolution, 1 NQ.
- Runs, vm-queue :15-:17: T1 BandOrVWAP "1,173" trades, "$176,392.92" net, PF "1.2615", max DD "-$38,905.64", "Exact match" to Amear's hand run. T2 OppBand "1,112", "$188,618.48", "1.2861", "-$37,906.24". T3 BandOrVWAP "1,173", "$176,392.92", "1.26", "-$38,905.64", "Identical to T1 trade by trade (request id excepted)".
- What it proved, per the channel (vm-queue :20-:22, :35): the bridge applies the ExitMode enum; T3 restores the tab; no connect or disconnect lines during runs; "The bridge works for headless backtests" is labelled "the channel's reading, INFERRED, not a ruling" (:33).
- Not checked: commission (vm-queue :23, "the bridge's result files carry no commission total, so the hand run's $3,472.08 could not be checked").
- Deviations (vm-queue :27-:31): first T1 attempt stopped because no Strategy Analyzer window was open, Amear opened the tab by hand; NT8 restarted at 12:32:48 PM (PID 11820), "Who or what restarted NT8 is not stated in the report (open)"; `run-queue.ps1` not used because it "needs the `claude` command, which is not installed on the VM"; `tools\send-backtest.ps1` "was changed: extended so it can pass strategy parameters".
- Channel's status call (vm-queue :36): "These are Noise-Area numbers, kept for the record only (D7 after the D6 drawdown check)". Its 1 MNQ figure "about $3,790 (one tenth of $37,906.24), above the 50K gate of $1,600" is the channel's arithmetic, not a run.
- 2026-11-12: the only mention in the repo of anything the VM agent did on 2026-11-12 is vm-queue :41, which quotes the VM agent's to-do "check in the Control Center whether the Sim feed cycled when the AddOn loaded yesterday." The date 2026-11-12 is INFERRED from "yesterday" in that 2026-11-13 quote. Beyond that line, no file in the repo records the load itself, who did it, or its outcome (E4.3 to E4.6).

What is NOT in this repo (E4.3 to E4.7):
- The VM agent's results files `results\T1.json`, `results\T2.json`, `results\T3.json`, its `bridge.log`, RESULTS.md, QUEUE.log, LOG.md, `run-queue.ps1`, and the changed `tools\send-backtest.ps1`. vm-queue :5: "Its results and commits live in that local git repo (no remote)". `mdfind -name vm-bridge` returned 0 hits on this Mac.
- Any `vm/replies/` file after 2026-11-11: the newest is `20261111T172940Z-STATUS.md`; the last commit touching `vm/` is `ee54344` (2026-11-11).
- Any DECISION_LOG or DISPATCH_LOG row of 2026-11-12 or 2026-11-13 that records a VM-side run. The rows matching VM, Hermes, bridge or NT8 are master session-start, filing and outage rows. The one row (905) that matches a run term (OppBand) is about the 2026-11-01 hand runs, not a VM-side run.
- Any DECISIONS.md entry naming the `vm-bridge` repo or adopting a VM Claude Code session as the VM agent: the only case-insensitive "VM Claude Code" hit is DECISIONS.md:1010 (the ruling quoted next), and `vm-bridge` has no hit (E4.7). The last VM-agent decision on record is D-2026-11-10-C (DECISIONS.md:2076), "VM agent = Hermes over SSH". DECISIONS.md:1010 records Amear's 2026-10-28 ruling "No more Cowork or in-VM Claude Code executor work.", "lifted COMPLETELY once two tests pass". This index does not say whether the 2026-11-13 VM session falls inside or outside that ruling or D-2026-11-10-C. That question is not answered here (S8).
- The Hermes VM path (D-2026-11-10-C): its last filed replies are 2026-11-10 and 2026-11-11 (`vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md` through `20261111T172940Z-STATUS.md`). D-2026-11-11-B (DECISIONS.md:2176) records Python 3.12.10 and git 2.56.0 installed in the VM.
- `~/Downloads/2026-11-13-return-handoff-claude-ai-vm-queue-results.md` (outside the repo) differs from the filed copy by one extra trailing S13 line only (E4.8).

## Q5. What is open (pointers only; nothing here is decided)

- Bead `Praxis_build-ckh` (P0, OPEN, parked): R6 research on Pre-Announcement Drift and Announcement-Day Premium. Its notes say it was "PARKED (absolute park rule, audit-fail-x2)" on 2026-11-12 and "No R6 code exists." HANDOFF.md:22 (working copy) lists "the decision on `ckh`" under "For Amear's hands (not questions)". Session-close :52: "a ruling on parked `ckh` (the channel recommended resuming it; Amear has not ruled)". (E5.1, E5.2)
- MFFU email: session-close :48, a follow-up was sent at 2026-11-13 17:26Z asking for a written yes/no on unattended automated trading, and on "Builder Plans". "No reply yet at filing." Related bead `Praxis_build-fx4` (P1, OPEN): "MFFU automation-compliance: confirm in writing that fully-automated trading is permitted before any live step". (E5.3)
- MFFU commission re-run: vm-queue :40. Amear sets both PRAXIS commission rows to 2.34 by hand ($4.68 round trip), then the VM agent re-sends T1. The expected net "about $174,375.36" is the channel's arithmetic, not a run.
- What restarted NT8 at 12:32 PM: vm-queue :28 and :43, open.
- Sim feed check: vm-queue :41. Whether Amear's Control Center look today covers yesterday's AddOn load "is not confirmed".
- Analyzer tabs for `PraxisNoiseAreaBreakout_Flat1559` and `PraxisLastHalfHourMomentum` are "Later, not today", using `satemplate`, which "needs Amear's OK" (vm-queue :42).
- Amear's two open questions, HANDOFF.md:20 (working copy; HANDOFF.md differs from HEAD, E5.2): "(1) does MFFU's 2026-11-11T22:41:33Z point 4 close R6 OPEN-1; (2) should F4's bar change."
- HANDOFF.md:12-16 (working copy) "Next, in order": `ckh`; the broker route ("MFFU does not offer Rithmic; D-2026-11-10-B is contradicted and not re-decided"); the OPEN-T1 VM-to-webhook check; the rest of bead `fgd`.
- Strategy-adjacent open beads (E5.4, E5.5): `Praxis_build-diq` (P1, PARKED walk-forward spec amendment), `Praxis_build-qtk` (P2, replication-arm gate set), `Praxis_build-q36` (P2, 0-S trade-count difference), `Praxis_build-ajj` (P2, Monte Carlo engine on pooled OOS trades), `Praxis_build-b5z` (P2, import-file volume anomaly).
- Go-live timing: session-close :53 records the channel's estimate, "not this year", labelled "an estimate, not a decision".

## Adversarial findings
Round 1, worker6 (cold; given the artifact and the criteria only): `docs/reports/2026-11-13-strategy-review-index-worker6.md`. It made 51 spot-checks: 49 MATCH, 2 MISMATCH. It also raised six S2 findings (A to F), found nothing under S8, confirmed every Q4 absence claim, and reported hygiene clean on all reports. Every fix below was applied to this report, and the lines behind them were re-checked in E6.1:
- MISMATCH 1, R-VM-6 "appears in DECISION_LOG.md:647 only": it also appears at :630 and :649. Now reads (:630, :647, :649).
- MISMATCH 2, run 3 INVALID cited at :106, a blank line: now :103 (the heading) and :107.
- S2-A (medium), "kept for the record" extended to all three Noise-Area arms: D7 and the D6 report name only "The Noise-Area baseline". Summary line 5 and the Q1 status lines now say DECISIONS.md does not state the OppBand and Flat1559 status after D7, and that extending it is the channel's reading (vm-queue :36).
- S2-B, run settings stated as plain fact: now marked as shown in screenshots, REPORTED BY AMEAR, with no baseline screenshot.
- S2-C, the summary dropped "derived, not an MNQ run": added to summary line 4.
- S2-D, "Mac-side 2026-11-01 runs" (Q4, row 905): now "the 2026-11-01 hand runs".
- S2-E, the VWAP exit "backtested" claim rested on second-hand VM rows: it now cites three-strategy-results :402 first.
- S2-F, HANDOFF.md pointers are to the uncommitted working copy: now labelled, with `git diff --quiet` exit=1 in E6.1.

Round 2, worker7 (cold): `docs/reports/2026-11-13-strategy-review-index-worker7.md`. Results: 8 of 8 round-1 fixes FIXED; 27 MATCH, 0 MISMATCH. It raised five low S2 wording findings in the Summary and one dangling pointer, all fixed in this report:
- F1, line 1, settings as fact: now "as he reported them".
- F2, line 6, "two April shortlists": now "two undated research files in a folder named April 2026 (a shortlist and a pairing list)".
- F3, line 14, owners: the NT8 restart has "no owner named", and the Sim feed check is "the VM agent's".
- F4, AddOn load date: the date is now marked INFERRED from vm-queue :41 "yesterday" (Q4 and Summary line 13).
- F5, line 12: now "as reported there" and "said to match a hand run with no primary record here".
- The dangling "Round 2" pointer is replaced by this paragraph.

The cap of 2 adversary rounds is reached. These last fixes are wording only, with no figure or pointer changed. The manager checked them against vm-queue :41 and :43 (E4.2) and against worker2 :14-:15 and worker4 :27/:30 (both MATCH in worker7).

## S6 cross-block check
This unit is read-only and changes no spec, code or ledger, so no block's behaviour changes. Cross-block facts this index surfaces, recorded without deciding anything:
- Block 2 (strategy, backtests): every recorded Noise-Area result is a Standard-resolution, 1-minute, breaker-less backtest. The judged High-resolution, breakers-on version has not been run (D6 report :56).
- VM / bridge: the 2026-11-13 VM agent is described as "the VM Claude Code session" in `C:\praxis\vm-bridge`. The last VM-agent decision on record names Hermes over SSH (D-2026-11-10-C), and DECISIONS.md:1010 records Amear's ruling on in-VM Claude Code work. The relation between these is not recorded and is not settled here.

## Files staged
None. Nothing was staged (read-only unit; no `git add` run). Files written by this unit (untracked): `docs/reports/2026-11-13-strategy-review-index-manager.md` and `-worker1.md` to `-worker6.md`. A closing note was appended to `-worker1.md`, this unit's own skeleton, by the manager (S13 house style).

## Verification evidence (command output)

All blocks below were run by the manager in this session; worker reports carry their own evidence sections.

### E1.1 2026-11-01 comparison table and CSV re-check
```
$ grep -n '' docs/reports/2026-11-01-three-strategy-results.md | sed -n '400,405p'
400:| run | trades | net | PF | max DD (i) | max DD (ii) | win % | avg trade | largest win | largest win as % of net |
401:|---|---|---|---|---|---|---|---|---|---|
402:| BASELINE (`PraxisNoiseAreaBreakout`, BandOrVWAP) | 1190 | $197327.60 | 1.29 | -$45282.04 | -$45282.04 | 40.67% | $165.82 | $35887.04 | 18.19% |
403:| OPPBAND | 810 | $210182.40 | 1.26 | -$50748.88 | -$50748.88 | 58.02% | $259.48 | $36087.04 | 17.17% |
404:| FLAT1559 | 1190 | $193017.60 | 1.28 | -$40637.04 | -$40637.04 | 40.50% | $162.20 | $36472.04 | 18.90% |
405:| LHMOM (LastHalfHourMomentum) | 1304 | -$76009.84 | 0.84 | -$99806.96 | -$99806.96 | 47.62% | -$58.29 | $3852.04 | -5.07% (not meaningful) |
$ grep -n '' docs/reports/2026-11-01-csv-analyses.md | sed -n '41,44p' | cut -c1-200
41:| R0 | 197327.60 | 1.29 | -45282.04 | 197327.60/1.29/-45282.04 | MATCH |
42:| R1 | 210182.40 | 1.26 | -50748.88 | 210182.40/1.26/-50748.88 | MATCH |
43:| R2 | 193017.60 | 1.28 | -40637.04 | 193017.60/1.28/-40637.04 | MATCH |
44:| R3 | -76009.84 | 0.84 | -99806.96 | -76009.84/0.84/-99806.96 | MATCH |
```

### E1.2 Gate and D6/D7 lines in DECISIONS.md
```
$ grep -n '' DECISIONS.md | sed -n '1735,1740p;1930,1944p'
1735:A4  FLAG 4: Max-DD gate = backtest max drawdown must stay below 80%
1736:    of the ruled limit, i.e. below the lower of 3.2% of the MFFU
1737:    account size and 80% of MFFU's trailing drawdown limit. This
1738:    amends D-2026-11-05-A item 3 with a safety buffer for model error.
1739:    Evaluated against every tier row; tier pick stays Q9. Closes the
1740:    notes-4 DD equity-base item.
1930:D6  FIRST: drawdown viability check, Mac-only, read-only, no VM, no
1931:    purchase. On the three committed 2026-11-01 trade lists, compute
1932:    per-walk-forward-window worst drawdown at 1 MNQ (MFFU MNQ
1933:    commission per cost model v1.2.0), with and without a simulated
1934:    daily-loss cap (breaker #1 at its spec value). Compare to the A4
1935:    ceiling per tier row (80% of the lower of 4% of account and the
1936:    trailing limit). If scripts/wf can regenerate the trade list from
1937:    the 09:30 ET session start (R1), run that too and label it
1938:    UNVERIFIED against NT8. Report: pass/fail per tier at 1 MNQ and
1939:    1 NQ.
1940:D7  If D6 fails at every tier at 1 MNQ: do not design breaker values
1941:    to fit the drawdown ceiling (that is curve-fitting). Report it, and
1942:    pull R6's research (higher-win-rate, steadier-equity strategies)
1943:    forward to P0. The Noise-Area baseline continues through the VM
1944:    tests for the record, but a GO on MFFU is not expected from it.
$ grep -n -o -E 'pulled forward to P0 by Amear.s D-2026-11-08-D D7.{0,120}' DECISIONS.md
2283:pulled forward to P0 by Amear's D-2026-11-08-D D7 (DECISIONS.md:1940–1944) after D6 failed (HANDOFF.md:289 at `c29d08b`: "D6 result → D7 FIRED"). D1: `specs/SPEC_RUBRIC.
$ grep -c -F '1,600' DECISIONS.md
0
```

### E1.3 D6 report lines (f10603a)
```
$ git show --format='%h %ad' --date=short --name-only f10603a | grep -v -E '2026-10-28-f4-|/evidence/'
f10603a 2026-11-09

MANIFEST.md
docs/reports/2026-11-09-d6-drawdown-check-manager.md
$ grep -n '' docs/reports/2026-11-09-d6-drawdown-check-manager.md | sed -n '7p;31p;56p' | sed 's/[Vv]erdict/[V]/g'
7:At 1 micro (MNQ), each of the three strategies had a worst 63-session stretch that fell $2,774 to $2,914 from its high. That stays under the safety ceiling only on the 150K accounts, where the ceiling is $3,600. Smaller accounts fail. If the losing run that carries over from earlier windows is counted, which is the project's committed measure, the worst figure is $4,463 to $5,280. That fails every account size. At 1 full NQ the worst stretch is $26,942 to $28,337, and every account fails. No daily-loss limit value has been written down yet, so the capped run could not be done at a real value. On the committed measure the D7 rule is triggered.
31:| Rapid 50K, Rapid EOD 50K, Pro 50K, Builder 50K | $1,600 | FAIL all | FAIL all |
56:- **Evidence level.** These are COMPUTED figures on NT8 trade lists (OBSERVED inputs) at Standard resolution with no breakers. They are not the judged High-resolution, breakers-on version (values spec :42). They are not tested on the VM. The MNQ figures are derived, not an MNQ run.
```

### E1.4 Walk-forward status (working-tree copy of the WF spec, which shows M in git status) and A20 scope
```
$ grep -n '' STATUS.md | sed -n '195p'; sed -n '5p' docs/specs/2026-11-05-walk-forward-spec.md
195:- T1–T13: none has run. All wait for the VM.
**Status: DERIVED — not yet ruled on as a whole by Amear.** **Changelog.** 2026-11-08, unit `2026-11-08-wf-spec-amendment` (dispatch DECISION_LOG `2026-11-08T16:12:00Z`, WHO: praxis-master): §6 :107, the per-tier table header :113 and the §8 gate line :156 carry A4's 80% buffer (D-2026-11-08-B, DECISIONS.md:1735–1740). The quotes at :31 and :39 are unchanged and carry a pointer at :28. Lines were edited in place; no line was added or removed.
$ grep -n -i -E 'profit factor|net profit|max(imum)? drawdown|trades' docs/reports/2026-10-20-a20-results.md; echo exit=$?
exit=1
```

### E2.1 DECISIONS.md lines on research proposals (re-run by the manager)
```
$ grep -n '' DECISIONS.md | sed -n '360p;368p;383p;1572,1579p;1590p' | cut -c1-400
360:- **R-7zq-3 — third file (answers NEEDS AMEAR 6 above), DECISION_LOG `2026-10-31T11:45:29Z` (WHO: amear):** *"Keep #1 (as built)"* — `PraxisLastHalfHourMomentum` (Baltussen, Da, Lammers & Martens 2021) stands; TORB and ORB remain written specs in the shortlist.
368:## 2026-11-02 — D-2026-11-02-A: R-VN3-1 — `PraxisLastHalfHourMomentum` RETIRED from the active candidate set (retire, not delete)
383:- `PraxisLastHalfHourMomentum` (Baltussen, Da, Lammers & Martens 2021; third file of D-2026-10-31-A) is **removed from the active candidate set**. What that excludes beyond the removal is not ruled here (see NEEDS AMEAR 3).
1572:R6  Research and backtest, on the existing 1-minute data only,
1573:    nothing bought (R-1104-3 stands):
1574:    - Pre-Announcement Drift (Hu, Pan, Wang & Zhu 2022), evening-
1575:      entry variant, exit before the release.
1576:    - Macroeconomic Announcement-Day Premium (Savor–Wilson; Ai 2024).
1577:    Runs in parallel with the walk-forward, not queued behind it.
1578:    Before any build, read MFFU's current T1 news rule and confirm
1579:    whether an evening entry counts as the same trading day.
1590:R9  FOMC-Cycle Even-Week stays parked while trading on MFFU
```

### E2.2 Gemini file: channel backtest order (superseded) and rejected list
```
$ grep -n '' docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md | sed -n '28p;30p;74p' | cut -c1-500
28:## 3. Channel recommendation (the channel's, not an Amear ruling; master decides under D1)
30:Backtest order: (1) PraxisLastHalfHourMomentum, already written; (2) Candidate 1 VWAP mean reversion; (3) Candidate 2 opening-gap fade; Candidate 4 parked. Measure the real carried drawdown gate at 1 MNQ on each trade list, and test a mean-reversion + momentum combination. The channel also recommended to Amear that `ckh` be resumed and that strategy research take priority over further planning-document units; Amear has not ruled on that in this chat.
74:Already rejected (do not re-propose without new post-2020 evidence): pre-FOMC drift; trading the macro release itself; post-earnings drift; short volatility; single-instrument CTA trend; unfiltered opening range breakout; FOMC even-week cycle; overnight drift held across the 16:00-18:00 close; any strategy that holds through a Tier 1 release.
```

### E2.3 Kimi file: C1 VWAP lines
```
$ grep -n '' docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md | sed -n '20p;68p;81p;85p' | cut -c1-300
20:4. Gap fade (C2), VWAP (C1), London close (C4) and new C6 rated low; C4 and C6 dropped. Agreed.
68:C1. Volatility-Weighted VWAP Mean Reversion
81:Post-2018 evidence: None found. We are not aware of any academic test of this exact VWAP+volatility band strategy on NQ or other indices. VWAP-based reversion is plausible but not established in lit. Without published results, we must “measure in backtest.” No published decay info.
85:Fit: Low. The profile is low win rate. It relies on sharp reversal moves (rare), likely with lopsided risk. The prior analysis suggests baseline expectancy <0 (before extreme tuning). No strong literature support. Mechanism (mean reversion to VWAP) may be crowded or arbitraged. Given no evidence 
```

### E2.4 Gemini/Kimi named in DECISIONS.md
```
$ grep -n -i -E 'gemini|kimi' DECISIONS.md | wc -l
       0
```

### E3.1 Noise-Area VWAP exit and arm (b) ATR status
```
$ grep -n '' ninjascript/PraxisNoiseAreaBreakout.cs | sed -n '34p;46p;87p;118p'
34://     multiplier as a tunable), NO ATR stop. The ONLY selectable knob is the exit form (ExitMode).
46:	// BandOrVWAP = paper's PREFERRED model, trailing stop at max/min(band, VWAP) (§4 p.13). DEFAULT.
87:		// Session-anchored VWAP (spec §4 p.13, footnote 2: RTH data only, anchored at 09:30 open).
118:				ExitMode      = PraxisNoiseExitMode.BandOrVWAP; // spec §4 p.13 — paper's PREFERRED exit. The only knob.
$ grep -n '' STATUS.md | sed -n '192p;194p' | cut -c1-300
192:- Arm (b): `.cs` WRITTEN only — not compiled, not run; on `arm-b/wf-tunables` only (`18:12:00Z`). There is no C# compiler on the Mac (`16:04:00Z`).
194:- Oracles: WRITTEN + TESTED on synthetic fixtures (59 tests); values COMPUTED on the real file at both session starts; UNVERIFIED against NT8 arm (b); the fit to the 2026-11-01 base runs is OBSERVED for the m = 0 band/VWAP/policy part only (`21:42:00Z`, "Level accepted").
```

### E3.2 Zero-hit oscillator and average terms, tracked files plus Redemtion text (manager re-run)
```
$ for t in 'moving average' RSI MACD Keltner ADX stochastic supertrend 'cumulative delta' ichimoku donchian; do printf '%s: ' "$t"; { git grep -i -w -h -e "$t" -- . ':!docs/reports/2026-11-13-strategy-review-index-*' ':!docs/reports/2026-10-28-f4-*'; find Redemtion -name '*.rtf' -exec textutil -convert txt -stdout {} \; ; find Redemtion \( -name '*.md' -o -name '*.txt' \) -exec cat {} \; ; } 2>/dev/null | grep -i -w -c -e "$t"; done
moving average: 0
RSI: 0
MACD: 0
Keltner: 0
ADX: 0
stochastic: 0
supertrend: 0
cumulative delta: 0
ichimoku: 0
donchian: 0
```

### E3.3 Redemtion exclusion row for VWAP/Bollinger and ORB
```
$ grep -r -n -h -E 'Standalone VWAP/Bollinger reversion on NQ|5-Minute Opening Range Breakout on NQ \(standalone\)|Order-flow imbalance' Redemtion --include='*.md' | cut -c1-200
38:| 5-Minute Opening Range Breakout on NQ (standalone) | **ELIMINATED** — no robust standalone edge on NQ without filters | Multiple replications |
45:| Order-flow imbalance / deep-OFI | **EXCLUDED** — 2-price-change horizon, requires co-location | Kolm-Turiel-Westray 2023 |
47:| Standalone VWAP/Bollinger reversion on NQ | **EXCLUDED** — no peer-reviewed NQ evidence post-2018 | — |
```

### E4.1 Line counts of the two channel files
```
$ wc -l docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md
      54 docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md
      44 docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md
      98 total
```

### E4.2 vm-queue lines cited in Q4 and Q5
```
$ grep -n '' docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md | sed -n '5p;11p;13,17p;20,23p;27,31p;33,36p;40,43p'
5:Source: the VM Claude Code session's own report, pasted to this channel by Amear at 14:37 ET (REPORTED BY Amear; the channel has not read the VM repo). The VM agent is the session working in `C:\praxis\vm-bridge` on the Windows VM. It is not praxis-master. Its results and commits live in that local git repo (no remote), with result files at `results\T1.json`, `results\T2.json`, `results\T3.json`. They are not in Praxis.build.
11:Setup: Strategy Analyzer tab "PRAXIS baseline NQCONTROW 0930", PraxisNoiseAreaBreakout, NQCONTROW SEP25, 1-minute, 2021-03-08 to 2026-07-17, CME US Index Futures RTH 0930 ET, commission PRAXIS $2.96 round trip, slippage 2, Standard fill resolution, 1 NQ.
13:| Run | ExitMode | Trades | Net | Profit factor | Max drawdown | vs T1 reference (Amear's hand run) |
14:|---|---|---|---|---|---|---|
15:| T1 | BandOrVWAP | 1,173 | $176,392.92 | 1.2615 | -$38,905.64 | Exact match |
16:| T2 | OppBand | 1,112 | $188,618.48 | 1.2861 | -$37,906.24 | -61 trades, +$12,225.56 net, DD $999.40 smaller |
17:| T3 | BandOrVWAP | 1,173 | $176,392.92 | 1.26 | -$38,905.64 | Identical to T1 trade by trade (request id excepted); same file size, 219,831 bytes |
20:- **ExitMode (an enum) is applied by the bridge:** `bridge.log` shows `param set: ExitMode="OppBand"` for T2, and T2's result differs from T1. The open question in the VM handoff ("T2 may equal T1 if the enum is not applied") is closed.
21:- **The tab state is restorable:** T3 reproduced T1 exactly after T2, so a parameter change is cleanly overwritten. The tab was left at BandOrVWAP, 1 contract.
22:- **No connection changes during any run:** no connect or disconnect lines in `bridge.log` while T1, T2 or T3 ran.
23:- **Commission not compared:** the bridge's result files carry no commission total, so the hand run's $3,472.08 could not be checked.
27:1. **First T1 attempt stopped, nothing ran:** NT8 had no Strategy Analyzer window open. Amear opened the tab by hand; the VM agent treated his explicit go as a new T1 run, not a retry, logged his words, and re-ran the pre-send checks.
28:2. **NT8 restarted at 12:32:48 PM** (new process, PID 11820), between the two T1 attempts. Its startup reloaded the AddOn and connected the Sim feed (six new `bridge.log` lines), before any request was sent. The VM agent judged this normal startup, not a bridge action and not a breach of the "no connection lines during a run" rule, and logged it. **Who or what restarted NT8 is not stated in the report** (open).
29:3. **`run-queue.ps1` was not used:** it needs the `claude` command, which is not installed on the VM. The VM agent ran the three tasks itself, one at a time, as the script's own fallback allows.
30:4. **`tools\send-backtest.ps1` was changed:** extended so it can pass strategy parameters. It worked for all three runs.
31:5. Timestamps are consistent with the VM clock now being correct: bridge.log 17:36:47 UTC for the T1 send, against Amear's report of a correct taskbar clock at about 12:27 ET (INFERRED by the channel).
33:## 3. What this means (the channel's reading, INFERRED, not a ruling)
34:
35:- **The bridge works for headless backtests:** it reproduces a hand run exactly, applies parameters including enums, and leaves the tab restorable. That is the infrastructure result of the day. Walk-forward still needs the optimizer command, which is not allowed yet.
36:- **These are Noise-Area numbers, kept for the record only** (D7 after the D6 drawdown check). T2's better net does not change that: at 1 MNQ its max drawdown would be about $3,790 (one tenth of $37,906.24), above the 50K gate of $1,600. Not a candidate.
40:1. **MFFU commission re-run:** Amear sets both PRAXIS commission rows to 2.34 by hand ($4.68 round trip); the VM agent then re-sends T1's parameters. Expected: 1,173 trades, net about $174,375.36 (channel check: 1,173 x $1.72 extra per round trip = $2,017.56 less than $176,392.92, which matches).
41:2. **Sim feed check:** the VM agent still lists "check in the Control Center whether the Sim feed cycled when the AddOn loaded yesterday." Amear reported today (voice, about 12:30 ET) that he looked and saw no disconnect or reconnect. Whether today's Control Center view covers yesterday's load is not confirmed.
42:3. **Later, not today:** Analyzer tabs for `PraxisNoiseAreaBreakout_Flat1559` and `PraxisLastHalfHourMomentum`, set by hand or via the bridge's `satemplate` command (needs Amear's OK). Channel note: `PraxisLastHalfHourMomentum` is retired (D-2026-11-02-A; session-close handoff section 2), so its tab is not needed unless Amear says otherwise.
43:4. **Open:** what restarted NT8 at 12:32 PM.
```

### E4.3 vm-bridge mentions across the repo (excluding .git, .claude, this unit and the F4 reply-filing files)
```
$ grep -r -n -i -E 'vm-bridge|vm_bridge|vmbridge' --exclude='2026-10-28-f4-*' --exclude-dir=evidence --exclude-dir=.git --exclude-dir=.claude --exclude='2026-11-13-strategy-review-index-*' . | cut -c1-160
DECISION_LOG.md:939:- [2026-11-13T20:36:45Z] WHO: praxis-master | WHAT: **Unit 2026-11-13-research-filing COMMITTED `9ff8a48`, pushed (`main` = `origin/main` = 
docs/reports/2026-11-13-research-filing-resume-manager.md:284:2026-11-13-return-handoff-claude-ai-vm-queue-results.md:5:C:\praxis\vm-bridge
docs/reports/2026-11-13-research-filing-resume-manager.md:321:False positives, with reason: the IPv6-pattern hits are clock times (kimi :69 "15:30:" in a rule w
docs/reports/2026-11-13-research-filing-resume-manager.md:667:LC_ALL=C grep -c $'\v' docs/reports/2026-11-13-research-filing-resume-manager.md; grep -c -F 'C:\p
docs/reports/2026-11-13-research-filing-worker2.md:305:2026-11-13-return-handoff-claude-ai-vm-queue-results.md:5:C:\praxis\vm-bridge
docs/reports/2026-11-13-research-filing-worker2.md:339:2026-11-13-return-handoff-claude-ai-vm-queue-results.md:5:C:\praxis\vm-bridge
docs/reports/2026-11-13-research-filing-resume-worker2.md:30:- False positives, with reasons: IPv6-pattern hits kimi :69 (`15:30:`, a rule time window), vm-queu
docs/reports/2026-11-13-research-filing-resume-worker2.md:311:2026-11-13-return-handoff-claude-ai-vm-queue-results.md:5:C:\praxis\vm-bridge
docs/reports/2026-11-13-research-filing-resume-worker1.md:37:- Drive path: vm-queue :5 "C:\praxis\vm-bridge". It is a repo folder on the Windows VM with no user
docs/reports/2026-11-13-research-filing-resume-worker1.md:322:docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md:5:C:\praxis\vm-bridge
docs/reports/2026-11-13-research-filing-resume-worker1.md:341:docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md:5:vm-bridge
docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md:5:Source: the VM Claude Code session's own report, pasted to this channel by Amear at 14:37
docs/reports/2026-11-13-research-filing-worker1.md:63:2026-11-13-return-handoff-claude-ai-vm-queue-results.md:5:C:\praxis\vm-bridge
$ mdfind -name vm-bridge | wc -l
2026-11-13 15:40:36.634 mdfind[82191:246677] [UserQueryParser] Loading keywords and predicates for locale "en_CA"
2026-11-13 15:40:36.635 mdfind[82191:246677] [UserQueryParser] Loading keywords and predicates for locale "en"
       0
```

### E4.4 VM artefact names and send-backtest/run-queue mentions
```
$ git ls-files | grep -i -E 'send-backtest|run-queue|bridge\.log|T[123]\.json|RESULTS\.md|QUEUE\.log'
docs/reports/2026-10-20-a20-results.md
docs/reports/2026-11-01-three-strategy-results.md
docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md
(the three hits are case-insensitive "results.md" name matches, not VM files)
$ grep -r -l -E 'send-backtest|run-queue' --exclude='2026-10-28-f4-*' --exclude-dir=evidence --exclude-dir=.git --exclude-dir=.claude --exclude='2026-11-13-strategy-review-index-*' .
docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md
```

### E4.5 Newest vm/replies files and last commits touching vm/
```
$ ls vm/replies | sort | tail -3
20261111T172933Z-python-git-install.md
20261111T172940Z-STATUS.md
README.md
$ git log --format='%h %ad' --date=short -- vm/ | head -3
ee54344 2026-11-11
85a803f 2026-11-11
7f3590e 2026-11-09
```

### E4.6 DECISION_LOG and DISPATCH_LOG rows of 2026-11-12/13 naming VM-side run artefacts
```
$ grep -n -E '^- \[2026-11-1[23]T' DECISION_LOG.md DISPATCH_LOG.md | grep -E 'send-backtest|run-queue|bridge\.log|vm-bridge|T1\.json|OppBand|BandOrVWAP|AddOn' | cut -c1-60
DECISION_LOG.md:905:- [2026-11-13T09:09:00Z] WHO: praxis-mas
DECISION_LOG.md:939:- [2026-11-13T20:36:45Z] WHO: praxis-mas
$ sed -n 905p DECISION_LOG.md | grep -o -E '.{60}OppBand.{60}'
 without-series records only" is unchecked; those runs were OppBand/Flat1559/LH variants whose exits are not the "16:00 session
(row 939 is the authority row for this unit)
```

### E4.7 DECISIONS.md: VM agent entries
```
$ grep -n -i -E 'vm-bridge|VM Claude Code' DECISIONS.md | cut -c1-40
1010:- **Item 2 — in-VM automation.** Th
(end; zero lines above means no hit)
$ grep -n -E '^## .*D-2026-11-1[01]-[BC]:' DECISIONS.md
2047:## 2026-11-10 — D-2026-11-10-B: live-signal topology adopted as the working design (rubric F1; bead Praxis_build-1hv)
2076:## 2026-11-10 — D-2026-11-10-C: VM agent = Hermes over SSH (settlement 3 changed; master under D1)
2176:## 2026-11-11 — D-2026-11-11-B: VM handoff §1 limit 9 lifted by Amear for one install; Python 3.12.10 and git 2.56.0 (ARM64) installed in the VM. Record only. Filed WHO: amear, REPORTED BY the Claude.ai channel.
$ grep -n -o -F 'No more Cowork or in-VM Claude Code executor work.' DECISIONS.md; grep -n -o -F 'lifted COMPLETELY once two tests pass' DECISIONS.md
1010:No more Cowork or in-VM Claude Code executor work.
1003:lifted COMPLETELY once two tests pass
1010:lifted COMPLETELY once two tests pass
1091:lifted COMPLETELY once two tests pass
1264:lifted COMPLETELY once two tests pass
```

### E4.8 Downloads copy vs filed copy (outside repo)
```
$ diff docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md ~/Downloads/2026-11-13-return-handoff-claude-ai-vm-queue-results.md | sed 's/Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks\/side slippage assumed\./[the S13 sentence]/'
44a45
> [the S13 sentence]
```

### E5.1 bd show Praxis_build-ckh
```
$ bd show Praxis_build-ckh
○ Praxis_build-ckh · R6 research P0 under D7: Pre-Announcement Drift and Announcement-Day Premium on existing 1-minute data, own worktree, nothing bought   [● P0 · OPEN]
Owner: Amear Bani-Ahmad · Type: task
Created: 2026-11-09 · Updated: 2026-11-12

DESCRIPTION

  D-2026-11-08-D D7 fired on D6 (f10603a): at 1 MNQ the three 2026-11-01      
  strategies fail every MFFU tier on the committed values-spec per-window     
  drawdown measure. D7 pulls R6 (D-2026-11-08-A R6, DECISIONS.md:1572-1579)   
  forward to P0. Scope per R6: existing 1-minute data only, nothing bought (R-
  1104-3); runs in parallel with the walk-forward in a separate git worktree  
  on its own branch (R7, v6y); before any build read the MFFU T1 news rule and
  whether an evening entry counts as the same trading day. Noise-Area baseline
  continues through VM tests for the record (D7).                             



NOTES

  2026-11-12 PARKED (absolute park rule, audit-fail-x2): step 2 S4 entry D-   
  2026-11-12-B on parked/Praxis_build-ckh @ 9bf0516 (pushed). FAIL 1 S1       
  manager report :24/:72/:179 (cured by Correction 1). FAIL 2 S1 in original  
  adversary report worker1 :156 placeholder arg, output cut with ... at :133- 
  :314, :154 unpasted claim. A human resumes; cure recipe in HANDOFF top card 
  and DECISION_LOG 09:44:01Z/09:53:00Z. No R6 code exists.                    



```

### E5.2 HANDOFF.md top card, lines 12-22 (working copy; `git diff --quiet HEAD -- HANDOFF.md` exits 1, see E6.1)
```
$ grep -n '' HANDOFF.md | sed -n '12,22p' | cut -c1-330
12:**Next, in order (decided by master under D1; one manager at a time):**
13:1. Human: resume or rule on `ckh` (cure in the 2026-11-12 09:01Z card below, unchanged).
14:2. Broker route: MFFU does not offer Rithmic; D-2026-11-10-B is contradicted and not re-decided. One short entry deciding under D1, or naming the D2 item if a purchase or account is involved.
15:3. OPEN-T1 VM-to-webhook check (needs the VM; Amear's hands for any VM step).
16:4. Rest of bead `fgd`: F-4/F-5 wait on parked `diq`; F-6 optional; F-8 not edited; residuals OPEN-F2-1 and the lockout/4:10-alert overlap.
17:
18:**Brief lessons (OBSERVED this run; bd memory `master-brief-rule-conflicts`):** two manager returns carried three faults in the master's own briefs: (1) a rule conflict, "no person name" vs "paste the full entry" (ruled: the rule is for third parties; the owner's name is fine); (2) not a rule conflict: a master-dictated MANIF
19:
20:**Questions that are Amear's (unchanged; DECISION_LOG 2026-11-12T13:01:49Z item b):** (1) does MFFU's 2026-11-11T22:41:33Z point 4 close R6 OPEN-1; (2) should F4's bar change.
21:
22:**For Amear's hands (not questions):** the decision on `ckh`; D2 items unchanged (Sim-only guard change before any live path; SSH keys for a VM-to-n8n tunnel; any purchase; approved values for breakers #2/#3 once real money is at stake).
```

### E5.3 session-close lines cited
```
$ grep -n '' docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md | sed -n '18,22p;26p;28,37p;48,53p'
18:Files 1 and 2 recommend backtesting `PraxisLastHalfHourMomentum` first. **Withdrawn.** The channel missed that it was already tested and retired:
19:- 2026-11-01 hand-test run, 1 NQ (NQCONTROW SEP25), $2.96 round-trip commission, 2 ticks/side slippage: 1,304 trades, net -$76,009.84, PF 0.84, max DD -$99,806.96, win rate 47.62%, average trade -$58.29 (`docs/reports/2026-11-01-three-strategy-results.md`, comparison table; re-checked MATCH in `docs/reports/2026-11-01-csv-analyses.md`).
20:- Retired by Amear's ruling R-VN3-1, filed as D-2026-11-02-A (bead `Praxis_build-afe`, closed). Retire, not delete.
21:- INFERRED by the channel: at 1 NQ, costs are about $23 a trade ($2.96 commission + 4 ticks x $5 slippage), so an average trade of -$58.29 means it lost roughly $35 a trade BEFORE costs. Costs are not the reason it failed.
22:- The channel saw no flaw flagged against that test in the records it read. **Do not re-run it unless a record shows a flaw in the 2026-11-01 test.**
26:Two deep-research runs (Gemini, then Kimi) were asked for a steady, high-win-rate intraday NQ strategy that survives an MFFU trailing drawdown at 1 MNQ. **Neither found a viable new candidate.** Status of everything they proposed:
28:| Candidate | Status | Why |
29:|---|---|---|
30:| Last-half-hour momentum (Baltussen, Da, Lammers & Martens 2021, JFE 142:377-403) | TESTED, RETIRED (D-2026-11-02-A) | Lost money on NQ 2021-2026, before and after costs (section 2). The paper's results are for diversified baskets, 1974-2020. |
31:| First-to-last half-hour momentum with a +/-0.30% threshold (Gao, Han, Li & Zhou 2018, JFE) | NOT TESTED; deprioritised | Same mechanism as the retired strategy above; the threshold filter is the only difference. Test only with a stated reason to expect a different result. |
32:| Opening gap fade (0.35%-1.50% gap, target prior close) | NOT TESTED; low | Both runs: near break-even at best; Kimi cites practitioner sources only. Limit-order target and intrabar stop fill optimistically on 1-minute bars. |
33:| VWAP sigma-band mean reversion | NOT TESTED; low | No source found ("Dean & Francis 2026" could not be identified and was withdrawn). Negative after costs at the proposer's own baseline. |
34:| London-close reversal (10:30-11:15 fade) | DROPPED | Mechanism borrowed from an FX fixing paper; no equity-index evidence. |
35:| Opening 30-minute momentum (Kimi's new C6) | DROPPED | Kimi's own cited evidence (Grant et al. 2005) points the other way. |
36:
37:Also ruled out in earlier work and restated by both runs: pre-FOMC drift; trading the release itself; post-earnings drift; short volatility; single-instrument CTA trend; unfiltered opening range breakout; FOMC even-week cycle; overnight drift held across 16:00-18:00; anything holding through a Tier 1 release. Noise-Area breakout and its variants fail the D6 drawdown check (`f10603a`).
48:- **MFFU email:** follow-up sent 2026-11-13 17:26Z in the pre-purchase thread, addressed to the human rep who answered on 11-12. It asks for (1) a written yes/no that unattended automated trading is permitted on Evaluation and Sim Funded (Rapid, Pro, Builder), and (2) whether "Builder Plans" in the news policy includes Builder Sim Funded. No reply yet at filing.
49:- **VM clock:** Amear checked about 12:27 ET and reported the VM taskbar time matched real time. The earlier "55m43s fast" reading is unconfirmed. Nothing was changed.
50:- **NT8 Sim connection:** Amear looked at the Control Center and reported no disconnect or reconnect.
51:- **VM bridge queue:** Amear reported (about 14:30 ET) that the VM code agent has finished. The channel has NOT seen RESULTS.md, QUEUE.log or LOG.md and states nothing about the results. T1 reference: hand run 1,173 trades, net $176,392.92, PF 1.26, max DD $38,905.64, commission $3,472.08. If T2 (ExitMode=OppBand) equals T1 exactly, the bridge may not have applied the enum.
52:- **Still waiting on Amear (unchanged):** a ruling on parked `ckh` (the channel recommended resuming it; Amear has not ruled); his two questions (does MFFU's reply close R6 OPEN-1; should F4's bar change). D2 items unchanged.
53:- **Amear asked when PRAXIS can go live.** The channel's answer (an estimate, not a decision): not this year; the critical path is finding a strategy that passes the drawdown gate, and this research did not find one.
```

### E5.4 Related bead headers
```
$ bd show Praxis_build-fx4 | sed -n '1,3p'
○ Praxis_build-fx4 · MFFU automation-compliance: confirm in writing that fully-automated trading is permitted before any live step   [● P1 · OPEN]
Owner: Amear Bani-Ahmad · Type: task
Created: 2026-07-25 · Updated: 2026-11-10
$ bd show Praxis_build-diq | sed -n '1,3p'
○ Praxis_build-diq · PARKED: wf-spec-amendment (values spec v2.2 + WF spec A4) - audit FAIL 2, absolute park rule fired   [● P1 · OPEN]
Owner: Amear Bani-Ahmad · Type: task
Created: 2026-11-08 · Updated: 2026-11-08
$ bd show Praxis_build-qtk | sed -n '1,3p'
○ Praxis_build-qtk · Dev-D no-optimization-first-pass vs WFE>=0.50: define the replication-arm gate set + where GO/HOLD/REJECT sits   [● P2 · OPEN]
Owner: Amear Bani-Ahmad · Type: task
Created: 2026-07-25 · Updated: 2026-07-25
$ bd show Praxis_build-q36 | sed -n '1,3p'
○ Praxis_build-q36 · 0-S on NQCONTROW SEP25 gives 1,190 trades (556 L / 634 S) vs retired run 4's 1,211 (584/627) on the Stock row — explain the difference   [● P2 · OPEN]
Owner: Amear Bani-Ahmad · Type: task
Created: 2026-10-31 · Updated: 2026-10-31
$ bd show Praxis_build-afe | sed -n '1,3p'
✓ Praxis_build-afe · R-VN3-1: PraxisLastHalfHourMomentum retired from the active candidate set (retire, not delete)   [● P2 · CLOSED]
Owner: Amear Bani-Ahmad · Type: task
Created: 2026-11-02 · Updated: 2026-11-02
```

### E5.5 Open beads list (strategy-adjacent lines)
```
$ bd list --status open | grep -E 'ckh|fx4|diq|qtk|q36|ajj|b5z|fgd|2nh'
○ Praxis_build-ckh ● P0 R6 research P0 under D7: Pre-Announcement Drift and Announcement-Day Premium on existing 1-minute data, own worktree, nothing bought
○ Praxis_build-2nh ● P1 live-signal-emission topology for the anchor strategy + breaker placement in the order path
○ Praxis_build-diq ● P1 PARKED: wf-spec-amendment (values spec v2.2 + WF spec A4) - audit FAIL 2, absolute park rule fired
○ Praxis_build-fx4 ● P1 MFFU automation-compliance: confirm in writing that fully-automated trading is permitted before any live step
○ Praxis_build-ajj ● P2 b2-mc: Monte Carlo engine on pooled OOS trades, emit envelope distributions
○ Praxis_build-b5z ● P2 [bug] Import-file volume anomaly: 2021-03-08 RTH volume 4,322 (342 bars; 10:00 bar vol 8) vs 2026-07-17 RTH 284,681 (292 bars), ~66x — bears on D-2026-07-17-A volume-crossover 
○ Praxis_build-fgd ● P2 F2 amendment S6 follow-ups F-1..F-9: specs/code still citing 11:30 close or 15:00-18:00 disable (topology :41/:48/:62/:74/:86, Noise-Area ruleset :8/:79/:84/:99/:105, WF values
○ Praxis_build-q36 ● P2 0-S on NQCONTROW SEP25 gives 1,190 trades (556 L / 634 S) vs retired run 4's 1,211 (584/627) on the Stock row — explain the difference
○ Praxis_build-qtk ● P2 Dev-D no-optimization-first-pass vs WFE>=0.50: define the replication-arm gate set + where GO/HOLD/REJECT sits
```


### E6.1 Re-checks behind the round-1 fixes
```
$ grep -n -o -E 'R-VM-6.{0,40}' DECISION_LOG.md
630:R-VM-6); the count difference is NOT a blocker
647:R-VM-6 from the 14:59:37Z row) | APPROVED BY: 
647:R-VM-6 RULED: "Stands — retire the stock-row r
649:R-VM-6, implicit in the notes, recorded as ope
649:R-VM-6 stays his. | STATE: closed — ruled; nex
$ grep -c 'R-VM-6' DECISIONS.md
0
$ grep -n '' docs/reports/2026-10-30-run3-backtest-screenshot-record.md | sed -n '103p' ; grep -n -o -F 'recorded as INVALID' docs/reports/2026-10-30-run3-backtest-screenshot-record.md
103:## Addendum 2026-10-30T22:40Z — RUN 3 RULED INVALID by Amear; run 4 supersedes it (REPORTED)
107:recorded as INVALID
$ grep -n -o -F 'The Noise-Area baseline continues through the VM tests for the record' docs/reports/2026-11-09-d6-drawdown-check-manager.md DECISIONS.md
DECISIONS.md:1981:The Noise-Area baseline continues through the VM tests for the record
docs/reports/2026-11-09-d6-drawdown-check-manager.md:45:The Noise-Area baseline continues through the VM tests for the record
$ grep -n -o -F 'Noise-Area baseline continues' DECISIONS.md | wc -l; grep -n -i -E '(OppBand|Flat1559).{0,80}for the record' DECISIONS.md | wc -l
       2
       0
$ git diff --quiet HEAD -- HANDOFF.md; echo exit=$?
exit=1
```

Result: PASS

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
