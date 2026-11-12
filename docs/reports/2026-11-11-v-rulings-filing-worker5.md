# Unit 2026-11-11-v-rulings-filing — worker 5 report

## Task
Apply fixes 1–13 from the brief to D-2026-11-11-A and D-2026-11-11-B in DECISIONS.md (only lines after 2099) and to this unit's MANIFEST rows.

## Mode
BUILD (fix).

## Criterion
Lines 1–2099 of DECISIONS.md byte-identical to HEAD `d056e91`. Every new or changed quotation copied by script and byte-identical to its cited line (or a joined line pair, labelled). The S13 sentence appears once per entry, as that entry's standalone last line. No identifiers. MANIFEST lines 1–387 unchanged; only :388, :398 and one appended row change.

## Process log
1. Took snapshots: `cp MANIFEST.md /tmp/vrf-manifest-pre5.md`, `cp DECISIONS.md /tmp/vrf-decisions-pre5.md`.
2. Pulled every cited source line by `sed -n`: proposal :79, return-handoff :46 and :53, DECISIONS.md:1740–1748 (A6), :2076–2097 (D-2026-11-10-C, IPv4 masked on display), DECISION_LOG.md:828 and :829, SPEC_RUBRIC.md:446–447 (shown with `od -c`), install reply :1–3, :7–9, :28, handoff :186–215, plus a grep for STOP at :185–230. Checked commit `55979ee` with `git log -1 --format=%B`.
3. Applied all edits with one Python script (`/tmp/vrf5/edit.py`). It builds each quote from its source line at run time and asserts it is a substring of that line, or equal to the joined pair. Each old string had to occur exactly once in the tail after line 2099. The 1–2099 head was written back unchanged. Result: 14 replacements (fix 1 has two parts, fix 4 has two, and fixes 7 and 5 share one replacement).
4. Re-checked quotes by script (`/tmp/vrf5/qcheck.py`), along with the S13 counts, the identifier scan and the git diff.
5. Updated MANIFEST by script (`/tmp/vrf5/manifest.py`) and diffed it against the snapshot.

Notes and deviations (all fixes were applied as written; nothing was refused):
- Fix 7: the brief's text cites "UNVERIFIED (DECISIONS.md:2089)". Line :2089 has "REPORTED BY Amear" and "Not observed: SSH reachability, the tunnel, n8n from the VM side". The word UNVERIFIED on :2089 is about `/healthz`, the T4 form and T3(b), not the tunnel. The tunnel is called "UNVERIFIED by Code" at :2085. The sentence just before it in the same item already cites "(DECISIONS.md:2085, :2089)". I applied the brief's wording and left the gap for worker 6 or the manager.
- Fix 4: the brief's parenthetical is lowercase and has no closing period of its own. The result reads `**F4 stays FROZEN / NOT MET.** (graded NOT MET by the auditor at `55979ee`; not re-graded here). The rubric's …`.
- Fix 1: the first mention keeps the full path `docs/specs/2026-11-10-f2-session-flat-proposal.md`:79. The short name "proposal" is defined in that same sentence, so "proposal :79" cannot be used before it. The sentence starts "It is filed as closing the A6 hold".
- Fix 3, "the brief itself is not on disk": `grep -rlF 'MFFU compliance governs; nothing across the 16:10-18:00 ET close'` finds the string only in DECISIONS.md, DECISION_LOG.md and this unit's worker 1 and worker 3 reports, which copy it. This supports the claim but does not prove a negative.
- Fix 12: handoff step 3.5 runs from :188 to :204 (:206 is the step-3 reply). The "Consequence" STOP is :200 and the "Detection, after the fact" STOP is :201.
- Fix 5: entry A's S6 cross-block (:2168) still mentions "any overnight-holding profile needs its own backtest, return-handoff :53" unquoted, as a cross-block pointer, not as decision text. Left alone because it is out of the fix list.

## Verification evidence

### Before
```
$ grep -n '^## 2026-11-11' DECISIONS.md; wc -l DECISIONS.md
2101:## 2026-11-11 — D-2026-11-11-A: Amear's rulings V1–V7 (Claude.ai channel voice sessions, 2026-11-10) and MFFU's replies. Filed WHO: amear, REPORTED BY the Claude.ai channel.
2170:## 2026-11-11 — D-2026-11-11-B: VM handoff §1 limit 9 lifted by Amear for one install; Python 3.12.10 and git 2.56.0 (ARM64) installed in the VM. Record only. Filed WHO: amear, REPORTED BY the Claude.ai channel.
    2195 DECISIONS.md
