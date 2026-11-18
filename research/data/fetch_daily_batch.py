"""Fetch the remaining daily series through Databento's batch service (streaming them took ~20 minutes a file).

Same data and price as fetch_databento.py's daily series; same cost guard: the quote for what is on disk, plus
this batch, plus the worst-case cost of every stream that failed partway (failed_partway.json) must stay within
$125. One job per rank, one file per symbol; each file is renamed to fetch_databento.py's naming so the loader
(research/trend-150k/mdata.py) and a rerun of fetch_databento.py both see it as present.

Run: ~/.venvs/databento/bin/python research/data/fetch_daily_batch.py [--resume] [v.0=JOBID ...]
"""
import glob
import os
import struct
import sys
import time
from compression import zstd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import databento as db  # noqa: E402
import fetch_databento as f  # noqa: E402

SCHEMA, START = "ohlcv-1d", "2010-06-06"


def _download_files(client, jid, keep, threads=16):
    """Every file of a finished job, one request each over HTTPS, checked against its sha256; files already
    present and matching are skipped. (The single zip of a job broke at the same byte on every try.)
    A finished job's files download again at no charge."""
    import concurrent.futures as cf
    import hashlib
    import requests
    key = client._key
    want = [x for x in client.batch.list_files(jid) if x["filename"].endswith(".dbn.zst")]

    def one(x):
        dest = os.path.join(keep, x["filename"])
        exp = x["hash"].split(":", 1)[1]
        if os.path.exists(dest) and hashlib.sha256(open(dest, "rb").read()).hexdigest() == exp:
            return 0
        for attempt in range(1, 6):
            try:
                r = requests.get(x["urls"]["https"], auth=(key, ""), timeout=60)
                r.raise_for_status()
                if hashlib.sha256(r.content).hexdigest() != exp:
                    raise ValueError("checksum mismatch")
                with open(dest + ".part", "wb") as fh:
                    fh.write(r.content)
                os.replace(dest + ".part", dest)
                return 1
            except Exception as e:  # noqa: BLE001 - retried, then reported
                last = e
                time.sleep(2 * attempt)
        raise RuntimeError(f"{x['filename']}: {last}")

    done = 0
    with cf.ThreadPoolExecutor(threads) as ex:
        for i, n in enumerate(ex.map(one, want), 1):
            done += n
            if i % 5000 == 0:
                print(f"  {i}/{len(want)} files checked", flush=True)
    print(f"  job {jid}: {len(want)} files present and checked ({done} downloaded now)", flush=True)


def _join(paths, dest):
    """One DBN file from several of one symbol: the first file's header, then every file's records, by stamp."""
    head, recs = None, []
    for p in paths:
        raw = zstd.decompress(open(p, "rb").read())
        if raw[:3] != b"DBN":
            sys.exit(f"STOPPED: not DBN: {p}")
        (mlen,) = struct.unpack_from("<I", raw, 4)
        if head is None:
            head = raw[:8 + mlen]
        body = raw[8 + mlen:]
        if len(body) % 56:
            sys.exit(f"STOPPED: partial records in {p}")
        recs += [body[i:i + 56] for i in range(0, len(body), 56)]
    recs.sort(key=lambda b: struct.unpack_from("<Q", b, 8)[0])
    tmp = dest + ".part"
    with open(tmp, "wb") as fh:
        fh.write(zstd.compress(head + b"".join(recs)))
    os.replace(tmp, dest)


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
                                          start=START, end=f.END, stype_in="continuous", split_symbols=True,
                                          split_duration="none")
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
        _download_files(client, jid, keep)
        files = [p for p in glob.glob(os.path.join(keep, "**", "*.dbn.zst"), recursive=True)]
        for m in syms:
            hit = sorted(p for p in files if os.path.basename(p).endswith(f".{m}.{r}.dbn.zst"))
            if not hit:
                sys.exit(f"STOPPED: no file for {m}.{r} in {keep} (files kept)")
            dest = os.path.join(f.OUT, f.file_name(m, r, SCHEMA, START, f.END))
            _join(hit, dest)
            print(f"saved {os.path.basename(dest)} from {len(hit)} file(s) "
                  f"({os.path.getsize(dest) / 1e6:.2f} MB)", flush=True)
    print("done", flush=True)


if __name__ == "__main__":
    main()
