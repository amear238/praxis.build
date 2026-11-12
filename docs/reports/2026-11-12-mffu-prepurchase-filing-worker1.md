# Unit 2026-11-12-mffu-prepurchase-filing — ADVERSARIAL worker 1 report

## Task

Mode: ADVERSARIAL. Try to break `docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md` (377 lines; "the artifact") against S1, S2, S5, S6, S8, S13, rubric F4, the de-identification rules, the placeholder rule, the forbidden-string rule and the MANIFEST append. Input it grades: `docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md` ("the input"). Baseline `main` at `ee54344`; R6 design read from `r6/announcement-research` (`bf6fcc7`) with `git show`. Read-only: nothing edited except this file; nothing staged; no git refs, VM, `vm/` or `.claude/` touched.

Criteria (rubric rows, `specs/SPEC_RUBRIC.md`): S1 :124, S2 :125, S5 :128, S6 :129, S8 :131, S13 :136; F4 :48-57.

## Checks run

### C1 — S1 re-runs: every pasted evidence block re-run and diffed against the artifact (all 8 blocks)

E0 (the input quote block):

```text
$ A=docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md; F=docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md
$ awk 'NR==3 || (NR>=8 && NR<=10) || NR==13 || NR==14 || (NR>=16 && NR<=27) || NR==29 || NR==30 || (NR>=32 && NR<=39) || NR==43 {print NR": "$0}' $F > /tmp/w1_e0_mine.txt
$ sed -n '134,162p' $A > /tmp/w1_e0_art.txt
$ diff /tmp/w1_e0_mine.txt /tmp/w1_e0_art.txt; echo "E0 diff exit $?"; wc -l /tmp/w1_e0_mine.txt /tmp/w1_e0_art.txt
E0 diff exit 0
      29 /tmp/w1_e0_mine.txt
      29 /tmp/w1_e0_art.txt
      58 total
```

E1 and E1d (input de-identification and S13 placement; the S13 sentence is not printed):

```text
$ F=docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md
$ wc -l -c $F; shasum -a 256 $F; git rev-parse --short HEAD; git rev-parse --short r6/announcement-research
      46    6510 docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md
9eedfe85c125fc5be2eb5686b5b9df41dd42e5d9463c2309891561b5b2493598  docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md
ee54344
bf6fcc7
$ grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' $F
0
$ TOK=$(ls docs/reports/evidence | grep mffu | head -1 | sed 's/.*mffu-//; s/-reply.*//'); echo "token length ${#TOK}"
token length 4
$ grep -ci -- "$TOK" $F
0
$ printf "x%sx\n" "$TOK" | grep -ci -- "$TOK"
1
$ grep -oE '\b([0-9]{1,3}\.){3}[0-9]{1,3}\b' $F | grep -vc '^127\.0\.0\.1$'
0
$ grep -ciE '\b([0-9a-f]{2}[:-]){5}[0-9a-f]{2}\b' $F
0
$ grep -ciE '(\.ssh/|id_rsa|id_ed25519|\.pem\b|authorized_keys|known_hosts)' $F
0
$ S=$(grep -o '"Fills are optimistic[^"]*"' specs/SPEC_RUBRIC.md | head -1 | tr -d '"'); echo "sentence length ${#S}"
sentence length 90
$ grep -cF -- "$S" $F
1
$ grep -nF -- "$S" $F | cut -d: -f1
5
$ sed -n 5p $F | cut -c22- | cmp -s - <(printf "%s\n" "$S") && echo "line 5 identical"
line 5 identical
```

E2/E3 (13 commands): I ran them as one group into a file. The artifact's block was then stripped of its `$ ` command-echo lines and `#` comments, and the two were diffed. The group is the artifact's own commands from lines 227-260, unchanged, with `$D` and `$I` set as in the artifact:

