# 2026-11-13 open-a1 worker 1 (ADVERSARIAL)

## Task

Unit 2026-11-13-open-a1, bead `Praxis_build-fgd`. Mode: ADVERSARIAL, read-only, one round. Artifact: entry D-2026-11-13-B at working-tree DECISIONS.md lines 2418-2434, and the rows appended at the end of working-tree MANIFEST.md (lines 471-473). Pre-copies `/tmp/oa1-pre-DECISIONS.md` and `/tmp/oa1-pre-MANIFEST.md` were read only. Rubric lines: S4, S6, S13 in `specs/SPEC_RUBRIC.md`. Authorising row: DECISION_LOG.md row stamped 2026-11-13T13:29:04Z (working-tree DECISION_LOG.md line 917).

All line numbers in this report are working-tree numbers at the time of the check. Every grep below uses `/usr/bin/grep` under bash or zsh, not the zsh `grep` alias. In the pasted output, the S13 sentence is shown as `[S13-LINE]` so it appears only once in this report, as rule (g) requires. That substitution is done by the awk filter shown in the command, not by hand.

Entry line count: 17 (lines 2418-2434), under 20.

MANIFEST line-number labels: none of the three new rows cites a line number. The only hits for `:<digits>` are parts of the timestamp `13:29:04Z` (output under (f)).

## Checks

### (a) Every quoted string is byte-present at its cited line: PASS

There are 13 double-quoted spans in the entry. Naive pairing splits the :61 quote into spans 8 and 9 because of its inner quotes:

```
$ awk 'NR>=2418 && NR<=2434' DECISIONS.md | /usr/bin/grep -o '"[^"]*"' | nl
     1	"cancel working entry orders"
     2	"confirm flat before 4:10 PM ET (alert if not)"
     3	"alert"
     4	"(a) Both are part of the FLATTEN command the consumer executes at the flat time (the consumer cancels its own working entries and reports flat or not flat)."
     5	"(b) The confirmation is a separate n8n-side check on account state, which needs the account-state feed of OPEN-T3."
     6	"EXIT / FLATTEN types, unbuilt"
     7	"Where account state (P&L, equity, fills, open position) comes from, and how fresh it must be."
     8	"Its "
     9	" action: the emitter's own time exit posted as a FLATTEN signal, plus the FLATTEN command from n8n at the gate time."
    10	"D8(8): the final step of this build is a Block 4 paper pass on MFFU sim; Block 5 live is a separate sign-off."
    11	"cancel working entry orders, send market orders closing all system positions, confirm flat before 4:10 PM ET (alert if not)"
    12	"SPECIFIED ONLY — zero implemented, zero tested, zero tested under failure."
    13	"close positions"
```

**Loop 1.** Each quote at its cited line in its cited file, using `awk 'NR==n' file | /usr/bin/grep -qF`. T is `docs/specs/2026-11-10-live-signal-topology.md` and S is `docs/specs/2026-11-05-phase3-build-specification.md`:

```
HIT  2026-11-10-live-signal-topology.md:198  (a) Both are part of the FLATTEN command the consumer executes at the flat time (the consumer cancels its own working entries and reports flat or not flat).
HIT  2026-11-10-live-signal-topology.md:198  (b) The confirmation is a separate n8n-side check on account state, which needs the account-state feed of OPEN-T3.
HIT  2026-11-10-live-signal-topology.md:99  EXIT / FLATTEN types, unbuilt
HIT  2026-11-10-live-signal-topology.md:100  Where account state (P&L, equity, fills, open position) comes from, and how fresh it must be.
HIT  2026-11-10-live-signal-topology.md:61  Its "close positions" action: the emitter's own time exit posted as a FLATTEN signal, plus the FLATTEN command from n8n at the gate time.
HIT  2026-11-10-live-signal-topology.md:106  D8(8): the final step of this build is a Block 4 paper pass on MFFU sim; Block 5 live is a separate sign-off.
HIT  2026-11-05-phase3-build-specification.md:212  cancel working entry orders, send market orders closing all system positions, confirm flat before 4:10 PM ET (alert if not)
HIT  2026-11-05-phase3-build-specification.md:212  cancel working entry orders
HIT  2026-11-05-phase3-build-specification.md:212  confirm flat before 4:10 PM ET (alert if not)
HIT  2026-11-05-phase3-build-specification.md:196  SPECIFIED ONLY — zero implemented, zero tested, zero tested under failure.
HIT  2026-11-10-live-signal-topology.md:61  close positions
HIT  2026-11-10-live-signal-topology.md:198  OPEN-A1
```

