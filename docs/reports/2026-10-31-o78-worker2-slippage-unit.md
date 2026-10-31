# o78 worker 2: what NT8's "Total slippage" measures, its unit, and whether Slippage 2 lands on every market fill

**Task:** `Praxis_build-o78`, worker 2. Work out from on-disk sources only (no web, no installs) what the Strategy Analyzer Summary row "Total slippage" measures and in what unit, and whether the Analyzer setting "Slippage = 2" is applied to every market fill.
**Mode:** BUILD (read-only research). I modified nothing except this report. Scratch copies of the sqlite DBs are in `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/`.
**Criteria:** `specs/SPEC_RUBRIC.md`:
- S1: "Every claim in a report has pasted command output, not a description of output."
- S2: "No component is reported at a higher level than the evidence supports."
- S8: "No question that belongs to Amear is answered on his behalf."
- S9: "A field that parses is not a field that is honoured."

**Labels used:** OBSERVED means I saw it in command output this session. REPORTED means it is stated in a repo document and I did not re-observe it. INFERRED means it is my reasoning from observed facts. UNVERIFIED means nothing on disk supports it.

---

## Bottom line

1. **No primary NT8 text on disk defines "Total slippage" or its unit (OBSERVED).** I checked the Custom source, `Resource.resx`, `NinjaTrader.Custom.xml`, all 103 DLLs (ASCII and UTF-16) and the MSI. None contains the string "lippage". The one NT8-written artifact that mentions it is the Analyzer log XML, which stores `TotalSlippage` **separately under each PerformanceUnit** (Currency, Percent, Pips, Points, Ticks). So the displayed value depends on the display unit. Both logs on disk have `<Slippage>0</Slippage>` and TotalSlippage 0, so they cannot show what the unit conversion looks like.
2. **The old (Parallels) instrument DB holds two `NQCONT` master instruments (OBSERVED):**
   - Id 699839150754594: type 0 = **Future**, PointValue **20.0**, TickSize **0.25**, trading hours `CME US Index Futures RTH`.
   - Id 699839150754605: type 1 = **Stock**, PointValue **1.0**, TickSize **0.01**, trading hours `US Equities RTH`.

   The minute bar data is filed under the bare name `db/minute/NQCONT` (1,710 files). `db/minute/NQCONT 09-25` is empty (OBSERVED).

   Caveat: this is the **old Parallels DB** (sqlite mtime Aug 29, rescued 2026-09-29). Runs 3 and 4 ran later on Fusion. This is evidence about the old definition only.
3. **The prices are on the 0.25 grid (OBSERVED).** In the import file, 0 of 7,429,448 OHLC values are off it. It is the same file (same sha256) in the rescue root and in `b2-data`.
4. **Per-trade grid test (INFERRED):** all five reported extreme trades fit **$1/point with 0.04 of cost per round trip** on top of the $2.96 commission. All five **fail** $20/point, with or without slippage.
5. **Best reading (INFERRED):** runs 3 and 4 executed on a **Stock-typed NQCONT ($1/pt, tick 0.01)**. Under that reading:
   - "Slippage 2" means 2 × 0.01 = 0.02 price per fill.
   - "Total slippage" = 4 × 0.01 × trades. That is **both points and dollars**, because the point value is 1 (candidates ii and vi coincide).
   - Slippage cost inside run 4's net is **$48.44**, not $24,220.
   - Every price-derived $ figure in runs 3 and 4 is in $1/point, i.e. 1/20 of real NQ dollars.
6. **An anomaly is not resolved, and it caps confidence (OBSERVED arithmetic).**
   - Under that same model every trade's P&L should be a multiple of $0.25, so the totals should be too. They are not. The (net + $3.00 × n) mod 0.25 residues are 0.11 (run 3), 0.21 (run 3 long), 0.15 (run 3 short) and 0.09 (run 4).
   - The $20 model fails the same test as well.
   - Also, the extreme-trade test cannot by itself tell "0.04 slippage + 2.96 commission" apart from "trade P&L shown before all costs". Both give quarter-multiples at $1/pt.
7. **"Applies to market and stop fills, not limit fills" has no NT8 source on disk.** Its first on-disk appearance is the voice notes `:42`, inside a "Claude's estimate" bullet. Label: **UNVERIFIED (PRAXIS/Claude assertion)**.
8. **S9:** the Slippage = 2 field parses and a non-zero Total slippage is shown. That does not prove it is honoured on every fill. Nobody has yet observed a single fill price against its bar Open. **Per-fill application: UNVERIFIED.**

---

