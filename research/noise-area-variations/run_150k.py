#!/usr/bin/env python3
"""run_150k.py -- the twelve Noise-Area variations on a $150,000 MyFundedFutures evaluation frame.

The frame (MFFU's help pages, read 2026-11-17): every $150,000 plan starts at 150,000 with a 4,500 maximum
loss limit that trails the end-of-day balance, and a 9,000 profit target. The bars are the five of gates.py
with the limit set to 4,500, so the profit bar is 9,000. The judged fill is "midpoint".

run_150k(variation_dir, out_dir) -> 0 when done, 2 when it refuses (the same refusals as run_all.run_all:
no settings file, a settings file that is not committed or not valid, a name that is not the file stem).
Each settings file <name>.json is run on three fills -- "midpoint", "kind", "harsh-stops" -- from 150,000,
each twice, comparing digests. Written per variation:
  out_dir/<name>/<fill>.json   the full engine result (large; not committed, see out/150k/.gitignore)
  out_dir/<name>/judge.json    gates.judge(midpoint result, calendar, limit=4500) plus
     "kind", "harsh_stops"     gates.judge of the other two fills, same limit (information)
     "digests"                 {fill: digest of the trades}
     "rule_breaks"             gates.rule_check of all three results, and a line for any run whose second
                               run differed; every judged result carries the same lines
     "info"                    info(midpoint result) -- see info(); not a bar
The frequency calendar is run_all.band_dates. JSON is written with sorted keys and holds no run time.

info(result): figures that are not bars.
  max_qty                the most micro contracts in one trade (the plans allow 90)
  days_down_2500         days whose end, or whose lowest mark, is 2,500 or more under the day's start (the
                         Builder plan pauses trading for the rest of such a day; the engine does not)
  lock                   survival again with MFFU's lock: the limit stops rising once it reaches 100 above
                         the start. {"first_cross", "shuffle_pct"} -- trailing_lock and shuffled_lock
  evaluation             evaluation(): an evaluation started on every day of the result

Usage: python3 -I -B research/noise-area-variations/run_150k.py [variation_dir [out_dir]]
Standard library only.
"""
import copy
import json
import multiprocessing
import os
import random
import shutil
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
import engine    # noqa: E402
import gates     # noqa: E402
import globex    # noqa: E402
import run_all   # noqa: E402

VARIATION_DIR = os.path.join(_HERE, "variations-150k")
OUT_DIR = os.path.join(_HERE, "out", "150k")
START = 150000.0
LIMIT = 4500.0
TARGET = 9000.0
LOCK_ABOVE_START = 100.0
SOFT_DAY_LOSS = 2500.0
MAX_MICROS = 90
FILLS = ("midpoint", "kind", "harsh-stops")
JUDGED = "midpoint"
RUNS, SEED = gates.SHUFFLE_RUNS, gates.SHUFFLE_SEED


def _floor(hwm, start, limit, lock):
    """The limit's level: `limit` under the highest end-of-day balance, never above start + lock."""
    return min(hwm - limit, start + lock)


def trailing_lock(days, start=START, limit=LIMIT, lock=LOCK_ABOVE_START):
    """-> the first date whose low is at or under the limit's level (None when none), the level moving at
    each day's end and stopping at start + lock."""
    hwm = start
    for d in days:
        if d["low"] <= _floor(hwm, start, limit, lock):
            return d["date"]
        hwm = max(hwm, d["end"])
    return None


def _blocks(days):
    return [(d["end"] - d["start"], d["low"] - d["start"]) for d in days
            if d["end"] != d["start"] or d["low"] != d["start"]]


def shuffled_lock(days, runs=RUNS, seed=SEED, start=START, limit=LIMIT, lock=LOCK_ABOVE_START):
    """-> (crossed, runs): the days that traded, reordered `runs` times; an order crosses when a day's low
    reaches the limit's level (trailing_lock's level)."""
    blocks = _blocks(days)
    rng = random.Random(seed)
    crossed = 0
    for _ in range(runs):
        rng.shuffle(blocks)
        bal = hwm = start
        for pnl, low in blocks:
            if bal + low <= _floor(hwm, start, limit, lock):
                crossed += 1
                break
            bal += pnl
            hwm = max(hwm, bal)
    return crossed, runs


