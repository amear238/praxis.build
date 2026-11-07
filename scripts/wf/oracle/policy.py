#!/usr/bin/env python3
"""policy.py — T12 grader (ExitPolicy under the stop) for arm (b) runs (unit 2026-11-07-wf-oracles, U3b-2, W3).

Test oracle only: it trades nothing and is not the walk-forward. grade.py's load_policy() loads this file by
path and calls grade_t12(ctx) -> [grade.Verdict]; the verdicts are rendered in the sheet's "## T12" section.

Acceptance text: docs/specs/2026-11-06-walk-forward-values.md T12 :203-212 ((i)-(vii) and the paragraph after
(vii)); T8's decision bar d and session-flat bar F (:195); §3's exit-policy definitions (:56-59); §4 precedence
with the v2.1 correction (:77).

Strategy read ONLY via `git show origin/arm-b/wf-tunables:ninjascript/PraxisNoiseAreaBreakoutArmB.cs` (never
checked out, never copied). Line numbers below are that file's:
  :233-239  (1) session flat: flatMod = 959 under Flat1559 else 960; `if (mod >= flatMod) { FlattenAll; return; }`
            — returns BEFORE the stop and the checkpoint.
  :244      isSessionLastBar (early-close last bar) — suppresses ONLY the stop (:250); no return there.
  :250-269  (2) stop on every bar; on a firing bar `return` (no checkpoint exit, no entry on that bar).
  :272-274  (3) isCheckpoint = (Minute==0||Minute==30) && mod > 570 && mod < 960; `if (!isCheckpoint ||
            !haveBand) return;` — no band, nothing is checked.
  :279-289  long: OppBand trail = curLower; else trail = vwapCumVol > 0 ? Math.Max(curUpper, curVwap) : curUpper;
            `if (price <= trail) ExitLong("XL")`.
  :290-300  short: OppBand trail = curUpper; else vwapCumVol > 0 ? Math.Min(curLower, curVwap) : curLower;
            `if (price >= trail) ExitShort("XS")`.
  :303-310  entries: atrGateOpen = m <= 0 || haveAtr; `price > curUpper && mp != Long -> EnterLong`, else
            `price < curLower && mp != Short -> EnterShort` (strict). `mp` here is Position.MarketPosition, still
            the old side on the bar an XL/XS is submitted, so a long's XL reverses only through `price < curLower`.

Every comparison uses Python floats in the code's operation order: the band, VWAP and trail come from band.py
(BuildBand :342-370, VWAP :213-218/:368), compared exactly like the C# doubles. A comparison within 1e-9
relative of its level is a tie (T12(vi)): listed, NOT graded.

UNVERIFIED: every oracle value is unverified against NT8 until the 2a comparison; the FlatEOD fill rule is the
results-report default (market.flateod_fill), not refitted from T3 (gated on grade.py's fill-rule fit).
Standard library only.
"""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
import grade as _gr   # noqa: E402  (grade.py registers itself as sys.modules['grade'] when run as __main__)
import market as _mk  # noqa: E402
import atr as _atr    # noqa: E402

TIE_REL = 1e-9                                   # T12(vi) :210
T12_VALUES = (14, 1.0, 1.5)                      # T12 :203 — (Lookback, NoiseMult, StopAtrMult) of T12a-c
TRIO = (("T12a", "BandOrVWAP"), ("T12b", "OppBand"), ("T12c", "Flat1559"))
FIRST_ENTRY_SESSION = _gr.FIRST_ATR_SESSION      # 16: T12(v) "a session at or after s16"
MAX_LINES = 60


def rule_of(policy):
    """The checkpoint-exit rule a policy runs (.cs :283/:294): OppBand, or BandOrVWAP (also Flat1559, §3 :59)."""
    _mk.check_policy(policy)
    return "OppBand" if policy == "OppBand" else "BandOrVWAP"