## Process log (commands and verbatim output)

### (a) Repo and ~/praxis-signals: "total slippage" hits

```
$ cd /Volumes/Sensidine/Praxis.build; echo "== repo =="; /usr/bin/grep -rIl --ignore-case --exclude-dir=.git "total slippage\|totalslippage" . ; echo "== praxis-signals =="; /usr/bin/grep -rIl --ignore-case --exclude-dir=.git "total slippage\|totalslippage" /Users/admin/praxis-signals; echo "== nt8 ref slippage =="; /usr/bin/grep -n --ignore-case "slippage" docs/reference/2026-07-24-nt8-windows-reference.md
== repo ==
./STATUS.md
./.claude/state/handoff-latest.md
./docs/reports/2026-10-31-7zq-m2-worker4-adversarial.md
./docs/reports/2026-10-31-7zq-m1-worker3-adversarial.md
./docs/reports/2026-10-30-zyd-rulings-append.md
./docs/reports/2026-10-31-7zq-m2-handtest-checklist.md
./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md
./docs/reports/2026-10-31-7zq-handtest-checklist.md
./docs/reports/2026-10-30-zyd-f3-artifact.md
./docs/reports/2026-10-28-voice-session-notes.md
./docs/reports/2026-10-30-run3-backtest-screenshot-record.md
./docs/reports/2026-10-30-zyd-worker10-closing-adversarial.md
./DECISION_LOG.md
./HANDOFF.md
./DECISIONS.md
== praxis-signals ==
== nt8 ref slippage ==
151:5. **Execution:** Include commission · Order fill resolution · Slippage (ticks) · Bars required to trade · Max bars look back · Entry handling.
```

**Classification:** all 15 repo hits are **PRAXIS commentary**. They are reports, ledgers, checklists and handoffs that quote the run-3/run-4 numbers or the open readback (hit lines are listed in the next block). There are 0 hits in `~/praxis-signals`. The NT8 reference doc `:151` says only "Slippage (ticks)", i.e. the *setting* is in ticks. It says nothing about the Summary row's unit, and it is PRAXIS-authored paraphrase citing NT8 help URLs that I did not fetch (no network). I did not read `docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md`; this report is independent of it.

```
$ /usr/bin/grep -rIn --ignore-case --exclude-dir=.git "total slippage\|totalslippage" . | cut -c1-260
[16 hit lines across the 15 files above; representative:]
./docs/reports/2026-10-28-voice-session-notes.md:54:- Slippage arithmetic (Claude's, unit unconfirmed): total slippage = trades × 4 / 100 in both runs (1,075 → 43.00; 1,211 → 48.44). This fits 2 ticks on every entry and exit (4 ticks per round trip), show
./docs/reports/2026-10-30-run3-backtest-screenshot-record.md:60:| Total slippage | **43** | 20.88 | 22.12 |
./docs/reports/2026-10-30-zyd-rulings-append.md:84:+3. Readback, open from `2026-10-30T22:22:00Z` (WHO: amear) (not a decision): does NT8 apply Slippage 2 on every market fill, and what is the unit of the Summary's "Total slippage" cell?
```

### (b) Rescued NT8 install: Custom source, DLLs, MSI, Analyzer logs

```
--- full/bin
Custom
--- full/bin/Custom
AddOns AssemblyInfo.cs BarsTypes ChartStyles DrawingTools ExportNinjaScript ImportTypes Indicators MarketAnalyzerColumns
NinjaTrader.Custom.csproj NinjaTrader.Custom.dll NinjaTrader.Custom.pdb NinjaTrader.Custom.xml NinjaTrader.Vendor.cs
NinjaTrader.Vendor.dll OptimizationFitnesses Optimizers PerformanceMetrics Resource.Designer.cs Resource.*.resx
Resource.resx ResourceEnumConverter.cs ShareServices Strategies SuperDomColumns [locale dirs]
```
(The listing is condensed onto lines; the entries are verbatim.) The rescue holds only `bin/Custom`. There is no NT8 core `bin/` (no `NinjaTrader.Core.dll` / `NinjaTrader.Gui.dll`), so the core text that would define the Summary row is not on disk.