```text
$ D=docs/specs/2026-11-09-r6-announcement-research-design.md; I=docs/reports/2026-11-11-mffu-connection-investigation.md
$ { git rev-parse --short r6/announcement-research
git grep -c "OPEN-1" HEAD -- docs/specs; echo "exit $?"
git grep -c "OPEN-1" r6/announcement-research -- docs/specs
git show r6/announcement-research:$D | awk 'NR==25 || NR==28 || NR==110 {print NR": "$0}'
git show r6/announcement-research:$D | awk 'NR==15' | grep -o 'Trades may be placed[^"]*"\|All positions must be closed before the daily session close. Holding overnight will breach the account.'
sed -n 2131p DECISIONS.md | grep -o 'MFFU compliance governs; nothing across the 16:10-18:00 ET close; evening entries stand on MFFU.s written answer\|V3 does not close OPEN-1. R6 stays open pending MFFU.s written answer to OPEN-1'
git grep -n -i -E 'T1|tier ?1' HEAD -- docs/specs specs/SPEC_RUBRIC.md | wc -l
git show r6/announcement-research:$D | awk 'NR==22 || NR==66 {print NR": "$0}'
git show r6/announcement-research:$D | awk 'NR==29' | grep -o 'All positions must be flattened at least two minutes prior to the scheduled T1 News event.\|On Builder Sim Funded, MFFU.s text conflicts (image banner vs Builder guides) → treated as blocked under (i) \[D1\]'
awk 'NR==1445 {print NR": "$0}' $I
git show r6/announcement-research:$D | awk 'NR==29' | grep -o 'Allowed by the T1 rule in evaluations, Studio and Live per MFFU.s text'
git ls-tree -r --name-only r6/announcement-research -- ninjascript | grep -c -i -E 'announce|drift|premium|r6'; echo "exit $?"
git ls-tree -r --name-only r6/announcement-research -- ninjascript | wc -l
} > /tmp/w1_e23_mine.txt 2>&1
$ grep -v '^\$ \|^# ' <(sed -n '225,261p' $A) > /tmp/w1_e23_art.txt
$ diff /tmp/w1_e23_mine.txt /tmp/w1_e23_art.txt; echo "E2/E3 diff exit $?"
E2/E3 diff exit 0
```

I used the same method for E3b/E4/E5/E6 (the 17 commands at artifact lines 270-326, compared against `sed -n '267,326p'`) and for the continued block, E5b and E8 (the 5 commands at artifact lines 331, 333, 336, 344 and 373, compared against `sed -n '331,337p;344,350p;374p'` with the fence lines stripped). Each group is the artifact's commands, unchanged, written to `/tmp/w1_e46_mine.txt` and `/tmp/w1_e5b_mine.txt`. The two diffs:

```text
$ diff /tmp/w1_e46_mine.txt /tmp/w1_e46_art.txt; echo "E3b-E6 diff exit $?"
E3b-E6 diff exit 0
$ diff /tmp/w1_e5b_mine.txt /tmp/w1_e5b_art.txt; echo "E5b/E8 diff exit $?"
E5b/E8 diff exit 0
```

E7 (MANIFEST) is re-run in C8. All pasted outputs in the artifact reproduce byte for byte.

### C2 — S1: quoted strings in the prose (lines 1-127) found in the cited sources

