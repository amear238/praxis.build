# Unit 2026-11-11-v-rulings-filing — worker 6 (ADVERSARIAL)

## Task
Attack DECISIONS.md lines 2100–end (D-2026-11-11-A from :2101, D-2026-11-11-B from :2172), MANIFEST.md lines 388–end, the de-identified return-handoff file and install reply, using attacks (a)–(k) from the brief. Read-only except this report. HEAD `d056e91`.

## Mode
ADVERSARIAL.

## Criterion
specs/SPEC_RUBRIC.md S1, S2, S4, S5, S8, S13 (verbatim in the brief) and the entry/MANIFEST requirements in the brief.

## Process log
1. Line counts, entry headings, HEAD line count; diffs against HEAD for DECISIONS.md and MANIFEST.md; MANIFEST 1–387 compared with `/tmp/vrf-manifest-before.md`.
2. Own script `/tmp/w6scripts/q.py`: pulls every `"…"` span in DECISIONS.md 2100–end and searches eleven source files (HEAD copy of DECISIONS.md, the bf6fcc7 capture and R6 design taken with `git show`) for each one. I then checked every hit against the line the entry cites. A second script `/tmp/w6scripts/j.py` checks the two "line break joined" quotes and the three fenced blocks.
3. De-identification: `/tmp/w6scripts/ph.py` treats each placeholder as a wildcard and matches the changed lines against the /tmp originals. `/tmp/w6scripts/ids.py` pulls the removed values out of the originals at runtime and prints only counts.
4. Checked the D1 block against DECISION_LOG.md:829, decision by decision. Read D-2026-11-10-C (:2076–2094), proposal :6–9, :74–80, DECISIONS.md:1740–1746, handoff :186–202.
5. Counted S13 occurrences and positions; checked MANIFEST paths with `ls`.

## Verification evidence

### Line counts, headings, append-only (attacks i, k)
```
$ git rev-parse --short HEAD; wc -l DECISIONS.md MANIFEST.md /tmp/vrf-manifest-before.md; git show HEAD:DECISIONS.md | wc -l; grep -n '^## 2026-11-11' DECISIONS.md
d056e91
    2199 DECISIONS.md
     399 MANIFEST.md
     387 /tmp/vrf-manifest-before.md
    2099
2101:## 2026-11-11 — D-2026-11-11-A: Amear's rulings V1–V7 (Claude.ai channel voice sessions, 2026-11-10) and MFFU's replies. Filed WHO: amear, REPORTED BY the Claude.ai channel.
2172:## 2026-11-11 — D-2026-11-11-B: VM handoff §1 limit 9 lifted by Amear for one install; Python 3.12.10 and git 2.56.0 (ARM64) installed in the VM. Record only. Filed WHO: amear, REPORTED BY the Claude.ai channel.

$ git diff HEAD -- DECISIONS.md | grep -E '^@@'
@@ -2097,3 +2097,103 @@ ...
DECISIONS plus: 100 minus: 0
lines 1-2099 identical to HEAD        (cmp <(git show HEAD:DECISIONS.md) <(head -n 2099 DECISIONS.md))

boundaries: 2100: []  2101: [## 2026-11-11 — D-2026-11-11-A ...]  2169: []  2170: [Fills are optimistic; ...]  2171: []  2172: [## 2026-11-11 — D-2026-11-11-B ...]  2198: []  2199: [Fills are optimistic; ...]

$ cmp <(head -n 387 MANIFEST.md) /tmp/vrf-manifest-before.md && echo ...
MANIFEST 1-387 identical to before-snapshot
@@ -304,6 +304,14 @@
@@ -377,3 +385,15 @@
MANIFEST plus: 20 minus: 0      (8 pre-unit rows inside 1–387 + 12 unit rows 388–399)
```
The file paths in MANIFEST rows 388–399 all exist (`ls -l`, size and path shown), except worker6, which this report creates:
```
404228 ./DECISIONS.md
13912 ./docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md
3170 ./vm/replies/20261111T172933Z-python-git-install.md
8 ./vm/replies/20261111T172802Z-STATUS.md
9 ./vm/replies/20261111T172940Z-STATUS.md
2191 ./docs/reports/2026-11-11-v-rulings-filing-manager.md
30244 ./docs/reports/2026-11-11-v-rulings-filing-worker1.md
11554 ./docs/reports/2026-11-11-v-rulings-filing-worker2.md
27038 ./docs/reports/2026-11-11-v-rulings-filing-worker3.md
8585 ./docs/reports/2026-11-11-v-rulings-filing-worker4.md
19823 ./docs/reports/2026-11-11-v-rulings-filing-worker5.md
STATUS contents (od -c): S T A R T E D \n  F I N I S H E D \n
```

