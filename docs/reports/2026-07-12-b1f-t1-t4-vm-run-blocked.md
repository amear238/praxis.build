# B1-f PraxisSignalConsumer — T1–T4 Evidence Report
**Date:** 2026-07-12 · **VM:** Parallels Win11-ARM · **NT8:** 8.1.7.2
**Status: BLOCKED — T1–T4 NOT RUN**

## Result summary

| Test | Result |
|---|---|
| Compile | **NOT RUN** — could not open NinjaScript Editor (see blocker) |
| T1 valid drop -> one bracket | **NOT RUN** |
| T2 dedup (same signal_id) | **NOT RUN** |
| T3 malformed -> rejected | **NOT RUN** |
| T4 restart -> no replay | **NOT RUN** |

- `<SIGDIR>` = `\\Mac\praxis-signals` (confirmed; contains signal-template.json)
- `<PX>` = never captured (no NQ chart could be opened)
- NT8 pid: 2956 throughout (no restart performed)
- Journal `praxis-processed-signals.log`: never created — strategy never reached State.Realtime

## Completed successfully

- Source verified: `PraxisSignalConsumer.cs`, 30,225 bytes,
  SHA256 `e4581f4ad2f03d8f22594be9ca03d4565e09dc539282b19f88d856f82fbb4e9a` — **matches expected**
- Installed to `%USERPROFILE%\Documents\NinjaTrader 8\bin\Custom\Strategies\PraxisSignalConsumer.cs`,
  re-hashed at destination (identical), share copy deleted per brief
- Preflight items from the RESUME brief all verified: stale B1-b signal gone (in `archive\`),
  SIGDIR root clean, `.heartbeat` ticking ~1 s (sweep daemon behaving as described)

## Blocker — NT8 WPF layout is in a permanent unhandled-exception loop

NT8 cannot lay out any NEW text-bearing visual. Sole exception, repeating on every layout pass:

```
System.NotSupportedException: Specified method is not supported.
   at System.Runtime.InteropServices.Marshal.ThrowExceptionForHR(Int32 errorCode, IntPtr errorInfo)
   at MS.Internal.Text.TextInterface.Native.Util.ConvertHresultToException(Int32 hr)
   at MS.Internal.Text.TextInterface.FontFace.GetDesignGlyphMetrics(UInt16* pGlyphIndices, ...)
   at System.Windows.Media.GlyphTypeface.GlyphMetrics(...)
   at System.Windows.Controls.Grid.MeasureOverride(Size constraint)
   at System.Windows.Window.MeasureOverride(Size availableSize)
   at System.Windows.ContextLayoutManager.UpdateLayout()
   at System.Windows.Media.MediaContext.RenderMessageHandler(Object resizedCompositionTarget)
*************** unhandled exception trapped ***************
```

Census of newest trace (first 200k lines): 2,703 x System.NotSupportedException,
2,702 x "unhandled exception trapped". No other exception type present.

**Consequence:** existing windows keep repainting (screenshots look normal), but every new
popup/dialog/window dies during Measure. Menus never drop down. This is why no GUI step could
be performed — Connections, NinjaScript Editor + F5, New->Chart, right-click->Strategies are all
new-visual operations. It is NOT an input-injection fault: clicks were verified to land on the
correct, focused, responding window (GetForegroundWindow == WindowFromPoint(509,12) ==
Control Center handle 656770; Responding=True). UIA invoke, real Win32 mouse_event click, and
keyboard (Alt) all failed identically.

### Collateral

| Metric | Value |
|---|---|
| Trace written | 1.6 GB, growing ~231 MB/min (new 231 MB file ~every 55 s) |
| Storm start | trace.20260712.00000.txt created 11:20:29 (first Connections click); continuous since |
| Rate change | ~5 MB/min until 12:03:10, then 231 MB/min |
| NT8 CPU consumed | 1,228 s |
| Disk | 155 GB free; ~11 h to fill at current rate |

## Unexpected / notable

1. NT8 process reports `Responding = True` throughout despite the loop — it is not hung, it is
   spinning in a trapped-exception render cycle.
2. Only three connections exist in Config.xml — Simulated Data Feed, Playback Connection,
   Kinetick End Of Day (Free). No live brokerage is configured on this install.
3. Sim101 could not be confirmed in the Accounts grid (grid empty = not connected), but
   trace.20260709 shows `Cbi.Connection.CreateAccount: account='Sim101'`, so it exists on connect.
4. Chart currently open is MNQ SEP26, not NQ. Note for whoever retries: the strategy validates
   payload `symbol` against `Instrument.MasterInstrument.Name`, so an "NQ" payload on an MNQ chart
   would be REJECTED as a symbol mismatch. The NQ chart is required, as the brief specifies.
5. No orders were placed. No position is open. praxis-processed-signals.log was never created and
   was never touched.

## Required before retry

Restart NinjaTrader. The current process cannot open a window for anyone, human or automation.
If the exception storm recurs on a clean NT8, this is an ARM/Parallels font-stack defect in the VM
and B1-f is blocked until it is fixed (escalate beyond Praxis_build-518, which was scoped to
input injection — that diagnosis is superseded by this one).
