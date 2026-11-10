# 2026-11-10-f4-grading, worker 4 (ADVERSARIAL)

**Task.** Attack the scoped parts of docs/reports/2026-11-10-f4-grading-manager.md: Element table rows 2, 4, 13, 14a, 14b; the paragraphs "Read as a whole", "CONTRADICTED", "Conditions recorded, not assessed"; the "Inquiry as sent" opening bold sentence and table.
**Mode.** ADVERSARIAL. HEAD d30ab4d. Read-only apart from this one new untracked file.
**Criterion.** Labels limited to COVERED-EXPLICITLY / COVERED-BY-INFERENCE (inference stated) / NOT ADDRESSED / CONTRADICTED, none stronger or weaker than the quoted MFFU words; no sentence grades F4 or recommends an F4 state; every quote byte-present in its cited source (allowed marked tokens only).

De-identification: no support representative's name, address or thread id appears below. The HEAD transcript is written as docs/reports/evidence/2026-10-28-mffu-[name]-reply-transcript.md.

## Process log

1. Confirmed this report path was absent (`ls: ... No such file or directory`). Found the HEAD transcript by `git ls-tree | grep reply-transcript`. Dumped the artifact (443 lines).
2. Wrote a stub report (budget rule).
3. Located the scoped sections by grep (Inquiry :36–47, table :92–112, paragraphs :114–126).
4. Printed the scoped text.
5. Printed the HEAD transcript and the R6-branch page capture (`git show r6/announcement-research:...2026-11-09-r6-mffu-news.txt`, 117 lines) at :79–105.
6. Saved HEAD copies of HANDOFF.md, ISSUE_REGISTER.md, DECISION_LOG.md, DECISIONS.md, the 2026-08-07 F4 report and voice-session-notes-3. Checked every scoped quote with `grep -F` at the cited line and anywhere in the file. Read the row labels for rows 3, 5, 6, 7 and 9, the "R2 bullet N" references, and searched HEAD for any other outgoing text.
7. Read the addendum at :636–647 (the other copy of the outgoing preview) and the R1 quote at :28.
8. Read the artifact's bullet numbering and the R1 text.
9. Checked the page's Section headings, the R1 conditions and the date at DECISION_LOG :435.

## Findings

### 1. BLOCKING: rows 2 and 14a rest on a route inference that rows 8 and 14b label NOT ADDRESSED

- **Artifact lines.** :111 (row 14a) and :99 (row 2).
- **Problem.** Row 14a states its inference as: "Algo trading is permitted on all plans" / "automated trading strategies" reaches a strategy that submits its own orders "by a non-Tradovate route". Row 2 states that "Algo trading is permitted on all plans" covers automated order submission "by any route". But the route is the element that row 8 (:105) and row 14b (:112) label NOT ADDRESSED. The only route R2 names is the Tradovate API (transcript :27–28), and no quoted MFFU word reaches a non-Tradovate route.
- **Why it matters.** Rows 2 and 14a are therefore labeled COVERED-BY-INFERENCE on the strength of an inference about an element the same report says is not addressed. That label is stronger than the quoted words support. It is the same two-labels-on-one-inference defect that the artifact's own adversary finding 2 (:161) says was fixed by splitting row 14. The split moved the platform and route into 14b, but the wording of 14a's inference brought the route back.
- **Evidence (pasted from the artifact).**
  `| 14a | ... | COVERED-BY-INFERENCE | Same inference as rows 2 and 4 (that "Algo trading is permitted on all plans" / "automated trading strategies" reaches a strategy that submits its own orders by a non-Tradovate route). |`
  `| 2 | ... | COVERED-BY-INFERENCE | ... needs the inference that "Algo trading is permitted on all plans" (R2 bullet 3, R1) includes automated order submission by any route. No MFFU line says so. |`
  `| 8 | Rithmic as the connection / order route ... | NOT ADDRESSED | No MFFU line names Rithmic. R2's only named route is Tradovate. ...`
