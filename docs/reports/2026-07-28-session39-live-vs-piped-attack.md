# Session 39 — ADVERSARIAL: "real payload closes" — live firing vs. piped payload

**Task:** attack the claim that `scripts/dispatch-log-close.sh` has been demonstrated
to close `DISPATCH_LOG.md` write-ahead rows end-to-end.
**Mode:** ADVERSARIAL (grading only — nothing repaired, nothing staged).
**Criterion:** rubric S2 — *being exercised by a payload fed to a script's stdin is
not the same as being exercised live end-to-end by the runtime in production
configuration.* Standing ruling G-2 deferred guard remediation because "every exit
code came from piped payloads."
**Attacker agent id:** `a3ecab2253e3f547f` (praxis-worker, spawnDepth 2, spawned
2026-07-28T16:01:15Z). All times below are UTC. Host local clock is UTC−4, so
`ls`/`stat` local stamps such as `11:49` correspond to `15:49Z`.

---

## READ THIS FIRST — the answer changed at 16:08:24Z, mid-run

Q1–Q5 below were measured between 16:03Z and 16:06Z, when the real ledger contained
**zero** closer-written rows. At **16:08:24Z**, while I was writing this report, my
sibling worker `a20182ce1471dcfae` stopped and the **production-form** hook entry
fired and appended a genuine closing row to the **real** `DISPATCH_LOG.md`:

```
$ grep -n "corr=a20182ce1471dcfae" DISPATCH_LOG.md
119:- [2026-07-28T16:01:32Z] WHO: praxis-worker | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session c1dec30 corr=a20182ce1471dcfae | WHEN: spawn | HOW: awaiting terminal state | STATE: dispatched
120:- [2026-07-28T16:08:24Z] WHO: praxis-worker | WHAT: subagent closed | WHY: hook-recorded at SubagentStop, keyed close for corr=a20182ce1471dcfae, matched 1 open row(s) | WHERE: closes corr=a20182ce1471dcfae | WHEN: stop | HOW: KEYED - matched via CORR_JQ token | STATE: closed
```

Attribution, checked rather than assumed — **CONFIRMED-BY-OBSERVATION**:

- `.claude/settings.json` has **not** been touched since 15:52:27Z (mtime
  `2026-07-28T15:52:27Z`, md5 `65ce9d8a966e275549829bef3e714f3f`), so the entry that
  fired is the production one, with no environment prefix:
  ```
  $ jq -r '.hooks.SubagentStop[] | .matcher // "<no matcher>", (.hooks[].command)' .claude/settings.json
  ^praxis-manager$
  ./scripts/gate-manager-output.sh
  <no matcher>
  "$CLAUDE_PROJECT_DIR"/scripts/dispatch-log-close.sh
  ```
- `PRAXIS_DISPATCH_LOG` is still absent from CLI process 85132
  (`ps -wwEp 85132 | tr ' ' '\n' | grep -c 'PRAXIS_DISPATCH_LOG'` → `0`), so the target
  resolved to the real ledger by the Q2 default path.
- The sibling did not write it by hand: its **last tool call was 16:08:10.668Z** (a
  `shasum` verifying the ledger unchanged); its 16:08:24.108Z transcript entry is
  `assistant / text` with no `tool_use`; its transcript mtime is 16:08:24Z, the same
  second as the ledger mtime and the row's own timestamp.
- The closed row (119) was itself written by the live write-ahead hook at 16:01:32Z,
  and `corr=a20182ce1471dcfae` is that worker's real runtime `agent_id`.

**So the closer does now sit on the LIVE side of the G-2 line for the production
configuration.** Everything below stands as recorded; where it says "count 0" that was
true at measurement time and is now 1. What survives the update is in
"Where this actually sits relative to S2," which I rewrote after this event.

---

## Q1 — Has the closer EVER written a row into the real `/Volumes/Sensidine/Praxis.build/DISPATCH_LOG.md`?