def exit_level(rule, side, st):
    """The .cs `trail` for `side` under `rule` from BandState st (have_band True). :284/:286, :295/:297."""
    if rule == "OppBand":
        return st.lower if side == "Long" else st.upper
    if side == "Long":
        return max(st.upper, st.vwap) if st.vwap_cum_vol > 0 else st.upper      # Math.Max(curUpper, curVwap)
    return min(st.lower, st.vwap) if st.vwap_cum_vol > 0 else st.lower          # Math.Min(curLower, curVwap)


def exit_holds(side, close, level):
    """:287 `price <= trail` (long), :298 `price >= trail` (short)."""
    return close <= level if side == "Long" else close >= level


def is_tie(close, level):
    """T12(vi): |Close - level| <= 1e-9 x |level|."""
    return abs(close - level) <= TIE_REL * abs(level)


def is_policy_checkpoint(market, pos, policy):
    """A T12(iii) checkpoint: .cs :272 isCheckpoint and NOT a session-flat bar F for the policy (T12(iii) :207:
    'not a session-flat bar F'; at F the flat comes first, §4 :77). The band test is the caller's (:273)."""
    return _mk.is_checkpoint(_gr.bar_at(market, pos).mod) and not _gr.is_flat_pos(market, pos, policy)


class Walk(object):
    """Result of a c* walk: c = first checkpoint where the exit holds (or None); tie = (pos, close, level) of a
    tie met before any c* (then c is None and the walk is not graded); n = checkpoints examined."""
    __slots__ = ("c", "tie", "n")

    def __init__(self, c=None, tie=None, n=0):
        self.c, self.tie, self.n = c, tie, n


def walk_cstar(ctx, params, ann, rule):
    """T12(iii) :207: walk the checkpoints strictly after the entry's decision bar (i.e. from the entry fill bar)
    up to and including d, skipping F bars of the RUN's policy and bars without a band (:273); c* = the first one
    at which `rule`'s exit condition holds for the trade's side. A tie stops the walk ungraded."""
    mk, side = ctx.market, ann.trade.side
    L, k, pol = params["Lookback"], params["NoiseMult"], params["ExitPolicy"]
    w = Walk()
    if ann.d_pos is None or ann.d_pos < ann.entry_pos:
        return w
    for p in _gr.iter_pos(mk, ann.entry_pos, ann.d_pos):
        if not is_policy_checkpoint(mk, p, pol):
            continue
        st = ctx.band(p, L, k)
        if not st.have_band:                       # :273 `if (!isCheckpoint || !haveBand) return;`
            continue
        w.n += 1
        close = _gr.bar_at(mk, p).c
        lvl = exit_level(rule, side, st)
        if is_tie(close, lvl):
            w.tie = (p, close, lvl)
            return w
        if exit_holds(side, close, lvl):
            w.c = p
            return w
    return w


# ---------------------------------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------------------------------

def _cap(lines):
    if len(lines) > MAX_LINES:
        return lines[:MAX_LINES] + ["... %d more line(s)" % (len(lines) - MAX_LINES)]
    return lines


def _vals(params):
    return (params["Lookback"], float(params["NoiseMult"]), float(params["StopAtrMult"]))


def find_trio(ctx):
    """{tag: GradedRun or None}, picked BY PARAMETERS (14, 1.0, 1.5, policy), never by label; the first match in
    the given order wins, later matches are reported in notes."""
    trio, notes = {}, []
    for tag, pol in TRIO:
        hits = [r for r in ctx.runs if _vals(r.params) == T12_VALUES and r.params["ExitPolicy"] == pol]
        trio[tag] = hits[0] if hits else None
        if len(hits) > 1:
            notes.append("%s: %d runs at (14, 1.0, 1.5, %s): %s; using %s" % (tag, len(hits), pol,
                                                                            [h.label for h in hits], hits[0].label))
    return trio, notes


def _row_key(t):
    return (t.entry_dt, t.exit_dt, t.entry_price, t.exit_price, t.side, t.exit_name)


