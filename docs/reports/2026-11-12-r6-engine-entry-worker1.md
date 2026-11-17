# 2026-11-12 — r6-engine-entry — worker 1 (adversarial)

## Task

Unit `2026-11-12-r6-engine-entry`. Mode: ADVERSARIAL. Artifact: entry D-2026-11-12-B, appended at `DECISIONS.md`:2279–2370 (heading :2280), uncommitted, HEAD `c29d08b`. Job: find where the entry breaks against its cited sources. Nothing was edited except this report. No index or HEAD change was made.

Scratch copies used below (read-only extracts, under /tmp/r6w1): `design.md` = `git -C /Users/admin/Praxis.build-r6 show bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md`; `entry.txt` = `sed -n '2280,2370p' DECISIONS.md`; one-line extracts `dl765`, `dl861`, `v125`, `v126`, `f3` (rubric :19–31), `d89`, `d95`, `d111`, `p212`.

## Checks run (pasted output)

### Check 1 — fenced quotation blocks are byte-identical to the cited lines

```text
$ D=/tmp/r6w1 && mkdir -p $D && git -C /Users/admin/Praxis.build-r6 show bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md > $D/design.md && wc -l $D/design.md && for pair in 2294:102 2300:84 2308:46 2314:85 2320:52 2355:111; do e=${pair%%:*}; s=${pair##*:}; if [ "$(sed -n "${e}p" DECISIONS.md)" = "$(sed -n "${s}p" $D/design.md)" ]; then echo "entry :$e vs design :$s IDENTICAL"; else echo "entry :$e vs design :$s DIFFER"; fi; done; for pair in 2334:212 2336:224; do e=${pair%%:*}; s=${pair##*:}; if [ "$(sed -n "${e}p" DECISIONS.md)" = "$(sed -n "${s}p" docs/specs/2026-11-05-phase3-build-specification.md)" ]; then echo "entry :$e vs phase3 :$s IDENTICAL"; else echo "entry :$e vs phase3 :$s DIFFER"; fi; done; sed -n '2335p' DECISIONS.md | od -c | head -2
     123 /tmp/r6w1/design.md
entry :2294 vs design :102 IDENTICAL
entry :2300 vs design :84 IDENTICAL
entry :2308 vs design :46 IDENTICAL
entry :2314 vs design :85 IDENTICAL
entry :2320 vs design :52 IDENTICAL
entry :2355 vs design :111 IDENTICAL
entry :2334 vs phase3 :212 IDENTICAL
entry :2336 vs phase3 :224 IDENTICAL
0000000   \n
0000001
```

All 8 quoted lines PASS. The two-line block at :2333–2337 has an empty separator line (:2335, a lone newline); the entry says the block is copied "from that spec's :212 and :224", which it is. The S4 block (:2286–2289) is command output, re-run under check 6.

### Check 2 — in-text quotations are substrings of the cited line

```text
$ q() { printf '%s | %s -> ' "$1" "$2"; grep -F -c -- "$2" "$1"; }   (applied to each)
/tmp/r6w1/dl765 | R6 step 2 (the backtest unit) sources a FREE release list (nothing bought, D2(a)); until it does, 1F and 2S stay provisional. -> 1
/tmp/r6w1/dl765 | no bar is written, lowered or waived. -> 1
/tmp/r6w1/v125 | ≥ 250 aggregate OOS trades -> 1
/tmp/r6w1/v126 | ≥ 60% of walk-forward windows profitable -> 1
/tmp/r6w1/dl765 | so an R6 result is reported as research, not as a gate pass. -> 1
/tmp/r6w1/f3 | The fill resolution the Strategy Analyzer will actually run at -> 1
/tmp/r6w1/f3 | `4uu`. Everything downstream of `4uu`. -> 1
/tmp/r6w1/dl861 | the R6 Python simulator is a separate arm pulled forward by Amear's D7 and is not downstream of `4uu` -> 1
/tmp/r6w1/d89 | cannot qualify for any funded-account tier row until OPEN-1 is answered in writing by MFFU -> 1
/tmp/r6w1/d95 | zero positions at 16:10 ET or across 16:10-18:00 -> 1
/tmp/r6w1/d111 | next session -> 1
/tmp/r6w1/p212 | until the next session opens at 18:00 ET -> 1
```

All 12 in-text quotations PASS. The values-spec lines are the same at HEAD and in the working copy:

```text
$ git show HEAD:docs/specs/2026-11-06-walk-forward-values.md | sed -n '125,126p' | nl -ba -v125
   125	  4. ≥ 250 aggregate OOS trades
   126	  5. ≥ 60% of walk-forward windows profitable
```

Paraphrase checks (not quotations, but they restate cited rows):

```text
DL:861 "states its fill resolution and slippage in writing before it runs" -> 1
entry "in writing before its results" -> 1
rubric F3 "stated in writing before" (:21-22 joined) -> 1
DL:765 "graded against the existing walk-forward gates as written" -> 1
entry "set beside the existing walk-forward gates as written" -> 1
entry "no gate is graded" -> 1
```

### Check 3 — line citations

Rubric D1/D2 positions at the entry's own stated HEAD `c29d08b`, compared with `e3323a8` (before `c29d08b` removed the F2 block above them):

```text
$ git diff --numstat HEAD -- specs/SPEC_RUBRIC.md
rubric diff lines above (empty = unchanged)
$ echo "== e3323a8 :437-447"; git show e3323a8:specs/SPEC_RUBRIC.md | sed -n '437,447p' | nl -ba -v437; echo "== HEAD :437-447"; git show HEAD:specs/SPEC_RUBRIC.md | sed -n '437,447p' | nl -ba -v437; echo "== HEAD F4 block"; git show HEAD:specs/SPEC_RUBRIC.md | sed -n '33,43p' | nl -ba -v33
== e3323a8 :437-447
   437	STANDING RULE CHANGE — AUTONOMY
   438	D1  Default-decide. When a unit or the master reaches a question that
   439	    would otherwise go to Amear, it takes the recommended option, logs
   440	    it as "decided by master under D-2026-11-08-D D1", and continues.
   441	    Amear may reverse any such decision later; the reversal is filed
   442	    like any ruling. No unit waits on Amear except for D2 items.
   443	D2  Only four things stop and wait for Amear's word: (a) spending
   444	    money; (b) switching live trading on, or any order path to a
   445	    funded account; (c) changing circuit-breaker values while real
   446	    money is at stake; (d) installing keys, credentials or agent
   447	    permissions. Everything else is D1.
== HEAD :437-447
   437	:1906–1927 (the D-2026-11-08-D verbatim block).
   438
   439	```text
   440	STANDING RULE CHANGE — AUTONOMY
   441	D1  Default-decide. When a unit or the master reaches a question that
   442	    would otherwise go to Amear, it takes the recommended option, logs
   443	    it as "decided by master under D-2026-11-08-D D1", and continues.
   444	    Amear may reverse any such decision later; the reversal is filed
   445	    like any ruling. No unit waits on Amear except for D2 items.
   446	D2  Only four things stop and wait for Amear's word: (a) spending
   447	    money; (b) switching live trading on, or any order path to a
== HEAD F4 block
    33	### F4 — MFFU automation compliance
    34	**Criterion.** Written confirmation from MFFU that this specific automation
    35	pattern is permitted on a funded account.
    36	**Why frozen.** Flagged as blocking in the Round 1+2 compilation, still open in
    37	the Phase 2 closure document, still open in the Phase 3 output summary, absent
    38	from the session-28 build report. The plan documents also contradict each
    39	other: the Round 3 handoff asserts automation is explicitly permitted; Phase 2
    40	closure states it has not been confirmed by direct inquiry.
    41	**Owner.** Amear. Not a build task — an email.
    42	**Blocks.** Block 4. Block 5.
    43
```

Where the stale numbers came from:

```text
$ grep -n -o 'SPEC_RUBRIC.md`:4[0-9][0-9][–-]4[0-9][0-9][^;,)]\{0,40\}' DECISIONS.md | tail -15
2085:SPEC_RUBRIC.md`:446–447
2156:SPEC_RUBRIC.md`:446–447
2208:SPEC_RUBRIC.md`:437–442. Every quotation in this entry is copie
2251:SPEC_RUBRIC.md`:443–447:
2283:SPEC_RUBRIC.md`:437–442. R6 step 1 design: `bf6fcc7:docs/specs/
2323:SPEC_RUBRIC.md`:443–444
```

D-2026-11-12-A (:2208, :2251) was written against `e3323a8`. The new entry reuses those numbers, but `c29d08b` has since moved the D block down 3 lines.

Rubric F3 and the R6/D7/D-2026-11-12-A ranges in DECISIONS.md:

