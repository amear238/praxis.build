# Block 1 Milestone — Independent Audit (2026-07-15)

This report records a fresh, read-only audit of Block 1 (Foundation, build-first).
Exit criterion: **full Block 1 signal path built and running on free SIM data**
(webhook → local n8n → JSON file drop → Parallels VM share → NT8 NinjaScript
FileSystemWatcher → sim bracket order on Sim101). Every claim below was checked
against the repo (git log, report files, DECISIONS.md, beads) — not restated from
STATUS.md. Verdicts: **VERIFIED** (auditor checked repo evidence directly),
**TRADER-CONFIRMED** (evidence is a recorded trader action), **FAIL**.

## Per-item results

| Item | Claim | Verdict |
|------|-------|---------|
| B1-0 | NT8-on-Parallels validation PASS | VERIFIED |
| B1-a | WireGuard tunnel — deferred by decision, in-scope | VERIFIED (deferral) |
| B1-b | n8n local file-write node live | VERIFIED |
| B1-c | Signals layout + VM share + launchd (+ follow-ups, relay re-architecture) | VERIFIED |
| B1-d | E2E latency + idempotency PASS | VERIFIED |
| B1-e | Offline failure drill PASS; F-B1e-1 gap fixed live | VERIFIED |
| B1-f | NinjaScript consumer, T1–T4 PASS | VERIFIED + TRADER-CONFIRMED (T1 GUI bracket) |

## Item detail

### B1-0 — NT8-on-Parallels validation: VERIFIED
Commit `6909b96` (2026-07-09) exists. Report
`docs/reports/2026-07-09-b1-0-nt8-parallels-validation.md` concludes NT8 on Win11
ARM/Parallels is viable for the build-first sim phase — checkpoints C2/C3/C4 all
pass, FileSystemWatcher detection 13/13 at 130–264 ms, no blockers. Report honestly
caveats that C4 used a generic .NET FSW harness (proxy), later superseded by the real
NinjaScript consumer evidence under B1-f. No live trading surface touched.

### B1-a — WireGuard tunnel: VERIFIED as DEFERRED (not a gap)
DECISIONS.md entry **D-2026-07-09-D** exists (Status: LOCKED, trader-chosen
2026-07-09): n8n runs locally on the Mac for Block-1 build-first; public-ingress
topology (VPS+WireGuard vs tunnel relay) is deferred to pre-live (Block 4–5). The
entry explicitly re-scopes B1-a as deferred and B1-b to a local file-write node.
Deferral is in-scope for the milestone; sim data never exercises public ingress.

### B1-b — n8n local file-write node: VERIFIED
Commit `b5e022e` (2026-07-09) exists. Report
`docs/reports/2026-07-09-b1-b-n8n-file-write.md` records the change published and
active on the production webhook (workflow `EmMbN4sslwIx1ydn`), atomic .tmp→.json
writes, retry, Telegram error route — verified with a real test signal landing in
the drop dir and live Telegram notifies on both paths.

### B1-c — Signals layout + VM share + launchd: VERIFIED
Commit `dc5216c` (2026-07-09) exists; report
`docs/reports/2026-07-09-b1-c-signals-layout-launchd.md` documents the layout,
scoped Parallels share (retiring the whole-home B1-0 share), and sweep/heartbeat/
stale-alert launchd jobs. Follow-ups verified: `7420ae5` (B1-c-fu, live-fire
stale-heartbeat Telegram alert) and `c19531b` (B1-b-fu, event-driven sweep).
Relay re-architecture **D-2026-07-12-A** exists in DECISIONS.md: WatchPaths
replaced by a persistent KeepAlive 1s-sweep daemon after measured launchd 10s
respawn throttling; relay leg bounded at ~1.3s.

### B1-d — E2E latency + idempotency: VERIFIED
Commit `d24537c` (2026-07-10) exists. Report
`docs/reports/2026-07-10-b1-d-e2e-sim-test.md` verdict: LATENCY PASS (max 4.309s
< 5s, thin margin, burst caveat F1) and IDEMPOTENCY PASS at contract level, with
finding F2 (filename keyed on ts+signal_id) mandating in-file signal_id dedup —
the contract later implemented and proven in B1-f (bead 9tl). The 4.3s figure was
reclassified by D-2026-07-12-A as a blocking-curl measurement artifact; true
unthrottled delivery is ~0.5–1.3s post-daemon.