- **Proposed fix.** Take the route out of the 2 and 14a inferences. For example: "...reaches a strategy that submits its own orders; the route is rows 8 / 14b, NOT ADDRESSED". If the label truly cannot stand without the route, relabel 2 and 14a NOT ADDRESSED.

### 2. MINOR: the "Read as a whole" paragraph brings in a whole-pattern label after saying it does not combine labels

- **Artifact line.** :114.
- **Problem.** The paragraph first says the report "does not combine the row labels into one label for the pattern". It then cites the addendum's label for "this specific automation pattern", which is the F4 criterion's own phrase (artifact :12). That label is "DOES NOT ADDRESS", which is not one of the four permitted labels.
- **Why it matters.** The quote is accurate, but placing it under "Read as a whole" offers a judgment on the F4 criterion through another document. That comes close to grading F4.
- **Evidence (pasted).**
  `[1 @:634 | anywhere:634,] w4_2026-08-07-f4-mffu-compliance-evidence.md: this specific automation pattern`
  `| F4 "this specific automation pattern" (and §3.5, specific vs general) | **DOES NOT ADDRESS** | The only specific pattern the reply names is the Tradovate API: ...`
- **Proposed fix.** Either drop the clause, or say: "the 2026-08-07 addendum (:634) records its own label for the criterion phrase; this report neither adopts nor restates it."

### 3. MINOR: row 13 never considers the "all plans" words

- **Artifact line.** :110.
- **Problem.** Row 13 quotes "now permitted" and "moving forward" (R1) and "your MyFundedFutures Tradovate evaluation and funded accounts" (R2). It leaves out the words that come closest to the element:
  - R1: "Algo trading is now permitted at MFFU moving forward on all plans" (2026-08-07 report :28).
  - R2: "Algo trading is permitted on all plans, including evaluation, simulated-funded, and live account stages." (transcript :29).
- **Why it matters.** An inference is available: "now ... moving forward on all plans" covers trading from now on in an account that already exists. The row's stated reason, "name no account", does not deal with that inference. I am not claiming the label must change. Opening date and plan are different things, and no word gives a date. The rationale is incomplete, though, so a too-weak label cannot be ruled out from the row as written.
- **Proposed fix.** Quote the "on all plans" words in the row and state why they do not reach an account opened before the change (they name plans, not accounts or opening dates). Otherwise, relabel COVERED-BY-INFERENCE with that inference stated.

### 4. MINOR: "R2 bullet 3" does not match the source's bullet markers

- **Artifact lines.** :99 and :101 (in scope). The same scheme is used at :134 and :135 (out of scope).
- **Problem.** The transcript marks four `•` bullets (:28–31). "Algo trading is permitted on all plans" is the second of them. Under the source's markers, bullet 3 is the high-frequency-trading line, and there is no bullet 5. The artifact counts the unbulleted line :27 as bullet 1 and never says so.
- **Evidence (pasted).**
  `28 • Automated trading solutions using an API are supported, ...`
  `29 • Algo trading is permitted on all plans, including evaluation, simulated-funded, and live account stages.`
  `30 • High-frequency trading is not allowed, ...`
  `31 • For live accounts, automated trading must comply with CME guidelines.`
- **Proposed fix.** Cite transcript file lines (for example "R2, transcript :29"), or define the numbering once.

## Checks that found nothing

