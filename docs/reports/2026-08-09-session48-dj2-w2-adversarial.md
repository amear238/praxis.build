# W2 — ADVERSARIAL review: K7 insertion into the ledger-compaction spec

## Task
Attempt to FAIL `/Volumes/Sensidine/Praxis.build/docs/specs/2026-08-08-ledger-compaction-spec.md`
(worktree/staged version) against its unmodified predecessor at git HEAD (`c41a969`), the ten binding
constraints, the protected-paragraph hash, and the seven acceptance checks. Hunting specifically for a
repeat of the prior HALT defect: paying for a line with a whitespace-only deletion.

## Mode
ADVERSARIAL. Read-only on the repo. All experiments on copies in the scratchpad. Nothing in the repo was
edited, staged, unstaged, checked out, reset, stashed, or committed by me.

## Criterion
The change must (a) insert K7 after K6 tagged `[PROPOSED]`, (b) keep body ≤60 lines paying for it out of §1/§2
PROSE, (c) add C-9 after C-8 — under constraints 1–10 as briefed, with the protected §3 acceptance paragraph
byte-identical and all seven acceptance checks holding.

---

## Process log / Verification evidence

Scratch copies:
```
$ git show HEAD:docs/specs/2026-08-08-ledger-compaction-spec.md > $S/head.md
$ cp docs/specs/2026-08-08-ledger-compaction-spec.md $S/cur.md
$ wc -l  head.md=101   cur.md=111
```

### A. Deleted lines — the cap-gaming hunt

Every deleted line in the whole file, enumerated:

```
=== ALL DELETED LINES (with -) ===
     1	-- **Retain** OPEN, BLOCKED, DEFERRED and IN-PROGRESS as open items. DEFERRED is open; it does not vanish. **DISPATCHED**
     2	-  is handled per §2.3.
=== count deleted ===
       2
=== deleted lines that are WHITESPACE-ONLY (incl empty) ===
0
```

Second, independent method — total blank-line census of the two files (if compression had eaten a blank
anywhere, the total would have fallen):

```
=== BLANK-LINE TOTALS (second method) ===
head blank(empty-or-ws-only): 21
cur  blank(empty-or-ws-only): 22
head strictly-empty: 21
cur  strictly-empty: 22
```

Blanks went **up** by one (the separator before the C-9 block), not down. Both methods agree: **zero
whitespace-only deletions.**

Both zero-results proven LIVE on a mutated copy (`head.md` with its first blank, line 2, removed):

```
=== find a real blank line number in head.md ===
2:
6:
8:
using blank line 2
-- files differ? --
Files .../head.md and .../mut_blankdel.md differ
-- METHOD1 (ws-only deletions) on mutant, expect >0 --
1
-- METHOD2 blank totals on mutant, expect 21 vs 20 --
head: 21
mut : 20
```

Both detectors fire on a planted blank deletion and stay silent on the artifact.

The specific blank the prior attempt killed — between the §3 heading and its table header — is present:

```
=== §3 heading + following lines (cur) ===
46:## 3. Constraints and acceptance
46[## 3. Constraints and acceptance]
47[]
48[| # | Constraint | Tag |]
49[|---|---|---|]
=== same in head ===
47[## 3. Constraints and acceptance]
48[]
49[| # | Constraint | Tag |]
50[|---|---|---|]
```

Identical structure, one line earlier because of the §2 join. Line 47 (cur) is the blank.

### The seven acceptance checks — PRE (HEAD) vs POST (worktree)

```
FILE=.../head.md
  conf_line=61
  body      = 60
  C1        = 6
  C2        = 1
  C3a       = 1
  C3b       = 1
  neg       = 0
  C4        = 1

FILE=.../cur.md
  conf_line=61
  body      = 60
  C1        = 6
  C2        = 1
  C3a       = 1
  C3b       = 1
  neg       = 0
  C4        = 1
```

All seven hold: body 60 ≤ 60; C1 6 ≥ 6; C2/C3a/C3b/C4 = 1; neg = 0. (C1 is case-sensitive, so the
`**DISPATCHED**` token in the rewritten line never contributed to it either way.)

### Protected paragraph

```
=== PROTECTED PARAGRAPH ===
.../head.md L=58
c1d0c8c4466a5b9a2ff20fe72a0e28bbb8f2a4896d91cdc7f4c41ed09184948d  -
     237
.../cur.md L=58
c1d0c8c4466a5b9a2ff20fe72a0e28bbb8f2a4896d91cdc7f4c41ed09184948d  -
     237
=== control: mutated protected para ===
2a7a703d59efad984a272dc10336ece8389f2178bb580a7e1dcdcb01f3eee40b  -
```

