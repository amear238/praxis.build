# Session 39 — Negative tests against `scripts/dispatch-log-close.sh`

**Task:** Adversarial negative-testing of the SubagentStop closing hook.
**Mode:** ADVERSARIAL. Goal was to break the stated contract, not to improve the script.
**Date:** 2026-07-28
**Artifact:** `/Volumes/Sensidine/Praxis.build/scripts/dispatch-log-close.sh`
(registered in `.claude/settings.json` → `SubagentStop` → `"$CLAUDE_PROJECT_DIR"/scripts/dispatch-log-close.sh`, timeout 30)

**Stated contract under test:** appends a closing row to a DISPATCH_LOG.md-format
file; NEVER edits an existing row; always exits 0; idempotent; when it cannot
identify the row to close it degrades to an explicit UNKEYED/unmatched row
rather than fabricating a close.

## Constraints honoured

- All testing ran against fixtures in the session scratch dir. The real ledger was
  never opened for write. Every invocation was wrapped in
  `env -u CLAUDE_PROJECT_DIR PRAXIS_DISPATCH_LOG=<scratch fixture>`.
- Real ledger integrity, checked after all tests:
  ```
  2026-07-28T12:01:32 /Volumes/Sensidine/Praxis.build/DISPATCH_LOG.md size=38049
  f24c107e8faf47cd1f3d7086f8b6b0b3a6f42d56e73602b5dee28dc5f2b69c9c  /Volumes/Sensidine/Praxis.build/DISPATCH_LOG.md
  2026-07-28T16:06:07Z
  ```
  Local time is UTC−4, so the ledger's last write was 16:01:32Z — **before** the
  first test invocation at 16:03:07Z. Untouched by this unit.
- Nothing edited under `scripts/`, `.claude/hooks/`, `.claude/settings.json`, or
  `specs/SPEC_RUBRIC.md`. Nothing staged. No `git add`/`commit`/`stash` run.

## Environment (verified this session)

```
jq-1.7.1-apple
GNU bash, version 5.3.15(1)-release (aarch64-apple-darwin25.4.0)
/usr/bin/jq
```

## Immutability method

For every run: record `before_size` (bytes) and `sha256` of the fixture, invoke
the closer, then `sha256` of the **first `before_size` bytes of the after-file**.
Equality proves every pre-existing byte is unchanged and the write was a pure
append. This is stricter than a line diff — it catches in-place edits of any
length, including ones that preserve line count.

---

## 1. NEGATIVE — token matching NO open row

Fixture: 3 open rows (`corr=aaaa1111bbbb2222c`, `ffff9999eeee8888d`,
`1234abcd5678efab9`) + 1 pre-existing closed row.
Payload: `{"agent_id":"9999zzzz0000yyyy1","agent_type":"praxis-worker",...}`

```
### t1-no-match
exit_code=0
stderr:
IMMUTABLE: YES  first 819B sha256=1fcaf768c956cd6274ebfef6ee604764eadfb6fa8e735f4efa4686898b600f55 == before sha256=1fcaf768c956cd6274ebfef6ee604764eadfb6fa8e735f4efa4686898b600f55
appended bytes: 417
--- appended content ---
- [2026-07-28T16:03:07Z] WHO: praxis-worker | WHAT: subagent stop recorded, no open row matched | WHY: SubagentStop carried corr=9999zzzz0000yyyy1 but no STATE: dispatched row in this log carries that token (already reconciled, writer patch not in effect for that spawn, or token mismatch) | WHERE: n/a - no row is claimed closed | WHEN: stop | HOW: KEYED - token present, lookup miss | STATE: closed@unmatched-token
------------------------
=== rows still STATE: dispatched after t1 (expect 3) ===
3
```

**No fabrication.** No unrelated row is claimed. The row is explicitly
`STATE: closed@unmatched-token` and says `WHERE: n/a - no row is claimed closed`.
All three unrelated open rows remain open. **PASS.**

## 2. NEGATIVE — no usable correlation field

Four shapes, same fixture each time: `{}`, `agent_id:null`, `agent_id:""`,
`agent_id` key absent.

