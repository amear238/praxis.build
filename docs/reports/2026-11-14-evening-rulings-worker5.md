# 2026-11-14 evening rulings - worker 5 (Q4 trade-count gap, Q5 2026-10-28 rule)

## Task
Read-only research on handoff docs/reports/2026-11-13-hermes-handoff-strategy-search.md :13 and :44 (Q4), and the status of the 2026-10-28 in-VM executor rule (Q5).

## Mode
BUILD (read-only research; only this report is written). HEAD 9ff8a48.

## Criterion
S1: every command and output pasted; grade OBSERVED vs INFERRED.

## Process log

### Batch 1 (Q4 greps)

```
$ git rev-parse --short HEAD
9ff8a48

$ sed -n '13p;44p' docs/reports/2026-11-13-hermes-handoff-strategy-search.md | cut -c1-600
- On why the 2026-11-13 VM run had 1,173 trades and the 2026-11-01 hand run had 1,190: "yesterday I basically changed the parameters so that it only trades from 9:30 a.m. onwards, right at the New York Open. And the back tests from November the first had the open via 8:30 a.m."
   4. **The trade-count gap is explained.** The 2026-11-13 VM runs trade from 09:30 ET. The 2026-11-01 hand runs used an 08:30 open. This bears on R1's re-run clause (DECISIONS.md :1551-:1555) for the three 2026-11-01 Noise-Area runs. Record the bearing; it does not change Noise-Area's status.

$ git show HEAD:DECISIONS.md | sed -n '1549,1557p' | cut -c1-400

RULINGS
R1  RTH = 09:30–16:00 ET (answers §4 item 1, B1). Arms (a) and (b)
    anchor at the 09:30 ET cash open. VM step 0 reads the live
    "CME US Index Futures RTH" template hours (T7 readback). If the
    live template starts 08:30 ET, the 2026-11-01 baselines are
    suspect and are re-run at 09:30 ET before either arm counts.
R2  GO requires arm (a) to pass. Arm (b) can only add confidence or
    block a GO; it can never carry a GO on its own (§4 item 3).

$ git grep -n -E '1,?190|1,?173' HEAD -- docs/reports DECISIONS.md STATUS.md | cut -c1-260 | head -40
HEAD:DECISIONS.md:259:- **(c) Why the fill-resolution choice does not decide the checkpoint order logic of this strategy, and where it may still bias the backtest:** the bead's premise ("enters on band-touch … INTRABAR events") does not match the code. `ninjas
HEAD:DECISIONS.md:626:7. Line 85 (R0 must reproduce *"1,190 trades and $197,327.60 exactly"*) and line 98 (*"total slippage 1190"*): these are pass bars the plan sets. The figures themselves are on record on the Mac: 1190 trades and net $197327.60 (`docs/repor
HEAD:DECISIONS.md:647:- **The plan** (line 28, verbatim): *"**Slippage under High: risk.** An NT staff forum post says slippage applies only under Standard. If that's true, a High run silently drops 2 ticks/side. That is the **F3 void-clause trigger**: if it i
HEAD:DECISIONS.md:714:42. Plan lines 85 and 98: whether "1,190 trades", "$197,327.60" and "total slippage 1190" are the R0/R1 pass bars (see b, item 7). New.
HEAD:DECISIONS.md:946:  - reading (voice agent, notes-4): Apply **$5.76 round trip all-in** ($2.88/side) in place of $2.96. Range $5.00–$5.80. Source: Tradeify's published NQ all-in and FundedNext's example (both REPORTED from web search in-call; MFFU's own fe
HEAD:DECISIONS.md:1003:2. In-VM automation (Oct 28 ruling): lifted COMPLETELY once two tests pass; until then it stands. a. cli-nt-bridge (MIT) drives the baseline from the terminal and reproduces 1,190 trades / ~$197,327 net on NQCONTROW. b. The VM agent load
HEAD:DECISIONS.md:1011:  - **2a** — cli-nt-bridge (MIT) drives the baseline from the terminal and reproduces 1,190 trades / ~$197,327 net on NQCONTROW. Those are his REPORTED figures. The committed baseline record is `docs/reports/2026-11-01-three-strategy-res
HEAD:DECISIONS.md:1044:4. For test 2a: is `docs/reports/2026-11-01-three-strategy-results.md:73` (1190 trades, $197327.60 net, `NQCONTROW SEP25`) the reference run, and does "reproduces" mean an exact match on trades and net, or a tolerance?
HEAD:DECISIONS.md:1063:Rulings 1. Bridge install (NEEDS AMEAR 2): the VM agent installs cli-nt-bridge via terminal, after a VMware snapshot. 2. Fees: apply MFFU's published round trip — NQ $4.68, MNQ $1.90 — by new DECISIONS entry amending the cost model. Cove
HEAD:DECISIONS.md:1087:| 4 — test 2a reference | "test 2a reference = 1,190 trades / $197,327.60 on NQCONTROW SEP25, exact match" | Exact match on 1,190 trades / $197,327.60, `NQCONTROW SEP25`; reference record `docs/reports/2026-11-01-three-strategy-results.m
HEAD:DECISIONS.md:1104:- Test 2a vs the fee amendment. The 2a reference figures were produced with commission $2.96 per trade (`docs/reports/2026-11-01-csv-analyses.md:51`, `commission/trade={'2.96': 1190}`). An exact-match reproduction (item 4) therefore need
HEAD:DECISIONS.md:1129:- **Arithmetic (no backtest):** +$1.72 per round turn against $2.96; over the 1,190 baseline trades, −$2,046.80, net $197,327.60 → $195,280.80 (`docs/reports/2026-11-05-mffu-fee-check.md:9`, `:96`). The baseline itself ran at $2.96 (see 
HEAD:DECISIONS.md:1264:- **Ruling 6 — Strategy Analyzer tab. Addendum-level statement to D-2026-11-06-A item 2 (DECISIONS.md:1003).** *Rules:* "Strategy Analyzer tab: a hand-set tab may be used for 2a and counts as "bridge reproduces the baseline". It does NOT
HEAD:DECISIONS.md:1413:- T1 (spec :180): run T1 (14, 1.0, 0, BandOrVWAP). Pass: the base file's trade list row for row and its totals, 1,190 / $197,327.60.
HEAD:DECISIONS.md:1415:- T3 (spec :184): run T3 (14, 1.0, 0, Flat1559). Pass: the `_Flat1559.cs` run row for row, 1,190 / $193,017.60.
HEAD:DECISIONS.md:1446:Reference figures at the committed $2.96 commission (`docs/reports/2026-11-01-three-strategy-results.md:402-404`, OBSERVED by `sed -n`): base 1,190 trades / $197,327.60; OppBand 810 / $210,182.40; Flat1559 1,190 / $193,017.60.
HEAD:DECISIONS.md:2087:**What it decides.** The VM agent for every step of `vm/2026-11-06-vm-handoff.md` is Hermes, driving the VM over SSH from the Mac (host alias `praxis-vm`) under its skill `praxis-vm-over-ssh`. The terms are in the CODE- reply `vm/replies
HEAD:DECISIONS.md:2154:2. The V7 strategy list at return-handoff :110, copied by script: "the Noise-Area baseline (test 2a: 1,190 trades / $197,327.60 on NQCONTROW SEP25) and its walk-forward; the three 2026-11-01 strategies; the R6 announcement variants (no N
HEAD:STATUS.md:322:- Baseline (BandOrVWAP): 1190 trades, net $197327.60, PF 1.29, max DD -$45282.04. [closing-line text elided by worker 5 so it occurs once]
HEAD:STATUS.md:324:- Flat1559: 1190 trades, net $193017.60, PF 1.28, max DD -$40637.04. [closing-line text elided by worker 5 so it occurs once]
HEAD:docs/reports/2026-10-28-nightly-checks-plan-review-rebuild.md:1191:$ cd /Volumes/Sensidine/Hemres.Planner && date; git show 4209004:docs/plans/2026-10-21-praxis-loop-plan.md | awk 'NR>=351&&NR<=353{printf "plan:%d\t%s\n",NR,$0}'; git show 4209004:docs/rep
HEAD:docs/reports/2026-10-30-zyd-f3-artifact.md:211:+- **(c) Why the fill-resolution choice does not decide the checkpoint order logic of this strategy, and where it may still bias the backtest:** the bead's premise ("enters on band-touch … INTRABAR events") d
HEAD:docs/reports/2026-10-30-zyd-worker10-closing-adversarial.md:38:| 20 | E13: section ranges D3 :737-773, Audit-1 §5 :1164-1173, §7 :1185-1207, D2 :688-735, §1 :1032-1083 | 3gm headers | `737:## D3`, `774:## D4`; `1164:### 5.`, `1175:### 6.`; `1185:### 7.`, 
HEAD:docs/reports/2026-10-30-zyd-worker2-adversarial.md:52:  `FlattenAll` sits before the checkpoint gate and runs on any bar with `mod >= 960`, not only at HH:00/HH:30. The cited D3 and §7 ranges also do not contain the `:105` or `:200` claims. Those are in R
HEAD:docs/reports/2026-10-30-zyd-worker2-adversarial.md:57:1173:**Corrected :103:** "... `Calculate = Calculate.OnBarClose` (line 105, OBSERVED). That `Close[0]` is then the close of a finished bar is NT8 runtime semantics (INFERRED; not observed on this insta
HEAD:docs/reports/2026-10-30-zyd-worker2-adversarial.md:168:- 3gm report `:5-8`, `:688-735`, `:737-775`, `:1028-1083`, `:1164-1173`, `:1185-1207`.
HEAD:docs/reports/2026-10-30-zyd-worker2-adversarial.md:203:- `:105` and `:200` are in R1, §5 `:1173` and D2(a), not in D3 or §7.
HEAD:docs/reports/2026-10-30-zyd-worker2-adversarial.md:205:Fix: `entry and checkpoint-exit decisions (:211, :219, :227, :229) are evaluated only at HH:00/HH:30 checkpoint bars (:196-198); the FlatEOD exits (:288, :290) are evaluated on any bar with mod >= Clo
HEAD:docs/reports/2026-10-30-zyd-worker4-readversarial.md:39:| M4 | RESOLVED (one range off by two lines) | Entry (c): "the FlatEOD exits (`:288`, `:290`) run on any bar with mod >= CloseMod (`:189`), a clock condition". Code :189 matches. Cited ranges checked
HEAD:docs/reports/2026-10-30-zyd-worker6-final-adversarial.md:20:- 3gm `:737-773` (D3) ✓. `:1164-1173` (§5 OnBarClose: "runtime half is INFERRED") ✓. `:1185-1207` (§7: market-order realisation INFERRED) ✓. `:688-735` (D2) ✓. D2(c) at `:716`: "CANNOT-DETERMINE-
HEAD:docs/reports/2026-10-30-zyd-worker8-final2-adversarial.md:28:The citations also check out: rubric `:55-56` (Unblocks when), O4 `:94-99`, SHM `:47-50`, F4 `:45` / `:151`, Q5/Q6/Q9 at DECISIONS `:185/:186/:189`, 3gm `:710`, `:737-773`, `:1164-1173`, `:1185-
HEAD:docs/reports/2026-10-31-voice-session-notes-2.md:23:1,190 trades (556 L / 634 S) · net $200,850.00 · gross profit $879,900.00 · gross loss −$679,050.00 · COMMISSION $0.00 · PF 1.30 · max DD −$44,545.00 · total slippage 1190 · avg trade $168.78 · largest w
HEAD:docs/reports/2026-10-31-voice-session-notes-2.md:26:(1) Commission $0.00, not 1,190 × $2.96. The PRAXIS template likely has no entry for this instrument.
HEAD:docs/reports/2026-10-31-voice-session-notes-2.md:27:(2) Trade count 1,190 ≠ 1,211, and L/S 556/634 ≠ 584/627, even though both spot bars match. Candidates: the stray Saturday file, Do-not-merge or rollover effects, tick rounding. Not diagnosed.
HEAD:docs/reports/2026-10-31-voice-session-notes-2.md:28:Slippage 1190 = 1,190 × 4 × 0.25 points, which fits 2 ticks/side applied.
HEAD:docs/reports/2026-10-31-voice-session-notes-2.md:40:  (slippage 1,190 = 1,190 × 4 × 0.25; largest winner $35,890 ≈ 20 × run-4's $1,792.50).
HEAD:docs/reports/2026-10-31-voice-session-notes-2.md:58:- Slippage: **1,190 points = 1,190 trades × 4 ticks × 0.25** — the 2-ticks-per-side assumption of
HEAD:docs/reports/2026-10-31-voice-session-notes-2.md:62:- **Commission $0.00** ≠ 1,190 × $2.96 = $3,522.40 → STOP condition met.
HEAD:docs/reports/2026-10-31-voice-session-notes-2.md:63:- **Total trades 1,190 ≠ 1,211; L/S 556/634 ≠ 584/627** → STOP condition met.
HEAD:docs/reports/2026-10-31-voice-session-notes-2.md:75:re-run: 1,190 × $2.96 = **$3,522.40** if the trade list is unchanged. Approved by Amear (R-A9D-3).

$ grep -rln -E '1,?173' docs/reports vm 2>/dev/null | head
docs/reports/2026-11-13-strategy-review-index-worker5.md
docs/reports/2026-10-30-zyd-worker4-readversarial.md
docs/reports/2026-11-11-vm-agent-hermes-correction-1-manager.md
docs/reports/evidence/2026-11-01-ninjatrader-grid-0759am.csv
docs/reports/evidence/2026-11-01-ninjatrader-grid-0800am.csv
docs/reports/evidence/2026-11-01-ninjatrader-grid-0710am.csv
docs/reports/evidence/2026-11-01-ninjatrader-grid-0757am.csv
docs/reports/2026-11-13-strategy-review-index-worker4.md
docs/reports/2026-11-13-research-filing-worker2.md
docs/reports/2026-10-30-zyd-worker8-final2-adversarial.md

$ git show HEAD:docs/reports/2026-11-01-three-strategy-results.md | grep -n -i -E 'noise|arm|trades|08:30|8:30|09:30|session' | head -30
12:This report does not grade F3, and it makes no claim that F3 is unfrozen; that needs an auditor grade. F2 (FROZEN): the early-close findings are only recorded here. No trading-hours template or session-flat rule is changed, proposed or decided. No strategy code or config was changed (Amear's brief). The report states facts and open questions only. Per R-1101-5 it gives no ranking of the strategies and no verdict between them.
16:- **OBSERVED**: read in data or command output in this session. Every value from a CSV or the bar file is OBSERVED, and the appendix holds the command and its output.
19:- **UNVERIFIED**: not checked in this session.
37:- No baseline screenshot exists. The baseline's settings and totals rest on Amear's C4 notes in `docs/reports/2026-10-31-voice-session-notes-2.md` section 3 (REPORTED BY AMEAR).
40:- Scripts: every script used is session scratch under `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/` and is **not in the repo**. Their sha256 values are in [K02] (OBSERVED). `screens.txt` is worker A's hand transcription of the Summary($) values (REPORTED BY AMEAR).
41:- Mapping from each CSV's `Strategy` column, all rows, [K03] `[1] Strategy` (OBSERVED): 07-10 = `PraxisNoiseAreaBreakout` (1190 rows), 07-57 = `PraxisNoiseAreaBreakout_OppBand` (810), 07-59 = `PraxisNoiseAreaBreakout_Flat1559` (1190), 08-00 = `PraxisLastHalfHourMomentum` (1304). Instrument `NQCONTROW SEP25` and Account `Backtest` on every row.
50:- **Conclusion (INFERRED** from the three facts above): the bar file and the grid CSVs use the same clock (offset 0), and that clock follows DST. The bars are end-stamped: the volume spike sits on the 09:31 stamp, not the 09:30 one. The identification as **US Eastern** wall time rests on general market-hours knowledge: cash open 09:30 ET, cash close 16:00 ET, CME daily halt 17:00-18:00 ET. That part is **UNVERIFIED** against an exchange document in this session. The NT8 platform time-zone setting is UNVERIFIED.
56:- **48 weekdays with no bar stamped 09:31..16:00** [K16 first line, K19] (OBSERVED). No CSV has a trade on any of them: 48 of 48 have `trades=[]` [K19]. They include the hole dates. The dates that still have some bars are listed in [K19]. Nine of them fall near the quarterly contract roll (INFERRED from timing): 2021-06-10, 2021-12-09, 2022-03-10, 2022-06-09, 2022-09-08, 2024-12-16, 2025-03-17, 2025-09-15, 2026-06-12. The roll link is INFERRED from the Mar/Jun/Sep/Dec timing only, and the holiday identity of the other dates is INFERRED from calendar knowledge.
57:- **The holes sit inside the 14-day lookback** of the NoiseAreaBreakout sessions right after them. INFERRED from the dates. The effect on the bands was **not analysed**.
63:- Missing stamps inside sessions, whole range: 184 stamps in 67 runs [K16]. 51 of those runs are on 2021-03-08..10 [K17], before the first NoiseAreaBreakout trade (2021-03-29 [K03 `[1] date span`]).
67:[K05] (CSV = OBSERVED; the `amear=` values are REPORTED BY AMEAR, from his C4 Summary and the C5 exit-name readback in notes-2 section 3): **all 22 compared values MATCH**. They are trades 1190, L 556 / S 634, net $197327.60, gross profit $878467.36, gross loss -$681139.76, commission $3522.40, PF 1.29, max DD -$45282.04 (both methods), avg trade $165.82, avg win $1815.02, avg loss -$964.79, W/L/E 484/706/0, largest win $35887.04, largest loss -$5407.96, long net $136314.24, short net $61013.36, and the exit counts Exit on session close 429, XS 429, XL 332. The CSV has no exit name outside that list.
71:| side | trades | net | gross profit | gross loss | commission | PF | W/L/E | % profitable | largest win | largest loss | avg trade | max DD (i) | max DD (ii) |
77:Max DD here is closed-trade cumulative net. Method (i) takes the peak from 0 and method (ii) the peak from the first trade, and the two give identical values. Baseline commission: 0 rows != $2.96; sum $3522.40 == 1190 x 2.96 [K03 `[4]`]. Baseline session-close exits fill at the CLOSE of the 16:00-stamped bar +/- 2 ticks: clamp model 423 of 423 [K12] (OBSERVED).
79:## Run 1: OppBand (`PraxisNoiseAreaBreakout_OppBand`, 07-57 CSV, screenshot 7.57.06)
100:| Exit on session close | checked | checked | MATCH |
103:| Exit mode | code default `OppBand` (`PraxisNoiseAreaBreakout_OppBand.cs:141` [K21]) | OppBand | MATCH |
106:| full strategy name | `PraxisNoiseAreaBreakout_OppBand` | prefix `PraxisNoiseAreaBreakout_Opp` (dropdown truncated) | NOT SHOWN |
110:**R-1101-4 test: 0 mismatches among the fields shown -> VALID on the shown fields; NOT SHOWN: the commission rate inside the PRAXIS template, and the full strategy name.** The NOT SHOWN items are not upgraded to pass. CSV facts that bear on them, OBSERVED, given separately: the Commission column is $2.96 on every row (0 rows differ) [K03 `[4]`], and the Strategy column reads `PraxisNoiseAreaBreakout_OppBand` on all 810 rows [K03 `[1]`].
114:| side | trades | net | gross profit | gross loss | commission | PF | W/L/E | % profitable | largest win | largest loss | avg trade | max DD (i) | max DD (ii) |
132:- Exit names: Exit on session close 792, XL 10, XS 8. **No `FlatEOD` exit appears.** The repo source has `ExitLong("FlatEOD")` / `ExitShort("FlatEOD")` at `PraxisNoiseAreaBreakout_OppBand.cs:314/316` [K21].
133:- Exit on session close by time: 16:00 784, 12:15 5, 12:00 2, 14:03 1. XL and XS exits are spread over 7 distinct times each [K03].
134:- Session-close fill reference [K13]: on the 784 16:00-stamped session-close exits, the fill is within 0.50 of the **CLOSE** of the 16:00-stamped bar on 784 of 784, and within 0.50 of that bar's OPEN on 33.
140:### f. Early-close and short-session exits (OBSERVED, [K24])
144:| 2021-11-26 | 13:15 | #90 | Short | 11:01 -> 12:15 | Exit on session close | 75 |
145:| 2023-04-05 | 14:03 | #312 | Short | 10:01 -> 14:03 | Exit on session close | 243 |
146:| 2024-07-03 | 13:15 | #514 | Long | 11:01 -> 12:15 | Exit on session close | 75 |
147:| 2024-11-29 | 13:15 | #576 | Long | 11:31 -> 12:15 | Exit on session close | 45 |
148:| 2024-12-24 | 13:15 | #583 | Long | 10:01 -> 12:15 | Exit on session close | 135 |
149:| 2025-01-20 | 13:00 | #594 | Long | 10:01 -> 12:00 | Exit on session close | 120 |
150:| 2025-06-19 | 13:00 | #652 | Short | 10:01 -> 12:00 | Exit on session close | 120 |

```

### Batch 2 (locating 1,173)

```
$ git grep -n -E '1,?173' HEAD -- vm docs | grep -v -E 'zyd-worker|evidence/' | cut -c1-300 | head -20
HEAD:docs/reports/2026-10-30-zyd-f3-artifact.md:211:+- **(c) Why the fill-resolution choice does not decide the checkpoint order logic of this strategy, and where it may still bias the backtest:** the bead's premise ("enters on band-touch … INTRABAR events") does not match the code. `ninjascript/Pra
HEAD:docs/reports/2026-11-06-cli-nt-bridge-code-read.md:180:| `ghostorders --cancel` | `target.Cancel(...)` (`:1173`) | no Sim-only check | [A14] |
HEAD:docs/reports/2026-11-06-cli-nt-bridge-code-read.md:442:1173:                            target.Cancel(cancelTargets);          // acts AFTER the locks (Lesson #159)
HEAD:docs/reports/2026-11-06-cli-nt-bridge-code-read.md:1328:1173:                             target.Cancel(cancelTargets);          // acts AFTER the locks (Lesson #159)
HEAD:docs/reports/2026-11-10-housekeeping-2a-manager.md:182:20ba6a34395e1173b3b788ade765dadc5bf3d2669f9838814a1f76b1791c0e36  -
HEAD:docs/reports/2026-11-10-vm-agent-hermes-ssh.md:19:- **Placement rule.** The CODE- reply was drafted outside the repo and written into vm/replies/ only once, after worker 4's PASS. There were two reasons: (a) a reply is never edited (vm/replies/README.md), and (b) the skill's gate 1 opens as soo
HEAD:docs/reports/2026-11-10-vm-agent-hermes-ssh.md:37:?? vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md
HEAD:docs/reports/2026-11-10-vm-agent-hermes-ssh.md:40:$ head -4 vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md
HEAD:docs/reports/2026-11-10-vm-agent-hermes-ssh.md:43:UTC: 20261110T211738Z
HEAD:docs/reports/2026-11-10-vm-agent-hermes-ssh.md:45:$ tail -1 vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md | grep -cxF '<the S13 sentence>'
HEAD:docs/reports/2026-11-10-vm-agent-hermes-ssh.md:48:23:- **Amendment 3 (2026-11-10):** the VM agent is now Hermes, driving the VM over SSH from the Mac (host alias `praxis-vm`), per the CODE- reply `vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md` 
HEAD:docs/reports/2026-11-10-vm-agent-hermes-ssh.md:54:vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md 1
HEAD:docs/reports/2026-11-10-vm-agent-hermes-ssh.md:64:   2 vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md:56:127.0.0.1
HEAD:docs/reports/2026-11-10-vm-agent-hermes-ssh.md:65:$ grep -c 20261110T211738Z
HEAD:docs/reports/2026-11-10-vm-agent-hermes-ssh.md:66:vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md:2
HEAD:docs/reports/2026-11-10-vm-agent-hermes-ssh.md:71:20261110T211738Z-CODE-vm-agent-hermes.md
HEAD:docs/reports/2026-11-10-vm-agent-hermes-ssh.md:83:$ set -o noclobber; echo x > vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md   # second write to a placed reply
HEAD:docs/reports/2026-11-10-vm-agent-hermes-ssh.md:84:(eval):1: file exists: vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md
HEAD:docs/reports/2026-11-10-vm-agent-hermes-ssh.md:116:- vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md (new)
HEAD:docs/reports/2026-11-11-v-rulings-filing-worker3.md:108:vm/replies CODE- files: 20261110T211738Z-CODE-vm-agent-hermes.md   (no CODE-cli-setup reply exists)

$ grep -n -E '1,?173' docs/reports/2026-11-13-strategy-review-index-worker5.md docs/reports/2026-11-13-strategy-review-index-worker4.md docs/reports/2026-11-13-research-filing-worker2.md docs/reports/2026-11-11-vm-agent-hermes-correction-1-manager.md | cut -c1-300 | head -20
docs/reports/2026-11-13-strategy-review-index-worker5.md:87:1. `docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md` (committed in 9ff8a48). VM bridge queue T1-T3 (bridge-driven Strategy Analyzer runs). Source `:5`: "the VM Claude Code session's own report, pasted to this channel by
docs/reports/2026-11-13-strategy-review-index-worker5.md:88:   - The "T1 reference (Amear's hand run)" of 1,173 trades (the 09:30 ET session-start run): no primary record found in `docs/reports`, STATUS.md or HANDOFF.md. The `1,173|176,392` grep (Evidence E11) hits only the 2026-11-13 handoffs and t
docs/reports/2026-11-13-strategy-review-index-worker5.md:300:$ grep -rn -E '1,173|176,392' docs/reports/*.md STATUS.md HANDOFF.md --exclude='2026-10-28-f4-*' | grep -v -E 'strategy-review-index|/evidence/' | cut -c1-120
docs/reports/2026-11-13-strategy-review-index-worker5.md:302:docs/reports/2026-11-13-research-filing-worker2.md:405:15:| T1 | BandOrVWAP | 1,173 | $176,392.92 | 1.2615 | -$38,9
docs/reports/2026-11-13-strategy-review-index-worker5.md:303:docs/reports/2026-11-13-research-filing-worker2.md:407:17:| T3 | BandOrVWAP | 1,173 | $176,392.92 | 1.26 | -$38,905
docs/reports/2026-11-13-strategy-review-index-worker5.md:306:docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md:15:| T1 | BandOrVWAP | 1,173 | $176,392.92 | 1.2615
docs/reports/2026-11-13-strategy-review-index-worker5.md:307:docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md:17:| T3 | BandOrVWAP | 1,173 | $176,392.92 | 1.26 |
docs/reports/2026-11-13-strategy-review-index-worker5.md:321:- The 1,173-trade "T1 reference (Amear's hand run)" at 09:30 ET: no primary record found in docs/reports, STATUS.md or HANDOFF.md (E11). NOT IN RECORD in the paths searched.
docs/reports/2026-11-13-strategy-review-index-worker4.md:202:   - `docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md:51` names a later "T1 reference: hand run 1,173 trades, net $176,392.92, PF 1.26, max DD $38,905.64". It is not one of the four 11-01 runs, so it is not indexed here.
docs/reports/2026-11-13-research-filing-worker2.md:405:15:| T1 | BandOrVWAP | 1,173 | $176,392.92 | 1.2615 | -$38,9
docs/reports/2026-11-13-research-filing-worker2.md:407:17:| T3 | BandOrVWAP | 1,173 | $176,392.92 | 1.26 | -$38,905
docs/reports/2026-11-11-vm-agent-hermes-correction-1-manager.md:49:$ mkdir -p /tmp/hermes-corr1-mgr-orig && cp -p docs/reports/2026-11-10-vm-agent-hermes-ssh*.md /tmp/hermes-corr1-mgr-orig/ && shasum -a 256 /tmp/hermes-corr1-mgr-orig/* docs/reports/2026-11-10-vm-agent-hermes-ssh*.md vm/replies/20261
docs/reports/2026-11-11-vm-agent-hermes-correction-1-manager.md:60:2b729b8e4469a1c3454dadba08ddcd9e48a387f201e583c5e326f66569ce2ed0  vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md
docs/reports/2026-11-11-vm-agent-hermes-correction-1-manager.md:120:$ tail -1 vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md | command grep -cxF '<the S13 sentence>'
docs/reports/2026-11-11-vm-agent-hermes-correction-1-manager.md:122:$ tail -1 vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md | command grep -cxF -- "$S13"
docs/reports/2026-11-11-vm-agent-hermes-correction-1-manager.md:125:vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md:2
docs/reports/2026-11-11-vm-agent-hermes-correction-1-manager.md:130:$ echo | command grep -c 20261110T211738Z
docs/reports/2026-11-11-vm-agent-hermes-correction-1-manager.md:132:$ command grep -c 20261110T211738Z vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md DECISIONS.md vm/2026-11-06-vm-handoff.md MANIFEST.md
docs/reports/2026-11-11-vm-agent-hermes-correction-1-manager.md:133:vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md:2
docs/reports/2026-11-11-vm-agent-hermes-correction-1-manager.md:220:$ for x in docs/reports/2026-11-10-vm-agent-hermes-ssh.md docs/reports/2026-11-10-vm-agent-hermes-ssh-worker1.md docs/reports/2026-11-10-vm-agent-hermes-ssh-worker2.md docs/reports/2026-11-10-vm-agent-hermes-ssh-worker3.md docs/repo

$ git ls-files --error-unmatch docs/reports/2026-11-13-strategy-review-index-worker5.md docs/reports/2026-11-13-research-filing-worker2.md docs/reports/2026-11-13-strategy-review-index-manager.md docs/reports/2026-11-13-hermes-handoff-strategy-search.md 2>&1 | cut -c1-200
error: pathspec 'docs/reports/2026-11-13-strategy-review-index-worker5.md' did not match any file(s) known to git
error: pathspec 'docs/reports/2026-11-13-strategy-review-index-manager.md' did not match any file(s) known to git
error: pathspec 'docs/reports/2026-11-13-hermes-handoff-strategy-search.md' did not match any file(s) known to git
Did you forget to 'git add'?
docs/reports/2026-11-13-research-filing-worker2.md

$ git show HEAD --stat | grep -i -E 'vm|bridge|t1|queue' | cut -c1-200 | head -20
    docs: file the four 2026-11-13 Claude.ai channel return handoffs (Gemini and Kimi strategy research with channel audits, session close with the PraxisLastHalfHourMomentum correction, VM bridge que
    Duplicate S13 lines deleted, first copy kept; a private name in pasted output redacted to [rep] with filer notes. Master under D-2026-11-08-D D1, DECISION_LOG 2026-11-13T19:40Z, 19:58Z (power-outa
 ...13-return-handoff-claude-ai-vm-queue-results.md |  44 ++

$ git show HEAD:docs/reports/2026-11-01-three-strategy-results.md | grep -n -E '^## |^# ' | head -30
1:# Three-strategy results readback - 2026-11-01
14:## Evidence grades
23:## Inputs
43:## Bar-file clock
53:## Data holes (shared by all four runs)
65:## Baseline re-derivation (07-10 CSV vs Amear's C4 values)
79:## Run 1: OppBand (`PraxisNoiseAreaBreakout_OppBand`, 07-57 CSV, screenshot 7.57.06)
185:## Run 2: Flat1559 (`PraxisNoiseAreaBreakout_Flat1559`, 07-59 CSV, screenshot 7.58.40)
303:## Run 3: LastHalfHourMomentum (`PraxisLastHalfHourMomentum`, 08-00 CSV, screenshot 8.00.21)
396:## Comparison (OBSERVED, [K08])
410:## Observations (flagged, not interpreted)
423:## Open questions for Amear
436:## Appendix: Commands and outputs

```

### Batch 3 (VM queue results, session close, T7)

```
$ git show HEAD:docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md | cat -n | cut -c1-420
     1	# Follow-up to the 2026-11-13 session-close handoff: VM bridge queue results (T1-T3)
     2	
     3	Written by the Claude.ai Praxis channel, 2026-11-13 about 14:45 ET. Read with `docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md`; this file replaces its "VM bridge queue" bullet, which said the channel had not seen the results.
     4	
     5	Source: the VM Claude Code session's own report, pasted to this channel by Amear at 14:37 ET (REPORTED BY Amear; the channel has not read the VM repo). The VM agent is the session working in `C:\praxis\vm-bridge` on the Windows VM. It is not praxis-master. Its results and commits live in that local git repo (no remote), with result files at `results\T1.json`, `results\T2.json`, `results\T3.json`. They are not 
     6	
     7	[closing-line text elided by worker 5 so it occurs once]
     8	
     9	## 1. Results (as reported by the VM agent)
    10	
    11	Setup: Strategy Analyzer tab "PRAXIS baseline NQCONTROW 0930", PraxisNoiseAreaBreakout, NQCONTROW SEP25, 1-minute, 2021-03-08 to 2026-07-17, CME US Index Futures RTH 0930 ET, commission PRAXIS $2.96 round trip, slippage 2, Standard fill resolution, 1 NQ.
    12	
    13	| Run | ExitMode | Trades | Net | Profit factor | Max drawdown | vs T1 reference (Amear's hand run) |
    14	|---|---|---|---|---|---|---|
    15	| T1 | BandOrVWAP | 1,173 | $176,392.92 | 1.2615 | -$38,905.64 | Exact match |
    16	| T2 | OppBand | 1,112 | $188,618.48 | 1.2861 | -$37,906.24 | -61 trades, +$12,225.56 net, DD $999.40 smaller |
    17	| T3 | BandOrVWAP | 1,173 | $176,392.92 | 1.26 | -$38,905.64 | Identical to T1 trade by trade (request id excepted); same file size, 219,831 bytes |
    18	
    19	- T1 run time about 19 seconds. `bridge.log` showed `param set: ExitMode="BandOrVWAP"`, `param set: Contracts=1`, `backtest: executing RunCommand`.
    20	- **ExitMode (an enum) is applied by the bridge:** `bridge.log` shows `param set: ExitMode="OppBand"` for T2, and T2's result differs from T1. The open question in the VM handoff ("T2 may equal T1 if the enum is not applied") is closed.
    21	- **The tab state is restorable:** T3 reproduced T1 exactly after T2, so a parameter change is cleanly overwritten. The tab was left at BandOrVWAP, 1 contract.
    22	- **No connection changes during any run:** no connect or disconnect lines in `bridge.log` while T1, T2 or T3 ran.
    23	- **Commission not compared:** the bridge's result files carry no commission total, so the hand run's $3,472.08 could not be checked.
    24	
    25	## 2. What went differently from the plan (REPORTED BY the VM agent)
    26	
    27	1. **First T1 attempt stopped, nothing ran:** NT8 had no Strategy Analyzer window open. Amear opened the tab by hand; the VM agent treated his explicit go as a new T1 run, not a retry, logged his words, and re-ran the pre-send checks.
    28	2. **NT8 restarted at 12:32:48 PM** (new process, PID 11820), between the two T1 attempts. Its startup reloaded the AddOn and connected the Sim feed (six new `bridge.log` lines), before any request was sent. The VM agent judged this normal startup, not a bridge action and not a breach of the "no connection lines during a run" rule, and logged it. **Who or what restarted NT8 is not stated in the report** (open)
    29	3. **`run-queue.ps1` was not used:** it needs the `claude` command, which is not installed on the VM. The VM agent ran the three tasks itself, one at a time, as the script's own fallback allows.
    30	4. **`tools\send-backtest.ps1` was changed:** extended so it can pass strategy parameters. It worked for all three runs.
    31	5. Timestamps are consistent with the VM clock now being correct: bridge.log 17:36:47 UTC for the T1 send, against Amear's report of a correct taskbar clock at about 12:27 ET (INFERRED by the channel).
    32	
    33	## 3. What this means (the channel's reading, INFERRED, not a ruling)
    34	
    35	- **The bridge works for headless backtests:** it reproduces a hand run exactly, applies parameters including enums, and leaves the tab restorable. That is the infrastructure result of the day. Walk-forward still needs the optimizer command, which is not allowed yet.
    36	- **These are Noise-Area numbers, kept for the record only** (D7 after the D6 drawdown check). T2's better net does not change that: at 1 MNQ its max drawdown would be about $3,790 (one tenth of $37,906.24), above the 50K gate of $1,600. Not a candidate.
    37	
    38	## 4. What's left (from the VM agent, with channel notes)
    39	
    40	1. **MFFU commission re-run:** Amear sets both PRAXIS commission rows to 2.34 by hand ($4.68 round trip); the VM agent then re-sends T1's parameters. Expected: 1,173 trades, net about $174,375.36 (channel check: 1,173 x $1.72 extra per round trip = $2,017.56 less than $176,392.92, which matches).
    41	2. **Sim feed check:** the VM agent still lists "check in the Control Center whether the Sim feed cycled when the AddOn loaded yesterday." Amear reported today (voice, about 12:30 ET) that he looked and saw no disconnect or reconnect. Whether today's Control Center view covers yesterday's load is not confirmed.
    42	3. **Later, not today:** Analyzer tabs for `PraxisNoiseAreaBreakout_Flat1559` and `PraxisLastHalfHourMomentum`, set by hand or via the bridge's `satemplate` command (needs Amear's OK). Channel note: `PraxisLastHalfHourMomentum` is retired (D-2026-11-02-A; session-close handoff section 2), so its tab is not needed unless Amear says otherwise.
    43	4. **Open:** what restarted NT8 at 12:32 PM.
    44	

$ git show HEAD:docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md | grep -n -i -E '1,?173|09:30|9:30|08:30|8:30|T1 reference|session start|template' | cut -c1-400
51:- **VM bridge queue:** Amear reported (about 14:30 ET) that the VM code agent has finished. The channel has NOT seen RESULTS.md, QUEUE.log or LOG.md and states nothing about the results. T1 reference: hand run 1,173 trades, net $176,392.92, PF 1.26, max DD $38,905.64, commission $3,472.08. If T2 (ExitMode=OppBand) equals T1 exactly, the bridge may not have applied the enum.

$ git grep -n -i 'T7' HEAD -- DECISIONS.md docs/reports | grep -i -E 'template|readback|08:30|09:30' | cut -c1-260 | head
HEAD:DECISIONS.md:1419:- T7 (spec :192): before every batch. Pass: the tab's commission template, backtest type, fill resolution and slippage read back as set ($2.96 acceptance, $4.68 walk-forward).
HEAD:DECISIONS.md:1553:    "CME US Index Futures RTH" template hours (T7 readback). If the
HEAD:DECISIONS.md:1619:- **R1 — RTH session.** *Answers:* return handoff `docs/reports/2026-11-07-return-handoff-claude-ai-2.md` §4 item 1 (B1 session start, :61-65). *Bears on:* values spec `docs/specs/2026-11-06-walk-forward-values.md` T12(iii) "the session'
HEAD:docs/reports/2026-11-06-wf-values-manager.md:41:7. A3 → T6 (static wiring check and band oracle) and T7 (Contracts, tab readback); minors fixed. **The entry's acceptance paragraph was edited in place after insertion** (lines 1191+ only; this unit's own un
HEAD:docs/reports/2026-11-06-wf-values-manager.md:366:463:- [2026-11-06T23:40:00Z] WHO: praxis-master | WHAT: **UNIT `2026-11-06-wf-values` — AUDIT FAIL 1 (S2 BLOCKING + S1; S8 PASS, fidelity to ruling 4 PASS); ONE correction dispatched (strike 1 of 2).** Audi
HEAD:docs/reports/2026-11-06-wf-values-manager.md:399:< 1. **Confirm or change every PROPOSED value** (ruling 4: "Report the exact values chosen back to me"): grid §3 (81 points); ATR, ATR warm-up and stop rules §4; objective, minimum trade count, no-eligible 
HEAD:docs/reports/2026-11-06-wf-values-manager.md:405:< **Acceptance test for the code unit.** At the committed runs' settings ($2.96 commission, so the reference figures apply): T1 ArmB (14, 1.0, Off, BandOrVWAP) = the base run row for row, 1,190 trades / $19
HEAD:docs/reports/2026-11-06-wf-values-manager.md:407:> **Acceptance test for the code unit.** At the committed runs' settings ($2.96 commission, so the reference figures apply): T1 ArmB (14, 1.0, Off, BandOrVWAP) = the base run row for row, 1,190 trades / $19
HEAD:docs/reports/2026-11-07-return-handoff-claude-ai-2.md:63:   - Which NT8 trading-hours template did the 2026-11-01 runs use, and will arm (b) use the same one? On record, REPORTED BY AMEAR (screenshots and his notes): `Trading hours` = `CME US Index Future
HEAD:docs/reports/2026-11-07-wf-values-fresh-manager.md:236:192:  - T7 (tab settings): before every batch the tab's settings (commission template, backtest type, fill res

$ git grep -n -i -E 'session template|trading hours template|template hours' HEAD -- docs/reports/2026-11-13*.md vm | cut -c1-260 | head
HEAD:vm/2026-11-06-vm-handoff.md:101:       "CME US Index Futures RTH" template hours (T7 readback). If the

```

### Batch 4 (template on record, 11-01 entry times, Noise-Area status)

```
$ git show HEAD:docs/reports/2026-11-07-return-handoff-claude-ai-2.md | sed -n '61,66p' | cut -c1-700
1. **B1 — session start.** The oracle fits the three committed 2026-11-01 base runs on all 3,190 trades (1190 + 810 + 1190, `scripts/wf/oracle/tests/test_baseruns.py:28–30`) for the m = 0 band/VWAP/policy part when sessions start at the 08:31-stamped bar. At 09:31 the baseline run fits 864/1190 entries, against 1190/1190 at 08:31; the 09:31 count was taken on the baseline run only (`docs/reports/2026-11-07-wf-oracles-manager.md` E5 :207–246; "Still the master's" items 1, 2, 11 at :352–362; "Questions only Amear can answer" 1–2 at :364–367).
   - Is 08:31–16:00 the session you mean by "RTH" (Q6, D-2026-11-07-A), or do arm (a)/(b) anchor at the 09:30 open?
   - Which NT8 trading-hours template did the 2026-11-01 runs use, and will arm (b) use the same one? On record, REPORTED BY AMEAR (screenshots and his notes): `Trading hours` = `CME US Index Futures RTH` for the runs in `docs/reports/2026-11-01-three-strategy-results.md:89`, `:195`, `:313`; the VM handoff sets the same name for 2a (`vm/2026-11-06-vm-handoff.md:205`). One earlier read exists: an adversarial worker on 2026-10-31 printed a RESCUED copy of `CME US Index Futures RTH.xml` as Monday–Friday `830`–`1600`, TimeZone `Eastern Standard Time` (`docs/reports/2026-10-31-o78-worker4-report-adversarial.md:208–219`, committed `29c3e13`; REPORTED BY that worker, not re-run here). That was a re
   - The master has a hypothesis about the cause (`21:42:00Z` item (2)). It is UNVERIFIED.
   - No spec wording changes before your word (`21:42:00Z` item (5)). The lines that bear on it: T12(iii) "VWAP from the 09:30 bar" (`docs/specs/2026-11-06-walk-forward-values.md:206`) and §4 "RTH sessions" (`:72`).
2. **Tier pick** (Q9): yours after paper results, not now (`docs/reports/2026-11-07-wf-mac-side-maths-manager.md:591`).

$ git show HEAD:DECISIONS.md | sed -n '1619,1622p' | cut -c1-900
- **R1 — RTH session.** *Answers:* return handoff `docs/reports/2026-11-07-return-handoff-claude-ai-2.md` §4 item 1 (B1 session start, :61-65). *Bears on:* values spec `docs/specs/2026-11-06-walk-forward-values.md` T12(iii) "the session's typical-price VWAP from the 09:30 bar" (:206) and §4's ATR line "the last 14 completed RTH sessions" (:72) (both pointers REPORTED BY the return handoff :65; re-read here, OBSERVED); VM handoff step 0 (see R1 in the block above). Master's reading (filing note 2, :87), changeable by Amear: `docs/reports/2026-10-31-o78-worker4-report-adversarial.md:208-219` at commit `29c3e13` prints a RESCUED copy of `CME US Index Futures RTH.xml` as Monday–Friday `830`–`1600`, TimeZone `Eastern Standard Time` (REPORTED BY that worker). The live VM template is UNVERIFIED. Conditional, per bd memory `amear-conditional-commitment`: nothing here asserts what the live templa
- **R2, R3 — which arm carries GO; gate 6.** *Answer:* return handoff §4 item 3 (:67) (his words: "(§4 item 3)" for each); R2 ↔ the part "whether GO / HOLD / REJECT may rest on arm (b)" and R3 ↔ "whether gate 6 applies to arm (a)" is the filer's assignment (INFERRED, the filer's, not his word). *Bear on:* values spec §8 :128 ("Judged arm = (a)" vs Q8 "both arms are judged against all six Phase 3 gates"), :132 (ii) and (iii), :133 ("The WFE formula for arm (b) … OPEN"); O1 (`specs/SPEC_RUBRIC.md:74-79`). Side by side, not reconciled here (INFERRED, the filer's, not his word): R3 "Gate 6 (WFE) applies to arm (b) only" and Q8 at values spec :121 "both arms are judged against all six Phase 3 gates"; raised to the master in the unit report. *Do NOT settle:* whether R2/R3 discharge O1 — the values spec :134 leaves "Whether Q8 discharges O1" to "the master and the auditor"; that the same holds 
- **R4 — scoring, hybrid.** *Answers:* §4 item 3's "the gate 2 Sharpe definition and its equity base" (his words: "(§4 item 3, gate 2)"; the sub-part is the filer's assignment (INFERRED, the filer's, not his word)). R4 instructs "flag any conflict back to Amear, do not resolve it". Master's reading (filing note 3, :88), changeable by Amear, names the same checks. The checks are NEEDS AMEAR FLAGS 1–5 below. *Does NOT settle:* any of FLAGS 1–5; the values spec is not edited.
- **R5 — R:R shape filter.** *Answers:* strategy filter audit `docs/reports/2026-11-08-strategy-filter-audit.md` §6 Q1 (:211). *Bears on:* filter C3 (audit :88; §4.1 at :127). R5's words name "The fixed R:R shape filter (3:1 partial plus runner; 1.5:1)"; that this is the audit's C3 is INFERRED, the filer's, not his word — C3's cell at :88 also carries "avg win ÷ avg loss < 1.5 fails regardless of win rate", a clause R5's words do not name, so whether that clause is retired with it is not settled here. *Bears on:* the higher-win-rate brief requested in `docs/reports/2026-11-04-voice-session-notes-4.md:36` ("New work requested by Amear" item 1, heading :35) and audit :144. The audit is "recommendation only … **PROPOSED**" (:4), by the Claude.ai channel research agent (:3). *Does NOT settle:* the audit's other C filters and its §5 ranking are not adopted by this entry — R5's words rule on t

$ git show HEAD:docs/reports/2026-11-01-three-strategy-results.md | grep -n -i -E 'entry time|entries by time|first entry|earliest|09:3|10:01|before 09|trading hours|template' | cut -c1-300 | head -20
12:This report does not grade F3, and it makes no claim that F3 is unfrozen; that needs an auditor grade. F2 (FROZEN): the early-close findings are only recorded here. No trading-hours template or session-flat rule is changed, proposed or decided. No strategy code or config was changed (Amear's brie
47:- **Offset test** [K10] (OBSERVED): baseline + Flat1559 entries (n=2380) were compared with the OPEN of the bar stamped at the entry time shifted by -3h..+3h. At offset +0h, 2338 are 2 ticks adverse, 18 are 1 tick adverse and 24 are exact, with 0 "other" and 0 "nobar". The split is the same in DS
50:- **Conclusion (INFERRED** from the three facts above): the bar file and the grid CSVs use the same clock (offset 0), and that clock follows DST. The bars are end-stamped: the volume spike sits on the 09:31 stamp, not the 09:30 one. The identification as **US Eastern** wall time rests on general 
56:- **48 weekdays with no bar stamped 09:31..16:00** [K16 first line, K19] (OBSERVED). No CSV has a trade on any of them: 48 of 48 have `trades=[]` [K19]. They include the hole dates. The dates that still have some bars are listed in [K19]. Nine of them fall near the quarterly contract roll (INFERR
59:  - "2024-07-19 10:01" is really 10 missing RTH stamps, 09:58-10:07.
89:| Trading hours | CME US Index Futures RTH | CME US Index Futures RTH | MATCH |
92:| Commission template | PRAXIS | PRAXIS | MATCH |
110:**R-1101-4 test: 0 mismatches among the fields shown -> VALID on the shown fields; NOT SHOWN: the commission rate inside the PRAXIS template, and the full strategy name.** The NOT SHOWN items are not upgraded to pass. CSV facts that bear on them, OBSERVED, given separately: the Commission column
138:Qty != 1: 0. Duplicate entry times: none. Overlapping positions (next entry before this exit): 0. A same-timestamp exit followed by an entry happens 18 times, with first examples (16, 17), (27, 28).
145:| 2023-04-05 | 14:03 | #312 | Short | 10:01 -> 14:03 | Exit on session close | 243 |
148:| 2024-12-24 | 13:15 | #583 | Long | 10:01 -> 12:15 | Exit on session close | 135 |
149:| 2025-01-20 | 13:00 | #594 | Long | 10:01 -> 12:00 | Exit on session close | 120 |
150:| 2025-06-19 | 13:00 | #652 | Short | 10:01 -> 12:00 | Exit on session close | 120 |
151:| 2025-07-03 | 13:15 | #657 | Long | 10:01 -> 12:15 | Exit on session close | 135 |
174:| first 5 | 1 | Short | 2021-03-29 10:01 -> 16:00 | 16270.25/16371.00 | S -> Exit on session close | -$2017.96 | 360 |
175:| first 5 | 2 | Long | 2021-03-31 10:01 -> 16:00 | 16468.50/16504.00 | L -> Exit on session close | $707.04 | 360 |
176:| first 5 | 3 | Long | 2021-04-05 10:01 -> 16:00 | 16892.50/16998.50 | L -> Exit on session close | $2117.04 | 360 |
177:| first 5 | 4 | Long | 2021-04-13 10:01 -> 16:00 | 17358.00/17391.25 | L -> Exit on session close | $662.04 | 360 |
181:| last 5 | 808 | Short | 2026-07-07 10:01 -> 16:00 | 29468.25/29393.00 | S -> Exit on session close | $1502.04 | 360 |
195:| Trading hours | CME US Index Futures RTH | CME US Index Futures RTH | MATCH |

$ grep -n -i 'noise' STATUS.md HANDOFF.md | cut -c1-260 | head -20
STATUS.md:373:**Delivered for the hand test:** `PraxisNoiseAreaBreakout_OppBand.cs`, `PraxisNoiseAreaBreakout_Flat1559.cs`, `PraxisLastHalfHourMomentum.cs`, each at the WRITTEN level with a one-page checklist; audited PASS (one correction on the DECISIONS appe
STATUS.md:385:**Phase: Block 2 — Backtesting. F1, F2, F4 FROZEN and untouched. F3 one commit away from unfreezing.** Measured at 00:41Z: `HEAD` `4d7ca80` (unpushed), 28 paths staged, 67 untracked, 0 stashes. No trading code moved; `ninjascript/PraxisNoiseAreaB
STATUS.md:393:**2026-10-31 morning, update:** Amear reversed the overnight hold ("Run them now"); commits 2 and 3 landed (`4ec75ea`, `fab2855`). `7zq` ran as three managers and three audits and is **committed `0ced412`**: two Noise-Area variants (OppBand corre
STATUS.md:545:**Last updated:** 2026-07-25 (session 29 — **852 VM-agent delegation workspace LIVE EXECUTOR LEG PROVEN — 852 now closeable; wx7 external build-progress report SHIPPED (497088b). No new repo commit for the 852 proof (artifact lives outside the re
STATUS.md:548:Block 2 of 6 — Backtesting (Block 1 milestone trader-signed-off 2026-07-15 — DECISIONS.md "Block 1 milestone" entry; evidence audit d405125). **Q1 RESOLVED + trader-confirmed 2026-07-15 (session 14):** strategy = Zarattini-Aziz-Barbon NQ Noise-Ar
STATUS.md:557:- **🔴 4uu NT8 re-import (Block-2 critical path) — TRADER/VM-gated:** the ET continuous series exists on disk but must be re-imported to NT8, then PraxisNoiseAreaBreakout.cs compiled + Strategy-Analyzer reconciled. This is the ONLY thing between h
STATUS.md:584:- **🔴 FIRST ACTION — check for 4uu output.** The v2 brief was handed to the Cowork agent this session; VM work was IN PROGRESS at close. On boot: `ls ~/praxis-signals/b2-data/inbound/` — if new import/compile/Strategy-Analyzer output has landed (
STATUS.md:606:- **✅ 4uu file-readiness INDEPENDENTLY AUDITED + PASSED (bead 4uu.1 CLOSED):** the VM's 7/17 `PraxisNoiseAreaBreakout.cs` hash "mismatch" was a CRLF line-ending artifact, NOT stale code — proven byte-identical to committed 719ab11 (LF sha256 `353
STATUS.md:607:- **🔴 FIRST ACTION — 4uu (P1, TRADER/VM):** F5-compile the (proven-current) `PraxisNoiseAreaBreakout.cs` → import `NQ-continuous-1min.csv` as a custom 1-min series → Strategy Analyzer (RTH 09:30–16:00 ET, ExitMode=BandOrVWAP, Contracts=1, ≥3 mo) 
STATUS.md:614:- **🔴 FIRST ACTION — 4uu (P1, TRADER/VM):** re-import NQ-continuous-1min.csv into NT8 as a custom 1-min series → compile `ninjascript/PraxisNoiseAreaBreakout.cs` (F5) → load in Strategy Analyzer on the imported series → reconcile sample entries v
STATUS.md:624:- **Then 4uu (VM):** once the ET continuous series exists + is re-imported to NT8 — compile PraxisNoiseAreaBreakout.cs + Strategy-Analyzer reconcile. Then the chain **zi1 (WFA) → ajj (MC) → xdr (refdist)**.
STATUS.md:648:   **VM queue for 4uu:** compile ninjascript/PraxisNoiseAreaBreakout.cs in NT8 (F5) → load in Strategy Analyzer on the b2-data NQ 1-min series (roll=vol/OI + Difference) → reconcile sample entry signals vs known live/sim TV alerts (procedure: doc
HANDOFF.md:9:- `661e073` entry D-2026-11-13-C (OPEN-A2: every Noise-Area arm keeps the full-day window to the 16:00 ET flat; an earlier strategy stop is allowed for a later arm only through that arm's own DECISIONS entry, written before it is built and graded 
HANDOFF.md:187:- `bf11fbd` bead `fgd` part A: appended, dated amendment notes in the topology doc, the Noise-Area ruleset and the F2 proposal so they read in line with amended #4 (16:00 flat gate) and #5 (operator lockout only). Bodies unchanged. No new design
HANDOFF.md:215:3. Other open work not blocked by `ckh`: bead `fgd` (align topology doc, Noise-Area ruleset, WF values, `_Flat1559.cs` comment with amended #4/#5); rubric O3/O4 gradeable; broker route (MFFU does not offer Rithmic; D-2026-11-10-B contradicted, n
HANDOFF.md:248:2. Bead `fgd`: align the topology doc, Noise-Area ruleset, WF values and `_Flat1559.cs` comment with amended #4/#5 (spec/doc edits; the `.cs` comment is code, a manager unit).
HANDOFF.md:787:- **No long/short code asymmetry** in `PraxisNoiseAreaBreakout.cs` (seven sites mirrored, auditor re-read). The short-side loss is market/data/engine; nine hypotheses with Trades-tab falsifiers.
HANDOFF.md:808:### ✅ DONE 2026-10-31 12:40Z — `Praxis_build-7zq` COMMITTED `0ced412`, pushed, verified. Three backtest strategies on disk and in `main`: `ninjascript/PraxisNoiseAreaBreakout_OppBand.cs` (opposite-band stop, default OppBand; needs the base insta
HANDOFF.md:1400:2. **F3 — reframed, and the reframing is the session's real product.** A browser research agent (the praxis stack has no web tools, and `Agent(general-purpose)` is denied by `projectSettings`) returned a graded brief. Its decisive question was 
HANDOFF.md:1410:- **F2's 15:00 disposition.** A trading decision. Note the contradiction is already shipped: the code hard-codes flat at 16:00 (`PraxisNoiseAreaBreakout.cs:101`) while breaker #4 says 11:30.

$ grep -n -i 'noise' docs/reports/2026-11-13-strategy-review-index-manager.md | cut -c1-260 | head -20
5:2. Three are Noise-Area breakout arms (baseline, OppBand, Flat1559): each made money at 1 NQ, profit factor 1.26 to 1.29, max drawdown -$40637.04 to -$50748.88 as written.
7:4. The D6 drawdown check (f10603a) found all three Noise-Area arms fail every MFFU account size at 1 MNQ on the committed measure (MNQ derived from the NQ trade lists, not an MNQ run); the 50K ceiling is $1,600.
8:5. D7 says "The Noise-Area baseline continues through the VM tests for the record, but a GO on MFFU is not expected from it"; DECISIONS.md does not say whether OppBand and Flat1559 share that status. No walk-forward has been run, and A20 was a connection che
10:7. Only two research ideas were ever backtested (Noise-Area and Last-Half-Hour Momentum); TORB/ORB and the R6 announcement strategies are written specs or designs only, with no code.
14:11. Indicators appear only inside Noise-Area (VWAP is its coded exit; an ATR stop is written, not run) and as a few screened-out ideas (VWAP/Bollinger reversion, standalone ORB, order flow).
51:- Baseline `PraxisNoiseAreaBreakout`, BandOrVWAP, :402: 1190, $197327.60, 1.29, -$45282.04, 40.67%, $165.82. Status: no DECISIONS.md entry retires or adopts it. It is listed as a walk-forward exit policy (DECISIONS.md:1077). D7 names it: "The Noise-Area bas
52:- OppBand `PraxisNoiseAreaBreakout_OppBand`, :403: 810, $210182.40, 1.26, -$50748.88, 58.02%, $259.48. Status: no DECISIONS.md entry retires or adopts it; listed as a walk-forward exit policy (DECISIONS.md:1077); definition ruled at :1222. Whether D7's "for
53:- Flat1559 `PraxisNoiseAreaBreakout_Flat1559`, BandOrVWAP exits, flat on the 15:59 bar, :404: 1190, $193017.60, 1.28, -$40637.04, 40.50%, $162.20. Status: no DECISIONS.md entry retires or adopts it; fill accepted at :504, definition ruled at :1223, exit pol
68:- D6 (DECISIONS.md:1930-1939) ordered a Mac-only drawdown check on the three 2026-11-01 Noise-Area trade lists, per walk-forward window, at 1 MNQ and 1 NQ. It was committed in `f10603a` (`docs/reports/2026-11-09-d6-drawdown-check-manager.md`).
70:- D7 (DECISIONS.md:1940-1944) applies if D6 fails at every tier at 1 MNQ: do not fit breaker values to the ceiling; pull R6 research forward to P0; "The Noise-Area baseline continues through the VM tests for the record, but a GO on MFFU is not expected from
71:- Status after D6/D7: D7 and the D6 report (:45) name only "The Noise-Area baseline" as continuing "through the VM tests for the record". DECISIONS.md does not state the status of OppBand and Flat1559 after D7. No retirement entry exists for any of the thre
81:- R1 and R2 (April 2026, gitignored RTFs in `Redemtion/Intitialization-April 2026/`). R1 is an NQ/ES shortlist; R2 covers higher-frequency strategies to pair with Noise-Area. The model that produced them is NOT IN RECORD.
92:- Only two ideas were ever backtested, both in the 2026-11-01 hand runs. One is Noise-Area with its variants. The other is Last-Half-Hour Momentum (Baltussen et al. 2021), retired by D-2026-11-02-A (DECISIONS.md:368, :383 "is **removed from the active candi
116:- Session VWAP is CODED as the default exit of `PraxisNoiseAreaBreakout`. `.cs:46`: "BandOrVWAP = paper's PREFERRED model, trailing stop at max/min(band, VWAP) (§4 p.13). DEFAULT." (E3.1). It was backtested as that strategy's exit: the 2026-11-01 table row
133:- Setup: vm-queue :11, tab "PRAXIS baseline NQCONTROW 0930", PraxisNoiseAreaBreakout, NQCONTROW SEP25, 1-minute, 2021-03-08 to 2026-07-17, RTH 0930, commission $2.96 round trip, slippage 2, Standard fill resolution, 1 NQ.
138:- Channel's status call (vm-queue :36): "These are Noise-Area numbers, kept for the record only (D7 after the D6 drawdown check)". Its 1 MNQ figure "about $3,790 (one tenth of $37,906.24), above the 50K gate of $1,600" is the channel's arithmetic, not a ru
156:- Analyzer tabs for `PraxisNoiseAreaBreakout_Flat1559` and `PraxisLastHalfHourMomentum` are "Later, not today", using `satemplate`, which "needs Amear's OK" (vm-queue :42).
166:- S2-A (medium), "kept for the record" extended to all three Noise-Area arms: D7 and the D6 report name only "The Noise-Area baseline". Summary line 5 and the Q1 status lines now say DECISIONS.md does not state the OppBand and Flat1559 status after D7, and
185:- Block 2 (strategy, backtests): every recorded Noise-Area result is a Standard-resolution, 1-minute, breaker-less backtest. The judged High-resolution, breakers-on version has not been run (D6 report :56).
200:402:| BASELINE (`PraxisNoiseAreaBreakout`, BandOrVWAP) | 1190 | $197327.60 | 1.29 | -$45282.04 | -$45282.04 | 40.67% | $165.82 | $35887.04 | 18.19% |

```

### Batch 5 (R1 re-run record, rescued template)

```
$ grep -n -i -E 're-run at 09:30|rerun at 09:30|baselines are suspect|R1 re-run|R1.s re-run|0930' DECISION_LOG.md | cut -c1-260 | tail -12
718:- [2026-11-08T14:02:11Z] **WHO: amear** | WHAT: **NINE RULINGS R1–R9 FROM HIS 2026-11-08 VOICE SESSION (Claude.ai channel), PLUS A HOUSEKEEPING LIST AND A "STILL OPEN" LIST — pasted by Amear into this session as the opening message.** The paste is filed ve
719:- [2026-11-08T14:22:00Z] WHO: praxis-master | WHAT: **SESSION OPEN; READ DONE; U1 `2026-11-08-rulings-filing` DISPATCHING.** Ledgers read: STATUS.md 11-07 evening section, HANDOFF.md 11-07 card, DECISION_LOG tail through `22:18:00Z`, DISPATCH_LOG tail, DEC
737:- [2026-11-08T17:01:00Z] WHO: praxis-master | WHAT: **U7 `2026-11-08-wf-spec-amendment` RETURNED (60 tool uses — at the cap — ~47 min, ~190k tokens; `Result: PASS at level WRITTEN`; three adversary rounds: R1 REFUTED 3 MAJOR, R2 REFUTED 1 MAJOR, R3 `GRADE:
768:- [2026-11-09T18:34:00Z] WHO: praxis-master | WHAT: **VM handoff amendment 2 manager returned (corr a4f12311d43f0709d, 47 tool uses, ~19 min), self-graded PASS at level WRITTEN; master read the report (549 lines: process log, line index, S6, Open list, sel
944:- [2026-11-14T01:28:05Z] WHO: amear | REPORTED BY: the Claude.ai channel, in `docs/reports/2026-11-13-hermes-handoff-strategy-search.md` :5-:17, which Amear pasted into this session and then approved here ("go from here", 01:25:40Z row) | WHAT: **Amear's 2

$ git grep -n -i -E 're-run at 09:30|baselines are suspect|R1 re-run|re-run clause|0930' HEAD -- DECISIONS.md STATUS.md HANDOFF.md docs/reports/2026-11-1*.md | cut -c1-260 | head -15
HEAD:DECISIONS.md:1555:    suspect and are re-run at 09:30 ET before either arm counts.
HEAD:DECISIONS.md:1619:- **R1 — RTH session.** *Answers:* return handoff `docs/reports/2026-11-07-return-handoff-claude-ai-2.md` §4 item 1 (B1 session start, :61-65). *Bears on:* values spec `docs/specs/2026-11-06-walk-forward-values.md` T12(iii) "the session'
HEAD:DECISIONS.md:1634:**S4 timing.** This entry is written before any unit that depends on R1–R9 is dispatched. The dependents are U2–U5 in the DECISION_LOG `2026-11-08T14:22:00Z` plan: U2 housekeeping, including the read of MFFU's current terms; U3 VM handof
HEAD:docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md:11:Setup: Strategy Analyzer tab "PRAXIS baseline NQCONTROW 0930", PraxisNoiseAreaBreakout, NQCONTROW SEP25, 1-minute, 2021-03-08 to 2026-07-17, CME US Index Futures RTH 0930 ET, commissi

$ grep -n -i -E '0930|09:30|R1|re-run' docs/reports/2026-11-13-hermes-handoff-strategy-search.md | cut -c1-300 | head -20
35:   - `docs/reports/2026-11-13-strategy-review-index-worker1.md` through `-worker7.md`
44:   4. **The trade-count gap is explained.** The 2026-11-13 VM runs trade from 09:30 ET. The 2026-11-01 hand runs used an 08:30 open. This bears on R1's re-run clause (DECISIONS.md :1551-:1555) for the three 2026-11-01 Noise-Area runs. Record the bearing; it does not change Noise-Area's status.
64:4. **Backtest it through the VM bridge** queue, dispatched by Hermes over SSH as on 2026-11-13. No Claude Code runs inside the VM. Settings match the 2026-11-01 runs: NQCONTROW, 1-minute bars, 2021-03-08 to 2026-07-17, Standard fill resolution, 2 ticks of slippage per side, 1 NQ. Trading runs 09:

$ git show HEAD:docs/reports/2026-10-31-o78-worker4-report-adversarial.md | sed -n '208,219p' | cut -c1-200
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

```

### Batch 6 (Q5 tests 2a/2b, NEEDS AMEAR 6)

```
$ grep -n -o -E '.{0,140}(1,173|08:30 open|9:30 a\.m).{0,110}' DECISION_LOG.md | cut -c1-260 | tail -6
944:nt to pause all builds until there's 3 contenders for the strategy." Voice quotes, transcribed, at handoff :13-:15. They cover the 09:30 vs 08:30 open, and Claude Code put on the VM by hand ("Those rules are for you, not for me"). The rulings as the handof
944:2) builds pause until three contenders exist; (3) the search loop runs in Claude Code; (4) the trade-count gap is explained by the 09:30 vs 08:30 open, with its bearing on R1's re-run clause recorded; (5) the 2026-10-28 rule (DECISIONS.md :1010) still bind

$ sed -n '64p' docs/reports/2026-11-13-hermes-handoff-strategy-search.md | cut -c1-500
4. **Backtest it through the VM bridge** queue, dispatched by Hermes over SSH as on 2026-11-13. No Claude Code runs inside the VM. Settings match the 2026-11-01 runs: NQCONTROW, 1-minute bars, 2021-03-08 to 2026-07-17, Standard fill resolution, 2 ticks of slippage per side, 1 NQ. Trading runs 09:30–16:00 ET (R1), flat by 16:00.

$ git show HEAD:DECISIONS.md | sed -n '1003p;1010,1013p' | cut -c1-700
2. In-VM automation (Oct 28 ruling): lifted COMPLETELY once two tests pass; until then it stands. a. cli-nt-bridge (MIT) drives the baseline from the terminal and reproduces 1,190 trades / ~$197,327 net on NQCONTROW. b. The VM agent loads a written skill and follows it correctly on a simple job. First confirm the VM's Cowork agent can load skills. Order: read the bridge's code read-only; write an install walkthrough; VMware snapshot first; then install. Direction: the walk-forward runs in NT8 through the bridge, not in a Mac-side Python copy.
- **Item 2 — in-VM automation.** The "Oct 28 ruling" is ruling (1) of `docs/reports/2026-10-28-voice-session-notes.md:7` (untracked file), "The in-VM automation approach is dropped. No more Cowork or in-VM Claude Code executor work.", taken onto the ledger at DECISION_LOG `2026-10-30T21:36:00Z` (WHO: amear). (filer's identification) DECISIONS.md has no entry for it. In his words it is "lifted COMPLETELY once two tests pass; until then it stands." How far "COMPLETELY" reaches beyond that ruling is not stated (NEEDS AMEAR 6). The two tests:
  - **2a** — cli-nt-bridge (MIT) drives the baseline from the terminal and reproduces 1,190 trades / ~$197,327 net on NQCONTROW. Those are his REPORTED figures. The committed baseline record is `docs/reports/2026-11-01-three-strategy-results.md:73` (committed in `8ca9861`): `| All | 1190 | $197327.60 | …`, instrument `NQCONTROW SEP25` (`:86`); `:67` grades the CSV values OBSERVED and the `amear=` values REPORTED BY AMEAR. The repo's record of the bridge (its code is not in the repo): `docs/reports/2026-11-04-comparable-builds.md:65`, eman007/cli-nt-bridge, MIT, "implemented; untested on 8.1.7.2".
  - **2b** — the VM agent loads a written skill and follows it correctly on a simple job, after first confirming that the VM's Cowork agent can load skills.
  - **Order he set:** read the bridge's code read-only → write an install walkthrough → VMware snapshot first → then install. Filer's pointer: R-VN4-13 is Amear's "Yeah, just do the snapshot." (DECISIONS.md:960); the voice agent's reading of it (`:961`, not his words) lets add-ons go on "after a VMware snapshot", and the bridge is recorded as a "third-party AddOn" (`docs/reports/2026-11-04-comparable-builds.md:216`). Whether R-VN4-13 covers the bridge is not ruled here.

$ git grep -n -i -E 'test 2a|test 2b|2a and 2b|tests 2a|2a pass|2b pass' HEAD -- DECISIONS.md docs/reports vm | cut -c1-260 | head -30
HEAD:DECISIONS.md:1014:  - **Direction he set:** the walk-forward runs in NT8 through the bridge, not in a Mac-side Python copy. The open question it bears on is the step-c harness question at DECISION_LOG `2026-11-06T00:54:04Z`: "arm (a) can only run in NT8 o
HEAD:DECISIONS.md:1015:  - **State:** the repo holds no specification of test 2a or 2b and no record of either being run. Nothing is downloaded, installed or run by this entry.
HEAD:DECISIONS.md:1034:- **No limit is lifted by this entry.** The 2026-10-28 ruling, D-071 and the `23:50:09Z` hard limits all stand. Only Amear's words lift them. His words in item 2 set the conditions for lifting the 2026-10-28 ruling (2a and 2b both pass);
HEAD:DECISIONS.md:1043:3. What is "the VM's Cowork agent", where does it run, and where is its skills directory? (The filer cannot write test 2b's steps without it.)
HEAD:DECISIONS.md:1044:4. For test 2a: is `docs/reports/2026-11-01-three-strategy-results.md:73` (1190 trades, $197327.60 net, `NQCONTROW SEP25`) the reference run, and does "reproduces" mean an exact match on trades and net, or a tolerance?
HEAD:DECISIONS.md:1046:6. Does test 2a (as the filer reads it, an NT8 run on the VM driven through the bridge) need your separate lift of the `23:50:09Z` limit "no NT8 runs or imports on the VM", and of D-071 if the bridge needs a connection, or does item 2 co
HEAD:DECISIONS.md:1048:8. Who judges that 2a and 2b have passed, and is the lift recorded by your own ledger row?
HEAD:DECISIONS.md:1063:Rulings 1. Bridge install (NEEDS AMEAR 2): the VM agent installs cli-nt-bridge via terminal, after a VMware snapshot. 2. Fees: apply MFFU's published round trip — NQ $4.68, MNQ $1.90 — by new DECISIONS entry amending the cost model. Cove
HEAD:DECISIONS.md:1069:Master's readings, flagged as readings: (i) "Handoff NEEDS AMEAR 1, 3–10, 15–17, 19" refers to the numbering in `docs/reports/2026-11-06-voice-handoff-evening.md` §4 (1–10 = D-2026-11-06-A's ten; 11–19 carried) — so items 2 (who installs
HEAD:DECISIONS.md:1087:| 4 — test 2a reference | "test 2a reference = 1,190 trades / $197,327.60 on NQCONTROW SEP25, exact match" | Exact match on 1,190 trades / $197,327.60, `NQCONTROW SEP25`; reference record `docs/reports/2026-11-01-three-strategy-results.m
HEAD:DECISIONS.md:1089:| 6 — lift scope | "my "lift completely once confirmed" ruling covers what tests 2a/2b need (bridge install + its import), D-071 untouched" | His lift covers the bridge install and its import; D-071 untouched. His words also say "what te
HEAD:DECISIONS.md:1104:- Test 2a vs the fee amendment. The 2a reference figures were produced with commission $2.96 per trade (`docs/reports/2026-11-01-csv-analyses.md:51`, `commission/trade={'2.96': 1190}`). An exact-match reproduction (item 4) therefore need
HEAD:DECISIONS.md:1231:7. Bridge items: (4) playbackrun/reconnect/flatten/strategies/ghostorders/AutoReconnect stay forbidden until live-trading design says otherwise. (5) NT8 Guard out. (7) 2a uses the committed base PraxisNoiseAreaBreakout.cs; the VM's insta
HEAD:DECISIONS.md:1263:- **Ruling 5 — 2a run.** *Rules:* "2a run: YES, covered by my lift. A test that needs a run includes the run." *Unlocks:* answers the run half of D-2026-11-06-A NEEDS AMEAR 6 (DECISIONS.md:1046): his lift covers the test 2a NT8 run on th
HEAD:DECISIONS.md:1264:- **Ruling 6 — Strategy Analyzer tab. Addendum-level statement to D-2026-11-06-A item 2 (DECISIONS.md:1003).** *Rules:* "Strategy Analyzer tab: a hand-set tab may be used for 2a and counts as "bridge reproduces the baseline". It does NOT
HEAD:DECISIONS.md:1268:  - (7) → row 7: "(7) 2a uses the committed base PraxisNoiseAreaBreakout.cs; the VM's installed copy must hash-match HEAD, or STOP." This is a hard STOP condition in his words ("or STOP"). His words do not say whether the STOP ends test 
HEAD:DECISIONS.md:1270:  - (12) → row 12: "(12) you propose how each arm runs through the bridge after 2a passes." The master proposes, after 2a passes.
HEAD:DECISIONS.md:1448:Before test 2a passes, the code unit can reach WRITTEN only. T6(i) runs on the Mac. Everything else runs on the VM after 2a. No code is changed by this entry; the code unit is dispatched only after this entry is committed.
HEAD:DECISIONS.md:1471:- **Hash STOP.** His words (ruling 7(7), :1231): "(7) 2a uses the committed base PraxisNoiseAreaBreakout.cs; the VM's installed copy must hash-match HEAD, or STOP." Scope reading, INFERRED, the master's, not his word, changeable by him: 
HEAD:DECISIONS.md:1472:- **§9.** The master's proposal under ruling 7(12) ("(12) you propose how each arm runs through the bridge after 2a passes."). It awaits his word after 2a passes and is not in force.
HEAD:DECISIONS.md:2094:- **Block 2 (tests 2a and 2b, in the handoff).** Step 1's self-report is test 2b part 1 (handoff §3, :91); step 2's skill load is test 2b part 2 (§4, :125); step 4.3's hand reads are Amear's (:241). Moving the screen reads to Amear does 
HEAD:DECISIONS.md:2154:2. The V7 strategy list at return-handoff :110, copied by script: "the Noise-Area baseline (test 2a: 1,190 trades / $197,327.60 on NQCONTROW SEP25) and its walk-forward; the three 2026-11-01 strategies; the R6 announcement variants (no N
HEAD:docs/reports/2026-11-06-cli-nt-bridge-code-read.md:226:2. Test 2a needs the bridge installed. Is installing it (copying C# into `bin\Custom` and compiling in NT8) an "import on the VM" under the ban that 2a is meant to lift? If so, which comes first, and 
HEAD:docs/reports/2026-11-06-cli-nt-bridge-code-read.md:234:10. For test 2a ("drives the baseline from the terminal"): does it count if you set a Strategy Analyzer tab by hand once and the terminal then presses Run? Or must every setting come from the terminal
HEAD:docs/reports/2026-11-06-rulings-filing-manager.md:12:- [2026-11-06T20:08:28Z] **WHO: amear** | WHAT: **"RULINGS + LOOP — 2026-11-06 evening voice (WHO: amear). File first, then run."** — pasted into the Code session mid-turn; recorded VERBATIM here first 
HEAD:docs/reports/2026-11-06-rulings-filing-manager.md:41:5. Adversary 1 → REFUTED. Applied fixes in place inside this unit's own uncommitted append (lines 1–1050 still byte-equal to HEAD): the settlement-source sentence (the 20:12:00Z row gives content for it
HEAD:docs/reports/2026-11-06-rulings-filing-manager.md:258:8. **MINOR: the item 6 settlement narrows his words.** He said "covers what tests 2a/2b need (bridge install + its import)". The settlement keeps only "install and import" and drops the NT8 run on the 
HEAD:docs/reports/2026-11-06-rulings-filing-manager.md:304:5. **MINOR** — item 8 (line 1091) says "auditor" means praxis-auditor and "my ruling" means D-2026-11-06-A item 2, without marking these as the filer's identifications. Item 6's first sentence is narro
HEAD:docs/reports/2026-11-06-rulings-filing-manager.md:312:- **Test 2a × cost amendment.** The 2a reference (1,190 / $197,327.60) ran at $2.96 per trade (`docs/reports/2026-11-01-csv-analyses.md:51`). An exact match needs that commission, not $4.68; at $4.68 t
HEAD:docs/reports/2026-11-06-status-handoff-evening-manager.md:277:   - Amear's own text at `20:08:28Z` is broader: "my "lift completely once confirmed" ruling covers what tests 2a/2b need (bridge install + its import)".

$ grep -n -i -E '2a and 2b|test 2a|test 2b' DECISION_LOG.md | cut -c1-260 | tail -15
486:- [2026-11-06T22:11:54Z] WHO: praxis-master | WHO COMMITTED: praxis-master through the gate (second time) | WHAT: **SECOND GATED SELF-COMMIT LANDED: `234e4bc`, 3 files / 4178+, PUSHED (`69ec506..234e4bc`); loop step c (bridge read) complete; DISPATCH DECIS
499:- [2026-11-06T20:34:29Z] WHO: praxis-master | WHAT: **UNIT `2026-11-06-rulings-filing` RETURNED (self-grade PASS, ungraded; 60 tool uses, ~169k tokens; two adversaries: REFUTED 4 MAJOR → fixed → NOT REFUTED) — R-1104-2 SETTLEMENTS RECORDED HERE; item 19 LO
501:- [2026-11-06T20:08:28Z] **WHO: amear** | WHAT: **"RULINGS + LOOP — 2026-11-06 evening voice (WHO: amear). File first, then run."** — pasted into the Code session mid-turn; recorded VERBATIM here first (master's `date -u` read at 20:08:28Z in the same turn
510:- [2026-11-06T16:12:02Z] WHO: praxis-master | WHAT: **CORRECTION 1 RETURNED (self-grade PASS; 37 tool uses, ~118k tokens) → `commit-idx-vnf` REBUILT; REDUCED RE-AUDIT DISPATCH.** OBSERVED this turn: report now 636 lines (`## Correction 1` at 182, `**Result
512:- [2026-11-06T15:54:21Z] WHO: praxis-master | WHAT: **UNIT `2026-11-06-voice-notes-filing` RETURNED (manager self-grade PASS; 69 tool uses, ~163k tokens, four adversarial passes 7/4/8/1 findings, all fixed; last fix script-checked only) → temp index `commi
517:- [2026-11-06T15:15:30Z] **WHO: amear** | WHAT: **"NOTES FROM AMEAR — 2026-11-06 voice (file as WHO: amear)"** — pasted into the Code session mid-turn; recorded VERBATIM here first (the master's `date -u` read at 15:15:30Z precedes the paste in the same tu
759:- [2026-11-09T13:50:00Z] WHO: praxis-master | WHAT: **D11 SWEEP — CLOSURES. Inventory: `docs/reports/2026-11-09-d11-sweep-manager.md` (2110 lines, sha `903a6a90…0ea0`; manager corr a8663fcc3a1d85852, 49 tool uses), Table 1 rows G01–G41 (no G16; moved to X1
768:- [2026-11-09T18:34:00Z] WHO: praxis-master | WHAT: **VM handoff amendment 2 manager returned (corr a4f12311d43f0709d, 47 tool uses, ~19 min), self-graded PASS at level WRITTEN; master read the report (549 lines: process log, line index, S6, Open list, sel

$ git grep -n 'NEEDS AMEAR 6' HEAD -- DECISIONS.md | cut -c1-260
HEAD:DECISIONS.md:360:- **R-7zq-3 — third file (answers NEEDS AMEAR 6 above), DECISION_LOG `2026-10-31T11:45:29Z` (WHO: amear):** *"Keep #1 (as built)"* — `PraxisLastHalfHourMomentum` (Baltussen, Da, Lammers & Martens 2021) stands; TORB and ORB remain written 
HEAD:DECISIONS.md:1010:- **Item 2 — in-VM automation.** The "Oct 28 ruling" is ruling (1) of `docs/reports/2026-10-28-voice-session-notes.md:7` (untracked file), "The in-VM automation approach is dropped. No more Cowork or in-VM Claude Code executor work.", ta
HEAD:DECISIONS.md:1014:  - **Direction he set:** the walk-forward runs in NT8 through the bridge, not in a Mac-side Python copy. The open question it bears on is the step-c harness question at DECISION_LOG `2026-11-06T00:54:04Z`: "arm (a) can only run in NT8 o
HEAD:DECISIONS.md:1034:- **No limit is lifted by this entry.** The 2026-10-28 ruling, D-071 and the `23:50:09Z` hard limits all stand. Only Amear's words lift them. His words in item 2 set the conditions for lifting the 2026-10-28 ruling (2a and 2b both pass);
HEAD:DECISIONS.md:1089:| 6 — lift scope | "my "lift completely once confirmed" ruling covers what tests 2a/2b need (bridge install + its import), D-071 untouched" | His lift covers the bridge install and its import; D-071 untouched. His words also say "what te
HEAD:DECISIONS.md:1263:- **Ruling 5 — 2a run.** *Rules:* "2a run: YES, covered by my lift. A test that needs a run includes the run." *Unlocks:* answers the run half of D-2026-11-06-A NEEDS AMEAR 6 (DECISIONS.md:1046): his lift covers the test 2a NT8 run on th

```

### Batch 7 (D-2026-11-10-C, D-2026-11-11-B, lift greps)

```
$ git show HEAD:DECISIONS.md | sed -n '2076,2080p' | cut -c1-600
## 2026-11-10 — D-2026-11-10-C: VM agent = Hermes over SSH (settlement 3 changed; master under D1)

**Status:** Decided by master under D-2026-11-08-D D1; changeable by Amear.
**Authority:** Amear's proposal, DECISION_LOG.md:813 (row 2026-11-10T20:42:00Z, WHO: amear; at filing that row sits in the working copy, after the 810 lines of DECISION_LOG.md at HEAD `55979ee`). His words, copied by script from that line:


$ git show HEAD:DECISIONS.md | sed -n '2176,2204p' | cut -c1-330
## 2026-11-11 — D-2026-11-11-B: VM handoff §1 limit 9 lifted by Amear for one install; Python 3.12.10 and git 2.56.0 (ARM64) installed in the VM. Record only. Filed WHO: amear, REPORTED BY the Claude.ai channel.

**Status:** Record only. WHO: amear, REPORTED BY the Claude.ai channel.
**Authority:** DECISION_LOG.md:828 (row 2026-11-11T18:19:40Z, WHO: amear; its ALSO part, on the limit 9 lift) and DECISION_LOG.md:829 (row 2026-11-11T18:20:00Z, praxis-master). Source: `vm/replies/20261111T172933Z-python-git-install.md` (called the install reply below; untracked at filing); its line numbers are cited as `install

**The limit.** VM handoff §1 limit 9, copied by script from `vm/2026-11-06-vm-handoff.md`:37: "**Do not install anything else** — not Python, not git, not a package manager. If a tool is missing, STOP and report it."

**Amear's words (install reply :7–8) and the channel's note (:9).** Voice, 2026-11-11 ~16:5xZ, on whether to snapshot first: "Okay, you know what? Let's forget about the snapshot. Let's have it execute those things first." Then: "Hermes is going to give me a uh, a physical button to accept or deny, so don't worry about that." (i

**Who did it.** Install reply :2 names the writer as "Claude (Claude.ai Praxis channel, Cowork session)", "driving the VM over SSH from the Mac (host praxis-vm), commands run from the Mac via osascript". By that line the install was driven by the Claude.ai channel, not by Hermes; D-2026-11-10-C (DECISIONS.md:2076) names Hermes a

**What was installed, and where (install reply :18–19).** Python: `Python 3.12.10` at `C:\Program Files\Python312-arm64\python.exe` (`py -0p`: `-V:3.12-arm64 *`), installer exit `PYTHON_EXIT=0`. Git: `git version 2.56.0.windows.4` at `C:\Program Files\Git\cmd\git.exe`, installer exit `GIT_EXIT=0`. NinjaTrader still pid 9600, sta

**What was kept (install reply :24–25).** "NinjaTrader not started, stopped or touched (same pid and start time before and after). No connection change (D-071). No orders. No pip run, no clone, no bridge files. No Windows restart. Nothing else installed. Only new files under `vm/replies/`."

**Scope.** The install reply's header (install reply :1) says limit 9 was "lifted by Amear for this install". Amear's quoted words at install reply :7–8 set no scope of their own. This entry reads the lift as covering this one install only and does not widen it; limit 9 binds every later step as written.

**Timing (S4).** The install reply is stamped `UTC: 20261111T172933Z` (install reply :3), that is 2026-11-11T17:29:33Z, before DECISION_LOG.md:828 (2026-11-11T18:19:40Z) and before this entry. This entry records the install after the fact. So for this install the order S4 and S5 ask for (a DECISIONS.md entry and a ledger append 

**Open risk.** Copied by script from install reply :28: "Whether the bridge's dependencies (notably `pyarrow`, also `numpy`) have win_arm64 wheels at versions meeting the bridge's floors is not checked." "If step 3.5 fails on a build-from-source, the fallback is an x64 Python (runs under emulation) — that is Amear's call, not ta

**How sure.** Every install fact above is REPORTED BY the Claude.ai channel in the install reply. Nobody in this repo re-ran the commands or looked at the VM.

**Open for Amear.** Whether the Claude.ai channel may drive the VM over SSH again is an agent-permission item, D2(d), his. The x64-Python fallback (install reply :28) is his call.

**What this entry does not do.** No pip, no clone, no venv, no bridge files. It does not edit the VM handoff. It changes no step gate in handoff step 3.5 (`vm/2026-11-06-vm-handoff.md`:188 onward), including its STOP conditions on a failed install (:200, "Consequence") and on any unnamed download (:201, "Detection, after the fac

[closing-line text elided by worker 5 so it occurs once]


$ git show HEAD:DECISIONS.md | sed -n '1089p' | cut -c1-700
| 6 — lift scope | "my "lift completely once confirmed" ruling covers what tests 2a/2b need (bridge install + its import), D-071 untouched" | His lift covers the bridge install and its import; D-071 untouched. His words also say "what tests 2a/2b need"; whether that reaches the 2a NT8 run on the VM (D-2026-11-06-A NEEDS AMEAR 6) stays in his words and is neither narrowed nor extended here. | pending: VM handoff (loop step c) |

$ grep -rn -i -E 'claude code.*(vm|inside the vm)|lifted' docs/reports/2026-11-13*.md | cut -c1-260 | head -20
docs/reports/2026-11-13-hermes-handoff-strategy-search.md:14:- On Claude Code being on the VM: "I just manually put it in there." Then: "I didn't lift it. ... that still exists." And: "Or if I determine that I will bypass the rules. Those rules are for you, no
docs/reports/2026-11-13-hermes-handoff-strategy-search.md:45:   5. **The 2026-10-28 rule still stands for agents** (DECISIONS.md :1010). Amear put Claude Code on the VM by hand, and that was his own act, not a lift of the rule. His words: "Those rules are for 
docs/reports/2026-11-13-hermes-handoff-strategy-search.md:64:4. **Backtest it through the VM bridge** queue, dispatched by Hermes over SSH as on 2026-11-13. No Claude Code runs inside the VM. Settings match the 2026-11-01 runs: NQCONTROW, 1-minute bars, 2021-0
docs/reports/2026-11-13-hermes-handoff-strategy-search.md:101:- No agent runs Claude Code inside the VM.
docs/reports/2026-11-13-o4-parity-worker2.md:18:6. Check 5 (D2, values, F3/F4): no D2 (a), (b), (d) mention; D2 (c) only referenced; no value set; F3/F4 explicitly not lifted and not depended on. Pass.
docs/reports/2026-11-13-o4-parity-worker2.md:305:Checks with no defect: check 1 (30 of 30 quotes byte-present), check 2 (both O4 questions answered without ambiguity), check 5 (no D2 item decided, no value set, F3/F4 not lifted or depended on), check 6 (format
docs/reports/2026-11-13-o4-parity-worker3.md:276:Check 5 and 6 pass: no D2 item decided, no breaker value set, no code or spec body changed, F3 and F4 neither lifted nor relied on; 28 lines; all sections present; the closing line is the file's last line, exact
docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md:5:Source: the VM Claude Code session's own report, pasted to this channel by Amear at 14:37 ET (REPORTED BY Amear; the channel has not read the VM repo). The VM agent is the session working i
docs/reports/2026-11-13-strategy-review-index-manager.md:129:The master's finding is CONFIRMED by this manager's own search (evidence blocks E4.1 to E4.8): the only record in this repo of what the VM-side agent did on 2026-11-12 and 2026-11-13 is the two Claud
docs/reports/2026-11-13-strategy-review-index-manager.md:145:- Any DECISIONS.md entry naming the `vm-bridge` repo or adopting a VM Claude Code session as the VM agent: the only case-insensitive "VM Claude Code" hit is DECISIONS.md:1010 (the ruling quoted next)
docs/reports/2026-11-13-strategy-review-index-manager.md:186:- VM / bridge: the 2026-11-13 VM agent is described as "the VM Claude Code session" in `C:\praxis\vm-bridge`. The last VM-agent decision on record names Hermes over SSH (D-2026-11-10-C), and DECISION
docs/reports/2026-11-13-strategy-review-index-manager.md:349:5:Source: the VM Claude Code session's own report, pasted to this channel by Amear at 14:37 ET (REPORTED BY Amear; the channel has not read the VM repo). The VM agent is the session working in `C:\pr
docs/reports/2026-11-13-strategy-review-index-manager.md:438:2176:## 2026-11-11 — D-2026-11-11-B: VM handoff §1 limit 9 lifted by Amear for one install; Python 3.12.10 and git 2.56.0 (ARM64) installed in the VM. Record only. Filed WHO: amear, REPORTED BY the C
docs/reports/2026-11-13-strategy-review-index-manager.md:439:$ grep -n -o -F 'No more Cowork or in-VM Claude Code executor work.' DECISIONS.md; grep -n -o -F 'lifted COMPLETELY once two tests pass' DECISIONS.md
docs/reports/2026-11-13-strategy-review-index-manager.md:441:1003:lifted COMPLETELY once two tests pass
docs/reports/2026-11-13-strategy-review-index-manager.md:442:1010:lifted COMPLETELY once two tests pass
docs/reports/2026-11-13-strategy-review-index-manager.md:443:1091:lifted COMPLETELY once two tests pass
docs/reports/2026-11-13-strategy-review-index-manager.md:444:1264:lifted COMPLETELY once two tests pass
docs/reports/2026-11-13-strategy-review-index-worker5.md:87:1. `docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md` (committed in 9ff8a48). VM bridge queue T1-T3 (bridge-driven Strategy Analyzer runs). Source `:5`: "the VM Claude Code session
docs/reports/2026-11-13-strategy-review-index-worker6.md:56:| 44 | 145 | DECISIONS.md:1010 only "VM Claude Code" hit; vm-bridge 0 hits; D-2026-11-10-C at :2076 | (Ev3) | MATCH | one hit at :1010; vm-bridge count 0; :2076 heading |

$ grep -n -o -E '.{0,200}(2026-10-28 rule|Those rules are for you).{0,200}' DECISION_LOG.md | cut -c1-260 | tail -6
944:rmes agent to pause all builds until there's 3 contenders for the strategy." Voice quotes, transcribed, at handoff :13-:15. They cover the 09:30 vs 08:30 open, and Claude Code put on the VM by hand ("Those rules are for you, not for me"). The rulings as th
944:hree contenders exist; (3) the search loop runs in Claude Code; (4) the trade-count gap is explained by the 09:30 vs 08:30 open, with its bearing on R1's re-run clause recorded; (5) the 2026-10-28 rule (DECISIONS.md :1010) still binds agents. The contender

```

### Batch 8 (D-2026-11-10-C scan, handoff :13-:15 and :45)

```
$ git show HEAD:DECISIONS.md | awk 'NR>=2076 && NR<=2175' | grep -n -i -E 'oct 28|2026-10-28|2b|lift|claude code|what it decides' | awk -F: '{ $1 = $1 + 2075; print }' OFS=: | cut -c1-300
2087:**What it decides.** The VM agent for every step of `vm/2026-11-06-vm-handoff.md` is Hermes, driving the VM over SSH from the Mac (host alias `praxis-vm`) under its skill `praxis-vm-over-ssh`. The terms are in the CODE- reply `vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md`, made part of t
2094:- **Block 2 (tests 2a and 2b, in the handoff).** Step 1's self-report is test 2b part 1 (handoff §3, :91); step 2's skill load is test 2b part 2 (§4, :125); step 4.3's hand reads are Amear's (:241). Moving the screen reads to Amear does not change what counts: a hand-set tab counts as "bridge r

$ sed -n '13,15p;45p' docs/reports/2026-11-13-hermes-handoff-strategy-search.md | cut -c1-600
- On why the 2026-11-13 VM run had 1,173 trades and the 2026-11-01 hand run had 1,190: "yesterday I basically changed the parameters so that it only trades from 9:30 a.m. onwards, right at the New York Open. And the back tests from November the first had the open via 8:30 a.m."
- On Claude Code being on the VM: "I just manually put it in there." Then: "I didn't lift it. ... that still exists." And: "Or if I determine that I will bypass the rules. Those rules are for you, not for me."
- On the other session: "The other session did stop. It's just, oh, I just didn't actually officially close it."
   5. **The 2026-10-28 rule still stands for agents** (DECISIONS.md :1010). Amear put Claude Code on the VM by hand, and that was his own act, not a lift of the rule. His words: "Those rules are for you, not for me." No agent runs Claude Code inside the VM. The VM agent stays Hermes over SSH (D-2026-11-10-C, :2076).

$ git show HEAD:docs/reports/2026-11-01-three-strategy-results.md | sed -n '41p;179p' | cut -c1-300
- Mapping from each CSV's `Strategy` column, all rows, [K03] `[1] Strategy` (OBSERVED): 07-10 = `PraxisNoiseAreaBreakout` (1190 rows), 07-57 = `PraxisNoiseAreaBreakout_OppBand` (810), 07-59 = `PraxisNoiseAreaBreakout_Flat1559` (1190), 08-00 = `PraxisLastHalfHourMomentum` (1304). Instrument `NQCONTRO
| last 5 | 806 | Short | 2026-07-01 11:01 -> 16:00 | 30192.50/30081.75 | S -> Exit on session close | $2212.04 | 300 |

```

### Batch 9 (scope line, arithmetic, elision)

```
$ git show HEAD:DECISIONS.md | grep -n -E '^\*\*Scope\.\*\* The install reply' | cut -c1-120
2191:**Scope.** The install reply's header (install reply :1) says limit 9 was "lifted by Amear for this install". Amear
$ python3 -c "print(round(1173*2.96,2), 1190-1173, round(197327.60-176392.92,2))"
3472.08 17 20934.68
$ grep -c -F "$L" docs/reports/2026-11-14-evening-rulings-worker5.md   (before elision)
4
$ grep -c -F "$L" docs/reports/2026-11-14-evening-rulings-worker5.md   (after elision)
0
```

Elision note: the brief requires the closing line to occur exactly once. Four pasted outputs contained it: vm-queue :7, STATUS.md :322 and :324, and the D-2026-11-11-B block. The worker replaced that text in the pasted outputs with a bracketed marker. Nothing else in the pasted output was changed.

## Q4 - trade-count gap (1,190 vs 1,173)

1. **The three 2026-11-01 Noise-Area runs (OBSERVED).** `docs/reports/2026-11-01-three-strategy-results.md:41` maps the CSVs: 07-10 = `PraxisNoiseAreaBreakout` (1190), 07-57 = `PraxisNoiseAreaBreakout_OppBand` (810), 07-59 = `PraxisNoiseAreaBreakout_Flat1559` (1190), 08-00 = `PraxisLastHalfHourMomentum` (1304). The report's own "three strategy" runs are Run 1 OppBand (:79), Run 2 Flat1559 (:185) and Run 3 LastHalfHourMomentum (:303). Run 3 is not Noise-Area. The handoff's "three 2026-11-01 Noise-Area runs" therefore has to mean baseline + OppBand + Flat1559, the same set as strategy-review-index-manager :5. That reading is correct, but it is not the report's own "three strategies" set (INFERRED).
2. **The 1,173 runs (REPORTED BY Amear, relayed by the channel).** They are in `docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md` (committed in 9ff8a48). Setup is at :11: tab "PRAXIS baseline NQCONTROW 0930", `PraxisNoiseAreaBreakout`, "CME US Index Futures RTH 0930 ET", $2.96. T1 BandOrVWAP is 1,173 / $176,392.92 (:15), T2 OppBand is 1,112 / $188,618.48 (:16), and T3 = T1 (:17). T1 is graded "Exact match" against the "T1 reference (Amear's hand run)", not against the 2026-11-01 1,190 run. That 1,173 hand run has no primary record in the repo. Only its figures appear, at session-close :51 (strategy-review-index-worker5 :88, :321). The hand-run commission $3,472.08 equals 1,173 x $2.96 (Batch 9, OBSERVED arithmetic).
3. **Not recorded as R1's re-run (OBSERVED absence).** The re-run clause appears only at DECISIONS.md :1555. The only records that connect it to the 1,173 runs are the handoff (:44) and DECISION_LOG :944, which says "its bearing on R1's re-run clause recorded". Neither calls T1/T2 the R1 re-run. On coverage (INFERRED): at 09:30 the baseline (T1) and OppBand (T2) exist. Flat1559 has no 09:30 run, because its tab is "Later, not today" (vm-queue :42). The re-run would cover 2 of 3 arms at most.
4. **T7 template readback: none on record (OBSERVED absence).** T7 at DECISIONS.md :1419 reads back commission, backtest type, fill resolution and slippage, not hours. R1 (:1552-:1553) adds the template-hours readback. No report records a readback of the live template's hours. R1's condition ("If the live template starts 08:30 ET") is therefore not discharged by a readback. It rests on Amear's voice quote (handoff :13). It is supported by the rescued XML "830"-"1600", TimeZone Eastern (o78-worker4 :208-:219 at HEAD, REPORTED BY that worker, file mtime Aug 29), and by the oracle fit of 1190/1190 at 08:31 against 864/1190 at 09:31 (`docs/reports/2026-11-07-return-handoff-claude-ai-2.md:61`). vm-queue :11's "RTH 0930 ET" is a label in a relayed report, not a readback.
5. **Noise-Area status (OBSERVED).** D7 keeps the baseline "for the record" (strategy-review-index-manager :8, :70-:71). The manager notes that DECISIONS.md is silent on OppBand and Flat1559 after D7. vm-queue :36 says "kept for the record only". STATUS.md has no current Noise-Area status line. HANDOFF.md :9 carries D-2026-11-13-C. The handoff's "does not change Noise-Area's status" is consistent with this.

## Q5 - the 2026-10-28 rule

1. **Tests 2a and 2b: no record of a pass (OBSERVED absence).** DECISIONS.md :1015: "the repo holds no specification of test 2a or 2b and no record of either being run." No later hit records a pass. D-2026-11-10-C :2094 maps 2b onto VM handoff steps 1 and 2, and no completion of those steps is on record. 2a is defined as an "Exact match on 1,190 trades / $197,327.60, `NQCONTROW SEP25`" (:1087). The 2026-11-13 T1 matched 1,173 / $176,392.92 (vm-queue :15). As defined, 2a is not met (INFERRED). Ruling 6 (:1264) lets a hand-set tab count, but the reference figures still have to match.
2. **NEEDS AMEAR 6: answered in two parts (OBSERVED).** The question is at :1046, and :1010 also tags the "COMPLETELY" scope with it. :1089 says the lift "covers the bridge install and its import; D-071 untouched" and leaves the run half open. :1263 Ruling 5 answers the run half: "2a run: YES, covered by my lift. A test that needs a run includes the run." Both rulings are scoped to "what tests 2a/2b need". Neither lifts the rule itself.
3. **D-2026-11-10-C (:2076).** :2087: "The VM agent for every step of `vm/2026-11-06-vm-handoff.md` is Hermes, driving the VM over SSH from the Mac (host alias `praxis-vm`) under its skill `praxis-vm-over-ssh`." It names the agent and does not lift the 2026-10-28 rule.
4. **D-2026-11-11-B (:2176-:2204).** Heading :2176: "VM handoff §1 limit 9 lifted by Amear for one install; Python 3.12.10 and git 2.56.0 (ARM64) installed in the VM. Record only." :2191: "This entry reads the lift as covering this one install only and does not widen it." This is a lift of limit 9, not of the 2026-10-28 rule.
5. **Lift / Claude Code on the VM.** No record says the 2026-10-28 rule was lifted. Amear's words (handoff :14, REPORTED by the channel transcript): "I just manually put it in there." / "I didn't lift it." DECISION_LOG :944 files these words and "(5) the 2026-10-28 rule ... still binds agents".

## Findings - where the handoff does not match the record

- **F1 (Q4 :44, wording).** "The 2026-11-13 VM runs trade from 09:30 ET. The 2026-11-01 hand runs used an 08:30 open." The 2026-11-01 runs did not trade from 08:30. Their entries are at 10:01 and 11:01 (11-01 report :174-:181, OBSERVED). The 08:30 is the session anchor that the bands/VWAP are measured from (oracle fit, 2026-11-07 handoff :61). The correct contrast is session start 08:30 vs 09:30, not trading start (INFERRED).
- **F2 (Q4 :44, "explained").** Amear's explanation is asserted, not shown. No report compares the two trade lists to account for the 17-trade / $20,934.68 gap (Batch 9). The 1,173 reference hand run has no primary record. No T7 hours readback exists. "Explained" is REPORTED BY Amear. It is not OBSERVED.
- **F3 (Q4, R1 conflict).** If R1's 08:30 condition holds, the 2a reference (1,190 / $197,327.60, DECISIONS.md :1087) is itself one of the "suspect" baselines. The handoff records a bearing on R1. It does not mention that the bearing reaches the 2a reference too (INFERRED).
- **F4 (Q5 :64 and :45 vs vm-queue :5).** The handoff says "dispatched by Hermes over SSH as on 2026-11-13" (:64) and "No agent runs Claude Code inside the VM" (:45, :101). The record of the 2026-11-13 runs says the source is "the VM Claude Code session's own report" and "It is not praxis-master" (vm-queue :5). No record says that Hermes dispatched the 2026-11-13 runs (strategy-review-index-manager :186 notes the same gap). On the record, an agent did run Claude Code inside the VM on 2026-11-13. Amear calls that his own act (:14). Whether that is "in-VM Claude Code executor work" under the standing rule is his call. It is not settled here.
- **F5 (internal tension in vm-queue, not the handoff).** :5 names a "VM Claude Code session". :29 says "`run-queue.ps1` was not used: it needs the `claude` command, which is not installed on the VM". This may be a desktop session without the CLI on PATH (INFERRED, UNVERIFIED).

## Files staged
None. Only this report was written, and it is untracked.

## Result: PASS
Both questions were answered from the record with file:line citations. Five mismatches are listed above.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
