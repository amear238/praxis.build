# Adversarial review A — a20 Kinetick research report (worker1)

- Task: break docs/reports/2026-10-20-a20-kinetick-research-worker1.md (citations, labels, contradictions C1–C5)
- Mode: ADVERSARIAL
- Criterion: specs/SPEC_RUBRIC.md:107-108 (S1 pasted output; S2 no claim stronger than evidence)
- Date: 2026-10-20

VERDICT: BROKEN (see foot)

## Findings

### F1. "Historical bars came from the NinjaTrader Historical Data Server (VERIFIED in the logs)" — artifact line 17
- Defect: wrong-label. The logs (S10, artifact 322-331) show only connection lost/restored events to the HDS host. They do not show any bar request being served or by whom. "Historical bars came from" is a statement about NT8 data-sourcing behaviour, so it is INFERRED from connection events plus `GetDataFromServer true`. It is not VERIFIED. The artifact's own C2 (line 397) is more careful ("true source is **unverified**"). So line 17 contradicts the report's own C2.
- Evidence: artifact S10 excerpt, as pasted by the artifact:
```
2026-08-16 08:07:33:743|3|2|Connection lost to the NinjaTrader Historical Data Server: hds-us-nt-020.ninjatrader.com
2026-08-16 08:07:44:040|1|2|Connection restored to the NinjaTrader Historical Data Server: hds-us-nt-012.ninjatrader.com
```
  No line says bars were downloaded.
- Severity: MAJOR (S2, and it sits in the plain-language answer Amear reads first).
- Fix: "The logs show NT8 connected to the NinjaTrader Historical Data Server (VERIFIED). INFERRED: historical bars came from there."

### F2. "VERIFIED context: `MultiProvider` is `true` … so NT8 is set up to allow more than one connection at once, with no preferred provider pinned" — artifact line 105
- Defect: wrong-label. That the field holds `true` is VERIFIED. What the field *does* ("allow more than one connection at once") and what `Unknown` means ("no preferred provider pinned") are statements about NT8 config-field semantics. They are read off the field names and sit inside a "VERIFIED context" clause. The INFERRED label only starts at the *next* sentence.
- Evidence:
```
$ cat -n Config.xml | sed -n '100,118p;205,210p'
   109	      <PreferredFutureConnection>Unknown</PreferredFutureConnection>
   116	      <PreferredRealtimeFutureConnection>Unknown</PreferredRealtimeFutureConnection>
   208	      <MultiProvider>true</MultiProvider>
```
  Nothing in the file or the repo defines these fields.
- Severity: MAJOR (this is exactly the "what a config field DOES" class in scope, and it is the only machine basis offered for the interference risk in B, C and the Simulated Data Feed question).
- Fix: "VERIFIED: `MultiProvider` reads `true`, and every `Preferred…Connection` reads `Unknown`. INFERRED from the field names (meaning UNVERIFIED): NT8 allows several connections at once, and no preferred provider is pinned."

### F3. "a setting that has been `false` since at least 2026-07-12 (VERIFIED as of the 08-29 Config.xml)" — artifact line 106
- Defect: wrong-label / unsupported date. A file with mtime 2026-08-29 cannot verify its own state on 2026-07-12. The 07-12 report lists the three connections, but it says nothing about `ConnectOnStartup` or any startup setting.
- Evidence:
```
$ grep -n -i -e startup -e kinetick docs/reports/2026-07-12-b1f-t1-t4-vm-run-blocked.md
72:   Kinetick End Of Day (Free). No live brokerage is configured on this install.
```
  (`startup` gets zero hits.) The artifact's own Config excerpt has mtime `Aug 29 12:00`.
- Severity: MAJOR (S2: a date bound stated as VERIFIED with no evidence behind it).
- Fix: "`false` in the 08-29 Config.xml (VERIFIED). Its earlier history is unrecorded. The connection has existed since at least 07-12 (REPORTED, `2026-07-12-b1f-t1-t4-vm-run-blocked.md:71-72`)."

### F4. "Orders go to Sim accounts regardless." — artifact line 112
- Defect: wrong-label (none given). This is an unlabelled statement about NT8 order routing. The closest record is the runbook (`2026-07-10-b1f-nt8-consumer-install.md:13`: "orders will go to the internal Sim account"), and the artifact does not cite it here. "Regardless" goes beyond even that.
- Evidence: artifact line 112 text, as quoted above. The runbook line was printed this run:
```
1. **TRADER-TOUCH** — VM running, NT8 launched, connected (Simulated Data Feed or Kinetick login is fine; orders will go to the internal Sim account).
```
- Severity: MINOR (there is a record basis, and the item is outside the decision itself). Still, it is an order-routing claim in a trading system with no label.
- Fix: "REPORTED (runbook `:13`): orders go to the internal Sim account. Whether that holds with Kinetick connected: UNVERIFIED."

