# Production Setup Guide: MCP Unified Coding Agent

This guide ensures your agent is wired up with **real** services and **no mocks**.

## 1. Security & Environment Variables

The agent uses real API tokens. **Never commit your `.env` file.**

### Required Tokens
| Variable | Purpose | Where to Get |
| :--- | :--- | :--- |
| `GITHUB_PERSONAL_ACCESS_TOKEN` | Manage Repos & PRs | [GitHub Settings](https://github.com/settings/tokens) |
| `NEON_API_KEY` | Provision Databases | [Neon Console](https://console.neon.tech/app/settings/profile) |
| `VERCEL_TOKEN` | Deploy Applications | [Vercel Tokens](https://vercel.com/account/tokens) |
| `SUPABASE_URL` | DB Management | Supabase Project Settings |
| `SUPABASE_SERVICE_ROLE_KEY` | Admin DB Access | Supabase Project Settings |

## 2. Real-World Wiring

The agent communicates with these services via the **Model Context Protocol (MCP)** using `stdio` transport. It launches real server processes using `npx`.

### Verification
Run the validation script to ensure your environment can launch the MCP servers and discover their tools:
```bash
python validate_connectors.py
```

## 3. Implementation Details

- **`core/mcp_client.py`**: Uses the official `mcp` Python SDK. It manages the lifecycle of the `npx` subprocesses and handles the JSON-RPC communication.
- **`core/agent.py`**: Contains the orchestration logic. It passes real data (like Neon connection strings) between different MCP tools (like Vercel environment variable creation).
- **`main.py`**: The execution engine that triggers the multi-service workflow.

## 4. Running the Agent

1. **Install official MCP SDK**:
   ```bash
   pip install mcp pydantic requests python-dotenv
   ```
2. **Set your environment variables**:
   ```bash
   export GITHUB_PERSONAL_ACCESS_TOKEN="your_token"
   # ... set others
   ```
3. **Execute**:
   ```bash
   python main.py
   ```

The agent will then:
1. Launch the GitHub MCP server and create a repo.
2. Launch the Neon MCP server and provision a Postgres instance.
3. Launch the Supabase MCP server and apply migrations to the Neon instance.
4. Launch the Vercel MCP server, create a project, and wire up the Neon DB URL.
