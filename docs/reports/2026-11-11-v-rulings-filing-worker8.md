# Unit 2026-11-11-v-rulings-filing — worker 8 (ADVERSARIAL)

## Task
Attack DECISIONS.md 2100–2200 (D-2026-11-11-A :2101–2171, D-2026-11-11-B :2173–2200), MANIFEST.md :388–401, the de-identified return-handoff file and the de-identified install reply. Attacks (a)–(k) from the brief. Read-only except this report.

## Mode
ADVERSARIAL. HEAD `d056e91`, branch main. My scripts are in /tmp/w8scripts/ (written this session, no other worker's script reused). Removed identifiers were built at run time from /tmp/vrf-deid/; only counts and lengths are printed below. No git index changes, no memory writes, no network.

## Criterion
specs/SPEC_RUBRIC.md S1, S2, S4, S5, S8, S13 (verbatim in the brief) and the unit brief's REQUIREMENTS list.

## Process log
1. Line counts, HEAD line counts, temp originals present.
2. Diffed both artifacts against /tmp/vrf-deid/ originals; token-level check of removed identifiers against all targets (counts only).
3. Generic scans: IPv4, MAC, `.ssh/`.
4. S13 counts and positions in both entries, the return-handoff file, worker reports 1–7, manager report.
5. `git diff HEAD` on DECISIONS.md and MANIFEST.md; prefix byte-identity.
6. Own script: every double-quoted span in DECISIONS.md 2100–2200 located in its source files, with two-line join detection; code-block quotes compared with `cmp`; backtick values and message ids checked.
7. Read every cited line (return-handoff, install reply, DECISION_LOG.md :828–829, proposal :20/:25/:30/:36/:38/:79, rubric :30–31/:49–50/:446–447, DECISIONS.md :1744–1745/:2054/:2076/:2082/:2085/:2089, handoff :37/:188/:200/:201, investigation :1422/:1424, topology :41, bf6fcc7 capture :10/:12/:20, bf6fcc7 R6 design :110).
8. D1 block compared with DECISION_LOG.md:829 item by item; F2/F4 wording scan; worker 6 findings checked against the current text.

## Verification evidence

### Counts and originals
```
$ git rev-parse --short HEAD && wc -l DECISIONS.md MANIFEST.md && git show HEAD:DECISIONS.md | wc -l && ls -la /tmp/vrf-deid/ /tmp/vrf-manifest-before.md && ls docs/reports/2026-11-11-v-rulings-filing*
d056e91
    2200 DECISIONS.md
     401 MANIFEST.md
    2601 total
    2099
-rw-r--r--@ 1 admin  wheel  173379 Nov 11 13:34 /tmp/vrf-manifest-before.md
/tmp/vrf-deid/:
-rw-r--r--@   1 admin  wheel  13733 Nov 11 13:23 2026-11-10-return-handoff-claude-ai-voice-rulings.md
-rw-r--r--@   1 admin  wheel   3168 Nov 11 13:23 20261111T172933Z-python-git-install.md
docs/reports/2026-11-11-v-rulings-filing-manager.md
docs/reports/2026-11-11-v-rulings-filing-worker1.md
... worker2 … worker7 (all present)
```

### (j) Artifacts vs originals
```
$ diff <orig> <new> | grep -E '^[0-9]'
== docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md
     138 (new)   136 (orig)
65,66c65,66
68c68
136a137,138
== vm/replies/20261111T172933Z-python-git-install.md
      28 (new)    28 (orig)
17c17
```
```
$ python3 -I /tmp/w8scripts/deid.py dec.txt man.txt <return-handoff> <install reply>
2026-11-10-return-handoff-claude-ai-voice-rulings.md replace old 65 66 new 65 66
  removed tokens: 4 lengths [13, 17, 17, 18]
  added tokens (safe to show, from de-identified): [':5678']
2026-11-10-return-handoff-claude-ai-voice-rulings.md replace old 68 68 new 68 68
  removed tokens: 3 lengths [5, 9, 13]
  added tokens (safe to show, from de-identified): ['LAN', 'address', 'user']
2026-11-10-return-handoff-claude-ai-voice-rulings.md insert old 137 136 new 137 138
  removed tokens: 0 lengths []
  added tokens (...): ['.', '1-minute', '2', '2026-11-11:', 'Filer', 'Fills', 'S13', ... 'ticks']
20261111T172933Z-python-git-install.md replace old 17 17 new 17 17
  removed tokens: 1 lengths [21]
  added tokens (safe to show, from de-identified): ['VM', '\\amear', 'machine', 'name']
candidate identifier tokens: 11
praxis-vm among removed tokens/parts: False
```
(The SSH host alias left on install reply :2 and return-handoff :68 is not the removed machine name; it is already in tracked files at HEAD, e.g. DECISIONS.md:2082.)
```
$ python3 -I /tmp/w8scripts/deid3.py dec.txt man.txt <return-handoff> <install reply> docs/reports/2026-11-11-v-rulings-filing-*.md
dec.txt 0
man.txt 0
2026-11-10-return-handoff-claude-ai-voice-rulings.md 0
20261111T172933Z-python-git-install.md 0
2026-11-11-v-rulings-filing-manager.md 0
2026-11-11-v-rulings-filing-worker1.md 0
... worker2–worker7: 0 each
identifier candidates: 7 total case-insensitive hits: 0
```
```
$ (IPv4 / MAC / .ssh/ scan)
== dec.txt          IPv4-like: 1 127.0.0.1;  MAC: 0  .ssh/: 0
== man.txt          IPv4-like: (none)        MAC: 0  .ssh/: 0
== return-handoff   IPv4-like: 2 127.0.0.1; 1 8.1.8.4;  MAC: 0  .ssh/: 1
== install reply    IPv4-like: 2 2.56.0.4;  MAC: 0  .ssh/: 0
 "Found Git [Git.Git] Version 2.56.0.4 … Downloa
ownload/v2.56.0.windows.4/Git-2.56.0.4-arm64.exe
108:elf-report.md` — NT8 running (pid 9600, 8.1.8.4 file version), `pyt
68: Hermes): key `[key file]` (comment `hermes-…`), `~/.ssh/config` Host `…` → [VM LAN addre
```
8.1.8.4 is NT8's file version; 2.56.0.4 is git's version. The only `.ssh/` path is `~/.ssh/config`, not a key path; the key file is `[key file]`. The webhook's public hostname on return-handoff :66 is unchanged from the original and is already in 23 tracked files at HEAD (`git grep -lF <domain> HEAD | wc -l` → 23); not a de-identification item.

### (i) DECISIONS.md append-only; (k) MANIFEST prefix
```
$ git diff HEAD -- DECISIONS.md | grep -E '^@@'
@@ -2097,3 +2097,104 @@ ...
minus lines: 0
$ git diff HEAD -- DECISIONS.md | grep -c '^+[^+]' ; ... grep -c '^+$'
62
39
$ cmp <(git show HEAD:DECISIONS.md) <(head -n 2099 DECISIONS.md) && echo "first 2099 identical"
first 2099 identical
$ cmp <(head -n 387 /tmp/vrf-manifest-before.md) <(head -n 387 MANIFEST.md) && echo "MANIFEST 1-387 identical"
MANIFEST 1-387 identical
     387 /tmp/vrf-manifest-before.md
$ git diff HEAD -- MANIFEST.md | grep -E '^@@'
@@ -304,6 +304,14 @@
@@ -377,3 +385,17 @@
```
101 added lines (62 non-blank + 39 blank) = lines 2100–2200; 0 removed. MANIFEST's first hunk (:307–314) is another unit's working-copy rows and is inside the snapshot's 1–387.

### (k) MANIFEST ranges and paths
```
$ grep -n '^## 2026-11-11' DECISIONS.md ; wc -l DECISIONS.md
2101:## 2026-11-11 — D-2026-11-11-A: ...
2173:## 2026-11-11 — D-2026-11-11-B: ...
    2200 DECISIONS.md
```
Row :388 says "appended at lines 2101-2171 (heading :2101)" and "lines 2173-2200 (heading :2173)": match.
```
exists ./DECISIONS.md tracked
exists ./docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md untracked
exists ./vm/replies/20261111T172933Z-python-git-install.md untracked
exists ./vm/replies/20261111T172802Z-STATUS.md untracked
exists ./vm/replies/20261111T172940Z-STATUS.md untracked
exists ./docs/reports/2026-11-11-v-rulings-filing-manager.md untracked
exists ./docs/reports/2026-11-11-v-rulings-filing-worker1.md … worker7.md untracked
MISSING ./docs/reports/2026-11-11-v-rulings-filing-worker8.md
STARTED
|
FINISHED
|
```
worker8.md is this report (being written). The manager report exists but is in progress ("Result: BLOCKED (in progress…)", "## S6 cross-block check (pending)"). All 22 rows at :380–401 have 7 `|`-fields; types follow file convention (DECISIONS.md → Log ×15, vm/replies → Reply).

### (h) S13
```
$ (per file: contains / standalone / last non-blank line is S13)
return-handoff  contains=2 standalone=1 last-nonblank-is-S13=yes lines=138
manager         contains=0 standalone=0 last-nonblank-is-S13=no  lines=35
worker1 1/1/yes  worker2 3/1/yes  worker3 1/1/yes  worker4 1/1/yes
worker5 1/1/yes  worker6 1/1/yes  worker7 1/1/yes
$ grep -nF "$S" return-handoff worker2
return-handoff:5:Standing limitation: Fills are optimistic; ...     (pre-existing, prefixed, not standalone)
return-handoff:138:Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
worker2:74:> Fills are ...   (quoted evidence)
worker2:130:     3	Fills are ...   (quoted evidence)
worker2:179:Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
$ grep -nF "$S" DECISIONS.md | awk -F: '$1>2099' ; grep -cxF "$S" dec.txt
2171:Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
2200:Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
2
```
Entry A ends at :2171 with S13 (blank :2172, then B's heading); entry B ends at :2200 with S13. Pass for both entries, the return-handoff file and workers 1–7. Manager report: pending.

### (a) Quotes — `python3 -I /tmp/w8scripts/quotes.py` (full output)
```
D2104 [U do them] -> IR:8, DL:825, DL:828, INV:289
D2106 [Write it now and then send it.] -> RH:10, DL:828
D2106 [Go ahead.] -> RH:82, DL:828
D2108 [flat by 16:00 ET governs; a position open at 15:00 may st...] -> RH:46
D2108 [Uh, yeah, you have my approval.] -> RH:47, DL:828
D2108 [Amear's approval under A6; then a DECISIONS.md entry and ...] -> PROP:79
D2114 [On a full trading day, at 15:00 ET an open system positio...] -> PROP:30
D2114 [Nothing closes it at 15:00.] -> PROP:30
D2116 [flat by 16:00 ET] -> RH:46, DL:828, DEC:327, DEC:329, DEC:341
D2116 [The closing order for every open system position is submi...] -> PROP:20
D2116 [(or no later than the exchange's early close on an early-...] -> PROP:20
D2116 [the position must be confirmed flat before MFFU's 4:10 PM...] -> PROP:20
D2116 [The system opens no new position from that flat time unti...] -> PROP:20
D2116 [New system entries between 15:00 and 16:00 are allowed un...] -> PROP:30
D2116 [Between 15:00 and 18:00 ET Amear's own manual interaction...] -> PROP:30
D2118 [it only stops the system firing while the account is shut] -> RH:47
D2120 [Trades may be placed beginning at 6:00 PM EST when the Gl...] -> CAP:10
D2120 [At MyFundedFutures, any open positions will be automatica...] -> CAP:12
D2120 [During holiday trading hours, auto-liquidation will not o...] -> CAP:20
D2120 [EST] -> DL:15, DL:17, DL:25, DL:29, DL:31, DL:34 (+353 more)
D2120 [this file reads it as US Eastern local time (ET), an INFE...] -> PROP:25
D2129 [its unblock also needs breaker specs #4 and #5 amended] -> DL:828
D2129 [F2's state changes when Amear approves the proposed values] -> DL:723, DL:725, PROP:8, DEC:1672-1673J, DEC:1744-1745J, DEC:2068
D2131 [Yes, however, if uh, I go with a, another prop firm that ...] -> RH:52
D2131 [Having to fuck around.] -> RH:52
D2131 [I don't care about evening entries. It's more about compl...] -> RH:78, DL:828
D2131 [MFFU compliance governs; nothing across the 16:10-18:00 E...] -> DL:828
D2131 [the combined reading] -> DL:828
D2131 [put back to him and not objected to] -> RH:79
D2131 [do not file V3 as closing OPEN-1 until Amear answers] -> RH:55, INV:476
D2131 [A written MFFU answer is needed before any funded use.] -> R6D:110
D2135 [commit everything that we just discussed and the plan for...] -> RH:106
D2135 [I don't remember if I installed the tool to access the Ni...] -> RH:107
D2135 [Asked that this check be on tomorrow's (2026-11-11) list.] -> RH:107
D2135 [So cli-nt-bridge is not installed] -> RH:108
D2138 [1. Kindly be informed that we do not offer Rithmic at MFFu] -> RH:120, INV:481
D2138 [2. Kindly be informed that automated trading is allowed p...] -> RH:121, INV:482
D2138 [4. You can trade using your strategy at the evaluation phase] -> RH:123, INV:483
D2138 [Funded-account permission for the pattern is not stated; ...] -> RH:130, INV:484
D2139 [OPEN-1 (evening entry vs overnight) is NOT answered.] -> RH:133, INV:489
D2140 [we see you've been inactive for some time, so this ticket...] -> RH:136, INV:486
D2149 [C3.3 — Replacement ticket] -> INV:1422
D2149 [Amear sends this himself from his logged-in MFFU dashboard.] -> INV:1424
D2153 [firm rules (flat time, overnight holding, other firm limi...] -> RH:53
D2153 [O2 — R6 per-firm profile (V3): confirm.] -> RH:72
D2154 [the Noise-Area baseline (test 2a: 1,190 trades / $197,327...] -> RH:110
D2155 [we do not offer Rithmic] -> RH:120, DL:828, DL:829, INV:15, INV:317, INV:465 (+4 more)
D2155 [The path in full is the one at :41.] -> DEC:2054
D2155 [→ Rithmic → account.] -> INV:512, INV:631, TOP:41
D2155 [next unit] -> DL:117, DL:373, ... (+16 more)
D2156 [SSH reverse tunnel from the Mac for sim testing (no new e...] -> RH:71
D2156 [(d) installing keys, credentials or agent permissions] -> RUB:446-447J, DEC:1915-1916J, DEC:1974
D2156 [n8n reachability is settled: an SSH reverse tunnel lets t...] -> DL:813, DEC:2082
D2156 [is settled] -> DL:289, DL:813, DEC:1097, DEC:1280, DEC:2082, VMH:339 (+1 more)
D2156 [stays open] -> RH:79, DL:141, DL:485, ... (+13 more)
D2158 [Any overnight-holding profile needs its own backtest, bec...] -> RH:53
D2162 [the verification details are his to give] -> RH:136, INV:486
D2178 [**Do not install anything else** — not Python, not git, n...] -> VMH:37
D2180 [Okay, you know what? Let's forget about the snapshot. Let...] -> IR:7, DL:828
D2180 [Hermes is going to give me a uh, a physical button to acc...] -> IR:7
D2180 [U do them] -> IR:8, DL:825, DL:828, INV:289
D2180 [No new snapshot was taken (Amear's choice).] -> IR:9
D2182 [Claude (Claude.ai Praxis channel, Cowork session)] -> IR:2
D2182 [driving the VM over SSH from the Mac (host …), co...] -> IR:2
D2184 [the VM is Windows on ARM64 and winget installed the ARM64...] -> IR:28
D2186 [NinjaTrader not started, stopped or touched (same pid and...] -> IR:25
D2188 [lifted by Amear for this install] -> IR:1
D2190 [for this grant only: Hermes acts as the VM agent over SSH] -> DEC:2085
D2192 [Whether the bridge's dependencies (notably `pyarrow`, als...] -> IR:28
D2192 [If step 3.5 fails on a build-from-source, the fallback is...] -> IR:28
D2192 [3.5 Python CLI.] -> VMH:188
D2198 [Consequence] -> DL:253, DL:584, DL:611, DEC:322, DEC:327, DEC:329 (+6 more)
D2198 [Detection, after the fact] -> VMH:201
quotes: 73
curly '“' 0
curly '”' 0
```
Every one of the 73 quotes is found in the line the entry cites ("next unit" and "stays open" checked in DL:829: `grep -c` → 1 and 1; "Consequence" is in VMH:200). The two joins (DEC:1744–1745, RUB:446–447) are marked "line break joined". Code blocks:
```
block1 == PROP:20
block2 == RUB:30-31
block3 == RUB:49-50
```
Backtick values and message ids:
```
D2106 id 1a1c6ef68efc93d2: in RH True
D2106 id 19f9edc188595b0c: in RH True
D2106 id 1a1c7a6d7d0d0dec: in RH True
D2138 id 1a1c6fce04330f0d: in RH True
D2139 id 1a1c7b82f130416b: in RH True
D2140 id 1a1cb3255cf62d16: in RH True
D2184 [Python 3.12.10] IR lines: [19]
D2184 [C:\Program Files\Python312-arm64\python.exe] IR lines: [19]
D2184 [-V:3.12-arm64 *] IR lines: [19]
D2184 [PYTHON_EXIT=0] IR lines: [18]
D2184 [git version 2.56.0.windows.4] IR lines: [19]
D2184 [C:\Program Files\Git\cmd\git.exe] IR lines: [19]
D2184 [GIT_EXIT=0] IR lines: [18]
D2184 [PROCESSOR_ARCHITECTURE=ARM64] IR lines: [19]
D2190 [UTC: 20261111T172933Z] IR lines: [3]
```
"the brief itself is not on disk" (:2131): `grep -rlF 'MFFU compliance governs' .` (excluding .git) → DECISIONS.md, DECISION_LOG.md, worker1/3/5/6 reports only.

### (d)/(b) Evidence for the findings
```
D2129:
DECISION_LOG.md:828 records "its unblock also needs breaker specs #4 and #5 amended" (copied by script from DECISION_LOG.md:828). This entry amends neither (that is a later unit) and grades no part of the unblock clause. A6 ties F2's state change to Amear's approval ("F2's state changes when Amear approves the proposed values", DECISIONS.md:1744–1745, line break joined); this entry changes no rubric state.
DL828 fragment:
F2 stays FROZEN (its unblock also needs breaker specs #4 and #5 amended)
w6 M1 fix text:
Fix: drop "also" and "still".

D2164:
- A header-bearing export of the outgoing messages is his to file (return-handoff :43).
RH:43 tail:
A header-bearing export of the outgoing message (Gmail "Show original") is Amear's to file if the auditor wants headers, not this summary.

RH:58 (V4 source):
- Amear (chat, 14:38 ET): "check whether
D2101 title:
## 2026-11-11 — D-2026-11-11-A: Amear's rulings V1–V7 (Claude.ai channel voice sessions, 2026-11-10) and M

D2104 source sentence:
The source of every ruling below is `docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md` (called the return-handoff file below;
D2131 answered:
The ambiguity the channel flagged at return-handoff :55 ("do not file V3 as closing OPEN-1 until Amear answers") is answered by V5. V3 does not close OPE
D2167:
It edits no spec, no rubric, no handoff
D2156 / DL829 item 4:
that tunnel would use SSH keys
(4) the VM-to-n8n path (O1) stays open: the recommended reverse tunnel uses SSH keys, a D2(d) item.
MANIFEST :389 / :401:
network identifiers replaced by placeholders
re-check of worker 7's fixes
placeholders in RH:
   1 [MAC]
   1 [Mac LAN address]
   1 [Mac tailnet address]
   2 [VM LAN address]
   1 [VM user]
   1 [key file]
```
A6 (DECISIONS.md:1743–1745, inside D-2026-11-08-B, heading :1710):
```
A6  FLAG 6: R8 starts the breaker PROPOSAL unit. F2's state changes
    when Amear approves the proposed values.
```

### (f) D1 block vs DECISION_LOG.md:829
DL:829 text (pasted in full in the process read): "(1) the per-firm settings profile (V3 :53, channel's proposal) is adopted as the design direction for firm rules, MFFU as the first profile, nothing built; (2) the V7 strategy list (:110) is the working scope of the NT8 backtest plan, and R6's first pass moves from Mac-side Python to NT8; (3) MFFU's "we do not offer Rithmic" contradicts D-2026-11-10-B's broker route, which is recorded as contradicted and NOT re-decided here (next unit); (4) the VM-to-n8n path (O1) stays open: the recommended reverse tunnel uses SSH keys, a D2(d) item."
- 1: same decision; adds O2 context and "The profile's contents are not decided here." No change to the decision.
- 2: same; adds "the channel's … this entry did not re-check them." No change.
- 3: same; adds "D-2026-11-10-B is not edited." No change.
- 4: same core; "uses" becomes "would use"; adds "so it waits for Amear", D-2026-11-10-C context, Amear's 20:42Z quote and "recorded here, not resolved" inside the numbered item (see m5).
- :2152 "These four are the master's decisions, not Amear's." None is presented as Amear's.

## Findings

**M1 — MAJOR (attack d; requirement "no part of the clause graded").** :2129 quotes DECISION_LOG.md:828: "its unblock also needs breaker specs #4 and #5 amended". The word "also" comes right after the entry restates Rule F2-1 (:2111) and the 15:00 disposition (:2114), which are exactly the first condition of the unblock clause (:2125–2126). So the line implies the first condition is now met and F2 is partly met. The entry then says it "grades no part of the unblock clause", which contradicts the quote it just used. This brings back worker 6's M1 through a quotation (worker 6's fix: 'drop "also" and "still"'). Quoting it correctly does not remove the implication. Fix: delete the DL:828 quote from :2129 and keep "This entry amends neither breaker spec #4 nor #5 (a later unit) and grades no part of the unblock clause." If the quote must stay, add: "the ledger's 'also' is its wording; this entry does not read any part of the clause as met."

**M2 — MAJOR (attack b; S2).** :2164 "A header-bearing export of the outgoing messages is his to file (return-handoff :43)." The cited line says "outgoing message" (singular, in the V1 section) and "is Amear's to file if the auditor wants headers". The entry makes it plural, so it now covers V6, which :43 does not mention, and drops the condition. This puts an unconditional task on Amear's Open list that the cited line does not support. Fix: "If the auditor wants headers, a header-bearing export of the V1 outgoing message is his to file (return-handoff :43)." Optionally add "(V6: no statement in the file)".

**m1 — MINOR (g).** :2129 quotes A6, "F2's state changes when Amear approves the proposed values", just after V2's approval, then says "this entry changes no rubric state" without saying why A6 is not triggered. In A6, "the proposed values" are the breaker PROPOSAL unit's values; the #4/#5 text was not put to him (:2116 (f)). Fix: add one clause, e.g. "the #4/#5 values A6 refers to were not put to him (element (f)); A6 is not graded here."

**m2 — MINOR (S2; c).** :2131 "The ambiguity … is answered by V5." This is not graded. The answer rests on V5's words plus the combined reading in Amear's brief, which reached the master through the channel (DL:828). The channel's own reading is INFERRED (:79). Fix: "is answered by V5 as the combined reading relayed in DECISION_LOG.md:828 states it (REPORTED BY the Claude.ai channel)."

**m3 — MINOR (g).** :2104 "The source of every ruling below is [the return-handoff file]", but the combined V3+V5 ruling at :2131 is sourced from DECISION_LOG.md:828 (Amear's brief, relayed), not from that file. Fix: "… every ruling below except the combined V3/V5 reading (DECISION_LOG.md:828)".

**m4 — MINOR (wording).** Title :2101 reads "V1–V7 (Claude.ai channel voice sessions, 2026-11-10)", but V4's words are from chat (return-handoff :58 "Amear (chat, 14:38 ET)"). DL:828 has the same framing. Fix: "voice sessions and chat".

**m5 — MINOR (f).** Decision 4 (:2156) still carries the D-2026-11-10-C context, Amear's 20:42Z quote and "recorded here, not resolved" inside the numbered master decision. It also softens DL:829's "uses SSH keys" to "would use". Worker 6's M3 fix said to move the context outside the numbered item, and that was not done. None of this changes the decision, but the block is meant to hold exactly DL:829's four. Fix: put "uses" back; move the sentences from "D-2026-11-10-C records …" to "… not resolved" into a "Context, not part of decision 4" paragraph.

**m6 — MINOR (e).** The difference between Amear's 20:42Z "n8n reachability is settled" and decision 4's "stays open" is "recorded here, not resolved", but no owner is named and it is not under Open for Amear (worker 6 M3 suggested this as optional). Fix: add one Open-for-Amear statement: "Both his 20:42Z 'is settled' and decision 4's 'stays open' are on record; which stands is his."

**m7 — MINOR (g; duplication).** "Amear sends it himself" appears three times (:2149 quote, :2149 sentence, :2163). "Item 4 names the evaluation phase only" (:2138) repeats the channel's reading in the next sentence. The "master's, not Amear's" note is in both :2103 and :2152. Fix: keep one of each.

**m8 — MINOR (g).** :2167 "It edits no spec, no rubric, no handoff". This unit did edit the return-handoff file (de-identified :65–66 and :68, appended :137–138). The sentence is about the entry, but "no handoff" next to a file called the return-handoff file reads as a contradiction. Fix: "no VM handoff".

**m9 — MINOR (k).** MANIFEST :389 says "network identifiers replaced by placeholders", but two of the placeholders, `[key file]` and `[VM user]`, are not network identifiers. This is the part of worker 6's m5 that was not fixed. Fix: "network identifiers, the key file name and the VM user replaced by placeholders".

**m10 — MINOR (k).** MANIFEST :401 describes this report as a "re-check of worker 7's fixes". The brief is a full (a)–(k) attack on both entries, both artifacts and the MANIFEST rows. Fix: "attack (a)–(k) on D-2026-11-11-A/-B, the de-identified files, S13 and the MANIFEST rows after worker 7's fixes; FAIL, 2 MAJOR, 10 MINOR".

**Pending, not graded.** The manager report (:393 row) is in progress: no S13 line yet and its S6 section is "(pending)". This report (:401 row) did not exist until now.

**Cases tried with no break:** all 73 double-quoted spans and 3 code blocks are byte-identical to their cited lines; all message and thread ids, install values and paths match their sources; S13 is correct in both entries, the return-handoff file and workers 1–7; DECISIONS.md is append-only (0 removed, 101 added after :2099); MANIFEST 1–387 equals the snapshot and the :388 ranges match the headings and `wc -l`; zero removed identifiers in any target (checked case-insensitively, including workers 1–7 and the manager report); no IPv4 other than 127.0.0.1 and version strings, no MAC, no key path; the artifacts differ from the originals only at the placeholder lines and the two appended lines. F4 is not re-graded (:2142, :2167). Entry B meets every listed requirement: limit 9 at :37, IR :7–9, who did it, :18–19, :24–25, no snapshot, one install only, S4/S5 order not held, :2085 reading, OPEN RISK UNVERIFIED, REPORTED BY.

## Files staged
None. Read-only except this report; no git add.

## Result: FAIL

Verdict: FAIL

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
