# b2-data Mailbox + Raw-Landing Validation Watcher — Implementer Report

**Date:** 2026-07-20
**Bead:** Praxis_build-3q4 (b2-data-mailbox)
**Spec:** `docs/specs/2026-07-20-b2-data-mailbox-watcher-design.md` (§2–§3 built; §4 continuous-series checks OUT OF SCOPE)
**Status:** BUILT + self-test PASS. Staged, NOT committed.

## What was built

A NEW, INDEPENDENT launchd daemon (`build.praxis.b2data-watch`) that turns the
Parallels share `~/praxis-signals/b2-data/` into a bidirectional file mailbox and
auto-runs raw-landing validation (OI gate + 44-file completeness) on the VM→Mac
NQ export. It clones the proven `praxis-signals-sweep-daemon` pattern (persistent
KeepAlive, internal-disk install for TCC) and does **not** touch the live
signal-path daemons (`build.praxis.signals-*`).

## File list (all SOURCE in repo)

| Path | Role |
|---|---|
| `scripts/praxis-b2data-watch.sh` | Sweep daemon (§2.2): settle-guard, seen-state, dispatch, calls validator |
| `scripts/b2data_raw_validate.py` | Raw-landing validator (§3): OI gate, completeness, sanity, coverage → report |
| `scripts/praxis-b2data-watch-install.sh` | Idempotent installer: scaffold mailbox + internal-disk copy + plist load (TCC-safe) |
| `deploy/launchd/build.praxis.b2data-watch.plist` | KeepAlive LaunchAgent template (`__BIN_DIR__`, `__MAILBOX_ROOT__`) |
| `scripts/tests/b2data-watch-selftest.sh` | Self-contained auditor harness (§6 verification command) |
| `docs/reports/2026-07-20-b2data-mailbox-watcher.md` | This report |
| `MANIFEST.md` | Updated (6 rows) |

Mailbox scaffolding (dirs + `outbound/INSTRUCTIONS.md` export brief + empty
`inbound/status.txt`) is created by the installer's `scaffold`/`deploy`/`install`
actions — verified in a sandboxed `HOME` with no side effects.

## Design choices (were left to the implementer)

- **Validator language: Python** (`b2data_raw_validate.py`). Cleaner CSV parsing,
  header matching, and median math than bash. Runs from the internal-disk install
  and honors a temp-root override (`--root DIR` / env `PRAXIS_B2DATA_ROOT`) so the
  self-test never reads `~/praxis-signals`.
- **Seen-state / settle-guard:** `~/.praxis/state/b2data-seen.txt` (one basename
  per line) gives notify-exactly-once; `b2data-sizes.txt` (name⇥size per sweep)
  gives the settle-guard — a file is acted on only when its previous recorded size
  equals the current size (unchanged across two consecutive sweeps) and >0. A file
  on first sighting is deferred to the next sweep. Completion is de-duped by a
  signature over (present-count, marker, seen-set) in `b2data-completion.txt`, and
  `status.txt` relay is de-duped by its mtime in `b2data-status-mtime.txt`. All
  bash-3.2-safe (no associative arrays; `awk` lookups against the sizes file).
- **OI detection:** case-insensitive header match on `open`+`interest`; documented
  fallback = the **last column** (NT8 daily export ends `…,Volume,OpenInterest`).
  "Populated" = non-zero for a **majority** of rows; min/median/max + non-zero
  fraction reported. `OI_PRESENT` vs `OI_BLANK`.
- **Report machine-summary line** is the very first line:
  `SUMMARY present=44/44 oi=PRESENT ready=YES` (adds `stop=OI_BLANK` on the blank
  path). This is the seam Phase 2 (n8n headless) will key off.

## How the self-test proves each §6 acceptance item

Run: `bash scripts/tests/b2data-watch-selftest.sh` → **exit 0, RESULT: ALL SCENARIOS PASS.**
It stages synthetic `raw/` into TEMP roots (never `~/praxis-signals`) and asserts:

- **§6.1 mailbox + seeds** — installer `deploy` in a sandboxed `HOME` created all
  four dirs, `outbound/INSTRUCTIONS.md` (the export brief), and an empty
  `inbound/status.txt`. Rendered plist passed `plutil -lint` with no unreplaced
  placeholders.
- **§6.2 source + internal-disk install** — installer copies watcher+validator+
  notify.sh to `~/Library/Application Support/Praxis/bin` and the plist
  `ProgramArguments` points there (internal disk, TCC-safe); repo holds SOURCE only.
- **§6.3 dry-run verdicts** —
  - A good full set → `SUMMARY present=44/44 oi=PRESENT ready=YES`.
  - B a blank-OI first daily → `oi=BLANK ready=NO stop=OI_BLANK`, and the report
    body carries the `STOP` notice (volume-only fallback needs trader sign-off +
    a DECISIONS entry, D-2026-07-17-A).
  - C a missing-files set → `ready=NO present=40/44`.
- **§6.4 idempotency + settle-guard** — three watcher sweeps over an unchanged
  good set: sweep 1 defers all files (settle-guard → 0 landings), sweep 2 notifies
  all 44 settled files exactly once, sweep 3 produces **zero** new landings; the
  seen-state holds exactly 44 entries.
- **§6.5 Telegram failure tolerance** — with `PRAXIS_NOTIFY=/usr/bin/false` the
  sweep still exits 0, `reports/landing-log.txt` is still written, and a
  `status.txt` edit is still relayed to the log.

### Self-test output (verbatim summary)

```
[A good ]  SUMMARY present=44/44 oi=PRESENT ready=YES
[B blank]  SUMMARY present=44/44 oi=BLANK ready=NO stop=OI_BLANK
[C miss ]  SUMMARY present=40/44 oi=PRESENT ready=NO
D: sweep1 defers un-settled files (settle-guard)  PASS
D: sweep2 notifies all 44 settled files           PASS
D: sweep3 idempotent (no duplicate notifications) PASS
D: seen-state holds exactly 44 files              PASS
E: sweep exits 0 despite failing notifier         PASS
E: landing-log written with Telegram down         PASS
RESULT: ALL SCENARIOS PASS
```

## Deviations / notes

- **Internal-disk path** is `~/Library/Application Support/Praxis/bin` (the actual
  proven `praxis-signals-install.sh` `BIN_DIR`), not the loosely-worded
  `~/.praxis/bin/` from the bead text. Both are internal disk; this one reuses the
  already-installed `notify.sh` and matches the existing daemon layout exactly. The
  TCC constraint (never execute from `/Volumes/Sensidine`) is satisfied.
- **Date-coverage** (§3.3 per-contract coverage) is implemented as a **coarse,
  non-blocking WARN** (spec: "Coarse sanity, not exact") so it never produces a
  false `ready=NO`; only completeness, OI, and hard file-sanity failures gate
  readiness.
- Nothing was loaded via `launchctl` and no live daemon was touched; installer runs
  were sandboxed (`HOME=$tmp`). Activation on the deployment Mac is a follow-up
  step: `scripts/praxis-b2data-watch-install.sh install`.
- Out of scope and NOT built (correctly): b2-data §4 continuous-series validation,
  the Python stitch tool, and the Phase 2 n8n headless trigger.
