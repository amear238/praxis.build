#!/usr/bin/env python3
"""C1 Opening Gap Fade pre-screen (unit 2026-11-14-search-c1-gap-fade, bead Praxis_build-vn4).

Implements research/search-loop/c1-gap-fade/RULES.md. Mac-side Python PRE-SCREEN only;
a pre-screen result is never a contender result. Standard library only.
Run:  python3 -I -B research/search-loop/c1-gap-fade/screen.py
Read-only on the data file and on scripts/wf (imported with -B so no __pycache__).

Overfitting guard (enforced below): in-sample is computed for V1, V2, V3; the selection
rule is applied to in-sample results; holdout and full are computed ONLY for the selected
variant (or, if none qualifies, the highest in-sample-net variant, "for the record, not
selected"). run_period() refuses any other variant outside the in-sample period.
"""
import csv
import datetime as dt
import hashlib
import json
import os
import sys
from fractions import Fraction as F

REPO = "/Volumes/Sensidine/Praxis.build"
HERE = os.path.join(REPO, "research", "search-loop", "c1-gap-fade")
OUT = os.path.join(HERE, "out")
TMP = "/tmp/praxis-c1"
DATA = "/Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt"
DATA_SHA = "307c5e8af1da42b7606d666f14e4f34228feec50d19dd52d25396aae1b16e454"
D6_DATA = "/Users/admin/praxis-signals/b2-data/NQ-continuous-1min.nt8import.txt"
RULES = os.path.join(HERE, "RULES.md")
RULES_SHA = "f892a265c99079365544a31c2f0fa85a6dff68ba72bfb450ffca391d4a774ba3"

sys.path.insert(0, os.path.join(REPO, "scripts", "wf"))
import sessions as S  # noqa: E402
import report as R    # noqa: E402

STANDING = "Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed."

RTH_FIRST, RTH_LAST = "093100", "160000"
LAST_DATE = dt.date(2026, 7, 17)          # "Ignore data after 2026-07-17"
PERIODS = {"in-sample": (dt.date(2021, 3, 8), dt.date(2024, 12, 31)),
           "holdout": (dt.date(2025, 1, 1), dt.date(2026, 7, 17)),
           "full": (dt.date(2021, 3, 8), dt.date(2026, 7, 17))}
VARIANTS = {"V1": (F("0.10"), F("0.50")), "V2": (F("0.20"), F("0.80")), "V3": (F("0.05"), F("0.30"))}
SLIP = F("0.5")          # 2 ticks
TICK = F("0.25")
NQ_PV, MNQ_PV = F(20), F(2)
COMMS = (F("2.96"), F("4.68"))
MNQ_COMM = F("1.90")
PF_MIN = F("1.10")

# D6 TIERS (D6 report Appendix B :589), ceiling() and rows_for() verbatim in logic.
TIERS = [("Studio #003 5K", 5000, 250, "Static"), ("Studio #001 10K", 10000, 500, "Static"),
         ("Studio #002 20K", 20000, 1000, "Static"),
         ("Rapid 25K", 25000, 1000, "Eval EOD / SimF intraday"), ("Rapid EOD 25K", 25000, 1000, "EOD"),
         ("Builder 25K", 25000, 1000, "EOD"),
         ("Rapid 50K", 50000, 2000, "Eval EOD / SimF intraday"), ("Rapid EOD 50K", 50000, 2000, "EOD"),
         ("Pro 50K", 50000, 2000, "EOD"), ("Builder 50K", 50000, 2000, "EOD"),
         ("Builder 50K add-on", 50000, 1500, "EOD"),
         ("Rapid 100K", 100000, 3000, "Eval EOD / SimF intraday"), ("Pro 100K", 100000, 3000, "EOD"),
         ("Builder 100K", 100000, 3000, "EOD"),
         ("Rapid 150K", 150000, 4500, "Eval EOD / SimF intraday"), ("Pro 150K", 150000, 4500, "EOD"),
         ("Builder 150K", 150000, 4500, "EOD")]


def ceiling(size, limit):
    return min(F(32, 1000) * size, F(8, 10) * limit)


def rows_for(typ):
    if "SimF" in typ:
        return [(" [Eval EOD]", "EOD"), (" [SimF intraday]", "SimF")]
    if typ == "Static":
        return [(" [trailing measure = stricter]", "EOD")]
    return [("", "EOD")]


