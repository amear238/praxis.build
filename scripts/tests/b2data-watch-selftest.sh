#!/bin/bash
# b2data-watch-selftest.sh — Praxis_build-3q4 (b2-data-mailbox)
# Self-contained verification harness for the raw-landing validator + watcher.
#
# Depends on NO real data and NO live daemon. It stages synthetic raw/ scenarios
# against TEMP mailbox roots (via the PRAXIS_B2DATA_ROOT / PRAXIS_B2DATA_STATE
# overrides) and asserts the validator's verdict line + the watcher's idempotency.
# Exit 0 iff every assertion passes. Prints a PASS/FAIL line per check.
#
# Maps to design §6 acceptance:
#   A good full set        -> ready=YES oi=PRESENT            (§6.3)
#   B blank-OI first daily -> oi=BLANK ready=NO (STOP)        (§6.3)
#   C missing files        -> ready=NO present=40/44          (§6.3)
#   D watcher idempotency  -> settle-guard + notify-once      (§6.4, settle-guard)
#   E notify failure        -> sweep survives, log still written (§6.5)
set -uo pipefail

TESTDIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCRIPTS_DIR="$(cd "$TESTDIR/.." && pwd)"
VALIDATOR="$SCRIPTS_DIR/b2data_raw_validate.py"
WATCH="$SCRIPTS_DIR/praxis-b2data-watch.sh"

FAILS=0
pass() { echo "PASS: $1"; }
fail() { echo "FAIL: $1"; FAILS=$((FAILS+1)); }
assert_contains() { # label  haystack  needle
  if printf '%s' "$2" | grep -q -- "$3"; then pass "$1"; else
    fail "$1 — expected to contain [$3]; got: $2"; fi
}
assert_eq() { # label  actual  expected
  if [ "$2" = "$3" ]; then pass "$1"; else
    fail "$1 — expected [$3] got [$2]"; fi
}

# --- synthetic fixture generator (self-contained) -----------------------------
# gen_raw <raw_dir> <mode>   mode = good | blankoi | missing
gen_raw() {
  python3 - "$1" "$2" <<'PY'
import csv, os, sys
from datetime import date, timedelta
raw, mode = sys.argv[1], sys.argv[2]
os.makedirs(raw, exist_ok=True)
contracts = ["06-21","09-21","12-21","03-22","06-22","09-22","12-22","03-23",
             "06-23","09-23","12-23","03-24","06-24","09-24","12-24","03-25",
             "06-25","09-25","12-25","03-26","06-26","09-26"]
skip = {"12-23","06-24"} if mode == "missing" else set()   # -> 40/44
blank_first = contracts[0] if mode == "blankoi" else None
for c in contracts:
    if c in skip:
        continue
    mm, yy = c.split("-"); year = 2000 + int(yy); month = int(mm)
    exp = date(year, month, 15)
    # 1-min OHLCV (30 rows, expiry day)
    with open(os.path.join(raw, "NQ-%s_1min.csv" % c), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["Timestamp","Open","High","Low","Close","Volume"])
        for i in range(30):
            ts = "%s 09:%02d:00" % (exp.isoformat(), 30 + i)
            base = 15000 + i
            w.writerow([ts, base, base+5, base-5, base+2, 100 + i])
    # daily bars w/ Volume + Open Interest (40 rows ending at expiry)
    with open(os.path.join(raw, "NQ-%s_daily.csv" % c), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["Date","Open","High","Low","Close","Volume","OpenInterest"])
        for i in range(40):
            d = exp - timedelta(days=(39 - i))
            base = 15000 + i
            oi = "" if (blank_first == c) else (200000 + i * 10)
            w.writerow([d.isoformat(), base, base+20, base-20, base+8, 5000 + i, oi])
PY
}

echo "=== b2data-watch self-test ==="
echo "validator: $VALIDATOR"
echo "watcher:   $WATCH"
echo

# --- Scenario A: good full set -----------------------------------------------
ROOTA="$(mktemp -d)"; gen_raw "$ROOTA/raw" good
SUMA="$(python3 "$VALIDATOR" --root "$ROOTA" 2>/dev/null | grep -m1 '^SUMMARY')"
echo "[A good ]  $SUMA"
assert_contains "A: present=44/44" "$SUMA" "present=44/44"
assert_contains "A: oi=PRESENT"    "$SUMA" "oi=PRESENT"
assert_contains "A: ready=YES"     "$SUMA" "ready=YES"

