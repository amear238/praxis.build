# Session 39 — DISPATCH_LOG closer build (Praxis_build-43n)

## Task
Build the `SubagentStop`-side counterpart to `scripts/dispatch-log-writeahead.sh`
so that write-ahead rows stop accumulating forever at `STATE: dispatched`. Build
it parameterized over an unconfirmed correlation key (KEYED / UNKEYED modes),
apply the minimal writer patch needed for KEYED correlation, and write a
self-contained test harness. Worker 1 of MAX-2 on this bead.

## Mode
BUILD

## Criterion
S12 — "A ledger writer ships with its closing or flushing counterpart in the
same change." (`specs/SPEC_RUBRIC.md` line 118, violation 1 named at lines
206-219.)

## Process log

1. Read `scripts/dispatch-log-writeahead.sh`, `DISPATCH_LOG.md` (header +
   tail), `.claude/settings.json` (read-only — confirmed the live hook wiring
   without editing it), and the S12 rubric text.
2. **Live capture, this session only, CONFIRMED (not static):** my own
   scratchpad directory (`/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/ffb8751c-a29c-4fce-8d11-3542454a16e2/scratchpad/payloads/capture.log`)
   already contained a real `SubagentStart` payload, captured by an
   out-of-band hook registered in `.claude/settings.json` that is not part of
   this deliverable and that I did not create or edit. It is the actual
   payload for the spawn that is running this build:
   ```
   {"session_id":"ffb8751c-a29c-4fce-8d11-3542454a16e2","transcript_path":"/Users/admin/.claude/projects/-Volumes-Sensidine-Praxis-build/ffb8751c-a29c-4fce-8d11-3542454a16e2.jsonl","cwd":"/Volumes/Sensidine/Praxis.build","prompt_id":"6092498c-688f-4146-8a4d-4111055fb7f4","agent_id":"a1be8620d08256ca4","agent_type":"praxis-worker","hook_event_name":"SubagentStart"}
   ```
   This CONFIRMS `agent_id` is a real field on `SubagentStart` for this build
   (2.1.220), and that it looks like a per-spawn hex token. It says **nothing**
   about `SubagentStop` — that event had not fired inside this run at the time
   I read the file (it fires when I conclude, which is causally after I can
   observe it), so no real `SubagentStop` payload was available to me at any
   point in this session. The brief's "you will not have it" held for Stop;
   it did not hold for Start, and I am reporting exactly what I saw, not what
   I expected to see.
3. **Static read, UNCONFIRMED:** ran `strings` on the installed binary at
   `/Users/admin/.local/share/claude/versions/2.1.220` (confirmed present,
   256,908,272 bytes, single Mach-O, not a directory). Found hook-schema doc
   text: *"Right before a subagent (Agent tool call) concludes its response"
   [SubagentStop] ... "Input to command is JSON with agent_id, agent_type,
   and agent_transcript_path"*, and a field description: *"Subagent
   identifier. Present only when the hook fires from within a subagent ...
   Use this field (not agent_type) to distinguish subagent calls from
   main-thread calls."* This is a string-table doc comment, not a captured
   runtime payload, and it is labeled STATIC READ, UNCONFIRMED throughout the
   code comments and this report. It corroborates (2) but does not confirm it.
4. Checked `scripts/master-write-guard.sh`, `scripts/master-bash-guard.sh`,
   `scripts/no-commit-guard.sh` — all gate on `agent_type == praxis-master`
   with empty `agent_id`; as `praxis-worker` with a present `agent_id` I pass
   through every one of them unaffected. Did not edit any guard.
5. Wrote `scripts/dispatch-log-close.sh` (closer), patched
   `scripts/dispatch-log-writeahead.sh` (writer, minimal addition only), and
   `scripts/tests/test-dispatch-log-close.sh` (harness, 13 cases).
6. Ran `bash -n` on all three files (syntax check), ran the writer patch
   manually against a `mktemp -d` fixture via `CLAUDE_PROJECT_DIR` override
   (never the real log), then ran the full test harness twice (once to catch
   a harness bug, once clean).
7. Verified `git diff --stat -- DISPATCH_LOG.md` before and after — no
   content changes attributable to my work (see Verification evidence).

## Design decisions

