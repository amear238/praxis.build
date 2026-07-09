# B1-a Runbook: Plain WireGuard Tunnel + Scoped SSH Drop Channel

**Date:** 2026-07-09
**Bead:** Praxis_build-dgt (prep task Praxis_build-dgt.1)
**Status:** PREP / DESIGN ONLY — copy-paste templates with placeholders. **No live machine has been touched; no real keys, IPs, or secrets appear in this document.** Every `<...>` is a placeholder the trader fills in at execution time.

> Governing decisions: **D-2026-07-09-A** (Block 1 tunnel = plain WireGuard, no third-party coordination plane) and the Option 1 / SCP-push design in `docs/design/2026-07-08-block1-signal-delivery.md`.

---

## 1. Overview & topology

Two hosts, one point-to-point WireGuard link. n8n pushes signal JSON over the tunnel into ONE directory on the Mac; a NinjaScript FileSystemWatcher inside a Parallels VM (out of scope for B1-a) consumes them.

```
  ┌───────────────────────────────┐                 ┌──────────────────────────────┐
  │  n8n host  (PUBLIC VPS)        │                 │  Mac Studio (residential NAT) │
  │  n8n.myzerker626.win           │                 │  no public inbound            │
  │                                │   WireGuard     │                               │
  │  wg0: 10.77.0.1/24             │◀───tunnel──────▶│  wg0: 10.77.0.2/24            │
  │  ListenPort = <WG_PORT>        │  (UDP, encrypted)│  dials OUT + keepalive       │
  │  [stable public Endpoint]      │                 │  [no ListenPort needed]       │
  │                                │                 │                               │
  │  scp signal.json ─────────────────over tunnel──────▶ sshd bound to 10.77.0.2    │
  │                                │                 │   forced-command → signals dir │
  └───────────────────────────────┘                 └──────────────────────────────┘
```

**Why the VPS holds the Endpoint (not the Mac):** WireGuard needs at least one peer with a stable, publicly-reachable `Endpoint = ip:port`. The VPS has a stable public IP; the Mac is behind residential NAT with no public inbound (confirmed by the trader, D-2026-07-09-A context). Therefore the **Mac is the dialing peer**: it sets `Endpoint` pointing at the VPS and uses `PersistentKeepalive` to keep the NAT mapping open so the VPS can send return traffic. The VPS peer stanza for the Mac has **no** `Endpoint` line — the VPS learns the Mac's current source ip:port from the incoming handshake (roaming).

**Direction of the SSH/SCP session:** n8n (on the VPS) is the SSH **client**; the Mac runs **sshd**. This is independent of who dials the WireGuard tunnel — WireGuard is a bidirectional L3 link once up, so the VPS can open a TCP/22 connection to `10.77.0.2` even though the Mac dialed the tunnel.

### WG subnet (CHOOSEABLE — confirm before execution)

| Role | WG address | Notes |
|------|-----------|-------|
| WireGuard subnet | `10.77.0.0/24` | RFC1918; pick any /24 that does not collide with the Mac LAN, the VPS LAN, or the Parallels VM subnet. **Verify no collision before committing.** |
| n8n host (VPS) | `10.77.0.1` | |
| Mac Studio | `10.77.0.2` | sshd binds here only |

> If the Mac's home LAN already uses `10.77.x.x` or the Parallels VM bridges onto a colliding range, choose a different block (e.g. `10.88.0.0/24`) and substitute consistently everywhere below.

---

## 2. Key generation (BOTH hosts)

Do this **once per host**. The private key is generated **on the host it belongs to and never leaves that host** — it is pasted only into that host's local `wg0.conf`. Only the **public** keys are exchanged between hosts.

Requires `wireguard-tools` (provides `wg`). On the Mac: `brew install wireguard-tools`. On the VPS (Debian/Ubuntu): `apt-get install wireguard-tools`.

**On the VPS (n8n host):**
```bash
umask 077
wg genkey | tee n8n_privatekey | wg pubkey > n8n_publickey
# n8n_privatekey  → paste into the VPS wg0.conf [Interface] PrivateKey   (STAYS ON VPS)
# n8n_publickey   → give to the Mac; goes in the Mac wg0.conf [Peer] PublicKey
```

