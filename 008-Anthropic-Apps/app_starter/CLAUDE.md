# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Setup
uv venv && source .venv/bin/activate
uv pip install -e .

# Run the MCP server
uv run main.py

# Run all tests
uv run pytest

# Run a single test
uv run pytest tests/test_document.py::TestBinaryDocumentToMarkdown::test_binary_document_to_markdown_with_docx
```

## Architecture

This is a **Python MCP (Model Context Protocol) server** built with `fastmcp`. It exposes document-processing tools to AI assistants via the MCP protocol.

- `main.py` — Entry point. Creates the `FastMCP` server instance and registers tools with `mcp.tool()(function)`.
- `tools/` — Tool implementations. Each file groups related tools. Functions here are plain Python; they are not MCP-aware.
- `tools/document.py` — Uses `markitdown` to convert binary document data (DOCX, PDF) to markdown.
- `tools/math.py` — Example/reference tool showing the expected tool definition pattern.
- `tests/` — pytest tests. Fixtures (sample `.docx` and `.pdf`) live in `tests/fixtures/`.

## Defining MCP Tools

Tools are plain Python functions registered in `main.py`:

```python
mcp.tool()(my_function)
```

Use `Field` from pydantic for parameter descriptions:

```python
from pydantic import Field

def my_tool(
    param1: str = Field(description="Detailed description of this parameter"),
    param2: int = Field(description="Explain what this parameter does"),
) -> ReturnType:
    """One-line summary.

    Detailed explanation of functionality.

    When to use:
    - Scenario A
    - Scenario B

    When NOT to use:
    - Scenario C

    Examples:
    >>> my_tool("foo", 1)
    "expected output"
    """
```

See `tools/math.py` for a complete reference implementation.

## Code Style

- Always apply appropriate types to function arguments.