```
$ C=".../NinjaTrader 8-full/bin/Custom"; /usr/bin/grep -rIl --ignore-case "slippage" "$C" | /usr/bin/grep -v -- "-[A-Z][A-Z]\|zh-Hans"; /usr/bin/grep -n --ignore-case -A2 "slippage" "$C/Resource.resx"; /usr/bin/grep -n --ignore-case -B2 -A3 "slippage" "$C/NinjaTrader.Custom.xml"; ls "$C/PerformanceMetrics"; /usr/bin/grep -rn --ignore-case "slippage" "$C/PerformanceMetrics"
--- grep slippage in Custom (file list, excluding locale dirs)
--- Resource.resx
--- NinjaTrader.Custom.xml
--- PerformanceMetrics
@PerformanceMetric.cs
@SampleCumProfit.cs
```
→ **0 hits** in the Custom source, `Resource.resx`, the XML doc file and PerformanceMetrics.

```
--- recursive grep incl. binaries, whole rescue NT8 dirs (file list)
--- strings ascii + utf16le on every dll
0 zlib1.dll
0 libxml2-2.dll
...
--- python utf16 scan of dlls
dlls scanned: 103
--- MSI
-rw-r--r--@  1 admin  staff    85770240 Jul  9 10:33 NinjaTrader.Install.msi
[strings -a NinjaTrader.Install.msi | grep --ignore-case lippage | head  → no output]
```
→ **0 hits** across 103 DLLs (ASCII and UTF-16LE) and in the MSI (`strings -a`). The MSI is compressed and there is no extractor on this Mac, so I stopped there, as the brief instructed.

**Analyzer log XMLs (`strategyanalyzerlogs/`).** There are two XMLs, the same in both `NinjaTrader 8-full` and `NinjaTrader 8`:
```
=== @@@PraxisNoiseAreaBreakout_2026_07_17_01.xml
22:    <FillType>Standard</FillType>
26:    <From>2026-01-01T00:00:00</From>
28:    <Instrument>NQ SEP26</Instrument>
29:    <IncludeCommission>false</IncludeCommission>
71:    <TradingHoursTemplate />
72:    <SetOrderQuantity>Strategy</SetOrderQuantity>
73:    <Slippage>0</Slippage>
74:    <SummaryPerformances>
76:        <Denomination>UsDollar</Denomination>
77:        <PerformanceUnit>Currency</PerformanceUnit>
78:        <SummaryPerformancesSerialize>...|TotalSlippage;0;0;0|TotalNumTrades;132;70;62|...
Currency | TotalSlippage ['0', '0', '0'] | Commission ['0', '0', '0'] | Trades ['132', '70', '62'] | Net ['17005', '22360', '-5355'] | LargestWin ['15165', '14120', '15165']
Percent | TotalSlippage ['0', '0', '0'] | Commission ['0', '0', '0'] | Trades ['132', '70', '62'] | Net ['17005', '22360', '-5355'] | LargestWin ['0.0252', '0.0243', '0.0252']
Pips | TotalSlippage ['0', '0', '0'] | Commission ['0', '0', '0'] | Trades ['132', '70', '62'] | Net ['17005', '22360', '-5355'] | LargestWin ['3033', '2824', '3033']
Points | TotalSlippage ['0', '0', '0'] | Commission ['0', '0', '0'] | Trades ['132', '70', '62'] | Net ['17005', '22360', '-5355'] | LargestWin ['758.25', '706', '758.25']
Ticks | TotalSlippage ['0', '0', '0'] | Commission ['0', '0', '0'] | Trades ['132', '70', '62'] | Net ['17005', '22360', '-5355'] | LargestWin ['3033', '2824', '3033']
=== @@@PraxisNoiseAreaBreakout_2026_08_29_27.xml
28:    <Instrument>NQ SEP26</Instrument>
71:    <TradingHoursTemplate>CME US Index Futures RTH</TradingHoursTemplate>
73:    <Slippage>0</Slippage>
Currency | TotalSlippage ['0', '0', '0'] | ... | Trades ['122', '65', '57'] | Net ['-4625', '-12225', '7600'] | LargestWin ['15165', '7530', '15165']
Points | TotalSlippage ['0', '0', '0'] | ... | LargestWin ['758.25', '376.5', '758.25']
Ticks | TotalSlippage ['0', '0', '0'] | ... | LargestWin ['3033', '1506', '3033']
```
What this shows:
- **OBSERVED:** NT8 serializes `TotalSlippage` once per PerformanceUnit, so the Summary value is unit-dependent.
- **OBSERVED:** for a real future (`NQ SEP26`), LargestWin is 758.25 pt in Points mode, 3033 in Ticks mode and $15,165 in Currency mode. INFERRED arithmetic from those: 758.25 / 0.25 = 3033 and 758.25 × 20 = 15,165, i.e. tick 0.25 and $20/pt are honoured *for NQ SEP26*.
- **OBSERVED:** both logs are Slippage 0 with TotalSlippage 0, so they cannot calibrate the TotalSlippage unit. Neither is a run-3 or run-4 log; no run-3 or run-4 log is on disk.