```text
$ cat -n specs/SPEC_RUBRIC.md | sed -n '17,45p'   (F3 excerpt)
    19	### F3 — Backtest fill resolution vs. acquired data granularity
    20	**Criterion.** The fill resolution the Strategy Analyzer will actually run at,
    ...
    31	**Blocks.** `4uu`. Everything downstream of `4uu`.
$ cat -n DECISIONS.md | sed -n '1566,1582p;1936,1946p;2203,2206p'   (excerpt)
  1572	R6  Research and backtest, on the existing 1-minute data only,
  1573	    nothing bought (R-1104-3 stands):
  ...
  1579	    whether an evening entry counts as the same trading day.
  1940	D7  If D6 fails at every tier at 1 MNQ: do not design breaker values
  ...
  1944	    tests for the record, but a GO on MFFU is not expected from it.
  2205	## 2026-11-12 — D-2026-11-12-A: breakers #4 and #5 amended to match Rule F2-1 (rubric F2; master under D-2026-11-08-D D1)
```

DECISION_LOG line counts and rows:

```text
$ wc -l DECISION_LOG.md && git show HEAD:DECISION_LOG.md | wc -l
     861 DECISION_LOG.md
     859
```

Row :765 begins `- [2026-11-09T17:32:00Z] WHO: praxis-master | WHAT: **D11 for this run ...` and holds (1) H01 and (3) H03. Row :861 begins `- [2026-11-12T09:03:23Z] WHO: praxis-master | WHAT: **Session start ...` and holds items (c) and (d) (pasted in full in the process output; both quoted substrings matched in check 2).

Phase 3 spec (excerpt of `cat -n ... | sed -n '95,112p;186,230p'`):

```text
   100	4. Session time gate — clock hits 11:30 ET → close positions, disable until next session
   101	5. Afternoon session window — clock enters 3:00–6:00 PM ET → disable everything
   109	The deterministic fallback script. A standalone Python script ...
   190	## Amendment 1 — 2026-11-12 — breakers #4 and #5 (Rule F2-1; D-2026-11-12-A)
   212	> 4. Session flat gate — clock reaches 16:00:00 ET, or the exchange's early close on an early-close day if earlier → ...
   224	> 5. Session window (operator lockout) — clock is in 3:00–6:00 PM ET → lock out manual order entry ...
```

Citation table (design line content from the `cat -n` of design.md, 123 lines):

| Citation in entry | Points at | Result |
|---|---|---|
| DECISIONS.md:1572–1579 (R6) | R6 text :1572–1579 | PASS |
| DECISIONS.md:1940–1944 (D7) | D7 text :1940–1944 | PASS |
| `specs/SPEC_RUBRIC.md`:437–442 (D1) | at HEAD: filer-note tail, blank, fence, header, first 2 of D1's 5 lines; D1 is :441–445 | FAIL |
| DECISION_LOG.md:765 (row 17:32:00Z, H01/H03) | yes | PASS |
| DECISION_LOG.md:861 (row 09:03:23Z, items (c),(d)); 859 lines at HEAD | yes; 859 confirmed | PASS |
| design :102 engine | yes | PASS |
| design §4, :84 data | yes | PASS |
| design :36–38 variants, :42–46 rules, :39 exclusions, :46 | yes | PASS |
| design :62 (2A), :64–68 (2S) | yes | PASS |
| design :85 costs, :52 sensitivity | yes | PASS |
| design §3 (:71–80), :119 R-1104-3, OPEN-4 :113, constraint (ii) :23 | yes | PASS |
| `specs/SPEC_RUBRIC.md`:443–444 for D2(a) | at HEAD: D1 lines "it as decided by master ..." / "Amear may reverse ..."; D2(a) is :446–447 | FAIL |
| values spec :125, :126 | gates 4 and 5 | PASS |
| design §5 (:87–98) | §5 heading :87, measures :90–98 | PASS |
| `specs/SPEC_RUBRIC.md`:19–31 (F3) | F3 block | PASS |
| design OPEN-1 :110, OPEN-5 :114, :89 | yes | PASS |
| `specs/SPEC_RUBRIC.md`:33–41 (F4) | F4 block is :33–42; :42 "Blocks." left out | MINOR FAIL |
| DECISIONS.md from :2205; spec heading :190, :212, :224 | yes | PASS |
| table: :42–43, :52; :42–44, :52; :62; :65–67 | yes | PASS |
| :45, :68 as "the design skips any exit after an early close" | :45 is Strategy 1's skip rule, :68 is the 2S skip; neither covers 2A | FAIL (see Finding 1) |
| constraint (iii) :24, :95 flat-by, :116 O4, :62 benchmark | yes | PASS |
| design :111 OPEN-2; Phase 3 spec :100–101 | yes | PASS |
| design :117 A14, :116 O4 | yes | PASS |

