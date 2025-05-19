"""
Main Redis MCP Server that combines Redis operations and task management.

This module mounts the Redis core operations and task management servers
to provide a unified interface with SSE support.
"""

import asyncio
from typing import Optional

from fastmcp import FastMCP

from . import redis_core, task_management


# Create main server
mcp = FastMCP("Redis MCP Server")

# Mount sub-servers
mcp.mount("redis", redis_core.redis_core)
mcp.mount("task", task_management.task_management)


@mcp.tool()
async def server_info() -> dict:
    """
    Get information about the Redis MCP server.

    Returns:
        Dictionary with server information
    """
    return {
        "name": "Redis MCP Server",
        "version": "0.1.0",
        "components": ["redis_operations", "task_management"],
        "transports": ["stdio", "sse"],
    }


def main(host: Optional[str] = None, port: Optional[int] = None) -> None:
    """
    Run the Redis MCP server.

    Args:
        host: Host to bind to for SSE transport (default: localhost)
        port: Port to bind to for SSE transport (default: 8000)
    """
    if host and port:
        # Start with SSE transport
        mcp.run(transport="sse", host=host, port=port)
    else:
        # Start with default STDIO transport
        mcp.run()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Redis MCP Server")
    parser.add_argument("--host", help="Host to bind to for SSE transport")
    parser.add_argument("--port", type=int, help="Port to bind to for SSE transport")
    args = parser.parse_args()

    main(host=args.host, port=args.port)
