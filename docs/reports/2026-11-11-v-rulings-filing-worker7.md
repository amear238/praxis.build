# Unit 2026-11-11-v-rulings-filing — worker 7 report

## Task
Second fix pass on D-2026-11-11-A (DECISIONS.md) after the worker 6 attack: fixes 1–6 in entry A, plus MANIFEST fixes 7–8 (rows :388, :389, :399 and two appended rows).

## Mode
BUILD (fix).

## Criterion
The brief's fixes 1–8. DECISIONS.md lines 1–2099 byte-identical to HEAD `d056e91`. Every new quotation copied by script and byte-identical to its cited line. The S13 sentence appears exactly once per entry, as that entry's standalone last line. MANIFEST diff touches only :388, :389, :399 and the two appended lines; MANIFEST lines 1–387 equal `/tmp/vrf-manifest-before.md` lines 1–387.

## Process log
1. Backups: `cp MANIFEST.md /tmp/vrf-manifest-pre7.md`; `cp DECISIONS.md /tmp/vrf-decisions-pre7.md`.
2. Read the source lines: proposal :79, DECISION_LOG.md :828 and :829, DECISIONS.md :2082, :2085, :2089, :1744–1745, :2054, topology :41, return-handoff :72.
   - "stays open" IS on DECISION_LOG.md:829 ("(4) the VM-to-n8n path (O1) stays open"), so I used that wording.
   - The D-2026-11-10-B line "The path in full is the one at :41." is DECISIONS.md:2054 (found with `grep -n`).
3. Checked that the amended #4/#5 text does not exist. `grep -n 'F2-1' docs/specs/2026-11-05-phase3-build-specification.md` (the Phase 3 breaker spec) gave no output. `git diff --stat HEAD` on that file was empty.
4. Applied fixes 1–6 with `/tmp/vrf7/edit.py`. Each quotation is a slice of its source line, read at run time and checked with `assert q in src`. Each `old_string` was checked to occur exactly once. The script asserts that lines 1–2099 are unchanged before it writes.
   - Fix 2: the entry no longer says "also requires" in its own voice, and states the #4/#5 requirement only through the DECISION_LOG.md:828 quote. The rubric clause block and the A6 sentence are kept. The A6 sentence now ends "; this entry changes no rubric state."
   - Fix 4: the preceding sentence about D-2026-11-10-C and the script-copied :2082 clause are kept. Only the "Decision 4 records that…re-ask him." sentence is replaced.
5. Applied fixes 7–8 with `/tmp/vrf7/man.py` (exact single-occurrence replacements; two rows inserted before the trailing newline). New ranges: entry A 2101–2171 (heading :2101), entry B 2173–2200 (heading :2173). Fix 6 added a line to entry A, which moved entry B down by one.
6. Wrote no memory files, nothing under `.claude/`, no `bd remember`, no git add, commit or stash, no network.

## Verification evidence

### Headings, `wc -l`, removed-line count, head byte-identity
In the pasted command below, the S13 sentence's literal text is replaced by `<S13>`. That keeps it to exactly one occurrence in this report (the last line). The command I actually ran had the literal sentence inside the single quotes.
```
$ S='<S13>'
$ grep -n '^## 2026-11-11' /tmp/vrf-decisions-pre7.md | cut -c1-60; wc -l < /tmp/vrf-decisions-pre7.md
$ grep -n '^## 2026-11-11' DECISIONS.md | cut -c1-60; wc -l < DECISIONS.md
$ git diff HEAD -- DECISIONS.md | grep -c '^-[^-]'
$ cmp <(sed -n 1,2099p DECISIONS.md) <(git show HEAD:DECISIONS.md | sed -n 1,2099p) && echo IDENTICAL; git show HEAD:DECISIONS.md | wc -l
== BEFORE headings/wc (pre7 copy)
2101:## 2026-11-11 — D-2026-11-11-A: Amear's rulings V1–
2172:## 2026-11-11 — D-2026-11-11-B: VM handoff §1 limit 
    2199
== AFTER headings/wc
2101:## 2026-11-11 — D-2026-11-11-A: Amear's rulings V1–
2173:## 2026-11-11 — D-2026-11-11-B: VM handoff §1 limit 
    2200
== removed-line count vs HEAD
0
== head 1-2099 cmp HEAD
IDENTICAL
    2099
```

### S13 standalone counts and last-line checks
`grep -cxF` matches whole lines only, so a count of 1 means the sentence stands alone on its line.
```
$ echo "A count: $(sed -n 2101,2172p DECISIONS.md | grep -cxF "$S")  B count: $(sed -n 2173,2200p DECISIONS.md | grep -cxF "$S")  file-wide substring count in 2100-end: $(sed -n '2100,$p' DECISIONS.md | grep -cF "$S")"
$ echo "A last nonblank line no.: $(awk 'NR>=2101&&NR<=2172&&NF{n=NR}END{print n}' DECISIONS.md)"; sed -n 2171p DECISIONS.md | grep -cxF "$S"
$ echo "B last line no.: $(wc -l < DECISIONS.md) ; last line exact:"; tail -n1 DECISIONS.md | grep -cxF "$S"; tail -c1 DECISIONS.md | od -c | head -1
== S13 per entry
A count: 1  B count: 1  file-wide substring count in 2100-end: 2
A last nonblank line no.: 2171
1
B last line no.:     2200 ; last line exact:
1
0000000   \n
```

