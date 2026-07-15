# Report — Telegram → Claude Inbound Control Channel BUILD (Praxis_build-10i)

Date: 2026-07-15
Bead: Praxis_build-10i
Design (authoritative): docs/design/2026-07-10-10i-telegram-inbound-control.md
Authority: **LOCKED to Option A — READ / REPORT / STATUS ONLY** (DECISION_LOG 2026-07-15T21:10Z)
Status: **AUTHORED, NOT ACTIVATED.** No launchd job loaded, no workflow imported/activated,
nothing staged or committed. Activation is a trader-gated later session (§Activation below).

---

## 1. Architecture as built

Reuses the B1-c signals-sweep + notify.sh discipline wholesale. Data crosses the
Docker→host boundary as a **file**, never as execution:

```
Trader phone ──Telegram msg──► Telegram Bot API
   │
   ▼  n8n (Docker)  [workflows/praxis-telegram-inbound-control.json, active:false]
   Telegram Trigger ─► IF "Is Trader (allowlist)"  from.id AND chat.id == 6156528469
        │ true                                   │ false
        ▼                                        ▼
   Code "Write Command File"                 NoOp "Drop Unauthorized"
   atomic tmp→rename                         (never written to host inbox)
   /files/tg-inbox/cmd-<update_id>.json
   (container /files ≡ host /Users/admin/n8n-compose/local-files)
   │
   ▼  macOS host
   launchd  build.praxis.tg-inbound   [deploy/launchd/build.praxis.tg-inbound.plist]
     WatchPaths: …/local-files/tg-inbox   +   StartInterval 60 (sweep/requeue backstop)
     ProgramArguments → ~/Library/Application Support/Praxis/bin/praxis-inbound-control-watch.sh
                        (INTERNAL disk — TCC rule §8)
   │
   ▼  praxis-inbound-control-watch.sh   [scripts/praxis-inbound-control-watch.sh — SOURCE ONLY]
     mkdir single-flight lock → claim oldest cmd-*.json to work/ → GUARDS 2..5 →
     FIXED read-only action → reply via notify.sh → audit row → archive done/|failed/
   │
   ▼  notify.sh "tg-reply" → ORCH_N8N_WEBHOOK → n8n orchestrator-notify → Telegram reply
```

