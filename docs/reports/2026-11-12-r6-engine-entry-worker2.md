# 2026-11-12 — R6 engine entry D-2026-11-12-B, adversarial re-check after cure (worker2)

## Task

Mode: ADVERSARIAL, narrow re-check. Repo `/Volumes/Sensidine/Praxis.build`, branch `main`, HEAD `c29d08b`. Artifact: entry D-2026-11-12-B, `DECISIONS.md`:2279–2370 (uncommitted). Pre-cure copy `/tmp/r6entry/DECISIONS.pre-cure.md`. Prior check: `docs/reports/2026-11-12-r6-engine-entry-worker1.md`, section Findings (2 MAJOR, 5 MINOR). Points checked: (1) the diff stays inside :2279–2370; (2) whether each of the 7 findings is cured; (3) every new or changed quotation is verbatim in its cited line, and every new citation points where it says; (4) the early-close text and the 2A row against amended breaker #4 (`docs/specs/2026-11-05-phase3-build-specification.md`:212), and no new number without a source; (5) the invariants still hold. No file other than this report was edited. No index or HEAD change.

## Checks run (pasted output)

### Check 1 — diff against the pre-cure copy

```text
$ diff /tmp/r6entry/DECISIONS.pre-cure.md /Volumes/Sensidine/Praxis.build/DECISIONS.md; echo "exit=$?"
2283c2283
< **Authority chain.** Amear's ruling D-2026-11-08-A R6 (DECISIONS.md:1572–1579: research and backtest on the existing 1-minute data only, nothing bought), pulled forward to P0 by Amear's D-2026-11-08-D D7 (DECISIONS.md:1940–1944) after D6 failed. D1: `specs/SPEC_RUBRIC.md`:437–442. R6 step 1 design: `bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md`, on branch `r6/announcement-research` in the worktree `/Users/admin/Praxis.build-r6`, not on `main` (cited below as "design :N"). The master's closures of R6 OPEN-3 and OPEN-4 (H01, H03): DECISION_LOG.md:765 (row 2026-11-09T17:32:00Z). This run's master row: DECISION_LOG.md:861 (row 2026-11-12T09:03:23Z, items (c) and (d)); at filing that row sits in the working copy, after the 859 lines of DECISION_LOG.md at HEAD `c29d08b`. Bead `Praxis_build-ckh`. Fenced quotations below are whole lines copied by script from the cited source; short quotations in running text are parts of the cited line.
---
> **Authority chain.** Amear's ruling D-2026-11-08-A R6 (DECISIONS.md:1572–1579: research and backtest on the existing 1-minute data only, nothing bought), pulled forward to P0 by Amear's D-2026-11-08-D D7 (DECISIONS.md:1940–1944) after D6 failed (HANDOFF.md:289 at `c29d08b`: "D6 result → D7 FIRED"). D1: `specs/SPEC_RUBRIC.md`:441–445. R6 step 1 design: `bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md`, on branch `r6/announcement-research` in the worktree `/Users/admin/Praxis.build-r6`, not on `main` (cited below as "design :N"). The master's closures of R6 OPEN-3 and OPEN-4 (H01, H03): DECISION_LOG.md:765 (row 2026-11-09T17:32:00Z). This run's master row: DECISION_LOG.md:861 (row 2026-11-12T09:03:23Z, items (c) and (d)); at filing that row sits in the working copy, after the 859 lines of DECISION_LOG.md at HEAD `c29d08b`. Bead `Praxis_build-ckh`. Fenced quotations below are whole lines copied by script from the cited source; short quotations in running text are parts of the cited line.
2323c2323
< **4. Event calendar.** Free sources only, design §3 (:71–80). Nothing bought: D2(a) (`specs/SPEC_RUBRIC.md`:443–444) and R-1104-3 (design :119). H03, DECISION_LOG.md:765, in part: "R6 step 2 (the backtest unit) sources a FREE release list (nothing bought, D2(a)); until it does, 1F and 2S stay provisional." So the backtest unit must also try to source a free list of the non-T1 releases inside the 1F and 2S holds (design OPEN-4 :113; constraint (ii) :23). If it cannot, every 1F and 2S result is labelled provisional. A list that could only be bought is not bought; it is reported as not sourced.
---
> **4. Event calendar.** Free sources only, design §3 (:71–80). Nothing bought: D2(a) (`specs/SPEC_RUBRIC.md`:446–447) and R-1104-3 (design :119). H03, DECISION_LOG.md:765, in part: "R6 step 2 (the backtest unit) sources a FREE release list (nothing bought, D2(a)); until it does, 1F and 2S stay provisional." So the backtest unit must also try to source a free list of the non-T1 releases inside the 1F and 2S holds (design OPEN-4 :113; constraint (ii) :23). If it cannot, every 1F and 2S result is labelled provisional. A list that could only be bought is not bought; it is reported as not sourced.
2325c2325,2327
< **5. Grading.** H01, DECISION_LOG.md:765, in part: "no bar is written, lowered or waived." Any R6 result is set beside the existing walk-forward gates as written (`docs/specs/2026-11-06-walk-forward-values.md`:125, gate 4 "≥ 250 aggregate OOS trades"; :126, gate 5 "≥ 60% of walk-forward windows profitable"), and, in the same row's words, "so an R6 result is reported as research, not as a gate pass." The R6 report names no gate as passed. The design §5 measures (:87–98) are reported as research measures.
---
> **5. Grading.** H01, DECISION_LOG.md:765, in part: "no bar is written, lowered or waived." In the same row's words, "any R6 event strategy is graded against the existing walk-forward gates as written" (`docs/specs/2026-11-06-walk-forward-values.md`:125, gate 4 "≥ 250 aggregate OOS trades"; :126, gate 5 "≥ 60% of walk-forward windows profitable"), and "so an R6 result is reported as research, not as a gate pass." The R6 report names no gate as passed. The design §5 measures (:87–98) are reported as research measures.
> 
> **6. Rubric F3 (FROZEN).** F3 (`specs/SPEC_RUBRIC.md`:19–31) concerns "The fill resolution the Strategy Analyzer will actually run at" and blocks "`4uu`. Everything downstream of `4uu`." This entry does NOT clear, satisfy or move F3. The master's reading that the R6 simulator sits outside F3's block is DECISION_LOG.md:861 item (d), in part: "the R6 Python simulator is a separate arm pulled forward by Amear's D7 and is not downstream of `4uu`"; this entry relies on that reading and does not grade it. The R6 report must state its fill resolution (1-minute bars, signals on bar close, fills at the next bar's open) and its slippage (2 ticks/side on the judged rows, 4 ticks/side on the sensitivity row) in writing before the backtest runs (F3's own timing, `specs/SPEC_RUBRIC.md`:20–22; DECISION_LOG.md:861 item (d), "before it runs") and again in the report before its results, and carry the S13 sentence once. No NT8 Strategy Analyzer run and no NT8 replication in step 2; any NT8 replication is later, on the VM, under its own DECISIONS.md entry.
2327,2329c2329
< **6. Rubric F3 (FROZEN).** F3 (`specs/SPEC_RUBRIC.md`:19–31) concerns "The fill resolution the Strategy Analyzer will actually run at" and blocks "`4uu`. Everything downstream of `4uu`." This entry does NOT clear, satisfy or move F3. The master's reading that the R6 simulator sits outside F3's block is DECISION_LOG.md:861 item (d), in part: "the R6 Python simulator is a separate arm pulled forward by Amear's D7 and is not downstream of `4uu`"; this entry relies on that reading and does not grade it. The R6 report must state its fill resolution (1-minute bars, signals on bar close, fills at the next bar's open) and its slippage (2 ticks/side on the judged rows, 4 ticks/side on the sensitivity row) in writing before its results, and carry the S13 sentence once. No NT8 Strategy Analyzer run and no NT8 replication in step 2; any NT8 replication is later, on the VM, under its own DECISIONS.md entry.
< 
< **7. MFFU.** Design OPEN-1 (:110, evening entry vs holding overnight) and OPEN-5 (:114, the low-volume / stale-fill rule) stay OPEN; this entry decides neither. The R6 report makes no funded-account eligibility claim; design :89 already says an evening-entry variant "cannot qualify for any funded-account tier row until OPEN-1 is answered in writing by MFFU". Rubric F4 (`specs/SPEC_RUBRIC.md`:33–41) stays FROZEN / NOT MET.
---
> **7. MFFU.** Design OPEN-1 (:110, evening entry vs holding overnight) and OPEN-5 (:114, the low-volume / stale-fill rule) stay OPEN; this entry decides neither. The R6 report makes no funded-account eligibility claim; design :89 already says an evening-entry variant "cannot qualify for any funded-account tier row until OPEN-1 is answered in writing by MFFU". Rubric F4 (`specs/SPEC_RUBRIC.md`:33–42) stays FROZEN / NOT MET.
2345c2345
< | 2A | 18:05 bar on E−1 | 16:05 bar on E | :62 | CONFLICT: holds past 16:00:00; its exit signal is the close of the 16:05 bar | no conflict |
---
> | 2A | 18:05 bar on E−1 | 16:05 bar on E | :62 | CONFLICT: holds past 16:00:00; its exit signal is the close of the 16:05 bar. Second CONFLICT on early-close days: 2A has no early-close rule (:62), so it holds across an early close (below) | no conflict |
2348c2348
< Early close: amended #4 flattens at the exchange's early close if earlier; the design skips any exit after an early close (:45, :68) and closes before any early close (constraint (iii) :24). No conflict is found in the text (a reading of text, not a test). The design's own flat-by measure (:95) checks "zero positions at 16:10 ET or across 16:10-18:00", which is MFFU's 16:10, not amended #4's 16:00.
---
> Early close: amended #4 flattens at the exchange's early close if earlier. Strategy 1 skips any exit after an early close (:45: "any later exit is skipped"; 1N and 1C exit at 08:25, before the data's 09:15 end on the Good Friday NFP days the design names there) and 2S skips its post-release leg on an early-close day (:68). 2A's rule (:62) carries no early-close skip, so on an early-close event day 2A as written holds across the early close: a second conflict with amended #4, and also with the design's own constraint (iii) (:24, "before any early close"). This is a reading of the design text, not a test. The design's own flat-by measure (:95) checks "zero positions at 16:10 ET or across 16:10-18:00", which is MFFU's 16:10, not amended #4's 16:00.
2350c2350
< Disposition. The strategies are not changed. The first pass simulates the design as written, 2A and 2S to the 16:05 bar included, without breakers as design :116 (O4) states, and the R6 report labels every 2A and 2S result as conflicting with amended breaker #4's 16:00 flat. 2A is already a research benchmark only (:62). A live or breakers-on version of 2A or 2S would need a resolution of this conflict; none is decided here.
---
> Disposition. The strategies are not changed. The first pass simulates the design as written, 2A and 2S to the 16:05 bar included, without breakers as design :116 (O4) states, and the R6 report labels every 2A and 2S result as conflicting with amended breaker #4's 16:00 flat. 2A is already a research benchmark only (:62). A live or breakers-on version of 2A or 2S would need a resolution of these conflicts; none is decided here.
2365c2365
< - No resolution of the 2A/2S conflict with amended #4; no breaker text or value is changed; no strategy rule is changed.
---
> - No resolution of the 2A/2S conflicts with amended #4; no breaker text or value is changed; no strategy rule is changed.
exit=1
```

