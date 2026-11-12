# ADVERSARIAL worker 1 — unit 2026-11-12-mffu-prepurchase-filing-resume (Unit 2R)

## Task

Mode: ADVERSARIAL. Read-only, except for this file. Baseline main = ee54344.
Artifact: `docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md` (475 lines). Pre-edit copy: `/tmp/2026-11-12-mffu-prepurchase-filing-manager.preedit.md`. Input: `docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md`. Findings to be cured: `docs/reports/2026-11-12-mffu-prepurchase-filing-worker2.md`, "## Findings" (1 MAJOR, 2 MINOR).
Criteria: S1, S2, S8, S13, F4 (FROZEN), plus the master's brief for this unit. The brief says to fix the three findings by the smallest edit, to change no other byte except the "(pending worker2)" lines, to keep Q2's text, to keep the Questions section free of any recommendation, and to keep the S13 sentence once, as the last line.

Process note: the pre-edit copy already contains all three fixes. This unit's only edits are the two pointer lines (Check 1). So the fix text was written by the manager that did not return, and this report is the first adversarial check of it.

## Checks run

### Check 1 — diff against the pre-edit copy, and sha256 of both

```
$ cd /Volumes/Sensidine/Praxis.build; A=docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md; P=/tmp/2026-11-12-mffu-prepurchase-filing-manager.preedit.md; wc -l "$A" "$P"; shasum -a 256 "$A" "$P"; diff "$P" "$A"; echo "diff exit=$?"
     475 docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md
     475 /tmp/2026-11-12-mffu-prepurchase-filing-manager.preedit.md
     950 total
5db6955831dd8616cbb55b74ebfa1a61a03d606fdfb177c9c351368f104ffd7e  docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md
61e980e033014b226f69d9b80570b6405940b1fcf9e9c0684359599dac977840  /tmp/2026-11-12-mffu-prepurchase-filing-manager.preedit.md
150c150
< (pending worker2)
---
> (manager did not return; completed by unit 2026-11-12-mffu-prepurchase-filing-resume — see docs/reports/2026-11-12-mffu-prepurchase-filing-resume-manager.md)
158c158
< (pending worker2)
---
> (manager did not return; completed by unit 2026-11-12-mffu-prepurchase-filing-resume — see docs/reports/2026-11-12-mffu-prepurchase-filing-resume-manager.md)
diff exit=1
```

Two lines changed (:150 and :158). Both were "(pending worker2)" lines. No other byte changed. No finding.

### Check 2 — are worker2's three findings cured?

Where each finding now sits:

```
$ A=docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md; grep -n -F 'bear on that link' "$A" | cut -c1-12; grep -n -F 'Account.Name' "$A" | cut -c1-12
80:Graded agai
92:1. Consumer
93:   What R2 p
148:3. MINOR, "
308:100:					&
310:639:				|
442:100: 					
444:639: 				
448:$ grep -c "
```

**2a. Q1 bullet vs input :23, byte-compared by script (:460).**

```
$ I=docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md; A=docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md; L=$(sed -n '23p' "$I"); echo "input23 len=${#L}"; S=$(sed -n '460p' "$A" | sed -e 's/^- The earlier reply, input :23, in full: "//' -e 's/"$//'); echo "artifact quote len=${#S}"; python3 -I -c 'import sys;a=open(sys.argv[1],"rb").read().split(b"\n")[22];b=open(sys.argv[2],"rb").read().split(b"\n")[459];print("input23 repr:",a[:12]);print("in artifact460 as substring:", a in b); s=a.lstrip(); print("stripped input23 in artifact460:", s in b); pre=b"- The earlier reply, input :23, in full: \""; print("exact form:", b==pre+s+b"\"")' "$I" "$A"
input23 len=279
artifact quote len=278
input23 repr: b' I cannot co'
in artifact460 as substring: False
stripped input23 in artifact460: True
exact form: True
```

Input :23 has one leading space, which is indentation inside the input's text block. Without that space, :460 is exactly the prefix, then the line, then a closing quote mark. The quote now includes ", as the policy distinguishes between holding within a session versus holding through the daily close." **Finding 1 is cured.**

**2b. G9 sentence (:80).**

```
$ git grep -n -F '(iv) "Overnight" in the FAQs' bf6fcc7 -- docs/specs
bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md:25:- (iv) "Overnight" in the FAQs = across the daily session close (the FAQ's own gloss, INFERRED).
```