- **Ledger quotes in the Inquiry table.** All are byte-present at the cited HEAD lines, each found only at that line: ISSUE_REGISTER :70 (three strings, including "2026-07-26 window"), DECISION_LOG :46, HANDOFF :784 (including the `**` markers), HANDOFF :764, DECISIONS :539, DECISION_LOG :435, and voice-session-notes-3 :44. The ruling date at DECISION_LOG :435 is 2026-10-28T20:54:29Z, which matches "ruled 2026-10-28".
- **Outgoing preview.** It is at transcript :16, which is fence line 2 of the fence opened at :14. It is byte-equal apart from "[rep name]".
- **Opening bold sentence of "Inquiry as sent".** I tried to break it with `git grep` at HEAD for "Two follow-ups" and "Does this specific". The only hits are transcript :16 and the 2026-08-07 addendum :642. The addendum line is the same truncated preview, ending "is f", and the addendum itself says "The full text of his questions is **not visible**." No fuller outgoing text was found. The search was not exhaustive for the initial 2026-07-26 email body.
- **Published-page quotes.** All are byte-present at the cited lines: bracket line :87 (including `●`), Section 4 heading :98 (the source line has a leading U+200B; the quoted text is a byte substring), Section 4 text :100, "automated trading strategies tailored to their own specific settings" :79, tier-1 line :88, hedging line :106. "Section 1 of the same page permits automated trading strategies" holds: Section 1 is the heading at :76, and :79 falls under it.
- **R2 quotes in rows 2, 4 and 13.** All are present in transcript :27–29. R1 "now permitted" and "moving forward" are present at 2026-08-07 report :28.
- **"Read as a whole" row list.** Rows 3, 5, 6, 7, 8, 9, 13 and 14b are all labeled NOT ADDRESSED in the table.
- **CONTRADICTED paragraph.** "No line in R1 or R2 prohibits any element" holds. The prohibitions in R1 and R2 (no HFT, no exploiting sim fills, CME compliance) are conditions, not pattern elements. Neither page line quoted under the paragraph names automation.
- **Conditions paragraph.** R1 at :44 and :46 has no HFT and requires CME compliance. R2 :30, :31 and :33 match the paraphrases. The P conditions match :85–90 and :106.
- **Grading check.** No sentence in the scoped parts grades F4 or recommends an F4 state. The only near miss is the import in finding 2.
- **Rows 4 and 14b.** Row 4's label and its stated inference are consistent with its quoted words. Row 14b's NOT ADDRESSED is consistent with "Rithmic = 0" and "NinjaTrader = 0" in R2.

## Files staged

None. This file is new and untracked, and was not added.

## Result

FAIL: one BLOCKING finding (1) and three MINOR findings (2, 3, 4).

## Correction 1 (2026-11-10, after audit fail 1)

This section was written by the manager, not by worker 4. The first audit found that this report states probe results ("The only hits are", and the other items under "Checks that found nothing") with no output. The blocks below are the **manager's** re-runs at HEAD `d30ab4d` (R6 page capture: branch `r6/announcement-research`) on 2026-11-10. Worker 4 did not run them in this form. Each block shows the literal command lines and their unedited output, apart from two filters that the command lines show. `perl -p /tmp/f4c1/redact.pl` writes `[address]` for an email address and `[patN]` for line N of `/tmp/f4c1-pat.txt` (line 1 is the trader's surname, lines 2 to 4 are the support representatives' names, line 5 is the thread id). `sed 's/-[a-z]*-reply/-[name]-reply/'` masks a representative's first name in a path. The method is in block C1-V0 of `docs/reports/2026-11-10-f4-grading-correction-1-manager.md`. This section changes no finding and no severity.

### C1-Y1. "Opening bold sentence of Inquiry as sent" and "Outgoing preview"

~~~text
$ git grep -n -i -F -e "Two follow-ups" -e "Does this specific" HEAD | cut -d: -f1-3 | sed 's/-[a-z]*-reply/-[name]-reply/'
HEAD:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md:642
HEAD:docs/reports/evidence/2026-10-28-mffu-[name]-reply-transcript.md:16
$ grep -n -F 'thanks for confirming' /tmp/f4c1/fence.txt | cut -c1-30 | perl -p /tmp/f4c1/redact.pl
2:Hi [pat2] — thanks for confir
$ git show HEAD:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | sed -n 642p | grep -o 'is f$'
is f
$ git show HEAD:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | grep -n -F 'The full text of his questions is **not visible**.' | cut -d: -f1
644
$ diff <(git show "HEAD:$T" | sed -n 16p | perl -p /tmp/f4c1/redact.pl | sed 's/\[pat2\]/[rep name]/') <(sed -n 46p docs/reports/2026-11-10-f4-grading-manager.md | grep -o 'Hi \[rep name\] — thanks[^"]*is f') && echo "transcript :16 = manager :46 preview, apart from the name token"
transcript :16 = manager :46 preview, apart from the name token
~~~