### (c) NQCONT instrument definition (old Parallels DB)

```
$ cp ".../db/NinjaTrader.sqlite" ".../db/NinjaTrader.sqlite.bak_praxis" ".../db/NinjaTrader.sqlite.bak_praxis2" "$S/" && shasum -a 256 ...
8f85d4adfaedfa7bc08e39bfb05a5948ad4f9b7293b07ac0cc7bf0aa041841e9  /Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/db/NinjaTrader.sqlite
8f85d4adfaedfa7bc08e39bfb05a5948ad4f9b7293b07ac0cc7bf0aa041841e9  /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/NinjaTrader.sqlite
TABLES: ['AccountItems', 'Accounts', 'Executions', 'Instrument2InstrumentList', 'InstrumentLists', 'Instruments', 'JournalEntries', 'Logs', 'MasterInstruments', 'OrderUpdates', 'Orders', 'Positions', 'Strategies', 'Strategy2Account', 'Strategy2Execution', 'Strategy2Instrument', 'Strategy2Order', 'User2Account', 'User2MarketDataEntitlement', 'Users', 'Versions']
COLS MasterInstruments ['Id', 'Currency', 'Description', 'InstrumentType', 'MergePolicy', 'Name', 'PointValue', 'PriceLevel', 'TickSize', 'TradingHours', 'Url', 'UserData', 'Version', 'IsServerSupported', 'AutoLiquidation']
```
The reads used `sqlite3.connect('file:...?mode=ro', uri=True)` on the scratch copies. Query: `select Id,Name,Description,InstrumentType,PointValue,TickSize,Currency,TradingHours,MergePolicy,Version from MasterInstruments where Name like "%NQ%"`.

```
=== DB NinjaTrader.sqlite            (mtime Aug 29 11:33)
MasterInstruments rows: 1858
  MI (699839150753737, 'MNQ', 'Micro E-mini Nasdaq-100 Futures', 0, 2.0, 0.25, 7, 'CME US Index Futures ETH', 3, 8582)
  MI (699839150754601, 'NNQ', 'E-nano Nasdaq-100 Index', 0, 0.2, 0.5, 7, 'CME US Index Futures ETH', 3, 10206)
  MI (135, 'NQ', 'E-mini NASDAQ 100 Futures', 0, 20.0, 0.25, 7, 'CME US Index Futures ETH', 3, 8591)
  MI (699839150754593, 'NQ', '', 1, 1.0, 0.01, 7, 'US Equities RTH', 3, 1)
  MI (699839150754594, 'NQCONT', '', 0, 20.0, 0.25, 7, 'CME US Index Futures RTH', 3, -10200)
  MI (699839150754605, 'NQCONT', '', 1, 1.0, 0.01, 7, 'US Equities RTH', 3, 1)
  MI (35, 'TRINQ', 'Nasdaq Short Term Trading Index', 2, 1.0, 0.01, 7, 'US Equities RTH', 3, 9519)
  [... Instruments rows for NQ and MNQ elided ...]
  INST (699839150770811, 'NQCONT', 23, 599266080000000000)
  INST (699839150770940, 'NQCONT', 23, 638922816000000000)
  INST (699839150770941, 'NQCONT', 9, 662353632000000000)
=== DB NinjaTrader.sqlite.bak_praxis   (mtime Jul 24 14:01)
  MI (699839150754594, 'NQCONT', '', 0, 20.0, 0.25, 7, 'CME US Index Futures RTH', 3, -10200)
  MI (699839150754596, 'NQCONT', '', 1, 1.0, 0.01, 7, 'US Equities RTH', 3, 1)
=== DB NinjaTrader.sqlite.bak_praxis2  (mtime Jul 24 14:27)
  MI (699839150754594, 'NQCONT', '', 0, 20.0, 0.25, 7, 'CME US Index Futures RTH', 3, -10200)
  MI (699839150754595, 'NQCONT', '', 1, 1.0, 0.01, 7, 'US Equities RTH', 3, 1)
```

