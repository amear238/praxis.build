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
import json
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
    """Quoted dollars for one chunk, or None when the contract did not trade then (e.g. RTY before mid-2017)."""
    for attempt in range(1, 6):
        try:
            return client.metadata.get_cost(dataset=DATASET, symbols=[f"{m}.{r}"], stype_in="continuous",
                                            schema=s, start=str(a), end=str(b))
        except db.BentoClientError as e:
            if "symbology_invalid_request" in str(e):
                return None
            raise
        except db.BentoServerError as e:
            print(f"  quote retry {attempt} {file_name(m, r, s, a, b)}: {e}", flush=True)
            time.sleep(5 * attempt)
    raise SystemExit(f"FAILED to quote {file_name(m, r, s, a, b)}")


WASTED = os.path.join(OUT, "failed_partway.json")


def _wasted():
    try:
        return sum(json.load(open(WASTED)).values())
    except FileNotFoundError:
        return 0.0


def _add_wasted(name, q):
    d = json.load(open(WASTED)) if os.path.exists(WASTED) else {}
    d[f"{name} #{len(d) + 1}"] = q
    json.dump(d, open(WASTED, "w"), indent=1)


def main():
    key = open(os.path.expanduser("~/.config/databento/key")).read().strip()
    client = db.Historical(key)
    os.makedirs(OUT, exist_ok=True)

    have_cost, todo = 0.0, []

    def have_now():
        return sum(cost(client, mm, rr, ss, a, b) or 0.0 for ss, rr, _ in SERIES for mm in MARKETS
                   for a, b in on_disk(mm, rr, ss))
    for s, r, st in SERIES:
        for m in MARKETS:
            have = on_disk(m, r, s)
            have_cost += sum(cost(client, m, r, s, a, b) or 0.0 for a, b in have)
            todo += [(m, r, s, a, b) for a, b in missing(D(st), D(END), have)]
    quotes = [(t, cost(client, *t)) for t in todo]
    for t, q in quotes:
        if q is None:
            print(f"skipped, contract not trading then: {file_name(*t)}", flush=True)
    todo = [t for t, q in quotes if q is not None]
    todo_cost = sum(q for _, q in quotes if q is not None)
    wasted = _wasted()
    print(f"on disk ${have_cost:.2f}; {len(todo)} chunks to fetch, ${todo_cost:.2f}; failed partway so far "
          f"${wasted:.2f}; total ${have_cost + todo_cost + wasted:.2f} (cap ${CAP_USD:.2f})", flush=True)
    if have_cost + todo_cost + wasted > CAP_USD:
        sys.exit("REFUSED: over the cap")

    for (m, r, s, a, b), q in zip(todo, [q for _, q in quotes if q is not None]):
        dest = os.path.join(OUT, file_name(m, r, s, a, b))
        tmp = dest + ".part"
        for attempt in range(1, 4):
            if os.path.exists(tmp):
                # a stream that ended early may have been billed: count it at its full quote (worst case)
                _add_wasted(os.path.basename(dest), q)
                os.remove(tmp)
                todo_cost_left = sum(cost(client, *x) or 0.0 for x in todo[todo.index((m, r, s, a, b)):])
                if have_now() + todo_cost_left + _wasted() > CAP_USD:
                    sys.exit("REFUSED: a retry would go over the cap")
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
