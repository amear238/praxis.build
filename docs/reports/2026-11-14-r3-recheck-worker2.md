# 2026-11-14 R3 recheck — worker 2 of 2 (ADVERSARIAL)

## Task
Unit `2026-11-14-r3-recheck`, worker 2. Mode: ADVERSARIAL. Artifact under attack: `docs/reports/2026-11-14-r3-recheck-worker1.md` (its script output `/tmp/praxis-r3/w1_out.txt` is pasted inside it). Criteria: SPEC_RUBRIC S1, S2, S8, S13. HEAD `244cfc3`, branch main. Read-only on tracked files. Nothing staged, nothing committed. This report is left untracked.

## Method
1. I wrote `/tmp/praxis-r3/w2_adv.py` from scratch (stdlib only), ran it with `python3 -I`, and saved its output to `/tmp/praxis-r3/w2_out.txt`. I did this BEFORE I opened the artifact. I did not open `w1_r3.py`, `w1_shell.txt`, `w1_out.txt`, `mgr_spot.py` or `mgr_rerun_w1.txt`. The artifact pastes `w1_shell.txt` and `w1_out.txt` in full, so I read that text as part of the artifact, after my run.
2. MNQ net = (Profit + Commission)/10 − 1.90 for NT8 rows, and points×2 − 1.90 for the gap fade, both in Decimal. Session date = entry date (exit date tested as an alternative). The calendar N comes from `scripts/wf/sessions.py` `build_calendar` on the bar file, loaded by path.
3. Fill test: I checked every NT8 entry and exit fill against the bar with the same timestamp in `/Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt` (read-only). Two models were tried: clamp(open ± 0.50 adverse, L, H) and clamp(close ± 0.50 adverse, L, H). Follow-up checks are in `/tmp/praxis-r3/w2_extra.py` → `w2_extra_out.txt` and `w2_slip_worst.py` → `w2_slip_worst_out.txt`.
4. Process log, including two mistakes of mine:
   - My first run loaded `sessions.py` through `importlib` without `sys.dont_write_bytecode`. That wrote `scripts/wf/__pycache__/sessions.cpython-314.pyc` into the repo. The file is gitignored (`.gitignore:4:__pycache__/`) and untracked. The directory's mtime was 10:21, my run time, and worker 1 had pasted that the directory did not exist. So I deleted the `.pyc` file and the directory, added `sys.dont_write_bytecode = True`, and reran. After the rerun, `ls scripts/wf/__pycache__` gives "No such file or directory" (pasted under X-runs below).
   - My first gap-fade entry-fill check had the sign inverted for shorts, and it printed 0/648. I fixed it to O − 0.5 for a short sell and O + 0.5 for a long buy, and it now prints 648/648. The w2_out.txt pasted below is from the final script.

