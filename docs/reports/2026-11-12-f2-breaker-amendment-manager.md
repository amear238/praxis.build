# Unit F2B — breakers #4 and #5 amended to match Rule F2-1 (manager report)

Unit: `2026-11-12-f2-breaker-amendment` (Unit F2B). Authority: DECISION_LOG.md:854, row 2026-11-12T05:29:00Z, WHO: praxis-master [E1]. Baseline `main` = `9905804` [E1]. Manager: praxis-manager. Evidence tags in square brackets point to "Verification evidence (command output)" below; every tag there is a literal command with its literal output.

## Task

Clear the remaining half of rubric F2's unblock clause ("breaker specs #4 and #5 are amended to match", `specs/SPEC_RUBRIC.md`:30–31 [E2]) by a spec amendment only: (1) DECISIONS.md entry D-2026-11-12-A, written before the spec edit; (2) an appended Amendment 1 in the Phase 3 import; (3) an S6 cross-block check, report only; (4) one adversarial worker; (5) this report; (6) MANIFEST rows. Nothing is built.

## Rubric criteria addressed

- F2 (unblock clause, `specs/SPEC_RUBRIC.md`:30–31 [E2]): supplied, not graded. F2's state is not changed (the state move is a later unit, DECISION_LOG.md:854 item (4), quoted in D-2026-11-12-A).
- S1: every claim below cites a tag with pasted output.
- S2: the nine breakers, #4 and #5 included, stay SPECIFIED ONLY — zero implemented, zero tested, zero tested under failure. The only "breaker" hits in tracked code are a comment in `_Flat1559.cs`:31 and a report string in `scripts/wf/report.py`:741; no `n8n/` directory is tracked [E11]. Nothing in this unit raises any level.
- S4: D-2026-11-12-A was on disk before the spec edit, in both the first and the final write [E20].
- S6: graded below, hit by hit, against every tracked file in `docs/specs`, `ninjascript`, `scripts` and `config` [E15]; rubric O4 and F1 named as bearings.
- S8 (read with D1/D2): no D2 item is decided. The adoption of the #4/#5 text is the master's under D1, changeable by Amear; it is not D2(c) because no account exists [E4], [E5], [E6].
- S13: the S13 sentence is the last line of this report and of D-2026-11-12-A.

## Workers dispatched

| id | mode | scope | outcome |
|---|---|---|---|
| worker1 | ADVERSARIAL | read-only except its report `docs/reports/2026-11-12-f2-breaker-amendment-worker1.md`; attack quote fidelity, S4 order, import-body integrity, de-identification, S2 level claims, S6 completeness | WORKER1_OUTCOME |

No BUILD worker: the two edits are pure doc appends composed by script from fixed source lines, and the brief named one adversarial worker only.

## Process log