### Quote check (attack a) — `python3 -I /tmp/w6scripts/q.py`, full output
```
D2104 Q1: "U do them" -> ['IR:8', 'DL:825', 'DL:828', 'INV:289']
D2106 Q2: "Write it now and then send it." -> ['RH:10', 'DL:828']
D2106 Q3: "Go ahead." -> ['RH:82', 'DL:828']
D2108 Q4: "flat by 16:00 ET governs; a position open at 15:00 may stay open until..." -> ['RH:46']
D2108 Q5: "Uh, yeah, you have my approval." -> ['RH:47', 'DL:828']
D2108 Q6: "Adoption of Rule F2-1." -> ['PROP:79']
D2114 Q7: "On a full trading day, at 15:00 ET an open system position stays open." -> ['PROP:30']
D2114 Q8: "Nothing closes it at 15:00." -> ['PROP:30']
D2116 Q9: "flat by 16:00 ET" -> ['RH:46', 'DEC:327', 'DEC:329', 'DEC:341', 'DL:828']
D2116 Q10: "The closing order for every open system position is submitted no later..." -> ['PROP:20']
D2116 Q11: "(or no later than the exchange's early close on an early-close day)" -> ['PROP:20']
D2116 Q12: "the position must be confirmed flat before MFFU's 4:10 PM ET auto-clos..." -> ['PROP:20']
D2116 Q13: "The system opens no new position from that flat time until 18:00 ET" -> ['PROP:20']
D2116 Q14: "New system entries between 15:00 and 16:00 are allowed under Rule F2-1..." -> ['PROP:30']
D2116 Q15: "Between 15:00 and 18:00 ET Amear's own manual interaction is locked ou..." -> ['PROP:30']
D2118 Q16: "it only stops the system firing while the account is shut" -> ['RH:47']
D2120 Q17: "Trades may be placed beginning at 6:00 PM EST when the Globex session ..." -> ['CAP:10']
D2120 Q18: "At MyFundedFutures, any open positions will be automatically closed at..." -> ['CAP:12']
D2120 Q19: "During holiday trading hours, auto-liquidation will not occur at the h..." -> ['CAP:20']
D2120 Q20: "EST" -> ['PROP:25', 'RUB:317', 'DEC:551', 'DEC:724', 'DEC:750', 'DEC:1097', '...+353']
D2120 Q21: "this file reads it as US Eastern local time (ET), an INFERENCE, not st..." -> ['PROP:25']
D2129 Q22: "F2's state changes when Amear approves the proposed values" -> ['PROP:8', 'DEC:2068', 'DL:723', 'DL:725']
D2131 Q23: "Yes, however, if uh, I go with a, another prop firm that uh, potential..." -> ['RH:52']
D2131 Q24: "Having to fuck around." -> ['RH:52']
D2131 Q25: "I don't care about evening entries. It's more about compli uh, the MFF..." -> ['RH:78', 'DL:828']
D2131 Q26: "MFFU compliance governs; nothing across the 16:10-18:00 ET close; even..." -> ['DL:828']
D2131 Q27: "the combined reading" -> ['DL:828']
D2131 Q28: "put back to him and not objected to" -> ['RH:79']
D2131 Q29: "do not file V3 as closing OPEN-1 until Amear answers" -> ['RH:55', 'INV:476']
D2131 Q30: "A written MFFU answer is needed before any funded use." -> ['R6:110']
D2135 Q31: "commit everything that we just discussed and the plan for tomorrow is ..." -> ['RH:106']
D2135 Q32: "I don't remember if I installed the tool to access the NinjaTrader thr..." -> ['RH:107']
D2135 Q33: "Asked that this check be on tomorrow's (2026-11-11) list." -> ['RH:107']
D2135 Q34: "So cli-nt-bridge is not installed" -> ['RH:108']
D2138 Q35: "1. Kindly be informed that we do not offer Rithmic at MFFu" -> ['RH:120', 'INV:481']
D2138 Q36: "2. Kindly be informed that automated trading is allowed provided you a..." -> ['RH:121', 'INV:482']
D2138 Q37: "4. You can trade using your strategy at the evaluation phase" -> ['RH:123', 'INV:483']
D2138 Q38: "Funded-account permission for the pattern is not stated; item 4 names ..." -> ['RH:130', 'INV:484']
D2139 Q39: "OPEN-1 (evening entry vs overnight) is NOT answered." -> ['RH:133', 'INV:489']
D2140 Q40: "we see you've been inactive for some time, so this ticket is being clo..." -> ['RH:136', 'INV:486']
D2149 Q41: "C3.3 — Replacement ticket" -> ['INV:1422']
D2149 Q42: "Amear sends this himself from his logged-in MFFU dashboard." -> ['INV:1424']
D2153 Q43: "firm rules (flat time, overnight holding, other firm limits) live in a..." -> ['RH:53']
D2153 Q44: "O2 — R6 per-firm profile (V3): confirm." -> ['RH:72']
D2154 Q45: "the Noise-Area baseline (test 2a: 1,190 trades / $197,327.60 on NQCONT..." -> ['RH:110']
D2155 Q46: "we do not offer Rithmic" -> ['RH:120', 'DL:828', 'DL:829', 'INV:15', 'INV:317', 'INV:465', '...+4']
D2155 Q47: "→ Rithmic → account." -> ['INV:512', 'INV:631', 'TOP:41']
D2155 Q48: "next unit" -> ['RUB:451', 'DEC:1257', 'DEC:1262', 'DEC:1920', 'DEC:1976', 'DL:117', '...+16']
D2156 Q49: "SSH reverse tunnel from the Mac for sim testing (no new exposure of n8..." -> ['RH:71']
D2156 Q50: "(d) installing keys, credentials or agent permissions" -> ['DEC:1974']
D2156 Q51: "n8n reachability is settled: an SSH reverse tunnel lets the VM reach t..." -> ['DEC:2082', 'DL:813']
D2158 Q52: "Any overnight-holding profile needs its own backtest, because current ..." -> ['RH:53']
D2162 Q53: "the verification details are his to give" -> ['RH:136', 'INV:486']
D2177 Q54: "**Do not install anything else** — not Python, not git, not a package ..." -> ['VMH:37']
D2179 Q55: "Okay, you know what? Let's forget about the snapshot. Let's have it ex..." -> ['IR:7', 'DL:828']
D2179 Q56: "Hermes is going to give me a uh, a physical button to accept or deny, ..." -> ['IR:7']
D2179 Q57: "U do them" -> ['IR:8', 'DL:825', 'DL:828', 'INV:289']
D2179 Q58: "No new snapshot was taken (Amear's choice)." -> ['IR:9']
D2181 Q59: "Claude (Claude.ai Praxis channel, Cowork session)" -> ['IR:2']
D2181 Q60: "driving the VM over SSH from the Mac (host praxis-vm), commands run fr..." -> ['IR:2']
D2183 Q61: "the VM is Windows on ARM64 and winget installed the ARM64 builds" -> ['IR:28']
D2185 Q62: "NinjaTrader not started, stopped or touched (same pid and start time b..." -> ['IR:25']
D2187 Q63: "lifted by Amear for this install" -> ['IR:1']
D2189 Q64: "for this grant only: Hermes acts as the VM agent over SSH" -> ['DEC:2085']
D2191 Q65: "Whether the bridge's dependencies (notably `pyarrow`, also `numpy`) ha..." -> ['IR:28']
D2191 Q66: "If step 3.5 fails on a build-from-source, the fallback is an x64 Pytho..." -> ['IR:28']
D2191 Q67: "3.5 Python CLI." -> ['VMH:188']
D2197 Q68: "Consequence" -> ['DEC:322', 'DEC:327', 'DEC:329', 'DEC:341', 'DEC:433', 'DEC:850', '...+6']
D2197 Q69: "Detection, after the fact" -> ['VMH:201']
total quotes 69
```
(RH = return-handoff, IR = install reply, PROP = F2 proposal, RUB = rubric, DEC = HEAD DECISIONS.md, DL = DECISION_LOG.md, CAP/R6 = bf6fcc7 files, INV = investigation, TOP = topology, VMH = VM handoff.) No line had an odd number of quote characters, and there are 0 curly quotes in 2100–end. All 69 spans were found, and for each one the cited line is among the hits. Q22 and Q50 are the joined quotes and Q68 needed a direct check:
```
$ python3 -I /tmp/w6scripts/j.py
Q22 in DEC 1744-1745 joined: True | in DEC:1744 alone False | in 1745 alone False
Q50 in RUB 446-447 joined: True
Q68 "Consequence" in VMH:200 True | VMH:201 Detection True
code fences at [2110, 2112, 2124, 2127, 2144, 2147]
Rule block == PROP:20 True
Unblock block == RUB:30-31 True
F4 block == RUB:49-50 True
```
Attack (a): no break.

