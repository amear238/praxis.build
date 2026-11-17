# W1 — ledger compaction spec: compression + K7 + C-9

## Task
Three edits, and only three, to `/Volumes/Sensidine/Praxis.build/docs/specs/2026-08-08-ledger-compaction-spec.md`:
(1) compress the §2.2 **Retain** bullet from two lines to one; (2) insert the K7 row after K6 in the §3 table;
(3) append conformance item C-9 after C-8. No other repo file touched. Nothing committed.

## Mode
BUILD

## Criterion
Body (everything above `## CONFORMANCE`) stays ≤ 60 lines while the K7 constraint row and the C-9 conformance entry
are both added; every existing suite-v3 conformance check still returns its required value; zero blank lines deleted;
the protected acceptance paragraph is byte-identical.

## Process log

1. Read the target file in full (101 lines, `## CONFORMANCE` at line 61, body = 60).
2. Confirmed the exact bytes of lines 27–28 with `od -c` before editing (line 28 carries two leading spaces).
3. **Edit 1** — replaced the two-line Retain bullet with the single dictated line. The dropped clause
   `DEFERRED is open;` is a verbatim restatement of `Retain ... DEFERRED ... as open items` in the same sentence, so
   no claim is lost. Net −1 body line.
4. **Edit 2** — inserted the K7 row verbatim, directly after K6. Net +1 body line. Body returns to exactly 60.
   Per instruction the K7 wording was **not** altered, despite being self-contradictory — that is the point of C-9.
5. **Edit 3** — before writing C-9 I *measured* the claim it makes rather than reasoning about it. Throwaway repo in
   the scratchpad (output pasted below): `git add` does write into `.git/`. The object path in the C-9 text,
   `.git/objects/ce/013625030ba8dba906f756967f9e9ca394464a`, reproduced exactly.
6. Also verified in-session the second C-9 claim, the file:line citation: `grep -n` on
   `.claude/hooks/gate-commit.sh` puts the staged-TREE binding comment at 167, `MINT_TREE=` at 169,
   `NOW_TREE=$(... git write-tree ...)` at 170, the mismatch `if` at 171, the deny `echo` at 173 — the block
   `167-176` cited in C-9 is accurate, and it does compare `git write-tree` against a `tree=` recorded at mint.
7. C-9 wrapped at ≤120 bytes/line to match the file's style; wording unaltered.
8. Ran the full verification block. All checks pass. Staged with the exact pathspec-scoped command.

Nothing under `.claude/` was written, created, or modified. No new file was created inside the repo.
No script, ledger, or other spec was touched. No number anywhere in the file was changed.

## Verification evidence (unedited stdout)

### Pre-edit byte inspection of lines 25–30 (excerpt showing the two target lines)

```
0000240    i   t   t   e   n   .  \n   -       *   *   R   e   t   a   i
0000260    n   *   *       O   P   E   N   ,       B   L   O   C   K   E
0000300    D   ,       D   E   F   E   R   R   E   D       a   n   d
0000320    I   N   -   P   R   O   G   R   E   S   S       a   s       o
0000340    p   e   n       i   t   e   m   s   .       D   E   F   E   R
0000360    R   E   D       i   s       o   p   e   n   ;       i   t
0000400    d   o   e   s       n   o   t       v   a   n   i   s   h   .
0000420        *   *   D   I   S   P   A   T   C   H   E   D   *   *  \n
0000440            i   s       h   a   n   d   l   e   d       p   e   r
0000460        §  **   2   .   3   .  \n   -       *   *   U   n   k   n
```

### Measurement backing C-9 (throwaway repo, this session)

```
$ SP=.../scratchpad; rm -rf "$SP/tw"; mkdir -p "$SP/tw"; cd "$SP/tw" && git init -q . && printf 'hello\n' > a.txt \
  && echo "BEFORE: index exists? ..." && ... && git add a.txt && ...
BEFORE: index exists? NO
BEFORE: objects file count = 0
AFTER: index exists? YES
AFTER: objects files:
.git/objects/ce/013625030ba8dba906f756967f9e9ca394464a
```

