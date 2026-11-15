# PRAXIS — Automated NQ Futures Trading System

TradingView → n8n → NinjaTrader 8 → Rithmic → MFFU

## Quick Links
- **Current State:** See [STATUS.md](./STATUS.md)
- **Amear's rulings:** See [RULINGS.md](./RULINGS.md)
- **Older tracking files:** See [archive/2026-11-15/](./archive/2026-11-15/)

## Monitoring
- **ClickUp:** [PRAXIS — Phase 3 Build space — link TBD]
- **Google Sheets:** [PRAXIS Phase 3 Build Tracker](https://docs.google.com/spreadsheets/d/12XNBvD6Ybp5HMGeU_XG6chKUzxWurn-z7M6TUbLvKoc/edit)
- **GitHub:** https://github.com/amear238/praxis.build

## Architecture
Deterministic signal pipeline. No AI/LLM in execution path.
Local server with UPS, 5G failover, n8n health monitoring.
Six build blocks from $0 proof-of-concept through graduated live deployment.