Spans 3 ("alert", in the named-gap sentence, read against spec :212) and 13 ("close positions" with its quotes, S6 paragraph, cited to topology :61):

```
$ awk 'NR==212' S | /usr/bin/grep -cF 'alert'
1
$ awk 'NR==61' T | /usr/bin/grep -cF '"close positions"'
1
```

**Loop 2.** This closes the retyping gap: the same strings, with their quote marks and line labels, are present in the entry text.

```
IN_ENTRY  DECISIONS.md:2425  "(a) Both are part of the FLATTEN command the consumer executes at the flat time (the consumer cancels its own working entries and reports flat or not flat)."
IN_ENTRY  DECISIONS.md:2425  "(b) The confirmation is a separate n8n-side check on account state, which needs the account-state feed of OPEN-T3."
IN_ENTRY  DECISIONS.md:2425  :99 "EXIT / FLATTEN types, unbuilt"
IN_ENTRY  DECISIONS.md:2425  :100 "Where account state (P&L, equity, fills, open position) comes from, and how fresh it must be."
IN_ENTRY  DECISIONS.md:2425  :61 "Its "close positions" action: the emitter's own time exit posted as a FLATTEN signal, plus the FLATTEN command from n8n at the gate time."
IN_ENTRY  DECISIONS.md:2425  :106 "D8(8): the final step of this build is a Block 4 paper pass on MFFU sim; Block 5 live is a separate sign-off."
IN_ENTRY  DECISIONS.md:2426  :212 "cancel working entry orders, send market orders closing all system positions, confirm flat before 4:10 PM ET (alert if not)"
IN_ENTRY  DECISIONS.md:2426  :196 "SPECIFIED ONLY — zero implemented, zero tested, zero tested under failure."
IN_ENTRY  DECISIONS.md:2422  "cancel working entry orders" and "confirm flat before 4:10 PM ET (alert if not)" (spec :212)
```

Non-ASCII bytes in the entry: only the em-dash (`e28094`, twice: the heading and the :196 quote) and the arrow (`e28692`, once). There is no trailing whitespace.

```
2 x e28094
1 x e28692
== trailing whitespace lines in entry
(end)
```

### (b) Files exactly the decision, adds none, does not decide OPEN-A2; every sentence sourced: PASS (with two notes)

Authorising row (DECISION_LOG.md:917, excerpt of the decided part, captured by `grep -n '2026-11-13T13:29:04Z' DECISION_LOG.md`):

```
**Decided by master under D-2026-11-08-D D1:** option (a), because (b) depends on OPEN-T3, which is unresolved, and (a) keeps both actions on the order path that already carries FLATTEN. CONDITIONAL: rests on the unobserved mechanism that the consumer can see and cancel its own working entry orders and read its own position; FLATTEN as an instruction type is unbuilt (OPEN-T2, topology :99). Void clause: if either is observed false, re-decide toward (b) after OPEN-T3. Named gap: where the "alert" goes is not decided here. Not a D2 item (no money, no live path switched on, no breaker value, no credential). Entry only: no spec body, no code. [...] OPEN-A2 is not decided in this unit.
```

The entry's Decision paragraph (diff under (f), line 2422) restates each clause in order: option (a); the master's two-part reason; CONDITIONAL on the same mechanism; FLATTEN unbuilt (OPEN-T2, topology :99); the void clause toward (b) after OPEN-T3; the named gap on "alert"; not a D2 item, with the same four parentheticals; and "OPEN-A2 is not decided here." The only addition is the clause "the consumer cancels its own working entries and reports flat or not flat", which is topology :198 option (a)'s own parenthetical (loop 1, first HIT).

OPEN-A2 is not decided. It is defined in the Noise-Area ruleset, not in the topology document. It concerns the 11:30 strategy stop, which is unrelated to #4 placement, and the entry's only mention of it is the disclaimer:

```
$ /usr/bin/grep -rn 'OPEN-A2' docs/specs DECISIONS.md ...   (first hit, cut)
docs/specs/2026-07-16-b2-noise-area-ruleset.md:170:| OPEN-A2 | Whether a strategy-level stop at 11:30 (a strategy rule, not a breaker) is still available to a later Noise-Area arm ...
$ ... entry | /usr/bin/grep -o '[^.]*OPEN-A2[^.]*\.'
 OPEN-A2 is not decided here.
$ /usr/bin/grep -n 'OPEN-A' docs/specs/2026-11-10-live-signal-topology.md   (OPEN-A rows)
198:| OPEN-A1 | Where amended #4's "cancel working entry orders" and "confirm flat before 4:10 PM ET (alert if not)" sit on the live path. ...
```