Hash matches the mandated `c1d0c8c4…948d` and byte count 237 in both. The control (one trailing space added)
produces a different hash, so the check is live. Note the paragraph happens to sit at L=58 in *both* files —
located by content, as instructed; the coincidence is because the §2 join (−1) and the K7 insert (+1) cancel
above it.

### B. Did the compression drop a claim, a number, or a normative word?

Exact word-level diff of the only prose change:

```
@@ -27,2 +27 @@
- **Retain** OPEN, BLOCKED, DEFERRED and IN-PROGRESS as open items. DEFERRED[-is open; it-] does not vanish. **DISPATCHED**[-is handled-] per §2.3.
```

Five words disappear, in two clusters: `is open; it` and `is handled`. Taking each pedantically, prosecution
first.

**Cluster 1 — "DEFERRED is open; it does not vanish" → "DEFERRED does not vanish".**
Prosecution: "DEFERRED is open" is a distinct declarative status assignment. DEFERRED-is-open is the
counterintuitive part of the design — a reader skimming for it now finds only the negative form ("does not
vanish"), which is weaker: a row could fail to vanish and still not be *open* (e.g. parked, or archived to a
holding file). On that reading, an assertion was removed and a weaker one left standing. That is a real
argument and I do not dismiss it lightly.
Defence, which I find decisive: the removed clause is not the only carrier of the proposition. The *same
bullet, same sentence group, one clause earlier* reads "**Retain** OPEN, BLOCKED, DEFERRED and IN-PROGRESS
**as open items**". DEFERRED is named in that list and the predicate "as open items" distributes over every
member of it. So "DEFERRED is open" is still asserted, on the same line, by the surviving text; the deleted
clause was a restatement for emphasis. Emphasis is rhetoric, not a claim. The assertion set is unchanged.
Verdict: **not a claim removal.** It is the one legitimate redundancy in §2 and it is what got spent.

**Cluster 2 — "**DISPATCHED** is handled per §2.3" → "**DISPATCHED** per §2.3".**
Prosecution: eliding the verb turns a proposition into a noun phrase; strictly, a fragment asserts nothing.
Defence: the bullet list it sits in is already verb-fronted and elliptical throughout (`- **Retain** …`,
`- **Archive** …`), the cross-reference target (§2.3) is unchanged, and no alternative reading of
"**DISPATCHED** per §2.3" exists other than "DISPATCHED is handled per §2.3". Cost is grammatical polish, not
content. Verdict: **not a claim removal.**

Numbers: the affected line contains no digits in either version, so no figure could have moved. Normative
modals: the line contains no *must/shall/never/always* in either version; `is handled` is descriptive, not
normative. Nothing was **added** to the line either — the diff shows only deletions on it.

Whole-body word-sequence diff confirms these five words are the *only* body text lost anywhere in the file:

```
=== BODY word-sequence diff (relocation detector) ===
294,296d293
< is
< open;
< it
301,302d297
< is
< handled
628a624,642
> |
> [PROPOSED]
> |
> |
> K7
> ...
body-word-diff-exit=1
-- body word counts --
     671
     685
```

The only body additions are the K7 row's tokens. Nothing else in §1 or §2 was touched.

The compression was taken from §2.2, i.e. §2 prose — §3 was not raided:

```
=== which section is the compressed line in? (head) ===
15: ## 2. Design
17: ### 2.1 STATE.md — the sole spawn-read
23: ### 2.2 compact.sh — deterministic, zero agent tokens
```

And §3 received the K7 row and nothing else:

```
=== §3 region diff: head 47..60 vs cur 46..60 (expect only K7 added) ===
10a11
> | K7 | compact.sh stages only; it never invokes `git commit` and never writes into `.git/` | [PROPOSED] |
```

### C. K7 row byte-for-byte

Mandated text written to `k7_expected.txt`; actual extracted with `grep -n '^| K7 ' | cut -d: -f2-`.

```
=== diff expected vs actual (empty = identical) ===
IDENTICAL
=== sha256 both ===
a46064b5054eb3db27ae3723d1552c6a66ce3d5c57ea88a2078a4f1ad0170d8b  .../k7_expected.txt
a46064b5054eb3db27ae3723d1552c6a66ce3d5c57ea88a2078a4f1ad0170d8b  .../k7_actual.txt
=== cmp ===
cmp: same bytes
=== control: mutate one byte ===
.../k7_expected.txt .../k7_mut.txt differ: char 26, line 1
control fired
```

