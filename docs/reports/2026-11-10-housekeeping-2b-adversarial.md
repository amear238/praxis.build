# 2026-11-10 housekeeping-2b — ADVERSARIAL

## Task
Adversarial review of unit 2026-11-10-housekeeping-2b (artifacts A-D).

## Mode
ADVERSARIAL

## Criterion
DECISION_LOG.md:795; archive rule; SPEC_RUBRIC O2, S1, S2, S6, S8, S13.

## Process log

About 22 tool calls. I wrote the skeleton first and appended each check as it finished. Read-only apart from this report: no git add, reset, rm, stash, checkout or commit. No CSV data rows are pasted, only the header, counts and unique values of label columns. I read the authority at `sed -n 795p` only. Note on Checks 1-2 and 4-5: some outputs are condensed into one row per file, with every value copied verbatim from the raw tool output.

## Check 1 — CSV byte identity / never committed

Command: per pair `openssl dgst -sha256`, `cmp`, `git hash-object`, `git cat-file -e`, `wc -c`, `git log --all -- <copy>`; then `sed -n 29,32p docs/reports/2026-11-01-three-strategy-results.md`.

```
0710am sha256 copy=desktop=421c44e6cd9d417b432be1a5b440b0861782a3bba7e1961beba5b5421e0534bd cmp=0 oid=90a581febb1442138805e962fca1541462b14199 exists=1 bytes 256796/256796
0757am sha256 copy=desktop=4207ea99e7f1187b54ebe45c97822409629192ed12e7ee0dbaacb241c152b6e8 cmp=0 oid=241e718eb6ab2c425717537d68132b78de3fd15a exists=1 bytes 191423/191423
0759am sha256 copy=desktop=5a3c4d783a44b33a18c4eb77f50444af1d4cf65ed4190038becc4c2007c868e0 cmp=0 oid=015c9c51d3248bca50e8721d424bffa8c36c7c14 exists=1 bytes 261564/261564
0800am sha256 copy=desktop=4efd8ce8e95cc408f82d494fcf55238c25b9980b030a39eb25f4eaa5fbd180d9 cmp=0 oid=476f3adf273f192392404d2c494df26266ba0c14 exists=1 bytes 293775/293775
git log --all -- <copy>: (empty for all four)

three-strategy-results.md:29-32 recorded hashes:
07-10 AM baseline grid 421c44e6cd9d417b432be1a5b440b0861782a3bba7e1961beba5b5421e0534bd
07-57 AM OppBand grid  4207ea99e7f1187b54ebe45c97822409629192ed12e7ee0dbaacb241c152b6e8
07-59 AM Flat1559 grid 5a3c4d783a44b33a18c4eb77f50444af1d4cf65ed4190038becc4c2007c868e0
08-00 AM LHHM grid     4efd8ce8e95cc408f82d494fcf55238c25b9980b030a39eb25f4eaa5fbd180d9
```
(Output condensed from the raw lines into one row per file; every hash/oid/byte value is copied verbatim from the raw output.)

Verdict: PASS. All four copies byte-identical to Desktop and to the 2026-11-01 recorded hashes; none of the four blobs exists in the object store (exists=1), so none was committed byte-for-byte before.

## Check 2 — CSV content screen

Command: header via `head -1`; python csv.reader on the Account column (unique count, values printed only because all = Backtest); `grep -c` for email regex, phone regex `\(?[0-9]{3}\)?[-. ][0-9]{3}[-. ][0-9]{4}`, `[0-9]{7,}`, `amear|bani|ahmad|mffu|rithmic|apex` (-i); `git check-ignore -v`; `.gitattributes`; `core.autocrlf`; unique values of Instrument/Strategy/Entry name/Exit name; CR count.

```
Header (all four identical):
Trade number,Instrument,Account,Strategy,Market pos.,Qty,Entry price,Exit price,Entry time,Exit time,Entry name,Exit name,Profit,Cum. net profit,Commission,Clearing Fee,Exchange Fee,IP Fee,NFA Fee,MAE,MFE,ETD,Bars,
0710am lines=1191 account_cols [2] account_unique 1 ['Backtest'] ncols 24 row_len_set [24] emails=0 phone=0 digit7=0 names=0 ignore=1
0757am lines=811  account_cols [2] account_unique 1 ['Backtest'] ncols 24 row_len_set [24] emails=0 phone=0 digit7=0 names=0 ignore=1
0759am lines=1191 account_cols [2] account_unique 1 ['Backtest'] ncols 24 row_len_set [24] emails=0 phone=0 digit7=0 names=0 ignore=1
0800am lines=1305 account_cols [2] account_unique 1 ['Backtest'] ncols 24 row_len_set [24] emails=0 phone=0 digit7=0 names=0 ignore=1
.gitattributes: absent (attr=1); core.autocrlf: unset (autocrlf=1)
Instrument: 1 value ['NQCONTROW SEP25'] in all four
Strategy: PraxisNoiseAreaBreakout / _OppBand / _Flat1559 / PraxisLastHalfHourMomentum (1 each)
Entry name: ['L','S'] x3, ['LHMomLong','LHMomShort']; Exit name: XL/XS/Exit on session close/FlatEOD/LHFlat1559
CR count 0710am: 1191 (= line count; file is CRLF)
```
(Condensed one row per file from the raw output; values verbatim.)

Verdict: PASS. Only account value is Backtest; zero emails, phones, 7+ digit runs, name/broker terms; free-text columns hold only strategy/signal labels. Not git-ignored. Files are CRLF, but with no .gitattributes and autocrlf unset git stores them byte-for-byte, so a later commit keeps the sha256 (hash-object above already ran under that config).

## Check 3 — D-2026-11-10-A cite-by-cite

Commands: `sed -n 795p DECISION_LOG.md`; `sed -n '2018,2045p' DECISIONS.md`; `sed -n` on DECISIONS.md 112-133, 151, 765, 1972-1975, 1982 (cut -c1-1200); `grep -n '' specs/SPEC_RUBRIC.md | sed -n '16,20p;59,62p'` and 95-101; VM design 44-49; sweep :69, :81; `bd show Praxis_build-zd4`; `id praxispush`; `ls -ld ~/praxis-signals/`; `dscl . -list /Users | grep -i push`.

Cite-by-cite (source text pasted, abbreviated with ... only where the line is long):

