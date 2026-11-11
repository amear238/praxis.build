# Unit 2026-11-10-vm-agent-hermes-ssh — worker 2 (ADVERSARIAL)

## Task
Try to break four artifacts: (1) the CODE- reply draft `scratchpad/CODE-vm-agent-hermes.draft.md` (`__TS__` placeholder; full path `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/af9aea76-b226-4610-b3fb-538269d1a642/scratchpad/CODE-vm-agent-hermes.draft.md`); (2) handoff Amendment 3, `vm/2026-11-06-vm-handoff.md:23`; (3) DECISIONS.md D-2026-11-10-C, :2075–2099; (4) MANIFEST.md :364–369. The test: walk handoff steps 1–4 and §7 the way Hermes would, reading its skill `~/.hermes/skills/devops/praxis-vm-over-ssh/SKILL.md`, the handoff, the draft and `vm/skills/*/SKILL.md`.

## Mode
ADVERSARIAL. Read-only. The only file written is this report. No git add/commit/stash/reset/checkout. No ssh, no vmps.sh, no curl, no VM or n8n contact. `~/.hermes` was read and not edited.

## Criterion
specs/SPEC_RUBRIC.md S1, S2, S4, S5, S6, S8, plus the S13 standing sentence. Spec for the artifacts as in the brief (T1–T7, Amendment 3, entry layout).

## Process log
1. Read the draft (61 lines), the handoff diff, DECISION_LOG :805–814, the Hermes skill (130 lines), the handoff in full (407 lines), both `vm/skills/*/SKILL.md`, `vm/replies/README.md`, DECISIONS :2040–2099.
2. Checked every citation in the draft and in the entry with `sed -n`.
3. Checked that the entry's Amear quote matches DECISION_LOG :813 character for character (python, `in` test).
4. Ran append-only checks (numstat, hunk headers), S13 counts and hygiene greps.
5. Walked steps 1→4 as Hermes. Findings follow.

## Findings

### BLOCKING

**F1. T2(a) and T2(d) contradict each other on step 3.3. Step 3 ends in a STOP with nothing defined to resume it.** Draft :35 lists "step 3.3 compile" among Amear's screen reads. Draft :36 (T2(a)) amends the skill's screen-STOP rule "for those two items only; everywhere else the skill's rule stands". The skill's rule, at skill :60–64, says anything a step reads from NT8's windows goes under `## Could not do` and the step ends `RESULT: STOP`. Draft :39 (T2(d)) says the reverse: "Step 3.3 keeps the handoff's own path: Hermes waits … and pastes his words". So for step 3.3, one term of the reply says STOP and another says continue. The skill's own tie-break is "When in doubt, STOP" (skill :15). The §7 order (:316–333) has no CODE- reply between `install.md` and `STOP-pip.md`, so a 3.3 STOP leaves 3.4 and 3.5 stranded with no named file to resume them.
Evidence (draft):
```
36	- **T2(a) Step 1 only.** ... This reply amends the skill's screen-STOP rule for those two items only; everywhere else the skill's rule stands.
39	- **T2(d) Who files them.** ... Step 3.3 keeps the handoff's own path: Hermes waits, does nothing in NT8, and pastes his words when he tells it he has compiled.
```
Skill :60–64: "Anything a step reads from NT8's windows (...) goes under `## Could not do` ... Then finish the step with `RESULT: STOP`."
**Fix.** In T2(a), replace the last sentence with: "This reply amends the skill's screen-STOP rule for those two items, and for step 3.3, which follows T2(d) and is not on its own a STOP; everywhere else the skill's rule stands." This goes slightly beyond the spec's "those two items only". The master decides it under D1.

