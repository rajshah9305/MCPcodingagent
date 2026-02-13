import asyncio
from core.agent import CodingAgent

async def main():
    print("--- MCP Unified Coding Agent v1.0 ---")
    agent = CodingAgent()
    
    # In a real environment, this would start the MCP servers
    await agent.initialize_connectors()
    
    # Run a sample full-stack workflow
    try:
        status = await agent.run_full_stack_workflow("mcp-demo-app")
        print(f"\nStatus: {status}")
    except Exception as e:
        print(f"Error during workflow: {e}")

if __name__ == "__main__":
    asyncio.run(main())
