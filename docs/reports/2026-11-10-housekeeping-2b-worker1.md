# Unit 2026-11-10-housekeeping-2b, worker 1 report

## Task
G18: archive the four 2026-11-01 NinjaTrader trade lists from `~/Desktop` into `docs/reports/evidence/`, unaltered, after a hash check and a content-safety check. G30: append DECISIONS.md entry D-2026-11-10-A, which records the `praxispush` deferral and the risk accepted with it. Add MANIFEST rows.

## Mode
BUILD.

## Criterion
Authority: DECISION_LOG.md:795, row 2026-11-10T09:43:00Z, WHO praxis-master, "Decided by master under D-2026-11-08-D D1" (items (1) G18 and (2) G30). Rubric O2 (`specs/SPEC_RUBRIC.md`:95-101) is cited. It is not graded here and stays OPEN. Rubric S1 applies: every output below is pasted, none is described.

## Process log
1. I read DECISION_LOG.md:795 and checked repo state (the index holds only the PNG; DECISIONS.md is clean at 2024 lines; no `D-2026-11-10` id exists).
2. I hashed the 4 CSVs and compared them with three-strategy-results.md:29-32. All 4 match. No CSV other than `tools/tickprep/nt-implied-offsets.csv` has ever been committed on any ref.
3. Content safety: I printed only the header rows, then ran a CSV-parsed scan (`python3 -I`, script kept in /tmp/hk2b-scripts/, outside the repo) plus raw grep cross-checks. All 4 files PASS.
4. I copied the files with `cp -p`. Source sha256 before and after equals the copy's. `cmp` exits 0. None is gitignored. No .gitattributes or autocrlf setting applies, and the filtered and unfiltered `git hash-object` values are equal, so the blobs will commit byte-exact.
5. I checked every cited source line myself. One discrepancy: the manager's brief put D8 at DECISIONS.md:1979. D8 is actually at **:1982**; :1979 is `*Section "WORK ORDER" (:39).*`. The entry cites :1982.
6. I appended the entry and verified it with the /tmp/hk2b-final reconstruction and `cmp`.
7. I appended 8 MANIFEST rows and verified that lines 1-344 are unchanged. The brief's 307-314 diff exits 1. That comes from earlier work, not from this unit (see V9).
8. Deviation: this report was written once at the end rather than as I went. Every output below is pasted from this session's commands.

## Verification evidence

### V1. Authority and repo state
```
$ sed -n '795p' DECISION_LOG.md   (excerpt, first sentences)
- [2026-11-10T09:43:00Z] WHO: praxis-master | WHAT: **UNIT 2: housekeeping 2b (HANDOFF top card item 2).** ... **Decided by master under D-2026-11-08-D D1** (changeable by Amear): (1) G18: ... (2) G30: ...
$ git diff --cached --name-only
docs/reports/evidence/2026-10-28-mffu-davi-reply.png
$ wc -l DECISIONS.md MANIFEST.md
    2024 DECISIONS.md
     344 MANIFEST.md
$ git diff --numstat HEAD -- DECISIONS.md     (empty)
$ grep -n 'D-2026-11-10' DECISIONS.md; echo "grep exit=$?"
grep exit=1
$ grep -n '^## ' DECISIONS.md | tail -3
1808:## 2026-11-08 — D-2026-11-08-C: Amear's answers C1–C10 to the 2026-11-08 park card (Claude.ai channel, 2026-11-08). Filed WHO: amear.
1891:## 2026-11-08 — D-2026-11-08-D: Amear's rulings D1–D12, voice session 2 (Claude.ai channel, 2026-11-08). Filed WHO: amear.
2009:## 2026-11-10 — Pointer note for D-2026-11-08-C and D-2026-11-08-D (bead Praxis_build-75n)
```

### V2. Prior facts re-confirmed
```
$ ls -l ~/Desktop/NinjaTrader\ Grid\ 2026-11-01*
-rw-------@ 1 admin  staff  256796 Nov  1 08:06 /Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-10 AM.csv
-rw-------@ 1 admin  staff  191423 Nov  1 08:02 /Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-57 AM.csv
-rw-------@ 1 admin  staff  261564 Nov  1 08:02 /Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-59 AM.csv
-rw-------@ 1 admin  staff  293775 Nov  1 08:02 /Users/admin/Desktop/NinjaTrader Grid 2026-11-01 08-00 AM.csv
$ git ls-files | grep -i '\.csv$'
tools/tickprep/nt-implied-offsets.csv
$ git log --all --format= --name-only | grep -i '\.csv$' | sort -u
tools/tickprep/nt-implied-offsets.csv
$ git show --stat --format='%h %s' 8ca9861
8ca9861 docs: three-strategy backtest readback 2026-11-01 (OppBand, Flat1559, LastHalfHourMomentum vs baseline); notes-2 s3, MANIFEST, ledgers

 DECISION_LOG.md                                    |   13 +
 DISPATCH_LOG.md                                    |   29 +
 MANIFEST.md                                        |    4 +
 docs/reports/2026-10-31-voice-session-notes-2.md   |  187 +++
 .../2026-11-01-three-strategy-results-manager.md   |  130 ++
 docs/reports/2026-11-01-three-strategy-results.md  | 1287 ++++++++++++++++++++
 .../2026-11-01-voice-handoff-commission-fix.md     |  136 +++
 7 files changed, 1786 insertions(+)
$ grep -n '' docs/reports/2026-11-01-three-strategy-results.md | sed -n '25,32p'
25:All seven files are on Amear's Desktop. They are read-only and were not copied, moved or modified (R-1101-6 default: cite path + sha256, no copies). [K01] OBSERVED:
26:
27:| file | role | sha256 |
28:|---|---|---|
29:| `/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-10 AM.csv` | baseline grid | `421c44e6cd9d417b432be1a5b440b0861782a3bba7e1961beba5b5421e0534bd` |
30:| `/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-57 AM.csv` | OppBand grid | `4207ea99e7f1187b54ebe45c97822409629192ed12e7ee0dbaacb241c152b6e8` |
31:| `/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-59 AM.csv` | Flat1559 grid | `5a3c4d783a44b33a18c4eb77f50444af1d4cf65ed4190038becc4c2007c868e0` |
32:| `/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 08-00 AM.csv` | LastHalfHourMomentum grid | `4efd8ce8e95cc408f82d494fcf55238c25b9980b030a39eb25f4eaa5fbd180d9` |
```
Line 25 says "seven files". The four CSVs are in this unit's scope; I did not look at the other three.