### Check 4 — numbers

```text
$ sed -n '2280,2370p' DECISIONS.md | grep -o -E '[0-9][0-9:.,–-]*[0-9]|[0-9]' | sort | uniq -c | sort -k2 | awk '{printf "%s(x%s) ", $2, $1} END{print ""}'
0(x2) 0.50(x1) 01(x2) 03(x2) 08(x2) 08:25(x2) 08:30(x1) 09-27(x1) 09:03:23(x1) 1(x40) 1,857,362(x1) 1.2.0(x1) 1.90(x1) 100-101(x1) 100–101(x1) 102(x4) 110(x1) 1104-3(x1) 111(x1) 112700(x1) 113(x1) 114(x1) 116(x2) 117(x1) 119(x1) 11:30(x3) 125(x1) 126(x1) 13(x1) 13:55(x2) 14(x1) 14:00(x1) 1572–1579(x1) 15:00-16:05(x1) 15:00–16:05(x1) 15:00–18:00(x1) 16:00(x5) 16:00:00(x4) 16:00–18:00(x3) 16:05(x5) 16:10(x2) 16:10-18:00(x1) 17:00(x1) 17:32:00(x1) 180100(x1) 18:00(x5) 18:01(x1) 18:05(x10) 190(x1) 1940–1944(x1) 19–31(x1) 2(x49) 2.00(x1) 20.00(x1) 2021-09-09(x1) 20210307(x1) 2024-06-11(x1) 2025-12-14(x1) 2026-01-01(x1) 2026-11-05(x1) 2026-11-06(x1) 2026-11-08(x4) 2026-11-09(x2) 2026-11-12(x7) 20260720(x1) 20:00(x3) 212(x1) 2205(x1) 224(x1) 23(x1) 24(x1) 24.68(x1) 250(x1) 256(x1) 257(x1) 29(x3) 3(x13) 3-3(x1) 3.90(x1) 307(x1) 33–41(x1) 36–38(x1) 39(x1) 3:00–6:00(x2) 4(x34) 4.68(x1) 42–43(x1) 42–44(x1) 42–46(x1) 437–442(x1) 443–444(x1) 45(x1) 454(x1) 46(x1) 4:10(x1) 5(x18) 52(x3) 6(x28) 60(x1) 62(x3) 64–68(x1) 65–67(x1) 68(x1) 7(x4) 7.80(x1) 71–80(x1) 765(x3) 8(x11) 84(x1) 85(x1) 859(x1) 86(x1) 861(x2) 87–98(x1) 89(x1) 9(x1) 95(x1)
$ sed -n '2280,2370p' DECISIONS.md | grep -n -o -E '.{25}(^|[^0-9:.,–-])(13|14|9|23|24)([^0-9:.,–-]|$).{0,15}'
48:s results, and carry the S13 sentence once.
89:PEN-2 is not closed; the A14 overlay priority
```

Every price, cost, version, line count, time and date traces to design :84, :85, :52, :62–67, :95, :111, Phase 3 spec :212/:224, values :125/:126, DECISION_LOG :765/:861 or the pasted `wc -l` (859). The only numbers that are wrong are the line citations under check 3. No invented number found.

### Check 5 — hold-time table against amended #4 (:212) and #5 (:224)

Design rule lines (from the full `cat -n` of design.md):

```text
    42	- Entry: on calendar day E−1 (...), buy 1 MNQ at market on the close of the bar stamped 18:05 ET. ...
    43	- Exit: sell at market on the close of the bar stamped T−5 min on day E (08:25 for 08:30 releases; 13:55 for FOMC). ...
    45	- Skip rules: no trade if the 18:05 bar on E−1 or the exit bar on E is missing, if a data hole lies between them, or if E's session is an early close (data or exchange) that ends before the target exit (E8 lists the three Good Friday NFP days, data ending 09:15: 1N exits at 08:25 and is unaffected; any later exit is skipped).
    62	**2A — as published (hold through the release).** Long 1 MNQ from the close of the 18:05 ET bar on E−1 to the close of the 16:05 ET bar on E. BLOCKED BY MFFU RULE on Rapid and Pro Sim Funded (§0). Run only as a research benchmark, never deployable on a Sim Funded account.
    66	- For every T1 release at time T on day E (CPI/NFP 08:30, FOMC statement or FOMC Minutes 14:00): exit at the close of the bar stamped T−5; re-enter long at the close of the bar stamped T+3 (fills at T−4 and T+4, outside T±2).
    67	- Exit: close of the bar stamped 16:05 ET on E.
    68	- Skip the whole post-release leg on any early-close day (E8) and on any day with an OPEN-4 release until that list exists.
```

