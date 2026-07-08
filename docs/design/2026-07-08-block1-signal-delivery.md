# Block 1 Design: Signal Delivery — Remote n8n → Local Mac

**Date:** 2026-07-08
**Bead:** Praxis_build-amd
**Status:** PROPOSAL — decision-ready, not decided. Nothing here is authorized for build until trader sign-off.

## Problem

Validated trade signals are produced by n8n running remotely (self-hosted Docker at `https://n8n.myzerker626.win`). Step 0.8 verification writes signal JSON to `/tmp/praxis-signals/` **on the remote host**. The NinjaTrader 8 FileSystemWatcher will watch `/Volumes/Sensidine/Praxis.build/signals/` **on the local Mac**. Something must move each validated signal across that gap, fast and observably, per D-2026-07-04-A (build-first: the full signal path is a Block 1 deliverable on sim data — this mechanism is needed now).

Governing constraints:

- **Latency:** NQ futures signals are time-sensitive; every second of delivery delay is slippage risk. Target: webhook receipt → local file on disk in low single-digit seconds.
- **Reliability/retry:** a signal must never be silently lost; duplicates must be tolerable downstream (watcher should be idempotent on signal ID regardless of option chosen).
- **Failure visibility:** delivery failure must reach Telegram (the Step 0.6 notification plumbing already exists in workflow `EmMbN4sslwIx1ydn`).
- **Security:** ASSUMPTION (unverified — open question for the trader): the Mac sits behind residential NAT/firewall with no public inbound reachability. The per-option security analysis below is written against this assumption; if the Mac is in fact directly reachable, see "What would change this recommendation." Either way, opening public inbound ports to the execution machine is undesirable. The 2026-05-08 decision stands: local server over VPS, **no cloud API in the execution stack**.
- **Solo-trader simplicity:** one operator; fewer moving parts and fewer places to look when something breaks.
- **Atomicity (applies to every option):** the writer must land files as `*.tmp` then `mv` to `*.json` in the watched dir, so the FileSystemWatcher never parses a partially written file.

Existing plumbing worth reusing: n8n already holds an SSH Password credential and an SSH Private Key credential (n8n-side SSH is plumbed), and the Telegram success/reject/write-fail nodes from Step 0.6.

---

## Option 1 — SFTP/SCP push from the n8n host to the Mac

### Mechanism
After the validation branch in workflow `EmMbN4sslwIx1ydn`, an SSH/SCP step pushes the signal JSON directly to the Mac over an encrypted private link (Tailscale or plain WireGuard between the two boxes), writing `signals/incoming/<id>.tmp` then renaming to `signals/<id>.json`. The remote `/tmp/praxis-signals/` write becomes a durable **outbox** (spool) that is deleted only after a confirmed push.

### Latency profile
Event-driven: fires the moment validation completes. SSH session setup + transfer of a ~1 KB JSON over a WireGuard tunnel is ~0.3–1.5 s; end-to-end webhook→local-file typically **1–3 s**. No polling floor.

### Failure modes + detection
- Mac asleep/offline, tunnel down, disk full → SSH node errors. n8n retry-on-fail (e.g., 3 attempts, 2 s backoff), then the error branch fires the existing Telegram write-fail node. Signal remains in the remote outbox for replay.
- Silent partial write → prevented by tmp-then-rename.
- Missed-push backstop: a 60 s launchd reconciliation sweep on the Mac rsyncs any leftover outbox files (see outline). Detection is therefore **push-side (n8n error branch → Telegram) plus pull-side sweep**, the strongest visibility of the four options.

### Setup burden
Moderate-low: install Tailscale (or WireGuard) on both hosts; create a dedicated SSH keypair; add one SSH node + retry/error wiring in n8n; write one small launchd sweep job. The n8n SSH credential slots already exist.

### Security surface
Mac accepts SSH **only on the tailnet/WireGuard interface** — nothing public inbound. The n8n host holds a key to the Mac: mitigate with a dedicated low-privilege account or an `authorized_keys` forced command (`rrsync`/`internal-sftp` chrooted to the signals dir) so a compromised n8n box can only drop JSON into one folder. Caveat: Tailscale's coordination plane is a third-party cloud (data plane is peer-to-peer WireGuard). If that reads as "cloud in the execution stack," use plain WireGuard site-to-site instead — same design, slightly more manual key management.

---

## Option 2 — rsync pull on a timer from the Mac

### Mechanism
The Mac runs a launchd job every N seconds: `rsync --remove-source-files remote:/tmp/praxis-signals/ → signals/` over SSH (outbound-only from the Mac), with tmp-then-rename via `--partial-dir`/staged copy.

