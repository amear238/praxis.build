# Design — Telegram → Claude Code Inbound Control Channel (Praxis_build-10i)

Date: 2026-07-10
Bead: Praxis_build-10i
Status: **DESIGN ONLY — build/activation is trader-gated.** Nothing in this document
is installed, loaded, or wired. No launchd plists exist, no n8n workflow was changed,
no scripts were written.

---

## 1. Problem & goal

**Outbound already works.** Claude Code sessions notify the trader's phone via
`.claude/hooks/notify.sh` → `ORCH_N8N_WEBHOOK` → n8n → Telegram (confirmed delivering;
see docs/reports/2026-07-08-orch-notify.md lineage and the B1-c stale-alert live-fire,
docs/reports/2026-07-09-b1-c-fu-stale-alert-livefire.md).

**Inbound does not exist.** When an unattended autonomous run is in flight, the trader
(Amear) can *see* what it is doing from his phone but cannot *ask it anything or steer
it*. The goal is a channel where a Telegram message from the trader becomes a bounded
Claude Code invocation on the Mac, and the answer comes back as a Telegram reply.

**The wrinkle:** n8n runs in Docker on the Mac. The `claude` CLI and the repo live on
the **host**. The container cannot execute `claude -p` directly — there is a
container/host boundary that must be crossed by *data*, not by *execution*.

**The answer:** cross the boundary the same way signals already do — a file drop into
a host directory watched by a host launchd agent. This is the proven B1-c pattern,
reused wholesale.

## 2. Prior art reused

| Prior art | Where | What we reuse |
|---|---|---|
| B1-c signals layout + launchd sweep/heartbeat | docs/reports/2026-07-09-b1-c-signals-layout-launchd.md | Internal-disk deployment model (repo scripts are SOURCE only; installer copies to internal disk; plists point internal), launchd LaunchAgent structure, heartbeat + stale-alert pattern, `deploy` vs `install` installer actions (deploy never loads launchd — loading is a trader step) |
| B1-b-fu WatchPaths event-driven sweep | docs/reports/2026-07-10-b1-b-fu-watchpaths-sweep.md | `WatchPaths` on the drop dir for event-driven wake (measured 0.25s relay), plus a slow `StartInterval` poll as the sweep/requeue safety net |
| WatchPaths ~10s throttle finding | bead Praxis_build-8xf | launchd throttles WatchPaths respawns (~10s); acceptable for a human-cadence chat channel — documented as a latency bound, not a defect |
| notify.sh outbound hook | .claude/hooks/notify.sh | The entire reply path. Fire-and-forget, never fails the caller, JSON built via python (no shell interpolation of message text) — the inbound side copies that discipline |
| n8n → host file write | docs/reports/2026-07-09-b1-b-n8n-file-write.md | n8n Docker container writing files into a host-mounted `local-files` volume — identical mechanism for dropping command files |
| Decisions D-2026-07-09-C / D-2026-07-09-D | DECISIONS.md | Least-privilege dir ownership philosophy (dedicated, signals-only surface) and the local-n8n topology this channel rides on |
| Headless authority rule | .claude/skills/praxis-build-manager/SKILL.md section G | Headless `claude -p` runs are **read/report only** — never close beads, commit, update state files, or dispatch implementers. Section F human gates apply unchanged. This is the basis for the recommended authority scope (Option A, §5) |

## 3. Architecture

