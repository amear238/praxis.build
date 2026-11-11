# 2026-11-11 MFFU investigation Correction 1, worker 5

## Task
Unit `2026-11-11-mffu-investigation-correction-1`, worker 5. Authority: DECISION_LOG 2026-11-11T17:32:05Z, decided by master under D-2026-11-08-D D1. Write correction items C5.1 to C5.4 for `docs/reports/2026-11-11-mffu-connection-investigation.md`. The target was read only, from the pristine copy `/tmp/mffu-orig.md`, which is byte-identical to the working-tree report (`cmp` exit 0, pasted in C5.1). The items cover lines 104, 213, 214 and 216. The paste-ready text is at `/tmp/mffu-corr/w5.md`.

## Mode
BUILD

## Rubric criteria
S1, S2, S5 (`specs/SPEC_RUBRIC.md`). Every claim is graded OBSERVED / INFERRED / UNVERIFIED / REPORTED BY. Every item pastes its command and real output. No claim rests on reasoning about a file that was not read in this session.

## Process log
1. Wrote skeletons of both files first. Read target lines 100–106 and 210–220.
2. C5.1: grep for the three effort figures. The only hit is the target, line 213. Graded INFERRED.
3. C5.2: listed `Redemtion/` (42 files, gitignored by `.gitignore:7`). Ran the drawdown-term grep on .md files and a `textutil` loop over every .rtf (find -print0 / read -d ""). Found the prop-firm comparison at `Redemtion/Intitialization-April 2026/PHASE 1 OUTPUT SUMMARY.rtf` §5 (text lines 272–301). It is NOT tracked. It covers Topstep and Apex only. Apex is listed with EOD trailing, plus an intraday option. The file has no MFFU, no Rithmic, no "peak", and no "hostile to breakout". The "most Rithmic prop firms use intraday trailing" generalisation is in no file. Graded REPORTED BY Amear, as relayed in the master's brief.
4. C5.2 found something unexpected. The whole-tree grep for "intraday trailing" hit the tracked `docs/specs/2026-11-05-walk-forward-spec.md` at HEAD, lines 118/121/125/128/139. That spec records MFFU's own Rapid plan as "Eval EOD; Sim-Funded intraday trailing", REPORTED BY MFFU's plans page, fetched 2026-11-05. This contradicts the blanket "MFFU's ... EOD trailing drawdown" on line 216. My first draft of C5.2 item 2 said the phrase appeared nowhere but the target. The pasted output proved that wrong, and I rewrote item 2 and item 4 to match the output before finishing. The current MFFU rule is UNVERIFIED (no network in this unit).
5. C5.3: grep over the whole tree plus the RTF loop for "stay with MFFU" and "connect another way". The only hit is the target, line 216. Graded UNVERIFIED (source not on disk).
6. C5.4: the line 104 quote is verbatim at line 23 of the compilation. That file is NOT tracked (gitignored). The quote is OBSERVED. The file's "only compliant path" (line 42) is scoped to Apex/Topstep. The file never mentions MFFU (count 0) and leaves the Tradovate question open (lines 147, 150). "falsely concluded ... only locked route for prop trading" is INFERRED by Hermes.
7. Ran the final checks: rep-name counts, the S13 sentence absent from w5.md, and no index change by this worker.

Scope notes: I made no broker-route judgement. I made no statement about rubric F4. I made no git index change. The only files written are the two named in the brief.

## Verification evidence
All item-level command output is pasted inside `/tmp/mffu-corr/w5.md` under each `### C5.<n>` heading. Final checks follow.

```text
$ grep -ci "$N" /tmp/mffu-corr/w5.md
0
$ grep -ci "$N" docs/reports/2026-11-11-mffu-investigation-correction-1-worker5.md
0
$ grep -c -i "fills are optimistic" /tmp/mffu-corr/w5.md
0
$ grep -c "^### C5\." /tmp/mffu-corr/w5.md; grep "^### C5\." /tmp/mffu-corr/w5.md
4
### C5.1 — Effort figures in the §6 option table have no source
### C5.2 — Prop-firm drawdown comparison: what the research file says, and what it does not
### C5.3 — The quoted Amear preference has no on-disk source
### C5.4 — The line 104 Tradovate quote is on disk; "falsely concluded ... only locked route" goes beyond the file
$ git diff --cached --name-only
docs/reports/evidence/2026-10-28-mffu-[rep]-reply.png
$ git status --porcelain -- docs/reports/2026-11-11-mffu-investigation-correction-1-worker5.md
?? docs/reports/2026-11-11-mffu-investigation-correction-1-worker5.md
```

## Files written (not staged)
- `/Volumes/Sensidine/Praxis.build/docs/reports/2026-11-11-mffu-investigation-correction-1-worker5.md`
- `/tmp/mffu-corr/w5.md`

## Result
PASS

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
