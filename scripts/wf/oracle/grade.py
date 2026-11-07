#!/usr/bin/env python3
"""grade.py — T8-T11 grader for arm (b) stop-on runs (unit 2026-11-07-wf-oracles, U3b-2, W2).

Test oracle only: it trades nothing and is not the walk-forward. It reads one or more trade lists produced
by ninjascript/PraxisNoiseAreaBreakoutArmB.cs (origin/arm-b/wf-tunables; read via `git show`, never checked
out), the 1-minute data file, and grades values-spec T8 (:195-196), T9 (:197), T10 (:199), T11 (:201)
(docs/specs/2026-11-06-walk-forward-values.md, v2.1, §4 precedence :77) into a markdown grade sheet.

UNVERIFIED: every oracle value here is unverified against NT8 until the 2a comparison. The fill rules are
the results-report defaults (market.py: market_fill / session_close_fill / flateod_fill), not yet refitted
from T1/T3 on the VM; the fill-rule-fit section reports whether the trade lists fit them.

T12 is NOT built here. W3 adds scripts/wf/oracle/policy.py exposing `grade_t12(ctx) -> [Verdict]`; it may
`import grade` (this module registers itself as sys.modules['grade'] when run as a script, so the Verdict
class is shared). If policy.py is absent or fails to import, the sheet says
"T12: not built in this file (policy.py)".

Usage:
  python3 -I -B scripts/wf/oracle/grade.py --session-start {09:31,08:31} --runs MANIFEST.json [--data FILE] [--out FILE]
  python3 -I -B scripts/wf/oracle/grade.py --session-start {09:31,08:31} --trades FILE --format bridge|nt8csv --label L \
      --lookback 10 --noise-mult 1.0 --stop-atr-mult 1.5 --exit-policy BandOrVWAP [--data FILE] [--out FILE]
--session-start is REQUIRED (no default; market.SESSION_STARTS); the sheet's Inputs section names it and its label.
MANIFEST.json = [{"label", "path", "format": "bridge"|"nt8csv", "Lookback", "NoiseMult", "StopAtrMult",
                  "ExitPolicy"}, ...]   (relative paths resolve against the manifest's directory)
Exit code: 0 = every verdict PASS/UNTESTED; 1 = any FAIL; 2 = input error.
Standard library only.
"""
import argparse
import csv
import hashlib
import importlib.util
import json
import os
import sys
from decimal import Decimal
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_WF = os.path.dirname(_HERE)
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
import market as _mk  # noqa: E402
import band as _band  # noqa: E402
import atr as _atr    # noqa: E402

# Let `import grade` (policy.py, W3) resolve to THIS module when grade.py runs as __main__.
sys.modules.setdefault("grade", sys.modules[__name__])

DEFAULT_DATA = "/Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt"


def _load_by_path(name, path):
    """Import a scripts/wf module by file path (READ-ONLY reuse). scripts/wf is NOT left on sys.path: it holds
    select.py, which would shadow the stdlib `select`. tradelist.py APPENDS scripts/wf to sys.path at import
    (tradelist.py:22); sys.path is restored afterwards so that side effect does not leak into this process."""
    mod = sys.modules.get(name)
    if mod is not None and os.path.abspath(getattr(mod, "__file__", "")) == path:
        return mod
    saved = list(sys.path)
    try:
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[name] = mod
        spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


tradelist = _load_by_path("tradelist", os.path.join(_WF, "tradelist.py"))
_report = _load_by_path("_wf_report", os.path.join(_WF, "report.py"))
STANDING_LIMITATION = _report.STANDING_LIMITATION
STANDING_PHRASE = _report.STANDING_PHRASE
_norm = _report._norm

VERDICTS = ("PASS", "FAIL", "UNTESTED")
STOP_GRID = tradelist.GRID_STOPATRMULT     # (1.5, 2.25, 3.0) — T8-T11 are stop-on gradings
SESSION_CLOSE = "Exit on session close"    # NT8's IsExitOnSessionCloseStrategy name (.cs :117; name UNVERIFIED
                                           # beyond the committed runs, results report :133)
FLATEOD = "FlatEOD"                        # .cs FlattenAll :422-428
MARKET_EXITS = ("XL", "XS", "XStop")       # .cs :282/:293 (XL/XS), :256/:264 (XStop)
FIRST_ATR_SESSION = 16                     # values-spec T11 :201, §4 warm-up (15 completed sessions, s1 drop)


class GradeInputError(Exception):
    """Bad input: exit code 2."""


class Verdict(object):
    """One graded result. verdict in VERDICTS; reason is always given; rows = the deciding trade rows
    (ints for a per-run verdict, 'label#row' strings for a cross-run one); lines = detail strings."""
    __slots__ = ("test", "verdict", "reason", "rows", "lines", "run")

    def __init__(self, test, verdict, reason, rows=None, lines=None, run=None):
        if verdict not in VERDICTS:
            raise ValueError("verdict must be one of %s: %r" % (VERDICTS, verdict))
        if not reason:
            raise ValueError("a verdict needs a reason (%s)" % test)
        self.test, self.verdict, self.reason = test, verdict, reason
        self.rows, self.lines, self.run = list(rows or []), list(lines or []), run

    def __repr__(self):
        return "Verdict(%s%s %s: %s rows=%r)" % (self.test, "" if self.run is None else " [%s]" % self.run,
                                                 self.verdict, self.reason, self.rows)


# ---------------------------------------------------------------------------------------------------
# parameters
# ---------------------------------------------------------------------------------------------------