**Answer as measured at 16:06Z: NO. Count of rows matching `WHAT: subagent closed` = 0.**
**SUPERSEDED at 16:08:24Z: the count is now 1 (see the update above).** At the moment
the claim under attack was authored (15:54:34Z) and at the moment I was briefed, it
was zero. **CONFIRMED-BY-OBSERVATION** in both directions.

```
$ grep -c "WHAT: subagent closed" DISPATCH_LOG.md
0
$ grep -n -E "WHAT: subagent (closed|stop recorded)" DISPATCH_LOG.md
(no output)
$ grep -c 'subagent closed' /Volumes/Sensidine/Praxis.build/DISPATCH_LOG.md
0
```

The closer emits exactly three row shapes (`dispatch-log-close.sh:160,167,197`):
`WHAT: subagent closed`, `WHAT: subagent stop recorded, no open row matched`, and
`WHAT: subagent stop recorded, correlation unavailable`. **None of the three appears
anywhere in the real ledger.** The only rows in the ledger carrying `STATE: closed`
are three hand-written reconciliation rows (lines 28, 105, 107), authored by humans /
the master, each of which explicitly says the closer does not exist. Two of them read
"writer/closer gap unrepaired."

Today's ledger rows are all write-ahead (`STATE: dispatched`), none closed:

```
114:- [2026-07-28T15:16:14Z] WHO: praxis-manager | ... | STATE: dispatched
115:- [2026-07-28T15:19:54Z] WHO: praxis-worker  | ... | STATE: dispatched
116:- [2026-07-28T15:35:43Z] WHO: praxis-worker  | ... corr=a94480e6c527a38b2 | STATE: dispatched
117:- [2026-07-28T15:57:09Z] WHO: praxis-manager | ... corr=a81988d393938a947 | STATE: dispatched
118:- [2026-07-28T16:01:15Z] WHO: praxis-worker  | ... corr=a3ecab2253e3f547f | STATE: dispatched
119:- [2026-07-28T16:01:32Z] WHO: praxis-worker  | ... corr=a20182ce1471dcfae | STATE: dispatched
```

The **writer** half (`dispatch-log-writeahead.sh`) *is* proven in production — rows
116–119 carry real `corr=` tokens written by the live hook into the real ledger. The
**closer** half has produced zero bytes of the real ledger, ever.

---

## Q2 — With no `PRAXIS_DISPATCH_LOG` set, which file does the closer target?

**Answer: the real ledger, `/Volumes/Sensidine/Praxis.build/DISPATCH_LOG.md`.**
**CONFIRMED-BY-OBSERVATION.**

`scripts/dispatch-log-close.sh:51`:

```sh
LOG="${PRAXIS_DISPATCH_LOG:-${CLAUDE_PROJECT_DIR:-.}/DISPATCH_LOG.md}"
```

The hook is launched by the CLI process, PID 85132, not by any shell of mine, so the
hook's environment is that process's environment plus whatever the runtime injects.
Checked directly:

```
$ ps -o lstart=,pid=,command= -p 85132
Tue 28 Jul 11:04:26 2026     85132 claude --dangerously-skip-permissions
$ ps -wwEp 85132 | tr ' ' '\n' | grep -c 'PRAXIS_DISPATCH_LOG'
0
```

`PRAXIS_DISPATCH_LOG` is **absent from the CLI process environment**, and the
`"env"` block of `.claude/settings.json` defines only `ORCH_N8N_WEBHOOK`,
`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`, `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`.
`CLAUDE_PROJECT_DIR` *is* injected into hook processes — proven from a real
runtime-launched hook, not inferred (`payloads/capture.log`):

```
########## EVENT=SubagentStop TS=2026-07-28T15:49:07Z PID=56161 ##########
--- PWD: /Volumes/Sensidine/Praxis.build
--- CLAUDE_PROJECT_DIR: /Volumes/Sensidine/Praxis.build
      CLAUDE_PID=85132
```

