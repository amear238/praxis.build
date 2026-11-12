# Worker 1 report — unit `2026-11-11-v-rulings-filing`

## Task
Append two entries at the end of DECISIONS.md: D-2026-11-11-A (Amear's rulings V1–V7 and MFFU's replies, WHO: amear, REPORTED BY the Claude.ai channel, plus the master's four D1 decisions from DECISION_LOG.md:829) and D-2026-11-11-B (VM handoff §1 limit 9 lifted for one install; Python 3.12.10 and git 2.56.0 ARM64 installed; record only). Append only. Every quotation copied by script.

## Mode
BUILD.

## Criterion
The brief's S1 (quotes byte-identical to the cited source line, copied by script), S4 (timing stated), S5 (ledger append is the authorisation record), S6 (cross-block), S13 (the S13 sentence once per entry as its standalone last line). Append-only: no existing byte of DECISIONS.md changed. No network identifiers, no rep first name, no D2 item decided, F2 and F4 not shown as unblocked.

## Process log
1. Checked the starting state: HEAD `d056e91`; DECISIONS.md 2099 lines, ending in `\n` after the S13 sentence of D-2026-11-10-C; `git diff HEAD --stat -- DECISIONS.md` empty.
2. Read all sources in full: the return-handoff file (136 lines), the install reply (lines 1–16 and 18–28; line 17 was printed to me only in masked form, see Deviation 1), DECISION_LOG.md:828–829, DECISIONS.md:2040–2099 (format precedent), `vm/2026-11-06-vm-handoff.md`:37, `specs/SPEC_RUBRIC.md`:19–58 and :440–450, the F2 proposal (all 81 lines), topology doc (grep), `bf6fcc7` trading-day capture :1–25, `bf6fcc7` R6 design (grep OPEN-1), investigation C3.3 (:1422–1432).
3. Checked line numbers rather than taking them from the brief. Rubric F2 unblock = `specs/SPEC_RUBRIC.md`:30–31 and F4 criterion = :49–50 (grep output below). The F2 proposal's :8 cites the unblock clause at `:43–44`, which is stale against the current rubric. Not mine to fix; reported here only. D2(d) is split across :446–447. Handoff step 3.5 heading is at :188. DECISION_LOG.md has 826 lines at HEAD, so :828 and :829 exist only in the working copy.
4. Wrote one Python generator, fed on stdin (`python3 -I - <mode>`, no script file written to disk). It has a quote table: key → (source, line, start anchor, end anchor, or a regex). Each anchor must occur exactly once in its line (asserted). The quoted text is sliced out of the source line itself. Text blocks are whole source lines. Placeholders `«key»` in the entry template are replaced from the table, and the run asserts nothing is left unresolved. First a `dry` run to stdout, read and corrected (double period after the :79 quote, a run-on sentence in V7, quote marks around labels that are not quotations, the nested-quote :43 quote dropped and replaced by a citation). Then one `append` run.
5. Verified: diff shape, line ranges, S13 counts, the identifier scans, and an independent quote check. That check pulls every `"…"` span and every text-block line out of the new lines and searches all sources for it. It does not reuse the generator's table.

### Deviations
1. **VM machine-name pattern.** The brief says to build it at runtime from install reply :17. When I read it, :17 no longer held a `NAME\user` token: the other worker had already put a bracketed placeholder there. Masked shape of :17: ``9. `[aa aaaaaaa aaaa]\aaaaa` / `a9.99.999` / `aaaa` / aaaaaaaaaaa `9999 9999-99-99 9:99:99 aa` ``. So the pattern was built at runtime from every `NAME\amear` token in `vm/replies/*.md` (3 distinct, found in `20261110T214834Z-self-report.md` and `20261110T224920Z-2b-skill-job.md`), plus any from :17 (0). The name was never printed or typed.
2. **D2(d) wording** spans two rubric lines. It is quoted as two fragments, `"(d) installing keys, credentials or agent"` … `"permissions"`, cited :446–447, so that each fragment is byte-identical to its own line. The F2 unblock clause and the F4 criterion are quoted as `text` blocks of whole source lines (:30–31, :49–50).
3. "U do them" also appears at DECISION_LOG.md:828 in the limit-9 (ALSO) part of that row, and install reply :8 says it answered "the two open items". Entry A quotes it as Amear's go from :828, as the brief directs. Entry B quotes it from install reply :8 with its context, which is also copied by script.

## Verification evidence

### Extraction: line-number checks
```
$ grep -n 'Unblocks when\|15:00 disposition, and\|Written confirmation from MFFU\|pattern is permitted on a funded' specs/SPEC_RUBRIC.md
30:**Unblocks when.** A DECISIONS.md entry names the governing rule and the
31:15:00 disposition, and breaker specs #4 and #5 are amended to match.
44:**Unblocks when.** The assumption is committed and the backtest report carries
49:**Criterion.** Written confirmation from MFFU that this specific automation
50:pattern is permitted on a funded account.
78:Filer's note, not a ruling: F1 is moved here out of FROZEN. [... line truncated in this report ...]
90:**Unblocks when.** `docs/specs/*-live-signal-topology.md` exists, is committed,
$ grep -n 'installing keys' specs/SPEC_RUBRIC.md
446:    money is at stake; (d) installing keys, credentials or agent
$ sed -n '37p' vm/2026-11-06-vm-handoff.md
9. **Do not install anything else** — not Python, not git, not a package manager. If a tool is missing, STOP and report it. Do not change PowerShell's execution policy; if `Activate.ps1` is blocked, use the README's fallback, `.venv\Scripts\python -m nt8bridge …` (`README.md:48@9664d9b`).
$ git show HEAD:DECISION_LOG.md | wc -l
     826
$ grep -n 'C3.3\|C3\.' docs/reports/2026-11-11-mffu-connection-investigation.md | head
[...] 1422:### C3.3 — Replacement ticket
$ sed -n '1422,1424p' docs/reports/2026-11-11-mffu-connection-investigation.md
### C3.3 — Replacement ticket

Amear sends this himself from his logged-in MFFU dashboard.
```

### Extraction: generator (the extraction part, verbatim)
Command: `cd /Volumes/Sensidine/Praxis.build && python3 -I - append <<'PYEOF' … PYEOF`. The part of that command that reads the sources and extracts the quotes:
```python
REPO='/Volumes/Sensidine/Praxis.build'
SRC={'RH':'docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md','IR':'vm/replies/20261111T172933Z-python-git-install.md','DL':'DECISION_LOG.md','RUB':'specs/SPEC_RUBRIC.md','PROP':'docs/specs/2026-11-10-f2-session-flat-proposal.md','HO':'vm/2026-11-06-vm-handoff.md','INV':'docs/reports/2026-11-11-mffu-connection-investigation.md','TOP':'docs/specs/2026-11-10-live-signal-topology.md','CAP':'bf6fcc7:docs/reports/evidence/2026-11-09-r6-mffu-trading-day.txt','R6':'bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md'}
def lines(k):
    p=SRC[k]
    if p.startswith('bf6fcc7:'): b=subprocess.run(['git','-C',REPO,'show',p],capture_output=True,check=True).stdout
    else: b=open(REPO+'/'+p,'rb').read()
    return b.decode('utf-8').split('\n')
L={k:lines(k) for k in SRC}
# Q = { key: (source, line, start_anchor_or_'re:'regex, end_anchor_or_None) }  -- 84 rows; each row's
#     source:line and extracted text is printed in the output table below
B={'PROP20':('PROP',20,20),'RUB30':('RUB',30,31),'RUB49':('RUB',49,50)}
def ext(k):
    s,n,a,e=Q[k]; line=L[s][n-1]
    if a.startswith('re:'):
        m=re.findall(a[3:],line); assert len(m)==1,(k,m); return m[0]
    assert line.count(a)==1,(k,line.count(a)); i=line.index(a)
    if e is None: return a
    j=line.index(e,i)+len(e); return line[i:j]
X={k:ext(k) for k in Q}
for k in B:
    s,a,b=B[k]; X['BLOCK:'+k]='\n'.join(L[s][a-1:b])
# T = entry template with «key» placeholders (its rendered text is DECISIONS.md:2100–2195)
out=re.sub('«([^»]+)»',lambda m: X[m.group(1)],T); assert '«' not in out and '»' not in out
# append: open(REPO+'/DECISIONS.md','a').write('\n'+out[1:])
```

### Extraction: raw output of the append run
```
appended 95 lines
DL828_udothem	DECISION_LOG.md:828	U do them
DL828_combined	DECISION_LOG.md:828	MFFU compliance governs; nothing across the 16:10-18:00 ET close; evening entries stand on MFFU's written answer
RH10	docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:10	Write it now and then send it.
RH11_time	docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:11	2026-11-10T19:29:01Z
RH11_msg	docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:11	1a1c6ef68efc93d2
RH11_thread	docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:11	19f9edc188595b0c
RH46	docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:46	flat by 16:00 ET governs; a position open at 15:00 may stay open until 16:00; no new system entries 16:00–18:00 ET.
RH46_flat	docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:46	flat by 16:00 ET
RH47_words	docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:47	Uh, yeah, you have my approval.
RH47_lockout	docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:47	it only stops the system firing while the account is shut
RH52a	docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:52	Yes, however, if uh, I go with a, another prop firm that uh, potentially allows for overnight uh, holds, would we be able to duplicate the dur uh, the uh, the infrastructure or change that?
RH52b	docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:52	Having to fuck around.
RH53_profile	docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:53	firm rules (flat time, overnight holding, other firm limits) live in a per-firm settings profile, MFFU as the first profile, not hard-coded.
RH53_backtest	docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:53	Any overnight-holding profile needs its own backtest, because current results assume flat every day.
RH55_hold	docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:55	do not file V3 as closing OPEN-1 until Amear answers
RH71_tunnel	docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:71	SSH reverse tunnel from the Mac for sim testing (no new exposure of n8n)
RH72	docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:72	O2 — R6 per-firm profile (V3): confirm.
RH78	docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:78	I don't care about evening entries. It's more about compli uh, the MFFU's compliance.
RH79_put	docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:79	put back to him and not objected to
RH82	docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:82	Go ahead.
RH83_time	docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:83	2026-11-10T22:49:22Z
RH83_thread	docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:83	19f9edc188595b0c
RH83_msg	docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:83	1a1c7a6d7d0d0dec
RH106	docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:106	commit everything that we just discussed and the plan for tomorrow is to get put together a plan to run within the VM to backtest all these strategies inside of NinjaTrader.
RH107	docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:107	I don't remember if I installed the tool to access the NinjaTrader through a bash command.
RH107_list	docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:107	Asked that this check be on tomorrow's (2026-11-11) list.
RH108_bridge	docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:108	So cli-nt-bridge is not installed
RH110_list	docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:110	the Noise-Area baseline (test 2a: 1,190 trades / $197,327.60 on NQCONTROW SEP25) and its walk-forward; the three 2026-11-01 strategies; the R6 announcement variants (no NinjaScript exists for them; the R6 design proposed a Mac-side Python first pass, which this work order changes to NT8 — the master's call under D1, changeable by Amear).
RH114_msg	docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:114	1a1c6fce04330f0d
RH120	docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:120	1. Kindly be informed that we do not offer Rithmic at MFFu
RH120_rithmic	docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:120	we do not offer Rithmic
RH121	docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:121	2. Kindly be informed that automated trading is allowed provided you abide by our rules and policies : https://help.myfundedfutures.com/en/articles/8444599-fair-play-and-prohibited-trading-practices
RH123	docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:123	4. You can trade using your strategy at the evaluation phase
RH130_funded	docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:130	Funded-account permission for the pattern is not stated; item 4 names the evaluation only.
RH132_msg	docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:132	1a1c7b82f130416b
RH133_not	docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:133	OPEN-1 (evening entry vs overnight) is NOT answered.
RH135_msg	docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:135	1a1cb3255cf62d16
RH136	docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:136	we see you've been inactive for some time, so this ticket is being closed.
RH136_give	docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:136	the verification details are his to give
PROP20_submitted	docs/specs/2026-11-10-f2-session-flat-proposal.md:20	The closing order for every open system position is submitted no later than 16:00:00 ET
PROP20_early	docs/specs/2026-11-10-f2-session-flat-proposal.md:20	(or no later than the exchange's early close on an early-close day)
PROP20_confirm	docs/specs/2026-11-10-f2-session-flat-proposal.md:20	the position must be confirmed flat before MFFU's 4:10 PM ET auto-close
PROP20_from	docs/specs/2026-11-10-f2-session-flat-proposal.md:20	The system opens no new position from that flat time until 18:00 ET
PROP25_inf	docs/specs/2026-11-10-f2-session-flat-proposal.md:25	this file reads it as US Eastern local time (ET), an INFERENCE, not stated by MFFU
PROP30_first	docs/specs/2026-11-10-f2-session-flat-proposal.md:30	On a full trading day, at 15:00 ET an open system position stays open.
PROP30_nothing	docs/specs/2026-11-10-f2-session-flat-proposal.md:30	Nothing closes it at 15:00.
PROP30_entries	docs/specs/2026-11-10-f2-session-flat-proposal.md:30	New system entries between 15:00 and 16:00 are allowed under Rule F2-1, subject to breakers #1, #2, #3, #6, #7, #8 and #9.
PROP30_lockout	docs/specs/2026-11-10-f2-session-flat-proposal.md:30	Between 15:00 and 18:00 ET Amear's own manual interaction is locked out
PROP79	docs/specs/2026-11-10-f2-session-flat-proposal.md:79	Adoption of Rule F2-1.
CAP10	bf6fcc7:docs/reports/evidence/2026-11-09-r6-mffu-trading-day.txt:10	Trades may be placed beginning at 6:00 PM EST when the Globex session opens and can remain open until the New York session closes at 4:10 PM EST.
CAP12	bf6fcc7:docs/reports/evidence/2026-11-09-r6-mffu-trading-day.txt:12	At MyFundedFutures, any open positions will be automatically closed at 4:10 PM EST on regular (non-holiday) trading days.
CAP20	bf6fcc7:docs/reports/evidence/2026-11-09-r6-mffu-trading-day.txt:20	During holiday trading hours, auto-liquidation will not occur at the half-time market close, and the trader is responsible for closing the positions.
R6_110	bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md:110	A written MFFU answer is needed before any funded use.
RUB446	specs/SPEC_RUBRIC.md:446	(d) installing keys, credentials or agent
RUB447	specs/SPEC_RUBRIC.md:447	permissions
TOP41_tail	docs/specs/2026-11-10-live-signal-topology.md:41	→ Rithmic → account.
INV1422	docs/reports/2026-11-11-mffu-connection-investigation.md:1422	C3.3 — Replacement ticket
INV1424	docs/reports/2026-11-11-mffu-connection-investigation.md:1424	Amear sends this himself from his logged-in MFFU dashboard.
HO37	vm/2026-11-06-vm-handoff.md:37	**Do not install anything else** — not Python, not git, not a package manager. If a tool is missing, STOP and report it.
HO188	vm/2026-11-06-vm-handoff.md:188	3.5 Python CLI.
IR1	vm/replies/20261111T172933Z-python-git-install.md:1	lifted by Amear for this install
IR2_who	vm/replies/20261111T172933Z-python-git-install.md:2	Claude (Claude.ai Praxis channel, Cowork session)
IR2_how	vm/replies/20261111T172933Z-python-git-install.md:2	driving the VM over SSH from the Mac (host praxis-vm), commands run from the Mac via osascript
IR3	vm/replies/20261111T172933Z-python-git-install.md:3	20261111T172933Z
IR7a	vm/replies/20261111T172933Z-python-git-install.md:7	Okay, you know what? Let's forget about the snapshot. Let's have it execute those things first.
IR7b	vm/replies/20261111T172933Z-python-git-install.md:7	Hermes is going to give me a uh, a physical button to accept or deny, so don't worry about that.
IR8	vm/replies/20261111T172933Z-python-git-install.md:8	U do them
IR8_items	vm/replies/20261111T172933Z-python-git-install.md:8	on the two open items (file the 2026-11-10 note; install Python and git in the VM)
IR9	vm/replies/20261111T172933Z-python-git-install.md:9	No new snapshot was taken (Amear's choice).
IR18_pyexit	vm/replies/20261111T172933Z-python-git-install.md:18	PYTHON_EXIT=0
IR18_gitexit	vm/replies/20261111T172933Z-python-git-install.md:18	GIT_EXIT=0
IR19_python	vm/replies/20261111T172933Z-python-git-install.md:19	`Python 3.12.10` at `C:\Program Files\Python312-arm64\python.exe`
IR19_py0p	vm/replies/20261111T172933Z-python-git-install.md:19	`py -0p`: `-V:3.12-arm64 *`
IR19_git	vm/replies/20261111T172933Z-python-git-install.md:19	`git version 2.56.0.windows.4` at `C:\Program Files\Git\cmd\git.exe`
IR19_nt	vm/replies/20261111T172933Z-python-git-install.md:19	NinjaTrader still pid 9600, start time unchanged
IR19_arch	vm/replies/20261111T172933Z-python-git-install.md:19	`PROCESSOR_ARCHITECTURE=ARM64`
IR25	vm/replies/20261111T172933Z-python-git-install.md:25	NinjaTrader not started, stopped or touched (same pid and start time before and after). No connection change (D-071). No orders. No pip run, no clone, no bridge files. No Windows restart. Nothing else installed. Only new files under `vm/replies/`.
IR28_arm	vm/replies/20261111T172933Z-python-git-install.md:28	the VM is Windows on ARM64 and winget installed the ARM64 builds
IR28a	vm/replies/20261111T172933Z-python-git-install.md:28	Whether the bridge's dependencies (notably `pyarrow`, also `numpy`) have win_arm64 wheels at versions meeting the bridge's floors is not checked.
IR28b	vm/replies/20261111T172933Z-python-git-install.md:28	If step 3.5 fails on a build-from-source, the fallback is an x64 Python (runs under emulation) — that is Amear's call, not taken here.
BLOCK:PROP20	docs/specs/2026-11-10-f2-session-flat-proposal.md:20-20
**Rule F2-1. Deviation B's 16:00 ET session flat governs. The closing order for every open system position is submitted no later than 16:00:00 ET (or no later than the exchange's early close on an early-close day), and the position must be confirmed flat before MFFU's 4:10 PM ET auto-close. The system opens no new position from that flat time until 18:00 ET, when the next session begins.**
BLOCK:RUB30	specs/SPEC_RUBRIC.md:30-31
**Unblocks when.** A DECISIONS.md entry names the governing rule and the
15:00 disposition, and breaker specs #4 and #5 are amended to match.
BLOCK:RUB49	specs/SPEC_RUBRIC.md:49-50
**Criterion.** Written confirmation from MFFU that this specific automation
pattern is permitted on a funded account.
```

### Line ranges, diff shape, S13 counts
The S13 check script set `S` to the full S13 sentence. It is shown here as `S='<the S13 sentence>'` so that this report carries the sentence only once.
```
$ wc -l DECISIONS.md; grep -n '^## 2026-11-11' DECISIONS.md | cut -c1-60; git diff HEAD --stat -- DECISIONS.md
    2195 DECISIONS.md
2101:## 2026-11-11 — D-2026-11-11-A: Amear's rulings V1–V7 (Cl
2170:## 2026-11-11 — D-2026-11-11-B: VM handoff §1 limit 9 lift
 DECISIONS.md | 96 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 96 insertions(+)
$ echo "minus-lines: $(git diff HEAD -- DECISIONS.md | grep -c '^-[^-]')"
minus-lines: 0
$ git diff HEAD -U0 -- DECISIONS.md | grep '^@@' | cut -c1-30
@@ -2099,0 +2100,96 @@
--- S13 per entry:
entry lines 2101-2168: substring count=1, standalone count=1, last line standalone=True
entry lines 2170-2195: substring count=1, standalone count=1, last line standalone=True
first new line 2100 '' line 2099 = 'Fills are optimistic; Standard resolution on 1-minute bars; '
```
(The `grep` heading lines and the `@@` line are cut with `cut` in this paste only, to keep this report free of a second copy of the S13 sentence. The raw `@@` context text was the start of line 2099.) First added line = 2100 (blank separator line), which is > 2099. D-2026-11-11-A = DECISIONS.md:2101–2168; blank line :2169; D-2026-11-11-B = DECISIONS.md:2170–2195.

### Identifier scans over new lines (2100–2195)
```
IPv4 (excl 127.0.0.1): 0
MAC: 0
.ssh/: 0
install reply :17 machine-name tokens of form NAME\user: 0 (other worker has placed a bracketed placeholder there: 1 "[" chars)
machine-name candidates built at runtime: 3 ; hits in new lines (case-insensitive): 0
rep first name check: "[rep]" occurrences in new lines: 1
```

### Quote proof (independent of the generator: scans the new lines, searches all sources)
```
BLOCK DECISIONS.md:2111 exact-line-match -> ['proposal:20']
BLOCK DECISIONS.md:2125 exact-line-match -> ['SPEC_RUBRIC.md:30']
BLOCK DECISIONS.md:2126 exact-line-match -> ['SPEC_RUBRIC.md:31']
BLOCK DECISIONS.md:2145 exact-line-match -> ['SPEC_RUBRIC.md:49']
BLOCK DECISIONS.md:2146 exact-line-match -> ['SPEC_RUBRIC.md:50']
OK  ['install-reply:8', 'DECISION_LOG.md:825', 'DECISION_LOG.md:828'] +1 more  "U do them"
OK  ['return-handoff:10', 'DECISION_LOG.md:828']  "Write it now and then send it."
OK  ['return-handoff:82', 'DECISION_LOG.md:828']  "Go ahead."
OK  ['return-handoff:46']  "flat by 16:00 ET governs; a position open at 15:00 may stay open until…"
OK  ['return-handoff:47', 'DECISION_LOG.md:828']  "Uh, yeah, you have my approval."
OK  ['proposal:79']  "Adoption of Rule F2-1."
OK  ['proposal:30']  "On a full trading day, at 15:00 ET an open system position stays open."
OK  ['proposal:30']  "Nothing closes it at 15:00."
OK  ['return-handoff:46', 'DECISION_LOG.md:828']  "flat by 16:00 ET"
OK  ['proposal:20']  "The closing order for every open system position is submitted no later…"
OK  ['proposal:20']  "(or no later than the exchange's early close on an early-close day)"
OK  ['proposal:20']  "the position must be confirmed flat before MFFU's 4:10 PM ET auto-clos…"
OK  ['proposal:20']  "The system opens no new position from that flat time until 18:00 ET"
OK  ['proposal:30']  "New system entries between 15:00 and 16:00 are allowed under Rule F2-1…"
OK  ['proposal:30']  "Between 15:00 and 18:00 ET Amear's own manual interaction is locked ou…"
OK  ['return-handoff:47']  "it only stops the system firing while the account is shut"
OK  ['bf6fcc7:trading-day.txt:10']  "Trades may be placed beginning at 6:00 PM EST when the Globex session …"
OK  ['bf6fcc7:trading-day.txt:12']  "At MyFundedFutures, any open positions will be automatically closed at…"
OK  ['bf6fcc7:trading-day.txt:20']  "During holiday trading hours, auto-liquidation will not occur at the h…"
OK  ['DECISION_LOG.md:15', 'DECISION_LOG.md:17', 'DECISION_LOG.md:25'] +334 more  "EST"
OK  ['proposal:25']  "this file reads it as US Eastern local time (ET), an INFERENCE, not st…"
OK  ['return-handoff:52']  "Yes, however, if uh, I go with a, another prop firm that uh, potential…"
OK  ['return-handoff:52']  "Having to fuck around."
OK  ['return-handoff:78', 'DECISION_LOG.md:828']  "I don't care about evening entries. It's more about compli uh, the MFF…"
OK  ['DECISION_LOG.md:828']  "MFFU compliance governs; nothing across the 16:10-18:00 ET close; even…"
OK  ['return-handoff:79']  "put back to him and not objected to"
OK  ['return-handoff:55', 'investigation:476']  "do not file V3 as closing OPEN-1 until Amear answers"
OK  ['bf6fcc7:r6-design:110']  "A written MFFU answer is needed before any funded use."
OK  ['return-handoff:106']  "commit everything that we just discussed and the plan for tomorrow is …"
OK  ['return-handoff:107']  "I don't remember if I installed the tool to access the NinjaTrader thr…"
OK  ['return-handoff:107']  "Asked that this check be on tomorrow's (2026-11-11) list."
OK  ['return-handoff:108']  "So cli-nt-bridge is not installed"
OK  ['return-handoff:120', 'investigation:481']  "1. Kindly be informed that we do not offer Rithmic at MFFu"
OK  ['return-handoff:121', 'investigation:482']  "2. Kindly be informed that automated trading is allowed provided you a…"
OK  ['return-handoff:123', 'investigation:483']  "4. You can trade using your strategy at the evaluation phase"
OK  ['return-handoff:130', 'investigation:484']  "Funded-account permission for the pattern is not stated; item 4 names …"
OK  ['return-handoff:133', 'investigation:489']  "OPEN-1 (evening entry vs overnight) is NOT answered."
OK  ['return-handoff:136', 'investigation:486']  "we see you've been inactive for some time, so this ticket is being clo…"
OK  ['investigation:1422']  "C3.3 — Replacement ticket"
OK  ['investigation:1424']  "Amear sends this himself from his logged-in MFFU dashboard."
OK  ['return-handoff:53']  "firm rules (flat time, overnight holding, other firm limits) live in a…"
OK  ['return-handoff:53']  "Any overnight-holding profile needs its own backtest, because current …"
OK  ['return-handoff:72']  "O2 — R6 per-firm profile (V3): confirm."
OK  ['return-handoff:110']  "the Noise-Area baseline (test 2a: 1,190 trades / $197,327.60 on NQCONT…"
OK  ['return-handoff:120', 'DECISION_LOG.md:828', 'DECISION_LOG.md:829'] +7 more  "we do not offer Rithmic"
OK  ['investigation:512', 'investigation:631', 'topology:41']  "→ Rithmic → account."
OK  ['return-handoff:71']  "SSH reverse tunnel from the Mac for sim testing (no new exposure of n8…"
OK  ['SPEC_RUBRIC.md:446']  "(d) installing keys, credentials or agent"
OK  ['DECISION_LOG.md:25', 'DECISION_LOG.md:83', 'DECISION_LOG.md:744'] +4 more  "permissions"
OK  ['return-handoff:136', 'investigation:486']  "the verification details are his to give"
OK  ['vm-handoff:37']  "**Do not install anything else** — not Python, not git, not a package …"
OK  ['install-reply:7', 'DECISION_LOG.md:828']  "Okay, you know what? Let's forget about the snapshot. Let's have it ex…"
OK  ['install-reply:7']  "Hermes is going to give me a uh, a physical button to accept or deny, …"
OK  ['install-reply:8', 'DECISION_LOG.md:825', 'DECISION_LOG.md:828'] +1 more  "U do them"
OK  ['install-reply:9']  "No new snapshot was taken (Amear's choice)."
OK  ['install-reply:2']  "Claude (Claude.ai Praxis channel, Cowork session)"
OK  ['install-reply:2']  "driving the VM over SSH from the Mac (host praxis-vm), commands run fr…"
OK  ['install-reply:28']  "the VM is Windows on ARM64 and winget installed the ARM64 builds"
OK  ['install-reply:25']  "NinjaTrader not started, stopped or touched (same pid and start time b…"
OK  ['install-reply:1']  "lifted by Amear for this install"
OK  ['install-reply:28']  "Whether the bridge's dependencies (notably `pyarrow`, also `numpy`) ha…"
OK  ['install-reply:28']  "If step 3.5 fails on a build-from-source, the fallback is an x64 Pytho…"
OK  ['vm-handoff:188']  "3.5 Python CLI."

quoted spans: 63; found in a source line: 63; not found: 0
```
The proof truncates matching-line lists at three. For "permissions" (+4 more), the generator's assert `line.count(a)==1` on `specs/SPEC_RUBRIC.md`:447 had already confirmed it is on that line. "EST" is the entry quoting MFFU's word, which is on capture :10 and :12.

Values copied by script but not in double quotes (ids, times, paths, exit codes), each checked against its cited line and against the new text:
```
OK  in-source(RH:11)=True in-new=True  2026-11-10T19:29:01Z
OK  in-source(RH:11)=True in-new=True  1a1c6ef68efc93d2
OK  in-source(RH:11)=True in-new=True  19f9edc188595b0c
OK  in-source(RH:83)=True in-new=True  2026-11-10T22:49:22Z
OK  in-source(RH:83)=True in-new=True  19f9edc188595b0c
OK  in-source(RH:83)=True in-new=True  1a1c7a6d7d0d0dec
OK  in-source(RH:114)=True in-new=True  1a1c6fce04330f0d
OK  in-source(RH:132)=True in-new=True  1a1c7b82f130416b
OK  in-source(RH:135)=True in-new=True  1a1cb3255cf62d16
OK  in-source(RH:114)=True in-new=True  2026-11-10T19:43:42Z
OK  in-source(RH:132)=True in-new=True  2026-11-10T23:08:17Z
OK  in-source(RH:135)=True in-new=True  2026-11-11T15:20:34Z
OK  in-source(IR:3)=True in-new=True  20261111T172933Z
OK  in-source(IR:18)=True in-new=True  PYTHON_EXIT=0
OK  in-source(IR:18)=True in-new=True  GIT_EXIT=0
OK  in-source(IR:19)=True in-new=True  `Python 3.12.10` at `C:\Program Files\Python312-arm64\python.exe`
OK  in-source(IR:19)=True in-new=True  `py -0p`: `-V:3.12-arm64 *`
OK  in-source(IR:19)=True in-new=True  `git version 2.56.0.windows.4` at `C:\Program Files\Git\cmd\git.exe`
OK  in-source(IR:19)=True in-new=True  NinjaTrader still pid 9600, start time unchanged
OK  in-source(IR:19)=True in-new=True  `PROCESSOR_ARCHITECTURE=ARM64`
OK  in-source(IR:8)=True in-new=True  on the two open items (file the 2026-11-10 note; install Python and git in the VM)
```

### Index untouched
```
cached DECISIONS.md: []
 M DECISIONS.md
?? docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md
?? vm/replies/20261111T172933Z-python-git-install.md
```

## Second issue found (reported, not fixed)
`docs/specs/2026-11-10-f2-session-flat-proposal.md`:8 cites the F2 unblock clause as `specs/SPEC_RUBRIC.md`:43–44. In the current rubric it is at :30–31 (grep above). D-2026-11-11-A cites :30–31.

## Files staged
None. The brief forbids git add and index changes. Files written: DECISIONS.md (append only, lines 2100–2195) and this report. No other file was written. The return-handoff file and the install reply were only read.

## Result: PASS

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