### Other citations (attack b)
```
UNVERIFI in DECISIONS 2076-2095: 2085 ; "REPORTED BY Amear (DECISION_LOG.md:813)": 2089
DECISIONS.md:2047 = "## 2026-11-10 — D-2026-11-10-B: live-signal topology adopted as the working design (rubric F1; bead Praxis_build-1hv)"
grep Rithmic in DECISIONS 2030-2075: (no lines)
topology :41 ends "... → `SubmitBracket` → Rithmic → account."
proposal :36 "> 4. Session flat gate — ..."   :38 "> 5. Session window (operator lockout) — ..."
handoff "## 1. Hard limits for the VM agent" at :25; :37 begins "9. **Do not install"; :188 "**3.5 Python CLI.**"
handoff :200 "- **Consequence (INFERRED; nothing tried).** ... Then STOP and reply with the output; ..."
R6 design :110 = OPEN-1 row of "## 7. Cross-block conflicts (S6)"
55979ee subject: "F4 graded NOT MET by the auditor, F4 stays FROZEN"
DECISION_LOG.md: 829 lines in the working copy, 826 at HEAD
```
Every `file:N` I checked resolves to the content the entry claims. There is one soft point, MINOR m2: :2047 is the D-2026-11-10-B heading, and that entry's body contains no "Rithmic".