```text
$ git show r6/announcement-research:docs/specs/2026-11-09-r6-announcement-research-design.md > /tmp/w1_r6design.md
$ cat docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md /tmp/w1_r6design.md DECISIONS.md DECISION_LOG.md specs/SPEC_RUBRIC.md docs/reports/2026-11-11-mffu-connection-investigation.md ninjascript/PraxisSignalConsumer.cs docs/reports/2026-10-30-run3-backtest-screenshot-record.md > /tmp/w1_corpus.txt
$ head -n 127 $A | python3 -I -c '
import re,sys
corpus=open("/tmp/w1_corpus.txt",encoding="utf-8").read()
text=sys.stdin.read()
qs=re.findall(r"\"([^\"\n]{12,})\"",text)
miss=0
for q in qs:
    parts=[p.strip() for p in q.split("(...)")]
    ok=all(p in corpus for p in parts if p)
    if not ok:
        miss+=1; print("NOT FOUND:",q[:140])
print("quoted strings checked:",len(qs),"not found:",miss)
'
NOT FOUND: MFFU support says
NOT FOUND: the input file says MFFU support wrote
NOT FOUND:  (input :8-9) are REPORTED BY the channel; the ledger record is DECISION_LOG.md:849, which itself says 
NOT FOUND: , with no exemption guaranteed and no confirmation 
NOT FOUND: . The 7-day figure matches the MFFU page text already in the repo (E5: investigation :1380, 
NOT FOUND:  and the pasted lines do not say that no working order exists inside T±2. That is UNVERIFIED. The R6 strategies have no file under `ninjascr
NOT FOUND: ; R6 design :29 treats Builder as blocked because 
NOT FOUND: . The reply is new text on that conflict; the design's rule (i) applies the window on every account anyway, so nothing in the design is loos
NOT FOUND: , consistent with design :29's 
NOT FOUND: , and does not say whether such a hold counts as holding overnight, which is how design :28 and message 3 item (4) (
NOT FOUND: , input :29) put it. Reading 
NOT FOUND: not overnight
NOT FOUND: ` (:48) and `Account.Name.StartsWith(RequiredAccountPrefix, ...)` at start-up (:100) and at the order boundary (:639); header :39, 
NOT FOUND: . The investigation's Correction 1 (E4, :347): 
NOT FOUND:  connection had a name starting with 
quoted strings checked: 70 not found: 15
```

All 15 misses come from the parser, not from misquotes. They are prose between two quotes, which the regex picks up when quotes are nested, plus two of the artifact's own labels ("MFFU support says", "not overnight"). Every real quotation was found. I also checked each line-number citation against the source line: input :3, :8-10, :13-14, :17, :19, :21, :23, :25-27, :29-30, :33, :35, :37, :39, :43; design :15, :22, :25, :28, :29, :66, :96, :103, :110; DECISIONS.md :950, :2101, :2108, :2111, :2131, :2172; investigation :118, :318, :347, :979, :1380, :1445; rubric :3-6, :30-31, :48-57; consumer :39, :48, :100, :639; run3 record :1, :13, :69, :74. All of them match, through the E-block diffs in C1.

### C3 — S1: prose claims with no pasted block

```text
$ sed -n 849p DECISION_LOG.md | grep -o -E '^- \[2026-11-12T02:41:00Z\] WHO: amear|a channel-reported instruction is recorded, not proven given'
- [2026-11-12T02:41:00Z] WHO: amear
a channel-reported instruction is recorded, not proven given
$ grep -c -E '^\$ .*DECISION_LOG' $A
0
$ tail -c 1 docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md | xxd -p
0a
$ wc -l specs/SPEC_RUBRIC.md
     461 specs/SPEC_RUBRIC.md
$ sed -n 2131p DECISIONS.md | grep -o '^\*\*V3 as clarified by V5 — overnight holding\.\*\*'
**V3 as clarified by V5 — overnight holding.**
$ grep -n -c -E 'Connection|AccountType|Simulat' ninjascript/PraxisSignalConsumer.cs; awk 'NR==96 || NR==637 {print NR": "$0}' ninjascript/PraxisSignalConsumer.cs
0
96: 			else if (State == State.DataLoaded)
637: 			// Defense in depth: re-assert the sim wall at the order boundary.
$ grep -n '^## ' DECISIONS.md | awk -F: '$1>=2095 && $1<=2180 {print $1}'
2101
2176
```

Each of these claims is true on disk. None has a pasted block in the artifact: DECISION_LOG.md:849 and its quote (artifact :5, :16), the 461 lines (:27), the trailing newline (:29, which cites E1, but E1 has only `wc -l -c`), the "V3 with V5" label (:116), the claim that the guard reads the name and not the connection property (:89), "start-up" and "order boundary" (:88), and line 2111 lying inside D-2026-11-11-A (:78). The claim at :84 that "no team decision is on disk" has no search pasted, and I did not test it either.

### C4 — S2 / S8: Q2's premise against the reply text

