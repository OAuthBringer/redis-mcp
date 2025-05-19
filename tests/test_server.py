"""
Tests for the main server.
"""

import pytest
from fastmcp import Client

from redis_mcp.server import mcp


@pytest.mark.asyncio
async def test_server_info():
    """Test the server_info operation."""
    async with Client(mcp) as client:
        result = await client.call_tool("server_info", {})
        assert result[0].text is not None
        data = eval(result[0].text)  # Convert string representation to dict
        assert isinstance(data, dict)
        assert data["name"] == "Redis MCP Server"
        assert data["version"] == "0.1.0"
        assert "redis_operations" in data["components"]
        assert "task_management" in data["components"]
        assert "stdio" in data["transports"]
        assert "sse" in data["transports"]


@pytest.mark.asyncio
async def test_mounted_redis_get():
    """Test the mounted redis_get operation."""
    async with Client(mcp) as client:
        with pytest.raises(NotImplementedError):
            await client.call_tool("redis_redis_get", {"key": "test_key"})


@pytest.mark.asyncio
async def test_mounted_create_project():
    """Test the mounted create_project operation."""
    async with Client(mcp) as client:
        with pytest.raises(NotImplementedError):
            await client.call_tool(
                "task_create_project", 
                {
                    "project_id": "test_project", 
                    "title": "Test Project", 
                    "description": "A test project"
                }
            )