### V3. Step 1: hash, size and line count (all 4 match :29-32)
```
SHA2-256(NinjaTrader Grid 2026-11-01 07-10 AM.csv)= 421c44e6cd9d417b432be1a5b440b0861782a3bba7e1961beba5b5421e0534bd
size=256796 lines=    1191
SHA2-256(NinjaTrader Grid 2026-11-01 07-57 AM.csv)= 4207ea99e7f1187b54ebe45c97822409629192ed12e7ee0dbaacb241c152b6e8
size=191423 lines=     811
SHA2-256(NinjaTrader Grid 2026-11-01 07-59 AM.csv)= 5a3c4d783a44b33a18c4eb77f50444af1d4cf65ed4190038becc4c2007c868e0
size=261564 lines=    1191
SHA2-256(NinjaTrader Grid 2026-11-01 08-00 AM.csv)= 4efd8ce8e95cc408f82d494fcf55238c25b9980b030a39eb25f4eaa5fbd180d9
size=293775 lines=    1305
```

### V4. Step 2: content safety (header rows and counts only, no data rows)
Header (the same in all 4 files):
```
Trade number,Instrument,Account,Strategy,Market pos.,Qty,Entry price,Exit price,Entry time,Exit time,Entry name,Exit name,Profit,Cum. net profit,Commission,Clearing Fee,Exchange Fee,IP Fee,NFA Fee,MAE,MFE,ETD,Bars,
```
(The trailing comma gives a 24th unnamed column.) `file` reports "CSV text" for all 4.

CSV-parsed scan (`python3 -I /tmp/hk2b-scripts/scan.py <4 paths>`):
```
== NinjaTrader Grid 2026-11-01 07-10 AM.csv
data_rows=1190 header_cols=24 row_lengths=[(24, 1190)]
Account unique count=1 all_match_sim_backtest=True
Account values: ['Backtest']
Strategy unique count=1 values=['PraxisNoiseAreaBreakout']
email matches total=0 by_col={}
phone-like matches total=0 by_col={}
7+digit-run matches total=0 by_col={}
PASS
== NinjaTrader Grid 2026-11-01 07-57 AM.csv
data_rows=810 header_cols=24 row_lengths=[(24, 810)]
Account unique count=1 all_match_sim_backtest=True
Account values: ['Backtest']
Strategy unique count=1 values=['PraxisNoiseAreaBreakout_OppBand']
email matches total=0 by_col={}
phone-like matches total=0 by_col={}
7+digit-run matches total=0 by_col={}
PASS
== NinjaTrader Grid 2026-11-01 07-59 AM.csv
data_rows=1190 header_cols=24 row_lengths=[(24, 1190)]
Account unique count=1 all_match_sim_backtest=True
Account values: ['Backtest']
Strategy unique count=1 values=['PraxisNoiseAreaBreakout_Flat1559']
email matches total=0 by_col={}
phone-like matches total=0 by_col={}
7+digit-run matches total=0 by_col={}
PASS
== NinjaTrader Grid 2026-11-01 08-00 AM.csv
data_rows=1304 header_cols=24 row_lengths=[(24, 1304)]
Account unique count=1 all_match_sim_backtest=True
Account values: ['Backtest']
Strategy unique count=1 values=['PraxisLastHalfHourMomentum']
email matches total=0 by_col={}
phone-like matches total=0 by_col={}
7+digit-run matches total=0 by_col={}
PASS
---
NinjaTrader Grid 2026-11-01 07-10 AM.csv: name/firm grep -c -i = 0
NinjaTrader Grid 2026-11-01 07-57 AM.csv: name/firm grep -c -i = 0
NinjaTrader Grid 2026-11-01 07-59 AM.csv: name/firm grep -c -i = 0
NinjaTrader Grid 2026-11-01 08-00 AM.csv: name/firm grep -c -i = 0
```
(name/firm grep = `grep -c -i -E 'amear|bani|ahmad|mffu|rithmic|apex'`. The Account check uses `^(Backtest|Sim[0-9]*|Playback[0-9]*)$`. The 7+ digit scan covered every column, price and time columns included, and found 0 matches.)

Raw-line grep cross-check (header included):
```
NinjaTrader Grid 2026-11-01 07-10 AM.csv: raw-line email=0 phone=0 digits7=0 at-sign=0
NinjaTrader Grid 2026-11-01 07-57 AM.csv: raw-line email=0 phone=0 digits7=0 at-sign=0
NinjaTrader Grid 2026-11-01 07-59 AM.csv: raw-line email=0 phone=0 digits7=0 at-sign=0
NinjaTrader Grid 2026-11-01 08-00 AM.csv: raw-line email=0 phone=0 digits7=0 at-sign=0
```
Result: all 4 PASS. No file is held out.

### V5. Step 3: copy, hashes, cmp, check-ignore
```
pre-existing check exit=1          (no 2026-11-01 file was in evidence/ before the copy)
SRC before: SHA2-256(NinjaTrader Grid 2026-11-01 07-10 AM.csv)= 421c44e6cd9d417b432be1a5b440b0861782a3bba7e1961beba5b5421e0534bd
SRC after:  SHA2-256(NinjaTrader Grid 2026-11-01 07-10 AM.csv)= 421c44e6cd9d417b432be1a5b440b0861782a3bba7e1961beba5b5421e0534bd
COPY:       SHA2-256(/Volumes/Sensidine/Praxis.build/docs/reports/evidence/2026-11-01-ninjatrader-grid-0710am.csv)= 421c44e6cd9d417b432be1a5b440b0861782a3bba7e1961beba5b5421e0534bd
cmp exit=0
check-ignore exit=1
SRC before: SHA2-256(NinjaTrader Grid 2026-11-01 07-57 AM.csv)= 4207ea99e7f1187b54ebe45c97822409629192ed12e7ee0dbaacb241c152b6e8
SRC after:  SHA2-256(NinjaTrader Grid 2026-11-01 07-57 AM.csv)= 4207ea99e7f1187b54ebe45c97822409629192ed12e7ee0dbaacb241c152b6e8
COPY:       SHA2-256(/Volumes/Sensidine/Praxis.build/docs/reports/evidence/2026-11-01-ninjatrader-grid-0757am.csv)= 4207ea99e7f1187b54ebe45c97822409629192ed12e7ee0dbaacb241c152b6e8
cmp exit=0
check-ignore exit=1
SRC before: SHA2-256(NinjaTrader Grid 2026-11-01 07-59 AM.csv)= 5a3c4d783a44b33a18c4eb77f50444af1d4cf65ed4190038becc4c2007c868e0
SRC after:  SHA2-256(NinjaTrader Grid 2026-11-01 07-59 AM.csv)= 5a3c4d783a44b33a18c4eb77f50444af1d4cf65ed4190038becc4c2007c868e0
COPY:       SHA2-256(/Volumes/Sensidine/Praxis.build/docs/reports/evidence/2026-11-01-ninjatrader-grid-0759am.csv)= 5a3c4d783a44b33a18c4eb77f50444af1d4cf65ed4190038becc4c2007c868e0
cmp exit=0
check-ignore exit=1
SRC before: SHA2-256(NinjaTrader Grid 2026-11-01 08-00 AM.csv)= 4efd8ce8e95cc408f82d494fcf55238c25b9980b030a39eb25f4eaa5fbd180d9
SRC after:  SHA2-256(NinjaTrader Grid 2026-11-01 08-00 AM.csv)= 4efd8ce8e95cc408f82d494fcf55238c25b9980b030a39eb25f4eaa5fbd180d9
COPY:       SHA2-256(/Volumes/Sensidine/Praxis.build/docs/reports/evidence/2026-11-01-ninjatrader-grid-0800am.csv)= 4efd8ce8e95cc408f82d494fcf55238c25b9980b030a39eb25f4eaa5fbd180d9
cmp exit=0
check-ignore exit=1
-rw-------@ 1 admin  staff  256796 Nov  1 08:06 /Volumes/Sensidine/Praxis.build/docs/reports/evidence/2026-11-01-ninjatrader-grid-0710am.csv
-rw-------@ 1 admin  staff  191423 Nov  1 08:02 /Volumes/Sensidine/Praxis.build/docs/reports/evidence/2026-11-01-ninjatrader-grid-0757am.csv
-rw-------@ 1 admin  staff  261564 Nov  1 08:02 /Volumes/Sensidine/Praxis.build/docs/reports/evidence/2026-11-01-ninjatrader-grid-0759am.csv
-rw-------@ 1 admin  staff  293775 Nov  1 08:02 /Volumes/Sensidine/Praxis.build/docs/reports/evidence/2026-11-01-ninjatrader-grid-0800am.csv
```
`git check-ignore -v` printed nothing and exited 1 for each copy: **none is ignored**.