def check_params(p, where="run"):
    """Validate one run's parameters; returns {'Lookback','NoiseMult','StopAtrMult','ExitPolicy'}."""
    for k in ("Lookback", "NoiseMult", "StopAtrMult", "ExitPolicy"):
        if k not in p:
            raise GradeInputError("%s: missing parameter %s" % (where, k))
    ep = p["ExitPolicy"]
    if not isinstance(ep, str) or ep.strip().lstrip("+-").isdigit() or ep not in _mk.POLICIES:
        raise GradeInputError(
            "%s: ExitPolicy must be given BY NAME, one of %s; got %r. A number is refused (values-spec §9(d): "
            "the enum order differs between ArmB {BandOrVWAP=0, OppBand=1, Flat1559=2} and the base)"
            % (where, list(_mk.POLICIES), ep))
    try:
        L = p["Lookback"]
        if isinstance(L, bool) or isinstance(L, str) and not L.strip().isdigit():
            raise ValueError
        L = int(L)
        if float(p["Lookback"]) != L:
            raise ValueError
        k = float(p["NoiseMult"])
        m = float(p["StopAtrMult"])
    except (TypeError, ValueError):
        raise GradeInputError("%s: Lookback/NoiseMult/StopAtrMult must be numbers: %r" % (where, p))
    if m not in STOP_GRID:
        raise GradeInputError("%s: StopAtrMult=%r refused: T8-T11 grade stop-on runs only, m in %s "
                              "(values-spec §3 :51; m = 0 is the stop-less T1-T3 path)" % (where, m, list(STOP_GRID)))
    if L not in tradelist.GRID_LOOKBACK:
        raise GradeInputError("%s: Lookback=%r not in %s" % (where, L, list(tradelist.GRID_LOOKBACK)))
    if k not in tradelist.GRID_NOISEMULT:
        raise GradeInputError("%s: NoiseMult=%r not in %s" % (where, k, list(tradelist.GRID_NOISEMULT)))
    out = {"Lookback": L, "NoiseMult": k, "StopAtrMult": m, "ExitPolicy": ep}
    tradelist.validate_params(dict(out, Contracts=1))   # cross-check against the 81-config GRID
    return out


# ---------------------------------------------------------------------------------------------------
# trade-list loading: tradelist.py for validation + canonical fields, a supplementary read for prices/names
# ---------------------------------------------------------------------------------------------------

def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _num(v, where):
    if isinstance(v, bool) or not isinstance(v, (int, Decimal, float)):
        raise GradeInputError("%s: price %r is not a number" % (where, v))
    return float(v)


def _supp_bridge(path, canon):
    """entryPrice / exitPrice from the bridge JSON (tradelist.load_bridge_file drops them). The bridge
    success status and payload are UNVERIFIED (code read only, as tradelist.py says). No entry name exists
    in the bridge payload. Times and side are re-parsed and asserted equal to tradelist's, row for row."""
    with open(path, "r", encoding="utf-8") as fh:
        doc = json.load(fh, parse_float=Decimal)
    trades = doc["trades"]
    if len(trades) != len(canon):
        raise GradeInputError("%s: supplementary read found %d trades, tradelist %d" % (path, len(trades), len(canon)))
    out = []
    for i, (t, c) in enumerate(zip(trades, canon)):
        where = "%s trade[%d] (row %d)" % (path, i, i + 1)
        en, ex = tradelist.parse_nt_time(t["entryTime"]), tradelist.parse_nt_time(t["exitTime"])
        if (en, ex, t["marketPosition"]) != (c["entry"], c["exit"], c["side"]):
            raise GradeInputError("%s: supplementary read disagrees with tradelist (%s %s %s vs %s %s %s)"
                                  % (where, en, ex, t["marketPosition"], c["entry"], c["exit"], c["side"]))
        for k in ("entryPrice", "exitPrice"):
            if k not in t:
                raise GradeInputError("%s: missing key %r (needed for the fill-rule fit and the stop level)" % (where, k))
        out.append((_num(t["entryPrice"], where), _num(t["exitPrice"], where), None))
    return out


def _price_csv(s, where):
    # UNVERIFIED: NT8 CSV price formatting (plain decimal, optional thousands commas, assumed).
    try:
        return float(s.strip().replace(",", ""))
    except ValueError:
        raise GradeInputError("%s: cannot parse price %r (NT8 CSV format UNVERIFIED)" % (where, s))


def _supp_csv(path, canon):
    """Entry price / Exit price / Entry name from the NT8 CSV (tradelist.load_nt8_csv drops them). The NT8
    CSV format (header, delimiter, time and number formats) is UNVERIFIED, as tradelist.py says; the header
    was already checked against tradelist.EXPECTED_NT8_COLUMNS. Blank rows skipped exactly as tradelist does."""
    with open(path, "r", encoding="utf-8-sig", newline="") as fh:
        rows = list(csv.reader(fh))
    header = tuple(h.strip() for h in rows[0])
    idx = {c: i for i, c in enumerate(header)}
    out = []
    j = 0
    for r, row in enumerate(rows[1:], start=2):
        if not any(c.strip() for c in row):
            continue
        where = "%s line %d (row %d)" % (path, r, j + 1)
        if j >= len(canon):
            raise GradeInputError("%s: more rows than tradelist parsed" % where)
        c = canon[j]
        en = tradelist._parse_csv_time(row[idx["Entry time"]], where)
        ex = tradelist._parse_csv_time(row[idx["Exit time"]], where)
        side = row[idx["Market pos."]].strip()
        if (en, ex, side) != (c["entry"], c["exit"], c["side"]):
            raise GradeInputError("%s: supplementary read disagrees with tradelist" % where)
        out.append((_price_csv(row[idx["Entry price"]], where), _price_csv(row[idx["Exit price"]], where),
                    row[idx["Entry name"]].strip()))
        j += 1
    if j != len(canon):
        raise GradeInputError("%s: supplementary read found %d rows, tradelist %d" % (path, j, len(canon)))
    return out


def load_trades(path, fmt):
    """-> (source dict from tradelist, [market.Trade]) with row = 1-based trade index in file order."""
    if not os.path.isfile(path):
        raise GradeInputError("trade file not found: %s" % path)
    if fmt == "bridge":
        src = tradelist.load_bridge_file(path, tradelist.OK_STATUSES)
        if src["truncated"]:
            raise GradeInputError("%s: bridge list truncated (%d listed, totalTrades %r): T8(iv) needs every trade"
                                  % (path, src["n_trades"], src["metrics"].get("totalTrades")))
        supp = _supp_bridge(path, src["trades"])
    elif fmt == "nt8csv":
        src = tradelist.load_nt8_csv(path, contracts=1)
        supp = _supp_csv(path, src["trades"])
    else:
        raise GradeInputError("format must be 'bridge' or 'nt8csv': %r" % (fmt,))
    trades = []
    for i, (c, (ep, xp, en)) in enumerate(zip(src["trades"], supp)):
        trades.append(_mk.Trade(c["entry"], c["exit"], c["side"], ep, xp, en, c["exit_name"], i + 1))
    return src, trades


