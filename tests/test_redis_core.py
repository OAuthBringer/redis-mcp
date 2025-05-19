"""
Tests for Redis core operations.
"""

import pytest
from fastmcp import Client

from redis_mcp.redis_core import redis_core


@pytest.mark.asyncio
async def test_redis_get():
    """Test the redis_get operation."""
    async with Client(redis_core) as client:
        with pytest.raises(NotImplementedError):
            await client.call_tool("redis_get", {"key": "test_key"})


@pytest.mark.asyncio
async def test_redis_set():
    """Test the redis_set operation."""
    async with Client(redis_core) as client:
        with pytest.raises(NotImplementedError):
            await client.call_tool("redis_set", {"key": "test_key", "value": "test_value"})


@pytest.mark.asyncio
async def test_redis_delete():
    """Test the redis_delete operation."""
    async with Client(redis_core) as client:
        with pytest.raises(NotImplementedError):
            await client.call_tool("redis_delete", {"keys": "test_key"})


@pytest.mark.asyncio
async def test_redis_list():
    """Test the redis_list operation."""
    async with Client(redis_core) as client:
        with pytest.raises(NotImplementedError):
            await client.call_tool("redis_list", {"pattern": "*"})
