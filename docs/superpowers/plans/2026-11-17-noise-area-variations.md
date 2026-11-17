# Noise-Area Variations Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Find out whether any variation of the Noise-Area breakout passes Amear's five bars on the held NQ 1-minute data, and name a finalist or say none passed.

**Architecture:** A small Globex-day loader and a band module feed two programs: a measuring pass that places no trades, and a backtest engine driven by one locked settings file per variation. A separate gates module judges each trade list. The lead session fixes the variation list between the two programs and recomputes every bar itself.

**Tech Stack:** Python 3, standard library only, `unittest`. Every command is run as `python3 -I -B <file>` from the repo root.

**Spec:** `docs/superpowers/specs/2026-11-17-noise-area-variations-design.md`. Read it first. Amear's rulings: `RULINGS.md`, last section.

## Who does what

Amear asked for a tester and a checking orchestrator (RULINGS.md, 2026-11-17). Helper agents are spawned with the Agent tool, `subagent_type: "general-purpose"`.

| Role | Tasks | Agent call |
|---|---|---|
| Lead (the session Amear starts; Fable 5.2, high effort) | 0, 4, 7, 9, and the gate at the end of every other task | none: the session itself. Writes no engine code. |
| Tester | 1, 2, 3, 5, 6, and the runs in 4 and 8 | `model: "opus"`, `effort: "high"` |
| Checker | the check steps in 3, 6 and 8 | `model: "fable"`, `effort: "high"`. A fresh agent each time. It is never the agent that wrote the code. |

The lead gives each agent its task text from this plan plus the spec path. The checker gets the code and the rule it must match. It never gets the tester's summary or the lead's expectation. Checks are about numbers and rules, never the form of a report. A failed check is a failed test: the tester fixes it and the check is rerun.

## Global Constraints

- Standard library only. Run as `python3 -I -B`.
- Data file: `os.environ.get("PRAXIS_DATA", "/Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt")`. Lines are `YYYYMMDD HHMMSS;open;high;low;close;volume`. Stamps are Eastern time and mark the end of the minute.
- Range: trading days 2021-03-08 to 2026-07-17. Measuring pass: 2021-03-08 to 2023-12-31 only. Later years: 2024-01-01 to 2026-07-17.
- Instrument: MNQ. `PV = 2.0` dollars a point, `COMM = 1.90` dollars a contract round trip, `TICK = 0.25`, `SLIP = 0.5` points (2 ticks) per side.
- Account: `START = 50000.0`, `LIMIT = 2000.0`. Information-only runs at `START = 10000.0`.
- Shuffle: 10,000 runs, seed 20261115, using `trailing` and `shuffled` from `research/intraday-momentum-long/run.py` unchanged.
- Every variation is flat by the bar stamped 16:00 at the latest. No entry is decided on a bar stamped after 15:59 or before 18:01.
- No backtest result is looked at before the settings file that produced it is committed.
- All work in its own git worktree on branch `noise-area-variations`. Code in `research/noise-area-variations/`. Commit after every task and push.
- No timestamp is typed by hand. No email address, phone number or support-staff name in any file.
- Anything Amear reads is plain English with dollar figures.

## Review Focus

Each line has a test in the task named.

1. A half day or holiday whose last bar is before 15:59: an open position is closed at that day's last bar, never carried over. (Task 5)
2. A bar that opens beyond the stop: the stop fills at the open, the loss is above the planned cost, and the trade is marked `gap: true`, not counted as a rule break. (Task 5)
3. A balance too small for one contract at the stop distance, or a stop distance under 10 points: the signal is skipped and counted, never traded at a smaller risk than stated or a bigger one. (Task 5)
4. A day whose 18:01 bar is missing (late Sunday open, data hole): the 6 PM band does not exist that day and no 6 PM-anchored trade is taken. (Task 2)
5. An entry window that crosses midnight (for example 18:00 to 02:00): bars after midnight belong to the same trading day as the evening before. (Task 1 and Task 5)

