# btc-mcp

MCP Server that exposes BTC market analysis reports from MacroAgent as Claude tools.

## Installation

```bash
pip install btc-mcp
```

## Claude Desktop Configuration

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`
(macOS) or `%APPDATA%\Claude\claude_desktop_config.json` (Windows):

```json
{
  "mcpServers": {
    "btc": {
      "command": "btc-mcp",
      "env": {
        "BTC_MCP_API_URL": "https://your-domain.com",
        "BTC_MCP_API_KEY": "your-api-key"
      }
    }
  }
}
```

Restart Claude Desktop after saving.

## Available Tools

### `get_btc_report`

Returns the latest BTC market analysis report. No parameters required.

Example response (as JSON string):
```json
{
  "id": "3f2a1b...",
  "coin": "BTC",
  "ts": 1712000000,
  "price_at_diag": 67500.0,
  "direction": "bull",
  "ai_analysis": {
    "direction_score": 7,
    "summary": "..."
  },
  "model_used": "claude-opus-4-6",
  "created_at": 1712000000
}
```

### `get_report_history`

Returns BTC analysis reports from the past N hours.

| Parameter | Type | Default | Range |
|-----------|------|---------|-------|
| `hours` | integer | 24 | 1–168 |

Returns a JSON array of report objects (same schema as above).

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `BTC_MCP_API_URL` | Yes | MacroAgent backend base URL (no trailing slash) |
| `BTC_MCP_API_KEY` | Yes | Bearer token set in `REPORT_API_KEYS` on the server |

## Development

```bash
git clone <this-repo> btc-mcp && cd btc-mcp
pip install -e .
BTC_MCP_API_URL=http://localhost:5001 BTC_MCP_API_KEY=your-key btc-mcp
```
