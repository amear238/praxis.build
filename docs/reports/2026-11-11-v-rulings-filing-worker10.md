# Unit 2026-11-11-v-rulings-filing — worker 10 report

## Task
Final adversarial attack (a)–(k) on DECISIONS.md:2100–2203 (D-2026-11-11-A :2101–2174, D-2026-11-11-B :2176–2203), MANIFEST.md:388–403, and the two de-identified files (`docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md`, `vm/replies/20261111T172933Z-python-git-install.md`), after worker 9's fixes.

## Mode
ADVERSARIAL. Read-only except this report. No index changes. Identifiers built at runtime from /tmp/vrf-deid/ and printed as counts or kinds only.

## Criterion
specs/SPEC_RUBRIC.md S1, S2, S4, S5, S8, S13 (verbatim in the brief) and the unit brief's REQUIREMENTS.

## Process log
1. HEAD and line counts checked; both entries read in full (Read tool, DECISIONS.md:2095–2203); return-handoff file, install reply, DECISION_LOG.md:826–829 and MANIFEST.md:386–403 read.
2. (a) Own script `/tmp/w10/quotes.py` finds every double-quoted span on DECISIONS.md:2100–2203 in 11 source files (working copy, HEAD, and `bf6fcc7` blobs), including one-space joins of adjacent lines. Each hit was compared to the cited line. The three ```text blocks were checked with `cmp`.
3. (b) Every `file:N` citation was opened with sed/git show (output below).
4. (c)–(g) Read against DECISION_LOG.md:828–829, the return-handoff file and the install reply.
5. (h) S13 counts in both entries, the return-handoff file, the manager report and workers 1–9.
6. (i) `git diff HEAD -- DECISIONS.md`.
7. (j) Per-line regex proof that the four changed lines differ from the originals only by placeholder substitution. Identifier scan of every target with patterns built from the originals.
8. (k) MANIFEST prefix compared with the snapshot; ranges checked against `grep -n` and `wc -l`; every listed path tested for existence.

## Verification evidence

### HEAD, counts, originals
```
$ git rev-parse --short HEAD && wc -l DECISIONS.md MANIFEST.md && git show HEAD:DECISIONS.md | wc -l
d056e91
    2203 DECISIONS.md
     403 MANIFEST.md
    2099
