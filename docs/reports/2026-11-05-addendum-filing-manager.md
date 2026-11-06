# 2026-11-05 — Unit `2026-11-05-addendum-filing` — manager report

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## Task
Task 1: append D-2026-11-05-A to DECISIONS.md from the DECISION_LOG row `[2026-11-05T23:40:21Z] WHO: amear`. Task 2: add MANIFEST rows for 2026-11-04/05 files in docs/reports/ and docs/briefs/ that had none. Working tree only; nothing staged.

## Rubric criteria addressed
S1 | Every claim in a report has pasted command output, not a description of output. S4 | Every deviation from the plan has a DECISIONS.md entry with a traceable authorisation chain, written before the work, not after. S5 | No approval is inferred from a verbal or in-session exchange. The ledger append is the authorisation. S8 | No question that belongs to Amear is answered on his behalf.

## Workers dispatched
| id | mode | outcome |
|---|---|---|
| (manager) | BUILD, pure doc edit by script | entry + rows appended |
| a3e070e749a33018b | ADVERSARIAL, fidelity of entry vs source row | VERDICT: FAIL — 4 MAJOR (3 wrong report-C line pointers, 1 wrong grade claim), 3 attribution defects, 4 MINOR. Fixed. |
| a6f1bcecb7ae2b43c | ADVERSARIAL, re-check of fixed lines 818-832 | VERDICT: FAIL — 1 attribution defect in (i), 2 MINOR in (ii)/(iii). All pointers, quotes and S8 passed. Fixed; this third edit had no third adversarial pass. |

## Process log
1. Read the source row, D-2026-11-04-A as the template, the MANIFEST row format, report C's anchors, and `bd show Praxis_build-r8j`.
2. `scratchpad/build.py` cut the five items out of the row programmatically, between `Verbatim:** "` and `" **Master's reading`. It asserted that the five items joined back equal the source, then appended the entry and nine MANIFEST rows. It also asserted that none of the seven report or brief filenames already had a row.
3. The first adversary found that I had misread report C's NEEDS AMEAR numbering by one line. A blank line at :246 meant item 2 is :248, not :247, and item 7 is :253, not :252. I had also claimed that :170 had no grade. It sits under the INFERRED heading at :165. And three sentences restated the master's reading without saying so. `fix.py` made six exact-match replacements, only on lines this unit had appended.
4. The second adversary found one more unattributed master-reading sentence and two minor ones. `fix2.py` made three replacements.
5. Lines 1–801 of DECISIONS.md (the pre-unit file) were hash-checked as unchanged after every edit. See the evidence below.
6. Observation: DECISION_LOG.md grew during the unit. The amear row moved from line 465 to line 466. A row was inserted above it, not by this unit. The quote was re-checked against the row found by its prefix, not by line number.

Not fixed (stated):
- Adversary 1 item 10: unit `2026-11-05-addendum-filing` has no DISPATCH_LOG row. DISPATCH_LOG is off-limits to this unit.
- Adversary 1 item 11: the standing-limitation line repeats inside the entry. That is the D-2026-11-04-A house style, and it is not attributed to Amear.

## Verification evidence

**Baseline (before any edit):**
```
     801 DECISIONS.md
     216 MANIFEST.md
aa1f48f6e830120108944bcb326b062f5764fe9c2d76978de2b6784680ec7bb3  DECISIONS.md
c74a958ca20886a49957e2b2eaaf8dbf1d04e8ef2e33d6258c1041812e69b337  MANIFEST.md
```
**After (final):**
```
     832 DECISIONS.md
     225 MANIFEST.md
600a57fbeb34da380fd17294efa5a7f6ee0234b024670a753df2a7bfad1043b8  DECISIONS.md
828b75ddb0b2032fdc6b12435751e08733275bc438f1b4528c305d4d24f059dd  MANIFEST.md
```
**Append-only proof:** the pre-unit prefix still hashes to the baseline.
```
$ head -n 801 DECISIONS.md | shasum -a 256
aa1f48f6e830120108944bcb326b062f5764fe9c2d76978de2b6784680ec7bb3  -
$ head -n 216 MANIFEST.md | shasum -a 256
c74a958ca20886a49957e2b2eaaf8dbf1d04e8ef2e33d6258c1041812e69b337  -
```
DECISIONS.md: appended lines 802–832. Line 802 is blank, the heading is at 803, the five quoted items are at 812–816 (heading 811), the interactions are at 819–823 (heading 818), and the NEEDS AMEAR questions are at 829–832 (heading 828). MANIFEST.md: appended lines 217–225.

**Index untouched:**
```
$ git status --porcelain -- DECISIONS.md MANIFEST.md
 M DECISIONS.md
 M MANIFEST.md
```

