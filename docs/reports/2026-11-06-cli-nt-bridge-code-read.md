# cli-nt-bridge: read-only code read (2026-11-06)

- Unit: `2026-11-06-cli-nt-bridge-code-read` (praxis-manager, three capture workers, one adversarial worker).
- Status: NOT audited at the time of writing. Nothing is staged or committed by this unit.
- What was read: `https://github.com/eman007/cli-nt-bridge`, cloned anonymously over HTTPS into an empty scratchpad directory, at commit **`9664d9b255bfa34b120d88a481afe7741a4115e6`** (`release: 1.7.5`, 2026-10-18T22:22:18-07:00) [M01]. Citations below read `path:line@9664d9b`. The README and `addon/NT8BridgeServer.cs` are byte-identical to the copies catalogued on 2026-11-04: same sha256 prefixes `948cb9d5bef0` / `8fb9566d11f8`, same line counts [M02][P13].
- Nothing in the clone was run: no Python, no PowerShell, no C# compiler, no scripts. Nothing went toward the VM, the SMB share or NT8. Nothing was copied into the repo except quotes of three lines or fewer.

## Authorisation

- DECISIONS.md `## 2026-11-06 — D-2026-11-06-A` (in `e31b9a4`), Amear's item 2 [P02][P03]: "Order: read the bridge's code read-only; write an install walkthrough; VMware snapshot first; then install. Direction: the walk-forward runs in NT8 through the bridge, not in a Mac-side Python copy." This unit is the first step only. The install walkthrough is the next unit.
- DECISION_LOG.md row `[2026-11-06T18:33:03Z] WHO: praxis-master` (working tree; line 464 when read) [P04] is the dispatch. Its limits include "Limits: clone anonymously into its own empty scratchpad directory (no `gh`, no login".

## Grades

- **OBSERVED**: read in the clone or the repo; a command pasted in the appendix prints it.
- **INFERRED**: reasoned from observed facts; the basis is given.
- **REPORTED BY**: someone else's statement. The bridge's README and comments are REPORTED BY eman007; repo notes are REPORTED BY Amear.
- **UNVERIFIED**: cannot be settled from code alone.
- Nothing about the bridge is "working" or "tested" in this report. Code that exists is "implemented". A README claim with no code found is "specified".

How to re-run the appendix: each `[Axx] [Bxx] [Cxx] [Mxx]` command runs from the clone root, and each `[Pxx]` command from the repo root `/Volumes/Sensidine/Praxis.build`. The harness passes each command line as one argument to `zsh -f -c` under `LC_ALL=C`: `( cd "$B" && LC_ALL=C zsh -f -c "$cmd" )`, with `B=/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/bridge-src/cli-nt-bridge` (or the repo root for P). Workers W1/W2/W3 wrote the A/B/C lines. The manager re-ran every line, and the manager's output is pasted. Blocks not cited in the text are left out.

Standing limitation for the baseline figures below (1190 trades, $197327.60): Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## Summary

1. **What it is.** A C# AddOn runs inside NT8 (`NT8BridgeServer`, split over two files). A **Python** command-line tool runs outside it (`nt8bridge`, Python 3.10+). The two talk only through JSON files in `Documents\NinjaTrader 8\NT8Bridge\trigger` and `\result`. There is no network port and no authentication. A separate optional product, "NT8 Guard" (PowerShell), adds scheduled tasks and password-filling. (OBSERVED; Q1, Q4.)
2. **Backtests.** `backtest` does not configure a run. It presses Run on a Strategy Analyzer tab **already open and set up by hand**, can inject strategy parameters, and returns summary metrics plus a trade list. (OBSERVED; Q2.)
3. **Reproducing the baseline.** 15 of the baseline's settings (the 12 BLOCKER rows of the Q3 table) have **no explicit field** in the bridge, among them slippage, the commission template, fill resolution, Break at EOD and Exit on session close. They reach the run only by one of four routes: already set on the hand-set tab; carried in an NT8-saved template; set through the generic by-name setter `configure`; or set by name through `backtest`'s own `params`. The bridge lists no NT8 property names for the last two. An exact 1190 / $197327.60 reproduction is **UNVERIFIED**. From the code it is plausible only if the tab is first set by hand exactly as in the committed run. (INFERRED; Q3.)
4. **Walk-forward.** The AddOn's only check for an empty `opt` is a blank-text test [B02][M41]. It splits `opt` on commas and drops empty parts [M49], and it has no min < max check [M42]. The Python CLI also refuses a list with no ranges [M50]. Whether NT8 runs a walk-forward with no range, or with a one-value range, and whether either would count as arm (a)'s "nothing optimised", is UNVERIFIED. The committed strategy declares only two inputs (`[NinjaScriptProperty]`): `ExitMode` (an enum) and `Contracts`. Its lookback is a private constant [P16], so arm (b)'s lookback, noise multiplier and stop-ATR multiplier are not inputs today. (OBSERVED code; consequences INFERRED; Q3.)
5. **Install.** Installing means copying C# into `bin\Custom\AddOns` and compiling it in NT8. The master's dispatch row reads that as an **import on the VM** [P18], which the 2026-11-05T23:50:09Z ruling bars until Amear lifts it [P05]. The README's install step names only one of the two files the AddOn needs, so a compile failure is likely (INFERRED; Q4).
6. **Safety.** Any process running as the VM user can drop a request. That includes `flatten` (**no Sim-only check**), `reconnect`, `strategies` enable, and `playbackrun`, whose Playback stages **disconnect every non-Playback connection**. An optional companion AddOn (`AutoReconnect`) reconnects on its own. No order-submission code was found. (OBSERVED; Q5.)
7. **Licence.** MIT, with **two copyright holders**: eman007, and Quantrosoft Pty. Ltd. for the Playback file and Python modules. (OBSERVED; Q6.)
8. **Maturity.** 55 commits, 2026-06-09 to 2026-10-18; 17 version headings in the CHANGELOG. 96 test files, none run, and no CI config. 8.1.8.4 is named nowhere in the clone. (OBSERVED; Q4, Q7.)

## Q1. Components, transport, what runs where

| Component | Where it runs | What it is | Evidence |
|---|---|---|---|
| `addon/NT8BridgeServer.cs` + `addon/NT8BridgeServerPlayback.cs` | inside NT8 | one AddOn, `public partial class NT8BridgeServer : AddOnBase`, split across two files | [A02] `addon/NT8BridgeServer.cs:36@9664d9b`, `addon/NT8BridgeServerPlayback.cs:61@9664d9b` (OBSERVED) |
| `addon/AutoReconnect.cs` | inside NT8 | a **separate** AddOn: "auto-reconnect dropped connections + ALERT on dead feeds" | [A02] `:123`; [M08] header `:1-12` (OBSERVED) |
| `addon/ChartDataSeriesSwitcher.cs` | inside NT8 | a static helper class found by reflection; only the `chartseries` command needs it | [A02] `:31`; [M34] `NT8BridgeServer.cs:2252,2277` (OBSERVED) |
| `nt8bridge/*.py` | outside NT8 (Windows Python) | the CLI: 38 `add_parser(` call sites, one of them a loop over the three analyzer modes (`cli.py:1261`) | [A32][A33][M28][M44] (OBSERVED); 40 subcommand names in all is arithmetic, 37 + 3 (INFERRED) |
| `guard/` | outside NT8 (Windows PowerShell 5.1; bundled Python in releases) | "NT8 Guard", an optional separate product | Q4 (OBSERVED) |

