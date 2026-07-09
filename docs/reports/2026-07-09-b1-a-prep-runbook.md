# Implementer Report — B1-a Prep: WireGuard + Scoped SSH Runbook

**Date:** 2026-07-09
**Bead:** Praxis_build-dgt.1 (prep for B1-a `Praxis_build-dgt`)
**Type:** DESIGN / PREP — no live machine touched, no real keys or IPs generated.

## What was produced

`docs/design/2026-07-09-b1-a-wireguard-ssh-runbook.md` — a copy-paste runbook + config templates for:
- Two-host topology (public-VPS WireGuard Endpoint vs NAT-dialing Mac).
- `wg0.conf` templates for both the VPS and the Mac (placeholders only).
- WireGuard key-generation steps for both hosts, with the private-key-never-leaves-host rule.
- macOS sshd hardening: drop-in `sshd_config.d` stanza binding sshd to the tunnel IP `10.77.0.2` only, password auth off, plus the verify command for "no `0.0.0.0:22`".
- The dedicated scoped SSH keypair and BOTH forced-command options: (a) `rrsync -wo <SIGNALS_DIR>` and (b) chrooted `internal-sftp`, each with `no-pty,no-port-forwarding,no-agent-forwarding` hardening.
- A fill-in table of every placeholder the trader supplies at execution.

## Key design choices

- **VPS holds the WireGuard Endpoint, Mac dials out.** WireGuard needs one peer with a stable public `Endpoint`; only the VPS has a stable public IP. The Mac (residential NAT, no public inbound) sets `Endpoint` at the VPS and uses `PersistentKeepalive = 25` to hold the NAT mapping open. The VPS peer stanza for the Mac deliberately has **no** `Endpoint` (roaming — the VPS learns the Mac's source ip:port from the handshake). SSH direction is independent: VPS = client, Mac = sshd, over the bidirectional L3 tunnel.
- **rrsync vs internal-sftp → recommend `rrsync -wo`.** Single `authorized_keys` line, write-only into exactly one directory, and it avoids sshd's root-owned-chroot-path-chain rule, which is especially awkward on macOS where `/Users/<user>` is user-owned (forces the chroot root to live under a root-owned path like `/opt/praxis/chroot` with the drop dir mounted inside). internal-sftp is documented as the fallback for when the n8n side must use the SFTP node specifically.

## macOS caveats flagged explicitly in the doc (not guessed silently)

1. **Interface name is `utunN`, not `wg0`** — bind/reference services by the **IP** `10.77.0.2` (stable), never the kernel-assigned interface name.
2. **sshd bind-ordering risk** — `ListenAddress 10.77.0.2` only binds if WireGuard brought the address up first; at boot sshd may start before the tunnel. Documented handling: order WG before Remote Login / add a launchd dependency, verify each reboot, and a `ListenAddress 0.0.0.0` + pf-drop-except-utun fallback if the clean bind proves flaky on the installed macOS version.
3. **AllowedIPs** on the Mac set to the whole `/24` (not `/32`) to dodge `wg-quick` macOS route-scoping quirks; explicitly NOT `0.0.0.0/0`.
4. **internal-sftp chroot ownership chain** is unforgiving under `/Users`; noted as a reason to prefer rrsync.

Each caveat is written into the runbook with a "verify on the installed macOS version before relying on it" instruction rather than asserting it works.

## Verification checklist — maps 1:1 to the three B1-a VERIFY steps

Prereq: WireGuard up (`sudo wg show` shows a recent handshake), sshd bound per §5, forced command installed per §6. Run all three from the **n8n host (VPS)** unless noted. `<KEY>` = `~/.ssh/praxis_signal_push`.

| # | B1-a VERIFY step | Expected | Exact command (trader runs) |
|---|------------------|----------|------------------------------|
| V1 | scp a test file INTO the signals dir → **succeeds** | file lands in `<SIGNALS_DIR>` on the Mac | rrsync option: `echo '{"test":1}' > /tmp/sig-test.json && rsync -e "ssh -i <KEY>" /tmp/sig-test.json praxispush@10.77.0.2:test-$(date +%s).json` — then confirm on the Mac it appears in `<SIGNALS_DIR>`. (sftp option: `sftp -i <KEY> praxispush@10.77.0.2` then `put /tmp/sig-test.json`.) |
| V2 | scp to ANY OTHER path → **denied** | non-zero exit / permission denied; nothing written outside `<SIGNALS_DIR>` | `rsync -e "ssh -i <KEY>" /tmp/sig-test.json praxispush@10.77.0.2:/etc/evil.json` and `ssh -i <KEY> praxispush@10.77.0.2 'cat /etc/passwd'` — **both must FAIL** (forced command ignores the arbitrary command; rrsync `-wo` refuses the out-of-subtree path). |
| V3 | sshd not reachable OFF the tunnel → **times out** | connection refused/timeout on any non-tunnel path | From a host on the public internet (or the Mac's LAN, NOT the tunnel): `nc -vz -w 5 <MAC_PUBLIC_OR_LAN_IP> 22` → must **time out / refuse**. Contrast: `nc -vz -w 5 10.77.0.2 22` from the VPS over the tunnel → **succeeds**. Also on the Mac: `sudo lsof -nP -iTCP:22 -sTCP:LISTEN` shows ONLY `10.77.0.2.22`, no `0.0.0.0.22`. |

All three are copy-paste executable once the trader fills placeholders from the §7 table.
