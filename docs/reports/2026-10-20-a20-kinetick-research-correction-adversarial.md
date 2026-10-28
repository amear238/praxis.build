# a20 Kinetick research: post-audit correction, ADVERSARIAL

**Bead:** Praxis_build-a20 · **Mode:** ADVERSARIAL (read-only except this file) · **Date:** 2026-10-20
**Artifact:** `docs/reports/2026-10-20-a20-kinetick-research.md`. Attacked: line 2 and `## Post-audit correction (2026-10-20)` (artifact :494 to :1148).
**Pristine:** `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/6d0e9294-2389-48c6-9c19-27f79fa5cae6/scratchpad/a20-original.md` (491 lines, sha256 `747b5084a2c02c9a…`).
**Criteria:** B1 (S2, S6), B2 (S1), M1–M4; `specs/SPEC_RUBRIC.md` S1 :107, S2 :108, S6 :112, S8 :114.
Line numbers: "artifact :N" means the artifact as it is now. "audited :N" means the pristine copy.

## Process log
1. `diff` pristine vs artifact; spot-checked the +1 offset on 10 lines.
2. Read the whole appended section. Built the set of lines to check from the pristine copy using a wider pattern than §2's own (`Simulated|connected to|any reading|below|No old connection log|:113|only option|changes nothing|other connection|demo server|item 13`), then read the key lines in full.
3. Re-ran every o2a and o2b source read: migration ledger :124, git log -S, brief :15/:65, walkthrough log :11/:20, the HEAD count, DECISION_LOG :424/:426/:427, update 2 :64/:67, results :21/:46, walkthrough :74, capture notes :50-55, reference :33, migration concerns, adversary-B :14/:22. Checked each output line verbatim against the artifact.
4. Re-ran o2c (Config.xml; lines 1–14 counted only, never printed), o3a, o3b, o3c (parts), o3d, o3e, o4a, o4b, o4c and o2d. Ran extra probes for unit and wording checks.
5. Checked the section's claims about each option against its own §5 table.

## Verification evidence

All three scripts below are adversary-run (this worker), 2026-10-20, under `bash`. `chk` reads a command's output line by line and runs `grep -qxF` against the artifact. It prints `m/n verbatim`, plus any line it could not find.

```
$ diff <pristine> <artifact> | grep -E '^[0-9]'
1a2
491a493,1148
$ sed -n 2p <artifact>
**Post-audit correction (2026-10-20) appended at the end; it supersedes the lines it names.**
$ (pristine :N == artifact :N+1 for N in 14 15 85 106 108 119 136 370 427 455)
14 ok … 455 ok   (all 10 ok)
```

```
# rerun1.sh: o2a / o2b sources
[mig124] 1/1   [gitlogS] 1/1   [brief] 2/2   [wlog] 2/2   [headcount] 1/1
[dl424] 1/1    [dl426] 1/1     [dl427] 1/1   [upd2] 2/2   [results] 2/2
[advB] 2/2     [concerns] 5/5
(migration repo: git status --porcelain on DECISION_LOG.md, the brief, the walkthrough log → empty)
praxis-repo: ls: docs/briefs/2026-10-19-in-vm-nt8-finish-and-usb.md: No such file or directory
praxis-repo: ls: docs/reports/2026-10-19-walkthrough-log.md: No such file or directory
```

```
# rerun2.sh / rerun3.sh: o1, o2c, o2d, o3a–e, o4a–c
[o1] 20/20  [walk74] 1/1  [capture] 6/6  [ref33] 1/1  [o4b] 2/2  [o2d] 4/4
[cfg-hash] 2/2  [cfg-blocks] 14/14  [cfg-sim] 4/4  [cfg-head] 1/1
extra: any '<Name>' at line >=15 containing Simulat:
25:       <Name>Simulated Data Feed</Name>
extra: ConnectOptions tags at line >=15: 15, 65
[o3d-kin] 19/19  [o4a-26] 1/1  [o4a-split] 2/2
extra: HDS lines (all log/*.txt) not "Connection (lost|restored) to": 0
[o3a-null] 3/3  [o3a-arm] 2/2  [o3b] 5/5  [o3e-null] 1/1  [o3e-arm] 4/4
[o3c-eod] 1/1  [o3c-12] 1/1  [o3c-prov] 5/5  [o4c] 5/5
o3c -o vs lines (kinetick[^s]|kinetick$, unit files excluded):
     135      <- with -o (matches), the artifact's figure
     129      <- without -o (lines)
final-check.md matches for 'quote freshness|last-tick-age|Continuum': 0
'identical output' labels in the section: 15; 'differed only by a cut width…': 1 (artifact :1136)
```

## Findings