### Fixed passages after the edit (line number, then the full line)
```
== line 2108
**V2 — Rule F2-1: APPROVED (A6).** (return-handoff :45–48.) The words put to Amear were the channel's summary, return-handoff :46: "flat by 16:00 ET governs; a position open at 15:00 may stay open until 16:00; no new system entries 16:00–18:00 ET." Amear: "Uh, yeah, you have my approval." (return-handoff :47). It is filed as closing the A6 hold, that is, Amear's approval, the first of the three parts OPEN-F2-5 names at `docs/specs/2026-11-10-f2-session-flat-proposal.md`:79 (its resolution cell, copied by script: "Amear's approval under A6; then a DECISIONS.md entry and the amended #4/#5 text in the breaker spec."), on the words put to him at return-handoff :46. The amended #4/#5 text does not exist, and OPEN-F2-5 is not closed by this entry. Whether his approval reaches the elements (a)–(f) listed below, which were not put to him in those words, is not graded here. That file is called the proposal below. Rule F2-1 as the proposal writes it, copied by script from proposal :20:
== line 2129
DECISION_LOG.md:828 records "its unblock also needs breaker specs #4 and #5 amended" (copied by script from DECISION_LOG.md:828). This entry amends neither (that is a later unit) and grades no part of the unblock clause. A6 ties F2's state change to Amear's approval ("F2's state changes when Amear approves the proposed values", DECISIONS.md:1744–1745, line break joined); this entry changes no rubric state.
== line 2155
3. MFFU's "we do not offer Rithmic" (return-handoff :120) contradicts D-2026-11-10-B's broker route (DECISIONS.md:2054: "The path in full is the one at :41."; the topology path ends "→ Rithmic → account.", `docs/specs/2026-11-10-live-signal-topology.md`:41). D-2026-11-10-B is not edited. The route is recorded as contradicted and is NOT re-decided here; that is the next unit (DECISION_LOG.md:829: "next unit").
== line 2156
4. The VM-to-n8n path (O1, return-handoff :71) stays open. The channel recommends an "SSH reverse tunnel from the Mac for sim testing (no new exposure of n8n)" (return-handoff :71); that tunnel would use SSH keys, which is a D2(d) item ("(d) installing keys, credentials or agent permissions", `specs/SPEC_RUBRIC.md`:446–447, line break joined), so it waits for Amear. D-2026-11-10-C records Amear's 20:42Z words about a reverse tunnel as REPORTED BY Amear and the tunnel as UNVERIFIED (DECISIONS.md:2085, :2089); decision 4 does not change that. Amear's 20:42Z clause, copied by script from DECISIONS.md:2082: "n8n reachability is settled: an SSH reverse tunnel lets the VM reach the Mac's n8n at http://127.0.0.1:5678, and n8n stays closed to the network". The tunnel Amear describes there is REPORTED BY Amear and UNVERIFIED (DECISIONS.md:2089, :2085). DECISION_LOG.md:829 keeps O1 open; the difference between his "is settled" and "stays open" is recorded here, not resolved.
== line 2165
- Confirming or changing the per-firm profile direction (O2, return-handoff :72) is his; decision 1 is changeable by him.
== line 2169
**S6 cross-block.** Block 2 (the NT8 backtest plan's working scope is the V7 list, decision 2; R6's first pass in NT8; any overnight-holding profile needs its own backtest, return-handoff :53). Block 3 (broker route recorded as contradicted, decision 3; VM-to-n8n path open, decision 4; breakers #4 and #5 not amended by this entry). Rubric F2 (Rule F2-1 approved; F2 FROZEN). Rubric F4 (FROZEN / NOT MET). R6 OPEN-1 (open; V6 asked it; MFFU's 23:08:17Z reply did not answer it).
```

