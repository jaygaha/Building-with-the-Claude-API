# Anthropic Apps

Two powerful applications built by Anthropic:

1. **Claude Code** — An agentic CLI for software development
2. **Computer Use** — Claude's ability to interact with a computer's UI

---

## Claude Code

Claude Code is an agentic coding tool that works alongside you throughout every phase of a software project — from initial setup to deployment. It can read files, write code, run commands, and reason about your entire codebase.

### Key Commands

| Command | Description |
|---------|-------------|
| `/init` | Scans the codebase and generates a `CLAUDE.md` file summarizing structure, dependencies, and coding patterns |
| `/clear` | Clears or resets the conversation history |
| `#` | Quickly append a note or guideline to `CLAUDE.md` (e.g. `# Always use descriptive variable names`) |

### CLAUDE.md Scopes

`/init` generates a `CLAUDE.md` that is automatically included as context in all future conversations. You can have multiple files at different scopes:

- **Project** — Shared across all engineers working on the project (checked into git)
- **Local** — Personal notes, not checked into git
- **User** — Applied across all your projects

### Registering an MCP Server with Claude Code

```bash
# claude mcp add [server-name] [command-to-start-server]
claude mcp add documents uv run main.py
```

---

## app_starter — MCP Document Tools Server

📁 [`app_starter/`](./app_starter/)

A starter Python MCP server built with `fastmcp` that exposes document-processing and math tools to AI assistants. It demonstrates the expected pattern for defining and registering MCP tools.

### Architecture

```
app_starter/
├── main.py              # FastMCP server entry point — registers tools
├── tools/
│   ├── document.py      # Converts PDF/DOCX files to Markdown via MarkItDown
│   └── math.py          # Example add tool (reference implementation)
└── tests/
    ├── fixtures/         # Sample .docx and .pdf files for tests
    └── test_document.py  # pytest tests for document tools
```

### Setup

```bash
cd app_starter
uv venv
source .venv/bin/activate
uv pip install -e .
```

### Running & Testing

```bash
# Start the MCP server
uv run main.py

# Run all tests
uv run pytest

# Run a single test
uv run pytest tests/test_document.py::TestBinaryDocumentToMarkdown::test_binary_document_to_markdown_with_docx
```

### Defining MCP Tools

Tools are plain Python functions registered in `main.py`:

```python
mcp.tool()(my_function)
```

Use `Field` from pydantic for parameter descriptions:

```python
from pydantic import Field

def my_tool(
    param: str = Field(description="Description of this parameter"),
) -> str:
    """One-line summary.

    Detailed explanation.

    When to use:
    - Scenario A

    When NOT to use:
    - Scenario B

    Examples:
    >>> my_tool("foo")
    "expected output"
    """
```

See `tools/math.py` for a complete reference implementation.
