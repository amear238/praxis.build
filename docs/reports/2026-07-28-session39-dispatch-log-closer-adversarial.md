# Session 39 — Adversarial audit of dispatch-log-close.sh / dispatch-log-writeahead.sh (Praxis_build-43n)

Mode: ADVERSARIAL, worker 2 of MAX-2. Target: falsify the five claims (a)-(e) about the
writer/closer pair. Did not read the builder's own report or any 2026-07-28-dated report,
per brief. All fixtures created under `mktemp -d`, `PRAXIS_DISPATCH_LOG` pointed at the
fixture in every run. The real `DISPATCH_LOG.md` was never written to by this session — see
verification at the end.

Environment actually used (checked, not assumed): `jq-1.7.1-apple`; `/bin/bash` invoked by the
scripts resolves to GNU bash 3.2.57 (macOS system bash); `grep` resolved by a script run via
`/bin/bash script.sh` is `/usr/bin/grep` (BSD grep) — the interactive shell's `grep` wrapper
function (which shells out to `ugrep` via the Claude Code binary) is a zsh/bash **interactive**
function sourced from the profile and is confirmed **not** inherited by a fresh `/bin/bash`
subprocess (`env | grep BASH_FUNC` empty; explicit path checks below).

Real log measured at session start: `DISPATCH_LOG.md` has 81 `STATE: dispatched` rows, of
which exactly **1** carries a `corr=` token.

---

## Attack 1 — log path is a directory

**Hypothesis:** pointing `PRAXIS_DISPATCH_LOG` at a directory instead of a file forces every
`>>`/`echo >>` in the closer to fail; does the script still exit 0?

**Command + output:**
```
$ mkdir -p "$LOG"          # $LOG is now a directory, not a file
$ printf '%s' '{"agent_id":"X1","agent_type":"praxis-worker","hook_event_name":"SubagentStop"}' \
  | PRAXIS_DISPATCH_LOG="$LOG" /bin/bash "$CLOSER"
/Volumes/Sensidine/Praxis.build/scripts/dispatch-log-close.sh: line 95: .../DISPATCH_LOG.md: Is a directory
/Volumes/Sensidine/Praxis.build/scripts/dispatch-log-close.sh: line 130: .../DISPATCH_LOG.md: Is a directory
EXIT CODE: 0
```
**Verdict: SURVIVED** for claim (c) (exit 0). Secondary note: the raw bash "Is a directory"
messages leak to real stderr **despite** the `2>/dev/null` written on those same lines — this
is a known bash ordering quirk (the shell's own redirection-open failure is reported before
the `2>/dev/null` on the same command line takes effect). Exit code is unaffected; flagged as
a stderr-hygiene defect, not a break of any of (a)-(e).

## Attack 2 — log file read-only (chmod 444), and parent directory read-only (chmod 555)

**Command + output (file read-only):**
```
$ chmod 444 "$LOG"
$ printf '%s' '{"agent_id":"RO-TOKEN", ...}' | PRAXIS_DISPATCH_LOG="$LOG" /bin/bash "$CLOSER"
.../dispatch-log-close.sh: line 137: .../DISPATCH_LOG.md: Permission denied
EXIT CODE: 0
--- log content after (unchanged) ---
# DISPATCH LOG
- [...] ... corr=RO-TOKEN ... STATE: dispatched
```
**Command + output (parent dir read-only, log missing):**
```
$ chmod 555 "$D2/locked"
$ printf '%s' '{"agent_id":"RODIR-TOKEN", ...}' | PRAXIS_DISPATCH_LOG="$D2/locked/DISPATCH_LOG.md" /bin/bash "$CLOSER"
.../dispatch-log-close.sh: line 95: .../locked/DISPATCH_LOG.md: Permission denied
.../dispatch-log-close.sh: line 130: .../locked/DISPATCH_LOG.md: Permission denied
EXIT CODE: 0
--- file was not created (expected, dir is read-only) ---
```
**Verdict: SURVIVED** for (c) exit-0 and (b) append-only (no existing bytes touched; nothing
new written either, but nothing was falsely claimed as written).

