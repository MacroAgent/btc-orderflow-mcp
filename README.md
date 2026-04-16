# btc-orderflow-mcp

> Real-time Bitcoin order flow analysis for Claude — powered by [MacroAgent](https://macroagent.ai)

[![MCP Compatible](https://img.shields.io/badge/MCP-Compatible-blueviolet)](https://modelcontextprotocol.io)
[![Claude Skill](https://img.shields.io/badge/Skill-%2Fbtc--report-orange)](https://github.com/MacroAgent/macroagent-marketplace)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

<!-- Demo GIF: record 20s of typing /btc-report in Claude Code → full report appears -->
![Demo](assets/demo.gif)

---

## What is Order Flow?

Most traders watch price. Order flow traders watch **who is actually buying and selling** — and how aggressively.

`btc-orderflow-mcp` brings professional-grade order flow data directly into your Claude conversations:

- **CVD (Cumulative Volume Delta)** — net buying vs selling pressure across timeframes
- **OI (Open Interest)** — whether new money is entering or leaving the market
- **Liquidations** — where forced selling/buying is happening
- **ETF flows** — institutional demand signals
- **Macro context** — DXY, rates, equity correlation

Hourly reports. Bilingual (EN/中文). Analyst-grade, not noise.

---

## Two Ways to Use

| Mode | How | Best for |
|------|-----|---------|
| **`/btc-orderflow-mcp:btc-report` Skill** | Type the command in Claude Code | Quick one-click report |
| **Natural language** | Ask Claude directly | Custom questions & analysis |

---

## Installation

### Prerequisites

Requires [`uv`](https://docs.astral.sh/uv/) — the MCP server runs via `uvx` automatically.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

### Step 1 — Get an API Key

**[→ Get your API key ($30)](https://macroagentbtc.lemonsqueezy.com/checkout/buy/e2809e37-9007-48d9-8b2f-5ab312c3be60)**

| Tier | Reports | History | Price |
|------|---------|---------|-------|
| Free Trial | Latest report only | — | Free |
| Pro | Unlimited | 7 days | $30 |

---

### Step 2 — Set your API credentials

Add to your shell profile so the key persists across restarts:

```bash
echo 'export BTC_MCP_API_URL="https://macroagent.ai"' >> ~/.zshrc
echo 'export BTC_MCP_API_KEY="your-api-key-here"' >> ~/.zshrc
source ~/.zshrc
```

> Using bash? Replace `~/.zshrc` with `~/.bash_profile`

---

### Step 3 — Install via Claude plugin

```bash
# Add MacroAgent marketplace
claude plugin marketplace add MacroAgent/macroagent-marketplace

# Install the plugin (includes MCP server + /btc-report skill)
claude plugin install btc-orderflow-mcp@macroagent-marketplace
```

Restart Claude. Done.

---

## Usage

**One-command report:**
```
/btc-orderflow-mcp:btc-report
```

**Or ask naturally:**
```
What's the current BTC order flow telling us?
Is this a short squeeze or real buying?
How has order flow changed over the past 12 hours?
```

---

## Example Conversations

**Market diagnosis:**
```
You: /btc-orderflow-mcp:btc-report

Claude: [calls get_btc_report()]
Direction: Bullish (+4/5)

7-day CVD +$4.5B, 5 of 7 days positive. OI expanded +9.97% on the move —
new longs entering at $74k, not a short squeeze. Key risk: 1H momentum
fading. Structure holds above VAH $72,959.
```

**Historical context:**
```
You: How has order flow evolved over the past 24 hours?

Claude: [calls get_report_history(24)]
Asian session drove all of yesterday's buying (+$2B CVD).
London and NY sessions flat — Western buyers have not confirmed yet.
Watch for continuation or fade at London open.
```

---

## Why Claude?

Order flow data is only useful if you can **ask questions about it**. Claude understands market context, remembers your trading style, and connects signals to actionable decisions — something a dashboard alone can't do.

---

## Roadmap

- [ ] ETH order flow support
- [ ] Alert system (Claude notifies you when key signals trigger)
- [ ] XAU (Gold) and macro asset coverage
- [ ] Strategy backtesting via historical data

---

## License

MIT — client code is open source. Backend data service requires API subscription.

---

*Built on [Model Context Protocol](https://modelcontextprotocol.io) · Data by [MacroAgent](https://macroagent.ai)*
