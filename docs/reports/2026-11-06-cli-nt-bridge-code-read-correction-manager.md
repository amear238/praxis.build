# cli-nt-bridge code read: correction after audit FAIL 1 (manager report, 2026-11-06)

## Task

This is the one allowed correction of unit `2026-11-06-cli-nt-bridge-code-read` after audit FAIL 1 (S1: B1–B3; S2: B4; MINOR M1–M3). The work had three parts:
- APPEND `## Correction 2` to `docs/reports/2026-11-06-cli-nt-bridge-code-read.md` (the main report).
- APPEND `## Correction 1` to `docs/reports/2026-11-06-cli-nt-bridge-code-read-manager.md` (the completion manager report).
- Make the smallest wording fix to MANIFEST rows 240–241, and add row 242 for this report.

Nothing is staged and nothing is committed. Working directory `/Volumes/Sensidine/Praxis.build`, branch main, HEAD `e31b9a4`.

## Authorisation

DECISION_LOG.md row `[2026-11-06T19:43:00Z] WHO: praxis-master` (working tree, line 463). From its WHAT, quoted:

> **UNIT `2026-11-06-cli-nt-bridge-code-read` — AUDIT FAIL 1 (S1: B1, B2, B3; S2: B4); ONE correction dispatched (strike 1 of 2).** […] Correction scope: APPEND `## Correction 2` to the main report (B1: paste the refusal lines with a new K block and fix the citation; B2: four adversaries, by file, with each MAJOR listed and its status — fixed where/when, or fixed now in this correction; B4: positive-controlled grep showing `NtCoreVersion`/`ntVersion`, corrected statement that the bridge reports NT8's build in its status output, grade OBSERVED code / UNVERIFIED on the VM, and note its bearing on item 1 as a pointer, no ruling; M3: swap); APPEND `## Correction 1` to the completion manager report (B3: `ls -lR bridge-work` pasted, a corrected statement of what exists, which MAJORs from ADV1–4 were and were not addressed, and a plain retraction of the false sentences; M1: paste the before-sha from the before-copy); MANIFEST rows 240–241 smallest wording fix to name the corrections and four adversaries. Nothing above any appended section edited.

The main report's Correction 2 pastes the row's identity line as block [P99], and the manager correction pastes it as [R07].

## Rubric criteria addressed (verbatim, specs/SPEC_RUBRIC.md)

- S1 | Every claim in a report has pasted command output, not a description of output.
- S2 | No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure.
- S8 | No question that belongs to Amear is answered on his behalf.

## Workers dispatched

| id | mode | target | outcome |
|---|---|---|---|
| `a831f52c70793a4a4` (praxis-worker) | ADVERSARIAL, read-only | Correction 2 draft (`scratchpad/corr2/c2-draft.md`, 235 lines), before it was inserted | `VERDICT: FAIL`: 2 MAJOR, 5 MINOR, and 13/13 blocks MATCH. The full return is under "Adversarial findings". All seven findings were fixed in the draft before the single insert. |

No other worker ran. The manager captured the evidence itself, using read-only commands through the main report's harness.

## Process log

1. Read the rubric's S1/S2/S8 lines, the authorisation row, the four adversary files, the main report's body lines 1–241 and its Correction 1 (2860–2919), and the completion manager report's lines 17–25 and 549–565.
2. Listed the scratchpad with `ls -lR bridge-work/` (pasted as [R01] in the manager correction). The W1, W2 and W3 notes, `M/`, `P/` and all four ADV files exist. No ADV5 directory exists.
3. Captured the new blocks K05–K11 (clone) and P91–P99 (repo) through the main report's harness `( cd "$D" && LC_ALL=C zsh -f -c "$cmd" )`, written by a scratch runner to `scratchpad/corr2/out/`.
4. Drafted Correction 2 from a template with the blocks spliced in, and dispatched the adversary on that draft.
5. Fixed all seven of the adversary's findings:
   - MAJOR 1: the claim that the repo has no observed value of the VM's build is replaced. The new text lists three REPORTED records [P98][P11] and states that the repo was not searched end to end.
   - MAJOR 2: the MAJOR findings are now printed in full in [P97].
   - MINORs: an exit-code note; "no MAJOR left unfixed" reworded and graded; the heading softened; "byte-identical" graded INFERRED; the authorisation row and the before-hash pasted in [P99]; "pending" graded UNVERIFIED.
   - Also added C2-5, a fix for ADV4's MINOR items 4 and 5, because row 3 of the MAJOR table named them as leftovers.
6. Appended Correction 2 once. Re-ran every block in the appended text from the final file (16/16 MATCH).
7. Drafted the manager Correction 1, appended it once, and re-ran its blocks. R04 failed the re-run because its pasted output contained fence lines. It was replaced, inside the appended section only, with a version that prints none, and the re-run is now 7/7 MATCH (see Verification evidence).
8. Edited MANIFEST rows 240–241 and added row 242.

Deviations from the brief, each disclosed:
- **C2-3, line 167.** The brief's replacement wording, "the repo has no observed value", was written as "This report observes no value of the VM's NT8 build". It is followed by the three REPORTED records the adversary found. As first drafted, the brief's wording was an absence claim with no search behind it, and it was false.
- **C2-4.** The brief and the audit name line 4. The sentence is on line 5 [P91], and the correction says so.
- **C2-5.** Added for two MINOR leftovers (lines 135 and 236). It changes no NEEDS AMEAR question.

## Verification evidence (pasted output only)

**Before: the state at the start of this unit**, before any edit. This was the unit's first command, pasted with its full output. It records a past state, so re-running it now prints the after state; the final-state block below is the re-runnable comparison.
```
$ cd /Volumes/Sensidine/Praxis.build; git rev-parse --short HEAD; grep -n '^| S1 \|^| S2 \|^| S8 ' specs/SPEC_RUBRIC.md | cut -c1-400; M=docs/reports/2026-11-06-cli-nt-bridge-code-read.md; R=docs/reports/2026-11-06-cli-nt-bridge-code-read-manager.md; wc -l $M $R; head -n 2919 $M | shasum -a 256; head -n 565 $R | shasum -a 256; grep -n '2026-11-06T19:43:00Z' DECISION_LOG.md | cut -c1-80; git diff --numstat MANIFEST.md; sed -n '240,242p' MANIFEST.md; git diff --cached --stat | tail -1
e31b9a4
107:| S1 | Every claim in a report has pasted command output, not a description of output. |
108:| S2 | No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure. |
114:| S8 | No question that belongs to Amear is answered on his behalf. |
    2919 docs/reports/2026-11-06-cli-nt-bridge-code-read.md
     565 docs/reports/2026-11-06-cli-nt-bridge-code-read-manager.md
    3484 total
da5f4dbc81a1ff295d9c78f0b3fca390e177d8a87c3ac0ad0ee9e658665b110d  -
2607be2f0323b37fb33254d2b2d7354ae9234b1452f46a3023dee3a12b12234c  -
463:- [2026-11-06T19:43:00Z] WHO: praxis-master | WHAT: **UNIT `2026-11-06-cli-n
2	0	MANIFEST.md
| /docs/reports/2026-11-06-cli-nt-bridge-code-read.md | Report | 2 | 2026-11-06 | Read-only code read of eman007/cli-nt-bridge @ 9664d9b (D-2026-11-06-A item 2, first step): components and file-drop transport, Strategy Analyzer backtest and walk-forward request/response, baseline-setting map with BLOCKER list (exact 1190 / $197327.60 reproduction UNVERIFIED), VM install footprint (AddOn import barred until Amear lifts it), security surface, MIT licence (two holders), maturity, NEEDS AMEAR 1-12; evidence appendix of pasted command blocks; nothing run; ungraded at time of row |
| /docs/reports/2026-11-06-cli-nt-bridge-code-read-manager.md | Report | 2 | 2026-11-06 | Manager report for unit 2026-11-06-cli-nt-bridge-code-read (written by completion unit 2026-11-06-cli-nt-bridge-code-read-completion from on-disk evidence only: sample of 12 appendix blocks re-run, one fresh adversarial pass with its return pasted, Correction 1 appended to the main report); ungraded at time of row |
 12 files changed, 5726 insertions(+), 2 deletions(-)
```

**After: final state.** This block is re-runnable. Lines 1–2919 of the main report and lines 1–565 of the manager report hash the same as before. The main report's appended lines 2920–3200 are byte-equal to the Correction 2 draft, the version with the adversary's findings fixed (`cmp` rc=0):
```
$ cd /Volumes/Sensidine/Praxis.build; head -n 2919 docs/reports/2026-11-06-cli-nt-bridge-code-read.md | shasum -a 256; head -n 565 docs/reports/2026-11-06-cli-nt-bridge-code-read-manager.md | shasum -a 256; wc -l docs/reports/2026-11-06-cli-nt-bridge-code-read.md docs/reports/2026-11-06-cli-nt-bridge-code-read-manager.md; tail -n +2920 docs/reports/2026-11-06-cli-nt-bridge-code-read.md | cmp - /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/corr2/c2-draft.md; echo rc=$?; git diff --numstat MANIFEST.md; git diff --cached --stat | tail -1; git status --short MANIFEST.md docs/reports/2026-11-06-cli-nt-bridge-code-read.md docs/reports/2026-11-06-cli-nt-bridge-code-read-manager.md; git rev-parse --short HEAD
da5f4dbc81a1ff295d9c78f0b3fca390e177d8a87c3ac0ad0ee9e658665b110d  -
2607be2f0323b37fb33254d2b2d7354ae9234b1452f46a3023dee3a12b12234c  -
    3200 docs/reports/2026-11-06-cli-nt-bridge-code-read.md
     739 docs/reports/2026-11-06-cli-nt-bridge-code-read-manager.md
    3939 total
rc=0
3	0	MANIFEST.md
 12 files changed, 5726 insertions(+), 2 deletions(-)
 M MANIFEST.md
?? docs/reports/2026-11-06-cli-nt-bridge-code-read-manager.md
?? docs/reports/2026-11-06-cli-nt-bridge-code-read.md
e31b9a4
```

**Re-run of every block in both appended sections, from the final files.** `rerun_check.py` parses each `[Tag]` block after the given line. It runs the block's `$` line under `zsh -f -c` with `LC_ALL=C`, K blocks from the clone and all others from the repo root, and compares the result byte for byte with the pasted output:
```
$ cd /Volumes/Sensidine/Praxis.build; python3 -I /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/corr2/rerun_check.py docs/reports/2026-11-06-cli-nt-bridge-code-read.md 2919 /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/bridge-src/cli-nt-bridge; python3 -I /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/corr2/rerun_check.py docs/reports/2026-11-06-cli-nt-bridge-code-read-manager.md 565 /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/bridge-src/cli-nt-bridge
K05 MATCH K06 MATCH K07 MATCH K08 MATCH K09 MATCH K10 MATCH K11 MATCH P91 MATCH P92 MATCH P93 MATCH P94 MATCH P95 MATCH P96 MATCH P97 MATCH P98 MATCH P99 MATCH
R01 MATCH R02 MATCH R03 MATCH R04 MATCH R05 MATCH R06 MATCH R07 MATCH
```

On its first run, the checker printed `R04 DIFF` (and a spurious `P01`) for the manager correction. The cause was a real defect. R04 printed `head -n 3` of `M/mgr-run.md` and `P/mgr-run.md`, and that output contains literal code-fence lines, which closed the block early. R04 was replaced inside the appended section with a `head -n 1` version that prints no fences. Lines 1–565 are unaffected (hash above). That is why the manager report is 739 lines, not the 749 it had right after the append.

**Key new evidence**, quoted from the appended blocks (the whole blocks are in the main report's Correction 2):
- [K05]: `1734: … "needs 4 fields Name:min:max:step."`, `1738: … "is not a public property of "`, `1748: … "does not fit "`, `1750: … "must be > 0."`
- [P92]: `refusal-lines-pasted exit=1`. No line among report lines 1–2919 starts with 1733/1734/1737/1738/1747/1748.
- [K06]: `C24-patterns exit=1`, then `addon/NT8BridgeServer.cs:348: … NtCoreVersion()`, `addon/NT8BridgeServer.cs:595: … "ntVersion"…`, `nt8bridge/ntstatus.py:24: … "ntVersion": str`.
- [K09]: `948cb9d5bef0  addon/NT8BridgeServer.cs`, `8fb9566d11f8  README.md`.

**MANIFEST: before and after**:
```
$ cd /Volumes/Sensidine/Praxis.build; diff /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/corr2/MANIFEST-before.md MANIFEST.md; echo rc=$?
240,241c240,242
< | /docs/reports/2026-11-06-cli-nt-bridge-code-read.md | Report | 2 | 2026-11-06 | Read-only code read of eman007/cli-nt-bridge @ 9664d9b (D-2026-11-06-A item 2, first step): components and file-drop transport, Strategy Analyzer backtest and walk-forward request/response, baseline-setting map with BLOCKER list (exact 1190 / $197327.60 reproduction UNVERIFIED), VM install footprint (AddOn import barred until Amear lifts it), security surface, MIT licence (two holders), maturity, NEEDS AMEAR 1-12; evidence appendix of pasted command blocks; nothing run; ungraded at time of row |
< | /docs/reports/2026-11-06-cli-nt-bridge-code-read-manager.md | Report | 2 | 2026-11-06 | Manager report for unit 2026-11-06-cli-nt-bridge-code-read (written by completion unit 2026-11-06-cli-nt-bridge-code-read-completion from on-disk evidence only: sample of 12 appendix blocks re-run, one fresh adversarial pass with its return pasted, Correction 1 appended to the main report); ungraded at time of row |
---
> | /docs/reports/2026-11-06-cli-nt-bridge-code-read.md | Report | 2 | 2026-11-06 | Read-only code read of eman007/cli-nt-bridge @ 9664d9b (D-2026-11-06-A item 2, first step): components and file-drop transport, Strategy Analyzer backtest and walk-forward request/response, baseline-setting map with BLOCKER list (exact 1190 / $197327.60 reproduction UNVERIFIED), VM install footprint (AddOn import barred until Amear lifts it), security surface, MIT licence (two holders), maturity, NEEDS AMEAR 1-12; evidence appendix of pasted command blocks; nothing run; Correction 1 (completion unit) and Correction 2 (after audit FAIL 1) appended; ungraded at time of row |
> | /docs/reports/2026-11-06-cli-nt-bridge-code-read-manager.md | Report | 2 | 2026-11-06 | Manager report for unit 2026-11-06-cli-nt-bridge-code-read (written by completion unit 2026-11-06-cli-nt-bridge-code-read-completion from on-disk evidence only: sample of 12 appendix blocks re-run, one fresh adversarial pass with its return pasted, Correction 1 appended to the main report); its own Correction 1 (after audit FAIL 1) retracts its absence claims and lists the original unit's three capture workers and four adversarial passes; ungraded at time of row |
> | /docs/reports/2026-11-06-cli-nt-bridge-code-read-correction-manager.md | Report | 2 | 2026-11-06 | Manager report for the correction after audit FAIL 1 of unit 2026-11-06-cli-nt-bridge-code-read: Correction 2 appended to the main report (refusal lines 1733-1750 pasted, four adversarial passes with a table of their six MAJOR findings, positive-controlled ntVersion grep, sha-prefix pairing, lines 135/236), Correction 1 appended to the completion manager report (retraction, scratch inventory, before-sha), one adversarial pass with its return pasted; ungraded at time of row |
rc=1
```
`rc=1` is `diff`'s exit when the files differ, which is expected here. Numstat went from `2	0` to `3	0` (the before and final-state blocks above).

## Adversarial findings

Full return of worker `a831f52c70793a4a4`, pasted as returned. It graded the **draft**, before the fixes in Process log step 5.

---
Three things. One, the verdict is FAIL, on two MAJOR findings. Two, all 13 pasted blocks re-run and match exactly. Three, the first fault is the new sentence that says the repo has no observed record of the VM's NT8 build: two repo reports do record one, and they disagree. The second fault is that the MAJOR table quotes the passes from lines its blocks never print.

**Block re-runs** (harness `( cd "$dir" && LC_ALL=C zsh -f -c "$cmd" )`, K blocks from the clone, P blocks from the repo root; output compared with `cmp`):
```
K05 MATCH  K06 MATCH  K07 MATCH  K08 MATCH  K09 MATCH  K10 MATCH  K11 MATCH
P91 MATCH  P92 MATCH  P93 MATCH  P94 MATCH  P95 MATCH  P96 MATCH
```

## Findings

1. **MAJOR — draft line 42: an absence claim with no search, no control and no grade, and it is wrong.** The line says "The repo holds no observed value of the VM's NT8 build." No block searches the repo. The repo has two records written from inside the VM, and they disagree:
```
$ awk 'NR==3' docs/reports/2026-11-02-vm-high-res-plan.md | cut -c1-200; awk 'NR==60' docs/reports/2026-10-19-windows-vm-state-update-2-from-migration.md | cut -c1-330
Written by Claude Code on the VM (VMware, Windows 11 ARM64, NinjaTrader 8.1.8.4) under Amear's ruling R-VN3-2. **Plan only.** ...
| 4 | NT8 8.1.7.2 from the saved MSI; sign in; new Machine ID | **Installed and signed in. Machine ID not recorded** | Install REPORTED (in-VM agent read the MsiInstaller events: 8.1.7.2, status 0, 2026-10-19 13:03Z). ... Version in Help > About: not read.
```
   Both are REPORTED BY an in-VM agent, not Amear. The line leaves them out and presents Amear's 8.1.8.4 as the only source. The two values bear on NEEDS AMEAR 6. Breaks S1 and the rule that every absence claim needs a positive control.

2. **MAJOR — draft line 17 and table lines 23–28: the passes' findings are quoted from lines no block prints.** Line 17 says the "MAJOR lines are as printed in [P94]". For ADV3, P94 prints only the verdict line, because ADV3's two findings start `M1`/`M2` and never contain the word "MAJOR":
```
$ /usr/bin/grep -n 'MAJOR' $W/ADV3/findings.md
2:VERDICT: FAIL (2 MAJOR, 5 MINOR)
$ /usr/bin/grep -n '^M[12] ' $W/ADV3/findings.md | cut -c1-120
3:M1 Summary:30 + Q3:132 "only/exactly two settable properties" (OBSERVED code). P16 greps only declared one-line auto-p
7:M2 Q2:79-80 the quote "1692: ... needs opt=..." has no path:line@sha, and the clause before it attributes it to the Py
```
   - Row 4 (ADV3 M2) has no pasted support at all.
   - Row 3 has only P95's `exactly two settable`.
   - P94 cuts every other MAJOR line at 150 characters. So no block prints these quoted parts:
     - Row 1: "one-value range passes" and "prescribes a method".
     - Row 2: `opt=","` and "passes the AddOn".
     - Row 6: "C24 is blind to the bridge's own version read".

   The wording is accurate: I found it in the files (`ADV/NOTES.md:Contracts:1:1:1`, `ADV/NOTES.md:prescribes method`, `ADV2/findings.md:opt=","`, `ADV4/...:blind to the relevant code`). It still breaks S1.

3. **MINOR — draft lines 23 and 32: the "control exit 0" values are the exit codes of `cut` and `sed`, not of `grep`.** This affects K06 `control exit=$?`, K08 `exit=$?` and P95 `control-on-ADV-files exit=$?`. Each one prints 0 even when grep finds nothing:
```
$ LC_ALL=C zsh -f -c '/usr/bin/grep -n NoSuchStringXYZ /etc/hosts | cut -c1-200; echo "control exit=$?"; /usr/bin/grep -o NoSuchStringXYZ /etc/hosts | sed s/a/b/; echo "control-on-ADV-files exit=$?"'
control exit=0
control-on-ADV-files exit=0
```
   The conclusions still stand, because the matched lines are printed. The absence exits (in P92, P95 and C24) are grep's own, so those are correct.

4. **MINOR — draft line 30: "No MAJOR finding is left unfixed."** The sentence has no grade, and it claims more than the evidence. "Reflected in the body" only means the wording changed. Row 3 itself admits leftovers: ADV4 item 5 says line 236 still says "are not properties of the committed strategy", which is the same overreach. Two small faults in the same line: "and Under its" is a typo, and the INFERRED basis gives no time for when the report was edited.

5. **MINOR — draft line 8: the heading "'one adversarial worker' is wrong" is stronger than its evidence.** P94 shows four files, not four workers. The corrected wording rightly says "passes". No block shows that all four passes "read the clone under the same limits" (line 17).

6. **MINOR — draft line 46 (C2-4).** "byte-identical" is graded OBSERVED, but it rests on matching 12-hex-character prefixes, so it is INFERRED. "The audit names this line 4" cites no block and carries no grade.

7. **MINOR — draft lines 4 and 44: claims with no grade and no block.**
   - "Every line above this heading is unchanged" has no hash or diff behind it.
   - The authorisation row is not pasted. I checked: it exists at DECISION_LOG.md:463.
   - "which is still pending" was not re-checked now.

## What held
- All 13 blocks match exactly (above).
- **C2-1.** K05 prints all four refusal paths. P92's absence result holds: in the whole report, `1733`/`1737`/`1747` appear only on line 81. The fields come from `part.Split(':')` at :1732, which matches "four fields".
- **C24.** K06 runs exactly C24's patterns, and P93 runs exactly P13's command.
- **K11.** The INFERRED claim that :595 sits inside `RunNtStatus` holds. Lines 512–594 contain no closing brace at 8-space indentation (0) and no tab-led lines (0).
- **K08.** The `CurrentVersion` substring reading is correct.
- **MINOR counts.** 8, 8, 5 and 7 are correct, and they sum to 28.
- **MAJOR table.** It is complete: 6 rows for 1+1+2+2 findings. Every "Reflected"/"NOT reflected" status matches P95, P92 and P96.
- **De-identification.** "breaker" appears nowhere in the draft (grep exit 1). The same grep finds 38 lines in DECISIONS.md (exit 0), so the search works.
- **S8.** No question is answered for Amear. D-2026-11-06-A item 1 is only pointed to. Lines 43–44 sit near a method suggestion, but they carry an explicit "pointer only" disclaimer.

Nothing was written. The notes directory holds only re-run scratch files, under `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/corr2/adv/`.

VERDICT: FAIL

---

**How each finding was dispositioned.** Each fix is in the appended Correction 2, and its blocks re-run 16/16 MATCH (above):

| # | Disposition |
|---|---|
| 1 MAJOR | Fixed. Line 167's replacement now lists the 2026-10-19 (8.1.7.2 install, Help > About not read), 2026-10-31 (Amear, 8.1.8.4) and 2026-11-02 (8.1.8.4 header) records as REPORTED [P98][P11]. It states that no end-to-end repo search was done (UNVERIFIED), and it is framed as "This report observes no value". |
| 2 MAJOR | Fixed. New block [P97] prints every MAJOR finding line in full (ADV:3, ADV2:3, ADV3:3–8, ADV4:8–9). The table column is headed "MAJOR finding [P97]" and is marked as a paraphrase, REPORTED BY that pass. |
| 3 | Fixed. A note on exit codes names K06, K08 and P95. The prose no longer cites "control exit 0". |
| 4 | Fixed. The sentence is reworded and graded. ADV4 items 4 and 5 are fixed in the new C2-5. The typo is gone. The INFERRED basis is now only [P96]. |
| 5 | Fixed. The heading now says "count one adversarial worker; four adversarial passes are on file". "Same limits" is graded REPORTED BY the original manager. The W1–W3 notes are listed in [P97]. |
| 6 | Fixed. Byte-identity is graded INFERRED. "M3 line 4" is pasted from the audit row in [P99]. |
| 7 | Fixed. [P99] pastes the authorisation row and the hash of lines 1–2919. "Pending" is graded UNVERIFIED. |

The fixed text was **not** re-attacked by a second worker; the brief allowed one adversary. Every fixed sentence cites a block that re-runs MATCH from the final file.

## S6 cross-block check

The three deviations above (line-167 wording, the line-5 location, C2-5) were checked against the parts of the reports they touch:
- **Line 167 and the new C2-3 text.** It touches NEEDS AMEAR 6 and D-2026-11-06-A item 1. It names both only as pointers: "This report does not say how item 1 should be done, and NEEDS AMEAR 6 stays a question for Amear." It adds no question and answers none (S8).
- **C2-5.** It touches NEEDS AMEAR 12. It says "The question in NEEDS AMEAR 12 is unchanged and stays Amear's", and it matches the wording of line 135 (`declares two inputs`, [P95]).
- **The two appended sections agree with each other.** The manager correction's [R01] times (ADV 13:59, ADV2 14:06, ADV3 14:12, ADV4 14:19) equal Correction 2's [P94] times. Its [R06] status summary reproduces Correction 2's six table rows.
- **The MANIFEST rows** name the corrections that now exist in both reports.
- **De-identification.** The word "breaker" appears in neither appended section. The adversary checked the Correction 2 draft and found it absent there, with a positive control. The manager correction contains no such text.

## Files staged

None. This unit made no `git add` and no index change. The index is unchanged from the start of the unit:
```
$ git diff --cached --stat | tail -1
 12 files changed, 5726 insertions(+), 2 deletions(-)
```
Changes left unstaged in the working tree:
- `docs/reports/2026-11-06-cli-nt-bridge-code-read.md` (untracked; Correction 2 appended, lines 2920–3200)
- `docs/reports/2026-11-06-cli-nt-bridge-code-read-manager.md` (untracked; Correction 1 appended, lines 566–739)
- `MANIFEST.md` (rows 240–241 reworded, row 242 added; numstat 3/0 vs HEAD)
- this report (new, untracked)

Standing limitation for the baseline figures the main report discusses: Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## Result

This is my grade of the correction, not an audit. The four blocking findings and the three MINOR findings are each addressed in an appended section, with blocks that re-run byte for byte from the final files: B1 (C2-1), B2 (C2-2), B3 (manager Correction 1), B4 (C2-3), M1 ([R02]), M2 (MANIFEST row 240) and M3 (C2-4). The text above each appended section hashes the same before and after. Every finding from the single adversarial pass was fixed. The fixed text was not re-attacked.

**Result: PASS**
