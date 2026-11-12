# Unit 2026-11-12-mffu-prepurchase-filing, worker 2 (ADVERSARIAL)

## Task

Adversarial re-check of `docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md` (471 lines) at main @ ee54344, scoped to: (A) the Q2 wording note and the absence of leaning in Q1/Q2 (S8); (B) the S1 paste of DECISION_LOG.md:849; (C) the report ending with `## Questions for Amear (his, not D2 items)` and the S13 sentence as the single final line; (D) a regression scan of the E9-citing prose, email addresses, and the forbidden word. Input graded by the artifact: `docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md`. Read-only. Nothing staged, nothing edited except this file.

## Checks run

### A1. Input lines cited by Q1/Q2, and where "will not approve" occurs in the input

```text
$ I=docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md; for n in 17 23 33 35 39 43 44 45 46; do echo "== :$n"; sed -n "${n}p" $I | sed -E 's/[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+/[ADDR]/g'; done; echo; grep -c 'will not approve' $I; grep -n 'will not approve' $I | cut -c1-12; grep -cF 'cannot be approved in writing from the available information' $I; grep -cF 'our team can review the details' $I
== :17
 Automated strategies are permitted on evaluation and funded accounts, subject to Fair Play rules: strategies must be tailored to your own settings, must not exploit favorable simulated fills, and high-frequency trading is prohibited. Your described setup—NinjaTrader sending signals to n8n for risk checks, then placing bracket orders—falls within general automation permission. However, I cannot issue written approval for your specific configuration or guarantee that unattended execution is allowed without supervision. For an official compliance decision on your exact setup, our team can review the details you've provided.
== :23
 I cannot confirm the exact definition of "overnight" for a position opened after 6:00 PM ET and closed before 9:30 AM ET the next day. This requires clarification from our team, as the policy distinguishes between holding within a session versus holding through the daily close.
== :33
 Automated strategies are permitted on MFFU accounts, including Evaluation, Sim Funded and Live, provided they follow the applicable rules. High‑frequency trading is prohibited, and strategies must not attempt to exploit favorable simulated fills. However, a specific technical configuration (such as NinjaTrader → n8n webhook → file‑based order execution) cannot be approved in writing from the available information. Automation is allowed in principle, but individual setups are not automatically approved.
== :35
 Automation is permitted, but the policy does not confirm whether unattended execution without supervision is allowed or required. The absence of a supervision rule does not establish permission for a specific unattended configuration.
== :39
 MFFU trading hours run from 6:00 PM to 4:10 PM Eastern Time. Positions must be closed by the 4:10 PM cutoff. A trade opened after 6:00 PM and closed before 9:30 AM the following day remains within the permitted trading window and does not cross the daily close.
== :43
- Both replies came within about a minute of the outgoing mail; they read as automated assistant replies (INFERRED, not confirmed).
== :44
- R6 OPEN-1 (evening entry vs overnight): answered in writing by MFFU support (message 4, point 4): within the permitted window, does not cross the daily close. Whether an automated-assistant reply counts as MFFU's written answer for the rubric is Amear's call.
== :45
- T1 news: message 2, point 5 answers it per plan (2-minute window on Rapid/Pro Sim Funded only; Builder and evaluations unrestricted).
== :46
- F4: still NOT MET. MFFU support states it will not approve a specific configuration in writing, and does not confirm unattended execution. Whether F4's bar can be met through email support, or must be revised, is Amear's (rubric is his).

1
46:- F4: sti
1
1
```

Artifact Q2 (artifact :461-469, read with `sed -n '/^## Questions for Amear/,$p'`): Q2 text at :461 is exactly the brief's mandated text. The wording note at :464 says "will not approve" is the channel's reading (input :46) and quotes MFFU's own text from input :33 and the team-review offer at input :17. Both quoted fragments match the input (counts 1 and 1 above), and "will not approve" occurs only at input :46. Q2's facts quote :17, :33, :35 and the rubric owner line. None of them carries a recommendation.

### A2. The Q1 truncation (artifact :456), set against the full clause the artifact quotes elsewhere

