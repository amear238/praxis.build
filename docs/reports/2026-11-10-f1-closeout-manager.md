# Manager report: unit 2026-11-10-f1-closeout (bead Praxis_build-1hv)

Result: PASS

## Task

This is a filing unit, authorised by DECISION_LOG.md row 2026-11-10T13:36:00Z (praxis-master, decided under D-2026-11-08-D D1).
- (a) Append DECISIONS.md entry D-2026-11-10-B. It records the live-signal topology (`docs/specs/2026-11-10-live-signal-topology.md`, committed at `b4c3291`) as the working design.
- (b) Move rubric F1 from FROZEN to PASSED, after O1. Its text stays unchanged; it gains a State line and a filer's note.
- (c) Add MANIFEST rows.
- (d) Write this report.

Nothing was built or committed, and the real index was not touched.

## Rubric criteria addressed

- **F1** (`specs/SPEC_RUBRIC.md` HEAD :19–30). The master's 13:36:00Z row says the unblock clause is met. The rubric now records the state as PASSED@b4c3291, under A11 (:3–6) and D-2026-11-08-D D1.
- **S4** (HEAD :124). The NT8 emitter departs from CLAUDE.md's stated signal flow, and D-2026-11-10-B is the DECISIONS.md entry for it. The entry says plainly that it was filed after the design doc and before any build.
- **S6** (HEAD :126). The entry's S6 line comes from topology doc §7 (:112).
- **S8 / D2.** The entry names what stays with Amear:
  - under D2(d): the B1 HMAC key, `praxispush` provisioning and the B5 credential;
  - under D2(b): the order path to a funded account;
  - under D2(c): breaker values;
  - under D2(a): a paid data feed, which the doc raises only under option 2.
- **S13** (HEAD :133). The sentence appears once as a standalone line in the entry, and once at the end of this report.
- **A6** (DECISIONS.md:1744). F2 stays FROZEN; the F2 proposal is not adopted.

## Workers dispatched (id, mode, outcome)

| id | mode | outcome |
|---|---|---|
| aae789d7ba4e013a4 | ADVERSARIAL, foreground, read-only, 13 tool uses | Claim 1 (the entry over-claims) REFUTED narrowly: 2 defects and 3 weaker points. Claims 2 and 3 (the rubric move) NOT REFUTED. Every finding was fixed or recorded below. |

I made the doc edits myself, not through a worker. The brief limits edits to four named files, and the work is pure doc filing. The brief also forbids touching any other file, so the worker wrote no report file. It returned its findings in its final message, and they are summarised below.

## Process log

1. **Reading.** I read the rubric in full, the topology doc (114 lines, with line numbers), the tails of DECISIONS.md and MANIFEST, and DECISION_LOG rows 13:03Z–13:36Z. Then I wrote the report skeleton.
2. **DECISIONS entry.** I appended D-2026-11-10-B to DECISIONS.md, heading at :2047. Every claim in it cites a topology doc line.
3. **Rubric move, done by script.**
   - The script asserted the HEAD line texts at :19, :30 and :31. It then cut the block with its trailing blank line and re-inserted it before the `---` above `## OPEN — gradeable now`.
   - My first draft of the filer's note put the quoted clause in backticks. The clause has backticks of its own, so this broke the markdown. I rewrote the quote with double quotes.
   - I traced the "check 1" wording to its source. Row 13:34:00Z says "six of six" and "nine breaker names `cmp`-identical to the Phase 3 import". The words "check 1 PASS" come from the master's row at 13:36:00Z. The note now credits each phrase to its own row.
