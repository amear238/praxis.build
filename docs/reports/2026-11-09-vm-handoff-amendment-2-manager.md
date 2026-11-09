# Unit `2026-11-09-vm-handoff-amendment-2` — manager report

Written by praxis-manager, 2026-11-09. Repo HEAD `cec36b8` (= origin/main). Nothing staged, nothing committed (master's brief: leave every change UNSTAGED).

Standing limitation: Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## Task

Amendment 2 of `vm/2026-11-06-vm-handoff.md` under Amear's C3, C9, C10 (D-2026-11-08-C) and R1 (D-2026-11-08-A); one go-live line appended to `docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md` (C3 (4)); three MANIFEST rows appended. Brief: master's dispatch of this unit (after the 17:29Z dispatch died with nothing on disk).

## Rubric criteria addressed

S1, S2, S4, S5, S6, S8, S13 (`specs/SPEC_RUBRIC.md` standing criteria table, lines 119–133; Autonomy section :386–416 read with S8).

## Workers dispatched

| id | mode | scope | outcome |
|---|---|---|---|
| W1 `aa73c5e34a67dcbbb` | ADVERSARIAL, foreground, read-only | the diff of both files + the whole amended handoff against the C3/C9/C10/R1 words and criteria (a)–(h); given the artifact and the criteria, not my reasoning | `VERDICT: REFUTED` — 1 MAJOR, 9 MINOR. Dispositions below. |
| W2 `ac0b020a456c72497` | ADVERSARIAL, foreground, read-only | re-check of W1's defects against the cured tree, plus new contradictions and pointer checks | `VERDICT: SURVIVES` — all W1 defects listed cured; 6 new MINOR. Dispositions below. |

No BUILD worker. The edits are documentation edits (no production code); the manager made them directly, by exact-string replacement scripts (`python3 -I`, each replacement asserted to match exactly once). This is the manager's choice, recorded here; it departs from the manager role's dispatch-a-builder default.

## Process log

1. 18:12:16Z — read state: HEAD `cec36b8`; handoff 351 lines, walkthrough 38, MANIFEST 316; this report absent (`ls docs/reports/2026-11-09*` listed six other files). Before-evidence captured (pasted below).
2. Read: the handoff in full; `specs/SPEC_RUBRIC.md` :117–250 and :386–416; DECISIONS.md :1534–1555, :1612–1625, :1800–1870, :1980–1984; the answers file :1–60; DECISION_LOG rows :718 and :743 (both also in HEAD); the NT8 windows reference :32, :140–160, :205–216; the rescued template at `29c3e13`.
3. Report skeleton written (tool use ~13).
4. Handoff edits, in order: §0 Amendment 2 line (:22); limit 1 (:28); §2 new block (:46–74) and old §2 body struck (:76–88); step 1 opening line (:94) and new item 0 (:96–110); item 6 (:116); item 9 (:119); step 3 gate (:138); 3.1 (:150); 3.3 (:171, :173–174, :176); 3.4 (:184–185); §8 new list (:358–365).
5. Walkthrough line appended (:39). MANIFEST rows appended (:317–319); `head -n 316 MANIFEST.md | openssl dgst -sha256` equal to the before value.
6. W1 dispatched → REFUTED. Fixes applied for F1, F4–F10 (including §9.5, :406). F2, F3 left (reasons below).
7. W2 dispatched → SURVIVES. Fixes applied for N1, N2, N4, N5 (second half), N6. N3 and N5 (first half) left (reasons below).
8. MANIFEST row :317 wording corrected to match the final place list (my own appended row; :1–316 untouched; hash re-checked).
9. Final evidence captured after the last edit to any of the three files (below). The report's own `grep -c` is taken last (observer note in the evidence section).

## Lines changed in `vm/2026-11-06-vm-handoff.md` (HEAD line → working-tree line)

Before/after text for every line is in the full diff pasted under Verification evidence. Index:

| HEAD | Now | What |
|---|---|---|
| — | 22 | New §0 bullet "Amendment 2 (2026-11-09)": C3, C9, C10, R1, unit name, HEAD `cec36b8`, places amended. |
| 27 | 28 | Limit 1: old account-wait text struck; "Amendment 2: item 5 is answered … "(5) Sim101;" (C3)". |
| — | 46–74 | §2: C10 quoted; C3, C9, C10 verbatim block; six-item answer table; grades (snapshot REPORTED BY Amear, not observed by Code); item 4's condition and the "sim tests" reading labelled INFERRED; what the answers leave open; then "Superseded by Amendment 2 — kept for the record; do not act on it:". |
| 45, 47–56 | 76, 78–88 | Old §2 body (snapshot hand step; "tell the VM session, in your own words, six things"; items 1–6; "Step 3 does not start until items 1–6 are answered in your words.") kept, struck through. |
| 62 | 94 | Step 1 opening line: one exception — item 0 opens the Trading Hours window, read-only. |
| — | 96–110 | New step 1 item 0, the R1 read: R1 quoted in a fenced block; read-only; NT8 must already be running, else STOP; route Tools → Trading Hours sourced to the reference doc :32, :156 and marked UNVERIFIED on this VM; exact template name; copy the time-zone field and every session row; do not judge; Code decides whether the 08:30 clause fired; row 7 unchanged. |
| 69 | 116 | Item 6: "It is the only NT8 window step 1 opens." struck; replaced to include item 0's window. |
| 72 | 119 | Item 9: "Paste them word for word" struck; now copy the six answers from §2 and say they were read from the file. |
| 91 | 138 | Step 3 gate (b), (c): old text struck; (b) Code writes `SNAPSHOT: confirmed` from C9, REPORTED BY Amear, meaning not observed; (c) answers filed in §2; item 4's condition and its labelled reading. |
| 103 | 150 | 3.1: "Run it only if Amear's step-0 words chose it…" struck; "he chose it — "(2) anonymous HTTPS clone, step 3.1;"". |
| 124 | 171 | 3.3 heading and "This file assumes neither path." struck; item 6's answer quoted. |
| 126–127 | 173–174 | 3.3's "drive NT8's window" and "not clearly named" paths struck, marked superseded. |
| 129 | 176 | 3.3 reply line struck; new reply line ("Compile by: Amear"). |
| 137–138 | 184–185 | 3.4: "Whether that is acceptable is Amear's question" and "stays section 2, item 4" struck; C3 (4) quoted; "restates" labelled the master's reading, with the wording difference. |
| — | 358–365 | §8: new "Settled since 2026-11-08 (Amendment 2)" list for rows 1, 2, 3, 8, 9 and row 11's route half; the rows themselves not edited. |
| 351 | 406 | §9.5: "stay **Amear's**" and ", nor the account" struck; now answered (C3). Inside §9; changed because it contradicted §2 (W1 F1, MAJOR); the only §9 line changed. |

Not edited, on purpose: :7 (the date line naming amendment 1), and the Amendment 2 line sits at :22 (end of the §0 authority list), not beside amendment 1 at :11. Reason: an edit at :7–:12 puts the handoff's :9 standing-limitation line into the context of the pasted diff, and this report must carry that sentence exactly once (S13; brief). The :22 line carries the date and HEAD. Also not edited: :21 (amendment 1's authority line, historical), :209 (step 4 gate), :320 and :329 (§7 items 5 and 14), :385 (§9.2), and `vm/skills/praxis-nt8-bridge-backtest/SKILL.md`:13 — see S6.

## Verification evidence (pasted output only)

### Before the first edit (captured 18:12:16Z)

````
---BEFORE
2026-11-09T18:12:16Z
     351 vm/2026-11-06-vm-handoff.md
      38 docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md
     316 MANIFEST.md
     705 total
SHA2-256(stdin)= a2c1afdc8f4655388e3a49227713b48c564da7c909f945ff706048b342c41042
````

