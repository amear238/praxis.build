# Decisions Log — PRAXIS

## Decision 1 — 2026-05-08
**Context:** Project needed version control and remote backup.
**Decision:** Git repo initialized at /Volumes/Sensidine/Praxis.build/, pushed to GitHub as amear238/praxis.build (public).
**Rationale:** Git is the source of truth for code + state files + history. GitHub provides remote backup and is physically downloadable via git clone.
**Impact:** All project files tracked from this point forward.

---

## Decision 2 — 2026-05-08
**Context:** Phase 3 research defaulted to Chicago VPS and Claude API integration.
**Decision:** Local server is the default. Execution is deterministic code — no LLM, no API at order placement. Milestones replace deadlines.
**Rationale:** Trader has equivalent redundancy (UPS, 5G, n8n watchdog). Latency irrelevant for clock-anchored strategy. Education timeline is unknown — deadlines create pressure that feeds behavioral pattern.
**Impact:** Monthly cost reduced by $42-85/month. Full local visibility feeds conviction requirement.

---
