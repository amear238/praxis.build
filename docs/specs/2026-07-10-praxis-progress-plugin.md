# praxis-progress — local Claude Code plugin for progress reports

**Date:** 2026-07-10 · **Bead:** Praxis_build-jpe · **Status:** built + installed (user scope)

## Purpose
Trader asked for a local plugin producing the ASCII progress-bar report toward **live SIM
trading** (sample format captured in the bead description): OVERALL bar, block-by-block bars
with audit annotations, current-block bead detail, and an "audits still required" checklist.
Stakeholder-readable, terminal-native.

## Design decisions
- **Plugin, not bare project skill** (as requested): `plugins/praxis-progress/` with a
  slash command `/progress`, distributed through an in-repo local marketplace
  `plugins/.claude-plugin/marketplace.json` ("praxis-local"). Installed user-scope via
  `claude plugin marketplace add <repo>/plugins` + `claude plugin install
  praxis-progress@praxis-local`.
- **Deterministic data, model-rendered layout.** `scripts/progress-data.sh` (read-only)
  gathers STATUS.md header + Phase Progress, `bd` in-progress/open/closed, AUDIT_LOG.md
  tail, and `git log -10`; the command injects it via `` !`…` `` context expansion and the
  model fills a fixed embedded template. Block names/states come from STATUS.md (source of
  truth), never hardcoded — the report survives block re-scopes without plugin edits.
- **Human gates preserved (praxis-build-manager §F).** The command hard-codes: never render
  a milestone as complete without trader sign-off recorded in STATUS.md; percentages are
  always labeled directional; the pre-live comprehension gate always renders 🔒; the
  command is report-only (no bead closes, no writes, no commits) — safe for headless runs (§G).
- **Update path:** install is a cached copy pinned to a commit; after editing plugin
  source, run `claude plugin update praxis-progress`.

## Verification
- `claude plugin validate` PASS on both plugin and marketplace manifests.
- `progress-data.sh` runs clean (exit 0) from the repo, emitting all sections.
- `claude plugin list` shows praxis-progress 0.1.0 enabled, user scope.