### Citation check backing C-9's second residual

```
$ grep -n 'staged-TREE\|MINT_TREE\|NOW_TREE\|write-tree' /Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh
9:#   1. staged-TREE binding — token carries `tree=<git write-tree>` from mint time;
167:  # staged-TREE binding: the index must still produce the exact tree the token
169:  MINT_TREE=$(sed -n 's/^tree=//p' "$TOKEN" | head -1)
170:  NOW_TREE=$(cd "$ROOT" && git write-tree 2>/dev/null)
171:  if [ -z "$MINT_TREE" ] || [ -z "$NOW_TREE" ] || [ "$MINT_TREE" != "$NOW_TREE" ]; then
173:    echo "Commit denied: staged tree no longer matches the tree the audit token was minted against (minted tree=${MINT_TREE:-missing/legacy-token}, current tree=${NOW_TREE:-unresolvable}). Something changed the index after mint — re-stage exactly the audited set and re-dispatch the orchestrator-auditor." >&2
```

### The seven prescribed checks

```
$ cd /Volumes/Sensidine/Praxis.build
$ SPEC=docs/specs/2026-08-08-ledger-compaction-spec.md
$ CONF=$(grep -n '^## CONFORMANCE' "$SPEC" | cut -d: -f1)
$ echo "body: $((CONF-1))"
body: 60
$ grep -o 'dispatched' "$SPEC" | wc -l
       6
$ tr '\n' ' ' < "$SPEC" | tr -s '[:space:]' ' ' | grep -c 'since the last compaction'
1
$ sed -n "${CONF},\$p" "$SPEC" | grep -c 'tokenizer'
1
$ sed -n "${CONF},\$p" "$SPEC" | tr '\n' ' ' | tr -s '[:space:]' ' ' | grep -c 'byte'
1
$ tr '\n' ' ' < "$SPEC" | tr -s '[:space:]' ' ' | grep -c 'zzz-phrase-not-present'
0
$ tr '\n' ' ' < "$SPEC" | tr -s '[:space:]' ' ' | grep -c 'one run late'
1
```

Required: body ≤60 → **60**. dispatched ≥6 → **6**. compaction phrase =1 → **1**. tokenizer =1 → **1**.
byte =1 → **1**. control phrase =0 → **0**. "one run late" =1 → **1**. All seven pass.

### Protected paragraph, located by content

```
$ L=$(grep -n '^Acceptance: STATE.md within K1' "$SPEC" | cut -d: -f1); echo "starts at $L"
starts at 58
$ sed -n "${L},$((L+1))p" "$SPEC" | shasum -a 256
c1d0c8c4466a5b9a2ff20fe72a0e28bbb8f2a4896d91cdc7f4c41ed09184948d  -
$ sed -n "${L},$((L+1))p" "$SPEC" | wc -c
     237
```

Hash matches the required `c1d0c8c4...94948d` exactly; byte count is the required 237.

### Blank line before §3's table still present

```
$ H=$(grep -n '^## 3. Constraints and acceptance' "$SPEC" | cut -d: -f1); echo "H=$H"
H=46
$ sed -n "${H},$((H+2))p" "$SPEC" | od -c | head -5
0000000    #   #       3   .       C   o   n   s   t   r   a   i   n   t
0000020    s       a   n   d       a   c   c   e   p   t   a   n   c   e
0000040   \n  \n   |       #       |       C   o   n   s   t   r   a   i
0000060    n   t       |       T   a   g       |  \n
0000073
```

The byte after the heading's `\n` is another `\n`. The blank line survives.

### BLANK-LINE ACCOUNTING — the number that matters

```
$ git diff -- "$SPEC" | grep '^-' | grep -v '^---'
-- **Retain** OPEN, BLOCKED, DEFERRED and IN-PROGRESS as open items. DEFERRED is open; it does not vanish. **DISPATCHED**
-  is handled per §2.3.
$ git diff -- "$SPEC" | grep '^-' | grep -v '^---' | grep -c '^-$'
0
```

