# 2026-11-13 — Unit 2026-11-13-open-a2 — worker 1 (ADVERSARIAL, cold) report

## Task

Cold adversarial grading of entry D-2026-11-13-C (working-tree DECISIONS.md :2435–2457), MANIFEST.md rows :475–476 and the evidence report `docs/reports/2026-11-13-open-a2-manager.md`, against DECISION_LOG.md rows 2026-11-13T17:19:15Z (decision, DECISION_LOG.md:927) and 2026-11-13T17:22:34Z (S13 ruling, DECISION_LOG.md:928), and rubric S1, S2, S4, S6, S8, S13. Read-only. The only file written is this report. Nothing was staged. No skill attached to this brief told me to write under `.claude/`. I wrote nothing there, and that includes my agent-memory directory, because the brief forbids it. All commands ran from `/Volumes/Sensidine/Praxis.build`.

## Checks

### (a) Diffs show only the appended entry and the two appended rows — PASS

```
$ wc -l DECISIONS.md MANIFEST.md /tmp/oa2-pre-DECISIONS.md /tmp/oa2-pre-MANIFEST.md
    2457 DECISIONS.md
     476 MANIFEST.md
    2434 /tmp/oa2-pre-DECISIONS.md
     474 /tmp/oa2-pre-MANIFEST.md
    5841 total
```