**Design deviation (deliberate, safer): no `claude -p` in the loop.** The design sketch
shows the runner invoking `claude -p <read-only prompt>`. Because authority is LOCKED to a
tiny read/report/status verb set, every verb maps to a **fixed argv command** instead. This
eliminates the LLM-prompt-injection surface entirely — there is no free-form prompt anywhere
in the path, and the runner cannot mutate the repo because it never runs a mutating command.
This is strictly within the mandate ("map recognized command keywords to fixed, safe actions;
do not pass a free-form prompt straight through").

## 2. Command allowlist → read-only action mapping

Message `text` is parsed with python3 (`json`), lowercased, reduced to its **first token
stripped to `[a-z0-9]`** — a verb, never a shell string. Verbs (Option A):

| Verb (aliases) | Fixed action (cwd = repo) | Mutates? |
|---|---|---|
| `bead`, `current` | `bd list --status in_progress` | no (read) |
| `ready` | `bd ready` | no (read) |
| `status`, `run` | read `.claude/state/{orchestrator-active,run-mode,iteration-count,max-iterations}` + `bd ready` count → one status line | no (read) |
| `pause` | `: > ~/praxis-tg/control/PAUSE` (flag OUTSIDE repo) | run→**less** autonomy only |
| `stop` | `: > ~/praxis-tg/control/STOP` (flag OUTSIDE repo) | run→**less** autonomy only |
| `help` | static command list | no |
| anything else | **REJECT** "unknown command", audit REJECT, raw verb echoed in reply/audit only, **never executed** | no |

`pause`/`stop` only **author** the control flags (`~/praxis-tg/control/{PAUSE,STOP}`, OUTSIDE
the repo). **Nothing in this delivered build consumes those flags** — the channel is fully
inert on its own. The registered Stop hook (`.claude/hooks/stop-gate.sh`) is left byte-for-byte
untouched by this bead. Making the flags actually halt an autonomous run is a **trader-gated
ACTIVATION step** (§6): at activation time the trader wires the additive, fail-safe honor-check
into the autonomous run loop / Stop hook. That honor-check only ever removes autonomy
(monotonically safety-increasing per design §5); remove the flag to resume. Until the trader
performs that wiring, `pause`/`stop` write a flag that no consumer reads.

## 3. Security / sender restriction

Enforced **twice** (design §6.1, defense in depth):
1. **n8n side (GUARD 1):** IF node requires `message.from.id == 6156528469` **AND**
   `message.chat.id == 6156528469`; non-matches route to a NoOp and are **never written to
   the host inbox** (junk never reaches the Mac). The id is the same one the outbound Telegram
   node already carries literally — chat_id is not a secret; the bot **token** stays only in
   n8n's credential store (`Orchastrator-Mine`, id `F9Q7ibTWgyAQpNAT`).
2. **Host side (GUARD 2):** the runner re-checks `chat_id` and `from_id` inside the JSON against
   `PRAXIS_TG_CHAT_ID`/`PRAXIS_TG_FROM_ID` (read from `~/.praxis/signals.env`, the same 0600
   file as `ORCH_N8N_WEBHOOK`; built-in fallback `6156528469`). The host never trusts the
   container's filtering.

Additional guards, all verified: update_id **dedupe** ledger (`~/praxis-tg/processed-ids`);
**15-min staleness** window (no replaying steering after a sleep/backlog); **6/min rate limit**
(defer, not drop); **mkdir single-flight lock** (macOS has no `flock`) with stale-lock reaping;
**append-only audit log** outside the repo (`~/praxis-tg/logs/inbound-audit.log`, schema
`ts update_id from_id verdict verb exit reply-bytes`); **kill switch** `touch ~/praxis-tg/DISABLED`
(runner exits before claiming anything). No secrets in command files or replies.

## 4. Smoke-test evidence (source-tree, ORCH_NOTIFY_DRYRUN=1, scratchpad dirs)

8 synthetic command files, one drain pass — all dispositions correct:

```
1001 EXEC   ready   0  → bd ready output (done/)
1002 EXEC   bead    0  → in_progress list (done/)
1003 EXEC   status  0  → run status line (done/)
1004 REJECT -       1  → unauthorized sender 999/999 (failed/)
1005 REJECT rm    127  → "rm -rf /" → verb "rm" unknown, NEVER executed (done/)
1006 STALE  stop    1  → 30-min-old steering rejected; STOP flag NOT set (done/)
1007 ERROR  -       1  → malformed JSON (failed/)
1008 EXEC   pause   0  → PAUSE flag written (done/)
replay 1002 → DEDUPE  → no execution, no duplicate reply
fresh stop  → STOP flag written; help → static list
```

launchd load + a live Telegram round-trip is the trader-run step (design §9.7).

## 5. Why nothing is activated

- launchd job **not loaded** — no `launchctl bootstrap`; installer default action is `deploy`
  (copy + render only, never loads). Plist exists only as a template + (after deploy) a rendered
  file the trader loads.
- n8n workflow exported with `active:false`; **not imported** to the live instance.
- Runner is **SOURCE ONLY** in `scripts/`; the internal-disk runtime copy does not exist until
  the trader runs the installer (TCC rule §8: launchd cannot exec on `/Volumes/Sensidine`).
- Nothing staged, nothing committed — all changes left in the working tree.

## 6. Exact trader steps to activate later

1. **Import the workflow:** n8n → import `workflows/praxis-telegram-inbound-control.json`;
   confirm the `Orchastrator-Mine` Telegram credential binds; **activate** it. (If the outbound
   bot is polling-based, ensure only one Telegram Trigger consumes updates for that bot token.)
2. **Deploy the host side (does NOT load launchd):**
   `./scripts/praxis-inbound-control-install.sh deploy`
   → copies runner + notify.sh to `~/Library/Application Support/Praxis/bin/`, creates
   `~/praxis-tg/{work,done,failed,logs,control}` + `tg-inbox`, seeds
   `PRAXIS_TG_CHAT_ID/FROM_ID` into `~/.praxis/signals.env`, renders the plist.
3. **Load the agent (trader gate):**
   `launchctl bootstrap gui/$UID ~/Library/LaunchAgents/build.praxis.tg-inbound.plist`
   (or `./scripts/praxis-inbound-control-install.sh install` to deploy + load in one step).
4. **(Optional, to make `pause`/`stop` actually halt a run) Wire the honor-check.** The build
   leaves the registered Stop hook untouched, so the flags are inert until this step. To make an
   autonomous run honor them, add a minimal additive check at the top of the autonomous run
   loop / Stop hook (`.claude/hooks/stop-gate.sh`) — e.g.:
   `if [ -e "$HOME/praxis-tg/control/STOP" ] || [ -e "$HOME/praxis-tg/control/PAUSE" ]; then` fire an
   `autonomous-halt` notify and stop requesting the next bead (let in-flight work wind down), then
   exit 0. It must ONLY remove autonomy (never block a normal manual session end) and must not
   alter any other stop-gate behavior. Remove the flag file to resume. **Skip this step and the
   channel remains read/report/status only, with `pause`/`stop` writing a flag nothing reads.**
5. **Verify end-to-end:** from the trader's phone send `help`, then `status`; confirm replies.
   Send a message from any other account → confirm it is dropped (no host file, no reply).
   **Watch the first run for TCC read-access to `/Volumes/Sensidine`** — the memory rule covers
   exec; if `bd` reads of the external-volume repo are also blocked under launchd, set
   `PRAXIS_REPO` to a Full-Disk-Access-granted context or grant the agent FDA.
6. **Kill switch anytime:** `touch ~/praxis-tg/DISABLED`, or
   `launchctl bootout gui/$UID/build.praxis.tg-inbound`.

## 7. Files authored

- `scripts/praxis-inbound-control-watch.sh` — host runner (source only)
- `deploy/launchd/build.praxis.tg-inbound.plist` — LaunchAgent template
- `scripts/praxis-inbound-control-install.sh` — companion installer (deploy/install/uninstall/status)
- `workflows/praxis-telegram-inbound-control.json` — n8n workflow (active:false)
- `MANIFEST.md` — new-file rows

**Not touched (deliberate):** `.claude/hooks/stop-gate.sh` — the pre-existing REGISTERED Stop
hook is left byte-for-byte unchanged. Wiring the pause/stop honor-check is a trader-gated
activation step (§6), NOT part of this build. This bead does not hot-patch enforcement
infrastructure.
- `docs/reports/2026-07-15-10i-telegram-inbound-build.md` — this report
