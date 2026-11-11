# 2026-11-10-vm-agent-hermes-ssh — worker 4 (ADVERSARIAL re-check)

## Task
Re-check, after worker 3's fixes, the CODE- reply draft (scratchpad `CODE-vm-agent-hermes.draft.md`), handoff Amendment 3 (`vm/2026-11-06-vm-handoff.md`:23), DECISIONS.md D-2026-11-10-C (:2075–2099) and MANIFEST.md rows 364–371. A: is each of F1–F13 closed. B: a fresh walk through steps 1–4 and §7 as Hermes would read them. C: hygiene and citations.

## Mode
ADVERSARIAL. I edited no file except this report. I ran no ssh, no vmps.sh (I only read its text with grep), no curl, no git write. Nothing under ~/.hermes was edited.

## Criterion
specs/SPEC_RUBRIC.md S1, S2, S4, S5, S6, S8, S13 (verbatim in the brief).

## Process log
1. Read the draft (63 lines), the Amendment 3 diff, the DECISIONS entry, the Hermes skill, handoff §0–§7 (:1–330), both VM skills and `vm/replies/README.md`.
2. Spot-checked citations with sed (pasted below).
3. Grepped all four artifacts for IPs, key paths, fingerprints, user@host. Counted the S13 sentence. Checked that every diff is additions only. Checked that DECISIONS 1–2074 match HEAD.
4. Walked Hermes through step 1 (T4(a) order, NT8-not-running path, mismatch path), step 2 (reporter skill), step 3 (3.1–3.5), step 4 (4.2–4.6 plus the backtest skill) and §7.

## A. Closure check (F1–F13). All 13 are CLOSED.

| F | Closed by (draft line, quoted) |
|---|---|
| F1 3.3 screen-STOP vs hand-compile | :39 T2(d): "That is quoting Amear, not a read Hermes makes from an NT8 window, so the skill's screen-STOP rule does not fire on 3.3 (master's reading under D1, changeable by Amear). Step 3.3's own STOP on compile errors stands." Also :36: "Step 3.3 needs no amendment, because it is not a read Hermes makes from an NT8 window (T2(d))." |
| F2 one-session rule in one direction only | :54 T5(a): "Before writing STARTED, Hermes checks that no Code session it started (timer or resume) is still running on this repo. If one is, it waits for that run to end, or tells Amear and stops. … A Code session that finds a `*-STATUS.md` holding STARTED newer than its own start dispatches nothing more and closes." |
| F3 fresh shell, folder and venv | :44 T3(b): "`Set-Location C:\praxis\bridge-src; ` for step 3.5's `python --version` and for step 4.5 … `C:\praxis\bridge-src\.venv\Scripts\python -m nt8bridge ntstatus` … No venv is created outside `C:\praxis\` (ruling 7(11), DECISIONS.md:1231)" |
| F4 which clock gives `<ts>` | :45 T3(c): "`<ts>` may come from the Mac's `date -u …` (the skill) or from the VM's PowerShell (handoff §1) … Each reply says which it used." (See finding 2 for what is left open.) |
| F5 Hermes might not read Amendment 3 | :32 T1(b): "At the start of every run, Hermes reads handoff §0 Amendment 3 (:23) and this reply, as well as §1, §7 and the step it is on." |
| F6 copied skills persist with no gate | :33 T1(c): "Hermes uses a copied VM skill only inside a `praxis-vm-over-ssh` run, under that skill's gates 1–4; never on its own and never from cron … Whether they stay there is Amear's call." |
| F7 4.3 set-up not labelled | :35: "step 4.3 tab set-up (set-up: master's reading under D1, changeable by Amear; his 20:42Z words name the reads)" |
| F8 settlement 7 changed but not named | :35: "item 6 changes settlement 7 (DECISIONS.md:1090, "VM agent reads and reports the NT8 version") by Amear's own 20:42Z words". Also DECISIONS :2085. |
| F9 a later go-2a vs T2 | :40 T2(e): "A later CODE-go-2a reply's words on step 4.3 govern over T2(d) and T2(e); whatever it says, every read Amear's 20:42Z words name (Strategy Analyzer, Commissions) stays with Amear" |
| F10 no §1 carve-out in Amendment 3 | handoff :23: "they govern for Hermes, except that no term relaxes a §1 hard limit." |
| F11 "outside the build loop" attributed to Amear | :61: "(master's filing note in the DECISION_LOG 2026-11-10T20:42:00Z row, which reads "set up outside this session"; UNVERIFIED by Code)". DECISIONS :2085 says the same. The quote is in DL:813 (1 hit, below). |
| F12 tunnel claim not hedged | DECISIONS :2085 "are UNVERIFIED by Code"; :2095 "If the tunnel works as REPORTED BY Amear" and "(this entry's inference)". |
| F13 D2(d) citation | DECISIONS :2085 "`specs/SPEC_RUBRIC.md`:446–447; DECISIONS.md:1912–1916". Checked: rubric 446 "(d) installing keys," and 447 "permissions."; DECISIONS 1912 "D2 Only four things…" and 1916 "permissions. Everything else is D1." |