Line endings and git filters. The files use CRLF line endings. No attribute, .gitattributes file or autocrlf setting applies, and `git hash-object` gives the same value with and without filters:
```
docs/reports/evidence/2026-11-01-ninjatrader-grid-0710am.csv CRLF-lines=1191
docs/reports/evidence/2026-11-01-ninjatrader-grid-0757am.csv CRLF-lines=811
docs/reports/evidence/2026-11-01-ninjatrader-grid-0759am.csv CRLF-lines=1191
docs/reports/evidence/2026-11-01-ninjatrader-grid-0800am.csv CRLF-lines=1305
attrs exit=0                       (git check-attr -a printed nothing for any copy)
ls: .gitattributes: No such file or directory
autocrlf exit=1
90a581febb1442138805e962fca1541462b14199 90a581febb1442138805e962fca1541462b14199 docs/reports/evidence/2026-11-01-ninjatrader-grid-0710am.csv
241e718eb6ab2c425717537d68132b78de3fd15a 241e718eb6ab2c425717537d68132b78de3fd15a docs/reports/evidence/2026-11-01-ninjatrader-grid-0757am.csv
015c9c51d3248bca50e8721d424bffa8c36c7c14 015c9c51d3248bca50e8721d424bffa8c36c7c14 docs/reports/evidence/2026-11-01-ninjatrader-grid-0759am.csv
476f3adf273f192392404d2c494df26266ba0c14 476f3adf273f192392404d2c494df26266ba0c14 docs/reports/evidence/2026-11-01-ninjatrader-grid-0800am.csv
```
Note: `cp -p` kept mode 600. Git records file mode as 644 or 755, so this does not affect the bytes. A pre-commit check for CRLF or trailing whitespace, if one exists, could flag these files. I did not check for one.

Rename table:

| old name (~/Desktop) | new name (docs/reports/evidence/) | role | sha256 |
|---|---|---|---|
| `NinjaTrader Grid 2026-11-01 07-10 AM.csv` | `2026-11-01-ninjatrader-grid-0710am.csv` | baseline (PraxisNoiseAreaBreakout) | 421c44e6cd9d417b432be1a5b440b0861782a3bba7e1961beba5b5421e0534bd |
| `NinjaTrader Grid 2026-11-01 07-57 AM.csv` | `2026-11-01-ninjatrader-grid-0757am.csv` | OppBand | 4207ea99e7f1187b54ebe45c97822409629192ed12e7ee0dbaacb241c152b6e8 |
| `NinjaTrader Grid 2026-11-01 07-59 AM.csv` | `2026-11-01-ninjatrader-grid-0759am.csv` | Flat1559 | 5a3c4d783a44b33a18c4eb77f50444af1d4cf65ed4190038becc4c2007c868e0 |
| `NinjaTrader Grid 2026-11-01 08-00 AM.csv` | `2026-11-01-ninjatrader-grid-0800am.csv` | LastHalfHourMomentum | 4efd8ce8e95cc408f82d494fcf55238c25b9980b030a39eb25f4eaa5fbd180d9 |

