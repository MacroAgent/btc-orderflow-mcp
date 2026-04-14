"""Tests for btc_mcp.server tool functions.

Tool functions are plain Python callables — they can be called directly
without spinning up the MCP server runtime.
"""
import os
import pytest
from unittest.mock import patch, MagicMock

# Set env vars before importing the module so _API_URL and _API_KEY are set
os.environ.setdefault("BTC_MCP_API_URL", "http://localhost:5001")
os.environ.setdefault("BTC_MCP_API_KEY", "test-key")

import btc_mcp.server as srv


def _mock_response(text: str) -> MagicMock:
    m = MagicMock()
    m.raise_for_status.return_value = None
    m.text = text
    return m


# ── get_btc_report ────────────────────────────────────────────────────────────

def test_get_btc_report_returns_string():
    mock = _mock_response('{"id":"d1","coin":"BTC","ts":1700000000}')
    with patch("btc_mcp.server.httpx.get", return_value=mock):
        result = srv.get_btc_report()
    assert isinstance(result, str)
    assert "BTC" in result


def test_get_btc_report_calls_correct_url():
    mock = _mock_response('{"coin":"BTC"}')
    with patch("btc_mcp.server.httpx.get", return_value=mock) as mock_get:
        srv.get_btc_report()
    url = mock_get.call_args.args[0]
    assert url.endswith("/report/latest")


def test_get_btc_report_sends_bearer_header():
    mock = _mock_response('{"coin":"BTC"}')
    with patch("btc_mcp.server.httpx.get", return_value=mock) as mock_get:
        srv.get_btc_report()
    headers = mock_get.call_args.kwargs["headers"]
    assert headers["Authorization"].startswith("Bearer ")


# ── get_report_history ────────────────────────────────────────────────────────

def test_get_report_history_returns_string():
    mock = _mock_response('[{"coin":"BTC"}]')
    with patch("btc_mcp.server.httpx.get", return_value=mock):
        result = srv.get_report_history()
    assert isinstance(result, str)


def test_get_report_history_default_24h():
    mock = _mock_response('[]')
    with patch("btc_mcp.server.httpx.get", return_value=mock) as mock_get:
        srv.get_report_history()
    assert mock_get.call_args.kwargs["params"]["hours"] == 24


def test_get_report_history_custom_hours():
    mock = _mock_response('[]')
    with patch("btc_mcp.server.httpx.get", return_value=mock) as mock_get:
        srv.get_report_history(hours=48)
    assert mock_get.call_args.kwargs["params"]["hours"] == 48


def test_get_report_history_clamps_to_max_168():
    mock = _mock_response('[]')
    with patch("btc_mcp.server.httpx.get", return_value=mock) as mock_get:
        srv.get_report_history(hours=9999)
    assert mock_get.call_args.kwargs["params"]["hours"] == 168


def test_get_report_history_clamps_to_min_1():
    mock = _mock_response('[]')
    with patch("btc_mcp.server.httpx.get", return_value=mock) as mock_get:
        srv.get_report_history(hours=0)
    assert mock_get.call_args.kwargs["params"]["hours"] == 1


def test_get_report_history_calls_correct_url():
    mock = _mock_response('[]')
    with patch("btc_mcp.server.httpx.get", return_value=mock) as mock_get:
        srv.get_report_history(hours=24)
    url = mock_get.call_args.args[0]
    assert url.endswith("/report/history")
