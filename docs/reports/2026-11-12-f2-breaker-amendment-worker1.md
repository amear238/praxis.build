# Unit F2B worker 1: adversarial check of the F2 breaker amendment

Task: adversarial check of Unit `2026-11-12-f2-breaker-amendment` (F2B), artifacts A1 to A4, HEAD `9905804`.
Mode: ADVERSARIAL.
Criteria: S1, S2, S4, S6, S8, S13 and the unit rules (copied text matches its source byte for byte; superseded lines quoted verbatim; import body unchanged; no placeholder arguments).
Files staged: none. This report is the only file written in the repository. Scratch files are under /tmp/f2b-w1/.

## Scope

- A1: DECISIONS.md lines 2204 to 2278 (D-2026-11-12-A, heading :2205)
- A2: docs/specs/2026-11-05-phase3-build-specification.md, Amendment 1, lines 189 to 244 (line 189 is blank; the heading is at :190)
- A3: docs/reports/2026-11-12-f2-breaker-amendment-manager.md
- A4: MANIFEST.md lines 434 to 437

Not read: DECISION_LOG.md, DECISIONS.md, MANIFEST.md and STATUS.md as whole files. Only the line ranges shown below were read.

## Findings

### 1. MAJOR: A3:396 contains paper-author surnames (de-identification), and A3 was never scanned

In the [E15] command, the `sed` expression that swaps author names for `[author]` contains the surnames themselves. They appear in plain text twice on that line, because the `sed` occurs twice. The brief counts paper authors as names. A3's own de-identification evidence [E12] scans only the A1 region and the spec diff (`{ sed -n 2204,2278p DECISIONS.md; git diff HEAD -- docs/specs/... | grep '^+'; }`). Neither A3 nor A4 is in that scan, so this hit could not have been caught. The surnames are not reproduced in this report. The check list sits in a scratch file outside the repository, and the output below redacts every match.

```text
$ for f in /tmp/f2b-w1/reg/A*; do printf '%s names=%s lines=%s\n' ${f##*/} "$(grep -oiEf /tmp/f2b-w1/names.txt $f | wc -l | tr -d ' ')" "$(grep -niEf /tmp/f2b-w1/names.txt $f | cut -d: -f1 | tr '\n' ',')"; done
A1 names=0 lines=
A2 names=0 lines=
A3 names=8 lines=396,
A4 names=0 lines=
$ python3 -I - (extracts the sed pattern on A3:396 and counts its alternatives; prints counts only)
sed pattern alternatives: 2 surname tokens: 5 token lengths: [9, 2, 7, 7, 9]
$ sed -n 396p docs/reports/2026-11-12-f2-breaker-amendment-manager.md | grep -o "sed -E 's/" | wc -l
       2
```

(The A1 to A4 copies in /tmp/f2b-w1/reg/ were made with `sed -n 2204,2278p DECISIONS.md`, `sed -n 189,244p` of the spec, `cp` of A3, and `sed -n 434,437p MANIFEST.md`.)

Fix: put the swap rule in a sed script outside the repository (for example `sed -E -f /tmp/f2b/author-redact.sed`). Re-run and re-paste [E15] with no surname in the command text. Widen [E12] to cover A3 and A4, and add the name list to it.

### 2. MINOR: A1:2276, the S6 paragraph lists fewer conflicts than A3 grades

A1's S6 paragraph names these topology conflicts: "its :41, :48, :62, :74". It names these Noise-Area ruleset lines: ":8, :84, :99". A3's follow-ups are longer:

- F-1 adds topology :86.
- F-3 adds ruleset :79 and :105.
- F-4 adds walk-forward values :65, which A1 does not mention at all.
- F-8 adds `_Flat1559.cs`:31.
- F-9 adds OPEN-F2-5.

The cause, from A3's process log: the entry was written at steps 3 and 5, and the S6 grading ran later, at step 9. So the entry is a snapshot taken before grading, and it now disagrees with the report it points to.

