# Unit 2026-11-13-open-a1-cure: adversarial worker 1 report

## Task

Mode: ADVERSARIAL (cold, read-only). The claim under test: the cure of entry D-2026-11-13-B (DECISIONS.md), the one appended MANIFEST.md row, and the manager report docs/reports/2026-11-13-open-a1-cure-manager.md were done exactly as specified (five edits) and meet the stated rules. Criteria: specs/SPEC_RUBRIC.md S1 (:133), S2 (:134), S6 (:138), S13 (:145). I verified everything from the files and did not rely on report prose. All commands were run from /Volumes/Sensidine/Praxis.build. `grep` is /usr/bin/grep under /bin/bash, not the zsh alias.

## Checks

### (a) diff against both pre-copies shows only the briefed edits: PASS

Command:
```
/bin/bash -c 'diff /tmp/oa1c-pre-DECISIONS.md DECISIONS.md; echo "rc=$?"; diff /tmp/oa1c-pre-MANIFEST.md MANIFEST.md; echo "rc=$?"; wc -l DECISIONS.md MANIFEST.md /tmp/oa1c-pre-DECISIONS.md /tmp/oa1c-pre-MANIFEST.md'
```
Output:
```
2422c2422
< **Decision.** Option (a) of topology :198: amended #4's "cancel working entry orders" and "confirm flat before 4:10 PM ET (alert if not)" (spec :212) are both part of the FLATTEN command the consumer executes at the flat time; the consumer cancels its own working entries and reports flat or not flat. The master's reason: option (b) depends on OPEN-T3 (topology :100), which is unresolved, and (a) keeps both actions on the order path that already carries FLATTEN (topology :61). CONDITIONAL: this rests on the unobserved mechanism that the consumer can see and cancel its own working entry orders and read its own position; FLATTEN as an instruction type is unbuilt (OPEN-T2, topology :99). Void clause: if either is observed false, the placement is re-decided toward (b) after OPEN-T3. Named gap: where the "alert" goes is not decided here. Not a D2 item (no money, no live path switched on, no breaker value, no credential). OPEN-A2 is not decided here.
---
> **Decision.** Option (a) of topology :198: amended #4's "cancel working entry orders" and "confirm flat before 4:10 PM ET (alert if not)" (spec :212) are both part of the FLATTEN command the consumer executes at the flat time; the consumer cancels its own working entries and reports flat or not flat. The master's reason: option (b) depends on OPEN-T3 (topology :100), which is unresolved. CONDITIONAL: this rests on the unobserved mechanism that the consumer can see and cancel its own working entry orders and read its own position; FLATTEN as an instruction type is unbuilt (OPEN-T2, topology :99). Void clause: if either is observed false, the placement is re-decided toward (b) after OPEN-T3. Named gap: where the "alert" goes is not decided here. Not a D2 item (no money, no live path switched on, no breaker value, no credential). OPEN-A2 is not decided here.
2425c2425
< - Topology `docs/specs/2026-11-10-live-signal-topology.md`: :198 "(a) Both are part of the FLATTEN command the consumer executes at the flat time (the consumer cancels its own working entries and reports flat or not flat)." and "(b) The confirmation is a separate n8n-side check on account state, which needs the account-state feed of OPEN-T3."; :99 "EXIT / FLATTEN types, unbuilt"; :100 "Where account state (P&L, equity, fills, open position) comes from, and how fresh it must be."; :61 "Its "close positions" action: the emitter's own time exit posted as a FLATTEN signal, plus the FLATTEN command from n8n at the gate time."; :106 "D8(8): the final step of this build is a Block 4 paper pass on MFFU sim; Block 5 live is a separate sign-off."
---
> - Topology `docs/specs/2026-11-10-live-signal-topology.md`: :198 "(a) Both are part of the FLATTEN command the consumer executes at the flat time (the consumer cancels its own working entries and reports flat or not flat)." and "(b) The confirmation is a separate n8n-side check on account state, which needs the account-state feed of OPEN-T3."; :99 "EXIT / FLATTEN types, unbuilt"; :100 "Where account state (P&L, equity, fills, open position) comes from, and how fresh it must be."; :61 "Its "close positions" action: the emitter's own time exit posted as a FLATTEN signal, plus the FLATTEN command from n8n at the gate time."; :58 "Its "cancel all, flatten" action: n8n writes a FLATTEN command file that the consumer executes"; :106 "D8(8): the final step of this build is a Block 4 paper pass on MFFU sim; Block 5 live is a separate sign-off."
2428c2428
< **S6 cross-block.** Block 3 breakers and topology: the two #4 actions at spec :212 are placed inside FLATTEN, the same command topology :61 already uses for #4's "close positions" action; no topology row and no spec text is edited. OPEN-T2 (topology :99) stays open; under (a) the FLATTEN type it names is where both actions would live. OPEN-T3 (topology :100) stays open; option (b) waits on it under the void clause. Block 4 paper (topology :106): no Block 4 text is changed. Nothing else is edited.
---
> **S6 cross-block.** Block 3 breakers and topology: the two #4 actions at spec :212 are placed inside FLATTEN, the same command topology :61 names for #4's "close positions" action; no topology row and no spec text is edited. OPEN-T2 (topology :99) stays open; under (a) the FLATTEN type it names is where both actions would live. OPEN-T3 (topology :100) stays open; option (b) waits on it under the void clause. Block 4 paper (topology :106): no Block 4 text is changed. Named gap: breaker #1's "cancel all, flatten" action (topology :58) is also specified as a FLATTEN command file the consumer executes; whether #1's flatten carries the cancel and confirm-flat steps placed here for #4 is not decided here. Nothing else is edited.
rc=1
473a474
> | /docs/reports/2026-11-13-open-a1-cure-manager.md | Report | 3 | 2026-11-13 | Evidence report for unit 2026-11-13-open-a1-cure (topology OPEN-A1, bead Praxis_build-fgd; master under D-2026-11-08-D D1, DECISION_LOG 2026-11-13T13:37:42Z and 2026-11-13T17:02:02Z): the cure of entry D-2026-11-13-B (one clause deleted in its Decision paragraph; one word replaced and one named gap on breaker #1 added in its S6 paragraph; one topology quote added to its Sources), with literal commands and full output. |
rc=1
    2434 DECISIONS.md
     474 MANIFEST.md
    2434 /tmp/oa1c-pre-DECISIONS.md
     473 /tmp/oa1c-pre-MANIFEST.md
    5815 total
```