Which section each skip rule belongs to, and whether 2A has one:

```text
$ echo -n 'design :62 skip/early-close words -> '; sed -n '62p' $D/design.md | grep -c -i -E 'skip|early'; echo -n 'design :45 skip rule mentions 2A -> '; sed -n '45p' $D/design.md | grep -c '2A'; echo -n 'design :68 mentions 2A -> '; sed -n '68p' $D/design.md | grep -c '2A'; sed -n '41p;54p;61p;62p;64p;68p' $D/design.md | cut -c1-120 | nl -ba
design :62 skip/early-close words -> 0
design :45 skip rule mentions 2A -> 0
design :68 mentions 2A -> 0
     1	**Rules (1-minute bars, end-stamped; US Eastern local time).**
     2	## 2. Strategy 2 — Macroeconomic Announcement-Day Premium (ADP)
     3
     4	**2A — as published (hold through the release).** Long 1 MNQ from the close of the 18:05 ET bar on E−1 to the close of t
     5	**2S — split hold, compliant with the T1 rule; its evening entry carries the UNVERIFIED overnight question (OPEN-1) [D1;
     6	- Skip the whole post-release leg on any early-close day (E8) and on any day with an OPEN-4 release until that list exis
```

(:41, the "Rules" heading over :42–46, sits under §1 Strategy 1; §2 starts at :54; :68 is a 2S bullet.)

The early-close event days the design's own evidence names, and what the data holds on them:

```text
$ git -C /Users/admin/Praxis.build-r6 show bf6fcc7:docs/reports/2026-11-09-r6-step1-manager.md | grep -n -E 'Good Friday|2021-04-02|2023-04-07|2026-04-03' | cut -c1-240 | head -8
195:event days whose data ends before 16:00: [('2021-04-02', '091500'), ('2023-04-07', '091500'), ('2026-04-03', '091500')]
$ F=~/praxis-signals/b2-data/NQ-continuous-1min.nt8import.txt; for d in 20210402 20230407 20260403; do printf '%s bars=%s last=' $d "$(grep -c "^$d " $F)"; grep "^$d " $F | awk '$2<"170000"' | tail -1 | cut -d';' -f1; printf '   16:05 bar present: '; grep -c "^$d 160500" $F; done
20210402 bars=552 last=20210402 091500
   16:05 bar present: 0
20230407 bars=555 last=20230407 091500
   16:05 bar present: 0
20260403 bars=551 last=20260403 091500
   16:05 bar present: 0
```

(Exit code 1 came from the last `grep -c` returning 0 matches, which is the result being shown.)

A second early-close date seen in the data (whether it is a release day is UNVERIFIED, not checked against any calendar in this session):

```text
$ grep '^20250703 13' $F | tail -1; grep '^20250703 1[89]' $F | head -1
20250703 131500;24054;24071.25;24053.25;24067.25;775
20250703 180100;24067.5;24069;24038;24044.25;626
```

