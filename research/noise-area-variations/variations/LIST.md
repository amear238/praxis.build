# The variation list, first list

Fixed by the lead from the measuring pass (`out/measure/tables.md` and `out/measure/READING.md`) before any backtest was run. Eight variations. Nothing in these files changes after this commit.

All eight use the original noise band built from the 9:30 AM open (14-day lookback, normal width), take buys and sells, may enter from 9:31 AM to 3:30 PM, and are flat by 4:00 PM. Every entry has a stop order resting from the moment it fills. The account is the $50,000 stand-in with the $2,000 trailing limit; a risk of 0.25% is $125 a trade at the start.

Why no evening or overnight variation: the measuring pass found the overnight hours flat or losing, and the evening a lottery (9 in 10 stopped out) that cannot keep to the seven-day rule on its own. They are left for a second list if this one fails.

**V1, the reference point.** The original rules with a real stop: breakouts checked on the half hour, exit when price comes back inside the band or through the day's average price, stop half a band-width away, 1% risk ($500), up to 10 trades a day, re-entry allowed straight away. It is here so the list has a known starting point. At $500 a trade the limit is four losers, so it is not expected to survive.

**V2, the strongest measured cell, traded the way it was measured.** Half-hour breakouts, stop half a band-width away, held to the close, at most 2 trades a day, and after an exit no new entry on that side until price has closed back inside the band. Risk 0.25% ($125), so the limit is about 16 losers. In the measuring pass these breakouts won 37% of the time with an average winner of 2.6 times the risk.

**V3, tighter stop and smaller risk, for survival.** As V2, but the stop is 0.35 of a band-width away and the risk is 0.15% ($75), so the limit is about 26 losers. The measuring pass showed results improving steadily as the stop got tighter. A tighter stop also costs fewer dollars a contract, so the small risk still fits most breakouts. This exact stop was not measured.

**V4, the tighter stop at V2's risk.** As V3 but at 0.25% ($125). It separates the effect of the stop from the effect of the risk.

**V5, one trade a day.** As V2, but only the first breakout of the day is taken. The first breakout is usually a morning one, which was the best part of the day, and one trade a day caps a bad day at one stop.

**V6, V2 with the original exit.** As V2, but it exits when price comes back inside the band or through the day's average price, as the original rules do. It shows whether the original exit can keep winners at twice the risk when the risk is small enough to survive.

**V7, V2 with a trailing stop.** As V2, but once in a trade the stop follows the best price at three times the risk. About 23% of these breakouts ran to three times the risk and 11% to five times; some gave it back before the close.

**V8, breakouts on any minute.** As V2, but a close outside the band on any minute counts, not only on the half hour. The longest stretch without a breakout was 6 trading days against 7 on the half hour, so it has more room on the frequency rule. Its measured edge was the weakest on this list.

A second list of at most eight is allowed once if none of these passes, using only the measuring pass and these variations' results on 2021 to 2023.
