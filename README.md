# btc-mcp

MCP Server for BTC market analysis reports via MacroAgent.

## Tools

- `get_btc_report()` — latest BTC diagnosis report
- `get_report_history(hours=24)` — historical reports for the past N hours

## Configuration

Set environment variables before running:

```
BTC_MCP_API_URL=https://macroagent.ai
BTC_MCP_API_KEY=your-bearer-token
```

## Usage

```bash
btc-mcp
```