## B. Fresh attack: findings

### Finding 1 — MINOR. Step 4.5 "Record both" asks for a Help → About read that no term covers. This sets up a DONE-vs-STOP clash on 2a-result.
- Handoff :284: "Whether that string equals the build Help → About shows is UNVERIFIED (`report:2962`). Record both."
- Draft :36 T2(a): "This reply amends the skill's screen-STOP rule for those two items only; everywhere else the skill's rule stands." Draft :40 T2(e): "Until it says otherwise, the skill's screen rule stands in step 4." T2's list (:35) names Help → About only for step 1 item 6.
- Hermes skill :60–64: any NT8-window read (Help → About is named) goes "under `## Could not do` … Then finish the step with `RESULT: STOP`."
- Backtest skill (`vm/skills/praxis-nt8-bridge-backtest/SKILL.md`:40): "with `RESULT: DONE` and a line `2a-NUMBERS: …`".
- Effect: unless go-2a says otherwise, Hermes either ends test 2a's reply as STOP even when the numbers pass, or treats this as a disagreement between the skill and the handoff and stops. Either way it fails safe: no limit is broken and no Amear item is decided. T2(e)'s "Until it says otherwise" lets go-2a settle it. That is why this is MINOR. It is the same kind of gap as F1, though, and nothing tells go-2a to cover it.
- Fix text: append to T2(e): "Step 4.5's "Record both" means, for Hermes: record `ntVersion` from `ntstatus`; the Help → About value is Amear's (T2, item 6) and goes under `## Could not do` with the T2(a) reason. That alone does not make RESULT STOP (master's reading under D1, changeable by Amear)."