Byte-identical, including the deliberately self-contradictory wording (constraint 4: not reworded). Position
verified — K7 sits directly after K6, no rows reordered:

```
50:| K1 | STATE.md ceiling 14,000, byte-only enforcement | [PROPOSED] |
51:| K2 | Marker path `.claude/state/last-compaction` | [PROPOSED] |
52:| K3 | Boundary is the last compaction, not session start | [BINDING — DECISION_LOG 2026-08-08T01:20:00Z] |
53:| K4 | First run with no marker retains every dispatched row | [PROPOSED] |
54:| K5 | Unknown state is a hard error, biased to retention | [PROPOSED] |
55:| K6 | Environment subtraction stays DEFERRED (D-7) | [PROPOSED] |
56:| K7 | compact.sh stages only; it never invokes `git commit` and never writes into `.git/` | [PROPOSED] |
```

### D. C-9 — both residuals, and are its facts TRUE?

C-9 as filed:

```
**C-9 — CONTRADICTION, carried not resolved. K7 [PROPOSED]: compact.sh stages only; it never invokes `git commit` and
never writes into `.git/`.** As filed, the row forbids what it mandates: staging *is* a write into `.git/`. Measured in
a throwaway repo this session — before `git add` there was no `.git/index` and `.git/objects/` held 0 files; after
`git add a.txt` the index existed and `.git/objects/ce/013625030ba8dba906f756967f9e9ca394464a` had appeared. The
wording stands as filed by ruling and is not reworded here; the intended reading is *no commit, and no writes to
`.git/` beyond those `git add` itself performs*. Second residual: staging-only collides with the commit gate.
`.claude/hooks/gate-commit.sh:167-176` binds the audit token to the exact staged tree — it compares `git write-tree`
against the `tree=` recorded at mint and denies on any mismatch — so a compact.sh run between mint and commit denies
that commit. Both residuals are recorded so they are visible at the ratification gate; neither is resolved here.
```