```text
$ sed -n 2276p DECISIONS.md | grep -oE 'its :41, :48, :62, :74\)|ruleset.md`:8, :84, :99\)'; grep -c 'walk-forward-values' /tmp/f2b-w1/reg/A1
its :41, :48, :62, :74)
ruleset.md`:8, :84, :99)
0
```

Fix: in A1, replace the list with a pointer ("named there as follow-ups F-1 to F-9"), or make it match A3's F-1 to F-9.

### 3. MINOR: A1:2261 and A3:16 state "no account exists"; the source says "no MFFU account" (S2, S8 basis)

A1:2261 reads: "no real money is at stake: no account exists." A3:16 reads: "it is not D2(c) because no account exists". The cited source is narrower, and it is labelled REPORTED BY the Claude.ai channel. It says nothing about any other funded account.

```text
$ sed -n 10p docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md
- Amear has no MFFU account. The email was sent as a pre-purchase question to MFFU support, not from a dashboard.
$ grep -n 'no account exists' DECISIONS.md docs/reports/2026-11-12-f2-breaker-amendment-manager.md | cut -c1-140
docs/reports/2026-11-12-f2-breaker-amendment-manager.md:16:- S8 (read with D1/D2): no D2 item is decided. The adoption of the #4/#5 text is
DECISIONS.md:2211:(1) the proposal's #4/#5 replacement text is adopted as the amended breaker spec, matching Rule F2-1; this is not D2(c) —
DECISIONS.md:2261:Moving #4 from 11:30 to 16:00 and removing #5's system disable change breaker values, but no real money is at stake: no ac
```

