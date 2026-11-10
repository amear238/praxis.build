# `Praxis_build-r8j` — §F2.1 byte-offset correction (session 44)

Manager: `praxis-manager`. Date: 2026-08-07. Worker cap: 2 (both used).
Authorisation: DECISION_LOG row `2026-08-07T18:57:33Z`, WHO: amear — human park resumption
at narrow scope. Read before work began; quoted in "Process log" below.

---

## Task

Correct the §F2.1 byte-offset locator table in
`docs/reports/2026-08-06-session42-r8j-phase3-import.md` (lines 828-834), **by append**,
per the `wx7` rule. Nothing else.

The file is correctly absent from `main`'s worktree; it lives at `f258a5d` on branch
`parked/Praxis_build-r8j` and was restored from there.

---

## What I verified myself vs. what I took from the brief

**Verified by me, in this session, from source:**

- That the defect exists and is exactly as characterised. I did NOT take this from the brief.
  I rebuilt the clause from the committed blob `f258a5d:docs/specs/2026-08-06-phase3-build-specification.md`
  and hexdumped it (output pasted below). The brief's claim held.
- The true offsets of all three characters in the table.
- That `0x25`–`0x27` holds `4d 20 45` (`M E`), not the arrow.
- That the resulting clause reproduces sha256 `906fd1ee…c37100`, matching §F2.2.
- That the worktree file is a **pure insertion** over the `f258a5d` blob at byte level.
- That lines 828-834 are byte-identical to the blob, with a firing negative control.
- The full staged set, and that `.claude/agent-memory/` was not touched.

**Taken from the brief, not independently re-derived:**

- That `f258a5d` is the tip of `parked/Praxis_build-r8j` — I verified the commit exists and
  contains the file, and that the checkout `parked/Praxis_build-r8j -- <path>` succeeded, which
  requires the branch to exist. I did not verify tip-ness. Not load-bearing for this repair.
  **UNVERIFIED.**
- That `scripts/no-commit-guard.sh` false-positives on `git merge-base`. Not exercised; I had
  no need for an ancestry query. **UNVERIFIED — carried forward from the brief only.**
- That audit items 2-8 were graded PASS. Out of scope by instruction; not re-checked.

---

## Rubric criteria addressed

Quoted verbatim from `specs/SPEC_RUBRIC.md` (lines 107-114).

| ID | Criterion | Disposition |
|---|---|---|
| S1 | "Every claim in a report has pasted command output, not a description of output." | PASS — every offset figure in the appended correction traces to a raw fence; adversarial worker de-blockquoted the fence, re-ran it under its declared wrapper, and got `cmp: IDENTICAL`. The `wc -c` line retains its six leading spaces and filename. |
| S2 | "No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure." | PASS — the correction carries an explicit scope note refusing to endorse untested §F2 figures. |
| S4 | "Every deviation from the plan has a DECISIONS.md entry with a traceable authorisation chain, written before the work, not after." | PASS — no deviation taken. The authorising row predates dispatch. |
| S5 | "No approval is inferred from a verbal or in-session exchange. The ledger append is the authorisation." | PASS — authority is the ledger row `2026-08-07T18:57:33Z`, not the brief text. I read the row at source before planning. |
| S7 | "Nothing is committed while any audit box is unchecked." | PASS by construction — nothing committed, no commit attempted. See caveat under "Negative tests". |

---

## Workers dispatched

| # | id | mode | outcome |
|---|---|---|---|
| 1 | `a8f43813203cc937e` | BUILD | PASS — defect confirmed independently, correction appended |
| 2 | `ad3fd84f85a0c3bc1` | ADVERSARIAL | `VERDICT: PASS` — could not break it on any of five attack lines |

Worker 2 was given the artifact and the criteria only. It was **not** given worker 1's
reasoning, report, or conclusion.

Both briefs named `.claude/agent-memory/` as off-limits without exception (standing hazard:
workers have written there twice in this project). Verified clean afterwards.

---

## Process log

1. Read DECISION_LOG rows `2026-08-07T18:57:33Z` (authorisation) and `2026-08-07T14:13:27Z`
   (the FAIL-2 park, which defines what is out of scope) at source before planning.
