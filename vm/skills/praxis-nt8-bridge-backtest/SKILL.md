---
name: praxis-nt8-bridge-backtest
description: Test 2a procedure for the PRAXIS VM agent — hash the strategy, read back the hand-set Strategy Analyzer tab, run only cli-nt-bridge `ntstatus` and `backtest`, and report 1190 trades / $197,327.60 exact-match or not. Use only after Z:\vm\replies holds Code's go-2a reply.
---

# praxis-nt8-bridge-backtest

Source: `Z:\vm\2026-11-06-vm-handoff.md`, step 4. The full text, settings table and citations are there; this skill is the short form. Nothing here has been tried.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## Gate
Start only if `Z:\vm\replies\` holds your `<ts>-cli-setup.md` reply and a `<ts>-CODE-go-2a.md` reply that names who sets the Strategy Analyzer tab and who reads the tab and the PRAXIS template back, and which strategy copy is meant, and Amear's step-0 words name the sim account (handoff section 2, item 5). Otherwise stop. If this skill and the handoff's step 4 disagree, STOP and reply; do not choose.

## Limits (all apply)
- Sim101 or the sim account Amear names. No live account. No orders. Nothing here runs until his words name the account (item 5).
- No connection changes (D-071): no connect, reconnect or disconnect. Do not start, close or restart NinjaTrader; if it is not running, STOP and reply.
- Only two bridge commands: `ntstatus` and `backtest`. Never `flatten`, `reconnect`, `playbackrun`, `strategies`, `ghostorders`, or any other.
- Do not install `AutoReconnect.cs`, `ChartDataSeriesSwitcher.cs` or NT8 Guard. No `pip`, no downloads, nothing bought.
- Do not edit the strategy, the PRAXIS commission template, or any `.cs` file. A difference is reported, not fixed.
- Write only under `Z:\vm\replies\` and `C:\praxis\2a-config.json`. The two bridge commands write their own request/result files under `Documents\NinjaTrader 8\NT8Bridge\`; that is expected. Never write the source title of circuit breaker #5.
- Write a `<ts>-STATUS.md` with `STARTED` first and `FINISHED` last.

## Procedure
1. Hash, and compare with the Mac hash `35393823e9bc146e95dcb1d9f6fe5785a3c72ee3a3fb71287f33fe2242752265` (ignore case and spaces):
   - `$D = [Environment]::GetFolderPath('MyDocuments')`
   - `certutil -hashfile "$D\NinjaTrader 8\bin\Custom\Strategies\PraxisNoiseAreaBreakout.cs" SHA256`
   - `certutil -hashfile Z:\ninjascript\PraxisNoiseAreaBreakout.cs SHA256`
   - Either copy differs → STOP and reply. NT8 copy missing → search `"$D\NinjaTrader 8\bin\Custom"` for it, report every path found, and STOP.
2. The person go-2a names reads the PRAXIS commission template without changing it. It must show Per unit 1.48 on the Future row and the `NQCONTROW SEP25` row (the run's own $2.96 per trade, not the amended $4.68). Otherwise STOP and reply.
3. The person go-2a names reads back every one of the 21 settings in the handoff's step 4.3 table from the open Strategy Analyzer tab; record what is read, and by whom. Any mismatch → STOP and reply; do not run.
4. `C:\praxis\2a-config.json` as in the handoff's step 4.4.
5. From `C:\praxis\bridge-src`, venv active (if `Activate.ps1` was blocked, use `.venv\Scripts\python -m nt8bridge` in place of `python -m nt8bridge`), type:
   - `python -m nt8bridge ntstatus`
   - `python -m nt8bridge backtest --config C:\praxis\2a-config.json --timeout 1800`
   - On a timeout or error: reply. Do not retry with other flags.
6. PASS only if `metrics.totalTrades` = `1190` AND `metrics.netProfit` = `197327.60` exactly. Any other number, an error or a timeout is FAIL. This is the numbers check only: whether 2a passes also waits on Amear's word on bridge NEEDS AMEAR 10 (handoff 4.6).

## Reply
File `Z:\vm\replies\<ts>-2a-result.md`, in the handoff's section 7 format, with `RESULT: DONE` and a line `2a-NUMBERS: totalTrades=<n> netProfit=<x>`. Paste: both hash outputs, the template rows, the 21 settings as read, the `ntstatus` output (including `ntVersion`), and the result JSON (`id`, `status`, `strategy`, `metrics`, and the first and last three `trades`). Code and praxis-auditor judge 2a; you do not.