```
$ shasum -a 256 /tmp/praxis-r3/w2_adv.py
cc29f8e6b186c5afb65eb34c3197b05d34099fe31eed019e112548c6b110ffb8  /tmp/praxis-r3/w2_adv.py
$ shasum -a 256 /tmp/praxis-r3/w2_*
cc29f8e6b186c5afb65eb34c3197b05d34099fe31eed019e112548c6b110ffb8  /tmp/praxis-r3/w2_adv.py
7b862534588d80960a8b953aa5c5e07fc00ead4f8d80b7e7ee49c5ee17f5394c  /tmp/praxis-r3/w2_extra_out.txt
62d3d5ac20c91264d2bae24da5ac5bd5ff2b897fb13349300a71e090390302a6  /tmp/praxis-r3/w2_extra.py
94972b873daf636c12ac8a6f38ccf558eaf682d96676b49b1626640e512d66c4  /tmp/praxis-r3/w2_mutant_out.txt
f1c9980e9a8c4d477de23554d14b24b5900ccc02a4f62309bb49e8680c456617  /tmp/praxis-r3/w2_mutant.csv
567b005f2dab6217d4b91f82a404b0731e241b172e09a4e3a5ddea54b5262357  /tmp/praxis-r3/w2_out.txt
bfd49f07fa5ca6e7e3728cb1924065e5465774ce3c01e09526b7b265fa45a34d  /tmp/praxis-r3/w2_s13.txt
98a6949884308a7bc97570daceaa6edbf8718f1d2866f42c6d3762761a8acc50  /tmp/praxis-r3/w2_slip_worst_out.txt
1615cffdbffee76cbb32b72209fa2ddd508b90759ca6f98b7aa1301ead2cb557  /tmp/praxis-r3/w2_slip_worst.py
```

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## Independent figures — /tmp/praxis-r3/w2_out.txt (in full)
```
sha256 307c5e8af1da42b7606d666f14e4f34228feec50d19dd52d25396aae1b16e454  /Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt
sha256 6d07b2454eba2bfcdfc059dcf75737256d50cbcbfd76d933e80a2c4d69352045  /Volumes/Sensidine/Praxis.build/research/search-loop/c1-gap-fade/out/trades_V2_full.csv
sha256 71cd073391018c4a27b783547a8df4143f9948eea77ceb064d57bf2619c9a9a8  /Volumes/Sensidine/Praxis.build/research/search-loop/c1-gap-fade/out/summary.json
sha256 421c44e6cd9d417b432be1a5b440b0861782a3bba7e1961beba5b5421e0534bd  /Volumes/Sensidine/Praxis.build/docs/reports/evidence/2026-11-01-ninjatrader-grid-0710am.csv
sha256 4207ea99e7f1187b54ebe45c97822409629192ed12e7ee0dbaacb241c152b6e8  /Volumes/Sensidine/Praxis.build/docs/reports/evidence/2026-11-01-ninjatrader-grid-0757am.csv
sha256 5a3c4d783a44b33a18c4eb77f50444af1d4cf65ed4190038becc4c2007c868e0  /Volumes/Sensidine/Praxis.build/docs/reports/evidence/2026-11-01-ninjatrader-grid-0759am.csv
sha256 4efd8ce8e95cc408f82d494fcf55238c25b9980b030a39eb25f4eaa5fbd180d9  /Volumes/Sensidine/Praxis.build/docs/reports/evidence/2026-11-01-ninjatrader-grid-0800am.csv
build_calendar(/Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt): N=1352  first 2021-03-08 last 2026-07-17  source sha256 307c5e8af1da42b7606d666f14e4f34228feec50d19dd52d25396aae1b16e454
summary.json trading_days=1354  d6.calendar_N=1352  skipped_days=3  weekend_trading_days=['2021-03-28', '2025-03-16']
====================================================================================================
STRATEGY: Baseline (NoiseArea BandOrVWAP)
trades: 1190
losers (MNQ net < 0): 712
ALT losers (NQ Profit < 0): 706 | MNQ<0 but NQ>=0: 6 | MNQ net == 0: 0
largest single loss MNQ: -542.40  at trade(s) [1182]  entry date(s) ['2026-06-25']  exit name(s) ['XS']
average loss MNQ (mean over MNQ losers): -97.26  (sum -69249.80 / 712)
largest loss as % of $50,000: 1.0848%   of $150,000: 0.3616%
longest losing run by trade number: length 10, 2 run(s) of that length:
    trades 319..328  entry dates 2022-09-15 .. 2022-09-26  summed MNQ -802.00
    trades 1150..1159  entry dates 2026-05-11 .. 2026-05-20  summed MNQ -1070.50
    (worst-summed run by trade number: length 8 trades 1027..1034 2025-10-13..2025-10-17 sum -1364.70)
longest losing run by exit time (stable on trade number): length 10, 2 run(s) of that length:
    trades 319..328  entry dates 2022-09-15 .. 2022-09-26  summed MNQ -802.00
    trades 1150..1159  entry dates 2026-05-11 .. 2026-05-20  summed MNQ -1070.50
    (worst-summed run by exit time (stable on trade number): length 8 trades 1027..1034 2025-10-13..2025-10-17 sum -1364.70)
longest losing run by entry time (stable on trade number): length 10, 2 run(s) of that length:
    trades 319..328  entry dates 2022-09-15 .. 2022-09-26  summed MNQ -802.00
    trades 1150..1159  entry dates 2026-05-11 .. 2026-05-20  summed MNQ -1070.50
    (worst-summed run by entry time (stable on trade number): length 8 trades 1027..1034 2025-10-13..2025-10-17 sum -1364.70)
ALT longest losing run on NQ<0 by trade number: length 10
by entry date: worst single-day MNQ -705.10 on ['2022-10-13'] (trades that day: [4]) | sessions with a trade 792 | most trades in one session 5 on 3 date(s) first 2023-12-04 | avg trades/session-with-trade 1.5025 | avg trades/calendar session (N=1352) 0.8802
by exit date: worst single-day MNQ -705.10 on ['2022-10-13'] (trades that day: [4]) | sessions with a trade 792 | most trades in one session 5 on 3 date(s) first 2023-12-04 | avg trades/session-with-trade 1.5025 | avg trades/calendar session (N=1352) 0.8802
trades whose exit date != entry date: 0 []
same-timestamp handoffs (exit of trade i == entry of trade i+1): 1
largest MAE at 1 MNQ (NQ MAE/10): 747.50  trade 1182  date 2026-06-25  (NQ MAE 7475.00; that trade MNQ net -542.40)
  commission values: Counter({'2.96': 1190})  qty values: Counter({1: 1190})
  exit names: Counter({'XS': 429, 'Exit on session close': 429, 'XL': 332})
  trades with -NQgross > MAE (loss beyond MAE): 0
  losers by exit type (count, worst MNQ): {'XS': (363, '-542.40'), 'XL': (284, '-447.40'), 'Exit on session close': (65, '-359.90')}
====================================================================================================
STRATEGY: OppBand
trades: 810
losers (MNQ net < 0): 346
ALT losers (NQ Profit < 0): 340 | MNQ<0 but NQ>=0: 6 | MNQ net == 0: 0
largest single loss MNQ: -1960.90  at trade(s) [627]  entry date(s) ['2025-04-08']  exit name(s) ['XL']
average loss MNQ (mean over MNQ losers): -232.61  (sum -80481.40 / 346)
largest loss as % of $50,000: 3.9218%   of $150,000: 1.3073%
longest losing run by trade number: length 6, 2 run(s) of that length:
    trades 84..89  entry dates 2021-11-17 .. 2021-11-24  summed MNQ -1429.40
    trades 472..477  entry dates 2024-03-18 .. 2024-04-04  summed MNQ -1302.90
    (worst-summed run by trade number: length 2 trades 626..627 2025-04-07..2025-04-08 sum -2415.80)
longest losing run by exit time (stable on trade number): length 6, 2 run(s) of that length:
    trades 84..89  entry dates 2021-11-17 .. 2021-11-24  summed MNQ -1429.40
    trades 472..477  entry dates 2024-03-18 .. 2024-04-04  summed MNQ -1302.90
    (worst-summed run by exit time (stable on trade number): length 2 trades 626..627 2025-04-07..2025-04-08 sum -2415.80)
longest losing run by entry time (stable on trade number): length 6, 2 run(s) of that length:
    trades 84..89  entry dates 2021-11-17 .. 2021-11-24  summed MNQ -1429.40
    trades 472..477  entry dates 2024-03-18 .. 2024-04-04  summed MNQ -1302.90
    (worst-summed run by entry time (stable on trade number): length 2 trades 626..627 2025-04-07..2025-04-08 sum -2415.80)
ALT longest losing run on NQ<0 by trade number: length 6
by entry date: worst single-day MNQ -1894.80 on ['2025-04-08'] (trades that day: [2]) | sessions with a trade 792 | most trades in one session 2 on 18 date(s) first 2021-05-06 | avg trades/session-with-trade 1.0227 | avg trades/calendar session (N=1352) 0.5991
by exit date: worst single-day MNQ -1894.80 on ['2025-04-08'] (trades that day: [2]) | sessions with a trade 792 | most trades in one session 2 on 18 date(s) first 2021-05-06 | avg trades/session-with-trade 1.0227 | avg trades/calendar session (N=1352) 0.5991
trades whose exit date != entry date: 0 []
same-timestamp handoffs (exit of trade i == entry of trade i+1): 18
largest MAE at 1 MNQ (NQ MAE/10): 2223.00  trade 627  date 2025-04-08  (NQ MAE 22230.00; that trade MNQ net -1960.90)
  commission values: Counter({'2.96': 810})  qty values: Counter({1: 810})
  exit names: Counter({'Exit on session close': 792, 'XL': 10, 'XS': 8})
  trades with -NQgross > MAE (loss beyond MAE): 0
  losers by exit type (count, worst MNQ): {'Exit on session close': (328, '-1099.90'), 'XS': (8, '-907.90'), 'XL': (10, '-1960.90')}
====================================================================================================
STRATEGY: Flat1559
trades: 1190
losers (MNQ net < 0): 715
ALT losers (NQ Profit < 0): 708 | MNQ<0 but NQ>=0: 7 | MNQ net == 0: 0
largest single loss MNQ: -542.40  at trade(s) [1182]  entry date(s) ['2026-06-25']  exit name(s) ['XS']
average loss MNQ (mean over MNQ losers): -96.45  (sum -68965.00 / 715)
largest loss as % of $50,000: 1.0848%   of $150,000: 0.3616%
longest losing run by trade number: length 10, 2 run(s) of that length:
    trades 319..328  entry dates 2022-09-15 .. 2022-09-26  summed MNQ -815.50
    trades 1150..1159  entry dates 2026-05-11 .. 2026-05-20  summed MNQ -1046.00
    (worst-summed run by trade number: length 8 trades 1027..1034 2025-10-13..2025-10-17 sum -1301.70)
longest losing run by exit time (stable on trade number): length 10, 2 run(s) of that length:
    trades 319..328  entry dates 2022-09-15 .. 2022-09-26  summed MNQ -815.50
    trades 1150..1159  entry dates 2026-05-11 .. 2026-05-20  summed MNQ -1046.00
    (worst-summed run by exit time (stable on trade number): length 8 trades 1027..1034 2025-10-13..2025-10-17 sum -1301.70)
longest losing run by entry time (stable on trade number): length 10, 2 run(s) of that length:
    trades 319..328  entry dates 2022-09-15 .. 2022-09-26  summed MNQ -815.50
    trades 1150..1159  entry dates 2026-05-11 .. 2026-05-20  summed MNQ -1046.00
    (worst-summed run by entry time (stable on trade number): length 8 trades 1027..1034 2025-10-13..2025-10-17 sum -1301.70)
ALT longest losing run on NQ<0 by trade number: length 10
by entry date: worst single-day MNQ -683.70 on ['2025-04-16'] (trades that day: [3]) | sessions with a trade 792 | most trades in one session 5 on 3 date(s) first 2023-12-04 | avg trades/session-with-trade 1.5025 | avg trades/calendar session (N=1352) 0.8802
by exit date: worst single-day MNQ -683.70 on ['2025-04-16'] (trades that day: [3]) | sessions with a trade 792 | most trades in one session 5 on 3 date(s) first 2023-12-04 | avg trades/session-with-trade 1.5025 | avg trades/calendar session (N=1352) 0.8802
trades whose exit date != entry date: 0 []
same-timestamp handoffs (exit of trade i == entry of trade i+1): 1
largest MAE at 1 MNQ (NQ MAE/10): 747.50  trade 1182  date 2026-06-25  (NQ MAE 7475.00; that trade MNQ net -542.40)
  commission values: Counter({'2.96': 1190})  qty values: Counter({1: 1190})
  exit names: Counter({'XS': 429, 'FlatEOD': 423, 'XL': 332, 'Exit on session close': 6})
  trades with -NQgross > MAE (loss beyond MAE): 0
  losers by exit type (count, worst MNQ): {'XS': (363, '-542.40'), 'XL': (284, '-447.40'), 'FlatEOD': (68, '-371.90')}
====================================================================================================
STRATEGY: LastHalfHourMomentum
trades: 1304
losers (MNQ net < 0): 694
ALT losers (NQ Profit < 0): 683 | MNQ<0 but NQ>=0: 11 | MNQ net == 0: 0
largest single loss MNQ: -555.40  at trade(s) [977]  entry date(s) ['2025-03-04']  exit name(s) ['LHFlat1559']
average loss MNQ (mean over MNQ losers): -71.82  (sum -49841.10 / 694)
largest loss as % of $50,000: 1.1108%   of $150,000: 0.3703%
longest losing run by trade number: length 10, 3 run(s) of that length:
    trades 604..613  entry dates 2023-08-29 .. 2023-09-12  summed MNQ -339.50
    trades 947..956  entry dates 2025-01-17 .. 2025-01-31  summed MNQ -895.00
    trades 1160..1169  entry dates 2025-11-26 .. 2025-12-11  summed MNQ -509.00
    (worst-summed run by trade number: length 10 trades 947..956 2025-01-17..2025-01-31 sum -895.00)
longest losing run by exit time (stable on trade number): length 10, 3 run(s) of that length:
    trades 604..613  entry dates 2023-08-29 .. 2023-09-12  summed MNQ -339.50
    trades 947..956  entry dates 2025-01-17 .. 2025-01-31  summed MNQ -895.00
    trades 1160..1169  entry dates 2025-11-26 .. 2025-12-11  summed MNQ -509.00
    (worst-summed run by exit time (stable on trade number): length 10 trades 947..956 2025-01-17..2025-01-31 sum -895.00)
longest losing run by entry time (stable on trade number): length 10, 3 run(s) of that length:
    trades 604..613  entry dates 2023-08-29 .. 2023-09-12  summed MNQ -339.50
    trades 947..956  entry dates 2025-01-17 .. 2025-01-31  summed MNQ -895.00
    trades 1160..1169  entry dates 2025-11-26 .. 2025-12-11  summed MNQ -509.00
    (worst-summed run by entry time (stable on trade number): length 10 trades 947..956 2025-01-17..2025-01-31 sum -895.00)
ALT longest losing run on NQ<0 by trade number: length 10
by entry date: worst single-day MNQ -555.40 on ['2025-03-04'] (trades that day: [1]) | sessions with a trade 1304 | most trades in one session 1 on 1304 date(s) first 2021-03-09 | avg trades/session-with-trade 1.0000 | avg trades/calendar session (N=1352) 0.9645
by exit date: worst single-day MNQ -555.40 on ['2025-03-04'] (trades that day: [1]) | sessions with a trade 1304 | most trades in one session 1 on 1304 date(s) first 2021-03-09 | avg trades/session-with-trade 1.0000 | avg trades/calendar session (N=1352) 0.9645
trades whose exit date != entry date: 0 []
same-timestamp handoffs (exit of trade i == entry of trade i+1): 0
largest MAE at 1 MNQ (NQ MAE/10): 694.00  trade 977  date 2025-03-04  (NQ MAE 6940.00; that trade MNQ net -555.40)
  commission values: Counter({'2.96': 1304})  qty values: Counter({1: 1304})
  exit names: Counter({'LHFlat1559': 1304})
  trades with -NQgross > MAE (loss beyond MAE): 0
  losers by exit type (count, worst MNQ): {'LHFlat1559': (694, '-555.40')}
====================================================================================================
STRATEGY: Gap fade V2 full (Python pre-screen)
trades: 648
losers (MNQ net < 0): 324
ALT losers (NQ net@2.96 < 0): 324 | MNQ<0 but NQ296>=0: 0 | MNQ net == 0: 0
largest single loss MNQ: -472.90  at trade(s) [648]  entry date(s) ['2026-07-16']  exit name(s) ['stop']
average loss MNQ (mean over MNQ losers): -161.64  (sum -52372.10 / 324)
largest loss as % of $50,000: 0.9458%   of $150,000: 0.3153%
longest losing run by trade number: length 10, 1 run(s) of that length:
    trades 612..621  entry dates 2026-03-11 .. 2026-04-10  summed MNQ -1951.50
    (worst-summed run by trade number: length 10 trades 612..621 2026-03-11..2026-04-10 sum -1951.50)
longest losing run by exit time (stable on trade number): length 10, 1 run(s) of that length:
    trades 612..621  entry dates 2026-03-11 .. 2026-04-10  summed MNQ -1951.50
    (worst-summed run by exit time (stable on trade number): length 10 trades 612..621 2026-03-11..2026-04-10 sum -1951.50)
longest losing run by entry time (stable on trade number): length 10, 1 run(s) of that length:
    trades 612..621  entry dates 2026-03-11 .. 2026-04-10  summed MNQ -1951.50
    (worst-summed run by entry time (stable on trade number): length 10 trades 612..621 2026-03-11..2026-04-10 sum -1951.50)
ALT longest losing run on NQ<0 by trade number: length 10
by entry date: worst single-day MNQ -472.90 on ['2026-07-16'] (trades that day: [1]) | sessions with a trade 648 | most trades in one session 1 on 648 date(s) first 2021-03-16 | avg trades/session-with-trade 1.0000 | avg trades/calendar session (N=1354) 0.4786
by exit date: worst single-day MNQ -472.90 on ['2026-07-16'] (trades that day: [1]) | sessions with a trade 648 | most trades in one session 1 on 648 date(s) first 2021-03-16 | avg trades/session-with-trade 1.0000 | avg trades/calendar session (N=1354) 0.4786
trades whose exit date != entry date: 0 []
same-timestamp handoffs (exit of trade i == entry of trade i+1): 0
largest MAE at 1 MNQ (mae_points*2): 471.0  trade 648  date 2026-07-16  (mae_points 235.5; that trade MNQ net -472.90)
  file mnq_net == points*2-1.90 on all rows: True
  exit kinds: Counter({'target': 301, 'stop': 286, 'time': 61})
  losers by exit type (count, worst MNQ): {'stop': (286, '-472.90'), 'time': (38, '-298.90')}
  ALT gap-fade avg trades/calendar session with N=1352 (d6 calendar_N): 0.4793 ; with 1354-3 skipped=1351: 0.4796
  summary selected_full trades=648 net_mnq=-254.20 ; recomputed sum mnq=-254.20
DECISIONS.md :1063 contains 'MNQ $1.90': True
DECISIONS.md lines containing 'MNQ $1.90': [970, 1063, 1075, 1118, 1124, 1125, 2314, 2605]
stop/limit-order API hits in ninjascript/PraxisNoiseAreaBreakout.cs: 0 []
stop/limit-order API hits in ninjascript/PraxisNoiseAreaBreakout_OppBand.cs: 0 []
stop/limit-order API hits in ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs: 0 []
stop/limit-order API hits in ninjascript/PraxisLastHalfHourMomentum.cs: 0 []
bar stamps needed 5679, found 5679, duplicate stamps 0
----------------------------------------------------------------------------------------------------
FILL TEST: Baseline (NoiseArea BandOrVWAP)
  entry  L                        {'open+-2tick clamp': 556, '(also) == close exactly': 5, '(of open-clamp) clipped to bar extreme, slip<2t': 13, '(also) == open exactly': 7}
  entry  S                        {'open+-2tick clamp': 634, '(of open-clamp) clipped to bar extreme, slip<2t': 8, '(also) == open exactly': 5, '(also) == close exactly': 8}
  exit   Exit on session close    {'close+-2tick clamp': 424, '(also) == open exactly': 4, 'open+-2tick clamp': 5, '(also) == close exactly': 2}
  exit   XL                       {'open+-2tick clamp': 332, '(also) == open exactly': 9, '(of open-clamp) clipped to bar extreme, slip<2t': 18, '(also) == close exactly': 3}
  exit   XS                       {'open+-2tick clamp': 429, '(also) == open exactly': 15, '(of open-clamp) clipped to bar extreme, slip<2t': 21, '(also) == close exactly': 7}
----------------------------------------------------------------------------------------------------
FILL TEST: OppBand
  entry  L                        {'open+-2tick clamp': 404, '(also) == close exactly': 4, '(of open-clamp) clipped to bar extreme, slip<2t': 6, '(also) == open exactly': 3}
  entry  S                        {'open+-2tick clamp': 406, '(of open-clamp) clipped to bar extreme, slip<2t': 2, '(also) == close exactly': 5, '(also) == open exactly': 1}
  exit   Exit on session close    {'close+-2tick clamp': 786, '(also) == close exactly': 3, '(also) == open exactly': 8, 'open+-2tick clamp': 6}
  exit   XL                       {'open+-2tick clamp': 10}
  exit   XS                       {'open+-2tick clamp': 8}
----------------------------------------------------------------------------------------------------
FILL TEST: Flat1559
  entry  L                        {'open+-2tick clamp': 556, '(also) == close exactly': 5, '(of open-clamp) clipped to bar extreme, slip<2t': 13, '(also) == open exactly': 7}
  entry  S                        {'open+-2tick clamp': 634, '(of open-clamp) clipped to bar extreme, slip<2t': 8, '(also) == open exactly': 5, '(also) == close exactly': 8}
  exit   Exit on session close    {'close+-2tick clamp': 6, '(also) == open exactly': 1}
  exit   FlatEOD                  {'open+-2tick clamp': 423, '(also) == close exactly': 4, '(of open-clamp) clipped to bar extreme, slip<2t': 21, '(also) == open exactly': 10}
  exit   XL                       {'open+-2tick clamp': 332, '(also) == open exactly': 9, '(of open-clamp) clipped to bar extreme, slip<2t': 18, '(also) == close exactly': 3}
  exit   XS                       {'open+-2tick clamp': 429, '(also) == open exactly': 15, '(of open-clamp) clipped to bar extreme, slip<2t': 21, '(also) == close exactly': 7}
----------------------------------------------------------------------------------------------------
FILL TEST: LastHalfHourMomentum
  entry  LHMomLong                {'open+-2tick clamp': 698, '(of open-clamp) clipped to bar extreme, slip<2t': 87, '(also) == open exactly': 55, '(also) == close exactly': 13}
  entry  LHMomShort               {'open+-2tick clamp': 606, '(also) == open exactly': 29, '(of open-clamp) clipped to bar extreme, slip<2t': 53, '(also) == close exactly': 11}
  exit   LHFlat1559               {'open+-2tick clamp': 1304, '(also) == open exactly': 36, '(of open-clamp) clipped to bar extreme, slip<2t': 78, '(also) == close exactly': 15}
----------------------------------------------------------------------------------------------------
GAP FADE stop-exit gap-through test (exit-stamped bar open already beyond the stop):
   {'stop exits': 286, 'stop exit == bound exactly': 286, 'entry O == 09:31 open': 648, 'entry fill == O +-0.5 adverse': 648}
   stop exits whose exit-bar OPEN is already beyond the stop: 0; summed extra points if filled at open+-0.5: 0; worst None
   largest predefined bound at 1 MNQ: -472.90 on 2026-07-16 (gap 234.5 pts)
```