### V6. Cited sources, checked myself
```
114:## D-2026-07-09-C — Signals Drop Dir = Dedicated Low-Privilege User (`praxispush`), Not Trader Home
121:The signal drop directory is owned by a **dedicated low-privilege macOS user `praxispush`** at the canonical path **`/Users/praxispush/praxis-signals`**. This single path is used identically by (1) the B1-a authorized_keys forced-command/rrsync chroot for the n8n push peer, (2) the B1-a sshd scoping, and (3) the B1-c Parallels VM share. It is NOT the trader's home directory.
124:- **Structural least privilege.** A compromised n8n push key reaches a directory that contains nothing but signals ...
129:**Impact:** B1-a's `SIGNALS_DIR` = `/Users/praxispush/praxis-signals`; ...
133:## D-2026-07-09-D — n8n Runs LOCALLY on the Mac for Block-1 Build-First; ...
151:- **B1-c (Praxis_build-dnt)** — still required: the Mac signals dir + Parallels VM-share scope + launchd. Note: D-2026-07-09-C's dedicated-`praxispush`-user choice was motivated partly by remote-push-key compromise (now moot with local n8n) and partly by clean VM-share-scope (still valid); whether local n8n writes as `praxispush` vs the trader user is revisited at B1-c execution.
1973:- **D1** (:17–21). "Default-decide." ... "takes the recommended option, logs it as "decided by master under D-2026-11-08-D D1", and continues." ...
1974:- **D2** (:22–26). "Only four things stop and wait for Amear's word": "(a) spending money"; "(b) switching live trading on, or any order path to a funded account"; "(c) changing circuit-breaker values while real money is at stake"; "(d) installing keys, credentials or agent permissions." "Everything else is D1."
1979:*Section "WORK ORDER" (:39).*          <- not D8 (the brief's cite)
1982:- **D8** (:55–64). ... "(6) the five P0 guard beads are accepted as known risk while only docs/specs move; fixed before any Block 3 code that can place orders." ... "(8) "final step of this build" = Block 4 paper pass on MFFU sim (the standing proof-of-concept ruling). Block 5 live is a separate sign-off under D2(b)."
765:- **F1** (`specs/SPEC_RUBRIC.md:17-28`), **F2** (`:30-43`), **F4** (`:59-70`): untouched. FROZEN.
```
Rubric (current file): `:17` is `## FROZEN — nothing downstream may proceed until these clear`, `:19` is `### F1 — Signal-path topology vs. circuit-breaker placement` and `:61` is `### F4 — MFFU automation compliance` (from `sed -n '10,72p' | grep -n`, offset +9). O2:
```
    95	### O2 — `praxispush` provisioning
    96	The signal directory was specified as a dedicated low-privilege macOS user, the
    97	rationale being structural blast-radius limitation. The build report places it
    98	at `~/praxis-signals/`, surfacing in Windows as `C:\Mac\Home\praxis-signals\` —
    99	the primary account home mounted into the VM. **Required:** either the user
   100	exists, or a DECISIONS.md entry records the removal and its accepted risk.
   101	A security requirement that stopped being mentioned is not a resolved one.
```
VM design spec:
```
    45	- **Mac:** `~/praxis-signals/vm-agent/` (on the Parallels share, outside the git repo).
    46	- **Windows:** `C:\Mac\Home\praxis-signals\vm-agent\`
    47	- **Prefix verified** 2026-07-25: `Test-Path C:\Mac\Home\praxis-signals\b2-data` → `True`
    48	  in the Parallels Windows 11 ARM VM. So `C:\Mac\Home\praxis-signals\` is the correct
```
Bead and sweep row:
```
$ bd show Praxis_build-zd4   (excerpt)
○ Praxis_build-zd4 · praxispush security requirement silently dropped: re-provision the low-priv macOS user + move the signal drop dir, OR formally log the removal decision   [● P1 · OPEN]
  ACCEPTANCE: EITHER provision praxispush + relocate the drop dir under it
  before the B1-a forced-command step, OR a DECISIONS entry explicitly
  recording the decision to defer/drop it with rationale. ...
$ sed -n '81p' docs/reports/2026-11-09-d11-sweep-manager.md
| G30 | ""provision praxispush + relocate the drop dir ... OR a DECISIONS entry explicitly recording the decision to defer/drop it ... Trader-owned action"" (raised 2026-07-25) | bd:Praxis_build-zd4 (rows W4-36) | WAITING | D2-AMBIGUOUS: provisioning a macOS user is close to D2(d) "credentials"; recording a deferral installs nothing. | manager's proposal: record the deferral and its accepted risk in DECISIONS.md (O2 allows this, SPEC_RUBRIC.md:93-94) | master may close under D1 by recording the deferral; provisioning stays D2(d)-adjacent |
```
Observations made on 2026-11-10:
```
$ id praxispush; echo "id exit=$?"
id: praxispush: no such user
id exit=1
$ ls -ld ~/praxis-signals/; echo "ls exit=$?"
drwxr-xr-x@ 14 admin  staff  448 Nov 10 01:54 /Users/admin/praxis-signals/
ls exit=0
$ date -u
2026-11-10T09:44:00Z
```

### V7. DECISIONS.md append (entry D-2026-11-10-A)
```
$ cat /tmp/hk2b-scripts/entry.md >> DECISIONS.md && wc -l DECISIONS.md && git diff --numstat HEAD -- DECISIONS.md
    2041 DECISIONS.md
17	0	DECISIONS.md
$ git show HEAD:DECISIONS.md > /tmp/hk2b-final/DECISIONS.md && tail -n +2025 DECISIONS.md >> /tmp/hk2b-final/DECISIONS.md && cmp /tmp/hk2b-final/DECISIONS.md DECISIONS.md; echo "cmp exit=$?"
cmp exit=0
$ grep -n 'D-2026-11-10' DECISIONS.md
2026:## 2026-11-10 — D-2026-11-10-A: praxispush low-privilege user DEFERRED, accepted risk recorded (bead Praxis_build-z
$ sed -n '1,2024p' DECISIONS.md | cmp - <(git show HEAD:DECISIONS.md); echo "head-prefix cmp exit=$?"
head-prefix cmp exit=0
```
Entry range: lines **2025-2041**. Line 2025 is the blank separator and the heading is at :2026, matching the blank-line-then-`## ` layout of the entries above. Lines 1-2024 are byte-identical to HEAD.

### V8. MANIFEST.md
```
$ sed -n '1,344p' MANIFEST.md | shasum -a 256      (before)
89962c893bcd1cfebfe8c0e7c92b87a6fa091c9a1ff5c56010a67bb7183ec2e5  -
$ sed -n '1,344p' MANIFEST.md | shasum -a 256      (after)
89962c893bcd1cfebfe8c0e7c92b87a6fa091c9a1ff5c56010a67bb7183ec2e5  -
$ wc -l MANIFEST.md
     352 MANIFEST.md
$ grep -n '' MANIFEST.md | tail -n 10 | cut -c1-200
343:| /docs/reports/2026-11-10-scrub-forward-adversarial.md | Report | 2 | 2026-11-10 | ADVERSARIAL worker report for unit 2026-11-10-scrub-forward (bead Praxis_build-8ux): independent term re-derivat
344:| /docs/reports/2026-11-07-rulings-filing-manager.md | Report | 2 | 2026-11-10 | MODIFIED (bead Praxis_build-8ux Correction 1; DECISION_LOG row 2026-11-10T09:24:00Z): append-only pointer note at t
345:| /docs/reports/evidence/2026-11-01-ninjatrader-grid-0710am.csv | Evidence | 2 | 2026-11-10 | baseline grid (PraxisNoiseAreaBreakout) trade list, NinjaTrader backtest export, Account column Backte
346:| /docs/reports/evidence/2026-11-01-ninjatrader-grid-0757am.csv | Evidence | 2 | 2026-11-10 | OppBand grid (PraxisNoiseAreaBreakout_OppBand) trade list, NinjaTrader backtest export, Account column
347:| /docs/reports/evidence/2026-11-01-ninjatrader-grid-0759am.csv | Evidence | 2 | 2026-11-10 | Flat1559 grid (PraxisNoiseAreaBreakout_Flat1559) trade list, NinjaTrader backtest export, Account colu
348:| /docs/reports/evidence/2026-11-01-ninjatrader-grid-0800am.csv | Evidence | 2 | 2026-11-10 | LastHalfHourMomentum grid (PraxisLastHalfHourMomentum) trade list, NinjaTrader backtest export, Accoun
349:| /docs/reports/2026-11-10-housekeeping-2b-worker1.md | Report | 2 | 2026-11-10 | BUILD worker report for unit 2026-11-10-housekeeping-2b (master under D-2026-11-08-D D1, DECISION_LOG row 2026-11-
350:| /docs/reports/2026-11-10-housekeeping-2b-adversarial.md | Report | 2 | 2026-11-10 | ADVERSARIAL worker report for unit 2026-11-10-housekeeping-2b (master under D-2026-11-08-D D1, DECISION_LOG ro
351:| /docs/reports/2026-11-10-housekeeping-2b-manager.md | Report | 2 | 2026-11-10 | Manager report for unit 2026-11-10-housekeeping-2b (master under D-2026-11-08-D D1, DECISION_LOG row 2026-11-10T09
352:| /DECISIONS.md | Log | 2 | 2026-11-10 | MODIFIED (unit 2026-11-10-housekeeping-2b; master under D-2026-11-08-D D1, DECISION_LOG row 2026-11-10T09:43:00Z): entry D-2026-11-10-A (praxispush low-pri
```
The third column is Phase (header row 3: `| File Path | Type | Phase | Date Created | Purpose |`). The last rows use 2, so the new rows use 2.