def judged(r, kind, meas):
    if meas == "WIN":
        v = max(r["ct_start"], r["eod_start"])
        return max(v, r["mae_start"]) if kind == "SimF" else v
    v = r["worst"]
    return max(v, r["mae_worst"]) if kind == "SimF" else v


# ---------------------------------------------------------------- helpers
def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def money(x):
    return "${:,.2f}".format(float(x))


def dec(x, places=None):
    """Exact decimal string of a Fraction if it terminates within 6 places, else rounded."""
    x = F(x)
    if places is None:
        for p in range(0, 7):
            if (x * 10 ** p).denominator == 1:
                places = p
                break
        else:
            places = 6
    q = round(x * 10 ** places)
    s = "-" if q < 0 else ""
    q = abs(q)
    if places == 0:
        return s + str(q)
    return "%s%d.%0*d" % (s, q // 10 ** places, places, q % 10 ** places)


def pf(nets):
    pos = sum((x for x in nets if x > 0), F(0))
    neg = sum((x for x in nets if x < 0), F(0))
    if neg == 0:
        return None   # printed "inf"
    return pos / -neg


def pfs(v):
    return "inf" if v is None else "%.4f" % float(v)


def dd(points, eq0=F(0), pk0=F(0)):
    return R._dd_series(points, eq0, pk0)


# ---------------------------------------------------------------- data
def load(path):
    """RTH bars per date (stamps 093100..160000), dates <= LAST_DATE. Verifies sha and order."""
    h = hashlib.sha256()
    days = {}
    prev_key = None
    lines = 0
    with open(path, "rb") as f:
        for raw in f:
            h.update(raw)
            lines += 1
            s = raw.decode("ascii").strip()
            d, rest = s.split(" ", 1)
            hms, o, hi, lo, c, v = rest.split(";")
            key = d + hms
            assert prev_key is None or key > prev_key, "file not in strict stamp order at line %d" % lines
            prev_key = key
            if not (RTH_FIRST <= hms <= RTH_LAST):
                continue
            date = dt.date(int(d[:4]), int(d[4:6]), int(d[6:]))
            if date > LAST_DATE:
                continue
            days.setdefault(date, []).append((hms, F(o), F(hi), F(lo), F(c)))
    got = h.hexdigest()
    assert got == DATA_SHA, "data sha mismatch %s" % got
    return days, lines, got


# ---------------------------------------------------------------- one day
def simulate_day(date, bars, PC, gmin, gmax):
    """Returns a trade dict or None. bars = RTH bars of the day in stamp order, first is 093100."""
    assert bars[0][0] == RTH_FIRST
    O = bars[0][1]
    gap_pct = (O - PC) / PC * 100
    if not (gmin <= abs(gap_pct) <= gmax):
        return None
    side = -1 if gap_pct > 0 else 1          # SHORT if gap up, LONG if gap down
    dist = abs(O - PC)
    entry_fill = O - SLIP if side == -1 else O + SLIP
    if side == -1:
        stop = O + dist
    else:
        stop = O - dist
    exit_kind = exit_stamp = exit_fill = None
    adverse = F(0)
    for (hms, o, hi, lo, c) in bars:
        if side == -1:
            stop_hit = hi >= stop
            tgt_hit = lo <= PC - TICK
        else:
            stop_hit = lo <= stop
            tgt_hit = hi >= PC + TICK
        if stop_hit:                          # both hit -> stop
            exit_kind, exit_stamp = "stop", hms
            exit_fill = stop + SLIP if side == -1 else stop - SLIP
            adv_price = exit_fill
        elif tgt_hit:
            exit_kind, exit_stamp = "target", hms
            exit_fill = PC + SLIP if side == -1 else PC - SLIP
            adv_price = hi if side == -1 else lo
        else:
            adv_price = hi if side == -1 else lo
        a = (adv_price - entry_fill) if side == -1 else (entry_fill - adv_price)
        if a > adverse:
            adverse = a
        if exit_kind is not None:
            break
    if exit_kind is None:
        hms, o, hi, lo, c = bars[-1]
        exit_kind, exit_stamp = "time", hms
        exit_fill = c + SLIP if side == -1 else c - SLIP
    points = (exit_fill - entry_fill) * side
    return {"date": date, "side": "long" if side == 1 else "short", "PC": PC, "O": O, "gap_pct": gap_pct,
            "entry_fill": entry_fill, "exit_kind": exit_kind, "exit_stamp": exit_stamp, "exit_fill": exit_fill,
            "points": points, "nq_net_296": points * NQ_PV - COMMS[0], "nq_net_468": points * NQ_PV - COMMS[1],
            "mnq_net": points * MNQ_PV - MNQ_COMM, "mae_points": adverse}


def build_day_list(days):
    """Trading days = dates with a 093100 bar. Returns [(date, bars, PC or None, skip reason)]."""
    tdays = sorted(d for d, b in days.items() if b[0][0] == RTH_FIRST)
    out = []
    for i, d in enumerate(tdays):
        if i == 0:
            out.append((d, days[d], None, "first trading day (no previous)"))
            continue
        p = tdays[i - 1]
        if (d - p).days > 4:
            out.append((d, days[d], None, "previous trading day %s is %d days back" % (p, (d - p).days)))
            continue
        out.append((d, days[d], days[p][-1][4], None))
    return tdays, out


ALLOWED = {"selected": None}


def run_period(daylist, vname, period):
    if period != "in-sample":
        assert ALLOWED["selected"] == vname, "overfitting guard: %s not allowed on %s" % (vname, period)
    gmin, gmax = VARIANTS[vname]
    a, b = PERIODS[period]
    tr = []
    for d, bars, PC, why in daylist:
        if why is not None or not (a <= d <= b):
            continue
        t = simulate_day(d, bars, PC, gmin, gmax)
        if t is not None:
            tr.append(t)
    return tr


def stats(tr):
    n468 = [t["nq_net_468"] for t in tr]
    n296 = [t["nq_net_296"] for t in tr]
    mnq = [t["mnq_net"] for t in tr]
    return {"trades": len(tr), "longs": sum(1 for t in tr if t["side"] == "long"),
            "shorts": sum(1 for t in tr if t["side"] == "short"),
            "target": sum(1 for t in tr if t["exit_kind"] == "target"),
            "stop": sum(1 for t in tr if t["exit_kind"] == "stop"),
            "time": sum(1 for t in tr if t["exit_kind"] == "time"),
            "wins_nq468": sum(1 for x in n468 if x > 0), "losses_nq468": sum(1 for x in n468 if x < 0),
            "zero_nq468": sum(1 for x in n468 if x == 0),
            "net_nq_296": sum(n296, F(0)), "net_nq_468": sum(n468, F(0)), "net_mnq": sum(mnq, F(0)),
            "pf_nq_296": pf(n296), "pf_nq_468": pf(n468), "pf_mnq": pf(mnq),
            "maxdd_ct_nq_296": dd(n296)[0], "maxdd_ct_nq_468": dd(n468)[0], "maxdd_ct_mnq": dd(mnq)[0],
            "points_sum": sum((t["points"] for t in tr), F(0))}


def print_stats(label, s):
    print("%s | trades %d (long %d, short %d) | exits target %d / stop %d / time %d | wins %d losses %d zero %d (at NQ $4.68)" % (
        label, s["trades"], s["longs"], s["shorts"], s["target"], s["stop"], s["time"],
        s["wins_nq468"], s["losses_nq468"], s["zero_nq468"]))
    print("    net NQ @2.96 %s PF %s | net NQ @4.68 %s PF %s | net MNQ %s PF %s | sum points %s" % (
        money(s["net_nq_296"]), pfs(s["pf_nq_296"]), money(s["net_nq_468"]), pfs(s["pf_nq_468"]),
        money(s["net_mnq"]), pfs(s["pf_mnq"]), dec(s["points_sum"])))
    print("    closed-trade max DD: NQ @2.96 %s | NQ @4.68 %s | MNQ %s" % (
        money(s["maxdd_ct_nq_296"]), money(s["maxdd_ct_nq_468"]), money(s["maxdd_ct_mnq"])))


def jstats(s):
    o = {}
    for k, v in s.items():
        if isinstance(v, F):
            o[k] = dec(v, 2) if not k.startswith("points") else dec(v)
        elif v is None:
            o[k] = "inf"
        else:
            o[k] = v
    for k in ("pf_nq_296", "pf_nq_468", "pf_mnq"):
        o[k] = pfs(s[k])
    return o


COLS = ["date", "side", "PC", "O", "gap_pct", "entry_fill", "exit_kind", "exit_stamp", "exit_fill", "points",
        "nq_net_296", "nq_net_468", "mnq_net", "mae_points"]


def write_csv(path, tr):
    with open(path, "w", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(COLS)
        for t in tr:
            row = []
            for c in COLS:
                v = t[c]
                if c == "date":
                    v = v.isoformat()
                elif c == "gap_pct":
                    v = dec(v, 6)
                elif isinstance(v, F):
                    v = dec(v)
                row.append(v)
            w.writerow(row)


# ---------------------------------------------------------------- D6 four-measure basis
def d6_measures(tr, cal, inst_pv, comm):
    """D6 window_measures (Appendix B :697) on our trades. Trades whose date is not a
    calendar session are left out of the windows (count returned)."""
    dates = [s["date"] for s in cal["sessions"]]
    d2n = {d: i + 1 for i, d in enumerate(dates)}
    W = cal["windows"]
    net = lambda x: x["points"] * inst_pv - comm
    mae_d = lambda x: x["mae_points"] * inst_pv
    notcal = [x for x in tr if x["date"].isoformat() not in d2n]
    trc = [x for x in tr if x["date"].isoformat() in d2n]
    pw_tr, pw_daily, pw_mae = [], [], []
    for w in W:
        c, d = w["oos"]
        tw = [x for x in trc if c <= d2n[x["date"].isoformat()] <= d]
        daily = []
        for s in range(c, d + 1):
            daily.append(sum((net(x) for x in tw if d2n[x["date"].isoformat()] == s), F(0)))
        pw_tr.append([net(x) for x in tw])
        pw_daily.append(daily)
        pts = []
        for x in tw:
            pts.append(("low", -mae_d(x) - comm))
            pts.append(("close", net(x)))
        pw_mae.append(pts)
    four = R.four_measure_drawdowns(pw_tr, pw_daily)
    eq = pk = F(0)
    for k, w in enumerate(W):
        def run(e0, p0):
            e, p, m = e0, p0, p0 - e0
            for kind, v in pw_mae[k]:
                if kind == "low":
                    lo = e + v
                    m = max(m, p - lo)
                else:
                    e = e + v
                    p = max(p, e)
                    m = max(m, p - e)
            return m, e, p
        ms = run(F(0), F(0))[0]
        mc, eq, pk = run(eq, pk)
        four[k]["mae_start"], four[k]["mae_carry"] = ms, mc
        e, lo_c, lo_m = F(0), F(0), F(0)
        for kind, v in pw_mae[k]:
            if kind == "low":
                lo_m = min(lo_m, e + v)
            else:
                e += v
                lo_c = min(lo_c, e)
                lo_m = min(lo_m, e)
        four[k]["static_ct"], four[k]["static_mae"] = -lo_c, -lo_m
        four[k]["n"] = len(pw_tr[k])
        four[k]["net"] = sum(pw_tr[k], F(0))
        four[k]["mae_worst"] = max(ms, mc)
    return four, notcal


def full_measures(tr, inst_pv, comm):
    """Full period, all trades, from 0: closed-trade, end-of-day (one point per trading day
    with a trade; days without a trade leave equity unchanged), intratrade-inclusive."""
    net = lambda x: x["points"] * inst_pv - comm
    ct = dd([net(x) for x in tr])[0]
    byday = {}
    for x in tr:
        byday[x["date"]] = byday.get(x["date"], F(0)) + net(x)
    eod = dd([byday[d] for d in sorted(byday)])[0]
    e = p = m = F(0)
    for x in tr:
        lo = e - x["mae_points"] * inst_pv - comm
        m = max(m, p - lo)
        e = e + net(x)
        p = max(p, e)
        m = max(m, p - e)
    return {"ct": ct, "eod": eod, "intratrade": m}


def full_for(kind, fm):
    v = max(fm["ct"], fm["eod"])
    return max(v, fm["intratrade"]) if kind == "SimF" else v


def tier_table(four, fm, inst_label):
    rows = []
    print("\n=== TIER TABLE @ 1 %s (D6 method; ceiling = min(3.2%% size, 80%% limit), strict '<') ===" % inst_label)
    print("tier | ceiling | WIN worst window (windows below /17) | VS4 worst window (windows below /17) | FULL | JUDGED")
    for tn, size, lim, typ in TIERS:
        ce = ceiling(size, lim)
        for lab, kind in rows_for(typ):
            cells = {}
            for meas in ("WIN", "VS4"):
                vals = [judged(r, kind, meas) for r in four]
                ok = sum(1 for v in vals if v < ce)
                cells[meas] = (max(vals), ok)
            fv = full_for(kind, fm)
            jud = "PASS" if (cells["VS4"][1] == len(four) == 17 and fv < ce) else "FAIL"
            print("%s%s | %s | %s %s (%d/17) | %s %s (%d/17) | %s %s | %s" % (
                tn, lab, money(ce), money(cells["WIN"][0]), "PASS" if cells["WIN"][1] == 17 else "FAIL",
                cells["WIN"][1], money(cells["VS4"][0]), "PASS" if cells["VS4"][1] == 17 else "FAIL",
                cells["VS4"][1], money(fv), "PASS" if fv < ce else "FAIL", jud))
            rows.append({"tier": tn + lab, "kind": kind, "ceiling": dec(ce, 2),
                         "win_worst": dec(cells["WIN"][0], 2), "win_below": cells["WIN"][1],
                         "vs4_worst": dec(cells["VS4"][0], 2), "vs4_below": cells["VS4"][1],
                         "full": dec(fv, 2), "judged": jud})
        if typ == "Static":
            vals = [r["static_ct"] for r in four]
            ok = sum(1 for v in vals if v < ce)
            print("%s [static measure, shown, not judged] | %s | static_ct worst %s (%d/17)" % (
                tn, money(ce), money(max(vals)), ok))
    return rows


# ---------------------------------------------------------------- main
def main():
    run_ts = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print(STANDING)
    print("C1 Opening Gap Fade PRE-SCREEN (not validated, not checked against NT8). Run at", run_ts)
    rsha = sha(RULES)
    print("RULES.md sha256", rsha, "MATCH" if rsha == RULES_SHA else "MISMATCH")
    assert rsha == RULES_SHA
    me = os.path.abspath(__file__)
    print("screen.py sha256", sha(me))
    print("PF definition: sum of positive net trade P&L / |sum of negative net trade P&L| at the stated "
          "commission; zero-net trades excluded; 'inf' if no losers.")
    print("Wins/losses counted on NQ net at $4.68.")

    days, lines, dsha = load(DATA)
    print("data", DATA, "| lines", lines, "| sha256", dsha, "MATCH")
    tdays, daylist = build_day_list(days)
    skipped = [(d, why) for d, b, pc, why in daylist if why]
    print("trading days (date with a 09:31 bar, <= 2026-07-17): %d, first %s last %s" % (len(tdays), tdays[0], tdays[-1]))
    print("skipped days (no PC):", len(skipped))
    for d, why in skipped:
        print("   skip", d, "-", why)
    wk = [d for d in tdays if d.weekday() >= 5]
    print("weekend-dated trading days (literal rule, kept):", [(d.isoformat(), d.strftime("%a"), len(days[d])) for d in wk])
    early = [(d.isoformat(), days[d][-1][0]) for d in tdays if days[d][-1][0] != RTH_LAST]
    print("trading days whose last RTH bar is not 16:00 (time exit at that bar): %d" % len(early))
    print("  ", early)
    print("sanity _dd_series([+100,-300,+50,-100]) =",
          float(R._dd_series([F(100), F(-300), F(50), F(-100)])[0]), "(expect 350)")

    # ---- in-sample, all three variants
    print("\n=== IN-SAMPLE %s..%s, all variants ===" % PERIODS["in-sample"])
    IS = {}
    for v in ("V1", "V2", "V3"):
        tr = run_period(daylist, v, "in-sample")
        s = stats(tr)
        IS[v] = (tr, s)
        print_stats("%s GMIN %s GMAX %s" % (v, dec(VARIANTS[v][0], 2), dec(VARIANTS[v][1], 2)), s)
        write_csv(os.path.join(TMP, "builder_is_trades_%s.csv" % v), tr)
        wkt = [t["date"].isoformat() for t in tr if t["date"].weekday() >= 5]
        print("    in-sample trades on weekend-dated days:", wkt)

    # ---- selection (in-sample only)
    def qualifies(s):   # PF None means no losers ("inf"), which is >= 1.10
        return s["net_nq_468"] > 0 and (s["pf_nq_468"] is None or s["pf_nq_468"] >= PF_MIN)
    qual = [v for v in ("V1", "V2", "V3") if qualifies(IS[v][1])]
    print("\n=== SELECTION (in-sample net @4.68 > 0 AND PF @4.68 >= 1.10; highest net @4.68) ===")
    for v in ("V1", "V2", "V3"):
        s = IS[v][1]
        print("%s: net @4.68 %s, PF @4.68 %s -> %s" % (v, money(s["net_nq_468"]), pfs(s["pf_nq_468"]),
                                                       "qualifies" if v in qual else "does not qualify"))
    if qual:
        sel = max(qual, key=lambda v: IS[v][1]["net_nq_468"])
        label = "SELECTED"
    else:
        sel = max(("V1", "V2", "V3"), key=lambda v: IS[v][1]["net_nq_468"])
        label = "for the record, not selected"
    print("RESULT: %s -> %s%s" % (sel, label, "" if qual else " (candidate FAILS in-sample)"))
    ALLOWED["selected"] = sel

    # ---- holdout and full, selected only
    res = {}
    for per in ("holdout", "full"):
        tr = run_period(daylist, sel, per)
        s = stats(tr)
        res[per] = (tr, s)
        print("\n=== %s %s..%s, %s (%s) ===" % (per.upper(), PERIODS[per][0], PERIODS[per][1], sel, label))
        print_stats(sel, s)
    full_tr = res["full"][0]
    write_csv(os.path.join(OUT, "trades_%s_full.csv" % sel), full_tr)

    # ---- D6 four-measure basis, FULL period, selected variant
    print("\n=== D6 four-measure basis, %s, FULL period ===" % sel)
    if os.path.exists(D6_DATA):
        cal_path = D6_DATA
        print("calendar file (D6's):", D6_DATA)
    else:
        cal_path = DATA
        print("D6 calendar file MISSING; using our data file for the calendar:", DATA)
    cal_sha = sha(cal_path)
    print("calendar file sha256", cal_sha)
    cal = S.build_calendar(cal_path)
    cdates = [s["date"] for s in cal["sessions"]]
    print("N sessions", cal["N"], "first", cdates[0], "last", cdates[-1], "K", cal["K"], "dropped",
          cal["dropped"], cal["dropped_dates"])
    out_d6 = {}
    for inst, pv, comm in (("MNQ", MNQ_PV, MNQ_COMM), ("NQ", NQ_PV, COMMS[1])):
        four, notcal = d6_measures(full_tr, cal, pv, comm)
        fm = full_measures(full_tr, pv, comm)
        out_d6[inst] = {"four": four, "full": fm, "notcal": notcal}
    print("our full-period trade dates that are not calendar sessions: %d %s" % (
        len(out_d6["MNQ"]["notcal"]), [x["date"].isoformat() for x in out_d6["MNQ"]["notcal"]]))
    lastoos = cal["windows"][-1]["oos_dates"][1]
    print("trades after the last OOS session (%s), outside every window: %d" % (
        lastoos, sum(1 for x in full_tr if x["date"].isoformat() > lastoos)))
    print("trades before the first OOS session (%s), outside every window: %d" % (
        cal["windows"][0]["oos_dates"][0], sum(1 for x in full_tr if x["date"].isoformat() < cal["windows"][0]["oos_dates"][0])))

    four = out_d6["MNQ"]["four"]
    print("\n--- %s @ 1 MNQ: per OOS window (dollars) ---" % sel)
    print("k | OOS dates | trades | net | ct_start | eod_start | ct_carry | eod_carry | WORST4 | mae_start | mae_carry | static_ct | static_mae")
    W = cal["windows"]
    for k, w in enumerate(W):
        r = four[k]
        print("%d | %s..%s | %d | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s" % (
            w["k"], w["oos_dates"][0], w["oos_dates"][1], r["n"], money(r["net"]), money(r["ct_start"]),
            money(r["eod_start"]), money(r["ct_carry"]), money(r["eod_carry"]), money(r["worst"]),
            money(r["mae_start"]), money(r["mae_carry"]), money(r["static_ct"]), money(r["static_mae"])))
    print("MAX over windows: WORST4 %s | MAE-incl %s | static_ct %s | static_mae %s" % (
        money(max(r["worst"] for r in four)), money(max(r["mae_worst"] for r in four)),
        money(max(r["static_ct"] for r in four)), money(max(r["static_mae"] for r in four))))
    for inst in ("MNQ", "NQ"):
        fm = out_d6[inst]["full"]
        print("FULL period, all trades, 1 %s: closed-trade max DD %s | end-of-day max DD %s | intratrade-inclusive max DD %s" % (
            inst, money(fm["ct"]), money(fm["eod"]), money(fm["intratrade"])))
    print("MAE note: bar-based bound from the trade's 1-minute bars (entry bar to exit bar inclusive; "
          "stop-exit bar uses the stop exit fill), not an NT8 figure.")

    tiers_mnq = tier_table(out_d6["MNQ"]["four"], out_d6["MNQ"]["full"], "MNQ")
    passing = [r["tier"] for r in tiers_mnq if r["judged"] == "PASS"]
    print("1 MNQ JUDGED PASS rows:", passing if passing else "NONE")

    print("\n=== 1 NQ (@ $4.68) JUDGED, one line per tier row ===")
    tiers_nq = []
    four_nq, fm_nq = out_d6["NQ"]["four"], out_d6["NQ"]["full"]
    for tn, size, lim, typ in TIERS:
        ce = ceiling(size, lim)
        for lab, kind in rows_for(typ):
            vals = [judged(r, kind, "VS4") for r in four_nq]
            ok = sum(1 for v in vals if v < ce)
            fv = full_for(kind, fm_nq)
            jud = "PASS" if (ok == 17 and fv < ce) else "FAIL"
            print("%s%s | ceiling %s | VS4 worst %s (%d/17) | FULL %s | JUDGED %s" % (
                tn, lab, money(ce), money(max(vals)), ok, money(fv), jud))
            tiers_nq.append({"tier": tn + lab, "ceiling": dec(ce, 2), "vs4_worst": dec(max(vals), 2),
                             "vs4_below": ok, "full": dec(fv, 2), "judged": jud})

    # ---- summary.json
    def fourj(fr):
        return [{k: (dec(v, 2) if isinstance(v, F) else v) for k, v in r.items()} for r in fr]
    summary = {
        "unit": "2026-11-14-search-c1-gap-fade", "bead": "Praxis_build-vn4", "kind": "PRE-SCREEN (not validated)",
        "standing_limitation": STANDING, "run_timestamp_utc": run_ts,
        "inputs": {"data": DATA, "data_sha256": dsha, "data_lines": lines, "rules": RULES, "rules_sha256": rsha,
                   "screen_py_sha256": sha(me), "calendar_file": cal_path, "calendar_file_sha256": cal_sha,
                   "sessions_py_sha256": sha(os.path.join(REPO, "scripts/wf/sessions.py")),
                   "report_py_sha256": sha(os.path.join(REPO, "scripts/wf/report.py"))},
        "pf_definition": "sum positive net / |sum negative net| at the stated commission; zero trades excluded; inf if no losers",
        "trading_days": len(tdays), "skipped_days": [[d.isoformat(), w] for d, w in skipped],
        "weekend_trading_days": [d.isoformat() for d in wk],
        "in_sample": {v: jstats(IS[v][1]) for v in IS},
        "selection": {"qualifying": qual, "variant": sel, "label": label},
        "selected_holdout": jstats(res["holdout"][1]), "selected_full": jstats(res["full"][1]),
        "d6": {"calendar_N": cal["N"], "K": cal["K"],
               "trade_dates_not_sessions": [x["date"].isoformat() for x in out_d6["MNQ"]["notcal"]],
               "mnq_windows": fourj(out_d6["MNQ"]["four"]), "nq_windows": fourj(out_d6["NQ"]["four"]),
               "mnq_full": {k: dec(v, 2) for k, v in out_d6["MNQ"]["full"].items()},
               "nq_full": {k: dec(v, 2) for k, v in out_d6["NQ"]["full"].items()},
               "tiers_mnq": tiers_mnq, "tiers_nq_468": tiers_nq, "mnq_judged_pass": passing},
        "sanity_dd_100_m300_50_m100": dec(R._dd_series([F(100), F(-300), F(50), F(-100)])[0]),
    }
    with open(os.path.join(OUT, "summary.json"), "w") as f:
        json.dump(summary, f, indent=1, sort_keys=False)
        f.write("\n")
    print("\nwrote", os.path.join(OUT, "summary.json"), "and", os.path.join(OUT, "trades_%s_full.csv" % sel))


if __name__ == "__main__":
    main()