```
DECISIONS.md:114 ## D-2026-07-09-C — Signals Drop Dir = Dedicated Low-Privilege User (`praxispush`), Not Trader Home
DECISIONS.md:117 **Status:** LOCKED (trader-chosen 2026-07-09)
DECISIONS.md:121 The signal drop directory is owned by a **dedicated low-privilege macOS user `praxispush`** at the canonical path **`/Users/praxispush/praxis-signals`**. This single path is used identically by (1) the B1-a authorized_keys forced-command/rrsync chroot for the n8n push peer, (2) the B1-a sshd scoping, and (3) the B1-c Parallels VM share. ...
DECISIONS.md:124 - **Structural least privilege.** A compromised n8n push key reaches a directory that contains nothing but signals ...
DECISIONS.md:129 **Impact:** ... B1-c creates this user + dir and scopes the Parallels share to it ... Operator creates the `praxispush` account before the B1-a forced-command step.
DECISIONS.md:151 ... D-2026-07-09-C's dedicated-`praxispush`-user choice was motivated partly by remote-push-key compromise (now moot with local n8n) and partly by clean VM-share-scope (still valid); whether local n8n writes as `praxispush` vs the trader user is revisited at B1-c execution.
DECISIONS.md:765 - **F1** (`specs/SPEC_RUBRIC.md:17-28`), **F2** (`:30-43`), **F4** (`:59-70`): untouched. FROZEN.
DECISIONS.md:1973 - **D1** (:17–21). "Default-decide." ... logs it as "decided by master under D-2026-11-08-D D1", and continues." ...
DECISIONS.md:1974 - **D2** (:22–26). "Only four things stop and wait for Amear's word": "(a) spending money"; "(b) switching live trading on, or any order path to a funded account"; "(c) changing circuit-breaker values while real money is at stake"; "(d) installing keys, credentials or agent permissions." "Everything else is D1."
DECISIONS.md:1982 ... "(6) the five P0 guard beads are accepted as known risk while only docs/specs move; fixed before any Block 3 code that can place orders." ... "(8) "final step of this build" = Block 4 paper pass on MFFU sim (the standing proof-of-concept ruling). Block 5 live is a separate sign-off under D2(b)."
SPEC_RUBRIC.md:17 ## FROZEN — nothing downstream may proceed until these clear
SPEC_RUBRIC.md:19 ### F1 — Signal-path topology vs. circuit-breaker placement
SPEC_RUBRIC.md:61 ### F4 — MFFU automation compliance
SPEC_RUBRIC.md:95-101 ### O2 — `praxispush` provisioning / ... at `~/praxis-signals/`, surfacing in Windows as `C:\Mac\Home\praxis-signals\` — / the primary account home mounted into the VM. **Required:** either the user / exists, or a DECISIONS.md entry records the removal and its accepted risk.
VM design :46 - **Windows:** `C:\Mac\Home\praxis-signals\vm-agent\`
VM design :47 - **Prefix verified** 2026-07-25: `Test-Path C:\Mac\Home\praxis-signals\b2-data` → `True`
VM design :48   in the Parallels Windows 11 ARM VM. So `C:\Mac\Home\praxis-signals\` is the correct
sweep :81 | G30 | ... | D2-AMBIGUOUS: provisioning a macOS user is close to D2(d) "credentials"; recording a deferral installs nothing. | manager's proposal: record the deferral and its accepted risk in DECISIONS.md (O2 allows this, SPEC_RUBRIC.md:93-94) | master may close under D1 by recording the deferral; provisioning stays D2(d)-adjacent |
bd zd4: ACCEPTANCE: EITHER provision praxispush + relocate the drop dir under it
  before the B1-a forced-command step, OR a DECISIONS entry explicitly
  recording the decision to defer/drop it with rationale. Trader-owned action
  (per DECISION_LOG 2026-07-25) but must not stay silent.
id: praxispush: no such user
exit=1
drwxr-xr-x@ 14 admin  staff  448 Nov 10 01:54 /Users/admin/praxis-signals/
dscl=1   (no user matching "push")
```

Sentence checks:
- Status / Authority lines: match :795 ("labelled 'decided by master under D-2026-11-08-D D1; changeable by Amear'"), :1973-1974, sweep :81. OK.
- "What was specified": :114-129 range, :121 quote, :124 quote, :151 quotes all verbatim. OK.
- "What exists now": `id` and `ls -ld` outputs reproduce exactly. Rubric :97-99 and VM design :46-48 support the Windows path. Hedge "did not observe the VM path" present. OK.
- "Decision" trigger (1): :1982 quote "fixed before any Block 3 code that can place orders" verbatim. OK. Trigger (2): zd4 quote "before the B1-a forced-command step" verbatim. OK.
- **DEFECT 3a (trigger content, not timing).** The entry's trigger is "it is provisioned". The bead it cites for the timing says the acceptance is "provision praxispush **+ relocate the drop dir under it**", and D-2026-07-09-C :129 has "B1-c creates this user + dir and scopes the Parallels share to it". The entry quotes the bead only for when, not what. Its own next paragraph says "Until the trigger, the drop dir sits in the primary account's home." That implies the trigger ends the exposure, but adding a user alone moves nothing. As written, the trigger can be met while the stated accepted risk stays exactly as it is. Authority :795 also says only "provisioned", so the unit followed its brief. The gap is still in the artifact.
- **DEFECT 3b (an exit the authority does not give).** "Trigger: it is provisioned, **or a replacement control is ruled by Amear**, before ...". DECISION_LOG.md:795 says "the trigger: provisioned before any Block 3 code ... and before the B1-a forced-command step (zd4)". The "replacement control" alternative is not in :795, sweep :81 or zd4. It does not decide a D2 item (it hands the choice to Amear), so this is not an S8 breach. It is still an added exit that nobody authorised.
- **DEFECT 3c (S2: something specified is presented as a control).** "The exposure is limited to sim and test because: D2(b) keeps ... behind Amear's word ...; F1 ... and F4 ... are FROZEN ...; and D8(8) makes the "final step of this build" a "Block 4 paper pass on MFFU sim"". Every reason given is a ruling or a rubric gate (specified). None is an observed technical state (implemented or tested). The entry admits this: "This entry states no fact about running processes". So "the exposure **is** limited" claims more than the cites carry. They support "is limited by ruling to sim and test". Neither the entry nor this check observed whether any non-sim account is connected in NinjaTrader on the VM.
- "What this entry does not do": the D2(d) quote is verbatim from :1974, O2 :95-101 is correct, and "does not grade it" agrees with :795 "rubric is not edited (O2 stays OPEN ...)". The bead-update sentence matches :795 (3). OK.
- S8: no D2 item is decided. The entry provisions nothing and leaves (b) and (d) with Amear. OK. Context only, not counted as a defect: D-2026-07-09-C is "LOCKED (trader-chosen)" and zd4 says "Trader-owned action (per DECISION_LOG 2026-07-25)". The entry defers the provisioning of a trader-locked decision under D1 without saying it was trader-locked. D1 (:1973) does cover this, since a D1 question is one "that would otherwise go to Amear".

Verdict: FAIL (3a, 3b, 3c).

## Check 4 — DECISIONS.md diff shape

```
$ git diff --numstat HEAD -- DECISIONS.md
17	0	DECISIONS.md
$ cmp <(git show HEAD:DECISIONS.md) <(head -n 2024 DECISIONS.md); echo cmp_head=$?
cmp_head=0
$ git show HEAD:DECISIONS.md | wc -l
    2024
$ cmp /tmp/hk2b-final/DECISIONS.md DECISIONS.md; echo cmp_final=$?
cmp_final=0
$ git show HEAD:DECISIONS.md | grep -c 'D-2026-11-10'
0
$ diff <(git show HEAD:DECISIONS.md) /tmp/hk2b-final/DECISIONS.md | head -3
2024a2025,2041
> 
> ## 2026-11-10 — D-2026-11-10-A: praxispush low-privilege user DEFERRED, accepted risk recorded (bead Praxis_build-zd4; rubric O2)
tail bytes HEAD: e . \n   working: d . \n   (both end in newline)
$ git diff --cached --numstat -- DECISIONS.md
(empty — unstaged)
```

Verdict: PASS. Pure append of 17 lines after HEAD's 2024. Lines 1-2024 are byte-equal to HEAD. /tmp/hk2b-final equals the working file. The ID D-2026-11-10 does not occur in HEAD, so there is no ID collision. It is unstaged, as Check 7 requires.

## Check 5 — MANIFEST rows