The same capture printed `git diff HEAD -- MANIFEST.md | tail -n 20 | cut -c1-200` (the parked diq rows :307–314 and HEAD's :307–308 as context; no rows of this unit) and ` M MANIFEST.md` as the only porcelain line of the three paths (the handoff and the walkthrough were clean). That `tail` output was cut to 200 columns and is not re-pasted here; the final capture below repeats the same command uncut. The report did not exist then: `ls docs/reports/2026-11-09*` listed `2026-11-09-c-d-filing-manager.md`, `2026-11-09-c-d-filing-resume-manager.md`, `2026-11-09-d11-sweep-manager.md`, `2026-11-09-d6-drawdown-check-manager.md`, `2026-11-09-rubric-unit-manager.md`, `2026-11-09-wf-spec-amendment-resume-manager.md`.

### After the last edit — final state

An earlier after-edit capture (taken before the MANIFEST row :317 wording fix, process step 8) is SUPERSEDED and not pasted. The block below is the only after-edit capture of record. It was taken after the last edit to the handoff, the walkthrough and MANIFEST.md; none of the three changed after it. Inserted by script from the capture file, not retyped.

````
$ date -u +%FT%TZ
2026-11-09T18:25:41Z
$ git diff HEAD -- vm/2026-11-06-vm-handoff.md docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md
diff --git a/docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md b/docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md
index 4d7c619..907a9c3 100644
--- a/docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md
+++ b/docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md
@@ -36,3 +36,4 @@ Caution (VMware): never open one file from both sides at once; a write can corru
 - **The Steps above are moot:** Fusion shows no Sharing pane (D-2026-11-06-A item 3, "no Sharing pane, as flagged", REPORTED BY amear).
 - Source: D-2026-11-06-B, ruling 5 settlements table, item 1 and item 10.
 - [ ] **Go-live checklist addendum 2026-11-07, his words (ruling 10):** "remove the unauthenticated bridge request folders (or add auth) before real money" (verbatim at `docs/reports/2026-11-07-amear-rulings-morning.md`:29; ledger DECISION_LOG 2026-11-07T12:55:00Z, WHO: amear; D-2026-11-07-A). His second item, "unmap Z: and turn off the SMB share", is already covered at :35; not duplicated.
+- [ ] **Go-live checklist addendum 2026-11-09, his words (C3 (4)):** "(4) unauthenticated request folders acceptable for sim tests only, closed before real money (go-live list);" (verbatim, lines joined, at `docs/reports/2026-11-08-amear-answers-park-card.md`:24–26; D-2026-11-08-C, DECISIONS.md:1831–1833; ledger DECISION_LOG 2026-11-08T19:12:30Z, WHO: amear; REPORTED BY the Claude.ai channel and pasted by Amear, answers file :3). C3 (4) restates the 2026-11-07 line at :38 (master's reading, changeable by Amear) (ruling 10: "remove the unauthenticated bridge request folders (or add auth) before real money"); the wordings differ ("closed" here; "remove … (or add auth)" at :38) and both bind before real money. The :38 line stands, unedited. Appended by unit 2026-11-09-vm-handoff-amendment-2; nothing above edited.
diff --git a/vm/2026-11-06-vm-handoff.md b/vm/2026-11-06-vm-handoff.md
index 5ff9357..13c2606 100644
--- a/vm/2026-11-06-vm-handoff.md
+++ b/vm/2026-11-06-vm-handoff.md
@@ -19,12 +19,13 @@
 - Amear, D-2026-11-06-B ruling 1 (DECISIONS.md:1063): "the VM agent installs cli-nt-bridge via terminal, after a VMware snapshot."
 - Amear's ruling-5 defaults (DECISIONS.md:1063): "test 2a reference = 1,190 trades / $197,327.60 on NQCONTROW SEP25, exact match; my "lift completely once confirmed" ruling covers what tests 2a/2b need (bridge install + its import), D-071 untouched; VM agent reads and reports the NT8 version; Code + auditor judge 2a/2b and log the lift under my ruling; VM agent on Z: while Code runs = second session, coordinate."
 - Amear, D-2026-11-07-A rulings 5–8 and 10 (DECISIONS.md:1229–1234; ledger DECISION_LOG `2026-11-07T12:55:00Z`, WHO: amear), quoted where applied: section 1 limits 4, 6, 8; section 2; steps 3.4, 3.5, 4.2, 4.3, 4.6; section 8.
+- **Amendment 2 (2026-11-09):** applies D-2026-11-08-C C3, C9 and C10 (DECISIONS.md:1830–1850; ledger DECISION_LOG `2026-11-08T19:12:30Z`, WHO: amear) and D-2026-11-08-A R1 (DECISIONS.md:1551–1555; ledger DECISION_LOG `2026-11-08T14:02:11Z`, WHO: amear); unit `2026-11-09-vm-handoff-amendment-2`, repo HEAD `cec36b8`. Writes Amear's filed step-0 answers into section 2 (C10); adds the R1 trading-hours read as step 1 item 0; brings section 1 limit 1, step 1's opening line and items 6 and 9, the step 3 gate, steps 3.1, 3.3 and 3.4, section 8 and §9.5 into line; appends C3 (4) to the go-live list of `docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md`. Superseded text is kept, struck through. Lines that say "Amear's step-0 words" and were not edited (step 4 gate; section 7 items 5 and 14; the step-4 skill) now read those words from section 2.
 
 ## 1. Hard limits for the VM agent
 
 Every limit holds for the whole of this file. If a step seems to need breaking one, STOP and write a reply saying which limit and why.
 
-1. **Account:** Sim101 only, or the sim account Amear names. No live account, ever. No step runs until item 5 is answered (section 2), except steps 1 and 2, which touch no account: steps 3 and 4 wait on Amear's words naming the account. Which account the tests use is still Amear's question (bridge NEEDS AMEAR 8, `report:232`).
+1. **Account:** Sim101 only, or the sim account Amear names. No live account, ever. ~~No step runs until item 5 is answered (section 2), except steps 1 and 2, which touch no account: steps 3 and 4 wait on Amear's words naming the account. Which account the tests use is still Amear's question (bridge NEEDS AMEAR 8, `report:232`).~~ **Amendment 2:** item 5 is answered in section 2 — Amear: "(5) Sim101;" (C3, D-2026-11-08-C). The account is Sim101.
 2. **No orders.** Place, change, cancel or flatten nothing.
 3. **No connection changes (D-071).** No new NT8 connection, no reconnect, no disconnect. Amear: "D-071 untouched" (DECISIONS.md:1063); "Hard limits unchanged: nothing bought, no new data connection, F1–F4 untouched, borrowed code on its own branch, old as-is set out of every commit." (DECISIONS.md:1063). Why it matters here: `reconnect`, `playbackrun` and AutoReconnect all call `Connection.Connect`, and `playbackrun`, on its baseline stage when `require` is playback, disconnects every non-Playback connection (`report:184`; the D-071 consequence is INFERRED, `report:188`). **Do not start, close or restart NinjaTrader.** Starting it may bring connections up; whether it does on this VM is UNVERIFIED. If a step needs NT8 running and it is not, STOP and reply. Starting it is Amear's.
 4. **Bridge commands you must not use.** Amear: "(4) playbackrun/reconnect/flatten/strategies/ghostorders/AutoReconnect stay forbidden until live-trading design says otherwise." (DECISIONS.md:1231, D-2026-11-07-A ruling 7(4)). `flatten` has no Sim-only check (`report:178`). This file's own limit for these steps, not his words: the only bridge commands it permits are `backtest` and `ntstatus` (step 4). Not `doctor`, `deploy`, `compile`, `reload`, `restart`, `watchdog`, `configure`, `satemplate`, `analyzerrun`, or any other.
@@ -42,34 +43,80 @@ Every limit holds for the whole of this file. If a step seems to need breaking o
 
 ## 2. Hand step 0 — Amear, on the Mac
 
-Before the VM agent does anything below, take a VMware Fusion snapshot of the VM. Source: ruling 1, "after a VMware snapshot" (DECISIONS.md:1063); R-VN4-13, "Yeah, just do the snapshot." (DECISIONS.md:960). Whose hand, in your words: "Snapshot is my hand step: confirmed." (DECISIONS.md:1232, D-2026-11-07-A ruling 8).
+**Amendment 2 (2026-11-09) — step 0 is answered. Read the answers here; Amear does not repeat them to you.** His words (C10, D-2026-11-08-C): "Code writes the filed step-0 answers into vm/2026-11-06-vm-handoff.md §2 so the VM session reads them from the file. Amear does not repeat them to the VM session." Do not wait for Amear to tell you items 1–6, and do not ask him for them.
+
+Amear's answers, verbatim (WHO: amear; REPORTED BY the Claude.ai channel and pasted by Amear, per the answers file's :3). Source: `docs/reports/2026-11-08-amear-answers-park-card.md` lines 23–27 (C3), 39–40 (C9) and 41–43 (C10), filed in D-2026-11-08-C (DECISIONS.md:1830–1834, :1846–1850); ledger DECISION_LOG `2026-11-08T19:12:30Z`, WHO: amear. His approval line in the same paste (:14): "Sending this message is my approval of C1-C10 as written."
+```text
+C3  Step 0, items 2-6: (2) anonymous HTTPS clone, step 3.1;
+    (3) only the two AddOn files of step 3.2; (4) unauthenticated
+    request folders acceptable for sim tests only, closed before real
+    money (go-live list); (5) Sim101; (6) Amear presses Compile in the
+    NinjaScript Editor by hand.
+C9  Step 0, item 1: snapshot taken, named pre-cli-nt-bridge-2026-11-06.
+    The Claude session on the VM is closed.
+C10 Code writes the filed step-0 answers into vm/2026-11-06-vm-handoff.md
+    §2 so the VM session reads them from the file. Amear does not repeat
+    them to the VM session.
+```
 
-- [ ] Fusion → select the VM → Snapshots → Take Snapshot. Name: `pre-cli-nt-bridge-2026-11-06`. (Menu path not checked by Code; use Fusion's own snapshot command if it differs.)
-- **You should see:** the snapshot listed in the VM's Snapshots window with that name and today's date.
-- Then tell the VM session, in your own words, six things. The VM agent pastes what you say, word for word, into its first reply, and Code files it as yours:
-  1. the snapshot is taken, and its name;
-  2. how the bridge source reaches the VM: the anonymous HTTPS clone in step 3.1 (the master's proposal, DECISION_LOG `2026-11-06T22:11:54Z`), the README's SSH clone, or a copy through Z: (bridge NEEDS AMEAR 11, `report:235`);
-  3. whether the install copies only the two AddOn files of step 3.2 (bridge NEEDS AMEAR 1, `report:225`);
-  4. whether the unauthenticated request folders the install creates are acceptable for these tests (bridge NEEDS AMEAR 3, `report:227`);
-  5. which sim account (bridge NEEDS AMEAR 8, `report:232`);
-  6. who performs the one in-NT8 compile (NinjaScript Editor → F5) — Amear by hand, or the VM agent driving NT8's window? The first compile is a step inside NT8, not a terminal command (`README.md:54@9664d9b`: "In NinjaTrader, open the NinjaScript Editor and **compile (F5)**"; `report:31`: "Installing means copying C# into `bin\Custom\AddOns` and compiling it in NT8"; `report:140`). Ruling 1 settles the terminal install and its order; it does not say whose hand presses F5.
-- Anything you leave out, the VM agent does not assume. Step 3 does not start until items 1–6 are answered in your words.
+| Item | The question (as asked 2026-11-06, struck below) | Amear's answer, his words | Where it applies |
+|---|---|---|---|
+| 1 | the snapshot is taken, and its name | "snapshot taken, named pre-cli-nt-bridge-2026-11-06." (C9) | Step 3 gate (b) |
+| 2 | how the bridge source reaches the VM | "(2) anonymous HTTPS clone, step 3.1;" (C3) | Step 3.1 |
+| 3 | whether the install copies only the two AddOn files | "(3) only the two AddOn files of step 3.2;" (C3) | Step 3.2 |
+| 4 | whether the unauthenticated request folders are acceptable | "(4) unauthenticated request folders acceptable for sim tests only, closed before real money (go-live list);" (C3) | Step 3.4; go-live list |
+| 5 | which sim account | "(5) Sim101;" (C3) | Limit 1; step 4 gate |
+| 6 | who performs the one in-NT8 compile | "(6) Amear presses Compile in the NinjaScript Editor by hand." (C3) | Step 3.3 |
+
+- **Grades.** The snapshot is REPORTED BY Amear (C9). Code has not seen it: no Fusion window and no snapshot list has been observed by Code. "The Claude session on the VM is closed." is REPORTED BY Amear (C9), as of his answer (2026-11-08).
+- **Item 4's condition.** His answer is "acceptable for sim tests only". That tests 2b and 2a are "sim tests" in his words is INFERRED (this file's reading, not his word; changeable by him): they run under limit 1 (Sim101 only; his item 5) and place no orders (limit 2). Which account NT8 uses inside a Strategy Analyzer backtest is UNVERIFIED. "closed before real money (go-live list)" is on the go-live list (step 3.4).
+- **What his answers do not say** stays open and is not filled in here: when, and by what message, Amear tells you he has compiled (step 3.3 waits for him).
+
+**Superseded by Amendment 2 — kept for the record; do not act on it:**
+
+~~Before the VM agent does anything below, take a VMware Fusion snapshot of the VM. Source: ruling 1, "after a VMware snapshot" (DECISIONS.md:1063); R-VN4-13, "Yeah, just do the snapshot." (DECISIONS.md:960). Whose hand, in your words: "Snapshot is my hand step: confirmed." (DECISIONS.md:1232, D-2026-11-07-A ruling 8).~~
+
+- ~~[ ] Fusion → select the VM → Snapshots → Take Snapshot. Name: `pre-cli-nt-bridge-2026-11-06`. (Menu path not checked by Code; use Fusion's own snapshot command if it differs.)~~
+- ~~**You should see:** the snapshot listed in the VM's Snapshots window with that name and today's date.~~
+- ~~Then tell the VM session, in your own words, six things. The VM agent pastes what you say, word for word, into its first reply, and Code files it as yours:~~
+  1. ~~the snapshot is taken, and its name;~~
+  2. ~~how the bridge source reaches the VM: the anonymous HTTPS clone in step 3.1 (the master's proposal, DECISION_LOG `2026-11-06T22:11:54Z`), the README's SSH clone, or a copy through Z: (bridge NEEDS AMEAR 11, `report:235`);~~
+  3. ~~whether the install copies only the two AddOn files of step 3.2 (bridge NEEDS AMEAR 1, `report:225`);~~
+  4. ~~whether the unauthenticated request folders the install creates are acceptable for these tests (bridge NEEDS AMEAR 3, `report:227`);~~
+  5. ~~which sim account (bridge NEEDS AMEAR 8, `report:232`);~~
+  6. ~~who performs the one in-NT8 compile (NinjaScript Editor → F5) — Amear by hand, or the VM agent driving NT8's window? The first compile is a step inside NT8, not a terminal command (`README.md:54@9664d9b`: "In NinjaTrader, open the NinjaScript Editor and **compile (F5)**"; `report:31`: "Installing means copying C# into `bin\Custom\AddOns` and compiling it in NT8"; `report:140`). Ruling 1 settles the terminal install and its order; it does not say whose hand presses F5.~~
+- ~~Anything you leave out, the VM agent does not assume. Step 3 does not start until items 1–6 are answered in your words.~~
 
 ## 3. Step 1 — VM agent self-report (test 2b, part 1)
 
 Write `Z:\vm\replies\<ts>-STATUS.md` with `STARTED` first.
 
-Report each item below. Observe only: open no settings dialog, click no Connect or Disconnect.
-
+Report each item below. Observe only: open no settings dialog, click no Connect or Disconnect. **Amendment 2:** one exception — item 0 opens the Trading Hours window, read-only.
+
+0. **VM step 0 — read the live trading-hours template (R1; Amendment 2).** Do this first, before items 1–9. Amear's words (D-2026-11-08-A R1, DECISIONS.md:1551–1555; source `docs/reports/2026-11-08-amear-rulings-voice.md`:18–22, REPORTED BY the Claude.ai channel and pasted by Amear, per that file's :3; ledger DECISION_LOG `2026-11-08T14:02:11Z`, WHO: amear). Placing his "VM step 0" here, as step 1 item 0, and reading the hours in NT8's Trading Hours window, is this file's reading, not his word; what his "(T7 readback)" names is not settled here:
+   ```text
+   R1  RTH = 09:30–16:00 ET (answers §4 item 1, B1). Arms (a) and (b)
+       anchor at the 09:30 ET cash open. VM step 0 reads the live
+       "CME US Index Futures RTH" template hours (T7 readback). If the
+       live template starts 08:30 ET, the 2026-11-01 baselines are
+       suspect and are re-run at 09:30 ET before either arm counts.
+   ```
+   - **Read only.** Change nothing: edit no field, add or delete no template or session, press no Save, OK or Apply. Close the window with its close button. If a prompt appears on closing, choose the answer that saves nothing; if no answer clearly saves nothing, leave the prompt open, STOP and reply.
+   - **NT8 must already be running.** Check with item 7's command first. If NT8 is not running, do not start it (limit 3): answer this item "could not read: NT8 not running", answer items 1–9 as written, set the self-report's `RESULT:` line to `STOP` (that self-report is the STOP reply of section 7), write `FINISHED`, and wait for Code. Do not go on to step 2. (The STOP is this file's reading of limit 3, not Amear's word.)
+   - **Route.** Tools → Trading Hours. Source: the committed reference `docs/reference/2026-07-24-nt8-windows-reference.md`, :32 (Tools menu list, marked "from notes") and :156 (`Tools > Trading Hours`). Code has not seen this window on this VM: the route is UNVERIFIED. If the menu differs, reach the Trading Hours window through NT8's own menus, open nothing else, and say how you got there.
+   - **Which template.** The one named exactly `CME US Index Futures RTH` — the name in step 4's table, row 7. If no template has that exact name, STOP: list the template names you see, and reply.
+   - **What to copy, exactly as the screen shows it:** the template's time-zone field; and every session row of its regular sessions, in order — begin day, begin time, end day, end time. If the window has other parts (for example holidays), list their names only; do not open them.
+   - **Do not judge it.** Do not convert time zones, compare with 09:30–16:00 or say whether it "starts 08:30 ET". Code, not you, decides whether R1's 08:30 clause fired. What follows if it fired is in his words above; no step in this file runs it. Code does not know what the live template holds (UNVERIFIED). Whatever it shows, change nothing in step 4: row 7 stays as written, and a difference is reported, not fixed (limit 13).
+   - **Reply:** in the self-report, as item 0: the route you used, then the copied text under `## What I saw on screen`.
 1. Your identity: product name, model and version, as you know them. Say whether you are "the Claude agent running inside the Windows VM" (settlement 3) or something else.
 2. How you load skills: the full path of your skills directory, and the file layout you expect there (for example `<dir>\<name>\SKILL.md`). Report your own convention. Do not guess it.
 3. `python --version` — paste the output. The bridge needs "Python 3.10+" (`README.md:35@9664d9b`; `report:143`).
 4. `$PSVersionTable.PSVersion` — paste the output.
 5. `git --version` — paste the output, or the error. Step 3 needs git.
-6. NT8 version from NinjaTrader → Help → About (D-2026-11-06-A item 1). Amear's own words cover this one read: "VM agent reads and reports the NT8 version" (ruling 5, DECISIONS.md:1063). The Help → About route is the master's (DECISION_LOG `2026-11-06T22:11:54Z`). It is the only NT8 window step 1 opens. If NT8 is not running, do not start it (limit 3): write "could not read: NT8 not running". Copy the text exactly. The bridge report "observes no value of the VM's NT8 build" (`report:2965`). The repo carries REPORTED values that differ by date: 8.1.7.2 from installer events, 2026-10-19 (`report:2966`); 8.1.8.4 per Amear, 2026-10-31 (`report:2967`); 8.1.8.4 per Claude Code on the VM, 2026-11-02 (`report:2968`). Code has observed none of them.
+6. NT8 version from NinjaTrader → Help → About (D-2026-11-06-A item 1). Amear's own words cover this one read: "VM agent reads and reports the NT8 version" (ruling 5, DECISIONS.md:1063). The Help → About route is the master's (DECISION_LOG `2026-11-06T22:11:54Z`). ~~It is the only NT8 window step 1 opens.~~ **Amendment 2:** it and item 0's Trading Hours window are the only NT8 windows step 1 opens. If NT8 is not running, do not start it (limit 3): write "could not read: NT8 not running". Copy the text exactly. The bridge report "observes no value of the VM's NT8 build" (`report:2965`). The repo carries REPORTED values that differ by date: 8.1.7.2 from installer events, 2026-10-19 (`report:2966`); 8.1.8.4 per Amear, 2026-10-31 (`report:2967`); 8.1.8.4 per Claude Code on the VM, 2026-11-02 (`report:2968`). Code has observed none of them.
 7. Is NT8 running? `Get-Process NinjaTrader -ErrorAction SilentlyContinue | Select-Object Id,StartTime` — paste the output.
 8. Your Documents folder: `[Environment]::GetFolderPath('MyDocuments')` — paste the output. NT8's folders sit under it.
-9. Amear's step-0 words (the six items of section 2). Paste them word for word. If you got none, say so.
+9. ~~Amear's step-0 words (the six items of section 2). Paste them word for word. If you got none, say so.~~ **Amendment 2:** Amear's step-0 answers, as filed in section 2 (C10: Amear does not repeat them). Copy the six answers from section 2's table, word for word, and say that you read them from this file. Do not wait for Amear to give them to you.
 
 **Reply:** `Z:\vm\replies\<ts>-self-report.md`, in the format of section 7.
 **You should see:** every item answered, or marked "could not read" with the reason.
@@ -88,7 +135,7 @@ Then write `<ts>-STATUS.md` with `FINISHED`, and stop. Wait for `Z:\vm\replies\<
 
 ## 5. Step 3 — install cli-nt-bridge
 
-**Gate:** start only when all of these hold. (a) `Z:\vm\replies\<ts>-CODE-2b-verdict.md` exists and holds the line `2b: PASS`. (b) The same file holds the line `SNAPSHOT: confirmed` — Code writes it only after reading Amear's step-0 words in your self-report. (c) Amear's words answer section 2 items 2–6 (route, file set, request folders, sim account, who compiles), and the answers let the steps run as written: item 3 accepts the two files of 3.2, item 4 accepts the request folders, item 5 names a sim account. A no, a different file set, a condition, or anything unclear is not a yes: STOP, quote his words in a reply, and wait. Do not adapt the steps. If any fails, do not start. Write `STARTED` first.
+**Gate:** start only when all of these hold. (a) `Z:\vm\replies\<ts>-CODE-2b-verdict.md` exists and holds the line `2b: PASS`. (b) The same file holds the line `SNAPSHOT: confirmed` — ~~Code writes it only after reading Amear's step-0 words in your self-report.~~ **Amendment 2:** Code writes it from Amear's item-1 answer as filed in section 2 (C9, REPORTED BY Amear); the line means Amear reports the snapshot taken, not that Code has seen it. (c) ~~Amear's words answer section 2 items 2–6 (route, file set, request folders, sim account, who compiles), and the answers let the steps run as written: item 3 accepts the two files of 3.2, item 4 accepts the request folders, item 5 names a sim account. A no, a different file set, a condition, or anything unclear is not a yes: STOP, quote his words in a reply, and wait.~~ **Amendment 2:** Amear's answers to section 2 items 2–6 are filed in section 2 (C3) and let the steps run as written: item 2 names the HTTPS clone of 3.1, item 3 names the two files of 3.2, item 5 names Sim101, item 6 names his own hand for the compile (3.3). Item 4 carries his condition, "for sim tests only"; that 2b and 2a are sim tests is this file's reading (section 2), not his word. Anything else unclear: STOP, quote his words in a reply, and wait. Do not adapt the steps. If any fails, do not start. Write `STARTED` first.
 
 What the install is: copy C# into `bin\Custom\AddOns` and compile it in NT8 (`report:31`, `report:140`). Amear's lift covers it: "bridge install + its import" (DECISIONS.md:1089, settlement 6). The commands below are untried.
 
@@ -100,7 +147,7 @@ git -C C:\praxis\bridge-src checkout 9664d9b
 git -C C:\praxis\bridge-src rev-parse HEAD
 ```
 - **You should see:** `9664d9b255bfa34b120d88a481afe7741a4115e6` from the last line (the pinned commit, `report:2973`).
-- The README clones over SSH (`README.md:41@9664d9b`: `git clone git@github.com:eman007/cli-nt-bridge.git`), which "needs a GitHub key" (`report:142`). The block above is the anonymous HTTPS clone the master proposed (DECISION_LOG `2026-11-06T22:11:54Z`). Run it only if Amear's step-0 words chose it. If he chose another route, follow his words and paste what you typed. How the source reaches the VM is his (bridge NEEDS AMEAR 11, `report:235`).
+- The README clones over SSH (`README.md:41@9664d9b`: `git clone git@github.com:eman007/cli-nt-bridge.git`), which "needs a GitHub key" (`report:142`). The block above is the anonymous HTTPS clone the master proposed (DECISION_LOG `2026-11-06T22:11:54Z`). ~~Run it only if Amear's step-0 words chose it. If he chose another route, follow his words and paste what you typed. How the source reaches the VM is his (bridge NEEDS AMEAR 11, `report:235`).~~ **Amendment 2:** he chose it — "(2) anonymous HTTPS clone, step 3.1;" (C3, section 2). Run the block above.
 - If `git` is missing or the clone asks for a login: STOP, reply.
 - **Reply line:** paste all four commands' output.
 
@@ -121,12 +168,12 @@ Get-ChildItem "$D\NinjaTrader 8\bin\Custom\AddOns" | Select-Object Name,Length,L
 - **You should see:** both names in the listing.
 - **Reply line:** paste both listings.
 
-**3.3 Compile in NT8 — wait for Amear's word on section 2, item 6.** The README's first compile is a step inside NT8 (`README.md:54@9664d9b`: "In NinjaTrader, open the NinjaScript Editor and **compile (F5)**"). NT8 compiles "the whole tree" (`report:141`). The bridge's own `compile` command is not permitted (section 1, limit 4). Who presses F5 is Amear's (item 6). This file assumes neither path. Follow only the path his words name:
+**3.3 Compile in NT8 — ~~wait for Amear's word on section 2, item 6.~~ Amendment 2: item 6 is answered — "(6) Amear presses Compile in the NinjaScript Editor by hand." (C3, section 2). Follow the "If he does it by hand" path below only; the other two paths are superseded.** The README's first compile is a step inside NT8 (`README.md:54@9664d9b`: "In NinjaTrader, open the NinjaScript Editor and **compile (F5)**"). NT8 compiles "the whole tree" (`report:141`). The bridge's own `compile` command is not permitted (section 1, limit 4). Who presses F5 is Amear's (item 6). ~~This file assumes neither path.~~ Follow only the path his words name:
 - **If he does it by hand:** after 3.2, wait. Do nothing in NT8. When Amear tells you he has compiled, paste his words, word for word, and the result he gives you (clean, or the error lines) into the reply.
-- **If he lets you drive NT8's window for this compile:** open the NinjaScript Editor, press F5, and copy what the editor shows. Do nothing else in NT8's windows. His word covers this one compile only; it does not cover the Strategy Analyzer tab (step 4.3).
-- **If his words do not clearly name one of the two:** STOP and reply. Do not choose.
+- ~~**If he lets you drive NT8's window for this compile:** open the NinjaScript Editor, press F5, and copy what the editor shows. Do nothing else in NT8's windows. His word covers this one compile only; it does not cover the Strategy Analyzer tab (step 4.3).~~ (Superseded by Amendment 2: his item-6 answer names his hand. Do not open the NinjaScript Editor.)
+- ~~**If his words do not clearly name one of the two:** STOP and reply. Do not choose.~~ (Superseded by Amendment 2: his words name one.)
 - **You should see:** no compile errors. If there are any, copy every error line (file, line, message) into the reply, and STOP. Do not edit any `.cs` file.
-- **Reply line:** Amear's item-6 words, then "Compile by: Amear" or "Compile by: VM agent", then "Compile: clean" or the error lines.
+- ~~**Reply line:** Amear's item-6 words, then "Compile by: Amear" or "Compile by: VM agent", then "Compile: clean" or the error lines.~~ **Amendment 2 — Reply line:** Amear's item-6 answer as filed in section 2, then "Compile by: Amear", then his words, word for word, when he tells you he has compiled, then "Compile: clean" or the error lines.
 
 **3.4 Check the request folders.** The AddOn polls `<UserDataDir>\NT8Bridge\trigger` and writes to `\result` (`report:47`; folders `report:145`):
 ```
@@ -134,8 +181,8 @@ $D = [Environment]::GetFolderPath('MyDocuments')
 Test-Path "$D\NinjaTrader 8\NT8Bridge\trigger"; Test-Path "$D\NinjaTrader 8\NT8Bridge\result"
 ```
 - **You should see:** `True` and `True` once NT8 has loaded the compiled AddOn. If `False`, restart nothing; reply with the output.
-- These folders take requests from any process running as your Windows user, with no authentication (`report:173`; Correction 1, C1-3, `report:2868`: who can write them on the VM is UNVERIFIED). Whether that is acceptable is Amear's question (bridge NEEDS AMEAR 3, `report:227`).
-- **Go-live (not these tests).** Amear: "Go-live checklist additions: remove the unauthenticated bridge request folders (or add auth) before real money; unmap Z: and turn off the SMB share." (DECISIONS.md:1234, D-2026-11-07-A ruling 10). Both items are in the go-live checklist of `docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md` (`:35` unmap Z: and the share; `:38` the request folders). They bind before real money. Whether the folders are acceptable for these tests stays section 2, item 4.
+- These folders take requests from any process running as your Windows user, with no authentication (`report:173`; Correction 1, C1-3, `report:2868`: who can write them on the VM is UNVERIFIED). ~~Whether that is acceptable is Amear's question (bridge NEEDS AMEAR 3, `report:227`).~~ **Amendment 2:** answered — "(4) unauthenticated request folders acceptable for sim tests only, closed before real money (go-live list);" (C3, section 2).
+- **Go-live (not these tests).** Amear: "Go-live checklist additions: remove the unauthenticated bridge request folders (or add auth) before real money; unmap Z: and turn off the SMB share." (DECISIONS.md:1234, D-2026-11-07-A ruling 10). Both items are in the go-live checklist of `docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md` (`:35` unmap Z: and the share; `:38` the request folders). They bind before real money. ~~Whether the folders are acceptable for these tests stays section 2, item 4.~~ **Amendment 2:** section 2 item 4 is answered (C3 (4)); its "closed before real money (go-live list)" restates ruling 10's first item (the master's reading, changeable by Amear; the wordings differ: "closed" here, "remove … (or add auth)" in ruling 10) and is appended to the same go-live list (`docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md`, the line after `:38`).
 
 **3.5 Python CLI.** The README (`README.md:43–45@9664d9b`):
 ```
@@ -308,6 +355,14 @@ This file answers none of these. Where a row is settled, the answer is Amear's w
 Settled since 2026-11-06:
 - Whether the 2a NT8 run on the VM needs his separate word (D-2026-11-06-A NEEDS AMEAR 6, DECISIONS.md:1046): the run half is answered in his words — "2a run: YES, covered by my lift. A test that needs a run includes the run." (DECISIONS.md:1229, D-2026-11-07-A ruling 5). The D-071 half is not: "The D-071 half of that question is not answered by ruling 5's words." (DECISIONS.md:1263). Limit 3 stands.
 
+Settled since 2026-11-08 (Amendment 2). Where a row above still says **Amear's** or "asked at step 0", this list supersedes that cell; the rows themselves are not edited. Source for all: D-2026-11-08-C (DECISIONS.md:1830–1834, :1846–1847); ledger DECISION_LOG `2026-11-08T19:12:30Z`, WHO: amear.
+- Row 1, which files: "(3) only the two AddOn files of step 3.2;" (C3). The lift half stays as the row says.
+- Row 2, whose hand for the in-NT8 compile: "(6) Amear presses Compile in the NinjaScript Editor by hand." (C3).
+- Row 3, the request folders: "(4) unauthenticated request folders acceptable for sim tests only, closed before real money (go-live list);" (C3). That 2b and 2a are sim tests is this file's reading (section 2), not his word.
+- Row 8, the account: "(5) Sim101;" (C3).
+- Row 9, the snapshot: "Step 0, item 1: snapshot taken, named pre-cli-nt-bridge-2026-11-06." (C9). REPORTED BY Amear; not observed by Code.
+- Row 11, route half: "(2) anonymous HTTPS clone, step 3.1;" (C3). The `pip` half is unchanged, as the row says; its open sub-question stays **Amear's**.
+
 Still not decided here:
 - Whether 2a/2b have passed. Code and praxis-auditor judge that (settlement 8). A 2a PASS on a hand-set tab is logged as a partial pass per ruling 6 (step 4.6). Recording the lift is "under my ruling" — his.
 
@@ -348,4 +403,4 @@ Amear, D-2026-11-07-A ruling 7 (DECISIONS.md:1231): "(12) you propose how each a
 8. The copy to Z: (9.2): the master's proposal; untried.
 9. How the NT8 Output-window text and NT8's own trade lists are captured on the VM and moved to Z: is not set here — UNVERIFIED. The only bridge commands permitted are `backtest` and `ntstatus` (limit 4); the `backtest` response shape (`report:65`) carries neither (INFERRED). Who does it, and by what route: **Amear's**.
 
-**9.5 Not answered here.** §8 rows 1, 2, 3 and 8, and row 11's route half, stay **Amear's**; row 6 is a pending value from step 1 (DECISIONS.md:1278). Nothing in §9 answers them, nor who sets the tab by hand, nor the account. §9 takes effect only by his word, after 2a passes.
+**9.5 Not answered here.** ~~§8 rows 1, 2, 3 and 8, and row 11's route half, stay **Amear's**;~~ **Amendment 2:** §8 rows 1, 2, 3 and 8, and row 11's route half, are now answered in his words (C3; §8, "Settled since 2026-11-08"); row 6 is a pending value from step 1 (DECISIONS.md:1278). Nothing in §9 answers them, nor who sets the tab by hand~~, nor the account~~ (the account is answered: "(5) Sim101;", C3). §9 takes effect only by his word, after 2a passes.
$ wc -l vm/2026-11-06-vm-handoff.md docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md MANIFEST.md
     406 vm/2026-11-06-vm-handoff.md
      39 docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md
     319 MANIFEST.md
     764 total
$ git show HEAD:MANIFEST.md | wc -l
     308
$ git diff HEAD -- MANIFEST.md | tail -n 20
index 9e92c26..088647c 100644
--- a/MANIFEST.md
+++ b/MANIFEST.md
@@ -304,5 +304,16 @@
 | /DECISIONS.md | Log | 2 | 2026-11-09 | Update: D-2026-11-08-C (DECISIONS.md:1808-1889; Amear's answers C1–C10 to the 2026-11-08 park card, answers file lines 12–43 verbatim by script, per-answer pointers, master's filing notes 1–5 labelled as the master's, two open readings left to the acting units under D-2026-11-08-D D1, nothing resolved; drafted by U8, checked and finished by unit 2026-11-09-c-d-filing (no return), re-checked by unit 2026-11-09-c-d-filing-resume, which replaced C's HANDOFF.md line pointers with park-card item pointers) and D-2026-11-08-D (DECISIONS.md:1891-2007; Amear's rulings D1–D12, voice-2 file lines 12–75 verbatim by script, per-ruling pointers, master's filing notes 1–5 labelled as the master's, S8 scope change recorded as a reading, rubric amendment left to the D12 rubric unit) appended |
 | /docs/reports/2026-11-09-c-d-filing-resume-manager.md | Report | 2 | 2026-11-09 | Manager report for unit 2026-11-09-c-d-filing-resume (re-ran the checks of the no-return unit 2026-11-09-c-d-filing on D-2026-11-08-C and D-2026-11-08-D; replaced 14 HANDOFF.md line pointers in C with park-card item pointers; fresh read-only adversary; corrections to the C/D filing's MANIFEST rows and this row). Two manager dispatches: dispatch 1 returned incomplete, and its Result line is superseded by the Result at the end of the section "Continuation — manager dispatch 2"; untracked (`??`) at time of row, ungraded |
 | /docs/reports/2026-11-09-d6-drawdown-check-manager.md | Report | 2 | 2026-11-09 | Manager report for unit 2026-11-09-d6-drawdown-check (Amear D-2026-11-08-D D6): per-walk-forward-window worst drawdown at 1 MNQ and 1 NQ on the three hash-pinned 2026-11-01 NT8 base-strategy trade lists vs the A4 ceiling per tier row; breaker #1 has no spec value (sensitivity only); 09:30 ET re-run not possible with committed scripts/wf; D7 test answered on both measures. Read-only; scripts in /tmp pasted in the appendix. |
+| /docs/specs/2026-11-06-walk-forward-values.md | Spec | 2 | 2026-11-08 | AMENDMENT ROW (append-only registry — adds to rows 254 and 271 for this path). Version 2.2 in place, unit 2026-11-08-wf-spec-amendment (dispatch DECISION_LOG 2026-11-08T16:12:00Z, WHO: praxis-master), under D-2026-11-08-A R1–R3 and D-2026-11-08-B A1–A8: §4 RTH hours (R1; baseline re-run CONDITIONAL; live template UNVERIFIED); §6 gate 2 (A2) and trading day (A5, first half); §8 gate sets (A7), judged arm (R2), WFE formula (A8), O1 state, Max-DD buffer (A4), win rate (A3); list (C)/(D) status cells, old text kept as was: "…". 20 lines edited in place, none added or removed. D-2026-11-08-B NEEDS AMEAR (i)–(iv) and A5's second half stay open; ungraded at time of row |
+| /docs/specs/2026-11-05-walk-forward-spec.md | Spec | 3 | 2026-11-08 | AMENDMENT ROW (append-only registry — adds to row 227 for this path). Unit 2026-11-08-wf-spec-amendment: A4's 80% Max-DD buffer (D-2026-11-08-B) at §6 :107, the per-tier table header :113 and §8 :156; one pointer at :28; the quotes at :31 and :39 unchanged; a minimal dated changelog appended to :5. 5 lines edited in place, none added or removed. NEEDS AMEAR (ii), both halves, stays open; ungraded at time of row |
+| /docs/reports/2026-11-08-wf-spec-amendment-manager.md | Report | 2 | 2026-11-08 | Manager report for unit 2026-11-08-wf-spec-amendment (U7: values spec v2.2 and the WF spec Max-DD amendment under D-2026-11-08-A R1–R3 and D-2026-11-08-B A1–A8; MANIFEST: the U7 amendment rows for the two specs and this report); untracked (`??`) at time of row, ungraded |
+| /docs/reports/2026-11-08-wf-spec-amendment-correction-1-manager.md | Report | 2 | 2026-11-08 | Manager report for the two-line correction to the values spec :3 and :128 (unit 2026-11-08-wf-spec-amendment, correction 1); untracked (`??`) at time of row |
+| /docs/reports/2026-11-08-wf-spec-amendment-correction-2-manager.md | Report | 2 | 2026-11-08 | Manager report for unit 2026-11-08-wf-spec-amendment-correction-2 (cures audit FAIL 1 of U7, DECISION_LOG 2026-11-08T17:08:00Z: Correction 1 appended to the U7 report; in-place labels at values :5, :93, :135 and WF spec :28, :107; MANIFEST: the U7 correction-1 and correction-2 report rows); ungraded at time of row |
+| /docs/reports/2026-11-08-wf-spec-amendment-correction-3-manager.md | Report | 2 | 2026-11-08 | manager report for the one-sentence update of values spec :12 (OPEN legend) to version 2.2 state; ungraded at time of row |
+| /docs/reports/2026-11-09-wf-spec-amendment-resume-manager.md | Report | 2 | 2026-11-09 | Manager report for unit 2026-11-09-wf-spec-amendment-resume (U7 resumed under Amear C1, D-2026-11-08-C; bead Praxis_build-diq): the U7 amendment rows moved after HEAD's rows (master's decision under D-2026-11-08-D D1) and their self-references made line-independent; the diff of record of the spec blobs being committed, superseding the stale paste in the U7 manager report; untracked (`??`) at time of row, ungraded |
+| /docs/reports/evidence/2026-11-09-u7-diff-of-record.patch | Evidence | 2 | 2026-11-09 | Byte-exact `git diff HEAD` of the two U7 spec amendments (docs/specs/2026-11-06-walk-forward-values.md, docs/specs/2026-11-05-walk-forward-spec.md), 43982 bytes, sha256 b06ee494396805c3cf0abc19314010347850b854c74a3e8f5a3f0226a6d4369e; the diff of record under Amear C1 (D-2026-11-08-C) for bead Praxis_build-diq, added by master decision under D-2026-11-08-D D1; untracked (`??`) at time of row, ungraded |
 | /docs/reports/2026-11-09-d11-sweep-manager.md | Report | 2 | 2026-11-09 | Manager report for unit 2026-11-09-d11-sweep (Amear D-2026-11-08-D D11): inventory of questions to Amear raised before 2026-11-09T09:00Z across sources A-G (HANDOFF cards, three return handoffs, DECISIONS NEEDS AMEAR, ISSUE_REGISTER, docs/specs, the bf6fcc7 R6 design, open beads); 40 WAITING (25 NOT-D2, 3 D2, 12 D2-AMBIGUOUS), 3 raised after the cutoff, 87 ANSWERED-BY, 61 CLOSED-OTHER (per source row), 13 actions in Amear's hands; proposals only, nothing closed; 416 pointers re-run and pasted; ADV1 no result (turn cap), ADV2a and ADV2b findings resolved. |
 | /docs/reports/2026-11-09-rubric-unit-manager.md | Report | 2 | 2026-11-09 | Manager report for unit 2026-11-09-rubric-unit (Amear D-2026-11-08-D D12; C2, C6, C8 of D-2026-11-08-C; D1-D5 of D-2026-11-08-D): specs/SPEC_RUBRIC.md edited (HEAD 345 lines, now 413): the July R-A/R-B/R-C hunk landed byte-for-byte (C8); O1 moved under a new "PASSED — closed criteria" heading (C6); the C2 park-commit exemption quoted and recorded as RULED and NOT YET BUILT; a new Autonomy section with D1-D5 copied by script; untracked (`??`) at time of row, ungraded |
+| /vm/2026-11-06-vm-handoff.md | Runbook | 2 | 2026-11-09 | UPDATE ROW 2026-11-09 (append-only registry; adds to rows 249 and 266 for this path): amendment 2, unit 2026-11-09-vm-handoff-amendment-2 at HEAD cec36b8 — Amear's step-0 answers C3 and C9 written into section 2 verbatim under C10 (D-2026-11-08-C), snapshot REPORTED BY Amear; R1 (D-2026-11-08-A) trading-hours template read added as step 1 item 0, read-only; limit 1, step 1's opening line and items 6 and 9, step 3 gate, steps 3.1, 3.3, 3.4, section 8 and §9.5 brought into line; superseded text kept struck through; untried |
+| /docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md | Report | 2 | 2026-11-09 | UPDATE ROW 2026-11-09 (append-only registry; adds to rows 231 and 264 for this path): one go-live line appended quoting Amear's C3 (4) (D-2026-11-08-C), "closed before real money (go-live list)", stating it restates the 2026-11-07 ruling-10 line; nothing above edited |
+| /docs/reports/2026-11-09-vm-handoff-amendment-2-manager.md | Report | 2 | 2026-11-09 | Manager report for unit 2026-11-09-vm-handoff-amendment-2 (C3, C9, C10, R1); ungraded at time of row |
$ head -n 316 MANIFEST.md | openssl dgst -sha256
SHA2-256(stdin)= a2c1afdc8f4655388e3a49227713b48c564da7c909f945ff706048b342c41042
$ { git show HEAD:MANIFEST.md; tail -n 3 MANIFEST.md; } | grep -n "amendment-2" | cut -c1-90
309:| /vm/2026-11-06-vm-handoff.md | Runbook | 2 | 2026-11-09 | UPDATE ROW 2026-11-09 (app
311:| /docs/reports/2026-11-09-vm-handoff-amendment-2-manager.md | Report | 2 | 2026-11-09
$ grep -c 'Fills are optimisti[c]' vm/2026-11-06-vm-handoff.md
1
$ git status --porcelain -- vm/2026-11-06-vm-handoff.md docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md MANIFEST.md docs/reports/2026-11-09-vm-handoff-amendment-2-manager.md
 M MANIFEST.md
 M docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md
 M vm/2026-11-06-vm-handoff.md
?? docs/reports/2026-11-09-vm-handoff-amendment-2-manager.md
$ git diff --cached --name-only | wc -l
      12
$ git diff --cached --name-only -- vm MANIFEST.md docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md docs/reports/2026-11-09-vm-handoff-amendment-2-manager.md | wc -l
       0
$ { git show HEAD:MANIFEST.md; tail -n 3 MANIFEST.md; } | sed -n '309,311p' | cut -c1-70
| /vm/2026-11-06-vm-handoff.md | Runbook | 2 | 2026-11-09 | UPDATE ROW
| /docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md | Repo
| /docs/reports/2026-11-09-vm-handoff-amendment-2-manager.md | Report 
````

The last command shows this unit's three rows at 309, 310, 311 of the commit blob (HEAD's 308 lines plus these rows). Their exact text (working tree :317–319):

````
$ tail -n 3 MANIFEST.md
| /vm/2026-11-06-vm-handoff.md | Runbook | 2 | 2026-11-09 | UPDATE ROW 2026-11-09 (append-only registry; adds to rows 249 and 266 for this path): amendment 2, unit 2026-11-09-vm-handoff-amendment-2 at HEAD cec36b8 — Amear's step-0 answers C3 and C9 written into section 2 verbatim under C10 (D-2026-11-08-C), snapshot REPORTED BY Amear; R1 (D-2026-11-08-A) trading-hours template read added as step 1 item 0, read-only; limit 1, step 1's opening line and items 6 and 9, step 3 gate, steps 3.1, 3.3, 3.4, section 8 and §9.5 brought into line; superseded text kept struck through; untried |
| /docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md | Report | 2 | 2026-11-09 | UPDATE ROW 2026-11-09 (append-only registry; adds to rows 231 and 264 for this path): one go-live line appended quoting Amear's C3 (4) (D-2026-11-08-C), "closed before real money (go-live list)", stating it restates the 2026-11-07 ruling-10 line; nothing above edited |
| /docs/reports/2026-11-09-vm-handoff-amendment-2-manager.md | Report | 2 | 2026-11-09 | Manager report for unit 2026-11-09-vm-handoff-amendment-2 (C3, C9, C10, R1); ungraded at time of row |
````

### Report's own S13 count (observer effect)

Taken after this report was written in full, then put on the line below by script. The pattern is written `optimisti[c]` so that the pasted command line does not itself match; it matches the same text as the brief's literal pattern. The pasted output does not match either, so pasting it does not change the count. SUPERSEDED first run: it printed `2`, because this paragraph then quoted the brief's pattern literally; the paragraph was reworded and the count re-run. The value below is the re-run.

````
$ grep -c 'Fills are optimisti[c]' docs/reports/2026-11-09-vm-handoff-amendment-2-manager.md
1
````

### Other observations used in this report

````
$ sed -n 72p docs/specs/2026-11-06-walk-forward-values.md | grep -o "T7[^.]*\."
T7 readback).
T7 readback that R1 names, which has not been run.
T7 (:193) reads back other settings (commission template, backtest type, fill resolution, slippage), not template hours.
$ git show HEAD:docs/specs/2026-11-06-walk-forward-values.md | grep -c "not template hours"
0
$ git show 29c3e13:docs/reports/2026-10-31-o78-worker4-report-adversarial.md | sed -n 210,212p | cut -c1-120
-----CME US Index Futures RTH
TimeZone ['Eastern Standard Time']
[('Monday', '830', 'Monday', '1600'), ('Tuesday', '830', 'Tuesday', '1600'), ('Wednesday', '830', 'Wednesday', '1600'),
````

The rescued copy at `29c3e13` printed Monday–Friday `830`–`1600` with TimeZone `Eastern Standard Time` — REPORTED BY that worker (DECISIONS.md:1619 records it as such). It is a rescued file, not the live VM template. The live template is UNVERIFIED; the handoff asserts nothing about what it holds.

## Adversarial findings

### W1 output — the worker's (`aa73c5e34a67dcbbb`, ADVERSARIAL), as returned; harness indentation removed

````
## Adversarial review: VM-handoff Amendment 2 and the walkthrough append

The change does not hold. One MAJOR finding: §9.5 still says items are open that §2 and the new §8 list now settle. There are also nine MINOR findings. All pointers check out, and the Markdown has no errors. I changed nothing: no file, no index, no memory.

### Findings

**F1. MAJOR.** Handoff line 406 (§9.5, not amended): "§8 rows 1, 2, 3 and 8, and row 11's route half, stay **Amear's** … Nothing in §9 answers them, nor who sets the tab by hand, nor the account."
- This contradicts the new §8 list (lines 358–364). That list says rows 1 (files), 2, 3, 8 and 11's route half are settled in his words, and §2/limit 1 (line 28) says "The account is Sim101."
- The criterion names §9.5 explicitly for the S6 test. The header (line 22) lists what was "brought into line" and leaves §9 out.
- It also breaks S2: settled items are reported at a lower level than the evidence supports.

**F2. MINOR.** Line 385 (§9.2, not amended): "**Amear's** (like step-0 items 2 and 6)." Items 2 and 6 are now answered, so the comparison now points at answered questions. This is the S6 issue again, at smaller scale.

**F3. MINOR.** Line 21 (Amendment 1 authority line, not amended): "rulings 5–8 and 10 … quoted where applied: … section 2". The ruling-8 quote in §2 is now struck (line 77), so the line points at superseded text. Criterion (e)/S6.

**F4. MINOR.** Line 22 says it brings "section 1 limit 1, step 1 item 9, the step 3 gate, steps 3.1, 3.3 and 3.4, and section 8 into line." That list is incomplete:
- Step 1 item 6 (line 116) was amended but is not listed.
- The step 4 gate (line 209), §7 (lines 320 and 329) and SKILL.md lines 13 and 16 were left alone. They still say "Amear's step-0 words" without saying those are now the filed §2 answers.
- None of them now says to wait. Each resolves through "(section 2, item 5)", so criterion (b) is not broken, but the header's claim of completeness is wrong.

**F5. MINOR.** Line 96: "**VM step 0 — read the live trading-hours template (R1; Amendment 2).**" Two readings of R1 are presented as if they were R1 itself, with no label (criterion d):
- that R1's "VM step 0" is step 1 item 0;
- that its "(T7 readback)" is a read of the Trading Hours window.

The spec's T7 is a tab-settings readback "as the 2a skill does" (values spec :193), run after 2a. The working-tree values spec :72 says that T7 "reads back other settings … not template hours".

**F6. MINOR.** Line 109: "Code, not you, decides whether R1's 08:30 clause fired, and what follows from it."
- "Whether it fired" is approved by criterion (c).
- "And what follows from it" goes beyond that. R1 itself states what follows (re-run at 09:30), and the line has no label (criterion d).
- The working-tree values spec :72 says a start time other than 08:30 "is not covered by them and is his to decide". That sentence is not in HEAD (grep count 0).

**F7. MINOR.** Line 72: "they run on Sim101 only (item 5; limit 1) and place no orders". This is the stated support for the INFERRED reading "sim tests". 2a is a Strategy Analyzer backtest. Which account NT8 uses for it is UNVERIFIED (I believe it is an internal Backtest account, not Sim101; not checked this session).
- Gate (c) at line 138 now passes item 4's condition on that inference.
- The old gate's own rule was "a condition … is not a yes: STOP".
- This is S2: the premise is asserted, not graded.

**F8. MINOR.** Line 185: "its 'closed before real money (go-live list)' restates ruling 10's first item". This is stated flatly. The walkthrough line notes that the wordings differ ("closed" against "remove … (or add auth)"); this line drops that caveat and gives no reading label (criterion d).

**F9. MINOR.** Lines 48 and 96 grade the words "verbatim (WHO: amear)". The sources grade them "REPORTED BY the Claude.ai channel and pasted by Amear" (answers file :3, DECISIONS.md:1811, voice file :3), and that step in the chain is dropped (S2). His approval line (:14) partly offsets this.

**F10. MINOR.** Lines 138 and 320: Code writes `SNAPSHOT: confirmed` from C9, which is REPORTED BY Amear. Only the handoff says "REPORTED"; the verdict file's token would say "confirmed" alone. The token states a higher grade than the evidence (S2).

### Checked and not broken
- **Criterion (a):** the §2 quote matches the answers file lines 23–27 and 39–43 exactly. The old text is struck, not deleted, and the snapshot is graded REPORTED.
- **Criterion (c):** item 0 is read-only, comes before step 3, copies the time-zone field and the session rows, and asserts nothing about what the template holds. The NT8-not-running STOP follows limit 3 and is labelled. The route is marked UNVERIFIED.
- **Criterion (f):** one line was appended at :39. HEAD has 38 lines and HEAD's :38 is unchanged.
- **Criterion (h):** strikethrough nesting, the "0." list with a 3-space-indented fence, and the 4-column table are all valid.

### Pointer evidence (g)
Every pointer resolves to what it claims. Both ledger rows exist in the working tree and in HEAD at the same line numbers.

- **Answers file:** C3 at :23–27, C9 at :39–40, C10 at :41–43, approval line at :14. The C3 (4) clause runs :24–26.
- **DECISIONS.md** (same as HEAD): `1808:## 2026-11-08 — D-2026-11-08-C`. C3 at 1830–1834; (4) inside 1831–1833; C9 at 1846–1847; C10 at 1848–1850.
- **R1:** DECISIONS.md :1551–1555 (`1534:## … D-2026-11-08-A`); voice file :18–22.
- **DECISION_LOG:**
  - working tree: `718:- [2026-11-08T14:02:11Z] **WHO: amear**`, `743:- [2026-11-08T19:12:30Z] **WHO: amear**`
  - `git show HEAD:DECISION_LOG.md | grep -n`: the same rows at 718 and 743 (exit=0)
- **Reference doc:** `32: - **Tools menu** (from notes): … · **Trading Hours** ·` and `156: … via \`Tools > Trading Hours\` …`
- **Walkthrough:** `35: - [ ] **Go-live checklist, his words:** "unmap Z: …"`, `38: - [ ] **Go-live checklist addendum 2026-11-07, his words (ruling 10):**`. HEAD line count is 38.

Side note, outside the criteria: both artifact files are unstaged (` M`), not staged.

VERDICT: REFUTED
````

Note on W1's form: the harness returned W1's report reformatted as prose with summarised pointer evidence; its raw command output did not reach me. Its pointer results are therefore REPORTED BY W1. The pointers this report itself relies on are also visible in the pasted diff and in my own reads (process step 2).

### What I did with each W1 finding

| # | Disposition |
|---|---|
| F1 MAJOR | Fixed: §9.5 (:406) amended (old text struck; rows now answered, C3; account answered). Listed as the one §9 line changed. |
| F2 MINOR | Not changed. :385 (§9.2) is the master's proposal, out of scope; "like step-0 items 2 and 6" still holds — those were Amear's questions, and he answered them. Flagged to the master (Open 8). |
| F3 MINOR | Not changed. :21 is amendment 1's authority line, a record of 2026-11-07; the ruling-8 quote it points at is kept, struck, at :76. |
| F4 MINOR | Fixed: :22 now lists step 1's opening line, items 6 and 9, §9.5, the walkthrough append, and names the unedited "step-0 words" lines that now read §2. |
| F5 MINOR | Fixed: :96 labels the placement as step 1 item 0, and the Trading Hours window read, as this file's reading; "(T7 readback)" left unsettled. |
| F6 MINOR | Fixed: :109 now "Code, not you, decides whether R1's 08:30 clause fired. What follows if it fired is in his words above; no step in this file runs it." |
| F7 MINOR | Fixed: :72 now "they run under limit 1 (Sim101 only; his item 5) and place no orders (limit 2). Which account NT8 uses inside a Strategy Analyzer backtest is UNVERIFIED." The reading stays a reading (Open 1). |
| F8 MINOR | Fixed: :185 labels "restates" as the master's reading and gives the wording difference. |
| F9 MINOR | Fixed: :46 and :96 add "REPORTED BY the Claude.ai channel and pasted by Amear". |
| F10 MINOR | Fixed: :138 says what `SNAPSHOT: confirmed` means (Amear reports it; Code has not seen it). |

### W2 output — the worker's (`ac0b020a456c72497`, ADVERSARIAL re-check), as returned; harness indentation removed; its closing spoken-summary block omitted

````
I checked the current working tree. All eight defects are cured. I found six new problems, all MINOR, and nothing that blocks.

**Defect status (line numbers are the current file's; the diff hunks run one lower)**

- **D1 — CURED.** Line 403: "~~§8 rows 1, 2, 3 and 8, and row 11's route half, stay **Amear's**;~~ **Amendment 2:** §8 rows 1, 2, 3 and 8, and row 11's route half, are now answered in his words (C3, C9; §8, "Settled since 2026-11-08") … nor who sets the tab by hand~~, nor the account~~ (the account is answered: "(5) Sim101;", C3)." This now agrees with limit 1 (:28) and §8's new list (:358–364). The citation `DECISIONS.md:1278` is unchanged from HEAD (checked with `git show HEAD:… | tail -n 1`), and it still resolves to "row 1 … row 2 … row 3 … row 8 … They stay his. Row 6". See new finding N1 for the new citation.
- **D4 — CURED.** Line 22: "brings section 1 limit 1, step 1's opening line and items 6 and 9, the step 3 gate, steps 3.1, 3.3 and 3.4, section 8 and §9.5 into line. … Lines that say "Amear's step-0 words" and were not edited (step 4 gate; section 7 items 5 and 14; the step-4 skill) now read those words from section 2." I checked each of those lines exists: :209, :320, :329, and `vm/skills/praxis-nt8-bridge-backtest/SKILL.md`:13. Small gaps are N3 and N5.
- **D5 — CURED.** Line 96: "Placing his "VM step 0" here, as step 1 item 0, and reading the hours in NT8's Trading Hours window, is this file's reading, not his word; what his "(T7 readback)" names is not settled here".
- **D6 — CURED.** Line 109: "Code, not you, decides whether R1's 08:30 clause fired. What follows if it fired is in his words above; no step in this file runs it."
- **D7 — CURED.** Line 72: "That tests 2b and 2a are "sim tests" in his words is INFERRED (this file's reading, not his word; changeable by him): they run under limit 1 (Sim101 only; his item 5) and place no orders (limit 2). Which account NT8 uses inside a Strategy Analyzer backtest is UNVERIFIED."
- **D8 — CURED.** Line 170 (step 3.4): "restates ruling 10's first item (the master's reading, changeable by Amear; the wordings differ: "closed" here, "remove … (or add auth)" in ruling 10)". The walkthrough file's :39 has the same label and the same note that the wordings differ.
- **D9 — CURED in §2 and item 0.** Line 46: "Amear's answers, verbatim (WHO: amear; REPORTED BY the Claude.ai channel and pasted by Amear, per the answers file's :3)". Line 96: "REPORTED BY the Claude.ai channel and pasted by Amear, per that file's :3". Both :3 lines say exactly that. The walkthrough line still lacks the chain (N4).
- **D10 — CURED.** Line 138: "Code writes it from Amear's item-1 answer as filed in section 2 (C9, REPORTED BY Amear); the line means Amear reports the snapshot taken, not that Code has seen it."

**Citations checked, all resolve:**
- `DECISIONS.md`:1551–1555 is R1. :1830–1834 is C3, :1846–1847 is C9, :1848–1850 is C10, and :1831–1833 is C3 (4).
- Answers file: :3, :14, :23–27, :24–26, :39–40 and :41–43 all match.
- Rulings voice file: :3 and :18–22 match.
- `DECISION_LOG.md`:718 (`2026-11-08T14:02:11Z`) and :743 (`2026-11-08T19:12:30Z`) both read WHO: amear.
- Walkthrough :35, :38 and :39 ("the line after :38") match.
- NT8 windows reference :32 and :156 match, as does limit 13 (:40).

**New findings**

1. **MINOR — wrong citation (§9.5, line 403).** It says rows 1, 2, 3, 8 and row 11's route half are answered by "(C3, C9 …)". C9 answers none of them; it answers only row 9, the snapshot (:363). Rows 1, 2, 3, 8 and 11-route all come from C3.
2. **MINOR — misdescribes row 11 (§8 list, line 364).** It says: "The `pip` half is unchanged and stays **Amear's**, as the row says." Row 11 (:352) actually says "`pip` half settled by his words — "(11) pip may download only the bridge's pinned requirements…"". Only the sub-question about base-package dependencies and `setuptools` is Amear's.
3. **MINOR — stale analogy not listed in the §0 amendment line (line 385, §9.2).** "How the file reaches the VM, and who installs and compiles it in NT8: **Amear's** (like step-0 items 2 and 6)." Items 2 and 6 are now answered, so "like" implies an open question that no longer exists.
4. **MINOR — the D9 chain is missing in the other file (walkthrough :39).** It reads "his words (C3 (4)): … (verbatim … WHO: amear)" without "REPORTED BY the Claude.ai channel and pasted by Amear".
5. **MINOR — header not updated (line 7, and line 22's place list).** Line 7 still reads only "Amended 2026-11-07 (amendment 1 …)", with no mention of amendment 2. Line 22 also never says that the amendment appended a line to the walkthrough file (:39).
6. **MINOR — STOP path differs from §7 (item 0, line 105).** When NT8 is not running, item 0 says to set the self-report's `RESULT:` to `STOP` and then `FINISHED`. §7 says "Any STOP: write the STOP reply, then `FINISHED`". Item 0 gives no separate STOP reply.

No file was written, staged or changed.

VERDICT: SURVIVES
````

W2's line numbers are off by one to three in places (it gives §9.5 as 403 and 3.4 as 170; the final file has them at :406 and :185 — see the hunk headers in the final diff). Its pointer results are REPORTED BY W2, as for W1.

### What I did with each W2 finding

| # | Disposition |
|---|---|
| N1 MINOR | Fixed: :406 cites C3 only. |
| N2 MINOR | Fixed: :364 now "The `pip` half is unchanged, as the row says; its open sub-question stays **Amear's**." |
| N3 MINOR | Not changed (same as F2; Open 8). |
| N4 MINOR | Fixed: walkthrough :39 adds "REPORTED BY the Claude.ai channel and pasted by Amear, answers file :3". |
| N5 MINOR | Second half fixed (:22 names the walkthrough append). First half (:7) not changed — see "Not edited, on purpose" above. |
| N6 MINOR | Fixed: :105 says the STOP self-report is the STOP reply of section 7. |

The N-fixes were not re-checked by a third adversary. They are the six edits listed, all visible in the final diff.

## S6 cross-block check

Places C3, C9, C10 and R1 touch, and how each was checked. Both workers read the whole amended file; I read the diff.

- **§1 limit 1 (account).** Amended (:28). C3 (5) "Sim101" matches limit 1's "Sim101 only".
- **§1 limit 3 (no start or restart of NT8; D-071).** Item 0 tells the agent to check, not start; if NT8 is not running, it STOPs (:105). W1 checked this against criterion (c).
- **§1 limits 10, 11, 13.** Item 0 writes nothing except the self-report under `Z:\vm\replies\` (limit 10). It runs inside step 1, after step 1's `STARTED` (limit 11). It changes nothing in NT8 and leaves step 4's row 7 alone (limit 13; :109). C9's "The Claude session on the VM is closed." bears on limit 11 (one-session rule); no line needed changing.
- **Step 1 (opening line, items 6, 7, 9).** The "observe only" line and item 6's "only NT8 window" sentence were amended so that item 0 does not contradict them. Item 0 uses item 7's command. Item 9 now copies §2.
- **Step 2.** Unchanged; it does not depend on step-0 answers.
- **Step 3 gate and 3.1–3.4.** Gate (b) and (c), 3.1, 3.3 and 3.4 amended. 3.2 unchanged: C3 (3) "only the two AddOn files of step 3.2" names the two files 3.2 already copies (W1 checked). 3.5 (pip) unchanged; C3 does not speak to it.
- **Step 4 gate (:209) and the settings table row 7 (:252, "CME US Index Futures RTH").** Unchanged. The gate's "(c) Amear's step-0 words name the sim account (section 2, item 5)" is met by §2's filed "(5) Sim101;". Row 7 names the template that item 0 reads; item 0 forbids changing it.
- **§7 items 5 and 14 (:320, :329).** Unchanged; "Amear's step-0 words" are now the §2 filed answers (named at :22). W2 checked the lines exist.
- **§8.** New settled list; rows not edited; "Still not decided here" unchanged.
- **§9.2 (:385) and §9.5 (:406).** §9.5 amended (F1); §9.2 not (F2).
- **Step-4 skill, `vm/skills/praxis-nt8-bridge-backtest/SKILL.md`:13.** Unchanged; its "Amear's step-0 words name the sim account (handoff section 2, item 5)" now resolves to §2's filed answer.
- **Go-live list, walkthrough :35 and :38.** Unchanged; :39 appended (C3 (4)).
- **Parked unit diq (not touched).** The working-tree values spec :72 (diq's text, not in HEAD: count 0 above) reads "T7 (:193) reads back other settings (commission template, backtest type, fill resolution, slippage), not template hours." Item 0 does not say what R1's "(T7 readback)" names (:96). When diq lands, the master may want to read the two side by side. Nothing here edits either.

## Open — not answered here (S8; listed, not filled in)

1. Whether tests 2b and 2a are "sim tests" in C3 (4)'s sense. The handoff carries it as an INFERRED reading (:72, :138), and step 3's gate (c) relies on it. A master decision under D1 may confirm it; Amear may reverse it.
2. Whether placing R1's "VM step 0" as step 1 item 0, and reading the hours in the Trading Hours window, is what his words mean; and what "(T7 readback)" names. Labelled a reading at :96.
3. If the live template "starts 08:30 ET": what that means for test 2a, an exact-match reproduction on the same template (step 4 row 7). R1 names the 2026-11-01 baselines and the two arms, not 2a. Code decides whether the clause fired (:109); what follows for 2a is not in his words.
4. How the template's time-zone field bears on "08:30 ET" (the rescued copy reads `830` with `Eastern Standard Time`; REPORTED, not live). Code's reading after the VM reply.
5. When, and by what message, Amear tells the VM agent he has compiled (3.3). Not in C3 (6).
6. The STOP when NT8 is not running at item 0 is this file's reading of limit 3 (labelled at :105), not his word.
7. §8 row 11's open `pip` sub-question (base-package dependencies, `setuptools`) stays Amear's, unchanged.
8. The §9.2 :385 analogy (F2/N3) and the :7 date line (N5) — the master's call.

## Files touched (unstaged)

- `vm/2026-11-06-vm-handoff.md` — ` M` (351 → 406 lines)
- `docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md` — ` M` (38 → 39 lines; one line appended)
- `MANIFEST.md` — ` M` (316 → 319 lines; three rows appended after :316; `head -n 316` sha256 unchanged)
- `docs/reports/2026-11-09-vm-handoff-amendment-2-manager.md` — `??` (new; this report). Its own final line count is not pasted: a count pasted into the file changes nothing, but any later edit would stale it, and the master's index build reads the file as it is.

Nothing staged: the index holds 12 paths, none of them these four (final capture above). Nothing written under `.claude/agent-memory/`. No DECISIONS.md, rubric, hook, agent definition, settings or ledger file touched. No diq file touched.

## Self-grade (the auditor grades; this is not a grade)

- **S1** — every claim about the files rests on pasted output (diff, wc, hash, grep counts, porcelain) or on the workers' returned checks, which are graded REPORTED BY the worker. Self-assessed: met.
- **S2** — the handoff stays "untried"; the snapshot is REPORTED BY Amear; the live template is UNVERIFIED; the menu route is UNVERIFIED on the VM; the rescued template is REPORTED. Self-assessed: met.
- **S4** — no new DECISIONS.md entry (out of scope for this unit). The work follows the master's order on the ledger (DECISION_LOG `2026-11-08T19:12:30Z`: "VM-handoff unit (C3, C9, C10, R1's template read, C3(4) go-live line)") and D8(3). The readings in Open 1, 2 and 6 are labelled in the file. If the master judges any of them a deviation from the plan, it needs a DECISIONS.md entry before the commit. Self-assessed: met, with that caveat.
- **S5** — authority is cited to ledger rows `2026-11-08T19:12:30Z` and `2026-11-08T14:02:11Z` (WHO: amear); both are in HEAD (W1's check). No in-session approval is used. Self-assessed: met.
- **S6** — the section above names each block touched and how it was checked. Self-assessed: met.
- **S8** — only C3, C9, C10 and R1 words are written as his; every reading is labelled; open items are listed, not filled in. Self-assessed: met.
- **S13** — this report carries the standing limitation sentence once (count pasted above). The handoff still carries it once (:9; count in the final capture); no second copy was added. Self-assessed: met.

Result: PASS (self-assessed, for the auditor to grade). W1 REFUTED the first state; after the fixes, W2 SURVIVES; the six N-fixes were not re-checked by a third adversary.
