# a20 follow-up: Kinetick End Of Day research (worker 1)

**Task:** answer Amear's "i dont know what that is or i dont remeber. look into it" (`DECISION_LOG.md:424`) about the row **Kinetick – End Of Day (Free)** in NT8's Connections menu on the Fusion VM (read K1, `docs/reports/2026-10-20-a20-results.md:21-22`). Bead `Praxis_build-a20`.
**Mode:** BUILD (read-only research). **Date:** 2026-10-20.
**Criterion:** `specs/SPEC_RUBRIC.md:107` (S1, pasted output for every claim), `:108` (S2, no claim stated more strongly than its evidence), `:114` (S8, no question of Amear's answered for him).
**Scope kept:** no commit, no `git add`, no existing file edited, nothing under `.claude/` touched. No VM, NinjaTrader, VMware or network access. **No web lookup tool was available to me in this run**, so every statement about Kinetick as a product that does not come from the repo or the rescue copy is general knowledge and is labelled **UNVERIFIED**.

**Labels.** **VERIFIED** = I saw it in this run (command and output pasted below, or file:line quoted word for word). **REPORTED** = someone in the record said it (file:line). **INFERRED** = my reasoning, with what it rests on. **UNVERIFIED** = general knowledge, not checked here. Reading a document is not watching the system: a document saying "Kinetick provides X" makes X REPORTED, not VERIFIED. Reading a machine-written NT8 file (Config.xml, a log, the data folder) is VERIFIED for *what the file contains*. What that implies about NT8's behaviour is still INFERRED.

**Disclosure.** While I was reading the rescue `Config.xml` (`cat -n … sed -n 1,80p`), lines 5-14 printed in my own tool output. Those lines hold the cached NinjaTrader account tokens for `amear238`. I have **not** reproduced them in this report, and every excerpt below starts at line 15 or later. They went no further than my session output.

---

## Plain-language answer (for Amear)

- **What it is (UNVERIFIED, general knowledge):** Kinetick is a market-data service sold through NinjaTrader. The "End Of Day (Free)" connection is its free tier, which gives **one bar per day** (daily open, high, low, close and volume) after the market closes. It gives **no live prices, no 1-minute or tick history, and no order routing.** As far as I know it comes pre-loaded in NT8, so you probably never set it up. **The record backs that up: nobody in PRAXIS ever recorded setting it up** (see Q2).
- **Has PRAXIS ever used it? No evidence that it has.** It was switched off at startup on the old install (`Config.xml:34`, VERIFIED). The surviving old NT8 logs (2026-08-15 to 08-29) show **only the Simulated Data Feed** connecting automatically, and **no Kinetick line at all** (VERIFIED). Historical bars came from the **NinjaTrader Historical Data Server** (VERIFIED in the logs). The Block 2 data decision is "NT8 default-provider minute history, no paid data" (`DECISIONS.md:184`, REPORTED), and Kinetick isn't named in it.
- **Does anything depend on it? No.** No code, workflow, config or script mentions it (searches pasted below). The signal path, backtesting and the NQCONT import don't need it.
- **The NQCONT "unknown instrument" error:** the record does **not** tie Kinetick to it. The a20 walkthrough says the error is "a separate defect" (`2026-10-20-a20-fusion-tz-kinetick-walkthrough.md:183`, REPORTED).
- **Your choice, not decided here:** leave it as it is (off), connect it by hand when needed, set it to connect at startup, or delete the connection. The risks are set out in Q4.

---

## Q1. What is "Kinetick – End Of Day (Free)" in NT8?

### What the repo and the old install record

| # | Claim | Label | Source |
|---|---|---|---|
| 1.1 | The old install had a connection named `Kinetick – End Of Day (Free)`, of type `NinjaTrader.Cbi.KinetickOptions`, provider `Provider7`, with `<Free>true</Free>` and an empty user name and password | **VERIFIED** (machine file read this run) | rescue `Config.xml:39-47`, excerpt below |
| 1.2 | It was set **not** to connect at startup. The Simulated Data Feed **was** set to connect at startup | **VERIFIED** | `Config.xml:34` `false`; `Config.xml:18` `true` |
| 1.3 | Its other stored options: `IsHdsEnabled false`, `BackadjustContinuousContracts false`, `UseFundamentalData true`, `NewsDaysBack 1`, `GlobexNonProFees false`, `CanManageOrders true` | **VERIFIED** (file contents). What each one does in NT8 is **UNVERIFIED** | `Config.xml:33-49` |
| 1.4 | NT8 lists Kinetick among the providers licensed to this account (`subscription=Free`) | **VERIFIED** (trace line read) | `trace.20260815.00001.txt:23`, also 08-29 traces, pasted below |
| 1.5 | "Kinetick (NT8 native partner) \| EOD free; minute/tick paid \| $ \| Cleanest NT8 integration for deep minute history" | **REPORTED** (a proposal; no source cited for the vendor facts) | `docs/specs/2026-07-15-block2-backtesting-scope-proposal.md:46` |
| 1.6 | "An **End Of Day** feed does not supply intraday minute bars." | **REPORTED** (stated without a source) | `docs/reports/2026-08-29-session53-nqcont-resolution-and-rth-corpus-read.md:418` |
| 1.7 | "**UNVERIFIED** whether Kinetick's free EOD tier serves any intraday history at all — a vendor-plan fact, and nobody here has connected it." | **REPORTED** | `docs/reports/2026-08-29-session53-w4-adversarial-q4-designs.md:270-271` |
| 1.8 | Continuous contracts (`NQ ##-##`) "Requires **provider support** (historically Kinetick / eSignal / IQFeed)" | **REPORTED** | `docs/reference/2026-07-24-nt8-windows-reference.md:186` |
| 1.9 | Whether Kinetick EOD Free meets that provider-support requirement "is not recorded" | **REPORTED** | `…session53-nqcont-resolution-and-rth-corpus-read.md:431-432` |
| 1.10 | "Data is real-time market data (via NinjaTrader's bundled Kinetick feed)" | **REPORTED, and contradicted** (see Contradictions C1) | `docs/reports/2026-07-09-b1-0-nt8-parallels-validation.md:82` |

### General knowledge (all UNVERIFIED, no web tool this run)

- **UNVERIFIED:** Kinetick is a market-data brand that NinjaTrader offered for NT7 and NT8. The data was supplied by a third-party vendor (my recollection is DTN/IQFeed infrastructure).
- **UNVERIFIED:** the **End Of Day (Free)** tier provides **daily bars only** (OHLC plus volume, one bar per trading day), published after each session closes. It covers US stocks, indices and futures, and possibly forex. **It costs nothing.**
- **UNVERIFIED:** it does **not** provide real-time quotes, intraday (minute or tick) history, Level II or market depth, or order routing. A paid Kinetick tier provided real-time and intraday data, plus exchange fees.
- **UNVERIFIED:** NT8 ships with this connection already configured, and no login is needed. This fits the empty user and password at `Config.xml:42,44` (VERIFIED), but the file doesn't prove it.
- **UNVERIFIED, and I'm not confident:** I have a weak recollection that NinjaTrader has wound down or rebranded Kinetick in recent years. I can't confirm whether the service still answers connections in October 2026. **Treat this as an open question, not a fact.**
- **UNVERIFIED:** whether Kinetick EOD can serve a continuous `NQ ##-##` series, or serves NQ futures daily bars at all.

---

## Q2. What has PRAXIS recorded about it?

No document records **anyone setting Kinetick up, or Amear making any decision about it**, before 2026-10-20. The one Amear statement in the record is the "undecided" ruling of 2026-10-20. Search evidence is under "Searches run" (S1, S8, S9).

| Date | Who (as recorded) | What | Citation | Label |
|---|---|---|---|---|
| 2026-07-09 | B1-0 report: "trader-executed. Findings transcribed to repo by the orchestrator" (`:6`) | Says the chart data was "real-time … via NinjaTrader's bundled Kinetick feed", and "Data feed was real-time Kinetick via the `amear238` NT login (cached token)" | `docs/reports/2026-07-09-b1-0-nt8-parallels-validation.md:82`, `:164` | REPORTED; contradicted (C1) |
| 2026-07-10 | runbook | Prerequisite: "connected (Simulated Data Feed or Kinetick login is fine…)" | `docs/runbooks/2026-07-10-b1f-nt8-consumer-install.md:13` | REPORTED |
| 2026-07-12 | VM run report | "Only three connections exist in Config.xml — Simulated Data Feed, Playback Connection, Kinetick End Of Day (Free). No live brokerage is configured on this install." | `docs/reports/2026-07-12-b1f-t1-t4-vm-run-blocked.md:71-72` | REPORTED (consistent with the rescue Config.xml today, VERIFIED) |
| 2026-07-15 | Block 2 scope **PROPOSAL** | Kinetick listed as one data-source option; the proposal names "NT8 default provider or Kinetick" for deep minute history | `docs/specs/2026-07-15-block2-backtesting-scope-proposal.md:46`, `:49` | REPORTED (proposal only) |
| 2026-07-15 | **Amear's Block 2 data decision** (D-2026-07-15-B, Q4) | "NT8 default-provider MINUTE history — no paid-data budget this block." **Kinetick isn't named** | `DECISIONS.md:184` | REPORTED. INFERRED: paid Kinetick minute data was not chosen |
| 2026-07-24 | coworker capture of 20 screenshots | Connections: Kinetick EOD listed with no dot; Simulated Data Feed "[green dot = currently connected]" | `docs/reference/assets/nt8-2026-07-24/00-coworker-capture-notes.txt:51-53`, `:184-185`; reference `:25`, `:33` | REPORTED (the screenshot was VERIFIED by the a20 manager and auditors, per walkthrough `:30`) |
| 2026-07-24 | in-VM agent status (outside repo) | `db\minute\NQ 12-25\` described as "pre-existing Kinetick-sourced data" | `/Users/admin/praxis-signals/b2-data/inbound/4uu-VM-status-2026-07-24.md:56-57` | REPORTED; no source given for "Kinetick-sourced" (C2) |
| 2026-07-25 | in-VM agent status (outside repo) | Warns that a mislabelled `NQ 12-25.txt` "will contaminate genuine Kinetick `NQ 12-25` contract data" | `…/inbound/4uu-VM-status-2026-07-25.md:95-98` | REPORTED (C2) |
| 2026-07-25 | wx7 build progress | "all 44 raw export files … were pulled from NT8's default data provider … No paid data was purchased" | `docs/reports/2026-07-25-wx7-build-progress-for-scoping-agent.md:105`, `:187-190` | REPORTED |
| 2026-08-29 | session 52 NQCONT investigation | Quotes reference `:186`. Calls the native `NQ 12-25` data "real Kinetick data" | `docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:46-48`, `:235-236` | REPORTED (C2) |
| 2026-08-29 | session 52 voice walkthroughs v1/v2 | "native `NQ 12-25` (this has real Kinetick data)", used for a 2026-07-17 comparison chart | `…session52-nt8-voice-walkthrough.md:144`; `…-v2.md:211-212` | REPORTED; contradicted by the data folder (C3) |
| 2026-08-29 | in-VM capture (outside repo) | "**Kinetick – End Of Day (Free)** — listed, not connected (no green dot, no 'disconnect' option shown for it)." | `/Users/admin/praxis-signals/b2-data/inbound/4uu-VM-capture-2026-08-29.md:172-173` | REPORTED |
| 2026-08-29 | session 53 corpus reads | An EOD feed has no intraday minute bars (`:418`). Provider-support question "not recorded" (`:431`). W4: "nobody here has connected it" (`:270-271`). W1: "Kinetick" (the data vendor) (`:368`) | files as cited | REPORTED |
| 2026-08-29 | DECISION_LOG (master) | Re-runs a grep that includes "Kinetick" as part of auditing `vu8`. Not a Kinetick decision | `DECISION_LOG.md:381` | REPORTED |
| 2026-09-29 | praxis-master, migration reply | Item 13: "Connections as before, and nothing more: Simulated Data Feed; Kinetick EOD configured." Not graded when written (`:7`) | `docs/reports/2026-09-29-vm-migration-concerns.md:121-122` | REPORTED (master's request to the migration agent, **not an Amear ruling**) |
| 2026-10-19 | update 2 from migration | "Kinetick EOD: NOT YET KNOWN"; listed as "Still owed inside NT8" | `docs/reports/2026-10-19-windows-vm-state-update-2-from-migration.md:67`, `:120` | REPORTED |
| 2026-10-20 | praxis-master / Amear | Bead a20 filed for the Fusion TZ and Kinetick reads; dispatch approved by Amear | `DECISION_LOG.md:411`, `:415` | REPORTED |
| 2026-10-20 | Amear (reads) | "Kinetick – End Of Day (Free), no dot." "Kinetick - End Of Day row: present, no dot." Mapped to K1 | `docs/reports/2026-10-20-a20-results.md:21-22`, `:45`; `DECISION_LOG.md:423` | REPORTED |
| 2026-10-20 | **Amear** | "**Kinetick EOD (K1): undecided.** Amear: 'i dont know what that is or i dont remeber. look into it'." | `DECISION_LOG.md:424` | REPORTED. **The only Amear decision on record about Kinetick** |
| 2026-10-20 | praxis-master | Dispatches this research | `DECISION_LOG.md:425` | REPORTED |

**What was it used for?** No recorded use. It was **not** the Block 2 source (the decision names the "default provider", `DECISIONS.md:184`). It was **not** part of the NQCONT import: NQCONT is a file import of PRAXIS's own stitched CSV (wx7 `:105-106`). It was **not** shown connected in any capture (2026-07-24, 2026-08-29, 2026-10-20). The only claims of use are C1 and C2, and both are contradicted.

---

## Q3. Does anything in PRAXIS depend on Kinetick being connected?

**Finding: nothing found that depends on it.** Each claim below is settled by a search pasted under "Searches run".

| Area | Dependency on Kinetick? | Evidence | Label |
|---|---|---|---|
| Live signal path (n8n workflows, file drop, NinjaScript consumer) | **None found** | S4, S5, S6: zero hits for kinetic / EOD / end of day / Provider7 / data feed / historical data in `src ninjascript n8n-workflows workflows scripts config deploy signals tests`. No `BarsRequest`, `AddDataSeries`, `ConnectOnStartup` or `Provider` in the NinjaScript | VERIFIED (search). INFERRED that "no mention means no dependency": the strategies run on whatever connection feeds the chart, which today is the Simulated Data Feed |
| Backtesting (Block 2) | **None found** | `DECISIONS.md:184` (default-provider minute history, no paid data). Old logs show the NinjaTrader Historical Data Server, not Kinetick (S10) | REPORTED + VERIFIED (log lines) |
| NQCONT import | **None found** | NQCONT is imported from a file (wx7 `:105-106`). Zero code hits (S4) | REPORTED + VERIFIED (search) |
| NQCONT "unknown instrument" defect | **The record does not tie Kinetick to it** | S12: wherever both appear, they are separate topics. Walkthrough `:183`: "This doesn't touch the NQCONT 'unknown instrument' error. That's a separate defect". The defect is explained as a name mismatch (`DECISION_LOG.md:363`: storage `NQCONT` vs request `NQCONT 09-2025`) | REPORTED. **Gap:** session 53 `:431` notes that whether Kinetick could serve a continuous series "is not recorded"; that is a question about continuous contracts in general, not a cause recorded for this defect. I did not try to solve the defect |
| Outside-repo code (`~/praxis-signals`) | **None found** | S7: the only hits are `.md` briefs and status files. The outside `ninjascript/` folder has no hit | VERIFIED (search) |
| The "native NQ 12-25" control chart in the session 52 walkthroughs | Leans on the phrase "real Kinetick data", but needs no Kinetick connection, and the data isn't there for that date | C3 below | VERIFIED (folder listing) |

---

## Q4. Amear's options (the decision is Amear's; nothing here is decided)

The evidence for each option's effects is thin. Most of it is UNVERIFIED general NT8 knowledge.

| Option | What it touches | Risk / what's known |
|---|---|---|
| **A. Leave it as it is (listed, not connected)** | Nothing | Matches the old install as found (`Config.xml:34` VERIFIED; 07-24 and 08-29 captures REPORTED). INFERRED: no PRAXIS function loses anything (Q3). The Fusion setting itself is **not verified** (see Gaps) |
| **B. Connect by hand only when needed** | The Connections menu, a network connection to Kinetick | **UNVERIFIED:** it would contact Kinetick's servers and could download daily bars into NT8's local data store (old store had a `db/day` folder, VERIFIED). **UNVERIFIED:** whether the service still works in 2026. **UNVERIFIED:** whether it would change which provider NT8 uses for daily data on NQ charts. VERIFIED context: `MultiProvider` is `true` (`Config.xml:208`) and every `Preferred…Connection` is `Unknown` (`Config.xml:109`, `:116`), so NT8 is set up to allow more than one connection at once, with no preferred provider pinned. INFERRED from those names: two live data connections would both be eligible to supply data, which is why the effect is uncertain |
| **C. Connect at startup** | `ConnectOnStartup` in Fusion's Config.xml (an NT8 settings change) | Same as B, every launch. It also changes a setting that has been `false` since at least 2026-07-12 (VERIFIED as of the 08-29 Config.xml). It breaks the "Connections as before, and nothing more" principle (`2026-09-29-vm-migration-concerns.md:121`, master's, REPORTED) and Amear's D-071 condition "no other connection" (update 2 `:67`, REPORTED) |
| **D. Remove the connection** | NT8's connection list (Config.xml) | **UNVERIFIED:** whether it can be added back easily. INFERRED: it gains nothing for PRAXIS (Q3), and it is a configuration change on a faithfully restored install |

**Interference questions:**
- **With Rithmic:** **no Rithmic connection exists** on the old install (`2026-09-29-vm-migration-concerns.md:122`, REPORTED; the Config.xml connection list at `:15-65` has only Simulator, Kinetick and Playback, VERIFIED). Fusion lists four rows and no Rithmic (`a20-results.md:21`, REPORTED). Kinetick EOD is data-only (UNVERIFIED), so there is nothing for it to interfere with today. Future live Rithmic interplay: **UNVERIFIED**.
- **With the Simulated Data Feed:** **UNVERIFIED.** The only machine evidence is the multi-provider setting above. Nobody in the record has ever connected Kinetick alongside it (w4 `:270-271`, REPORTED; no Kinetick connect line in any surviving log, VERIFIED S9).
- **Orders:** `CanManageOrders` reads `true` in the Kinetick block (`Config.xml:33`, VERIFIED). It reads `true` in the Playback block too (`:52`), so it looks like a generic field (INFERRED). Whether Kinetick EOD can route orders: **UNVERIFIED** (general knowledge says no). Orders go to Sim accounts regardless.

### PRAXIS view (reasoning, not a decision)

INFERRED, resting on Q3 and the Config/log evidence: nothing in PRAXIS needs Kinetick, and it has never been seen connected. So **A (leave it off)** changes nothing and carries no new risk. B, C and D each change something on a faithfully restored install for no recorded benefit. If Amear ever wants free daily bars from it, B is the reversible way to try. **Amear decides.**

---

## Config.xml excerpt (old install, rescue copy)

Both rescue copies are byte-identical (same sha256). This is the **Parallels** install as of the file's mtime, 2026-08-29. It is **not** Fusion.

```
$ ls -la ".../NinjaTrader 8/Config.xml"; shasum -a 256 ...   (both copies)
-rw-r--r--@ 1 admin  staff  16879 Aug 29 12:00 /Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8/Config.xml
7a040a1106eb6c674b0cb17c70132cdfc6cf64453dcc8f564f63514feee0edf6  /Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8/Config.xml
-rw-r--r--@ 1 admin  staff  16879 Aug 29 12:00 /Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/Config.xml
7a040a1106eb6c674b0cb17c70132cdfc6cf64453dcc8f564f63514feee0edf6  /Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/Config.xml

$ grep -n -i -B3 -A3 kinetick "/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8/Config.xml"
29-      <TicksPerSecond>2</TicksPerSecond>
30-      <TimerMilliseconds>500</TimerMilliseconds>
31-    </SimulatorOptions>
32:    <KinetickOptions>
33-      <CanManageOrders>true</CanManageOrders>
34-      <ConnectOnStartup>false</ConnectOnStartup>
35-      <DisableL2Data>false</DisableL2Data>
36-      <IsHdsEnabled>false</IsHdsEnabled>
37-      <IsPasswordRequiredOnStartup>false</IsPasswordRequiredOnStartup>
38-      <RunAsProcess>false</RunAsProcess>
39:      <TypeName>NinjaTrader.Cbi.KinetickOptions</TypeName>
40-      <Mode>Live</Mode>
41:      <Name>Kinetick – End Of Day (Free)</Name>
42-      <Password />
43-      <Provider>Provider7</Provider>
44-      <User />
--
47-      <Free>true</Free>
48-      <NewsDaysBack>1</NewsDaysBack>
49-      <UseFundamentalData>true</UseFundamentalData>
50:    </KinetickOptions>
51-    <PlaybackOptions>
52-      <CanManageOrders>true</CanManageOrders>
53-      <ConnectOnStartup>false</ConnectOnStartup>
--
238-      <BrushDownPrimarySerializeKo>&lt;SolidColorBrush xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"&gt;#FF115BCB&lt;/SolidColorBrush&gt;</BrushDownPrimarySerializeKo>
239-      <BrushDownSecondarySerializeKo>&lt;SolidColorBrush xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"&gt;#FF4682B4&lt;/SolidColorBrush&gt;</BrushDownSecondarySerializeKo>
240-      <CurrentUICultureSerializable>en-US</CurrentUICultureSerializable>
241:      <KinetickGlobexNonProFees>false</KinetickGlobexNonProFees>
242-      <LogsLoaded>1000</LogsLoaded>
243-      <Name>General</Name>
244-      <PromptLanguageWarningForBasicEntry>false</PromptLanguageWarningForBasicEntry>
```
(The `-full` copy gave identical output.) Lines 45-46 fall in the gap between the grep windows. Here they are, with the startup flags of the other connections and the multi-provider settings:

```
$ cat -n Config.xml | sed -n 15,18p; sed -n 25p; sed -n 45,46p; sed -n 60p; sed -n 102p; sed -n 109p; sed -n 116p; sed -n 208p   (excerpted from the run)
    15	  <ConnectOptions>
    16	    <SimulatorOptions>
    17	      <CanManageOrders>true</CanManageOrders>
    18	      <ConnectOnStartup>true</ConnectOnStartup>
    25	      <Name>Simulated Data Feed</Name>
    45	      <GlobexNonProFees>false</GlobexNonProFees>
    46	      <BackadjustContinuousContracts>false</BackadjustContinuousContracts>
    60	      <Name>Playback Connection</Name>
   102	      <GetDataFromServer>true</GetDataFromServer>
   109	      <PreferredFutureConnection>Unknown</PreferredFutureConnection>
   116	      <PreferredRealtimeFutureConnection>Unknown</PreferredRealtimeFutureConnection>
   208	      <MultiProvider>true</MultiProvider>
```
`ConnectOptions` (`:15-65`) contains exactly three blocks: `SimulatorOptions`, `KinetickOptions` and `PlaybackOptions`. There is no Rithmic block and no "Simulation" block.

**Fusion-side config readable from the Mac? No.** Nothing NT8-related on the Mac is newer than the rescue copy, and no VMware share is mounted. I did not try to reach the VM.
```
$ find ~ -maxdepth 6 -iname "Config.xml" -path "*inja*" 2>/dev/null
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8/Config.xml
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/Config.xml
$ find ~ -maxdepth 6 -type d -iname "NinjaTrader 8*" -newermt 2026-10-18 2>/dev/null
exit=0
$ mount | grep -i -E "vmware|hgfs|fusion"
exit=1
```
This matches the master's 15:55:42Z observation that the Fusion `.vmx` has no shared folder (`DECISION_LOG.md:424`, REPORTED).

---

## Searches run

Note: `grep` in this shell is a function wrapping **ugrep** (`type grep` → "grep is a shell function from …/shell-snapshots/snapshot-zsh-…sh"). One early search failed because zsh doesn't split `$D`, and ugrep reported `No such file or directory, exit=2`. **That run is discarded.** The runs below name their directories explicitly.

**S1. Every Kinetick mention, repo-wide (25 files)**
```
$ grep -rliI kinetick --exclude-dir=.git . | wc -l
      25
```
The full `grep -rinI kinetick` listing (about 120 lines) was read in full. Every line cited in Q2 comes from it.

**S2. Spelling variant "kinetic" not followed by k**
```
$ grep -rnoiI "kinetic[^k]\|kinetic$" --exclude-dir=.git .
exit=1
```

**S3. Phrase variants, repo-wide**
```
$ grep -rniI "end of day" --exclude-dir=.git . | grep -vi kinetick | cut -c1-250
docs/reports/2026-08-29-session53-nqcont-resolution-and-rth-corpus-read.md:418:An **End Of Day** feed does not supply intraday minute bars. A1's decision rule reads control
$ grep -rniIw "EOD" --exclude-dir=.git . | grep -vi kinetick | cut -c1-250
DECISION_LOG.md:351:- [2026-08-29T00:30:00Z] WHO: praxis-master (session 52) | WHAT: **MASTER'S ERROR, RECORDED NOT ABSORBED — THE MASTER TOLD AMEAR THE STRATEGY'S EDGE LIVES AT A BAND-EDGE CROSS AND THAT INTRABAR ORDERING IS THEREFORE THE F3 DAMAGE 
specs/SPEC_RUBRIC.md:36:shortlist recorded the source strategy as EOD-flat while Phase 2 closure and
docs/reference/2026-07-24-nt8-windows-reference.md:150:4. **Time frame:** **Start date** / **End date** · **Trading hours** = **session template dropdown** — for PRAXIS RTH select **"CME US Index Futures RTH"** · **Break at EOD**.
docs/reports/2026-08-29-session53-w3-q3-rth-timezone.md:136:150:4. **Time frame:** **Start date** / **End date** · **Trading hours** = **session template dropdown** — for PRAXIS RTH select **"CME US Index Futures RTH"** · **Break at EOD**.
docs/reports/2026-08-29-session52-nt8-voice-walkthrough-v2.md:309:- Break at EOD → leave default
docs/reports/2026-08-06-session42-r8j-phase3-import.md:682:< 	6.	Trailing drawdown proximity — account approaches MFFU’s $1,500 EOD trailing drawdown → reduce size or halt
docs/reports/2026-08-06-session42-r8j-phase3-import.md:685:> 	6.	Trailing drawdown proximity — account approaches MFFU's $1,500 EOD trailing drawdown → reduce size or halt
docs/reports/2026-08-06-session42-r8j-phase3-import.md:730:7:	6.	Trailing drawdown proximity — account approaches MFFU’s $1,500 EOD trailing drawdown → reduce size or halt
docs/reports/2026-08-29-session52-handoff-planning-chat.md:70:- exits `:211` / `:219` also below the gate; `:288` / `:290` are EOD-flat
docs/reports/2026-08-29-session52-handoff-planning-chat.md:75:`HH:30` and EOD flat. Intrabar path ordering cannot affect its fills.
$ grep -rniI "data provider\|historical data provider\|EOD feed" --exclude-dir=.git . | cut -c1-260
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:53:series the *data provider* assembles and serves. It is **not a container you can
docs/reports/2026-08-07-f3-fill-resolution-research-UNGRADED.md:54:  send a request to your data provider for 1-tick data."* With no tick data, the
docs/reports/2026-07-25-wx7-build-progress-for-scoping-agent.md:105:- **Raw data landed:** all 44 raw export files (22 daily + 22 one-minute contracts) were pulled from NT8's default data provider inside the VM and delivered to a shared folder. **No paid data 
exit=0
```
None of the non-Kinetick "EOD" hits is about a data feed. They are about "Break at EOD", EOD-flat exits, and MFFU's EOD drawdown.

**S4. Code directories: inventory and Kinetick/feed terms**
```
$ find src ninjascript n8n-workflows workflows config deploy signals -type f
signals/signal-template.json
signals/signal-template.README.md
signals/.gitkeep
config/b2-stitch-schema.json
config/backtest-cost-model.json
deploy/launchd/build.praxis.signals-stale-check.plist
deploy/launchd/build.praxis.signals-backlog-check.plist
deploy/launchd/build.praxis.signals-sweep-daemon.plist
deploy/launchd/build.praxis.b2data-watch.plist
deploy/launchd/build.praxis.tg-inbound.plist
src/.DS_Store
ninjascript/PraxisSignalConsumer.cs
ninjascript/PraxisNoiseAreaBreakout.cs
workflows/EmMbN4sslwIx1ydn.before-b1-b.json
workflows/praxis-telegram-inbound-control.json
workflows/EmMbN4sslwIx1ydn.after-b1-b.json
workflows/EmMbN4sslwIx1ydn.before-qxd.json
workflows/EmMbN4sslwIx1ydn.after-qxd.json
$ grep -rniIw "eod" src ninjascript n8n-workflows workflows scripts config deploy signals tests
exit=1
$ grep -rniI "kinetic" src ninjascript n8n-workflows workflows scripts config deploy signals tests
exit=1
$ grep -rniI "end of day\|endofday\|provider7\|data feed\|datafeed\|historical data" src ninjascript n8n-workflows workflows scripts config deploy signals tests
exit=1
```
(`n8n-workflows/` is empty. `scripts/` and `tests/` were searched by the commands above and also returned no hits. `find … | wc -l` over all of them gave 46 files.)

**S5. NinjaScript: data-connection hooks**
```
$ grep -rnI "BarsRequest\|AddDataSeries\|Connection\.\|ConnectOnStartup\|Provider\|##-##" ninjascript src
exit=1
```

**S6. Decision and top-level files**
```
$ grep -niI kinetick DECISIONS.md RUN_DECISIONS.md PATCH_NOTES.md README.md AGENTS.md
exit=1
```

**S7. Outside the repo (`~/praxis-signals`)**
```
$ grep -rliI kinetick /Users/admin/praxis-signals
/Users/admin/praxis-signals/b2-data/4uu-VM-brief.md
/Users/admin/praxis-signals/b2-data/inbound/4uu-VM-status-2026-07-25.md
/Users/admin/praxis-signals/b2-data/outbound/INSTRUCTIONS.md
/Users/admin/praxis-signals/b2-data/inbound/4uu-VM-status-2026-07-24.md
/Users/admin/praxis-signals/b2-data/inbound/4uu-VM-capture-2026-08-29.md
/Users/admin/praxis-signals/b2-data/inbound/nt8-layout-2026-07-24/00-notes.txt
/Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md
/Users/admin/praxis-signals/b2-data/outbound/4uu-VM-brief-v3.md
/Users/admin/praxis-signals/archive/b1f-t1-t4-report-2026-07-12.md
/Users/admin/praxis-signals/vm-agent/reference/nt8-windows-reference.md
exit=0
$ ls /Users/admin/praxis-signals/b2-data/ninjascript
PraxisNoiseAreaBreakout.cs
PROVENANCE.txt
```
Every hit is a `.md` or `.txt` brief, note or status file. No code file mentions Kinetick.

**S8. Old NT8 logs: any Kinetick line?** (rescue `NinjaTrader 8-full/log`, 2026-08-15 to 08-29. Older logs were purged, per `DECISION_LOG.md:393`, REPORTED)
```
$ grep -c -i -a kinetick log/*.en.txt
log.20260815.00000.en.txt:0
log.20260815.00001.en.txt:0
log.20260817.00000.en.txt:0
log.20260816.00000.en.txt:0
log.20260818.00000.en.txt:0
log.20260828.00000.en.txt:0
log.20260829.00000.en.txt:0
log.20260829.00001.en.txt:0
```

**S9. Old NT8 logs: which connections actually connected**
```
$ grep -h -a "Auto connecting\|: Primary connection=Connected" log/*.en.txt | sort | uniq -c
   3 Auto connecting 'Simulated Data Feed'...
   3 Simulated Data Feed: Primary connection=Connected, Price feed=Connected
```

**S10. Old NT8 logs: where historical data came from**
```
$ grep -h -a -i "connect" log/*.en.txt | cut -c1-220 | sort | uniq | head -25   (first 7 shown)
2026-08-15 10:12:01:190|1|4|Auto connecting 'Simulated Data Feed'...
2026-08-15 10:12:01:379|1|2|Simulated Data Feed: Primary connection=Connecting, Price feed=Connecting
2026-08-15 10:12:01:476|1|2|Simulated Data Feed: Primary connection=Connected, Price feed=Connected
2026-08-16 08:07:33:743|3|2|Connection lost to the NinjaTrader Historical Data Server: hds-us-nt-020.ninjatrader.com
2026-08-16 08:07:44:040|1|2|Connection restored to the NinjaTrader Historical Data Server: hds-us-nt-012.ninjatrader.com
2026-08-17 10:32:16:485|3|2|Connection lost to the NinjaTrader Historical Data Server: hds-us-nt-012.ninjatrader.com
2026-08-17 10:32:26:661|1|2|Connection restored to the NinjaTrader Historical Data Server: hds-us-nt-019.ninjatrader.com
$ grep -h -a -o "Historical Data Server: [a-z0-9.-]*" log/*.en.txt | wc -l
      26
```

**S11. Old NT8 traces: the only Kinetick mentions** (one per file, in 3 of 9 trace files)
```
== trace.20260815.00001.txt
23:2026-08-15 10:11:52:447 Cbi.UserEntitlement.VerifyAsync.99: subscription=Free licensedProviders='Playback Simulator NinjaTrader NinjaTrader Continuum NinjaTrader FXCM IQFeed E-Signal External FOREX.com Interactive Brokers Barchart.com Kinetick FXCM Coinbase cTrader Schwab Rithmic for NinjaTrader 
count: 1
== trace.20260829.00000.txt
25:2026-08-29 09:28:16:290 Cbi.UserEntitlement.VerifyAsync.99: subscription=Free licensedProviders='Playback Simulator … Kinetick … Rithmic for NinjaTrader 
count: 1
== trace.20260829.00001.txt
23:2026-08-29 11:02:37:257 Cbi.UserEntitlement.VerifyAsync.99: subscription=Free licensedProviders='Playback Simulator … Kinetick … Rithmic for NinjaTrader 
count: 1
```
(The output was cut at 300 characters per line by `cut -c1-300`. In the last two entries, "…" marks provider names I left out; the first entry is complete as far as the cut.)

**S12. NQCONT defect vs Kinetick: line positions in files that mention both**
```
== STATUS.md  kinetick@ 13   unknown-instrument@ 7 
== DECISION_LOG.md  kinetick@ 381 411 415 418 419 423 424 425   unknown-instrument@ 363 393 395 
== docs/reports/2026-08-29-session53-nqcont-resolution-and-rth-corpus-read.md  kinetick@ 413 414 415 428 431   unknown-instrument@ 401 
== docs/reports/2026-08-29-session52-nt8-voice-walkthrough-v2.md  kinetick@ 212   unknown-instrument@ 76 
== docs/reports/2026-08-29-session53-w4-adversarial-q4-designs.md  kinetick@ 256 257 258 263 270   unknown-instrument@ 35 36 37 39 40 45 46 47 48 49 50 51 62 106 108 109 
== docs/reports/2026-08-29-session53-w1-q1-import-instructions.md  kinetick@ 368 375 379 381 385 387 391   unknown-instrument@ 124 437 
== docs/reports/2026-10-19-windows-vm-state-update-2-from-migration.md  kinetick@ 67 120   unknown-instrument@ 29 63 72 
== docs/reports/2026-10-20-a20-voice-handoff.md  kinetick@ 4 57 97   unknown-instrument@ 115 
```
I read the Kinetick lines in each file (Q2 table). None names Kinetick as a cause of, or a fix for, the unknown-instrument error. The closest is session 53 `:428-432`, which flags as unrecorded whether Kinetick EOD can serve a continuous contract. Walkthrough `:183`, read this run: "This doesn't touch the NQCONT "unknown instrument" error. That's a separate defect, reported to reproduce on Fusion, and still open. Nothing here requests bars."

**S13. The "native NQ 12-25 has Kinetick data" control: what is actually stored** (rescue data folder)
```
== NinjaTrader 8/db/minute/NQ 12-25
      90
20250911.Last.ncd
20251221.Last.ncd
0                     <- files whose name starts with 2026
== NinjaTrader 8-full/db/minute/NQ 12-25
      90
20250911.Last.ncd
20251221.Last.ncd
0
$ ls -la ".../db/minute/NQ 12-25" | head -5
drwxr-xr-x@ 92 admin  staff   2944 Jul 21 12:46 .
-rw-r--r--@  1 admin  staff   4960 Jul 21 12:46 20250911.Last.ncd
```

**S14. Tracked status of the Kinetick files**
```
$ git status --porcelain -- $(grep -rliI kinetick --exclude-dir=.git .)
MM DECISION_LOG.md
?? docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md
?? docs/reports/2026-08-29-session52-nt8-voice-walkthrough.md
?? docs/reports/2026-08-29-session53-nqcont-resolution-and-rth-corpus-read.md
?? docs/reports/2026-08-29-session53-w1-q1-import-instructions.md
?? docs/reports/2026-08-29-session53-w4-adversarial-q4-designs.md
?? docs/reports/2026-10-20-a20-results.md
?? docs/reports/2026-10-20-a20-voice-handoff.md
```
Seven of the cited files are untracked, and `DECISION_LOG.md` lines 423-425 are in the uncommitted worktree. Their line numbers may move.

---

## Contradictions in the record

- **C1. "Real-time Kinetick feed" (07-09) vs "nobody here has connected it" (08-29).** B1-0 `:82` and `:164` say the chart data was real-time via Kinetick through the `amear238` login. Against that: w4 `:270-271` says "nobody here has connected it"; Kinetick is set `ConnectOnStartup false` (`Config.xml:34`, VERIFIED as of 08-29); every capture shows it unconnected; and the logs show only the Simulated Data Feed auto-connecting (S9). `amear238` is the **NinjaTrader account** login (`Config.xml:66` `<Username>amear238</Username>`, VERIFIED), not a Kinetick credential (Kinetick `<User />` is empty, `:44`). INFERRED: B1-0 probably took the NT account plus the Simulated Data Feed for Kinetick. The 07-09 log isn't in the rescue copy, so this can't be settled (gap). B1-0 `:82` also says it is "the same data feed that will be used with Rithmic in production", which the record nowhere supports.
- **C2. "Kinetick-sourced" NQ contract history vs "NT8 default data provider".** The 07-24 and 07-25 VM status files, session 52 investigation `:236` and the 4uu briefs call the native `NQ 12-25` data "Kinetick". wx7 `:105` and `DECISIONS.md:184` call the source "NT8's default data provider". The only machine evidence (logs from 08-15 onward) shows the **NinjaTrader Historical Data Server** (S10), with `GetDataFromServer true` (`Config.xml:102`). The data was written 2026-07-21 (S13), and logs from that day are gone, so the true source is **unverified**. Nothing in the record supports "Kinetick".
- **C3. A control chart that can't work as written.** Session 52 walkthroughs v1 `:144` and v2 `:211-212`, and the 4uu briefs (`4uu-VM-brief-v3.md:255`), tell Amear to compare against "native `NQ 12-25` (has real Kinetick data)" on **2026-07-17**. `NQ 12-25` is the December 2025 contract, and the stored minute files run 2025-09-11 to 2025-12-21 with no 2026 file (S13, VERIFIED). INFERRED: that chart would have had no bars for 2026-07-17, whatever the provider. Reported here, not fixed; it's outside this brief.
- **C4. Wording drift on "connected".** Walkthrough `:30` labels "no dot = not connected" INFERRED from the legend. The 08-29 in-VM capture states it as OBSERVED ("not connected (no green dot, no 'disconnect' option)", `4uu-VM-capture-2026-08-29.md:172-173`). Both describe the same appearance. The capture's extra evidence is the missing "disconnect" link.
- **C5. "Connections as before" vs the Fusion list.** The master's migration item 13 (`2026-09-29-vm-migration-concerns.md:121`) lists "Simulated Data Feed; Kinetick EOD configured". The old Config.xml has no "Simulation" connection block (VERIFIED), yet "Simulation" appears in both the old menu (capture `:54`) and the Fusion menu. INFERRED: "Simulation" is a built-in entry, not a stored connection. It bears on K5/K8, which Amear has already ruled on (`DECISION_LOG.md:424`).

---

## Gaps / unknowns

1. **Fusion's own Kinetick setting is unread.** No Fusion-side config is readable from the Mac (see above). INFERRED: it is `ConnectOnStartup false`. That rests on (a) the faithful restore from `NinjaTrader 8-full` (update 2 `:62`, REPORTED) and (b) that copy's Config.xml being byte-identical to the one read here (VERIFIED). Whether the restore actually overwrote Fusion's fresh Config.xml is not recorded (update 2 `:70`, REPORTED).
2. **Product facts about Kinetick EOD** (data type, coverage, whether it serves NQ futures or continuous contracts, whether the service still runs in 2026) are all **UNVERIFIED**. I had no web tool. A read-only check of NinjaTrader's own help pages would settle them.
3. **What connecting it would do** to the Simulated Data Feed, or to the provider NT8 chooses for daily NQ data: **UNVERIFIED**. No one in the record has ever connected it.
4. **Source of the old contract history before 2026-08-15** (C2): unverifiable from the rescue copy, because the logs were purged.
5. **Who added the connection, and when:** no record. UNVERIFIED that it ships with NT8 by default.
6. **The NQCONT defect** was not investigated, per the brief. Only its absence of a recorded Kinetick tie is reported.

---

## Process log

1. `grep -rinI kinetick` repo-wide (S1), then read every cited passage with `sed -n`.
2. Read the rescue Config.xml (both copies, hashed), the old logs and traces, and the `NQ 12-25` data folder.
3. Searched the code directories, decision files, variants and the outside `~/praxis-signals` tree (S2-S7).
4. Checked file provenance (`git log --diff-filter=A`) and tracked status (S14).
5. Looked for Fusion-side config on the Mac (none). No VM access was attempted.

## Verification evidence

All pasted above, under "Config.xml excerpt" and "Searches run" (S1-S14).

## Files staged

**None.** One new untracked file was written: `docs/reports/2026-10-20-a20-kinetick-research-worker1.md`. No `git add`, per the brief's hard limits.

## Result: PASS

Q1-Q4, the Config excerpt and the Fusion-readability check are answered, each to the level its evidence supports. Product facts stay UNVERIFIED because no web tool was available, and that is stated where it applies.
