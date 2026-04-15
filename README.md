# btc-orderflow-mcp

Real-time BTC order flow analysis as a Claude plugin — powered by MacroAgent.

## Install as Claude Plugin

### Step 0 — Install uv (if not already installed)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

`uv` is required to run the MCP server. Restart your terminal after installing.

### Step 1 — Add the MacroAgent marketplace

```bash
claude plugin marketplace add MacroAgent/macroagent-marketplace
```

### Step 2 — Install the plugin

```bash
claude plugin install btc-orderflow-mcp@macroagent-marketplace
```

### Step 3 — Set your API key (persistent)

```bash
echo 'export BTC_MCP_API_URL="https://macroagent.ai"' >> ~/.zshrc
echo 'export BTC_MCP_API_KEY="your-api-key-here"' >> ~/.zshrc
source ~/.zshrc
```

> Bash users: replace `~/.zshrc` with `~/.bashrc`.

### Step 4 — Restart Claude and use it

Type `/btc-orderflow-mcp:btc-report` in any Claude session, or ask naturally:

> "What's the current BTC market condition?"

Claude will automatically invoke the skill.

---

## Get an API Key

Contact [@trader_jessepan](https://t.me/trader_jessepan) on Telegram.

---

## Available Tools

Once installed, Claude has access to two MCP tools:

### `mcp__btc__get_btc_report`

Returns the latest hourly BTC market analysis. No parameters.

Example response:
```json
{
  "id": "3f2a1b...",
  "coin": "BTC",
  "ts": 1712000000,
  "price_at_diag": 67500.0,
  "direction": "bull",
  "ai_analysis": { "direction_score": 7, "summary": "..." },
  "model_used": "claude-opus-4-6",
  "created_at": 1712000000
}
```

### `mcp__btc__get_report_history`

Returns BTC analysis reports from the past N hours.

| Parameter | Type | Default | Range |
|-----------|------|---------|-------|
| `hours` | integer | 24 | 1–168 |

---

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `BTC_MCP_API_URL` | Yes | `https://macroagent.ai` |
| `BTC_MCP_API_KEY` | Yes | API key received after purchase |

---

## Development

```bash
git clone https://github.com/MacroAgent/btc-orderflow-mcp.git && cd btc-orderflow-mcp
pip install -e .
BTC_MCP_API_URL=http://localhost:5001 BTC_MCP_API_KEY=dev-key btc-mcp
```