## Mismatch table
I compared every (b) and (e) figure the artifact prints (its per-strategy blocks at :139-:151, :178-:190, :204-:216, :243-:254, :283-:295 and its `[3]`/`[4]`/`[5]` output) with w2_out.txt above.

| strategy | trades | losers | largest loss (date) | avg loss | longest run (ties, sums) | worst day (date, n) | % 50k / 150k | max MAE 1 MNQ | max trades/session | avg/session-with-trade | avg/calendar |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Baseline | 1190 = | 712 = | −542.40 2026-06-25 = | −97.26 = | 10 ×2, −802.00 / −1070.50 = | −705.10 2022-10-13, 4 = | 1.085 / 0.362 = | 747.50 = | 5 (3 dates) = | 1.5025 = | 0.8802 (N 1352) = |
| OppBand | 810 = | 346 = | −1960.90 2025-04-08 = | −232.61 = | 6 ×2, −1429.40 / −1302.90 = | −1894.80 2025-04-08, 2 = | 3.922 / 1.307 = | 2223.00 = | 2 (18 dates) = | 1.0227 = | 0.5991 = |
| Flat1559 | 1190 = | 715 = | −542.40 2026-06-25 = | −96.45 = | 10 ×2, −815.50 / −1046.00 = | −683.70 2025-04-16, 3 = | 1.085 / 0.362 = | 747.50 = | 5 (3 dates) = | 1.5025 = | 0.8802 = |
| LastHalfHour | 1304 = | 694 = | −555.40 2025-03-04 = | −71.82 = | 10 ×3, −339.50 / −895.00 / −509.00 = | −555.40 2025-03-04, 1 = | 1.111 / 0.370 = | 694.00 = | 1 = | 1.0000 = | 0.9645 = |
| Gap fade V2 | 648 = | 324 = | −472.90 2026-07-16 = | −161.64 = | 10 ×1, −1951.50 = | −472.90 2026-07-16, 1 = | 0.946 / 0.315 = | 471.00 = | 1 = | 1.0000 = | 0.4786 (1354) = |