### V9. The brief's 307-314 check: exit=1, from earlier work and not this unit
```
$ diff <(git show HEAD:MANIFEST.md | sed -n '307,314p') <(sed -n '307,314p' MANIFEST.md); echo exit=$?
1,8c1,8
< | /docs/reports/2026-11-09-d11-sweep-manager.md | Report | 2 | 2026-11-09 | ... (HEAD rows 307-314: d11 sweep, rubric unit, vm-handoff, fusion walkthrough, amendment-2, praxis-manager.md, c7 probe control, c7 probe test)
---
> | /docs/specs/2026-11-06-walk-forward-values.md | Spec | 2 | 2026-11-08 | AMENDMENT ROW ... (working-tree rows 307-314: the parked U7 unit's 8 rows, ending with the u7-diff-of-record.patch row)
exit=1
```
(The full diff output was printed in this session; the diff body above is cut to one representative line per side. The `exit=1` line is verbatim.) The cause:
```
$ git diff --numstat HEAD -- MANIFEST.md
16	0	MANIFEST.md
$ git diff -U0 HEAD -- MANIFEST.md | grep '^@@'
@@ -306,0 +307,8 @@
@@ -336,0 +345,8 @@
$ diff <(git show HEAD:MANIFEST.md | sed -n '307,314p') <(sed -n '315,322p' MANIFEST.md); echo "HEAD307-314 vs WT315-322 exit=$?"
HEAD307-314 vs WT315-322 exit=0
```
The parked unit's 8 rows were inserted after HEAD line 306, before this unit started. The 1-344 hash is the same before and after my edit, so the insertion predates me. HEAD's rows 307-336 now sit at 315-344, unchanged. This unit's only hunk is `@@ -336,0 +345,8 @@`: 8 rows appended at 345-352. The brief's check assumed the parked rows sat at 307-314 in HEAD as well. They do not; they exist only in the working tree.

### V10. Index unchanged
```
$ git diff --cached --name-only
docs/reports/evidence/2026-10-28-mffu-davi-reply.png
$ git status --short -- DECISIONS.md MANIFEST.md docs/reports/evidence/ docs/reports/2026-11-10-housekeeping-2b-worker1.md
 M DECISIONS.md
 M MANIFEST.md
A  docs/reports/evidence/2026-10-28-mffu-davi-reply.png
?? docs/reports/evidence/2026-11-01-ninjatrader-grid-0710am.csv
?? docs/reports/evidence/2026-11-01-ninjatrader-grid-0757am.csv
?? docs/reports/evidence/2026-11-01-ninjatrader-grid-0759am.csv
?? docs/reports/evidence/2026-11-01-ninjatrader-grid-0800am.csv
?? docs/reports/evidence/2026-11-09-u7-diff-of-record.patch
```
(The u7 patch was untracked before this unit and belongs to the parked unit. That status was run before this report existed.)

## Files staged
None. The brief forbids `git add`, and the index still holds exactly the one PNG.

Files created:
- `docs/reports/evidence/2026-11-01-ninjatrader-grid-0710am.csv`, `-0757am.csv`, `-0759am.csv`, `-0800am.csv` (untracked)
- `docs/reports/2026-11-10-housekeeping-2b-worker1.md` (this report, untracked)

Files changed:
- `DECISIONS.md`: entry **D-2026-11-10-A** appended at lines **2025-2041** (heading :2026); lines 1-2024 unchanged.
- `MANIFEST.md`: rows **345-352** appended (345-348 CSVs, 349 this report, 350 adversarial report, 351 manager report, 352 DECISIONS.md MODIFIED); lines 1-344 unchanged.

Files held out: none (all 4 passed content safety).

Not touched: specs/SPEC_RUBRIC.md, DECISION_LOG.md, HANDOFF.md, STATUS.md, the Desktop files (read and copied only; source hashes unchanged), bead Praxis_build-zd4, macOS users and permissions, .gitignore.

Also reported, outside scope and not fixed:
1. The brief's D8 cite (:1979) is wrong; D8 is at DECISIONS.md:1982.
2. The brief's 307-314 MANIFEST check cannot pass while the parked rows are uncommitted (V9).
3. Rubric O2's "Required" (:99-100) asks for an entry that records a *removal*. D-2026-11-10-A records a *deferral* and says it does not grade O2, which stays OPEN as instructed.

## Result: PASS

## Fix 1 (adversarial defects 3a 3b 3c 6a 6b)

Mode: BUILD (fix). Scope: entry D-2026-11-10-A at the end of DECISIONS.md, its MANIFEST row (:352), the /tmp landing blob, this section.

Changes:
- 3a: Trigger is now "the user is provisioned AND the drop dir is moved under it" to `/Users/praxispush/praxis-signals` (DECISIONS.md:121), quoting the first branch of bead `Praxis_build-zd4` acceptance.
- 3b: "or a replacement control is ruled by Amear" removed. Replaced by D1 (DECISIONS.md:1973), quoted exactly.
- 3c: sim/test limit now stated as record-level: the rulings on record (D2(b) :1974; F1/F4 FROZEN :765; D8(8) :1982) do not permit an order path to a funded account; not observed, not tested.
- 6a: "shared into the Windows VM" removed. New paragraphs set Parallels-era (rubric :97-99, VM design :46-48, B1-c close reason) and Fusion-era (DECISIONS.md:1004 item 3, :1019, :1275 Ruling 10) records side by side without picking. OBSERVED facts (`id`, `ls -ld`) kept; entry says it did not observe how or whether the current VM reaches the drop dir. Accepted risk restated as the brief gave it.
- 6b: new paragraph "Where B1-c and B1-a stand" with bd outputs (dnt CLOSED, 0 praxispush mentions; dgt DEFERRED to 2027-01-01).
- Entry range changed 2025-2041 -> 2025-2045 (heading :2026). MANIFEST :352 updated to match.

Source checks (each quoted string grepped in DECISIONS.md lines 1-2024; line numbers printed):

```
Fusion shared folders unavailable => 1004 1017 
admin Read & Write => 1004 
mapped as Z: => 1004 
unmap Z: and turn the share off before real money => 1004 1041 1085 1275 1473 
unmap Z: and turn off the SMB share => 1234 1275 
Amear may reverse any such decision later; the reversal is filed like any ruling. => 1973 
rubric :98-99 "the primary account home mounted into the VM" count: 1
dnt close-reason quote count: 1 (rerun; the first run printed 0 because of a shell quoting slip in the check, not in the source)
```

Verification output (pasted):