```text
$ sed -n 119p $A
Q2. Should F4's bar change, given that MFFU support says it will not approve a specific configuration in writing?
$ F=docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md
$ grep -c 'will not approve' $F; grep -n -o 'will not approve[^.]*' $F; grep -n -o 'cannot be approved in writing from the available information' $F; grep -n -o 'our team can review the details you.ve provided' $F
1
46:will not approve a specific configuration in writing, and does not confirm unattended execution
33:cannot be approved in writing from the available information
17:our team can review the details you've provided
```

The words "will not approve" appear only at input :46, which is the channel's own reading. They do not appear in either MFFU reply.

### C5 — S8: scan for leaning or answering wording (prose, lines 1-127)

```text
$ head -n 127 $A | /usr/bin/grep -n -o -i -E 'that is the gap[^.]*\.|meets[^.]*|should[^?.]*'
71:should be configured with the account type set to Simulation in the NinjaTrader connection properties
75:meets; no MFFU text says it in terms of an evening entry
76:That is the gap design :110 names ("no MFFU text says it in terms of an evening entry").
119:Should F4's bar change, given that MFFU support says it will not approve a specific configuration in writing
$ head -n 127 $A | /usr/bin/grep -n -i -E 'recommend|suggest|prefer|answered|answers|resolv|satisf|closes|is closed|propos|lean|advis' | cut -c1-60
5:File the Claude.ai channel's return handoff `docs/reports/
18:- S8: Q1 and Q2 are listed for Amear and not answered; no
30:4. Found the repo text for each item by `grep` on the wor
47:What it says (REPORTED BY): the rule applies after 7 cons
88:1. Consumer Sim-only guard (Block 1/3 code) vs R2 point 3
```

Lines 71 and 75 are quotes. The hits at 5, 30, 47 and 88 are "answers"/"propos"/"advis" inside quoted or neutral text; nothing in them recommends anything. No line says OPEN-1 is closed. Line 76 does say "Whether R2 point 4 closes OPEN-1 is not decided here; it is Q1."

### C6 — S8 structure and F4

```text
$ grep -n '^## ' $A
3:## Task
11:## Rubric criteria addressed
21:## Workers dispatched (id, mode, outcome)
25:## Process log
33:## Grading of the MFFU statements
86:## S6 cross-block check
95:## Adversarial findings
99:## Files staged
103:## Result
107:## Questions for Amear (his, not D2 items)
128:## Verification evidence (command output)
$ grep -n -E '^Q[0-9]+\.' $A | cut -c1-12
109:Q1. Does
119:Q2. Shou
$ Q=$(awk 'NR>=49 && NR<=50' specs/SPEC_RUBRIC.md | tr '\n' ' ' | sed 's/^\*\*Criterion\.\*\* //; s/ $//'); echo "rubric F4 text length ${#Q}"; echo "$Q"; echo "exact F4 quote occurrences in artifact: $(grep -cF -- "\"$Q\"" $A)"; grep -nF -- "\"$Q\"" $A | cut -d: -f1 | paste -sd, -
rubric F4 text length 102
Written confirmation from MFFU that this specific automation pattern is permitted on a funded account.
exact F4 quote occurrences in artifact: 3
13,82,122
```

The F4 text is quoted exactly 3 times. Line 82 grades it "NOT MET. F4 stays FROZEN; Owner Amear." Q1 is worded neutrally. There are exactly two questions. The Questions section is not the last section, because Verification evidence (:128-375) comes after it.

### C7 — S6: the consumer guard, and DECISIONS.md:950 in context

```text
$ grep -n -E "RequiredAccountPrefix|HARD SCOPE WALL" ninjascript/PraxisSignalConsumer.cs
39:// HARD SCOPE WALL: refuses to run unless the attached account name starts with "Sim"
48:		private const string RequiredAccountPrefix = "Sim";
100:					&& Account.Name.StartsWith(RequiredAccountPrefix, StringComparison.OrdinalIgnoreCase);
106:						+ RequiredAccountPrefix + "'). No signals will be processed. SIM ONLY.", LogLevel.Error);
639:				|| !Account.Name.StartsWith(RequiredAccountPrefix, StringComparison.OrdinalIgnoreCase))
$ git grep -n -i -E 'StartsWith\(|"Sim' HEAD -- ninjascript | cut -c1-200
HEAD:ninjascript/PraxisSignalConsumer.cs:39:// HARD SCOPE WALL: refuses to run unless the attached account name starts with "Sim"
HEAD:ninjascript/PraxisSignalConsumer.cs:48:		private const string RequiredAccountPrefix = "Sim";
HEAD:ninjascript/PraxisSignalConsumer.cs:100:					&& Account.Name.StartsWith(RequiredAccountPrefix, StringComparison.OrdinalIgnoreCase);
HEAD:ninjascript/PraxisSignalConsumer.cs:639:				|| !Account.Name.StartsWith(RequiredAccountPrefix, StringComparison.OrdinalIgnoreCase))
$ git ls-tree -r --name-only r6/announcement-research -- ninjascript
ninjascript/PraxisLastHalfHourMomentum.cs
ninjascript/PraxisNoiseAreaBreakout.cs
ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs
ninjascript/PraxisSignalConsumer.cs
$ awk 'NR==949 || NR==950 {print NR": "$0}' DECISIONS.md
949: - **R-VN4-8** — D-071: "Yes."
950:   - reading (voice agent, notes-4): **The MFFU Rithmic connection is approved to be opened when Block 4 starts.** D-071 (Simulated Data Feed only) stands until then.
$ sed -n 927p DECISIONS.md | grep -o 'RULED by Amear — R-VN4-1..14, graded REPORTED BY the voice agent.'
RULED by Amear — R-VN4-1..14, graded REPORTED BY the voice agent.
```

The line numbers the artifact gives for the guard (:39, :48, :100, :639) are correct. The consumer is the only file that has a Sim guard. The artifact's claim that there is no R6 strategy file under `ninjascript/` on the branch holds: the branch has 5 files there and none of them is R6. The artifact decides nothing about the guard: :89 says "Nothing is decided; any change ... is D2(b), Amear's."

### C8 — MANIFEST (item 10)

```text
$ wc -l /tmp/mffu-prepurchase-MANIFEST.before MANIFEST.md
     426 /tmp/mffu-prepurchase-MANIFEST.before
     429 MANIFEST.md
     855 total
