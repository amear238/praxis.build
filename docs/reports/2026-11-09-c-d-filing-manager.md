Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

# Unit 2026-11-09-c-d-filing — manager report

## Task
File two DECISIONS.md entries that record Amear's rulings by pointer: D-2026-11-08-C (C1–C10, answers file `docs/reports/2026-11-08-amear-answers-park-card.md` :12–43) and D-2026-11-08-D (D1–D12, `docs/reports/2026-11-08-amear-rulings-voice-2.md` :12–75). Check and finish U8's untrusted draft of C at DECISIONS.md :1807 onward. Add D after it. Correct the MANIFEST rows from :305 on. Stage nothing. This unit decides nothing.

## Rubric criteria addressed
S1, S2, S4, S5, S8 (scope note per brief: under D-2026-11-08-D D1/D2 only the D2 items belong to Amear; the rubric's own amendment is a later unit), S13. The wording is quoted verbatim in the brief from `specs/SPEC_RUBRIC.md` standing criteria.

## Workers dispatched
| id | mode | scope | outcome |
|---|---|---|---|
| W1 | ADVERSARIAL | every cross-file pointer and quote in U8's frozen draft (/tmp/cdf-decisions-pre.md :1807–1889) | `VERDICT: 16 WRONG of 181 checked` (see Adversarial findings) |
| W2 | ADVERSARIAL | finished entries C and D and MANIFEST :305–310: hashes, cmp, every item pointer, paraphrase content, labels, S13 | see Adversarial findings |

No BUILD worker. The edits were made by script (python, exact-match replace with count==1 asserts, and a block splice from the paste file). That is the "pure doc edit" kind of work, and the brief makes this unit the filer.

## Process log
- 01:03:50Z baseline. HEAD = origin/main = 6c4c109. DECISIONS.md had 1889 lines (HEAD 1806). MANIFEST.md had 307 lines (HEAD 298). Pre-edit copies: /tmp/cdf-decisions-pre.md, /tmp/cdf-manifest-pre.md, /tmp/cdf-manifest-pre304.txt (`head -n 304`).
- I recomputed both hashes. They match (V1).
- I hashed U8's draft block at :1819–1850. It equals the C paste (V3).
- I sent W1 to check U8's draft pointers against a frozen copy. While it ran, I made the structural corrections to C by script (31 exact replacements, each asserted to match once):
  - (a) Status: U8 is recorded as drafter, its no-return is recorded, and this unit is recorded as checker/finisher.
  - (b) Every HANDOFF.md:10–16 pointer now points to :63–69, the park card's current place in the working tree. I saw this with `sed -n '54,78p' HANDOFF.md`: the items are at :63–69.
  - (c) The Copy check no longer says that U8's report holds the post-insertion hash. It points to this report.
  - (d) "re-read … this unit (OBSERVED)" is re-attributed to this unit.
  - (e) Each C bullet now opens with its answers-file line range.
  - (f) The filing-notes heading is renamed "Filing notes (master's/manager's readings, not rulings)".
  - (g) The S4 grep is replaced by one this unit observed.
  - (h) A manager's reading notes that D12 re-sets the order.
  - (i) U8's "NEEDS AMEAR" is retitled "Open readings (not decided here)". See Decisions taken.
- W1 returned. Its one new WRONG was the U8-report hash claim, already fixed by (c). Its 15 stale HANDOFF pointers were fixed by (b). Its S1 note on "re-read this unit" was fixed by (d). Its hunk-header caveat is fixed: the C8 bullet now names `git diff -U0 HEAD -- specs/SPEC_RUBRIC.md`.
- I wrote entry D into two template files (/tmp/cdf-scripts/d_head.md, d_tail.md). The script spliced them after C, with the fenced block copied by script from voice-2 file lines 12–75. The fences were asserted at :11 and :76.
- MANIFEST:
  - :305 (C paste) is kept byte-identical to U8's draft row after its claims were checked: sha prefix, heading at :48, notes at :50–54.
  - :306 (U8 report) is rewritten as a no-return record.
  - :307 (D paste), :308 (strategy brief) and :309 (this report) are new.
  - :310 is the DECISIONS.md update row naming both entries and their line ranges.
- Negative tests (V6), then W2.

## Verification evidence

### V1. Hashes, recomputed (task 2)
```
$ sed -n '12,43p' docs/reports/2026-11-08-amear-answers-park-card.md | openssl dgst -sha256
SHA2-256(stdin)= 7fd6c65e2e694b3dd88b3e99a880288f204c111be70a114cfb1244fa0ffc60fa
$ sed -n '12,75p' docs/reports/2026-11-08-amear-rulings-voice-2.md | openssl dgst -sha256
SHA2-256(stdin)= fd2654699e105849cbfa2f0954a89c97aabe896195af1ac02b11866519115ab1
```
Both equal the recorded values. No stop.

### V2. Baseline (pre-edit)
```
2026-11-09T01:03:50Z
DEC 1-1806 == HEAD: cmp exit 0
MAN 1-298 == HEAD: cmp exit 0
5bfab44568757ae2652fd4a4c7aa19844745e7995c0cdc28110c8d1165bdda95  -   (sha256 of `git diff --cached --name-only`)
      12   (staged path count)
0          (`git show HEAD:DECISIONS.md | grep -c 'D-2026-11-08-[CD]:'`)
```

### V3. U8 draft block = C paste (pre-edit)
```
$ sed -n '1819,1850p' DECISIONS.md | openssl dgst -sha256
SHA2-256(stdin)= 7fd6c65e2e694b3dd88b3e99a880288f204c111be70a114cfb1244fa0ffc60fa
```

### V4. Post-edit state (tasks 3 and 4)
```
2026-11-09T01:07:21Z
    2007 DECISIONS.md
     310 MANIFEST.md
cmp DEC 1-1806 vs HEAD exit=0
cmp MAN 1-298 vs HEAD exit=0
cmp MAN 1-304 vs pre-edit exit=0
cmp MAN 305 vs U8 draft exit=0
1818:```text
1851:```
1901:```text
1966:```
SHA2-256(stdin)= 7fd6c65e2e694b3dd88b3e99a880288f204c111be70a114cfb1244fa0ffc60fa   (DECISIONS.md :1819-1850, C block body)
SHA2-256(stdin)= fd2654699e105849cbfa2f0954a89c97aabe896195af1ac02b11866519115ab1   (DECISIONS.md :1902-1965, D block body)
standing sentence in 1807,1889: 1
standing sentence in 1890,2007: 1
Fills in D block: 0
5bfab44568757ae2652fd4a4c7aa19844745e7995c0cdc28110c8d1165bdda95  -   (index fingerprint, unchanged)
 M DECISIONS.md
 M MANIFEST.md
?? docs/reports/2026-11-09-c-d-filing-manager.md
```
Entry headings: `grep -n '^## 2026-11-08 — D-2026-11-08-[CD]'` gave 1808 (C) and 1891 (D). The last line of each entry is "Nothing else." at :1889 and :2007. The blank separators are at :1807 and :1890.

### V5. S4: no unit acting on C or D dispatched (DISPATCH_LOG after the U8 dispatch row :2037)
```
$ sed -n '2038,$p' DISPATCH_LOG.md | /usr/bin/grep -c 'WHAT: U[0-9]\|D6\|drawdown'
1
1:- [2026-11-08T22:27:00Z] WHO: praxis-master | WHAT: U8 `2026-11-08-park-card-filing` — NO RETURN by session
```
The one match is the U8 no-return row. All the other rows after :2037 are hook spawn/close rows.

### V6. Negative tests: the gates trip
```
stdin /tmp/cdf-dec-head.md differ: char 161885, line 1000
NEG1 one-space change at :1000 cmp exit=1
cmp: EOF on /tmp/cdf-dec-head.md
NEG2 1807 lines vs HEAD cmp exit=1
SHA2-256(stdin)= ac80cef776c1125d52c27b15c1ea508ff77948a55285098085c1a3327f0aaaf8
NEG3 above: block range off by one (1819-1851)
SHA2-256(stdin)= 8abe2924c6dee6695a644303dab9c7580ebb4f8d9b6ccc545d53f2419ce64763
NEG4 above: hyphen->en dash in approval line
```

## Adversarial findings

### W1 (ADVERSARIAL, U8 draft pointers; worker's output, excerpt)
```
| 1814 | HANDOFF.md:10–16 (twice), :16 | HANDOFF.md:63–69 | WRONG (known stale) ×3 |
| 1853 | "the fenced body's hash after insertion is pasted in the unit report `docs/reports/2026-11-08-park-card-filing-manager.md`" | that report, 30 lines | **WRONG**: no hash in it (output below) |
$ grep -n -i -E 'sha|dgst|[0-9a-f]{64}' docs/reports/2026-11-08-park-card-filing-manager.md
(no output)
$ git diff HEAD -- specs/SPEC_RUBRIC.md | grep '^@@'
@@ -272,6 +272,16 @@ blocked, move on" wording. ...
$ git diff -U0 HEAD -- specs/SPEC_RUBRIC.md | grep '^@@'
@@ -274,0 +275,10 @@ PRAXIS work.
Breakdown: 15 known-stale HANDOFF.md pointers plus 1 new (line 1853, the unit-report hash claim).
VERDICT: 16 WRONG of 181 checked
```
W1 also reported, outside the criterion, that the draft's "re-read … this unit (OBSERVED)" sentence failed S1 because U8's report shows no output. All four points are cured (Process log, items b, c, d and the -U0 fix). W1 checked every other pointer and found it OK. That covers the DECISION_LOG :741–743 quotes, the `bd show` states of diq/8sw/gjj, the rubric, vm-handoff, walkthrough and WF-spec-at-HEAD lines, and DECISIONS :748/:978/:1546/:1678/:1708/:1744–1745/:1774/:1783/:1801–1804. W1 noted that the working tree differed from the frozen copy. Those differences are this unit's own edits, made while W1 ran.

### W2 (ADVERSARIAL, finished entries)
(pending at time of writing; appended below)

## S6 cross-block check
Units and blocks that cite these entries (manager's reading, from the entries' own words):
- **D12 sequence** (voice-2 file :71–75): U7 resume (C1); rubric unit (C2, C6, C8, and D1–D5 as an "Autonomy" section); values spec (C5); VM handoff (C3, C9, C10); manager memory off (C7); park-commit gate exemption (C2, trip-tested); housekeeping (D9); F1 topology + F2 PROPOSAL (D8 (4)); F4 grading (D8 (5)); R6 research (D7). D6 comes first ("Sequence after D6").
- **Rubric unit**: amends S8's scope per D1–D5 and carries C2/C6/C8. This entry records the S8 change as a reading only. `specs/SPEC_RUBRIC.md` is not touched (it is not in this unit's write set, and `git status` above lists only DECISIONS.md, MANIFEST.md and this report as this unit's paths).
- **VM handoff** (`vm/2026-11-06-vm-handoff.md` §2): C3, C9, C10, and D8 (3) (start the VM session once the handoff carries the step-0 answers). Not edited here.
- **Blocks**: D2(b)/D8 (8) touch the Block 5 sign-off. D2(c) touches the circuit breakers (F1/F2, Block 3). D8 (5) touches F4. D8 (6) touches the P0 guard beads before Block 3 order code.
- The entries change no spec, rubric or code. Each entry's "What this entry does NOT do" says so. V4's `git status` and the brief's write set bound this unit to DECISIONS.md :1807+, MANIFEST.md :305+ and this report.

## Decisions taken
Each is the conservative option. None is a D2 item, so each is decided under the brief's instruction and D-2026-11-08-D D1. Amear may reverse any of them.
1. **U8's "NEEDS AMEAR" in C retitled "Open readings (not decided here)".** Neither item ((i) C5 (ii) vs the Rapid rows; (ii) C2 vs S7) is a D2 item. So under D1 neither waits for Amear. The entry still picks no reading: it names the acting unit (values-spec unit, rubric unit), which decides and logs "decided by master under D-2026-11-08-D D1". Rejected options: keeping "NEEDS AMEAR", which would route a non-D2 question to Amear (D5 calls that a defect when a recommendation is attached), and deciding the items in a filing entry.
2. **D's block copied verbatim into the entry**, as was done for C and B. The pointer-per-item bullets sit on top of it. This is more than a pointer-only filing. I chose it because it makes the entry hash-checkable.
3. **MANIFEST row 305 (U8's C-paste row) kept byte-identical** after its claims were checked. Rows 306–310 are this unit's.
4. **HANDOFF pointers re-pointed to the working-tree lines (:63–69)**, with a note on why they moved. HANDOFF.md is uncommitted, so these pointers can go stale again if HANDOFF changes before commit.

## Files staged
None. This unit stages nothing (brief hard limit). The index fingerprint is unchanged (V2 = V4: `5bfab445…bda95`, 12 paths). Unit paths, unstaged: DECISIONS.md (:1807–2007), MANIFEST.md (:305–310), this report.

Result: (pending W2)