`=` means the artifact's value equals mine. **Figure mismatches: 0.** The calendar N is 1352 in both. The gap-fade stop-distance maximum is 234.5 pt and the realized bound is −472.90 in both.

Alternative definitions (from w2_out.txt and X4 below):
- Losers on NQ Profit < 0 instead of MNQ net < 0: 706 / 340 / 708 / 683 / 324 (gap fade on NQ@2.96), against 712 / 346 / 715 / 694 / 324. The longest-run lengths are unchanged on NQ < 0 (10 / 6 / 10 / 10 / 10).
- Streak order by exit time or by entry time instead of trade number: the same runs and sums in all five.
- Session date by exit date instead of entry date: the same worst day and the same counts in all five. Exit date ≠ entry date on 0 trades in all five.
- Same-timestamp reversals: this definition DOES change one answer. In OppBand, all 18 two-trade sessions are a reversal at one timestamp (XL→S or XS→L). With reversal legs merged into one exposure, OppBand's "most trades in one session" goes from 2 to 1. Baseline and Flat1559 have 1 such handoff, and their maximum stays at 5.
- Gap-fade calendar denominator: 1354 gives 0.4786, 1352 (summary `d6.calendar_N`) gives 0.4793, and 1351 (1354 − 3 skipped) gives 0.4796.

