# 2026-11-13 — Unit 2026-11-13-open-a2 — manager evidence report

## Task

File ruleset item OPEN-A2 (bead `Praxis_build-fgd`) as DECISIONS.md entry D-2026-11-13-C, "Strategy-level stop before 16:00 for a later Noise-Area arm", with two MANIFEST.md rows, as decided by master under D-2026-11-08-D D1 at DECISION_LOG 2026-11-13T17:19:15Z, continued under DECISION_LOG 2026-11-13T17:22:34Z. This report is written from scratch; every command below was run by this manager in this session.

## Rubric criteria addressed

- S1 (`specs/SPEC_RUBRIC.md` :133): every claim below rests on pasted command output.
- S2 (:134): the entry describes no specified-only item as built; the breakers stay SPECIFIED ONLY.
- S4 (:136): the entry is written before any arm it governs is built, with the chain D-2026-11-08-D D1 → DECISION_LOG 2026-11-13T17:19:15Z.
- S6 (:138): the entry's S6 paragraph names the cross-block items without resolving them.
- S8 (:140): no reading is credited to Amear; the reasons are labelled the master's.
- S13 (:145): the entry carries the standing sentence once; this report carries it once as a standalone line.

## Workers dispatched

| id | mode | outcome |
|---|---|---|
| worker 1 | ADVERSARIAL, read-only, cold | A cold adversary graded this unit before audit; its report is not part of this commit. It returned FAIL; the changes made in response are listed in the Process log, steps 6 to 8. |

## Process log

1. A previous manager appended entry D-2026-11-13-C to DECISIONS.md (lines 2435–2457) and the two MANIFEST.md rows (lines 475–476), then stopped on a brief conflict before writing a report or running an adversary. The conflict (the S13 sentence appearing inside a full diff versus the once-only rule) was ruled at DECISION_LOG 2026-11-13T17:22:34Z: the once-rule counts standalone lines.
2. This manager did not write the entry or the rows. It read the entry in full against the 17:19:15Z decision: option (b) with the stated default; earlier stop only through the arm's own entry, before build, graded under S6 against D-2026-11-13-A, amended breaker #4 and the Block 4 gate; replication arm unchanged; no arm adopts an 11:30 stop; reasons labelled the master's; proposal :24 not credited to Amear; not CONDITIONAL; not D2; ruleset row :170 not edited.
3. The pre-copies `/tmp/oa2-pre-DECISIONS.md` and `/tmp/oa2-pre-MANIFEST.md` were not recopied.
4. Every check below was re-run by this manager. All commands ran from the repo root, `/Volumes/Sensidine/Praxis.build`.
5. One cold adversary was dispatched after a first draft of this report was written. It returned FAIL.
6. Changes to the entry in response, each a deletion only (no words added), all inside DECISIONS.md lines 2435–2457:
   - Decision paragraph (line 2440): deleted the clause `, and DECISIONS.md :2116 records that whether Amear's approval reaches proposal text outside the summary is not graded`. Reason: line 2116 lists six named elements (a) to (f) as not graded, and proposal :24 is not among them, so the clause stated more than that line records.
   - Sources, DECISIONS.md bullet (line 2445): deleted `; :2116 "listed without grading whether his approval reaches them"`, the quote that supported only the deleted clause.
   - S6 paragraph (line 2451): deleted `, and whether it falls under this entry's rule is not decided here` after the arm (b) Flat1559 sentence. Reason: a carve-out not in the 17:19:15Z decision.
   - S6 paragraph (line 2451): deleted `; how backtest and live match for such an arm is for that arm's entry` after the D-2026-11-13-A sentence. Reason: the 17:19:15Z decision holds the later arm's entry to D-2026-11-13-A parity (backtest and live carry the same stop); the clause read as leaving that open.
   The entry is still lines 2435–2457 (23 lines; no line added or removed). MANIFEST.md rows 475–476 are unchanged; neither row names a deleted clause.
7. Not changed: the adversary also noted the entry has 15 non-blank lines against the decision's "at most ~12 lines". Not fixed: the only deletions that would shorten it remove Sources quotes that carry byte evidence. Left for the master and the auditor.
8. Changes to this report in response: the Workers table and this Process log now state the adversary's outcome; multi-command blocks now show each command directly followed by its own output; every block touching DECISIONS.md was re-run after the deletions and the fresh output pasted (Blocks 1, 2, 4, 5, 9, 14, 15, 16, 17).

## Verification evidence (command output)

Block 1 — sizes of both files and both pre-copies.