```
$ diff /tmp/oa2-pre-DECISIONS.md DECISIONS.md; echo "exit=$?"; echo -----; diff /tmp/oa2-pre-MANIFEST.md MANIFEST.md; echo "exit=$?"
2434a2435,2457
> 
> ## 2026-11-13 — D-2026-11-13-C: Strategy-level stop before 16:00 for a later Noise-Area arm (ruleset OPEN-A2; master under D-2026-11-08-D D1)
> 
> **Status:** Decided by master under D-2026-11-08-D D1 (DECISION_LOG 2026-11-13T17:19:15Z), changeable by Amear. Not Amear's ruling. A written statement only (bead `Praxis_build-fgd`, ruleset item OPEN-A2). Not CONDITIONAL: it rests on no unobserved mechanism. Not a D2 item (no money, no live path, no breaker value, no credential).
> 
> **Decision.** Option (b) of ruleset :170, with a stated default. DEFAULT: every Noise-Area arm keeps lock item (1)'s full-day window to the 16:00 ET flat. An earlier strategy-level stop (11:30 or any other time) is allowed for a later arm (the walk-forward tunables arm or the live emitter) ONLY through that arm's own DECISIONS.md entry, written before the arm is built (S4) and graded under S6 against entry D-2026-11-13-A (backtest-vs-live parity), amended breaker #4 (the 16:00 backstop, unchanged) and the Block 4 gate. The replication arm is unchanged. No arm adopts an 11:30 stop by this entry. Reasons, each the master's reading under D1, changeable by Amear: lock item (3) scopes the "FIRST build" to paper replication; Amear's V2 approval was given on the summary "flat by 16:00 ET governs", which sets a latest flat, not an earliest; the sentence "Strategies may flat earlier than 16:00 by their own rules" (proposal :24) is the proposal's text, adopted by the master, and DECISIONS.md :2116 records that whether Amear's approval reaches proposal text outside the summary is not graded. Neither that sentence nor any reading here is credited to Amear.
> 
> **Sources (quoted byte-exact).**
> - Ruleset `docs/specs/2026-07-16-b2-noise-area-ruleset.md` :170 "Whether a strategy-level stop at 11:30 (a strategy rule, not a breaker) is still available to a later Noise-Area arm" and "Not chosen here."
> - Lock row `DECISION_LOG.md` :42 (stamp 2026-07-16T19:29Z; "WHO: trader (Amear) + orchestrator (session 16)"): item (1) "session-flat = 16:00 ET cash close (NOT the 11:30 PRAXIS window)"; item (3) "FIRST build = pure paper replication with FIXED params".
> - `DECISIONS.md` :2108 "flat by 16:00 ET governs; a position open at 15:00 may stay open until 16:00"; :2116 "listed without grading whether his approval reaches them".
> - F2 proposal `docs/specs/2026-11-10-f2-session-flat-proposal.md`: :24 "Strategies may flat earlier than 16:00 by their own rules (for example arm (b)'s Flat1559 exit policy)"; :60 "Allowed: an earlier flat than 16:00."
> - Entry D-2026-11-13-A, "Backtest-vs-live breaker parity": "Every Block 2 run yields two series from one trade list."
> - Phase 3 spec `docs/specs/2026-11-05-phase3-build-specification.md`: :212 "clock reaches 16:00:00 ET" and "confirm flat before 4:10 PM ET (alert if not)"; :196 "SPECIFIED ONLY — zero implemented, zero tested, zero tested under failure".
> - Rubric `specs/SPEC_RUBRIC.md` :111 "±15% win rate and ±25% average trade P&L".
> 
> **S6 cross-block.** Named here, not resolved. Replication arm: unchanged; lock items (1) and (3) govern it. Arm (b): the proposal's text names its Flat1559 exit policy as an earlier flat (proposal :24, :60); this entry neither adopts nor changes it, and whether it falls under this entry's rule is not decided here. D-2026-11-13-A parity: an earlier stop would change the one trade list from which that entry's two series are drawn; how backtest and live match for such an arm is for that arm's entry. Amended breaker #4 (spec :212): its 16:00 trigger is unchanged; how an earlier strategy stop sits with it is for that arm's entry. Block 4 gate (rubric :111): how an arm with an earlier stop meets it is for that arm's entry. No ruleset row, spec text or breaker text is edited.
> 
> **Limits.** No code, no spec body and no breaker value is changed. The ruleset row :170 is not edited. The nine breakers stay SPECIFIED ONLY (spec :196): zero implemented, zero tested. This entry does not touch F3 or F4.
> 
> **S4 timing.** Written 2026-11-13. It governs future arm entries only: each later arm's earlier stop must be filed in that arm's own entry before that arm is built. Chain: D-2026-11-08-D D1 → DECISION_LOG 2026-11-13T17:19:15Z (WHO: praxis-master).
> 
> Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
exit=1
-----
474a475,476
> | /DECISIONS.md | Log | 3 | 2026-11-13 | AMENDMENT ROW (append-only registry). Unit 2026-11-13-open-a2 (ruleset OPEN-A2, bead Praxis_build-fgd; master under D-2026-11-08-D D1, DECISION_LOG 2026-11-13T17:19:15Z): appends entry D-2026-11-13-C, "Strategy-level stop before 16:00 for a later Noise-Area arm", filing option (b) with a stated default: every Noise-Area arm keeps lock item (1)'s full-day window to the 16:00 ET flat; an earlier strategy-level stop is allowed for a later arm only through that arm's own DECISIONS.md entry, written before the arm is built and graded under S6 against D-2026-11-13-A, amended breaker #4 and the Block 4 gate. Replication arm unchanged; no arm adopts an 11:30 stop; reasons labelled the master's reading, none credited to Amear. Not CONDITIONAL, not D2. No code, no breaker value, no spec body changed; ruleset row :170 not edited; breakers stay SPECIFIED ONLY; F3 and F4 untouched. |
> | /docs/reports/2026-11-13-open-a2-manager.md | Report | 3 | 2026-11-13 | Evidence report for unit 2026-11-13-open-a2 (ruleset OPEN-A2, bead Praxis_build-fgd; master under D-2026-11-08-D D1, DECISION_LOG 2026-11-13T17:19:15Z): the filing of entry D-2026-11-13-C and its two MANIFEST rows, with literal commands and full output (pre-copies, diffs, HEAD prefix cmp, quote byte checks, S2 and hygiene counts, entry text). |
exit=1
```

