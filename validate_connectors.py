import asyncio
import os
from core.mcp_client import MCPClientManager

async def validate():
    """
    Validates that all MCP servers are correctly installed and accessible.
    This script runs real npx commands to verify connectivity.
    """
    manager = MCPClientManager()
    connectors = {
        "github": ["-y", "@modelcontextprotocol/server-github"],
        "supabase": ["-y", "@supabase/mcp-server"],
        "neon": ["-y", "@neondatabase/mcp-server"],
        "vercel": ["-y", "@vercel/mcp-server"]
    }

    print("🔍 Validating MCP Connectors...")
    
    for name, args in connectors.items():
        try:
            print(f"Testing {name}...")
            async with manager.get_server_session(name, "npx", args) as session:
                tools = await manager.list_tools(session)
                print(f"✅ {name} is LIVE. Found {len(tools)} tools.")
                # Print first 3 tools for verification
                for tool in tools[:3]:
                    print(f"  - {tool.name}")
        except Exception as e:
            print(f"❌ {name} FAILED: {str(e)}")

if __name__ == "__main__":
    asyncio.run(validate())