### Latency profile
Bounded below by the poll interval. Cron floors at 60 s — unacceptable. launchd `StartInterval` can run every 5–10 s, but each tick pays SSH handshake cost against a WAN host (~0.5–1 s), so practical average delivery is **~5–15 s, worst case a full interval + transfer**. Structurally the slowest viable option.

### Failure modes + detection
- Remote host unreachable → rsync exits non-zero on the Mac; but the Mac has no existing alert path — you must script a Telegram `curl` (bot API direct) or a dead-man's-switch. n8n never learns delivery failed, so the existing Step 0.6 nodes don't help.
- Silence is the dangerous failure: a wedged launchd job just stops pulling; needs an explicit heartbeat.
- Signals are never lost (outbox persists until pulled) and rsync is idempotent/resumable — best raw durability.

### Setup burden
Low: one SSH keypair (Mac → remote, outbound), one launchd plist, one script. No n8n changes beyond keeping the outbox write.

### Security surface
Best of the four: zero inbound exposure on the Mac; the Mac holds a read/delete-scoped key to one remote directory. Remote host compromise cannot reach into the Mac.

---

## Option 3 — HTTP response + local poller on the Mac

### Mechanism
n8n exposes an authenticated "pending signals" endpoint (second webhook backed by the outbox or an n8n Data Table). A Mac launchd/daemon script polls it every 2–5 s over HTTPS, writes any returned signals locally (tmp-then-rename), then calls an ack endpoint (or the fetch is destructive) so signals aren't redelivered.

### Latency profile
Poll-bounded: **~2–6 s** average at a 3 s interval. HTTPS keep-alive polling is cheaper per tick than SSH, so a tighter interval is feasible than Option 2 — but still strictly worse than push.