### Proposal A6 / OPEN-F2-5 and A6 text (used in findings M1, M2)
```
proposal :79: | OPEN-F2-5 | Adoption of Rule F2-1. | Amear's approval under A6; then a DECISIONS.md entry and the amended #4/#5 text in the breaker spec. |
DECISIONS.md:1744-1745: A6  FLAG 6: R8 starts the breaker PROPOSAL unit. F2's state / when Amear approves the proposed values.
```

### F2/F4 wording scan (attack d)
```
$ tail -n +2100 DECISIONS.md | grep -n -i -E 'unblock|partly|partial|met\b|satisf|still to be|also requires' | cut -c1-200
30:The unblock clause also requires breaker specs #4 and #5 amended; this entry amends neither, and that is a later unit. This entry does not grade any part of the clause. A6 ties F2's state change to
69:**S6 cross-block.** Block 2 (...). Blo[ck 3 (... breakers #4 and #5 still to be amended to Rule F2-1)]
$ git status --short -- specs/SPEC_RUBRIC.md docs/specs/2026-11-10-f2-session-flat-proposal.md docs/specs/2026-11-10-live-signal-topology.md vm/2026-11-06-vm-handoff.md | wc -l
       0
```
(Offset 30 is DECISIONS.md:2129 and offset 69 is :2168. The bracketed tail of offset 69 was read with `sed -n 2168p`.)

### D1 block vs DECISION_LOG.md:829 (attack f)
DL:829 says, verbatim: "(1) the per-firm settings profile (V3 :53, channel's proposal) is adopted as the design direction for firm rules, MFFU as the first profile, nothing built; (2) the V7 strategy list (:110) is the working scope of the NT8 backtest plan, and R6's first pass moves from Mac-side Python to NT8; (3) MFFU's "we do not offer Rithmic" contradicts D-2026-11-10-B's broker route, which is recorded as contradicted and NOT re-decided here (next unit); (4) the VM-to-n8n path (O1) stays open: the recommended reverse tunnel uses SSH keys, a D2(d) item."
- Decisions 1–3: these match. The additions are scope limiters only ("The profile's contents are not decided here", "D-2026-11-10-B is not edited", "this entry did not re-check them").
- Decision 4: the core matches. The final sentence is extra; see M3.
- The block says "These four are the master's decisions, not Amear's". None of the four is presented as Amear's.

