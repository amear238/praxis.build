# Unit 2026-11-10-vm-agent-hermes-ssh — worker 3 (BUILD, fix)

## Task
Apply the manager's decisions on worker 2's findings (`docs/reports/2026-11-10-vm-agent-hermes-ssh-worker2.md`, F1–F15) to four artifacts. (1) The CODE- reply draft, `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/af9aea76-b226-4610-b3fb-538269d1a642/scratchpad/CODE-vm-agent-hermes.draft.md`. (2) The handoff Amendment 3 bullet, `vm/2026-11-06-vm-handoff.md:23`. (3) The uncommitted D-2026-11-10-C entry, `DECISIONS.md:2075–2099`. (4) This unit's MANIFEST rows, plus two appended rows.

## Mode
BUILD (fix). No git add, commit, stash, reset or checkout. No ssh, vmps.sh, curl, VM or n8n contact. `~/.hermes` was read only and not edited. The reply was not placed in `vm/replies/`. All `__TS__` placeholders were kept.

## Criterion
specs/SPEC_RUBRIC.md S1, S2, S4, S5, S6 and S8, plus the S13 standing sentence, as set in the brief. The constraints:
- Handoff diff: +1/−0.
- DECISIONS.md: lines 1–2074 byte-identical to HEAD, additions only.
- MANIFEST: nothing above :364 changes.
- S13: the sentence appears once as the last line of the draft and once as the last line of the entry, and not in Amendment 3.
- No non-loopback IP, no key path, no fingerprint, no username paired with the host, and no title for breaker #5.

## Process log
1. Read the worker 2 report, the draft (61 lines), Hermes's skill (read-only, 130 lines), both `vm/skills/*/SKILL.md`, and handoff §1 (:25–43), §5 3.3–3.5 (:172–206) and §6 4.3–4.5 (:241–288).
2. Checked citations with sed -n / grep -n:
   - DECISIONS.md:1090 is settlement 7 ("| 7 — who reads the NT8 version | "VM agent reads and reports the NT8 version" | The VM agent reads and reports it; Code records it.").
   - DECISIONS.md:1912–1916 is D2, with "(d) installing keys, credentials or agent" at :1915 and "permissions." at :1916.
   - DECISIONS.md:1231 holds ruling 7(11), "(11) pip may download only the bridge's pinned requirements, into its own venv under C:\praxis\.".
   - Handoff 3.3's by-hand path is at :173, and its STOP on compile errors at :176.
   - DECISION_LOG.md:813's closing quote mark comes before the words "The SSH key, firewall rule and tunnel were set up outside this session; the master installed nothing." So that sentence is the master's filing note, not Amear's words.
3. Backed up the draft to `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/af9aea76-b226-4610-b3fb-538269d1a642/scratchpad/CODE-vm-agent-hermes.draft.pre-worker3.md`, then edited it with Edit. The draft went from 61 to 63 lines; the two new lines are T3(c) and T5(a).
4. Edited the Amendment 3 bullet in place with Edit, and the entry in place with Edit and one `sed -i ''`. The entry's line count is unchanged (DECISIONS.md is still 2099 lines, heading at :2076), so the MANIFEST DECISIONS row's range "2075-2099 (heading :2076)" is still correct.
5. MANIFEST: re-read rows :364–369. None became wrong; the descriptions summarise and do not list the sub-points. Left them unchanged and appended two rows with `>>`.
6. Ran the verification commands below.

## Each finding → what changed

**F1 (BLOCKING): T2(a) and T2(d) disagreed on step 3.3.** T2(a)'s amendment was not widened, and its "for those two items only" is kept. T2(a) now ends with:
> "Step 3.3 needs no amendment, because it is not a read Hermes makes from an NT8 window (T2(d))."