4. **MANIFEST.** I appended three rows at the end. I did not touch the parked unit's rows :307–314; its hunk `@@ -306,0 +307,8 @@` is unchanged.
5. **Adversarial pass.** The worker ran, then I applied fixes (see Adversarial findings). One fix added a bullet, so I changed the MANIFEST row's line range from 2046-2073 to 2046-2074.
6. **Withheld-term check.** No word was printed. I took the word tokens in `0eea766:DECISION_LOG.md` and removed those also in `HEAD:DECISION_LOG.md`. The script printed `scrubbed-word set size 1 ; hits in added content 0`. It checked the added diff lines of all three edited files plus a draft of this report. This only stands in for a test of the withheld term. It cannot test the category word; I could only avoid typing it.
7. **Hook block.** A first attempt to write this report through one Bash heredoc was blocked by `scripts/mint-guard.sh`. The heredoc text named the audit log file and contained shell redirections, and the guard reads that as a write to the audit log. Nothing was written: the report was still the 361-byte skeleton afterwards. I then wrote the report with the Write tool. I did not touch the audit log.

## Verification evidence (command output)

The commands below were run after the final edits to DECISIONS.md, the rubric and MANIFEST. The `grep -n F1` output was cut at 160 columns (`cut -c1-160`).

```text
$ cmp <(git show HEAD:DECISIONS.md) <(head -n 2045 DECISIONS.md) && echo PREFIX-OK
PREFIX-OK
$ git show HEAD:DECISIONS.md | wc -l; wc -l < DECISIONS.md
    2045
    2074
$ tail -n +2046 DECISIONS.md | grep -c -x '<S13 sentence>'
1
$ git diff specs/SPEC_RUBRIC.md
diff --git a/specs/SPEC_RUBRIC.md b/specs/SPEC_RUBRIC.md
index f03a4d6..77d7e14 100644
--- a/specs/SPEC_RUBRIC.md
+++ b/specs/SPEC_RUBRIC.md
@@ -16,19 +16,6 @@ State values: `FROZEN` (blocks dependent work) · `OPEN` (gradeable now) ·
 
 ## FROZEN — nothing downstream may proceed until these clear
 
-### F1 — Signal-path topology vs. circuit-breaker placement
-**Criterion.** A written statement, committed, naming what emits the live
-trading signal, and showing how each of the nine circuit breakers sits upstream
-of order submission on that path.
-**Why frozen.** Block 3 specifies the breakers as n8n workflow gates that
-terminate before the file-write node. Deviation A moved strategy logic into
-NinjaScript. If NT8 computes the signal internally there is no webhook, no n8n
-execution, and no gate — every breaker is bypassed and the Block 1 pipe is
-unused.
-**Unblocks when.** `docs/specs/*-live-signal-topology.md` exists, is committed,
-and the auditor confirms it addresses every one of the nine breakers by name.
-**Blocks.** Block 3 entirely. Any SHM threshold derivation.
-
 ### F2 — Session-flat time vs. breakers #4 and #5
 **Criterion.** One governing rule, written down, resolving: breaker #4 closes
 positions at 11:30 ET; breaker #5 disables everything 15:00–18:00 ET;
@@ -88,6 +75,22 @@ optimisation from the first pass. **Required:** a written statement of which
 gate set applies to the replication arm and whether GO/HOLD/REJECT sits on the
 replication arm or the later optimisation arm.
 
+Filer's note, not a ruling: F1 is moved here out of FROZEN. F1's own unblock clause, copied by script from its text at `b4c3291` :28–29 joined with one space: "**Unblocks when.** `docs/specs/*-live-signal-topology.md` exists, is committed, and the auditor confirms it addresses every one of the nine breakers by name." `docs/specs/2026-11-10-live-signal-topology.md` was committed at `b4c3291`. The auditor (DECISION_LOG 2026-11-10T13:34:00Z) graded check 1 PASS, with the nine breaker names byte-identical to the Phase 3 import (that row: "six of six", "nine breaker names `cmp`-identical to the Phase 3 import"; the check-1 numbering is the master's 2026-11-10T13:36:00Z row). The move is made under A11 (rubric :3–6) and D-2026-11-08-D D1 (DECISION_LOG 2026-11-08T19:57:00Z, WHO: amear) as the master's decision, changeable by Amear. The design itself is recorded in D-2026-11-10-B (DECISIONS.md).
+
+### F1 — Signal-path topology vs. circuit-breaker placement
+**State:** PASSED@b4c3291.
+**Criterion.** A written statement, committed, naming what emits the live
+trading signal, and showing how each of the nine circuit breakers sits upstream
+of order submission on that path.
+**Why frozen.** Block 3 specifies the breakers as n8n workflow gates that
+terminate before the file-write node. Deviation A moved strategy logic into
+NinjaScript. If NT8 computes the signal internally there is no webhook, no n8n
+execution, and no gate — every breaker is bypassed and the Block 1 pipe is
+unused.
+**Unblocks when.** `docs/specs/*-live-signal-topology.md` exists, is committed,
+and the auditor confirms it addresses every one of the nine breakers by name.
+**Blocks.** Block 3 entirely. Any SHM threshold derivation.
+
 ---
 
 ## OPEN — gradeable now
$ cmp <(git show HEAD:specs/SPEC_RUBRIC.md | sed -n '19,30p') <(sed -n '80p;82,92p' specs/SPEC_RUBRIC.md) && echo F1-BLOCK-IDENTICAL
F1-BLOCK-IDENTICAL
$ sed -n '80,81p' specs/SPEC_RUBRIC.md
### F1 — Signal-path topology vs. circuit-breaker placement
**State:** PASSED@b4c3291.
$ git diff --numstat specs/SPEC_RUBRIC.md
16	13	specs/SPEC_RUBRIC.md
$ grep -n F1 specs/SPEC_RUBRIC.md
78:Filer's note, not a ruling: F1 is moved here out of FROZEN. F1's own unblock clause, copied by script from its text at `b4c3291` :28–29 joined with one space
80:### F1 — Signal-path topology vs. circuit-breaker placement
453:    decided under D1, what is blocked under D2. No code names (F1, O1,
$ git diff -U0 MANIFEST.md | grep '^@@'
@@ -306,0 +307,8 @@
@@ -347,0 +356,3 @@
```

Only one other rubric line names F1: :453, which is :450 at HEAD. It sits inside the D-2026-11-08-D verbatim block ("No code names (F1, O1, ..."). It is outside both diff hunks and unchanged; only its line number moved, by +3. F2's "Blocks." line, at :45 at HEAD and :32 now, does not mention F1.

Negative tests: I tripped both checks once to show they can fail.

```text
$ cmp <(git show HEAD:specs/SPEC_RUBRIC.md | sed -n '19,30p') <(sed -n '80,91p' specs/SPEC_RUBRIC.md) || echo IDENTITY-CHECK-TRIPPED
/dev/fd/12 /dev/fd/13 differ: char 65, line 2
IDENTITY-CHECK-TRIPPED
$ cmp <(git show HEAD:DECISIONS.md) <(head -n 2045 DECISIONS.md | sed '2045s/$/ /') || echo PREFIX-CHECK-TRIPPED
/dev/fd/12 /dev/fd/13 differ: char 372316, line 2045
PREFIX-CHECK-TRIPPED
```

The first test compares HEAD's block with the moved block but leaves the State line in; the files differ at line 2, where the State line sits. The second appends one space to HEAD's last line, and the prefix check catches it.

## Adversarial findings

These come from worker aae789d7ba4e013a4, summarised from its final message.

1. **Defect, fixed.**
   - The entry said the consumer "adds checks for breakers #4, #5, #7, #8 and #9". But topology :48 lists only #4, #5, #8 and #9 as gaining a consumer-side check, and :64 calls #7's consumer check the existing `qty > MaxQty` reject.
   - The entry now says the consumer carries consumer-side checks for all five, per :41. The checks for #4, #5, #8 and #9 are new (:48, :61–62, :65–66). For #7 it is the existing reject, set to plan size (:64, :74).
2. **Defect, fixed.** The entry said "F2's state changes only on Amear's approval under A6". A6 at :1744 does not say "only". The entry now quotes A6's own words: "F2's state changes when Amear approves the proposed values".
3. **Weak point, fixed.** The list of items left with Amear did not include `praxispush` provisioning (B1 (c), D2(d), :86). It is added.
4. **Weak point, fixed.** #5's consumer check depends on the F2 proposal staying unadopted (:62). The entry now states that condition.
5. **Weak point, fixed.** The fuller CLAUDE.md quote and the commit-order fact came from outside the doc but were not flagged as such. Both are now flagged in the text: "quoted from CLAUDE.md itself" and "from git, not from the doc".
6. **Minor, recorded, not changed.** The A11 cite treats D1 as the logged Amear approval. That is the rubric's own reading, at :458 at HEAD and :461 now. The brief directed this cite.
7. **Minor, partly addressed.**
   - On S4 timing: the doc came before the entry. The entry now says so and cites the S4-gap finding in row 13:34:00Z.
   - The entry calls itself "filed after the design document and before any build work". That is the entry's own reading, not a cure.

The worker did not refute the other two claims.
- **Claim 2, the block is byte-identical.** The shasum of HEAD :19–30 equals the shasum of the working block minus the State line: `e62f1336dd2906b4b48c239d136e185e47a46710`. There are no CR bytes and no trailing-whitespace differences.
- **Claim 3, nothing else changed.** numstat is `16 13`, in two hunks. Both versions end in the bytes `29 2e 0a`.

The worker also noted that DECISION_LOG rows 13:34:00Z and 13:36:00Z, and the 13:32:36Z audit row, are in the working tree only, not in HEAD. The master flushes those.

There was no second adversarial pass on the fixes; the brief allows one worker. Instead I re-checked each fix's cites myself, against topology :48, :61–66, :74 and :86 and DECISIONS.md:1744. I re-ran the prefix and S13 counts after the fixes; the output is above.

## S6 cross-block check

- **The entry.** It touches no code, workflow or spec. It records a design whose cross-block touches are listed in topology doc §7 (:112): Blocks 1–5, Deviations A, C and G, D-2026-11-10-A, rubric F2, F4, O2 and O4, and the SHM thresholds.
- **The rubric move.** It changes only F1's state, and does not unfreeze anything downstream on its own.
  - F2 is still FROZEN and blocks Block 3 and Block 4 paper trading.
  - F3 blocks `4uu`.
  - F4 blocks Blocks 4 and 5.
  - So Block 3 stays blocked through F2, even with F1 PASSED.
- **Not advanced here.** Rubric O2 (:95–101 at HEAD) and the SHM threshold work are not graded or advanced by this unit.

## Files staged

None. The brief forbids index operations, and the real index still holds only the PNG. This unit changed these files in the working tree:
- `DECISIONS.md` (appended :2046–2074)
- `specs/SPEC_RUBRIC.md` (F1 move, State line, filer's note)
- `MANIFEST.md` (rows appended at :356–358)
- `docs/reports/2026-11-10-f1-closeout-manager.md` (this report, new)

## Line counts and hashes (pasted last, after the final edit)

```text
$ wc -l DECISIONS.md specs/SPEC_RUBRIC.md MANIFEST.md; openssl dgst -sha256 DECISIONS.md specs/SPEC_RUBRIC.md MANIFEST.md
    2074 DECISIONS.md
     461 specs/SPEC_RUBRIC.md
     358 MANIFEST.md
    2893 total
SHA2-256(DECISIONS.md)= ad453ecc2d37c397bf38d77fb7f14895efbf38313c77497bbeb045a451f298da
SHA2-256(specs/SPEC_RUBRIC.md)= baed55c2d8327307fe189f247221d0974fdbe8bea643451d7e4d9c6d7a32b6b2
SHA2-256(MANIFEST.md)= 87e2fb7ccd086a9ea478b7690e367a5662c7a376e8edb7244e3a930f1137cd4b
```

This report cannot carry its own hash. It is given in the manager's return to the master, computed after the final write.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
