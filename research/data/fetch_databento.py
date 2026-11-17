"""Buy and save the broad multi-market data set from Databento (Amear's ruling, 2026-11-17).

What it fetches (CME Globex, volume-ranked continuous contracts):
  - 1-minute bars, front month, 2018-01-01 to 2026-11-16, eleven markets
  - daily bars, front and second month, 2010-06-06 to 2026-11-16 (second month lets rolls be back-adjusted)

It quotes the cost first and refuses to download if the quote exceeds the cap (the $125 free credit).
Files already on disk are skipped, so a rerun is free.

Run with the databento virtualenv:  ~/.venvs/databento/bin/python research/data/fetch_databento.py
The API key is read from ~/.config/databento/key (outside the repo, owner-only).
"""
import os
import sys

import databento as db

MARKETS = ["NQ", "ES", "RTY", "CL", "GC", "ZN", "ZB", "6E", "6J", "6B", "6A"]
END = "2026-11-16"
JOBS = [  # (schema, rank, start)
    ("ohlcv-1m", "v.0", "2018-01-01"),
    ("ohlcv-1d", "v.0", "2010-06-06"),
    ("ohlcv-1d", "v.1", "2010-06-06"),
]
CAP_USD = 125.00
OUT = os.environ.get("PRAXIS_MARKET_DATA", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "market-data", "databento"))
DATASET = "GLBX.MDP3"


def path_for(market, schema, rank, start):
    return os.path.join(OUT, f"{market}.{rank}.{schema}.{start}_{END}.dbn.zst")


def main():
    key = open(os.path.expanduser("~/.config/databento/key")).read().strip()
    client = db.Historical(key)
    os.makedirs(OUT, exist_ok=True)

    todo = [(m, s, r, st) for (s, r, st) in JOBS for m in MARKETS
            if not os.path.exists(path_for(m, s, r, st))]
    quote = sum(
        client.metadata.get_cost(dataset=DATASET, symbols=[f"{m}.{r}"], stype_in="continuous",
                                 schema=s, start=st, end=END)
        for (m, s, r, st) in todo)
    print(f"{len(todo)} files to fetch, quoted ${quote:.2f} (cap ${CAP_USD:.2f})", flush=True)
    if quote > CAP_USD:
        sys.exit(f"REFUSED: quote ${quote:.2f} is over the ${CAP_USD:.2f} cap")

    for (m, s, r, st) in todo:
        dest = path_for(m, s, r, st)
        tmp = dest + ".part"
        client.timeseries.get_range(dataset=DATASET, symbols=[f"{m}.{r}"], stype_in="continuous",
                                    schema=s, start=st, end=END, path=tmp)
        os.replace(tmp, dest)
        print(f"saved {os.path.basename(dest)} ({os.path.getsize(dest) / 1e6:.1f} MB)", flush=True)
    print("done", flush=True)


if __name__ == "__main__":
    main()
