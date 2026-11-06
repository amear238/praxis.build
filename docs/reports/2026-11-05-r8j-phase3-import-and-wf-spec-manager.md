# 2026-11-05 — r8j Phase 3 import and walk-forward spec — manager report

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## Task
This report covers unit `2026-11-05-r8j-phase3-import-and-wf-spec`, bead `Praxis_build-r8j` (P0). It was authorised by Amear in DECISION_LOG `2026-11-05T23:50:09Z` (WHO: amear), item b, and dispatched in DECISION_LOG `2026-11-05T23:55:05Z` (WHO: praxis-master). The unit had three deliverables:
1. Import the Phase 3 build specification.
2. Derive the walk-forward spec from the ledger only.
3. Append the ledger rows.

Nothing was bought. There was no NT8 connection, run or import. No commit was made and nothing was `git add`-ed.

## Rubric criteria addressed
These are quoted from `specs/SPEC_RUBRIC.md`:
- S1 | Every claim in a report has pasted command output, not a description of output.
- S2 | No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure.
- S4 | Every deviation from the plan has a DECISIONS.md entry with a traceable authorisation chain, written before the work, not after.
- S6 | Cross-block check: every approved deviation is tested against the specs of every other block it touches, not only its own.
- S8 | No question that belongs to Amear is answered on his behalf.
- The walk-forward spec also covers O1 (`:74-79`) and O4 (`:94-101`). Both are cited and left OPEN.

## Deliverables

| File | Lines / words | sha256 | State |
|---|---|---|---|
| `docs/specs/2026-11-05-phase3-build-specification.md` | 188 / 3,360 | `cd02d34ae635626e674f4316bdfd9ac14d96f819aaf28d39b7d651607be69b83` | untracked, unstaged |
| `docs/specs/2026-11-05-walk-forward-spec.md` | 224 / 5,544 | `b4341724134b0af1c2b268c7c38952f7f75cc801d84c72c61aad5ec0020d8645` | untracked, unstaged |
| `DECISIONS.md` | 879 → 922 lines (entry D-2026-11-05-C appended) | before `afed14e3…2567` → after `f91f421442390fb7069a614da8fe395cc7eb29c0677376b3b73b44e48716a876` | modified, unstaged |
| `MANIFEST.md` | 225 → 229 lines (4 rows appended) | before `784579e3…ea54` → after `4d1139ef2e38e6719f56082989322822894fbfbf340b1669d5b24420b276de47` | modified, unstaged |
| this report | — | — | untracked |

## Workers dispatched

| # | id | mode | task | outcome |
|---|---|---|---|---|
| W1 | a9dad9bcae70dcfec | BUILD | Phase 3 import | file written, 186 lines |
| W2 | a2fec27e639914278 | BUILD (research) | MFFU tier capture, 11 fetches of MFFU's own pages | captured; Flex row UNVERIFIED |
| W3 | ae9907833d0223b12 | BUILD | walk-forward spec | file written, 189 lines |
| A1 | aa4b02731731b2b99 | ADVERSARIAL | Phase 3 import | **FAIL**: 1 BLOCKER, 3 MAJOR, 3 MINOR |
| F1 | a2797be79fa6ccd00 | BUILD fix | Phase 3 header, 7 defects | applied; one prescribed parenthetical was corrected by the worker ("above", not "below") |
| A2 | aa2a53983d30384c7 | ADVERSARIAL | walk-forward spec | **FAIL**: 2 MAJOR, 5 MINOR |
| F2 | a7bb61bfbc85da6f4 | BUILD fix | walk-forward, 8 defects | applied |
| A3 | a538502617be6895f | ADVERSARIAL | Phase 3 import, post-fix | **FAIL**: 1 MAJOR, 2 MINOR |
| A4 | aae1f7a57bfa1269f | ADVERSARIAL | walk-forward, post-fix | **FAIL**: 4 MAJOR, several MINOR |
| F3 | ab318d1a71dfda12a | BUILD fix | Phase 3 header, 3 edits | applied |
| F4 | ab2cb2374a6c8515d | BUILD fix | walk-forward, G1–G7 | applied |
| A5 | a5a50c4e1247a05ce | ADVERSARIAL | walk-forward, post-fix-2 | **FAIL**: 1 MAJOR (the evidence section of this report did not exist yet), 4 MINOR |
| F5 | a87a054adcbd7fb84 | BUILD fix | walk-forward, M1–M4 | applied |