**Deleted blank lines: 0.** Exactly two lines deleted in the whole diff, both prose, both from the §2.2 Retain bullet.

### Full diff

```
$ git diff -- docs/specs/2026-08-08-ledger-compaction-spec.md
diff --git a/docs/specs/2026-08-08-ledger-compaction-spec.md b/docs/specs/2026-08-08-ledger-compaction-spec.md
index ce6683b..55b417e 100644
--- a/docs/specs/2026-08-08-ledger-compaction-spec.md
+++ b/docs/specs/2026-08-08-ledger-compaction-spec.md
@@ -24,8 +24,7 @@ own — template gap (b) — compact.sh also regenerates the line `S12: <N> rows
 `scripts/compact.sh`, POSIX shell or stdlib Python, run at session close by a human. It registers no hook.
 - **Archive** rows whose `STATE:` is CLOSED, RESOLVED or SUPERSEDED out of the three ledgers into `archive/<same-name>`,
   appended in file order and never rewritten.
-- **Retain** OPEN, BLOCKED, DEFERRED and IN-PROGRESS as open items. DEFERRED is open; it does not vanish. **DISPATCHED**
-  is handled per §2.3.
+- **Retain** OPEN, BLOCKED, DEFERRED and IN-PROGRESS as open items. DEFERRED does not vanish. **DISPATCHED** per §2.3.
 - **Unknown state is a hard error.** Fail safe toward retention: never archive a row the script cannot classify.
 - **Exit nonzero, loudly,** when STATE.md breaches the ceiling. No soft-warning path — failing loud is the enforcement.
 
@@ -54,6 +53,7 @@ master's, pasted into the brief. A convention, not a hook.
 | K4 | First run with no marker retains every dispatched row | [PROPOSED] |
 | K5 | Unknown state is a hard error, biased to retention | [PROPOSED] |
 | K6 | Environment subtraction stays DEFERRED (D-7) | [PROPOSED] |
+| K7 | compact.sh stages only; it never invokes `git commit` and never writes into `.git/` | [PROPOSED] |
 
 Acceptance: STATE.md within K1 · compact.sh exits nonzero when it is not · Step 3's positive control — one auditor
 answering a known-answer question under the new brief format in under 30,000 tokens — is the empirical check on K1.
@@ -99,3 +99,13 @@ property of this author's formatting rather than of the suite.
 praxis-auditor, and the master must not self-grade. Recorded because the master normally dispatches rather than authors:
 writing to `specs/` is permitted by `master-write-guard.sh:15`, and dispatching a manager to write it would have spent
 the tokens the spec exists to save.
+
+**C-9 — CONTRADICTION, carried not resolved. K7 [PROPOSED]: compact.sh stages only; it never invokes `git commit` and
+never writes into `.git/`.** As filed, the row forbids what it mandates: staging *is* a write into `.git/`. Measured in
+a throwaway repo this session — before `git add` there was no `.git/index` and `.git/objects/` held 0 files; after
+`git add a.txt` the index existed and `.git/objects/ce/013625030ba8dba906f756967f9e9ca394464a` had appeared. The
+wording stands as filed by ruling and is not reworded here; the intended reading is *no commit, and no writes to
+`.git/` beyond those `git add` itself performs*. Second residual: staging-only collides with the commit gate.
+`.claude/hooks/gate-commit.sh:167-176` binds the audit token to the exact staged tree — it compares `git write-tree`
+against the `tree=` recorded at mint and denies on any mismatch — so a compact.sh run between mint and commit denies
+that commit. Both residuals are recorded so they are visible at the ratification gate; neither is resolved here.
```

Three hunks. No fourth. `§3` heading, its blank line, and every other line of §3 untouched apart from the inserted
K7 row.

### C-9 forbidden-content check (0 = absent, as required)

```
$ C9=$(grep -n '^\*\*C-9' docs/specs/2026-08-08-ledger-compaction-spec.md | cut -d: -f1)
$ sed -n "${C9},\$p" ... | tr '\n' ' ' | tr -s ' ' ' ' > c9.txt
$ for p in tokenizer 'one run late' 'since the last compaction'; do printf '%s -> ' "$p"; grep -c "$p" c9.txt; done
tokenizer -> 0
one run late -> 0
since the last compaction -> 0
```

C-9 also makes no claim that compact.sh runs `git add` on archive files; it only states the general fact, measured
above, that `git add` writes into `.git/`.

### Line lengths

```
$ N=$(grep -n 'DEFERRED does not vanish' "$SPEC" | cut -d: -f1); echo "new compressed line is line $N"
new compressed line is line 27
$ awk -v n="$N" 'NR==n{print "length="length($0)}' "$SPEC"
length=119
$ awk '{ if (length($0)>m) {m=length($0); ml=NR} } END {print "max line length="m" (line "ml")"}' "$SPEC"
max line length=127 (line 18)
$ sed -n '27p' "$SPEC" | wc -c
     120