def _verdict(test, run, bad, graded_rows, lines, pass_reason, untested_reason, bad_rows=None):
    if bad:
        return _gr.Verdict(test, "FAIL", "%d violation(s)" % len(bad), sorted(set(bad_rows or [r for r, _ in bad])),
                           _cap([x for _r, x in bad] + lines), run)
    if graded_rows:
        return _gr.Verdict(test, "PASS", pass_reason % len(graded_rows), sorted(set(graded_rows)), _cap(lines), run)
    return _gr.Verdict(test, "UNTESTED", untested_reason, [], _cap(lines), run)


# ---------------------------------------------------------------------------------------------------
# (i) pairwise difference
# ---------------------------------------------------------------------------------------------------

def grade_i(ctx, trio):
    missing = [tag for tag, _p in TRIO if trio[tag] is None]
    if missing:
        return _gr.Verdict("T12(i)", "UNTESTED", "trio incomplete: no run at (14, 1.0, 1.5, %s) for %s"
                           % ("/".join(p for t, p in TRIO if t in missing), ", ".join(missing)), [], [], "all")
    lines, bad, rows = [], [], []
    tags = [t for t, _p in TRIO]
    for x in range(3):
        for y in range(x + 1, 3):
            A, B = trio[tags[x]], trio[tags[y]]
            ta, tb = A.run.trades, B.run.trades
            diff = None
            for j in range(max(len(ta), len(tb))):
                if j >= len(ta) or j >= len(tb) or _row_key(ta[j]) != _row_key(tb[j]):
                    diff = j
                    break
            pair = "%s (%s) vs %s (%s)" % (tags[x], A.label, tags[y], B.label)
            if diff is None:
                bad.append(pair)
                lines.append("%s: IDENTICAL — %d rows, every row equal" % (pair, len(ta)))
            else:
                ra = ta[diff] if diff < len(ta) else None
                rb = tb[diff] if diff < len(tb) else None
                rows += ["%s#%d" % (A.label, diff + 1)] if ra else []
                rows += ["%s#%d" % (B.label, diff + 1)] if rb else []
                lines.append("%s: first differing row %d (%d vs %d trades): %r | %r" % (pair, diff + 1, len(ta), len(tb),
                                                                                   ra, rb))
    if bad:
        return _gr.Verdict("T12(i)", "FAIL", "pair(s) with no differing trade row: %s" % "; ".join(bad), [], lines, "all")
    return _gr.Verdict("T12(i)", "PASS", "each of the three pairs has a differing trade row", rows, lines, "all")


# ---------------------------------------------------------------------------------------------------
# (ii) names
# ---------------------------------------------------------------------------------------------------

