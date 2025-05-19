"""
Core Redis operations for the Redis MCP Server.

This module provides a FastMCP-compatible interface for basic Redis operations.
"""

from typing import Any, Dict, List, Optional, Union

import redis
from fastmcp import FastMCP

# Create Redis core operations server
redis_core = FastMCP("Redis Core Operations")


@redis_core.tool()
async def redis_get(key: str) -> Optional[str]:
    """
    Get the value of a key from Redis.

    Args:
        key: The Redis key to retrieve

    Returns:
        The value of the key, or None if the key does not exist
    """
    # This is a placeholder that will be implemented later
    # We're creating failing tests first, as per task requirements
    raise NotImplementedError("redis_get is not yet implemented")


@redis_core.tool()
async def redis_set(
    key: str, value: str, ex: Optional[int] = None, nx: bool = False, xx: bool = False
) -> bool:
    """
    Set the value of a key in Redis.

    Args:
        key: The Redis key to set
        value: The value to set
        ex: Expiry time in seconds
        nx: Only set if the key does not exist
        xx: Only set if the key already exists

    Returns:
        True if the operation was successful, False otherwise
    """
    # This is a placeholder that will be implemented later
    raise NotImplementedError("redis_set is not yet implemented")


@redis_core.tool()
async def redis_delete(keys: Union[str, List[str]]) -> int:
    """
    Delete one or more keys from Redis.

    Args:
        keys: The key or list of keys to delete

    Returns:
        The number of keys that were deleted
    """
    # This is a placeholder that will be implemented later
    raise NotImplementedError("redis_delete is not yet implemented")


@redis_core.tool()
async def redis_list(pattern: str = "*") -> List[str]:
    """
    List keys in Redis matching a pattern.

    Args:
        pattern: Pattern to match keys (default: "*")

    Returns:
        List of keys matching the pattern
    """
    # This is a placeholder that will be implemented later
    raise NotImplementedError("redis_list is not yet implemented")