**Sizes and sha256 of the files given rows:**
```
   11411 docs/briefs/2026-11-04-research-briefs-tickdata-repos-poc.md
   62522 docs/reports/2026-11-04-tick-data-sources.md
   76290 docs/reports/2026-11-04-comparable-builds.md
   61504 docs/reports/2026-11-04-proof-of-concept-standard.md
   13967 docs/reports/2026-11-04-research-compiled-for-voice.md
   17183 docs/reports/2026-11-04-research-compiled-for-voice-v2.md
    7765 docs/reports/2026-11-04-voice-session-notes-4.md
4c115d0382c571487ce2c249c34aa533d8330ba9454c283c7bdeee3312059980  docs/briefs/2026-11-04-research-briefs-tickdata-repos-poc.md
72957d25f0dbc0ab306fdcc37c6799d39af64f6a34dce032b4513d443cc7bec9  docs/reports/2026-11-04-tick-data-sources.md
05888af093cf7857e30f3711504174cf6b08ba73737f1da48660b95c8a761b1e  docs/reports/2026-11-04-comparable-builds.md
cf7560381bad73a535a18778bdea970953084d8416f431457083240b40eeb617  docs/reports/2026-11-04-proof-of-concept-standard.md
f1bcf385468b5204a623ec0a36cd637d2321afc4c85f72fd305b7c77fb5a2401  docs/reports/2026-11-04-research-compiled-for-voice.md
c1eb4acd5060df638f48f0db1562a679152ea79d7d818d9a68f6a6247dfbbc27  docs/reports/2026-11-04-research-compiled-for-voice-v2.md
ea5d168511bd9f26059105c16fca611040074de72cf7f89debd8c5ed4c5f307f  docs/reports/2026-11-04-voice-session-notes-4.md
```
These are pre-unit sizes and hashes. This unit did not touch these files. My own report's hash cannot appear inside itself.

**Pre-existing-row check:** the first number is the count of MANIFEST lines naming the file; the bracket is its git status.
```
0 [??] docs/briefs/2026-11-04-research-briefs-tickdata-repos-poc.md
0 [??] docs/reports/2026-11-04-comparable-builds.md
1 [??] docs/reports/2026-11-04-gate-r1104-1-manager.md
1 [] docs/reports/2026-11-04-handoff-r1104-filing-manager.md
0 [??] docs/reports/2026-11-04-proof-of-concept-standard.md
0 [??] docs/reports/2026-11-04-research-compiled-for-voice-v2.md
0 [??] docs/reports/2026-11-04-research-compiled-for-voice.md
1 [??] docs/reports/2026-11-04-return-handoff-claude-ai.md
1 [] docs/reports/2026-11-04-status-refresh-manager.md
0 [??] docs/reports/2026-11-04-tick-data-sources.md
1 [??] docs/reports/2026-11-04-vm-handoff-readback-ticksource-exe.md
0 [??] docs/reports/2026-11-04-voice-session-notes-4.md
```
The vm-handoff, return-handoff and gate-r1104-1 files already had rows, so they were not duplicated. The voice-session-notes-4 file had no row and was not on the brief's list. It got a row.

## Fidelity check (his quoted words vs the source row)
```
$ cmp source-quote.txt filed-quote.txt && echo "CMP: IDENTICAL"
CMP: IDENTICAL
$ wc -c source-quote.txt filed-quote.txt
     637 source-quote.txt
     637 filed-quote.txt
```
The check was re-run after both fix passes: `CMP: IDENTICAL`. It was also re-run against the row at its new line, found by prefix: `current-row quote == filed quote: True 635`. That is 635 characters, versus 637 bytes, because the em dash is three bytes in UTF-8. Adversary 1's own comparison gave `JOINED==SRC: True` and matched each item one by one.

Quoted master-reading strings after fix 2, substring-checked against the row:
```
(a) has no optimisation step, (b) does True
is put back to Amear, not resolved True
the MFFU account size itself is still no True
```
**Negative test** (the gate blocks): one word was changed in a copy.
```
source-quote.txt tampered.txt differ: char 22, line 1
negative-test cmp exit=1
```

**The filed items (DECISIONS.md:812-816):**
    - *"1. Walk-forward runs BOTH ways: (a) paper's fixed rules, nothing optimised; (b) four parameters tuned per window — lookback, noise multiplier, stop-ATR multiplier, exit policy. A stop is added to the strategy for (b) on its own branch; baseline file unchanged."*
    - *"2. Windows per spec: 252-day in-sample / 63-day out-of-sample / 63-day step."*
    - *"3. Max-DD gate base: the lower of 4% of the MFFU account size and MFFU's trailing drawdown limit. Revisit if a personal account is used."*
    - *"4. Every window also reports worst drawdown at 1 MNQ and 1 NQ against each MFFU tier's limit."*
    - *"5. Account tier: no decision until backtest + paper results exist."*