**On the Mac:**
```bash
umask 077
wg genkey | tee mac_privatekey | wg pubkey > mac_publickey
# mac_privatekey  → paste into the Mac wg0.conf [Interface] PrivateKey    (STAYS ON MAC)
# mac_publickey   → give to the VPS; goes in the VPS wg0.conf [Peer] PublicKey
```

Placeholder mapping used in the templates below:
- `<N8N_PRIVATE_KEY>` = contents of `n8n_privatekey` (VPS-local only)
- `<N8N_PUBLIC_KEY>`  = contents of `n8n_publickey`
- `<MAC_PRIVATE_KEY>` = contents of `mac_privatekey` (Mac-local only)
- `<MAC_PUBLIC_KEY>`  = contents of `mac_publickey`

> Optional hardening: a WireGuard pre-shared key (`wg genpsk`) adds a symmetric layer on top of the keypairs. If used, it goes in **both** peers' `[Peer]` stanza as `PresharedKey = <WG_PSK>`. Omitted from the base templates to keep the first bring-up minimal; note it in the fill-in table if the trader wants it.

---

## 3. `wg0.conf` — n8n host (VPS)

Path on VPS: `/etc/wireguard/wg0.conf` (root-owned, `chmod 600`).

```ini
# /etc/wireguard/wg0.conf  —  n8n host (PUBLIC VPS)
[Interface]
Address    = 10.77.0.1/24
ListenPort = <WG_PORT>            # e.g. 51820 ; must be open UDP inbound on the VPS firewall
PrivateKey = <N8N_PRIVATE_KEY>    # contents of n8n_privatekey — never leaves the VPS

[Peer]
# The Mac Studio. No Endpoint here — the Mac dials in and roams; the VPS
# learns the Mac's current source ip:port from its handshake.
PublicKey  = <MAC_PUBLIC_KEY>     # contents of mac_publickey
AllowedIPs = 10.77.0.2/32         # only route the Mac's single tunnel IP to this peer
```

Bring up on VPS: `sudo wg-quick up wg0` (persist with `sudo systemctl enable wg-quick@wg0`).
**Open UDP `<WG_PORT>` inbound** on the VPS firewall / security group — this is the only new public listener introduced by B1-a, and it is UDP WireGuard, not SSH.

---

## 4. `wg0.conf` — Mac Studio (NAT-dialing peer)

### macOS delivery path (choose one)

- **Option A — `wireguard-tools` via Homebrew (recommended for this runbook):** `brew install wireguard-tools`, place the config at `/opt/homebrew/etc/wireguard/wg0.conf` (Apple Silicon Homebrew prefix; Intel is `/usr/local/etc/wireguard/`), bring up with `sudo wg-quick up wg0`. This uses the userspace `wireguard-go` backend on macOS and creates a `utunN` interface. Matches the copy-paste `wg-quick`/`wg` commands used throughout this runbook.
- **Option B — official WireGuard.app (Mac App Store):** import a tunnel from the same `wg0.conf` text (Import Tunnel(s) from File). GUI-managed; good for autostart-on-login and menubar status. The `[Interface]`/`[Peer]` contents are identical to below. Note: the app names the interface `utunN` too; you cannot pin the name.

> **macOS caveat — interface name:** on macOS the tunnel interface is `utunN` (kernel-assigned, e.g. `utun3`), **not** `wg0`. `wg-quick up wg0` still reads `wg0.conf` and manages the tunnel, but any command that names the live interface (e.g. `sudo wg show`, or the sshd `ListenAddress` reasoning in §5) refers to the **IP** `10.77.0.2`, which is stable, rather than the interface name, which is not. Prefer binding services to the **IP**, not the interface name, on macOS.

Path on Mac (Homebrew, Apple Silicon): `/opt/homebrew/etc/wireguard/wg0.conf` (`chmod 600`).

