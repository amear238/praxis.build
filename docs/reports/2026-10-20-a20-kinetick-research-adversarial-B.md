# a20 Kinetick research — adversarial review B

- **Task:** break docs/reports/2026-10-20-a20-kinetick-research-worker1.md, conclusions (a)–(d)
- **Mode:** ADVERSARIAL (read-only; this file is the only write)
- **Criterion:** specs/SPEC_RUBRIC.md S1/S2 (:107-108), S8 (:114), R3 (:159-166)
- **Date:** 2026-10-20
- **Tools:** `/usr/bin/grep` used throughout (BSD grep, `\|` alternation proven live by the positive arms below). The rescue Config.xml was not opened, so no token lines were printed. The rescue NinjaTrader.sqlite was read from a **copy** in the session scratchpad, with `sqlite3 -readonly`.

## Findings

### F1. Option B conflicts with D-071. The artifact applies D-071 only to C. MAJOR (under-claim, S8-adjacent)

- **Claim:** row C, artifact :106: "It also … breaks … Amear's D-071 condition 'no other connection'". Row B (:105) says nothing about D-071. The PRAXIS view (:116) says: "If Amear ever wants free daily bars from it, B is the reversible way to try."
- **Defect:** D-071 forbids *any* other connection, however brief. Amear's 15:55:42Z ruling pins the one accepted connection as the Simulated Data Feed. Connecting Kinetick by hand (B) is "another connection" just as much as C is. Only A complies outright. D is not a connection, but it breaks the master's "Connections as before, and nothing more" principle (item 13), which the artifact cites for C and leaves out for D. On S8: :116 is labelled "reasoning, not a decision" and ends "Amear decides". That alone doesn't cross S8. But it offers Amear B as the safe path to try without telling him that B breaks a condition he set himself. That is an under-informed steer.
- **Evidence:**
```
$ sed -n 60,72p docs/reports/2026-10-19-windows-vm-state-update-2-from-migration.md   (row 13)
| 13 | Connections as before, nothing more | **One change, accepted.** After sign-in NT8 connected by itself to **"Simulation"**, … Amear accepted it on condition: no orders, no other connection (D-071). …
$ sed -n 424p DECISION_LOG.md
- [2026-10-20T15:55:42Z] WHO: amear | WHAT: **Amear's rulings on the a20 results.** (1) **K5/K8: ACCEPT AS FOUND.** "Simulated Data Feed" connected (green) is recorded as what D-071's "Simulation" meant. Nothing touched. … (3) **Kinetick EOD (K1): undecided.** …
```
- **Smallest fix:** add to row B: "Conflicts with D-071 'no other connection' (update 2 :67, as clarified by DECISION_LOG :424). Needs Amear to lift or amend D-071 first." Add the item-13 principle to row D. In :116, replace "B is the reversible way to try" with "B would first need D-071 amended. That is Amear's call."

### F2. "Historical bars came from the NinjaTrader Historical Data Server (VERIFIED)" covers 1 of 51 NQ daily files. MAJOR (over-claim, S2, plus a missed source)

- **Claim:** artifact :17: "Historical bars came from the **NinjaTrader Historical Data Server** (VERIFIED in the logs)." Conclusion (c).
- **Defect:** the logs only cover 2026-08-15 to 08-29. The artifact never looked inside the rescue `db/day` store. It mentions the folder once, at :105. Daily bars are exactly what Kinetick EOD supplies. 49 of the 51 NQ daily `.ncd` files were written in one batch on 2026-07-14 at 15:09:06, a month before the first surviving log. One more is from 07-20. Only `NQ 12-25/2025.Last.ncd` (08-16 08:16) falls inside the log window, and that day's log does show HDS in use at 08:07. **Nothing in the rescue copy names the provider that wrote the 07-14 batch:** zero "kinetick" bytes anywhere under `db/`, and the sqlite has no provider column. The artifact already concedes in C2 that the source is unverified for *minute* data before 08-15. The headline line drops that hedge and labels the claim VERIFIED. This finding does **not** show that Kinetick wrote the data. It shows that the VERIFIED label reaches past its evidence.
- **Evidence:**
```
$ ls -d ".../NinjaTrader 8-full/db/day"/NQ\ * | wc -l
      41
$ ls -l -D %F_%T ".../db/day"/NQ\ */*.ncd | awk '{print $6}' | sort | uniq -c
  49 2026-07-14_15:09:06
   1 2026-07-20_11:26:23
   1 2026-08-16_08:16:53
$ /usr/bin/grep -a "^2026-08-16 08:\(0[5-9]\|1[0-9]\|2[0-9]\)" ".../log/log.20260816.00000.en.txt"
2026-08-16 08:07:33:743|3|2|Connection lost to the NinjaTrader Historical Data Server: hds-us-nt-020.ninjatrader.com
2026-08-16 08:07:43:773|1|2|Using HDS (hds-us-nt-012.ninjatrader.com/31655)
2026-08-16 08:07:44:040|1|2|Connection restored to the NinjaTrader Historical Data Server: hds-us-nt-012.ninjatrader.com
$ /usr/bin/grep -rlai kinetick ".../NinjaTrader 8-full/db"; echo exit=$?      (no file printed)
$ sqlite3 -readonly <copy>/nt.sqlite ".tables"   -> no provider table; MasterInstruments has no provider column; Logs rows = 0
$ /usr/bin/grep -c -a -i kinetick nt.sqlite NinjaTrader.sqlite.bak_praxis NinjaTrader.sqlite.bak_praxis2
0 / 0 / 0
```
  Both rescue copies of `db/day` are identical (`diff -rq` printed nothing).
