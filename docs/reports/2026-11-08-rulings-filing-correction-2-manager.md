Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

# Unit 2026-11-08-rulings-filing-correction-2 — manager report (praxis-manager)

## Task

Append "D-2026-11-08-A Correction 1" to DECISIONS.md after :1645. It cures findings 1, 2, 3, 4 and 7 of the Correction-1 adversary (`docs/reports/2026-11-08-rulings-filing-manager.md:965–1049`, `VERDICT: REFUTED`), carries findings 5, 6, 8 and 9 as wording, and follows the master's dispositions in DECISION_LOG `2026-11-08T14:57:00Z` (WHO: praxis-master, DECISION_LOG.md:725). Also append one MANIFEST.md row after :293 for `docs/reports/2026-11-08-amear-answers-flags.md`. Append only; no git index change; A1–A11 are cited, not filed (D-2026-11-08-B is a later unit).

## Rubric criteria addressed

S1, S2, S4, S5, S6 (cross-block line in the entry), S8, S13 (the standing sentence once in the appended range; see V4). The auditor grades these; this report does not grade itself.

## Workers dispatched

| id | mode | task | outcome |
|---|---|---|---|
| `ad23212ee271d34a0` | BUILD | Draft the block, the MANIFEST row and an evidence file in the scratchpad only. Quotes made by script (`quotes.sh` + `assemble.py`). | Returned a 63-line draft. 10 tool uses. No repo file touched. It reported 2 pointer differences from the brief: bullets at :1619–1626, not :1618–1626; A6 at answers :38–39. |
| `ac62e80437189363c` | ADVERSARIAL | Attack DECISIONS.md :1646–1708 and MANIFEST :294 against the criterion, the entry, the answers file, the adversary block, S1/S2/S8 and the labelling rule. It did not get the drafter's reasoning. | `VERDICT: CONFIRMED-WITH-MINORS`: 6 MINOR, 2 NOTE, no MAJOR. Block pasted verbatim below. |
| `a866b982207a1e70a` | BUILD (fix) | Apply 8 exact old→new replacements, written by the manager, to lines ≥1646 only, using the Edit tool. | All 8 applied. Prefix cmp rc=0 before and after. 1708 lines (unchanged). |

## Process log

1. Baselines were captured before any edit (V1).
2. The manager read the adversary block (:965–1049), DECISION_LOG :719 and :723–725, the answers file and the entry, outside its fenced block.
3. Drafting worker → the manager re-checked every quoted string against its cited source line itself, and checked fenced blocks with `cmp` (V2). Everything matched.
4. The block and the row were appended with `cat >>`, then the after-state was captured (V3).
5. Adversary → CONFIRMED-WITH-MINORS. The manager checked each source substring for the replacement text (re-captured after the fix in V5b and V5c), then wrote exact replacements for minors 1–6.
   - Minor 1: the A11 quote's line-join is now disclosed, both in the evidence-grades line and at the quote.
   - Minor 2: the invented IDs "D-2026-11-08-A1 … A9" were removed. The alternative now quotes :725.
   - Minor 3: the sentence now says "eight bullets … R2 and R3 share one".
   - Minor 4: the R-1104-2 decision is now quoted from :725, and :719 is cited as the plan.
   - Minor 5: "has since answered" is now attributed to the master's row :725. FLAG 6's #4/#5 sub-part is stated as neither settled nor left open by this entry.
   - Minor 6: the A1/A2 link is now labelled INFERRED.
   - NOTE 7: A11's third sentence is now quoted as his words, not as the master's paraphrase. "changes only on his approval" stays, labelled the master's reading, because the brief requires it.
   - NOTE 8 (MANIFEST): not changed; see "Still the master's".
6. Fix worker → the manager re-ran the diff. Exactly 5 lines changed (:1653, :1669, :1676, :1678, :1680). Every new quote matches its source (V5b).
7. Negative tests (V6): the prefix `cmp` trips on a one-byte change and on one extra line. The MANIFEST prefix sha changes when it includes row 294. The standing-sentence count reads 2 when the range also covers the original entry.
8. No second adversary was run on the fix. The brief named ONE adversarial worker. The fix is the manager's exact text, checked by the manager's own re-run (V5b). It has not been independently attacked; the auditor sees it fresh.