$ head -n 426 MANIFEST.md | cmp - /tmp/mffu-prepurchase-MANIFEST.before && echo "first 426 lines byte-identical"
first 426 lines byte-identical
$ diff /tmp/mffu-prepurchase-MANIFEST.before MANIFEST.md | head -1; diff /tmp/mffu-prepurchase-MANIFEST.before MANIFEST.md | grep -c '^>'; diff /tmp/mffu-prepurchase-MANIFEST.before MANIFEST.md | grep -c '^<'
426a427,429
3
0
$ tail -n 3 MANIFEST.md | cut -d'|' -f2
 /docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md 
 /docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md 
 /docs/reports/2026-11-12-mffu-prepurchase-filing-worker1.md 
$ diff /tmp/mffu-prepurchase-MANIFEST.before MANIFEST.md | sed -n '2,4p' | diff - <(sed -n '358,360p' docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md) && echo "appended rows match artifact E7 paste"
appended rows match artifact E7 paste
$ git diff HEAD -U0 -- MANIFEST.md | grep '^@@'
@@ -306,0 +307,8 @@
@@ -418,0 +427,3 @@
```

This unit's 3 rows are appended at the end, and nothing above them changed relative to the snapshot. The other units' 8 uncommitted rows were inserted after HEAD line 306, not appended. That is outside this unit's scope; I report it and do not fix it.

### C9 — de-identification, S13 and forbidden strings in the artifact (runtime-built tokens; nothing sensitive printed)

```text
$ A=docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md
$ echo "email lines: $(grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' $A)"
email lines: 0
$ echo "email control: $(printf '%s@%s.%s\n' qq rr org | grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}')"
email control: 1
$ grep -n '@' $A | cut -d: -f1; grep -n '@' $A | grep -c 'grep -cE'
178
180
2
$ TOK=$(ls docs/reports/evidence | grep mffu | head -1 | sed 's/.*mffu-//; s/-reply.*//'); echo "token length ${#TOK}"
token length 4
$ echo "token hits in artifact: $(grep -ci -- "$TOK" $A)"
token hits in artifact: 0
$ echo "token control: $(printf 'y%sy\n' "$TOK" | grep -ci -- "$TOK")"
token control: 1
$ echo "token hits in MANIFEST appended rows: $(tail -n 3 MANIFEST.md | grep -ci -- "$TOK")"
token hits in MANIFEST appended rows: 0
$ S=$(grep -o '"Fills are optimistic[^"]*"' specs/SPEC_RUBRIC.md | head -1 | tr -d '"'); echo "sentence length ${#S}"
sentence length 90
$ echo "S13 count: $(grep -cF -- "$S" $A)"
S13 count: 1
$ echo "S13 line: $(grep -nF -- "$S" $A | cut -d: -f1)"; echo "total lines: $(wc -l < $A)"
S13 line: 377
total lines:      377
$ tail -n 1 $A | cmp -s - <(printf '%s\n' "$S") && echo "last line byte-identical to rubric sentence, standalone"
last line byte-identical to rubric sentence, standalone
$ echo "line before last is blank: [$(tail -n 2 $A | head -1)]"
line before last is blank: []
$ W1=$(printf 'ver%s' dict); W2=$(printf 'COMMIT-%s' INDEX); W3=$(printf 'COMMIT-DIFF-%s' SHA256); echo "w1: $(grep -ci -- "$W1" $A)"; echo "w2: $(grep -c -- "$W2" $A)"; echo "w3: $(grep -c -- "$W3" $A)"; echo "w1 control: $(printf 'x%sx\n' "$W1" | grep -ci -- "$W1")"; echo "git-status markers: $(grep -c -E 'git status|On branch|Changes not staged|Untracked files' $A)"
w1: 0
w2: 0
w3: 0
w1 control: 1
git-status markers: 0
```

The two lines in the artifact that contain `@` are the email regex itself, at :178 and :180.

### C10 — placeholders and undefined variables in the artifact's pasted commands

```text
$ grep -n '^\$ ' $A | grep -n -E '\.\.\.|<[^>(]*>' ; echo "placeholder exit $?"
placeholder exit 1
$ printf '$ grep foo ...\n$ cat <path>\n$ echo ok\n' | grep -n -E '\.\.\.|<[^>(]*>'
1:$ grep foo ...
2:$ cat <path>
$ awk '/^```/{inb=!inb; if(inb){blk++; delete def}; next} inb && /^\$ /{ line=$0; if (match(line,/^\$ [A-Z][A-Z0-9_]*=/)) { v=substr(line,3,RLENGTH-3); def[v]=1 } ; while (match(line,/\$\{?#?[A-Z][A-Z0-9_]*/)) { t=substr(line,RSTART,RLENGTH); gsub(/[\$\{#]/,"",t); if(!(t in def)) print "block "blk": undefined "t" in: "substr($0,1,80); line=substr(line,RSTART+RLENGTH) } ; if (match($0,/TOK=/)) def["TOK"]=1; if (match($0,/S=\$\(/)) def["S"]=1 }' $A; echo "var scan done"
var scan done
$ printf '```text\n$ X=1\n$ echo $X $Y\n```\n```text\n$ echo $X\n```\n' > /tmp/w1_varctl.md; awk '/^```/{inb=!inb; if(inb){blk++; delete def}; next} inb && /^\$ /{ line=$0; if (match(line,/^\$ [A-Z][A-Z0-9_]*=/)) { v=substr(line,3,RLENGTH-3); def[v]=1 } ; while (match(line,/\$\{?#?[A-Z][A-Z0-9_]*/)) { t=substr(line,RSTART,RLENGTH); gsub(/[\$\{#]/,"",t); if(!(t in def)) print "block "blk": undefined "t; line=substr(line,RSTART+RLENGTH) } }' /tmp/w1_varctl.md
block 1: undefined Y
block 2: undefined X
```

The artifact's pasted commands contain no placeholders and no undefined variables, and the positive controls fire. The `(...)` at artifact :78 and :84 marks elisions inside quotations, not commands.

### C11 — the T1 count pasted at artifact :245-246

```text
$ git grep -n -i -E 'tier ?1|T1 news|T1 release' HEAD -- docs/specs specs/SPEC_RUBRIC.md | wc -l
       0