### F5. "the screenshot was VERIFIED by the a20 manager and auditors, per walkthrough `:30`" — artifact line 63
- Defect: wrong-citation (embellished). Walkthrough :30 says "VERIFIED by PRAXIS today: the screenshot". It names neither a manager nor auditors.
- Evidence:
```
=== docs/reports/2026-10-20-a20-fusion-tz-kinetick-walkthrough.md:30
| P8 | Old install: Kinetick EOD showed **no dot** on 2026-07-24 (VERIFIED, screenshot). ... | VERIFIED by PRAXIS today: the screenshot, and `ConnectOnStartup` `false` in the old `Config.xml` line 34. **Old install only** |
```
- Severity: MINOR.
- Fix: "(the walkthrough records the screenshot as VERIFIED by PRAXIS, `:30`)".

### F6. "As far as I know it comes pre-loaded in NT8 … **The record backs that up: nobody in PRAXIS ever recorded setting it up**" — artifact line 16
- Defect: wrong-label (S2). An UNVERIFIED claim is presented as corroborated, and the only support is an *absence* of a record. Having no setup record does not show that NT8 ships the connection. The artifact's own Gap 5 (line 410) says "UNVERIFIED that it ships with NT8 by default", so line 16 and line 410 disagree.
- Evidence: artifact line 410: "**Who added the connection, and when:** no record. UNVERIFIED that it ships with NT8 by default."
- Severity: MINOR.
- Fix: "Nobody in PRAXIS recorded setting it up (REPORTED, absence of a record). That is consistent with it being pre-loaded, but it does not show it."

### F7. C1 lists post-dated machine evidence as "Against that" — artifact line 396
- Defect: wrong-contradiction (framing). The 07-09 claim is set against `Config.xml:34` (mtime 08-29) and the logs (08-15 onward, S9). Neither can contradict a 07-09 event, and `ConnectOnStartup false` does not rule out a connection made by hand. The only real opposing evidence is another REPORTED claim, w4 `:270-271`. The artifact does concede the gap ("07-09 log isn't in the rescue copy"), so this is a framing defect, not a false contradiction. C1 is real as a record-vs-record conflict.
- Evidence: rescue log inventory, this run: the earliest file is `log.20260815.00000.en.txt`. Config mtime is `Aug 29 12:00` (artifact line 126).
- Severity: MINOR.
- Fix: put the Config and log evidence under "consistent with, but post-dated", and keep w4 as the only direct counter-claim.

### F8. C2 "Nothing in the record supports 'Kinetick'" — artifact line 397
- Defect: other (universal negative stronger than its evidence). B1-0 `:82` and `:164` *are* record claims that the chart feed on this install was Kinetick. They are contested (C1), but they exist. The negative holds only once the artifact's own C1 inference is granted.
- Evidence:
```
=== docs/reports/2026-07-09-b1-0-nt8-parallels-validation.md:164
- **Data feed was real-time Kinetick via the `amear238` NT login** (cached token), ...
```
- Severity: MINOR.
- Fix: "No machine evidence supports 'Kinetick'. The only record support is B1-0's contested claim (C1)."

### C1–C5 assessment
- C1: real (B1-0 `:82`/`:164` vs w4 `:270-271`). Framing defect F7.
- C2: real (VM status 07-24 `:56-57`, 07-25 `:95-98`, s52 `:236` say "Kinetick". wx7 `:105` and DECISIONS.md:184 say "default provider"). Overstatement F8.
- C3: real. v1 `:142` "Open two charts, both for 2026-07-17" plus `:144`. v2 `:210` "**2026-07-17**" plus `:211-212`. Brief v3 `:255` holds. The folder runs `20250911` to `20251221`, 90 files, 0 starting `2026`, in both copies (re-run this run). NQ 12-25 expired in Dec 2025, so the inference holds whatever the provider. Minor citation looseness: the date sits at v1 `:142` and v2 `:210`, not at the cited `:144` / `:211-212`.
- C4: real and correctly described (walkthrough `:30` INFERRED legend; capture `:170` "OBSERVED, from the Connections menu:" and `:172-173`).
- C5: real but loosely put. Item 13 (`:121`) omits Playback and Simulation, while `:122` cites reference `:33`, which lists Simulation. Update 2 `:67` says "'Simulation' was in the old install's list (your 5.2 item 13)". The artifact does not name that specific conflict. No defect large enough to grade.