## Process log
1. The manager captured the source plaintext himself, then dispatched W1 and W2 in parallel.
2. The manager re-ran W1's counts, read its header and diffed its body. He negative-tested W1's comparator (see Verification evidence).
3. W3 and A1 ran in parallel.
4. A1's authority finding was verified by the manager: D-2026-08-06-A exists only at `f258a5d`. The fix brief carried exact replacement text.
5. F1 and A2 ran in parallel. F2 fixed the A2 defects.
6. A3 and A4 re-attacked the post-fix artifacts. The manager re-measured A4's weekend-date claim himself (output below). He confirmed R-VN3-3, R-VN3-5 and R-VN3-6 at `DECISIONS.md:488-516` before dispatching F3 and F4.
7. F3 changed the Phase 3 file's sha. The walk-forward spec pinned the old sha, so the manager updated that one sha token at walk-forward line 12 (`sed` on that line only, diff shown below).
8. A5 then attacked the walk-forward spec, and F5 fixed its four MINOR defects.
9. The ledger rows went on last. Each append ran in the same command as the re-read of the ledger.
10. **Not adversarially re-checked:** the final states after F3 (Phase 3) and F5 (walk-forward). Those two rounds applied exact manager-specified text and were verified only by the manager's re-run below, not by a fresh adversary.

## Verification evidence
All of this is manager-run output, pasted.

**Source, both specs, import body and per-item diffs (final state):**
```
$ textutil -convert txt -stdout "<source rtf>" | shasum -a 256; ... | wc -lw
d149bc8e11b18cd9db075dd4ad19c9ecea53b1f8e3c5460fcf583b83bc888de5  -
     111    2350
$ wc -lw <both specs>; shasum -a 256 <both specs>
     188    3360 docs/specs/2026-11-05-phase3-build-specification.md
     224    5544 docs/specs/2026-11-05-walk-forward-spec.md
     412    8904 total
cd02d34ae635626e674f4316bdfd9ac14d96f819aaf28d39b7d651607be69b83  docs/specs/2026-11-05-phase3-build-specification.md
b4341724134b0af1c2b268c7c38952f7f75cc801d84c72c61aad5ec0020d8645  docs/specs/2026-11-05-walk-forward-spec.md
$ diff <(sed -n "/^## Adapted Architecture/,$p" parked.md) <(sed -n "/^## Adapted Architecture/,$p" docs/specs/2026-11-05-phase3-build-specification.md); echo exit=$?
exit=0
$ python3 -I compare.py source.txt docs/specs/2026-11-05-phase3-build-specification.md <tmp>
--- breaker 1: source lines 44-44, 1 non-empty; repo match at normalised index [59]
diff exit code: 0
--- breaker 2: source lines 45-45, 1 non-empty; repo match at normalised index [60]
diff exit code: 0
--- breaker 3: source lines 46-46, 1 non-empty; repo match at normalised index [61]
diff exit code: 0
--- breaker 4: source lines 47-47, 1 non-empty; repo match at normalised index [62]
diff exit code: 0
--- breaker 5: source lines 48-48, 1 non-empty; repo match at normalised index [63] (compared from first em dash onward; title segment not printed)
diff exit code: 0
--- breaker 6: source lines 49-49, 1 non-empty; repo match at normalised index [64]
diff exit code: 0
--- breaker 7: source lines 50-50, 1 non-empty; repo match at normalised index [65]
diff exit code: 0
--- breaker 8: source lines 51-51, 1 non-empty; repo match at normalised index [66]
diff exit code: 0
--- breaker 9: source lines 52-52, 1 non-empty; repo match at normalised index [67]
diff exit code: 0
--- Block-2 Pass gates (src 31-38): source lines 31-38, 8 non-empty; repo match at normalised index [47]
diff exit code: 0
--- Block-4 gate text (src 58-68): source lines 58-68, 11 non-empty; repo match at normalised index [72]
diff exit code: 0
--- whole-source check: 97 non-empty normalised source lines
source non-empty lines with no exact normalised match in repo file: 1 (ordinal(s): [44])
$ T=<#5 title from source line 48, never printed>; grep -ciF "$T" <spec>; [REDACTED — de-identified per DECISION_LOG 2026-08-06T20:18:56Z]  (phase3, then wf)
docs/specs/2026-11-05-phase3-build-specification.md title=0 [REDACTED — de-identified per DECISION_LOG 2026-08-06T20:18:56Z]
docs/specs/2026-11-05-walk-forward-spec.md title=0 [REDACTED — de-identified per DECISION_LOG 2026-08-06T20:18:56Z]
$ sed -n 1p <each spec>; grep -n "^\*\*Status" wf
Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
5:**Status: DERIVED — not yet ruled on as a whole by Amear.**
$ grep -c "[REDACTED — de-identified per DECISION_LOG 2026-08-06T20:18:56Z]\|two tracked files\|elsewhere in the repository" phase3
0
$ grep -cw <placeholder token> <both specs>
docs/specs/2026-11-05-phase3-build-specification.md:0
docs/specs/2026-11-05-walk-forward-spec.md:0
$ (count of numbered NEEDS AMEAR items after the "## NEEDS AMEAR" heading at wf:194)
      29
$ git status --short docs/specs/2026-11-05-*; git diff --cached --name-only | wc -l
?? docs/specs/2026-11-05-phase3-build-specification.md
?? docs/specs/2026-11-05-walk-forward-spec.md
      12
```

