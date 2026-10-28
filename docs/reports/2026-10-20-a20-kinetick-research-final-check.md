# a20 Kinetick research — final adversarial check

VERDICT: BROKEN

## Task
Break docs/reports/2026-10-20-a20-kinetick-research.md (final version).

## Mode
ADVERSARIAL

## Criterion
S1/S2 (specs/SPEC_RUBRIC.md:107-108), S8 (:114).

## Process log
- Created file (PENDING).
- Read artifact (425 lines), A F1-F3, B F1-F2 in full.
- Re-ran E7, E11, E1 (both /usr/bin/grep and the shell `grep` wrapper), E3.

## Findings (appended as found)

### N1. E1 / Q2 inventory claim is false: 4 pre-existing files mentioning Kinetick were missed — MAJOR
- Claim (artifact :64): "search E1 covers all 25 files that mention it"; E1 header (:179) "Every file mentioning Kinetick (tracked + untracked)".
- Defect: false-null / missed source (S2). E1 was run with this shell's `grep` function (a ugrep wrapper; its output has no `./` prefix, matching E1), which skips gitignored paths. `/usr/bin/grep -rilI kinetick --exclude-dir=.git .` additionally returns, all pre-dating the unit:
```
-rw-r--r--@ 1 admin  staff  12694 2026-08-29_12:30:13 .claude/agent-memory/praxis-auditor/audit_evidence_standards.md
-rw-r--r--@ 1 admin  staff  51786 2026-05-05_17:28:01 Redemtion/Research Results/2nd round/compass_artifact_wf-ee42cda6-..._text_markdown.md
-rw-r--r--@ 1 admin  staff  30964 2026-05-06_12:15:05 Redemtion/Research Results/Round 3/compass_artifact_wf-ec22adb4-..._text_markdown.md
-rw-r--r--@ 1 admin  staff  20328 2026-05-05_16:47:28 Redemtion/Research Results/ROUND_2_RESEARCH_PROMPT_Agent_1.md
.gitignore:7:Redemtion/	Redemtion/Research Results/ROUND_2_RESEARCH_PROMPT_Agent_1.md
...2nd round/compass_artifact...:101:| **Kinetick** (NinjaTrader's own DTN-rebadged service) | Native NT adapter; 180 days tick, multi-year minute | Standalone (no broker required) | ~$65/mo base + ~$11 CME non-pro = ~$76/mo (no funded account) | ...
```
  Wrapper re-run gives 30 = the 25 listed + the 5 unit files; `redemtion|agent-memory` count in it = 0. "Redemtion" appears 0 times in the artifact, W1, A and B.
- Why it matters: Q1 (:5, :50-56) says every Kinetick product fact is "general knowledge" and NT8's rebrand is a "weak, unconfirmed recollection"; a May-2026 research artifact in the working tree describes Kinetick as "DTN-rebadged" with pricing and history depth. It does not change Q3 or the "no Amear ruling" finding (the hits are research, not decisions; the agent-memory hit is a methodology note).
- Smallest fix: rerun E1 with `/usr/bin/grep` (or `--no-ignore`), restate the count, and add the Redemtion research lines to Q1 as REPORTED (pre-PRAXIS research, its own sources unchecked).

### N2. Summary line 3 labels a conclusion VERIFIED that the body labels INFERRED, and drops the body's stated exception — MAJOR
- Claim (artifact :15): "**Nothing in PRAXIS needs it connected.** That covers the signal path, the NinjaScript, the n8n workflows, the Block 2 data and the NQCONT import. Every search came back empty ... (VERIFIED, below)."
- Defect: wrong label / summary stronger than body (S2), in a line Amear reads first. Same class as A-F1, which was graded MAJOR for the same reason. The body says:
  - :95 "no dependency found ... **with one latent exception (a stale spec step)**"
  - :99 "VERIFIED (search). **INFERRED that no mention = no dependency**"
  - :100 Block 2: "A *future re-pull* of daily data has an untested provider path ... UNVERIFIED"
  - :101 latent B2 spec step "Would need provider support if re-run as written"
  The summary turns "no dependency found (search VERIFIED, conclusion INFERRED, one latent exception)" into an unqualified VERIFIED "Nothing ... needs it", and names "the Block 2 data" without the re-pull caveat.
- Evidence: artifact lines quoted above (read from the file this session). The searches do hold (see Survived), so this is a labelling defect, not a false null.
- Smallest fix: ":15 → No search found anything in PRAXIS that needs it connected (searches VERIFIED, each with a positive control; 'no mention = no need' is INFERRED). One stale spec step would need provider support if anyone re-ran it as written (Q3)."