def grade_ii(ctx, r, in_trio):
    mk, pol = ctx.market, r.params["ExitPolicy"]
    allowed = {"XL", "XS", "XStop", _gr.SESSION_CLOSE} | ({_gr.FLATEOD} if pol == "Flat1559" else set())
    if r.label not in ctx.fillfit:
        _gr.grade_fillfit(ctx)
    fit = ctx.fillfit.get(r.label, False)
    bad, lines, graded, n_xlxs, price_skipped = [], [], [], 0, []
    for a in r.anns:
        t, row, name = a.trade, a.row, a.trade.exit_name
        graded.append(row)
        if name in ("XL", "XS"):
            n_xlxs += 1
        if name == "XL" and t.side != "Long":
            bad.append((row, "row %d: XL closes a %s (XL must close a Long, .cs :288)" % (row, t.side)))
        if name == "XS" and t.side != "Short":
            bad.append((row, "row %d: XS closes a %s (XS must close a Short, .cs :299)" % (row, t.side)))
        if name not in allowed:
            bad.append((row, "row %d: exit name %r not allowed under %s (allowed %s)" % (row, name, pol, sorted(allowed))))
        if pol != "Flat1559":
            continue
        xb = _gr.bar_at(mk, a.exit_pos)
        n, i = a.exit_pos
        s = mk.sessions[n - 1]
        if a.kind == "FLATEOD" and not (xb.mod == _mk.CLOSE_MOD and a.d_pos is not None
                                        and _gr.bar_at(mk, a.d_pos).mod == _mk.FLATTEN_MOD):
            bad.append((row, "row %d: FlatEOD fills %s, not on the 16:00 bar after a 15:59 decision (.cs :234-235)"
                        % (row, _gr.pos_str(mk, a.exit_pos))))
        if a.kind == "SESSION_CLOSE":
            if xb.mod == _mk.CLOSE_MOD:
                bad.append((row, "row %d: '%s' on a 16:00 bar %s under Flat1559 (the 15:59 flatten precedes it)"
                            % (row, _gr.SESSION_CLOSE, _gr.pos_str(mk, a.exit_pos))))
            elif not (s.early and i == len(s.bars) - 1):
                bad.append((row, "row %d: '%s' at %s is not an early-close day's last bar"
                            % (row, _gr.SESSION_CLOSE, _gr.pos_str(mk, a.exit_pos))))
        F1 = a.first_f
        if _gr.bar_at(mk, F1).mod != _mk.FLATTEN_MOD or not (a.entry_pos <= F1 and a.d_pos is not None and a.d_pos >= F1):
            continue
        # open at the close of a 15:59-stamped bar: FlatEOD decided there (mod >= 959, .cs :234-235), filled on 16:00
        nx = _gr.next_pos(mk, F1)
        if nx is None or nx[0] != F1[0] or _gr.bar_at(mk, nx).mod != _mk.CLOSE_MOD:
            lines.append("row %d open at 15:59 %s but the session has no 16:00 bar: placement not graded"
                         % (row, _gr.pos_str(mk, F1)))
            continue
        if a.kind != "FLATEOD" or a.d_pos != F1 or a.exit_pos != nx:
            bad.append((row, "row %d open at the close of 15:59 %s: exit %r filled %s; expected FlatEOD filled %s"
                        % (row, _gr.pos_str(mk, F1), name, _gr.pos_str(mk, a.exit_pos), _gr.pos_str(mk, nx))))
            continue
        want = _mk.flateod_fill(_gr.bar_at(mk, nx), t.side == "Short")
        if not fit:
            price_skipped.append(row)
            lines.append("row %d FlatEOD price %r vs rule %r: NOT graded (fill rules do not fit this run)"
                         % (row, t.exit_price, want))
        elif not _gr._eq(t.exit_price, want):
            bad.append((row, "row %d FlatEOD price %r != FlatEOD rule %r (16:00 open, 2 ticks adverse, clipped)"
                        % (row, t.exit_price, want)))
        else:
            lines.append("row %d open at 15:59 exits FlatEOD %s at %r (rule)" % (row, _gr.pos_str(mk, nx), want))
    lines.insert(0, "XL/XS exits: %d" % n_xlxs)
    if bad:
        return _gr.Verdict("T12(ii)", "FAIL", "%d name violation(s)" % len(bad), sorted({x for x, _ in bad}),
                           _cap([x for _r, x in bad] + lines), r.label)
    if in_trio and n_xlxs == 0:
        return _gr.Verdict("T12(ii)", "FAIL", "no XL or XS exit (each of T12a-c needs >= 1)", [], _cap(lines), r.label)
    if price_skipped:
        return _gr.Verdict("T12(ii)", "UNTESTED", "names hold; FlatEOD prices not graded: fill rules do not fit "
                           "(calibration from T3 on the VM is a separate step)", price_skipped, _cap(lines), r.label)
    if not graded:
        return _gr.Verdict("T12(ii)", "UNTESTED", "no trades", [], lines, r.label)
    return _gr.Verdict("T12(ii)", "PASS", "every exit name fits %s (%d trades)" % (pol, len(graded)),
                       graded, _cap(lines), r.label)


# ---------------------------------------------------------------------------------------------------
# (iii) policy-rule oracle, (iv) reversal, (v) entry soundness, (vi) ties
# ---------------------------------------------------------------------------------------------------

