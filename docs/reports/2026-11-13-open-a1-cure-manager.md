# Unit 2026-11-13-open-a1-cure: manager evidence report

Date: 2026-11-13. Bead Praxis_build-fgd, topology item OPEN-A1. Authority: DECISION_LOG 2026-11-13T13:37:42Z (cure plan items i to iv) and 2026-11-13T17:02:02Z (this dispatch, item v), both decided by master under D-2026-11-08-D D1. Fix pass: DECISION_LOG 2026-11-13T17:12:19Z, decided by master under D-2026-11-08-D D1.

## Task

Cure entry D-2026-11-13-B ("Breaker #4 cancel and confirm-flat placement") in DECISIONS.md by one deletion, one wording substitution ("already uses" becomes "names") and one named gap only, after its first audit FAIL (S2 over-statement in the Decision paragraph, missing breaker #1 gap in the S6 paragraph, S1 gaps in the earlier evidence report). Exactly five edits:

1. DECISIONS.md :2422 (Decision paragraph): the clause beginning ", and (a) keeps both actions on the order path ..." and ending "(topology :61)" is deleted; the sentence now ends "...depends on OPEN-T3 (topology :100), which is unresolved."
2. DECISIONS.md :2428 (S6 paragraph): the words "already uses for" become "names for".
3. DECISIONS.md :2428 (S6 paragraph): one named-gap sentence on breaker #1 (topology :58) is inserted before the closing sentence "Nothing else is edited." Under DECISION_LOG 2026-11-13T17:12:19Z the gap sentence then lost the word "also" (deletion only), so it reads "is specified as a FLATTEN command file".
4. DECISIONS.md :2425 (Sources, topology bullet): one quote of topology :58 is inserted before the :106 quote. It was byte-checked against the topology file before insertion and again in Block 10.
5. MANIFEST.md :474: one row appended for this report. Lines 1 to 473 are unchanged, including :471 (the entry's row) and :472 to :473. Under DECISION_LOG 2026-11-13T17:12:19Z the row's "one word replaced" became "two words replaced by one".

The entry spans DECISIONS.md :2417 to :2434 (2417 blank, heading at 2418). Its structure is Status (:2420), Decision (:2422), Sources (:2424 to :2426), S6 (:2428), Limits (:2430), S4 (:2432), then the S13 line (:2434), as listed in Block 18.

## Rubric criteria addressed

- S1 (specs/SPEC_RUBRIC.md :133): every claim below rests on pasted command output, run by this manager in this session.
- S2 (:134): the deleted clause called FLATTEN carried on an order path; FLATTEN is unbuilt (topology :99), so the clause is removed and "already uses" becomes "names". The added sentences call breaker #1's action "specified", not built.
- S6 (:138): the S6 paragraph now names breaker #1's "cancel all, flatten" action (topology :58) as an open gap.
- S13 (:145): the S13 sentence appears once, as the last line before the Result line.

## Workers dispatched

| id | mode | outcome |
|---|---|---|
| adversary-1 | ADVERSARIAL (cold, read-only) | A cold adversary graded this unit before audit; its report is not part of this commit. |

The five edits are four exact string replacements and one appended line, so the manager made them directly. No build worker was dispatched. The fix pass (one deletion, one rewording) also used no worker.

## Process log

1. Pre-images copied (Block 0). The topology :58 quote was byte-checked before edit 4 (the same check appears as Block 10).
2. Edits 1 to 4 were made as exact string replacements in DECISIONS.md. Edit 5 was a single appended line in MANIFEST.md.
3. All evidence commands (Blocks 1 to 21) were first run after edits 1 to 5 by this manager. After the fix pass (item 7), Blocks 1, 2, 3, 4, 10, 14, 15, 16, 17, 19, 20 and 21 were re-run with the identical commands, and their output here is from that re-run; Blocks 5 to 9, 11 to 13 and 18 are from the first run (the fix changes no line number and no spec or topology file). Block 22 was run once, after the fix pass. All output was captured verbatim into this file by a loop that prints each command and runs it.
4. Line :2434 (the entry's S13 line) is not printed in Block 20, because the S13 sentence may appear only once in this report. Block 19 shows that its SHA-256 matches the pre-copy's :2434, and Block 2 shows that diff reports no change outside :2422, :2425 and :2428.
5. Only one personal name appears in this report: the decision owner, in the entry's own Status line (Block 20), printed as part of the entry text. No email address appears. No path under the reports evidence directory appears; the evidence-path count in Block 16 uses the pattern `evidenc[e]/`. The owner's name in the quoted entry text is permitted under DECISION_LOG 2026-11-13T17:12:19Z (decided by master under D-2026-11-08-D D1).
6. The MANIFEST row at :474 was reworded from "one word replaced" to "two words replaced by one" under DECISION_LOG 2026-11-13T17:12:19Z (decided by master under D-2026-11-08-D D1).
7. Fix pass under DECISION_LOG 2026-11-13T17:12:19Z: new pre-images were copied (Block 0b); then at DECISIONS.md :2428 the gap sentence lost the word "also" (deletion only), and MANIFEST.md :474 was reworded as in item 6. Block 22 shows these are the only two changed lines against the new pre-images.

## Verification evidence (command output)

All commands were run from the repo root, /Volumes/Sensidine/Praxis.build.

Block 0 (unit start; run as the first two commands of a chained call, before any edit; cp prints nothing on success, so there was no output. Block 1 shows the pre-copies' line counts).

```
$ cp DECISIONS.md /tmp/oa1c-pre-DECISIONS.md && cp MANIFEST.md /tmp/oa1c-pre-MANIFEST.md
```

Block 0b (fix-pass start; run as the first two copy commands of a chained call, before fix edits A and B; cp prints nothing on success, so there was no output. Block 22 diffs against these copies).

```
$ cp DECISIONS.md /tmp/oa1f-pre-DECISIONS.md && cp MANIFEST.md /tmp/oa1f-pre-MANIFEST.md
```

Block 1.

```
$ wc -l /tmp/oa1c-pre-DECISIONS.md /tmp/oa1c-pre-MANIFEST.md DECISIONS.md MANIFEST.md
    2434 /tmp/oa1c-pre-DECISIONS.md
     473 /tmp/oa1c-pre-MANIFEST.md
    2434 DECISIONS.md
     474 MANIFEST.md
    5815 total
```

Block 2.

```
$ diff /tmp/oa1c-pre-DECISIONS.md DECISIONS.md
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
> **S6 cross-block.** Block 3 breakers and topology: the two #4 actions at spec :212 are placed inside FLATTEN, the same command topology :61 names for #4's "close positions" action; no topology row and no spec text is edited. OPEN-T2 (topology :99) stays open; under (a) the FLATTEN type it names is where both actions would live. OPEN-T3 (topology :100) stays open; option (b) waits on it under the void clause. Block 4 paper (topology :106): no Block 4 text is changed. Named gap: breaker #1's "cancel all, flatten" action (topology :58) is specified as a FLATTEN command file the consumer executes; whether #1's flatten carries the cancel and confirm-flat steps placed here for #4 is not decided here. Nothing else is edited.
```

Block 3.

```
$ diff /tmp/oa1c-pre-MANIFEST.md MANIFEST.md
473a474
> | /docs/reports/2026-11-13-open-a1-cure-manager.md | Report | 3 | 2026-11-13 | Evidence report for unit 2026-11-13-open-a1-cure (topology OPEN-A1, bead Praxis_build-fgd; master under D-2026-11-08-D D1, DECISION_LOG 2026-11-13T13:37:42Z and 2026-11-13T17:02:02Z): the cure of entry D-2026-11-13-B (one clause deleted in its Decision paragraph; two words replaced by one and one named gap on breaker #1 added in its S6 paragraph; one topology quote added to its Sources), with literal commands and full output. |
```

Block 4.

```
$ head -n 2416 /tmp/oa1c-pre-DECISIONS.md > /tmp/oa1c-pre-head2416.txt && head -n 2416 DECISIONS.md > /tmp/oa1c-post-head2416.txt && cmp /tmp/oa1c-pre-head2416.txt /tmp/oa1c-post-head2416.txt && echo "cmp exit=$? (lines 1-2416 identical)"
cmp exit=0 (lines 1-2416 identical)
```

Block 5.

```
$ awk 'NR==198' docs/specs/2026-11-10-live-signal-topology.md | grep -cF '(a) Both are part of the FLATTEN command the consumer executes at the flat time (the consumer cancels its own working entries and reports flat or not flat).'
1
```

Block 6.

```
$ awk 'NR==198' docs/specs/2026-11-10-live-signal-topology.md | grep -cF '(b) The confirmation is a separate n8n-side check on account state, which needs the account-state feed of OPEN-T3.'
1
```

Block 7.

```
$ awk 'NR==99' docs/specs/2026-11-10-live-signal-topology.md | grep -cF 'EXIT / FLATTEN types, unbuilt'
1
```

Block 8.

```
$ awk 'NR==100' docs/specs/2026-11-10-live-signal-topology.md | grep -cF 'Where account state (P&L, equity, fills, open position) comes from, and how fresh it must be.'
1
```

Block 9.

```
$ awk 'NR==61' docs/specs/2026-11-10-live-signal-topology.md | grep -cF 'Its "close positions" action: the emitter'"'"'s own time exit posted as a FLATTEN signal, plus the FLATTEN command from n8n at the gate time.'
1
```

Block 10.

```
$ awk 'NR==58' docs/specs/2026-11-10-live-signal-topology.md | grep -cF 'Its "cancel all, flatten" action: n8n writes a FLATTEN command file that the consumer executes'
1
```

Block 11.

```
$ awk 'NR==106' docs/specs/2026-11-10-live-signal-topology.md | grep -cF 'D8(8): the final step of this build is a Block 4 paper pass on MFFU sim; Block 5 live is a separate sign-off.'
1
```

Block 12.

```
$ awk 'NR==212' docs/specs/2026-11-05-phase3-build-specification.md | grep -cF 'cancel working entry orders, send market orders closing all system positions, confirm flat before 4:10 PM ET (alert if not)'
1
```

Block 13.

```
$ awk 'NR==196' docs/specs/2026-11-05-phase3-build-specification.md | grep -cF 'SPECIFIED ONLY — zero implemented, zero tested, zero tested under failure.'
1
```

Block 14.

```
$ awk 'NR>=2417' DECISIONS.md | grep -c 'already'
0
```

Block 15.

```
$ awk 'NR>=2417' DECISIONS.md | grep -c 'T[B]D'
0
```

Block 16.

```
$ awk 'NR>=2417' DECISIONS.md | grep -c 'evidenc[e]/'
0
```

Block 17.

```
$ awk 'NR>=2417' DECISIONS.md | grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]'
0
```

Block 18.

```
$ awk 'NR>=2417 && /^(## |\*\*)/ {print NR": "substr($0,1,40)}' DECISIONS.md
2418: ## 2026-11-13 — D-2026-11-13-B: Breake
2420: **Status:** Decided by master under D-20
2422: **Decision.** Option (a) of topology :19
2424: **Sources (quoted byte-exact).**
2428: **S6 cross-block.** Block 3 breakers and
2430: **Limits.** No code, no spec body and no
2432: **S4 timing.** Written 2026-11-13, befor
```

Block 19.

```
$ awk 'NR==2434' DECISIONS.md | shasum -a 256; awk 'NR==2434' /tmp/oa1c-pre-DECISIONS.md | shasum -a 256; awk 'NR==2434' DECISIONS.md | grep -c '^Fills are optimistic; Standard resolution on 1-minute bars'
bfd49f07fa5ca6e7e3728cb1924065e5465774ce3c01e09526b7b265fa45a34d  -
bfd49f07fa5ca6e7e3728cb1924065e5465774ce3c01e09526b7b265fa45a34d  -
1
```

Block 20.

```
$ awk 'NR>=2417 && NR<=2433' DECISIONS.md

## 2026-11-13 — D-2026-11-13-B: Breaker #4 cancel and confirm-flat placement (topology OPEN-A1; master under D-2026-11-08-D D1)

**Status:** Decided by master under D-2026-11-08-D D1 (DECISION_LOG 2026-11-13T13:29:04Z), changeable by Amear. Not Amear's ruling. A written statement only (bead `Praxis_build-fgd`, topology item OPEN-A1). The part marked CONDITIONAL rests on a mechanism nobody has observed and carries a void clause.

**Decision.** Option (a) of topology :198: amended #4's "cancel working entry orders" and "confirm flat before 4:10 PM ET (alert if not)" (spec :212) are both part of the FLATTEN command the consumer executes at the flat time; the consumer cancels its own working entries and reports flat or not flat. The master's reason: option (b) depends on OPEN-T3 (topology :100), which is unresolved. CONDITIONAL: this rests on the unobserved mechanism that the consumer can see and cancel its own working entry orders and read its own position; FLATTEN as an instruction type is unbuilt (OPEN-T2, topology :99). Void clause: if either is observed false, the placement is re-decided toward (b) after OPEN-T3. Named gap: where the "alert" goes is not decided here. Not a D2 item (no money, no live path switched on, no breaker value, no credential). OPEN-A2 is not decided here.

**Sources (quoted byte-exact).**
- Topology `docs/specs/2026-11-10-live-signal-topology.md`: :198 "(a) Both are part of the FLATTEN command the consumer executes at the flat time (the consumer cancels its own working entries and reports flat or not flat)." and "(b) The confirmation is a separate n8n-side check on account state, which needs the account-state feed of OPEN-T3."; :99 "EXIT / FLATTEN types, unbuilt"; :100 "Where account state (P&L, equity, fills, open position) comes from, and how fresh it must be."; :61 "Its "close positions" action: the emitter's own time exit posted as a FLATTEN signal, plus the FLATTEN command from n8n at the gate time."; :58 "Its "cancel all, flatten" action: n8n writes a FLATTEN command file that the consumer executes"; :106 "D8(8): the final step of this build is a Block 4 paper pass on MFFU sim; Block 5 live is a separate sign-off."
- Phase 3 spec `docs/specs/2026-11-05-phase3-build-specification.md`: :212 "cancel working entry orders, send market orders closing all system positions, confirm flat before 4:10 PM ET (alert if not)"; :196 "SPECIFIED ONLY — zero implemented, zero tested, zero tested under failure."

**S6 cross-block.** Block 3 breakers and topology: the two #4 actions at spec :212 are placed inside FLATTEN, the same command topology :61 names for #4's "close positions" action; no topology row and no spec text is edited. OPEN-T2 (topology :99) stays open; under (a) the FLATTEN type it names is where both actions would live. OPEN-T3 (topology :100) stays open; option (b) waits on it under the void clause. Block 4 paper (topology :106): no Block 4 text is changed. Named gap: breaker #1's "cancel all, flatten" action (topology :58) is specified as a FLATTEN command file the consumer executes; whether #1's flatten carries the cancel and confirm-flat steps placed here for #4 is not decided here. Nothing else is edited.

**Limits.** No code, no spec body and no breaker value is changed. The nine breakers stay SPECIFIED ONLY (spec :196): zero implemented, zero tested. This entry does not touch F3 or F4.

**S4 timing.** Written 2026-11-13, before the work it governs: FLATTEN is unbuilt (topology :99) and no breaker is implemented (spec :196). Chain: D-2026-11-08-D D1 → DECISION_LOG 2026-11-13T13:29:04Z (WHO: praxis-master).

```

Block 21.

```
$ git diff --cached --name-only | wc -l
       1
```

Block 22 (run after the fix pass; it compares against the fix-pass pre-images of Block 0b).

```
$ diff /tmp/oa1f-pre-DECISIONS.md DECISIONS.md; diff /tmp/oa1f-pre-MANIFEST.md MANIFEST.md
2428c2428
< **S6 cross-block.** Block 3 breakers and topology: the two #4 actions at spec :212 are placed inside FLATTEN, the same command topology :61 names for #4's "close positions" action; no topology row and no spec text is edited. OPEN-T2 (topology :99) stays open; under (a) the FLATTEN type it names is where both actions would live. OPEN-T3 (topology :100) stays open; option (b) waits on it under the void clause. Block 4 paper (topology :106): no Block 4 text is changed. Named gap: breaker #1's "cancel all, flatten" action (topology :58) is also specified as a FLATTEN command file the consumer executes; whether #1's flatten carries the cancel and confirm-flat steps placed here for #4 is not decided here. Nothing else is edited.
---
> **S6 cross-block.** Block 3 breakers and topology: the two #4 actions at spec :212 are placed inside FLATTEN, the same command topology :61 names for #4's "close positions" action; no topology row and no spec text is edited. OPEN-T2 (topology :99) stays open; under (a) the FLATTEN type it names is where both actions would live. OPEN-T3 (topology :100) stays open; option (b) waits on it under the void clause. Block 4 paper (topology :106): no Block 4 text is changed. Named gap: breaker #1's "cancel all, flatten" action (topology :58) is specified as a FLATTEN command file the consumer executes; whether #1's flatten carries the cancel and confirm-flat steps placed here for #4 is not decided here. Nothing else is edited.
474c474
< | /docs/reports/2026-11-13-open-a1-cure-manager.md | Report | 3 | 2026-11-13 | Evidence report for unit 2026-11-13-open-a1-cure (topology OPEN-A1, bead Praxis_build-fgd; master under D-2026-11-08-D D1, DECISION_LOG 2026-11-13T13:37:42Z and 2026-11-13T17:02:02Z): the cure of entry D-2026-11-13-B (one clause deleted in its Decision paragraph; one word replaced and one named gap on breaker #1 added in its S6 paragraph; one topology quote added to its Sources), with literal commands and full output. |
---
> | /docs/reports/2026-11-13-open-a1-cure-manager.md | Report | 3 | 2026-11-13 | Evidence report for unit 2026-11-13-open-a1-cure (topology OPEN-A1, bead Praxis_build-fgd; master under D-2026-11-08-D D1, DECISION_LOG 2026-11-13T13:37:42Z and 2026-11-13T17:02:02Z): the cure of entry D-2026-11-13-B (one clause deleted in its Decision paragraph; two words replaced by one and one named gap on breaker #1 added in its S6 paragraph; one topology quote added to its Sources), with literal commands and full output. |
```

## Adversarial findings

A cold adversary graded this unit before audit; its report is not part of this commit.

## S6 cross-block check

The entry touches Block 3 (breakers, spec :212 and :196) and the live-signal topology (:58, :61, :99, :100, :106, :198). Block 4 paper (topology :106) is cited and left unchanged. This cure edits no spec or topology file. Its only cross-block change is the added named gap: breaker #1's FLATTEN command file (topology :58, Block 10) may or may not carry the cancel and confirm-flat steps placed for #4, and the entry leaves this undecided. Blocks 5 to 13 show that every quote in the entry's Sources is byte-present at its cited line.

## Files staged

None. This unit staged nothing. Block 21 shows the index holds 1 path. This unit ran no git add and no other staging command. DECISIONS.md and MANIFEST.md are modified in the working tree and left unstaged for the master.

## Master rulings

Under DECISION_LOG 2026-11-13T17:12:19Z, the no-name rule covers third parties only, so the owner's name in the quoted entry text (Block 20) is permitted. Under the same row, MANIFEST.md :474 says "two words replaced by one" in place of "one word replaced" (Block 3, Block 22). Under the same row, the word "also" is deleted from the gap sentence at DECISIONS.md :2428 (Block 2, Block 22).

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
Result: PASS