## Findings by attack item

### 1. Recompute — 0 mismatches (above). Two related findings:
- **F8 (LOW).** The headline "longest losing streak" is the longest run, not the costliest one. The worst-summed consecutive-loser runs are larger: OppBand trades 626..627 (2025-04-07..04-08) sum **−$2,415.80**, against −$1,429.40 for the 6-trade run. Baseline trades 1027..1034 sum −$1,364.70 (against −$1,070.50). Flat1559 trades 1027..1034 sum −$1,301.70 (against −$1,046.00). This is not an error under the brief's definition, but the artifact does not show the figure that matters most for R3.
- **F7 (LOW).** The OppBand max trades/session of 2 depends on counting a same-timestamp reversal as two trades (X4).

### 2. Slippage claim — F1 (MED, S1/S2)
The artifact (:73) says "The fills therefore already include 2 ticks per side." It rests that on results-report lines :51, :77 and :253. What those lines OBSERVE:
- :51 covers ENTRIES in all four CSVs, plus (via the K15 sentence) the LastHalfHour fills that are not open ± 2 ticks.
- :77 and :253 cover the baseline's **423** 16:00-stamped "Exit on session close" fills only. The baseline has 429 such exits, so the 6 early-close exits are not covered.
- Nothing in the cited lines covers XL or XS (in any of the three Noise-Area arms), FlatEOD (Flat1559), OppBand's 792 session-close exits, or Flat1559's 6 session-close exits. For those exit types the artifact's claim is **INFERRED**.

My bar-file test now OBSERVES the clamp model on every exit type, with 0 NO MATCH (w2_out.txt, FILL TEST blocks). Per-type tick residuals from w2_extra_out.txt [X1]:
```
[X1] adverse slippage residual per fill, ticks (residual vs bar OPEN for all fills; vs bar CLOSE for session-close exits)
  -- Baseline (NoiseArea BandOrVWAP)
    entry  L                      n=556   {'0t': 7, '1t': 6, '2t': 543}  | full 2-tick: 543, less than 2 ticks: 13
    entry  S                      n=634   {'0t': 5, '1t': 3, '2t': 626}  | full 2-tick: 626, less than 2 ticks: 8
    exit   Exit on session close  n=429   {'0t': 2, '1t': 4, '2t': 423}  | full 2-tick: 423, less than 2 ticks: 6
    exit   XL                     n=332   {'0t': 9, '1t': 9, '2t': 314}  | full 2-tick: 314, less than 2 ticks: 18
    exit   XS                     n=429   {'0t': 15, '1t': 6, '2t': 408}  | full 2-tick: 408, less than 2 ticks: 21
  -- OppBand
    entry  L                      n=404   {'0t': 3, '1t': 3, '2t': 398}  | full 2-tick: 398, less than 2 ticks: 6
    entry  S                      n=406   {'0t': 1, '1t': 1, '2t': 404}  | full 2-tick: 404, less than 2 ticks: 2
    exit   Exit on session close  n=792   {'0t': 3, '1t': 7, '2t': 782}  | full 2-tick: 782, less than 2 ticks: 10
    exit   XL                     n=10    {'2t': 10}  | full 2-tick: 10, less than 2 ticks: 0
    exit   XS                     n=8     {'2t': 8}  | full 2-tick: 8, less than 2 ticks: 0
  -- Flat1559
    entry  L                      n=556   {'0t': 7, '1t': 6, '2t': 543}  | full 2-tick: 543, less than 2 ticks: 13
    entry  S                      n=634   {'0t': 5, '1t': 3, '2t': 626}  | full 2-tick: 626, less than 2 ticks: 8
    exit   Exit on session close  n=6     {'1t': 1, '2t': 5}  | full 2-tick: 5, less than 2 ticks: 1
    exit   FlatEOD                n=423   {'0t': 10, '1t': 11, '2t': 402}  | full 2-tick: 402, less than 2 ticks: 21
    exit   XL                     n=332   {'0t': 9, '1t': 9, '2t': 314}  | full 2-tick: 314, less than 2 ticks: 18
    exit   XS                     n=429   {'0t': 15, '1t': 6, '2t': 408}  | full 2-tick: 408, less than 2 ticks: 21
  -- LastHalfHourMomentum
    entry  LHMomLong              n=698   {'0t': 55, '1t': 32, '2t': 611}  | full 2-tick: 611, less than 2 ticks: 87
    entry  LHMomShort             n=606   {'0t': 29, '1t': 24, '2t': 553}  | full 2-tick: 553, less than 2 ticks: 53
    exit   LHFlat1559             n=1304  {'0t': 36, '1t': 42, '2t': 1226}  | full 2-tick: 1226, less than 2 ticks: 78
```
So the conclusion holds. The artifact, however, grades it from evidence that does not cover most exit types.

Second part of F1: the fills carry "up to 2 ticks", not "2 ticks per side". 384 of 8,988 fills carry 0 or 1 tick (13+8+6+18+21 baseline, 6+2+10 OppBand, 13+8+1+21+18+21 Flat1559, 87+53+78 LastHalfHour). That is the clipping that :51's own plain-words sentence states, and the artifact's sentence drops it. The headline largest-loss trades all carry the full 2 ticks on both legs, so the headline figures are unaffected:
```
Baseline (NoiseArea BandOrVWAP) trade 1182 MNQ -542.40 | entry S px 29316.25 ref 29316.75 slip 2t ; exit XS px 29586.50 ref 29586 slip 2t
OppBand trade 627 MNQ -1960.90 | entry L px 19483.25 ref 19482.75 slip 2t ; exit XL px 18503.75 ref 18504.25 slip 2t
Flat1559 trade 1182 MNQ -542.40 | entry S px 29316.25 ref 29316.75 slip 2t ; exit XS px 29586.50 ref 29586 slip 2t
LastHalfHourMomentum trade 977 MNQ -555.40 | entry LHMomLong px 22111.25 ref 22110.75 slip 2t ; exit LHFlat1559 px 21834.50 ref 21835 slip 2t
```

| exit type | the artifact's evidence | w2 bar test |
|---|---|---|
| entries (all 4) | OBSERVED (:51) | OBSERVED, 0 no-match |
| baseline session close at 16:00 (423) | OBSERVED (:77, :253) | OBSERVED |
| baseline session close, early-close days (6) | INFERRED | OBSERVED (429/429 match a clamp model) |
| XL / XS (baseline, OppBand, Flat1559) | INFERRED | OBSERVED (332/429, 10/8, 332/429) |
| FlatEOD (Flat1559) | INFERRED | OBSERVED (423/423) |
| OppBand session close (792), Flat1559 session close (6) | INFERRED | OBSERVED |
| LHFlat1559 | OBSERVED indirectly (:51 K15) | OBSERVED (1304/1304) |