```
$ A=docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md; python3 -I -c '
import sys,re
a=open(sys.argv[1]).read().split("\n")[79]
q1="(iv) \"Overnight\" in the FAQs = across the daily session close (the FAQ'"'"'s own gloss, INFERRED)."
print("design25 quote in :80:", q1 in a)
inp=open(sys.argv[2]).read().split("\n")[22]
q2="the policy distinguishes between holding within a session versus holding through the daily close"
print("R1 clause in input:23:", q2 in inp, "| in :80:", q2 in a)
' "$A" docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md
design25 quote in :80: True
R1 clause in input:23: True | in :80: True
```

Both sources the sentence names are quoted accurately. The source labels are also right: R1 is input :16-27 by the artifact's own definition at :39, and :23 sits under R1's "4. Overnight positions". The other timing facts on :80 hold too. "Three minutes earlier" matches 22:38:25Z to 22:41:33Z. "49 seconds" matches 22:40:44Z to 22:41:33Z (input :14, :29, :30).

The break: the sentence makes a count claim, and the line just above it contradicts that count.

```
$ A=docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md; sed -n '79p' "$A" | grep -o -F 'which an 18:05→08:25 hold meets'; sed -n '80p' "$A" | grep -o -E 'Two texts on disk bear on that link: [^(]*'; sed -n '80p' "$A" | grep -o -F 'Neither says in terms that such a hold is not overnight.'
which an 18:05→08:25 hold meets
Two texts on disk bear on that link: design :25's gloss, which the design itself grades INFERRED 
Neither says in terms that such a hold is not overnight.
```

```
$ git show bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md | sed -n '110p' | grep -o -F '"Holding overnight will breach" is glossed by the FAQ as "closed before the daily session close", which an 18:05→08:25 hold meets;'
"Holding overnight will breach" is glossed by the FAQ as "closed before the daily session close", which an 18:05→08:25 hold meets;
```

Design :110, which the artifact quotes in full at :79, also bears on the link. It applies the FAQ gloss to an evening hold and says the hold meets it. The investigation (HEAD) at :1379 also carries the FAQ's own OBSERVED text, which is what design :25 glosses:

```
$ git show HEAD:docs/reports/2026-11-11-mffu-connection-investigation.md | sed -n '1379p' | cut -c1-200
| R2 | Holding overnight breaches the account | **OBSERVED** (MFFU page), plan-specific wording | Rapid FAQ: "All positions must be closed before the daily session close. Holding overnight will
```

So "Two texts on disk bear on that link" is a new count claim. No search is pasted for it, and :79 refutes it. The sentence was edited to cure worker2 finding 2, which said the line understated support for one answer to Q1. It still understates that support, in the same direction, and it now does so with a count that is false. The brief said "with no new claim", and this is one. **Finding 2 is not cured** (Finding 1 below).

**2c. S6 item 1, `Account.Name` (:93).**

```
$ A=docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md; sed -n '93p' "$A" | grep -o -F '`Account.Name` is on 7 lines, by `grep -c`'
`Account.Name` is on 7 lines, by `grep -c`
```

The artifact's pasted command (:448-449):
```
$ grep -c "Account.Name" ninjascript/PraxisSignalConsumer.cs
7
```

Reality, re-run in this session:
```
$ grep -c "Account.Name" ninjascript/PraxisSignalConsumer.cs; grep -oF "Account.Name" ninjascript/PraxisSignalConsumer.cs | wc -l; grep -cF "Account.Name" ninjascript/PraxisSignalConsumer.cs; grep -c -i "accounttype" ninjascript/PraxisSignalConsumer.cs
7
       8
7
0
$ grep -n -F "Account.Name" ninjascript/PraxisSignalConsumer.cs | cut -c1-80
99:					&& !string.IsNullOrEmpty(Account.Name)
100:					&& Account.Name.StartsWith(RequiredAccountPrefix, StringComparison.OrdinalIgnoreCase);
104:					string acct = (Account == null || Account.Name == null) ? "<null>" : Account.Name;
181:			Print(LogPrefix + " STARTED on account '" + Account.Name + "', dir '" + SignalsPath + "', "
183:			Log(LogPrefix + " consumer started (sim account " + Account.Name + ").", LogLevel.Information);
639:				|| !Account.Name.StartsWith(RequiredAccountPrefix, StringComparison.OrdinalIgnoreCase))
666:					+ " acct=" + Account.Name);
```