## File structure

All in `research/noise-area-variations/`:

| File | Responsibility |
|---|---|
| `globex.py` | Load the data file into trading days that run 18:01 to 17:00. |
| `bands.py` | The noise band and VWAP for one day, anchored at 9:30 or at 6:00 PM. |
| `measure.py` | The measuring pass. No trades, no account. |
| `engine.py` | Settings validation and the backtest simulator. |
| `gates.py` | The five bars and the statistics, from a trade list. |
| `run_all.py` | Run every settings file in `variations/` and write results. |
| `lead_check.py` | Written by the lead in Task 8. Recomputes the bars from raw trade lists. |
| `variations/*.json` | One locked settings file per variation. Written by the lead in Task 7. |
| `out/` | Results. Committed. |
| `test_*.py` | One test file per module. |

---

### Task 0: Workspace (lead)

- [ ] **Step 1:** Read `STATUS.md`, `RULINGS.md`, the spec and this plan.
- [ ] **Step 2:** Create the worktree with the superpowers:using-git-worktrees skill, branch `noise-area-variations`, from `main`.
- [ ] **Step 3:** Run `bd update Praxis_build-7yq --claim`.
- [ ] **Step 4:** Confirm the data file exists and `python3 -I -B research/noise-area-stop/test_retest.py` passes in the worktree. This proves the existing loader and data are intact before anything new is built.

### Task 1: Globex-day loader (tester)

**Files:** Create `research/noise-area-variations/globex.py`, `research/noise-area-variations/test_globex.py`.

**Interfaces — produces:**

```python
class Bar:      # __slots__ = ("dt", "sm", "o", "h", "l", "c", "v")
    # dt: datetime of the stamp. sm: minutes after 18:00 of the trading day's evening.
    # The bar stamped 18:01 has sm 1; 00:00 has sm 360; 09:31 has sm 931; 16:00 has sm 1320.
class Day:      # __slots__ = ("date", "bars", "by_sm")
    # date: 'YYYY-MM-DD' of the trading day (the day the 9:30 open belongs to).
    # bars: Bar list in stamp order, stamps 18:01 (previous calendar day) to 16:00 only.
    # by_sm: dict sm -> index into bars.
def sm_of(hhmm: str) -> int            # '18:01' -> 1, '02:00' -> 480, '09:31' -> 931, '16:00' -> 1320
def load_days(path: str, start: str = "2021-03-08", end: str = "2026-07-17") -> list[Day]
```

Rules: a bar stamped 18:01 to 23:59 belongs to the next weekday's trading day (Friday evening does not exist; Sunday evening belongs to Monday). Bars stamped 16:01 to 18:00 are dropped. A trading day is kept only if it is Monday to Friday and has at least one bar. Out-of-order or duplicate stamps raise `ValueError`.

- [ ] **Step 1: Write the failing tests** in `test_globex.py`. Tests build small data files in a temp directory.

```python
def test_sm_of(self):
    self.assertEqual([g.sm_of(x) for x in ("18:01", "00:00", "02:00", "09:31", "16:00")], [1, 360, 480, 931, 1320])
def test_sunday_evening_belongs_to_monday(self):      # bars 20210307 180100 and 20210308 093100
    days = g.load_days(path); self.assertEqual([d.date for d in days], ["2021-03-08"]); self.assertEqual(len(days[0].bars), 2)
def test_bar_after_midnight_same_trading_day(self):   # 20210308 230000 and 20210309 010000 -> both in 2021-03-09 (Review Focus 5)
def test_break_bars_dropped(self):                    # 163000 and 180000 stamps are not loaded
def test_duplicate_stamp_raises(self):
def test_real_file_matches_rth_loader(self):          # skip if no data file
    # for every session date of market.load_market(DATA, session_start="09:31"), the Day with that date has
    # the same bars (o,h,l,c,v) for stamps 09:31..that session's last bar. Count of dates compared > 1300.
```