# ---------------------------------------------------------------------------------------------------
# trade annotation (reusable; W3 imports these)
# ---------------------------------------------------------------------------------------------------

def bar_at(market, pos):
    n, i = pos
    return market.sessions[n - 1].bars[i]


def prev_pos(market, pos):
    n, i = pos
    if i > 0:
        return (n, i - 1)
    if n > 1:
        return (n - 1, len(market.sessions[n - 2].bars) - 1)
    return None


def next_pos(market, pos):
    n, i = pos
    if i + 1 < len(market.sessions[n - 1].bars):
        return (n, i + 1)
    if n < market.N:
        return (n + 1, 0)
    return None


def iter_pos(market, a, b):
    """Positions a..b inclusive in loaded-bar order (crosses sessions)."""
    p = a
    while p is not None and p <= b:
        yield p
        p = next_pos(market, p)


def pos_str(market, pos):
    if pos is None:
        return "none"
    return "s%d %s" % (pos[0], bar_at(market, pos).dt.strftime("%Y-%m-%d %H:%M"))


def first_flat_pos(market, n, policy):
    """The session's first F: the first bar with market.is_session_flat true."""
    s = market.sessions[n - 1]
    for i in range(len(s.bars)):
        if _mk.is_session_flat(market, n, i, policy):
            return (n, i)
    raise AssertionError("session s%d has no session-flat bar" % n)


def is_flat_pos(market, pos, policy):
    return _mk.is_session_flat(market, pos[0], pos[1], policy)


def exit_kind(name):
    if name == "XStop":
        return "XStop"
    if name in ("XL", "XS"):
        return name
    if name == SESSION_CLOSE:
        return "SESSION_CLOSE"
    if name == FLATEOD:
        return "FLATEOD"
    return "OTHER"


class Ann(object):
    """Annotation of one trade against the loaded-bar model."""
    __slots__ = ("trade", "row", "entry_pos", "entry_dec_pos", "exit_pos", "kind", "d_pos", "flat_d",
                 "first_f", "have_atr", "atr_sum", "c_pos", "c_flat", "alt_c_pos", "ambiguous", "notes")

    def __repr__(self):
        return "Ann(row=%d %s entry=%r d=%r c=%r kind=%s)" % (self.row, self.trade.side, self.entry_pos, self.d_pos,
                                                           self.c_pos, self.kind)


def _locate(market, dt, what, row):
    p = market.index.get(dt)
    if p is None:
        raise GradeInputError("row %d: %s %s is not a loaded bar stamp (calibration of fill time stamps "
                              "is a VM step; values-spec T8 'Calibration first')" % (row, what, dt))
    return p


def first_crossing(market, side, fill, m, atr_sum, a, b, only=None):
    """First position in a..b (inclusive) whose close crosses the level (atr.stop_crossed: exact; a tie IS a
    crossing). only(pos) -> bool restricts the scan (wrong stop (4)). None if no crossing."""
    for p in iter_pos(market, a, b):
        if only is not None and not only(p):
            continue
        if _atr.stop_crossed(side, fill, bar_at(market, p).c, m, atr_sum):
            return p
    return None


def annotate_trade(market, t, params):
    policy, m = params["ExitPolicy"], params["StopAtrMult"]
    a = Ann()
    a.trade, a.row, a.notes = t, t.row, []
    a.entry_pos = _locate(market, t.entry_dt, "entry time", t.row)
    a.exit_pos = _locate(market, t.exit_dt, "exit time", t.row)
    a.entry_dec_pos = prev_pos(market, a.entry_pos)
    if a.entry_dec_pos is None:
        raise GradeInputError("row %d: entry fills on the first loaded bar (no decision bar)" % t.row)
    a.kind = exit_kind(t.exit_name)
    xb = bar_at(market, a.exit_pos)
    if a.kind == "SESSION_CLOSE":
        a.d_pos = a.exit_pos                                   # d = F (values-spec T8)
        n, i = a.exit_pos
        if i != len(market.sessions[n - 1].bars) - 1:
            a.notes.append("'%s' not on the session's last bar (%s)" % (SESSION_CLOSE, pos_str(market, a.exit_pos)))
    elif a.kind == "FLATEOD":
        n, i = a.exit_pos
        if xb.mod == _mk.CLOSE_MOD and i > 0:
            a.d_pos = (n, i - 1)                               # fill on the 16:00 bar; d = the bar before (15:59)
        else:
            a.d_pos = prev_pos(market, a.exit_pos)
            a.notes.append("FlatEOD fill not on a 16:00 bar (%s)" % pos_str(market, a.exit_pos))
        if policy != "Flat1559":
            a.notes.append("FlatEOD under %s is unexpected (T12(ii) grades exit names)" % policy)
    else:
        a.d_pos = prev_pos(market, a.exit_pos)                 # market exit: decided on the bar before its fill
        if a.kind == "OTHER":
            a.notes.append("exit name %r is not XL/XS/XStop/%s/FlatEOD; graded as a market exit"
                           % (t.exit_name, SESSION_CLOSE))
    a.flat_d = a.d_pos is not None and is_flat_pos(market, a.d_pos, policy)
    a.first_f = first_flat_pos(market, a.entry_pos[0], policy)
    a.have_atr, a.atr_sum, _ = _atr.atr_at(market, a.entry_pos[0])   # ATR of the entry FILL bar's session
    a.c_pos = a.alt_c_pos = None
    a.ambiguous = False
    if a.d_pos is None or a.d_pos < a.entry_pos:
        a.notes.append("decision bar d precedes the entry fill bar; no stop scan")
    elif a.have_atr:
        a.c_pos = first_crossing(market, t.side, t.entry_price, m, a.atr_sum, a.entry_pos, a.d_pos)
    else:
        a.notes.append("entry with no ATR(14) (s%d): the .cs sets no stop level (OnExecutionUpdate returns)"
                       % a.entry_pos[0])
    if a.entry_pos[1] == 0 and a.d_pos is not None and a.d_pos >= a.entry_pos:
        # UNVERIFIED order on a session's first bar: ComputeAtr (OnBarUpdate) vs OnExecutionUpdate. If the fill
        # is processed first, stopAtrSum is the PREVIOUS session's atrSum.
        ph, ps, _ = _atr.atr_at(market, a.entry_pos[0] - 1) if a.entry_pos[0] > 1 else (False, 0.0, 0.0)
        a.alt_c_pos = (first_crossing(market, t.side, t.entry_price, m, ps, a.entry_pos, a.d_pos) if ph else None)
        a.ambiguous = a.alt_c_pos != a.c_pos
        a.notes.append("FLAG: entry fills on the session's first bar (ComputeAtr vs OnExecutionUpdate order "
                       "UNVERIFIED); c with this session's ATR = %s, with the previous session's = %s%s"
                       % (pos_str(market, a.c_pos), pos_str(market, a.alt_c_pos),
                          " — AMBIGUOUS, not graded" if a.ambiguous else ""))
    a.c_flat = a.c_pos is not None and is_flat_pos(market, a.c_pos, policy)
    return a


