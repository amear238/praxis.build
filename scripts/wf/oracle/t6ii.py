#!/usr/bin/env python3
"""t6ii.py — T6(ii) band oracle table (values-spec :191; oracle input (e) :235) (unit 2026-11-07-wf-oracles, W1).

For the code unit's three oracle sessions (2021-06-15 s70, 2024-12-26 s967, 2026-03-18 s1267; the .cs
OracleDates :98-103) at the 10:00 bar (OracleMod = 600, :53, print at :230-231 / PrintOracle :396-407):
sigma, UpperBound, LowerBound, ATR(14) (or NOBAND / NOATR), plus the session VWAP, which the ORACLE line
does not print. Floats are repr() (round-trip; the .cs prints {0:R}; the textual forms may differ, e.g.
.NET "16000" vs Python "16000.0", "1E-05" vs "1e-05" -- compare numerically, relative 1e-9).
Test oracle only; trades nothing.

python3 -I -B scripts/wf/oracle/t6ii.py --data FILE --session-start {09:31,08:31} (--lookback L --noise-mult k | --grid)
The session start is REQUIRED (market.SESSION_STARTS); the table's second line names it and its label.
"""
import argparse
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
import market as _mk  # noqa: E402
import band as _band  # noqa: E402
import atr as _atr    # noqa: E402

ORACLE_SESSIONS = (("2021-06-15", 70), ("2024-12-26", 967), ("2026-03-18", 1267))  # values-spec :235
GRID_LOOKBACK = (10, 14, 18)
GRID_K = (0.8, 1.0, 1.2)
HEADER = "oracle values — UNVERIFIED against NT8 until 2a"


def check_sessions(market):
    for date, n in ORACLE_SESSIONS:
        s = market.by_date.get(date)
        if s is None or s.n != n:
            raise SystemExit("FATAL: oracle session %s expected s%d, calendar has %s"
                             % (date, n, "no session" if s is None else "s%d" % s.n))


def rows(market, pairs):
    out = []
    for date, n in ORACLE_SESSIONS:
        have_atr, _sum, atr = _atr.atr_at(market, n)
        for L, k in pairs:
            try:
                st = _band.band_at(market, n, _mk.ORACLE_MOD, L, k)
            except KeyError:
                out.append((date, n, L, k, "NO 10:00 BAR (no ORACLE print)", "", "", "", ""))
                continue
            atr_txt = repr(atr) if have_atr else "NOATR"
            if st.have_band:
                out.append((date, n, L, k, repr(st.sigma), repr(st.upper), repr(st.lower), repr(st.vwap), atr_txt))
            else:
                out.append((date, n, L, k, "NOBAND", "", "", repr(st.vwap), atr_txt))
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description="T6(ii) oracle table (test oracle; trades nothing)")
    ap.add_argument("--data", required=True)
    ap.add_argument("--lookback", type=int)
    ap.add_argument("--noise-mult", type=float)
    ap.add_argument("--grid", action="store_true", help="all nine Lookback {10,14,18} x k {0.8,1.0,1.2}")
    ap.add_argument("--session-start", required=True, choices=sorted(_mk.SESSION_STARTS),
                    help="REQUIRED, no default: 09:31 = %s; 08:31 = %s" % (_mk.SESSION_STARTS["09:31"],
                                                                         _mk.SESSION_STARTS["08:31"]))
    a = ap.parse_args(argv)
    if a.grid:
        pairs = [(L, k) for L in GRID_LOOKBACK for k in GRID_K]
    elif a.lookback is not None and a.noise_mult is not None:
        pairs = [(a.lookback, a.noise_mult)]
    else:
        ap.error("give --grid or both --lookback and --noise-mult")
    m = _mk.load_market(a.data, session_start=a.session_start)
    check_sessions(m)
    print(HEADER)
    print(_mk.session_start_line(m))
    print("")
    print("source: %s (%d bytes, sha256 %s); N = %d sessions; weekend dates dropped (INFERRED) = %d"
          % (m.source["path"], m.source["bytes"], m.source["sha256"], m.N, m.weekend_dates_dropped))
    print("pre-open bars loaded = %d; pre-open-only weekdays dropped (UNVERIFIED whether NT8 makes them "
          "sessions) = %d%s" % (m.pre_open_bars, len(m.pre_open_only_dropped),
                                (": " + ", ".join(m.pre_open_only_dropped)) if m.pre_open_only_dropped else ""))
    for date, n in ORACLE_SESSIONS:
        s = m.by_date[date]
        print("s%d = %s, %d loaded bars, nt8_last_bar %s" % (n, date, len(s.bars), s.nt8_last_bar))
    print("")
    print("| date | s | Lookback | k | σ | UpperBound | LowerBound | VWAP — not printed by the strategy's ORACLE line | ATR(14) |")
    print("|---|---|---|---|---|---|---|---|---|")
    for r in rows(m, pairs):
        print("| %s | s%d | %d | %r | %s | %s | %s | %s | %s |" % r)
    return 0


if __name__ == "__main__":
    sys.exit(main())