```
$ wc -l MANIFEST.md ; git show HEAD:MANIFEST.md | wc -l
     352 MANIFEST.md
     336
$ git diff -U0 HEAD -- MANIFEST.md | grep '^@@'
@@ -306,0 +307,8 @@
@@ -336,0 +345,8 @@
rows 345-348: the four evidence CSVs, each with "Account column Backtest only", its Desktop name, and a sha256 equal to Check 1 (421c44e6..34bd, 4207ea99..b6e8, 5a3c4d78..68e0, 4efd8ce8..80d9; verified by eye against the full row text)
rows 349-351: housekeeping-2b worker1 / adversarial / manager reports
row 352: | /DECISIONS.md | Log | 2 | 2026-11-10 | MODIFIED (...): entry D-2026-11-10-A (...) appended at lines 2025-2041 (heading :2026); lines 1-2024 unchanged |
path existence: all 8 paths "exists"
rows 307-314 (hunk 1), first cells:
307 /docs/specs/2026-11-06-walk-forward-values.md ... AMENDMENT ROW ... unit 2026-11-08-wf-spec-amendment
308 /docs/specs/2026-11-05-walk-forward-spec.md ... unit 2026-11-08-wf-spec-amendment
309-313 /docs/reports/2026-11-08-wf-spec-amendment-*-manager.md, 2026-11-09-wf-spec-amendment-resume-manager.md
314 /docs/reports/evidence/2026-11-09-u7-diff-of-record.patch
$ git show HEAD:MANIFEST.md | grep -c 'wf-spec-amendment-resume-manager'
0
```

Verdict for this unit's rows: PASS. There is one row per new file, every path exists, and the hashes match. The DECISIONS row's range 2025-2041, with the heading at :2026, matches Check 4: diff `2024a2025,2041`, line 2025 blank, heading on the next line.
Out-of-scope observation (reported, not a defect of this unit): MANIFEST.md also holds 8 uncommitted rows (307-314) from the 2026-11-08/09 wf-spec-amendment units, so HEAD is not a byte prefix of the working file. If this unit commits MANIFEST.md whole, those foreign rows land in the same commit. Any commit needs a hunk-scoped add or an explicit ruling.

## Check 6 — S6 praxispush blocks

```
$ grep -rn -i 'praxispush' specs docs/specs | cut -c1-200
specs/SPEC_RUBRIC.md:95:### O2 — `praxispush` provisioning
$ grep -n -i 'praxispush' DECISIONS.md | cut -c1-160
114, 121, 129, 151 (D-2026-07-09-C/-D), 1019, 1050 (D-2026-11-06-A), 2026, 2031, 2033, 2035 (the entry)
DECISIONS.md:1019   - **D-072:** ... "D-072 item 7: a new low-privilege Mac user, `praxispush`, that can see only `~/praxis-signals`." The two records differ (both REPORTED): D-072 names the low-privilege user `praxispush` and `~/praxis-signals` only; item 3 shares `Praxis.build`, with `admin` Read & Write and `staff` Read Only. ...
DECISIONS.md:1050 10. Does item 3 close the Fusion walkthrough's Question 0 (`:8`) ... Question 0's SMB option was D-072's form (`praxispush`, `~/praxis-signals`); item 3 shares `Praxis.build`, with `admin` Read & Write.
DECISIONS.md:991 ## 2026-11-06 — D-2026-11-06-A: Amear's voice notes of 2026-11-06 (... SMB file sharing ...)
DECISIONS.md:1004 3. File sharing: Fusion shared folders unavailable (no Sharing pane, as flagged). SMB route done by hand: Mac File Sharing on; Praxis.build shared; admin Read & Write; staff Read Only; Everyone No Access. VM: \\192.168.1.204\Praxis.build mapped as Z:, reconnect at sign-in, credentials remembered. ... Go-live checklist: unmap Z: and turn the share off before real money.
DECISIONS.md:1275 - **Ruling 10 — go-live checklist.** *Rules:* "Go-live checklist additions: remove the unauthenticated bridge request folders (or add auth) before real money; unmap Z: and turn off the SMB share." ...
$ bd show Praxis_build-dgt | head -1
❄ Praxis_build-dgt · B1-a: WireGuard tunnel + scoped SSH into signals drop   [● P1 · DEFERRED]   (Deferred: 2027-01-01)
$ bd show Praxis_build-dnt | head -1
✓ Praxis_build-dnt · B1-c: Mac signals layout + VM share + launchd reconciliation   [● P1 · CLOSED]
$ sed -n '2025,$p' DECISIONS.md | grep -n -o -i -E '.{40}(Fusion|SMB|D-2026-11-06|Parallels).{40}'
7:oot, the B1-a sshd scoping and the B1-c Parallels VM share (:121). Its first rationale is
```