def annotate(market, run):
    """[Ann] for every trade of a market.Run (params already checked)."""
    return [annotate_trade(market, t, run.params) for t in run.trades]


def expected_fill(market, a):
    """(kind label, fill-bar pos, predicted price) by the default fill rules (market.py)."""
    t = a.trade
    if a.kind == "SESSION_CLOSE":
        return SESSION_CLOSE, a.exit_pos, _mk.session_close_fill(bar_at(market, a.exit_pos), t.side == "Short")
    if a.kind == "FLATEOD":
        xb = bar_at(market, a.exit_pos)
        if xb.mod != _mk.CLOSE_MOD:
            return FLATEOD, a.exit_pos, None
        return FLATEOD, a.exit_pos, _mk.flateod_fill(xb, t.side == "Short")
    label = t.exit_name if a.kind != "OTHER" else "other:%s" % t.exit_name
    return label, a.exit_pos, _mk.market_fill(bar_at(market, a.exit_pos), t.side == "Short")


def _eq(x, y):
    return y is not None and abs(x - y) < 1e-9


# ---------------------------------------------------------------------------------------------------
# context and caches
# ---------------------------------------------------------------------------------------------------

class GradedRun(object):
    __slots__ = ("label", "run", "anns", "fmt", "path", "sha256")

    def __init__(self, label, run, anns, fmt, path, sha256):
        self.label, self.run, self.anns, self.fmt, self.path, self.sha256 = label, run, anns, fmt, path, sha256

    @property
    def params(self):
        return self.run.params


class Ctx(object):
    def __init__(self, market, runs):
        self.market, self.runs = market, runs
        self._states = {}
        self.fillfit = {}      # label -> bool (filled by grade_fillfit)

    def states(self, n, lookback, k):
        """[BandState] for every bar of session n (cached)."""
        key = (n, lookback, k)
        st = self._states.get(key)
        if st is None:
            st = [s for _i, _b, s in _band.iter_session_states(self.market, n, lookback, k)]
            self._states[key] = st
        return st

    def band(self, pos, lookback, k):
        return self.states(pos[0], lookback, k)[pos[1]]


def build_ctx(market, specs):
    """specs: [{'label','path','format', params...}] -> Ctx with annotated runs."""
    runs, seen = [], set()
    for j, sp in enumerate(specs):
        label = str(sp.get("label") or "run%d" % (j + 1))
        if label in seen:
            raise GradeInputError("duplicate run label %r" % label)
        seen.add(label)
        params = check_params(sp, "run %r" % label)
        src, trades = load_trades(sp["path"], sp.get("format"))
        run = _mk.Run(params, trades, {"label": label, "path": sp["path"], "format": sp.get("format"),
                                       "sha256": src["sha256"], "n_trades": src["n_trades"]})
        runs.append(GradedRun(label, run, annotate(market, run), sp.get("format"), sp["path"], src["sha256"]))
    return Ctx(market, runs)


# ---------------------------------------------------------------------------------------------------
# graders: each takes a Ctx and returns [Verdict]
# ---------------------------------------------------------------------------------------------------

def grade_fillfit(ctx):
    """values-spec T8 'Calibration first': do the trade lists fit the default fill rules?"""
    out = []
    mk = ctx.market
    for r in ctx.runs:
        counts, bad = {}, []
        for a in r.anns:
            t = a.trade
            kinds = [("entry", a.entry_pos, _mk.market_fill(bar_at(mk, a.entry_pos), t.side == "Long"), t.entry_price)]
            lab, fp, pred = expected_fill(mk, a)
            kinds.append((lab, fp, pred, t.exit_price))
            for lab, fp, pred, got in kinds:
                c = counts.setdefault(lab, [0, 0])
                c[1] += 1
                if _eq(got, pred):
                    c[0] += 1
                else:
                    bad.append((a.row, "row %d %s at %s: trade list %r, rule %r" % (a.row, lab, pos_str(mk, fp), got, pred)))
        lines = ["%s: %d/%d match" % (k, v[0], v[1]) for k, v in sorted(counts.items())]
        lines += [b for _r, b in bad[:20]] + (["... %d more mismatches" % (len(bad) - 20)] if len(bad) > 20 else [])
        ctx.fillfit[r.label] = not bad
        if bad:
            out.append(Verdict("FILLFIT", "UNTESTED", "fill rules do not fit (calibration from T1/T3 on the VM is a "
                               "separate step); %d price(s) differ" % len(bad), sorted({x for x, _ in bad}), lines, r.label))
        else:
            out.append(Verdict("FILLFIT", "PASS", "every entry and exit price equals the default fill rule "
                               "(%d trades)" % len(r.anns), [], lines, r.label))
    return out


