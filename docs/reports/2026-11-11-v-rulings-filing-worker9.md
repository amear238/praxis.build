# Unit 2026-11-11-v-rulings-filing — worker 9 report

## Task
Apply fixes 1–11 from the brief to D-2026-11-11-A and -B (DECISIONS.md, after line 2099) and to MANIFEST.md rows :388, :389, :401, plus two rows appended at the end.

## Mode
BUILD (fix).

## Criterion
From the brief: DECISIONS.md lines 1–2099 byte-identical to HEAD; both entry headings unchanged; every new quotation copied by script and byte-identical to the line it cites; the S13 sentence once per entry, standalone, as the entry's last line; no identifiers; MANIFEST diff touches only :388, :389, :401 and the two appended lines, and lines 1–387 match /tmp/vrf-manifest-before.md.

## Process log
1. Took snapshots first: `cp MANIFEST.md /tmp/vrf-manifest-pre9.md`, `cp DECISIONS.md /tmp/vrf-decisions-pre9.md`. Checked shasums: each snapshot matched its live file. Ran the pre-edit `cmp` against /tmp/vrf-manifest-before.md: silent.
2. Read the cited source lines: DECISION_LOG.md:828 and :829, return-handoff :58, DECISIONS.md:2082, investigation :1424.
3. Applied fixes 1–8 with /tmp/vrf9/edit.py. Each replacement asserts that its old text occurs exactly once, and only in the text after the D-2026-11-11-A heading. The script builds each new inner quotation by slicing it out of its source line ("also" from DECISION_LOG.md:828; "Amear (chat, 14:38 ET)" from return-handoff :58; "uses SSH keys" from :829; "is settled" from DECISIONS.md:2082; "stays open" from DECISION_LOG.md:829).
4. Fix 7 checks before deleting:
   - "Item 4 names the evaluation phase only." The next sentence's channel quote already says "item 4 names the evaluation only", so the sentence was deleted.
   - "These four are the master's decisions, not Amear's." Status (:2103) already says "they are not Amear's rulings", so the sentence was deleted. The D1 heading line (:2151) is unchanged.
   - In the F4 paragraph, the separate sentence "Amear sends it himself." was deleted and the :1424 quote kept. NOTE for the manager: the exact words "Amear sends it himself" now appear nowhere in DECISIONS.md (grep count 0). The point survives only as the existing Open-for-Amear bullet "Sending the replacement ticket (investigation C3.3, :1422) is his." I added no new wording because the brief did not supply any.
5. Fix 5: changed "would use" to "uses". "uses SSH keys" is in DECISION_LOG.md:829 (byte check below). In the entry it is the restored verb in plain prose, not a quotation. The sentences from "D-2026-11-10-C records…" to the end of item 4 now form their own paragraph at :2158, which begins "Context for decision 4 (not part of it):". Item 4 (:2156) now ends "so it waits for Amear."
6. Fix 6: the new bullet is the last line of the Open-for-Amear list (:2168).
7. Fixes 9–11 applied with /tmp/vrf9/man.py. Before writing the :389 wording I checked that the return-handoff file really has the "[key file]" and "[VM user]" placeholders (both at :68).

## Verification evidence

### Headings and wc -l, before
```
    2200 DECISIONS.md
     401 MANIFEST.md
2101:## 2026-11-11 — D-2026-11-11-A: Amear's rulings V1–V7 (Claude.ai channel voice sessions, 2026-11-10) and MFFU's replies. Filed WHO: amear, REPORTED BY the Claude.ai channel.
2173:## 2026-11-11 — D-2026-11-11-B: VM handoff §1 limit 9 lifted by Amear for one install; Python 3.12.10 and git 2.56.0 (ARM64) installed in the VM. Record only. Filed WHO: amear, REPORTED BY the Claude.ai channel.
```

