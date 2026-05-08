# Project: PRAXIS — Automated NQ Futures Trading System

## Identity
- Automated trading infrastructure: TradingView → n8n → NinjaTrader 8 → Rithmic → MFFU
- Primary language: NinjaScript (C# on .NET 4.8), Python, JavaScript
- Key dependencies: NinjaTrader 8, n8n (self-hosted Docker), TradingView, Rithmic API

## Current Phase
Read STATUS.md for current state before doing anything.

## Rules
- Read STATUS.md first, every session
- Update STATUS.md at session end
- Update MANIFEST.md when creating or modifying files
- Append to DECISIONS.md for any architectural choice
- Use `bd ready` to find work, `bd show <id>` for details, `bd close <id>` when done
- Commit after every meaningful change
- Do not advance to next phase without trader confirmation

## Architecture
Signal flow: TradingView alert → webhook → n8n workflow → JSON file drop → NinjaScript FileSystemWatcher → bracket order → Rithmic → MFFU
Monitoring: Git (source of truth) → STATUS.md → Google Sheets → ClickUp → n8n → Telegram

## Do Not
- Skip STATUS.md read
- Make architectural decisions without logging to DECISIONS.md
- Create files without updating MANIFEST.md
- Advance phases without trader sign-off
- Trade or execute orders on live accounts without explicit authorization