### 3. Source quotes and stop-API grep — no break
I re-ran every sed range the artifact quotes and checked each output line for a verbatim match in the artifact:
```
sed -n 196,221p ninjascript/PraxisNoiseAreaBreakout.cs -> 25 lines, lines NOT found verbatim in artifact: 0
sed -n 188,192p ninjascript/PraxisNoiseAreaBreakout.cs -> 5 lines, lines NOT found verbatim in artifact: 0
sed -n 229,244p ninjascript/PraxisNoiseAreaBreakout_OppBand.cs -> 16 lines, lines NOT found verbatim in artifact: 0
sed -n 30,33p ninjascript/PraxisNoiseAreaBreakout_OppBand.cs -> 4 lines, lines NOT found verbatim in artifact: 0
sed -n 243,258p ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs -> 16 lines, lines NOT found verbatim in artifact: 0
sed -n 227,231p ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs -> 5 lines, lines NOT found verbatim in artifact: 0
sed -n 91p ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs -> 1 lines, lines NOT found verbatim in artifact: 0
sed -n 46p ninjascript/PraxisLastHalfHourMomentum.cs -> 1 lines, lines NOT found verbatim in artifact: 0
sed -n 205,212p ninjascript/PraxisLastHalfHourMomentum.cs -> 8 lines, lines NOT found verbatim in artifact: 0
sed -n 230,235p ninjascript/PraxisLastHalfHourMomentum.cs -> 6 lines, lines NOT found verbatim in artifact: 0
sed -n 16p research/search-loop/c1-gap-fade/RULES.md -> 1 lines, lines NOT found verbatim in artifact: 0
sed -n 19,23p research/search-loop/c1-gap-fade/RULES.md -> 5 lines, lines NOT found verbatim in artifact: 0
--- single-line cites
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:141: ExitMode      = PraxisNoiseExitMode.OppBand;    // VARIANT 7zq default (base default BandOrVWAP, spec §4 p.13). The only knob.
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:219: bool isCheckpoint = (Time[0].Minute == 0 || Time[0].Minute == 30) && mod > OpenMod && mod < CloseMod;
ninjascript/PraxisLastHalfHourMomentum.cs:194: ExitLong("LHStaleFlat", "LHMomLong");
ninjascript/PraxisLastHalfHourMomentum.cs:200: ExitShort("LHStaleFlat", "LHMomShort");
--- is OppBand :219 shown in artifact's own grep output?
no 'OppBand.cs:219' in artifact
```
A wider stop, limit and unmanaged-order grep finds no hits either (my pattern adds StopLimit, *Limit, SubmitOrderUnmanaged, OrderType., IsUnmanaged and ChangeOrder):
```
PraxisNoiseAreaBreakout.cs: stop/limit/unmanaged API hits=0
PraxisNoiseAreaBreakout_OppBand.cs: stop/limit/unmanaged API hits=0
PraxisNoiseAreaBreakout_Flat1559.cs: stop/limit/unmanaged API hits=0
PraxisLastHalfHourMomentum.cs: stop/limit/unmanaged API hits=0
--- FlattenAll / Exit* call sites
PraxisNoiseAreaBreakout.cs:191:				FlattenAll("16:00 session flat");
PraxisNoiseAreaBreakout.cs:211:					ExitLong("XL", "");
PraxisNoiseAreaBreakout.cs:219:					ExitShort("XS", "");
PraxisNoiseAreaBreakout.cs:285:		private void FlattenAll(string reason)
PraxisNoiseAreaBreakout.cs:288:				ExitLong("FlatEOD", "");
PraxisNoiseAreaBreakout.cs:290:				ExitShort("FlatEOD", "");
```
- **F6 (LOW, S1).** The artifact (:174) cites OppBand `isCheckpoint` as "file :219 in the earlier grep". The artifact's grep does not print :219. The line itself is correct (pasted above), but the artifact never pasted it.
- **F10 (LOW).** "Every exit in all four sources is ExitLong(...) / ExitShort(...)" is true of the source text, since FlattenAll at :285-:290 calls ExitLong/ExitShort("FlatEOD"). But 429 baseline exits and 792 OppBand exits are named "Exit on session close". That is NT8's `IsExitOnSessionCloseStrategy` backstop, not a source ExitLong. The baseline has 0 FlatEOD fills. The artifact's "the 16:00 flat (a market order)" (:135) attributes those exits to the source.

### 4. Verdicts — F2 (MED, S2), F3 (MED, S8), F4/F5/F9 (LOW)
- **F2 (MED, S2): the gap-fade "no loss exceeded it" is circular, and "how a resting stop would behave" over-claims.** RULES.md :20 books every stop at stop ± 0.5 whatever the bar did, so all 286 stop exits equal the bound exactly (`'stop exit == bound exactly': 286` in w2_out.txt). A time exit happens only when the stop was never touched. The simulator therefore cannot produce a loss beyond the bound. "In this list no trade lost more than…" (:278, :306) is true by construction, not evidence. The artifact's own test only checks bar OPENS beyond the stop (0). The bar EXTREMES tell a different story (X2):
```
[X2] gap fade: stop-exit bar overshoot beyond the stop (bar extreme past stop), points
   stop exits 286 | overshoot >0: 273 | >=5pt: 113 | >=10pt: 52 | max 45.50 | top5 [(Decimal('45.50'), '2026-01-14', '100100'), (Decimal('44'), '2024-08-06', '093300'), (Decimal('31.75'), '2025-03-04', '100100'), (Decimal('26.50'), '2026-03-18', '102700'), (Decimal('26.50'), '2022-02-16', '095100')]
   stop exits on the 09:31 entry bar itself (intrabar order unknown): 6
   if every stop fill were the bar extreme +-0.5 instead of stop +-0.5: summed extra loss points 1634.00, worst single-trade extra 45.50
```
  273 of 286 stop-exit bars traded past the stop, 52 of them by 10 pt or more, and the largest overshoot was 45.5 pt (2026-01-14 10:01). 1-minute bars cannot show where a resting stop would have filled inside such a bar. :268 says "tested against each 1-minute bar's high/low, which is how a resting stop would behave". That states as fact a behaviour equivalence nobody has tested. The Limits section (:333) partly hedges ("does not show that a live stop would fill at the level"), but (a) and (d) are not hedged. The S2 level supported by the evidence is "specified in a simulation rule", not "YES".
- **F3 (MED, S8): Q2 is mislabelled and in effect decided.** Q2 (voice notes :65) reads: "Is a stop filled past its level by a news gap or slippage still 'the cost of the trade', or a breach like a server crash?" The artifact says three times that Q2 is about the percentage (:4 "no percentage, no cap … (those are Amear's Q2/Q3/Q6)", :278 "a percentage of the account … (Q2/Q3)", :331 "R3's percentage is undecided (Amear's Q2/Q3)"). The percentage is R3's own TBD (:21-:22). Then the gap-fade YES uses a bound of level + 1 pt modelled slippage + $1.90. That counts the fill past the level as part of the predefined cost, which is exactly the reading Q2 leaves open. Under the other reading (the level alone), every one of the 286 stop exits loses 1.0 pt ($2.00 at MNQ) more than the level, by construction (`stop trades with points != -(|O-PC| + 1.0): 0`, artifact :485). The verdict depends on Q2, and the artifact does not say so.
- **F4 (LOW): "known at the moment of entry" is weaker than R3's "before entry", and a true pre-entry bound exists.** O is the entry bar's open, so the point distance is known only when the order fills. The variant's GMAX gives a bound from PC alone, before the open:
```
[X3] gap fade: bound knowable BEFORE the 09:31 open from GMAX 0.80% and PC alone
   max |O-PC|/PC over trades = 0.797403% (GMAX 0.80)
   max pre-open bound (0.008*PC + 1pt)*2 + 1.90 over trades = 497.92 ; trades whose realized loss exceeds own pre-open bound: 0
```
  This strengthens the structural YES instead of breaking it. The artifact does not use it.