```
  Trader's phone
      │  Telegram message: "status"
      ▼
  Telegram Bot API
      │  (long-poll / webhook to n8n)
      ▼
┌──────────────────────────── n8n (Docker container) ────────────────────────────┐
│  Telegram Trigger node                                                         │
│    ├─ GUARD 1: from.id / chat.id == trader allowlist?  ──no──► reject + log    │
│    ▼                                                          (+ notify reply  │
│  Write Binary File node                                        "unauthorized") │
│    writes /files/tg-inbox/cmd-<update_id>.json.tmp  → rename → .json           │
│    (container /files ≡ host ~/n8n-compose/local-files, the proven B1-b mount)  │
└────────────────────────────────────────────────────────────────────────────────┘
      │  host-visible file appears:
      │  /Users/admin/n8n-compose/local-files/tg-inbox/cmd-<update_id>.json
      ▼
┌──────────────────────────────── macOS host ─────────────────────────────────────┐
│  launchd LaunchAgent  build.praxis.tg-inbound                                   │
│    WatchPaths: …/local-files/tg-inbox   +  StartInterval 60s (sweep/requeue)    │
│    ProgramArguments: ~/Library/Application Support/Praxis/bin/tg-inbound.sh     │
│                      (INTERNAL disk — TCC rule, §8)                             │
│    ▼                                                                            │
│  tg-inbound.sh (runner)                                                         │
│    1. flock single-flight lock (one command at a time)                          │
│    2. claim oldest cmd-*.json → mv to work/ (atomic; crash-safe requeue)        │
│    3. GUARD 2: chat_id allowlist re-check (defense in depth)                    │
│    4. GUARD 3: dedupe on update_id (processed-ids ledger)                       │
│    5. GUARD 4: parse text → match against COMMAND WHITELIST (§6.3)              │
│         no match ──► reply "unknown command" + audit log; NEVER executed        │
│    6. run:  claude -p <rendered read-only prompt>  (argv-passed, cwd=repo,      │
│         permission-restricted profile, timeout, output captured to file)        │
│    7. reply: notify.sh tg-reply "<verb>: <output excerpt>"                      │
│    8. append audit row → ~/praxis-tg/logs/inbound-audit.log (append-only)       │
│    9. archive command file → done/ (or failed/)                                 │
└──────────────────────────────────────────────────────────────────────────────────┘
      │  notify.sh → ORCH_N8N_WEBHOOK
      ▼
  n8n orchestrator-notify workflow ──► Telegram ──► trader's phone (reply)
```

Data-flow summary: **message text only ever moves as file content and argv elements.
It is never interpolated into a shell command line** (§6.2). The container never
executes anything on the host; the host never trusts anything the container wrote
until it passes guards 2–4.

Kill switch (§6.7): touch `~/praxis-tg/DISABLED` → runner exits immediately before
step 2; or `launchctl bootout` the one agent.

## 4. Command-file format spec

One JSON object per file. File name: `cmd-<update_id>.json`. Written by n8n as
`.tmp` then renamed (atomic-appearance, same as the signals outbox discipline).

```json
{
  "update_id": 987654321,
  "chat_id":   123456789,
  "from_id":   123456789,
  "text":      "status",
  "ts":        "2026-07-10T21:14:03Z"
}
```

| Field | Type | Required | Meaning / rules |
|---|---|---|---|
| `update_id` | integer | yes | Telegram's monotonically-increasing update id. **Dedupe key** — runner keeps a processed-ids ledger; an already-seen id is archived without execution |
| `chat_id` | integer | yes | Telegram chat the message arrived in. Must equal the allowlisted trader chat id or the file is rejected + logged |
| `from_id` | integer | yes | Sender's Telegram user id. Must equal the allowlisted trader user id (guards against the bot being added to a group) |
| `text` | string | yes | Raw message text. **Data only** — parsed against the whitelist; never placed in a shell line |
| `ts` | string (ISO-8601 UTC) | yes | Telegram message timestamp. Runner rejects messages older than a staleness window (e.g. 15 min) — a queue that backed up while the Mac slept must not replay stale steering commands |

Malformed JSON, missing fields, wrong types → move to `failed/`, audit-log the
rejection, send an "unparseable command rejected" reply. Never partially process.

## 5. Authority scope — OPTIONS (trader decision)

The single most consequential choice: **what is a phone message allowed to make the
machine do?** This channel is, structurally, remote command injection into the build
Mac by design — the scope decides how much blast radius a compromised Telegram
account, a stolen phone, or a Telegram-side bug has.