def _t8_findings(ctx, r):
    """(i)-(iv) violations: [(row, text)], predicted count, actual count."""
    mk, pol = ctx.market, r.params["ExitPolicy"]
    v = []
    for a in r.anns:
        if a.ambiguous:
            continue
        t = a.trade
        if a.kind == "XStop":                                                     # (i)
            if a.c_pos != a.d_pos:
                v.append((a.row, "(i) row %d XStop: decided %s but first crossing c = %s"
                          % (a.row, pos_str(mk, a.d_pos), pos_str(mk, a.c_pos))))
            if a.flat_d:
                v.append((a.row, "(i) row %d XStop decided on a session-flat bar %s" % (a.row, pos_str(mk, a.d_pos))))
            pred = _mk.market_fill(bar_at(mk, a.exit_pos), t.side == "Short")
            if not _eq(t.exit_price, pred):
                v.append((a.row, "(i) row %d XStop fill %r at %s != market-exit rule %r"
                          % (a.row, t.exit_price, pos_str(mk, a.exit_pos), pred)))
        if a.c_pos is None and a.kind == "XStop":                                  # (ii)
            v.append((a.row, "(ii) row %d has no crossing through d but exits XStop" % a.row))
        if a.c_pos is not None and a.d_pos is not None and a.c_pos < a.d_pos:      # (iii) c < d
            v.append((a.row, "(iii) row %d first crossing c = %s before d = %s (exit %s)"
                      % (a.row, pos_str(mk, a.c_pos), pos_str(mk, a.d_pos), t.exit_name)))
        if a.c_pos is not None and a.c_pos == a.d_pos and a.kind != "XStop":       # (iii) c == d, not XStop
            ok = a.flat_d and (a.kind == "SESSION_CLOSE" or (a.kind == "FLATEOD" and pol == "Flat1559"))
            if not ok:
                v.append((a.row, "(iii) row %d c = d = %s but exit %r is not XStop nor the session flat on F"
                          % (a.row, pos_str(mk, a.d_pos), t.exit_name)))
    pred = sum(1 for a in r.anns if a.c_pos is not None and not a.c_flat)
    act = sum(1 for a in r.anns if a.kind == "XStop")
    if pred != act:                                                               # (iv)
        v.append((None, "(iv) XStop count %d != predicted %d (trades with c off a session-flat bar)" % (act, pred)))
    return v, pred, act


def _wrong_predictions(ctx, r, a):
    """Predicted c' under the four named wrong stops (values-spec T8 power check (b))."""
    mk, t = ctx.market, a.trade
    P = r.params
    m, k = P["StopAtrMult"], P["NoiseMult"]
    F = Fraction
    out = {}
    if not a.have_atr or a.d_pos is None or a.d_pos < a.entry_pos:
        return {w: None for w in WRONG_STOPS}

    def scan(dist, only=None):
        for p in iter_pos(mk, a.entry_pos, a.d_pos):
            if only is not None and not only(p):
                continue
            cl = F(bar_at(mk, p).c)
            gap = (F(t.entry_price) - cl) if t.side == "Long" else (cl - F(t.entry_price))
            if gap >= dist:
                return p
        return None
    # (1) ATR of the last 14 one-minute bars: mean 1-minute TR max(h, prev c) - min(l, prev c) of the 14
    #     bars ending at the entry decision bar (INFERRED reading).
    trs, p = [], a.entry_dec_pos
    while p is not None and len(trs) < 14:
        q = prev_pos(mk, p)
        if q is None:
            break
        b, pc = bar_at(mk, p), bar_at(mk, q).c
        trs.append(F(max(b.h, pc)) - F(min(b.l, pc)))
        p = q
    out["atr14min"] = scan(F(m) * sum(trs) / 14) if len(trs) == 14 else None
    # (2) m x the entry decision bar's band half-width (upper - lower)/2 at the run's Lookback/k.
    st = ctx.band(a.entry_dec_pos, P["Lookback"], k)
    out["band_halfwidth"] = scan(F(m) * (F(st.upper) - F(st.lower)) / 2) if st.have_band else None
    # (3) k in place of m: level = fill -/+ k x ATR(14).
    out["k_for_m"] = scan(F(repr(k)) * F(a.atr_sum) / 14)
    # (4) the correct level checked only at HH:00/HH:30 checkpoints.
    out["checkpoint_only"] = first_crossing(mk, t.side, t.entry_price, m, a.atr_sum, a.entry_pos, a.d_pos,
                                            only=lambda q: _mk.is_checkpoint(bar_at(mk, q).mod))
    return out


WRONG_STOPS = ("atr14min", "band_halfwidth", "k_for_m", "checkpoint_only")
WRONG_TEXT = {"atr14min": "(1) ATR of the last 14 one-minute bars",
              "band_halfwidth": "(2) m x the entry decision bar's band half-width",
              "k_for_m": "(3) k in place of m",
              "checkpoint_only": "(4) stop checked only at HH:00/HH:30"}