- [ ] **Step 2:** Run `python3 -I -B research/noise-area-variations/test_globex.py`. Expected: fails, no module `globex`.
- [ ] **Step 3:** Implement `globex.py` to the interface above.
- [ ] **Step 4:** Run the tests. Expected: all pass.
- [ ] **Step 5:** Commit: `research: Globex-day loader for the Noise-Area variation search`.

### Task 2: Bands at both anchors (tester)

**Files:** Create `bands.py`, `test_bands.py`.

**Interfaces — consumes:** `globex.Day`, `globex.sm_of`. **Produces:**

```python
class BandPoint:   # __slots__ = ("upper", "lower", "vwap", "anchor_price", "width")   width = anchor_price * mult * sigma
def day_bands(days: list[Day], k: int, anchor: str, lookback: int = 14, mult: float = 1.0) -> dict[int, BandPoint]
    # anchor is "0930" or "1800". Returns sm -> BandPoint for day index k, only for minutes that have a band.
```

Rules for `"0930"`: exactly the published rule as coded in `scripts/wf/oracle/band.py` at `session_start="09:31"`. The open is the open of the bar stamped 09:31. The reference prices are the larger and the smaller of that open and the previous day's last bar close. Sigma at a minute is the mean, over the most recent `lookback` earlier days that have that minute, looking back at most `lookback + 15` days, of `abs(close_at_minute / open - 1)`. No band before 09:31. VWAP runs from the 09:31 bar using `(h + l + c) / 3`.

Rules for `"1800"`: the anchor price is the open of the bar stamped 18:01, with no previous-close adjustment. `upper = open * (1 + mult * sigma)`, `lower = open * (1 - mult * sigma)`. Sigma uses each earlier day's own 18:01 open. VWAP runs from the 18:01 bar. A day with no 18:01 bar has no band and is not used in other days' sigma.

- [ ] **Step 1: Write the failing tests.**

```python
def test_0930_reproduces_band_py_on_real_file(self):   # skip if no data file
    # for 60 dates spread evenly over the range and every minute 09:31..16:00: upper, lower and vwap equal
    # scripts/wf/oracle/band.py iter_session_states(market, n, 14, 1.0) to 1e-9, and a band exists exactly when have_band.
def test_1800_sigma_by_hand(self):       # 15 synthetic days, constant +1% move at sm 60 -> sigma 0.01, upper = open * 1.01
def test_1800_needs_14_days(self):       # day index 13 has no band, day index 14 has one
def test_missing_1801_bar_no_band(self): # Review Focus 4: that day returns {} and is skipped in later days' sigma
def test_no_lookahead(self):             # changing every bar of day k+1 leaves day_bands(days, k, ...) unchanged;
                                         # changing day k's bars after sm S leaves BandPoints at sm <= S unchanged
```

- [ ] **Step 2:** Run. Expected: fails, no module `bands`.
- [ ] **Step 3:** Implement `bands.py`.
- [ ] **Step 4:** Run. Expected: all pass.
- [ ] **Step 5:** Commit: `research: noise bands anchored at 9:30 and at 6 PM; the 9:30 band reproduces the existing one`.

### Task 3: The measuring pass (tester, then checker)

**Files:** Create `measure.py`, `test_measure.py`.

**Interfaces — consumes:** `globex.load_days`, `bands.day_bands`. **Produces:**

```python
STOPS = ("half_width", "full_width", "to_anchor", "opposite_band")
PARTS = (("evening", "18:00", "02:00"), ("overnight", "02:00", "09:30"), ("morning", "09:30", "11:30"),
         ("midday", "11:30", "14:00"), ("afternoon", "14:00", "16:00"))   # a decision stamp T is in a part when start < T <= end
MIN_STOP_POINTS = 10.0
def events(days, anchor: str, cadence: str) -> list[dict]     # cadence "half_hour" or "minute"
def tables(evts: list[dict]) -> list[dict]
def main(argv=None) -> int   # --start --end --out ; default range 2021-03-08 .. 2023-12-31, out research/noise-area-variations/out/measure
```