**Block 1 (signal path B1-a / B1-c): CONTRADICTION FOUND.**
- **DEFECT 6a (the VM-share fact is stale and was not tested against D-2026-11-06-A).** The accepted risk says as plain fact that the drop dir is in "the primary account's home, which is shared into the Windows VM", at `C:\Mac\Home\praxis-signals\`. Its sources are the rubric and the 2026-07-25 Parallels-era design. The newest DECISIONS record of the share, Amear's own D-2026-11-06-A item 3 (:1004), says "Fusion shared folders unavailable" and that the SMB share is `Praxis.build` (admin Read & Write), mapped as `Z:`. :1019 says outright that the two records differ. The entry names neither Fusion, SMB nor D-2026-11-06-A; its only VM word is "Parallels", and that is in the quote of the 2026-07-09 spec. So the accepted risk may describe a share topology that DECISIONS.md itself records as replaced. The real exposure may be different: the repo is shared R/W, and whether the home is still shared is unknown. The hedge "This entry did not observe the VM path" covers the Windows path. It does not cover "which is shared into the Windows VM", which is stated without qualification.
- **DEFECT 6b (passed decision point not reconciled).** The entry quotes :151, that the praxispush choice "is revisited at B1-c execution", as live context. B1-c (`Praxis_build-dnt`) is CLOSED, and :129 says "B1-c creates this user + dir". So the revisit point named in :151 has already gone by without the user being created. The entry neither records this nor puts B1-c in its trigger. B1-a (`dgt`) is DEFERRED to 2027-01-01, so trigger (2) is far off and trigger (1) is the one that binds. The entry does not say so.

**Block 3 (breakers): no contradiction found.** The trigger (1) wording matches :1982 D8(6). No spec under specs/ or docs/specs links breakers to the drop dir (the breaker/drop-dir grep returned nothing).
**Block 4/5 (paper/live): partial gap.** No contradiction with D8(8) or D2(b). The entry's accepted risk leaves out the go-live control that does exist on record, D-2026-11-06-B Ruling 10 (:1275), "unmap Z: and turn off the SMB share". That control bears directly on the share exposure the entry accepts (folded into 6a).

Verdict: FAIL (6a, 6b).

## Check 7 — staged set

```
$ git diff --cached --name-only
docs/reports/evidence/2026-10-28-mffu-davi-reply.png
n=       1
```
Verdict: PASS. The staged set is exactly the one held-out PNG. This unit staged none of its own files.

## Check 8 — S13 line

```
$ sed -n '2025,$p' DECISIONS.md | grep -c -F 'Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.'
1
$ grep -n -F 'Fills are optimistic' specs/SPEC_RUBRIC.md | cut -c1-200
133:| S13 | Every report under docs/reports/ and every DECISIONS.md entry that states a backtest or P&L figure carries, once, the standing limitation sentence: "Fills are optimistic; Standard resoluti
```
Verdict: PASS (exactly once). The entry gives no backtest or P&L figure, so the line is not strictly required, but it does no harm.

## Defects

1. **3a. The trigger ends nothing.** It is "it is provisioned". The cited bead zd4 acceptance is "provision praxispush + relocate the drop dir under it", and D-2026-07-09-C :129 is "creates this user + dir and scopes the Parallels share to it". The entry's own risk paragraph ("Until the trigger, the drop dir sits in the primary account's home") implies the trigger ends the exposure. Provisioning alone moves nothing. (The root is in authority :795, which also says only "provisioned".)
2. **3b. An exit the authority does not give.** "or a replacement control is ruled by Amear" is not in DECISION_LOG.md:795, sweep :81 or zd4.
3. **3c. S2 overstatement.** "The exposure is limited to sim and test because ..." rests only on rulings and rubric gates (specified), not on observed state (implemented or tested), and the entry itself says it "states no fact about running processes".
4. **6a. S6: the VM-share fact is stale.** The accepted risk says the primary home "is shared into the Windows VM" at `C:\Mac\Home\...`, sourced to the rubric and the 2026-07-25 Parallels design. It was not tested against D-2026-11-06-A item 3 (DECISIONS.md:1004: "Fusion shared folders unavailable", SMB share is `Praxis.build` admin R/W as `Z:`), or against :1019, which records that the two differ. It also leaves out the go-live control D-2026-11-06-B Ruling 10 (:1275).
5. **6b. S6: a decision point that has passed is quoted as live.** The entry quotes :151 "revisited at B1-c execution", but B1-c (`dnt`) is CLOSED without the user. It does not say that B1-a (`dgt`) is DEFERRED to 2027-01-01, which leaves trigger (1) as the one that binds.

Out-of-scope (reported, not fixed): MANIFEST.md also holds 8 uncommitted rows 307-314 from the 2026-11-08/09 wf-spec-amendment units. A whole-file commit of MANIFEST.md would carry them.

Clean: the CSV copies (identity, never committed, content-safe, not ignored), the DECISIONS append shape, /tmp/hk2b-final, this unit's MANIFEST rows, the staged set, the S13 line, and S8 (no D2 item decided).

## Files staged
None by this worker.

Result: FAIL



## Round 2 (fresh worker, revised entry)

Mode: ADVERSARIAL. Artifact: DECISIONS.md:2025-end, entry D-2026-11-10-A. Findings appended per check below.

### Check 1: entry printed
`sed -n '2025,$p' DECISIONS.md`: 21 lines, :2025 blank, heading at :2026, S13 line at :2045 (file is 2045 lines). Entry D-2026-11-10-A read in full.

### Check 2: sentence-by-sentence cite verification (all cites opened this session)
Commands run: `sed -n` on DECISION_LOG.md:795 (full row), sweep report :81, DECISIONS.md :114-129, :151, :765, :1004, :1019, :1275, :1973-1974, :1982, SPEC_RUBRIC.md :14-20, :59-62, :93-101, VM design :44-49; `bd show Praxis_build-dnt|dgt|zd4`; `bd comments Praxis_build-dnt`; `id praxispush`; `ls -ld /Users/admin/praxis-signals/`.

Observed outputs (pasted, trimmed):
```
id: praxispush: no such user
exit=1
drwxr-xr-x@ 14 admin  staff  448 Nov 10 01:54 /Users/admin/praxis-signals/
✓ Praxis_build-dnt · B1-c: Mac signals layout + VM share + launchd reconciliation   [● P1 · CLOSED]
0        <- bd show Praxis_build-dnt | grep -c -i praxispush
0        <- bd comments Praxis_build-dnt | grep -c -i praxispush ("No comments on Praxis_build-dnt")
Close reason: ... AC2 Parallels share scoped to /Users/admin/praxis-signals only + whole-home 'admin' home share unchecked -> prlctl confirms ...
❄ Praxis_build-dgt · B1-a: WireGuard tunnel + scoped SSH into signals drop   [● P1 · DEFERRED]
Created: 2026-07-09 · Started: 2026-07-09 · Updated: 2026-07-09 · Deferred: 2027-01-01
○ Praxis_build-zd4 · praxispush security requirement silently dropped: ... [● P1 · OPEN]
  ACCEPTANCE: EITHER provision praxispush + relocate the drop dir under it before the B1-a forced-command step, OR a DECISIONS entry explicitly recording the decision to defer/drop it with rationale. Trader-owned action (per DECISION_LOG 2026-07-25) but must not stay silent.