**CORR_JQ.** A single placeholder line in the closer:
```sh
CORR_JQ='.agent_id // empty'
```
Marked UNBOUND in a block comment that states exactly what is confirmed
(item 2 above, THIS session only, SubagentStart only) vs. what is static/
unconfirmed (item 3, SubagentStop). It is the best-available guess, not a
claim. Nothing downstream assumes it resolves to anything real — the
UNKEYED path is fully implemented and independently tested.

**KEYED vs UNKEYED, selected automatically at runtime.** If `jq` can parse
the stdin as JSON and `$CORR_JQ` yields a non-empty string, the run is
KEYED. Otherwise (jq missing, empty stdin, non-JSON stdin, or the field
resolves empty) it is UNKEYED. No flag, no config — purely a function of
what actually showed up on stdin.

**KEYED close behavior.** Count every `STATE: dispatched` row in the log
containing the exact token (`grep -F`, fixed string, no regex surprises).
- 0 matches: append a `STATE: closed@unmatched-token` row. It makes no claim
  about which row this was — because there is no row.
- N≥1 matches: append **one** `STATE: closed` row stating `matched N open
  row(s)`. It never singles out one of several as "the" one that ended,
  because a duplicate write-ahead row for the same token still describes the
  one spawn that token names — closing all of them and saying so is a count,
  not a guess about which one "really" finished.

**UNKEYED close behavior (the conservative fallback the brief asked me to
justify).** Append a `STATE: closed@unattributed` row that:
- records that a stop event happened,
- records why no token was usable (`reason=jq-missing` /
  `empty-stdin` / `non-json-stdin` / `token-absent`),
- explicitly claims no specific open row as closed (`WHERE: n/a - no row is
  claimed closed`).
It never guesses. The tradeoff, stated plainly: an UNKEYED close does not
resolve any `STATE: dispatched` row — those rows stay open exactly as they
were, because there is no honest way to close them without a correlating
token. That gap is the pre-existing one named in the S12 violation text
(the reason 29+ rows were only ever cleared by a hand sweep); this build does
not close that gap for the token-less case, and does not claim to. It closes
it fully for the case the writer patch below makes possible.

