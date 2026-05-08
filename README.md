# PRAXIS — Automated NQ Futures Trading System

TradingView → n8n → NinjaTrader 8 → Rithmic → MFFU

## Quick Links
- **Current State:** See [STATUS.md](./STATUS.md)
- **Decision History:** See [DECISIONS.md](./DECISIONS.md)
- **Build Manifest:** See [MANIFEST.md](./MANIFEST.md)

## Monitoring
- **ClickUp:** [PRAXIS — Phase 3 Build space — link TBD]
- **Google Sheets:** [PRAXIS Phase 3 Build Tracker — link TBD]
- **GitHub:** https://github.com/amear238/praxis.build

## Architecture
Deterministic signal pipeline. No AI/LLM in execution path.
Local server with UPS, 5G failover, n8n health monitoring.
Six build blocks from $0 proof-of-concept through graduated live deployment.
