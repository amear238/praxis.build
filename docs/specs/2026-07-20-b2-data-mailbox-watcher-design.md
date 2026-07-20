# B2-Data Mailbox + Raw-Landing Validation Watcher — Design

**Date:** 2026-07-20
**Bead:** Praxis_build-<mailbox> (b2-data-mailbox)
**Status:** DESIGN — trader-approved approach (A + auto-validate; C deferred to Phase 2), 2026-07-20.
**Serves:** Praxis_build-hlw (b2-data) — makes the VM→Mac data pull complete and validate **without a human relay**.
**Locks respected:** D-2026-07-17-A (per-contract export → Python stitch), D-2026-07-09-A (no third-party coordination plane — this uses only the existing Parallels share + local n8n/Telegram).

---

## 1. Problem

Today the trader is the middleman between the VM coworker (who runs NT8, exports contract
CSVs) and the Mac (repo host / Claude). The coworker only has the VM + the Parallels
shared folder (`\\Mac\praxis-signals` == `~/praxis-signals` on the Mac). The **data files
already auto-cross** the share; what still routes through the trader is:

1. **Mac→VM instructions** — Claude produces a brief, the trader pastes it to the coworker.
2. **VM→Mac status** — the coworker says "done" / "OI blank" / asks a question, the trader
   relays it to Claude.
3. **"Did it land / is it valid?"** — nobody knows without a human checking the folder.

## 2. Solution (Approach A)

Turn the shared folder into a **bidirectional file mailbox** and add a **Mac-side watcher
daemon** that notifies on landings, relays coworker status, and **auto-runs raw-landing
validation** (including the Open-Interest gate). Reuses the proven `signals-sweep-daemon`
pattern. Phase 2 (separate, later bead): n8n-triggered headless auto-validation.

### 2.1 Mailbox layout (under the share, `~/praxis-signals/b2-data/`)

```
b2-data/
  outbound/                     # Mac → VM (Claude writes, coworker reads in the VM)
    INSTRUCTIONS.md             # current task brief for the coworker
  inbound/                      # VM → Mac (coworker writes, watcher reads)
    status.txt                  # free-text status / questions / "done" / "OI blank"
  raw/                          # coworker drops the 22×2 export CSVs (already the plan)
    _EXPORT-COMPLETE            # optional marker the coworker touches when all 44 files are written
  reports/                      # watcher writes results here (visible to coworker + trader)
    raw-landing-validation.md   # rolling validation report
    landing-log.txt             # append-only log of every file seen + every notification
```

### 2.2 Watcher daemon

- **Script:** `praxis-b2data-watch.sh` — a clone of `praxis-signals-sweep-daemon.sh`
  (KeepAlive launchd job, sweep loop). Interval **15s** (data landing is not
  latency-sensitive; keeps CPU near zero).
- **Install (TCC rule, per memory `macos-launchd-launchagent-jobs-cannot-run-scripts-stored`):**
  installer copies the script to the **internal disk** (`~/.praxis/bin/`), and the plist
  `ProgramArguments` points at the internal path. Data/log/report dirs live under
  `~/praxis-signals` (internal disk — fine). The repo holds SOURCE only.
- **Plist:** `build.praxis.b2data-watch.plist` in `~/Library/LaunchAgents/`.
- **State:** a seen-files state file (e.g. `~/.praxis/state/b2data-seen.txt`) so a file is
  notified **exactly once** across sweeps (same idempotency approach as the signals daemon).
- **File-settle guard:** a file is only acted on once its size is **unchanged across two
  consecutive sweeps** (avoids parsing a half-written CSV mid-export).

**Per-sweep behavior:**

1. **New stable CSV in `raw/`** → append to `landing-log.txt`; Telegram + report:
   `"landed NQ-03-22_daily.csv (N/44)"`.
2. **First stable `*_daily.csv`** → run the **OI-check** (§3.1) → Telegram + report the
   verdict. If OI blank/zero → a loud `⚠️ OI BLANK — STOP` message stating the
   volume-only fallback needs trader sign-off + a DECISIONS entry before use (D-2026-07-17-A).