**F2. T5 only covers one direction. Nothing stops Hermes from writing STARTED while a Code timer run is already working on the repo.** Draft :52 binds the timer only while a STARTED is the newest STATUS. Hermes's gate 2 (skill :36–39) checks only the STATUS files and the in-VM Claude session. Handoff limit 11 (:39) says "Code starts no agent between those two files", but a Code session that started earlier is not told to look. Amear's own ruling-5 default names exactly this case: "VM agent on Z: while Code runs = second session, coordinate" (DECISIONS.md:1063; settlement 9, :1092). The case is realistic. Today's timer run lasted from 17:01Z to 18:28Z (DECISION_LOG :806, :812), and HANDOFF.md:83 records a Hermes resume-cron agent "running loop commands" during a Code run. If Amear asks Hermes for VM work in such a window, two sessions are open, which breaks §1 limit 11.
**Fix.** Add **T5(a)**: "Before writing STARTED, Hermes checks that no Code session it started (timer or resume) is still running on this repo. If one is, it waits for that run to end, or tells Amear and stops. A Code session that finds a `*-STATUS.md` holding STARTED newer than its own start dispatches nothing more and closes. (Master's reading under D1, changeable by Amear.)"

**F3. T3(b) fixes only `$D`. Working directory and venv activation do not survive a fresh shell either. That leaves step 4.5 impossible to follow as written, and opens a path to writing outside `C:\praxis\`.** Draft :44 allows only the `$D = …;` prefix. Handoff :279 and backtest skill :33 say "From `C:\praxis\bridge-src`, venv active", and the limit-9 fallback `.venv\Scripts\python -m nt8bridge` is a relative path. Each vmps.sh call opens a fresh PowerShell (skill :51), presumably in the SSH user's home. Run as written, `python -m nt8bridge ntstatus` either errors, and backtest skill :36–37 then records 2a as FAIL ("an error … is FAIL"), or Hermes adds an unauthorised `Set-Location`. Step 3.5's commands (README form `python -m venv .venv`, `-e .`, handoff :190–192) are also relative. If `CODE-cli-setup` copies that form, a fresh shell creates the venv in the home folder, outside `C:\praxis\`. That breaks ruling 7(11) ("into its own venv under C:\praxis\", DECISIONS.md:1231) and §1 limit 10 (:38). (Whether the SSH shell starts in the home folder is INFERRED. It is untried.)
**Fix.** Add to T3(b): "Where a step runs commands 'from' a folder or with the venv active, Hermes prefixes `Set-Location C:\praxis\bridge-src; ` and calls `C:\praxis\bridge-src\.venv\Scripts\python` by full path in place of `python`/activation. It names no other change, and pastes the command exactly as sent. CODE-cli-setup writes every path in full." Or, at the least, state that cli-setup and go-2a must carry this.

### MINOR

**F4. The two texts disagree on which clock `<ts>` comes from. Under T1(b) that is an "other disagreement", so Hermes's first write could become a STOP.** Handoff :43: "`<ts>` everywhere means UTC time from PowerShell". Skill :111: "`<ts>` comes from `date -u +%Y%m%dT%H%M%SZ`" (the Mac). Reporter skill :23 also takes `<ts>` from the VM. Draft :32: "Any other disagreement: the skill's rule stands", and the skill's rule is "Stop and tell Amear" (skill :22–23). The failure is safe, but it can block step 1 before STARTED. **Fix:** add **T3(c)**: "`<ts>` may come from the Mac's `date -u +%Y%m%dT%H%M%SZ` or from the VM's PowerShell; both are UTC in the same format. The reply says which. This is not a disagreement to stop on."

**F5. Hermes may never read Amendment 3, and T1(b) cannot by its own force switch off the skill's stop rule.** Skill :20 tells Hermes to read "sections 1 and 7, and the step you are on". Amendment 3 sits in §0 (:23). The skill's "Stop and tell Amear about the disagreement" (:22–23) has no conditions. T1(b) (draft :32) relies on Amendment 3 to neutralise it. The failure is safe (STOP), but the unit's goal, step 1 DONE and then step 2, may not happen. **Fix:** add to T1(b): "At the start of every run, read handoff §0 Amendment 3 (:23) as well as §1, §7 and the step." Editing the skill itself is Amear's to do; it is not this unit's.

**F6. T1(c) widens Hermes's Mac-side writes into its live skills directory, outside the repo, and the copies stay there.** Skill :86–87 says that on the Mac Hermes writes only new files in `vm/replies/`. Draft :33 allows a copy into "the skills directory it reported", which for Hermes is on the Mac (skill path `~/.hermes/skills/…`; `platforms: [macos]`, skill :6). The copied `praxis-nt8-bridge-backtest` carries none of the gates 1–4 in `praxis-vm-over-ssh`: no cron ban, no one-session check, no acceptance check. Once installed it is a second way into an NT8 `backtest` run. DECISIONS :2097 says T1(c) "widens nothing else". That holds for the write set but leaves out persistence. **Fix:** add to T1(c): "Hermes uses a copied VM skill only inside a `praxis-vm-over-ssh` run, under that skill's gates 1–4. In its end-of-run message it tells Amear the copy is in its skills directory; whether it stays is Amear's call." In :2097, change "widens nothing else" to "widens nothing else in the write set; the copies persist in Hermes's skills directory (see T1(c))".

**F7. T2 makes "step 4.3 tab set-up" Amear's without a label.** Amear's 20:42Z words cover reads only: "anything read from NT8's windows (… Strategy Analyzer, Commissions) stays with me" (DECISION_LOG :813). The handoff leaves who sets the tab to go-2a "as Amear decides" (:241, :292; §8 row 10, :352). This is not a D2 item, so it is not an S8 breach under the D2 list. It is the master's reading, though, and it carries no label. **Fix:** draft :35, after "step 4.3 tab set-up", insert "(set-up: master's reading under D1, changeable by Amear; his 20:42Z words name the reads)".

**F8. Settlement 7 is changed but not named (S4/S6).** DECISIONS.md:1090: "| 7 — who reads the NT8 version | "VM agent reads and reports the NT8 version" | The VM agent reads and reports it; Code records it." The handoff's §8 row 6 (:348) says the same. T2 moves the item 6 read to Amear. That is covered by his 20:42Z words, but neither the draft nor the entry names settlement 7 or the ruling-5 default as changed. **Fix:** in the entry, after the settlement 3 sentence (:2085), add: "Settlement 7 (DECISIONS.md:1090, the VM agent reads the NT8 version) changes by Amear's own 20:42Z words for Hermes: the Help → About read is his; T2(b)'s FileVersion is extra information only." Add a matching clause to T2.

**F9. T2(d) and step 4.3 / the backtest skill conflict, and precedence against a later go-2a is not set.** T2(d) says "Hermes does not write a screen value on his behalf" (draft :39). Handoff :271 says "you record what is read, and by whom", and backtest skill :40 requires "the template rows, the 21 settings as read" in the reply. T2(e) leaves step 4 to go-2a, but Amendment 3 says T1–T7 "govern for Hermes", so it is unclear whether a later go-2a can override T2(d). **Fix:** add to T2(e): "go-2a's words on step 4.3 govern over T2(d) and T2(e)."

**F10. Amendment 3's precedence clause has no carve-out for §1.** :23: "where they differ from the text above or below, they govern for Hermes." T1 says every §1 limit binds unchanged, but the general clause would let any sub-point win over §1. **Fix:** change it to "…they govern for Hermes, except that no term relaxes a §1 hard limit."

**F11. Draft :59 attributes "set up outside the build loop" to Amear (S2 label).** Those words come from the master's filing note, which sits after Amear's quoted excerpt in row 813 (output under V5). **Fix:** "the SSH key, the firewall rule and the tunnel were set up outside the build loop (master's filing note, DECISION_LOG 2026-11-10T20:42:00Z; UNVERIFIED by Code)".

**F12. DECISIONS :2095 makes an unhedged claim about the tunnel (S2).** "The tunnel is also a route by which something on the VM can POST to the webhook". The tunnel has not been observed. **Fix:** "If the tunnel works as REPORTED BY Amear, it is also a route by which …".

**F13. Citation imprecision.** DECISIONS :2085 cites "DECISIONS.md:1912" for the quoted D2(d) words. :1912 is D2's first line; the quoted words are at :1915–1916 (output under V2). **Fix:** "DECISIONS.md:1912–1916".

**F14. Placeholder and placement hazard.** `__TS__` occurs 7 times in 4 files: draft 3, handoff :23 twice, DECISIONS 1 (:2087), MANIFEST 1 (:364). DECISIONS.md is append-only, so all of them must be replaced before the first commit, never after. Placing the reply opens Hermes's gate 1 (skill :29–35). It must not be placed before the audit PASS, or Hermes could start on terms nobody has audited.

**F15. Outside the four artifacts (named only).** DECISION_LOG.md:814 carries the skill's host alias and SSH username as a pair, plus the helper name. No IP or key path is in it. It is a file bound for the public repo. Consider "SSH host praxis-vm (user and key per the skill)".

### Checks that found no break
- Header lines 1–4 match the spec exactly (draft :1–4). The file name matches the gate-1 glob `*-CODE-*.md`.
- All seven terms are present in the spec's order. Required wording is present: T2(a) reason text; "untried (UNVERIFIED)" in T4; "/healthz … UNVERIFIED", "no `/webhook` path, no POST", and "Block 3 question, not decided here" in T6; "Never run from cron" in T7.
- Citations all point where they say: DECISIONS.md :1086, :1092, :1230, :1907, :1919, :2047; rubric :446–447; topology :78, :89, :90, :98; walkthrough :26–27, :35, :38, :39; handoff :8, :23, :91, :125, :241; DECISION_LOG :813/:814 (HEAD has 810 lines). The quote of Amear's words in the entry is exact.
- Entry heading and Status match the spec.
- S8: no D2 item is decided. No screen value is filled in. Nothing is spent. No order path is opened. No breaker value is set.
- Hygiene: no non-loopback IP, key path, fingerprint, username@host, launchctl label or helper name in the four artifacts. Circuit breaker #5 is not mentioned.
- S13: the sentence appears once in the draft and once in the new entry, each as the last line. Amendment 3 adds none; the handoff count is 1 at HEAD and 1 in the working copy.
- Append-only: DECISIONS hunk starts at the old line 2072 with 0 deletions. Handoff is +1/−0. MANIFEST is +14/−0 in two hunks. The 8 rows added before this unit (first hunk) cannot be compared with their pre-unit state from git alone; git shows only that no line is deleted.

## Verification evidence (pasted command output)

V1. Append-only:
```
$ git diff --numstat DECISION_LOG.md DECISIONS.md MANIFEST.md vm/2026-11-06-vm-handoff.md
25	0	DECISIONS.md
4	0	DECISION_LOG.md
14	0	MANIFEST.md
1	0	vm/2026-11-06-vm-handoff.md
$ git diff DECISIONS.md | grep '^@@'; git diff MANIFEST.md | grep '^@@'; git diff vm/2026-11-06-vm-handoff.md | grep '^@@'; git show HEAD:DECISIONS.md | wc -l
@@ -2072,3 +2072,28 @@ S13: Fills are optimistic; ...   [hunk-context text truncated here by the reporter to keep the S13 count]
@@ -304,6 +304,14 @@
@@ -353,3 +361,9 @@
@@ -20,6 +20,7 @@
    2074