```
### t2-empty-obj
exit_code=0
IMMUTABLE: YES  first 819B sha256=1fcaf768c956cd6274ebfef6ee604764eadfb6fa8e735f4efa4686898b600f55 == before sha256=1fcaf768c956cd6274ebfef6ee604764eadfb6fa8e735f4efa4686898b600f55
- [2026-07-28T16:03:15Z] WHO: unknown | WHAT: subagent stop recorded, correlation unavailable | WHY: no usable correlation token (token-absent) - no claim made about which open row this closes | WHERE: n/a - no row is claimed closed | WHEN: stop | HOW: UNKEYED - reason=token-absent, key=3332656686-2 | STATE: closed@unattributed

### t2-null-id       -> UNKEYED reason=token-absent, key=441958924-46,  STATE: closed@unattributed
### t2-emptystr-id   -> UNKEYED reason=token-absent, key=1425591726-44, STATE: closed@unattributed
### t2-no-id-key     -> UNKEYED reason=token-absent, key=1305152933-81, STATE: closed@unattributed
(all four: exit_code=0, IMMUTABLE: YES, same before sha256)
```

Degrades explicitly. The state token `closed@unattributed` is distinct from the
keyed `closed`, and the row carries `HOW: UNKEYED` plus a machine-readable
`reason=`. No reader would mistake it for a keyed close. **PASS.**

## 3. NEGATIVE — malformed / empty / non-object stdin

```
### t3a-nonjson     (this is not json at all {{{)  exit_code=0  IMMUTABLE: YES  reason=non-json-stdin
### t3b-truncjson   ({"agent_id":"abc)             exit_code=0  IMMUTABLE: YES  reason=non-json-stdin
### t3c-emptystdin  (:)                            exit_code=0  IMMUTABLE: YES  reason=empty-stdin   key=4294967295-0
### t3d-scalar      (12345)                        exit_code=0  IMMUTABLE: YES  reason=token-absent
### t3e-array       (["agent_id","x"])             exit_code=0  IMMUTABLE: YES  reason=token-absent
### t3f-null        (null)                         exit_code=0  IMMUTABLE: YES  reason=non-json-stdin
### t3g-binary      (64B /dev/urandom)             exit_code=0  IMMUTABLE: YES  reason=non-json-stdin
```

Every branch exits 0. Every branch degrades to `STATE: closed@unattributed`.
Nothing corrupted. **PASS.**

## 4. IMMUTABILITY — pre-existing bytes

Across all 25 invocations in this unit, `IMMUTABLE: YES` in every case. Not one
run altered a single pre-existing byte. Specifically checked, the hostile case of
a log **not ending in a newline** (which without the guard would fuse the new row
onto the last existing row and hide it from the `STATE: dispatched$` matcher):

```
### t9a-no-trailing-nl
exit_code=0
IMMUTABLE: YES  first 126B sha256=bf2e395fce6f4b6ea80481fb972931983d325214a747daa2be6f7d33a296e569 == before sha256=bf2e395fce6f4b6ea80481fb972931983d325214a747daa2be6f7d33a296e569
appended bytes: 260
--- appended content ---
$
- [2026-07-28T16:05:56Z] WHO: praxis-worker | WHAT: subagent closed | ... | STATE: closed$
------------------------
last-row integrity check (must still match the dispatched matcher):
1
```

The guard appends one `\n` byte (visible as the leading `$` in `cat -etv`), which
is strictly additive, and the previously-last row still matches the drain matcher.
**PASS — this is the strongest part of the artifact.**

## 5. IDEMPOTENCY — same payload twice

```
### t5a-first  (keyed match)      appended 277B, "matched 1 open row(s)", STATE: closed
### t5a-second                    exit_code=0
                                  stderr: dispatch-log-close.sh: idempotent no-op: corr=aaaa1111bbbb2222c already has a closing row
                                  appended bytes: 0

### t5b-first  (unmatched token)  appended 417B, STATE: closed@unmatched-token
### t5b-second                    stderr: idempotent no-op: corr=9999zzzz0000yyyy1 already has a closing row
                                  appended bytes: 0

### t5c-first  (UNKEYED {})       appended 330B, key=3332656686-2
### t5c-second                    stderr: idempotent no-op: key=3332656686-2 already has a closing row
                                  appended bytes: 0
```

