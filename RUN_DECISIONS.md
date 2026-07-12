# RUN_DECISIONS — 2026-07-09 — autonomous run: clear Block-1 ready beads

Trigger: "run the next steps autonomously. i can be readed via telegram" (user stepping away, reachable via Telegram).
Phase-0 question round SKIPPED — user unavailable; scope fixed by HANDOFF resume card (session 3) + bd ready. Precedent: 2026-07-08 DECISION_LOG autonomous entry ("ping me on telegram"). ORCH_N8N_WEBHOOK is SET → notify.sh delivers to Telegram for blockers/safe-defaults.
Max iterations: 25.

Planned bead order (P0→P2):
1. Praxis_build-p7s (B1-b) — n8n LOCAL file-write node → outbox. Dep B1-c CLOSED. Build via n8n MCP + verify.
2. Praxis_build-4hd (B1-c-fu) — live-fire stale-heartbeat alert. Verify send-side autonomously; Telegram-ping trader for the receive-side human confirmation (I cannot read trader's Telegram).
3. Praxis_build-10i — design doc only (least-priv scope); PARK the build (external control path + authority-scope decision needs trader).
4. Praxis_build-30h (bug) — AUDIT_LOG flush path. Done LAST so the audit gate stays stable for the core work. Decision pre-made (option a).

## D1: Autonomy scope for this run
**Answer (safe-default, not asked):** Build + verify fully autonomously for in-repo / reversible work (n8n workflow edits are reversible; live sim path carries no real orders). | **Scope:** all 4 beads.

## D2: B1-b target path (D-2026-07-09-D re-scope)
**Answer:** n8n Write-File node writes atomically (.tmp → rename .json) into the outbox dir; the existing B1-c 60s launchd sweep relays outbox → ~/praxis-signals/incoming → VM drop. Host outbox = /Users/admin/n8n-compose/local-files/outbox; implementer finds the in-container mount from the compose file. | **Scope:** Praxis_build-p7s.

## D3: B1-c-fu receive-side verification
**Answer (safe-default):** I cannot observe the trader's Telegram inbox. Fire the live test, verify the alert was SENT (n8n execution 200 / notify webhook), then Telegram-ping the trader to confirm receipt. If receipt can't be auto-confirmed, close the send-side and leave a human-confirm note; do NOT block the run. | **Scope:** Praxis_build-4hd.

## D4: Telegram→Claude inbound channel (10i) authority scope — NEVER-DEFAULT (external control path)
**Answer (safe-default):** Build the DESIGN DOC ONLY, with least-privilege scope = read/report/status only (bead's own recommendation). PARK the actual build/activation as blocked-on-trader — it creates an execution path from an external channel into the host shell and needs trader sign-off on authority scope + Telegram bot credential. Notify via Telegram. | **Scope:** Praxis_build-10i.

## Never-default list active this run
destructive/irreversible ops · force-push · spending money · publishing outside the repo · creating/rotating credentials · deleting user data · activating an external→shell control path (10i build).
