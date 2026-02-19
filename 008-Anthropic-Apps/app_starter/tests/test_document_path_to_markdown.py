import os
import pytest
from tools.document import binary_document_to_markdown, document_path_to_markdown


class TestDocumentPathToMarkdown:
    FIXTURES_DIR = os.path.join(os.path.dirname(__file__), "fixtures")
    DOCX_FIXTURE = os.path.join(FIXTURES_DIR, "mcp_docs.docx")
    PDF_FIXTURE = os.path.join(FIXTURES_DIR, "mcp_docs.pdf")

    # --- Happy path ---

    def test_converts_docx_to_markdown(self):
        """Returns a non-empty string for a valid DOCX file."""
        result = document_path_to_markdown(self.DOCX_FIXTURE)
        assert isinstance(result, str)
        assert len(result) > 0

    def test_converts_pdf_to_markdown(self):
        """Returns a non-empty string for a valid PDF file."""
        result = document_path_to_markdown(self.PDF_FIXTURE)
        assert isinstance(result, str)
        assert len(result) > 0

    def test_docx_contains_markdown_formatting(self):
        """Output from DOCX includes recognisable markdown syntax."""
        result = document_path_to_markdown(self.DOCX_FIXTURE)
        assert "#" in result or "-" in result or "*" in result

    def test_pdf_contains_markdown_formatting(self):
        """Output from PDF includes recognisable markdown syntax."""
        result = document_path_to_markdown(self.PDF_FIXTURE)
        assert "#" in result or "-" in result or "*" in result

    def test_extension_inferred_from_path_docx(self):
        """File type is inferred from the path extension, not passed explicitly."""
        result = document_path_to_markdown(self.DOCX_FIXTURE)
        # If extension inference were broken the conversion would fail or return empty
        assert len(result) > 0

    def test_extension_inferred_from_path_pdf(self):
        """File type is inferred from the path extension, not passed explicitly."""
        result = document_path_to_markdown(self.PDF_FIXTURE)
        assert len(result) > 0

    # --- Content accuracy ---

    def test_docx_output_matches_binary_function(self):
        """Output equals what binary_document_to_markdown produces for the same bytes."""
        with open(self.DOCX_FIXTURE, "rb") as f:
            data = f.read()
        expected = binary_document_to_markdown(data, "docx")
        assert document_path_to_markdown(self.DOCX_FIXTURE) == expected

    def test_pdf_output_matches_binary_function(self):
        """Output equals what binary_document_to_markdown produces for the same bytes."""
        with open(self.PDF_FIXTURE, "rb") as f:
            data = f.read()
        expected = binary_document_to_markdown(data, "pdf")
        assert document_path_to_markdown(self.PDF_FIXTURE) == expected

    # --- Error / invalid input ---

    def test_raises_for_nonexistent_path(self):
        """Raises FileNotFoundError when the path does not exist."""
        with pytest.raises(FileNotFoundError):
            document_path_to_markdown("/nonexistent/path/file.docx")

    def test_raises_for_unsupported_file_type(self):
        """Raises an error for unsupported file extensions."""
        unsupported = os.path.join(self.FIXTURES_DIR, "file.txt")
        # Create a temporary dummy file so the path exists
        with open(unsupported, "w") as f:
            f.write("hello")
        try:
            with pytest.raises((ValueError, Exception)):
                document_path_to_markdown(unsupported)
        finally:
            os.remove(unsupported)

    def test_raises_for_empty_path(self):
        """Raises an error when an empty string is passed as the path."""
        with pytest.raises((ValueError, FileNotFoundError, Exception)):
            document_path_to_markdown("")

    def test_raises_for_directory_path(self):
        """Raises an error when the path points to a directory."""
        with pytest.raises((IsADirectoryError, ValueError, Exception)):
            document_path_to_markdown(self.FIXTURES_DIR)
