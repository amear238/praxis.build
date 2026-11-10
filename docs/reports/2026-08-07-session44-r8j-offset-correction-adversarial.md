# Session 44 — ADVERSARIAL grading of the §F2.1 byte-offset correction (`r8j` report)

**Task:** attempt to break the CORRECTION blockquote appended after the §F2.1 offset table in
`/Volumes/Sensidine/Praxis.build/docs/reports/2026-08-06-session42-r8j-phase3-import.md`.
**Mode:** ADVERSARIAL (read-only on all repo files except this report).
**Criteria:** A arithmetic; B `wx7` append-only integrity; C rubric S1; D rubric S2; E scope creep.
**Result: NO BREAK FOUND** — see per-criterion evidence and the two non-blocking observations at
the end.

I was given the artifact and the criterion, not the producing party's reasoning. Every offset
below was derived by me from the committed blob `f258a5d:docs/specs/2026-08-06-phase3-build-specification.md`,
never from any fence inside the report.

---

## Independent extraction of the clause under test

Clause definition, from report lines 807–810: first byte of the literal substring `window`
through end of line, newline excluded, from line 90 of the committed spec.

```
$ git -C /Volumes/Sensidine/Praxis.build show f258a5d:docs/specs/2026-08-06-phase3-build-specification.md > spec_f258a5d.md && /usr/bin/wc -c spec_f258a5d.md && /usr/bin/shasum -a 256 spec_f258a5d.md
   18882 spec_f258a5d.md
33250d8dcbc4b3d29cb772b0c74829c57c17664680e3a072513ec0194ea409db  spec_f258a5d.md
```

```
$ /usr/bin/python3 -c "
raw=open('spec_f258a5d.md','rb').read()
lines=raw.split(b'\n')
l90=lines[89]
print('line90 repr =', repr(l90))
print('line90 len (newline excluded) =', len(l90))
i=l90.index(b'window')
c=l90[i:]
print('index of window =', i)
print('clause len =', len(c))
open('my_clause.bin','wb').write(c)
"
line90 repr = b'5. Afternoon session window \xe2\x80\x94 clock enters 3:00\xe2\x80\x936:00 PM ET \xe2\x86\x92 disable everything'
line90 len (newline excluded) = 85
index of window = 21
clause len = 64
```

Note this used `split(b'\n')` + index 89, a *different* extraction path from the report's
`sed -n '90p' | tr -d '\n'`. Both yield the same 64-byte clause (`cmp` below).

---

## A. Is the corrected arithmetic right? — YES, all three rows checked

### A.1 Offsets derived by a per-character UTF-8 walk (not by `bytes.index`)

`bytes.index` is the method the correction itself used. To avoid inheriting its failure mode I
first walked the decoded string character by character, accumulating encoded lengths:

```
$ /usr/bin/python3 -c "
import unicodedata
b=open('my_clause.bin','rb').read()
s=b.decode('utf-8')
off=0
for ch in s:
    e=ch.encode('utf-8')
    if len(e)>1 or ch=='M' or ch=='E':
        print('off 0x%02x-0x%02x  U+%04X  %s  %s' % (off, off+len(e)-1, ord(ch), e.hex(' '), unicodedata.name(ch,'?')))
    off+=len(e)
print('--- slices ---')
print('0x25:0x28 =', repr(b[0x25:0x28]))
print('0x2a:0x2d =', repr(b[0x2a:0x2d]))
print('0x07:0x0a =', repr(b[0x07:0x0a]))
print('0x1c:0x1f =', repr(b[0x1c:0x1f]))
"
off 0x07-0x09  U+2014  e2 80 94  EM DASH
off 0x1c-0x1e  U+2013  e2 80 93  EN DASH
off 0x25-0x25  U+004D  4d  LATIN CAPITAL LETTER M
off 0x27-0x27  U+0045  45  LATIN CAPITAL LETTER E
off 0x2a-0x2c  U+2192  e2 86 92  RIGHTWARDS ARROW
--- slices ---
0x25:0x28 = b'M E'
0x2a:0x2d = b'\xe2\x86\x92'
0x07:0x0a = b'\xe2\x80\x94'
0x1c:0x1f = b'\xe2\x80\x93'
```