def grade_iii(ctx, r, ties):
    mk, rule = ctx.market, rule_of(r.params["ExitPolicy"])
    bad, lines, graded = [], [], []
    for a in r.anns:
        row = a.row
        if a.d_pos is None or a.d_pos < a.entry_pos:
            lines.append("row %d: d precedes the entry fill; not graded" % row)
            continue
        w = walk_cstar(ctx, r.params, a, rule)
        if w.tie is not None:
            p, c, lvl = w.tie
            ties.append("(iii) row %d: checkpoint %s close %r vs %s level %r — tie, not graded"
                        % (row, _gr.pos_str(mk, p), c, rule, lvl))
            continue
        graded.append(row)
        d, cs = _gr.pos_str(mk, a.d_pos), _gr.pos_str(mk, w.c)
        if a.kind in ("XL", "XS", "OTHER"):
            if w.c != a.d_pos:
                bad.append((row, "row %d %s %s decided %s but c* = %s (%s rule, %d checkpoint(s) walked)"
                            % (row, a.trade.side, a.trade.exit_name, d, cs, rule, w.n)))
            else:
                lines.append("row %d %s %s: c* = d = %s" % (row, a.trade.side, a.trade.exit_name, d))
        else:                                       # XStop / Exit on session close / FlatEOD
            if w.c is not None and w.c < a.d_pos:
                bad.append((row, "row %d %s %s decided %s but the %s exit holds earlier at c* = %s"
                            % (row, a.trade.side, a.trade.exit_name, d, rule, cs)))
            else:
                lines.append("row %d %s %s decided %s: no c* before d (c* = %s)" % (row, a.trade.side,
                                                                                   a.trade.exit_name, d, cs))
    return _verdict("T12(iii)", r.label, bad, graded, lines,
                    "every graded trade's exit agrees with the %s rule (%%d trades)" % rule,
                    "no trade graded (none, or all ties)")


def grade_iv(ctx, r, ties):
    mk, P = ctx.market, r.params
    order = sorted(r.anns, key=lambda a: (a.entry_pos, a.row))
    bad, lines, graded, bad_rows = [], [], [], []
    for j, a in enumerate(order):
        if a.kind not in ("XL", "XS"):
            continue
        row, d = a.row, a.d_pos
        b = _gr.bar_at(mk, d)
        st = ctx.band(d, P["Lookback"], P["NoiseMult"])
        if not (_mk.is_checkpoint(b.mod) and st.have_band):
            lines.append("row %d %s decided %s: not a checkpoint with a band ((iii) grades it); not graded"
                         % (row, a.trade.exit_name, _gr.pos_str(mk, d)))
            continue
        long_ = a.trade.side == "Long"
        lvl = st.lower if long_ else st.upper
        if is_tie(b.c, lvl):
            ties.append("(iv) row %d: decision %s close %r vs opposite band %r — tie, not graded"
                        % (row, _gr.pos_str(mk, d), b.c, lvl))
            continue
        opp = (b.c < lvl) if long_ else (b.c > lvl)              # .cs :308 / :306, strict
        have_atr = _atr.atr_at(mk, d[0])[0]                      # .cs :303 atrGateOpen (m > 0)
        nxt = order[j + 1] if j + 1 < len(order) else None
        graded.append(row)
        nd = "none" if nxt is None else "row %d %s fills %s" % (nxt.row, nxt.trade.side, _gr.pos_str(mk, nxt.entry_pos))
        if opp and have_atr:
            want = "Short" if long_ else "Long"
            ok = nxt is not None and nxt.trade.side == want and nxt.entry_pos == a.exit_pos
            txt = "row %d %s at %s close %r passes the opposite band %r: expect a %s entry filling %s; next: %s" % (
                row, a.trade.exit_name, _gr.pos_str(mk, d), b.c, lvl, want, _gr.pos_str(mk, a.exit_pos), nd)
        else:
            ok = nxt is None or nxt.entry_pos > a.exit_pos
            txt = "row %d %s at %s close %r does not pass the opposite band %r%s: expect the next entry after %s; next: %s" % (
                row, a.trade.exit_name, _gr.pos_str(mk, d), b.c, lvl, "" if have_atr else " (or no ATR)",
                _gr.pos_str(mk, a.exit_pos), nd)
        if ok:
            lines.append(txt)
        else:
            bad.append((row, "FAIL " + txt))
            bad_rows += [row] + ([nxt.row] if nxt is not None else [])
    return _verdict("T12(iv)", r.label, bad, graded, lines, "every graded XL/XS reverses exactly when its close "
                    "passes the opposite band (%d exits)", "no XL/XS exit graded", bad_rows)