- **F5 (LOW, context).** summary.json has `selection.qualifying: []` and label "for the record, not selected": V2 failed its own in-sample selection. The artifact never says so (`grep -ciE "not selected|qualifying|fails in-sample"` → 0), yet V2 gets the only "Meets R3's structure" line. A reader could take that as leaning on Q6.
- **F9 (LOW): the strongest case against OppBand's NO.** In OppBand mode the exit level is the opposite band. The band is fully computable at 09:30 from the prior 14 days' σ, today's open and the prior close, with no VWAP (`PraxisNoiseAreaBreakout_OppBand.cs` :287-:290 `refUpper = Math.Max(todayOpen, prevClose)` … `curLower = refLower * (1.0 - BandSigmaMult * curSigma)`; :232-:233 picks `curLower` for a long). So a predefined level exists before entry. What is missing is enforcement: a checkpoint-close test with a market exit. "PARTIAL (level predefined, loss not capped)" is defensible. The verdict "Fails R3 as tested" survives either way. Trade 627 ran from the 10:01 entry to the 15:31 exit and lost 979.5 pt ($1,960.90 at MNQ), with MAE $2,223.00 at MNQ (X5):
```
[X5] OppBand worst consecutive pair vs longest streak (2025-04-07/08)
    625 Short 2025-04-04 10:31:00 2025-04-04 16:00:00 S Exit on session close 19150.50 18770.25 MNQ 758.60 MAE/10 465.00
    626 Long 2025-04-07 14:01:00 2025-04-07 16:00:00 L Exit on session close 19020.25 18793.75 MNQ -454.90 MAE/10 760.50
    627 Long 2025-04-08 10:01:00 2025-04-08 15:31:00 L XL 19483.25 18503.75 MNQ -1960.90 MAE/10 2223.00
    628 Short 2025-04-08 15:31:00 2025-04-08 16:00:00 S Exit on session close 18503.75 18469.75 MNQ 66.10 MAE/10 4.50
    629 Long 2025-04-09 10:01:00 2025-04-09 16:00:00 L Exit on session close 18681.75 20486.25 MNQ 3607.10 MAE/10 481.50
```
  For the baseline and Flat1559, NO is robust: VWAP is not known in advance. For LastHalfHour, NO is robust: there is no price level at all. One small wording point: :256 says the "loss is bounded only by the 15:59 time exit", but a time exit bounds the holding time, not the loss.
- No verdict recommends a percentage, a cap, a rerun or a strategy to keep (my word scan found no "recommend/should/worth/rerun/keep/drop" in any verdict). Q6 is not answered.

### 5. Cost line — no break
`DECISIONS.md :1063 contains 'MNQ $1.90': True` (w2_out.txt). The same string is also on lines 970, 1075, 1118, 1124, 1125, 2314 and 2605.

### 7. S13 in the artifact — no break
I counted with a pattern file, so the sentence does not appear a second time in this report:
```
$ grep -c -F -f /tmp/praxis-r3/w2_s13.txt docs/reports/2026-11-14-r3-recheck-worker1.md
1
$ grep -c -F -f /tmp/praxis-r3/w2_s13.txt /tmp/praxis-r3/w2_out.txt /tmp/praxis-r3/w2_extra_out.txt
/tmp/praxis-r3/w2_out.txt:0
/tmp/praxis-r3/w2_extra_out.txt:0
```

### X-runs (w2_extra_out.txt, in full)
```
[X1] adverse slippage residual per fill, ticks (residual vs bar OPEN for all fills; vs bar CLOSE for session-close exits)
  -- Baseline (NoiseArea BandOrVWAP)
    entry  L                      n=556   {'0t': 7, '1t': 6, '2t': 543}  | full 2-tick: 543, less than 2 ticks: 13
    entry  S                      n=634   {'0t': 5, '1t': 3, '2t': 626}  | full 2-tick: 626, less than 2 ticks: 8
    exit   Exit on session close  n=429   {'0t': 2, '1t': 4, '2t': 423}  | full 2-tick: 423, less than 2 ticks: 6
    exit   XL                     n=332   {'0t': 9, '1t': 9, '2t': 314}  | full 2-tick: 314, less than 2 ticks: 18
    exit   XS                     n=429   {'0t': 15, '1t': 6, '2t': 408}  | full 2-tick: 408, less than 2 ticks: 21
  -- OppBand
    entry  L                      n=404   {'0t': 3, '1t': 3, '2t': 398}  | full 2-tick: 398, less than 2 ticks: 6
    entry  S                      n=406   {'0t': 1, '1t': 1, '2t': 404}  | full 2-tick: 404, less than 2 ticks: 2
    exit   Exit on session close  n=792   {'0t': 3, '1t': 7, '2t': 782}  | full 2-tick: 782, less than 2 ticks: 10
    exit   XL                     n=10    {'2t': 10}  | full 2-tick: 10, less than 2 ticks: 0
    exit   XS                     n=8     {'2t': 8}  | full 2-tick: 8, less than 2 ticks: 0
  -- Flat1559
    entry  L                      n=556   {'0t': 7, '1t': 6, '2t': 543}  | full 2-tick: 543, less than 2 ticks: 13
    entry  S                      n=634   {'0t': 5, '1t': 3, '2t': 626}  | full 2-tick: 626, less than 2 ticks: 8
    exit   Exit on session close  n=6     {'1t': 1, '2t': 5}  | full 2-tick: 5, less than 2 ticks: 1
    exit   FlatEOD                n=423   {'0t': 10, '1t': 11, '2t': 402}  | full 2-tick: 402, less than 2 ticks: 21
    exit   XL                     n=332   {'0t': 9, '1t': 9, '2t': 314}  | full 2-tick: 314, less than 2 ticks: 18
    exit   XS                     n=429   {'0t': 15, '1t': 6, '2t': 408}  | full 2-tick: 408, less than 2 ticks: 21
  -- LastHalfHourMomentum
    entry  LHMomLong              n=698   {'0t': 55, '1t': 32, '2t': 611}  | full 2-tick: 611, less than 2 ticks: 87
    entry  LHMomShort             n=606   {'0t': 29, '1t': 24, '2t': 553}  | full 2-tick: 553, less than 2 ticks: 53
    exit   LHFlat1559             n=1304  {'0t': 36, '1t': 42, '2t': 1226}  | full 2-tick: 1226, less than 2 ticks: 78
[X2] gap fade: stop-exit bar overshoot beyond the stop (bar extreme past stop), points
   stop exits 286 | overshoot >0: 273 | >=5pt: 113 | >=10pt: 52 | max 45.50 | top5 [(Decimal('45.50'), '2026-01-14', '100100'), (Decimal('44'), '2024-08-06', '093300'), (Decimal('31.75'), '2025-03-04', '100100'), (Decimal('26.50'), '2026-03-18', '102700'), (Decimal('26.50'), '2022-02-16', '095100')]
   stop exits on the 09:31 entry bar itself (intrabar order unknown): 6
   if every stop fill were the bar extreme +-0.5 instead of stop +-0.5: summed extra loss points 1634.00, worst single-trade extra 45.50
[X3] gap fade: bound knowable BEFORE the 09:31 open from GMAX 0.80% and PC alone
   max |O-PC|/PC over trades = 0.797403% (GMAX 0.80)
   max pre-open bound (0.008*PC + 1pt)*2 + 1.90 over trades = 497.92 ; trades whose realized loss exceeds own pre-open bound: 0
[X4] OppBand/baseline: same-timestamp reversal legs vs multi-trade sessions
   Baseline (NoiseArea BandOrVWAP)  handoffs 1 [(666, 667, '2024-03-08', 'XL', 'S')] | max trades/session 5 | max exposure-episodes/session (reversal legs merged) 5
   OppBand                          handoffs 18 [(16, 17, '2021-05-06', 'XS', 'L'), (27, 28, '2021-06-16', 'XL', 'S'), (100, 101, '2021-12-15', 'XS', 'L')] | max trades/session 2 | max exposure-episodes/session (reversal legs merged) 1
   Flat1559                         handoffs 1 [(666, 667, '2024-03-08', 'XL', 'S')] | max trades/session 5 | max exposure-episodes/session (reversal legs merged) 5
   LastHalfHourMomentum             handoffs 0 [] | max trades/session 1 | max exposure-episodes/session (reversal legs merged) 1
[X5] OppBand worst consecutive pair vs longest streak (2025-04-07/08)
    625 Short 2025-04-04 10:31:00 2025-04-04 16:00:00 S Exit on session close 19150.50 18770.25 MNQ 758.60 MAE/10 465.00
    626 Long 2025-04-07 14:01:00 2025-04-07 16:00:00 L Exit on session close 19020.25 18793.75 MNQ -454.90 MAE/10 760.50
    627 Long 2025-04-08 10:01:00 2025-04-08 15:31:00 L XL 19483.25 18503.75 MNQ -1960.90 MAE/10 2223.00
    628 Short 2025-04-08 15:31:00 2025-04-08 16:00:00 S Exit on session close 18503.75 18469.75 MNQ 66.10 MAE/10 4.50
    629 Long 2025-04-09 10:01:00 2025-04-09 16:00:00 L Exit on session close 18681.75 20486.25 MNQ 3607.10 MAE/10 481.50
```
After the reruns:
```
ls: /Volumes/Sensidine/Praxis.build/scripts/wf/__pycache__: No such file or directory
```

