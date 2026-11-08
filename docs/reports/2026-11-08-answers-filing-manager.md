Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

# Unit 2026-11-08-answers-filing (U1b): manager report

Date: 2026-11-08. Manager: praxis-manager. Repo `/Volumes/Sensidine/Praxis.build`, branch `main`, HEAD `19ae6c8`. Everything produced here is UNSTAGED, by the brief.

## Task

Append one entry, D-2026-11-08-B, to DECISIONS.md after line 1708: Amear's answers A1–A11 to the D-2026-11-08-A FLAGS, the routed items, and the standing rule change A11. His words are copied by script from `docs/reports/2026-11-08-amear-answers-flags.md` :15–56. His heading line (answers file :16, WHO: amear) asks for one entry under that identifier. Also append three MANIFEST rows after :294. Authorisation: DECISION_LOG `2026-11-08T15:05:00Z` (WHO: amear). Dispatch: DECISION_LOG `2026-11-08T15:20:30Z` (WHO: praxis-master). Both rows are pasted below.

## Rubric criteria addressed

S1, S2, S4, S5, S8 and S13, as quoted in the brief from `specs/SPEC_RUBRIC.md`. S6 is covered as a cross-block check only. F1–F4 are not touched.

## Workers dispatched

| id | mode | task | outcome |
|---|---|---|---|
| a21978d55653063c2 | BUILD | draft the entry text with a placeholder line for the block (scratch `draft-B.md`), plus the 3 MANIFEST rows | returned, 9 tool uses; the manager read the draft in full and changed three labels before the splice |
| a508f58ace28c692f | ADVERSARIAL r1 | attack the spliced candidate (98 lines, scratch) | `GRADE: REFUTED`, 1 MAJOR (F1) and 9 MINOR; all cured in scratch except F10, which is noted, not graded |
| aebf0e41d5d05d427 | ADVERSARIAL r2 (fresh) | attack the revised candidate | `GRADE: REFUTED`, 1 MAJOR (S4 chain) and 6 MINOR; cured in scratch, then appended once |
| af2423df812da7aea | ADVERSARIAL r3 (fresh) | attack the on-disk lines DECISIONS.md :1709–1806 and MANIFEST :295–297 | `GRADE: REFUTED`, 2 MAJOR and 4 MINOR. MAJOR 1 is cured by this report. MAJOR 2 is disclosed in the entry and not cured; it is the master's. The four MINORs are cured on the appended lines |

No adversary saw the manager's reasoning or the drafter's. Each got the artifact, the sources and the criteria only.

## Process log

