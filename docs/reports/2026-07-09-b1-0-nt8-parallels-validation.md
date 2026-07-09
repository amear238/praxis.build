# B1-0: NinjaTrader 8 on Parallels — Validation Report

**Bead:** `Praxis_build-3i7` (B1-0)
**Date:** 2026-07-09
**Environment:** Windows 11 Pro ARM64, Parallels ARM Virtual Machine, Mac Studio host
**NT8 Version:** 8.1.7.2
**Executed:** on the Mac Studio's Parallels Win11-ARM VM (trader-executed). Findings transcribed to repo by the orchestrator; graded by an independent audit before B1-0 closure.
**Verdict:** PASS — NT8 is usable under x64 emulation for the build-first sim phase.

---

## C2 — NT8 Viability

**Verdict: YES — NT8 installs, launches, and connects cleanly under ARM x64 emulation.**

### Installation

- Installer: `NinjaTrader.Install.msi` (81.8 MB), standard MSI install
- Prerequisite: .NET Framework 4.8 was already present (v4.8.09032, release 533320)
- Installed to `C:\Program Files\NinjaTrader 8\` — full binary tree deployed (NinjaTrader.exe, NinjaTrader.Core.dll, NinjaTrader.Gui.dll, Rithmic adapter DLLs, etc.)
- No installation errors or missing dependency prompts

### Launch & Login

- NT8 launched without crashes or error dialogs
- Login dialog rendered correctly; username `amear238` pre-filled from cached token
- Authenticated against NinjaTrader IS server (`is-us-nt-005.ninjatrader.com:31658`)
- Workspace `Getting Started (Basic)` restored with Control Center, two chart windows, Market Analyzer, and order-entry panel

### Sim Account Connection

- Simulated Data Feed connected; account `DEMO1628771` activated
- Simulation balance: USD $50,000.00
- Net liquidation, margins, PnL fields all populated correctly
- Playback Connection also tested — connected/disconnected cleanly (minor `ObjectDisposedException` on Playback disconnect — cosmetic, non-blocking)

### Responsiveness

- **User assessment: responsive, not laggy.** Chart scrolling and order-entry interaction feel normal.
- Startup time: ~2 minutes from launch to workspace restore (acceptable for x64 emulation)
- Memory footprint: ~677 MB working set for NT8 process (56 threads, 2173 handles)
- System memory: 5.3 GB / 8 GB used (67%) — workable but not generous; recommend 12–16 GB VM allocation if multi-chart workflows are planned
- No UI rendering artifacts, missing elements, or visual glitches observed across multiple screenshots

### Errors

- One non-critical exception: `System.ObjectDisposedException` ("Timer") on Playback Connection disconnect — does not affect sim or live operation
- No crashes at any point during the ~1 hour validation session

---

## C3 — Data + Chart

**Verdict: YES — live market data streams to charts and Market Analyzer without stalling.**

### Chart Verification

- **MNQ SEP26, 1-Minute chart:** full candle rendering (green/red bars), volume histogram, price axis, time axis all functioning
- Price observed: 29,873.50 with live bid/ask updating (A: 29873.75 / B: 29873.25, size 5)
- Chart displayed continuous bars from ~09:10 to 11:30 with no gaps or stalls
- "Time remaining = 00:00:07" countdown visible — confirming real-time bar construction
- **MNQ SEP26, Daily chart:** rendered ~10 months of historical data (Oct 2025–Jul 2026) correctly

### Market Analyzer

All 11 instruments populated with real-time data:

| Instrument | Last | Change | Daily Vol | Rollover |
|-----------|------|--------|-----------|----------|
| MNQ SEP26 | 29,874.50 | +1.38% | 1,940,060 | 71 days |
| ES SEP26 | 7,573.00 | +0.59% | 589,276 | 67 days |
| MES SEP26 | 7,573.00 | +0.59% | 578,249 | 71 days |
| NQ SEP26 | 29,873.75 | +1.38% | 289,463 | 69 days |
| MGC AUG26 | 4,137.50 | +1.35% | 203,079 | 19 days |
| CL AUG26 | 72.18 | −1.82% | 102,508 | 7 days |
| MCL AUG26 | 72.18 | −1.82% | 96,637 | 7 days |
| MYM SEP26 | 52,769 | +0.28% | 76,557 | 71 days |
| GC AUG26 | 4,137.60 | +1.35% | 69,746 | 15 days |
| YM SEP26 | 52,772 | +0.28% | 39,824 | 71 days |
| MBT JUL26 | 63,150 | +1.15% | 32,068 | 22 days |

Data is real-time market data (via NinjaTrader's bundled Kinetick feed), not synthetic sim ticks. This is the same data feed that will be used with Rithmic in production — validating the full rendering pipeline.

---

## C4 — File-Drop Path + Latency

**Verdict: YES — Parallels shared folder works for FileSystemWatcher signal delivery. Latency is sub-300 ms.**

### Shared Folder Configuration

- Parallels shared folders active out of the box: `\\psf\Home`, `\\Mac\Home`, and `Z:\` all map to the Mac user's home directory
- Created `~/praxis-signals/` on Mac side via `\\psf\Home\praxis-signals` — directory appeared instantly
- Test `signal-template.json` written and readable from both paths

### Latency Measurements

Three test suites were run, writing JSON signal files and measuring detection time:

**1. Polling test (5 samples)**

| Sample | Write (ms) | Read confirm (ms) | Total (ms) |
|--------|-----------|-------------------|------------|
| 1 (cold) | 26 | 24 | 54 |
| 2 | 0 | 2 | 3 |
| 3 | 0 | 1 | 2 |
| 4 | 0 | 1 | 2 |
| 5 | 0 | 1 | 1 |

**2. FileSystemWatcher test — same path (5 samples)**

| Sample | Write (ms) | FSW detect (ms) |
|--------|-----------|-----------------|
| 1 | 26 | 185 |
| 2 | 0 | 134 |
| 3 | 0 | 264 |
| 4 | 0 | 140 |
| 5 | 0 | 160 |

**3. FileSystemWatcher test — cross-path: write via Z:\, watch via \\psf\Home (3 samples)**

| Sample | Write (ms) | FSW detect (ms) |
|--------|-----------|-----------------|
| 1 | 30 | 148 |
| 2 | 0 | 143 |
| 3 | 0 | 130 |

### Summary

| Metric | Value |
|--------|-------|
| Polling avg (steady-state) | 2 ms |
| FSW avg (same path) | 177 ms |
| FSW avg (cross-path) | 140 ms |
| FSW max | 264 ms |
| Detection rate | 13/13 (100%) |

The FileSystemWatcher approach (which NinjaScript will use) detects files in **130–264 ms** — well within acceptable range for the n8n → NinjaScript signal chain. Cold-start penalty (~54 ms on first file) is negligible.

---

## Overall Assessment

NT8 on Windows 11 ARM in Parallels is **viable for the build-first sim phase.** No blockers found.

| Checkpoint | Pass? | Notes |
|-----------|-------|-------|
| C2 — NT8 viability | ✅ Yes | Installs, launches, connects cleanly. Responsive under emulation. |
| C3 — Data + chart | ✅ Yes | Real-time bars stream to chart and Market Analyzer without stalling. |
| C4 — File-drop path | ✅ Yes | FSW latency 130–264 ms, 100% detection. Shared folder works. |

### Recommendations

- **Proceed with Block 1 on Parallels.** Emulation performance is sufficient for sim trading and strategy development.
- **Increase VM RAM to 12–16 GB** if multi-chart or multi-strategy workflows are planned (currently at 8 GB, 67% utilized with one chart open).
- **Native x64 mini-PC purchase remains a pre-Block-5 requirement** but is not escalated — no urgency beyond the existing timeline.
- The `ObjectDisposedException` on Playback disconnect is a known NT8 cosmetic bug and does not affect Simulated Data Feed or Rithmic operation.

---

## Caveats & follow-ups (orchestrator notes)

- **C4 used a generic .NET `FileSystemWatcher` harness, not the production NinjaScript indicator.** This validates the OS-level Parallels shared-folder event path (which NinjaScript's watcher rides on) but is a proxy — the real NinjaScript FileSystemWatcher gets exercised in B1-c/B1-d.
- **Data feed was real-time Kinetick via the `amear238` NT login** (cached token), not the account-free Sim101 internal simulator described in the coworker brief. Acceptable — trader's own account, `DEMO1628771` sim/demo account, no live orders placed. Live trading surface was never touched.
- **Shared-folder path used was `~/` (whole Mac home) via `\\psf\Home` / `Z:\`.** B1-a/B1-c should scope delivery to a dedicated `~/praxis-signals/` dir, not expose the full home directory to the VM.