Resolution under exactly that environment:

```
$ env -u PRAXIS_DISPATCH_LOG CLAUDE_PROJECT_DIR=/Volumes/Sensidine/Praxis.build \
    bash -c 'echo "LOG=${PRAXIS_DISPATCH_LOG:-${CLAUDE_PROJECT_DIR:-.}/DISPATCH_LOG.md}"'
LOG=/Volumes/Sensidine/Praxis.build/DISPATCH_LOG.md
```

(The fallback arm is harmless too: hook `PWD` is the project dir, so `./DISPATCH_LOG.md`
is the same file.) So under the currently registered production entry the closer aims
at the real ledger — and per Q1 it has never landed a byte there.

To show the mechanism itself works against real ledger *content*, I exercised it
against a **copy**, feeding the real 15:49:07Z `SubagentStop` payload extracted from
`payloads/capture.log`:

```
$ jq -r '{agent_id, agent_type, hook_event_name}' atk39/stop-1549.json
{ "agent_id": "a94480e6c527a38b2", "agent_type": "praxis-worker",
  "hook_event_name": "SubagentStop" }
$ cp DISPATCH_LOG.md atk39/COPY_DISPATCH_LOG.md
$ PRAXIS_DISPATCH_LOG=atk39/COPY_DISPATCH_LOG.md scripts/dispatch-log-close.sh < atk39/stop-1549.json
CLOSER_EXIT=0
$ diff DISPATCH_LOG.md atk39/COPY_DISPATCH_LOG.md
119a120
> - [2026-07-28T16:06:01Z] WHO: praxis-worker | WHAT: subagent closed | WHY: hook-recorded at SubagentStop, keyed close for corr=a94480e6c527a38b2, matched 1 open row(s) | WHERE: closes corr=a94480e6c527a38b2 | WHEN: stop | HOW: KEYED - matched via CORR_JQ token | STATE: closed
--- real ledger md5 before/after (must match):
6addf5aa525669e8cecb7c0c9623318d
6addf5aa525669e8cecb7c0c9623318d
```

Real ledger byte-identical before and after. That line is what the ledger *would*
have gained — and it is a **piped-payload** result, precisely the G-2 category.

---

## Q3 — Was the "live end-to-end" firing aimed at the real ledger or at a redirected target?

**Answer: REDIRECTED. The runtime genuinely fired the closer, but the registration in
force at 15:49:07Z carried an environment prefix pointing at a scratchpad fixture.**
**CONFIRMED-BY-OBSERVATION.**

The exact registration, recovered from the manager's own transcript
(`subagents/agent-a4914f6c17c4355f4.jsonl`, `Edit` at `2026-07-28T15:34:24.879Z`):

```json
{ "hooks": [ { "type": "command",
  "command": "PRAXIS_DISPATCH_LOG=/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/ffb8751c-a29c-4fce-8d11-3542454a16e2/scratchpad/live-fixture/DISPATCH_LOG.md \"$CLAUDE_PROJECT_DIR\"/scripts/dispatch-log-close.sh" } ] }
```

That entry was live from 15:34:24Z until 15:52:27Z, when it was replaced by the
production form now in `.claude/settings.json` (`git diff HEAD`):

```
+      {
+        "hooks": [
+          {
+            "type": "command",
+            "command": "\"$CLAUDE_PROJECT_DIR\"/scripts/dispatch-log-close.sh",
+            "timeout": 30
+          }
+        ]
+      }
```

The close therefore landed in the fixture, not the ledger:

```
$ cat live-fixture/DISPATCH_LOG.md
# DISPATCH LOG
- [2026-07-28T15:35:43Z] ... corr=a94480e6c527a38b2 | ... | STATE: dispatched
- [2026-07-28T15:49:07Z] WHO: praxis-worker | WHAT: subagent closed | ... keyed close for corr=a94480e6c527a38b2, matched 1 open row(s) | ... | STATE: closed
$ cat live-fixture/DISPATCH_LOG.md.synclog
15:35:45Z MIRRORED corr=a94480e6c527a38b2
15:49:07Z CLOSE OBSERVED - loop exiting
```

