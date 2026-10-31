# a9d worker 1: why the Future `NQCONT` row has no bars (research only)

> Revised 2026-10-31 by a9d worker 4 after the adversarial review (findings 1-13) in `docs/reports/2026-10-31-a9d-adversarial.md`. Corrections are marked in place as **CORRECTED (a9d worker 4, finding N)** with the old text quoted; grades were only lowered, never raised.

- **Unit:** `Praxis_build-a9d`, worker 1 of praxis-manager. **Mode:** BUILD (research only). No NT8, no web, no backtest, no code change, nothing staged.
- **Date:** 2026-10-31.
- **Grades:** OBSERVED = read from disk in this session, shown below. REPORTED = Amear or a prior record says so. INFERRED = my reasoning from the observed facts. SPEC-SILENT = no on-disk source covers it. UNVERIFIED = a claim that has not been checked.
- **Which install this is about. Read this first.** Every OBSERVED NT8 fact below comes from the **rescued OLD Parallels install** (`/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/`, read-only). Its sqlite file has mtime Aug 29 11:33, and its logs stop on 2026-08-29. **None of it was read from Amear's current Fusion VM.** The voice notes say Fusion shows the same two rows (REPORTED). Every statement about Fusion is therefore INFERRED, and a readback on Fusion is needed to confirm it.
- **Method:** each command list sits in a scratchpad script. It ran as `bash -v <script> 2>&1 | tee <script>.out`, and `bash -v` echoes each script line before its output. Python ran as `python3 -I <file>.py 2>&1 | tee <file>.out`. The sqlite file was opened with URI `file:...?mode=ro&immutable=1`. The `.bak_praxis*` files were never opened. The evidence blocks were spliced in from those `.out` files by an awk splicer. Nothing in them was retyped.
- **Windows `\r` disclosure:** the sqlite `CREATE TABLE` text contains CR characters. `schema.py` prints them as a literal `\r`. **CORRECTED (a9d worker 4, finding 8).** Old: "The NT8 log and trace files are CRLF (see the `od -c` in Q1 evidence C)". That `od -c` is in Q2 Evidence A, and it ran on `Install.xml`, not on a log or trace file. New: The NT8 log `.txt` files are CRLF (`od -c` of `log.20260829.00000.en.txt`, pasted in `docs/reports/2026-10-31-a9d-adversarial.md` finding 8). The trace files were not checked byte-wise; their first 64 bytes contain no line end. Every log or trace extract below was piped through `tr -d '\r'` anyway. In the import file, the first 48 bytes of row 1 contain no `\r` (Q6 `od -c`). The rest of that line was not checked.

Scratchpad: `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/w1/`

---

## Q1. With two rows named `NQCONT`, where does an import of `NQCONT.Last.txt` land?

**Answer.**
1. **OBSERVED (rescued install):** the imported minute data is filed in `db/minute/NQCONT/`. That folder holds 1,710 files, `20210307.Last.ncd` through `20260720.Last.ncd`, all with mtime Aug 29 11:43. The Future contract-month folder `db/minute/NQCONT 09-25/` exists and is **empty** (0 entries, mtime Aug 29 10:00). `db/day/NQCONT` and `db/day/NQCONT 09-25` are both empty.
   - **ADDED (a9d worker 4, finding 12).** All 1,710 `.ncd` files carry mtime `Aug 29 11:43:45`, ten minutes **after** the sqlite's last write (`11:33:53`). No log or trace line mentions an import between 11:34:06 and 11:47:58 (OBSERVED, `docs/reports/2026-10-31-a9d-adversarial.md` finding 12). What wrote the folder at 11:43:45 is INFERRED (a re-import), and it left no Log line. So an empty Log after an import is not evidence of success.
2. **OBSERVED (sqlite, rescued):** two `MasterInstruments` rows are named `NQCONT`:
   - Id `699839150754594`: `InstrumentType 0`, PointValue 20.0, TickSize 0.25, `CME US Index Futures RTH`, MergePolicy 3. It owns two `Instruments` rows, with Expiry ticks `599266080000000000` (1900-01-01) and `638922816000000000` (2025-09-01).
   - Id `699839150754605`: `InstrumentType 1`, PointValue 1.0, TickSize 0.01, `US Equities RTH`, MergePolicy 3. It owns one `Instruments` row, Expiry 2099-12-01.

   A Stock-typed `NQ` row (Id `…593`, type 1, PV 1, tick 0.01) also exists. The tick-to-date conversion is in Q1 evidence C.
3. **INFERRED (decode of an undocumented blob):** the Future master's `UserData` blob holds the pair 2025-09-01 / 2025-12-01 at byte offsets 242/250. This matches session 53's REPORTED `Expiry 09-25, Rollover date 12-01-2025`. That makes it the single rollover row: contract month 09-25, rollover date 2025-12-01. The 8 bytes after it read as a double are NaN.
4. **INFERRED (strong):** the folder key is the instrument's **full-name string**. No master Id appears in the path. For a Future, the full name includes a month. The evidence:
   - Every downloaded NQ future is filed under `NQ MM-YY`.
   - The `NQ` folder, which carries the bare name of the Stock-typed `NQ` row, is empty.
   - `NQCONT 09-25` was created at Aug 29 10:00, the same minute the log records `Unknown instrument 'NQCONT 09-25'` (10:00:22).
   - Reference §2 says minute data lands in `db\minute\<instrument>\`.

   So bars imported from a file named `NQCONT.Last.txt` sit under the name `NQCONT`. That is the full name of the **Stock** row. The Future row's only dated name is `NQCONT 09-25`, and that folder is empty. **The Future row has no bars because none were ever filed under any of its contract names.** Amear's REPORTED run 0-S slippage of 48.44 = 1,211 × 4 × 0.01 (voice notes) agrees: those runs used a 0.01 tick, which is the Stock row.

   **ADDED (a9d worker 4, finding 6).** The alternative, that the Future's 1900-01-01 row (`699839150770811`) is named bare `NQCONT` and so owns the folder, is ruled out INFERRED (moderate). Three picker entries (`NQCONT`, `NQCONT SEP25`, `NQCONT ##-##`, REPORTED) match three `Instruments` rows (OBSERVED, Evidence C). The Stock row's only row is 2099, and `##-##` is therefore the 1900 row. No source states the 1900 row's full name. The one type-1 master that owns a 1900 row is `MHI`, unrelated (OBSERVED, `docs/reports/2026-10-31-a9d-adversarial.md` finding 6).
5. **REPORTED:** session 53 recorded Amear's observation: "Data is filed under the exact bare name NQCONT … in db\minute\NQCONT". Session 52 reached the same INFERRED diagnosis (report lines 84-90).
6. **Not decidable from disk (SPEC-SILENT):** NT8 has two masters that share the name `NQCONT`. No source says which of them "owns" the folder. The folder is only a name.
7. **For Fusion:** the same layout is INFERRED, not OBSERVED.