```

| # | Sentence (short) | Verdict | Reason |
|---|---|---|---|
| 1 | Status: decided by master under D1; changeable by Amear | OK | Matches label demanded by DECISION_LOG.md:795 item (2). |
| 2 | Authority: DECISION_LOG.md:795, sweep G30 :81, DECISIONS.md:1973-1974 | OK | Row 795 is 09:43:00Z praxis-master, item (2) G30; :81 is G30; :1973/:1974 are D1/D2 under D-2026-11-08-D heading (:1891). |
| 3 | D-2026-07-09-C owned by "a dedicated low-privilege macOS user `praxispush`" at `/Users/praxispush/praxis-signals`, one path for B1-a chroot, sshd, B1-c share (:121) | OK | :121 verbatim. |
| 4 | First rationale "Structural least privilege" (:124) | OK | :124. |
| 5 | D-2026-07-09-D (:151) quotes "was motivated partly by ... (still valid)" and "is revisited at B1-c execution." | OK | :151 verbatim; heading :133 is D-2026-07-09-D. |
| 6 | "That revisit is not ahead." B1-c CLOSED, bead does not mention praxispush, close reason included (grep -c = 0) | OK | Re-run: CLOSED, grep 0; comments also 0. |
| 7 | B1-a DEFERRED, "Deferred: 2027-01-01" | OK | Re-run. |
| 8 | No praxispush user (`id` exit 1) | OK | Re-run, identical. |
| 9 | Drop dir in primary home, owned by admin, `ls -ld` output | OK | Re-run, byte-identical. |
| 10 | Did not observe how/whether the VM reaches the drop dir | OK | Scope statement; no overclaim. |
| 11 | Rubric :97-99 and VM design :46-48 "give the Windows path `C:\Mac\Home\praxis-signals\`, "the primary account home mounted into the VM"" | DEFECT (minor, S1) | The path is in both, but the quoted phrase is only in the rubric (:99). The VM design says "on the Parallels share" (:45) and nowhere "primary account home". Joint attribution makes the quote unverifiable at the second cite. |
| 12 | B1-c close reason quote "AC2 Parallels share scoped to /Users/admin/praxis-signals only + whole-home 'admin' home share unchecked" | OK | Verbatim in `bd show` close reason. |
| 13 | D-2026-11-06-A item 3 (:1004, REPORTED) "Fusion shared folders unavailable"; Praxis.build over SMB "admin Read & Write"; "mapped as Z:" | OK | :1004 verbatim; heading :991 is D-2026-11-06-A voice notes; REPORTED per :1019. |
| 14 | :1019 notes D-072 and item 3 differ | OK | :1019 "The two records differ (both REPORTED)". |
| 15 | Go-live "unmap Z: and turn the share off before real money" (:1004); Ruling 10 "unmap Z: and turn off the SMB share" (:1275) | OK | Both verbatim. |
| 16 | Decision: DEFERRED not dropped; trigger provision + move to `/Users/praxispush/praxis-signals` (:121) | OK | Decision text; path verified at :121. |
| 17 | First branch of zd4 acceptance, quote | OK | Verbatim in `bd show Praxis_build-zd4`. |
| 18 | Deadline (1) D8(6) wording "fixed before any Block 3 code that can place orders" (:1982) | OK | :1982 verbatim; correctly labelled as borrowed wording, not as D8(6) applying to zd4. |
| 19 | Deadline (2) "before the B1-a forced-command step" | OK | zd4 acceptance; also consistent with D-2026-07-09-C :129 "Operator creates the `praxispush` account before the B1-a forced-command step". |
| 20 | D1 reversal quote (:1973) | OK | Verbatim. |
| 21 | Accepted risk: dedicated-user boundary does not exist; anything that can write as admin or via a share exposing the dir can drop a signal file | OK as far as it goes; see DEFECT 1 | Mode drwxr-xr-x admin staff supports "only admin (and root) writes" (no `+` ACL in `ls -lde`). But it is the ONLY risk the "Accepted risk" paragraph names. |
| 22 | D2(b) quote (:1974) | OK | Verbatim. |
| 23 | F1 and F4 FROZEN (DECISIONS.md:765; rubric :17, :19, :61) | OK (weak) | :765 is a 2026-11-04 statement inside D-2026-11-04-A ("untouched. FROZEN."), dated; the rubric headings carry the present state and show no clear/pass note for F1 or F4 (grep of :17-70). |
| 24 | D8(8) quotes (:1982) | OK | Verbatim. |
| 25 | "did not observe the running system ... record-level limit, not a tested one" | OK | Correct S2 separation. |
| 26 | Provisions nothing; D2(d)-adjacent stays with Amear (:1974; :81) | OK | :81 "provisioning stays D2(d)-adjacent". |
| 27 | Does not edit the rubric; O2 (:95-101) stays OPEN; does not grade it | OK | :95 is O2 heading, :101 last line; entry makes no O2-satisfied claim. |
| 28 | zd4 stays open; master updates it after the commit | OK | zd4 OPEN (re-run); plan matches row 795 item (3). |

DEFECT 1 (O2 completeness / S2, moderate). The "Accepted risk, plainly" paragraph (DECISIONS.md:2041) names only the inbound risk: anyone who can write as admin or through a share can drop a signal file. It does not name the risk O2 itself identifies (SPEC_RUBRIC.md:96-99: "structural blast-radius limitation", "the primary account home mounted into the VM"), nor the D-2026-07-09-C rationale it says no longer holds (:124: a compromise reaching the signals dir reaches "nothing but signals — no documents, no repo, no credentials"; :125 the whole-home share over-exposure). Without the dedicated user, whatever reaches the drop dir through a home-level share reaches the rest of the primary home. It also omits the consequence of an injected file that the rubric's F1 "Why frozen" sets out (SPEC_RUBRIC.md:23-26 region): a file written straight into the drop dir skips every n8n-gate breaker. The master's own brief (DECISION_LOG.md:795) asked for the risk "stated plainly (drop dir sits in the primary home, shared into the VM)". The entry states the first half as OBSERVED and leaves the second half as a records conflict, so the exposure half is never accepted. Since O2 needs "its accepted risk", accepting only part of the named risk is a gap.

Non-defect observations: (a) D-2026-07-09-C is "LOCKED (trader-chosen 2026-07-09)" (:117); the entry does not say so. The deferral keeps that ruling's own timing (:129), so it is not a reversal and it is not a D2 item. Still, a master decision under D1 that defers part of a trader-locked ruling would be clearer if it said so. (b) zd4 asks for the DECISIONS entry "with rationale". The only reason the entry gives for deferring is implicit (provisioning is D2(d)-adjacent and stays with Amear). (c) The Block 2 specs give a third VM path form, `\\Mac\praxis-signals` (b2-data-acquisition-spec :118; mailbox-watcher design :15), which fits the B1-c named share. The entry leaves it out of "per the records" but does not claim to list them all.

### S8 verdict
No D2 item is decided. (a) No spend. (b) Live and funded paths stay behind D2(b); the entry adds a gate and opens no path. (c) No breaker values. (d) Nothing is provisioned or installed, and provisioning is left with Amear. The deadline makes Block 3 order-capable code wait on a provisioning step that is D2(d)-adjacent. That is a gate, not a decision taken for Amear. PASS.

### O2 judgment
O2 (SPEC_RUBRIC.md:99-100) says "either the user exists, or a DECISIONS.md entry records the removal and its accepted risk." Read strictly, a deferral is not a removal: the requirement is kept and only its timing moves. Read for purpose, the entry does record that the control is absent now (OBSERVED `id` and `ls`), owns that absence as a decision, and attaches accepted risk and a deadline. That answers O2's closing line ("A security requirement that stopped being mentioned is not a resolved one"). My view: a deferral entry meets O2 only on the purposive reading, as a time-bound removal, and only if the accepted risk covers the risk O2 names. Because of DEFECT 1 it does not fully do that today. The entry rightly does not grade O2 itself. The claim "O2 allows this" in sweep :81 is the manager's gloss. O2's text never says "defer".

### Check 3: byte checks
```
cmp <(git show HEAD:DECISIONS.md) <(head -n 2024 DECISIONS.md); echo exit=$?   -> exit=0
cmp /tmp/hk2b-final/DECISIONS.md DECISIONS.md; echo cmp=$?                    -> cmp=0
git show HEAD:DECISIONS.md | wc -l                                             -> 2024
git diff HEAD --stat -- DECISIONS.md -> DECISIONS.md | 21 +++++++++++++++++++++  (1 file changed, 21 insertions(+))
```
PASS.

### Check 4: S6 search and per-block verdict
`grep -rn -i 'praxispush\|praxis-signals' specs docs/specs` hits: SPEC_RUBRIC.md :95, :98; b2-data-acquisition-spec :118; walk-forward-spec :16, :99; vm-agent-delegation design :17, :45-48, :110, :169; b2-data-mailbox-watcher design :15, :30, :47, :53, :88, :144. None is a Block 1, 3, 4 or 5 spec. I also checked the phase-3 build spec (docs/specs/2026-11-05-phase3-build-specification.md).
- Block 1 (:46-60): the watched dir is an example ("e.g., C:\Signals\Incoming\", :56) and no user is required. No contradiction.
- Block 3 (:91-111): breakers are n8n gates, all SPECIFIED ONLY (:11). The entry adds a gate before order-capable Block 3 code and changes no breaker. No contradiction. It does fail to state the breaker-bypass consequence (DEFECT 1).
- Block 4/5: the entry repeats D8(8) (Block 4 paper on MFFU sim; Block 5 a separate D2(b) sign-off). No contradiction.
- Rubric O2: kept OPEN, not edited. No contradiction.
PASS (no contradiction).

### Check 5: S13 count
`grep -c 'Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.'` on :2025-end -> `1`. `grep -c 'Fills are optimistic'` -> `1`. PASS.

### Check 6: MANIFEST
`grep -n 'DECISIONS.md' MANIFEST.md | tail -1`: row :352 "... appended at lines 2025-2045 (heading :2026); lines 1-2024 unchanged |". This matches wc (2045) and the heading position. PASS.

### Check 7: staged set
`git diff --cached --name-only` -> `docs/reports/evidence/2026-10-28-mffu-davi-reply.png` (exactly one path). PASS.

### Round 2 defect list
1. DECISIONS.md:2041 (Accepted risk). The accepted risk covers only signal-file injection. It leaves out the blast-radius exposure O2 names (SPEC_RUBRIC.md:96-99; D-2026-07-09-C :124-125) and the n8n-breaker bypass an injected file would get. O2's "its accepted risk" is only partly met. Moderate.
2. DECISIONS.md:2037 ("How the VM reaches it"). The quote "the primary account home mounted into the VM" is credited jointly to the rubric and the VM workspace design. It appears only in the rubric (:99), not in docs/specs/2026-07-25-vm-agent-delegation-workspace-design.md:46-48. S1, minor.

Round 2 result: FAIL

## Round 3 (fresh worker, revised lines 2033, 2037, 2041)

Mode: ADVERSARIAL. Worker had no access to the reasoning behind the revision. Read-only apart from this section.

### Check 1 — paragraphs located
`grep -n "What was specified" DECISIONS.md` -> `2031:`. Paragraphs read with `sed -n '2025,2045p'`: 2031 What was specified, 2033 Where B1-c and B1-a stand, 2035 What exists now, 2037 How the VM reaches it, 2039 Decision, 2041 Accepted risk, 2043 What this entry does not do, 2045 S13.

### Check 2 — quote by quote (grep -n -F hits, cut)
DECISIONS.md:2031
- "dedicated low-privilege macOS user `praxispush`" -> `121:The signal drop directory is owned by a **dedicated low-privilege macOS user `praxispush`** at the canonical path **`/Users/praxispush/praxis-signals`**`. OK. The three uses (chroot, sshd scoping, Parallels VM share) are at :121 ("(1) the B1-a authorized_keys forced-command/rrsync chroot ... (2) the B1-a sshd scoping, and (3) the B1-c Parallels VM share"). OK.
- "Structural least privilege" -> `124:- **Structural least privilege.** A compromised n8n push key reaches ...`; first bullet under **Rationale:** (:123). OK.
- :151 quotes -> `151: ... choice was motivated partly by remote-push-key compromise (now moot with local n8n) and partly by clean VM-share-scope (still valid); whether local n8n writes as `praxispush` vs the trader user is revisited at B1-c execution.` :151 is under `133: ## D-2026-07-09-D`. OK ("or" vs "vs" is outside the quotes).
- "LOCKED (trader-chosen 2026-07-09)" -> `117:**Status:** LOCKED (trader-chosen 2026-07-09)` (inside D-2026-07-09-C, :114). OK.

