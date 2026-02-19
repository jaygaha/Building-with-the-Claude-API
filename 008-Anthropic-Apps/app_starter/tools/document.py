from markitdown import MarkItDown, StreamInfo
from io import BytesIO
from pathlib import Path
from pydantic import Field


def binary_document_to_markdown(binary_data: bytes, file_type: str) -> str:
    """Converts binary document data to markdown-formatted text."""
    md = MarkItDown()
    file_obj = BytesIO(binary_data)
    stream_info = StreamInfo(extension=file_type)
    result = md.convert(file_obj, stream_info=stream_info)
    return result.text_content


SUPPORTED_EXTENSIONS = {".docx", ".pdf"}


def document_path_to_markdown(
    path: str = Field(description="Absolute or relative path to a PDF or DOCX file"),
) -> str:
    """Convert a PDF or DOCX file on disk to markdown-formatted text.

    Reads the file at the given path, infers the document type from its
    extension, and returns the contents as a markdown string.

    When to use:
    - When you have a local file path to a PDF or DOCX document
    - When you need to extract readable text from a document for further processing

    When NOT to use:
    - When you already have the file bytes in memory (use binary_document_to_markdown)
    - For file types other than PDF or DOCX

    Examples:
    >>> document_path_to_markdown("/tmp/report.pdf")
    "# Report\\n\\nSome content..."
    >>> document_path_to_markdown("/tmp/notes.docx")
    "# Notes\\n\\n- Item one"
    """
    if not path:
        raise ValueError("Path must not be empty.")

    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"No file found at: {path}")

    if file_path.is_dir():
        raise IsADirectoryError(f"Path is a directory, not a file: {path}")

    extension = file_path.suffix.lower()
    if extension not in SUPPORTED_EXTENSIONS:
        raise ValueError(
            f"Unsupported file type '{extension}'. Supported types: {', '.join(SUPPORTED_EXTENSIONS)}"
        )

    binary_data = file_path.read_bytes()
    return binary_document_to_markdown(binary_data, extension.lstrip("."))