**Type enum, checked empirically against well-known names (OBSERVED):**
```
0 ['CL', 'ES', 'NQ'] ['10YR', '1OZ', '2YR', '30YR']
1 ['AAPL', 'CL', 'ES', 'MSFT', 'NQ', 'QQQ'] ['1COV', 'A', 'AA', 'AAL']
2 ['TRINQ'] ['ADD', 'ADV', 'BRTI', 'COMP']
3 ['CL', 'ES'] ['BBAS', 'BBDC', 'BOVA', 'BVMF']
4 ['EURUSD', 'GBPUSD', 'XAUUSD'] ['AUDCAD', 'AUDCHF', 'AUDJPY', 'AUDNZD']
...
NQCONT inst (699839150770811, 699839150754594, 0, 20.0, 0.25, 23) expiry 1900-01-01
NQCONT inst (699839150770940, 699839150754594, 0, 20.0, 0.25, 23) expiry 2025-09-01
NQCONT inst (699839150770941, 699839150754605, 1, 1.0, 0.01, 9) expiry 2099-12-01
```
INFERRED from that table: 0 = Future and 1 = Stock (type 1 holds AAPL, MSFT, QQQ and the stock-style A/AA/AAL). That matches the "Stock-typed NQCONT" wording in the repo notes.

**Findings:**
- **OBSERVED:** the Stock-typed NQCONT is present in all three DB copies, each time under a **different Id** (754596, then 754595, then 754605). INFERRED: it was deleted and re-created at least once. The newest copy (Aug 29 11:33) still has it, although `docs/reports/2026-08-29-session53-vm-checks-A-and-B.md:15` REPORTS "A Stock-typed duplicate NQCONT was deleted". The deletion may have happened after 11:33; it is not settled.
- **OBSERVED:** the Future NQCONT instruments expire 1900-01-01 and 2025-09-01. That matches the REPORTED "Analyzer resolves bare NQCONT to NQCONT 09-2025 and throws unknown-instrument" (vm-checks `:13`).

Minute data location (from the call in section (d)):
```
NQCONT: 1710 files,  19M, first 20210307.Last.ncd, last 20260720.Last.ncd
NQCONT 09-25: 0 files,   0B, first , last
```
and the `db/minute` listing shows futures filed with expiry suffixes (`NQ 03-20` … `NQ 12-25`, `MNQ 09-26`) while `ADSK`, `NQ` and `NQCONT` are bare. INFERRED: NT8 files futures data under "NAME MM-YY" and non-expiring instruments under the bare name. So the 1,857,362-bar series sits where a **non-Future (Stock)** NQCONT would read it, not where `NQCONT 09-25` would. **UNVERIFIED:** no NT8 text on disk states this filing rule.

### (d) Price grid

```
307c5e8af1da42b7606d666f14e4f34228feec50d19dd52d25396aae1b16e454  /Users/admin/praxis-signals/b2-data/NQCONT.Last.txt
307c5e8af1da42b7606d666f14e4f34228feec50d19dd52d25396aae1b16e454  /Users/admin/praxis-signals/b2-data/NQ-continuous-1min.nt8import.txt
307c5e8af1da42b7606d666f14e4f34228feec50d19dd52d25396aae1b16e454  /Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/NQ 12-25.txt
20210307 180100;16120.5;16167;16120.5;16154.75;17
20210307 180200;16164.25;16164.25;16144.75;16144.75;7
20210307 180300;16145.75;16145.75;16129.75;16134.5;5
20260720 112600;29001.5;29014.75;28993.5;29002.5;587
20260720 112700;29005.5;29020.75;29003.5;29016;308
Timestamp,Open,High,Low,Close,Volume,SrcContract
2021-03-07 18:01:00,16120.5,16167,16120.5,16154.75,17,06-21
rows 1857362 first 20210307 180100 last 20260720 112700
OHLC values off 0.25 grid: 0 of 7429448 | off 0.01 grid: 0
rows with any value off 0.25: 0
per-year [rows, rows_off_0.25]: {'2021': [273470, 0], '2022': [350102, 0], '2023': [353136, 0], '2024': [353910, 0], '2025': [334110, 0], '2026': [192634, 0]}
examples off-grid: []
```
**OBSERVED:** every price is on the 0.25 grid, so the series is not back-adjusted off-grid (the CSV carries a per-row `SrcContract`, i.e. a spliced, unadjusted series). The 1,857,362-row count matches the REPORTED Fusion/VM count (vm-migration `:110`). Whether Fusion imported this exact file: **UNVERIFIED**.