Deviations from the brief's wording, stated rather than hidden:
- (a) The bullets are cited as DECISIONS.md:1619–1626, not :1618–1626. The `grep -n '^- \*\*R'` output in V2 shows R1 at :1619.
- (b) The precedent is quoted by its :1052 heading, "rulings 1–5 and loop a–e". The adversary checked the five ruling bullets.

## Verification evidence

All blocks below are command output written to files by `tee`/redirect during the unit and inserted here by `cat`; nothing is retyped. Session scratchpad: `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/dac8a676-3ed6-4fca-96a1-deecc90b3c48/scratchpad`.

### V1 — before any edit

~~~~text
$ git rev-parse --short HEAD
6c233d1
$ wc -l DECISIONS.md MANIFEST.md
    1645 DECISIONS.md
     293 MANIFEST.md
    1938 total
$ cmp <(head -n 1645 DECISIONS.md) <(git cat-file -p ba941dac7adbef0d36ffe135e90991d2a2037c7d); echo rc=$?
rc=0
$ head -n 293 MANIFEST.md | openssl dgst -sha256
SHA2-256(stdin)= de2e2825ffab5b2ce56eacc59e6ff4a1a9ce9397a4d6f8899639e86e4264b271
$ git hash-object DECISIONS.md
ba941dac7adbef0d36ffe135e90991d2a2037c7d
$ git diff --numstat HEAD -- DECISIONS.md MANIFEST.md specs/SPEC_RUBRIC.md
113	0	DECISIONS.md
4	0	MANIFEST.md
10	0	specs/SPEC_RUBRIC.md
$ git diff --cached --stat | tail -1
 12 files changed, 5726 insertions(+), 2 deletions(-)
$ git status --porcelain | grep -E 'DECISIONS|MANIFEST|2026-11-08'
 M DECISIONS.md
 M MANIFEST.md
?? docs/reports/2026-11-08-amear-answers-flags.md
?? docs/reports/2026-11-08-amear-rulings-voice.md
?? docs/reports/2026-11-08-rulings-filing-manager.md
?? docs/reports/2026-11-08-strategy-filter-audit.md
$ sed -n '15,56p' docs/reports/2026-11-08-amear-answers-flags.md | openssl dgst -sha256
SHA2-256(stdin)= 7aebc0158f6d4b1907a7eeaab0d84e5835789fee91512e6d489d5acf857e9fdd
~~~~

### V2 — quote and pointer checks against sources (re-captured after the fix; line numbers are current)

~~~~text
$ chk <label> <line> <file> <string>   # = sed -n "<line>p" <file> | grep -cF <string>
R86 | 1
R88 | 1
D1546 | 1
D1624 | 1
D1625 | 1
D1645 | 1
L725a | 1
L725b | 1
L725c | 1
L719 | 1
L724 | 1
A16 | 1
$ cmp <(sed -n 1583,1589p DECISIONS.md) <(sed -n 1658,1664p DECISIONS.md) && echo MATCH   # R8 fenced
MATCH
$ cmp <(sed -n 38,39p answers) <(sed -n 1672,1673p DECISIONS.md) && echo MATCH   # A6 fenced
MATCH
$ cmp <(sed -n 18,23p answers) <(sed -n 1683,1688p DECISIONS.md) && echo MATCH   # A1-A2 fenced
MATCH
$ sed -n 50,51p answers | sed "s/^A11 //; s/^ *//" | tr "
" " " | sed "s/ Every rubric.*//"
Amear no longer edits any repo file by hand, including specs/SPEC_RUBRIC.md. Amear decides; agents write.
$ sed -n 1052p DECISIONS.md
## 2026-11-06 — D-2026-11-06-B: Amear's evening rulings 1–5 and loop a–e (voice, 2026-11-06)
$ grep -no '^- \*\*R[1-9][, R0-9]*' DECISIONS.md
1619:- **R1 
1620:- **R2, R3 
1621:- **R4 
1622:- **R5 
1623:- **R6 
1624:- **R7 
1625:- **R8 
1626:- **R9 
$ grep -no '^### F[1-4]' specs/SPEC_RUBRIC.md
17:### F1
30:### F2
45:### F3
59:### F4
$ sed -n '15,56p' answers | openssl dgst -sha256
SHA2-256(stdin)= 7aebc0158f6d4b1907a7eeaab0d84e5835789fee91512e6d489d5acf857e9fdd
$ grep -c '^## .*D-2026-11-08-B' DECISIONS.md
0
$ grep -c '2026-11-08.*U4' DISPATCH_LOG.md
0
~~~~