Agrees. "Two follow-ups" and "Does this specific" hit only the 2026-08-07 report :642 and transcript :16. The :642 line ends "is f". The "not visible" sentence is at :644. The last command compares transcript :16 with the preview quoted at manager :46: they are equal apart from the name token, which the command maps to "[rep name]". The preview is fence line 2 (fence file `/tmp/f4c1/fence.txt`, which equals transcript lines 15 to 39; see the manager report's Correction 1, C1-V2). The probes for other outgoing wording, with positive controls, are in C1-V40 of the same section.

### C1-Y2. "Ledger quotes in the Inquiry table"

~~~text
$ git show HEAD:HANDOFF.md | grep -c -F 'was **sent 2026-08-07**'
1
$ git show HEAD:DECISION_LOG.md | sed -n 435p | cut -c1-25
- [2026-10-28T20:54:29Z] 
~~~
~~~text
$ git show HEAD:ISSUE_REGISTER.md | grep -n -F -e 'the outreach was run to establish whether the PRAXIS automation pattern is permitted per-firm' -e 'an English inquiry' -e 'outreach sent 2026-07-26 window' | cut -d: -f1 | tr '\n' ' '; echo
70 
$ git show HEAD:DECISION_LOG.md | grep -n -F -e "the MFFU inquiry email are the TRADER'S actions to execute" -e 'by a human rep' -e 'boilerplate indicator' -e 'F4 is called "closed" in the strategy filter audit' -e 'naming NinjaTrader 8 + Rithmic. F4 stays FROZEN.**' | cut -d: -f1 | tr '\n' ' '; echo
46 177 435 801 
$ git show HEAD:HANDOFF.md | grep -n -F -e 'A follow-up email naming the actual architecture, and asking the policy' -e 'Follow-up sent 2026-08-07, awaiting reply.' | cut -d: -f1 | tr '\n' ' '; echo
764 784 
$ git show HEAD:DECISIONS.md | grep -n -F 'Does Amear send the follow-up himself' | cut -d: -f1; git show HEAD:DECISIONS.md | sed -n '2054p;2056p' | cut -c1-48
539
**The working design: option 1** (:37–41, :74, :
**Fallback: option 3, only if OPEN-T1 fails.** O
$ git show HEAD:docs/reports/2026-11-01-voice-session-notes-3.md | grep -n -F 'Whether Amear sends the follow-up himself is unconfirmed' | cut -d: -f1
44
~~~
~~~text
$ for s in 'the outreach was run to establish whether the PRAXIS automation pattern is permitted per-firm' 'an English inquiry' 'outreach sent 2026-07-26 window'; do printf 'IR %s\n' "$(git show HEAD:ISSUE_REGISTER.md | grep -n -F -- "$s" | cut -d: -f1 | tr '\n' ' ')"; done
IR 70 
IR 70 
IR 70 
$ for s in "the MFFU inquiry email are the TRADER'S actions to execute" '2026-07-26T21:20:22Z' 'by a human rep' 'boilerplate indicator' 'F4 is called "closed" in the strategy filter audit' 'naming NinjaTrader 8 + Rithmic. F4 stays FROZEN.**'; do printf 'DL %s\n' "$(git show HEAD:DECISION_LOG.md | grep -n -F -- "$s" | cut -d: -f1 | tr '\n' ' ')"; done
DL 46 
DL 177 
DL 177 
DL 435 
DL 801 
DL 435 
$ for s in 'A follow-up email naming the actual architecture, and asking the policy' 'was **sent 2026-08-07**' 'Follow-up sent 2026-08-07, awaiting reply.'; do printf 'HO %s\n' "$(git show HEAD:HANDOFF.md | grep -n -F -- "$s" | cut -d: -f1 | tr '\n' ' ')"; done
HO 784 
HO 784 
HO 764 
~~~

Agrees. Each set of strings is found only at the cited lines: the per-string loops (the last three commands) show this for each string separately: ISSUE_REGISTER.md :70; DECISION_LOG.md :46, :177, :435 and :801; HANDOFF.md :764 and :784 (with the `**` markers, count 1); DECISIONS.md :539; notes-3 :44. The DECISION_LOG.md :435 row is dated 2026-10-28T20:54:29Z.

### C1-Y3. "Published-page quotes"

~~~text
$ R=r6/announcement-research:docs/reports/evidence/2026-11-09-r6-mffu-news.txt; git show "$R" | wc -l
     117
$ git show "$R" | grep -n -F -e '● Slippage and Bracket Usage: Exploiting the absence of slippage' -e 'Section 4: Device Sharing & Copy-Trading other Traders' -e 'Each individual trader is required to maintain their own individual trading activity.' -e 'automated trading strategies tailored to their own specific settings' -e 'Engaging in trades during tier 1 economic data releases is restricted.' -e 'MyFunded Futures prohibits hedging of any kind.' | cut -c1-60
79:Traders may make use of automated trading strategies tail
87:● Slippage and Bracket Usage: Exploiting the absence of s
88:● Tier 1 Economic Data Trading: Engaging in trades during
98:​Section 4: Device Sharing & Copy-Trading other Traders
100:Each individual trader is required to maintain their own
106:MyFunded Futures prohibits hedging of any kind. Hedging 
$ git show "$R" | sed -n 98p | od -An -tx1 | head -1
           e2  80  8b  53  65  63  74  69  6f  6e  20  34  3a  20  44  65
$ git show "$R" | grep -n 'Section [0-9]' | cut -c1-70
76:Section 1: Automated Trading Protocols
82:Section 2: Order Management and Market Conduct
92:Section 3: Termination Policies and Violation Consequences
98:​Section 4: Device Sharing & Copy-Trading other Traders
104:​Section 5: Hedging
~~~

Agrees. The quotes are present at :79, :87, :88, :98, :100 and :106 of the 117-line capture. Line :98 starts with the bytes `e2 80 8b` (U+200B) before "Section 4". Section 1 is the heading at :76, so :79 falls under it.

### C1-Y4. "R2 quotes in rows 2, 4 and 13", and the bullet count

~~~text
$ T=$(git ls-tree -r --name-only HEAD docs/reports/evidence/ | grep -- '-reply-transcript.md$'); git show "HEAD:$T" | grep -n -F -e 'for fully automated order execution' -e 'This enables your custom software to submit orders, manage positions' -e 'integrate your trading bot or automated strategy via the Tradovate API' -e 'your MyFundedFutures Tradovate evaluation and funded accounts' -e 'on all plans' | cut -d: -f1 | tr '\n' ' '; echo
27 28 29 
$ git show "HEAD:$T" | grep -n '^•' | cut -c1-40
28:• Automated trading solutions using a
29:• Algo trading is permitted on all pl
30:• High-frequency trading is not allow
31:• For live accounts, automated tradin
$ git show HEAD:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | grep -n -F -e 'now permitted' -e 'moving forward' | cut -c1-50 | head -5
28:> "Algo trading is now permitted at MFFU moving
108:### 3.2 The "now permitted" effective-date gap
636:| §3.2 effective date | **DOES NOT ADDRESS** |
~~~

Agrees. The R2 strings are on transcript :27 to :29. There are four `•` bullets at :28 to :31, so "Algo trading is permitted on all plans" is bullet 2. R1's "now permitted" and "moving forward" are on the 2026-08-07 report :28.

### C1-Y5. "Read as a whole row list"

~~~text
$ sed -n '98,115p' docs/reports/2026-11-10-f4-grading-manager.md | grep -E '^\| (3|5|6|7|8|9|13|14b) \|' | awk -F'|' '{print $2 "|" $5}'
 3 | NOT ADDRESSED 
 5 | NOT ADDRESSED 
 6 | NOT ADDRESSED 
 7 | NOT ADDRESSED 
 8 | NOT ADDRESSED 
 9 | NOT ADDRESSED 
 13 | NOT ADDRESSED 
 14b | NOT ADDRESSED 
~~~

Agrees. Rows 3, 5, 6, 7, 8, 9, 13 and 14b of the current element table (manager report lines 98 to 115) are labelled NOT ADDRESSED.

### C1-Y6. "CONTRADICTED paragraph", "Conditions paragraph", "Grading check" and "Rows 4 and 14b"

~~~text
$ R=r6/announcement-research:docs/reports/evidence/2026-11-09-r6-mffu-news.txt; git show "$R" | sed -n '87p;100p' | grep -c -i automat; git show "$R" | grep -n '' | sed -n '85,90p;106p' | cut -c1-80
0
85:● Order Placement: Simultaneously placing multiple limit orders at the same p
86:● Gapped or Illiquid Market Trading: Profiting from isolated, stale or unreal
87:● Slippage and Bracket Usage: Exploiting the absence of slippage and utilizin
88:● Tier 1 Economic Data Trading: Engaging in trades during tier 1 economic dat
89:● Compliance with CME Group Rules: All trading activities must adhere to CME 
90:● Collaborative Trading: Collaborating with others to execute identical or op
106:MyFunded Futures prohibits hedging of any kind. Hedging is defined as a trad
$ T=$(git ls-tree -r --name-only HEAD docs/reports/evidence/ | grep -- '-reply-transcript.md$'); git show "HEAD:$T" | grep -n '' | sed -n '30,31p;33p' | cut -c1-80; git show HEAD:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | grep -n '' | sed -n '44,46p'
30:• High-frequency trading is not allowed, and automated tools must not exploit
31:• For live accounts, automated trading must comply with CME guidelines.
33:You are responsible for the performance and reliability of your automated sys
44:1. **No high-frequency trading.**
45:2. **Automated tools may not be built to exploit sim-environment fill favorability.**
46:3. **Live automation must follow CME guidelines.**
$ sed -n '38,49p;98,128p' docs/reports/2026-11-10-f4-grading-manager.md | grep -c -i -E 'F4 (passes|is closed|is satisfied|is met|should be|can be closed)|satisfie[s] F4|recommend(s|ed)? (that )?F4'
0
$ sed -n '98,115p' docs/reports/2026-11-10-f4-grading-manager.md | grep -E '^\| (4|14b) \|' | awk -F'|' '{print $2 "|" $5}'
 4 | COVERED-BY-INFERENCE 
 14b | NOT ADDRESSED 
~~~

Reading. The two published-page lines quoted under the CONTRADICTED paragraph (:87 and :100) contain no "automat" (count 0), so neither names automation. The page conditions are at :85 to :90 and :106. The R2 conditions are at transcript :30, :31 and :33, and the R1 conditions at the 2026-08-07 report :44 to :46. The conditions paragraph paraphrases these. That the paraphrase is fair is a reading, and the lines are printed here for it. The grading-phrase search over the scoped parts (manager lines 38 to 49 and 98 to 128) gives 0. Row 4 is COVERED-BY-INFERENCE and row 14b is NOT ADDRESSED. The R2 counts behind 14b (NinjaTrader 0, Rithmic 0) are in the manager report's Correction 1, C1-V7.

### Not re-run

The evidence under findings 1 to 4 quotes the manager draft as it stood when worker 4 read it, with that draft's line numbers (for example :111, :99, :114). The draft has since been changed by the fixes, so those blocks cannot be re-run. The labels in the current table are listed in C1-Y5. The process-log figures (for example "443 lines") also describe that draft.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
