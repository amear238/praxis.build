# Session 46 — independent grade of the session-45 adoption report and v0.2 gap list

**Session 46 · 2026-08-08 · author: praxis-auditor · GRADE, not producer testimony**

Artifacts graded (read in full, nothing else read):

- A. `docs/reports/2026-08-08-session45-project-kit-adoption.md` (100 lines)
- B. `docs/reports/2026-08-08-project-kit-v0.2-gap-list.md` (72 lines)
- C. `docs/specs/2026-08-08-ledger-compaction-spec.md` (101 lines) — the artifact A and B describe

Read-only audit. Nothing changed, staged or committed. All toggle variants were built in the
session scratchpad, never in the repo.

The `tr '\n' ' '` whitespace defect was supplied to me as established prior art with controls.
It is not claimed here as a finding. What follows is re-measurement of A's figures and a
mechanism toggle A never performed.

---

## 0. Directly answering the question put

**Do the post-run figures reproduce?** Yes, all six, exactly.

```
$ S=docs/specs/2026-08-08-ledger-compaction-spec.md
$ grep -o 'dispatched' "$S" | wc -l
       6
$ tr '\n' ' ' < "$S" | grep -c 'since the last compaction'
1
$ sed -n '/^## CONFORMANCE/,$p' "$S" | tr '\n' ' ' | grep -c 'tokenizer'
1
$ sed -n '/^## CONFORMANCE/,$p' "$S" | tr '\n' ' ' | grep -c 'byte'
1
$ tr '\n' ' ' < "$S" | grep -c 'one run late'
1
$ sed -n '1,/^## CONFORMANCE/p' "$S" | sed '$d' | wc -l
      60
```

A reports `C1=6  C2=1  C3a=1  C3b=1  C4=1  body=60`. Match on every figure.

Note the reconstruction cost. A pastes no command for any check, so the check definitions had
to be inferred. `C3b=1` only reconciles under one reading: `grep -c` against text already
flattened to a single line, so the value is a 0/1 presence bit, not an occurrence count. The
raw occurrence count of `byte` inside CONFORMANCE is 4, and the raw line count is 4:

```
$ sed -n '/^## CONFORMANCE/,$p' "$S" | grep -c 'byte'
4
```

Three readings were tried before one matched. That is a direct consequence of S1 being unmet.

**Do the baselines reproduce?** No — `UNVERIFIABLE`. The baselines were taken against the
pre-amendment spec, which exists nowhere retrievable:

```
$ git log --all --oneline -- docs/specs/2026-08-08-ledger-compaction-spec.md
$ git stash list
$ git ls-files -s -- docs/specs/2026-08-08-ledger-compaction-spec.md
100644 e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 0	docs/specs/2026-08-08-ledger-compaction-spec.md
```

No commit, no stash, no blob. `e69de29` is the empty blob. The validity precondition — the line
on which A's whole "no literal disqualified" argument rests — cannot be checked by anyone.

**Is any PASS load-bearing on formatting rather than content?** Yes, two of five.

| Check | Phrase | Where it sits in C | Wrap-fragile? |
|---|---|---|---|
| C2 | `since the last compaction` | line 32, one unwrapped line: `### 2.3 DISPATCHED — the boundary is since the last compaction` | **YES** |
| C3a | `tokenizer` | line 66, single token inside a word (`tokenizers`) | No — a single token cannot straddle a break |
| C3b | `byte` | lines 65–68, single token | No — same |
| C4 | `one run late` | line 73, one unwrapped line: `...rows abandoned in it archive one run late.` | **YES** |

C2 and C4 are multi-word literals that survive only because the author left those two lines
unwrapped. C3a and C3b are single tokens and are immune to the defect entirely. A's table
presents all four as the same kind of result, which they are not.

---

## 1. The toggle A never ran (S9, ruling-R3 form)

R3: *toggle Y, hold everything else constant, show the behaviour changes.* The mechanism claim
under test is A's own: that C2 and C4 pass *because the phrases were kept unwrapped*. So
reflow those two lines and nothing else.

```
C2 baseline (unmodified, tr only)      : 1
C2 reflow TAB      (tr only)           : 0     [mechanism confirmed: check dies]
C2 reflow TAB      (tr + tr -s ' ')    : 0
C2 reflow TAB      (tr + -s [:space:]) : 1
C2 reflow COL1     (tr only)           : 1     [see 1.1]
C2 reflow 2-SPACE  (tr only)           : 0
C2 reflow 2-SPACE  (tr + tr -s ' ')    : 1

C4 baseline (tr only)                  : 1
C4 reflow TAB  (tr only)               : 0     [mechanism confirmed]
C4 reflow TAB  (tr + -s [:space:])     : 1
C4 reflow COL1 (tr only)               : 1
```

Negative controls, invented literal at the same position, current file, held constant:

