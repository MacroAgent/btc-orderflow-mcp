---
name: btc-report
description: "Use when user asks about BTC market, order flow, price direction, or trading signals"
---

# BTC Order Flow Report

When this skill is invoked, use the `plugin_btc-orderflow-mcp_btc` MCP server to fetch and present the latest market analysis.

## Steps

1. Detect the user's language from the conversation (English → `language="en"`, Chinese/中文 → `language="zh"`). Default to `"en"`.
2. Call `mcp__plugin_btc-orderflow-mcp_btc__get_btc_report(language=<detected>)` to fetch the latest hourly order flow report.
3. Output ONLY the `ai_analysis.free_text` field content exactly as-is. Do not add any extra fields, labels, metadata, footers, or commentary of your own.
4. If the user asks about historical data or trend, call `mcp__plugin_btc-orderflow-mcp_btc__get_report_history` with the appropriate `hours` parameter (1–168, default 24) and the same `language` value.

## Timezone

All timestamps (`ts`) are UTC. When presenting time to the user, convert to their local timezone if known, otherwise present as UTC.

## Translation rule

Never translate the report text yourself. The `language` parameter instructs the backend to return the correct language version. Output the `ai_analysis.free_text` field exactly as received.

## Tool reference

- `mcp__plugin_btc-orderflow-mcp_btc__get_btc_report(language: str = "en")` — returns JSON string with: `coin`, `ts`, `price_at_diag`, `direction` (bull/bear), `ai_analysis`
- `mcp__plugin_btc-orderflow-mcp_btc__get_report_history(hours: int, language: str = "en")` — returns JSON array of report objects, newest first

## Usage

Triggered by `/btc-orderflow-mcp:btc-report` or automatically when user asks about BTC market conditions.