```

### After
```
$ grep -n '^## 2026-11-11' DECISIONS.md; wc -l DECISIONS.md
2101:## 2026-11-11 — D-2026-11-11-A: Amear's rulings V1–V7 (Claude.ai channel voice sessions, 2026-11-10) and MFFU's replies. Filed WHO: amear, REPORTED BY the Claude.ai channel.
2172:## 2026-11-11 — D-2026-11-11-B: VM handoff §1 limit 9 lifted by Amear for one install; Python 3.12.10 and git 2.56.0 (ARM64) installed in the VM. Record only. Filed WHO: amear, REPORTED BY the Claude.ai channel.
    2199 DECISIONS.md
```
New ranges: entry A is 2101–2170 (the S13 line at :2170, blank line :2171). Entry B is 2172–2199 (EOF).

### Head unchanged
```
$ git diff HEAD -- DECISIONS.md | grep -c '^-[^-]'
0
$ git diff HEAD -- DECISIONS.md | grep '^@@'
@@ -2097,3 +2097,103 @@ The Mac's Hermes agent can now drive the Windows VM over SSH (host praxis-vm, ke
$ cmp <(head -2099 DECISIONS.md) <(git show HEAD:DECISIONS.md | head -2099) && echo "1-2099 identical to HEAD"
1-2099 identical to HEAD
$ git show HEAD:DECISIONS.md | wc -l
    2099
```
The hunk header starts at 2097 only because of the 3 lines of context. HEAD has 2099 lines, so every added line is at 2100 or later, and no line is removed.

### Source extractions (raw)
```
--- proposal 79
| OPEN-F2-5 | Adoption of Rule F2-1. | Amear's approval under A6; then a DECISIONS.md entry and the amended #4/#5 text in the breaker spec. |
--- rh 46
- Asked: flat by 16:00 ET governs; a position open at 15:00 may stay open until 16:00; no new system entries 16:00–18:00 ET.
--- rh 53
- Channel's proposal, not his explicit word (INFERRED reading of "Having to fuck around" = without rework): firm rules (flat time, overnight holding, other firm limits) live in a per-firm settings profile, MFFU as the first profile, not hard-coded. Any overnight-holding profile needs its own backtest, because current results assume flat every day. Filer: treat the profile design as a proposal for Amear to confirm.
--- A6 lines
$ sed -n '1744,1745p' DECISIONS.md
A6  FLAG 6: R8 starts the breaker PROPOSAL unit. F2's state changes
    when Amear approves the proposed values.
```
DECISION_LOG.md:828 contains "states the combined reading:" (the full line was printed this session; it is the WHO: amear row). DECISION_LOG.md:829 contains "NOT re-decided here (next unit)".
```
$ git log -1 --format=%B 55979ee
docs: F4 comparison of MFFU written replies against the D-2026-11-10-B pattern (D-2026-11-08-D D8 item 5 and D12; master under D1, DECISION_LOG 17:01Z; bead fx4) - no outgoing message describing the pattern is on disk; neither reply names NT8 or Rithmic; F4 graded NOT MET by the auditor, F4 stays FROZEN

Manager report, four worker reports, manifest-manager report, Correction 1 with three reports (audit FAIL 1 on S1 evidence form, cured by append-only sections; one no-result re-audit under R-A, then reduced re-audit PASS). MANIFEST rows for five reports. DECISION_LOG flush through 18:19Z.

