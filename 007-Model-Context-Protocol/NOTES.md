# Model Context Protocol (MCP) Notes

## What is MCP?

MCP (Model Context Protocol) is a standardized protocol that allows AI models to interact with external tools, resources, and prompts through a client-server architecture. It decouples the AI application from the capabilities it can access.

## Core Concepts

### Architecture

```
┌─────────────┐    stdio     ┌─────────────┐
│  MCP Client │ ◄──────────► │  MCP Server  │
│  (Host App) │   transport  │  (Capabilities)│
└─────────────┘              └─────────────┘
```

- **MCP Server** — Exposes tools, resources, and prompts
- **MCP Client** — Connects to servers and invokes their capabilities
- **Transport** — Communication layer (e.g., `stdio`, SSE)

### Three Primitives

| Primitive | Purpose | Example |
|-----------|---------|---------|
| **Tools** | Actions the model can invoke | Read a document, edit a file |
| **Resources** | Data the client can fetch | List of documents, document content |
| **Prompts** | Reusable prompt templates | Format a document in Markdown |

## MCP Server (`mcp_server.py`)

Built using `FastMCP` from the `mcp` package.

### Defining Tools

Tools are functions the AI model can call. Defined with `@mcp.tool()`:

```python
from pydantic import Field
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("DocumentMCP", log_level="ERROR")

@mcp.tool(
    name="read_doc_contents",
    description="Reads the contents of a document and return it as a string.",
)
def read_document(
    doc_id: str = Field(description="The ID of the document to read.")
):
    if doc_id not in docs:
        raise ValueError(f"Document with ID '{doc_id}' not found.")
    return docs[doc_id]
```

- `name` — Tool identifier exposed to the model
- `description` — Helps the model understand when/how to use the tool
- `Field(description=...)` — Documents each parameter for the model

### Defining Resources

Resources provide data to the client. Two types:

**Direct Resources** — Static URIs:

```python
@mcp.resource("docs://documents", mime_type="application/json")
def list_docs() -> list[str]:
    return list(docs.keys())
```

**Templated Resources** — URIs with parameters:

```python
@mcp.resource("docs://documents/{doc_id}", mime_type="text/plain")
def fetch_doc(doc_id: str) -> str:
    return docs[doc_id]
```

### Defining Prompts

Prompts are reusable templates that return structured messages:

```python
from mcp.server.fastmcp.prompts import base

@mcp.prompt(
    name="format",
    description="Rewrites the contents of the document in Markdown format.",
)
def format_document(
    doc_id: str = Field(description="The ID of the document to format.")
) -> list[base.Message]:
    prompt = f"Your goal is to reformat document {doc_id} to markdown..."
    return [base.UserMessage(prompt)]
```

### Running the Server

```python
if __name__ == "__main__":
    mcp.run(transport="stdio")
```

## MCP Client (`mcp_client.py`)

Connects to an MCP server via `stdio` transport and provides methods for all three primitives.

### Key Operations

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Connect
server_params = StdioServerParameters(command="uv", args=["run", "mcp_server.py"])
stdio_transport = await stdio_client(server_params)
session = ClientSession(read_stream, write_stream)
await session.initialize()

# Tools
tools = await session.list_tools()               # List available tools
result = await session.call_tool(name, input)     # Call a tool

# Resources
resource = await session.read_resource(AnyUrl(uri))  # Read a resource

# Prompts
prompts = await session.list_prompts()            # List available prompts
messages = await session.get_prompt(name, args)   # Get a prompt
```

### Context Manager Pattern

The sample project wraps the client as an async context manager for clean setup/teardown:

```python
async with MCPClient(command="uv", args=["run", "mcp_server.py"]) as client:
    tools = await client.list_tools()
```

## Tool Execution Loop

The sample project implements a multi-turn tool use loop in `core/chat.py`:

```
User Query → Claude → [tool_use?] → Execute Tool → Send Result → Claude → Final Response
                         ▲                                           │
                         └───────────────────────────────────────────┘
```

1. Send user message + available tools to Claude
2. If Claude responds with `stop_reason == "tool_use"`, execute the requested tools
3. Send tool results back to Claude
4. Repeat until Claude responds with a final text answer

## CLI Features (Sample Project)

The `cli_project` demonstrates MCP integration in a chat application:

- **`@` mentions** — Reference documents inline (e.g., `@deposition.md`), fetched via MCP resources
- **`/` commands** — Trigger MCP prompts (e.g., `/format deposition.md`), with tab-completion
- **Multi-server support** — Pass additional server scripts as CLI arguments

### Running the Sample

```bash
cd cli_project
uv sync
uv run main.py
```

Requires `.env` with `ANTHROPIC_API_KEY` and `CLAUDE_MODEL` set. See `cli_project/README.md` for full setup instructions.