An event is the first decision bar whose close is outside the band after a decision bar whose close was inside it, or the day's first decision bar with a band if that close is already outside. Decision bars are every bar with a band (`minute`) or those stamped `:00` and `:30` (`half_hour`), up to the bar stamped 15:59. The reference entry price is the open of the next bar, with no slippage. For each stop kind the distance is: half or all of `width`; the gap from the reference price to `anchor_price`; the gap from the reference price to the opposite band at the decision bar. From the entry bar to the day's last bar at or before 16:00, in order: if the bar's adverse extreme reaches the stop, the event is stopped and that bar's favourable move is not counted; otherwise the best favourable move so far is updated.

Each event dict has `date, time, sm, part, side, anchor, cadence, width, ref` and per stop kind `dist, tight (dist < 10.0), stopped, mfe_r, r_at_flat` (`-1.0` when stopped), `reached_2, reached_3, reached_5`.

Each table row has `anchor, cadence, stop, part, side, n, tight_excluded, pct_reached_2, pct_reached_3, pct_reached_5, avg_r_at_flat, max_gap_trading_days`. Tight events are left out of the percentages and counted in `tight_excluded`. `max_gap_trading_days` is the longest run of trading days with no event in that part.

`main` writes `events-<anchor>-<cadence>.json`, `tables.json`, and `tables.md` (plain-English column names, one table per stop kind).

- [ ] **Step 1: Write the failing tests** on synthetic days with a hand-built band (patch `bands.day_bands`).

```python
def test_one_event_per_excursion(self):        # 5 closes outside in a row -> 1 event; back inside then outside -> 2
def test_half_hour_ignores_other_minutes(self):# breakout at 10:17 held to 10:30 -> event time '10:30'
def test_mfe_and_stop_order(self):             # long, dist 20: bars run +50 then -25 -> stopped, mfe_r 2.5, reached_2 True, reached_3 False, r_at_flat -1.0
def test_stop_bar_favourable_move_not_counted(self): # a bar with high +100 and low at the stop -> stopped, mfe_r excludes that bar
def test_tight_excluded(self):                 # dist 6 -> tight True, absent from pct_reached_2, counted in tight_excluded
def test_parts(self):                          # stamps 18:01, 02:00, 02:01, 09:30, 09:31, 11:30, 14:00, 14:01 -> evening, evening, overnight, overnight, morning, morning, midday, afternoon
def test_range_guard(self):                    # main() refuses --end later than 2023-12-31 unless --allow-later is given; exit code 2
def test_same_twice(self):                     # two runs give byte-identical tables.json
```

- [ ] **Step 2:** Run. Expected: fails, no module `measure`.
- [ ] **Step 3:** Implement `measure.py`.
- [ ] **Step 4:** Run. Expected: all pass.
- [ ] **Step 5:** Commit: `research: the measuring pass (no trades), tests only, not yet run on the data`.
- [ ] **Step 6: Check (checker).** Brief: "Read `globex.py`, `bands.py`, `measure.py` and the spec's Stage 1. Find any place where a value at minute T depends on a bar after T, or on a later day. Find any place the code departs from the spec's definition of a breakout or of the stop distances. Then take 10 events you choose at random from a run you make yourself on 2021-06 only (`--start 2021-06-01 --end 2021-06-30 --out` a scratch directory) and re-derive each by hand from the raw data file. Report defects with file, line and evidence, or 'no defects found'." Fix and recheck until clean.

### Task 4: Run the measuring pass (tester runs, lead reads)

- [ ] **Step 1 (tester):** Run `python3 -I -B research/noise-area-variations/measure.py`. Run it a second time into a scratch directory and confirm `tables.json` is byte-identical.
- [ ] **Step 2 (tester):** Commit `out/measure/`: `research: measuring pass on 2021-03-08 to 2023-12-31, <N> breakouts, no trades`.
- [ ] **Step 3 (lead):** Read `tables.md`. Write `out/measure/READING.md`: in plain English, where breakouts reach twice the risk most often, where they do not, and which parts of the day have gaps longer than seven trading days. No variation is named yet.