```ini
# wg0.conf  —  Mac Studio (behind residential NAT, dials OUT)
[Interface]
Address    = 10.77.0.2/24
PrivateKey = <MAC_PRIVATE_KEY>    # contents of mac_privatekey — never leaves the Mac
# No ListenPort — the Mac is a client; the kernel picks an ephemeral source port.

[Peer]
# The n8n host (VPS) — the stable public endpoint.
PublicKey           = <N8N_PUBLIC_KEY>            # contents of n8n_publickey
Endpoint            = <VPS_PUBLIC_IP>:<WG_PORT>   # the VPS public IP + its ListenPort
AllowedIPs          = 10.77.0.0/24                # route the whole tunnel /24 via the VPS peer
PersistentKeepalive = 25                          # keep the NAT mapping open (seconds)
```

> **macOS caveat — AllowedIPs:** using `AllowedIPs = 10.77.0.0/24` (the whole subnet) rather than just `10.77.0.1/32` is the robust choice here — it ensures the Mac routes all tunnel-subnet traffic through the peer and avoids `wg-quick` route-scoping quirks seen on some macOS versions. Since this is a two-host link, the /24 and the /32 are functionally equivalent for reachability; the /24 is simply less fragile. Do **not** put `0.0.0.0/0` here — that would route ALL Mac internet traffic through the VPS, which is not wanted.

Bring up on Mac: `sudo wg-quick up wg0`.
Autostart: either the WireGuard.app "On Demand / Start on login" toggle (Option B), or a launchd job invoking `wg-quick up wg0` at boot (Option A).

---

## 5. sshd hardening on the Mac — bind to the tunnel ONLY

Goal: the Mac's sshd is reachable **only** over the WireGuard tunnel (`10.77.0.2`), never on the LAN or any public path. Password auth off; key auth only.

### 5a. Enable Remote Login (macOS)
macOS ships sshd but it is off by default. Enable it: **System Settings → General → Sharing → Remote Login = On** (or `sudo systemsetup -setremotelogin on`). By default macOS sshd listens on **all** interfaces (`0.0.0.0:22` and `[::]:22`) — §5b restricts that.

### 5b. Drop-in config
Modern macOS `/etc/ssh/sshd_config` ends with `Include /etc/ssh/sshd_config.d/*`. Create a drop-in so upgrades don't clobber it:

Path: `/etc/ssh/sshd_config.d/100-praxis-wg.conf`
```conf
# Bind sshd to the WireGuard tunnel IP ONLY — no LAN, no public listener.
# WireGuard (wg0) must be UP before sshd starts, or sshd cannot bind this address
# (see caveat below).
ListenAddress 10.77.0.2

# Key-only auth.
PasswordAuthentication no
KbdInteractiveAuthentication no
ChallengeResponseAuthentication no
PermitRootLogin no
UsePAM yes            # leave as macOS default; do not flip blindly
```

> **macOS caveat — bind ordering / bind failure:** an `sshd` `ListenAddress 10.77.0.2` can only bind if `10.77.0.2` already exists on an interface. If sshd (launchd job `com.openssh.sshd`) starts at boot **before** WireGuard brings up the `utunN` address, the bind fails and sshd may fall back or not listen. Two robust handlings:
> 1. Bring up WireGuard at boot **before** enabling Remote Login, and/or add a launchd dependency so sshd (re)starts after `wg-quick up wg0`.
> 2. Verify after every reboot with the check in §5c. If binding to the tunnel IP proves flaky across reboots on the installed macOS version, the fallback is `ListenAddress 0.0.0.0` **plus a pf firewall rule** that drops tcp/22 on every interface except `utunN` — document which was used. Flag this explicitly to the trader; do not assume the clean `ListenAddress` bind survives reboot until observed.

Reload sshd after editing: on macOS toggle Remote Login off/on, or `sudo launchctl kickstart -k system/com.openssh.sshd`.

### 5c. Verify no public listener remains
```bash
# Should show sshd listening ONLY on 10.77.0.2:22 — NOT 0.0.0.0:22 or *:22
sudo lsof -nP -iTCP:22 -sTCP:LISTEN
# or:
netstat -an -p tcp | grep '\.22 ' | grep LISTEN
# PASS = the only LISTEN line is 10.77.0.2.22 . FAIL = any 0.0.0.0.22 / *.22 line present.
```

---

## 6. Scoped SSH keypair + forced command (limit n8n to ONE directory)