| | Option A — read/report/status ONLY (**RECOMMENDED**) | Option B — A + bead mutations | Option C — full agent steering |
|---|---|---|---|
| Verbs | `status`, `bead` (current), `ready` (bd ready), `audit` (read-only consistency check), `pause` / `stop` (touch a stop-file an autonomous run honors), `help` | A + `claim <id>`, `close <id>`, `note <id> …`, `park/unpark` | Arbitrary prompt forwarded to a live/new session; can direct edits, runs, dispatch |
| Writes to repo/ledgers | **None.** Only its own audit log + a stop-flag file outside the repo | bd database mutations (ledger writes from an unauthenticated-beyond-Telegram channel) | Anything an interactive session can do |
| Consistency with skill §G/§F | Fully consistent — headless = read/report only; pause/stop is *removing* autonomy, never adding | Violates §G ("headless runs never close beads"); would need a §G amendment logged in DECISIONS.md | Directly violates §G and the audit-gate model (writes without the auditor/commit-token path) |
| If trader's Telegram is compromised | Attacker learns build status; can annoyingly pause runs. No writes, no trades, no shell | Attacker can corrupt the task ledger (close/claim beads falsely) — silent process damage | Attacker has a remote agent with repo write reach on the trading-system build machine — worst case |
| Failure-mode character | Fail-safe (worst outcome: a paused run) | Fail-dirty (ledger drift) | Fail-dangerous |
| Build complexity | Small: whitelist + read-only prompt templates | Medium: per-verb argument validation, bd auth story | Large: session hand-off, prompt injection defenses, still unsolved trust problem |

Why A is recommended: it matches the already-locked headless rule (skill §G), keeps
every §F human gate intact, and makes the channel *monotonically safety-increasing* —
the only state it can change is toward LESS autonomy (pause/stop). Escalation later is
a one-way door that is easy to open (new bead, new decision row) and hard to close.

> ### ⚠ TRADER DECISION REQUIRED
> **Choose the authority scope: A, B, or C (A recommended).**
> This is a section-F-class gate: the channel converts a phone message into host
> execution, so its scope is an architectural/risk decision, not an implementation
> detail. Record the choice as a DECISIONS.md row (D-2026-07-1x-…) before any build
> bead is opened. If B or C is ever chosen, skill section G must be amended in the
> same decision, and the security controls in §6 are the *floor*, not the ceiling.
> **No build work proceeds until this is decided.**

## 6. Security controls (numbered, all mandatory at build time)