### Task 5: The backtest engine (tester)

**Files:** Create `engine.py`, `test_engine.py`.

**Interfaces — consumes:** `globex`, `bands`. **Produces:**

```python
MIN_STOP_POINTS = 10.0
def validate(settings: dict, allow_no_stop: bool = False) -> dict    # returns it, or raises ValueError naming the field
def run(days, settings: dict, fill: str = "harsh-stops", start: float = 50000.0, allow_no_stop: bool = False) -> dict
    # fill is "kind" or "harsh-stops". Returns {"settings", "fill", "start", "trades", "days", "skipped", "digest"}
```

A settings file has exactly these fields:

```json
{"name": "V1", "reason": "one line from the measuring pass",
 "anchor": "0930", "lookback": 14, "band_mult": 1.0,
 "cadence": "half_hour", "entry_window": ["09:31", "15:30"], "sides": "both",
 "reentry": "any",
 "stop": {"kind": "half_width"},
 "exit": {"kind": "band_or_vwap"},
 "max_trades_per_day": 3, "risk_pct": 1.0, "flat_time": "15:59"}
```

Allowed values: `anchor` `"0930"|"1800"`; `cadence` `"half_hour"|"minute"`; `sides` `"both"|"long"|"short"`; `reentry` `"any"|"fresh"` (`fresh`: after any exit, no new entry on that side until a decision bar has closed inside the band); `stop.kind` `"half_width"|"full_width"|"to_anchor"|"opposite_band"|"width_frac"` (`width_frac` needs `"value"` between 0.1 and 3.0), and `"none"` only with `allow_no_stop=True`; `exit.kind` `"band_or_vwap"|"hold_to_flat"|"trail_r"` (`trail_r` needs `"value"` between 0.5 and 5.0); `max_trades_per_day` 1 to 10; `risk_pct` 0.1 to 2.0; `flat_time` no later than `"15:59"`; `entry_window` two decision-bar stamps inside the trading day, the first earlier than the second in trading-day order, the second no later than `flat_time`. Unknown fields raise.

Simulator rules, in this order on each bar:

1. **Resting stop.** If a position is open and the bar's adverse extreme reaches the stop, the stop fills. `kind`: at the stop level, or the bar's open if the open is already beyond it (then `gap: true`), 2 ticks against, kept inside the bar's range. `harsh-stops`: at the bar's low for a long, its high for a short. Nothing else happens on that bar.
2. **Flat.** On the bar stamped `flat_time` or later, or on the day's last bar, an open position is closed: at the next bar's open, 2 ticks against, if a next bar exists in the day; otherwise at this bar's close, 2 ticks against. No entry on such a bar.
3. **Decision bar** (per `cadence`, with a band). Exit first: `band_or_vwap` closes a long when `close <= max(upper, vwap)` and a short when `close >= min(lower, vwap)`; a position is also closed when the opposite entry signal fires. Then entry, if the bar is inside `entry_window`, the day's trade count is under `max_trades_per_day`, and `reentry` allows: long when `close > upper` and not long; short when `close < lower` and not short. Orders fill at the next bar's open, 2 ticks against.
4. **`trail_r`.** At each bar close the stop is moved to `best favourable price since entry -/+ value * dist`, only ever toward the price. It takes effect on the next bar.

Stop and size, fixed at the decision bar: `dist` is the stop kind's distance measured from the decision bar's close, rounded down to a tick. The stop rests at `entry fill -/+ dist`. `loss_per_contract = (dist + 0.5) * 2.0 + 1.90`. `qty = floor(balance * risk_pct / 100 / loss_per_contract)`. `planned_cost = qty * loss_per_contract`. If `dist < 10.0` or `qty < 1`, the signal is skipped and added to `skipped` with its reason; it does not count toward `max_trades_per_day`.

