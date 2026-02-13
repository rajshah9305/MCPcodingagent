# 🚀 MCP Unified Coding Agent

An advanced, open-source coding agent that leverages the **Model Context Protocol (MCP)** to provide a unified control plane for modern full-stack development.

## 🌟 What Makes This Stand Out?

Most coding agents focus on writing code within an IDE. The **MCP Unified Coding Agent** goes beyond the editor to orchestrate your entire cloud infrastructure:

1.  **Cross-Service Orchestration**: It doesn't just write code; it links services. It can create a GitHub repo, provision a Neon database, sync the connection string to Vercel, and trigger a deployment in one go.
2.  **Infrastructure-as-Code (IaC) Intelligence**: Using the Supabase and Neon MCPs, the agent understands your database schema and can suggest migrations based on your frontend changes.
3.  **Unified Context**: The agent maintains a "global project state," understanding how your Vercel frontend, GitHub CI/CD, and Supabase backend interact.
4.  **Zero-Config Connectors**: Pre-configured with the best-of-breed open-source and free-tier friendly services (GitHub, Neon, Supabase, Vercel).

## 🛠️ Integrated MCP Connectors

This agent comes with built-in support for:

| Service | MCP Connector | Key Capabilities |
| :--- | :--- | :--- |
| **GitHub** | `@modelcontextprotocol/server-github` | Repo management, PRs, Issues, Projects |
| **Supabase** | `@supabase/mcp-server` | Schema design, migrations, data management |
| **Neon** | `@neondatabase/mcp-server` | Serverless Postgres, branching, scaling |
| **Vercel** | `@vercel/mcp-server` | Deployments, env vars, team management |

## 🏗️ Architecture

The agent is built on a modular Python core using the official MCP SDK.

- **`core/mcp_client.py`**: Handles the protocol handshake and tool execution for any stdio-based MCP server.
- **`core/agent.py`**: The "brain" that orchestrates multi-step workflows across different services.
- **`connectors/`**: Configuration and adapter logic for specific service APIs.

## 🚀 Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/mcp-coding-agent.git
   cd mcp-coding-agent
   ```

2. **Install dependencies**:
   ```bash
   pip install mcp pydantic requests
   ```

3. **Configure your API keys**:
   Create a `.env` file with your credentials for GitHub, Supabase, Neon, and Vercel.

4. **Run the demo**:
   ```bash
   python main.py
   ```

## 🧩 Adding New Connectors

Adding a new service is as simple as adding its MCP server command to the `agent.py` initialization logic. Any service that supports the Model Context Protocol can be integrated instantly.

## 📄 License

Open-source under the MIT License.