def grade_t8(ctx):
    mk = ctx.market
    if not ctx.fillfit:
        grade_fillfit(ctx)
    out, per_run = [], {}
    for r in ctx.runs:
        v, pred, act = _t8_findings(ctx, r)
        amb = [a.row for a in r.anns if a.ambiguous]
        lines = ["XStop count %d; predicted %d" % (act, pred)] + [x for _r, x in v]
        if amb:
            lines.append("ambiguous first-bar-of-session entries (not graded): rows %s" % amb)
        rows = sorted({x for x, _ in v if x is not None})
        if not ctx.fillfit.get(r.label):
            vd = Verdict("T8(i-iv)", "UNTESTED", "fill rules do not fit (calibration from T1/T3 on the VM is a "
                         "separate step); findings below are NOT graded", rows, lines, r.label)
        elif v:
            vd = Verdict("T8(i-iv)", "FAIL", "%d violation(s) of (i)-(iv)" % len(v), rows, lines, r.label)
        elif amb:
            vd = Verdict("T8(i-iv)", "UNTESTED", "first-bar-of-session entries whose stop depends on an UNVERIFIED "
                         "event order", amb, lines, r.label)
        else:
            vd = Verdict("T8(i-iv)", "PASS", "(i)-(iv) hold; XStop count %d = predicted %d" % (act, pred),
                         [a.row for a in r.anns if a.kind == "XStop" or a.c_pos is not None], lines, r.label)
        per_run[r.label] = vd
        out.append(vd)
    # power (b): across all runs given
    found, plines = {}, []
    for r in ctx.runs:
        for a in r.anns:
            if a.ambiguous:
                continue
            wp = _wrong_predictions(ctx, r, a)
            for w in WRONG_STOPS:
                if w not in found and wp[w] != a.c_pos:
                    found[w] = "%s#%d" % (r.label, a.row)
                    plines.append("%s: differs on %s#%d — correct c = %s, wrong c' = %s"
                                  % (WRONG_TEXT[w], r.label, a.row, pos_str(mk, a.c_pos), pos_str(mk, wp[w])))
    missing = [w for w in WRONG_STOPS if w not in found]
    plines += ["%s: NO trade differs" % WRONG_TEXT[w] for w in missing]
    if missing:
        pb = Verdict("T8 power (b)", "UNTESTED", "no differing trade for: %s" % ", ".join(WRONG_TEXT[w] for w in missing),
                     sorted(set(found.values())), plines, "all")
    else:
        pb = Verdict("T8 power (b)", "PASS", "every named wrong stop moves at least one exit in the runs given",
                     sorted(set(found.values())), plines, "all")
    out.append(pb)
    # aggregate per m, with power (a)
    for m in STOP_GRID:
        rs = [r for r in ctx.runs if r.params["StopAtrMult"] == m]
        if not rs:
            out.append(Verdict("T8 m=%r" % m, "UNTESTED", "no run at this m in this invocation", [], [], "all"))
            continue
        nl = [("%s#%d" % (r.label, a.row)) for r in rs for a in r.anns if a.kind == "XStop" and a.trade.side == "Long"]
        ns = [("%s#%d" % (r.label, a.row)) for r in rs for a in r.anns if a.kind == "XStop" and a.trade.side == "Short"]
        lines = ["runs: %s" % ", ".join(r.label for r in rs),
                 "power (a): long XStops %d %s, short XStops %d %s" % (len(nl), nl[:5], len(ns), ns[:5])]
        fails = [per_run[r.label] for r in rs if per_run[r.label].verdict == "FAIL"]
        unt = [per_run[r.label] for r in rs if per_run[r.label].verdict == "UNTESTED"]
        if fails:
            vd = Verdict("T8 m=%r" % m, "FAIL", "(i)-(iv) fail in %s" % ", ".join(x.run for x in fails),
                         ["%s#%d" % (x.run, y) for x in fails for y in x.rows], lines, "all")
        elif unt:
            vd = Verdict("T8 m=%r" % m, "UNTESTED", "not graded in %s: %s" % (", ".join(x.run for x in unt), unt[0].reason),
                         [], lines, "all")
        elif not nl or not ns:
            vd = Verdict("T8 m=%r" % m, "UNTESTED", "power check (a): the runs at m=%r hold %d long and %d short XStop(s); "
                         "T8 is not passed at this m (report to the master)" % (m, len(nl), len(ns)), [], lines, "all")
        elif pb.verdict != "PASS":
            vd = Verdict("T8 m=%r" % m, "UNTESTED", "power check (b) not met: " + pb.reason, [], lines, "all")
        else:
            vd = Verdict("T8 m=%r" % m, "PASS", "(i)-(iv) hold in every run at this m; power (a) and (b) met",
                         (nl[:1] + ns[:1]), lines, "all")
        out.append(vd)
    return out


def grade_t9(ctx):
    mk, out = ctx.market, []
    for r in ctx.runs:
        pol = r.params["ExitPolicy"]
        v, lines, pw = [], [], []
        for a in r.anns:
            t = a.trade
            if a.kind == "XStop" and a.flat_d:
                v.append((a.row, "row %d XStop decided on session-flat bar %s" % (a.row, pos_str(mk, a.d_pos))))
            F1 = a.first_f
            if a.entry_pos <= F1 and a.d_pos is not None and a.d_pos >= F1:       # still open at the first F
                want = FLATEOD if (pol == "Flat1559" and bar_at(mk, F1).mod == _mk.FLATTEN_MOD) else SESSION_CLOSE
                if a.d_pos != F1 or t.exit_name != want:
                    v.append((a.row, "row %d open at first F %s: exit %r decided %s; expected %r decided on F"
                              % (a.row, pos_str(mk, F1), t.exit_name, pos_str(mk, a.d_pos), want)))
            if a.c_flat:
                pw.append(a.row)
                lines.append("row %d first crossing on session-flat bar %s, exit %r"
                             % (a.row, pos_str(mk, a.c_pos), t.exit_name))
        lines += [x for _r, x in v]
        if v:
            out.append(Verdict("T9", "FAIL", "%d violation(s)" % len(v), sorted({x for x, _ in v}), lines, r.label))
        elif pw:
            out.append(Verdict("T9", "PASS", "no XStop on a session-flat bar; every trade open at F exits by the "
                               "session flat; %d trade(s) cross on F" % len(pw), pw, lines, r.label))
        else:
            out.append(Verdict("T9", "UNTESTED", "no trade's first crossing falls on a session-flat bar", [], lines, r.label))
    return out


