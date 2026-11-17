# Manager report — unit 2026-11-13-open-a1 (bead Praxis_build-fgd, topology OPEN-A1)

## Task
File entry D-2026-11-13-B at the end of DECISIONS.md: the master's decision (DECISION_LOG 2026-11-13T13:29:04Z, under D-2026-11-08-D D1) that amended breaker #4's cancel and confirm-flat actions sit inside the FLATTEN command (topology :198 option (a)). Filing only; the manager chose nothing. Plus three MANIFEST rows.

## Rubric criteria addressed
S4 (entry with authorisation chain, written before the work), S6 (cross-block paragraph in the entry), S13 (standing sentence once in entry and in each report). `specs/SPEC_RUBRIC.md` :133, :135, :142.

## Workers dispatched
- worker1, ADVERSARIAL, read-only, one round: checks (a)-(g). Outcome below.
- No BUILD worker: the edit is two heredoc appends written by the manager under the brief's explicit write instructions.

## Process log
Read rubric, the cited lines and the row; byte-checked eight planned quotes before writing; took pre-copies; appended entry and MANIFEST rows; computed diffs, prefix identity and sha256; dispatched one cold adversary with artifact, pre-copies, row text and cited files only.

## Verification evidence (command output)
```
$ git diff --cached --name-only | wc -l   (start of unit)
       1
$ wc -l /tmp/oa1-pre-DECISIONS.md /tmp/oa1-pre-MANIFEST.md DECISIONS.md MANIFEST.md
    2416 /tmp/oa1-pre-DECISIONS.md
     470 /tmp/oa1-pre-MANIFEST.md
    2434 DECISIONS.md
     473 MANIFEST.md
    5793 total
$ head -n 2416 DECISIONS.md | cmp - /tmp/oa1-pre-DECISIONS.md && echo "DECISIONS prefix identical"
DECISIONS prefix identical
$ head -n 470 MANIFEST.md | cmp - /tmp/oa1-pre-MANIFEST.md && echo "MANIFEST prefix identical"
MANIFEST prefix identical
$ diff /tmp/oa1-pre-DECISIONS.md DECISIONS.md | sed '3s/^> .*/> [S13 standing sentence, elided by this sed so the report carries it once]/'
2414a2415,2426
> 
> [S13 standing sentence, elided by this sed so the report carries it once]
> 
> ## 2026-11-13 — D-2026-11-13-B: Breaker #4 cancel and confirm-flat placement (topology OPEN-A1; master under D-2026-11-08-D D1)
> 
> **Status:** Decided by master under D-2026-11-08-D D1 (DECISION_LOG 2026-11-13T13:29:04Z), changeable by Amear. Not Amear's ruling. A written statement only (bead `Praxis_build-fgd`, topology item OPEN-A1). The part marked CONDITIONAL rests on a mechanism nobody has observed and carries a void clause.
> 
> **Decision.** Option (a) of topology :198: amended #4's "cancel working entry orders" and "confirm flat before 4:10 PM ET (alert if not)" (spec :212) are both part of the FLATTEN command the consumer executes at the flat time; the consumer cancels its own working entries and reports flat or not flat. The master's reason: option (b) depends on OPEN-T3 (topology :100), which is unresolved, and (a) keeps both actions on the order path that already carries FLATTEN (topology :61). CONDITIONAL: this rests on the unobserved mechanism that the consumer can see and cancel its own working entry orders and read its own position; FLATTEN as an instruction type is unbuilt (OPEN-T2, topology :99). Void clause: if either is observed false, the placement is re-decided toward (b) after OPEN-T3. Named gap: where the "alert" goes is not decided here. Not a D2 item (no money, no live path switched on, no breaker value, no credential). OPEN-A2 is not decided here.
> 
> **Sources (quoted byte-exact).**
> - Topology `docs/specs/2026-11-10-live-signal-topology.md`: :198 "(a) Both are part of the FLATTEN command the consumer executes at the flat time (the consumer cancels its own working entries and reports flat or not flat)." and "(b) The confirmation is a separate n8n-side check on account state, which needs the account-state feed of OPEN-T3."; :99 "EXIT / FLATTEN types, unbuilt"; :100 "Where account state (P&L, equity, fills, open position) comes from, and how fresh it must be."; :61 "Its "close positions" action: the emitter's own time exit posted as a FLATTEN signal, plus the FLATTEN command from n8n at the gate time."; :106 "D8(8): the final step of this build is a Block 4 paper pass on MFFU sim; Block 5 live is a separate sign-off."
> - Phase 3 spec `docs/specs/2026-11-05-phase3-build-specification.md`: :212 "cancel working entry orders, send market orders closing all system positions, confirm flat before 4:10 PM ET (alert if not)"; :196 "SPECIFIED ONLY — zero implemented, zero tested, zero tested under failure."
2415a2428,2433
> **S6 cross-block.** Block 3 breakers and topology: the two #4 actions at spec :212 are placed inside FLATTEN, the same command topology :61 already uses for #4's "close positions" action; no topology row and no spec text is edited. OPEN-T2 (topology :99) stays open; under (a) the FLATTEN type it names is where both actions would live. OPEN-T3 (topology :100) stays open; option (b) waits on it under the void clause. Block 4 paper (topology :106): no Block 4 text is changed. Nothing else is edited.
> 
> **Limits.** No code, no spec body and no breaker value is changed. The nine breakers stay SPECIFIED ONLY (spec :196): zero implemented, zero tested. This entry does not touch F3 or F4.
> 
> **S4 timing.** Written 2026-11-13, before the work it governs: FLATTEN is unbuilt (topology :99) and no breaker is implemented (spec :196). Chain: D-2026-11-08-D D1 → DECISION_LOG 2026-11-13T13:29:04Z (WHO: praxis-master).
> 
$ diff /tmp/oa1-pre-MANIFEST.md MANIFEST.md
470a471,473
> | /DECISIONS.md | Log | 3 | 2026-11-13 | AMENDMENT ROW (append-only registry). Unit 2026-11-13-open-a1 (topology OPEN-A1, bead Praxis_build-fgd; master under D-2026-11-08-D D1, DECISION_LOG 2026-11-13T13:29:04Z): appends entry D-2026-11-13-B, "Breaker #4 cancel and confirm-flat placement", filing option (a): amended breaker #4's cancel of working entry orders and its confirm-flat check are both part of the FLATTEN command the consumer executes at the flat time. CONDITIONAL on the unobserved consumer mechanism, with a void clause toward option (b) after OPEN-T3; where the alert goes is a named gap; OPEN-A2 not decided. No code, no breaker value, no spec body changed; breakers stay SPECIFIED ONLY; F3 and F4 untouched. |
> | /docs/reports/2026-11-13-open-a1-manager.md | Report | 3 | 2026-11-13 | Manager report for unit 2026-11-13-open-a1 (topology OPEN-A1, bead Praxis_build-fgd; master under D-2026-11-08-D D1, DECISION_LOG 2026-11-13T13:29:04Z): entry D-2026-11-13-B line range and sha256, full diffs of DECISIONS.md and MANIFEST.md against pre-copies, adversary grades quoted, index count. Ungraded at time of row. |
> | /docs/reports/2026-11-13-open-a1-worker1.md | Report | 3 | 2026-11-13 | ADVERSARIAL worker 1 report for unit 2026-11-13-open-a1: checks (a)-(g) on D-2026-11-13-B, including a byte check of every cited quote at its cited line and the append-only shape of both diffs. Ungraded at time of row. |
$ grep -n "^## 2026-11-13 — D-2026-11-13-B" DECISIONS.md | cut -d: -f1; wc -l < DECISIONS.md
2418
    2434
$ awk 'NR==2418,NR==2434' DECISIONS.md | openssl dgst -sha256
SHA2-256(stdin)= 1dc3cc08348ac2b38a9dce83699e5bab01a5f73ace9ef4819a67056541c1cf17
```
Diff note (manager's reading): diff aligns the pre-existing blank line and S13 line (old :2415-2416) with the new ones, so the additions print as two `a` hunks; the `cmp` prefix checks above show old lines 1-2416 and 1-470 are unchanged and the new text starts at :2417 and :471. Entry range: DECISIONS.md :2418-2434 (working tree), 17 lines, with :2417 the blank separator.

## Adversarial findings
worker1 report `docs/reports/2026-11-13-open-a1-worker1.md`, grades quoted: :15 "### (a) Every quoted string is byte-present at its cited line: PASS"; 
:85 "### (b) Files exactly the decision, adds none, does not decide OPEN-A2; every sentence sourced: PASS (with two notes)"; :128 "### (c) Nothing credited to Amear; readings labelled as the master's: PASS"; 
:143 "### (d) CONDITIONAL marked; void clause present: PASS"; :152 "### (e) No D2 item decided; no breaker described as built, implemented or tested: PASS"; :168 "### (f) Both diffs append-only at end of file: PASS"; :220 "### (g) S13 sentence placement: PASS"; :236 "## Overall: PASS".
Its two (b) notes (:106 F3/F4 sentence rests on the row's "Entry only" plus the diff; :117 "already carries FLATTEN" is the row's wording while topology :61 says the FLATTEN path is unbuilt) were graded by it as not breaks. Not cured: one round only.

## S6 cross-block check
The entry's S6 paragraph (working-tree :2430) names Block 3 breakers and topology (:61, :99, :100), OPEN-T2 and OPEN-T3 as open, Block 4 paper (topology :106) unchanged. No spec, topology or ledger file was edited by this unit; only the ends of DECISIONS.md and MANIFEST.md and the two reports.

## Files staged
None by this unit; no git add. End of unit, `git diff --cached --name-only | wc -l` printed `       1` (same as start).

Result: PASS

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