DECISIONS.md:2033 (checked again because it was revised)
- `bd show Praxis_build-dnt` line 1: `... [● P1 · CLOSED]`. `bd show Praxis_build-dnt | grep -c -i praxispush` -> `0`. OK.
- `bd show Praxis_build-dgt`: `1:... [● P1 · DEFERRED]`, `3:... Deferred: 2027-01-01`. OK.

DECISIONS.md:2037
- Rubric :98 `at `~/praxis-signals/`, surfacing in Windows as `C:\Mac\Home\praxis-signals\` —`; :99 `the primary account home mounted into the VM. **Required:** ...`. OK.
- VM design :46 `- **Windows:** `C:\Mac\Home\praxis-signals\vm-agent\``; :47 `- **Prefix verified** 2026-07-25: `Test-Path C:\Mac\Home\praxis-signals\b2-data` → `True``; :48 `in the Parallels Windows 11 ARM VM. So `C:\Mac\Home\praxis-signals\` is the correct`. `grep -n -F 'primary account home mounted'` over the design and the rubric -> only `specs/SPEC_RUBRIC.md:99`. So "it does not use the rubric's wording" is OK. The round 2 defect 2 (joint credit) is fixed.
- B1-c close reason: `bd show Praxis_build-dnt | grep -n -F "AC2 Parallels share scoped to /Users/admin/praxis-signals only + whole-home 'admin' home share unchecked"` -> `4:Close reason: Infra committed dc5216c ...` (matched). OK.
- :1004 "Fusion shared folders unavailable", "admin Read & Write", "mapped as Z:", "unmap Z: and turn the share off before real money": all hit `1004:3. File sharing: Fusion shared folders unavailable ... Go-live checklist: unmap Z: and turn the share off before real money.`; :1004 sits under `991: ## 2026-11-06 — D-2026-11-06-A`. Marked REPORTED. OK.
- :1019 -> `The two records differ (both REPORTED): D-072 names ... item 3 shares `Praxis.build` ...`. OK.
- "unmap Z: and turn off the SMB share" -> `1275:- **Ruling 10 — go-live checklist.** *Rules:* "... unmap Z: and turn off the SMB share."`. OK.

DECISIONS.md:2041
- "reaches a directory that contains nothing but signals — no documents, no repo, no credentials" -> `124:- **Structural least privilege.** A compromised n8n push key reaches a directory that contains nothing but signals — no documents, no repo, no credentials.` The quoted words are exact. The text around them is NOT: the entry says "with the dedicated user a compromised writer 'reaches ...'"; :124's subject is "A compromised n8n push key". The same entry quotes :151 at 2031 saying that motivation is "now moot with local n8n". **DEFECT** (see list).
- "accidentally shared the entire Mac home into the VM" -> `125:- **Retires the B1-0 finding structurally.** The B1-0 spike accidentally shared the entire Mac home into the VM (`\\psf\Home` / `Z:\`).`. OK.
- "structural blast-radius limitation" -> rubric `96:The signal directory was specified as a dedicated low-privilege macOS user, the` / `97:rationale being structural blast-radius limitation.`. OK.
- Breakers -> rubric `23:**Why frozen.** Block 3 specifies the breakers as n8n workflow gates that` / `24:terminate before the file-write node.`; labelled "(inference from that text, not tested)". OK (S2).
- D2(b) -> `1974:- **D2** (:22–26). ... "(b) switching live trading on, or any order path to a funded account"`. OK.
- F1/F4 FROZEN -> `765:- **F1** (`specs/SPEC_RUBRIC.md:17-28`), **F2** (`:30-43`), **F4** (`:59-70`): untouched. FROZEN.`; rubric `17:## FROZEN — nothing downstream may proceed until these clear`, `19:### F1 — Signal-path topology vs. circuit-breaker placement`, `61:### F4 — MFFU automation compliance`; next `## ` heading is `74:## PASSED`, so both sit under FROZEN. OK.
- D8(6), D8(8) -> `1982: ... "(6) the five P0 guard beads are accepted as known risk while only docs/specs move; fixed before any Block 3 code that can place orders." ... "(8) "final step of this build" = Block 4 paper pass on MFFU sim (the standing proof-of-concept ruling). Block 5 live is a separate sign-off under D2(b)."`. OK.
- "This entry did not observe the running system ... a record-level limit, not a tested one." S2 OK.

Also checked (not in focus): `bd show Praxis_build-zd4 | tr '\n' ' ' | tr -s ' ' | grep -o -F 'provision praxispush + relocate the drop dir under it before the B1-a forced-command step'` -> matched (it wraps over bead lines 15–16). D1 at :1973 OK. DECISION_LOG.md:795 is `[2026-11-10T09:43:00Z] WHO: praxis-master` and carries "(2) G30: a DECISIONS.md entry ...". Sweep report :81 is row `| G30 |`. OK.

O2 (rubric :95–101): the accepted-risk paragraph now names the blast radius in so many words ("Blast radius: ... that is the risk this deferral accepts"), cites rubric :97, and says a writer acting as the primary account "is not held to that directory". The round 2 defect 1 is fixed in substance. Whether a *deferral* meets O2's "records the removal" is a grading question; the entry says it does not grade O2 (:2043). Not graded here.

S8: The provisioning stays with Amear (:2043). D2(b) is kept behind his word. The deferral installs nothing. No D2 item is decided. Note: bead zd4 says "Trader-owned action (per DECISION_LOG 2026-07-25)". The entry relies on D1 (:1973) to supersede that, and says Amear may change it. Not a defect.