Note 1, a scope sentence with no direct quote: Limits says "This entry does not touch F3 or F4." This sentence rests on neither a quoted line nor a verbatim phrase of the row. It rests on the row's "Entry only: no spec body, no code." together with the (f) diff, which shows that only DECISIONS.md and MANIFEST.md changed and that the entry changes nothing else. F3 and F4 appear in the entry only in that sentence:

```
$ ... entry | /usr/bin/grep -oE '[^.]*\bF[34]\b[^.]*\.'
 This entry does not touch F3 or F4.
$ /usr/bin/grep '2026-11-13T13:29:04Z' DECISION_LOG.md | /usr/bin/grep -oF 'Entry only: no spec body, no code.'
Entry only: no spec body, no code.
```

I grade this as sourced through the row's "Entry only" plus the diff, not as a break. The same applies to "Nothing else is edited." in the S6 paragraph.

Note 2, wording carried from the row: "the order path that already carries FLATTEN (topology :61)". Topology :61 also says the FLATTEN path is unbuilt:

```
$ awk 'NR==61' T | /usr/bin/grep -oF 'FLATTEN path (unbuilt)'
FLATTEN path (unbuilt)
$ /usr/bin/grep '2026-11-13T13:29:04Z' DECISION_LOG.md | /usr/bin/grep -oF 'the order path that already carries FLATTEN'
the order path that already carries FLATTEN
```

"Already carries" is true of the specified design: :61 routes #4's "close positions" action through FLATTEN. The same paragraph of the entry says "FLATTEN as an instruction type is unbuilt", and the S4 paragraph says "FLATTEN is unbuilt (topology :99)". So the entry does not claim that FLATTEN exists, and the phrase is the master's verbatim reason from the row. This is not a break.

### (c) Nothing credited to Amear; readings labelled as the master's: PASS

```
== Amear in entry
**Status:** Decided by master under D-2026-11-08-D D1 (DECISION_LOG 2026-11-13T13:29:04Z), changeable by Amear.
 Not Amear's ruling.
== master in entry
## 2026-11-13 — D-2026-11-13-B: Breaker #4 cancel and confirm-flat placement (topology OPEN-A1; master under D-2026-11-08-D D1)
**Status:** Decided by master under D-2026-11-08-D D1 (DECISION_LOG 2026-11-13T13:29:04Z), changeable by Amear
 The master's reason: option (b) depends on OPEN-T3 (topology :100), which is unresolved, and (a) keeps both actions on the order path that already carries FLATTEN (topology :61)
 Chain: D-2026-11-08-D D1 → DECISION_LOG 2026-11-13T13:29:04Z (WHO: praxis-master)
```

The entry mentions Amear only twice: once to say the decision can be changed by him, and once to say it is not his ruling. No approval, confirmation or sign-off is attributed to him. The heading, the Status line, the reason and the chain all label the decision as the master's.

### (d) CONDITIONAL marked; void clause present: PASS

```
== CONDITIONAL / void
CONDITIONAL rests on a mechanism nobody has observed and carries a void clause.
CONDITIONAL: this rests on the unobserved mechanism that the consumer can see and cancel its own working entry orders and read its own position; FLATTEN as an instruction type is unbuilt (OPEN-T2, topology :99).
Void clause: if either is observed false, the placement is re-decided toward (b) after OPEN-T3.
```

### (e) No D2 item decided; no breaker described as built, implemented or tested: PASS

```
== built/implemented/tested/working in entry
...the order path that already carries FLATTEN (topology :61). CONDITIONAL: th
 FLATTEN as an instruction type is unbuilt (OPEN-T2, topology :99). Void clause: i
 is not decided here. Not a D2 item (no money, no live path switched on, no breaker value, no crede
...:196 "SPECIFIED ONLY — zero implemented, zero tested, zero tested under failure."
ne breakers stay SPECIFIED ONLY (spec :196): zero implemented, zero tested. This entry does not tou
6-11-13, before the work it governs: FLATTEN is unbuilt (topology :99) and no breaker is implem
```

(This is an excerpt of the hits from `grep -oiE '.{0,50}(built|implement|tested|working|carries|live path).{0,40}'`. The other hits were "working entry orders" or "working entries", the name of the orders being cancelled, not claims about status.)

Every built, implemented or tested hit is a negation. The entry sets no money, no live switch-on, no breaker value and no credential, so it decides no D2 item. Topology :106 (OPEN-T9, "Waits for Amear (D2(b))") is cited only to say that no Block 4 text changes.

### (f) Both diffs append-only at end of file: PASS