```

V2. Citations:
```
--- DECISIONS.md:1086
| 3 — "the VM's Cowork agent" | none given | The master adopts a working definition: the Claude agent running inside the Windows VM ...
--- DECISIONS.md:1092
| 9 — VM agent on Z: | "VM agent on Z: while Code runs = second session, coordinate" | It is a second session. Coordinate: Code does not run agents while the VM session writes; ...
--- DECISIONS.md:1907
D1  Default-decide. When a unit or the master reaches a question that
--- DECISIONS.md:1912
D2  Only four things stop and wait for Amear's word: (a) spending
[sed -n 1910,1922p:] ... money is at stake; (d) installing keys, credentials or agent
    permissions. Everything else is D1.
--- DECISIONS.md:1919
D4  Loop: a Hermes timer starts a fresh Code session every four hours.
--- DECISIONS.md:2047
## 2026-11-10 — D-2026-11-10-B: live-signal topology adopted as the working design (rubric F1; bead Praxis_build-1hv)
--- rubric 440-450 (cat -n from 440): 7 → "(d) installing keys, credentials or agent" (=:446), 8 → "permissions. Everything else is D1." (=:447)
--- topo:98
| OPEN-T1 | Can an NT8 strategy in the VM reach the Mac's n8n webhook over HTTP? | ...
--- topo:89
| B4 | n8n down or Redis unreachable. | ...
--- topo:90
| B5 | Anything that can POST to the webhook. | ...
--- walk:27
- [ ] before real money: isolate the VM — remove the shared folder ...
--- walk:35
- [ ] **Go-live checklist, his words:** "unmap Z: and turn the share off before real money" (D-2026-11-06-A item 3).
--- DECISIONS.md:1090
| 7 — who reads the NT8 version | "VM agent reads and reports the NT8 version" | The VM agent reads and reports it; Code records it. | pending: VM agent |
```

V3. Ledger lines and quote:
```
     814 DECISION_LOG.md