def grade_v(ctx, r, ties):
    mk, P = ctx.market, r.params
    xstop_d = {}
    for a in r.anns:
        if a.kind == "XStop" and a.d_pos is not None:
            xstop_d.setdefault(a.d_pos, []).append(a.row)
    bad, lines, graded = [], [], []
    for a in r.anns:
        row, dec, side = a.row, a.entry_dec_pos, a.trade.side
        b = _gr.bar_at(mk, dec)
        probs, tie = [], None
        if not _mk.is_checkpoint(b.mod):                         # .cs :272
            probs.append("not a checkpoint (mod %d)" % b.mod)
        if dec[0] < FIRST_ENTRY_SESSION:                         # spec §4 warm-up, T11
            probs.append("session s%d < s%d" % (dec[0], FIRST_ENTRY_SESSION))
        st = ctx.band(dec, P["Lookback"], P["NoiseMult"])
        if not st.have_band:                                     # .cs :273
            probs.append("no band")
        else:
            lvl = st.upper if side == "Long" else st.lower
            if is_tie(b.c, lvl):
                tie = lvl
            elif not ((b.c > lvl) if side == "Long" else (b.c < lvl)):   # .cs :306 / :308, strict
                probs.append("close %r not %s %s %r" % (b.c, ">" if side == "Long" else "<",
                                                         "Upper" if side == "Long" else "Lower", lvl))
        if dec in xstop_d:                                       # .cs :258/:266 return; T10
            probs.append("is the XStop decision bar of row(s) %s" % xstop_d[dec])
        where = "row %d %s entry decided %s" % (row, side, _gr.pos_str(mk, dec))
        if probs:
            graded.append(row)
            bad.append((row, "%s: %s" % (where, "; ".join(probs))))
            continue
        if tie is not None:
            ties.append("(v) %s: close %r vs band %r — tie, not graded" % (where, b.c, tie))
            continue
        graded.append(row)
        extra = ""
        if _gr.is_flat_pos(mk, dec, P["ExitPolicy"]):
            # Early-close last bar that is a checkpoint: the checkpoint step still runs (.cs :241-244, no return;
            # §4 v2.1 correction :77). Not flagged; whether/where NT8 fills it is UNVERIFIED (T9 note :197).
            extra = " (early-close last bar: checkpoint step runs, §4 v2.1; fill session UNVERIFIED)"
        lines.append("%s: sound%s" % (where, extra))
    return _verdict("T12(v)", r.label, bad, graded, lines, "every graded entry is sound (%d entries)", "no trades")


def grade_vi(r, ties):
    lines = ties or ["none"]
    return _gr.Verdict("T12(vi)", "PASS", "ties within 1e-9 relative listed and NOT graded: count %d" % len(ties),
                       [], _cap(lines), r.label)


# ---------------------------------------------------------------------------------------------------
# (vii) power
# ---------------------------------------------------------------------------------------------------

def _cross(ctx, r, other_rule):
    own = rule_of(r.params["ExitPolicy"])
    diffs, skipped = [], 0
    for a in r.anns:
        w0 = walk_cstar(ctx, r.params, a, own)
        w1 = walk_cstar(ctx, r.params, a, other_rule)
        if w0.tie is not None or w1.tie is not None:
            skipped += 1
            continue
        if w0.c != w1.c:
            diffs.append((a.row, w0.c, w1.c))
    return diffs, skipped