Each diff is a single append hunk (`2434a2435,2457`, `474a475,476`), with no `<` lines and no `c` or `d` hunks. Prefix equality is shown under (d).

### (b) Entry files exactly the 17:19:15Z decision, adds no decision of its own — FAIL

```
$ grep -n '2026-11-13T17:19:15Z' DECISION_LOG.md
927:- [2026-11-13T17:19:15Z] WHO: praxis-master | WHAT: **Unit 2 choice: bead `fgd` OPEN-A2, one short DECISIONS.md entry D-2026-11-13-C.** Question (ruleset `docs/specs/2026-07-16-b2-noise-area-ruleset.md` :170): whether a strategy-level 11:30 stop (a strategy rule, not a breaker) is still available to a later Noise-Area arm (walk-forward tunables arm or live emitter). The row offers (a) No and (b) Yes as that arm's own design choice, and chooses neither. **Decided by master under D-2026-11-08-D D1:** option (b) with a stated default. DEFAULT: every Noise-Area arm carries lock item (1)'s full-day window to the 16:00 ET flat (DECISION_LOG.md:42, the 2026-07-16T19:29Z lock row, WHO: trader (Amear) + orchestrator). An earlier strategy-level stop, 11:30 or any other time, is allowed for a later arm ONLY through that arm's own DECISIONS.md entry, written before the arm is built (S4) and graded under S6 against: D-2026-11-13-A (backtest-vs-live parity: backtest and live must carry the same stop), amended breaker #4 (16:00 backstop, unchanged), and the Block 4 gate. The replication arm is unchanged (lock items (1) and (3)). Reasons, all labelled the master's reading: lock item (3) scopes the "FIRST build" to paper replication; Amear's V2 approval (DECISIONS.md :2108) was given on the summary "flat by 16:00 ET governs; …", which sets a latest flat, not an earliest; the proposal's sentence "Strategies may flat earlier than 16:00 by their own rules" (f2 proposal :24) is the PROPOSAL'S text, adopted by the master, and D-2026-11-11-A :2116 does not grade whether Amear's approval reaches it, so the entry must NOT credit it to Amear. No arm adopts an 11:30 stop by this entry. Not CONDITIONAL (no unobserved mechanism; a policy reading). Not a D2 item (no money, no live path, no breaker value, no credential). The ruleset row :170 is not edited. Filing manager drafts the entry (Status, Decision, Sources, S6, Limits, S4, S13 line; at most ~12 lines), quotes byte-checked; one fresh evidence report written from scratch; MANIFEST rows for the entry and the report; one cold adversary (uncommitted, not cited); then one auditor; commit blob = HEAD DECISIONS.md + the new entry range, HEAD MANIFEST + the new rows. | WHY: HANDOFF top card item 3; D1; S4; S6; S8 | WHERE: DECISIONS.md end; MANIFEST.md end | WHEN: `date -u` 17:19:15Z | HOW: praxis-manager, foreground | STATE: open
```

```
$ git show HEAD:docs/specs/2026-11-05-walk-forward-spec.md | grep -niE 'flat ?15:?59|tunable' | head -n 5 | cut -c1-250
42:> "c. Walk-forward build: arm (a) on the unchanged baseline; arm (b) on its own branch with the four tunables and the bar-close stop. Build and test on existing minute data only."
70:## 3. Arm (b) — four tunables plus a bar-close stop
72:- Tunables, tuned per window: lookback, noise multiplier, stop-ATR multiplier, exit policy (item 1b, `:812`; Block 2 config, Phase 3 spec `:76` names the same four). — RULED (D-2026-11-05-A).
75:- Branch: arm (b) is built "on its own branch with the four tunables and the bar-close stop" (typed item c). The baseline file stays unchanged (item 1). — RULED (typed item c; item 1 is RULED (D-2026-11-05-A)). The branch name is not ruled. → NEED
76:- The candidate set for each tunable, the exit-policy options, the ATR period behind the stop-ATR multiplier and the in-sample objective are not ruled. → NEEDS AMEAR 1–6.
```