```text
$ cmp <(head -n 2282 /tmp/r6entry/DECISIONS.pre-cure.md) <(head -n 2282 DECISIONS.md) && echo identical-first-2282
identical-first-2282
$ diff /tmp/r6entry/DECISIONS.pre-cure.md DECISIONS.md | grep -E "^[0-9]"
2283c2283
2323c2323
2325c2325,2327
2327,2329c2329
2345c2345
2348c2348
2350c2350
2365c2365
```

Every hunk is in :2283–2365, inside :2279–2370. Lines 1–2282 are byte-identical to the pre-cure copy. The hunks `2325c2325,2327` and `2327,2329c2329` are one rewrite of item 5 plus a re-alignment by diff: item 6 is now :2327 and item 7 is :2329. Line count is unchanged at 2370. PASS.

### Check 2 sources — rubric, HANDOFF, DECISION_LOG, design

Source files are unchanged against HEAD, except DECISION_LOG.md (+2, the row at :861) and the walk-forward values spec. The cited lines :125–126 of that spec are the same at HEAD and in the working copy:

```text
$ git diff --numstat HEAD -- specs/SPEC_RUBRIC.md HANDOFF.md DECISION_LOG.md docs/specs/2026-11-06-walk-forward-values.md docs/specs/2026-11-05-phase3-build-specification.md
2	0	DECISION_LOG.md
21	21	docs/specs/2026-11-06-walk-forward-values.md
$ sed -n '125,126p' docs/specs/2026-11-06-walk-forward-values.md            (working copy)
  4. ≥ 250 aggregate OOS trades
  5. ≥ 60% of walk-forward windows profitable
$ git show HEAD:docs/specs/2026-11-06-walk-forward-values.md | sed -n '125,126p'
  4. ≥ 250 aggregate OOS trades
  5. ≥ 60% of walk-forward windows profitable
```