```
$ sed -n 2025,$p DECISIONS.md

## 2026-11-10 — D-2026-11-10-A: praxispush low-privilege user DEFERRED, accepted risk recorded (bead Praxis_build-zd4; rubric O2)

**Status:** Decided by master under D-2026-11-08-D D1; changeable by Amear.
**Authority:** DECISION_LOG.md:795 (row 2026-11-10T09:43:00Z, praxis-master, item (2) G30); D11 sweep row G30 (`docs/reports/2026-11-09-d11-sweep-manager.md`:81); D-2026-11-08-D D1 and D2 (DECISIONS.md:1973–1974).

**What was specified.** D-2026-07-09-C (DECISIONS.md:114–129): the signal drop directory is owned by "a **dedicated low-privilege macOS user `praxispush`**" at `/Users/praxispush/praxis-signals`, the one path used by the B1-a forced-command/rrsync chroot, the B1-a sshd scoping and the B1-c Parallels VM share (:121). Its first rationale is "Structural least privilege" (:124). Context, D-2026-07-09-D (DECISIONS.md:151): the choice "was motivated partly by remote-push-key compromise (now moot with local n8n) and partly by clean VM-share-scope (still valid)", and whether local n8n writes as `praxispush` or the trader user "is revisited at B1-c execution."

**Where B1-c and B1-a stand.** That revisit is not ahead. B1-c (bead `Praxis_build-dnt`) is CLOSED: on 2026-11-10 `bd show Praxis_build-dnt` printed "[● P1 · CLOSED]". The bead does not mention `praxispush`, close reason included: `bd show Praxis_build-dnt | grep -c -i praxispush` printed 0. B1-a (bead `Praxis_build-dgt`) is DEFERRED: on 2026-11-10 `bd show Praxis_build-dgt` printed "[● P1 · DEFERRED]" and "Deferred: 2027-01-01".

**What exists now (OBSERVED 2026-11-10).** There is no `praxispush` user: `id praxispush` printed `id: praxispush: no such user` (exit 1). The drop dir is in the primary account's home, owned by admin: `ls -ld /Users/admin/praxis-signals/` printed `drwxr-xr-x@ 14 admin  staff  448 Nov 10 01:54 /Users/admin/praxis-signals/`. This entry did not observe how, or whether, the current VM reaches the drop dir.

**How the VM reaches it, per the records.** The records differ; this entry does not pick one. Parallels era: the rubric (`specs/SPEC_RUBRIC.md`:97–99) and the VM workspace design (`docs/specs/2026-07-25-vm-agent-delegation-workspace-design.md`:46–48, prefix verified there on 2026-07-25 in the Parallels VM) give the Windows path `C:\Mac\Home\praxis-signals\`, "the primary account home mounted into the VM". The B1-c close reason (`bd show Praxis_build-dnt`) says instead: "AC2 Parallels share scoped to /Users/admin/praxis-signals only + whole-home 'admin' home share unchecked". Fusion era: D-2026-11-06-A item 3 (DECISIONS.md:1004, REPORTED) says "Fusion shared folders unavailable"; `Praxis.build` is shared over SMB with "admin Read & Write" and is "mapped as Z:" in the VM. DECISIONS.md:1019 notes that D-072 and item 3 differ. The go-live checklist says to "unmap Z: and turn the share off before real money" (DECISIONS.md:1004) and to "unmap Z: and turn off the SMB share" (Ruling 10, DECISIONS.md:1275).

**Decision.** The `praxispush` user is DEFERRED, not dropped. Trigger: the user is provisioned AND the drop dir is moved under it, to the canonical path `/Users/praxispush/praxis-signals` (D-2026-07-09-C, DECISIONS.md:121). This is the first branch of bead `Praxis_build-zd4`'s acceptance: "provision praxispush + relocate the drop dir under it before the B1-a forced-command step". Both must be done before whichever comes first of (1) any Block 3 code that can place orders, using the wording D8(6) gives for the five P0 guard beads: "fixed before any Block 3 code that can place orders" (DECISIONS.md:1982); and (2) the B1-a forced-command step, as the same acceptance names it: "before the B1-a forced-command step". Amear may reverse or replace this decision under D1 (DECISIONS.md:1973): "Amear may reverse any such decision later; the reversal is filed like any ruling."

**Accepted risk, plainly.** Until the trigger, the dedicated-user boundary of D-2026-07-09-C does not exist. Anything that can write as the primary account (admin), or through any share that exposes that directory to the VM, can drop a signal file. The rulings on record do not permit an order path to a funded account: D2(b) keeps "switching live trading on, or any order path to a funded account" behind Amear's word (DECISIONS.md:1974); F1 (signal-path topology vs. circuit-breaker placement) and F4 (MFFU automation compliance) are FROZEN (DECISIONS.md:765; both sit under the rubric's FROZEN heading, `specs/SPEC_RUBRIC.md`:17, :19, :61); and D8(8) makes the "final step of this build" a "Block 4 paper pass on MFFU sim", with "Block 5 live is a separate sign-off under D2(b)" (DECISIONS.md:1982). This entry did not observe the running system. So the limit to sim and test is a record-level limit, not a tested one.

**What this entry does not do.** It provisions no user, changes no permissions and installs nothing; provisioning is D2(d)-adjacent ("installing keys, credentials or agent permissions", DECISIONS.md:1974; sweep row G30, :81) and stays with Amear. It does not edit the rubric: O2 (`specs/SPEC_RUBRIC.md`:95–101) stays OPEN, and this entry does not grade it. Bead `Praxis_build-zd4` stays open; the master updates it after the commit.

S13: Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
$ cmp HEAD vs head -n 2024
exit=0
$ rebuild
cmp=0
$ numstat
21	0	DECISIONS.md
16	0	MANIFEST.md
$ manifest rows
350:| /docs/reports/2026-11-10-housekeeping-2b-adversarial.md | Report | 2 | 2026-11-10 | ADVERSARIAL worker report for unit 2026-11-10-housekeeping-2b (master under D-2026-11-08-D D1, DECISION_LOG row 2026-11-10T09:43:00Z): break attempts on the G18 trade-list copies and the G30 DECISIONS.md entry 
352:| /DECISIONS.md | Log | 2 | 2026-11-10 | MODIFIED (unit 2026-11-10-housekeeping-2b; master under D-2026-11-08-D D1, DECISION_LOG row 2026-11-10T09:43:00Z): entry D-2026-11-10-A (praxispush low-privilege user DEFERRED, accepted risk recorded; bead Praxis_build-zd4; rubric O2) appended at lines 20
$ S13 count
1
$ cached
docs/reports/evidence/2026-10-28-mffu-davi-reply.png
$ MANIFEST 1-344 unchanged vs HEAD
/dev/fd/13 /dev/fd/15 differ: char 142364, line 307
exit=1
$ MANIFEST diff 345+
+| /docs/specs/2026-11-06-walk-forward-values.md | Spec | 2 
+| /docs/specs/2026-11-05-walk-forward-spec.md | Spec | 3 | 
+| /docs/reports/2026-11-08-wf-spec-amendment-manager.md | R
+| /docs/reports/2026-11-08-wf-spec-amendment-correction-1-m
+| /docs/reports/2026-11-08-wf-spec-amendment-correction-2-m
+| /docs/reports/2026-11-08-wf-spec-amendment-correction-3-m
+| /docs/reports/2026-11-09-wf-spec-amendment-resume-manager
+| /docs/reports/evidence/2026-11-09-u7-diff-of-record.patch
+| /docs/reports/evidence/2026-11-01-ninjatrader-grid-0710am
+| /docs/reports/evidence/2026-11-01-ninjatrader-grid-0757am
+| /docs/reports/evidence/2026-11-01-ninjatrader-grid-0759am
+| /docs/reports/evidence/2026-11-01-ninjatrader-grid-0800am
+| /docs/reports/2026-11-10-housekeeping-2b-worker1.md | Rep
+| /docs/reports/2026-11-10-housekeeping-2b-adversarial.md |
+| /docs/reports/2026-11-10-housekeeping-2b-manager.md | Rep
+| /DECISIONS.md | Log | 2 | 2026-11-10 | MODIFIED (unit 202
$ verification sources
id: praxispush: no such user
exit=1
drwxr-xr-x@ 14 admin  staff  448 Nov 10 01:54 /Users/admin/praxis-signals/
✓ Praxis_build-dnt · B1-c: Mac signals layout + VM share + launchd reconciliation   [● P1 · CLOSED]
Owner: Amear Bani-Ahmad · Assignee: Amear Bani-Ahmad · Type: task
Created: 2026-07-09 · Started: 2026-07-09 · Updated: 2026-07-09
0
❄ Praxis_build-dgt · B1-a: WireGuard tunnel + scoped SSH into signals drop   [● P1 · DEFERRED]
Owner: Amear Bani-Ahmad · Assignee: Amear Bani-Ahmad · Type: task
Created: 2026-07-09 · Started: 2026-07-09 · Updated: 2026-07-09 · Deferred: 2027-01-01
  ACCEPTANCE: EITHER provision praxispush + relocate the drop dir under it    
  before the B1-a forced-command step, OR a DECISIONS entry explicitly        
  recording the decision to defer/drop it with rationale. Trader-owned action 
```