### B1-e — Offline failure drill: VERIFIED
Commit `5822420` (2026-07-10) exists. Report
`docs/reports/2026-07-10-b1-e-offline-drill.md` shows spool+replay PASS with a
silent-loss gap found (stuck promotion un-alerted). Fix verified: commit `1c53a18`
(F-B1e-1 stuck-backlog detector), report
`docs/reports/2026-07-10-f-b1e-1-backlog-detector.md` — deployed live, real
Telegram alert observed at 71s plus recovery note on drain; gap closed.

### B1-f — NinjaScript consumer, T1–T4: VERIFIED + TRADER-CONFIRMED
Source commit `ed2bc9e` and final-state commit `228b586` (2026-07-15) both exist.
Evidence report `docs/reports/2026-07-14-b1f-t1-t3-mac-run.md` end state:
- **T1 (valid drop → exactly one sim bracket)**: corrected-geometry drop ACCEPTED
  sub-second Mac-side (journal 15:12:45Z), and the standing bracket (fill 29820
  long, working OCO stop 29741.25 / target 29901.25 on Sim101, no Log errors) was
  **TRADER-CONFIRMED** in the NT8 GUI 2026-07-15 ~12:05 ET. The screenshot PNG was
  OS-purged before archival; the evidence of record is the transcription in the
  report (trader may re-drop a capture; non-blocking).
- **T2 dedupe (9tl contract)**: PASS — same signal_id under a new filename journaled
  DUPLICATE, filed to `duplicates/`, proven across an NT8 restart. VERIFIED.
- **T3 malformed → rejected, no order**: PASS (non-vacuous instance). VERIFIED.
- **T4 restart no-replay**: PASS via catch-up evidence (9:43 restart, journal
  reload, no replay of processed file). VERIFIED.
- Journal shows exactly two ACCEPTED signals total, one per unique signal_id.
The report also honestly records the 07-15 10:35 bracket **failure** (blind-priced
legs above fill → stop reject → OCO-ID-reuse cascade → safety flatten/terminate),
filed as bug bead `btb` — the failed attempt does not carry the T1 verdict; the
corrected drop does.
Beads **ct5** and **9tl** are both CLOSED (`bd show` checked); close reasons cite
T1–T4 PASS with the trader-touch satisfied 2026-07-15 and commits 5a05a67/ec10f58/
228b586, matching the report.

## Known-open items (honest carry list — `bd list --status=open`, 6 open)

- **btb (P2, bug)**: OCO-ID-reuse cascade after stop-leg reject + missing
  market-relative bracket-geometry pre-validation. Includes the honest 07-15 10:35
  failure record. Whether btb lands pre- or post-milestone is a pending
  milestone-ask-time decision for the trader.
- **10i (P2)**: Telegram→Claude inbound control channel — design decision pending;
  not a Block-1 exit item.
- **518 (P3, monitor-only)**: Win11 VM DirectWrite glyph-metrics storm; probe
  negative for 3 consecutive sessions (10–12); dependency removed from ct5.
- **01h (P3, bug)**: VM T1–T4 harness did not fire on journal go-signal.
- **qxd (P3, bug)**: n8n Write-Signal-File false-failure retry (~4s HTTP-200 delay,
  triple-writes; dedup absorbs it downstream).
- **6h7 (P4)**: signal-template.json stale schema.

Also carried, not bead-tracked:
- **Open sim position possibly still standing on Sim101** (long 1 NQ SEP26 with
  working bracket at last evidence). Sim-only; flatten vs let it work is the
  trader's call.
- **OnTermination-journaling DECLINE recommendation pending ratification** —
  recorded in `docs/runbooks/2026-07-10-b1f-nt8-consumer-install.md` section 6.2;
  ratification (and a DECISIONS.md entry if ratified) belongs to trader/orchestrator.

## Scope wall — live/funded accounts

**No live or funded account was touched at any point in Block 1.** All order
activity was on **Sim101** (NT8 sim). The consumer source
`ninjascript/PraxisSignalConsumer.cs` carries a hard SIM-only guard: a
`private const string RequiredAccountPrefix = "Sim"` account-name check with no
parameter or property to disable it — a non-Sim account logs REFUSED and the
watcher never starts (verified in source, lines ~40–107). B1-0's data feed used the
trader's demo login (`DEMO1628771`); no live orders placed.

## Bottom line

7/7 items pass verification: 6 VERIFIED from repo evidence, with B1-f's T1 GUI
bracket confirmation TRADER-CONFIRMED (recorded 2026-07-15). 0 FAIL. The full
Block-1 signal path is built and has run end-to-end on sim data with the exit-path
evidence committed. Known-open items above are carried honestly; none is a Block-1
exit criterion, though the trader should explicitly rule on btb timing, the open
Sim101 position, and the section-6.2 ratification at sign-off.

---

**This report does not certify the milestone. Sign-off is the trader's alone.**