## MANIFEST rows added (MANIFEST.md:217-225, pasted)
    | /docs/briefs/2026-11-04-research-briefs-tickdata-repos-poc.md | Brief | 2 | 2026-11-04 | Research briefs A/B/C (tick data, comparable builds, proof of concept), written 2026-11-04 in the Claude.ai Praxis channel at Amear's request; briefs only, nothing dispatched/bought/decided; three separate agents, one report each |
    | /docs/reports/2026-11-04-tick-data-sources.md | Report | 2 | 2026-11-04 | Brief A: NQ tick data 2021-03-08 → 2026-07-17 — sources, cost, format, NT8 path; unit 2026-11-04-tick-data-sources; research only, nothing bought/downloaded/imported/run; header says not audited (the voice compilation reports it passed on re-audit) |
    | /docs/reports/2026-11-04-comparable-builds.md | Report | 2 | 2026-11-04 | Brief B: comparable builds on GitHub (research unit B), URLs read 2026-11-04; producer praxis-manager; header says ungraded (the voice compilation reports it passed on re-audit) |
    | /docs/reports/2026-11-04-proof-of-concept-standard.md | Report | 2 | 2026-11-04 | Brief C (report C): what "proof of concept" means before spending money; unit 2026-11-04-proof-of-concept-standard; research only; PROPOSED checklist, §3 tick data refinement vs prerequisite, NEEDS AMEAR 1–11; corrections appended |
    | /docs/reports/2026-11-04-research-compiled-for-voice.md | Report | 2 | 2026-11-04 | Research compiled for the voice session v1 (A/B/C summary for Amear, from praxis-master); SUPERSEDED by v2 (-v2.md), kept unchanged |
    | /docs/reports/2026-11-04-research-compiled-for-voice-v2.md | Report | 2 | 2026-11-04 | Research compiled for the voice session v2 (supersedes v1 after v1's fidelity-audit FAIL); PARKED at audit FAIL 2, two MINOR — see DECISION_LOG 2026-11-04T22:42:03Z |
    | /docs/reports/2026-11-04-voice-session-notes-4.md | Report | 2 | 2026-11-04 | Voice session notes 4 (Amear, Claude.ai voice, 2026-11-04 evening ET; written 2026-11-05) on the v2 compilation and its §5 decision list; not an audited report; rulings are Amear's, quoted or closely paraphrased |
    | /DECISIONS.md | Log | 2 | 2026-11-05 | D-2026-11-05-A appended: walk-forward design rulings (Amear, voice 2026-11-05; DECISION_LOG 2026-11-05T23:40:21Z) — five items verbatim, interactions stated not resolved, four NEEDS AMEAR |
    | /docs/reports/2026-11-05-addendum-filing-manager.md | Report | 2 | 2026-11-05 | Manager report for unit 2026-11-05-addendum-filing (D-2026-11-05-A filing + MANIFEST rows for 2026-11-04/05 briefs and reports); ungraded at time of row |

## Adversarial findings
- Adversary 1 found pointers wrong by one line: :247 should be :248, and :252 should be :253. Fixed. It found that "`:170` carries no grade" was false, because the :165 heading says INFERRED. Fixed. It found that "Item 3 answers the formula", "Walk-forward still waits on it" and the (v) authorises-a-stop sentence were all master-reading text without attribution. Fixed. It found that "R-1104-3's purchase condition … is unchanged" was a statement by the filer. Removed. It found that NEEDS AMEAR 1 had a statement tail. Turned into a question. Items 10 and 11 were left; see the Process log.
- Adversary 2 found that bullet (i)'s "(a) has no optimisation step, (b) does" was master-reading text without attribution. Fixed. Its two minor findings in (ii) and (iii) were also fixed, with verbatim quotes. All pointers, all quotes, S8, and the questions-only check passed.

## S6 cross-block check
F1 (`specs/SPEC_RUBRIC.md:17`), F2 (`:30`), F3 (`:45`) and F4 (`:59`) were not touched. No code, hook, template or config changed. Only DECISIONS.md, MANIFEST.md and this report were written.

## NEEDS AMEAR
Four questions. See DECISIONS.md:828-832 (D-2026-11-05-A, NEEDS AMEAR 1–4). None are answered here.

## Files staged
None. By instruction, nothing was staged, through `git add` or otherwise. Working-tree changes: DECISIONS.md, MANIFEST.md, and this report (new, untracked).

## Result
Result: PASS (manager's assessment, not a grade). Both tasks are done. The quote is byte-identical. The pre-unit prefixes are hash-proven unchanged. Every adversarial defect is fixed, except the two out-of-scope items stated above. The last fix pass (three attribution edits) was checked by substring and cmp only. It had no third adversarial pass.