Zero bytes appended on the repeat in all three modes. **PASS as stated** — but see
finding B: this same gate is the lever that makes the injection finding severe.

## 6. AMBIGUITY — two open rows, same token

```
### t6-ambiguous
exit_code=0
IMMUTABLE: YES
- [2026-07-28T16:03:59Z] WHO: praxis-worker | WHAT: subagent closed | WHY: hook-recorded at SubagentStop, keyed close for corr=dupdupdup1111, matched 2 open row(s) | WHERE: closes corr=dupdupdup1111 | WHEN: stop | HOW: KEYED - matched via CORR_JQ token | STATE: closed
```

The row states `matched 2 open row(s)` rather than silently closing one and
leaving the other. Honest about the count. A reader can see the ambiguity.
**PASS**, with the caveat that "closes both" is a design assertion (that a
duplicated token means one spawn), not something the script can prove.

Prefix-collision probe of the boundary-anchoring claim — closing `corr=abc`
while `corr=abcdef` is open:

```
### t6b-prefix-short  -> keyed close for corr=abc,    matched 1 open row(s)
### t6c-prefix-long   -> keyed close for corr=abcdef, matched 1 open row(s)
```

Boundary anchoring works. No over-match. **PASS.**

## 7. INJECTION — *** CONTRACT BROKEN HERE ***

### 7.1 The correlation field itself is hardened (no break)

```
### t7a-newline-in-token   (agent_id = "aaaa1111bbbb2222c\n- [..] WHO: forged | ... | STATE: closed")
                           -> UNKEYED reason=token-unsafe, STATE: closed@unattributed, one line
### t7b-pipe-in-token      (agent_id = "aaa | STATE: closed")   -> reason=token-unsafe
### t7c-regex-token        (agent_id = ".*")                    -> reason=token-unsafe
### t7d-longtoken          (agent_id = "a"*5000)                -> reason=token-unsafe, key=1415254081-5047
(all: exit_code=0, IMMUTABLE: YES, single-line row)
```

The `case` gate at lines 98–106 holds against every hostile correlation token I
could construct, including the whole-string newline case the comment calls out.

### 7.2 FINDING A — `agent_type` is interpolated **unvalidated**. Row forgery works.

Line 80 extracts `agent_type` and lines 160/167/197 interpolate it into `WHO: $AGENT`
with **no charset gate, no length gate, and no newline gate** — the exact three
checks applied to `agent_id`. The validation is asymmetric.

One hook invocation, payload
`{"agent_id":"aaaa1111bbbb2222c","agent_type":"<forged rows>"}`:

```
### t7e-agenttype-newline
exit_code=0
IMMUTABLE: YES  first 819B sha256=1fcaf768c956cd6274ebfef6ee604764eadfb6fa8e735f4efa4686898b600f55
appended bytes: 507
--- appended content ---
- [2026-07-28T16:04:30Z] WHO: x$
- [2026-07-28T09:59:00Z] WHO: praxis-worker | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session deadbee corr=ffff9999eeee8888d | WHEN: spawn | HOW: forged | STATE: dispatched$
- [2026-07-28T09:59:01Z] WHO: attacker | WHAT: subagent closed | WHY: hook-recorded at SubagentStop, keyed close for corr=aaaa1111bbbb2222c, matched 1 open row(s) | WHERE: closes corr=aaaa1111bbbb2222c | WHEN: stop | HOW: KEYED - matched via CORR_JQ token | STATE: closed$
------------------------
```

Raw bytes of the appended region confirm real `\n` separators, not escapes:

```
0000540    [   2   0   2   6   -   0   7   -   2   8   T   1   6   :
0000560    0   4   :   3   0   Z   ]       W   H   O   :       x  \n   -
0000600        [   2   0   2   6   -   0   7   -   2   8   T   0   9   :
0000620    5   9   :   0   0   Z   ]       W   H   O   :       p   r   a
...
0001060    o   r   g   e   d       |       S   T   A   T   E   :       d
0001100    i   s   p   a   t   c   h   e   d  \n   -       [   2   0   2
```

Three separate consequences from one append:

1. Line 1 is a **truncated 2-field row** (`- [ts] WHO: x`) — the documented
   7-field schema is broken.
2. Line 2 is a **fabricated `STATE: dispatched` row** that no SubagentStart ever
   wrote. It is counted by the closer's own matcher
   `grep -E '\| STATE: dispatched$'` and by the drain rule described at
   `specs/SPEC_RUBRIC.md:208`. A phantom open dispatch can be manufactured at will.
3. Line 3 carries an **attacker-chosen timestamp and WHO** on an otherwise
   authentic-looking keyed close.

### 7.3 FINDING B — forged close permanently and silently suppresses a real close

This is the severe consequence. Forge a row containing `corr=<victim>` and
`| STATE: closed`; the closer's own idempotency gate (line 143) then swallows the
victim's genuine SubagentStop forever.

Step 1 — attacker's stop, its own valid `agent_id`, hostile `agent_type`:

```
### t7f-step1-forge
exit_code=0
IMMUTABLE: YES
appended bytes: 420
--- appended content ---
- [2026-07-28T16:04:52Z] WHO: attacker | WHAT: x | WHY: x | WHERE: x | WHEN: stop | HOW: x | STATE: closed@unmatched-token corr=ffff9999eeee8888d |$
- [2026-07-28T09:59:59Z] WHO: attacker | WHAT: subagent closed | WHY: hook-recorded at SubagentStop, keyed close for corr=aaaa1111bbbb2222c, matched 1 open row(s) | ... | STATE: closed$
------------------------
```

Step 2 — the victim subagent (`corr=ffff9999eeee8888d`) now genuinely stops with
its own honest payload:

```
### t7f-step2-victim
exit_code=0
stderr: dispatch-log-close.sh: idempotent no-op: corr=ffff9999eeee8888d already has a closing row
IMMUTABLE: YES
appended bytes: 0
------------------------
>>> Did the victim ever get a close row? (grep for its keyed close)
0
>>> victim row still STATE: dispatched, never closed:
- [2026-07-28T09:01:00Z] WHO: praxis-auditor | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session deadbee corr=ffff9999eeee8888d | WHEN: spawn | HOW: awaiting terminal state | STATE: dispatched
```

The victim's real close is never written, and never can be — the gate is
permanent in an append-only ledger. This is precisely the failure mode the
comment at lines 138–142 says the boundary-anchored matcher was introduced to
prevent ("permanently and silently suppressing its close"). The anchoring fixed
the accidental prefix case; it does not fix the case where the attacker supplies
the whole substring.

### 7.4 FINDING C — the newline is reachable without a newline in any string

Two variants that need no control over string *content*, only over JSON *shape*:

```
### t7g-agenttype-array   payload {"agent_id":"aaaa1111bbbb2222c","agent_type":["praxis-worker","x"]}
- [2026-07-28T16:05:15Z] WHO: [$
  "praxis-worker",$
  "x"$
] | WHAT: subagent closed | ... | STATE: closed$

### t7h-json-stream       payload {"agent_type":"aaa"}{"agent_id":"aaaa1111bbbb2222c","agent_type":"bbb"}
- [2026-07-28T16:05:15Z] WHO: aaa$
bbb | WHAT: subagent closed | ... | STATE: closed$
```

`jq -r` pretty-prints a non-string value across multiple lines, and `jq -e .`
accepts a concatenated JSON stream and emits one result per document. Both turn
a single logical row into several physical lines. The `-e .` validity check at
line 77 does not constrain the payload to a single JSON **object**.

### 7.5 FINDING D — pipes alone break the 7-field schema