```

### (a) Quoted spans: `python3 -I /tmp/w10/quotes.py` (full output; each span truncated to 70 chars; hits capped at 8)
```
D2104 [U do them] -> IR:8,DL:825,DL:828,INV:289
D2104 [Amear (chat, 14:38 ET)] -> RH:58
D2106 [Write it now and then send it.] -> RH:10,DL:828
D2106 [Go ahead.] -> RH:82,DL:828
D2108 [flat by 16:00 ET governs; a position open at 15:00 may stay open until] -> RH:46
D2108 [Uh, yeah, you have my approval.] -> RH:47,DL:828
D2108 [Amear's approval under A6; then a DECISIONS.md entry and the amended #] -> PROP:79
D2114 [On a full trading day, at 15:00 ET an open system position stays open.] -> PROP:30
D2114 [Nothing closes it at 15:00.] -> PROP:30
D2116 [flat by 16:00 ET] -> RH:46,DL:828,DEC:327,DEC:329,DEC:341
D2116 [The closing order for every open system position is submitted no later] -> PROP:20
D2116 [(or no later than the exchange's early close on an early-close day)] -> PROP:20
D2116 [the position must be confirmed flat before MFFU's 4:10 PM ET auto-clos] -> PROP:20
D2116 [The system opens no new position from that flat time until 18:00 ET] -> PROP:20
D2116 [New system entries between 15:00 and 16:00 are allowed under Rule F2-1] -> PROP:30
D2116 [Between 15:00 and 18:00 ET Amear's own manual interaction is locked ou] -> PROP:30
D2118 [it only stops the system firing while the account is shut] -> RH:47
D2120 [Trades may be placed beginning at 6:00 PM EST when the Globex session ] -> CAP:10
D2120 [At MyFundedFutures, any open positions will be automatically closed at] -> CAP:12
D2120 [During holiday trading hours, auto-liquidation will not occur at the h] -> CAP:20
D2120 [EST] -> DL:15,DL:17,DL:25,DL:29,DL:31,DL:34,DL:35,DL:47
D2120 [this file reads it as US Eastern local time (ET), an INFERENCE, not st] -> PROP:25
D2129 [its unblock also needs breaker specs #4 and #5 amended] -> DL:828
D2129 [also] -> RH:34,IR:28,DL:24,DL:57,DL:79,DL:95,DL:121,DL:127
D2129 [F2's state changes when Amear approves the proposed values] -> DL:723,DL:725,PROP:8,DEC:2068
D2131 [Yes, however, if uh, I go with a, another prop firm that uh, potential] -> RH:52
D2131 [Having to fuck around.] -> RH:52
D2131 [I don't care about evening entries. It's more about compli uh, the MFF] -> RH:78,DL:828
D2131 [MFFU compliance governs; nothing across the 16:10-18:00 ET close; even] -> DL:828
D2131 [the combined reading] -> DL:828
D2131 [put back to him and not objected to] -> RH:79
D2131 [do not file V3 as closing OPEN-1 until Amear answers] -> RH:55,INV:476
D2131 [A written MFFU answer is needed before any funded use.] -> R6D:110
D2135 [commit everything that we just discussed and the plan for tomorrow is ] -> RH:106
D2135 [I don't remember if I installed the tool to access the NinjaTrader thr] -> RH:107
D2135 [Asked that this check be on tomorrow's (2026-11-11) list.] -> RH:107
D2135 [So cli-nt-bridge is not installed] -> RH:108
D2138 [1. Kindly be informed that we do not offer Rithmic at MFFu] -> RH:120,INV:481
D2138 [2. Kindly be informed that automated trading is allowed provided you a] -> RH:121,INV:482
D2138 [4. You can trade using your strategy at the evaluation phase] -> RH:123,INV:483
D2138 [Funded-account permission for the pattern is not stated; item 4 names ] -> RH:130,INV:484
D2139 [OPEN-1 (evening entry vs overnight) is NOT answered.] -> RH:133,INV:489
D2140 [we see you've been inactive for some time, so this ticket is being clo] -> RH:136,INV:486
D2149 [C3.3 — Replacement ticket] -> INV:1422
D2149 [Amear sends this himself from his logged-in MFFU dashboard.] -> INV:1424
D2153 [firm rules (flat time, overnight holding, other firm limits) live in a] -> RH:53
D2153 [O2 — R6 per-firm profile (V3): confirm.] -> RH:72
D2154 [the Noise-Area baseline (test 2a: 1,190 trades / $197,327.60 on NQCONT] -> RH:110
D2155 [we do not offer Rithmic] -> RH:120,DL:828,DL:829,INV:15,INV:317,INV:465,INV:481,INV:498
D2155 [The path in full is the one at :41.] -> DEC:2054
D2155 [→ Rithmic → account.] -> INV:512,INV:631,TOP:41
D2155 [next unit] -> DL:117,DL:373,DL:515,DL:517,DL:593,DL:597,DL:649,DL:731
D2156 [SSH reverse tunnel from the Mac for sim testing (no new exposure of n8] -> RH:71
D2156 [(d) installing keys, credentials or agent permissions] -> DEC:1974
D2158 [n8n reachability is settled: an SSH reverse tunnel lets the VM reach t] -> DL:813,DEC:2082
D2158 [is settled] -> DL:289,DL:813,DEC:1097,DEC:1280,DEC:2082,VMH:339,VMH:348
D2158 [stays open] -> RH:79,DL:141,DL:485,DL:578,DL:760,DL:801,DL:805,DL:825
D2160 [Any overnight-holding profile needs its own backtest, because current ] -> RH:53
D2164 [the verification details are his to give] -> RH:136,INV:486
D2168 [is settled] -> DL:289,DL:813,DEC:1097,DEC:1280,DEC:2082,VMH:339,VMH:348
D2168 [stays open] -> RH:79,DL:141,DL:485,DL:578,DL:760,DL:801,DL:805,DL:825
D2181 [**Do not install anything else** — not Python, not git, not a package ] -> VMH:37
D2183 [Okay, you know what? Let's forget about the snapshot. Let's have it ex] -> IR:7,DL:828
D2183 [Hermes is going to give me a uh, a physical button to accept or deny, ] -> IR:7
D2183 [U do them] -> IR:8,DL:825,DL:828,INV:289
D2183 [No new snapshot was taken (Amear's choice).] -> IR:9
D2185 [Claude (Claude.ai Praxis channel, Cowork session)] -> IR:2
D2185 [driving the VM over SSH from the Mac (host praxis-vm), commands run fr] -> IR:2
D2187 [the VM is Windows on ARM64 and winget installed the ARM64 builds] -> IR:28
D2189 [NinjaTrader not started, stopped or touched (same pid and start time b] -> IR:25
D2191 [lifted by Amear for this install] -> IR:1
D2193 [for this grant only: Hermes acts as the VM agent over SSH] -> DEC:2085
D2195 [Whether the bridge's dependencies (notably `pyarrow`, also `numpy`) ha] -> IR:28
D2195 [If step 3.5 fails on a build-from-source, the fallback is an x64 Pytho] -> IR:28
D2195 [3.5 Python CLI.] -> VMH:188
D2201 [Consequence] -> DL:253,DL:584,DL:611,DEC:322,DEC:327,DEC:329,DEC:341,DEC:433
D2201 [Detection, after the fact] -> VMH:201
```
Pairing and coverage:
```
$ awk 'NR>=2100 && NR<=2203 {...odd quote count check...}' DECISIONS.md ; quotes.py | grep -c 'NOT FOUND' ; quotes.py | wc -l
total double-quote chars 154 spans 77
0
      77
```
The capped spans whose cited line was not in the first 8 hits were checked directly (DL:829 "next unit" and "stays open"; VMH:200 "Consequence"):
```
$ sed -n '829p' DECISION_LOG.md | grep -o '.\{30\}\(next unit\|stays open\).\{30\}'
cted and NOT re-decided here (next unit); (4) the VM-to-n8n path (O1)
$ git show HEAD:vm/2026-11-06-vm-handoff.md | sed -n 200p   (first 60 chars)
200: - **Consequence (INFERRED; nothing tried).** Without their own ...
```
The two "line break joined" quotes, tested against the cited lines:
```
DECISIONS.md:1744-1745 | join with exactly one space (raw): False | join after dropping next-line indent (4 spaces): True
SPEC_RUBRIC.md:446-447 | join with exactly one space (raw): False | join after dropping next-line indent (4 spaces): True
```
Code blocks:
```
block1 == proposal:20
block2 == rubric:30-31
block3 == rubric:49-50
```

### (b) Cited lines (selection from the sed and git show runs; "..." marks a trimmed line)
```
=== DECISIONS.md 1742,1746
1744: A6  FLAG 6: R8 starts the breaker PROPOSAL unit. F2's state changes
1745:     when Amear approves the proposed values.
=== specs/SPEC_RUBRIC.md 444,448
444:     money; (b) switching live trading on, or any order path to a
445:     funded account; (c) changing circuit-breaker values while real
446:     money is at stake; (d) installing keys, credentials or agent
447:     permissions. Everything else is D1.
=== specs/SPEC_RUBRIC.md 28,32
30: **Unblocks when.** A DECISIONS.md entry names the governing rule and the
31: 15:00 disposition, and breaker specs #4 and #5 are amended to match.
=== specs/SPEC_RUBRIC.md 47,51
48: ### F4 — MFFU automation compliance
49: **Criterion.** Written confirmation from MFFU that this specific automation
50: pattern is permitted on a funded account.
=== vm/2026-11-06-vm-handoff.md 186,202
188: **3.5 Python CLI.** The README (`README.md:43–45@9664d9b`):
200: - **Consequence (INFERRED; nothing tried).** ... Then STOP and reply with the output; ...
201: - **Detection, after the fact.** If `pip`'s output shows any download other than the four named packages, STOP and reply. ...
--- docs/specs/2026-11-10-f2-session-flat-proposal.md:79
| OPEN-F2-5 | Adoption of Rule F2-1. | Amear's approval under A6; then a DECISIONS.md entry and the amended #4/#5 text in the breaker spec. |
--- :36  > 4. Session flat gate — clock reaches 16:00:00 ET, ...
--- :38  > 5. Session window (operator lockout) — clock is in 3:00–6:00 PM ET → ...

### C3.3 — Replacement ticket                       (investigation :1422)
Amear sends this himself from his logged-in MFFU dashboard.   (investigation :1424)
Path: NT8 emitter ... → `SubmitBracket` → Rithmic → account.  (topology :41)
```
```
$ sed -n '2085p;2089p' DECISIONS.md | grep -o -i '.\{80\}unverified.\{60\}'
ey, the firewall rule and the tunnel were set up outside the build loop and are UNVERIFIED by Code; the master installed nothing (master's filing note
ly README.md. Not observed: SSH reachability, the tunnel, n8n from the VM side. UNVERIFIED: whether `/healthz` exists on this n8n; the T4 command form
$ git show bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md | grep -n '^#' (90–115)
100:## 6. How it would be backtested later, and dependencies
106:## 7. Cross-block conflicts (S6)
$ git log --format='%h %s' -1 55979ee   (truncated)
55979ee docs: F4 comparison ... neither reply names NT8 or Rithmic; F4 graded NOT MET by the auditor, F4
$ wc -l DECISION_LOG.md ; git show HEAD:DECISION_LOG.md | wc -l
     829 DECISION_LOG.md
     826
$ git status --short <proposal> <investigation> <topology> specs/SPEC_RUBRIC.md vm/2026-11-06-vm-handoff.md
(no output: all five cited files are tracked and unchanged)
```

### Headings and S13 in the entries (`python3 -I /tmp/w10/head.py`)
```
A heading :2101 exact: True
B heading :2176 exact: True
A substring count 1 standalone at [2174] last line of range ==S True
B substring count 1 standalone at [2203] last line of range ==S True
file total lines 2203 trailing newline True
```

### (h) S13 in reports
```
2026-11-10-return-handoff-claude-ai-voice-rulings.md: lines=138 substr=2 standalone=1 lastline_is_S13=yes standalone_at=138,
2026-11-11-v-rulings-filing-worker1.md: lines=318 substr=1 standalone=1 lastline_is_S13=yes standalone_at=318,
2026-11-11-v-rulings-filing-worker2.md: lines=179 substr=3 standalone=1 lastline_is_S13=yes standalone_at=179,
2026-11-11-v-rulings-filing-worker3.md: lines=277 substr=1 standalone=1 lastline_is_S13=yes standalone_at=277,
2026-11-11-v-rulings-filing-worker4.md: lines=113 substr=1 standalone=1 lastline_is_S13=yes standalone_at=113,
2026-11-11-v-rulings-filing-worker5.md: lines=241 substr=1 standalone=1 lastline_is_S13=yes standalone_at=241,
2026-11-11-v-rulings-filing-worker6.md: lines=241 substr=1 standalone=1 lastline_is_S13=yes standalone_at=241,
2026-11-11-v-rulings-filing-worker7.md: lines=177 substr=1 standalone=1 lastline_is_S13=yes standalone_at=177,
2026-11-11-v-rulings-filing-worker8.md: lines=353 substr=5 standalone=1 lastline_is_S13=yes standalone_at=353,
2026-11-11-v-rulings-filing-worker9.md: lines=160 substr=1 standalone=1 lastline_is_S13=yes standalone_at=160,
2026-11-11-v-rulings-filing-manager.md: lines=35 substr=0 standalone=0 lastline_is_S13=no standalone_at=
```
The return-handoff file's second occurrence is original :5 ("Standing limitation: ..."), not standalone. Byte-identity requires it to stay.

### (i) Append-only
```
$ git diff HEAD --stat -- DECISIONS.md ; ... | grep -c '^-[^-]' ; ... | grep '^@@'
 DECISIONS.md | 104 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 104 insertions(+)
0
@@ -2097,3 +2097,107 @@ The Mac's Hermes agent can now drive the Windows VM over SSH (host praxis-vm, ke
1-2099 identical to HEAD
added 104 context 3
```

### (j) De-identification
```
$ diff /tmp/vrf-deid/<return-handoff> <working copy> | grep -E '^[0-9]'
65,66c65,66
68c68
136a137,138
$ diff /tmp/vrf-deid/<install reply> <working copy> | grep -E '^[0-9]'
17c17
(trailing byte of all four files: 0a)
```
Per-line proof (placeholder becomes a wildcard and must full-match the original line; kind of the captured original printed, not its value):
```
RH65 full match; placeholders: ['[VM LAN address]<-ipv4', '[MAC]<-mac']
RH66 full match; placeholders: ['[Mac LAN address]<-ipv4', '[Mac tailnet address]<-ipv4']
RH68 full match; placeholders: ['[key file]<-ssh-key-path', '[VM LAN address]<-ipv4', '[VM user]<-alnum-name len5']
IR17 full match; placeholders: ['[VM machine name]<-alnum-name len15']
RH [rep] count orig/new: 5 5
n8n URL kept: True | Amear name count orig/new: 23 23
RH new last two lines: ["Filer's addendum, 2026-11-11: standing limitation line added as house style (S13).", 'Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.', '']
RH-orig IPv4-like total 7 version-strings 1 127.0.0.1 2 other 4
IR-orig IPv4-like total 2 version-strings 2 127.0.0.1 0 other 0
VM user equals "amear": True | key path contains comment string hermes-praxis-vm: False | key path has .ssh/: True
machine name == "praxis-vm": False
```
Identifier scan (`python3 -I /tmp/w10/ids3.py`; patterns = 4 original IPv4s, 1 MAC, the machine name, the key path; version strings 2.56.0.4 and 8.1.8.4 excluded and shown as kinds):
```
pattern count 6
DEC2100-2203: original-identifier hits=0 other-IPv4-like=0 kinds=[] MAC-like=0 ssh-key-path-like=0
MAN388-403: original-identifier hits=0 other-IPv4-like=0 kinds=[] MAC-like=0 ssh-key-path-like=0
RH: original-identifier hits=0 other-IPv4-like=1 kinds=['8.1.8.4'] MAC-like=0 ssh-key-path-like=0
IR: original-identifier hits=0 other-IPv4-like=2 kinds=['2.56.0.4'] MAC-like=0 ssh-key-path-like=0
2026-11-11-v-rulings-filing-manager.md: original-identifier hits=0 other-IPv4-like=0 kinds=[] MAC-like=0 ssh-key-path-like=0
2026-11-11-v-rulings-filing-worker1.md: original-identifier hits=0 other-IPv4-like=0 kinds=[] MAC-like=0 ssh-key-path-like=1
2026-11-11-v-rulings-filing-worker2.md: original-identifier hits=0 other-IPv4-like=9 kinds=['2.56.0.4', '8.1.8.4', 'UNKNOWN'] MAC-like=0 ssh-key-path-like=2
2026-11-11-v-rulings-filing-worker3.md: original-identifier hits=0 other-IPv4-like=6 kinds=['2.56.0.4', '8.1.8.4'] MAC-like=0 ssh-key-path-like=0
2026-11-11-v-rulings-filing-worker4.md: original-identifier hits=0 other-IPv4-like=0 kinds=[] MAC-like=0 ssh-key-path-like=0
2026-11-11-v-rulings-filing-worker5.md: original-identifier hits=0 other-IPv4-like=0 kinds=[] MAC-like=0 ssh-key-path-like=0
2026-11-11-v-rulings-filing-worker6.md: original-identifier hits=0 other-IPv4-like=2 kinds=['2.56.0.4', '8.1.8.4'] MAC-like=0 ssh-key-path-like=0
2026-11-11-v-rulings-filing-worker7.md: original-identifier hits=0 other-IPv4-like=0 kinds=[] MAC-like=0 ssh-key-path-like=0
2026-11-11-v-rulings-filing-worker8.md: original-identifier hits=0 other-IPv4-like=7 kinds=['2.56.0.4', '8.1.8.4'] MAC-like=0 ssh-key-path-like=4
2026-11-11-v-rulings-filing-worker9.md: original-identifier hits=0 other-IPv4-like=0 kinds=[] MAC-like=0 ssh-key-path-like=0
20261111T172933Z-python-git-install.md: original-identifier hits=0 other-IPv4-like=2 kinds=['2.56.0.4'] MAC-like=0 ssh-key-path-like=0
20261111T172940Z-STATUS.md: original-identifier hits=0 other-IPv4-like=0 kinds=[] MAC-like=0 ssh-key-path-like=0
```
In worker reports, the remaining "other IPv4-like" hits are 127.0.0.1 (this scan did not exclude it) and one 100.x.x.x net-range mention (masked `ddd.dd.d.d`, context "the Mac's tailnet IPv4 (inside ..."). The `.ssh/` hits are `.ssh/:` scan labels and two `~/.ssh/<...>` placeholders:
```
worker2 ssh-path tail is substring of key basename: False | key basename in tail: False | tail looks like placeholder angle: True   (x2)
done; basename len 9   (key basename found in no unit report)
```

### (k) MANIFEST
```
MANIFEST 1-387 identical to snapshot
     387 /tmp/vrf-manifest-before.md
2101:## 2026-11-11 — D-2026-11-11-A: ...
2176:## 2026-11-11 — D-2026-11-11-B: ...
    2203 DECISIONS.md
EXISTS [ M] /DECISIONS.md 2203L
EXISTS [??] /docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md 138L
EXISTS [??] /vm/replies/20261111T172933Z-python-git-install.md 28L
EXISTS [??] /vm/replies/20261111T172802Z-STATUS.md 1L
EXISTS [??] /vm/replies/20261111T172940Z-STATUS.md 1L
EXISTS [??] /docs/reports/2026-11-11-v-rulings-filing-manager.md 35L
EXISTS [??] /docs/reports/2026-11-11-v-rulings-filing-worker1.md 318L
  ... worker2–worker9: all EXISTS [??]
MISSING /docs/reports/2026-11-11-v-rulings-filing-worker10.md
STATUS contents (od -c): S T A R T E D \n F I N I S H E D \n
```
Row :388 says "lines 2101-2174 (heading :2101)", "lines 2176-2203 (heading :2176)", "lines 1-2099 unchanged". All three match. `worker10.md` was missing only because it is this report. The manager report is still being written: it says "Result: BLOCKED (in progress)" and has no S13 line yet.

Index state:
```
$ git diff --cached --stat
 docs/reports/evidence/[2026-10-28 MFFU reply image, filename withheld] | Bin 0 -> 254350 bytes
index entries staged:        1
```
The only staged file is the PNG. It was staged before this unit and was not touched.

### (f) D1 block vs DECISION_LOG.md:829
DL:829 items (from the printout above): "(1) the per-firm settings profile (V3 :53, channel's proposal) is adopted as the design direction for firm rules, MFFU as the first profile, nothing built; (2) the V7 strategy list (:110) is the working scope of the NT8 backtest plan, and R6's first pass moves from Mac-side Python to NT8; (3) MFFU's "we do not offer Rithmic" contradicts D-2026-11-10-B's broker route, which is recorded as contradicted and NOT re-decided here (next unit); (4) the VM-to-n8n path (O1) stays open: the recommended reverse tunnel uses SSH keys, a D2(d) item."
- 1 (:2153): same decision. Adds an O2 pointer and "The profile's contents are not decided here." inside the item.
- 2 (:2154): same decision. Adds "The list and its P&L figure are the channel's ...; this entry did not re-check them." inside the item.
- 3 (:2155): same decision. Adds "D-2026-11-10-B is not edited." and the :2054/:41 citations.
- 4 (:2156): same decision; "uses SSH keys" is kept. Adds "so it waits for Amear". The D-2026-11-10-C context is now outside the item, in a paragraph labelled "Context for decision 4 (not part of it)" (:2158).
- The block names exactly four items. The heading (:2151) and the Status line (:2103) present them as the master's, not Amear's.

## Findings

No MAJOR.

**m1 — MINOR (a).** Two quotes labelled "line break joined" match their cited lines only after the 4-space hanging indent of the second line is also dropped: :2129 (DECISIONS.md:1744–1745) and :2156 (SPEC_RUBRIC.md:446–447). Evidence: "join with exactly one space (raw): False | ... dropping next-line indent (4 spaces): True". The text itself is identical; the difference is whitespace from hard wrapping. The brief allows one space for the join, so this reads as within the rule, but :2104 claims "byte-identical". Fix: label these quotes "line break and indent joined".

**m2 — MINOR (b).** :2104 calls "U do them" "Amear's go" for this filing and cites DECISION_LOG.md:828. In DL:828 those words sit only in the ALSO part, on the limit 9 lift. The line that says they also cover filing the note is install reply :8 ("on the two open items (file the 2026-11-10 note; install Python and git in the VM)"). Fix: add "install reply :8" as the source for the scope of the go.

**m3 — MINOR (g).** :2108 files V2 as closing "the A6 hold, that is, Amear's approval". :2129 quotes A6 ("F2's state changes when Amear approves the proposed values") and then says "whether A6 is triggered is not graded here". A reader can ask how the A6 approval is closed while the A6 trigger is ungraded. The words "on the words put to him" and element (f) do reconcile the two, and the brief requires both statements. Fix (optional): at :2129, say that the hold is closed on the summary at return-handoff :46, and that whether that summary is "the proposed values" in A6 is not graded.

**m4 — MINOR (f).** Context sits inside numbered items 1–4 without a label: item 1's O2 pointer and "The profile's contents are not decided here."; item 2's "did not re-check them"; item 3's "D-2026-11-10-B is not edited."; item 4's "so it waits for Amear". None changes a decision. Item 1's "contents are not decided" could be read as narrowing the adopted proposal, because the quoted :53 text names what goes in the profile (flat time, overnight holding, other firm limits). Fix: move these sentences into a labelled "Context (not part of the decisions)" line, as was done for decision 4.

**m5 — MINOR (S2 wording).** The S6 line at :2172 says "Rule F2-1 approved" without the qualifier used at :2108 ("on the words put to him at return-handoff :46"). Fix: "Rule F2-1 approved on the summary put to him".

**m6 — MINOR (b).** :2193 says "the work is stamped 17:29:33Z". 17:29:33Z is the install reply's stamp, written when the work finished. Its STATUS marker `20261111T172802Z-STATUS.md` (content `STARTED`, MANIFEST :391) dates the start to 17:28:02Z. The conclusion (the work came before the ledger append) still holds. Fix: "the work ran 17:28:02Z–17:29:33Z (STATUS markers and install reply :3)".

**m7 — MINOR (c).** :2135 puts Amear's question about "the tool to access the NinjaTrader through a bash command" next to "So cli-nt-bridge is not installed". The return-handoff file does not say that cli-nt-bridge is the tool he meant. Fix: add "whether cli-nt-bridge is the tool he meant is not stated in the file".

**m8 — MINOR (S2).** :2199 calls the channel's further SSH driving of the VM "an agent-permission item, D2(d)". That is the filer's reading, and it is not labelled. It matches D-2026-11-10-C's reading for Hermes (DECISIONS.md:2085). Fix: add "(this entry's reading)".

**Notes, not findings against the artifacts:**
- N1 (S4/S5, process). As entry B states, the install ran on voice/chat words before any ledger append or DECISIONS entry (17:28–17:29Z against DL:828 at 18:19:40Z). The filing cannot cure this, and it does not hide it. It belongs to the master or Amear.
- N2 (S8, master's decision). Decision 1 adopts the profile direction that the channel's file left for Amear to confirm (return-handoff :53 "Filer: treat the profile design as a proposal for Amear to confirm"; :72 O2). The entry files DL:829 faithfully and keeps O2 under Open for Amear. Whether the master should decide under D1 at all is the master's question.
- N3 (k, pending). The manager report has no S13 line yet and says "Result: BLOCKED (in progress)". This report did not exist when the MANIFEST check ran.
- N4 (UNVERIFIED). The rep-name check was not run, because the name is not in the /tmp originals (both have `[rep]`, 5 = 5) and must not be typed.

## Cases tried with no break
- All 77 double-quoted spans (75 found directly on their cited lines, 2 with line-plus-indent joins) and the 3 code blocks match their sources.
- Every message id, thread id, time and install path matches its source.
- Both headings are exact.
- S13 is correct in both entries, the return-handoff file and workers 1–9.
- DECISIONS.md is append-only: 0 lines removed, 104 added after :2099.
- MANIFEST 1–387 equals the snapshot, and the :388 ranges match.
- The four changed lines differ from the originals only by placeholder substitution, of the right kinds.
- 0 original identifiers appear in any target or unit report.
- `[rep]`, Amear's name and the n8n URL are unchanged.
- Nothing states or implies that F2 or F4 is met or unblocked, and no rubric state changes. :2129 explicitly refuses the "also" reading.
- No question that is Amear's is answered for him.

## Files staged
None. This report is untracked; the index was not touched.

## Result: NO MAJOR FOUND (8 MINOR, 4 notes)

Verdict: PASS

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