```
$ sed -n '2435,2457p' DECISIONS.md | grep -c .
15
```

The core holds: option (b), the default, the arm's own entry before build, no 11:30 adoption, replication unchanged, not CONDITIONAL, not D2. Three things fail. One, the decision constrains D-2026-11-13-A parity with "backtest and live must carry the same stop". The entry drops that and writes "how backtest and live match for such an arm is for that arm's entry", which reopens what the decision closed (Defect 1). Two, the entry adds its own carve-out for arm (b)'s Flat1559: "whether it falls under this entry's rule is not decided here". The authority row says nothing about Flat1559. Arm (b) is the walk-forward tunables arm (walk-forward spec :70–72). The entry's own rule covers "11:30 or any other time" for that arm, so declining to decide whether it applies is both an addition and inconsistent with the rule (Defect 2). Three, the decision caps the entry at "at most ~12 lines", and the entry has 15 non-blank lines and 23 in all (Defect 3, minor).

### (c) No credit to Amear beyond V2 approval and the lock row; readings labelled; cited-line statements true — FAIL

```
$ for n in 2108 2116; do echo "--- $n"; awk -v n=$n 'NR==n' DECISIONS.md; done
--- 2108
**V2 — Rule F2-1: APPROVED (A6).** (return-handoff :45–48.) The words put to Amear were the channel's summary, return-handoff :46: "flat by 16:00 ET governs; a position open at 15:00 may stay open until 16:00; no new system entries 16:00–18:00 ET." Amear: "Uh, yeah, you have my approval." (return-handoff :47). It is filed as closing the A6 hold, that is, Amear's approval, the first of the three parts OPEN-F2-5 names at `docs/specs/2026-11-10-f2-session-flat-proposal.md`:79 (its resolution cell, copied by script: "Amear's approval under A6; then a DECISIONS.md entry and the amended #4/#5 text in the breaker spec."), on the words put to him at return-handoff :46. The amended #4/#5 text does not exist, and OPEN-F2-5 is not closed by this entry. Whether his approval reaches the elements (a)–(f) listed below, which were not put to him in those words, is not graded here. That file is called the proposal below. Rule F2-1 as the proposal writes it, copied by script from proposal :20:
--- 2116
Elements of the proposal's text that are not in the summary at return-handoff :46, listed without grading whether his approval reaches them: (a) the summary says "flat by 16:00 ET"; proposal :20 says "The closing order for every open system position is submitted no later than 16:00:00 ET"; (b) "(or no later than the exchange's early close on an early-close day)" (proposal :20); (c) "the position must be confirmed flat before MFFU's 4:10 PM ET auto-close" (proposal :20); (d) the summary's no-entry period is 16:00–18:00 ET; proposal :20 says "The system opens no new position from that flat time until 18:00 ET"; (e) from proposal :30: "New system entries between 15:00 and 16:00 are allowed under Rule F2-1, subject to breakers #1, #2, #3, #6, #7, #8 and #9." and "Between 15:00 and 18:00 ET Amear's own manual interaction is locked out"; (f) the proposed replacement text for breakers #4 and #5 (proposal :36, :38). DECISION_LOG.md:828 records V2 in the summary's terms.
```

```
$ f=docs/specs/2026-11-10-f2-session-flat-proposal.md; for n in 20 24 60; do echo "--- $n"; awk -v n=$n 'NR==n' $f; done
--- 20
**Rule F2-1. Deviation B's 16:00 ET session flat governs. The closing order for every open system position is submitted no later than 16:00:00 ET (or no later than the exchange's early close on an early-close day), and the position must be confirmed flat before MFFU's 4:10 PM ET auto-close. The system opens no new position from that flat time until 18:00 ET, when the next session begins.**
--- 24
- Strategies may flat earlier than 16:00 by their own rules (for example arm (b)'s Flat1559 exit policy). No system position may have its closing order sent later than the flat time.
--- 60
| Walk-forward arm (b) exit policy Flat1559 | Allowed: an earlier flat than 16:00. (`git show HEAD:docs/specs/2026-11-05-walk-forward-spec.md` is the authority; parked under `Praxis_build-diq`; not edited.) |
$ awk 'NR==20' $f | grep -cF 'Strategies may flat earlier'
0
```

