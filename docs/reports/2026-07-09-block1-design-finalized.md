# Report — Block 1 Design Finalized (bead Praxis_build-elo)

**Date:** 2026-07-09
**Type:** Planning / ledger only — no build dispatched, no commit made (staged only).

## What changed

1. **DECISIONS.md** — appended two entries at the end (append-only, zero edits to prior entries):
   - **D-2026-07-09-A** — Block 1 tunnel technology = plain WireGuard (over Tailscale). LOCKED. No third-party coordination plane; satisfies "no cloud API in the execution stack". Applies to B1-a.
   - **D-2026-07-09-B** — NT8 execution host = Parallels Windows 11 ARM VM now (Apple Silicon has no Boot Camp) / dedicated native x64 Windows PC required before Block 5 live. NT8 is x86-under-emulation, UNPROVEN — validated by B1-0. Signals delivered into a folder shared into the VM. Aligns with D-2026-07-04-A.

2. **docs/design/2026-07-08-block1-signal-delivery.md** — appended a `## Resolved — 2026-07-09` section (existing analysis untouched): the 3 answers (NAT = behind-NAT; tunnel = WireGuard; NT8 = Parallels-VM-now / native-PC-before-live) and the delivery-target consequence (SCP target = shared folder into the Parallels VM; B1-b/B1-c point at that shared-folder path). Trader-parameter-confirmed; pending explicit Block 1 sign-off + Block 0 milestone sign-off.

3. **STATUS.md** — rewrote Current Step / Blockers / Next Action; added D-2026-07-09-A/B to Recent Decisions; Block 0 milestone box left UNCHECKED.

4. **MANIFEST.md** — updated the design-doc row and added the row for this report.

## New beads + dependency edges

| Bead | ID | Priority | Depends on |
|------|-----|----------|-----------|
| B1-0 NT8-on-Parallels validation spike | Praxis_build-3i7 | P1 | (none) |
| B1-a WireGuard mesh + scoped SSH | Praxis_build-dgt | P1 | (none) |
| B1-b n8n SCP-push node (EmMbN4sslwIx1ydn) | Praxis_build-p7s | P1 | B1-a (dgt) |
| B1-c Mac signals layout + VM share + launchd sweep | Praxis_build-dnt | P1 | B1-0 (3i7) |
| B1-d e2e sim latency + idempotency test | Praxis_build-4wk | P2 | B1-b (p7s), B1-c (dnt) |
| B1-e offline failure drill | Praxis_build-63b | P2 | B1-d (4wk) |

Edges wired: B1-c→B1-0; B1-b→B1-a; B1-d→B1-b; B1-d→B1-c; B1-e→B1-d.
`bd ready` shows exactly B1-0 (3i7) and B1-a (dgt) unblocked; all others blocked as designed.

## Verification

- `git diff DECISIONS.md` — no deletion lines: **append-only confirmed**.
- `bd show` on each bead — dependency edges match the intended graph (see table).
- `bd ready` → 2 issues (Praxis_build-3i7, Praxis_build-dgt).

## Not done (by design / gate)

- No commit (staged with `git add -A` only).
- Block 0 milestone NOT marked complete (human-gated).
- No Block 1 build/install/run performed — dispatch stays gated on Block 0 milestone sign-off (F-1/F-3) + explicit Block 1 sign-off.