Observations, not defects: (a) Filing the rubric under "Parallels era" at 2037 is this entry's own reading. The rubric's text does not say Parallels; the `C:\Mac\Home` prefix is what ties it to Parallels. (b) The Fusion SMB share at 2037 is `Praxis.build`, not the drop dir. The paragraph does not claim the drop dir is reachable through Z:, but its heading ("How the VM reaches it") could be read that way.

### Check 3 — byte shape
```
cmp <(git show HEAD:DECISIONS.md) <(head -n 2024 DECISIONS.md); echo exit=$?
exit=0
cmp /tmp/hk2b-final/DECISIONS.md DECISIONS.md; echo cmp=$?
cmp=0
```

### Check 4 — S13 line
`tail -n +2025 DECISIONS.md | grep -c -x -F 'S13: Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.'` -> `1`. OK.

### Check 5 — staged set
`git diff --cached --name-only` -> `docs/reports/evidence/2026-10-28-mffu-davi-reply.png` (only). OK.

### Round 3 defect list
1. DECISIONS.md:2041 (S1, plus S2 framing). "D-2026-07-09-C's rationale (DECISIONS.md:124) is that with the dedicated user a compromised writer 'reaches a directory that contains nothing but signals ...'". At :124 the subject is "A compromised n8n push key", not "a compromised writer". The entry's own quote of :151 (at 2031) says that push-key motivation is "now moot with local n8n". So the blast-radius sentence gives the source's moot rationale a wider subject without saying so. Fix: either quote the subject as written ("a compromised n8n push key") or label the widening to "any writer" as this entry's inference.

Round 3 result: FAIL

## Round 4 (fresh worker, DECISIONS.md:2041 only)

Mode: ADVERSARIAL. Fresh worker; no access to the reasoning behind the revision. Scope: DECISIONS.md:2041 only.

### Check (3) integrity (run first, output pasted)

```
$ cmp <(git show HEAD:DECISIONS.md) <(head -n 2024 DECISIONS.md); echo exit=$?
exit=0
$ cmp /tmp/hk2b-final/DECISIONS.md DECISIONS.md; echo cmp=$?
cmp=0
$ git diff --cached --name-only
docs/reports/evidence/2026-10-28-mffu-davi-reply.png
```

Lines 1-2024 match HEAD byte for byte. The working file matches /tmp/hk2b-final. DECISIONS.md is not staged. The only staged path is the held-out PNG, which was already staged before this unit.

### Check (2) quote fragments, `grep -n -F` line hits

```
D[A compromised n8n push key reaches a directory that contains nothing but signals — no documents, no repo, no credentials]: 124 2041
D[now moot with local n8n]: 151 2031 2041
D[accidentally shared the entire Mac home into the VM]: 125 2041
D[switching live trading on, or any order path to a funded account]: 1974 2041
D[final step of this build]: 1952 1982 2041
D[Block 4 paper pass on MFFU sim]: 1953 1982 2041
D[Block 5 live is a separate sign-off under D2(b)]: 1954 1982 2041
D[untouched. FROZEN.]: 392 393 395 465 466 468 524 525 527 728 729 731 765 766
R[structural blast-radius limitation]: 97
R[Block 3 specifies the breakers as n8n workflow gates that]: 23
R[terminate before the file-write node]: 24
R[Signal-path topology vs. circuit-breaker placement]: 19
R[MFFU automation compliance]: 61
R[FROZEN — nothing downstream]: 17
```

Context checks. The nearest `##` heading above :124 is :114 "D-2026-07-09-C — Signals Drop Dir = Dedicated Low-Privilege User", so :124 and :125 do belong to D-2026-07-09-C. The rubric `## ` headings between :17 and :101 are :17 FROZEN, :74 PASSED and :93 OPEN, so F1 (:19) and F4 (:61) both sit under FROZEN. O2 is at :95-101. The "(admin)" owner comes from the entry's own OBSERVED section (:2035, `ls -ld` shows owner admin).

### Sentence-by-sentence

1. "Until the trigger, the dedicated-user boundary ... does not exist." OK. It rests on :2035, where `id praxispush` returned no such user.
2. "Anything that can write as the primary account (admin), or through any share that exposes that directory to the VM, can drop a signal file." OK, borderline on S2. The admin half follows from the observed `drwxr-xr-x admin` listing. The share half is phrased as a conditional. Whether a share can write was not tested, and the sentence does not say it was. This is not counted as a defect.
3. Blast radius, :124 quote. OK on S1: the text is verbatim and the subject is now "A compromised n8n push key", as the source has it. This fixes the Round 3 defect. The widening to "any writer" is labelled "this entry's inference, not the source's words". Minor point, not counted: "D-2026-07-09-C's rationale" (singular) narrows the source. The entry's own :2029 calls this the "first rationale", and :125 is a second one.
4. Blast radius, :151 quote "now moot with local n8n". OK. The subject is "that push-key motive", which matches the source's "remote-push-key compromise (now moot with local n8n)".
5. Blast radius, "without the dedicated user, a writer acting as the primary account is not held to that directory". DEFECT (S2). This is an inference: a converse drawn from :124, and nothing was tested. It sits after a semicolon, outside the clause that carries the "this entry's inference" label. No line is cited for it, and it is stated as fact.
6. Blast radius, :125 quote. OK. The text is verbatim and the subject "the B1-0 spike" is kept.
7. Blast radius, rubric :97 "structural blast-radius limitation". OK. The subject is the rationale for the dedicated user, as in the rubric. On O2: the paragraph names the blast-radius risk O2 names. It covers the whole home shared into the VM (:125) and the share exposing the directory. It records that risk as accepted ("that is the risk this deferral accepts"). O2 is MET.
8. Breakers, rubric :23-24. OK. The quote is verbatim across the line wrap and the subject is "Block 3". The conclusion is labelled "inference from that text, not tested".
9. D2(b), :1974. OK. Opening the sentence with "do not permit" is slightly stronger than the source, which makes this wait for Amear's word rather than forbidding it. The next clause, "behind Amear's word", restates it correctly. Not counted.
10. F1/F4 FROZEN, :765 and rubric :17, :19, :61. OK. The heading text matches verbatim.
11. D8(8), :1982. OK. All three fragments are verbatim and the subjects are kept.
12. "This entry did not observe the running system." DEFECT (S2, underclaim). The negative is universal and the same entry contradicts it: :2035 is headed "What exists now (OBSERVED 2026-11-10)" and records live `id` and `ls -ld` output. Read with the next sentence, the intended scope is the order path and the sim/test limit, but the text does not say that. Fix: scope it, e.g. "This entry did not observe the order path or any account connection."

### Defects

1. DECISIONS.md:2041, Blast radius: "without the dedicated user, a writer acting as the primary account is not held to that directory" is an unlabelled inference stated as fact. It falls outside the semicolon clause that carries the inference label (S2).
2. DECISIONS.md:2041, last two sentences: "This entry did not observe the running system" is a universal negative that the entry's own OBSERVED section at :2035 contradicts. It is an underclaim and needs scoping (S2).

S1: no defect. Every quote is verbatim at its cited line with its subject kept, and the Round 3 subject defect is fixed. O2: MET.

Round 4 result: FAIL

## Round 5 (fresh worker, final read of DECISIONS.md:2025-2045)

Mode: ADVERSARIAL. Fresh worker; no prior-round reasoning was used. Quotes were not re-checked against their sources, as the brief says (rounds 2-4 did that).

### Mechanical checks (output pasted)