```
== DECISIONS diff (S13 sentence shown as [S13-LINE])
2414a2415,2426
> 
> [S13-LINE]
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
diff exit=1
== MANIFEST diff
470a471,473
> | /DECISIONS.md | Log | 3 | 2026-11-13 | AMENDMENT ROW (append-only registry). Unit 2026-11-13-open-a1 (topology OPEN-A1, bead Praxis_build-fgd; master under D-2026-11-08-D D1, DECISION_LOG 2026-11-13T13:29:04Z): appends entry D-2026-11-13-B, "Breaker #4 cancel and confirm-flat placement", filing option (a): amended breaker #4's cancel of working entry orders and its confirm-flat check are both part of the FLATTEN command the consumer executes at the flat time. CONDITIONAL on the unobserved consumer mechanism, with a void clause toward option (b) after OPEN-T3; where the alert goes is a named gap; OPEN-A2 not decided. No code, no breaker value, no spec body changed; breakers stay SPECIFIED ONLY; F3 and F4 untouched. |
> | /docs/reports/2026-11-13-open-a1-manager.md | Report | 3 | 2026-11-13 | Manager report for unit 2026-11-13-open-a1 (topology OPEN-A1, bead Praxis_build-fgd; master under D-2026-11-08-D D1, DECISION_LOG 2026-11-13T13:29:04Z): entry D-2026-11-13-B line range and sha256, full diffs of DECISIONS.md and MANIFEST.md against pre-copies, adversary grades quoted, index count. Ungraded at time of row. |
> | /docs/reports/2026-11-13-open-a1-worker1.md | Report | 3 | 2026-11-13 | ADVERSARIAL worker 1 report for unit 2026-11-13-open-a1: checks (a)-(g) on D-2026-11-13-B, including a byte check of every cited quote at its cited line and the append-only shape of both diffs. Ungraded at time of row. |
diff exit=1
== prefix byte compare
DECISIONS first 2416 lines == pre-copy (2416 lines)
MANIFEST first 470 lines == pre-copy (470 lines)
    2416 /tmp/oa1-pre-DECISIONS.md
    2434 DECISIONS.md
     470 /tmp/oa1-pre-MANIFEST.md
     473 MANIFEST.md
```

The DECISIONS hunk headers (`2414a…`, `2415a…`) look like mid-file insertions. They are an artifact of diff's alignment: the pre-copy's last two lines (a blank line, then the D-2026-11-13-A S13 line) are identical to the new file's lines 2427 and 2434, and diff matches them there. The byte compare settles the question. The first 2416 lines of the working-tree file are byte-identical to the whole 2416-line pre-copy, and both files end in `0a`. So all 18 new lines (2417-2434) follow the old end of file, and no existing line was changed, removed or reordered. The same holds for MANIFEST: the first 470 lines equal the 470-line pre-copy, and there are 3 new rows.

MANIFEST line-number check on the new rows:

```
$ awk 'NR>=471' MANIFEST.md | /usr/bin/grep -oE '.{12}:[0-9]+.{6}'
026-11-13T13:29:04Z):
026-11-13T13:29:04Z):
```

These are timestamp hits only. No new row cites line numbers.

### (g) S13 sentence placement: PASS

```
== S13 counts
entry 2418-2434 substring count: 1
entry standalone line no: 2434
entry last line no: 2434
manager substring count: 1
manager standalone line no: 75
manager total lines: 75
```

- Entry: once, as the whole of line 2434, which is the entry's last line and the file's last line. The other S13 line, at 2416, belongs to D-2026-11-13-A and lies outside the entry.
- Manager report: it exists at the time of the check. The sentence appears once, as standalone line 75 of 75. The report may still change after this check.
- This report: the sentence appears once, as the standalone last line, and is shown as `[S13-LINE]` everywhere else.

## Overall: PASS

No break found. Methods tried:
- byte-checking all 13 quote spans at their cited lines in both directions
- searching the topology for OPEN-A2 (it is not there; it lives in ruleset :170 and is not decided)
- tracing each clause to DECISION_LOG:917
- grepping for credit to Amear and for claims that something is built, implemented or tested
- checking the append-only shape by a prefix byte compare, which defeats diff's misleading hunk headers
- scanning the entry's bytes for non-ASCII characters and trailing whitespace
- checking MANIFEST rows for line numbers that carry no label

Two notes are recorded under (b), neither graded as a break: the scope sentence on F3 and F4 rests on the row's "Entry only" plus the diff, and the phrase "already carries FLATTEN" is true of the specified design while FLATTEN itself is unbuilt.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