### Identifiers and byte-identity (attack j)
```
$ diff <orig> <new> hunk headers
return-handoff: 65,66c65,66 / 68c68 / 136a137,138   (new 138 lines vs orig 136)
install reply:  17c17                               (28 vs 28)
$ python3 -I /tmp/w6scripts/ph.py
2026-11-10-return-handoff-claude-ai-voice-rulings.md 65 placeholders ['[VM LAN address]', '[MAC]'] match_original_with_placeholders_as_wildcards= True n_captures 2  -> ipv4, mac
... 66 ['[Mac LAN address]', '[Mac tailnet address]'] True -> ipv4, ipv4
... 68 ['[key file]', '[VM LAN address]', '[VM user]'] True -> sshpath, ipv4, other(len=5)
appended new lines beyond original: 2
20261111T172933Z-python-git-install.md 17 ['[VM machine name]'] True -> other(len=15)
$ python3 -I /tmp/w6scripts/ids.py   (removed values pulled from originals at runtime; counts only)
vm_user==amear True ; machine is <SSH host alias>? False
DECISIONS 2100-end vm_lan=0 mac=0 mac_lan=0 mac_tail=0 keyfile=0 machine=0 machine_ci=0 keybase=0 other_ipv4_like= [] mac_like= 0 ssh_paths= []
MANIFEST 388-end   all 0, other_ipv4_like= [] mac_like= 0 ssh_paths= []
return-handoff     all 0, other_ipv4_like= ['8.1.8.4'] (NT8 file version) mac_like= 0 ssh_paths= ['.ssh/config'] (config path, not a key)
install reply      all 0, other_ipv4_like= ['2.56.0.4'] (Git version) mac_like= 0 ssh_paths= []
worker1..5, manager, DECISION_LOG 828-829: all removed-value counts 0
```
The public n8n webhook hostname on return-handoff :66 was not removed, but `git grep -l -F` finds it already in 23 tracked files at HEAD, so this file adds no new exposure. A proxy for the rep-name check (a 4-letter token taken at runtime from an already-staged evidence filename) counts 0 in DECISIONS 2100–end, MANIFEST 388–end and both artifacts. It counts 1 each in workers 3, 4 and 5, each time only inside that existing file path. Whether that token is the rep's name is UNVERIFIED. Attack (j): no break.

### S13 (attack h)
```
return-handoff total=2 standalone=1 last_line_is_S13=yes   (line 5 is the channel's "Standing limitation: ..." sentence; line 138 standalone)
manager.md   total=0 standalone=0 last_line_is_S13=no  lines=35
worker1 total=1 standalone=1 last=yes | worker2 total=3 standalone=1 last=yes | worker3 1/1 yes | worker4 1/1 yes | worker5 1/1 yes
DECISIONS A (2101-2170): standalone=1 total=1 at=70 (=:2170, last line)
DECISIONS B (2172-2199): standalone=1 total=1 at=28 (=:2199, last line)
```

## Findings

**M1 — MAJOR (attack d/g; S2).** DECISIONS.md:2129 says "The unblock clause **also** requires breaker specs #4 and #5 amended; this entry amends neither". :2168 says "breakers #4 and #5 **still** to be amended to Rule F2-1". The clause has two conditions: name the rule and the 15:00 disposition, then amend #4/#5. Writing "also" and "still" right after the entry quotes the rule and the disposition implies the first condition is now met, so F2 reads as partly met. The same paragraph also says "This entry does not grade any part of the clause" while saying the #4/#5 part is unmet, which contradicts itself. The paragraph states the #4/#5 requirement twice (:2129, first and last sentences). Fix: drop "also" and "still". Keep one sentence: "F2 stays FROZEN; this entry grades no part of the unblock clause and changes no rubric state."