Each trade dict: `entry_dt, exit_dt, date, side, qty, entry, exit, stop_initial, dist, planned_cost, reason ("stop"|"exit"|"reverse"|"flat"), gap, net, r (net / planned_cost), balance`. `net = (exit - entry) * side_sign * 2.0 * qty - 1.90 * qty`.

Each day dict: `{"date", "start", "end", "low"}` as in `research/intraday-momentum-long/run.py`: `low` is the lowest the balance reached that day with an open position marked at each bar's adverse extreme.

`digest` is the sha256 of the JSON of `trades`.

- [ ] **Step 1: Write the failing tests.**

```python
def test_validate_rejects(self):            # each of: unknown field, stop none without the flag, flat_time 16:00, risk_pct 3, window end after flat_time
def test_entry_fill_and_stop_offset(self):  # long decided at close 100.00, next open 101.00, dist 20 -> entry 101.50, stop_initial 81.50
def test_size_and_planned_cost(self):       # balance 50000, risk 1.0, dist 20 -> loss_per_contract 42.90, qty 11, planned_cost 471.90
def test_kind_stop_loss_equals_planned(self):   # stopped inside the bar -> net == -planned_cost to the cent, gap False, r == -1.0
def test_gap_through_stop(self):            # Review Focus 2: bar opens 5 points beyond the stop -> exit at open - 0.5, gap True, net < -planned_cost
def test_harsh_stop_fills_at_low(self):
def test_skips(self):                       # Review Focus 3: dist 8 -> skipped "stop under 10 points"; balance 100 -> skipped "under one contract"; neither counts toward max_trades_per_day
def test_half_day_flat_at_last_bar(self):   # Review Focus 1: day's last bar 13:00, position open -> closed at that bar's close, reason "flat"
def test_window_across_midnight(self):      # Review Focus 5: anchor 1800, window 18:01..02:00 -> entry at 01:30 allowed, at 02:30 refused, trade date is the trading day
def test_max_trades_per_day(self):
def test_fresh_reentry(self):               # stopped while still outside the band: "any" re-enters at the next decision bar, "fresh" does not
def test_trail_r_only_tightens(self):
def test_stop_bar_does_nothing_else(self):  # a decision bar that also hits the stop: stop fills, no exit order, no new entry
def test_day_low_marks_adverse_extreme(self):
def test_no_lookahead(self):                # altering all bars after bar B leaves every trade with exit_dt <= B's stamp unchanged
def test_same_twice(self):                  # two runs, same digest
def test_baseline_matches_retest(self):     # skip if no data file. Settings: anchor 0930, half_hour, window 09:31..15:30... see below
```

`test_baseline_matches_retest`: with `stop none` (`allow_no_stop=True`), `exit band_or_vwap`, `sides both`, `reentry any`, `max_trades_per_day 10`, `flat_time "15:59"`, `entry_window ["09:31", "15:30"]`, the list of `(side, entry_dt, entry, exit_dt, exit)` equals the trade list of `research/noise-area-stop/retest.py` run as Flat1559, session start 09:31, no stop, kind fills. (retest decides only on bars stamped :00 and :30 after 09:30 and before 16:00.) This test ties the new engine to the simulator that already reproduces NinjaTrader trade for trade.

- [ ] **Step 2:** Run. Expected: fails, no module `engine`.
- [ ] **Step 3:** Implement `engine.py`.
- [ ] **Step 4:** Run. Expected: all pass.
- [ ] **Step 5:** Commit: `research: variation backtest engine; baseline settings reproduce the Nov 15 retest trade for trade`.

### Task 6: The bars (tester, then checker)

**Files:** Create `gates.py`, `run_all.py`, `test_gates.py`.

**Interfaces — consumes:** `engine.run` output; `trailing`, `shuffled` from `research/intraday-momentum-long/run.py` (import by adding that directory to `sys.path`). **Produces:**