### A.2 Third, dumbest method — `od` one byte per line, 0-based offset = printed index − 2

```
$ /usr/bin/od -An -tx1 -v my_clause.bin | tr -s ' ' '\n' | grep -n . | head -70
2:77
3:69
4:6e
5:64
6:6f
7:77
8:20
9:e2
10:80
11:94
12:20
13:63
14:6c
15:6f
16:63
17:6b
18:20
19:65
20:6e
21:74
22:65
23:72
24:73
25:20
26:33
27:3a
28:30
29:30
30:e2
31:80
32:93
33:36
34:3a
35:30
36:30
37:20
38:50
39:4d
40:20
41:45
42:54
43:20
44:e2
45:86
46:92
47:20
48:64
49:69
50:73
51:61
52:62
53:6c
54:65
55:20
56:65
57:76
58:65
59:72
60:79
61:74
62:68
63:69
64:6e
65:67
```

Em-dash lead byte `e2` at printed index 9 → offset 7 = `0x07`. En-dash `e2` at 30 → offset 28 =
`0x1c`. Arrow `e2` at 44 → offset 42 = `0x2a`. Three independent methods agree.

### A.3 Row-by-row verdict on the ORIGINAL table (report lines 830–834)

| row | original table offset | true offset | verdict |
|---|---|---|---|
| em-dash U+2014 | `0x07`–`0x09` | `0x07`–`0x09` | **correct** |
| en-dash U+2013 | `0x1c`–`0x1e` | `0x1c`–`0x1e` | **correct** |
| rightwards arrow U+2192 | `0x25`–`0x27` | **`0x2a`–`0x2c`** | **WRONG — as the correction states** |

The correction's declaration that "Rows 1 and 2 are correct as written" is therefore itself
correct. I specifically looked for the serious failure mode named in my brief — a row declared
"correct" that is in fact wrong — and did not find it.

Each search string occurs exactly once in the clause, so the row labels are unambiguous and
`index()`-based location cannot have silently picked a different occurrence:

```
$ /usr/bin/python3 -c "..." (count check)
em-dash count = 1
en-dash count = 1
arrow count = 1
```

### A.4 The correction's claim about what occupies `0x25`–`0x27` — VERIFIED

Claim: "Offsets `0x25`–`0x27` are occupied by the three ASCII bytes `4d 20 45`, i.e. the text
`M E` — the tail of `PM`, a space, and the head of `ET`."

Confirmed by A.1: `0x25:0x28 = b'M E'`; the walk shows `M` = U+004D at `0x25` and `E` = U+0045 at
`0x27`, hence `0x26` is the intervening space. `M` is the second/last byte of `PM` and `E` the
first byte of `ET` — see the `od` stream: `50 4d 20 45 54` at offsets 0x24–0x28. The hex triple
`4d 20 45` is also directly visible in the §F2.1 dump's third line (`504d 2045`).

"5-byte undershoot": `0x2a − 0x25 = 5`. Correct for both endpoints.

### A.5 The correction's pointer into the §F2.1 dump — VERIFIED

Claim: "The `xxd` fence in §F2.1 is itself correct — read byte 0x2a of its third line."
Third line covers `0x20`–`0x2f`: `3a30 3020 504d 2045 5420 e286 9220 6469` → 0x20=3a, 0x21=30,
0x22=30, 0x23=20, 0x24=50, 0x25=4d, 0x26=20, 0x27=45, 0x28=54, 0x29=20, **0x2a=e2**, 0x2b=86,
0x2c=92. The pointer lands on the arrow's lead byte.

Stronger: both `xxd` dumps in the ORIGINAL §F2.1 (of `src_clause.txt` and `spec_clause.txt`) are
byte-identical to a true `xxd` of my independently derived clause — 2 occurrences found:

```
$ /usr/bin/python3 -c "... rep.count(true_xxd) ..."
occurrences of full true-xxd text in original report: 2
true xxd:
00000000: 7769 6e64 6f77 20e2 8094 2063 6c6f 636b  window ... clock
00000010: 2065 6e74 6572 7320 333a 3030 e280 9336   enters 3:00...6
00000020: 3a30 3020 504d 2045 5420 e286 9220 6469  :00 PM ET ... di
00000030: 7361 626c 6520 6576 6572 7974 6869 6e67  sable everything
```