**Evidence A: minute folders, counts, mtimes, `NQCONT` and `NQCONT 09-25` contents, `du`, db root.** Command as run: `bash -v q1a.sh 2>&1 | tee q1a.out`
````text
R="/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full"
ls -la "$R/db/minute/"
total 0
drwxr-xr-x@   36 admin  staff   1152 Aug 29 10:00 .
drwxr-xr-x@   12 admin  staff    384 Jul 24 14:32 ..
drwxr-xr-x@    2 admin  staff     64 Aug 29 09:49 ADSK
drwxr-xr-x@    2 admin  staff     64 Jul 14 14:45 CL 08-26
drwxr-xr-x@    8 admin  staff    256 Jul 14 15:25 MGC 08-26
drwxr-xr-x@   32 admin  staff   1024 Aug 29 11:02 MNQ 09-26
drwxr-xr-x@    2 admin  staff     64 Jul 20 11:26 NQ
drwxr-xr-x@   70 admin  staff   2240 Jul 19 07:17 NQ 03-20
drwxr-xr-x@   89 admin  staff   2848 Jul 19 07:17 NQ 03-21
drwxr-xr-x@   92 admin  staff   2944 Jul 21 12:43 NQ 03-22
drwxr-xr-x@   86 admin  staff   2752 Jul 21 12:45 NQ 03-23
drwxr-xr-x@   94 admin  staff   3008 Jul 21 12:45 NQ 03-24
drwxr-xr-x@   92 admin  staff   2944 Jul 21 12:46 NQ 03-25
drwxr-xr-x@   69 admin  staff   2208 Aug 29 10:40 NQ 03-26
drwxr-xr-x@   90 admin  staff   2880 Jul 19 07:17 NQ 06-20
drwxr-xr-x@   99 admin  staff   3168 Jul 19 07:17 NQ 06-21
drwxr-xr-x@   94 admin  staff   3008 Jul 21 12:43 NQ 06-22
drwxr-xr-x@   90 admin  staff   2880 Jul 21 12:45 NQ 06-23
drwxr-xr-x@   96 admin  staff   3072 Jul 21 12:45 NQ 06-24
drwxr-xr-x@   92 admin  staff   2944 Jul 21 12:46 NQ 06-25
drwxr-xr-x@   80 admin  staff   2560 Jul 17 14:40 NQ 06-26
drwxr-xr-x@   92 admin  staff   2944 Jul 19 07:17 NQ 09-20
drwxr-xr-x@  101 admin  staff   3232 Jul 19 07:17 NQ 09-21
drwxr-xr-x@   97 admin  staff   3104 Jul 21 12:43 NQ 09-22
drwxr-xr-x@   89 admin  staff   2848 Jul 21 12:45 NQ 09-23
drwxr-xr-x@   88 admin  staff   2816 Jul 21 12:46 NQ 09-24
drwxr-xr-x@   91 admin  staff   2912 Jul 21 12:46 NQ 09-25
drwxr-xr-x@   42 admin  staff   1344 Aug 29 10:30 NQ 09-26
drwxr-xr-x@   87 admin  staff   2784 Jul 19 07:17 NQ 12-20
drwxr-xr-x@   75 admin  staff   2400 Jul 21 12:43 NQ 12-21
drwxr-xr-x@   94 admin  staff   3008 Jul 21 12:43 NQ 12-22
drwxr-xr-x@   91 admin  staff   2912 Jul 21 12:45 NQ 12-23
drwxr-xr-x@   92 admin  staff   2944 Jul 21 12:46 NQ 12-24
drwxr-xr-x@   92 admin  staff   2944 Jul 21 12:46 NQ 12-25
drwxr-xr-x@ 1712 admin  staff  54784 Aug 29 11:43 NQCONT
drwxr-xr-x@    2 admin  staff     64 Aug 29 10:00 NQCONT 09-25
for d in "$R"/db/minute/*/; do printf '%s\t' "$(basename "$d")"; ls -1 "$d" | wc -l; done
ADSK	       0
CL 08-26	       0
MGC 08-26	       6
MNQ 09-26	      30
NQ 03-20	      68
NQ 03-21	      87
NQ 03-22	      90
NQ 03-23	      84
NQ 03-24	      92
NQ 03-25	      90
NQ 03-26	      67
NQ 06-20	      88
NQ 06-21	      97
NQ 06-22	      92
NQ 06-23	      88
NQ 06-24	      94
NQ 06-25	      90
NQ 06-26	      78
NQ 09-20	      90
NQ 09-21	      99
NQ 09-22	      95
NQ 09-23	      87
NQ 09-24	      86
NQ 09-25	      89
NQ 09-26	      40
NQ 12-20	      85
NQ 12-21	      73
NQ 12-22	      92
NQ 12-23	      89
NQ 12-24	      90
NQ 12-25	      90
NQ	       0
NQCONT 09-25	       0
NQCONT	    1710
ls -la "$R/db/minute/NQCONT 09-25/"
total 0
drwxr-xr-x@  2 admin  staff    64 Aug 29 10:00 .
drwxr-xr-x@ 36 admin  staff  1152 Aug 29 10:00 ..
ls -1 "$R/db/minute/NQCONT/" | head -5
20210307.Last.ncd
20210308.Last.ncd
20210309.Last.ncd
20210310.Last.ncd
20210311.Last.ncd
ls -1 "$R/db/minute/NQCONT/" | tail -5
20260715.Last.ncd
20260716.Last.ncd
20260717.Last.ncd
20260719.Last.ncd
20260720.Last.ncd
ls -1 "$R/db/minute/NQCONT/" | wc -l
    1710
du -sh "$R/db/minute/NQCONT/"
 19M	/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/db/minute/NQCONT/
ls -la "$R/db/"
total 26320
drwxr-xr-x@  12 admin  staff      384 Jul 24 14:32 .
drwxr-xr-x@  20 admin  staff      640 Jul 24 07:56 ..
-rw-r--r--@   1 admin  staff  4505600 Aug 29 11:33 NinjaTrader.sqlite
-rw-r--r--@   1 admin  staff  4485120 Jul 24 14:01 NinjaTrader.sqlite.bak_praxis
-rw-r--r--@   1 admin  staff  4485120 Jul 24 14:27 NinjaTrader.sqlite.bak_praxis2
drwxr-xr-x@   7 admin  staff      224 Aug 29 09:54 cache
drwxr-xr-x@ 256 admin  staff     8192 Aug 29 11:35 day
drwxr-xr-x@   2 admin  staff       64 Jul  9 10:37 messages
drwxr-xr-x@  36 admin  staff     1152 Aug 29 10:00 minute
drwxr-xr-x@   2 admin  staff       64 Jul  9 10:37 replay
drwxr-xr-x@   2 admin  staff       64 Jul  9 10:37 snapshot
drwxr-xr-x@   2 admin  staff       64 Aug 29 09:59 tick
ls -la "$R/db/minute/NQ/"
total 0
drwxr-xr-x@  2 admin  staff    64 Jul 20 11:26 .
drwxr-xr-x@ 36 admin  staff  1152 Aug 29 10:00 ..
````

**Evidence B: sqlite table names and schemas (read-only).** Command as run: `python3 -I schema.py 2>&1 | tee schema.out`
````text
TABLE AccountItems rows=75
    CREATE TABLE AccountItems\r 										(\r 											Account		integer not null references Accounts on delete cascade,\r 											Currency	integer,\r 											ItemType	integer,\r 											Value		real,\r 											TimeUtc		integer,\r 											primary key (Account, ItemType, Currency)\r 										)
TABLE Accounts rows=4
    CREATE TABLE Accounts\r 										(\r 											Id						integer not null primary key,\r 											Denomination			integer,\r 											ForexLotSize			integer,\r 											Name					text,\r 											Provider				integer,\r 											SimulatorDelayExchange	integer,\r 											SimulatorDelayInternet	integer,\r 											SimulatorInitialCash	real,\r 											Commission				text,\r 											DisplayName				text(250),\r 											Fcm						text,\r 											Risk					text,\r 											MinimumCashValue		real,\r 											PrimaryUser				integer,\r 											AccountStatus			int,\r 											LossLimit				real,\r 											Fee						text(50),\r 											MarginMultiplier		real,\r 											MaxOrderSize			int,\r 											MaxPositionSize			int,\r 											Data					blob,\r 											LiquidationState		int\r 										)
TABLE Executions rows=14
    CREATE TABLE Executions\r 										(\r 											Id					integer not null primary key,\r 											Account				integer not null references Accounts on delete cascade,\r 											BarIndex			integer,\r 											Commission			real,\r 											Exchange			integer,\r 											ExecutionId			text not null,\r 											Fee					real,\r 											Instrument			integer not null references Instruments on delete cascade,\r 											IsEntry				integer,\r 											IsEntryStrategy		integer,\r 											IsExit				integer,\r 											IsExitStrategy		integer,\r 											LotSize				integer,\r 											MarketPosition		integer,\r 											MaxPrice			real,\r 											MinPrice			real,\r 											Name				text,\r 											OrderId				text,\r 											Position			integer,\r 											PositionStrategy	integer,\r 											Price				real,\r 											Quantity			integer,\r 											Rate				real,\r 											StatementDate		integer,\r 											Time				integer,\r 											ServerName			text(20)\r 										)
TABLE Instrument2InstrumentList rows=777
    CREATE TABLE Instrument2InstrumentList\r 										(\r 											Instrument		integer not null references Instruments on delete cascade,\r 											InstrumentList	integer not null references InstrumentLists on delete cascade,\r 											primary key (Instrument, InstrumentList)\r 										)
TABLE InstrumentLists rows=11
    CREATE TABLE InstrumentLists\r 										(\r 											Id			integer not null primary key,\r 											Name		text,\r 											Version		integer,\r 											IsWebOnly	integer\r 										)
TABLE Instruments rows=32129
    CREATE TABLE Instruments\r 										(\r 											Id					integer not null primary key,\r 											Exchange			integer,\r 											Expiry				integer,\r 											MasterInstrument	integer not null references MasterInstruments on delete cascade,\r 											[Right]				integer,\r 											StrikePrice			real\r 										)
TABLE JournalEntries rows=0
    CREATE TABLE JournalEntries\r 										(\r 											Id			integer not null primary key,\r 											Execution	integer references Executions on delete cascade,\r 											Text		blob,\r 											Time		integer\r 										)
TABLE Logs rows=0
    CREATE TABLE Logs\r 										(\r 											Account			integer not null,\r 											LogCategory		int,\r 											LogLevel		int,\r 											Message			blob,\r 											Time			integer,\r 											User			integer not null,\r 											ServerName		text(20)\r 										)
TABLE MasterInstruments rows=1858
    CREATE TABLE MasterInstruments\r 										(\r 											Id					integer not null primary key,\r 											Currency			integer,\r 											Description			text,\r 											InstrumentType		integer,\r 											MergePolicy			integer,\r 											Name				text not null,\r 											PointValue			real,\r 											PriceLevel			real,\r 											TickSize			real,\r 											TradingHours		text,\r 											Url					text,\r 											UserData			blob,\r 											Version				integer,\r 											IsServerSupported	integer,\r 											AutoLiquidation		integer\r 										)
TABLE OrderUpdates rows=117
    CREATE TABLE OrderUpdates\r 										(\r 											[Order]			integer not null references Orders on delete cascade,\r 											Nr				integer not null,\r 											AvgFillPrice	real,\r 											Comment			text,\r 											Error			integer,\r 											Filled			integer,\r 											LimitPrice		real,\r 											OrderId			text,\r 											OrderState		integer,\r 											Quantity		integer,\r 											StatementDate	integer,\r 											StopPrice		real,\r 											Time			integer,\r 											ServerName		text(20),\r 											primary key ([Order], Nr)\r 										)
TABLE Orders rows=24
    CREATE TABLE Orders\r 										(\r 											Id				integer not null primary key,\r 											Account			integer not null references Accounts on delete cascade,\r 											AvgFillPrice	real,\r 											Data			blob,\r 											Filled			integer,\r 											Gtd				integer,\r 											Instrument		integer not null references Instruments on delete cascade,\r 											Name			text,\r 											LimitPrice		real,\r 											Oco				text,\r 											OrderAction		integer,\r 											OrderEntry		integer,\r 											OrderId			text,\r 											OrderType		integer,\r 											OrderState		integer,\r 											Quantity		integer,\r 											StatementDate	integer,\r 											StopPrice		real,\r 											Time			integer,\r 											TimeInForce		integer\r 										)
TABLE Positions rows=0
    CREATE TABLE Positions\r 										(\r 											Account			integer not null references Accounts on delete cascade,\r 											Instrument		integer not null references Instruments on delete cascade,\r 											AvgPrice		real,\r 											MarketPosition	integer,\r 											Quantity		integer,\r 											StatementDate	integer\r 										)
TABLE Strategies rows=5
    CREATE TABLE Strategies\r 										(\r 											Id						integer not null primary key,\r 											Category				integer,\r 											Classname				text,\r 											IsReplay				integer,\r 											IsResetOnNewTradingDay	integer,\r 											IsTerminal				integer,\r 											Name					text,\r 											ServerId				integer,\r 											Template				text,\r 											Userdata				blob,\r 											Workspace				text\r 										)
TABLE Strategy2Account rows=5
    CREATE TABLE Strategy2Account\r 										(\r 											Account		integer not null references Accounts on delete cascade,\r 											Strategy	integer not null references Strategies on delete cascade,\r 											Nr			integer not null,\r 											primary key (Strategy, Account)\r 										)
TABLE Strategy2Execution rows=11
    CREATE TABLE Strategy2Execution\r 										(\r 											Execution	integer not null references Executions on delete cascade,\r 											Strategy	integer not null references Strategies on delete cascade,\r 											primary key (Strategy, Execution)\r 										)
TABLE Strategy2Instrument rows=5
    CREATE TABLE Strategy2Instrument\r 										(\r 											Instrument	integer not null references Instruments on delete cascade,\r 											Strategy	integer not null references Strategies on delete cascade,\r 											Nr			integer not null,\r 											primary key (Strategy, Instrument, Nr)\r 										)
TABLE Strategy2Order rows=23
    CREATE TABLE Strategy2Order\r 										(\r 											[Order]		integer not null references Orders on delete cascade,\r 											Strategy	integer not null references Strategies on delete cascade,\r 											primary key (Strategy, [Order])\r 										)
TABLE User2Account rows=0
    CREATE TABLE User2Account\r 										(\r 											Account		integer not null references Accounts on delete cascade,\r 											User		integer not null references Users on delete cascade,\r 											IsViewOnly	integer\r 										)
TABLE User2MarketDataEntitlement rows=0
    CREATE TABLE User2MarketDataEntitlement\r 										(\r 											MarketData				integer,\r 											MarketDataEntitlement	text(250) not null,\r 											MarketDepth				integer,\r 											User					integer not null references Users on delete cascade\r 										)
TABLE Users rows=0
    CREATE TABLE Users\r 										(\r 											Id								integer not null primary key,\r 											IsMonitor						integer,\r 											Name							text,\r 											Password						text,\r 											Salt							text,\r 											ManagesAllAccounts				integer,\r 											MaxConcurrentLogins				integer,\r 											Address							text(100),\r 											CanManageAccounts				integer,\r 											CanManageMessages				integer,\r 											CanManagePermissions			integer,\r 											CanManagePlatform				integer,\r 											CanManageRisk					integer,\r 											CanManageTreasury				integer,\r 											CanManageUsers					integer,\r 											City							text(100),\r 											Country							text(100),\r 											Email1							text(100),\r 											Email2							text(100),\r 											FirstName						text(100),\r 											LastName						text(100),\r 											PostalCode						text(20),\r 											State							text(100),\r 											IsEnabled						integer,\r 											IsProfessional					integer,\r 											NumSimulationAccounts			int,\r 											ApiRateMultiplier				real,\r 											MaxMarketDataSubscriptions		int,\r 											MaxMarketDepthSubscriptions		int,\r 											CanRunReports					integer,\r 											UserData						blob,\r 											CanViewAccounts					integer,\r 											CanViewUsers					integer,\r 											Email3							text(100),\r 											Company							text(100),\r 											CqgPurchaseEligible				integer,\r 											Description						text(250),\r 											Phone							text(30),\r 											ManagedProvider					int,\r 											CreatedByProvider				int,\r 											RegisteredTime					integer,\r 											ExpirationTime					integer,\r 											Auth0UserId						text(100)\r 										)
TABLE Versions rows=78
    CREATE TABLE Versions\r 										(\r 											Version		integer not null primary key,\r 											Updated		integer\r 										)
````

**Evidence C: NQCONT and NQ instrument rows.** Command as run: `python3 -I inst.py 2>&1 | tee inst.out`. The block below stops at the `== UserData` header. The splicer trimmed the output with `awk '/== UserData/{exit} {print}' inst.out | tee inst_trim.out`, because the raw UTF-8 decode of the binary blob prints NUL bytes. The same blob is shown cleanly as hex in Evidence D.
````text
== MasterInstruments with Name in (NQ, NQCONT, MNQ) or like NQCONT%
{'Id': 699839150753737, 'Name': 'MNQ', 'InstrumentType': 0, 'PointValue': 2.0, 'TickSize': 0.25, 'MergePolicy': 3, 'TradingHours': 'CME US Index Futures ETH', 'Description': 'Micro E-mini Nasdaq-100 Futures', 'Version': 8582, 'len(UserData)': 1244}
{'Id': 135, 'Name': 'NQ', 'InstrumentType': 0, 'PointValue': 20.0, 'TickSize': 0.25, 'MergePolicy': 3, 'TradingHours': 'CME US Index Futures ETH', 'Description': 'E-mini NASDAQ 100 Futures', 'Version': 8591, 'len(UserData)': 2888}
{'Id': 699839150754593, 'Name': 'NQ', 'InstrumentType': 1, 'PointValue': 1.0, 'TickSize': 0.01, 'MergePolicy': 3, 'TradingHours': 'US Equities RTH', 'Description': '', 'Version': 1, 'len(UserData)': 246}
{'Id': 699839150754594, 'Name': 'NQCONT', 'InstrumentType': 0, 'PointValue': 20.0, 'TickSize': 0.25, 'MergePolicy': 3, 'TradingHours': 'CME US Index Futures RTH', 'Description': '', 'Version': -10200, 'len(UserData)': 278}
{'Id': 699839150754605, 'Name': 'NQCONT', 'InstrumentType': 1, 'PointValue': 1.0, 'TickSize': 0.01, 'MergePolicy': 3, 'TradingHours': 'US Equities RTH', 'Description': '', 'Version': 1, 'len(UserData)': 246}
== distinct InstrumentType values across MasterInstruments (type, count, example name)
(0, 366, '10YR')
(1, 1040, '1COV')
(2, 52, 'ADD')
(3, 13, 'BBAS')
(4, 64, 'AUDCAD')
(5, 262, 'ADIDAS')
(7, 61, 'ADABTC')
== distinct MergePolicy values across MasterInstruments (policy, count)
(0, 1)
(3, 1857)
== Instruments rows (contracts) per master
MNQ master Id 699839150753737 instrument rows: 35
    (699839150755443, 23, 599266080000000000, 99, 0.0)
    (699839150755426, 23, 636949440000000000, 99, 0.0)
    (699839150755427, 23, 637028928000000000, 99, 0.0)
    ...
    (699839150768171, 23, 639394560000000000, 99, 0.0)
    (699839150768172, 23, 639474048000000000, 99, 0.0)
    (699839150768173, 23, 639553536000000000, 99, 0.0)
NQ master Id 135 instrument rows: 94
    (136, 23, 599266080000000000, 99, 0.0)
    (6373, 23, 632452320000000000, 99, 0.0)
    (6374, 23, 632531808000000000, 99, 0.0)
    ...
    (699839150764690, 23, 639553536000000000, 99, 0.0)
    (699839150764691, 23, 639632160000000000, 99, 0.0)
    (699839150764692, 23, 639790272000000000, 99, 0.0)
NQ master Id 699839150754593 instrument rows: 1
    (699839150770809, 9, 662353632000000000, 99, 0.0)
NQCONT master Id 699839150754594 instrument rows: 2
    (699839150770811, 23, 599266080000000000, 99, 0.0)
    (699839150770940, 23, 638922816000000000, 99, 0.0)
NQCONT master Id 699839150754605 instrument rows: 1
    (699839150770941, 9, 662353632000000000, 99, 0.0)
````

**Evidence D: NQCONT file mtimes, day folders, tick-to-date conversion, and the Future master's rollover blob as hex.** Commands as run: `bash -v q1b.sh 2>&1 | tee q1b.out`, then `python3 -I blob.py 2>&1 | tee blob.out`
````text
R="/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full"
ls -la "$R/db/minute/NQCONT/" | head -6
total 39088
drwxr-xr-x@ 1712 admin  staff  54784 Aug 29 11:43 .
drwxr-xr-x@   36 admin  staff   1152 Aug 29 10:00 ..
-rw-r--r--@    1 admin  staff   1529 Aug 29 11:43 20210307.Last.ncd
-rw-r--r--@    1 admin  staff   7669 Aug 29 11:43 20210308.Last.ncd
-rw-r--r--@    1 admin  staff   7164 Aug 29 11:43 20210309.Last.ncd
ls -la "$R/db/minute/NQCONT/" | tail -3
-rw-r--r--@    1 admin  staff  10095 Aug 29 11:43 20260717.Last.ncd
-rw-r--r--@    1 admin  staff   3642 Aug 29 11:43 20260719.Last.ncd
-rw-r--r--@    1 admin  staff   6960 Aug 29 11:43 20260720.Last.ncd
ls -la -T "$R/db/minute/NQCONT/" | awk 'NR>3 {print $6, $7, $9}' | sort | uniq -c | sort -rn | head -5
1710 Aug 29 2026
ls -1 "$R/db/day/" | /usr/bin/grep -n NQ
179:MNQ 03-20
180:MNQ 03-21
181:MNQ 03-22
182:MNQ 03-23
183:MNQ 03-24
184:MNQ 03-25
185:MNQ 03-26
186:MNQ 06-19
187:MNQ 06-20
188:MNQ 06-21
189:MNQ 06-22
190:MNQ 06-23
191:MNQ 06-24
192:MNQ 06-25
193:MNQ 06-26
194:MNQ 09-19
195:MNQ 09-20
196:MNQ 09-21
197:MNQ 09-22
198:MNQ 09-23
199:MNQ 09-24
200:MNQ 09-25
201:MNQ 09-26
202:MNQ 12-19
203:MNQ 12-20
204:MNQ 12-21
205:MNQ 12-22
206:MNQ 12-23
207:MNQ 12-24
208:MNQ 12-25
210:NQ
211:NQ 03-17
212:NQ 03-18
213:NQ 03-19
214:NQ 03-20
215:NQ 03-21
216:NQ 03-22
217:NQ 03-23
218:NQ 03-24
219:NQ 03-25
220:NQ 03-26
221:NQ 06-17
222:NQ 06-18
223:NQ 06-19
224:NQ 06-20
225:NQ 06-21
226:NQ 06-22
227:NQ 06-23
228:NQ 06-24
229:NQ 06-25
230:NQ 06-26
231:NQ 09-16
232:NQ 09-17
233:NQ 09-18
234:NQ 09-19
235:NQ 09-20
236:NQ 09-21
237:NQ 09-22
238:NQ 09-23
239:NQ 09-24
240:NQ 09-25
241:NQ 09-26
242:NQ 12-16
243:NQ 12-17
244:NQ 12-18
245:NQ 12-19
246:NQ 12-20
247:NQ 12-21
248:NQ 12-22
249:NQ 12-23
250:NQ 12-24
251:NQ 12-25
252:NQCONT
253:NQCONT 09-25
ls -la "$R/db/day/NQCONT" "$R/db/day/NQCONT 09-25" 2>&1 | head -12
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/db/day/NQCONT:
total 0
drwxr-xr-x@   2 admin  staff    64 Aug 29 11:35 .
drwxr-xr-x@ 256 admin  staff  8192 Aug 29 11:35 ..

/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/db/day/NQCONT 09-25:
total 0
drwxr-xr-x@   2 admin  staff    64 Aug 29 11:34 .
drwxr-xr-x@ 256 admin  staff  8192 Aug 29 11:35 ..
ls -la "$R/db/tick/" "$R/db/cache/"
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/db/cache/:
total 0
drwxr-xr-x@  7 admin  staff  224 Aug 29 09:54 .
drwxr-xr-x@ 12 admin  staff  384 Jul 24 14:32 ..
drwxr-xr-x@  3 admin  staff   96 Jul  9 10:38 CME US Index Futures ETH.SA Western Standard Time
drwxr-xr-x@  4 admin  staff  128 Aug 29 09:45 CME US Index Futures RTH.SA Western Standard Time
drwxr-xr-x@  3 admin  staff   96 Aug 29 09:54 Default 24 x 7.SA Western Standard Time
drwxr-xr-x@  3 admin  staff   96 Jul 14 14:45 Nymex Metals - Energy ETH.SA Western Standard Time
drwxr-xr-x@  3 admin  staff   96 Jul 20 11:26 US Equities RTH.SA Western Standard Time

/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/db/tick/:
total 0
drwxr-xr-x@  2 admin  staff   64 Aug 29 09:59 .
drwxr-xr-x@ 12 admin  staff  384 Jul 24 14:32 ..
python3 -I -c 'import sys; [print(t, "->", __import__("datetime").datetime(1,1,1) + __import__("datetime").timedelta(microseconds=t//10)) for t in (599266080000000000, 638922816000000000, 662353632000000000, 639553536000000000, 639790272000000000)]'
599266080000000000 -> 1900-01-01 00:00:00
638922816000000000 -> 2025-09-01 00:00:00
662353632000000000 -> 2099-12-01 00:00:00
639553536000000000 -> 2027-09-01 00:00:00
639790272000000000 -> 2028-06-01 00:00:00
````
````text
NQCONT Future master UserData, 278 bytes, hex:
0000  22 00 00 00 00 00 00 00 01 00 00 00 17 00 00 00 37 00 00 00 01 00 2d 00 01 00 2d 00 01 00 2d 00
0020  01 00 2d 00 01 00 2d 00 01 00 2d 00 01 00 2d 00 01 00 2d 00 01 00 2d 00 01 00 2d 00 01 00 2d 00
0040  01 00 2d 00 01 00 2d 00 01 00 2d 00 01 00 2d 00 01 00 2d 00 01 00 2d 00 01 00 2d 00 01 00 2d 00
0060  01 00 2d 00 01 00 2d 00 01 00 2d 00 01 00 2d 00 01 00 2d 00 01 00 2d 00 01 00 2d 00 01 00 2d 00
0080  01 00 2d 00 01 00 2d 00 01 00 2d 00 01 00 2d 00 01 00 2d 00 01 00 2d 00 01 00 2d 00 01 00 2d 00
00a0  01 00 2d 00 01 00 2d 00 01 00 2d 00 01 00 2d 00 01 00 2d 00 01 00 2d 00 01 00 2d 00 01 00 2d 00
00c0  01 00 2d 00 01 00 2d 00 01 00 2d 00 01 00 2d 00 01 00 2d 00 01 00 2d 00 01 00 2d 00 00 00 01 00
00e0  2d 00 01 00 2d 00 01 00 2d 00 01 00 2d 00 01 00 00 00 00 80 92 7e ea e8 dd 08 00 c0 29 92 6c 30
0100  de 08 00 00 00 00 00 00 f8 ff 01 00 00 00 00 00 00 00 00 00 00 00
== every 8-byte little-endian int64 at any offset that decodes to a .NET-ticks date 2000..2030, plus the double that follows it
offset 242 ticks 638922816000000000 -> 2025-09-01 00:00:00 | next 8 bytes as double: 5.851602581354036e-266
offset 250 ticks 639001440000000000 -> 2025-12-01 00:00:00 | next 8 bytes as double: nan
````

**Evidence E: masters per type that own a 1900-01-01 `Instruments` row.** All 366 Future masters do. This supports reading that row as the `##-##` placeholder, which is INFERRED. Command as run: `python3 -I inst2.py 2>&1 | tee inst2.out`
````text
== masters by InstrumentType: total, and how many own an Instruments row with Expiry 1900-01-01
type 0 masters 366 with-1900-row 366
type 1 masters 1040 with-1900-row 1
type 2 masters 52 with-1900-row 0
type 3 masters 13 with-1900-row 0
type 4 masters 64 with-1900-row 0
type 5 masters 262 with-1900-row 0
type 7 masters 61 with-1900-row 0
== the one master with MergePolicy != 3
(699839150754358, 'DDI', 0, 0)
== Stock NQCONT and Stock NQ: Version, Description, Currency, Url
(699839150754593, 'NQ', 1, 7, 1, '')
(699839150754594, 'NQCONT', 0, 7, -10200, '')
(699839150754605, 'NQCONT', 1, 7, 1, '')
````

**Evidence F: reference §2 and §6, plus the session 52 and 53 decision rows.** Command as run: `bash -v docs1.sh 2>&1 | tee docs1.out`
````text
cd /Volumes/Sensidine/Praxis.build
sed -n '85,125p' docs/reference/2026-07-24-nt8-windows-reference.md
- **What it's for:** configure/connect/disconnect market-data and brokerage connections; per-provider + aggregate status (bottom-left of Control Center).
- **Open:** `Connections` menu on the Control Center menu bar. ([`20-connections-menu.png`](assets/nt8-2026-07-24/20-connections-menu.png))
- Cite: https://ninjatrader.com/support/helpguides/nt8/connections_menu.htm

---

## 2. Import Historical Data — NT8 Native Format

**Open:** `Tools > Historical Data` → expand the **Import** accordion section (⚠️ accordion, not a tab — see §1e). ([`16-historical-data-import.png`](assets/nt8-2026-07-24/16-historical-data-import.png))

**Fields (confirmed live in the Import section):**
1. **Format** — choose the NinjaTrader native option (**"NinjaTrader (end of bar timestamps)"**). NT8 native minute/tick bars use end-of-bar timestamps.
2. **Data Type** — **Last** (also Bid / Ask). PRAXIS minute bars = **Last**.
3. **Time Zone of Imported Data** — the zone the file's timestamps are in (set to match the source file exactly).
4. (Tick imports only) checkboxes to **generate 'Minute' / 'Day' bars from imported tick data**.
5. Press **"Import"** → OS file-picker → select the `.txt` → **"Open"**.

**⚠️ LIVE — the instrument gotcha, now confirmed by evidence:** the **Import** section has **no instrument field** (Format / Data Type / Time Zone / Import only — [`16-historical-data-import.png`](assets/nt8-2026-07-24/16-historical-data-import.png)); the **Download** section *does* have an Instrument field ([`17-historical-data-download.png`](assets/nt8-2026-07-24/17-historical-data-download.png)). So NT8 derives the import's target instrument **from the filename**, not from any dialog field. This is exactly what blocked the 4uu import (`NQ-continuous-1min.nt8import.txt` → "Instrument is not supported by repository").

**Filename convention:** `<NinjaTrader instrument name>.<DataType>.txt` — the instrument string must match a known instrument and the `.Last/.Bid/.Ask` token must match the selected **Data Type**:
- `MSFT.Last.txt` · `ES 12-09.Bid.txt` (contract-month form, with a space) · `EURUSD.Ask.txt`
- For PRAXIS NQ: **`NQ 12-25.Last.txt`** (space before `12-25`; `.Last` matches Data Type).

**Expected file format (semicolon-delimited, one record/line):**
- Minute bars: `yyyyMMdd HHmmss;Open;High;Low;Close;Volume` — e.g. `20061023 004400;1377.25;1377.25;1377.25;1377.25;86`
- Tick (second): `yyyyMMdd HHmmss;Price;Volume`
- Tick (sub-second): `yyyyMMdd HHmmss fffffff;Price;Volume`

**Verify a successful import:**
- A **confirmation window** appears on success.
- **Errors appear in the Control Center `Log` tab** (formatting/naming problems show here).
- **On-disk:** minute data lands under `Documents\NinjaTrader 8\db\minute\<instrument>\` (analogous `db\tick\`, `db\day\`). Confirm files/bar counts exist for the imported instrument.
- Cross-check by charting the instrument for the imported range (Merge Policy affects what's shown — §6).

- Cite: https://ninjatrader.com/support/helpguides/nt8/importing.htm · https://ninjatrader.com/support/helpguides/nt8/historical_data_manager.htm
- 🔲 **TODO:** whether `.zip` files import directly is undocumented and untested — treat as unsupported until verified on the live Import dialog.

---

## 3. Compile a NinjaScript Strategy

echo ----- lines 175-200
----- lines 175-200
sed -n '175,200p' docs/reference/2026-07-24-nt8-windows-reference.md
- The related **Data Series** dialog (right-click chart → **"Data Series…"**) is [`13-chart-data-series-dialog.png`](assets/nt8-2026-07-24/13-chart-data-series-dialog.png).
- Cite: https://ninjatrader.com/support/helpguides/nt8/running_a_ninjascript_strategy.htm

---

## 6. Continuous / Custom-Instrument Setup (Futures)

**Manager:** `Tools > Instruments`.

**Representation of futures:**
- **Individual contract month:** `<ROOT> <MM-YY>` with a **space** — e.g. `NQ 12-25` (Dec 2025). ⚠️ **LIVE:** NT8 can also *display* months as a **month abbreviation** — the chart during capture read **`MNQ SEP26`** — same underlying expiry, display-mode option.
- **Continuous contract:** the **`<ROOT> ##-##`** designation (e.g. `NQ ##-##`), a rolling front-month series. Requires **provider support** (historically Kinetick / eSignal / IQFeed).

**Merge Policy** (how contract months stitch at rollover — matters for backtests spanning a roll):
- **Global:** `Tools > Options > Market Data > Merge policy`. **Per-instrument:** `Tools > Instruments` → select → **Edit** → **Merge policy**.
- Options: **MergeBackAdjusted** (back-adjust to next front month, seamless) · **MergeNonBackAdjusted** (raw, visible roll gaps) · **DoNotMerge** (single expiry only) · **UseGlobalSetting** (per-instrument, inherit global).
- Cite: https://ninjatrader.com/support/helpguides/nt8/instruments.htm · https://ninjatrader.com/support/helpguides/nt8/merge_policy.htm

---

## 7. Sim Account Operations — Flatten / Cancel All (Sim Safety)

All in the Control Center:
- **Cancel one order:** `Orders` tab → right-click → **"Cancel Order"**.
- **Cancel all working orders:** `Orders` tab → right-click → **"Cancel All Orders"**.
- **Flatten one account** (close positions + cancel its working orders): `Accounts` tab → right-click **Sim101** → **"Flatten Account"**.
echo ----- DECISION_LOG rows
----- DECISION_LOG rows
/usr/bin/grep -n -e '2026-08-29T12:05:00Z' -e '2026-08-29T19:00:00Z' DECISION_LOG.md
359:- [2026-08-29T12:05:00Z] WHO: praxis-master (session 52) | WHO EXECUTED: amear (VM, by hand) | WHAT: **Q4 CLOSED, AND A NEW FINDING THE MASTER DID NOT PREDICT — `NQCONT` EXISTED TWICE, AS BOTH A `Future` AND A `Stock`. Deleting the duplicate did NOT stop the auto-resolution** | WHY: Q4 asked what the contract-month **offset** field does, since entering December 2025 produced a resolution to September 2025. **The master marked it UNVERIFIED and explicitly refused to guess.** That was correct: the answer is that **no offset value was ever entered at all**, so the offset was never the mechanism. Root cause is NT8's data-series **auto-rollover defaulting to December 2025 with no explicit configuration** | WHERE: NT8 Instruments manager and Strategy Analyzer instrument picker on the Windows VM; `docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md` (Q4, left UNVERIFIED) | WHEN: 2026-08-29 | HOW: **THE REFUSAL TO GUESS PAID.** Had the master asserted an offset semantics — the three-month backward step was superficially consistent with a one-quarterly offset — it would have been a confident, well-reasoned, **wrong** explanation of a field that was never populated. Same shape as this project's two documented confident-wrong conclusions. **THE NEW FINDING, NOT PREDICTED BY ANY DOCUMENT AND NOT IN THE LAYOUT REFERENCE:** a **duplicate `NQCONT` instrument existed — one typed `Future`, one typed `Stock`.** The `Stock` duplicate was confirmed empty against Historical Data and deleted. **The auto-resolution to `NQCONT 09-2025` PERSISTED afterward, unchanged.** So the duplicate was not the cause; it was a second, independent defect sitting alongside it. **UNVERIFIED AND NOT INVESTIGATED: how a `Stock`-typed `NQCONT` came to exist.** Candidate origin is an earlier attempt at the Fix-B shape, but nothing observed supports that and it is not asserted. **Part 6 remains blocked:** the Analyzer resolves bare `NQCONT` to `NQCONT 09-2025` and throws unknown-instrument on requesting bars | STATE: open — Q4 closed; duplicate-instrument finding open and unexplained
371:- [2026-08-29T19:00:00Z] WHO: praxis-master (session 53) | WHO EXECUTED: amear (VM, by hand) | WHAT: **CHECK A2 CLOSED, DECISIVE. `NQCONT` IS DEFINED AS `Type: Future`, `Expiry: 09-25`, `Rollover date: 12-01-2025`. THE REQUEST-REWRITE IS NOT AN INTERMEDIATE LAYER — IT IS THE INSTRUMENT DEFINITION ITSELF** | WHY: the master's framing at `18:00:00Z` was that *"something rewrites the request from the root name into a contract month"* and explicitly refused to name the cause. **The shape was right and the cause is now observed rather than inferred: bare `NQCONT` resolves to a dated contract because the definition carries `Expiry: 09-25`.** There is no mystery layer. **`Merge Policy` found at `Use Global Setting`, NOT `DoNotMerge`** — recorded, and deliberately NOT changed pending a ruling | WHERE: NT8 `Tools > Instruments`, `NQCONT` properties, Windows VM; predicted-and-tested per the falsifier published in `docs/reports/2026-08-29-session53-vm-checks-A-and-B.md` | WHEN: 2026-08-29 | HOW: **THE PUBLISHED FALSIFIER WAS *"no expiry, no contract months, no merge policy means the framing is wrong."* The opposite was observed, so the framing survives a test it could have failed.** That is the only reason it is now load-bearing. **THE ATTEMPTED FIX FAILED AND THE FAILURE IS THE MORE IMPORTANT DATUM: NT8 refused to save a `Future`-type instrument with zero contract-month entries**, which independently reproduces the session-52 Part 1 finding that a contract-month entry is mandatory for this type. **CONSEQUENCE, AND IT IS LARGER THAN A FIELD EDIT:** the premise carried by this workstream — *"create a bare continuous `NQCONT`, select it, get the stitched series"* — **may never have been reachable as configured.** Whether NT8's `Future` type supports a genuinely rollover-free continuous series **AT ALL** is now the governing question, and it is a claim about vendor software that **nobody in this project has observed.** The master **does not answer it** and is dispatching it to two independent sources — the on-disk layout reference §6 (manager, in flight) and the **NT8 Help Guide inside the VM** (coworker) — precisely so that a single confident static read cannot settle it | STATE: closed — A2 `PASS`, root cause named; continuous-series feasibility OPEN and dispatched
375:- [2026-08-29T19:30:00Z] WHO: praxis-master (session 53) | WHO OBSERVED: vm coworker | WHAT: **🛑 HALT. THE VM STATE CONTRADICTS THE BRIEF'S BASELINE ON FOUR INDEPENDENT POINTS, AND THERE IS EVIDENCE OF ACTIVITY MINUTES BEFORE THE COWORKER STARTED. CAUSE UNESTABLISHED. TASKS 2–4 CANCELLED BEFORE EXECUTION** | WHY: **the coworker caught this on its FIRST screenshot, before touching anything, and flagged it instead of proceeding.** That is the behaviour the brief's "report what you observed, someone else decides" clause exists to produce, and it is recorded as the rule working. **A discrepancy noticed at step zero costs one turn; the same discrepancy noticed after Task 4 would have contaminated a toggle experiment and been indistinguishable from a result** | WHERE: NT8 on the Windows VM; brief `docs/reports/2026-08-29-session53-coworker-brief-continuous-series.md`; contradicted baseline rows `2026-08-29T12:05:00Z`, `12:10:00Z`, `19:00:00Z` | WHEN: 2026-08-29, VM clock ~12:18, error rows timestamped 11:58–12:01 | HOW: **THE FOUR CONTRADICTIONS, AS REPORTED, EACH UNVERIFIED BY THE MASTER:** (1) **`Merge Policy` already reads `Do not merge`** — the properties dialog was **already open mid-session** when the coworker looked; row `19:00:00Z` records `Use Global Setting`, observed by Amear, and the master's brief instructed that it NOT be changed. (2) **Red error rows in the Control Center `Log` tab timestamped 11:58–12:01**, minutes before the coworker began. (3) **The `Stock`-typed `NQCONT` IS STILL PRESENT**, alongside the `Future`; row `12:05:00Z` records it *"confirmed empty and deleted."* **Plus an `NQ`-typed `Stock` entry that appears in no document in this project.** (4) **A live `NQCONT` 1-minute chart is RENDERING VISIBLE CANDLES** — directly contradicting `12:10:00Z`'s blank chart. **THE INFERENCE THIS VOIDS, AND IT IS THE MOST IMPORTANT CONSEQUENCE:** row `12:05:00Z` concluded that the duplicate *"was not the cause; it was a second, independent defect"* **on the strength of the auto-resolution persisting AFTER the deletion.** If the `Stock` duplicate was never actually deleted — or the deletion did not persist — **then that inference rests on an event that did not occur and it is VOID, not merely doubtful.** You cannot conclude anything from the effect of a deletion that did not happen. **The master does NOT determine which of three hypotheses holds** — never deleted, deletion did not persist, or recreated since — and does not guess. **A SECOND ACTOR ON THE VM IS THE LEADING CANDIDATE AND IS NOT ASSERTED:** a `docs/reports/2026-08-29-session53-parallel-handoff.md` exists, dated `10:11`, describing **two seats**. The single-session rule governs this git worktree; **it has never covered the VM.** That gap is named here for the first time. **CONFOUNDED LEAD, EXPLICITLY NOT A FINDING:** `Merge Policy = Do not merge` and a **rendering** chart now co-occur, which is the exact pairing Task 4 was designed to test — **but performed by an unknown actor, with no control, no before-state observed by us, and no record of what else changed in the same window. Correlation with an unobserved intervention is not evidence, and this project's standing failure is precisely the well-formed conclusion drawn from an unobserved mechanism** | STATE: 🛑 open — HALTED; provenance is Amear's question; no VM state to be altered until it is answered
464:- [2026-10-31T15:01:22Z] WHO: praxis-master | WHAT: **BEAD `Praxis_build-a9d` CREATED AND DISPATCHED — Future-row loading plan.** Facts assembled for the brief, all from disk this turn: the import file in use is `~/praxis-signals/b2-data/NQCONT.Last.txt` (1,857,362 lines, byte-identical to `NQ-continuous-1min.nt8import.txt`, first row `20210307 180100`); NT8's Import section has NO instrument field — it maps by file name `<instrument>.<DataType>.txt` (`docs/reference/2026-07-24-nt8-windows-reference.md:91-123`), contract months are written `<ROOT> <MM-YY>` with a space, continuous is `<ROOT> ##-##`, Merge Policy options listed (:180-194); session 52 (DECISION_LOG `2026-08-29T12:05:00Z`): a Stock-typed duplicate `NQCONT` existed then too, was deleted, and bare `NQCONT` still auto-resolved to `09-2025`; session 53 (`2026-08-29T19:00:00Z`): `NQCONT` Future is `Expiry: 09-25`, `Rollover 12-01-2025`, NT8 refuses a Future with zero contract months, Merge Policy was `Use Global Setting` (left unchanged pending a ruling); Fusion today (REPORTED): Stock row present again, Future row with one rollover shown as `NQCONT SEP25`, Analyzer picker offers `NQCONT` / `NQCONT SEP25` / `NQCONT ##-##`. Leading hypothesis for the manager to test against sources (INFERRED): the bare-named file landed under `db\minute\NQCONT\` on the Stock row; the Future's bars would need to live under the contract-month name (`NQCONT 09-25`) or be reachable through the rollover collection. Unit = research + a pre-registered walkthrough with readbacks and stop conditions; **no deletion of any instrument or data without an explicit Amear step; no template change (F2, 08-29 row)**; save-as-default control from on-disk sources or UNVERIFIED with a readback; MANIFEST rows owed folded in. Return handoff for the Claude.ai channel is the unit's last deliverable, written after the baseline lands (R-VM-4). | WHY: R-VM-1/2; loop steps 2–3. | STATE: open — a9d manager running.
echo ----- wc
----- wc
wc -l docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md docs/reports/2026-08-29-session53-vm-checks-A-and-B.md docs/reports/2026-10-31-voice-session-notes.md
     285 docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md
      87 docs/reports/2026-08-29-session53-vm-checks-A-and-B.md
      58 docs/reports/2026-10-31-voice-session-notes.md
     430 total
````

**Evidence G: session 52 and 53 grep for import, minute, folder, `NQCONT 09-25` and Loaded; the voice notes in full; DECISION_LOG row 12:10.** Command as run: `bash -v docs2.sh 2>&1 | tee docs2.out`
````text
cd /Volumes/Sensidine/Praxis.build
/usr/bin/grep -n -i -E 'import|minute|folder|NQCONT 09-25|09-2025|Loaded|deleted|delete' docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md docs/reports/2026-08-29-session53-vm-checks-A-and-B.md | cut -c1-400
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:54:import synthetic stitched bars into.**
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:57:instrument, correct tick and point value, no expiry, accepts imported flat bars."*
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:74:1. **VERIFIED (reference §2):** the import filename convention is
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:79:   data landed in `db\minute\NQCONT\`, a folder with **no month suffix**.
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:80:3. **VERIFIED (reference §2):** minute data lands under
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:81:   `db\minute\<instrument>\`, so NT8 wrote it to the literal name it was given.
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:84:**INFERRED conclusion:** the import keyed the bars to the bare string `NQCONT`.
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:86:*dated* series — something like `NQCONT 09-25`. It looks in the expiry-suffixed
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:87:folder, finds nothing, and renders blank.
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:89:**The data is on disk, filed under a name nothing ever asks for.** Import writes by
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:98:## Q3 — Can the data be loaded under the literal name?
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:103:whose **`Loaded`** section exists to *"access/manage all historical data"* and
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:104:inspect what is loaded.
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:106:**UNVERIFIED:** whether `Loaded` can *chart* a series, or only list and manage it.
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:108:never expanded during capture; `Loaded` was captured but its capabilities were not
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:113:**`Tools > Historical Data` → expand `Loaded` → find the NQCONT records and read
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:118:- **Filed as `NQCONT 09-25` or any dated form** → my diagnosis is **wrong**, the
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:164:that stores bars in per-expiry folders and serves whatever is in them — Fix A works
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:169:for the imported instrument"* — a folder-contents check with no mention of date
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:183:**Gate: run the `Loaded` check from Q3 first.** Everything below assumes it shows
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:186:## FIX A — give the filename a contract month, re-import *(try this first)*
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:189:filename. Costs one re-import.
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:192:   `NQ-continuous-1min.nt8import.txt` → `NQCONT 12-25.Last.txt`
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:201:4. `Tools > Historical Data > Import`: Format `NinjaTrader (end of bar
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:214:finds the folder you already have. **No re-import needed.**
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:221:3. Import `NQCONT2.Last.txt` and chart the bare name.
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:254:2. **Does NT8 filter imported historical bars by the contract's expiry window**,
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:255:   or serve whatever is in `db\minute\<instrument>\` regardless of date? **This is
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:260:   backtesting imported stitched data.** Search NinjaTrader forums and futures.io.
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:264:6. **Is `<ROOT> ##-##` ever usable with imported data**, or is it strictly
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:284:Part 1 is superseded by this document pending the `Loaded` check and the research
docs/reports/2026-08-29-session53-vm-checks-A-and-B.md:12:    approx 1,857,362 records, in db\minute\NQCONT. (Amear, today.)
docs/reports/2026-08-29-session53-vm-checks-A-and-B.md:13:  - The Strategy Analyzer resolves bare NQCONT to NQCONT 09-2025 and throws
docs/reports/2026-08-29-session53-vm-checks-A-and-B.md:15:  - A Stock-typed duplicate NQCONT was deleted and the resolution persisted
docs/reports/2026-08-29-session53-vm-checks-A-and-B.md:21:data - the standard NQ front-month contract is fine. Set the SAME 1-minute
docs/reports/2026-08-29-session53-vm-checks-A-and-B.md:43:asking for NQCONT 09-2025. Those are different strings, so "unknown instrument"
docs/reports/2026-08-29-session53-vm-checks-A-and-B.md:87:  - the chart interval is 1 minute, not Daily
echo ----- voice notes, full
----- voice notes, full
cat docs/reports/2026-10-31-voice-session-notes.md
# 2026-10-31 — Voice session notes (Amear, at the Fusion VM)

Written by Claude from a voice/chat session, about 10:29–10:52 ET (14:29–14:52Z). This is a record for the next Claude Code session to read first, as `docs/reports/2026-10-31-voice-handoff-backtest-session.md` §10 asks.
It is not an audited report. Screen values are REPORTED BY AMEAR, by voice or by screenshot. The screenshots went to the voice agent and are not in this repo. Claude's reasoning is labelled INFERRED.

## Amear's rulings
- **None made this session.** One decision is open and is Amear's (see "Open — Amear's decision" below).

## R-I1 — `Tools > Instruments`, filter `NQCONT` (REPORTED BY AMEAR, screenshots)
- **Two rows: one Future, one Stock.** The Stock-typed `NQCONT` row exists on Fusion, not just in the rescued Parallels database.
- **Stock row:** point value **1**, tick size **0.01**, trading hours **US Equities RTH**, rollovers **0**. This matches the rescued-database row `(…, 'NQCONT', 1, 1.0, 0.01, 'US Equities RTH')`.
- **Future row:** point value **20**, tick size **0.25**, trading hours **CME US Index Futures RTH**, **one rollover** (the Analyzer list shows it as `NQCONT SEP25`).
- Both edit windows were closed with the X and nothing was changed.

## Strategy Analyzer — which row runs 3/4 used
- The instrument field shows plain **`NQCONT`**, so the name alone doesn't say which row.
- The dropdown lists three entries (Amear's screenshot, read by the voice agent): plain `NQCONT`, `NQCONT SEP25`, `NQCONT ##-##`.
- Settings confirmed from Amear's screenshot to match run 4: base strategy, BandOrVWAP, 1 contract, 2021-03-08 → 2026-07-17, CME US Index Futures RTH, PRAXIS commission, Standard fill resolution, slippage 2.

## Run 0-S (Standard, base strategy, plain `NQCONT`) — REPORTED BY AMEAR
- **Total slippage: 48.44.** This is the same as run 4.
- **Net profit: "$3,136"** (spoken; the cents were not read). Run 4 was $3,136.84.
- **Trade count was not read directly.** INFERRED 1,211, because 48.44 = 1,211 × 4 × 0.01.
- Not read: L/S split, PF, max DD, gross profit and loss, the first and last 5 trades, exit-name counts, and R1/R2/R6.
- **INFERRED, strong:** run 0-S reproduces run 4, and both ran on the **Stock row at $1/point**. The 48.44 figure only works at a 0.01 tick. So the slippage actually simulated was 0.02 points per side, not the locked 2 ticks (0.50 points), and every run-3/4/0-S dollar is at $1/point. The voice agent told Amear this.

## Attempt on the continuous future (`NQCONT ##-##`) — REPORTED BY AMEAR
- The Analyzer **would not accept a start date of March 2021**.
- It **threw an error requesting bars, "unknown instrument"**. **The exact text was not captured word for word.** Amear paraphrased it, and it is the same family as the August `error on requesting bars series, unknown instrument NQCONT`.
- No result was produced on the Future row.
- **INFERRED (voice agent), not verified:** the price data was imported onto the Stock row, so the Future row has no bars to load. A fix would mean re-importing under the future contract. That needs planning in Claude Code, not improvising at the VM.

## Not done this session
- R-I2 (the time zone and sessions of the RTH template) and R-I3 (run 4's largest-winner entry price). R-I3 is now largely redundant, but it is a cheap confirmation.
- Run 0-H (High resolution). Installing and compiling the three new files (OppBand, Flat1559, LastHalfHourMomentum). All of §§5–8 of the handoff.
- The strategy files were not copied to the VM. The base `PraxisNoiseAreaBreakout.cs` is unchanged on the VM.

## Open — Amear's decision (record his answer, do not decide)
1. Which instrument to test on from here:
   - (a) Keep testing on the Stock row. The three files still compare against each other and against run 4, but the dollars aren't real NQ, and the locked 2-tick slippage isn't being simulated.
   - (b) Get the Future row loadable first (re-import, or another mechanism), then re-baseline. 0-S on the future becomes the new baseline.
   - (c) Hold the backtests until (b) is planned.
2. The consequences the handoff §1 already names: whether `D-2026-10-30-A` and the F3 cost model need a cold re-decision under their void clause, now that the Stock-row reading is confirmed on screen rather than inferred.

## Auditor-channel findings on the handoff itself (Claude.ai, 2026-10-31 ~14:40Z, unrelayed until now)
- §1's "≈ $62.7k at $20/pt" is **wrong**: it scales the commission by 20. Recommendation: delete the conversion, don't correct it. Nothing depends on it.
- The handoff had no plan for what happens if the readbacks confirm the Stock row: the settings table says only "NQCONT", which doesn't say which row. That gap is the open decision above.
- §1 R-I2 leaves out the 2026-08-29 on-screen reading of the RTH template (**Central**, 8:30–16:00). There are three readings on record, not two. The 08-29 ledger row also blocks any template change until F2 is ruled.
- Repo hygiene: there is a stray root file `F` (15 bytes, `# DISPATCH LOG`, dated Jul 28). It is untracked, and the next commit should leave it out.
- Still owed: the MANIFEST row for the handoff file (text in DECISION_LOG `2026-10-31T14:04:31Z`), plus a MANIFEST row for this notes file.

## 2026-10-31 10:54 ET (14:54Z) — Amear's rulings (typed in the Claude.ai chat)
1. **Use the Future row, not the Stock row.** In Amear's words, the Stock row "does not represent the strategy I'm using." This answers the open decision above: option (b).
2. **Get the Future row loading first, then set the new baseline on it.** 0-S on the Future row becomes the baseline. Run 4 and run 0-S on the Stock row are no longer the baseline.
3. **Reminder Amear asked for:** once the Future row loads and the new baseline run is done, **save those Strategy Analyzer settings as the default**, so he isn't re-entering them every run and can't silently fall back to the Stock row through human error. The return handoff (item 4) must carry this as an explicit step. How NT8 saves Analyzer defaults (believed to be a Template → Save as default control) is UNVERIFIED; Code confirms the control before it goes in a step.
4. **Instruction to Claude Code:** when the Future row is loading and the new baseline is set, **prepare a handoff for Amear to bring back to the Claude.ai Praxis channel.** It should cover what changed, the new baseline numbers, what is still open, and the save-as-default step from item 3.
5. Amear wants a backtest at the VM while Code works on the Future row. Which run he means was being clarified at the time of writing; his answer goes below when given.
   - **Amear's answer (10:55 ET): none. No backtests on the Stock row. Wait for the Future row.** The three new files stay uninstalled and unrun until the Future row loads.
echo ----- DECISION_LOG row 12:10
----- DECISION_LOG row 12:10
/usr/bin/grep -n -e '2026-08-29T12:10:00Z' DECISION_LOG.md | cut -c1-1500
361:- [2026-08-29T12:10:00Z] WHO: praxis-master (session 52) | WHAT: **MASTER'S ERROR, RECORDED NOT ABSORBED — BOTH OF THE MASTER'S BLANK-CHART THEORIES WERE REFUTED BY OBSERVATION. The diagnosis was offered at "INFERRED, high confidence" and it was wrong** | WHY: the master told Amear his two reported symptoms were **"not two symptoms — Symptom A is Symptom B,"** and built the claim on an arithmetic argument that looked decisive: the Analyzer resolved to September 2025, the chart window was January–August 2026, so the chart must be silently resolving to a dated contract whose expiry the Data Series field does not display. **A second theory was offered alongside it** — that the chart interval had defaulted to `Daily` against minute-only data, citing reference §1d where the 2026-07-24 capture opened on `MNQ SEP26, Daily` | WHERE: `docs/reports/2026-08-29-session52-blank-chart-diagnosis.md`, checks A1 and A2 | WHEN: 2026-08-29 | HOW: **BOTH CHECKED BY AMEAR, BOTH RULED OUT.** (1) **The chart title bar reads plain `NQCONT`, with no dated suffix** — refuting the resolution theory directly, at the exact observation the master nominated as decisive (*"If the title carries an expiry, diagnosis confirmed, stop testing"*). (2) **The interval is confirmed one minute, not Daily** — refuting the second. **THE BLANK CHART IS UNEXPLAINED.** **WHAT THE MASTER GOT RIGHT, AND IT IS THE ONLY REASON THIS COST ONE TURN INSTEAD OF SEVERAL:** the theory was published **with its own fa
````

---

## Q2. Which file name would land data on the Future row's contract month, and what would the Analyzer select?

**Answer.**
1. **CORRECTED (a9d worker 4, finding 3): grade lowered from OBSERVED to INFERRED (strong).** Old: "**OBSERVED: the display form and the stored name are the same contract.**" New: **OBSERVED:** at 10:00:22 the trace names `NQCONT SEP25` and, 128 ms later, the log names `NQCONT 09-25`. At 09:54:01 the pair is `NQCONT DEC29` / `NQCONT 12-29`. The folder `db/minute/NQCONT 09-25/` was created at 10:00:22. **INFERRED (strong, from co-timing; no source states it):** the picker's `NQCONT SEP25` is `NQCONT 09-25` internally. Walkthrough step 1.5 now tests this on Fusion (chart title readback, falsifier, STOP). The original text follows, kept for the record; its OBSERVED grade is withdrawn: "Log and trace lines with the same timestamp pair them up. At 10:00:22 the trace shows `instrument='NQCONT SEP25'` and the log shows `Unknown instrument 'NQCONT 09-25'`. At 09:54:01 the trace shows `'NQCONT DEC29'` and the log shows `'NQCONT 12-29'`. So the picker's `NQCONT SEP25` **is** `NQCONT 09-25` internally. The folder name uses the `MM-YY` form, as `db/minute/NQCONT 09-25/` shows."
2. **Import file name.** Reference §2 states the convention `<NinjaTrader instrument name>.<DataType>.txt`, with the contract-month form using a space (`ES 12-09.Bid.txt`, `NQ 12-25.Last.txt`). Applying it here gives **`NQCONT 09-25.Last.txt`** (INFERRED). No source says whether `NQCONT SEP25.Last.txt` would also be accepted: SPEC-SILENT, UNVERIFIED.
3. **Analyzer selection: two options.**
   - **(a) `NQCONT SEP25` (single expiry).** INFERRED: it would read `db\minute\NQCONT 09-25\`, by the folder pattern in Q1.
   - **(b) `NQCONT ##-##`.** This would go through the rollover collection, which holds exactly one row: 09-25, rollover 2025-12-01 (blob decode INFERRED; session 53 REPORTED).
4. **Merge Policy.**
   - OBSERVED: the rescued `Config.xml` has `<GlobalMergePolicy>MergeBackAdjusted</GlobalMergePolicy>`.
   - REPORTED (session 53, row `19:00:00Z`): the Future `NQCONT` per-instrument policy was `Use Global Setting`. The sqlite value is `MergePolicy 3`, and 1,857 of the 1,858 masters carry 3 (OBSERVED).
   - INFERRED: integer 3 means UseGlobalSetting, so the effective policy on that install was MergeBackAdjusted.
   - There is a conflict on record: row `19:30:00Z` REPORTS that the coworker later saw `Do not merge` in an open dialog. Which state reached disk is not established.
5. **Risk of a second back-adjustment.** The file is already Difference back-adjusted (D-2026-07-17-A, D-2026-07-21-A). Reference §6 says MergeBackAdjusted "back-adjust[s] to next front month". With one contract month and no neighbour, whether NT8 would apply any offset at all is **SPEC-SILENT / UNVERIFIED**. Reference §6 describes DoNotMerge as "single expiry only". Choosing (a) with DoNotMerge removes the question by construction (INFERRED). That still changes an instrument setting, which is Amear's call.
6. **The March-2021 refusal on `##-##`.** One explanation fits: the rollover table makes 09-25 the front month only from 2025-12-01. Before that date there is no contract for `##-##` to map to, so a 2021 start has nothing to resolve. **This is plausible but UNVERIFIED.** No on-disk source describes how NT8 handles dates before the first rollover entry.
7. **A caution about the error text.** Every `Unknown instrument` error in the rescued log is paired with a trace line `Cbi.Instrument.RequestBars (to Provider)`, while the Simulated Data Feed was connected (OBSERVED). So the error is raised on a **provider** request (INFERRED). **CORRECTED (a9d worker 4, finding 2).** Old: "After 11:26, the bare-`NQCONT` minute requests ask the provider only for `7/20/2026` to `8/28/2026`. That window starts on the date of the last local file, `20260720` (OBSERVED), which is consistent with NT8 already holding local bars up to that date (INFERRED)." That contradicted Evidence B, which itself shows `11:33:54:114 ... instrument='NQCONT' from='1/2/2026'` and `11:59:19:301 ... from='12/31/2025'`. New: After 11:26, 11 of the 19 bare-`NQCONT` 1-minute provider requests start at `7/20/2026`, the date of the last local file. The other 8 start at `1/2/2026` (6), `12/31/2025` (1) or `8/24/2026` (1) (OBSERVED, Evidence B; tally pasted in `docs/reports/2026-10-31-a9d-adversarial.md` finding 2). The 7/20 starts are consistent with NT8 already holding local bars up to that date (INFERRED, weak: the start date also varies with the requested range). **So the error does not, on its own, prove that local bars are absent.** The empty `NQCONT 09-25` folder is the stronger evidence.
8. **Reference §6 says `<ROOT> ##-##` "Requires provider support"** (OBSERVED text). Whether imported data can ever feed `##-##` is UNVERIFIED (session 52 open question 6).

**Evidence A: logs and trace from 2026-08-29.** Command as run: `bash -v logs.sh 2>&1 | tee logs.out`
````text
R="/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full"
ls -la "$R/log/" "$R/templates/StrategyAnalyzer/"
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/log/:
total 136
drwxr-xr-x@ 19 admin  staff   608 Aug 29 11:02 .
drwxr-xr-x@ 20 admin  staff   640 Jul 24 07:56 ..
-rw-r--r--@  1 admin  staff   382 Aug 29 11:02 Install.xml
-rw-r--r--@  1 admin  staff    61 Aug 15 10:09 log.20260815.00000.en.txt
-rw-r--r--@  1 admin  staff    61 Aug 15 10:09 log.20260815.00000.txt
-rw-r--r--@  1 admin  staff   882 Aug 15 10:12 log.20260815.00001.en.txt
-rw-r--r--@  1 admin  staff   882 Aug 15 10:12 log.20260815.00001.txt
-rw-r--r--@  1 admin  staff   317 Aug 16 08:07 log.20260816.00000.en.txt
-rw-r--r--@  1 admin  staff   317 Aug 16 08:07 log.20260816.00000.txt
-rw-r--r--@  1 admin  staff  2536 Aug 17 14:02 log.20260817.00000.en.txt
-rw-r--r--@  1 admin  staff  2536 Aug 17 14:02 log.20260817.00000.txt
-rw-r--r--@  1 admin  staff  1086 Aug 18 19:55 log.20260818.00000.en.txt
-rw-r--r--@  1 admin  staff  1086 Aug 18 19:55 log.20260818.00000.txt
-rw-r--r--@  1 admin  staff   317 Aug 28 18:18 log.20260828.00000.en.txt
-rw-r--r--@  1 admin  staff   317 Aug 28 18:18 log.20260828.00000.txt
-rw-r--r--@  1 admin  staff  2150 Aug 29 11:01 log.20260829.00000.en.txt
-rw-r--r--@  1 admin  staff  2150 Aug 29 11:01 log.20260829.00000.txt
-rw-r--r--@  1 admin  staff  2530 Aug 29 12:01 log.20260829.00001.en.txt
-rw-r--r--@  1 admin  staff  2530 Aug 29 12:01 log.20260829.00001.txt

/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/templates/StrategyAnalyzer/:
total 0
drwxr-xr-x@  2 admin  staff   64 Jul  9 10:37 .
drwxr-xr-x@ 24 admin  staff  768 Jul  9 10:37 ..
echo ----- log lines mentioning NQCONT or import, per file count
----- log lines mentioning NQCONT or import, per file count
/usr/bin/grep -r -c -a -i -E 'NQCONT|import' "$R/log" "$R/trace" | /usr/bin/grep -v ':0$'
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/log/log.20260829.00000.en.txt:10
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/log/log.20260829.00001.en.txt:17
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/log/log.20260829.00000.txt:10
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/log/log.20260829.00001.txt:17
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/trace/trace.20260829.00001.txt:31
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/trace/trace.20260829.00000.txt:21
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/trace/trace.20260816.00000.txt:2
echo ----- distinct NQCONT/import messages in log, with first occurrence, CR stripped
----- distinct NQCONT/import messages in log, with first occurrence, CR stripped
/usr/bin/grep -r -h -a -i -E 'NQCONT|import' "$R/log" | tr -d '\r' | cut -c1-260 | awk '{k=substr($0, 25); if (!(k in s)) {s[k]=1; print}}' | head -40
2026-08-29 09:54:01:461|0|4|Error on requesting bars series: 'Unknown instrument 'NQCONT 12-29''
2026-08-29 09:56:52:507|0|4|Error on requesting bars series: 'Unknown instrument 'NQCONT''
2026-08-29 10:00:22:727|0|4|Error on requesting bars series: 'Unknown instrument 'NQCONT 09-25''
echo ----- CR check on one log file
----- CR check on one log file
f="$(ls -1 "$R/log/" | head -1)"; od -c "$R/log/$f" | head -3
0000000  357 273 277   <   ?   x   m   l       v   e   r   s   i   o   n
0000020    =   "   1   .   0   "       e   n   c   o   d   i   n   g   =
0000040    "   u   t   f   -   8   "   ?   >  \r  \n   <   N   i   n   j
````

**Evidence B: full 2026-08-29 log, and every NQCONT trace line.** Command as run: `bash -v logs2.sh 2>&1 | tee logs2.out`
````text
R="/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full"
cat "$R/log/log.20260829.00000.en.txt" "$R/log/log.20260829.00001.en.txt" | tr -d '\r' | cut -c1-240
2026-08-29 09:27:33:912|2|4|Session Break (Version 8.1.7.2)
2026-08-29 09:28:20:678|1|4|Global simulation mode disabled
2026-08-29 09:28:25:401|1|2|Using IS (is-us-nt-006.ninjatrader.com/31658)
2026-08-29 09:28:25:417|1|4|Automated trading disabled
2026-08-29 09:28:25:691|1|4|Auto connecting 'Simulated Data Feed'...
2026-08-29 09:28:25:878|1|2|Simulated Data Feed: Primary connection=Connecting, Price feed=Connecting
2026-08-29 09:28:26:007|1|2|Simulated Data Feed: Primary connection=Connected, Price feed=Connected
2026-08-29 09:28:26:285|1|32|Order entry hot keys disabled
2026-08-29 09:28:26:294|1|4|Auto close enabled=False
2026-08-29 09:28:27:121|1|2|Time to auto close position='12:00:00 AM', Enabled=False
2026-08-29 09:28:27:137|1|2|Using HDS (hds-us-nt-016.ninjatrader.com/31655)
2026-08-29 09:28:32:976|1|4|Restoring workspace 'Getting Started (Basic)'...
2026-08-29 09:54:01:461|0|4|Error on requesting bars series: 'Unknown instrument 'NQCONT 12-29''
2026-08-29 09:56:52:507|0|4|Error on requesting bars series: 'Unknown instrument 'NQCONT''
2026-08-29 10:00:22:727|0|4|Error on requesting bars series: 'Unknown instrument 'NQCONT 09-25''
2026-08-29 10:14:52:985|0|4|Error on requesting bars series: 'Unknown instrument 'NQCONT''
2026-08-29 10:16:09:033|0|4|Error on requesting bars series: 'Unknown instrument 'NQCONT 09-25''
2026-08-29 10:16:11:343|0|4|Error on requesting bars series: 'Unknown instrument 'NQCONT''
2026-08-29 10:17:25:934|0|4|Error on requesting bars series: 'Unknown instrument 'NQCONT''
2026-08-29 10:18:15:300|0|4|Error on requesting bars series: 'Unknown instrument 'NQCONT''
2026-08-29 10:18:21:444|0|4|Error on requesting bars series: 'Unknown instrument 'NQCONT''
2026-08-29 10:40:22:312|0|4|Error on requesting bars series: 'Unknown instrument 'NQCONT 09-25''
2026-08-29 10:51:36:710|0|4|Unhandled exception: Exception has been thrown by the target of an invocation.
2026-08-29 11:01:38:551|1|2|Simulated Data Feed: Primary connection=Disconnecting, Price feed=Disconnecting
2026-08-29 11:01:38:602|1|2|Simulated Data Feed: Primary connection=Disconnected, Price feed=Disconnected
2026-08-29 11:02:17:212|2|4|Session Break (Version 8.1.7.2)
2026-08-29 11:02:41:873|1|4|Global simulation mode disabled
2026-08-29 11:02:45:020|1|2|Using IS (is-us-nt-005.ninjatrader.com/31658)
2026-08-29 11:02:45:073|1|4|Automated trading disabled
2026-08-29 11:02:45:337|1|4|Auto connecting 'Simulated Data Feed'...
2026-08-29 11:02:45:511|1|2|Simulated Data Feed: Primary connection=Connecting, Price feed=Connecting
2026-08-29 11:02:45:633|1|2|Simulated Data Feed: Primary connection=Connected, Price feed=Connected
2026-08-29 11:02:45:811|1|32|Order entry hot keys disabled
2026-08-29 11:02:45:819|1|4|Auto close enabled=False
2026-08-29 11:02:46:582|1|2|Time to auto close position='12:00:00 AM', Enabled=False
2026-08-29 11:02:46:596|1|2|Using HDS (hds-us-nt-012.ninjatrader.com/31655)
2026-08-29 11:02:49:435|1|4|Restoring workspace 'Getting Started (Basic)'...
2026-08-29 11:03:41:323|1|4|Global simulation mode enabled
2026-08-29 11:25:54:038|0|4|Error on requesting bars series: 'Unknown instrument 'NQCONT 09-25''
2026-08-29 11:26:13:668|0|4|Error on requesting bars series: 'Unknown instrument 'NQCONT''
2026-08-29 11:27:19:218|0|4|Error on requesting bars series: 'Unknown instrument 'NQCONT''
2026-08-29 11:29:30:624|0|4|Error on requesting bars series: 'Unknown instrument 'NQCONT''
2026-08-29 11:30:07:336|0|4|Error on requesting bars series: 'Unknown instrument 'NQCONT 09-25''
2026-08-29 11:33:38:297|0|4|Error on requesting bars series: 'Unknown instrument 'NQCONT 09-25''
2026-08-29 11:33:54:226|0|4|Error on requesting bars series: 'Unknown instrument 'NQCONT''
2026-08-29 11:34:06:945|0|4|Error on requesting bars series: 'Unknown instrument 'NQCONT''
2026-08-29 11:47:58:561|0|4|Error on requesting bars series: 'Unknown instrument 'NQCONT''
2026-08-29 11:49:52:080|0|4|Error on requesting bars series: 'Unknown instrument 'NQCONT''
2026-08-29 11:52:35:776|0|4|Error on requesting bars series: 'Unknown instrument 'NQCONT''
2026-08-29 11:57:55:833|0|4|Error on requesting bars series: 'Unknown instrument 'NQCONT''
2026-08-29 11:58:08:207|0|4|Error on requesting bars series: 'Unknown instrument 'NQCONT 09-25''
2026-08-29 11:58:59:668|0|4|Error on requesting bars series: 'Unknown instrument 'NQCONT''
2026-08-29 11:59:19:337|0|4|Error on requesting bars series: 'Unknown instrument 'NQCONT''
2026-08-29 12:01:38:549|0|4|Error on requesting bars series: 'Unknown instrument 'NQCONT''
2026-08-29 12:01:50:840|0|4|Error on requesting bars series: 'Unknown instrument 'NQCONT''
echo ----- trace lines mentioning NQCONT or import, CR stripped
----- trace lines mentioning NQCONT or import, CR stripped
/usr/bin/grep -h -a -i -E 'NQCONT|import' "$R/trace/trace.20260816.00000.txt" "$R/trace/trace.20260829.00000.txt" "$R/trace/trace.20260829.00001.txt" | tr -d '\r' | cut -c1-300
2026-08-16 08:18:24:424 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT DEC29' from='8/11/2026 12:00:00 AM' to='8/14/2026 12:00:00 AM' period='1 Minute'
2026-08-16 08:18:24:455 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT DEC29' from='8/18/2016 12:00:00 AM' to='8/17/2026 12:00:00 AM' period='Daily'
2026-08-29 09:44:55:648 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT DEC29' from='8/24/2026 12:00:00 AM' to='8/28/2026 12:00:00 AM' period='1 Minute'
2026-08-29 09:44:55:802 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT DEC29' from='8/31/2016 12:00:00 AM' to='8/30/2026 12:00:00 AM' period='Daily'
2026-08-29 09:45:19:583 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT DEC29' from='8/26/2026 12:00:00 AM' to='8/28/2026 11:59:59 PM' period='1 Tick'
2026-08-29 09:45:25:631 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT DEC29' from='8/24/2026 12:00:00 AM' to='8/28/2026 12:00:00 AM' period='1 Minute'
2026-08-29 09:50:02:052 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT DEC29' from='8/24/2026 12:00:00 AM' to='8/28/2026 12:00:00 AM' period='1 Minute'
2026-08-29 09:50:02:084 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT DEC29' from='8/31/2016 12:00:00 AM' to='8/30/2026 12:00:00 AM' period='Daily'
2026-08-29 09:54:01:419 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT DEC29' from='6/20/2026 12:00:00 AM' to='6/20/2026 12:00:00 AM' period='1 Minute'
2026-08-29 09:56:52:395 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT' from='6/20/2026 12:00:00 AM' to='6/20/2026 12:00:00 AM' period='1 Minute'
2026-08-29 09:56:52:459 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT' from='8/24/2026 12:00:00 AM' to='8/28/2026 12:00:00 AM' period='1 Minute'
2026-08-29 10:00:22:599 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT SEP25' from='6/20/2026 12:00:00 AM' to='6/20/2026 12:00:00 AM' period='1 Minute'
2026-08-29 10:00:22:669 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT SEP25' from='8/24/2026 12:00:00 AM' to='8/28/2026 12:00:00 AM' period='1 Minute'
2026-08-29 10:14:52:950 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT' from='6/20/2026 12:00:00 AM' to='6/20/2026 12:00:00 AM' period='1 Minute'
2026-08-29 10:14:52:995 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT' from='8/24/2026 12:00:00 AM' to='8/28/2026 12:00:00 AM' period='1 Minute'
2026-08-29 10:16:08:991 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT SEP25' from='6/20/2026 12:00:00 AM' to='6/20/2026 12:00:00 AM' period='1 Minute'
2026-08-29 10:16:09:085 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT SEP25' from='8/24/2026 12:00:00 AM' to='8/28/2026 12:00:00 AM' period='1 Minute'
2026-08-29 10:16:11:310 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT' from='6/20/2026 12:00:00 AM' to='6/20/2026 12:00:00 AM' period='1 Minute'
2026-08-29 10:16:11:382 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT' from='8/24/2026 12:00:00 AM' to='8/28/2026 12:00:00 AM' period='1 Minute'
2026-08-29 10:17:25:896 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT' from='12/31/2025 12:00:00 AM' to='7/31/2026 12:00:00 AM' period='1 Minute'
2026-08-29 10:18:15:257 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT' from='12/31/2025 12:00:00 AM' to='7/31/2026 12:00:00 AM' period='1 Minute'
2026-08-29 10:18:21:399 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT' from='12/31/2025 12:00:00 AM' to='7/31/2026 12:00:00 AM' period='1 Minute'
2026-08-29 10:40:22:275 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT SEP25' from='12/31/2025 12:00:00 AM' to='7/31/2026 12:00:00 AM' period='1 Minute'
2026-08-29 11:25:53:959 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT SEP25' from='1/2/2026 12:00:00 AM' to='8/28/2026 12:00:00 AM' period='1 Minute'
2026-08-29 11:26:13:593 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT' from='7/20/2026 12:00:00 AM' to='8/28/2026 12:00:00 AM' period='1 Minute'
2026-08-29 11:27:19:177 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT' from='7/20/2026 12:00:00 AM' to='8/28/2026 12:00:00 AM' period='1 Minute'
2026-08-29 11:29:30:584 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT' from='7/20/2026 12:00:00 AM' to='8/28/2026 12:00:00 AM' period='1 Minute'
2026-08-29 11:30:07:270 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT SEP25' from='1/2/2026 12:00:00 AM' to='8/28/2026 12:00:00 AM' period='1 Minute'
2026-08-29 11:33:38:261 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT SEP25' from='1/2/2026 12:00:00 AM' to='8/28/2026 12:00:00 AM' period='1 Minute'
2026-08-29 11:33:54:114 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT' from='1/2/2026 12:00:00 AM' to='8/28/2026 12:00:00 AM' period='1 Minute'
2026-08-29 11:34:06:900 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT' from='1/2/2026 12:00:00 AM' to='8/28/2026 12:00:00 AM' period='1 Minute'
2026-08-29 11:34:20:919 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT SEP25' from='8/24/2026 12:00:00 AM' to='8/28/2026 12:00:00 AM' period='1 Minute'
2026-08-29 11:34:21:023 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT SEP25' from='12/1/2025 12:00:00 AM' to='8/30/2026 12:00:00 AM' period='Daily'
2026-08-29 11:34:57:505 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT SEP25' from='1/2/2026 12:00:00 AM' to='8/28/2026 12:00:00 AM' period='1 Minute'
2026-08-29 11:35:05:927 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT' from='1/2/2026 12:00:00 AM' to='8/28/2026 12:00:00 AM' period='1 Minute'
2026-08-29 11:35:05:992 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT' from='8/31/2016 12:00:00 AM' to='8/28/2026 12:00:00 AM' period='Daily'
2026-08-29 11:35:34:052 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT' from='1/2/2026 12:00:00 AM' to='8/28/2026 12:00:00 AM' period='1 Minute'
2026-08-29 11:36:22:853 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT' from='1/2/2026 12:00:00 AM' to='8/28/2026 12:00:00 AM' period='1 Minute'
2026-08-29 11:37:57:254 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT' from='8/24/2026 12:00:00 AM' to='8/28/2026 12:00:00 AM' period='1 Minute'
2026-08-29 11:39:36:524 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT SEP25' from='8/24/2026 12:00:00 AM' to='8/28/2026 12:00:00 AM' period='1 Minute'
2026-08-29 11:40:21:365 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT SEP25' from='8/24/2026 12:00:00 AM' to='8/28/2026 12:00:00 AM' period='1 Minute'
2026-08-29 11:41:38:839 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT SEP25' from='1/2/2026 12:00:00 AM' to='8/28/2026 12:00:00 AM' period='1 Minute'
2026-08-29 11:41:43:811 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT' from='1/2/2026 12:00:00 AM' to='8/28/2026 12:00:00 AM' period='1 Minute'
2026-08-29 11:44:22:677 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT SEP25' from='1/2/2026 12:00:00 AM' to='8/28/2026 12:00:00 AM' period='1 Minute'
2026-08-29 11:47:11:438 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT' from='7/20/2026 12:00:00 AM' to='8/28/2026 12:00:00 AM' period='1 Minute'
2026-08-29 11:47:58:521 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT' from='7/20/2026 12:00:00 AM' to='8/28/2026 12:00:00 AM' period='1 Minute'
2026-08-29 11:49:52:041 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT' from='7/20/2026 12:00:00 AM' to='8/28/2026 12:00:00 AM' period='1 Minute'
2026-08-29 11:52:35:738 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT' from='7/20/2026 12:00:00 AM' to='8/28/2026 12:00:00 AM' period='1 Minute'
2026-08-29 11:57:55:782 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT' from='7/20/2026 12:00:00 AM' to='8/28/2026 12:00:00 AM' period='1 Minute'
2026-08-29 11:58:08:147 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT SEP25' from='1/2/2026 12:00:00 AM' to='8/28/2026 12:00:00 AM' period='1 Minute'
2026-08-29 11:58:59:615 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT' from='7/20/2026 12:00:00 AM' to='8/28/2026 12:00:00 AM' period='1 Minute'
2026-08-29 11:59:19:301 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT' from='12/31/2025 12:00:00 AM' to='8/27/2026 12:00:00 AM' period='1 Minute'
2026-08-29 12:01:38:506 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT' from='7/20/2026 12:00:00 AM' to='8/28/2026 12:00:00 AM' period='1 Minute'
2026-08-29 12:01:50:802 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT' from='7/20/2026 12:00:00 AM' to='8/28/2026 12:00:00 AM' period='1 Minute'
````

**Evidence C: Config.xml global merge policy, UI.xml recent and pinned instruments.** These lines are in the Q6 evidence block, `q6.out`, under `----- Config.xml and UI.xml`.

---

## Q3. Can a Future instrument with Expiry 09-25 hold and chart bars from 2021-03?

**Answer.**
1. **SPEC-SILENT / UNVERIFIED.** No on-disk source says whether NT8 filters stored or served bars by a contract's life. Session 52 named this "the load-bearing unknown" (report lines 254-256). Its expectation that expiry is metadata, not a filter, is graded there as INFERRED and weak (lines 166-170).
2. **Storage and serving are separate questions.** This install shows that a folder can be keyed to a name. Nothing on disk shows bars outside a contract's life being stored or served.
3. **The test that decides it** (pre-registered; Amear runs it; nothing gets deleted):
   - **(i) Storage.** Import a copy named `NQCONT 09-25.Last.txt` using the same Format, Data Type and Time Zone as before. Then list `db\minute\NQCONT 09-25\`. About 1,710 files from `20210307` to `20260720` means storage does not filter. A short span near 2025 means it does.
   - **(ii) Serving.** Open a 1-minute chart of `NQCONT SEP25` with a Data Series range of 2021-03-08 to 2021-03-12. Candles mean expiry is not a serving filter. A blank chart, or an `Unknown instrument 'NQCONT 09-25'` log line, means it is (or that the merge or rollover mapping intervenes).
   - Read the Control Center Log after each step (reference §2).

   Session 52's "Fix A" proposed `NQCONT 12-25` with a new contract-month row. The variant above reuses the existing 09-25 row, so it needs no instrument edit for step (i).

**Evidence:** the session 52 Q5 and open-question text is in Q1 Evidence G and in the block below. Command as run: `bash -v docs3.sh 2>&1 | tee docs3.out`
````text
cd /Volumes/Sensidine/Praxis.build
sed -n '70,122p' docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md
establishes it.**

The chain:

1. **VERIFIED (reference §2):** the import filename convention is
   `<instrument>.<DataType>.txt`, and for a dated contract the instrument token
   carries the month **with a space** — the documented example is
   `ES 12-09.Bid.txt`, and for PRAXIS NQ the reference gives `NQ 12-25.Last.txt`.
2. **Your report:** the file was `NQCONT.Last.txt` — **no month token** — and the
   data landed in `db\minute\NQCONT\`, a folder with **no month suffix**.
3. **VERIFIED (reference §2):** minute data lands under
   `db\minute\<instrument>\`, so NT8 wrote it to the literal name it was given.
4. **Your report:** charting `NQCONT` resolves to `NQCONT September 25`.

**INFERRED conclusion:** the import keyed the bars to the bare string `NQCONT`.
The chart, resolving a **Future** through its contract-month table, asks for a
*dated* series — something like `NQCONT 09-25`. It looks in the expiry-suffixed
folder, finds nothing, and renders blank.

**The data is on disk, filed under a name nothing ever asks for.** Import writes by
literal filename; chart lookup reads by resolved expiry. The two never meet.

That is consistent with every symptom you reported, including the refusal to save
with zero contract months — a Future without an expiry table has nothing to
resolve *to*.

---

## Q3 — Can the data be loaded under the literal name?

**Partly VERIFIED, and this is your cheapest next move.**

**VERIFIED (reference §1e):** `Tools > Historical Data` is a vertical accordion
whose **`Loaded`** section exists to *"access/manage all historical data"* and
inspect what is loaded.

**UNVERIFIED:** whether `Loaded` can *chart* a series, or only list and manage it.
The reference explicitly records the `Export` and `Get Market Replay` sections as
never expanded during capture; `Loaded` was captured but its capabilities were not
enumerated.

### Do this before anything else — 30 seconds, and it discriminates

**`Tools > Historical Data` → expand `Loaded` → find the NQCONT records and read
me the exact instrument name they are filed under.**

- **Filed as bare `NQCONT`, ~1,857,362 records** → confirms Q2's diagnosis
  outright. Fix A or Fix B below applies, and you can stop guessing.
- **Filed as `NQCONT 09-25` or any dated form** → my diagnosis is **wrong**, the
  problem is elsewhere, and nothing below should be actioned until we re-think.

**One observation kills or confirms the whole analysis.** Make it first.

echo ----- s52 160-225
----- s52 160-225
sed -n '160,225p' docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md

Your data spans **2021-03-07 → 2026-07-20**. No single real quarterly contract
lives five years. If NT8 filters bars by expiry window, Fix A fails. If expiry is
only metadata for rollover and display — which is what I'd expect from a system
that stores bars in per-expiry folders and serves whatever is in them — Fix A works
regardless of dates.

**INFERRED, and stated as the weaker claim it is:** I expect expiry to be metadata,
not a filter, because §2's verification step is *"confirm files/bar counts exist
for the imported instrument"* — a folder-contents check with no mention of date
validation. **But this project has been wrong twice on well-cited static reads, and
this has exactly that shape. Test it; do not trust it.**

---

## Q6 — Official docs and forum threads

**Cannot execute. No web tools.** See the limitation at the top.

---

# DELIVERABLE — replacement procedure

**Gate: run the `Loaded` check from Q3 first.** Everything below assumes it shows
bare `NQCONT`.

## FIX A — give the filename a contract month, re-import *(try this first)*

**Rationale:** works *with* NT8's resolution instead of against it. Changes only a
filename. Costs one re-import.

1. On the Mac side, copy — **do not rename or move** the original:
   `NQ-continuous-1min.nt8import.txt` → `NQCONT 12-25.Last.txt`
   **Space before `12-25`.** That spacing is VERIFIED from the reference's
   documented examples (`ES 12-09.Bid.txt`, `NQ 12-25.Last.txt`).
2. `Tools > Instruments` → edit `NQCONT` → contract months: **one entry only**,
   **December 2025**, **offset `0`**, roll date **after 2026-07-20** (your data's
   last bar).
3. **Set Merge Policy = `DoNotMerge`.** VERIFIED as an option in reference §6:
   *"DoNotMerge (single expiry only)."* You have exactly one expiry and no real
   rollover — merging can only introduce artefacts.
4. `Tools > Historical Data > Import`: Format `NinjaTrader (end of bar
   timestamps)`, Data Type `Last`, **Time Zone `US Eastern`**, select the new file.
5. Chart **`NQCONT 12-25`** explicitly — the dated symbol, not the bare root.

**Report:** whether bars from **2021** appear, or only bars near Dec-2025. That
single answer resolves Q5 for good, and it is worth recording either way.

**Known risk:** if NT8 date-filters by expiry, you get a short window instead of
five years. **That is a real result** — report it, don't work around it.

## FIX B — non-expiring instrument type *(if A fails, and it needs one check)*

**Rationale:** removes contract-month resolution entirely, so bare-name lookup
finds the folder you already have. **No re-import needed.**

1. `Tools > Instruments` → create a new instrument, e.g. `NQCONT2`, with a type
   that has **no expiry** — `Index`, `CFD` or `Stock`, whichever the dialog offers
   that accepts a tick size and a point value.
2. Tick size `0.25`, point value `20`, currency `USD`, trading hours
   `CME US Index Futures RTH`.
3. Import `NQCONT2.Last.txt` and chart the bare name.

**⚠️ The check that decides whether B is usable at all — do not skip it.**
**UNVERIFIED:** whether NT8 honours **point value** for P&L on a non-Future type.
If it treats the instrument as 1 unit = $1, every P&L number is wrong by a factor
echo ----- s52 250-270
----- s52 250-270
sed -n '250,270p' docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md

1. **In NT8 8.1.x, does charting a `Future` instrument by root name always resolve
   through the contract-month table to a dated expiry?** Can a Future ever serve
   data stored under its bare name? Cite `instruments.htm`, `merge_policy.htm`.
2. **Does NT8 filter imported historical bars by the contract's expiry window**,
   or serve whatever is in `db\minute\<instrument>\` regardless of date? **This is
   the load-bearing unknown** — it decides Fix A.
3. **What exactly does the contract-month `offset` field do?** Real example: entered
   December 2025, NT8 resolved to September 25.
4. **Documented practice for a synthetic continuous instrument used only for
   backtesting imported stitched data.** Search NinjaTrader forums and futures.io.
   This is a common algo-trader workflow; there should be threads.
5. **Does NT8 honour tick size and point value for P&L on non-Future instrument
   types** (Index / CFD / Stock)? Decides Fix B.
6. **Is `<ROOT> ##-##` ever usable with imported data**, or is it strictly
   provider-served? Reference §6 says provider support is required — **confirm or
   refute that.**

Require pasted source text and a URL per answer. Anything unsourced comes back
marked UNVERIFIED, same as here.

echo ----- s53 1-50
----- s53 1-50
sed -n '1,50p' docs/reports/2026-08-29-session53-vm-checks-A-and-B.md
PRAXIS - session 53 - TWO VM CHECKS. Both read-only. Change no setting.

Issued by praxis-master, 2026-08-29. Executor: Amear, by hand, on the Windows VM.
This file exists on disk so the brief survives transmission. Prior briefs were
garbled twice in the clipboard path; a citable artifact is the fix.


CHECK A - THE ANALYZER "unknown instrument NQCONT"

Standing facts, observed, not recalled:
  - Data is filed under the exact bare name NQCONT, no dated suffix,
    approx 1,857,362 records, in db\minute\NQCONT. (Amear, today.)
  - The Strategy Analyzer resolves bare NQCONT to NQCONT 09-2025 and throws
    unknown-instrument. (Amear, session 52.)
  - A Stock-typed duplicate NQCONT was deleted and the resolution persisted
    UNCHANGED, so the duplicate was not the cause. (Amear, session 52.)

A1. POSITIVE CONTROL. Run this one first.

Open Strategy Analyzer. Select any built-in NT8 instrument that already has
data - the standard NQ front-month contract is fine. Set the SAME 1-minute
interval and the SAME date range you used for NQCONT. Run it.

  - If it ALSO errors on requesting bars: the fault is in the data-series
    layer, not in NQCONT specifically. That supports the "records built but no
    usable bars series" idea.
  - If it RUNS CLEAN: the fault is specific to NQCONT's own definition, and the
    bars-series idea is dead.

FALSIFIER: a clean run on the control kills the bars-series theory outright.

A2. READ NQCONT'S DEFINITION, verbatim. Change nothing.

Tools, then Instruments. Find NQCONT. Open its properties. Read back, exactly
as printed, four things:

  1. Instrument type
  2. Expiry, or contract month, if any field carries one
  3. Merge Policy
  4. Whether any contract-month rows are listed beneath it, such as 09-25

WHY THIS FOUR: your data is filed under the bare name NQCONT. The Analyzer is
asking for NQCONT 09-2025. Those are different strings, so "unknown instrument"
is the correct answer to the wrong question. Something rewrites the request from
the root name into a contract month. These four fields are where that would
live.

FALSIFIER: if the definition shows no expiry, no contract months and no merge
policy, then nothing in the definition explains the rewrite and the framing
above is wrong. That is a useful answer, not a failed check.
````

---

## Q4. Must the Stock row be removed or renamed for the Future to be selectable as plain `NQCONT`?

**Answer.**
1. **The Future row is already selectable, as `NQCONT SEP25` or `NQCONT ##-##`.** It is never selectable as plain `NQCONT`. A Future's names all carry a month (Q1/Q2; INFERRED from the folder pattern and the trace pairing).
2. **No on-disk source says what deleting or renaming the Stock row would do (SPEC-SILENT).** Specifically, it is not documented whether that would make bare `NQCONT` resolve to the Future, or whether it would orphan or delete the existing `db\minute\NQCONT\` files. Removal is not required to reach the Future row, and it carries an unknown risk to the only imported copy on the VM. By the brief's rule, it is not a step Code can take without Amear.
   **ADDED (a9d worker 4, finding 7).** Datum (INFERRED): `NQCONT 12-29` was requested at Daily period three times (2026-08-16 08:18:24, 2026-08-29 09:44:55 and 09:50:02), and Daily requests do create `db/day/<name>` folders (`db/day/NQCONT 09-25` was created 11:34:21, the second of the SEP25 Daily request). Yet no `12-29` folder survives anywhere in `db/`, and no 12-29 contract row remains in the sqlite (OBSERVED, `docs/reports/2026-10-31-a9d-adversarial.md` finding 7). Removing a row or contract month may remove its data folders; another cause cannot be excluded. Treat Stock-row removal, and any edit that removes a Future contract month, as a possible deletion of `db\minute\NQCONT\` or `db\minute\NQCONT 09-25\`.
3. **Session 52 quote** (DECISION_LOG `2026-08-29T12:05:00Z`, Q1 Evidence F): "The `Stock` duplicate was confirmed empty against Historical Data and deleted. **The auto-resolution to `NQCONT 09-2025` PERSISTED afterward, unchanged.**"
4. **That inference was later voided.** Row `2026-08-29T19:30:00Z` records: "The `Stock`-typed `NQCONT` IS STILL PRESENT … If the `Stock` duplicate was never actually deleted — or the deletion did not persist — then that inference … is VOID".
5. **OBSERVED:** the rescued sqlite (mtime 11:33) still holds Stock `NQCONT` Id `…605`. Its contract row Id `…770941` immediately follows the Future's 09-25 row `…770940`.
   - INFERRED, weak, and depending on Ids being allocated sequentially: the Stock row was created after the Future's 09-25 row was added.
   - The disk cannot tell "never deleted" apart from "recreated".
6. **On "Confirmed empty against Historical Data".** On disk, the data sits under the name `NQCONT`, which is the Stock row's name. So the session 52 report that the Stock row was "confirmed empty" conflicts with the disk. What Amear was shown at the time is UNVERIFIED.
7. **`Tools > Historical Data > Loaded`.** Session 52 report lines 101-120 (Q1 Evidence G / Q3 block) cite reference §1e: `Loaded` exists to "access/manage all historical data". Session 52 asked Amear to "read me the exact instrument name they are filed under". No source says whether `Loaded` shows instrument **type** (SPEC-SILENT). So `Loaded` can tell `NQCONT` from `NQCONT 09-25`, but it cannot tell Stock `NQCONT` from Future `NQCONT` (INFERRED). That is the readback to use: after a re-import, `Loaded` should list an `NQCONT 09-25` entry (INFERRED).

---

## Q5. What is the save-as-default control for Strategy Analyzer settings?

**Answer.**
1. **REPORTED BY AMEAR** (2026-10-28 voice notes, line 33): the Analyzer settings were "Saved as template **"Praxis Backtest"** and as default." Line 52: "Amear is re-saving the "Praxis Backtest" default template with the corrected session."
2. The run-3 screenshot record (line 5) notes a label `template` at the lower right of the Settings pane. This is a Claude-transcribed screenshot, so it is a recorded observation, not observed by me.
3. **The exact control text** (a `Template` button and whatever menu item saves it as default) is **UNVERIFIED**. The NT8 reference has no "save as default" text: grep finds only "session template dropdown" (lines 150, 156, 213).
4. **OBSERVED:** `templates/StrategyAnalyzer/` exists in the rescued install and is empty. "Praxis Backtest" was saved on Fusion (2026-10-28), after the rescue (2026-09-29). Its file on Fusion is expected under `Documents\NinjaTrader 8\templates\StrategyAnalyzer\` (INFERRED from the folder name).
5. **The trap Amear named is already loaded (REPORTED, line 33):** the current default template's instrument field is plain `NQCONT`, which is the Stock row (Q1, INFERRED). The default has to be **re-saved after** the instrument is set to the Future name (`NQCONT SEP25` or `##-##`). Readback: open a fresh Analyzer and read the instrument field.

**Evidence A: template and default greps** (all with `/usr/bin/grep`). Command as run: `bash -v q5.sh 2>&1 | tee q5.out`
````text
cd /Volumes/Sensidine/Praxis.build
/usr/bin/grep -n -i -E 'save as default|as default|set as default|template' docs/reference/2026-07-24-nt8-windows-reference.md
150:4. **Time frame:** **Start date** / **End date** · **Trading hours** = **session template dropdown** — for PRAXIS RTH select **"CME US Index Futures RTH"** · **Break at EOD**.
156:- 🔲 **TODO (residual gap):** the **"CME US Index Futures RTH"** template's exact printed session hours were **not** captured. Verify **09:30–16:00 ET** equivalence via `Tools > Trading Hours` and record the printed CT hours here. (Tracked in the follow-up bead — see footer.)
213:1. `Tools > Trading Hours` — exact printed hours of the **CME US Index Futures RTH** template (confirm 09:30–16:00 ET). *(§4)*
echo ----- docs-wide: save-as-default phrasing, any file
----- docs-wide: save-as-default phrasing, any file
/usr/bin/grep -r -n -i -E 'save as default|saved as default|set as default|save.{0,20}default' docs | cut -c1-300
docs/reports/2026-10-31-voice-session-notes.md:55:3. **Reminder Amear asked for:** once the Future row loads and the new baseline run is done, **save those Strategy Analyzer settings as the default**, so he isn't re-entering them every run and can't silently fall back to the Stock row through human 
docs/reports/2026-10-31-voice-session-notes.md:56:4. **Instruction to Claude Code:** when the Future row is loading and the new baseline is set, **prepare a handoff for Amear to bring back to the Claude.ai Praxis channel.** It should cover what changed, the new baseline numbers, what is still open, 
docs/reports/2026-10-30-run3-backtest-screenshot-record.md:107:**Amear's ruling (DECISION_LOG `2026-10-30T22:22:00Z`; `docs/reports/2026-10-28-voice-session-notes.md:45-60`):** discrepancy (A) was real. Run 3 ran on `CME FX Futures RTH`. The strategy anchors on `Bars.IsFirstBarOfSession` for a 09:30
docs/reports/2026-10-30-zyd-worker10-closing-adversarial.md:55:| 37 | E37: Analyzer template already at Slippage 2 / Standard (REPORTED) | notes:33; :450 | `**Slippage 2** · **Order fill resolution Standard**. Saved as template **"Praxis Backtest"**`; `template re-saved as default` | HOLDS |
echo ----- docs-wide: Template near Analyzer, file counts
----- docs-wide: Template near Analyzer, file counts
/usr/bin/grep -r -l -i 'template' docs | wc -l
      79
/usr/bin/grep -r -n -i -E 'analyzer.{0,80}template|template.{0,80}analyzer' docs | cut -c1-300
docs/reports/2026-08-29-session53-w3-q3-rth-timezone.md:187:- **Line 150 — "session template dropdown".** This is the **Trading hours** field inside the Strategy Analyzer's Time-frame panel, where one *picks a template* (e.g. "CME US Index Futures RTH"). It is a template selector, **not** a time-z
docs/reports/2026-10-30-3gm-worker1-checklist.md:708:// 1-MINUTE NQ series with an RTH (09:30-16:00 ET) session template in the Strategy Analyzer.
docs/reports/2026-10-30-zyd-rulings-append.md:77:+- Analyzer template "Praxis Backtest": already at Slippage 2 / Standard (REPORTED); no change.
docs/reports/2026-10-31-voice-session-notes.md:55:3. **Reminder Amear asked for:** once the Future row loads and the new baseline run is done, **save those Strategy Analyzer settings as the default**, so he isn't re-entering them every run and can't silently fall back to the Stock row through human 
docs/reports/2026-07-16-4uu-noise-area-strategy.md:39:2. **Data.** Load the b2-data NQ **1-minute** series (per `2026-07-15 b2-data` acquisition spec). Confirm the chart/Analyzer uses an **RTH 09:30–16:00 ET** session template — the band math assumes it.
docs/reports/2026-07-16-4uu-noise-area-strategy.md:40:3. **Strategy Analyzer run.** Add `PraxisNoiseAreaBreakout` on NQ 1-min, RTH template. Only ExitMode and Contracts are Inputs (leave at BandOrVWAP, 1); Lookback=14 and σ-mult=1.0 are compiled-in consts, not shown/optimizable in the Analyzer. Bac
docs/reports/2026-10-31-7zq-handtest-checklist.md:36:**0.1 — FIRST: check the trading-hours template.** In the Strategy Analyzer, `Trading hours` must
docs/reports/2026-10-30-zyd-f3-artifact.md:216:+- **Void clause (VERBATIM, DECISION_LOG `2026-08-29T00:10:00Z`):** *"We accept Standard resolution on 1-minute bars. Band-edge slippage widened to [N]. Fills are optimistic and the report states so. If the VM measurement shows NT8 errors or demands a s
docs/reports/2026-10-30-zyd-f3-artifact.md:235:+- Analyzer template "Praxis Backtest": already at Slippage 2 / Standard (REPORTED); no change.
docs/reports/2026-10-30-zyd-f3-artifact.md:466:- **Analyzer template "Praxis Backtest":** already Slippage 2 / Standard (REPORTED).
docs/reports/2026-10-30-3gm-fidelity-check.md:610:// 1-MINUTE NQ series with an RTH (09:30-16:00 ET) session template in the Strategy Analyzer.
docs/reports/2026-10-30-run3-backtest-screenshot-record.md:5:**Window:** NinjaTrader 8 Strategy Analyzer, Display = `Summary ($)`, tab `Analyzer`, label `template` at the lower right of the Settings pane. Windows taskbar clock `6:12 PM 2026-10-30`, `13°C Partly sunny`. A small `Trend` slider box fl
docs/reports/2026-10-30-zyd-worker3-fix.md:16:- F10: added the S6 F4 (MFFU) bullet after the Analyzer-template bullet.
docs/reports/2026-10-30-zyd-worker10-closing-adversarial.md:55:| 37 | E37: Analyzer template already at Slippage 2 / Standard (REPORTED) | notes:33; :450 | `**Slippage 2** · **Order fill resolution Standard**. Saved as template **"Praxis Backtest"**`; `template re-saved as default` | HOLDS |
echo ----- reference screenshot assets named for analyzer
----- reference screenshot assets named for analyzer
ls docs/reference/assets/nt8-2026-07-24/ | /usr/bin/grep -i -E 'analy|template|strateg'
05-cc-strategies.png
11-strategy-analyzer.png
14-chart-strategies-dialog.png
````

**Evidence B: where "re-saved as default" comes from; the rescued `templates/` tree.** Command as run: `bash -v q5b.sh 2>&1 | tee q5b.out`
````text
cd /Volumes/Sensidine/Praxis.build
/usr/bin/grep -r -n -i -E 're-saved as default|Praxis Backtest' --include='*.md' . | cut -c1-400
./docs/reports/2026-10-30-3gm-worker1-checklist.md:698:- **Strategy Analyzer settings:** PraxisNoiseAreaBreakout · NQCONT · Last · Minute 1 · trading hours CME US Index Futures RTH · ExitMode BandOrVWAP · Contracts 1 · Include commission True · Account Sim101 · **Slippage 2** · **Order fill resolution Standard**. Saved as template **"Praxis Backtest"** and as default.
./docs/reports/2026-10-30-zyd-rulings-append.md:77:+- Analyzer template "Praxis Backtest": already at Slippage 2 / Standard (REPORTED); no change.
./docs/reports/2026-10-30-3gm-worker2-timing-orders-count.md:51:- **Strategy Analyzer settings:** PraxisNoiseAreaBreakout · NQCONT · Last · Minute 1 · trading hours CME US Index Futures RTH · ExitMode BandOrVWAP · Contracts 1 · Include commission True · Account Sim101 · **Slippage 2** · **Order fill resolution Standard**. Saved as template **"Praxis Backtest"** and as default.
./docs/reports/2026-10-31-7zq-handtest-checklist.md:38:(DECISION_LOG `2026-10-30T22:22:00Z`, WHO: amear). The saved "Praxis Backtest" template carried the
./docs/reports/2026-10-30-zyd-f3-artifact.md:216:+- **Void clause (VERBATIM, DECISION_LOG `2026-08-29T00:10:00Z`):** *"We accept Standard resolution on 1-minute bars. Band-edge slippage widened to [N]. Fills are optimistic and the report states so. If the VM measurement shows NT8 errors or demands a secondary series rather than falling back silently, this row is void and the assumption is re-decid
./docs/reports/2026-10-30-zyd-f3-artifact.md:235:+- Analyzer template "Praxis Backtest": already at Slippage 2 / Standard (REPORTED); no change.
./docs/reports/2026-10-30-zyd-f3-artifact.md:466:- **Analyzer template "Praxis Backtest":** already Slippage 2 / Standard (REPORTED).
./docs/reports/2026-10-30-3gm-fidelity-check.md:1077:**(A) Trading hours = `CME FX Futures RTH`.** The notes (`:33`) report the saved template "Praxis Backtest" as `trading hours CME US Index Futures RTH`. The screenshot shows a different template selected for the run on screen. The
./docs/reports/2026-10-28-voice-session-notes.md:33:- **Strategy Analyzer settings:** PraxisNoiseAreaBreakout · NQCONT · Last · Minute 1 · trading hours CME US Index Futures RTH · ExitMode BandOrVWAP · Contracts 1 · Include commission True · Account Sim101 · **Slippage 2** · **Order fill resolution Standard**. Saved as template **"Praxis Backtest"** and as default.
./docs/reports/2026-10-28-voice-session-notes.md:47:- **Run 3 is INVALID. Trading hours were set to `CME FX Futures RTH`, not `CME US Index Futures RTH`.** The strategy depends on an RTH session that opens at 09:30 ET. `PraxisNoiseAreaBreakout.cs:37` says so, and `:147-152` set the session anchor `todayOpen = Open[0]` on `Bars.IsFirstBarOfSession`. With the wrong template, the open anchor, the pre
./docs/reports/2026-10-28-voice-session-notes.md:52:- Settings are the same as run 3 except **Trading hours = CME US Index Futures RTH**. Amear is re-saving the "Praxis Backtest" default template with the corrected session.
./docs/reports/2026-10-30-run3-backtest-screenshot-record.md:93:**(A) Trading hours = `CME FX Futures RTH`.** The notes (`:33`) report the saved template "Praxis Backtest" as `trading hours CME US Index Futures RTH`. The screenshot shows a different template selected for the run on screen. The code hard-codes a 09:30–16:00 ET session (`ninjascript/PraxisNoiseAreaBreakout.cs` lines 58, 189, 196) 
./docs/reports/2026-10-30-run3-backtest-screenshot-record.md:107:**Amear's ruling (DECISION_LOG `2026-10-30T22:22:00Z`; `docs/reports/2026-10-28-voice-session-notes.md:45-60`):** discrepancy (A) was real. Run 3 ran on `CME FX Futures RTH`. The strategy anchors on `Bars.IsFirstBarOfSession` for a 09:30 ET session (`ninjascript/PraxisNoiseAreaBreakout.cs:37`, `:147-152`), so the open anchor, prior c
./docs/reports/2026-10-30-zyd-worker10-closing-adversarial.md:55:| 37 | E37: Analyzer template already at Slippage 2 / Standard (REPORTED) | notes:33; :450 | `**Slippage 2** · **Order fill resolution Standard**. Saved as template **"Praxis Backtest"**`; `template re-saved as default` | HOLDS |
./DECISION_LOG.md:442:- [2026-10-30T21:36:30Z] **WHO: amear** | PROPOSED BY: amear | APPROVED BY: amear, 2026-10-28 (voice session), reaffirmed in this session's opening message | WHAT: **F3 `[N]` IS SET: band-edge slippage = 2 ticks per side ($10/side at $5/tick; with $2.96 commission ≈ $22.96 per round trip). Fill resolution = Standard, on 1-minute bars. This FILLS the conditional ruled at `20
./DECISION_LOG.md:443:- [2026-10-30T21:37:00Z] WHO: praxis-master | WHO OBSERVED: amear (by hand on Fusion; voice-reported; no screenshots seen by any Claude) | WHAT: **INTAKE OF THE 2026-10-30 HAND-RUN RESULTS, graded REPORTED BY AMEAR throughout.** (a) `PraxisNoiseAreaBreakout.cs` copied from `ninjascript/` (Mac sha256 `35393823…2752265` = commit `719ab11`, re-hashed by the master this turn) i
./DECISION_LOG.md:450:- [2026-10-30T22:22:00Z] **WHO: amear** | WHO OBSERVED: amear (his screenshots; the master saw only the run-3 image) | WHAT: **(1) RUN 3 IS RULED INVALID, not a result.** Trading hours were `CME FX Futures RTH`; the strategy anchors on `Bars.IsFirstBarOfSession` at a 09:30 ET session (`PraxisNoiseAreaBreakout.cs:37`, `:147-152`), so the open anchor, prior close, VWAP anchor a
./DECISIONS.md:264:- **Void clause (VERBATIM, DECISION_LOG `2026-08-29T00:10:00Z`):** *"We accept Standard resolution on 1-minute bars. Band-edge slippage widened to [N]. Fills are optimistic and the report states so. If the VM measurement shows NT8 errors or demands a secondary series rather than falling back silently, this row is void and the assumption is re-decided cold."* **Status:** NOT trig
./DECISIONS.md:283:- Analyzer template "Praxis Backtest": already at Slippage 2 / Standard (REPORTED); no change.
echo ----- run3 record line 5 full
----- run3 record line 5 full
sed -n '5p' docs/reports/2026-10-30-run3-backtest-screenshot-record.md
**Window:** NinjaTrader 8 Strategy Analyzer, Display = `Summary ($)`, tab `Analyzer`, label `template` at the lower right of the Settings pane. Windows taskbar clock `6:12 PM 2026-10-30`, `13°C Partly sunny`. A small `Trend` slider box floats over the results pane (dropped per Amear's 2026-10-28 ruling; noted only).
echo ----- rescued install templates tree
----- rescued install templates tree
R="/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full"
ls -la "$R/"
total 374680
-rw-r--r--@  1 admin  staff  95900139 Jul 23 13:02 'NQ 12-25.txt'
drwxr-xr-x@ 20 admin  staff       640 Jul 24 07:56 .
drwxr-xr-x@ 16 admin  staff       512 Sep 29 11:28 ..
-rw-r--r--@  1 admin  staff     16879 Aug 29 12:00 Config.xml
drwxr-xr-x@ 25 admin  staff       800 Jul 14 11:15 EBWebView
-rw-r--r--@  1 admin  staff  95900139 Jul 23 13:02 NQ 12-25.txt
-rw-r--r--@  1 admin  staff      6842 Aug 29 12:52 UI.xml
drwxr-xr-x@  3 admin  staff        96 Jul  9 10:35 bin
drwxr-xr-x@ 30 admin  staff       960 Aug 29 12:00 cache
drwxr-xr-x@ 12 admin  staff       384 Jul 24 14:32 db
drwxr-xr-x@  2 admin  staff        64 Jul  9 10:35 export
drwxr-xr-x@  2 admin  staff        64 Jul  9 10:35 import
drwxr-xr-x@  2 admin  staff        64 Jul  9 10:35 incoming
drwxr-xr-x@ 19 admin  staff       608 Aug 29 11:02 log
drwxr-xr-x@  2 admin  staff        64 Jul  9 10:35 outgoing
drwxr-xr-x@ 23 admin  staff       736 Aug 29 12:01 strategyanalyzerlogs
drwxr-xr-x@ 24 admin  staff       768 Jul  9 10:37 templates
drwxr-xr-x@ 43 admin  staff      1376 Aug 29 12:00 tmp
drwxr-xr-x@ 11 admin  staff       352 Aug 29 11:02 trace
drwxr-xr-x@  3 admin  staff        96 Jul  9 10:38 workspaces
ls -laR "$R/templates/" 2>&1 | /usr/bin/grep -i -v -E '^total' | head -60
drwxr-xr-x@  24 admin  staff   768 Jul  9 10:37 .
drwxr-xr-x@  20 admin  staff   640 Jul 24 07:56 ..
drwxr-xr-x@   2 admin  staff    64 Jul  9 10:35 AlertAction
drwxr-xr-x@   2 admin  staff    64 Jul  9 10:35 AtmStrategy
drwxr-xr-x@   2 admin  staff    64 Jul  9 10:35 Chart
drwxr-xr-x@   2 admin  staff    64 Jul  9 10:35 ChartSeries
drwxr-xr-x@   2 admin  staff    64 Jul  9 10:35 ChartStyle
drwxr-xr-x@   5 admin  staff   160 Jul  9 10:37 Commission
drwxr-xr-x@   4 admin  staff   128 Aug 29 10:27 DrawingTool
drwxr-xr-x@   3 admin  staff    96 Jul  9 10:37 Fee
drwxr-xr-x@   2 admin  staff    64 Jul  9 10:35 GlobalDrawingObject
drwxr-xr-x@   2 admin  staff    64 Jul  9 10:35 HotListAnalyzer
drwxr-xr-x@   2 admin  staff    64 Jul  9 10:35 Indicator
drwxr-xr-x@   2 admin  staff    64 Jul  9 10:35 MarketAnalyzer
drwxr-xr-x@  15 admin  staff   480 Jul  9 10:37 MarketDataEntitlement
drwxr-xr-x@   3 admin  staff    96 Aug 29 09:28 Risk
drwxr-xr-x@   9 admin  staff   288 Jul  9 10:35 Skins
drwxr-xr-x@   2 admin  staff    64 Jul  9 10:35 StopStrategy
drwxr-xr-x@   2 admin  staff    64 Jul  9 10:35 Strategy
drwxr-xr-x@   2 admin  staff    64 Jul  9 10:37 StrategyAnalyzer
drwxr-xr-x@   2 admin  staff    64 Jul  9 10:35 StrategyWizardAction
drwxr-xr-x@   2 admin  staff    64 Jul  9 10:35 StrategyWizardCondition
drwxr-xr-x@   2 admin  staff    64 Jul  9 10:35 SuperDom
drwxr-xr-x@ 119 admin  staff  3808 Aug 29 11:52 TradingHours

/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/templates//AlertAction:
drwxr-xr-x@  2 admin  staff   64 Jul  9 10:35 .
drwxr-xr-x@ 24 admin  staff  768 Jul  9 10:37 ..

/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/templates//AtmStrategy:
drwxr-xr-x@  2 admin  staff   64 Jul  9 10:35 .
drwxr-xr-x@ 24 admin  staff  768 Jul  9 10:37 ..

/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/templates//Chart:
drwxr-xr-x@  2 admin  staff   64 Jul  9 10:35 .
drwxr-xr-x@ 24 admin  staff  768 Jul  9 10:37 ..

/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/templates//ChartSeries:
drwxr-xr-x@  2 admin  staff   64 Jul  9 10:35 .
drwxr-xr-x@ 24 admin  staff  768 Jul  9 10:37 ..

/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/templates//ChartStyle:
drwxr-xr-x@  2 admin  staff   64 Jul  9 10:35 .
drwxr-xr-x@ 24 admin  staff  768 Jul  9 10:37 ..

/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/templates//Commission:
drwxr-xr-x@  5 admin  staff   160 Jul  9 10:37 .
drwxr-xr-x@ 24 admin  staff   768 Jul  9 10:37 ..
-rw-r--r--@  1 admin  staff  4949 Jul  9 10:37 NinjaTrader Brokerage Free.xml
-rw-r--r--@  1 admin  staff  4961 Jul  9 10:37 NinjaTrader Brokerage Lifetime.xml
-rw-r--r--@  1 admin  staff  4958 Jul  9 10:37 NinjaTrader Brokerage Monthly.xml

/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/templates//DrawingTool:
drwxr-xr-x@  4 admin  staff  128 Aug 29 10:27 .
drwxr-xr-x@ 24 admin  staff  768 Jul  9 10:37 ..
drwxr-xr-x@  2 admin  staff   64 Aug 29 10:22 Line
drwxr-xr-x@  2 admin  staff   64 Aug 29 10:27 RiskReward

/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/templates//DrawingTool/Line:
drwxr-xr-x@ 2 admin  staff   64 Aug 29 10:22 .
````

---

## Q6. Disk footprint of `db/minute/NQCONT/` in the rescued install

**Answer.**
1. **OBSERVED:** 1,710 files, `du -sh` = 19M, 16,608,933 bytes in total, a mean of 9,713 bytes per file. The first file is `20210307.Last.ncd` and the last is `20260720.Last.ncd`.
2. **OBSERVED:** the import file has 1,857,362 lines and **1,712** distinct `yyyyMMdd` dates, from `20210307` to `20260720`.
3. **OBSERVED:** `comm -3` shows exactly two import dates with no `.ncd` file, `20221112` and `20260612`, and no `.ncd` file without an import date. Why those two dates are missing was not examined.
4. **This is one file per bar-date, Sundays included, not one per trading day.** 1,710 of 1,712 dates are present, which fits NT8 writing one `.ncd` per local calendar date of the bars (INFERRED).
5. **REPORTED / record:** the rescued import is of the same file. The 2026-10-31 DECISION_LOG row `15:01:22Z` records `NQCONT.Last.txt` as byte-identical to `NQ-continuous-1min.nt8import.txt`.
6. **Expectation for the Fusion readback (INFERRED):**
   - `Documents\NinjaTrader 8\db\minute\NQCONT\` holds about 1,710 `*.Last.ncd` files from `20210307` to `20260720`, about 16-19 MB.
   - `db\minute\NQCONT 09-25\` is empty or absent.
   - After a correct re-import as `NQCONT 09-25.Last.txt`, `db\minute\NQCONT 09-25\` should hold about the same count, if storage does not filter by expiry (Q3, UNVERIFIED).
   - A different Time Zone setting at import could shift dates and change the count.

**Evidence: dates in the import file against the `.ncd` files; size; Config/UI merge and NQCONT lines.** Command as run: `bash -v q6.sh 2>&1 | tee q6.out`
````text
R="/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full"
F="$HOME/praxis-signals/b2-data/NQCONT.Last.txt"
wc -l "$F"
 1857362 /Users/admin/praxis-signals/b2-data/NQCONT.Last.txt
head -1 "$F" | od -c | head -3
0000000    2   0   2   1   0   3   0   7       1   8   0   1   0   0   ;
0000020    1   6   1   2   0   .   5   ;   1   6   1   6   7   ;   1   6
0000040    1   2   0   .   5   ;   1   6   1   5   4   .   7   5   ;   1
cut -c1-8 "$F" | uniq | wc -l
    1712
cut -c1-8 "$F" | uniq | head -2
20210307
20210308
cut -c1-8 "$F" | uniq | tail -2
20260719
20260720
echo ----- dates in import file but no .ncd file, and .ncd files with no import date
----- dates in import file but no .ncd file, and .ncd files with no import date
comm -3 <(cut -c1-8 "$F" | uniq | sort -u) <(ls -1 "$R/db/minute/NQCONT/" | cut -c1-8 | sort -u) | head -20
20221112
20260612
comm -3 <(cut -c1-8 "$F" | uniq | sort -u) <(ls -1 "$R/db/minute/NQCONT/" | cut -c1-8 | sort -u) | wc -l
       2
echo ----- size distribution of .ncd files, bytes
----- size distribution of .ncd files, bytes
ls -l "$R/db/minute/NQCONT/" | awk 'NR>1 {s+=$5; n++} END {print "files", n, "bytes", s, "mean", s/n}'
files 1710 bytes 16608933 mean 9712.83
echo ----- Config.xml and UI.xml mentions of merge, rollover, NQCONT, analyzer
----- Config.xml and UI.xml mentions of merge, rollover, NQCONT, analyzer
/usr/bin/grep -n -a -i -E 'merge|rollover|NQCONT|StrategyAnalyzer' "$R/Config.xml" "$R/UI.xml" | tr -d '\r' | cut -c1-200
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/Config.xml:103:      <GlobalMergePolicy>MergeBackAdjusted</GlobalMergePolicy>
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/UI.xml:28:    <RecentInstrument>NQCONT SEP25</RecentInstrument>
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/UI.xml:32:    <PinnedInstrument>NQCONT</PinnedInstrument>
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/UI.xml:84:    <NinjaTrader.Gui.NinjaScript.StrategyAnalyzer.StrategyAnalyzer>
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/UI.xml:87:    </NinjaTrader.Gui.NinjaScript.StrategyAnalyzer.StrategyAnalyzer>
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/UI.xml:153:      <Contract_x0020_months_x0020__x0028_expirations_x0020_and_x0020_rollover_x0020_dates_x0029_>true</Contract_x0020_months_x002
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/UI.xml:160:  <IgnoredRollovers />
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/UI.xml:161:  <AutoRolloverRetry>20260830</AutoRolloverRetry>
````

---

## Open / UNVERIFIED

1. **Fusion is unread.** Every OBSERVED NT8 fact is from the rescued Parallels install. On Fusion, these need a readback:
   - a `db\minute\` listing, including the `NQCONT` count and first/last file, and whether `NQCONT 09-25` exists;
   - `Loaded` names;
   - the Future row's rollover table and Merge Policy;
   - `Tools > Options > Market Data > Merge policy`.
2. **Whether NT8 stores or serves bars outside a contract's life (Q3).** SPEC-SILENT. Decided by the two-step test in Q3.
3. **Whether `NQCONT SEP25.Last.txt` (display form) imports.** UNVERIFIED. Use the `MM-YY` form.
4. **What MergeBackAdjusted does with a one-row rollover table.** It might apply no offset, or it might apply one. SPEC-SILENT. DoNotMerge avoids the question, but it is an instrument edit that needs Amear.
5. **Whether the March-2021 refusal on `##-##` comes from having no contract before the 2025-12-01 rollover.** Plausible, UNVERIFIED. The exact error text on Fusion was not captured.
6. **Whether `##-##` can use imported data at all.** UNVERIFIED. Reference §6 says it requires provider support.
7. **What deleting or renaming the Stock `NQCONT` row does** to name resolution and to the `db\minute\NQCONT\` files. SPEC-SILENT. Not required to reach the Future row.
8. **The integer meanings of `MergePolicy 3` and `InstrumentType 0/1`.** INFERRED from co-occurrence (type 0 has PV 20 and an expiry; type 1 has PV 1 and expiry 2099). No source maps them.
9. **The decode of the Future master's `UserData` blob** (contract 2025-09-01, rollover 2025-12-01, NaN after them). INFERRED. The format is undocumented.
10. **The exact save-as-default control label in the Analyzer.** UNVERIFIED (Q5).
11. **The 2 import dates with no `.ncd` file** (`20221112`, `20260612`). Not examined.
12. **Merge Policy on the rescued install at its last save.** REPORTED as `Use Global Setting` (19:00) and as `Do not merge` (19:30, coworker, open dialog). The sqlite holds 3 for both NQCONT rows. Which REPORTED state, if either, matches 3 is INFERRED only.
13. **Possible record defect for the manager to route:** session 52's "Stock duplicate confirmed empty against Historical Data" conflicts with the on-disk layout, where the data sits under the Stock row's name. Not fixed here; I changed no other file.
14. **ADDED (a9d worker 4, finding 1): whether a data connection on Fusion writes provider bars into `db\minute\NQCONT 09-25\`.** UNVERIFIED. On the connected old install (`Provider` = Simulator), a `(to Provider)` request for `NQ SEP26` at 2026-08-29 10:30 was followed by provider-written files `20260823`..`20260828` in `db/minute/NQ 09-26/` (OBSERVED, `docs/reports/2026-10-31-a9d-adversarial.md` finding 1; walkthrough Evidence). `SaveDataAsHistorical` and `RecordForPlayback` read `false` on the old install only. Neither the setting nor any provider symbol mapping for the Future `NQCONT` has been read on Fusion. The walkthrough guards this with read-only step 0.8 and re-lists of the folder after 1.5 and after the Phase 3 run.
15. **ADDED (a9d worker 4, finding 3): `NQCONT SEP25` = `NQCONT 09-25`.** INFERRED (strong) from co-timed log/trace lines, not OBSERVED (Q2 item 1). Tested on Fusion by walkthrough 1.5.