```text
$ awk 'NR>=435 && NR<=452 {print NR": "$0}' specs/SPEC_RUBRIC.md
435: 
436: Filer's note, not a ruling: Amear's words, copied by script from DECISIONS.md
437: :1906–1927 (the D-2026-11-08-D verbatim block).
438: 
439: ```text
440: STANDING RULE CHANGE — AUTONOMY
441: D1  Default-decide. When a unit or the master reaches a question that
442:     would otherwise go to Amear, it takes the recommended option, logs
443:     it as "decided by master under D-2026-11-08-D D1", and continues.
444:     Amear may reverse any such decision later; the reversal is filed
445:     like any ruling. No unit waits on Amear except for D2 items.
446: D2  Only four things stop and wait for Amear's word: (a) spending
447:     money; (b) switching live trading on, or any order path to a
448:     funded account; (c) changing circuit-breaker values while real
449:     money is at stake; (d) installing keys, credentials or agent
450:     permissions. Everything else is D1.
451: D3  The Telegram commit-approval step in the Hermes setup is removed.
452:     Commits land on an audit PASS. Telegram informs; it does not ask.
```

```text
$ sed -n '17,43p' specs/SPEC_RUBRIC.md | cat -n | awk '{ $1=$1+16; print }'
17 ## FROZEN — nothing downstream may proceed until these clear
18
19 ### F3 — Backtest fill resolution vs. acquired data granularity
20 **Criterion.** The fill resolution the Strategy Analyzer will actually run at,
21 and the slippage assumption applied at the band edge, stated in writing before
22 the backtest runs.
23 **Why frozen.** The Block 2 spec requires Order Fill Resolution = High with a
24 1-tick resolution series, 1-tick slippage, $2.96 round-trip. Deviation F
25 delivered 1-minute bars. High-resolution fill modelling needs a finer intrabar
26 series. A band-touch strategy backtested on 1-minute bars with no intrabar
27 resolution produces optimistic fills exactly where the edge lives, and the
28 optimism is invisible in the output.
29 **Unblocks when.** The assumption is committed and the backtest report carries
30 it as a stated limitation.
31 **Blocks.** `4uu`. Everything downstream of `4uu`.
32
33 ### F4 — MFFU automation compliance
34 **Criterion.** Written confirmation from MFFU that this specific automation
35 pattern is permitted on a funded account.
36 **Why frozen.** Flagged as blocking in the Round 1+2 compilation, still open in
37 the Phase 2 closure document, still open in the Phase 3 output summary, absent
38 from the session-28 build report. The plan documents also contradict each
39 other: the Round 3 handoff asserts automation is explicitly permitted; Phase 2
40 closure states it has not been confirmed by direct inquiry.
41 **Owner.** Amear. Not a build task — an email.
42 **Blocks.** Block 4. Block 5.
43
```

```text
$ echo "--- RUBRIC :33-42 NOT MET count"; sed -n 33,42p specs/SPEC_RUBRIC.md | grep -F -c 'NOT MET'
--- RUBRIC :33-42 NOT MET count
0
$ grep -n -F 'NOT MET' specs/SPEC_RUBRIC.md | cut -c1-200
(no output)
$ sed -n 861p DECISION_LOG.md | grep -F -c 'NOT MET'
1
$ sed -n 861p DECISION_LOG.md | grep -o '.\{160\}NOT MET.\{60\}'
mitted and carried in the backtest report; blocks `4uu` and everything downstream of it) and F4 (MFFU written confirmation of this pattern on a funded account; NOT MET; blocks Block 4 and 5). **Decided by master under D-2026-11
$ sed -n 861p DECISION_LOG.md | awk '{ print "NOT MET at char", index($0,"NOT MET"); print "(b) first at char", index($0,"(b) "); print "(c) at char", index($0,"(c) "); print "(d) at char", index($0,"(d) ") }'
NOT MET at char 1016
(b) first at char 1178
(c) at char 1580
(d) at char 2071
$ sed -n 861p DECISION_LOG.md | grep -F -c 'states its fill resolution and slippage in writing before it runs'
1
```

```text
$ git -C /Users/admin/Praxis.build-r6 show bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md > /tmp/r6design-bf6fcc7.md
$ sed -n 24p /tmp/r6design-bf6fcc7.md
- (iii) Every position opened at or after 18:00 ET is closed before 16:10 ET in the same MFFU session, and before any early close.
$ sed -n 41p /tmp/r6design-bf6fcc7.md
**Rules (1-minute bars, end-stamped; US Eastern local time).**
$ sed -n 45p /tmp/r6design-bf6fcc7.md
- Skip rules: no trade if the 18:05 bar on E−1 or the exit bar on E is missing, if a data hole lies between them, or if E's session is an early close (data or exchange) that ends before the target exit (E8 lists the three Good Friday NFP days, data ending 09:15: 1N exits at 08:25 and is unaffected; any later exit is skipped).
$ sed -n 62p /tmp/r6design-bf6fcc7.md
**2A — as published (hold through the release).** Long 1 MNQ from the close of the 18:05 ET bar on E−1 to the close of the 16:05 ET bar on E. BLOCKED BY MFFU RULE on Rapid and Pro Sim Funded (§0). Run only as a research benchmark, never deployable on a Sim Funded account.
$ sed -n 68p /tmp/r6design-bf6fcc7.md
- Skip the whole post-release leg on any early-close day (E8) and on any day with an OPEN-4 release until that list exists.
$ sed -n 36,38p /tmp/r6design-bf6fcc7.md
- 1N (core): Employment Situation (NFP), release 08:30 ET. In the abstract; free dates.
- 1C (extension, labelled NOT IN THE ABSTRACT): CPI, 08:30 ET.
- 1F: FOMC statement, 14:00 ET ("similar to the pre-FOMC returns").
```

### Check 3 — each new or changed quotation against its cited line

These are all quotations in the changed lines :2283, :2325, :2327, :2329 and :2348. :2323, :2345, :2350 and :2365 have no new quotation. :2323's H03 quotation is unchanged from pre-cure.

```text
$ git show c29d08b:HANDOFF.md | sed -n 289p | grep -F -c 'D6 result → D7 FIRED'
1
$ sed -n 289p HANDOFF.md | grep -F -c 'D6 result → D7 FIRED'
1
$ sed -n 765p DECISION_LOG.md | grep -F -c 'no bar is written, lowered or waived.'
1
$ sed -n 765p DECISION_LOG.md | grep -F -c 'any R6 event strategy is graded against the existing walk-forward gates as written'
1
$ sed -n 765p DECISION_LOG.md | grep -F -c 'so an R6 result is reported as research, not as a gate pass.'
1
$ sed -n 125p docs/specs/2026-11-06-walk-forward-values.md | grep -F -c '≥ 250 aggregate OOS trades'
1
$ sed -n 126p docs/specs/2026-11-06-walk-forward-values.md | grep -F -c '≥ 60% of walk-forward windows profitable'
1
$ sed -n 20p specs/SPEC_RUBRIC.md | grep -F -c 'The fill resolution the Strategy Analyzer will actually run at'
1
$ sed -n 31p specs/SPEC_RUBRIC.md | grep -F -c '`4uu`. Everything downstream of `4uu`.'
1
$ sed -n 861p DECISION_LOG.md | grep -F -c "the R6 Python simulator is a separate arm pulled forward by Amear's D7 and is not downstream of \`4uu\`"
1
$ sed -n 861p DECISION_LOG.md | grep -F -c 'before it runs'
1
$ sed -n 89p /tmp/r6design-bf6fcc7.md | grep -F -c 'cannot qualify for any funded-account tier row until OPEN-1 is answered in writing by MFFU'
1
$ sed -n 45p /tmp/r6design-bf6fcc7.md | grep -F -c 'any later exit is skipped'
1
$ sed -n 24p /tmp/r6design-bf6fcc7.md | grep -F -c 'before any early close'
1
$ sed -n 95p /tmp/r6design-bf6fcc7.md | grep -F -c 'zero positions at 16:10 ET or across 16:10-18:00'
1
```

All 15 quotations are verbatim (count 1 each). Now the new line citations and the claims in :2348 that are not quoted but are tied to a cited line:

```text
$ sed -n 45p /tmp/r6design-bf6fcc7.md | grep -F -c 'data ending 09:15'
1
$ sed -n 45p /tmp/r6design-bf6fcc7.md | grep -F -c 'three Good Friday NFP days'
1
$ sed -n 45p /tmp/r6design-bf6fcc7.md | grep -F -c '1N exits at 08:25 and is unaffected'
1
$ sed -n 45p /tmp/r6design-bf6fcc7.md | grep -F -c '1C'
0
$ sed -n 23p /tmp/r6design-bf6fcc7.md | grep -F -c 'PAD-E core variants exit at 08:25'
1
$ sed -n 117p /tmp/r6design-bf6fcc7.md | grep -F -c '1N/1C exit 08:25'
1
$ sed -n 62p /tmp/r6design-bf6fcc7.md | grep -F -c -i 'early'
0
$ sed -n 62p /tmp/r6design-bf6fcc7.md | grep -F -c -i 'skip'
0
$ sed -n 68p /tmp/r6design-bf6fcc7.md | grep -F -c 'Skip the whole post-release leg on any early-close day'
1
$ sed -n 116p /tmp/r6design-bf6fcc7.md | grep -F -c 'First pass runs without breakers'
1
```

New citations, each checked: HANDOFF.md:289 holds "D6 result → D7 FIRED" (correct). SPEC_RUBRIC :441–445 is D1 exactly (correct). :446–447 is D2(a) "(a) spending / money" (correct). :20–22 is F3's "stated in writing before / the backtest runs" (correct). :33–42 is F4 from heading to Blocks (correct). Design :45 is Strategy 1's skip rule, under the Strategy 1 "Rules" heading at :41 (correct). :68 is 2S's skip (correct). :62 has no early-close or skip word (correct, "carries no early-close skip"). :24 is constraint (iii) (correct). One exception: :45 names 1N only, not 1C (Finding B below).

### Check 4 — early-close text and 2A row against amended #4; new numbers

```text
$ sed -n 212p docs/specs/2026-11-05-phase3-build-specification.md
> 4. Session flat gate — clock reaches 16:00:00 ET, or the exchange's early close on an early-close day if earlier → cancel working entry orders, send market orders closing all system positions, confirm flat before 4:10 PM ET (alert if not), and refuse new system entries until the next session opens at 18:00 ET.
$ sed -n 212p docs/specs/2026-11-05-phase3-build-specification.md | grep -F -c "or the exchange's early close on an early-close day if earlier"
1
```

Conflict calls, read against :212:
- 2A second CONFLICT on early-close days. Right. #4 flattens at the early close if it comes before 16:00:00. Design :62 holds 2A to the 16:05 bar and gives it no skip (counts 0 and 0 above). So 2A holds across the early close.
- 2A also breaks design constraint (iii) :24 "before any early close". Right, verbatim.
- Strategy 1 is not in conflict on early-close days. Right: :45 skips the trade when the early close ends before the target exit.
- 2S skips its post-release leg on an early-close day (:68). Right as text. One case is still UNVERIFIED (raised by worker1, not tested here): a T1 release whose T−5 exit falls after that day's early close.

Numbers that the cure adds:

```text
$ diff /tmp/r6entry/DECISIONS.pre-cure.md DECISIONS.md | grep '^<' | grep -oE '[0-9][0-9:.,–-]*' | sort -u > /tmp/r6w2-old-nums.txt; diff /tmp/r6entry/DECISIONS.pre-cure.md DECISIONS.md | grep '^>' | grep -oE '[0-9][0-9:.,–-]*' | sort -u > /tmp/r6w2-new-nums.txt; echo "numbers in new changed lines, absent from old changed lines:"; comm -13 /tmp/r6w2-old-nums.txt /tmp/r6w2-new-nums.txt
numbers in new changed lines, absent from old changed lines:
08:25,
09:15
20–22
24,
289
33–42
4,
441–445.
446–447
45:
```

Each has a source: 08:25 and 09:15 are at design :45 (counts above). 20–22, 33–42, 441–445 and 446–447 are rubric line citations, checked above. 289 is the HANDOFF line, checked. "4," is "#4,". "24," and "45:" are design line citations. No number without a source.

Supplementary data probe, read-only, on the 1-minute file the design names at :84. It shows the last bar before 18:00 on a few candidate early-close dates:

```text
$ F=~/praxis-signals/b2-data/NQ-continuous-1min.nt8import.txt; ls -l $F; for d in 20210402 20230407 20250703 20241129 20211126; do echo "$d last bar before 18:00: $(grep "^$d " $F | awk '{split($2,t,";"); if (t[1] < "180000") last=$0} END{print last}' | cut -c1-40)"; done
-rw-r--r--@ 1 admin  staff  95900139 Jul 23 13:02 /Users/admin/praxis-signals/b2-data/NQ-continuous-1min.nt8import.txt
20210402 last bar before 18:00: 20210402 091500;16764.5;16766.25;16760.2
20230407 last bar before 18:00: 20230407 091500;16268;16272.5;16266.25;1
20250703 last bar before 18:00: 20250703 131500;24054;24071.25;24053.25;
20241129 last bar before 18:00: 20241129 175800;22731;22731;22731;22731;
20211126 last bar before 18:00: 20211126 131500;19473.5;19477;19468;1947
```

On 2021-04-02 and 2023-04-07 the data ends at 09:15, matching design :45. On 2025-07-03 the data ends at 13:15. UNVERIFIED: whether 2025-07-03 is an event date in the design's calendar (not checked against any release list in this session). If it is, it is an early-close event day that the design's E8 list (three Good Friday NFP days) does not name. The entry's 2A conflict wording is general ("on an early-close event day"), so it stays correct either way. Not graded.

### Check 5 — invariants

```text
$ git diff --numstat HEAD -- DECISIONS.md
92	0	DECISIONS.md
$ git diff HEAD -- DECISIONS.md | grep -c "^-[^-]"
0
$ git show HEAD:DECISIONS.md | wc -l
    2278