**M2 — MAJOR (S2).** DECISIONS.md:2108 says V2 is "filed as closing the A6 hold, OPEN-F2-5 at proposal:79". OPEN-F2-5's own resolution column (proposal :79, pasted above) reads "Amear's approval under A6; then a DECISIONS.md entry and the amended #4/#5 text in the breaker spec." The amended #4/#5 text does not exist, and the entry admits it. Calling OPEN-F2-5 closed reports a tracked open item at a higher state than the evidence supports. Fix: "filed as closing the A6 approval step (the first step of OPEN-F2-5, proposal :79); OPEN-F2-5 stays open until #4/#5 are amended."

**M3 — MAJOR (attack f/g).** In decision 4 (DECISIONS.md:2156), the final sentence says "Decision 4 records that as REPORTED BY Amear (DECISIONS.md:2089) and the tunnel as UNVERIFIED (DECISIONS.md:2085) and keeps O1 open; it does not re-ask him." DL:829's decision 4 contains no recording act and no "does not re-ask him". The same paragraph has already said D-2026-11-10-C does that recording and that "decision 4 does not change that". So the block adds content to a master decision beyond DL:829, against the requirement for exactly the four decisions, and contradicts itself about which entry does the recording. It also leaves a tension unnamed: Amear's ledgered 20:42Z words (DL:813) say "n8n reachability is settled", while decision 4 keeps O1 open and "waits for Amear". Fix: delete the final sentence. Move the D-2026-11-10-C context outside the numbered decision. Optionally add one statement under Open for Amear that his 20:42Z "settled" and decision 4's "stays open" are both on record.

**m1 — MINOR.** The #4/#5 requirement appears twice in the F2 paragraph (:2129). This overlaps M1.
**m2 — MINOR (b).** "D-2026-11-10-B's broker route (DECISIONS.md:2047…)" cites the heading of an entry whose body never names Rithmic (grep of 2030–2075 is empty). The route is only in topology :41. Cite the entry as a pointer, or cite only :41.
**m3 — MINOR (e; upstream).** Decision 1 adopts what the channel left for Amear as O2 ("confirm", return-handoff :72; :53 "Filer: treat the profile design as a proposal for Amear to confirm"). Under D1 this is the master's to decide, and the entry shows it openly. However, Open for Amear does not note that O2's confirmation stays with him. Consider adding it.
**m4 — MINOR (k).** The worker6 MANIFEST row (:399) describes this report as a "re-check of worker 5's fixes and the MANIFEST rows". The brief is a full attack, (a)–(k), on both entries, both artifacts and the MANIFEST. Suggested wording: "attack on D-2026-11-11-A/-B, the de-identified artifacts and the MANIFEST rows".
**m5 — MINOR (k).** The return-handoff row (:389) says "S13 addendum line added". Two lines were added (:137 the filer's note, :138 the S13 line). It also says "network identifiers", but the placeholders include a key-file path and a VM user.
**m6 — MINOR (j).** `[VM user]` replaces a value on return-handoff :68, but that same value (Amear's own name) is left on install reply :17 after the placeholder. It is harmless but inconsistent.
**m7 — observation (h).** The manager report has no S13 line (35 lines, presumably still in progress). It is outside the reports the brief listed.
**m8 — observation.** The return-handoff file carries the S13 sentence twice: embedded in the channel's line 5 and standalone at :138. There is one standalone line, at the end, so S13 is met.

Attacks with no break: (a) 69/69 quotes match; (b) every other citation resolves; (c) no master decision is presented as Amear's and no channel words are attributed to Amear (V2 lockout answer, V5 reading and :107 framing are all labelled as the channel's); (e) nothing found beyond m3; (h) both entries, the return-handoff file and workers 1–5 have exactly one standalone S13 line, placed last; (i) DECISIONS has 100 '+' lines and 0 '-' lines, and 1–2099 equal HEAD; (j) both artifacts match the originals except the placeholder lines and the 2 appended lines, and every removed value counts 0 in all scoped files; (k) the :388 ranges 2101–2170 and 2172–2199 match the headings and `wc -l` 2199, all listed paths exist, MANIFEST 1–387 equals the snapshot, and there are 0 '-' lines. Entry B met every brief requirement I checked.

## Files staged
None. The only file written is this report, and I made no index changes.

## Result
FAIL. 3 MAJOR (M1, M2, M3), 6 MINOR (m1–m6), 2 observations.

Verdict: FAIL

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