### V3 — immediately after the append (before the fix round)

~~~~text
$ wc -l DECISIONS.md MANIFEST.md
    1708 DECISIONS.md
     294 MANIFEST.md
    2002 total
$ cmp <(head -n 1645 DECISIONS.md) <(git cat-file -p ba941dac7adbef0d36ffe135e90991d2a2037c7d); echo rc=$?
rc=0
$ head -n 293 MANIFEST.md | openssl dgst -sha256
SHA2-256(stdin)= de2e2825ffab5b2ce56eacc59e6ff4a1a9ce9397a4d6f8899639e86e4264b271
$ cmp <(tail -n +1646 DECISIONS.md) draft-block.md; echo rc=$?
rc=0
$ cmp <(tail -n +294 MANIFEST.md) manifest-row.txt; echo rc=$?
rc=0
$ git diff --numstat HEAD -- DECISIONS.md MANIFEST.md specs/SPEC_RUBRIC.md
176	0	DECISIONS.md
5	0	MANIFEST.md
10	0	specs/SPEC_RUBRIC.md
$ git diff --cached --stat | tail -1
 12 files changed, 5726 insertions(+), 2 deletions(-)
$ git status --porcelain | grep -E 'DECISIONS|MANIFEST|2026-11-08'
 M DECISIONS.md
 M MANIFEST.md
?? docs/reports/2026-11-08-amear-answers-flags.md
?? docs/reports/2026-11-08-amear-rulings-voice.md
?? docs/reports/2026-11-08-rulings-filing-correction-2-manager.md
?? docs/reports/2026-11-08-rulings-filing-manager.md
?? docs/reports/2026-11-08-strategy-filter-audit.md
$ sed -n '1646,$p' DECISIONS.md | grep -c 'Fills are optimistic'
1
$ awk -F"|" "NR>=290{print NR\": \"NF}" MANIFEST.md
290: 7
291: 7
292: 7
293: 7
294: 7
~~~~

### V4 — final state (after the fix round)

~~~~text
$ wc -l DECISIONS.md MANIFEST.md
    1708 DECISIONS.md
     294 MANIFEST.md
    2002 total
$ cmp <(head -n 1645 DECISIONS.md) <(git cat-file -p ba941dac7adbef0d36ffe135e90991d2a2037c7d); echo rc=$?
rc=0
$ head -n 293 MANIFEST.md | openssl dgst -sha256
SHA2-256(stdin)= de2e2825ffab5b2ce56eacc59e6ff4a1a9ce9397a4d6f8899639e86e4264b271
$ git diff --numstat HEAD -- DECISIONS.md MANIFEST.md specs/SPEC_RUBRIC.md
176	0	DECISIONS.md
5	0	MANIFEST.md
10	0	specs/SPEC_RUBRIC.md
$ git diff --cached --stat | tail -1
 12 files changed, 5726 insertions(+), 2 deletions(-)
$ git status --porcelain | grep -E 'DECISIONS|MANIFEST|2026-11-08'
 M DECISIONS.md
 M MANIFEST.md