## Attack 3 — absurdly large stdin (50MB)

**Command + output:**
```
$ python3 -c "...50,000,000 char 'pad' field..." > huge_payload.json   # 50000096 bytes
$ time (cat huge_payload.json | PRAXIS_DISPATCH_LOG="$LOG" /bin/bash "$CLOSER")
... 6.15s user 0.67s system 102% cpu 6.628 total
EXIT CODE: 0
--- tail of log ---
...WHY: SubagentStop carried corr=HUGE-TOKEN but no STATE: dispatched row ... | STATE: closed@unmatched-token
```
**Verdict: SURVIVED.** Handled correctly, exit 0, honest miss (no open row existed for
HUGE-TOKEN in this fixture). Took 6.6s for 50MB — not tested against an actual Claude Code
hook timeout value, flagged under "not tested."

## Attack 4 — stdin is syntactically valid JSON but not a JSON object

**Command + output (all six payloads, one log per case):**
```
payload: []      -> EXIT 0, UNKEYED reason=token-absent
payload: "str"   -> EXIT 0, UNKEYED reason=token-absent
payload: null    -> EXIT 0, UNKEYED reason=non-json-stdin   <-- mislabeled, see below
payload: 123     -> EXIT 0, UNKEYED reason=token-absent
payload: true    -> EXIT 0, UNKEYED reason=token-absent
payload: {}      -> EXIT 0, UNKEYED reason=token-absent
```
**Verdict: SURVIVED for (c)/(d)** — no crash, no false close claim in any case. **Minor,
separately-flagged defect:** `null` is syntactically valid JSON, but `jq -e .` treats a
top-level `null` (and `false`) output as boolean-false, so `jq -e .` returns non-zero on it —
the script's own branching therefore records `REASON="non-json-stdin"` for a payload that
*was* valid JSON. This is a self-diagnostic accuracy bug (the ledger's "WHY" text is
factually wrong about *why* correlation failed), but it never causes a false *closing* claim
and the outcome (UNKEYED, no row claimed) is still correct. Not counted as a break of (a)-(e).

## Attack 5 — deeply nested JSON (10,000 levels of `[`)

**Command + output:**
```
$ python3 -c "print('['*10000 + ']'*10000)" > deep.json   # 20001 bytes
$ cat deep.json | PRAXIS_DISPATCH_LOG="$LOG" /bin/bash "$CLOSER"
EXIT CODE: 0
...UNKEYED - reason=non-json-stdin, key=349147114-20000 | STATE: closed@unattributed
```
**Verdict: SURVIVED.** `jq -e .` apparently declines (recursion-limited or similar) and the
script falls back cleanly. No crash, exit 0.

## Attack 6 — NUL bytes embedded in stdin

**Command + output:**
```
$ python3 -c "...b'{\"agent_id\":\"NUL-TOKEN\",\"agent_type\":\"praxis-\x00worker\",...}'..." > nul_payload.bin
$ cat nul_payload.bin | PRAXIS_DISPATCH_LOG="$LOG2" /bin/bash "$CLOSER"
EXIT CODE: 0
--- resulting log ---
...WHO: praxis-worker | WHAT: subagent closed | WHY: ... corr=NUL-TOKEN, matched 1 open row(s) ... STATE: closed
```
**Verdict: SURVIVED.** `$(cat ...)` command substitution silently drops the NUL byte
(bash strings are NUL-terminated internally), yielding `"praxis-worker"` from
`"praxis-\x00worker"` — no crash. Correlation on `agent_id` (which had no NUL in this case)
worked correctly. Exit 0.

## Attack 7 — prefix/substring collision in `grep -F` → FALSE CLOSURE of an unrelated, still-open spawn

**This is the most serious break found.** `grep -F "corr=$TOKEN"` is an *unanchored substring*
search. If token A is a literal prefix of token B, closing A also counts B's row as a match.