- **Smallest fix:** scope :17 to "in the 2026-08-15 to 08-29 logs". Add: "49 of 51 NQ daily files in `db/day` date from 2026-07-14 15:09, before any surviving log. Their provider is UNVERIFIED."

### F3. The Block 2 row leaves out the 22 daily-bar series the backtest consumes. MINOR (under-claim)

- **Claim:** Q3 Block 2 row (:90): "None found — `DECISIONS.md:184` (default-provider **minute** history…)".
- **Defect:** Block 2's roll dates are computed from **daily** series (22 `_daily.csv` exports), the same data class Kinetick EOD serves. The artifact never mentions them. The present-tense conclusion holds: the files are already on the Mac, so nothing needs Kinetick connected today. But R3 needs the dependency to be graded by search, and the search never covered daily data. Any future re-pull of daily data has an untested provider path (see F2, and multi-provider at Config.xml:208).
- **Evidence:**
```
$ sed -n 105p docs/reports/2026-07-25-wx7-build-progress-for-scoping-agent.md
- **Raw data landed:** all 44 raw export files (22 daily + 22 one-minute contracts) were pulled from NT8's default data provider …
$ /usr/bin/grep -niI "daily" scripts/b2_stitch.py | head -2
11:#   ~/praxis-signals/b2-data/raw/  ->  NQ-<MM-YY>_1min.csv + NQ-<MM-YY>_daily.csv
13:# DAILY series (spec §3), applies additive Difference offsets at each seam, and
$ ls -l ~/praxis-signals/b2-data/raw | /usr/bin/grep -c daily
22
```
- **Smallest fix:** add the daily series to the Block 2 row, with the provider label "default provider (REPORTED, wx7:105); unverified for the 07-14 pull".

### F4. Missed source: the B2 acquisition spec planned a provider-served continuous `NQ` download. MINOR (missed source, latent dependency)

- **Claim:** (a) covers "planned design". The artifact cites the Block 2 *proposal* (:46, :49) but not the acquisition spec.
- **Defect:** `docs/specs/2026-07-15-b2-data-acquisition-spec.md` §5 step 2 tells the operator to download "instrument `NQ` (continuous)" inside NT8. Reference :186 says that needs provider support, "historically Kinetick / eSignal / IQFeed". In practice it was superseded: wx7 §7 E2 built the series in Python from per-contract exports instead. But the spec's own status line still reads "COMPLETE", with no superseded marker. This is the only *planned step* found that would need `NQ ##-##` provider support. Re-run as written, it could pull Kinetick in.
- **Evidence:**
```
$ /usr/bin/grep -rniI "continuous…" docs/specs docs/runbooks config
docs/specs/2026-07-15-b2-data-acquisition-spec.md:16:| Contract form | **Continuous / front-month rolled** (see §2 roll convention) |
docs/specs/2026-07-15-b2-data-acquisition-spec.md:115:2. **Download the minute history.** NT8 → *Tools → Historical Data* … → instrument `NQ` (continuous) → data type **Minute** … Default provider only (Q4 — no paid feed).
$ sed -n 5p same file
**Status:** Mac-side spec COMPLETE. Physical pull + validation is VM-GATED (see §5, §6).
$ wx7:184  - **E2 — build the series outside NT8, in Python.** The VM's NT8 install could **not natively construct** that roll convention …
$ /usr/bin/grep -rnI -- "##-##" docs/specs docs/runbooks config ~/praxis-signals
~/praxis-signals/vm-agent/reference/nt8-windows-reference.md:149 and :186 only (reference copies; no plan step)
```
- **Smallest fix:** add a row to Q3: "B2 acquisition spec §5.2 (NT8 continuous `NQ` download) needs provider support per reference :186. Superseded by wx7 E2, but the spec is not marked superseded. Latent only." Report the spec's stale status to the manager (not fixed here).

### F5. (b) is narrowly true, but the artifact under-states how far the record ties Kinetick to the defect's diagnosis. MINOR (under-claim)