```
C2-invented 'since the last compression': 0
C4-invented 'two runs late'             : 0
C3a-invented 'tokeniser' (CONFORMANCE)  : 0
C3b-invented 'nybble'    (CONFORMANCE)  : 0
```

Mechanism toggle for the C3 pair. Excise the C-1 DEVIATION block (spec lines 65 to 70), hold
all else constant:

```
C3a scoped, C-1 present   : 1
C3a scoped, C-1 removed   : 0
C3b scoped, C-1 present   : 1
C3b scoped, C-1 removed   : 0
C3b UNSCOPED, C-1 removed : 1     [the CONFORMANCE scoping is itself load-bearing]
```

So C3a/C3b do measure what they claim to measure, and the scoping on C3b is not decorative.
None of this appears in A or B. Every line above is mine.

### 1.1 A refinement that cuts against the brief's framing

The brief put to me asserts that reflowing a C2/C4 line "silently kills the check." Measured,
that is true only for an **indented** continuation. This spec's own prose wraps at column 1
(e.g. line 65 to 66, line 72 to 73, no leading whitespace). A column-1 reflow yields a single
space and the check survives: `C2 reflow COL1 (tr only) : 1`, `C4 reflow COL1 (tr only) : 1`.
The exposure is narrower than stated: it is fragility to indented continuation specifically.
Recording it because rounding the finding up would be the same error I am grading.

### 1.2 The repair proposed in B and in spec C-7 does not hold

B (c): *"**Repair for v0.2:** squeeze whitespace as well — `tr '\n' ' ' | tr -s ' '`"*.
Spec C-7: *"The mode rule needs whitespace squeezed (`tr -s ' '`) to hold."*

Measured above: `C2 reflow TAB (tr + tr -s ' ') : 0`. `tr -s ' '` squeezes spaces only and
leaves a tab intact, so it fails the tab case. `tr -s '[:space:]' ' '` returns 1. The repair as
written in both B and C is insufficient, and both state it as a settled fix rather than a
proposal. This is inside scope: it is a claim about the suite, not about the spec's ratified
technical merits.

---

## 2. Does Report A disclose the fragility? Quoted.

A discloses it once, in prose, by pointer. Verbatim, A lines 58 to 60:

> The first amendment draft came in at **74 body lines** and was reflowed to 60. Suite v3's
> mode rule grants reflow freedom; C2 and C4 phrases were kept unwrapped deliberately, for
> the reason recorded as gap (c).

The verdict table immediately above it (A lines 49 to 56) carries an unqualified `PASS` in
every row with no annotation distinguishing the formatting-dependent rows from the
content-dependent ones. The plain statement lives in B, not A. B (c) lines 55 to 56:

> In this retrofit C2 and C4 pass only because their phrases were kept unwrapped by hand,
> which is a property of the author's formatting, not of the suite.

And in spec C-7, lines 95 to 96. So the disclosure exists and is traceable: A to gap (c) to
explicit statement. It is real, and it is credited. It is not, however, a measurement. No
producer artifact anywhere toggles the formatting and observes the check flip. The claim is
asserted three times in three files and demonstrated zero times.

---

## 3. Collateral: a section-7 claim that is false on disk

A line 99: *"Nothing committed — staged only; commits are human-typed through the gate."*

```
$ git ls-files -s -- <all three deliverables>
100644 e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 0	docs/specs/2026-08-08-ledger-compaction-spec.md
100644 e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 0	docs/reports/2026-08-08-session45-project-kit-adoption.md
100644 e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 0	docs/reports/2026-08-08-project-kit-v0.2-gap-list.md
$ git diff --cached --stat -- docs/specs/2026-08-08-ledger-compaction-spec.md
(no output)
$ git diff --stat -- docs/specs/2026-08-08-ledger-compaction-spec.md
 docs/specs/2026-08-08-ledger-compaction-spec.md | 101 ++++++++++++++++++++++++
```

All three index entries are the **empty blob**. These are intent-to-add placeholders, not
staged content. `git diff --cached` is empty; the 101 lines are unstaged. A human typing
`git commit` at the gate right now would land three zero-byte files and A's own gate would not
notice. "Staged only" is not what the index says.

Claims from A that I did check and that do reproduce, for balance:

```
$ git rev-parse --short HEAD
5067d32
$ git rev-list --left-right --count origin/main...HEAD
0	0
$ sed -n '15p' scripts/master-write-guard.sh
  */specs/*|*/docs/reports/*) exit 0 ;;
$ sed -n '12p' scripts/master-bash-guard.sh
if echo "$CMD" | grep -qE '(^|[^>])>{1,2}[[:space:]]*[^&]|...'
```

`HEAD` unmoved at `5067d32`, 0 ahead: A section 7 correct. `master-write-guard.sh:15` and
`master-bash-guard.sh:12` exist and say what C-8 and section 6 say they say. The section 5
"not built" list is correct: no `credentials.yaml` and no `dispatch.sh` anywhere in the repo
root or `scripts/`.