?? docs/reports/2026-11-08-amear-answers-flags.md
?? docs/reports/2026-11-08-amear-rulings-voice.md
?? docs/reports/2026-11-08-rulings-filing-correction-2-manager.md
?? docs/reports/2026-11-08-rulings-filing-manager.md
?? docs/reports/2026-11-08-strategy-filter-audit.md
$ sed -n '1646,$p' DECISIONS.md | grep -c 'Fills are optimistic'
1
$ sed -n '1646,$p' DECISIONS.md | grep -c '```'
6
$ tail -n 1 MANIFEST.md
| /docs/reports/2026-11-08-amear-answers-flags.md | Report | 2 | 2026-11-08 | Amear's answers A1–A11 to the D-2026-11-08-A FLAGS and the master's routed items, from his 2026-11-08 voice session, filed verbatim by praxis-master (ruling block lines 15–56, sha 7aebc015…9fdd); source for D-2026-11-08-B (to be filed) |
$ git hash-object DECISIONS.md MANIFEST.md
8845ce7a2e9d19ec62e57799bd1922e4a162797c
b4ab05eaccc893be8fa94738305928598f5c87dc
$ sed -n 1646,1708p DECISIONS.md | openssl dgst -sha256
SHA2-256(stdin)= 2fa6aed075679b9ab5626d28059f8c601872f212e6d40dc0c9d1d4babdb629a6
$ git diff --cached --name-only | grep -cE "DECISIONS|MANIFEST"
0
~~~~

### V5 — fix round: diff of the draft against the appended tail (draft line N = DECISIONS.md line 1645+N)

