#!/usr/bin/env python3
"""make_150k_list.py -- write variations-150k/: the twelve locked variations, each at three risk sizes.

Nothing but risk_pct, name and reason changes from variations/<V>.json. The three sizes:
  <V>-pct      the same percentage of the account (risk_pct unchanged)
  <V>-room     the same number of losers inside the limit: risk_pct * 0.75, because the limit is 4% of the
               50,000 account (2,000) and 3% of the 150,000 account (4,500)
  <V>-dollars  the same dollars a trade at the start: risk_pct / 3
risk_pct is rounded to six decimal places. Run once, before the list is committed.
Usage: python3 -I -B research/noise-area-variations/make_150k_list.py
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "variations")
DST = os.path.join(HERE, "variations-150k")
SIZES = (("pct", 1.0, "the same percentage of the account as on the 50,000 frame"),
         ("room", 0.75, "the same number of losers inside the limit as on the 50,000 frame"),
         ("dollars", 1.0 / 3.0, "the same dollars a trade as on the 50,000 frame"))


def main():
    os.makedirs(DST, exist_ok=True)
    for f in sorted(os.listdir(SRC)):
        if not f.endswith(".json"):
            continue
        with open(os.path.join(SRC, f), "r", encoding="utf-8") as fh:
            s = json.load(fh)
        for tag, mult, why in SIZES:
            t = dict(s)
            t["name"] = "%s-%s" % (s["name"], tag)
            t["risk_pct"] = round(s["risk_pct"] * mult, 6)
            t["reason"] = "%s on the 150,000 frame, %s (%s%% of the balance, $%.0f at the start). %s" % (
                s["name"], why, ("%.6f" % t["risk_pct"]).rstrip("0").rstrip("."), 1500.0 * t["risk_pct"], s["reason"])
            with open(os.path.join(DST, t["name"] + ".json"), "w", encoding="utf-8", newline="\n") as fh:
                fh.write(json.dumps(t, indent=1) + "\n")
            print("%-12s risk_pct %-9s $%.0f a trade, %.0f losers inside 4,500" % (
                t["name"], t["risk_pct"], 1500.0 * t["risk_pct"], 4500.0 / (1500.0 * t["risk_pct"])))


if __name__ == "__main__":
    main()