3. **`inbound/status.txt` mtime changed** → Telegram + append to log the new contents (so
   the coworker's free-text reaches the trader/Claude with no relay).
4. **Completion** (all 44 expected files present & stable, **or** `_EXPORT-COMPLETE`
   present) → run the **full raw-landing battery** (§3) → write `raw-landing-validation.md`
   + Telegram summary + one-line "ready to stitch" (or "NOT ready — see report").

**Resilience:** Telegram delivery via `notify.sh` is **best-effort** (token rotation still
open — see B1-c-fu). Every notification is **also** written to `reports/` in the share, so
the system is fully functional with Telegram down. The watcher must never crash the sweep
on a Telegram failure.

## 3. Auto-validation — RAW-LANDING checks only

> **Scope boundary (critical):** this validates the **raw per-contract files** — the
> question *"is the export complete and stitch-ready, and is OI present?"*. It does **NOT**
> run b2-data spec §4 (bar-count medians, TZ/DST boundaries, gap analysis, roll seams) —
> those operate on the **stitched continuous series** and belong to the Python stitch step
> (a separate bead). Keeping these apart prevents false "validated" claims.

Script: `praxis-b2data-validate.sh` (or a small Python helper `b2data_raw_validate.py`
under `scripts/` — implementer's choice, but it must run from the internal-disk install and
read `~/praxis-signals/b2-data/raw/`). Emits a machine-readable + human-readable report.

### 3.1 OI-check (per `_daily.csv`, and the headline gate)

- Daily CSV has an **Open Interest** column (case-insensitive header match on "open" +
  "interest", or a documented fallback to a fixed column position).
- OI is **populated**: non-zero for a **majority** of rows (report min / median / max +
  the non-zero fraction).
- Verdict: `OI_PRESENT` or `OI_BLANK`. `OI_BLANK` → the loud STOP notification (§2.2 step 2).

### 3.2 Completeness

- Expected set = **22 contracts × 2 files = 44**:
  `06-21, 09-21, 12-21, 03-22, 06-22, 09-22, 12-22, 03-23, 06-23, 09-23, 12-23, 03-24,
  06-24, 09-24, 12-24, 03-25, 06-25, 09-25, 12-25, 03-26, 06-26, 09-26`, each as
  `NQ-<MMM-YY>_1min.csv` + `NQ-<MMM-YY>_daily.csv`.
- Report which are present / missing. `N/44` count in every notification.

### 3.3 Per-file sanity

- No zero-byte / truncated files (header + ≥1 data row).
- Each CSV parses (consistent column count).
- `_1min.csv`: has timestamp + O/H/L/C/V columns; row count above a plausible floor for a
  quarterly's liquid window (flag suspiciously small files).
- `_daily.csv`: has date + O/H/L/C + **Volume** + **Open Interest** columns.
- **Per-contract date coverage**: min/max timestamp roughly overlaps the contract's expected
  liquid window (e.g. `03-22` trades late-2021 → Mar-2022). Coarse sanity, not exact.

### 3.4 Report format (`reports/raw-landing-validation.md`)

Header verdict line — `READY TO STITCH` / `NOT READY (blockers: …)` — then: OI verdict +
numbers, completeness table (present/missing), per-file sanity flags, timestamp of the run.
Machine-parseable summary line at top (e.g. `SUMMARY present=44/44 oi=PRESENT ready=YES`) so
Phase 2 (n8n headless) can key off it later.

## 4. Components & boundaries

| Unit | Does | Depends on |
|------|------|------------|
| Mailbox convention (dirs + `INSTRUCTIONS.md` + `status.txt`) | Bidirectional file channel | Parallels share (exists) |
| `praxis-b2data-watch.sh` | Sweep, settle-guard, seen-state, dispatch notifications, call validator | `notify.sh`, validator |
| `praxis-b2data-validate.sh` / `.py` | Raw-landing checks + OI gate → report | `raw/` contents |
| `praxis-b2data-watch-install.sh` | Internal-disk copy + plist load (TCC-safe) | — |
| `build.praxis.b2data-watch.plist` | launchd KeepAlive job → internal-disk script | installer |

## 5. Out of scope (explicit)

- Full §4 continuous-series validation — belongs to the Python stitch bead.
- The Python Vol/OI-crossover + Difference stitch itself — separate bead.
- Phase 2 n8n headless auto-validate trigger (Approach C) — separate later bead; the §3.4
  machine-summary line is the seam it will hook.
- Any change to the live signal-path daemons — this is a **new, independent** daemon.

## 6. Acceptance criteria

1. Mailbox dirs + seed `outbound/INSTRUCTIONS.md` (holds the current export brief) +
   empty `inbound/status.txt` exist under `~/praxis-signals/b2-data/`.
2. `praxis-b2data-watch.sh`, `praxis-b2data-validate.sh` (or `.py`), the installer, and the
   plist exist in the repo as SOURCE; installer copies to `~/.praxis/bin/` and loads the job.
3. **Dry-run proof (no real data needed):** drop synthetic fixture CSVs into a temp `raw/`
   (a good set → `READY TO STITCH oi=PRESENT`; a set with a blank-OI daily → the `OI_BLANK`
   STOP path; a missing-file set → `NOT READY present=<N>/44`). Validator produces the
   correct verdict + report for each; watcher notifies exactly once per file and relays a
   `status.txt` edit. Evidence captured in the report doc.
4. Idempotency: re-running the sweep over an unchanged `raw/` produces **no** duplicate
   notifications.
5. Telegram failure does not crash the sweep; the `reports/` file is still written.
6. MANIFEST.md updated for new files; this design doc committed.

**Verification command (auditor re-runs):**
`bash scripts/tests/b2data-watch-selftest.sh` — a self-contained test that stages the three
synthetic `raw/` scenarios against a temp mailbox root and asserts the validator's verdict
line for each, plus a seen-state idempotency assertion. (Implementer creates this harness.)