```
$ wc -l DECISIONS.md MANIFEST.md /tmp/oa2-pre-DECISIONS.md /tmp/oa2-pre-MANIFEST.md
    2457 DECISIONS.md
     476 MANIFEST.md
    2434 /tmp/oa2-pre-DECISIONS.md
     474 /tmp/oa2-pre-MANIFEST.md
    5841 total
```

Block 2 — full diff of DECISIONS.md against its pre-copy.

```
$ diff /tmp/oa2-pre-DECISIONS.md DECISIONS.md; echo "exit=$?"
2434a2435,2457
> 
> ## 2026-11-13 — D-2026-11-13-C: Strategy-level stop before 16:00 for a later Noise-Area arm (ruleset OPEN-A2; master under D-2026-11-08-D D1)
> 
> **Status:** Decided by master under D-2026-11-08-D D1 (DECISION_LOG 2026-11-13T17:19:15Z), changeable by Amear. Not Amear's ruling. A written statement only (bead `Praxis_build-fgd`, ruleset item OPEN-A2). Not CONDITIONAL: it rests on no unobserved mechanism. Not a D2 item (no money, no live path, no breaker value, no credential).
> 
> **Decision.** Option (b) of ruleset :170, with a stated default. DEFAULT: every Noise-Area arm keeps lock item (1)'s full-day window to the 16:00 ET flat. An earlier strategy-level stop (11:30 or any other time) is allowed for a later arm (the walk-forward tunables arm or the live emitter) ONLY through that arm's own DECISIONS.md entry, written before the arm is built (S4) and graded under S6 against entry D-2026-11-13-A (backtest-vs-live parity), amended breaker #4 (the 16:00 backstop, unchanged) and the Block 4 gate. The replication arm is unchanged. No arm adopts an 11:30 stop by this entry. Reasons, each the master's reading under D1, changeable by Amear: lock item (3) scopes the "FIRST build" to paper replication; Amear's V2 approval was given on the summary "flat by 16:00 ET governs", which sets a latest flat, not an earliest; the sentence "Strategies may flat earlier than 16:00 by their own rules" (proposal :24) is the proposal's text, adopted by the master. Neither that sentence nor any reading here is credited to Amear.
> 
> **Sources (quoted byte-exact).**
> - Ruleset `docs/specs/2026-07-16-b2-noise-area-ruleset.md` :170 "Whether a strategy-level stop at 11:30 (a strategy rule, not a breaker) is still available to a later Noise-Area arm" and "Not chosen here."
> - Lock row `DECISION_LOG.md` :42 (stamp 2026-07-16T19:29Z; "WHO: trader (Amear) + orchestrator (session 16)"): item (1) "session-flat = 16:00 ET cash close (NOT the 11:30 PRAXIS window)"; item (3) "FIRST build = pure paper replication with FIXED params".
> - `DECISIONS.md` :2108 "flat by 16:00 ET governs; a position open at 15:00 may stay open until 16:00".
> - F2 proposal `docs/specs/2026-11-10-f2-session-flat-proposal.md`: :24 "Strategies may flat earlier than 16:00 by their own rules (for example arm (b)'s Flat1559 exit policy)"; :60 "Allowed: an earlier flat than 16:00."
> - Entry D-2026-11-13-A, "Backtest-vs-live breaker parity": "Every Block 2 run yields two series from one trade list."
> - Phase 3 spec `docs/specs/2026-11-05-phase3-build-specification.md`: :212 "clock reaches 16:00:00 ET" and "confirm flat before 4:10 PM ET (alert if not)"; :196 "SPECIFIED ONLY — zero implemented, zero tested, zero tested under failure".
> - Rubric `specs/SPEC_RUBRIC.md` :111 "±15% win rate and ±25% average trade P&L".
> 
> **S6 cross-block.** Named here, not resolved. Replication arm: unchanged; lock items (1) and (3) govern it. Arm (b): the proposal's text names its Flat1559 exit policy as an earlier flat (proposal :24, :60); this entry neither adopts nor changes it. D-2026-11-13-A parity: an earlier stop would change the one trade list from which that entry's two series are drawn. Amended breaker #4 (spec :212): its 16:00 trigger is unchanged; how an earlier strategy stop sits with it is for that arm's entry. Block 4 gate (rubric :111): how an arm with an earlier stop meets it is for that arm's entry. No ruleset row, spec text or breaker text is edited.
> 
> **Limits.** No code, no spec body and no breaker value is changed. The ruleset row :170 is not edited. The nine breakers stay SPECIFIED ONLY (spec :196): zero implemented, zero tested. This entry does not touch F3 or F4.
> 
> **S4 timing.** Written 2026-11-13. It governs future arm entries only: each later arm's earlier stop must be filed in that arm's own entry before that arm is built. Chain: D-2026-11-08-D D1 → DECISION_LOG 2026-11-13T17:19:15Z (WHO: praxis-master).
> 
> Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
exit=1
```