| Variant | Entry / exit (design) | Entry's call #4 | Entry's call #5 | This check |
|---|---|---|---|---|
| 1N, 1C | 18:05 E−1 (or 20:00) → 08:25 E | no conflict | no conflict | Agree. Entry is after 18:00; exit 08:25 is before 16:00 and before the 09:15 Good Friday end; :45 skips if the exit bar is missing. |
| 1F | 18:05 E−1 (or 20:00) → 13:55 E, or earlier override | no conflict | no conflict | Agree. On an early close before 13:55, :45 skips the trade; the override exits with no re-entry. |
| 2A | 18:05 E−1 → 16:05 E | CONFLICT (past 16:00:00) | no conflict | Agree on the 16:00 tail. **Missed:** on early-close days 2A has no rule. :62 has no skip, :45 covers Strategy 1 and :68 covers 2S. On the three event days named at report :195 the data ends 09:15 and there is no 16:05 bar, so 2A as written holds across the early close. Amended #4 flattens "at the exchange's early close on an early-close day if earlier", so this is a second #4 conflict. |
| 2S | 18:05 E−1; out T−5, back T+3; → 16:05 E | CONFLICT (as 2A); T+3 re-entries before 16:00 | no conflict | Agree. Re-entries at 08:33 / 14:03 bar closes fall outside 16:00–18:00. On early-close days :68 skips the post-release leg. Edge case, UNVERIFIED whether any date in range has it: :68 skips only the *post*-release leg, so a T1 release timed after that day's early close would leave the pre-release leg open across the early close. |
| #5 (all) | — | — | no conflict | Agree. :224 says "The system's own trading is not disabled by this breaker". |
| 16:00–18:00 no-entry | — | — | — | No variant enters in that window (18:05 / 20:00 entries; re-entries before 16:00). Agree. |

The entry's text at :2348: "the design skips any exit after an early close (:45, :68) and closes before any early close (constraint (iii) :24). No conflict is found in the text". For 2A the first half is false: neither cited line covers 2A. The second half only restates the design's constraint (iii); no rule implements it for 2A.

### Check 6 — S2, S8, S4

```text
$ grep -n -o -i -E '.{30}\b(implemented|tested|passed|PASS|verified|OBSERVED|working|cleared|satisf[a-z]*)\b.{0,30}' /tmp/r6w1/entry.txt
1:test engine authorised, first pass only (Mac-side Python event s
4:t filing that row sits in the working copy, after the 859 lines of
15:(O4). No VM time in the first pass.
18: as design :102 states, first pass only: a Mac-side Python event
26:arameter optimisation in this pass. Design :46:
29: no optimisation in the first pass. Size 1 MNQ (1 NQ shown along
41:on 2024-06-11, E5). The first pass reports a 20:00 ET entry and
46:ed as research, not as a gate pass." The R6 report names no gate
48:." This entry does NOT clear, satisfy or move F3. The master's read
55:close day if earlier → cancel working entry orders, send market ord
71:es are not changed. The first pass simulates the design as writt
82:gn :102 plus this entry): not implemented, not tested.
$ grep -n -o -E '.{40}(D2|Amear).{0,40}' /tmp/r6w1/entry.txt
3: under D-2026-11-08-D D1, changeable by Amear. Not Amear's ruling. An authorisation e
4:othing bought), pulled forward to P0 by Amear's D-2026-11-08-D D7 (DECISIONS.md:1940–
44:ly, design §3 (:71–80). Nothing bought: D2(a) (`specs/SPEC_RUBRIC.md`:443–444) and
44:es a FREE release list (nothing bought, D2(a)); until it does, 1F and 2S stay prov
48:tor is a separate arm pulled forward by Amear's D7 and is not downstream of `4uu`"; t
76:dow. | OPEN (F2 changes state only when Amear approves the breaker proposal, A6) |
```

S2: PASS. The engine is "SPECIFIED ONLY ... not implemented, not tested". No higher level is claimed for anything.
S8: PASS. Nothing is bought; no D2 item is decided; OPEN-1, OPEN-5 and F4 are left open; OPEN-3 is handled through the master's prior D1 closure H01, which the entry cites rather than answers fresh.
S4: PASS. The pre-write check is recorded at :2284–2289. Re-run:

```text
$ git show HEAD:DECISIONS.md | grep -c D-2026-11-12-B
0
$ grep -c D-2026-11-12-B DECISIONS.md
2
```

The premise "after D6 failed" (:2283) carries no citation in the entry. It is supported elsewhere:

```text
$ grep -n -i 'D6 fail\|D6 failed\|fails at every tier\|failed at every tier\|D7 fired\|D7 trigger' DECISIONS.md DECISION_LOG.md HANDOFF.md STATUS.md | cut -c1-260 | head -15
DECISIONS.md:1940:D7  If D6 fails at every tier at 1 MNQ: do not design breaker values
...
HANDOFF.md:289:**D6 result → D7 FIRED** (report `docs/reports/2026-11-09-d6-drawdown-check-manager.md`; computed on NT8 Standard-resolution lists, MNQ derived, no breakers). At 1 MNQ the committed values-spec measure (worst of four, values spec :139) fails eve
```

### Check 7 — format

