# Setup Guide for MCP Unified Coding Agent

This guide provides detailed instructions on how to set up and run the MCP Unified Coding Agent.

## 1. Prerequisites

Before you begin, ensure you have the following installed:

*   **Python 3.9+**: Download and install from [python.org](https://www.python.org/downloads/).
*   **pip**: Python's package installer, usually comes with Python.
*   **git**: For cloning the repository. Download from [git-scm.com](https://git-scm.com/downloads).
*   **Node.js and npm/npx**: Required for running some MCP server commands (e.g., GitHub, Supabase, Neon, Vercel MCP servers are often Node.js based). Download from [nodejs.org](https://nodejs.org/en/download/).

## 2. Installation

1.  **Clone the repository**:
    Open your terminal or command prompt and run:
    ```bash
    git clone https://github.com/your-username/mcp-coding-agent.git
    cd mcp-coding-agent
    ```

2.  **Install Python dependencies**:
    Navigate to the cloned directory and install the required Python packages:
    ```bash
    pip install mcp pydantic requests
    ```

## 3. Configuration

The agent requires API keys and credentials for interacting with GitHub, Supabase, Neon, and Vercel. These should be stored as environment variables for security.

1.  **Create a `.env` file**:
    In the root directory of the `mcp-coding-agent` project, create a file named `.env`.

2.  **Add your credentials**:
    Populate the `.env` file with your API keys and connection strings. Replace the placeholder values with your actual credentials.

    ```dotenv
    GITHUB_TOKEN="your_github_personal_access_token"
    SUPABASE_API_KEY="your_supabase_anon_key"
    SUPABASE_URL="your_supabase_project_url"
    NEON_API_KEY="your_neon_api_key"
    VERCEL_API_TOKEN="your_vercel_api_token"
    ```

    *   **GitHub Token**: Generate a personal access token with appropriate `repo` and `workflow` scopes from your [GitHub Developer Settings](https://github.com/settings/tokens).
    *   **Supabase API Key & URL**: Find these in your Supabase project settings under "API".
    *   **Neon API Key**: Obtain this from your Neon dashboard.
    *   **Vercel API Token**: Generate an API token from your [Vercel Account Settings](https://vercel.com/account/tokens).

## 4. Running the Agent

To run the demo workflow, execute the `main.py` script:

```bash
python main.py
```

This will simulate a full-stack development workflow, including:

*   Connecting to MCP servers (simulated).
*   Creating a GitHub repository.
*   Provisioning a Neon PostgreSQL database.
*   Applying a database schema via Supabase MCP.
*   Deploying the application to Vercel.

## 5. Extending the Agent

### Adding New MCP Connectors

To integrate a new service that supports the Model Context Protocol:

1.  **Identify the MCP Server command**: Most MCP servers are available as `npm` packages. For example, `@newservice/mcp-server`.
2.  **Update `core/agent.py`**: In the `initialize_connectors` method, add an entry for your new service with its corresponding `npx` command.
    ```python
    connectors = {
        # ... existing connectors
        "newservice": ["npx", "-y", "@newservice/mcp-server"]
    }
    ```
3.  **Implement workflow logic**: In `core/agent.py`, add new methods or extend `run_full_stack_workflow` to utilize the tools exposed by your new MCP server.

### Developing Custom Tools

The agent is designed to be extensible. You can create your own custom tools and expose them via a local MCP server. Refer to the [Model Context Protocol documentation](https://modelcontextprotocol.io/docs/develop/build-server) for guidance on building custom MCP servers.

## 6. Troubleshooting

*   **`mcp` package not found**: Ensure you have run `pip install mcp pydantic requests`.
*   **API Key issues**: Double-check your `.env` file for correct API keys and ensure they have the necessary permissions.
*   **MCP Server connection errors**: Verify that the `npx` commands for the MCP servers are correct and that Node.js is properly installed.