This is the security core. The n8n peer gets a **dedicated** SSH keypair used for nothing else, and the Mac's `authorized_keys` line pins a **forced command** so that key can only write into the signals drop dir — even if the VPS is fully compromised, it can do nothing on the Mac but drop files into that one folder.

### 6a. Generate the dedicated keypair (on the VPS / n8n host)
```bash
umask 077
ssh-keygen -t ed25519 -f ~/.ssh/praxis_signal_push -C "praxis-n8n-signal-push" -N ""
# ~/.ssh/praxis_signal_push       → private key; loaded into the n8n SSH Private Key credential slot only
# ~/.ssh/praxis_signal_push.pub   → public key; goes in the Mac authorized_keys (below)
```
Placeholder for the public key contents below: `<N8N_SIGNAL_PUSH_PUBKEY>` (the full `ssh-ed25519 AAAA... praxis-n8n-signal-push` line).

The private key is loaded ONLY into the existing n8n **SSH Private Key** credential slot (never committed, never copied elsewhere).

### 6b. Mac account & the signals drop dir
Use a dedicated low-privilege macOS account for the push (e.g. `praxispush`) rather than the trader's login account, so the forced command and its `authorized_keys` are isolated. Its `~/.ssh/authorized_keys` (mode `600`, dir `700`, owned by that user) holds the line below.

`<SIGNALS_DIR>` = the absolute drop-dir path on the Mac. Per the resolved design the SCP target is a **folder shared into the Parallels VM** (B1-c owns that mapping), e.g. `/Users/praxispush/praxis-signals` — confirm the exact absolute path at execution.

### 6c. authorized_keys — Option (a): `rrsync` forced command  ← RECOMMENDED

`rrsync` (restricted rsync, ships with the rsync package) confines rsync to a subtree, read-only or write-only. `-wo` = write-only (the peer can push files in, cannot list or pull) — the tightest fit for a one-way signal drop. **Requires the n8n push to use `rsync -e ssh` (or scp that rsync tolerates)**; the Option 1 design's atomic `tmp`-then-rename push maps cleanly to rsync with a staged filename.

