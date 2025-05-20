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
async def test_redis_get_implemented():
    """Test the redis_get operation when implemented."""
    # This test will be skipped until the implementation is ready
    pytest.skip("Implementation not ready")
    
    async with Client(redis_core) as client:
        # Test getting a non-existent key
        result = await client.call_tool("redis_get", {"key": "nonexistent_key"})
        assert result[0].text is None or result[0].text == "None", "Non-existent key should return None"
        
        # Test setting and getting a key
        await client.call_tool("redis_set", {"key": "test_get_key", "value": "test_value"})
        result = await client.call_tool("redis_get", {"key": "test_get_key"})
        assert result[0].text == "test_value", "Should return the correct value"
        
        # Test getting a key with expiry that hasn't expired
        await client.call_tool("redis_set", {"key": "test_get_ex_key", "value": "test_value", "ex": 10})
        result = await client.call_tool("redis_get", {"key": "test_get_ex_key"})
        assert result[0].text == "test_value", "Should return value before expiry"


@pytest.mark.asyncio
async def test_redis_set():
    """Test the redis_set operation."""
    async with Client(redis_core) as client:
        with pytest.raises(NotImplementedError):
            await client.call_tool("redis_set", {"key": "test_key", "value": "test_value"})


@pytest.mark.asyncio
async def test_redis_set_implemented():
    """Test the redis_set operation when implemented."""
    # This test will be skipped until the implementation is ready
    pytest.skip("Implementation not ready")
    
    async with Client(redis_core) as client:
        # Test basic set
        result = await client.call_tool("redis_set", {"key": "test_set_key", "value": "test_value"})
        assert result[0].text == "True", "Basic set should return True"
        
        # Test set with NX option (key doesn't exist)
        result = await client.call_tool("redis_set", {
            "key": "test_set_nx_key", 
            "value": "test_value", 
            "nx": True
        })
        assert result[0].text == "True", "NX set on non-existent key should return True"
        
        # Test set with NX option (key exists)
        await client.call_tool("redis_set", {"key": "test_set_nx_exists", "value": "original"})
        result = await client.call_tool("redis_set", {
            "key": "test_set_nx_exists", 
            "value": "updated", 
            "nx": True
        })
        assert result[0].text == "False", "NX set on existing key should return False"
        
        # Test set with XX option (key exists)
        await client.call_tool("redis_set", {"key": "test_set_xx_exists", "value": "original"})
        result = await client.call_tool("redis_set", {
            "key": "test_set_xx_exists", 
            "value": "updated", 
            "xx": True
        })
        assert result[0].text == "True", "XX set on existing key should return True"
        
        # Test set with XX option (key doesn't exist)
        result = await client.call_tool("redis_set", {
            "key": "test_set_xx_nonexistent", 
            "value": "test_value", 
            "xx": True
        })
        assert result[0].text == "False", "XX set on non-existent key should return False"


@pytest.mark.asyncio
async def test_redis_delete():
    """Test the redis_delete operation."""
    async with Client(redis_core) as client:
        with pytest.raises(NotImplementedError):
            await client.call_tool("redis_delete", {"keys": "test_key"})


@pytest.mark.asyncio
async def test_redis_delete_implemented():
    """Test the redis_delete operation when implemented."""
    # This test will be skipped until the implementation is ready
    pytest.skip("Implementation not ready")
    
    async with Client(redis_core) as client:
        # Test deleting a non-existent key
        result = await client.call_tool("redis_delete", {"keys": "nonexistent_key"})
        assert result[0].text == "0", "Deleting non-existent key should return 0"
        
        # Test deleting a single key
        await client.call_tool("redis_set", {"key": "test_delete_key", "value": "test_value"})
        result = await client.call_tool("redis_delete", {"keys": "test_delete_key"})
        assert result[0].text == "1", "Deleting single key should return 1"
        
        # Test deleting multiple keys
        await client.call_tool("redis_set", {"key": "test_delete_key1", "value": "test_value1"})
        await client.call_tool("redis_set", {"key": "test_delete_key2", "value": "test_value2"})
        result = await client.call_tool("redis_delete", {"keys": ["test_delete_key1", "test_delete_key2"]})
        assert result[0].text == "2", "Deleting two keys should return 2"
        
        # Test deleting a mix of existing and non-existent keys
        await client.call_tool("redis_set", {"key": "test_delete_key3", "value": "test_value3"})
        result = await client.call_tool("redis_delete", {"keys": ["test_delete_key3", "nonexistent_key"]})
        assert result[0].text == "1", "Deleting mix of keys should return count of existing keys"


@pytest.mark.asyncio
async def test_redis_list():
    """Test the redis_list operation."""
    async with Client(redis_core) as client:
        with pytest.raises(NotImplementedError):
            await client.call_tool("redis_list", {"pattern": "*"})


@pytest.mark.asyncio
async def test_redis_list_implemented():
    """Test the redis_list operation when implemented."""
    # This test will be skipped until the implementation is ready
    pytest.skip("Implementation not ready")
    
    async with Client(redis_core) as client:
        # Clean up any existing test keys
        existing_keys = await client.call_tool("redis_list", {"pattern": "test_list_*"})
        if existing_keys[0].text and existing_keys[0].text != "[]":
            keys = eval(existing_keys[0].text)
            await client.call_tool("redis_delete", {"keys": keys})
        
        # Test listing with no matching keys
        result = await client.call_tool("redis_list", {"pattern": "test_list_nonexistent_*"})
        assert result[0].text == "[]", "No matching keys should return empty list"
        
        # Test listing with matching keys
        await client.call_tool("redis_set", {"key": "test_list_key1", "value": "value1"})
        await client.call_tool("redis_set", {"key": "test_list_key2", "value": "value2"})
        result = await client.call_tool("redis_list", {"pattern": "test_list_*"})
        result_list = eval(result[0].text)
        assert isinstance(result_list, list), "Result should be a list"
        assert len(result_list) == 2, "Should find 2 keys"
        assert "test_list_key1" in result_list, "Should contain first key"
        assert "test_list_key2" in result_list, "Should contain second key"
        
        # Test listing with specific pattern
        await client.call_tool("redis_set", {"key": "test_list_abc", "value": "abc"})
        await client.call_tool("redis_set", {"key": "test_list_def", "value": "def"})
        result = await client.call_tool("redis_list", {"pattern": "test_list_a*"})
        result_list = eval(result[0].text)
        assert len(result_list) == 1, "Pattern should match 1 key"
        assert "test_list_abc" in result_list, "Should contain matching key"