### F1. MAJOR (S2, S8; criterion 4): §6 makes a false factual claim about the options
- **Artifact :730:** "A is the only option that leaves the Simulated Data Feed as the sole connection, which matches the restated D-071 on its plain words."
- **Defect:** option D also leaves the Simulated Data Feed as the sole connection. The section's own §5 row D (artifact :722) says D "Adds no connection" and is "Not crossed on its words". §8's replacement S6 bullet says "D adds no connection". So the PRAXIS lean toward A rests partly on a premise that contradicts the section's own table. The brief asks specifically for this kind of error ("which options add no connection").
- **Evidence:** artifact :722 vs :730 (see the grep -n output in the process log; the text is quoted above).
- **Smallest fix:** "A and D both leave the Simulated Data Feed as the sole connection. A is the only one of them that changes nothing (D is a settings change and departs from item 13)."

### F2. MAJOR (S8): §6 drops the conditional and assumes how Amear reads the scope
- **Artifact :731:** "B and C would need Amear to amend the restated D-071 first."
- **Defect:** this is unconditional. Whether the restated D-071 covers a data-only connection is the question the section itself leaves to Amear (§5 header, artifact :715: "Whether Amear meant them to cover a data-only connection is his to say"; open question 2, §7: "Does that cover…? If it does…"). The audited :136 had the hedge ("**B and C**, if D-071 covers them, would need Amear to amend it first"). The correction removed it, so S8 got worse. A blanket "all INFERRED" header does not turn an assumed answer into a question.
- **Smallest fix:** "B and C, *if the restated D-071 covers a data-only connection*, would need Amear to amend it first."

### F3. MAJOR (B1 history accuracy; S2/S6): an omitted nuance in the sources changes the reading
- **Artifact :578, :580, :586** (§3 i, iii, "Where it stands now") and §4.
- **Defect:** the section quotes, but never draws out, what its own o2a paste shows. In the original 10-19 regime the **Simulated Data Feed was already allowed alongside "Simulation"**:
  - D-071 itself: "the Part 4 test chart still runs on "Simulated Data Feed"".
  - Brief :15: "Allowed connections: "Simulated Data Feed" and "Simulation" only."
  - Brief :65: ""Simulated Data Feed" and/or "Simulation" may connect by itself: both allowed."

  Two consequences go unstated:
  - (a) §3 (iii) approves results :46 ("D-071 accepted only "Simulation" connected") and walkthrough :74 as having "kept the two apart". But by the same-day brief, that K5 framing was itself wrong. The Simulated Data Feed being connected was never outside the 10-19 allowance. So the master's framing error was two-layered: the false equivalence, and a K5 "mismatch" that was not one under the 10-19 rules. Neither the master's 16:36:23Z row nor this section names the second layer. The brief required C4 "plus the master's framing error", and C4 (§4) does not carry it.
  - (b) The restated D-071 ("the Simulated Data Feed is the one allowed connection") **narrows** the 10-19 allowance. It drops "Simulation", the demo server. That server connected by itself on 10-19 (walkthrough log :20, "Simulation connected"). On the restatement's plain words (INFERRED), a future auto-connect of "Simulation" would now be an "other connection". That is an S6 cross-block consequence, and §4/§8 omit it. "Where it stands now" (:586) says only "The original D-071 named "Simulation"", which reads as if the Simulated Data Feed was outside the original allowance.
- **Evidence:** rerun1 `[mig124] 1/1`, `[brief] 2/2` and `[results] 2/2` confirm the quoted source lines verbatim. The texts are as quoted above.
- **Smallest fix:** add to §3/§4 (C4): "On 10-19 both connections were allowed (D-071 Part 4 clause; brief :15, :65). So results :46 / walkthrough :74 misstated D-071 as 'only Simulation', and K5's firing was not a mismatch under the 10-19 rules. The restatement narrows the allowance to the Simulated Data Feed alone. On its words a 'Simulation' auto-connect would now be outside it (INFERRED; Amear's to confirm)."

### F4. MINOR (S2): §5 row B calls the parenthetical scope "cannot be settled here" without citing the brief that bears on it
- **Artifact :720**, original-D-071 column: "Whether the parenthetical was the scope of 'no other connection' or only examples cannot be settled here."
- **Defect:** the same-day brief the section pastes (o2a) reads "No broker, no Rithmic, **nothing else**" (:15) and "**Any other connection: rule 1.**" (:65). That is the operational reading the 10-19 walkthrough ran under. It is not D-071 itself, so "cannot be settled" is defensible, but the evidence that leans one way goes unmentioned.
- **Smallest fix:** append "(the same-day brief :15 reads 'nothing else'; :65 'Any other connection: rule 1'. REPORTED)".