```text
$ grep -c -F 'optimistic; Standard resolution' entry
1
$ grep -n -F 'optimistic; Standard resolution' entry | cut -d: -f1
91
$ tail -1 entry == S13 sentence?   (compared with the sentence extracted from rubric :139)
LAST-LINE-MATCHES-RUBRIC-SENTENCE
$ grep -c -i (the forbidden word)
0
$ grep -c -E 'COMMIT-(INDEX|DIFF-SHA256)' entry
0
$ grep -c email pattern
0
$ grep -c -F status phrase
3:**Status:** Decided by master under D-2026-11-08-D D1, changeable by Amear. Not Amear's
```

The S13 sentence appears once, as line 91 of 91 (DECISIONS.md:2370), and matches the rubric S13 text byte for byte. The forbidden word count is 0, both COMMIT strings 0, emails 0. The Status line is present. PASS.

### Check 8 — append-only

```text
$ git diff --numstat HEAD -- DECISIONS.md
92	0	DECISIONS.md
$ git show HEAD:DECISIONS.md | wc -l
    2278
$ git diff HEAD -- DECISIONS.md | grep -c "^-[^-]"
0
```

92 lines added (:2279–2370), 0 deleted. PASS.

## Findings

1. **MAJOR — missed early-close conflict for 2A, and a false claim about the source (:2348).** The entry says "the design skips any exit after an early close (:45, :68)" and "No conflict is found in the text." But :45 is Strategy 1's skip rule (under the §1 "Rules" heading :41), and :68 is the 2S skip. Design :62 gives 2A no skip and no early-close rule (grep counts 0, 0, 0 above). The design's own evidence (step-1 report :195) names three event days whose data ends at 09:15, with no 16:05 bar (pasted above). On those days 2A as written holds across the early close. Amended #4 (:212) flattens "at the exchange's early close on an early-close day if earlier". That is a second 2A conflict under amended #4, and on those days the authorised engine ("simulates the design as written, 2A and 2S to the 16:05 bar included", :2350) has no exit bar to use. Mitigation: every 2A result is already labelled as conflicting with #4, and 2A is a research benchmark only. Smaller sub-point, UNVERIFIED whether any date in range has it: 2S's :68 skips only the post-release leg, so the case of a release timed after that day's early close is not covered either.

2. **MAJOR — D2(a) citation points at the wrong rule (:2323).** `specs/SPEC_RUBRIC.md`:443–444 at HEAD `c29d08b` (the HEAD the entry names) is the middle of D1 ("it as "decided by master under ..." / "Amear may reverse ..."). D2(a) is at :446–447. The number is copied from D-2026-11-12-A (:2251), written against `e3323a8`, before `c29d08b` moved the D block down 3 lines. The two prior entries (:2085, :2156) cite :446–447.

3. **MINOR — D1 citation stale (:2283).** `specs/SPEC_RUBRIC.md`:437–442 at HEAD covers a filer-note line, a blank line, the fence, the header and the first two of D1's five lines. D1 is :441–445. Same cause as Finding 2.

4. **MINOR — F4 range short by one line (:2329).** `specs/SPEC_RUBRIC.md`:33–41 leaves out :42 "**Blocks.** Block 4. Block 5." The "NOT MET" label has no source in the rubric. It comes from DECISION_LOG :861, which is not cited at that point.

5. **MINOR — paraphrase drift from the master row on F3 timing (:2327).** DECISION_LOG :861 (d) says the report "states its fill resolution and slippage in writing before it runs". The entry says "in writing before its results". Rubric F3 :20–22 asks for it "stated in writing before the backtest runs". The entry's own item 6 does state both before any run, so the effect is small, but the duty it hands to the R6 report is weaker than the row it relies on.

6. **MINOR — paraphrase drift from H01 (:2325, :2363).** DECISION_LOG :765 H01 says an R6 strategy "is graded against the existing walk-forward gates as written". The entry says "set beside" those gates, and :2363 says "no gate is graded". Read as "this entry grades nothing", :2363 is fine. But "set beside" restates a master D1 decision in softer words without saying so.

7. **MINOR — uncited premise (:2283).** "after D6 failed" carries no citation. It is supported at HANDOFF.md:289 ("D6 result → D7 FIRED"), pasted above.

Counts: BLOCKER 0, MAJOR 2, MINOR 5. Checks 1, 2, 4, 6, 7 and 8 PASS. Check 3 FAIL (Findings 2–4). Check 5 FAIL (Finding 1).

## Result: FAIL

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
