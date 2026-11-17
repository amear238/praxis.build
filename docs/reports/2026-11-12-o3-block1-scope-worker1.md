# 2026-11-12 — O3 Block 1 milestone scope — ADVERSARIAL worker 1 report

## Task
Mode: ADVERSARIAL, read-only re-check. Working directory /Volumes/Sensidine/Praxis.build, branch main, HEAD a411e17. Artifacts under test: entry D-2026-11-12-C appended to DECISIONS.md (working tree, claimed lines 2371–2387), the three new MANIFEST.md rows at the end, and the manager report docs/reports/2026-11-12-o3-block1-scope-manager.md (its "Adversarial findings" section and Result line declared pending). Criterion: rubric O3 (specs/SPEC_RUBRIC.md "## OPEN — gradeable now", "### O3 — Block-1 milestone scope statement"), plus standing S1, S2, S6, S13. No file was staged or edited other than this report.

## Checks run
1. Every double-quoted string in the entry against the HEAD source at the cited line; every cited line number.
2. S2 level and no-design-choice reading of the entry.
3. Parked D-2026-11-12-B block (lines 2279–2370) and HEAD prefix (lines 1–2278) byte-unchanged; diff has zero removed lines.
4. Line-range arithmetic for 2371–2387 and the blank separator.
5. MANIFEST rows: last 3 are this unit's, no row removed, DECISIONS.md row cites by id only.
6. Evidence rules on the manager report and this report.
7. De-identification on the unit's added lines, all added lines in DECISIONS.md and MANIFEST.md, the manager report and this report.

## Verification evidence (command output)

