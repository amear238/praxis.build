# Session 44 — `Praxis_build-r8j` worker 1 — §F2.1 byte-offset correction

## Task

Verify, then correct **by append**, a reported arithmetic error in the §F2.1 byte-offset
locator table (lines 828–834) of
`/Volumes/Sensidine/Praxis.build/docs/reports/2026-08-06-session42-r8j-phase3-import.md`.

## Mode

BUILD.

## Criterion

**S1** — "Every claim in a report has pasted command output, not a description of output."
Secondary: **S2** — do not report a claim at a higher level than the evidence supports.

## Process log

1. Read lines 795–855 of the target report to see the clause definition (lines 807–810) and
   the table under test (lines 828–834).
2. Treated the manager's characterisation as a claim, not a fact. Re-derived the clause from
   the **committed blob** (`git show f258a5d:docs/specs/2026-08-06-phase3-build-specification.md`),
   not from the report's own `xxd` fence, so the check is independent of the artifact it audits.
3. Located each of the three characters by byte offset with `python3` `bytes.index`, and dumped
   the clause with `/usr/bin/xxd`.
4. **First transcript attempt was discarded.** It ran `git` from the scratch directory, which is
   not a git worktree, so `rev-parse` and `show` both failed with
   `fatal: not a git repository`, `line90.txt` was written 0 bytes, and the `xxd` step silently
   read a **stale `clause.txt` left over from an earlier exploratory run**. That transcript
   produced correct-looking numbers from the wrong provenance. It was thrown away and the whole
   sequence re-run in a freshly `rm -rf`'d directory with `git -C <repo>`. Recording this because
   the discarded fence would have passed casual review.
5. Derived offsets contradicted the table in exactly one row. Appended a correction marker
   immediately after line 834, in the existing `> **CORRECTION 2026-08-07 — ...**` blockquote
   convention used at lines 117, 158, 452 and 495.
6. Verified the append was insertion-only and that lines 828–834 are byte-unchanged.

## Verification evidence

### Derivation of the true offsets (clean re-run; raw, unedited)

The `$ ` lines are echoed by a wrapper function `run() { echo "\$ $1"; eval "$1"; echo; }`,
not by an interactive shell prompt. Everything beneath each `$ ` line is unmodified command
output.

```
$ git -C /Volumes/Sensidine/Praxis.build rev-parse f258a5d
f258a5dafedf454f30e8d82f4134857caafd5693

$ git -C /Volumes/Sensidine/Praxis.build show f258a5d:docs/specs/2026-08-06-phase3-build-specification.md | sed -n '90p' | tr -d '\n' > line90.txt; /usr/bin/wc -c line90.txt
      85 line90.txt

$ /usr/bin/python3 -c "b=open('line90.txt','rb').read(); i=b.index(b'window'); open('clause.txt','wb').write(b[i:]); print('index of literal window in line 90 =', i); print('clause length =', len(b)-i)"
index of literal window in line 90 = 21
clause length = 64

$ /usr/bin/xxd clause.txt
00000000: 7769 6e64 6f77 20e2 8094 2063 6c6f 636b  window ... clock
00000010: 2065 6e74 6572 7320 333a 3030 e280 9336   enters 3:00...6
00000020: 3a30 3020 504d 2045 5420 e286 9220 6469  :00 PM ET ... di
00000030: 7361 626c 6520 6576 6572 7974 6869 6e67  sable everything

$ /usr/bin/python3 -c "
b=open('clause.txt','rb').read()
for n,s in [('em-dash  U+2014',b'\xe2\x80\x94'),('en-dash  U+2013',b'\xe2\x80\x93'),('arrow    U+2192',b'\xe2\x86\x92')]:
    i=b.index(s); print('%s  first=0x%02x last=0x%02x' % (n,i,i+2))
print('bytes 0x25..0x27 =', repr(b[0x25:0x28]))
print('bytes 0x2a..0x2c =', repr(b[0x2a:0x2d]))
"
em-dash  U+2014  first=0x07 last=0x09
en-dash  U+2013  first=0x1c last=0x1e
arrow    U+2192  first=0x2a last=0x2c
bytes 0x25..0x27 = b'M E'
bytes 0x2a..0x2c = b'\xe2\x86\x92'
```

### The discarded first attempt (kept, not hidden — this is why it was discarded)

```
$ git rev-parse f258a5d
fatal: not a git repository (or any of the parent directories): .git

$ git show f258a5d:docs/specs/2026-08-06-phase3-build-specification.md | sed -n '90p' | tr -d '\n' > line90.txt; /usr/bin/wc -c line90.txt
fatal: not a git repository (or any of the parent directories): .git
       0 line90.txt

$ /usr/bin/python3 -c "b=open('line90.txt','rb').read(); i=b.index(b'window'); open('clause.txt','wb').write(b[i:]); print('start index of window in line 90 =', i)"
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ValueError: subsection not found

$ /usr/bin/xxd clause.txt
00000000: 7769 6e64 6f77 20e2 8094 2063 6c6f 636b  window ... clock
00000010: 2065 6e74 6572 7320 333a 3030 e280 9336   enters 3:00...6
00000020: 3a30 3020 504d 2045 5420 e286 9220 6469  :00 PM ET ... di
00000030: 7361 626c 6520 6576 6572 7974 6869 6e67  sable everything
```