**Can `sync-loop.sh` itself have written the closing row? NO — ruled out on two
independent grounds.** CONFIRMED-BY-OBSERVATION. Its only write to the fixture is
line 12, and it is fed exclusively by line 15's filter:

```sh
15:  done < <(grep -E 'STATE: dispatched$' "$REAL" 2>/dev/null | grep 'corr=')
12:      printf '%s\n' "$line" >> "$FIX"
16:  if grep -q 'WHAT: subagent closed' "$FIX" 2>/dev/null; then
17:    echo "$(date -u +%H:%M:%SZ) CLOSE OBSERVED - loop exiting" >> "$FIX.synclog"
```

(a) It can only copy lines ending in `STATE: dispatched`; the closing row ends in
`STATE: closed`. (b) It can only copy lines that exist in the REAL log, and the real
log contains zero `subagent closed` strings (Q1). Its close-detection branch at
line 16 writes to `$FIX.synclog` only — it is a *detector*, not a writer. Its mirror
filter over the real log yields spawn rows only:

```
$ grep -E 'STATE: dispatched$' DISPATCH_LOG.md | grep 'corr='
- [2026-07-28T15:35:43Z] ... corr=a94480e6c527a38b2 ... STATE: dispatched
- [2026-07-28T15:57:09Z] ... corr=a81988d393938a947 ... STATE: dispatched
- [2026-07-28T16:01:15Z] ... corr=a3ecab2253e3f547f ... STATE: dispatched
- [2026-07-28T16:01:32Z] ... corr=a20182ce1471dcfae ... STATE: dispatched
```

So the fixture's *open* row is a mirrored copy of a genuine hook-written ledger row,
and the fixture's *closing* row was written by the closer itself. What was NOT the
real ledger is the file the close landed in.

---

## Q4 — Is a hook added to `.claude/settings.json` mid-session live in the already-running CLI process?

**Answer, in two parts, both CONFIRMED-BY-OBSERVATION:**

**(a) YES for subagents spawned AFTER the edit — no restart required.**
CLI process 85132 started **15:04:26Z**:

```
$ TZ=UTC ps -o lstart= -p 85132
Tue 28 Jul 15:04:26 2026
```

`capture-hook.sh` did not exist at that moment — it was created at **15:18:43Z** (14
minutes after process start) at a path containing this session's UUID, so no settings
file could have referenced it before this session began. It was registered by an
`Edit` at **15:18:54.705Z** (SubagentStart + SubagentStop capture entries, recovered
verbatim from the manager transcript). It then fired, in that same process:

```
########## EVENT=SubagentStart TS=2026-07-28T15:19:54Z PID=7208  ##########   CLAUDE_PID=85132
########## EVENT=SubagentStop  TS=2026-07-28T15:30:23Z PID=22504 ##########   CLAUDE_PID=85132
########## EVENT=SubagentStart TS=2026-07-28T15:35:43Z PID=30815 ##########   CLAUDE_PID=85132
########## EVENT=SubagentStop  TS=2026-07-28T15:49:07Z PID=56161 ##########   CLAUDE_PID=85132
```

Each of these is runtime-launched, not shell-launched: `CLAUDE_PROJECT_DIR` is set and
the hook PID differs from `CLAUDE_PID=85132`. (The 15:18:44Z `SELFTEST` entry has
`CLAUDE_PROJECT_DIR: <UNSET>` — that is the manual control, and the contrast is what
makes the other four provably runtime-launched.) `.claude/settings.json` is the only
settings source modified today; `~/.claude/settings.json` (2026-07-27T18:34Z) and
`.claude/settings.local.json` (2026-07-26T17:31Z) are stale and contain no `"hooks"`
key at all (`grep -c '"hooks"'` = 0 for both). **Mid-session registration is live.**