```python
LATER_FROM = "2024-01-01"
def rule_check(result: dict, days) -> list[str]     # list of breaks, empty when clean
def judge(result: dict, all_dates: list[str]) -> dict
def run_all(variation_dir: str, out_dir: str) -> int   # run_all.py main
```

`rule_check` replays each trade against the bars and the settings and reports: no stop at entry; `stop_initial` not `dist` from `entry`; a bar between entry and exit whose adverse extreme reached the stop; on a `kind` result, a stop loss above `planned_cost` by more than one cent with `gap` false; `qty` or `planned_cost` not matching the size rule for the balance before the trade; an entry outside `entry_window`, after `flat_time`, or over `max_trades_per_day`; an exit after the bar stamped 16:00.

`judge` returns:

```python
{"rule_check": {"pass": bool, "breaks": int},
 "two_to_one": {"pass": bool, "avg_winner_r": float, "later_avg_winner_r": float, "later_net": float},
      # pass: avg_winner_r >= 2.0 and later_avg_winner_r >= 2.0 and later_net > 0. Winners are trades with net > 0.
 "frequency": {"pass": bool, "max_gap_trading_days": int, "gap_from": str, "gap_to": str},
      # longest run of consecutive dates in all_dates with no trade entered; pass when <= 7
 "profit": {"pass": bool, "net": float},                    # pass: net >= 2 * 2000
 "survival": {"pass": bool, "first_cross": str | None, "shuffle_pct": float},
      # pass: first_cross is None and shuffle_pct <= 5.0
 "overall": bool,
 "stats": {"trades", "win_pct", "avg_winner_dollars", "avg_loser_dollars", "avg_loser_r", "longest_losing_run",
           "worst_drop_dollars", "skipped", "stops_over_planned", "worst_stop_vs_planned", "by_year"}}
```

`run_all` runs each settings file four times (`kind` and `harsh-stops`, start 50,000 and 10,000), each twice to compare digests, and writes `out/variations/<name>/<fill>-<start>.json` (the full result) and `out/variations/<name>/judge.json` (the `harsh-stops` 50,000 result judged, with `rule_check` also run on the `kind` 50,000 result). It refuses to run if `git status --porcelain research/noise-area-variations/variations` shows any uncommitted settings file.

- [ ] **Step 1: Write the failing tests.**

```python
def test_two_to_one_boundary(self):      # winners' r [1.5, 2.5] -> avg 2.0 pass; [1.5, 2.4] -> fail
def test_two_to_one_needs_later_years(self):  # full avg 2.5 but later winners avg 1.8 -> fail; later_net <= 0 -> fail
def test_frequency_boundary(self):       # 7 trading days with no entry between two trades -> pass; 8 -> fail, with gap_from and gap_to
def test_frequency_counts_start_and_end(self):  # no trade in the first 8 trading days -> fail
def test_profit_boundary(self):          # 4000.00 pass, 3999.99 fail
def test_survival_real_cross_fails(self):# shuffle 0% but first_cross set -> fail
def test_survival_boundary(self):        # 5.0 pass, 5.1 fail (patch shuffled)
def test_overall_needs_all(self):
def test_rule_check_catches(self):       # one tampered trade per break listed above -> each reported
def test_run_all_refuses_uncommitted(self):
```

- [ ] **Step 2:** Run. Expected: fails, no module `gates`.
- [ ] **Step 3:** Implement `gates.py` and `run_all.py`.
- [ ] **Step 4:** Run all five test files. Expected: all pass.
- [ ] **Step 5:** Commit: `research: the five bars and the runner for the variation search`.
- [ ] **Step 6: Check (checker).** Brief: "Read `engine.py`, `gates.py`, `run_all.py`, the spec's bars table and 'Calls made by Claude', and this plan's Task 5 and Task 6 rules. Find: any use of a bar after the decision bar in a decision; any order the simulator can place that the rules do not allow; any path where a position has no resting stop; any way a loss at the stop can exceed the planned cost on kind fills without `gap`; any bar in `judge` that is computed differently from its written rule. Build your own three-day synthetic file and a settings file, work the expected trades out by hand, and compare with `engine.run`. Do not run anything on the real data file. Report defects with file, line and evidence, or 'no defects found'." Fix and recheck until clean.

