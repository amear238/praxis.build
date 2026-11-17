"""Buy and save the broad multi-market data set from Databento (Amear's ruling, 2026-11-17).

What it fetches (CME Globex, volume-ranked continuous contracts):
  - 1-minute bars, front month, 2018-01-01 to 2026-11-16, eleven markets
  - daily bars, front and second month, 2010-06-06 to 2026-11-16 (second month lets rolls be back-adjusted)

Files are named <market>.<rank>.<schema>.<start>_<end>.dbn.zst (end exclusive). For each series the script
works out which dates no file on disk covers yet and fetches only those, one calendar year per request, with
retries. A dropped stream therefore costs at most one year, and a rerun never pays twice for data on disk.

Cost guard: the quote for what is on disk plus the quote for what is still missing must stay within CAP_USD
(the $125 free credit), or nothing is fetched.

Run with the databento virtualenv:  ~/.venvs/databento/bin/python research/data/fetch_databento.py
The API key is read from ~/.config/databento/key (outside the repo, owner-only).
"""
import datetime as dt
import glob
import os
import sys
import time

import databento as db

MARKETS = ["NQ", "ES", "RTY", "CL", "GC", "ZN", "ZB", "6E", "6J", "6B", "6A"]
END = "2026-11-16"
SERIES = [  # (schema, rank, start)
    ("ohlcv-1m", "v.0", "2018-01-01"),
    ("ohlcv-1d", "v.0", "2010-06-06"),
    ("ohlcv-1d", "v.1", "2010-06-06"),
]
CAP_USD = 125.00
OUT = os.environ.get("PRAXIS_MARKET_DATA", os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "market-data", "databento"))
DATASET = "GLBX.MDP3"
D = dt.date.fromisoformat


def file_name(m, r, s, a, b):
    return f"{m}.{r}.{s}.{a}_{b}.dbn.zst"


def on_disk(m, r, s):
    """(start, end) date ranges already saved for one series, sorted."""
    out = []
    for p in glob.glob(os.path.join(OUT, f"{m}.{r}.{s}.*_*.dbn.zst")):
        a, b = os.path.basename(p).split(".")[-3].split("_")
        out.append((D(a), D(b)))
    return sorted(out)


def missing(start, end, have):
    """Date ranges in [start, end) not covered by `have`, split at calendar-year boundaries."""
    gaps, cur = [], start
    for a, b in have:
        if a > cur:
            gaps.append((cur, min(a, end)))
        cur = max(cur, b)
    if cur < end:
        gaps.append((cur, end))
    chunks = []
    for a, b in gaps:
        while a < b:
            nxt = min(b, dt.date(a.year + 1, 1, 1))
            chunks.append((a, nxt))
            a = nxt
    return chunks


def cost(client, m, r, s, a, b):
    return client.metadata.get_cost(dataset=DATASET, symbols=[f"{m}.{r}"], stype_in="continuous",
                                    schema=s, start=str(a), end=str(b))


def main():
    key = open(os.path.expanduser("~/.config/databento/key")).read().strip()
    client = db.Historical(key)
    os.makedirs(OUT, exist_ok=True)

    have_cost, todo = 0.0, []
    for s, r, st in SERIES:
        for m in MARKETS:
            have = on_disk(m, r, s)
            have_cost += sum(cost(client, m, r, s, a, b) for a, b in have)
            todo += [(m, r, s, a, b) for a, b in missing(D(st), D(END), have)]
    todo_cost = sum(cost(client, *t) for t in todo)
    print(f"on disk ${have_cost:.2f}; {len(todo)} chunks to fetch, ${todo_cost:.2f}; "
          f"total ${have_cost + todo_cost:.2f} (cap ${CAP_USD:.2f})", flush=True)
    if have_cost + todo_cost > CAP_USD:
        sys.exit("REFUSED: over the cap")

    for m, r, s, a, b in todo:
        dest = os.path.join(OUT, file_name(m, r, s, a, b))
        tmp = dest + ".part"
        for attempt in range(1, 4):
            try:
                client.timeseries.get_range(dataset=DATASET, symbols=[f"{m}.{r}"], stype_in="continuous",
                                            schema=s, start=str(a), end=str(b), path=tmp)
                break
            except db.BentoError as e:
                print(f"  retry {attempt} {os.path.basename(dest)}: {e}", flush=True)
                time.sleep(10 * attempt)
        else:
            sys.exit(f"FAILED after 3 tries: {dest}")
        os.replace(tmp, dest)
        print(f"saved {os.path.basename(dest)} ({os.path.getsize(dest) / 1e6:.1f} MB)", flush=True)
    print("done", flush=True)


if __name__ == "__main__":
    main()
