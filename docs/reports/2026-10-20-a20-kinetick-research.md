# a20 follow-up — what "Kinetick – End Of Day (Free)" is, and whether PRAXIS needs it
**Post-audit correction (2026-10-20) appended at the end; it supersedes the lines it names.**

**Bead:** `Praxis_build-a20` (follow-up). **Date:** 2026-10-20. **Author:** praxis-manager (session of 2026-10-20).
**Brief:** answer Amear's "i dont know what that is or i dont remeber. look into it" (`DECISION_LOG.md:424`, uncommitted worktree line) about row K1 of the a20 results (`docs/reports/2026-10-20-a20-results.md:21-22`).
**Read-only.** No NT8, VM, VMware or network interaction. No web tool was available to any agent in this unit, so **no product fact about Kinetick was vendor-checked**: each is general knowledge (UNVERIFIED) or comes from the record or pre-PRAXIS research (REPORTED).

**Labels.** **VERIFIED** = seen in this unit, with the command/output pasted or file:line quoted verbatim. Reading a machine-written file (Config.xml, a log, a folder listing) is VERIFIED for *what the file contains*; what that implies about NT8's behaviour is INFERRED. **REPORTED** = the record says so (cited). **INFERRED** = reasoning, basis stated. **UNVERIFIED** = general knowledge, not checked here.

---

## Plain-language summary (for Amear)

1. **What it is (UNVERIFIED, general knowledge):** Kinetick is a market-data service NinjaTrader has offered. The "End Of Day (Free)" connection is its free tier: one price bar per day (open, high, low, close, volume), after the close. It gives no live prices, no 1-minute or tick bars, and it does not place orders.
2. **No setup entry, and no decision by you, is on file.** Your "undecided" today is the only ruling (REPORTED, `DECISION_LOG.md:424`). The master's migration plan carried it over as "configured" (REPORTED). On your old install its startup setting reads `false` (value VERIFIED, old `Config.xml:34`; that this means "doesn't connect at startup" is INFERRED, and the logs agree). No old connection log mentions it. NT8's licence trace lists it among its licensed providers (both VERIFIED).
3. **No search found anything in PRAXIS that needs it connected.** The searches covered the signal path, the NinjaScript, the n8n workflows, the Block 2 data and the NQCONT import. Each empty search was checked against a word known to be there (searches VERIFIED, below). Concluding "no mention = no need" is INFERRED. One exception: a stale planning step would need a data provider like Kinetick if anyone re-ran it as written (Q3).
4. **It is not recorded as the cause of the NQCONT "unknown instrument" error.** It does appear once in that diagnosis, as the possible reason a *control check* had no minute data (REPORTED, session 53 §6b).
5. **Your own condition matters here.** When NinjaTrader connected itself on Fusion, you accepted it on condition "no orders, no other connection" (D-071). Connecting Kinetick, whether by hand or at startup, would be another connection (INFERRED from that wording). Leaving it off is the only option that changes nothing.
6. **The choice is yours.** Options and what each touches are in Q4. PRAXIS's view is kept separate.

---

## Task

Answer Q1–Q4 from the brief for a trader who has forgotten what Kinetick is, each claim labelled. Use one research worker and an independent adversarial worker. Write no ledger, commit nothing.

## Rubric criteria addressed