To rule out a whitespace or byte-level difference that a visual read of the diff could miss, I rebuilt the expected files in memory from the pre-copies by applying the five briefed strings, and compared them byte-for-byte with the current files. Command:
```
python3 -I - <<'EOF'
pre=open('/tmp/oa1c-pre-DECISIONS.md','rb').read().decode()
cur=open('DECISIONS.md','rb').read().decode()
e1=', and (a) keeps both actions on the order path that already carries FLATTEN (topology :61)'
e2a='the same command topology :61 already uses for'; e2b='the same command topology :61 names for'
gap='Named gap: breaker #1\'s "cancel all, flatten" action (topology :58) is also specified as a FLATTEN command file the consumer executes; whether #1\'s flatten carries the cancel and confirm-flat steps placed here for #4 is not decided here.'
e4anchor='; :106 "D8(8)'; e4ins='; :58 "Its "cancel all, flatten" action: n8n writes a FLATTEN command file that the consumer executes"'
print('e1 count pre', pre.count(e1)); print('e2a count pre', pre.count(e2a)); print('anchor count pre', pre.count(e4anchor)); print('NothingElse count pre', pre.count(' Nothing else is edited.'))
exp=pre.replace(e1,'',1).replace(e2a,e2b,1)
exp=exp.replace(' Nothing else is edited.', ' '+gap+' Nothing else is edited.')
exp=exp.replace(e4anchor, e4ins+e4anchor,1)
print('expected==current:', exp==cur)
pm=open('/tmp/oa1c-pre-MANIFEST.md','rb').read().decode(); cm=open('MANIFEST.md','rb').read().decode()
row='| /docs/reports/2026-11-13-open-a1-cure-manager.md | Report | 3 | 2026-11-13 | Evidence report for unit 2026-11-13-open-a1-cure (topology OPEN-A1, bead Praxis_build-fgd; master under D-2026-11-08-D D1, DECISION_LOG 2026-11-13T13:37:42Z and 2026-11-13T17:02:02Z): the cure of entry D-2026-11-13-B (one clause deleted in its Decision paragraph; one word replaced and one named gap on breaker #1 added in its S6 paragraph; one topology quote added to its Sources), with literal commands and full output. |\n'
print('pre manifest ends with newline:', pm.endswith('\n')); print('manifest expected==current:', pm+row==cm)
EOF
```
Output:
```
e1 count pre 1
e2a count pre 1
anchor count pre 1
NothingElse count pre 1
expected==current: True
pre manifest ends with newline: True
manifest expected==current: True
```
All five edits match the brief byte for byte. Each anchor occurred exactly once in the pre-copy, so no edit could have landed in a second place. Nothing else changed.