**(b) NO, it is not retroactive to a subagent already in flight.** New finding, not in
the closer report. Timeline:

```
15:16:14.666Z  master spawns manager a4914f6c17c4355f4 (praxis-manager)
15:52:27.361Z  manager Edit registers the PRODUCTION closer entry (no env prefix)
15:52:27Z      .claude/settings.json mtime (last write; content = production form)
15:54:34.775Z  master receives <task-notification> a4914f6c17c4355f4 → that manager STOPPED
16:01:32Z      DISPATCH_LOG.md mtime (last write = the 16:01:32Z write-ahead row)
```

Between 15:52:27Z and now, **exactly one SubagentStop occurred** — manager a4914's, at
15:54:34.775Z — and the real ledger gained **no closing row of any shape** (Q1, count 0;
ledger goes straight from row 116 @15:35:43Z to row 117 @15:57:09Z). The closer would
have appended even on a total failure to correlate: the UNKEYED branch (line 197) is
unconditional and the log is writable (`master-write-guard.sh` explicitly allows
`DISPATCH_LOG.md`). The closer report itself staked a falsifiable prediction on this:

> "**Predicted, not observed:** when I return, the now-registered closer should fire on
> my own `SubagentStop` and append one `closed@unmatched-token` row to the real
> `DISPATCH_LOG.md` … That is a falsifiable prediction the master can check."

**That prediction is falsified.** No row appeared.

**Model consistent with all four observations (INFERRED, n=4):** hook configuration is
resolved per subagent at *spawn* time. Every firing observed today belongs to a
subagent spawned after its hook was registered (a1be86 spawned 15:19:54 > 15:18:54;
a94480 spawned 15:35:43 > 15:34:24); the single non-firing belongs to a subagent
spawned at 15:16:14, before its hook existed at 15:52:27. A *continuous*-reload model
is **ruled out** by the 15:54:34Z non-firing. Whether the production entry fires at all
for a post-15:52:27Z spawn remains **unobserved** — I am such a spawn (16:01:15Z), so
the master can settle it by running, after I return:
`grep -c "WHAT: subagent" /Volumes/Sensidine/Praxis.build/DISPATCH_LOG.md`.
I explicitly do **not** claim that result; it has not happened yet.

---

## Q5 — Could the 15:49:07Z close have been produced by something other than the runtime firing the hook?

Enumerated and dispositioned:

| # | Alternative | Disposition |
|---|---|---|
| 1 | `sync-loop.sh` mirrored it | **RULED OUT** — CONFIRMED. Filter takes only `STATE: dispatched$` lines that exist in the real log; the real log has zero `subagent closed` lines. |
| 2 | The manager hand-piped a payload into the closer at that moment | **RULED OUT** — CONFIRMED. The manager made **no tool call between 15:41:19.537Z and 15:49:40.546Z** (blocked awaiting worker 2). The close row and the fixture mtime are both 15:49:07Z, inside that idle window. |
| 3 | Worker `a94480e6c527a38b2` wrote the fixture row itself | **RULED OUT** — CONFIRMED. `grep -c 'live-fixture' agent-a94480e6c527a38b2.jsonl` = **0**; the string never appears in its transcript, and no tool_use of its targets that path. |
| 4 | Row hand-authored into the fixture afterwards | **RULED OUT** — CONFIRMED for the only two actors alive at 15:49:07Z, by #2 and #3. The independent `sync-loop.sh` poller, running on its own 2s clock, recorded `15:49:07Z CLOSE OBSERVED`, corroborating that the row materialised at that instant. |
| 5 | Runtime fired the registered `SubagentStop` hook | **RULED IN** — CONFIRMED. Registration recovered verbatim (Q3); the runtime's own capture hook logged `EVENT=SubagentStop TS=2026-07-28T15:49:07Z PID=56161`; the worker's transcript mtime is 15:49:07Z; the fixture mtime is 15:49:07Z; the row's `corr=a94480e6c527a38b2` is that worker's real `agent_id`, and its `agent_type` field was populated from the runtime payload. |