### N3. Summary line 2: three small over-reaches — MINOR
- (a) :14 "Your old install had it set *not* to connect at startup (VERIFIED, old `Config.xml:34`)". Q1 1.2 (:39) says "Values VERIFIED; meaning INFERRED". The summary drops the hedge. MINOR only because E5 corroborates it: across 3 launches only Simulated Data Feed auto-connects and there are 0 Kinetick lines. Re-run:
```
   1 2026-08-15 10:12:01:190|1|4|Auto connecting 'Simulated Data Feed'...
   1 2026-08-29 09:28:25:691|1|4|Auto connecting 'Simulated Data Feed'...
   1 2026-08-29 11:02:45:337|1|4|Auto connecting 'Simulated Data Feed'...
log.20260815.00000.en.txt:0 ... log.20260829.00001.en.txt:0   (all 8 .en logs: 0 kinetick)
```
- (b) :14 "No surviving old log mentions it at all (VERIFIED)". The old install's trace files do mention it: 3 of 9 contain `Kinetick` (E6, re-run below), and Q1 1.4 relies on them. True only if "log" means `log/` and excludes `trace/`. A trader won't read it that way.
```
trace.20260815.00001.txt:1   trace.20260829.00000.txt:1   trace.20260829.00001.txt:1
subscription=Free licensedProviders='Playback Simulator NinjaTrader ... Kinetick ... Rithmic for NinjaTrader ...
```
- (c) :14 "Nobody in the PRAXIS record ever set it up or decided anything about it." The body (:64) limits this to Amear. But the master's migration item 13 explicitly carried it over: `docs/reports/2026-09-29-vm-migration-concerns.md:121` "Connections as before, and nothing more: Simulated Data Feed; Kinetick EOD configured." And B1-0 claims use (C1, contested).
- Smallest fix: "(values VERIFIED; meaning INFERRED)"; "no `log/` file mentions it; the licence trace lists it"; "No Amear decision and no setup entry is on file; the master's migration plan carried it over as 'configured'".