1. **Sender allowlist, enforced twice.** n8n Telegram Trigger checks
   `from.id`/`chat.id` against the trader's ids (n8n-side, so junk never reaches the
   host); the host runner re-checks the ids inside the JSON (defense in depth — the
   host does not trust the container's filtering). Non-allowlisted → reject, audit
   log, and a one-line notify so the trader learns someone probed the bot.
2. **Message text is data, never shell.** The runner reads `text` from the JSON with
   a real JSON parser (python3/jq), matches it against the whitelist, and passes any
   surviving argument via **argv array or a file path** — never string-interpolated
   into a shell line. Same discipline notify.sh already uses for payload building.
3. **Command whitelist.** Enumerated verbs only (per the chosen scope, §5). Matching
   is exact-verb + typed-argument validation (e.g. bead ids must match
   `^Praxis_build-[a-z0-9]+$`). Anything else: rejected, logged, replied
   "unknown command" — the raw text is echoed back in the *reply and audit log only*,
   never executed.
4. **Single-flight + rate limit.** `flock` lockfile: one command processes at a time;
   queued files wait. Rate limit: max N commands per minute (e.g. 6); excess files are
   deferred, not dropped. Prevents both runaway loops and Telegram-side flooding.
5. **Least-privilege `claude -p` invocation.** Runs as the login user but with a
   dedicated settings profile that (a) permits only read tools (Read/Grep/Glob/`bd
   show`/`bd ready`-class read-only Bash), (b) denies Write/Edit and mutating shell,
   (c) has a hard wall-clock timeout, (d) `cwd` = repo, output to a capture file.
   Consistent with skill §G read/report mode. (The later hooks bead can make this
   deterministic; instruction-level until then, same as §G notes.)
6. **Append-only audit trail.** Every inbound file — accepted, rejected, deduped, or
   failed — appends one row to `~/praxis-tg/logs/inbound-audit.log`:
   `<utc-ts> <update_id> <from_id> <verdict:EXEC|REJECT|DEDUPE|ERROR> <verb|-> <exit> <reply-bytes>`.
   Log is outside the repo (no repo writes from the channel) and never truncated by
   the runner.
7. **Kill switch, two independent layers.** (a) `touch ~/praxis-tg/DISABLED` — runner
   checks it first and exits (works even if launchctl is misbehaving; trader can be
   told the one-liner over any channel). (b) `launchctl bootout gui/$UID/…tg-inbound`
   or delete the single plist. Either alone fully disables inbound; outbound
   notify.sh is unaffected.
8. **Every reply states what ran.** Reply format is `"<verb> → <result>"` (or
   `"REJECTED: <reason>"`), so the trader always sees what the machine believed it
   was told. A silent execution path does not exist.
9. **Staleness window.** Commands older than ~15 min (per `ts`) are rejected as
   stale (control decisions must not replay after a sleep/backlog).
10. **No secrets in the channel.** Bot token lives only in n8n's credential store;
    `ORCH_N8N_WEBHOOK` stays in `~/.praxis/signals.env` (0600) as today. Command
    files contain no credentials; the runner never echoes env into replies.

## 7. Failure modes & mitigations

| Failure mode | Effect | Mitigation |
|---|---|---|
| launchd WatchPaths ~10s respawn throttle (bead 8xf) | Second command inside ~10s waits for the throttle | Acceptable for human chat cadence; `StartInterval 60s` poll bounds worst case; runner drains the whole queue per wake (loop until inbox empty), so a burst costs one throttle window, not one per message |
| Duplicate Telegram deliveries / n8n retries | Same command executed twice | Dedupe on `update_id` (processed-ids ledger, §4); duplicate → archive + audit `DEDUPE`, no execution, no duplicate reply |
| Runner crashes mid-command | Command file stranded in `work/` | Sweep pass (the 60s poll) requeues `work/` files older than the timeout; audit row marks `ERROR`; same sweep/requeue idea as B1-b-fu |
| `claude` CLI unavailable / quota-dead / timeout | No answer produced | Runner captures the non-zero exit, replies `"ERROR: claude unavailable (<reason>)"` — the trader always gets *a* reply; file → `failed/` |
| n8n container down | Outbound reply path dead — trader texts into a void AND inbound stops arriving | Detection: n8n down kills both directions at once, so the symptom (no reply at all) is unambiguous. Runner still executes+logs any already-dropped files; notify.sh fails silently by design, so the audit log records `reply-bytes=0`. Existing stale-heartbeat alerting pattern (B1-c) can be extended to an n8n-liveness check at build time |
| Mac asleep / logged out | Commands queue in the inbox | On wake, staleness window (§6.9) rejects old *steering* commands with an explanatory reply instead of replaying them; fresh ones process normally |
| Telegram account compromise / stolen phone | Attacker can issue whitelisted commands | Scope Option A limits blast radius to reads + pause (§5); kill switch (§6.7); audit trail shows exactly what was issued |
| Bot added to a group / forwarded messages | Foreign `chat_id`/`from_id` | Both ids must match the allowlist (§6.1); reject + notify |
| Command file malformed (n8n bug, partial write) | Parse failure | `.tmp`→rename atomic write on the n8n side; parser rejects to `failed/` + reply (§4); never partially processed |

## 8. TCC / internal-disk install layout

**Hard constraint (persistent memory + B1-c incident):** macOS TCC blocks per-user
launchd agents from *executing* anything on `/Volumes/Sensidine`
(`Operation not permitted` — captured verbatim in
docs/reports/2026-07-09-b1-c-signals-layout-launchd.md). Repo copies are **source
only**; an installer copies runtime pieces to internal disk and the plist points there.

| Role | Path | Disk |
|---|---|---|
| Source scripts (committed, never a runtime path) | `/Volumes/Sensidine/Praxis.build/scripts/tg-inbound*.sh` | external |
| Plist template (committed, `__BIN_DIR__` placeholder) | `/Volumes/Sensidine/Praxis.build/deploy/launchd/build.praxis.tg-inbound.plist` | external |
| Runtime scripts (deployed copy, incl. notify.sh) | `~/Library/Application Support/Praxis/bin/` | internal |
| Installed plist | `~/Library/LaunchAgents/build.praxis.tg-inbound.plist` | internal |
| Inbox (n8n-writable via existing mount) | `/Users/admin/n8n-compose/local-files/tg-inbox/` | internal |
| Work / done / failed / logs / dedupe ledger / DISABLED flag | `/Users/admin/praxis-tg/{work,done,failed,logs}/`, `…/processed-ids`, `…/DISABLED` | internal |
| Webhook env (existing, git-ignored, 0600) | `~/.praxis/signals.env` | internal |

The installer follows the B1-c `praxis-signals-install.sh` shape exactly: a `deploy`
action (copy + render, **never** loads launchd) and an `install` action (deploy +
bootstrap) — with loading reserved for the trader per the B1-c precedent.

## 9. What build/activation will involve (sizing the gated follow-up)

1. **DECISIONS.md row** recording the trader's scope choice (§5) — prerequisite.
2. **n8n workflow** (new, small): Telegram Trigger (bot credential; allowlist filter)
   → Write Binary File to `/files/tg-inbox/` (`.tmp`→rename). Reuses the existing
   local-files mount; no container changes.
3. **Telegram bot setup**: reuse the existing outbound bot or create a dedicated one;
   capture the trader's numeric user/chat ids for the allowlist.
4. **Host runner** `scripts/tg-inbound.sh` (+ small verb→prompt template table) with
   guards §6.1–6.10; a read-only `claude` settings profile.
5. **Plist template** `deploy/launchd/build.praxis.tg-inbound.plist` (WatchPaths on
   the inbox + StartInterval 60).
6. **Installer** (extend `praxis-signals-install.sh` or a sibling) — internal-disk
   copy + render, per §8.
7. **Verification, staged like B1-c**: implementer verifies by running the deployed
   internal-disk script directly against synthetic command files (allowlisted,
   non-allowlisted, duplicate, malformed, stale, unknown-verb) with
   `ORCH_NOTIFY_DRYRUN=1`; **launchd load + live Telegram round-trip is a
   trader-run step.**
8. **MANIFEST/STATUS/report + audit gate** as for any bead.

Rough size: one implementer session for 2–6, plus the trader activation step.
Nothing above starts before the §5 decision.

## 10. Explicit non-goals

- **No trading authority, ever, via this channel.** No order placement, cancelation,
  flattening, or NT8/Rithmic interaction in any scope option. (CLAUDE.md live-account
  rule; skill §F.)
- **No arbitrary shell / arbitrary prompt execution** (unless the trader explicitly
  chooses Option C, which this doc recommends against).
- **No write/edit/vcs/credential authority** — no repo writes, no ledger writes
  (Option A), no credential reads or changes.
- **No public exposure.** No new inbound network surface on the Mac; Telegram→n8n
  uses n8n's existing connectivity (D-2026-07-09-D local topology unchanged).
- **No multi-user support.** Exactly one allowlisted human.
- **No conversational sessions.** Each message is one bounded command→reply cycle;
  this is not a chat interface to a persistent agent.
- **Not a replacement for the audit gate.** Nothing this channel does can mint
  tokens, approve audits, or advance milestones.

## 11. Acceptance criteria (restated from the bead)

1. Trader texts a status command from his own Telegram account → receives the correct
   reply in Telegram, **within the agreed authority scope** (per the §5 decision),
   with the reply stating what was executed.
2. A message from any non-allowlisted sender is **rejected, never executed, audit-
   logged**, and surfaces a rejection notice.
3. Duplicate deliveries of the same `update_id` execute at most once.
4. The kill switch (DISABLED flag or plist removal) fully stops inbound processing.
5. Design doc under docs/design/ before build — **this document.**