Crediting passes. Amear is credited only with the V2 approval of the summary (:2108) and the lock row (:42, WHO "trader (Amear) + orchestrator (session 16)"). The proposal :24 sentence is explicitly not credited to him, and the Decision reasons carry the label "each the master's reading under D1, changeable by Amear". The statement about :2116 fails. The entry says "DECISIONS.md :2116 records that whether Amear's approval reaches proposal text outside the summary is not graded". Line :2116 records non-grading only for six listed elements, (a)–(f), drawn from proposal :20, :30, :36 and :38. Proposal :24 is not among them, and :2116 says nothing about it. The entry turns a closed list into a general rule, and it uses that rule to cover the very sentence (:24) the list leaves out (Defect 4). The authority row's weaker wording ("does not grade whether Amear's approval reaches it") is true. The entry's restatement is not. A minor point: the S6 readings ("an earlier stop would change the one trade list…") carry no per-reading master label. Only the Status line covers them (observation, not graded as a defect).

### (d) Every quote byte-present at its cited line; DECISIONS.md cites below 2280 — PASS

```
$ f=docs/specs/2026-07-16-b2-noise-area-ruleset.md; for q in 'Whether a strategy-level stop at 11:30 (a strategy rule, not a breaker) is still available to a later Noise-Area arm' 'Not chosen here.'; do awk 'NR==170' $f | grep -cF "$q"; done; for q in '2026-07-16T19:29Z' 'WHO: trader (Amear) + orchestrator (session 16)' 'session-flat = 16:00 ET cash close (NOT the 11:30 PRAXIS window)' 'FIRST build = pure paper replication with FIXED params'; do awk 'NR==42' DECISION_LOG.md | grep -cF "$q"; done
1
1
1
1
1
1
```

```
$ awk 'NR==2108' DECISIONS.md | grep -cF 'flat by 16:00 ET governs; a position open at 15:00 may stay open until 16:00'; awk 'NR==2116' DECISIONS.md | grep -cF 'listed without grading whether his approval reaches them'
1
1
$ cmp <(git show HEAD:DECISIONS.md | head -n 2279) <(head -n 2279 DECISIONS.md); echo "exit=$?"; cmp <(head -n 2434 DECISIONS.md) /tmp/oa2-pre-DECISIONS.md; echo "exit=$?"
exit=0
exit=0
```

```
$ awk 'NR==24' $f | grep -cF "Strategies may flat earlier than 16:00 by their own rules (for example arm (b)'s Flat1559 exit policy)"; awk 'NR==60' $f | grep -cF 'Allowed: an earlier flat than 16:00.'   (f = F2 proposal)
1
1
```