T2(d) now reads:
> "Amear's screen reads in step 1 and step 4 reach Code from Amear, and Code files them as his. Hermes does not write a screen value on his behalf. Step 3.3 keeps the handoff's own path ("If he does it by hand", handoff 3.3): Amear presses Compile and tells Hermes the result; Hermes waits, does nothing in NT8, and pastes his words, word for word, and the result he gives (clean, or the error lines). That is quoting Amear, not a read Hermes makes from an NT8 window, so the skill's screen-STOP rule does not fire on 3.3 (master's reading under D1, changeable by Amear). Step 3.3's own STOP on compile errors stands."

The words "in step 1 and step 4" were added so that T2(d)'s first sentence does not clash with Hermes pasting Amear's 3.3 words.

**F2 (BLOCKING): one-session rule, the other direction.** New sub-point after T5:
> "**T5(a) The other direction** (master's reading under D1, changeable by Amear). Before writing STARTED, Hermes checks that no Code session it started (timer or resume) is still running on this repo. If one is, it waits for that run to end, or tells Amear and stops. Alongside the skill's gate-2 question, Hermes also asks Amear to confirm that no other Code session is working on this repo. A Code session that finds a `*-STATUS.md` holding STARTED newer than its own start dispatches nothing more and closes."

**F3 (BLOCKING): fresh shell — working folder and venv.** T3(b) now reads:
> "Each command to the VM goes through the skill's helper and runs in a fresh PowerShell, so any state a command depends on is set in the same call. Where a step or skill command uses `$D` set by an earlier command, Hermes puts `$D = [Environment]::GetFolderPath('MyDocuments'); ` in front of it. Where a step runs a command "from" or "in" a folder, Hermes puts `Set-Location <the full folder the step names>; ` in front of it (for example `Set-Location C:\praxis\bridge-src; ` for step 3.5's `python --version` and for step 4.5). Where a step says "venv active", Hermes calls the venv's python by its full path under `C:\praxis\` in place of activation (for example `C:\praxis\bridge-src\.venv\Scripts\python -m nt8bridge ntstatus`). Nothing else in the command changes. Hermes pastes the command exactly as sent, wrapper included. Code and praxis-auditor judge step 2 against what was sent. Code's later CODE-cli-setup and CODE-go-2a replies write every path in full. No venv is created outside `C:\praxis\` (ruling 7(11), DECISIONS.md:1231), and no file is written outside what handoff §1 limit 10 names. The folder the SSH shell starts in is UNVERIFIED."