**What differs from the source:**
- Ordinal [44] is source line 48, breaker #5. It is the only source line without an exact normalised match, because its title is de-identified.
- From the em dash onward, line 48 is identical to the source.
- Everything else that differs is markdown markup (bullets/tabs → list syntax, heading markers) or dropped trailing U+200B, plus the labelled header notes and line 1.

**Comparator negative test.** Two characters were mutated in a copy of the spec (gate 1.30 → 1.35; "2 consecutive losers" → "3"). The comparator flags both:
```
> OOS profit factor ≥ 1.35
diff exit code: 1
...
source non-empty lines with no exact normalised match in repo file: 3 (ordinal(s): [29, 42, 44])
```
The output also showed breaker 3 with `diff exit code: 1` and an empty `>` side.

**Breaker status basis, the baseline pin and the data-file pin (walk-forward §2 and §5 point here):**
```
$ shasum -a 256 ninjascript/PraxisNoiseAreaBreakout.cs; git log -1 --format=%h -- ninjascript/PraxisNoiseAreaBreakout.cs; git status --short ninjascript/PraxisNoiseAreaBreakout.cs
35393823e9bc146e95dcb1d9f6fe5785a3c72ee3a3fb71287f33fe2242752265  ninjascript/PraxisNoiseAreaBreakout.cs
719ab11
$ ls -l ~/praxis-signals/b2-data/NQ-continuous-1min.nt8import.txt | awk "{print \$5}"; shasum -a 256 <same> | cut -c1-64; wc -l < <same>
95900139
307c5e8af1da42b7606d666f14e4f34228feec50d19dd52d25396aae1b16e454
 1857362
$ grep -rniE "breaker|circuit" ninjascript/ | cut -c1-120
ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:31:// This variant does NOT decide rubric F2 (session-flat time vs break
$ grep -n MaxQty ninjascript/PraxisSignalConsumer.cs | cut -c1-90
94:				MaxQty             = 5;                         // sim sanity cap
527:			if (d > MaxQty)
528:				return "'qty' " + d + " exceeds sim MaxQty cap " + MaxQty;
858:		public int MaxQty { get; set; }
```

**Window-count basis (walk-forward §4; manager-run, script quoted in the F4 brief):**
```
dates_with_RTH_bars 1494 weekend 141 weekday 1353 first_weekend ['20210314', '20210320', '20210328']
windows(252+63, step 63) on weekday dates: 17 leftover 30
```

**Authority check behind the A1 finding:**
```
main DECISIONS D-2026-08-06-A: 0
HEAD: 0
parked: 1
$ git show HEAD:DECISION_LOG.md | grep -c '\[2026-08-06T20:18:56Z\] \*\*WHO: amear'
1
```

