# 2026-11-10 — housekeeping 2b — manager report

## Task

Unit `2026-11-10-housekeeping-2b`, authorised by DECISION_LOG row `2026-11-10T09:43:00Z` (DECISION_LOG.md:795, working tree; WHO: praxis-master; "Decided by master under D-2026-11-08-D D1", changeable by Amear). Two parts:

- PART 1 — G18 (D11 sweep report `docs/reports/2026-11-09-d11-sweep-manager.md`:69): archive the 2026-11-01 Desktop trade-list CSVs into `docs/reports/evidence/`, unaltered, sha256 before and after, content safety first.
- PART 2 — G30 (same report :81; bead `Praxis_build-zd4`): one DECISIONS.md entry, appended at the end, recording the praxispush low-privilege user as DEFERRED, with its accepted risk and trigger (rubric O2).

Not done here (out of scope): bead zd4 is not closed or updated. SPEC_RUBRIC.md, DECISION_LOG.md, HANDOFF.md and STATUS.md are not edited. No user is provisioned and no permission is changed. The git index is not touched. Nothing is committed.

## Rubric criteria addressed

- O2 (specs/SPEC_RUBRIC.md:95-101): entry D-2026-11-10-A records the deferral and its accepted risk, including the blast-radius risk O2 names (:97). O2 stays OPEN; the entry does not grade it and the rubric is not edited.
- S1: every claim below rests on pasted output. The workers' reports hold their own pasted output.
- S2: the entry keeps OBSERVED (`id praxispush`, `ls -ld`, bd states), REPORTED (D-2026-11-06-A item 3) and inference apart, and labels each inference. The sim-only exposure is stated as "record-level, not tested".
- S4: the authorising rows exist before the work. DECISION_LOG :795 (09:43Z) is the master's decision, and the entry is the DECISIONS.md record of the deviation (the praxispush user specified in D-2026-07-09-C and not built).
- S6: see the cross-block section.
- S8: no D2 item is decided. Provisioning is D2(d)-adjacent and stays with Amear. Archiving files is not a D2 item. The 2026-11-01 "no copies" was a default, not his word: DECISION_LOG.md:626 (R-1101-6) says "The archive-copy question went unanswered, so the default is to cite Desktop paths + sha256 with no copies made." The master closes that question under D1 (DECISION_LOG :795).
- S13: carried once, as the standalone line at the end of the Result section.

## Workers dispatched