def evaluation(days, start=START, limit=LIMIT, target=TARGET, lock=LOCK_ABOVE_START):
    """An evaluation started on every day of `days`, using each later day's change (end - start) and lowest
    mark (low - start) as they were in the run. It fails on the first day whose low reaches the limit's
    level, passes on the first day that ends `target` or more above the start, and is unfinished when the
    days run out first. -> {"starts", "passed", "failed", "unfinished", "median_days_to_pass"} (days counted
    from the start day, 1 = the same day; None when none passed). Approximate: the sizes are those of the
    long run's balance, not of a fresh 150,000 account."""
    passed = failed = unfinished = 0
    took = []
    deltas = [(d["end"] - d["start"], d["low"] - d["start"]) for d in days]
    for i in range(len(deltas)):
        bal = hwm = start
        outcome = None
        for n, (pnl, low) in enumerate(deltas[i:], 1):
            if bal + low <= _floor(hwm, start, limit, lock):
                outcome = "failed"
                break
            bal += pnl
            hwm = max(hwm, bal)
            if bal >= start + target:
                outcome = "passed"
                took.append(n)
                break
        if outcome == "passed":
            passed += 1
        elif outcome == "failed":
            failed += 1
        else:
            unfinished += 1
    took.sort()
    return {"starts": len(deltas), "passed": passed, "failed": failed, "unfinished": unfinished,
            "median_days_to_pass": took[len(took) // 2] if took else None}


def info(result):
    days, trades, start = result["days"], result["trades"], result["start"]
    crossed, runs = shuffled_lock(days, start=start)
    return {
        "max_qty": max([t["qty"] for t in trades] or [0]),
        "days_down_2500": sum(1 for d in days if min(d["end"], d["low"]) - d["start"] <= -SOFT_DAY_LOSS),
        "lock": {"first_cross": trailing_lock(days, start=start), "shuffle_pct": 100.0 * crossed / runs},
        "evaluation": evaluation(days, start=start),
    }


_DAYS = None


def _one(item):
    """Run one variation on the three fills (twice each) and judge it -> (name, {fill: result}, judge)."""
    name, s = item
    days = _DAYS
    all_dates = run_all.band_dates(days, s)
    res, breaks = {}, []
    for fill in FILLS:
        a = engine.run(days, copy.deepcopy(s), fill=fill, start=START)
        b = engine.run(days, copy.deepcopy(s), fill=fill, start=START)
        if a["digest"] != b["digest"]:
            breaks.append("%s: second run gives different trades (digest %s, then %s)"
                          % (fill, a["digest"], b["digest"]))
        res[fill] = a
    for fill in FILLS:
        breaks.extend("%s: %s" % (fill, x) for x in gates.rule_check(res[fill], days))
    judged = gates.judge(dict(res[JUDGED], rule_breaks=breaks), all_dates, limit=LIMIT)
    judged["kind"] = gates.judge(dict(res["kind"], rule_breaks=breaks), all_dates, limit=LIMIT)
    judged["harsh_stops"] = gates.judge(dict(res["harsh-stops"], rule_breaks=breaks), all_dates, limit=LIMIT)
    judged["digests"] = {fill: res[fill]["digest"] for fill in FILLS}
    judged["rule_breaks"] = breaks
    judged["info"] = info(res[JUDGED])
    return name, res, judged


def run_150k(variation_dir=VARIATION_DIR, out_dir=OUT_DIR, days=None, workers=None):
    """-> 0 when every settings file was run and written, 2 when nothing was run (module docstring).
    `days` stands in for the data file (tests); None loads it."""
    global _DAYS
    if not os.path.isdir(variation_dir):
        print("refused: %s is not a directory" % (variation_dir,))
        return 2
    names = sorted(f for f in os.listdir(variation_dir)
                   if f.endswith(".json") and not os.path.isdir(os.path.join(variation_dir, f)))
    if not names:
        print("refused: no settings file in %s" % (variation_dir,))
        return 2
    dirty = run_all._uncommitted(variation_dir, names)
    if dirty:
        print("refused: settings not committed:\n%s" % (dirty,))
        return 2
    variations = []
    for f in names:
        try:
            with open(os.path.join(variation_dir, f), "r", encoding="utf-8") as fh:
                s = json.load(fh)
            engine.validate(s)
        except ValueError as exc:
            print("refused: %s: %s" % (f, exc))
            return 2
        stem = f[:-len(".json")]
        if s["name"] != stem:
            print("refused: %s: name %r is not the file stem %r" % (f, s["name"], stem))
            return 2
        variations.append((stem, s))
    _DAYS = globex.load_days(run_all.DATA) if days is None else days
    workers = workers or min(len(variations), max(1, (os.cpu_count() or 2) - 2))
    if workers > 1:
        with multiprocessing.get_context("fork").Pool(workers) as pool:
            done = pool.imap(_one, variations)
            _write_all(done, out_dir)
    else:
        _write_all((_one(v) for v in variations), out_dir)
    return 0


def _write_all(done, out_dir):
    for name, res, judged in done:
        vdir = os.path.join(out_dir, name)
        if os.path.lexists(vdir):
            shutil.rmtree(vdir)
        os.makedirs(vdir)
        for fill in FILLS:
            run_all._write(os.path.join(vdir, "%s.json" % fill), res[fill])
        run_all._write(os.path.join(vdir, "judge.json"), judged)
        print(os.path.join(vdir, "judge.json"), flush=True)


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) > 2:
        print(__doc__)
        return 2
    return run_150k(argv[0] if argv else VARIATION_DIR, argv[1] if len(argv) > 1 else OUT_DIR)


if __name__ == "__main__":
    sys.exit(main())