```
### t7i-pipes   agent_type = "w | STATE: closed | WHO: ghost"
- [2026-07-28T16:05:16Z] WHO: w | STATE: closed | WHO: ghost | WHAT: subagent closed | ... | STATE: closed
=== field counts of last appended line (schema wants 7 pipe-separated fields => 6 pipes) ===
pipe-separated fields: 9
```

Nine fields where the schema documented at the head of DISPATCH_LOG.md specifies
seven. Any field-position parser reading `WHAT:` from field 2 now reads
`STATE: closed`.

### Reachability — marked honestly

I demonstrated all of 7.2–7.5 at the **script's stdin boundary**, which is where a
hook script's contract is defined and where it validates `agent_id`. Whether the
current Claude Code build can itself emit an `agent_type` containing a newline, an
`agent_type` of non-string type, or a multi-document stdin stream is **UNVERIFIED**
— I did not capture a live hostile payload this session. The defect stands
regardless of that: the script chose to validate one interpolated field precisely
because "a correlation token is interpolated into a grep pattern and into a ledger
row, so it is validated rather than trusted" (lines 84–86), and then interpolated a
second field from the same untrusted payload into the same ledger row without any
validation at all. The existing suite at `scripts/tests/test-dispatch-log-close.sh`
passes a benign `agent_type` in all nine cases, so this surface is untested.

## 8. PATH RESOLUTION

Deciding line:

```
51:LOG="${PRAXIS_DISPATCH_LOG:-${CLAUDE_PROJECT_DIR:-.}/DISPATCH_LOG.md}"
```

Precedence: `PRAXIS_DISPATCH_LOG` → `$CLAUDE_PROJECT_DIR/DISPATCH_LOG.md` → `./DISPATCH_LOG.md`.

Demonstrated in sandbox only — never against the real repo file:

```
=== 8a: PRAXIS_DISPATCH_LOG UNSET, CLAUDE_PROJECT_DIR=<sandbox> ===
exit=0
files created under sandbox project dir:
.../scratchpad/lab/proj8/DISPATCH_LOG.md
--- content ---
# DISPATCH LOG
- [2026-07-28T16:05:32Z] WHO: praxis-worker | WHAT: subagent stop recorded, no open row matched | WHY: SubagentStop carried corr=sandbox8token but no STATE: dispatched row ... | STATE: closed@unmatched-token

=== 8b: BOTH unset -> './DISPATCH_LOG.md' relative to CWD (run in a temp cwd, NOT the repo) ===
exit=0
files created in temp cwd:
.../scratchpad/lab/cwd8/DISPATCH_LOG.md
```

In production the hook is invoked as `"$CLAUDE_PROJECT_DIR"/scripts/dispatch-log-close.sh`,
so `CLAUDE_PROJECT_DIR` is set and the real ledger is the target. Minor latent
hazard: with `CLAUDE_PROJECT_DIR` unset the `.` fallback silently **creates** a
stray `DISPATCH_LOG.md` in whatever the cwd happens to be (observed above) rather
than failing loudly. Not a contract violation; reported, not fixed.

## Summary

| # | Check | Result |
|---|---|---|
| 1 | Non-matching token | PASS — explicit `closed@unmatched-token`, no fabrication |
| 2 | No correlation field | PASS — explicit `closed@unattributed` + reason |
| 3 | Malformed/empty/binary stdin | PASS — exit 0 every branch, no corruption |
| 4 | Immutability | PASS — 25/25 runs, pre-existing bytes byte-identical |
| 5 | Idempotency | PASS as stated (0 bytes on repeat) |
| 6 | Ambiguity | PASS — reports `matched 2 open row(s)` honestly |
| 7 | Injection | **FAIL** — findings A–D |
| 8 | Path resolution | PASS, with a latent `.`-fallback hazard |

The append-only guarantee is genuinely solid and the correlation-token gate is
genuinely hardened. The break is next to them: a second field from the same
untrusted payload reaches the ledger row unvalidated, which forges rows, breaks
the 7-field schema, manufactures phantom `STATE: dispatched` rows, and — via the
script's own idempotency check — permanently suppresses a legitimate close.

Not fixed, per adversarial-mode scope. Nothing staged.

Verdict: CONTRACT VIOLATED