```
$ f=docs/specs/2026-11-05-phase3-build-specification.md; awk 'NR==212' $f | grep -cF 'clock reaches 16:00:00 ET'; awk 'NR==212' $f | grep -cF 'confirm flat before 4:10 PM ET (alert if not)'; awk 'NR==196' $f | grep -cF 'SPECIFIED ONLY — zero implemented, zero tested, zero tested under failure'; awk 'NR==111' specs/SPEC_RUBRIC.md | grep -cF '±15% win rate and ±25% average trade P&L'
1
1
1
1
$ git show HEAD:DECISIONS.md | grep -nF 'Every Block 2 run yields two series from one trade list.'
2301:**Decision 1: the Block 2 backtest runs both, and is graded with breakers.** Every Block 2 run yields two series from one trade list. The *without* series is the raw list as the strategy emits it (reverse-and-re-enter, 16:00 flat, no trade cap, no loser stop). The *with* series is that list after breakers #2 and #3 are applied to it after the run, Mac-side, by the rule below. Every Block 2 pass-gate value (arm (a) gates 1-5; arm (b) gates 1-6 and PBO) is computed on the with series. The without series is a record of what the breakers cost or saved; it is never graded.
$ git show HEAD:DECISIONS.md | grep -n '^## ' | tail -n 4
2205:## 2026-11-12 — D-2026-11-12-A: breakers #4 and #5 amended to match Rule F2-1 (rubric F2; master under D-2026-11-08-D D1)
2280:## 2026-11-12 — D-2026-11-12-C: Block 1 milestone scope — internal path only (rubric O3; master under D-2026-11-08-D D1)
2297:## 2026-11-13 — D-2026-11-13-A: Backtest-vs-live breaker parity (rubric O4; master under D-2026-11-08-D D1)
2326:## 2026-11-13 — D-2026-11-13-B: Breaker #4 cancel and confirm-flat placement (topology OPEN-A1; master under D-2026-11-08-D D1)
$ git show HEAD:DECISIONS.md | awk 'NR==2297' | grep -cF 'Backtest-vs-live breaker parity'
1
$ tail -n 23 DECISIONS.md | grep -oE ':[0-9]{4}\b' | sort -u
:2108
:2116
```

Two blocks in this section group commands from one compound invocation in my session, with `$f` as labelled. The outputs are as printed. The D-2026-11-13-A quote is at HEAD :2301, inside 2297–2325. The title quote sits in heading :2297. The only DECISIONS.md cites are :2108 and :2116, both below 2280. The source files have no uncommitted edits, except DECISION_LOG.md, whose diff is the new rows:

```
$ git diff --quiet HEAD -- $f docs/specs/2026-07-16-b2-noise-area-ruleset.md docs/specs/2026-11-05-phase3-build-specification.md specs/SPEC_RUBRIC.md DECISION_LOG.md; echo "srcs-vs-HEAD exit=$?"; git status --porcelain -- $f docs/specs/2026-07-16-b2-noise-area-ruleset.md docs/specs/2026-11-05-phase3-build-specification.md specs/SPEC_RUBRIC.md DECISION_LOG.md   ($f = docs/specs/2026-11-10-f2-session-flat-proposal.md)
srcs-vs-HEAD exit=1
 M DECISION_LOG.md
```

### (e) S2: nothing specified-only described as existing, carried, used, built or tested — PASS

Evidence: the entry text in (a). The breakers are "stay SPECIFIED ONLY … zero implemented, zero tested". The default uses "keeps", which is a rule, where the authority row has "carries". Arm (b)'s Flat1559 is attributed to "the proposal's text". The replication arm is "unchanged", which makes no build claim. The MANIFEST rows say "breakers stay SPECIFIED ONLY". One observation, not graded a defect: "the one trade list from which that entry's two series are drawn" uses the present tense of D-2026-11-13-A's rule. The rubric's O4 note says no with series exists yet. I read the sentence as describing the rule, not as a claim that the list exists.

### (f) S6 paragraph names the five items without resolving them — PASS

Evidence: the S6 paragraph in (a). The replication arm ("unchanged; lock items (1) and (3) govern it"), arm (b)'s Flat1559 ("neither adopts nor changes it"), D-2026-11-13-A parity ("for that arm's entry"), amended breaker #4 ("16:00 trigger is unchanged … for that arm's entry") and the Block 4 gate ("for that arm's entry") are all named, and none is resolved. Leaving parity open conflicts with the authority row, which is Defect 1 under (b). It does not make (f) fail.

### (g) Evidence report rules — FAIL

```
$ f=docs/reports/2026-11-13-open-a2-manager.md; wc -l $f; grep -n '^#' $f; echo ---; grep -c '^```' $f; echo "fences/2 = blocks"; tail -n 3 $f; echo ---; grep -nF 'Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.' $f; grep -nE 'T[B]D|evidenc[e]/|[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]' $f; echo "hyg-exit=$?"; grep -nE 'git status|diff --cached|ls ' $f
     223 docs/reports/2026-11-13-open-a2-manager.md