**Idempotency.** Stateless, log-based, no side files:
- KEYED: before appending, grep for an existing `STATE: closed` row already
  containing `corr=<token>` (covers both the matched and unmatched-token
  outcomes for that token — either way it's already dispositioned once).
- UNKEYED: hash the raw stdin bytes with `cksum` (portable, always present,
  no security requirement here) and grep for an existing closed row
  containing that `key=<hash>`. Documented limitation: two genuinely
  different UNKEYED stop events with byte-identical payloads would be
  treated as the same event and only the first recorded. Not observed to be
  possible given `agent_transcript_path`/timestamps typically vary, but not
  provably impossible, so it is disclosed here rather than assumed away.

**Always exit 0.** The script never calls `exit` except the single line at
the very end. Every branch (jq missing, bad JSON, missing log, no matches,
idempotent no-op) falls through to it. `diag()` writes to stderr only and
never changes control flow.

**Append-only.** Every write path in the script is `>>`. Grep, `dirname`,
`mkdir -p` for the parent directory, and jq are the only other operations
against the filesystem/log; none of them can rewrite an existing line.
Verified directly in test 6b (an existing row's exact bytes are still
present, byte for byte, after a close event that did not match it).

**S12 applied recursively to this closer.** Every row the closer appends
carries a `STATE` that is *itself* terminal: `closed`, `closed@unmatched-token`,
`closed@unattributed`. None of them reads "awaiting" anything, so none of
them creates a new obligation for a third mechanism to discharge. The
UNKEYED path's honest limitation (dispatched rows it cannot close stay open)
is not a new debt this closer created — it is the same, already-named,
pre-existing gap, now bounded and disclosed rather than silently swept by
hand. Nothing produced by this script is itself awaiting a terminal state.

## The minimal writer change, and why the closer cannot work without it

`scripts/dispatch-log-writeahead.sh` originally recorded nothing that
correlates a `SubagentStart` row to any future `SubagentStop` event — the row
has no per-spawn identifier at all, only `WHO` (agent type, not unique) and a
session-wide git SHA (shared by every spawn in the session). Without a token
written at spawn time, KEYED close is mathematically impossible: there is
nothing in any open row for a later `SubagentStop` payload's token to match
against, no matter how good `CORR_JQ` is. The patch adds exactly one thing:
```sh
CORR=$(echo "$INPUT" | jq -r '.agent_id // empty' 2>/dev/null)
...
[ -n "$CORR" ] && WHERE="$WHERE corr=$CORR"
```
appended to the existing `WHERE` field (no new `|`-delimited column, so the
documented 7-field schema in the `DISPATCH_LOG.md` header is unchanged and
every existing row still parses the same way). When `agent_id` is absent
(e.g. a main-thread `--agent` spawn) the row is byte-for-byte the old format.
Verified manually against a `mktemp -d` fixture (see evidence below) — never
against the real log.

## Verification evidence

Syntax check on all three files:
```
$ bash -n scripts/dispatch-log-close.sh && echo "SYNTAX OK"
SYNTAX OK
$ bash -n scripts/dispatch-log-writeahead.sh && echo "SYNTAX OK"
SYNTAX OK
$ bash -n scripts/tests/test-dispatch-log-close.sh && echo "SYNTAX OK"
SYNTAX OK
```

Manual writer-patch verification, against a `mktemp -d` fixture, never the
real log:
```
$ TMPD=$(mktemp -d)
$ echo '{"session_id":"s1","agent_type":"praxis-worker","agent_id":"a1be8620d08256ca4","hook_event_name":"SubagentStart"}' | CLAUDE_PROJECT_DIR="$TMPD" bash scripts/dispatch-log-writeahead.sh
$ cat "$TMPD/DISPATCH_LOG.md"
# DISPATCH LOG
- [2026-07-28T15:26:09Z] WHO: praxis-worker | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session no-git corr=a1be8620d08256ca4 | WHEN: spawn | HOW: awaiting terminal state | STATE: dispatched
$ echo '{"agent_type":"praxis-master","hook_event_name":"SubagentStart"}' | CLAUDE_PROJECT_DIR="$TMPD" bash scripts/dispatch-log-writeahead.sh
$ cat "$TMPD/DISPATCH_LOG.md"
# DISPATCH LOG
- [2026-07-28T15:26:09Z] WHO: praxis-worker | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session no-git corr=a1be8620d08256ca4 | WHEN: spawn | HOW: awaiting terminal state | STATE: dispatched
- [2026-07-28T15:26:09Z] WHO: praxis-master | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session no-git | WHEN: spawn | HOW: awaiting terminal state | STATE: dispatched
```
Confirms both branches: `corr=` present with `agent_id`, absent (old format)
without it.

Full test harness run (final, clean):
```
$ /opt/homebrew/bin/bash scripts/tests/test-dispatch-log-close.sh
=== test-dispatch-log-close.sh ===
CLOSER: /Volumes/Sensidine/Praxis.build/scripts/dispatch-log-close.sh

PASS - 1 clean KEYED close appends exactly one closed row
PASS - 1b KEYED close is idempotent (second run adds no row)
PASS - 2 UNKEYED stop (no agent_id) closes with closed@unattributed, claims no specific row
PASS - 2b UNKEYED close is idempotent for byte-identical repeat stdin
PASS - 3 missing log file: created, exit 0, honest unattributed close appended
PASS - 4 zero open rows + KEYED token: honest unmatched-token close, no false claim
PASS - 5 malformed/truncated row present: script does not crash, still matches the one real open row
PASS - 6 token present, matches no open row: honest miss, open row for SOME-OTHER-TOKEN left untouched
PASS - 6b original open row is untouched (append-only honoured)
PASS - 7 multiple open rows same token: one closing row, honestly states matched=2 (no per-row guess)
PASS - 8 jq absent from PATH: falls back to UNKEYED reason=jq-missing, exit 0, no crash
PASS - 9 empty stdin: exit 0, recorded as UNKEYED reason=empty-stdin
PASS - 10 non-JSON stdin: exit 0, recorded as UNKEYED reason=non-json-stdin

=== TALLY: 13 passed, 0 failed (of 13 cases) ===
```
(Note: an earlier run of this same suite failed case 6b on a harness bug —
`grep -qF` was passed a pattern starting with `-`, which `grep` parsed as an
option and errored. Fixed by passing the pattern via a variable with `grep
-F -- "$pattern"`. Pasting this because S1 asks for real output, including
the one failure I hit and fixed, not just the final green run.)

Confirmation the real ledger was never touched by this build:
```
$ git diff --stat -- DISPATCH_LOG.md
 DISPATCH_LOG.md | 56 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 56 insertions(+)
$ git diff --numstat -- DISPATCH_LOG.md
56      0       DISPATCH_LOG.md
$ git diff -- DISPATCH_LOG.md | grep "^+" | grep -v "^+++" | wc -l
      56
$ git diff -- DISPATCH_LOG.md | grep -E "TOKEN-CASE|corr=|closed@" | head -20
(no output)
```
56 insertions, unchanged across the whole session (I checked this three
times, at the start, mid-session, and here at the end — an earlier
intermediate check of mine used `grep -c "^+"` without excluding the diff's
own `+++` header line, which miscounted 57; the `--numstat` and
header-excluded counts above are the correct ones and agree at 56). The
`- [2026-07-28T15:19:54Z] WHO: praxis-worker | ... | STATE: dispatched` row
— the real write-ahead row the platform's own (pre-existing, out-of-scope)
`SubagentStart` hook wrote for this very spawn — was already present among
those 56 lines before my first tool call in this session, since hooks fire
at spawn time before an agent's own actions begin. It carries no `corr=`
because it was written by the unpatched writer. No test fixture content, no
`corr=`, no `closed@` string from my work appears anywhere in the diff.

Confirmed nothing was staged and no forbidden file was touched:
```
$ git status --short -- scripts/dispatch-log-close.sh scripts/tests/test-dispatch-log-close.sh scripts/dispatch-log-writeahead.sh
 M scripts/dispatch-log-writeahead.sh
?? scripts/dispatch-log-close.sh
?? scripts/tests/test-dispatch-log-close.sh
$ git diff --cached --stat
 .../2026-07-26-session36-adversarial-actor-hunt.md | 226 ++++++++++++
 .../2026-07-26-session36-agent-key-audit.md        | 385 +++++++++++++++++++++
 docs/reports/2026-07-26-session36-agent-key-lab.md | 287 +++++++++++++++
 .../2026-07-26-session36-agent-key-s9-control.md   | 219 ++++++++++++
 docs/reports/2026-07-26-session36-null-attack.md   | 328 ++++++++++++++++++
 .../2026-07-26-session36-worker-trigger-probe.md   | 131 +++++++
 6 files changed, 1576 insertions(+)
```
The staged index is exactly the pre-existing 6-file / 1,576-insertion parked
commit named in the brief — unchanged by this work.

## Files staged
None. Everything is unstaged in the working tree, per hard limits:
- `scripts/dispatch-log-close.sh` (new, `+x`)
- `scripts/tests/test-dispatch-log-close.sh` (new, `+x`)
- `scripts/dispatch-log-writeahead.sh` (modified — minimal `corr=` addition)
- This report (new)

## What I did NOT verify

- **A real `SubagentStop` payload.** Never observed one, from any source,
  at any point in this session. `CORR_JQ`'s correctness against the real
  event is UNVERIFIED. This is the single largest open risk in this build
  and is exactly why the script is architected to degrade to UNKEYED rather
  than assume KEYED will fire.
- **Whether `agent_id` is stable/unique per spawn across retries or
  compaction.** Only one live value was ever observed
  (`a1be8620d08256ca4`, this session, this spawn). Uniqueness across a whole
  session, and whether it is ever reused, is UNVERIFIED.
- **End-to-end wiring.** I did not register `dispatch-log-close.sh` on the
  `SubagentStop` hook in `.claude/settings.json` — that file is explicitly
  off-limits to me this session (owned by a parallel capture experiment).
  So this closer has not been exercised by a real `SubagentStop` firing in
  this repo; it has only been exercised by the test harness and by manual
  fixture runs. Wiring it up is a separate, follow-up step for whoever owns
  `.claude/settings.json` next.
- **Behavior when the log file's parent directory itself is unwritable**
  (permission denied). Not in the required failure-mode list; not tested.
  Reasoned only: since the script never uses `set -e` and never treats a
  failed `>>` as fatal, it should still reach `exit 0`, but I did not trip
  this deliberately, so I am not claiming it as tested.
- **Behavior under concurrent/parallel invocation** (two `SubagentStop`
  events for different tokens racing to append at the same instant). Not
  tested; `>>` is append-mode but I did not verify atomicity under real
  concurrent writers.
- I did not run the pre-existing `scripts/test-gate-hardening.sh` or any
  other repo test suite — out of scope for this unit, not touched, not
  claimed.

## Result: PASS
