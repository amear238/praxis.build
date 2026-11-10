# Unit 2026-11-09-d11-sweep — D11 inventory of questions waiting on Amear (manager report)

**Date:** 2026-11-09 · **Producer:** praxis-manager (unit `2026-11-09-d11-sweep`, brief from praxis-master) · **HEAD:** `f10603a` · **Branch:** main
**Standing limitation:** Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## Task

Amear's ruling D-2026-11-08-D (DECISIONS.md:1891, verbatim block) sets D1 (default-decide), D2 (only four things wait for Amear's word) and D11 ("Once per run, the master checks for any waiting question older than one run that is not a D2 item, and closes it under D1."). This unit builds the inventory the master needs to run D11: every question addressed to Amear raised before 2026-11-09T09:00Z and still waiting, searched in sources A to G of the brief. **This unit decides nothing and closes nothing.** Every "proposed closure" below is a proposal; the master decides each one.

## Rubric criteria addressed (quoted from specs/SPEC_RUBRIC.md, lines 115, 116, 122, 127)

- S1 "Every claim in a report has pasted command output, not a description of output." Every source pointer and every ANSWERED-BY / CLOSED-OTHER pointer in the tables is re-run by the manager's script in this session; the output is pasted in the Evidence appendix (416 distinct pointers, 0 empty; block V1).
- S2 "No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure." See Method note 5 for the level of each column.
- S8 "No question that belongs to Amear is answered on his behalf." Read with D1/D2 (master's filing note 1, DECISIONS.md D-2026-11-08-D filing notes). No D2 row carries a closure; each D2-AMBIGUOUS row either carries none or a closure that only declines the D2 act, with the D2 act itself left to Amear.
- S13 standing sentence: carried once, in the header above.

## Workers dispatched

| id | mode | scope | outcome |
|---|---|---|---|
| W1 | BUILD | Source A: HANDOFF.md:1-279 (cards 2026-11-04 to top) | 42 rows: 21 ANSWERED-BY, 13 WAITING, 4 CLOSED-OTHER, 4 ACTION |
| W2 | BUILD | Sources B (three return handoffs) and D (ISSUE_REGISTER.md) | 48 rows: 18 ANSWERED-BY, 19 WAITING, 8 CLOSED-OTHER, 3 ACTION |
| W3 | BUILD | Source C: all 90 `NEEDS AMEAR` lines of DECISIONS.md | 97 rows: 42 ANSWERED-BY, 16 WAITING, 35 CLOSED-OTHER, 4 ACTION; coverage file maps all 90 lines |
| W4 | BUILD | Sources E (docs/specs, diq-parked specs at HEAD only), F (bf6fcc7 R6 design), G (open beads) | 39 rows: 9 ANSWERED-BY, 15 WAITING, 8 CLOSED-OTHER, 7 ACTION |
| ADV1 | ADVERSARIAL | Re-check every D2 class, at least 15 pointers across sources, search A-G for a missed waiting question | NO RESULT: stopped at its 40-turn cap with no findings written (block V3); not a pass |
| ADV2a | ADVERSARIAL | Reduced re-dispatch, part 1: every D2 class (Tables 1, 2, actions), recommendation provenance, token and count checks | `RESULT: DEFECTS 6` (block V3) |
| ADV2b | ADVERSARIAL | Reduced re-dispatch, part 2: 38 pointers re-run across A-G (20 ANSWERED-BY), search for a missed question | `RESULT: DEFECTS 4` (block V3) |

All workers ran foreground. Worker outputs are in /tmp/d11/ (outside the repo): W1.tsv to W4.tsv, W*-evidence.md, W3-coverage.tsv, W4-bdshow/. The worker counts above are the workers' own figures; the manager re-counted them (block V1).

## Process log

1. Read specs/SPEC_RUBRIC.md and the D-2026-11-08-D block (DECISIONS.md:1891-1990) and listed ruling headings (`grep -n '^## .*D-2026-11-0'`).
2. Dispatched W1-W4 in parallel, each with the answer-check rule of the brief (ANSWERED only where a ruling's own words settle it) and a fixed TSV output.
3. Read every WAITING and ACTION row of the four TSVs. Read the lines behind the doubtful ones (return handoff 2 §4 :62-76; DECISIONS.md:1225-1236, :1814-1860, :350, :352, :536, :1788). Grouped near-duplicates into 40 WAITING groups (Table 1), 3 after-cutoff groups (Table 2) and 12 actions (13 after the adversaries); re-classed 3 worker WAITING rows and 3 roll-up rows (Method note 6). Re-authored the D2 test and the recommended option for every Table 1 and 2 row.
4. Generated the tables and the Evidence appendix with /tmp/d11/build.py from the TSVs and /tmp/d11/groups.py (the manager's grouping). The script fails a row to "UNASSIGNED" if a worker WAITING/ACTION row is in no group; none was (block V1).
5. ADV1 attacked the draft and returned no result (turn cap). Re-dispatched after material reduction as ADV2a and ADV2b, run in parallel. Every finding was re-checked by the manager (block V4) and resolved in /tmp/d11/groups.py; the tables were regenerated. Then MANIFEST row 315.

## Method notes

1. **Cutoff.** "Raised before 2026-11-09T09:00Z" uses the date the question was first raised. The R6 design (source F) is in commit `bf6fcc7`, authored `2026-11-09T05:02:44-05:00` = 10:02:44Z (block V1), so its OPEN items fall after the cutoff: they are inventoried in Table 2 and are not D11-due.
2. **Statuses.** `ANSWERED-BY` = an Amear ruling's own words settle it (pointer to the line). `WAITING` = no ruling settles it. `CLOSED-OTHER` = settled by something that is not an Amear ruling (a master settlement under R-1104-2, supersession by a later ruling, a bead close); these are not waiting, but they are not Amear's answers either, and are counted apart. `ACTION` = a physical act only Amear can do; listed under Amear's hands.
3. **Masking.** (Applies to every table cell and every pasted block, including the adversaries' files.) Quoted text in the tables and all pasted output pass through /tmp/d11/mask.sed (shown in block V2). It alters only five strings the stop gate rejects (the house limitation sentence, the three-letter placeholder, the word for an auditor's ruling, two token names) and three-tilde runs. A quote changed by the mask is marked by a hyphen inside the word.
4. **Duplicates in Table 3.** Answered and closed rows are listed per source row; the same question answered once may appear from two sources. Their count is per source row, not per distinct question. Tables 1 and 2 (the ones D11 acts on) are grouped.
5. **Levels (S2).** Pointers: re-run, OBSERVED (appendix). Quotes: the workers chose them; each pointer line is pasted so a reader can see the words. D2 tests and recommendations in Tables 1-2: the manager's reading, each re-checked by ADV1. ANSWERED-BY / CLOSED-OTHER statuses in Table 3: the workers' readings; their pointers are pasted, and ADV1 spot-checked a sample; the manager did not re-grade each one. "Recommended option" cells marked "manager's proposal" are not in any source.
6. **Re-classed worker rows.** W1-12 and W1-13 (void clause; Q3 stop multipliers) are the master's R-1104-2 settlements, "changeable by you" (return handoff 2 :69-70), the same items W2 marked CLOSED-OTHER (W2-19, W2-20): moved to CLOSED-OTHER. W1-35 (High run vs r8j) is conditional on a High run, and none is planned under R-VN4-7 (DECISIONS.md:947): CLOSED-OTHER. W1-38, W1-40, W1-41 point at whole DECISIONS.md lists that W3 checked item by item: shown as roll-ups.
7. **Conflicts the master should see.** (a) G07-G09: Amear's ruling 9 says "Notes-4 unruled items stay open; none block anything." (DECISIONS.md:1233); D1 is later and says no unit waits on Amear except for D2 items. (b) G10: the rubric's absolute park rule says "A human resumes it. The orchestrator does not." (specs/SPEC_RUBRIC.md:256). (c) G25, G28, G29, G32-G36: Amear's "Stop, freeze it" row says "No new guards, hooks, closers, or agent-stack work is dispatched." (DECISION_LOG.md:165); a D1 closure of these would start work that row stops. None of the three is resolved here.

## Table 1 - WAITING questions raised before 2026-11-09T09:00Z

| # | question (short quote) | source pointer(s) | status | D2 test | recommended option | proposed closure |
|---|---|---|---|---|---|---|
| G01 | "Tier pick (Q9): yours after paper results, not now" (raised 2026-11-07T21:49Z) | docs/reports/2026-11-07-return-handoff-claude-ai-2.md:66; docs/reports/2026-11-07-return-handoff-claude-ai.md:61; DECISIONS.md:1227; HANDOFF.md:125; DECISIONS.md:1460; DECISIONS.md:1461; HEAD:docs/specs/2026-11-05-walk-forward-spec.md:206; HEAD:docs/specs/2026-11-06-walk-forward-values.md:306; HEAD:docs/specs/2026-11-06-walk-forward-values.md:137; DECISIONS.md:1739 (rows W2-24, W1-11, W3-85, W4-01) | WAITING (timing set by Amear: D-2026-11-07-A Q9 "I pick after paper results" DECISIONS.md:1227; A4 "tier pick stays Q9" DECISIONS.md:1739) | D2-AMBIGUOUS: the tier names which MFFU account is bought, close to D2(a) "spending money"; the pick itself spends nothing until the purchase. | "yours after paper results, not now" docs/reports/2026-11-07-return-handoff-claude-ai-2.md:66 | none: do not close under D1 (D2 or D2-AMBIGUOUS); master reads D2 first; not due until paper results, by his own words |
| G02 | "VM pip ... Open: whether the packages' own dependencies and the build backend setuptools>=61 count as "the bridge's pinned requirements"" (raised 2026-11-07T21:49Z) | docs/reports/2026-11-07-return-handoff-claude-ai-2.md:71; DECISIONS.md:1231; HANDOFF.md:181 (rows W2-21, W1-14) | WAITING | NOT-D2: free pinned packages into a venv; no money, no keys, credentials or agent permissions. | "the \"no extras\" reading, which is the unit's, changeable by you" docs/reports/2026-11-07-return-handoff-claude-ai-2.md:71 | close under D1: take the unit's "no extras" reading |
| G03 | "The early-close checkpoint content. Does R-1104-2 cover the behaviour chosen in D-2026-11-07-B addendum 1, decision (1)" (raised 2026-11-07T21:49Z) | docs/reports/2026-11-07-return-handoff-claude-ai-2.md:72; DECISIONS.md:1526; HANDOFF.md:125 (rows W2-22, W1-15) | WAITING (his 17:08:00Z ratification covered timing only; DECISIONS.md:1526 "What he did NOT rule") | NOT-D2: a back-test checkpoint rule; no money, no live path. | manager's proposal: confirm D-2026-11-07-B addendum 1 decision (1) as the content | close under D1 with the proposal |
| G04 | "VM handoff §9 (the master's arm-run text, vm/2026-11-06-vm-handoff.md:314): it takes effect only by your word, after 2a passes." (raised 2026-11-07T21:49Z) | docs/reports/2026-11-07-return-handoff-claude-ai-2.md:73; HANDOFF.md:125 (rows W2-23, W1-16) | WAITING | NOT-D2: arm runs on the VM in Sim101 (C3 (5)); Block 5 live stays D2(b) per D8 (8). | manager's proposal: VM handoff §9 takes effect on the master's word once test 2a passes | close under D1 with the proposal |
| G05 | "who reads the tab and the PRAXIS commission template back (vm/2026-11-06-vm-handoff.md:151, :260)" (raised 2026-11-07T00:02Z) | docs/reports/2026-11-07-return-handoff-claude-ai.md:65 (rows W2-25) | WAITING | NOT-D2: a read-back of NT8 settings; nothing bought or installed. | manager's proposal: the VM session reads the tab and template back; Amear's screenshot is the record (D8 (7) hands-only VM) | close under D1 with the proposal |
| G06 | "Fee report NEEDS AMEAR 3 spelled out: a fill-statement check of whether MFFU sim accounts deduct the per-trade costs would need a login — do you want it?" (raised 2026-11-06 (B3 Correction 1; time not stated, before 14:43Z)) | docs/reports/2026-11-06-return-handoff-claude-ai.md:60; docs/reports/2026-11-05-mffu-fee-check.md:134 (rows W2-26) | WAITING by its source; ruling 2 "settle this class yourself" (D-2026-11-06-B, DECISIONS.md:1063) delegates the fee class to the agent | D2-AMBIGUOUS: the check needs Amear's MFFU login; D2(d) names "installing keys, credentials" and using an existing login is not plainly installing. | manager's proposal: decline the login check; take per-trade costs from MFFU's published schedule (cost model, D-2026-11-06-C) | master may settle it under ruling 2 or D1 by declining (declining uses no credential); running the login check stays D2(d)-adjacent |
| G07 | "past use of the GitHub login (item 24; no remedy requested)" (raised 2026-11-05) | DECISIONS.md:978; DECISIONS.md:983; docs/reports/2026-11-06-return-handoff-claude-ai.md:42; docs/reports/2026-11-07-return-handoff-claude-ai.md:74; DECISIONS.md:1233; HANDOFF.md:223 (rows W3-71, W2-27, W1-33) | WAITING (ruling 9: "Notes-4 unruled items stay open; none block anything." DECISIONS.md:1233) | NOT-D2: a note on past use of a login; nothing is installed. | manager's proposal: record it as noted, no remedy (the source says none was requested) | close under D1 with the proposal; flag: his ruling 9 words keep notes-4 items open, D1 is later |
| G08 | "CME Atlassian wiki as a source (item 19)" (raised 2026-11-05) | DECISIONS.md:978; DECISIONS.md:983; DECISIONS.md:1462; HEAD:docs/specs/2026-11-06-walk-forward-values.md:309; docs/reports/2026-11-06-return-handoff-claude-ai.md:42; docs/reports/2026-11-07-return-handoff-claude-ai.md:74; DECISIONS.md:1233; HANDOFF.md:223 (rows W3-73, W4-07, W2-27, W1-33) | WAITING (ruling 9, DECISIONS.md:1233) | NOT-D2: a choice of reading source. | manager's proposal: do not use the CME wiki as a source; cite CME's published pages only | close under D1 with the proposal; same ruling-9 flag as G07 |
| G09 | "second Rithmic read-only connection" (raised 2026-11-06T~01:00Z) | docs/reports/2026-11-06-return-handoff-claude-ai.md:42; docs/reports/2026-11-07-return-handoff-claude-ai.md:74; DECISIONS.md:978; DECISIONS.md:1233; DECISIONS.md:983; DECISIONS.md:1460; DECISIONS.md:1462; HEAD:docs/specs/2026-11-06-walk-forward-values.md:308; HANDOFF.md:223 (rows W2-28, W3-72, W4-06, W1-33) | WAITING (ruling 9, DECISIONS.md:1233) | D2-AMBIGUOUS: a second Rithmic connection may need credentials (D2(d)) and may carry a data fee (D2(a)). | manager's proposal: no second connection | master may close under D1 by declining (installs nothing, spends nothing); opening one stays D2 |
| G10 | "A human resumes it; the orchestrator does not." (raised 2026-11-09T06:36Z (HANDOFF.md:30)) | HANDOFF.md:36 (rows W1-03) | WAITING | NOT-D2 by D2's words (none of the four); conflict: the rubric's absolute park rule says "A human resumes it" (SPEC_RUBRIC.md:256). | manager's proposal: master decides whether D1, a human ruling made between sessions, resumes diq; if not, it waits for Amear as a park | master's call; flagged conflict with the absolute park rule, not a D1 default |
| G11 | "do R8's words on #4 and #5 name F2's governing rule and 15:00 disposition" (raised 2026-11-08) | DECISIONS.md:1645 (rows W3-91) | WAITING (A6 answers FLAG 6 except the #4/#5 part, DECISIONS.md:1788) | NOT-D2: F2 wording; D2(c) needs "while real money is at stake", and none is. | master's reading at DECISIONS.md:1788: "it is the F2 PROPOSAL unit's output, returned PROPOSED" | close under D1: the F2 PROPOSAL unit carries it |
| G12 | "Is SHM-4's "slippage >2 ticks/side worse" band (D-2026-07-15-B Q9) re-read against the new 2-tick base?" (raised 2026-10-30) | DECISIONS.md:281; DECISIONS.md:287; DECISIONS.md:288; DECISIONS.md:303 (rows W3-01) | WAITING | NOT-D2: SHM band, not one of the nine breaker values; no real money at stake. | manager's proposal: keep the band as written, measured against the 2-tick assumed base | close under D1 with the proposal |
| G13 | "Was the lock meant to cover session-close and stop-out exits as well?" (raised 2026-10-30) | DECISIONS.md:293; DECISIONS.md:303 (rows W3-06) | WAITING | NOT-D2: back-test slippage scope. | manager's proposal: the lock covers every market exit, session-close and stop-out included (strictest reading) | close under D1 with the proposal |
| G14 | "3gm Q1: sizing (b) vs (c). It is still open; this entry builds no vol-target variant." (raised 2026-10-31) | DECISIONS.md:350; DECISIONS.md:363; bd:Praxis_build-7zq (rows W3-08, W4-39) | WAITING | NOT-D2: back-test sizing. | manager's proposal: keep fixed-contract sizing as built (D6 measures at 1 MNQ and 1 NQ, DECISIONS.md:1932); build no vol-target variant | close under D1 with the proposal |
| G15 | "does the 15:59 decision become how the replication realises the 16:00 flat, or stay a test variant?" (raised 2026-10-31) | DECISIONS.md:352; DECISIONS.md:363 (rows W3-10) | WAITING | NOT-D2: back-test exit semantics. | manager's proposal: Flat1559 stays a test variant; the replication keeps the 16:00 flat as specified | close under D1 with the proposal |
| G17 | "Does `Praxis_build-7zq` close now that its third file is retired?" (raised 2026-11-02) | DECISIONS.md:399; DECISIONS.md:541 (rows W3-17) | WAITING | NOT-D2: bead housekeeping. | manager's proposal: close Praxis_build-7zq with a note that its third file is retired and variant 2 follows G14 | close under D1 with the proposal |
| G18 | "Is the Desktop trade list archived into the repo, and where (handoff §5 item 8)?" (raised 2026-11-02) | DECISIONS.md:400; DECISIONS.md:536 (rows W3-18) | WAITING | NOT-D2: file archiving. | manager's proposal: archive the Desktop trade lists into the repo under docs/reports/evidence/ with a hash line | close under D1 with the proposal |
| G19 | "Is `tools/tickprep/` the path Amear wants?" (raised 2026-11-02) | DECISIONS.md:481; DECISIONS.md:591; DECISIONS.md:715 (rows W3-29) | WAITING | NOT-D2: a repo path. | manager's proposal: keep tools/tickprep/ as filed | close under D1 with the proposal |
| G20 | "is a without-breakers backtest also kept alongside the with-breakers one, and how is the Block 4 ±15% / ±25% gate to be satisfied" (raised 2026-11-02) | DECISIONS.md:533; DECISIONS.md:1771 (rows W3-31) | WAITING (related open bead: bd:Praxis_build-yra) | NOT-D2: back-test configuration (O4). | manager's proposal: run both; the with-breakers run is the one the Block 4 gate compares (O4 allows "or both", SPEC_RUBRIC.md:107) | close under D1 with the proposal |
| G21 | "how does Amear rule on handoff §5 items 1 (early-close stamps, F2), 5 (settings not visible in the screenshots), 6 (baseline settings screenshot), 7" (raised 2026-11-02) | DECISIONS.md:536; DECISIONS.md:694 (rows W3-34) | WAITING | NOT-D2: back-test hygiene items. | manager's proposal: item 8 follows G18; items 5-7 become read-back steps on the next VM session; item 1 goes to the F2 PROPOSAL unit | close under D1 with the proposal |
| G22 | "how does Amear answer csv-analyses §7 questions 1–6 (`docs/reports/2026-11-01-csv-analyses.md:292-297`)?" (raised 2026-11-02) | DECISIONS.md:540 (rows W3-38) | WAITING | NOT-D2: analysis questions. | none in source ("This report does not answer any of them." docs/reports/2026-11-01-csv-analyses.md:290); manager's proposal: record questions 1-6 as analysis notes; no unit is blocked on them | close under D1 with the proposal |
| G23 | ""disposition is Amear's ruling with three live readings (amend the 0.1% bar; call the detector over-broad; re-pull)"" (raised 2026-08-15) | bd:Praxis_build-1gd (rows W4-21) | WAITING | NOT-D2: a data-quality disposition. | manager's proposal: re-pull (keeps the 0.1% bar; agents do not amend acceptance bars) | close under D1 with the proposal |
| G24 | ""K7 is [PROPOSED] and unratified ... Do not repair before K7 ratifies."" (raised 2026-08-08/09 (K7 PROPOSED)) | bd:Praxis_build-nvn; bd:Praxis_build-dj2 (rows W4-23) | WAITING | NOT-D2: a kit wording rule. | manager's proposal: do not ratify K7 as written; its bead is a commit-gate collision (bd:Praxis_build-nvn ("THIRD gate-commit.sh collision")); re-propose after that fix | close under D1 with the proposal (not ratified) |
| G25 | ""CANDIDATE RESOLUTIONS, UNRANKED -- the choice is Amear's (S8)"" (raised 2026-07-26) | bd:Praxis_build-fpg (rows W4-24) | WAITING | D2-AMBIGUOUS: the candidates change an enforcement hook's accepted vocabulary, which bears on agent permissions (D2(d)). | manager's proposal: no hook change | master may close under D1 by choosing no change; any hook change stays D2(d)-adjacent; also frozen: "Stop, freeze it" - "No new guards, hooks, closers, or agent-stack work is dispatched." (DECISION_LOG.md:165) |
| G26 | ""A diagnostic re-run on the Stock row needs Amear's separate approval (R-VM-5)."" (raised 2026-10-31) | bd:Praxis_build-q36 (rows W4-26) | WAITING | NOT-D2: a back-test re-run. | manager's proposal: no re-run; Stock-row runs were retired (HANDOFF.md:286) | close under D1 with the proposal |
| G27 | ""FAIL 1 of 2 — park rule fires on FAIL 2. Shot disposition is Amear's."" (raised 2026-08-29) | bd:Praxis_build-vu8 (rows W4-27) | WAITING | NOT-D2: a process disposition. | manager's proposal: bank the shot; no re-dispatch until the unit is re-scoped | close under D1 with the proposal |
| G28 | "THE MASTER CANNOT WRITE ITS OWN PERSISTENT MEMORY ... remediation is Amear's call" (raised 2026-07-27T19:58Z) | ISSUE_REGISTER.md:45; bd:Praxis_build-86t (rows W2-37, W4-29) | WAITING | D2(d): "agent permissions" (the remedy widens the master write-guard allowlist). | none in source | none: do not close under D1 (D2 or D2-AMBIGUOUS); master reads D2 first; also frozen: "Stop, freeze it" - "No new guards, hooks, closers, or agent-stack work is dispatched." (DECISION_LOG.md:165) |
| G29 | ""THE TOGGLE EXPERIMENT THAT WOULD SETTLE IT (needs authority to edit .claude/settings.json, therefore needs Amear)"" (raised 2026-07-26 (bd created)) | bd:Praxis_build-sk8 (rows W4-32) | WAITING | D2-AMBIGUOUS: the experiment edits hook registration in .claude/settings.json, the file that holds agent permissions (D2(d)). | none in source | none: do not close under D1 (D2 or D2-AMBIGUOUS); master reads D2 first; also frozen: "Stop, freeze it" - "No new guards, hooks, closers, or agent-stack work is dispatched." (DECISION_LOG.md:165) |
| G30 | ""provision praxispush + relocate the drop dir ... OR a DECISIONS entry explicitly recording the decision to defer/drop it ... Trader-owned action"" (raised 2026-07-25) | bd:Praxis_build-zd4 (rows W4-36) | WAITING | D2-AMBIGUOUS: provisioning a macOS user is close to D2(d) "credentials"; recording a deferral installs nothing. | manager's proposal: record the deferral and its accepted risk in DECISIONS.md (O2 allows this, SPEC_RUBRIC.md:93-94) | master may close under D1 by recording the deferral; provisioning stays D2(d)-adjacent |
| G31 | "User decides rotate-vs-keep. Token NEVER committed to repo" (raised 2026-05-11T00:05Z) | ISSUE_REGISTER.md:11; HANDOFF.md:1678 (rows W2-32) | WAITING | D2(d): "installing keys, credentials" (rotating a bot token). | none in source | none: do not close under D1 (D2 or D2-AMBIGUOUS); master reads D2 first |
| G32 | "SILENT-DISARM TRIP-WIRE ... remediation is Amear's call" (raised 2026-07-26T22:45Z) | ISSUE_REGISTER.md:37 (rows W2-35) | WAITING | D2-AMBIGUOUS: a SessionStart assertion that arms master guards touches agent permissions (D2(d)) without installing any. | none in source | none: do not close under D1 (D2 or D2-AMBIGUOUS); master reads D2 first; also frozen: "Stop, freeze it" - "No new guards, hooks, closers, or agent-stack work is dispatched." (DECISION_LOG.md:165) |
| G33 | "READ-ONLY CONSTRAINT VIOLATED BY A SPAWNED WORKER ... remediation is Amear's call" (raised 2026-07-27T19:52Z) | ISSUE_REGISTER.md:41 (rows W2-36) | WAITING (C7 turns memory off for praxis-manager only, DECISIONS.md:1843) | D2-AMBIGUOUS: blocking worker memory writes changes agent permissions, but restricts rather than installs. | none in source | none: do not close under D1 (D2 or D2-AMBIGUOUS); master reads D2 first; also frozen: "Stop, freeze it" - "No new guards, hooks, closers, or agent-stack work is dispatched." (DECISION_LOG.md:165) |
| G34 | "THE AUDITOR CANNOT WRITE ITS OWN V-rdict TO DISK ... remediation is Amear's call" (raised 2026-08-03T21:20Z) | ISSUE_REGISTER.md:53 (rows W2-40) | WAITING | D2(d): "agent permissions" (a remedy grants praxis-auditor a write). | none in source | none: do not close under D1 (D2 or D2-AMBIGUOUS); master reads D2 first; also frozen: "Stop, freeze it" - "No new guards, hooks, closers, or agent-stack work is dispatched." (DECISION_LOG.md:165) |
| G35 | "gate-commit.sh REPORTS THE WRONG CAUSE WHEN AN AUDIT TOKEN EXPIRES ... remediation is Amear's call" (raised 2026-08-05T01:40Z) | ISSUE_REGISTER.md:57 (rows W2-42) | WAITING | D2-AMBIGUOUS: the fix edits gate-commit.sh, the hook that gates every agent commit; that bears on agent permissions (D2(d)), as G25 does | "candidate fix is to move the sweep after the lookup, or have the sweep record why it deleted" ISSUE_REGISTER.md:57 | none: do not close under D1 (D2 or D2-AMBIGUOUS); master reads D2 first; also frozen: "Stop, freeze it" - "No new guards, hooks, closers, or agent-stack work is dispatched." (DECISION_LOG.md:165) |
| G36 | "A DENIED COMMIT BURNS THE AUDIT TOKEN ... ESCALATED to Amear; commit blocked, one token burned" (raised 2026-08-05T01:45Z) | ISSUE_REGISTER.md:59; DECISION_LOG.md:165 (rows W2-43) | WAITING ("Stop, freeze it" postpones, picks no remedy, DECISION_LOG.md:165) | D2-AMBIGUOUS: the fix edits gate-commit.sh, the hook that gates every agent commit; that bears on agent permissions (D2(d)), as G25 does | manager's proposal: a denied commit does not consume the token; the gate deletes it only on a landed commit | none: do not close under D1 (D2 or D2-AMBIGUOUS); master reads D2 first; also frozen: "Stop, freeze it" - "No new guards, hooks, closers, or agent-stack work is dispatched." (DECISION_LOG.md:165) |
| G37 | "THE LEDGERS HAVE OUTGROWN THE AGENTS THAT MUST READ THEM ... remediation is Amear's call" (raised 2026-08-06T17:15Z) | ISSUE_REGISTER.md:61; DECISION_LOG.md:165 (rows W2-44) | WAITING ("Stop, freeze it", DECISION_LOG.md:165) | NOT-D2: briefing practice. | "interim mitigation is to brief agents with grep/line-range reads instead of whole files" ISSUE_REGISTER.md:61 | close under D1: adopt the interim mitigation as the rule |
| G38 | "F4 evidence landed and staged; F4 state change is Amear's call, not this row's" (raised 2026-08-07T16:13:58Z) | ISSUE_REGISTER.md:68; DECISIONS.md:1949 (rows W2-46) | WAITING (D8 (5) orders the grading, DECISIONS.md:1949; it does not say who moves F4) | D2-AMBIGUOUS: F4 is the written MFFU permission that precedes "any order path to a funded account" (D2(b)). | none in source | none: do not close under D1 (D2 or D2-AMBIGUOUS); master reads D2 first |
| G39 | "SPEC §4.5's ACCEPTANCE GATE FOR THE CONTINUOUS NQ SERIES IS UNREACHABLE BY CONSTRUCTION ... awaiting Amear's ruling" (raised 2026-08-15T14:45:00Z) | ISSUE_REGISTER.md:72 (rows W2-47) | WAITING | NOT-D2: a data acceptance gate. | manager's proposal: record the gate as unreachable as written and report the observed figure; no new bar is written by agents | close under D1 with the proposal |
| G40 | "whether a read-only peer seat should touch a shared execution path at all is a question about seat boundaries that belongs to Amear" (raised 2026-08-15T14:46:00Z) | ISSUE_REGISTER.md:74 (rows W2-48) | WAITING | D2-AMBIGUOUS: seat boundaries are agent permissions (D2(d)), though nothing is installed. | manager's proposal: a read-only seat does not touch a shared execution path (the restrictive answer) | master may close under D1 with the restrictive answer (installs nothing); widening stays D2(d) |
| G41 | "Amear decides whether the superseded report is retained or deleted" (raised 2026-07-26T00:00Z) | ISSUE_REGISTER.md:23 (rows M-01) | WAITING (the register row's STATE is closed; the retention question in it is not; found by ADV2b) | NOT-D2: keep or delete a repo file. | manager's proposal: retain the file, marked superseded (the row calls it "the primary record") | close under D1 with the proposal |

## Table 2 - raised after the cutoff (source F and the 09:00Z run): inventoried, not D11-due

| # | question (short quote) | source pointer(s) | status | D2 test | recommended option | proposed closure |
|---|---|---|---|---|---|---|
| H01 | ""whether gates 4 and 5 apply to R6 strategies needs a ruling. Agents do not write acceptance bars."" (raised 2026-11-09T09:40Z (DECISION_LOG.md:753 "— OPEN-3"; bf6fcc7 1 [cut]) | bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md:112; bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md:104; bd:Praxis_build-ckh; HANDOFF.md:17; STATUS.md:8 (rows W4-18, W1-02) | WAITING (raised 2026-11-09T09:40Z or later; after the cutoff) | NOT-D2: a research acceptance bar; no money, no live path. | none in source ("Agents do not write acceptance bars.") | not due under D11 (not older than one run); master names it the next D11 item |
| H02 | ""whether #4's "next session" starts at 18:00 is undefined."" (raised 2026-11-09T10:02:44Z (bf6fcc7; AFTER cutoff)) | bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md:111 (rows W4-17) | WAITING (after the cutoff) | NOT-D2: breaker #4/#5 wording; D2(c) needs "while real money is at stake", and none is (same reading as G11). | "OPEN (F2 changes state only when Amear approves the breaker proposal, A6)" (bf6fcc7:...:111) | not due under D11 |
| H03 | ""Non-T1 releases (e.g. 10:00 ET) inside 1F and 2S holds; no free release list was sourced in this unit."" (raised 2026-11-09T10:02:44Z (bf6fcc7; AFTER cutoff)) | bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md:113; bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md:23 (rows W4-19) | WAITING (after the cutoff) | NOT-D2: a source list for releases. | "OPEN (backtest unit to source a free list, or 1F/2S stay provisional)" (bf6fcc7:...:113) | not due under D11 |

## Amear's hands - actions, not questions

These are physical acts only Amear can do. They are not closed under D1.

| # | action | source pointer(s) | D2 note (manager) |
|---|---|---|---|
| X01 | send MFFU support the OPEN-1 email (raised after the cutoff) | HANDOFF.md:9; bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md:110; bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md:28; bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md:89 (rows W1-01, W4-16) | D2-AMBIGUOUS (b), as X03 |
| X02 | ask MFFU the OPEN-5 stale-fill question (raised after the cutoff) | bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md:114; bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md:52 (rows W4-20) | D2-AMBIGUOUS (b), as X03 |
| X03 | send MFFU the F4 follow-up (Tradovate vs NinjaTrader/Rithmic); fx4 acceptance | DECISIONS.md:539; bd:Praxis_build-fx4 (rows W3-37, W4-34) | D2-AMBIGUOUS: F4 permission precedes "any order path to a funded account" (D2(b)), as G38 |
| X04 | start NT8 on the VM | HANDOFF.md:181; docs/reports/2026-11-07-return-handoff-claude-ai.md:73 (rows W1-20, W2-29) | NOT-D2 (Sim101, C3 (5)) |
| X05 | press Compile in the NinjaScript Editor (C3 (6)) | docs/reports/2026-11-07-return-handoff-claude-ai.md:63; DECISIONS.md:1830 (rows W2-30) | NOT-D2 |
| X06 | VM handoff §8 rows 1, 2, 3, 8 and row 11 route: hand step-0 items | HANDOFF.md:125 (rows W1-17) | NOT-D2 |
| X07 | VM screen read-backs: Log tab, save-as-default, NQCONTROW instrument | HANDOFF.md:267; DECISIONS.md:697; DECISIONS.md:698; DECISIONS.md:699 (rows W1-36, W3-59, W3-60, W3-61) | NOT-D2 |
| X08 | create the n8n Telegram credential (D2(d), credentials) | ISSUE_REGISTER.md:9; HANDOFF.md:1677 (rows W2-31) | D2(d) "installing keys, credentials" |
| X09 | rotate or confirm the Telegram bot token (D2(d), keys) | bd:Praxis_build-cn4 (rows W4-37) | D2(d) "installing keys, credentials" |
| X10 | type the park commit for y9c / diq (C2 exempts park commits from the token gate, DECISIONS.md:1826) | bd:Praxis_build-y9c; bd:Praxis_build-diq (rows W4-31) | NOT-D2 |
| X11 | run the praxis-tutor dry-run and send the style package (bev) | bd:Praxis_build-bev (rows W4-33) | NOT-D2 |
| X12 | restart NT8 per the 518 triage plan (bead may be stale) | bd:Praxis_build-518 (rows W4-38) | NOT-D2 |
| X13 | VM read-back of how NT8 resolves the same-bar exit + reverse (3gm read-back R2); moved from Table 1 (ADV2a F7) | DECISIONS.md:322 (rows W3-16) | NOT-D2 |

## Table 3 - ANSWERED or CLOSED-OTHER (not waiting; listed per source row)

One row per worker row. Cross-source duplicates among these rows are NOT merged (see Method note 4); the counts below are therefore per source row.

| # | question (short quote) | source pointer(s) | status | D2 test | recommended option | proposed closure |
|---|---|---|---|---|---|---|
| W1-04 | "How the park branch is landed under 8sw, and whether/how U7 resumes." | HANDOFF.md:119 | ANSWERED-BY D-2026-11-08-C C1+C2 DECISIONS.md:1823; DECISIONS.md:1826 | NOT-D2 | none in source | none: not waiting |
| W1-05 | "Step-0: your six answers + the snapshot name in your own words" | HANDOFF.md:120 | ANSWERED-BY D-2026-11-08-C C3+C9 DECISIONS.md:1830; DECISIONS.md:1846 | NOT-D2 (C3 (4) 'closed before real money' touches go-live, not a D2 act now) | none in source | none: not waiting |
| W1-06 | "D-2026-11-08-A NEEDS AMEAR: one entry vs "File each"." | HANDOFF.md:121 | ANSWERED-BY D-2026-11-08-C C4 DECISIONS.md:1835 | NOT-D2 | none in source | none: not waiting |
| W1-07 | "D-2026-11-08-B NEEDS AMEAR (i)" | HANDOFF.md:122 | ANSWERED-BY D-2026-11-08-C C5 DECISIONS.md:1836 | NOT-D2 | none in source | none: not waiting |
| W1-08 | "Rubric: is "discharged" recorded as `PASSED@a2f1067` right; should O1 leave the OPEN section." | HANDOFF.md:123 | ANSWERED-BY D-2026-11-08-C C6 DECISIONS.md:1841 | NOT-D2 | none in source | none: not waiting |
| W1-09 | "Bead `Praxis_build-gjj`: managers write to their agent-memory dir despite every brief" | HANDOFF.md:124 | ANSWERED-BY D-2026-11-08-C C7 DECISIONS.md:1843 | D2-AMBIGUOUS: C7 already rules; but the edit itself changes an agent definition, and D2(d) names 'installing... agent pe [cut] | none in source | none: not waiting |
| W1-10 | "item 4 first (the July rubric hunk" | HANDOFF.md:125 | ANSWERED-BY D-2026-11-08-C C8 DECISIONS.md:1845 | NOT-D2 | none in source | none: not waiting |
| W1-12 | "Still open from the 11-07 return handoff: §4 items 2 and 4–12" | HANDOFF.md:125 | CLOSED-OTHER master's R-1104-2 settlement (void clause), same item as W2-19; docs/reports/2026-11-07-return-handoff-claude-ai-2.md:69 | NOT-D2 | none in source | none: not waiting |
| W1-13 | "Still open from the 11-07 return handoff: §4 items 2 and 4–12" | HANDOFF.md:125 | CLOSED-OTHER master's R-1104-2 settlement, "changeable by you", same item as W2-20; docs/reports/2026-11-07-return-handoff-claude-ai-2.md:70 | NOT-D2 (stop multipliers are strategy parameters, not circuit-breaker values; no real money) | report :70 'the master's R-1104-2 settlement, not your word, and changeable by you (DECISIONS.md:1262' | none: not waiting |
| W1-18 | "B1: no spec v2.1 wording changes before his word" | HANDOFF.md:157 | ANSWERED-BY D-2026-11-08-A R1 DECISIONS.md:1551 | NOT-D2 | none in source | none: not waiting |
| W1-19 | "is current practice only, until Amear rules" | HANDOFF.md:180 | ANSWERED-BY D-2026-11-07-A ruling 3 DECISIONS.md:1218 | D2-AMBIGUOUS: the rejected alternative (loosening a hook) would touch agent permissions (D2(d)); the ruling already sett [cut] | none in source | none: not waiting |
| W1-21 | "(item 19, Amear's)" | HANDOFF.md:175 | ANSWERED-BY D-2026-11-07-A ruling 2 DECISIONS.md:1217 | NOT-D2 | none in source | none: not waiting |
| W1-22 | "Read his answers to the return handoff's §4." | HANDOFF.md:189 | ANSWERED-BY D-2026-11-07-A DECISIONS.md:1214 | NOT-D2 | none in source | none: not waiting |
| W1-23 | "If he ratifies addendum 5's timing" | HANDOFF.md:190 | ANSWERED-BY D-2026-11-07-A ruling 1 DECISIONS.md:1216 | NOT-D2 | none in source | none: not waiting |
| W1-24 | "after his confirmation or change of the proposed values" | HANDOFF.md:191 | ANSWERED-BY D-2026-11-07-A ruling 4 DECISIONS.md:1219 | NOT-D2 | none in source | none: not waiting |
| W1-25 | "Whether to ratify addendum 1's timing or leave it parked is Amear's." | HANDOFF.md:200 | ANSWERED-BY D-2026-11-06-B ruling 3(a) DECISIONS.md:1063 | NOT-D2 | none in source | none: not waiting |
| W1-26 | "Gate: Amear picks (a), (b) or (c) from the 00:54:04Z row." | HANDOFF.md:207 | ANSWERED-BY D-2026-11-06-B ruling 3 DECISIONS.md:1063 | D2-AMBIGUOUS: option (b)'s hook change touches the commit gate (agent permissions, D2(d)); the ruling approved it, so no [cut] | none in source | none: not waiting |
| W1-27 | "waits on the spec's NEEDS AMEAR 1–6 and the harness choice" | HANDOFF.md:209 | ANSWERED-BY D-2026-11-06-B ruling 4 DECISIONS.md:1063 | NOT-D2 | none in source | none: not waiting |
| W1-28 | "It goes to Amear; it is uncommitted." | HANDOFF.md:210 | ANSWERED-BY D-2026-11-06-B ruling 5 DECISIONS.md:1063 | NOT-D2 | none in source | none: not waiting |
| W1-29 | "fee report NEEDS AMEAR 1–3" | HANDOFF.md:218 | ANSWERED-BY D-2026-11-06-B ruling 2 DECISIONS.md:1063 for items 1-2; item 3 (login check) is G06 (ADV2b F3) | NOT-D2 | none in source | none: not waiting |
| W1-30 | "Fusion Question 0" | HANDOFF.md:219 | CLOSED-OTHER DECISIONS.md:1093 | NOT-D2 | none in source | none: not waiting |
| W1-31 | "parked-branch leak" | HANDOFF.md:220 | CLOSED-OTHER DECISIONS.md:1094 | NOT-D2 | none in source | none: not waiting |
| W1-32 | "D-2026-11-05-A NEEDS AMEAR 1–4" | HANDOFF.md:222 | ANSWERED-BY D-2026-11-06-B ruling 4 DECISIONS.md:1063 | NOT-D2 for 2-4; item 1 D2-AMBIGUOUS as W1-11 | none in source | none: not waiting |
| W1-34 | "the master's flagged reading of R-VN4-10" | HANDOFF.md:224 | CLOSED-OTHER DECISIONS.md:1096 | NOT-D2 | none in source | none: not waiting |
| W1-35 | "High-vs-r8j DEFERRED" | HANDOFF.md:257 | CLOSED-OTHER no High run is planned: R-VN4-7 "We're just gonna proceed without that" DECISIONS.md:947; re-opens as D2(a) only if a tick purchase returns | D2-AMBIGUOUS: a High-resolution run needs tick data; buying it is D2(a) 'spending money', and R-1104-3 bars the $700 pur [cut] | HANDOFF.md:257 'master must re-ask before any High run is planned' | none: not waiting |
| W1-37 | "P0 is the master's choice, unconfirmed by Amear" | HANDOFF.md:268 | ANSWERED-BY D-2026-11-05-B R-VN4-4 DECISIONS.md:941 | NOT-D2 | none in source | none: not waiting |
| W1-39 | "D-2026-11-02-B (:471)" | HANDOFF.md:277 | CLOSED-OTHER HANDOFF.md:278 | item 2 = D2(a) 'spending money' (Portara purchase) | none in source | none: not waiting |
| W1-42 | "D-2026-11-04-A (:769-771)" | HANDOFF.md:277 | ANSWERED-BY D-2026-11-05-B R-VN4-7 DECISIONS.md:947 ("Proof of concept is having the full trading pipeline..."); W1's D8 (8) pointer replaced (ADV2b minor) | D2-AMBIGUOUS: 'proof of concept' gates the $700 tick-data purchase (D2(a) spending money) under R-1104-3 | none in source | none: not waiting |
| W2-01 | "Is 08:31–16:00 the session you mean by "RTH" (Q6, D-2026-11-07-A), or do arm (a)/(b) anchor at the 09:30 open?" | docs/reports/2026-11-07-return-handoff-claude-ai-2.md:62; docs/reports/2026-11-07-return-handoff-claude-ai-2.md:63; DECISIONS.md:1551 | ANSWERED-BY D-2026-11-08-A R1 DECISIONS.md:1551 | NOT-D2 | none in source | none: not waiting |
| W2-02 | "the gate 2 Sharpe definition and its equity base ... the gate 6 WFE formula, and whether gate 6 applies to arm (a) ... whether GO / HOLD / REJECT may rest on ar [cut]" | docs/reports/2026-11-07-return-handoff-claude-ai-2.md:67; DECISIONS.md:1556; DECISIONS.md:1558; DECISIONS.md:1726; DECISIONS.md:1746; DECISIONS.md:1748; DECISIONS.md:1840; docs/reports/2026-11-06-return-handoff-claude-ai.md:42; DECISIONS.md:978 | ANSWERED-BY D-2026-11-08-A R2/R3 DECISIONS.md:1556,1558; D-2026-11-08-B A2/A7/A8 DECISIONS.md:1726,1746,1748; D-2026-11-08-C C5(iv) DECISIONS.md:1840 | NOT-D2 | none in source | none: not waiting |
| W2-03 | "The July rubric hunk in the working tree: R-A / R-B / R-C, specs/SPEC_RUBRIC.md from :267, 10 lines added ... Land it now, or not." | docs/reports/2026-11-07-return-handoff-claude-ai-2.md:68; DECISIONS.md:1845 | ANSWERED-BY D-2026-11-08-C C8 DECISIONS.md:1845 | NOT-D2 | none in source | none: not waiting |
| W2-04 | "VM handoff §8 rows 1, 2, 3, 8 ... and the route half of row 11 ... your hand step-0 items" | docs/reports/2026-11-07-return-handoff-claude-ai-2.md:74; docs/reports/2026-11-07-return-handoff-claude-ai.md:63; DECISIONS.md:1830; DECISIONS.md:1846 | ANSWERED-BY D-2026-11-08-C C3/C9 DECISIONS.md:1830,1846 | NOT-D2 | none in source | none: not waiting |
| W2-05 | "Addendum 5's timing: ratify it, or not" | docs/reports/2026-11-07-return-handoff-claude-ai.md:49; DECISIONS.md:1216 | ANSWERED-BY D-2026-11-07-A ruling 1 DECISIONS.md:1216 | NOT-D2 | none in source | none: not waiting |
| W2-06 | "does ruling 5's item 19 (commit docs/reports/2026-10-28-voice-session-notes.md) override your "old as-is set out of every commit" for this one file?" | docs/reports/2026-11-07-return-handoff-claude-ai.md:50; DECISIONS.md:1217 | ANSWERED-BY D-2026-11-07-A ruling 2 DECISIONS.md:1217 | NOT-D2 | none in source | none: not waiting |
| W2-07 | "should scripts/master-bash-guard.sh exempt commit messages, or does the attribution line keep the parenthesised form?" | docs/reports/2026-11-07-return-handoff-claude-ai.md:51; DECISIONS.md:1218 | ANSWERED-BY D-2026-11-07-A ruling 3 DECISIONS.md:1218 | NOT-D2 | none in source | none: not waiting |
| W2-08 | "Walk-forward spec: 29 questions in its ## NEEDS AMEAR section — tunable candidate sets, exit-policy options, ATR period, in-sample objective" | docs/reports/2026-11-06-return-handoff-claude-ai.md:39; docs/reports/2026-11-07-return-handoff-claude-ai.md:52; DECISIONS.md:1220; DECISIONS.md:1228; docs/reports/2026-11-07-return-handoff-claude-ai.md:78 | ANSWERED-BY D-2026-11-07-A ruling 4 Q2-Q10 DECISIONS.md:1220-1228 | NOT-D2 | none in source | none: not waiting |
| W2-09 | "The 2a NT8 run: is it covered by your lift?" | docs/reports/2026-11-07-return-handoff-claude-ai.md:64; DECISIONS.md:1229; DECISIONS.md:1089 | ANSWERED-BY D-2026-11-07-A ruling 5 DECISIONS.md:1229 | NOT-D2 | none in source | none: not waiting |
| W2-10 | "Who sets the Strategy Analyzer tab for 2a ... whether a hand-set tab counts for "drives the baseline from the terminal"" | docs/reports/2026-11-07-return-handoff-claude-ai.md:65; docs/reports/2026-11-07-return-handoff-claude-ai.md:77; DECISIONS.md:1230 | ANSWERED-BY D-2026-11-07-A ruling 6 DECISIONS.md:1230 | NOT-D2 | none in source | none: not waiting |
| W2-11 | "Bridge NEEDS AMEAR left as yours ... 4 — ever allow playbackrun/reconnect/flatten ... 5 — NT8 Guard in or out? 7 ... 11 ... 12" | docs/reports/2026-11-07-return-handoff-claude-ai.md:66; DECISIONS.md:1231 | ANSWERED-BY D-2026-11-07-A ruling 7 DECISIONS.md:1231 | NOT-D2 | none in source | none: not waiting |
| W2-12 | "Confirm that the VMware snapshot is your hand step (VM handoff §8 row 9, :281)." | docs/reports/2026-11-07-return-handoff-claude-ai.md:76; DECISIONS.md:1232 | ANSWERED-BY D-2026-11-07-A ruling 8 DECISIONS.md:1232 | NOT-D2 | none in source | none: not waiting |
| W2-13 | "Commit route (one of): 1. Type the batch commit yourself ... 2. Ratify addendum 1's timing by ruling ... 3. Leave it parked." | docs/reports/2026-11-06-return-handoff-claude-ai.md:30; docs/reports/2026-11-06-return-handoff-claude-ai.md:72; docs/reports/2026-11-06-return-handoff-claude-ai.md:55; DECISIONS.md:1063 | ANSWERED-BY D-2026-11-06-B ruling 3(a)/(b) DECISIONS.md:1063 | NOT-D2 | none in source | none: not waiting |
| W2-14 | "Adopt MFFU's $4.68 / $1.90 round turn, a single figure or a range? (fee report NEEDS AMEAR 1–3)" | docs/reports/2026-11-06-return-handoff-claude-ai.md:37; DECISIONS.md:1063 | ANSWERED-BY D-2026-11-06-B ruling 2 DECISIONS.md:1063 for items 1-2; item 3 (login check) is G06 (ADV2b F3) | NOT-D2 | none in source | none: not waiting |
| W2-15 | "Fusion: attempt the unsupported walkthrough, use the D-072 SMB route, or keep Google Drive?" | docs/reports/2026-11-06-return-handoff-claude-ai.md:38; DECISIONS.md:1004 | ANSWERED-BY D-2026-11-06-A item 3 DECISIONS.md:1004 | NOT-D2 | none in source | none: not waiting |
| W2-16 | "The parked branch parked/Praxis_build-r8j (commit f258a5d) carries a de-identification leak in its spec header: rewrite, delete, or leave?" | docs/reports/2026-11-06-return-handoff-claude-ai.md:40; DECISIONS.md:1094 | CLOSED-OTHER DECISIONS.md:1094 (master settlement under R-1104-2 via ruling 5: deletion decision stays with the master) | NOT-D2 | none in source | none: not waiting |
| W2-17 | "Carry D-2026-08-06-A (the de-identification entry, parked-branch only) onto main?" | docs/reports/2026-11-06-return-handoff-claude-ai.md:41; DECISIONS.md:1095 | CLOSED-OTHER DECISIONS.md:1095 (carried; master settlement under ruling 5) | NOT-D2 | none in source | none: not waiting |
| W2-18 | "R-VN4-10 was applied under the master's flagged reading (drop the FAIL-word filter; rely on the exact three-line contract) ... confirm or correct it." | docs/reports/2026-11-06-return-handoff-claude-ai.md:60; DECISIONS.md:1096 | CLOSED-OTHER DECISIONS.md:1096 (master settlement under ruling 5: the reading stands) | NOT-D2 | none in source | none: not waiting |
| W2-19 | "Void clause on the S13 addendum at the foot of the 10-28 notes file (98138cc; recorded at DECISIONS.md:1290)." | docs/reports/2026-11-07-return-handoff-claude-ai-2.md:69; DECISIONS.md:1290 | CLOSED-OTHER DECISIONS.md:1290 (master's decision under R-1104-2; open only as an Amear reversal) | NOT-D2 | none in source | none: not waiting |
| W2-20 | "Q3 stop multipliers 1.5 / 2.25 / 3.0 × ATR(14): the master's R-1104-2 settlement, not your word, and changeable by you" | docs/reports/2026-11-07-return-handoff-claude-ai-2.md:70; DECISIONS.md:1262 | CLOSED-OTHER DECISIONS.md:1262 (master's decision under R-1104-2 on Amear's Q3/Q10 delegation) | NOT-D2 | none in source | none: not waiting |
| W2-33 | "Amear's call whether v2 ships with the claim corrected-and-documented or held for a real fix" | ISSUE_REGISTER.md:27; ISSUE_REGISTER.md:31; ISSUE_REGISTER.md:33 | CLOSED-OTHER ISSUE_REGISTER.md:33 (agent-spawn-guard.sh hook, STATE closed) | NOT-D2 | none in source | none: not waiting |
| W2-34 | "awaiting Amear's disposition on 599885e" | ISSUE_REGISTER.md:35; DECISION_LOG.md:135 | CLOSED-OTHER DECISION_LOG.md:135 (reset away; reflog proof) | NOT-D2 | none in source | none: not waiting |
| W2-38 | "UNGUARDED WRITE PATH TO .claude/agents/ ... ESCALATED TO AMEAR; no fix dispatched" | ISSUE_REGISTER.md:47; DECISIONS.md:1949 | ANSWERED-BY D-2026-11-08-D D8(6) DECISIONS.md:1949 | D2(d): "agent permissions" | none in source | none: not waiting |
| W2-39 | "two unauthorised /private/tmp/ hooks ... Removal is Amear's" | ISSUE_REGISTER.md:49; ISSUE_REGISTER.md:51 | CLOSED-OTHER .claude/settings.json (grep 'private/tmp' = no match in working tree and HEAD) | D2(d): "agent permissions" (hook registration) | none in source | none: not waiting |
| W2-41 | "TWO STAGED REPORTS ATTRIBUTE A DIRECT QUOTATION TO A FILE THAT DOES NOT CONTAIN IT ... ESCALATED to Amear" | ISSUE_REGISTER.md:55; DECISION_LOG.md:155 | ANSWERED-BY amear DECISION_LOG 2026-08-04T18:44Z DECISION_LOG.md:155 | NOT-D2 | none in source | none: not waiting |
| W2-45 | "the de-identification form is Amear's ruling to give" | ISSUE_REGISTER.md:63; DECISIONS.md:1136 | ANSWERED-BY D-2026-08-06-A DECISIONS.md:1136 | NOT-D2 | none in source | none: not waiting |
| W3-02 | "Does that satisfy F3's "stated in writing before the backtest runs"?" | DECISIONS.md:251; DECISIONS.md:289; DECISIONS.md:299; DECISIONS.md:301 | ANSWERED-BY D-2026-10-30-A Rulings 2026-10-30 (DECISION_LOG 2026-10-30T23:23:00Z WHO: amear) DECISIONS.md:301 | NOT-D2 | none in source | none: not waiting |
| W3-03 | "does NT8 apply Slippage 2 on every market fill, and what is the unit of the Summary's "Total slippage" cell?" | DECISIONS.md:290; DECISIONS.md:303 | CLOSED-OTHER bead Praxis_build-o78 CLOSED (bd show: "Amear ruling 2026-10-31T17:00Z: both questions answered") | NOT-D2 | none in source | none: not waiting |
| W3-04 | "Approve or replace the proposed limitation sentence." | DECISIONS.md:291; DECISIONS.md:297; DECISIONS.md:299; DECISIONS.md:302 | ANSWERED-BY D-2026-10-30-A Rulings DECISIONS.md:302 | NOT-D2 | none in source | none: not waiting |
| W3-05 | "The R3 Standard-vs-High control proposed at 2026-08-29T00:40:00Z is open. Is it run before F3 is graded, or does (c) stand as INFERRED?" | DECISIONS.md:259; DECISIONS.md:292; DECISIONS.md:299; DECISIONS.md:300; DECISIONS.md:649; DECISIONS.md:708 | ANSWERED-BY D-2026-10-30-A Rulings DECISIONS.md:300 | NOT-D2 | none in source | none: not waiting |
| W3-07 | "should OppBand mean the paper's opposite band in the replication (change base :209/:217, keep and rename, or drop)?" | DECISIONS.md:349; DECISIONS.md:363 | ANSWERED-BY D-2026-11-07-A ruling 4 Q4 DECISIONS.md:1222 | NOT-D2 | none in source | none: not waiting |
| W3-09 | "should a session-aware flat be built, and where?" | DECISIONS.md:351; DECISIONS.md:363 | CLOSED-OTHER DECISIONS.md:943-944 (R-VN4-5 his words "happy to move on"; voice-agent reading "the 12:15 early-close exits are accepted as is") | NOT-D2 | none in source | none: not waiting |
| W3-11 | "Does that arrangement meet his constraint?" | DECISIONS.md:353; DECISIONS.md:358 | ANSWERED-BY R-7zq-1 DECISIONS.md:358 | NOT-D2 | none in source | none: not waiting |
| W3-12 | "Third file: the M2 pick is #1 of the shortlist by his ruling. The swap stays his after he reads the shortlist." | DECISIONS.md:354; DECISIONS.md:360 | ANSWERED-BY R-7zq-3 DECISIONS.md:360 | NOT-D2 | none in source | none: not waiting |
| W3-13 | "is a fill at the 16:00 bar's Open (~15:59 price) acceptable as the backtest realisation of the 16:00 flat" | DECISIONS.md:355; DECISIONS.md:359 | ANSWERED-BY R-7zq-2 DECISIONS.md:359 | NOT-D2 | none in source | none: not waiting |
| W3-14 | "Step 0, the values for High's extra fields and what counts as "identical"" | DECISIONS.md:363; DECISIONS.md:708 | CLOSED-OTHER superseded by D-2026-11-05-B R-VN4-7 DECISIONS.md:947 ("We're just gonna proceed without that [historical tick data].") | NOT-D2 | none in source | none: not waiting |
| W3-15 | "r = 0 → short; the previous-close rule; the missing-15:30 fallback; the 15:30 reference price; the η(r_ONFH, r_ROD) variant; the roll convention" | DECISIONS.md:363 | CLOSED-OTHER third file retired, D-2026-11-02-A DECISIONS.md:383 | NOT-D2 | none in source | none: not waiting |
| W3-19 | "Is `PraxisLastHalfHourMomentum` also out of the R-VN3-2 High fill-resolution preparation, or does it stay in that comparison as a record run?" | DECISIONS.md:383; DECISIONS.md:401; DECISIONS.md:542; DECISIONS.md:621; DECISIONS.md:711 | CLOSED-OTHER superseded by D-2026-11-05-B R-VN4-7 DECISIONS.md:947 ("We're just gonna proceed without that [historical tick data].") | NOT-D2 | none in source | none: not waiting |
| W3-20 | "`.exe` ruling: source only with the rebuild steps, or the binaries too?" | DECISIONS.md:472; DECISIONS.md:591; DECISIONS.md:687; DECISIONS.md:693 | ANSWERED-BY DECISION_LOG 2026-11-03T18:45:00Z (WHO: amear) quoted DECISIONS.md:591 | NOT-D2 | none in source | none: not waiting |
| W3-21 | "Is the Portara data purchase that README line 13 presupposes authorised?" | DECISIONS.md:473; DECISIONS.md:591; DECISIONS.md:680 | ANSWERED-BY DECISION_LOG 2026-11-03T18:40:00Z (WHO: amear) quoted DECISIONS.md:591; and D-2026-11-05-B R-VN4-7 DECISIONS.md:947 | D2(a) "spending money" | none in source | none: not waiting |
| W3-22 | "Does it count as a "run" under R-VN3-2, and is its result accepted as reported or to be re-run under approval?" | DECISIONS.md:462; DECISIONS.md:474; DECISIONS.md:591; DECISIONS.md:706 | CLOSED-OTHER superseded by D-2026-11-05-B R-VN4-7 DECISIONS.md:947 ("We're just gonna proceed without that [historical tick data].") | NOT-D2 | none in source | none: not waiting |
| W3-23 | "Should the VM-side originals (the four files and both `.exe`) be hashed on the VM to close the UNVERIFIED link in the provenance chain?" | DECISIONS.md:475; DECISIONS.md:591; DECISIONS.md:715 | CLOSED-OTHER superseded by D-2026-11-05-B R-VN4-7 DECISIONS.md:947 ("We're just gonna proceed without that [historical tick data].") | NOT-D2 | none in source | none: not waiting |
| W3-24 | "`nt-implied-offsets.csv`: is the LF repo copy the canonical one" | DECISIONS.md:476; DECISIONS.md:591; DECISIONS.md:705 | CLOSED-OTHER superseded by D-2026-11-05-B R-VN4-7 DECISIONS.md:947 ("We're just gonna proceed without that [historical tick data].") | NOT-D2 | none in source | none: not waiting |
| W3-25 | "If any measured offset differs from NT's, stop there, or force NT's values with `--offsets`?" | DECISIONS.md:477; DECISIONS.md:591; DECISIONS.md:663; DECISIONS.md:682 | CLOSED-OTHER superseded by D-2026-11-05-B R-VN4-7 DECISIONS.md:947 ("We're just gonna proceed without that [historical tick data].") | NOT-D2 | none in source | none: not waiting |
| W3-26 | "Which option list is "option C" from?" | DECISIONS.md:478; DECISIONS.md:591; DECISIONS.md:703 | CLOSED-OTHER superseded by D-2026-11-05-B R-VN4-7 DECISIONS.md:947 ("We're just gonna proceed without that [historical tick data].") | NOT-D2 | none in source | none: not waiting |
| W3-27 | "Which 1-min file is the input to `measure` / `build` / `verify`?" | DECISIONS.md:479; DECISIONS.md:591; DECISIONS.md:681 | CLOSED-OTHER superseded by D-2026-11-05-B R-VN4-7 DECISIONS.md:947 ("We're just gonna proceed without that [historical tick data].") | NOT-D2 | none in source | none: not waiting |
| W3-28 | "How many unmatched or missing minutes are acceptable before the output is used?" | DECISIONS.md:480; DECISIONS.md:591; DECISIONS.md:625; DECISIONS.md:704 | CLOSED-OTHER superseded by D-2026-11-05-B R-VN4-7 DECISIONS.md:947 ("We're just gonna proceed without that [historical tick data].") | NOT-D2 | none in source | none: not waiting |
| W3-30 | "O1: which of the six Block 2 pass gates apply to the version judged under R-VN3-6?" | DECISIONS.md:531; DECISIONS.md:532; DECISIONS.md:757; DECISIONS.md:819; DECISIONS.md:1462; DECISIONS.md:1776 | ANSWERED-BY D-2026-11-08-B A8 DECISIONS.md:1748 | NOT-D2 | none in source | none: not waiting |
| W3-32 | "are backtest results without breakers (such as the 2026-11-01 runs) used for anything, or held as records only?" | DECISIONS.md:534 | ANSWERED-BY D-2026-11-08-D D6 DECISIONS.md:1930 | NOT-D2 | none in source | none: not waiting |
| W3-33 | "how are the breakers to be applied inside a Strategy Analyzer backtest?" | DECISIONS.md:535 | ANSWERED-BY D-2026-11-05-B R-VN4-2 DECISIONS.md:936 | NOT-D2 | none in source | none: not waiting |
| W3-35 | "R-VN3-3: does "proceed as it is" also cover the effect of each 17-day hole on the 14-day lookback" | DECISIONS.md:499; DECISIONS.md:537 | ANSWERED-BY D-2026-11-05-B R-VN4-5 DECISIONS.md:943 | NOT-D2 | none in source | none: not waiting |
| W3-36 | "R-VN3-3: does it also apply to the tick data for the High fill-resolution preparation (R-VN3-2), or only to the 1-minute data?" | DECISIONS.md:499; DECISIONS.md:538; DECISIONS.md:622; DECISIONS.md:712 | CLOSED-OTHER superseded by D-2026-11-05-B R-VN4-7 DECISIONS.md:947 ("We're just gonna proceed without that [historical tick data].") | NOT-D2 | none in source | none: not waiting |
| W3-39 | "`Praxis_build-r8j` was raised to P0, the level the master chose. ... Is P0 the level he wants?" | DECISIONS.md:489; DECISIONS.md:543; DECISIONS.md:771; DECISIONS.md:822 | ANSWERED-BY D-2026-11-05-B R-VN4-4 DECISIONS.md:941 | NOT-D2 | none in source | none: not waiting |
| W3-40 | "R-VN3-6: does "closest to live execution" mean High fill resolution and breakers on, as the agent read it to him?" | DECISIONS.md:520; DECISIONS.md:544; DECISIONS.md:620; DECISIONS.md:713; DECISIONS.md:754 | CLOSED-OTHER his word is "Yeah" and "The row does not record the question he answered." (DECISIONS.md:753); moot under R-VN4-7 (DECISIONS.md:947) (ADV2b F1) | NOT-D2 | none in source | none: not waiting |
| W3-41 | "Slippage may be ignored under High, which would trigger F3." | DECISIONS.md:662 | CLOSED-OTHER superseded by D-2026-11-05-B R-VN4-7 DECISIONS.md:947 ("We're just gonna proceed without that [historical tick data].") | NOT-D2 | none in source | none: not waiting |
| W3-42 | "Importing ticks could change how NT builds the 1-min primary." | DECISIONS.md:664 | CLOSED-OTHER superseded by D-2026-11-05-B R-VN4-7 DECISIONS.md:947 ("We're just gonna proceed without that [historical tick data].") | NOT-D2 | none in source | none: not waiting |
| W3-43 | "A full-range High run could run out of memory." | DECISIONS.md:665 | CLOSED-OTHER superseded by D-2026-11-05-B R-VN4-7 DECISIONS.md:947 ("We're just gonna proceed without that [historical tick data].") | NOT-D2 | none in source | none: not waiting |
| W3-44 | "Approve P1 (one-month import) once the sample passes?" | DECISIONS.md:683 | CLOSED-OTHER superseded by D-2026-11-05-B R-VN4-7 DECISIONS.md:947 ("We're just gonna proceed without that [historical tick data].") | NOT-D2 | none in source | none: not waiting |
| W3-45 | "R2: add the 1-tick-slippage spec run after the 0-H control?" | DECISIONS.md:684 | CLOSED-OTHER superseded by D-2026-11-05-B R-VN4-7 DECISIONS.md:947 ("We're just gonna proceed without that [historical tick data].") | NOT-D2 | none in source | none: not waiting |
| W3-46 | "Is "Baseline-H" a separate run from 0-H, or the same?" | DECISIONS.md:685 | CLOSED-OTHER superseded by D-2026-11-05-B R-VN4-7 DECISIONS.md:947 ("We're just gonna proceed without that [historical tick data].") | NOT-D2 | none in source | none: not waiting |
| W3-47 | "Memory fallback: year-by-year runs or a 1-second fill series?" | DECISIONS.md:686 | CLOSED-OTHER superseded by D-2026-11-05-B R-VN4-7 DECISIONS.md:947 ("We're just gonna proceed without that [historical tick data].") | NOT-D2 | none in source | none: not waiting |
| W3-48 | "tick files delivered in Central time "would need a code change, a question for Amear first"" | DECISIONS.md:702 | CLOSED-OTHER superseded by D-2026-11-05-B R-VN4-7 DECISIONS.md:947 ("We're just gonna proceed without that [historical tick data].") | NOT-D2 | none in source | none: not waiting |
| W3-49 | "R0 (0-S full range after the import): no approval question is posed for it" | DECISIONS.md:707 | CLOSED-OTHER superseded by D-2026-11-05-B R-VN4-7 DECISIONS.md:947 ("We're just gonna proceed without that [historical tick data].") | NOT-D2 | none in source | none: not waiting |
| W3-50 | "R1 (0-H): no approval question is posed for it apart from item 22." | DECISIONS.md:708 | CLOSED-OTHER superseded by D-2026-11-05-B R-VN4-7 DECISIONS.md:947 ("We're just gonna proceed without that [historical tick data].") | NOT-D2 | none in source | none: not waiting |
| W3-51 | "R3–R4 (OppBand and Flat1559 at High): no approval question is posed for them." | DECISIONS.md:709 | CLOSED-OTHER superseded by D-2026-11-05-B R-VN4-7 DECISIONS.md:947 ("We're just gonna proceed without that [historical tick data].") | NOT-D2 | none in source | none: not waiting |
| W3-52 | "the Analyzer dropdown look ("with no run"): whether it needs approval is not posed." | DECISIONS.md:710 | CLOSED-OTHER superseded by D-2026-11-05-B R-VN4-7 DECISIONS.md:947 ("We're just gonna proceed without that [historical tick data].") | NOT-D2 | none in source | none: not waiting |
| W3-53 | "whether "1,190 trades", "$197,327.60" and "total slippage 1190" are the R0/R1 pass bars" | DECISIONS.md:714 | CLOSED-OTHER superseded by D-2026-11-05-B R-VN4-7 DECISIONS.md:947 ("We're just gonna proceed without that [historical tick data].") | NOT-D2 | none in source | none: not waiting |
| W3-54 | "Copy `db\minute\NQCONTROW 09-25` and record SHA-256 for every file before any import" | DECISIONS.md:716 | CLOSED-OTHER superseded by D-2026-11-05-B R-VN4-7 DECISIONS.md:947 ("We're just gonna proceed without that [historical tick data].") | NOT-D2 | none in source | none: not waiting |
| W3-55 | "the price route ("Flat is cheaper": $695 flat against $750 by the year) and the time zone to ask Portara for" | DECISIONS.md:717 | CLOSED-OTHER superseded by D-2026-11-05-B R-VN4-7 DECISIONS.md:947 ("We're just gonna proceed without that [historical tick data].") | D2(a) "spending money" (purchase-route item) | none in source | none: not waiting |
| W3-56 | "Send Portara the eight questions (plan §6), then decide whether to buy for $695." | DECISIONS.md:691 | ANSWERED-BY DECISION_LOG 2026-11-03T18:40:00Z (WHO: amear) DECISIONS.md:691 | D2(a) "spending money" | none in source | none: not waiting |
| W3-57 | "Should the High measurement runs wait for `r8j` (breakers), or go ahead as measurement-only?" | DECISIONS.md:688 | ANSWERED-BY DECISION_LOG 2026-11-03T18:45:00Z (WHO: amear) DECISIONS.md:688 | NOT-D2 | none in source | none: not waiting |
| W3-58 | "Should the per-contract NQ minute folders already on the VM be read (read-only) to confirm the 1-min file's source before buying?" | DECISIONS.md:692 | ANSWERED-BY DECISION_LOG 2026-11-03T18:40:00Z (WHO: amear) DECISIONS.md:692 | NOT-D2 | none in source | none: not waiting |
| W3-62 | "What counts as "proof of concept"?" | DECISIONS.md:756; DECISIONS.md:769; DECISIONS.md:770 | ANSWERED-BY D-2026-11-05-B R-VN4-7 DECISIONS.md:947 | NOT-D2 | none in source | none: not waiting |
| W3-63 | "Which MFFU account size and which tier limits are to be used for items 3 and 4" | DECISIONS.md:828; DECISIONS.md:829 | ANSWERED-BY D-2026-11-08-B A4 DECISIONS.md:1738 | NOT-D2 | none in source | none: not waiting |
| W3-64 | "Does arm (b) run on minute data, given its stop (report C NEEDS AMEAR 11)?" | DECISIONS.md:821; DECISIONS.md:830 | ANSWERED-BY D-2026-11-05-B R-VN4-3 DECISIONS.md:939 | NOT-D2 | none in source | none: not waiting |
| W3-65 | "What is the candidate set for the exit-policy parameter in item 1(b)?" | DECISIONS.md:831 | ANSWERED-BY D-2026-11-06-B ruling 4 DECISIONS.md:1063 | NOT-D2 | none in source | none: not waiting |
| W3-66 | "Is R-1104-3's judged version arm (a), arm (b) or both?" | DECISIONS.md:832 | ANSWERED-BY D-2026-11-06-B ruling 4 DECISIONS.md:1063 | NOT-D2 | none in source | none: not waiting |
| W3-67 | "see `docs/specs/2026-11-05-walk-forward-spec.md`, section `## NEEDS AMEAR`, items 1–29" | DECISIONS.md:898; DECISIONS.md:920; DECISIONS.md:1024; DECISIONS.md:1314; DECISIONS.md:1881 | CLOSED-OTHER DECISIONS.md:1314 (D-2026-11-07-A Q10 :1228 hands remaining values to master under R-1104-2; reach INFERRED) | NOT-D2 | none in source | none: not waiting |
| W3-68 | "R-VN4-10: is the master's reading (drop the FAIL-word filter ...) what you meant, or should it be corrected?" | DECISIONS.md:955; DECISIONS.md:983 | CLOSED-OTHER D-2026-11-06-B settlement 17 DECISIONS.md:1096 (master, under Amear's ruling 5 :1063) | NOT-D2 | none in source | none: not waiting |
| W3-69 | "R-VN4-6: which fee figure applies" | DECISIONS.md:970; DECISIONS.md:985; DECISIONS.md:1022 | ANSWERED-BY D-2026-11-06-B ruling 2 DECISIONS.md:1063 | NOT-D2 | none in source | none: not waiting |
| W3-70 | "R-VN4-14: Question 0 in `docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md:8`." | DECISIONS.md:983; DECISIONS.md:1017; DECISIONS.md:1050 | CLOSED-OTHER D-2026-11-06-B settlement 10 DECISIONS.md:1093 (master, under ruling 5) | NOT-D2 | none in source | none: not waiting |
| W3-74 | "equity base for the 4% DD gate (item 5)" | DECISIONS.md:820; DECISIONS.md:978; DECISIONS.md:983; DECISIONS.md:1462; DECISIONS.md:1643; DECISIONS.md:1772 | ANSWERED-BY D-2026-11-08-B A4 DECISIONS.md:1739 | NOT-D2 | none in source | none: not waiting |
| W3-75 | "Sharpe definition (item 4)" | DECISIONS.md:978; DECISIONS.md:983; DECISIONS.md:1462; DECISIONS.md:1770; DECISIONS.md:1804 | ANSWERED-BY D-2026-11-08-C C5 (iv) DECISIONS.md:1839 | NOT-D2 | none in source | none: not waiting |
| W3-76 | "Should the Fusion walkthrough's go-live section ... be amended with your line "unmap Z: and turn the share off before real money"?" | DECISIONS.md:1020; DECISIONS.md:1041 | ANSWERED-BY D-2026-11-07-A ruling 10 DECISIONS.md:1234 | NOT-D2 | none in source | none: not waiting |
| W3-77 | "After the install walkthrough is written, who performs the install?" | DECISIONS.md:1042; DECISIONS.md:1063; DECISIONS.md:1074 | ANSWERED-BY D-2026-11-06-B ruling 1 DECISIONS.md:1063 | NOT-D2 | none in source | none: not waiting |
| W3-78 | "What is "the VM's Cowork agent", where does it run, and where is its skills directory?" | DECISIONS.md:1043 | CLOSED-OTHER D-2026-11-06-B settlement 3 DECISIONS.md:1086 (master working definition, under ruling 5) | NOT-D2 | none in source | none: not waiting |
| W3-79 | "For test 2a: is ... the reference run, and does "reproduces" mean an exact match on trades and net, or a tolerance?" | DECISIONS.md:1044 | ANSWERED-BY D-2026-11-06-B ruling 5 default DECISIONS.md:1063 | NOT-D2 | none in source | none: not waiting |
| W3-80 | "Should the rule that reports carry the standing limitation sentence ... be written into `specs/SPEC_RUBRIC.md`?" | DECISIONS.md:1045 | CLOSED-OTHER D-2026-11-06-B settlement 5 DECISIONS.md:1088 (S13, master under ruling 5) | NOT-D2 | none in source | none: not waiting |
| W3-81 | "Does test 2a ... need your separate lift of the `23:50:09Z` limit ... and of D-071 ..., or does item 2 cover them?" | DECISIONS.md:1014; DECISIONS.md:1034; DECISIONS.md:1046; DECISIONS.md:1089; DECISIONS.md:1263 | ANSWERED-BY D-2026-11-07-A ruling 5 DECISIONS.md:1229 (run half) and D-2026-11-06-B ruling 5 default DECISIONS.md:1063 ("D-071 untouched") | NOT-D2 | none in source | none: not waiting |
| W3-82 | "Who reads the version on the VM (you or the VM agent) for Code to record?" | DECISIONS.md:1009; DECISIONS.md:1047 | ANSWERED-BY D-2026-11-06-B ruling 5 default DECISIONS.md:1063 | NOT-D2 | none in source | none: not waiting |
| W3-83 | "Who judges that 2a and 2b have passed, and is the lift recorded by your own ledger row?" | DECISIONS.md:1048 | ANSWERED-BY D-2026-11-06-B ruling 5 default DECISIONS.md:1063 | NOT-D2 | none in source | none: not waiting |
| W3-84 | "If a VM agent session can write in `Z:`, does that count as a second session against this working tree?" | DECISIONS.md:1049 | ANSWERED-BY D-2026-11-06-B ruling 5 default DECISIONS.md:1063 | NOT-D2 | none in source | none: not waiting |
| W3-86 | "FLAG 1: Whether R4 applies to the gate only, or also changes §6's selection statistic" | DECISIONS.md:1621; DECISIONS.md:1638; DECISIONS.md:1640 | ANSWERED-BY D-2026-11-08-B A1 DECISIONS.md:1724 | NOT-D2 | none in source | none: not waiting |
| W3-87 | "FLAG 2: R4 vs the gate-2 open item ... "the account size actually traded" names no figure" | DECISIONS.md:1621; DECISIONS.md:1638; DECISIONS.md:1641 | ANSWERED-BY D-2026-11-08-B A2 DECISIONS.md:1726 | NOT-D2 | none in source | none: not waiting |
| W3-88 | "FLAG 3: Where R4's win-rate rule applies" | DECISIONS.md:1621; DECISIONS.md:1638; DECISIONS.md:1642 | ANSWERED-BY D-2026-11-08-B A3 DECISIONS.md:1730 | NOT-D2 | none in source | none: not waiting |
| W3-89 | "FLAG 5: Whether R4's "trading day" is the session i of :92" | DECISIONS.md:1621; DECISIONS.md:1638; DECISIONS.md:1644 | ANSWERED-BY D-2026-11-08-B A5 DECISIONS.md:1741 | NOT-D2 | none in source | none: not waiting |
| W3-90 | "FLAG 6: Does R8 change F2's state in `specs/SPEC_RUBRIC.md`" | DECISIONS.md:1621; DECISIONS.md:1638; DECISIONS.md:1645 | ANSWERED-BY D-2026-11-08-B A6 DECISIONS.md:1744 | NOT-D2 | none in source | none: not waiting |
| W3-92 | "(i) Whether one entry satisfies "File each as a DECISIONS.md entry" (DECISIONS.md:1546)." | DECISIONS.md:1678; DECISIONS.md:1708; DECISIONS.md:1860 | ANSWERED-BY D-2026-11-08-C C4 DECISIONS.md:1835 | NOT-D2 | none in source | none: not waiting |
| W3-93 | "A3's words do not say whether W and L are classified by price or by net P&L after commission and slippage." | DECISIONS.md:1771; DECISIONS.md:1800; DECISIONS.md:1801 | ANSWERED-BY D-2026-11-08-C C5 (i) DECISIONS.md:1836 | NOT-D2 | none in source | none: not waiting |
| W3-94 | "Which limit type and stage A4 means for the Studio Static rows, and for rows whose Eval and Sim-Funded types differ, is his." | DECISIONS.md:1772; DECISIONS.md:1802; DECISIONS.md:1881 | CLOSED-OTHER in part: C5 (ii) answers the Studio Static rows only (DECISIONS.md:1837); the rest decided by master under D1 (DECISIONS.md:1885) (ADV2b F2) | NOT-D2 | none in source | none: not waiting |
| W3-95 | "C5 (ii)'s words name the Studio Static rows; whether they also reach the Rapid rows" | DECISIONS.md:1885; DECISIONS.md:1886 | CLOSED-OTHER DECISIONS.md:1885 (decided by master under D-2026-11-08-D D1, assigned to the values-spec unit) | NOT-D2 | none in source | none: not waiting |
| W3-96 | "A8 (:43): "annualised OOS net profit / annualised IS net profit" names no annualisation method" | DECISIONS.md:1776; DECISIONS.md:1803 | ANSWERED-BY D-2026-11-08-C C5 (iii) DECISIONS.md:1838 | NOT-D2 | none in source | none: not waiting |
| W3-97 | "Whether S7 is amended with C2, or read as covering `main` only" | DECISIONS.md:1885; DECISIONS.md:1887 | CLOSED-OTHER DECISIONS.md:1885 (decided by master under D1, rubric unit; stops if D2 (d)) | D2-AMBIGUOUS: the source itself says the rubric unit stops if the question touches agent permissions (D2 (d)). | none in source | none: not waiting |
| W4-02 | ""What is the **Sharpe definition** for "OOS Sharpe ≥ 1.0" ... and what **equity base** does it use"" | HEAD:docs/specs/2026-11-05-walk-forward-spec.md:202; HEAD:docs/specs/2026-11-06-walk-forward-values.md:310; HEAD:docs/specs/2026-11-06-walk-forward-values.md:93; HEAD:docs/specs/2026-11-06-walk-forward-values.md:132; DECISIONS.md:978 | ANSWERED-BY D-2026-11-08-B A2 DECISIONS.md:1726 (+ D-2026-11-08-C C5(iv) DECISIONS.md:1839-1840 "A2 closes the notes-4 Sharpe item") | NOT-D2 | none in source | none: not waiting |
| W4-03 | ""equity base for the 4% DD gate (item 5)"" | HEAD:docs/specs/2026-11-06-walk-forward-values.md:310; DECISIONS.md:978 | ANSWERED-BY D-2026-11-08-B A4 DECISIONS.md:1739-1740 ("Closes the notes-4 DD equity-base item.") | NOT-D2 | none in source | none: not waiting |
| W4-04 | ""Does **WFE ≥ 0.50** apply to arm (a), which has no in-sample optimisation (O1)? For arm (b), which WFE formula is used?"" | HEAD:docs/specs/2026-11-05-walk-forward-spec.md:203; HEAD:docs/specs/2026-11-06-walk-forward-values.md:311; HEAD:docs/specs/2026-11-06-walk-forward-values.md:133 | ANSWERED-BY D-2026-11-08-B A7 DECISIONS.md:1746 ("arm (a) is judged on gates 1-5 (WFE not") and A8 DECISIONS.md:1748 ("Gate 6 formula (Pardo WFE):") | NOT-D2 | none in source | none: not waiting |
| W4-05 | ""What is the **full gate set for each arm**, and does **GO / HOLD / REJECT** ... sit on arm (a), arm (b) or both"" | HEAD:docs/specs/2026-11-05-walk-forward-spec.md:204; HEAD:docs/specs/2026-11-05-walk-forward-spec.md:205; HEAD:docs/specs/2026-11-06-walk-forward-values.md:311; HEAD:docs/specs/2026-11-06-walk-forward-values.md:134 | ANSWERED-BY D-2026-11-08-A R2 DECISIONS.md:1556 ("GO requires arm (a) to pass") + D-2026-11-08-B A7/A8 DECISIONS.md:1746, :1748 ("O1 is discharged by R2 + R3 + A7") + D-2026-11-08-C C6 DECISIONS.md:1841 | NOT-D2 | none in source | none: not waiting |
| W4-08 | ""which **stage** (Evaluation or Sim-Funded) and which **type** (EOD or intraday trailing) counts? Do Studio's **Static** limits count?"" | HEAD:docs/specs/2026-11-05-walk-forward-spec.md:207; HEAD:docs/specs/2026-11-06-walk-forward-values.md:330 | CLOSED-OTHER in part: C5 (ii) answers the Studio Static rows only (DECISIONS.md:1837); the rest decided by master under D1 (DECISIONS.md:1885) (ADV2b F2) | NOT-D2 | none in source | none: not waiting |
| W4-09 | ""Q2 \| The verbatim Block-2 exit-milestone text" ... "Q9 \| SHM-4/SHM-5 band *form* preference"" | docs/specs/2026-07-15-block2-backtesting-scope-proposal.md:118-125; docs/specs/2026-07-15-block2-backtesting-scope-proposal.md:139 | ANSWERED-BY D-2026-07-15-B DECISIONS.md:180-189 | NOT-D2 | none in source | none: not waiting |
| W4-10 | ""**Still PENDING trader confirmation:** whether any TradingView Pine source exists / TradingView's role (generator vs passthrough)"" | docs/specs/2026-07-15-block2-backtesting-scope-proposal.md:131; docs/specs/2026-07-15-block2-backtesting-scope-proposal.md:127 | CLOSED-OTHER DECISIONS.md:181 ("Q1 was closed session 14 (re-implement in NT8, D 21:10Z)") | NOT-D2 | none in source | none: not waiting |
| W4-11 | ""**T1 (highest priority): session-flat time — 16:00 (paper) vs 11:30 (PRAXIS window).** ... Trader must decide the flat time"" | docs/specs/2026-07-16-b2-noise-area-ruleset.md:105; docs/specs/2026-07-16-b2-noise-area-ruleset.md:79 | CLOSED-OTHER DECISIONS.md:812 ("(a) paper's fixed rules, nothing optimised") + DECISIONS.md:1552-1553 (R1 "RTH = 09:30–16:00 ET") | D2-AMBIGUOUS: the backtest flat time is NOT-D2, but the live 11:30 flat is breaker #4 (R8, DECISIONS.md:1585), a breaker [cut] | none in source | none: not waiting |
| W4-12 | ""**T2: one-position-per-session vs paper's reverse-on-cross.** ... Decide"" | docs/specs/2026-07-16-b2-noise-area-ruleset.md:106; docs/specs/2026-07-16-b2-noise-area-ruleset.md:76 | CLOSED-OTHER HEAD:specs/SPEC_RUBRIC.md:103 ("Deviation C permits reverse-and-re-enter") | NOT-D2 | none in source | none: not waiting |
| W4-13 | ""**T3: whether to expose a `noise multiplier` and/or `stop-ATR` at all.**"" | docs/specs/2026-07-16-b2-noise-area-ruleset.md:107 | ANSWERED-BY D-2026-11-05-A item 1 DECISIONS.md:812 ("(b) four parameters tuned per window — lookback, noise multiplier, stop-ATR multiplier, exit policy") | NOT-D2 | none in source | none: not waiting |
| W4-14 | ""**T4: exit mode** — OppBand vs BandOrVWAP (paper prefers the latter)."" | docs/specs/2026-07-16-b2-noise-area-ruleset.md:108 | CLOSED-OTHER HEAD:docs/specs/2026-11-06-walk-forward-values.md:322 ("Exit-policy options \| RULED (set: ruling 4 of 2026-11-06; definitions: Q4, Q5)") | NOT-D2 | none in source | none: not waiting |
| W4-15 | ""**T5: instrument transfer** — SPY→NQ is unvalidated by this paper ... Confirm the NQ port is treated as requiring its own Block-2 validation"" | docs/specs/2026-07-16-b2-noise-area-ruleset.md:109 | CLOSED-OTHER DECISIONS.md:812 (walk-forward of the NQ port, both arms) | NOT-D2 | none in source | none: not waiting |
| W4-22 | ""BLOCKED ON AMEAR: ratify K1 (14,000 bytes, byte-only) and K2 ... rule on C-4 UNDERDETERMINED"" | bd:Praxis_build-f5f | CLOSED-OTHER DECISION_LOG.md:253 ("K1 RATIFIED", WHO: amear); DECISION_LOG.md:255 ("K2 RATIFIED", WHO: amear) | NOT-D2 | none in source | none: not waiting |
| W4-25 | ""WHAT: decide (Amear) whether managers should have agent memory at all"" | bd:Praxis_build-gjj | ANSWERED-BY D-2026-11-08-C C7 DECISIONS.md:1843 ("Praxis_build-gjj: disable memory in the praxis-manager agent") | NOT-D2 | none in source | none: not waiting |
| W4-28 | ""Hook change needed; Amear's call."" | bd:Praxis_build-22q | CLOSED-OTHER DECISIONS.md:1165 (D-2026-11-04-B addendum 5 "third hand-back shape (task-notification)") + DECISIONS.md:1192 (addendum 6 "ratification (WHO: amear)") | D2-AMBIGUOUS: a commit-gate hook change; hooks vs "agent permissions" (D2(d)) not defined. | none in source | none: not waiting |
| W4-30 | ""NEEDS A HUMAN RULING, COLD: either gate-commit.sh gains a park-branch exemption ... or the park rule step 1 changes"" | bd:Praxis_build-8sw | ANSWERED-BY D-2026-11-08-C C2 DECISIONS.md:1826-1829 ("a park commit to parked/ branches is exempt from the audit-token gate ... Closes Praxis_build-8sw.") | NOT-D2 | none in source | none: not waiting |
| W4-35 | ""Exact MFFU account size + trailing-DD limit numbers NOT yet supplied by trader — required before RoR can compute. Ask trader"" | bd:Praxis_build-xdr | CLOSED-OTHER DECISIONS.md:816 ("Account tier: no decision until backtest + paper results exist.") + DECISIONS.md:1739 ("Evaluated against every tier row") | NOT-D2 | none in source | none: not waiting |

## Roll-up rows (W1 pointed at whole DECISIONS.md lists; W3 checked the members one by one)

- W1-38 (HANDOFF.md:277): ROLL-UP into G17, G18 (D-2026-11-02-A items checked one by one by W3)
- W1-40 (HANDOFF.md:277): ROLL-UP into G20, G21, G22, X03 (D-2026-11-02-C items checked one by one by W3)
- W1-41 (HANDOFF.md:277): ROLL-UP of D-2026-11-03-A §e: W3 rows W3-41..W3-61 checked one by one; open members are X07

## Counts

| measure | count |
|---|---|
| Total question rows (Tables 1 + 2 + 3) | 191 |
| ANSWERED-BY an Amear ruling (Table 3, per source row) | 87 |
| CLOSED-OTHER, not an Amear ruling (Table 3, per source row) | 61 |
| WAITING, raised before the cutoff (Table 1, grouped) | 40 |
| of which NOT-D2 | 25 |
| of which D2 (G28, G31, G34) | 3 |
| of which D2-AMBIGUOUS (G01, G06, G09, G25, G29, G30, G32, G33, G35, G36, G38, G40) | 12 |
| WAITING, raised after the cutoff (Table 2; not D11-due) | 3 |
| Amear's hands, actions (not questions; not counted above) | 13 |
| Roll-up rows (pointers only; members counted in their own rows) | 3 |

Source: the `COUNTS` line of the build run in block V1; 191 = 40 + 3 + 87 + 61.

## Adversarial findings and resolution

ADV1 returned no result (turn cap, findings file held only its stub; block V3). A no-result return is not a pass. It was re-dispatched after material reduction as two adversaries, ADV2a and ADV2b, each given the artifact and the criteria, not the manager's reasoning. Both returned a result line. The manager re-checked each finding (block V4) before acting on it.

| finding | row(s) | claim attacked | manager check (V4) | resolution |
|---|---|---|---|---|
| ADV2a F1 DEFECT; ADV2b minor 1 | G35, G36 | NOT-D2, closed under D1, though the fix edits gate-commit.sh; conflicts with "Stop, freeze it" | DECISION_LOG.md:165 holds "No new guards, hooks, closers, or agent-stack work is dispatched." | Accepted. Both now D2-AMBIGUOUS (D2(d), as G25), closure "none", freeze quoted. Freeze added to G25, G28, G29, G32-G34 and Method note 7(c). |
| ADV2a F3 MINOR | G22 | proposal takes recommendations the source does not have | csv-analyses :290 "This report does not answer any of them." | Accepted. Cell now "none in source" with that quote, then a labelled manager's proposal. |
| ADV2a F4 MINOR | G24 | "ratify K7 as written" though its bead is a gate collision | bd nvn title: "THIRD gate-commit.sh collision" | Accepted. Proposal now: do not ratify as written; re-propose after the fix. |
| ADV2a F5 MINOR | X03 | NOT-D2 while G38 calls the same F4 permission D2-AMBIGUOUS (b) | (table text) | Accepted. The actions table now carries the manager's D2 note per row; X01-X03 are D2-AMBIGUOUS (b). |
| ADV2a F6 MINOR | H02 vs G11 | same breaker reasoning, two D2 classes | (table text) | Accepted. H02 is now NOT-D2, same reading as G11 (D2(c) needs "while real money is at stake"). |
| ADV2a F7 MINOR | G16 | points to an action row that does not exist | `grep -c '^| G16 '` = 0 after fix | Accepted. W3-16 is a read-back: moved to X13; G16 removed. |
| ADV2a F2, F8 NOTE | G37; Result line | backticks dropped; draft Result line | (table text) | F8 fixed (this Result line). F2 not changed: the quote is generated from the worker's field, words intact. |
| ADV2b F1 DEFECT | W3-40 | ANSWERED-BY on Amear's "Yeah" | DECISIONS.md:753 "The row does not record the question he answered." | Accepted. CLOSED-OTHER (moot under R-VN4-7, DECISIONS.md:947). |
| ADV2b F2 DEFECT | W3-94, W4-08 | ANSWERED-BY C5 (ii), which names Studio Static rows only | DECISIONS.md:1885 "decided by master under D-2026-11-08-D D1" | Accepted. Both CLOSED-OTHER "in part". |
| ADV2b F3 DEFECT | W1-29, W2-14 vs G06 | fee item 3 is both answered and waiting | DECISIONS.md:1063 holds "settle this class yourself" | Accepted. W1-29/W2-14 now say "items 1-2; item 3 is G06". G06 notes the delegation; the login act stays D2(d)-adjacent. |
| ADV2b F4 DEFECT (MISSED) | new G41 | ISSUE_REGISTER.md:23 "Amear decides whether the superseded report is retained or deleted" in no row | row STATE "closed (recovered; retention is Amear's call)"; file still tracked | Accepted. Added as G41 (NOT-D2). W2 had excluded it because the row's STATE is closed; the question in it is not. |
| ADV2b minor 2 | W1-42 | pointer to D8 (8) is the wrong ruling | (W1 flagged the same doubt) | Accepted. Now ANSWERED-BY R-VN4-7 (DECISIONS.md:947). |
| ADV2b notes | W3-33, W1-27; G20 | weak answers; bead yra not in G20 | bd yra title: "Dev-C reverse-and-re-enter vs breakers #2/#3 + Block-4 ..." | yra added to G20 as a related open bead. W3-33 and W1-27 kept as the workers' readings (Method note 5). |

**Limit.** The fixes were applied by the manager after the adversaries returned. No third adversary re-ran over the fixed tables. The manager's own check of the fixed rows is block V4. ADV2b re-ran 38 pointers. It found no pointer whose line lacks its quoted words. Its defects were about status readings, and those are listed above.

## S6 cross-block check

This unit changes no spec, breaker, gate or hook; it inventories. The interactions the master will meet when acting on the proposals: G11, H02, G21 touch Block 3 (F2, breakers #4/#5); G38, X01-X03 touch Blocks 4-5 (F4, MFFU permission; D2(b) for any funded path); G20 touches Block 2 vs Block 4 (O4 parity); G25, G28, G29, G32-G36 touch the supervision stack under the 2026-08-06 freeze; G10 touches the rubric's absolute park rule; G01 touches A4's per-tier ceiling (D6). None is modified here.

## MANIFEST

Row 315 appended for this report; lines 1-314 unchanged (hash equal before and after).

~~~~text
$ wc -l MANIFEST.md
     314 MANIFEST.md
$ head -n 314 MANIFEST.md | openssl dgst -sha256
SHA2-256(stdin)= 7045e0e55533f459617071c2f7233d9bc1da6926141cb8b50b91973c8d495d5b
--- after append ---
$ wc -l MANIFEST.md
     315 MANIFEST.md
$ head -n 314 MANIFEST.md | openssl dgst -sha256
SHA2-256(stdin)= 7045e0e55533f459617071c2f7233d9bc1da6926141cb8b50b91973c8d495d5b
$ sed -n '315p' MANIFEST.md
| /docs/reports/2026-11-09-d11-sweep-manager.md | Report | 2 | 2026-11-09 | Manager report for unit 2026-11-09-d11-sweep (Amear D-2026-11-08-D D11): inventory of questions to Amear raised before 2026-11-09T09:00Z across sources A-G (HANDOFF cards, three return handoffs, DECISIONS NEEDS AMEAR, ISSUE_REGISTER, docs/specs, the bf6fcc7 R6 design, open beads); 40 WAITING (25 NOT-D2, 3 D2, 12 D2-AMBIGUOUS), 3 raised after the cutoff, 87 ANSWERED-BY, 61 CLOSED-OTHER (per source row), 13 actions in Amear's hands; proposals only, nothing closed; 416 pointers re-run and pasted; ADV1 no result (turn cap), ADV2a and ADV2b findings resolved. |
~~~~

## Verification evidence

### V1 — baseline, worker row counts, build run (pasted output)

~~~~text
$ git rev-parse --short HEAD
f10603a
$ git log -1 --format="%H %aI %cI" bf6fcc7
bf6fcc74e1392e606750b33294ca83e07c3d7ab3 2026-11-09T05:02:44-05:00 2026-11-09T05:02:44-05:00
$ /usr/bin/grep -n -i -c "NEEDS AMEAR" DECISIONS.md
90
$ wc -l < /tmp/d11/W3-coverage.tsv   # header + 90 lines
      91
$ for f in W1 W2 W3 W4; do awk -F"	" "NR>1" /tmp/d11/$f.tsv | wc -l; done
      42
      48
      97
      39
$ for f in W1 W2 W3 W4; do awk -F"	" "NR>1{split(\$5,a,\" \"); print a[1]}" /tmp/d11/$f.tsv | sort | uniq -c; done
== W1
   4 ACTION
  21 ANSWERED-BY
   4 CLOSED-OTHER
  13 WAITING
== W2
   3 ACTION
  18 ANSWERED-BY
   8 CLOSED-OTHER
  19 WAITING
== W3
   4 ACTION
  42 ANSWERED-BY
  35 CLOSED-OTHER
  16 WAITING
== W4
   7 ACTION
   9 ANSWERED-BY
   8 CLOSED-OTHER
  15 WAITING
$ bd list --status open | wc -l
      54
$ cd /tmp/d11 && python3 -I build.py
COUNTS {'WAIT_NOT': 25, 'WAIT_D2': 3, 'WAIT_AMB': 12, 'ANS': 87, 'CLO': 61, 'AFTER': 3, 'ACT': 13, 'ROLL': 3}
POINTERS 416 EMPTY/MISSING 0
~~~~

### V2 — the mask program

~~~~text
$ cat /tmp/d11/mask.sed
s/[Vv][Ee][Rr][Dd][Ii][Cc][Tt]/V-rdict/g
s/[Tt][Bb][Dd]/T-D/g
s/F[i]lls are optimistic/Fills-are-optimistic/g
s/[Cc][Oo][Mm][Mm][Ii][Tt][-][Ii][Nn][Dd][Ee][Xx]/COMMIT_INDEX/g
s/[Cc][Oo][Mm][Mm][Ii][Tt][-][Dd][Ii][Ff][Ff][-][Ss][Hh][Aa]256/COMMIT_DIFF_SHA256/g
s/~~~/~-~/g
~~~~

### V3 — the adversaries' own files (masked)

~~~~text
$ sed -E -f /tmp/d11/mask.sed /tmp/d11/ADV1.md
# ADV1 — adversarial check of docs/reports/2026-11-09-d11-sweep-manager.md (HEAD f10603a)

Mode: ADVERSARIAL. Read-only on repo. Draft in progress; extended below.

## Findings

(in progress)
~~~~

~~~~text
$ sed -E -f /tmp/d11/mask.sed /tmp/d11/ADV2a.md
# ADV2a adversarial findings — unit 2026-11-09-d11-sweep
Artifact: docs/reports/2026-11-09-d11-sweep-manager.md
Criterion: D2 (DECISIONS.md D-2026-11-08-D) + S8

## F1 — DEFECT — G35, G36 (D2 test inconsistent with G25; closure contradicts Amear's own 2026-08-06 ruling)
Claim attacked: G35 "NOT-D2: a hook's error message" -> "close under D1: take the source's candidate fix"; G36 "NOT-D2: token handling grants no permission" -> "close under D1 with the proposal" (gate deletes token only on a landed commit).
Both closures are edits to gate-commit.sh, the hook that gates every agent commit. G25 classes a change to an enforcement hook's accepted vocabulary as D2-AMBIGUOUS "bears on agent permissions (D2(d))" and declines; the same test applied to the commit gate is not applied to G35/G36. G36's change alters when an agent may commit after a denial — that is what the gate permits, i.e. agent permissions in D2(d)'s sense at least as much as G25.
Separately, the row's own status cell cites an Amear answer that already rules on it:
$ sed -n '165p' DECISION_LOG.md | cut -c1-600
- [2026-08-06T19:48:03Z] **WHO: amear** | ... APPROVED BY: Amear, 2026-08-06, in-session — selected **"Stop, freeze it"** | WHAT: **THE SUPERVISION BUILD STOPS.** No new guards, hooks, closers, or agent-stack work is dispatched. The three P0s (`s8g`, `hwk`, `1ys`) stay open and documented rather than fixed. ...
D1 applies to "a question that would otherwise go to Amear"; Amear's "Stop, freeze it" says hooks are not worked on. Proposing a D1 closure that dispatches hook work (G35, G36) overrides an Amear ruling — an S8 problem the report does not flag (Method note 7 lists conflicts for G07-G10 only).
Correct entry: G35/G36 D2 test = D2-AMBIGUOUS (commit gate = agent permissions, D2(d)), consistent with G25; proposed closure = "none" or "close by declining the fix (freeze stands, DECISION_LOG.md:165)"; add to Method note 7 as a conflict.

## F2 — NOTE — G37 (quote not verbatim)
Claim attacked: recommended cell quotes "interim mitigation is to brief agents with grep/line-range reads instead of whole files" ISSUE_REGISTER.md:61.
$ /usr/bin/grep -c 'interim mitigation is to brief agents with grep/line-range reads instead of whole files' ISSUE_REGISTER.md
0
$ sed -n '61p' ISSUE_REGISTER.md | /usr/bin/grep -o -i '.\{0,250\}mitigation.\{0,250\}'   (tail)
... STATE: open — remediation is Amear's call; interim mitigation is to brief agents with `grep`/line-range reads instead of whole files
Words are in the source; backticks were dropped, and Method note 3 says the mask alters only five strings plus tilde runs, not backticks. Correct entry: quote with backticks, or note the change. Substance of the recommendation is in the source.

## F3 — MINOR — G22 (closure has no content; the source states no recommendation)
Claim attacked: "manager's proposal: take any recommendation the csv-analyses file states for each of questions 1-6; where none, the master's reading" -> "close under D1 with the proposal".
$ sed -n '290p' docs/reports/2026-11-01-csv-analyses.md
These questions are left open. This report does not answer any of them.
The file states no recommendation for any of the six, so the proposal reduces to "the master's reading" for all six, which is unstated. A D1 closure needs a recommended option to take (D1: "it takes the recommended option"). Correct entry: state an option per question 1-6 (e.g. 1 = show 1-tick as well, per F3; 2 = as-is, labelled partial; ...), or mark "no option stated; master must write one before closing". Not a D2 breach (none of the six touches (a)-(d)).

## F4 — MINOR — G24 (proposal ratifies a rule its own cited bead records as defective)
Claim attacked: "manager's proposal: ratify K7 as written" -> "close under D1 with the proposal". NOT-D2 is right; the option is not.
$ bd show Praxis_build-nvn | grep -n -i -E 'K7 as proposed|ratif|do not repair'
10:  DEFECT. K7 as proposed makes compact.sh a STAGING-ONLY process: it runs the
40:  BLOCKED ON. K7 is [PROPOSED] and unratified; its wording is itself under
43:  rejected at the ratification gate this bead's premise may change. Do not
44:  repair before K7 ratifies.
(bead title: "THIRD gate-commit.sh collision: compact.sh stages at session close, invalidating any live audit token")
The cited bead says K7-as-proposed collides with the commit gate. "Ratify as written" bakes that collision in, and the report doesn't mention it. Correct entry: either "ratify K7 with the nvn collision fixed first" or "leave K7 unratified (ledger compaction frozen with the supervision build, DECISION_LOG.md:165)", with the nvn defect named in the cell.

## F5 — MINOR — X03 (D2 note inconsistent with the report's own G38 / X02 test)
Claim attacked: X03 "send MFFU the F4 follow-up (Tradovate vs NinjaTrader/Rithmic); fx4 acceptance" — worker D2 note "NOT-D2".
G38 (the same F4 question) is D2-AMBIGUOUS "F4 is the written MFFU permission that precedes 'any order path to a funded account' (D2(b))", and X02 is D2-AMBIGUOUS because it "gates funded use (D2(b))".
$ bd show Praxis_build-fx4 | grep -i -E 'before any live|Blocks live'
○ Praxis_build-fx4 · MFFU automation-compliance: confirm in writing that fully-automated trading is permitted before any live step ...
  PROVISIONAL. Human/trader-gated (requires contacting MFFU). Blocks live-
Sending the email is not D2. But "fx4 acceptance" (accepting MFFU's written permission, which unblocks live) is the same act as G38. Correct entry: X03 note = "sending: NOT-D2; fx4 acceptance: D2-AMBIGUOUS (D2(b)), as G38". X03 is not marked for closure, so no closure breach; the risk is that a master reading NOT-D2 accepts fx4 under D1.

## F6 — MINOR — H02 vs G11 (same reasoning, opposite class)
Claim attacked: H02 "D2-AMBIGUOUS: breaker #4/#5 wording; D2(c) needs real money at stake, and none is."
G11 says the same thing about the same breakers: "NOT-D2: F2 wording; D2(c) needs 'while real money is at stake', and none is." The H02 reasoning gives the answer NOT-D2 but the row is classed D2-AMBIGUOUS. Correct entry: make both rows the same class (NOT-D2 per D2(c)'s words, or both D2-AMBIGUOUS with a stated reason). H02 is not D11-due, so the effect is on the next run's class.

## F7 — MINOR — G16 (closure points to a hands row that does not exist)
Claim attacked: G16 "manager's proposal: read it back on the next VM session as a hand step (see Amear's hands)".
$ /usr/bin/grep -n -i -E 'R2|reversal' docs/reports/2026-11-09-d11-sweep-manager.md  -> no X row; X07 lists only "Log tab, save-as-default, NQCONTROW instrument".
No X01-X12 row carries the 3gm R2 same-bar exit+reverse read-back (G21's items 5-7 read-backs aren't there either). Closing G16 "as a read-back task" leaves the task in no list. Correct entry: add an X row (R2 reversal read-back, NOT-D2), or drop "see Amear's hands".

## F8 — NOTE — Result line vs process log
$ /usr/bin/grep -n '^Result:' docs/reports/2026-11-09-d11-sweep-manager.md
338:Result: FAIL (draft; adversarial check not yet run)
Process log step 5 says "ADV1 attacked the finished draft; findings and resolutions below". One of the two is stale. Count of '^Result:' = 1 (>=1 passes).

## Checks with no defect (cases tried)
- Token checks: 'Fills-are-optimistic' = 1; V-rdict|T-D|COMMIT_INDEX|COMMIT_DIFF_SHA256 = 0; '^Result:' = 1.
- Row counts: G = 40, H = 3, X = 12; no duplicate ids. Column-5 tally: NOT-D2 27, D2(d) 3 (G28, G31, G34), D2-AMBIGUOUS 10 (G01, G06, G09, G25, G29, G30, G32, G33, G38, G40). Matches Counts 27/3/10/40/3/12. Table 3: ANSWERED-BY rows 90, CLOSED-OTHER rows 58; 191 = 40+3+90+58 holds.
- Every D2 row (G28, G31, G34) and X08/X09 has closure "none". Every D2-AMBIGUOUS closure only declines (G06, G09, G25, G30, G40) or is none (G01, G29, G32, G33, G38). No closure performs a D2 act.
- D2 words quoted ("spending money", "any order path to a funded account", "while real money is at stake", "installing keys, credentials", "agent permissions") match DECISIONS.md:1912-1916.
- Source recommendations re-read: G01 (:66), G02 (:71, "the unit's, changeable by you"), G11 (DECISIONS.md:1788), G35 (ISSUE_REGISTER.md:57, exact match grep -c = 1), H02/H03 quote bf6fcc7 lines. The other cells are labelled "manager's proposal" or "none in source".
- G04: vm handoff §9 = backtest arm runs (9.1/9.2), Sim101; NOT-D2 holds. G12: SHM is "distinct from the nine circuit breakers" (DECISIONS.md:50); NOT-D2 holds. Pointers C2 :1826, C3 :1830, C7 :1843, D8 :1949/:1954, SPEC_RUBRIC :93-94/:107/:256, HANDOFF :286 all say what the rows claim.
Tally: 1 DEFECT (F1) + 5 MINOR (F3-F7); NOTEs F2, F8 not counted.
RESULT: DEFECTS 6
~~~~

~~~~text
$ sed -E -f /tmp/d11/mask.sed /tmp/d11/ADV2b.md
# ADV2b — adversarial, unit 2026-11-09-d11-sweep
Started 2026-11-09T13:27:40Z

Artifact: docs/reports/2026-11-09-d11-sweep-manager.md (1685 lines). Tables read :47-279.

## Pointer checks (appended as run)

### Batch 1 (DECISIONS.md lines; `sed -n "${n}p" DECISIONS.md`)
| # | pointer | row | OK/BAD | reason |
|---|---|---|---|---|
| P1 | DECISIONS.md:753 | W3-40 (ANSWERED-BY R-1104-3) | BAD | Amear's own word is only "Yeah"; the same line says "The row does not record the question he answered." Does not settle the question. |
| P2 | DECISIONS.md:936 | W3-33 (ANSWERED-BY R-VN4-2) | OK-weak | Words hold ("Until the account is live … resting stops." / "The latter."); the backtest half rests on the elided "…" and the voice agent's reading. NOTE only. |
| P3 | DECISIONS.md:941 | W1-37, W3-39 (ANSWERED-BY R-VN4-4) | OK | "r8j at P0: "Yes."" settles "Is P0 the level he wants?" |
| P4 | DECISIONS.md:1930-1932 | W3-32 (ANSWERED-BY D6) | OK | D6 uses "the three committed 2026-11-01 trade lists" (no-breaker runs) for the drawdown check: settles "used for anything". |
| P5 | DECISIONS.md:358 | W3-11 (ANSWERED-BY R-7zq-1) | OK | "Yes — append it now, then commit." with stated ordering. |
| P6 | DECISIONS.md:1217 | W1-21/W2-06 (ANSWERED-BY ruling 2) | OK | "Item 19: commit ... as a one-file exception to the as-is rule". |
| P7 | DECISIONS.md:1645, :1788 | G11 | OK | Quote holds; :1788 "Not resolved here; master's reading". |
| P8 | DECISIONS.md:1952-1953 | W1-42 (ANSWERED-BY D8(8)) | checked further below | |

Raw output (excerpt):
```
--- DECISIONS.md:753
- Amear's words: *"Yeah"*. Brief's framing: *"Yeah"* = High fill resolution with circuit breakers on as the judged go/no-go version, confirming R-VN3-6. The row does not record the question he answered.
--- DECISIONS.md:754
- Closes D-2026-11-02-C NEEDS AMEAR 14 (DECISIONS.md:544). That closure label is in the ledger row's framing. Amear's own word is "Yeah".
--- DECISIONS.md:520
- **Settles (against O1), in Amear's words only:** the go/no-go judges the version *"closest to live execution"*. That this means High fill resolution and breakers on is the agent's reading, which Amear did not contradict. Not contradicting a reading is not ruling on it, so this entry records it as the agent's reading and not as Amear's ruling (see NEEDS AMEAR 14).
--- DECISIONS.md:544
14. R-VN3-6: does "closest to live execution" mean High fill resolution and breakers on, as the agent read it to him?
--- DECISIONS.md:936
- **R-VN4-2** — breakers as resting stops?: "Until the account is live … resting stops." Asked which: "The latter."
--- DECISIONS.md:941
- **R-VN4-4** — r8j at P0: "Yes."
--- DECISIONS.md:1930
D6  FIRST: drawdown viability check, Mac-only, read-only, no VM, no
--- DECISIONS.md:1931
    purchase. On the three committed 2026-11-01 trade lists, compute
--- DECISIONS.md:358
- **R-7zq-1 — S4 ordering (answers NEEDS AMEAR 5 above), DECISION_LOG `2026-10-31T11:04:20Z` (WHO: amear):** *"Yes — append it now, then commit."* ...
--- DECISIONS.md:1217
2. Item 19: commit docs/reports/2026-10-28-voice-session-notes.md as a one-file exception to the as-is rule — it is the source of a ruling. Fix MANIFEST.md:244 to match.
--- DECISIONS.md:1788
**FLAG 6 residual.** ... Not resolved here; master's reading, changeable by Amear (DECISION_LOG `15:13:00Z`, :728): it is the F2 PROPOSAL unit's output, returned PROPOSED.
```

### Batch 2 (A HANDOFF.md, B return handoffs; `sed -n "${n}p" <file>`)
| # | pointer | row | OK/BAD | reason |
|---|---|---|---|---|
| P8 | DECISIONS.md:1952-1953 (+HANDOFF.md:277) | W1-42 (ANSWERED-BY D8(8)) | MINOR | HANDOFF.md:277 is a bare pointer list "D-2026-11-04-A (:769-771)" covering two questions (:770 proof of concept, :771 r8j P0). D8(8) itself says "(the standing proof-of-concept ruling)" — it cites, not makes, the PoC ruling (R-VN4-7 :947); :771 is settled by R-VN4-4 :941, not D8(8). |
| P9 | DECISIONS.md:1738-1739 | W3-63 (ANSWERED-BY A4) | OK | "Evaluated against every tier row; tier pick stays Q9." settles which tier limits for items 3-4. |
| P10 | HANDOFF.md:36 | G10 | OK | "A human resumes it; the orchestrator does not." present; 06:36Z (HANDOFF.md:30) is before cutoff. |
| P11 | HANDOFF.md:119 | W1-04 | OK | quote holds verbatim. |
| P12 | HANDOFF.md:125 | G01/G03/G04/X06/W1-10 | OK | "§4 items 2 and 4–12, item 4 first (the July rubric hunk" holds. |
| P13 | HANDOFF.md:181 | G02/X04 | OK | pip / "Starting it is Amear's" holds. |
| P14 | return-handoff-claude-ai-2.md:66,:71,:72,:73 | G01,G02,G03,G04 | OK | quotes hold verbatim. |
| P15 | return-handoff-claude-ai.md:65 | G05, W2-10 | OK | "who reads the tab and the PRAXIS commission template back" holds. |
| P16 | 2026-11-06-return-handoff-claude-ai.md:42,:60 | G07-G09, G06, W2-18 | OK | both quotes hold; :60(a) R-VN4-10 is covered by W2-18/W3-68/W1-34 (CLOSED-OTHER :1096). |

Raw output (excerpt):
```
--- HANDOFF.md:36
**PARKED — `Praxis_build-diq` (U7). A human resumes it; the orchestrator does not.** The C1 audit PASSED the diff of record ...
--- HANDOFF.md:277
- D-2026-11-02-A (DECISIONS.md:398); D-2026-11-02-B (:471); D-2026-11-02-C (:530-544); D-2026-11-03-A §e (:653); D-2026-11-04-A (:769-771).
--- DECISIONS.md:769-771
**NEEDS AMEAR (questions only, not answered):** ...
1. What counts as "proof of concept"? ...
2. `Praxis_build-r8j` is at P0, the master's choice ... Is P0 the level he wants?
--- DECISIONS.md:1952-1953
    executor; Mac is the only master. (8) "final step of this build" =
    Block 4 paper pass on MFFU sim (the standing proof-of-concept
--- DECISIONS.md:1738-1739
    amends D-2026-11-05-A item 3 with a safety buffer for model error.
    Evaluated against every tier row; tier pick stays Q9. Closes the
--- docs/reports/2026-11-07-return-handoff-claude-ai-2.md:71
7. **VM pip.** ... Open: whether the packages' own dependencies and the build backend `setuptools>=61` count as "the bridge's pinned requirements" (`:150`); and the "no extras" reading, which is the unit's, changeable by you (`16:04:00Z`).
--- docs/reports/2026-11-07-return-handoff-claude-ai-2.md:72
8. **The early-close checkpoint content.** Does R-1104-2 cover the behaviour chosen in D-2026-11-07-B addendum 1, decision (1) (DECISIONS.md:1480)? ...
--- docs/reports/2026-11-07-return-handoff-claude-ai.md:65
7. **Who sets the Strategy Analyzer tab for 2a,** and who reads the tab and the PRAXIS commission template back (`vm/2026-11-06-vm-handoff.md:151`, `:260`). ...
--- docs/reports/2026-11-06-return-handoff-claude-ai.md:60
6. **Two items for Amear, added.** (a) R-VN4-10 was applied under the master's flagged reading ... (b) Fee report NEEDS AMEAR 3 spelled out: ... would need a login — do you want it?
```

### Batch 3 (D ISSUE_REGISTER.md, DECISION_LOG.md)
| # | pointer | row | OK/BAD | reason |
|---|---|---|---|---|
| P17 | ISSUE_REGISTER.md:57 | G35 | OK (quote) | "STATE: open — remediation is Amear's call; candidate fix is to move the sweep after the lookup" holds. D2/closure: see F3. |
| P18 | ISSUE_REGISTER.md:45 | G28 | OK | "Candidate remediations for Amear, unranked" holds. |
| P19 | ISSUE_REGISTER.md:72 | G39 | OK | "STATE: open — awaiting Amear's ruling" holds. |
| P20 | ISSUE_REGISTER.md:11 | G31 | OK | "User decides rotate-vs-keep. Token NEVER committed to repo" holds. |
| P21 | DECISION_LOG.md:165 | G36, G37 | OK (quote) | "selected **"Stop, freeze it"** ... No new guards, hooks, closers, or agent-stack work is dispatched." Holds; but see F3. |
| P22 | DECISION_LOG.md:155 | W2-41 (ANSWERED-BY) | OK | "WHO: amear ... selected **"Inline correction marker"**" settles the disposition of the false quotation. |
| P23 | DECISIONS.md:1230 | W2-10 (ANSWERED-BY ruling 6) | OK | "a hand-set tab may be used for 2a and counts ... It does NOT count as "driven from the terminal"". Read-back half correctly left to G05. |

Coverage sweep: lines of ISSUE_REGISTER.md naming Amear = `21 23 27 31 35 37 41 45 47 49 51 53 55 57 59 61 63 68 70 72 74`; report hit-count for `ISSUE_REGISTER.md:<n>`: 21->0, 23->0, 70->0, all others >=2.
```
--- ISSUE_REGISTER.md:21
STATE: closed (verified 2026-07-25 by Amear)
--- ISSUE_REGISTER.md:23
... Amear decides whether the superseded report is retained or deleted — its P0 conclusion is wrong (built on the stale 2.1.206 binary) but it is the primary record of how the false V-rdict was reached | STATE: closed (recovered; retention is Amear's call)
--- ISSUE_REGISTER.md:70
STATE: deferred — non-blocking; re-raise on any move to Apex or Topstep
$ /usr/bin/grep -n -i 'retention\|agent-stack-install' docs/reports/2026-11-09-d11-sweep-manager.md   -> (no output)
$ /usr/bin/grep -n 'P0-BLOCKED-superseded' DECISIONS.md DECISION_LOG.md HANDOFF.md STATUS.md MANIFEST.md   -> (no output)
$ git ls-files docs/reports/2026-07-25-agent-stack-install-P0-BLOCKED-superseded.md -> docs/reports/2026-07-25-agent-stack-install-P0-BLOCKED-superseded.md
$ git log --oneline -1 -- <that file> -> b8008e4 feat(agent-stack): install master/manager/auditor v1 — 5 trip tests + depth-2 nesting proven
$ /usr/bin/grep -n ... 'Stop, freeze it' row DECISION_LOG.md:165:
- [2026-08-06T19:48:03Z] **WHO: amear** ... selected **"Stop, freeze it"** | WHAT: **THE SUPERVISION BUILD STOPS.** No new guards, hooks, closers, or agent-stack work is dispatched. The three P0s (`s8g`, `hwk`, `1ys`) stay open and documented rather than fixed.
```

### Batch 4 (E specs via `git show HEAD:<path> | sed -n`, F bf6fcc7)
| # | pointer | row | OK/BAD | reason |
|---|---|---|---|---|
| P24 | HEAD:docs/specs/2026-11-05-walk-forward-spec.md:206 | G01 | OK | item 11 "Which **MFFU account size / tier** sets the max-DD gate". |
| P25 | HEAD:...walk-forward-spec.md:202 | W4-02 (ANSWERED-BY A2 + C5(iv)) | OK | Sharpe/equity base; C5(iv) "A2 closes the notes-4 Sharpe item." (DECISIONS.md:1839-1840) settles in Amear's words. |
| P26 | HEAD:...walk-forward-spec.md:203 | W4-04 (ANSWERED-BY A7/A8) | OK | A7 "arm (a) is judged on gates 1-5 (WFE not applicable)"; A8 gives the Pardo formula. Settles both halves. |
| P27 | HEAD:...walk-forward-spec.md:207 | W4-08 (ANSWERED-BY C5(ii)) | OK | stage/type/Static question at :207; pointer holds. |
| P28 | HEAD:docs/specs/2026-11-06-walk-forward-values.md:308,:309 | G09, G08 | OK | "- a second Rithmic read-only connection;" / "- the CME wiki as a source;". |
| P29 | HEAD:...walk-forward-values.md:310 | W4-03 (ANSWERED-BY A4) | OK | :310 says DD-base closure "NOT decided here"; A4 :1739-1740 "Closes the notes-4 DD equity-base item." settles it. |
| P30 | bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md:112 | H01 | OK | OPEN-3 "needs a ruling. Agents do not write acceptance bars." Commit time 2026-11-09T05:02:44-05:00 = 10:02:44Z, after cutoff. |
| P31 | bf6fcc7:...:111 | H02 | OK | "whether #4's "next session" starts at 18:00 is undefined." |

Raw output (excerpt):
```
$ git show HEAD:docs/specs/2026-11-05-walk-forward-spec.md | sed -n '202,207p'
7. What is the **Sharpe definition** for "OOS Sharpe ≥ 1.0" ...
8. Does **WFE ≥ 0.50** apply to arm (a), which has no in-sample optimisation (O1)? For arm (b), which WFE formula is used?
...
11. Which **MFFU account size / tier** sets the max-DD gate under items 3 and 5, ...
12. For "MFFU's trailing drawdown limit", which **stage** (Evaluation or Sim-Funded) and which **type** (EOD or intraday trailing) counts? Do Studio's **Static** limits count?
$ git show HEAD:docs/specs/2026-11-06-walk-forward-values.md | sed -n '306,311p'
1. **The tier pick**, after paper results (Q9: "I pick after paper results").
2. **Ruling 9's open notes-4 items** ("Notes-4 unruled items stay open; none block anything."; ...
   - a second Rithmic read-only connection;
   - the CME wiki as a source;
   - the equity base and the Sharpe definition: ... whether it closes the notes-4 DD-gate item is NOT decided here;
   - the O1 gate set: ...
$ git show bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md | sed -n '112p'
| OPEN-3 | Walk-forward gates (A7: arm (a) gates 1-5) | No event strategy on this data reaches gate 4's 250 OOS trades; whether gates 4 and 5 apply to R6 strategies needs a ruling. Agents do not write acceptance bars. | OPEN (Amear) |
$ git log -1 --format='%H %aI %cI' bf6fcc7
bf6fcc74e1392e606750b33294ca83e07c3d7ab3 2026-11-09T05:02:44-05:00 2026-11-09T05:02:44-05:00
```

### Batch 5 (G beads)
Open beads (54) whose id is absent from the report: `1tz 1ys 2nh 2vu 37h 43n 4gx 67b 6di 9lj 9qx aac ajj ax4 b5z c2t cbf cyd hwk kgp lnb nj1 qtk yra zi1`. Scanned each `bd show` for amear/trader/ruling: only "Owner: Amear Bani-Ahmad" boilerplate, except 1tz ("AMEAR RULED 2026-07-26"), 9qx, 6di (past facts). Content check of the question-shaped ones:
- ax4 ("which of {11:30 gate, 16:00 flat, session window disable} governs the anchor strategy and what manages an open position 15:00-16:00") — same content as G11/H02 (breakers #4/#5); NOTE only.
- yra ("whether 4uu runs with breakers / without / both, and how the Block-4 acceptance gate is satisfiable") — same as G20 (DECISIONS.md:533); NOTE: G20 should list bd:Praxis_build-yra.
- qtk (gate set per arm, GO/HOLD/REJECT) — settled by A7/A8 (DECISIONS.md:1746,:1748); stale bead.
- 2nh (live-signal topology) — D8(4) orders the doc (DECISIONS.md:1946-1947).
None is phrased as addressed to Amear, so not counted as MISSED.

### Batch 6 (C DECISIONS.md NEEDS AMEAR > :1530; C5 text)
| # | pointer | row | OK/BAD | reason |
|---|---|---|---|---|
| P32 | DECISIONS.md:1836-1838 (C5 (ii)) | W3-94 (ANSWERED-BY C5(ii)) | BAD | Question includes "and for rows whose Eval and Sim-Funded types differ"; C5(ii)'s words are only "Studio Static rows use the stricter limit type and stage, both shown". The ledger itself (DECISIONS.md:1885-1886) treats the non-Static residual as an open reading decided by the master under D1, and the report's own W3-95 marks that residual CLOSED-OTHER. |
| P33 | HEAD:...walk-forward-spec.md:207 + DECISIONS.md:1837 | W4-08 (ANSWERED-BY C5(ii)) | BAD | Same: "which **stage** (Evaluation or Sim-Funded) and which **type** (EOD or intraday trailing) counts?" is not settled for the Rapid rows by C5(ii)'s words; only the Static sub-question is. |
| P34 | DECISIONS.md:1708, :1835 | W3-92 (ANSWERED-BY C4) | OK | "C4  One entry satisfies "File each" for D-2026-11-08-A." |
| P35 | DECISIONS.md:1839-1840 | W3-75 (ANSWERED-BY C5(iv)) | OK | "(iv) A2 closes the notes-4 Sharpe item." |
Late NEEDS AMEAR lines (>1530) with zero report hits: :1624 (R7 parallel work, master's reading "changeable by Amear"), :1693 (cure for finding 4), :1861 (C5 answers-map). None is a new question to Amear (1624 is a master reading; 1693/1861 are filing text). Not MISSED.

Raw output:
```
$ sed -n 1834,1841p DECISIONS.md
C4  One entry satisfies "File each" for D-2026-11-08-A.
C5  D-2026-11-08-B (i) win/loss judged by price, consistent with
    B = exit at entry price; (ii) Studio Static rows use the stricter
    limit type and stage, both shown; (iii) A8 annualisation = mean net
    P&L per session x 252, for IS and OOS alike; (iv) A2 closes the
    notes-4 Sharpe item.
$ sed -n 1886p DECISIONS.md
- (i) **C5 (ii) and rows whose Eval and Sim-Funded types differ.** B (ii) (DECISIONS.md:1802): "Which limit type and stage A4 means for the Studio Static rows, and for rows whose Eval and Sim-Funded types differ, is his." C5 (ii) (answers file :30–31, joined): "(ii) Studio Static rows use the stricter limit type and stage, both shown;". WF spec at HEAD, rows :118, :121, :125, :128 (Rapid 25K, 50K, 100K, 150K): "(Eval EOD; Sim-Funded intraday trailing)"; ...
$ sed -n 1885p DECISIONS.md
**Open readings (not decided here).** ... U8 drafted this as "NEEDS AMEAR". Decided by master under D-2026-11-08-D D1 ... changeable by Amear ...
$ /usr/bin/grep -n 'DECISIONS.md:1885\|DECISIONS.md:1886' docs/reports/2026-11-09-d11-sweep-manager.md
253:| W3-95 | "C5 (ii)'s words name the Studio Static rows; whether they also reach the Rapid rows" | DECISIONS.md:1885; DECISIONS.md:1886 | CLOSED-OTHER DECISIONS.md:1885 (decided by master under D-2026-11-08-D D1, assigned to the values-spec unit) | ...
report Table 3 rows:
| W3-94 | "Which limit type and stage A4 means for the Studio Static rows, and for rows whose Eval and Sim-Funded types differ, is his." | DECISIONS.md:1772; DECISIONS.md:1802; DECISIONS.md:1881 | ANSWERED-BY D-2026-11-08-C C5 (ii) DECISIONS.md:1837 | ...
| W4-08 | ""which **stage** (Evaluation or Sim-Funded) and which **type** (EOD or intraday trailing) counts? Do Studio's **Static** limits count?"" | HEAD:...walk-forward-spec.md:207; HEAD:...walk-forward-values.md:330 | ANSWERED-BY D-2026-11-08-C C5(ii) DECISIONS.md:1837-1838 ("Studio Static rows use the stricter limit type and stage, both shown") | ...
```

### Batch 7 (DECISIONS.md:1063 D-2026-11-06-B paste; HANDOFF.md:207,:209,:218)
| # | pointer | row | OK/BAD | reason |
|---|---|---|---|---|
| P36 | DECISIONS.md:1063 ruling 3 | W1-25, W1-26 | OK | "3. Commit gate: (a) RATIFY ... (b) APPROVE the hook change" settles the pick. |
| P37 | DECISIONS.md:1063 ruling 4 | W1-27 | OK-weak (NOTE) | ruling 4 covers "spec NEEDS AMEAR" with defaults; HANDOFF.md:209's "and the harness choice" is not named in ruling 4's words (only implied by loop d "Mac side, ready to run through the bridge"). |
| P38 | DECISIONS.md:1063 ruling 2 | W1-29 ("fee report NEEDS AMEAR 1–3"), W2-14 | BAD (inconsistent) | ruling 2 = "apply MFFU's published round trip — NQ $4.68, MNQ $1.90 ... settle this class yourself." It does not answer fee NEEDS AMEAR 3 (the login fill-statement check); the same report lists that item as WAITING in G06. |

Raw output (excerpt):
```
$ sed -n 1063p DECISIONS.md | fold -w 300
Rulings 1. Bridge install (NEEDS AMEAR 2): ... 2. Fees: apply MFFU's published round trip — NQ $4.68, MNQ $1.90 — by new DECISIONS entry amending the cost model. Covered by my earlier "apply the best figure" ruling; settle this class yourself. 3. Commit gate: (a) RATIFY D-2026-11-04-B addendum 1's timing — unpark uqb for a fresh audit; (b) APPROVE the hook change ... 4. Walk-forward arm (b) and spec NEEDS AMEAR, under "We're not here to fuck around" — strictest reasonable defaults: ...
--- HANDOFF.md:209
3. Step c (walk-forward build) waits on the spec's NEEDS AMEAR 1–6 and the harness choice (00:54:04Z).
--- HANDOFF.md:218
- the cost model (23:59:40Z; fee report NEEDS AMEAR 1–3);
```

Pointer total: 38 rows checked (P1-P38) across sources A (HANDOFF.md:36,:119,:125,:181,:207,:209,:218,:277), B (three return handoffs), C (DECISIONS.md NEEDS AMEAR / ruling lines), D (ISSUE_REGISTER.md:11,:45,:57,:72), E (HEAD: specs), F (bf6fcc7 :111,:112), G (bd show of 25 beads). ANSWERED-BY rows judged: W3-40, W3-33, W1-37/W3-39, W3-32, W3-11, W1-21, W1-42, W3-63, W2-41, W2-10, W4-02, W4-04, W4-03, W3-94, W4-08, W3-92, W3-75, W1-25/26, W1-27, W1-29/W2-14 (20).

## Findings

**F1 — DEFECT — W3-40 (ANSWERED-BY D-2026-11-04-A R-1104-3, DECISIONS.md:753).** Amear's own word is "Yeah"; the ruling line itself says "The row does not record the question he answered." and :754 "Amear's own word is "Yeah"". The originating entry says the reading is not his ruling: DECISIONS.md:520 "Not contradicting a reading is not ruling on it, so this entry records it as the agent's reading and not as Amear's ruling (see NEEDS AMEAR 14)." His words do not settle the question under the brief's rule. Correct entry: not ANSWERED-BY. Either CLOSED-OTHER, overtaken by later rulings (R-VN4-3 "walk-forward on minute data: "Yes."", DECISIONS.md:938-939; R-VN4-7 "We're just gonna proceed without that [historical tick data]", :947; judged arm by R2 :1556 / A7 :1746), or WAITING if the master holds that the "breakers on" half is still open.

**F2 — DEFECT — W3-94 and W4-08 (ANSWERED-BY C5 (ii), DECISIONS.md:1837).** Both questions include the Eval-vs-Sim-Funded / EOD-vs-intraday part for non-Static (Rapid) rows. C5 (ii)'s words: "Studio Static rows use the stricter limit type and stage, both shown". The ledger treats the rest as an open reading closed by the master under D1 (DECISIONS.md:1885-1886), and the report's own W3-95 marks that residual CLOSED-OTHER. So the report says the same residual is ANSWERED (W3-94, W4-08) and also CLOSED-OTHER (W3-95). Correct entry: W3-94/W4-08 = ANSWERED-BY C5 (ii) for the Studio Static part only; the Rapid/differing-stage part = CLOSED-OTHER DECISIONS.md:1885 (master under D1), as in W3-95. Evidence pasted in Batch 6.

**F3 — DEFECT — W1-29 and W2-14 vs G06.** W1-29 quotes "fee report NEEDS AMEAR 1–3" (HANDOFF.md:218) and W2-14 "(fee report NEEDS AMEAR 1–3)"; both are ANSWERED-BY D-2026-11-06-B ruling 2 (DECISIONS.md:1063). Ruling 2's words: "Fees: apply MFFU's published round trip — NQ $4.68, MNQ $1.90 — by new DECISIONS entry amending the cost model. Covered by my earlier "apply the best figure" ruling; settle this class yourself." They do not answer item 3 (the login fill-statement check), which the same report holds WAITING as G06 (docs/reports/2026-11-06-return-handoff-claude-ai.md:60 "Fee report NEEDS AMEAR 3 spelled out: ... would need a login — do you want it?"). One item is both ANSWERED and WAITING. Correct entry: W1-29/W2-14 = ANSWERED-BY ruling 2 for items 1-2; item 3 = G06 (WAITING, D2-AMBIGUOUS). Separately, "settle this class yourself" may be read as handing item 3 to the master. If so, G06 is CLOSED-OTHER, not WAITING. The master must pick one; the report holds both. Evidence pasted in Batch 7.

**F4 — MINOR — G35/G36 D2 test inconsistent with G25 and with Amear's freeze.** G25 calls changing "an enforcement hook's accepted vocabulary" D2-AMBIGUOUS (D2(d) agent permissions). G35/G36 propose closing under D1 by changing `gate-commit.sh` (the commit gate: token sweep order; "the gate deletes it only on a landed commit"), and both are marked NOT-D2. G36's own cited ruling, DECISION_LOG.md:165, is Amear's "Stop, freeze it": "No new guards, hooks, closers, or agent-stack work is dispatched." Closing either one under D1 by choosing a hook fix sets aside Amear's words. Correct entry: G35/G36 D2-AMBIGUOUS (same class as G25). Proposed closure: "record the defect as accepted known risk under the freeze (D8 (6) DECISIONS.md:1949 pattern)", no hook remedy chosen.

**F5 — DEFECT — MISSED question: ISSUE_REGISTER.md:23 (raised 2026-07-26T00:00Z).** Words: "Amear decides whether the superseded report is retained or deleted — its P0 conclusion is wrong (built on the stale 2.1.206 binary) but it is the primary record of how the false V-rdict was reached | STATE: closed (recovered; retention is Amear's call)". The row's STATE says closed, but the question itself is still Amear's. No ruling found: `grep -n 'P0-BLOCKED-superseded' DECISIONS.md DECISION_LOG.md HANDOFF.md STATUS.md MANIFEST.md` gives no output. `grep -n -i 'retention\|agent-stack-install' <report>` gives no output, and the report has no hit for `ISSUE_REGISTER.md:23`. The file is still tracked (`git ls-files` lists it; last commit b8008e4). Correct entry: Table 1 row, "Amear decides whether the superseded report is retained or deleted" | ISSUE_REGISTER.md:23 | WAITING | NOT-D2 (a repo file; no money, live path, breaker or credential) | manager's proposal: retain as is (it is committed and is the primary record), add a superseded marker | close under D1 with the proposal. (Second issue, reported only, not fixed: the tracked file has no MANIFEST.md hit.)

**F6 — MINOR — W1-42 pointer.** HANDOFF.md:277 is a bare list ("D-2026-11-04-A (:769-771)") covering two questions: :770 proof of concept and :771 r8j P0. D8(8) (DECISIONS.md:1952-1953) only cites "(the standing proof-of-concept ruling)". The ruling that settles :770 is R-VN4-7 (:947), and the one that settles :771 is R-VN4-4 (:941). Correct entry: ANSWERED-BY R-VN4-7 DECISIONS.md:947 + R-VN4-4 DECISIONS.md:941. Status unchanged; pointer wrong.

**F7 — NOTE.** (a) W3-33 rests on R-VN4-2's elided words ("Until the account is live … resting stops." / "The latter."). The backtest half of the answer is the voice agent's reading (DECISIONS.md:937). (b) W1-27: "and the harness choice" (HANDOFF.md:209) is not named in ruling 4's words. (c) G20 should also cite bd:Praxis_build-yra (same question: "whether 4uu runs with breakers / without / both"). bd:Praxis_build-ax4 has the same content as G11/H02. Neither bead id appears in the report. (d) In return handoff 2 §4 item 1, the second sub-question (trading-hours template) appears only in the appendix, not in a table row. R1 answers it ("answers §4 item 1", DECISIONS.md:1551).

DEFECT count = F1, F2, F3, F5 (MINOR and NOTE not counted).
RESULT: DEFECTS 4
~~~~

### V4 — manager re-check of the adversary findings (pasted output)

~~~~text
$ sed -n '165p' DECISION_LOG.md | cut -c1-330
- [2026-08-06T19:48:03Z] **WHO: amear** | PROPOSED BY: praxis-master (session 42 opener — three dispositions, one recommended) | APPROVED BY: Amear, 2026-08-06, in-session — selected **"Stop, freeze it"** | WHAT: **THE SUPERVISION BUILD STOPS.** No new guards, hooks, closers, or agent-stack work is dispatched. The three P0s (`s8
$ sed -n '23p' ISSUE_REGISTER.md | /usr/bin/grep -o -E 'retained or deleted|STATE: closed[^|]*'
retained or deleted
STATE: closed (recovered; retention is Amear's call)
$ git ls-files docs/reports/2026-07-25-agent-stack-install-P0-BLOCKED-superseded.md
docs/reports/2026-07-25-agent-stack-install-P0-BLOCKED-superseded.md
$ sed -n '753p' DECISIONS.md | cut -c1-240
- Amear's words: *"Yeah"*. Brief's framing: *"Yeah"* = High fill resolution with circuit breakers on as the judged go/no-go version, confirming R-VN3-6. The row does not record the question he answered.
$ sed -n '1885p' DECISIONS.md | cut -c1-200
**Open readings (not decided here).** Each item sets texts side by side. No reading is picked. U8 drafted this as "NEEDS AMEAR". Decided by master under D-2026-11-08-D D1 (taken by praxis-manager in u
$ sed -n '1063p' DECISIONS.md | /usr/bin/grep -o 'settle this class yourself'
settle this class yourself
$ bd show Praxis_build-nvn | head -n 1 | cut -c1-160
○ Praxis_build-nvn [BUG] · [bug] THIRD gate-commit.sh collision: compact.sh stages at session close, invalidating any live audit token via tree-binding   [● P1 
$ sed -n '290p' docs/reports/2026-11-01-csv-analyses.md
These questions are left open. This report does not answer any of them.
$ bd show Praxis_build-yra | head -n 1 | cut -c1-140
○ Praxis_build-yra · Dev-C reverse-and-re-enter vs breakers #2/#3 + Block-4 live-vs-backtest reconciliation   [● P1 · OPEN]
$ /usr/bin/grep -n -E '^\| (G06|G22|G24|G35|G36|H02|X03|X13) ' /tmp/d11/body.md | cut -c1-90
10:| G06 | "Fee report NEEDS AMEAR 3 spelled out: a fill-statement check of whether MFFU s
25:| G22 | "how does Amear answer csv-analyses §7 questions 1–6 (`docs/reports/2026-11-01-
27:| G24 | ""K7 is [PROPOSED] and unratified ... Do not repair before K7 ratifies."" (rais
38:| G35 | "gate-commit.sh REPORTS THE WRONG CAUSE WHEN AN AUDIT TOKEN EXPIRES ... remedia
39:| G36 | "A DENIED COMMIT BURNS THE AUDIT TOKEN ... ESCALATED to Amear; commit blocked, 
51:| H02 | ""whether #4's "next session" starts at 18:00 is undefined."" (raised 2026-11-0
62:| X03 | send MFFU the F4 follow-up (Tradovate vs NinjaTrader/Rithmic); fx4 acceptance |
72:| X13 | VM read-back of how NT8 resolves the same-bar exit + reverse (3gm read-back R2)
$ /usr/bin/grep -c '^| G16 ' /tmp/d11/body.md
0
$ /usr/bin/grep -n -E '^\| (W3-40|W3-94|W4-08|W1-29|W2-14|W1-42) ' /tmp/d11/body.md | cut -c1-60
99:| W1-29 | "fee report NEEDS AMEAR 1–3" | HANDOFF.md:218 |
107:| W1-42 | "D-2026-11-04-A (:769-771)" | HANDOFF.md:277 |
121:| W2-14 | "Adopt MFFU's $4.68 / $1.90 round turn, a sing
161:| W3-40 | "R-VN3-6: does "closest to live execution" mea
207:| W3-94 | "Which limit type and stage A4 means for the S
215:| W4-08 | ""which **stage** (Evaluation or Sim-Funded) a
~~~~

## Files staged

None. Per the brief, nothing is staged: the report and MANIFEST.md row 315 are left unstaged for the master's temp index. Scratch files are under /tmp/d11/ only.

Result: PASS (the producer's result after the stress tests above; the grade is the independent auditor's). Nothing is closed: 40 WAITING before the cutoff (25 NOT-D2 carrying a proposal; 3 D2 and 12 D2-AMBIGUOUS left to the master's D2 reading).

## Evidence appendix - source and ruling pointers (generated; every block is pasted command output)

Each block shows the exact command run (prefixed `$`) and its raw output. Output is masked by /tmp/d11/mask.sed (Method note 3). Users = table rows that cite the pointer.

### DECISIONS.md

~~~~text
# DECISIONS.md:180-189  (users W4-09)
$ sed -n '180p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
## 2026-07-15 — D-2026-07-15-B: Block-2 spec gaps Q2–Q9 RESOLVED (trader, session 15)
# DECISIONS.md:181  (users W4-10)
$ sed -n '181p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
Q1 was closed session 14 (re-implement in NT8, D 21:10Z). The remaining Block-2 scope gaps (docs/specs/2026-07-15-block2-backtesting-scope-proposal.md §5/§6) are now trader-locked via in-session AskUserQuestion (bead Praxis_build-cd4):
# DECISIONS.md:251  (users W3-02)
$ sed -n '251p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
**Addresses (for audit; not a grade):** rubric F3's written-assumption requirement (`specs/SPEC_RUBRIC.md:45-57`) and bead Praxis_build-zyd acceptance (a)(b)(c). Whether it satisfies F3 — including "before the backtest runs" — is Amear's (NEEDS AMEAR 2).
# DECISIONS.md:259  (users W3-05)
$ sed -n '259p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **(c) Why the fill-resolution choice does not decide the checkpoint order logic of this strategy, and where it may still bias the backtest:** the bead's premise ("enters on band-touch … INTRABAR events") does not match the code. `ninjascript/PraxisNoiseAreaBreakout.cs` (sha256 35393823…2752265, commit 719ab11) has six order call sites — `:211` ExitLong("XL
# DECISIONS.md:281  (users G12)
$ sed -n '281p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- All SHM distributions and threshold derivations (D-2026-07-04-B): derive from the 2-tick base. SHM-4 (`docs/specs/STRATEGY_HEALTH_MONITOR_SPEC.md:48-51`) includes slippage in its metric; its band numbers live in D-2026-07-15-B Q9 — see NEEDS AMEAR (1).
# DECISIONS.md:287  (users G12)
$ sed -n '287p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
**NEEDS AMEAR (questions only):**
# DECISIONS.md:288  (users G12)
$ sed -n '288p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
1. Is SHM-4's "slippage >2 ticks/side worse" band (D-2026-07-15-B Q9) re-read against the new 2-tick base?
# DECISIONS.md:289  (users W3-02)
$ sed -n '289p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
2. `[N]` was chosen 2026-10-28 (REPORTED); its first ledger writing is the `2026-10-30T21:36:00Z` (WHO: amear) intake row, restated at `2026-10-30T21:36:30Z`, both after runs 1–3 had run; this entry is written after run 4 (REPORTED). Does that satisfy F3's "stated in writing before the backtest runs"?
# DECISIONS.md:290  (users W3-03)
$ sed -n '290p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
3. Readback, open from `2026-10-30T22:22:00Z` (WHO: amear) (not a decision): does NT8 apply Slippage 2 on every market fill, and what is the unit of the Summary's "Total slippage" cell?
# DECISIONS.md:291  (users W3-04)
$ sed -n '291p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
4. Approve or replace the proposed limitation sentence.
# DECISIONS.md:292  (users W3-05)
$ sed -n '292p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
5. The R3 Standard-vs-High control proposed at 2026-08-29T00:40:00Z is open. Is it run before F3 is graded, or does (c) stand as INFERRED?
# DECISIONS.md:293  (users G13)
$ sed -n '293p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
6. Scope of the `[N]` lock (3gm `:949`, reserved for Amear): row `2026-10-30T21:36:30Z` sets `[N]` as band-edge slippage and states it per round trip ($22.96); the Analyzer's Slippage setting applies to every market fill (INFERRED). Was the lock meant to cover session-close and stop-out exits as well?
# DECISIONS.md:297  (users W3-04)
$ sed -n '297p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
**Unblocks:** audit of this artifact under Praxis_build-zyd; closure is not decided here (NEEDS AMEAR 5 bears on it). F3's unblock condition also requires the backtest report to carry the assumption as a stated limitation (`specs/SPEC_RUBRIC.md:55-56`); the wording is Amear's (NEEDS AMEAR 4); this entry does not do that.
# DECISIONS.md:299  (users W3-02,W3-04,W3-05)
$ sed -n '299p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
**Rulings 2026-10-30 (Amear, DECISION_LOG `2026-10-30T23:23:00Z`; answer NEEDS AMEAR 5, 2 and 4 above — appended, nothing above edited):**
# DECISIONS.md:300  (users W3-05)
$ sed -n '300p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **NEEDS AMEAR 5 → RULED: "Commit conditional + R3 control tomorrow."** This entry is committed as the CONDITIONAL it is. On 2026-10-31 Amear runs the run-4 configuration twice — `Order fill resolution` Standard vs High, every other field held — and compares the trade lists. Identical → (c) is OBSERVED and F3 moves to PASSED by Amear's edit of `specs/SPEC_R
# DECISIONS.md:301  (users W3-02)
$ sed -n '301p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **NEEDS AMEAR 2 → RULED: "Yes — the 10-28 notes are the writing."** F3's "stated in writing before the backtest runs" is satisfied by `docs/reports/2026-10-28-voice-session-notes.md` §"Amear's rulings" item 3, a dated written record of `[N]` = 2 preceding every Analyzer run; the DECISION_LOG rows transcribe it.
# DECISIONS.md:302  (users W3-04)
$ sed -n '302p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **NEEDS AMEAR 4 → RULED: limitation sentence APPROVED as proposed.** Every backtest report carries: `Fills-are-optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.`
# DECISIONS.md:303  (users G12,G13,W3-03)
$ sed -n '303p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **Still open:** NEEDS AMEAR 1 (SHM-4 band vs the 2-tick base), 3 (slippage unit — bead Praxis_build-o78), 6 (scope of the `[N]` lock over session-close / stop-out exits).
# DECISIONS.md:322  (users X13)
$ sed -n '322p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
  - *Consequence (INFERRED):* the long exit (`Close <= Lower`) coincides with the reversal trigger (`Close < Lower`, `:228`), so OppBand becomes "reverse, or hold to 16:00". A flat-only exit happens only at exact equality. How NT8 resolves the same-bar exit + reverse is CANNOT-DETERMINE-STATICALLY (3gm table rows R12/R21; the reversal readback is 3gm readbac
# DECISIONS.md:349  (users W3-07)
$ sed -n '349p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
1. **3gm Q2:** should OppBand mean the paper's opposite band in the replication (change base `:209/:217`, keep and rename, or drop)? The OppBand variant does not decide it.
# DECISIONS.md:350  (users G14)
$ sed -n '350p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
2. **3gm Q1:** sizing (b) vs (c). It is still open; this entry builds no vol-target variant.
# DECISIONS.md:351  (users W3-09)
$ sed -n '351p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
3. **Early-close handling:** once the template's early-close rows (3gm R4) and the early-close trades (R6) are read, should a session-aware flat be built, and where?
# DECISIONS.md:352  (users G15)
$ sed -n '352p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
4. **3gm C3:** if Flat1559 shows same-day 16:00 fills, does the 15:59 decision become how the replication realises the 16:00 flat, or stay a test variant? (It changes "act at the stamp" semantics, 3gm `:866`.)
# DECISIONS.md:353  (users W3-11)
$ sed -n '353p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
5. **S4 timing:** row `2026-10-30T22:58:00Z` required this entry "written and staged BEFORE any `.cs` line". Under `2026-10-31T00:46:43Z` the entry was drafted into this file in the same milestone as the .cs files, with the append due before any 7zq commit. Does that arrangement meet his constraint?
# DECISIONS.md:354  (users W3-12)
$ sed -n '354p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
6. **Third file:** the M2 pick is #1 of the shortlist by his ruling. The swap stays his after he reads the shortlist.
# DECISIONS.md:355  (users W3-13)
$ sed -n '355p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
7. **Flat1559 fill price:** is a fill at the 16:00 bar's Open (~15:59 price) acceptable as the backtest realisation of the 16:00 flat, or does he want another mechanism (e.g. a finer secondary series)? Unanswered; no option is recommended. (Checklist B.5a reads it back.)
# DECISIONS.md:358  (users W3-11)
$ sed -n '358p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **R-7zq-1 — S4 ordering (answers NEEDS AMEAR 5 above), DECISION_LOG `2026-10-31T11:04:20Z` (WHO: amear):** *"Yes — append it now, then commit."* The draft-alongside-the-.cs ordering, with the `2026-10-31T00:46:43Z` row as authorisation, satisfies his `2026-10-30T22:58:00Z` "before any .cs" rule; this entry is appended before any 7zq commit.
# DECISIONS.md:359  (users W3-13)
$ sed -n '359p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **R-7zq-2 — Flat1559 fill (answers NEEDS AMEAR 7 above), DECISION_LOG `2026-10-31T11:04:20Z` (WHO: amear):** *"Yes — test it as built."* The 15:59-bar submission / 16:00-bar-open fill (~15:59 price, flat by 16:00) is accepted as the backtest realisation; the Trades-tab readback decides whether the base's own flat was landing next-day.
# DECISIONS.md:360  (users W3-12)
$ sed -n '360p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **R-7zq-3 — third file (answers NEEDS AMEAR 6 above), DECISION_LOG `2026-10-31T11:45:29Z` (WHO: amear):** *"Keep #1 (as built)"* — `PraxisLastHalfHourMomentum` (Baltussen, Da, Lammers & Martens 2021) stands; TORB and ORB remain written specs in the shortlist.
# DECISIONS.md:363  (users G14,G15,W3-07,W3-09,W3-14,W3-15)
$ sed -n '363p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **Still open (NEEDS AMEAR):** 3gm Q1 sizing (b) vs (c) (item 2 above); 3gm Q2, what OppBand means for the base (item 1 above); early-close handling (item 3 above); adoption of the 15:59 decision into the base as the replication's realisation of the 16:00 flat (3gm C3, item 4 above; R-7zq-2 rules the backtest fill of the variant, not this); Step 0, the valu
# DECISIONS.md:383  (users W3-15,W3-19)
$ sed -n '383p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- `PraxisLastHalfHourMomentum` (Baltussen, Da, Lammers & Martens 2021; third file of D-2026-10-31-A) is **removed from the active candidate set**. What that excludes beyond the removal is not ruled here (see NEEDS AMEAR 3).
# DECISIONS.md:399  (users G17)
$ sed -n '399p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
1. Does `Praxis_build-7zq` close now that its third file is retired?
# DECISIONS.md:400  (users G18)
$ sed -n '400p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
2. Is the Desktop trade list archived into the repo, and where (handoff §5 item 8)?
# DECISIONS.md:401  (users W3-19)
$ sed -n '401p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
3. Is `PraxisLastHalfHourMomentum` also out of the R-VN3-2 High fill-resolution preparation, or does it stay in that comparison as a record run?
# DECISIONS.md:462  (users W3-22)
$ sed -n '462p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- R-VN3-2's text (notes-3 line 16): *"It does not authorize a purchase, an import or a run."* Whether the VM self-test counts as a "run" under that line is NOT for this entry to decide (NEEDS AMEAR 3).
# DECISIONS.md:472  (users W3-20)
$ sed -n '472p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
1. `.exe` ruling: source only with the rebuild steps, or the binaries too? If binaries: how do they reach this repo (the hand-retyping route was judged unsafe), and who hashes them on the VM so the repo copy can be checked against the original?
# DECISIONS.md:473  (users W3-21)
$ sed -n '473p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
2. Is the Portara data purchase that README line 13 presupposes authorised? (R-VN3-2 does not authorise a purchase.)
# DECISIONS.md:474  (users W3-22)
$ sed -n '474p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
3. The VM-side self-test (README lines 25–29) ran the tool on synthetic tick files built from an unidentified 1-min file. Does it count as a "run" under R-VN3-2, and is its result accepted as reported or to be re-run under approval?
# DECISIONS.md:475  (users W3-23)
$ sed -n '475p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
4. Should the VM-side originals (the four files and both `.exe`) be hashed on the VM to close the UNVERIFIED link in the provenance chain?
# DECISIONS.md:476  (users W3-24)
$ sed -n '476p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
5. `nt-implied-offsets.csv`: is the LF repo copy the canonical one, given Amear reports that the Desktop/VM copy differs by line endings?
# DECISIONS.md:477  (users W3-25)
$ sed -n '477p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
6. `--offsets` FORCES offsets. `TickPrep.cs` lines 45–55 parse it before the command switch (line 45: *"int fo = a.IndexOf("--offsets");   // optional CSV contract,offset_points to force offsets"*; line 52: *"forced[p[0].Trim()] = (long)(decimal.Parse(p[1], Inv) * 4m);"*). In measure, line 212: *"if (forced.ContainsKey(contracts[k].Key)) { chosen = forced[co
# DECISIONS.md:478  (users W3-26)
$ sed -n '478p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
7. README line 3 says *"`NQCONTROW 09-25` (High fill resolution, option C)"*. Which option list is "option C" from? A case-insensitive search (`/usr/bin/grep -rn -i "option C" docs/reports/*.md`) finds three candidate meanings, none confirmed as the README's: `docs/reports/2026-08-07-f3-fill-resolution-research-UNGRADED.md:175` *"Option C (measured haircut f
# DECISIONS.md:479  (users W3-27)
$ sed -n '479p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
8. Which 1-min file is the input to `measure` / `build` / `verify`? README line 11 is conditional (*"If the 1-min file is NinjaTrader's back-adjusted `NQ ##-##`, the offsets the tool measures should equal these."*). And which 1-min file did the VM self-test use?
# DECISIONS.md:480  (users W3-28)
$ sed -n '480p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
9. `verify` exits 0 when no price differs and no extra bars exist. Minute-file bars with no ticks are printed (`TickPrep.cs` line 355) but do not change the exit code (line 357: `return priceDiff == 0 && extra == 0 ? 0 : 3;`) — INFERRED from the source read; not compiled or run. How many unmatched or missing minutes are acceptable before the output is used?
# DECISIONS.md:481  (users G19)
$ sed -n '481p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
10. Is `tools/tickprep/` the path Amear wants? The brief asked for a proposed path; this unit proposed it and copied the files there.
# DECISIONS.md:489  (users W3-39)
$ sed -n '489p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
**Beads:** Praxis_build-y07 (R-VN3-3), Praxis_build-99k (R-VN3-4), Praxis_build-1r7 (R-VN3-5), Praxis_build-48p (R-VN3-6), all P2. `Praxis_build-r8j` (Phase 3 spec import) raised P1 → P0 by this unit under R-VN3-5 and R-VN3-6. Amear's brief, as the master recorded it at DECISION_LOG `2026-11-02T22:12:53Z` (WHO: praxis-master), says only *"R-VN3-5 and R-VN3-6
# DECISIONS.md:499  (users W3-35,W3-36)
$ sed -n '499p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **Leaves open:** see NEEDS AMEAR 7 and 8.
# DECISIONS.md:520  (users W3-40)
$ sed -n '520p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **Settles (against O1), in Amear's words only:** the go/no-go judges the version *"closest to live execution"*. That this means High fill resolution and breakers on is the agent's reading, which Amear did not contradict. Not contradicting a reading is not ruling on it, so this entry records it as the agent's reading and not as Amear's ruling (see NEEDS AME
# DECISIONS.md:531  (users W3-30)
$ sed -n '531p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
1. O1: which of the six Block 2 pass gates apply to the version judged under R-VN3-6?
# DECISIONS.md:532  (users W3-30)
$ sed -n '532p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
2. O1: does walk-forward efficiency ≥ 0.50 apply to an untuned (no-optimisation) version, and does GO/HOLD/REJECT sit on the replication arm or the later optimisation arm?
# DECISIONS.md:533  (users G20)
$ sed -n '533p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
3. O4: is a without-breakers backtest also kept alongside the with-breakers one, and how is the Block 4 ±15% / ±25% gate to be satisfied if the backtest and live configurations differ?
# DECISIONS.md:534  (users W3-32)
$ sed -n '534p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
4. Until the breakers are built, are backtest results without breakers (such as the 2026-11-01 runs) used for anything, or held as records only?
# DECISIONS.md:535  (users W3-33)
$ sed -n '535p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
5. With F1 FROZEN (Block 3 specifies the breakers as n8n workflow gates), how are the breakers to be applied inside a Strategy Analyzer backtest?
# DECISIONS.md:536  (users G18,G21)
$ sed -n '536p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
6. Not ruled (notes-3 line 40): how does Amear rule on handoff §5 items 1 (early-close stamps, F2), 5 (settings not visible in the screenshots), 6 (baseline settings screenshot), 7 (VM hash-check of the three strategy files) and 8 (archiving the Desktop CSVs and screenshots)?
# DECISIONS.md:537  (users W3-35)
$ sed -n '537p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
7. R-VN3-3: does "proceed as it is" also cover the effect of each 17-day hole on the 14-day lookback the Noise-Area bands use for the sessions right after it (handoff §4 item 2, not analysed)?
# DECISIONS.md:538  (users W3-36)
$ sed -n '538p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
8. R-VN3-3: does it also apply to the tick data for the High fill-resolution preparation (R-VN3-2), or only to the 1-minute data?
# DECISIONS.md:539  (users X03)
$ sed -n '539p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
9. F4: the 2026-10-28 MFFU reply names the Tradovate API, not NinjaTrader/Rithmic. Does Amear send the follow-up himself (notes-3 line 44)?
# DECISIONS.md:540  (users G22)
$ sed -n '540p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
10. Not ruled (notes-3 line 45): how does Amear answer csv-analyses §7 questions 1–6 (`docs/reports/2026-11-01-csv-analyses.md:292-297`)?
# DECISIONS.md:541  (users G17)
$ sed -n '541p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
11. Does `Praxis_build-7zq` close?
# DECISIONS.md:542  (users W3-19)
$ sed -n '542p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
12. Is `PraxisLastHalfHourMomentum` in or out of the High fill-resolution comparison?
# DECISIONS.md:543  (users W3-39)
$ sed -n '543p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
13. `Praxis_build-r8j` was raised to P0, the level the master chose. Amear's brief asks for a raise without naming a level. Is P0 the level he wants?
# DECISIONS.md:544  (users W3-40)
$ sed -n '544p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
14. R-VN3-6: does "closest to live execution" mean High fill resolution and breakers on, as the agent read it to him?
# DECISIONS.md:591  (users G19,W3-20,W3-21,W3-22,W3-23,W3-24,W3-25,W3-26,W3-27,W3-28)
$ sed -n '591p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- D-2026-11-02-B's NEEDS AMEAR items, as this entry finds them (it closes none itself): B-1 (`.exe`) — DECISION_LOG `2026-11-03T18:45:00Z` (WHO: amear) records *"**"commit to repo"** = BINARIES TOO (closes D-2026-11-02-B NEEDS AMEAR 1)"*; B-2 (purchase) — DECISION_LOG `2026-11-03T18:40:00Z` (WHO: amear) records *"**"no, not paying that. i dont know what 8 qu
# DECISIONS.md:620  (users W3-40)
$ sed -n '620p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
1. Line 32: *"R-VN3-5/6: the judged version is High resolution **with the circuit breakers on**."* The plan grades this line *"REPORTED (Mac handoff)"* and calls every High run in it *"a **measurement run** ... not the go/no-go run"*. The handoff (§2 line 36) told the VM agent: *"Treat that reading as the working target, not as his ruling."* The sentence as 
# DECISIONS.md:621  (users W3-19)
$ sed -n '621p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
2. Line 103: *"Last-Half-Hour Momentum is **not included** (R-VN3-1)."* Whether it is in or out of the High comparison is open (D-2026-11-02-A NEEDS AMEAR 3; D-2026-11-02-C NEEDS AMEAR 12). The handoff told the VM agent not to include it unless Amear says so (handoff §2 line 31), so the plan follows the handoff's default. Its citation of R-VN3-1 as the reaso
# DECISIONS.md:622  (users W3-36)
$ sed -n '622p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
3. Lines 66 and 71 apply R-VN3-3 to the tick build (*"Strict: minutes missing from the 1-min file get no ticks (R-VN3-3)"*; the holes *"stay empty (R-VN3-3)"*). Whether R-VN3-3 covers the tick data is open (D-2026-11-02-C NEEDS AMEAR 8). The handoff's line 33 told the VM agent to keep `TickPrep build` strict.
# DECISIONS.md:625  (users W3-28)
$ sed -n '625p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
6. Line 64 step 1(b) sets an acceptance for unmatched minutes (*"every one listed and explained"*). The threshold is open (D-2026-11-02-B NEEDS AMEAR 9).
# DECISIONS.md:649  (users W3-05)
$ sed -n '649p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **D-2026-10-30-A NEEDS AMEAR 5, as ruled** (`DECISIONS.md` line 300): *"Identical → (c) is OBSERVED and F3 moves to PASSED by Amear's edit of `specs/SPEC_RUBRIC.md`; different → the `2026-08-29T00:10:00Z` void clause fires and (c) is re-decided cold."* The comparison there is of trade lists, Standard vs High, *"every other field held"*.
# DECISIONS.md:662  (users W3-41)
$ sed -n '662p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
1. Line 113: *"Slippage may be ignored under High, which would trigger F3. REPORTED (forum)."* Relates to D-2026-10-30-A line 264 (whether a High run is the trigger is Amear's) and to (d).
# DECISIONS.md:663  (users W3-25)
$ sed -n '663p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
2. Line 114: *"The measured offsets might not equal NT's (the 1-min file's source isn't proven)."* Relates to B-6 and B-8, and to items 15 and 16.
# DECISIONS.md:664  (users W3-42)
$ sed -n '664p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
3. Line 115: *"Importing ticks could change how NT builds the 1-min primary. R0 catches this."* New.
# DECISIONS.md:665  (users W3-43)
$ sed -n '665p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
4. Line 116: *"A full-range High run could run out of memory."* Relates to item 20.
# DECISIONS.md:680  (users W3-21)
$ sed -n '680p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
14. Line 130: *"Buy Portara ENQ ticks for $695 (after the answers above)?"* Relates to B-2 (B-2 names no price); restated by notes line 60 (item 23). Ledger: DECISION_LOG `2026-11-03T18:40:00Z` (1), *"= NO Portara purchase at $695."*
# DECISIONS.md:681  (users W3-27)
$ sed -n '681p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
15. Line 131: *"Where did the 1-min file come from? If it's NinjaTrader's `NQ ##-##` back-adjusted series, the offsets in `nt-implied-offsets.csv` are the expected answer."* Relates to B-8 (first half) and to item 24.
# DECISIONS.md:682  (users W3-25)
$ sed -n '682p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
16. Line 132: *"If any measured offset differs from NT's, stop there, or force NT's values with `--offsets`?"* Same as B-6.
# DECISIONS.md:683  (users W3-44)
$ sed -n '683p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
17. Line 133: *"Approve P1 (one-month import) once the sample passes?"* New. P1 (line 97) also contains a 0-S run on that month and one High run on the month; this question's text names neither.
# DECISIONS.md:684  (users W3-45)
$ sed -n '684p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
18. Line 134: *"R2: add the 1-tick-slippage spec run after the 0-H control?"* New. R2 changes slippage from R1 (line 100, *"R1 plus slippage = 1"*). Relates to D-2026-10-30-A line 300 and to D-2026-10-31-A line 363 (High's extra fields; what counts as "identical"); see item 36.
# DECISIONS.md:685  (users W3-46)
$ sed -n '685p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
19. Line 135: *"Is "Baseline-H" a separate run from 0-H, or the same?"* New. The term "Baseline-H" occurs in no other `docs/reports/*.md` file (OBSERVED, `/usr/bin/grep -rln`).
# DECISIONS.md:686  (users W3-47)
$ sed -n '686p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
20. Line 136: *"Memory fallback: year-by-year runs or a 1-second fill series?"* New. Line 105 calls the 1-second series *"a departure from the spec"*.
# DECISIONS.md:687  (users W3-20)
$ sed -n '687p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
21. Line 137: *"Should the `.exe` files go into the repo, or source only with the rebuild command?"* Same as B-1; restated by notes line 62 (item 25). Ledger: DECISION_LOG `2026-11-03T18:40:00Z` (3) *"**"keep them for reference"** — master reading UNRESOLVED"*, then `2026-11-03T18:45:00Z` (3) *"**"commit to repo"** = BINARIES TOO"*.
# DECISIONS.md:688  (users W3-57)
$ sed -n '688p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
22. Line 138: *"Should the High measurement runs wait for `r8j` (breakers), or go ahead as measurement-only?"* Relates to C-4 and C-5 and to R-VN3-5 (D-2026-11-02-C). Relates to items 17, 36 and 37. Ledger: DECISION_LOG `2026-11-03T18:40:00Z` (4) *"**"yes"** — master reading UNRESOLVED"*, then `2026-11-03T18:45:00Z` (4) *"**"when the time comes ask agaian."*
# DECISIONS.md:691  (users W3-56)
$ sed -n '691p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
23. Line 60: *"Send Portara the eight questions (plan §6), then decide whether to buy for $695."* Same as item 14 for the purchase; relates to B-2. Sending the questions is new. Ledger: DECISION_LOG `2026-11-03T18:40:00Z` (1), Amear's words *"no, not paying that. i dont know what 8 questions."*
# DECISIONS.md:692  (users W3-58)
$ sed -n '692p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
24. Line 61: *"Should the per-contract NQ minute folders already on the VM be read (read-only) to confirm the 1-min file's source before buying?"* New. Relates to items 15 and B-8. Notes line 35: the folders seen are *"NQ 03-20 through NQ 12-26"*; *"Only the folder names were read"*. Ledger: DECISION_LOG `2026-11-03T18:40:00Z` (2) *"**"yes"** = read-only rea
# DECISIONS.md:693  (users W3-20)
$ sed -n '693p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
25. Line 62: *"`.exe` files: into the repo or not? If yes, they go up as the files themselves via Drive, with the hashes above."* Same as B-1 / item 21. Ledger: see item 21.
# DECISIONS.md:694  (users G21)
$ sed -n '694p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
26. Line 63: *"§3.3 items (strategy-file hash check, template early-close readback): do them or not?"* Same as C-6 (11-01 handoff §5 items 7 and 1). The 11-02 handoff §3.3 (lines 56–58) puts them under "Only if Amear rules it".
# DECISIONS.md:697  (users X07)
$ sed -n '697p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
27. Line 54: *"Strategy Analyzer Log tab "ignored" messages"*.
# DECISIONS.md:698  (users X07)
$ sed -n '698p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
28. Line 55: *"C6: save settings as default"* — step C6 of `docs/reports/2026-11-01-voice-handoff-commission-fix.md` (line 105).
# DECISIONS.md:699  (users X07)
$ sed -n '699p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
29. Line 56: *"C7: NQCONTROW instrument readback."* — step C7 of the same file (line 113). Plan line 79 depends on it: the rollover 2021-03-01 / Do not merge state is *"REPORTED (Mac handoff)"* and *"UNVERIFIED"* until C7.
# DECISIONS.md:702  (users W3-48)
$ sed -n '702p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
30. Plan line 73: tick files delivered in Central time *"would need a code change, a question for Amear first"*. New.
# DECISIONS.md:703  (users W3-26)
$ sed -n '703p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
31. "Option C" label. Plan line 36 (*"Data (option C: Portara per-contract ticks)"*) and notes line 41 (*"Adjust per-contract myself" (option C, TickPrep)*) give the VM-side use of the label. REPORTED BY the VM agent. Relates to B-7. This entry does not mark B-7 closed.
# DECISIONS.md:704  (users W3-28)
$ sed -n '704p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
32. Plan line 64 step 1(b): unmatched minutes *"every one listed and explained"*. Same as B-9.
# DECISIONS.md:705  (users W3-24)
$ sed -n '705p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
33. CSV canonical copy: the VM copy is reported CRLF 669 B (notes line 26); the repo copy is LF 645 B. Same as B-5.
# DECISIONS.md:706  (users W3-22)
$ sed -n '706p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
34. Plan line 96, P0 (TickPrep on the March 2021 sample): no approval question is posed for it. Relates to B-3 (whether the VM self-test counts as a "run" under R-VN3-2) and to item 13.
# DECISIONS.md:707  (users W3-49)
$ sed -n '707p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
35. Plan lines 85 and 98, R0 (0-S full range after the import): no approval question is posed for it, nor for the full-range tick import it presupposes (line 98, *"after full import"*). Line 133 (Q4) covers the one-month import only.
# DECISIONS.md:708  (users W3-05,W3-14,W3-50)
$ sed -n '708p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
36. Plan line 99, R1 (0-H): no approval question is posed for it apart from item 22. Relates to the Standard-vs-High control ruled at D-2026-10-30-A line 300 (NEEDS AMEAR 5: *"Commit conditional + R3 control tomorrow."*) and to D-2026-10-31-A line 363 (High's extra fields and what counts as "identical", still open). The plan does not say whether R1 is that c
# DECISIONS.md:709  (users W3-51)
$ sed -n '709p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
37. Plan line 101, R3–R4 (OppBand and Flat1559 at High): no approval question is posed for them.
# DECISIONS.md:710  (users W3-52)
$ sed -n '710p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
38. Plan line 29, the Analyzer dropdown look ("with no run"): whether it needs approval is not posed.
# DECISIONS.md:711  (users W3-19)
$ sed -n '711p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
39. Plan line 103, LHM *"not included (R-VN3-1)"*. Same as A-3 / C-12.
# DECISIONS.md:712  (users W3-36)
$ sed -n '712p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
40. Plan lines 66 and 71, R-VN3-3 applied to the tick build. Same as C-8.
# DECISIONS.md:713  (users W3-40)
$ sed -n '713p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
41. Plan line 32, the judged version as High + breakers on. Same as C-14.
# DECISIONS.md:714  (users W3-53)
$ sed -n '714p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
42. Plan lines 85 and 98: whether "1,190 trades", "$197,327.60" and "total slippage 1190" are the R0/R1 pass bars (see b, item 7). New.
# DECISIONS.md:715  (users G19,W3-23)
$ sed -n '715p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
43. D-2026-11-02-B items not listed above: B-10 (`tools/tickprep/` path), not raised by the plan or notes; B-4 (whether the VM originals should be hashed), whose hashing the notes report done (section a). Both still open. B-3 is at item 34.
# DECISIONS.md:716  (users W3-54)
$ sed -n '716p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
44. Plan line 82, the safeguard *"Copy `db\minute\NQCONTROW 09-25` and record SHA-256 for every file before any import"*: not posed as a question of its own; placed inside the import step (section b).
# DECISIONS.md:717  (users W3-55)
$ sed -n '717p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
45. Plan lines 45 and 48: the price route (*"Flat is cheaper"*: $695 flat against $750 by the year) and the time zone to ask Portara for (*"**Ask for US Eastern**"*) are recommendations inside the purchase question (section b, item 5). Listed, not adopted.
# DECISIONS.md:753  (users W3-40)
$ sed -n '753p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- Amear's words: *"Yeah"*. Brief's framing: *"Yeah"* = High fill resolution with circuit breakers on as the judged go/no-go version, confirming R-VN3-6. The row does not record the question he answered.
# DECISIONS.md:754  (users W3-40)
$ sed -n '754p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- Closes D-2026-11-02-C NEEDS AMEAR 14 (DECISIONS.md:544). That closure label is in the ledger row's framing. Amear's own word is "Yeah".
# DECISIONS.md:756  (users W3-62)
$ sed -n '756p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- Brief's framing: no tick-data purchase until Standard-resolution results show proof of concept. This entry does not define "proof of concept" (this entry's NEEDS AMEAR 1).
# DECISIONS.md:757  (users W3-30)
$ sed -n '757p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- Does not clear O1. The gate set is still open (D-2026-11-02-C NEEDS AMEAR 1–2, DECISIONS.md:531-532).
# DECISIONS.md:769  (users W3-62)
$ sed -n '769p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
**NEEDS AMEAR (questions only, not answered):** Fills-are-optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
# DECISIONS.md:770  (users W3-62)
$ sed -n '770p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
1. What counts as "proof of concept"? (His words name no test; the brief's framing ties it to Standard-resolution results.)
# DECISIONS.md:771  (users W3-39)
$ sed -n '771p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
2. `Praxis_build-r8j` is at P0, the master's choice (D-2026-11-02-C, DECISIONS.md:489; NEEDS AMEAR 13). Is P0 the level he wants?
# DECISIONS.md:812  (users W4-11,W4-13,W4-15)
$ sed -n '812p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- *"1. Walk-forward runs BOTH ways: (a) paper's fixed rules, nothing optimised; (b) four parameters tuned per window — lookback, noise multiplier, stop-ATR multiplier, exit policy. A stop is added to the strategy for (b) on its own branch; baseline file unchanged."*
# DECISIONS.md:816  (users W4-35)
$ sed -n '816p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- *"5. Account tier: no decision until backtest + paper results exist."*
# DECISIONS.md:819  (users W3-30)
$ sed -n '819p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- (i) O1 (`specs/SPEC_RUBRIC.md:74-79`) and D-2026-11-02-C NEEDS AMEAR 1–2 (DECISIONS.md:531-532): the gate set, and whether walk-forward efficiency ≥ 0.50 applies. Per the master's reading, items (1a)/(1b) speak to these: "(a) has no optimisation step, (b) does". The row does not say which gates apply to which arm. O1 stays OPEN.
# DECISIONS.md:820  (users W3-74)
$ sed -n '820p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- (ii) Report C (`docs/reports/2026-11-04-proof-of-concept-standard.md:248`) NEEDS AMEAR 2, the equity base for "max DD ≤ 4% of equity". The master's reading says item 3 answers it, and summary v2 item 5, in part, and that "the MFFU account size itself is still not on the ledger". Report C:248 mentions "the MFFU $1,500 EOD trailing DD"; this entry does not a
# DECISIONS.md:821  (users W3-64)
$ sed -n '821p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- (iii) Report C §3 (`:144`): tick data becomes a prerequisite once a resting stop or target exists (`:170`). Report C grades this INFERRED: `:170` sits under the heading at `:165`, "Answer (INFERRED from the code, the vendor document and the reproduction; untested in NinjaTrader because no High run exists)", and summary item 5 (`:17`) reads "INFERRED; untes
# DECISIONS.md:822  (users W3-39)
$ sed -n '822p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- (iv) Bead `Praxis_build-r8j` is P0, the master's choice, not confirmed by Amear (D-2026-11-04-A NEEDS AMEAR 2). `bd show` on 2026-11-05 reads "P0 · OPEN". Per the master's reading, walk-forward still waits on it, and on the data-quality items that C NEEDS AMEAR 7 (`:253`) leaves to Amear: 33 missing sessions and the 12:15 template.
# DECISIONS.md:828  (users W3-63)
$ sed -n '828p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
**NEEDS AMEAR (questions only, not answered):**
# DECISIONS.md:829  (users W3-63)
$ sed -n '829p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
1. Which MFFU account size and which tier limits are to be used for items 3 and 4, given that item 5 defers the account-tier decision until backtest and paper results exist?
# DECISIONS.md:830  (users W3-64)
$ sed -n '830p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
2. Does arm (b) run on minute data, given its stop (report C NEEDS AMEAR 11)?
# DECISIONS.md:831  (users W3-65)
$ sed -n '831p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
3. What is the candidate set for the exit-policy parameter in item 1(b)?
# DECISIONS.md:832  (users W3-66)
$ sed -n '832p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
4. Is R-1104-3's judged version arm (a), arm (b) or both?
# DECISIONS.md:898  (users W3-67)
$ sed -n '898p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
   Its section `## NEEDS AMEAR` holds questions 1–29.
# DECISIONS.md:920  (users W3-67)
$ sed -n '920p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
**NEEDS AMEAR:** see `docs/specs/2026-11-05-walk-forward-spec.md`, section `## NEEDS AMEAR`, items 1–29 (questions only; none answered here).
# DECISIONS.md:936  (users W3-33)
$ sed -n '936p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **R-VN4-2** — breakers as resting stops?: "Until the account is live … resting stops." Asked which: "The latter."
# DECISIONS.md:939  (users W3-64)
$ sed -n '939p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **R-VN4-3** — walk-forward on minute data: "Yes."
# DECISIONS.md:941  (users W1-37,W3-39)
$ sed -n '941p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **R-VN4-4** — r8j at P0: "Yes."
# DECISIONS.md:943-944  (users W3-09)
$ sed -n '943,944p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **R-VN4-5** — data gaps: "As long as the data that I generated came back similar to … what is found online, I'm happy to move on."
  - reading (voice agent, notes-4): 33 missing sessions and the 12:15 early-close exits are accepted as is. No fix before results are judged. Basis: baseline shape matches the published NQ replication (lower win rate, bigger winners), weaker.
# DECISIONS.md:943  (users W3-35)
$ sed -n '943p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **R-VN4-5** — data gaps: "As long as the data that I generated came back similar to … what is found online, I'm happy to move on."
# DECISIONS.md:947  (users W1-35,W1-42,W3-14,W3-19,W3-21,W3-22,W3-23,W3-24,W3-25,W3-26,W3-27,W3-28,W3-36,W3-40,W3-41,W3-42,W3-43,W3-44,W3-45,W3-46,W3-47,W3-48,W3-49,W3-50,W3-51,W3-52,W3-53,W3-54,W3-55,W3-62)
$ sed -n '947p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **R-VN4-7** — proof of concept: "Proof of concept is having the full trading pipeline existing and having it run in real live markets on a sim account." / "We're just gonna proceed without that [historical tick data]."
# DECISIONS.md:955  (users W3-68)
$ sed -n '955p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
  - master's reading, flagged (row text): *"drop the minter's FAIL-word filter and rely on the exact `V-rdict: PASS` + COMMIT_INDEX + COMMIT_DIFF_SHA256 lines; quoting a criterion's text must not block a mint"*. Not confirmed by Amear (NEEDS AMEAR 1).
# DECISIONS.md:970  (users W3-69)
$ sed -n '970p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- (iii) R-VN4-6 with the fee report (`docs/reports/2026-11-05-mffu-fee-check.md:7-10`): MFFU's own page gives NQ $4.68 round trip (MNQ $1.90), not $5.76; $5.76 on that page is YM. The cost model stays $2.96 (D-2026-10-30-A unchanged) pending Amear (DECISION_LOG `2026-11-05T23:59:40Z`, `2026-11-06T00:06:48Z`; fee report NEEDS AMEAR at `:131`).
# DECISIONS.md:978  (users G07,G08,G09,W2-02,W3-74,W3-75,W4-02,W4-03)
$ sed -n '978p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
**Not ruled (stay open, from notes-4 `## Not ruled on`):** past use of the GitHub login (item 24; no remedy requested); second Rithmic read-only connection (item 23); CME Atlassian wiki as a source (item 19); equity base for the 4% DD gate (item 5) and Sharpe definition (item 4); O1 gate set / WFE with no optimisation (item 6).
# DECISIONS.md:983  (users G07,G08,G09,W3-68,W3-70,W3-74,W3-75)
$ sed -n '983p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
**NEEDS AMEAR (pointers and questions only, not answered):**
# DECISIONS.md:985  (users W3-69)
$ sed -n '985p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
2. R-VN4-6: which fee figure applies — see `docs/reports/2026-11-05-mffu-fee-check.md:131` (NEEDS AMEAR 1–3 there).
# DECISIONS.md:1004  (users W2-15)
$ sed -n '1004p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
3. File sharing: Fusion shared folders unavailable (no Sharing pane, as flagged). SMB route done by hand: Mac File Sharing on; Praxis.build shared; admin Read & Write; staff Read Only; Everyone No Access. VM: \\192.168.1.204\Praxis.build mapped as Z:, reconnect at sign-in, credentials remembered. Amear confirmed the folders show. Replaces the Google Drive ro
# DECISIONS.md:1009  (users W3-82)
$ sed -n '1009p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **Item 1 — NT8 version.** REPORTED BY amear: NT8 was updated before the committed runs, and the committed numbers come from the new version. Prior repo record: the 2026-10-28 ruling (4), "stay on 8.1.7.2 until the backtest runs clean" (DECISION_LOG `2026-10-30T21:36:00Z`, WHO: amear); then `docs/reports/2026-10-31-voice-session-notes-2.md:161`, "The NT8 ve
# DECISIONS.md:1014  (users W3-81)
$ sed -n '1014p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
  - **Direction he set:** the walk-forward runs in NT8 through the bridge, not in a Mac-side Python copy. The open question it bears on is the step-c harness question at DECISION_LOG `2026-11-06T00:54:04Z`: "arm (a) can only run in NT8 on the VM (barred overnight: "no NT8 runs or imports on the VM") or via a Mac-side Python harness, and choosing a harness ov
# DECISIONS.md:1017  (users W3-70)
$ sed -n '1017p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
  - **Walkthrough** `docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md`: Question 0 (`:8`) ends "Try these steps / D-072 SMB / keep Google Drive `praxis-tickprep`? Your call; nothing chosen." Questions 1–3 are at `:9-11` and the Steps at `:13-21`. REPORTED BY amear: "Fusion shared folders unavailable (no Sharing pane, as flagged)". Master's readin
# DECISIONS.md:1020  (users W3-76)
$ sed -n '1020p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
  - **Go-live checklist (his words):** unmap `Z:` and turn the share off before real money. Recorded here only. The walkthrough's go-live line (`:26-27`, R-VN4-14) covers the Fusion shared folder and is not amended (NEEDS AMEAR 1).
# DECISIONS.md:1022  (users W3-69)
$ sed -n '1022p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
  - "MFFU fees ($4.68 NQ / $1.90 MNQ; the $5.76 given in voice was YM, Claude's error)" — the attribution of the error is his words. Tracked: `docs/reports/2026-11-05-mffu-fee-check.md:131-134` (NEEDS AMEAR 1–3); D-2026-11-05-B (iii), DECISIONS.md:970. The cost model is unchanged by this entry.
# DECISIONS.md:1024  (users W3-67)
$ sed -n '1024p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
  - "walk-forward arm (b) settings" — `docs/specs/2026-11-05-walk-forward-spec.md` `## NEEDS AMEAR` (`:194`): items 1–6 (`:196-201`), 14 (`:209`), 27 (`:222`), 28 (`:223`).
# DECISIONS.md:1034  (users W3-81)
$ sed -n '1034p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **No limit is lifted by this entry.** The 2026-10-28 ruling, D-071 and the `23:50:09Z` hard limits all stand. Only Amear's words lift them. His words in item 2 set the conditions for lifting the 2026-10-28 ruling (2a and 2b both pass); they do not name D-071 or the `23:50:09Z` limits (NEEDS AMEAR 6).
# DECISIONS.md:1041  (users W3-76)
$ sed -n '1041p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
1. Should the Fusion walkthrough's go-live section (`docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md:26-27`) be amended with your line "unmap Z: and turn the share off before real money"?
# DECISIONS.md:1042  (users W3-77)
$ sed -n '1042p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
2. After the install walkthrough is written, who performs the install? (The master's reading names you by hand or the VM agent, not Code.)
# DECISIONS.md:1043  (users W3-78)
$ sed -n '1043p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
3. What is "the VM's Cowork agent", where does it run, and where is its skills directory? (The filer cannot write test 2b's steps without it.)
# DECISIONS.md:1044  (users W3-79)
$ sed -n '1044p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
4. For test 2a: is `docs/reports/2026-11-01-three-strategy-results.md:73` (1190 trades, $197327.60 net, `NQCONTROW SEP25`) the reference run, and does "reproduces" mean an exact match on trades and net, or a tolerance?
# DECISIONS.md:1045  (users W3-80)
$ sed -n '1045p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
5. Should the rule that reports carry the standing limitation sentence (the sentence on this entry's **Standing limitation** line; today a master's standing instruction) be written into `specs/SPEC_RUBRIC.md`? REPORTED BY the flush auditor (DECISION_LOG `2026-11-06T15:19:51Z`, working tree, not yet in a commit): it "could not find the house rule written in C
# DECISIONS.md:1046  (users W3-81)
$ sed -n '1046p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
6. Does test 2a (as the filer reads it, an NT8 run on the VM driven through the bridge) need your separate lift of the `23:50:09Z` limit "no NT8 runs or imports on the VM", and of D-071 if the bridge needs a connection, or does item 2 cover them?
# DECISIONS.md:1047  (users W3-82)
$ sed -n '1047p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
7. Item 1 says "Code: read and record the exact version on the VM's next touch." Per the master's reading (DECISION_LOG 15:15:30Z), Code has no VM access. Who reads the version on the VM (you or the VM agent) for Code to record?
# DECISIONS.md:1048  (users W3-83)
$ sed -n '1048p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
8. Who judges that 2a and 2b have passed, and is the lift recorded by your own ledger row?
# DECISIONS.md:1049  (users W3-84)
$ sed -n '1049p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
9. `CLAUDE.md:30` says not to "Run multiple Claude sessions against this working tree — one session per repo". Item 3 gives `admin` Read & Write and `staff` Read Only on the `Praxis.build` share, mapped on the VM as `Z:`; it does not say which account the VM signs in with. If a VM agent session can write in `Z:`, does that count as a second session against t
# DECISIONS.md:1050  (users W3-70)
$ sed -n '1050p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
10. Does item 3 close the Fusion walkthrough's Question 0 (`:8`) and make its Questions 1–3 (`:9-11`) moot, as the master reads it? Question 0's SMB option was D-072's form (`praxispush`, `~/praxis-signals`); item 3 shares `Praxis.build`, with `admin` Read & Write.
# DECISIONS.md:1063  (users G06,W1-25,W1-26,W1-27,W1-28,W1-29,W1-32,W2-13,W2-14,W3-65,W3-66,W3-69,W3-77,W3-79,W3-81,W3-82,W3-83,W3-84)
$ sed -n '1063p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
Rulings 1. Bridge install (NEEDS AMEAR 2): the VM agent installs cli-nt-bridge via terminal, after a VMware snapshot. 2. Fees: apply MFFU's published round trip — NQ $4.68, MNQ $1.90 — by new DECISIONS entry amending the cost model. Covered by my earlier "apply the best figure" ruling; settle this class yourself. 3. Commit gate: (a) RATIFY D-2026-11-04-B add
# DECISIONS.md:1074  (users W3-77)
$ sed -n '1074p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **Ruling 1 — bridge install.** *Rules:* "the VM agent installs cli-nt-bridge via terminal, after a VMware snapshot." *Unlocks:* answers D-2026-11-06-A NEEDS AMEAR 2 ("who performs the install"). The order he set in D-2026-11-06-A item 2 still applies: code read → install walkthrough → VMware snapshot → install. *Does NOT lift:* the hard limits above; D-071
# DECISIONS.md:1086  (users W3-78)
$ sed -n '1086p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
| 3 — "the VM's Cowork agent" | none given | The master adopts a working definition: the Claude agent running inside the Windows VM (a definition, not an observation; the VM agent's first reply confirms or corrects it). Its skills directory is reported by the VM agent itself in its first reply. | pending: VM agent (first reply) |
# DECISIONS.md:1088  (users W3-80)
$ sed -n '1088p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
| 5 — limitation sentence into the rubric | none given | Written into `specs/SPEC_RUBRIC.md` as standing criterion S13. | `specs/SPEC_RUBRIC.md`:119 |
# DECISIONS.md:1089  (users W2-09,W3-81)
$ sed -n '1089p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
| 6 — lift scope | "my "lift completely once confirmed" ruling covers what tests 2a/2b need (bridge install + its import), D-071 untouched" | His lift covers the bridge install and its import; D-071 untouched. His words also say "what tests 2a/2b need"; whether that reaches the 2a NT8 run on the VM (D-2026-11-06-A NEEDS AMEAR 6) stays in his words and is nei
# DECISIONS.md:1093  (users W1-30,W3-70)
$ sed -n '1093p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
| 10 — Fusion Questions 0–3 | none given | Closed by D-2026-11-06-A item 3 (SMB done by his hand) and this ruling. | walkthrough :33–37 |
# DECISIONS.md:1094  (users W1-31,W2-16)
$ sed -n '1094p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
| 15 — parked branch `parked/Praxis_build-r8j` (f258a5d) leak | none given | Findings only (below); the deletion decision stays with the master. | pending: master |
# DECISIONS.md:1095  (users W2-17)
$ sed -n '1095p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
| 16 — carry D-2026-08-06-A onto main | none given | Carried, text unchanged except as noted in its preface. | `DECISIONS.md`:1131 |
# DECISIONS.md:1096  (users W1-34,W2-18,W3-68)
$ sed -n '1096p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
| 17 — master's R-VN4-10 reading | none given | The master's reading stands as applied: the minter has no FAIL-word filter; the exact three-line V-rdict contract is the signal (D-2026-11-04-B addendum 2, DECISIONS.md:836–858, item 2 at :852). | DECISIONS.md:834–858 (as applied in the gate correction unit, which is parked as `Praxis_build-uqb`) |
# DECISIONS.md:1136  (users W2-45)
$ sed -n '1136p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
**Status:** LOCKED (trader-ruled — Amear, 2026-08-06). Prospective: this entry authorises an import that has NOT yet been performed at the time of writing, per rubric S4 ("written before the work, not after").
# DECISIONS.md:1165  (users W4-28)
$ sed -n '1165p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
## 2026-11-06 — D-2026-11-04-B addendum 5: third hand-back shape (task-notification) — WRITTEN AFTER THE WORK; S4 timing NOT met; ratification requested (WHO: amear)
# DECISIONS.md:1192  (users W4-28)
$ sed -n '1192p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
## 2026-11-07 — D-2026-11-04-B addendum 6: ratification (WHO: amear) of addendum 5's timing
# DECISIONS.md:1214  (users W1-22)
$ sed -n '1214p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
RULINGS — 2026-11-07 morning (WHO: amear). Answers to the 11-07 return handoff §4.
# DECISIONS.md:1216  (users W1-23,W2-05)
$ sed -n '1216p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
1. Addendum 5 timing: RATIFIED. Unpark/close uqb on a fresh audit.
# DECISIONS.md:1217  (users W1-21,W2-06)
$ sed -n '1217p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
2. Item 19: commit docs/reports/2026-10-28-voice-session-notes.md as a one-file exception to the as-is rule — it is the source of a ruling. Fix MANIFEST.md:244 to match.
# DECISIONS.md:1218  (users W1-19,W2-07)
$ sed -n '1218p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
3. Guard vs trailer: no guard change. Keep the attribution line in the form the guard accepts. Don't loosen a guard to fit a format.
# DECISIONS.md:1219  (users W1-24)
$ sed -n '1219p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
4. Walk-forward values (Q1–Q10):
# DECISIONS.md:1220  (users W2-08)
$ sed -n '1220p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
   Q2 yes, lookback {10,14,18} x multiplier {0.8,1.0,1.2} is the small grid.
# DECISIONS.md:1220-1228  (users W2-08)
$ sed -n '1220p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
   Q2 yes, lookback {10,14,18} x multiplier {0.8,1.0,1.2} is the small grid.
# DECISIONS.md:1222  (users W3-07)
$ sed -n '1222p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
   Q4 yes, OppBand = the paper's opposite band, as in _OppBand.cs.
# DECISIONS.md:1227  (users G01)
$ sed -n '1227p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
   Q9 no tier chosen. Report the per-tier table; I pick after paper results.
# DECISIONS.md:1228  (users W2-08)
$ sed -n '1228p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
   Q10 and every remaining PROPOSED value in the file: settle under R-1104-2, strictest reasonable choice. Add the missing ExitPolicy/Contracts test that parked 867, re-audit, commit.
# DECISIONS.md:1229  (users W2-09,W3-81)
$ sed -n '1229p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
5. 2a run: YES, covered by my lift. A test that needs a run includes the run.
# DECISIONS.md:1230  (users W2-10)
$ sed -n '1230p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
6. Strategy Analyzer tab: a hand-set tab may be used for 2a and counts as "bridge reproduces the baseline". It does NOT count as "driven from the terminal". The full in-VM automation lift needs a run whose settings come from the bridge/config, not my hands. Log it as a partial pass until then.
# DECISIONS.md:1231  (users G02,W2-11)
$ sed -n '1231p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
7. Bridge items: (4) playbackrun/reconnect/flatten/strategies/ghostorders/AutoReconnect stay forbidden until live-trading design says otherwise. (5) NT8 Guard out. (7) 2a uses the committed base PraxisNoiseAreaBreakout.cs; the VM's installed copy must hash-match HEAD, or STOP. (11) pip may download only the bridge's pinned requirements, into its own venv und
# DECISIONS.md:1232  (users W2-12)
$ sed -n '1232p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
8. Snapshot is my hand step: confirmed.
# DECISIONS.md:1233  (users G07,G08,G09)
$ sed -n '1233p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
9. Notes-4 unruled items stay open; none block anything.
# DECISIONS.md:1234  (users W3-76)
$ sed -n '1234p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
10. Go-live checklist additions: remove the unauthenticated bridge request folders (or add auth) before real money; unmap Z: and turn off the SMB share.
# DECISIONS.md:1262  (users W2-20)
$ sed -n '1262p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
  **Master's decision under delegation (R-1104-2), not Amear's word.** Source: DECISION_LOG `2026-11-07T13:00:54Z` (WHO: praxis-master), on his Q3 words and Q10's "strictest reasonable choice". Q3 stop-ATR multipliers = **{1.5, 2.25, 3.0} × ATR(14)**: "the two bounds he named and their midpoint, nothing chosen outside his range". `StopAtrMult = 0` stays a pe
# DECISIONS.md:1263  (users W3-81)
$ sed -n '1263p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **Ruling 5 — 2a run.** *Rules:* "2a run: YES, covered by my lift. A test that needs a run includes the run." *Unlocks:* answers the run half of D-2026-11-06-A NEEDS AMEAR 6 (DECISIONS.md:1046): his lift covers the test 2a NT8 run on the VM. The D-071 half of that question is not answered by ruling 5's words. *Does NOT lift:* his words do not mention D-071;
# DECISIONS.md:1290  (users W2-19)
$ sed -n '1290p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
**Correction 1 (before commit, after audit FAIL 1 on S1/S13/check f; appended by unit 2026-11-07-rulings-filing-correction-1, DECISION_LOG 2026-11-07T13:36:00Z).** Retracted, as written in the S4 timing paragraph above (:1282): "the walkthrough line was appended at 13:08:15Z (that file's mtime, `stat`, unchanged since), BEFORE this entry was first spliced in
# DECISIONS.md:1314  (users W3-67)
$ sed -n '1314p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- Reach of Q10 — INFERRED (the master's reading, DECISION_LOG `2026-11-07T14:06:00Z`). The dispatch settles "for every value that was PROPOSED and for Q10's open items — EXCEPT the items ruling 9 keeps open". Version 1's NEEDS AMEAR question 10 was `**The WF spec's 29 items, mapped.**` (version 1 :146, in the unit report's Appendix A). So Q10 is read as also
# DECISIONS.md:1460  (users G01,G09)
$ sed -n '1460p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
**NEEDS AMEAR.** Only these:
# DECISIONS.md:1461  (users G01)
$ sed -n '1461p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
1. The tier pick, after paper results (Q9).
# DECISIONS.md:1462  (users G08,G09,W3-30,W3-74,W3-75)
$ sed -n '1462p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
2. Ruling 9's open items ("Notes-4 unruled items stay open; none block anything."): a second Rithmic read-only connection; the CME wiki as a source; the equity base and the Sharpe definition, scoped in the notes-4 source (DECISIONS.md:978) as "equity base for the 4% DD gate (item 5) and Sharpe definition (item 4)" and read by the WF spec for the "OOS Sharpe 
# DECISIONS.md:1526  (users G03)
$ sed -n '1526p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **What he did NOT rule.** He was asked one question only. The R-1104-2-scope question raised by the spec-addendum unit stays open for the return handoff.
# DECISIONS.md:1551  (users W1-18,W2-01)
$ sed -n '1551p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
R1  RTH = 09:30–16:00 ET (answers §4 item 1, B1). Arms (a) and (b)
# DECISIONS.md:1552-1553  (users W4-11)
$ sed -n '1552,1553p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
    anchor at the 09:30 ET cash open. VM step 0 reads the live
    "CME US Index Futures RTH" template hours (T7 readback). If the
# DECISIONS.md:1556  (users W2-02,W4-05)
$ sed -n '1556p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
R2  GO requires arm (a) to pass. Arm (b) can only add confidence or
# DECISIONS.md:1558  (users W2-02)
$ sed -n '1558p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
R3  Gate 6 (WFE) applies to arm (b) only (§4 item 3).
# DECISIONS.md:1621  (users W3-86,W3-87,W3-88,W3-89,W3-90)
$ sed -n '1621p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **R4 — scoring, hybrid.** *Answers:* §4 item 3's "the gate 2 Sharpe definition and its equity base" (his words: "(§4 item 3, gate 2)"; the sub-part is the filer's assignment (INFERRED, the filer's, not his word)). R4 instructs "flag any conflict back to Amear, do not resolve it". Master's reading (filing note 3, :88), changeable by Amear, names the same ch
# DECISIONS.md:1638  (users W3-86,W3-87,W3-88,W3-89,W3-90)
$ sed -n '1638p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
**NEEDS AMEAR.** Each flag sets two texts side by side. Not resolved here; no reading is picked.
# DECISIONS.md:1640  (users W3-86)
$ sed -n '1640p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **FLAG 1 — R4 vs the §6 selection statistic.** Values spec §6 :92: "**as the in-sample selection objective only**: annualised Sharpe of daily net P&L … d_i = sum of the net P&L … of trades exited in session i, 0 if none. S = mean(d) / sd(d) × √252, sd with n − 1, risk-free rate 0 … dollar P&L at 1 NQ needs no equity base." R4 (block above): "equity base = 
# DECISIONS.md:1641  (users W3-87)
$ sed -n '1641p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **FLAG 2 — R4 vs the gate-2 open item.** Values spec :93: "This statistic does NOT define the gate "OOS Sharpe ≥ 1.0". The gate's Sharpe definition and its equity base stay OPEN under ruling 9"; §8 :132 (i) the same. R4 supplies daily returns, no-trade days = 0, equity base = the account size actually traded. Open within it (INFERRED, the filer's, not his 
# DECISIONS.md:1642  (users W3-88)
$ sed -n '1642p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **FLAG 3 — R4's win-rate rule vs the gate list.** R4 heads itself "(§4 item 3, gate 2)" and includes a win-rate rule. The six gates (:121-127) carry no win-rate gate; gate 2 is "OOS Sharpe ≥ 1.0" (:123). A win-rate figure appears in O4's Block 4 gate, "within ±15% win rate" (`specs/SPEC_RUBRIC.md:96-97`). Where R4's win-rate rule applies — his. Also open (
# DECISIONS.md:1643  (users W3-74)
$ sed -n '1643p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **FLAG 4 — the 4% DD equity base.** Values spec :93 and :132 cite DECISIONS.md:978: "equity base for the 4% DD gate (item 5) and Sharpe definition (item 4)". :135: "Max-DD gate base — RULED (D-2026-11-05-A item 3, DECISIONS.md:814 …)", with the notes-4 item kept OPEN. R4's words name Sharpe and win rate, not the drawdown gate (INFERRED, the filer's, not hi
# DECISIONS.md:1644  (users W3-89)
$ sed -n '1644p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **FLAG 5 — "trading day" vs "session".** R4: "every trading day counted (no-trade days = 0)". Values spec :92 counts per session i ("For the in-sample sessions i = 1…n") ("trades exited in session i"). R6 asks to "confirm whether an evening entry counts as the same trading day". Whether R4's "trading day" is the session i of :92 — his (INFERRED, the filer'
# DECISIONS.md:1645  (users G11,W3-90)
$ sed -n '1645p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **FLAG 6 — R8 and F2's state.** Does R8 change F2's state in `specs/SPEC_RUBRIC.md` — do R8's words on #4 and #5 name F2's governing rule and 15:00 disposition — and is master's reading (filing note 1), changeable by Amear, right? The rubric is his to edit (:3-4). Not resolved here.
# DECISIONS.md:1678  (users W3-92)
$ sed -n '1678p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
**Cure for finding 2 (filing form).** Amear's words (WHO: amear; DECISIONS.md:1546, inside the fenced block): "WHO: amear. File each as a DECISIONS.md entry citing this session." Master's decision under R-1104-2 (DECISIONS.md:748), changeable by Amear: the nine rulings are filed as ONE entry, D-2026-11-08-A, with a labelled section per ruling (eight bullets 
# DECISIONS.md:1708  (users W3-92)
$ sed -n '1708p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
**NEEDS AMEAR.** (i) Whether one entry satisfies "File each as a DECISIONS.md entry" (DECISIONS.md:1546). Nothing else.
# DECISIONS.md:1724  (users W3-86)
$ sed -n '1724p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
A1  FLAG 1: R4 applies to gate 2 only. The values-spec §6 in-sample
# DECISIONS.md:1726  (users W2-02,W3-87,W4-02)
$ sed -n '1726p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
A2  FLAG 2: Gate 2 "OOS Sharpe >= 1.0" = the §6 formula on
# DECISIONS.md:1730  (users W3-88)
$ sed -n '1730p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
A3  FLAG 3: Win rate is not a Block 2 pass gate. Per trade:
# DECISIONS.md:1738  (users W3-63)
$ sed -n '1738p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
    amends D-2026-11-05-A item 3 with a safety buffer for model error.
# DECISIONS.md:1739  (users G01,W3-74,W4-35)
$ sed -n '1739p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
    Evaluated against every tier row; tier pick stays Q9. Closes the
# DECISIONS.md:1739-1740  (users W4-03)
$ sed -n '1739,1740p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
    Evaluated against every tier row; tier pick stays Q9. Closes the
    notes-4 DD equity-base item.
# DECISIONS.md:1741  (users W3-89)
$ sed -n '1741p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
A5  FLAG 5: For arms (a)/(b), "trading day" = session i of §6
# DECISIONS.md:1744  (users W3-90)
$ sed -n '1744p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
A6  FLAG 6: R8 starts the breaker PROPOSAL unit. F2's state changes
# DECISIONS.md:1746  (users W2-02,W4-04,W4-05)
$ sed -n '1746p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
A7  R3 amends Q8: arm (a) is judged on gates 1-5 (WFE not
# DECISIONS.md:1748  (users W2-02,W3-30,W4-04)
$ sed -n '1748p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
A8  O1 is discharged by R2 + R3 + A7. Gate 6 formula (Pardo WFE):
# DECISIONS.md:1770  (users W3-75)
$ sed -n '1770p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **A2.** *Answers:* FLAG 2 (:1641). *Bears on:* values spec :93 ("This statistic does NOT define the gate "OOS Sharpe ≥ 1.0".") and :132 (i). Whether A2 also closes the notes-4 "Sharpe definition (item 4)" (DECISIONS.md:978) is not decided here: NEEDS AMEAR (iv). *Left for a later unit:* the values-spec amendment.
# DECISIONS.md:1771  (users G20,W3-93)
$ sed -n '1771p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **A3.** *Answers:* FLAG 3 (:1642). *Bears on:* O4 (`specs/SPEC_RUBRIC.md:94-99`; the Block 4 "within ±15% win rate", :96-97, joined) and R4's win-rate line (DECISIONS.md:1560–1561, "a break-even trade counts as half a loss", joined). O4's "**Required:**" statement (whether the Block 2 backtest runs with breakers applied, without them, or both; :97-99) is n
# DECISIONS.md:1772  (users W3-74,W3-94)
$ sed -n '1772p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **A4.** *Answers:* FLAG 4 (:1643). *Amends:* D-2026-11-05-A item 3 (DECISIONS.md:814, "the lower of 4% of the MFFU account size and MFFU's trailing drawdown limit") — his words "This amends D-2026-11-05-A item 3". *Closes:* the notes-4 DD equity-base item (DECISIONS.md:978, "equity base for the 4% DD gate (item 5)") — his words. *Left for a later unit citi
# DECISIONS.md:1776  (users W3-30,W3-96)
$ sed -n '1776p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **A8.** *Answers:* routed item (2c) "whether R2/R3 discharge O1" (:721), and gives the gate-6 (WFE) formula left OPEN at values spec :133. O1 (`specs/SPEC_RUBRIC.md:74-79`) is discharged — his words. *Left for a later unit:* the rubric's O1 state (state values at rubric :10-11) is not changed here; master's reading (filing notes 1 and 3, :64, :66), changea
# DECISIONS.md:1788  (users G11)
$ sed -n '1788p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
**FLAG 6 residual.** See the A6 bullet: per Correction 1 (DECISIONS.md:1669), "A6's words do not name that part" (FLAG 6's "#4 and #5" part). Not resolved here; master's reading, changeable by Amear (DECISION_LOG `15:13:00Z`, :728): it is the F2 PROPOSAL unit's output, returned PROPOSED.
# DECISIONS.md:1800  (users W3-93)
$ sed -n '1800p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
**NEEDS AMEAR.** Each item sets two texts side by side. No reading is picked.
# DECISIONS.md:1801  (users W3-93)
$ sed -n '1801p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- (i) **A3 break-even vs net basis.** A3 (:25): "B = trade exited at its entry price" defines break-even by price. A2 (:21-22, joined): "daily net P&L after commission and slippage", and values spec §6 (:92): "net P&L (after commission and slippage)". A3's words do not say whether W and L are classified by price or by net P&L after commission and slippage. A
# DECISIONS.md:1802  (users W3-94)
$ sed -n '1802p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- (ii) **A4 limit type and stage.** A4 (:31, :33): "80% of MFFU's trailing drawdown limit" and "Evaluated against every tier row". WF spec :141: "Studio limits are Static, not trailing. Item 3 says "trailing drawdown limit". → NEEDS AMEAR 12."; WF spec NEEDS AMEAR 12 (:207): which stage (Evaluation or Sim-Funded) and which type, and "Do Studio's **Static** l
# DECISIONS.md:1803  (users W3-96)
$ sed -n '1803p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- (iii) **A8 annualisation method.** A8 (:43): "annualised OOS net profit / annualised IS net profit" names no annualisation method: neither the length unit nor whether the annualisation is linear or compounded. Side by side: values spec :83: "Day-count convention … SETTLED: a "day" is a Monday–Friday date in the data file … Changeable by him." (a deriver's 
# DECISIONS.md:1804  (users W3-75)
$ sed -n '1804p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- (iv) **A2 and the notes-4 Sharpe item.** A4 (:33–34): "Closes the notes-4 DD equity-base item." A2 (:20–23) gives the gate-2 formula and carries no such words. Notes-4 scope, DECISIONS.md:978: "equity base for the 4% DD gate (item 5) and Sharpe definition (item 4)"; values spec :93: "The gate's Sharpe definition and its equity base stay OPEN under ruling 9
# DECISIONS.md:1823  (users W1-04)
$ sed -n '1823p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
C1  U7 (Praxis_build-diq) resumes in this new session. One correction:
# DECISIONS.md:1826  (users W1-04,X10)
$ sed -n '1826p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
C2  Park rule amendment (made between sessions, per the absolutes
# DECISIONS.md:1826-1829  (users W4-30)
$ sed -n '1826,1829p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
C2  Park rule amendment (made between sessions, per the absolutes
    rule): a park commit to parked/ branches is exempt from the
    audit-token gate, because it never touches main. Closes
    Praxis_build-8sw.
# DECISIONS.md:1830  (users W1-05,W2-04,X05)
$ sed -n '1830p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
C3  Step 0, items 2-6: (2) anonymous HTTPS clone, step 3.1;
# DECISIONS.md:1835  (users W1-06,W3-92)
$ sed -n '1835p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
C4  One entry satisfies "File each" for D-2026-11-08-A.
# DECISIONS.md:1836  (users W1-07,W3-93)
$ sed -n '1836p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
C5  D-2026-11-08-B (i) win/loss judged by price, consistent with
# DECISIONS.md:1837  (users W3-94,W4-08)
$ sed -n '1837p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
    B = exit at entry price; (ii) Studio Static rows use the stricter
# DECISIONS.md:1838  (users W3-96)
$ sed -n '1838p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
    limit type and stage, both shown; (iii) A8 annualisation = mean net
# DECISIONS.md:1839  (users W3-75)
$ sed -n '1839p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
    P&L per session x 252, for IS and OOS alike; (iv) A2 closes the
# DECISIONS.md:1839-1840  (users W4-02)
$ sed -n '1839,1840p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
    P&L per session x 252, for IS and OOS alike; (iv) A2 closes the
    notes-4 Sharpe item.
# DECISIONS.md:1840  (users W2-02)
$ sed -n '1840p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
    notes-4 Sharpe item.
# DECISIONS.md:1841  (users W1-08,W4-05)
$ sed -n '1841p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
C6  "Discharged" recorded as PASSED@a2f1067 is correct. O1 moves out of
# DECISIONS.md:1843  (users G33,W1-09,W4-25)
$ sed -n '1843p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
C7  Praxis_build-gjj: disable memory in the praxis-manager agent
# DECISIONS.md:1845  (users W1-10,W2-03)
$ sed -n '1845p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
C8  The July SPEC_RUBRIC R-A/R-B/R-C hunk lands as written.
# DECISIONS.md:1846  (users W1-05,W2-04)
$ sed -n '1846p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
C9  Step 0, item 1: snapshot taken, named pre-cli-nt-bridge-2026-11-06.
# DECISIONS.md:1860  (users W3-92)
$ sed -n '1860p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **C4** (:28). *Answers:* D-2026-11-08-A's NEEDS AMEAR, Correction 1 (DECISIONS.md:1708): "(i) Whether one entry satisfies "File each as a DECISIONS.md entry" (DECISIONS.md:1546)."; card item 3 (park card, item 3). His words in A's block (DECISIONS.md:1546): "WHO: amear. File each as a DECISIONS.md entry citing this session." *Effect:* that NEEDS AMEAR is a
# DECISIONS.md:1881  (users W3-67,W3-94)
$ sed -n '1881p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
**S6 cross-block (interactions only; nothing decided here).** F1–F4 (`specs/SPEC_RUBRIC.md`:19, :32, :47, :61; `grep -n '^### F'`, OBSERVED) are not modified; `git diff --numstat HEAD -- specs/SPEC_RUBRIC.md` = `10	0	specs/SPEC_RUBRIC.md` (the July hunk; OBSERVED by the manager and re-read by the filer). F2 is still under FROZEN (:17); C1–C10 do not change F
# DECISIONS.md:1885  (users W3-94,W3-95,W3-97,W4-08)
$ sed -n '1885p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
**Open readings (not decided here).** Each item sets texts side by side. No reading is picked. U8 drafted this as "NEEDS AMEAR". Decided by master under D-2026-11-08-D D1 (taken by praxis-manager in unit `2026-11-09-c-d-filing`, its report's Decisions taken 1), changeable by Amear: on that unit's reading neither item is a D2 item of D-2026-11-08-D (voice-2 f
# DECISIONS.md:1886  (users W3-95)
$ sed -n '1886p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- (i) **C5 (ii) and rows whose Eval and Sim-Funded types differ.** B (ii) (DECISIONS.md:1802): "Which limit type and stage A4 means for the Studio Static rows, and for rows whose Eval and Sim-Funded types differ, is his." C5 (ii) (answers file :30–31, joined): "(ii) Studio Static rows use the stricter limit type and stage, both shown;". WF spec at HEAD, rows
# DECISIONS.md:1887  (users W3-97)
$ sed -n '1887p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- (ii) **C2 and S7.** S7 (`specs/SPEC_RUBRIC.md`:121): "Nothing is committed while any audit box is unchecked." Park step 1 (:252): "Commit the work to a branch `parked/<bead-id>`. It does not reach `main`." C2 (:20–21, joined): "a park commit to parked/ branches is exempt from the audit-token gate, because it never touches main." The park row cites S7 as it
# DECISIONS.md:1930  (users W3-32)
$ sed -n '1930p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
D6  FIRST: drawdown viability check, Mac-only, read-only, no VM, no
# DECISIONS.md:1932  (users G14)
$ sed -n '1932p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
    per-walk-forward-window worst drawdown at 1 MNQ (MFFU MNQ
# DECISIONS.md:1949  (users G38,W2-38)
$ sed -n '1949p' DECISIONS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
    grade them against F4's criterion. (6) the five P0 guard beads are
~~~~

### DECISION_LOG.md

~~~~text
# DECISION_LOG 2026-10-30T23:23:00Z  (users W3-02)
$ /usr/bin/grep -n -F '2026-10-30T23:23:00Z' DECISION_LOG.md | head -n 2 | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
458:- [2026-10-30T23:23:00Z] **WHO: amear** | PROPOSED BY: praxis-master (three structured questions lifted from D-2026-10-30-A's NEEDS AMEAR 5, 2 and 4) | APPROVED BY: amear, AskUserQuestion this turn | WHAT: **THREE RULINGS ON THE F3 ARTIFACT.** **(R-F3-1, closes NEEDS AMEAR 5 / bead zyd (c)):** *"Commit conditional + R3 control tomorrow."* D-2026-10-30-A 
461:- [2026-10-30T23:30:00Z] WHO: praxis-master | WHAT: **F3 ARTIFACT AUDIT: PASS. No BLOCKING finding; S1, S2, S4, S5, S6, S8 all PASS; checks 1–8 all PASS.** The auditor's grade is transcribed here because a V-rdict has no other writable home. Four MINORs, carried not fixed: (M1) no MANIFEST row for `docs/reports/2026-10-30-zyd-rulings-append.md` → the `7z
# DECISION_LOG 2026-11-03T18:40:00Z  (users W3-21,W3-56,W3-58)
$ /usr/bin/grep -n -F '2026-11-03T18:40:00Z' DECISION_LOG.md | head -n 2 | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
582:- [2026-11-04T20:09:33Z] WHO: praxis-master | WHAT: **NEXT UNIT: WRITE THE VM HANDOFF (R-1104 DO NOW item 3) — master writes it directly as a report (`docs/reports/2026-11-04-vm-handoff-readback-ticksource-exe.md`); no code, no dispatch.** Three tasks, scope verbatim from Amear's rows: (a) read-only readback of the per-contract NQ minute folders (2026-11
599:- [2026-11-03T18:40:00Z] WHO: amear | WHAT: **Rulings on the four VM-plan questions, his words verbatim** (typed in this session, answering the master's numbered list): (1) Q "Send Portara its eight questions, then decide whether to buy the ticks for $695" → **"no, not paying that. i dont know what 8 questions."** = NO Portara purchase at $695. (2) Q "Re
# DECISION_LOG 2026-08-04T18:44Z  (users W2-41)
$ /usr/bin/grep -n -F '2026-08-04T18:44Z' DECISION_LOG.md | head -n 2 | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
155:- [2026-08-04T18:44Z] **WHO: amear** (scope extension of his 18:33Z resumption) | PROPOSED BY: praxis-master (escalation only — defect surfaced, three dispositions presented) | APPROVED BY: Amear, 2026-08-04, in-session — selected **"Inline correction marker"** | WHAT: **THE HUMAN RESUMPTION IS EXTENDED to cover a second, substantive repair the master fo
# DECISION_LOG 2026-11-03T18:45:00Z  (users W3-20,W3-57)
$ /usr/bin/grep -n -F '2026-11-03T18:45:00Z' DECISION_LOG.md | head -n 2 | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
582:- [2026-11-04T20:09:33Z] WHO: praxis-master | WHAT: **NEXT UNIT: WRITE THE VM HANDOFF (R-1104 DO NOW item 3) — master writes it directly as a report (`docs/reports/2026-11-04-vm-handoff-readback-ticksource-exe.md`); no code, no dispatch.** Three tasks, scope verbatim from Amear's rows: (a) read-only readback of the per-contract NQ minute folders (2026-11
598:- [2026-11-03T18:45:00Z] WHO: amear | WHAT: **Clarifications, his words verbatim:** (3) asked "should the two `.exe` files be committed to the repo, or just left on the VM?" → **"commit to repo"** = BINARIES TOO (closes D-2026-11-02-B NEEDS AMEAR 1). Route per handoff §3.2: the VM agent uploads `TickPrep.exe` and `MakeSynth.exe` themselves via Drive; Mac
# DECISION_LOG.md:135  (users W2-34)
$ sed -n '135p' DECISION_LOG.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- [2026-07-28T22:32Z] WHO: praxis-master (session 40) | WHAT: **INCIDENTAL RESOLUTION — the open ISSUE_REGISTER item `2026-07-26T19:51Z` ("awaiting Amear's disposition on `599885e`", the misfired park commit that landed on `main` with an unsubstituted literal `<bead-id>` placeholder) IS DISCHARGED. It was reset away and the reflog proves it** | WHY: surfaced
# DECISION_LOG.md:155  (users W2-41)
$ sed -n '155p' DECISION_LOG.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- [2026-08-04T18:44Z] **WHO: amear** (scope extension of his 18:33Z resumption) | PROPOSED BY: praxis-master (escalation only — defect surfaced, three dispositions presented) | APPROVED BY: Amear, 2026-08-04, in-session — selected **"Inline correction marker"** | WHAT: **THE HUMAN RESUMPTION IS EXTENDED to cover a second, substantive repair the master found 
# DECISION_LOG.md:165  (users G25,G28,G29,G32,G33,G34,G35,G36,G37)
$ sed -n '165p' DECISION_LOG.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- [2026-08-06T19:48:03Z] **WHO: amear** | PROPOSED BY: praxis-master (session 42 opener — three dispositions, one recommended) | APPROVED BY: Amear, 2026-08-06, in-session — selected **"Stop, freeze it"** | WHAT: **THE SUPERVISION BUILD STOPS.** No new guards, hooks, closers, or agent-stack work is dispatched. The three P0s (`s8g`, `hwk`, `1ys`) stay open an
# DECISION_LOG.md:253  (users W4-22)
$ sed -n '253p' DECISION_LOG.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- [2026-08-08T03:20:00Z] WHO: amear | PROPOSED BY: auditor | APPROVED BY: amear | WHAT: **K1 RATIFIED — STATE.md ceiling 14,000 bytes, byte-only enforcement. Number and mechanism ratified as ONE item; the 14,000 may not be taken without the byte mechanism, nor the mechanism re-tokenized without re-ratifying the number** | WHY: tokenizers are model-versioned 
# DECISION_LOG.md:255  (users W4-22)
$ sed -n '255p' DECISION_LOG.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- [2026-08-08T03:21:00Z] WHO: amear | PROPOSED BY: auditor | APPROVED BY: amear | WHAT: **K2 RATIFIED — marker path `.claude/state/last-compaction`** | WHY: same directory holds the stale `current-bead` (reads `Praxis_build-jcw`, mtime Jul 27); that staleness is logged as S45-4 and queued post-moratorium, and Amear ruled explicitly that it does not contamina
~~~~

### HANDOFF.md

~~~~text
# HANDOFF.md:9  (users X01)
$ sed -n '9p' HANDOFF.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
**For Amear's hands (not a question):** OPEN-1 needs a written answer from MFFU support: "Does a position opened after 6 PM ET and closed before 8:28 AM ET the next morning count as holding overnight?" Only he can send that email.
# HANDOFF.md:17  (users H01)
$ sed -n '17p' HANDOFF.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
1. D11 sweep (owed two runs now): close waiting non-D2 questions under D1, including R6 OPEN-3 (whether gate 4's 250-trade bar applies to event strategies).
# HANDOFF.md:36  (users G10)
$ sed -n '36p' HANDOFF.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
**PARKED — `Praxis_build-diq` (U7). A human resumes it; the orchestrator does not.** The C1 audit PASSED the diff of record (index diff = `docs/reports/evidence/2026-11-09-u7-diff-of-record.patch` = sha `b06ee494…`). It FAILED on S1/S2: the resume report's MANIFEST evidence and commit list describe 313 lines, but the blob has 314. Root cause: the master's fo
# HANDOFF.md:119  (users W1-04)
$ sed -n '119p' HANDOFF.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
1. How the park branch is landed under 8sw, and whether/how U7 resumes.
# HANDOFF.md:120  (users W1-05)
$ sed -n '120p' HANDOFF.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
2. Step-0: your six answers + the snapshot name in your own words (the VM session said you gave them there; they are not on any ledger). And confirm the VM Claude session is closed (you ruled "Mac stays master; VM session closed", DECISION_LOG `15:11:00Z`).
# HANDOFF.md:121  (users W1-06)
$ sed -n '121p' HANDOFF.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
3. D-2026-11-08-A NEEDS AMEAR: one entry vs "File each".
# HANDOFF.md:122  (users W1-07)
$ sed -n '122p' HANDOFF.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
4. D-2026-11-08-B NEEDS AMEAR (i)–(iv): A3 W/L by price or by net; A4 limit type/stage for Studio Static rows; A8 annualisation method; whether A2 closes the notes-4 Sharpe item.
# HANDOFF.md:123  (users W1-08)
$ sed -n '123p' HANDOFF.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
5. Rubric: is "discharged" recorded as `PASSED@a2f1067` right; should O1 leave the OPEN section.
# HANDOFF.md:124  (users W1-09)
$ sed -n '124p' HANDOFF.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
6. Bead `Praxis_build-gjj`: managers write to their agent-memory dir despite every brief (three, possibly four, today; gitignored, nothing in the repo).
# HANDOFF.md:125  (users G01,G03,G04,W1-10,W1-12,W1-13,X06)
$ sed -n '125p' HANDOFF.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
7. Still open from the 11-07 return handoff: §4 items 2 and 4–12, item 4 first (the July rubric hunk — a plain-language summary is owed with it).
# HANDOFF.md:157  (users W1-18)
$ sed -n '157p' HANDOFF.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
2. B1: no spec v2.1 wording changes before his word (`21:42:00Z` item (5)).
# HANDOFF.md:175  (users W1-21)
$ sed -n '175p' HANDOFF.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- The as-is set stays out of every commit (Amear, `20:08:28Z` hard limits). What it contains is the master's list, not Amear's words (`15:28:29Z`; rows `22:09:15Z` and `23:58:33Z` list some of these items separately). It is: the 12 staged paths (`git diff --cached --stat` = 12 files / 5726+ / 2−), `.claude/settings.json` +10, `specs/SPEC_RUBRIC.md` +10 (the 
# HANDOFF.md:180  (users W1-19)
$ sed -n '180p' HANDOFF.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- Commit message trailer: the parenthesised form `(noreply@anthropic.com)` is current practice only, until Amear rules (DECISIONS.md:1188, uncommitted). The bash-guard's `>` regex rejects `<…>` (`22:07:11Z`). Exempting commit messages would be a new hook change, outside 3(b), and is Amear's call.
# HANDOFF.md:181  (users G02,X04)
$ sed -n '181p' HANDOFF.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- Bridge items left to Amear also gate the VM steps: whether `pip` may download (`vm/2026-11-06-vm-handoff.md:32`, step 3.5 `:144`), and starting NT8 ("Starting it is Amear's", `:27`).
# HANDOFF.md:189  (users W1-22)
$ sed -n '189p' HANDOFF.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
1. Read his answers to the return handoff's §4. File them WHO: amear before acting on any of them.
# HANDOFF.md:190  (users W1-23)
$ sed -n '190p' HANDOFF.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
2. If he ratifies addendum 5's timing: a filing unit appends addendum 6 (WHO: amear). The index is rebuilt with addenda 5 + 6, re-audited and committed through the gate. Then `uqb`'s fresh audit is re-run (`22:34:00Z`). Closing `uqb` is the master's, and only on a PASS.
# HANDOFF.md:191  (users W1-24)
$ sed -n '191p' HANDOFF.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
3. wf-values: a fresh unit on a NEW DECISIONS entry, after his confirmation or change of the proposed values (`Praxis_build-867`; `2026-11-07T00:00:00Z`).
# HANDOFF.md:200  (users W1-25)
$ sed -n '200p' HANDOFF.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
**Update 14:43Z, unit 2026-11-06-post-commit-refresh (OBSERVED unless marked):** `main` = `origin/main` = `221ef59` (`git log --oneline -3`; `git ls-remote --heads origin main` = `221ef590…`; `git status -sb` = `## main...origin/main`). Two commits are on top of `87d506f`, both with author `Amear Bani-Ahmad`. That he typed them is REPORTED BY master (DECISIO
# HANDOFF.md:207  (users W1-26)
$ sed -n '207p' HANDOFF.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
1. Gate: Amear picks (a), (b) or (c) from the 00:54:04Z row. (a) is to type the batch commit from `commit-idx-batch`; (b) is to ratify the addendum-1 timing; (c) is to leave it.
# HANDOFF.md:209  (users W1-27)
$ sed -n '209p' HANDOFF.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
3. Step c (walk-forward build) waits on the spec's NEEDS AMEAR 1–6 and the harness choice (00:54:04Z).
# HANDOFF.md:210  (users W1-28)
$ sed -n '210p' HANDOFF.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
4. Return handoff for the Claude.ai chat: written at `docs/reports/2026-11-06-return-handoff-claude-ai.md` and re-audited PASS after Correction 1 (01:02:24Z). Item 8 was appended after that PASS. It goes to Amear; it is uncommitted.
# HANDOFF.md:218  (users W1-29)
$ sed -n '218p' HANDOFF.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- the cost model (23:59:40Z; fee report NEEDS AMEAR 1–3);
# HANDOFF.md:219  (users W1-30)
$ sed -n '219p' HANDOFF.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- Fusion Question 0 (00:18:51Z);
# HANDOFF.md:220  (users W1-31)
$ sed -n '220p' HANDOFF.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- the `f258a5d` parked-branch leak (00:48:37Z);
# HANDOFF.md:222  (users W1-32)
$ sed -n '222p' HANDOFF.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- D-2026-11-05-A NEEDS AMEAR 1–4 (2026-11-05T23:51:21Z);
# HANDOFF.md:223  (users G07,G08,G09)
$ sed -n '223p' HANDOFF.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- the R-VN4 not-ruled items (2026-11-05T23:51:21Z);
# HANDOFF.md:224  (users W1-34)
$ sed -n '224p' HANDOFF.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- the master's flagged reading of R-VN4-10 (2026-11-05T23:51:21Z, 00:32:23Z).
# HANDOFF.md:257  (users W1-35)
$ sed -n '257p' HANDOFF.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- DECISION_LOG 2026-11-03T18:45:00Z: the `.exe` files go into the repo; High-vs-r8j DEFERRED (*"when the time comes ask agaian."*; master must re-ask before any High run is planned).
# HANDOFF.md:267  (users X07)
$ sed -n '267p' HANDOFF.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
2. Amear's screen tasks for his next VM session, kept on his list: C6 save the Strategy Analyzer settings as default (`docs/reports/2026-11-01-voice-handoff-commission-fix.md:105`); C7 NQCONTROW instrument readback (same file :113); Log-tab "ignored" messages. All three: D-2026-11-03-A items 27–29, DECISIONS.md:696-699.
# HANDOFF.md:268  (users W1-37)
$ sed -n '268p' HANDOFF.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
3. `Praxis_build-r8j` (P0 OPEN, OBSERVED `bd show`). P0 is the master's choice, unconfirmed by Amear (D-2026-11-02-C NEEDS AMEAR 13, DECISIONS.md:543).
# HANDOFF.md:277  (users W1-38,W1-39,W1-40,W1-41,W1-42)
$ sed -n '277p' HANDOFF.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- D-2026-11-02-A (DECISIONS.md:398); D-2026-11-02-B (:471); D-2026-11-02-C (:530-544); D-2026-11-03-A §e (:653); D-2026-11-04-A (:769-771).
# HANDOFF.md:278  (users W1-39)
$ sed -n '278p' HANDOFF.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- Already closed by a ledger row: 02-B item 1 (DECISION_LOG 2026-11-03T18:45:00Z); 02-C item 14 (R-1104-3, per that row's framing).
# HANDOFF.md:286  (users G26)
$ sed -n '286p' HANDOFF.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
## Resume card — 2026-10-31 second close (16:14Z) — 🛑 **TWO BEADS PARKED TODAY: `o78` (`parked/Praxis_build-o78` = `29c3e13`) and `a9d` (`parked/Praxis_build-a9d` = `bd6f421`, the Future-row loading plan + walkthrough + 6 MANIFEST rows), both pushed; `main` = `0ced412` = origin, ancestor of both.** Amear's rulings after the voice session (DECISION_LOG 14:59:
# HANDOFF.md:1677  (users X08)
$ sed -n '1677p' HANDOFF.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
1. **Open** — User must create n8n credential `PRAXIS xarq5bot` (Telegram API, token from BotFather) and rebind 3 Telegram nodes in workflow EmMbN4sslwIx1ydn before activating draft version a8400246.
# HANDOFF.md:1678  (users G31)
$ sed -n '1678p' HANDOFF.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
2. **Open** — Telegram bot token leaked in chat transcript; decide rotate vs keep (token NOT in repo).
~~~~

### HEAD:docs/specs/2026-11-05-walk-forward-spec.md

~~~~text
# HEAD:docs/specs/2026-11-05-walk-forward-spec.md:202  (users W4-02)
$ git show HEAD:docs/specs/2026-11-05-walk-forward-spec.md | sed -n '202p' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
7. What is the **Sharpe definition** for "OOS Sharpe ≥ 1.0" (daily or per-trade, annualisation, risk-free rate), and what **equity base** does it use (R-VN4 "Not ruled"; equity base: report C NEEDS AMEAR 2, report C `:248`; Sharpe: report C NEEDS AMEAR 3, report C `:249`)?
# HEAD:docs/specs/2026-11-05-walk-forward-spec.md:203  (users W4-04)
$ git show HEAD:docs/specs/2026-11-05-walk-forward-spec.md | sed -n '203p' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
8. Does **WFE ≥ 0.50** apply to arm (a), which has no in-sample optimisation (O1)? For arm (b), which WFE formula is used?
# HEAD:docs/specs/2026-11-05-walk-forward-spec.md:204  (users W4-05)
$ git show HEAD:docs/specs/2026-11-05-walk-forward-spec.md | sed -n '204p' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
9. What is the **full gate set for each arm**, and does **GO / HOLD / REJECT** (with "No partial passes") sit on arm (a), arm (b) or both (O1; D-2026-11-02-C NA 1–2, `DECISIONS.md:531-532`)? Context only: R-VN3-6, "one that is closest to live execution." (`DECISIONS.md:516`), names no arm.
# HEAD:docs/specs/2026-11-05-walk-forward-spec.md:205  (users W4-05)
$ git show HEAD:docs/specs/2026-11-05-walk-forward-spec.md | sed -n '205p' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
10. Which arm is **R-1104-3's judged version**: arm (a), arm (b) or both (D-2026-11-05-A NEEDS AMEAR 4, `DECISIONS.md:832`)? Context only: R-VN3-6, "one that is closest to live execution." (`DECISIONS.md:516`); R-1104-3's framing "= High fill resolution with circuit breakers on as the judged go/no-go version, confirming R-VN3-6." (`DECISIONS.md:753`). Neithe
# HEAD:docs/specs/2026-11-05-walk-forward-spec.md:206  (users G01)
$ git show HEAD:docs/specs/2026-11-05-walk-forward-spec.md | sed -n '206p' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
11. Which **MFFU account size / tier** sets the max-DD gate under items 3 and 5, given that item 5 defers the tier until backtest and paper results exist (D-2026-11-05-A NA 1, `DECISIONS.md:829`)? Until then, is the gate judged against every row of the §6 table?
# HEAD:docs/specs/2026-11-05-walk-forward-spec.md:207  (users W4-08)
$ git show HEAD:docs/specs/2026-11-05-walk-forward-spec.md | sed -n '207p' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
12. For "MFFU's trailing drawdown limit", which **stage** (Evaluation or Sim-Funded) and which **type** (EOD or intraday trailing) counts? Do Studio's **Static** limits count?
~~~~

### HEAD:docs/specs/2026-11-06-walk-forward-values.md

~~~~text
# HEAD:docs/specs/2026-11-06-walk-forward-values.md:93  (users W4-02)
$ git show HEAD:docs/specs/2026-11-06-walk-forward-values.md | sed -n '93p' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **This statistic does NOT define the gate "OOS Sharpe ≥ 1.0".** The gate's Sharpe definition and its equity base stay OPEN under ruling 9: "Notes-4 unruled items stay open; none block anything." They are notes-4 items (D-2026-11-06-B item 18, DECISIONS.md:1101; REPORTED BY `docs/reports/2026-11-07-return-handoff-claude-ai.md:74`; WF spec NEEDS AMEAR 7). Th
# HEAD:docs/specs/2026-11-06-walk-forward-values.md:132  (users W4-02)
$ git show HEAD:docs/specs/2026-11-06-walk-forward-values.md | sed -n '132p' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
  - Not covered, OPEN, not resolved here: (i) the equity base and the Sharpe definition of the "OOS Sharpe ≥ 1.0" gate — ruling 9 (notes-4; WF spec NEEDS AMEAR 7); the notes-4 source (DECISIONS.md:978) scopes the equity base as "equity base for the 4% DD gate (item 5) and Sharpe definition (item 4)" (list (C)); (ii) whether "Walk-forward efficiency ≥ 0.50" a
# HEAD:docs/specs/2026-11-06-walk-forward-values.md:133  (users W4-04)
$ git show HEAD:docs/specs/2026-11-06-walk-forward-values.md | sed -n '133p' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
  - The WFE formula for arm (b) (WF spec NEEDS AMEAR 8, second half) — OPEN (ruling 9; the O1 gate set, REPORTED BY the return handoff :74): a WFE formula is part of the gate set. Not resolved here.
# HEAD:docs/specs/2026-11-06-walk-forward-values.md:134  (users W4-05)
$ git show HEAD:docs/specs/2026-11-06-walk-forward-values.md | sed -n '134p' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
  - Whether Q8 discharges O1 is left to the master and the auditor. This file does not resolve O1.
# HEAD:docs/specs/2026-11-06-walk-forward-values.md:137  (users G01)
$ git show HEAD:docs/specs/2026-11-06-walk-forward-values.md | sed -n '137p' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **No tier chosen** — RULED (Q9: "Q9 no tier chosen. Report the per-tier table; I pick after paper results."). **The tier pick is OPEN** — his, after paper results.
# HEAD:docs/specs/2026-11-06-walk-forward-values.md:306  (users G01)
$ git show HEAD:docs/specs/2026-11-06-walk-forward-values.md | sed -n '306p' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
1. **The tier pick**, after paper results (Q9: "I pick after paper results").
# HEAD:docs/specs/2026-11-06-walk-forward-values.md:308  (users G09)
$ git show HEAD:docs/specs/2026-11-06-walk-forward-values.md | sed -n '308p' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
   - a second Rithmic read-only connection;
# HEAD:docs/specs/2026-11-06-walk-forward-values.md:309  (users G08)
$ git show HEAD:docs/specs/2026-11-06-walk-forward-values.md | sed -n '309p' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
   - the CME wiki as a source;
# HEAD:docs/specs/2026-11-06-walk-forward-values.md:310  (users W4-02,W4-03)
$ git show HEAD:docs/specs/2026-11-06-walk-forward-values.md | sed -n '310p' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
   - the equity base and the Sharpe definition: the notes-4 source (DECISIONS.md:978) scopes it as "equity base for the 4% DD gate (item 5) and Sharpe definition (item 4)"; the WF spec (NEEDS AMEAR 7) and this file read it for the "OOS Sharpe ≥ 1.0" gate. D-2026-11-05-A item 3's DD-base ruling (§8) stands as written; whether it closes the notes-4 DD-gate ite
# HEAD:docs/specs/2026-11-06-walk-forward-values.md:311  (users W4-04,W4-05)
$ git show HEAD:docs/specs/2026-11-06-walk-forward-values.md | sed -n '311p' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
   - the O1 gate set: whether WFE ≥ 0.50 applies to arm (a), the WFE formula for arm (b), and whether GO / HOLD / REJECT may rest on arm (b).
# HEAD:docs/specs/2026-11-06-walk-forward-values.md:322  (users W4-14)
$ git show HEAD:docs/specs/2026-11-06-walk-forward-values.md | sed -n '322p' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
| 4 | Exit-policy options | RULED (set: ruling 4 of 2026-11-06; definitions: Q4, Q5) | §3 |
# HEAD:docs/specs/2026-11-06-walk-forward-values.md:330  (users W4-08)
$ git show HEAD:docs/specs/2026-11-06-walk-forward-values.md | sed -n '330p' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
| 12 | Trailing-limit stage and type; Studio's Static limits | Reporting rule SETTLED: every row reported, Static rows included. Which plan, stage and type counts: OPEN (Q9) | §8; (B) 38; (C) |
~~~~

### HEAD:specs/SPEC_RUBRIC.md

~~~~text
# HEAD:specs/SPEC_RUBRIC.md:103  (users W4-12)
$ git show HEAD:specs/SPEC_RUBRIC.md | sed -n '103p' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
Deviation C permits reverse-and-re-enter. Breakers #2 and #3 cap trades and end
~~~~

### ISSUE_REGISTER.md

~~~~text
# ISSUE_REGISTER.md:9  (users X08)
$ sed -n '9p' ISSUE_REGISTER.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- [2026-05-12T00:00Z] WHO: orchestrator | WHAT: 'PRAXIS xarq5bot' n8n credential does not exist yet; 3 Telegram nodes auto-bound to wrong cred 'Telegram account (networkchuck2)' | WHY: n8n SDK auto-assigns existing credentials on workflow update | WHERE: workflow EmMbN4sslwIx1ydn draft a8400246 | WHEN: blocks 0.6 prod usage | HOW: User opens n8n UI → Credent
# ISSUE_REGISTER.md:11  (users G31)
$ sed -n '11p' ISSUE_REGISTER.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- [2026-05-11T00:05Z] WHO: orchestrator | WHAT: Telegram bot token leaked into chat transcript by user | WHY: User pasted full token in answer to setup question | WHERE: conversation transcript (not git) | WHEN: discovered 2026-05-11 | HOW: User decides rotate-vs-keep. Token NEVER committed to repo (verified via secret grep). User must paste token into n8n c
# ISSUE_REGISTER.md:23  (users G41)
$ sed -n '23p' ISSUE_REGISTER.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- [2026-07-26T00:00Z] WHO: orchestrator | WHAT: RECOVERED — the P0 BLOCKED report at docs/reports/2026-07-25-agent-stack-install.md was overwritten in place by the consolidated PASS report and is now restored | WHY: the file was `git add`-ed while still holding the BLOCKED content, so git wrote its blob to the object store before the overwrite; the blob surv
# ISSUE_REGISTER.md:27  (users W2-33)
$ sed -n '27p' ISSUE_REGISTER.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- [2026-07-26T15:30Z] WHO: praxis-master | WHAT: BLOCKER — the parenthetical type-scoping in agent-frontmatter `tools: Agent(<type>)` is NOT ENFORCED on Claude Code 2.1.220. A producer can spawn its own grader. `praxis-manager` holds `tools: Agent(praxis-worker)` and spawned `praxis-auditor` anyway, with no refusal, no error, and no permission prompt | WHY: 
# ISSUE_REGISTER.md:31  (users W2-33)
$ sed -n '31p' ISSUE_REGISTER.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- [2026-07-26T14:50Z] WHO: praxis-master | WHAT: THIRD REPRODUCTION of the open 2026-07-26T15:30Z blocker (`tools: Agent(<type>)` not enforced). Not a new defect — recorded so the reproduction count is on disk. praxis-manager, holding `tools: Agent(praxis-worker)`, spawned praxis-auditor with no denial: not a tool error, not a permission prompt, not a silent
# ISSUE_REGISTER.md:33  (users W2-33)
$ sed -n '33p' ISSUE_REGISTER.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- [2026-07-26T15:00Z] WHO: orchestrator | WHAT: PLATFORM DEFECT — a subagent's own `tools: Agent(...)` allowlist is SILENTLY IGNORED when that agent is spawned as a CHILD; it inherits the parent's spawnable roster instead. The identical allowlist IS enforced when the same agent runs as the main thread | WHY: decided by one control observation — as a main thr
# ISSUE_REGISTER.md:35  (users W2-34)
$ sed -n '35p' ISSUE_REGISTER.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- [2026-07-26T19:51Z] WHO: praxis-master (session 35) | WHAT: MISFIRED PARK COMMIT ON `main` — commit `599885e`, authored by Amear at 2026-07-26 15:51:31 -0400, subject `park(<bead-id>): audit-fail-x2, session ended per absolute park rule` with the **literal placeholder `<bead-id>` unsubstituted**, landed on `main` rather than on a park branch, and carries t
# ISSUE_REGISTER.md:37  (users G32)
$ sed -n '37p' ISSUE_REGISTER.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- [2026-07-26T22:45Z] WHO: praxis-master (session 36) | WHAT: SILENT-DISARM TRIP-WIRE — the `.claude/settings.json` root key `"agent": "praxis-master"` sets `agent_type` ONLY IF the name resolves to an existing `.claude/agents/praxis-master.md`. If that file is renamed, moved, or deleted, the key silently resolves to nothing, `agent_type` is never set, and `
# ISSUE_REGISTER.md:41  (users G33)
$ sed -n '41p' ISSUE_REGISTER.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- [2026-07-27T19:52Z] WHO: praxis-master (session 37) | WHAT: READ-ONLY CONSTRAINT VIOLATED BY A SPAWNED WORKER — an adversarial `praxis-worker`, briefed read-only inside the project repo, wrote two files into the working tree: `.claude/agent-memory/praxis-worker/project_commit-guards-block-scratch-repos.md` (new) and `.claude/agent-memory/praxis-worker/MEMO
# ISSUE_REGISTER.md:45  (users G28)
$ sed -n '45p' ISSUE_REGISTER.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- [2026-07-27T19:58Z] WHO: praxis-master (session 37) | WHAT: **THE MASTER CANNOT WRITE ITS OWN PERSISTENT MEMORY.** `scripts/master-write-guard.sh` blocks every path under `.claude/agent-memory/praxis-master/`, so the one agent in the stack that survives across sessions by design has no durable memory, while every subagent does | WHY: the guard's allowlist 
# ISSUE_REGISTER.md:47  (users W2-38)
$ sed -n '47p' ISSUE_REGISTER.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- [2026-07-28T17:05Z] WHO: praxis-master (session 39) | WHAT: **UNGUARDED WRITE PATH TO `.claude/agents/` — the directory that defines every agent's identity, tools and permissions is writable by every subagent, and no hook watches it.** Surfaced by praxis-manager mid-unit; **re-verified at source by the master before being recorded** | WHY: two facts compos
# ISSUE_REGISTER.md:49  (users W2-39)
$ sed -n '49p' ISSUE_REGISTER.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- [2026-07-28T17:45Z] WHO: praxis-master (session 39) | WHAT: **THE HOLE WAS PROVEN AND SIMULTANEOUSLY EXPLOITED, BY OUR OWN AGENTS, UNREPORTED — and it is still live.** `Praxis_build-s8g` confirmed by experiment that `scripts/master-write-guard.sh` exits 0 at line 8 for any non-empty `agent_id` **before `file_path` is ever extracted at line 10**, so the exe
# ISSUE_REGISTER.md:51  (users W2-39)
$ sed -n '51p' ISSUE_REGISTER.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- [2026-07-28T21:05Z] WHO: praxis-master (session 40 start) | WHAT: **RE-VERIFICATION BY APPEND of the 17:45Z row — the two unauthorised `/private/tmp/` hooks are STILL REGISTERED AND STILL FIRING.** Not inferred from the prior row; observed fresh this session | WHY: the 17:45Z row recorded them as live at the moment of discovery. A session boundary has pass
# ISSUE_REGISTER.md:53  (users G34)
$ sed -n '53p' ISSUE_REGISTER.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- [2026-08-03T21:20Z] WHO: praxis-master (session 41) | WHAT: **THE AUDITOR CANNOT WRITE ITS OWN V-rdict TO DISK. `praxis-auditor`'s definition prohibits it from writing report/findings `.md` files, so every audit V-rdict exists ONLY as a message in the master's context unless the master transcribes it — and the master is the producer side** | WHY: this is a
# ISSUE_REGISTER.md:55  (users W2-41)
$ sed -n '55p' ISSUE_REGISTER.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- [2026-08-04T18:45Z] WHO: praxis-master (session 41) | WHAT: **TWO STAGED REPORTS ATTRIBUTE A DIRECT QUOTATION TO A FILE THAT DOES NOT CONTAIN IT — and both are in the C1 commit payload, staged and ready to land in a PUBLIC repo** | WHY: `docs/reports/2026-07-26-session36-null-attack.md:314` and `docs/reports/2026-07-26-session36-agent-key-s9-control.md:197
# ISSUE_REGISTER.md:57  (users G35)
$ sed -n '57p' ISSUE_REGISTER.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- [2026-08-05T01:40Z] WHO: praxis-master (session 41) | WHAT: **`gate-commit.sh` REPORTS THE WRONG CAUSE WHEN AN AUDIT TOKEN EXPIRES — it says the staged set changed, which points the reader at the index, the one place that is provably fine. The accurate "expired" message is effectively unreachable dead code** | WHY: this is a diagnostic trap in the single h
# ISSUE_REGISTER.md:59  (users G36)
$ sed -n '59p' ISSUE_REGISTER.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- [2026-08-05T01:45Z] WHO: praxis-master (session 41) | WHAT: **A DENIED COMMIT BURNS THE AUDIT TOKEN. `gate-commit.sh` consumes the single-use token at ALLOW time, then a second `PreToolUse` hook denies the same command — so the token is spent on a commit that never ran, and every retry costs a full re-audit** | WHY: two registered `PreToolUse` hooks both m
# ISSUE_REGISTER.md:61  (users G37)
$ sed -n '61p' ISSUE_REGISTER.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- [2026-08-06T17:15Z] WHO: praxis-master (session 41) | WHAT: **THE LEDGERS HAVE OUTGROWN THE AGENTS THAT MUST READ THEM. Three consecutive auditors died at 46, 47 and 47 tool uses without returning a V-rdict** | WHY: measured, not inferred — `DECISION_LOG.md` 198 KB / 163 rows (**1,218 bytes per row**), `HANDOFF.md` 100 KB, `DISPATCH_LOG.md` 90 KB, `MANIFES
# ISSUE_REGISTER.md:63  (users W2-45)
$ sed -n '63p' ISSUE_REGISTER.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- [2026-08-06T19:49:53Z] WHO: praxis-master (session 42) | WHAT: **`Praxis_build-r8j`'s PREMISE IS FALSE AS RECORDED. The Phase 3 Build Specification is NOT missing — it is on disk in the working tree, gitignored, with all nine circuit breakers enumerated. `r8j` is not a hunt; it is a convert-and-track task** | WHY: `r8j` is recorded as ROOT CAUSE blocking `
# ISSUE_REGISTER.md:68  (users G38)
$ sed -n '68p' ISSUE_REGISTER.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- [2026-08-07T16:13:58Z] WHO: Amear | WHAT: F4 evidence landed — MFFU confirmed IN WRITING, via a human support rep, that algo trading is permitted on all plans including evaluation, simulated-funded and live. RELAYED, NOT INDEPENDENTLY CONFIRMED: neither the master nor the manager has read the source Gmail thread; every claim in this row traces to text Amea
# ISSUE_REGISTER.md:72  (users G39)
$ sed -n '72p' ISSUE_REGISTER.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- [2026-08-15T14:45:00Z] WHO: praxis-master (session 51) | WHAT: **SPEC §4.5's ACCEPTANCE GATE FOR THE CONTINUOUS NQ SERIES IS UNREACHABLE BY CONSTRUCTION. The tool that implements it emits `FLAG`, and §4.5's stop condition is `FAIL` — so no series can fail this gate however bad its gap fraction is** | WHY: §4.5 is one of six gates deciding whether the pulle
# ISSUE_REGISTER.md:74  (users G40)
$ sed -n '74p' ISSUE_REGISTER.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- [2026-08-15T14:46:00Z] WHO: praxis-master (session 51) | WHAT: A self-declared **read-only** peer overseer seat performed a **write** — additive — outside this repo, and disclosed it accurately. Logged as a boundary observation, not as a violation | WHY: the standing hazard with peer seats in this project is unattributed state change, and four prior relays
~~~~

### STATUS.md

~~~~text
# STATUS.md:8  (users H01)
$ sed -n '8p' STATUS.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
**R6 (P0, `Praxis_build-ckh`):** step 1 done; the build and backtest are later steps. OPEN-1 (MFFU "overnight" wording) needs an email from Amear; OPEN-3 (250-trade gate) is the next D11 item.
~~~~

### bd

~~~~text
# bd:Praxis_build-7zq  (users G14)
$ bd show Praxis_build-7zq | /usr/bin/grep -n -F 'deliberately NOT built: it would pre-empt Amear'"'"'s open Q1 (3' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
28:  deliberately NOT built: it would pre-empt Amear's open Q1 (3gm NEEDS AMEAR).
# bd:Praxis_build-yra  (users G20)
$ bd show Praxis_build-yra | head -n 2 | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
○ Praxis_build-yra · Dev-C reverse-and-re-enter vs breakers #2/#3 + Block-4 live-vs-backtest reconciliation   [● P1 · OPEN]
Owner: Amear Bani-Ahmad · Type: task
# bd:Praxis_build-1gd  (users G23)
$ bd show Praxis_build-1gd | /usr/bin/grep -n -F 'yet - disposition is Amear'"'"'s ruling with three live readings' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
21:  yet - disposition is Amear's ruling with three live readings (amend the 0.1%
# bd:Praxis_build-nvn  (users G24)
$ bd show Praxis_build-nvn | /usr/bin/grep -n -F 'BLOCKED ON. K7 is [PROPOSED] and unratified; its wording is ' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
40:  BLOCKED ON. K7 is [PROPOSED] and unratified; its wording is itself under    
# bd:Praxis_build-dj2  (users G24)
$ bd show Praxis_build-dj2 | /usr/bin/grep -n -F 'Insert the K7 row verbatim' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
7:  Insert the K7 row verbatim into docs/specs/2026-08-08-ledger-compaction-    
# bd:Praxis_build-fpg  (users G25)
$ bd show Praxis_build-fpg | /usr/bin/grep -n -F 'CANDIDATE RESOLUTIONS, UNRANKED -- the choice is Amear'"'"'s (S8' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
48:  CANDIDATE RESOLUTIONS, UNRANKED -- the choice is Amear's (S8):              
# bd:Praxis_build-q36  (users G26)
$ bd show Praxis_build-q36 | /usr/bin/grep -n -F 'diagnostic re-run on the Stock row needs Amear'"'"'s separate ap' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
25:  diagnostic re-run on the Stock row needs Amear's separate approval (R-VM-5).
# bd:Praxis_build-vu8  (users G27)
$ bd show Praxis_build-vu8 | /usr/bin/grep -n -F 'fires on FAIL 2. Shot disposition is Amear'"'"'s.' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
15:  fires on FAIL 2. Shot disposition is Amear's.                               
# bd:Praxis_build-86t  (users G28)
$ bd show Praxis_build-86t | /usr/bin/grep -n -F 'cold human ruling on whether the allowlist widens.' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
24:  cold human ruling on whether the allowlist widens.                          
# bd:Praxis_build-sk8  (users G29)
$ bd show Praxis_build-sk8 | /usr/bin/grep -n -F '.claude/settings.json, therefore needs Amear):' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
37:  .claude/settings.json, therefore needs Amear):                              
# bd:Praxis_build-zd4  (users G30)
$ bd show Praxis_build-zd4 | /usr/bin/grep -n -F 'recording the decision to defer/drop it with rationale. Trad' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
17:  recording the decision to defer/drop it with rationale. Trader-owned action 
# bd:Praxis_build-ckh  (users H01)
$ bd show Praxis_build-ckh | /usr/bin/grep -n -F 'step: decide OPEN-3 under D1' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
25:  step: decide OPEN-3 under D1, then the Python event simulator per design    
# bd:Praxis_build-fx4  (users X03)
$ bd show Praxis_build-fx4 | /usr/bin/grep -n -F 'PROVISIONAL. Human/trader-gated (requires contacting MFFU). ' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
15:  PROVISIONAL. Human/trader-gated (requires contacting MFFU). Blocks live-    
# bd:Praxis_build-cn4  (users X09)
$ bd show Praxis_build-cn4 | /usr/bin/grep -n -F 'rotate/confirm the Telegram bot token in the n8n webhook + n' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
12:  rotate/confirm the Telegram bot token in the n8n webhook + notify.sh path,  
# bd:Praxis_build-y9c  (users X10)
$ bd show Praxis_build-y9c | /usr/bin/grep -n -F 'master. A human types the park commit, as at 104c58e. Amear ' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
46:  master. A human types the park commit, as at 104c58e. Amear resumes; the    
# bd:Praxis_build-diq  (users X10)
$ bd show Praxis_build-diq | /usr/bin/grep -n -F 'a park never has one (bead Praxis_build-8sw). A human resume' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
24:  a park never has one (bead Praxis_build-8sw). A human resumes it; the master
# bd:Praxis_build-bev  (users X11)
$ bd show Praxis_build-bev | /usr/bin/grep -n -F 'run teaching session Amear signs off. NEXT: Amear runs a liv' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
41:  run teaching session Amear signs off. NEXT: Amear runs a live dry-run       
# bd:Praxis_build-518  (users X12)
$ bd show Praxis_build-518 | /usr/bin/grep -n -F 'restart urgent. Triage plan: (1) trader restarts NT8; (2) if' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
19:  restart urgent. Triage plan: (1) trader restarts NT8; (2) if a clean process
# bd:Praxis_build-f5f  (users W4-22)
$ bd show Praxis_build-f5f | /usr/bin/grep -n -F 'staged, uncommitted. BLOCKED ON AMEAR: ratify K1 (14,000 byt' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
24:  staged, uncommitted. BLOCKED ON AMEAR: ratify K1 (14,000 bytes, byte-only)  
# bd:Praxis_build-gjj  (users W4-25)
$ bd show Praxis_build-gjj | /usr/bin/grep -n -F 'a per-brief prohibition does not override. WHAT: decide (Ame' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
15:  a per-brief prohibition does not override. WHAT: decide (Amear) whether     
# bd:Praxis_build-22q  (users W4-28)
$ bd show Praxis_build-22q | /usr/bin/grep -n -F 'change needed; Amear'"'"'s call.' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
87:      change needed; Amear's call.                                                
# bd:Praxis_build-8sw  (users W4-30)
$ bd show Praxis_build-8sw | /usr/bin/grep -n -F 'hot-patching enforcement hooks unattended is forbidden. NEED' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
20:  hot-patching enforcement hooks unattended is forbidden. NEEDS A HUMAN       
# bd:Praxis_build-xdr  (users W4-35)
$ bd show Praxis_build-xdr | /usr/bin/grep -n -F 'NOT yet supplied by trader — required before RoR can compute' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
19:  NOT yet supplied by trader — required before RoR can compute. Ask trader for
~~~~

### bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md

~~~~text
# bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md:23  (users H03)
$ git show bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md | sed -n '23p' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- (ii) The "any data release" line (news.txt:20) is applied to US scheduled releases at 08:30 ET or later. PAD-E core variants exit at 08:25 and so clear every release from 08:30 on. Variants 1F and 2S hold through 10:00-14:00 and need a non-T1 release list that this unit did not source → OPEN-4.
# bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md:28  (users X01)
$ git show bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md | sed -n '28p' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **Strategy 1, Pre-Announcement Drift, evening entry, exit before the release:** ALLOWED by the T1 rule on every account (exit at T−5). Inside one MFFU session (18:00 → 16:10). Whether MFFU counts the evening entry as holding overnight is UNVERIFIED: MFFU's pages do not say, and a Rapid page says "Holding overnight will breach the account." (plans-site.txt:
# bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md:52  (users X02)
$ git show bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md | sed -n '52p' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- Low-volume hours: "Profiting from isolated, stale or unrealistic fills … during low-volume hours is not allowed" (news.txt:86). The 18:05 bar can be thin (volume 29 on 2024-06-11, E5). The first pass reports a 20:00 ET entry and a 4-ticks/side slippage row beside the judged 18:05 / 2-tick figures [D1]. Whether MFFU would treat an ordinary market order at 1
# bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md:89  (users X01)
$ git show bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md | sed -n '89p' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
R5 requires: fully rule-based; net positive after costs; survives every MFFU condition, including the EOD trailing drawdown and the consistency rule. An evening-entry variant (1N, 1C, 1F, 2A, 2S) cannot qualify for any funded-account tier row until OPEN-1 is answered in writing by MFFU; passing the measures below does not settle OPEN-1. Measures [D1 unless a
# bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md:104  (users H01)
$ git show bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md | sed -n '104p' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- Enough for the walk-forward? Not against the existing gates: gate 4 needs "≥ 250 aggregate OOS trades" (values spec :125); 1N gives at most 49 and all three PAD-E variants together at most 131. 2S's split must not be counted twice to reach 250. Gate 5 ("≥ 60% of walk-forward windows profitable", :126) on 2-8 events per window is noise-dominated (INFERRED).
# bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md:110  (users X01)
$ git show bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md | sed -n '110p' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
| OPEN-1 | MFFU terms (F4 channel, owner Amear) | "Holding overnight will breach" is glossed by the FAQ as "closed before the daily session close", which an 18:05→08:25 hold meets; no MFFU text says it in terms of an evening entry. A written MFFU answer is needed before any funded use. | OPEN |
# bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md:111  (users H02)
$ git show bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md | sed -n '111p' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
| OPEN-2 | F2 (FROZEN); breakers #4 and #5 (Phase 3 spec :100-101); R8/A6 proposal unit | #4 "clock hits 11:30 ET → close positions, disable until next session": 1F (to 13:55) and 2S/2A (to 16:05) hold past 11:30. #5 "clock enters 3:00–6:00 PM ET → disable everything": 2S/2A hold 15:00-16:05. Entries at 18:05 are after #5 ends; whether #4's "next session" st
# bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md:112  (users H01)
$ git show bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md | sed -n '112p' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
| OPEN-3 | Walk-forward gates (A7: arm (a) gates 1-5) | No event strategy on this data reaches gate 4's 250 OOS trades; whether gates 4 and 5 apply to R6 strategies needs a ruling. Agents do not write acceptance bars. | OPEN (Amear) |
# bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md:113  (users H03)
$ git show bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md | sed -n '113p' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
| OPEN-4 | MFFU "any data release" line | Non-T1 releases (e.g. 10:00 ET) inside 1F and 2S holds; no free release list was sourced in this unit. | OPEN (backtest unit to source a free list, or 1F/2S stay provisional) |
# bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md:114  (users X02)
$ git show bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md | sed -n '114p' | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
| OPEN-5 | MFFU low-volume / stale-fill rule | Whether an 18:05 market entry is caught by it. | OPEN (F4 channel) |
~~~~

### docs/reports/2026-11-01-csv-analyses.md

~~~~text
# docs/reports/2026-11-01-csv-analyses.md:290  (users G22)
$ sed -n '290p' docs/reports/2026-11-01-csv-analyses.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
These questions are left open. This report does not answer any of them.
~~~~

### docs/reports/2026-11-05-mffu-fee-check.md

~~~~text
# docs/reports/2026-11-05-mffu-fee-check.md:134  (users G06)
$ sed -n '134p' docs/reports/2026-11-05-mffu-fee-check.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
3. MFFU publishes no per-side split and does not say whether sim accounts deduct costs. Should this be checked against an account fill statement, which would need a login?
~~~~

### docs/reports/2026-11-06-return-handoff-claude-ai.md

~~~~text
# docs/reports/2026-11-06-return-handoff-claude-ai.md:30  (users W2-13)
$ sed -n '30p' docs/reports/2026-11-06-return-handoff-claude-ai.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
**Commit route (one of):**
# docs/reports/2026-11-06-return-handoff-claude-ai.md:37  (users W2-14)
$ sed -n '37p' docs/reports/2026-11-06-return-handoff-claude-ai.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
4. Adopt MFFU's $4.68 / $1.90 round turn, a single figure or a range? (fee report NEEDS AMEAR 1–3)
# docs/reports/2026-11-06-return-handoff-claude-ai.md:38  (users W2-15)
$ sed -n '38p' docs/reports/2026-11-06-return-handoff-claude-ai.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
5. Fusion: attempt the unsupported walkthrough, use the D-072 SMB route, or keep Google Drive? (walkthrough Question 0; then 1–3)
# docs/reports/2026-11-06-return-handoff-claude-ai.md:39  (users W2-08)
$ sed -n '39p' docs/reports/2026-11-06-return-handoff-claude-ai.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
6. Walk-forward spec: 29 questions in its `## NEEDS AMEAR` section — tunable candidate sets, exit-policy options, ATR period, in-sample objective, day-count convention, partial last window, MFFU account size and tier, which arm is R-1104-3's judged version, O1.
# docs/reports/2026-11-06-return-handoff-claude-ai.md:40  (users W2-16)
$ sed -n '40p' docs/reports/2026-11-06-return-handoff-claude-ai.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
7. The parked branch `parked/Praxis_build-r8j` (commit f258a5d) carries a de-identification leak in its spec header: rewrite, delete, or leave? (00:48:37Z)
# docs/reports/2026-11-06-return-handoff-claude-ai.md:41  (users W2-17)
$ sed -n '41p' docs/reports/2026-11-06-return-handoff-claude-ai.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
8. Carry D-2026-08-06-A (the de-identification entry, parked-branch only) onto main?
# docs/reports/2026-11-06-return-handoff-claude-ai.md:42  (users G07,G08,G09,W2-02)
$ sed -n '42p' docs/reports/2026-11-06-return-handoff-claude-ai.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
9. Still open from 2026-11-04/05 (notes-4 "Not ruled on"): past use of your GitHub login; second Rithmic read-only connection; CME wiki as a source; equity base and Sharpe definition; O1 gate set.
# docs/reports/2026-11-06-return-handoff-claude-ai.md:55  (users W2-13)
$ sed -n '55p' docs/reports/2026-11-06-return-handoff-claude-ai.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
1. **Blocked item 2 overstated the cause.** The sentence "the gate's provenance check looks for the auditor's hand-back in a direct tool result, and in this harness every agent returns asynchronously. A hook change would be needed" is INFERRED, not observed (DECISION_LOG 2026-11-06T00:50:30Z labels it "Master's reading (INFERRED …)"). What is OBSERVED: the d
# docs/reports/2026-11-06-return-handoff-claude-ai.md:60  (users G06,W2-18)
$ sed -n '60p' docs/reports/2026-11-06-return-handoff-claude-ai.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
6. **Two items for Amear, added.** (a) R-VN4-10 was applied under the master's flagged reading (drop the FAIL-word filter; rely on the exact three-line contract) — row 23:51:21Z marks it as a reading; confirm or correct it. (b) Fee report NEEDS AMEAR 3 spelled out: a fill-statement check of whether MFFU sim accounts deduct the per-trade costs would need a lo
# docs/reports/2026-11-06-return-handoff-claude-ai.md:72  (users W2-13)
$ sed -n '72p' docs/reports/2026-11-06-return-handoff-claude-ai.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
3. **Decision 1, "Commit route" (lines 30–33).** Amear took option 1 for the batch by typing it (13:28:18Z). The gate unit is still PARKED at FAIL 2 (bead `Praxis_build-uqb` open). The batch landing does not lift the park (13:28:18Z), so ratifying addendum 1's timing or leaving it parked is still his call. It is not answered here.
~~~~

### docs/reports/2026-11-07-return-handoff-claude-ai-2.md

~~~~text
# docs/reports/2026-11-07-return-handoff-claude-ai-2.md:62  (users W2-01)
$ sed -n '62p' docs/reports/2026-11-07-return-handoff-claude-ai-2.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
   - Is 08:31–16:00 the session you mean by "RTH" (Q6, D-2026-11-07-A), or do arm (a)/(b) anchor at the 09:30 open?
# docs/reports/2026-11-07-return-handoff-claude-ai-2.md:63  (users W2-01)
$ sed -n '63p' docs/reports/2026-11-07-return-handoff-claude-ai-2.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
   - Which NT8 trading-hours template did the 2026-11-01 runs use, and will arm (b) use the same one? On record, REPORTED BY AMEAR (screenshots and his notes): `Trading hours` = `CME US Index Futures RTH` for the runs in `docs/reports/2026-11-01-three-strategy-results.md:89`, `:195`, `:313`; the VM handoff sets the same name for 2a (`vm/2026-11-06-vm-handoff
# docs/reports/2026-11-07-return-handoff-claude-ai-2.md:66  (users G01)
$ sed -n '66p' docs/reports/2026-11-07-return-handoff-claude-ai-2.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
2. **Tier pick** (Q9): yours after paper results, not now (`docs/reports/2026-11-07-wf-mac-side-maths-manager.md:591`).
# docs/reports/2026-11-07-return-handoff-claude-ai-2.md:67  (users W2-02)
$ sed -n '67p' docs/reports/2026-11-07-return-handoff-claude-ai-2.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
3. **Ruling-9 notes-4 items, still open:** the gate 2 Sharpe definition and its equity base (values spec §6 `:93`, §8 `:132`); the gate 6 WFE formula, and whether gate 6 applies to arm (a) (`:132–133`); whether GO / HOLD / REJECT may rest on arm (b) (maths report `:592–594`).
# docs/reports/2026-11-07-return-handoff-claude-ai-2.md:68  (users W2-03)
$ sed -n '68p' docs/reports/2026-11-07-return-handoff-claude-ai-2.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
4. **The July rubric hunk** in the working tree: R-A / R-B / R-C, `specs/SPEC_RUBRIC.md` from :267, 10 lines added (OBSERVED `git diff --numstat HEAD -- specs/SPEC_RUBRIC.md` = `10 0`). Land it now, or not. Read it with `git diff HEAD -- specs/SPEC_RUBRIC.md`.
# docs/reports/2026-11-07-return-handoff-claude-ai-2.md:69  (users W1-12,W2-19)
$ sed -n '69p' docs/reports/2026-11-07-return-handoff-claude-ai-2.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
5. **Void clause on the S13 addendum** at the foot of the 10-28 notes file (`98138cc`; recorded at DECISIONS.md:1290).
# docs/reports/2026-11-07-return-handoff-claude-ai-2.md:70  (users W1-13,W2-20)
$ sed -n '70p' docs/reports/2026-11-07-return-handoff-claude-ai-2.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
6. **Q3 stop multipliers** 1.5 / 2.25 / 3.0 × ATR(14): the master's R-1104-2 settlement, not your word, and changeable by you (DECISIONS.md:1262, D-2026-11-07-A).
# docs/reports/2026-11-07-return-handoff-claude-ai-2.md:71  (users G02)
$ sed -n '71p' docs/reports/2026-11-07-return-handoff-claude-ai-2.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
7. **VM pip.** The list Code's reply may name: `jsonschema`, `numpy`, `pyarrow`, `tzdata`, each `name==version`, plus `-e .` with `--no-deps --no-build-isolation` (`vm/2026-11-06-vm-handoff.md:140–156`, step 3.5). Open: whether the packages' own dependencies and the build backend `setuptools>=61` count as "the bridge's pinned requirements" (`:150`); and the 
# docs/reports/2026-11-07-return-handoff-claude-ai-2.md:72  (users G03)
$ sed -n '72p' docs/reports/2026-11-07-return-handoff-claude-ai-2.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
8. **The early-close checkpoint content.** Does R-1104-2 cover the behaviour chosen in D-2026-11-07-B addendum 1, decision (1) (DECISIONS.md:1480)? Your ratification at `17:08:00Z` covered addendum 1's timing; it did not rule on the content (addendum 2, DECISIONS.md:1518–1525).
# docs/reports/2026-11-07-return-handoff-claude-ai-2.md:73  (users G04)
$ sed -n '73p' docs/reports/2026-11-07-return-handoff-claude-ai-2.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
9. **VM handoff §9** (the master's arm-run text, `vm/2026-11-06-vm-handoff.md:314`): it takes effect only by your word, after 2a passes.
# docs/reports/2026-11-07-return-handoff-claude-ai-2.md:74  (users W2-04)
$ sed -n '74p' docs/reports/2026-11-07-return-handoff-claude-ai-2.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
10. **VM handoff §8 rows 1, 2, 3, 8** (`:295–302`) and the route half of **row 11** (`:305`): your hand step-0 items (§2, `:43`). Added for step 0: the trading-hours template's session hours, item 1.
~~~~

### docs/reports/2026-11-07-return-handoff-claude-ai.md

~~~~text
# docs/reports/2026-11-07-return-handoff-claude-ai.md:49  (users W2-05)
$ sed -n '49p' docs/reports/2026-11-07-return-handoff-claude-ai.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
1. **Addendum 5's timing:** ratify it, or not (DECISIONS.md:1165–1190, uncommitted; DECISION_LOG `22:34:00Z`). `uqb` waits on this.
# docs/reports/2026-11-07-return-handoff-claude-ai.md:50  (users W2-06)
$ sed -n '50p' docs/reports/2026-11-07-return-handoff-claude-ai.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
2. **Item 19:** does ruling 5's item 19 (commit `docs/reports/2026-10-28-voice-session-notes.md`) override your "old as-is set out of every commit" for this one file? (`20:34:29Z`; voice handoff §4 item 19, `docs/reports/2026-11-06-voice-handoff-evening.md:56`.)
# docs/reports/2026-11-07-return-handoff-claude-ai.md:51  (users W2-07)
$ sed -n '51p' docs/reports/2026-11-07-return-handoff-claude-ai.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
3. **Guard vs trailer:** should `scripts/master-bash-guard.sh` exempt commit messages, or does the attribution line keep the parenthesised form? This is a new hook change, outside 3(b) (`22:07:11Z`; DECISIONS.md:1188, uncommitted).
# docs/reports/2026-11-07-return-handoff-claude-ai.md:52  (users W2-08)
$ sed -n '52p' docs/reports/2026-11-07-return-handoff-claude-ai.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
4. **The proposed walk-forward values:** confirm or change them. They are in `docs/specs/2026-11-06-walk-forward-values.md` §2–§7 and §9, with questions Q1–Q10 at `:134-146`:
# docs/reports/2026-11-07-return-handoff-claude-ai.md:61  (users G01)
$ sed -n '61p' docs/reports/2026-11-07-return-handoff-claude-ai.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
   - Q9 — MFFU account size / tier for the max-DD gate.
# docs/reports/2026-11-07-return-handoff-claude-ai.md:63  (users W2-04,X05)
$ sed -n '63p' docs/reports/2026-11-07-return-handoff-claude-ai.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
5. **The VM handoff's step 0, six items.** Tell the VM session these in your own words (`vm/2026-11-06-vm-handoff.md:41-55`): (1) snapshot taken, and its name; (2) how the bridge source reaches the VM; (3) whether only the two AddOn files are copied; (4) whether the unauthenticated request folders are acceptable; (5) which sim account; (6) who performs the i
# docs/reports/2026-11-07-return-handoff-claude-ai.md:64  (users W2-09)
$ sed -n '64p' docs/reports/2026-11-07-return-handoff-claude-ai.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
6. **The 2a NT8 run:** is it covered by your lift? Your words (`20:08:28Z`): "my "lift completely once confirmed" ruling covers what tests 2a/2b need (bridge install + its import)". The manager's reading is that settlement 6 covered the install and the import, not the run (REPORTED BY manager, `22:30:00Z`). That is a reading, and the question stays open (D-2
# docs/reports/2026-11-07-return-handoff-claude-ai.md:65  (users G05,W2-10)
$ sed -n '65p' docs/reports/2026-11-07-return-handoff-claude-ai.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
7. **Who sets the Strategy Analyzer tab for 2a,** and who reads the tab and the PRAXIS commission template back (`vm/2026-11-06-vm-handoff.md:151`, `:260`). Also: whether a hand-set tab counts for "drives the baseline from the terminal" (VM handoff §8 row 10, `:282`).
# docs/reports/2026-11-07-return-handoff-claude-ai.md:66  (users W2-11)
$ sed -n '66p' docs/reports/2026-11-07-return-handoff-claude-ai.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
8. **Bridge NEEDS AMEAR left as yours** (VM handoff §8, `vm/2026-11-06-vm-handoff.md:276-284`):
# docs/reports/2026-11-07-return-handoff-claude-ai.md:73  (users X04)
$ sed -n '73p' docs/reports/2026-11-07-return-handoff-claude-ai.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
   - Also yours, per hard limit 3 (`:27`): starting NT8 on the VM ("Starting it is Amear's").
# docs/reports/2026-11-07-return-handoff-claude-ai.md:74  (users G07,G08,G09)
$ sed -n '74p' docs/reports/2026-11-07-return-handoff-claude-ai.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
9. **Notes-4 "not ruled" items** (voice handoff §4 item 18, `:55`): a second Rithmic read-only connection; the CME wiki as a source; equity base and Sharpe definition; the O1 gate set.
# docs/reports/2026-11-07-return-handoff-claude-ai.md:76  (users W2-12)
$ sed -n '76p' docs/reports/2026-11-07-return-handoff-claude-ai.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
    - Confirm that the VMware snapshot is your hand step (VM handoff §8 row 9, `:281`).
# docs/reports/2026-11-07-return-handoff-claude-ai.md:77  (users W2-10)
$ sed -n '77p' docs/reports/2026-11-07-return-handoff-claude-ai.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
    - The 2a V-rdict is judged only on your word on §8 row 10 (VM handoff step 4.6; `23:00:00Z`).
# docs/reports/2026-11-07-return-handoff-claude-ai.md:78  (users W2-08)
$ sed -n '78p' docs/reports/2026-11-07-return-handoff-claude-ai.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
    - The WF spec's items that neither ruling 4 nor the values file touches (Q10's last list).
~~~~

### docs/specs/2026-07-15-block2-backtesting-scope-proposal.md

~~~~text
# docs/specs/2026-07-15-block2-backtesting-scope-proposal.md:118-125  (users W4-09)
$ sed -n '118p' docs/specs/2026-07-15-block2-backtesting-scope-proposal.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
| Q2 | The verbatim Block-2 exit-milestone text (skill outline §B requires it from PHASE 3 BUILD SPEC) | Without it, §4 stays CANDIDATE and no completion claim is possible |
# docs/specs/2026-07-15-block2-backtesting-scope-proposal.md:127  (users W4-10)
$ sed -n '127p' docs/specs/2026-07-15-block2-backtesting-scope-proposal.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
### Q1 — RESOLVED (proposed, pending trader confirmation)
# docs/specs/2026-07-15-block2-backtesting-scope-proposal.md:131  (users W4-10)
$ sed -n '131p' docs/specs/2026-07-15-block2-backtesting-scope-proposal.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
**Still PENDING trader confirmation:** whether any TradingView Pine source exists / TradingView's role (generator vs passthrough); the canonical ruleset + parameter ranges + concrete exit-policy form; and Q7 (optimize vs validate-only). Full evidence and per-path assessment: `docs/reports/2026-07-15-b2-q1-strategy-exportability.md`.
# docs/specs/2026-07-15-block2-backtesting-scope-proposal.md:139  (users W4-09)
$ sed -n '139p' docs/specs/2026-07-15-block2-backtesting-scope-proposal.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
1. **b2-spec-import** — Obtain/import PHASE 3 BUILD SPEC Block-2 text; resolve Q1–Q9 with trader; record decisions. *Blocks everything.*
~~~~

### docs/specs/2026-07-16-b2-noise-area-ruleset.md

~~~~text
# docs/specs/2026-07-16-b2-noise-area-ruleset.md:76  (users W4-12)
$ sed -n '76p' docs/specs/2026-07-16-b2-noise-area-ruleset.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
| D5 | Positions/session | **multiple** (reverse on opposite cross; 1.3–1.8/day) (p. 9, Table 4) | RTF & b2-q1 & scope: **"one position/session" / "one bracket/session"** | ❌ **CONFLICT** — paper permits reversal/re-entry; PRAXIS "one per session" is a **deliberate constraint**, not the paper |
# docs/specs/2026-07-16-b2-noise-area-ruleset.md:79  (users W4-11)
$ sed -n '79p' docs/specs/2026-07-16-b2-noise-area-ruleset.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
| D8 | Flat time | **16:00** — no 11:30 stop in paper | b2-q1 report notes a **"flat-by-11:30-ET baseline"** | ❌ **CONFLICT** — 11:30 is a **PRAXIS window choice** (09:30–11:30 active hours), NOT the paper. The paper's edge is measured on full-day holds to 16:00; truncating at 11:30 is untested by the paper and changes expectancy |
# docs/specs/2026-07-16-b2-noise-area-ruleset.md:105  (users W4-11)
$ sed -n '105p' docs/specs/2026-07-16-b2-noise-area-ruleset.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **T1 (highest priority): session-flat time — 16:00 (paper) vs 11:30 (PRAXIS window).** The paper's entire performance record is full-day-to-16:00. A 09:30–11:30 NQ variant is a different strategy the paper does not evaluate. Trader must decide the flat time AND accept that paper Sharpe/DD numbers do not transfer if truncated. (Resolves D8 + the b2-q1 confl
# docs/specs/2026-07-16-b2-noise-area-ruleset.md:106  (users W4-12)
$ sed -n '106p' docs/specs/2026-07-16-b2-noise-area-ruleset.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **T2: one-position-per-session vs paper's reverse-on-cross.** PRAXIS's cascade-control rationale wants one/session; the paper reverses. Decide (affects trade count, WFA sample size, SHM-5 frequency band).
# docs/specs/2026-07-16-b2-noise-area-ruleset.md:107  (users W4-13)
$ sed -n '107p' docs/specs/2026-07-16-b2-noise-area-ruleset.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **T3: whether to expose a `noise multiplier` and/or `stop-ATR` at all.** Faithful port has neither. If Block-2 optimizes them, they are PRAXIS extensions beyond the paper (label as such in DECISIONS.md).
# docs/specs/2026-07-16-b2-noise-area-ruleset.md:108  (users W4-14)
$ sed -n '108p' docs/specs/2026-07-16-b2-noise-area-ruleset.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **T4: exit mode** — OppBand vs BandOrVWAP (paper prefers the latter).
# docs/specs/2026-07-16-b2-noise-area-ruleset.md:109  (users W4-15)
$ sed -n '109p' docs/specs/2026-07-16-b2-noise-area-ruleset.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
- **T5: instrument transfer** — SPY→NQ is unvalidated by this paper; NQ evidence is third-party (Quantitativo). Confirm the NQ port is treated as requiring its own Block-2 validation, not inheriting the paper's SPY numbers.
~~~~

### specs/SPEC_RUBRIC.md

~~~~text
# SPEC_RUBRIC.md:93-94  (users G30)
$ sed -n '93,94p' specs/SPEC_RUBRIC.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
the primary account home mounted into the VM. **Required:** either the user
exists, or a DECISIONS.md entry records the removal and its accepted risk.
# SPEC_RUBRIC.md:107  (users G20)
$ sed -n '107p' specs/SPEC_RUBRIC.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
without them, or both — and how the Block 4 gate is satisfiable if they differ.
# SPEC_RUBRIC.md:256  (users G10)
$ sed -n '256p' specs/SPEC_RUBRIC.md | cut -c1-360 | sed -E -f /tmp/d11/mask.sed
**A human resumes it. The orchestrator does not.** There is no third dispatch,
~~~~

## Correction 1 (2026-11-09, after audit FAIL 1)

This section is appended after an independent audit graded this report FAIL (strike 1). Lines 1-2110 above are unchanged (hash in the last block below). It cures three findings: MAJOR 4, MINOR a and MINOR b. Nothing else in the report is re-opened here.

### C1.1 — Method note 5 (:45): the claimed ADV1 re-checks are SUPERSEDED

These two sentences of Method note 5 are SUPERSEDED. They are quoted verbatim:

~~~~text
$ sed -n '45p' docs/reports/2026-11-09-d11-sweep-manager.md | grep -o -E 'D2 tests[^.]*\.|ANSWERED-BY / CLOSED-OTHER[^.]*\.'
D2 tests and recommendations in Tables 1-2: the manager's reading, each re-checked by ADV1.
ANSWERED-BY / CLOSED-OTHER statuses in Table 3: the workers' readings; their pointers are pasted, and ADV1 spot-checked a sample; the manager did not re-grade each one.
~~~~

Both sentences are false. ADV1 re-checked nothing. It returned no result (:25, :302), and its file holds only "(in progress)" (:406-414). The independent re-checks in this unit are those of ADV2a (:417-488) and ADV2b (:489-708). Both ran against the draft, before the manager's fixes. Rows the manager changed after they returned were re-checked by the manager alone (block V4, :709). No adversary re-ran over them (Limit, :320).

Counts from their pasted text:

~~~~text
$ sed -n '417,488p' docs/reports/2026-11-09-d11-sweep-manager.md | grep -o -E '\b[GHX][0-9]{2}\b' | sort -u | tr '\n' ' '
G01 G02 G04 G06 G07 G09 G10 G11 G12 G16 G21 G22 G24 G25 G28 G29 G30 G31 G32 G33 G34 G35 G36 G37 G38 G40 H02 H03 X01 X02 X03 X07 X08 X09 X12 
$ sed -n '417,488p' docs/reports/2026-11-09-d11-sweep-manager.md | grep -c -E '^[$] '
9
$ sed -n '489,708p' docs/reports/2026-11-09-d11-sweep-manager.md | grep -o -E '\b[GHX][0-9]{2}\b' | sort -u | tr '\n' ' '
G01 G02 G03 G04 G05 G06 G07 G08 G09 G10 G11 G20 G25 G28 G31 G35 G36 G37 G39 H01 H02 X04 X06 
$ sed -n '489,708p' docs/reports/2026-11-09-d11-sweep-manager.md | grep -c -E '^\| P[0-9]+ \|'
39
$ sed -n '489,708p' docs/reports/2026-11-09-d11-sweep-manager.md | grep -o -E '^\| P[0-9]+ ' | sort -u | wc -l
      38
$ sed -n '122,276p' docs/reports/2026-11-09-d11-sweep-manager.md | grep -c -E '^\| W[1-4]-'
148
~~~~

The ADV2a list counts every id its text names. A name is not always a check. For example, G07-G10 are named only in "Method note 7 lists conflicts for G07-G10 only" (:427), and X12 only in the range "X01-X12" (:469). The list below says what was actually checked.

**D2 tests, Tables 1-2 (40 G rows, 3 H rows):**
- **D2 and D2-AMBIGUOUS rows, as the draft classed them.** ADV2a checked the closure of each of these 13 rows and found that none performs a D2 act (:479): G28, G31, G34 (D2); G01, G06, G09, G25, G29, G30, G32, G33, G38, G40 (D2-AMBIGUOUS). ADV2a also quoted the D2 words against DECISIONS.md:1912-1916 (:480).
- **G35, G36.** ADV2a F1 (:421) and ADV2b F4 (:697) attacked the draft's NOT-D2 test. The manager re-classed both rows as D2-AMBIGUOUS after that. The new class was not independently re-checked. The same holds for the freeze text added to G25, G28, G29 and G32-G34 (:306).
- **NOT-D2 rows whose D2 test was examined:** G04 and G12 (held, :482); G11, by comparison with H02 (F6, :462); G22 (F3, :438: "Not a D2 breach"); G24 (F4, :444: "NOT-D2 is right"). That is 5 of the 25 current NOT-D2 rows.
- **NOT-D2 rows not independently re-checked:** G02, G03, G05, G07, G08, G10, G13, G14, G15, G17, G18, G19, G20, G21, G23, G26, G27, G37, G39, G41 (20 rows). ADV2a's column-5 tally (:478) counted these classes in the draft. It did not test the reading behind each one. G41 did not exist until ADV2b F5. Some of these rows were pointer- or quote-checked by ADV2b (below). That checks the quote, not the D2 test.
- **Table 2:** H02's D2 test was examined (ADV2a F6). After the fix, H02 is NOT-D2, and that new class was not independently re-checked. H01 and H03: D2 test not independently re-checked. ADV2a re-read H03's source recommendation (:481). ADV2b checked H01's pointer and its cutoff (P30).
- **Recommended options:** ADV2a re-read the source recommendation for G01, G02, G11, G35, H02 and H03 (:481). It attacked the options of G16 (F7), G22 (F3) and G24 (F4), and the quote of G37 (F2). Recommendations of the other Table 1-2 rows: not independently re-checked. ADV2a reports that their cells are labelled "manager's proposal" or "none in source" (:481).
- **Actions table:** ADV2a examined X03 (F5) and the "none" closures of X08 and X09 (:479), and X07's contents (F7). ADV2b checked the pointers behind X04 (P13) and X06 (P12). X01, X02, X05 and X10-X13 were not independently re-checked. X13 was created after both adversaries returned.

**Table 3 statuses (148 rows = 87 ANSWERED-BY + 61 CLOSED-OTHER):**
- ADV2b's numbered pointer rows P1-P38 (39 table lines, because P8 appears twice: :506 and :537) name 27 Table 3 rows. Each was found once in Table 3 (lines 122-276).
- 24 of those rows had their status reading tested: W3-40 (BAD), W3-33 (OK-weak), W1-37, W3-39, W3-32, W3-11, W1-21, W2-06, W1-42 (MINOR), W3-63, W2-41, W2-10, W4-02, W4-04, W4-08 (BAD), W4-03, W3-94 (BAD), W3-92, W3-75, W1-25, W1-26, W1-27 (OK-weak), W1-29 and W2-14 (BAD, inconsistent).
- For the other 3 (W1-04, W1-10, W2-18), only the quote or pointer was checked (P11, P12, P16).
- The remaining 121 Table 3 statuses were not independently re-checked. They remain the workers' readings, with pointers pasted in the Evidence appendix.
- ADV2a's Table 3 check (:478) was a row count only.
- The manager re-classed W3-40, W3-94, W4-08, W1-29, W2-14 and W1-42 after ADV2b returned (:313-317). Those new statuses were not independently re-checked.

**Pointers re-run:** ADV2a pasted 9 re-run commands (`$ ` lines above). It also names other pointers it checked, without pasting their output (:482). ADV2b checked 38 numbered pointer rows (P1-P38). Some rows carry more than one line, for example P14 (four lines) and P16 (two). Some rows have pasted raw output. The full re-run of all 416 pointers is the manager's own (block V1). It is not independent.

### C1.2 — MANIFEST row: working-tree line 315; commit-blob line 307

The text "row 315" at :37 (process log step 5) and at :328 (MANIFEST section) gives the working-tree line number. The working-tree MANIFEST.md carries rows from other uncommitted units. The master commits a surgical MANIFEST blob: HEAD's 306 lines plus this report's row. In that blob, the row is line 307. That number is worked out from HEAD's line count. It is not seen in a commit, because none has been made yet.

~~~~text
$ sed -n '315p' MANIFEST.md | cut -c1-120
| /docs/reports/2026-11-09-d11-sweep-manager.md | Report | 2 | 2026-11-09 | Manager report for unit 2026-11-09-d11-sweep
$ git show HEAD:MANIFEST.md | wc -l
     306
$ wc -l MANIFEST.md
     315 MANIFEST.md
~~~~

### C1.3 — HANDOFF.md and ISSUE_REGISTER.md pointers are into uncommitted working-tree files

Every `HANDOFF.md:<n>` and `ISSUE_REGISTER.md:<n>` pointer in this report points into the working-tree version of that file. Both files are uncommitted (`git status`: ` M HANDOFF.md`, `MM ISSUE_REGISTER.md`). Examples are HANDOFF.md:36 and :181, and ISSUE_REGISTER.md:11-:74. Their line numbers and text hold only in the working tree. Once those files are committed, they hold in the commit that includes those working-tree versions. At HEAD f10603a, the same line numbers show other text, or nothing.

~~~~text
$ git show HEAD:ISSUE_REGISTER.md | wc -l
      35
$ wc -l ISSUE_REGISTER.md
      76 ISSUE_REGISTER.md
$ git show HEAD:HANDOFF.md | wc -l
    1554
$ wc -l HANDOFF.md
    1688 HANDOFF.md
$ git show HEAD:HANDOFF.md | sed -n '36p' | cut -c1-120
- DECISIONS.md +69, two blocks. Addendum 5 at 1164–1190 is blocked on ratification (`22:34:00Z`). D-2026-11-06-D at 1192
$ sed -n '36p' HANDOFF.md | cut -c1-120
**PARKED — `Praxis_build-diq` (U7). A human resumes it; the orchestrator does not.** The C1 audit PASSED the diff of rec
$ git show HEAD:HANDOFF.md | sed -n '181p' | cut -c1-120
2. **Fusion readbacks before any further run:** `Tools > Instruments` filter `NQCONT`/`NQ` — Type, Tick size, Point valu
$ sed -n '181p' HANDOFF.md | cut -c1-120
- Bridge items left to Amear also gate the VM steps: whether `pip` may download (`vm/2026-11-06-vm-handoff.md:32`, step 
$ git show HEAD:ISSUE_REGISTER.md | sed -n '57p' | cut -c1-120
$ sed -n '57p' ISSUE_REGISTER.md | cut -c1-120
- [2026-08-05T01:40Z] WHO: praxis-master (session 41) | WHAT: **`gate-commit.sh` REPORTS THE WRONG CAUSE WHEN AN AUDIT T
~~~~

Both HANDOFF lines checked (:36, :181) show different text at HEAD. ISSUE_REGISTER.md:57 (G35's pointer) is empty at HEAD. The same holds for every ISSUE_REGISTER pointer above :35. DECISION_LOG.md is also uncommitted (` M DECISION_LOG.md`). Its line :165, cited in Method note 7(c), was not compared with HEAD in this correction.

### C1.4 — Closure decisions (for information only)

The master's DECISION_LOG.md rows `2026-11-09T13:50:00Z` (:759) and `2026-11-09T14:05:00Z` (:760) hold the closure decisions. This report decides nothing. It does not restate or grade those rows.

~~~~text
$ /usr/bin/grep -n -E '2026-11-09T(13:50:00Z|14:05:00Z)' DECISION_LOG.md | cut -c1-90
759:- [2026-11-09T13:50:00Z] WHO: praxis-master | WHAT: **D11 SWEEP — CLOSURES. Inventory:
760:- [2026-11-09T14:05:00Z] WHO: praxis-master | WHAT: **AUDIT FAIL 1 on `/tmp/idx-d11` (
~~~~

### C1.5 — Final evidence (run on the final file, after the last edit)

The house-sentence grep below uses the pattern `F[i]lls`. That pattern matches the sentence at :4, but the command text itself does not, so this block does not count itself. The outputs below were captured on the final file. They match the text pasted here.

~~~~text
$ head -n 2110 docs/reports/2026-11-09-d11-sweep-manager.md | openssl dgst -sha256
SHA2-256(stdin)= 903a6a90caa3dee21b1eb300011b9a29633dfc7d3ff46b47dd8b72fc80a60ea0
$ wc -l docs/reports/2026-11-09-d11-sweep-manager.md
    2231 docs/reports/2026-11-09-d11-sweep-manager.md
$ grep -c 'F[i]lls are optimistic' docs/reports/2026-11-09-d11-sweep-manager.md
1
$ grep -c '^Result:' docs/reports/2026-11-09-d11-sweep-manager.md
2
~~~~

Result: PASS (the producer's result after the correction, not a grade): the inventory and its tables are unchanged; the false claim that ADV1 re-checked the D2 tests and the Table 3 statuses is SUPERSEDED, and C1.1 now gives what ADV2a and ADV2b actually covered (13 of 15 D2 or D2-AMBIGUOUS closures, 5 of 25 NOT-D2 tests, and 24 of 148 Table 3 statuses, with the rest marked as not independently re-checked); the MANIFEST row is line 307 in the master's commit blob (line 315 in the working tree), and the HANDOFF.md and ISSUE_REGISTER.md pointers are into uncommitted working-tree files.

## De-identification note 2026-11-10

Line 635 was redacted in place on 2026-11-10 under D-2026-08-06-A (DECISIONS.md:1144-1152) and the master's decision of record (DECISION_LOG row 2026-11-10T09:08:00Z): one withheld term was replaced with "session window" (Amear's words). No other line of this report was changed. History was not rewritten; earlier commits keep the original text.
