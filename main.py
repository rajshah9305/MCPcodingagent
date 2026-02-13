import asyncio
import os
import sys
from core.agent import ProductionCodingAgent

async def main():
    """
    Production entry point for the MCP Unified Coding Agent.
    Requires real environment variables to be set.
    """
    print("==========================================")
    print("   MCP UNIFIED CODING AGENT (PROD)        ")
    print("==========================================")
    
    # Check for .env file or existing environment variables
    # In a real setup, we'd use python-dotenv here
    required_services = ["GITHUB_PERSONAL_ACCESS_TOKEN", "NEON_API_KEY", "VERCEL_TOKEN"]
    missing = [v for v in required_services if not os.getenv(v)]
    
    if missing:
        print(f"❌ Error: Missing critical environment variables: {', '.join(missing)}")
        print("Please set these in your environment before running.")
        sys.exit(1)

    agent = ProductionCodingAgent()
    
    try:
        # Example: Deploy a new microservice
        project_name = "mcp-prod-service-" + os.urandom(2).hex()
        result = await agent.orchestrate_full_stack(
            repo_name=project_name,
            db_name=project_name + "-db"
        )
        
        print("\n--- Final Project State ---")
        for service, data in result.items():
            print(f"{service.upper()}: {data}")
            
    except Exception as e:
        print(f"\n❌ Orchestration Failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