**The transport was genuinely live.** The process was launched by the runtime, stdin
came from the runtime, and the correlation token was a real per-spawn `agent_id` that
no human typed. On the G-2 axis — "every exit code came from piped payloads" — this
closer sits on the **live** side for payload provenance. That part of the claim is
real and should not be discounted.

---

## Where this actually sits relative to S2 (rewritten after the 16:08:24Z event)

1. **NOW PROVEN LIVE, END-TO-END, IN PRODUCTION CONFIGURATION.** At 16:08:24Z the
   unmodified production entry closed a real write-ahead row in the real ledger. The
   capability the claim asserts is real. I am not discounting it.
2. **BUT THE CITED EVIDENCE NEVER SHOWED IT.** Every close performed before 16:08:24Z
   landed in a scratchpad fixture under an `PRAXIS_DISPATCH_LOG=` prefix. At the time
   the claim was written (15:54:34Z) the ledger had zero closer-written rows and the
   production string had never fired. The claim was, on its own evidence, a claim about
   a redirected artifact — the S2 distinction exactly. It came true 14 minutes later by
   an event nobody staged as a test, and only because I re-checked the ledger instead
   of trusting my own 16:06Z measurement. Had I stopped at 16:06Z I would have graded
   it FALSE on evidence that was already stale.
3. **THE SCOPE IS NARROWER THAN THE CLAIM.** The closer closes rows for subagents
   spawned *after* its registration. It does **not** close rows for subagents in flight
   when it was registered: manager `a4914f6c17c4355f4` stopped at 15:54:34.775Z, two
   minutes after registration, and produced nothing — falsifying the closer report's own
   written prediction. Ledger rows **114 (15:16:14Z), 115 (15:19:54Z), 116 (15:35:43Z)
   and 117 (15:57:09Z) are permanently unclosable by this mechanism**; 116 in
   particular belongs to a spawn that *did* stop, and whose close was diverted into the
   fixture. So "closes `DISPATCH_LOG.md` write-ahead rows" is true prospectively and
   false for every row now open. Four orphan rows are exactly the S12 condition this
   unit exists to end, and they will still be there at session close.

The verdict token is OVERSTATED rather than HOLDS for two reasons, and neither is that
the mechanism does not work — it demonstrably does. First, the claim's *warrant* was a
fixture run; the demonstration that vindicates it is not the demonstration it cites,
and G-2 exists precisely to stop a project from banking a claim whose warrant is one
env var away from the real thing. Second, the claim as phrased covers write-ahead rows
generally, and the mechanism provably does not reach in-flight or pre-existing ones —
a limit discovered here by a falsified prediction, not disclosed in the claim.

The closer's own report is honest in its limitations section ("the *exact* production
string has not itself been observed firing"). The overstatement lives in the summary
phrasing "real payload closes," which a reader takes as "the ledger closes."

Nothing was repaired. Nothing was staged. **I did not modify the real
`DISPATCH_LOG.md`** — md5 `6addf5aa525669e8cecb7c0c9623318d` was verified identical
before and after my only exercise of the closer (which ran against a copy under
`PRAXIS_DISPATCH_LOG`). The subsequent change to `f6c16f5e1e12e72d92699d26695a6a9c`
is the 16:08:24Z hook-written row, attributed above.

## Files staged

None. `git add` / `git commit` / `git stash` were never run. The only file this unit
created inside the repo is this report; all experiment artifacts are under
`/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/ffb8751c-a29c-4fce-8d11-3542454a16e2/scratchpad/atk39/`.

Verdict: CLAIM OVERSTATED
