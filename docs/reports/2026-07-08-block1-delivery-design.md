# Implementer report — Block 1 signal delivery design (Praxis_build-amd)

**Date:** 2026-07-08
**Deliverable:** docs/design/2026-07-08-block1-signal-delivery.md (proposal only — no DECISIONS.md write, no existing files modified, nothing staged or committed)

## Sources consulted
- CLAUDE.md — architecture chain (TradingView → n8n → JSON file drop → NT8 FileSystemWatcher → Rithmic → MFFU) and the 2026-05-08 local-over-VPS / no-cloud-API constraint.
- STATUS.md — Block 0 progress (0.1–0.6 done, 0.7 awaiting trader, 0.8 pending), D-2026-07-04-A build-first reorder.
- HANDOFF.md resume card 2026-05-12 — workflow `EmMbN4sslwIx1ydn` at `https://n8n.myzerker626.win/webhook/praxis-signal`; open ARCH issue that the webhook write path is remote-only; the four candidate options as listed there.
- Task brief — Step 0.8 outbox at remote `/tmp/praxis-signals/`; local target `/Volumes/Sensidine/Praxis.build/signals/`; n8n SSH credentials exist (noted only, not read).

## Key trade-offs
- **Push vs poll is the decisive axis.** Only SFTP push (Opt 1) and n8n-relocation (Opt 4) are event-driven; polling options carry a structural 5–15 s floor that is hard to justify for NQ.
- **Opt 1 vs Opt 4:** Opt 4 is the cleaner end state (sub-second, one machine, matches the 2026-05-08 local-server intent) but is a migration that re-opens Steps 0.5–0.8 mid-block; Opt 1 reuses everything Block 0 built (SSH credential slots, Telegram error nodes, outbox). Recommended Opt 1 now, Opt 4 named explicitly as the pivot if push latency disappoints or the remote box is being retired anyway.
- **Failure visibility:** Opt 1 is the only option where the existing n8n Telegram error branch natively sees delivery failures; pull-based options need new Mac-side alerting and a dead-man's switch.
- **Cross-cutting requirement regardless of option:** atomic tmp-then-rename writes into the watched dir, and watcher-side idempotency on signal ID.

## Uncertainties / flagged for the trader
1. **Mac network reality unverified:** I assumed residential NAT with no public inbound; if the Mac is directly reachable, Opt 1's setup shrinks but its security note changes.
2. **Tailscale's cloud coordination plane** may or may not violate "no cloud API in execution stack" — the doc offers plain WireGuard as the strict-reading alternative; trader ruling needed.
3. **NT8 is Windows-only**, yet the watcher target is a Mac path. Presumably a VM/Parallels arrangement; the doc flags that a non-shared VM filesystem changes the delivery target path (not the mechanism). Worth confirming before B1-b/B1-c are cut.
4. Latency figures (1–3 s push, 5–15 s rsync poll) are engineering estimates, not measurements; bead B1-d measures the real number with an accept threshold (<5 s).