## Survived (checked this run, held)
1. L39/L58 B1-0 `:82`: "Data is real-time market data (via NinjaTrader's bundled Kinetick feed)…"
2. L58 B1-0 `:164`: "**Data feed was real-time Kinetick via the `amear238` NT login** (cached token)"
3. L59 runbook `:13`: "connected (Simulated Data Feed or Kinetick login is fine; …)"
4. L60 07-12 `:71-72`: "Only three connections exist in Config.xml — Simulated Data Feed, Playback Connection, / Kinetick End Of Day (Free)."
5. L34/L61 proposal `:46`: "| **Kinetick (NT8 native partner)** | EOD free; minute/tick paid | $ |"; `:49`: "(NT8 default provider or Kinetick)"
6. L62 **DECISIONS.md**:184 (right file; under D-2026-07-15-B header at :180): "**Q4 data:** NT8 default-provider MINUTE history — no paid-data budget this block." Kinetick has zero hits in DECISIONS.md.
7. L63 coworker notes `:51-53`: "Kinetick – End Of Day (Free) / Playback / Simulated Data Feed [green dot = currently connected]"; `:184-185` holds; reference `:25` and `:33` hold.
8. L38/L67 reference `:186` and s52 `:46-48`: "Requires **provider support** (historically Kinetick / eSignal / IQFeed)."
9. L64 outside repo 07-24 `:56-57`: "(pre-existing Kinetick-sourced data)"
10. L65 outside repo 07-25 `:95-98`: "it will contaminate genuine Kinetick `NQ 12-25` contract data"
11. L69 outside repo capture 08-29 `:172-173`: "**Kinetick – End Of Day (Free)** — listed, not connected (no green dot, no / "disconnect" option shown for it)."
12. L66 wx7 `:105`: "pulled from NT8's default data provider … **No paid data was purchased"; `:187-190` holds.
13. L67 s52 `:235-236`: "contaminating real Kinetick data with synthetic bars."
14. L68 v1 `:144`: "native `NQ 12-25` (this has real Kinetick data)"; v2 `:211-212` holds.
15. L35 s53 `:418`: "An **End Of Day** feed does not supply intraday minute bars."; L38 `:431-432`: "Whether Kinetick EOD Free satisfies that provider-support requirement is / not recorded."
16. L36 w4 `:270-271`: "**UNVERIFIED** whether Kinetick's free EOD tier serves / any intraday history at all — … nobody here has connected it."
17. L70 w1 `:368`: "\"Kinetick\" (the data vendor)"
18. L71 DECISION_LOG `:381`: vu8 audit, "`grep -rni \"Kinetick\|Playback\|connection\"` on the layout reference returns **10** lines"
19. L72 migration `:121-122`: "13. **Connections as before, and nothing more:** Simulated Data Feed; Kinetick EOD configured." `:7` "not graded by the auditor"
20. L73 update 2 `:67`: "… Kinetick EOD: NOT YET KNOWN |"; `:120`: "Still owed inside NT8: … Kinetick EOD"
21. L74 DECISION_LOG `:411` "Bead `Praxis_build-a20` filed"; `:415` "APPROVED BY: amear … DISPATCH `Praxis_build-a20`"
22. L75 a20-results `:21-22`: "Kinetick – End Of Day (Free), no dot." / "Kinetick - End Of Day row: present, no dot"; `:45` K1; DECISION_LOG `:423` "**K1** (Kinetick present, no dot)"
23. L76 DECISION_LOG `:424`: "(3) **Kinetick EOD (K1): undecided.** Amear: \"i dont know what that is or i dont remeber. look into it\"."
24. L77 DECISION_LOG `:425`: "DISPATCH: praxis-manager, Kinetick EOD research"
25. L92 DECISION_LOG `:363`: "Storage name = bare `NQCONT` … Analyzer request name = `NQCONT 09-2025`"
26. L19/L92 walkthrough `:183`: "This doesn't touch the NQCONT \"unknown instrument\" error. That's a separate defect"
27. L194 DECISION_LOG `:424`: "**Master observation, 15:55:42Z:** the Fusion `.vmx` (140 lines) contains no `sharedFolder`/`hgfs` line"
28. L300 DECISION_LOG `:393`: "(d) **NT8 PURGED all older log and trace files at its 11:12 start.**"
29. L106 update 2 `:67` D-071: "no orders, no other connection (D-071)"; L406 `:62` "**(a) Faithful** … `NinjaTrader 8-full/`"; `:70` "Not recorded: whether the fresh install's files were moved aside first"
30. Config.xml (from line 15 on only): `:18` `true`, `:34` `false`, `:39-47` type/name/Provider7/Free, `:33` and `:52` CanManageOrders true, `:66` `<Username>amear238</Username>`, `:102` GetDataFromServer true, `:15-65` has exactly the Simulator, Kinetick and Playback blocks. All match.
31. S11 traces: Kinetick count is 1 in 15-00001, 29-00000 and 29-00001 and 0 in the other 6. Line numbers 23, 25 and 23 match.
32. Labels that held: 1.1-1.4 (file contents), L89 INFERRED basis stated, L110 "data-only (UNVERIFIED)", L41-48 general knowledge all UNVERIFIED.

## Summary
Three MAJOR wrong-label findings (F1 line 17, F2 line 105, F3 line 106) and five MINOR (F4-F8). Of 31 numbered citation checks, all 31 point at real text that says what is claimed. The DECISIONS.md / DECISION_LOG.md naming is correct throughout. C1-C5 are all real; C1 and C2 carry framing or overstatement defects.

VERDICT: BROKEN