- **Transport: JSON files polled once a second.** There is no socket, no pipe and no file watcher. (OBSERVED.)
  - Requests go to `<UserDataDir>\NT8Bridge\trigger\*.json`; answers go to `\result\` [A04][A05][M13][M29]. `NT8BridgeServer.cs:122@9664d9b`: `_poller = new Timer(delegate { Poll(); }, null, 1000, 1000);` [A04].
  - No `HttpListener / TcpListener / UdpClient / IPAddress. / NamedPipe / FileSystemWatcher / socket / http.server` appears in `addon/*.cs` or `nt8bridge/*.py`: grep exit 1 [A03]. Positive control on the same files: `Timer` 4 hits, `Path` 10 hits [M03].
  - A wider scan that adds HTTP-client names, over `addon nt8bridge guard tools`, lists only guard files and the vendored QR library [M04]. A third scan over the bridge AddOn files adds `TcpClient / HttpWebRequest / WebRequest / Socket / Dns.` and exits 1; its positive control finds `HttpWebRequest` in `AutoReconnect.cs` [M45]. The CLI imports no `socket / http / urllib / requests / ssl / asyncio` module (grep exit 1, control: `json` and `pathlib` imports found) [M46]. The bridge AddOn and CLI make no network calls (OBSERVED for these patterns).
  - Two optional parts make **outbound** HTTP calls, for alerts only. `AutoReconnect.cs` uses `HttpWebRequest` (`AutoReconnect.cs:2000@9664d9b`; "https webhooks" at `:329`) [M32][M05]. Guard uses `Invoke-RestMethod ... -Method Post` (`guard/app/lib/Guard.Alerts.psm1:12@9664d9b`) [M33]. Neither listens.
  - README:5 says "No UI automation, no network." [M19]. That holds for the bridge's own transport, not for AutoReconnect or guard. The bridge's `strategies` command also clicks a GUI checkbox by reflection (Q5), which sits poorly with "No UI automation". (INFERRED from the cited code.)
- **Request shape.** A request is flat JSON: `id`, `kind`, per-kind fields, and an optional `ttlSec`. The AddOn dispatches on `kind` through an if/else chain [A09][M35]. Kinds include `compile, reload, backtest, flatten, reconnect, playbackrun, strategies, ghostorders, screenshot, configure, satemplate, analyzerrun` (`NT8BridgeServer.cs:214-252@9664d9b`) [M35]. The Python side writes `trigger/<kind>_<id>.json` atomically (`.tmp`, then `os.replace`) and polls `result/<prefix><id>.json` [A01][B17]. (OBSERVED.)
- **Config.** `config/config.json` is a per-backtest file (strategy, instrument, barType, dates, commission, slippageTicks, params), not a bridge setting. It has no port, folder or auth key [M10]. (OBSERVED.)
- **Correction to the 2026-11-04 catalogue.** It listed the repo language as "PowerShell" [P13], which is GitHub's metadata. The bridge CLI is Python: `pyproject.toml`, package `nt8bridge` 1.7.5 [C02]. PowerShell is guard's language. (OBSERVED.)

## Q2. How it drives a Strategy Analyzer backtest and a walk-forward

**Backtest (`backtest` kind).**
- It needs an **open** Strategy Analyzer window. It takes the selected tab and injects `params` onto the tab's strategy template by property name. Then it fires the same `RunCommand` the Run button fires (`NT8BridgeServer.cs:2632-2665@9664d9b`) [B12]. (OBSERVED.)
  > `2637: WriteResult("backtest_" + id + ".json", BtErr(id, "no Strategy Analyzer window open"));`
  > `2651: InjectParams(tab.TabStrategyProperties.StrategyTemplate, prms);`
  > `2664: rc.Execute(null, saWin);`
- The only thing it reads from the request is the `params` object (`ParseParams`, `:2713-2718`) [B13]. README:165 says it "Drives an **open, configured** Strategy Analyzer. Set the SA tab up once (strategy, instrument, dates, commission)", and README:182 calls `instrument, barType, from, to, capital, commission, slippageTicks` "reference fields" [B28]. The AddOn never reads `slippageTicks` or `commission` [B26][M37]. (OBSERVED.)
- It never sets the backtest type. The only `BacktestType =` in `addon/` is on the walk-forward/optimise path (`NT8BridgeServerPlayback.cs:1833`) [B25]. So a `backtest` run after a walk-forward on the same tab uses whatever type the tab still holds. (Code OBSERVED; consequence INFERRED; whether NT8 resets it is UNVERIFIED.)
- **Response.** `{id, status, strategy, metrics:{totalTrades, profitFactor, netProfit, maxDrawdown}, trades:[...]}`, with `netProfit` = `tp.Currency.CumProfit` and `maxDrawdown` = `tp.Currency.Drawdown` (`NT8BridgeServer.cs:2812-2832`) [B14].
  - Each trade carries pnl, side, entry and exit time and price, and exit name. There is no per-trade commission or quantity. The list is **capped at 5000** (`:2844`) [B15].
  - The file is written to `<UserDataDir>\NT8Bridge\result\backtest_<id>.json` [M13][B16]. (OBSERVED.)
  - Whether `CumProfit` is net of the template commission is NT8 behaviour: UNVERIFIED.

**Other ways to set the tab.**
- **`configure`** sets any public writable property **by name**. It tries three targets in order: the tab, the tab's strategy properties, then the strategy template (`NT8BridgeServer.cs:2491`) [B18][B19].
  - Value converters exist only for `Instrument`, `DateTime` and `BarsPeriod` (`"Minute:1"`), plus generic enum/bool/number conversion [B20].
  - The bridge's own comment says "From / To / BarsPeriod / IsTickReplay are writable ONLY on the template" (`:2528`) [M11]. (OBSERVED.)
  - The bridge does not list NT8's property names for slippage, fill resolution and the rest, so whether `configure` can set them is UNVERIFIED.
- **`satemplate`** loads a strategy template XML that NT8 saved, by full path or by name (`NT8BridgeServerPlayback.cs:1425-1541, 2404-2417`) [B09][B10][B11]. NT8, not the bridge, decides which Strategy Analyzer settings go into that template: UNVERIFIED. README:337-343 claims the template carries "exactly what the GUI would run" [B29] (REPORTED BY eman007).

**Optimise / walk-forward (`analyzerrun` kind; CLI `optimize`, `walkforward [--anchored]`, `multiobjective`).**
- The AddOn reads `mode, template, opt, optimizer, fitness, timeoutSec, params` (`NT8BridgeServerPlayback.cs:1679-1685`) [B02]. The Python side adds `ttlSec` [B34]. (OBSERVED.)
- `template` is required. The AddOn's only check for an empty `opt` is a blank-text test (`addon/NT8BridgeServerPlayback.cs:1691-1692@9664d9b`) [B02][M41]:
  > `1692: { WriteResult(resultFile, BtErr(id, "analyzerrun: " + mode + " needs opt=Name:min:max:step[,...]")); return; }`
- The AddOn then splits `opt` on commas and drops empty parts (`:1730`) [M49]. It also refuses a malformed entry, a name that is not a property, a type mismatch, and step ≤ 0 (`:1733-1750`) [M41][M42]. The Python CLI separately refuses a list with no ranges, with its own message (`nt8bridge/analyzerrun.py:117-118@9664d9b`, called at `cli.py:597`) [M50].
- Window lengths are not their own fields. They are strategy properties, passed as `--OptimizationPeriod=<days> --TestPeriod=<days>` [B01][B27][B30]. The mode sets `tsp.BacktestType` [B05]. The optimizer is `default` or `genetic` [B04]. (OBSERVED.)
- **Response.** One row per new Strategy Analyzer grid entry (in-sample combinations and out-of-sample windows), with guid/parent, from/to and parameters [B07]. Each row's `results` holds only `totalTrades, profitFactor, netProfit, maxDrawdown, performanceValue` (`:2156-2173`) [B08]. **Walk-forward output has no per-trade list.** `csvFiles` are CSVs the strategy itself writes, not a grid export (README:378-385) [B06][B30]. (OBSERVED.)

**Fill resolution, slippage, commission.** Nothing on the analyzer path mentions them: no field, no converter, no code.
- A case-insensitive search for `slippage|fillresolution|fill resolution` over `addon/` exits 1 [M37].
- `NT8BridgeServer.cs:2632-2870` and `NT8BridgeServerPlayback.cs:1677-2352` hold 0 commission lines; the positive controls find 4 and 5 `RunCommand` lines [M38].
- The commission code that does exist reads an **account's** template for the live performance report (`NT8BridgeServer.cs:3436-3447`). It does not set the Analyzer's [M37][B26].
- **No explicit bridge field sets 1-minute Standard fill resolution, 2 ticks/side slippage or the PRAXIS commission template.** They must already be on the tab, or in an NT8 template, or be set by NT8's own property names through `configure` or `backtest`'s `params` (UNVERIFIED; Q3 routes a-d). (Absence OBSERVED; routes INFERRED.)

## Q3. What reproducing the committed baseline would need

The committed baseline: `docs/reports/2026-11-01-three-strategy-results.md:73`, `| All | 1190 | $197327.60 |`, on instrument `NQCONTROW SEP25` (`:86`), strategy `PraxisNoiseAreaBreakout` (1190 rows) [P07][P09]. Its settings are Amear's C4 notes, `docs/reports/2026-10-31-voice-session-notes-2.md:111` [P10] (REPORTED BY Amear). The results report names no NT8 build: 0 lines match `8.1.` [P08]. The notes say "C4 ran on 8.1.8.4." (`notes-2:161`) [P11] (REPORTED BY Amear).

| Baseline setting (notes-2:111) | Bridge route | Grade |
|---|---|---|
| Strategy `PraxisNoiseAreaBreakout` | template / `configure Strategy` [B03][B18] | OBSERVED (mechanism) |
| Instrument NQCONTROW SEP25 | template instrument copied to tab; `configure Instrument` → `Instrument.GetInstrument(name)` [B11][B20] | mechanism OBSERVED; whether a custom continuous name resolves: UNVERIFIED |
| Price based on Last | **no field**: `PriceBasedOn` / `MarketDataType` are absent from `addon/` [B21][B23] | BLOCKER |
| Minute, 1 | `configure BarsPeriod=Minute:1` [B20][M11] | OBSERVED (mechanism) |
| 2021-03-08 → 2026-07-17 | `configure From/To` [B20][M11] | OBSERVED (mechanism) |
| Trading hours "CME US Index Futures RTH" | no Analyzer path; only `playbackrun` takes `tradingHours` [B24][M39] | BLOCKER |
| Break at EOD ✓ | no field [B21][B22] | BLOCKER |
| Include commission ✓ / template PRAXIS | no field; `commission` is a "reference field" [B21][B26][B28][M38] | BLOCKER |
| Max bars look back 256 | no field [B21] | BLOCKER |
| Bars required 20 | no field [B21] | BLOCKER |
| Order fill resolution Standard (Fastest) | no field [B21][M37] | BLOCKER |
| Fill limit orders on touch ☐ | no field [B21] | BLOCKER |
| Slippage 2 | no field; the AddOn never reads `slippageTicks` [B21][B26][M37] | BLOCKER |
| Entries per direction 1 / Entry handling All entries | no field [B21] | BLOCKER |
| Exit on session close ✓ | no field [B21] | BLOCKER |
| Set order quantity Strategy / Time in force DAY | no field [B21] | BLOCKER |
| ExitMode BandOrVWAP / Contracts 1 | `params` → `InjectParams` by property name, with enum and int conversion [B13][B20] | mechanism OBSERVED. Both are public properties of the repo strategy (`ninjascript/PraxisNoiseAreaBreakout.cs:300,305`) [P16]; defaults `:118-119` [P12] |
| Backtest type: Backtest | `backtest` never sets it and runs whatever the tab holds [B25] | OBSERVED; see Q2 |

"BLOCKER" means only "no explicit bridge field". B21 searches `addon nt8bridge config README.md` for 14 NT8 setting names and prints only `grep-exit=1`; its positive control on the same trees is [B22]. Each BLOCKER row has four possible routes:
- (a) set it by hand on the open tab before `backtest`. This is OBSERVED as the README's intended use [B28].
- (b) carry it in an NT8-saved template. UNVERIFIED.
- (c) send `configure <NT8PropertyName>=<value>`. UNVERIFIED.
- (d) put `<NT8PropertyName>` into `backtest`'s own `params`. `InjectParams` sets any public writable property of the strategy template by name (`NT8BridgeServer.cs:2678-2686`) [B13]. Whether these settings are such properties under those names is NT8 behaviour: UNVERIFIED.

The repo strategy's own `SetDefaults` assigns five of the BLOCKER settings to the baseline's values: `EntriesPerDirection = 1`, `EntryHandling.AllEntries`, `IsExitOnSessionCloseStrategy = true`, `TimeInForce.Day`, `BarsRequiredToTrade = 20` (`ninjascript/PraxisNoiseAreaBreakout.cs:106-112`) [P17]. These are inherited NT8 members. The bridge looks properties up with `GetProperty(name, BindingFlags.Public | BindingFlags.Instance)` (`NT8BridgeServer.cs:2684`, `NT8BridgeServerPlayback.cs:1736`) [M54], which can find public inherited members (INFERRED, .NET reflection). Whether these five are public writable properties under these names, and whether a Strategy Analyzer run uses the strategy's defaults or the tab's values, is NT8 behaviour: UNVERIFIED. The rows stay BLOCKER, because the bridge has no explicit field for them.

**Plausibility of an exact 1190 / $197327.60 reproduction: UNVERIFIED.**
- What the code allows. `backtest` presses NT8's own Run on the tab and reads NT8's own `SystemPerformance` [B12][B14]. With the tab set exactly as in the committed run, the bridge adds no logic of its own between Run and the result (INFERRED from [B12][B13][B14]). Agreement then depends on NT8, the VM's strategy copy and the VM's data, not on the bridge.
- What the code does not show. That the bridge "drives the baseline from the terminal" with no hand setup: 15 settings have no explicit field (INFERRED).
- The 5000-trade cap is above 1190 [B15].
- Whether the VM's strategy is the repo's `ninjascript/PraxisNoiseAreaBreakout.cs` (last changed in `719ab11`) [P12] is not known. The 2026-11-01 report records that the VM copies were not hash-checked.

**Walk-forward vs the committed walk-forward spec (INFERRED).**
- `docs/specs/2026-11-05-walk-forward-spec.md` (`221ef59`) [P15] defines two arms:
  - arm (a): "the paper's fixed rules, nothing optimised" (`:65`);
  - arm (b): "four parameters tuned per window — lookback, noise multiplier, stop-ATR multiplier, exit policy" (`:29`).
- The AddOn's only check for an empty `opt` is a blank-text test (`NT8BridgeServerPlayback.cs:1691-1692`) [M41]. It then splits `opt` on commas, dropping empty parts (`:1730`) [M49]. Its only range check is `step > 0`: lines 1726-1770 hold no min/max comparison (0 lines; control: 7 lines with `step`) [M42]. The Python CLI refuses a list with no ranges [M50]; a trigger file written directly does not pass through that check (INFERRED from [M49][M50]). A one-value range, for example `Contracts:1:1:1`, therefore passes the bridge's checks, and so may an `opt` of only commas (INFERRED). Whether NT8 runs either, and whether that, a series of plain `backtest` runs or something else counts as arm (a), is UNVERIFIED and not decided here (NEEDS AMEAR 12).
- The committed strategy declares two inputs (`[NinjaScriptProperty]`), `ExitMode` and `Contracts`. `Lookback` and `BandSigmaMult` are private constants (`:74`, `:76`) [P16]. Arm (b)'s lookback, noise multiplier and stop-ATR multiplier are not declared inputs today. (The strategy also inherits NT8 members, below; none of them is one of those three.)
- The bridge builds each `opt` bound with `Convert.ChangeType(<text>, prop.PropertyType)` (`NT8BridgeServerPlayback.cs:1743-1744`) [M41]. Whether that accepts an enum such as `ExitMode` is .NET behaviour that nobody ran here: UNVERIFIED.

## Q4. What an install touches on the VM

- **The AddOn install, read by the master's dispatch row as an import on the VM** ("AddOn import = an \"import on the VM\", barred until Amear lifts it", DECISION_LOG `2026-11-06T18:33:03Z`) [P18]. README:50-54 [M29]: "`python -m nt8bridge deploy --strategy addon/NT8BridgeServer.cs --kind addon` (copies it to `…\NinjaTrader 8\bin\Custom\AddOns\`)", then "compile (F5)". Guard's alternative is an `NT8Guard-AddOns.zip` for "Tools > Import > NinjaScript Add-On" (`guard/README.md:27`) [M30]. Either way, C# is brought into NT8 and compiled. "no NT8 runs or imports on the VM" (DECISION_LOG `2026-11-05T23:50:09Z`, WHO: amear, line 519) [P05] bars that until Amear lifts it. (Text OBSERVED. Calling the install an "import" is the master's reading [P18], not Amear's words.)
- **README install gap.** The README deploys only `NT8BridgeServer.cs`. That file calls `RunPlaybackRun`, which is defined only in `NT8BridgeServerPlayback.cs` [C08]. NT8 compiles the "whole tree" (README:148) [M21], and CHANGELOG:491 says "Adds a second AddOn file (`NT8BridgeServerPlayback.cs`)" [M21]. A one-file deploy should therefore fail to compile (INFERRED from the C# partial-class rule; not tried).
- **Getting the source.** README:41 clones with `git clone git@github.com:...` [M29]. That SSH form needs a GitHub key. This unit cloned anonymously over HTTPS instead; [M01] runs inside that clone.
- **Python side.** "Python 3.10+" (README:35), a venv, and `pip install -e ".[dev,report]"` [M29]. The pyproject base deps are `jsonschema>=4, numpy>=1.24, pyarrow>=14, tzdata`: floors only, no lock file [C02]. pip would download them on the VM (INFERRED).
- **Files the bridge writes** (OBSERVED):
  - `Documents\NinjaTrader 8\NT8Bridge\{trigger,result}` [A01][C04].
  - `bin\Custom\<Strategies|Indicators|AddOns>\<file>` via `deploy`, replacing a same-named file without asking [C03][A28].
  - `screenshot` writes wherever the request's `out` path points [A25].
  - `regions` rewrites `.cs` files in place and keeps a `.bak` (`nt8bridge/regions.py:96-97`) [M27].
  - A `satemplate` save writes a template XML (`NT8BridgeServerPlayback.cs:4442-4453`) [M26].
  - AutoReconnect, if installed, writes its log, heartbeat and marker files in the NT8 user root [A31].
- **Process control** (OBSERVED). `restart` runs `taskkill`, then `taskkill /F` [A30][C07]. It then relaunches NT8, either by running the scheduled task named in `--task` (`schtasks /run /tn <task>`, `nt8bridge/restart.py:99`) or with `Popen` on a given exe (`:158`) [M47][C07]. `watchdog` force-kills NT8 and relaunches it from a default exe path that `--exe` overrides (`nt8bridge/watchdog.py:26, 68-71`; `cli.py:1391` `p_wd.add_argument("--exe", default=ntwatchdog.NT8_EXE_DEFAULT)`) [C07][M52][M55]. The bridge's own comment says that "on a box where NT is started through a wrapper that supplies credentials, the bare exe stops at the Welcome screen" (`nt8bridge/restart.py:39-40`) [M17].
- **Guard** is optional and not needed by the bridge: the CLI has no guard import (grep exit 1) [M24]. If installed, guard does the following (OBSERVED):
  - adds three per-user scheduled tasks at "the normal (Limited) run level": `NT8Guard-Relaunch` (every 1 min), `-Overwatch` (1 min) and `-LogArchive` (10 min) [C13];
  - saves the NT8 password with `Export-Clixml` (Windows DPAPI) [C14];
  - fills the login window by UI Automation, falling back to SendKeys [C15];
  - kills and relaunches NT8 on its own [C16][C17];
  - can rewrite `NinjaTrader.sqlite` with `--apply` while NT8 is closed [C19];
  - writes AutoReconnect's config into the NT8 data dir (`Register-GuardTasks.ps1:87`) [M20];
  - needs "Windows PowerShell 5.1" [C21].
  The patterns searched found no registry writes, firewall rules, services or startup entries [C18].
- **Firewall / port.** None: there is no listener [A03][M03][M04]. (Absence OBSERVED, with positive control.)
- **NT8 version.**
  - The README says "developed/verified against 8.1.6.x" (`:34`, `:629`) [M29][B32] (REPORTED BY eman007).
  - Build strings across the whole clone: 8.1.5.2 ×2, 8.1.6.0 ×1, 8.1.6.3 ×9, 8.1.6.x ×5, 8.1.7.2 ×2, 8.1.8.2 ×14, 8.1.8.3 ×23 [M22]. **8.1.8.4 appears nowhere** (grep exit 1) [M23].
  - The bridge has no version check (grep exit 1) [C24]. Guard checks `>= 8.1.6.3` [C23].
  - The 2026-11-04 correction stands [P14]. The 8.1.7.2 lines are about hot-reload. The walk-forward measurements are on 8.1.8.2 (README:364-414) [B29][B30][B32], all REPORTED BY eman007.
  - Code does not know the VM's build. Amear reports 8.1.8.4 [P11]. D-2026-11-06-A item 1 (record it) is pending.
- **.NET.** No version is stated. NT8's own compiler builds the AddOn [C25]. Anything further is UNVERIFIED.

## Q5. Security and safety surface

- **Off-host connections.** The bridge cannot accept any: it has no listener [A03][M03]. An off-host actor would need some way to write `Documents\NinjaTrader 8\NT8Bridge\trigger`, such as a share. (INFERRED.)
- **Authentication.** None. There is no token, HMAC, signature or ACL code; the `signature` hits are comments [A10]. The folders are made with plain `CreateDirectory` / `mkdir` [A01][A04]. Any process running as the VM user can issue any command. (Code OBSERVED; the VM's effective ACL is UNVERIFIED.)
- **Commands that act on accounts, orders, connections or strategies** (OBSERVED unless marked):

| Command | NT8 call | Guard in code | Evidence |
|---|---|---|---|
| `flatten --name <acct>` | `acct.Cancel(...)`, `acct.Flatten(...)` (`NT8BridgeServer.cs:3328,3333`) | account must exist; **no Sim-only check, no confirmation** | [A11][A12][M06] |
| `watch` (loop) | calls flatten on positions with no protective stop | `--name` list, grace period | [A13][M25] |
| `ghostorders --cancel` | `target.Cancel(...)` (`:1173`) | no Sim-only check | [A14] |
| `ghostorders --reset` | `ResetSimulationAccount` (`:1226`) | Sim-only | [A15] |
| `strategies` enable/disable | clicks the Control Center Enabled checkbox | disable is refused while a position is open unless `force`; **enable has no guard** | [A16] |
| `reconnect --name` | `Connection.Connect(...)` (`:4439`) | comment says "UNCONDITIONAL" | [A17] |
| `playbackrun` | **`c.Disconnect()` on every non-Playback connection** (`NT8BridgeServerPlayback.cs:4880-4883`, baseline stage, only when `require` is playback and not `checkOnly`, `:4874`; `:5509`, connect stage), then `Connection.Connect(playback)` (`:5549`). Other Connect/Disconnect sites (`:1233, 4908, 5251, 5308, 5337, 5354`) were not traced: UNVERIFIED [M56] | none on the `baseline` and `connect` stages beyond that condition; the `alloff` stage reads a request `keep` list (`:5203`) and skips connections named in it (`:5219-5222`) | [A19][A21][M43][M51] |
| `AutoReconnect` AddOn | `Connection.Connect(savedOptions)` once NT8 reports a lost link; re-enables strategies | runs every NT8 session once compiled; `"reconnect": false` makes it alert-only | [M08][M09][A18] |
| `compile`, `reload`, `restart`, `watchdog` | compile/reload NT8's Custom assembly; kill NT8 | none | [C05][C06][A30][C07] |

- **Disconnects stop strategies.** The bridge's own comment: "an explicit Connection.Disconnect() disables every running strategy, and NT8 restores none of them" (`NT8BridgeServer.cs:1287-1288@9664d9b`) [M07] (REPORTED BY eman007). Against D-071 (no new NT8 connection): `reconnect`, `playbackrun` and AutoReconnect all call `Connection.Connect`, and `playbackrun` would drop a live Rithmic connection (INFERRED from [A17][A19][M08]).
- **Order submission.** `addon/*.cs` has no `.Submit( / CreateOrder( / SubmitOrder / PlaceOrder` (grep exit 1); as a positive control, `.Flatten(` and `.Cancel(` are found [M06]. (Absence OBSERVED.) `strategies` enable can still start a strategy that trades (INFERRED).
- **Does a backtest need a connection?** The bridge's backtest and analyzer code does not touch connections: 0 `Connection|Connect(` hits in the backtest span (`NT8BridgeServer.cs:2632-3176`) or the analyzer span (`NT8BridgeServerPlayback.cs:1677-2352`) [A23]. The README asks for NT8 "with historical data loaded" (`:34`) [M29]. Whether NT8's Analyzer needs a live connection to load data it does not already hold is NT8 behaviour: UNVERIFIED.
- **TTL "NOT executed" path** (`NT8BridgeServer.cs:195-212@9664d9b`) [M36][A06][A07].
  - A request older than its `ttlSec` (default 300 s, `NT8BridgeServerPlayback.cs:7672`) is consumed and answered `"status":"expired","executed":false`. Age is measured from the trigger file's last-write time.
  - The comment gives its purpose: "A caller that has timed out is gone; running its command now acts on a state it never saw" (`:195-196`). It keeps a backlog from running late.
  - It does not protect against a hostile or careless writer, who picks `ttlSec` with no upper bound and controls the file time (INFERRED from [A06][A07]).
  - The result write is `.tmp`, then delete, then `File.Move` (`:4535-4537`), not one atomic replace [A08].
- **Writes outside its folders.** `screenshot` to any path; `deploy` and `regions` into `bin\Custom`; AutoReconnect files in the NT8 root; guard's sqlite restore (Q4). No registry writes in the AddOn [A24], and none in the guard patterns searched [C18].

## Q6. Licence

- **Copyright holders** (OBSERVED):
  - The top-level `LICENSE` and `guard/LICENSE` are MIT, "Copyright (c) 2026 eman007" [M16][C26].
  - `addon/NT8BridgeServerPlayback.cs:2` and `nt8bridge/analyzerrun.py:2` read "Copyright (c) 2026 Quantrosoft Pty. Ltd." [M16]. The full list of `Copyright (c)` lines outside `.git` and `vendor` is [C28]. Seven more files mention Quantrosoft [M16]: `nt8bridge/satemplate.py`, `nt8bridge/playback_run.py`, `tests/test_analyzerrun.py`, `tests/test_satemplate.py`, `addon/NT8BridgeServer.cs`, `CHANGELOG.md` and `guard/THIRD-PARTY-NOTICES.txt`. In two of them the mention is not a copyright notice: `NT8BridgeServer.cs:2476` and `CHANGELOG.md:642` name Quantrosoft as the reporter of issue #6 [M53]. Guard's add-on zip ships `NT8BridgeServerPlayback.cs` under the Quantrosoft notice (`guard/THIRD-PARTY-NOTICES.txt:26-28`) [M48].
  - Vendored segno is BSD 3-Clause; the fonts are SIL OFL 1.1 [C26][C29][C30].
- **The MIT condition** (`LICENSE:12-13@9664d9b`) [C27]: "The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software."
- **If any pattern or code were ever used**, the matching notice must go with every copy or substantial portion: eman007's, plus Quantrosoft's for each file whose header carries it (INFERRED from the licence text; not legal advice). This unit uses nothing. "no edits to main from borrowed code" stands [P05].

## Q7. Maturity

- **History** (OBSERVED). 55 commits; the clone is full, not shallow [M01].
  - First commit 2026-06-09 (`724a29f`), last 2026-10-18 (`9664d9b`) [C31].
  - Commits per month, June to October: 6 / 9 / 7 / 10 / 23 [C33].
  - Authors: eman007 43, silentsudo-io 6, Heinrich Munz 5, GreyBeard 1 [M40].
- **Releases.** 17 version headings: 1.0.0 to 1.7.5 plus an older 0.1.0, besides "Unreleased". Six fall between 2026-10-10 and 2026-10-19 [C35]. (OBSERVED.)
- **Tests.** 96 test files: tests/ 41, guard/app/tests 36, guard/python/tests 10, tools 9 [C36]. There is no `.github` directory [C37]. None were run, so their status is UNVERIFIED.
- **Open issues.** Not checked: no network beyond the clone was allowed. UNVERIFIED. One code comment cites "issue #6 on the public repo" [C22].
- **README claims vs code.**
  - Implemented (code found; nothing run): compile/reload [C06][C38]; backtest via RunCommand [B12]; optimise/walk-forward [B05][B06]; flatten [A11]; reconnect [A17]; the strategies click [A16]; restart [A30].
  - Specified only (no code found by this unit; UNVERIFIED): "Parity with a GUI-less host, measured 2026-09-08 on NinjaTrader 8.1.8.2" (README:406-414) [B32][M15]; the template is "exactly what the GUI would run" (README:337-343) [B29]; hot-reload "Measured on NinjaTrader 8.1.7.2" (README:154) [C22].
  - `nt8bridge/backtest.py` promises an `equity` field that the AddOn does not emit [B38].

## NEEDS AMEAR

Questions only. None is answered here.

1. Do you lift "no NT8 runs or imports on the VM" (2026-11-05T23:50:09Z) for importing the bridge AddOn? If so, for which files: `NT8BridgeServer.cs` + `NT8BridgeServerPlayback.cs` only, or also `AutoReconnect.cs` and `ChartDataSeriesSwitcher.cs`?
2. Test 2a needs the bridge installed. Is installing it (copying C# into `bin\Custom` and compiling in NT8) an "import on the VM" under the ban that 2a is meant to lift? If so, which comes first, and by whose hand?
3. Is a file-drop control folder on the VM acceptable, given that any process running as the VM user can issue `flatten`, `reconnect`, `strategies` and `playbackrun` with no authentication? (There is no listening port that could be bound to localhost: the bridge has none.)
4. Do you rule out `playbackrun`, `reconnect`, `flatten`, `strategies`, `ghostorders` and the `AutoReconnect` AddOn on a VM that holds the Rithmic connection (D-071)?
5. Is NT8 Guard in or out of scope? It brings scheduled tasks, a saved NT8 password, auto-login and auto-kill/relaunch.
6. Which NT8 build is on the VM? D-2026-11-06-A item 1 is pending. The newest build the bridge's clone names is 8.1.8.3; the clone never names 8.1.8.4.
7. Is the strategy on the VM the repo's `ninjascript/PraxisNoiseAreaBreakout.cs`? Which copy or hash?
8. Which account do tests use (Sim101 or another), given that `flatten` has no Sim-only check?
9. Does a VMware snapshot precede the import (R-VN4-13, "Yeah, just do the snapshot." [P06]), and is that your hand step?
10. For test 2a ("drives the baseline from the terminal"): does it count if you set a Strategy Analyzer tab by hand once and the terminal then presses Run? Or must every setting come from the terminal?
11. How should the source reach the VM? Options: the README's SSH clone (needs a GitHub key; R-VN4-1, "Only within this directory." [P06]), an anonymous HTTPS clone on the VM, or a copy through the Z: share. May `pip` download packages on the VM?
12. Arm (a) has "nothing optimised". The bridge's walk-forward refuses a blank `opt`, and its CLI refuses one with no ranges, but a one-value range passes its checks. Arm (b)'s lookback, noise multiplier and stop-ATR multiplier are not properties of the committed strategy. How should each arm be run through the bridge?

## What this unit did not do

This unit ran nothing, installed nothing, and did not touch the VM, the share or NT8. Its only network call was one anonymous `git clone`. It staged nothing and made no change to beads or ledgers beyond the two MANIFEST rows. Three capture workers and one adversarial worker read the clone under the same limits.

## Appendix: evidence (pasted output; cited blocks only)

[P02]
```
$ git show e31b9a4:DECISIONS.md | /usr/bin/grep -n 'D-2026-11-06-A' | head -2 | cut -c1-120; git show e31b9a4:DECISIONS.md | /usr/bin/grep -nF 'Order: read the bridge' | cut -c1-40
991:## 2026-11-06 — D-2026-11-06-A: Amear's voice notes of 2026-11-06 (NT8 version; in-VM automation lift conditions; 
1003:2. In-VM automation (Oct 28 ruling)
```

[P03]
```
$ git show e31b9a4:DECISIONS.md | /usr/bin/grep -oF 'Order: read the bridge'"'"'s code read-only; write an install walkthrough; VMware snapshot first; then install. Direction: the walk-forward runs in NT8 through the bridge, not in a Mac-side Python copy.' | head -1
Order: read the bridge's code read-only; write an install walkthrough; VMware snapshot first; then install. Direction: the walk-forward runs in NT8 through the bridge, not in a Mac-side Python copy.
```

[P04]
```
$ /usr/bin/grep -n '^- \[2026-11-06T18:33:03Z\] WHO: praxis-master' DECISION_LOG.md | cut -c1-80; /usr/bin/grep -oF 'Limits: clone anonymously into its own empty scratchpad directory (no `gh`, no login' DECISION_LOG.md
464:- [2026-11-06T18:33:03Z] WHO: praxis-master | WHO COMMITTED: amear (typed) |
Limits: clone anonymously into its own empty scratchpad directory (no `gh`, no login
```

[P05]
```
$ /usr/bin/grep -n '^- \[2026-11-05T23:50:09Z\] WHO: amear' DECISION_LOG.md | cut -c1-70; /usr/bin/grep -oF 'no new NT8 connection (D-071), no NT8 runs or imports on the VM' DECISION_LOG.md | head -1
519:- [2026-11-05T23:50:09Z] WHO: amear | WHAT: **RULINGS + OVERNIGHT 
no new NT8 connection (D-071), no NT8 runs or imports on the VM
```

[P06]
```
$ /usr/bin/grep -nE '^- \*\*R-VN4-(1|13)\*\*' DECISIONS.md | cut -c1-120
934:- **R-VN4-1** — GitHub login, future use: "Only within this directory."
960:- **R-VN4-13** — NT8 add-ons: "Yeah, just do the snapshot."
```

[P07]
```
$ awk 'NR==73||NR==86{print NR": "$0}' docs/reports/2026-11-01-three-strategy-results.md | cut -c1-200; awk 'NR==10{print NR": "$0}' docs/reports/2026-11-01-three-strategy-results.md
73: | All | 1190 | $197327.60 | $878467.36 | -$681139.76 | $3522.40 | 1.29 | 484/706/0 | 40.67% | $35887.04 | -$5407.96 | $165.82 | -$45282.04 | -$45282.04 |
86: | Instrument | NQCONTROW SEP25 | NQCONTROW SEP25 | MATCH |
10: Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
```

[P08]
```
$ /usr/bin/grep -c '8\.1\.' docs/reports/2026-11-01-three-strategy-results.md; /usr/bin/grep -c 'NQCONTROW' docs/reports/2026-11-01-three-strategy-results.md
0
18
```

[P09]
```
$ /usr/bin/grep -oE '\[1\] Strategy.{0,0}|07-10 = `PraxisNoiseAreaBreakout` \(1190 rows\)' docs/reports/2026-11-01-three-strategy-results.md | head -2
[1] Strategy
07-10 = `PraxisNoiseAreaBreakout` (1190 rows)
```

[P10]
```
$ awk 'NR==111{print NR": "$0}' docs/reports/2026-10-31-voice-session-notes-2.md
111: - Settings, same as the 10-31 run: NQCONTROW SEP25 · Last · Minute 1 · 2021-03-08 → 2026-07-17 · CME US Index Futures RTH · Break at EOD ✓ · Include commission ✓ PRAXIS · Max bars look back 256 · Bars required 20 · Standard (Fastest) · Fill limit on touch ☐ · Slippage 2 · Entries per direction 1 · All entries · Exit on session close ✓ · Set order quantity Strategy · DAY · BandOrVWAP · Contracts 1.
```

[P11]
```
$ awk 'NR==161{print NR": "$0}' docs/reports/2026-10-31-voice-session-notes-2.md | cut -c1-260
161: - **The NT8 version reads 8.1.8.4.** Amear: "updated it". He updated NT8 himself, which supersedes the 10-28 ruling to stay on 8.1.7.2. C4 ran on 8.1.8.4.
```

[P12]
```
$ /usr/bin/grep -nE 'ExitMode +=|Contracts +=|public class PraxisNoiseAreaBreakout ' ninjascript/PraxisNoiseAreaBreakout.cs; git log -1 --format='%h %cI' -- ninjascript/PraxisNoiseAreaBreakout.cs
53:	public class PraxisNoiseAreaBreakout : Strategy
118:				ExitMode      = PraxisNoiseExitMode.BandOrVWAP; // spec §4 p.13 — paper's PREFERRED exit. The only knob.
119:				Contracts     = 1;                  // position sizing only (NOT a rule knob); paper uses vol-target sizing (§3 p.15) not ported here.
208:				double stop = (ExitMode == PraxisNoiseExitMode.BandOrVWAP && vwapCumVol > 0)
216:				double stop = (ExitMode == PraxisNoiseExitMode.BandOrVWAP && vwapCumVol > 0)
719ab11 2026-07-16T15:41:01-04:00
```

[P13]
```
$ awk 'NR==65||NR==216||NR==217||NR==245||NR==280||NR==408{print NR": "$0}' docs/reports/2026-11-04-comparable-builds.md | cut -c1-230
65: - **Walk-forward from outside NT8 (OBSERVED, implemented; untested on 8.1.7.2).** eman007/cli-nt-bridge (MIT, LICENSE file in tree). Manager re-print:
216: | A2 | eman007/cli-nt-bridge · `addon/NT8BridgeServerPlayback.cs` `RunAnalyzerRun` ~1827-1849 | external driver for NT8 WalkForward (implemented; unverified on 8.1.7.2) | MIT | third-party AddOn on the trading install |
217: | A3 | eman007/cli-nt-bridge · `addon/NT8BridgeServer.cs` 200-212 (TTL → "NOT executed"), 4534-4537 (`.tmp` + `File.Move`) | stale-request rejection; atomic write (implemented) | MIT | pattern for the PRAXIS watcher and th
245: eman007/cli-nt-bridge	17	2026-10-19T05:22:33Z	MIT	PowerShell	false	false
280: eman007/cli-nt-bridge main addon/NT8BridgeServer.cs     4766 lines 948cb9d5bef0
408: 200	eman007/cli-nt-bridge	HEAD	README.md	633 lines 8fb9566d11f8
```

[P14]
```
$ awk 'NR>=663&&NR<=666{print NR": "$0}' docs/reports/2026-11-04-comparable-builds.md | cut -c1-260
663: **j. eman007/cli-nt-bridge NT8 version: CORRECTED.** Every README line that names an 8.1.x build:
664: ```
665: $ /usr/bin/grep -nE '8\.1\.[0-9]' eman007__cli-nt-bridge/README.md | cut -c1-200
666: 34:- NinjaTrader 8 (developed/verified against 8.1.6.x), with historical data loaded
```

[P15]
```
$ awk 'NR==29||NR==65{print NR": "$0}' docs/specs/2026-11-05-walk-forward-spec.md | cut -c1-240; git log -1 --format='%h' -- docs/specs/2026-11-05-walk-forward-spec.md
29: - *"1. Walk-forward runs BOTH ways: (a) paper's fixed rules, nothing optimised; (b) four parameters tuned per window — lookback, noise multiplier, stop-ATR multiplier, exit policy. A stop is added to the strategy for (b) on its own br
65: - What: the paper's fixed rules, nothing optimised (item 1a, `DECISIONS.md:812`). — RULED (D-2026-11-05-A). It runs on the unchanged baseline (typed item c). — RULED (typed).
221ef59
```

[P16]
```
$ /usr/bin/grep -c 'NinjaScriptProperty' ninjascript/PraxisNoiseAreaBreakout.cs; /usr/bin/grep -nE '\{ *get; *set; *\}' ninjascript/PraxisNoiseAreaBreakout.cs; awk 'NR==74||NR==76||NR==116{print NR": "$0}' ninjascript/PraxisNoiseAreaBreakout.cs | cut -c1-160
2
300:		public PraxisNoiseExitMode ExitMode { get; set; }
305:		public int Contracts { get; set; }
74: 		private const int Lookback = 14;
76: 		private const double BandSigmaMult = 1.0;
116: 				//     private consts (field region), not settable Inputs — Analyzer cannot vary them
```

[P17]
```
$ awk 'NR>=105&&NR<=113{print NR": "$0}' ninjascript/PraxisNoiseAreaBreakout.cs | cut -c1-120
105: 				Calculate                                 = Calculate.OnBarClose;
106: 				EntriesPerDirection                       = 1;
107: 				EntryHandling                             = EntryHandling.AllEntries;
108: 				IsExitOnSessionCloseStrategy              = true;   // backstop; explicit 16:00 flat is primary
109: 				ExitOnSessionCloseSeconds                 = 30;
110: 				StartBehavior                             = StartBehavior.WaitUntilFlat;
111: 				TimeInForce                               = TimeInForce.Day;
112: 				BarsRequiredToTrade                       = 20;
113: 				IsInstantiatedOnEachOptimizationIteration = false;
```

[P18]
```
$ /usr/bin/grep -n '^- \[2026-11-06T18:33:03Z\] WHO: praxis-master' DECISION_LOG.md | cut -c1-60; /usr/bin/grep -oF 'AddOn import = an "import on the VM", barred until Amear lifts it' DECISION_LOG.md | head -1
464:- [2026-11-06T18:33:03Z] WHO: praxis-master | WHO COMMIT
AddOn import = an "import on the VM", barred until Amear lifts it
```

[M01]
```
$ git rev-parse HEAD; git rev-parse --is-shallow-repository; git rev-list --count HEAD; git status --porcelain | wc -l
9664d9b255bfa34b120d88a481afe7741a4115e6
false
55
       0
```

[M02]
```
$ shasum -a 256 addon/NT8BridgeServer.cs README.md | cut -c1-12,65-; wc -l addon/NT8BridgeServer.cs README.md
948cb9d5bef0  addon/NT8BridgeServer.cs
8fb9566d11f8  README.md
    4766 addon/NT8BridgeServer.cs
     633 README.md
    5399 total
```

[M03]
```
$ /usr/bin/grep -c 'Timer' addon/NT8BridgeServer.cs; /usr/bin/grep -c 'Path' nt8bridge/ntio.py
4
10
```

[M04]
```
$ /usr/bin/grep -rnlE 'HttpListener|TcpListener|UdpClient|IPAddress|NamedPipe|FileSystemWatcher|socket\.socket|http\.server|socketserver|Invoke-WebRequest|Invoke-RestMethod|WebClient|HttpClient|urllib' addon nt8bridge guard tools; echo "grep-exit=$?"
guard/app/lib/Guard.Alerts.psm1
guard/python/vendor/segno/__init__.py
guard/python/vendor/segno/writers.py
guard/build/Guard.Release.psm1
grep-exit=0
```

[M05]
```
$ /usr/bin/grep -nE 'Listen|Bind|IPAddress|Loopback' addon/AutoReconnect.cs | cut -c1-200; echo "grep-exit=$?"; /usr/bin/grep -nE '^using System\.Net' addon/AutoReconnect.cs addon/NT8BridgeServer.cs addon/NT8BridgeServerPlayback.cs
391:                System.Reflection.BindingFlags anyStatic = System.Reflection.BindingFlags.Public
392:                    | System.Reflection.BindingFlags.NonPublic | System.Reflection.BindingFlags.Static;
398:                    System.Reflection.BindingFlags.NonPublic | System.Reflection.BindingFlags.Instance) != null;
883:                    : mt.GetProperty("All", System.Reflection.BindingFlags.Public | System.Reflection.BindingFlags.Static);
1016:                System.Reflection.BindingFlags.Instance | System.Reflection.BindingFlags.Public
1017:                | System.Reflection.BindingFlags.NonPublic);
1687:        private const System.Reflection.BindingFlags AnyInstance =
1688:            System.Reflection.BindingFlags.Public | System.Reflection.BindingFlags.NonPublic | System.Reflection.BindingFlags.Instance;
1730:                    var sp = cc.GetProperty(sm, System.Reflection.BindingFlags.Public | System.Reflection.BindingFlags.NonPublic | System.Reflection.BindingFlags.Static);
1920:                var onClick = typeof(System.Windows.Controls.Primitives.ButtonBase).GetMethod("OnClick", System.Reflection.BindingFlags.NonPublic | System.Reflection.BindingFlags.Instance);
grep-exit=0
addon/AutoReconnect.cs:110:using System.Net;
```

[M06]
```
$ /usr/bin/grep -nE '\.Submit\(|CreateOrder\(|SubmitOrder|PlaceOrder' addon/*.cs; echo "grep-exit=$?"; /usr/bin/grep -nE '\.Flatten\(|\.Cancel\(' addon/NT8BridgeServer.cs | cut -c1-160
grep-exit=1
1014:                // working state, so acct.Cancel() was never called on exactly the orders that need it.
1150:                // wedged in CancelPending. acct.Cancel() does reach them - `flatten` just never passes
1173:                            target.Cancel(cancelTargets);          // acts AFTER the locks (Lesson #159)
3328:                    try { acct.Cancel(ordersToCancel); cancelled = ordersToCancel.Count; }
3333:                    try { acct.Flatten(instrs); flattenCalled = true; }
```

[M07]
```
$ awk 'NR>=1284&&NR<=1290{print NR": "$0}' addon/NT8BridgeServer.cs | cut -c1-200
1284:         //
1285:         //  ⭐ WHY THIS IS NOT `workspace`. `workspace` walks the chart windows, so it sees only strategies
1286:         //  attached to a chart. The Control Center grid is the other population — strategies added in the
1287:         //  Strategies tab itself — and it is the one that a connection cycle turns OFF: an explicit
1288:         //  Connection.Disconnect() disables every running strategy, and NT8 restores none of them, not on
1289:         //  reconnect and not on an app restart. Answering "is it enabled, and if not turn it back on" from
1290:         //  a script is the difference between a box that heals and a box that needs an RDP session.
```

[M08]
```
$ awk 'NR>=1&&NR<=12{print NR": "$0}' addon/AutoReconnect.cs | cut -c1-200
1: // AutoReconnect.cs — NinjaTrader 8 AddOn: auto-reconnect dropped connections + ALERT on dead feeds.
2: //
3: // DROP-IN: copy this file into  Documents\NinjaTrader 8\bin\Custom\AddOns\  and compile once
4: // (NinjaScript Editor -> F5). From then on, every NT8 session it watches your connections.
5: // No Python; config optional.
6: //
7: // WHAT IT DOES — two distinct behaviors, split so RUNNING STRATEGIES ARE NEVER KILLED:
8: //   * RECONNECT — only when NinjaTrader itself declares the LINK lost (Status == ConnectionLost).
9: //     After a grace period (NT8's own retry gets first crack) it re-issues
10: //     Connection.Connect(savedOptions) on the UI thread, with exponential backoff, a max-attempts
11: //     cap, then a cooldown. This is the long-standing v1 behavior. Config "reconnect": false makes it
12: //     ALERT-ONLY instead (NT8 Guard's Watch only preset).
```

[M09]
```
$ /usr/bin/grep -nE 'Enabled|IsEnabled|SetState' addon/AutoReconnect.cs | awk -F: '$1>=1820&&$1<=1845' | cut -c1-200
1821:        private List<string> CaptureEnabledStrategyNames()
1832:        // Re-enable the named strategies by setting each matching entry's IsEnabled=true (or dry-run log). Returns count set.
1833:        // Re-enable the named strategies by CLICKING each row's Enabled checkbox (ButtonBase.OnClick — the only
1834:        // path that actually starts the strategy; setting IsEnabled or executing the RoutedCommand only flips
```

[M10]
```
$ cat config/config.json
{
  "strategy": "MyStrategy.cs",
  "typeName": "MyStrategy",
  "instrument": "ES 06-25",
  "barType": {"type": "Minute", "value": 5},
  "from": "2024-01-01",
  "to": "2024-12-31",
  "capital": 50000,
  "commission": "MyCommissionTemplate",
  "slippageTicks": 1,
  "params": {"Period": 14, "StopTicks": 40, "TargetTicks": 80}
}
```

[M11]
```
$ awk 'NR>=2524&&NR<=2530{print NR": "$0}' addon/NT8BridgeServer.cs | cut -c1-200
2524:         // ParseParams hands back a Dictionary, and Dictionary iteration order is not part of its
2525:         // contract -- so "Strategy processed last" was always reachable and was never a caller's
2526:         // typo. Hoisting the swap keys is what makes ONE configure call carrying Strategy plus
2527:         // data-series keys behave like the two-call workaround (Strategy alone, then the rest).
2528:         // Measured on the live SA tab: From / To / BarsPeriod / IsTickReplay are writable ONLY on
2529:         // the template, so those are precisely the keys a mis-ordered call drops. (Instrument-
2530:         // OrInstrumentList exists on tabStrategyProperties too, which is earlier in the target
```

[M13]
```
$ /usr/bin/grep -nE 'UserDataDir, *"NT8Bridge"' addon/NT8BridgeServer.cs addon/NT8BridgeServerPlayback.cs | cut -c1-200; awk 'NR>=294&&NR<=310{print NR": "$0}' addon/NT8BridgeServer.cs | /usr/bin/grep -E 'backtest|configure|analyzerrun|satemplate' | cut -c1-160
addon/NT8BridgeServer.cs:105:            string root = Path.Combine(Globals.UserDataDir, "NT8Bridge");
addon/NT8BridgeServer.cs:715:                outPath = Path.Combine(Globals.UserDataDir, "NT8Bridge", "result", "shot_" + id + ".png");
addon/NT8BridgeServerPlayback.cs:468:                string dir = Path.Combine(NinjaTrader.Core.Globals.UserDataDir, "NT8Bridge", "result");
addon/NT8BridgeServerPlayback.cs:559:                    string dir0 = Path.Combine(Globals.UserDataDir, "NT8Bridge");
addon/NT8BridgeServerPlayback.cs:626:                        string dir = Path.Combine(Globals.UserDataDir, "NT8Bridge");
addon/NT8BridgeServerPlayback.cs:3512:                             ? ("ON - " + Path.Combine(Globals.UserDataDir, "NT8Bridge", "ntlog.txt")
296:             if (kind == "backtest") return "backtest_";
307:             if (kind == "configure") return "configure_";
```

[M15]
```
$ /usr/bin/grep -niE 'parity|reproduc|same result|identical' README.md | cut -c1-200
406:Parity with a GUI-less host, measured 2026-09-08 on NinjaTrader 8.1.8.2 (NQ 09-26,
410:hosts; in-sample ranking per window identical (250 > 200 > 150 three times, 150 > 200 > 250 in
411:the last window); every CSV written on both sides byte-identical (11 of 11, all 4 out-of-sample
```

[M16]
```
$ /usr/bin/grep -rnl 'Quantrosoft' . --exclude-dir=.git; /usr/bin/grep -rn 'Copyright (c)' LICENSE guard/LICENSE addon/NT8BridgeServerPlayback.cs nt8bridge/analyzerrun.py | cut -c1-160
./CHANGELOG.md
./tests/test_analyzerrun.py
./tests/test_satemplate.py
./addon/NT8BridgeServerPlayback.cs
./addon/NT8BridgeServer.cs
./guard/THIRD-PARTY-NOTICES.txt
./nt8bridge/satemplate.py
./nt8bridge/analyzerrun.py
./nt8bridge/playback_run.py
LICENSE:3:Copyright (c) 2026 eman007
guard/LICENSE:3:Copyright (c) 2026 eman007
addon/NT8BridgeServerPlayback.cs:2:Copyright (c) 2026 Quantrosoft Pty. Ltd.
nt8bridge/analyzerrun.py:2:# Copyright (c) 2026 Quantrosoft Pty. Ltd.
```

[M17]
```
$ awk 'NR>=37&&NR<=44{print NR": "$0}' nt8bridge/restart.py | cut -c1-200
37: # ⚠ NO DEFAULT EXE, for the same reason there is no default task — and the failure is worse.
38: #
39: # Launching `bin\NinjaTrader.exe` directly produces a PROCESS, not a usable PLATFORM: on a box where
40: # NT is started through a wrapper that supplies credentials, the bare exe stops at the Welcome screen.
41: # A running-check sees NinjaTrader.exe and reports healthy, so the caller believes it restarted the
42: # platform and every subsequent headless step fails against a login prompt. Reported upstream from a
43: # box that launches via an auto-login wrapper. Pass --exe (or better, --task) explicitly.
44: DEFAULT_EXE = ""
```

[M19]
```
$ /usr/bin/grep -niE 'ntfy|webhook' guard/app/README.md | head -5 | cut -c1-200; awk 'NR==5{print NR": "$0}' README.md
40:| **Alerts** | Phone alerts through ntfy: a private random topic, a QR code to subscribe, how loud each kind of alert is, an optional webhook, and Send a test. The topic and the webhook address sta
245:  "alerts":     { "ntfyTopic": "pick-a-long-random-name" },
251:- `alerts.ntfyTopic` — your phone alerts (install the ntfy app and subscribe to the same name). Treat
279:| `alerts.ntfyTopic` (else `alerts.webhookUrl`) | `webhookUrl` + `webhookFormat` |
5: Everything runs locally and in-process: a small Python CLI talks to a NinjaScript **AddOn** running inside NinjaTrader through plain JSON files. No UI automation, no network.
```

[M20]
```
$ awk 'NR>=84&&NR<=89{print NR": "$0}' guard/app/Register-GuardTasks.ps1 | cut -c1-200
84:         Import-Module (Join-Path $PSScriptRoot 'lib\Guard.FeedGuard.psm1')
85:         $cfg = Get-GuardConfig $gh
86:         $nt8Dir = Get-Nt8DataDir ([string]$cfg.nt8.dataDir)
87:         if (Test-Path -LiteralPath $nt8Dir) { Write-FeedGuardConfig -Config $cfg -Nt8Dir $nt8Dir | Out-Null }
88:         Remove-Item -LiteralPath $stopFile -Force
89:         Write-GuardEvent -Component guard -Kind 'guard.started' -Severity info -Text 'Guard running again: its tasks were installed' -GuardHome $gh
```

[M21]
```
$ awk 'NR==148||NR==232{print NR": "$0}' README.md | cut -c1-220; awk 'NR==491{print NR": "$0}' CHANGELOG.md | cut -c1-220
148: `--type` is accepted but ignored — NinjaTrader's compiler always builds the **whole tree**, exactly as F5 does, so there is nothing to scope. `compile` on its own is enough.
232: It answers the questions a stalled status feed can't: **is a position actually open right now**, what are the live stop/target orders, and what were the real fills. Read-only — it never submits, cancels, or flatte
491:   Adds a second AddOn file (`NT8BridgeServerPlayback.cs`) carrying the stages this needs.
```

[M22]
```
$ /usr/bin/grep -rnoE '8\.1\.[0-9]+\.[0-9x]+' . --exclude-dir=.git -h | sed 's/^[0-9]*://' | sort | uniq -c
   2 8.1.5.2
   1 8.1.6.0
   9 8.1.6.3
   5 8.1.6.x
   2 8.1.7.2
  14 8.1.8.2
  23 8.1.8.3
```

[M23]
```
$ /usr/bin/grep -rnE '8\.1\.8\.4' . --exclude-dir=.git; echo "grep-exit=$?"
grep-exit=1
```

[M24]
```
$ /usr/bin/grep -rnE 'import winreg|from guard|import guard|nt8guard' nt8bridge; echo "grep-exit=$?"; /usr/bin/grep -c 'import' nt8bridge/cli.py
grep-exit=1
52
```

[M25]
```
$ /usr/bin/grep -nE 'flatten|reconnect' nt8bridge/watch.py nt8bridge/connwatch.py | head -8 | cut -c1-200
nt8bridge/watch.py:7:grace period, flatten it and log WHY.
nt8bridge/watch.py:23:from nt8bridge import flatten as ntflatten
nt8bridge/watch.py:77:    _flatten=None,
nt8bridge/watch.py:85:    to the real scan/flatten/sleep/clock.
nt8bridge/watch.py:90:    flatten_fn = _flatten or (lambda acct, instr: ntflatten.run_flatten(acct, instr))
nt8bridge/watch.py:108:                result = flatten_fn(f["account"], f["instrument"])
nt8bridge/watch.py:116:                    "flatten_result": result,
nt8bridge/connwatch.py:1:"""Connection guardian: auto-reconnect connections that dropped INADVERTENTLY.
```

[M26]
```
$ awk 'NR>=4436&&NR<=4454&&/tfile|GetTemplateFolder|Save/{print NR": "$0}' addon/NT8BridgeServerPlayback.cs | cut -c1-200
4442:                             Directory.CreateDirectory(Path.GetDirectoryName(tfile));
4444:                             // SaveFullStrategyTemplate FILLS the container - it writes
4452:                             miSave.Invoke(null, new object[] { root, probe });
4453:                             new System.Xml.Linq.XDocument(root).Save(tfile);
4454:                             step("save", File.Exists(tfile),
```

[M27]
```
$ /usr/bin/grep -nE 'open\(|write' nt8bridge/regions.py | head -6 | cut -c1-200
66:                text = io.open(p, encoding="utf-8", errors="replace").read()
83:    ⚠ It CAN, however, remove the wrong tail if detection is wrong — which is why this writes
87:    text = io.open(path, encoding="utf-8", errors="replace").read()
96:        io.open(str(path) + ".bak", "w", encoding="utf-8", newline="").write(text)
97:    io.open(path, "w", encoding="utf-8", newline="").write(kept)
```

[M28]
```
$ awk 'NR==1189||NR==1190||NR==1314||NR==1315||NR==1330||NR==1331{print NR": "$0}' nt8bridge/cli.py | cut -c1-200
1189:     p_pr = sub.add_parser(
1190:         "playbackrun",
1314:     p_strat = sub.add_parser(
1315:         "strategies",
1330:     p_ghost = sub.add_parser(
1331:         "ghostorders",
```

[M29]
```
$ awk 'NR>=30&&NR<=60{print NR": "$0}' README.md | cut -c1-200
30: The AddOn polls `…\Documents\NinjaTrader 8\NT8Bridge\trigger\` for request files and writes results to `…\result\`. Every command prints structured JSON to stdout.
31: 
32: ## Requirements
33: 
34: - NinjaTrader 8 (developed/verified against 8.1.6.x), with historical data loaded
35: - Python 3.10+
36: - Windows (NinjaTrader is Windows-only)
37: 
38: ## Install
39: 
40: ```bash
41: git clone git@github.com:eman007/cli-nt-bridge.git
42: cd cli-nt-bridge
43: python -m venv .venv
44: .venv\Scripts\Activate.ps1                  # PowerShell: activate the venv for this shell
45: python -m pip install -e ".[dev,report]"    # numpy+pyarrow are base deps; report adds matplotlib for --pdf
46: ```
47: 
48: Every command below assumes the venv is **active** — you'll see `(.venv)` in your prompt. If activation is inconvenient or PowerShell blocks the activate script, prefix every command with the ve
49: 
50: Then load the AddOn into NinjaTrader **once**:
51: 
52: 1. `python -m nt8bridge deploy --strategy addon/NT8BridgeServer.cs --kind addon`
53:    (copies it to `…\NinjaTrader 8\bin\Custom\AddOns\`)
54: 2. In NinjaTrader, open the NinjaScript Editor and **compile (F5)**. After this one compile the AddOn loads on every NinjaTrader start, and strategy compiles no longer need F5.
55: 
56: Verify the setup:
57: 
58: ```bash
59: python -m nt8bridge doctor
60: ```
```

[M30]
```
$ /usr/bin/grep -nE 'Import|NinjaScript Add-On|AddOns\.zip' guard/README.md README.md | head -8 | cut -c1-200
guard/README.md:27:ship in the release as `NT8Guard-AddOns.zip`, for NinjaTrader's *Tools > Import > NinjaScript Add-On*.
```

[M32]
```
$ /usr/bin/grep -nE 'WebRequest|HttpWebRequest|WebClient|Dns\.|Ping|Socket|ServicePointManager|https?://' addon/AutoReconnect.cs | head -8 | cut -c1-200; echo "grep-exit=$?"
329:            try { ServicePointManager.SecurityProtocol |= SecurityProtocolType.Tls12; } catch { }   // https webhooks
2000:                    HttpWebRequest req = (HttpWebRequest)WebRequest.Create(url);
2091:        //    "alertRepeatMinutes":5, "alertSound":"Alert1.wav", "webhookUrl":"https://...",
grep-exit=0
```

[M33]
```
$ /usr/bin/grep -nE 'Invoke-RestMethod|Invoke-WebRequest|https://' guard/app/lib/Guard.Alerts.psm1 | head -5 | cut -c1-200
12:    Invoke-RestMethod -Uri $Uri -Method Post -Headers $Headers -Body $Body -ContentType $ContentType -TimeoutSec 10 | Out-Null
```

[M34]
```
$ /usr/bin/grep -nE 'AutoReconnect|ChartDataSeriesSwitcher' addon/NT8BridgeServer.cs addon/NT8BridgeServerPlayback.cs | head -6 | cut -c1-200; echo "grep-exit=$?"
addon/NT8BridgeServer.cs:1314:        //  ⚠ THIS REACH IS DUPLICATED. A companion connection-recovery AddOn (`AutoReconnect.cs`, not
addon/NT8BridgeServer.cs:2027:        // shared ChartDataSeriesSwitcher (the ChartScheduler reuses the same engine). The switcher is
addon/NT8BridgeServer.cs:2252:            if (sr == null) return CsErr(id, "ChartDataSeriesSwitcher unavailable (not compiled into Custom.dll?)");
addon/NT8BridgeServer.cs:2271:        // Invoke a static method on the sibling ChartDataSeriesSwitcher by reflection (same assembly at
addon/NT8BridgeServer.cs:2277:                Type t = Type.GetType("NinjaTrader.NinjaScript.AddOns.ChartDataSeriesSwitcher");
grep-exit=0
```

[M35]
```
$ /usr/bin/grep -nE 'kind == "(compile|reload|deploy|screenshot|flatten|reconnect|strategies|ghostorders|playbackrun|backtest|analyzerrun|configure|satemplate)"' addon/NT8BridgeServer.cs | cut -c1-160
214:                if (kind == "compile")
216:                else if (kind == "reload")
220:                else if (kind == "backtest")
224:                else if (kind == "flatten")
228:                else if (kind == "reconnect")
232:                else if (kind == "playbackrun")
238:                else if (kind == "strategies")
240:                else if (kind == "ghostorders")
242:                else if (kind == "screenshot")
248:                else if (kind == "configure")
250:                else if (kind == "satemplate")
252:                else if (kind == "analyzerrun")
295:            if (kind == "flatten") return "flatten_";
296:            if (kind == "backtest") return "backtest_";
298:            if (kind == "reconnect") return "reconnect_";
302:            if (kind == "strategies") return "strategies_";
303:            if (kind == "ghostorders") return "ghostorders_";
304:            if (kind == "screenshot") return "screenshot_";
307:            if (kind == "configure") return "configure_";
312:            if (kind == "reload") return "reload_";
```

[M36]
```
$ awk 'NR>=195&&NR<=212{print NR": "$0}' addon/NT8BridgeServer.cs | cut -c1-200
195:                 // A caller that has timed out is gone; running its command now acts on
196:                 // a state it never saw. Measured 2026-08-19: a backlog released after
197:                 // 11 minutes enabled, disabled and removed a strategy in the middle of
198:                 // a running measurement (see the file header).
199:                 double ageSec = (DateTime.UtcNow - writtenUtc).TotalSeconds;
200:                 double ttlSec = RequestTtlSec(text);
201:                 if (ageSec > ttlSec)
202:                 {
203:                     LogSafe("expired " + kind + " " + id + ": " + ageSec.ToString("0") +
204:                             "s old, ttl " + ttlSec.ToString("0") + "s - NOT executed");
205:                     WriteResult(ResultPrefixEx(kind, ResultPrefix(kind)) + id + ".json",
206:                         "{\"id\":" + JsonStr(id) + ",\"status\":\"expired\",\"executed\":false" +
207:                         ",\"ageSec\":" + ageSec.ToString("0.###", InvCi) +
208:                         ",\"ttlSec\":" + ttlSec.ToString("0.###", InvCi) +
209:                         ",\"errors\":[{\"code\":\"EXPIRED\",\"message\":" +
210:                         JsonStr("request waited " + ageSec.ToString("0") + "s in the queue, past its " +
211:                                 ttlSec.ToString("0") + "s TTL; not executed") + "}]}");
212:                     return;
```

[M37]
```
$ /usr/bin/grep -rniE 'slippage|fillresolution|fill resolution' addon; echo "grep-exit=$?"; /usr/bin/grep -rniE 'slippage' nt8bridge config | cut -c1-120
grep-exit=1
nt8bridge/config.schema.json:21:    "slippageTicks": {"type": "integer"},
config/config.json:10:  "slippageTicks": 1,
```

[M38]
```
$ awk 'FNR>=2632&&FNR<=2870{if(tolower($0)~/commission/)c++; if($0~/RunCommand/)r++} END{print "NT8BridgeServer.cs 2632-2870: commission lines=" c+0 ", RunCommand lines=" r+0}' addon/NT8BridgeServer.cs; awk 'FNR>=1677&&FNR<=2352{if(tolower($0)~/commission/)c++; if($0~/RunCommand/)r++} END{print "NT8BridgeServerPlayback.cs 1677-2352: commission lines=" c+0 ", RunCommand lines=" r+0}' addon/NT8BridgeServerPlayback.cs
NT8BridgeServer.cs 2632-2870: commission lines=0, RunCommand lines=4
NT8BridgeServerPlayback.cs 1677-2352: commission lines=0, RunCommand lines=5
```

[M39]
```
$ awk 'NR>=6283&&NR<=6290{print NR": "$0}' addon/NT8BridgeServerPlayback.cs | cut -c1-200
6283:                     // Optional override via the request's `tradingHours` field (e.g. a
6284:                     // 24/7 template for coverage experiments). The name must match an
6285:                     // installed template EXACTLY - on a miss the step fails and lists
6286:                     // every available name, so the caller never has to guess one.
6287:                     TradingHours th = inst.MasterInstrument.TradingHours;
6288:                     string thWanted = ExtractJsonString(triggerJson, "tradingHours");
6289:                     if (!string.IsNullOrWhiteSpace(thWanted))
6290:                     {
```

[M40]
```
$ git log --format='%an' | sort | uniq -c
   1 GreyBeard
   5 Heinrich Munz
  43 eman007
   6 silentsudo-io
```

[M41]
```
$ awk 'NR==1691||NR==1692||NR==1743||NR==1744||NR==1745{print NR": "$0}' addon/NT8BridgeServerPlayback.cs | cut -c1-200
1691:             if (string.IsNullOrWhiteSpace(optSpec))
1692:             { WriteResult(resultFile, BtErr(id, "analyzerrun: " + mode + " needs opt=Name:min:max:step[,...]")); return; }
1743:                             min  = Convert.ChangeType(f[1].Trim(), prop.PropertyType, InvCi);
1744:                             max  = Convert.ChangeType(f[2].Trim(), prop.PropertyType, InvCi);
1745:                             step = double.Parse(f[3].Trim(), InvCi);
```

[M42]
```
$ awk 'NR>=1749&&NR<=1758{print NR": "$0}' addon/NT8BridgeServerPlayback.cs | cut -c1-200; awk 'NR>=1726&&NR<=1770&&/min *[<>]=? *max|max *[<>]=? *min|CompareTo/{print "cmp " NR": "$0; c++} NR>=1726&&NR<=1770&&/step/{s++} END{print "1726-1770: min/max comparison lines=" c+0 ", control lines with step=" s+0}' addon/NT8BridgeServerPlayback.cs
1749:                         if (step <= 0)
1750:                         { WriteResult(resultFile, BtErr(id, "analyzerrun: step width in '" + part + "' must be > 0.")); return; }
1751:                         NinjaTrader.NinjaScript.Parameter par = new NinjaTrader.NinjaScript.Parameter();
1752:                         par.Name          = name;
1753:                         par.ParameterType = prop.PropertyType;
1754:                         par.Min           = min;
1755:                         par.Max           = max;
1756:                         par.Increment     = step;
1757:                         par.Value         = min;
1758:                         strat.OptimizationParameters.Add(par);
1726-1770: min/max comparison lines=0, control lines with step=7
```

[M43]
```
$ /usr/bin/grep -nE 'ExtractJsonString\(triggerJson, "keep"\)|Stage_Alloff' addon/NT8BridgeServerPlayback.cs | cut -c1-160
2615:                if (stage == "alloff") return Stage_Alloff(ctx);
5162:        private string Stage_Alloff(PbRunCtx ctx)
5203:                    string keepS = ExtractJsonString(triggerJson, "keep");
```

[M44]
```
$ /usr/bin/grep -c 'add_parser(' nt8bridge/cli.py; /usr/bin/grep -nE 'in ntanalyzerrun\.COMMANDS:' nt8bridge/cli.py; awk 'NR>=70&&NR<=89&&/MODES|COMMANDS/{print NR": "$0}' nt8bridge/analyzerrun.py | cut -c1-160
38
1261:    for _cmd in ntanalyzerrun.COMMANDS:
1429:    if argv[0] in ntanalyzerrun.COMMANDS:
84: MODES = {
89: COMMANDS = tuple(MODES)
```

[M45]
```
$ /usr/bin/grep -nE 'HttpListener|TcpListener|TcpClient|UdpClient|HttpWebRequest|WebRequest|WebClient|HttpClient|Socket|Dns\.|NamedPipe|FileSystemWatcher' addon/NT8BridgeServer.cs addon/NT8BridgeServerPlayback.cs addon/ChartDataSeriesSwitcher.cs; echo "grep-exit=$?"; /usr/bin/grep -c 'HttpWebRequest' addon/AutoReconnect.cs
grep-exit=1
1
```

[M46]
```
$ /usr/bin/grep -rnE '^ *(import|from) +(socket|http|urllib|requests|ssl|asyncio)' nt8bridge; echo "grep-exit=$?"; /usr/bin/grep -rnE '^ *(import|from) +(json|pathlib)' nt8bridge | head -2
grep-exit=1
nt8bridge/analyzerrun.py:76:from pathlib import Path
nt8bridge/config.py:4:import json
```

[M47]
```
$ /usr/bin/grep -nE '"schtasks", "/run"|Popen\(' nt8bridge/restart.py | cut -c1-160
99:        r = subprocess.run(["schtasks", "/run", "/tn", task],
158:        subprocess.Popen([str(p)], close_fds=True)
```

[M48]
```
$ /usr/bin/grep -nE 'NT8BridgeServerPlayback|Quantrosoft' guard/THIRD-PARTY-NOTICES.txt | cut -c1-200
26:4. NT8BridgeServerPlayback.cs - part of the NT8 link add-on (Playback and Strategy Analyzer requests)
27:   NT8Guard-AddOns.zip -> AddOns/NT8BridgeServerPlayback.cs
28:   Copyright (c) 2026 Quantrosoft Pty. Ltd.
```

[M49]
```
$ awk 'NR>=1726&&NR<=1732{print NR": "$0}' addon/NT8BridgeServerPlayback.cs | cut -c1-200
1726:                     // 3. The ranges, as NinjaTrader's own Parameter objects.
1727:                     var parJson = new StringBuilder("[");
1728:                     HashSet<string> optNames = new HashSet<string>(StringComparer.Ordinal);
1729:                     strat.OptimizationParameters.Clear();
1730:                     foreach (string part in optSpec.Split(new char[] { ',' }, StringSplitOptions.RemoveEmptyEntries))
1731:                     {
1732:                         string[] f = part.Split(':');
```

[M50]
```
$ awk 'NR>=113&&NR<=119{print NR": "$0}' nt8bridge/analyzerrun.py; awk 'NR==597{print NR": "$0}' nt8bridge/cli.py
113:         if step <= 0:
114:             raise ValueError("step width in '%s' must be > 0." % part)
115:         entries.append({"name": name, "min": f[1].strip(), "max": f[2].strip(),
116:                         "step": f[3].strip()})
117:     if not entries:
118:         raise ValueError("needs --opt=Name:min:max:step[,...]")
119:     return entries
597:         ntanalyzerrun.parse_opt_spec(args.opt)
```

[M51]
```
$ awk 'NR>=5219&&NR<=5223{print NR": "$0}' addon/NT8BridgeServerPlayback.cs | cut -c1-200
5219:                         bool spare = false;
5220:                         foreach (string k in keepList)
5221:                             if (string.Equals(k, nm, StringComparison.OrdinalIgnoreCase)) spare = true;
5222:                         if (spare) { kept.Add(nm + "=" + st); continue; }
5223:                         if (st != ConnectionStatus.Disconnected.ToString()) open.Add(c);
```

[M52]
```
$ awk 'NR==26||(NR>=68&&NR<=71){print NR": "$0}' nt8bridge/watchdog.py
26: NT8_EXE_DEFAULT = r"C:\Program Files\NinjaTrader 8\bin\NinjaTrader.exe"
68: def launch_nt8(exe: str = NT8_EXE_DEFAULT) -> None:
69:     if not os.path.exists(exe):
70:         raise FileNotFoundError(f"NinjaTrader exe not found: {exe} (pass --exe)")
71:     subprocess.Popen([exe], close_fds=True)
```

[M53]
```
$ awk 'NR==2476{print NR": "$0}' addon/NT8BridgeServer.cs | cut -c1-200; /usr/bin/grep -n 'Quantrosoft' CHANGELOG.md | cut -c1-160
2476:         //   Reported by Quantrosoft as issue #6 on the public repo (verified on 8.1.8.2).
642:  [@Quantrosoft](https://github.com/Quantrosoft) in #6, with a repro whose run kept `Tick 1` +
```

[M54]
```
$ awk 'NR==2684{print FILENAME":"NR": "$0}' addon/NT8BridgeServer.cs | cut -c1-200; awk 'NR==1736{print FILENAME":"NR": "$0}' addon/NT8BridgeServerPlayback.cs | cut -c1-200
addon/NT8BridgeServer.cs:2684:                     PropertyInfo p = strat.GetType().GetProperty(kv.Key, BindingFlags.Public | BindingFlags.Instance);
addon/NT8BridgeServerPlayback.cs:1736:                         PropertyInfo prop = strat.GetType().GetProperty(name, BindingFlags.Public | BindingFlags.Instance);
```

[M55]
```
$ /usr/bin/grep -n '"--exe"' nt8bridge/cli.py | cut -c1-160
1172:    p_rst.add_argument("--exe", default=ntrestart.DEFAULT_EXE,
1391:    p_wd.add_argument("--exe", default=ntwatchdog.NT8_EXE_DEFAULT)
```

[M56]
```
$ /usr/bin/grep -nE '\.Disconnect\(\)|Connection\.Connect\(' addon/NT8BridgeServerPlayback.cs | cut -c1-150
318:        //      pc.Disconnect();
1233:                        pc.Disconnect();
4883:                                    try { c.Disconnect(); } catch { }
4908:                                Connection.Connect(po2);
5251:                        try { c.Disconnect(); }
5308:                        pd.Disconnect();
5337:                        pc.Disconnect();
5354:                    Connection.Connect(po);
5509:                            foreach (Connection c in others) { names.Add(c.Options.Name); c.Disconnect(); }
5549:                            Connection conn = Connection.Connect(opts);
```

[A01]
```
$ awk 'NR>=10&&NR<=36{print NR": "$0}' nt8bridge/ntio.py
10: def nt8_root() -> Path:
11:     """NinjaTrader 8 user data dir. Override with NT8_DIR (used in tests)."""
12:     override = os.environ.get("NT8_DIR")
13:     if override:
14:         return Path(override)
15:     return Path.home() / "Documents" / "NinjaTrader 8"
16: 
17: 
18: def bridge_dir() -> Path:
19:     return nt8_root() / "NT8Bridge"
20: 
21: 
22: def ensure_bridge_dirs() -> tuple[Path, Path]:
23:     """Create <NT8>/NT8Bridge/{trigger,result} and return (trigger, result)."""
24:     trigger = bridge_dir() / "trigger"
25:     result = bridge_dir() / "result"
26:     trigger.mkdir(parents=True, exist_ok=True)
27:     result.mkdir(parents=True, exist_ok=True)
28:     return trigger, result
29: 
30: 
31: def atomic_write_json(target: Path, payload: dict) -> None:
32:     """Write JSON via temp-then-rename so readers never see a partial file."""
33:     target = Path(target)
34:     tmp = target.with_suffix(target.suffix + ".tmp")
35:     tmp.write_text(json.dumps(payload, indent=2), encoding="utf-8")
36:     os.replace(tmp, target)
```

[A02]
```
$ /usr/bin/grep -nE 'class [A-Za-z]+ : AddOnBase|public (static |partial )*class [A-Za-z]+' addon/AutoReconnect.cs addon/ChartDataSeriesSwitcher.cs addon/NT8BridgeServer.cs addon/NT8BridgeServerPlayback.cs | cut -c1-160
addon/AutoReconnect.cs:123:    public class AutoReconnect : AddOnBase
addon/ChartDataSeriesSwitcher.cs:31:    public static class ChartDataSeriesSwitcher
addon/ChartDataSeriesSwitcher.cs:35:        public class SwitchResult
addon/NT8BridgeServer.cs:36:    public partial class NT8BridgeServer : AddOnBase
addon/NT8BridgeServerPlayback.cs:61:    public partial class NT8BridgeServer
```

[A03]
```
$ /usr/bin/grep -nE 'HttpListener|TcpListener|UdpClient|IPAddress\.|NamedPipe|FileSystemWatcher|socket\.socket|http\.server|socketserver' addon/*.cs nt8bridge/*.py; echo "grep-exit=$?"
grep-exit=1
```

[A04]
```
$ awk 'NR>=103&&NR<=122{print NR": "$0}' addon/NT8BridgeServer.cs | cut -c1-200
103:         private void Init()
104:         {
105:             string root = Path.Combine(Globals.UserDataDir, "NT8Bridge");
106:             _triggerDir = Path.Combine(root, "trigger");
107:             _resultDir = Path.Combine(root, "result");
108:             Directory.CreateDirectory(_triggerDir);
109:             Directory.CreateDirectory(_resultDir);
110:             // Diagnostic heartbeat: proves the AddOn loaded and the poller started.
111:             WriteResult("heartbeat.json",
112:                 "{\"server\":\"NT8BridgeServer\",\"started\":" + JsonStr(Globals.Now.ToString("o")) + "}");
113:             // Output tee: the marker decides whether it records; subscribing is harmless when
114:             // it's off (the handler returns on a single volatile bool read).
115:             _outDir = Path.Combine(root, "output");
116:             _teeMarker = Path.Combine(_outDir, "tee.on");
117:             _teeOn = File.Exists(_teeMarker);
118:             try { NinjaTrader.Code.Output.OutputEvent += OnNtOutput; _teeSubscribed = true; }
119:             catch (Exception ex) { LogSafe("tee subscribe: " + ex.Message); }
120:             LogSafe("tee: Output 1/2 capture " + (_teeOn ? "ON" : "off (drop " + _teeMarker + " to enable)"));
121:             // Poll once per second on wall-clock time; never tick-time.
122:             _poller = new Timer(delegate { Poll(); }, null, 1000, 1000);
```

[A05]
```
$ awk 'NR>=130&&NR<=151{print NR": "$0}' addon/NT8BridgeServer.cs | cut -c1-200
130:         private void Poll()
131:         {
132:             TryBeat();   // UI-liveness heartbeat (runs regardless of the compile gate)
133:             TeeTick();   // Output 1/2 drain — OUTSIDE the gate, so a long compile can't stall it
134:             // Re-entrancy guard: skip this tick if the previous compile is still running.
135:             if (!Monitor.TryEnter(_gate)) return;
136:             try
137:             {
138:                 if (_triggerDir == null) return;
139:                 CheckLease();
140:                 SubscribePlaybackEvents();
141:                 // Subscribe from the poller, not from the first `botout` request:
142:                 // a line printed BEFORE the driver first asks would otherwise be
143:                 // lost, and a missing line is indistinguishable from a silent bot.
144:                 SubscribeBotOutput();
145:                 PruneResults();
146:                 foreach (string file in Directory.GetFiles(_triggerDir, "*.json"))
147:                     HandleTrigger(file);
148:             }
149:             catch (Exception ex) { LogSafe("Poll: " + ex.Message); }
150:             finally { Monitor.Exit(_gate); }
151:         }
```

[A06]
```
$ awk 'NR>=179&&NR<=213{print NR": "$0}' addon/NT8BridgeServer.cs | cut -c1-200
179:         private void HandleTrigger(string file)
180:         {
181:             string id = null;
182:             string kind = null;
183:             bool leaseHolder = false;   // did THIS request carry `leaseSec`? - see RearmLease
184:             try
185:             {
186:                 string text = File.ReadAllText(file);
187:                 DateTime writtenUtc;
188:                 try { writtenUtc = File.GetLastWriteTimeUtc(file); }
189:                 catch { writtenUtc = DateTime.UtcNow; }
190:                 try { File.Delete(file); } catch { }   // consume the trigger
191:                 id = ExtractJsonString(text, "id");
192:                 kind = ExtractJsonString(text, "kind");
193:                 leaseHolder = NoteLease(text);   // a leaseSec request: the driver is alive - push the deadline out
194: 
195:                 // A caller that has timed out is gone; running its command now acts on
196:                 // a state it never saw. Measured 2026-08-19: a backlog released after
197:                 // 11 minutes enabled, disabled and removed a strategy in the middle of
198:                 // a running measurement (see the file header).
199:                 double ageSec = (DateTime.UtcNow - writtenUtc).TotalSeconds;
200:                 double ttlSec = RequestTtlSec(text);
201:                 if (ageSec > ttlSec)
202:                 {
203:                     LogSafe("expired " + kind + " " + id + ": " + ageSec.ToString("0") +
204:                             "s old, ttl " + ttlSec.ToString("0") + "s - NOT executed");
205:                     WriteResult(ResultPrefixEx(kind, ResultPrefix(kind)) + id + ".json",
206:                         "{\"id\":" + JsonStr(id) + ",\"status\":\"expired\",\"executed\":false" +
207:                         ",\"ageSec\":" + ageSec.ToString("0.###", InvCi) +
208:                         ",\"ttlSec\":" + ttlSec.ToString("0.###", InvCi) +
209:                         ",\"errors\":[{\"code\":\"EXPIRED\",\"message\":" +
210:                         JsonStr("request waited " + ageSec.ToString("0") + "s in the queue, past its " +
211:                                 ttlSec.ToString("0") + "s TTL; not executed") + "}]}");
212:                     return;
213:                 }
```

[A07]
```
$ awk 'NR>=7669&&NR<=7697{print NR": "$0}' addon/NT8BridgeServerPlayback.cs | cut -c1-200
7669:         // How long a queued request stays valid, in seconds. `ttlSec` in the request
7670:         // wins so the long commands (backtest, downloads, compile) can outlive the
7671:         // default without weakening it for everything else.
7672:         private const double DefaultTtlSec = 300.0;
7673: 
7674:         // Reads a NUMBER, which ExtractJsonString cannot: that one takes the first
7675:         // '"' after the colon, and for `"ttlSec": 300` the next quote belongs to the
7676:         // FOLLOWING key. A quoted value is accepted as well.
7677:         private static double RequestTtlSec(string json)
7678:         {
7679:             if (json == null) return DefaultTtlSec;
7680:             const string pat = "\"ttlSec\"";
7681:             int i = json.IndexOf(pat, StringComparison.Ordinal);
7682:             if (i < 0) return DefaultTtlSec;
7683:             int c = json.IndexOf(':', i + pat.Length);
7684:             if (c < 0) return DefaultTtlSec;
7685:             int p = c + 1;
7686:             while (p < json.Length && (char.IsWhiteSpace(json[p]) || json[p] == '"')) p++;
7687:             int s = p;
7688:             while (p < json.Length && (char.IsDigit(json[p]) || json[p] == '.' ||
7689:                                        json[p] == '-' || json[p] == '+' ||
7690:                                        json[p] == 'e' || json[p] == 'E')) p++;
7691:             double v;
7692:             if (p > s && double.TryParse(json.Substring(s, p - s),
7693:                                          System.Globalization.NumberStyles.Float, InvCi, out v)
7694:                 && v > 0.0)
7695:                 return v;
7696:             return DefaultTtlSec;
7697:         }
```

[A08]
```
$ awk 'NR>=4529&&NR<=4540{print NR": "$0}' addon/NT8BridgeServer.cs | cut -c1-200
4529:         private void WriteResult(string name, string json)
4530:         {
4531:             try
4532:             {
4533:                 string dst = Path.Combine(_resultDir, name);
4534:                 string tmp = dst + ".tmp";
4535:                 File.WriteAllText(tmp, json);
4536:                 if (File.Exists(dst)) File.Delete(dst);
4537:                 File.Move(tmp, dst);   // atomic rename so Python never reads a partial file
4538:             }
4539:             catch (Exception ex) { LogSafe("WriteResult: " + ex.Message); }
4540:         }
```

[A09]
```
$ /usr/bin/grep -nE '^ +(else )?if \(kind == "' addon/NT8BridgeServer.cs | cut -c1-200
214:                if (kind == "compile")
216:                else if (kind == "reload")
218:                else if (kind == "windows")
220:                else if (kind == "backtest")
222:                else if (kind == "account")
224:                else if (kind == "flatten")
226:                else if (kind == "connections")
228:                else if (kind == "reconnect")
230:                else if (kind == "playback")
232:                else if (kind == "playbackrun")
234:                else if (kind == "ntstatus")
236:                else if (kind == "workspace")
238:                else if (kind == "strategies")
240:                else if (kind == "ghostorders")
242:                else if (kind == "screenshot")
244:                else if (kind == "peek")
246:                else if (kind == "probe")
248:                else if (kind == "configure")
250:                else if (kind == "satemplate")
252:                else if (kind == "analyzerrun")
254:                else if (kind == "feedhealth")
256:                else if (kind == "performance")
260:                else if (kind == "perfwindow")
264:                else if (kind == "chartseries")
266:                else if (kind == "marketReplayDump")
268:                else if (kind == "marketReplayDownload")
294:            if (kind == "account") return "account_";
295:            if (kind == "flatten") return "flatten_";
296:            if (kind == "backtest") return "backtest_";
297:            if (kind == "connections") return "connections_";
298:            if (kind == "reconnect") return "reconnect_";
299:            if (kind == "playback") return "playback_";
300:            if (kind == "ntstatus") return "ntstatus_";
301:            if (kind == "workspace") return "workspace_";
302:            if (kind == "strategies") return "strategies_";
303:            if (kind == "ghostorders") return "ghostorders_";
304:            if (kind == "screenshot") return "screenshot_";
305:            if (kind == "peek") return "peek_";
306:            if (kind == "probe") return "probe_";
307:            if (kind == "configure") return "configure_";
308:            if (kind == "feedhealth") return "feedhealth_";
309:            if (kind == "performance") return "perf_";
310:            if (kind == "perfwindow") return "perfwindow_";
311:            if (kind == "chartseries") return "chartseries_";
312:            if (kind == "reload") return "reload_";
313:            if (kind == "windows") return "windows_";
314:            if (kind == "marketReplayDump") return "marketReplayDump_";
315:            if (kind == "marketReplayDownload") return "marketReplayDownload_";
```

[A10]
```
$ /usr/bin/grep -niE 'hmac|secret|signature|apikey|api_key|FileSecurity|DirectorySecurity|AccessControl|WindowsIdentity' addon/NT8BridgeServer.cs addon/NT8BridgeServerPlayback.cs nt8bridge/ntio.py; echo "grep-exit=$?"
addon/NT8BridgeServerPlayback.cs:580:                // ResourceManager - the signature says so:
addon/NT8BridgeServerPlayback.cs:1371:                    // The handler signature has to match the event; both are
addon/NT8BridgeServerPlayback.cs:1401:        //  below do the same work with no UI at all. Their signatures were read back from the
addon/NT8BridgeServerPlayback.cs:7254:                // The common signature of NinjaTrader's order-rejection boxes is the
grep-exit=0
```

[A11]
```
$ awk '(NR>=3278&&NR<=3296)||(NR>=3325&&NR<=3337){print NR": "$0}' addon/NT8BridgeServer.cs | cut -c1-200
3278:         // --- Force-close: flatten an account's position(s) and cancel its working
3279:         // orders. Automated strategies do not always reliably close a stranded/naked
3280:         // position; this is the independent kill switch the `watch` watchdog calls when it
3281:         // sees an unprotected position. Account name is REQUIRED (refuses to
3282:         // flatten everything). Acts AFTER releasing the snapshot locks — Lesson
3283:         // #159: never call Account.Cancel/Flatten while holding a collection lock.
3284:         private string RunFlatten(string id, string accountFilter, string instrumentFilter)
3285:         {
3286:             try
3287:             {
3288:                 if (string.IsNullOrEmpty(accountFilter))
3289:                     return "{\"id\":" + JsonStr(id) + ",\"status\":\"error\",\"flattened\":[],\"errors\":[{" +
3290:                            "\"code\":\"BRIDGE\",\"message\":\"flatten requires an account name\"}]}";
3291: 
3292:                 Account acct = null;
3293:                 try { lock (Account.All) { foreach (Account a in Account.All) { if (a.Name == accountFilter) { acct = a; break; } } } } catch { }
3294:                 if (acct == null)
3295:                     return "{\"id\":" + JsonStr(id) + ",\"status\":\"error\",\"flattened\":[],\"errors\":[{" +
3296:                            "\"code\":\"BRIDGE\",\"message\":" + JsonStr("account not found: " + accountFilter) + "}]}";
3325:                 // act AFTER the locks are released (Lesson #159)
3326:                 int cancelled = 0;
3327:                 if (ordersToCancel.Count > 0) {
3328:                     try { acct.Cancel(ordersToCancel); cancelled = ordersToCancel.Count; }
3329:                     catch (Exception ex) { LogSafe("flatten cancel: " + ex.Message); }
3330:                 }
3331:                 bool flattenCalled = false;
3332:                 if (instrs.Count > 0) {
3333:                     try { acct.Flatten(instrs); flattenCalled = true; }
3334:                     catch (Exception ex) { LogSafe("flatten: " + ex.Message); }
3335:                 }
3336:                 LogSafe("FLATTEN account=" + accountFilter + " instrument='" + instrumentFilter +
3337:                         "' positions=" + instrs.Count + " ordersCancelled=" + cancelled);
```

[A12]
```
$ awk 'NR>=17&&NR<=34{print NR": "$0}' nt8bridge/flatten.py
17: 
18: def build_flatten_request(request_id: str, account: str, instrument: str = "") -> dict:
19:     return {"id": request_id, "kind": "flatten", "account": account, "instrument": instrument or ""}
20: 
21: 
22: def run_flatten(account: str, instrument: str = "", timeout: float = 20.0) -> dict:
23:     """Force-close `account` (optionally a single `instrument`). Returns the raw
24:     response payload. Requires an account name — refuses to flatten everything.
25:     """
26:     if not account:
27:         raise ValueError("flatten requires an account name")
28:     trigger, result = ntio.ensure_bridge_dirs()
29:     request_id = new_request_id()
30:     ntio.atomic_write_json(
31:         trigger / f"flatten_{request_id}.json",
32:         build_flatten_request(request_id, account, instrument),
33:     )
34:     return ntio.poll_for_json(result / f"flatten_{request_id}.json", timeout=timeout)
```

[A13]
```
$ awk '(NR>=1280&&NR<=1288)||(NR>=1348&&NR<=1356){print NR": "$0}' nt8bridge/cli.py | cut -c1-200
1280:     p_flat = sub.add_parser("flatten")
1281:     p_flat.add_argument("--name", required=True, help="account to flatten, e.g. Sim101 (REQUIRED)")
1282:     p_flat.add_argument("--instrument", default="", help="limit to one instrument, e.g. 'MNQ 06-26' (empty = all)")
1283:     p_flat.add_argument("--timeout", type=float, default=20.0)
1284:     p_watch = sub.add_parser("watch")
1285:     p_watch.add_argument("--name", action="append", required=True, help="account(s) to watch; repeatable")
1286:     p_watch.add_argument("--grace", type=float, default=20.0, help="seconds a position may stay naked before kill")
1287:     p_watch.add_argument("--interval", type=float, default=5.0, help="seconds between scans")
1288:     p_watch.add_argument("--once", action="store_true", help="single scan (no loop) — for testing")
1348:     p_recon = sub.add_parser("reconnect")
1349:     p_recon.add_argument("--name", required=True, help="connection name to reconnect (REQUIRED)")
1350:     p_recon.add_argument("--timeout", type=float, default=30.0)
1351:     p_cwatch = sub.add_parser("connwatch")
1352:     p_cwatch.add_argument("--name", action="append", required=True, help="connection(s) to guard; repeatable")
1353:     p_cwatch.add_argument("--grace", type=float, default=20.0, help="seconds a connection may stay dropped before reconnect")
1354:     p_cwatch.add_argument("--interval", type=float, default=10.0, help="seconds between scans")
1355:     p_cwatch.add_argument("--max-attempts", type=int, default=5, help="reconnect attempts before giving up (per drop)")
1356:     p_cwatch.add_argument("--once", action="store_true", help="single scan (no loop) — for testing")
```

[A14]
```
$ awk 'NR>=1157&&NR<=1175{print NR": "$0}' addon/NT8BridgeServer.cs | cut -c1-200
1157:                 if (doCancel)
1158:                 {
1159:                     string creason = null;
1160:                     if (string.IsNullOrEmpty(acctFilter)) creason = "cancel requires an explicit account name; it will never cancel across every account";
1161:                     else if (target == null)              creason = "account not found: " + acctFilter;
1162: 
1163:                     int attempted = cancelTargets.Count;
1164:                     int stillStalled = -1;
1165:                     var cancelledIds = new List<string>();
1166:                     if (creason == null && attempted > 0)
1167:                     {
1168:                         foreach (Order o in cancelTargets)
1169:                             cancelledIds.Add(JsonStrOrNull(SafeStr(delegate { return o.OrderId; })));
1170:                         try
1171:                         {
1172:                             LogSafe("GHOSTORDERS cancel account=" + acctFilter + " orders=" + attempted);
1173:                             target.Cancel(cancelTargets);          // acts AFTER the locks (Lesson #159)
1174:                         }
1175:                         catch (Exception ex) { creason = "Cancel threw: " + ex.Message; }
```

[A15]
```
$ awk 'NR>=1206&&NR<=1227{print NR": "$0}' addon/NT8BridgeServer.cs | cut -c1-200
1206:                 if (doReset)
1207:                 {
1208:                     string reason = null;
1209:                     if (string.IsNullOrEmpty(acctFilter)) reason = "reset requires an explicit account name; it will never reset every account";
1210:                     else if (target == null)              reason = "account not found: " + acctFilter;
1211:                     else
1212:                     {
1213:                         bool isSim = false;
1214:                         try { isSim = (target.Provider == Provider.Simulator); } catch { }
1215:                         // ALLOWLIST. Unknown provider => refuse.
1216:                         if (!isSim) reason = "'" + acctFilter + "' is provider '" + SafeStr(delegate { return target.Provider.ToString(); })
1217:                                            + "', not Simulator — refusing. ResetSimulationAccount is for simulation accounts only.";
1218:                     }
1219: 
1220:                     bool performed = false;
1221:                     if (reason == null)
1222:                     {
1223:                         try
1224:                         {
1225:                             LogSafe("GHOSTORDERS reset account=" + acctFilter + " clearTradeData=" + clearTrades);
1226:                             target.ResetSimulationAccount(clearTrades);
1227:                             performed = true;
```

[A16]
```
$ awk '(NR>=1351&&NR<=1354)||(NR>=1406&&NR<=1424){print NR": "$0}' addon/NT8BridgeServer.cs | cut -c1-200
1351:                 List<string> wantOn = SplitNames(ExtractJsonString(text, "enable"));
1352:                 List<string> wantOff = SplitNames(ExtractJsonString(text, "disable"));
1353:                 bool dryRun = JsonBoolFlag(text, "dryRun");
1354:                 bool force = JsonBoolFlag(text, "force");
1406:                     if (!on && !force)
1407:                     {
1408:                         // Disabling a strategy does NOT flatten what it is holding — it stops managing it.
1409:                         // An open position or a working order left with nobody minding it is the one
1410:                         // outcome this verb must never cause by accident, so it is opt-in via force.
1411:                         string why = ExposureGuard(row);
1412:                         if (why != null) { skipped.Add(SkipJson(name, "exposure", why + " — pass force to disable anyway")); continue; }
1413:                     }
1414:                     toClick.Add(name);
1415:                 }
1416: 
1417:                 if (toClick.Count > 0 && !dryRun)
1418:                 {
1419:                     // PHASE 3 — click, back on the Control Center's dispatcher.
1420:                     var clicked = WithStrategiesGrid<List<string>>(delegate(object grid)
1421:                     {
1422:                         var okd = new List<string>();
1423:                         foreach (string name in toClick)
1424:                             if (ClickEnabledCheckbox(grid, name, wantOn.Contains(name), notes)) okd.Add(name);
```

[A17]
```
$ awk 'NR>=4408&&NR<=4439{print NR": "$0}' addon/NT8BridgeServer.cs | cut -c1-200
4408:         // Reconnect a configured connection by name via Connection.Connect(savedOptions),
4409:         // marshalled to the UI dispatcher (the spike-proven safe path). UNCONDITIONAL —
4410:         // an explicit reconnect is an operator override; the inadvertent-only POLICY lives
4411:         // in the Python guardian, not here. No-op (reports wasConnected) if already up.
4412:         private string RunReconnect(string id, string nameArg)
4413:         {
4414:             try
4415:             {
4416:                 if (string.IsNullOrEmpty(nameArg))
4417:                     return "{\"id\":" + JsonStr(id) + ",\"status\":\"error\",\"errors\":[{" +
4418:                            "\"code\":\"BRIDGE\",\"message\":\"reconnect requires a connection name\"}]}";
4419: 
4420:                 var live = new List<Connection>();
4421:                 try { lock (Connection.Connections) { foreach (Connection c in Connection.Connections) live.Add(c); } } catch { }
4422:                 bool wasConnected = LiveStatusOf(live, nameArg) == "Connected";
4423: 
4424:                 ConnectOptions opt = null;
4425:                 var cfg = new List<ConnectOptions>();
4426:                 try { lock (Globals.ConnectOptions) { foreach (ConnectOptions o in Globals.ConnectOptions) cfg.Add(o); } } catch { }
4427:                 foreach (ConnectOptions o in cfg)
4428:                     if (SafeStr(delegate { return o.Name; }) == nameArg) { opt = o; break; }
4429:                 if (opt == null)
4430:                     return "{\"id\":" + JsonStr(id) + ",\"status\":\"error\",\"errors\":[{" +
4431:                            "\"code\":\"BRIDGE\",\"message\":" + JsonStr("connection not configured: " + nameArg) + "}]}";
4432: 
4433:                 bool attempted = false, threw = false, timedOut = false; string err = "";
4434:                 if (!wasConnected)
4435:                 {
4436:                     Exception cap = null;
4437:                     bool ran = false;
4438:                     ConnectOptions o2 = opt;
4439:                     Action act = delegate { ran = true; try { Connection.Connect(o2); } catch (Exception ex) { cap = ex; } };
```

[A18]
```
$ awk '(NR>=1&&NR<=12)||NR==820||NR==1532{print NR": "$0}' addon/AutoReconnect.cs | cut -c1-200
1: // AutoReconnect.cs — NinjaTrader 8 AddOn: auto-reconnect dropped connections + ALERT on dead feeds.
2: //
3: // DROP-IN: copy this file into  Documents\NinjaTrader 8\bin\Custom\AddOns\  and compile once
4: // (NinjaScript Editor -> F5). From then on, every NT8 session it watches your connections.
5: // No Python; config optional.
6: //
7: // WHAT IT DOES — two distinct behaviors, split so RUNNING STRATEGIES ARE NEVER KILLED:
8: //   * RECONNECT — only when NinjaTrader itself declares the LINK lost (Status == ConnectionLost).
9: //     After a grace period (NT8's own retry gets first crack) it re-issues
10: //     Connection.Connect(savedOptions) on the UI thread, with exponential backoff, a max-attempts
11: //     cap, then a cooldown. This is the long-standing v1 behavior. Config "reconnect": false makes it
12: //     ALERT-ONLY instead (NT8 Guard's Watch only preset).
820:             Action act = delegate { try { Connection.Connect(o2); } catch (Exception ex) { LogSafe("reconnect Connect(" + name + "): " + ex.Message); } };
1532:             Action act = delegate { try { c2.Disconnect(); LogSafe("recover: Disconnect() fired on " + DescribeConn(c2)); } catch (Exception ex) { LogSafe("recover disconnect(" + name + "): " + 
```

[A19]
```
$ awk '(NR>=4874&&NR<=4883)||(NR>=5494&&NR<=5509)||NR==5549{print NR": "$0}' addon/NT8BridgeServerPlayback.cs | cut -c1-200
4874:                     if (!checkOnly && string.Equals(require, "playback", StringComparison.OrdinalIgnoreCase))
4875:                     {
4876:                         // Playback refuses to connect while anything else is up, and says
4877:                         // so in a modal dialog that also blocks the dispatcher.
4878:                         if (live.Count > 0)
4879:                         {
4880:                             foreach (Connection c in Connection.Connections)
4881:                                 if (c != null && c.Options != null && c.Options.Provider != Provider.Playback
4882:                                     && c.Status != ConnectionStatus.Disconnected)
4883:                                     try { c.Disconnect(); } catch { }
5494:                     // Playback refuses to connect while anything else is connected and
5495:                     // says so in a MODAL dialog — which also blocks the dispatcher, so
5496:                     // the bridge stops answering entirely. Disconnect first, and prove
5497:                     // it by status rather than by the call returning.
5498:                     try
5499:                     {
5500:                         List<Connection> others = new List<Connection>();
5501:                         foreach (Connection c in Connection.Connections)
5502:                             if (c != null && c.Options != null && c.Options.Provider != Provider.Playback
5503:                                 && c.Status != ConnectionStatus.Disconnected)
5504:                                 others.Add(c);
5505:                         if (others.Count == 0) step("disconnect others", true, "nothing connected");
5506:                         else
5507:                         {
5508:                             List<string> names = new List<string>();
5509:                             foreach (Connection c in others) { names.Add(c.Options.Name); c.Disconnect(); }
5549:                             Connection conn = Connection.Connect(opts);
```

[A21]
```
$ awk 'NR>=5243&&NR<=5254{print NR": "$0}' addon/NT8BridgeServerPlayback.cs | cut -c1-200
5243:                     // 2. TRIGGER on every one that is not already down
5244:                     int markOff = NtLogCount();
5245:                     List<string> hit = new List<string>();
5246:                     foreach (Connection c in open)
5247:                     {
5248:                         string nm = "?";
5249:                         try { nm = c.Options == null ? "<no options>" : c.Options.Name; } catch { }
5250:                         hit.Add(nm);
5251:                         try { c.Disconnect(); }
5252:                         catch (Exception ex) { step("disconnect " + nm, false, Deep(ex)); }
5253:                     }
5254:                     step("triggered", true, "Disconnect() on " + string.Join(", ", hit.ToArray()));
```

[A23]
```
$ awk 'FILENAME~/Server\.cs$/&&FNR>=2632&&FNR<=3176&&/Connection|Connect\(/{print FILENAME":"FNR": "$0} FILENAME~/Playback\.cs$/&&FNR>=1677&&FNR<=2352&&/Connection|Connect\(/{print FILENAME":"FNR": "$0} END{print "END-of-scan"}' addon/NT8BridgeServer.cs addon/NT8BridgeServerPlayback.cs | cut -c1-200
END-of-scan
```

[A24]
```
$ /usr/bin/grep -nE 'File\.(Copy|Delete|WriteAll|AppendAll|Move)|Directory\.Delete|new FileStream\(|Registry' addon/NT8BridgeServer.cs addon/NT8BridgeServerPlayback.cs | cut -c1-190
addon/NT8BridgeServer.cs:190:                try { File.Delete(file); } catch { }   // consume the trigger
addon/NT8BridgeServer.cs:743:                using (var fs = new FileStream(outPath, FileMode.Create, FileAccess.Write))
addon/NT8BridgeServer.cs:4535:                File.WriteAllText(tmp, json);
addon/NT8BridgeServer.cs:4536:                if (File.Exists(dst)) File.Delete(dst);
addon/NT8BridgeServer.cs:4537:                File.Move(tmp, dst);   // atomic rename so Python never reads a partial file
addon/NT8BridgeServer.cs:4646:                    File.AppendAllText(path, kv.Value.ToString());
addon/NT8BridgeServer.cs:4674:                if (File.Exists(prev)) File.Delete(prev);
addon/NT8BridgeServer.cs:4675:                File.Move(path, prev);
addon/NT8BridgeServer.cs:4760:                File.AppendAllText(Path.Combine(dir, "bridge.log"),
addon/NT8BridgeServerPlayback.cs:470:                File.AppendAllText(Path.Combine(dir, "bridge.log"),
addon/NT8BridgeServerPlayback.cs:562:                    File.AppendAllText(_ntLogFile,
addon/NT8BridgeServerPlayback.cs:630:                    File.AppendAllText(_ntLogFile, line + Environment.NewLine);
addon/NT8BridgeServerPlayback.cs:6791:                File.AppendAllText(Path.Combine(_resultDir, "playbackrun_" + id + ".progress.txt"),
addon/NT8BridgeServerPlayback.cs:7722:                        File.Delete(f);
addon/NT8BridgeServerPlayback.cs:7734:                        File.Delete(f);
```

[A25]
```
$ awk '(NR>=646&&NR<=652)||(NR>=740&&NR<=745){print NR": "$0}' addon/NT8BridgeServer.cs | cut -c1-200
646:             string title = ExtractJsonString(triggerJson, "title");
647:             string hwndStr = ExtractJsonString(triggerJson, "hwnd");
648:             string outPath = ExtractJsonString(triggerJson, "out");
649: 
650:             try { SetProcessDPIAware(); } catch { }
651: 
652:             IntPtr target = IntPtr.Zero;
740: 
741:                 string dir = Path.GetDirectoryName(outPath);
742:                 if (!string.IsNullOrEmpty(dir) && !Directory.Exists(dir)) Directory.CreateDirectory(dir);
743:                 using (var fs = new FileStream(outPath, FileMode.Create, FileAccess.Write))
744:                     enc.Save(fs);
745: 
```

[A28]
```
$ awk 'NR>=1&&NR<=25{print NR": "$0}' nt8bridge/deploy.py | cut -c1-200
1: """Atomic deploy of a .cs into the correct NT8 bin/Custom subfolder."""
2: from __future__ import annotations
3: 
4: import os
5: from pathlib import Path
6: 
7: from nt8bridge import ntio
8: 
9: _SUBFOLDER = {"strategy": "Strategies", "indicator": "Indicators", "addon": "AddOns"}
10: 
11: 
12: def dest_for(name: str, kind: str) -> Path:
13:     if kind not in _SUBFOLDER:
14:         raise ValueError(f"Unknown kind '{kind}'; expected one of {list(_SUBFOLDER)}")
15:     return ntio.nt8_root() / "bin" / "Custom" / _SUBFOLDER[kind] / name
16: 
17: 
18: def deploy(src, kind: str) -> Path:
19:     src = Path(src)
20:     dest = dest_for(src.name, kind)
21:     dest.parent.mkdir(parents=True, exist_ok=True)
22:     tmp = dest.with_suffix(dest.suffix + ".tmp")
23:     tmp.write_bytes(src.read_bytes())
24:     os.replace(tmp, dest)
25:     return dest
```

[A30]
```
$ awk 'NR>=130&&NR<=142{print NR": "$0}' nt8bridge/restart.py | cut -c1-200
130:     """
131:     if not is_running():
132:         return True, "not running"
133:     try:
134:         subprocess.run(["taskkill", "/IM", "NinjaTrader.exe"],
135:                        capture_output=True, text=True, errors="replace", timeout=30)
136:     except Exception as e:  # noqa: BLE001 - reported, not swallowed
137:         return False, f"graceful close failed to dispatch: {e}"
138:     if wait_for(False, force_after):
139:         return True, "closed gracefully"
140:     try:
141:         subprocess.run(["taskkill", "/F", "/IM", "NinjaTrader.exe"],
142:                        capture_output=True, text=True, errors="replace", timeout=30)
```

[A31]
```
$ /usr/bin/grep -nE 'Path\.Combine\(Globals\.UserDataDir' addon/AutoReconnect.cs addon/NT8BridgeServer.cs addon/NT8BridgeServerPlayback.cs | cut -c1-200
addon/AutoReconnect.cs:326:            _logPath = Path.Combine(Globals.UserDataDir, "AutoReconnect.log");
addon/AutoReconnect.cs:794:                string path = Path.Combine(Globals.UserDataDir, "AutoReconnect.heartbeat.json");
addon/AutoReconnect.cs:1189:                string stallPath = Path.Combine(Globals.UserDataDir, "AutoReconnect.stall");
addon/AutoReconnect.cs:1191:                string deafPath = Path.Combine(Globals.UserDataDir, "AutoReconnect.deafen");
addon/AutoReconnect.cs:1193:                string reloadPath = Path.Combine(Globals.UserDataDir, "AutoReconnect.reload");
addon/AutoReconnect.cs:2033:                string dir = Path.Combine(Globals.UserDataDir, "NT8Guard");
addon/AutoReconnect.cs:2107:                string path = Path.Combine(Globals.UserDataDir, "AutoReconnect.config.json");
addon/NT8BridgeServer.cs:105:            string root = Path.Combine(Globals.UserDataDir, "NT8Bridge");
addon/NT8BridgeServer.cs:447:                string root = Path.Combine(Globals.UserDataDir, "db", "replay");
addon/NT8BridgeServer.cs:565:                    string custDir = Path.Combine(Globals.UserDataDir, "bin", "Custom");
addon/NT8BridgeServer.cs:574:                string dllOnDisk = Path.Combine(Globals.UserDataDir, "bin", "Custom", "NinjaTrader.Custom.dll");
addon/NT8BridgeServer.cs:715:                outPath = Path.Combine(Globals.UserDataDir, "NT8Bridge", "result", "shot_" + id + ".png");
addon/NT8BridgeServer.cs:2148:                string nrdPath = System.IO.Path.Combine(Globals.UserDataDir, "db", "replay",
addon/NT8BridgeServerPlayback.cs:559:                    string dir0 = Path.Combine(Globals.UserDataDir, "NT8Bridge");
addon/NT8BridgeServerPlayback.cs:626:                        string dir = Path.Combine(Globals.UserDataDir, "NT8Bridge");
addon/NT8BridgeServerPlayback.cs:1576:                string dir = Path.Combine(Globals.UserDataDir, "db", "replay", instrument);
addon/NT8BridgeServerPlayback.cs:1616:                string dir = Path.Combine(Globals.UserDataDir, "db", "tick", instrument);
addon/NT8BridgeServerPlayback.cs:3512:                             ? ("ON - " + Path.Combine(Globals.UserDataDir, "NT8Bridge", "ntlog.txt")
```

[A32]
```
$ /usr/bin/grep -nE 'add_parser\(' nt8bridge/cli.py | cut -c1-130
1133:    sub.add_parser("doctor")
1134:    p_pre = sub.add_parser("precheck")
1136:    p_dep = sub.add_parser("deploy")
1146:    p_com = sub.add_parser("compile")
1157:    p_rel = sub.add_parser("reload", help="compile AND load it (what F5 does) — DISRUPTIVE")
1159:    p_win = sub.add_parser("windows", help="inventory NT's top-level windows")
1162:    p_reg = sub.add_parser("regions", help="find/strip DUPLICATED NinjaScript generated regions")
1167:    p_rst = sub.add_parser("restart", help="restart NinjaTrader (required after reload before a bake)")
1180:    p_bt = sub.add_parser("backtest")
1189:    p_pr = sub.add_parser(
1226:    p_acct = sub.add_parser("account")
1229:    p_perf = sub.add_parser("performance")
1236:    p_pw = sub.add_parser("perfwindow")
1242:    p_peek = sub.add_parser("peek")
1244:    p_probe = sub.add_parser("probe")
1246:    p_conf = sub.add_parser("configure")
1249:    p_satpl = sub.add_parser("satemplate")
1262:        p_ar = sub.add_parser(_cmd, allow_abbrev=False,
1280:    p_flat = sub.add_parser("flatten")
1284:    p_watch = sub.add_parser("watch")
1289:    p_conns = sub.add_parser("connections")
1291:    p_pb = sub.add_parser("playback", help="replay transport state: clock, MOVING?, speed, "
1304:    p_nts = sub.add_parser("ntstatus", help="is NT running the code on disk? exit 2 if the DLL is newer")
1306:    p_shot = sub.add_parser("screenshot", help="capture a window (or the whole screen) as PNG")
1311:    p_ws = sub.add_parser("workspace", help="charts, indicators, strategies + enabled state")
1314:    p_strat = sub.add_parser(
1330:    p_ghost = sub.add_parser(
1348:    p_recon = sub.add_parser("reconnect")
1351:    p_cwatch = sub.add_parser("connwatch")
1357:    p_fh = sub.add_parser("feedhealth")
1361:    p_fw = sub.add_parser("feedwatch")
1368:    p_out = sub.add_parser("output", help="read NT8's Output 1/2 (Print) — tail, follow, grep")
1377:    p_batch = sub.add_parser("batch")
1381:    p_sweep = sub.add_parser("sweep")
1388:    p_wd = sub.add_parser("watchdog")
1392:    p_cs = sub.add_parser("chartseries")
1403:    p_hd = sub.add_parser("histdump")
1416:    p_hg = sub.add_parser("histget")
```

[A33]
```
$ awk 'NR>=70&&NR<=89{print NR": "$0}' nt8bridge/analyzerrun.py | cut -c1-200
70:              "errors": [{code, message}]}
71: """
72: from __future__ import annotations
73: 
74: import re
75: import shutil
76: from pathlib import Path
77: 
78: from nt8bridge import ntio
79: from nt8bridge.compile import new_request_id
80: 
81: # CLI command -> the value the AddOn writes to StrategyAnalyzerTabProperties.BacktestType
82: # (enum StrategyAnalyzerGuiBacktestType: Backtest, Optimize, WalkForward,
83: # WalkForwardAnchored, MultiObjective, AiGenerate - read off NinjaTrader.Gui 8.1.8.2).
84: MODES = {
85:     "optimize": "Optimize",
86:     "walkforward": "WalkForward",
87:     "multiobjective": "MultiObjective",
88: }
89: COMMANDS = tuple(MODES)
```

[B01]
```
$ awk 'NR>=1638&&NR<=1664{print NR": "$0}' addon/NT8BridgeServerPlayback.cs | cut -c1-220
1638:         // ── analyzerrun: optimize / walkforward / multiobjective ─────────────
1639:         //  NinjaTrader's own parameter search, started on the Strategy Analyzer
1640:         //  tab the way the Run button starts it. One request kind serves the
1641:         //  three CLI commands; the tab's BacktestType decides which run NinjaTrader
1642:         //  performs (enum StrategyAnalyzerGuiBacktestType: Backtest, Optimize,
1643:         //  WalkForward, WalkForwardAnchored, MultiObjective, AiGenerate - read off
1644:         //  NinjaTrader.Gui 8.1.8.2).
1645:         //
1646:         //  What the run needs, each item measured on 8.1.8.2:
1647:         //   * the template on the tab (same steps as `satemplate`, so a run is
1648:         //     asked for by FILE and cannot drift from what the GUI runs);
1649:         //   * the property overrides from `params` written to that template
1650:         //     (OptimizationPeriod / TestPeriod are the walk-forward window lengths
1651:         //     in days);
1652:         //   * OptimizationParameters filled from `opt` ("Name:min:max:step[,...]")
1653:         //     as NinjaTrader's own Parameter objects - the collection the GUI's
1654:         //     parameter grid fills. With the type set and this collection empty the
1655:         //     Run button shows "The strategy must have at least one parameter to
1656:         //     optimize." and runs nothing (measured 08.09.2026, walk-forward on a
1657:         //     template without ranges);
1658:         //   * an Optimizer instance on the template (default | genetic) and, when
1659:         //     asked for, an OptimizationFitness by class name;
1660:         //   * the strategy's Category set to the run mode - what a GUI-less host
1661:         //     had to set itself before its walk-forward applied the in-sample
1662:         //     optimization; set here too, so both kinds of host run the same
1663:         //     template state whatever the GUI's own Run handler does with it;
1664:         //   * BacktestType on TabStrategyProperties, then RunCommand.
```

[B02]
```
$ awk 'NR>=1677&&NR<=1695{print NR": "$0}' addon/NT8BridgeServerPlayback.cs | cut -c1-220
1677:         private void RunAnalyzerRun(string id, string text)
1678:         {
1679:             string mode      = JsonUnescape(ExtractJsonString(text, "mode"));
1680:             string want      = JsonUnescape(ExtractJsonString(text, "template"));
1681:             string optSpec   = JsonUnescape(ExtractJsonString(text, "opt"));
1682:             string optimizer = JsonUnescape(ExtractJsonString(text, "optimizer"));
1683:             string fitness   = JsonUnescape(ExtractJsonString(text, "fitness"));
1684:             double timeoutSec = JsonNumberField(text, "timeoutSec", 1800.0);
1685:             Dictionary<string, string> prms = ParseParams(text);
1686:             string resultFile = "analyzerrun_" + id + ".json";
1687:             if (string.IsNullOrWhiteSpace(mode))
1688:             { WriteResult(resultFile, BtErr(id, "analyzerrun: no mode given")); return; }
1689:             if (string.IsNullOrWhiteSpace(want))
1690:             { WriteResult(resultFile, BtErr(id, "analyzerrun: no template given")); return; }
1691:             if (string.IsNullOrWhiteSpace(optSpec))
1692:             { WriteResult(resultFile, BtErr(id, "analyzerrun: " + mode + " needs opt=Name:min:max:step[,...]")); return; }
1693:             Window saWin = FindStrategyAnalyzerWindow();
1694:             if (saWin == null)
1695:             { WriteResult(resultFile, BtErr(id, "analyzerrun: no Strategy Analyzer window open")); return; }
```

[B03]
```
$ awk 'NR>=1706&&NR<=1724{print NR": "$0}' addon/NT8BridgeServerPlayback.cs | cut -c1-220
1706:                     // 1. The template, exactly as satemplate puts it there.
1707:                     StrategyBase before = tsp.StrategyTemplate;
1708:                     string file = TemplatePath(before, want);
1709:                     if (string.IsNullOrEmpty(file))
1710:                     { WriteResult(resultFile, BtErr(id, "analyzerrun: cannot resolve template " + want)); return; }
1711:                     string problem;
1712:                     StrategyBase strat = RestoreTemplate(file, out problem);
1713:                     if (strat == null) { WriteResult(resultFile, BtErr(id, "analyzerrun: " + problem)); return; }
1714:                     string had = before != null ? before.GetType().FullName : "(none)";
1715:                     if (!string.Equals(strat.GetType().FullName, had, StringComparison.Ordinal))
1716:                         tsp.Strategy = strat.GetType().Name;
1717:                     tsp.StrategyTemplate = strat;
1718:                     if (!string.IsNullOrWhiteSpace(strat.InstrumentOrInstrumentList))
1719:                         tsp.InstrumentOrInstrumentList = strat.InstrumentOrInstrumentList;
1720:                     if (!ReferenceEquals(tsp.StrategyTemplate, strat))
1721:                     { WriteResult(resultFile, BtErr(id, "analyzerrun: the tab kept its previous StrategyTemplate instance")); return; }
1722: 
1723:                     // 2. Property overrides (--Name=value), after the template.
1724:                     if (prms.Count > 0) InjectParams(strat, prms);
```

[B04]
```
$ awk 'NR>=1769&&NR<=1783{print NR": "$0}' addon/NT8BridgeServerPlayback.cs | cut -c1-220
1769:                     // 4. The optimizer. Exactly default | genetic; anything else is
1770:                     //    refused rather than silently run as the default.
1771:                     string optName = string.IsNullOrWhiteSpace(optimizer) ? "default" : optimizer.Trim().ToLowerInvariant();
1772:                     if (optName != "default" && optName != "genetic")
1773:                     { WriteResult(resultFile, BtErr(id, "analyzerrun: --optimizer=" + optName + " is not a known optimizer. Valid: default | genetic.")); return; }
1774:                     string optTypeName = optName == "genetic"
1775:                         ? "NinjaTrader.NinjaScript.Optimizers.GeneticOptimizer"
1776:                         : "NinjaTrader.NinjaScript.Optimizers.DefaultOptimizer";
1777:                     Type optType = NewestLoadedType(optTypeName);
1778:                     if (optType == null)
1779:                     { WriteResult(resultFile, BtErr(id, "analyzerrun: optimizer type not found: " + optTypeName)); return; }
1780:                     NinjaTrader.NinjaScript.Optimizers.Optimizer opt =
1781:                         (NinjaTrader.NinjaScript.Optimizers.Optimizer)Activator.CreateInstance(optType);
1782:                     opt.SetState(NinjaTrader.NinjaScript.State.SetDefaults);
1783:                     strat.Optimizer = opt;
```

[B05]
```
$ awk 'NR>=1822&&NR<=1834{print NR": "$0}' addon/NT8BridgeServerPlayback.cs | cut -c1-220
1822:                     // 6. Category and the tab's run type.
1823:                     NinjaTrader.NinjaScript.Category cat;
1824:                     StrategyAnalyzerGuiBacktestType bt;
1825:                     try
1826:                     {
1827:                         cat = (NinjaTrader.NinjaScript.Category)Enum.Parse(typeof(NinjaTrader.NinjaScript.Category), mode, true);
1828:                         bt  = (StrategyAnalyzerGuiBacktestType)Enum.Parse(typeof(StrategyAnalyzerGuiBacktestType), mode, true);
1829:                     }
1830:                     catch (Exception)
1831:                     { WriteResult(resultFile, BtErr(id, "analyzerrun: mode '" + mode + "' is not Optimize | WalkForward | WalkForwardAnchored | MultiObjective")); return; }
1832:                     strat.Category = cat;
1833:                     tsp.BacktestType = bt;
1834: 
```

[B06]
```
$ awk 'NR>=1849&&NR<=1873{print NR": "$0}' addon/NT8BridgeServerPlayback.cs | cut -c1-220
1849:                     RoutedCommand rc = StrategyAnalyzerViewModel.RunCommand as RoutedCommand;
1850:                     if (rc == null) { WriteResult(resultFile, BtErr(id, "analyzerrun: RunCommand is not a RoutedCommand")); return; }
1851:                     if (!rc.CanExecute(null, saWin))
1852:                     { WriteResult(resultFile, BtErr(id, "analyzerrun: RunCommand.CanExecute=false - the tab is not ready to run")); return; }
1853:                     string head = "\"mode\":" + JsonStr(mode)
1854:                         + ",\"backtestType\":" + JsonStr(tsp.BacktestType.ToString())
1855:                         + ",\"category\":" + JsonStr(strat.Category.ToString())
1856:                         + ",\"template\":" + JsonStr(file)
1857:                         + ",\"strategy\":" + JsonStr(strat.GetType().FullName)
1858:                         + ",\"instrument\":" + JsonStr(tsp.InstrumentOrInstrumentList)
1859:                         + ",\"from\":" + JsonStr(strat.From.ToString("yyyy-MM-dd"))
1860:                         + ",\"to\":" + JsonStr(strat.To.ToString("yyyy-MM-dd"))
1861:                         + ",\"optimizationPeriod\":" + strat.OptimizationPeriod
1862:                         + ",\"testPeriod\":" + strat.TestPeriod
1863:                         + ",\"parameters\":" + parJson.ToString()
1864:                         + ",\"optimizer\":" + JsonStr(optType.Name)
1865:                         + ",\"fitness\":" + JsonStr(fitUsed)
1866:                         + ",\"combinations\":" + combos
1867:                         + ",\"logDir\":" + JsonStr(logDir)
1868:                         + ",\"logFilePrefix\":" + JsonStr(csvPrefix ?? "");
1869:                     LogSafe("analyzerrun: " + mode + " " + Path.GetFileName(file) + " opt=" + optSpec
1870:                         + " optimizer=" + optType.Name + " combinations=" + combos + " -> RunCommand");
1871:                     DateTime started = DateTime.UtcNow;
1872:                     rc.Execute(null, saWin);
1873:                     StartAnalyzerRunPoll(id, resultFile, saWin, head, optNames, gridBefore, logDir, csvPrefix, csvBefore, started, timeoutSec);
```

[B07]
```
$ awk 'NR>=2017&&NR<=2036{print NR": "$0}' addon/NT8BridgeServerPlayback.cs | cut -c1-220
2017:             sb.Append("{\"id\":").Append(JsonStr(id)).Append(",\"status\":\"ok\",").Append(head);
2018:             sb.Append(",\"elapsedSec\":").Append(Num(elapsedSec));
2019:             sb.Append(",\"rows\":[");
2020:             bool first = true;
2021:             foreach (StrategyAnalyzerGridEntry e in unique)
2022:             {
2023:                 if (!first) sb.Append(",");
2024:                 first = false;
2025:                 sb.Append("{\"guid\":").Append(JsonStr(e.Guid))
2026:                   .Append(",\"parentGuid\":").Append(JsonStr(e.ParentGuid))
2027:                   .Append(",\"isSummary\":").Append(e.IsWalkForwardSummaryRow ? "true" : "false")
2028:                   .Append(",\"isParetoDetails\":").Append(e.IsParetoDetails ? "true" : "false")
2029:                   .Append(",\"isParetoPlaceholder\":").Append(e.IsParetoPlaceholder ? "true" : "false")
2030:                   .Append(",\"category\":").Append(JsonStr(e.Action.ToString()))
2031:                   .Append(",\"strategy\":").Append(JsonStr(e.StrategyName))
2032:                   .Append(",\"instrument\":").Append(JsonStr(e.Instrument))
2033:                   .Append(",\"from\":").Append(JsonStr(e.From.ToString("yyyy-MM-dd HH:mm:ss")))
2034:                   .Append(",\"to\":").Append(JsonStr(e.To.ToString("yyyy-MM-dd HH:mm:ss")))
2035:                   .Append(",\"parametersString\":").Append(JsonStr(e.ParametersString))
2036:                   .Append(",\"optimizerType\":").Append(JsonStr(e.OptimizerType));
```

[B08]
```
$ awk 'NR>=2123&&NR<=2127{print NR": "$0} NR>=2156&&NR<=2173{print NR": "$0}' addon/NT8BridgeServerPlayback.cs | cut -c1-220
2123:                 sb.Append(",\"children\":").Append(e.Children != null ? e.Children.Count : 0);
2124:                 sb.Append("}");
2125:             }
2126:             sb.Append("]");
2127:             sb.Append(",\"windows\":").Append(windows).Append(",\"rankedWindows\":").Append(ranked);
2156:         private static string PerfSummaryJson(SystemPerformance perf)
2157:         {
2158:             if (perf == null) return "null";
2159:             var sb = new StringBuilder("{");
2160:             TradeCollection all = perf.AllTrades;
2161:             sb.Append("\"totalTrades\":").Append(all != null ? all.Count : 0);
2162:             if (all != null && all.TradesPerformance != null)
2163:             {
2164:                 TradesPerformance tp = all.TradesPerformance;
2165:                 sb.Append(",\"profitFactor\":").Append(Num(tp.ProfitFactor));
2166:                 if (tp.Currency != null)
2167:                 {
2168:                     sb.Append(",\"netProfit\":").Append(Num(tp.Currency.CumProfit));
2169:                     sb.Append(",\"maxDrawdown\":").Append(Num(tp.Currency.Drawdown));
2170:                 }
2171:             }
2172:             sb.Append(",\"performanceValue\":").Append(Num(perf.PerformanceValue));
2173:             sb.Append("}");
```

[B09]
```
$ awk 'NR>=1425&&NR<=1447{print NR": "$0}' addon/NT8BridgeServerPlayback.cs | cut -c1-220
1425:         private static Type TemplateType()
1426:         {
1427:             foreach (Assembly asm in AppDomain.CurrentDomain.GetAssemblies())
1428:             {
1429:                 Type ty = null;
1430:                 try { ty = asm.GetType("NinjaTrader.Gui.NinjaScript.StrategyTemplate", false); }
1431:                 catch { }
1432:                 if (ty != null) return ty;
1433:             }
1434:             return null;
1435:         }
1436: 
1437:         // The folder is asked of NinjaTrader, never assembled from a naming rule: it differs
1438:         // per bot (flat "Strategy\Foo" vs nested "Strategy\Foo.Foo") and NT8 creates it when
1439:         // the strategy first appears.
1440:         private static string TemplateFolder(StrategyBase strat)
1441:         {
1442:             Type tt = TemplateType();
1443:             if (tt == null || strat == null) return null;
1444:             MethodInfo mi = tt.GetMethod("GetTemplateFolder",
1445:                 BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
1446:             if (mi == null) return null;
1447:             try { return (string)mi.Invoke(null, new object[] { strat }); }
```

[B10]
```
$ awk 'NR>=1519&&NR<=1541{print NR": "$0}' addon/NT8BridgeServerPlayback.cs | cut -c1-220
1519:         private static StrategyBase RestoreTemplate(string file, out string problem)
1520:         {
1521:             problem = null;
1522:             Type tt = TemplateType();
1523:             if (tt == null) { problem = "StrategyTemplate type not found"; return null; }
1524:             MethodInfo mi = tt.GetMethod("RestoreFullStrategyTemplate",
1525:                 BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static);
1526:             if (mi == null) { problem = "RestoreFullStrategyTemplate not found"; return null; }
1527:             if (!File.Exists(file)) { problem = "not found: " + file; return null; }
1528:             try
1529:             {
1530:                 System.Xml.Linq.XDocument doc = System.Xml.Linq.XDocument.Load(file);
1531:                 // Hand over the ROOT ELEMENT, symmetric to Save, which fills that element.
1532:                 // A whole document looks for <StrategyType>/<Strategy> as its own children -
1533:                 // and below a document there is only <StrategyTemplate>, so it found nothing
1534:                 // and returned null. Proven by the positive control: a template written by
1535:                 // NinjaTrader ITSELF failed the same way, which ruled out the file.
1536:                 System.Xml.Linq.XContainer node =
1537:                     (System.Xml.Linq.XContainer)doc.Root ?? (System.Xml.Linq.XContainer)doc;
1538:                 object r = mi.Invoke(null, new object[] { node });
1539:                 StrategyBase sbr = r as StrategyBase;
1540:                 if (sbr == null) { problem = "template produced no StrategyBase"; return null; }
1541:                 return sbr;
```

[B11]
```
$ awk 'NR>=2404&&NR<=2417{print NR": "$0}' addon/NT8BridgeServerPlayback.cs | cut -c1-220
2404:                         // ⚠ THE TAB KEEPS ITS OWN INSTRUMENT. It is not taken from the
2405:                         // template, measured on a running NinjaTrader: after assigning
2406:                         // a template that names NQ 06-26, the strategy read NQ 06-26
2407:                         // and the tab still read ES 09-26. A run in that state applies
2408:                         // the template's parameters to the tab's instrument and says
2409:                         // nothing about it - a wrong result that looks like a right
2410:                         // one. So the name travels, when the template carries one.
2411:                         //
2412:                         // Written AFTER the template, and read back below together
2413:                         // with it: if this write were to reinstall the template the
2414:                         // way `Strategy` does, the reference check would catch it.
2415:                         string tmplInstrument = restored.InstrumentOrInstrumentList;
2416:                         if (!string.IsNullOrWhiteSpace(tmplInstrument))
2417:                             tsp.InstrumentOrInstrumentList = tmplInstrument;
```

[B12]
```
$ awk 'NR>=2632&&NR<=2665{print NR": "$0}' addon/NT8BridgeServer.cs | cut -c1-220
2632:         private void RunBacktest(string id, Dictionary<string, string> prms)
2633:         {
2634:             Window saWin = FindStrategyAnalyzerWindow();
2635:             if (saWin == null)
2636:             {
2637:                 WriteResult("backtest_" + id + ".json", BtErr(id, "no Strategy Analyzer window open"));
2638:                 return;
2639:             }
2640:             saWin.Dispatcher.BeginInvoke(new Action(delegate
2641:             {
2642:                 try
2643:                 {
2644:                     StrategyAnalyzerViewModel vm = saWin.DataContext as StrategyAnalyzerViewModel;
2645:                     if (vm == null) { WriteResult("backtest_" + id + ".json", BtErr(id, "SA DataContext is not a StrategyAnalyzerViewModel")); return; }
2646:                     StrategyAnalyzerTabControl tab = vm.SelectedTab;
2647:                     if (tab == null) { WriteResult("backtest_" + id + ".json", BtErr(id, "no active SA tab")); return; }
2648: 
2649:                     // Inject config.json params onto the configured template before running.
2650:                     if (prms != null && prms.Count > 0 && tab.TabStrategyProperties != null && tab.TabStrategyProperties.StrategyTemplate != null)
2651:                         InjectParams(tab.TabStrategyProperties.StrategyTemplate, prms);
2652: 
2653:                     // Capture the current latest result's SystemPerformance so the poll can
2654:                     // detect a NEW one. The SA REPLACES the result on a re-run (Results.Count
2655:                     // stays the same), so a count-based check misses every run after the first.
2656:                     SystemPerformance prevPerf = LatestPerf(tab);
2657: 
2658:                     RoutedCommand rc = StrategyAnalyzerViewModel.RunCommand as RoutedCommand;
2659:                     if (rc == null) { WriteResult("backtest_" + id + ".json", BtErr(id, "RunCommand is not a RoutedCommand")); return; }
2660:                     if (!rc.CanExecute(null, saWin)) { WriteResult("backtest_" + id + ".json", BtErr(id, "RunCommand.CanExecute=false — configure the SA tab (strategy + instrument + dates) first")); return; }
2661: 
2662:                     // Button-equivalent: routes through OnRun on a background thread (safe).
2663:                     LogSafe("backtest: executing RunCommand (had prior result=" + (prevPerf != null) + ")");
2664:                     rc.Execute(null, saWin);
2665:                     StartResultPoll(id, saWin, prevPerf);
```

[B13]
```
$ awk 'NR>=2675&&NR<=2691{print NR": "$0} NR>=2713&&NR<=2718{print NR": "$0}' addon/NT8BridgeServer.cs | cut -c1-220
2675:         // Set config.json params onto the configured strategy template by property
2676:         // name (reflection). Values are converted to each property's type
2677:         // (int/double/bool/enum/string). Unknown or read-only props are skipped.
2678:         private void InjectParams(StrategyBase strat, Dictionary<string, string> prms)
2679:         {
2680:             foreach (var kv in prms)
2681:             {
2682:                 try
2683:                 {
2684:                     PropertyInfo p = strat.GetType().GetProperty(kv.Key, BindingFlags.Public | BindingFlags.Instance);
2685:                     if (p == null || !p.CanWrite) { LogSafe("param skip (no writable prop '" + kv.Key + "')"); continue; }
2686:                     p.SetValue(strat, ConvertToken(kv.Value, p.PropertyType), null);
2687:                     LogSafe("param set: " + kv.Key + "=" + kv.Value);
2688:                 }
2689:                 catch (Exception ex) { LogSafe("param set failed '" + kv.Key + "': " + ex.Message); }
2690:             }
2691:         }
2713:         private static Dictionary<string, string> ParseParams(string json)
2714:         {
2715:             var d = new Dictionary<string, string>();
2716:             if (json == null) return d;
2717:             int pi = json.IndexOf("\"params\"", StringComparison.Ordinal);
2718:             if (pi < 0) return d;
```

[B14]
```
$ awk 'NR>=2812&&NR<=2832{print NR": "$0}' addon/NT8BridgeServer.cs | cut -c1-220
2812:         private string BuildBacktestJson(string id, SystemPerformance perf, string stratName)
2813:         {
2814:             if (perf == null) return BtErr(id, "no SystemPerformance");
2815:             TradeCollection all = perf.AllTrades;
2816:             int nTrades = all != null ? all.Count : 0;
2817: 
2818:             var sb = new StringBuilder();
2819:             sb.Append("{\"id\":").Append(JsonStr(id)).Append(",\"status\":\"ok\",\"strategy\":")
2820:               .Append(JsonStr(stratName != null ? stratName : "")).Append(",\"metrics\":{");
2821:             sb.Append("\"totalTrades\":").Append(nTrades);
2822:             if (all != null && all.TradesPerformance != null)
2823:             {
2824:                 TradesPerformance tp = all.TradesPerformance;
2825:                 sb.Append(",\"profitFactor\":").Append(Num(tp.ProfitFactor));
2826:                 if (tp.Currency != null)
2827:                 {
2828:                     sb.Append(",\"netProfit\":").Append(Num(tp.Currency.CumProfit));
2829:                     sb.Append(",\"maxDrawdown\":").Append(Num(tp.Currency.Drawdown));
2830:                 }
2831:             }
2832:             sb.Append("},\"trades\":[");
```

[B15]
```
$ awk 'NR>=2844&&NR<=2863{print NR": "$0}' addon/NT8BridgeServer.cs | cut -c1-220
2844:                 int cap = nTrades < 5000 ? nTrades : 5000;
2845:                 for (int i = 0; i < cap; i++)
2846:                 {
2847:                     Trade t = all[i];
2848:                     if (i > 0) sb.Append(",");
2849:                     string entry = (t.Entry != null) ? t.Entry.Time.ToString("o") : "";
2850:                     string exit  = (t.Exit  != null) ? t.Exit.Time.ToString("o")  : "";
2851:                     // Times are the NT chart wall-clock (ET per the runbook), tz-naive --
2852:                     // matching the original entryTime; the comparator attaches ET.
2853:                     sb.Append("{\"pnl\":").Append(Num(t.ProfitCurrency))
2854:                       .Append(",\"marketPosition\":").Append(JsonStr(SafeStr(delegate { return t.Entry.MarketPosition.ToString(); })))
2855:                       .Append(",\"entryTime\":").Append(JsonStr(entry))
2856:                       .Append(",\"exitTime\":").Append(JsonStr(exit))
2857:                       .Append(",\"entryPrice\":").Append(SafeNum(delegate { return t.Entry.Price; }))
2858:                       .Append(",\"exitPrice\":").Append(SafeNum(delegate { return t.Exit.Price; }))
2859:                       .Append(",\"exitName\":").Append(JsonStr(SafeStr(delegate { return t.Exit.Order.Name; })));
2860:                     double stp = ResolveStop(t, stops);
2861:                     if (!double.IsNaN(stp))
2862:                         sb.Append(",\"stopPrice\":").Append(Num(stp));
2863:                     sb.Append("}");
```

[B16]
```
$ awk 'NR>=103&&NR<=107{print FILENAME":"NR": "$0} NR>=4529&&NR<=4537{print FILENAME":"NR": "$0}' addon/NT8BridgeServer.cs | cut -c1-220
addon/NT8BridgeServer.cs:103:         private void Init()
addon/NT8BridgeServer.cs:104:         {
addon/NT8BridgeServer.cs:105:             string root = Path.Combine(Globals.UserDataDir, "NT8Bridge");
addon/NT8BridgeServer.cs:106:             _triggerDir = Path.Combine(root, "trigger");
addon/NT8BridgeServer.cs:107:             _resultDir = Path.Combine(root, "result");
addon/NT8BridgeServer.cs:4529:         private void WriteResult(string name, string json)
addon/NT8BridgeServer.cs:4530:         {
addon/NT8BridgeServer.cs:4531:             try
addon/NT8BridgeServer.cs:4532:             {
addon/NT8BridgeServer.cs:4533:                 string dst = Path.Combine(_resultDir, name);
addon/NT8BridgeServer.cs:4534:                 string tmp = dst + ".tmp";
addon/NT8BridgeServer.cs:4535:                 File.WriteAllText(tmp, json);
addon/NT8BridgeServer.cs:4536:                 if (File.Exists(dst)) File.Delete(dst);
addon/NT8BridgeServer.cs:4537:                 File.Move(tmp, dst);   // atomic rename so Python never reads a partial file
```

[B17]
```
$ awk 'FNR>=18&&FNR<=28{print FILENAME":"FNR": "$0}' nt8bridge/ntio.py; awk 'NR>=40&&NR<=53{print FILENAME":"NR": "$0}' nt8bridge/backtest.py | cut -c1-220
nt8bridge/ntio.py:18: def bridge_dir() -> Path:
nt8bridge/ntio.py:19:     return nt8_root() / "NT8Bridge"
nt8bridge/ntio.py:20: 
nt8bridge/ntio.py:21: 
nt8bridge/ntio.py:22: def ensure_bridge_dirs() -> tuple[Path, Path]:
nt8bridge/ntio.py:23:     """Create <NT8>/NT8Bridge/{trigger,result} and return (trigger, result)."""
nt8bridge/ntio.py:24:     trigger = bridge_dir() / "trigger"
nt8bridge/ntio.py:25:     result = bridge_dir() / "result"
nt8bridge/ntio.py:26:     trigger.mkdir(parents=True, exist_ok=True)
nt8bridge/ntio.py:27:     result.mkdir(parents=True, exist_ok=True)
nt8bridge/ntio.py:28:     return trigger, result
nt8bridge/backtest.py:40: def run_backtest(config: dict, timeout: float = 120.0) -> dict:
nt8bridge/backtest.py:41:     """Drop a backtest request for the in-NT8 AddOn and wait for its result.
nt8bridge/backtest.py:42: 
nt8bridge/backtest.py:43:     Returns the raw response payload. During Part-3 bring-up the AddOn replies
nt8bridge/backtest.py:44:     with a probe payload (status="probe"); once real backtests run it carries
nt8bridge/backtest.py:45:     metrics/trades/equity. Raises TimeoutError if the AddOn does not respond.
nt8bridge/backtest.py:46:     """
nt8bridge/backtest.py:47:     trigger, result = ntio.ensure_bridge_dirs()
nt8bridge/backtest.py:48:     request_id = new_request_id()
nt8bridge/backtest.py:49:     ntio.atomic_write_json(
nt8bridge/backtest.py:50:         trigger / f"backtest_{request_id}.json",
nt8bridge/backtest.py:51:         build_backtest_request(request_id, config),
nt8bridge/backtest.py:52:     )
nt8bridge/backtest.py:53:     return ntio.poll_for_json(result / f"backtest_{request_id}.json", timeout=timeout)
```

[B18]
```
$ awk 'NR>=2477&&NR<=2481{print NR": "$0} NR>=2488&&NR<=2500{print NR": "$0}' addon/NT8BridgeServer.cs | cut -c1-220
2477:         private string RunConfigure(string id, string triggerJson)
2478:         {
2479:             Window saWin = FindStrategyAnalyzerWindow();
2480:             if (saWin == null) return BtErr(id, "no Strategy Analyzer window open");
2481:             Dictionary<string, string> prms = ParseParams(triggerJson);
2488:                         StrategyAnalyzerViewModel vm = saWin.DataContext as StrategyAnalyzerViewModel;
2489:                         StrategyAnalyzerTabControl tab = vm != null ? vm.SelectedTab : null;
2490:                         if (tab == null) return BtErr(id, "no active SA tab");
2491:                         string[] targetNames = new string[] { "tab", "tabStrategyProperties", "strategyTemplate" };
2492:                         // Called before EVERY write and again for every read-back. The template
2493:                         // this returns is only guaranteed to be the live one at the moment it is
2494:                         // asked for -- which is the whole lesson of issue #6.
2495:                         StrategyAnalyzerTabControl tabRef = tab;
2496:                         Func<object[]> resolve = new Func<object[]>(delegate
2497:                         {
2498:                             object tsp = tabRef.TabStrategyProperties;
2499:                             object strat = (tsp != null) ? tabRef.TabStrategyProperties.StrategyTemplate : null;
2500:                             return new object[] { tabRef, tsp, strat };
```

[B19]
```
$ awk 'NR>=2557&&NR<=2568{print NR": "$0} NR>=2579&&NR<=2579{print NR": "$0}' addon/NT8BridgeServer.cs | cut -c1-220
2557:         private static string TrySetOnTargets(Func<object[]> resolve, string[] names, string key, string token)
2558:         {
2559:             object[] targets = resolve();
2560:             for (int ti = 0; ti < targets.Length; ti++)
2561:             {
2562:                 if (targets[ti] == null) continue;
2563:                 PropertyInfo p = targets[ti].GetType().GetProperty(key, BindingFlags.Public | BindingFlags.Instance);
2564:                 if (p == null || !p.CanWrite) continue;
2565:                 try
2566:                 {
2567:                     object v = ConvertConfigToken(token, p.PropertyType);
2568:                     p.SetValue(targets[ti], v, null);
2579:             return "{\"key\":" + JsonStr(key) + ",\"status\":\"skip\",\"message\":\"no writable property of this name on tab/tabStrategyProperties/strategyTemplate\"}";
```

[B20]
```
$ awk 'NR>=2607&&NR<=2629{print NR": "$0}' addon/NT8BridgeServer.cs | cut -c1-220
2607:         private static object ConvertConfigToken(string token, Type t)
2608:         {
2609:             string raw = token == null ? null : token.Trim();
2610:             if (raw != null && raw.Length >= 2 && raw[0] == '"' && raw[raw.Length - 1] == '"')
2611:                 raw = raw.Substring(1, raw.Length - 2).Replace("\\\"", "\"").Replace("\\\\", "\\");
2612:             Type nt = Nullable.GetUnderlyingType(t) ?? t;
2613:             if (nt == typeof(Instrument)) return Instrument.GetInstrument(raw);
2614:             if (nt == typeof(DateTime))   return DateTime.Parse(raw, System.Globalization.CultureInfo.InvariantCulture);
2615:             if (nt == typeof(BarsPeriod))
2616:             {
2617:                 // "Second:1" / "Minute:1" / "Tick:1" — type:value[:value2] form. The optional third
2618:                 // part sets Value2 for two-parameter bar types (e.g. a custom add-on type like
2619:                 // NinzaRenko: "12345:64:16" = type 12345, brick 64 / reversal 16). A numeric type
2620:                 // token parses straight through Enum.Parse to (BarsPeriodType)value, so custom add-on
2621:                 // bar types (which register an int BarsPeriodType, not a named enum member) work too.
2622:                 string[] parts = raw.Split(':');
2623:                 BarsPeriodType bpType = (BarsPeriodType)Enum.Parse(typeof(BarsPeriodType), parts[0], true);
2624:                 int val = parts.Length > 1 ? int.Parse(parts[1]) : 1;
2625:                 BarsPeriod bp = new BarsPeriod { BarsPeriodType = bpType, Value = val };
2626:                 if (parts.Length > 2) bp.Value2 = int.Parse(parts[2]);
2627:                 return bp;
2628:             }
2629:             return ConvertToken(token, t);
```

[B21]
```
$ /usr/bin/grep -rnE 'Slippage|IncludeCommission|BarsRequiredToTrade|MaximumBarsLookBack|EntriesPerDirection|EntryHandling|ExitOnSessionClose|TimeInForce|OrderFillResolution|IsFillLimitOnTouch|BreakAtEod|PriceBasedOn|QuantityType|SetOrderQuantity' addon nt8bridge config README.md; echo "grep-exit=$?"
grep-exit=1
```

[B22]
```
$ /usr/bin/grep -n -m1 -E 'StrategyTemplate|RunCommand' addon/NT8BridgeServer.cs addon/NT8BridgeServerPlayback.cs nt8bridge/satemplate.py README.md | cut -c1-200; /usr/bin/grep -n -m1 'params' config/config.json
addon/NT8BridgeServer.cs:2006:        // --- Part 3: run a backtest by firing the SA's RunCommand (the exact
addon/NT8BridgeServerPlayback.cs:1398:        //      StrategyTemplate.LoadTemplate(Window owner, StrategyBase, out StrategyBase)
nt8bridge/satemplate.py:40:Writing the tab's `Strategy` makes NinjaTrader install a fresh StrategyTemplate
README.md:390:the view model's `RunCommand`, and reads the result off the tab's results grid once its progress
11:  "params": {"Period": 14, "StopTicks": 40, "TargetTicks": 80}
```

[B23]
```
$ /usr/bin/grep -rnE 'MarketDataType' addon nt8bridge | cut -c1-200; echo "grep-exit=$?"
nt8bridge/nrd_offline.py:11:MarketDataType, 10/11 = L2 ask/bid depth). Then a merged, time-ordered, variable-length
nt8bridge/nrd_offline.py:288:        "MarketDataType": pa.array(mdt, pa.int8()),
nt8bridge/nrd_offline.py:298:        "MarketDataType": pa.array(side, pa.int8()),
grep-exit=0
```

[B24]
```
$ /usr/bin/grep -nE 'TradingHoursSerializable|TradingHours\.All' addon/NT8BridgeServer.cs addon/NT8BridgeServerPlayback.cs | cut -c1-200
addon/NT8BridgeServerPlayback.cs:6002:                    if (thD != null) { sd.TradingHoursInstance = thD; sd.TradingHoursSerializable = thD.Name; sd.TradingHours = thD; }
addon/NT8BridgeServerPlayback.cs:6293:                        foreach (TradingHours cand in TradingHours.All)
addon/NT8BridgeServerPlayback.cs:6309:                    strat.TradingHoursSerializable = th.Name;
```

[B25]
```
$ /usr/bin/grep -rnE 'BacktestType *=' addon | cut -c1-200
addon/NT8BridgeServerPlayback.cs:1833:                    tsp.BacktestType = bt;
```

[B26]
```
$ /usr/bin/grep -rnE 'slippageTicks|"commission"' addon nt8bridge config | cut -c1-200
nt8bridge/config.schema.json:20:    "commission": {"type": "string"},
nt8bridge/config.schema.json:21:    "slippageTicks": {"type": "integer"},
nt8bridge/performance.py:16:                         "exitPrice","exitName","quantity","commission"}],
nt8bridge/account.py:19:                           "recentExecutions":[{"instrument","marketPosition","quantity","price","time","commission","orderName"}]}],
config/config.json:9:  "commission": "MyCommissionTemplate",
config/config.json:10:  "slippageTicks": 1,
```

[B27]
```
$ /usr/bin/grep -rnE 'OptimizationPeriod|TestPeriod' addon | cut -c1-200
addon/NT8BridgeServerPlayback.cs:1650:        //     (OptimizationPeriod / TestPeriod are the walk-forward window lengths
addon/NT8BridgeServerPlayback.cs:1861:                        + ",\"optimizationPeriod\":" + strat.OptimizationPeriod
addon/NT8BridgeServerPlayback.cs:1862:                        + ",\"testPeriod\":" + strat.TestPeriod
```

[B28]
```
$ awk 'NR>=163&&NR<=183{print NR": "$0}' README.md | cut -c1-260
163: ### backtest
164: 
165: Drives an **open, configured** Strategy Analyzer. Set the SA tab up once (strategy, instrument, dates, commission); the bridge injects `config.json`'s `params` onto the strategy, fires the Run button's command, waits for the run to finish, and reads the c
166: 
167: ```json
168: { "status": "ok", "strategy": "MyStrategy",
169:   "metrics": { "totalTrades": 42, "netProfit": 1250.0, "profitFactor": 1.62, "maxDrawdown": -380.0 },
170:   "trades": [ { "pnl": 72.5, "entryTime": "2024-05-19T09:30:03" } ] }
171: ```
172: 
173: ```bash
174: python -m nt8bridge backtest --config config/config.json --timeout 300 --pdf report.pdf
175: ```
176: 
177: `config.json` (see `config/config.json`):
178: 
179: | field | notes |
180: |---|---|
181: | `typeName` | the NinjaScript class name |
182: | `instrument`, `barType`, `from`, `to`, `capital`, `commission`, `slippageTicks` | reference fields |
183: | `params` | strategy inputs injected before each run (matched by property name) |
```

[B29]
```
$ awk 'NR>=337&&NR<=343{print NR": "$0} NR>=358&&NR<=364{print NR": "$0}' README.md | cut -c1-260
337: `--template` is a full path to one of NinjaTrader's own strategy template `.xml` files, or a
338: bare name looked up in the strategy's template folder. The template is **assigned** to the
339: Strategy Analyzer tab (the complete parameter set plus instrument and window, exactly what the
340: GUI would run); when it belongs to a different strategy than the tab shows, that strategy is
341: selected first, and the instrument travels to the tab because NinjaTrader does not carry it over
342: on its own. The response's `applied` is a reference comparison of the assigned template, and the
343: run window is reported.
358: * `--template` names the strategy template file (full path, or a bare name in the strategy's
359:   template folder, as `satemplate`); it carries the complete parameter set, instrument and window.
360: * `--opt="Name:min:max:step[,...]"` names the parameters to search. The AddOn writes them onto
361:   the template's `OptimizationParameters` as NinjaTrader's own `Parameter` objects — the
362:   collection the GUI's parameter grid fills. NinjaTrader refuses a run without one: with the
363:   run type set and the collection empty, Run shows `The strategy must have at least one
364:   parameter to optimize.` and runs nothing (measured on 8.1.8.2).
```

[B30]
```
$ awk 'NR>=365&&NR<=377{print NR": "$0}' README.md | cut -c1-260
365: * `--optimizer=default|genetic` (exactly these two; anything else is refused rather than run
366:   as the default), `--fitness=<OptimizationFitness class name>` (default: the template's) - ONE
367:   measure for `optimize` and the walk-forwards, a list is refused there; `multiobjective` takes
368:   `--fitness=<A>,<B>[,...]` and needs at least two measures - NinjaTrader's own rule, its Run
369:   button shows `You must have at least two optimization fitnesses selected.` and runs nothing
370:   (measured on 8.1.8.2, 2026-09-09); the CLI and the AddOn refuse such a request before it
371:   reaches the button. The list goes to `Optimizer.MultiObjectiveOptimizationFitnesses`; the
372:   rows of a multi-objective run carry `isParetoDetails` / `isParetoPlaceholder` and
373:   `multiObjectiveValues` (parameter values with one performance value per measure).
374: * Any further `--Name=value` is written to the strategy property of that name after the
375:   template — `--OptimizationPeriod=<days>` and `--TestPeriod=<days>` are the walk-forward
376:   window lengths. A token of another shape is refused (exit 2), never silently dropped.
377: * `--anchored` (walkforward only) selects the anchored walk-forward.
```

[B32]
```
$ awk 'NR>=406&&NR<=414{print NR": "$0} NR>=627&&NR<=629{print NR": "$0}' README.md | cut -c1-260
406: Parity with a GUI-less host, measured 2026-09-08 on NinjaTrader 8.1.8.2 (NQ 09-26,
407: 16.06.–13.07.2026, one optimized parameter 150–250 step 50, in-sample 10 / out-of-sample 5
408: days; bridge run 594 s, the other host's walk-forward on the same template and strategy sources):
409: 4 windows, out-of-sample parameter 250 / 250 / 250 / 150 with 7 / 3 / 14 / 3 trades on both
410: hosts; in-sample ranking per window identical (250 > 200 > 150 three times, 150 > 200 > 250 in
411: the last window); every CSV written on both sides byte-identical (11 of 11, all 4 out-of-sample
412: files among them). The SET of in-sample iteration CSVs differs: the GUI run wrote 12 of the 16
413: instances' files, the headless run 15, each missing different iterations — a strategy instance
414: that never reaches its termination step leaves no file, on either host.
627: ## Compatibility & disclaimer
628: 
629: Developed and verified against NinjaTrader 8.1.6.x on Windows. NT8 Bridge uses some of NinjaTrader's internal APIs; a NinjaTrader update could change them. On a different build, `perfwindow` may report `feesCalculated: false` (trust that flag) and other i
```

[B34]
```
$ awk 'NR>=81&&NR<=90{print NR": "$0} NR>=155&&NR<=183{print NR": "$0}' nt8bridge/analyzerrun.py | cut -c1-220
81: # CLI command -> the value the AddOn writes to StrategyAnalyzerTabProperties.BacktestType
82: # (enum StrategyAnalyzerGuiBacktestType: Backtest, Optimize, WalkForward,
83: # WalkForwardAnchored, MultiObjective, AiGenerate - read off NinjaTrader.Gui 8.1.8.2).
84: MODES = {
85:     "optimize": "Optimize",
86:     "walkforward": "WalkForward",
87:     "multiobjective": "MultiObjective",
88: }
89: COMMANDS = tuple(MODES)
90: OPTIMIZERS = ("default", "genetic")
155: def build_request(request_id: str, mode: str, template: str, opt: str, *,
156:                   optimizer: str = "default", fitness: str = "", anchored: bool = False,
157:                   params: dict | None = None, timeout: float = DEFAULT_TIMEOUT) -> dict:
158:     if mode not in MODES:
159:         raise ValueError("mode must be one of %s" % ", ".join(COMMANDS))
160:     if optimizer not in OPTIMIZERS:
161:         raise ValueError("--optimizer=%s is not a known optimizer. Valid: default | genetic."
162:                          % optimizer)
163:     backtest_type = MODES[mode]
164:     if anchored:
165:         if mode != "walkforward":
166:             raise ValueError("--anchored belongs to walkforward only")
167:         backtest_type = "WalkForwardAnchored"
168:     return {
169:         "id": request_id,
170:         "kind": "analyzerrun",
171:         "mode": backtest_type,
172:         "template": template,
173:         "opt": opt,
174:         "optimizer": optimizer,
175:         "fitness": fitness or "",
176:         "params": dict(params or {}),
177:         # The AddOn stops waiting for the grid when the client would have
178:         # stopped waiting for the file; one number, read on both sides.
179:         "timeoutSec": float(timeout),
180:         # A request that sat in the queue past this is not executed (the AddOn's
181:         # own rule); a parameter search is never worth running on a stale tab.
182:         "ttlSec": 300.0,
183:     }
```

[B38]
```
$ /usr/bin/grep -rnE 'equity' addon/NT8BridgeServer.cs; echo "grep-exit=$?"; /usr/bin/grep -nE 'equity|metrics' nt8bridge/backtest.py | cut -c1-200
addon/NT8BridgeServer.cs:3496:        // The full scorecard (win rate, avg win/loss, equity, drawdown) is derived client-side
grep-exit=0
6:             "metrics": {...}, "trades": [...], "equity": [...],
20:    metrics: dict = field(default_factory=dict)
22:    equity: list[dict] = field(default_factory=list)
33:        metrics=payload.get("metrics", {}),
35:        equity=payload.get("equity", []),
45:    metrics/trades/equity. Raises TimeoutError if the AddOn does not respond.
```

[C02]
```
$ /usr/bin/grep -n '' pyproject.toml
1:[build-system]
2:requires = ["setuptools>=61"]
3:build-backend = "setuptools.build_meta"
4:
5:[project]
6:name = "nt8bridge"
7:version = "1.7.5"
8:license = {text = "MIT"}
9:requires-python = ">=3.10"
10:# numpy + pyarrow are required: histdump's default engine decodes .nrd offline to parquet.
11:dependencies = ["jsonschema>=4", "numpy>=1.24", "pyarrow>=14", "tzdata"]
12:
13:[project.optional-dependencies]
14:dev = ["pytest>=7"]
15:report = ["matplotlib>=3"]
16:parquet = ["pyarrow>=14"]
17:
18:[tool.setuptools.packages.find]
19:include = ["nt8bridge*"]
20:
21:[tool.pytest.ini_options]
22:pythonpath = ["."]
23:testpaths = ["tests"]
```

[C03]
```
$ /usr/bin/grep -n '' nt8bridge/deploy.py
1:"""Atomic deploy of a .cs into the correct NT8 bin/Custom subfolder."""
2:from __future__ import annotations
3:
4:import os
5:from pathlib import Path
6:
7:from nt8bridge import ntio
8:
9:_SUBFOLDER = {"strategy": "Strategies", "indicator": "Indicators", "addon": "AddOns"}
10:
11:
12:def dest_for(name: str, kind: str) -> Path:
13:    if kind not in _SUBFOLDER:
14:        raise ValueError(f"Unknown kind '{kind}'; expected one of {list(_SUBFOLDER)}")
15:    return ntio.nt8_root() / "bin" / "Custom" / _SUBFOLDER[kind] / name
16:
17:
18:def deploy(src, kind: str) -> Path:
19:    src = Path(src)
20:    dest = dest_for(src.name, kind)
21:    dest.parent.mkdir(parents=True, exist_ok=True)
22:    tmp = dest.with_suffix(dest.suffix + ".tmp")
23:    tmp.write_bytes(src.read_bytes())
24:    os.replace(tmp, dest)
25:    return dest
```

[C04]
```
$ awk 'NR>=10&&NR<=28{print NR": "$0}' nt8bridge/ntio.py
10: def nt8_root() -> Path:
11:     """NinjaTrader 8 user data dir. Override with NT8_DIR (used in tests)."""
12:     override = os.environ.get("NT8_DIR")
13:     if override:
14:         return Path(override)
15:     return Path.home() / "Documents" / "NinjaTrader 8"
16: 
17: 
18: def bridge_dir() -> Path:
19:     return nt8_root() / "NT8Bridge"
20: 
21: 
22: def ensure_bridge_dirs() -> tuple[Path, Path]:
23:     """Create <NT8>/NT8Bridge/{trigger,result} and return (trigger, result)."""
24:     trigger = bridge_dir() / "trigger"
25:     result = bridge_dir() / "result"
26:     trigger.mkdir(parents=True, exist_ok=True)
27:     result.mkdir(parents=True, exist_ok=True)
28:     return trigger, result
```

[C05]
```
$ /usr/bin/grep -nE 'checkCompileOnly=|"kind": "(compile|reload)"' nt8bridge/compile.py nt8bridge/reload.py | cut -c1-200
nt8bridge/compile.py:4:  request : {"id": str, "kind": "compile", "typeName": str}
nt8bridge/compile.py:29:    return {"id": request_id, "kind": "compile", "typeName": type_name}
nt8bridge/reload.py:5:`compile` invokes NinjaTrader's compiler with `checkCompileOnly=true`. That answers "does this build?"
nt8bridge/reload.py:11:`reload` runs the same compiler with `checkCompileOnly=false`. NinjaTrader emits and swaps in the new
nt8bridge/reload.py:21:    request : {"id": str, "kind": "reload"}
nt8bridge/reload.py:46:        {"id": request_id, "kind": "reload"},
```

[C06]
```
$ awk 'NR>=1871&&NR<=1878{print NR": "$0}' addon/NT8BridgeServer.cs | cut -c1-200
1871:             Type compilerType = Type.GetType("NinjaTrader.Code.Compiler, NinjaTrader.Core");
1872:             if (compilerType == null) throw new Exception("NinjaTrader.Code.Compiler not found");
1873:             MethodInfo compile = compilerType.GetMethod("Compile", BindingFlags.Public | BindingFlags.Static);
1874:             if (compile == null) throw new Exception("Compiler.Compile(...) not found");
1875: 
1876:             var empty = new List<string>();
1877:             // checkCompileOnly, debugBuild=false, filesToIgnore=[], filesInTmp=[]
1878:             object emit = compile.Invoke(null, new object[] { !reload, false, empty, empty });
```

[C07]
```
$ /usr/bin/grep -nE 'DEFAULT_TASK =|DEFAULT_EXE =|"schtasks", "/run"|"taskkill"|Popen\(|NT8_EXE_DEFAULT =|^def (kill_nt8|launch_nt8|restart_nt8)' nt8bridge/restart.py nt8bridge/watchdog.py | cut -c1-200
nt8bridge/restart.py:36:DEFAULT_TASK = ""
nt8bridge/restart.py:44:DEFAULT_EXE = ""
nt8bridge/restart.py:99:        r = subprocess.run(["schtasks", "/run", "/tn", task],
nt8bridge/restart.py:134:        subprocess.run(["taskkill", "/IM", "NinjaTrader.exe"],
nt8bridge/restart.py:141:        subprocess.run(["taskkill", "/F", "/IM", "NinjaTrader.exe"],
nt8bridge/restart.py:158:        subprocess.Popen([str(p)], close_fds=True)
nt8bridge/watchdog.py:26:NT8_EXE_DEFAULT = r"C:\Program Files\NinjaTrader 8\bin\NinjaTrader.exe"
nt8bridge/watchdog.py:60:def kill_nt8(process_name: str = PROCESS_NAME) -> None:
nt8bridge/watchdog.py:62:        subprocess.run(["taskkill", "/F", "/IM", process_name],
nt8bridge/watchdog.py:68:def launch_nt8(exe: str = NT8_EXE_DEFAULT) -> None:
nt8bridge/watchdog.py:71:    subprocess.Popen([exe], close_fds=True)
nt8bridge/watchdog.py:74:def restart_nt8(exe: str = NT8_EXE_DEFAULT) -> None:
```

[C08]
```
$ /usr/bin/grep -n 'partial class NT8BridgeServer\|RunPlaybackRun(' addon/NT8BridgeServer.cs addon/NT8BridgeServerPlayback.cs | cut -c1-200
addon/NT8BridgeServer.cs:36:    public partial class NT8BridgeServer : AddOnBase
addon/NT8BridgeServer.cs:233:                    WriteResult("playbackrun_" + id + ".json", RunPlaybackRun(id, text));
addon/NT8BridgeServerPlayback.cs:61:    public partial class NT8BridgeServer
addon/NT8BridgeServerPlayback.cs:2489:        private string RunPlaybackRun(string id, string triggerJson)
```

[C13]
```
$ awk '(NR<=5)||(NR>=21&&NR<=25)||(NR>=53&&NR<=59){print NR": "$0}' guard/app/Register-GuardTasks.ps1 | cut -c1-220
1: # Register-GuardTasks.ps1 - install (or -Remove) NT8 Guard's scheduled tasks for the CURRENT user.
2: #
3: # No administrator rights needed: the tasks run as you, in your logged-on session, at the normal
4: # (Limited) run level - verified on Windows 11 with UAC on. They only run while you are logged on,
5: # which is also the only time NinjaTrader can be logged in.
21: $all = [ordered]@{
22:     relaunch   = @{ Task = "$TaskPrefix-Relaunch";   Script = 'Guard-Relaunch.ps1';   Every = 1;  Heartbeat = 'relaunch.heartbeat' }
23:     overwatch  = @{ Task = "$TaskPrefix-Overwatch";  Script = 'Guard-Overwatch.ps1';  Every = 1;  Heartbeat = 'overwatch.heartbeat' }
24:     logarchive = @{ Task = "$TaskPrefix-LogArchive"; Script = 'Guard-LogArchive.ps1'; Every = 10; Heartbeat = 'logarchive.heartbeat' }
25: }
53:     $action    = New-ScheduledTaskAction -Execute 'wscript.exe' -Argument ('"{0}" "{1}" -GuardHome "{2}"' -f $vbs, $d.Script, $gh)
54:     # No -RepetitionDuration: omitted means "repeat indefinitely" ([TimeSpan]::MaxValue is rejected).
55:     $trigger   = New-ScheduledTaskTrigger -Once -At (Get-Date).AddSeconds(30) -RepetitionInterval (New-TimeSpan -Minutes $d.Every)
56:     $principal = New-ScheduledTaskPrincipal -UserId "$env:USERDOMAIN\$env:USERNAME" -LogonType Interactive -RunLevel $RunLevel
57:     $settings  = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable `
58:                      -ExecutionTimeLimit (New-TimeSpan -Minutes 5) -MultipleInstances IgnoreNew
59:     Register-ScheduledTask -TaskName $d.Task -Action $action -Trigger $trigger -Principal $principal -Settings $settings -Force | Out-Null
```

[C14]
```
$ awk '(NR<=4)||(NR>=9&&NR<=13){print NR": "$0}' guard/app/lib/Guard.Password.psm1 | cut -c1-200
1: # The saved NinjaTrader password: a PSCredential exported with Export-Clixml, i.e. Windows DPAPI for the
2: # CURRENT USER. It cannot be read by another Windows user or on another machine - it must be saved on the
3: # box, under the account the scheduled tasks run as. Written by the control panel (or Guard-Login.ps1
4: # -SetPassword), read by the login helper. Never logged, never shown.
9: function Save-GuardPassword {
10:     [CmdletBinding()] param([Parameter(Mandatory)][securestring]$Password, [string]$GuardHome)
11:     New-Object System.Management.Automation.PSCredential('nt8', $Password) |
12:         Export-Clixml -Path (Get-GuardCredentialPath $GuardHome) -Force
13: }
```

[C15]
```
$ awk '(NR>=3&&NR<=16)||/SendKeys\]::SendWait|IsPasswordProperty, \$true|InvokePattern\]::Pattern\)\.Invoke/{print NR": "$0}' guard/app/Guard-Login.ps1 | cut -c1-200
3: # NinjaTrader has no command-line login, so the password is entered into its login window. That only
4: # works on an UNLOCKED, connected desktop (every starter holds off while the screen is locked).
5: #   * First choice, no keyboard at all: Windows UI Automation finds the password box by what it is
6: #     (not where it sits) and sets its value, then presses the Log In button. Nothing can land in
7: #     another app, and the clipboard is never used.
8: #   * Only if that is not possible, the keyboard - and only after checking that NinjaTrader's window
9: #     really is in front with the keyboard focus. A watchdog runs in the background, and Windows often
10: #     refuses to bring a window forward while you are typing elsewhere: then nothing is typed (the
11: #     password would go into your chat or browser) and the attempt is counted as 'not in front'.
12: #     The keyboard path pastes from a clipboard copy marked to stay out of clipboard history and
13: #     cloud sync (cleared right after), or types if the clipboard is unavailable.
14: #   * Enter is pressed only to a verified NinjaTrader window, when there is no Log In button.
15: #   * NinjaTrader must remember the USERNAME (tick "Remember username" in its login window once):
16: #     only the password is entered.
168:         $c = New-Object Windows.Automation.PropertyCondition([Windows.Automation.AutomationElement]::IsPasswordProperty, $true)
201:         [Windows.Forms.SendKeys]::SendWait('^v')
206:         [Windows.Forms.SendKeys]::SendWait((ConvertTo-SendKeysLiteral $Secret))
254:         $b.GetCurrentPattern([Windows.Automation.InvokePattern]::Pattern).Invoke()
257:     Enter       = { [Windows.Forms.SendKeys]::SendWait('{ENTER}') }
```

[C16]
```
$ awk '(NR<=13)||(NR==138){print NR": "$0}' guard/app/Guard-Relaunch.ps1 | cut -c1-200
1: # Guard-Relaunch.ps1 - keep a HEALTHY NinjaTrader 8 running. Scheduled task, every minute.
2: #
3: # Owns "NinjaTrader is DOWN" (crash, closed by hand, killed by the overwatch) and "NinjaTrader is up
4: # but stuck at its login window". The overwatch owns "up but sick".
5: #
6: #   * PAUSE, LOCKED SCREEN, BACKOFF, REFUSED PASSWORD: the shared gate (Test-Nt8StartAllowed in
7: #     Guard.Start) - the same rules hold every starter. A locked screen holds starts until the unlock
8: #     (logged once); the probe FAILS OPEN.
9: #   * STUCK AT LOGIN: NinjaTrader still titled 'Welcome' after stuckMinutes -> kill it so the next start
10: #     can log in. Sooner (loginDeadSeconds) only for a NinjaTrader GUARD launched whose login helper has
11: #     gone: one the user opened by hand gets the full stuckMinutes.
12: #   * DISCONNECTED REMOTE SESSION: reattach it to the console (tscon) so the login can type.
13: #   * Starting NinjaTrader always goes through Invoke-Nt8Start (put strategies back, unlock wait, log in).
138:     Tscon         = { param($id) try { & tscon.exe $id /dest:console 2>&1 | Out-Null; Start-Sleep -Seconds 2 } catch { } }
```

[C17]
```
$ awk 'NR>=29&&NR<=34{print NR": "$0}' guard/app/Guard-Overwatch.ps1 | cut -c1-200
29: #   Guard-Relaunch.ps1  owns "NinjaTrader is DOWN": starts it through the shared start routine, with
30: #                       its own backoff and the stuck-at-login detector.
31: #   this overwatch      owns "NinjaTrader is UP but SICK": prove it, then KILL the process and let the
32: #                       relauncher bring it back. It starts NinjaTrader itself ONLY when the relauncher
33: #                       is not running (its heartbeat is stale) - through the same routine, so the same
34: #                       rules (pause, lock screen, backoff, refused password, one start at a time) hold.
```

[C18]
```
$ /usr/bin/grep -rnE 'HKCU:|HKLM:|Registry::|New-ItemProperty|Set-ItemProperty|netsh|New-NetFirewallRule|New-Service|sc\.exe|CurrentVersion\\Run|shell:startup|#Requires|tscon\.exe' guard/app guard/python guard/Install.cmd --exclude-dir=tests --include='*.ps1' --include='*.psm1' --include='*.py' --include='*.cmd' --include='*.vbs' | cut -c1-200
guard/app/Guard-Relaunch.ps1:138:    Tscon         = { param($id) try { & tscon.exe $id /dest:console 2>&1 | Out-Null; Start-Sleep -Seconds 2 } catch { } }
guard/app/lib/Guard.Setup.psm1:70:        $AutoLogon = { try { [string](Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon' -Name AutoAdminLogon -ErrorAction Stop).AutoAdmin
guard/app/lib/Guard.Setup.psm1:73:        $ScalePercent = { try { [int][math]::Round([double](Get-ItemProperty 'HKCU:\Control Panel\Desktop\WindowMetrics' -Name AppliedDPI -ErrorAction Stop).AppliedDP
```

[C19]
```
$ awk '(NR<=8)||(NR>=121&&NR<=127){print NR": "$0}' guard/python/nt8guard_backup/restore.py | cut -c1-200
1: """Put strategies NinjaTrader dropped from its list back - then back on their charts.
2: 
3: NinjaTrader must be CLOSED: a row written under a running NT8 is overwritten from memory when it
4: exits, and so are the workspace files. Report only, unless --apply. The database is backed up first
5: (last 3 kept). One transaction per strategy, with foreign_key_check and integrity_check compared to a
6: baseline from the untouched database. The original Id is reused when free; otherwise a fresh Id is
7: taken AT INSERT TIME (two remaps in one pass must not collide) and the chart follows via relink.
8: A strategy whose account or instrument no longer exists is refused, never half-restored.
121:     # Two independent checks: NT8 running against the folder Guard finds by itself, and the target
122:     # database file being open at all - which also catches the live folder spelled another way.
123:     live_db = nt8 / "db" / "NinjaTrader.sqlite"
124:     if (paths.is_live_nt8_dir(nt8) and nt8_running()) or db_in_use(db) or (db != live_db and db_in_use(live_db)):
125:         print("REFUSED: NinjaTrader is running (or something has its database open). A strategy written now "
126:               "is overwritten from memory when it closes. Close NinjaTrader first.", file=sys.stderr)
127:         return 1
```

[C21]
```
$ /usr/bin/grep -nH -e 'Windows PowerShell 5.1' -e 'Python 3.14 embeddable' -e 'Standard-library Python' guard/app/README.md guard/python/README.md | cut -c1-200
guard/app/README.md:3:Windows PowerShell 5.1 scripts that keep NinjaTrader 8 running. They ship as source, run as scheduled
guard/app/README.md:207:- `app\` and `python\` — the program and its bundled Python (Python 3.14 embeddable, with the backup
guard/python/README.md:3:Command-line tools that NT8 Guard runs for you. Standard-library Python 3.10+, no installs (the QR
```

[C22]
```
$ /usr/bin/grep -rnoE '.{0,90}8\.1\.[0-9]+(\.[0-9x]+)?.{0,50}' README.md CHANGELOG.md addon nt8bridge guard --include='*.md' --include='*.cs' --include='*.py' --include='*.ps1' --include='*.psm1' --include='*.txt' | /usr/bin/grep -v 'tests/' | cut -c1-220
README.md:34:- NinjaTrader 8 (developed/verified against 8.1.6.x), with historical data loaded
README.md:154:d hot-reload the assembly by itself — no F5, nobody at the GUI. Measured on NinjaTrader 8.1.7.2: `NinjaTrader.Custom.dll` was rebuilt ~19 s after
README.md:154:as separately verified to trigger the same reload (`Custom.dll` rebuilt within seconds on 8.1.6.x), so `deploy` is not an inert copy either.
README.md:364:  parameter to optimize.` and runs nothing (measured on 8.1.8.2).
README.md:370:  (measured on 8.1.8.2, 2026-09-09); the CLI and the AddOn refuse such a
README.md:395:one Guid become one row). What NinjaTrader 8.1.8.2 puts into the grid for a walk-forward: one
README.md:406:Parity with a GUI-less host, measured 2026-09-08 on NinjaTrader 8.1.8.2 (NQ 09-26,
README.md:629:Developed and verified against NinjaTrader 8.1.6.x on Windows. NT8 Bridge uses some of NinjaTrader's
CHANGELOG.md:184:  parameter to optimize.` and runs nothing (NinjaTrader 8.1.8.2, 2026-09-08) — which is why
CHANGELOG.md:273:  NinjaTrader 8.1.8.2 the same day: answered in 1.2 s with
CHANGELOG.md:670:Verified live on 8.1.6.3 with `Strategy` deliberately listed **last** in t
CHANGELOG.md:859:  + `os.replace` rename triggers the reload too (DLL rebuilt within seconds on 8.1.6.x), matching the
CHANGELOG.md:860:  in-place overwrite measured on 8.1.7.2 (~19s). Documents the two consequences: the reloa
CHANGELOG.md:914:NinjaTrader 8.1.6.x on Windows.
addon/NT8BridgeServerPlayback.cs:1644:        //  NinjaTrader.Gui 8.1.8.2).
addon/NT8BridgeServerPlayback.cs:1646:        //  What the run needs, each item measured on 8.1.8.2:
addon/NT8BridgeServerPlayback.cs:1972:        // One JSON object per new grid entry. What NinjaTrader 8.1.8.2 puts into the
addon/NT8BridgeServerPlayback.cs:2468:        // 8.1.8.2: `PlaybackAdapter.FromEst` set before the connect
addon/AutoReconnect.cs:875:        // NinjaTrader 8.1.8.3 by tools\Test-FeedGuardNt8Api.ps1.
addon/NT8BridgeServer.cs:2476:        //   Reported by Quantrosoft as issue #6 on the public repo (verified on 8.1.8.2).
nt8bridge/analyzerrun.py:43:  optimize``, measured on 8.1.8.2 with the type set and the collection empty).
nt8bridge/analyzerrun.py:83:# WalkForwardAnchored, MultiObjective, AiGenerate - read off NinjaTrader.Gui 8.1.8.2).
guard/app/README.md:61:1. **Check this PC** - NinjaTrader's version (8.1.6.3 and later green, other 8.1 amber, 8.0 red), its
guard/app/lib/Guard.Status.psm1:238:        if ($v -ge [version]'8.1.6.3') { $verNote = "version $v" }
guard/app/lib/Guard.Status.psm1:239:f ($v.Major -eq 8 -and $v.Minor -eq 1) { $verNote = "version $v is not tested with Guard (8.1.6.3 and later are)"; $verState = 'warn' }
guard/app/lib/Guard.Setup.psm1:83:        if ($v -ge [version]'8.1.6.3') { $rows.Add((New-SetupRow nt8version 'NinjaTrad
guard/app/lib/Guard.Setup.psm1:84:(New-SetupRow nt8version 'NinjaTrader' warn "NinjaTrader $v is not tested with Guard yet (8.1.6.3 and later are). It should work: watch the Status 
guard/python/nt8guard_backup/nt8db.py:4:are exactly the layout it was built against (NT8 8.1.6.3 - 8.1.8.3), and only reads one that has the
guard/build/Build-AddOnsZip.ps1:58:    <Version>8.1.6.0</Version>
guard/build/New-GuardDemoState.ps1:56:usArgs = @{ Processes = $procs; TaskState = { param($n) 'Ready' }; Nt8Version = [version]'8.1.8.3' }
guard/build/New-GuardDemoState.ps1:57:        SetupCheckArgs = @{ Nt8Version = [version]'8.1.8.3'; AutoLogon = { $true }; ScalePercent = { 125 }; 
guard/build/Guard.Release.psm1:262:         "(Get-GuardSetupCheck -Nt8Version ([version]'8.1.8.3') -AutoLogon { `$true } -ScalePercent { 100 } -Ot
```

[C23]
```
$ /usr/bin/grep -nE "\[version\]'8\.1\.6\.3'|VersionInfo\.FileVersion" guard/app/lib/Guard.Status.psm1 guard/app/lib/Guard.Setup.psm1 guard/app/lib/Guard.Paths.psm1 | cut -c1-200
guard/app/lib/Guard.Status.psm1:238:        if ($v -ge [version]'8.1.6.3') { $verNote = "version $v" }
guard/app/lib/Guard.Setup.psm1:83:        if ($v -ge [version]'8.1.6.3') { $rows.Add((New-SetupRow nt8version 'NinjaTrader' ok "NinjaTrader $v - tested with Guard.")) }
guard/app/lib/Guard.Paths.psm1:50:    try { return [version](Get-Item $exe).VersionInfo.FileVersion } catch { return $null }
```

[C24]
```
$ /usr/bin/grep -rnE 'FileVersionInfo|ProductVersion|Globals\.Version|VersionInfo\.FileVersion' addon nt8bridge --include='*.cs' --include='*.py'; echo "grep exit=$? (1 = no match in addon/ or nt8bridge/)"
grep exit=1 (1 = no match in addon/ or nt8bridge/)
```

[C25]
```
$ /usr/bin/grep -nE 'C# 5|\.NET Framework' addon/NT8BridgeServer.cs | head -3 | cut -c1-200
3024:        // The stop of one trade, from plain data (C# 5: the test compiles it with the .NET Framework csc).
```

[C26]
```
$ awk 'FNR<=3{print FILENAME":"FNR": "$0}' LICENSE guard/LICENSE guard/python/vendor/segno/LICENSE guard/app/panel/fonts/OFL.txt
LICENSE:1: MIT License
LICENSE:2: 
LICENSE:3: Copyright (c) 2026 eman007
guard/LICENSE:1: MIT License
guard/LICENSE:2: 
guard/LICENSE:3: Copyright (c) 2026 eman007
guard/python/vendor/segno/LICENSE:1: Copyright (c) 2016 - 2024, Lars Heuer
guard/python/vendor/segno/LICENSE:2: All rights reserved.
guard/python/vendor/segno/LICENSE:3: 
guard/app/panel/fonts/OFL.txt:1: Copyright © 2017 IBM Corp. with Reserved Font Name "Plex"
guard/app/panel/fonts/OFL.txt:2: 
guard/app/panel/fonts/OFL.txt:3: This Font Software is licensed under the SIL Open Font License, Version 1.1.
```

[C27]
```
$ /usr/bin/grep -n -A1 'above copyright notice and this permission notice' LICENSE guard/LICENSE addon/NT8BridgeServerPlayback.cs
LICENSE:12:The above copyright notice and this permission notice shall be included in all
LICENSE-13-copies or substantial portions of the Software.
--
guard/LICENSE:12:The above copyright notice and this permission notice shall be included in all
guard/LICENSE-13-copies or substantial portions of the Software.
--
addon/NT8BridgeServerPlayback.cs:11:The above copyright notice and this permission notice shall be included in all
addon/NT8BridgeServerPlayback.cs-12-copies or substantial portions of the Software.
```

[C28]
```
$ /usr/bin/grep -rnI 'Copyright (c)' --exclude-dir=.git --exclude-dir=vendor . | cut -c1-160
./LICENSE:3:Copyright (c) 2026 eman007
./tests/test_analyzerrun.py:2:# Copyright (c) 2026 Quantrosoft Pty. Ltd.
./tests/test_satemplate.py:2:# Copyright (c) 2026 Quantrosoft Pty. Ltd.
./addon/NT8BridgeServerPlayback.cs:2:Copyright (c) 2026 Quantrosoft Pty. Ltd.
./guard/LICENSE:3:Copyright (c) 2026 eman007
./guard/THIRD-PARTY-NOTICES.txt:9:   Copyright (c) 2001 Python Software Foundation; All Rights Reserved.
./guard/THIRD-PARTY-NOTICES.txt:16:   Copyright (c) 2016 - 2024, Lars Heuer. All rights reserved.
./guard/THIRD-PARTY-NOTICES.txt:22:   Copyright (c) 2017 IBM Corp. with Reserved Font Name "Plex".
./guard/THIRD-PARTY-NOTICES.txt:28:   Copyright (c) 2026 Quantrosoft Pty. Ltd.
./nt8bridge/satemplate.py:2:# Copyright (c) 2026 Quantrosoft Pty. Ltd.
./nt8bridge/analyzerrun.py:2:# Copyright (c) 2026 Quantrosoft Pty. Ltd.
./nt8bridge/playback_run.py:2:# Copyright (c) 2026 Quantrosoft Pty. Ltd.
```

[C29]
```
$ awk 'NR>=4&&NR<=35{print NR": "$0}' guard/THIRD-PARTY-NOTICES.txt | cut -c1-200
4: NT8 Guard itself is MIT-licensed (LICENSE). It includes, unchanged, the following works by others.
5: Each one's full licence text ships beside it, at the path given.
6: 
7: 1. Python (CPython) 3.14 - embeddable package
8:    python\  (python.exe, python314.dll, python314.zip and their modules)
9:    Copyright (c) 2001 Python Software Foundation; All Rights Reserved.
10:    Licence: PSF License Agreement for Python, and the licences of the libraries CPython bundles
11:    (bzip2, expat, libffi, OpenSSL, SQLite, xz, zlib and others).
12:    Full text: python\LICENSE.txt
13: 
14: 2. segno - QR code generator (draws the phone-alert QR code)
15:    python\vendor\segno\
16:    Copyright (c) 2016 - 2024, Lars Heuer. All rights reserved.
17:    Licence: BSD 3-Clause.
18:    Full text: python\vendor\segno\LICENSE
19: 
20: 3. IBM Plex fonts (the control panel's type: Plex Sans, Sans Condensed, Mono)
21:    app\panel\fonts\
22:    Copyright (c) 2017 IBM Corp. with Reserved Font Name "Plex".
23:    Licence: SIL Open Font License, Version 1.1.
24:    Full text: app\panel\fonts\OFL.txt
25: 
26: 4. NT8BridgeServerPlayback.cs - part of the NT8 link add-on (Playback and Strategy Analyzer requests)
27:    NT8Guard-AddOns.zip -> AddOns/NT8BridgeServerPlayback.cs
28:    Copyright (c) 2026 Quantrosoft Pty. Ltd.
29:    Licence: MIT. Full text: the notice at the top of that file.
30: 
31: Credit, no code included
32: ------------------------
33: The way the login helper (app\Guard-Login.ps1) finds NinjaTrader's login window and fills in the
34: password follows the approach of the NinjaTraderAutoLogin project. None of its code is included;
35: Guard's helper is its own PowerShell script and finds the password box with Windows UI Automation.
```

[C30]
```
$ /usr/bin/grep -n 'Redistributions' guard/python/vendor/segno/LICENSE
7:1. Redistributions of source code must retain the above copyright notice,
10:2. Redistributions in binary form must reproduce the above copyright notice,
```

[C31]
```
$ git log --oneline | wc -l; git log --reverse --format='first: %ad %h %an' --date=short | head -1; git log -1 --format='last: %ad %h %an (committer date %cd)' --date=short
      55
first: 2026-06-09 724a29f eman007
last: 2026-10-18 9664d9b eman007 (committer date 2026-10-18)
```

[C33]
```
$ git log --format='%ad' --date=format:%Y-%m | sort | uniq -c
   6 2026-06
   9 2026-07
   7 2026-08
  10 2026-09
  23 2026-10
```

[C35]
```
$ /usr/bin/grep -nE '^## \[' CHANGELOG.md
7:## [Unreleased]
9:## [1.7.5] - 2026-10-19
17:## [1.7.4] - 2026-10-19
44:## [1.7.3] - 2026-10-18
65:## [1.7.2] - 2026-10-17
98:## [1.7.1] - 2026-10-15
148:## [1.7.0] - 2026-10-10
572:## [1.6.0] - 2026-08-20
631:## [1.5.1] - 2026-08-19
673:## [1.5.0] - 2026-08-04
735:## [1.4.0] - 2026-08-04
798:## [1.3.0] - 2026-07-30
839:## [1.2.0] - 2026-07-22
867:## [1.1.2] - 2026-07-22
878:## [1.1.1] - 2026-07-19
890:## [1.1.0] - 2026-07-19
911:## [1.0.0] - 2026-07-18
958:## [0.1.0]
```

[C36]
```
$ /usr/bin/grep -rl --include='test_*.py' --include='Test-*.ps1' '' tests guard/app/tests guard/python/tests tools | awk -F/ '{d=($1=="guard")?$1"/"$2"/"$3:$1; c[d]++} END{for(k in c) print k": "c[k]" test files"}'
tests: 41 test files
guard/python/tests: 10 test files
tools: 9 test files
guard/app/tests: 36 test files
```

[C37]
```
$ /usr/bin/grep -rl '' .github 2>&1 | head -2
grep: .github: No such file or directory
```

[C38]
```
$ /usr/bin/grep -nE 'compile\.Invoke\(null|StrategyAnalyzerViewModel\.RunCommand as RoutedCommand|tsp\.BacktestType = bt|acct\.Flatten\(instrs\)|Connection\.Connect\(o2\)|GetProperty\("IsSourceHistoricalData"|GetMethod\("OnClick"|UI-thread liveness beat' addon/NT8BridgeServer.cs addon/NT8BridgeServerPlayback.cs | cut -c1-200
addon/NT8BridgeServer.cs:153:        // UI-thread liveness beat: rewrite heartbeat.json from the MAIN UI dispatcher
addon/NT8BridgeServer.cs:1832:                    .GetMethod("OnClick", BindingFlags.NonPublic | BindingFlags.Instance);
addon/NT8BridgeServer.cs:1878:            object emit = compile.Invoke(null, new object[] { !reload, false, empty, empty });
addon/NT8BridgeServer.cs:2658:                    RoutedCommand rc = StrategyAnalyzerViewModel.RunCommand as RoutedCommand;
addon/NT8BridgeServer.cs:3333:                    try { acct.Flatten(instrs); flattenCalled = true; }
addon/NT8BridgeServer.cs:4439:                    Action act = delegate { ran = true; try { Connection.Connect(o2); } catch (Exception ex) { cap = ex; } };
addon/NT8BridgeServerPlayback.cs:1200:                        ? null : pbT.GetProperty("IsSourceHistoricalData", BFStatic);
addon/NT8BridgeServerPlayback.cs:1833:                    tsp.BacktestType = bt;
addon/NT8BridgeServerPlayback.cs:1849:                    RoutedCommand rc = StrategyAnalyzerViewModel.RunCommand as RoutedCommand;
addon/NT8BridgeServerPlayback.cs:5639:                                    PropertyInfo piS = pb.GetProperty("IsSourceHistoricalData", BFStatic);
```

## Correction 1 (2026-11-06, completion unit; appended, nothing above edited)

Written by unit `2026-11-06-cli-nt-bridge-code-read-completion` after a fresh read-only adversarial pass. Its full return is in `docs/reports/2026-11-06-cli-nt-bridge-code-read-manager.md`. The completion manager re-ran each block below through this report's own harness (line 21). `[Kxx]` blocks run from the clone root, `[P90]` from the repo root. Every line above this heading is unchanged.

**C1-1. Line 29, "The bridge lists no NT8 property names for the last two."** This is too strong. The bridge's playback code sets NT8's trading-hours properties by name on a `StrategyBase` [K01]. A test fixture also sets `BacktestCommissionTemplate` on a strategy [K02]. B21 did not cover that fixture, because it searched only `addon nt8bridge config README.md`. Corrected statement: the bridge's code does name NT8 properties for two of the 15 BLOCKER settings. B21's 14 setting names appear nowhere in the clone, tests included; the positive control in the same command finds the two names [K04]. For trading hours, its playback path writes `TradingHoursSerializable` / `TradingHours` (OBSERVED, `addon/NT8BridgeServerPlayback.cs:6002,6309@9664d9b`). For the commission template, a test fixture names `BacktestCommissionTemplate` (OBSERVED in `tests/fixtures/BadLoadStrategy.cs:16@9664d9b`; that it is an NT8 property is REPORTED BY eman007). Whether `configure` or `params` with either name takes effect on a Strategy Analyzer tab is UNVERIFIED. Line 102's "no Analyzer path" should read "no explicit Analyzer field".

**C1-2. Line 29, "plausible only if the tab is first set by hand exactly as in the committed run."** The word "only" rules out routes (b), (c) and (d). Lines 118–120 grade those routes UNVERIFIED, not refuted [P90]. The `NT8 behaviour: UNVERIFIED` hits at lines 68, 122 and 190 in [P90] are other statements; they are not part of this correction. The `configure` header also says it is meant to replace the hand set-up (REPORTED BY eman007) [K03]. Corrected statement (INFERRED): from the code, an exact reproduction is plausible if the tab holds exactly the committed run's settings. Those settings can be set by hand (route a). They might also be set by template, `configure` or `params` (routes b–d, all UNVERIFIED). This changes the premise behind NEEDS AMEAR 10. It answers nothing on Amear's behalf.

**C1-3. Line 32, Summary item 6 is graded "(OBSERVED; Q5.)" as a whole.** That grade covers its first sentence, "Any process running as the VM user can drop a request". The body grades this point lower at line 173: "(Code OBSERVED; the VM's effective ACL is UNVERIFIED.)" [P90]. Corrected grade: code OBSERVED (no authentication, plain `CreateDirectory`). Who can write the request folder on the VM is UNVERIFIED.

[K01]
```
$ /usr/bin/grep -n 'TradingHoursSerializable' addon/NT8BridgeServerPlayback.cs | cut -c1-200; /usr/bin/grep -n 'StrategyBase strat;\|sd = (StrategyBase)' addon/NT8BridgeServerPlayback.cs | cut -c1-120
6002:                    if (thD != null) { sd.TradingHoursInstance = thD; sd.TradingHoursSerializable = thD.Name; sd.TradingHours = thD; }
6309:                    strat.TradingHoursSerializable = th.Name;
5975:                        sd = (StrategyBase)Activator.CreateInstance(stD);
6214:                    StrategyBase strat;
```

[K02]
```
$ /usr/bin/grep -rn 'BacktestCommissionTemplate' --exclude-dir=.git . | cut -c1-200; sed -n '15,16p' tests/fixtures/BadLoadStrategy.cs
./tests/fixtures/BadLoadStrategy.cs:16:                BacktestCommissionTemplate = "DoesNotExist";
                // Illegal in SetDefaults: surfaces only when NT8 instantiates the type.
                BacktestCommissionTemplate = "DoesNotExist";
```

[K03]
```
$ sed -n '2462,2465p' addon/NT8BridgeServer.cs
        // DateTime/TimeSpan/Enum parsed explicitly; ints/doubles via Convert.ChangeType.
        // Returns a per-key result list so the caller can verify what landed where.
        // (Intended replacement for the manual "open SA tab + click everything" step
        //  before each backtest sweep.)
```

[K04]
```
$ /usr/bin/grep -rnE 'Slippage|IncludeCommission|BarsRequiredToTrade|MaximumBarsLookBack|EntriesPerDirection|EntryHandling|ExitOnSessionClose|TimeInForce|OrderFillResolution|IsFillLimitOnTouch|BreakAtEod|PriceBasedOn|QuantityType|SetOrderQuantity' --exclude-dir=.git .; echo "grep-exit=$?"; /usr/bin/grep -rlE 'TradingHoursSerializable|BacktestCommissionTemplate' --exclude-dir=.git .; echo "control-exit=$?"
grep-exit=1
./tests/fixtures/BadLoadStrategy.cs
./addon/NT8BridgeServerPlayback.cs
control-exit=0
```

[P90]
```
$ awk 'NR<=240' docs/reports/2026-11-06-cli-nt-bridge-code-read.md | /usr/bin/grep -n -o 'The bridge lists no NT8 property names for the last two\.\|plausible only if the tab is first set by hand\|(OBSERVED; Q5\.)\|(Code OBSERVED; the VM.s effective ACL is UNVERIFIED\.)\|(b) carry it in an NT8-saved template\. UNVERIFIED\.\|(c) send `configure <NT8PropertyName>=<value>`\. UNVERIFIED\.\|is NT8 behaviour: UNVERIFIED\.'
29:The bridge lists no NT8 property names for the last two.
29:plausible only if the tab is first set by hand
32:(OBSERVED; Q5.)
68:is NT8 behaviour: UNVERIFIED.
118:(b) carry it in an NT8-saved template. UNVERIFIED.
119:(c) send `configure <NT8PropertyName>=<value>`. UNVERIFIED.
120:is NT8 behaviour: UNVERIFIED.
122:is NT8 behaviour: UNVERIFIED.
173:(Code OBSERVED; the VM's effective ACL is UNVERIFIED.)
190:is NT8 behaviour: UNVERIFIED.
```


## Correction 2 (2026-11-06, after audit FAIL 1; appended, nothing above edited)

Written by a correction unit for `2026-11-06-cli-nt-bridge-code-read` after audit FAIL 1. Authorisation: DECISION_LOG.md row `[2026-11-06T19:43:00Z] WHO: praxis-master` (working tree, line 463 when read) [P99] (OBSERVED). Each block below was run through this report's own harness (line 21). `[Kxx]` blocks run from the clone root `B`, and `[P9x]` blocks from the repo root `/Volumes/Sensidine/Praxis.build`. Nothing in the clone was run. The K blocks use only `awk`, `grep`, `cut`, `echo`, `git rev-parse` and `shasum` (OBSERVED; the commands are pasted). [P99] hashes lines 1–2919 of this report. It was captured before this section was appended, so re-running it prints the same hash only if nothing above this heading has changed (OBSERVED). Grades follow the key at lines 13–19.

A note on exit codes: in [K06], [K08] and [P95], an `exit=$?` printed right after a pipe that ends in `cut` or `sed` is that command's exit, not `grep`'s. There the evidence of a match is the printed lines, not the number. Each absence below rests on a `grep` that is the last command of its pipe or is not piped at all: C24's patterns in [K06], the second command of [P92], and the old-wording and new-wording `grep`s of [P95] (OBSERVED; the commands are pasted).

**C2-1. Line 81: the refusal paths are cited to blocks that do not show them.** Line 81 says the AddOn "refuses a malformed entry, a name that is not a property, a type mismatch, and step ≤ 0 (`:1733-1750`) [M41][M42]" [P91]. As pasted, M41 and M42 print lines 1691–1692, 1743–1745 and 1749–1758 of `addon/NT8BridgeServerPlayback.cs` [P92]. No line among lines 1–2919 of this report starts with `1733: `, `1734: `, `1737: `, `1738: `, `1747: ` or `1748: ` (grep exit 1) [P92]. That is the form the appendix's awk blocks use to print a source line. So [M41][M42] never showed three of the four refusal paths; they showed only step ≤ 0 (OBSERVED). [K05] prints lines 1733–1750. Corrected sentence for line 81 (OBSERVED code; [K05]): the AddOn also refuses an entry without four fields, with "needs 4 fields Name:min:max:step." (`addon/NT8BridgeServerPlayback.cs:1733-1734@9664d9b`); a name that is not a public instance property of the strategy, with "is not a public property of" (`:1736-1738`); a min or max that does not convert to the property's type, or a step that does not parse as a number, with "does not fit" (`:1741-1748`); and a step ≤ 0, with "must be > 0." (`:1749-1750`). The rest of line 81 is unchanged: `:1730` [M49] and the Python CLI refusal [M50].

**C2-2. Lines 3 and 240 count one adversarial worker; four adversarial passes are on file.** Line 3 says "(praxis-manager, three capture workers, one adversarial worker)". Line 240 says "Three capture workers and one adversarial worker read the clone under the same limits" [P91]. The original unit's scratchpad holds four adversarial-pass files, dated 13:59 to 14:19 [P94] (OBSERVED):

| Pass | File | Time | Size (bytes) | Headline |
|---|---|---|---|---|
| ADV | `bridge-work/ADV/NOTES.md` | 13:59 | 2036 | no verdict line; 1 MAJOR, 8 MINOR |
| ADV2 | `bridge-work/ADV2/findings.md` | 14:06 | 2210 | `VERDICT: FAIL`; F1 MAJOR, 8 MINOR |
| ADV3 | `bridge-work/ADV3/findings.md` | 14:12 | 1723 | `VERDICT: FAIL (2 MAJOR, 5 MINOR)` |
| ADV4 | `bridge-work/ADV4/2026-11-06-cli-nt-bridge-adv4.md` | 14:19 | 4207 | `Result: FAIL`; 2 MAJOR, 7 MINOR |

The times, sizes and verdict lines are as printed in [P94], and the MINOR counts are its per-file counts (8, 8, 5, 7). Every MAJOR finding is printed in full in [P97]. `bridge-work/` is `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/bridge-work`. Its `W1/notes.md`, `W2/notes.md` and `W3/notes.md` exist [P97] (OBSERVED).
- Corrected statement for line 3 (OBSERVED [P94][P97]): praxis-manager, three capture workers (W1, W2, W3), and four adversarial passes (ADV, ADV2, ADV3, ADV4).
- Corrected statement for the last sentence of line 240: three capture workers and four adversarial passes worked on the clone (OBSERVED [P94][P97]). That they all kept to the same limits is the original manager's statement (REPORTED BY the original manager). It is not re-checked here.

Every MAJOR finding in the four passes, and where it now stands. The "finding" column paraphrases the pass's own text in [P97] (REPORTED BY that pass).

| # | Pass | MAJOR finding [P97] | Status |
|---|---|---|---|
| 1 | ADV (`ADV/NOTES.md:3`) | "arm (a) cannot run as NT8 WalkForward through this bridge" overclaims, because `opt=Contracts:1:1:1` passes the AddOn's checks; "would have to be" prescribes a method, and that choice is Amear's | Reflected in the body. Neither phrase is in lines 1–241 (grep exit 1), and the same patterns print matches from `ADV/NOTES.md` [P95]. Line 30 has "is UNVERIFIED. The committed strategy declares only two inputs", and line 236 asks Amear "How should each arm be run through the bridge?" [P95] (OBSERVED) |
| 2 | ADV2 F1 (`ADV2/findings.md:3`) | the empty-range refusal is CLI-only; the AddOn checks only blank text, so `opt=","` "gets past every AddOn check" in a raw trigger file | Reflected in the body. "refuses a walk-forward with an empty" and "requires a non-empty" are absent from lines 1–241 (grep exit 1), and the same patterns print matches from `ADV2/findings.md` [P95]. Lines 30, 79 and 134 say the AddOn's "only check for an empty `opt` is a blank-text test". Line 134 says "a trigger file written directly does not pass through that check", and line 236 says "and its CLI refuses one with no ranges" [P95] (OBSERVED) |
| 3 | ADV3 M1 (`ADV3/findings.md:3-6`) | "only/exactly two settable properties" misses the members the strategy inherits from NT8, which `GetProperty(name, Public\|Instance)` finds | Reflected in the body. "exactly two settable" is absent from lines 1–241 (grep exit 1), and the same pattern prints a match from `ADV3/findings.md` [P95]. Line 135 says the strategy "declares two inputs (`[NinjaScriptProperty]`)", and line 122 says "These are inherited NT8 members" [P95] (OBSERVED). The two leftovers ADV4 names (its MINOR items 4 and 5) are fixed here in C2-5 |
| 4 | ADV3 M2 (`ADV3/findings.md:7-8`) | the `1692:` quote at lines 79–80 had no `path:line@sha`, and the clause before it attributed it to the Python CLI | Reflected in the body. Line 79 cites `addon/NT8BridgeServerPlayback.cs:1691-1692@9664d9b` [P95], and source line 1692 is printed in M41, at report line 821 [P92] (OBSERVED) |
| 5 | ADV4 item 1 (`ADV4/…adv4.md:8`) | line 81 cites [M41][M42] for refusal lines that those blocks do not print | Not reflected in the body. Fixed here: C2-1 [K05][P92] |
| 6 | ADV4 item 2 (`ADV4/…adv4.md:9`) | line 165 "no version check (grep exit 1) [C24]" is an absence claim with no positive control, and C24's patterns miss `NtCoreVersion()` | Not reflected in the body. Fixed here: C2-3 [K06][K07][K08][K10][K11] |

"Reflected in the body" means only that lines 1–241 now carry the replacement wording and not the flagged wording, as [P95] prints (OBSERVED). That the original manager made those edits in answer to these passes is INFERRED. The only basis is that ADV4 marks six "Prior items" FIXED under that heading, and its items 1 and 2 match rows 3 and 4 by content [P96] (REPORTED BY the fourth adversary; the match is INFERRED). For each of the six MAJOR rows, the body now carries replacement wording or this correction carries a fix (OBSERVED for the wording, [P95]; for the fixes, the blocks named in rows 5 and 6). The 28 MINOR findings are not listed one by one here. Apart from ADV4 items 4 and 5 (C2-5), this correction claims none of them fixed. No fix here needs a ruling, so no NEEDS AMEAR question is added.

**C2-3. Lines 165–167 (Q4, NT8 version): the absence claim was blind to the bridge's own version read.** Line 165 says "The bridge has no version check (grep exit 1) [C24]". Line 167 says "Code does not know the VM's build" [P91]. On the same `addon nt8bridge` trees, C24's four patterns still give grep exit 1. A positive control on two files of those trees prints three lines: `addon/NT8BridgeServer.cs:348`, `:595` and `nt8bridge/ntstatus.py:24` [K06]. So C24's patterns cannot see the bridge's version code (OBSERVED).

Corrected statement for the first sentence of line 165 (code OBSERVED; nothing run):
- The AddOn has `private static string NtCoreVersion()`. It returns `typeof(Connection).Assembly.GetName().Version.ToString()`, or `""` on any exception (`addon/NT8BridgeServer.cs:348-351@9664d9b`) [K07].
- A request of kind `ntstatus` writes `ntstatus_<id>.json` from `RunNtStatus(id)` (`:234-235`, `:512`) [K10]. The JSON built at `:590-596` includes `"ntVersion"`, set to `NtCoreVersion()` (`:595`) [K07][K10]. That `:595` lies inside `RunNtStatus` is INFERRED: between lines 512 and 594 only line 512 starts at class-member indentation [K11].
- `nt8bridge/ntstatus.py:22-25@9664d9b` describes the `ntstatus` response with `"ntVersion": str` [K07].
- A search of the whole clone for `NtCoreVersion` or `ntVersion` prints only those three lines from `addon/` and `nt8bridge/`. Its other two hits are in `guard/`, and one of them is a substring match inside `CurrentVersion` [K08] (OBSERVED). None of the three bridge lines compares the version with a required build (OBSERVED for those lines, [K07]). Whether a check exists under some other name is not shown here: UNVERIFIED.
- Whether this string equals the build NT8 shows the user, such as 8.1.8.x, is UNVERIFIED. It is the version of the .NET assembly that defines `Connection`, and nobody ran it here. Guard's `>= 8.1.6.3` check [C23] stands as written.

Corrected statement replacing the first sentence of line 167, "Code does not know the VM's build":
- This report observes no value of the VM's NT8 build. The repo carries REPORTED values that name different builds at different dates:
  - a 2026-10-19 report records an 8.1.7.2 install from the MsiInstaller events, and says "Version in Help > About: not read" [P98] (REPORTED BY an in-VM agent);
  - Amear's 2026-10-31 notes say "The NT8 version reads 8.1.8.4." [P11] (REPORTED BY Amear);
  - the 2026-11-02 plan's line 3 says it was written on the VM with "NinjaTrader 8.1.8.4" [P98] (REPORTED BY Claude Code on the VM).
- The repo was not searched end to end for other records, so whether more exist is UNVERIFIED.
- Once installed, the bridge could report a version string as `ntVersion` in its `ntstatus` result (code OBSERVED [K07][K10]). What it would print on the VM is UNVERIFIED.
- This bears on D-2026-11-06-A item 1 (record the build) and on NEEDS AMEAR 6 (INFERRED). Line 167 records item 1 as pending; its status now is not re-checked here (UNVERIFIED). This is a pointer only. This report does not say how item 1 should be done, and NEEDS AMEAR 6 stays a question for Amear.

**C2-4. Line 5: the two sha256 prefixes are paired the wrong way round.** The audit row calls this "M3 line 4" [P99]. The sentence is on line 5 [P91] (OBSERVED). Line 5 names "The README and `addon/NT8BridgeServer.cs`" in that order, then the prefixes "`948cb9d5bef0` / `8fb9566d11f8`". That order puts `948cb9d5bef0` against the README [P91] (OBSERVED). In the clone at `9664d9b255bfa34b120d88a481afe7741a4115e6`, `948cb9d5bef0` is `addon/NT8BridgeServer.cs` and `8fb9566d11f8` is `README.md` [K09]. The 2026-11-04 catalogue pairs them the same way: its line 280 has `addon/NT8BridgeServer.cs … 948cb9d5bef0`, and its line 408 has `README.md … 8fb9566d11f8` ([P13] re-run as pasted) [P93] (OBSERVED). Corrected statement: `addon/NT8BridgeServer.cs` (`948cb9d5bef0`, 4766 lines) and the README (`8fb9566d11f8`, 633 lines) match the copies catalogued on 2026-11-04 in sha256 prefix and line count (OBSERVED [K09][P93][M02]). That they are byte-identical is INFERRED from matching 12-hex-digit prefixes and line counts; the full hashes were not compared.

**C2-5. Lines 135 and 236 (ADV4's MINOR items 4 and 5).** Line 135 says "NT8 members, below". Line 236 says arm (b)'s three parameters "are not properties of the committed strategy" [P98] (OBSERVED).
- Corrected statement for line 135: the paragraph on inherited NT8 members is above, at line 122 [P95] (OBSERVED).
- Corrected statement for line 236's second sentence: arm (b)'s lookback, noise multiplier and stop-ATR multiplier are not declared inputs (`[NinjaScriptProperty]`) of the committed strategy [P16] (OBSERVED). This matches line 135. Whether NT8 or the bridge could set them some other way is not shown here: UNVERIFIED. The question in NEEDS AMEAR 12 is unchanged and stays Amear's.

[K05]
```
$ awk 'NR>=1733&&NR<=1750{print NR": "$0}' addon/NT8BridgeServerPlayback.cs | cut -c1-200
1733:                         if (f.Length != 4)
1734:                         { WriteResult(resultFile, BtErr(id, "analyzerrun: --opt entry '" + part + "' needs 4 fields Name:min:max:step.")); return; }
1735:                         string name = f[0].Trim();
1736:                         PropertyInfo prop = strat.GetType().GetProperty(name, BindingFlags.Public | BindingFlags.Instance);
1737:                         if (prop == null)
1738:                         { WriteResult(resultFile, BtErr(id, "analyzerrun: '" + name + "' is not a public property of " + strat.GetType().Name + ".")); return; }
1739:                         object min, max;
1740:                         double step;
1741:                         try
1742:                         {
1743:                             min  = Convert.ChangeType(f[1].Trim(), prop.PropertyType, InvCi);
1744:                             max  = Convert.ChangeType(f[2].Trim(), prop.PropertyType, InvCi);
1745:                             step = double.Parse(f[3].Trim(), InvCi);
1746:                         }
1747:                         catch (Exception ex)
1748:                         { WriteResult(resultFile, BtErr(id, "analyzerrun: '" + part + "' does not fit " + prop.PropertyType.Name + ": " + ex.Message)); return; }
1749:                         if (step <= 0)
1750:                         { WriteResult(resultFile, BtErr(id, "analyzerrun: step width in '" + part + "' must be > 0.")); return; }
```

[K06]
```
$ /usr/bin/grep -rnE 'FileVersionInfo|ProductVersion|Globals\.Version|VersionInfo\.FileVersion' addon nt8bridge --include='*.cs' --include='*.py'; echo "C24-patterns exit=$?"; /usr/bin/grep -n 'NtCoreVersion\|ntVersion' addon/NT8BridgeServer.cs nt8bridge/ntstatus.py | cut -c1-200; echo "control exit=$?"
C24-patterns exit=1
addon/NT8BridgeServer.cs:348:        private static string NtCoreVersion()
addon/NT8BridgeServer.cs:595:                  .Append(",\"ntVersion\":").Append(JsonStr(NtCoreVersion()))
nt8bridge/ntstatus.py:24:             "processStartUtc": str, "ntVersion": str, "userDataDir": str,
control exit=0
```

[K07]
```
$ awk 'NR>=347&&NR<=351{print FILENAME":"NR": "$0}' addon/NT8BridgeServer.cs | cut -c1-200; awk 'NR==595{print FILENAME":"NR": "$0}' addon/NT8BridgeServer.cs | cut -c1-220; awk 'NR>=22&&NR<=25{print FILENAME":"NR": "$0}' nt8bridge/ntstatus.py | cut -c1-200
addon/NT8BridgeServer.cs:347:         private const int PlaybackSampleMs = 400;
addon/NT8BridgeServer.cs:348:         private static string NtCoreVersion()
addon/NT8BridgeServer.cs:349:         {
addon/NT8BridgeServer.cs:350:             try { return typeof(Connection).Assembly.GetName().Version.ToString(); } catch { return ""; }
addon/NT8BridgeServer.cs:351:         }
addon/NT8BridgeServer.cs:595:                   .Append(",\"ntVersion\":").Append(JsonStr(NtCoreVersion()))
nt8bridge/ntstatus.py:22:   request : {"id": str, "kind": "ntstatus"}
nt8bridge/ntstatus.py:23:   response: {"id": str, "status": "ok"|"error", "ts": str, "pid": int,
nt8bridge/ntstatus.py:24:              "processStartUtc": str, "ntVersion": str, "userDataDir": str,
nt8bridge/ntstatus.py:25:              "loadedAssembly": {"version": str|None, "location": str|None,
```

[K08]
```
$ /usr/bin/grep -rn 'NtCoreVersion\|ntVersion' --exclude-dir=.git . | cut -c1-200; echo "exit=$?"
./addon/NT8BridgeServer.cs:348:        private static string NtCoreVersion()
./addon/NT8BridgeServer.cs:595:                  .Append(",\"ntVersion\":").Append(JsonStr(NtCoreVersion()))
./guard/app/tools/Probe-LoginWindow.ps1:61:    [ordered]@{ utc = [DateTime]::UtcNow.ToString('o'); ntVersion = $version; title = $p.MainWindowTitle; verdict = $verdict
./guard/app/lib/Guard.Setup.psm1:70:        $AutoLogon = { try { [string](Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon' -Name AutoAdminLogon -ErrorAction Stop).AutoAdm
./nt8bridge/ntstatus.py:24:             "processStartUtc": str, "ntVersion": str, "userDataDir": str,
exit=0
```

[K09]
```
$ git rev-parse HEAD; shasum -a 256 addon/NT8BridgeServer.cs README.md | cut -c1-12,65-
9664d9b255bfa34b120d88a481afe7741a4115e6
948cb9d5bef0  addon/NT8BridgeServer.cs
8fb9566d11f8  README.md
```

[K10]
```
$ awk 'NR==234||NR==235||NR==512||(NR>=590&&NR<=596){print NR": "$0}' addon/NT8BridgeServer.cs | cut -c1-170
234:                 else if (kind == "ntstatus")
235:                     WriteResult("ntstatus_" + id + ".json", RunNtStatus(id));
512:         private string RunNtStatus(string id)
590:                 var sb = new StringBuilder();
591:                 sb.Append("{\"id\":").Append(JsonStr(id))
592:                   .Append(",\"status\":\"ok\",\"ts\":").Append(JsonStr(DateTime.UtcNow.ToString("o")))
593:                   .Append(",\"pid\":").Append(proc.Id.ToString(InvCi))
594:                   .Append(",\"processStartUtc\":").Append(JsonStr(procStart.ToString("o")))
595:                   .Append(",\"ntVersion\":").Append(JsonStr(NtCoreVersion()))
596:                   .Append(",\"userDataDir\":").Append(JsonStr(Globals.UserDataDir))
```

[K11]
```
$ awk 'NR>=512&&NR<595&&/^        [A-Za-z]/{print NR": "$0; c++} END{print "class-indent lines in 512-594: " c+0}' addon/NT8BridgeServer.cs | cut -c1-120
512:         private string RunNtStatus(string id)
class-indent lines in 512-594: 1
```

[P91]
```
$ awk 'NR==3||NR==81||NR==165||NR==167||NR==240{print NR": "$0}' docs/reports/2026-11-06-cli-nt-bridge-code-read.md | cut -c1-420; awk 'NR==5' docs/reports/2026-11-06-cli-nt-bridge-code-read.md | /usr/bin/grep -o 'The README and .*\[P13\]\.' | sed 's/^/5: /'
3: - Unit: `2026-11-06-cli-nt-bridge-code-read` (praxis-manager, three capture workers, one adversarial worker).
81: - The AddOn then splits `opt` on commas and drops empty parts (`:1730`) [M49]. It also refuses a malformed entry, a name that is not a property, a type mismatch, and step ≤ 0 (`:1733-1750`) [M41][M42]. The Python CLI separately refuses a list with no ranges, with its own message (`nt8bridge/analyzerrun.py:117-118@9664d9b`, called at `cli.py:597`) [M50].
165:   - The bridge has no version check (grep exit 1) [C24]. Guard checks `>= 8.1.6.3` [C23].
167:   - Code does not know the VM's build. Amear reports 8.1.8.4 [P11]. D-2026-11-06-A item 1 (record it) is pending.
240: This unit ran nothing, installed nothing, and did not touch the VM, the share or NT8. Its only network call was one anonymous `git clone`. It staged nothing and made no change to beads or ledgers beyond the two MANIFEST rows. Three capture workers and one adversarial worker read the clone under the same limits.
5: The README and `addon/NT8BridgeServer.cs` are byte-identical to the copies catalogued on 2026-11-04: same sha256 prefixes `948cb9d5bef0` / `8fb9566d11f8`, same line counts [M02][P13].
```

[P92]
```
$ awk 'NR>=817&&NR<=845&&/^\[M4[12]\]$/{print NR": "$0} NR>=817&&NR<=845&&/^1[67][0-9][0-9]: /{print NR": "substr($0,1,5)}' docs/reports/2026-11-06-cli-nt-bridge-code-read.md; awk 'NR<=2919' docs/reports/2026-11-06-cli-nt-bridge-code-read.md | /usr/bin/grep -n '^173[3478]: \|^174[78]: '; echo "refusal-lines-pasted exit=$?"
817: [M41]
820: 1691:
821: 1692:
822: 1743:
823: 1744:
824: 1745:
827: [M42]
830: 1749:
831: 1750:
832: 1751:
833: 1752:
834: 1753:
835: 1754:
836: 1755:
837: 1756:
838: 1757:
839: 1758:
refusal-lines-pasted exit=1
```

[P93]
```
$ awk 'NR==65||NR==216||NR==217||NR==245||NR==280||NR==408{print NR": "$0}' docs/reports/2026-11-04-comparable-builds.md | cut -c1-230
65: - **Walk-forward from outside NT8 (OBSERVED, implemented; untested on 8.1.7.2).** eman007/cli-nt-bridge (MIT, LICENSE file in tree). Manager re-print:
216: | A2 | eman007/cli-nt-bridge · `addon/NT8BridgeServerPlayback.cs` `RunAnalyzerRun` ~1827-1849 | external driver for NT8 WalkForward (implemented; unverified on 8.1.7.2) | MIT | third-party AddOn on the trading install |
217: | A3 | eman007/cli-nt-bridge · `addon/NT8BridgeServer.cs` 200-212 (TTL → "NOT executed"), 4534-4537 (`.tmp` + `File.Move`) | stale-request rejection; atomic write (implemented) | MIT | pattern for the PRAXIS watcher and th
245: eman007/cli-nt-bridge	17	2026-10-19T05:22:33Z	MIT	PowerShell	false	false
280: eman007/cli-nt-bridge main addon/NT8BridgeServer.cs     4766 lines 948cb9d5bef0
408: 200	eman007/cli-nt-bridge	HEAD	README.md	633 lines 8fb9566d11f8
```

[P94]
```
$ W=/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/bridge-work; cd $W && ls -l ADV/NOTES.md ADV2/findings.md ADV3/findings.md ADV4/2026-11-06-cli-nt-bridge-adv4.md | awk '{print $5, $6, $7, $8, $9}'; /usr/bin/grep -nE '^(VERDICT|Result):|MAJOR' ADV/NOTES.md ADV2/findings.md ADV3/findings.md ADV4/2026-11-06-cli-nt-bridge-adv4.md | cut -c1-150; /usr/bin/grep -cE '^MINOR|^F[0-9] MINOR|^m[0-9] |^[0-9]\. MINOR' ADV/NOTES.md ADV2/findings.md ADV3/findings.md ADV4/2026-11-06-cli-nt-bridge-adv4.md
2036 Nov 6 13:59 ADV/NOTES.md
2210 Nov 6 14:06 ADV2/findings.md
1723 Nov 6 14:12 ADV3/findings.md
4207 Nov 6 14:19 ADV4/2026-11-06-cli-nt-bridge-adv4.md
ADV/NOTES.md:3:MAJOR: report L30/L130 "arm (a) cannot run as NT8 WalkForward through this bridge" - Playback.cs:1691 checks only optSpec non-empty; 17
ADV2/findings.md:2:VERDICT: FAIL
ADV2/findings.md:3:F1 MAJOR L30/L233 (also L131): The text says "refuses a walk-forward with an empty opt (no parameter range)" and "requires a non-em
ADV3/findings.md:2:VERDICT: FAIL (2 MAJOR, 5 MINOR)
ADV4/2026-11-06-cli-nt-bridge-adv4.md:8:1. MAJOR, line 81. Says the AddOn "refuses a malformed entry, a name that is not a property, a type mismatch, 
ADV4/2026-11-06-cli-nt-bridge-adv4.md:9:2. MAJOR, line 165. "The bridge has no version check (grep exit 1) [C24]" is an absence claim with no positive
ADV4/2026-11-06-cli-nt-bridge-adv4.md:29:Result: FAIL
ADV/NOTES.md:8
ADV2/findings.md:8
ADV3/findings.md:5
ADV4/2026-11-06-cli-nt-bridge-adv4.md:7
```

[P95]
```
$ W=/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/bridge-work; X='cannot run as NT8\|would have to be\|requires a non-empty\|refuses a walk-forward with an empty\|exactly two settable'; awk 'NR<=241' docs/reports/2026-11-06-cli-nt-bridge-code-read.md | /usr/bin/grep -n -o "$X"; echo "old-wording-in-body exit=$?"; /usr/bin/grep -o "$X" $W/ADV/NOTES.md $W/ADV2/findings.md $W/ADV3/findings.md | sed "s|$W/||"; echo "control-on-ADV-files exit=$?"; awk 'NR<=241' docs/reports/2026-11-06-cli-nt-bridge-code-read.md | /usr/bin/grep -n -o 'only check for an empty `opt` is a blank-text test\|is UNVERIFIED\. The committed strategy declares only two inputs\|a trigger file written directly does not pass through that check\|addon/NT8BridgeServerPlayback.cs:1691-1692@9664d9b\|These are inherited NT8 members\|declares two inputs (`\[NinjaScriptProperty\]`)\|and its CLI refuses one with no ranges\|How should each arm be run through the bridge?'; echo "new-wording exit=$?"
old-wording-in-body exit=1
ADV/NOTES.md:cannot run as NT8
ADV/NOTES.md:would have to be
ADV2/findings.md:refuses a walk-forward with an empty
ADV2/findings.md:requires a non-empty
ADV3/findings.md:exactly two settable
control-on-ADV-files exit=0
30:only check for an empty `opt` is a blank-text test
30:is UNVERIFIED. The committed strategy declares only two inputs
79:only check for an empty `opt` is a blank-text test
79:addon/NT8BridgeServerPlayback.cs:1691-1692@9664d9b
122:These are inherited NT8 members
134:only check for an empty `opt` is a blank-text test
134:a trigger file written directly does not pass through that check
135:declares two inputs (`[NinjaScriptProperty]`)
236:and its CLI refuses one with no ranges
236:How should each arm be run through the bridge?
new-wording exit=0
```

[P96]
```
$ W=/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/bridge-work; /usr/bin/grep -n '^## Prior items\|^[0-9] FIXED' $W/ADV4/2026-11-06-cli-nt-bridge-adv4.md | cut -c1-110
18:## Prior items
19:1 FIXED (P16, P17, M54 support line 122 and Summary 4). Leftovers: findings 4 and 5.
20:2 FIXED (line 79 cites addon/NT8BridgeServerPlayback.cs:1691-1692@9664d9b; M41 and B02 paste it).
21:3 FIXED in wording. The new sentence at line 81 brings in finding 1.
22:4 FIXED (P18 pastes the master's row 464 text).
23:5 FIXED (M55 pastes cli.py:1391).
24:6 FIXED in the Q5 table (A19 shows :4874; M56 lists the other sites). Leftovers: findings 6 and 7.
```

[P97]
```
$ cd /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/bridge-work && awk 'FILENAME=="ADV/NOTES.md"&&FNR==3 || FILENAME=="ADV2/findings.md"&&FNR==3 || FILENAME=="ADV3/findings.md"&&FNR>=3&&FNR<=8 || FILENAME~/^ADV4/&&(FNR==8||FNR==9){print FILENAME":"FNR": "$0}' ADV/NOTES.md ADV2/findings.md ADV3/findings.md ADV4/2026-11-06-cli-nt-bridge-adv4.md; ls W1/notes.md W2/notes.md W3/notes.md
ADV/NOTES.md:3: MAJOR: report L30/L130 "arm (a) cannot run as NT8 WalkForward through this bridge" - Playback.cs:1691 checks only optSpec non-empty; 1730-1750 accept any Name:min:max:step with step>0, no min<max check -> opt=Contracts:1:1:1 passes. NT8 behaviour UNVERIFIED; "cannot" overclaims; L130 "would have to be" prescribes method (Q12 is Amear's).
ADV2/findings.md:3: F1 MAJOR L30/L233 (also L131): The text says "refuses a walk-forward with an empty opt (no parameter range)" and "requires a non-empty opt range". The AddOn checks only IsNullOrWhiteSpace(optSpec) (Playback.cs:1691). Then 1729-1730 Clear() + Split(',', RemoveEmptyEntries): opt="," gives zero ranges and gets past every AddOn check. The empty-range refusal is CLI-only (analyzerrun.py:117-118, called from cli.py:597), and the report neither cites nor pastes it. A raw trigger file, which Q5 treats as a real path, can request a zero-parameter WF, which is arm (a)'s case. The evidence is in evidence-wf-empty-opt.txt.
ADV3/findings.md:3: M1 Summary:30 + Q3:132 "only/exactly two settable properties" (OBSERVED code). P16 greps only declared one-line auto-properties.
ADV3/findings.md:4:    ninjascript/PraxisNoiseAreaBreakout.cs:105-113 sets EntriesPerDirection=1, EntryHandling.AllEntries, IsExitOnSessionCloseStrategy=true,
ADV3/findings.md:5:    ExitOnSessionCloseSeconds, StartBehavior, TimeInForce.Day, BarsRequiredToTrade=20 (inherited members). The bridge reflects
ADV3/findings.md:6:    GetProperty(name, Public|Instance) (NT8BridgeServer.cs:2683, PlaybackServer:1736), and that call finds inherited members too.
ADV3/findings.md:7: M2 Q2:79-80 the quote "1692: ... needs opt=..." has no path:line@sha, and the clause before it attributes it to the Python CLI (analyzerrun.py/cli.py) [M50].
ADV3/findings.md:8:    The quoted line is in addon/NT8BridgeServerPlayback.cs:1692. The CLI text is "needs --opt=...". The fix for item 1 brought this in.
ADV4/2026-11-06-cli-nt-bridge-adv4.md:8: 1. MAJOR, line 81. Says the AddOn "refuses a malformed entry, a name that is not a property, a type mismatch, and step <= 0 (:1733-1750) [M41][M42]". M41 prints 1691,1692,1743-1745 only. M42 prints 1749-1758. The refusal lines are not pasted in any block: 1733-1734 (needs 4 fields), 1737-1738 (is not a public property), 1747-1748 (does not fit). This sentence was added to fix prior item 3. The claim is true in the clone (I read 1686-1800), but the blocks it cites do not show it. S1.
ADV4/2026-11-06-cli-nt-bridge-adv4.md:9: 2. MAJOR, line 165. "The bridge has no version check (grep exit 1) [C24]" is an absence claim with no positive control. Its patterns (FileVersionInfo|ProductVersion|Globals.Version|VersionInfo.FileVersion) miss the bridge's own version read: addon/NT8BridgeServer.cs:348-350 NtCoreVersion() = typeof(Connection).Assembly.GetName().Version, which ntstatus reports as "ntVersion" (:595; nt8bridge/ntstatus.py:24). I found no version comparison, so "no check" may still hold. The search was blind to the relevant code, though. The report also leaves out that the bridge can report the NT build, which bears on line 167, D-2026-11-06-A item 1 and NEEDS AMEAR 6.
W1/notes.md
W2/notes.md
W3/notes.md
```

[P98]
```
$ awk 'NR==135||NR==236{print NR": "$0}' docs/reports/2026-11-06-cli-nt-bridge-code-read.md | /usr/bin/grep -o '^[0-9]*: \|NT8 members, below\|are not properties of the committed strategy' | paste -sd' ' -; awk 'NR==3' docs/reports/2026-11-02-vm-high-res-plan.md | cut -c1-200; awk 'NR==60' docs/reports/2026-10-19-windows-vm-state-update-2-from-migration.md | cut -c1-330
135:  NT8 members, below 236:  are not properties of the committed strategy
Written by Claude Code on the VM (VMware, Windows 11 ARM64, NinjaTrader 8.1.8.4) under Amear's ruling R-VN3-2. **Plan only.** Nothing was bought, imported, run or changed in NinjaTrader to write it.
| 4 | NT8 8.1.7.2 from the saved MSI; sign in; new Machine ID | **Installed and signed in. Machine ID not recorded** | Install REPORTED (in-VM agent read the MsiInstaller events: 8.1.7.2, status 0, 2026-10-19 13:03Z). Amear signed in himself; no licence or update prompt (REPORTED). Version in Help > About: not read. **Machine ID
```

[P99]
```
$ awk 'NR==463' DECISION_LOG.md | /usr/bin/grep -o '^- \[2026-11-06T19:43:00Z\] WHO: praxis-master\|M3 line 4 pairs the two sha prefixes the wrong way round'; head -n 2919 docs/reports/2026-11-06-cli-nt-bridge-code-read.md | shasum -a 256
- [2026-11-06T19:43:00Z] WHO: praxis-master
M3 line 4 pairs the two sha prefixes the wrong way round
da5f4dbc81a1ff295d9c78f0b3fca390e177d8a87c3ac0ad0ee9e658665b110d  -
```