$ git grep -n -i -E 'T1|tier ?1' HEAD -- docs/specs specs/SPEC_RUBRIC.md | grep -c -E '[0-9]T1[0-9]|Flat1559|T1–T3|T1-T3'
73
```

### C12 — artifact :50, the Run 3 flat period

```text
$ awk 'NR==74 {print NR": "$0}' docs/reports/2026-10-30-run3-backtest-screenshot-record.md
74: | Longest flat period | 20.88 days | 30.94 days | 34.98 days |
```

## Findings

1. **MAJOR — artifact :119 (Q2), S2 and S8.** Q2 reads "given that MFFU support says it will not approve a specific configuration in writing". MFFU's text does not say that. The words "will not approve" appear only in the channel's own reading at input :46 (C4). MFFU support wrote "cannot be approved in writing from the available information" (input :33), and R1 offers "our team can review the details you've provided" (input :17). So the question attributes the channel's paraphrase to MFFU. It also turns a conditional refusal ("from the available information", with a team review offered and none on disk) into a flat one. That premise steers Amear toward changing F4's bar, so the question is not neutral. Minimal fix: "Q2. Should F4's bar change?" Leave the facts list (:121-126) as it is, since it already quotes :33 and :17 exactly.

2. **MAJOR — artifact :14, :16 and :5, S1.** Line 14 says "every claim below rests on a pasted block in `Verification evidence (command output)` (E0-E7)". That is false. Line 16 quotes DECISION_LOG.md:849 ("a channel-reported instruction is recorded, not proven given"), and line 5 cites the same line as the unit's authority (2026-11-12T02:41:00Z). No evidence block contains any DECISION_LOG command (C3: `grep -c -E '^\$ .*DECISION_LOG'` returns 0). The text is accurate on disk (C3). But this is the S5 authorisation record, the report quotes it, and the report claims S1 compliance, so the missing paste is load-bearing. Minimal fix: add `sed -n 849p DECISION_LOG.md | grep -o -E '^- \[2026-11-12T02:41:00Z\] WHO: amear|a channel-reported instruction is recorded, not proven given'` with its output to E6.

3. **MINOR — artifact :27, :29, :78, :84, :88, :89, :116, S1.** These claims are true but have no paste (C3): the rubric is 461 lines (:27); the input "ends in a newline (E1)" (:29), but E1 has only `wc -l -c`, so the citation is wrong; line 2111 sits inside D-2026-11-11-A (:78); "no team decision is on disk" (:84), which no search backs; "start-up" (State.DataLoaded, :96) and "order boundary" (comment :637) (:88); the guard reads the account name and not the connection's account-type property (:89; the negative grep returns 0); and "V3 with V5" (:116). Fix: add the C3 commands to the evidence. Either add a search for :84 or reword it to "no team decision is in the input".

4. **MINOR — artifact :76 and :111-117, S8 leaning.** "That is the gap design :110 names" asserts that a support email (REPORTED BY, possibly an automated assistant's) counts as "MFFU text" that "says it in terms of an evening entry". That is part of what Q1 asks. The Q1 facts list then sets the reply directly beside the trimmed OPEN-1 text, which invites a yes. It also leaves out the main counter-fact the artifact itself found at :76: the reply does not use the word "overnight", although the outgoing question (investigation :1445 Q4, input :29 item 4) asked in exactly those terms. Fix: change :76 to "Whether that text is the written MFFU answer design :110 asks for is Q1", and add the "does not use the word overnight" fact to Q1's list.

5. **MINOR — artifact :67, :76, :59, S2.** G1 (:39) and G6 (:63) hedge with "if accurate (REPORTED BY)". G7 (:67) says "Establishes:" with no hedge, about MFFU's policy. Line 76 says "R2 point 4 is MFFU support text" as a plain fact. Line 59 says "The outgoing ticket said the same window (E3: investigation :1445)". But :1445 is the C3.3 draft; the sent text is not on disk, and input :13 ("Five questions as C3.3") is REPORTED BY the channel. Fix: hedge G7 the same way as G1/G6, write "the input gives as MFFU support's text" at :76, and write "the C3.3 draft said the same window; the sent text is REPORTED BY the channel as C3.3's (input :13)" at :59.

6. **MINOR — artifact :90, S2.** The prose quotes DECISIONS.md:950 as the standing D-071 position without saying that it is the voice agent's reading of Amear's one-word "Yes." (DECISIONS.md:949). DECISIONS.md:927 grades the whole entry "REPORTED BY the voice agent" (C7). The E4 paste shows "reading (voice agent, notes-4):", but the prose leaves it out. Fix: "DECISIONS.md:950, the voice agent's reading of R-VN4-8 (:949), REPORTED BY: ...".

7. **MINOR — artifact :89, S6 precision.** The guard compares with `StringComparison.OrdinalIgnoreCase` (:100, :639; C7). So it admits any account name that starts with "sim" in any case, not only "Sim". The artifact's case analysis ("had a name starting with "Sim"") therefore understates which names it admits. The conclusion is unchanged: the case is UNVERIFIED and nothing is decided. Fix: "a name starting with "sim" in any letter case (the comparison is OrdinalIgnoreCase)".

8. **MINOR — artifact :50, S2 wording.** "On both figures the strategy ... has stretches of more than 7 calendar days without a trade." For Run 3 the record gives one figure, "Longest flat period 20.88 days" (C12). That shows at least one such stretch, not several. The R6 figure (90 of 173 gaps) does support the plural. Fix: "R6: 90 gaps over 7 days; Run 3: at least one (longest flat period 20.88 days)".

9. **MINOR — artifact :9, input :44-46 not graded.** The provenance paragraph grades only input :43. The channel's reading at input :44 says R6 OPEN-1 was "answered in writing by MFFU support", which is a lean on Q1 sitting in a file this unit files unedited. Input :46 is where Q2's "will not approve" came from (finding 1). Fix: one sentence at :9 saying that input :44-46 are the channel's readings, INFERRED, and that this unit does not adopt them.

10. **MINOR — artifact :245-246, S1 relevance.** The pasted count `102` for `T1|tier ?1` on HEAD's specs is not used anywhere in the prose. On its face it suggests T1-news text on main, which E3b at :270-271 says does not exist. In fact 0 of those hits are T1 news (C11), and 73 are timestamps, `Flat1559` or tests T1-T3. Fix: drop that command, or replace it with the `tier ?1|T1 news|T1 release` count (0).

11. **MINOR — artifact :107-128, structure.** The brief asks for the report to end with `## Questions for Amear (his, not D2 items)`. In the artifact, `## Verification evidence (command output)` (:128-375) comes after it. Fix: move the Questions section so it sits after the evidence and directly before the final S13 line.