### Finding 2 — MINOR. T3(c) leaves step 2's `<ts>` open, but the reporter skill fixes it.
- `vm/skills/praxis-vm-reporter/SKILL.md`:23: "5. `(Get-Date).ToUniversalTime().ToString("yyyyMMdd'T'HHmmss'Z'")` — this is `<ts>`." Handoff :129: "Perform the skill's job exactly as it is written". T3(c) (:45) allows either clock "the skill" (Hermes's) or the VM. T3(a) settles the reporter's Z: paths, but nothing settles its `<ts>`.
- Effect: if Hermes names 2b-skill-job with the Mac clock, Code could grade 2b against "exactly as it is written".
- Fix text: add to T3(c): "In step 2, `<ts>` for `<ts>-2b-skill-job.md` and its `UTC:` line is the output of the reporter skill's command 5."

### Finding 3 — MINOR. T1(c)'s "exactly one file each" leaves out the folder the copy needs, and a re-run of step 2 deadlocks.
- Draft :33: "Hermes may write exactly one file each, the copy of that step's SKILL.md, into the skills directory … in the layout it reported … If a file of that name is already there, STOP and reply; do not overwrite it."
- A `<dir>/<name>/SKILL.md` layout needs a new `<name>` folder. If Code asks for step 2 again after a 2b FAIL, the copy is already there, so Hermes STOPs and only Amear can clear it. Both outcomes fail safe.
- Fix text: "…exactly one file each (and the folder the reported layout needs for it)…; if step 2 is re-run on Code's word, an identical existing copy (same SHA-256 as the Mac source) is used as is, not re-copied."

### Finding 4 — MINOR. T5(a)'s rule for Code sessions lives only in a vm/replies file.
- Draft :54: "A Code session that finds a `*-STATUS.md` holding STARTED newer than its own start dispatches nothing more and closes." DECISIONS :2087 carries T5(a) only for Hermes ("no Code session Hermes started may still be running when it writes STARTED"). The Code-side half is not in the entry and not in HANDOFF.md, which is what timer runs read (DECISIONS.md:1976). DECISIONS.md:1993 (each timer run "checks for a live session on the tree and exits") may not see a Hermes-over-SSH session, which is not a process with this tree as its cwd. INFERRED; not tested.
- Fix text (DECISIONS :2087, after "when it writes STARTED"): "; and a Code session that finds a `*-STATUS.md` holding STARTED newer than its own start dispatches nothing more and closes".

### Checked and found sound (no break)
- T3(b) vs limit 10: `Set-Location` and calling python by full path write nothing. Limit 10 (:38) is about writes only.
- T5(a) vs gate 2: T5(a) adds a question "Alongside" gate 2 and removes nothing. Gate 2's FINISHED-or-none check still applies.
- T4(a)/(b)/(c) vs item 0 (:106): the order keeps "Do this first, before items 1–9". The NT8-not-running path still ends STOP → FINISHED → wait. T4(b) and T6(a) carry item 10 through consistently.
- T2(a) DONE path: an error on item 10 counts as "answered" (T6: "reported, not judged"). Item 5's missing git is not a STOP in step 1 (:116).
- T2(d)'s "does not write a screen value" vs 4.3 "you record what is read" (:271) and backtest skill :31/:40: there is a clash, but T2(e) gives go-2a precedence on 4.3 and the screen rule stands until it speaks. Go-2a gates step 4 (:210), so this fails safe.
- Precedence: no term relaxes a §1 limit. T1(c) stays inside limit 10's own allowance. T6's GET is named by a CODE- reply, as skill :103–106 requires, and no §1 limit covers network reads.
- S8: no D2 item is decided beyond the labelled D2(d) reading of Amear's grant (DL:813 says the same). The 4.3 set-up is D1, not D2 (rubric :443–447), and it is labelled. No Amear read is filled in (:61).

## C. Hygiene and verification evidence (pasted)

S13 counts, IP and key grep, minus-lines, DECISIONS prefix, DL line count:
```
== CODE-vm-agent-hermes.draft.md: S13=1 IPs:
56:127.0.0.1
== w4-entry.txt: S13=1 IPs:
8:127.0.0.1
== w4-am3.txt: S13=0 IPs:
== w4-man.txt: S13=0 IPs:
== diff minus lines:
0
== DECISIONS 1-2074 vs HEAD:
IDENTICAL
    2074
== DL at HEAD:
     810
== handoff S13 in diff:
0
```
(The grep for `.ssh|praxis_vm|SHA256:|fingerprint|user amear|amear@|@praxis-vm|192.168` printed nothing for all four files.)

Numstat (additions only; Amendment 3 is +1/-0):
```
25	0	DECISIONS.md
16	0	MANIFEST.md
1	0	vm/2026-11-06-vm-handoff.md
```
MANIFEST hunks: `@@ -306,0 +307,8 @@` (not this unit's) and `@@ -355,0 +364,8 @@` (this unit's rows 364–371).

Quote checks:
```
DECISIONS quote: EXACT substring of DL:813
DL hits for [If you accept, write a CODE- r]: 1
DL hits for [set up outside this session]: 1
1   (handoff: "the two SKILL.md copies into your skills directory (steps 2 and 4)")
1   (skill: "the file's wording wins")
1   (DECISIONS:1090 "VM agent reads and reports the NT8 version")
1   (handoff:173 "If he does it by hand")
```

Citation spot-checks (sed -n; 20 checked, all point where they say):
```
--- D:1086  | 3 — "the VM's Cowork agent" | none given | The master adopts a working definition: the Claude agent running inside the Windows VM …
--- D:1090  | 7 — who reads the NT8 version | "VM agent reads and reports the NT8 version" | …
--- D:1092  | 9 — VM agent on Z: | "VM agent on Z: while Code runs = second session, coordinate" | …
--- D:1231  7. Bridge items: (4) playbackrun/… (11) pip may download only the bridge's pinned requirements, into its own venv under C:\praxis\. …
--- D:2047  ## 2026-11-10 — D-2026-11-10-B: live-signal topology adopted as the working design …
--- D:1907  D1  Default-decide. …
--- D:1919  D4  Loop: a Hermes timer starts a fresh Code session every four hours.
--- D:1912  D2  Only four things stop and wait for Amear's word: (a) spending
--- D:1916      permissions. Everything else is D1.
--- D:1230  6. Strategy Analyzer tab: a hand-set tab may be used for 2a and counts as "bridge reproduces the baseline". …
--- topology:78  … So option 1 is recommended, and option 3 is the fallback
--- topology:89  | B4 | n8n down or Redis unreachable. | …
--- topology:90  | B5 | Anything that can POST to the webhook. | … **waits for Amear (D2(d))** …
--- topology:98  | OPEN-T1 | Can an NT8 strategy in the VM reach the Mac's n8n webhook over HTTP? | …
--- W:27  - [ ] before real money: isolate the VM — remove the shared folder …
--- W:35  - [ ] **Go-live checklist, his words:** "unmap Z: and turn the share off before real money" …
--- W:38  - [ ] **Go-live checklist addendum 2026-11-07, his words (ruling 10):** "remove the unauthenticated bridge request folders …
--- W:39  - [ ] **Go-live checklist addendum 2026-11-09, his words (C3 (4)):** …
--- DL:813  [2026-11-10T20:42:00Z] WHO: amear | WHAT: **Amear proposes Hermes over SSH as the VM agent …
--- DL:814  [2026-11-10T20:43:00Z] WHO: praxis-master | WHAT: **Accept Hermes over SSH as the VM agent, decided by master under D-2026-11-08-D D1 …
```
Handoff :8 (Z: = repo root INFERRED), :23 (Amendment 3), :91 (step 1), :125 (step 2), :241 (4.3) and :284 (4.5 "Record both") were read in full above. Rubric :446–447 is the D2(d) text, read with sed :436–450.

## Files staged
None. I wrote this report only; I did not stage it.

## Result
Result: PASS. No finding is blocking. All of F1–F13 are closed. Findings 1–4 are MINOR, and each comes with fix text. Finding 1 is the one most worth fixing before step 4.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