**Per-trade grid test and aggregate residue (python3 -I, Decimal):**
```
== per-trade grid test (bars on 0.25 grid, market fill = bar price +/- slippage)
A Future $20/0.25, 2 ticks/side applied: (P+2.96) % 5 == 0 [('run3 largest win', False), ('run3 L largest win', False), ('run3 largest loss', False), ('run3 L largest loss', False), ('run4 largest win', False)]
B Future $20/0.25, no slippage:        (P+2.96) % 5 == 0 [('run3 largest win', False), ('run3 L largest win', False), ('run3 largest loss', False), ('run3 L largest loss', False), ('run4 largest win', False)]
C Stock $1/0.01, 2 ticks/side applied: (P+3.00) % 0.25 == 0 [('run3 largest win', True), ('run3 L largest win', True), ('run3 largest loss', True), ('run3 L largest loss', True), ('run4 largest win', True)]
D Stock $1/0.01, no slippage:          (P+2.96) % 0.25 == 0 [('run3 largest win', False), ('run3 L largest win', False), ('run3 largest loss', False), ('run3 L largest loss', False), ('run4 largest win', False)]
E Stock $1/0.01, 1 tick/side only:     (P+2.98) % 0.25 == 0 [('run3 largest win', False), ('run3 L largest win', False), ('run3 largest loss', False), ('run3 L largest loss', False), ('run4 largest win', False)]
== aggregate residue test: sum over trades of (P+3.00) mod 0.25 under model C (should be 0)
run3 net 1281.61 n 1075 (net+3.00n) mod 0.25 = 0.11 | model A (net+2.96n) mod 5 = 3.61
run3 L net 2721.21 n 522 (net+3.00n) mod 0.25 = 0.21 | model A (net+2.96n) mod 5 = 1.33
run3 S net -1439.60 n 553 (net+3.00n) mod 0.25 = 0.15 | model A (net+2.96n) mod 5 = 2.28
run4 net 3136.84 n 1211 (net+3.00n) mod 0.25 = 0.09 | model A (net+2.96n) mod 5 = 1.40
```
Inputs: run-3 figures are OBSERVED-by-master from the screenshot (`docs/reports/2026-10-30-run3-backtest-screenshot-record.md:41-73`). Run-4 figures are REPORTED by Amear (`docs/reports/2026-10-28-voice-session-notes.md:53`). The relevant record lines, pasted:
```
| Total net profit | $1,281.61 | $2,721.21 | −$1,439.60 |
| Gross profit | $35,911.01 | $17,606.91 | $18,304.10 |
| Gross loss | −$34,629.40 | −$14,885.70 | −$19,743.70 |
| Commission | $3,182.00 | $1,545.12 | $1,636.88 |
| Total slippage | **43** | 20.88 | 22.12 |
| Avg. winning trade | $87.80 | $76.89 | $101.69 |
| Largest winning trade | $580.25 | $373.00 | $580.25 |
| Largest losing trade | −$319.25 | −$318.00 | −$319.25 |
```

**What the grid test implies (INFERRED):**
- **$20/point is ruled out for the reported extreme trades.** With 0.25-grid prices and $20/pt, any trade's P&L + $2.96 must be a multiple of $5 whatever the slippage tick count. None of the five is.
- **$1/point fits all five, but only when 0.04 of cost per round trip is added on top of the $2.96 commission.** Model D (no slippage) and model E (one tick per side) fail.
- **Two limits on that.** (1) Model C reduces to "P is a multiple of 0.25". That would also hold if the Analyzer's trade P&L were shown before *all* costs, so the extremes do not uniquely prove slippage was applied. (2) The aggregates break model C: every residue is non-zero (0.09 to 0.21), so some trades' P&L is not a multiple of 0.25. The $20 model fails the aggregates too.
- **Possible causes (UNVERIFIED):** some fills not at a 0.25-grid bar price; costs inside trades differing from the Commission row; Fusion data differing from this file; or a transcription error (run 4 is REPORTED, not observed).
- **The magnitudes fit $1/pt better than $20/pt (INFERRED).** The run-3 average winner of $87.80 is 87.8 NQ points at $1/pt, or 4.39 points at $20/pt, for a ~106-minute hold. For comparison, the real `NQ SEP26` log's largest winner was 758.25 pt ($15,165).

---

## Candidate definitions of "Total slippage" (4 slippage ticks per round trip)