```
$ sed -n '1974p' DECISIONS.md | cut -c1-400
- **D2** (:22–26). "Only four things stop and wait for Amear's word": "(a) spending money"; "(b) switching live trading on, or any order path to a funded account"; "(c) changing circuit-breaker values while real money is at stake"; "(d) installing keys, credentials or agent permissions." "Everything else is D1."
$ grep -cF "Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed." DECISIONS.md
32
$ sed -n '2025,2045p' DECISIONS.md | grep -cF "<same S13 line>"
1
$ cmp <(git show HEAD:DECISIONS.md) <(head -n 2024 DECISIONS.md); echo exit=$?
exit=0
$ cmp /tmp/hk2b-final/DECISIONS.md DECISIONS.md; echo cmp=$?
cmp=0
$ wc -l DECISIONS.md
    2045 DECISIONS.md
```

S13: the line appears exactly once in the entry (2025-2045). The file has 32 copies in total, and the other 31 come from earlier entries. Lines 1-2024 are byte-identical to HEAD, and the file is identical to /tmp/hk2b-final.

S8: no defect. The entry defers provisioning, which it calls "D2(d)-adjacent" and says "stays with Amear". It sets only D1 gates (Block 3 order-capable code, the B1-a forced-command step), and its claims about D2(b) only cite the record. No D2 item (a)-(d) is decided for Amear.

### S2: sentence-by-sentence findings

1. DEFECT, DECISIONS.md:2041: "Anything that can write as the primary account (admin), or through any share that exposes that directory to the VM, can drop a signal file." This states a capability the entry does not show, and it is not labelled as an inference.
   - The share half overclaims. A share that exposes the directory read-only does not let anyone write to it, so "any share that exposes" is wider than what the records cited at :2037 support. Of those, only the Fusion SMB share is recorded as "Read & Write".
   - :2035 says "This entry did not observe how, or whether, the current VM reaches the drop dir". So the VM-write half has no observation behind it, but the sentence has no "(inference, not tested)" tag. The sentences after it in the same paragraph do carry that tag.
   - The admin half follows from the `drwxr-xr-x ... admin` output, but that the written file is a "signal file" (that is, one the system consumes) is not shown either.
   - Fix: scope it to writable shares and add the entry's own label, e.g. "... or through any share that gives write access to that directory from the VM, can place a file there (inference from the :2035 mode bits and the :2037 records, not tested)."
2. Minor, DECISIONS.md:2033: "That revisit is not ahead." This is an inference: B1-c's CLOSED status is taken to mean its "execution" point (the :151 revisit trigger) has passed. It has no label. The CLOSED output printed right after it supports it, so this is a weak finding. It is not the basis for the FAIL.
3. Minor, DECISIONS.md:2041: "The rulings on record do not permit an order path to a funded account". D2(b) puts that behind Amear's word; it does not forbid it. The clause after the colon gives the conditional reading, so this is wording, not a contradiction. Also, "the limit to sim and test": no cited record mentions "test"; only sim is sourced (D8(8)). This is minor and not the basis for the FAIL.

No contradictions between sentences found. I checked these pairs:
- :2035 "did not observe how, or whether, the current VM reaches" against the :2037 heading "How the VM reaches it, per the records". The heading is qualified, so they agree.
- "does not change" LOCKED D-2026-07-09-C (:2031) against the deferral. The entry records non-implementation and does not overturn the lock.
- "Trigger" (:2039) against "Until the trigger" (:2041). Both use "trigger" to mean the work is done, so they agree.
- "stays with Amear" (:2043) against "Both must be done before" (:2039). The second is a gate, not an action taken, so they agree.

The Round 4 universal-negative defect is fixed. :2041 now reads "did not observe the order path, any account connection or any running process", which is scoped.

Defects: one S2 defect, item 1 above (DECISIONS.md:2041, "or through any share that exposes that directory to the VM, can drop a signal file": an unlabelled inference that overclaims). Items 2 and 3 are minor and listed for the record.

Round 5 result: FAIL

## Round 6 (fresh worker, final read of DECISIONS.md:2025-2045)

Mode: ADVERSARIAL. Criteria: S2, S8, O2, S13. I did not re-check quotes against their sources; rounds 2-4 did that.

### Mechanical checks (run 2026-11-10, output pasted)

```
$ tail -n +2025 DECISIONS.md | grep -oF "Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed." | wc -l
       1
$ cmp <(git show HEAD:DECISIONS.md) <(head -n 2024 DECISIONS.md); echo exit=$?
exit=0
$ cmp /tmp/hk2b-final/DECISIONS.md DECISIONS.md; echo cmp=$?
cmp=0
$ git diff --cached --name-only
docs/reports/evidence/2026-10-28-mffu-davi-reply.png
$ wc -l DECISIONS.md
    2045 DECISIONS.md
```

- S13: the line appears exactly once in 2025-$ (it is line 2045).
- Lines 1-2024 are byte-identical to HEAD. The file is identical to /tmp/hk2b-final.
- The only staged path is the mffu PNG, which was already staged when the session started. DECISIONS.md is not staged; that is a fact for the record, not a defect under these criteria.

### Round 5 defects, re-checked

1. The Round 5 blocking item (:2041) is FIXED. It now reads "so can anything with write access through a share that exposes that directory to the VM, if one exists (this entry did not observe one)". That is scoped to writable shares, it is conditional, and it says nothing was observed. The admin half rests on the OBSERVED `drwxr-xr-x ... admin` output, so it no longer overclaims.
2. The Round 5 minor item (:2033) is FIXED. "That revisit point has passed (this entry's reading of the bead states below)" is now labelled.
3. The Round 5 minor item (:2041, "do not permit") is FIXED. It now reads "put any order path to a funded account behind Amear's word", which matches D2(b) at :1974 as printed.

### S2: new read of every sentence

- Every inference in the blast-radius and breaker sentences is labelled. The three labels are "this entry's inference, not the source's words", "this entry's inference from :124, not tested" and "inference from that text, not tested".
- Minor, still open: "So the limit to sim and test is a record-level limit". The cited records source only sim (D8(8), "Block 4 paper pass on MFFU sim"); none of them sources "test". The phrase is also the first time "the limit" is mentioned, so it has no antecedent. The sentence's own qualifier ("record-level ... not a tested one") keeps it from being an overclaim, so I am not blocking on it.
- Minor: ":1019 notes that D-072 and item 3 differ". "D-072" is not introduced anywhere in the entry, so a reader cannot tell what it is. This is a clarity issue, not an overclaim.

I found no internal contradictions. I checked these pairs:
- "Decided by master under D1" (:2027) against "provisioning ... stays with Amear" (:2043). The deferral is D1; the action stays with Amear.
- "did not observe how, or whether, the current VM reaches the drop dir" (:2035) against the share clause at :2041. The share clause is conditional and says nothing was observed.
- "LOCKED ... this entry does not change it" (:2031) against "DEFERRED, not dropped" (:2039).

### S8 and O2

- S8: no defect. The entry sets D1 gates only. Provisioning is called "D2(d)-adjacent" and stays with Amear. D2(b) is cited, not exercised.
- O2: the requirement is met. The entry records the deferral and its accepted risk, and it names the O2 risk with the rubric's own wording, "structural blast-radius limitation", followed by "that is the risk this deferral accepts". O2 itself is left OPEN and is not graded.

Defects: no blocking defects. Two minor items, listed for the record: "the limit to sim and test" (no source for "test" and no antecedent for "the limit"), and "D-072", which the entry never introduces.

Round 6 result: PASS

S13 (added by the manager under Correction 1, 2026-11-10): Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