`specs/SPEC_RUBRIC.md` **S1** (`:107`, pasted output), **S2** (`:108`, nothing stated above its evidence), **S8** (`:114`, Amear's question not answered for him), **R3** (`:159-166`: "X depends / doesn't depend on Y" settled by search with a positive control, not by inspection), **S6** (`:113`, cross-block section below).

---

## Q1. What is "Kinetick – End Of Day (Free)"?

### What the old install's own files show (Parallels install, rescue copy, file mtime 2026-08-29; **not Fusion**)

| # | Claim | Label |
|---|---|---|
| 1.1 | A connection named `Kinetick – End Of Day (Free)`, type `NinjaTrader.Cbi.KinetickOptions`, `<Provider>Provider7</Provider>`, `<Free>true</Free>`, empty `<User />` and `<Password />` (`Config.xml:32-50`) | VERIFIED (file contents; excerpt in Verification evidence) |
| 1.2 | `ConnectOnStartup` is `false` for Kinetick (`:34`) and `true` for Simulated Data Feed (`:18`). That `true` means "connects at startup" is read off the field name | Values VERIFIED; meaning INFERRED (consistent with logs E5: only Simulated Data Feed auto-connects) |
| 1.3 | The connection list (`:15-65`) holds exactly three blocks: Simulator, Kinetick, Playback. There is **no Rithmic block** | VERIFIED |
| 1.4 | NT8's licence check lists `Kinetick` among licensed providers, `subscription=Free` (3 of 9 trace files) | VERIFIED (trace text; E6) |

### What the record says (REPORTED)

- "Kinetick (NT8 native partner) | EOD free; minute/tick paid | $" — Block 2 proposal, no vendor source cited (`docs/specs/2026-07-15-block2-backtesting-scope-proposal.md:46`).
- "An **End Of Day** feed does not supply intraday minute bars." (`docs/reports/2026-08-29-session53-nqcont-resolution-and-rth-corpus-read.md:418`, unsourced).
- "**UNVERIFIED** whether Kinetick's free EOD tier serves any intraday history at all — a vendor-plan fact, and nobody here has connected it." (`docs/reports/2026-08-29-session53-w4-adversarial-q4-designs.md:270-271`).
- Continuous contracts `NQ ##-##` "Requires **provider support** (historically Kinetick / eSignal / IQFeed)" (`docs/reference/2026-07-24-nt8-windows-reference.md:186`). Whether Kinetick EOD Free meets that "is not recorded" (session 53 `:431-432`).

- **Pre-PRAXIS research (May 2026, gitignored `Redemtion/` folder; its own sources unchecked):** "**Kinetick** (NinjaTrader's own DTN-rebadged service) | Native NT adapter; 180 days tick, multi-year minute | Standalone (no broker required) | ~$65/mo base + ~$11 CME non-pro = ~$76/mo" (`Redemtion/Research Results/2nd round/compass_artifact_wf-ee42cda6-…_text_markdown.md:101`). That describes the **paid** tier, not EOD Free. The same file, `:564`: CME data bundle via NinjaTrader/Rithmic is "pass-through, not Kinetick". It also proposed a monitor, "Kinetick/Continuum data feed quote freshness" (`:511`), which was not carried into any current spec (INFERRED from E12's search; Q3). The research lines are REPORTED, files dated 2026-05-05/06.

### General knowledge — all UNVERIFIED

- Kinetick is a market-data brand offered through NinjaTrader (consistent with the May-2026 research line above). The free End Of Day tier gives **daily bars only**, published after the session closes, for US stocks, indices and futures. It costs nothing.
- It does **not** give real-time quotes, intraday (minute/tick) history, market depth, or order routing. Paid Kinetick tiers gave real-time and intraday data.
- NT8 ships with this connection pre-configured and no login needed. That would fit the empty user and password (1.1), but the files do not prove it, and the record holds no setup entry either way.
- Whether the Kinetick service still answers connections in October 2026 is **unknown**. The research worker recorded a weak, unconfirmed recollection that NinjaTrader wound it down or rebranded it. Treat that as an open question.
- Whether it serves NQ futures daily bars, or a continuous `NQ ##-##` series, is **unknown**.

**Settling observation (not run; would need a read-only look at NinjaTrader's own help pages):** the vendor's description of the EOD tier and its current status.

---

## Q2. What PRAXIS has recorded about it

**No document records anyone setting Kinetick up, or Amear making any decision about it, before 2026-10-20.** E1 covers the 29 files that mentioned it before this unit, gitignored ones included: 25 found by the first search, plus 4 gitignored that the first search **missed**. That miss was caught by the final adversarial check (N1) and is corrected in E1. Rows below are REPORTED unless marked.

| Date | Who / what | Citation |
|---|---|---|
| 2026-05-05/06 | Pre-PRAXIS research rounds (gitignored `Redemtion/`): Kinetick costed as a paid data option; a quote-freshness monitor proposed. Research, not a decision | `Redemtion/Research Results/2nd round/compass_artifact_wf-ee42cda6-…:101`, `:511`, `:564`; `…/ROUND_2_RESEARCH_PROMPT_Agent_1.md:56`, `:206`; `…/Round 3/compass_artifact_wf-ec22adb4-…:109` |
| 2026-07-09 | B1-0 report (trader-executed, orchestrator-transcribed): chart data "real-time … via NinjaTrader's bundled Kinetick feed", and "Data feed was real-time Kinetick via the `amear238` NT login". **Contested — C1** | `docs/reports/2026-07-09-b1-0-nt8-parallels-validation.md:82`, `:164` |
| 2026-07-10 | Install runbook prerequisite: "connected (Simulated Data Feed or Kinetick login is fine; orders will go to the internal Sim account)" | `docs/runbooks/2026-07-10-b1f-nt8-consumer-install.md:13` |
| 2026-07-12 | VM run: "Only three connections exist in Config.xml — Simulated Data Feed, Playback Connection, Kinetick End Of Day (Free). No live brokerage is configured" | `docs/reports/2026-07-12-b1f-t1-t4-vm-run-blocked.md:71-72` |
| 2026-07-15 | Block 2 **proposal** lists Kinetick as one data option ("NT8 default provider or Kinetick") | proposal `:46`, `:49` |
| 2026-07-15 | **Amear's Block 2 data decision**: "NT8 default-provider MINUTE history — no paid-data budget this block." Kinetick not named | `DECISIONS.md:184` |
| 2026-07-24 | Screenshot capture: Kinetick listed, no dot; Simulated Data Feed "[green dot = currently connected]" | `docs/reference/assets/nt8-2026-07-24/00-coworker-capture-notes.txt:51-53`, `:184-185`; screenshot re-viewed this unit (VERIFIED, E4) |
| 2026-07-24 | Orchestrator → VM-agent instructions: "**Definitive check** — open two charts for **2026-07-17**: native `NQ 12-25` (has Kinetick data) and the imported **`NQCONT`**". The earliest found source of the "has Kinetick data" label and of the C3 control chart | `~/praxis-signals/b2-data/outbound/INSTRUCTIONS.md:94-95` (outside repo, mtime 2026-07-24 09:54) |
| 2026-07-24/25 | In-VM status files call the old `NQ 12-25` data "Kinetick-sourced". **Unsupported — C2** | `~/praxis-signals/b2-data/inbound/4uu-VM-status-2026-07-24.md:56-57`; `…-07-25.md:95-98` (outside repo) |
| 2026-07-25 | wx7: "all 44 raw export files (22 daily + 22 one-minute contracts) were pulled from NT8's default data provider … No paid data" | `docs/reports/2026-07-25-wx7-build-progress-for-scoping-agent.md:105` |
| 2026-08-29 | Session 52/53: "real Kinetick data" for native `NQ 12-25` (C2/C3). Session 53 §6b names the EOD feed as why the NQCONT diagnostic control may lack minute data | s52 investigation `:235-236`; walkthroughs v1 `:144`, v2 `:211-212`; s53 `:407`, `:418`, `:428-432` |
| 2026-08-29 | In-VM capture: "listed, not connected (no green dot, no 'disconnect' option shown for it)" | `~/praxis-signals/b2-data/inbound/4uu-VM-capture-2026-08-29.md:172-173` (outside repo) |
| 2026-09-29 | Master's migration request (not an Amear ruling): "Connections as before, and nothing more: Simulated Data Feed; Kinetick EOD configured" | `docs/reports/2026-09-29-vm-migration-concerns.md:121-122` |
| 2026-10-19 | Migration update 2: Amear accepted NT8's self-connection "on condition: no orders, no other connection (D-071)"; "Kinetick EOD: NOT YET KNOWN" | `docs/reports/2026-10-19-windows-vm-state-update-2-from-migration.md:67`, `:120` |
| 2026-10-20 | a20 reads: "Kinetick – End Of Day (Free), no dot" | `docs/reports/2026-10-20-a20-results.md:21-22` |
| 2026-10-20 | **Amear:** K5/K8 accepted ("Simulated Data Feed" = what D-071's "Simulation" meant); "**Kinetick EOD (K1): undecided.**" — **the only Amear ruling on Kinetick** | `DECISION_LOG.md:424` |

**What was it used for?** **No recorded use.** It was not the Block 2 source (`DECISIONS.md:184` names the default provider). It was not part of the NQCONT import, which is a file import of PRAXIS's own stitched CSV (REPORTED, wx7 `:105-106`). No capture shows it connected (07-24, 08-29, 10-20). The only claims of use are C1 and C2, and both are contested.

### Contradictions in the record

- **C1.** B1-0 (07-09) says the feed was "real-time Kinetick via the `amear238` NT login". Against it stands one direct counter-claim, w4 `:270-271` "nobody here has connected it" (REPORTED). The machine evidence is *consistent with* C1 being a mislabel but **post-dates 07-09**, so it cannot settle it: `ConnectOnStartup false` in the 08-29 file, logs only from 08-15 on, and `amear238` as the NinjaTrader account username (`Config.xml:66`) while Kinetick's `<User />` is empty (VERIFIED file contents). INFERRED: B1-0 probably took the NT login plus Simulated Data Feed for Kinetick. B1-0 `:82` also says this is "the same data feed that will be used with Rithmic in production", which nothing else in the record supports.
- **C2.** "Kinetick-sourced" / "has Kinetick data" `NQ 12-25` history (earliest found: 07-24 VM-agent instructions `INSTRUCTIONS.md:94-95`; then the 07-24/25 status files, s52 `:236`) vs "NT8's default data provider" (wx7 `:105`, `DECISIONS.md:184`). No machine evidence supports "Kinetick". The only record support is B1-0's contested claim. The actual provider for data written before 2026-08-15 is **UNVERIFIED** (see Q3 row "historical data source").
- **C3.** The session-52 walkthroughs tell Amear to compare against "native `NQ 12-25` (has real Kinetick data)" for **2026-07-17** (v1 `:142`/`:144`, v2 `:210-212`). The same check first appears in the 07-24 VM-agent instructions (`~/praxis-signals/b2-data/outbound/INSTRUCTIONS.md:94-95`). The stored `NQ 12-25` minute files run 2025-09-11 → 2025-12-21, 90 files, none from 2026 (VERIFIED by both the worker and adversary A). INFERRED: that chart would have no bars for that date, whatever the provider. **Outside this brief; flagged for the master, not fixed.**

---

## Q3. Does anything in PRAXIS depend on Kinetick being connected?

**Finding: no dependency found, current or planned, with one latent exception (a stale spec step).** Each row rests on a search that was re-run, with a positive control (Verification evidence E7–E9).

| Area | Dependency? | Evidence | Label |
|---|---|---|---|
| Live signal path (NinjaScript consumer, n8n workflows, scripts, config, deploy, signals) | **None found** | 0 hits for kinetick/kinetic/Provider7 and, separately, for EOD/end of day/data feed/historical data/default provider, in all 44 tracked code and config files; positive arms (FileSystemWatcher/Rithmic; OnBarUpdate) fire in the same pipeline (E7). No `BarsRequest`/`AddDataSeries`/`Connection`/`Provider` in the NinjaScript (E7) | VERIFIED (search). INFERRED that no mention = no dependency: the strategies take whatever series the chart supplies (`PraxisNoiseAreaBreakout.cs:132` checks only for 1-minute bars, per adversary B) |
| Block 2 backtesting | **None found today** | Minute and **daily** inputs (22 `_daily.csv` + 22 minute files, used for roll dates) are already on the Mac (`ls ~/praxis-signals/b2-data/raw \| grep -c daily` → `22`, E9). Decision: default provider (`DECISIONS.md:184`, REPORTED) | VERIFIED (files present) + REPORTED. A *future re-pull* of daily data has an untested provider path (see multi-provider note, Q4) — UNVERIFIED |
| **Latent:** B2 acquisition spec §5 step 2 | **Would need provider support if re-run as written** | It says to download "instrument `NQ` (continuous)" in NT8 (`docs/specs/2026-07-15-b2-data-acquisition-spec.md:115`). Continuous needs "provider support (historically Kinetick / eSignal / IQFeed)" (reference `:186`). Superseded in practice by the Python stitch, wx7 E2 (`:184`), but the spec status still reads "Mac-side spec COMPLETE" (`:5`) with no superseded marker (E9) | REPORTED + VERIFIED (lines read). **Flagged for the master; not fixed** |
| NQCONT import | **None found** | The import is a 1-minute file copy into `NQCONT`. 0 `##-##` hits in the import instructions, positive arm `NQ 12-25` = 16 (adversary B) | REPORTED + VERIFIED (search) |
| NQCONT "unknown instrument" defect | **Not recorded as cause or fix.** Recorded in its *diagnostic*: s53 §6b ("DEFECT FOUND in the existing Check A1 — the control is confounded", `:407`) cites the EOD feed as why the control may lack minute data. s52 open question 6 (`:264-266`) asks whether `<ROOT> ##-##` works with imported data or is strictly provider-served | The defect is recorded as a name mismatch: storage `NQCONT` vs request `NQCONT 09-2025` (`DECISION_LOG.md:363`). The a20 walkthrough: "a separate defect" (`:183`) | REPORTED. Not investigated, per brief |
| Historical data source (old install) | **Kinetick not shown; provider of the oldest data UNVERIFIED** | The 08-15 → 08-29 logs show NT8 **connected to** the "NinjaTrader Historical Data Server" (26 lines) and contain 0 Kinetick lines (E5). INFERRED: bars fetched in that window came from there. But 49 of 51 NQ daily-bar files are dated **2026-07-14 15:09:06**, before any surviving log. Nothing in the rescue `db/` names any provider (E8) | Log text and mtimes VERIFIED; which provider wrote the 07-14 batch **UNVERIFIED** |
| Outside-repo code (`~/praxis-signals`) | **None found** | Only `.md`/`.txt` briefs mention Kinetick; the outside `ninjascript/` has none (worker S7). The final check re-ran it on `*.cs|py|js|json|sh`: `exit=1`, positive arm `OnBarUpdate|FileSystemWatcher` → 2 files | VERIFIED (search, by W1 and W5; not re-run by manager) |
| Monitoring (pre-PRAXIS proposal) | **Not adopted** | May-2026 research proposed a "Kinetick/Continuum data feed quote freshness" monitor (Q1). E12: 0 hits for `quote freshness`/`last-tick-age` outside `Redemtion/`, while `circuit breaker` hits `docs/specs/STRATEGY_HEALTH_MONITOR_SPEC.md` | VERIFIED (search); "not adopted" INFERRED from no mention |

---

## Q4. Amear's options — what each touches (the decision is Amear's)

**State on Fusion today:** K1 shows the row present with no dot (REPORTED by Amear, `a20-results.md:21-22`). "No dot = not connected" is INFERRED from the capture legend. Fusion's own `ConnectOnStartup` value is **unread**: no Fusion-side config is reachable from the Mac (no VMware share mounted; E10). INFERRED `false` only via the reported faithful restore from `NinjaTrader 8-full` (update 2 `:62`), whose Config.xml is byte-identical to the one read here (VERIFIED, E3).

**Two recorded constraints bear on every option:**
- **D-071 (Amear):** NT8's self-connection accepted "on condition: no orders, no other connection" (update 2 `:67`, REPORTED), with the accepted connection pinned on 10-20 as the Simulated Data Feed (`DECISION_LOG.md:424`, REPORTED).
- **Item 13 (master's migration principle, not an Amear ruling):** "Connections as before, and nothing more" (`2026-09-29-vm-migration-concerns.md:121`, REPORTED).

| Option | What it touches | D-071 / item 13 | Risk / what is known |
|---|---|---|---|
| **A. Leave as found (listed, not connected)** | Nothing | Consistent with both | Matches the old install (`Config.xml:34` VERIFIED for the 08-29 file). INFERRED: no PRAXIS function loses anything (Q3) |
| **B. Connect by hand only when needed** | Connections menu; a network connection to Kinetick's servers | **Likely conflicts with D-071** "no other connection" (INFERRED from its wording). If Amear reads D-071 as covering it, he would need to amend it first | UNVERIFIED: would contact Kinetick and could write daily bars into NT8's local store (the old install has a `db/day` folder, VERIFIED). UNVERIFIED: whether the service still works. UNVERIFIED: whether it changes which provider NT8 uses for NQ daily data. File facts: `MultiProvider` reads `true` (`Config.xml:208`), every `Preferred…Connection` reads `Unknown` (`:109`, `:116`) — **values VERIFIED; their meaning ("several connections allowed, none preferred") is INFERRED from the field names, UNVERIFIED** |
| **C. Connect at startup** | `ConnectOnStartup` in Fusion's NT8 settings | **Likely conflicts with D-071** (same reading as B, INFERRED) **and departs from item 13** | Same as B, on every launch. Changes a value that reads `false` in the 08-29 Config.xml (VERIFIED). Its history before 08-29 is unrecorded |
| **D. Remove the connection** | NT8's connection list | Not a connection, so D-071 is untouched; **departs from item 13** ("as before") | UNVERIFIED: whether it can be re-added easily. INFERRED: no PRAXIS gain (Q3) |

**Interference questions:**
- **Rithmic:** there is no Rithmic connection on the old install (VERIFIED, Config.xml `:15-65`) or in the Fusion list (REPORTED, `a20-results.md:21`). So there is nothing for Kinetick to interfere with today (INFERRED). Interplay with a future Rithmic connection: UNVERIFIED.
- **Simulated Data Feed:** UNVERIFIED. Nobody in the record has connected Kinetick alongside it (w4 `:270-271`, REPORTED; 0 Kinetick lines in the surviving logs, VERIFIED E5). The only machine hint is the multi-provider fields above, whose meaning is INFERRED.
- **Orders:** `CanManageOrders` reads `true` in the Kinetick block (`:33`) and also in Playback (`:52`) (VERIFIED values). INFERRED: it is a generic field. Whether Kinetick EOD can route orders: UNVERIFIED (general knowledge says no). The runbook says orders go "to the internal Sim account" (`b1f-nt8-consumer-install.md:13`, REPORTED). Whether that holds with Kinetick connected: UNVERIFIED.

### PRAXIS view (reasoning only — not a decision)

INFERRED, from Q3 and the constraints above. No search found anything in PRAXIS that needs Kinetick, and it has never been seen connected. **A** is the only option that changes nothing and sits inside D-071 under any reading. **B and C**, if D-071 covers them, would need Amear to amend it first, and they bring an unknown effect on the data path, for no recorded benefit. **D** gains nothing and departs from "as before". If daily bars from Kinetick were ever wanted, that would be a new data-source decision for Amear (S4: a ledger entry before the change), not a settings tweak. **Amear decides.**

---

## Adversarial findings

Adversaries 1, A and B attacked the research worker's report (`…-worker1.md`). W5 and W6 attacked this report. Each saw only the artifact and the criteria, never a producer's reasoning.

- **Adversary 1 (full scope): NO RESULT.** It hit its turn limit with no verdict and wrote no file. Its last partial line flagged a possible false null on "continuous … provider" (wide-window search). Treated as no result, never as a pass. Re-dispatched as two narrower halves; the hint was covered by adversary B (F4, F5).
- **Adversary A (citations, labels, contradictions): VERDICT: BROKEN.** All 31 numbered citation checks held. 3 MAJOR, 5 MINOR:
  - A-F1 MAJOR: "Historical bars came from the NinjaTrader Historical Data Server (VERIFIED)" — logs show connection events only. **Resolved:** Q3 now says "connected to (VERIFIED)… bars came from there (INFERRED)".
  - A-F2 MAJOR: multi-provider field *meaning* under "VERIFIED context". **Resolved:** values VERIFIED, meaning INFERRED/UNVERIFIED (Q4 row B).
  - A-F3 MAJOR: "`false` since at least 2026-07-12 (VERIFIED)" — an 08-29 file can't show 07-12. Manager re-ran: `grep -c -i startup` on the 07-12 report → `0`. **Resolved:** "reads `false` in the 08-29 file; history unrecorded" (Q4 row C).
  - A-F4..F8 MINOR (unlabelled "Orders go to Sim regardless"; embellished "manager and auditors"; absence of a record treated as support for "pre-loaded"; C1 framing with post-dated evidence; C2 "nothing in the record" ignoring B1-0). **All five resolved** in Q1/Q2/Q4 wording above.
- **Adversary B (false nulls, missed sources, Q4/S8): VERDICT: BROKEN.** Every zero-hit search survived with a firing positive arm. 2 MAJOR, 3 MINOR:
  - B-F1 MAJOR: D-071 applied only to option C; B is also "another connection", and the PRAXIS view steered toward B. **Resolved:** D-071 and item 13 are now columns across all four options. The D-071 reading is labelled INFERRED, with its scope left to Amear (see N4). The PRAXIS view no longer offers B as "the way to try".
  - B-F2 MAJOR: the old historical-data source was labelled VERIFIED, but 49/51 NQ daily files pre-date every log. **Resolved:** Q3 "historical data source" row. Manager re-ran the mtimes (E8).
  - B-F3 MINOR: Block 2's 22 daily series were left out. **Resolved** (Q3 Block 2 row).
  - B-F4 MINOR: missed source, the B2 acquisition spec step for continuous `NQ`. **Resolved** as the "latent" Q3 row, flagged for the master.
  - B-F5 MINOR: the record ties Kinetick to the NQCONT *diagnostic* (s53 §6b, s52 Q6), not to its cause. **Resolved** (Q3 defect row, summary line 4).
- **Final check on this report (W5): VERDICT: BROKEN.** It confirmed all five earlier MAJORs fixed in the body, with current lines quoted, and all 22 citations it checked held. It found 2 new MAJOR and 4 MINOR:
  - N1 MAJOR: E1's inventory used the ugrep wrapper, which skips gitignored files. 4 were missed, including May-2026 Kinetick research in `Redemtion/`. Manager re-ran and confirmed (34 vs 30). **Resolved:** E1 corrected; Redemtion lines added to Q1 and Q2 as REPORTED; the monitor proposal searched (E12).
  - N2 MAJOR: summary line 3 said "Nothing in PRAXIS needs it (VERIFIED)" while the body labels the conclusion INFERRED, with a latent exception. **Resolved:** line 3 rewritten.
  - N3 MINOR: summary line 2 over-reaches (startup value vs meaning; "no log mentions it" vs the trace; "nobody set it up" vs master item 13). **Resolved:** line 2 rewritten.
  - N4 MINOR: D-071's scope was treated as settled. **Resolved:** INFERRED labels at Q4 B/C, S6 and the PRAXIS view; open question 2 now asks first whether D-071 covers it.
  - N5 MINOR: E5/E6 sub-blocks described, not pasted; the extra-term search not shown. **Resolved:** commands and output pasted (E5, E6, E7).
  - N6 MINOR: missed 07-24 source of "has Kinetick data" (`INSTRUCTIONS.md:94`). **Resolved:** Q2 row added and cited in C3.
- **Fix check (W6):** a narrow pass on the N1–N6 fixes only. Outcome under "Final adversarial check".

---

## Workers dispatched

| # | Mode | Scope | Outcome |
|---|---|---|---|
| W1 | BUILD (research) | Q1–Q4, Config excerpt, searches | Report delivered (`…-worker1.md`); self-stated PASS not relied on |
| W2 | ADVERSARIAL | Full attack surface | **No result** (turn limit, no verdict, no file) |
| W3 (A) | ADVERSARIAL | Citations, labels, C1–C5 | VERDICT: BROKEN — 3 MAJOR / 5 MINOR, all folded in above |
| W4 (B) | ADVERSARIAL | False nulls, missed sources, Q4/S8 | VERDICT: BROKEN — 2 MAJOR / 3 MINOR, all folded in above |
| W5 | ADVERSARIAL | Final report, narrow | VERDICT: BROKEN — 2 MAJOR / 4 MINOR (N1–N6), all folded in |
| W6 | ADVERSARIAL | N1–N6 fixes only | See "Final adversarial check" |

## Process log

1. Read the rubric. Took my own Kinetick file inventory (25 files; the brief's list missed 7, including the capture notes and a20 results). Passed the full list to W1.
2. Read the rescue Config.xml myself (both copies, hashed) and re-viewed the 07-24 screenshot.
3. Ran my own code search with a positive control before W1 returned.
4. Read W1's report in full and re-ran its key citations and log/trace counts (E2–E7).
5. Dispatched W2; it returned no verdict. Split the scope into W3 and W4, with a write-as-you-go rule.
6. Re-ran W3/W4's load-bearing evidence (E8, E9) before accepting it. Wrote this report with every finding folded in.
7. Dispatched W5 on the written report; it returned BROKEN (N1–N6). Re-ran N1 and N6 myself, applied the fixes, then dispatched W6 on the fixes.
8. Stop-gate note: `gate-manager-output.sh` fired three times mid-unit, because ending a turn while waiting on a worker grades the newest report (`a20-results.md`, which has no evidence section). After that I waited inside tool calls. No hook was edited.

---

## Verification evidence (pasted output, this unit, manager-run unless marked)

**E1. Every file mentioning Kinetick — CORRECTED.** The first run below was made before dispatch with this shell's `grep`, which is a wrapper function (`type grep` → "grep is a shell function from /Users/admin/.claude/shell-snapshots/snapshot-zsh-…sh", a ugrep wrapper). It **silently skips gitignored paths**, so its "tracked + untracked" scope was false: it missed 4 files. The final adversarial check caught it (N1). The corrected run uses `/usr/bin/grep` (after the five unit files existed):
```
$ /usr/bin/grep -rilI kinetick --exclude-dir=.git . | wc -l
      34
$ grep -rilI kinetick --exclude-dir=.git . | wc -l          (wrapper)
      30
$ comm -23 <(/usr/bin/grep -rilI kinetick --exclude-dir=.git . | sed 's#^\./##' | sort) <(grep -rilI kinetick --exclude-dir=.git . | sed 's#^\./##' | sort)
.claude/agent-memory/praxis-auditor/audit_evidence_standards.md
Redemtion/Research Results/2nd round/compass_artifact_wf-ee42cda6-0085-4b1e-a813-4f4221d90a63_text_markdown.md
Redemtion/Research Results/Round 3/compass_artifact_wf-ec22adb4-94b2-4977-8296-f2f3a6557e2f_text_markdown.md
Redemtion/Research Results/ROUND_2_RESEARCH_PROMPT_Agent_1.md
$ /usr/bin/grep -rn -i kinetick Redemtion | cut -c1-420     (excerpt)
Redemtion/Research Results/ROUND_2_RESEARCH_PROMPT_Agent_1.md:56:  - Kinetick (NinjaTrader's own data service) — cost, quality, history depth
Redemtion/Research Results/ROUND_2_RESEARCH_PROMPT_Agent_1.md:206:- **Data provider documentation** — Kinetick, Rithmic historical data, DTN IQFeed, FirstRate Data. Pricing, data formats, NinjaTrader compatibility, history depth
Redemtion/Research Results/Round 3/compass_artifact_wf-ec22adb4-…:109:- **NinjaTrader + Rithmic supports Eurex only at four FCMs: Dorman, AMP, Wedbush, and TheTradingPit.** EUREX fees ~$23/month + $30/month international real-time exchange package via Kinetick.
Redemtion/Research Results/2nd round/compass_artifact_wf-ee42cda6-…:101:| **Kinetick** (NinjaTrader's own DTN-rebadged service) | Native NT adapter; 180 days tick, multi-year minute | Standalone (no broker required) | ~$65/mo base + ~$11 CME non-pro = ~$76/mo (no funded account) | If you want NT8 paper-trading without opening a brokerage account. |
Redemtion/Research Results/2nd round/compass_artifact_wf-ee42cda6-…:511:| Kinetick/Continuum data feed quote freshness | TCP probe of NT data port + last-tick-age check | 60 sec | Critical |
Redemtion/Research Results/2nd round/compass_artifact_wf-ee42cda6-…:564:| CME Level 1 non-pro data bundle | NinjaTrader / Rithmic (via NT Brokerage) | **$12** | Required for live trading; pass-through, not Kinetick |
$ /usr/bin/grep -n -i kinetick .claude/agent-memory/praxis-auditor/audit_evidence_standards.md | cut -c1-300
152:Session 53's corpus-read report pasted `$ grep -rni "Kinetick\|Playback\|connection" docs/reference/2026-07-24-nt8-windows-reference.md`
```
34 = 29 pre-unit files + 5 written by this unit at that point. Later writes raise it: W6 measured 36 (`/usr/bin/grep`) / 31 (wrapper), after the fix-check file and the manager's memory file existed. The agent-memory hit is a methodology note, not a Kinetick fact. The `Redemtion/` files (mtime 2026-05-05) are folded into Q1/Q2. The earlier wrapper listing, kept as the record of what was first used:
```
$ grep -rilI kinetick --exclude-dir=.git . | sort        (wrapper — skips gitignored paths)
DECISION_LOG.md
docs/reference/2026-07-24-nt8-windows-reference.md
docs/reference/assets/nt8-2026-07-24/00-coworker-capture-notes.txt
docs/reports/2026-07-09-b1-0-nt8-parallels-validation.md
docs/reports/2026-07-12-b1f-t1-t4-vm-run-blocked.md
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md
docs/reports/2026-08-29-session52-nt8-voice-walkthrough-v2.md
docs/reports/2026-08-29-session52-nt8-voice-walkthrough.md
docs/reports/2026-08-29-session53-nqcont-resolution-and-rth-corpus-read.md
docs/reports/2026-08-29-session53-w1-q1-import-instructions.md
docs/reports/2026-08-29-session53-w4-adversarial-q4-designs.md
docs/reports/2026-09-29-vm-migration-concerns.md
docs/reports/2026-10-19-windows-vm-state-update-2-from-migration.md
docs/reports/2026-10-20-a20-adversarial-1.md
docs/reports/2026-10-20-a20-adversarial-2.md
docs/reports/2026-10-20-a20-adversarial-3.md
docs/reports/2026-10-20-a20-fusion-tz-kinetick-walkthrough.md
docs/reports/2026-10-20-a20-manager-report.md
docs/reports/2026-10-20-a20-results.md
docs/reports/2026-10-20-a20-voice-handoff.md
docs/reports/2026-10-20-seat-close-handover.md
docs/runbooks/2026-07-10-b1f-nt8-consumer-install.md
docs/specs/2026-07-15-block2-backtesting-scope-proposal.md
HANDOFF.md
STATUS.md
```
(Observer effect: this report and the four other unit files now also match. That listing was taken before any of them existed.)

**E2. Key citations re-read (verbatim; command: `sed -n <line>p <file>`, long lines cut with `cut -c1-700` or truncated as marked)**
```
== DECISIONS.md:184
- **Q4 data:** NT8 default-provider MINUTE history — no paid-data budget this block. Depth target ≥4 yrs NQ / ≥12 OOS windows (subject to what the default provider supplies; shortfall to be logged, not silently accepted).
== DECISION_LOG.md:424
- [2026-10-20T15:55:42Z] WHO: amear | WHAT: **Amear's rulings on the a20 results.** (1) **K5/K8: ACCEPT AS FOUND.** "Simulated Data Feed" connected (green) is recorded as what D-071's "Simulation" meant. Nothing touched. (2) **N1: ACCEPTED** on the spoken read. The punctuation (brackets, "&") stays unconfirmed. (3) **Kinetick EOD (K1): undecided.** Amear: "i dont know what that is or i dont remeber. look into it". (4) **Trend box screenshot: inside the VM.** | WHY: ...
== walkthrough:183
- This doesn't touch the NQCONT "unknown instrument" error. That's a separate defect, reported to reproduce on Fusion, and still open. Nothing here requests bars.
== B1-0 :82 :164
Data is real-time market data (via NinjaTrader's bundled Kinetick feed), not synthetic sim ticks. This is the same data feed that will be used with Rithmic in production — validating the full rendering pipeline.
- **Data feed was real-time Kinetick via the `amear238` NT login** (cached token), not the account-free Sim101 internal simulator described in the coworker brief. ...
== upd2 :67 (excerpt)
| 13 | Connections as before, nothing more | **One change, accepted.** After sign-in NT8 connected by itself to **"Simulation"**, NinjaTrader's demo server (US$50,000 pretend cash, delayed real prices). Amear accepted it on condition: no orders, no other connection (D-071). Still connected after the restore | ... Kinetick EOD: NOT YET KNOWN |
== mig :121
13. **Connections as before, and nothing more:** Simulated Data Feed; Kinetick EOD configured.
== results :21-22
Connections rows (name + dot colour, or no dot): Simulated Data Feed, green dot. Kinetick – End Of Day (Free), no dot. Playback, no dot. Simulation, no dot.
Kinetick - End Of Day row: present, no dot
```

**E3. Old install Config.xml (rescue copy; lines 1-14 hold account tokens and are deliberately not printed)**
```
-rw-r--r--@ 1 admin  staff  16879 Aug 29 12:00 /Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8/Config.xml
7a040a1106eb6c674b0cb17c70132cdfc6cf64453dcc8f564f63514feee0edf6  /Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8/Config.xml
-rw-r--r--@ 1 admin  staff  16879 Aug 29 12:00 /Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/Config.xml
7a040a1106eb6c674b0cb17c70132cdfc6cf64453dcc8f564f63514feee0edf6  /Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/Config.xml
32:    <KinetickOptions>
33-      <CanManageOrders>true</CanManageOrders>
34-      <ConnectOnStartup>false</ConnectOnStartup>
39:      <TypeName>NinjaTrader.Cbi.KinetickOptions</TypeName>
40-      <Mode>Live</Mode>
41:      <Name>Kinetick – End Of Day (Free)</Name>
42-      <Password />
43-      <Provider>Provider7</Provider>
50:    </KinetickOptions>
241:      <KinetickGlobexNonProFees>false</KinetickGlobexNonProFees>

$ sed -n '1,120p' Config.xml | grep -n -E 'Options>|ConnectOnStartup|<Name>|<Provider>'   (lines 15-65 shown)
15:  <ConnectOptions>
16:    <SimulatorOptions>
18:      <ConnectOnStartup>true</ConnectOnStartup>
25:      <Name>Simulated Data Feed</Name>
27:      <Provider>Simulator</Provider>
31:    </SimulatorOptions>
32:    <KinetickOptions>
34:      <ConnectOnStartup>false</ConnectOnStartup>
41:      <Name>Kinetick – End Of Day (Free)</Name>
43:      <Provider>Provider7</Provider>
50:    </KinetickOptions>
51:    <PlaybackOptions>
53:      <ConnectOnStartup>false</ConnectOnStartup>
60:      <Name>Playback Connection</Name>
62:      <Provider>Playback</Provider>
64:    </PlaybackOptions>
65:  </ConnectOptions>
```
(`:44 <User />`, `:47 <Free>true</Free>`, `:66 <Username>amear238</Username>`, `:109/:116 Preferred…Connection Unknown`, `:208 <MultiProvider>true` are from W1's pasted run, re-checked by adversary A's item 30.)

**E4. 2026-07-24 screenshot** (`docs/reference/assets/nt8-2026-07-24/20-connections-menu.png`, viewed by the manager this unit): menu rows "Kinetick – End Of Day (Free)", "Playback", "Simulated Data Feed" (green dot, "disconnect" link), "Simulation". No dot on Kinetick. Capture notes:
```
51:  Kinetick – End Of Day (Free)
53:  Simulated Data Feed   [green dot = currently connected]   -> "disconnect" link
```

**E5. Old NT8 logs (rescue `NinjaTrader 8-full/log`, 2026-08-15 → 08-29)**
```
$ cd ".../NinjaTrader 8-full" && /usr/bin/grep -c -i -a kinetick log/*.en.txt
log/log.20260815.00000.en.txt:0
log/log.20260815.00001.en.txt:0
log/log.20260816.00000.en.txt:0
log/log.20260817.00000.en.txt:0
log/log.20260818.00000.en.txt:0
log/log.20260828.00000.en.txt:0
log/log.20260829.00000.en.txt:0
log/log.20260829.00001.en.txt:0
$ /usr/bin/grep -h -a -E "Auto connecting|: Primary connection=Connected" log/*.en.txt | sort | uniq -c     (positive arm, same files; filter keeps only auto-connect and Connected lines)
   1 2026-08-15 10:12:01:190|1|4|Auto connecting 'Simulated Data Feed'...
   1 2026-08-15 10:12:01:476|1|2|Simulated Data Feed: Primary connection=Connected, Price feed=Connected
   1 2026-08-29 09:28:25:691|1|4|Auto connecting 'Simulated Data Feed'...
   1 2026-08-29 09:28:26:007|1|2|Simulated Data Feed: Primary connection=Connected, Price feed=Connected
   1 2026-08-29 11:02:45:337|1|4|Auto connecting 'Simulated Data Feed'...
   1 2026-08-29 11:02:45:633|1|2|Simulated Data Feed: Primary connection=Connected, Price feed=Connected
$ /usr/bin/grep -h -a -o "Historical Data Server: [a-z0-9.-]*" log/*.en.txt | wc -l
      26
```

**E6. Old NT8 traces — Kinetick mentions**
```
trace/trace.20260815.00000.txt:0
trace/trace.20260815.00001.txt:1
trace/trace.20260816.00000.txt:0
trace/trace.20260817.00000.txt:0
trace/trace.20260818.00000.txt:0
trace/trace.20260819.00000.txt:0
trace/trace.20260828.00000.txt:0
trace/trace.20260829.00000.txt:1
trace/trace.20260829.00001.txt:1
```
(Command: `/usr/bin/grep -c -i -a kinetick trace/*.txt`.) Line content, manager run:
```
$ /usr/bin/grep -n -a -i -o "subscription=Free licensedProviders=.\{0,140\}" trace/trace.20260815.00001.txt
23:subscription=Free licensedProviders='Playback Simulator NinjaTrader NinjaTrader Continuum NinjaTrader FXCM IQFeed E-Signal External FOREX.com Interactive Brokers Barchart.com K
```
(Cut at 140 characters by the pattern. The full line naming `Kinetick … Rithmic for NinjaTrader` is in W1's S11 and was re-run by the final check.)

**E7. Code dependency null, with positive control (R3)**
```
$ git ls-files | /usr/bin/grep -E '\.(cs|py|js|json|ts|sh|xml)$' | wc -l
      44
$ git ls-files | /usr/bin/grep -E '\.(cs|py|js|json|ts|sh|xml)$' | xargs /usr/bin/grep -l -i -E 'kinetick|kinetic|provider7' 2>/dev/null; echo "exit=$?"
exit=1
$ git ls-files | /usr/bin/grep -E '\.(cs|py|js|json|ts|sh|xml)$' | xargs /usr/bin/grep -l -i -E 'FileSystemWatcher|Rithmic' 2>/dev/null; echo "exit=$?"   (positive arm)
ninjascript/PraxisSignalConsumer.cs
scripts/praxis-signals-sweep.sh
exit=0
$ /usr/bin/grep -n -i -E 'BarsRequest|AddDataSeries|Connection|Provider' ninjascript/*.cs | head -20
(no output)
$ git ls-files | /usr/bin/grep -E '\.(cs|py|js|json|ts|sh|xml)$' | xargs /usr/bin/grep -l -i -w -E 'eod|end of day|data feed|datafeed|historical data|default provider'; echo "exit=$?"
exit=1
$ git ls-files | /usr/bin/grep -E '\.(cs|py|js|json|ts|sh|xml)$' | xargs /usr/bin/grep -l -i -w -E 'eod|end of day|data feed|datafeed|historical data|default provider|OnBarUpdate'; echo "exit=$?"     (positive arm)
ninjascript/PraxisNoiseAreaBreakout.cs
ninjascript/PraxisSignalConsumer.cs
exit=0
```
(All E7 runs used `/usr/bin/grep`, not the wrapper from N1, over the explicit `git ls-files` list.)
Adversary B independently re-ran W1's S2/S4/S5/S6/S8 nulls with positive arms: S4 code dirs (positive `OnBarUpdate|webhook` → 12 files), S5 (positive → 2), S6 (positive `provider` → `DECISIONS.md:4`), S8 logs (positive "Simulated Data Feed" 3/5/3) — see the adversary B file, "Survived" 1-5.

**E8. Rescue daily-bar store (adversary B's F2, re-run by the manager)**
```
$ ls -l -D %F_%T ".../NinjaTrader 8-full/db/day"/NQ*/*.ncd | awk '{print $6}' | sort | uniq -c
  49 2026-07-14_15:09:06
   1 2026-07-20_11:26:23
   1 2026-08-16_08:16:53
$ ... | awk '$6 !~ /2026-07-14/'
-rw-r--r--@ 1 admin  staff  1324 2026-07-20_11:26:23 .../db/day/NQ 09-26/2026.Last.ncd
-rw-r--r--@ 1 admin  staff  3388 2026-08-16_08:16:53 .../db/day/NQ 12-25/2025.Last.ncd
$ /usr/bin/grep -rlai kinetick ".../NinjaTrader 8-full/db"; echo "exit=$?"
exit=1
$ /usr/bin/grep -rlai -m1 'Last' ".../NinjaTrader 8-full/db" | head -2      (positive arm, same tree)
.../db/NinjaTrader.sqlite.bak_praxis
.../db/cache/US Equities RTH.SA Western Standard Time/MINUTE/NQCONT/Minute_1_1_Last_Close_Tick_BidAsk_Minute_1.Last.ntb
```
(File mtimes are VERIFIED. That they mark when NT8 wrote the bars, rather than a later copy, is INFERRED.)

**E9. Latent spec step, Block 2 daily inputs, 07-12 report (manager re-run)**
```
== acq spec :5 :16 :115
**Status:** Mac-side spec COMPLETE. Physical pull + validation is VM-GATED (see §5, §6).
| Contract form | **Continuous / front-month rolled** (see §2 roll convention) |
2. **Download the minute history.** NT8 → *Tools → Historical Data* (Data window) → *Download* tab → instrument `NQ` (continuous) → data type **Minute**, interval **1** → date range **2021-07-15 → 2026-07-14** → run. Default provider only (Q4 — no paid feed). ...
== wx7 184
- **E2 — build the series outside NT8, in Python.** The VM's NT8 install could **not natively construct** that roll convention ...
== 07-12 report, count of "startup"
0
== s52 264-266
6. **Is `<ROOT> ##-##` ever usable with imported data**, or is it strictly
   provider-served? Reference §6 says provider support is required — **confirm or
   refute that.**
== s53 407
### 6b. DEFECT FOUND in the existing Check A1 — the control is confounded
$ ls ~/praxis-signals/b2-data/raw | grep -c daily
22
```

**E10. Fusion-side config not reachable (W1's run)**
```
$ find ~ -maxdepth 6 -iname "Config.xml" -path "*inja*"
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8/Config.xml
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/Config.xml
$ mount | grep -i -E "vmware|hgfs|fusion"
exit=1
```

**E12. Was the May-2026 Kinetick quote-freshness monitor adopted?**
```
$ /usr/bin/grep -rn -i -E 'quote freshness|last-tick-age|Continuum' --exclude-dir=.git --exclude-dir=Redemtion . | cut -c1-260 | head
./docs/reports/2026-10-20-a20-kinetick-research-worker1.md:337:23:2026-08-15 10:11:52:447 Cbi.UserEntitlement.VerifyAsync.99: subscription=Free licensedProviders='Playback Simulator NinjaTrader NinjaTrader Continuum NinjaTrader FXCM IQFeed E-Signal External FO
./DECISIONS.md:208:**Context:** The VM coworker reports the locked roll convention — Vol/OI-crossover trigger + Difference back-adjustment (D-2026-07-15, b2-data §2) — is **not natively constructible** in the current NT8 install (NT8's built-in continuous cont
$ /usr/bin/grep -rl -i -E 'circuit breaker' docs/specs | head -3       (positive arm)
docs/specs/STRATEGY_HEALTH_MONITOR_SPEC.md
docs/specs/2026-07-24-bev-teaching-agent-design.md
```
Neither hit is the monitor: one is the licence trace quoted in W1, and `DECISIONS.md:208` is a roll-convention note whose line extends past the 260-character cut. Observer effect: a re-run now also matches this report and the W5/W6 files, which quote these terms. W6 re-ran a broader search (`quote freshness|last-tick-age|tick age|stale (data|quote|feed)|data feed (health|loss|stale)`) and found nothing outside `Redemtion/` and the unit files. No spec carries "quote freshness" or "last-tick-age".

**E11. Scope / staged set (manager, after W1)**
```
$ git diff --cached --name-only
DECISION_LOG.md
ISSUE_REGISTER.md
MANIFEST.md
docs/reports/2026-08-06-session42-r8j-phase3-import.md
docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
docs/reports/2026-08-07-session44-r8j-offset-correction-adversarial.md
docs/reports/2026-08-07-session44-r8j-offset-correction-worker1.md
docs/reports/2026-08-07-session44-r8j-offset-correction.md
docs/specs/2026-08-08-ledger-compaction-spec.md
$ /usr/bin/grep -c -F '<first 21 chars of the cached-username token>' docs/reports/2026-10-20-a20-kinetick-research-worker1.md
0
```
The staged set is identical to the session-start snapshot (9 paths, carried from earlier units; not touched here). Token string not present in the W1 report.

---

## S6 cross-block check

This unit proposes no deviation and changes nothing. Cross-block reading of the Kinetick question:
- **Block 1 (signal path):** no dependency (E7).
- **Block 2 (backtesting data):** no current dependency (inputs on disk, E9). One latent risk: the stale acquisition-spec step (Q3). That bears on **F3** only if a re-pull were made through a different provider, which is not proposed.
- **Block 3 (circuit breakers, F1/F2):** not touched. Kinetick EOD carries no live signal (UNVERIFIED product fact; no record of use).
- **Blocks 4–5 (paper/live via Rithmic, F4 MFFU):** no Rithmic connection is configured (E3), so there is no interaction today. A future Rithmic + Kinetick interplay is UNVERIFIED and would be a question for that block's own spec.
- **D-071 (Amear's migration condition):** options B and C would cross it *if* "no other connection" covers a hand-made data connection. That reading is INFERRED from its wording. Whether it does is Amear's to say (Q4, open question 2).

---

## Open questions for Amear

1. **Kinetick on Fusion (K1):** leave it as found (listed, no dot), or something else (connect when needed / at startup / remove)? Your call. Q4 has what each touches.
2. **Only if you want it connected:** does your D-071 condition, "no other connection", cover connecting Kinetick (by hand or at startup)? If it does, does it stand, or do you amend it? Any change needs a ledger entry first (S4/S5).

**For the master (housekeeping; not Amear's questions, not fixed here):** (a) `docs/specs/2026-07-15-b2-data-acquisition-spec.md` still reads COMPLETE, with a continuous-`NQ` download step that wx7 E2 superseded. (b) The session-52 walkthroughs' "native `NQ 12-25` … 2026-07-17" control chart cannot have bars for that date (C3). (c) B1-0 `:82`/`:164` "real-time Kinetick" is contested (C1). Each may warrant a bead.

---

## Files created in this unit (all untracked; nothing staged)

- `docs/reports/2026-10-20-a20-kinetick-research.md` — this report
- `docs/reports/2026-10-20-a20-kinetick-research-worker1.md` — W1 research
- `docs/reports/2026-10-20-a20-kinetick-research-adversarial-A.md` — W3
- `docs/reports/2026-10-20-a20-kinetick-research-adversarial-B.md` — W4
- `docs/reports/2026-10-20-a20-kinetick-research-final-check.md` — W5
- `docs/reports/2026-10-20-a20-kinetick-research-fix-check.md` — W6
- Adversary 1 (W2) wrote no file.
- Outside the repo: a read-only scratch copy of the rescue sqlite made by adversary B in the session scratchpad; the manager's draft of this report in the scratchpad. No ledger or spec was written. **One `.claude/` write, by the manager, outside the deliverable:** `.claude/agent-memory/praxis-manager/project_grep_wrapper_skips_ignored.md` (new) plus one index line appended to that directory's `MEMORY.md`. It records the N1 grep-wrapper lesson. It is the manager's own persistent memory (gitignored), not a ledger, and it contains the word Kinetick.

## Files staged

None by this unit.

## Final adversarial check

- **W5 (final report): VERDICT: BROKEN**, with N1–N6 folded in above.
- **W6 (N1–N6 fixes only): VERDICT: SURVIVES.** All six fixes are in the body and adequate. The fixes introduced 8 MINOR defects (F1–F8), all applied afterwards by the manager: licence-trace wording in summary line 2 (F1); the header's label scope (F2); `INSTRUCTIONS.md:94-95` (F3); the E12 observer-effect note (F4); the `.claude/` memory write disclosed (F5); the 2026-05-05/06 date (F6); C2 now cites the 07-24 origin (F7); "not carried into any spec" relabelled INFERRED (F8).
- **Not adversarially re-checked:** the eight F1–F8 edits themselves. They are wording and citation corrections, each the smallest fix W6 proposed. Disclosed so the auditor can target them.

## Result

**Result: PASS** — the manager's stress-test outcome under the report contract. **It is not an audit grade**, and per the brief it is not a rubric grade of this report: the master's auditor grades it. What it means: Q1–Q4 are answered to the level their evidence supports. Every adversarial MAJOR (A: 3, B: 2, W5: 2) was fixed, and the fixes survived W6. Every MINOR was applied. The staged set is unchanged. Residuals, disclosed: no vendor-checked Kinetick product facts (no web tool); Fusion's own Config.xml unread; F1–F8 edits not re-attacked; the first adversary returned no result.

## Post-audit correction (2026-10-20)

**Line convention.** `audited :N` means line N of this report as audited (sha256 `747b5084…`, 491 lines). The pointer line inserted after line 1 shifts every later line by +1, so each is cited as `audited :N (now :N+1)`. Line numbers of other files are those files' own.

**Labels** are as defined at audited :7 (now :8). Every VERIFIED in this section rests on a block pasted in this section. Each block starts with the `cd` it ran in and is labelled with who ran it.

### 1. Scope and what the audit found

This section corrects the report by append. No earlier line is changed. Where this section and an earlier line disagree, this section wins for the lines named in §2. The audit findings below are as recorded in the master's audit-FAIL row `DECISION_LOG.md:428` (16:40:32Z, an uncommitted worktree line: HEAD's DECISION_LOG has 59 lines, o4b; REPORTED), pasted as o7 below. That row itself names the root cause: "the master's question framing (corrected 16:36:23Z), carried in faithfully by the manager".
- **B1.** The report took in, unverified, the 15:55:42Z equivalence "Simulated Data Feed = what D-071's 'Simulation' meant" and built Q4, the PRAXIS view, the S6 block and open question 2 on it (the audit row names audited :85, :119, :136 and :455; Q4's other rows and open question 2 are added by this correction). The master withdrew that equivalence at 16:36:23Z. Amear restated D-071 at 16:37:30Z (§3).
- **B2.** Nulls relayed from workers or adversary B had no paste in the report (audited :106, :109, :370). Pasted now (§9).
- **M1** audited :427's observer-effect list is wrong. **M2** audited :15's "(searches VERIFIED, below)" says "below" for arms not pasted (`:428`). **M3** audited :14's "No old connection log mentions it" overstates: only the 08-15 → 08-29 logs survive. **M4** as recorded at `:428`: "E5 pastes only the count 26". §10 M4 pastes all 26 lines (o4a), and also corrects audited :108 and :146, which say "connected to" where the log lines say "Connection lost to" / "Connection restored to". All four: §10.
- **M5** (found during this correction): audited :28 cites S6 as `:113`. S6 is `specs/SPEC_RUBRIC.md:112`; `:113` is S7 (§10, M5).

**o7**. *Manager-run, 2026-10-20 ~13:10 EDT.*

```
$ cd "/Volumes/Sensidine/Praxis.build"
$ sed -n 428p DECISION_LOG.md | cut -c1-1700
- [2026-10-20T16:40:32Z] WHO: praxis-master | WHAT: **AUDIT FAIL: `2026-10-20-a20-kinetick-research.md`. This is STRIKE ONE on `Praxis_build-a20`.** The earlier 14:33Z no-verdict doesn't count, per R-A; audits A and B passed. **Blocking findings:** B1 (S2, S6): D-071 applied to the wrong connection. The report repeats the master's false Simulation = Simulated Data Feed equivalence (`:85`, `:119`, `:136` "under any reading", `:455`), which its own E2 paste contradicts. **Root cause: the master's question framing (corrected 16:36:23Z), carried in faithfully by the manager.** B2 (S1): the NQCONT-import null is labelled VERIFIED with no pasted output; adversary B's nulls are relayed as counts (E7 `:370`). **Minor findings:** M1, the F4 observer note names the W5 file wrongly; M2, summary line 3 says "below" for arms not pasted; M3, it doesn't say the old logs only survive from 08-15; M4, E5 pastes only the count 26. S8 and S9/R3 PASS; the auditor re-ran E7 and planted a positive control. | WHY: S7; SPEC_RUBRIC park rule `:240` (re-read this turn), "On the second audit FAIL for the same bead" → park, absolute | WHERE: the report and its 5 support files, untracked | WHEN: 2026-10-20 | HOW: **Re-dispatch to praxis-manager for a correction by APPEND.** Body untouched apart from one pointer line under the title. It must cite Amear's re-ruling (16:37:30Z: D-071 restated to Simulated Data Feed). **A second FAIL on a20 parks it; the master does not re-dispatch a third time** | STATE: dispatched — fix in progress
```

### 2. Supersession register

Every hit of `D-071|Simulation|:424|15:55` in the audited copy:

**o1**. *Manager-run, 2026-10-20 ~12:55 EDT (re-run of correction-worker-1's commands; identical output).*

```
$ cd "/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/6d0e9294-2389-48c6-9c19-27f79fa5cae6/scratchpad"
$ shasum -a 256 a20-original.md | cut -c1-16
747b5084a2c02c9a
$ /usr/bin/grep -n -i -E 'D-071|Simulation|:424|15:55' a20-original.md | cut -c1-200
4:**Brief:** answer Amear's "i dont know what that is or i dont remeber. look into it" (`DECISION_LOG.md:424`, uncommitted worktree line) about row K1 of the a20 results (`docs/reports/2026-10-20-a20-
14:2. **No setup entry, and no decision by you, is on file.** Your "undecided" today is the only ruling (REPORTED, `DECISION_LOG.md:424`). The master's migration plan carried it over as "configured" (
17:5. **Your own condition matters here.** When NinjaTrader connected itself on Fusion, you accepted it on condition "no orders, no other connection" (D-071). Connecting Kinetick, whether by hand or a
83:| 2026-10-19 | Migration update 2: Amear accepted NT8's self-connection "on condition: no orders, no other connection (D-071)"; "Kinetick EOD: NOT YET KNOWN" | `docs/reports/2026-10-19-windows-vm-s
85:| 2026-10-20 | **Amear:** K5/K8 accepted ("Simulated Data Feed" = what D-071's "Simulation" meant); "**Kinetick EOD (K1): undecided.**" — **the only Amear ruling on Kinetick** | `DECISION_LOG.md:42
119:- **D-071 (Amear):** NT8's self-connection accepted "on condition: no orders, no other connection" (update 2 `:67`, REPORTED), with the accepted connection pinned on 10-20 as the Simulated Data Fe
122:| Option | What it touches | D-071 / item 13 | Risk / what is known |
125:| **B. Connect by hand only when needed** | Connections menu; a network connection to Kinetick's servers | **Likely conflicts with D-071** "no other connection" (INFERRED from its wording). If Ame
126:| **C. Connect at startup** | `ConnectOnStartup` in Fusion's NT8 settings | **Likely conflicts with D-071** (same reading as B, INFERRED) **and departs from item 13** | Same as B, on every launch.
127:| **D. Remove the connection** | NT8's connection list | Not a connection, so D-071 is untouched; **departs from item 13** ("as before") | UNVERIFIED: whether it can be re-added easily. INFERRED: 
136:INFERRED, from Q3 and the constraints above. No search found anything in PRAXIS that needs Kinetick, and it has never been seen connected. **A** is the only option that changes nothing and sits in
151:  - B-F1 MAJOR: D-071 applied only to option C; B is also "another connection", and the PRAXIS view steered toward B. **Resolved:** D-071 and item 13 are now columns across all four options. The D
160:  - N4 MINOR: D-071's scope was treated as settled. **Resolved:** INFERRED labels at Q4 B/C, S6 and the PRAXIS view; open question 2 now asks first whether D-071 covers it.
249:== DECISION_LOG.md:424
250:- [2026-10-20T15:55:42Z] WHO: amear | WHAT: **Amear's rulings on the a20 results.** (1) **K5/K8: ACCEPT AS FOUND.** "Simulated Data Feed" connected (green) is recorded as what D-071's "Simulation"
257:| 13 | Connections as before, nothing more | **One change, accepted.** After sign-in NT8 connected by itself to **"Simulation"**, NinjaTrader's demo server (US$50,000 pretend cash, delayed real pr
261:Connections rows (name + dot colour, or no dot): Simulated Data Feed, green dot. Kinetick – End Of Day (Free), no dot. Playback, no dot. Simulation, no dot.
303:**E4. 2026-07-24 screenshot** (`docs/reference/assets/nt8-2026-07-24/20-connections-menu.png`, viewed by the manager this unit): menu rows "Kinetick – End Of Day (Free)", "Playback", "Simulated Da
455:- **D-071 (Amear's migration condition):** options B and C would cross it *if* "no other connection" covers a hand-made data connection. That reading is INFERRED from its wording. Whether it does 
462:2. **Only if you want it connected:** does your D-071 condition, "no other connection", cover connecting Kinetick (by hand or at startup)? If it does, does it stand, or do you amend it? Any change
```

| Audited line | Now line | Status | Replacement, or why it stands |
|---|---|---|---|
| :4 | :5 | STANDS | Its `DECISION_LOG.md:424` cite is for Amear's Kinetick question, which that row carries |
| :14 | :15 | SUPERSEDED in "No old connection log mentions it" (M3) | §10 M3. The rest of the line stands: `DECISION_LOG.md:427` still leaves K1 open ("Kinetick (K1) awaits the audit") |
| :15 | :16 | SUPERSEDED in "(searches VERIFIED, below)" (M2) | §10 M2 |
| :17 | :18 | SUPERSEDED (summary line 5) | §7, replacement for summary line 5, on the restated D-071 |
| :28 | :29 | SUPERSEDED in "**S6** (`:113`" (M5) | S6 is `:112` (§10 M5) |
| :40 | :41 | STANDS | Supplemented by §4 (C4): none of the three blocks is a "Simulation" connection |
| :83 | :84 | STANDS | Accurate history of what update 2 `:67` says |
| :85 | :86 | SUPERSEDED in its parenthetical only | The equivalence was withdrawn at 16:36:23Z and replaced at 16:37:30Z (§3 vi–vii). "The only Amear ruling on Kinetick" still holds: `:427` says "Kinetick (K1) awaits the audit" |
| :106 | :107 | STANDS (finding) | Its VERIFIED label now rests on manager-run pastes o3a, o3b (§9) |
| :108 | :109 | SUPERSEDED in "**connected to**" (M4) | §10 M4 gives the exact log wording |
| :109 | :110 | STANDS (finding); "not re-run by manager" SUPERSEDED | Now manager-run, o3e (§9) |
| :119 | :120 | SUPERSEDED | §3. The "pin" it cites (`:424`) was withdrawn; D-071 now reads as restated at `:427` |
| :122 | :123 | STANDS | Table header only |
| :124 | :125 | SUPERSEDED | §5 row A |
| :125 | :126 | SUPERSEDED | §5, Q4 restated, row B |
| :126 | :127 | SUPERSEDED | §5, row C |
| :127 | :128 | SUPERSEDED | §5, row D |
| :136 | :137 | SUPERSEDED | §6. "Under any reading" is withdrawn |
| :146 | :147 | SUPERSEDED in the quoted "connected to (VERIFIED)" (M4) | §10 M4 |
| :151 | :152 | STANDS as history of adversary B's F1 | F1's premise (`adversarial-B.md:14`, `:22`: the 15:55:42Z "pin") is superseded (§3 v) |
| :160 | :161 | STANDS as history | The "Resolved" it records is overtaken by §5–§8 |
| :249 | :250 | STANDS | Header of a pasted block |
| :250 | :251 | STANDS as pasted evidence of what row `:424` says | Its content is superseded by rows `:426` and `:427` (§3) |
| :257 | :258 | STANDS | Already shows "Simulation" is the demo server, not the Simulated Data Feed |
| :261 | :262 | STANDS | Already shows the two as separate rows |
| :303 | :304 | STANDS | Already shows the two as separate rows on 07-24 |
| :327-328 | :328-329 | STANDS (pasted) | Supplemented by §10 M4: the 26 lines are 13 "lost" + 13 "restored" |
| :370 | :371 | STANDS as relay | Supplemented by o3c (§9): `DECISIONS.md:4` there is a `-c` count of 4 lines, not a line cite |
| :427 | :428 | SUPERSEDED in its observer-effect sentence (M1) | §10 M1 |
| :455 | :456 | SUPERSEDED | §8, corrected S6 entry |
| :462 | :463 | SUPERSEDED | §7, open question 2 restated |

### 3. B1. D-071: what it named, then and now

Quotes are from blocks o6 and o2a (migration repo, `~/Windows-migration`) and o2b (this repo), pasted below. The quoted text is VERIFIED as what each file says. What the rows record is REPORTED.

- **(0) 2026-10-16, migration in-VM brief, hard rule 1** (`~/Windows-migration/docs/briefs/2026-10-16-in-vm-agent-nt8-faithful-restore.md:20`; committed: porcelain empty, last commit `0888f0f`; o6): "**Simulation only.** No broker connection, no Rithmic, no new connection of any kind, no orders, not even on Sim101. The only connection allowed is "Simulated Data Feed"." `:69` and `:94` repeat it (""Simulated Data Feed" may connect by itself: that is the old setting and is allowed. Any other connection: rule 1."). REPORTED (outside-repo record, committed). INFERRED: the heading "Simulation only" uses the word in the generic sim-only sense, a third use of "Simulation" in the record, beside the demo-server connection and the 15:55:42Z reading of it as the Simulated Data Feed.
- **(i) 2026-10-19T14:05Z, migration ledger D-071** (`~/Windows-migration/DECISION_LOG.md:124`; committed: porcelain empty, `cmp` exit 0 against HEAD, `git log -S` → `dd076ef`; o2a). It accepted "the auto-connected "Simulation" connection", "NinjaTrader's own demo server", relaxing hard rule 1 "for this one connection only". Conditions: "no orders of any kind"; "no other connection (no broker, no Rithmic)"; "the Part 4 test chart still runs on "Simulated Data Feed""; "Part 6 rechecks what connects at start-up after Part 5 swaps in the old `Config.xml`". The same day's in-VM brief (`~/Windows-migration/docs/briefs/2026-10-19-in-vm-nt8-finish-and-usb.md:15`) says: "Allowed connections: "Simulated Data Feed" and "Simulation" only. No broker, no Rithmic, nothing else." (`:65` repeats "both allowed"). The walkthrough log (`~/Windows-migration/docs/reports/2026-10-19-walkthrough-log.md`) has D-071 at 14:05Z (`:11`) and "Simulation connected" at 16:03Z after the restore (`:20`). All REPORTED (outside-repo records, committed). So on the migration-side record the 10-19 allowance was the Simulated Data Feed (rule 1, (0)) plus "Simulation" (D-071) (REPORTED as what the records say; reading the relaxation as "plus" is INFERRED from rule 1 and "relaxed for this one connection only").
- **(ii) Update 2 `:67`** relayed it to PRAXIS as "Simulation" with "no orders, no other connection (D-071)". The parenthetical "(no broker, no Rithmic)" and the Simulated Data Feed clause were dropped (o2b).
- **(iii)** The a20 walkthrough (`:74`, K5 "A dot on any row other than "Simulation"") and the a20 results (`:46`, "That is a row other than "Simulation"") kept the two connections apart. But they stated D-071 as accepting only "Simulation" (results `:46`: "D-071 accepted only "Simulation" connected"; walkthrough `:74`: "A connection beyond the one Amear accepted (P9, D-071)"). The walkthrough's P9 row (`:31`) cites "REPORTED (update 2 `:67`, D-071)" (o9); that results `:46` followed the same relay, which named only "Simulation" (ii), is INFERRED (o2b). Against the migration-side record ((0), (i)), K5 firing on the Simulated Data Feed was not outside the 10-19 allowance (INFERRED). This is a second layer of the framing problem (§4, C4).
- **(iv) 2026-10-20T15:55:42Z, ruling (1)** (`DECISION_LOG.md:424`): ""Simulated Data Feed" connected (green) is recorded as what D-071's "Simulation" meant." It rested on the master's option text, which made the two the same (o2b).
- **(v)** The audited report took that in at audited :85 (now :86) and :119 (now :120), both citing `:424`, and built on it at :136 (now :137) and :455 (now :456). Adversary B carried it too: `adversarial-B.md:14` ("Amear's 15:55:42Z ruling pins the one accepted connection as the Simulated Data Feed") and `:22` ("as clarified by DECISION_LOG :424") (o1, o2b).
- **(vi) 16:36:23Z, master correction** (`DECISION_LOG.md:426`): "The master's own question was wrong." … "So Amear's "accept as found" was given on a false premise the master supplied." (o2b).
- **(vii) 16:37:30Z, Amear** (`DECISION_LOG.md:427`): "K5/K8 RE-RULED on the corrected framing: KEEP AS FOUND." … "D-071 is restated by Amear: the Simulated Data Feed is the one allowed connection. No orders, no other connection." … "This supersedes ruling (1) of the 15:55:42Z row" (o2b).

**Where it stands now.** The original regime was the Simulated Data Feed (10-16 rule 1, (0)) plus "Simulation", the demo server (D-071, which itself accepted only "Simulation"; its Part 4 clause names the Simulated Data Feed as the test chart's feed) (REPORTED; the "plus" is INFERRED, (i)). The restated D-071 (10-20, `:427`) says "the Simulated Data Feed is the one allowed connection" (REPORTED). The restatement supersedes ruling (1) (REPORTED). It narrows the 10-19 allowance by dropping "Simulation", and its wording matches the 10-16 rule 1 ("The only connection allowed is "Simulated Data Feed"") (both INFERRED from the wording). Every PRAXIS `DECISION_LOG.md` row cited here (`:424`, `:426`, `:427`) is an uncommitted worktree line: HEAD has 0 of the three timestamps (o2b).

**Root cause.** Per the master's 16:36:23Z row, the cause was the master's option text ("WHY: S2 … without checking the cited source", REPORTED). The manager then carried it into this report without checking it (S2), although E2 (audited :257, :261) and E4 (audited :303) already showed the two connections are distinct (o1 shows those lines).

**o2a**. *Manager-run, 2026-10-20 ~12:55 EDT (re-run of correction-worker-1's commands; identical output).*

```
$ cd "/Users/admin/Windows-migration"
$ git status --porcelain DECISION_LOG.md; echo "porcelain exit=$?"
porcelain exit=0
$ git show HEAD:DECISION_LOG.md | sed -n 124p | cmp - <(sed -n 124p DECISION_LOG.md); echo "cmp exit=$?"
cmp exit=0
$ git log --format='%h %ad' -S '2026-10-19T14:05:00Z] **D-071**' -- DECISION_LOG.md
dd076ef Mon Oct 19 16:54:02 2026 -0400
$ sed -n 124p DECISION_LOG.md | sed 's/DEMO[0-9]*/DEMO…/'
- [2026-10-19T14:05:00Z] **D-071** WHO: Amear (decided: "thats fine allow it"), walkthrough guide (recorded it; pure doc edit) | WHAT: **Option (a): the auto-connected "Simulation" connection is accepted.** Hard rule 1 of the 10-16 NT8 brief is relaxed for this one connection only: NinjaTrader's own demo server (account DEMO…, US$50,000 pretend cash, delayed real prices). Conditions: no orders of any kind (including Chart Trader's Buy Mkt / Sell Mkt in the default workspace); no other connection (no broker, no Rithmic); the Part 4 test chart still runs on "Simulated Data Feed"; Part 6 rechecks what connects at start-up after Part 5 swaps in the old `Config.xml` | WHY: it is NinjaTrader's demo server with no real money, no orders were placed, and rule 1 was there to keep brokers and Rithmic out; option (b) would need a NinjaTrader settings change, which rule 6 forbids | WHERE: `docs/briefs/2026-10-19-amear-walkthrough-handoff.md` step 3; `docs/briefs/2026-10-16-in-vm-agent-nt8-faithful-restore.md` hard rules 1 and 6; `06_Validation/nt8-restore-report-2026-10-19-partial.txt`; D-070; bead wm-ckj | WHEN: 2026-10-19T14:05:00Z | HOW: walkthrough continues with the 10-16 brief from Part 3 step 4; hard rules 2-8 unchanged | STATE: closed
$ git status --porcelain docs/briefs/2026-10-19-in-vm-nt8-finish-and-usb.md docs/reports/2026-10-19-walkthrough-log.md; echo "porcelain exit=$?"
porcelain exit=0
$ /usr/bin/grep -n '' docs/briefs/2026-10-19-in-vm-nt8-finish-and-usb.md | sed -n '15p;65p'
15:1. **No orders, ever,** on any account. The default workspace has Chart Trader with Buy Mkt / Sell Mkt buttons: remind Amear once not to touch them. Allowed connections: "Simulated Data Feed" and "Simulation" only. No broker, no Rithmic, nothing else. If anything else connects or asks to: Amear disconnects it; stop and report.
65:1. **Amear:** start NinjaTrader 8 and sign in if asked. With the old `Config.xml`, "Simulated Data Feed" and/or "Simulation" may connect by itself: both allowed. **Any other connection: rule 1.** Read the Connections menu / status and record exactly what connected.
$ /usr/bin/grep -n '' docs/reports/2026-10-19-walkthrough-log.md | sed -n '11p;20p' | cut -c1-260
11:- 14:05Z · Step 3 (Simulation decision) · Amear: "thats fine allow it". Option (a) recorded as D-071: Simulation accepted on condition of no orders and no other connection.
20:- 16:03Z · NT8 by hand · Amear stopped the VM agent and finished by hand: Documents\NinjaTrader 8 has 6,287 files / 485 folders; NT starts, Simulation connected, old charts and windows opened (S2 looks met). Historical Data lists NQCONT Minute Last 2021-03.
```

**o2b**. *Manager-run, 2026-10-20 ~12:55 EDT (re-run of correction-worker-1's commands; identical output).*

```
$ cd "/Volumes/Sensidine/Praxis.build"
$ git show HEAD:DECISION_LOG.md | /usr/bin/grep -c -E '15:55:42Z|16:36:23Z|16:37:30Z'
0
$ sed -n 424p DECISION_LOG.md | cut -c1-247
- [2026-10-20T15:55:42Z] WHO: amear | WHAT: **Amear's rulings on the a20 results.** (1) **K5/K8: ACCEPT AS FOUND.** "Simulated Data Feed" connected (green) is recorded as what D-071's "Simulation" meant. Nothing touched. (2) **N1: ACCEPTED** on th
$ sed -n 426p DECISION_LOG.md
- [2026-10-20T16:36:23Z] WHO: praxis-master | WHAT: **CORRECTION BY APPEND to the 15:55:42Z row, ruling (1). The master's own question was wrong.** The K5/K8 option offered to Amear read "Record that Simulated Data Feed is what was meant by 'Simulation' in D-071". The record contradicts that equivalence. Update 2 `:67` (re-read by the master this turn) describes "Simulation" as "NinjaTrader's demo server (US$50,000 pretend cash, delayed real prices)". That is a distinct row in the Connections list, and Amear's reads show it with **no dot**. The **Simulated Data Feed** is a separate connection. In the old install's Config.xml it has `ConnectOnStartup` `true` (`:18`, VERIFIED earlier this session by the a20 audit and manager). **So Amear's "accept as found" was given on a false premise the master supplied.** The facts stand: nothing was touched, both rows are simulation-only, and no orders were placed. The ruling must be re-asked with the correct framing | WHY: S2 (the master stated an interpretation as the option text, without checking the cited source) | WHERE: rows 15:55:42Z, `a20-results.md` | WHEN: 2026-10-20 | HOW: `sed -n 67p` on update 2 | STATE: open — K5/K8 to be re-ruled by Amear
$ sed -n 427p DECISION_LOG.md
- [2026-10-20T16:37:30Z] WHO: amear | WHAT: **K5/K8 RE-RULED on the corrected framing: KEEP AS FOUND.** Simulated Data Feed is connected and Simulation (the demo server) is not. **D-071 is restated by Amear: the Simulated Data Feed is the one allowed connection. No orders, no other connection.** This supersedes ruling (1) of the 15:55:42Z row, which rested on the master's false equivalence (corrected 16:36:23Z). Nothing touched | WHY: a20 K5/K8 mismatch, "every mismatch is your decision" | WHERE: D-071; `a20-results.md` | WHEN: 2026-10-20 | HOW: AskUserQuestion, with the option text naming both connections separately | STATE: closed — K5/K8 settled. Kinetick (K1) awaits the audit of `2026-10-20-a20-kinetick-research.md`
$ /usr/bin/grep -n '' docs/reports/2026-10-19-windows-vm-state-update-2-from-migration.md | sed -n '64p;67p'
64:| 8–10 | NinjaScript from the repo, hash-verified; Compile; consumer on `Sim101` | **Not started.** PRAXIS's work | `bin` (327 files) was left out of the faithful set on purpose, per your item 8 (D-068) |
67:| 13 | Connections as before, nothing more | **One change, accepted.** After sign-in NT8 connected by itself to **"Simulation"**, NinjaTrader's demo server (US$50,000 pretend cash, delayed real prices). Amear accepted it on condition: no orders, no other connection (D-071). Still connected after the restore | REPORTED (in-VM agent 13:43Z; Amear 16:03Z). "Simulation" was in the old install's list (your 5.2 item 13). No broker or Rithmic added (REPORTED; every brief forbade it). Kinetick EOD: NOT YET KNOWN |
$ /usr/bin/grep -n '' docs/reports/2026-10-20-a20-results.md | sed -n '21p;46p'
21:Connections rows (name + dot colour, or no dot): Simulated Data Feed, green dot. Kinetick – End Of Day (Free), no dot. Playback, no dot. Simulation, no dot.
46:| K | **K5 FIRED** | **Simulated Data Feed has a green dot.** That is a row other than "Simulation" | Report it. **Don't disconnect.** Amear decides. D-071 accepted only "Simulation" connected |
$ /usr/bin/grep -n '' docs/reports/2026-10-20-a20-fusion-tz-kinetick-walkthrough.md | sed -n '74p'
74:| K5. A dot on any row other than "Simulation" | A connection beyond the one Amear accepted (P9, D-071). On the old Parallels install, `Config.xml:18` reads `ConnectOnStartup` `true` for 'Simulated Data Feed' (name at `:25`; VERIFIED, old install only). That this connects it at startup is INFERRED. Whether a dot here is acceptable is Amear's call (D-071 says no other connection) | Report it. **Don't disconnect.** Amear decides |
$ /usr/bin/grep -n '' docs/reference/assets/nt8-2026-07-24/00-coworker-capture-notes.txt | sed -n '50,55p'
50:Connections menu (top to bottom, as expanded):
51:  Kinetick – End Of Day (Free)
52:  Playback
53:  Simulated Data Feed   [green dot = currently connected]   -> "disconnect" link
54:  Simulation                                                 -> "configure" link
55:(Did not click disconnect or configure — layout capture only, per task constraints.)
$ /usr/bin/grep -n '' docs/reference/2026-07-24-nt8-windows-reference.md | sed -n '33p'
33:- **Connections menu** ([`20-connections-menu.png`](assets/nt8-2026-07-24/20-connections-menu.png)): Kinetick – End Of Day (Free) · Playback · Simulated Data Feed *(green = connected, "disconnect" link)* · Simulation *("configure" link)*.
$ /usr/bin/grep -n '' docs/reports/2026-09-29-vm-migration-concerns.md | sed -n '111p;116p;118p;121,122p'
111:8. **PRAXIS NinjaScript deployed from the repo, hash-verified by whoever has hands on the VM, not pasted.**
116:9. **Compile with the toolbar button.** Evidence is a fresh modified time on `NT8\bin\Custom\NinjaTrader.Custom.dll`.
118:10. **Consumer starts on `Sim101`** against the new `SignalsPath` and moves one test JSON into `processed\`. Then re-run the C4 latency test.
121:13. **Connections as before, and nothing more:** Simulated Data Feed; Kinetick EOD configured.
122:    VERIFIED: no Rithmic connection exists on the old install (reference `:33` lists Kinetick, Playback, Simulated Data Feed, Simulation). **Do not add one during the migration.**
$ /usr/bin/grep -n '' docs/reports/2026-10-20-a20-kinetick-research-adversarial-B.md | sed -n '14p;22p' | cut -c1-400
14:- **Defect:** D-071 forbids *any* other connection, however brief. Amear's 15:55:42Z ruling pins the one accepted connection as the Simulated Data Feed. Connecting Kinetick by hand (B) is "another connection" just as much as C is. Only A complies outright. D is not a connection, but it breaks the master's "Connections as before, and nothing more" principle (item 13), which the artifact cites fo
22:- **Smallest fix:** add to row B: "Conflicts with D-071 'no other connection' (update 2 :67, as clarified by DECISION_LOG :424). Needs Amear to lift or amend D-071 first." Add the item-13 principle to row D. In :116, replace "B is the reversible way to try" with "B would first need D-071 amended. That is Amear's call."
```

**o6**. *Manager-run, 2026-10-20 ~13:10 EDT.*

```
$ cd "/Users/admin/Windows-migration"
$ git status --porcelain docs/briefs/2026-10-16-in-vm-agent-nt8-faithful-restore.md; echo "porcelain exit=$?"
porcelain exit=0
$ git log -1 --format='%h %ad' -- docs/briefs/2026-10-16-in-vm-agent-nt8-faithful-restore.md
0888f0f Fri Oct 16 12:06:47 2026 -0400
$ /usr/bin/grep -n '' docs/briefs/2026-10-16-in-vm-agent-nt8-faithful-restore.md | sed -n '18p;20p;69p;94p'
18:## Hard rules
20:1. **Simulation only.** No broker connection, no Rithmic, no new connection of any kind, no orders, not even on Sim101. The only connection allowed is "Simulated Data Feed". If anything else connects or asks to, Amear disconnects it; stop and report.
69:1. Connections: only "Simulated Data Feed" may be connected. If it is not, **Amear** connects it from the Connections menu.
94:1. **Amear** starts NinjaTrader 8 from the Start menu and signs in if asked. "Simulated Data Feed" may connect by itself: that is the old setting and is allowed. Any other connection: rule 1.
```

### 4. C4 (new contradiction): "Simulation" is not the Simulated Data Feed

- **Two distinct rows.** The 10-20 read lists "Simulated Data Feed, green dot" and, separately, "Simulation, no dot" (results `:21`). The 07-24 capture has "Simulated Data Feed [green dot …] -> "disconnect" link" and "Simulation -> "configure" link" (capture notes `:53-54`; reference `:33`). VERIFIED as file text (o2b).
- **Old install's Config.xml** (rescue copy, sha256 `7a040a11…`, 272 lines; o2c). `ConnectOptions` (`:15-65`) holds three blocks: `SimulatorOptions` named "Simulated Data Feed" (`:25`) with `ConnectOnStartup` `true` (`:18`); `KinetickOptions`; `PlaybackOptions` named "Playback Connection". There is no "Simulation" connection block. "Simulation" appears in lines 15 onward only three times, all non-connection fields: `:183` `IsGlobalSimulationMode` `true`, `:188` `SimulationColorSerialize`, `:191` `StartInGlobalSimulationMode` `false`. Lines 1–14: count 0, case-sensitive and `-i` (count only, nothing printed). VERIFIED for the file's contents (o2c).
- **Where Fusion's "Simulation" entry comes from: UNVERIFIED.** It is not stored as a `ConnectOptions` block in this file. The 07-24 menu showed it with a "configure" link (o2b).
- Update 2's ""Simulation" was in the old install's list (your 5.2 item 13)" refers to the **menu list** (migration concerns `:122` → reference `:33`), not to Config.xml (o2b).
- **A second layer of the framing problem.** Besides the false equivalence (§3 iv–vi), the a20 walkthrough `:74` and results `:46` text framed K5 as a connection beyond what D-071 accepted ("D-071 accepted only "Simulation" connected"). On the migration-side record the Simulated Data Feed was already allowed on 10-19 (10-16 rule 1, o6; D-071's Part 4 clause and the 10-19 brief `:15`/`:65`, o2a). So K5 firing on it was not outside the 10-19 allowance (INFERRED). The walkthrough's P9 row (`:31`) cites "REPORTED (update 2 `:67`, D-071)" (o9); that results `:46` followed the same relay, which named only "Simulation", is INFERRED (o2b; §3 ii, iii).
- **INFERRED, not asserted.** The D-071 row's Part 5 swap of the old `Config.xml` and Part 6 recheck were a PLAN (o2a). That the faithful restore from `NinjaTrader 8-full` happened is REPORTED (update 2 `:25`; `:62` is the restore-choice row, cited at audited :116, now :117; `:70`: whether the fresh install's files were moved aside first is "Not recorded" (o9)). The old Config.xml's only `ConnectOnStartup` `true` is the Simulated Data Feed (`:18`, o2c). That fits the 10-20 read ("Simulated Data Feed, green dot … Simulation, no dot"). It does not by itself explain the 10-19 post-restore "Simulation connected" (walkthrough log `:20`; update 2 `:67` "Still connected after the restore"). What actually changed between the two reads is UNVERIFIED.

**o9**. *Manager-run, 2026-10-20 ~13:20 EDT.*

```
$ cd "/Volumes/Sensidine/Praxis.build"
$ /usr/bin/grep -n '' docs/reports/2026-10-19-windows-vm-state-update-2-from-migration.md | sed -n '25p;62p;70p' | cut -c1-700
25:**NinjaTrader 8.1.7.2 is installed and restored by route (a), faithful** (D-068).
62:| 6 | Restore choice | **(a) Faithful**, Amear's call, 2026-10-16 15:52Z | D-068. Source: the unfiltered 09-29 copy `NinjaTrader 8-full/`, 5,444 files, 55,593,912 B, on disc NT8_TRANSFER, 5,445/5,445 hashes VERIFIED on the Mac and REPORTED 0 bad inside the VM |
70:**How the restore finished (REPORTED, walkthrough log 16:03Z–16:04Z).** The in-VM agent stopped at the "Simulation" connection. Amear finished by hand. Not recorded: whether the fresh install's files were moved aside first, the brief's whole-set manifest check (expected 5,444, 0 bad) and the read-only counts. INFERRED: 6,287 files is more than the 5,444 restored, because NT8 has run since and the installer had made 417 files. So the whole folder is **not** byte-proven against the 09-29 copy. Only `db\minute\NQCONT` is.
$ /usr/bin/grep -n '' docs/reports/2026-10-20-a20-fusion-tz-kinetick-walkthrough.md | sed -n '31p' | cut -c1-400
31:| P9 | Fusion connections: NinjaTrader connected itself to **"Simulation"**, and Amear accepted that on condition: no orders, no other connection | REPORTED (update 2 `:67`, D-071). Kinetick EOD on Fusion: **NOT YET KNOWN**. **Step 10 observes it** |
```

**o2c**. *Manager-run, 2026-10-20 ~12:55 EDT (re-run of correction-worker-1's commands; identical output).* The source files are Windows text: the trailing CR bytes of their lines were dropped when this section was edited; otherwise identical (the manager's check is pasted at the end of this section).

```
$ cd "/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full"
$ shasum -a 256 Config.xml | cut -c1-16; wc -l < Config.xml
7a040a1106eb6c67
     272
$ awk 'NR>=15 && NR<=65 && /Options>|<Name>|ConnectOnStartup/ {print NR": "$0}' Config.xml
15:   <ConnectOptions>
16:     <SimulatorOptions>
18:       <ConnectOnStartup>true</ConnectOnStartup>
25:       <Name>Simulated Data Feed</Name>
31:     </SimulatorOptions>
32:     <KinetickOptions>
34:       <ConnectOnStartup>false</ConnectOnStartup>
41:       <Name>Kinetick – End Of Day (Free)</Name>
50:     </KinetickOptions>
51:     <PlaybackOptions>
53:       <ConnectOnStartup>false</ConnectOnStartup>
60:       <Name>Playback Connection</Name>
64:     </PlaybackOptions>
65:   </ConnectOptions>
$ awk 'NR>=15 && /Simulation/ {c++; print NR": "$0} END {print "case-sensitive count (lines>=15)="c+0}' Config.xml
183:       <IsGlobalSimulationMode>true</IsGlobalSimulationMode>
188:       <SimulationColorSerialize>&lt;SolidColorBrush xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"&gt;#00FFFFFF&lt;/SolidColorBrush&gt;</SimulationColorSerialize>
191:       <StartInGlobalSimulationMode>false</StartInGlobalSimulationMode>
case-sensitive count (lines>=15)=3
$ awk 'NR>=15 && tolower($0) ~ /simulation/ {c++; print NR": "$0} END {print "case-insensitive count (lines>=15)="c+0}' Config.xml
183:       <IsGlobalSimulationMode>true</IsGlobalSimulationMode>
188:       <SimulationColorSerialize>&lt;SolidColorBrush xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"&gt;#00FFFFFF&lt;/SolidColorBrush&gt;</SimulationColorSerialize>
191:       <StartInGlobalSimulationMode>false</StartInGlobalSimulationMode>
case-insensitive count (lines>=15)=3
$ head -14 Config.xml | /usr/bin/grep -c 'Simulation'
0
$ head -14 Config.xml | /usr/bin/grep -c -i 'simulation'
0
$ awk 'NR>=15 && /<Provider>|ConnectOptions>/ {print NR": "$0}' Config.xml
15:   <ConnectOptions>
27:       <Provider>Simulator</Provider>
43:       <Provider>Provider7</Provider>
62:       <Provider>Playback</Provider>
65:   </ConnectOptions>
$ awk 'NR==33 || NR==44 || NR==47 || NR==52 || NR==66 || NR==109 || NR==116 || NR==208 {print NR": "$0}' Config.xml
33:       <CanManageOrders>true</CanManageOrders>
44:       <User />
47:       <Free>true</Free>
52:       <CanManageOrders>true</CanManageOrders>
66:   <Username>amear238</Username>
109:       <PreferredFutureConnection>Unknown</PreferredFutureConnection>
116:       <PreferredRealtimeFutureConnection>Unknown</PreferredRealtimeFutureConnection>
208:       <MultiProvider>true</MultiProvider>
```

### 5. Q4 restated against the restated D-071

Supersedes audited :124-127 (now :125-128). The restated words are REPORTED (`DECISION_LOG.md:427`, o2b). Applying them to a Kinetick end-of-day connection is INFERRED. Whether Amear meant them to cover a data-only connection is his to say.

| Option | What it touches | Restated D-071 (16:37:30Z): "the Simulated Data Feed is the one allowed connection. No orders, no other connection." | Original D-071 (10-19): "no other connection (no broker, no Rithmic)" | Item 13: "Connections as before, and nothing more" |
|---|---|---|---|---|
| **A** | Nothing. No second connection | Consistent with the plain words (INFERRED). Amear ruled the neighbouring found state KEEP AS FOUND (REPORTED, `:427`) | Consistent: nothing added (INFERRED) | As before (INFERRED) |
| **B** | Connections menu; a second connection besides the Simulated Data Feed, by hand | Conflicts with "the one allowed connection" on the plain words (INFERRED) | Kinetick is neither broker nor Rithmic. Whether D-071's own parenthetical was the scope of "no other connection" or only examples cannot be settled here. The same-day brief reads "No broker, no Rithmic, nothing else" (`:15`) and "Any other connection: rule 1" (`:65`), and the 10-16 rule 1 reads "no new connection of any kind" (REPORTED, o2a, o6). INFERRED: these lean toward the full scope; still Amear's to say | Adds a connection that was not connected before (INFERRED); whether that is "more" is Amear's reading |
| **C** | As B, on every launch, plus `ConnectOnStartup` in Fusion's NT8 settings (a settings change) | As B (INFERRED) | As B; plus a settings change (see the rule-6 note below) | Departs from item 13 (as audited :126, now :127) |
| **D** | Removes the entry from NT8's connection list. Adds no connection | Not crossed on its words (INFERRED) | Not crossed on its words (INFERRED); it is a settings change (see the rule-6 note) | Departs from item 13 (as audited :127, now :128) |

**Rule-6 note (REPORTED, o2a).** The original D-071's WHY says option (b) "would need a NinjaTrader settings change, which rule 6 forbids" (rule 6 of the 10-16 migration brief). Whether that migration rule still binds now is unread (UNVERIFIED). If it does, it bears on C and D.

### 6. PRAXIS view restated (reasoning only, not a decision)

Supersedes audited :136 (now :137). The lean toward **A** still holds. Reasons, all INFERRED:
- Q3's no-dependency finding is unchanged, and its searches are now pasted (B2, §9).
- A and D both leave the Simulated Data Feed as the sole connection, which matches the restated D-071 on its plain words. A is the only one of them that changes nothing (D is a settings change and departs from item 13).
- B and C, if the restated D-071 covers a data-only connection, would need Amear to amend it first.

"Under any reading" (audited :136) is **WITHDRAWN**. A's fit rested there on a false equivalence; it now rests on the restated wording. K1 remains Amear's (`DECISION_LOG.md:427`: "Kinetick (K1) awaits the audit"). **Amear decides.**

### 7. Open question 2 and summary line 5, restated

**Open question 2** (supersedes audited :462, now :463):

> 2. **Only if you want Kinetick connected:** your restated D-071 (16:37:30Z) makes the Simulated Data Feed "the one allowed connection". Does that cover connecting Kinetick, by hand or at startup? If it does, it would need amending first, with a ledger entry (S4/S5).

**Summary line 5** (supersedes audited :17, now :18):

> 5. **Your own condition matters here.** On 10-19 the Simulated Data Feed was already allowed (the 10-16 migration brief, rule 1), and you also accepted NinjaTrader connecting itself to "Simulation", its demo server, on condition of no orders and no other connection (no broker, no Rithmic) (D-071, REPORTED). Today you restated it: "the Simulated Data Feed is the one allowed connection. No orders, no other connection." (`DECISION_LOG.md:427`, REPORTED). Connecting Kinetick, by hand or at startup, would be a second connection besides the Simulated Data Feed (INFERRED from those words). Whether your restatement covers that is yours to say. Leaving it off is the only option that changes nothing. Removing it (D) would also add no connection, but it changes the connection list.

### 8. S6 cross-block, corrected

**Replacement for audited :455 (now :456):**

> - **D-071 as restated by Amear (16:37:30Z, `DECISION_LOG.md:427`):** "the Simulated Data Feed is the one allowed connection. No orders, no other connection." Options B and C would add a second connection, which conflicts with those words on their plain reading (INFERRED). D adds no connection but is a settings change and departs from item 13. Whether the restated D-071 covers a data-only connection is Amear's to say (§5; open question 2, §7).

**S6 on the restated D-071 itself.** INFERRED, flagged for the master and Amear. This decides nothing. As worded, the restatement has no stated scope or end date. Three places it meets other blocks:
- **(a) "No orders" vs the planned consumer on `Sim101`.** Migration concerns item 10 (`:118`, `:131`) plans the consumer on `Sim101` moving one test JSON into `processed\`. Update 2 `:64` marks items 8–10 "**Not started.** PRAXIS's work" (o2b). The consumer places orders (`EnterLong` `:660`, `EnterShort` `:662`) and is Sim-only by its scope wall (`:39-40`) (VERIFIED as file text, o2d). Whether the item-10 test JSON produces an order is **not checked here**. The 10-16 migration rule 1 also said "no orders, not even on Sim101" (REPORTED, o6), which bears on the planned consumer on `Sim101` in the same way.
- **(b) "No other connection" vs Blocks 4–5.** `STATUS.md:296-297` show Block 4 (Paper Trading) and Block 5 (Graduated Live) unchecked, and the signal flow at `CLAUDE.md:21` ends "→ bracket order → Rithmic → MFFU" (VERIFIED as file text, o5 in §10). So a Rithmic connection is planned by design. No PRAXIS order path runs today (migration concerns `:63`, o2d).
- **(c) "Simulation" auto-connect.** On the restatement's plain words, a future auto-connect of "Simulation" (as on 10-19, walkthrough log `:20`, o2a) would now be an "other connection" (INFERRED; Amear's to confirm).
- Whether D-071 was meant for the migration window only is **Amear's call**.

**o2d**. *Manager-run, 2026-10-20 ~12:55 EDT (re-run of correction-worker-1's commands; identical output).*

```
$ cd "/Volumes/Sensidine/Praxis.build"
$ /usr/bin/grep -n '' ninjascript/PraxisSignalConsumer.cs | sed -n '39,40p;660p;662p'
39:// HARD SCOPE WALL: refuses to run unless the attached account name starts with "Sim"
40:// (e.g. Sim101). The guard is a const — there is no parameter to disable it.
660:					EnterLong(sig.Qty, entrySignal);
662:					EnterShort(sig.Qty, entrySignal);
$ /usr/bin/grep -n '' docs/reports/2026-09-29-vm-migration-concerns.md | sed -n '63p;131p' | cut -c1-260
63:VERIFIED from `specs/SPEC_RUBRIC.md`: F1–F4 are all FROZEN. F3 blocks `4uu`, the Block-2 backtest and the main VM workload, and everything downstream of it. No PRAXIS order path runs today.
131:> (3) `PraxisSignalConsumer` on `Sim101` logs `STARTED … dir '<new share path>'` and moves one test `.json` into `processed\`.
```

### 9. B2. Pasted nulls and positive arms

Note on counts: `grep -c` counts matching **lines**, not occurrences. Where it matters, `-o | wc -l` is pasted too.

**o3a**. *Manager-run, 2026-10-20 ~12:55 EDT (re-run of correction-worker-1's commands). Differs from correction-worker-1's own run in one place: its run of the `NQ 12-25` listing used `cut -c1-110`; the command file it left, re-run here, uses `cut -c1-80`. Every other line identical (REPORTED by the manager).*

```
$ cd "/Volumes/Sensidine/Praxis.build"
$ F=docs/reports/2026-08-29-session53-w1-q1-import-instructions.md; wc -l < $F
     473
$ /usr/bin/grep -c -F '##-##' $F; echo "exit=$?"
0
exit=1
$ /usr/bin/grep -n -F '##-##' $F; echo "exit=$?"
exit=1
$ /usr/bin/grep -c -F 'NQ 12-25' $F
16
$ /usr/bin/grep -o -F 'NQ 12-25' $F | wc -l
      16
$ /usr/bin/grep -n -F 'NQ 12-25' $F | cut -c1-80
188:/Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md:150:the copy was name
245:$ grep -n -E 'filename|file name|NQCONT\.Last\.txt|<instrument>|NQ 12-25\.tx
250:/Users/admin/praxis-signals/b2-data/4uu-VM-brief.md:64:(The earlier run fail
260:/Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md:150:the copy was name
261:/Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md:161:`C:\Users\amearba
276:| `NQ 12-25.txt` | the historic WRONG name that broke the 7/23–7/24 run (v2 
290:(The earlier run failed partly because the copy was named `NQ 12-25.txt` — m
299:the copy was named `NQ 12-25.txt`, missing the `.Last` data-type token.
375:/Users/admin/praxis-signals/b2-data/4uu-VM-brief.md:94:**Definitive check** 
379:/Users/admin/praxis-signals/b2-data/outbound/INSTRUCTIONS.md:94:**Definitive
381:/Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md:163:If anyone ever im
385:/Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md:255:**Definitive chec
387:/Users/admin/praxis-signals/b2-data/outbound/4uu-VM-brief-v3.md:163:If anyon
391:/Users/admin/praxis-signals/b2-data/outbound/4uu-VM-brief-v3.md:255:**Defini
441:| M7 | NT8 "sometimes treats a minute bar's stamp as the bar's CLOSE", shift
456:- Deletion of the misnamed 95 MB `NQ 12-25.txt` — v3 l.166: *"Do NOT delete 
$ /usr/bin/grep -n '' $F | sed -n '84p;90,92p'
84:**Answer: 1-minute bars (OHLCV). Not tick. Not daily.** This is a document fact, corroborated by the data file on disk.
90:19:| `NQ-continuous-1min.nt8import.txt` | the source data (NT8-native format) — you will COPY it to the correctly-named file in STEP 1 |
91:20:| `NQ-continuous-1min.csv` | source of record (comma+header+7th col); **do NOT feed to the importer** — it will bounce |
92:61:copy "C:\Mac\Home\praxis-signals\b2-data\NQ-continuous-1min.nt8import.txt" ^
```

o3a: the NQCONT import instructions (473 lines) have 0 `##-##` lines (`exit=1`). The positive arm `NQ 12-25` fires: 16 lines and 16 occurrences, matching audited :106's "16 (adversary B)". `:84` quotes "1-minute bars (OHLCV). Not tick. Not daily."; `:90-92` are the quoted copy-step lines.

**o3b**. *Manager-run, 2026-10-20 ~12:55 EDT (re-run of correction-worker-1's commands; identical output).*

```
$ cd "/Users/admin/praxis-signals/b2-data"
$ /usr/bin/grep -c -F '##-##' 4uu-VM-brief.md 4uu-VM-brief-v3.md outbound/INSTRUCTIONS.md outbound/4uu-VM-brief-v3.md; echo "exit=$?"
4uu-VM-brief.md:0
4uu-VM-brief-v3.md:0
outbound/INSTRUCTIONS.md:0
outbound/4uu-VM-brief-v3.md:0
exit=1
$ /usr/bin/grep -c -F 'NQCONT' 4uu-VM-brief.md 4uu-VM-brief-v3.md outbound/INSTRUCTIONS.md outbound/4uu-VM-brief-v3.md
4uu-VM-brief.md:10
4uu-VM-brief-v3.md:16
outbound/INSTRUCTIONS.md:10
outbound/4uu-VM-brief-v3.md:16
```

o3b: the four outside-repo import briefs have 0 `##-##` lines each (`exit=1`); positive arm `NQCONT` fires in each (10 / 16 / 10 / 16 lines).

**o3c**. *Manager-run, 2026-10-20 ~12:55 EDT (re-run of correction-worker-1's commands; identical output).*

```
$ cd "/Volumes/Sensidine/Praxis.build"
$ /usr/bin/grep -rnoiI -E 'kinetic[^k]|kinetic$' --exclude-dir=.git . | cut -d: -f1 | sort | uniq -c; echo "exit=${PIPESTATUS[0]}"
   2 ./docs/reports/2026-10-20-a20-kinetick-research-adversarial-B.md
   1 ./docs/reports/2026-10-20-a20-kinetick-research-final-check.md
   5 ./docs/reports/2026-10-20-a20-kinetick-research-worker1.md
   2 ./docs/reports/2026-10-20-a20-kinetick-research.md
exit=0
$ /usr/bin/grep -rnoiI -E 'kinetic[^k]|kinetic$' --exclude-dir=.git --exclude='2026-10-20-a20-kinetick-research*' .; echo "exit=$?"
exit=1
$ /usr/bin/grep -rnoiI -E 'kinetick[^s]|kinetick$' --exclude-dir=.git . | wc -l
     483
$ /usr/bin/grep -rnoiI -E 'kinetick[^s]|kinetick$' --exclude-dir=.git --exclude='2026-10-20-a20-kinetick-research*' . | wc -l
     135
$ D="src ninjascript n8n-workflows workflows scripts config deploy signals tests"
$ /usr/bin/grep -rniIw 'eod' $D; echo "exit=$?"
exit=1
$ /usr/bin/grep -rniI 'kinetic' $D; echo "exit=$?"
exit=1
$ /usr/bin/grep -rniI -E 'end of day|endofday|provider7|data feed|datafeed|historical data' $D; echo "exit=$?"
exit=1
$ /usr/bin/grep -rliI -E 'end of day|endofday|provider7|data feed|datafeed|historical data|OnBarUpdate|webhook' $D; echo "exit=$?"
ninjascript/PraxisSignalConsumer.cs
ninjascript/PraxisNoiseAreaBreakout.cs
workflows/EmMbN4sslwIx1ydn.before-b1-b.json
workflows/praxis-telegram-inbound-control.json
workflows/EmMbN4sslwIx1ydn.after-b1-b.json
workflows/EmMbN4sslwIx1ydn.before-qxd.json
workflows/EmMbN4sslwIx1ydn.after-qxd.json
scripts/praxis-signals-sweep-daemon.sh
scripts/praxis-signals-stale-check.sh
scripts/praxis-signals-install.sh
scripts/praxis-inbound-control-watch.sh
scripts/praxis-signals-backlog-check.sh
exit=0
$ /usr/bin/grep -rliI -E 'end of day|endofday|provider7|data feed|datafeed|historical data|OnBarUpdate|webhook' $D | wc -l
      12
$ /usr/bin/grep -rnI -E 'BarsRequest|AddDataSeries|Connection\.|ConnectOnStartup|Provider|##-##' ninjascript src; echo "exit=$?"
exit=1
$ /usr/bin/grep -rnI -E 'BarsRequest|AddDataSeries|Connection\.|ConnectOnStartup|Provider|##-##|OnBarUpdate' ninjascript src | cut -c1-120; echo "exit=${PIPESTATUS[0]}"
ninjascript/PraxisSignalConsumer.cs:134:		protected override void OnBarUpdate()
ninjascript/PraxisNoiseAreaBreakout.cs:138:		protected override void OnBarUpdate()
exit=0
$ ls -la DECISIONS.md RUN_DECISIONS.md PATCH_NOTES.md README.md AGENTS.md
-rw-r--r--@ 1 admin  staff   2908 May  8 14:33 AGENTS.md
-rw-r--r--@ 1 admin  staff  25638 Aug  7 11:43 DECISIONS.md
-rw-r--r--@ 1 admin  staff   9773 Jul 26 12:23 PATCH_NOTES.md
-rw-r--r--@ 1 admin  staff    775 May 11 20:25 README.md
-rw-r--r--@ 1 admin  staff   2880 Jul  9 16:19 RUN_DECISIONS.md
$ /usr/bin/grep -niI kinetick DECISIONS.md RUN_DECISIONS.md PATCH_NOTES.md README.md AGENTS.md; echo "exit=$?"
exit=1
$ /usr/bin/grep -ciI provider DECISIONS.md RUN_DECISIONS.md PATCH_NOTES.md README.md AGENTS.md
DECISIONS.md:4
RUN_DECISIONS.md:0
PATCH_NOTES.md:0
README.md:0
AGENTS.md:0
$ /usr/bin/grep -niI provider DECISIONS.md RUN_DECISIONS.md PATCH_NOTES.md README.md AGENTS.md | cut -c1-90
DECISIONS.md:184:- **Q4 data:** NT8 default-provider MINUTE history — no paid-data budget 
DECISIONS.md:216:**OPEN RISK (flagged, not yet decided):** if the free default provider do
DECISIONS.md:229:**Context:** NinjaTrader 8 cannot export Open Interest. Confirmed a HARD 
DECISIONS.md:233:**Rationale / accepted trade-off:** Roll seams may land ~1–2 days from wh
```

o3c, against adversary B's relayed nulls:
- **S2.** `kinetic[^k]|kinetic$` hits only this unit's own `2026-10-20-a20-kinetick-research*` files (observer effect). Excluding them: `exit=1`. The positive arm `kinetick[^s]|kinetick$` gives **483** matches (`-o` prints one line per match); 135 matches excluding the unit's files, which is 129 lines (o8, below). Adversary B stated **251**. They differ mainly because files have grown since adversary B ran: the unit's own, and also `DECISION_LOG.md` `:426`–`:428` (written 16:36Z–16:40Z, after adversary B's file) (INFERRED); adversary B gave no unit for 251, and it cannot be reconstructed now. What matters is the null plus a firing arm, and both hold.

**o8**. *Manager-run, 2026-10-20 ~13:10 EDT.*

```
$ cd "/Volumes/Sensidine/Praxis.build"
$ /usr/bin/grep -rnoiI -E 'kinetick[^s]|kinetick$' --exclude-dir=.git --exclude='2026-10-20-a20-kinetick-research*' . | wc -l
     135
$ /usr/bin/grep -rniI -E 'kinetick[^s]|kinetick$' --exclude-dir=.git --exclude='2026-10-20-a20-kinetick-research*' . | wc -l
     129
```

- **S4.** Three nulls `exit=1`; positive arm with `OnBarUpdate|webhook` → 12 files (matches B). **S5.** Null `exit=1`; positive `OnBarUpdate` → 2 lines (matches B).
- **S6.** The five files exist (`ls -la`); `kinetick` → `exit=1`. Positive `provider`: `DECISIONS.md:4` is a **`-c` count of 4 lines** (`:184`, `:216`, `:229`, `:233`), not line 4. Audited :370 (now :371) relays it as "→ `DECISIONS.md:4`", which reads like a line cite; it is the count.

**o3d**. *Manager-run, 2026-10-20 ~12:55 EDT (re-run of correction-worker-1's commands; identical output).*

```
$ cd "/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full"
$ ls log | wc -l
      17
$ /usr/bin/grep -c -i -a kinetick log/*; echo "exit=$?"
log/Install.xml:0
log/log.20260815.00000.en.txt:0
log/log.20260815.00000.txt:0
log/log.20260815.00001.en.txt:0
log/log.20260815.00001.txt:0
log/log.20260816.00000.en.txt:0
log/log.20260816.00000.txt:0
log/log.20260817.00000.en.txt:0
log/log.20260817.00000.txt:0
log/log.20260818.00000.en.txt:0
log/log.20260818.00000.txt:0
log/log.20260828.00000.en.txt:0
log/log.20260828.00000.txt:0
log/log.20260829.00000.en.txt:0
log/log.20260829.00000.txt:0
log/log.20260829.00001.en.txt:0
log/log.20260829.00001.txt:0
exit=1
$ /usr/bin/grep -c -a 'Simulated Data Feed' log/*
log/Install.xml:0
log/log.20260815.00000.en.txt:0
log/log.20260815.00000.txt:0
log/log.20260815.00001.en.txt:3
log/log.20260815.00001.txt:3
log/log.20260816.00000.en.txt:0
log/log.20260816.00000.txt:0
log/log.20260817.00000.en.txt:0
log/log.20260817.00000.txt:0
log/log.20260818.00000.en.txt:0
log/log.20260818.00000.txt:0
log/log.20260828.00000.en.txt:0
log/log.20260828.00000.txt:0
log/log.20260829.00000.en.txt:5
log/log.20260829.00000.txt:5
log/log.20260829.00001.en.txt:3
log/log.20260829.00001.txt:3
$ /usr/bin/grep -c -a 'Historical Data Server' log/*
log/Install.xml:0
log/log.20260815.00000.en.txt:0
log/log.20260815.00000.txt:0
log/log.20260815.00001.en.txt:0
log/log.20260815.00001.txt:0
log/log.20260816.00000.en.txt:2
log/log.20260816.00000.txt:2
log/log.20260817.00000.en.txt:16
log/log.20260817.00000.txt:16
log/log.20260818.00000.en.txt:6
log/log.20260818.00000.txt:6
log/log.20260828.00000.en.txt:2
log/log.20260828.00000.txt:2
log/log.20260829.00000.en.txt:0
log/log.20260829.00000.txt:0
log/log.20260829.00001.en.txt:0
log/log.20260829.00001.txt:0
$ for f in log/*.en.txt; do cmp -s "$f" "${f%.en.txt}.txt" && echo "same: $f" || echo "DIFFERENT: $f"; done
same: log/log.20260815.00000.en.txt
same: log/log.20260815.00001.en.txt
same: log/log.20260816.00000.en.txt
same: log/log.20260817.00000.en.txt
same: log/log.20260818.00000.en.txt
same: log/log.20260828.00000.en.txt
same: log/log.20260829.00000.en.txt
same: log/log.20260829.00001.en.txt
```

o3d: all 17 files in the old install's `log/` have 0 `kinetick` lines (`exit=1`). Positive arms fire: "Simulated Data Feed" 3 / 5 / 3 lines (08-15 `00001`, 08-29 `00000`, 08-29 `00001`), matching audited :370's 3/5/3; "Historical Data Server" 2 / 16 / 6 / 2 lines (08-16, 08-17, 08-18, 08-28). Each `.en` file is byte-identical to its non-`.en` twin (`cmp`), so each figure appears twice.

**o3e**. *Manager-run, 2026-10-20 ~12:55 EDT (re-run of correction-worker-1's commands; identical output).*

```
$ cd "/Volumes/Sensidine/Praxis.build"
$ /usr/bin/grep -rlI -i kinetick /Users/admin/praxis-signals --include='*.cs' --include='*.py' --include='*.js' --include='*.json' --include='*.sh'; echo "exit=$?"
exit=1
$ /usr/bin/grep -rlI -i -E 'OnBarUpdate|FileSystemWatcher' /Users/admin/praxis-signals --include='*.cs' --include='*.py' --include='*.js' --include='*.json' --include='*.sh'; echo "exit=$?"
/Users/admin/praxis-signals/b2-data/ninjascript/PraxisNoiseAreaBreakout.cs
/Users/admin/praxis-signals/archive/PraxisSignalConsumer.cs
exit=0
$ find /Users/admin/praxis-signals -type f \( -name '*.cs' -o -name '*.py' -o -name '*.js' -o -name '*.json' -o -name '*.sh' \) | wc -l
      16
$ /usr/bin/grep -rliI kinetick /Users/admin/praxis-signals | sed 's/.*\.//' | sort | uniq -c
   9 md
   1 txt
```

o3e: outside-repo code in `~/praxis-signals` (`*.cs|py|js|json|sh`, 16 files in scope): `kinetick` → `exit=1`; positive `OnBarUpdate|FileSystemWatcher` → 2 files. All Kinetick hits there are 9 `.md` and 1 `.txt`. Matches audited :109.

**What this changes.** Audited :106 (now :107) and :109 (now :110) now rest on these pastes: VERIFIED (search), manager-run. The conclusion drawn from them, "no mention = no dependency", stays **INFERRED**.

### 10. M1–M5

**M1** (audited :427, now :428).

**o4c**. *Manager-run, 2026-10-20 ~12:55 EDT (re-run of correction-worker-1's commands; identical output).*

```
$ cd "/Volumes/Sensidine/Praxis.build"
$ /usr/bin/grep -rl -i -E 'quote freshness|last-tick-age|Continuum' --exclude-dir=.git --exclude-dir=Redemtion .; echo "exit=$?"
./docs/reports/2026-10-20-a20-kinetick-research-fix-check.md
./docs/reports/2026-10-20-a20-kinetick-research-worker1.md
./docs/reports/2026-10-20-a20-kinetick-research.md
./DECISIONS.md
exit=0
```

Replacement for audited :427's observer-effect sentence: "Observer effect: a re-run now matches this report, the W6 (fix-check) and W1 (worker1) files, and `DECISIONS.md`. The W5 (final-check) file does **not** match." (VERIFIED, o4c.) This appended section quotes the same terms, and later files may add matches. The figures here are as pasted and are not edited afterwards. The rest of audited :427 stands.

**M2** (audited :15, now :16). Replacement for "(searches VERIFIED, below)": "(searches VERIFIED: E7, E9 (Block 2 daily inputs) and E12 in the body, and the manager-run pastes in the post-audit correction §9)".

**M3** (audited :14, now :15). NT8 purged its older logs (o4b); only 08-15 → 08-29 survive (`ls -l log` at the top of o4a).

**o4b**. *Manager-run, 2026-10-20 ~12:55 EDT (re-run of correction-worker-1's commands; identical output).*

```
$ cd "/Volumes/Sensidine/Praxis.build"
$ sed -n 393p DECISION_LOG.md | cut -c1-600
- [2026-09-29T15:45:00Z (approximate, not measured)] WHO: praxis-master | WHAT: **Answered the migration agent's final pre-shutdown question: "(a) SUFFICIENT."** One optional insurance item: the AppData NinjaTrader* folders, if any exist | WHY: every PRAXIS item is either on disk in two places or recoverable from the Mac side. VERIFIED this turn: (1) the 11:03 copy's `NinjaTrader.sqlite`, opened read-only with `immutable=1`, holds MasterInstruments `NQ` (Future and Stock) and `NQCONT` (Future, trading hours `CME US Index Futures RTH`; and Stock, blank description), plus Instruments rows for th
$ sed -n 393p DECISION_LOG.md | /usr/bin/grep -o '(d) \*\*NT8 PURGED.\{0,190\}'
(d) **NT8 PURGED all older log and trace files at its 11:12 start.** `files/NinjaTrader 8-full` is the ONLY record of the 08-15 to 08-29 logs. **Standing lesson: copy NT8 log evidence off BEFORE NT8 is next
$ git show HEAD:DECISION_LOG.md | wc -l; git show HEAD:DECISION_LOG.md | /usr/bin/grep -c 'NT8 PURGED all older log'
      59
0
```

**o4a**. *Manager-run, 2026-10-20 ~12:55 EDT (re-run of correction-worker-1's commands; identical output).* The source files are Windows text: the trailing CR bytes of their lines were dropped when this section was edited; otherwise identical (the manager's check is pasted at the end of this section).

```
$ cd "/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full"
$ ls -l log
total 136
-rw-r--r--@ 1 admin  staff   382 Aug 29 11:02 Install.xml
-rw-r--r--@ 1 admin  staff    61 Aug 15 10:09 log.20260815.00000.en.txt
-rw-r--r--@ 1 admin  staff    61 Aug 15 10:09 log.20260815.00000.txt
-rw-r--r--@ 1 admin  staff   882 Aug 15 10:12 log.20260815.00001.en.txt
-rw-r--r--@ 1 admin  staff   882 Aug 15 10:12 log.20260815.00001.txt
-rw-r--r--@ 1 admin  staff   317 Aug 16 08:07 log.20260816.00000.en.txt
-rw-r--r--@ 1 admin  staff   317 Aug 16 08:07 log.20260816.00000.txt
-rw-r--r--@ 1 admin  staff  2536 Aug 17 14:02 log.20260817.00000.en.txt
-rw-r--r--@ 1 admin  staff  2536 Aug 17 14:02 log.20260817.00000.txt
-rw-r--r--@ 1 admin  staff  1086 Aug 18 19:55 log.20260818.00000.en.txt
-rw-r--r--@ 1 admin  staff  1086 Aug 18 19:55 log.20260818.00000.txt
-rw-r--r--@ 1 admin  staff   317 Aug 28 18:18 log.20260828.00000.en.txt
-rw-r--r--@ 1 admin  staff   317 Aug 28 18:18 log.20260828.00000.txt
-rw-r--r--@ 1 admin  staff  2150 Aug 29 11:01 log.20260829.00000.en.txt
-rw-r--r--@ 1 admin  staff  2150 Aug 29 11:01 log.20260829.00000.txt
-rw-r--r--@ 1 admin  staff  2530 Aug 29 12:01 log.20260829.00001.en.txt
-rw-r--r--@ 1 admin  staff  2530 Aug 29 12:01 log.20260829.00001.txt
$ /usr/bin/grep -H -a "Historical Data Server" log/*.en.txt
log/log.20260816.00000.en.txt:2026-08-16 08:07:33:743|3|2|Connection lost to the NinjaTrader Historical Data Server: hds-us-nt-020.ninjatrader.com
log/log.20260816.00000.en.txt:2026-08-16 08:07:44:040|1|2|Connection restored to the NinjaTrader Historical Data Server: hds-us-nt-012.ninjatrader.com
log/log.20260817.00000.en.txt:2026-08-17 10:32:16:485|3|2|Connection lost to the NinjaTrader Historical Data Server: hds-us-nt-012.ninjatrader.com
log/log.20260817.00000.en.txt:2026-08-17 10:32:26:661|1|2|Connection restored to the NinjaTrader Historical Data Server: hds-us-nt-019.ninjatrader.com
log/log.20260817.00000.en.txt:2026-08-17 10:35:19:679|3|2|Connection lost to the NinjaTrader Historical Data Server: hds-us-nt-019.ninjatrader.com
log/log.20260817.00000.en.txt:2026-08-17 10:56:22:799|1|2|Connection restored to the NinjaTrader Historical Data Server: hds-us-nt-017.ninjatrader.com
log/log.20260817.00000.en.txt:2026-08-17 11:05:25:012|3|2|Connection lost to the NinjaTrader Historical Data Server: hds-us-nt-017.ninjatrader.com
log/log.20260817.00000.en.txt:2026-08-17 11:05:35:230|1|2|Connection restored to the NinjaTrader Historical Data Server: hds-us-nt-016.ninjatrader.com
log/log.20260817.00000.en.txt:2026-08-17 11:09:36:823|3|2|Connection lost to the NinjaTrader Historical Data Server: hds-us-nt-016.ninjatrader.com
log/log.20260817.00000.en.txt:2026-08-17 11:09:47:123|1|2|Connection restored to the NinjaTrader Historical Data Server: hds-us-nt-017.ninjatrader.com
log/log.20260817.00000.en.txt:2026-08-17 12:03:57:700|3|2|Connection lost to the NinjaTrader Historical Data Server: hds-us-nt-017.ninjatrader.com
log/log.20260817.00000.en.txt:2026-08-17 12:04:07:963|1|2|Connection restored to the NinjaTrader Historical Data Server: hds-us-nt-007.ninjatrader.com
log/log.20260817.00000.en.txt:2026-08-17 12:05:39:430|3|2|Connection lost to the NinjaTrader Historical Data Server: hds-us-nt-007.ninjatrader.com
log/log.20260817.00000.en.txt:2026-08-17 12:12:47:059|1|2|Connection restored to the NinjaTrader Historical Data Server: hds-us-nt-014.ninjatrader.com
log/log.20260817.00000.en.txt:2026-08-17 12:14:23:259|3|2|Connection lost to the NinjaTrader Historical Data Server: hds-us-nt-014.ninjatrader.com
log/log.20260817.00000.en.txt:2026-08-17 12:14:33:550|1|2|Connection restored to the NinjaTrader Historical Data Server: hds-us-nt-016.ninjatrader.com
log/log.20260817.00000.en.txt:2026-08-17 13:42:19:954|3|2|Connection lost to the NinjaTrader Historical Data Server: hds-us-nt-016.ninjatrader.com
log/log.20260817.00000.en.txt:2026-08-17 14:02:13:946|1|2|Connection restored to the NinjaTrader Historical Data Server: hds-us-nt-011.ninjatrader.com
log/log.20260818.00000.en.txt:2026-08-18 11:16:20:645|3|2|Connection lost to the NinjaTrader Historical Data Server: hds-us-nt-011.ninjatrader.com
log/log.20260818.00000.en.txt:2026-08-18 15:10:46:480|1|2|Connection restored to the NinjaTrader Historical Data Server: hds-us-nt-019.ninjatrader.com
log/log.20260818.00000.en.txt:2026-08-18 16:14:33:305|3|2|Connection lost to the NinjaTrader Historical Data Server: hds-us-nt-019.ninjatrader.com
log/log.20260818.00000.en.txt:2026-08-18 16:14:44:410|1|2|Connection restored to the NinjaTrader Historical Data Server: hds-us-nt-018.ninjatrader.com
log/log.20260818.00000.en.txt:2026-08-18 19:55:06:741|3|2|Connection lost to the NinjaTrader Historical Data Server: hds-us-nt-018.ninjatrader.com
log/log.20260818.00000.en.txt:2026-08-18 19:55:16:965|1|2|Connection restored to the NinjaTrader Historical Data Server: hds-us-nt-017.ninjatrader.com
log/log.20260828.00000.en.txt:2026-08-28 18:18:36:315|3|2|Connection lost to the NinjaTrader Historical Data Server: hds-us-nt-017.ninjatrader.com
log/log.20260828.00000.en.txt:2026-08-28 18:18:46:538|1|2|Connection restored to the NinjaTrader Historical Data Server: hds-us-nt-008.ninjatrader.com
$ /usr/bin/grep -h -a "Historical Data Server" log/*.en.txt | wc -l
      26
$ /usr/bin/grep -h -a -o -E '(Connection [a-z]+ to|[Cc]onnected to|[Cc]onnecting to|Disconnected from) the NinjaTrader Historical Data Server' log/*.en.txt | sort | uniq -c
  13 Connection lost to the NinjaTrader Historical Data Server
  13 Connection restored to the NinjaTrader Historical Data Server
$ /usr/bin/grep -h -a "Historical Data Server" log/*.en.txt | /usr/bin/grep -c -v -E 'Connection (lost|restored) to the NinjaTrader Historical Data Server'
0
```

Replacement for audited :14's "No old connection log mentions it": "None of the surviving old logs (08-15 → 08-29 only) mentions it (VERIFIED, o3d and the `ls -l log` in o4a). Older logs were purged by NT8 at its 11:12 start (REPORTED, `DECISION_LOG.md:393` (d), an uncommitted worktree line: HEAD's DECISION_LOG has 59 lines and 0 matches, o4b)."

**M4** (audited :108, now :109; audited :146, now :147). o4a above lists all 26 "Historical Data Server" lines. They are 13 "Connection lost to the NinjaTrader Historical Data Server: …" and 13 "Connection restored to the NinjaTrader Historical Data Server: …" events, on 08-16, 08-17, 08-18 and 08-28. There are 0 lines of any other form (VERIFIED text, o4a). Audited :108's "**connected to**" and :146's quoted "connected to (VERIFIED)" are superseded by that exact description. That NT8 held such a connection in that window is read off "restored" (INFERRED). "Bars came from there" stays INFERRED. Which provider wrote the 07-14 batch stays UNVERIFIED.

**M5** (audited :28, now :29).

**o5**. *Manager-run, 2026-10-20 ~12:55 EDT (re-run of correction-worker-1's commands; identical output).*

```
$ cd "/Volumes/Sensidine/Praxis.build"
$ /usr/bin/grep -n '^| S6\|^| S7' specs/SPEC_RUBRIC.md
112:| S6 | Cross-block check: every approved deviation is tested against the specs of every other block it touches, not only its own. |
113:| S7 | Nothing is committed while any audit box is unchecked. |
$ git show HEAD:specs/SPEC_RUBRIC.md | /usr/bin/grep -n '^| S6\|^| S7'
112:| S6 | Cross-block check: every approved deviation is tested against the specs of every other block it touches, not only its own. |
113:| S7 | Nothing is committed while any audit box is unchecked. |
$ /usr/bin/grep -n '^| S1 \|^| S2 \|^| S8 ' specs/SPEC_RUBRIC.md | cut -c1-60
107:| S1 | Every claim in a report has pasted command output
108:| S2 | No component is reported at a higher level than t
114:| S8 | No question that belongs to Amear is answered on 
$ /usr/bin/grep -n '' CLAUDE.md | sed -n '21p'
21:Signal flow: TradingView alert → webhook → n8n workflow → JSON file drop → NinjaScript FileSystemWatcher → bracket order → Rithmic → MFFU
$ /usr/bin/grep -n '' STATUS.md | sed -n '296,297p'
296:- [ ] Block 4 — Paper Trading
297:- [ ] Block 5 — Graduated Live (comprehension gate: recorded debrief pass required before live — D-2026-07-04-A)
```

o5: S6 is `specs/SPEC_RUBRIC.md:112` and S7 is `:113`, in the worktree and at HEAD. Audited :28's S6 cite should read `:112`. Its S1 (`:107`), S2 (`:108`) and S8 (`:114`) cites stand. o5 also carries `CLAUDE.md:21` and `STATUS.md:296-297`, used in §8 (b).

### Verification evidence (correction)

Each block appears once, where it is first used:
- **o7** (§1): the master's audit-FAIL row `DECISION_LOG.md:428`. Carries §1.
- **o1** (§2): the audited copy's `D-071|Simulation|:424|15:55` hits, i.e. the lines the register covers.
- **o2a** (§3): the original D-071 row (committed, migration repo), the in-VM brief `:15`/`:65`, the walkthrough log `:11`/`:20`. Carries §3 (i), §4's Part 5/6 inference, §5's rule-6 note.
- **o2b** (§3): HEAD count 0 for the 15:55:42Z / 16:36:23Z / 16:37:30Z rows; rows `:424`, `:426`, `:427`; update 2 `:64`, `:67`; results `:21`, `:46`; walkthrough `:74`; capture notes `:50-55`; reference `:33`; migration concerns `:111-122`; adversarial-B `:14`, `:22`. Carries §3, §4's two-rows point, §5–§8's quotes of the restated D-071.
- **o6** (§3, after o2b): the 10-16 in-VM brief `:18`, `:20` (hard rule 1), `:69`, `:94`; committed `0888f0f`. Carries §3 (0), (i), (iii), "Where it stands now", §4's second layer, §5 row B, §8 (a).
- **o2c** (§4): Config.xml's three connection blocks and the three non-connection "Simulation" fields. Carries C4.
- **o9** (§4): update 2 `:25`, `:62`, `:70`; walkthrough `:31` P9. Carries §3 (iii) and §4's restore and relay points.
- **o2d** (§8): the consumer's scope wall and order calls; migration concerns `:63`, `:131`. Carries §8 (a), (b).
- **o3a–o3e** (§9): the B2 nulls and positive arms. Carry audited :106, :109, :370.
- **o8** (§9, in the S2 bullet's note): `kinetick[^s]|kinetick$` excluding the unit's files, 135 with `-o` (matches) and 129 without (lines).
- **o4a, o4b, o4c, o5** (§10): M1, M3, M4, M5; o5 also §8 (b).

### Workers dispatched (correction)

- **CW1, BUILD.** Hit its 40-turn limit and wrote nothing to the artifact. The manager re-ran its captured commands with identical output (one block, o3a, differed only by a cut width: CW1's run of the `NQ 12-25` listing used `cut -c1-110`, the command file it left uses `cut -c1-80`). Those re-runs are the o-blocks o1–o5 above.
- **CW2, BUILD.** Wrote this section.
- **CW3, ADVERSARIAL.** VERDICT: FAIL, 3 MAJOR (F1–F3) and 5 MINOR (F4–F8). Report `docs/reports/2026-10-20-a20-kinetick-research-correction-adversarial.md`.
- **CW4, BUILD.** Applied F1–F8 and the manager's M-a…M-d to this section. o6, o7, o8 were captured by the manager.
- **CW5, ADVERSARIAL fix-check.** VERDICT: PASS; all 12 earlier items fixed; 7 MINOR in the new text (report `docs/reports/2026-10-20-a20-kinetick-research-correction-fixcheck.md`).
- **CW6, BUILD.** Applied CW5's 7 MINOR fixes and the o9 block.

### Files staged (correction)

None by this correction. Run by CW2 at build time (the artifact is untracked, so building it does not change this count):

```
$ cd "/Volumes/Sensidine/Praxis.build"
$ git diff --cached --name-only | wc -l
       9
```

### Adversarial findings (correction)

- **CW3, full attack on this section: VERDICT: FAIL.** 3 MAJOR and 5 MINOR. CW4 applied all eight:
  - F1 MAJOR: §6 said only A leaves the Simulated Data Feed as the sole connection, but D does too. Fixed in §6.
  - F2 MAJOR (S8): §6 had dropped the "if D-071 covers it" hedge. Restored in §6.
  - F3 MAJOR: on 10-19 the Simulated Data Feed was already allowed, and the restatement narrows that allowance. Now drawn out using the 10-16 rule 1 (o6): §3 (0), (iii) and "Where it stands now"; the second layer in §4; §8 (c).
  - F4–F8 MINOR: the brief's wording in §5 row B; `-o` matches vs lines (o8); the o3a label; register row :124; the `~/Windows-migration/` prefixes.
- **The manager's own read, applied by CW4:** §1 cites the audit row `:428` (o7); the M2 replacement includes E9; §4 labels the Config.xml swap as a plan; the summary-line-5 replacement no longer reads two ways.
- **CW5, narrow fix-check: VERDICT: PASS.** All 12 items above are fixed. It found 7 MINOR defects in the new text, and CW6 applied all of them: D-071's Part 4 clause; the restore cite (`:25`, `:70`) and the 10-19 counter-evidence; §1's attribution against `:428`; the relay claim, now labelled (o9); row B's "lean", now labelled INFERRED; the 251 explanation, widened and labelled; the o1 label.
- **Not re-attacked:** CW6's edits and the o9 block. The manager read CW6's whole diff against its pre-edit backup. Only the listed edits changed, and no pasted block's content changed (blockcheck, below).

### Manager checks (correction)

*Manager-run, 2026-10-20 ~13:25 EDT. Taken after CW6's rebuild and before this closing block was appended, so appending the block lengthens the tail hunk past `1205`. The final figures are in the manager's return to the master. `support-sums.txt` holds the sha256 values of the five support files, taken at the start of this unit.*

```
$ cd "/Volumes/Sensidine/Praxis.build"
$ diff /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/6d0e9294-2389-48c6-9c19-27f79fa5cae6/scratchpad/a20-original.md docs/reports/2026-10-20-a20-kinetick-research.md | /usr/bin/grep -E '^[0-9]'
1a2
491a493,1205
$ sed -n 2p docs/reports/2026-10-20-a20-kinetick-research.md
**Post-audit correction (2026-10-20) appended at the end; it supersedes the lines it names.**
$ diff <(sed '2d' docs/reports/2026-10-20-a20-kinetick-research.md | head -491) /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/6d0e9294-2389-48c6-9c19-27f79fa5cae6/scratchpad/a20-original.md && echo "audited body byte-identical (artifact minus line 2, first 491 lines)"
audited body byte-identical (artifact minus line 2, first 491 lines)
$ wc -l < /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/6d0e9294-2389-48c6-9c19-27f79fa5cae6/scratchpad/a20-original.md; wc -l < docs/reports/2026-10-20-a20-kinetick-research.md
     491
    1205
$ shasum -a 256 -c /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/6d0e9294-2389-48c6-9c19-27f79fa5cae6/scratchpad/support-sums.txt
docs/reports/2026-10-20-a20-kinetick-research-adversarial-A.md: OK
docs/reports/2026-10-20-a20-kinetick-research-adversarial-B.md: OK
docs/reports/2026-10-20-a20-kinetick-research-final-check.md: OK
docs/reports/2026-10-20-a20-kinetick-research-fix-check.md: OK
docs/reports/2026-10-20-a20-kinetick-research-worker1.md: OK
$ /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/6d0e9294-2389-48c6-9c19-27f79fa5cae6/scratchpad/blockcheck.sh docs/reports/2026-10-20-a20-kinetick-research.md /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/6d0e9294-2389-48c6-9c19-27f79fa5cae6/scratchpad/ev2
o1:       24 lines, found at line 523, byte-identical
o2a:       17 lines, found at line 603, byte-identical
o2b:       35 lines, found at line 625, byte-identical
o2c:       48 lines, found at line 701, identical-except-CR
o2d:        9 lines, found at line 798, byte-identical
o3a:       34 lines, found at line 816, byte-identical
o3b:       12 lines, found at line 857, byte-identical
o3c:       61 lines, found at line 876, byte-identical
o3d:       67 lines, found at line 958, byte-identical
o3e:       12 lines, found at line 1032, byte-identical
o4a:       54 lines, found at line 1088, identical-except-CR
o4b:        8 lines, found at line 1075, byte-identical
o4c:        7 lines, found at line 1057, byte-identical
o5:       16 lines, found at line 1153, byte-identical
o6:       10 lines, found at line 665, byte-identical
o7:        3 lines, found at line 511, byte-identical
o8:        5 lines, found at line 945, byte-identical
o9:        7 lines, found at line 689, byte-identical
$ /usr/bin/grep -c -w -i 'T[B]D' docs/reports/2026-10-20-a20-kinetick-research.md
0
$ git diff --cached --name-only | wc -l
       9
$ diff <(git diff --cached --name-only) /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/6d0e9294-2389-48c6-9c19-27f79fa5cae6/scratchpad/staged-before.txt && echo "staged set identical to the session-start snapshot"
staged set identical to the session-start snapshot
$ git status --porcelain --untracked-files=all docs/reports/ | /usr/bin/grep -F '2026-10-20-a20-kinetick-research'
?? docs/reports/2026-10-20-a20-kinetick-research-adversarial-A.md
?? docs/reports/2026-10-20-a20-kinetick-research-adversarial-B.md
?? docs/reports/2026-10-20-a20-kinetick-research-correction-adversarial.md
?? docs/reports/2026-10-20-a20-kinetick-research-correction-fixcheck.md
?? docs/reports/2026-10-20-a20-kinetick-research-correction-worker.md
?? docs/reports/2026-10-20-a20-kinetick-research-final-check.md
?? docs/reports/2026-10-20-a20-kinetick-research-fix-check.md
?? docs/reports/2026-10-20-a20-kinetick-research-worker1.md
?? docs/reports/2026-10-20-a20-kinetick-research.md
```

For each pasted block, `blockcheck.sh` reports where its CR-stripped content sits in the artifact and whether the raw bytes match. o2c and o4a differ only by the CR bytes dropped from their Windows source lines, as their labels say.

### S6 cross-block check (correction)

See §8. It holds the corrected S6 entry for audited :455, and it runs S6 on the restated D-071 itself: (a) "No orders" vs the planned consumer on `Sim101`; (b) "no other connection" vs Blocks 4–5 and Rithmic; (c) a future "Simulation" auto-connect. All of it is INFERRED and flagged for the master and Amear. It decides nothing.

### Result (correction)

**Result: PASS.** This is the manager's stress-test outcome for this correction under the report contract. **It is not an audit grade**: the master's auditor grades it. What it means: B1, B2 and M1–M5 are each addressed by append, with pasted evidence. The last adversary (CW5) returned VERDICT: PASS, and its seven MINORs have been applied. The audited body and the five support files are unchanged, and so is the staged set. Residuals, disclosed: CW6's edits were not re-attacked; Fusion's own Config.xml is still unread; the scope of the restated D-071 and the K1 choice remain Amear's.

---

## Auditor grades, 2026-10-20

> **PROVENANCE:** praxis-master transcribed this from the messages returned by two `praxis-auditor` runs. The auditor cannot write files. Nothing above this line was edited after either grade.

**Audit 1 (on the original 491-line body): `Result: FAIL`.** This was **strike one on `Praxis_build-a20`** (`DECISION_LOG` 16:40:32Z).
- B1 (S2, S6), blocking: D-071 was applied to the wrong connection ("Simulation" was treated as the Simulated Data Feed). Root cause: the master's question framing, carried into this report.
- B2 (S1), blocking: the NQCONT-import null and adversary B's nulls had no pasted output.
- Minor M1–M4. S8 and S9/R3 PASS.

**Audit 2 (re-audit of the appended correction): `Result: PASS`.** S1, S2, S6, S8 and S9/R3 all PASS. No blocking findings.
- The auditor re-ran o2a, o6 and o2b against `~/Windows-migration` and this repo's ledger rows.
- It searched the stored original for every term carrying the equivalence and found the §2 register complete.
- It re-ran the §9 nulls with their positive arms, and planted a control of its own in a scratch copy of a log.
- It confirmed the append-only diff: `1a2` and `491a493,1285`, with the first 491 lines byte-identical once line 2 is removed.
- It sampled all seven CW6 fixes.
- Minor findings, not fixed here:
  - m1: the original Result line isn't named in the §2 register.
  - m2: "identical output" for CW1 rests on the manager's word.
  - m3: M1's matching-file list has grown since the paste, as the report anticipates.
- One limit it disclosed: the copy of the original is in the producer's scratchpad. Its sha matches the sha in the report's header, but it hasn't been compared with an independent copy.

**Master re-ran in this turn (17:29:16Z):** the code null (`exit=1`) with its positive arm (2 files). D-071 at `~/Windows-migration/DECISION_LOG.md:124`: clean, and the text matches. The 10-19 brief `:15`: "Simulated Data Feed" and "Simulation" only. The pointer line, the length (1285) and the staged set (9). All reproduce.

**Status: cleared to bring to Amear. K1 (Kinetick) is his decision.**