*Deviation from the brief's wording, flagged for the manager.* The brief's text was "no venv or file is created outside `C:\praxis\`". Taken literally, that contradicts steps 3.2 and 3.4 and limit 10. Step 3.2 copies two AddOn files into `Documents\NinjaTrader 8\bin\Custom\AddOns`, and the bridge commands write under `Documents\NinjaTrader 8\NT8Bridge\`; limit 10 (handoff :38) names both. So the sentence was split: venv → `C:\praxis\` (ruling 7(11)), and files → whatever limit 10 names. Same intent, without the contradiction.

**F4: the `<ts>` clock.** New sub-point:
> "**T3(c) `<ts>`** (master's reading under D1, changeable by Amear). `<ts>` may come from the Mac's `date -u +%Y%m%dT%H%M%SZ` (the skill) or from the VM's PowerShell (handoff §1); both are UTC in the same format. Each reply says which it used. This is not a disagreement to stop on."

**F5: read Amendment 3 at the start of every run.** Appended to T1(b), which already carries the master's label:
> "At the start of every run, Hermes reads handoff §0 Amendment 3 (:23) and this reply, as well as §1, §7 and the step it is on."

**F6: the copied skills persist.** Appended to T1(c), which already carries the master's label:
> "Hermes uses a copied VM skill only inside a `praxis-vm-over-ssh` run, under that skill's gates 1–4; never on its own and never from cron. In its end-of-run message it tells Amear the copies are in its skills directory. Whether they stay there is Amear's call."

In the entry's last S6 bullet:
> "...allows exactly those two copies and widens nothing else in the write set; the copies persist in Hermes's skills directory (T1(c))."

The same bullet now says "joined by T5 and T5(a)".

**F7: step 4.3 tab set-up was not labelled.** T2's opening line now reads:
> "step 4.3 tab set-up (set-up: master's reading under D1, changeable by Amear; his 20:42Z words name the reads), the tab read-back and the PRAXIS commission read-back."

**F8: settlement 7 was not named.** Verified at :1090 (process log, step 2). Added to the T2 opening paragraph:
> "For Hermes, item 6 changes settlement 7 (DECISIONS.md:1090, "VM agent reads and reports the NT8 version") by Amear's own 20:42Z words: the Help → About read is his. T2(b)'s file version is extra information only."

Added to the entry, after the D2(d) sentence:
> "Settlement 7 (DECISIONS.md:1090, "VM agent reads and reports the NT8 version") changes for Hermes by Amear's own 20:42Z words: the Help → About read is his; the reply's T2(b) file version is extra information only."

**F9: which wins at step 4.3, a later go-2a reply or T2.** Appended to T2(e):
> "A later CODE-go-2a reply's words on step 4.3 govern over T2(d) and T2(e); whatever it says, every read Amear's 20:42Z words name (Strategy Analyzer, Commissions) stays with Amear (master's reading under D1, changeable by Amear)."

**F10: Amendment 3 had no §1 carve-out.** The bullet at :23, changed in place (still +1/−0 against HEAD):
> "...where they differ from the text above or below, they govern for Hermes, except that no term relaxes a §1 hard limit. Authority: ..."

**F11: "set up outside the build loop" was attributed to Amear.** The draft's "What this reply does not do" now reads:
> "the SSH key, the firewall rule and the tunnel were set up outside the build loop (master's filing note in the DECISION_LOG 2026-11-10T20:42:00Z row, which reads "set up outside this session"; UNVERIFIED by Code)."

The quoted "set up outside this session" was added because the note's own words say "this session", not "the build loop"; the brief's wording is kept. The entry carried the same problem: it cited ":813" with no label. It now reads:
> "...UNVERIFIED by Code; the master installed nothing (master's filing note in DECISION_LOG.md:813, after Amear's quoted words; it reads "set up outside this session")."

**F12: unhedged tunnel claim.** In the entry's Block 3 bullet:
> "If the tunnel works as REPORTED BY Amear, it is also a route by which something on the VM can POST to the webhook, the B5 row (:90)..."

**F13: imprecise citation.** Verified with grep -n (:1912–1916). In the entry: "DECISIONS.md:1912" → "DECISIONS.md:1912–1916".

**F14: no action.** This is the manager's placement and placeholder hazard. All seven `__TS__` are kept (see V6).

**F15: nothing done.** It is out of scope, as directed.

**Entry "What it decides" (updated by pointer).** T5 now reads:
> "T5 the one-session rule binds Hermes's four-hour Code timer (D4, DECISIONS.md:1919), and T5(a) no Code session Hermes started may still be running when it writes STARTED"

The sub-point list now reads:
> "(step 1 order, the skills-directory copies and their use only under the skill's gates, intended differences against the skill's stop-on-disagreement rule, reading Amendment 3 at the start of every run, the item 1 answer, item 8's overlap with T4, Z: paths inside the two VM skills, one fresh shell per command with folder and venv paths in full, which clock gives `<ts>`, who sets the step 4.3 tab, step 3.3 not being a screen read, a later go-2a reply's precedence on step 4.3, Code sessions still running before STARTED)"

The "How sure" UNVERIFIED list gains "the folder the SSH shell starts in (T3(b))".

**MANIFEST.** Rows :364–369 are unchanged; they are still accurate. Two rows were appended at :370–371:
- `/docs/reports/2026-11-10-vm-agent-hermes-ssh-worker3.md` (BUILD fix)
- `/docs/reports/2026-11-10-vm-agent-hermes-ssh-worker4.md` (ADVERSARIAL re-check)

Both say "ungraded at time of row".

### Residual (not fixed, reported)
- T5(a) says Hermes "checks" that no Code session it started is still running. How it checks (process list, the timer's own state) is not named, and is UNVERIFIED. It is a Hermes-side mechanism that this unit cannot see.
- `scratchpad/s13.txt` holds the S13 pattern used by the greps. It is a scratch file, not a project file.

## Verification evidence (pasted command output)

V1. Diff numstat:
```
$ git diff --numstat -- vm/2026-11-06-vm-handoff.md DECISIONS.md MANIFEST.md
25	0	DECISIONS.md
16	0	MANIFEST.md
1	0	vm/2026-11-06-vm-handoff.md
```
(MANIFEST +16 = the 8 rows from before this unit, plus this unit's 6, plus the 2 appended now.)

V2. Hunk headers and deletions:
```
$ git diff DECISIONS.md | grep -c "^-[^-]"
0
$ git diff MANIFEST.md | grep "^@@"; git diff vm/2026-11-06-vm-handoff.md | grep "^@@"
@@ -304,6 +304,14 @@
@@ -353,3 +361,11 @@
@@ -20,6 +20,7 @@
```

V3. Staged files:
```
$ git diff --cached --name-only
docs/reports/evidence/2026-10-28-mffu-<rep>-reply.png
```
(That file was staged before this unit. This worker staged nothing.)

V4. Draft header:
```
$ head -4 draft
REPLY-TO: Amear's 2026-11-10 proposal (DECISION_LOG 2026-11-10T20:42:00Z, WHO: amear) and Z:\vm\2026-11-06-vm-handoff.md §0 settlement 3
WRITTEN-BY: Claude Code on the Mac (praxis-master, through unit 2026-11-10-vm-agent-hermes-ssh)
UTC: __TS__
RESULT: DONE
```

V5. Amendment 3 and DECISIONS prefix:
```
$ grep -n 'Amendment 3' vm/2026-11-06-vm-handoff.md | cut -c1-120
23:- **Amendment 3 (2026-11-10):** the VM agent is now Hermes, driving the VM over SSH from the Mac (host alias `praxis-
$ cmp <(git show HEAD:DECISIONS.md) <(head -2074 DECISIONS.md) && echo same
same
```

V6. S13 counts, placeholders, IPs and hygiene. The pattern was read from a file so that this block does not repeat the sentence.
```
S13 draft:
1
draft last line is S13:
1
S13 handoff WC:
1
S13 handoff HEAD:
1
S13 Amendment 3 line:
0
S13 entry:          (sed -n '2075,$p' DECISIONS.md | grep -c)
1
entry last line is S13:
1
$ grep -n __TS__ (counts per line shown)
draft:3:__TS__
draft:8:__TS__
draft:8:__TS__
vm/2026-11-06-vm-handoff.md:23:__TS__
vm/2026-11-06-vm-handoff.md:23:__TS__
MANIFEST.md:364:__TS__
DECISIONS.md:2087:__TS__
$ IP grep draft
   2 127.0.0.1
$ IP grep entry
   1 127.0.0.1
$ IP grep Amendment 3
0
$ hygiene: key path / fingerprint / user@host / launchctl / helper / breaker 5
```
(The hygiene grep, `\.ssh|SHA256:|amear@|@praxis|launchctl|vmps|tunnel\.plist|#5|breaker 5` over the draft, the entry, Amendment 3 and MANIFEST :364–end, printed nothing.)

## Files staged
None. Per the brief, the following are left unstaged for the manager:
- the edited draft (scratchpad)
- `vm/2026-11-06-vm-handoff.md` (Amendment 3 bullet only)
- `DECISIONS.md` (entry :2075–2099 only)
- `MANIFEST.md` (rows :370–371 appended)
- this report

## Result
All of F1–F13 are applied as the manager decided. F14 and F15 needed no action. There is one flagged wording deviation in F3, which avoids a contradiction with limit 10. Every constraint check passes.

Result: PASS

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