The prose "is on 7 lines, by `grep -c`" matches the paste (7) and matches reality (7 lines, 8 occurrences; line 104 holds two). **Finding 3 is cured.**

Independent judgment on the brief's "say 7 lines, 8 occurrences". The brief is not met literally: the artifact never states 8 occurrences. That is not an S1 or S2 defect. The artifact claims only what its paste shows, and it claims nothing higher. Writing "8 occurrences" without also pasting a `grep -o | wc -l` run would itself have breached S1, because the pasted command cannot show 8. The brief's own condition, "matching the pasted command", is met only by the 7-lines wording. Graded MINOR, as a brief deviation and not a rubric breach (Finding 3 below). This unit's no-other-byte rule now blocks the fix inside this unit. If the master wants "8 occurrences" stated, it needs a new paste.

### Check 3 — pointer lines

```
$ A=docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md; grep -c -F '(pending worker2)' "$A"; echo "exit $?"; T='(manager did not return; completed by unit 2026-11-12-mffu-prepurchase-filing-resume — see docs/reports/2026-11-12-mffu-prepurchase-filing-resume-manager.md)'; grep -n -x -F "$T" "$A"; grep -n -F 'prepurchase-filing-resume-manager.md' "$A" | cut -c1-12; grep -n -F '(pending worker2)' /tmp/2026-11-12-mffu-prepurchase-filing-manager.preedit.md; ls -la docs/reports/2026-11-12-mffu-prepurchase-filing-resume-manager.md 2>&1
0
exit 1
150:(manager did not return; completed by unit 2026-11-12-mffu-prepurchase-filing-resume — see docs/reports/2026-11-12-mffu-prepurchase-filing-resume-manager.md)
158:(manager did not return; completed by unit 2026-11-12-mffu-prepurchase-filing-resume — see docs/reports/2026-11-12-mffu-prepurchase-filing-resume-manager.md)
150:(manager
158:(manager
150:(pending worker2)
158:(pending worker2)
ls: docs/reports/2026-11-12-mffu-prepurchase-filing-resume-manager.md: No such file or directory
```

Each of the two former "(pending worker2)" lines is now exactly one line, a whole-line match, with the target path. The count of "(pending worker2)" is 0. The pointer target does not exist yet. That is expected mid-unit, but the pointer dangles until the resume manager writes that file. This is noted for the manager, not graded.

### Check 4 — S13 once, as the last line

