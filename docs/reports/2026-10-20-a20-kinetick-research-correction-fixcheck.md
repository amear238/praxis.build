# a20 Kinetick research: post-audit correction, ADVERSARIAL fix-check

**Bead:** Praxis_build-a20 · **Mode:** ADVERSARIAL, narrow fix-check (read-only except this file) · **Date:** 2026-10-20
**Artifact:** `docs/reports/2026-10-20-a20-kinetick-research.md` (1191 lines). Attacked: the text the fix pass added or changed in `## Post-audit correction (2026-10-20)` (:494 to the end).
**Pristine:** `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/6d0e9294-2389-48c6-9c19-27f79fa5cae6/scratchpad/a20-original.md`.
**Prior adversary:** `docs/reports/2026-10-20-a20-kinetick-research-correction-adversarial.md` (F1–F8). Manager items M-a…M-d.
**Criteria:** `specs/SPEC_RUBRIC.md` S1 :107, S2 :108, S8 :114 (the S6 cite is :112).
Line numbers are the artifact's current lines unless marked otherwise.

## Process log
1. Ran the append-only `diff` first, then read the prior adversary report.
2. Read artifact :490–809, :900–945, :1045–1065 and :1140–1191.
3. Re-ran o6 (migration repo) and checked each output line verbatim against the artifact (`grep -qxF`). Also listed the 10-16 brief's Part headings and rules for context.
4. Re-ran o7 (verbatim check plus the row's full length) and o8 (both counts). Also ran the uncut total and a growth probe on non-unit files newer than adversarial-B.
5. Spot-checked §3 (0)/(iii) and §4's sources: walkthrough :31 and :74, results :46, update 2 :25, :62 and :70, audited :116 and :15, and the body's E-block list.
6. Checked the evidence index against the o-block headers (`^\*\*o[0-9]`), and o4b's "59".

## Verification evidence (adversary-run, 2026-10-20)

```
$ diff <pristine> <artifact> | /usr/bin/grep -E '^[0-9]'
1a2
491a493,1191
```

o6 re-run (cwd `/Users/admin/Windows-migration`):
```
porcelain exit=0
0888f0f Fri Oct 16 12:06:47 2026 -0400
18:## Hard rules
20:1. **Simulation only.** No broker connection, no Rithmic, no new connection of any kind, no orders, not even on Sim101. The only connection allowed is "Simulated Data Feed". If anything else connects or asks to, Amear disconnects it; stop and report.
69:1. Connections: only "Simulated Data Feed" may be connected. If it is not, **Amear** connects it from the Connections menu.
94:1. **Amear** starts NinjaTrader 8 from the Start menu and signs in if asked. "Simulated Data Feed" may connect by itself: that is the old setting and is allowed. Any other connection: rule 1.
--- verbatim check
ok
ok
ok
ok
(brief structure: 25:6. Do not change NinjaTrader settings…; 67:## Part 4: a Simulated Data Feed chart…; 79:## Part 5: the faithful restore; 92:## Part 6: the data check)
```

o7 / o8 re-run (cwd `/Volumes/Sensidine/Praxis.build`):
```
o7 verbatim ok
    1530            <- sed -n 428p DECISION_LOG.md | wc -c  (the row is whole under cut -c1-1700)
      59            <- git show HEAD:DECISION_LOG.md | wc -l
--- o8
     135
     129
--- 483 all  (uncut, no exclusion, now)
     569
```

Growth probe for the §9 S2 "because" claim:
```
$ find . -path ./.git -prune -o -type f -newer docs/reports/2026-10-20-a20-kinetick-research-adversarial-B.md ! -name '2026-10-20-a20-kinetick-research*' -print | (count kinetick[^s]|kinetick$ matches per file)
      15 ./DECISION_LOG.md
       2 ./.claude/agent-memory/praxis-auditor/audit_ruling_superseded_and_name_collisions.md
       2 ./.claude/agent-memory/praxis-manager/project_grep_wrapper_skips_ignored.md
$ sed -n '426,428p' DECISION_LOG.md | /usr/bin/grep -oiE 'kinetick[^s]|kinetick$' | wc -l
       3
$ sed -n '425,432p' DECISION_LOG.md | cut -c1-40
- [2026-10-20T15:55:42Z] WHO: praxis-mas
- [2026-10-20T16:36:23Z] WHO: praxis-mas
- [2026-10-20T16:37:30Z] WHO: amear | WH
- [2026-10-20T16:40:32Z] WHO: praxis-mas
(adversarial-B.md mtime: Oct 20 12:21 local, i.e. 16:21Z EDT)
```

Source spot-checks:
```
walkthrough :31: | P9 | Fusion connections: NinjaTrader connected itself to **"Simulation"**, and Amear accepted that on condition: no orders, no other connection | REPORTED (update 2 `:67`, D-071). …
walkthrough :74: | K5. A dot on any row other than "Simulation" | A connection beyond the one Amear accepted (P9, D-071). …
results :46:     | K | **K5 FIRED** | **Simulated Data Feed has a green dot.** That is a row other than "Simulation" | … D-071 accepted only "Simulation" connected |
update 2 :25:    **NinjaTrader 8.1.7.2 is installed and restored by route (a), faithful** (D-068).
update 2 :62:    | 6 | Restore choice | **(a) Faithful**, Amear's call, 2026-10-16 15:52Z | D-068. Source: the unfiltered 09-29 copy `NinjaTrader 8-full/`, 5,444 files, …
update 2 :70:    **How the restore finished (REPORTED, walkthrough log 16:03Z–16:04Z).** The in-VM agent stopped at the "Simulation" connection. Amear finished by hand. Not recorded: whether the fresh install's files were moved aside first, the brief's whole-set manifest check (expected 5,444, 0 bad) and the read-only counts. …
audited :116:    … INFERRED `false` only via the reported faithful restore from `NinjaTrader 8-full` (update 2 `:62` …
body E-blocks: E7 (:350 code dependency null), E9 (:389 Block 2 daily inputs), E12 (:418 quote-freshness monitor)
o-block headers: o7 :508, o2a :600, o2b :622, o6 :662, o2c :686, o2d :783, o3a :801, o3b :842, o3c :861, o8 :930, o3d :943, o3e :1017, o4c :1042, o4b :1060, o4a :1073, o5 :1138; the §2 block at :520 has NO "o1" label
```

## Check 1: prior findings and manager items

| Item | Status | Current artifact line |
|---|---|---|
| F1 | FIXED | :756 "A and D both leave the Simulated Data Feed as the sole connection, which matches the restated D-071 on its plain words. A is the only one of them that changes nothing (D is a settings change and departs from item 13)." |
| F2 | FIXED | :757 "B and C, if the restated D-071 covers a data-only connection, would need Amear to amend it first." |
| F3 (a) | FIXED | :590 "…K5 firing on the Simulated Data Feed was not outside the 10-19 allowance (INFERRED). This is a second layer of the framing problem (§4, C4)." and :683 |
| F3 (b) | FIXED | :596 "It narrows the 10-19 allowance by dropping "Simulation"… (both INFERRED from the wording)" and :780 §8 (c), "(INFERRED; Amear's to confirm)". Wording defect, see finding 1 |
| F4 | FIXED | :746 row B cites brief `:15` "nothing else" / `:65` "Any other connection: rule 1" and 10-16 rule 1. Label gap, see finding 5 |
| F5 | FIXED | :928 "gives **483** matches (`-o` prints one line per match); 135 matches excluding the unit's files, which is 129 lines (o8, below)". o8 re-run: 135 / 129 |
| F6 | FIXED | :801 o3a's label names the cut-width difference (`-c1-110` vs `-c1-80`). The other blocks say "identical output". :1177 repeats this |
| F7 | FIXED | :564 register row ":124 \| :125 \| SUPERSEDED \| §5 row A". :741 "Supersedes audited :124-127 (now :125-128)" |
| F8 | FIXED | :588 both paths now carry the `~/Windows-migration/` prefix |
| M-a | FIXED | :502 cites `DECISION_LOG.md:428`, pasted as o7 (:510–514). Re-run is verbatim and the row is complete (1530 chars < 1700). Paraphrase defects, see finding 3 |
| M-b | FIXED | :1056 "(searches VERIFIED: E7, E9 (Block 2 daily inputs) and E12 in the body, and the manager-run pastes in the post-audit correction §9)". E7, E9 and E12 exist at audited :350, :389, :418 |
| M-c | FIXED | :684 "The D-071 row's Part 5 swap of the old `Config.xml` and Part 6 recheck were a PLAN (o2a). That the faithful restore … happened is REPORTED". Cite defect, see finding 2 |
| M-d | FIXED | :769 ends "Leaving it off is the only option that changes nothing. Removing it (D) would also add no connection, but it changes the connection list." Unambiguous. Opens with the 10-19 allowance (F3) |

## Findings (Check 2: attack on added or changed text)

### 1. MINOR (factual, vs o2a): "Where it stands now" says D-071 "itself named only 'Simulation'"
- **Artifact :596:** "plus "Simulation", the demo server (D-071, which itself named only "Simulation")".
- **Defect:** the D-071 row (o2a, :611) also names the Simulated Data Feed: "the Part 4 test chart still runs on "Simulated Data Feed"". The fix pass's own §4 :683 uses that same "D-071's Part 4 clause" as evidence that the feed was allowed. The two lines contradict each other. The conclusion (the feed was allowed on 10-19) is unaffected.
- **Smallest fix:** "(D-071, which itself accepted only "Simulation"; its Part 4 clause names the Simulated Data Feed as the test chart's feed)".

### 2. MINOR (S1 cite / S2 omitted caveat): the M-c bullet cites the restore-choice row, and its "fits" inference skips counter-evidence the section itself pastes
- **Artifact :684:** "That the faithful restore from `NinjaTrader 8-full` happened is REPORTED (update 2 `:62` …) … That fits the 10-19 16:03Z "Simulation connected" (walkthrough log `:20`) giving way to the 10-20 "Simulated Data Feed, green dot … Simulation, no dot"."
- **Defect:**
  - (a) Update 2 `:62` is the "Restore choice" row. The report that the restore happened is `:25`, and `:70` adds "Not recorded: whether the fresh install's files were moved aside first". That caveat bears directly on whether the old Config.xml was in effect.
  - (b) The section's own pastes put "Simulation connected" **after** the restore: §3 (i) "at 16:03Z after the restore"; log :20 "NT starts, Simulation connected"; update 2 :67 "Still connected after the restore". The old Config.xml (startup `true` for the Simulated Data Feed only) does not predict that. So "fits" overstates the agreement. The labels INFERRED and "What actually changed … is UNVERIFIED" limit the damage, and no K1 conclusion rests on this.
- **Smallest fix:** cite "update 2 `:25` (`:70`: whether the fresh files were moved aside is not recorded)". Change "That fits…" to "That fits the 10-20 read. It does not by itself explain the 10-19 post-restore "Simulation connected" (log `:20`; update 2 `:67`)".

### 3. MINOR (S2 attribution): §1 presents its own extensions as what the audit row records
- **Artifact :502–505:** "The audit findings below are as recorded in the master's audit-FAIL row `DECISION_LOG.md:428`".
- **Defect:**
  - (a) B1 :503 says the report built "Q4, the PRAXIS view, the S6 block and open question 2" on the equivalence. Row :428 (o7) lists only "`:85`, `:119`, `:136` "under any reading", `:455`". Q4 (audited :124–127) and open question 2 (:462) are the correction's own extension.
  - (b) M2 :505 says audited :15 "does not say where". Row :428 says "summary line 3 says "below" for arms not pasted". That is a stronger finding than the paraphrase. (§9 and M2's new cite do address it.)
- **Smallest fix:** "(Q4 and open question 2 added by this correction)". For M2, quote :428: "says "below" for arms not pasted".

### 4. MINOR (S2, unlabelled causal claim): "That followed update 2 `:67`'s relay"
- **Artifact :590** ("That followed update 2 `:67`'s relay, which named only "Simulation" (ii) (o2b)") and **:683** ("The text followed update 2 `:67`'s relay").
- **Defect:** this is a causal claim with no label. For the walkthrough it is supported, because walkthrough :31 (P9) cites "REPORTED (update 2 `:67`, D-071)". But :31 is neither pasted nor cited, and o2b pastes only :74. For results :46 no source citation was found.
- **Smallest fix:** "(walkthrough P9 `:31` cites update 2 `:67`, REPORTED; that results `:46` followed it too is INFERRED)".

### 5. MINOR (S2, unlabelled interpretive claim; grammar): §5 row B "These lean toward the full scope"
- **Artifact :746:** "…and the 10-16 rule 1 "no new connection of any kind" (o6) (REPORTED, o2a, o6). These lean toward the full scope; still Amear's to say".
- **Defect:**
  - The REPORTED label covers the quotes. "Lean toward the full scope" is an interpretation of D-071's scope and has no INFERRED label.
  - The clause "and the 10-16 rule 1 …" has no verb.
  - S8 holds ("still Amear's to say").
- **Smallest fix:** "…and the 10-16 rule 1 reads "no new connection of any kind" (REPORTED, o2a, o6). INFERRED: these lean toward the full scope; still Amear's to say".

### 6. MINOR (S2, unlabelled and incomplete causal claim): §9 S2 "They differ because the unit's own files have grown since"
- **Artifact :928:** "Adversary B stated **251**. They differ because the unit's own files have grown since; 251 cannot be reconstructed now."
- **Defect:** this is stated as fact, with no label, and it is incomplete. Files outside the unit's set also gained matches after adversarial-B's file (mtime 12:21 local ≈ 16:21Z):
  - `DECISION_LOG.md` rows :426–:428 (16:36Z–16:40Z) hold 3 matches;
  - two `.claude/agent-memory/` files newer than adversarial-B hold 2 each.

  B's unit ("hits") is also unstated (adversarial-B :99).
- **Smallest fix:** "They differ mainly because files have grown since, the unit's own and also `DECISION_LOG.md` :426–:428 (INFERRED); 251 cannot be reconstructed now."

### 7. MINOR (S1 traceability): the evidence index names an "o1" block that carries no o1 label
- **Artifact :1165** "**o1** (§2): …". Also used at :592 "(o1, o2b)" and :598 "(o1 shows those lines)".
- **Defect:** the §2 block header at :520 reads "*Manager-run, 2026-10-20 ~12:55 EDT (re-run …)*" with no "**o1**". Every other block is labelled (o-block header list above). A reader resolving "o1" has to guess.
- **Smallest fix:** prefix :520 with "**o1**. ".

No MAJOR or BLOCKING finding. S8 was checked on every changed passage:
- §6 :754–759 says "reasoning only, not a decision" and "Amear decides".
- §5 :741 and :746 leave the scope to him.
- §7 :769 says "yours to say".
- §8 :777 says "This decides nothing", :780 says "Amear's to confirm", and :781 says "Amear's call".
- K1 stays his throughout (:759).

No VERIFIED label without a paste was found in the changed text: §3 header → o2a/o2b/o6; §8 (a) → o2d; §8 (b) → o5.

## Survived
1. **Append-only (Check 4):** the diff is exactly `1a2` plus one tail hunk `491a493,1191`.
2. **o6:** the re-run matches. Porcelain is empty, the last commit is `0888f0f Fri Oct 16 12:06:47 2026 -0400`, and :18/:20/:69/:94 are all 4/4 verbatim in the artifact. §3 (0)'s quote of :20 is exact. The ":69 and :94 repeat it" parenthetical quotes :94's wording, and :69 ("only "Simulated Data Feed" may be connected") is consistent with it.
3. **o7:** verbatim. The row is 1530 chars, so `cut -c1-1700` shows it whole. HEAD's DECISION_LOG has 59 lines, as o4b pastes (:1069–1070). The root-cause quote at :502 is in the row.
4. **o8:** 135 (`-o`) and 129 (lines) both reproduce. The excluded glob also covers this report's filename.
5. **§3 (iii) sources:** walkthrough :74 and results :46 match the artifact's quotes. "Kept the two connections apart" holds (both name "Simulation" as the accepted row and the Simulated Data Feed as "a row other than").
6. **§3 (i)/"Where it stands now":** the "plus" reading is labelled INFERRED and rests on D-071 "relaxed for this one connection only" and the 10-19 brief :15 "Allowed connections: "Simulated Data Feed" and "Simulation" only". The narrowing claim is labelled INFERRED.
7. **§7 summary line 5 (:769):** every factual clause is labelled REPORTED or INFERRED. "Leaving it off is the only option that changes nothing" agrees with §6 :756.
8. **§8 (a)/(c):** (a)'s added 10-16 rule 1 quote ("no orders, not even on Sim101") is verbatim in o6. (c) is labelled and left to Amear.
9. **§10 M2 (:1056):** E7, E9 and E12 exist in the body (audited :350, :389, :418) and are searches with arms.
10. **Workers list (:1175–1181):** CW1's cut-width exception matches o3a's label (:801). CW4 and the manager-captured o6/o7/o8 match the block headers ("~13:10 EDT", no "re-run" claim).

## Files staged
None. Read-only except this report (untracked, not added).

**Result:** PASS. All of F1–F8 and M-a…M-d are fixed. The attack on the added text found 7 MINOR defects and no MAJOR or BLOCKING one.

VERDICT: PASS
