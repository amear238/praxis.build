# B1-f PraxisSignalConsumer — T1–T4 Evidence Report
**Date:** 2026-07-14 · **VM:** Parallels Win11-ARM · **NT8:** 8.1.7.2
**Operator:** Cowork VM agent (read-only GUI tier — no click/type access to NinjaTrader)
**Status: BLOCKED — T1–T4 NOT RUN**

## Result summary

| Test | Result | Reason |
|---|---|---|
| Task A: Start consumer on Sim101 | **BLOCKED** | GUI read-only; two config errors found (see below) |
| T1 valid drop → one bracket | **NOT RUN** | Blocked by Task A |
| T2 dedup (same signal_id) | **NOT RUN** | Blocked by Task A |
| T3 malformed → rejected | **NOT RUN** | Blocked by Task A |
| T4 restart → no replay | **NOT RUN** | Blocked by Task A |

## Evidence gathered (all verified from trace files + source code)

### Blocker 1: Strategy is on DEMO1628771, not Sim101

The trader renamed DEMO1628771's **display name** to "sim101", making the
Accounts grid appear to show sim101. But `Account.Name` (which the strategy
checks) is still `DEMO1628771`.

**Trace evidence (trace.20260714.00002.txt):**

```
2026-07-14 11:16:53:811 (Simulation) Cbi.Connection.CreateAccount: account='DEMO1628771' displayName='sim101' fcm='' denomination=UsDollar forexLotSize=1
2026-07-14 11:16:53:811 (Simulation) Cbi.Connection.CreateAccount.DisplayName: account='DEMO1628771' fcm='' oldDisplayName=DEMO1628771 newDisplayName=sim101
```

**Strategy correctly refused — 4 times across 2 NT8 sessions today:**

```
2026-07-14 10:56:46:515 ERROR: PRAXIS-B1f REFUSED: account 'DEMO1628771' is not a Sim account (must start with 'Sim'). No signals will be processed. SIM ONLY.
2026-07-14 10:56:46:605 ERROR: PRAXIS-B1f realtime reached on non-sim account — watcher NOT started.
2026-07-14 11:10:46:004 ERROR: PRAXIS-B1f REFUSED: account 'DEMO1628771' ...
2026-07-14 11:17:18:603 ERROR: PRAXIS-B1f REFUSED: account 'DEMO1628771' ...
2026-07-14 14:36:48:159 ERROR: PRAXIS-B1f REFUSED: account 'DEMO1628771' ...
```

**Source confirms (PraxisSignalConsumer.cs):**

```csharp
accountIsSim = Account != null
    && !string.IsNullOrEmpty(Account.Name)
    && Account.Name.StartsWith(RequiredAccountPrefix, StringComparison.OrdinalIgnoreCase);
```

The check is on `Account.Name` (internal name), NOT the display name.

The real `Sim101` account also exists and connects fine:

```
2026-07-14 11:16:50:661 (Simulation) Cbi.Connection.CreateAccount: account='Sim101' displayName='Sim101'
2026-07-14 11:16:53:875 (Simulation) Cbi.Account.OnConnectionStatus: account='Sim101' fcm='' status=Connected
```

### Blocker 2: Chart instrument is MNQ (Micro), not NQ (E-mini)

Chart tab reads **MNQ SEP26** (Micro E-mini Nasdaq-100), not NQ SEP26
(E-mini NASDAQ 100). The signal template has `"symbol": "NQ"`.

**Source confirms symbol validation:**

```csharp
string chartSymbol = Instrument.MasterInstrument.Name; // e.g. "NQ"
if (!string.Equals(sig.Symbol, chartSymbol, StringComparison.OrdinalIgnoreCase))
    return "symbol '" + sig.Symbol + "' does not match strategy instrument '" + chartSymbol + "'";
```

On an MNQ chart, `Instrument.MasterInstrument.Name` = "MNQ".
A signal with `"symbol": "NQ"` → rejected as symbol mismatch.

This was also flagged in the 2026-07-12 report but was not corrected.