Co-Authored-By: Claude Opus 5.5 (noreply address withheld)
```
```
$ S='n8n reachability is settled: an SSH reverse tunnel lets the VM reach the Mac'"'"'s n8n at http://127.0.0.1:5678, and n8n stays closed to the network'; sed -n '2082p' DECISIONS.md | grep -cF "$S"; sed -n '2082p' DECISIONS.md | grep -oE '([0-9]{1,3}\.){3}[0-9]{1,3}'
1
127.0.0.1
$ sed -n '2085p' DECISIONS.md | grep -cF 'for this grant only: Hermes acts as the VM agent over SSH'
1
$ sed -n '2089p' DECISIONS.md | grep -oE 'REPORTED BY Amear|Not observed: [^.]*|UNVERIFIED' ; sed -n '2085p' DECISIONS.md | grep -oE 'UNVERIFIED by Code'
REPORTED BY Amear
Not observed: SSH reachability, the tunnel, n8n from the VM side
UNVERIFIED
UNVERIFIED by Code
--- install reply
[1]
REPLY-TO: Z:\vm\2026-11-06-vm-handoff.md §1 limit 9 (install of Python and git), lifted by Amear for this install
[2]
WRITTEN-BY: Claude (Claude.ai Praxis channel, Cowork session), driving the VM over SSH from the Mac (host praxis-vm), commands run from the Mac via osascript
[28]
- **Architecture (UNVERIFIED risk for step 3.5):** the VM is Windows on ARM64 and winget installed the ARM64 builds. Whether the bridge's dependencies (notably `pyarrow`, also `numpy`) have win_arm64 wheels at versions meeting the bridge's floors is not checked. If step 3.5 fails on a build-from-source, the fallback is an x64 Python (runs under emulation) — that is Amear's call, not taken here.
--- handoff STOP lines in step 3.5
188:**3.5 Python CLI.** The README (`README.md:43–45@9664d9b`):
200:- **Consequence (INFERRED; nothing tried).** Without their own dependencies the packages may fail to install or import; without `setuptools` in the venv the `-e .` build may fail. Then STOP and reply with the output; Code takes the dependency / build-backend question to Amear. Do not add a package, drop a flag, or retry another way.
201:- **Detection, after the fact.** If `pip`'s output shows any download other than the four named packages, STOP and reply. This only detects; the flags are the prevention.
203:- **Now:** run `python --version` in `C:\praxis\bridge-src` and paste it. Create no venv. Then **STOP before `pip`.** ...
206:**Reply for step 3:** `Z:\vm\replies\<ts>-install.md` (3.1–3.4 outputs, and 3.5's `python --version`), then `<ts>-STOP-pip.md`.
```
(The :188 line is printed in full above. :203 is shortened here; it was printed in full this session.)

### Fix 8 proof (joined string)
```
'money is at stake; (d) installing keys, credentials or agent'
'permissions. Everything else is D1.'
'(d) installing keys, credentials or agent permissions' True True True
```
(These are line 446 stripped, line 447 stripped, then the joined string, whether it equals the target, whether 446 ends in "…or agent", and whether 447 starts with "permissions".)

### Per-fix new text (after), with line numbers
Fix 1, sentence one (:2108):
```
2108	... Amear: "Uh, yeah, you have my approval." (return-handoff :47). It is filed as closing the A6 hold, OPEN-F2-5 at `docs/specs/2026-11-10-f2-session-flat-proposal.md`:79 ("Adoption of Rule F2-1."), on the words put to him at return-handoff :46; whether his approval reaches the elements (a)–(f) listed below, which were not put to him in those words, is not graded here. That file is called the proposal below. Rule F2-1 as the proposal writes it, copied by script from proposal :20:
```
Fixes 2 and 1, A6 sentence (:2129):
```
2129	The unblock clause also requires breaker specs #4 and #5 amended; this entry amends neither, and that is a later unit. This entry does not grade any part of the clause. A6 ties F2's state change to Amear's approval ("F2's state changes when Amear approves the proposed values", DECISIONS.md:1744–1745, line break joined), and the rubric's unblock clause also requires breaker specs #4 and #5 amended, so this entry changes no rubric state.
```
Fix 3 (:2131, excerpt):
```
2131	... copied by script from DECISION_LOG.md:828: "MFFU compliance governs; nothing across the 16:10-18:00 ET close; evening entries stand on MFFU's written answer" (as relayed in DECISION_LOG.md:828, which calls it "the combined reading"; the brief itself is not on disk). The channel's reading at return-handoff :79 ...
```
Fix 4 (:2142 and :2166, excerpt):
```
2142	**F4 stays FROZEN / NOT MET.** (graded NOT MET by the auditor at `55979ee`; not re-graded here). The rubric's F4 criterion, copied by script from `specs/SPEC_RUBRIC.md`:49–50:
2166	... It does not unblock F2 or F4; it grades neither and does not re-grade F4. ...
```
Fix 5 (:2153 and :2158):
```
2153	1. The per-firm settings profile, the channel's proposal at return-handoff :53 ("firm rules (flat time, overnight holding, other firm limits) live in a per-firm settings profile, MFFU as the first profile, not hard-coded."), which the channel left for Amear as O2 at return-handoff :72 ("O2 — R6 per-firm profile (V3): confirm."), is adopted as the design direction for firm rules, MFFU as the first profile. Nothing is built. The profile's contents are not decided here.
2158	Context from the channel's proposal (return-handoff :53), not part of the decision: "Any overnight-holding profile needs its own backtest, because current results assume flat every day."
```
Fix 6 (:2155, excerpt):
```
2155	... The route is recorded as contradicted and is NOT re-decided here; that is the next unit (DECISION_LOG.md:829: "next unit").
```
Fixes 7 and 8 (:2156):
```
2156	4. The VM-to-n8n path (O1, return-handoff :71) stays open. The channel recommends an "SSH reverse tunnel from the Mac for sim testing (no new exposure of n8n)" (return-handoff :71); that tunnel would use SSH keys, which is a D2(d) item ("(d) installing keys, credentials or agent permissions", `specs/SPEC_RUBRIC.md`:446–447, line break joined), so it waits for Amear. D-2026-11-10-C records Amear's 20:42Z words about a reverse tunnel as REPORTED BY Amear and the tunnel as UNVERIFIED (DECISIONS.md:2085, :2089); decision 4 does not change that. Amear's 20:42Z clause, copied by script from DECISIONS.md:2082: "n8n reachability is settled: an SSH reverse tunnel lets the VM reach the Mac's n8n at http://127.0.0.1:5678, and n8n stays closed to the network". Decision 4 records that as REPORTED BY Amear and UNVERIFIED (DECISIONS.md:2089) and keeps O1 open; it does not re-ask him.
```
Fix 9 (:2179, excerpt):
```
2179	**Amear's words (install reply :7–8) and the channel's note (:9).** Voice, ... Install reply :9: "No new snapshot was taken (Amear's choice)."
```
Fix 10 (:2187):
```
2187	**Scope.** The install reply's header (install reply :1) says limit 9 was "lifted by Amear for this install". Amear's quoted words at install reply :7–8 set no scope of their own. This entry reads the lift as covering this one install only and does not widen it; limit 9 binds every later step as written.
```
Fix 11 (:2189 and :2195):
```
2189	**Timing (S4).** The install reply is stamped `UTC: 20261111T172933Z` (install reply :3), that is 2026-11-11T17:29:33Z, before DECISION_LOG.md:828 (2026-11-11T18:19:40Z) and before this entry. This entry records the install after the fact. So for this install the order S4 and S5 ask for (a DECISIONS.md entry and a ledger append before the work) did not hold: the work is stamped 17:29:33Z, the ledger append 18:19:40Z, this entry later. D-2026-11-10-C reads Amear's D2(d) word as "for this grant only: Hermes acts as the VM agent over SSH" (DECISIONS.md:2085, copied by script). This entry records that the Claude.ai channel drove the VM over SSH (install reply :2); it grants nothing.
2195	**Open for Amear.** Whether the Claude.ai channel may drive the VM over SSH again is an agent-permission item, D2(d), his. The x64-Python fallback (install reply :28) is his call.
```
Fix 12 (:2197):
```
2197	**What this entry does not do.** No pip, no clone, no venv, no bridge files. It does not edit the handoff. It changes no step gate in handoff step 3.5 (`vm/2026-11-06-vm-handoff.md`:188 onward), including its STOP conditions on a failed install (:200, "Consequence") and on any unnamed download (:201, "Detection, after the fact"). It installs nothing and grants no key, credential or permission.
```

### Quote byte-identity check (every double-quoted span new after line 2099, compared with the snapshot)
```
$ python3 -I /tmp/vrf5/qcheck.py
new quoted spans: 8
OK  DECISIONS.md:1744-1745 joined | F2's state changes when Amear approves the proposed values
OK  DECISION_LOG.md:828 | the combined reading
OK  DECISION_LOG.md:829 | next unit
OK  SPEC_RUBRIC.md:446-447 joined | (d) installing keys, credentials or agent permissions
OK  DECISIONS.md:2082 | n8n reachability is settled: an SSH reverse tunnel lets the VM reach the Mac's n8n at http://127.0.0.1:5678, and n8n stays closed to the network
OK  DECISIONS.md:2085 | for this grant only: Hermes acts as the VM agent over SSH
OK  handoff:200 | Consequence
OK  handoff:201 | Detection, after the fact
pre-existing/moved (re-checked): OK return-handoff:53 | Any overnight-holding profile needs its own backtest, because current results assume flat every day.
pre-existing/moved (re-checked): OK install reply:1 | lifted by Amear for this install
rh53a OK
dl828 combined OK
```

### S13 sentence count and last line
```
A standalone:
1
A any:
1
B standalone:
1
B any:
1
$ S='<the S13 sentence>'; [ "$(sed -n '2170p' DECISIONS.md)" = "$S" ] && echo ...; [ "$(tail -1 DECISIONS.md)" = "$S" ] && echo ...; sed -n '2171p' DECISIONS.md | wc -c
A last line 2170 == S13 sentence: yes
B last line 2199 (EOF) == S13 sentence: yes
       1
```
(The final `1` is the byte count of line 2171: an empty line, just its newline. In the command, `$S` held the S13 sentence verbatim; it is written as a placeholder here so that the sentence appears only once in this report. A first run that printed the line text gave the same result.)

### Identifier scan, DECISIONS.md lines 2100 to end
```
--- identifier scan 2100-end
       0
0
0
```
(The three numbers are: IPv4 other than 127.0.0.1, MAC addresses, and the ssh key-folder pattern (dot-ssh slash). This is the pattern name only, not a path.)

### MANIFEST
```
$ wc -l MANIFEST.md
     399 MANIFEST.md
$ diff /tmp/vrf-manifest-pre5.md MANIFEST.md
388c388
< | /DECISIONS.md | Log | 3 | 2026-11-11 | MODIFIED (unit 2026-11-11-v-rulings-filing; master under D-2026-11-08-D D1, DECISION_LOG rows 2026-11-11T18:19:40Z WHO: amear and 18:20:00Z): entry D-2026-11-11-A (Amear's rulings V1-V7 and MFFU's replies, WHO: amear, REPORTED BY the Claude.ai channel; four master D1 decisions, changeable by Amear) appended at lines 2101-2168 (heading :2101); entry D-2026-11-11-B (VM handoff §1 limit 9 lifted for one install; Python 3.12.10 and git 2.56.0 ARM64; record only) appended at lines 2170-2195 (heading :2170); lines 1-2099 unchanged; ungraded at time of row |
---
> | /DECISIONS.md | Log | 3 | 2026-11-11 | MODIFIED (unit 2026-11-11-v-rulings-filing; master under D-2026-11-08-D D1, DECISION_LOG rows 2026-11-11T18:19:40Z WHO: amear and 18:20:00Z): entry D-2026-11-11-A (Amear's rulings V1-V7 and MFFU's replies, WHO: amear, REPORTED BY the Claude.ai channel; four master D1 decisions, changeable by Amear) appended at lines 2101-2170 (heading :2101); entry D-2026-11-11-B (VM handoff §1 limit 9 lifted for one install; Python 3.12.10 and git 2.56.0 ARM64; record only) appended at lines 2172-2199 (heading :2172); lines 1-2099 unchanged; ungraded at time of row |
398c398,399
< | /docs/reports/2026-11-11-v-rulings-filing-worker5.md | Report | 3 | 2026-11-11 | ADVERSARIAL worker 5 report for unit 2026-11-11-v-rulings-filing: check of the MANIFEST rows and any fixes; ungraded at time of row |
---
> | /docs/reports/2026-11-11-v-rulings-filing-worker5.md | Report | 3 | 2026-11-11 | BUILD fix worker 5 report for unit 2026-11-11-v-rulings-filing: fixes to D-2026-11-11-A and -B after the worker 3 attack; MANIFEST row ranges updated; ungraded at time of row |
> | /docs/reports/2026-11-11-v-rulings-filing-worker6.md | Report | 3 | 2026-11-11 | ADVERSARIAL worker 6 report for unit 2026-11-11-v-rulings-filing: re-check of worker 5's fixes and the MANIFEST rows; ungraded at time of row |
diff rc=1
MANIFEST 1-387 unchanged
0000000   \n
```

### Index untouched
```
$ git diff --cached --name-only
docs/reports/evidence/[2026-10-28 MFFU reply image, filename withheld]
```
(This file was already staged before this session. I made no index changes.)

## Files staged
None by this worker; index changes are out of scope per the brief. Files modified in the working tree: `DECISIONS.md` (lines 2100 and later only), `MANIFEST.md` (:388, :398, new :399), and this report.

## Result: PASS
All 13 fixes are applied. One open note is for the next check: the fix 7 citation of :2089 for the tunnel's UNVERIFIED (see the process log).

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