```
== candidate units for Total slippage, 4 slippage ticks per round trip
(i) ticks / 100                                {'run4 1211': '48.44', 'run3 1075': '43', 'run3 L 522': '20.88', 'run3 S 553': '22.12'} ALL4 MATCH
(ii) points, tick 0.01                         {'run4 1211': '48.44', 'run3 1075': '43.00', 'run3 L 522': '20.88', 'run3 S 553': '22.12'} ALL4 MATCH
(iii) points, tick 0.25                        {'run4 1211': '1211.00', 'run3 1075': '1075.00', 'run3 L 522': '522.00', 'run3 S 553': '553.00'} no
(iv) currency, tick 0.25, $20/pt ($5/tick)     {'run4 1211': '24220', 'run3 1075': '21500', 'run3 L 522': '10440', 'run3 S 553': '11060'} no
(v) currency, tick 0.01, $20/pt ($0.20/tick)   {'run4 1211': '968.80', 'run3 1075': '860.00', 'run3 L 522': '417.60', 'run3 S 553': '442.40'} no
(vi) currency, tick 0.01, $1/pt ($0.01/tick)   {'run4 1211': '48.44', 'run3 1075': '43.00', 'run3 L 522': '20.88', 'run3 S 553': '22.12'} ALL4 MATCH
(vii) raw ticks                                {'run4 1211': '4844', 'run3 1075': '4300', 'run3 L 522': '2088', 'run3 S 553': '2212'} no
(viii) currency, tick 0.25, $1/pt              {'run4 1211': '1211.00', 'run3 1075': '1075.00', 'run3 L 522': '522.00', 'run3 S 553': '553.00'} no
```

| Rank | Candidate | All four numbers | Fits the on-disk instrument def | Fits the per-trade grid test | Verdict |
|---|---|---|---|---|---|
| 1 | **(ii) points at tick 0.01 ≡ (vi) currency at tick 0.01, $1/pt** | ✓ all four | ✓ the Stock NQCONT (1.0 / 0.01) exists on disk | ✓ all 5 extremes (model C); ✗ aggregate residue | **Best reading, INFERRED** |
| 2 | (i) ticks / 100 | ✓ all four | No unit like this appears on disk. The XML units are Currency, Percent, Pips, Points, Ticks | n/a | Numerically equal to (ii) only because tick = 0.01. Not a known NT8 unit (UNVERIFIED) |
| — | (iii) points at 0.25, (iv) currency $20/0.25, (v) $20 at 0.01, (vii) raw ticks, (viii) $1 at 0.25 | ✗ | (iii)/(iv) would be the Future NQCONT | (iv) fails all 5 extremes | Rejected |

Readings (ii) and (vi) are indistinguishable when the point value is 1: points equal dollars. The run-3 screenshot shows "43" with no `$`, while the $ rows carry `$` (REPORTED: voice notes `:48`, "NT8 shows no unit"). That weakly favours points, but the number is the same either way.

**$ cost of slippage inside run 4's net:**
```
slippage $ if Stock $1/0.01: 48.44 | if Future $20/0.25: 24220 | if 0.01 tick at $20: 968.80
run4 sum of price moves under C (net+comm+slip) = 6769.84 points; x$20 = 135396.80 ; x$20 minus $20/RT slip minus comm = 107592.24
run3 same = 4506.61 points; avg winner $87.80 = 87.80 pts at $1 vs 4.39 pts at $20
```
- **Best reading (INFERRED):** slippage cost = **$48.44**. The locked "2 ticks/side, $10/side" assumption (DECISION_LOG `:442`) was therefore **not** what was simulated. It was 0.02 pt/side, about 8% of one real NQ tick.
- **Alternatives:** $24,220 if it really was the $20/0.25 Future with every fill slipped (inconsistent with every displayed number). $968.80 at 0.01 tick and $20/pt (inconsistent with the per-trade test).
- **Arithmetic only:** if model C held, run 4's price moves total 6,769.84 points. At real NQ terms ($20/pt, $20/RT slippage, $3,584.56 commission) that is about $107,592. **This figure inherits the unresolved aggregate residue. It is not a result, and what it means is Amear's call (S8).**

---

## Origin of "NT8 Analyzer slippage applies to market and stop fills, not limit fills"