| # | agent id | mode | outcome |
|---|---|---|---|
| W1 | a4b69d8cc446cf13d | BUILD (Part 1 + Part 2 + MANIFEST) | done; report `docs/reports/2026-11-10-housekeeping-2b-worker1.md` |
| W2 | a0dabb8824a097e15 | ADVERSARIAL | no result: stopped at its 40-turn limit, wrote no report |
| W3 | a7e5cf7046a7b6e37 | ADVERSARIAL (re-dispatch, budgeted) | FAIL: 5 entry defects (3a, 3b, 3c, 6a, 6b); CSV checks PASS |
| W4 | af9b4553705be54db | BUILD fix 1 | fixed all 5; Fix 1 section in worker1 report |
| W5 | af7d66828c8b96701 | ADVERSARIAL round 2 | FAIL: 2 defects (accepted risk omitted O2's blast radius; one quote misattributed) |
| W6 | a913a8f16eab72422 | BUILD fix 2 | fixed both, added the LOCKED-status sentence; Fix 2 section in worker1 report |
| W7 | a29fbbec78ad74f3e | ADVERSARIAL round 3 | FAIL: 1 defect (subject of the :124 quote widened); manager made a one-line fix |
| W8 | ade7c33af890ef897 | ADVERSARIAL round 4 | FAIL: 2 S2 defects (an unlabelled inference; "did not observe the running system" too broad); manager made a one-line fix |
| W9 | a0d6f5efc4b07e184 | ADVERSARIAL round 5 | FAIL: 1 blocking defect (share overclaim) + 2 minor; manager made a one-line fix |
| W10 | a54f635048bc12f02 | ADVERSARIAL round 6 | PASS; 2 minor findings, which the manager fixed afterwards (see below) |

All adversarial rounds W3 and W5-W10 are in `docs/reports/2026-11-10-housekeeping-2b-adversarial.md`, one section each. Each adversary was given the artifact and the criteria, not the builder's reasoning.

## Process log

1. The manager read DECISION_LOG :795, d11 sweep :69 and :81, DECISIONS.md :400 and :536, `bd show Praxis_build-zd4` and SPEC_RUBRIC.md :95-101.
2. Manager pre-check (read-only). `git ls-files | grep -i -E 'grid|trade'` returns only `scripts/wf/tests/test_tradelist.py` and `scripts/wf/tradelist.py`. `git ls-files | grep -i '\.csv$'` returns only `tools/tickprep/nt-implied-offsets.csv`. Commit 8ca9861 lists 7 .md files and no CSV. The 2026-11-01 readback (`docs/reports/2026-11-01-three-strategy-results.md`:25-32) records the four Desktop CSVs by path and sha256 only. So no trade list was committed byte-for-byte, and all four are candidates.
3. W1 did both parts. All 4 CSVs hash to the recorded values and pass content safety. They were copied with `cp -p` and renamed without spaces (table below). Entry D-2026-11-10-A was appended, and MANIFEST rows were appended at 345-352.
4. The manager re-ran the hashes, `cmp`, the landing-blob `cmp` and the numstat. The manager also ran an independent content-safety scan with a negative test: a temp copy with a planted email and a planted 7-digit account number trips all three counters (output below).
5. Adversarial loop: W3, then fix W4, then W5, then fix W6, then W7 to W10. See the table above.
6. Manager edits. These were wording-only edits inside DECISIONS.md lines 2033, 2037 and 2041, which are this unit's own uncommitted entry. Each one is a single-line change, which the manager contract allows. They fixed the round 3, 4 and 5 findings. After round 6 PASSed, the manager made two more wording edits for its two minor findings. At :2041 "So the limit to sim and test is a record-level limit, not a tested one." became "So, on the record, the exposure is limited to sim; that limit is record-level, not tested." At :2037 a gloss was added for D-072, matching DECISIONS.md:1019 (grep count 1 below). **These two post-round-6 edits narrow claims only, and no worker has re-read them. The master's auditor should read :2037 and :2041.**

### CSV rename table (old name on ~/Desktop, then new name in docs/reports/evidence/)

| role | old | new |
|---|---|---|
| baseline | `NinjaTrader Grid 2026-11-01 07-10 AM.csv` | `2026-11-01-ninjatrader-grid-0710am.csv` |
| OppBand | `NinjaTrader Grid 2026-11-01 07-57 AM.csv` | `2026-11-01-ninjatrader-grid-0757am.csv` |
| Flat1559 | `NinjaTrader Grid 2026-11-01 07-59 AM.csv` | `2026-11-01-ninjatrader-grid-0759am.csv` |
| LastHalfHourMomentum | `NinjaTrader Grid 2026-11-01 08-00 AM.csv` | `2026-11-01-ninjatrader-grid-0800am.csv` |

Held out: none.

## Adversarial findings

- W3 3a: the trigger said only "provisioned". It now reads provisioned AND the drop dir moved to `/Users/praxispush/praxis-signals` (D-2026-07-09-C :121; zd4 acceptance). **This is wider than the master's 09:43Z text ("provisioned"). It follows the bead's own acceptance. Master to note.**
- W3 3b: "a replacement control ruled by Amear" had no source. It is replaced by the D1 reversal clause, quoted from :1973.
- W3 3c and W8: the sim-only limit is now stated as record-level, not tested. The no-observation sentence is now scoped to the order path, account connections and running processes.
- W3 6a: **the master's brief wording, "the primary account's home, which is shared into the Windows VM", is not stated as fact.** The records differ. The rubric and the VM design give `C:\Mac\Home\praxis-signals\` (Parallels era). The B1-c close reason (`bd show Praxis_build-dnt`) says the Parallels share was scoped to /Users/admin/praxis-signals only. D-2026-11-06-A item 3 (:1004, REPORTED) says Fusion shared folders are unavailable and an SMB share of `Praxis.build` is mapped as Z:. The entry sets these side by side. It says it did not observe how, or whether, the current VM reaches the drop dir.
- W3 6b: B1-c (`dnt`) is CLOSED, its bead does not mention praxispush (grep count 0), and B1-a (`dgt`) is DEFERRED to 2027-01-01. All of this is now in the entry.
- W5: the blast-radius risk is added (:124, :125, rubric :97). So is the breaker bypass, quoting rubric :23-24 and labelled "inference from that text, not tested". One misattributed quote is fixed.
- W7: the :124 quote now keeps its own subject, "A compromised n8n push key". Widening it to any writer is labelled as the entry's inference.
- W9: the share sentence is narrowed to "write access through a share ... if one exists (this entry did not observe one)".
- W3 note (out of scope): MANIFEST.md working-tree rows 307-314 are a parked unit's uncommitted rows, inserted after HEAD line 306. Committing MANIFEST.md whole would carry them along. A landing blob `/tmp/hk2b-final/MANIFEST.md` = HEAD + this unit's rows 345-352 is built and checked below.

## S6 cross-block check

- Block 1 (signal path; B1-a `dgt`, B1-c `dnt`): no contradiction found by W3 or W5 (their `grep -rn -i 'praxispush'` over specs and docs/specs is in the adversarial report). B1-c is closed, and B1-a is deferred to 2027-01-01. The trigger ties the deferral to the B1-a forced-command step, which has not run, so it does not undo a finished step. D-2026-07-09-C stays LOCKED and unchanged (:117). The entry says so.
- Block 3 (breakers): the trigger reuses D8(6)'s gate, "fixed before any Block 3 code that can place orders" (:1982). The breaker-bypass risk of a direct file drop is recorded as an inference from rubric F1 :23-24. F1 stays FROZEN, and no Block 3 spec says otherwise (W5 round 2: "the entry contradicts no Block 1, 3, 4 or 5 spec").
- Block 4/5 (paper/live): D8(8) (:1982) makes the final step a paper pass on MFFU sim and Block 5 a separate D2(b) sign-off. The go-live checklist line "unmap Z: and turn off the SMB share" (:1275) is cited, not changed. No contradiction found.

## Files staged

None by this unit. The index holds exactly `docs/reports/evidence/2026-10-28-mffu-davi-reply.png`, as before (pasted below). The unit's working-tree changes for the master to land:
- new: `docs/reports/evidence/2026-11-01-ninjatrader-grid-{0710am,0757am,0759am,0800am}.csv`, `docs/reports/2026-11-10-housekeeping-2b-worker1.md`, `docs/reports/2026-11-10-housekeeping-2b-adversarial.md`, this report
- modified: `DECISIONS.md` (entry D-2026-11-10-A, lines 2025-2045, heading :2026; landing blob `/tmp/hk2b-final/DECISIONS.md`), `MANIFEST.md` (rows 345-352; landing blob `/tmp/hk2b-final/MANIFEST.md` = HEAD :1-336 + rows 345-352, so the blob numbers them 337-344)

## Result

Result: PASS

PASS on the six-step stress test, with one disclosed caveat: the two post-round-6 wording edits (process log item 6) have not been re-read by a worker. Bead zd4 stays open for the master.

S13: Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## Verification evidence (command output)

Pasted last, after the final edit. Every block below is raw output appended by the command that produced it.

```
$ git rev-parse --short HEAD
16c7bfe
[exit=0]
$ git ls-files | grep -i -E 'grid|trade'
scripts/wf/tests/test_tradelist.py
scripts/wf/tradelist.py
[exit=0]
$ git ls-files | grep -i '\.csv$'
tools/tickprep/nt-implied-offsets.csv
[exit=0]
$ git show --stat --format=%h 8ca9861 | tail -n 8
 DECISION_LOG.md                                    |   13 +
 DISPATCH_LOG.md                                    |   29 +
 MANIFEST.md                                        |    4 +
 docs/reports/2026-10-31-voice-session-notes-2.md   |  187 +++
 .../2026-11-01-three-strategy-results-manager.md   |  130 ++
 docs/reports/2026-11-01-three-strategy-results.md  | 1287 ++++++++++++++++++++
 .../2026-11-01-voice-handoff-commission-fix.md     |  136 +++
 7 files changed, 1786 insertions(+)
[exit=0]
$ sed -n '29,32p' docs/reports/2026-11-01-three-strategy-results.md | cut -c1-200
| `/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-10 AM.csv` | baseline grid | `421c44e6cd9d417b432be1a5b440b0861782a3bba7e1961beba5b5421e0534bd` |
| `/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-57 AM.csv` | OppBand grid | `4207ea99e7f1187b54ebe45c97822409629192ed12e7ee0dbaacb241c152b6e8` |
| `/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-59 AM.csv` | Flat1559 grid | `5a3c4d783a44b33a18c4eb77f50444af1d4cf65ed4190038becc4c2007c868e0` |
| `/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 08-00 AM.csv` | LastHalfHourMomentum grid | `4efd8ce8e95cc408f82d494fcf55238c25b9980b030a39eb25f4eaa5fbd180d9` |
[exit=0]
$ openssl dgst -sha256 "/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-10 AM.csv" "docs/reports/evidence/2026-11-01-ninjatrader-grid-0710am.csv"
SHA2-256(/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-10 AM.csv)= 421c44e6cd9d417b432be1a5b440b0861782a3bba7e1961beba5b5421e0534bd
SHA2-256(docs/reports/evidence/2026-11-01-ninjatrader-grid-0710am.csv)= 421c44e6cd9d417b432be1a5b440b0861782a3bba7e1961beba5b5421e0534bd
[exit=0]
$ stat -f '%z bytes' "/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-10 AM.csv" "docs/reports/evidence/2026-11-01-ninjatrader-grid-0710am.csv"; wc -l < "docs/reports/evidence/2026-11-01-ninjatrader-grid-0710am.csv"
256796 bytes
256796 bytes
    1191
[exit=0]
$ cmp "/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-10 AM.csv" "docs/reports/evidence/2026-11-01-ninjatrader-grid-0710am.csv"
[exit=0]
$ git check-ignore -v "docs/reports/evidence/2026-11-01-ninjatrader-grid-0710am.csv"
[exit=1]
$ git cat-file -e 90a581febb1442138805e962fca1541462b14199
[exit=1]
account_col=3 uniq_accounts=1 all_Backtest_or_Sim=yes emails=0 phones=0 digits7=0 name_terms=0
$ openssl dgst -sha256 "/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-57 AM.csv" "docs/reports/evidence/2026-11-01-ninjatrader-grid-0757am.csv"
SHA2-256(/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-57 AM.csv)= 4207ea99e7f1187b54ebe45c97822409629192ed12e7ee0dbaacb241c152b6e8
SHA2-256(docs/reports/evidence/2026-11-01-ninjatrader-grid-0757am.csv)= 4207ea99e7f1187b54ebe45c97822409629192ed12e7ee0dbaacb241c152b6e8
[exit=0]
$ stat -f '%z bytes' "/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-57 AM.csv" "docs/reports/evidence/2026-11-01-ninjatrader-grid-0757am.csv"; wc -l < "docs/reports/evidence/2026-11-01-ninjatrader-grid-0757am.csv"
191423 bytes
191423 bytes
     811
[exit=0]
$ cmp "/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-57 AM.csv" "docs/reports/evidence/2026-11-01-ninjatrader-grid-0757am.csv"
[exit=0]
$ git check-ignore -v "docs/reports/evidence/2026-11-01-ninjatrader-grid-0757am.csv"
[exit=1]
$ git cat-file -e 241e718eb6ab2c425717537d68132b78de3fd15a
[exit=1]
account_col=3 uniq_accounts=1 all_Backtest_or_Sim=yes emails=0 phones=0 digits7=0 name_terms=0
$ openssl dgst -sha256 "/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-59 AM.csv" "docs/reports/evidence/2026-11-01-ninjatrader-grid-0759am.csv"
SHA2-256(/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-59 AM.csv)= 5a3c4d783a44b33a18c4eb77f50444af1d4cf65ed4190038becc4c2007c868e0
SHA2-256(docs/reports/evidence/2026-11-01-ninjatrader-grid-0759am.csv)= 5a3c4d783a44b33a18c4eb77f50444af1d4cf65ed4190038becc4c2007c868e0
[exit=0]
$ stat -f '%z bytes' "/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-59 AM.csv" "docs/reports/evidence/2026-11-01-ninjatrader-grid-0759am.csv"; wc -l < "docs/reports/evidence/2026-11-01-ninjatrader-grid-0759am.csv"
261564 bytes
261564 bytes
    1191
[exit=0]
$ cmp "/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-59 AM.csv" "docs/reports/evidence/2026-11-01-ninjatrader-grid-0759am.csv"
[exit=0]
$ git check-ignore -v "docs/reports/evidence/2026-11-01-ninjatrader-grid-0759am.csv"
[exit=1]
$ git cat-file -e 015c9c51d3248bca50e8721d424bffa8c36c7c14
[exit=1]
account_col=3 uniq_accounts=1 all_Backtest_or_Sim=yes emails=0 phones=0 digits7=0 name_terms=0
$ openssl dgst -sha256 "/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 08-00 AM.csv" "docs/reports/evidence/2026-11-01-ninjatrader-grid-0800am.csv"
SHA2-256(/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 08-00 AM.csv)= 4efd8ce8e95cc408f82d494fcf55238c25b9980b030a39eb25f4eaa5fbd180d9
SHA2-256(docs/reports/evidence/2026-11-01-ninjatrader-grid-0800am.csv)= 4efd8ce8e95cc408f82d494fcf55238c25b9980b030a39eb25f4eaa5fbd180d9
[exit=0]
$ stat -f '%z bytes' "/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 08-00 AM.csv" "docs/reports/evidence/2026-11-01-ninjatrader-grid-0800am.csv"; wc -l < "docs/reports/evidence/2026-11-01-ninjatrader-grid-0800am.csv"
293775 bytes
293775 bytes
    1305
[exit=0]
$ cmp "/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 08-00 AM.csv" "docs/reports/evidence/2026-11-01-ninjatrader-grid-0800am.csv"
[exit=0]
$ git check-ignore -v "docs/reports/evidence/2026-11-01-ninjatrader-grid-0800am.csv"
[exit=1]
$ git cat-file -e 476f3adf273f192392404d2c494df26266ba0c14
[exit=1]
account_col=3 uniq_accounts=1 all_Backtest_or_Sim=yes emails=0 phones=0 digits7=0 name_terms=0
$ head -1 docs/reports/evidence/2026-11-01-ninjatrader-grid-0710am.csv
Trade number,Instrument,Account,Strategy,Market pos.,Qty,Entry price,Exit price,Entry time,Exit time,Entry name,Exit name,Profit,Cum. net profit,Commission,Clearing Fee,Exchange Fee,IP Fee,NFA Fee,MAE,MFE,ETD,Bars,
[exit=0]
--- negative test: temp copy with planted email and 7-digit account
emails=1 digits7=1 name_terms=1
$ id praxispush
id: praxispush: no such user
[exit=1]
$ ls -ld ~/praxis-signals/
drwxr-xr-x@ 14 admin  staff  448 Nov 10 01:54 /Users/admin/praxis-signals/
[exit=0]
$ git show HEAD:DECISIONS.md | grep -c 'D-2026-11-10'
0
[exit=1]
$ grep -n 'D-2026-11-10-A' DECISIONS.md | cut -c1-120
2026:## 2026-11-10 — D-2026-11-10-A: praxispush low-privilege user DEFERRED, accepted risk recorded (bead Praxis_build-z
[exit=0]
$ cmp <(git show HEAD:DECISIONS.md) <(head -n 2024 DECISIONS.md)
[exit=0]
$ git show HEAD:DECISIONS.md > /tmp/hk2b-final/DECISIONS.md && tail -n +2025 DECISIONS.md >> /tmp/hk2b-final/DECISIONS.md && cmp /tmp/hk2b-final/DECISIONS.md DECISIONS.md
[exit=0]
$ sed -n '2025,$p' DECISIONS.md | grep -c -F 'Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.'
1
[exit=0]
$ sed -n '1019p' DECISIONS.md | grep -c -F 'a migration-ledger decision, not in this repo'
1
[exit=0]
$ sed -n '124p' DECISIONS.md | grep -c -F 'A compromised n8n push key reaches a directory that contains nothing but signals'
1
[exit=0]
$ git diff --numstat HEAD -- DECISIONS.md MANIFEST.md
21	0	DECISIONS.md
16	0	MANIFEST.md
[exit=0]
$ git diff -U0 HEAD -- MANIFEST.md | grep '^@@'
@@ -306,0 +307,8 @@
@@ -336,0 +345,8 @@
[exit=0]
$ diff <(git show HEAD:MANIFEST.md | sed -n '307,314p') <(sed -n '307,314p' MANIFEST.md) >/dev/null
[exit=1]
$ diff <(git diff -U0 HEAD -- MANIFEST.md | sed -n '/^@@ -306,0 +307,8 @@/,/^@@/p' | grep '^+' | cut -c2-) <(sed -n '307,314p' MANIFEST.md)
[exit=0]
$ diff <(git show HEAD:MANIFEST.md | sed -n '307,336p') <(sed -n '315,344p' MANIFEST.md)
[exit=0]
$ git show HEAD:MANIFEST.md > /tmp/hk2b-final/MANIFEST.md && sed -n '345,352p' MANIFEST.md >> /tmp/hk2b-final/MANIFEST.md && wc -l < /tmp/hk2b-final/MANIFEST.md && cmp <(git show HEAD:MANIFEST.md) <(head -n 336 /tmp/hk2b-final/MANIFEST.md) && cmp <(tail -n 8 /tmp/hk2b-final/MANIFEST.md) <(sed -n '345,352p' MANIFEST.md)
     344
[exit=0]
$ grep -n '' MANIFEST.md | tail -n 8 | cut -c1-240
345:| /docs/reports/evidence/2026-11-01-ninjatrader-grid-0710am.csv | Evidence | 2 | 2026-11-10 | baseline grid (PraxisNoiseAreaBreakout) trade list, NinjaTrader backtest export, Account column Backtest only; source Desktop name `NinjaTrade
346:| /docs/reports/evidence/2026-11-01-ninjatrader-grid-0757am.csv | Evidence | 2 | 2026-11-10 | OppBand grid (PraxisNoiseAreaBreakout_OppBand) trade list, NinjaTrader backtest export, Account column Backtest only; source Desktop name `Nin
347:| /docs/reports/evidence/2026-11-01-ninjatrader-grid-0759am.csv | Evidence | 2 | 2026-11-10 | Flat1559 grid (PraxisNoiseAreaBreakout_Flat1559) trade list, NinjaTrader backtest export, Account column Backtest only; source Desktop name `N
348:| /docs/reports/evidence/2026-11-01-ninjatrader-grid-0800am.csv | Evidence | 2 | 2026-11-10 | LastHalfHourMomentum grid (PraxisLastHalfHourMomentum) trade list, NinjaTrader backtest export, Account column Backtest only; source Desktop n
349:| /docs/reports/2026-11-10-housekeeping-2b-worker1.md | Report | 2 | 2026-11-10 | BUILD worker report for unit 2026-11-10-housekeeping-2b (master under D-2026-11-08-D D1, DECISION_LOG row 2026-11-10T09:43:00Z): G18 hash match, content-s
350:| /docs/reports/2026-11-10-housekeeping-2b-adversarial.md | Report | 2 | 2026-11-10 | ADVERSARIAL worker report for unit 2026-11-10-housekeeping-2b (master under D-2026-11-08-D D1, DECISION_LOG row 2026-11-10T09:43:00Z): break attempts 
351:| /docs/reports/2026-11-10-housekeeping-2b-manager.md | Report | 2 | 2026-11-10 | Manager report for unit 2026-11-10-housekeeping-2b (master under D-2026-11-08-D D1, DECISION_LOG row 2026-11-10T09:43:00Z): G18 archive of the four 2026-1
352:| /DECISIONS.md | Log | 2 | 2026-11-10 | MODIFIED (unit 2026-11-10-housekeeping-2b; master under D-2026-11-08-D D1, DECISION_LOG row 2026-11-10T09:43:00Z): entry D-2026-11-10-A (praxispush low-privilege user DEFERRED, accepted risk reco
[exit=0]
$ for f in docs/reports/evidence/2026-11-01-ninjatrader-grid-0*am.csv; do test -e "$f" && echo ok "$f"; done; ls docs/reports/2026-11-10-housekeeping-2b-*.md
ok docs/reports/evidence/2026-11-01-ninjatrader-grid-0710am.csv
ok docs/reports/evidence/2026-11-01-ninjatrader-grid-0757am.csv
ok docs/reports/evidence/2026-11-01-ninjatrader-grid-0759am.csv
ok docs/reports/evidence/2026-11-01-ninjatrader-grid-0800am.csv
docs/reports/2026-11-10-housekeeping-2b-adversarial.md
docs/reports/2026-11-10-housekeeping-2b-manager.md
docs/reports/2026-11-10-housekeeping-2b-worker1.md
[exit=0]
$ git diff --cached --name-only
docs/reports/evidence/2026-10-28-mffu-davi-reply.png
[exit=0]
```

## Correction 1 (after audit FAIL 1, 2026-11-10)

Scope: DECISION_LOG row 2026-11-10T10:20:00Z (audit FAIL 1, strike 1). Done by the manager directly, no workers. The rubric line is S13 (specs/SPEC_RUBRIC.md:133). The standalone-line count below follows the auditor's rule: lines outside quoted commands and pasted output.

### (a) Manager report line 20

Line 20 was a second standalone copy of the S13 sentence (a bullet in "Rubric criteria addressed"). It now reads `- S13: carried once, as the standalone line at the end of the Result section.` That line is :89, which is unchanged. Line :207 is a pasted grep command inside the evidence block; it was left as is. Before the edit, the file with line 20 removed hashed to `4968d402094c1356722c30f0ad69f8dc4f8fb8594530ba773cdc7c457b7836cc`. The same hash, taken on the first 255 lines, is re-run below, so only line 20 changed in the original body.

### (b) Worker reports

The auditor counted 0 standalone copies in each worker report. One line was appended at the end of each: a blank line, then `S13 (added by the manager under Correction 1, 2026-11-10): ` followed by the S13 sentence. This was a pure append: worker1 went from 542 to 544 lines, adversarial from 539 to 541. The before-hashes of the old bodies were worker1 `head -n 542` = `b90df06c805c0972278677a54b844f2a84562bfbf70b55dc7ce3983d845616da` and adversarial `head -n 539` = `2e35cbdad7f6d136800665895800a5d61b1ecb218fcd55352bcdc06c382680c0`. Both are re-run below.

### S6 addendum: specs that hard-code the drop-dir path

The S6 cross-block check above did not list the specs that name the drop dir. This grep runs on the working tree, cut to 160 columns:

```
$ git grep -n -E 'praxis-signals' -- docs/specs specs | cut -c1-160
docs/specs/2026-07-15-b2-data-acquisition-spec.md:118:5. **Landing location:** write the export to the VM→Mac shared path so it reaches the repo host — **`\\Mac
docs/specs/2026-07-20-b2-data-mailbox-watcher-design.md:15:shared folder (`\\Mac\praxis-signals` == `~/praxis-signals` on the Mac). The **data files
docs/specs/2026-07-20-b2-data-mailbox-watcher-design.md:30:### 2.1 Mailbox layout (under the share, `~/praxis-signals/b2-data/`)
docs/specs/2026-07-20-b2-data-mailbox-watcher-design.md:47:- **Script:** `praxis-b2data-watch.sh` — a clone of `praxis-signals-sweep-daemon.sh`
docs/specs/2026-07-20-b2-data-mailbox-watcher-design.md:53:  `~/praxis-signals` (internal disk — fine). The repo holds SOURCE only.
docs/specs/2026-07-20-b2-data-mailbox-watcher-design.md:88:read `~/praxis-signals/b2-data/raw/`). Emits a machine-readable + human-readable report.
docs/specs/2026-07-20-b2-data-mailbox-watcher-design.md:144:   empty `inbound/status.txt` exist under `~/praxis-signals/b2-data/`.
docs/specs/2026-07-25-vm-agent-delegation-workspace-design.md:17:This generalizes the existing `~/praxis-signals/b2-data/{outbound/INSTRUCTIONS.md, inbound/}`
docs/specs/2026-07-25-vm-agent-delegation-workspace-design.md:45:- **Mac:** `~/praxis-signals/vm-agent/` (on the Parallels share, outside the git repo).
docs/specs/2026-07-25-vm-agent-delegation-workspace-design.md:46:- **Windows:** `C:\Mac\Home\praxis-signals\vm-agent\`
docs/specs/2026-07-25-vm-agent-delegation-workspace-design.md:47:- **Prefix verified** 2026-07-25: `Test-Path C:\Mac\Home\praxis-signals\b2-data` → `True`
docs/specs/2026-07-25-vm-agent-delegation-workspace-design.md:48:  in the Parallels Windows 11 ARM VM. So `C:\Mac\Home\praxis-signals\` is the correct
docs/specs/2026-07-25-vm-agent-delegation-workspace-design.md:110:1. **What this workspace is** + the real Windows root `C:\Mac\Home\praxis-signals\vm-agent\`.
docs/specs/2026-07-25-vm-agent-delegation-workspace-design.md:169:the workspace: `cd C:\Mac\Home\praxis-signals\vm-agent` then `claude`. Standing kickoff line
docs/specs/2026-11-05-walk-forward-spec.md:16:8. Data file `~/praxis-signals/b2-data/NQ-continuous-1min.nt8import.txt` (outside the repo), named at `DECISIONS.m
docs/specs/2026-11-05-walk-forward-spec.md:99:- File: `~/praxis-signals/b2-data/NQ-continuous-1min.nt8import.txt`, 95,900,139 bytes, sha256 `307c5e8af1da42b7606
specs/SPEC_RUBRIC.md:98:at `~/praxis-signals/`, surfacing in Windows as `C:\Mac\Home\praxis-signals\` —
```

`docs/specs/2026-07-15-b2-data-acquisition-spec.md:118` is cut off before the path at 160 columns. The path there is `\\Mac\praxis-signals\b2-data\...` (from `git grep -n -o -E '.{0,20}praxis-signals.{0,30}'` on that file). The dependencies:
- `docs/specs/2026-11-05-walk-forward-spec.md` :16 and :99, the data file `~/praxis-signals/b2-data/NQ-continuous-1min.nt8import.txt`
- `docs/specs/2026-07-20-b2-data-mailbox-watcher-design.md` :15, :30, :53, :88, :144, the `~/praxis-signals` share and `~/praxis-signals/b2-data/`. :47 is a script name (`praxis-signals-sweep-daemon.sh`), not a path.
- `docs/specs/2026-07-25-vm-agent-delegation-workspace-design.md` :17, :45-48, :110, :169, both `~/praxis-signals/` and the Windows view `C:\Mac\Home\praxis-signals\`
- `docs/specs/2026-07-15-b2-data-acquisition-spec.md` :118, `\\Mac\praxis-signals\b2-data\`
- `specs/SPEC_RUBRIC.md` :98, the rubric's own description of the share at `~/praxis-signals/` and `C:\Mac\Home\praxis-signals\`

If the drop dir moves under the D-2026-11-10-A trigger, all of these specs will need updating, and the rubric line will need its own owner decision. This section records that. None of these files was changed by this unit or by this correction.

### Files staged (correction)

The "Files staged" section above describes the real index only, so it is not the commit index. The commit index for this unit is the master's temp index `/tmp/idx-hk2b`. The master built it from HEAD plus the landing blobs (`/tmp/hk2b-final/DECISIONS.md`, `/tmp/hk2b-final/MANIFEST.md`, and the master's DECISION_LOG flush) and the new files (the four grid CSVs and the three hk2b reports). Read-only view before this correction, using `GIT_INDEX_FILE=/tmp/idx-hk2b git diff --cached --name-status HEAD`, cut to 160: M DECISIONS.md, M DECISION_LOG.md, M MANIFEST.md, A the three hk2b reports, A the four grid CSVs. That temp index still holds the pre-correction report blobs, so the master has to rebuild it before re-audit. The real index holds `docs/reports/evidence/2026-10-28-mffu-davi-reply.png` only, the held-out PNG, and this correction did not touch it (no git add, reset, rm, stash, or checkout).

### Verification evidence (command output), Correction 1

Run after all edits to the three reports. To keep the S13 sentence out of this section, `S` is not typed out. It is read from manager line 89 (`S=$(sed -n 89p <manager> | cut -c6-)`), and the first command proves `S` equals the sentence quoted in the rubric at :133. In `grep -n` output, the awk filter swaps the sentence for the marker `<the S13 sentence>` so the sentence is not copied into this file. Line numbers and line prefixes are kept. R is `docs/reports/2026-11-10-housekeeping-2b`.

```
$ sed -n 133p specs/SPEC_RUBRIC.md | grep -c -F "\"$S\""
1
[exit=0]
$ grep -c -F "$S" $R-manager.md
2
[exit=0]
$ grep -n -F "$S" $R-manager.md | awk -v s="$S" '{i=index($0,s); if(i) $0=substr($0,1,i-1) "<the S13 sentence>" substr($0,i+length(s))} 1' | cut -c1-120
89:S13: <the S13 sentence>
207:$ sed -n '2025,$p' DECISIONS.md | grep -c -F '<the S13 sentence>'
[exit=0]
$ grep -c -F "$S" $R-worker1.md
3
[exit=0]
$ grep -n -F "$S" $R-worker1.md | awk -v s="$S" '{i=index($0,s); if(i) $0=substr($0,1,i-1) "<the S13 sentence>" substr($0,i+length(s))} 1' | cut -c1-120
402:S13: <the S13 sentence>
523:S13: <the S13 sentence>
544:S13 (added by the manager under Correction 1, 2026-11-10): <the S13 sentence>
[exit=0]
$ grep -c -F "$S" $R-adversarial.md
6
[exit=0]
$ grep -n -F "$S" $R-adversarial.md | awk -v s="$S" '{i=index($0,s); if(i) $0=substr($0,1,i-1) "<the S13 sentence>" substr($0,i+length(s))} 1' | cut -c1-120
196:$ sed -n '2025,$p' DECISIONS.md | grep -c -F '<the S13 sentence>'
306:`grep -c '<the S13 sentence>'` on :2025-end -> `1`. `grep -c 'Fills are optimistic'` -> `1`. PASS.
373:`tail -n +2025 DECISIONS.md | grep -c -x -F 'S13: <the S13 sentence>'` -> `1`. OK.
454:$ grep -cF "<the S13 sentence>" DECISIONS.md
499:$ tail -n +2025 DECISIONS.md | grep -oF "<the S13 sentence>" | wc -l
541:S13 (added by the manager under Correction 1, 2026-11-10): <the S13 sentence>
[exit=0]
$ sed -n "/^## Correction 1/,\$p" $M | grep -c -F "$S"
0
[exit=1]
$ sed -n 20p $M
- S13: carried once, as the standalone line at the end of the Result section.
[exit=0]
$ head -n 255 $M | sed 20d | openssl dgst -sha256
SHA2-256(stdin)= 4968d402094c1356722c30f0ad69f8dc4f8fb8594530ba773cdc7c457b7836cc
[exit=0]
$ head -n 542 $R-worker1.md | openssl dgst -sha256
SHA2-256(stdin)= b90df06c805c0972278677a54b844f2a84562bfbf70b55dc7ce3983d845616da
[exit=0]
$ head -n 539 $R-adversarial.md | openssl dgst -sha256
SHA2-256(stdin)= 2e35cbdad7f6d136800665895800a5d61b1ecb218fcd55352bcdc06c382680c0
[exit=0]
$ tail -n 2 $R-worker1.md | awk -v s="$S" '{i=index($0,s); if(i) $0=substr($0,1,i-1) "<the S13 sentence>" substr($0,i+length(s))} 1' | cut -c1-120

S13 (added by the manager under Correction 1, 2026-11-10): <the S13 sentence>
[exit=0]
$ tail -n 2 $R-adversarial.md | awk -v s="$S" '{i=index($0,s); if(i) $0=substr($0,1,i-1) "<the S13 sentence>" substr($0,i+length(s))} 1' | cut -c1-120

S13 (added by the manager under Correction 1, 2026-11-10): <the S13 sentence>
[exit=0]
$ grep -c -w "T[B]D" $M $R-worker1.md $R-adversarial.md
docs/reports/2026-11-10-housekeeping-2b-manager.md:0
docs/reports/2026-11-10-housekeeping-2b-worker1.md:0
docs/reports/2026-11-10-housekeeping-2b-adversarial.md:0
[exit=1]
$ wc -l $M $R-worker1.md $R-adversarial.md
     369 docs/reports/2026-11-10-housekeeping-2b-manager.md
     544 docs/reports/2026-11-10-housekeeping-2b-worker1.md
     541 docs/reports/2026-11-10-housekeeping-2b-adversarial.md
    1454 total
[exit=0]
$ git diff --cached --name-only
docs/reports/evidence/2026-10-28-mffu-davi-reply.png
[exit=0]
```

The manager count of 369 above was taken partway through this block. The rest of the block, this note and the Result line below bring the file to 382 lines. The S13 standalone lines are manager :89, worker1 :544, and adversarial :541. Manager :207 and the worker reports' other hits are quoted commands or pasted output.

Correction 1 Result: PASS