### Task 7: Fix the list (lead)

- [ ] **Step 1:** From `out/measure/tables.md` and `READING.md` only, write at most eight settings files in `variations/`, named `V1.json` to `V8.json`. Each `reason` field cites the table rows it rests on. One of them is the baseline with a stop: `anchor 0930, half_hour, band_or_vwap, both, stop half_width, risk_pct 1.0`, so the list has a known reference point.
- [ ] **Step 2:** Do not pick a part of the day whose `max_gap_trading_days` in the measuring pass is over seven as a variation's only entry window: it cannot pass the frequency bar.
- [ ] **Step 3:** Run `python3 -I -B -c "import json,glob,sys; sys.path.insert(0,'research/noise-area-variations'); import engine; [engine.validate(json.load(open(f))) for f in sorted(glob.glob('research/noise-area-variations/variations/*.json'))]"`. Expected: no error.
- [ ] **Step 4:** Write `variations/LIST.md`: one plain-English paragraph per variation, saying what it does and why.
- [ ] **Step 5:** Commit and push before any run: `research: variation list V1 to V<n> locked before any run`. Record the commit hash; the verdict cites it.

### Task 8: Run and check (tester, checker, lead)

- [ ] **Step 1 (tester):** Run `python3 -I -B research/noise-area-variations/run_all.py`. Commit `out/variations/`. Hand back only the paths, not a view on pass or fail.
- [ ] **Step 2 (checker):** Brief: "For each directory in `out/variations/`, choose 8 trades at random from `harsh-stops-50000.json`, at least 2 stop exits and 2 from 2024 or later. For each, re-derive from the raw data file and the variation's settings file: the band at the decision bar, that the entry signal was true, the fill, the stop level, the size and planned cost for the balance before it, and the exit. Report every mismatch with the numbers, or 'no mismatches'." A mismatch is a failed test: back to the tester, rerun from Step 1.
- [ ] **Step 3 (lead):** Write `lead_check.py`: it reads only the four result files per variation and recomputes, without importing `gates.py`, the average winner R (full and 2024 on), later net, longest gap in trading days (dates from `globex.load_days`), net profit, and the trailing first crossing and shuffle percentage (calling `trailing` and `shuffled` from `research/intraday-momentum-long/run.py`). It prints a diff against each `judge.json`. Expected: no differences. Any difference is a failed test.
- [ ] **Step 4 (lead):** Commit `lead_check.py` and its output `out/variations/lead-check.txt`.

### Task 9: Verdict (lead)

- [ ] **Step 1:** Write `out/VERDICT.md` in plain English: one table, a row per variation, a column per bar with pass or fail and the figure in dollars or as "x times the risk"; then win rate, average winner and loser in dollars, longest losing run, skipped signals, and the $10,000-account profit for information. State how many variations were tried in total, the list's lock commit, and that 2024 to 2026 were not used to choose the list but are not truly unseen.
- [ ] **Step 2:** If one or more passes every bar: name as finalist the one with the lowest shuffle percentage. Stop. The next stage is a new design with Amear.
- [ ] **Step 3:** If none passes and this was the first list: a second list of at most eight may be fixed, using only the measuring pass and each first-list variation's results on 2021 to 2023. Repeat Tasks 7 to 9 with names `W1` to `W8`. If none passes after the second list: the verdict is that Noise-Area is dead under these bars.
- [ ] **Step 4:** Update `STATUS.md` (one page). Add nothing to `RULINGS.md` unless Amear rules. Close the bd issue. Merge the branch to `main` with the superpowers:finishing-a-development-branch skill, `git pull --rebase`, `bd dolt push`, `git push`, and confirm `git status` shows up to date.
- [ ] **Step 5:** Tell Amear the result in a few plain lines with dollar figures.
