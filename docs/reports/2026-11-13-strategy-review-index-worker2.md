# 2026-11-13 strategy-review-index — worker2 (Q2: index of strategy-research runs)

## Task
- Unit `2026-11-13-strategy-review-index`, worker2. Mode: BUILD (read-only research). HEAD `9ff8a48`, branch `main`. Authority: DECISION_LOG last row 2026-11-13T20:36:45Z (per brief; not re-read by this worker).
- Q2: index every strategy-research run in the record. For each run: date, who ran it, what it proposed (with file:line), and what happened to each proposal (TESTED / BUILT-NOT-TESTED / SPECIFIED / DROPPED / NOT TESTED, no record). Also flag proposals that appear in more than one run.
- Only file written: this report. No git staging, no edits to existing files. Every E-number below points to pasted command output in the Evidence section.
- Status words are not upgraded. "Ranked/passed by a research run" is not "tested". Only a recorded trade list counts as TESTED, and only `ninjascript/*.cs` counts as BUILT.
- Gitignored sources: everything under `Redemtion/` is gitignored (E0 shows `.gitignore:7:Redemtion/`). Runs R1–R3 below exist only in those untracked files. The tracked record cites them through `docs/reports/2026-11-08-strategy-filter-audit.md`, which names them D2, D4, D6 and D8.

## Research runs table

| ID | Date | Who ran it (model/channel) | Scope | Source file(s) | Evidence |
|---|---|---|---|---|---|
| R1 (D2) | Undated in the text; the file sits in `Redemtion/Intitialization-April 2026/` (folder name only) | **NOT IN RECORD.** 0 model-name hits in the text (E15) | NQ/ES strategy shortlist with behavioural screening | `Redemtion/Intitialization-April 2026/Verified Trading-Strategy Shortlist for NQ : Index Futures.rtf` | E1, E15 |
| R2 (D8) | Undated in the text; same folder | **NOT IN RECORD.** 0 model-name hits (E15) | Higher-frequency NQ strategies to pair with Noise-Area | `Redemtion/Intitialization-April 2026/Systematic, Higher-Frequency NQ Strategies to Pair with the Noise-Area Breakout .rtf` | E2, E15 |
| R3 (D4 prompts, D6 compiled) | Prompts: "**Generated:** May 6, 2026". Compiled: "**Date:** May 6, 2026" | Three agents. The prompt file's instruction says "Paste each prompt into a separate Claude deep research session" (E3). That is the instruction, not proof of what was run. The `compass_artifact_*` file names are UNVERIFIED as Claude output | Commodities, FX, and multi-session/cross-instrument; NQ/ES resolved list carried in as "do not duplicate" | `Redemtion/Research Prompts/PRAXIS_Phase2_Expanded_Strategy_Search_3Agent_Prompts.md`; `Redemtion/Research Results/PHASE_2_STRATEGY_DECISION_Compiled_Round_3.md`; `Redemtion/Research Results/Round 3/` (3 files) | E3, E4 |
| R4 (7zq M2) | 2026-10-31 | Claude Code: `Praxis_build-7zq` M2 worker 1 (research) under praxis-manager | Three published NQ-applicable intraday strategies, excluding Noise-Area | `docs/reports/2026-10-31-7zq-m2-shortlist.md`, `-7zq-m2-worker1-research.md`, `-7zq-m2-new-strategy.md` | E6 |
| R5 (research set A/B/C) | Reports dated 2026-11-04; landed in `84b1a58` (author date 2026-11-06) | Claude Code (Mac). praxis-master compiled the voice summaries | Tick data (A), comparable public builds (B), proof-of-concept standard (C). **No new strategy was proposed.** B surveyed public code: one Noise-Area NinjaScript implementation, plus an ORB repo listed as reference code (E8, E20) | `docs/reports/2026-11-04-tick-data-sources.md`, `-comparable-builds.md`, `-proof-of-concept-standard.md`, `-research-compiled-for-voice.md`, `-v2.md` | E8, E20 |
| R6 (strategy filter audit) | 2026-11-08 | "Claude.ai Praxis channel (research agent), at Amear's brief" (E9) | Re-read of D1–D8 to find strategies dropped for manual-trading reasons. Proposed two re-evaluations | `docs/reports/2026-11-08-strategy-filter-audit.md` | E9, E18 |
| R7 (Gemini) | 2026-11-13 ~13:00 ET (REPORTED BY the Claude.ai channel) | Amear ran Gemini Deep Research. The Claude.ai channel audited the output and filed it | Steady daily NQ/MNQ strategy that survives an MFFU trailing drawdown at 1 MNQ | `docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md` (Appendix A) | E10 |
| R8 (Kimi) | 2026-11-13; output supplied 14:26 ET (REPORTED BY the channel) | Amear ran Kimi Deep Research on the brief the channel wrote (Gemini handoff Appendix B). The channel audited the output | Verify R7's four candidates and add 2–4 new ones | `docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md` (Appendix A) | E11 |