### Headings and wc -l, after
```
    2203 DECISIONS.md
     403 MANIFEST.md
2101:## 2026-11-11 — D-2026-11-11-A: Amear's rulings V1–V7 (Claude.ai channel voice sessions, 2026-11-10) and MFFU's replies. Filed WHO: amear, REPORTED BY the Claude.ai channel.
2176:## 2026-11-11 — D-2026-11-11-B: VM handoff §1 limit 9 lifted by Amear for one install; Python 3.12.10 and git 2.56.0 (ARM64) installed in the VM. Record only. Filed WHO: amear, REPORTED BY the Claude.ai channel.
```

### Fixed passages: `diff /tmp/vrf-decisions-pre9.md DECISIONS.md` (">" lines are the after-text; the right-hand numbers are the after line numbers)
```
2104c2104
< **Authority:** DECISION_LOG.md:828 (row 2026-11-11T18:19:40Z, WHO: amear) and DECISION_LOG.md:829 (row 2026-11-11T18:20:00Z, praxis-master, the four D1 decisions); at filing both rows sit in the working copy, after the 826 lines of DECISION_LOG.md at HEAD `d056e91`. Amear's go reached the master through the Claude.ai channel (chat 2026-11-11 17:27Z); his words, copied by script from DECISION_LOG.md:828: "U do them". S5: the ledger append at DECISION_LOG.md:828 is the authorisation record; a channel-reported ruling is recorded, not proven given. The source of every ruling below is `docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md` (called the return-handoff file below; untracked at filing), written by the Claude.ai channel; its line numbers are cited as `return-handoff :N`. Every quotation in this entry is copied by script, byte-identical to the cited line.
---
> **Authority:** DECISION_LOG.md:828 (row 2026-11-11T18:19:40Z, WHO: amear) and DECISION_LOG.md:829 (row 2026-11-11T18:20:00Z, praxis-master, the four D1 decisions); at filing both rows sit in the working copy, after the 826 lines of DECISION_LOG.md at HEAD `d056e91`. Amear's go reached the master through the Claude.ai channel (chat 2026-11-11 17:27Z); his words, copied by script from DECISION_LOG.md:828: "U do them". S5: the ledger append at DECISION_LOG.md:828 is the authorisation record; a channel-reported ruling is recorded, not proven given. The source of every ruling below, except the combined V3/V5 reading (DECISION_LOG.md:828), is `docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md` (called the return-handoff file below; untracked at filing), written by the Claude.ai channel; its line numbers are cited as `return-handoff :N`. V4's words are from chat, not a voice session (return-handoff :58: "Amear (chat, 14:38 ET)"). Every quotation in this entry is copied by script, byte-identical to the cited line.
2129c2129
< DECISION_LOG.md:828 records "its unblock also needs breaker specs #4 and #5 amended" (copied by script from DECISION_LOG.md:828). This entry amends neither (that is a later unit) and grades no part of the unblock clause. A6 ties F2's state change to Amear's approval ("F2's state changes when Amear approves the proposed values", DECISIONS.md:1744–1745, line break joined); this entry changes no rubric state.
---
> DECISION_LOG.md:828 records "its unblock also needs breaker specs #4 and #5 amended" (copied by script from DECISION_LOG.md:828). This entry does not read that "also" as meaning any part of the unblock clause is met. This entry amends neither (that is a later unit) and grades no part of the unblock clause. A6 ties F2's state change to Amear's approval ("F2's state changes when Amear approves the proposed values", DECISIONS.md:1744–1745, line break joined). The #4/#5 text was not put to him (element (f) above); whether A6 is triggered is not graded here. This entry changes no rubric state.
2131c2131
< **V3 as clarified by V5 — overnight holding.** V3 (return-handoff :50–53): Amear: "Yes, however, if uh, I go with a, another prop firm that uh, potentially allows for overnight uh, holds, would we be able to duplicate the dur uh, the uh, the infrastructure or change that?" Then: "Having to fuck around." (return-handoff :52). V5 (return-handoff :76–79): Amear: "I don't care about evening entries. It's more about compli uh, the MFFU's compliance." (return-handoff :78). The combined ruling as Amear's 2026-11-11 brief states it (relayed, chat 17:27Z), copied by script from DECISION_LOG.md:828: "MFFU compliance governs; nothing across the 16:10-18:00 ET close; evening entries stand on MFFU's written answer" (as relayed in DECISION_LOG.md:828, which calls it "the combined reading"; the brief itself is not on disk). The channel's reading at return-handoff :79 is INFERRED, not his words; the channel says it was "put back to him and not objected to". The ambiguity the channel flagged at return-handoff :55 ("do not file V3 as closing OPEN-1 until Amear answers") is answered by V5. V3 does not close OPEN-1. R6 stays open pending MFFU's written answer to OPEN-1 (R6 design §7, `bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md`:110: "A written MFFU answer is needed before any funded use.").
---
> **V3 as clarified by V5 — overnight holding.** V3 (return-handoff :50–53): Amear: "Yes, however, if uh, I go with a, another prop firm that uh, potentially allows for overnight uh, holds, would we be able to duplicate the dur uh, the uh, the infrastructure or change that?" Then: "Having to fuck around." (return-handoff :52). V5 (return-handoff :76–79): Amear: "I don't care about evening entries. It's more about compli uh, the MFFU's compliance." (return-handoff :78). The combined ruling as Amear's 2026-11-11 brief states it (relayed, chat 17:27Z), copied by script from DECISION_LOG.md:828: "MFFU compliance governs; nothing across the 16:10-18:00 ET close; evening entries stand on MFFU's written answer" (as relayed in DECISION_LOG.md:828, which calls it "the combined reading"; the brief itself is not on disk). The channel's reading at return-handoff :79 is INFERRED, not his words; the channel says it was "put back to him and not objected to". The ambiguity the channel flagged at return-handoff :55 ("do not file V3 as closing OPEN-1 until Amear answers") is answered by V5, as the combined reading relayed in DECISION_LOG.md:828 states it (REPORTED BY the Claude.ai channel). V3 does not close OPEN-1. R6 stays open pending MFFU's written answer to OPEN-1 (R6 design §7, `bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md`:110: "A written MFFU answer is needed before any funded use.").
2138c2138
< - 2026-11-10T19:43:42Z, reply to V1 (message `1a1c6fce04330f0d`, return-handoff :114). Items 1, 2 and 4, copied by script from return-handoff :120, :121, :123: "1. Kindly be informed that we do not offer Rithmic at MFFu"; "2. Kindly be informed that automated trading is allowed provided you abide by our rules and policies : https://help.myfundedfutures.com/en/articles/8444599-fair-play-and-prohibited-trading-practices"; "4. You can trade using your strategy at the evaluation phase". Item 4 names the evaluation phase only. The channel's reading (INFERRED, return-handoff :130): "Funded-account permission for the pattern is not stated; item 4 names the evaluation only."
---
> - 2026-11-10T19:43:42Z, reply to V1 (message `1a1c6fce04330f0d`, return-handoff :114). Items 1, 2 and 4, copied by script from return-handoff :120, :121, :123: "1. Kindly be informed that we do not offer Rithmic at MFFu"; "2. Kindly be informed that automated trading is allowed provided you abide by our rules and policies : https://help.myfundedfutures.com/en/articles/8444599-fair-play-and-prohibited-trading-practices"; "4. You can trade using your strategy at the evaluation phase". The channel's reading (INFERRED, return-handoff :130): "Funded-account permission for the pattern is not stated; item 4 names the evaluation only."
2149c2149
< A replacement ticket exists at `docs/reports/2026-11-11-mffu-connection-investigation.md`:1422 (heading "C3.3 — Replacement ticket"); its :1424 reads "Amear sends this himself from his logged-in MFFU dashboard." Amear sends it himself.
---
> A replacement ticket exists at `docs/reports/2026-11-11-mffu-connection-investigation.md`:1422 (heading "C3.3 — Replacement ticket"); its :1424 reads "Amear sends this himself from his logged-in MFFU dashboard."
2152c2152
< Source: DECISION_LOG.md:829. These four are the master's decisions, not Amear's.
---
> Source: DECISION_LOG.md:829.
2156c2156
< 4. The VM-to-n8n path (O1, return-handoff :71) stays open. The channel recommends an "SSH reverse tunnel from the Mac for sim testing (no new exposure of n8n)" (return-handoff :71); that tunnel would use SSH keys, which is a D2(d) item ("(d) installing keys, credentials or agent permissions", `specs/SPEC_RUBRIC.md`:446–447, line break joined), so it waits for Amear. D-2026-11-10-C records Amear's 20:42Z words about a reverse tunnel as REPORTED BY Amear and the tunnel as UNVERIFIED (DECISIONS.md:2085, :2089); decision 4 does not change that. Amear's 20:42Z clause, copied by script from DECISIONS.md:2082: "n8n reachability is settled: an SSH reverse tunnel lets the VM reach the Mac's n8n at http://127.0.0.1:5678, and n8n stays closed to the network". DECISION_LOG.md:829 keeps O1 open; the difference between his "is settled" and "stays open" is recorded here, not resolved.
---
> 4. The VM-to-n8n path (O1, return-handoff :71) stays open. The channel recommends an "SSH reverse tunnel from the Mac for sim testing (no new exposure of n8n)" (return-handoff :71); that tunnel uses SSH keys, which is a D2(d) item ("(d) installing keys, credentials or agent permissions", `specs/SPEC_RUBRIC.md`:446–447, line break joined), so it waits for Amear.
2157a2158,2159
> Context for decision 4 (not part of it): D-2026-11-10-C records Amear's 20:42Z words about a reverse tunnel as REPORTED BY Amear and the tunnel as UNVERIFIED (DECISIONS.md:2085, :2089); decision 4 does not change that. Amear's 20:42Z clause, copied by script from DECISIONS.md:2082: "n8n reachability is settled: an SSH reverse tunnel lets the VM reach the Mac's n8n at http://127.0.0.1:5678, and n8n stays closed to the network". DECISION_LOG.md:829 keeps O1 open; the difference between his "is settled" and "stays open" is recorded here, not resolved.
> 
2164c2166
< - A header-bearing export of the outgoing messages is his to file (return-handoff :43).
---
> - A header-bearing export of the outgoing V1 message is his to file if the auditor wants headers (return-handoff :43).
2165a2168
> - Both his 20:42Z "is settled" (DECISIONS.md:2082) and decision 4's "stays open" (DECISION_LOG.md:829) are on record; which stands is his.
2167c2170
< **What this entry does not do.** It builds nothing. It edits no spec, no rubric, no handoff, and not D-2026-11-10-B, the F2 proposal or the topology document. It does not unblock F2 or F4; it grades neither and does not re-grade F4. It sets no breaker value and amends no breaker text. It decides no D2 item, no broker route, no per-firm profile contents and no VM-to-n8n path. It does not file the four 2026-11-10 Hermes replies (DECISION_LOG.md:829).
---
> **What this entry does not do.** It builds nothing. It edits no spec, no rubric, no VM handoff, and not D-2026-11-10-B, the F2 proposal or the topology document. It does not unblock F2 or F4; it grades neither and does not re-grade F4. It sets no breaker value and amends no breaker text. It decides no D2 item, no broker route, no per-firm profile contents and no VM-to-n8n path. It does not file the four 2026-11-10 Hermes replies (DECISION_LOG.md:829).
2198c2201
< **What this entry does not do.** No pip, no clone, no venv, no bridge files. It does not edit the handoff. It changes no step gate in handoff step 3.5 (`vm/2026-11-06-vm-handoff.md`:188 onward), including its STOP conditions on a failed install (:200, "Consequence") and on any unnamed download (:201, "Detection, after the fact"). It installs nothing and grants no key, credential or permission.
---
> **What this entry does not do.** No pip, no clone, no venv, no bridge files. It does not edit the VM handoff. It changes no step gate in handoff step 3.5 (`vm/2026-11-06-vm-handoff.md`:188 onward), including its STOP conditions on a failed install (:200, "Consequence") and on any unnamed download (:201, "Detection, after the fact"). It installs nothing and grants no key, credential or permission.
```