def grade_t10(ctx):
    mk, out = ctx.market, []
    for r in ctx.runs:
        P = r.params
        entries = {}
        for a in r.anns:
            entries.setdefault(a.entry_pos, []).append(a.row)
        v, pw, lines = [], [], []
        for a in r.anns:
            if a.kind != "XStop":
                continue
            hit = entries.get(a.exit_pos)
            if hit:
                v.append((a.row, hit))
                lines.append("row %d XStop fills %s; entry row(s) %s fill on that bar"
                             % (a.row, pos_str(mk, a.exit_pos), hit))
            d = a.d_pos
            if d is None or not _mk.is_checkpoint(bar_at(mk, d).mod):
                continue
            st = ctx.band(d, P["Lookback"], P["NoiseMult"])
            have_atr = _atr.atr_at(mk, d[0])[0]
            c = bar_at(mk, d).c
            side = a.trade.side
            if st.have_band and have_atr and ((c > st.upper and side != "Long") or (c < st.lower and side != "Short")):
                pw.append(a.row)
                lines.append("row %d XStop decided at checkpoint %s where the entry rule holds (close %r, band %r..%r)"
                             % (a.row, pos_str(mk, d), c, st.lower, st.upper))
        if v:
            out.append(Verdict("T10", "FAIL", "%d entr(ies) fill on an XStop fill bar" % len(v),
                               sorted({x for p in v for x in [p[0]] + p[1]}), lines, r.label))
        elif pw:
            out.append(Verdict("T10", "PASS", "no entry on an XStop fill bar; %d XStop decision bar(s) are checkpoints "
                               "where the entry rule would enter" % len(pw), pw, lines, r.label))
        else:
            out.append(Verdict("T10", "UNTESTED", "no XStop decision bar is a checkpoint where the entry rule would "
                               "enter", [], lines, r.label))
    return out


def _scan_entry(ctx, P, n_from, n_to, need_atr):
    """First checkpoint (pos, side) in sessions n_from..n_to where the band exists (and ATR, if need_atr) and
    Close > Upper (Long) or Close < Lower (Short); the position is flat before a run's first entry."""
    mk = ctx.market
    for n in range(n_from, min(n_to, mk.N) + 1):
        if need_atr and not _atr.atr_at(mk, n)[0]:
            continue
        sts = ctx.states(n, P["Lookback"], P["NoiseMult"])
        for i, b in enumerate(mk.sessions[n - 1].bars):
            if not _mk.is_checkpoint(b.mod):
                continue
            st = sts[i]
            if not st.have_band:
                continue
            if b.c > st.upper:
                return (n, i), "Long"
            if b.c < st.lower:
                return (n, i), "Short"
    return None, None


def grade_t11(ctx):
    mk, out = ctx.market, []
    for r in ctx.runs:
        P = r.params
        early = [a for a in r.anns if a.entry_pos[0] < FIRST_ATR_SESSION]
        wpos, wside = _scan_entry(ctx, P, 1, FIRST_ATR_SESSION - 1, False)
        lines = ["oracle: first checkpoint before s16 with band and rule: %s %s" % (pos_str(mk, wpos), wside or "")]
        lines += ["row %d entry fills %s (before s16)" % (a.row, pos_str(mk, a.entry_pos)) for a in early]
        if early:
            out.append(Verdict("T11(i)", "FAIL", "%d entr(ies) fill before s16" % len(early), [a.row for a in early],
                               lines, r.label))
        elif wpos is not None:
            out.append(Verdict("T11(i)", "PASS", "no entry before s16 although the band rule would enter at %s"
                               % pos_str(mk, wpos), [], lines, r.label))
        else:
            out.append(Verdict("T11(i)", "UNTESTED", "no checkpoint before s16 at which the band exists and the rule "
                               "holds (possible only at Lookback 10, s12-s15)", [], lines, r.label))
        opos, oside = _scan_entry(ctx, P, 1, mk.N, True)
        first = min(r.anns, key=lambda a: a.entry_pos) if r.anns else None
        fdec = first.entry_dec_pos if first else None
        lines = ["oracle first entry decision: %s %s" % (pos_str(mk, opos), oside or ""),
                 "run first entry decision:    %s %s%s" % (pos_str(mk, fdec), first.trade.side if first else "",
                                                          " (row %d)" % first.row if first else "")]
        if first is None and opos is None:
            out.append(Verdict("T11(ii)", "UNTESTED", "no trade and no oracle entry", [], lines, r.label))
        elif first is not None and fdec == opos and first.trade.side == oside:
            out.append(Verdict("T11(ii)", "PASS", "first entry decided at the oracle's first checkpoint %s"
                               % pos_str(mk, opos), [first.row], lines, r.label))
        else:
            out.append(Verdict("T11(ii)", "FAIL", "first entry decided %s, oracle %s"
                               % (pos_str(mk, fdec) + (" " + first.trade.side if first else ""),
                                  pos_str(mk, opos) + (" " + oside if oside else "")),
                               [first.row] if first else [], lines, r.label))
    return out


GRADERS = [grade_fillfit, grade_t8, grade_t9, grade_t10, grade_t11]
T12_MISSING = "T12: not built in this file (policy.py)"


def load_policy():
    """(module or None, error text or None). W3's policy.py must expose grade_t12(ctx) -> [Verdict]."""
    path = os.path.join(_HERE, "policy.py")
    if not os.path.isfile(path):
        return None, None
    try:
        mod = _load_by_path("policy", path)
        if not hasattr(mod, "grade_t12"):
            return None, "policy.py has no grade_t12"
        return mod, None
    except Exception as e:  # noqa: BLE001 — reported in the sheet
        sys.modules.pop("policy", None)
        return None, "%s: %s" % (type(e).__name__, e)


def run_graders(ctx):
    verdicts = []
    for g in GRADERS:
        verdicts.extend(g(ctx))
    pol, err = load_policy()
    t12 = None
    if pol is not None:
        t12 = list(pol.grade_t12(ctx))
        verdicts.extend(t12)
    return verdicts, t12, err


# ---------------------------------------------------------------------------------------------------
# sheet
# ---------------------------------------------------------------------------------------------------

def _section(L, vs):
    for v in vs:
        L.append("### %s%s — %s" % (v.test, "" if v.run in (None, "all") else " [%s]" % v.run, v.verdict))
        L.append("")
        L.append("Reason: %s" % v.reason)
        L.append("Deciding rows: %s" % (", ".join(str(x) for x in v.rows) if v.rows else "none"))
        for x in v.lines:
            L.append("- %s" % x)
        L.append("")