- **Claim:** :92: session 53 :431 is "a question about continuous contracts in general, not a cause recorded for this defect".
- **Defect:** session 53 :431 sits inside §6b, "DEFECT FOUND in the existing Check A1 — the control is confounded". Check A1 is the diagnostic for the NQCONT unknown-instrument defect. Session 53 names the Kinetick *End Of Day* feed as the reason the check's control may have no minute data, and links reference :186 as "relevant, and not previously connected". Session 52 open question 6 (:264-266), part of the NQCONT fix research, asks whether `<ROOT> ##-##` works with imported data or is strictly provider-served. So the record ties Kinetick to the defect's **diagnostic control and its candidate fix**, though not to its **cause**. (b) as worded ("not tie … to the defect") still holds for causation.
- **Evidence:**
```
$ sed -n 407-432p docs/reports/2026-08-29-session53-nqcont-resolution-and-rth-corpus-read.md
### 6b. DEFECT FOUND in the existing Check A1 — the control is confounded
A1 says to run "any built-in NT8 instrument that already has data." **On this install there may be no such instrument at 1-minute granularity:**
… An **End Of Day** feed does not supply intraday minute bars. A1's decision rule reads control *failure* as **supporting** the bars-series theory …
Also relevant, and not previously connected (`reference:186`): … Requires **provider support** (historically Kinetick / eSignal / IQFeed).
$ sed -n 264,266p docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md
6. **Is `<ROOT> ##-##` ever usable with imported data**, or is it strictly provider-served? Reference §6 says provider support is required — **confirm or refute that.**
```
- **Smallest fix:** reword :92 and (b): "No recorded cause. The record does tie Kinetick EOD to the defect's diagnostic control (s53 §6b) and to an open fix-route question (s52 Q6)."

## Survived (with evidence)

1. **S2 null (kinetic variant): survives.** Re-run today, the only hits are the artifact quoting itself (`…worker1.md:89, 209, 211, 261`), which post-dates its own search. Positive arm, same shape: `"kinetick[^s]\|kinetick$"` gives **251** hits. Output from the wrapper and from `/usr/bin/grep` agree.
2. **S4 null (code dirs): survives.** `eod` -w gives exit 1. `kinetic` gives exit 1. The six-way alternation gives exit 1. Positive arm, same command with `\|OnBarUpdate\|webhook` appended: **12** files. So alternation fires and the directories resolve. (`-w nq` also gives 12 files.)
3. **S5 null (NinjaScript hooks): survives.** Exit 1. The same pattern with `\|OnBarUpdate` appended gives **2** hits. The strategies take whatever series the chart supplies (`PraxisNoiseAreaBreakout.cs:132` checks only for 1-minute bars). There is no provider hook.
4. **S6 null (decision files): survives.** All five files exist (`ls -la` shows each), so exit 1 is a true no-match, not a missing file. Positive arm, `provider` in the same files: `DECISIONS.md:4`.
5. **S8 null (old logs): survives, and it's wider than the artifact's run.** "kinetick" appears 0 times in all 17 files in `log/`, which includes the non-`.en` `log.*.txt` copies and `Install.xml` that the artifact skipped. Positive arms in the same files: "Simulated Data Feed" 3/5/3 (the 08-15 00001, 08-29 00000 and 08-29 00001 `.en` files) and "Historical Data Server" 2/16/6/2 (08-16, 08-17, 08-18, 08-28). The non-`.en` twins give identical counts. The `NinjaTrader 8` (non-full) copy has no `log/` folder.
6. **The NQCONT import route doesn't need `NQ ##-##`: survives.** The import instructions have **0** `##-##` hits (the positive arm "NQ 12-25" in the same file: 16). The import is a 1-minute file copy into `NQCONT` (`…w1-q1-import-instructions.md:84, :90-92`). The live path (n8n workflows, file drop, consumer) has no data-provider term (S4).
7. **Option C's D-071 conflict and the absence of Rithmic: correct as stated.**
8. **The S8 line itself:** :114-116 is labelled as reasoning and ends "Amear decides". It answers no question for Amear. The defect is in what it leaves out (F1), not in deciding.

## Process log

Read the artifact. Re-ran S2, S4, S5, S6 and S8 with positive arms. Listed the rescue `log/`, `db/` and `db/day` folders and their mtimes. Read the 08-16 log window. Opened a copy of the sqlite read-only. Searched specs, runbooks, config, the NQCONT reports, the walkthrough and `~/praxis-signals` for continuous / `##-##` / provider / daily. Read D-071 (update 2 row 13) and DECISION_LOG :424. About 18 tool calls.

## Files staged

None. This one new untracked file, no `git add`.

## Result

Two MAJOR findings (F1, F2) and three MINOR (F3–F5). Conclusions (a) and (b) hold in the present tense, but with under-stated evidence. (c) is over-labelled VERIFIED. (d) leaves out B's conflict with D-071.

VERDICT: BROKEN