### HEAD identity
```
$ git diff HEAD -- DECISIONS.md | grep -c '^-[^-]'
0
$ cmp <(sed -n 1,2099p DECISIONS.md) <(git show HEAD:DECISIONS.md | sed -n 1,2099p) && echo HEAD-1-2099-IDENTICAL
HEAD-1-2099-IDENTICAL
```

### Byte-identity of added and moved quoted spans (`python3 -I /tmp/vrf9/check.py`)
has-quoted means the span appears in double quotes on that DECISIONS line. "uses SSH keys" is plain prose (the restored verb), so has-quoted=False is expected for it.
```
DECISIONS:2104 has-quoted=True  docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:58 contains-bytes=True  [Amear (chat, 14:38 ET)]
DECISIONS:2129 has-quoted=True  DECISION_LOG.md:828 contains-bytes=True  [also]
DECISIONS:2129 has-quoted=True  DECISION_LOG.md:828 contains-bytes=True  [its unblock also needs breaker specs #4 and #5 ame]
DECISIONS:2156 has-quoted=False  DECISION_LOG.md:829 contains-bytes=True  [uses SSH keys]
DECISIONS:2156 has-quoted=True  docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:71 contains-bytes=True  [SSH reverse tunnel from the Mac for sim testing (n]
DECISIONS:2158 has-quoted=True  DECISIONS.md:2082 contains-bytes=True  [n8n reachability is settled: an SSH reverse tunnel]
DECISIONS:2158 has-quoted=True  DECISIONS.md:2082 contains-bytes=True  [is settled]
DECISIONS:2158 has-quoted=True  DECISION_LOG.md:829 contains-bytes=True  [stays open]
DECISIONS:2168 has-quoted=True  DECISIONS.md:2082 contains-bytes=True  [is settled]
DECISIONS:2168 has-quoted=True  DECISION_LOG.md:829 contains-bytes=True  [stays open]
DECISIONS:2131 has-quoted=True  DECISION_LOG.md:828 contains-bytes=True  [MFFU compliance governs; nothing across the 16:10-]
DECISIONS:2149 has-quoted=True  docs/reports/2026-11-11-mffu-connection-investigation.md:1424 contains-bytes=True  [Amear sends this himself from his logged-in MFFU d]
```