```
$ /usr/bin/grep -rIn --ignore-case --exclude-dir=.git "slippage[^.|]*limit\|limit[^.|]*slippage\|not limit fills\|stop-market fills\|market and stop" . /Users/admin/praxis-signals | cut -c1-330 | head -30
./docs/reports/2026-10-30-3gm-worker2-timing-orders-count.md:60:- Run 3 cost arithmetic (Claude's estimate): ... In NT8 the Analyzer slippage applies to market and stop fills, not limit fills,
./docs/reports/2026-10-28-voice-session-notes.md:42:- Run 3 cost arithmetic (Claude's estimate): ... In NT8 the Analyzer slippage applies to market and stop fills, not limit fills, so check whi
./Redemtion/Research Results/2nd round/compass_artifact_wf-ee42cda6-0085-4b1e-a813-4f4221d90a63_text_markdown.md:47:  - Slippage = 1 tick on entry (stop fills), 0 on bracket exits (they're limits/stops at the exchange).
[other hits: the "Fills are optimistic … 2 ticks/side slippage assumed" limitation sentence and cost-model notes — unrelated]
-- 4uu file slippage lines
43:6. **Stamp-vs-fill divergence.** NT8 fills managed market entries at the **next bar's open**, whereas the paper acts *at* the stamp price. ...
-- git log first appearance of the claim
[no output]
```
- **OBSERVED:** the claim's earliest on-disk appearance is the voice notes `:42`, inside a bullet titled "Run 3 cost arithmetic (Claude's estimate)". The 3gm worker-2 report `:60` quotes it verbatim.
- **OBSERVED:** the 4uu checklist mentions only "next bar's open" market fills. Nothing on disk (the NT8 reference doc, the Custom source, 103 DLLs, the MSI, the log XMLs) states which order types the Slippage setting applies to. The `Redemtion` hit is a third-party research artifact about a bracket design, not NT8 text.
- `git log -S` on the voice notes returned nothing, so I could not date the text to a commit.
- **Label: UNVERIFIED — PRAXIS/Claude assertion, no NT8 source on disk.**

**S9:** "A field that parses is not a field that is honoured." What is OBSERVED/REPORTED is `Slippage 2` in the settings and a non-zero Total slippage. Whether 2 ticks land on **every** market fill, or on any given fill, is **UNVERIFIED** until one fill price is read against its bar Open. The aggregate residue makes that observation more necessary, not less.

---

## Readbacks for Amear (his to perform and rule on; I have answered none of them)

1. **Fusion, `Tools > Instruments`, filter `NQCONT` (and `NQ`).** For **every** row, read Type, Tick size, Point value, Currency, Trading hours and Expiry. Also read the exact text in the Strategy Analyzer's Instrument field for run 4. Does it name the Stock or the Future NQCONT?
2. **One run-4 trade (Trades tab):** the entry price vs the **Open of the bar after the signal bar**. Expected for a long entry: **+0.50 pt** if tick 0.25 and Slippage 2 are honoured; **+0.02 pt** if tick 0.01; **+0.00** if slippage is not applied. A short entry is the mirror (−). Do the same for that trade's exit. A price ending in a non-quarter (e.g. .27 or .52) shows the 0.01 tick directly.
3. **The same trade's Profit:** does it equal (exit − entry) × 1 − $2.96, or × 20 − $2.96? That separates $1/pt from $20/pt on a single fill.
4. **"Total slippage" unit:** hover for a tooltip or open help on the Summary row if NT8 offers one. Then switch the Analyzer's display unit (Currency → Points → Ticks) and read Total slippage in each. The on-disk XML shows NT8 stores TotalSlippage per unit, so this one switch settles the unit. Expected if the best reading holds: Points 48.44 and Ticks 4,844.
5. **(Optional) aggregate residue:** export the run-4 Trades list, so that one can check whether any trade's P&L is not a multiple of $0.25 and which trades they are.

---

## Verification evidence

All command output is pasted inline above, under "Process log", "Candidate definitions" and "Origin". There are no tests to run; this is read-only research.

## Files staged

None. This report is written and not staged (no `git add`, per the brief).

Result: PASS


---

## Manager correction note (2026-10-31, appended; nothing above was edited)

The adversarial worker `docs/reports/2026-10-31-o78-worker3-adversarial.md` raised findings F3, F7 and F8 against this report. They are accepted, and the manager report `docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md` carries the corrected text. Where this report conflicts with W3 F3/F7/F8, W3 governs:
- **F3 (MAJOR, S2):** bottom line 1's "TotalSlippage is stored per PerformanceUnit, so the displayed value depends on the display unit" is **withdrawn**. The log XML repeats every field under each unit, including fields that never change (TotalNetProfit 17005 in all five). There is no `TotalSlippageValue` twin. Readback 4 is amended: if Total slippage reads the same in every display unit, the switch does **not** settle the unit.
- **F7 (MINOR, S2):** the mapping "type 0 = Future, type 1 = Stock" is INFERRED (from AAPL, MSFT and QQQ; type 1 holds 1,040 rows, all PointValue 1.0), not OBSERVED.
- **F8 (MINOR):** the run-4 largest winner matches one import-file trade to the cent after 3.00 of costs: 2025-04-09, long, 12:31 open 18,691.25 → 16:00 close 20,486.75. "P&L before all costs" would show 1,795.50, so it is disfavoured for that trade. INFERRED; assumes the Fusion data is the import file.