### N4. S8-adjacent: the scope of Amear's own D-071 is treated as settled — MINOR
- Claims: S6 :397 "**D-071 (Amear's migration condition):** options B and C would cross it" (no label). Open question 2 (:404) "does D-071's 'no other connection' stand, or do you amend it?" Summary :17 "Leaving it off is the only option that changes nothing", while :18 says "PRAXIS's view is kept separate".
- Defect: whether "no other connection" (said about NT8's self-connection at migration) covers a by-hand EOD connection is Amear's question to answer. Q4 :120 correctly labels the conflict INFERRED. But :397 states it flat, and :404 offers only "stand / amend". It leaves out a third answer: "D-071 doesn't reach this". Nothing is decided for him ("Your call", "Amear decides"), so this is not a full S8 break. It is a framed choice.
- Smallest fix: label :397 "(INFERRED from its wording)". Make :404: "Does D-071's 'no other connection' cover connecting Kinetick by hand or at startup? If it does, does it stand or do you amend it?"

### N5. Evidence blocks that are partly described, not pasted — MINOR (S1)
- E5 ":285 == autoconnect" and ":292 == HDS" show no command. The pasted autoconnect block is a filtered subset: my re-run of `Auto connecting|Simulated Data Feed: Primary` also returns the Connecting/Disconnecting lines, e.g. `2026-08-29 11:01:38:602|1|2|Simulated Data Feed: Primary connection=Disconnected`. The counts match (HDS total re-run = `26`).
- E6 :308 "Line content per W1" means the manager didn't paste the content. My re-run confirms it (above).
- E3 :266 says the values at `:44/:47/:66/:109/:116/:208` are "from W1's pasted run", not re-pasted. My re-run confirms every one (`44: <User />`, `47: <Free>true</Free>`, `106-119` all `Unknown`, `208 <MultiProvider>true`; `:66` holds the username, count 1, value not printed).
- Q3 :99 claims 0 hits for "EOD/end of day/data feed/historical data". E7 pastes only `kinetick|kinetic|provider7`. My re-run: `xargs /usr/bin/grep -l -i -E '\beod\b|end of day|data feed|historical data'` → `exit=1`. True, but not shown in E7.
- Smallest fix: paste the commands for the E5 sub-blocks, the E6 line and the extra-term search.

### N6. Missed outside-repo origin of the C2/C3 "has Kinetick data" claim — MINOR
- `~/praxis-signals/b2-data/outbound/INSTRUCTIONS.md` (mtime 2026-07-24 09:54, orchestrator → VM agent), line 94: "**Definitive check** — open two charts for **2026-07-17**: native `NQ 12-25` (has Kinetick data) and the imported **`NQCONT`**". This dates both the C2 label and the C3 control chart to 07-24, a month before s52's walkthroughs. W1 S7 listed the file as a hit. It does not appear in Q2's table or in C2/C3.
- Smallest fix: add a 07-24 row to Q2 and cite it under C2/C3.

## Survived (with evidence)

1. **A-F1 fixed in body.** :104 "show NT8 **connected to** the 'NinjaTrader Historical Data Server' (26 lines) ... INFERRED: bars fetched in that window came from there." Re-run HDS count = `26`. The HDS claim is no longer in the summary.
2. **A-F2 fixed.** :120 "values VERIFIED; their meaning ... is INFERRED from the field names, UNVERIFIED". :126 "whose meaning is INFERRED". Values re-run: `208 <MultiProvider>true`; `106-119` all `Unknown`.
3. **A-F3 fixed.** :121 "Changes a value that reads `false` in the 08-29 Config.xml (VERIFIED). Its history before 08-29 is unrecorded". Re-run `grep -c -i startup` on the 07-12 report → `0`.
4. **B-F1 fixed.** :120 row B "**Conflicts with D-071** 'no other connection' (INFERRED from its wording): it needs Amear to amend D-071 first". :122 row D "**departs from item 13**". The PRAXIS view (:131) no longer offers B as "the way to try".
5. **B-F2 fixed.** :104 "Kinetick not shown; provider of the oldest data UNVERIFIED ... 49 of 51 NQ daily-bar files are dated 2026-07-14 15:09:06". Re-run E8: `49 2026-07-14_15:09:06 / 1 2026-07-20_11:26:23 / 1 2026-08-16_08:16:53`; `grep -rlai kinetick db` → `exit=1`.
6. **E-blocks re-run, output matches:**
   - E3: both hashes `7a040a11…0edf6`, 16879 B, Aug 29 12:00; lines 15-65 as pasted.
   - E5: per-log counts and auto-connect lines.
   - E6: per-trace counts `0/1/0/0/0/0/0/1/1`.
   - E7: 44 files; `exit=1`; positive arm `PraxisSignalConsumer.cs`, `praxis-signals-sweep.sh`; no BarsRequest/Connection/Provider in `ninjascript/*.cs`.
   - E8, as above.
   - E9: spec :5, :16, :115; `22` daily files; `0` for startup.
   - E10: the same two Config.xml paths; mount grep `exit=1`.
   - E11: staged set identical, 9 paths.
   - E4: I viewed the 07-24 screenshot. The rows are "Kinetick – End Of Day (Free)", "Playback", "Simulated Data Feed" (green dot, "disconnect"), "Simulation". No dot on Kinetick. It matches.
   - E1: reproduces with the shell's `grep` wrapper (30 = 25 + 5 unit files). The defect is the scope claim (N1), not fabrication.
7. **Citations checked, all hold:**
   - runbook :13
   - 07-12 :71-72
   - proposal :46, :49
   - capture notes :51-53, :184-185
   - wx7 :105, :184
   - s52 :235-236, :264
   - walkthrough v1 :142/:144, v2 :210-212
   - s53 :407, :418, :428-432
   - mig :121-122
   - upd2 :62, :120
   - DECISION_LOG :363 (bare `NQCONT` vs request `NQCONT 09-2025`)
   - walkthrough :183
   - reference :186
   - `PraxisNoiseAreaBreakout.cs:132` (Minute/1 check)
   - w4 :270-271
   - DECISION_LOG :424 and DECISIONS :184 (as pasted in E2)
8. **Outside-repo code null survives.** Re-run with `/usr/bin/grep`, kinetick in `~/praxis-signals` `*.cs|py|js|json|sh` → `exit=1`. Positive arm `OnBarUpdate|FileSystemWatcher` → `b2-data/ninjascript/PraxisNoiseAreaBreakout.cs`, `archive/PraxisSignalConsumer.cs`.
9. **S8 core survives.** The PRAXIS view (:129-131) is headed "reasoning only — not a decision" and ends "**Amear decides.**". Open Q1 (:403) ends "Your call". No option is presented as chosen.

## Verification evidence
All command output is pasted inline under each finding and Survived item above, from this session's runs.

## Files staged
None. One new untracked file (this one). No `git add`, no edits to existing files.

## Result
Two MAJOR (N1 false-null file inventory and missed in-tree Kinetick research; N2 summary line 3 VERIFIED over an INFERRED body conclusion that has a stated exception). Four MINOR (N3–N6). All five earlier MAJORs (A-F1..F3, B-F1..F2) are actually fixed in the body.
VERDICT: BROKEN