1:# 2026-11-13 — Unit 2026-11-13-open-a2 — manager evidence report
3:## Task
7:## Rubric criteria addressed
16:## Workers dispatched
22:## Process log
30:## Verification evidence (command output)
213:## S6 cross-block check
217:## Files staged
---
34
fences/2 = blocks
Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

Result: PASS
---
70:> Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
221:Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
hyg-exit=1
64:> **S6 cross-block.** Named here, not resolved. Replication arm: unchanged; lock items (1) and (3) govern it. Arm (b): the proposal's text names its Flat1559 exit policy as an earlier flat (proposal :24, :60); this entry neither adopts nor changes it, and whether it falls under this entry's rule is not decided here. D-2026-11-13-A parity: an earlier stop would change the one trade list from which that entry's two series are drawn; how backtest and live match for such an arm is for that arm's entry. Amended breaker #4 (spec :212): its 16:00 trigger is unchanged; how an earlier strategy stop sits with it is for that arm's entry. Block 4 gate (rubric :111): how an arm with an earlier stop meets it is for that arm's entry. No ruleset row, spec text or breaker text is edited.
70:> Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
202:$ tail -n 23 DECISIONS.md | grep -c 'Fills are optimistic'
209:$ git diff --cached --name-only | wc -l
```

```
$ grep -nE 'Zarattini|Davi' docs/reports/2026-11-13-open-a2-manager.md; echo "exit=$?"
exit=1
```

I re-ran these report commands literally (Blocks 4, 5, 6, 13 (:110), 14, 15, 16, 17, 11). All match the report:

```
$ git show HEAD:DECISIONS.md | head -n 2279 | cmp - <(head -n 2279 DECISIONS.md); echo "exit=$?"; head -n 2434 DECISIONS.md | cmp - /tmp/oa2-pre-DECISIONS.md; echo "exit=$?"; head -n 474 MANIFEST.md | cmp - /tmp/oa2-pre-MANIFEST.md; echo "exit=$?"; awk 'NR==110' specs/SPEC_RUBRIC.md | grep -cF "Block 4's gate compares live to"; for p in 'already' 'T[B]D' 'evidenc[e]/'; do tail -n 23 DECISIONS.md | grep -c "$p"; done; tail -n 23 DECISIONS.md | grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]'; tail -n 23 DECISIONS.md | grep -oE ':[0-9]{4}\b' | sort -u; tail -n 23 DECISIONS.md | grep -c 'Fills are optimistic'; git diff --cached --name-only | wc -l; git show HEAD:DECISIONS.md | grep -n '^## ' | awk -F: '$1>=2280'
exit=0
exit=0
exit=0
1
0
0
0
0
:2108
:2116
1
       1