(:2211 is the authority row's own words, quoted. That is not a defect in A1.)

Fix: in both places write "no MFFU account exists (REPORTED BY the Claude.ai channel, return handoff :10)". The "not D2(c)" reasoning otherwise rests on evidence on disk: handoff :10 at HEAD, and the Sim-only wall at the consumer's :39. Both pass in G1 below.

### 4. MINOR: A1:2247 has a missing full stop

The text reads `("Amendment 1 — 2026-11-12 — breakers #4 and #5 (Rule F2-1; D-2026-11-12-A)") No pointer line is added`.

```text
$ grep -n 'D-2026-11-12-A)") No pointer' DECISIONS.md | cut -c1-20
2247:The Phase 3 spe
```

Fix: put a full stop after `)")`.

### 5. MINOR: A1:2247's S4 statement does not say this entry is a second version

A1 says "This entry is written to disk before that spec edit (S4)." The final order does hold (see G2 below). But A3 [E20] shows four steps:

1. The first version of the entry was written at 05:32:56Z.
2. A spec write that included a pointer line followed at 05:33:23Z.
3. The spec was then reverted, and the entry region was re-written at 05:35:54Z. Two sentences changed, and the walk-forward pin was added. These changes were driven by what the first spec write had shown.
4. The final spec write came at 05:36:00Z.

The DECISIONS.md region is uncommitted, so git will never show the first version. Only A3 records it. This does not break S4, because the final entry precedes the final spec edit, and "zero pointer lines" is inside the row's "at most one pointer line". But the ledger's own account of its S4 order is incomplete.

```text
$ stat -f '%Sm %N' -t '%Y-%m-%dT%H:%M:%S%z' DECISIONS.md docs/specs/2026-11-05-phase3-build-specification.md
2026-11-12T00:35:54-0500 DECISIONS.md
2026-11-12T00:36:00-0500 docs/specs/2026-11-05-phase3-build-specification.md
```

Fix: add one sentence to A1. Say that it was re-written at 05:35:54Z after a first spec write, now reverted, and that the record is in the manager report [E20].

### 6. MINOR, outside A1 to A4 and routed up, not for this unit to fix: the authority row's time is later than DECISION_LOG.md's last write

Row 854 is the last line of DECISION_LOG.md, and it is stamped 05:29:00Z. The file's mtime is 05:27:25Z, 95 seconds earlier. So the row's stamp is not the time it was written. The likely cause is a stamp set ahead of time; this is INFERRED, not checked, and a preserved mtime could also explain it. The order is not affected, because 05:29:00Z is still before the first entry write at 05:32:56Z. But A1 cites the stamp as if it were the write time.

```text
$ TZ=UTC stat -f '%Sm' -t '%Y-%m-%dT%H:%M:%SZ' DECISION_LOG.md; sed -n 854p DECISION_LOG.md | cut -c1-40; tail -n1 DECISION_LOG.md | cut -c1-40
2026-11-12T05:27:25Z
- [2026-11-12T05:29:00Z] WHO: praxis-mas
- [2026-11-12T05:29:00Z] WHO: praxis-mas
```

Fix: none in this unit. Route to the master.

### 7. MINOR: A3's S6 section does not grade several references to the Phase 3 file (S6 completeness)

A3's [E18] looked only for `Phase 3 :1xx` style references. A grep by file name and by sha256 finds more references at HEAD that A3 does not grade:

- `docs/specs/2026-11-06-walk-forward-values.md`:121
- `scripts/wf/report.py`:11, :46, :575 and :770, all citing :78 to :85
- proposal :34 ("The Phase 3 import ... is not edited by this unit", which is true of that unit only)

All of them would grade as unaffected, because lines 1 to 188 do not move. So no conflict is missed. But A3's claim to cover "every tracked file" is not fully backed. `report.py` opens no spec file and computes no hash of it.

```text
$ git grep -n -E 'phase3-build-specification|Phase 3 :|Phase 3 spec :|cd02d34a|d149bc8e' HEAD -- docs/specs ninjascript scripts config specs | (file:line summary)
docs/specs/2026-11-05-walk-forward-spec.md: 12
docs/specs/2026-11-10-f2-session-flat-proposal.md: 34 67
docs/specs/2026-11-05-phase3-build-specification.md: 19
docs/specs/2026-11-06-walk-forward-values.md: 121
docs/specs/2026-11-10-live-signal-topology.md: 24 54 61 89
scripts/wf/report.py: 11 46 575 770
$ git show HEAD:scripts/wf/report.py | grep -nE 'hashlib|sha256|open\(|phase3|read_text' | cut -c1-140
11:Gates  = docs/specs/2026-11-05-phase3-build-specification.md :80-85
236:        with open(path, "r", encoding="utf-8") as fh:
764:    L.extend(render_open(sel_a, sel_b))
770:    L.append("Gates quoted from docs/specs/2026-11-05-phase3-build-specification.md:80-85.")
902:def render_open(sel_a, sel_b):
992:            with open(args.out, "w", encoding="utf-8", newline="\n") as fh:
```

Fix: add one row to A3's S6 section grading these as unaffected (they cite lines ≤188, which are unchanged).

## Checks that passed

**G1, quote fidelity.** All 8 fenced blocks in A1 and all 4 in A2 match their cited lines exactly, whole line, or as a substring for the two parts of DECISION_LOG :854. The two blockquoted #4 and #5 lines in A2 are whole-line matches for proposal :36 and :38. Every double-quoted passage cited to DECISIONS.md :2068, :2108, :2114 and :2116, DECISION_LOG :854, the consumer's :39 and the handoff's :10 at HEAD is present. "no MFFU account" does not appear in D-2026-11-11-A, as A1 states.

```text
A1 fenced blocks: 8
 block0 vs DECISION_LOG.md:854 substring=True wholeline=False
 block1 vs DECISION_LOG.md:854 substring=True wholeline=False
 block2 vs docs/specs/2026-11-10-f2-session-flat-proposal.md:20 substring=True wholeline=True
 block3 vs docs/specs/2026-11-10-f2-session-flat-proposal.md:30 substring=True wholeline=True
 block4 vs docs/specs/2026-11-10-f2-session-flat-proposal.md:36+38 wholeline-each=True 2 2
 block5 vs docs/specs/2026-11-05-phase3-build-specification.md:100+101 wholeline-each=True 2 2
 block6 vs specs/SPEC_RUBRIC.md:443-447 wholeline-each=True 5 5
 block7 vs specs/SPEC_RUBRIC.md:30-31 wholeline-each=True 2 2
A2 fenced blocks: 4
 block0 vs docs/specs/2026-11-10-f2-session-flat-proposal.md:20 substring=True wholeline=True
 block1 vs docs/specs/2026-11-05-phase3-build-specification.md:100 substring=True wholeline=True
 block2 vs docs/specs/2026-11-05-phase3-build-specification.md:101 substring=True wholeline=True
 block3 vs docs/specs/2026-11-10-f2-session-flat-proposal.md:30 substring=True wholeline=True
A2 bq > 4. Session True
A2 bq > 5. Session True
DECISIONS.md:2108 flat by 16:00 ET governs; a position ope -> True
DECISIONS.md:2108 The amended #4/#5 text does not exist -> True
DECISIONS.md:2108 Whether his approval reaches the element -> True
DECISIONS.md:2116 (f) the proposed replacement text for br -> True
DECISIONS.md:2068 PROPOSED, not adopted -> True
DECISION_LOG.md:854 (4) the rubric F2 state move is a later, -> True
DECISION_LOG.md:854 Amear has no MFFU account -> True
DECISIONS.md:2114 On a full trading day, at 15:00 ET an op -> True
DECISIONS.md:2114 Nothing closes it at 15:00. -> True
ninjascript/PraxisSignalConsumer.cs:39 // HARD SCOPE WALL: refuses to run unles -> True
handoff:10 HEAD -> True
no MFFU account in 2101-2175: []
```

(Script: /tmp/f2b-w1/g1.py, run with `python3 -I`.) Each pointer citation was read with `sed -n Np` and says what A1 says it does:

- DECISIONS.md :1744 and :1745: A6, "F2's state changes when Amear approves the proposed values."
- Rubric :437: "STANDING RULE CHANGE — AUTONOMY". Rubric :442: "No unit waits on Amear except for D2 items."
- Proposal :8 cites `:43–44`.
- Proposal :67: fallback script, Phase 3 :109.
- Proposal :75 to :78: OPEN-F2-1 to OPEN-F2-4.
- Topology :24 and :89: Phase 3 :107. Topology :61: the #4 row. Topology :105: OPEN-T8.
- Phase 3 :11: the STATUS note. Phase 3 :109: the fallback script.
- Ruleset :8, :84 and :99: the 11:30 framing.
- Walk-forward spec :12: "188 lines, sha256 `cd02d34a…`".
- Rubric :80 and :81: "### F1 …" followed by "**State:** PASSED@b4c3291."

**G2, import integrity and S4.**

```text
$ git show HEAD:$F > /tmp/f2b-w1/spec_head.md; head -n 188 $F > /tmp/f2b-w1/spec_188.md; cmp ... && echo CMP_IDENTICAL; shasum -a 256 ...
CMP_IDENTICAL
cd02d34ae635626e674f4316bdfd9ac14d96f819aaf28d39b7d651607be69b83  /tmp/f2b-w1/spec_head.md
cd02d34ae635626e674f4316bdfd9ac14d96f819aaf28d39b7d651607be69b83  /tmp/f2b-w1/spec_188.md
$ head -n 2203 DECISIONS.md | cmp - /tmp/f2b-w1/dec_head.md && echo DEC_1_2203_IDENTICAL
DEC_1_2203_IDENTICAL
    2203 /tmp/f2b-w1/dec_head.md
    2278 DECISIONS.md
```

(The `...` in the first command above is shorthand in this report for the two scratch file paths named in the same line. The full command was `cmp /tmp/f2b-w1/spec_head.md /tmp/f2b-w1/spec_188.md` and `shasum -a 256 /tmp/f2b-w1/spec_head.md /tmp/f2b-w1/spec_188.md`, with `F=docs/specs/2026-11-05-phase3-build-specification.md`.)

The current mtimes (DECISIONS.md 00:35:54, spec 00:36:00, both -0500) match the final stat in A3 [E20]. So the final entry comes before the final spec edit. See finding 5 for the disclosure gap.

**G3, de-identification.** The term list, emails, IPv4 addresses and titles for breaker #5 are all clean in A1 to A4. Names are clean except A3:396 (finding 1).

```text
A1 deid=0 email=0 ipv4=0
A2 deid=0 email=0 ipv4=0
A3 deid=0 email=0 ipv4=0
A4 deid=0 email=0 ipv4=0
-- breaker 5 titles
   4  5. Session window (operator lockout) —
   2 5. Afternoon session window —
```

The only #5 titles found are the importer's "Afternoon session window" and the proposal's "Session window (operator lockout)".

**G4, S2 and S8.** The only sentences that say "enforced", "implemented" or "tested" in A1 and A2 are these:

- the copied proposal :38 ("enforced by breaker #4")
- the explicit SPECIFIED ONLY statements (A1:2263, and A2's Level paragraph at :196)
- "how #5's operator lockout is enforced" (OPEN-T8, left open)

No D2 item is decided. Whether something is D2(c) is treated as the master's reading under D1, and its premise rests on the handoff's :10 at HEAD and the consumer's :39. The wording caveat is finding 3.

```text
## A1
34:y this breaker; the system's no-entry period 16:00–18:00 ET is enforced by breaker #4
60:e breakers, #4 and #5 included, remain SPECIFIED ONLY: zero implemented, zero tested, zero tested under failure (Phase 3 import sta
71:to OPEN-F2-4 (proposal :75–78) or how #5's operator lockout is enforced (topology doc OPEN-T8, :105)
## A2
8:ine breakers, #4 and #5 included, are SPECIFIED ONLY — zero implemented, zero tested, zero tested under failure
36:y this breaker; the system's no-entry period 16:00–18:00 ET is enforced by breaker #4
```

**G5, S6 grep at HEAD.** My own grep found 250 matching lines, and every per-file count equals A3's: Phase 3 6, topology 11, proposal 35, ruleset 10, walk-forward values 18, walk-forward spec 4, data-acquisition spec 3, ninjascript 79 across 4 files, scripts 83 (3+3+3+12+5+4+3+9+3+7+13+2+3+7+6), config 1. Rubric O4 is named as a bearing in A3's "Ledgers and rubric" section, citing :111–116 [E14]. Spot checks of the gradings agree with A3: topology :44, :86, :88 and :112, values :65, ruleset :79 and :105, and proposal :12, :40 and :79.

```text
$ git grep -n -E "$P" HEAD -- docs/specs ninjascript scripts config | wc -l
     250
```

**G6, S1 and A4.** A3 has 25 pasted `$ ` command lines, and none has a `<...>`, `...` or `…` placeholder:

```text
$ grep -nE '^\$ ' $A | grep -nE '<[A-Za-z_ -]+>|\.\.\.|…' | cut -c1-200
$ grep -cE '^\$ ' $A
25
```

A4: each of the four rows has 7 `|`-separated fields, the same as rows 425 to 433 (`9 7`). Row 435's facts are true: ":189-244", "row 226 for this path" (MANIFEST :226 is that path), and lines 1 to 188 identical. Row 434's facts are true: "2204-2278 (heading :2205)" and "lines 1-2203 unchanged".

**S13.** In A3, the sentence occurs exactly once, as the last line (count=1, last=1, and the file ends with a newline). A1 ends with it (count=1, line 2278). A2 does not carry it.

```text
-- S13 A3 count=1 last=1 A1count=1 A1last=1 A2count=0
```

Result: FAIL (one MAJOR finding).

Verdict: 1 MAJOR, 6 MINOR

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