**Setup:** two real OPEN rows: `corr=abc` (the token that is actually stopping) and
`corr=abcdef` (a **different, still-running** spawn). A SubagentStop for `agent_id=abc`
arrives.

**Command + output:**
```
--- log BEFORE ---
# DISPATCH LOG
- [...] ... corr=abc | ... STATE: dispatched
- [...] ... corr=abcdef | ... STATE: dispatched

$ printf '%s' '{"agent_id":"abc","agent_type":"praxis-worker","hook_event_name":"SubagentStop"}' \
  | PRAXIS_DISPATCH_LOG="$LOG" /bin/bash "$CLOSER"
EXIT CODE: 0

--- log AFTER ---
# DISPATCH LOG
- [...] ... corr=abc | ... STATE: dispatched
- [...] ... corr=abcdef | ... STATE: dispatched
- [2026-07-28T15:39:18Z] WHO: praxis-worker | WHAT: subagent closed | WHY: hook-recorded at
  SubagentStop, keyed close for corr=abc, matched 2 open row(s) | WHERE: closes corr=abc |
  WHEN: stop | HOW: KEYED - matched via CORR_JQ token | STATE: closed
```
The closing row asserts **"matched 2 open row(s)"** for a stop event that corresponds to
exactly one real spawn. The `corr=abcdef` row is a different, unrelated, still-running
spawn — its `STATE: dispatched` text is never edited (append-only literally holds), but the
new row's own claim ("matched 2 open row(s)... closes corr=abc") is read naturally by a human
auditor as "both of these are now accounted for," which is false: `abcdef` has not stopped.

**Verdict: BROKEN.** Directly falsifies claim (d): "the closer never makes a false claim
about which spawn ended." The script's own comment (line ~132-136) argues that a MATCHES>1
count is always "a duplicate write-ahead row... about the one spawn that token names" —
this reasoning is not defensive against a *different* spawn's token merely containing this
token as a substring, which is exactly what was constructed here.

## Attack 8 — same substring flaw on the idempotency (`ALREADY`) check → permanent silent orphan (over-dedupe)

**Hypothesis:** if the *idempotency* check also uses unanchored `grep -F "corr=$TOKEN"`
against the whole log, a **prior** closing row for a longer token that contains this token as
a prefix will falsely satisfy the idempotency check for a **later, genuinely different**
spawn — silently and permanently dropping its close.

**Setup:** two OPEN rows, `corr=abcdef` and `corr=abc` (abc is a prefix of abcdef). Close
`abcdef` first (legitimate). Then the **different**, still-open `abc` spawn genuinely stops.

