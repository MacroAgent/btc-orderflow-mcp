---
name: btc-report
description: "Use when user asks about BTC market, order flow, price direction, or trading signals"
---

# BTC Order Flow Report

When this skill is invoked, use the `btc` MCP server to fetch and present the latest market analysis.

## Steps

1. Call `mcp__btc__get_btc_report` to fetch the latest hourly order flow report
2. Present the full report to the user in a clear, readable format
3. If the user asks about historical data or trend, call `mcp__btc__get_report_history` with the appropriate `hours` parameter (1–168, default 24)

## Tool reference

- `mcp__btc__get_btc_report` — returns JSON string with: `id`, `coin`, `ts`, `price_at_diag`, `direction` (bull/bear), `ai_analysis`, `model_used`
- `mcp__btc__get_report_history(hours: int)` — returns JSON array of report objects, newest first

## Usage

Triggered by `/btc-orderflow-mcp:btc-report` or automatically when user asks about BTC market conditions.