### Byte-identity of every quoted span I added (shell check, then Python exact-slice check)
```
== quote identity
MATCH  docs/specs/2026-11-10-f2-session-flat-proposal.md:79 <- DECISIONS.md:2108  [Amear's approval under A6; then a DECISIONS.md entry and the amended #4/#5 text in the breaker spec.]
MATCH  DECISION_LOG.md:828 <- DECISIONS.md:2129  [its unblock also needs breaker specs #4 and #5 amended]
MATCH  DECISIONS.md:2082 <- DECISIONS.md:2156  [is settled]
MATCH  DECISION_LOG.md:829 <- DECISIONS.md:2156  [stays open]
MATCH  DECISIONS.md:2054 <- DECISIONS.md:2155  [The path in full is the one at :41.]
== python exact-slice check
docs/specs/2026-11-10-f2-session-flat-proposal.md 79 src_idx 39 dst_idx 518 bytes 100 identical True
DECISION_LOG.md 828 src_idx 2181 dst_idx 28 bytes 54 identical True
DECISIONS.md 2082 src_idx 626 dst_idx 918 bytes 10 identical True
DECISION_LOG.md 829 src_idx 1219 dst_idx 935 bytes 10 identical True
DECISIONS.md 2054 src_idx 816 dst_idx 120 bytes 35 identical True
== "also requires" in entry A
0
== #4 and #5 amended mentions in A (line nos)
2116
2126
2129
2169
```
What the four remaining "#4 and #5" lines are:
- :2116 is element (f), the proposed replacement text.
- :2126 is the script-copied rubric block.
- :2129 is the DECISION_LOG.md:828 quote.
- :2169 is the S6 "not amended by this entry".

So the requirement is stated once in the entry's own text, through the :828 quote.

### Identifier scan (DECISIONS.md 2100–end, MANIFEST.md 388–end)
The first scan attempt failed: zsh quoting broke `sed -n "$2,\$p"`, and that run printed empty results. The run below uses `tail -n +N` and is the valid one.
```
== DECISIONS.md 2100-end (     101 lines)
IPv4 (non-127.0.0.1): 
all IPv4 hits:    1 127.0.0.1 
MAC: 
key path: 
Windows machine-name pattern: 
SSH host alias praxis-vm count:        1
== MANIFEST.md 388-end (      14 lines)
IPv4 (non-127.0.0.1): 
all IPv4 hits: 
MAC: 
key path: 
Windows machine-name pattern: 
SSH host alias praxis-vm count:        0
== praxis-vm at HEAD DECISIONS (pre-existing alias)
2
```
- The one `praxis-vm` is in entry B :2182. I did not add it: it was at pre7 :2181, inside the script-copied install reply :2 text. It is the SSH host alias; the same string appears twice at HEAD (D-2026-11-10-C), and the install reply's VM machine name was handled by a placeholder. Whether the alias counts as a "VM machine name" is for the manager to judge. I did not change it (out of scope).
- Rep name: I did not scan for it, because scanning needs the name typed. My added text contains no personal names other than Amear and Hermes (see the passages above).

### MANIFEST diff vs pre7, and lines 1–387 vs before
```
== wc
     399
     401
== diff pre7 -> now
388,389c388,389
< | /DECISIONS.md | Log | 3 | 2026-11-11 | MODIFIED (unit 2026-11-11-v-rulings-fil ...
< | /docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md | Report |  ...
---
> | /DECISIONS.md | Log | 3 | 2026-11-11 | MODIFIED (unit 2026-11-11-v-rulings-fil ...
> | /docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md | Report |  ...
399c399,401
< | /docs/reports/2026-11-11-v-rulings-filing-worker6.md | Report | 3 | 2026-11-11 ...
---
> | /docs/reports/2026-11-11-v-rulings-filing-worker6.md | Report | 3 | 2026-11-11 ...
> | /docs/reports/2026-11-11-v-rulings-filing-worker7.md | Report | 3 | 2026-11-11 ...
> | /docs/reports/2026-11-11-v-rulings-filing-worker8.md | Report | 3 | 2026-11-11 ...
== diff line-address summary
388,389c388,389
399c399,401
== cmp 1-387 vs before
IDENTICAL
```
Changed text in each row (exact replacements made by `/tmp/vrf7/man.py`):
- :388: "appended at lines 2101-2170 (heading :2101)" became "appended at lines 2101-2171 (heading :2101)". "appended at lines 2172-2199 (heading :2172)" became "appended at lines 2173-2200 (heading :2173)".
- :389: "S13 addendum line added at end" became "two-line S13 addendum (a filer's line, then the S13 sentence alone) added at end".
- :399: the description became "ADVERSARIAL worker 6 report for unit 2026-11-11-v-rulings-filing: re-attack on D-2026-11-11-A and -B after worker 5's fixes, the de-identified files, S13 placement and the MANIFEST rows; ungraded at time of row".
- :400 and :401: rows for worker7 and worker8, with the descriptions from the brief and the full unit name filled in.

## Files staged
None. The rules forbid index changes, so nothing was staged. Files written in the working tree:
- `DECISIONS.md` (lines after 2099 only)
- `MANIFEST.md` (:388, :389, :399, plus the appended :400–401)
- this report

Scratch files: `/tmp/vrf7/edit.py`, `/tmp/vrf7/man.py`, `/tmp/vrf-manifest-pre7.md`, `/tmp/vrf-decisions-pre7.md`.

## Not in scope, reported only
- Entry B :2182 carries the SSH alias `praxis-vm`; the disposition is the manager's.
- Fix 4 leaves two sentences in item 4 that both cite :2085 and :2089. The brief asked for both: keep the preceding sentence, and add the new one.

## Result: PASS

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