Checks with no break: E0-E8 reproduce byte for byte (C1). All prose quotations and line citations match their sources (C2). The F4 text is quoted exactly, and F4 is graded FROZEN / NOT MET (C6). There are exactly two questions, and nothing states OPEN-1 is closed (C5, C6). There are 0 email addresses, the regex control fires, there are 0 hits for the rep's name, and the token control fires (C9). The S13 sentence appears once, as the standalone final line, byte-identical to the rubric (C9). There are 0 forbidden strings and no pasted `git status` (C9). The pasted commands contain no placeholders or undefined variables (C10). The guard line numbers are correct, and nothing is decided about the guard or D2(b) (C7). The arithmetic is correct: 58 s, 49 s, [T−2, T+2] inside [T−5, T+3], and 16:00-18:00 contains 16:10-18:00. The 3 MANIFEST rows are appended at the end, and lines 1-426 are byte-identical to the snapshot (C8).

Out of scope, reported only: MANIFEST.md has 8 uncommitted rows from other units inserted after HEAD line 306 rather than appended (C8). Artifact :23, :97 and :105 still read "(filled after the worker returns)". That is expected at this stage, but they must be filled in before the report is graded.

## Files staged

None. The only file written is this report, and it is untracked.

## Result

FAIL (2 MAJOR: findings 1 and 2; 9 MINOR).

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
