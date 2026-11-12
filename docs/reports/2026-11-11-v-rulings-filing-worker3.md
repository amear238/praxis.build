# 2026-11-11 v-rulings-filing — worker 3 (ADVERSARIAL)

## Task
Attack D-2026-11-11-A (DECISIONS.md:2101–2168) and D-2026-11-11-B (:2170–2195), the de-identified return-handoff file and the de-identified install reply, against S1, S2, S4, S5, S8 and S13 and the unit brief's requirements. Attacks a–j.

## Mode
ADVERSARIAL. Read-only on everything except this report. No git index changes. Scripts live in /tmp/w3vrf/ (my own; no other worker's script reused). Removed identifiers were built at runtime from /tmp/vrf-deid/ originals; only counts and classes are printed below. The rep's name and the VM machine name are not typed anywhere here.

## Criterion
S1, S2, S4, S5, S8, S13 (specs/SPEC_RUBRIC.md, as quoted in the brief) plus the unit brief's content requirements for Entry A, Entry B and de-identification.

## Process log
1. Read DECISIONS.md:2095–2195, DECISION_LOG.md:828–829, both artifacts, and the /tmp originals (diffed with '<' lines masked).
2. a: wrote /tmp/w3vrf/quotes.py. It pulls every double-quoted span in DECISIONS.md:2100–2195, then searches 13 sources for each one (the /tmp originals included) and checks the three code-block quotations line by line.
3. f: printed every cited line.
4. g: wrote /tmp/w3vrf/deid2.py. It derives the removed identifiers by token difference between each original and the de-identified line, then counts them in each target. A placeholder-wildcard full match proves that each changed line differs only at its placeholders.
5. h: S13 position script. i: git diff and git status.
6. b/c/d/e/j: read the entries against DECISION_LOG.md:828–829, A6 (DECISIONS.md:1744–1745), proposal :3/:79, D-2026-11-10-C (:2076–2091) and the rubric D1/D2 text (:438–447).

## Verification evidence

### a. Quote byte-identity (python3 -I /tmp/w3vrf/quotes.py; full output)
```
D:2104 len=9 hits=['DLOG:825', 'DLOG:828', 'IR-orig:8', 'IR-deid:8', 'INVEST:289'] :: U do them
D:2106 len=30 hits=['DLOG:828', 'RH-orig:10', 'RH-deid:10'] :: Write it now and then send it.
D:2106 len=9 hits=['DLOG:828', 'RH-orig:82', 'RH-deid:82'] :: Go ahead.
D:2108 len=115 hits=['RH-orig:46', 'RH-deid:46'] :: flat by 16:00 ET governs; a position open at 15:00 may stay open until
D:2108 len=31 hits=['DLOG:828', 'RH-orig:47', 'RH-deid:47'] :: Uh, yeah, you have my approval.
D:2108 len=22 hits=['PROP:79'] :: Adoption of Rule F2-1.
D:2114 len=70 hits=['PROP:30'] :: On a full trading day, at 15:00 ET an open system position stays open.
D:2114 len=27 hits=['PROP:30'] :: Nothing closes it at 15:00.
D:2116 len=16 hits=['DLOG:828', 'RH-orig:46', 'RH-deid:46', 'DEC-HEAD:327', 'DEC-HEAD:329', 'DEC-HEAD:341'] :: flat by 16:00 ET
D:2116 len=87 hits=['PROP:20'] :: The closing order for every open system position is submitted no later
D:2116 len=67 hits=['PROP:20'] :: (or no later than the exchange's early close on an early-close day)
D:2116 len=71 hits=['PROP:20'] :: the position must be confirmed flat before MFFU's 4:10 PM ET auto-clos
D:2116 len=67 hits=['PROP:20'] :: The system opens no new position from that flat time until 18:00 ET
D:2116 len=122 hits=['PROP:30'] :: New system entries between 15:00 and 16:00 are allowed under Rule F2-1
D:2116 len=71 hits=['PROP:30'] :: Between 15:00 and 18:00 ET Amear's own manual interaction is locked ou
D:2118 len=57 hits=['RH-orig:47', 'RH-deid:47'] :: it only stops the system firing while the account is shut
D:2120 len=145 hits=['R6CAP:10'] :: Trades may be placed beginning at 6:00 PM EST when the Globex session 
D:2120 len=121 hits=['R6CAP:12'] :: At MyFundedFutures, any open positions will be automatically closed at
D:2120 len=149 hits=['R6CAP:20'] :: During holiday trading hours, auto-liquidation will not occur at the h
D:2120 len=3 hits=['DLOG:15', 'DLOG:17', 'DLOG:25', 'DLOG:29', 'DLOG:31', 'DLOG:34', 'DLOG:35', 'DLOG:47']... :: EST
D:2120 len=82 hits=['PROP:25'] :: this file reads it as US Eastern local time (ET), an INFERENCE, not st
D:2131 len=189 hits=['RH-orig:52', 'RH-deid:52'] :: Yes, however, if uh, I go with a, another prop firm that uh, potential
D:2131 len=22 hits=['RH-orig:52', 'RH-deid:52'] :: Having to fuck around.
D:2131 len=85 hits=['DLOG:828', 'RH-orig:78', 'RH-deid:78'] :: I don't care about evening entries. It's more about compli uh, the MFF
D:2131 len=112 hits=['DLOG:828'] :: MFFU compliance governs; nothing across the 16:10-18:00 ET close; even
D:2131 len=35 hits=['RH-orig:79', 'RH-deid:79'] :: put back to him and not objected to
D:2131 len=52 hits=['RH-orig:55', 'RH-deid:55', 'INVEST:476'] :: do not file V3 as closing OPEN-1 until Amear answers
D:2131 len=54 hits=['R6DES:110'] :: A written MFFU answer is needed before any funded use.
D:2135 len=173 hits=['RH-orig:106', 'RH-deid:106'] :: commit everything that we just discussed and the plan for tomorrow is 
D:2135 len=90 hits=['RH-orig:107', 'RH-deid:107'] :: I don't remember if I installed the tool to access the NinjaTrader thr
D:2135 len=57 hits=['RH-orig:107', 'RH-deid:107'] :: Asked that this check be on tomorrow's (2026-11-11) list.
D:2135 len=33 hits=['RH-orig:108', 'RH-deid:108'] :: So cli-nt-bridge is not installed
D:2138 len=58 hits=['RH-orig:120', 'RH-deid:120', 'INVEST:481'] :: 1. Kindly be informed that we do not offer Rithmic at MFFu
D:2138 len=198 hits=['RH-orig:121', 'RH-deid:121', 'INVEST:482'] :: 2. Kindly be informed that automated trading is allowed provided you a
D:2138 len=60 hits=['RH-orig:123', 'RH-deid:123', 'INVEST:483'] :: 4. You can trade using your strategy at the evaluation phase
D:2138 len=90 hits=['RH-orig:130', 'RH-deid:130', 'INVEST:484'] :: Funded-account permission for the pattern is not stated; item 4 names 
D:2139 len=52 hits=['RH-orig:133', 'RH-deid:133', 'INVEST:489'] :: OPEN-1 (evening entry vs overnight) is NOT answered.
D:2140 len=74 hits=['RH-orig:136', 'RH-deid:136', 'INVEST:486'] :: we see you've been inactive for some time, so this ticket is being clo
D:2149 len=25 hits=['INVEST:1422'] :: C3.3 — Replacement ticket
D:2149 len=59 hits=['INVEST:1424'] :: Amear sends this himself from his logged-in MFFU dashboard.
D:2153 len=140 hits=['RH-orig:53', 'RH-deid:53'] :: firm rules (flat time, overnight holding, other firm limits) live in a
D:2153 len=100 hits=['RH-orig:53', 'RH-deid:53'] :: Any overnight-holding profile needs its own backtest, because current 
D:2153 len=39 hits=['RH-orig:72', 'RH-deid:72'] :: O2 — R6 per-firm profile (V3): confirm.
D:2154 len=339 hits=['RH-orig:110', 'RH-deid:110'] :: the Noise-Area baseline (test 2a: 1,190 trades / $197,327.60 on NQCONT
D:2155 len=23 hits=['DLOG:828', 'DLOG:829', 'RH-orig:120', 'RH-deid:120', 'INVEST:15', 'INVEST:317', 'INVEST:465', 'INVEST:481']... :: we do not offer Rithmic
D:2155 len=20 hits=['INVEST:512', 'INVEST:631', 'TOPO:41'] :: → Rithmic → account.
D:2156 len=72 hits=['RH-orig:71', 'RH-deid:71'] :: SSH reverse tunnel from the Mac for sim testing (no new exposure of n8
D:2156 len=41 hits=['RUBRIC:446', 'DEC-HEAD:1915', 'DEC-HEAD:1974'] :: (d) installing keys, credentials or agent
D:2156 len=11 hits=['DLOG:25', 'DLOG:83', 'DLOG:744', 'DLOG:759', 'DLOG:770', 'DLOG:778', 'RUBRIC:447', 'DEC-HEAD:1887']... :: permissions
D:2160 len=40 hits=['RH-orig:136', 'RH-deid:136', 'INVEST:486'] :: the verification details are his to give
D:2175 len=120 hits=['HANDOFF:37'] :: **Do not install anything else** — not Python, not git, not a package 
D:2177 len=95 hits=['DLOG:828', 'IR-orig:7', 'IR-deid:7'] :: Okay, you know what? Let's forget about the snapshot. Let's have it ex
D:2177 len=96 hits=['IR-orig:7', 'IR-deid:7'] :: Hermes is going to give me a uh, a physical button to accept or deny, 
D:2177 len=9 hits=['DLOG:825', 'DLOG:828', 'IR-orig:8', 'IR-deid:8', 'INVEST:289'] :: U do them
D:2177 len=43 hits=['IR-orig:9', 'IR-deid:9'] :: No new snapshot was taken (Amear's choice).
D:2179 len=49 hits=['IR-orig:2', 'IR-deid:2'] :: Claude (Claude.ai Praxis channel, Cowork session)
D:2179 len=94 hits=['IR-orig:2', 'IR-deid:2'] :: driving the VM over SSH from the Mac (host praxis-vm), commands run fr
D:2181 len=64 hits=['IR-orig:28', 'IR-deid:28'] :: the VM is Windows on ARM64 and winget installed the ARM64 builds
D:2183 len=247 hits=['IR-orig:25', 'IR-deid:25'] :: NinjaTrader not started, stopped or touched (same pid and start time b
D:2185 len=32 hits=['IR-orig:1', 'IR-deid:1'] :: lifted by Amear for this install
D:2189 len=145 hits=['IR-orig:28', 'IR-deid:28'] :: Whether the bridge's dependencies (notably `pyarrow`, also `numpy`) ha
D:2189 len=134 hits=['IR-orig:28', 'IR-deid:28'] :: If step 3.5 fails on a build-from-source, the fallback is an x64 Python 
D:2189 len=15 hits=['HANDOFF:188'] :: 3.5 Python CLI.
```
No ODD-QUOTE-COUNT lines were printed. I compared every hit by hand with the line the entry cites, and every quoted span sits on the cited line or inside the cited range. Code blocks:
```
prop20 == D2111: True
rubric30-31 == D2125-2126: True
rubric49-50 == D2145-2146: True
prop30 startswith two sentences: False
'**On a full trading day, at 15:00 ET an open system position stays open.** Nothing closes it at 15:00. (On an early-close day ...
```
(The False is only the `**` bold markers around sentence 1. Both quoted sentences are substrings of :30, so they pass.) **a: no mismatch and no wrong line citation found.**

### f. Cited lines (raw)
```
DEC:2047: ## 2026-11-10 — D-2026-11-10-B: live-signal topology adopted as the working design (rubric F1; bead Praxis_build-1hv)
DEC:2076: ## 2026-11-10 — D-2026-11-10-C: VM agent = Hermes over SSH (settlement 3 changed; master under D1)
D:2085 ...The SSH key, the firewall rule and the tunnel were set up outside the build loop and are UNVERIFIED by Code; ...
D:2089 ...REPORTED BY Amear (DECISION_LOG.md:813): Hermes can drive the VM over SSH; ... the reverse tunnel to n8n; ...
H:37: 9. **Do not install anything else** — not Python, not git, not a package manager. If a tool is missing, STOP and report it. ...
H:188: **3.5 Python CLI.** The README (`README.md:43–45@9664d9b`):
H:36: 8. **`pip`.** ... Step 3.5 keeps a STOP before `pip` until Code names the pinned list, ...
16:203:- **Now:** run `python --version` in `C:\praxis\bridge-src` and paste it. Create no venv. Then **STOP before `pip`.** ...
vm/replies CODE- files: 20261110T211738Z-CODE-vm-agent-hermes.md   (no CODE-cli-setup reply exists)
RUB:30: **Unblocks when.** A DECISIONS.md entry names the governing rule and the
RUB:31: 15:00 disposition, and breaker specs #4 and #5 are amended to match.
RUB:49: **Criterion.** Written confirmation from MFFU that this specific automation
RUB:50: pattern is permitted on a funded account.
RUB:446:     money is at stake; (d) installing keys, credentials or agent
RUB:447:     permissions. Everything else is D1.
INV:1422: ### C3.3 — Replacement ticket
INV:1424: Amear sends this himself from his logged-in MFFU dashboard.
TOPO:41: Path: NT8 emitter ... → `SubmitBracket` → Rithmic → account.
R6:110: | OPEN-1 | MFFU terms (F4 channel, owner Amear) | ... A written MFFU answer is needed before any funded use. | OPEN |
PROP:79: | OPEN-F2-5 | Adoption of Rule F2-1. | Amear's approval under A6; then a DECISIONS.md entry and the amended #4/#5 text in the breaker spec. |
CAP:10/12/20: (match quoted text exactly, see a.)
$ git show HEAD:DECISION_LOG.md | wc -l  ->  826 ;  wc -l DECISION_LOG.md -> 829
```
**f: every line citation checks out**, including "826 lines … at HEAD d056e91" and "step 3.5 keeps its STOP before pip" (:36, :203; no CODE-cli-setup reply on disk).

### g. De-identification
Masked diff:
```
$ diff /tmp/vrf-deid/<return-handoff> docs/reports/<return-handoff> | sed -E 's/^< .*/< [MASKED ORIGINAL LINE]/'
65,66c65,66   (two masked '<' lines; '>' lines carry [VM LAN address], [MAC], [Mac LAN address], [Mac tailnet address])
68c68         (one masked '<' line; '>' carries [key file], [VM LAN address], [VM user])
136a137,138   (Filer's addendum + S13 line)
$ diff /tmp/vrf-deid/<install reply> vm/replies/<install reply> | (masked)
17c17         ('>' 1. `[VM machine name]\amear` / `v1.29.380` / `True` / NinjaTrader `9600 2026-11-10 5:46:59 PM`)
```
Placeholder-wildcard full match: each changed line is byte-identical apart from its placeholders.
```
...rulings.md 65 outside placeholders byte-identical: True; [('[VM LAN address]', 'IPv4', 13), ('[MAC]', 'MAC', 17)]
...rulings.md 66 outside placeholders byte-identical: True; [('[Mac LAN address]', 'IPv4', 13), ('[Mac tailnet address]', 'IPv4', 12)]
...rulings.md 68 outside placeholders byte-identical: True; [('[key file]', 'ssh-key-path', 16), ('[VM LAN address]', 'IPv4', 13), ('[VM user]', 'word==amear', 5)]
...install.md 17 outside placeholders byte-identical: True; [('[VM machine name]', 'hostname-like', 15)]
   orig ends with newline: True new ends with newline: True   (both files)
```
Surviving-identifier counts (python3 -I /tmp/w3vrf/deid2.py, trimmed to the relevant lines):
```
derived identifiers: 7 classes: ['IPv4', 'IPv4', 'IPv4', 'MAC', 'name', 'name', 'path']
DEC-new 2100-2195: [('MAC', 0), ('IPv4', 0), ('IPv4', 0), ('IPv4', 0), ('name', 6), ('name', 0), ('path', 0)]
DECISIONS.md whole: [('MAC', 0), ('IPv4', 0), ('IPv4', 0), ('IPv4', 2), ('name', 160), ('name', 0), ('path', 0)]
RH-deid: [('MAC', 0), ('IPv4', 0), ('IPv4', 0), ('IPv4', 0), ('name', 4), ('name', 0), ('path', 0)]
IR-deid: [('MAC', 0), ('IPv4', 0), ('IPv4', 0), ('IPv4', 0), ('name', 2), ('name', 0), ('path', 0)]
worker1: [... all IPv4/MAC/path/machine-name 0 ...]   worker2: [... all IPv4/MAC/path/machine-name 0 ...]
DECISION_LOG.md: [('MAC', 0), ('IPv4', 0), ('IPv4', 0), ('IPv4', 1), ('name', 258), ...]
DECISIONS lines with an orig IPv4 identifier: [1004, 1016]
DECISION_LOG lines with an orig IPv4 identifier: [517]
HEAD DECISIONS.md count of orig IPv4 identifiers: 2
```
(The 'name' with non-zero counts is the [VM user] value. The classifier shows it is the five-letter word equal to "amear", which is Amear's name and is kept. The other 'name' is the VM machine name: 0 everywhere.) IPv4-regex matches that remain in the artifacts:
```
RH-deid:  127.0.0.1 (x2, :66 and :108);  8.1.8.4 | ctx: — NT8 running (pid 9600, 8.1.8.4 file version)
IR-deid:  2.56.0.4 | ctx: nd Git [Git.Git] Version 2.56.0.4 …;  2.56.0.4 | ctx: .../v2.56.0.windows.4/Git-2.56.0.4-arm64.exe
DEC-new:  none.  MAC-regex count 0 in all.  ~/.ssh/ paths: RH-deid 1 ['~/.ssh/config'] (generic, not a key file); DEC-new 0
[rep]: RH-deid 5, orig 5; IR 0, orig 0; DEC-new 1
```
**g: no removed identifier survives in either artifact or in the new DECISIONS lines.** The version strings are versions. `[rep]` is unchanged. The n8n URL and Amear's name are kept, which the full match on :66 proves.

### h. S13
```
headings after 2090: [2101, 2170]
Entry A 2101-2169: standalone at [2168]; substring at [2168]; last non-blank line 2168; S13 is last: True
Entry B 2170-2195: standalone at [2195]; substring at [2195]; last non-blank line 2195; S13 is last: True
docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md standalone [138]; embedded [5]; last non-blank 138; ok=True
docs/reports/2026-11-11-v-rulings-filing-worker1.md standalone [318]; embedded []; last non-blank 318; ok=True
docs/reports/2026-11-11-v-rulings-filing-worker2.md standalone [179]; embedded [74, 130]; last non-blank 179; ok=True
vm/replies/20261111T172933Z-python-git-install.md standalone []; embedded []; last non-blank 28; ok=False
addendum line exact: True; S13 last line exact: True; trailing: ['']
```
(RH :5 is the original's "Standing limitation: …" line and is not standalone. worker2 :74/:130 are quotations inside that report.)

### i. Diff shape
```
$ git diff HEAD --stat -- DECISIONS.md
 DECISIONS.md | 96 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 96 insertions(+)
$ git diff HEAD -- DECISIONS.md | grep -c '^-[^-]'
0
$ git diff HEAD -- DECISIONS.md | grep '^@@'
@@ -2097,3 +2097,99 @@ The Mac's Hermes agent can now drive the Windows VM over SSH (host praxis-vm, ke
$ git diff --cached --stat
 docs/reports/evidence/[2026-10-28 MFFU reply image, filename withheld] | Bin 0 -> 254350 bytes   (already 'A' in the baseline)
```
The ` M` set in `git status --porcelain` is identical to the session-start baseline: .claude/settings.json, AUDIT_LOG.md, DECISIONS.md, DECISION_LOG.md, DISPATCH_LOG.md, HANDOFF.md, ISSUE_REGISTER.md, MANIFEST.md, STATUS.md, two 2026-10-28 reports, two specs, scripts/dispatch-log-writeahead.sh. **i: additions only, all after :2099.** Files that were already ` M` at baseline cannot be cleared of further edits by status alone. That limit is UNVERIFIED, not a finding.

### A6 / OPEN-F2-5 sources (for finding 1)
```
DECISIONS.md:1744-1745:  A6  FLAG 6: R8 starts the breaker PROPOSAL unit. F2's state changes
                             when Amear approves the proposed values.
PROP:3: ...Status: PROPOSED. F2 stays FROZEN until Amear approves (A6, DECISIONS.md:1744)...
PROP:79: | OPEN-F2-5 | Adoption of Rule F2-1. | Amear's approval under A6; then a DECISIONS.md entry and the amended #4/#5 text in the breaker spec. |
DECISIONS.md:2108 (Entry A): "... This answers the A6 hold, OPEN-F2-5 at `docs/specs/2026-11-10-f2-session-flat-proposal.md`:79 ..."
F2/F4 wording locations: 'answers the A6' [2108]; 'still needed' [2129]; 'NOT MET' [2142, 2166]; 'grades neither' [2164]
```

### D-2026-11-10-C sources (for findings 2 and 7)
```
DECISIONS.md:2082 (Amear's 20:42Z words): "... I propose Hermes runs the VM handoff ... in place of the Claude agent inside the VM. ... Separately, n8n reachability is settled: an SSH reverse tunnel lets the VM reach the Mac's n8n at http://127.0.0.1:5678 ..."
DECISIONS.md:2085: "The master reads his message as Amear's word on the D2(d) item ("installing keys, credentials or agent permissions" ...) for this grant only: Hermes acts as the VM agent over SSH, under the handoff's limits."
H:23: - **Amendment 3 (2026-11-10):** the VM agent is now Hermes, driving the VM over SSH from the Mac (host alias `praxis-vm` ...
H:27: Every limit holds for the whole of this file. If a step seems to need breaking one, STOP and write a reply saying which ...
IR :2: WRITTEN-BY: Claude (Claude.ai Praxis channel, Cowork session), driving the VM over SSH from the Mac (host praxis-vm), commands run from the Mac via osascript
IR :3: UTC: 20261111T172933Z     DLOG:828 row time 2026-11-11T18:19:40Z
```

## Findings

**1. MAJOR (S2; attack c; internal contradiction). Entry A :2108, "This answers the A6 hold, OPEN-F2-5", contradicts the entry's own F2 FROZEN position and goes beyond what it does.**
- A6 says "F2's state changes when Amear approves the proposed values", and proposal :3 says "F2 stays FROZEN until Amear approves (A6…)".
- If the A6 hold is answered, A6 as written changes F2's state. Yet the entry says "F2 stays FROZEN" (:2122), "does not grade the unblock clause" (:2129) and "does not unblock F2" (:2164). It never reconciles the two.
- OPEN-F2-5 (proposal :79) needs three things: Amear's approval, a DECISIONS entry, and the amended #4/#5 text. Only the first exists, and it covers the channel's summary, not the proposal text. The entry's own list (a)–(f) admits the summary leaves out the #4/#5 replacement text, and declines to grade whether his approval reaches it.
- So "answers" is a grade, and it implies the A6 trigger is met.
- Fix: replace with "Recorded against the A6 hold (OPEN-F2-5, proposal :79). Whether his approval of the summary meets A6's 'approves the proposed values' is not graded here. OPEN-F2-5's DECISIONS-entry and #4/#5 parts are not done." Also add one sentence on why A6's state change is not applied.

**2. MAJOR (S4, S5; D2(d) gap). Entry B records an install that was a deviation, done before any ledger append or DECISIONS entry. It does not say S4/S5 are not met, and it does not record that the agent who did it falls outside the existing D2(d) grant.**
- The install reply is stamped 17:29:33Z (IR :3). DLOG:828 is 18:19:40Z. Entry B is later still.
- S4 asks for an entry "written before the work". S5 says "the ledger append is the authorisation". The install rested only on voice/chat words relayed by the channel that did the work.
- "Timing (S4)" says "records the install after the fact", but never says "S4: not met / S5: not met for this install".
- The handoff's own procedure for a limit that seems to need breaking (H:27: "STOP and write a reply saying which") was not followed.
- D-2026-11-10-C's D2(d) reading is "for this grant only: Hermes acts as the VM agent over SSH" (:2085). The Claude.ai channel driving the VM over SSH (IR :2) is an agent permission no ledger row grants. Entry B states "grants no key, credential or permission" (:2193) but says nothing about one having been used.
- Fix: add factual lines, which carry no judgement:
  - "S4 and S5: not met for this install (work at or before 17:29:33Z; ledger 18:19:40Z)."
  - "D-2026-11-10-C's D2(d) reading covers Hermes only (DECISIONS.md:2085); no ledger row grants the Claude.ai channel SSH access to the VM."
  - Open for Amear: "whether the Claude.ai channel may drive the VM over SSH: D2(d)."

**3. MINOR (internal contradiction).** :2142 heads "F4 stays FROZEN / NOT MET" and :2166 repeats "NOT MET", which is a grade. :2164 says the entry "grades neither". Fix: "F4 stays FROZEN; graded NOT MET by the auditor at 55979ee (not re-graded here)".

**4. MINOR (S2, attack c).** :2129 "that amendment is still needed" implies the other half of the unblock clause (entry names the rule and the 15:00 disposition) is done, while the same sentence says it does not grade the clause. Fix: "The rubric's unblock clause also requires breaker specs #4 and #5 amended; that is a later unit. This entry does not grade any part of the clause."

**5. MINOR (attack d, D1 block against DECISION_LOG:829).** The count is right: exactly four decisions, none missing, none added, and no decision verb strengthened. Content drift:
- (1) Adds the second :53 sentence ("Any overnight-holding profile needs its own backtest…") inside the decision text, and the S6 line (:2166) then lists it as a Block 2 item. DLOG:829 cites only ":53, channel's proposal". It also adds "The profile's contents are not decided here", a narrowing that sits awkwardly beside the decided "MFFU as the first profile".
- (3) "NOT re-decided here (next unit)" becomes "that is a later unit", which softens the timing.
- (4) "uses SSH keys" becomes "would use"; "so it waits for Amear" is added. That is equivalent under D2, so acceptable.
- Fix: keep the second :53 sentence as context outside the numbered item, and restore "next unit" in (3).

**6. MINOR (attack b, scope beyond Amear's words).** Entry B :2185 "The lift covers this one install only." Amear's words (IR :7–8) set no scope. DLOG:828 says "Amear's lift of VM handoff §1 limit 9", also with no scope. The only source is the channel's header (IR :1), and the sentence carries no label. Fix: "(the install reply's header, :1; this entry reads it as one install only)".

**7. MINOR (attack e/j, understatement).** Decision 4 and Open-for-Amear item 1 treat the reverse tunnel as hypothetical ("would use"). Amear's own 20:42Z words, quoted at DECISIONS.md:2082, say "n8n reachability is settled: an SSH reverse tunnel lets the VM reach the Mac's n8n". Entry A calls them only "words about a reverse tunnel". The S8 risk runs in reverse: Amear could be re-asked something he has already stated. Fix: quote his "is settled" clause next to "REPORTED BY Amear … UNVERIFIED".

**8. MINOR (attack b, attribution).** Entry B's heading "Amear's words (install reply :7–9)" includes IR :9, "No new snapshot was taken (Amear's choice).", which is the channel's sentence. It is labelled "Install reply :9", but it sits under Amear's heading. Fix: move it out of the heading's scope, or retitle the heading "Amear's words (install reply :7–8) and the channel's note (:9)".

**9. MINOR (wording).** :2131 says "The combined ruling as Amear's 2026-11-11 brief states it". DLOG:828 says "states the combined reading". The brief itself is not on disk, so its wording is UNVERIFIED beyond DLOG:828. Its text closely mirrors the channel's INFERRED reading at RH :79, with a hyphen where RH has an en dash. Fix: use DLOG's word "reading", or add "(as relayed in DLOG:828; the brief itself is not on disk)".

**10. MINOR (de-identification consistency).** In RH :68 the VM user is masked as `[VM user]`. The same value is printed in clear in IR :17 (whoami output, after `[VM machine name]\`). The value is Amear's own login word, which is kept, so nothing leaks. But the mask can be reversed by reading the other file, and the two files treat the item differently. The SSH Host alias `praxis-vm` is kept in RH :68, IR :2/:12–14 and Entry B :2179. This matches HEAD (DECISIONS.md:2081 and handoff :23 already carry it). No action unless Amear wants the alias treated as a mapping detail.

**11. MINOR (S13 scope).** The install reply has no S13 line (standalone []), because the brief requires it to stay byte-identical. If a VM reply counts as a "report" under S13, it fails there. Fix: the master to state whether vm/replies files are in S13's scope, or add a filer's addendum as was done for the return-handoff file.

**12. MINOR (quotation rendering).** :2156 renders D2(d) as "(d) installing keys, credentials or agent" … "permissions". The ellipsis implies omitted words where there is only a line break (RUB:446–447). Fix: "(d) installing keys, credentials or agent permissions" (rubric :446–447, line break joined).

**13. Out of scope, reported only (not this unit's lines).** One of the four removed IPv4 identifiers is already in the tree at HEAD: DECISIONS.md:1004 and :1016, and DECISION_LOG.md:517 (count 2 in HEAD DECISIONS.md, 1 in DECISION_LOG.md). Also, proposal :8 cites the rubric unblock clause at ":43–44"; it is at :30–31 now. Both need their own unit.

**Checked with no break (attacks):**
- a: every quote is byte-identical and on its cited line.
- f: all line citations are correct.
- g: no surviving identifiers; files are byte-identical outside placeholders; `[rep]` 5=5.
- h: S13 is correct in Entry A, Entry B, the return-handoff file, worker1 and worker2.
- i: additions only, after :2099.
- Times and ids all match RH: 19:29:01Z, 22:49:22Z, 19:43:42Z, 23:08:17Z, 2026-11-11T15:20:34Z; message ids 1a1c6ef68efc93d2, 1a1c7a6d7d0d0dec, 1a1c6fce04330f0d, 1a1c7b82f130416b, 1a1cb3255cf62d16; thread 19f9edc188595b0c.
- Entry B content requirements (limit 9 quote, :24–25 kept-list, open risk, REPORTED BY grade) are present.
- Open-for-Amear is D2 plus his own hands only.
- No broker route, profile contents, tunnel, D2 item or x64 fallback is decided on Amear's behalf.

## Files staged
None. This report is the only file written. It is not staged.

## Result
FAIL. Two MAJOR (findings 1, 2), ten MINOR (findings 3–12), one out-of-scope report (finding 13).

Verdict: FAIL

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
