# `Praxis_build-c2t` — guard localisation by live control

**Session 45 · 2026-08-08 · Claude Code 2.1.226 · author: praxis-master · UNGRADED**

Written to satisfy session-45 ruling 3 ("the evidence goes on the record first … Show,
then fix"). No fix is built here. Nothing in this file is an auditor verdict.

---

## 1. Why this report exists, and the correction it opens with

The session-45 directive asserted the `c2t` defect lives in "the commit-gate script." My
Step 1 halt report asserted it lives at `scripts/master-bash-guard.sh:12`. **Both were
assertions about a file. Ruling 3 correctly refused to trade one unobserved claim for
another.**

Two further corrections to my own earlier record, made before the evidence rather than
after it:

1. **I did not observe three blocks.** I observed **one** — `2>/dev/null`, incidental to a
   directory listing. The "three blocks" figure is session 42's, carried in `HANDOFF.md`.
2. **`DECISION_LOG` row `2026-08-08T00:05:00Z` says the regex "catches `>=`". That was a
   static read of a regex, not an observation.** Session 42's `>=` block was recorded on
   binary **2.1.223**; this session logged the binary as **2.1.226**, which under this
   project's own standing rule makes the carried observation UNVERIFIED. The row is
   corrected by append in `DECISION_LOG`, not edited.

## 2. The control — three payloads, two axes isolated

Minimal pairs. Each was a real `Bash` tool call in this session; results are the harness's,
pasted, not described.

**Control C — non-exempt path, no `>` anywhere.** Isolates the filename as innocent.

```
awk 'NR!=0{c++} END{print "control-C lines:", c}' STATUS.md
→ ALLOWED.  stdout: control-C lines: 213
```

**Control B — `>=` present, but path is on the guard's exemption list.** Isolates the
exemption as the thing that rescues it.

```
awk 'NR>=1{c++} END{print "control-B lines:", c}' DECISION_LOG.md
→ ALLOWED.  stdout: control-B lines: 193
```

**Control A — `>=` present, non-exempt path.** Differs from C by `NR>=1` vs `NR!=0` and one
letter in a label string. Differs from B by the filename only.

```
awk 'NR>=1{c++} END{print "control-A lines:", c}' STATUS.md
→ BLOCKED.
  PreToolUse:Bash hook error: ["$CLAUDE_PROJECT_DIR"/scripts/master-bash-guard.sh]:
  BLOCKED: shell write from praxis-master. Use Edit on a ledger, or dispatch a worker.
```

**A vs C isolates the trigger: `>=`, in a numeric comparison that redirects nothing.**
**A vs B isolates the rescue: the exemption list, not the command's semantics.**

**Attribution.** The standing hazard — that parallel `PreToolUse` deniers surface only the
last message, so a trip test can show the wrong block string — does not apply here: the
harness names the firing script in the error text itself. Sole denier identified as
`scripts/master-bash-guard.sh`.

## 3. What the code says, marked as derived

`scripts/master-bash-guard.sh:12` is the only `>`-matching line in the file:

```
if echo "$CMD" | grep -qE '(^|[^>])>{1,2}[[:space:]]*[^&]|(^|\s)(sed|tee|patch|dd)\s+.*-i|\bcat\s*<<'; then
```

The trailing `[^&]` excludes `>&`, which is why `2>&1` passed unremarked earlier in this
session while `2>/dev/null` blocked. **The rule is not "redirect." It is "any `>` whose next
character is neither `&` nor absent."** `>=` satisfies that. This paragraph is a reading of
the source and is corroborated by §2, not a substitute for it.

## 4. Second finding — the two guards disagree about one ledger

`master-bash-guard.sh:14`'s exemption list is `DISPATCH_LOG.md | DECISION_LOG.md |
ISSUE_REGISTER.md | HANDOFF.md | */specs/* | */docs/reports/*`. **`STATUS.md` is absent.**
`master-write-guard.sh:14` **does** allow `STATUS.md`. So the master may `Edit` STATUS.md but
may not run a shell command that merely *mentions* it alongside a `>`. Control A is that
asymmetry firing. Not repaired here; not in the Step 4 grant.

## 5. Consequence for Step 4 — a trip test the master cannot run

Any payload exercising this guard contains the character that trips it. The master cannot
self-test the fix: verification of the Step 4 change **must** be dispatched to a worker,
which `master-bash-guard.sh:7` exempts (`[ -n "$AGENT_ID" ] && exit 0`). Recorded so the fix
is not accepted on a self-report.

## 6. Corrected Step 4 target

Fix target is `scripts/master-bash-guard.sh:12`. **Not** `gate-commit.sh`, which the
prohibited list protects and which this evidence does not implicate. Narrow fix only.
Linkage to `Praxis_build-kgp` — same family: these guards match on command strings without
parsing shell quoting or operator context, so they over-match prose and under-match tokens.
Fixing one direction carelessly returns the other.

---

## DEFERRED MEMORY — pending Step 4 reconcile

Per session-45 ruling 2. Content preserved on a sanctioned write path without ratifying
either competing memory mechanism (`CLAUDE.md:51` `bd remember` vs. the master's file-based
agent memory). Migrate forward after Step 4 lands; this line is not deleted.

- **Amear, on cleanups that hide defects (2026-08-08).** Offered three dispositions for the
  181 abandoned `DISPATCH_LOG` rows, he declined both the cheap shrink and the honest
  no-shrink, and took the option costing extra script so the archive emits a running count
  of what it swept. **He will pay implementation cost to stop a cleanup from making a known
  defect quiet.** Apply when scoping any archive, compaction, or suppression change: offer
  the variant that preserves the signal, and offer it with its cost stated.
- **Related, already held in `bd`:** `amear-walkthrough-preference` — he answers structured
  questions decisively and takes the narrow option when its reasoning is given. The
  observation above refines it: *narrow* is not the same as *cheap*, and where those two
  conflict he has chosen thoroughness.