Block 3 — full diff of MANIFEST.md against its pre-copy.

```
$ diff /tmp/oa2-pre-MANIFEST.md MANIFEST.md; echo "exit=$?"
474a475,476
> | /DECISIONS.md | Log | 3 | 2026-11-13 | AMENDMENT ROW (append-only registry). Unit 2026-11-13-open-a2 (ruleset OPEN-A2, bead Praxis_build-fgd; master under D-2026-11-08-D D1, DECISION_LOG 2026-11-13T17:19:15Z): appends entry D-2026-11-13-C, "Strategy-level stop before 16:00 for a later Noise-Area arm", filing option (b) with a stated default: every Noise-Area arm keeps lock item (1)'s full-day window to the 16:00 ET flat; an earlier strategy-level stop is allowed for a later arm only through that arm's own DECISIONS.md entry, written before the arm is built and graded under S6 against D-2026-11-13-A, amended breaker #4 and the Block 4 gate. Replication arm unchanged; no arm adopts an 11:30 stop; reasons labelled the master's reading, none credited to Amear. Not CONDITIONAL, not D2. No code, no breaker value, no spec body changed; ruleset row :170 not edited; breakers stay SPECIFIED ONLY; F3 and F4 untouched. |
> | /docs/reports/2026-11-13-open-a2-manager.md | Report | 3 | 2026-11-13 | Evidence report for unit 2026-11-13-open-a2 (ruleset OPEN-A2, bead Praxis_build-fgd; master under D-2026-11-08-D D1, DECISION_LOG 2026-11-13T17:19:15Z): the filing of entry D-2026-11-13-C and its two MANIFEST rows, with literal commands and full output (pre-copies, diffs, HEAD prefix cmp, quote byte checks, S2 and hygiene counts, entry text). |
exit=1
```

Block 4 — DECISIONS.md lines 1–2279 equal HEAD.

```
$ git show HEAD:DECISIONS.md | head -n 2279 | cmp - <(head -n 2279 DECISIONS.md); echo "exit=$?"
exit=0
```

Block 5 — DECISIONS.md lines 1–2434 equal the pre-copy.

```
$ head -n 2434 DECISIONS.md | cmp - /tmp/oa2-pre-DECISIONS.md; echo "exit=$?"
exit=0
```

Block 6 — MANIFEST.md lines 1–474 equal the pre-copy.

```
$ head -n 474 MANIFEST.md | cmp - /tmp/oa2-pre-MANIFEST.md; echo "exit=$?"
exit=0
```

Block 7 — ruleset quotes at :170 (two commands, each followed by its output).

```
$ awk 'NR==170' docs/specs/2026-07-16-b2-noise-area-ruleset.md | grep -cF 'Whether a strategy-level stop at 11:30 (a strategy rule, not a breaker) is still available to a later Noise-Area arm'
1
$ awk 'NR==170' docs/specs/2026-07-16-b2-noise-area-ruleset.md | grep -cF 'Not chosen here.'
1
```

Block 8 — lock row quotes at DECISION_LOG.md :42 (stamp, WHO, item (1), item (3); four commands, each followed by its output).

```
$ awk 'NR==42' DECISION_LOG.md | grep -cF '2026-07-16T19:29Z'
1
$ awk 'NR==42' DECISION_LOG.md | grep -cF 'WHO: trader (Amear) + orchestrator (session 16)'
1
$ awk 'NR==42' DECISION_LOG.md | grep -cF 'session-flat = 16:00 ET cash close (NOT the 11:30 PRAXIS window)'
1
$ awk 'NR==42' DECISION_LOG.md | grep -cF 'FIRST build = pure paper replication with FIXED params'
1
```

Block 9 — DECISIONS.md quote at :2108 (below line 2280), the only DECISIONS.md line the entry now cites; then, for the Process log step 6 deletion, what line 2116 lists: its element labels, and zero hits for the proposal :24 sentence and for Flat1559 (four commands, each followed by its output).

```
$ awk 'NR==2108' DECISIONS.md | grep -cF 'flat by 16:00 ET governs; a position open at 15:00 may stay open until 16:00'
1
$ awk 'NR==2116' DECISIONS.md | grep -oE '\([a-f]\) ' | tr -d '\n'; echo
(a) (b) (c) (d) (e) (f) 
$ awk 'NR==2116' DECISIONS.md | grep -cF 'Strategies may flat earlier'
0
$ awk 'NR==2116' DECISIONS.md | grep -c 'Flat1559'
0
```

Block 10 — F2 proposal quotes at :24 and :60 (two commands, each followed by its output).