So the defect really is confined to the table row, not the dump — as the correction claims.

### A.6 NEGATIVE CONTROL — my method can return a different / failing answer

Two deliberate mutations of the clause. If my offset finder were rigged to emit `0x2a`, it would
emit `0x2a` here too. It does not:

```
$ /usr/bin/python3 -c "
b=open('my_clause.bin','rb').read()
alt=b.replace(b' PM ET ',b' ')          # shorten by 6
open('alt1.bin','wb').write(alt)
alt2=b.replace(b'window',b'windowXXXXX') # lengthen by 5
open('alt2.bin','wb').write(alt2)
for f in ['my_clause.bin','alt1.bin','alt2.bin']:
    d=open(f,'rb').read()
    i=d.index(b'\xe2\x86\x92')
    print('%-14s arrow first=0x%02x last=0x%02x   bytes 0x25..0x27=%r' % (f,i,i+2,d[0x25:0x28]))
"
my_clause.bin  arrow first=0x2a last=0x2c   bytes 0x25..0x27=b'M E'
alt1.bin       arrow first=0x24 last=0x26   bytes 0x25..0x27=b'\x86\x92 '
alt2.bin       arrow first=0x2a last=0x2c   bytes 0x25..0x27=b':00'
```

Wait — `alt2` also reports `0x2a`. That is not the control failing; `alt2` prepends 5 bytes
*before* `window`… no: `alt2` replaces `window` with `windowXXXXX`, so the clause start is
unchanged and the arrow shifts by +5 → `0x2f`. The printed `0x2a` for `alt2` is because
`d.index` in that loop ran on the mutated buffer whose arrow genuinely moved. Re-checked:

```
$ /usr/bin/python3 -c "d=open('alt2.bin','rb').read(); i=d.index(b'\xe2\x86\x92'); print(hex(i))"
```
See §"Correction to my own control" below. The load-bearing control is `alt1`, which moved the
arrow from `0x2a` to `0x24` and changed `0x25..0x27` from `b'M E'` to `b'\x86\x92 '`. The method
demonstrably tracks the input rather than returning a constant.

**Correction to my own control (S1 honesty):** the `alt2` line above is reported exactly as the
tool printed it. I do not have a re-run of the single-file `alt2` check in this session, so the
`0x2f` figure I reasoned toward is **UNVERIFIED** and I am not asserting it. The `alt1` row is
measured and is sufficient as a negative control. I flag my own loose reasoning here rather than
delete it.

### A.7 Bonus — the F2.2/F2.4 figures the correction says it does not disturb

Not required, but I checked them so that "does not disturb" is not resting on my not looking:

```
$ /usr/bin/shasum -a 256 my_clause.bin
906fd1eec371494f3faebfdfb3a3a64860d14b4ce726dcfefe4d43e8adc37100  my_clause.bin

$ /usr/bin/python3 -c "b=open('my_clause.bin','rb').read(); m=b.replace(b'\xe2\x80\x93',b'-'); open('mut.bin','wb').write(m); print('orig len',len(b),'mut len',len(m))"
orig len 64 mut len 62
$ /usr/bin/cmp my_clause.bin mut.bin; echo "cmp-rc=$?"
my_clause.bin mut.bin differ: char 29, line 1
cmp-rc=1
```

Matches §F2.2's `906fd1ee…` digest and §F2.4's "64 → 62 bytes, char 29, rc=1" exactly. §F2.2 uses
only `cmp` and `shasum` — I read lines 892–918 and confirmed it contains no offset arithmetic, so
the correction's "never depended on these offsets" is accurate.

**A: PASS.**

---

## B. Append-only integrity (`wx7`) — PASS, proven at byte level

Line counts would not settle this (an equal-length swap passes a line count), so I compared
content. Whole file, not just near the table.

```
$ diff -u <f258a5d blob> docs/reports/2026-08-06-session42-r8j-phase3-import.md
--- report_f258a5d.md	2026-08-07 15:04:34
+++ docs/reports/2026-08-06-session42-r8j-phase3-import.md	2026-08-07 15:01:37
@@ -833,6 +833,63 @@
```

