# Report: Orchestrator Notify Webhook (Bead Praxis_build-w7b)

Date: 2026-07-08
Task: Build, publish, and verify an n8n workflow that lets shell hooks ping the trader (Amear) on Telegram.

## Workflow

- Name: `PRAXIS — Orchestrator Notify`
- Workflow ID: `Wq90beq5oysV1bpe`
- URL: https://n8n.myzerker626.win/workflow/Wq90beq5oysV1bpe
- Published: yes (active version `e08e04be-ac8c-449a-b728-4c284ff18bf3`)
- Production endpoint: `POST https://n8n.myzerker626.win/webhook/praxis-orch-notify`
- Payload contract: JSON `{event, project, detail}` (all optional strings)

### Nodes

1. **Orchestrator Webhook** — `n8n-nodes-base.webhook` v2.1, POST, path `praxis-orch-notify`, responseMode `responseNode`
2. **Respond OK** — `n8n-nodes-base.respondToWebhook` v1.5, responds immediately with `{"ok": true}`
3. **Telegram: Notify Trader** — `n8n-nodes-base.telegram` v1.2, resource `message`, operation `sendMessage`, chatId `6156528469`, credential `Orchastrator-Mine` (id `F9Q7ibTWgyAQpNAT`, referenced only — not created or modified), `additionalFields.appendAttribution: false`
   - Message template: `🤖 {{ $json.body?.event ?? $json.event ?? "notification" }} — {{ $json.body?.project ?? $json.project ?? "PRAXIS" }}\n{{ $json.body?.detail ?? $json.detail ?? "" }}`

## Verification

1. **validate_workflow**: `{"valid": true, "nodeCount": 3}`

2. **curl** (production webhook):

   ```
   $ curl -s -X POST https://n8n.myzerker626.win/webhook/praxis-orch-notify \
       -H 'Content-Type: application/json' \
       -d '{"event":"run-start","project":"Praxis.build","detail":"Autonomous run active — orchestrator will ping here if you are needed. (path verification, no action required)"}'
   {"ok":true}
   HTTP status: 200
   ```

3. **Execution evidence** (get_execution): execution id `1030337`, mode `webhook`, status `success` (started 2026-07-08T15:29:12.513Z). Node `Telegram: Notify Trader` executionStatus: **success**, output:

   ```json
   {
     "ok": true,
     "result": {
       "message_id": 4,
       "from": {"id": 8344523288, "is_bot": true, "username": "orchastrator_Mine_bot"},
       "chat": {"id": 6156528469, "first_name": "Amear", "last_name": "Bani Ahmad", "type": "private"},
       "text": "🤖 run-start — Praxis.build\nAutonomous run active — orchestrator will ping here if you are needed. (path verification, no action required)"
     }
   }
   ```

   Message confirmed delivered to Amear's Telegram (chat 6156528469).

## Repo changes

- `.claude/settings.json`: added top-level `env` key with `"ORCH_N8N_WEBHOOK": "https://n8n.myzerker626.win/webhook/praxis-orch-notify"`. All existing hooks preserved; JSON validated with `python3 -m json.tool`.
- `docs/reports/2026-07-08-orch-notify.md`: this report.

Hooks can now ping the trader with:

```sh
curl -s -X POST "$ORCH_N8N_WEBHOOK" -H 'Content-Type: application/json' \
  -d '{"event":"...","project":"...","detail":"..."}'
```
