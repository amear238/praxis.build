# NinjaTrader 8 (Windows) — Layout & Workflow Reference

**Purpose:** Grounded, task-oriented knowledge base of *this* NinjaTrader 8 install for (a) Amear to execute NT8 tasks himself and (b) the repo teaching-agent (bead `bev`) to teach against. Feeds the Block-5 comprehension gate (D-2026-07-04-A).

**Target install (version-stamped):** NinjaTrader **8.1.7.2 (64-bit)**, Windows 11 VM (Parallels).
- Machine ID `077EF45C126711A89343DA3F0E442333` · User `Amear238` · © 2003–2026 NinjaTrader, LLC.
- Source of the version: `Help > About` — see [`02-help-about.png`](assets/nt8-2026-07-24/02-help-about.png).

**Provenance:** two independent halves, merged 2026-07-24.
1. **Web-docs half** — official NT8 Help Guide (https://ninjatrader.com/support/helpguides/nt8/), researched against 8.1.x. Each section cites its exact page.
2. **Live-install half** — 20 screenshots + capture notes taken on this VM on 2026-07-24 08:14–08:44 ET by the Cowork agent (sim-only, no orders/compile/run). Raw captures + the coworker's `00-notes.txt` are in [`assets/nt8-2026-07-24/`](assets/nt8-2026-07-24/).

Where the live UI differs from the public Help Guide, **the live install wins** and the difference is called out with a ⚠️ **LIVE**. Items still unverified against the live UI carry a 🔲 **TODO**.

> **Convention:** `Menu > Submenu > Item` = click-path. `"Button"` / `"Field"` = literal on-screen label.

---

## 0. Fast orientation (this install at a glance)

- **Root window:** Control Center. Everything opens from its **New** menu (working windows) or **Tools** menu (managers/utilities).
- **Control Center top menu bar:** NINJATRADER · **New** · **Tools** · **Workspaces** · **Connections** · **Help** · **Chat**.
- **Control Center tabs:** Orders · Executions · Strategies · Positions · Accounts · Log · Messages.
- **Account:** `Sim101` on the **Simulated Data Feed**, $99,995 cash — the whole PRAXIS build stays on this sim account through Block 4.
- **Data feed:** Kinetick – End Of Day (Free) available; Simulated Data Feed connected during capture (green dot).
- **Your strategies are already installed:** `PraxisNoiseAreaBreakout` (Strategy Analyzer category "02. Praxis (tunable)") and `PraxisSignalConsumer` (chart Strategies dialog). Confirmed live — see §5.
- ⚠️ **LIVE — license tooltips are advisory only.** NinjaScript Editor, NinjaScript Output, Strategy Builder, Strategy Analyzer, and Global Simulation Mode show a "Please upgrade to a Lease or Lifetime license to unlock this feature" tooltip, **but every one that was opened (Editor, Analyzer) opened and functioned normally**. The gating is advisory/tooltip-only in this install, not enforced.

**Menu contents captured live (use these, not guesses):**

- **New menu** ([`09-new-menu.png`](assets/nt8-2026-07-24/09-new-menu.png)): Basic Entry · FX Pro · Option Chain · Order Ticket · SuperDOM Dynamic · SuperDOM Static · Alerts Log · Calendar · **Chart** · Depth Chart · FX Board · FX Correlation · Hot List Analyzer · Level II · Market Analyzer · Market Watch · News · Pulse · **Strategy Analyzer** · T&S · Account Data · Trade Performance · **NinjaScript Editor** · NinjaScript Output · Strategy Builder.
- **Tools menu** (from notes): Instruments · Instrument Lists · Database Management · Hot Keys · **Historical Data** · Commissions · Risk · **Trading Hours** · Import · Export · Remove NinjaScript Assembly… · Global Simulation Mode *(license-gated)* · Client Dashboard · Settings.
- **Connections menu** ([`20-connections-menu.png`](assets/nt8-2026-07-24/20-connections-menu.png)): Kinetick – End Of Day (Free) · Playback · Simulated Data Feed *(green = connected, "disconnect" link)* · Simulation *("configure" link)*.

---

## 1. UI Layout / Windows

### 1a. Control Center
- **What it's for:** root window, always open while NT8 runs; centralized view of accounts, orders, executions, positions, logs; toggles global app features.
- **Open:** appears on launch; if minimized to tray, restore from the taskbar/tray icon.
- **Tabs & purpose:**
  - **Orders** — working/filled/rejected orders (Instrument, Action, Type, Qty, Limit, Stop, State, Filled…). Double-click to modify qty/price inline; right-click to cancel. ([`03-cc-orders.png`](assets/nt8-2026-07-24/03-cc-orders.png))
  - **Executions** — individual fills. ([`04-cc-executions.png`](assets/nt8-2026-07-24/04-cc-executions.png))
  - **Strategies** — every NinjaScript strategy running against an account or chart; enable/disable and monitor. ⚠️ **LIVE:** this is the *Control Center* Strategies grid — distinct from the per-chart Strategies dialog in §5. ([`05-cc-strategies.png`](assets/nt8-2026-07-24/05-cc-strategies.png))
  - **Positions** — open positions per account; right-click to close/flatten. ([`06-cc-positions.png`](assets/nt8-2026-07-24/06-cc-positions.png))
  - **Accounts** — account rows incl. **Sim101** (cash, P&L, buying power); right-click to Edit/Reset a sim account. ([`07-cc-accounts.png`](assets/nt8-2026-07-24/07-cc-accounts.png))
  - **Log** — **where import errors and compile/connection issues surface — check here first when something fails silently.** ([`01-control-center-log.png`](assets/nt8-2026-07-24/01-control-center-log.png))
  - **Messages** — system/vendor messages. ([`08-cc-messages.png`](assets/nt8-2026-07-24/08-cc-messages.png))
- Cite: https://ninjatrader.com/support/helpguides/nt8/control_center.htm

### 1b. NinjaScript Editor
- **What it's for:** create/compile custom indicators and strategies (C# / NinjaScript). Includes NinjaScript Explorer tree, Wizard, Intelliprompt, code snippets, compile-error panel, Visual Studio debugging hooks.
- **Open:** `New > NinjaScript Editor`.
- ⚠️ **LIVE toolbar** ([`10-ninjascript-editor.png`](assets/nt8-2026-07-24/10-ninjascript-editor.png)): Print · Print Preview · NinjaScript Output · Find · **Compile** · Open in Visual Studio. The Explorer tree is on the left.
- Cite: https://ninjatrader.com/support/helpguides/nt8/editor.htm

### 1c. Strategy Analyzer
- **What it's for:** runs historical analysis (backtest / optimization / walk-forward) on NinjaScript strategies. See §4.
- **Open:** `New > Strategy Analyzer`. ([`11-strategy-analyzer.png`](assets/nt8-2026-07-24/11-strategy-analyzer.png))
- Cite: https://ninjatrader.com/support/helpguides/nt8/strategy_analyzer.htm

### 1d. Chart
- **What it's for:** price chart with intervals, indicators, drawing tools, discretionary trading via **Chart Trader**, and automated trading via NinjaScript strategies.
- **Open:** `New > Chart` (✅ confirmed live — "Chart" is in the New menu; capture opened on `MNQ SEP26`, Daily). ([`12-chart-mnq-sep26.png`](assets/nt8-2026-07-24/12-chart-mnq-sep26.png))
- ⚠️ **SAFETY:** the chart carries **Chart Trader** with live Buy Mkt / Sell Mkt buttons. During capture it was opened accidentally and closed immediately with no button clicked — treat chart-canvas clicks near the right edge with care.
- Cite: https://ninjatrader.com/support/helpguides/nt8/charts.htm

### 1e. Historical Data window
- **What it's for:** access/manage all historical + Market Replay data; Import, Export, Download, and inspect Loaded data.
- **Open:** `Tools > Historical Data`.
- ⚠️ **LIVE — CORRECTION to the Help Guide:** in 8.1.7.2 this window is a **vertical accordion** with stacked expand/collapse sections **Loaded · Download · Import · Export · Get Market Replay data** — **not** the horizontal Import/Export/Edit/Download *tab* strip the public Guide implies. ([`15-historical-data-loaded.png`](assets/nt8-2026-07-24/15-historical-data-loaded.png))
- Cite: https://ninjatrader.com/support/helpguides/nt8/historical_data_manager.htm

### 1f. Instruments manager
- **What it's for:** add/remove/edit instruments in the local DB (single master instance shared across providers); per-instrument settings (e.g. Merge Policy). ([`18-instruments-manager.png`](assets/nt8-2026-07-24/18-instruments-manager.png))
- **Open:** `Tools > Instruments`. Grid columns: Name / Type / Description, with an "All" filter and a search box; add/edit/remove at the bottom.
- Cite: https://ninjatrader.com/support/helpguides/nt8/instruments.htm

### 1g. Instrument Lists
- **What it's for:** manage named instrument lists. ⚠️ **LIVE:** built-in lists in this install are Cryptocurrency · DAX 30 · DOW 30 · FOREX · Futures · Indexes · Micros · NASDAQ 100 · SP 500. ([`19-instrument-lists.png`](assets/nt8-2026-07-24/19-instrument-lists.png))
- **Open:** `Tools > Instrument Lists`.

### 1h. Connections
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

**Open editor:** `New > NinjaScript Editor`; open (or create via the NinjaScript Wizard) the strategy `.cs` file.

**Compile:**
- Press **F5**, **or** right-click in the editor → **"Compile"**. ⚠️ **LIVE:** the Editor toolbar has a **Compile** button; the notes confirm **F5** as the compile shortcut on this install.
- Compilation compiles **ALL** NinjaScript files in the library, not just the open file.

**Where compile errors surface:**
- An **error-list panel at the bottom** of the Editor: each row = **filename**, **description**, **line/column**. Open-file errors render lighter; other-file errors darker.
- Offending code gets a **red wavy underline**.
- **Double-click an error row** → jumps to the spot. **Click the error code** → opens Help for that code.
- Compile messages also echo to the Control Center **Log** tab.

- Cite: https://ninjatrader.com/support/helpguides/nt8/editor.htm · https://ninjatrader.com/support/helpguides/nt8/compile_errors.htm · https://ninjatrader.com/support/helpguides/nt8/how_do_i_resolve_ninjascript_p.htm

---

## 4. Configure + Run Strategy Analyzer (Backtest)

**Open:** `New > Strategy Analyzer`. Top control **Backtest type = "Backtest"** (also Optimization / Multi-Objective / Walk-Forward). ([`11-strategy-analyzer.png`](assets/nt8-2026-07-24/11-strategy-analyzer.png))

**Configuration (left-hand properties):**
1. **Strategy** — pick your compiled strategy. ⚠️ **LIVE:** `PraxisNoiseAreaBreakout` appears under custom category **"02. Praxis (tunable)"**.
2. **Parameters (…)** — the strategy's user inputs.
3. **Data Series:** **Instrument** (e.g. `NQ 12-25` or continuous `NQ ##-##`) · **Price based on** (Last/Bid/Ask) · **Type** (Minute/Tick/Range…) · **Value** (e.g. 1 for 1-minute).
4. **Time frame:** **Start date** / **End date** · **Trading hours** = **session template dropdown** — for PRAXIS RTH select **"CME US Index Futures RTH"** · **Break at EOD**.
5. **Execution:** Include commission · Order fill resolution · Slippage (ticks) · Bars required to trade · Max bars look back · Entry handling.

**Run:** click **"Run"**. Results populate the Analyzer's output area (performance summary, trades list, equity/chart, executions).

- Cite: https://ninjatrader.com/support/helpguides/nt8/backtest_a_strategy.htm · https://ninjatrader.com/support/helpguides/nt8/strategy_analyzer_layout.htm
- 🔲 **TODO (residual gap):** the **"CME US Index Futures RTH"** template's exact printed session hours were **not** captured. Verify **09:30–16:00 ET** equivalence via `Tools > Trading Hours` and record the printed CT hours here. (Tracked in the follow-up bead — see footer.)

---

## 5. Add a Strategy to a Chart on Sim101

**Precondition:** strategy compiled (§3); a chart open (`New > Chart`).

**Steps:**
1. Open the **Strategies** window from the chart: right-click the chart → **"Strategies"**, or the chart-toolbar **Strategies** icon, or **CTRL + S**. ([`14-chart-strategies-dialog.png`](assets/nt8-2026-07-24/14-chart-strategies-dialog.png))
2. In **"Available"**, select the strategy → add (or double-click) → moves to **"Configured"**. ⚠️ **LIVE Available list:** `PraxisNoiseAreaBreakout`, `PraxisSignalConsumer`, Sample ATM, Sample MA crossover, Sample multi-instrument, Sample multi-timeframe.
3. In the Configured instance set: **Data Series** · **Account = Sim101** · **Strategy Parameters** · **Calculate** mode.
4. Set **"Enabled" = True** to run (False = attached but inactive).
5. **"OK"** to apply.

**Enable/disable later:** flip **Enabled** in the chart Strategies window, or from the Control Center **Strategies** tab. **"Remove"** detaches entirely.

**⚠️ Account-change safety:** account persists only on already-configured instances (no global default). To change accounts: **Disable → change Account → re-Enable** to avoid orphaned working orders.

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
- **Flatten everything** (all positions + all orders, all accounts): `Positions` tab → right-click → **"Flatten Everything"**.
- **Close one position:** `Positions` tab → right-click → **"Close Position"**.
- **From a chart:** Chart Trader Close/Flatten controls for the chart's account.

**Reset Sim101** (clears sim state between backtests): `Accounts` tab → right-click **Sim101** → **Edit** → set **"Initial cash"** → **"Reset"**. (Sim accounts are USD-only.)

- Cite: https://ninjatrader.com/support/helpguides/nt8/orders_tab.htm · https://ninjatrader.com/support/helpguides/nt8/the_sim101_account.htm
- 🔲 **TODO:** `orders_tab.htm` confirms **"Cancel Order"** / **"Cancel All Orders"** directly; the exact right-click wording of **"Flatten Account"** / **"Flatten Everything"** / **"Close Position"** should be verified against the live 8.1.7.2 context menus.

---

## Residual gaps (for a future capture pass)
1. `Tools > Trading Hours` — exact printed hours of the **CME US Index Futures RTH** template (confirm 09:30–16:00 ET). *(§4)*
2. Historical Data **Export** and **Get Market Replay data** accordion sections — not expanded/captured. *(§1e)*
3. `.zip` direct-import support — undocumented, untested. *(§2)*
4. Exact right-click wording for **Flatten Account / Flatten Everything / Close Position**. *(§7)*

## Asset index
All raw captures + the coworker's original capture log: [`assets/nt8-2026-07-24/`](assets/nt8-2026-07-24/) (20 PNGs `01`–`20` + `00-coworker-capture-notes.txt`).

## Help Guide source index
Control Center · Editor · Compile errors · Strategy Analyzer · Backtest a Strategy · Analyzer layout · Charts · Running a strategy from a chart · Historical Data manager · Importing · Instruments · Merge policy · Connections menu · Sim101 · Orders tab — all under `https://ninjatrader.com/support/helpguides/nt8/<page>.htm` (see per-section cites). Blocked slugs found during research: `historical_data.htm` (404 → use `historical_data_manager.htm`), `futures.htm` (404 → covered via `instruments.htm` + `merge_policy.htm`).