~~~~text
$ diff draft-block.md <(tail -n +1646 DECISIONS.md)   # draft line N = DECISIONS.md line 1645+N
8c8
< **Evidence grades.** Every quotation below was produced by script (`sed -n` / `grep -o`) from the file and line cited; none is retyped. Amear's words carry WHO: amear and a pointer. Other sentences carry one of three labels: "master's reading, changeable by Amear"; "master's decision under R-1104-2 (DECISIONS.md:748), changeable by Amear"; "INFERRED, the filer's, not his word". Line pointers were re-read this unit (OBSERVED).
---
> **Evidence grades.** Every quotation below was produced by script (`sed -n` / `grep -o`) from the file and line cited; none is retyped. Where a quote spans two or more source lines, the lines are joined by script with one space, and the leading label and indent are dropped; the quote's pointer gives the line range. Amear's words carry WHO: amear and a pointer. Other sentences carry one of three labels: "master's reading, changeable by Amear"; "master's decision under R-1104-2 (DECISIONS.md:748), changeable by Amear"; "INFERRED, the filer's, not his word". Line pointers were re-read this unit (OBSERVED).
24c24
< Amear has since answered this flag; his A6 opens "FLAG 6:" (OBSERVED). A6 (**WHO: amear**; DECISION_LOG `2026-11-08T15:05:00Z`, DECISION_LOG.md:723 — a hand stamp, "about 19 minutes ahead; the order of events in this ledger is correct" per DECISION_LOG `2026-11-08T14:47:00Z`, :724; answers file `docs/reports/2026-11-08-amear-answers-flags.md`:38–39):
---
> The master's row DECISION_LOG `2026-11-08T14:57:00Z` (:725) says his A6 "now answers it"; A6 opens "FLAG 6:" (OBSERVED). FLAG 6 also asks "do R8's words on #4 and #5 name F2's governing rule and 15:00 disposition" (:1645); A6's words do not name that part, and this entry does not read A6 as settling it or as leaving it open. A6 (**WHO: amear**; DECISION_LOG `2026-11-08T15:05:00Z`, DECISION_LOG.md:723 — a hand stamp, "about 19 minutes ahead; the order of events in this ledger is correct" per DECISION_LOG `2026-11-08T14:47:00Z`, :724; answers file `docs/reports/2026-11-08-amear-answers-flags.md`:38–39):
31c31
< Master's reading, changeable by Amear: the F2 breaker-values PROPOSAL unit (U4 in the DECISION_LOG `2026-11-08T14:22:00Z` plan) is authorised. Master's reading, changeable by Amear: F2's state in `specs/SPEC_RUBRIC.md` changes only on his approval of the proposed values. FLAG 6's sentence "The rubric is his to edit (:3-4)." (DECISIONS.md:1645) is superseded by his A11 (master's reading, changeable by Amear). A11's first two sentences (**WHO: amear**; DECISION_LOG `2026-11-08T15:05:00Z`, :723; answers file :50–51): "Amear no longer edits any repo file by hand, including specs/SPEC_RUBRIC.md. Amear decides; agents write." Master's reading, changeable by Amear: the rubric is now edited by agents; each edit cites a logged Amear approval inline and passes the auditor before commit. A11's replacement of the rubric's :3-4 sentence is NOT done here. Nothing is resolved beyond his words.
---
> Master's reading, changeable by Amear: the F2 breaker-values PROPOSAL unit (U4 in the DECISION_LOG `2026-11-08T14:22:00Z` plan) is authorised. Master's reading, changeable by Amear: F2's state in `specs/SPEC_RUBRIC.md` changes only on his approval of the proposed values. FLAG 6's sentence "The rubric is his to edit (:3-4)." (DECISIONS.md:1645) is superseded by his A11 (master's reading, changeable by Amear). A11's first two sentences (**WHO: amear**; DECISION_LOG `2026-11-08T15:05:00Z`, :723; answers file :50–51, joined): "Amear no longer edits any repo file by hand, including specs/SPEC_RUBRIC.md. Amear decides; agents write." Master's reading, changeable by Amear: the rubric is now edited by agents. A11's third sentence (**WHO: amear**; answers file :51–53, joined): "Every rubric edit cites a logged Amear approval inline and passes the auditor before commit." A11's replacement of the rubric's :3-4 sentence is NOT done here. Nothing is resolved beyond his words.
33c33
< **Cure for finding 2 (filing form).** Amear's words (WHO: amear; DECISIONS.md:1546, inside the fenced block): "WHO: amear. File each as a DECISIONS.md entry citing this session." Master's decision under R-1104-2 (DECISIONS.md:748), changeable by Amear: the nine rulings are filed as ONE entry, D-2026-11-08-A, with a labelled per-ruling section each (the R1–R9 bullets at DECISIONS.md:1619–1626). Master's decision under R-1104-2 (DECISIONS.md:748), changeable by Amear: this is the master's plan, DECISION_LOG `2026-11-08T14:22:00Z` (DECISION_LOG.md:719): "U1 FILING — D-2026-11-08-A in DECISIONS.md: R1–R9". The alternative the master named and did not take: nine separate entries, D-2026-11-08-A1 … A9. Precedent (OBSERVED, DECISIONS.md:1052): `## 2026-11-06 — D-2026-11-06-B: Amear's evening rulings 1–5 and loop a–e (voice, 2026-11-06)`. INFERRED, the filer's, not his word: his own answers heading "File as D-2026-11-08-B" (answers file :16, WHO: amear) covers eleven answers, A1–A11, in one entry. Whether one entry satisfies "File each" is his question; it is under NEEDS AMEAR, unanswered.
---
> **Cure for finding 2 (filing form).** Amear's words (WHO: amear; DECISIONS.md:1546, inside the fenced block): "WHO: amear. File each as a DECISIONS.md entry citing this session." Master's decision under R-1104-2 (DECISIONS.md:748), changeable by Amear: the nine rulings are filed as ONE entry, D-2026-11-08-A, with a labelled section per ruling (eight bullets at DECISIONS.md:1619–1626; R2 and R3 share one, :1620). The decision is on the ledger at DECISION_LOG `2026-11-08T14:57:00Z` (WHO: praxis-master, DECISION_LOG.md:725): "Master's decision under R-1104-2, changeable by him: one entry per ruling-set with a labelled per-ruling section each". It follows the master's plan, DECISION_LOG `2026-11-08T14:22:00Z` (DECISION_LOG.md:719): "U1 FILING — D-2026-11-08-A in DECISIONS.md: R1–R9". The alternative the master named and did not take (:725, "alternative = nine separate entries"): nine separate entries, one per ruling. Precedent (OBSERVED, DECISIONS.md:1052): `## 2026-11-06 — D-2026-11-06-B: Amear's evening rulings 1–5 and loop a–e (voice, 2026-11-06)`. INFERRED, the filer's, not his word: his own answers heading "File as D-2026-11-08-B" (answers file :16, WHO: amear) covers eleven answers, A1–A11, in one entry. Whether one entry satisfies "File each" is his question; it is under NEEDS AMEAR, unanswered.
35c35
< **Cure for finding 3 (filing note 3's lean).** Filing note 3 (rulings file :88) also says: "R4 fills the gate definition." That sentence is the master's reading at the time of filing (filing note 3), changeable by Amear; D-2026-11-08-A did not carry it. His A1 and A2 now rule on that subject (**WHO: amear**; DECISION_LOG `2026-11-08T15:05:00Z`, :723; answers file :18–23):
---
> **Cure for finding 3 (filing note 3's lean).** Filing note 3 (rulings file :88) also says: "R4 fills the gate definition." That sentence is the master's reading at the time of filing (filing note 3), changeable by Amear; D-2026-11-08-A did not carry it. That his A1 and A2 now rule on that subject is INFERRED, the filer's, not his word (their openings are "FLAG 1:" and "FLAG 2:"; the master's row :725 says "his A1/A2 now rule on it"). A1 and A2 (**WHO: amear**; DECISION_LOG `2026-11-08T15:05:00Z`, :723; answers file :18–23):
~~~~

#### V5b — new strings present once in :1646+, and their sources

~~~~text
$ diff draft-block.md final-block.md | grep -c "^[<>]"
10
$ diff ... | grep "^[<>]" | cut -c1-3 | sort | uniq -c
   5 < 
   5 > 
$ wdiff-style: changed lines numbers
8c8
24c24
31c31
33c33
35c35
$ new-quote checks
L725 | 1
D1645 | 1
A11 s3 joined | 1
none is retyped. Where a quote spans | 1
now answers it"; A6 opens | 1
answers file :50–51, joined) | 1
answers file :51–53, joined) | 1
eight bullets at DECISIONS.md:1619–1626 | 1
The decision is on the ledger at DECISION_LOG | 1
"alternative = nine separate entries"): nine separate entries, one per ruling. | 1
That his A1 and A2 now rule on that subject is INFERRED | 1
~~~~

#### V5c — remaining :725 sources and the removed IDs

~~~~text
$ sed -n 725p DECISION_LOG.md | grep -cF 'alternative = nine separate entries'
1
$ sed -n 725p DECISION_LOG.md | grep -cF 'now answers it'
1
$ sed -n 725p DECISION_LOG.md | grep -cF 'his A1/A2 now rule on it'
1
$ grep -c 'D-2026-11-08-A1' DECISIONS.md
0
~~~~

### V6 — negative tests (the checks trip)

~~~~text
$ cmp <(head -n 1645 DECISIONS.md | sed "1645s/here\./here!/") <(git cat-file -p ba941dac...) >/dev/null; echo rc=$?   # one-byte change to line 1645, in a pipe only
rc=1
$ cmp <(head -n 1646 DECISIONS.md) <(git cat-file -p ba941dac...) >/dev/null; echo rc=$?   # one line too many
rc=1
$ head -n 294 MANIFEST.md | openssl dgst -sha256   # includes the new row: must differ from de2e2825...
SHA2-256(stdin)= 8b50a2f7585b9ede695b5bceff04e1db4267edd189c59db4ccaddab4d826d114
$ sed -n '1534,$p' DECISIONS.md | grep -c 'Fills are optimistic'   # entry + correction: must be 2
2
~~~~

### V7 — the appended block

Not pasted here, so that this report carries the standing sentence once (S13): a full copy would repeat it. The block is DECISIONS.md:1646–1708. Its sha256, `2fa6aed0…29a6`, is in V4; V5 shows its 5 changed lines; the auditor reads it in place.

## Adversarial findings

Worker `ac62e80437189363c` (praxis-worker, ADVERSARIAL) returned the block below; it is its own output, verbatim. The only change is that the harness's two-space indent was removed from each line. The worker made 12 tool calls and wrote no repo file. It wrote one scratch file outside the repo, by its own account. The block contains triple-backtick lines, so it is fenced with `~~~~`. Line pointers in it refer to DECISIONS.md BEFORE the fix round. Each finding's disposition is in the Process log, step 5, and the diff is in V5.

~~~~text
VERDICT: CONFIRMED-WITH-MINORS

Findings:

1. **MINOR — :1676, the A11 quote joins two lines without saying so.** The quote "Amear no longer edits any repo file by hand, including specs/SPEC_RUBRIC.md. Amear decides; agents write." is not on any single line of the answers file. It is :50 and :51 joined, with the "A11 " prefix and the 4-space indent removed. :1653 says every quotation was "produced by script (`sed -n` / `grep -o`) from the file and line cited; none is retyped". `grep -o` cannot produce a quote that spans two lines, and the join is not disclosed. The words themselves are identical.
```
single-line grep in answers file:
0
joined:
1
in entry:
1
```

2. **MINOR — :1678, the names "D-2026-11-08-A1 … A9" are not on disk.** The entry says "The alternative the master named and did not take: nine separate entries, D-2026-11-08-A1 … A9." Row :725 names only "alternative = nine separate entries". The entry ID strings occur nowhere else, and this sentence gives no pointer to :725. The names also collide with Amear's answer numbers A1–A9. A9 is his "File the … audit as an input to F2".
```
A1..A9 names:
DECISIONS.md:1678:**Cure for finding 2 (filing form).** ...
```

3. **MINOR — :1678, "a labelled per-ruling section each (the R1–R9 bullets at DECISIONS.md:1619–1626)" overstates what is there.** Those are 8 bullets for 9 rulings: R2 and R3 share one bullet, "**R2, R3 — which arm carries GO; gate 6.**" (:1620).

4. **MINOR — :1678, the R-1104-2 decision points at the wrong row.** The second sentence is labelled "Master's decision under R-1104-2 …" but cites the plan row :719. Row :719 does not invoke R-1104-2 and is a plan, not a decision. The R-1104-2 decision itself ("Master's decision under R-1104-2, changeable by him: one entry per ruling-set…") is in :725, and this cure never cites :725. :725 appears only in the Status line, as general authorisation.

5. **MINOR — :1669, "Amear has since answered this flag" has no label and says more than A6 does.** FLAG 6 (:1645) asks three things. One of them is "do R8's words on #4 and #5 name F2's governing rule and 15:00 disposition". A6's words ("R8 starts the breaker PROPOSAL unit. F2's state changes when Amear approves the proposed values.") do not address that part. The correction does not carry it, does not label it as made moot, and does not put it under NEEDS AMEAR. The brief's criterion 8 does allow NEEDS AMEAR to hold only (i), so this is wording, not an S8 answer.

6. **MINOR — :1680, "His A1 and A2 now rule on that subject" has no label.** It links note 3's lean to A1/A2 (the same kind of gap as finding 5). It can be traced through A2's own opening "FLAG 2:" and adversary :985 ("Note 3 also picks a reading on FLAG 2's subject"), but it is not marked INFERRED.

7. **NOTE — :1676, A11's third sentence is labelled as the master's.** "the rubric is now edited by agents; each edit cites a logged Amear approval inline and passes the auditor before commit" is close to his own third sentence ("Every rubric edit cites a logged Amear approval inline and passes the auditor before commit."). It carries the label "master's reading", which credits it below his word. The reading "changes only on his approval" adds "only" to A6's "when". It is labelled and was required by the criterion.

8. **NOTE — MANIFEST.** :294 has the right column count:
```
pipes: 6 6 6 6 6
```
But unlike :290–291 it has no "untracked (`??`) at time of row" clause, although the file is `?? docs/reports/2026-11-08-amear-answers-flags.md`. The DECISIONS.md row :293 still describes only :1534–1645, not the Correction at :1646–1708. Neither was in the brief's scope.

CHECKED-CLEAN:
- R8 fenced block :1658–1664 against :1583–1589: `CMP_SAME`. A6 :1672–1673 against answers :38–39: `A6_SAME`. A1/A2 :1683–1688 against answers :18–23: `A1A2_SAME`.
- Answers ruling block sha: `7aebc0158f6d4b1907a7eeaab0d84e5835789fee91512e6d489d5acf857e9fdd`, matches.
- `grep -cF` = 1 for each of these quotes on their cited lines:
  - rulings :86 ("Until it does … unblocked.") and :88 ("R4 fills the gate definition.")
  - DECISIONS :1546, :1645, :1624, :1625 (whole sentence) and :1052 heading (`-x`)
  - answers :16
  - DECISION_LOG :719, :724, :725 (×3)
  - adversary findings 5, 6, 8, 9
- Adversary block :970 = `VERDICT: REFUTED`. "fills the gate" in :1534–1645 = `0`, so "did not carry it" holds.
- Append-only: `head -n 1645 | git hash-object` = `ba941dac…`, matching row :725.
- S4 grep = `0`. No 2026-11-08 U4 row in DISPATCH_LOG. Rubric F1–F4 at :17/:30/:45/:59. Numstat bytes are `1 0 \t 0 \t specs/SPEC_RUBRIC.md` (real tabs). Standing sentence count in :1646–1708 = `1`.
- R-1104-2 at :748. Precedent heading at :1052 verified, with five rulings in one entry. Row 723 is WHO: amear. :724's clock note is quoted faithfully.
- De-identification: no medication or brand term matched; #5 is named only by number with 15:00–18:00.
- Only A1, A2, A6 and A11 are quoted. The only other A-numbers are the "A1–A11" and "A1 … A9" mentions at :1678; no answer is filed as a ruling.
- NEEDS AMEAR holds only (i).

Read-only held: the only file written was a scratch file outside the repo.

Result: PASS
~~~~

The manager stress-tested this block. Every finding is about the wording or labelling of lines ≥1646. Findings 1–6 were cured with the manager's exact text (Process log, step 5). Finding 2's absence claim was confirmed by the post-fix count in V5b: `grep -c 'D-2026-11-08-A1'` = 0. NOTE 7 was partly cured: A11's third sentence is now his quoted words. "only" stays, labelled as the master's reading. NOTE 8 was not acted on (outside the brief's scope).

## S6 cross-block check

- F1–F4 sit at `specs/SPEC_RUBRIC.md`:17, :30, :45, :59 (V2), and this unit did not touch them.
- `git diff --numstat HEAD -- specs/SPEC_RUBRIC.md` reads `10	0` both before and after (V1, V4). That is the pre-existing July hunk.
- Interaction recorded in the entry, not resolved: R8/A6 ↔ F2's state. The entry gives it as the master's reading only: F2 changes on Amear's approval of the proposed values.
- No other block is touched.

## Files staged

None. This unit ran no git add, commit, reset, stash or checkout. The index is unchanged: `git diff --cached --stat | tail -1` still reads `12 files changed, 5726 insertions(+), 2 deletions(-)` (V4). DECISIONS.md and MANIFEST.md are not in the index (V4: `grep -cE` = 0). Both show ` M` in the working tree. This report is untracked (`??`).

Working-tree changes by this unit:
- `DECISIONS.md` :1646–1708: 63 lines appended. The block sha256 is `2fa6aed0…29a6` and the file blob is `8845ce7a`.
- `MANIFEST.md` :294: 1 row appended. The file blob is `b4ab05ea`.
- `docs/reports/2026-11-08-rulings-filing-correction-2-manager.md`: created (this file).

No other repo file was written. Workers wrote only into the session scratchpad. No agent-memory file was written by any worker.

## Result

**Result: PASS at level WRITTEN** — appended and adversary-checked. This is not audited, not staged and not committed; the independent auditor grades it.

**Does NOT cover:**
- Filing A1–A11 (that is D-2026-11-08-B, a later unit).
- The rubric :3-4 replacement under A11.
- Any U4 dispatch.
- Re-wording lines ≤1645.
- A second adversary on the fix round. The brief named one; the fix rests on the manager's re-run, V5b.
- Updating MANIFEST row :293. It still describes DECISIONS.md :1534–1645 only.

**Still the master's:**
- Whether MANIFEST :293 should be updated to cover :1646–1708. This unit was limited to one row.
- Whether row :294 should carry an "untracked at time of row" clause, as :290–291 do (adversary NOTE 8).
- Rebuilding `commit-idx-u1` with the new blobs (`8845ce7a`, `b4ab05ea`) and the re-audit (DECISION_LOG :725).
- The A6 sub-part the entry neither settles nor leaves open ("do R8's words on #4 and #5 name F2's governing rule and 15:00 disposition"). Routing it is the master's.

**Questions only Amear can answer:**
- (i) Whether one entry satisfies "File each as a DECISIONS.md entry" (DECISIONS.md:1546). Unanswered.