## Negative test
`/tmp/praxis-r3/w2_mutant.csv` is the baseline CSV with ONE losing row changed: trade 342 (2022-10-13 XS) Profit −$5,337.96 → −$6,337.96. (In the pasted diff, `diff_exit=0` is the exit of `cut`, not of `diff`.)
```
343c343
< 342,NQCONTROW SEP25,Backtest,PraxisNoiseAreaBreakout,Short,1,13984.75,14251.50,2022-10-13 11:01:00 AM,2022-10-13 11:31:00 AM,S,XS,-$5337.96,$88462.68,$2.96,$0.00,$0.00,$0.00,$0.00,$7155.00,$285.00,$5622.96,31,
---
> 342,NQCONTROW SEP25,Backtest,PraxisNoiseAreaBreakout,Short,1,13984.75,14251.50,2022-10-13 11:01:00 AM,2022-10-13 11:31:00 AM,S,XS,-$6337.96,$88462.68,$2.96,$0.00,$0.00,$0.00,$0.00,$7155.00,$285.00,$5622.96,31,
```
`python3 -I /tmp/praxis-r3/w2_adv.py --one /tmp/praxis-r3/w2_mutant.csv MUTANT-baseline` (full output, w2_mutant_out.txt):
```
====================================================================================================
STRATEGY: MUTANT-baseline
trades: 1190
losers (MNQ net < 0): 712
ALT losers (NQ Profit < 0): 706 | MNQ<0 but NQ>=0: 6 | MNQ net == 0: 0
largest single loss MNQ: -635.40  at trade(s) [342]  entry date(s) ['2022-10-13']  exit name(s) ['XS']
average loss MNQ (mean over MNQ losers): -97.40  (sum -69349.80 / 712)
largest loss as % of $50,000: 1.2708%   of $150,000: 0.4236%
longest losing run by trade number: length 10, 2 run(s) of that length:
    trades 319..328  entry dates 2022-09-15 .. 2022-09-26  summed MNQ -802.00
    trades 1150..1159  entry dates 2026-05-11 .. 2026-05-20  summed MNQ -1070.50
    (worst-summed run by trade number: length 8 trades 1027..1034 2025-10-13..2025-10-17 sum -1364.70)
longest losing run by exit time (stable on trade number): length 10, 2 run(s) of that length:
    trades 319..328  entry dates 2022-09-15 .. 2022-09-26  summed MNQ -802.00
    trades 1150..1159  entry dates 2026-05-11 .. 2026-05-20  summed MNQ -1070.50
    (worst-summed run by exit time (stable on trade number): length 8 trades 1027..1034 2025-10-13..2025-10-17 sum -1364.70)
longest losing run by entry time (stable on trade number): length 10, 2 run(s) of that length:
    trades 319..328  entry dates 2022-09-15 .. 2022-09-26  summed MNQ -802.00
    trades 1150..1159  entry dates 2026-05-11 .. 2026-05-20  summed MNQ -1070.50
    (worst-summed run by entry time (stable on trade number): length 8 trades 1027..1034 2025-10-13..2025-10-17 sum -1364.70)
ALT longest losing run on NQ<0 by trade number: length 10
by entry date: worst single-day MNQ -805.10 on ['2022-10-13'] (trades that day: [4]) | sessions with a trade 792 | most trades in one session 5 on 3 date(s) first 2023-12-04 | avg trades/session-with-trade 1.5025 | avg trades/calendar session (N=1352) 0.8802
by exit date: worst single-day MNQ -805.10 on ['2022-10-13'] (trades that day: [4]) | sessions with a trade 792 | most trades in one session 5 on 3 date(s) first 2023-12-04 | avg trades/session-with-trade 1.5025 | avg trades/calendar session (N=1352) 0.8802
trades whose exit date != entry date: 0 []
same-timestamp handoffs (exit of trade i == entry of trade i+1): 1
largest MAE at 1 MNQ (NQ MAE/10): 747.50  trade 1182  date 2026-06-25  (NQ MAE 7475.00; that trade MNQ net -542.40)
  commission values: Counter({'2.96': 1190})  qty values: Counter({1: 1190})
  exit names: Counter({'XS': 429, 'Exit on session close': 429, 'XL': 332})
  trades with -NQgross > MAE (loss beyond MAE): 0
  losers by exit type (count, worst MNQ): {'XS': (363, '-635.40'), 'XL': (284, '-447.40'), 'Exit on session close': (65, '-359.90')}
```
The largest loss moves from −542.40 (trade 1182, 2026-06-25) to **−635.40 (trade 342, 2022-10-13)**. The worst day moves from −705.10 to **−805.10** on 2022-10-13. The average loss moves from −97.26 to −97.40, and the % of $50,000 from 1.0848 to 1.2708. The comparison detects a $100 MNQ change in one row.

## Files staged
None. Written: `/tmp/praxis-r3/w2_*` (listed with hashes above) and this report (untracked). As described in Method, `scripts/wf/__pycache__/` was written by my first run and then removed.

## Result: FAIL — on grading, not on figures
All (b)/(e) figures hold, with 0 mismatches. The source quotes, the stop-API grep, the cost line and the S13 count all hold. What breaks:
- **F1 (MED):** the slippage claim is graded above its cited evidence for XL, XS, FlatEOD and non-baseline session-close exits. It is now OBSERVED by w2. "2 ticks" is really "up to 2 ticks" (384 of 8,988 fills carry less).
- **F2 (MED):** the gap-fade "no loss exceeded it" is true by construction, and the claim that the 1-min test behaves like a resting stop is untested (273/286 stop bars overshot, max 45.5 pt).
- **F3 (MED):** Q2 is mislabelled as the percentage question, and the gap-fade YES silently uses one reading of Q2.
- **LOW:** F4 (a GMAX pre-entry bound exists and is unused), F5 (V2 "not selected" omitted), F6 (:219 cited but not pasted), F7 (OppBand max trades/session 2 → 1 when reversal legs are merged), F8 (worst-summed losing run is larger than the longest-run sum), F9 (OppBand PARTIAL is arguable, verdict unchanged), F10 (session-close exits come from the NT8 backstop, not source ExitLong).