2. Read `specs/SPEC_RUBRIC.md:107-118` and quoted the criteria verbatim.
3. Restored the file from `f258a5d`.
4. **Verified the brief's defect claim myself before dispatching anyone.** This was deliberate:
   the brief explicitly warned that a prior dispatch in this project was briefed from a ledger
   row *about* a file rather than from the file. Had my derivation disagreed with the brief, the
   instruction was to stop and report the divergence. It agreed.
5. Identified the project's existing inline correction convention by grepping `docs/reports/`
   for `CORRECTION` — a markdown blockquote `> **CORRECTION <date> — ...**` placed immediately
   after the passage, original byte-unchanged. Handed the convention to worker 1 with in-file
   examples rather than letting it invent a shape.
6. Dispatched worker 1 (BUILD) with instructions to derive the offsets itself and to **stop and
   report "no defect found" if its derivation matched the table**, rather than correct toward my
   description.
7. On return: read worker 1's report file, re-ran the verification myself, read the staged diff,
   ran independent negative controls.
8. Dispatched worker 2 (ADVERSARIAL) with the artifact and criteria only.
9. Staged worker 2's report, which worker 2 had correctly left unstaged under its read-only
   instruction.

---

## Verification evidence — pasted output only

### V1 — the defect, derived by me from the committed blob (not from the report's own fence)

```
$ git show f258a5d:docs/specs/2026-08-06-phase3-build-specification.md | /usr/bin/sed -n '90p' > line90.txt
$ /usr/bin/python3 -c "
b=open('line90.txt','rb').read().rstrip(b'\n')
i=b.index(b'window')
open('spec_clause.txt','wb').write(b[i:])
"
$ /usr/bin/xxd spec_clause.txt
00000000: 7769 6e64 6f77 20e2 8094 2063 6c6f 636b  window ... clock
00000010: 2065 6e74 6572 7320 333a 3030 e280 9336   enters 3:00...6
00000020: 3a30 3020 504d 2045 5420 e286 9220 6469  :00 PM ET ... di
00000030: 7361 626c 6520 6576 6572 7974 6869 6e67  sable everything

$ /usr/bin/shasum -a 256 spec_clause.txt
906fd1eec371494f3faebfdfb3a3a64860d14b4ce726dcfefe4d43e8adc37100  spec_clause.txt
```

Path shortened for width in the two `python3`/`shasum` lines above: the real invocation used the
absolute scratch path `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/b6929095-bad7-4760-8061-8b2867116cc1/scratchpad/`,
which is what the `shasum` output line actually printed. Stated rather than silently trimmed.

The digest independently reproduces §F2.2's `906fd1ee…c37100`, so the clause I derived is the
same clause §F2 tested.

### V2 — the offsets, computed

```
$ /usr/bin/python3 -c "
b=open('spec_clause.txt','rb').read()
for name,seq in [('em-dash U+2014',b'\xe2\x80\x94'),('en-dash U+2013',b'\xe2\x80\x93'),('arrow U+2192',b'\xe2\x86\x92')]:
    i=b.index(seq); print('%-16s bytes %s  offset 0x%02x-0x%02x' % (name, seq.hex(' '), i, i+len(seq)-1))
print()
print('bytes at 0x25-0x27 (what the table claims for the arrow): %s  = %r' % (b[0x25:0x28].hex(' '), b[0x25:0x28]))
"
em-dash U+2014   bytes e2 80 94  offset 0x07-0x09
en-dash U+2013   bytes e2 80 93  offset 0x1c-0x1e
arrow U+2192     bytes e2 86 92  offset 0x2a-0x2c

bytes at 0x25-0x27 (what the table claims for the arrow): 4d 20 45  = b'M E'
```

Row 3 of the table is wrong by a 5-byte undershoot. Rows 1 and 2 are correct as written.

### V3 — append-only integrity, at byte level (not by line count)