```

The new compressed line is **119 bytes** (120 including the newline). The file's existing maximum is **127 bytes**
(line 18), and 15 pre-existing lines already exceed 120. The new line is therefore comfortably inside the file's
established wrap norm and is not the longest line in the file. Every C-9 line is ≤120 bytes.

### Staging

```
$ cd /Volumes/Sensidine/Praxis.build && git add docs/specs/2026-08-08-ledger-compaction-spec.md
$ git diff --cached --numstat -- docs/specs/2026-08-08-ledger-compaction-spec.md
12	2	docs/specs/2026-08-08-ledger-compaction-spec.md
$ git ls-files -s -- docs/specs/2026-08-08-ledger-compaction-spec.md
100644 55b417ee898f0a9394779f114eaf5a750ca3c157 0	docs/specs/2026-08-08-ledger-compaction-spec.md
$ git diff --name-only -- docs/specs/2026-08-08-ledger-compaction-spec.md
(empty — index matches worktree)
```

Blob is `55b417ee...` — **not** `e69de29b...`, so the content is real, not empty. 12 added / 2 deleted, so not zero
added lines. Staged.

### Index scope — nothing of mine beyond the one path

```
$ git diff --cached --name-only
DECISION_LOG.md
ISSUE_REGISTER.md
MANIFEST.md
docs/reports/2026-08-06-session42-r8j-phase3-import.md
docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
docs/reports/2026-08-07-session44-r8j-offset-correction-adversarial.md
docs/reports/2026-08-07-session44-r8j-offset-correction-worker1.md
docs/reports/2026-08-07-session44-r8j-offset-correction.md
docs/specs/2026-08-08-ledger-compaction-spec.md
```

The first eight were already staged before this task began — they match the `M `/`A ` entries in the session-start
`git status` snapshot (ISSUE_REGISTER.md, MANIFEST.md, DECISION_LOG.md and the five session-42/44 reports).
The spec is the only path I added. No commit was made; no `git add -A`, `git add .`, `checkout`, `reset` or `stash`
was run at any point.

## Files staged
- `/Volumes/Sensidine/Praxis.build/docs/specs/2026-08-08-ledger-compaction-spec.md` (+12 / −2)

## Result: PASS

## Note for the manager (reported, not fixed — out of scope)
C-9's own measurement demonstrates that K7 as filed is unsatisfiable by any script that stages. That is by design and
is now recorded. A second, separate observation surfaced while verifying and is **not** acted on here: the C-2
legality argument at lines 75–77 ("the guards inspect the master's command string only, so writes performed inside a
script the master invokes fall outside the hook surface") and the C-9 gate-commit finding point in opposite
directions — the commit gate binds on the resulting *tree*, not on a command string, so a script-mediated index
change is caught by `gate-commit.sh` regardless of whose command string invoked it. Whether C-2's legality wording
needs a residual is a ratification-gate question, not mine.