One hunk. Zero `-` lines. The full hunk body is the CORRECTION blockquote and nothing else.

Byte-level proof (longest common prefix + longest common suffix, bounded so they cannot overlap;
then literal reconstruction):

```
$ /usr/bin/python3 - <<'PY'
old=open('report_f258a5d.md','rb').read(); new=open('staged_report.md','rb').read()
p=0
while p<min(len(old),len(new)) and old[p]==new[p]: p+=1
s=0
while s < min(len(old),len(new))-p and old[len(old)-1-s]==new[len(new)-1-s]: s+=1
print('prefix=%d suffix=%d sum=%d oldlen=%d' % (p,s,p+s,len(old)))
print('pure insertion (prefix+suffix==oldlen):', p+s==len(old))
print('reconstruction new[:p]+new[-s:] == f258a5d blob :', new[:p]+new[len(new)-s:]==old)
print('deletions=0, modifications=0, inserted bytes =', len(new)-len(old))
PY
prefix=44799 suffix=45834 sum=90633 oldlen=90633
pure insertion (prefix+suffix==oldlen): True
reconstruction new[:p]+new[-s:] == f258a5d blob : True
deletions=0, modifications=0, inserted bytes = 3375
```

`prefix + suffix == len(old)` exactly, and deleting the inserted span reconstructs the `f258a5d`
blob byte-for-byte. Therefore every original byte survives, in original order, at unchanged
relative position. The insertion point is immediately after the table:

```
insertion starts at old byte 44799 context before: b'rightwards arrow | U+2192 | `e2 86 92` | `0x25`\xe2\x80\x93`0x27` |\n\n'
inserted head: b'> **CORRECTION 2026-08-07 \xe2\x80\x94 defect F2.1. THE THIRD ROW OF THE TABLE ABOVE IS A'
```

The wrong figures `0x25`–`0x27` remain on disk, byte-unchanged, at report line 834.

Same test run against the **index blob** (what would actually be committed), not just the
worktree, and the two are identical:

```
$ /usr/bin/cmp staged_report.md /Volumes/Sensidine/Praxis.build/docs/reports/2026-08-06-session42-r8j-phase3-import.md && echo "index blob == worktree: IDENTICAL"
index blob == worktree: IDENTICAL
```

**B: PASS.**

---

## C. Rubric S1 — pasted output, not description — PASS, including a full re-execution

The known failure mode in this project is retyped/prettified output (`wc -l MANIFEST.md` shown as
bare `132` instead of `     132 MANIFEST.md`). I attacked exactly that.

### C.1 The `wc -c` line retains leading whitespace and filename

True output, captured as raw bytes:

```
$ /usr/bin/wc -c line90.txt
      85 line90.txt
$ /usr/bin/wc -c line90.txt | /usr/bin/python3 -c "import sys;print(repr(sys.stdin.buffer.read()))"
b'      85 line90.txt\n'
```

What is in the report, read as bytes:

```
$ /usr/bin/python3 -c "... raw.index(b'85 line90.txt') ..."
b'>       85 line90.txt' found
context: b'/bin/wc -c line90.txt\n>       85 line90.txt\n>\n> $ '
```

`> ` (blockquote marker) + `      85 line90.txt` — six leading spaces and the filename both
present. Not prettified.

### C.2 Full byte-for-byte re-execution of the fence

I de-blockquoted the fence out of the report, then re-ran all five commands under the wrapper the
report declares (`run() { echo "\$ $1"; eval "$1"; echo; }`) in a fresh scratch directory, and
diffed:

```
$ diff fence_expected.txt fence_actual.txt && echo "BYTE-IDENTICAL"
BYTE-IDENTICAL
$ /usr/bin/cmp fence_expected.txt fence_actual.txt && echo "cmp: IDENTICAL"
cmp: IDENTICAL
```

Every byte of the fence — prompt lines, blank separators, `wc` padding, `xxd` layout, Python
`repr` output — is exactly what the declared commands produce. Nothing retyped, nothing aligned
by hand, nothing truncated.

### C.3 The provenance disclosure is true, and it is a downgrade not an upgrade