2280:## 2026-11-12 — D-2026-11-12-C: Block 1 milestone scope — internal path only (rubric O3; master under D-2026-11-08-D D1)
2297:## 2026-11-13 — D-2026-11-13-A: Backtest-vs-live breaker parity (rubric O4; master under D-2026-11-08-D D1)
2326:## 2026-11-13 — D-2026-11-13-B: Breaker #4 cancel and confirm-flat placement (topology OPEN-A1; master under D-2026-11-08-D D1)
```

Passing parts:
- The report has 17 blocks, within the limit of 25.
- It pastes no `git status` and lists no evidence directory. `git diff --cached` appears only piped to `wc -l`, with output 1.
- It contains no evidenc[e]/ path, no email, no T[B]D and no third-party name.
- Every required block is present: wc, both full diffs, HEAD prefix cmp with exit, 1–2434 cmp, one check per Sources quote, the four hygiene counts and the index count.
- The S13 sentence appears once as a standalone line (:221), just above `Result:` (:223). The second occurrence (:70) is inside diff output, which the 17:22:34Z ruling permits.
- All sections are present and in order.
- Every line number it cites is correct: entry 2435–2457, rows 475–476, rubric :133/:134/:136/:138/:140/:145 (confirmed by grep in my session), HEAD :2280/:2297/:2301/:2326, rubric :110/:111.

Failing parts:
- The Workers table (:20) says "A cold adversary graded this unit before audit". The Process log (:28) says the adversary "was dispatched after this report was written". The report therefore states an outcome that had not happened when it was written, with no pasted evidence. That breaks S1 (Defect 5).
- Blocks 7–10 and 12–13 print several `$` command lines and then all the outputs together ("output in order"). A shell does not produce that layout. Either the displayed commands are not the literal invocation, or the outputs were rearranged after the fact (Defect 6, minor). The outputs themselves match my re-runs.

### (h) MANIFEST rows accurate against the diffs and report — PASS

Evidence: the MANIFEST diff in (a) and the report in (g). Row :475 matches the entry: option (b), the default, the arm's own entry before build, the S6 trio, replication unchanged, no 11:30 adoption, not CONDITIONAL, not D2, row :170 not edited, breakers SPECIFIED ONLY, F3 and F4 untouched. Row :476 matches the report's contents: pre-copies (Blocks 1, 5, 6), diffs (2, 3), HEAD prefix cmp (4), quote byte checks (7–13), S2 and hygiene counts (14), and entry text via the diff in Block 2. The rows repeat the entry's wording, so they share none of Defects 1–4 except by reference.

### (i) Structure: Status, Decision, Sources, S6, Limits, S4, S13 line — PASS

```
$ sed -n '2435,2457p' DECISIONS.md | grep -n -oE '^(## |\*\*Status:\*\*|\*\*Decision\.\*\*|\*\*Sources|\*\*S6 cross-block\.\*\*|\*\*Limits\.\*\*|\*\*S4 timing\.\*\*|Fills are optimistic)'
2:## 
4:**Status:**
6:**Decision.**
8:**Sources
17:**S6 cross-block.**
19:**Limits.**
21:**S4 timing.**
23:Fills are optimistic
```

## Defects

1. DECISIONS.md :2453 (S6 paragraph; Decision :2441 too): "D-2026-11-13-A parity: … how backtest and live match for such an arm is for that arm's entry." The 17:19:15Z decision fixes the parity constraint as "backtest and live must carry the same stop". The entry drops that and leaves open what the decision settled, so it does not file the decision exactly.
2. DECISIONS.md :2453: "Arm (b): … this entry neither adopts nor changes it, and whether it falls under this entry's rule is not decided here." This carve-out appears nowhere in the authority row. Arm (b) is the walk-forward tunables arm (walk-forward spec :70–72), and the entry's own rule covers "11:30 or any other time" for that arm. The clause is an addition, and it makes the rule's scope ambiguous.
3. DECISIONS.md :2435–2457: the entry has 15 non-blank lines (23 in all). The authority row caps it at "at most ~12 lines". Minor.
4. DECISIONS.md :2441: "DECISIONS.md :2116 records that whether Amear's approval reaches proposal text outside the summary is not graded." Line :2116 records non-grading only for listed elements (a)–(f), taken from proposal :20, :30, :36 and :38. Proposal :24 is not listed. The statement is false as a description of what that line records, and it is used to cover :24.
5. docs/reports/2026-11-13-open-a2-manager.md :20: "A cold adversary graded this unit before audit". Process log :28 says the adversary was dispatched after the report was written. The report states an outcome that had not happened and gives no evidence for it (S1).
6. docs/reports/2026-11-13-open-a2-manager.md :107–176 (Blocks 7–10, 12–13): several `$` lines are followed by all their outputs ("output in order"). That is not a literal transcript, so either the commands or the output layout were reconstructed. The outputs match my re-runs. Minor.

Result: FAIL