# --- Scenario B: blank-OI first daily -> OI_BLANK / STOP ----------------------
ROOTB="$(mktemp -d)"; gen_raw "$ROOTB/raw" blankoi
SUMB="$(python3 "$VALIDATOR" --root "$ROOTB" 2>/dev/null | grep -m1 '^SUMMARY')"
echo "[B blank]  $SUMB"
assert_contains "B: oi=BLANK"      "$SUMB" "oi=BLANK"
assert_contains "B: ready=NO"      "$SUMB" "ready=NO"
assert_contains "B: stop=OI_BLANK" "$SUMB" "stop=OI_BLANK"
if grep -q "STOP" "$ROOTB/reports/raw-landing-validation.md" 2>/dev/null; then
  pass "B: report carries the STOP notice"; else fail "B: report missing STOP notice"; fi

# --- Scenario C: missing files -> ready=NO present=40/44 ----------------------
ROOTC="$(mktemp -d)"; gen_raw "$ROOTC/raw" missing
SUMC="$(python3 "$VALIDATOR" --root "$ROOTC" 2>/dev/null | grep -m1 '^SUMMARY')"
echo "[C miss ]  $SUMC"
assert_contains "C: present=40/44" "$SUMC" "present=40/44"
assert_contains "C: ready=NO"      "$SUMC" "ready=NO"

# --- Scenario D: watcher settle-guard + idempotency --------------------------
ROOTD="$(mktemp -d)"; STATED="$(mktemp -d)"; gen_raw "$ROOTD/raw" good
LOGD="$ROOTD/reports/landing-log.txt"
run_sweep() {
  PRAXIS_B2DATA_ROOT="$ROOTD" PRAXIS_B2DATA_STATE="$STATED" \
    PRAXIS_NOTIFY=/usr/bin/true "$WATCH" once
}
landed_count() { awk '/landed NQ-/{n++} END{print n+0}' "$LOGD" 2>/dev/null || echo 0; }

run_sweep                          # sweep 1: first sighting -> settle-guard defers
C1="$(landed_count)"
assert_eq "D: sweep1 defers un-settled files (settle-guard)" "$C1" "0"

run_sweep                          # sweep 2: size unchanged -> settled -> notify once
C2="$(landed_count)"
assert_eq "D: sweep2 notifies all 44 settled files" "$C2" "44"

run_sweep                          # sweep 3: unchanged -> zero new notifications
C3="$(landed_count)"
assert_eq "D: sweep3 idempotent (no duplicate notifications)" "$C3" "44"

SEEN_N="$(wc -l < "$STATED/b2data-seen.txt" 2>/dev/null | tr -d ' ')"
assert_eq "D: seen-state holds exactly 44 files" "$SEEN_N" "44"

SUMD="$(grep -m1 '^SUMMARY' "$ROOTD/reports/raw-landing-validation.md" 2>/dev/null)"
echo "[D done ]  $SUMD"
assert_contains "D: completion battery wrote ready=YES report" "$SUMD" "ready=YES"

# --- Scenario E: notify failure never crashes the sweep (§6.5) ---------------
ROOTE="$(mktemp -d)"; STATEE="$(mktemp -d)"; gen_raw "$ROOTE/raw" good
run_sweep_e() {
  PRAXIS_B2DATA_ROOT="$ROOTE" PRAXIS_B2DATA_STATE="$STATEE" \
    PRAXIS_NOTIFY=/usr/bin/false "$WATCH" once
}
run_sweep_e; RC1=$?          # sweep 1 (settle)
# simulate a coworker status edit between sweeps
printf 'export in progress; OI column confirmed non-zero on 06-21\n' > "$ROOTE/inbound/status.txt"
run_sweep_e; RC2=$?          # sweep 2 (notify with a FAILING notifier)
assert_eq "E: sweep exits 0 despite failing notifier (rc1)" "$RC1" "0"
assert_eq "E: sweep exits 0 despite failing notifier (rc2)" "$RC2" "0"
LOGE="$ROOTE/reports/landing-log.txt"
if [ -s "$LOGE" ]; then pass "E: landing-log written with Telegram down"; else
  fail "E: landing-log empty/absent with Telegram down"; fi
if grep -q 'status.txt update' "$LOGE" 2>/dev/null; then
  pass "E: status.txt edit relayed to the log"; else
  fail "E: status.txt edit not relayed"; fi

echo
if [ "$FAILS" -eq 0 ]; then
  echo "RESULT: ALL SCENARIOS PASS"
  exit 0
else
  echo "RESULT: $FAILS ASSERTION(S) FAILED"
  exit 1
fi