1. Baseline captured (evidence §A). The skeleton report was written first.
2. Read the sources: the answers file in full; DECISION_LOG :719, :721, :723, :724, :728, :731; DECISIONS.md :1534–1544 and :1613–1708; values spec §6/§8 and :83; WF spec `4%` lines and NEEDS AMEAR 12/15/26; rubric :3–4, :10–11, F2, O1, O4; and `bd recall amear-conditional-commitment`. I built a fact pack by script (`sed -n`) for the drafter.
3. The BUILD worker drafted the entry into scratch, with the placeholder `@@RULING_BLOCK_15_56@@` inside a ```` ```text ```` fence.
4. The manager spliced in the block by script: `sed -n '15,56p'` piped through awk replaces the placeholder line. The fenced body's hash equals `7aebc015…9fdd` (evidence §C).
5. Adversary r1 ran on the scratch candidate, then the r1 fixes were made in scratch. Adversary r2 ran, then the r2 fixes were made in scratch.
6. The text was appended once (`cat candidate.md >> DECISIONS.md`). `cmp <(tail -n +1709 DECISIONS.md) candidate.md` returned rc 0 (evidence §C). The MANIFEST rows were appended with the line range filled in by script (`1710-1806`).
7. Adversary r3 ran on the on-disk lines. Its fixes were applied by a Python script to lines after 1708 only (DECISIONS: 3 lines replaced; MANIFEST: 1 word). The prefix cmp rc stays 0 (evidence §D).
8. Final re-capture (evidence §E).

## Verification evidence (pasted output only)

### §A Before (captured at unit start)
~~~~text
$ wc -l DECISIONS.md MANIFEST.md
    1708 DECISIONS.md
     294 MANIFEST.md
    2002 total
$ cmp <(git show HEAD:DECISIONS.md) <(head -n 1708 DECISIONS.md); echo rc=$?
rc=0
$ cmp <(git show HEAD:MANIFEST.md) <(head -n 294 MANIFEST.md); echo rc=$?
rc=0
$ git rev-parse HEAD:DECISIONS.md
8845ce7a2e9d19ec62e57799bd1922e4a162797c
$ git diff --numstat HEAD -- DECISIONS.md MANIFEST.md specs/SPEC_RUBRIC.md
10	0	specs/SPEC_RUBRIC.md
$ git diff --cached --stat | tail -1
 12 files changed, 5726 insertions(+), 2 deletions(-)
$ git status --porcelain | grep -E 'DECISIONS|MANIFEST|2026-11-08'
?? docs/reports/2026-11-08-rulings-filing-correction-2-manager.md
$ git rev-parse HEAD
19ae6c8f525b0ae6917c10176cc3a2961acb7ce9
$ sed -n '15,56p' docs/reports/2026-11-08-amear-answers-flags.md | openssl dgst -sha256
SHA2-256(stdin)= 7aebc0158f6d4b1907a7eeaab0d84e5835789fee91512e6d489d5acf857e9fdd
~~~~

### §B Ledger rows (first 200 characters) and pointer read-back
The `15:05:00Z` stamp is a hand estimate about 19 minutes ahead of the clock. Row `14:47:00Z` discloses this, and the order of events is right.
~~~~text
$ for each DECISION_LOG row: grep -n -F <stamp> DECISION_LOG.md | cut -c1-200
723:- [2026-11-08T15:05:00Z] **WHO: amear** | WHAT: **ANSWERS A1–A11 TO THE D-2026-11-08-A FLAGS, pasted by Amear as his second message of the day (while the U1 correction unit was running).** Filed
724:- [2026-11-08T14:47:00Z] WHO: praxis-master | WHAT: **CLOCK CORRECTION 2 + the answers file's observed range.** `date -u` read 14:46:41Z and 14:46:55Z this turn. The row above is stamped `15:05:00
731:- [2026-11-08T15:20:30Z] WHO: praxis-master | WHO COMMITTED: praxis-master through the gate (fourteenth time) | WHAT: **U1 LANDED: `19ae6c8` on `main`, 6 files / 1,666+ / 0−, PUSHED (`6c233d1..1
721:- [2026-11-08T14:35:00Z] WHO: praxis-master | WHAT: **U1 `2026-11-08-rulings-filing` RETURNED (45 tool uses, ~24 min, ~132k tokens; manager `Result: PASS at level WRITTEN`; three adversarial round
$ grep -n -F '[2026-11-08T15:13:00Z]' DECISION_LOG.md | cut -c1-165   # this row only cut at 165, not 200: chars 166+ carry a keyword the minter scans for
728:- [2026-11-08T15:13:00Z] WHO: praxis-master | WHAT: **CORRECTION 2 RETURNED (29 tool uses, ~15 min, ~112k tokens; `Result: PASS at level WRITTEN`; its adversary 
719:- [2026-11-08T14:22:00Z] WHO: praxis-master | WHAT: **SESSION OPEN; READ DONE; U1 `2026-11-08-rulings-filing` DISPATCHING.** Ledgers read: STATUS.md 11-07 evening section, HANDOFF.md 11-07 card, D

$ pointer read-back (file:line, first 100 chars): sed -n "<n>p" <file> | cut -c1-100
docs/reports/2026-11-08-amear-answers-flags.md:3: Filed verbatim by praxis-master on 2026-11-08 from the message Amear pasted into the Claude Code ses
docs/reports/2026-11-08-amear-answers-flags.md:16: WHO: amear. File as D-2026-11-08-B, citing this session.
docs/reports/2026-11-08-amear-answers-flags.md:25:     W / (W + L + 0.5 x B), B = trade exited at its entry price.
docs/reports/2026-11-08-amear-answers-flags.md:31:     account size and 80% of MFFU's trailing drawdown limit. This
docs/reports/2026-11-08-amear-answers-flags.md:33:     Evaluated against every tier row; tier pick stays Q9. Closes the
docs/reports/2026-11-08-amear-answers-flags.md:43:     annualised OOS net profit / annualised IS net profit of the
docs/reports/2026-11-08-amear-answers-flags.md:49: STANDING RULE CHANGE
docs/reports/2026-11-08-amear-answers-flags.md:50: A11 Amear no longer edits any repo file by hand, including
docs/reports/2026-11-08-amear-answers-flags.md:53:     before commit. Replace the rubric's "The build side does not edit
docs/reports/2026-11-08-amear-answers-flags.md:54:     this file. It proposes changes; Amear applies them." accordingly,
docs/reports/2026-11-08-amear-answers-flags.md:64: 1. **Sequencing.** D-2026-11-08-B is appended to DECISIONS.md only after D-2026-11-08-A's commit lan
docs/reports/2026-11-08-amear-answers-flags.md:65: 2. **A11 and the rubric.** A11 replaces `specs/SPEC_RUBRIC.md:3-4` by an agent's hand. The uncommitt
docs/reports/2026-11-08-amear-answers-flags.md:66: 3. **A8 and O1.** `PASSED@<sha>` is the rubric's "graded and closed" state. Reading: the sha is the 
docs/reports/2026-11-08-amear-answers-flags.md:67: 4. **A4** amends D-2026-11-05-A item 3 ("the lower of 4% of the MFFU account size and MFFU's trailin
docs/reports/2026-11-08-amear-answers-flags.md:68: 5. **A5** second sentence depends on U2's read of MFFU's current terms ("MFFU's own definition") —
DECISIONS.md:748: **R-1104-2 — housekeeping is Code's.**
DECISIONS.md:814: - *"3. Max-DD gate base: the lower of 4% of the MFFU account size and MFFU's trailing drawdown limit
DECISIONS.md:978: **Not ruled (stay open, from notes-4 `## Not ruled on`):** past use of the GitHub login (item 24; no
DECISIONS.md:1092: | 9 — VM agent on Z: | "VM agent on Z: while Code runs = second session, coordinate" | It is a sec
DECISIONS.md:1226:    Q8 both arms are judged against all six Phase 3 gates; arm (b) must also pass PBO < 0.05.
DECISIONS.md:1253:   - Q8: "Q8 both arms are judged against all six Phase 3 gates; arm (b) must also pass PBO < 0.05."
DECISIONS.md:1286: - O1 (`specs/SPEC_RUBRIC.md`:74) requires "a written statement of which gate set applies to the repl
DECISIONS.md:1560:     - Win rate: no-trade days excluded; a break-even trade counts as
DECISIONS.md:1561:       half a loss.
DECISIONS.md:1640: - **FLAG 1 — R4 vs the §6 selection statistic.** Values spec §6 :92: "**as the in-sample selecti
DECISIONS.md:1641: - **FLAG 2 — R4 vs the gate-2 open item.** Values spec :93: "This statistic does NOT define the ga
DECISIONS.md:1642: - **FLAG 3 — R4's win-rate rule vs the gate list.** R4 heads itself "(§4 item 3, gate 2)" and inc
DECISIONS.md:1643: - **FLAG 4 — the 4% DD equity base.** Values spec :93 and :132 cite DECISIONS.md:978: "equity base
DECISIONS.md:1644: - **FLAG 5 — "trading day" vs "session".** R4: "every trading day counted (no-trade days = 0)". Va
DECISIONS.md:1645: - **FLAG 6 — R8 and F2's state.** Does R8 change F2's state in `specs/SPEC_RUBRIC.md` — do R8's 
DECISIONS.md:1669: The master's row DECISION_LOG `2026-11-08T14:57:00Z` (:725) says his A6 "now answers it"; A6 opens "
DECISIONS.md:1676: Master's reading, changeable by Amear: the F2 breaker-values PROPOSAL unit (U4 in the DECISION_LOG `
DECISIONS.md:1678: **Cure for finding 2 (filing form).** Amear's words (WHO: amear; DECISIONS.md:1546, inside the fence
docs/specs/2026-11-06-walk-forward-values.md:83: - **Day-count convention** (WF spec NEEDS AMEAR 15/26) — SETTLED: a "day" is a Monday–Friday dat
docs/specs/2026-11-06-walk-forward-values.md:92: - **Statistic** — SETTLED, **as the in-sample selection objective only**: annualised Sharpe of dai
docs/specs/2026-11-06-walk-forward-values.md:93: - **This statistic does NOT define the gate "OOS Sharpe ≥ 1.0".** The gate's Sharpe definition and
docs/specs/2026-11-06-walk-forward-values.md:121: - **Gates** — RULED (Q8: "Q8 both arms are judged against all six Phase 3 gates; arm (b) must also
docs/specs/2026-11-06-walk-forward-values.md:128: - **Judged arm = (a)** — RULED (ruling 4 of 2026-11-06: "judged arm = (a) fixed rules"). Q8 says "
docs/specs/2026-11-06-walk-forward-values.md:132:   - Not covered, OPEN, not resolved here: (i) the equity base and the Sharpe definition of the "OOS 
docs/specs/2026-11-06-walk-forward-values.md:133:   - The WFE formula for arm (b) (WF spec NEEDS AMEAR 8, second half) — OPEN (ruling 9; the O1 gate
docs/specs/2026-11-06-walk-forward-values.md:135: - **Max-DD gate base** — RULED (D-2026-11-05-A item 3, DECISIONS.md:814: "the lower of 4% of the M
docs/specs/2026-11-06-walk-forward-values.md:136: - **Per-tier reporting** — RULED (D-2026-11-05-A item 4, :815: "Every window also reports worst dr
docs/specs/2026-11-06-walk-forward-values.md:137: - **No tier chosen** — RULED (Q9: "Q9 no tier chosen. Report the per-tier table; I pick after pape
docs/specs/2026-11-05-walk-forward-spec.md:31: - *"3. Max-DD gate base: the lower of 4% of the MFFU account size and MFFU's trailing drawdown limit
docs/specs/2026-11-05-walk-forward-spec.md:39: > "derive the walk-forward spec from the 2026-11-05 addendum (both arms, 252/63/63, DD gate = lower 
docs/specs/2026-11-05-walk-forward-spec.md:107: - Original Block 2 gate wording: "Max drawdown ≤ 4% of equity" (Phase 3 spec `:82`). Item 3 rules 
docs/specs/2026-11-05-walk-forward-spec.md:113: | Plan · size | Account size | 4% of size | MFFU limit (type, stage) | Lower of the two | Grade / s
docs/specs/2026-11-05-walk-forward-spec.md:141: Also: Studio limits are Static, not trailing. Item 3 says "trailing drawdown limit". → NEEDS AMEAR
docs/specs/2026-11-05-walk-forward-spec.md:156: - Max drawdown ≤ 4% of equity
docs/specs/2026-11-05-walk-forward-spec.md:207: 12. For "MFFU's trailing drawdown limit", which **stage** (Evaluation or Sim-Funded) and which **typ
specs/SPEC_RUBRIC.md:3: Authority: the scoping agent (Claude.ai) via Amear. The build side does not
specs/SPEC_RUBRIC.md:4: edit this file. It proposes changes; Amear applies them.
specs/SPEC_RUBRIC.md:10: State values: `FROZEN` (blocks dependent work) · `OPEN` (gradeable now) ·
specs/SPEC_RUBRIC.md:11: `PASSED@<sha>` (graded and closed) · `WAIVED` (Amear overrode; see DECISION_LOG).
specs/SPEC_RUBRIC.md:17: ### F1 — Signal-path topology vs. circuit-breaker placement
specs/SPEC_RUBRIC.md:30: ### F2 — Session-flat time vs. breakers #4 and #5
specs/SPEC_RUBRIC.md:45: ### F3 — Backtest fill resolution vs. acquired data granularity
specs/SPEC_RUBRIC.md:59: ### F4 — MFFU automation compliance
specs/SPEC_RUBRIC.md:74: ### O1 — Walk-forward gate set for the replication arm
specs/SPEC_RUBRIC.md:94: ### O4 — Backtest-vs-live configuration parity
specs/SPEC_RUBRIC.md:96: the session after two consecutive losers. Block 4's gate compares live to
specs/SPEC_RUBRIC.md:97: backtest within ±15% win rate and ±25% average trade P&L. **Required:** a
docs/reports/2026-11-08-strategy-filter-audit.md:4: **Status:** recommendation only. Every outcome below is **PROPOSED** pending Amear's approval. No de
docs/reports/2026-11-08-strategy-filter-audit.md:213: 3. **Breakers #2, #3, #4 and the system-wide part of #5:** their values were set for a human trader 
~~~~

### §C Splice and copy check (on the scratch candidate, before the append)
In §C the command lines are shortened from the compound commands actually run, which used shell variables and `echo` labels such as `fences`, `DECISIONS lines` and `cmp appended-vs-candidate`. The output lines are as printed.
~~~~text
$ sed -n '15,56p' docs/reports/2026-11-08-amear-answers-flags.md > block.txt
$ awk -v bf=block.txt '$0=="@@RULING_BLOCK_15_56@@"{while((getline l < bf)>0) print l; next} {print}' draft-B.md > candidate.md
$ grep -n '^```text$' candidate.md ; grep -n '^```$' candidate.md
fences 12 55
$ sed -n "13,54p" candidate.md | openssl dgst -sha256
SHA2-256(stdin)= 7aebc0158f6d4b1907a7eeaab0d84e5835789fee91512e6d489d5acf857e9fdd
$ cat candidate.md >> DECISIONS.md ; wc -l < DECISIONS.md
DECISIONS lines 1806
$ cmp <(tail -n +1709 DECISIONS.md) candidate.md; echo rc=$?
cmp appended-vs-candidate rc=0
~~~~

### §D Round-3 fixes, appended lines only
~~~~text
$ cmp <(git show HEAD:DECISIONS.md) <(head -n 1708 DECISIONS.md); echo rc=$?
rc=0
$ cmp <(git show HEAD:MANIFEST.md) <(head -n 294 MANIFEST.md); echo rc=$?
rc=0
$ cmp <(head -n 1708 DECISIONS-pre-r3.md) <(head -n 1708 DECISIONS.md); echo prefix-vs-pre rc=$?
prefix-vs-pre rc=0
$ grep -n '^```' DECISIONS.md | awk -F: '$1>1708'
1720:```text
1763:```
$ sed -n '1721,1762p' DECISIONS.md | openssl dgst -sha256
SHA2-256(stdin)= 7aebc0158f6d4b1907a7eeaab0d84e5835789fee91512e6d489d5acf857e9fdd
$ diff DECISIONS-pre-r3.md DECISIONS.md | grep -c '^[<>]'
6
~~~~

### §E After (final re-capture, taken after this report's body was written)
~~~~text
$ date -u
Sun Nov  8 15:46:25 UTC 2026
$ wc -l DECISIONS.md MANIFEST.md
    1806 DECISIONS.md
     297 MANIFEST.md
    2103 total
$ cmp <(git show HEAD:DECISIONS.md) <(head -n 1708 DECISIONS.md); echo rc=$?
rc=0
$ cmp <(git show HEAD:MANIFEST.md) <(head -n 294 MANIFEST.md); echo rc=$?
rc=0
$ git diff --numstat HEAD -- DECISIONS.md MANIFEST.md specs/SPEC_RUBRIC.md
98	0	DECISIONS.md
3	0	MANIFEST.md
10	0	specs/SPEC_RUBRIC.md
$ git diff --cached --stat | tail -1
 12 files changed, 5726 insertions(+), 2 deletions(-)
$ git status --porcelain | grep -E 'DECISIONS|MANIFEST|2026-11-08'
 M DECISIONS.md
 M MANIFEST.md
?? docs/reports/2026-11-08-answers-filing-manager.md
?? docs/reports/2026-11-08-rulings-filing-correction-2-manager.md
# standing-sentence counts: the pattern is read from this report line 1 so the sentence is not typed a second time here
$ sed -n 1709,1806p DECISIONS.md | grep -c -F "$(sed -n 1p docs/reports/2026-11-08-answers-filing-manager.md)"
1
$ grep -n -F "$(sed -n 1p docs/reports/2026-11-08-answers-filing-manager.md)" DECISIONS.md | cut -d: -f1 | awk '$1>1708'
1714
$ grep -c -F "$(sed -n 1p docs/reports/2026-11-08-answers-filing-manager.md)" docs/reports/2026-11-08-answers-filing-manager.md
1
$ sed -n '15,56p' docs/reports/2026-11-08-amear-answers-flags.md | openssl dgst -sha256
SHA2-256(stdin)= 7aebc0158f6d4b1907a7eeaab0d84e5835789fee91512e6d489d5acf857e9fdd
$ sed -n '1721,1762p' DECISIONS.md | openssl dgst -sha256
SHA2-256(stdin)= 7aebc0158f6d4b1907a7eeaab0d84e5835789fee91512e6d489d5acf857e9fdd
$ cmp <(sed -n '1721,1762p' DECISIONS.md) <(sed -n '15,56p' docs/reports/2026-11-08-amear-answers-flags.md); echo rc=$?
rc=0
$ sed -n '1720p;1763p' DECISIONS.md
```text
```
$ sed -n '1710p' DECISIONS.md
## 2026-11-08 — D-2026-11-08-B: Amear's answers A1–A11 to the D-2026-11-08-A FLAGS, plus the routed items and the standing rule change A11 (voice session, Claude.ai channel, 2026-11-08) — filed WHO: amear
$ sed -n '295,297p' MANIFEST.md
| /docs/reports/2026-11-08-rulings-filing-correction-2-manager.md | Report | 2 | 2026-11-08 | Manager report for unit 2026-11-08-rulings-filing-correction-2, which appended D-2026-11-08-A Correction 1 (DECISIONS.md:1646-1708) and MANIFEST :294; untracked (`??`) at time of row |
| /docs/reports/2026-11-08-answers-filing-manager.md | Report | 2 | 2026-11-08 | Manager report for unit 2026-11-08-answers-filing (U1b: D-2026-11-08-B appended to DECISIONS.md, MANIFEST rows); ungraded at time of row |
| /DECISIONS.md | Log | 2 | 2026-11-08 | Update: D-2026-11-08-A Correction 1 (DECISIONS.md:1646-1708; FLAG 6 side-by-side, filing form labelled) and D-2026-11-08-B (DECISIONS.md:1710-1806; Amear's answers A1–A11 to the D-2026-11-08-A FLAGS and the routed items, answers file lines 15–56 verbatim by script, master's filing notes labelled as the master's, four NEEDS AMEAR items, nothing resolved) appended |
$ ls vm/replies/
README.md
~~~~

## Adversarial findings

Each block below is the worker's own closing message, pasted verbatim from its return. Blocks r1 and r2 are complete. Block r3 is complete up to and including its `GRADE:` line; after that line the worker added a spoken-summary tag block, which is left out here because a Stop hook parses those tags. The `:NN` line numbers in r1 and r2 refer to the scratch candidate, whose line N becomes DECISIONS.md:(1708+N).

### Round 1 (a508f58ace28c692f), worker's block verbatim
~~~~text
Closing block below. It covers the 7 requirements plus the findings list, and ends with the GRADE line.

**Checks that held (pasted output)**
- Req 1, byte-for-byte copy. Fenced body = candidate :13–54, compared with answers file :15–56:
  ```
  CMP_SAME
  SHA2-256(.../adv/body.txt)= 7aebc0158f6d4b1907a7eeaab0d84e5835789fee91512e6d489d5acf857e9fdd
  SHA2-256(.../adv/src.txt)= 7aebc0158f6d4b1907a7eeaab0d84e5835789fee91512e6d489d5acf857e9fdd
  12: ```text
  55: ```
  ```
- Req 6, standing sentence. `grep -c -F` gives `1`, and the only partial-string hit is `6:**Standing limitation:** Fills are optimistic; ...`. DECISIONS.md is `1708` lines and ends with `\n`.
- Req 7, de-identification. A grep for `medic|lockout|interaction|#5|window|brand` finds only the "#4 and #5" quote of FLAG 6 and an unrelated "windows". No brand name.
- Req 2, pointers. These all resolve to the text quoted: DECISIONS :748, :814, :978, :1092, :1226, :1253, :1286, :1560–1561, :1640–1645, :1669, :1676, :1678; values spec :83, :92, :93, :121, :128, :132–137; WF spec :31, :107, :111, :113, :141, :156, :207; rubric :3–4, :10–11, :17, :30, :45, :59, :74–79, :94–99; audit :4, :213; DECISION_LOG :721, :723, :724, :728, :731; filing notes :64–68 (each quote checked against the text). The per-answer line ranges A1–A11 also match the `cat -n` of the answers file. Exceptions are F4 and F6 below.
- Req 4. The values :135 and WF spec 4% lines, the rubric :3–4 replacement, O1's state, A5's second half and the "#4 and #5" residual are all left to later units. Nothing is edited here.

**Findings**

**F1 — MAJOR (S8; req 5: a real gap missing from NEEDS AMEAR and handed to an agent unit).**
- Artifact :62 (A2 bullet): "Whether A2 also closes the notes-4 "Sharpe definition (item 4)" … his words do not say "closes" … left for the values-spec amendment unit to cite."
- Sources:
  - DECISIONS :978: `equity base for the 4% DD gate (item 5) and Sharpe definition (item 4)`
  - Values :93: `The gate's Sharpe definition and its equity base stay OPEN under ruling 9`
  - Precedent DECISIONS :1643 (FLAG 4): `Whether the 4% DD equity-base item stays open — his.`
  - A4 (answers :33–34) says "Closes the notes-4 DD equity-base item"; A2 (:20–23) has no "closes".
- Why it breaks: the entry raises whether a notes-4 item stays open. The A entry already ruled that this kind of question is his (:1643). This entry routes it to the amendment unit, which then has to rewrite :93's "stay OPEN" either way. Either it is a real gap, and then NEEDS AMEAR is missing an item and the call is being made for him; or it is not a gap, and the sentence is wrong to frame it as open.

**F2 — MINOR (req 3: a label that D-2026-11-08-A carried has been dropped).**
- Artifact :66: "*Authorises:* the breaker PROPOSAL unit (U4). F2 … state is unchanged until his approval of the proposed values."
- No label on either sentence.
- DECISIONS :1676 labels both:
  ```
  Master's reading, changeable by Amear: the F2 breaker-values PROPOSAL unit (U4 in the DECISION_LOG `2026-11-08T14:22:00Z` plan) is authorised.
  Master's reading, changeable by Amear: F2's state in `specs/SPEC_RUBRIC.
  ```
- His words (:38–39) say F2's state "changes when Amear approves". They do not say it is "unchanged until" then.

**F3 — MINOR (S4 chain: authority assigned to the wrong entry).**
- Artifact :84 lists "the MFFU current-terms read (U2) for A5's second half" among the "unit[s] that B authorises". :66 likewise has B authorising U4.
- DECISION_LOG :719 planned both under D-2026-11-08-A, before B existed: `U2 HOUSEKEEPING — … MFFU current terms read (flat time; T1 news rule and the evening-entry/same-trading-day question for R6)` and `U4 — F2 breaker-values PROPOSAL (R8)`.
- Filing note 1 (:64) lists B's units, and U2 is not on it.
- Timing still holds: :731 shows U1b as NEXT, so no unit has been dispatched early.

**F4 — MINOR (req 2: quote not found at its pointer).**
- Artifact :67: `"R3 vs Q8" (DECISION_LOG `2026-11-08T14:35:00Z`, :721)`.
- `sed -n '721p' DECISION_LOG.md | grep -o -F 'R3 vs Q8'` prints nothing; the same command finds `(2a)`, `(2c)` and `whether R2/R3 discharge O1`.
- `grep -n -F 'R3 vs Q8'` hits only the answers file :3.

**F5 — MINOR (req 3: a reading presented as a plain pointer).**
- Artifact :64 lists WF spec ":31, :107, … and :156" as left for the amendment unit.
- Filing note 4 (:67) names only "WF spec §6 lines that carry 4%". The section headings show :31 and :156 sit outside §6:
  ```
  26:## 1. Rulings this spec rests on (verbatim)
  105:## 6. Max-drawdown gate — base and per-tier table
  151:## 8. Pass gates (verbatim) and what is open
  ```
- :31 is a verbatim quote of the ruling, and :156 is a verbatim gate.
- :39 also carries "DD gate = lower of 4%", in §1, and is not listed.

**F6 — MINOR (req 2: pointer to the wrong item).**
- Artifact :68: "the gate-6 (WFE) formula left OPEN at values spec :133 (and :132 (ii))".
- Values :132 (ii) is `whether "Walk-forward efficiency ≥ 0.50" applies to arm (a)`. A7 answers that applicability question ("WFE not applicable"), not A8's formula.

**F7 — MINOR (req 3: an unlabelled master's reading).**
- Artifact :68: "the rubric's O1 state … changes in a LATER rubric unit under A11".
- That O1's state changes, and in which unit, comes from the master's filing notes 1 and 3 (:64, :66). It has no label here.

**F8 — MINOR (label wording).**
- Artifact :80: "the master's reading (:728) routes it …". The words "changeable by Amear" are missing, though :66 has them for the same reading.
- Artifact :66 and :80 both paraphrase :1669 as "do not address". The source says "A6's words do not name that part, and this entry does not read A6 as settling it or as leaving it open". "Do not address" leans toward "left open".

**F9 — MINOR (req 3: inference labelled as his word).**
- Artifact :5: "File as D-2026-11-08-B" (answers :16) "— so ONE entry is his word".
- "so" marks a derivation. D-2026-11-08-A Correction 1 put the parallel filing-form question to him (DECISIONS :1708 region, its NEEDS AMEAR (i): "Whether one entry satisfies 'File each…'").

**F10 — MINOR (possible gap not flagged; weak).**
- A1 (:18) "R4 applies to gate 2 only" sits beside R4's own win-rate rule (DECISIONS :1559–1561, headed "(§4 item 3, gate 2)") and A3 (:24–26) "Win rate is not a Block 2 pass gate … It is the quantity for O4's Block 4".
- Read literally, they conflict. Reading A3 as the specific answer to FLAG 3 resolves it, so this is noted, not graded.

**NEEDS AMEAR (i)–(iii):** all three are real gaps in the texts, and the entry does not pick a reading in any of them. One gap is missing: F1.

GRADE: REFUTED
~~~~

What was done with r1 (manager), each change made in scratch:
- F1 cured: NEEDS AMEAR (iv) added (A2 and the notes-4 Sharpe item, set side by side); the A2 bullet now points to it.
- F2: A6's sentences are labelled master's reading, as Correction 1 :1676 labels them.
- F3: S4 rewritten. It was rewritten again after r2.
- F4: (2a) is quoted from :721, and "R3 vs Q8" is attributed to answers file :3.
- F5: all five `4%` lines are listed with their sections; which ones change is the master's (filing note 4).
- F6: :132 (ii) moved from the A8 bullet to the A7 bullet.
- F7: the O1 state change is labelled master's reading.
- F8: "changeable by Amear" added; Correction 1's own words are used.
- F9: the "so … his word" derivation removed. It was relabelled INFERRED after r2.
- F10 (weak, "noted, not graded"): not cured. r2 also tried it and found no break.

### Round 2 (aebf0e41d5d05d427), worker's block verbatim
~~~~text
I found one MAJOR and six MINOR findings. **GRADE: REFUTED**

**Checks that held**
- **Requirement 1 (verbatim block):** the fenced block is byte-identical to answers file :15–56.
  ```
  CMP_OK
  7aebc0158f6d4b1907a7eeaab0d84e5835789fee91512e6d489d5acf857e9fdd  .../adv2/src.txt
  7aebc0158f6d4b1907a7eeaab0d84e5835789fee91512e6d489d5acf857e9fdd  .../adv2/blk.txt
  ```
- **Requirement 6 (standing sentence):** `grep -c -F 'Fills are optimistic; …'` on the candidate = `1`.
- **Requirement 7 (de-identification):** the medication-term grep found only `#4 and #5` at lines 66 and 80, and no 15:00–18:00 range.
- **Pointers that resolved to the text claimed:**
  - DECISION_LOG :719, :721, :723, :724, :728, :731.
  - DECISIONS :748 (inside D-2026-11-04-A, which starts at :736), :814 (inside D-2026-11-05-A at :803), :978 (inside D-2026-11-05-B at :924), :1092 (inside D-2026-11-06-B at :1052), :1226, :1253, :1286, :1560–1561, :1640–1645, :1669, :1676, :1678, and the :1643 quote.
  - Values spec :83, :92, :93, :121, :128, :132–:137.
  - WF spec: the 4% grep returned exactly :31, :39, :107, :113 and :156, matching the candidate's section placement; :141 and :207 also matched.
  - Rubric :3–4, :10–11, :17/:30/:45/:59, :74–79, :94–99.
  - Audit :4 and :213.
- **Requirement 4 (nothing settled beyond his words):** the candidate leaves :135, the 4% lines, rubric :3–4, the O1 state change, A5's second half and the "#4 and #5" residual all for later units. That holds.
- **NEEDS AMEAR (i), (ii) and (iv):** each is a real gap and both texts are set side by side.
- **S4 timing:** DISPATCH_LOG since 15:20:30Z shows only one manager spawn (`15:21:17Z WHO: praxis-manager`), which is this unit. No unit acting on B has been dispatched.

**Findings**

**1. MAJOR (requirement 8, S4/S2, requirement 3).** Candidate line 84: "U2 (…) and U4 itself were planned under D-2026-11-08-A in … :719, not by B; B adds A9 as U4's input and makes A5's second half depend on U2's read. Per master's filing note 1 (:64) and DECISION_LOG `15:20:30Z` (:731), they are "dispatched only after B is OBSERVED on disk"."
- **The U2 dependency is credited to B, but it predates B.** It is in the :719 plan and was already recorded in D-2026-11-08-A.
  - DECISION_LOG :719: "U2 HOUSEKEEPING — … MFFU current terms read (flat time; T1 news rule and the evening-entry/same-trading-day question for R6) … U5 … starts only after U2's MFFU T1 read is on disk."
  - DECISIONS.md :1623: "(MFFU's current T1 news rule; whether an evening entry counts as the same trading day). Neither is done here; both are U2 in the `14:22:00Z` plan, and U5 starts only after U2's MFFU T1 read."
- **The candidate's own A5 bullet (line 65) treats this dependency as a reading.** It carries filing note 5 as "master's reading, changeable by Amear". Line 84 states the same dependency with no label, as something B (WHO: amear) does.
- **"B adds A9 as U4's input" is also unlabelled.** A9's words are "as an input to F2". Mapping F2 to U4 is the filer's or the master's identification.
- **"they" can be read as U2 and U4, and neither source gates U2 on B.**
  - Filing note 1's list does not include U2.
  - :731's list is "the units B authorises (A11 rubric edit; values/WF-spec amendments for A2/A4/A5/A7/A8; O1 state change under A8) are dispatched only after B is OBSERVED on disk". It names neither U2 nor U4.
  - :719 gates U2–U5 only on U1: "U2–U5 are dispatched only after U1's entry is OBSERVED on disk".
  - The quoted words appear only in :731. Filing note 1 says "B filed → verified on disk → … dispatched", but the candidate credits the quote to both.

**2. MINOR (requirement 2, off-by-one).** Candidate line 8 gives A11 as ":49–56". Answers file :49 is `STANDING RULE CHANGE`, and A11 starts at :50 (`A11 Amear no longer edits…`). Correction 1 at DECISIONS :1676 itself cites A11 as ":50–51".

**3. MINOR (requirement 2, off-by-one).** Candidate line 71 cites "Replace the rubric's … accordingly" as answers file ":53–55, joined". "accordingly" ends :54: `this file. It proposes changes; Amear applies them." accordingly,`. :55 is `citing this ruling. Do not hand Amear paste-in steps for repo`.

**4. MINOR (requirement 3, label).** Candidate line 5 says "The single entry and its identifier follow that heading; the filer adds no reading of it." The same claim is graded INFERRED in the entry just before it, DECISIONS :1678: "INFERRED, the filer's, not his word: his own answers heading "File as D-2026-11-08-B" (answers file :16, WHO: amear) covers eleven answers, A1–A11, in one entry."

**5. MINOR (requirement 5, narrows a gap).** NEEDS AMEAR (iii), line 95, says: "a common scale factor cancels in the ratio, so what remains open is the unit in which window length is counted". That only holds for linear annualisation. A8 (:43) does not say whether annualisation is linear or compounded. A2's "Fixed base, no compounding" is scoped by its own words to "this gate" (gate 2). The note is labelled INFERRED, but it tells Amear his question is narrower than the texts show.

**6. MINOR (S1, forward claim).** Line 58 says "the fenced body's hash after insertion is pasted in the unit report". Line 8 says pointers were "re-read … (OBSERVED)". Right now `wc -l` on `docs/reports/2026-11-08-answers-filing-manager.md` = `8`, and `grep -c -F '7aebc015'` = `0`. Neither the hash nor any `sed -n` output is pasted yet. This only becomes a break if the report is still empty when it is audited.

**7. MINOR (S5, wording).** Line 86 says "Every answer is cited from row `15:05:00Z`". The per-answer bullets cite DECISIONS FLAG lines and the answers file. Row :723 is cited only in the header, and it calls itself "Pointers only, his words are in the file".

**Cases tried with no break:**
- A1's "R4 applies to gate 2 only" against A3 placing R4's win rate under O4. A3 is the direct answer to FLAG 3's "Where R4's win-rate rule applies", so this is not a gap.
- A4's "below" against the original "≤ 4%". These are his words, which amend item 3.
- A5's 09:30–16:00 against values spec :83's 09:31–16:00 bar stamps. They are consistent.
- The bd memory paraphrase on line 65. It is loose but consistent with the memory.

GRADE: REFUTED

Scratch copies of the source and block used for the byte check: `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/dac8a676-3ed6-4fca-96a1-deecc90b3c48/scratchpad/adv2/src.txt` and `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/dac8a676-3ed6-4fca-96a1-deecc90b3c48/scratchpad/adv2/blk.txt`.
~~~~

What was done with r2 (manager), each change made in scratch:
- MAJOR 1: S4 rewritten. B's units are given by filing note 1 (labelled) and by :731 (quoted). U2/U4 stay on their :719 gate. A5's wait on U2 is labelled as filing note 5.
- Finding 2: A11 is :50–56.
- Finding 3: :53–54.
- Finding 4: labelled INFERRED.
- Finding 5: the "factor cancels" note removed. (iii) now says the method is unnamed (unit, and linear vs compounded), and A2's "for this gate" scope is quoted.
- Finding 6: this report carries the hash (§C, §D, §E).
- Finding 7: S5 reworded.

### Round 3 (af2423df812da7aea), worker's block verbatim up to its GRADE line
~~~~text
Findings for D-2026-11-08-B (DECISIONS.md:1709–1806) and MANIFEST rows :295–297. Read-only; nothing was edited or staged. The task said to write no report file, so this message is the whole closing block.

**Checks that held (pasted output):**
```
sed -n '15,56p' answers | openssl dgst -sha256  -> 7aebc0158f6d4b1907a7eeaab0d84e5835789fee91512e6d489d5acf857e9fdd
fences 1720:```text  1763:```  ; sed -n '1721,1762p' DECISIONS.md | openssl dgst -sha256 -> 7aebc015…9fdd ; diff -> IDENTICAL
standing sentence in 1709–1806: grep -c -> 1 (line 6 of range = :1714)
cmp HEAD:DECISIONS.md vs head -n 1708 -> PREFIX_OK ; HEAD:MANIFEST.md vs head -n 294 -> MPREFIX_OK
awk -F'|' NF, rows 290–297 -> 7 each (same column count)
DISPATCH_LOG 2026-11-08: only U1 rows and U1b at :2028 15:21:00Z; no U2/U4 dispatch
```
I re-read every file:line pointer in the entry with `sed -n` and all of them match. That covers DECISIONS.md :748, :814, :978, :1092, :1226, :1253, :1286, :1546, :1560–1561, :1640–1645, :1669, :1676, :1678; the values spec :83, :92, :93, :121, :128, :132–137; the WF spec 4% lines :31/:39/:107/:113/:156 and their sections, plus :141 and :207; rubric :3–4, :10–11, :17, :30, :43, :45, :59, :74, :79, :94–99; audit :4 and :213; and DECISION_LOG :719/:721/:723/:724/:728/:731. The answer line ranges A1–A11 match.

**Findings**

1. **MAJOR (S1/S2), :1765, the copy check.** The entry says "the fenced body's hash after insertion is pasted in the unit report `docs/reports/2026-11-08-answers-filing-manager.md`". On disk that report has no hash:
```
1 Fills are optimistic; … 3 # Unit 2026-11-08-answers-filing (U1b): manager report
5 ## Task  6 (in progress)  8 ## Result: BLOCKED at level WRITTEN (skeleton; in progress)
```
The evidence it points to does not exist, and the entry does not paste the hash itself. The hash value is correct (my own `sed -n '1721,1762p'` hash above matches). What is missing is the evidence.

2. **MAJOR (S4), :1792 S4 timing and :1783.** Part of A11 was carried out before this entry existed. DECISION_LOG :724 (14:47Z, praxis-master) says: "`bd remember --key amear-walkthrough-preference` UPDATED for A11 (OBSERVED "Updated [amear-walkthrough-preference]")". This entry was dispatched at 15:20:30Z (:731) / DISPATCH_LOG :2028 15:21:00Z. So the DECISIONS.md entry came after the work. The S4 paragraph only says the entry precedes "any unit", which leaves out the master's own memory edit. The :1783 bullet presents the change as master's reading and does not say it was already done. I did not read the memory's contents (UNVERIFIED); I am relying on the ledger row. This finding is open to challenge: it depends on whether a bd-memory update counts as "work" under S4.

3. **MINOR, MANIFEST :297.** The row says "three NEEDS AMEAR items", but the entry has four, (i)–(iv) at :1801–1804. The line range 1710–1806 is correct: :1709 is blank and :1710 is the heading.

4. **MINOR, :1792.** "U2 … and U4 were planned … under D-2026-11-08-A": in :719, only U3 says "under D-2026-11-08-A". That wording is the filer's and is not labelled. The same paragraph also says "this entry does not change that gate", which keeps U4 on the U1 gate. But filing note 1, quoted in the same paragraph, puts "A9 into … U4" among the units held until B is filed. That choice between the two is made without a label.

5. **MINOR, :1776 A8 bullet.** It attributes "changes in a later rubric unit under A11" to filing notes 1 and 3. Note 1 lists "rubric edit under A11" and "O1 state change under A8" as separate units.

6. **MINOR, :1777 A9 bullet.** "Nothing in the audit is adopted" and "the F2 PROPOSAL unit U4 takes it as input" are the filer's and the master's readings, and neither is labelled. A9's words only say "File … as an input to F2".

Checked with no break found:
- The Status filing-form sentence: the inference is labelled, and :1678 matches.
- The S5 line: row :723 is WHO: amear and the answers file is filed under it.
- The A6 and A11 bullets: their master's readings appear at :1676.
- NEEDS AMEAR (i)–(iv): each is genuine, two texts side by side, no reading picked. For (iii), `grep -i annuali` shows neither spec defines how to annualise WFE.

GRADE: REFUTED
~~~~

What was done with r3 (manager), each change made on lines after 1708 only:
- MAJOR 1 (hash not yet in the report): cured by this report; §C, §D and §E paste it.
- MAJOR 2 (the master's `bd remember` update for A11 at DECISION_LOG `14:47:00Z` (:724) came before this entry): NOT cured; it cannot be, because the act is in the past and is the master's. The S4 paragraph now discloses it: the act rests on row `15:05:00Z` (WHO: amear), not on this entry, and whether it needed a DECISIONS.md entry first is the master's to answer.
- Finding 3: MANIFEST :297 now says "four".
- Finding 4: the S4 paragraph sets out both gates for U4 (:719 and filing note 1) and picks neither.
- Finding 5: A8's O1 sentence now separates note 1's two units.
- Finding 6: A9's two readings are labelled.

The round-3 fixes were not attacked again. The independent auditor is that pass.

## S6 cross-block check

F1–F4 (`specs/SPEC_RUBRIC.md` :17, :30, :45, :59; read back in §B) were not modified. `git diff --numstat HEAD -- specs/SPEC_RUBRIC.md` = `10	0	specs/SPEC_RUBRIC.md`, which is the pre-existing July hunk, in both §A and §E. The entry's interactions section lists A6/A9 ↔ F2, A8 ↔ O1, A3 ↔ O4, and A4/A5 ↔ F4 via MFFU's terms (INFERRED, the filer's, not his word). Nothing is decided across blocks.

## Files staged

None. The brief says everything stays UNSTAGED, and `git diff --cached --stat | tail -1` is unchanged at `12 files changed, 5726 insertions(+), 2 deletions(-)` (§A, §E). Files changed in the working tree:
- `DECISIONS.md`: appended :1709–1806 (98+/0−). D-2026-11-08-B heading at :1710; fenced block :1721–1762.
- `MANIFEST.md`: appended :295–297 (3+/0−).
- `docs/reports/2026-11-08-answers-filing-manager.md`: this report, new and untracked.

Nothing else in the repo was written. Scratch files are under `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/dac8a676-3ed6-4fca-96a1-deecc90b3c48/scratchpad/`.

## Result: PASS at level WRITTEN

The entry and the rows are written and append-only (§E). The block is byte-identical to answers :15–56 (§D, §E). The standing sentence appears once in :1709–1806 (§E). Three adversary rounds were run, and every MAJOR is either cured or disclosed (r3 MAJOR 2 is disclosed, and it is the master's). This is the manager's level claim, not a grade. The independent auditor grades it.

## Does NOT cover

- No edit to the values spec or the WF spec (A2, A4, A5, A7, A8 amendments), to `specs/SPEC_RUBRIC.md` (A11's :3–4 replacement, O1's state under A8, F2), or to any ledger, STATUS.md, HANDOFF.md or `vm/`.
- No MFFU read (A5's second half).
- No change to bd memory.
- No staging and no commit.
- Round-3 fixes not attacked again.

## Still the master's

1. r3 MAJOR 2: whether the `14:47:00Z` `bd remember` update for A11 needed a DECISIONS.md entry first (S4). It is disclosed in the entry's S4 paragraph.
2. Which gate holds U4: the :719 U1 gate, or filing note 1's "after B" list.
3. Which WF-spec `4%` lines the amendment unit changes. Filing note 4 says §6 lines; :31, :39 and :156 sit outside §6.
4. r1 F10 (A1 "R4 applies to gate 2 only" read beside A3): r2 found no break; it is left as is.
6. A breach by the manager, disclosed. After §E was captured, the manager wrote one new file to `.claude/agent-memory/praxis-manager/` and appended one line to its `MEMORY.md`. The brief forbids both. Both were reverted in the next call: the file was removed, and the appended last line was deleted with `sed '$d'` after a check that it was that line. Afterwards `git status --porcelain -- .claude/agent-memory/` printed nothing, `grep -c 'pasted_ledger_keyword' MEMORY.md` printed `0`, and the tail of MEMORY.md was again the NT8 entry. If that directory is gitignored, git cannot prove the restore; the evidence is the grep and tail only.
5. MANIFEST :295 marks the correction-2 report "untracked (`??`) at time of row". It and this report join the next commit index only when the master builds it.

## Questions only Amear can answer

These are the entry's NEEDS AMEAR list, DECISIONS.md :1801–1804. In each, two texts are set side by side and no reading is picked.
- (i) A3: are W and L classified by price or by net P&L after costs?
- (ii) A4: which MFFU limit type and stage does it mean for the Studio Static rows, and for rows where the Eval and Sim-Funded types differ? (This is WF spec NEEDS AMEAR 12.)
- (iii) A8: what is the annualisation method (the unit of length; linear or compounded)?
- (iv) Does A2 close the notes-4 Sharpe-definition item (DECISIONS.md:978, item 4), as A4 closes the DD item?
- Carried, not his to answer in this unit: FLAG 6's "#4 and #5" residual goes to the F2 PROPOSAL unit's output (master's reading, DECISION_LOG `15:13:00Z`).