Residual (i) present ("staging *is* a write into `.git/`"). Residual (ii) present ("collides with the commit
gate"). Constraint 7 satisfied.

**(i) verified independently in my own throwaway repo** (scratchpad, isolated config):

```
=== BEFORE git add ===
-- .git/index exists? --
NO (absent)
-- files under .git/objects: --
0

=== AFTER git add a.txt ===
-- .git/index exists? --
YES
-- files under .git/objects: --
1
.git/objects/ce/013625030ba8dba906f756967f9e9ca394464a
```

`git add` does write into `.git/` — index created, one loose object created. I reproduced the *exact* object
hash C-9 cites, `ce013625030ba8dba906f756967f9e9ca394464a`, with `a.txt` containing `hello\n`. C-9's
measurement is reproducible and true. (Minor: C-9 does not state a.txt's contents, so the hash is only
reproducible by guessing `hello\n`. Non-blocking; the claim it supports is true regardless.)

**(ii) verified by reading the cited range.** `.claude/hooks/gate-commit.sh:167-176`, unedited:

```
167	  # staged-TREE binding: the index must still produce the exact tree the token
168	  # was minted against — extra/missing/changed paths in the mint→commit gap deny.
169	  MINT_TREE=$(sed -n 's/^tree=//p' "$TOKEN" | head -1)
170	  NOW_TREE=$(cd "$ROOT" && git write-tree 2>/dev/null)
171	  if [ -z "$MINT_TREE" ] || [ -z "$NOW_TREE" ] || [ "$MINT_TREE" != "$NOW_TREE" ]; then
172	    rm -f "$TOKEN"
173	    echo "Commit denied: staged tree no longer matches the tree the audit token was minted against (minted tree=${MINT_TREE:-missing/legacy-token}, current tree=${NOW_TREE:-unresolvable}). Something changed the index after mint — re-stage exactly the audited set and re-dispatch the orchestrator-auditor." >&2
174	    exit 2
175	  fi
176	  rm -f "$TOKEN"   # single-use: consumed at allow time, before the commit runs
```

The cited range contains exactly what C-9 says it contains: line 169 reads `tree=` from the token, line 170
runs `git write-tree`, lines 171–174 deny on mismatch. The range boundaries are well chosen (167 is the first
line of the binding block, 176 the token-consumption line). The subsidiary claim "the `tree=` recorded at
mint" is also true — the mint side writes it:

```
.claude/hooks/audit-approve.sh:26:printf 'tree=%s\n' "$TREE" > "$STATE/audit-pass-$HASH"
```

**No citation defect.** This is the one place I most expected to find a fabricated or off-by-N line range,
and it is accurate.

### E. C-9 against constraint 8

```
=== E1: any '26' in C-9? ===
0
=== E1b: any digits in C-9? ===
0 013625030 167 176 394464 7 756967 8 9 906
=== E2: 'git add' occurrences in C-9 ===
git add
git add a.txt
git add
=== E3: 'archive' in C-9? ===
0
=== control: does the 26-grep fire on a mutant? ===
1
```

No `26`. The digits present are the object hash, the line range 167–176, and the entry labels C-8/C-9/K7 —
no re-assertion of the stale untracked-report figure. The three `git add` mentions are all about the
throwaway-repo measurement and the intended reading of K7; **none** claims compact.sh runs `git add` on the
archive files. Zero occurrences of "archive" in C-9 at all. The `26` check fires on a planted mutant, so it
is live. Constraint 8 satisfied.

### F. Nothing else changed

Headings — text identical, only line numbers shift by one below the join:

```
=== headings identical? ===
6,8c6,8
< 32:### 2.3 DISPATCHED — the boundary is since the last compaction
< 39:### 2.4 Report archive and dispatch template
< 47:## 3. Constraints and acceptance
---
> 31:### 2.3 DISPATCHED — the boundary is since the last compaction
> 38:### 2.4 Report archive and dispatch template
> 46:## 3. Constraints and acceptance
```

Stale §2.4 figures left stale, as required (constraint 3):

```
=== stale figures present in BOTH? ===
11:101 files in `docs/reports/`. …
40:All 101 files in `docs/reports/` move to `docs/reports/archive/` …
42:`MANIFEST.md`. The 26 untracked reports are `git add`-ed in the archive commit — they exist on this disk only.
---cur---
11:101 files in `docs/reports/`. …
39:All 101 files in `docs/reports/` move to `docs/reports/archive/` …
41:`MANIFEST.md`. The 26 untracked reports are `git add`-ed in the archive commit — they exist on this disk only.
```

C-7 untouched, stale `tr -s ' '` intact (constraint 9):

```
=== C-7 unchanged? ===
C-7 IDENTICAL
5:(`tr -s ' '`) to hold. C2 and C4 escape this only because their phrases were deliberately kept unwrapped, which is a
```

Tag census — no flips; the only delta is +2 `[PROPOSED]`, one from the K7 row and one from C-9's quotation
of it. The single `[BINDING …]` tag on K3 is intact:

```
=== full tag census incl BINDING ===
   1 [BINDING — DECISION_LOG 2026-08-08T01:20:00Z]
   6 [PROPOSED]
---cur---
   1 [BINDING — DECISION_LOG 2026-08-08T01:20:00Z]
   8 [PROPOSED]
```

CONFORMANCE entries in order, C-9 appended after C-8:

```
**C-1 **C-2 **C-3 **C-4 **C-5 **C-6 **C-7 **C-8
**C-1 **C-2 **C-3 **C-4 **C-5 **C-6 **C-7 **C-8 **C-9
```

### G. Staging / commit state

```
=== HEAD ===
c41a969296743ceeafc261280afeb98d87577733 c41a969 Commit session-46 audit grade: resolve dangling citation from 28b3922
=== is HEAD c41a969? ===
c41a969
=== spec staged, worktree clean vs index? ===
M  docs/specs/2026-08-08-ledger-compaction-spec.md
0            <- `git diff` (unstaged) line count for the spec
=== files whose staged content differs from HEAD (full staged set) ===
 DECISION_LOG.md                                    |  118 ++
 ISSUE_REGISTER.md                                  |   35 +
 MANIFEST.md                                        |   15 +
 .../2026-08-06-session42-r8j-phase3-import.md      | 1882 ++++++++++++++++++++
 .../2026-08-07-f4-mffu-compliance-evidence.md      |  537 ++++++
 ...-session44-r8j-offset-correction-adversarial.md |  546 ++++++
 ...8-07-session44-r8j-offset-correction-worker1.md |  195 ++
 .../2026-08-07-session44-r8j-offset-correction.md  |  301 ++++
 docs/specs/2026-08-08-ledger-compaction-spec.md    |   14 +-
 9 files changed, 3641 insertions(+), 2 deletions(-)
```

HEAD is unchanged at `c41a969`. The spec is staged with no unstaged remainder (`M ` + empty `git diff`), i.e.
staged-not-committed as required. The other eight staged paths were **already staged before this unit began**
— they all appear in the pre-existing session `git status` snapshot; the spec did not. So this change added
exactly one path to the index.

`git diff --cached --check` on the spec is clean (exit 0), so no whitespace errors were introduced.

### H. Other cap-gaming vectors

- **Trailing-whitespace stripping**: ruled out. `grep -c '[[:space:]]$'` = **0** on head, **0** on cur. There
  was none to strip, so it cannot have been the currency.
- **Body line relocated into CONFORMANCE**: ruled out two ways. First, the CONFORMANCE word-sequence diff has
  **no removals and only C-9 additions** (`diff … | grep '^<'` exit 1 = nothing removed). Second, a direct
  content probe for the deleted clause inside CONFORMANCE:
  ```
  === CONTROL for relocation grep (append the phrase, expect 1) ===
  1
  === live (expect 0) ===
  0
  ```
  The control fires, the live check is silent. The removed text was not smuggled below the CONFORMANCE line.
- **Line joined that shouldn't be**: the join is a wrapped continuation of a single bullet (`  is handled per
  §2.3.` was a soft-wrap of the preceding line, not an independent statement). Joining a soft wrap is
  compression, not deletion — and it was only possible because five redundant words were also cut.
- **Content deleted rather than compressed**: addressed at length in §B. Five words, all redundant, from one
  §2.2 bullet.
- **EOF newline**: unchanged (`0a` on both), so no byte was won there.
- **Arithmetic sanity**: 101 − 1 (join) + 1 (K7) + 10 (C-9 block incl. its separator blank) = 111 = observed
  `wc -l`. Every line of the delta is accounted for; nothing unexplained.

---

## Observations (reported, not fixed — outside the pass/fail criteria)

1. **C-9 slightly over-generalises the deny.** It says "a compact.sh run between mint and commit denies that
   commit." Per line 171 the deny is triggered by a *tree* mismatch, not by a run per se; a compact.sh
   invocation that staged nothing new would leave `git write-tree` unchanged and would not deny. Given K7
   defines compact.sh as a thing that stages, the practical claim holds. Non-blocking; flagging because the
   sentence is stronger than the code strictly supports.
2. **A latent contradiction C-9 does not name.** Body line 41 says "The 26 untracked reports are `git
   add`-ed in the archive **commit**", while K7 says compact.sh "never invokes `git commit`". C-9 documents
   the staging-vs-`.git/` contradiction and the gate collision, which is what constraint 7 asked for; it does
   not address this third one. Not a defect against the brief (constraint 3 forbids touching that stale
   line), recorded so the ratification gate sees it.
3. **A second repo file exists from this unit.** `docs/reports/2026-08-09-session48-dj2-k7-insert.md`
   (mtime `2026-08-09 10:59:07`, 468 lines) is untracked and unstaged; the spec's mtime is `11:14:13`. It is
   the builder's own report and its header asserts "Target (only file modified)". It does not affect the
   staged set or the artifact. If constraint 10 is read as "only this one file may exist as a change in the
   repo," this is a deviation for the manager to rule on; I did not touch it.

## Files staged
None by me. I made no repo writes of any kind. Repo state is exactly as I found it: `c41a969` at HEAD, spec
staged, no unstaged remainder on the spec.

## Attack summary — what I tried and could not break
Whitespace-only deletion (2 methods + planted-mutant controls); §3 heading/table blank; the protected
paragraph hash and byte count (+ mutant control); all seven acceptance checks PRE vs POST; K7 byte equality
(+ one-byte mutant control) and row ordering; tag flips including the `[BINDING …]` tag; C-7 amendment;
the two stale §2.4 figures; C-9's `.git/` claim reproduced in my own repo down to the object hash; C-9's
`gate-commit.sh:167-176` citation read line-by-line and cross-checked against `audit-approve.sh:26`; C-9 for
"26" and for archive-file `git add` claims (+ mutant control); trailing-whitespace stripping; body→CONFORMANCE
relocation (2 methods + control); EOF newline; and a full line-arithmetic reconciliation. None broke it.

## Result: NO BREAK FOUND

VERDICT: PASS