1. Read the authority row, rubric F2 (:19–32), O4 (:111–116), D1/D2 (:437–447), the F2 proposal in full, D-2026-11-11-A (DECISIONS.md:2101–2175), the Phase 3 import (:1–30, :90–115, tail) and the topology doc [E1], [E2], [E6], [E14].
2. Pre-edit: both target files byte-identical to HEAD; sha256 of DECISIONS.md `df1661e0…1d43`, of the Phase 3 spec `cd02d34a…9b83` [E20].
3. Composed D-2026-11-12-A by script (Python; every quotation read from the cited file and line, substring quotations asserted present before writing). Appended it [E20, first write].
4. Composed and wrote the Phase 3 Amendment 1 by script, at first with the optional pointer line after the breaker list [E20, first write].
5. Found by grep that a pointer line after :106 shifts every later body line by two, and that other committed specs cite those lines: topology doc :24, :61, :89 and proposal :67 cite Phase 3 :107 and :109 [E18]. Decision (manager, within the brief's "may"): no pointer line. Reverted the spec to HEAD bytes, rewrote D-2026-11-12-A in the region after HEAD's line 2203 only (two sentences that described the pointer replaced, and the walk-forward pin added to its S6 paragraph; lines 1–2203 checked byte-identical to HEAD before the rewrite), then re-wrote the spec amendment without the pointer [E20, final write]. The final entry still precedes the final spec edit.
6. Verified byte fidelity of every copied line (whole-line `grep -cxF`) and that the spec's lines 1–188 are byte-identical to HEAD [E8], [E9], [E10].
7. Ran the de-identification scan on all new text (the term list is held outside the repository and is not reproduced here) [E12].
8. Appended four MANIFEST rows [E21].
9. S6 grep and grading (section below) [E15], [E16], [E17], [E18], [E19].
10. Dispatched worker1 (ADVERSARIAL); findings and fixes under "Adversarial findings".

## Decisions and findings recorded by this unit

- **Rubric citation in the proposal.** Proposal :8 cites the unblock clause as rubric `:43–44`; rubric :43–44 is F3 text; the clause is at :30–31 [E3], [E2]. Recorded in D-2026-11-12-A; the proposal is not edited.
- **Citation in the authority row.** DECISION_LOG.md:854 cites D-2026-11-11-A for "Amear has no MFFU account". D-2026-11-11-A (DECISIONS.md:2101–2175) does not contain that phrase (count 0); the statement is at `docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md`:10, committed at `9905804`, REPORTED BY the Claude.ai channel [E4]. D-2026-11-12-A cites that line instead. The consumer's Sim-only wall is at `ninjascript/PraxisSignalConsumer.cs`:39 and :98–100 [E5].
- **No adaptation of copied text.** Proposal :20, :30, :36 and :38 each appear exactly once as a whole line in the amended spec and in D-2026-11-12-A (:20 twice in DECISIONS.md, the other copy being D-2026-11-11-A's); Phase 3 HEAD :100 and :101 appear twice in the spec (the body line and the "Supersedes" quote) [E8].
- **No pointer line** (process step 5). Consequence, recorded: a reader of :100–101 alone sees the superseded text; the amendment is found only at the end of the file. Named follow-up F-6 below.
- **The amendment changes the file's hash.** The walk-forward spec :12 pins the Phase 3 import as "188 lines, sha256 cd02d34a…"; the amended file has a different sha256 and 244 lines [E18], [E9]. Any amendment breaks that pin; named follow-up F-5.

## Adversarial findings

ADVERSARIAL_FINDINGS

## S6 cross-block check

Scope: every tracked file under `docs/specs`, `ninjascript`, `scripts`, `config` at HEAD `9905804`, pattern `11:30|15:00|3:00|breaker #4|breaker #5|#4|#5|16:00|4:10|16:10|Session time gate|Afternoon session window|session time`; 250 hit lines, pasted in full at [E15] (paper-author names replaced by `[author]` in the paste, by the `sed` shown in the command). The working-tree changes to the two walk-forward files (parked work, not this unit's) touch none of these times [E16]. Edited by this check: nothing.

Grades: **agrees** (consistent with the amended #4/#5 and Rule F2-1), **conflicts** (states something the amendment contradicts or makes stale; named as a follow-up, not fixed), **unaffected** (the match is not about the session clock or the breakers: a timestamp, a fixture, a data convention).

### docs/specs/2026-11-05-phase3-build-specification.md (6 hits)

| line | grade | why |
|---|---|---|
| :11 | agrees | Status basis note (2026-11-05). Re-run: still the only code hits [E11]. |
| :15, :19 | agrees | De-identification notes. The amendment reproduces no source title; "Afternoon session window" (the importer's wording) appears in new text only in the two verbatim quotes of :101 [E12]. |
| :100, :101 | superseded by Amendment 1 | Body text kept as imported by design (DECISION_LOG.md:854 item (2)); superseded in the appended section. See F-6. |
| :109 | agrees (reading) | Fallback script "checks hardcoded thresholds (daily loss, max trades, session time)" [E17]; states no value. Read as 16:00 under the amended #4 (also proposal :67). |
| :76 (not a pattern hit) | agrees | "Session window and clock times held fixed." [E17] — states no time. |

### docs/specs/2026-11-10-live-signal-topology.md (11 hits)

| line | grade | why |
|---|---|---|
| :4 | unaffected | Match is the timestamp `13:03:00Z`. |
| :41 | **conflicts** (F-1) | Path lists "consumer-side checks #4, #5, #7, #8, #9". The amended #5 is an operator lockout and no longer a system entry block; proposal :40 says the system window check is then removed and the lockout cannot sit on the signal path [E19]. |
| :44 | agrees | #4's flatten action is an order; unchanged by the amendment. |
| :48 | **conflicts** (F-1) | "Breakers #4, #5, #8 and #9 gain a consumer-side check" — #5's part is stale. |
| :54 | **conflicts** (F-2) | "Names are exactly as the Phase 3 import lists them (…:97–105, at HEAD)" [E19]. #4 is now "Session flat gate", #5 "Session window (operator lockout)". |
| :61 | agrees in mechanism, name stale (F-2) | #4 row: entries refused after the flat time until the next session, FLATTEN at the gate time — matches the amended #4. Its dependency cell names the flat time as F2's, "PROPOSED". |
| :62 | **conflicts** (F-1) | #5 row describes the Phase 3 text "as it stands" and the proposal as "PROPOSED, not adopted" [E19]; now adopted for #4/#5. |
| :74 | **conflicts** (F-1) | Option 1's unbuilt list includes "consumer clock check for #4/#5"; the #5 part is stale. |
| :86 | **conflicts** (F-1) | B1 (a): "consumer-side checks #4, #5, #7, #8 and #9 still apply"; #5 no longer applies to a file. |
| :88 | agrees | B3: #5's KEPT half (lockout on Amear's own interaction) needs a separate mechanism (OPEN-T8). Matches amended #5. |
| :105 | agrees | OPEN-T8: how the 15:00–18:00 lockout is enforced is still open; the amendment does not decide it. |
| :112 | agrees | S6 list names rubric F2 "(the flat time and session boundary for #4/#5)" — the bearing this unit addresses. |

### docs/specs/2026-11-10-f2-session-flat-proposal.md (35 hits)

The source of the amendment. :20, :30, :36, :38 are copied (agrees, by construction [E8]). :1, :14, :16, :22, :24, :25, :28, :32, :40, :42, :48, :50, :51, :52, :53, :59–:64, :66, :67, :69: agree (they state Rule F2-1, its inputs and its S6 touches, which the amendment adopts; :40 now applies, F-1). :12, :13: unaffected (they quote the pre-amendment #4/#5 "at HEAD", as history). :5: unaffected (timestamp `13:03:00Z`). :75, :76: unaffected (OPEN-F2-1, OPEN-F2-2 stay open). :8: **conflicts** with the rubric's line numbers (cites :43–44; clause at :30–31) [E3] — recorded, not edited (F-7). :79 (OPEN-F2-5): bearing — its three parts ("Amear's approval under A6; then a DECISIONS.md entry and the amended #4/#5 text in the breaker spec.") now exist on disk (D-2026-11-11-A V2; D-2026-11-12-A; Amendment 1); closing OPEN-F2-5 is not done or graded here (F-9).

### docs/specs/2026-07-16-b2-noise-area-ruleset.md (10 hits)

| line | grade | why |
|---|---|---|
| :26, :27, :30, :64, :78 | agrees | Paper's 16:00 cash-close flat; band anchors at 16:00. |
| :8 | **conflicts** (F-3) | "PRAXIS applies it to NQ inside a 09:30–11:30 ET window" — stated as the current framing; the amended #4 removes the 11:30 cut. |
| :79, :84, :99, :105 | **conflicts, stale option** (F-3) | They name the 11:30 flat as the trader's open alternative to 16:00 ("the trader-chosen 11:30 — see D8"; T1 asks the trader to decide). Deviation B and now the amended #4 settle it at 16:00. |

### docs/specs/2026-11-06-walk-forward-values.md (18 hits) and docs/specs/2026-11-05-walk-forward-spec.md (4 hits)

| line | grade | why |
|---|---|---|
| values :65 | **conflicts, stale** (F-4) | "a Flat1559 position runs past breaker #4's 11:30 and breaker #5's 15:00). It is not resolved here." The amendment resolves that interaction (Flat1559 flats at 15:59, inside Rule F2-1). |
| values :33, :63, :64, :77, :195, :203, :205, :211, :222, :268 | agrees | Backtest session flat at 16:00, or at the early-close cut (12:00 / 12:15 / 14:03); Flat1559 at 15:59 — all no later than Rule F2-1's flat. Whether the backtest must decide on the 15:59 bar to meet "closing order … no later than 16:00:00" is OPEN-F2-1 (unchanged). |
| values :232, :233 | agrees | Weekend bars, early-close cut — data handling consistent with the early-close clause; the stamp question is OPEN-F2-3. |
| values :24, :56 | unaffected | Match is the timestamp `13:00:54Z`. |
| values :83, :160, :269; WF spec :82, :84, :210, :221 | unaffected | Day-count convention (bars 09:31–16:00) and test inventory; no breaker or flat rule. |
| WF spec :12 (not a pattern hit) | **conflicts** (F-5) | Pins the Phase 3 import by "188 lines, sha256 cd02d34a…"; the amended file no longer matches [E18]. |

### docs/specs/2026-07-15-b2-data-acquisition-spec.md (3 hits)

:80, :91 (RTH 09:30–16:00) and :82 (half-day early close 13:00 ET): agree (Rule F2-1's 16:00 flat and early-close clause).

### ninjascript/ (79 hits in four files)

- `PraxisNoiseAreaBreakout.cs` (12), `_OppBand.cs` (13), `_Flat1559.cs` (22): every hit is the 16:00 ET cash-close flat, the 16:00 prev-close anchor, the RTH template 09:30–16:00, or (Flat1559) the 15:59 flatten decision — **agrees** (Rule F2-1 governs at 16:00; earlier flats allowed, proposal :24). `_Flat1559.cs`:31 "This variant does NOT decide rubric F2 (… breakers #4/#5, FROZEN)" — agrees today (F2 is still FROZEN); it goes stale when the F2 state move lands (F-8). `_OppBand.cs`:32 "reverse or hold to 16:00" agrees.
- `PraxisLastHalfHourMomentum.cs` (32): 15:30 entry, 15:59-bar flat, 16:00 close capture — agrees (inside Rule F2-1; the strategy is retired, proposal :65). :84 ("ending 13:00") and :89 ("17:00 ET") — unaffected (data facts).
- `PraxisSignalConsumer.cs`: no pattern hit; its only session reference is `IsExitOnSessionCloseStrategy = false` at :84 [E16]. It has no ET clock check, so the amended #4's consumer-side check (topology :61) is unbuilt — consistent with SPECIFIED; no conflict.

### scripts/ (83 hits) and config/ (1 hit)

- `scripts/wf/**` (sessions.py 13, oracle/market.py 12, oracle/policy.py 5, oracle/grade.py 3, and their tests): the backtest oracle's session last bar 16:00, the NT8 early-close cuts (13:15 → 12:15, 13:00 → 12:00, 14:03), FlatEOD on the 16:00 bar after a 15:59 decision — **agrees** (backtest modelling of the same flat; OPEN-F2-1 and OPEN-F2-3 unchanged). Test fixtures carrying times (for example `test_sessions.py`:242 "15:00", `test_policy.py`:184 "XS at 11:30" — a checkpoint exit in a fixture) — **unaffected**. `test_policy.py`:183 ("A#4", "C#4") — **unaffected** (row labels, not breakers).
- `scripts/b2_stitch.py`:57 (reopen "== 18:00 ET") — agrees with #4's next-session open at 18:00. :67 and :604 and `scripts/tests/b2-stitch-selftest.py` (:276, :282, :317) — unaffected (time-zone conversion, RTH filter 09:30–16:00, fixtures).
- `config/backtest-cost-model.json`:29 — FlatEOD at minute-of-day ≥ 16:00 and "the 16:00 orders" — agrees.

### Ledgers and rubric (outside the grep scope, named because the amendment bears on them)

- DECISIONS.md:2068 (D-2026-11-10-B): "is PROPOSED, not adopted (:62)" [E17] — superseded for the #4/#5 text by D-2026-11-12-A; not edited (append-only).
- DECISIONS.md:1744–1745 (A6): "F2's state changes when Amear approves the proposed values." [E17] — not graded here; the F2 state move is a later unit.
- **Rubric O4** (`specs/SPEC_RUBRIC.md`:111–116 [E14]) — bearing. Before the amendment, a breakers-on backtest would have cut at 11:30 and blocked entries from 15:00, while the current backtests flat at 16:00. After it, #4 flattens at 16:00 and #5 does not touch system trading, so on the session clock a breakers-on and a breakers-off backtest agree for #4 and #5 (proposal :61). #2 and #3 still differ, and bind more often, since entries 11:30–16:00 are now allowed (proposal :63). O4's required statement (breakers on, off, or both, and how the Block 4 gate is satisfiable) is not written here.
- **Rubric F1** (`PASSED@b4c3291`, :81 [E14]) — bearing. F1's unblock asks that the topology document address "every one of the nine breakers by name"; two of those names change (F-2). F1 is not re-graded here; whether it needs re-grading is the master's call.
- Rubric F2's "Why frozen" text (:24–29) is not reproduced here. Proposal :69 grades it: the 11:30 cut's justification is retired by Rule F2-1.

### Follow-ups (named, not fixed)

- F-1: topology doc :41, :48, :62, :74, :86 — #5 still placed as a system entry block / consumer-side check; per proposal :40 the system window check is removed and only the operator lockout remains.
- F-2: topology doc :54, :61–62 — breaker names for #4/#5; F1 bearing.
- F-3: Noise-Area ruleset :8, :79, :84, :99, :105 — 09:30–11:30 window framing and the 11:30 option.
- F-4: walk-forward values :65 — the "not resolved here" F2 interaction is now resolved (that file carries parked uncommitted work; any edit goes through that work's unit).
- F-5: walk-forward spec :12 — the Phase 3 file's line count and sha256 pin.
- F-6: Phase 3 :100–101 carry no in-body pointer to Amendment 1 (no-pointer decision, process step 5); a later unit can re-point the line citations in the topology doc and the proposal and then add a pointer, if wanted.
- F-7: F2 proposal :8 rubric line citation.
- F-8: `_Flat1559.cs`:31 "FROZEN" when F2's state moves.
- F-9: OPEN-F2-5 (proposal :79) closure, with the F2 state move.

## Files staged

None. Nothing staged, committed or touched in git refs by this unit; the one staged path in the index is pre-existing and none of this unit's paths are staged [E13]. Working-tree changes by this unit:

- `DECISIONS.md` — appended lines 2204–2278 (D-2026-11-12-A, heading :2205); 0 lines removed [E7].
- `docs/specs/2026-11-05-phase3-build-specification.md` — appended lines 189–244 (Amendment 1); lines 1–188 byte-identical to HEAD; 0 lines removed [E9], [E10].
- `MANIFEST.md` — four rows appended at :434–437; the other eight added rows in its diff against HEAD were in the working copy before this unit (diff against the pre-unit copy: 4 added, 0 removed) [E21].
- `docs/reports/2026-11-12-f2-breaker-amendment-manager.md` (this file, new); `docs/reports/2026-11-12-f2-breaker-amendment-worker1.md` (worker1, new).

Not touched (mtimes before this unit, or unchanged against HEAD): the rubric, the F2 proposal, the topology doc, `ninjascript/`, `config/`, `.claude/settings.json`, `scripts/dispatch-log-writeahead.sh`, the two walk-forward files [E13].

## Verification evidence (command output)

#### [E1]

```text
$ git rev-parse --short HEAD; git show HEAD:DECISION_LOG.md | wc -l; wc -l < DECISION_LOG.md; grep -n '2026-11-12T05:29:00Z' DECISION_LOG.md | cut -c1-120
9905804
     851
     854
854:- [2026-11-12T05:29:00Z] WHO: praxis-master | WHAT: **Unit F2B dispatched: breaker #4/#5 amendment to match Rule F2-
```

#### [E2]

```text
$ sed -n '19,24p;30,32p' specs/SPEC_RUBRIC.md
### F2 — Session-flat time vs. breakers #4 and #5
**Criterion.** One governing rule, written down, resolving: breaker #4 closes
positions at 11:30 ET; breaker #5 disables everything 15:00–18:00 ET;
Deviation B flattens at 16:00 ET. State what happens to an open position at
15:00.
**Why frozen.** The plan itself carried the contradiction — the strategy
**Unblocks when.** A DECISIONS.md entry names the governing rule and the
15:00 disposition, and breaker specs #4 and #5 are amended to match.
**Blocks.** Block 3. Block 4 paper trading.
```

#### [E3]

```text
$ sed -n 8p docs/specs/2026-11-10-f2-session-flat-proposal.md | grep -o '(`specs/SPEC_RUBRIC.md`:43–44)'; sed -n 43,44p specs/SPEC_RUBRIC.md
(`specs/SPEC_RUBRIC.md`:43–44)
optimism is invisible in the output.
**Unblocks when.** The assumption is committed and the backtest report carries
```

#### [E4]

```text
$ grep -n 'The amended #4/#5 text does not exist' DECISIONS.md | cut -c1-6; grep -n '(f) the proposed replacement text for breakers #4 and #5 (proposal :36, :38).' DECISIONS.md | cut -c1-6; sed -n 2101,2175p DECISIONS.md | grep -c 'no MFFU account'; sed -n 2101p DECISIONS.md | cut -c1-40; sed -n 2176p DECISIONS.md | cut -c1-40; git show HEAD:docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md | sed -n 10p
2108:*
2249:*
2116:E
2249:*
0
## 2026-11-11 — D-2026-11-11-A: Amear's 
## 2026-11-11 — D-2026-11-11-B: VM hando
- Amear has no MFFU account. The email was sent as a pre-purchase question to MFFU support, not from a dashboard.
```

#### [E5]

```text
$ sed -n '39p;98,100p' ninjascript/PraxisSignalConsumer.cs; git diff --quiet HEAD -- ninjascript/PraxisSignalConsumer.cs && echo consumer-unchanged-vs-HEAD
// HARD SCOPE WALL: refuses to run unless the attached account name starts with "Sim"
				accountIsSim = Account != null
					&& !string.IsNullOrEmpty(Account.Name)
					&& Account.Name.StartsWith(RequiredAccountPrefix, StringComparison.OrdinalIgnoreCase);
consumer-unchanged-vs-HEAD
```

#### [E6]

```text
$ sed -n 443,447p specs/SPEC_RUBRIC.md
D2  Only four things stop and wait for Amear's word: (a) spending
    money; (b) switching live trading on, or any order path to a
    funded account; (c) changing circuit-breaker values while real
    money is at stake; (d) installing keys, credentials or agent
    permissions. Everything else is D1.
```

#### [E7]

```text
$ grep -n '^## 2026-11-12 — D-2026-11-12-A' DECISIONS.md; wc -l < DECISIONS.md; git show HEAD:DECISIONS.md | wc -l; git diff --stat HEAD -- DECISIONS.md; git diff HEAD -- DECISIONS.md | grep -c '^-[^-]'
2205:## 2026-11-12 — D-2026-11-12-A: breakers #4 and #5 amended to match Rule F2-1 (rubric F2; master under D-2026-11-08-D D1)
    2278
    2203
 DECISIONS.md | 75 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 75 insertions(+)
0
```

#### [E8]

```text
$ P=docs/specs/2026-11-10-f2-session-flat-proposal.md; S=docs/specs/2026-11-05-phase3-build-specification.md; for n in 20 30 36 38; do L=$(sed -n ${n}p $P); printf 'proposal:%s spec=%s decisions=%s\n' $n $(grep -cxF -- "$L" $S) $(grep -cxF -- "$L" DECISIONS.md); done; git show HEAD:$S > /tmp/f2b/p3-head.md; for n in 100 101; do L=$(sed -n ${n}p /tmp/f2b/p3-head.md); printf 'HEAD-spec:%s spec=%s decisions=%s\n' $n $(grep -cxF -- "$L" $S) $(grep -cxF -- "$L" DECISIONS.md); done
proposal:20 spec=1 decisions=2
proposal:30 spec=1 decisions=1
proposal:36 spec=1 decisions=1
proposal:38 spec=1 decisions=1
HEAD-spec:100 spec=2 decisions=1
HEAD-spec:101 spec=2 decisions=1
```

#### [E9]

```text
$ S=docs/specs/2026-11-05-phase3-build-specification.md; git show HEAD:$S | wc -l; wc -l < $S; head -n 188 $S | cmp - /tmp/f2b/p3-head.md && echo LINES-1-188-IDENTICAL-TO-HEAD; git diff HEAD -U0 -- $S | grep '^@@'; git diff --stat HEAD -- $S; git diff HEAD -- $S | grep -c '^-[^-]'
     188
     244
LINES-1-188-IDENTICAL-TO-HEAD
@@ -188,0 +189,56 @@ What questions do you have before we close this session’s scope?
 .../specs/2026-11-05-phase3-build-specification.md | 56 ++++++++++++++++++++++
 1 file changed, 56 insertions(+)
0
```

#### [E10]

```text
$ git diff HEAD -- docs/specs/2026-11-05-phase3-build-specification.md
diff --git a/docs/specs/2026-11-05-phase3-build-specification.md b/docs/specs/2026-11-05-phase3-build-specification.md
index 0f2c33d..41a67ec 100644
--- a/docs/specs/2026-11-05-phase3-build-specification.md
+++ b/docs/specs/2026-11-05-phase3-build-specification.md
@@ -186,3 +186,59 @@ The Praxis coaching integration. The EQS scoring, debrief automation, and behavi
 One strategy. One instrument. One build path. Prove it works. Then expand.
 
 What questions do you have before we close this session’s scope?
+
+## Amendment 1 — 2026-11-12 — breakers #4 and #5 (Rule F2-1; D-2026-11-12-A)
+
+> ***Added 2026-11-12; not part of the source document.*** This section amends the imported breaker list. It is not part of the import and is not the source author's text; the import notes at the top of this file describe the imported body only.
+
+**Authority.** `DECISIONS.md` entry D-2026-11-12-A (DECISIONS.md:2205), decided by master under D-2026-11-08-D D1, changeable by Amear; DECISION_LOG row 2026-11-12T05:29:00Z (WHO: praxis-master). Rule F2-1 was approved by Amear in the words of a summary (D-2026-11-11-A, V2, DECISIONS.md:2108); the #4/#5 text below is the master's adoption of the F2 proposal's replacement text (`docs/specs/2026-11-10-f2-session-flat-proposal.md`:36, :38), not Amear's words.
+
+**Level.** Unchanged: the nine breakers, #4 and #5 included, are SPECIFIED ONLY — zero implemented, zero tested, zero tested under failure. This amendment changes specified text, nothing else.
+
+**How the text was carried.** Each quoted line below is copied by script, byte-identical to the cited line, including the `> ` marker at the start of the proposal's lines :36 and :38. No adaptation was made. The imported body is not rewritten: lines :100 and :101 above stay as imported, no line of the body is changed and no pointer line is added, so the body's line numbers stay as other documents cite them.
+
+### Governing rule (Rule F2-1)
+
+Copied by script from `docs/specs/2026-11-10-f2-session-flat-proposal.md`:20:
+
+```text
+**Rule F2-1. Deviation B's 16:00 ET session flat governs. The closing order for every open system position is submitted no later than 16:00:00 ET (or no later than the exchange's early close on an early-close day), and the position must be confirmed flat before MFFU's 4:10 PM ET auto-close. The system opens no new position from that flat time until 18:00 ET, when the next session begins.**
+```
+
+### Breaker #4 — amended
+
+Amended text, copied by script from the proposal :36:
+
+> 4. Session flat gate — clock reaches 16:00:00 ET, or the exchange's early close on an early-close day if earlier → cancel working entry orders, send market orders closing all system positions, confirm flat before 4:10 PM ET (alert if not), and refuse new system entries until the next session opens at 18:00 ET.
+
+Supersedes the imported line :100, quoted verbatim:
+
+```text
+4. Session time gate — clock hits 11:30 ET → close positions, disable until next session
+```
+
+### Breaker #5 — amended
+
+Amended text, copied by script from the proposal :38:
+
+> 5. Session window (operator lockout) — clock is in 3:00–6:00 PM ET → lock out manual order entry and manual changes to the system by the operator. The system's own trading is not disabled by this breaker; the system's no-entry period 16:00–18:00 ET is enforced by breaker #4.
+
+Supersedes the imported line :101, quoted verbatim:
+
+```text
+5. Afternoon session window — clock enters 3:00–6:00 PM ET → disable everything
+```
+
+De-identification (import note, top of this file) is unchanged: the amended name "Session window (operator lockout)" is the F2 proposal's wording; the source document's title for breaker #5 is not reproduced.
+
+### What happens to an open position at 15:00
+
+Copied by script from the proposal :30:
+
+```text
+**On a full trading day, at 15:00 ET an open system position stays open.** Nothing closes it at 15:00. (On an early-close day whose close is at or before 15:00, Rule F2-1 has already flattened it and no system position is open at 15:00.) It is managed by its own strategy's exits (for the Noise-Area: the band / VWAP trailing stop and reverse rule) and by the always-on breakers #1, #6 and #7, and its closing order is sent no later than 16:00:00 ET by Rule F2-1 (the strategy's own flat, backed by breaker #4), flat before 16:10 ET. New system entries between 15:00 and 16:00 are allowed under Rule F2-1, subject to breakers #1, #2, #3, #6, #7, #8 and #9. Between 15:00 and 18:00 ET Amear's own manual interaction is locked out (R8 KEEP, breaker #5 below).
+```
+
+### Not changed by this amendment
+
+Breakers #1, #2, #3, #6, #7, #8 and #9 and their values; the Block 3 state management, fallback script and milestone text; Blocks 1, 2, 4 and 5. Where #4 and #5 sit on the live path is in `docs/specs/2026-11-10-live-signal-topology.md`, section 3, which this amendment does not edit.
```

#### [E11]

```text
$ git grep -n -i -E 'breaker|circuit' HEAD -- '*.cs' '*.py' '*.js' '*.ts' '*.json' '*.sh' '*.ps1' | cut -c1-160; git ls-files n8n | wc -l; sed -n 11p docs/specs/2026-11-05-phase3-build-specification.md | cut -c1-200
HEAD:ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:31:// This variant does NOT decide rubric F2 (session-flat time vs breakers #4/#5, FROZEN). The
HEAD:scripts/wf/report.py:741:    L.append("PROVISIONAL. This Standard-resolution, breaker-less walk-forward gives a provisional "
       0
> **STATUS — the nine circuit breakers below are SPECIFIED ONLY.** As of 2026-11-05: **zero implemented, zero tested, zero tested under failure.** Specified ≠ implemented ≠ tested ≠ tested under failu
```

#### [E12]

```text
$ { sed -n 2204,2278p DECISIONS.md; git diff HEAD -- docs/specs/2026-11-05-phase3-build-specification.md | grep '^+'; } > /tmp/f2b/newtext.txt; wc -l < /tmp/f2b/newtext.txt; grep -ciEf /tmp/f2b/deid-terms.txt /tmp/f2b/newtext.txt; grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' /tmp/f2b/newtext.txt; grep -oE '\b[0-9]{1,3}(\.[0-9]{1,3}){3}\b' /tmp/f2b/newtext.txt | sort -u | wc -l; grep -c -F 'Afternoon session window' /tmp/f2b/newtext.txt
     132
0
0
       0
2
```

#### [E13]

```text
$ git status --short -- DECISIONS.md MANIFEST.md docs/specs specs ninjascript scripts config .claude; git diff --cached --name-only -- DECISIONS.md MANIFEST.md docs/specs docs/reports/2026-11-12-f2-breaker-amendment-manager.md docs/reports/2026-11-12-f2-breaker-amendment-worker1.md | wc -l; git diff --cached --name-only | wc -l; stat -f '%N mtime=%Sm' -t '%Y-%m-%dT%H:%M:%S%z' .claude/settings.json scripts/dispatch-log-writeahead.sh docs/specs/2026-11-05-walk-forward-spec.md docs/specs/2026-11-06-walk-forward-values.md docs/specs/2026-11-10-f2-session-flat-proposal.md docs/specs/2026-11-10-live-signal-topology.md specs/SPEC_RUBRIC.md; git diff --quiet HEAD -- specs docs/specs/2026-11-10-f2-session-flat-proposal.md docs/specs/2026-11-10-live-signal-topology.md ninjascript config && echo rubric-proposal-topology-ninjascript-config-unchanged-vs-HEAD
 M .claude/settings.json
 M DECISIONS.md
 M MANIFEST.md
 M docs/specs/2026-11-05-phase3-build-specification.md
 M docs/specs/2026-11-05-walk-forward-spec.md
 M docs/specs/2026-11-06-walk-forward-values.md
 M scripts/dispatch-log-writeahead.sh
?? scripts/dispatch-log-close.sh
?? scripts/tests/test-dispatch-log-close.sh
       0
       1
.claude/settings.json mtime=2026-11-05T19:33:46-0500
scripts/dispatch-log-writeahead.sh mtime=2026-07-28T12:46:11-0400
docs/specs/2026-11-05-walk-forward-spec.md mtime=2026-11-08T12:09:06-0500
docs/specs/2026-11-06-walk-forward-values.md mtime=2026-11-08T12:19:05-0500
docs/specs/2026-11-10-f2-session-flat-proposal.md mtime=2026-11-10T08:25:16-0500
docs/specs/2026-11-10-live-signal-topology.md mtime=2026-11-10T08:25:41-0500
specs/SPEC_RUBRIC.md mtime=2026-11-10T08:36:33-0500
rubric-proposal-topology-ninjascript-config-unchanged-vs-HEAD
```

#### [E14]

```text
$ sed -n 111,116p specs/SPEC_RUBRIC.md; sed -n 81p specs/SPEC_RUBRIC.md
### O4 — Backtest-vs-live configuration parity
Deviation C permits reverse-and-re-enter. Breakers #2 and #3 cap trades and end
the session after two consecutive losers. Block 4's gate compares live to
backtest within ±15% win rate and ±25% average trade P&L. **Required:** a
written statement of whether the Block 2 backtest runs with breakers applied,
without them, or both — and how the Block 4 gate is satisfiable if they differ.
**State:** PASSED@b4c3291.
```

#### [E15]

```text
$ git grep -n -E '11:30|15:00|3:00|breaker #4|breaker #5|#4|#5|16:00|4:10|16:10|Session time gate|Afternoon session window|session time' HEAD -- docs/specs ninjascript scripts config | sed -E -f /tmp/f2br/author-redact.sed | cut -c1-220 | wc -l; git grep -n -E '11:30|15:00|3:00|breaker #4|breaker #5|#4|#5|16:00|4:10|16:10|Session time gate|Afternoon session window|session time' HEAD -- docs/specs ninjascript scripts config | sed -E -f /tmp/f2br/author-redact.sed | cut -c1-220
     250
HEAD:config/backtest-cost-model.json:29:    "fill_resolution_note": "NT8 Strategy Analyzer 'Order fill resolution' = Standard on 1-minute bars (no secondary series). Every strategy order is a managed Enter*/Exit* call wi
HEAD:docs/specs/2026-07-15-b2-data-acquisition-spec.md:80:| **RTH** | 09:30–16:00 | **390** bars/day (391 boundary-inclusive) | Median RTH day == 390 ± a few (holidays/half-days excluded) |
HEAD:docs/specs/2026-07-15-b2-data-acquisition-spec.md:82:| **Half-days** | early close 13:00 ET (e.g. day after Thanksgiving) | RTH ~210 | Flag as expected, not a gap |
HEAD:docs/specs/2026-07-15-b2-data-acquisition-spec.md:91:- [ ] RTH filter reproduces 09:30–16:00 ET exactly and yields the 390-bar median.
HEAD:docs/specs/2026-07-16-b2-noise-area-ruleset.md:8:> **Scope note.** The paper studies **SPY** (the ETF), NOT NQ futures, and trades **all day** (every half-hour, flat at the 16:00 cash close). PRAXIS applies it to **
HEAD:docs/specs/2026-07-16-b2-noise-area-ruleset.md:26:`UpperBound = max(Open_{t,9:30}, Close_{t-1,16:00}) · (1 + σ)`
HEAD:docs/specs/2026-07-16-b2-noise-area-ruleset.md:27:`LowerBound = min(Open_{t,9:30}, Close_{t-1,16:00}) · (1 − σ)`
HEAD:docs/specs/2026-07-16-b2-noise-area-ruleset.md:30:- **Clock/time anchor:** session Open = 09:30 ET; σ is indexed by *minute-of-day* elapsed from the open. Bands **widen through the day** (Fig. 1, p. 8), peaking at 1
HEAD:docs/specs/2026-07-16-b2-noise-area-ruleset.md:64:- **Session flat:** **all positions closed at the market Close = 16:00 ET** (cash close), never held overnight (Fig. 2 caption p. 9; Fig. 4 p. 12). The paper has **n
HEAD:docs/specs/2026-07-16-b2-noise-area-ruleset.md:78:| D7 | Session flat | **16:00 ET cash close** (p. 9,12) | RTF: "flat at 16:00 cash close" | ✅ RTF correct |
HEAD:docs/specs/2026-07-16-b2-noise-area-ruleset.md:79:| D8 | Flat time | **16:00** — no 11:30 stop in paper | b2-q1 report notes a **"flat-by-11:30-ET baseline"** | ❌ **CONFLICT** — 11:30 is a **PRAXIS window choice** (
HEAD:docs/specs/2026-07-16-b2-noise-area-ruleset.md:84:**Net:** The RTF prose is a faithful summary of the paper on band/gap/sizing/16:00-flat, but three PRAXIS framings are **NOT paper-derived and need trader decisions*
HEAD:docs/specs/2026-07-16-b2-noise-area-ruleset.md:99:Other implementation facts to hard-code (not optimize): checkpoints at `HH:00`/`HH:30`; `ref = max/min(Open_{9:30}, PrevClose)`; VWAP anchored at 09:30, market-hours
HEAD:docs/specs/2026-07-16-b2-noise-area-ruleset.md:105:- **T1 (highest priority): session-flat time — 16:00 (paper) vs 11:30 (PRAXIS window).** The paper's entire performance record is full-day-to-16:00. A 09:30–11:30 N
HEAD:docs/specs/2026-11-05-phase3-build-specification.md:11:> **STATUS — the nine circuit breakers below are SPECIFIED ONLY.** As of 2026-11-05: **zero implemented, zero tested, zero tested under failure.** Specified ≠ i
HEAD:docs/specs/2026-11-05-phase3-build-specification.md:15:> **De-identification.** Circuit breaker #5 is carried here as a session-window constraint. The source document's title for that breaker is **not** reproduced i
HEAD:docs/specs/2026-11-05-phase3-build-specification.md:19:> **Source:** `Redemtion/Intitialization-April 2026/Phase 3 build specification.rtf` [local-only — not in this repo by design]. Extracted 2026-11-05 with `textu
HEAD:docs/specs/2026-11-05-phase3-build-specification.md:100:4. Session time gate — clock hits 11:30 ET → close positions, disable until next session
HEAD:docs/specs/2026-11-05-phase3-build-specification.md:101:5. Afternoon session window — clock enters 3:00–6:00 PM ET → disable everything
HEAD:docs/specs/2026-11-05-phase3-build-specification.md:109:The deterministic fallback script. A standalone Python script that runs independently of n8n. It polls the broker API directly, checks hardcoded thresholds (da
HEAD:docs/specs/2026-11-05-walk-forward-spec.md:82:- **Day-count convention used here: one "day" = one trading session present in the data file, counted as a Monday–Friday calendar date that has at least one bar stamped 
HEAD:docs/specs/2026-11-05-walk-forward-spec.md:84:  - whole file: 1,494 dates with a bar in 09:31–16:00. Of these, **141 are Saturday or Sunday dates** (44 Saturdays, 97 Sundays), carrying 201 bars stamped 09:31–16:00; 
HEAD:docs/specs/2026-11-05-walk-forward-spec.md:210:15. What **day-count convention** defines the days in "252-day in-sample / 63-day out-of-sample / 63-day step" (item 2, `DECISIONS.md:813`): Monday–Friday dates in the 
HEAD:docs/specs/2026-11-05-walk-forward-spec.md:221:26. **Weekend-dated bars and holidays:** the file has 141 Saturday/Sunday dates carrying 201 bars stamped 09:31–16:00 (§4, OBSERVED). Are those bars excluded (this spec
HEAD:docs/specs/2026-11-06-walk-forward-values.md:24:- **The master's Q3 settlement** (D-2026-11-07-A, paragraph "**Master's decision under delegation (R-1104-2), not Amear's word.**", DECISIONS.md:1262; source DECISION_
HEAD:docs/specs/2026-11-06-walk-forward-values.md:33:- Exits: "(a) opposite band; (b) `max(VWAP, band)`" (`:49`); flat at 16:00 ET (`:64`).
HEAD:docs/specs/2026-11-06-walk-forward-values.md:56:- Values — SETTLED: **m ∈ {1.5, 2.25, 3.0} × ATR(14)**. This is the master's decision in D-2026-11-07-A, paragraph "**Master's decision under delegation (R-1104-2), no
HEAD:docs/specs/2026-11-06-walk-forward-values.md:63:- **BandOrVWAP** — OBSERVED (code): the base file's logic: at HH:00/HH:30 checkpoints, a long exits when `Close <= max(UpperBound, VWAP)`, a short when `Close >= min(L
HEAD:docs/specs/2026-11-06-walk-forward-values.md:64:- **OppBand** — RULED (Q4: "Q4 yes, OppBand = the paper's opposite band, as in _OppBand.cs."): the 7zq-corrected opposite band (paper Table 1): long exits at `LowerBou
HEAD:docs/specs/2026-11-06-walk-forward-values.md:65:- **Flat1559** — RULED (Q5: "Q5 yes, Flat1559 = BandOrVWAP exits, flatten on the 15:59 bar, as in _Flat1559.cs."): BandOrVWAP exits, with the flatten decided on the cl
HEAD:docs/specs/2026-11-06-walk-forward-values.md:77:- **Precedence** — SETTLED: on every bar, (1) the session flat, (2) the stop, (3) the checkpoint exits and entries. The session flat is the session's last bar — 16:00,
HEAD:docs/specs/2026-11-06-walk-forward-values.md:83:- **Day-count convention** (WF spec NEEDS AMEAR 15/26) — SETTLED: a "day" is a Monday–Friday date in the data file with at least one bar stamped 09:31:00–16:00:00, ins
HEAD:docs/specs/2026-11-06-walk-forward-values.md:160:- **Acceptance tests for the code unit, T1–T13** — SETTLED (R-1104-2, delegated by Q10; made by this unit on the master's dispatch and recorded in D-2026-11-07-B; not
HEAD:docs/specs/2026-11-06-walk-forward-values.md:195:  - T8 (stop exits against the oracle; T6 checks only the values the strategy prints, not where it exits). Runs: every stop-on acceptance run and the 81. Stop exits c
HEAD:docs/specs/2026-11-06-walk-forward-values.md:203:  - T12 (ExitPolicy under the stop, the test whose absence parked version 1). Runs: T12a = T4's run (14, 1.0, 1.5, BandOrVWAP), T12b = T5d's run (14, 1.0, 1.5, OppBan
HEAD:docs/specs/2026-11-06-walk-forward-values.md:205:    - (ii) Names. An `XL` closes a long and an `XS` a short. In T12a and T12b every exit is `XL`, `XS`, `XStop` or `Exit on session close`, and none is `FlatEOD`. In 
HEAD:docs/specs/2026-11-06-walk-forward-values.md:211:    - (iii)–(vi) also run over every other stop-on acceptance run and the 81, at each run's own values. **A build that applies `ExitPolicy` only when `StopAtrMult == 
HEAD:docs/specs/2026-11-06-walk-forward-values.md:222:| ExitPolicy | T5(ii) (T5d = T4, whatever the fixed policy); T12(i) unconditionally; T12(ii) (Flat1559's `FlatEOD` vs the 16:00 `Exit on session close`); T12(iii) on 
HEAD:docs/specs/2026-11-06-walk-forward-values.md:232:- (b) **Weekend-dated bars.** The data file has weekend-dated bars inside 09:31–16:00: 141 dates, first 2021-03-14 (OBSERVED, `docs/reports/2026-11-07-arm-b-code-mana
HEAD:docs/specs/2026-11-06-walk-forward-values.md:233:- (c) **Early-close cut.** The oracle must cut early-close sessions where NT8 cuts them (12:00 / 12:15 / 14:03; results report `:133`, `:149-154`, as the code report 
HEAD:docs/specs/2026-11-06-walk-forward-values.md:268:| 9 | Precedence (incl. T8's bar order) | Session flat (last bar 16:00 or 12:00 / 12:15 / 14:03; under Flat1559 also 15:59), then stop, then checkpoint exits/entries 
HEAD:docs/specs/2026-11-06-walk-forward-values.md:269:| 10 | Day-count convention (WF NA 15/26) | Mon–Fri file dates with a 09:31–16:00 bar; weekend-dated bars excluded | An exchange session calendar | §5 |
HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md:1:# F2 session-flat proposal: one governing rule for breakers #4, #5 and Deviation B
HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md:5:Unit: 2026-11-10-f1-f2-proposal (authorisation: DECISION_LOG.md row 2026-11-10T13:03:00Z, praxis-master, items (2) and (3)). Bead context: `Praxis_build-ax4`.
HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md:8:This file is a proposal only. It writes no DECISIONS.md entry, edits no breaker spec, and changes no rubric state. F2 unblocks when "A DECISIONS.md entry names the
HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md:12:- Breaker #4, Session time gate: "clock hits 11:30 ET → close positions, disable until next session" (Phase 3 import :100, at HEAD) [E1].
HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md:13:- Breaker #5, Afternoon session window: "clock enters 3:00–6:00 PM ET → disable everything" (Phase 3 import :101) [E1].
HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md:14:- Deviation B: session-flat = 16:00 ET cash close (DECISION_LOG 2026-07-16T19:29Z item (1); `ninjascript/PraxisNoiseAreaBreakout.cs`:188–191) [E3], [E7].
HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md:16:A Deviation B position runs past 11:30 (against #4) and through 15:00 (against #5) [E16].
HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md:20:**Rule F2-1. Deviation B's 16:00 ET session flat governs. The closing order for every open system position is submitted no later than 16:00:00 ET (or no later tha
HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md:22:That is the one rule. Breakers #4 and #5 are amended to enforce it (section 4); they do not compete with it.
HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md:24:- Strategies may flat earlier than 16:00 by their own rules (for example arm (b)'s Flat1559 exit policy). No system position may have its closing order sent later
HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md:25:- "Session" means the MFFU trading day, 18:00 ET → 16:10 ET (R6 step 1, `bf6fcc7`, MFFU capture trading-day.txt:10, :12; adopted for R6 as A5, R6 design :118) [E1
HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md:28:## 3. What happens to an open position at 15:00
HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md:30:**On a full trading day, at 15:00 ET an open system position stays open.** Nothing closes it at 15:00. (On an early-close day whose close is at or before 15:00, R
HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md:32:## 4. Proposed replacement text for breakers #4 and #5
HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md:36:> 4. Session flat gate — clock reaches 16:00:00 ET, or the exchange's early close on an early-close day if earlier → cancel working entry orders, send market orde
HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md:38:> 5. Session window (operator lockout) — clock is in 3:00–6:00 PM ET → lock out manual order entry and manual changes to the system by the operator. The system's 
HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md:40:Placement of both on the live path is in `docs/specs/2026-11-10-live-signal-topology.md`, section 3. That table places #5 as the Phase 3 text stands (a system ent
HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md:42:How the rule maps to R8 (DECISIONS.md:1583–1589): R8 opens "F2 unfreezes." and says "#4 flat at 11:30" and "#5 as a disable of the system's own trading 15:00–18:0
HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md:48:| G11 (`docs/reports/2026-11-09-d11-sweep-manager.md`:63; FLAG 6 at DECISIONS.md:1645) | Do R8's words on #4 and #5 name F2's governing rule and 15:00 disposition
HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md:50:| H02 (same report :99; `bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md`:111) | Does #4's "next session" start at 18:00? | **Proposed: yes.** Th
HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md:51:| A9 (DECISIONS.md:1751, :1777) | The 2026-11-08 strategy filter audit is an input to F2. | Taken as input. Its finding C9 (audit :94) is that #4's 11:30 flat and
HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md:52:| MFFU flat time | MFFU auto-closes at 4:10 PM ET (R6 step 1, `bf6fcc7`). | Rule F2-1's 16:00 is 10 minutes inside it. MFFU also warns about orders after 4:10 PM 
HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md:53:| Breaker #1 value | No numeric value exists anywhere (`docs/reports/2026-11-09-d6-drawdown-check-manager.md`:39, :65) [E20]. | Rule F2-1 does not depend on it. S
HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md:59:| Block 2 backtest session window | R1 "RTH = 09:30–16:00 ET" (DECISIONS.md:1551) agrees with Rule F2-1 [E21]. `PraxisNoiseAreaBreakout.cs` has an explicit 16:00 
HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md:60:| Walk-forward arm (b) exit policy Flat1559 | Allowed: an earlier flat than 16:00. (`git show HEAD:docs/specs/2026-11-05-walk-forward-spec.md` is the authority; p
HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md:61:| Block 4 parity gate (rubric O4, `specs/SPEC_RUBRIC.md`:108–113) | Rule F2-1 removes the 11:30 cut and the 15:00 system disable, so a breakers-on backtest and th
HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md:62:| Deviation B | Becomes the governing rule (no change to its 16:00). |
HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md:63:| Deviation C, breakers #2 and #3 | Allowing entries 11:30–16:00 gives the Noise-Area more decision points per session (it acts at HH:00 / HH:30; header and `Desc
HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md:64:| R6 evening-entry strategy (Pre-Announcement Drift) | Entries at 18:05 fall after the 18:00 next-session start, so they are allowed. Variants that hold to 16:05 
HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md:66:| Breaker #8, #9 and the F1 topology | The 16:00 flat needs a FLATTEN path to the order engine, which does not exist (topology doc, breaker #1 and #4 rows). |
HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md:67:| Block 3 deterministic fallback script (Phase 3 :109) | Its "session time" threshold becomes 16:00, not 11:30. |
HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md:69:| Rubric F2 "Why frozen" (`specs/SPEC_RUBRIC.md`:37–42) | The operator-schedule justification for the 11:30 cut named there is retired by Rule F2-1, not repaired.
HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md:75:| OPEN-F2-1 | Backtest flat on the 15:59 bar (fills by 16:00) or the 16:00 bar (fill may land after 16:00:00). | The master under D1 with the O4 parity statement 
HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md:76:| OPEN-F2-2 | R6 variants that hold to 16:05. | The R6 unit under D1 (exit by 16:00 under Rule F2-1, or propose an exception inside MFFU's 16:10); changeable by A
HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md:79:| OPEN-F2-5 | Adoption of Rule F2-1. | Amear's approval under A6; then a DECISIONS.md entry and the amended #4/#5 text in the breaker spec. |
HEAD:docs/specs/2026-11-10-live-signal-topology.md:4:Unit: 2026-11-10-f1-f2-proposal (authorisation: DECISION_LOG.md row 2026-11-10T13:03:00Z, praxis-master, item (2)). Bead context: `Praxis_build-2nh`.
HEAD:docs/specs/2026-11-10-live-signal-topology.md:41:Path: NT8 emitter (computes signal) → HTTP POST → n8n webhook → **[breaker gates, Redis, default closed]** → Write Signal File → outbox → sweep daemon → drop dir → `P
HEAD:docs/specs/2026-11-10-live-signal-topology.md:44:1. Every one of the nine breakers must sit upstream of order submission on the live path. Under this topology, every gate check runs before `SubmitBracket` (table, se
HEAD:docs/specs/2026-11-10-live-signal-topology.md:48:**What changes from the Block 1 architecture.** The emitter is NT8, not TradingView (CLAUDE.md "Signal flow: TradingView alert → webhook → …"). Deviation G's public-i
HEAD:docs/specs/2026-11-10-live-signal-topology.md:61:| 4 | Session time gate | Two checks: an n8n gate node before Write Signal File (ET clock; entries refused after the flat time until the next session), and an ET cloc
HEAD:docs/specs/2026-11-10-live-signal-topology.md:62:| 5 | Afternoon session window | As the Phase 3 text stands: an n8n gate node before Write Signal File plus the same consumer clock check as #4, refusing every system
HEAD:docs/specs/2026-11-10-live-signal-topology.md:74:| **1 (recommended)** | NT8 emitter strategy posts to the local n8n webhook | n8n + Redis before the file write; #7/#8/#9 also in the consumer | emitter strategy; VM 
HEAD:docs/specs/2026-11-10-live-signal-topology.md:86:| B1 | A JSON file written straight into the drop dir `/Users/admin/praxis-signals`, into `incoming/`, or into the n8n outbox, by anything that can write as `admin`, 
HEAD:docs/specs/2026-11-10-live-signal-topology.md:88:| B3 | Manual orders typed into NT8, Rithmic or the MFFU platform. | No, never. | Nothing on this path can gate a human order. R8's KEPT half of #5 (lockout on Amear'
HEAD:docs/specs/2026-11-10-live-signal-topology.md:105:| OPEN-T8 | How R8's lockout on Amear's own interaction 15:00–18:00 is enforced, since manual orders never pass n8n (B3). | Block 3 design under D1; it binds Amear's
HEAD:docs/specs/2026-11-10-live-signal-topology.md:112:This topology touches: Block 1 (the emitter changes from TradingView to NT8; the TESTED pipe is reused; Deviation G's ingress question leaves the anchor's live path)
HEAD:ninjascript/PraxisLastHalfHourMomentum.cs:27://   * Hours: NQ trades on the cash hours 09:30-16:00 (Table 1, p. 383; Table A1, PDF p. 19).
HEAD:ninjascript/PraxisLastHalfHourMomentum.cs:29://     close (Eq. 2, p. 381). For NQ, c = 16:00, so the signal price is the 15:30 price.
HEAD:ninjascript/PraxisLastHalfHourMomentum.cs:32://   * Holding: the last half hour, 15:30 -> 16:00 close. Flat at the close; at most one trade a day.
HEAD:ninjascript/PraxisLastHalfHourMomentum.cs:38:// INSTRUMENT / SESSION ASSUMPTIONS: NQ futures, 1-MINUTE series, RTH session template 09:30-16:00 ET,
HEAD:ninjascript/PraxisLastHalfHourMomentum.cs:41://   the 16:00-stamped bar is the regular session's last. The 15:30-stamped bar covers 15:29-15:30, so its
HEAD:ninjascript/PraxisLastHalfHourMomentum.cs:48://   * Previous close P(c,t-1): on every WEEKDAY bar stamped 16:00 (mod == CloseMod), lastRegularClose = Close[0]
HEAD:ninjascript/PraxisLastHalfHourMomentum.cs:50://     recent 16:00-stamped close of a PRIOR session (today's 16:00 bar comes after 15:30). No 16:00 bar
HEAD:ninjascript/PraxisLastHalfHourMomentum.cs:63://   * Exit is decided on the 15:59 bar's close and fills at the 16:00-stamped bar's Open, about the 15:59
HEAD:ninjascript/PraxisLastHalfHourMomentum.cs:64://     price. So the final minute 15:59 -> 16:00 of the paper's window is NOT earned.
HEAD:ninjascript/PraxisLastHalfHourMomentum.cs:65://   * M1 (PraxisNoiseAreaBreakout_Flat1559.cs) found that an exit decided ON the 16:00 bar fills in the
HEAD:ninjascript/PraxisLastHalfHourMomentum.cs:66://     next session (INFERRED). That is why FlatMod is 15:59 and not 16:00.
HEAD:ninjascript/PraxisLastHalfHourMomentum.cs:71://   bar, and a 16:00 close captured on an EARLIER bar. No future bar is read; the order fills one bar
HEAD:ninjascript/PraxisLastHalfHourMomentum.cs:75://   the paper dropping those days. Such a session also has no 16:00 bar, so it never sets lastRegularClose.
HEAD:ninjascript/PraxisLastHalfHourMomentum.cs:82://   D2. The last minute 15:59 -> 16:00 is not earned (exit fills at the 16:00 bar's Open, INFERRED).
HEAD:ninjascript/PraxisLastHalfHourMomentum.cs:83://   D3. P(c,t-1) = the most recent 16:00-stamped close of a prior session, NOT the prior session's last
HEAD:ninjascript/PraxisLastHalfHourMomentum.cs:84://       bar. Why: the import data has 37 weekday sessions ending 13:00 (CME halts on NYSE holidays),
HEAD:ninjascript/PraxisLastHalfHourMomentum.cs:86://       ("last-bar stamp counts (non-16:00): [(1300, 37), (1315, 9), (1403, 1)]"). The paper drops
HEAD:ninjascript/PraxisLastHalfHourMomentum.cs:88://       day's 16:00 close (INFERRED). A 16:00-stamped close is also robust to whether the template ends
HEAD:ninjascript/PraxisLastHalfHourMomentum.cs:89://       at 16:00 or 17:00 ET (DECISION_LOG:365); the prior session's last bar is not (INFERRED).
HEAD:ninjascript/PraxisLastHalfHourMomentum.cs:93://   D4. Missing 15:59 bar: the 16:00 bar triggers the exit, which may fill in the next session (INFERRED);
HEAD:ninjascript/PraxisLastHalfHourMomentum.cs:94://       on that 16:00 bar the session-close backstop may also fire (double exit, CANNOT-DETERMINE-
HEAD:ninjascript/PraxisLastHalfHourMomentum.cs:107://   Regular close stamp 16:00 (D3) ..................... CloseMod const         L128
HEAD:ninjascript/PraxisLastHalfHourMomentum.cs:108://   P(c,t-1) = most recent 16:00 close (Eq. 2, D3) ..... mod == CloseMod test   L178, capture L180
HEAD:ninjascript/PraxisLastHalfHourMomentum.cs:114://   No prior 16:00 close -> no trade ................... lastRegularClose <= 0  L224
HEAD:ninjascript/PraxisLastHalfHourMomentum.cs:127:		private const int FlatMod   = 16 * 60 - 1;    // 959 — the 15:59 bar; exit fills at the 16:00 bar Open (INFERRED)
HEAD:ninjascript/PraxisLastHalfHourMomentum.cs:128:		private const int CloseMod  = 16 * 60;        // 960 — the 16:00 bar; its Close is the regular close P(c) (D3)
HEAD:ninjascript/PraxisLastHalfHourMomentum.cs:132:		private double   lastRegularClose;       // P(c,t-1): Close of the most recent 16:00-stamped bar; 0 = none yet
HEAD:ninjascript/PraxisLastHalfHourMomentum.cs:141:				Description  = "PRAXIS 7zq M2 Last-half-hour market intraday momentum ([author] 2021, JFE 142, eta(r_ROD)). At 15:30 ET: long if (last 16:00 close)->15:30 return > 0
HEAD:ninjascript/PraxisLastHalfHourMomentum.cs:177:			// ---- Regular close capture (D3): every 16:00-stamped bar. Used only on a LATER session's signal bar. ----
HEAD:ninjascript/PraxisLastHalfHourMomentum.cs:205:			// ---- Flat on the 15:59 bar (or any later bar) — fills at the 16:00 bar Open (INFERRED). ----
HEAD:ninjascript/PraxisLastHalfHourMomentum.cs:228:				Print(Name + " WARNING: prior 16:00 close is from " + lastRegularCloseDate.ToString("yyyy-MM-dd")
HEAD:ninjascript/PraxisLastHalfHourMomentum.cs:231:			double r = Close[0] / lastRegularClose - 1.0;   // r_ROD = P(15:30)/P(last 16:00 close) - 1 (Eq. 2, p. 381)
HEAD:ninjascript/PraxisNoiseAreaBreakout.cs:31://   * Session-flat = 16:00 ET cash close (paper §4 p.9/12; NOT the 09:30-11:30 PRAXIS window).
HEAD:ninjascript/PraxisNoiseAreaBreakout.cs:37:// 1-MINUTE NQ series with an RTH (09:30-16:00 ET) session template in the Strategy Analyzer.
HEAD:ninjascript/PraxisNoiseAreaBreakout.cs:56:		// Minute-of-day (ET) constants. Session Open = 09:30, cash Close = 16:00 (spec §1, §4).
HEAD:ninjascript/PraxisNoiseAreaBreakout.cs:68:			public double Close1600;                             // Close_{t,16:00} (prev-close ref, spec §1 p.7)
HEAD:ninjascript/PraxisNoiseAreaBreakout.cs:84:		private double     prevClose;      // Close_{t-1,16:00}  (overnight-gap ref, spec §1 p.7)
HEAD:ninjascript/PraxisNoiseAreaBreakout.cs:101:				Description  = "PRAXIS B2 Noise-Area Breakout ([author] SSRN 4824172) — paper-faithful NQ backtest strategy. 14-day per-minute-of-day noise band anchored at the 09:30 o
HEAD:ninjascript/PraxisNoiseAreaBreakout.cs:108:				IsExitOnSessionCloseStrategy              = true;   // backstop; explicit 16:00 flat is primary
HEAD:ninjascript/PraxisNoiseAreaBreakout.cs:154:				// prevClose = last bar of the prior session (its 16:00 close). Close[1] is that bar.
HEAD:ninjascript/PraxisNoiseAreaBreakout.cs:188:			// ---- 16:00 ET cash-close flat (spec §4 p.9/12; trader-locked). Applies before any entry. ----
HEAD:ninjascript/PraxisNoiseAreaBreakout.cs:191:				FlattenAll("16:00 session flat");
HEAD:ninjascript/PraxisNoiseAreaBreakout.cs:236:		//   Upper = max(Open_{t,09:30}, Close_{t-1,16:00}) · (1 + k·σ)
HEAD:ninjascript/PraxisNoiseAreaBreakout.cs:237:		//   Lower = min(Open_{t,09:30}, Close_{t-1,16:00}) · (1 − k·σ),  k = BandSigmaMult (=1.0 paper).
HEAD:ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:22:// CHANGE: the flatten decision moves from the 16:00-stamped bar (mod >= 960) to mod >= 959
HEAD:ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:24://   15:59-stamped 1-min bar, so it fills at the 16:00 bar's open on the same day (INFERRED:
HEAD:ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:31:// This variant does NOT decide rubric F2 (session-flat time vs breakers #4/#5, FROZEN). The
HEAD:ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:32:// governing flat time stays 16:00 ET. The variant changes only WHEN the exit order is submitted
HEAD:ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:34:// Consequence: the exit fills at the Open of the 16:00-stamped bar (the first trade after ~15:59:00,
HEAD:ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:35://   INFERRED), one minute earlier in price than a 16:00:00 close; the position is still flat by 16:00 ET.
HEAD:ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:43:// MISSING 15:59 BAR (no trades that minute): the 16:00 bar triggers the flatten, as in the base (INFERRED).
HEAD:ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:64://   * Session-flat = 16:00 ET cash close (paper §4 p.9/12; NOT the 09:30-11:30 PRAXIS window).
HEAD:ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:70:// 1-MINUTE NQ series with an RTH (09:30-16:00 ET) session template in the Strategy Analyzer.
HEAD:ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:88:		// Minute-of-day (ET) constants. Session Open = 09:30, cash Close = 16:00 (spec §1, §4).
HEAD:ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:101:			public double Close1600;                             // Close_{t,16:00} (prev-close ref, spec §1 p.7)
HEAD:ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:117:		private double     prevClose;      // Close_{t-1,16:00}  (overnight-gap ref, spec §1 p.7)
HEAD:ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:134:				Description  = "PRAXIS B2 Noise-Area Breakout ([author] SSRN 4824172) — paper-faithful NQ backtest strategy. 14-day per-minute-of-day noise band anchored at th
HEAD:ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:187:				// prevClose = last bar of the prior session (its 16:00 close). Close[1] is that bar.
HEAD:ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:221:			// ---- 16:00 ET cash-close flat (spec §4 p.9/12; trader-locked). Applies before any entry. ----
HEAD:ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:223:			//      fills at the 16:00 bar's open (INFERRED). The governing flat time is unchanged at 16:00 ET.
HEAD:ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:224:			//      Consequence: the exit fills at the Open of the 16:00-stamped bar (the first trade after
HEAD:ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:225:			//      ~15:59:00, INFERRED), one minute earlier in price than a 16:00:00 close; the position is
HEAD:ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:226:			//      still flat by 16:00 ET.
HEAD:ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:229:				FlattenAll("16:00 session flat");
HEAD:ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:274:		//   Upper = max(Open_{t,09:30}, Close_{t-1,16:00}) · (1 + k·σ)
HEAD:ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:275:		//   Lower = min(Open_{t,09:30}, Close_{t-1,16:00}) · (1 − k·σ),  k = BandSigmaMult (=1.0 paper).
HEAD:ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:32://   Close > UpperBound). OppBand therefore becomes "reverse or hold to 16:00". A flat-only exit
HEAD:ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:56://   * Session-flat = 16:00 ET cash close (paper §4 p.9/12; NOT the 09:30-11:30 PRAXIS window).
HEAD:ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:62:// 1-MINUTE NQ series with an RTH (09:30-16:00 ET) session template in the Strategy Analyzer.
HEAD:ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:79:		// Minute-of-day (ET) constants. Session Open = 09:30, cash Close = 16:00 (spec §1, §4).
HEAD:ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:91:			public double Close1600;                             // Close_{t,16:00} (prev-close ref, spec §1 p.7)
HEAD:ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:107:		private double     prevClose;      // Close_{t-1,16:00}  (overnight-gap ref, spec §1 p.7)
HEAD:ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:124:				Description  = "PRAXIS B2 Noise-Area Breakout ([author] SSRN 4824172) — paper-faithful NQ backtest strategy. 14-day per-minute-of-day noise band anchored at the
HEAD:ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:131:				IsExitOnSessionCloseStrategy              = true;   // backstop; explicit 16:00 flat is primary
HEAD:ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:177:				// prevClose = last bar of the prior session (its 16:00 close). Close[1] is that bar.
HEAD:ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:211:			// ---- 16:00 ET cash-close flat (spec §4 p.9/12; trader-locked). Applies before any entry. ----
HEAD:ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:214:				FlattenAll("16:00 session flat");
HEAD:ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:262:		//   Upper = max(Open_{t,09:30}, Close_{t-1,16:00}) · (1 + k·σ)
HEAD:ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:263:		//   Lower = min(Open_{t,09:30}, Close_{t-1,16:00}) · (1 − k·σ),  k = BandSigmaMult (=1.0 paper).
HEAD:scripts/b2_stitch.py:57:# reopen is 23:00Z in winter / 22:00Z in summer, BOTH == 18:00 ET, and it tracks
HEAD:scripts/b2_stitch.py:67:# (stored 00:00-04:00Z on roll_date, i.e. 19:00-23:00 ET on roll_date-1) back a
HEAD:scripts/b2_stitch.py:604:    return (9 * 60 + 30) <= m < (16 * 60)  # 09:30 <= t < 16:00
HEAD:scripts/tests/b2-stitch-selftest.py:276:        # 01:00/02:00/03:00Z on the roll date 2024-03-15 == 21:00/22:00/23:00 ET on
HEAD:scripts/tests/b2-stitch-selftest.py:282:            ["2024-03-15 03:00:00", 18052, 18052, 18052, 18052, 100],  # -> ET 03-14 23:00
HEAD:scripts/tests/b2-stitch-selftest.py:317:        evenings = ["2024-03-14 21:00", "2024-03-14 22:00", "2024-03-14 23:00"]
HEAD:scripts/wf/oracle/grade.py:359:            a.d_pos = (n, i - 1)                               # fill on the 16:00 bar; d = the bar before (15:59)
HEAD:scripts/wf/oracle/grade.py:362:            a.notes.append("FlatEOD fill not on a 16:00 bar (%s)" % pos_str(market, a.exit_pos))
HEAD:scripts/wf/oracle/grade.py:840:         "the 16:00 bar's open, 2 ticks adverse, clipped. Not refitted from T1/T3.", "",
HEAD:scripts/wf/oracle/market.py:11:    dates with >= 1 bar stamped 09:31:00-16:00:00 inside the range; no second calendar is written here;
HEAD:scripts/wf/oracle/market.py:24:    by sessions.py's NT8_MAP rule (13:15 -> 12:15, 13:00 -> 12:00, 14:03 stays); any other early last bar
HEAD:scripts/wf/oracle/market.py:28:  * bars stamped outside SESSION_START..16:00:00 are ignored;
HEAD:scripts/wf/oracle/market.py:29:  * the session LIST and the s-numbering are sessions.py's at either start (09:31-16:00 day rule). A weekday
HEAD:scripts/wf/oracle/market.py:30:    in range with bars only inside SESSION_START..09:30 and none in 09:31-16:00 (possible only at 08:31; on
HEAD:scripts/wf/oracle/market.py:80:# close fills at the CLOSE of the 16:00-stamped bar, within 0.50) and :255 (FlatEOD = OPEN of the 16:00 bar,
HEAD:scripts/wf/oracle/market.py:108:        self.cut_dropped = 0   # bars in session_start-16:00 past the NT8 cut (dropped)
HEAD:scripts/wf/oracle/market.py:131:        self.weekend_bars_dropped = 0        # weekend-dated bars in session_start-16:00, in range
HEAD:scripts/wf/oracle/market.py:221:    (09:31-16:00 day rule at either start; it validates every line with sessions._parse_line and raises
HEAD:scripts/wf/oracle/market.py:256:                continue                       # outside session_start..16:00: ignored
HEAD:scripts/wf/oracle/market.py:327:    """Step (1) of values-spec §4 precedence: the bar is the session's last loaded bar (16:00, or the
HEAD:scripts/wf/oracle/market.py:349:    """FlatEOD = market fill on the 16:00-stamped bar (results :255)."""
HEAD:scripts/wf/oracle/policy.py:224:            bad.append((row, "row %d: FlatEOD fills %s, not on the 16:00 bar after a 15:59 decision (.cs :234-235)"
HEAD:scripts/wf/oracle/policy.py:228:                bad.append((row, "row %d: '%s' on a 16:00 bar %s under Flat1559 (the 15:59 flatten precedes it)"
HEAD:scripts/wf/oracle/policy.py:236:        # open at the close of a 15:59-stamped bar: FlatEOD decided there (mod >= 959, .cs :234-235), filled on 16:00
HEAD:scripts/wf/oracle/policy.py:239:            lines.append("row %d open at 15:59 %s but the session has no 16:00 bar: placement not graded"
HEAD:scripts/wf/oracle/policy.py:252:            bad.append((row, "row %d FlatEOD price %r != FlatEOD rule %r (16:00 open, 2 ticks adverse, clipped)"
HEAD:scripts/wf/oracle/tests/test_edges.py:26:# (g2) s16 file last bar 13:00 -> cut 12:00, which is both the last bar (F) and a checkpoint.
HEAD:scripts/wf/oracle/tests/test_edges.py:31:              ("1300", 1000, 1000, 1000, 1000)]       # dropped; file last bar 13:00
HEAD:scripts/wf/oracle/tests/test_edges.py:42:           ("1600", 1000.5, 1001, 1000, 1000.5)]      # FlatEOD = 16:00 open 1000.5 - 0.5 = 1000.0 (clipped at l 1000)
HEAD:scripts/wf/oracle/tests/test_edges.py:70:    # (g2) 13:00 file: 12:00 is the last bar AND a checkpoint; an entry decided there is not flagged by (v)
HEAD:scripts/wf/oracle/tests/test_grade.py:5:  09:31 o 1000 h 1002 l 998 c 1000;  10:00, 10:30, 11:00, 15:30, 15:59, 16:00  o=h=l=c=1000
HEAD:scripts/wf/oracle/tests/test_grade.py:68:# s16 day D: long entered 15:31, first crossing on the 16:00 bar (F under BandOrVWAP).
HEAD:scripts/wf/oracle/tests/test_grade.py:272:        tr = ("Long", T(16, "1531"), 1003.5, T(17, "0931"), 999.5, "XStop")    # d = prev bar = s16 16:00 = F
HEAD:scripts/wf/oracle/tests/test_policy.py:5:  09:31 o1000 h1002 l998 c1000; every checkpoint 10:00, 10:30, ..., 15:30; 15:59; 16:00 — all o=h=l=c=1000.
HEAD:scripts/wf/oracle/tests/test_policy.py:11:    every override below; prev close = s15 16:00 = 1000).
HEAD:scripts/wf/oracle/tests/test_policy.py:13:    close -/+ 0.5 clipped; FlatEOD = the 16:00 bar's open -/+ 0.5 clipped.
HEAD:scripts/wf/oracle/tests/test_policy.py:183:        self.assertEqual(V[("T12(i)", "all")].rows, ["A#1", "B#1", "A#4", "C#4", "B#1", "C#1"])
HEAD:scripts/wf/oracle/tests/test_policy.py:184:        # (iv): A's XL at 10:30 (1003 not < 1000) -> next entry 11:01 later; XS at 11:30 (1004.25 > 1004) -> reversal
HEAD:scripts/wf/oracle/tests/test_policy.py:192:    # (a) Flat1559 FlatEOD rows at 16:00 -> (ii) PASS; a 16:00 session close -> FAIL; an off-rule price -> not PASS
HEAD:scripts/wf/oracle/tests/test_policy.py:197:        self.assertTrue(any("row 4 open at 15:59 exits FlatEOD s16 2021-03-29 16:00 at 1006.0" in x for x in v.lines),
HEAD:scripts/wf/oracle/tests/test_policy.py:198:                        v.lines)   # 16:00 open 1006 - 0.5 = 1005.5 clipped to the bar's low 1006 -> 1006.0
HEAD:scripts/wf/oracle/tests/test_policy.py:203:        self.assertTrue(any("on a 16:00 bar" in x for x in v.lines))
HEAD:scripts/wf/oracle/tests/test_session_start.py:14:  16:00  o=h=l=c 1000 v 10
HEAD:scripts/wf/oracle/tests/test_session_start.py:84:    pc = 1000.0                                       # s16 16:00 close
HEAD:scripts/wf/oracle/tests/test_session_start.py:199:        pb = mk.prev_bar(m08, 4, 0)                    # s4's previous loaded bar = s3 16:00, not the dropped day
HEAD:scripts/wf/oracle/tests/test_synthetic.py:8:  16:00  o=h=l=c=E_n = 1024 + 0.5*(n % 5) - 1.0, v 40   (E_6 = 1034.0, a gap above s7's range)
HEAD:scripts/wf/oracle/tests/test_synthetic.py:9:  s10 2021-03-19 early close: no 16:00; 12:15 o=h=l=c=1044 v 40; 12:30 h 2000 l 500 (dropped); 13:15 c 1100
HEAD:scripts/wf/oracle/tests/test_synthetic.py:72:        if n == 5:   # Friday 2021-03-12 -> Saturday 2021-03-13 weekend bar inside 09:31-16:00
HEAD:scripts/wf/oracle/tests/test_synthetic.py:102:        pb = mk.prev_bar(m, 6, 0)                                # Monday's previous loaded bar = Friday 16:00
HEAD:scripts/wf/oracle/tests/test_synthetic.py:207:        # 16:00: s10 (early close, cut 12:15) has no 16:00 close, so s2..s11 yield only 9 -> no band (.cs :354, :360)
HEAD:scripts/wf/oracle/tests/test_synthetic.py:209:        self.assertEqual(bd.band_at(self.m, 12, "16:00", 10, 1.0).cnt, 9)
HEAD:scripts/wf/oracle/tests/test_synthetic.py:210:        self.assertTrue(bd.band_at(self.m, 13, "16:00", 10, 1.0).have_band)   # s2..s12 minus s10 = 10
HEAD:scripts/wf/sessions.py:19:RTH_FIRST = "093100"   # values-spec §5 :83 "at least one bar stamped 09:31:00–16:00:00"
HEAD:scripts/wf/sessions.py:29:# that table (13:15 -> 12:15 session-close exit, 13:00 -> 12:00, 14:03 -> 14:03).
HEAD:scripts/wf/sessions.py:34:    "13:00": "12:00",
HEAD:scripts/wf/sessions.py:45:    "2025-01-20": ("13:00", "12:00"),
HEAD:scripts/wf/sessions.py:46:    "2025-06-19": ("13:00", "12:00"),
HEAD:scripts/wf/sessions.py:58:# INFERRED: a session whose file last RTH bar is 16:00 ends at 16:00 in NT8 too
HEAD:scripts/wf/sessions.py:59:# (RTH template 09:30-16:00; not separately observed per session).
HEAD:scripts/wf/sessions.py:60:GRADE_FULL = "INFERRED: file last bar 16:00, full session"
HEAD:scripts/wf/sessions.py:137:    rth = {}            # date -> [first HHMMSS, last HHMMSS] of bars in 09:31:00-16:00:00
HEAD:scripts/wf/sessions.py:169:            nt8, grade = "16:00", GRADE_FULL
HEAD:scripts/wf/sessions.py:173:            # values-spec §9 (c) :233 names NT8 cuts only for file last bar 13:15 / 13:00 /
HEAD:scripts/wf/sessions.py:269:        "rule": {"rth_first": "09:31:00", "rth_last": "16:00:00", "weekdays": "Mon-Fri",
HEAD:scripts/wf/sessions.py:320:    p("weekend dates with a 09:31-16:00 bar, in range (dropped) = %d; first = %s; whole file = %s"
HEAD:scripts/wf/tests/test_report.py:39:                             "last_bar": "16:00", "early_close_in_file": False,
HEAD:scripts/wf/tests/test_report.py:40:                             "nt8_last_bar": "16:00", "nt8_last_bar_grade": "synthetic"})
HEAD:scripts/wf/tests/test_select.py:48:            "rule": {"rth_first": "09:31:00", "rth_last": "16:00:00", "weekdays": "Mon-Fri",
HEAD:scripts/wf/tests/test_select.py:50:            "N": n, "sessions": [{"n": i, "date": "d%d" % i, "first_bar": "09:31", "last_bar": "16:00",
HEAD:scripts/wf/tests/test_select.py:51:                                  "early_close_in_file": False, "nt8_last_bar": "16:00",
HEAD:scripts/wf/tests/test_sessions.py:90:            bar("20210308", "160100"),            # after 16:00 - ignored
HEAD:scripts/wf/tests/test_sessions.py:94:            bar("20210311", "100000"),            # Thu last bar 13:00 -> 12:00
HEAD:scripts/wf/tests/test_sessions.py:109:                         ("09:31", "16:00", False, "16:00"))
HEAD:scripts/wf/tests/test_sessions.py:112:        self.assertEqual(S[3]["nt8_last_bar"], "16:00")
HEAD:scripts/wf/tests/test_sessions.py:242:        for t, hm in (("120000", "12:00"), ("121500", "12:15"), ("150000", "15:00")):
HEAD:scripts/wf/tests/test_sessions.py:320:        for date, last, nt8 in [("2024-12-24", "13:15", "12:15"), ("2025-01-20", "13:00", "12:00"),
HEAD:scripts/wf/tests/test_sessions.py:321:                                ("2025-06-19", "13:00", "12:00"), ("2021-11-26", "13:15", "12:15"),
HEAD:scripts/wf/tests/test_tradelist.py:30:               "sessions": [{"n": i + 1, "date": d, "first_bar": "09:31", "last_bar": "16:00",
HEAD:scripts/wf/tests/test_tradelist.py:31:                             "early_close_in_file": False, "nt8_last_bar": "16:00",
HEAD:scripts/wf/tests/test_tradelist.py:84:        f = self.bridge("b.json", [trade("2021-03-08T10:01:00", "2021-03-08T16:00:00", 100.0),
HEAD:scripts/wf/tests/test_tradelist.py:94:        f = self.bridge("b.json", [trade("2021-03-08T10:01:00", "2021-03-08T16:00:00", 95.32)])
HEAD:scripts/wf/tests/test_tradelist.py:119:            trade("2021-03-11T10:00:00", "2021-03-11T16:00:00", -5.0, "Short"),
HEAD:scripts/wf/tests/test_tradelist.py:277:        self.assertEqual(s["trades"][0]["exit_time"], "2021-03-09T16:00:00")
```

#### [E16]

```text
$ git grep -n -i -E 'session|clock|11:30|16:00' HEAD -- ninjascript/PraxisSignalConsumer.cs | cut -c1-160; git diff HEAD -U0 -- docs/specs/2026-11-05-walk-forward-spec.md docs/specs/2026-11-06-walk-forward-values.md | grep -E '^[+-][^+-]' | grep -c -E '11:30|15:00|3:00|16:00|4:10|16:10'
HEAD:ninjascript/PraxisSignalConsumer.cs:84:				IsExitOnSessionCloseStrategy             = false;
0
```

#### [E17]

```text
$ sed -n 2068p DECISIONS.md | grep -o 'is PROPOSED, not adopted (:62)'; sed -n 1744,1745p DECISIONS.md; sed -n 76p docs/specs/2026-11-05-phase3-build-specification.md | grep -o 'Session window and clock times held fixed.'; sed -n 109p docs/specs/2026-11-05-phase3-build-specification.md | grep -o 'checks hardcoded thresholds (daily loss, max trades, session time)'
is PROPOSED, not adopted (:62)
A6  FLAG 6: R8 starts the breaker PROPOSAL unit. F2's state changes
    when Amear approves the proposed values.
Session window and clock times held fixed.
checks hardcoded thresholds (daily loss, max trades, session time)
```

#### [E18]

```text
$ sed -n 12p docs/specs/2026-11-05-walk-forward-spec.md | grep -o '(188 lines, sha256 \`cd02d34ae635626e674f4316bdfd9ac14d96f819aaf28d39b7d651607be69b83\`)'; git show HEAD:docs/specs/2026-11-05-phase3-build-specification.md | shasum -a 256; shasum -a 256 docs/specs/2026-11-05-phase3-build-specification.md; git grep -n -o -E 'Phase 3( spec)? :1(0[7-9]|1[0-9])' HEAD -- docs/specs
(188 lines, sha256 `cd02d34ae635626e674f4316bdfd9ac14d96f819aaf28d39b7d651607be69b83`)
cd02d34ae635626e674f4316bdfd9ac14d96f819aaf28d39b7d651607be69b83  -
cd8facf45d9f297e91a13329715ca81ecbaf5dd7a6801586af23e377e21607ba  docs/specs/2026-11-05-phase3-build-specification.md
HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md:67:Phase 3 :109
HEAD:docs/specs/2026-11-10-live-signal-topology.md:24:Phase 3 spec :107
HEAD:docs/specs/2026-11-10-live-signal-topology.md:61:Phase 3 :109
HEAD:docs/specs/2026-11-10-live-signal-topology.md:89:Phase 3 :107
HEAD:docs/specs/2026-11-10-live-signal-topology.md:89:Phase 3 :109
```

#### [E19]

```text
$ sed -n 2068p DECISIONS.md | cut -c1-120; sed -n 54p docs/specs/2026-11-10-live-signal-topology.md | cut -c1-140; sed -n 62p docs/specs/2026-11-10-live-signal-topology.md | cut -c1-420; sed -n 40p docs/specs/2026-11-10-f2-session-flat-proposal.md
**F2 stays FROZEN.** Breakers #4 and #5 depend on F2 (:61–62). The F2 proposal `docs/specs/2026-11-10-f2-session-flat-pr
Names are exactly as the Phase 3 import lists them (`docs/specs/2026-11-05-phase3-build-specification.md`:97–105, at HEAD) [E1]. Every row's
| 5 | Afternoon session window | As the Phase 3 text stands: an n8n gate node before Write Signal File plus the same consumer clock check as #4, refusing every system entry (including Noise-Area reversals) in the window. Under the F2 proposal (`docs/specs/2026-11-10-f2-session-flat-proposal.md`, PROPOSED, not adopted) #5 becomes an operator lockout only, and the system no-entry period 16:00–18:00 moves into #4; the n
Placement of both on the live path is in `docs/specs/2026-11-10-live-signal-topology.md`, section 3. That table places #5 as the Phase 3 text stands (a system entry block in the window) and states what changes under this proposal: if adopted, the system window check is removed and only the operator lockout remains. That document notes that #5's operator lockout cannot sit on the signal path, because manual orders never pass n8n (its bypass B3, OPEN-T8).
```


#### [E20] S4 order — captured at the time of each write (commands and outputs as run; not re-runnable after the fact)

Pre-edit state:

```text
$ cd /Volumes/Sensidine/Praxis.build && shasum -a 256 DECISIONS.md docs/specs/2026-11-05-phase3-build-specification.md && git diff --quiet HEAD -- DECISIONS.md docs/specs/2026-11-05-phase3-build-specification.md && echo both-clean-vs-HEAD
df1661e042e1856bbdeb727df787bc07552dee8543b0b9c3bc9424081b381d43  DECISIONS.md
cd02d34ae635626e674f4316bdfd9ac14d96f819aaf28d39b7d651607be69b83  docs/specs/2026-11-05-phase3-build-specification.md
both-clean-vs-HEAD
```

First write — entry appended, spec not yet edited:

```text
$ cd /Volumes/Sensidine/Praxis.build && cat /tmp/f2b/entry.md >> DECISIONS.md && date -u +%Y-%m-%dT%H:%M:%SZ && stat -f '%N mtime=%Sm' -t '%Y-%m-%dT%H:%M:%S%z' DECISIONS.md docs/specs/2026-11-05-phase3-build-specification.md && grep -n '^## 2026-11-12 — D-2026-11-12-A' DECISIONS.md && grep -c 'Amendment 1 — 2026-11-12' docs/specs/2026-11-05-phase3-build-specification.md; wc -l DECISIONS.md
2026-11-12T05:32:56Z
DECISIONS.md mtime=2026-11-12T00:32:56-0500
docs/specs/2026-11-05-phase3-build-specification.md mtime=2026-11-05T19:24:11-0500
2205:## 2026-11-12 — D-2026-11-12-A: breakers #4 and #5 amended to match Rule F2-1 (rubric F2; master under D-2026-11-08-D D1)
0
    2278 DECISIONS.md
```

First spec write (with the pointer line, later withdrawn) — entry grep run immediately before it:

```text
$ cd /Volumes/Sensidine/Praxis.build && grep -n '^## 2026-11-12 — D-2026-11-12-A' DECISIONS.md && date -u +%Y-%m-%dT%H:%M:%SZ && python3 -I /tmp/f2b/compose_spec.py && stat -f '%N mtime=%Sm' -t '%Y-%m-%dT%H:%M:%S%z' DECISIONS.md docs/specs/2026-11-05-phase3-build-specification.md && git diff docs/specs/2026-11-05-phase3-build-specification.md
2205:## 2026-11-12 — D-2026-11-12-A: breakers #4 and #5 amended to match Rule F2-1 (rubric F2; master under D-2026-11-08-D D1)
2026-11-12T05:33:23Z
DECISIONS.md mtime=2026-11-12T00:32:56-0500
docs/specs/2026-11-05-phase3-build-specification.md mtime=2026-11-12T00:33:23-0500
diff --git a/docs/specs/2026-11-05-phase3-build-specification.md b/docs/specs/2026-11-05-phase3-build-specification.md
index 0f2c33d..507019c 100644
--- a/docs/specs/2026-11-05-phase3-build-specification.md
+++ b/docs/specs/2026-11-05-phase3-build-specification.md
@@ -104,6 +104,8 @@ The breakers (from Round 2 Agent 3):
 8. Stale signal filter — signal file older than X seconds → reject (prevents acting on delayed signals after a system hiccup)
 9. Heartbeat dead-man switch — if n8n hasn’t confirmed system health in 5 minutes → disable new orders
 
+> ***Added 2026-11-12; not part of the source document.*** Breakers #4 and #5 are amended; see Amendment 1 at the end of this file (D-2026-11-12-A).
+
```

(The rest of that first diff, the appended section, is not repeated here; the final diff is at [E10].)

Withdrawal of the pointer — spec reverted to HEAD bytes, entry region rewritten, before the final spec write:

```text
$ cd /Volumes/Sensidine/Praxis.build && S=docs/specs/2026-11-05-phase3-build-specification.md && git show HEAD:$S > $S && git diff --quiet HEAD -- $S && echo "spec reverted to HEAD bytes" && git show HEAD:DECISIONS.md > /tmp/f2b/decisions-head.md && cmp <(head -n 2203 DECISIONS.md) /tmp/f2b/decisions-head.md && echo "DECISIONS 1-2203 == HEAD" && cat /tmp/f2b/decisions-head.md /tmp/f2b/entry.md > DECISIONS.md && date -u +%Y-%m-%dT%H:%M:%SZ && stat -f '%N mtime=%Sm' -t '%Y-%m-%dT%H:%M:%S%z' DECISIONS.md $S && grep -n '^## 2026-11-12 — D-2026-11-12-A' DECISIONS.md && grep -c 'Amendment 1 — 2026-11-12' $S; wc -l < DECISIONS.md
spec reverted to HEAD bytes
DECISIONS 1-2203 == HEAD
2026-11-12T05:35:54Z
DECISIONS.md mtime=2026-11-12T00:35:54-0500
docs/specs/2026-11-05-phase3-build-specification.md mtime=2026-11-12T00:35:54-0500
2205:## 2026-11-12 — D-2026-11-12-A: breakers #4 and #5 amended to match Rule F2-1 (rubric F2; master under D-2026-11-08-D D1)
0
    2278
```

Final spec write — entry present and spec still at HEAD bytes immediately before it:

```text
$ cd /Volumes/Sensidine/Praxis.build && S=docs/specs/2026-11-05-phase3-build-specification.md && grep -n '^## 2026-11-12 — D-2026-11-12-A' DECISIONS.md && git diff --quiet HEAD -- $S && echo "spec still == HEAD before write" && date -u +%Y-%m-%dT%H:%M:%SZ && python3 -I /tmp/f2b/compose_spec.py && stat -f '%N mtime=%Sm' -t '%Y-%m-%dT%H:%M:%S%z' DECISIONS.md $S && git diff --stat HEAD -- $S
2205:## 2026-11-12 — D-2026-11-12-A: breakers #4 and #5 amended to match Rule F2-1 (rubric F2; master under D-2026-11-08-D D1)
spec still == HEAD before write
2026-11-12T05:36:00Z
DECISIONS.md mtime=2026-11-12T00:35:54-0500
docs/specs/2026-11-05-phase3-build-specification.md mtime=2026-11-12T00:36:00-0500
 .../specs/2026-11-05-phase3-build-specification.md | 56 ++++++++++++++++++++++
 1 file changed, 56 insertions(+)
```

#### [E21]

```text
$ wc -l < MANIFEST.md; git diff HEAD -- MANIFEST.md | grep -c '^+|'; tail -n 4 MANIFEST.md | cut -c1-150; git diff HEAD -- MANIFEST.md | grep -c '^-[^-]'; diff /tmp/f2b/manifest-before.md MANIFEST.md | grep -c '^>'; diff /tmp/f2b/manifest-before.md MANIFEST.md | grep -c '^<'
     437
12
| /DECISIONS.md | Log | 3 | 2026-11-12 | MODIFIED (unit 2026-11-12-f2-breaker-amendment, Unit F2B; master under D-2026-11-08-D D1, DECISION_LOG row 20
| /docs/specs/2026-11-05-phase3-build-specification.md | Spec | 3 | 2026-11-12 | AMENDMENT ROW (append-only registry — adds to row 226 for this path).
| /docs/reports/2026-11-12-f2-breaker-amendment-manager.md | Report | 3 | 2026-11-12 | Manager report for unit 2026-11-12-f2-breaker-amendment (Unit F
| /docs/reports/2026-11-12-f2-breaker-amendment-worker1.md | Report | 3 | 2026-11-12 | ADVERSARIAL worker 1 report for unit 2026-11-12-f2-breaker-amen
0
4
0
```

## Result

Result: see docs/reports/2026-11-12-f2-breaker-amendment-resume-manager.md (manager stopped at its turn cap; completed by unit 2026-11-12-f2-breaker-amendment-resume)

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