```
$ git diff --cached --numstat -- docs/reports/2026-08-06-session42-r8j-phase3-import.md docs/reports/2026-08-07-session44-r8j-offset-correction-worker1.md
1882	0	docs/reports/2026-08-06-session42-r8j-phase3-import.md
195	0	docs/reports/2026-08-07-session44-r8j-offset-correction-worker1.md
--- append-only check: deleted lines in staged diff for the parked report ---
0
--- byte-identity of lines 828-834 vs f258a5d ---
6f2c21e1ba9e60330ec50356dd824ebd6b3a244d951cbbdf9110395185737a25  -
6f2c21e1ba9e60330ec50356dd824ebd6b3a244d951cbbdf9110395185737a25  -
```

`1882` added on a file staged as `A` is the whole file (1825 original + 57 inserted), which is
expected for a path new to the index; it is not evidence of a rewrite. The byte-level proof is V4.

### V4 — pure-insertion proof and its negative control

```
=== NEGATIVE CONTROL: does the 828-834 byte-identity check actually fire? ===
20d324d2141ef26e92e19d1cd05e01f5dac0359c8be0e3c1d7d10983c3d9c6bf  -
(above = deliberately mutated; must NOT equal 6f2c21e1... shown earlier)

=== whole-file pure-insertion proof (independent of worker 2) ===
common prefix bytes = 44799
common suffix bytes = 45834
p+s = 90633  len(old) = 90633  PURE INSERTION = True
bytes inserted = 3375
reconstructs old exactly = True
```

The mutation was a single `0x25` → `0xXX` substitution inside the preserved table, applied to a
pipe, not to disk. The check produced a different digest, so the identity check in V3 is capable
of failing and its agreement is meaningful. `reconstructs old exactly = True` proves the file is
a superset of the `f258a5d` blob: no deletion, no modification, no equal-length swap.

### V5 — staged set and hazard sweep

```
=== full staged set ===
M	DECISION_LOG.md
M	ISSUE_REGISTER.md
M	MANIFEST.md
A	docs/reports/2026-08-06-session42-r8j-phase3-import.md
A	docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
A	docs/reports/2026-08-07-session44-r8j-offset-correction-adversarial.md
A	docs/reports/2026-08-07-session44-r8j-offset-correction-worker1.md

=== agent-memory touched at all? (known hazard) ===
porcelain-rc=0 (empty above = untouched)

=== any staged change to protected paths? ===
MANIFEST.md
(empty = none)
```

---

## Adversarial findings

Worker 2 attacked five lines and returned `VERDICT: PASS`. Substantive findings:

- **Arithmetic re-derived by three independent methods** (per-character UTF-8 walk, `od` byte
  stream, `bytes.index`) from the `f258a5d` blob, not from any fence in the report. Arrow at
  `0x2a`–`0x2c`; `0x25`–`0x27` is `b'M E'`. It checked rows 1 and 2 rather than trusting the
  correction's "correct as written" declaration — they are correct.
- **Negative control fired**: mutating the clause moved the arrow to `0x24` and changed the slice
  to `b'\x86\x92 '`, so the method tracks its input.
- **S1 trap specifically hunted**: it de-blockquoted the appended fence, re-ran it under the
  wrapper the fence declares, and got `cmp: IDENTICAL`. The `wc -c` line retains
  `      85 line90.txt` with six leading spaces and the filename — the exact shape a prior audit
  in this project caught being faked as a bare number.
- **`wx7` proven at byte level**, independently reaching the same `44799 / 45834 / 90633` figures
  I derived separately.

Worker 1 self-disclosed a discarded first attempt: it ran `git` from a non-worktree scratch dir,
the command failed, and it silently read a stale `clause.txt`. It caught this, discarded the run,
re-ran clean, and **kept the bad transcript in its report** rather than hiding it. I regard the
disclosure as correct behaviour; the final figures are the clean run's, and they match mine and
worker 2's independently.

---

## S6 cross-block check

"Every approved deviation is tested against the specs of every other block it touches, not only
its own."

- **§F2.2 / §F2.3 / §F2.4** — the `cmp` rc=0, the twin sha256 `906fd1ee…c37100`, the alternate
  boundary, and the negative control never depended on the locator offsets. I independently
  reproduced `906fd1ee…c37100` from the committed blob (V1), so the §F2 conclusion the table
  annotates is undisturbed. The appended correction says this explicitly and declines to endorse
  anything else in §F2.