Notes:
- MANIFEST lines 1-344 differ from HEAD at line 307. That is the pre-existing uncommitted parked rows (see V9 above), not this fix: numstat shows 0 deleted lines, and this fix touched only :352 (sed on line 352).
- Bead zd4 acceptance has a second branch: "OR a DECISIONS entry explicitly recording the decision to defer/drop it with rationale." The removed phrase in 3b may have been a paraphrase of that branch. Per brief, the entry now cites D1 instead. Flagged for the manager, not acted on.
- Staged set unchanged (only the PNG, staged before this unit). Nothing added, reset or committed.

## Fix 1 Result: PASS

## Fix 2 (round-2 adversarial defects)

Mode: BUILD (fix 2). Scope: entry D-2026-11-10-A only (DECISIONS.md:2025-2045), /tmp/hk2b-final blob, this report. Three in-line edits; no lines added, so range stays 2025-2045 and MANIFEST.md:352 is unchanged.

### Sources checked before use (pasted)

```
$ sed -n 117p;124p;125p DECISIONS.md
**Status:** LOCKED (trader-chosen 2026-07-09)
- **Structural least privilege.** A compromised n8n push key reaches a directory that contains nothing but signals — no documents, no repo, no credentials. The trader-home option only stays safe while everything else is configured correctly; the dedicated user is safe even when something is misconfigured. Same logic as the circuit breakers: remove the failure surface, don't rely on correct behavior.
- **Retires the B1-0 finding structurally.** The B1-0 spike accidentally shared the entire Mac home into the VM (`\\psf\Home` / `Z:\`). A dedicated user makes that class of over-exposure impossible to repeat — the share, the SSH chroot, and the forced-command all point at the same signals-only dir.
$ sed -n 23,24p;95,101p specs/SPEC_RUBRIC.md
**Why frozen.** Block 3 specifies the breakers as n8n workflow gates that
terminate before the file-write node. Deviation A moved strategy logic into
### O2 — `praxispush` provisioning
The signal directory was specified as a dedicated low-privilege macOS user, the
rationale being structural blast-radius limitation. The build report places it
at `~/praxis-signals/`, surfacing in Windows as `C:\Mac\Home\praxis-signals\` —
the primary account home mounted into the VM. **Required:** either the user
exists, or a DECISIONS.md entry records the removal and its accepted risk.
A security requirement that stopped being mentioned is not a resolved one.
$ grep -n -i blast specs/SPEC_RUBRIC.md
97:rationale being structural blast-radius limitation. The build report places it
$ sed -n 46,48p docs/specs/2026-07-25-vm-agent-delegation-workspace-design.md
- **Windows:** `C:\Mac\Home\praxis-signals\vm-agent\`
- **Prefix verified** 2026-07-25: `Test-Path C:\Mac\Home\praxis-signals\b2-data` → `True`
  in the Parallels Windows 11 ARM VM. So `C:\Mac\Home\praxis-signals\` is the correct
$ grep -c "the primary account home mounted into the VM" <design doc>
0
```

Deviation from brief: brief cited SPEC_RUBRIC.md:96 for "structural blast-radius limitation"; grep shows it is at :97 (line 96 is "The signal directory was specified as a dedicated low-privilege macOS user, the"). Entry cites :97. The rubric Windows path is at :98 and the quote at :99, so the rubric cite in "How the VM reaches it" is now :98-99 (was :97-99).

### Edits

1. "How the VM reaches it": quote "the primary account home mounted into the VM" now attributed to the rubric alone (:99); design doc :46-48 cited only for `C:\Mac\Home\praxis-signals\` and its 2026-07-25 prefix check, with "it does not use the rubric's wording".
2. "What was specified": added the LOCKED-status sentence citing DECISIONS.md:117.
3. "Accepted risk, plainly": added Blast radius sentence (:124, :125, rubric O2 :97) and Breakers sentence (rubric :23-24, labelled "inference from that text, not tested"). Rest of the paragraph unchanged.

### Verification (pasted)

```
$ sed -n 2025,$p DECISIONS.md

## 2026-11-10 — D-2026-11-10-A: praxispush low-privilege user DEFERRED, accepted risk recorded (bead Praxis_build-zd4; rubric O2)

**Status:** Decided by master under D-2026-11-08-D D1; changeable by Amear.
**Authority:** DECISION_LOG.md:795 (row 2026-11-10T09:43:00Z, praxis-master, item (2) G30); D11 sweep row G30 (`docs/reports/2026-11-09-d11-sweep-manager.md`:81); D-2026-11-08-D D1 and D2 (DECISIONS.md:1973–1974).