### (b) The deleted phrase is gone and the Decision sentence reads correctly: PASS

Command:
```
/bin/bash -s <<'EOF'
echo "keeps both actions: $(/usr/bin/grep -cF 'keeps both actions' DECISIONS.md)"
echo "order path that already carries FLATTEN: $(/usr/bin/grep -cF 'order path that already carries FLATTEN' DECISIONS.md)"
echo "already uses for (entry range): $(awk 'NR>=2417' DECISIONS.md | /usr/bin/grep -cF 'already uses for')"
awk 'NR==2422' DECISIONS.md | /usr/bin/grep -oF 'The master'"'"'s reason: option (b) depends on OPEN-T3 (topology :100), which is unresolved. CONDITIONAL:'
echo "--- breaker #1 row at topology :58 col 2:"; awk -F'|' 'NR==58{print $2"|"$3}' docs/specs/2026-11-10-live-signal-topology.md
echo "--- evidence path / email in new MANIFEST row:"; awk 'NR==474' MANIFEST.md | /usr/bin/grep -cE 'evidence/|[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]'
echo "--- report file referenced by row exists:"; test -f docs/reports/2026-11-13-open-a1-cure-manager.md && echo yes
git diff --cached --quiet -- DECISIONS.md MANIFEST.md docs/reports/2026-11-13-open-a1-cure-manager.md; echo "staged-check exit=$? (0 = none of the three staged)"
git diff --cached --name-only | wc -l
EOF
```
Full output. The lines after the fourth are the evidence for (e), (f) and (g), which refer to "block B" (this block):
```
keeps both actions: 0
order path that already carries FLATTEN: 0
already uses for (entry range): 0
The master's reason: option (b) depends on OPEN-T3 (topology :100), which is unresolved. CONDITIONAL:
--- breaker #1 row at topology :58 col 2:
 1 | Daily loss limit 
--- evidence path / email in new MANIFEST row:
0
--- report file referenced by row exists:
yes
staged-check exit=0 (0 = none of the three staged)
       1
```
The phrase is gone from the whole file. The sentence ends "...which is unresolved." and is followed directly by "CONDITIONAL:". It is grammatical, with a single period and no stray comma.

### (c) S2: nothing added or changed describes an unbuilt or specified-only thing as existing, carried, used, built or tested: PASS

This is a reading check on the changed lines DECISIONS.md :2422, :2425 and :2428, shown in full in the (a) diff.
- :2422 (Decision): the only change is the deletion. The remaining text says FLATTEN "is unbuilt (OPEN-T2, topology :99)" and marks the mechanism "CONDITIONAL ... unobserved". The phrase "the FLATTEN command the consumer executes" restates option (a) of topology :198 as the placement chosen, and it falls under the CONDITIONAL clause.
- :2425 (Sources): the added text is a byte-exact quote of topology :58. A quote is not a claim of the entry.
- :2428 (S6): "the same command topology :61 names for" uses the word "names", a design-text verb. Topology :61's Depends-on column says "FLATTEN path (unbuilt)". The added gap says "is also specified as a FLATTEN command file the consumer executes". "Specified" governs the clause, and topology :58's status column reads "SPECIFIED." The question is put as "whether ... carries ... is not decided here", which is not a claim that anything exists.
Non-failing observation: in the gap, "also specified as a FLATTEN command file" can be read as saying #4's FLATTEN is a "command file". Topology :61 says "FLATTEN command from n8n" and does not say "file". This is a matter of wording precision. It is not an S2 level claim, so I did not grade it as a break.

### (d) Every quote in the entry's Sources is byte-present at its cited line: PASS