- [2026-11-10T20:42:00Z] WHO: amear | WHAT: **Amear proposes Hermes over SSH as 
- [2026-11-10T20:43:00Z] WHO: praxis-master | WHAT: **Accept Hermes over SSH as 
     810
quote in log: True
```

V4. S13 counts (pattern read from a file, so this report does not repeat the sentence) and hygiene:
```
draft=1 entry2075-2099=1 am3=0 handoffHEAD=1 handoffWC=1 draftLast=1 entryLast=1
--- IPs (non-127):
--- key/user/host/fingerprint:
--- #5 / breaker 5:
```
(The three hygiene greps printed nothing.)

V5. Attribution (F11):
```
$ sed -n 813p DECISION_LOG.md | grep -o 'stays closed to the network." The SSH key, firewall rule and tunnel were set up outside this session; the master installed nothing.'
stays closed to the network." The SSH key, firewall rule and tunnel were set up outside this session; the master installed nothing.
```
The closing quote mark comes before "The SSH key …", so that sentence is the master's, not Amear's.

V6. Placeholders, cwd/venv and `<ts>` lines (F3, F4, F14):
```
vm/2026-11-06-vm-handoff.md:1      [lines; :23 holds 2 occurrences]
MANIFEST.md:1
DECISIONS.md:1
draft: 3 occurrences
vm/skills/praxis-nt8-bridge-backtest/SKILL.md:33:5. From `C:\praxis\bridge-src`, venv active (if `Activate.ps1` was blocked, use `.venv\Scri
vm/2026-11-06-vm-handoff.md:279:**4.5 Run — the only two bridge commands permitted.** From `C:\praxis\bridge-src`, venv active (if `Activate
vm/2026-11-06-vm-handoff.md:43:`<ts>` everywhere means UTC time from PowerShell: `(Get-Date).ToUniversalTime().ToString("yyyyMMdd'T'HHmmss'Z'")` — for example `20261107T091500Z`.
~/.hermes/skills/devops/praxis-vm-over-ssh/SKILL.md:111:  where `<ts>` comes from `date -u +%Y%m%dT%H%M%SZ`.
```

V7. F2 support:
```
DECISION_LOG :806 [2026-11-10T17:01:00Z] ... SESSION START, timer run ...
DECISION_LOG :812 [2026-11-10T18:28:00Z] ... F4 GRADING UNIT LANDED ...
HANDOFF.md:83 ... cause UNVERIFIED (the Hermes resume-cron agent was running loop commands at the time; INFERRED candidate).
```

## Files staged
None. This report was written with Write and is not staged. No other file was touched.

## Result
3 BLOCKING (F1, F2, F3), 12 MINOR (F4–F15).

Result: FAIL

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