```
$ awk 'NR==24' docs/specs/2026-11-10-f2-session-flat-proposal.md | grep -cF "Strategies may flat earlier than 16:00 by their own rules (for example arm (b)'s Flat1559 exit policy)"
1
$ awk 'NR==60' docs/specs/2026-11-10-f2-session-flat-proposal.md | grep -cF 'Allowed: an earlier flat than 16:00.'
1
```

Block 11 — the D-2026-11-13-A quote in HEAD's DECISIONS.md: its line number, its count, and the HEAD headings from line 2280 on (three commands, each followed by its output). The quote is at HEAD line 2301, inside the D-2026-11-13-A entry, which runs from its heading at 2297 to the next heading at 2326.

```
$ git show HEAD:DECISIONS.md | grep -nF 'Every Block 2 run yields two series from one trade list.' | cut -d: -f1
2301
$ git show HEAD:DECISIONS.md | grep -cF 'Every Block 2 run yields two series from one trade list.'
1
$ git show HEAD:DECISIONS.md | grep -n '^## ' | awk -F: '$1>=2280'
2280:## 2026-11-12 — D-2026-11-12-C: Block 1 milestone scope — internal path only (rubric O3; master under D-2026-11-08-D D1)
2297:## 2026-11-13 — D-2026-11-13-A: Backtest-vs-live breaker parity (rubric O4; master under D-2026-11-08-D D1)
2326:## 2026-11-13 — D-2026-11-13-B: Breaker #4 cancel and confirm-flat placement (topology OPEN-A1; master under D-2026-11-08-D D1)
```

Block 12 — Phase 3 spec quotes at :212 (two) and :196 (one); three commands, each followed by its output.

```
$ awk 'NR==212' docs/specs/2026-11-05-phase3-build-specification.md | grep -cF 'clock reaches 16:00:00 ET'
1
$ awk 'NR==212' docs/specs/2026-11-05-phase3-build-specification.md | grep -cF 'confirm flat before 4:10 PM ET (alert if not)'
1
$ awk 'NR==196' docs/specs/2026-11-05-phase3-build-specification.md | grep -cF 'SPECIFIED ONLY — zero implemented, zero tested, zero tested under failure'
1
```

Block 13 — rubric quote at :111, and the Block 4 gate wording on the line above it (:110); two commands, each followed by its output.

```
$ awk 'NR==111' specs/SPEC_RUBRIC.md | grep -cF '±15% win rate and ±25% average trade P&L'
1
$ awk 'NR==110' specs/SPEC_RUBRIC.md | grep -cF "Block 4's gate compares live to"
1
```

Block 14 — hygiene counts on the entry range (the last 23 lines are 2435–2457); four commands, each followed by its output, all expected 0.

```
$ tail -n 23 DECISIONS.md | grep -c 'already'
0
$ tail -n 23 DECISIONS.md | grep -c 'T[B]D'
0
$ tail -n 23 DECISIONS.md | grep -c 'evidenc[e]/'
0
$ tail -n 23 DECISIONS.md | grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]'
0
```

Block 15 — every four-digit line cite in the entry range (the one DECISIONS.md cite; below 2280).

```
$ tail -n 23 DECISIONS.md | grep -oE ':[0-9]{4}\b' | sort -u
:2108
```

Block 16 — the entry carries the standing sentence once.

```
$ tail -n 23 DECISIONS.md | grep -c 'Fills are optimistic'
1
```

Block 17 — index count (expected 1, unchanged; nothing staged by this unit).

```
$ git diff --cached --name-only | wc -l
       1
```

## S6 cross-block check

The entry's S6 paragraph (Block 2, the "S6 cross-block." line, DECISIONS.md line 2451) names five items and resolves none: the replication arm (unchanged; lock items (1) and (3) govern it); arm (b)'s Flat1559 exit policy (proposal :24, :60; the entry neither adopts nor changes it); D-2026-11-13-A parity (an earlier stop would change the one trade list from which that entry's two series are drawn; the Decision paragraph holds any later arm's entry to grading against D-2026-11-13-A); amended breaker #4 (spec :212; 16:00 trigger unchanged; how an earlier stop sits with it is left to that arm's entry); and the Block 4 gate (rubric :111; left to that arm's entry). This unit changes no code, spec body, breaker value or ruleset row (Blocks 2 and 3 show only appended lines). The breakers stay SPECIFIED ONLY (spec :196, Block 12).

## Files staged

None. This unit stages nothing (Block 17: index count 1, as before the unit). Working-tree changes left for the master: DECISIONS.md lines 2435–2457, MANIFEST.md lines 475–476, and this report.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

Result: PASS