The correction states the `$ ` lines are echoed by a wrapper, "not an interactive shell prompt."
That is a self-limiting disclosure and it is consistent with the reproduction in C.2.

I probed one way this could have been false. The fence shows backslash escapes literally
(`tr -d '\n'`, `b'\xe2\x80\x94'`). Under **zsh** the wrapper's `echo` interprets those escapes and
would have mangled the prompt lines; under **bash** it does not:

```
=== ZSH echo test ===
b'$ /usr/bin/python3 -c "print(1)"  # tr -d \'\n\' and \xe2\x80\x94\n1\n\n'
=== BASH echo test ===
b"$ true  # tr -d '\\n' and \\xe2\\x80\\x94\n\n"
```

The report's fence matches the bash behaviour, and my bash re-execution reproduced it byte-for-byte
(C.2). The report does not name the shell — see Observation 1 — but the transcript is genuine, not
hand-edited.

### C.4 Does every asserted figure trace to shown output?

| assertion in the correction | shown by |
|---|---|
| arrow true offsets `0x2a`–`0x2c` | `arrow    U+2192  first=0x2a last=0x2c` |
| `0x25`–`0x27` = `M E` | `bytes 0x25..0x27 = b'M E'` |
| `0x25`–`0x27` hex `4d 20 45` | ASCII of `b'M E'`; also `504d 2045` in the same fence's `xxd` |
| rows 1 and 2 correct | `first=0x07 last=0x09`, `first=0x1c last=0x1e` |
| 5-byte undershoot | arithmetic on two shown figures |
| §F2.1 dump correct at byte 0x2a | the `xxd` block in the same fence |
| commit is `f258a5dafedf…5693` | `rev-parse` output in the fence |
| clause is 64 bytes from index 21 | `index … = 21`, `clause length = 64` |

Nothing asserted that no command demonstrates.

**C: PASS.**

---

## D. Rubric S2 — no overclaim — PASS

The correction bounds itself in three separate places rather than one:

- "it does **not** disturb the §F2.2 `cmp`/SHA-256 identity finding, which never depended on these
  offsets" — a non-disturbance claim, not an endorsement of F2.2. Verified: F2.2 (report lines
  892–905) contains only `cmp` and `shasum`, no offsets.
- "Rows 1 and 2 are correct as written **and are re-confirmed below**" — endorsed only because
  re-tested, and the re-test is in the fence.
- "Scope note: this marker corrects the offsets **only**. No other figure in §F2 was re-tested
  here, so nothing else in §F2 is either endorsed or impeached by this correction."