def render(ctx, verdicts, t12, t12_err):
    mk = ctx.market
    L = ["# Oracle grade sheet — %s" % ", ".join(r.label for r in ctx.runs), "", STANDING_LIMITATION,
         "Oracle status: UNVERIFIED against NT8 (until the 2a comparison). Fill rules are the results-report "
         "defaults (docs/reports/2026-11-01-three-strategy-results.md:133-135, :255): market order = next bar's "
         "open, 2 ticks adverse, clipped; exit on session close = F's close, 2 ticks adverse, clipped; FlatEOD = "
         "the 16:00 bar's open, 2 ticks adverse, clipped. Not refitted from T1/T3.", "",
         "## Inputs", "",
         "- data: %s — sha256 %s (%d sessions)" % (mk.source.get("path"), mk.source.get("sha256"), mk.N),
         "- %s; pre-open bars loaded %d; pre-open-only weekdays dropped %d%s" % (
             _mk.session_start_line(mk), mk.pre_open_bars, len(mk.pre_open_only_dropped),
             (" (%s; UNVERIFIED whether NT8 makes them sessions)" % ", ".join(mk.pre_open_only_dropped))
             if mk.pre_open_only_dropped else "")]
    for r in ctx.runs:
        L.append("- %s: %s %s — sha256 %s (%d trades)" % (r.label, r.fmt, r.path, r.sha256, len(r.anns)))
    L += ["", "## Run parameters", "", "| label | Lookback | NoiseMult | StopAtrMult | ExitPolicy |", "|---|---|---|---|---|"]
    for r in ctx.runs:
        P = r.params
        L.append("| %s | %d | %r | %r | %s |" % (r.label, P["Lookback"], P["NoiseMult"], P["StopAtrMult"], P["ExitPolicy"]))
    L += ["", "## Summary", "", "| test | run | verdict |", "|---|---|---|"]
    for v in verdicts:
        L.append("| %s | %s | %s |" % (v.test, v.run, v.verdict))
    L += ["", "## Trade annotation notes", ""]
    nn = 0
    for r in ctx.runs:
        for a in r.anns:
            for x in a.notes:
                L.append("- %s row %d: %s" % (r.label, a.row, x))
                nn += 1
    if not nn:
        L.append("- none")
    L.append("")
    groups = [("Fill-rule fit", lambda t: t == "FILLFIT"), ("T8", lambda t: t.startswith("T8")),
              ("T9", lambda t: t == "T9"), ("T10", lambda t: t == "T10"), ("T11", lambda t: t.startswith("T11"))]
    for title, f in groups:
        L += ["## %s" % title, ""]
        _section(L, [v for v in verdicts if f(v.test)])
    L += ["## T12", ""]
    if t12 is None:
        L.append(T12_MISSING + (" (import error: %s)" % t12_err if t12_err else ""))
        L.append("")
    else:
        _section(L, t12)
    text = "\n".join(L) + "\n"
    lines = text.splitlines()
    if _norm(text).count(STANDING_PHRASE) != 1 or lines[2] != STANDING_LIMITATION:
        raise GradeInputError("grade sheet has the standing sentence %d time(s) / not at line 3 — not written"
                              % _norm(text).count(STANDING_PHRASE))
    return text


# ---------------------------------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------------------------------

def _read_manifest(path):
    with open(path, "r", encoding="utf-8") as fh:
        doc = json.load(fh)
    if not isinstance(doc, list) or not doc:
        raise GradeInputError("%s: run manifest must be a non-empty JSON list" % path)
    base = os.path.dirname(os.path.abspath(path))
    out = []
    for j, sp in enumerate(doc):
        if not isinstance(sp, dict) or "path" not in sp:
            raise GradeInputError("%s: entry %d must be an object with a 'path'" % (path, j))
        sp = dict(sp)
        if not os.path.isabs(sp["path"]):
            sp["path"] = os.path.join(base, sp["path"])
        out.append(sp)
    return out


def build_parser():
    ap = argparse.ArgumentParser(description="arm (b) T8-T11 grader (test oracle; trades nothing)")
    ap.add_argument("--data", default=DEFAULT_DATA)
    ap.add_argument("--out")
    ap.add_argument("--runs", help="JSON run manifest")
    ap.add_argument("--trades")
    ap.add_argument("--format", choices=("bridge", "nt8csv"))
    ap.add_argument("--label", default="run1")
    ap.add_argument("--lookback")
    ap.add_argument("--noise-mult")
    ap.add_argument("--stop-atr-mult")
    ap.add_argument("--exit-policy")
    ap.add_argument("--session-start", required=True, choices=sorted(_mk.SESSION_STARTS),
                    help="REQUIRED, no default: 09:31 = %s; 08:31 = %s" % (_mk.SESSION_STARTS["09:31"],
                                                                         _mk.SESSION_STARTS["08:31"]))
    ap.add_argument("--start", default=_mk.sessions.RANGE[0])
    ap.add_argument("--end", default=_mk.sessions.RANGE[1])
    return ap


def main(argv=None):
    a = build_parser().parse_args(argv)
    try:
        if a.runs:
            if a.trades:
                raise GradeInputError("give --runs or --trades, not both")
            specs = _read_manifest(a.runs)
        else:
            if not (a.trades and a.format):
                raise GradeInputError("give --runs FILE, or --trades FILE --format F with the four parameters")
            specs = [{"label": a.label, "path": a.trades, "format": a.format, "Lookback": a.lookback,
                      "NoiseMult": a.noise_mult, "StopAtrMult": a.stop_atr_mult, "ExitPolicy": a.exit_policy}]
        for j, sp in enumerate(specs):              # parameters before the (slow) data load
            check_params(sp, "run %r" % sp.get("label", j + 1))
        market = _mk.load_market(a.data, a.start, a.end, session_start=a.session_start)
        ctx = build_ctx(market, specs)
        verdicts, t12, err = run_graders(ctx)
        text = render(ctx, verdicts, t12, err)
    except (GradeInputError, tradelist.TradelistError, _mk.DataError, _mk.NotSettledBySpec, OSError, ValueError) as e:
        sys.stderr.write("grade.py: input error: %s\n" % e)
        return 2
    if a.out:
        with open(a.out, "w", encoding="utf-8") as fh:
            fh.write(text)
    else:
        sys.stdout.write(text)
    return 1 if any(v.verdict == "FAIL" for v in verdicts) else 0


if __name__ == "__main__":
    sys.exit(main())