### DirectWrite storm (bead 518): NOT recurring

Trace files today are normal size:

| File | Size | Last write |
|---|---|---|
| trace.20260714.00000.txt | 18 KB | 10:48:24 AM |
| trace.20260714.00001.txt | 45 KB | 11:16:05 AM |
| trace.20260714.00002.txt | 107 KB | 2:36:37 PM |

Compare to 2026-07-12 storm: 1.6 GB growing at 231 MB/min. Today's trace
is 4 orders of magnitude smaller and not growing abnormally. No
`System.NotSupportedException` observed. **Bead 518 probe negative.**

### Other observations

- `praxis-processed-signals.log`: **does not exist** — strategy has never started
- `incoming/` directory: **empty** — no signals pending
- No `processed/`, `rejected/`, or `duplicates/` directories exist yet
- No orders placed, no positions open
- Sim101 account: $50,000 cash, connected (green), clean
- Connection loss at 14:35 UTC (10:35 ET) auto-disabled strategy;
  auto-restart at 14:36 UTC immediately REFUSED again (same account issue)

## Operator access limitation

NinjaTrader was granted at **read-only** tier by the Cowork access control
system. The operator could screenshot and read trace files but could not
click, type, or interact with NinjaTrader's GUI. This prevented:

- Opening the Strategies dialog to change the account assignment
- Changing the chart instrument from MNQ to NQ
- Enabling/disabling the strategy
- Any GUI-based test execution

This is a platform-level access restriction that cannot be overridden by
the operator.

## Required manual steps before retry

### Fix 1: Assign strategy to real Sim101 (not the renamed DEMO1628771)

1. Right-click the MNQ SEP26 chart → **Strategies…**
2. Select PraxisSignalConsumer → **uncheck Enabled** (must disable to edit)
3. In the **Account** dropdown: the current "sim101" entry is DEMO1628771
   in disguise. Select the **other** entry — the real `Sim101` account.
   If both show as "sim101" due to the display name rename, check the
   Accounts tab: Sim101 has $50,000 cash / $0 buying power; DEMO1628771
   may show different values.
4. **Re-check Enabled** → OK

### Fix 2: Change chart to NQ (or change signal template symbol to MNQ)

**Option A (recommended):** Open a new chart on **NQ SEP26** (E-mini NASDAQ
100 Futures, not MNQ Micro), attach PraxisSignalConsumer to it with the
same params (40,80,5,15,\\Mac\praxis-signals) on account Sim101.

**Option B:** Change the signal template to `"symbol": "MNQ"` and test on
the existing MNQ chart. This changes the signal contract though.

### Verification after fixes

- Log tab must show: `PRAXIS-B1f STARTED on account 'Sim101'...`
- `\\Mac\praxis-signals\praxis-processed-signals.log` must appear
- Strategy status in Strategies tab should show Enabled, account Sim101

## Timestamps (all UTC unless noted)

| Time (UTC) | Event |
|---|---|
| 10:25:17 | NT8 session 1 connected (Sim101 + DEMO1628771) |
| 10:48:22 | NT8 session 1 shutdown |
| 10:49:03 | NT8 session 2 started |
| 10:56:46 | PRAXIS-B1f REFUSED (1st, account DEMO1628771) |
| 11:10:46 | PRAXIS-B1f REFUSED (2nd) |
| 11:16:03 | NT8 session 2 shutdown |
| 11:16:37 | NT8 session 3 started (current) |
| 11:16:53 | DEMO1628771 displayName changed to 'sim101' |
| 11:17:18 | PRAXIS-B1f REFUSED (3rd — display rename didn't help) |
| 14:35:39 | Connection lost (WebSocket abort) |
| 14:35:50 | Strategy auto-disabled (10s timeout) |
| 14:36:48 | Strategy auto-restarted → REFUSED (4th) |
| ~15:22 | Operator screenshot (11:22 AM ET) — current state |

---
*Report generated by Cowork VM agent, 2026-07-14. Honest NOT RUN — no self-certification.*