### F5. MINOR (S2, wrong unit; criterion 5): o3c counts with `-o` are called "lines"
- **Artifact :901:** "The positive arm `kinetick[^s]|kinetick$` gives **483** lines (135 excluding the unit's files)."
- **Defect:** the pasted command is `grep -rnoiI … | wc -l`. With `-o` each **match** is printed on its own line, so the figure counts matches, not lines. Excluding the unit files: 135 matches vs 129 lines. The section's own count note (§9, "`grep -c` counts matching **lines**, not occurrences") makes the mislabel conspicuous. Adversary B's "251 **hits**" (adversarial-B :99) has no stated unit either.
- **Evidence:** the rerun2 tail shows `135` with -o and `129` without.
- **Smallest fix:** "483 matches (135 excluding the unit's files; 129 lines)".

### F6. MINOR (S1 provenance; criterion 3): one block's "identical output" label is false, and which one is not said
- **Artifact :1136** vs the 15 block labels "(re-run of correction-worker-1's commands; identical output)".
- **Defect:** :1136 admits "one file differed only by a cut width the worker edited after its run". At least one of the 15 labels is therefore inaccurate, and the reader cannot tell which. Every output this adversary re-ran matched the artifact verbatim, so the pasted *content* holds. The *label* does not.
- **Smallest fix:** name the block and change its label to "identical except `cut -c` width (N → M)".

### F7. MINOR (register completeness; criterion 2): audited :124 (Q4 row A) is not in the §2 register
- **Defect:** §5 restates row A (artifact :719, now with INFERRED labels and the restated D-071). But §5 says it supersedes only "audited :125-127". Audited :124 ("Consistent with both", unlabelled, judged against the old D-071) is not in the register with a status. So two row As coexist and the section does not say which wins. All other lines the section supersedes are in the register, and all register "now" numbers are +1. I checked this.
- **Smallest fix:** add a register row `:124 | :125 | SUPERSEDED | §5 row A`, and change §5's header to "Supersedes audited :124-127".

### F8. MINOR (path ambiguity; criterion 1): two migration-repo paths are cited bare in prose
- **Artifact :578:** `docs/briefs/2026-10-19-in-vm-nt8-finish-and-usb.md:15` and "The walkthrough log … (`:11`)". These have no `~/Windows-migration/` prefix, while the ledger in the same bullet does have one. They exist only in the migration repo (rerun1: `No such file or directory` in Praxis.build), so a reader resolving them from this repo gets nothing. o2a's `cd` makes them recoverable.
- **Smallest fix:** prefix both with `~/Windows-migration/`.

## Survived
1. **Append-only (criterion 6):** the diff is exactly `1a2` plus one tail hunk `491a493,1148`. The pointer text matches the brief character for character. The +1 offset holds on 10 sampled lines. The pristine sha256 prefix `747b5084a2c02c9a` matches the section's stated hash.
2. **Quotes verbatim (criterion 1):** migration ledger :124, git log -S → `dd076ef`, brief :15/:65, walkthrough log :11/:20, DECISION_LOG :424/:426/:427, HEAD count 0, update 2 :64/:67, results :21/:46, walkthrough :74, capture notes, reference :33, migration concerns and adversary-B :14/:22 are all verbatim (rerun1/rerun3, every line found). Dates and attributions check out: D-071 14:05Z 10-19 Amear; 15:55:42Z Amear; 16:36:23Z praxis-master; 16:37:30Z Amear. The migration-repo records are committed (porcelain empty).
3. **Config.xml C4:** 272 lines; `ConnectOptions` spans :15–:65 and holds exactly three blocks (Simulator "Simulated Data Feed" `true`; Kinetick `false`; Playback "Playback Connection" `false`). The only `<Name>` containing "Simulat" is :25. At line ≥15 "Simulation" appears 3 times, all non-connection fields. Lines 1–14 have 0, counted without printing.
4. **B2 nulls with arms re-run and matching:** the NQCONT import null `exit=1` with arm 16/16; the four outside briefs null with NQCONT arms; outside-repo code null `exit=1` with arm 2 files (16 in scope); adversary-B S4 (12 files), S6 (`DECISIONS.md:4` is a `-c` count; this correction to audited :370 is right); old-log kinetick 0 in all 17 files.
5. **M4:** 26 "Historical Data Server" lines, 13 lost + 13 restored, 0 of any other form (across every `log/*.txt` too).
6. **M1:** a re-run matches this report, the fix-check (W6), worker1 and `DECISIONS.md`. The final-check (W5) has 0 matches. This confirms the replacement (W5 = final-check, W6 = fix-check per audited :474-475).
7. **M3/M5:** HEAD DECISION_LOG has 59 lines and 0 "NT8 PURGED" matches. S6 is `:112` and S7 is `:113`.
8. **S8, other parts:** open question 2 (§7), the replacement summary line 5 and the §8 S6 entry each leave scope to Amear. Summary line 5's "the only option that adds no connection and changes nothing" is true as a conjunction (D adds none but changes something). K1 is left to Amear throughout.

**Result:** FAIL. Three MAJOR findings (F1 false option claim, F2 S8 hedge removed, F3 omitted 10-19 allowance and narrowing). Five MINOR.

VERDICT: FAIL
