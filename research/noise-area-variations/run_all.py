#!/usr/bin/env python3
"""run_all.py -- run every locked settings file and write the results and the judged bars.

run_all(variation_dir, out_dir) -> 0 when done, 2 when it refuses to run anything:
  * the directory has no settings file (*.json; other files are skipped), or
  * `git status --porcelain --ignored --untracked-files=all -- <variation_dir>` (in the repository that
    holds the directory) is not empty or fails: a settings file that is new, changed, ignored or outside
    a repository is not committed, or
  * a settings file does not pass engine.validate (all are checked before any is run).
Then the days are loaded once (globex.load_days on PRAXIS_DATA, 2021-03-08 to 2026-07-17) and each settings
file <name>.json is run four times -- fills "kind" and "harsh-stops", starts 50,000 and 10,000 -- each
twice, comparing digests. It writes out_dir/<name>/<fill>-<start>.json (the full engine result) and
out_dir/<name>/judge.json: gates.judge of the harsh-stops 50,000 result, plus "kind_50000" (gates.judge of
the kind 50,000 result), "info_10000" (net, trades and skipped of the two 10,000 runs, for information)
and "rule_breaks" (the break lines). The break lines are gates.rule_check of the harsh-stops 50,000 and
the kind 50,000 results, and a line for every run whose second run gave a different digest; both judged
results carry the same lines. JSON is written with sorted keys and a trailing newline and holds no run
time, so two runs write the same bytes.

Usage: python3 -I -B research/noise-area-variations/run_all.py [variation_dir [out_dir]]
Standard library only.
"""
import copy
import json
import os
import subprocess
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
import engine   # noqa: E402
import gates    # noqa: E402
import globex   # noqa: E402

DATA = os.environ.get("PRAXIS_DATA", "/Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt")
VARIATION_DIR = os.path.join(_HERE, "variations")
OUT_DIR = os.path.join(_HERE, "out", "variations")
FILLS = ("harsh-stops", "kind")
STARTS = (50000.0, 10000.0)
JUDGED = ("harsh-stops", 50000.0)
CHECKED = (("harsh-stops", 50000.0), ("kind", 50000.0))


def _label(fill, start):
    return "%s %d" % (fill, int(start))


def _uncommitted(variation_dir):
    """-> '' when every file under variation_dir is committed, else what git says (or why it failed)."""
    try:
        p = subprocess.run(["git", "status", "--porcelain", "--ignored", "--untracked-files=all", "--", "."],
                           cwd=variation_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                           universal_newlines=True)
    except OSError as exc:
        return "git could not be run: %s" % (exc,)
    if p.returncode != 0:
        return "git status failed: %s" % (p.stderr.strip() or p.returncode,)
    return p.stdout.strip()


def _write(path, obj):
    with open(path, "w", encoding="ascii", newline="\n") as fh:
        fh.write(json.dumps(obj, sort_keys=True, indent=1) + "\n")


def run_all(variation_dir=VARIATION_DIR, out_dir=OUT_DIR, days=None):
    """-> 0 when every settings file was run and written, 2 when nothing was run (module docstring).
    `days` stands in for the data file (tests); None loads it."""
    if not os.path.isdir(variation_dir):
        print("refused: %s is not a directory" % (variation_dir,))
        return 2
    names = sorted(f for f in os.listdir(variation_dir)
                   if f.endswith(".json") and os.path.isfile(os.path.join(variation_dir, f)))
    if not names:
        print("refused: no settings file in %s" % (variation_dir,))
        return 2
    dirty = _uncommitted(variation_dir)
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
        variations.append((f[:-len(".json")], s))
    if days is None:
        days = globex.load_days(DATA)
    all_dates = [d.date for d in days]
    for name, s in variations:
        res, breaks = {}, []
        for fill in FILLS:
            for start in STARTS:
                a = engine.run(days, copy.deepcopy(s), fill=fill, start=start)
                b = engine.run(days, copy.deepcopy(s), fill=fill, start=start)
                if a["digest"] != b["digest"]:
                    breaks.append("%s: second run gives different trades (digest %s, then %s)"
                                  % (_label(fill, start), a["digest"], b["digest"]))
                res[fill, start] = a
        for key in CHECKED:
            breaks.extend("%s: %s" % (_label(*key), x) for x in gates.rule_check(res[key], days))
        judged = gates.judge(dict(res[JUDGED], rule_breaks=breaks), all_dates)
        judged["kind_50000"] = gates.judge(dict(res["kind", 50000.0], rule_breaks=breaks), all_dates)
        judged["info_10000"] = {fill: {"net": round(sum(t["net"] for t in res[fill, 10000.0]["trades"]), 2),
                                       "trades": len(res[fill, 10000.0]["trades"]),
                                       "skipped": len(res[fill, 10000.0]["skipped"])} for fill in FILLS}
        judged["rule_breaks"] = breaks
        vdir = os.path.join(out_dir, name)
        os.makedirs(vdir, exist_ok=True)
        for (fill, start), r in sorted(res.items()):
            path = os.path.join(vdir, "%s-%d.json" % (fill, int(start)))
            _write(path, r)
            print(path)
        path = os.path.join(vdir, "judge.json")
        _write(path, judged)
        print(path)
    return 0


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) > 2:
        print(__doc__)
        return 2
    return run_all(argv[0] if argv else VARIATION_DIR, argv[1] if len(argv) > 1 else OUT_DIR)


if __name__ == "__main__":
    sys.exit(main())