### Failure modes + detection
- The hard part is **queue semantics you must build yourself**: fetch-then-crash-before-write loses a signal unless you implement fetch/ack two-phase; ack-then-fail duplicates. Every such bug is a trading incident.
- Poller death is silent (same dead-man's problem as Option 2); endpoint auth token becomes a new secret to manage.
- n8n can alert on "signal unfetched for >X s" via a scheduled check — buildable, not free.

### Setup burden
Highest: new n8n endpoint + queue/ack workflow, auth scheme, poller script with two-phase logic, staleness monitor. Most custom code of any option, all of it correctness-critical.

### Security surface
Outbound-only from the Mac (good), but adds a **public** authenticated HTTPS endpoint on the n8n host that returns live trade signals — a new internet-facing surface guarded by a bearer token. Middling.

---

## Option 4 — Relocate n8n onto the local Mac

### Mechanism
Move the Docker n8n stack to the Mac. TradingView webhooks reach it via an outbound-only tunnel (Cloudflare Tunnel or equivalent) mapped to the existing hostname. The "delivery" step becomes a local file write by n8n straight into `signals/` — the remote hop ceases to exist.

### Latency profile
Best possible: webhook → validation → local write, **sub-second**. No network hop in the execution path at all.

### Failure modes + detection
- Fewer hops = fewer failure modes; the Step 0.6 Telegram nodes migrate intact and now cover the whole path.
- Concentrates everything on one machine — but the Mac is already the hard single point of failure (NinjaTrader lives there), so this adds little marginal risk while removing the remote box as a second thing that can break.
- Tunnel outage kills signal **ingestion** (not just delivery) — TradingView alerts would 4xx/timeout with no n8n-side error to alert on; needs an external uptime check.

### Setup burden
High, front-loaded: export/import workflows and credentials, stand up Docker on the Mac, configure the tunnel + DNS cutover, and **re-verify Steps 0.5–0.8**. It also discards freshly built Block 0 remote infrastructure mid-block, and there are open ISSUE_REGISTER items (Telegram credential rebind) tangled with the current instance.

### Security surface
Good: Cloudflare Tunnel is outbound-only (no inbound firewall holes), but the execution Mac now also runs the internet-facing automation stack, and the tunnel provider sits in the signal ingestion path — arguably in tension with "no cloud API in execution stack," though it is transport, not a decision-making API. Long-term this is the architecture most consistent with the 2026-05-08 "local server over VPS" intent.

---

## Scored comparison

Scores 1 (poor) – 5 (excellent). Weights reflect the stated constraints (latency and visibility dominate for a live signal path).

| Criterion (weight)            | 1. SFTP push | 2. rsync pull | 3. HTTP poller | 4. Relocate n8n |
|-------------------------------|:---:|:---:|:---:|:---:|
| Latency (×2)                  | 5 | 2 | 3 | 5 |
| Reliability / retry           | 4 | 5 | 3 | 4 |
| Failure visibility (Telegram) | 5 | 3 | 3 | 4 |
| Security surface              | 4 | 5 | 3 | 4 |
| Setup burden (now)            | 4 | 4 | 2 | 2 |
| Solo-trader simplicity        | 4 | 4 | 2 | 5 |
| **Weighted total (/35)**      | **31** | **25** | **19** | **29** |

## Recommendation — Option 1: SFTP/SCP push over a private WireGuard/Tailscale link

**Rationale:** it is the only option that is simultaneously event-driven (1–3 s, no polling floor), reuses plumbing that already exists (n8n SSH credential slots, Step 0.6 Telegram error nodes, the Step 0.8 outbox write), keeps the Mac invisible to the public internet, and preserves all Block 0 work. Option 4 scores nearly as well and is the better *end state*, but it is a migration project with a Block 0 re-verification tail — wrong move mid-build-first-block. Option 2's polling latency is disqualifying for NQ; Option 3 makes you hand-build queue correctness for no latency win.

### Implementation outline

1. **Private link:** Tailscale on the n8n host and the Mac (or plain WireGuard if the trader wants zero third-party coordination plane). Mac SSH bound to the tunnel interface only.
2. **Scoped access:** dedicated keypair; Mac `authorized_keys` entry with forced command (`rrsync -wo` or `internal-sftp`) chrooted to `/Volumes/Sensidine/Praxis.build/signals/` so the remote box can only drop files there. Load the private key into the existing n8n SSH Private Key credential slot.
3. **n8n workflow `EmMbN4sslwIx1ydn`:** after validation + outbox write, add an SSH/SCP node: upload as `signals/incoming/<signalId>.tmp`, then `mv` to `signals/<signalId>.json` (atomic rename — the watcher never sees partial JSON). Node retry-on-fail: 3 attempts / 2 s backoff. On success, delete the outbox copy. On final failure, route to the existing Telegram write-fail node (outbox copy retained).
4. **Reconciliation sweep (backstop):** launchd job on the Mac every 60 s: `rsync --remove-source-files` of any leftover remote outbox files into `signals/`, plus a heartbeat touch-file; a second check alerts (Telegram bot curl) if the heartbeat goes stale.
5. **Verification:** curl a sim payload at `/webhook/praxis-signal`, measure webhook→local-file latency (accept < 5 s), then run a failure drill: take the Mac off the tailnet, confirm Telegram fires and the backlog replays on reconnect.

### Block 1 bead decomposition

- **B1-a:** Tailscale/WireGuard mesh + scoped SSH key + Mac sshd hardening (tunnel-only bind).
- **B1-b:** n8n SCP-push node with atomic rename, retry, outbox-delete-on-success, Telegram error wiring.
- **B1-c:** Mac `signals/` dir layout + launchd reconciliation sweep + heartbeat alert script.
- **B1-d:** End-to-end sim test: latency measurement + duplicate-delivery idempotency check at the watcher contract level.
- **B1-e:** Failure drill: Mac-offline scenario — Telegram alert observed, backlog replay verified.

## What would change this recommendation

- **The NAT assumption proves false (Mac directly reachable):** if the trader confirms the Mac has a stable public address/port-forward, Option 1 simplifies to a plain SSH/SCP push with no tunnel (key-only auth, forced command, fail2ban/port hardening still required) — same ranking, less setup. But direct exposure also raises Option 1's security cost relative to the outbound-only options, so if the trader is unwilling to harden public SSH on the execution machine, prefer the tunnel variant or re-weigh Options 2/4.
- **No VPN acceptable on the Mac** (policy or Parallels/VM networking constraints) → fall back to Option 2 with an aggressive 5 s launchd interval, accepting the latency hit, plus a mandatory dead-man's heartbeat.
- **Measured push latency > 5 s or flaky residential uplink** → Option 4 becomes the fix (remove the hop entirely).
- **Trader intends to decommission the remote box anyway** → skip straight to Option 4 now and eat the Steps 0.5–0.8 re-verification; don't build Option 1 as throwaway.
- **Tailscale's cloud coordination plane is ruled a violation of "no cloud API in execution stack"** → same design over plain WireGuard (config-only change), or Option 4 with a self-hosted ingress.
- **The watcher lands on a Windows VM (NT8 is Windows-only) with a non-shared filesystem** → the delivery *target* changes (push into a folder shared into the VM); mechanism choice is unaffected but B1-b/B1-c paths must be revisited.
- **Multiple future consumers of signals** (e.g., a second execution box) → Option 3's queue model earns its complexity; revisit then, not now.

---

Sign-off: pending trader — on approval this becomes a DECISIONS.md entry
