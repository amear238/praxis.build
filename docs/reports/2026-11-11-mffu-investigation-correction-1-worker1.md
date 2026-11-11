# Correction 1, worker 1: MFFU connection investigation

## Task
Unit `2026-11-11-mffu-investigation-correction-1`, worker 1. This is a re-dispatch with reduced scope. Draft correction items C1.1 to C1.4 against `/tmp/mffu-orig.md`, a pristine copy of `docs/reports/2026-11-11-mffu-connection-investigation.md` (282 lines, untracked in git). The manager pastes the items into the target's `## Correction 1`. Authority: DECISION_LOG 2026-11-11T17:32:05Z, decided by master under D-2026-11-08-D D1. HEAD 85a803f.

## Mode
BUILD (text drafting only). No git index change, no code change, no network, no VM.

## Rubric criteria
- S1: every claim is graded against evidence, and the command and its real output are pasted.
- S2: components are graded SPECIFIED / IMPLEMENTED / TESTED. Specified is not implemented, and implemented is not tested.

## Process log
1. Wrote skeletons of both files. Read the target lines 18-30, 145-175, 205-225 and 268-280.
2. C1.1: read `PraxisSignalConsumer.cs` :36-50 and :632-642, and grepped `RequiredAccountPrefix` (hits at :48, :100, :106, :639). The Sim-only wall is a const and is checked again at the order boundary. That refutes target line 23. The item corrects lines 23, 156-157, 212, 213 and 219. It does not propose or estimate a code change, because the guard is Amear's under D2(b).
3. C1.2: topology :9 (level words), :24 (Redis, SPECIFIED only), :29 (nine breakers, SPECIFIED), :39 (emitter "not built"). `git ls-files`, `ls ninjascript/`, a grep over `ninjascript/*.cs`, and a grep of node types in the workflow JSON. Regraded §4.2 lines 160-169 and §4.1 lines 152-156 one component at a time. Partly existing: the consumer's MaxQty reject (:94, :527-528, :858) is IMPLEMENTED but set as a "sim sanity cap". The consumer parses `ts` but never compares it with the clock. The file-drop relay is TESTED in Block 1 and UNVERIFIED on the current VM (topology :26, cited, not re-run here).
4. C1.3: grepped the return-handoff file. MFFU items 1, 2 and 4 are quoted. "Only … evaluation phase" is the target's wording, not MFFU's. The claim "auto-closed before answering" is graded PARTLY SUPPORTED. The V6 reply asked for identity verification (:132-133), and the ticket was closed for inactivity (:135-136).
5. C1.4: the D-2026-11-10-B entry runs from DECISIONS.md:2047 to :2075 (the next heading is at 2076). **The brief's premise that the entry "still names Rithmic" is not literally true:** the entry has 0 Rithmic hits. The entry adopts "The path in full is the one at :41" (:2054), and topology :41 ends `SubmitBracket → Rithmic → account`. The item states the reference chain exactly.
6. I re-ran every command whose exact form I pasted into w1.md and checked the pasted output against the re-run. Ran the final checks: rep-name counts, no S13 sentence in w1.md, no F4-met wording, 4 headings, index unchanged.

### Second findings (reported, not fixed; out of scope)
- Target line 149 cites the topology diagram at "lines 14, 41". Line 14 of the topology doc is blank (OBSERVED, `sed -n '14p'` printed an empty line 14).
- Topology :23 (row 1.7) says "The workflow JSON is not in the repo (no `n8n/` directory)". There is no `n8n/` directory, but `git ls-files` lists `workflows/EmMbN4sslwIx1ydn.{before,after}-{b1-b,qxd}.json`, which carry webhook path `praxis-signal`. These may be older exports than the live workflow (last updated 2026-07-16 per :23). Whether they match the live workflow is UNVERIFIED.
- Target line 155 grades the file-drop relay OBSERVED. Topology :26 says it is UNVERIFIED on the current VM. C1.2 notes this, but line 155 was not one of the lines the brief assigned for regrading.

## Verification evidence
All item evidence is pasted inside `/tmp/mffu-corr/w1.md` under each item. The final checks were run in this session:

```text
$ grep -ci "$N" /tmp/mffu-corr/w1.md docs/reports/2026-11-11-mffu-investigation-correction-1-worker1.md
docs/reports/2026-11-11-mffu-investigation-correction-1-worker1.md:0
/tmp/mffu-corr/w1.md:0
$ grep -c 'optimistic;' /tmp/mffu-corr/w1.md
0
$ grep -c -i -E 'F4 (is )?(met|closed|nearly)' /tmp/mffu-corr/w1.md
0
$ grep -c '^### C1\.' /tmp/mffu-corr/w1.md
4
$ git diff --cached --name-only
docs/reports/evidence/2026-10-28-mffu-[rep]-reply.png
$ git rev-parse --short HEAD
85a803f
$ wc -l /tmp/mffu-orig.md
     282 /tmp/mffu-orig.md
$ git status --short docs/reports/2026-11-11-mffu-connection-investigation.md
?? docs/reports/2026-11-11-mffu-connection-investigation.md
```

The rep-name count was computed before this report was rewritten in its final form. The manager should re-run it on the final file. The index shows only the pre-existing staged PNG, the same as at session start (from the gitStatus snapshot, `A  docs/reports/evidence/2026-10-28-mffu-[rep]-reply.png`).

## Files staged
None. Files written, both unstaged: this report, and `/tmp/mffu-corr/w1.md`, which is outside the repo.

## Result
PASS. All four items (C1.1-C1.4) are written with pasted evidence. C1.4 records that the D-2026-11-10-B entry names Rithmic only by reference to topology :41.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