Command:
```
/bin/bash -s <<'EOF'
T=docs/specs/2026-11-10-live-signal-topology.md; S=docs/specs/2026-11-05-phase3-build-specification.md
awk 'NR==198' $T | /usr/bin/grep -cF '(a) Both are part of the FLATTEN command the consumer executes at the flat time (the consumer cancels its own working entries and reports flat or not flat).'
awk 'NR==198' $T | /usr/bin/grep -cF '(b) The confirmation is a separate n8n-side check on account state, which needs the account-state feed of OPEN-T3.'
awk 'NR==99' $T | /usr/bin/grep -cF 'EXIT / FLATTEN types, unbuilt'
awk 'NR==100' $T | /usr/bin/grep -cF 'Where account state (P&L, equity, fills, open position) comes from, and how fresh it must be.'
awk 'NR==61' $T | /usr/bin/grep -cF "Its \"close positions\" action: the emitter's own time exit posted as a FLATTEN signal, plus the FLATTEN command from n8n at the gate time."
awk 'NR==58' $T | /usr/bin/grep -cF 'Its "cancel all, flatten" action: n8n writes a FLATTEN command file that the consumer executes'
awk 'NR==106' $T | /usr/bin/grep -cF 'D8(8): the final step of this build is a Block 4 paper pass on MFFU sim; Block 5 live is a separate sign-off.'
awk 'NR==212' $S | /usr/bin/grep -cF 'cancel working entry orders, send market orders closing all system positions, confirm flat before 4:10 PM ET (alert if not)'
awk 'NR==196' $S | /usr/bin/grep -cF 'SPECIFIED ONLY — zero implemented, zero tested, zero tested under failure.'
EOF
```
Output:
```
1
1
1
1
1
1
1
1
1
```
All nine quotes (seven topology, two spec) are present at their cited lines. The :61 check used an ASCII apostrophe, which matches the entry's bytes.

### (e) The S6 gap names breaker #1 and topology :58, and says it is not decided: PASS

Reading check on DECISIONS.md :2428 (full text in the (a) diff): "Named gap: breaker #1's "cancel all, flatten" action (topology :58) is also specified as a FLATTEN command file the consumer executes; whether #1's flatten carries the cancel and confirm-flat steps placed here for #4 is not decided here." Block B under (b) shows that topology :58 is breaker #1: its `awk -F'|' 'NR==58{print $2"|"$3}'` line prints ` 1 | Daily loss limit `.

### (f) The manager report meets every rule: FAIL

I first re-ran every command in the manager report except Block 0 (cp) and Block 4 (which writes into /tmp). The script then compared each fresh output with the pasted output. Command:
```
python3 -I - <<'EOF'
import re,subprocess
txt=open('docs/reports/2026-11-13-open-a1-cure-manager.md').read()
blocks=re.findall(r'^Block (\d+)[^\n]*\n\n```\n(.*?)```\n', txt, re.S|re.M)
print('blocks found:', len(blocks), 'fence pairs:', txt.count('\n```\n')//1)
for n,b in blocks:
    lines=b.split('\n')
    cmd=lines[0][2:]; out='\n'.join(lines[1:])
    if n in ('0','4'):
        print(f'Block {n}: SKIPPED (writes files)'); continue
    r=subprocess.run(['/bin/bash','-c',cmd],capture_output=True,text=True)
    print(f'Block {n}: match={r.stdout==out} rc={r.returncode} stderr={r.stderr!r}')
    if r.stdout!=out: print(repr(r.stdout[:300])); print(repr(out[:300]))
