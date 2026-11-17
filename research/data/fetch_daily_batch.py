"""Fetch the remaining daily series through Databento's batch service (streaming them took ~20 minutes a file).

Same data and price as fetch_databento.py's daily series; same cost guard: the quote for what is on disk, plus
this batch, plus the worst-case cost of every stream that failed partway (failed_partway.json) must stay within
$125. One job per rank, one file per symbol; each file is renamed to fetch_databento.py's naming so the loader
(research/trend-150k/mdata.py) and a rerun of fetch_databento.py both see it as present.

Run: ~/.venvs/databento/bin/python research/data/fetch_daily_batch.py [--resume] [v.0=JOBID ...]
"""
import glob
import os
import shutil
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import databento as db  # noqa: E402
import fetch_databento as f  # noqa: E402

SCHEMA, START = "ohlcv-1d", "2010-06-06"


def main():
    client = db.Historical(open(os.path.expanduser("~/.config/databento/key")).read().strip())
    have = sum(f.cost(client, m, r, s, a, b) or 0.0 for s, r, _ in f.SERIES for m in f.MARKETS
               for a, b in f.on_disk(m, r, s))
    jobs = {}
    for r in ("v.0", "v.1"):
        syms = [m for m in f.MARKETS if not f.on_disk(m, r, SCHEMA)]
        if syms:
            jobs[r] = syms
    # resume: --resume v.0=JOBID means that rank's job was already submitted (and paid); poll it, do not resubmit
    resumed = dict(a.split("=", 1) for a in sys.argv[1:] if "=" in a)
    quote = sum(client.metadata.get_cost(dataset=f.DATASET, symbols=[f"{m}.{r}" for m in syms],
                                         stype_in="continuous", schema=SCHEMA, start=START, end=f.END)
                for r, syms in jobs.items() if r not in resumed)
    wasted = f._wasted()
    total = have + quote + wasted
    print(f"on disk ${have:.2f}; batch ${quote:.2f}; failed partway ${wasted:.2f}; total ${total:.2f} "
          f"(cap ${f.CAP_USD:.2f})", flush=True)
    if total > f.CAP_USD:
        sys.exit("REFUSED: over the cap")
    for r, syms in jobs.items():
        if r in resumed:
            jid = resumed[r]
            print(f"resuming {jid} ({r}: {', '.join(syms)})", flush=True)
        else:
            job = client.batch.submit_job(dataset=f.DATASET, symbols=[f"{m}.{r}" for m in syms], schema=SCHEMA,
                                          start=START, end=f.END, stype_in="continuous", split_symbols=True)
            jid = job["id"]
            print(f"submitted {jid} ({r}: {', '.join(syms)})", flush=True)
        while True:
            state = next((j["state"] for j in client.batch.list_jobs(states="queued,processing,done,expired")
                          if j["id"] == jid), None)
            if state == "done":
                break
            if state in (None, "expired"):
                sys.exit(f"FAILED: job {jid} state {state}")
            time.sleep(15)
        keep = os.path.join(f.OUT, f"batch-{jid}")   # paid data: a kept folder, never a temporary one
        os.makedirs(keep, exist_ok=True)
        client.batch.download(job_id=jid, output_dir=keep)
        files = [p for p in glob.glob(os.path.join(keep, "**", "*.dbn.zst"), recursive=True)]
        for m in syms:
            hit = [p for p in files if f"{m}.{r}" in os.path.basename(p)]
            if len(hit) != 1:
                sys.exit(f"STOPPED: expected one file for {m}.{r} in {keep}, found "
                         f"{[os.path.basename(p) for p in files]} (files kept; rename by hand)")
            dest = os.path.join(f.OUT, f.file_name(m, r, SCHEMA, START, f.END))
            shutil.move(hit[0], dest)
            print(f"saved {os.path.basename(dest)} ({os.path.getsize(dest) / 1e6:.2f} MB)", flush=True)
    print("done", flush=True)


if __name__ == "__main__":
    main()