**What was specified.** D-2026-07-09-C (DECISIONS.md:114–129): the signal drop directory is owned by "a **dedicated low-privilege macOS user `praxispush`**" at `/Users/praxispush/praxis-signals`, the one path used by the B1-a forced-command/rrsync chroot, the B1-a sshd scoping and the B1-c Parallels VM share (:121). Its first rationale is "Structural least privilege" (:124). Context, D-2026-07-09-D (DECISIONS.md:151): the choice "was motivated partly by remote-push-key compromise (now moot with local n8n) and partly by clean VM-share-scope (still valid)", and whether local n8n writes as `praxispush` or the trader user "is revisited at B1-c execution." D-2026-07-09-C's status is "LOCKED (trader-chosen 2026-07-09)" (DECISIONS.md:117); this entry does not change it; it records that it is not yet implemented and when it must be.

**Where B1-c and B1-a stand.** That revisit is not ahead. B1-c (bead `Praxis_build-dnt`) is CLOSED: on 2026-11-10 `bd show Praxis_build-dnt` printed "[● P1 · CLOSED]". The bead does not mention `praxispush`, close reason included: `bd show Praxis_build-dnt | grep -c -i praxispush` printed 0. B1-a (bead `Praxis_build-dgt`) is DEFERRED: on 2026-11-10 `bd show Praxis_build-dgt` printed "[● P1 · DEFERRED]" and "Deferred: 2027-01-01".

**What exists now (OBSERVED 2026-11-10).** There is no `praxispush` user: `id praxispush` printed `id: praxispush: no such user` (exit 1). The drop dir is in the primary account's home, owned by admin: `ls -ld /Users/admin/praxis-signals/` printed `drwxr-xr-x@ 14 admin  staff  448 Nov 10 01:54 /Users/admin/praxis-signals/`. This entry did not observe how, or whether, the current VM reaches the drop dir.

**How the VM reaches it, per the records.** The records differ; this entry does not pick one. Parallels era: the rubric (`specs/SPEC_RUBRIC.md`:98–99) gives the Windows path `C:\Mac\Home\praxis-signals\` and calls it "the primary account home mounted into the VM" (:99). The VM workspace design (`docs/specs/2026-07-25-vm-agent-delegation-workspace-design.md`:46–48) gives the same Windows path `C:\Mac\Home\praxis-signals\` and records its prefix check on 2026-07-25 in the Parallels VM; it does not use the rubric's wording. The B1-c close reason (`bd show Praxis_build-dnt`) says instead: "AC2 Parallels share scoped to /Users/admin/praxis-signals only + whole-home 'admin' home share unchecked". Fusion era: D-2026-11-06-A item 3 (DECISIONS.md:1004, REPORTED) says "Fusion shared folders unavailable"; `Praxis.build` is shared over SMB with "admin Read & Write" and is "mapped as Z:" in the VM. DECISIONS.md:1019 notes that D-072 and item 3 differ. The go-live checklist says to "unmap Z: and turn the share off before real money" (DECISIONS.md:1004) and to "unmap Z: and turn off the SMB share" (Ruling 10, DECISIONS.md:1275).

**Decision.** The `praxispush` user is DEFERRED, not dropped. Trigger: the user is provisioned AND the drop dir is moved under it, to the canonical path `/Users/praxispush/praxis-signals` (D-2026-07-09-C, DECISIONS.md:121). This is the first branch of bead `Praxis_build-zd4`'s acceptance: "provision praxispush + relocate the drop dir under it before the B1-a forced-command step". Both must be done before whichever comes first of (1) any Block 3 code that can place orders, using the wording D8(6) gives for the five P0 guard beads: "fixed before any Block 3 code that can place orders" (DECISIONS.md:1982); and (2) the B1-a forced-command step, as the same acceptance names it: "before the B1-a forced-command step". Amear may reverse or replace this decision under D1 (DECISIONS.md:1973): "Amear may reverse any such decision later; the reversal is filed like any ruling."

**Accepted risk, plainly.** Until the trigger, the dedicated-user boundary of D-2026-07-09-C does not exist. Anything that can write as the primary account (admin), or through any share that exposes that directory to the VM, can drop a signal file. Blast radius: D-2026-07-09-C's rationale (DECISIONS.md:124) is that with the dedicated user a compromised writer "reaches a directory that contains nothing but signals — no documents, no repo, no credentials"; without it, a writer acting as the primary account is not held to that directory; the B1-0 spike "accidentally shared the entire Mac home into the VM" (DECISIONS.md:125), and the rubric names the rationale "structural blast-radius limitation" (O2, `specs/SPEC_RUBRIC.md`:97); that is the risk this deferral accepts. Breakers: the rubric says "Block 3 specifies the breakers as n8n workflow gates that terminate before the file-write node" (`specs/SPEC_RUBRIC.md`:23–24), so a file written straight into the drop dir would not pass those gates (inference from that text, not tested). The rulings on record do not permit an order path to a funded account: D2(b) keeps "switching live trading on, or any order path to a funded account" behind Amear's word (DECISIONS.md:1974); F1 (signal-path topology vs. circuit-breaker placement) and F4 (MFFU automation compliance) are FROZEN (DECISIONS.md:765; both sit under the rubric's FROZEN heading, `specs/SPEC_RUBRIC.md`:17, :19, :61); and D8(8) makes the "final step of this build" a "Block 4 paper pass on MFFU sim", with "Block 5 live is a separate sign-off under D2(b)" (DECISIONS.md:1982). This entry did not observe the running system. So the limit to sim and test is a record-level limit, not a tested one.

**What this entry does not do.** It provisions no user, changes no permissions and installs nothing; provisioning is D2(d)-adjacent ("installing keys, credentials or agent permissions", DECISIONS.md:1974; sweep row G30, :81) and stays with Amear. It does not edit the rubric: O2 (`specs/SPEC_RUBRIC.md`:95–101) stays OPEN, and this entry does not grade it. Bead `Praxis_build-zd4` stays open; the master updates it after the commit.

S13: Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
$ cmp <(git show HEAD:DECISIONS.md) <(head -n 2024 DECISIONS.md); echo exit=$?
exit=0
$ rebuild /tmp/hk2b-final/DECISIONS.md and cmp
cmp=0
$ git diff --numstat HEAD -- DECISIONS.md
21	0	DECISIONS.md
$ wc -l DECISIONS.md
    2045 DECISIONS.md
$ sed -n 352p MANIFEST.md | cut -c1-300
| /DECISIONS.md | Log | 2 | 2026-11-10 | MODIFIED (unit 2026-11-10-housekeeping-2b; master under D-2026-11-08-D D1, DECISION_LOG row 2026-11-10T09:43:00Z): entry D-2026-11-10-A (praxispush low-privilege user DEFERRED, accepted risk recorded; bead Praxis_build-zd4; rubric O2) appended at lines 2025-2
$ S13 count
1
$ git diff --cached --name-only
docs/reports/evidence/2026-10-28-mffu-davi-reply.png
```

Files staged by this fix: none (index unchanged; the one cached path predates this unit).

Result (Fix 2): PASS

S13 (added by the manager under Correction 1, 2026-11-10): Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