**Command + output:**
```
--- Step 1: close corr=abcdef (legit) ---
$ printf '%s' '{"agent_id":"abcdef",...}' | PRAXIS_DISPATCH_LOG="$LOG" /bin/bash "$CLOSER"
--- log after step 1 ---
- [...] corr=abcdef | ... STATE: dispatched
- [...] corr=abc    | ... STATE: dispatched
- [2026-07-28T15:40:57Z] ... keyed close for corr=abcdef, matched 1 open row(s) ... STATE: closed

--- Step 2: the genuinely different spawn corr=abc stops ---
$ printf '%s' '{"agent_id":"abc",...}' | PRAXIS_DISPATCH_LOG="$LOG" /bin/bash "$CLOSER"
dispatch-log-close.sh: idempotent no-op: corr=abc already has a closing row
EXIT CODE: 0

--- log after step 2: UNCHANGED, no closing row for corr=abc was ever written ---
- [...] corr=abcdef | ... STATE: dispatched
- [...] corr=abc    | ... STATE: dispatched          <-- still open, forever
- [2026-07-28T15:40:57Z] ... keyed close for corr=abcdef ... STATE: closed
```
The diagnostic literally says `corr=abc already has a closing row` — this is false; only
`corr=abcdef` has one. Because `grep -F "corr=abcdef"` (the closing row's text) contains
`corr=abc` as a substring, **every future retry for `agent_id=abc` will hit this same
false idempotency short-circuit forever** — the `corr=abc` row is now permanently
unclosable by mechanism, silently.

**Verdict: BROKEN.** Falsifies claim (a) (this row can never reach a terminal state by
mechanism) and is the "over-dedupe silently drops a genuine second spawn" case the brief
asked to test for claim (e).

## Attack 9 — embedded newline in `agent_id` corrupts the writer's one-row-per-line schema, then defeats the closer's own matcher via multi-pattern injection

**Step 1 (writer):** feed `dispatch-log-writeahead.sh` an `agent_id` containing a literal
newline byte.
```
$ python3 -c "...json.dumps({'agent_id':'EVIL\nINJECTED', 'agent_type':'praxis-worker',
  'hook_event_name':'SubagentStart'})..." \
  | PRAXIS_DISPATCH_LOG="$LOG" CLAUDE_PROJECT_DIR=/Volumes/Sensidine/Praxis.build /bin/bash "$WRITER"
--- resulting log (od -c confirms a real embedded \n, not an escape) ---
# DISPATCH LOG
- [...] ... corr=EVIL
INJECTED | WHEN: spawn | HOW: awaiting terminal state | STATE: dispatched
```
One logical row is now split across 2 physical lines; `corr=EVIL` ends line 2, `INJECTED |
... STATE: dispatched` is line 3. `line count: 3` (header + 2 physical lines for 1 logical
row).

**Step 2 (closer, cross-row false match):** a **completely unrelated** real open row exists
whose text merely happens to contain the substring `INJECTED` (not as a `corr=` value at
all — just present in prose). A SubagentStop with the same hostile `agent_id` arrives.
```
--- log BEFORE ---
# DISPATCH LOG
- [...] corr=REALTOKEN-UNRELATED-SPAWN-INJECTED-INTO-LOG-BY-COINCIDENCE | ... STATE: dispatched

$ python3 -c "...json.dumps({'agent_id':'EVIL\nINJECTED', ...,'hook_event_name':'SubagentStop'})..." \
  | PRAXIS_DISPATCH_LOG="$LOG" /bin/bash "$CLOSER"
EXIT CODE: 0

--- log AFTER: falsely claims a close ---
- [...] corr=REALTOKEN-UNRELATED-SPAWN-INJECTED-INTO-LOG-BY-COINCIDENCE | ... STATE: dispatched
- [2026-07-28T15:40:32Z] WHO: praxis-worker | WHAT: subagent closed | WHY: hook-recorded at
  SubagentStop, keyed close for corr=EVIL
INJECTED, matched 1 open row(s) | WHERE: closes corr=EVIL
INJECTED | WHEN: stop | HOW: KEYED - matched via CORR_JQ token | STATE: closed
```
Root cause: `grep -F` given a pattern argument that itself contains an embedded newline
treats each line of the pattern as a **separate fixed string, OR'd together**. So
`grep -F "corr=EVIL\nINJECTED"` actually searches for `corr=EVIL` **or** `INJECTED`
independently. The unrelated row matched purely because its own (unrelated) text contained
`INJECTED` as a substring — the token never legitimately correlated to anything.

**Verdict: BROKEN.** Falsifies (b) in spirit (the row schema — one logical row, one physical
line — is corrupted by unsanitized input, even though no *existing* byte was rewritten) and
falsifies (d) hard (a real, different, still-open spawn is falsely claimed closed).

## Attack 10 — very long token: `/usr/bin/grep -F` errors with "out of memory," causing a false negative claim

**Hypothesis:** an extremely long correlation token could break the fixed-string grep calls.

**Isolated root-cause test (bypassing the script entirely, plain grep):**
```
$ for n in 100 500 1000 2000 3000 5000 8000; do
    TOKEN=$(python3 -c "print('T'*$n)")
    echo "corr=$TOKEN test" | /usr/bin/grep -F "corr=$TOKEN" 2>&1 | head -c60
  done
n=100  -> corr=TTT...  (matches)
n=500  -> corr=TTT...  (matches)
n=1000 -> corr=TTT...  (matches)
n=2000 -> corr=TTT...  (matches)
n=3000 -> corr=TTT...  (matches)
n=5000 -> corr=TTT...  (matches)
n=8000 -> grep: out of memory
```
The system `/usr/bin/grep -F` (BSD grep on this macOS/darwin box) fails outright somewhere
between 5,000 and 8,000 characters in the pattern argument, printing `grep: out of memory`
and producing **zero** matching lines (not a crash of the whole pipe — grep just emits
nothing, which the script's `wc -l` then counts as 0).

**End-to-end reproduction against the real closer, with a 10,000-char `agent_id` written by
the real writer and then closed by the real closer** (clean fixture, single writer call,
single closer call):
```
$ LONGTOK=$(python3 -c "print('T'*10000)")
$ ... writer ... # row written correctly, corr=T{10000} present verbatim
$ ... closer ...
--- result row 3 ---
- [...] WHO: praxis-worker | WHAT: subagent stop recorded, no open row matched | WHY:
  SubagentStop carried corr=TTT...T but no STATE: dispatched row in this log carries that
  token (already reconciled, writer patch not in effect for that spawn, or token mismatch) |
  ... STATE: closed@unmatched-token
```
**Independent check that the row actually IS present with that exact token** (run manually,
directly against the same file, right after the closer ran):
```
$ TOKEN=$(python3 -c "print('T'*10000)")
$ grep -E '\| STATE: dispatched$' "$LOG" | grep -F "corr=$TOKEN" | wc -l
       1
```
The row demonstrably **does** carry that exact token — verified independently — yet the
closer's own ledger entry states **"no STATE: dispatched row in this log carries that
token,"** which is factually false. Isolated in a minimal standalone script (no jq, no
surrounding logic) to rule out every other variable:
```
$ cat isolate.sh
#!/bin/bash
LOG="$1"; TOKEN="$2"
MATCHES=$(grep -E '\| STATE: dispatched$' "$LOG" | grep -F "corr=$TOKEN" | wc -l | tr -d ' ')
echo "MATCHES=$MATCHES"
$ /bin/bash isolate.sh "$LOG" "$TOKEN"
MATCHES=0
```
(same pipeline typed directly at the interactive tool-shell prompt returns `MATCHES=1` —
because that shell's `grep` is the profile-installed interactive wrapper function that
shells out to `ugrep`, not `/usr/bin/grep`; a script invoked via `/bin/bash script.sh`, which
is how both hooks actually run, does **not** inherit that function and hits real
`/usr/bin/grep`, which fails as shown above.)

**Verdict: BROKEN.** Real agent_id tokens observed this session are ~17-18 hex characters
(e.g. `a94480e6c527a38b2`), nowhere near this threshold, so this requires an anomalously long
token to trigger — flagged with that caveat, not overclaimed as a routine risk. But it is a
real, reproducible, measured failure mode of the shipped mechanism, not a hypothetical: the
closer writes a **specific, checkable, false statement** into the append-only ledger, and
because the same false "already closed"-style reasoning would recur identically on any retry
(the failure is deterministic on this grep for tokens ≥ ~8,000 chars), the row is permanently
orphaned. Directly falsifies claim (d), cascades into (a).

## Attack 11 — claim (a) against the real, current log: legacy corr-less rows can never be closed by mechanism

**Command + output (read-only query against the real file, no write):**
```
$ grep -cE '\| STATE: dispatched$' /Volumes/Sensidine/Praxis.build/DISPATCH_LOG.md
81
$ grep -E '\| STATE: dispatched$' /Volumes/Sensidine/Praxis.build/DISPATCH_LOG.md | grep -c 'corr='
1
```
80 of the 81 currently-open rows in the real ledger carry **no** `corr=` substring at all.

**Fixture proof that no token can ever close such a row** (a corr-less dispatched row,
byte-identical in shape to the 80 real ones, probed with several real-looking and arbitrary
tokens):
```
$ cat "$LOG"
# DISPATCH LOG
- [...] WHERE: session c1dec30 | WHEN: spawn | HOW: awaiting terminal state | STATE: dispatched
$ for tok in a94480e6c527a38b2 a1be8620d08256ca4 "" "anything"; do
    printf '%s' "{\"agent_id\":\"$tok\",...}" | PRAXIS_DISPATCH_LOG="$LOG" /bin/bash "$CLOSER" >/dev/null
  done
$ grep -cE '\| STATE: dispatched$' "$LOG"
1                     # the original row is STILL open; nothing ever touches it
```
This is not just a historical artifact of the 80 legacy rows: the writer's own comment
states `agent_id` is absent for "a main-thread `--agent` spawn," and the closer's UNKEYED
branch, by design, **never resolves a specific `STATE: dispatched` row** — it only appends a
generic `closed@unattributed` note elsewhere in the log. So any future dispatch opened
without an `agent_id` is, by the mechanism's own construction, in the same permanently-open
category as the 80 legacy rows today.

**Verdict: this is a real, provable limit on claim (a), stated plainly:** the pair does *not*
guarantee "every row opened by the writer reaches a terminal state by mechanism, with no
human sweep" — it only does so for the subset of rows that (i) get a `corr=` tag at all, and
(ii) whose token doesn't collide via substring with another token (Attacks 7-8), and (iii)
whose token is short enough for the system's `grep -F` (Attack 10). 80 of 81 real rows today
fall outside that subset and require the human sweep the DISPATCH_LOG's own session-37/38
entries already describe.

## Attack 12 — UNKEYED over-dedupe for two genuinely different, byte-identical stop payloads

**Hypothesis:** the brief asked specifically whether the pair can "over-dedupe so a genuine
second spawn is silently never closed." The script's own comments already disclose this as a
named, accepted limitation for the UNKEYED path — reproduced to confirm it is real, not just
theoretical.
```
--- two real open rows, both agent_type=praxis-worker, neither has an agent_id ---
$ PAYLOAD='{"agent_type":"praxis-worker","hook_event_name":"SubagentStop"}'
$ printf '%s' "$PAYLOAD" | PRAXIS_DISPATCH_LOG="$LOG" /bin/bash "$CLOSER"   # spawn #1 stops
$ printf '%s' "$PAYLOAD" | PRAXIS_DISPATCH_LOG="$LOG" /bin/bash "$CLOSER"   # spawn #2 stops (byte-identical payload)
dispatch-log-close.sh: idempotent no-op: key=3701351910-63 already has a closing row
--- log after both: exactly ONE closed@unattributed row for two distinct stop events ---
$ grep -c 'STATE: closed@unattributed' "$LOG"
1
```
**Verdict: CONFIRMED, but not counted as a hidden break** — the script's own comments (lines
~153-158) name this exact scenario and its consequence explicitly ("documented limitation,
not silently assumed away"). Confirmed real and reproducible; reported for completeness since
the brief asked for it directly, but distinguished from the undisclosed defects above.

## Attack 13 — does anything else in the repo parse `DISPATCH_LOG.md`'s row schema in a way the new row shapes would break?

**Command + output:**
```
$ grep -rn "DISPATCH_LOG" --include="*.sh" -l scripts .claude
scripts/dispatch-log-close.sh
scripts/dispatch-log-writeahead.sh
scripts/master-write-guard.sh
scripts/master-bash-guard.sh
scripts/tests/test-dispatch-log-close.sh
.claude/hooks/precompact-handoff.sh

$ grep -n "DISPATCH_LOG" scripts/master-write-guard.sh
14:  *DISPATCH_LOG.md|*DECISION_LOG.md|*ISSUE_REGISTER.md|*HANDOFF.md|*STATUS.md) exit 0 ;;
$ grep -n "DISPATCH_LOG" scripts/master-bash-guard.sh
14:    *DISPATCH_LOG.md*|*DECISION_LOG.md*|*ISSUE_REGISTER.md*|*HANDOFF.md*|*/specs/*|*/docs/reports/*) exit 0 ;;
$ grep -n "DISPATCH_LOG" .claude/hooks/precompact-handoff.sh
16:  (cd "$ROOT" && bd ready 2>/dev/null) || echo "(bd unavailable — check DISPATCH_LOG.md fallback)"
```
**Verdict: NO BREAK FOUND.** All three other references are path-string matches (guard
exemptions) or a plain-text fallback message — none parse row content, so `STATE:
closed@unmatched-token` / `closed@unattributed` cannot break any other consumer in this repo.

## Attack 14 — append-only, exit-0, and existing test suite baseline

**Command + output (shipped suite, unmodified):**
```
$ /bin/bash scripts/tests/test-dispatch-log-close.sh
=== TALLY: 13 passed, 0 failed (of 13 cases) ===
```
13/13 pass — none of these 13 cases cover the substring/prefix collision, the embedded
newline, or the long-token grep failure found above; the shipped suite does not exercise them.

**Append-only check across every attack above:** in every single command run in this report,
`diff`/`od -c` on the fixture before/after confirms pre-existing bytes were never rewritten —
only appended to, or (in the directory/read-only cases) not written at all. Claim (b)'s literal
wording ("never rewrites, edits, reorders or deletes an existing DISPATCH_LOG.md line")
**survives** every attack tried, including the ones that break (a)/(d)/(e) — the false claims
above are all made via new appended rows, never by editing history.

**Exit code across every attack above:** every single invocation in this report, including
the out-of-memory grep failure, the directory-as-log case, and the 50MB stdin case, returned
exit 0. Claim (c) **survived every attack tried.**

---

## Summary table

| # | Attack | Claim(s) targeted | Verdict |
|---|--------|-------------------|---------|
| 1 | log path is a directory | (c) | SURVIVED |
| 2 | read-only log file / read-only parent dir | (b)(c) | SURVIVED |
| 3 | 50MB stdin | (c) | SURVIVED |
| 4 | non-object JSON (`[]`,`"str"`,`null`,`123`,`true`,`{}`) | (c)(d) | SURVIVED (minor: `null` mislabeled reason=non-json-stdin) |
| 5 | 10,000-level nested JSON | (c) | SURVIVED |
| 6 | embedded NUL bytes | (c)(d) | SURVIVED |
| 7 | prefix/substring token collision → false closure of unrelated open row | (d) | **BROKEN** |
| 8 | prefix/substring collision in idempotency check → permanent silent orphan | (a)(e) | **BROKEN** |
| 9 | embedded newline in agent_id → schema split + multi-pattern false match on unrelated row | (b)(d) | **BROKEN** |
| 10 | very long token (~10,000 chars) → `grep -F` "out of memory" → false "no row matched" claim | (a)(d) | **BROKEN** |
| 11 | claim (a) vs. real log: 80/81 open rows carry no corr= tag, provably unclosable by mechanism | (a) | **BROKEN** (stated as a limit, not a crash) |
| 12 | UNKEYED over-dedupe on byte-identical distinct payloads | (e) | CONFIRMED, but disclosed by the script itself — not a hidden break |
| 13 | other DISPATCH_LOG.md parsers in repo | (b) collateral | NO BREAK FOUND |
| 14 | shipped test suite baseline + append-only/exit-0 across all attacks | (b)(c) | SURVIVED; suite doesn't cover 7/8/9/10/11 |

**Defect count: 4 undisclosed breaks (Attacks 7, 8, 9, 10), plus 1 disclosed/pre-existing
limitation on claim (a) confirmed against the real log (Attack 11), plus 1 cosmetic
mislabel (Attack 4/null) and 1 stderr-hygiene note (Attack 1).**

The single most serious finding is **Attack 7**: a hostile or merely coincidental
prefix-relationship between two real correlation tokens causes the closer to append a
ledger row that explicitly claims to have matched and closed a spawn that is, in fact, still
running — a directly false statement, in an append-only file that the rest of the system
(per DECISION_LOG/DISPATCH_LOG entries already in this repo) treats as ground truth precisely
because it cannot be rewritten. Attack 8 shows the same root cause (unanchored `grep -F`
substring matching on `corr=$TOKEN`) can also **silently and permanently drop** a real
spawn's closure. Attack 10 shows this is not confined to adversarial input shape — a
sufficiently long (but still plausible, e.g. a long hash or path used as a token) value hits
a real, measured `/usr/bin/grep` limitation on this machine and produces the same class of
false claim through an entirely different mechanism (grep OOM, not substring collision).

## What I did NOT test

- A true full/out-of-space filesystem (e.g., a filled ramdisk or quota-limited volume). I
  tested read-only-file and read-only-parent-directory as a proxy (both survived), but did
  not construct an actual ENOSPC condition. **UNVERIFIED.**
- Real concurrent/racing invocations of the closer (two SubagentStop hooks firing for
  different spawns at the exact same instant, testing for a read-modify-append race on the
  idempotency check). Not attempted — would require true parallel process launches with
  precise timing; flagged as untested, not claimed either way. **UNVERIFIED.**
- Whether Claude Code's actual hook runner enforces a timeout that the 50MB-stdin case (6.6s)
  or a much larger payload could exceed. I only measured wall-clock time of the script in
  isolation, not against any real hook timeout value. **UNVERIFIED.**
- The real shape of a live `SubagentStop` payload — per the closer's own header comment, this
  has never been captured; all payloads in this report are constructed based on the static
  string-table evidence the builder already documented. If the real field name differs from
  `agent_id`, correlation degrades to UNKEYED for every real spawn, which is a different
  (weaker but not false) failure mode than what Attacks 7-10 demonstrate. **UNVERIFIED
  either way — not re-derived in this session.**
- Windows/cygwin code paths in the writer/closer (irrelevant on this macOS box; not tested).
- jq versions other than 1.7.1-apple, and grep implementations other than the system
  `/usr/bin/grep` actually resolved here — the Attack 10 threshold (5,000-8,000 chars) is a
  property of *this machine's* BSD grep and is not claimed to generalize to GNU grep or other
  platforms.

## Files touched

No files under test were modified. All fixtures were created under
`/private/tmp/claude-501/.../scratchpad/dlc-adversarial/` via `mktemp -d`, with
`PRAXIS_DISPATCH_LOG` pointed at each fixture. Verification that the real ledger was never
written to by this session:
```
$ git diff --numstat -- DISPATCH_LOG.md
57  0  DISPATCH_LOG.md
```
This diff was already present in the working tree before this session started (it is part of
the pre-existing parked/staged change set listed in the initial `git status`, containing rows
timestamped 2026-07-26 through 2026-07-28T15:35:43Z — all real, hook-written content). Confirmed
none of this session's adversarial fixture strings (`TOKEN-CASE*`, `DUPTOKEN`, `abc`/`abcdef`,
`EVIL`/`INJECTED`, `attack-*`, `scratchpad`) appear anywhere in that diff:
```
$ git diff -- DISPATCH_LOG.md | grep -iE "TOKEN-CASE|DUPTOKEN|abcdef|EVIL|INJECTED|attack-|scratchpad"
clean: no adversarial fixture strings found in the real log's diff
```

No guard scripts, hook scripts, `.claude/settings.json`, `specs/SPEC_RUBRIC.md`, or ledger
files were edited. No `git add`/`commit`/`push`/`stash`/`checkout`/`reset` was run. Nothing
was written under `.claude/agent-memory/`.

## Result: FAIL (claims (a), (d) broken; (e) broken via a distinct mechanism from the
disclosed one; (b) and (c) survived every attack tried)
