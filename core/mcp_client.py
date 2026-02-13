import asyncio
import os
from contextlib import asynccontextmanager
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from typing import Dict, List, Any, Optional

class MCPClientManager:
    """
    Manages multiple MCP server connections with real lifecycle management.
    Ensures no mocks or fallbacks are used.
    """
    def __init__(self):
        self.sessions: Dict[str, ClientSession] = {}
        self.exit_stack = {}

    @asynccontextmanager
    async def get_server_session(self, name: str, command: str, args: List[str], env: Optional[Dict[str, str]] = None):
        """
        Connects to an MCP server and yields a session.
        Handles real process management via stdio.
        """
        # Merge system env with provided env
        full_env = os.environ.copy()
        if env:
            full_env.update(env)

        server_params = StdioServerParameters(
            command=command,
            args=args,
            env=full_env
        )
        
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                self.sessions[name] = session
                try:
                    yield session
                finally:
                    del self.sessions[name]

    async def list_tools(self, session: ClientSession) -> List[Any]:
        """Real tool discovery from the MCP server."""
        response = await session.list_tools()
        return response.tools

    async def execute_tool(self, session: ClientSession, tool_name: str, arguments: Dict[str, Any]) -> Any:
        """Real tool execution on the MCP server."""
        return await session.call_tool(tool_name, arguments)

class UnifiedContext:
    """Maintains real state across different services."""
    def __init__(self):
        self.state = {
            "github": {},
            "supabase": {},
            "neon": {},
            "vercel": {}
        }

    def update(self, service: str, data: Dict[str, Any]):
        self.state[service].update(data)

    def get(self, service: str, key: str):
        return self.state[service].get(key)