EOF
```
Output:
```
blocks found: 22 fence pairs: 44
Block 0: SKIPPED (writes files)
Block 1: match=True rc=0 stderr=''
Block 2: match=True rc=1 stderr=''
Block 3: match=True rc=1 stderr=''
Block 4: SKIPPED (writes files)
Block 5: match=True rc=0 stderr=''
Block 6: match=True rc=0 stderr=''
Block 7: match=True rc=0 stderr=''
Block 8: match=True rc=0 stderr=''
Block 9: match=True rc=0 stderr=''
Block 10: match=True rc=0 stderr=''
Block 11: match=True rc=0 stderr=''
Block 12: match=True rc=0 stderr=''
Block 13: match=True rc=0 stderr=''
Block 14: match=True rc=1 stderr=''
Block 15: match=True rc=1 stderr=''
Block 16: match=True rc=1 stderr=''
Block 17: match=True rc=1 stderr=''
Block 18: match=True rc=0 stderr=''
Block 19: match=True rc=0 stderr=''
Block 20: match=True rc=0 stderr=''
Block 21: match=True rc=0 stderr=''
```
For Block 4 and Block 0, I ran an equivalent check that writes no files, plus file mtimes:
```
/bin/bash -s <<'EOF'
cmp <(head -n 2416 /tmp/oa1c-pre-DECISIONS.md) <(head -n 2416 DECISIONS.md); echo "cmp exit=$?"
ls -l /tmp/oa1c-pre-head2416.txt /tmp/oa1c-post-head2416.txt 2>&1
stat -f '%Sm %N' -t '%Y-%m-%dT%H:%M:%S' /tmp/oa1c-pre-DECISIONS.md /tmp/oa1c-pre-MANIFEST.md DECISIONS.md MANIFEST.md docs/reports/2026-11-13-open-a1-cure-manager.md
EOF
```
Output:
```
cmp exit=0
-rw-r--r--@ 1 admin  wheel  439462 Nov 13 12:04 /tmp/oa1c-post-head2416.txt
-rw-r--r--@ 1 admin  wheel  439462 Nov 13 12:04 /tmp/oa1c-pre-head2416.txt
2026-11-13T12:03:15 /tmp/oa1c-pre-DECISIONS.md
2026-11-13T12:03:15 /tmp/oa1c-pre-MANIFEST.md
2026-11-13T12:03:23 DECISIONS.md
2026-11-13T12:03:27 MANIFEST.md
2026-11-13T12:05:20 docs/reports/2026-11-13-open-a1-cure-manager.md
```
The pre-copies are older than both edits, which fits Block 0's "before any edit" claim.

Rule-by-rule greps:
```
/bin/bash -s <<'EOF'
R=docs/reports/2026-11-13-open-a1-cure-manager.md
echo "T[B]D: $(/usr/bin/grep -c 'T[B]D' $R)"
echo "evidence-dir path: $(/usr/bin/grep -c 'evidenc[e]/' $R)"
echo "email: $(/usr/bin/grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]' $R)"
echo "S13 exact standalone line numbers: $(/usr/bin/grep -nx 'Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks.side slippage assumed\.' $R | cut -d: -f1 | tr '\n' ' ')"
echo "S13 substring occurrences (any position): $(/usr/bin/grep -c 'Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks.side slippage assumed\.' $R)"
echo "total lines: $(wc -l < $R)"; echo "last line: $(tail -n 1 $R)"
echo "verification heading: $(/usr/bin/grep -n '^## Verification evidence (command output)$' $R)"
echo "fenced blocks: $(( $(/usr/bin/grep -c '^```$' $R) / 2 ))"
echo "Block headers: $(/usr/bin/grep -c '^Block [0-9]' $R)"
echo "name hits:"; /usr/bin/grep -noE 'Amear|Bani-Ahmad' $R
echo "cure-worker refs: $(/usr/bin/grep -c 'cure-worker' $R)"
echo "--- entry structure (DECISIONS.md)"
awk 'NR>=2417 && /^(## |\*\*)/ {print NR": "substr($0,1,30)}' DECISIONS.md
echo "S13 line number in entry: $(awk 'NR>=2417' DECISIONS.md | /usr/bin/grep -nx 'Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks.side slippage assumed\.' | cut -d: -f1) (offset from 2417; file total $(wc -l < DECISIONS.md))"
EOF
```
This is block F. Output (its last nine lines are shown under (h)):
```
T[B]D: 0
evidence-dir path: 0
email: 0
S13 exact standalone line numbers: 249 
S13 substring occurrences (any position): 1
total lines:      250
last line: Result: PASS
verification heading: 40:## Verification evidence (command output)
fenced blocks: 22
Block headers: 22
name hits:
214:Amear
214:Amear
cure-worker refs: 0
--- entry structure (DECISIONS.md)
2418: ## 2026-11-13 — D-2026-11-13
2420: **Status:** Decided by master 
2422: **Decision.** Option (a) of to
2424: **Sources (quoted byte-exact).
2428: **S6 cross-block.** Block 3 br
2430: **Limits.** No code, no spec b
2432: **S4 timing.** Written 2026-11
S13 line number in entry: 18 (offset from 2417; file total     2434)
```
Index check (permitted form): see block B under (b). Its last two output lines are `staged-check exit=0` and `1` for `git diff --cached --name-only | wc -l`.

Rubric line citations (manager report :19 to :22). Command:
```
/bin/bash -c 'for n in 133 134 138 145; do printf "%s: " $n; awk "NR==$n" specs/SPEC_RUBRIC.md | cut -c1-90; done'
```
Output:
```
133: | S1 | Every claim in a report has pasted command output, not a description of output. |
134: | S2 | No component is reported at a higher level than the evidence supports. Specified ≠ 
138: | S6 | Cross-block check: every approved deviation is tested against the specs of every ot
145: | S13 | Every report under docs/reports/ and every DECISIONS.md entry that states a backte
```
DECISION_LOG authority (manager report :3, :7): DECISION_LOG.md :919 (13:37:42Z) contains cure items (i) to (iv). They are, quoted: "(ii) at :2422 delete ", and (a) keeps both actions on the order path that already carries FLATTEN (topology :61)"; (iii) in S6 add one named gap: breaker #1's flatten (topology :58) ...". DECISION_LOG.md :923 (17:02:02Z) contains "(v): in the S6 paragraph (:2428) replace "already uses" with "names"". Both match the report's line 3.

Per-rule grades:
- Pasted outputs were produced by the commands: PASS. 20 of 22 blocks reproduce byte-exact. Block 4's cmp reproduces as exit 0, and the two /tmp files it says it created exist with equal sizes. Block 0's cp produces no output, and the mtimes fit its claim.
- Literal commands, no placeholders, no `...`, no angle-bracket placeholders: PASS. No `$ ` command line has `...` or a `<word>` placeholder. Two notes: manager report :9 has `...` twice, but in Task prose quoting the sentence, not in a command; Block 4 (:90) uses the shell redirect `>`, which is literal syntax, not a placeholder.
- At most 25 command blocks: PASS (22).
- No pasted `git status`, `--name-only` only as `| wc -l` with output 1, no `ls` of the evidence dir: PASS (:233 to :234; the output 1 matches my run).
- No evidence-dir path, no email: PASS (both counts 0).
- **No person's name anywhere in the report: FAIL.** Manager report :214 (inside Block 20's pasted entry text, the Status line) has the name "Amear" twice: "changeable by Amear. Not Amear's ruling." The manager admits this at :38 ("Only one name appears in this report: the decision owner"). Graded against the rule as written, the rule is broken. My reasoning is that the same brief also requires "the full final entry text", and the entry's Status line contains that name. The two rules cannot both be met. Only a redaction, or dropping the Status line, could satisfy both, and either one would break "full output". The defect therefore comes from the brief, but it is still a break of the rule as written.
- `T[B]D` absent: PASS (0).
- Every cited line number correct: PASS. I checked :2417, :2418, :2420, :2422, :2424 to :2426, :2428, :2430, :2432, :2434 against my (h) structure output; MANIFEST :471 (the DECISIONS.md amendment row for D-2026-11-13-B), :472 to :473 and :474 against MANIFEST.md tail; topology :58, :61, :99, :100, :106, :198 and spec :196, :212 against my (d) and (e) outputs; and rubric :133, :134, :138, :145 above.
- Required content: the two cp commands (:47) are present; the full diffs (:64 to :76, :82 to :84) are present and reproduce; wc -l of both files (:53 to :58) is present; the 1 to 2416 cmp (:90 to :91) is present; the nine quote byte checks (Blocks 5 to 13) each output 1; the four grep -c counts on `awk 'NR>=2417'` (Blocks 14 to 17) each output 0. **"The full final entry text": not literally met.** Block 20 (:210) prints only DECISIONS.md :2417 to :2433 and leaves out :2434, the entry's S13 line. That line is shown only through a SHA-256 match against the pre-copy (Block 19, :201 to :204). The manager says this at :37 and gives the reason (the S13 sentence may appear only once). This is a second conflict inside the brief, between the S13-once rule and the full-entry rule. I record it as a deviation but do not count it as a separate break, because no report could meet both rules.
- `## Verification evidence (command output)` at :40, final line `Result: PASS` at :250: PASS.
- S13 sentence exactly once, as a standalone line at the end: PASS. Its only occurrence is :249, followed only by the Result line. Block 19 (:201) greps for a prefix of it, not the full sentence.
- Adversary's report not cited or named: PASS. :28 and :239 use only the permitted wording, and "cure-worker" has 0 hits.

