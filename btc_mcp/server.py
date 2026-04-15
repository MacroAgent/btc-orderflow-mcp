"""MCP Server — BTC market analysis reports from MacroAgent.

Tools:
  get_btc_report()             → latest report (string JSON)
  get_report_history(hours=24) → array of reports (string JSON)

Env vars required at startup:
  BTC_MCP_API_URL   base URL of MacroAgent backend (no trailing slash)
  BTC_MCP_API_KEY   Bearer token issued by the backend operator
"""
import json
import os
import httpx
from mcp.server.fastmcp import FastMCP

_API_URL = os.environ.get("BTC_MCP_API_URL", "").rstrip("/")
_API_KEY  = os.environ.get("BTC_MCP_API_KEY", "")

_KEEP = {"coin", "ts", "price_at_diag", "direction", "ai_analysis"}

mcp = FastMCP("btc-report")


def _strip(obj: dict) -> dict:
    """Remove internal metadata fields before returning to client."""
    return {k: v for k, v in obj.items() if k in _KEEP}


@mcp.tool()
def get_btc_report() -> str:
    """Retrieve the latest BTC market analysis report from MacroAgent.

    Returns a JSON string with: coin, ts, price_at_diag, direction, ai_analysis.
    """
    headers = {"Authorization": f"Bearer {_API_KEY}"}
    r = httpx.get(f"{_API_URL}/report/latest", headers=headers, timeout=30)
    r.raise_for_status()
    return json.dumps(_strip(r.json()))


@mcp.tool()
def get_report_history(hours: int = 24) -> str:
    """Retrieve BTC market analysis reports from the past N hours.

    Args:
        hours: Look-back window in hours (1-168, default 24).

    Returns a JSON array of report objects ordered newest-first.
    Each object contains: coin, ts, price_at_diag, direction, ai_analysis.
    """
    hours = max(1, min(168, hours))
    headers = {"Authorization": f"Bearer {_API_KEY}"}
    r = httpx.get(
        f"{_API_URL}/report/history",
        headers=headers,
        params={"hours": hours},
        timeout=30,
    )
    r.raise_for_status()
    return json.dumps([_strip(item) for item in r.json()])


def run() -> None:
    """Entry point for the btc-mcp command."""
    mcp.run()