- **DECISION_LOG rows `2026-08-07T14:13:27Z` and `2026-08-07T18:57:33Z`** both state the arrow is
  at `0x2a`–`0x2c`. The correction agrees with both. No ledger contradiction is created, and no
  ledger edit is needed or permitted.
- **Other `CORRECTION 2026-08-07` markers in the same file** (lines 30, 53, 73, 117, 158, 207,
  452, 471, 495, 522) are untouched; the new marker follows their established shape, so the file's
  "everything above is preserved unedited" claim at line 558 remains true.
- **`main` vs `parked/Praxis_build-r8j`** — the file's absence from `main` is correct per the
  authorising row. Restoring it into `main`'s index is what the brief directed; I did not merge,
  rebase, or otherwise move the parked branch.

---

## Findings reported, NOT fixed (out of scope)

Per the brief: "If you find a defect outside this scope, report it and do not fix it."

1. **Four unrelated paths were already staged before this unit began** — `DECISION_LOG.md`,
   `ISSUE_REGISTER.md`, `MANIFEST.md`, and `docs/reports/2026-08-07-f4-mffu-compliance-evidence.md`.
   They appear in V5 and were present in the session-start `git status` snapshot. **Neither worker
   touched them**, and I did not unstage them — unstaging is itself a scope widening, and the
   authorising row's own COMPOSITION WARNING says the commit path list is composed deliberately.
   **This matters to whoever commits**: a bare `git commit` here would sweep in eleven days of
   unrelated ledger, which is precisely the failure the session-42 park commit already suffered.
   The r8j repair is exactly three paths: the parked report and the two session-44 worker reports.
2. **`MANIFEST.md` registry rule vs. this brief.** `CLAUDE.md` requires a MANIFEST update when
   files are created; this unit created two report files. The brief puts `MANIFEST.md` explicitly
   out of scope. I honoured the brief and did not touch it. **This is an unresolved conflict for
   the master, not for me to settle.**
3. **UNVERIFIED, carried from the brief:** the `no-commit-guard.sh` / `git merge-base`
   false-positive. Never exercised — no ancestry query was needed.

---

## Negative tests — one performed, one refused

- **Performed:** the byte-identity gate (V4). Deliberately tripped, block observed, digest
  diverged. The `wx7` preservation check is not a comment.
- **Refused, and this is a deliberate non-execution rather than an omission:** I did **not** trip
  `scripts/no-commit-guard.sh` by attempting a commit. My standing instructions call for tripping
  a gate to prove it blocks; this brief states "You cannot commit and **must not try**." The
  explicit instruction wins over the general practice. **S7 is therefore satisfied by
  construction — nothing was committed — and NOT by an observed block. UNVERIFIED that the guard
  would have fired.** Flagged rather than smoothed.

---

## Files staged

| Path | Status | Attribution |
|---|---|---|
| `/Volumes/Sensidine/Praxis.build/docs/reports/2026-08-06-session42-r8j-phase3-import.md` | `A` | this unit — restored from `f258a5d` + 3375 bytes appended |
| `/Volumes/Sensidine/Praxis.build/docs/reports/2026-08-07-session44-r8j-offset-correction-worker1.md` | `A` | this unit — worker 1 BUILD report |
| `/Volumes/Sensidine/Praxis.build/docs/reports/2026-08-07-session44-r8j-offset-correction-adversarial.md` | `A` | this unit — worker 2 ADVERSARIAL report |
| `DECISION_LOG.md`, `ISSUE_REGISTER.md`, `MANIFEST.md`, `docs/reports/2026-08-07-f4-mffu-compliance-evidence.md` | `M`/`A` | **PRE-EXISTING — not this unit. See finding 1.** |

This report is itself unstaged at time of writing; the master may stage it as a fourth r8j path.

Nothing committed. No commit attempted.

---

## Result: PASS

Appended 2026-11-10 under D9 (S13): Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