### S13 placement per entry (the sentence is matched by grep -xF and is not printed here)
```
A (2101-2175): standalone=1 substring=1 at-line=2174 last-nonblank-line=2174
B (2176-2203): standalone=1 substring=1 at-line=2203 last-nonblank-line=2203
file last line number: 2203; line 2175 blank: yes
```

### Identifier scan (IPv4, MAC, key path, VM name patterns)
```
$ sed -n "2100,$p" DECISIONS.md | grep -noE "$P" (match only, offset line numbers)
59:127.0.0.1
86:praxis-vm
$ sed -n "388,$p" MANIFEST.md | grep -cE "$P"
0
$ git show HEAD:DECISIONS.md | grep -c praxis-vm
2
```
The only IPv4 is 127.0.0.1 (allowed). It sits in the moved paragraph (:2158), which quotes DECISIONS.md:2082 at HEAD. "praxis-vm" at :2185 was already there, in entry B's quote of install reply :2. It is the SSH host alias, which also appears in HEAD's DECISIONS.md:2082; the install reply puts its VM machine name behind the placeholder "[VM machine name]" at :17. I did not add it and did not change it. I did not scan for the MFFU rep's name by name, because the brief forbids typing it. None of my edits added a personal name.

### MANIFEST diff against pre9, and the cmp
```
$ diff /tmp/vrf-manifest-pre9.md MANIFEST.md
388,389c388,389
< | /DECISIONS.md | Log | 3 | 2026-11-11 | MODIFIED (unit 2026-11-11-v-rulings-filing; master under D-2026-11-08-D D1, DECISION_LOG rows 2026-11-11T18:19:40Z WHO: amear and 18:20:00Z): entry D-2026-11-11-A (Amear's rulings V1-V7 and MFFU's replies, WHO: amear, REPORTED BY the Claude.ai channel; four master D1 decisions, changeable by Amear) appended at lines 2101-2171 (heading :2101); entry D-2026-11-11-B (VM handoff §1 limit 9 lifted for one install; Python 3.12.10 and git 2.56.0 ARM64; record only) appended at lines 2173-2200 (heading :2173); lines 1-2099 unchanged; ungraded at time of row |
< | /docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md | Report | 3 | 2026-11-11 | Return handoff from the Claude.ai Praxis channel (Amear's rulings V1-V7 from the 2026-11-10 voice sessions, MFFU's replies), filed by unit 2026-11-11-v-rulings-filing; network identifiers replaced by placeholders; two-line S13 addendum (a filer's line, then the S13 sentence alone) added at end; ungraded at time of row |
---
> | /DECISIONS.md | Log | 3 | 2026-11-11 | MODIFIED (unit 2026-11-11-v-rulings-filing; master under D-2026-11-08-D D1, DECISION_LOG rows 2026-11-11T18:19:40Z WHO: amear and 18:20:00Z): entry D-2026-11-11-A (Amear's rulings V1-V7 and MFFU's replies, WHO: amear, REPORTED BY the Claude.ai channel; four master D1 decisions, changeable by Amear) appended at lines 2101-2174 (heading :2101); entry D-2026-11-11-B (VM handoff §1 limit 9 lifted for one install; Python 3.12.10 and git 2.56.0 ARM64; record only) appended at lines 2176-2203 (heading :2176); lines 1-2099 unchanged; ungraded at time of row |
> | /docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md | Report | 3 | 2026-11-11 | Return handoff from the Claude.ai Praxis channel (Amear's rulings V1-V7 from the 2026-11-10 voice sessions, MFFU's replies), filed by unit 2026-11-11-v-rulings-filing; network identifiers, the key file name and the VM user replaced by placeholders; two-line S13 addendum (a filer's line, then the S13 sentence alone) added at end; ungraded at time of row |
401c401,403
< | /docs/reports/2026-11-11-v-rulings-filing-worker8.md | Report | 3 | 2026-11-11 | ADVERSARIAL worker 8 report for unit 2026-11-11-v-rulings-filing: re-check of worker 7's fixes; ungraded at time of row |
---
> | /docs/reports/2026-11-11-v-rulings-filing-worker8.md | Report | 3 | 2026-11-11 | ADVERSARIAL worker 8 report for unit 2026-11-11-v-rulings-filing: attack (a)–(k) on D-2026-11-11-A and -B, the de-identified files, S13 placement and the MANIFEST rows after worker 7's fixes; ungraded at time of row |
> | /docs/reports/2026-11-11-v-rulings-filing-worker9.md | Report | 3 | 2026-11-11 | BUILD fix worker 9 report for unit 2026-11-11-v-rulings-filing: third fix pass on D-2026-11-11-A and -B after the worker 8 attack; MANIFEST rows corrected; ungraded at time of row |
> | /docs/reports/2026-11-11-v-rulings-filing-worker10.md | Report | 3 | 2026-11-11 | ADVERSARIAL worker 10 report for unit 2026-11-11-v-rulings-filing: final attack on D-2026-11-11-A and -B, the de-identified files, S13 placement and the MANIFEST rows after worker 9's fixes; ungraded at time of row |
$ cmp <(sed -n 1,387p MANIFEST.md) <(sed -n 1,387p /tmp/vrf-manifest-before.md) && echo CMP-SILENT
CMP-SILENT
```

## Files staged
None. The brief forbids index changes; I ran no git add. Files written in the working copy: DECISIONS.md (lines after 2099 only), MANIFEST.md (:388, :389, :401, plus appended :402 and :403), and this report. Helper scripts are in /tmp/vrf9/, outside the repo.

## Result: PASS
All 11 fixes applied, and every check above passed. One note for the manager: the brief's fix 7 says to keep "Amear sends it himself" in the Open-for-Amear list, but the list never had those exact words; it says "Sending the replacement ticket (investigation C3.3, :1422) is his." No rubric state, F2 status or F4 status was changed or claimed.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