Locate `rrsync` on the Mac first (`brew`'s rsync 3.x ships it, path varies): e.g. `/opt/homebrew/bin/rrsync` or under the rsync libexec. Substitute the real path for `<RRSYNC_PATH>`.

```
# ~praxispush/.ssh/authorized_keys  (Mac)   — single logical line, no wrapping
command="<RRSYNC_PATH> -wo <SIGNALS_DIR>",restrict,no-agent-forwarding,no-port-forwarding,no-pty,no-user-rc,no-X11-forwarding <N8N_SIGNAL_PUSH_PUBKEY>
```
- `-wo` = write-only into `<SIGNALS_DIR>`; the peer cannot read, list, or escape the subtree.
- `restrict` = OpenSSH shorthand that disables pty/forwarding/etc.; the explicit `no-*` flags are belt-and-suspenders and self-document intent.
- Any ssh command other than the rsync server invocation is ignored — the forced command always runs instead.

### 6d. authorized_keys — Option (b): chrooted `internal-sftp` forced command

Confines the peer to SFTP inside a chroot. Pairs with n8n's SFTP node. sshd chroot has a **strict ownership rule**: every component of the `ChrootDirectory` path must be owned by **root** and not group/other-writable, and the chroot dir itself cannot be the writable drop dir — the writable subdir lives *inside* it.

`sshd_config.d` stanza (Mac):
```conf
# /etc/ssh/sshd_config.d/110-praxis-sftp.conf
Match User praxispush
    ChrootDirectory <SIGNALS_CHROOT>     # MUST be root-owned, 755, not writable by praxispush
    ForceCommand internal-sftp -d /drop  # land inside the writable subdir
    AllowTcpForwarding no
    X11Forwarding no
    PermitTTY no
    AllowAgentForwarding no
```
Layout: `<SIGNALS_CHROOT>` root-owned (e.g. `/Users/praxispush/chroot`), with a writable subdir `<SIGNALS_CHROOT>/drop` owned by `praxispush` — that subdir is the real signals dir the VM shares. The `authorized_keys` line then only needs the hardening flags (the `ForceCommand` is enforced by the `Match` block):
```
# ~praxispush/.ssh/authorized_keys  (Mac)
restrict,no-agent-forwarding,no-port-forwarding,no-pty,no-user-rc <N8N_SIGNAL_PUSH_PUBKEY>
```

> **macOS caveat — internal-sftp chroot:** the root-owned-path-chain rule is unforgiving under `/Users/...` (the user's home is user-owned), so the chroot root usually must live somewhere like `/opt/praxis/chroot` (root-owned) with a bind/synthetic mount or the Parallels shared folder mounted at `<chroot>/drop`. This adds moving parts vs. rrsync. Verify the exact chroot ownership chain on the installed macOS version before relying on it.

### Recommendation: **Option (a) `rrsync -wo`.**
It is a single `authorized_keys` line, no chroot ownership-chain gymnastics (which are especially awkward under macOS `/Users`), and `-wo` write-only is a perfect match for a one-directional signal drop. Choose Option (b) `internal-sftp` only if the n8n side must use the SFTP node specifically and rsync/scp is not viable. Both restrict the peer to one directory; rrsync does it with less macOS-specific fragility.

---

## 7. Fill-in table — everything the trader supplies at execution

| Placeholder | Where used | What to supply |
|-------------|-----------|----------------|
| `<VPS_PUBLIC_IP>` | Mac `wg0.conf` `Endpoint` | Stable public IP (or DNS name) of the n8n VPS |
| `<WG_PORT>` | VPS `ListenPort`, Mac `Endpoint`, VPS firewall | Chosen WireGuard UDP port (e.g. 51820); open inbound UDP on VPS |
| WG subnet / addresses | both `wg0.conf` | Confirm `10.77.0.0/24`, `10.77.0.1` (VPS), `10.77.0.2` (Mac) — or a non-colliding block |
| `<N8N_PRIVATE_KEY>` | VPS `[Interface] PrivateKey` | From `wg genkey` on VPS — **stays on VPS** |
| `<N8N_PUBLIC_KEY>` | Mac `[Peer] PublicKey` | From `wg pubkey` on VPS |
| `<MAC_PRIVATE_KEY>` | Mac `[Interface] PrivateKey` | From `wg genkey` on Mac — **stays on Mac** |
| `<MAC_PUBLIC_KEY>` | VPS `[Peer] PublicKey` | From `wg pubkey` on Mac |
| `<WG_PSK>` (optional) | both `[Peer] PresharedKey` | From `wg genpsk`, if the PSK hardening layer is used |
| `<N8N_SIGNAL_PUSH_PUBKEY>` | Mac `authorized_keys` | Public half of the dedicated `praxis_signal_push` SSH key (from VPS) |
| `<SIGNALS_DIR>` | rrsync forced command | Absolute drop-dir path on the Mac (the Parallels-shared folder), e.g. `/Users/praxispush/praxis-signals` |
| `<RRSYNC_PATH>` | rrsync forced command | Absolute path to `rrsync` on the Mac (from the rsync install) |
| `<SIGNALS_CHROOT>` | internal-sftp option only | Root-owned chroot root; writable `drop` subdir inside it |
| Mac push account | account, `authorized_keys` owner | Dedicated low-priv user (e.g. `praxispush`) |

---

## 8. Bring-up order (summary)

1. Generate WG keypairs on each host (§2); exchange **public** keys only.
2. Write `wg0.conf` on VPS (§3) and Mac (§4); `wg-quick up wg0` on both; open UDP `<WG_PORT>` on the VPS.
3. Confirm handshake: `sudo wg show` on either host shows a recent `latest handshake` and nonzero transfer.
4. Generate the dedicated `praxis_signal_push` SSH keypair on the VPS (§6a); install the pubkey in the Mac push account's `authorized_keys` with the rrsync forced command (§6c).
5. Enable Remote Login on the Mac and apply the sshd drop-in bound to `10.77.0.2` (§5); verify no `0.0.0.0:22` remains (§5c).
6. Run the three VERIFY checks (see the companion report `docs/reports/2026-07-09-b1-a-prep-runbook.md`).