```
$ A=docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md; S=$(grep -o -E 'Fills are optimistic[^|`"]*assumed\.' specs/SPEC_RUBRIC.md | head -1); echo "S length ${#S}; first 20: ${S:0:20}"; echo "full-sentence count: $(grep -c -F "$S" "$A")"; echo "line(s): $(grep -n -F "$S" "$A" | cut -d: -f1)"; echo "total lines: $(wc -l < "$A" | tr -d ' ')"; [ "$(tail -n 1 "$A")" = "$S" ] && echo "last line == S exactly"
S length 90; first 20: Fills are optimistic
full-sentence count: 1
line(s): 475
total lines: 475
last line == S exactly
```

Pass. The two other partial hits, at :141 and :242, are 20-character fragments inside pasted commands and outputs. Neither is the full sentence.

### Check 5 — email addresses and the rep's name

```
$ A=docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md; RE='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'; grep -cE "$RE" "$A"; printf '%s@%s.%s\n' user example org | grep -cE "$RE"; grep -c '@' "$A"; grep -n '@' "$A" | cut -c1-160
0
1
2
210:$ grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' $F
212:$ printf '%s@%s.%s\n' a b com | grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
```

Email addresses: 0, and the runtime control hits 1. The only two "@" characters are inside the artifact's own regex commands.

Rep name. The input replaces the rep with `[rep]` (input :3, :14, :30). The only rep first name recoverable on disk is the token embedded in the staged MFFU evidence filename. Prior units (correction-1 worker3 :13, worker4 :14) and this artifact (:214) used that token. I built it at runtime and did not print it:

```
$ A=docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md; TOK=$(ls docs/reports/evidence | grep mffu | head -1 | sed 's/.*mffu-//; s/-reply.*//'); echo "len ${#TOK}"; echo "artifact: $(grep -ci -- "$TOK" "$A")"; echo "control: $(printf 'x%sx\n' "$TOK" | grep -ci -- "$TOK")"; echo "input: $(grep -ci -- "$TOK" docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md)"; for f in docs/reports/2026-11-12-mffu-prepurchase-filing-worker1.md docs/reports/2026-11-12-mffu-prepurchase-filing-worker2.md docs/reports/2026-11-11-mffu-connection-investigation.md; do echo "$f: $(grep -ci -- "$TOK" "$f")"; done; echo "[rep] in artifact: $(grep -c -F '[rep]' "$A")"
len 4
artifact: 0
control: 1
input: 0
docs/reports/2026-11-12-mffu-prepurchase-filing-worker1.md: 0
docs/reports/2026-11-12-mffu-prepurchase-filing-worker2.md: 0
docs/reports/2026-11-11-mffu-connection-investigation.md: 0
[rep] in artifact: 6
```

I also listed every distinct capitalized word in the artifact (`grep -o -E '\b[A-Z][a-z]{2,}\b' | sort | uniq -c`). The only personal name in that list is the trader's own name. The 2026-11-11 thread's rep name is not on disk; the input shows only `[rep]`. Pass.

### Check 6 — Q1 and Q2 carry no recommendation; Q2's text

```
$ A=docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md; Q2='Q2. Should F4'"'"'s bar change, given that MFFU support says it will not approve a specific configuration in writing?'; grep -n -x -F "$Q2" "$A"; echo "--- leaning words in Q section"; sed -n '452,474p' "$A" | grep -n -i -E 'recommend|suggest|should (be|we|Amear)|propose|advise|lean|we think|likely|probably|best|prefer|answer is|closes OPEN-1|yes|no,' | cut -c1-200
465:Q2. Should F4's bar change, given that MFFU support says it will not approve a specific configuration in writing?
--- leaning words in Q section
7:- OPEN-1, R6 design :110 (`bf6fcc7`): "no MFFU text says it in terms of an evening entry. A written MFFU answer is needed before any funded use."
```
(The one hit is "answer is" inside a quote from the design. It is not a recommendation.)

Every quote in the Questions section was verified against its source:
```
$ A=docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md; python3 -I - "$A" docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md specs/SPEC_RUBRIC.md <<'EOF'
import sys,re
art=open(sys.argv[1]).read().split("\n"); inp=open(sys.argv[2]).read().split("\n"); rub=open(sys.argv[3]).read().split("\n")
checks=[(39,'A trade opened after 6:00 PM and closed before 9:30 AM the following day remains within the permitted trading window and does not cross the daily close.'),
(33,'a specific technical configuration (such as NinjaTrader → n8n webhook → file‑based order execution) cannot be approved in writing from the available information.'),
(35,'the policy does not confirm whether unattended execution without supervision is allowed or required.'),
(17,'Your described setup—NinjaTrader sending signals to n8n for risk checks, then placing bracket orders—falls within general automation permission. However, I cannot issue written approval for your specific configuration or guarantee that unattended execution is allowed without supervision. For an official compliance decision on your exact setup, our team can review the details you\'ve provided.'),
(46,'will not approve'),(43,'automated assistant replies')]
for n,q in checks: print("input",n,q in inp[n-1])
print("rubric 49-50 F4:", 'Written confirmation from MFFU that this specific automation pattern is permitted on a funded account.' in " ".join(l.strip() for l in rub[48:50]))
print("rubric 56:", rub[55][:200])
print("rubric 49:", rub[48][:200]); print("rubric 50:", rub[49][:200])
EOF
input 39 True
input 33 True
input 35 True
input 17 True
input 46 True
input 43 True
rubric 49-50 F4: True
rubric 56: **Owner.** Amear. Not a build task — an email.
rubric 49: **Criterion.** Written confirmation from MFFU that this specific automation
rubric 50: pattern is permitted on a funded account.
$ git show bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md | sed -n '110p' | grep -c -F 'no MFFU text says it in terms of an evening entry. A written MFFU answer is needed before any funded use.'
1
$ sed -n '2131p' DECISIONS.md | grep -o -F -e 'evening entries stand on MFFU'"'"'s written answer' -e 'V3 does not close OPEN-1. R6 stays open pending MFFU'"'"'s written answer to OPEN-1'
evening entries stand on MFFU's written answer
V3 does not close OPEN-1. R6 stays open pending MFFU's written answer to OPEN-1
```

Q2's line is exact (:465). Neither question carries a recommendation, and neither is answered. The break: Q1's OPEN-1 bullet (:458) quotes design :110 starting mid-sentence, after a semicolon, with no ellipsis. It drops the part of the same line that says the evening hold meets the FAQ gloss:

```
$ sed -n '458p' docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md | grep -c -F '18:05'
0
```
(The dropped text is shown in the design :110 `git show bf6fcc7` output in Check 2b.) This has the same structure as worker2 finding 1: a truncated quote with no marker, where the dropped part supports one answer. Here the dropped clause is the design's own application of the :25 gloss, which Q1 does carry at :459. So the effect is smaller. Graded MINOR (Finding 2 below). The text predates this unit; the pre-edit copy has the same Questions section:
```
$ diff <(sed -n '450,475p' /tmp/2026-11-12-mffu-prepurchase-filing-manager.preedit.md) <(sed -n '450,475p' docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md) && echo "Q section identical to preedit"
Q section identical to preedit
```

### Check 7 — nothing claims F4 MET or unfrozen

```
$ A=docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md; grep -n -i -E 'F4[^.]{0,60}\b(MET|unfrozen|satisf|thaw|cleared|passes)\b' "$A" | cut -c1-160; echo "--- unfroz/thaw anywhere"; grep -n -i -E 'unfroz|thaw' "$A" | cut -c1-200; echo "--- F4 is met (positive)"; grep -n -E 'F4 (is |now )?MET|F4: MET|F4 .{0,20}= MET' "$A" | cut -c1-200
13:- F4 (FROZEN; Owner Amear): "Written confirmation from MFFU that this specific automation pattern is permitted on a funded account." Graded in G-F4: stays FROZEN / NOT MET.
97:5. Rubric F4: G-F4, NOT MET.
338:$ sed -n 2172p DECISIONS.md | grep -o 'Rubric F2 (Rule F2-1 approved; F2 FROZEN). Rubric F4 (FROZEN / NOT MET).'
339:Rubric F2 (Rule F2-1 approved; F2 FROZEN). Rubric F4 (FROZEN / NOT MET).
--- unfroz/thaw anywhere
--- F4 is met (positive)
```

Every F4 hit reads NOT MET or FROZEN. G-F4 says "Grade: NOT MET. F4 stays FROZEN; Owner Amear." Pass.

## Findings

1. MAJOR (S1 / S2 drift; brief "no new claim"; worker2 finding 2 not cured), artifact :80. "Two texts on disk bear on that link: design :25's gloss ... and R1 point 4's clause ..." is a new count claim with no pasted search. The artifact's own :79 refutes it: :79 quotes design :110 in full, including "which an 18:05→08:25 hold meets". That text bears on the link directly: it applies the FAQ gloss to the evening hold and says the hold meets it. The FAQ's own OBSERVED text (investigation :1379) is a further source. Worker2 finding 2 said this sentence understated the support for one answer to Q1. The edited sentence still does, in the same direction, and it now does so with a false count. I grade it MAJOR because the edit was meant to cure exactly this defect, and the brief's "no new claim" was a stated condition. If the manager reads it only as the same incompleteness worker2 graded, it falls to MINOR.
2. MINOR (S8 drift; quote truncation with no marker), artifact :458. Q1's OPEN-1 bullet quotes design :110 from mid-sentence. It drops '"Holding overnight will breach" is glossed by the FAQ as "closed before the daily session close", which an 18:05→08:25 hold meets;', which is the part that supports reading the hold as not overnight. It has the same structure as worker2 finding 1. It is mitigated because Q1 carries design :25's gloss at :459. The text predates this unit, and this unit's no-other-byte rule put it out of scope here.
3. MINOR (brief deviation, not a rubric breach), artifact :93. The brief asked for "7 lines, 8 occurrences". The artifact says only "is on 7 lines, by `grep -c`". That matches its paste (:448-449) and matches reality (7 lines, 8 occurrences, re-run above). It is S1-sound. Adding "8 occurrences" would need a new pasted `grep -oF "Account.Name" ninjascript/PraxisSignalConsumer.cs | wc -l`. Worker2 finding 3 itself is cured.

Checked with no break: the diff touches only the two pointer lines (Check 1). Finding 1 is cured byte for byte (2a). There are 0 "(pending worker2)" lines, and both pointers are exact single lines (Check 3; their target file does not exist yet). The S13 sentence appears once, as line 475 of 475 (Check 4). Emails: 0, with the control at 1. The rep token count is 0, with the control at 1 (Check 5). Q2's text is exact, and no question is answered (Check 6). F4 is never claimed MET or unfrozen (Check 7).

## Result: FAIL

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