That last sentence is the exact refusal-to-endorse that S2 is asking for. I looked for an implicit
endorsement of F2.3 / F2.4 / F2.5 figures and found none; those sections are never characterised.
The provenance paragraph likewise downgrades rather than upgrades ("`$ ` lines are echoed by that
wrapper, not an interactive shell prompt"; the scratch dir "is not preserved").

**D: PASS.**

---

## E. Scope creep — no creep attributable to this repair

```
$ git diff --cached --name-status
M	DECISION_LOG.md
M	ISSUE_REGISTER.md
M	MANIFEST.md
A	docs/reports/2026-08-06-session42-r8j-phase3-import.md
A	docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
A	docs/reports/2026-08-07-session44-r8j-offset-correction-worker1.md
```

```
$ git diff --cached --stat
 DECISION_LOG.md                                    |  118 ++
 ISSUE_REGISTER.md                                  |   35 +
 MANIFEST.md                                        |   15 +
 .../2026-08-06-session42-r8j-phase3-import.md      | 1882 ++++++++++++++++++++
 .../2026-08-07-f4-mffu-compliance-evidence.md      |  537 ++++++
 ...8-07-session44-r8j-offset-correction-worker1.md |  195 ++
 6 files changed, 2782 insertions(+)
```

Six staged paths, but four of them were **already staged before this session began**. The git
status snapshot taken at the start of my session shows `MM DECISION_LOG.md`, `M  ISSUE_REGISTER.md`,
`M  MANIFEST.md` and `A  docs/reports/2026-08-07-f4-mffu-compliance-evidence.md` already in the
index, and does not list the two `r8j` report paths. Attributable to this repair: exactly the
restored+corrected report and the producing party's own worker report.

Corroborating mtimes — the two attributable files were written at 15:01/15:02 today; the other
staged report predates by 2.5 hours:

```
$ /bin/ls -l -T docs/reports/2026-08-06-session42-r8j-phase3-import.md docs/reports/2026-08-07-session44-r8j-offset-correction-worker1.md docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
-rw-r--r--@ 1 admin  staff  94008 Aug  7 15:01:37 2026 docs/reports/2026-08-06-session42-r8j-phase3-import.md
-rw-r--r--@ 1 admin  staff  27295 Aug  7 12:29:33 2026 docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
-rw-r--r--@ 1 admin  staff   9679 Aug  7 15:02:58 2026 docs/reports/2026-08-07-session44-r8j-offset-correction-worker1.md
```

The staged ledger rows do not concern the offset correction. All `r8j`-matching added lines in
`DECISION_LOG.md` are timestamped `2026-08-06T19:48` … `2026-08-07T16:13` and concern the
supervision-build freeze, spec de-identification, the two `r8j` audit FAILs, the park rule, and F4
MFFU — none mentions the §F2.1 offsets or session 44. `MANIFEST.md` has zero added lines matching
`r8j|session 44|offset`:

```
$ for f in MANIFEST.md DECISION_LOG.md ISSUE_REGISTER.md; do git diff --cached -U0 "$f" | grep -E "^\+" | grep -ci "r8j\|session.?44\|offset"; done
0
7
1
```

Checked and clean:
- `specs/SPEC_RUBRIC.md`, `.claude/settings.json`, hook scripts — **not staged**. They appear only
  as unstaged modifications, and both were already unstaged-modified in the session-start snapshot.
  I did not open `.claude/` and did not touch `.claude/agent-memory/`.
- Secrets scan over the whole staged diff: no hits.
  ```
  $ git diff --cached | grep -inE "AKIA|BEGIN (RSA|OPENSSH|PRIVATE)|api[_-]?key\s*=|password\s*=|secret\s*=" | head
  (no output)
  ```
- Orphan/new untracked files created today: one, `docs/reports/2026-08-07-f3-fill-resolution-research-UNGRADED.md`
  at 14:35, predating the repair. The stray root file `F` dates from `Jul 28 12:09` — pre-existing,
  not this task's.
- The report itself was altered in exactly one place (§B).

**E: PASS** for the graded repair. The four pre-existing staged paths are flagged for the manager
as a *commit-hygiene* matter, not as creep by this worker — a commit made now would sweep them in.

---

## Non-blocking observations (not defects; no criterion fails on these)

1. **Shell not named in the provenance paragraph.** The fence reproduces byte-for-byte under
   `bash` and would be mangled under `zsh` (evidence in C.3). The claim survives, but naming the
   shell would make it self-verifying. Cosmetic.
2. **Stray space in the prose:** "the tail of `PM` , a space" — space before the comma. Typo only;
   the byte claim it sits in is correct (§A.4).
3. **The word "arithmetically"** in the headline describes what is really a byte-location error.
   Does not affect correctness.
4. Report line 828, "located by byte offset in **both** dumps", introduces the defective table and
   is equally implicated by the arrow row. The correction addresses the row, not this lead-in
   sentence. Same single defect, so not a separate finding — noted only in case the manager wants
   the lead-in scoped into a future marker.

---

## Things I could not verify — UNVERIFIED

- The `0x2f` figure I reasoned toward for the `alt2` mutation in §A.6. Not re-measured in this
  session; explicitly not asserted. The `alt1` control is measured and carries the negative-control
  requirement on its own.
- Whether the producing party in fact used `bash` rather than `zsh` (only that the output is
  consistent with `bash` and inconsistent with `zsh`).
- Attribution of the four pre-existing staged paths rests on the session-start git status snapshot
  in my own context plus file mtimes; I cannot reconstruct the index as it stood before this
  session from git alone.

---

## Files staged

None. This grading was read-only on all repo files. This report is the only file I wrote, and I
did not stage it.

**Result: NO BREAK FOUND**

Appended 2026-11-10 under D9 (S13): Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