### (g) The new MANIFEST row is accurate, names the report, and has no evidence-dir path: FAIL

Evidence: block B under (b). Its lines `--- evidence path / email in new MANIFEST row:` and `0`, then `--- report file referenced by row exists:` and `yes`, come from `awk 'NR==474' MANIFEST.md | /usr/bin/grep -cE ...` (the full pattern is pasted there) and `test -f`. The full row text is in the (a) diff.
The row names the report, the report exists, and the row has no evidence path or email. Its DECISION_LOG stamps 13:37:42Z (:919) and 17:02:02Z (:923) both exist. "One clause deleted in its Decision paragraph" is correct, and so is "one topology quote added to its Sources".
**Break:** MANIFEST.md :474 says "one word replaced ... in its S6 paragraph". The (a) diff at :2428 shows two words, "already uses", replaced by one word, "names". The authority row DECISION_LOG.md :923 also says "replace "already uses" with "names"". So "one word replaced" is factually wrong. The row is byte-identical to the text the brief authorised, so the manager made it exactly as specified; the error is in the briefed wording. An accurate wording would be "one phrase replaced" or "two words replaced by one". The manager report repeats the imprecision at :7 ("one word substitution"), but states it correctly at :10 ("the words "already uses for" become "names for"").

### (h) Entry structure, in order: Status, Decision, Sources, S6, Limits, S4, then the S13 line: PASS