**Manager's one-token edit to walk-forward line 12 (stale Phase 3 sha):**
```
12c12
< 4. `docs/specs/2026-11-05-phase3-build-specification.md` (188 lines, sha256 `0f798a4adf9df12c066e1fd15392c78a6bb4a345e1894a9af0e9a12d7cc41
---
> 4. `docs/specs/2026-11-05-phase3-build-specification.md` (188 lines, sha256 `cd02d34ae635626e674f4316bdfd9ac14d96f819aaf28d39b7d651607be69
```

**Ledger appends.** Each ledger was re-read in the same command as its append. Appending was by `cat >>` from scratch files, so no overwrite was possible; Edit/Write were not used on either ledger. Both quotes were checked first: `grep -cF` of item b and of ruling 1 gives 1 against the DECISION_LOG row and 1 in the entry.
```
== DECISIONS.md BEFORE: 879 lines, afed14e36f39135cff9be9999e5484a28388a53ffda26fae4440ff55484a2567
5. The gate, the provenance library, the tripwire and the verifier are not changed.
== MANIFEST.md BEFORE: 225 lines, 784579e3b3cfbd88dd9d2d38d982ad46401ed08df178ce0318368454a685ea54
| /docs/reports/2026-11-05-addendum-filing-manager.md | Report | 2 | 2026-11-05 | Manager report for
== DECISIONS.md AFTER: 922 lines, f91f421442390fb7069a614da8fe395cc7eb29c0677376b3b73b44e48716a876
== MANIFEST.md AFTER: 229 lines, 4d1139ef2e38e6719f56082989322822894fbfbf340b1669d5b24420b276de47
DECISIONS prefix unchanged
MANIFEST prefix unchanged
DECISIONS tail = entry
MANIFEST tail = rows
```
DECISIONS.md was 857 lines when this unit started and 879 just before the append, so a concurrent unit appended in between. Nothing of theirs was altered: the prefix `cmp` above returns identical.

## Adversarial findings
**Phase 3 import**

A1 (FAIL), all fixed by F1:
- BLOCKER: the header leaked a property of the #5 title [REDACTED — de-identified per DECISION_LOG 2026-08-06T20:18:56Z].
- MAJOR: the header pointed to a count of the files where the term occurs.
- MAJOR: it cited `D-2026-08-06-A` as authority, but that entry is absent on main.
- MAJOR: line 1 was unlabelled.
- MINOR: "zero implemented" rested on a keyword search only. A scope note was added: `PraxisSignalConsumer.cs` has a MaxQty cap that resembles #7.
- MINOR: tab/heading wording.
- MINOR: "Afternoon" was undisclosed as importer wording.

A3 (FAIL), fixed by F3 with exact text:
- MAJOR: the replacement sentence still asserted the term exists elsewhere.
- MINOR: line 3 claimed an "every new file" rule. The ledger rule is that every backtest report carries the line (`DECISIONS.md:302`).
- MINOR: tab description.

**Walk-forward spec**

A2 (FAIL), fixed by F2:
- MAJOR: Phase 3 pointers were off by 2 after the import note was inserted.
- MAJOR: a CONDITIONAL entry was graded RULED and called "superseded".
- 5 MINOR.

A4 (FAIL), fixed by F4:
- MAJOR: R-VN3-5 (breakers on once built; the agent's reading, confirmed by Amear in voice only) and R-VN3-6 were omitted.
- MAJOR: R-VN3-3 (data as is) was omitted, and the gaps were re-asked.
- MAJOR: the day-count convention counted 141 weekend dates. The manager re-measured this (output above); the result is 17 windows, not 19.
- MAJOR: an evidence pointer led to the empty report skeleton.
- Several MINOR.

A5 (FAIL):
- MAJOR: this report's evidence section did not exist yet. It is resolved by the section above, which pastes the baseline, data and window counts.
- 4 MINOR (notes-2 qualifier, an unlabelled identification, an inconsistent pointer range, a missing status). F5 fixed all four.

**Residual (A5, disclosed in the spec; not a defect):**
- Weekday exchange holidays are inside the 1,353 Monday–Friday dates. Dropping them could give 16 windows instead of 17.
- The spec routes this to NEEDS AMEAR 26.

## S6 cross-block check
**F1, F2, F3, F4 (rubric `:17`, `:30`, `:45`, `:59`):** untouched and not discharged.
- Both specs say so.
- `git diff --quiet HEAD -- ninjascript/` exits 0, and no hook was edited by this unit. `.claude/hooks/` shows diff-exit 1, but `audit-approve.sh` and `gate-commit.sh` were already modified in the session-start git status, before this unit.
- The Phase 3 import labels its Block-2 configuration (High resolution, 1-tick) against the standing limitation as open under F3.

**Blocks the walk-forward spec touches:**
- **Block 2:** pass gates, windows, configuration, the DD-gate base. O1 stays OPEN.
- **Block 3:** how breakers and the arm-(b) stop are modelled in a backtest, quoted from ruling 1 only. The breakers are not built, which is NEEDS AMEAR 24.
- **Block 4:** the O4 parity gate stays OPEN.
- **Account tier:** a table only. No tier is chosen (D-2026-11-05-A item 5).
- The Phase 3 import changes no block's design text.

**Hard limits:**
- The old 12-path staged set is unchanged in count (`git diff --cached --name-only | wc -l` → 12), and no 2026-11-05 path was staged.
- The parked branch tip is still `f258a5d`.
- Root `F` was not touched.

## NEEDS AMEAR
See `docs/specs/2026-11-05-walk-forward-spec.md`, section `## NEEDS AMEAR` (heading at line 194), items 1–29. They are questions only; none is answered.

Also open for the master (housekeeping, not decided here): whether `D-2026-08-06-A` is carried from `f258a5d` to `DECISIONS.md` on main.

## Files staged
None. This unit staged nothing: the staged set is the pre-existing 12 paths. Changed in the working tree:
- `docs/specs/2026-11-05-phase3-build-specification.md` (new)
- `docs/specs/2026-11-05-walk-forward-spec.md` (new)
- `DECISIONS.md` (+43 lines)
- `MANIFEST.md` (+4 rows)
- this report (new)

## Result
**Result: PASS** (manager stress-test, not a grade). Every adversarial defect was fixed and verified by the manager's re-run above. The last fix round on each file (F3, F5) was not re-attacked by a fresh adversary. The auditor grades.

## Correction 1 (2026-11-06, after audit FAIL 1)

Authority: DECISION_LOG row `[2026-11-06T00:43:51Z] WHO: praxis-master` (audit FAIL 1; logs the in-place redaction as a deliberate exception to append-only), under the de-identification ruling at DECISION_LOG row `[2026-08-06T20:18:56Z] **WHO: amear**`. Everything below this heading is appended. Above it, only the tokens listed in (a) were changed. Scratch files are under `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/corr-r8j/` (written `<C>` below).

### (a) Redaction record
- Before the redaction: sha256 `4accc0eddf5a350ecfad123b99cb362c45eba15f957e6f655d1dd9200ede52ef`, 264 lines. A copy was kept at `<C>/report.pre-redaction.md`. That copy is outside the repo and must not be imported.
- After the redaction, before this section: sha256 `b1e36dfa898e78ba49679ab29e7c1e581478cf5010bf30ad22ae614a1ff1440d`, 264 lines. The line count is unchanged.
- Lines edited: **103, 104, 105, 110, 197**. On each line only the leaking token was replaced; the rest of the line is as it was.
- Replacement token: `[REDACTED — de-identified per DECISION_LOG 2026-08-06T20:18:56Z]`.
- Script `<C>/scripts/redact.py` asserts exactly one match per line before it edits. Its output, followed by the pre-vs-post diff hunk headers (the `<` side is not pasted because it is the leak):
```
line 103: edited
line 104: edited
line 105: edited
line 110: edited
line 197: edited
$ diff <C>/report.pre-redaction.md <report> | grep '^[0-9]'
103,105c103,105
110c110
197c197
```
- Absence check, `python3 -I <C>/scripts/absence.py "<source rtf>" <C>/patterns.txt <file>`. P1 is the full #5 title. The script cuts it from `textutil` source line 48 at run time; it is never printed or stored. P2–P5 are the four leak tokens the audit named, read from `<C>/patterns.txt` so they appear nowhere in this report. Counts are case-insensitive.
  - Positive arm: on the source plaintext `r8j/source.txt`, P1 = 1. On the pre-redaction copy, P2 = 1, P3 = 2, P4 = 1, P5 = 1.
  - On this report after the redaction (before this section was appended):
```
<report>: P1 (full #5 title, from source line 48, not printed): 0
<report>: P2 (patterns.txt line 1): 0
<report>: P3 (patterns.txt line 2): 0
<report>: P4 (patterns.txt line 3): 0
<report>: P5 (patterns.txt line 4): 0
```
  - On both specs (the auditor already found them clean; re-run here):
```
docs/specs/2026-11-05-phase3-build-specification.md: P1 (full #5 title, from source line 48, not printed): 0
docs/specs/2026-11-05-phase3-build-specification.md: P2 (patterns.txt line 1): 0
docs/specs/2026-11-05-phase3-build-specification.md: P3 (patterns.txt line 2): 0
docs/specs/2026-11-05-phase3-build-specification.md: P4 (patterns.txt line 3): 0
docs/specs/2026-11-05-phase3-build-specification.md: P5 (patterns.txt line 4): 0
docs/specs/2026-11-05-walk-forward-spec.md: P1 (full #5 title, from source line 48, not printed): 0
docs/specs/2026-11-05-walk-forward-spec.md: P2 (patterns.txt line 1): 0
docs/specs/2026-11-05-walk-forward-spec.md: P3 (patterns.txt line 2): 0
docs/specs/2026-11-05-walk-forward-spec.md: P4 (patterns.txt line 3): 0
docs/specs/2026-11-05-walk-forward-spec.md: P5 (patterns.txt line 4): 0
```
- The whole file was re-read for other hints: word or character counts, first or last letters, initials, rhymes, the rationale. Nothing else was found. Two passages were looked at and left alone, because they describe the import, not the title: the em-dash wording at :87 and :124–125 (every breaker line in the source has that form), and "the term" at :198 and :206. The master may still want to decide whether :198/:206 and the untouched `two tracked files` / `elsewhere in the repository` grep terms at :110 need a ruling of their own; that is not decided here.

### (b) S1 pastes

**Session counts.** Script `<C>/scripts/sessions.py`, run read-only on the data file, in full:
```
# Read-only session count over the NT8 import file. Usage: python3 -I sessions.py <file>
import sys, hashlib, datetime
path = sys.argv[1]
h = hashlib.sha256(); rth = {}; alldates = set(); n = 0
with open(path, "rb") as f:
    for raw in f:
        h.update(raw); n += 1
        d, t = raw[:8].decode(), raw[9:15].decode()   # "yyyyMMdd HHmmss;..."
        alldates.add(d)
        if "093100" <= t <= "160000":
            rth[d] = rth.get(d, 0) + 1
wd = lambda d: datetime.date(int(d[:4]), int(d[4:6]), int(d[6:])).weekday()
sat = sorted(d for d in rth if wd(d) == 5); sun = sorted(d for d in rth if wd(d) == 6)
wkend = sorted(sat + sun); wkday = sorted(d for d in rth if wd(d) < 5)
run4 = [d for d in wkday if "20210308" <= d <= "20260717"]
print("sha256", h.hexdigest(), "lines", n)
print("dates_with_RTH_bars(09:31-16:00)", len(rth))
print("weekend_dates", len(wkend), "sat", len(sat), "sun", len(sun), "weekend_RTH_bars", sum(rth[d] for d in wkend), "first3", wkend[:3])
print("weekday_dates_whole_file", len(wkday), "first", wkday[0], "last", wkday[-1])
print("weekday_dates_run4_range(20210308-20260717)", len(run4))
print("all_distinct_dates", len(alldates))
for lab, N in (("whole", len(wkday)), ("run4", len(run4))):
    print(f"windows {lab}: N={N} floor(({N}-252)/63)={(N-252)//63} remainder={(N-252)%63}")
```
`$ python3 -I <C>/scripts/sessions.py ~/praxis-signals/b2-data/NQ-continuous-1min.nt8import.txt`
```
sha256 307c5e8af1da42b7606d666f14e4f34228feec50d19dd52d25396aae1b16e454 lines 1857362
dates_with_RTH_bars(09:31-16:00) 1494
weekend_dates 141 sat 44 sun 97 weekend_RTH_bars 201 first3 ['20210314', '20210320', '20210328']
weekday_dates_whole_file 1353 first 20210308 last 20260720
weekday_dates_run4_range(20210308-20260717) 1352
all_distinct_dates 1712
windows whole: N=1353 floor((1353-252)/63)=17 remainder=30
windows run4: N=1352 floor((1352-252)/63)=17 remainder=29
```
The script hashes the file as it reads it, and the sha matches the pin `307c5e8a…` at walk-forward §5 (`:99`). Results: 1,494 dates with a bar at 09:31–16:00; 141 weekend dates (44 Saturday, 97 Sunday) carrying 201 such bars; 1,353 Monday–Friday dates in the whole file; 1,352 in the run-4 range; 1,712 distinct dates of any kind. Windows: (17, remainder 30) for the whole file and (17, remainder 29) for the run-4 range.

**Parked-vs-new spec comparator.** `<parked>` is `git show f258a5d:docs/specs/2026-08-06-phase3-build-specification.md` saved to `<C>/parked-f258a5d.md`, sha256 `33250d8dcbc4b3d29cb772b0c74829c57c17664680e3a072513ec0194ea409db`. That is the same sha as the earlier capture `r8j/parked.md`. Hunk headers only are pasted for the whole-file diff: the text of the `<` side of hunk `11c15` gives a P2 count of 1 on the absence check, so it is not reproduced here.
```
$ diff <parked> docs/specs/2026-11-05-phase3-build-specification.md | grep "^[0-9]"   # whole file
0a1,4
7c11
11c15
15c19,26
whole-file diff exit=1
$ diff <(sed -n "/^## Adapted Architecture/,$p" <parked>) <(sed -n "/^## Adapted Architecture/,$p" docs/specs/2026-11-05-phase3-build-specification.md); echo exit=$?
exit=0
$ grep -n "^## Adapted Architecture" <parked> docs/specs/2026-11-05-phase3-build-specification.md
<parked>:17:## Adapted Architecture: Your Server, Not a VPS
docs/specs/2026-11-05-phase3-build-specification.md:28:## Adapted Architecture: Your Server, Not a VPS
```
So the whole-file diff has four header hunks (lines 1–15 of the parked file against lines 1–26 of the new one). From the `## Adapted Architecture` heading on (parked :17, new :28) the body is byte-identical (exit 0). **This is a new finding for the master:** the parked commit `f258a5d` (a committed file, on a parked branch, not on main) contains a P2 hit in its header at parked line 11. Its history is not changed by this unit.

**MFFU tier excerpts.** `$ zsh <C>/scripts/mffu-rows.sh <C>/../r8j/w2-mffu-tiers.txt`. The capture's sha256 is `72e6abccd3aa2b27e14b96a400f407124a3bfb3d39c0017790df3bb5e91dfa3a`, fetched 2026-11-05 23:58Z–2026-11-06 00:00Z (untrusted page data; read only, never executed). The script greps each walk-forward §6 row's line in the capture's TABLE and the matching home-page JSON product line, plus page text where §6 cites it. Lines are cut to 200 columns:
```
-- WF §6 row: Studio #003 · 5K
86:Studio | Studio #003 | account_size=5000 max_drawdown_amount=250 drawdown_mode="Static" drawdown_mode_in_funded="Static" daily_drawdown=0 daily_drawdown_in_funded=0 dll_hard_breach=0 max_position_s
152:Studio#003 | 5K   | 250                 | Static       | Static                          | 0 / 5 micros (no minis)       | None             | REPORTED — help art. 17589665 (+/studio "5 contracts
-- WF §6 row: Studio #001 · 10K
87:Studio | Studio #001 | account_size=10000 max_drawdown_amount=500 drawdown_mode="Static" drawdown_mode_in_funded="Static" daily_drawdown=0 daily_drawdown_in_funded=0 dll_hard_breach=0 max_position_
153:Studio#001 | 10K  | 500                 | Static       | Static                          | 0 / 10 micros (no minis)      | None             | REPORTED — help art. 17589665 (+JSON 10)
-- WF §6 row: Studio #002 · 20K
88:Studio | Studio #002 | account_size=20000 max_drawdown_amount=1000 drawdown_mode="Static" drawdown_mode_in_funded="Static" daily_drawdown=0 daily_drawdown_in_funded=0 dll_hard_breach=0 max_position
154:Studio#002 | 20K  | 1,000               | Static       | Static                          | 0 / 20 micros (no minis)      | None             | REPORTED — help art. 17589665 (+JSON 20)
-- WF §6 row: Rapid · 25K
73:Rapid | Rapid 25K | account_size=25000 max_drawdown_amount=1000 drawdown_mode="EOD" drawdown_mode_in_funded="RealTime" daily_drawdown=0 daily_drawdown_in_funded=0 dll_hard_breach=0 max_position_siz
139:Rapid      | 25K  | 1,000               | EOD          | Intraday trailing (locks +$100) | 3/30 ; 3/30                   | None             | REPORTED — /plans/rapid (+home JSON)
-- WF §6 row: Rapid EOD · 25K
77:Rapid EOD | Rapid EOD 25k | account_size=25000 max_drawdown_amount=1000 drawdown_mode="EOD" drawdown_mode_in_funded="EOD" daily_drawdown=0 daily_drawdown_in_funded=0 dll_hard_breach=0 max_position_
143:Rapid EOD  | 25K  | 1,000               | EOD          | EOD trailing                    | 2/20 ; 2/20                   | None             | REPORTED — /plans/rapid-eod table (+JSON); card text
-- WF §6 row: Builder · 25K
82:Builder | Builder 25K | account_size=25000 max_drawdown_amount=1000 drawdown_mode="EOD" drawdown_mode_in_funded="EOD" daily_drawdown=600 daily_drawdown_in_funded=600 dll_hard_breach=0 max_position_
148:Builder    | 25K  | 1,000               | EOD trailing | EOD trailing                    | 2/20                          | $600 soft pause  | REPORTED — /plans/builder (+JSON)
-- WF §6 row: Rapid · 50K
74:Rapid | Rapid 50K | account_size=50000 max_drawdown_amount=2000 drawdown_mode="EOD" drawdown_mode_in_funded="RealTime" daily_drawdown=0 daily_drawdown_in_funded=0 dll_hard_breach=0 max_position_siz
140:Rapid      | 50K  | 2,000               | EOD          | Intraday trailing               | 5/50 ; 5/50                   | None             | REPORTED — /plans/rapid (+home JSON)
-- WF §6 row: Rapid EOD · 50K
78:Rapid EOD | Rapid EOD 50k | account_size=50000 max_drawdown_amount=2000 drawdown_mode="EOD" drawdown_mode_in_funded="EOD" daily_drawdown=0 daily_drawdown_in_funded=0 dll_hard_breach=0 max_position_
128:Stage Account Parameters | Parameters | Rapid EOD - $50,000 | Initial Balance | $0 | Maximum Drawdown (MLL) | $2,000 | Drawdown Type | End-of-Day (EOD) Trailing | Daily Loss Limit | None | Max Con
144:Rapid EOD  | 50K  | 2,000               | EOD          | EOD trailing (locks $100)       | 3/30 ; 3/30                   | None             | REPORTED — /plans/rapid-eod + help art. 16158363 (+J
-- WF §6 row: Pro · 50K
79:Pro | Pro 50K | account_size=50000 max_drawdown_amount=2000 drawdown_mode="EOD" drawdown_mode_in_funded="EOD" daily_drawdown=0 daily_drawdown_in_funded=0 dll_hard_breach=0 max_position_size=3 max_p
145:Pro        | 50K  | 2,000               | EOD          | EOD trailing                    | 3/30 ; 3/3                    | None             | REPORTED — /plans/pro (+JSON micro factor funded=1)
-- WF §6 row: Builder · 50K
83:Builder | Builder 2.0K | account_size=50000 max_drawdown_amount=2000 drawdown_mode="EOD" drawdown_mode_in_funded="EOD" daily_drawdown=1000 daily_drawdown_in_funded=1000 dll_hard_breach=0 max_positi
114:Trailing) | $1,000 | $2,000 | ($1,500 with add-on) | $3,000 | $4,500 | Starting Floor | $24,000 | $48,000 | ($48,500 with add-on) | $97,000 | $145,500 | Daily Loss Limit | $600 - soft pause | $1,0
149:Builder    | 50K  | 2,000 ($1,500 w/ add-on) | EOD trailing | EOD trailing               | 4/40                          | $1,000 soft pause| REPORTED — /plans/builder (+JSON)
173:4. Builder 50K: home/plan card "Max Drawdown 1.5k or 2k"; table "$2,000 ($1,500 with add-on)"; JSON 2000; JSON public_name "Builder 2.0K".
-- WF §6 row: Rapid · 100K
75:Rapid | Rapid 100K | account_size=100000 max_drawdown_amount=3000 drawdown_mode="EOD" drawdown_mode_in_funded="RealTime" daily_drawdown=0 daily_drawdown_in_funded=0 dll_hard_breach=0 max_position_s
141:Rapid      | 100K | 3,000               | EOD          | Intraday trailing               | 8/80 ; 8/80                   | None             | REPORTED — /plans/rapid (+home JSON)
-- WF §6 row: Pro · 100K
80:Pro | Pro 100K | account_size=100000 max_drawdown_amount=3000 drawdown_mode="EOD" drawdown_mode_in_funded="EOD" daily_drawdown=0 daily_drawdown_in_funded=0 dll_hard_breach=0 max_position_size=6 max
146:Pro        | 100K | 3,000               | EOD          | EOD trailing                    | 6/60 ; 6/6                    | None             | REPORTED — /plans/pro
-- WF §6 row: Builder · 100K
84:Builder | Builder 100K | account_size=100000 max_drawdown_amount=3000 drawdown_mode="EOD" drawdown_mode_in_funded="EOD" daily_drawdown=1750 daily_drawdown_in_funded=1750 dll_hard_breach=0 max_posit
150:Builder    | 100K | 3,000               | EOD trailing | EOD trailing                    | 6/60                          | $1,750 soft pause| REPORTED — /plans/builder (+JSON)
-- WF §6 row: Rapid · 150K
76:Rapid | Rapid 150K | account_size=150000 max_drawdown_amount=4500 drawdown_mode="EOD" drawdown_mode_in_funded="RealTime" daily_drawdown=0 daily_drawdown_in_funded=0 dll_hard_breach=0 max_position_s
142:Rapid      | 150K | 4,500               | EOD          | Intraday trailing               | 10/100 ; 10/100               | None             | REPORTED — /plans/rapid (+home JSON)
-- WF §6 row: Pro · 150K
81:Pro | Pro 150K | account_size=150000 max_drawdown_amount=4500 drawdown_mode="EOD" drawdown_mode_in_funded="EOD" daily_drawdown=0 daily_drawdown_in_funded=0 dll_hard_breach=0 max_position_size=9 max
147:Pro        | 150K | 4,500               | EOD          | EOD trailing                    | 9/90 ; 9/9                    | None             | REPORTED — /plans/pro
-- WF §6 row: Builder · 150K
85:Builder | Builder 150K | account_size=150000 max_drawdown_amount=4500 drawdown_mode="EOD" drawdown_mode_in_funded="EOD" daily_drawdown=2500 daily_drawdown_in_funded=2500 dll_hard_breach=0 max_posit
151:Builder    | 150K | 4,500               | EOD trailing | EOD trailing                    | 9/90                          | $2,500 soft pause| REPORTED — /plans/builder (+JSON)
-- WF §6 row: Flex
72:## initialProducts occurrence 1 groups ['Rapid', 'Rapid EOD', 'Flex', 'Pro', 'Builder', 'Studio']
155:Flex       | —    | —                   | —            | —                               | —                             | —                | UNVERIFIED — JSON group "Flex" present w
```
All 17 §6 rows have a TABLE line, and every size and limit in §6 matches it. Flex is UNVERIFIED in both places. The Builder 50K JSON product name reads `Builder 2.0K` with `account_size=50000`; this is how it appears in the capture.

### (c) D-2026-11-05-C "exits 0", corrected here by note
`DECISIONS.md:893` (D-2026-11-05-C) says: "Its body is identical to the parked conversion: `diff` against `git show f258a5d:…` exits 0." This is true only of the **body** comparison (from `## Adapted Architecture` on). The whole-file `diff` exits 1 with four header hunks, as pasted in (b). DECISIONS.md is not edited in this unit, so this note is the correction of record until the master changes the entry.

### (d) OBSERVED is missing from the walk-forward spec's legend
```
$ grep -n OBSERVED docs/specs/2026-11-05-walk-forward-spec.md | cut -c1-12; sed -n 22p docs/specs/2026-11-05-walk-forward-spec.md | grep -c OBSERVED
66:- Code: `
84:  - whole
99:- File: `
221:26. **We
0
```
The walk-forward spec grades statements OBSERVED at :66, :84 and :99. Line :221 (NEEDS AMEAR 26) repeats ":84" as "§4, OBSERVED". The evidence-grade legend at :22 lists RULED, REPORTED BY, INFERRED and UNVERIFIED, and leaves OBSERVED out (count 0 above). As used there, OBSERVED means "observed this session; the commands and output are in this report". The spec is not edited in this unit.