All commands were run inside one `/bin/bash -c` call per block from /Volumes/Sensidine/Praxis.build. Each block shows the literal lines and their full output. [Correction 1 label: the first sentence is a process record of worker1's run, not reproducible now and not claimed as evidence.]

### Report absent before writing; HEAD; line counts; the entry in context (checks 3, 4)
```
$ test -e docs/reports/2026-11-12-o3-block1-scope-worker1.md && echo REPORT_EXISTS || echo report-absent
report-absent
$ git rev-parse --short HEAD
a411e17
$ wc -l DECISIONS.md; git show HEAD:DECISIONS.md | wc -l
    2387 DECISIONS.md
    2278
$ echo "--- 2365-2390 ---"; sed -n "2365,2390p" DECISIONS.md | cat -n
--- 2365-2390 ---
     1	- No resolution of the 2A/2S conflicts with amended #4; no breaker text or value is changed; no strategy rule is changed.
     2	- Nothing is bought; no D2 item is decided.
     3	- Nothing merges from `r6/announcement-research` to `main`.
     4	- Design OPEN-2 is not closed; the A14 overlay priority (design :117) and O4 parity (design :116) stay open.
     5	
     6	[the S13 sentence, filtered] [Correction 1 label: this output line was altered after the run by the fix worker; see :271–273.]
     7	
     8	## 2026-11-12 — D-2026-11-12-C: Block 1 milestone scope — internal path only (rubric O3; master under D-2026-11-08-D D1)
     9	
    10	**Status:** Decided by master under D-2026-11-08-D D1 (DECISION_LOG 2026-11-12T17:31Z), changeable by Amear. Not Amear's ruling. A scope record only.
    11	
    12	**Scope line (rubric O3).** The Block 1 milestone signed off on 2026-07-15 covers the internal path only: the locally driven path that D-2026-07-09-D names, test webhook posts through "webhook → local n8n → JSON file drop into the signals dir → Parallels VM share → NT8 FileSystemWatcher → sim bracket order"; public TradingView ingress (Deviation G, D-2026-07-09-D) was "deferred to pre-live (Block 4–5)" and is untested (rubric O3).
    13	
    14	**Sources (DECISIONS.md at a411e17).**
    15	- D-2026-07-09-D, heading at :133 ("n8n Runs LOCALLY on the Mac for Block-1 Build-First; Public-Ingress Topology Deferred to Pre-Live"); the path and the deferral are in its **Decision:** paragraph at :140.
    16	- The sign-off, heading "## 2026-07-15 — Block 1 milestone — trader sign-off" at :174, body at :175; the body records B1-a as "verified-as-DEFERRED (D-2026-07-09-D)".
    17	- Rubric O3, `specs/SPEC_RUBRIC.md` "## OPEN — gradeable now", "### O3 — Block-1 milestone scope statement".
    18	
    19	**Limits.** This entry records scope only. It makes no design choice, adds no test, and does not re-open or re-grade the 2026-07-15 sign-off. It does not change rubric O3's state; that move is a later master step. It does not decide where public ingress goes. Cross-reference only: `docs/specs/2026-11-10-live-signal-topology.md` (D-2026-11-10-B) :112 already says Deviation G's ingress question leaves the anchor's live path; this entry adds nothing to it.
    20	
    21	**S6 cross-block.** Touches Block 1 (states the reach of the sign-off; its basis and evidence are unchanged), Block 4 and Block 5 (where D-2026-07-09-D places the deferred ingress question; nothing is moved or decided there) and rubric F1 / the live-signal topology (:112, cross-reference only). Conflicts with none: it restates the split D-2026-07-09-D already makes between the local path and the deferred ingress, and the sign-off itself cites D-2026-07-09-D for B1-a. Evidence: `docs/reports/2026-11-12-o3-block1-scope-manager.md` (S6 section).
    22	
    23	[the S13 sentence, filtered] [Correction 1 label: this output line was altered after the run by the fix worker; see :271–273.]
```
Window line 7 is file line 2371 (blank), window line 8 is 2372 (heading), window line 23 is 2387 (S13 sentence, last line of the file). Entry length 17 lines including the separator, under 40.

### Quotes and cited lines against HEAD (check 1)
```
$ H() { git show HEAD:DECISIONS.md | sed -n "$1p"; }
$ echo "--- :133 ---"; H 133
--- :133 ---
## D-2026-07-09-D — n8n Runs LOCALLY on the Mac for Block-1 Build-First; Public-Ingress Topology Deferred to Pre-Live
$ echo "--- :140 ---"; H 140
--- :140 ---
For Block-1 build-first (sim data), **n8n runs locally on the Mac**, not on a remote internet-facing VPS. The signal path is built and proven end-to-end using **test webhook posts** driven locally (as Step 0.8 did against `/tmp`): webhook → local n8n → JSON file drop into the signals dir → Parallels VM share → NT8 FileSystemWatcher → sim bracket order. The question of how live TradingView (public internet) signals reach the system — **rent a VPS + WireGuard** vs **a tunnel relay (e.g. Cloudflare Tunnel)** — is **deferred to pre-live (Block 4–5)** when live signal ingress is actually exercised.
$ echo "--- :174 ---"; H 174
--- :174 ---
## 2026-07-15 — Block 1 milestone — trader sign-off
$ echo "--- :175 ---"; H 175
--- :175 ---
Block 1 (Foundation, build-first) milestone SIGNED OFF by Amear, 2026-07-15, in-session (AskUserQuestion record) + Google Sheets row (clipboard-delivered). Basis: independent evidence audit docs/reports/2026-07-15-block1-milestone-audit.md (commit d405125) — B1-0/b/c/d/e/f VERIFIED, B1-a verified-as-DEFERRED (D-2026-07-09-D), B1-f T1-T4 all PASS with the standing bracket TRADER-CONFIRMED in the NT8 GUI. Known-open items carried into Block 2 with eyes open: btb P2 (trader chose post-milestone, next-session dispatch), 10i P2, 518/01h/qxd P3, 6h7 P4. Block 2 (Backtesting) entry condition now satisfied.
$ echo "=== quote checks (line-specific, fixed string) ==="
$ for spec in "133|n8n Runs LOCALLY on the Mac for Block-1 Build-First; Public-Ingress Topology Deferred to Pre-Live" "140|webhook → local n8n → JSON file drop into the signals dir → Parallels VM share → NT8 FileSystemWatcher → sim bracket order" "140|deferred to pre-live (Block 4–5)" "174|## 2026-07-15 — Block 1 milestone — trader sign-off" "175|verified-as-DEFERRED (D-2026-07-09-D)"; do
 n=${spec%%|*}; q=${spec#*|}; c=$(H $n | /usr/bin/grep -c -F -- "$q"); a=$(git show HEAD:DECISIONS.md | /usr/bin/grep -n -F -- "$q" | cut -d: -f1 | tr "\n" ","); echo "line $n count=$c all-lines=$a :: $q"; done
=== quote checks (line-specific, fixed string) ===
line 133 count=1 all-lines=133, :: n8n Runs LOCALLY on the Mac for Block-1 Build-First; Public-Ingress Topology Deferred to Pre-Live
line 140 count=1 all-lines=140, :: webhook → local n8n → JSON file drop into the signals dir → Parallels VM share → NT8 FileSystemWatcher → sim bracket order
line 140 count=1 all-lines=140, :: deferred to pre-live (Block 4–5)
line 174 count=1 all-lines=174, :: ## 2026-07-15 — Block 1 milestone — trader sign-off
line 175 count=1 all-lines=175, :: verified-as-DEFERRED (D-2026-07-09-D)
$ echo "=== :140 Decision label ==="; H 140 | /usr/bin/grep -c -F "**Decision:**"
=== :140 Decision label ===
0
$ echo "=== rubric ==="; git show HEAD:specs/SPEC_RUBRIC.md | /usr/bin/grep -n -F -e "## OPEN — gradeable now" -e "### O3 — Block-1 milestone scope statement"
=== rubric ===
99:## OPEN — gradeable now
109:### O3 — Block-1 milestone scope statement
$ git show HEAD:specs/SPEC_RUBRIC.md | /usr/bin/grep -n -A4 -F "### O3 — Block-1 milestone scope statement"
109:### O3 — Block-1 milestone scope statement
110-Block 1 was signed off as the signal path proven end-to-end. Deviation G defers
111-public ingress to Blocks 4–5, untested. **Required:** one line in DECISIONS.md
112-recording that the Block 1 milestone covers the internal path only.
113-
$ echo "=== topology :112 ==="; git show HEAD:docs/specs/2026-11-10-live-signal-topology.md | sed -n "112p"
=== topology :112 ===
This topology touches: Block 1 (the emitter changes from TradingView to NT8; the TESTED pipe is reused; Deviation G's ingress question leaves the anchor's live path); Block 2 (the emitter must reproduce the backtest strategy's decisions, so O4 parity now also covers emitter-vs-backtest equality); Block 3 (all nine breakers, Redis, PostgreSQL, the fallback script); Block 4 (the paper pass on MFFU sim runs on this path, D8(8)); Block 5 (live, D2(b)); Deviation A (strategy logic in NinjaScript, kept; now also the emitter); Deviation C (reversals are entries for #2, bead `Praxis_build-yra`); Deviation G (D-2026-07-09-D); D-2026-11-10-A (bypass B1); rubric F2 (the flat time and session boundary for #4/#5); rubric F4 (MFFU automation, FROZEN); rubric O2 (`praxispush`); rubric O4 (parity); the SHM thresholds that F1 blocks (`specs/SPEC_RUBRIC.md`:30).
$ git show HEAD:docs/specs/2026-11-10-live-signal-topology.md | /usr/bin/grep -c -F "D-2026-11-10-B"
0
$ echo "=== untested in O3/HEAD DECISIONS ==="; git show HEAD:specs/SPEC_RUBRIC.md | /usr/bin/grep -n -F "untested" | /usr/bin/grep -n -F "Deviation G"
=== untested in O3/HEAD DECISIONS ===
```
The last pipeline printed nothing [Correction 1: "(exit 1)" removed, the exit status was not pasted; see "Correction 1 evidence" for the count 0 and the topology :112 check] because "Deviation G" is at rubric :110 and "untested" at :111; the -A4 output above shows both. Topology :112 also names "Deviation G (D-2026-07-09-D)", which sources the Deviation G = D-2026-07-09-D equation.

### Decision label, topology id link, hashes and ranges (checks 1, 3, 4)
```
$ echo "--- HEAD 134-141 ---"; git show HEAD:DECISIONS.md | sed -n "134,141p" | cut -c1-80 | cat -n
--- HEAD 134-141 ---
     1	
     2	**Date:** 2026-07-09
     3	**Status:** LOCKED (trader-chosen 2026-07-09)
     4	**Supersedes the timing/premise of:** D-2026-07-09-A (WireGuard tunnel) and the 
     5	
     6	**Decision:**
     7	For Block-1 build-first (sim data), **n8n runs locally on the Mac**, not on a re
     8	
$ echo "--- Decision label lines in HEAD 133-160 ---"; git show HEAD:DECISIONS.md | sed -n "133,160p" | /usr/bin/grep -n -F "**Decision" | cut -c1-60
--- Decision label lines in HEAD 133-160 ---
7:**Decision:**
$ echo "--- D-2026-11-10-B headings ---"; git show HEAD:DECISIONS.md | /usr/bin/grep -n -F "D-2026-11-10-B" | /usr/bin/grep -F "##" | cut -c1-200
--- D-2026-11-10-B headings ---
2047:## 2026-11-10 — D-2026-11-10-B: live-signal topology adopted as the working design (rubric F1; bead Praxis_build-1hv)
$ echo "--- topology doc mentions decision id? ---"; git show HEAD:docs/specs/2026-11-10-live-signal-topology.md | /usr/bin/grep -n -o "D-2026-11-10-[A-Z]" | sort | uniq -c
--- topology doc mentions decision id? ---
   1 112:D-2026-11-10-A
   3 189:D-2026-11-10-A
   1 217:D-2026-11-10-A
   2 26:D-2026-11-10-A
   3 86:D-2026-11-10-A
$ echo "=== check 3 ==="
=== check 3 ===
$ sed -n "2279,2370p" DECISIONS.md | shasum -a 256
ad933a6cdf59492a0f4a79ff2951da96978b0321a738b4d938eee2a6fcd23093  -
$ head -n 2278 DECISIONS.md | shasum -a 256
a258d9d8e6c33a652b11d9635dd3b4490f56c4586d92607a52361a549707c039  -
$ git show HEAD:DECISIONS.md | shasum -a 256
a258d9d8e6c33a652b11d9635dd3b4490f56c4586d92607a52361a549707c039  -
$ git diff HEAD --numstat -- DECISIONS.md
109	0	DECISIONS.md
$ git diff HEAD -- DECISIONS.md | /usr/bin/grep -c "^-[^-]"
0
$ git diff HEAD -- DECISIONS.md | /usr/bin/grep "^@@"
@@ -2276,3 +2276,112 @@ This entry names the governing rule (Rule F2-1) and the 15:00 disposition, and r
$ echo "=== check 4 ==="
=== check 4 ===
$ (git show HEAD:DECISIONS.md; sed -n "2371,2387p" DECISIONS.md) | wc -l
    2295
$ sed -n "2371,2387p" DECISIONS.md | shasum -a 256
7d8f6577dfe6e75fdeb42158ff33e1e3ab29da864d839f16c918360132ed0653  -
$ sed -n "2370p" DECISIONS.md | cut -c1-40; echo "2371=[$(sed -n 2371p DECISIONS.md)]"; sed -n "2372p" DECISIONS.md | cut -c1-40
Fills are optimistic; Standard resolutio
2371=[]
## 2026-11-12 — D-2026-11-12-C: Block 1 
$ tail -c 1 DECISIONS.md | xxd
00000000: 0a                                       .
$ sed -n "2371,2387p" DECISIONS.md | wc -l
      17
```
Arithmetic: 2278 (HEAD) + 92 (parked 2279–2370) + 17 (2371–2387) = 2387 = file length; numstat 109 added = 92 + 17, 0 removed. Line 2370 is the parked block's S13 sentence and line 2371 is empty, so the separator is needed and present; line 2387 ends the file with one newline. The range holds nothing of the parked block (2370 excluded) and nothing of the entry is outside it (file ends at 2387). The shas match the manager report's claimed pre-edit and HEAD values and its 7d8f6577 range hash.

### MANIFEST (check 5)
```
$ git diff HEAD --numstat -- MANIFEST.md
17	0	MANIFEST.md
$ git diff HEAD -- MANIFEST.md | /usr/bin/grep -c "^-[^-]"
0
$ git diff HEAD -- MANIFEST.md | /usr/bin/grep "^@@"
@@ -304,6 +304,14 @@
@@ -429,6 +437,12 @@
@@ -442,3 +456,6 @@
$ wc -l MANIFEST.md; git show HEAD:MANIFEST.md | wc -l
     461 MANIFEST.md
     444
$ git show HEAD:MANIFEST.md | shasum -a 256; head -n $(git show HEAD:MANIFEST.md | wc -l) MANIFEST.md | shasum -a 256
e7bb6bf662ffc9b3369712995cf601d3d7397e000050c6da5354945bf8d9ea87  -
c830ab53557efc76de3f45ad861758b0c4da91ea3f2c9ab8901ea3fdafd73edb  -
$ echo "--- last 3 rows ---"; tail -n 3 MANIFEST.md
--- last 3 rows ---
| /DECISIONS.md | Log | 3 | 2026-11-12 | AMENDMENT ROW (append-only registry). Unit 2026-11-12-o3-block1-scope (rubric O3; master under D-2026-11-08-D D1, DECISION_LOG 2026-11-12T17:31:00Z): appends entry D-2026-11-12-C, "Block 1 milestone scope — internal path only", recording that the Block 1 milestone signed off on 2026-07-15 covers the internal path only and that public TradingView ingress (Deviation G, D-2026-07-09-D) is deferred and untested. Scope record only: no design choice, no test, no re-grade of the sign-off, rubric O3 state unchanged. |
| /docs/reports/2026-11-12-o3-block1-scope-manager.md | Report | 3 | 2026-11-12 | Manager report for unit 2026-11-12-o3-block1-scope (rubric O3; master under D-2026-11-08-D D1): filing of DECISIONS.md entry D-2026-11-12-C, S4 pre-check, HEAD source quote checks, committed-blob line arithmetic and sha256, parked-entry byte-identity check, S6 cross-block check, de-identification scan. |
| /docs/reports/2026-11-12-o3-block1-scope-worker1.md | Report | 3 | 2026-11-12 | ADVERSARIAL worker 1 report for unit 2026-11-12-o3-block1-scope: independent read-only re-check of entry D-2026-11-12-C quotes against HEAD sources, no-design-choice and S2 level check, parked-entry byte-identity, line-range arithmetic, evidence rules on both unit reports. |
$ echo "--- row 4th from end (prior parked) ---"; tail -n 4 MANIFEST.md | head -n 1 | cut -c1-160
--- row 4th from end (prior parked) ---
| /docs/reports/2026-11-12-fgd-part-b-worker2.md | Report | 3 | 2026-11-12 | BUILD fix worker 2 report for unit 2026-11-12-fgd-part-b: de-identification and tru
```
The head-444 hash differs from HEAD's because the 14 parked rows are inserted inside the file (hunks at 304 and 429, 8 + 6 lines), not appended; the last hunk adds exactly 3 rows. Zero lines removed, so no HEAD row is removed or changed. Limit: no pre-edit hash of the 14 parked rows was claimed, so this check shows they were not removed and their count is 14; it does not show they are byte-identical to their pre-edit state. The DECISIONS.md row cites D-2026-11-12-C by id; the only numbers in it are dates and the DECISION_LOG timestamp, no line numbers.

### DECISION_LOG row and email re-count
```
$ /usr/bin/grep -n -F "2026-11-12T17:31" DECISION_LOG.md | cut -c1-220
879:- [2026-11-12T17:31:00Z] WHO: praxis-master | WHAT: **Unit 2 dispatched: rubric O3, Block 1 milestone scope statement.** Rubric O3 (re-read this run, `specs/SPEC_RUBRIC.md` "## OPEN — gradeable now"): "Block 1 was si
$ for f in /tmp/w1-dec-all.txt /tmp/w1-dec-unit.txt /tmp/w1-man-all.txt /tmp/w1-man-unit.txt docs/reports/2026-11-12-o3-block1-scope-manager.md; do echo "$f email=$(/usr/bin/grep -c -E "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+[.][A-Za-z]+" $f)"; done
/tmp/w1-dec-all.txt email=0
/tmp/w1-dec-unit.txt email=0
/tmp/w1-man-all.txt email=0
/tmp/w1-man-unit.txt email=0
docs/reports/2026-11-12-o3-block1-scope-manager.md email=0
$ echo "Decision label line:"; git show HEAD:DECISIONS.md | /usr/bin/grep -n -x -F "**Decision:**" | /usr/bin/awk -F: "\$1>=133 && \$1<=160"
Decision label line:
139:**Decision:**
```

### Scans (checks 6, 7)
Run before this block and the S13 line were inserted; the inserted text is commands and counts only. [Correction 1 label: process record of worker1's run, not reproducible now and not claimed as evidence.]
```
$ M=docs/reports/2026-11-12-o3-block1-scope-manager.md; R=docs/reports/2026-11-12-o3-block1-scope-worker1.md; E=$(printf "\342\200\246")
$ git diff HEAD -U0 -- DECISIONS.md | /usr/bin/grep "^+[^+]" | sed "s/^+//" > /tmp/w1-dec-all.txt
$ sed -n 2371,2387p DECISIONS.md > /tmp/w1-dec-unit.txt
$ git diff HEAD -U0 -- MANIFEST.md | /usr/bin/grep "^+[^+]" | sed "s/^+//" > /tmp/w1-man-all.txt
$ tail -n 3 MANIFEST.md > /tmp/w1-man-unit.txt
$ for f in /tmp/w1-dec-all.txt /tmp/w1-dec-unit.txt /tmp/w1-man-all.txt /tmp/w1-man-unit.txt $M $R; do
 echo "$f lines=$(wc -l < $f | tr -d " ")"
 echo "  email=$(/usr/bin/grep -c -E "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+[.][A-Za-z]+" $f)"
 echo "  rep=$(/usr/bin/grep -c -i -F -f /tmp/o3-rep-name.txt $f)"
 echo "  med=$(/usr/bin/grep -c -i -F -f /tmp/o3-med-words.txt $f)"
 echo "  banned=$(/usr/bin/grep -c -i -F -f /tmp/o3-banned-words.txt $f)"; done
/tmp/w1-dec-all.txt lines=72
  email=0
  rep=0
  med=0
  banned=0
/tmp/w1-dec-unit.txt lines=17
  email=0
  rep=0
  med=0
  banned=0
/tmp/w1-man-all.txt lines=17
  email=0
  rep=0
  med=0
  banned=0
/tmp/w1-man-unit.txt lines=3
  email=0
  rep=0
  med=0
  banned=0
docs/reports/2026-11-12-o3-block1-scope-manager.md lines=178
  email=0
  rep=0
  med=0
  banned=0
docs/reports/2026-11-12-o3-block1-scope-worker1.md lines=220
  email=0
  rep=0
  med=0
  banned=0
$ cat /tmp/w1-dec-unit.txt /tmp/w1-man-unit.txt $M | /usr/bin/grep -o -E "\b[A-Z][A-Za-z]+\b" | sort -u | /usr/bin/grep -v -i -F -f /tmp/o3-rep-name.txt | /usr/bin/grep -v -i -F -f /tmp/o3-med-words.txt | tr "\n" " "; echo
ADVERSARIAL AMENDMENT Adversarial Amear Append Block Blocks Both Build Conflicts Cross DECISIONS DEFERRED De Decided Decision Deferred Deviation Disposition Evidence FileSystemWatcher Files Fills First Foundation HEAD Ingress It JSON LOCALLY Limits Line Live Log MANIFEST Mac Manager Master Negative No None Not Nothing OFF OPEN PENDING PNG Parallels Parked Pre Process Public Quotes ROW Report Required Result Rubric Rule Runs Scope Sources Standard Standing Status Task The This Topology Touches TradingView Unit VM Verification Workers Working Za 
$ cat /tmp/w1-dec-unit.txt /tmp/w1-man-unit.txt $M | /usr/bin/grep -o -E "\b[A-Z][A-Za-z]+\b" | sort -u > /tmp/w1-tok-base.txt
$ /usr/bin/grep -o -E "\b[A-Z][A-Za-z]+\b" $R | sort -u | /usr/bin/comm -23 - /tmp/w1-tok-base.txt | /usr/bin/grep -v -i -F -f /tmp/o3-rep-name.txt | /usr/bin/grep -v -i -F -f /tmp/o3-med-words.txt | tr "\n" " "; echo
All Arithmetic Artifacts AskUserQuestion BUILD Backtesting Basis CONFIRMED Checks Cloudflare Criterion Date Defects Design Each Entry Every FAIL FROZEN Findings For GUI Google Known LOCKED Limit MFFU Mode NinjaScript Observations PASS PostgreSQL Praxis Redis SHM Same Scans Sensidine Sheets Step Supersedes TESTED TRADER Timestamp Tunnel VERIFIED VPS Volumes WHAT WHO Window WireGuard Zero 
$ for f in $M $R; do
 echo "== $f"
 echo "  three-dot=$(/usr/bin/grep -c -E "[.]{3}" $f) ellipsis=$(/usr/bin/grep -c -F "$E" $f) angle=$(/usr/bin/grep -c -E "<[a-z_ -]+>" $f)"
 echo "  listing-cmds=$(/usr/bin/grep -c -E "git[ ]status|diff[ ]--name-only|diff[ ]--cached[ ]--name-only|ls[ ].*reports/[e]vidence" $f)"
 echo "  s13=$(/usr/bin/grep -c -x -F -f /tmp/s13.txt $f) result-lines=$(/usr/bin/grep -c "^Result:" $f) evidence-section=$(/usr/bin/grep -c -x -F "## Verification evidence (command output)" $f)"
 /usr/bin/grep -n -F -e "(filled below)" -e "(report scans below)" $f | /usr/bin/grep -v -F "Evidence:"; done
== docs/reports/2026-11-12-o3-block1-scope-manager.md
  three-dot=0 ellipsis=0 angle=0
  listing-cmds=0
  s13=0 result-lines=1 evidence-section=1
11:(filled below)
14:(filled below)
163:(report scans below)
166:(filled below)
== docs/reports/2026-11-12-o3-block1-scope-worker1.md
  three-dot=0 ellipsis=0 angle=0
  listing-cmds=0
  s13=0 result-lines=1 evidence-section=1
```
Person names: every capitalised token above is a word, product, acronym or path part; the only person name is Amear. The first token list is the one from the scan call of the same session (unit DECISIONS and MANIFEST lines plus the manager report). The five /tmp/w1-* setup lines ran in an earlier call of this session and the files were reused. [Correction 1 label: the second and third sentences are process records of worker1's run, not reproducible now and not claimed as evidence.] The manager report's s13=0 is noted only; this report's s13=0 is before the S13 line was appended.

### Fix note (S13 filter)

Lines 35 and 52 of this file (inside the pasted numbered listings of the DECISIONS.md entry) held the S13 sentence. A fix worker replaced that text after the fact with the marker `[the S13 sentence, filtered]`, keeping the line-number prefix so each listing stays line-aligned. The underlying listings were not re-run; the rest of each listing is as first pasted.

Output of the two checks, run after the edit (final run): [Correction 1 label: this run predates correction 1, which edited lines and inserted 21 lines in this file; the S13 sentence is still the last line; the count-only re-run is under "Correction 1 evidence, round 2".]

```
$ grep -n -F -f /tmp/s13.txt /Volumes/Sensidine/Praxis.build/docs/reports/2026-11-12-o3-block1-scope-worker1.md | cut -d: -f1
301
$ tail -n 1 /Volumes/Sensidine/Praxis.build/docs/reports/2026-11-12-o3-block1-scope-worker1.md | grep -c -x -F -f /tmp/s13.txt
1
```

### Correction 1 evidence
Added by the correction 1 manager after the run; these commands were run by the correction 1 manager, not by worker1, before this block was inserted. They cover :101 (the pipeline count 0; topology :112 names Deviation G (D-2026-07-09-D)), O-e (the entry holds no "proven end-to-end"; HEAD :140 and rubric :110 do) and the fix note (the pre-edit copy held the S13 sentence at lines 35, 52 and 288 of 288).
```
$ sed -n 2371,2387p DECISIONS.md | grep -c -F 'proven end-to-end'
0
$ git show HEAD:specs/SPEC_RUBRIC.md | sed -n 110p | grep -c -F 'proven end-to-end'
1
$ git show HEAD:DECISIONS.md | sed -n 140p | grep -c -F 'proven end-to-end'
1
$ git show HEAD:docs/specs/2026-11-10-live-signal-topology.md | sed -n 112p | grep -c -F 'Deviation G (D-2026-07-09-D)'
1
$ git show HEAD:specs/SPEC_RUBRIC.md | grep -n -F 'untested' | grep -c -F 'Deviation G'
0
$ grep -n -F -f /tmp/s13.txt /tmp/o3-worker1-orig.md | cut -d: -f1
35
52
288
$ wc -l < /tmp/o3-worker1-orig.md
     288
```

### Correction 1 evidence, round 2
Added by the correction 1 manager after its adversary run; run by the correction 1 manager, not by worker1, before this block was inserted (the block holds commands and counts only). Covers :317 (17:31Z in the master's row), :318 (the phrase at topology :112 and :217) and :275 (S13 count and last line).
```
$ git show HEAD:docs/specs/2026-11-10-live-signal-topology.md | grep -n -F "Deviation G's ingress question leaves the anchor's live path" | cut -d: -f1
112
217
$ grep -F '[2026-11-12T17:31:00Z]' DECISION_LOG.md | grep -o -E 'WHEN: 17:31Z'
WHEN: 17:31Z
$ grep -c -F -f /tmp/s13.txt docs/reports/2026-11-12-o3-block1-scope-worker1.md
1
$ tail -n 1 docs/reports/2026-11-12-o3-block1-scope-worker1.md | grep -c -x -F -f /tmp/s13.txt
1
```

## Findings

Defects:

1. Manager report is incomplete beyond the two parts declared pending. `docs/reports/2026-11-12-o3-block1-scope-manager.md` :10–11 "## Workers dispatched" holds only "(filled below)", :13–14 "## Process log" holds only "(filled below)", and :163 reads "(report scans below)", so the report's own evidence-rule and de-identification scans (S13 count, banned words, rep pattern, medication list, email, person names on the report text) are absent. The brief declared only "Adversarial findings" (:165–166) and the Result line (:178) pending. [Correction 1 label: the brief is not on disk; this sentence is a process record of worker1's brief, not claimed as evidence.] Evidence: the `(filled below)` / `(report scans below)` grep lines in the scan block below. At the time worker1 ran, the S13 sentence was absent from the manager report (s13=0 for the manager report in the scan block above); noted only. [Correction 1 label: the earlier words on the manager report's last line had no pasted output and are withdrawn; manager report line numbers in this item are as at worker1's run, when it had 178 lines (scan block above).]

No defect found in the entry D-2026-11-12-C, the parked block, the line-range arithmetic or the MANIFEST rows.

Observations (not defects):

- O-a. Entry line 2379 (window line 15 above) says the path and deferral are "in its **Decision:** paragraph at :140". The `**Decision:**` label is at HEAD :139; the paragraph text holding both quotes is at :140. The citation is right for the quoted text; a reader looking for the label at :140 will find it one line up.
- O-b. Entry Limits paragraph (2383): "that move is a later master step" is a forward process statement with no source in the entry. It decides nothing about design or ingress, so it does not break S2 or the no-design-choice rule.
- O-c. Timestamp format: the entry writes DECISION_LOG 2026-11-12T17:31Z (the master's row DECISION_LOG 2026-11-12T17:31:00Z writes 17:31Z in its WHEN field; pasted under "Correction 1 evidence, round 2"); the MANIFEST row, the manager report and the DECISION_LOG row :879 write 17:31:00Z. Same instant.
- O-d. The topology phrase "Deviation G's ingress question leaves the anchor's live path" is at topology :112 and also :217 (pasted under "Correction 1 evidence, round 2") (manager report :101–103, line numbers as at worker1's run); the entry cites :112 only. The topology doc does not carry the id D-2026-11-10-B; the link is DECISIONS.md :2047 (adopts the topology for rubric F1), which the entry's parenthetical relies on.
- O-e. S2 read of the entry: it does not claim anything was tested or proven on its own authority. "proven end-to-end" appears only in the HEAD sources (:140, rubric :110), not in the entry (counts under "Correction 1 evidence"). "untested" is attributed to rubric O3 (:111). The ingress-placement claim (Block 4–5) is quoted from :140. The entry makes no design choice and records no ingress decision.

Result: FAIL
Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