Command: the last three lines of block F under (f), where it is pasted in full. Output of those lines:
```
--- entry structure (DECISIONS.md)
2418: ## 2026-11-13 — D-2026-11-13
2420: **Status:** Decided by master 
2422: **Decision.** Option (a) of to
2424: **Sources (quoted byte-exact).
2428: **S6 cross-block.** Block 3 br
2430: **Limits.** No code, no spec b
2432: **S4 timing.** Written 2026-11
S13 line number in entry: 18 (offset from 2417; file total     2434)
```
Offset 18 from 2417 is :2434, the last line of the file. The order is Status, Decision, Sources, S6, Limits, S4, then the S13 line, and the S13 line occurs once in the entry range.

## Overall

(a) PASS, (b) PASS, (c) PASS, (d) PASS, (e) PASS, (f) FAIL, (g) FAIL, (h) PASS.

Defects:
1. docs/reports/2026-11-13-open-a1-cure-manager.md:214. A person's name ("Amear", twice, in the pasted Status line of the entry) breaks the rule "no person's name anywhere in the report" as written. It is forced by the conflicting requirement to paste the full final entry text.
2. MANIFEST.md:474. "one word replaced" is inaccurate, because two words ("already uses") were replaced by one ("names"). The wording is byte-identical to the briefed row, so the defect is in the authorised text, not in how the manager carried it out. The same imprecision appears at manager report :7.
Deviation recorded but not graded as a separate break: manager report Block 20 (:210) leaves out entry line :2434 and substitutes a hash match (Block 19). This is forced by the S13-once rule.
Out of scope, observed only: the working-tree DECISIONS.md differs from HEAD before the entry. HEAD has 2324 lines, and the pre-copy's lines 1 to 2416 first differ from HEAD at line 2280. The DECISION_LOG :923 commit plan (HEAD plus the entry range) should take this into account. Command and output:
```
echo "HEAD DECISIONS lines: $(git show HEAD:DECISIONS.md | wc -l)"; cmp <(git show HEAD:DECISIONS.md) <(head -n 2416 /tmp/oa1c-pre-DECISIONS.md); echo "cmp HEAD vs pre 1-2416 exit=$?"
HEAD DECISIONS lines:     2324
/dev/fd/63 /dev/fd/62 differ: char 414862, line 2280
cmp HEAD vs pre 1-2416 exit=1
```
I did not investigate this further. It is outside this unit's diff, which is taken against the pre-copies.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
Result: FAIL