Excluded as non-strategy research (no strategy proposals): Rounds 1–2 (`Redemtion/Research Results/PHASE_2_INPUT_COMPILED_Round_1_and_2.md`, infrastructure); the a20 Kinetick reports (data feed); `docs/reports/2026-08-07-f3-fill-resolution-research-UNGRADED.md` (fill resolution); `docs/reports/2026-11-08-voice-strategy-brief.md` (a status brief; the only strategy hit is the baseline's drawdown, E17). No `docs/research` directory exists (E13, last command: exit=1).

## Proposal fate table

Fate key: **TESTED** = a recorded trade list exists. **BUILT-NOT-TESTED** = a `.cs` file exists with no recorded run. **SPECIFIED** = a written rule set or design exists, with no code. **DROPPED** = removed by a ruling or by the run itself (reason quoted). **NOT TESTED** = no build or test in the record.

| # | Proposal | Proposed in (file:line) | Fate | Evidence |
|---|---|---|---|---|
| 1 | Noise-Area intraday momentum breakout (Zarattini–Aziz–Barbon) | R1 D2 RTF:23 (Strategy #1); R3 prompts:31 "**SELECTED** as baseline" | **TESTED.** Baseline 1190 trades, PF 1.29 (three-strategy-results:402). Variants OppBand (810, PF 1.26) and Flat1559 (1190, PF 1.28) also TESTED (:403–404). Session close, line 37: "Noise-Area breakout and its variants fail the D6 drawdown check (`f10603a`)". This worker did not open `f10603a`'s report; that D6 result is cited, not re-checked | E7, E19 |
| 2 | FOMC-Cycle Even-Week long bias (Cieslak et al.) | R1 D2:52; R3 prompts:32 PARKED | **NOT TESTED; parked by ruling.** DECISIONS.md:1590 "R9  FOMC-Cycle Even-Week stays parked while trading on MFFU" | E1, E3, E9 |
| 3 | Pre-Announcement Drift NFP/ISM/GDP (Hu, Pan, Wang & Zhu 2022) | R1 D2:80; R3 prompts:33 PARKED; R6 filter-audit:177 (evening-entry variant, PROPOSED) | **SPECIFIED.** Ruled for research under R6 (DECISIONS.md:1572–1574). Design exists on branch `r6/announcement-research` (`bf6fcc7`). Topology spec:20 says "no strategy code" and grades it SPECIFIED. Bead `Praxis_build-ckh` is OPEN | E9 |
| 4 | Macroeconomic Announcement-Day Premium (Savor–Wilson; Ai 2024) | R1 D2:113; R3 prompts:34 "RETAINED as manual fallback only"; R6 filter-audit:184 | **SPECIFIED.** Same R6 ruling (DECISIONS.md:1576), same branch, design and open bead. The topology spec row quoted in E9 names only Pre-Announcement Drift. That this design also covers Savor–Wilson rests on the `bf6fcc7` subject line ("PROPOSED research design for Pre-Announcement Drift and Announcement-Day Premium") | E9 |
| 5 | 5-min ORB on "Stocks in Play" (Zarattini–Barbon–Aziz 2024) | R1 D2:141 | **NOT TESTED.** Not pursued by any ruling found. Filter-audit row "ORB on Stocks in Play (D2 #5)": not routable via MFFU futures (A9) | E1, E21 |
| 6 | Last-Half-Hour Hedging-Demand Momentum `η(r_ROD)` (Baltussen, Da, Lammers & Martens 2021) | R2 D8:29 (Strategy A); R3 prompts:35 PASSED; R4 shortlist:11 (#1, Pick); R8 Kimi:167 (New C5) and rank 1 at :314 | **TESTED, then DROPPED.** Built as `ninjascript/PraxisLastHalfHourMomentum.cs`. Run 2026-11-01: 1304 trades, net -$76009.84, PF 0.84 (three-strategy-results:405). Retired by D-2026-11-02-A, DECISIONS.md:383: "is **removed from the active candidate set**". Bead `Praxis_build-afe` CLOSED | E6, E7 |
| 7 | Threshold-conditioned first-half-hour momentum (Rosa 2022, TC-FHM) | R2 D8:43 (Strategy B); R3 prompts:37 "**DEFERRED** — correlated with Strategy #1, testing as regime filter only" | **NOT TESTED.** No build or run in the record | E2, E3 |
| 8 | Overnight→intraday reversal CO-OC (Della Corte et al. 2015) | R2 D8:58 (Strategy C); R3 prompts:36 "**CONDITIONAL PASS** — NQ post-2018 evidence gap, in paper-trade validation" | **NOT TESTED** in the tracked record. The only tracked file naming it is the filter audit (row :111). The R3 claim "in paper-trade validation" has no tracked record | E3, E13, E18 |
| 9 | FX Fixings W-Shape reversal (6E/6B/6A/6J) | R3 D6:31 (rank 1) | **NOT TESTED; deferred.** Phase 3 spec:154, Block 6 satellites: "This is where FX Fixings, Overnight Drift, or CL EIA get added". Spec:182 says they get scoped "after Block 5 proves the baseline is stable" | E4, E5 |
| 10 | Overnight Drift (ES/NQ 02:00–03:00 ET; Boyarchenko–Larsen–Whelan 2023) | R1 D2:214 disqualified ("Active-window violation"); R3 prompts:40 ELIMINATED; R3 D6:32 (rank 2) | **NOT TESTED; deferred** to Block 6 (spec:154) | E1, E3, E4, E5 |
| 11 | CL EIA-conditioned intraday momentum | R3 D6:34 (rank 4) | **NOT TESTED; deferred** to Block 6 (spec:154) | E4, E5 |
| 12 | Gotobi-day USD/JPY | R3 D6:33 (rank 3) | **NOT TESTED; no record.** One tracked hit for "Gotobi\|NG EIA\|OPEC\|Brent" (E13), and it is an unrelated 2026-07-15 line ("Companion / satellite strategies (NOT under test in Block 2)") (E14) | E4, E13, E14 |
| 13 | NG EIA storage announcement | R3 D6:35 | **NOT TESTED; no record** (same search) | E4, E13 |
| 14 | FOMC-Day short-USD basket | R3 D6:36 | **NOT TESTED.** Filter-audit:114 "Low priority" | E4, E18 |
| 15 | Market intraday momentum on FDAX/FESX/Nikkei | R3 D6:37 | **NOT TESTED.** Filter-audit:117: "Eurex not routed by MFFU (A9)" | E4, E18 |
| 16 | OPEC meeting drift (CL) | R3 D6:38 | **NOT TESTED; no record** | E4, E13 |
| 17 | Carry + momentum composite (G10 FX) | R3 D6:39 | **NOT TESTED.** Filter-audit:113: "month-end holds against flat-by-close (A7)" | E4, E18 |
| 18 | Brent–WTI cointegration | R3 D6:40 | **NOT TESTED; no record** | E4, E13 |
| 19 | TORB, t_p = 1 min (Tsai et al. 2019) | R4 shortlist:63 (#2) | **SPECIFIED, not built.** DECISIONS.md:360 "TORB and ORB remain written specs in the shortlist." No `.cs` file (E13 `ls ninjascript`) | E6, E13 |
| 20 | 5-min ORB on QQQ (Zarattini & Aziz 2023) | R4 shortlist:109 (#3) | **SPECIFIED, not built** (same DECISIONS.md:360 line). The shortlist marks its rules "UNVERIFIED-from-secondary" | E6 |
| 21 | Volatility-adaptive VWAP mean reversion | R7 Gemini:98 (Candidate 1); R8 Kimi:68 (C1) | **NOT TESTED.** Session close: "NOT TESTED; low" | E10, E11, E12 |
| 22 | Opening gap fade / reversal | R7 Gemini:100 (Candidate 2); R8 Kimi:87 (C2), rank 3 at :316 | **NOT TESTED.** Session close: "NOT TESTED; low" | E10, E11, E12 |
| 23 | First-to-last half-hour momentum, ±0.30% threshold (Gao, Han, Li & Zhou 2018) | R7 Gemini:102 (Candidate 3); R8 Kimi:108 (C3), rank 2 at :315 | **NOT TESTED.** Session close: "NOT TESTED; deprioritised" | E10, E11, E12 |
| 24 | London-close reversal (benchmark-fixing intermediation) | R7 Gemini:104 (Candidate 4); R8 Kimi:146 (C4) | **DROPPED** (channel/Kimi, not an Amear ruling): "Mechanism borrowed from an FX fixing paper; no equity-index evidence." | E10, E11, E12 |
| 25 | Opening 30-minute momentum (Grant et al. 2005) | R8 Kimi:192 (New C6) | **DROPPED** (channel/Kimi): "Kimi's own cited evidence (Grant et al. 2005) points the other way." | E11, E12 |

Proposals that a run itself ranked out (each run's own exclusion lists; none was built or tested):
- R1 D2 §5 (:209–219): Pre-FOMC drift; Overnight Drift (later re-ranked in R3); PEAD; VRP/short VIX; cross-asset CTA; standalone ORB; Lucca–Moench FOMC (E1).
- R2 D8 (:17–20, :103, :106): OFI; pre-FOMC drift; standalone VWAP/Bollinger, ORB and gap fade; End-of-Day Reversal (E2).
- R3 prompts (:38–49): the resolved ELIMINATED/EXCLUDED rows (E3).
- R3 D6 :42–44: consensus rejections (E4).
- R8 Kimi "Rejected Strategies" (:294) (E11).

None of these has a DECISIONS.md ID. They are run-internal exclusions, not rulings. No DECISIONS.md entry names Gemini or Kimi (E13: `git grep ... DECISIONS.md` exit=1).

## Cross-run repeats

| Idea | Runs (file:line) | Note |
|---|---|---|
| Market intraday momentum, last half hour (Baltussen 2021) | R2 D8:29; R3 prompts:35; R3 D6:37 (Eurex variant); R4 shortlist:11; R8 Kimi:167 / :314 | 5 appearances (INFERRED count). Tested once on NQ (2026-11-01) and retired. The R7 audit and the R8 audit both recommended backtesting it first. The session-close correction (lines 18–20) withdrew that recommendation. The `.cs` header still reads "WRITTEN, NOT COMPILED, NOT TESTED" (`PraxisLastHalfHourMomentum.cs:19`, E16). That header is the likely source of the channel's error (INFERRED) |
| First-half-hour → last-half-hour momentum with threshold | R2 D8:43 (Rosa 2022); R3 prompts:37 DEFERRED; R4 shortlist:39 (Gao 2018 as abstract-only seed, not a candidate); R7 Gemini:102; R8 Kimi:108 / :315 | Never tested. Rosa 2022 (R2) and Gao 2018 (R7/R8) are different papers on the same mechanism (INFERRED from the two descriptions) |
| Opening gap fade | R2 D8:19 / :106 excluded; R3 prompts:48 EXCLUDED; R4 shortlist:169 (named as a possible fourth, "I did not research one"); R7 Gemini:100; R8 Kimi:87 / :316 | Excluded twice in the April/May runs, then re-proposed in Nov. Never tested |
| VWAP / Bollinger mean reversion | R2 D8:19 / :106; R3 prompts:47 EXCLUDED; R7 Gemini:98; R8 Kimi:68 | Same pattern as gap fade. Never tested |
| Opening range breakout (various) | R1 D2:141 (Stocks in Play) and :218 (standalone, disqualified); R2 D8:19; R3 prompts:38 ELIMINATED; R4 shortlist:63 (TORB) and :109 (Zarattini QQQ); R7 brief to Kimi, Gemini handoff:74 ("unfiltered opening range breakout" in the rejected list) | ORB was eliminated in May and short-listed again on 2026-10-31. It now sits at SPECIFIED (DECISIONS.md:360) |
| Overnight Drift | R1 D2:214; R3 prompts:40 ELIMINATED; R3 D6:32 rank 2; Gemini handoff:74 ("overnight drift held across the 16:00-18:00 close", rejected) | R3's 02:00–03:00 variant is deferred to Block 6. The Nov rejected-list wording names a different holding window |
| Pre-FOMC drift | R1 D2:213 / :219; R2 D8:18; R3 prompts:39; R3 D6:44 (FX version); Gemini handoff:74 | Rejected in every run. Never built |
| Pre-Announcement Drift / Savor–Wilson | R1 D2:80 / :113; R3 prompts:33–34; R6 filter-audit:177 / :184 | Re-surfaced by R6. Now SPECIFIED under bead `ckh` (OPEN) |
| FOMC even-week | R1 D2:52; R3 prompts:32; R6 filter audit; Gemini handoff:74 | Parked by R9 |
| Fixing-flow reversal | R3 D6:31 (FX Fixings W-shape, London fix 11:00 ET); R7 Gemini:104 / R8 Kimi:146 (London-close reversal applied to NQ) | Related mechanism, different instrument (INFERRED from the descriptions). The NQ version was dropped; the FX version is deferred to Block 6 |

## Evidence (command output)

E-sections E0–E13 come from one bash runner (`printf '%s\n' "$ cmd"` followed by `bash -c`). Output lines are cut at 330 characters. E14–E20 come from a second runner. A line ending mid-word was cut by `cut`, not by the source.

```
### E0 Redemtion/ is gitignored
$ cd /Volumes/Sensidine/Praxis.build && git check-ignore -v "Redemtion/Research Results/PHASE_2_STRATEGY_DECISION_Compiled_Round_3.md"
.gitignore:7:Redemtion/	Redemtion/Research Results/PHASE_2_STRATEGY_DECISION_Compiled_Round_3.md

### E1 D2 Verified shortlist (April 2026, gitignored RTF)
$ cd "/Volumes/Sensidine/Praxis.build/Redemtion/Intitialization-April 2026" && textutil -convert txt -stdout "Verified Trading-Strategy Shortlist for NQ : Index Futures.rtf" | grep -n -E "^### Strategy #|^## 5\.|^\| \*\*(Pre-FOMC|Overnight|Post-Earn|Volatility|Cross-asset|Standalone|Pure)"
23:### Strategy #1 — Intraday Momentum / "Noise-Area" Breakout (Zarattini–Aziz–Barbon)
52:### Strategy #2 — FOMC-Cycle Even-Week Long Bias
80:### Strategy #3 — Pre-Announcement Drift around NFP / ISM / GDP (and Heightened-Uncertainty Premium)
113:### Strategy #4 — Macroeconomic Announcement-Day Long-Beta Premium (Savor–Wilson Framework)
141:### Strategy #5 — 5-Minute Opening Range Breakout on "Stocks in Play" (Zarattini–Barbon–Aziz, 2024) — Included with Caveats
209:## 5. Honorable Mentions / Disqualified Candidates
213:| **Pre-FOMC Announcement Drift** | Lucca & Moench, *Journal of Finance* 2015 | **Algo-degraded.** Kurov-Wolfe-Gilbert (2020), Boguth-Grégoire-Martineau (2019), Ignatieva-Ohashi (2024) all document substantial decay or disappearance after 2015. Especially weak on non-press-conference FOMC days. |
214:| **Overnight Drift** | Boyarchenko-Larsen-Whelan, *RFS* 2023 (NY Fed Staff Report 917) | **Active-window violation.** The drift accrues 2:00–3:00 a.m. ET (European market open). Cannot be entered or managed inside 9:00–11:30 AM ET. |
215:| **Post-Earnings Announcement Drift (PEAD)** | Ball & Brown 1968; Bernard-Thomas 1989 | **Algo-absorbed (post-2006) and wrong instrument.** Martineau (2022) titled his paper "Rest in Peace Post-Earnings Announcement Drift." Index-futures don't have meaningful idiosyncratic earnings surprises. |
216:| **Volatility Risk Premium / Short VIX** | Various; Quantpedia | **Tail-risk profile incompatible with prop firm daily-loss-limits.** XIV-style or short-VIX-futures positions face occasional 50%+ single-day losses (Feb 2018) that breach prop firm rules instantly. Strategy is materially better on own, properly-sized capital 
217:| **Cross-asset Time-Series Momentum (CTA)** | Moskowitz-Ooi-Pedersen, *JFE* 2012; Clenow 2013/2023 | **Demoted to honorable mention.** Excellent academic support; portfolio is the unit of edge, not single-instrument NQ. Requires diversified futures book (currencies, rates, commodities, indices). SG Trend Index in drawdown 2
218:| **Standalone NQ/ES Opening Range Breakout (no filter)** | Crabel 1990; multiple practitioner sources | **Insufficient peer-reviewed validation post-2018.** QuantifiedStrategies and other backtests find no edge without additional volatility/news/regime filters. The Zarattini Stocks-in-Play version is academically validated 
219:| **Pure Lucca-Moench-style "buy 24h before FOMC, sell at announcement"** | Lucca-Moench 2015 | **Edge dead** per multiple post-2015 replications. The newer FOMC variant (Cieslak even-week, Strategy #2) operates on a different mechanism and remains valid. |

### E2 D8 Higher-frequency pairing (gitignored RTF)
$ cd "/Volumes/Sensidine/Praxis.build/Redemtion/Intitialization-April 2026" && textutil -convert txt -stdout "Systematic, Higher-Frequency NQ Strategies to Pair with the Noise-Area Breakout .rtf" | grep -n -E "^#### Strategy|^1\. \*\*(Order-book|Pre-FOMC|Standalone|The .End-of-Day)"
17:1. **Order-book imbalance (OBI / OFI) has peer-reviewed support but the wrong time-horizon.** Kolm, Turiel & Westray, *Mathematical Finance* 33(4), 1044–1081 (2023), demonstrate that deep-OFI features predict mid-price returns out-of-sample, but their own analysis shows the effective forecasting horizon is **approximately two
18:1. **Pre-FOMC drift (Lucca-Moench 2015) is gone.** Kurov, Wolfe & Gilbert, *Finance Research Letters* (2020/PMC) extend the sample to December 2019 and demonstrate the drift “essentially disappeared after 2015”  on E-mini S&P futures across announcements with and without press conferences. The overlapping work by Quantseeker 
19:1. **Standalone VWAP-reversion, Bollinger-band reversion, opening-range breakout, and opening-gap fade lack peer-reviewed validation specifically on NQ futures over 2018–2025 with sample size ≥200 and full cost accounting.** The Zarattini–Aziz literature (*SSRN* 2023, 2024) on ORB applies to a broad equity universe of ~7,000 
20:1. **The “End-of-Day Reversal” (Baltussen, Da & Soebhag, SSRN November 2024; Quantpedia Award 2025)** documents a cross-sectional reversal in *individual stocks* during the last 30 minutes  — not the index. Because NQ is a market-level instrument, this paper is **not directly tradeable on NQ futures alone**. Mentioned for com
29:#### Strategy A. Last-Half-Hour Hedging-Demand Momentum (LHHM)
43:#### Strategy B. Threshold-Conditioned First-Half-Hour Momentum (TC-FHM)
58:#### Strategy C. Overnight→Intraday Reversal (CO-OC)
103:1. **The “End-of-Day Reversal” of Baltussen-Da-Soebhag (2024)** is cross-sectional in individual stocks; despite the strong evidence (Quantpedia Award 2025 second prize),  it does not translate cleanly to a single index-futures instrument like NQ. Useful for users running multi-instrument equity baskets, irrelevant for NQ-on
106:1. **Pre-FOMC drift, opening gap fade, and pure VWAP/Bollinger reversion** lack peer-reviewed evidence of survival on NQ post-2018. Properly excluded by the user.

### E3 Round 3 prompts: run instructions and the already-resolved table
$ cd /Volumes/Sensidine/Praxis.build && sed -n 3,5p "Redemtion/Research Prompts/PRAXIS_Phase2_Expanded_Strategy_Search_3Agent_Prompts.md"
**Generated:** May 6, 2026
**Purpose:** Three research prompts designed to run as separate deep research sessions. The prior research round was constrained to NQ/ES index futures during the New York session (9:00 AM – 3:00 PM ET). Now that full automation is confirmed, both constraints are removed. This round searches for the best systematic, fully-automa
**Usage:** Paste each prompt into a separate Claude deep research session. Run all three in parallel. Compile outputs into a single reference document for Phase 2 strategy decision.

$ cd /Volumes/Sensidine/Praxis.build && sed -n 31,49p "Redemtion/Research Prompts/PRAXIS_Phase2_Expanded_Strategy_Search_3Agent_Prompts.md"
| Noise-Area Intraday Momentum Breakout (Zarattini–Aziz–Barbon 2024) | **SELECTED** as baseline. Clock-anchored, ~1 trade/session, 38% WR, 2.25 payoff, Sharpe 1.67 on NQ | Swiss Finance Institute WP |
| FOMC-Cycle Even-Week (Cieslak–Morse–Vissing-Jorgensen 2019) | **PARKED** — overnight hold incompatible with prop firm at current capital | *Journal of Finance* |
| Pre-Announcement Drift NFP/ISM/GDP (Hu–Pan–Wang–Zhu 2022) | **PARKED** — overnight hold + thin annual sample | *Journal of Financial Economics* |
| Macroeconomic Announcement-Day Premium (Savor–Wilson 2013/2014) | **RETAINED** as manual fallback only | *JFQA* / *JFE* |
| Last-Half-Hour Hedging-Demand Momentum (Baltussen et al. 2021) | **PASSED** — pending walk-forward validation on NQ | *Journal of Financial Economics* |
| Overnight→Intraday Reversal CO-OC (Della Corte et al. 2015) | **CONDITIONAL PASS** — NQ post-2018 evidence gap, in paper-trade validation | SSRN, heavily cited |
| Threshold-Conditioned First-Half-Hour Momentum (Rosa 2022) | **DEFERRED** — correlated with Strategy #1, testing as regime filter only | *Journal of Futures Markets* |
| 5-Minute Opening Range Breakout on NQ (standalone) | **ELIMINATED** — no robust standalone edge on NQ without filters | Multiple replications |
| Pre-FOMC Announcement Drift (Lucca–Moench 2015) | **ELIMINATED** — edge disappeared post-2015 per Kurov et al. 2020 | *Finance Research Letters* |
| Overnight Drift (Boyarchenko–Larsen–Whelan 2023) | **ELIMINATED** — was outside active window; NOW potentially viable under automation but already assessed | *Review of Financial Studies* |
| Standard PEAD | **ELIMINATED** — dead for non-microcap post-2006 | Martineau 2022 |
| Volatility Risk Premium / short-VIX | **ELIMINATED** — tail risk incompatible with prop firm drawdown | Various |
| Cross-asset CTA trend-following | **ELIMINATED** — portfolio-level, extended drawdown 2023-2025 | Moskowitz et al. 2012 |
| End-of-Day Reversal (Baltussen-Da-Soebhag 2024) | **EXCLUDED** — cross-sectional in individual stocks, not tradeable on single index future | SSRN |
| Order-flow imbalance / deep-OFI | **EXCLUDED** — 2-price-change horizon, requires co-location | Kolm-Turiel-Westray 2023 |
| 0DTE gamma as standalone signal | **EXCLUDED** — too small as standalone NQ signal | Cboe research, Dim-Eraker-Vilkov 2024 |
| Standalone VWAP/Bollinger reversion on NQ | **EXCLUDED** — no peer-reviewed NQ evidence post-2018 | — |
| Opening gap fade on NQ | **EXCLUDED** — no peer-reviewed NQ evidence post-2018 | — |
| ML/gradient-boosting on intraday NQ | **EXCLUDED** — no published walk-forward validation meeting evidence bar | — |

### E4 Round 3 compiled ranking (gitignored)
$ cd /Volumes/Sensidine/Praxis.build && sed -n 1,5p "Redemtion/Research Results/PHASE_2_STRATEGY_DECISION_Compiled_Round_3.md"; grep -n -E "^\| \*\*[0-9]" "Redemtion/Research Results/PHASE_2_STRATEGY_DECISION_Compiled_Round_3.md" | cut -c1-90; sed -n 42,44p "Redemtion/Research Results/PHASE_2_STRATEGY_DECISION_Compiled_Round_3.md"; sed -n 263,266p "Redemtion/Research Results/PHASE_2_STRATEGY_DECISION_Compiled_Round_3.md"
# PRAXIS PHASE 2 — STRATEGY DECISION INPUT
## Compiled Cross-Agent Analysis (Round 3)

**Date:** May 6, 2026
**Sources:** Agent 1 (Commodities), Agent 2 (FX Macro), Agent 3 (Multi-Session/Cross-Instrument)
31:| **1** | **FX Fixings W-Shape Reversal (Tokyo + London on 6E/6B/6A/6J)** | 2+3 | Tier 
32:| **2** | **Overnight Drift (ES/NQ, 2:00–3:00 a.m. ET)** | 3 | Tier 1 (RFS 2023, JFQA 2
33:| **3** | **Gotobi-Day USD/JPY** | 2 | Tier 1/2 (NBER WP + arXiv, t-stats >3) | 2:1 ✓ (
34:| **4** | **CL EIA-Conditioned Intraday Momentum** | 1 | Tier 1 (Economic Modelling 202
35:| **5** | **NG EIA Storage Announcement** | 1 | Tier 1 (Energy Journal 2021, ~830 annou
36:| **6** | **FOMC-Day Short-USD Basket** | 2 | Tier 1 (JF 2017, replicated through ~2020
37:| **7** | **Market Intraday Momentum (FDAX/FESX/Nikkei last 30 min)** | 3 | Tier 1 (JFE
38:| **8** | **OPEC Meeting Drift (CL)** | 1 | Tier 1 but older (Energy Journal 2004, Ener
39:| **9** | **Carry + Momentum Composite (G10 FX, monthly)** | 2 | Tier 1 (multiple JFE/J
40:| **10** | **Brent–WTI Cointegration** | 3 | Tier 2 with Tier 1 methodology | ~2:1 | Hi
248:| **1. Validate** | Custom backtest FX Fixings on 6E/6J (2018–2025) | 2–3 weeks |
249:| **2. Validate** | Custom backtest Overnight Drift on ES (2019–2025) | 2–3 weeks (par
250:| **3. Build** | NinjaScript strategies for validated winners | 1–2 weeks per strategy
251:| **4. Forward Test** | 30-day sim on MFFU for each strategy | 30 days |
252:| **5. Deploy** | Graduated live: MNQ/M6E micro contracts first, then full size | 60 d
253:| **6. Evaluate CL EIA** | Only after Phases 1–5 prove stable: backtest CL, open Apex 
### Strategies Excluded Across All Agents (Consensus Rejections)

London Breakout / Asian Range Break (Tier 3 only), Pre-FOMC Drift on FX (negative evidence — does not transfer from equities), Single-Pair G10 Momentum (decayed post-2010), Gold FOMC/CPI Strategies (judgment-based, not mechanical), PPP/REER Mean Reversion (multi-year horizon, incompatible with prop firms), Risk-Reversal as Direc
3. **CL EIA Intraday** — clean rules, good diversifier, but requires a second prop firm account

The optimal portfolio is **NQ (anchor) + FX Fixings + Overnight Drift**, all on MFFU, targeting a combined Sharpe of 2.0+ with 30–40% drawdown reduction. CL EIA on Apex is a Phase 2 addition after the core portfolio proves stable.


$ cd /Volumes/Sensidine/Praxis.build && for f in "Redemtion/Research Results/Round 3"/*.md; do head -1 "$f"; done
# PRAXIS PHASE 2 — AGENT 1: COMMODITY FUTURES ECONOMIC-DATA-DRIVEN SYSTEMATIC STRATEGIES
# FOREX: Macro-Driven Systematic Strategies — Catalog, Evidence, and Combination Analysis with NQ Noise-Area Breakout
# PRAXIS PHASE 2 — AGENT 3 REPORT

### E5 Phase 3 spec Block 6 (tracked)
$ cd /Volumes/Sensidine/Praxis.build && grep -n -E "Block 6|FX Fixings, Overnight Drift, or CL EIA get added|Satellite strategy specifications" docs/specs/2026-11-05-phase3-build-specification.md
152:### Block 6: Satellite Strategy Layering (Only After Block 5 Is Stable)
154:This is where FX Fixings, Overnight Drift, or CL EIA get added. Same sequence for each: backtest → NinjaScript build → n8n workflow → circuit breaker extension → paper trade → graduated live. Each satellite uses the same file-drop integration, same monitoring, same breaker architecture. The infrastructure you built in Blocks
182:Satellite strategy specifications. FX Fixings, Overnight Drift, and CL EIA each need their own NinjaScript spec and backtest configuration. Those get scoped after Block 5 proves the baseline is stable. Building three strategies in parallel before one is validated is the kind of scattered execution that feeds the pattern.

### E6 7zq M2 shortlist (2026-10-31)
$ cd /Volumes/Sensidine/Praxis.build && grep -n -E "^## Candidate #|^\*\*Pick = |Supporting abstract-only seed|^Note for Amear" docs/reports/2026-10-31-7zq-m2-shortlist.md
11:## Candidate #1 — Last-half-hour market intraday momentum, `η(r_ROD)` (Baltussen, Da, Lammers, Martens 2021)
39:- Supporting abstract-only seed: Gao, Han, Li, Zhou (2018), "Market intraday momentum," *JFE*, DOI 10.1016/j.jfineco.2018.05.009. Abstract via the Semantic Scholar API (OBSERVED): "Based on high frequency data of the S&P 500 ETF from 1993-2013, we document an intraday momentum pattern: the first half-hour return on the market
63:## Candidate #2 — Timely Opening Range Breakout, TORB (Tsai, Wu, Syu, Lei, Wu, Ho, Wang 2019)
109:## Candidate #3 — 5-minute Opening Range Breakout on QQQ (Zarattini & Aziz 2023)
161:**Pick = #1 (Baltussen et al. 2021 `η(r_ROD)`).** Reasons:
169:Note for Amear: #2 and #3 are both opening-range breakouts, so they are one signal family. If you want three distinct families, a fourth candidate would have to be researched (for example, an opening-gap fade). I did not research one in this run.

$ cd /Volumes/Sensidine/Praxis.build && sed -n 3,3p docs/reports/2026-10-31-7zq-m2-shortlist.md; sed -n 3,4p docs/reports/2026-10-31-7zq-m2-new-strategy.md
- Unit: `Praxis_build-7zq`, phase M2, worker 1. Mode: BUILD (research). Date: 2026-10-31.
**Unit:** `Praxis_build-7zq` phase M2 · praxis-manager · 2026-10-31 (10:44Z → 11:20Z) · base HEAD `fab2855`.
**Deliverable level: WRITTEN.** It has not been compiled or tested, and no backtest was run. This Mac has no NT8 toolchain. Every NT8 behaviour claim below is INFERRED or CANNOT-DETERMINE-STATICALLY. The compile on the Fusion VM is Amear's step 1.

$ cd /Volumes/Sensidine/Praxis.build && grep -n -E "TORB and ORB remain" DECISIONS.md
360:- **R-7zq-3 — third file (answers NEEDS AMEAR 6 above), DECISION_LOG `2026-10-31T11:45:29Z` (WHO: amear):** *"Keep #1 (as built)"* — `PraxisLastHalfHourMomentum` (Baltussen, Da, Lammers & Martens 2021) stands; TORB and ORB remain written specs in the shortlist.

### E7 LastHalfHourMomentum test and retirement
$ cd /Volumes/Sensidine/Praxis.build && sed -n 400,405p docs/reports/2026-11-01-three-strategy-results.md
| run | trades | net | PF | max DD (i) | max DD (ii) | win % | avg trade | largest win | largest win as % of net |
|---|---|---|---|---|---|---|---|---|---|
| BASELINE (`PraxisNoiseAreaBreakout`, BandOrVWAP) | 1190 | $197327.60 | 1.29 | -$45282.04 | -$45282.04 | 40.67% | $165.82 | $35887.04 | 18.19% |
| OPPBAND | 810 | $210182.40 | 1.26 | -$50748.88 | -$50748.88 | 58.02% | $259.48 | $36087.04 | 17.17% |
| FLAT1559 | 1190 | $193017.60 | 1.28 | -$40637.04 | -$40637.04 | 40.50% | $162.20 | $36472.04 | 18.90% |
| LHMOM (LastHalfHourMomentum) | 1304 | -$76009.84 | 0.84 | -$99806.96 | -$99806.96 | 47.62% | -$58.29 | $3852.04 | -5.07% (not meaningful) |

$ cd /Volumes/Sensidine/Praxis.build && grep -n -E "^## 2026-11-02 — D-2026-11-02-A|removed from the active candidate set" DECISIONS.md
368:## 2026-11-02 — D-2026-11-02-A: R-VN3-1 — `PraxisLastHalfHourMomentum` RETIRED from the active candidate set (retire, not delete)
383:- `PraxisLastHalfHourMomentum` (Baltussen, Da, Lammers & Martens 2021; third file of D-2026-10-31-A) is **removed from the active candidate set**. What that excludes beyond the removal is not ruled here (see NEEDS AMEAR 3).

$ cd /Volumes/Sensidine/Praxis.build && bd show Praxis_build-afe 2>/dev/null | head -2
✓ Praxis_build-afe · R-VN3-1: PraxisLastHalfHourMomentum retired from the active candidate set (retire, not delete)   [● P2 · CLOSED]
Owner: Amear Bani-Ahmad · Type: task

### E8 Research set A/B/C (2026-11-04, landed in 84b1a58)
$ cd /Volumes/Sensidine/Praxis.build && git show --stat --format="%h %ad" --date=short 84b1a58 | grep -E "^84b1a58|comparable-builds|proof-of-concept|tick-data-sources|research-compiled|research-briefs"
84b1a58 2026-11-06
 ...026-11-04-research-briefs-tickdata-repos-poc.md |  89 +++
 docs/reports/2026-11-04-comparable-builds.md       | 877 +++++++++++++++++++++
 .../2026-11-04-proof-of-concept-standard.md        | 669 ++++++++++++++++
 .../2026-11-04-research-compiled-for-voice-v2.md   | 216 +++++
 .../2026-11-04-research-compiled-for-voice.md      | 151 ++++
 docs/reports/2026-11-04-tick-data-sources.md       | 552 +++++++++++++

$ cd /Volumes/Sensidine/Praxis.build && sed -n 10,13p docs/reports/2026-11-04-research-compiled-for-voice-v2.md; sed -n 129,132p docs/reports/2026-11-04-research-compiled-for-voice-v2.md
**Status of the three reports.** Each one failed its first audit, was corrected by an append (no original text overwritten), and then passed re-audit.
- **A, tick data** (`docs/reports/2026-11-04-tick-data-sources.md`): four minor findings, no blocking ones. These were missing excerpts and a dropped "inferred" grade.
- **B, comparable builds** (`docs/reports/2026-11-04-comparable-builds.md`): three blocking findings. One claim was wrong, a dozen code claims had no pasted lines, and your GitHub login was used without your authorisation.
- **C, proof of concept** (`docs/reports/2026-11-04-proof-of-concept-standard.md`): some figures had no pasted output. Separately, the auditor re-ran C's statistics with its own script and reproduced them.
- **Noise-Area in NinjaScript.**
  - One public implementation was found: skizzunni/money, MNQ, no licence. It was being pushed to on the day it was read.
  - Its chart timeframe is unresolved; one file says 5-minute and another says 1-minute.
  - Its author reports native Strategy Analyzer runs that match his simulator on 86–92 of 97–98 trades. That is his report, against an older version of the file. We ran nothing.

### E9 Strategy filter audit (2026-11-08) and R6
$ cd /Volumes/Sensidine/Praxis.build && sed -n 3,4p docs/reports/2026-11-08-strategy-filter-audit.md; grep -n -E "^## 5\. Step 5|^1\. \*\*Pre-Announcement|^2\. \*\*Macroeconomic|^\*\*Not recommended" docs/reports/2026-11-08-strategy-filter-audit.md
**Date:** 2026-11-08. **By:** Claude.ai Praxis channel (research agent), at Amear's brief of the same date.
**Status:** recommendation only. Every outcome below is **PROPOSED** pending Amear's approval. No decision, spec or ruling is changed. The 2026-11-08 ruling RTH = 09:30–16:00 ET is not reopened.
175:## 5. Step 5: ranked re-evaluation list (PROPOSED)
177:1. **Pre-Announcement Drift (Hu, Pan, Wang & Zhu 2022, JFE), evening-entry variant.**
184:2. **Macroeconomic Announcement-Day Premium (Savor–Wilson 2013/2014; Ai 2024).**
191:**Not recommended for re-evaluation, with the non-C reason:**

$ cd /Volumes/Sensidine/Praxis.build && grep -n -E "^R6 |Pre-Announcement Drift \(Hu|Savor–Wilson; Ai 2024|^R9 " DECISIONS.md
1572:R6  Research and backtest, on the existing 1-minute data only,
1574:    - Pre-Announcement Drift (Hu, Pan, Wang & Zhu 2022), evening-
1576:    - Macroeconomic Announcement-Day Premium (Savor–Wilson; Ai 2024).
1590:R9  FOMC-Cycle Even-Week stays parked while trading on MFFU

$ cd /Volumes/Sensidine/Praxis.build && git log --oneline -1 bf6fcc7 | cut -c1-140; git branch --list "*r6*"; git branch -r --list "*r6*"; grep -n "R6 Pre-Announcement Drift" docs/specs/2026-11-10-live-signal-topology.md
bf6fcc7 docs: R6 step 1 (bead Praxis_build-ckh, P0 under D-2026-11-08-D D7) - MFFU current rules read with raw captures, and PROPOSED resear
+ r6/announcement-research
  origin/r6/announcement-research
20:| 1.4 | R6 Pre-Announcement Drift, evening entry | A PROPOSED research design on branch `r6/announcement-research` (`bf6fcc7`); no strategy code. | SPECIFIED | [E15] |

$ cd /Volumes/Sensidine/Praxis.build && bd show Praxis_build-ckh 2>/dev/null | head -2
○ Praxis_build-ckh · R6 research P0 under D7: Pre-Announcement Drift and Announcement-Day Premium on existing 1-minute data, own worktree, nothing bought   [● P0 · OPEN]
Owner: Amear Bani-Ahmad · Type: task

### E10 Gemini run (2026-11-13)
$ cd /Volumes/Sensidine/Praxis.build && sed -n 9,9p docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md; grep -n -o -E "Candidate [1-4]: [A-Za-z() -]{10,55}" docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md
- 2026-11-13 ~13:00 ET: Amear ran a Gemini Deep Research brief (steady daily NQ/MNQ strategy that survives an MFFU trailing drawdown at 1 MNQ). The full output is Appendix A, unedited.
98:Candidate 1: Volatility-Adaptive VWAP Mean ReversionMicrostructural 
100:Candidate 2: Institutional Opening Gap ReversalMicrostructural Mecha
102:Candidate 3: First-to-Last Half-Hour Intraday MomentumMicrostructura
104:Candidate 4: Benchmark Fixing Intermediation Reversal (London Close)

### E11 Kimi run (2026-11-13)
$ cd /Volumes/Sensidine/Praxis.build && sed -n 3,3p docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md | cut -c150-330; grep -n -E "^(New )?C[1-6]\. |^Rejected Strategies|^Recommended Backtests|^(End-of-Day Momentum|First-to-Last 30m|Opening Gap Fade)" docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md | cut -c1-120
s Appendix B is the brief Kimi answered). File it as written unless a de-identification check fails. REPORTED BY the channel: Amear ran the Kimi brief and supplied the output below 
68:C1. Volatility-Weighted VWAP Mean Reversion
87:C2. Opening Gap Fade
108:C3. First- vs. Last-Half-Hour Momentum (Gao et al. 2018) and Baltussen et al. 2021
146:C4. London-Close Reversal (10:30–11:15 to 11:15–12:00)
167:New C5. End-of-Day Directional Momentum (Baltussen et al. 2021)
192:New C6. Opening-Bars Momentum (Inspired by Grant et al. 2005)
215:C1. VWAP σ-band mean reversion	See above (VWAP±2.5σ)	Mean reversion to intraday VWAP	None for NQ. (Report: ~60–65% w
216:C2. Opening Gap Fade	Gap 0.35–1.5% fade at 09:34 (target prior close)	Gap-fade mean-reversion	No NQ pub. fig.; Fung+
217:C3. First→Last 30m Momentum	9:30–10:00 > +0.30% → long @15:30; <–0.30% → short; exit 15:59; 0.5% stop	Intraday momen
219:C4. London-Close Reversal	10:30–11:15 >+0.40% → short at 11:15; <–0.40% → long; exit 12:00	FX-fixing contrarian?	No 
220:C6. Opening 30m Momentum	9:30–10:00 > +0.50% → long at 10:00; <-0.50% → short; exit 12:00	Morning momentum	None. (Gr
294:Rejected Strategies
311:Recommended Backtests (Top-3 Priorities)
314:End-of-Day Momentum (Baltussen et al.). This has the strongest support: multi-year evidence on futures, trades daily
315:First-to-Last 30m Momentum (Gao et al.). A variation on (1) with a threshold, but still momentum. Even though Baltus
316:Opening Gap Fade. This is the best-supported mean-reversion candidate. It trades often enough to meet sample size. E

### E12 Session-close correction and status table (2026-11-13)
$ cd /Volumes/Sensidine/Praxis.build && sed -n 18,20p docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md; sed -n 26,37p docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md
Files 1 and 2 recommend backtesting `PraxisLastHalfHourMomentum` first. **Withdrawn.** The channel missed that it was already tested and retired:
- 2026-11-01 hand-test run, 1 NQ (NQCONTROW SEP25), $2.96 round-trip commission, 2 ticks/side slippage: 1,304 trades, net -$76,009.84, PF 0.84, max DD -$99,806.96, win rate 47.62%, average trade -$58.29 (`docs/reports/2026-11-01-three-strategy-results.md`, comparison table; re-checked MATCH in `docs/reports/2026-11-01-csv-analys
- Retired by Amear's ruling R-VN3-1, filed as D-2026-11-02-A (bead `Praxis_build-afe`, closed). Retire, not delete.
Two deep-research runs (Gemini, then Kimi) were asked for a steady, high-win-rate intraday NQ strategy that survives an MFFU trailing drawdown at 1 MNQ. **Neither found a viable new candidate.** Status of everything they proposed:

| Candidate | Status | Why |
|---|---|---|
| Last-half-hour momentum (Baltussen, Da, Lammers & Martens 2021, JFE 142:377-403) | TESTED, RETIRED (D-2026-11-02-A) | Lost money on NQ 2021-2026, before and after costs (section 2). The paper's results are for diversified baskets, 1974-2020. |
| First-to-last half-hour momentum with a +/-0.30% threshold (Gao, Han, Li & Zhou 2018, JFE) | NOT TESTED; deprioritised | Same mechanism as the retired strategy above; the threshold filter is the only difference. Test only with a stated reason to expect a different result. |
| Opening gap fade (0.35%-1.50% gap, target prior close) | NOT TESTED; low | Both runs: near break-even at best; Kimi cites practitioner sources only. Limit-order target and intrabar stop fill optimistically on 1-minute bars. |
| VWAP sigma-band mean reversion | NOT TESTED; low | No source found ("Dean & Francis 2026" could not be identified and was withdrawn). Negative after costs at the proposer's own baseline. |
| London-close reversal (10:30-11:15 fade) | DROPPED | Mechanism borrowed from an FX fixing paper; no equity-index evidence. |
| Opening 30-minute momentum (Kimi's new C6) | DROPPED | Kimi's own cited evidence (Grant et al. 2005) points the other way. |

Also ruled out in earlier work and restated by both runs: pre-FOMC drift; trading the release itself; post-earnings drift; short volatility; single-instrument CTA trend; unfiltered opening range breakout; FOMC even-week cycle; overnight drift held across 16:00-18:00; anything holding through a Tier 1 release. Noise-Area breakout

$ cd /Volumes/Sensidine/Praxis.build && git log --oneline -1 f10603a | cut -c1-120
f10603a docs: D6 drawdown viability check (Amear D-2026-11-08-D D6) on the three 2026-11-01 trade lists at 1 MNQ and 1 N

### E13 Searches for later work on proposals (tracked files)
$ cd /Volumes/Sensidine/Praxis.build && git grep -n -i -E "Gotobi|NG EIA|OPEC|Brent" -- . ":!docs/reports/2026-10-28-f4-*" ":!docs/reports/evidence" | wc -l
       1

$ cd /Volumes/Sensidine/Praxis.build && git grep -l -i -E "Della Corte|CO-OC Reversal" -- . ":!docs/reports/2026-10-28-f4-*" ":!docs/reports/evidence"
docs/reports/2026-11-08-strategy-filter-audit.md

$ cd /Volumes/Sensidine/Praxis.build && ls ninjascript
PraxisLastHalfHourMomentum.cs
PraxisNoiseAreaBreakout_Flat1559.cs
PraxisNoiseAreaBreakout_OppBand.cs
PraxisNoiseAreaBreakout.cs
PraxisSignalConsumer.cs

$ cd /Volumes/Sensidine/Praxis.build && git grep -l -i -E "TORB|Tsai|Gao|Savor|Fixing|Overnight" -- ninjascript; echo "exit=$?"
ninjascript/PraxisNoiseAreaBreakout.cs
ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs
exit=0

$ cd /Volumes/Sensidine/Praxis.build && git grep -n -i -E "Gemini|Kimi" DECISIONS.md; echo "exit=$?"
exit=1

$ cd /Volumes/Sensidine/Praxis.build && ls docs | grep -i research; echo "exit=$?"
exit=1

### E14 Incidental matches behind E13 counts
$ cd /Volumes/Sensidine/Praxis.build && git grep -n -i -E "TORB|Tsai|Gao|Savor|Fixing|Overnight" -- ninjascript | cut -c1-120
ninjascript/PraxisNoiseAreaBreakout.cs:84:		private double     prevClose;      // Close_{t-1,16:00}  (overnight-gap ref,
ninjascript/PraxisNoiseAreaBreakout.cs:101:				Description  = "PRAXIS B2 Noise-Area Breakout (Zarattini SSRN 4824172) — 
ninjascript/PraxisNoiseAreaBreakout.cs:235:		// Bounds with overnight-gap adjustment (spec §1 step 3, p.7):
ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:117:		private double     prevClose;      // Close_{t-1,16:00}  (overnigh
ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:134:				Description  = "PRAXIS B2 Noise-Area Breakout (Zarattini SSRN 48
ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:273:		// Bounds with overnight-gap adjustment (spec §1 step 3, p.7):
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:107:		private double     prevClose;      // Close_{t-1,16:00}  (overnight
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:124:				Description  = "PRAXIS B2 Noise-Area Breakout (Zarattini SSRN 482
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:261:		// Bounds with overnight-gap adjustment (spec §1 step 3, p.7):

$ cd /Volumes/Sensidine/Praxis.build && git grep -n -i -E "Gotobi|NG EIA|OPEC|Brent" -- . ":!docs/reports/2026-10-28-f4-*" ":!docs/reports/evidence" | cut -c1-160
docs/reports/2026-07-15-b2-q1-strategy-exportability.md:20:**Companion / satellite strategies (NOT under test in Block 2).** The portfolio adds uncorrelated sat

### E15 Model attribution in the April RTFs (D2, D8)
$ cd "/Volumes/Sensidine/Praxis.build/Redemtion/Intitialization-April 2026" && for f in "Verified Trading-Strategy Shortlist for NQ : Index Futures.rtf" "Systematic, Higher-Frequency NQ Strategies to Pair with the Noise-Area Breakout .rtf"; do textutil -convert txt -stdout "$f" | grep -c -i -E "claude|gemini|kimi|qwen|perplexity|chatgpt|openai"; done
0
0

### E16 Gemini handoff: rejected list given to Kimi; repo cross-check claim
$ cd /Volumes/Sensidine/Praxis.build && sed -n 74,74p docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md
Already rejected (do not re-propose without new post-2020 evidence): pre-FOMC drift; trading the macro release itself; post-earnings drift; short volatility; single-instrument CTA trend; unfiltered opening range breakout; FOMC even-week cycle; overnight drift held across the 16:00-18:00 close; any strategy that holds through a T

$ cd /Volumes/Sensidine/Praxis.build && sed -n 26,26p docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md | cut -c1-260
Repo cross-check (OBSERVED by the channel, read-only, 2026-11-13): `ninjascript/PraxisLastHalfHourMomentum.cs` (commit `0ced412`) codes the related Baltussen, Da, Lammers & Martens (2021, JFE) signal: prior 16:00 close to 15:30 return, long if positive, short 

$ cd /Volumes/Sensidine/Praxis.build && grep -n "NOT TESTED" ninjascript/PraxisLastHalfHourMomentum.cs | cut -c1-200
19:// WRITTEN, NOT COMPILED, NOT TESTED. No NT8 toolchain on the Mac; every behaviour note below is
141:				Description  = "PRAXIS 7zq M2 Last-half-hour market intraday momentum (Baltussen, Da, Lammers, Martens 2021, JFE 142, eta(r_ROD)). At 15:30 ET: long if (last 16:00 close)->15:30 return > 0, ot

### E17 Voice strategy brief 2026-11-08: no strategy proposals
$ cd /Volumes/Sensidine/Praxis.build && grep -n -i -E "momentum|reversion|breakout|ORB|gap fade|drift" docs/reports/2026-11-08-voice-strategy-brief.md | cut -c1-160
30:- **The backtested baseline's max drawdown** (PraxisNoiseAreaBreakout, BandOrVWAP, 1 NQ, 2021-03-08 → 2026-07-17): **−$45,282.04** (`docs/reports/2026-11-01-

### E18 Filter audit: CO-OC row and which C-items it re-scored
$ cd /Volumes/Sensidine/Praxis.build && grep -n -E "^\| (CO-OC Reversal|Last-Half-Hour Momentum|R3 FDAX|Carry \+ Momentum|FOMC-Day Short-USD)" docs/reports/2026-11-08-strategy-filter-audit.md | cut -c1-200
110:| Last-Half-Hour Momentum (D8 Strategy A; D4 "PASSED") | Built 10-31 as research-only "because it trades inside breaker #5's window" (repo, 10-31 handoff §0); retired by R-VN3-1 after net PF 0.84 
111:| CO-OC Reversal (D8 Strategy C) | CONDITIONAL PASS, NQ post-2018 gap | C9: breaker #4 at 11:30 cuts its 12:00–15:00 exit window [I] | No | The evidence gap is A4, not disqualifying. |
113:| Carry + Momentum composite (D6 #9) | "FAILS R:R hard filter" | C3 | **Yes** [V] | **Yes on MFFU:** month-end holds against flat-by-close (A7) [I]; naive carry near zero since 2010 (A4) [V as sta
114:| FOMC-Day Short-USD Basket (D6 #6) | CONDITIONAL: "R:R unvalidated at 3:1 (low-freq 8/yr)" | C3; C9 (13:00–17:00 overlaps breaker #5) | One of several | A3 (8 trades a year, low power); A9 (spot 
117:| R3 FDAX/FESX last 30 minutes (D6 #7) | BLOCKED on infrastructure; noted "overlaps NQ tail" | C10 | No | **Yes:** Eurex not routed by MFFU (A9) [V]. |

### E19 Session-close: Noise-Area D6 line
$ cd /Volumes/Sensidine/Praxis.build && grep -n -o "Noise-Area breakout and its variants fail the D6 drawdown check (.f10603a.)" docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md
37:Noise-Area breakout and its variants fail the D6 drawdown check (`f10603a`)

### E20 Comparable builds: ORB repo surfaced (reference code, not a proposal)
$ cd /Volumes/Sensidine/Praxis.build && grep -n "IctOrbStrategyMBT" docs/reports/2026-11-04-comparable-builds.md | cut -c1-120
178:seamoors/ninjascript-strategies	IctOrbStrategyMBT.cs
188:seamoors/ninjascript-strategies/IctOrbStrategyMBT.cs

### E21 Filter audit: ORB on Stocks in Play row
$ cd /Volumes/Sensidine/Praxis.build && grep -n -E "^\| ORB on Stocks in Play" docs/reports/2026-11-08-strategy-filter-audit.md
115:| ORB on Stocks in Play (D2 #5) | Deprioritized: not the preferred class, fails cascade resistance, weak narrative | C2, C5, C8 | One of several | **Yes:** an equity universe not routable via MFFU futures (A9) [I]; the NQ version lacks evidence (A4) [V]. |

### E22 D5 (Round 3 handoff) location search
$ cd /Volumes/Sensidine/Praxis.build && find Redemtion docs -iname "*Handoff_Round3*" | grep -v -E "2026-10-28-f4-|/evidence/"; echo "found_exit=$?"
found_exit=1

```

De-identification check (the brief's command, run against this file before this paragraph was inserted; output pasted):
```
$ grep -c -i -w "$(ls /Volumes/Sensidine/Praxis.build/docs/reports | grep '^2026-10-28-f4-' | head -1 | sed 's/^2026-10-28-f4-//; s/-.*//')" /Volumes/Sensidine/Praxis.build/docs/reports/2026-11-13-strategy-review-index-worker2.md
0
```

## Gaps
1. **R1 and R2: who ran them, and when.** NOT IN RECORD. Neither RTF names a model (E15 counts 0 and 0), and neither text carries a date. "April 2026" comes from the folder name only.
2. **R3: which model ran it.** The prompt file instructs "Claude deep research" (E3), but no output file records the model. UNVERIFIED.
3. **D5 (the Round 3 handoff) was not found.** The filter audit lists it. The `find` in E22 returned no file.
4. **R3 per-agent artifacts were not read in full.** Only their title lines were read (E4). This index uses the compiled ranking at D6:31–40 and :42–44. A strategy that appears only inside an agent artifact and not in the compiled document is not indexed.
5. **CO-OC "in paper-trade validation".** This claim is at R3 prompts:36. No tracked file records any CO-OC paper trade or backtest (E13). NOT IN RECORD.
6. **The R6 design was not read.** It lives on branch `r6/announcement-research` at `bf6fcc7`, which is not on `main`. Only its subject line is cited. Its contents, and whether any R6 backtest has run, are UNVERIFIED. Bead `ckh` is OPEN (E9).
7. **The D6 drawdown result (`f10603a`) was not re-checked.** The Noise-Area D6 failure is cited from the session-close handoff, line 37 (E19).
8. **The LHM test and the Gemini/Kimi framing use different contract sizes.** The 2026-11-01 test was 1 NQ, while R7 and R8 framed their work at 1 MNQ. No MNQ run of LHM is in the record. The session-close claim that LHM lost money "before and after costs" is that channel's INFERRED arithmetic and was not re-checked here.
9. **The `.cs` header is stale.** `PraxisLastHalfHourMomentum.cs:19` still says "WRITTEN, NOT COMPILED, NOT TESTED" after the 2026-11-01 run (E16). This is reported, not fixed (out of scope; read-only).
10. **The Gemini Appendix A text is run together.** Its paragraphs have no line breaks between sections. Candidate positions come from `grep -o` (E10), and the rule details of each Gemini candidate are not pasted here. The session-close table and the Kimi C1–C4 restatement were used for the rules.
11. **Some status in the tables is the Claude.ai channel's word, not Amear's.** The session-close statuses for items 21–25 ("NOT TESTED; low", "DROPPED") are REPORTED BY that channel. No DECISIONS.md ID exists for them (E13).
12. **Filing-unit reports were not read.** The 2026-11-13 research-filing worker and manager reports are filing work, not research runs.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