$ wc -l < DECISIONS.md
    2370
$ cmp <(git show HEAD:DECISIONS.md) <(head -n 2278 DECISIONS.md) && echo identical-first-2278
identical-first-2278
$ grep -n "Fills are optimistic" DECISIONS.md | tail -3 | cut -d: -f1
2203
2278
2370
$ sed -n 2279,2370p DECISIONS.md | grep -c "Fills are optimistic"
1
$ sed -n 2279,2370p DECISIONS.md | grep -n "Fills are optimistic" | cut -d: -f1   (relative line within the 92-line entry)
92
$ sed -n 2370p DECISIONS.md | grep -F -x -c "$(sed -n 289p HANDOFF.md | grep -o "Fills are optimistic[^*]*assumed\.")"
1
$ tail -c 1 DECISIONS.md | od -c
0000000   \n                                                            
0000001
$ sed -n 2279,2370p DECISIONS.md | grep -i -c "v[e]rdict"
0
$ sed -n 2279,2370p DECISIONS.md | grep -c "COMMIT-I[N]DEX"
0
$ sed -n 2279,2370p DECISIONS.md | grep -c "COMMIT-DIFF-SHA[2]56"
0
$ sed -n 2279,2370p DECISIONS.md | grep -c @
0
```

0 deletions. The S13 sentence occurs once in :2279–2370. It is the whole of :2370 (`grep -x` count 1), the last line of the file, ending in a newline. The banned-word, banned-marker and '@' counts are all 0. PASS.

## Findings

### Status of worker1's 7 findings

1. **MAJOR (missed 2A early-close conflict; false ":45, :68" source claim): CURED in substance. A residual is left, graded MINOR as Finding A.** :2348 no longer says "the design skips any exit after an early close (:45, :68)" or "No conflict is found". It now gives :45 to Strategy 1 and :68 to 2S, says :62 has no skip, and names a second 2A conflict with #4 and with :24. The 2A cell at :2345 carries it too. The calls are right against :212 (Check 4).
2. **MAJOR (D2(a) at :443–444): CURED.** :2323 now cites :446–447, which is D2's "(a) spending / money" (awk output above).
3. **MINOR (D1 at :437–442): CURED.** :2283 now cites :441–445, which is D1 from its label to "No unit waits on Amear except for D2 items."
4. **MINOR (F4 range :33–41; "NOT MET" unsourced): PARTLY CURED.** The range is now :33–42 and includes :42 "**Blocks.** Block 4. Block 5." The "NOT MET" label is still unsourced at :2329: rubric count 0. Its only source found is DECISION_LOG.md:861 at char 1016, before item (a)/(b). The authority chain cites :861 for "items (c) and (d)" only (char 1580 and 2071). Residual graded as Finding C.
5. **MINOR (F3 timing "before its results"): CURED.** :2327 now requires the statement "in writing before the backtest runs", citing rubric :20–22 and DECISION_LOG :861 (d) "before it runs" (both verbatim, Check 3). The report must repeat it before its results.
6. **MINOR ("set beside" vs H01 "graded against"): CURED.** :2325 now quotes H01 verbatim, "any R6 event strategy is graded against the existing walk-forward gates as written" (count 1). :2363 "no gate is graded" stays under "What this entry does not decide". There it reads as this entry grading nothing, which worker1 accepted.
7. **MINOR (uncited "after D6 failed"): CURED.** :2283 now cites HANDOFF.md:289 at `c29d08b`, "D6 result → D7 FIRED", verbatim at HEAD and in the working copy.

### New or residual findings in the current text

A. **MINOR: residual of worker1 Finding 1. The engine instruction has no rule for 2A on early-close days.** :2350 is unchanged in substance: "The first pass simulates the design as written, 2A and 2S to the 16:05 bar included ... and the R6 report labels every 2A and 2S result as conflicting with amended breaker #4's 16:00 flat." On an early-close event day there is no 16:05 bar on E. Design :62 gives 2A no skip, and :45's "exit bar on E is missing" skip is Strategy 1's rule. So "as written" does not say what the engine does with 2A on those days. The data shows 09:15 ends on 2021-04-02 and 2023-04-07, and a 13:15 end on 2025-07-03 (whether that date is an event date is UNVERIFIED). A whole-entry search finds no rule for the missing exit:

```text
$ sed -n 2279,2370p DECISIONS.md | grep -c -i "early.close.*exit bar\|no 16:05 bar\|missing exit"
0
```

The label instruction also names only the 16:00 conflict, not the new early-close one. Every 2A result is still labelled as conflicting, though. Graded MINOR rather than MAJOR because 2A is a research benchmark only (:62), every 2A result already carries a conflict label, and the cases are a handful of days. The backtest unit will still have to choose an exit rule that this entry does not give.

B. **MINOR: new. "1C" is attributed to design :45.** :2348 reads "(:45: "any later exit is skipped"; 1N and 1C exit at 08:25, before the data's 09:15 end on the Good Friday NFP days the design names there)". :45 names 1N only (count for '1C' is 0). 1C is the CPI variant (:37), so it does not trade on NFP days just because they are NFP days. That 1C exits at 08:25 is sourced elsewhere (:23, :117, counts 1), but not at :45, and not as a Good Friday NFP case.

C. **MINOR: residual of worker1 Finding 4.** At :2329, "NOT MET" still has no citation at the point of use. The rubric does not contain the phrase (count 0). DECISION_LOG.md:861 does, but outside the items (c) and (d) that the authority chain names.

D. **MINOR: new ambiguity made by the cure, 2S row (:2346, unchanged).** "CONFLICT: as 2A." The 2A cell now holds two conflicts: the 16:00 tail, and the early close. Read literally, "as 2A" gives 2S the early-close conflict too. :2348 says 2S skips its post-release leg on early-close days, which is the opposite.

E. **MINOR: new inconsistency, :2358 (unchanged).** "What remains is the 2S/2A tail past 16:00:00 under amended #4, recorded above." Since the cure, a second conflict also remains under amended #4 (2A across an early close), and :2350 and :2365 now say "these conflicts" / "conflicts" in the plural. In context, :2358 is about what is left of OPEN-2's own list, which never named early close. But as written it says the 16:00 tail is all that remains.

Counts: BLOCKER 0, MAJOR 0, MINOR 5 (A–E). Of worker1's findings, 5 are cured (2, 3, 5, 6, 7), 1 is cured in substance with a MINOR residual (1, see A), and 1 is partly cured with a MINOR residual (4, see C). Checks 1, 3, 4 and 5 PASS. Check 3's citation sub-check has one exception (B).

## Result: PASS

PASS here means no BLOCKER or MAJOR is open: both of worker1's MAJORs are cured. Five MINORs remain, listed above for the filer to dispose of.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