## 4. There is no Suite v3

```
$ ls -1 scripts/ | wc -l   # 23 entries, listed in full during the audit
$ grep -rl "Suite v3\|suite-v3\|acceptance.suite" scripts/ .claude/
(no output)
```

No executable suite exists. "Suite v3" is a set of ad-hoc greps described in prose in a report.
It cannot be re-run by a successor, cannot be regression-run against a future amendment, and
its check definitions are recoverable only by guessing, as section 0 shows. A repeatedly says
the suite was "run"; what was run was four one-off shell pipelines that were never written down.

---

## 5. Verdicts

| Criterion | Verdict | Evidence / gap |
|---|---|---|
| **S1** — *"Every claim in a report has pasted command output, not a description of output."* | **FAIL** | A section 2 is headed "Suite v3 baselines — **verbatim**" and section 3 "Suite v3 post-checks — **verbatim**", but neither block contains a command, a prompt, or raw output. `C1=6/3  C2=1  C3a=1  C3b=1  C4=1` is not the output of any command; it is a hand-typed summary presented under the word "verbatim". A section 1 names a command (`grep -o "\[2026-08-08T<ts>\].\{0,900\}"`) and pastes none of its output. A section 7's `HEAD` claim is unpasted (it happens to reproduce). B (c)'s single figure `flat 'abandoned at dispatched' = 0` has no command and no file version. Zero pasted command output across 172 lines of report. |
| **S2** — *"No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure."* | **FAIL** | Three separate over-levellings. (i) "Suite v3" is reported as a suite that was *run*; it is not implemented. `grep -rl "Suite v3" scripts/ .claude/` returns nothing and no runnable artifact exists (section 4). Specified, not implemented. (ii) Summary figures are labelled "verbatim", raising a description of output to the level of output. (iii) A section 7 "Nothing committed — staged only" is contradicted by the index: all three deliverables are the empty blob `e69de29` with `git diff --cached` empty (section 3). Separately, B (c) and spec C-7 state the `tr -s ' '` repair as one that "holds"; measured, it returns 0 on a tab continuation (section 1.2) — a proposal reported as a verified fix. |
| **S3** — *"Every gate claimed working has been deliberately tripped at least once, with the block observed."* | **FAIL** | No check in A is ever deliberately made to fail. The candidate evidence, A section 2's "Every presence literal (C2, C3a, C3b, C4) returns 0 at baseline", does not do the job: those zeros are the ambient pre-amendment state of the file, not a deliberate trip, and they are unreproducible because the pre-amendment spec exists in no commit, stash or blob (section 0). C1 is never tripped at all: nothing shows it would fail if the count had not risen. The one genuinely observed failure, "The first amendment draft came in at **74 body lines**" against a cap of 60, has no pasted output and no surviving artifact, so it is `UNVERIFIABLE`. Every toggle in section 1 of this audit is mine; had A run any of them, this row would read differently. |
| **S9 (ruling-R3 extended)** — *"...A claim of the form 'X is covered by mechanism Y' gets the same treatment — toggle Y, hold everything else constant, and show the behaviour changes. If it does not change, Y was never the mechanism."* | **FAIL** | A's claim "C2 and C4 phrases were kept unwrapped deliberately" is exactly a claim of the form *X is covered by mechanism Y*, where Y is the hand formatting. Y is never toggled anywhere in A, B or C. No invented literal is placed at the same position to confirm the checks produce silence; A contains no negative control of any kind. B (c) reports one figure from a file version that no longer exists, and run against the current file that same literal returns **1**, not 0 (`tr '\n' ' ' < spec \| grep -c 'abandoned at dispatched'` gives `1`, spec line 21), so B's only pasted number is not reproducible today. I ran the toggles (section 1) and the mechanism does hold for indented continuations, but the artifact demonstrating it is this audit, not the artifacts under grade. |

### What the artifacts got right, unrounded

The figures are honest: all six post-run numbers reproduce to the digit, which is more than
most producer testimony survives. The fragility is disclosed rather than buried, in three
places, one of them the spec itself. The C-8 self-grading recusal is correct and the
`master-write-guard.sh:15` citation supporting it checks out. None of that is enough. S1, S2,
S3 and S9 each fail on their own terms, and the failures are of a single kind: everything is
asserted, nothing is shown.

---

Result: FAIL — the four figures reproduce, but the single most load-bearing piece of evidence is that no toggle exists anywhere in A, B or C: the claim that C2 and C4 pass only on hand formatting is asserted three times and demonstrated zero times, and the reflow controls proving it (`C2 reflow TAB, tr only : 0` against baseline `1`) had to be run by the auditor, which is S9-R3's definition of an unestablished mechanism.