The `xxd` output here is real but came from a stale file, not from this run's `git show`.
It is retained only as the reason the run was redone.

### Derived offsets vs. the table as written

| character | table (lines 830–834) | derived from `f258a5d` | verdict |
|---|---|---|---|
| em-dash U+2014 | `0x07`–`0x09` | `0x07`–`0x09` | matches |
| en-dash U+2013 | `0x1c`–`0x1e` | `0x1c`–`0x1e` | matches |
| rightwards arrow U+2192 | `0x25`–`0x27` | **`0x2a`–`0x2c`** | **contradicts** |

Offsets `0x25`–`0x27` in fact hold `4d 20 45` = `M E`. The stated row undershoots by 5 bytes.

**On the manager's claim:** it said "one row is reported to be arithmetically wrong" without
naming the row. My independent derivation confirms exactly one row is wrong and identifies it
as row 3. Rows 1 and 2 are correct as written; I did not correct toward the characterisation.

### Insertion-only proof

```
$ git diff --numstat -- docs/reports/2026-08-06-session42-r8j-phase3-import.md
57	0	docs/reports/2026-08-06-session42-r8j-phase3-import.md
--- deletions (should be none) ---
0
rc=1
```

(`rc=1` is `grep -c` reporting zero matches for `^-[^-]`, i.e. zero deleted lines.)

### Lines 828–834 byte-unchanged

```
$ sed -n '828,834p' docs/reports/2026-08-06-session42-r8j-phase3-import.md | /usr/bin/shasum -a 256 && git show f258a5d:docs/reports/2026-08-06-session42-r8j-phase3-import.md | sed -n '828,834p' | /usr/bin/shasum -a 256
6f2c21e1ba9e60330ec50356dd824ebd6b3a244d951cbbdf9110395185737a25  -
6f2c21e1ba9e60330ec50356dd824ebd6b3a244d951cbbdf9110395185737a25  -
```

Working-tree lines 828–834 hash-identical to the same lines in `f258a5d`.

### `git diff --cached --stat`

Captured after `git add` of both files:

```
$ git add docs/reports/2026-08-06-session42-r8j-phase3-import.md docs/reports/2026-08-07-session44-r8j-offset-correction-worker1.md && git diff --cached --stat -- docs/reports/2026-08-06-session42-r8j-phase3-import.md docs/reports/2026-08-07-session44-r8j-offset-correction-worker1.md
 .../2026-08-06-session42-r8j-phase3-import.md      | 1882 ++++++++++++++++++++
 ...8-07-session44-r8j-offset-correction-worker1.md |  184 ++
 2 files changed, 2066 insertions(+)
```

Two notes so these figures are not over-read. (a) The `...` path elision is **git's own default
`--stat` abbreviation**, emitted by git, not applied by me; the output is otherwise verbatim,
leading spaces included. (b) **1882 is not the size of my change.** The import report was already
staged as `A` (whole file new to the index) before I touched it, so `--cached` shows the entire
file. My contribution to it is the +57/−0 shown by the working-tree `git diff --numstat` above.
The 184-line count for this report is its length at the moment of that `git add`; this very
paragraph was written afterwards, so the final file is longer and was re-staged.

## Text appended

Inserted immediately after line 834, before the blank line preceding `### F2.2`. Opens
`> **CORRECTION 2026-08-07 — defect F2.1. THE THIRD ROW OF THE TABLE ABOVE IS ARITHMETICALLY
WRONG.**` It names row 3 (rightwards arrow U+2192), gives the true offsets `0x2a`–`0x2c`,
states that `0x25`–`0x27` actually holds `4d 20 45` = `M E`, re-confirms rows 1 and 2, notes
the §F2.1 `xxd` dump is itself correct, notes the §F2.2 `cmp`/SHA-256 finding is undisturbed,
embeds the raw transcript above, declares the `run()` wrapper provenance of the `$ ` lines,
and closes with a scope note that nothing else in §F2 was re-tested. Full text is in the file
at the lines immediately following 834.

## Files staged

- `docs/reports/2026-08-06-session42-r8j-phase3-import.md` (+57, −0)
- `docs/reports/2026-08-07-session44-r8j-offset-correction-worker1.md` (new)

## Out of scope — reported, not fixed

Nothing further found. I did not inspect audit items 2–8, the two non-blocking stale figures,
or any other report.

## UNVERIFIED / limits of this evidence

- I verified the clause **as reconstructed from `f258a5d`**. I did not verify that `f258a5d` is
  the tip of `parked/Praxis_build-r8j`, nor that the report file in the worktree is otherwise
  identical to the one at that commit beyond lines 828–834, which I hashed.
- The `> **CORRECTION ...**` convention was read from lines 117 and 452 only. Lines 158 and 495
  were named in the brief but I did not open them; my marker follows the two I read. UNVERIFIED
  whether 158/495 differ in shape.
- Whether the `wx7` preservation ruling has any requirement beyond "do not edit the original"
  is UNVERIFIED — I did not read the ruling itself, only followed the brief's statement of it.
- I did not attempt any commit, and therefore did not exercise `scripts/no-commit-guard.sh`.
  The brief's note about that guard false-positiving on `git merge-base` is UNTESTED by me; I
  never needed an ancestry query. No read-only command I ran was blocked.

## Result

**PASS** — defect independently confirmed at source, corrected by append, original bytes intact.

Appended 2026-11-10 under D9 (S13): Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
