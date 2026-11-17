"""Quick measure, plain Python: NQ overnight high/low swept in the NY morning, then reclaimed -> fade.
Stamps are Eastern, bar END. Rules fixed before the run:
- Trading day = bars ending 18:01 prior evening .. 16:00. Overnight range = bars ending 18:01 .. 09:30.
- Window: bars ending 09:31 .. 11:00. Sweep: high >= ONH + 1 tick (or low <= ONL - 1 tick).
- Reclaim: that bar or a later window bar CLOSES back inside. Enter at next bar's open.
- Stop-market 1 tick beyond the extreme since the sweep. Target 2R. Exit at last bar <= 15:59 otherwise.
- First event per day. Stop and target in same minute -> stop. Gap through stop -> fill at the open.
- Costs: 2 ticks slippage per side + $0.62/side commission (MNQ $2/pt) = 1.62 pts round trip.
- FOLLOW = same moment and distance, opposite direction.
- 4H trend: last CLOSED 4-hour bar (Eastern clock buckets) close vs mean of last 50 closed 4H closes.
"""
import sys, math, datetime as dt
from collections import OrderedDict
TICK = 0.25
COST = 2*2*TICK + 2*0.62/2.0
days = OrderedDict()
h4_close = OrderedDict()   # bucket end datetime -> close
for line in open(sys.argv[1]):
    s, o, h, l, c, v = line.strip().split(";")
    t = dt.datetime.strptime(s, "%Y%m%d %H%M%S")
    if not (dt.datetime(2021,3,7,18) < t < dt.datetime(2026,7,18)): continue
    o, h, l, c = float(o), float(h), float(l), float(c)
    d = (t + dt.timedelta(hours=6)).date()
    hm = t.hour*100 + t.minute
    if 1600 < hm <= 1800: continue
    days.setdefault(d, []).append((t, hm, o, h, l, c))
    m = t - dt.timedelta(minutes=1)  # bar start
    b = m.replace(minute=0, second=0) - dt.timedelta(hours=m.hour % 4) + dt.timedelta(hours=4)
    h4_close[b] = c
h4k = list(h4_close.keys()); h4v = list(h4_close.values())
def trend_at(t):
    # last 4H bucket whose end <= t
    lo, hi = 0, len(h4k)
    while lo < hi:
        mid = (lo+hi)//2
        if h4k[mid] <= t: lo = mid+1
        else: hi = mid
    k = lo - 1
    if k < 49: return None
    w = h4v[k-49:k+1]
    return 1 if h4v[k] > sum(w)/50 else 0
rows = []
for d, bars in days.items():
    on = [b for b in bars if b[1] >= 1801 or b[1] <= 930]
    sess = [b for b in bars if 931 <= b[1] <= 1559]
    if len(on) < 300 or len(sess) < 300: continue
    onh = max(b[3] for b in on); onl = min(b[4] for b in on)
    side = ext = e = None
    for i, (t, hm, o, h, l, c) in enumerate(sess):
        if hm > 1100: break
        if side is None:
            if h >= onh + TICK: side, ext = "short", h
            elif l <= onl - TICK: side, ext = "long", l
        else:
            ext = max(ext, h) if side == "short" else min(ext, l)
        if side == "short" and c < onh: e = i+1; break
        if side == "long" and c > onl: e = i+1; break
    if e is None or e >= len(sess): continue
    entry = sess[e][2]
    stop = ext + TICK if side == "short" else ext - TICK
    risk = abs(entry - stop)
    if risk < 2*TICK: continue
    # entry must still be on the right side of the stop
    if (side == "short" and entry >= stop) or (side == "long" and entry <= stop): continue
    def sim(sgn, stop_px):
        tgt = entry + sgn*2*risk
        for (t, hm, o, h, l, c) in sess[e:]:
            if (l <= stop_px) if sgn == 1 else (h >= stop_px):
                px = min(stop_px, o) if sgn == 1 else max(stop_px, o)
                return (px - entry)*sgn
            if (h >= tgt) if sgn == 1 else (l <= tgt): return 2*risk
        return (sess[-1][5] - entry)*sgn
    sg = 1 if side == "long" else -1
    fade = sim(sg, stop)
    follow = sim(-sg, entry + sg*risk)
    tr = trend_at(sess[e-1][0])
    withtr = None if tr is None else ((side == "long" and tr == 1) or (side == "short" and tr == 0))
    rows.append(dict(day=d, year=d.year, side=side, risk=risk, withtr=withtr,
                     fade=(fade-COST)/risk, gross=fade/risk, follow=(follow-COST)/risk))
def summ(xs):
    n = len(xs)
    if n < 3: return f"n={n}"
    m = sum(xs)/n; sd = math.sqrt(sum((x-m)**2 for x in xs)/(n-1))
    gp = sum(x for x in xs if x > 0); gl = -sum(x for x in xs if x <= 0)
    wins = [x for x in xs if x > 0]
    # longest losing run
    run = best = 0
    for x in xs:
        run = run+1 if x <= 0 else 0; best = max(best, run)
    return (f"n={n:4d} win={len(wins)/n:5.1%} avgR={m:+.3f} PF={gp/gl:.2f} t={m/(sd/math.sqrt(n)):+.2f} "
            f"avgWinR={sum(wins)/len(wins):.2f} maxLossRun={best}")
risks = sorted(r["risk"] for r in rows)
print("events:", len(rows), "of", len(days), "days | median risk pts:", risks[len(risks)//2],
      "| longs:", sum(r["side"]=="long" for r in rows))
print("FADE net         ", summ([r["fade"] for r in rows]))
print("FADE gross       ", summ([r["gross"] for r in rows]))
print("FOLLOW net       ", summ([r["follow"] for r in rows]))
print("FADE with 4H     ", summ([r["fade"] for r in rows if r["withtr"] is True]))
print("FADE against 4H  ", summ([r["fade"] for r in rows if r["withtr"] is False]))
for y in sorted(set(r["year"] for r in rows)):
    print(" ", y, "fade", summ([r["fade"] for r in rows if r["year"] == y]),
          "| with4H", summ([r["fade"] for r in rows if r["year"] == y and r["withtr"] is True]))