def grade_vii(ctx, trio):
    mk, out = ctx.market, []
    A, B = trio["T12a"], trio["T12b"]
    if A is None or B is None:
        out.append(_gr.Verdict("T12(vii) power", "UNTESTED", "cross-apply needs T12a and T12b; missing: %s"
                               % ", ".join(t for t, x in (("T12a", A), ("T12b", B)) if x is None), [], [], "all"))
    else:
        lines, rows, short = [], [], []
        for tag, r, other in (("T12a", A, "OppBand"), ("T12b", B, "BandOrVWAP")):
            diffs, skipped = _cross(ctx, r, other)
            lines.append("%s (%s): %s rule applied to %d trades: %d differ, %d tie-skipped"
                         % (tag, r.label, other, len(r.anns), len(diffs), skipped))
            for row, c0, c1 in diffs[:10]:
                lines.append("  %s#%d: own c* = %s, %s c* = %s" % (r.label, row, _gr.pos_str(mk, c0), other,
                                                                  _gr.pos_str(mk, c1)))
                rows.append("%s#%d" % (r.label, row))
            if not diffs:
                short.append("%s under the %s rule" % (tag, other))
        if short:
            out.append(_gr.Verdict("T12(vii) power", "UNTESTED", "T12 not passed: no trade whose c* differs from "
                                   "the run's own rule for %s" % "; ".join(short), rows, lines, "all"))
        else:
            out.append(_gr.Verdict("T12(vii) power", "PASS", "both cross-applications move >= 1 c*", rows, lines, "all"))
    for tag, pol in TRIO:
        r = trio[tag]
        if r is None:
            out.append(_gr.Verdict("T12(vii) stop", "UNTESTED", "the stop runs with %s: no run at (14, 1.0, 1.5, %s)"
                                   % (pol, pol), [], [], tag))
            continue
        xs = [a.row for a in r.anns if a.kind == "XStop"]
        if xs:
            out.append(_gr.Verdict("T12(vii) stop", "PASS", "%s (%s) holds %d XStop exit(s)" % (tag, pol, len(xs)),
                                   xs, [], r.label))
        else:
            out.append(_gr.Verdict("T12(vii) stop", "UNTESTED", "the stop runs with this policy (%s): no XStop in %s"
                                   % (pol, tag), [], [], r.label))
    return out


# ---------------------------------------------------------------------------------------------------
# entry point
# ---------------------------------------------------------------------------------------------------

def grade_t12(ctx):
    trio, notes = find_trio(ctx)
    members = {id(r): tag for tag, r in trio.items() if r is not None}
    required, optional = [], []
    head = ["%s = %s" % (tag, trio[tag].label if trio[tag] else "MISSING (no run at (14, 1.0, 1.5, %s))" % pol)
            for tag, pol in TRIO] + notes
    required.append(grade_i(ctx, trio))
    for tag, pol in TRIO:
        if trio[tag] is None:
            required.append(_gr.Verdict("T12(ii)", "UNTESTED", "no run at (14, 1.0, 1.5, %s)" % pol, [], [], tag))
    per_run = []
    for r in ctx.runs:
        in_trio = id(r) in members
        ties = []
        vs = [grade_ii(ctx, r, in_trio), grade_iii(ctx, r, ties), grade_iv(ctx, r, ties), grade_v(ctx, r, ties)]
        (required if in_trio else optional).extend(vs)
        per_run.extend(vs)
        per_run.append(grade_vi(r, ties))
    vii = grade_vii(ctx, trio)
    required.extend(vii)
    allv = required + optional
    fails = [v for v in allv if v.verdict == "FAIL"]
    unt = [v for v in required if v.verdict == "UNTESTED"]
    tag = lambda v: "%s%s" % (v.test, "" if v.run in (None, "all") else " [%s]" % v.run)   # noqa: E731
    if fails:
        overall = _gr.Verdict("T12", "FAIL", "failing part(s): %s" % ", ".join(tag(v) for v in fails), [], head, "all")
    elif unt:
        overall = _gr.Verdict("T12", "UNTESTED", "required part(s) UNTESTED: %s" % ", ".join(tag(v) for v in unt),
                              [], head, "all")
    else:
        overall = _gr.Verdict("T12", "PASS", "every required part passes (trio (i), (ii)-(v) of T12a-c, (vii)); "
                              "no FAIL in any other run", [], head, "all")
    order = [overall, required[0]] + [v for v in required[1:] if v.test == "T12(ii)" and v.run in ("T12a", "T12b", "T12c")]
    return order + per_run + vii