```text
$ grep -n -F 'holding within a session versus holding through the daily close' $A | cut -c1-16
58:Establishes: 
175:23:  I canno
== line 58:
Establishes: nothing about the definition. "I cannot confirm the exact definition of "overnight" for a position opened after 6:00 PM ET and closed before 9:30 AM ET the next day. This requires clarification from our team". It adds that "the policy distinguishes between holding within a session versus holding through the daily close". Bearing: G9 and Q1.
== line 456:
- The earlier reply, input :23: "I cannot confirm the exact definition of "overnight" for a position opened after 6:00 PM ET and closed before 9:30 AM ET the next day. This requires clarification from our team".
```

Artifact :80 (G9, an edited line) says: 'Reading "does not cross the daily close" as "not overnight" needs design :25's gloss, which the design itself grades INFERRED'.

### B. DECISION_LOG.md:849 paste in E9, re-run

```text
$ grep -nF 'a channel-reported instruction is recorded, not proven given' $A | cut -c1-200
16:- S5: no approval is inferred. Amear's chat words "yep" and "go" (input :8-9) are REPORTED BY the channel; the ledger record is DECISION_LOG.md:849 (E9), which itself says "a channel-reported instr
121:$ grep -v '^\$ ' $R | grep -c -F 'a channel-reported instruction is recorded, not proven given'
410:$ sed -n 849p DECISION_LOG.md | grep -o -E '^- \[2026-11-12T02:41:00Z\] WHO: amear|a channel-reported instruction is recorded, not proven given'
412:a channel-reported instruction is recorded, not proven given
```

Re-run of the E9 command (artifact :410-412):

```text
$ sed -n 849p DECISION_LOG.md | grep -o -E '^- \[2026-11-12T02:41:00Z\] WHO: amear|a channel-reported instruction is recorded, not proven given'
- [2026-11-12T02:41:00Z] WHO: amear
a channel-reported instruction is recorded, not proven given
```

This is byte-for-byte the same as the artifact's paste at :411-412.

### C. Structure: last heading and the S13 sentence

The sentence is pulled at runtime with a fragment pattern, and is not printed:

```text
$ S=$(grep -o -E 'Fills are optimistic[^|`"]*assumed\.' specs/SPEC_RUBRIC.md | head -1); echo "len=${#S}"; echo "count=$(grep -cF -- "$S" $A)"; echo "on lines: $(grep -nF -- "$S" $A | cut -d: -f1 | tr '\n' ' ')"; echo "total=$(wc -l < $A)"; echo "last line exact match: $(tail -n1 $A | grep -cxF -- "$S")"
len=90
count=1
on lines: 471 
total=     471
last line exact match: 1
$ grep -n '^## ' $A | tail -1 ; awk 'NR>448 && /^#/' $A | head
448:## Questions for Amear (his, not D2 items)
```

The last section is `## Questions for Amear (his, not D2 items)` (:448), with no heading after it. The S13 sentence occurs once, as the whole of line 471, which is the last line.

### D1. Every E9-citing prose line, with the E9 commands re-run

```text
$ grep -n 'E9' $A | cut -c1-260   (prose hits: :14, :16, :30, :32, :39, :80, :82, :93, :104-106, :457, :458)
$ sed -n 849p DECISION_LOG.md | grep -o -E '...'   (see B)
$ wc -l specs/SPEC_RUBRIC.md; tail -c 1 $F | od -c | head -1; awk 'NR>=38 && NR<=39' $F | grep -c -i overnight; awk 'NR==1444 {print NR": "$0}' $I
     461 specs/SPEC_RUBRIC.md
0000000   \n                                                            
0
1444: 4. Does a position opened after 6:00 PM ET and closed before 9:30 AM ET the next day count as holding overnight? It is never held past your 4:10 PM ET close.
$ awk 'NR>=2101 && /^## /{print NR": "substr($0,1,60)}' DECISIONS.md | head -2; sed -n 2131p DECISIONS.md | grep -o 'V3 as clarified by V5 — overnight holding.'
2101: ## 2026-11-11 — D-2026-11-11-A: Amear's rulings V1–V7 (C
2176: ## 2026-11-11 — D-2026-11-11-B: VM handoff §1 limit 9 lif
V3 as clarified by V5 — overnight holding.
$ grep -c -i accounttype ninjascript/PraxisSignalConsumer.cs; grep -c "Account.Name" ninjascript/PraxisSignalConsumer.cs
0
7
$ sed -n 2131p DECISIONS.md | grep -o -F -e "evening entries stand on MFFU's written answer" -e "V3 does not close OPEN-1. R6 stays open pending MFFU's written answer to OPEN-1"
evening entries stand on MFFU's written answer
V3 does not close OPEN-1. R6 stays open pending MFFU's written answer to OPEN-1
```

These match the artifact's E9 paste. The two quotes at :457 are pasted in the E2/E3 block (:269-271), which Q1's facts header cites. Timing at :39: 22:37:27Z to 22:38:25Z is 58 s, and 22:40:44Z to 22:41:33Z is 49 s. Both are correct, and the four timestamps are in E9's message list.

The "occurs 7 times" claim at :93, checked against occurrences:

```text
$ C=ninjascript/PraxisSignalConsumer.cs; echo "lines(regex)=$(grep -c 'Account.Name' $C) lines(fixed)=$(grep -cF 'Account.Name' $C) occurrences(fixed)=$(grep -oF 'Account.Name' $C | wc -l | tr -d ' ')"
lines(regex)=7 lines(fixed)=7 occurrences(fixed)=8
```

### D2. Email addresses (regex control assembled by printf) and the forbidden word (pattern assembled by printf)

```text
$ P=$(printf '%s%s%s' 'probe.user' '@' 'example.org'); RX='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
$ printf '%s\n' "$P" | grep -cE "$RX"; grep -cE "$RX" $A
1
0
$ W=$(printf '%s%s' ver dict); echo "forbidden-word hits: $(grep -ci "$W" $A)"; echo "control: $(printf 'x %s y\n' "$W" | grep -ci "$W")"
forbidden-word hits: 0
control: 1
```

## Findings

1. MAJOR (S8 / brief item A(iii), Q1 leans): artifact :456. Q1's fact bullet quotes input :23 but closes the quotation at "from our team". It drops the rest of the same sentence: ", as the policy distinguishes between holding within a session versus holding through the daily close." The quote has no ellipsis. That dropped clause is the only text from MFFU support on disk that ties "overnight" to "the daily close". It is therefore the one fact that would support reading R2 point 4 ("does not cross the daily close", input :39) as closing OPEN-1. Every other fact in Q1's list bears against closure: the design gloss is INFERRED (:455), R1 could not confirm (:456), DECISIONS says V3 does not close OPEN-1 (:457), the word "overnight" is absent (:458), and the reply may be automated (:459). The artifact knows the clause bears on Q1: at :58 it quotes the clause and writes "Bearing: G9 and Q1". Yet the clause is missing from Q1 itself, so Q1 as written leans toward "not closed". Evidence: A2. Brief item A(iii) requires that no leaning be attached to Q1. (Graded MAJOR because the brief makes leaning a stated condition. If the manager takes the narrower reading of S8, where only an answer breaches it, this falls to MINOR. That call is the manager's.)
2. MINOR (S1/S8 drift, edited line): artifact :80. "Reading 'does not cross the daily close' as 'not overnight' needs design :25's gloss, which the design itself grades INFERRED." This is incomplete. MFFU support's own R1 text (input :23, quoted by the artifact at :58) supplies the within-session versus through-the-daily-close distinction. So the reading does not rest only on the design's INFERRED gloss. As written, the sentence understates the support for one answer to Q1. Evidence: A1 (:23) and A2.
3. MINOR (S1, E9 regression): artifact :93. The text says "`Account.Name` occurs 7 times". The pasted command (`grep -c`) counts lines, not occurrences. The consumer has 8 occurrences on 7 lines. The paste is accurate, but the prose misdescribes it. Evidence: D1, last block.

Checked with no break: Q2 keeps the mandated text exactly. Its wording note says plainly that "will not approve" is the channel's reading (input :46, the only place it occurs) and quotes MFFU's actual words (:33) and the team-review offer (:17), both exact. Q2 carries no recommendation. DECISION_LOG.md:849 is pasted in E9, and the re-run output is identical. The report ends with the Questions section, and the S13 sentence is the single final line (count 1, line 471 of 471). Every other E9-citing prose fact (:16, :30, :32, :39, :82, :457, :458) is in E9 or in the block cited for it. Email addresses: 0, with the control at 1. The forbidden word: 0, with the control at 1.

## Result: FAIL

One MAJOR (finding 1, artifact :456) and two MINOR (findings 2 and 3, artifact :80 and :93).

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
