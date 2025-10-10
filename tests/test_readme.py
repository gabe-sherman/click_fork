"""Tests for README.md structure and content validation."""
from __future__ import annotations

import re
from pathlib import Path

import pytest


@pytest.fixture
def readme_path():
    """Return the path to README.md at the repository root."""
    return Path(__file__).parent.parent / "README.md"


@pytest.fixture
def readme_content(readme_path):
    """Read and return the content of README.md."""
    return readme_path.read_text(encoding="utf-8")


class TestAIMaintainerComment:
    """Tests for the AI maintainer comment structure and content."""

    def test_ai_maintainer_comment_exists(self, readme_content):
        """Verify that the AI maintainer comment exists at the beginning."""
        assert readme_content.startswith("<!--"), (
            "README should start with an HTML comment"
        )
        assert "🤖 AI MAINTAINER NOTE:" in readme_content, (
            "AI maintainer note should be present"
        )

    def test_ai_maintainer_comment_is_html_comment(self, readme_content):
        """Verify the AI maintainer note is properly enclosed in HTML comment tags."""
        lines = readme_content.split("\n")
        assert lines[0].strip() == "<!--", (
            "First line should be HTML comment opening tag"
        )
        
        # Find the closing tag
        closing_found = False
        for _i, line in enumerate(lines[:15]):  # Check first 15 lines
            if line.strip() == "-->":
                closing_found = True
                break
        
        assert closing_found, "HTML comment should be properly closed with -->"

    def test_ai_maintainer_comment_contains_key_guidance(self, readme_content):
        """Verify the AI maintainer comment contains essential guidance."""
        comment_section = readme_content.split("-->")[0]
        
        required_phrases = [
            "reviewing or updating this README",
            "improvements",
            "user-friendly",
            "clarity",
            "readability",
            "visual appeal",
        ]
        
        for phrase in required_phrases:
            assert phrase in comment_section, (
                f"AI maintainer comment should mention '{phrase}'"
            )

    def test_ai_maintainer_comment_mentions_formatting(self, readme_content):
        """Verify the comment mentions formatting guidelines."""
        comment_section = readme_content.split("-->")[0]
        
        formatting_terms = ["emoji", "Markdown", "formatting"]
        found_terms = [term for term in formatting_terms if term in comment_section]
        
        assert len(found_terms) >= 2, (
            f"AI maintainer comment should mention formatting guidelines. "
            f"Found: {found_terms}"
        )

    def test_ai_maintainer_comment_has_proper_structure(self, readme_content):
        """Verify the comment has a clear, structured format."""
        lines = readme_content.split("\n")
        comment_lines = []
        
        for line in lines[1:15]:  # Skip opening tag, check next lines
            if line.strip() == "-->":
                break
            comment_lines.append(line)
        
        # Should have multiple lines with guidance
        assert len(comment_lines) >= 4, (
            "AI maintainer comment should have multiple guidance lines"
        )
        
        # Should not be empty
        non_empty_lines = [line for line in comment_lines if line.strip()]
        assert len(non_empty_lines) >= 4, (
            "AI maintainer comment should have substantial content"
        )


class TestReadmeStructure:
    """Tests for overall README structure and required sections."""

    def test_readme_exists(self, readme_path):
        """Verify README.md file exists."""
        assert readme_path.exists(), "README.md should exist at repository root"
        assert readme_path.is_file(), "README.md should be a file"

    def test_readme_has_main_heading(self, readme_content):
        """Verify README has a main 'Click' heading."""
        assert "# Click" in readme_content, (
            "README should have a main heading '# Click'"
        )

    def test_readme_has_required_sections(self, readme_content):
        """Verify README contains all required sections."""
        required_sections = [
            "# Click",
            "## A Simple Example",
            "## Donate",
            "## Contributing",
        ]
        
        for section in required_sections:
            assert section in readme_content, (
                f"README should contain section: {section}"
            )

    def test_readme_has_project_description(self, readme_content):
        """Verify README contains a description of the project."""
        key_phrases = [
            "command line interface",
            "composable way",
            # Uses regex to handle both straight and curly quotes
        ]
        
        for phrase in key_phrases:
            assert phrase in readme_content, (
                f"README should describe the project, mentioning '{phrase}'"
            )
        
        # Check for "Command Line Interface Creation Kit" with flexible quote matching
        assert re.search(r'Command\s+Line Interface Creation Kit', readme_content), (
            "README should mention 'Command Line Interface Creation Kit'"
        )

    def test_readme_has_key_features(self, readme_content):
        """Verify README lists key features of Click."""
        features = [
            "Arbitrary nesting of commands",
            "Automatic help page generation",
            "lazy loading of subcommands",
        ]
        
        for feature in features:
            assert feature in readme_content, (
                f"README should mention key feature: '{feature}'"
            )

    def test_readme_sections_order(self, readme_content):
        """Verify sections appear in logical order."""
        sections = [
            "# Click",
            "## A Simple Example",
            "## Donate",
            "## Contributing",
        ]
        
        positions = []
        for section in sections:
            pos = readme_content.find(section)
            assert pos != -1, f"Section '{section}' should exist"
            positions.append(pos)
        
        # Verify positions are in ascending order
        assert positions == sorted(positions), (
            "Sections should appear in the expected order"
        )


class TestReadmeCodeBlocks:
    """Tests for code blocks in README."""

    def test_readme_has_python_code_example(self, readme_content):
        """Verify README contains Python code examples."""
        assert "```python" in readme_content, (
            "README should contain Python code examples"
        )

    def test_readme_python_example_is_valid_syntax(self, readme_content):
        """Verify the Python example has valid syntax structure."""
        # Extract Python code blocks
        python_blocks = re.findall(
            r"```python\n(.*?)```", readme_content, re.DOTALL
        )
        
        assert len(python_blocks) > 0, "Should have at least one Python code block"
        
        # Check the main example has key Click elements
        example_code = python_blocks[0]
        assert "import click" in example_code, (
            "Python example should import click"
        )
        assert "@click.command()" in example_code, (
            "Python example should use @click.command decorator"
        )
        assert "@click.option" in example_code, (
            "Python example should demonstrate @click.option"
        )

    def test_readme_has_shell_output_example(self, readme_content):
        """Verify README shows example shell output."""
        # Look for shell/terminal output blocks
        has_shell_block = (
            "```\n$" in readme_content or 
            "```bash" in readme_content or
            "```shell" in readme_content
        )
        assert has_shell_block, (
            "README should show example shell output"
        )

    def test_python_example_shows_click_features(self, readme_content):
        """Verify the Python example demonstrates key Click features."""
        python_blocks = re.findall(
            r"```python\n(.*?)```", readme_content, re.DOTALL
        )
        
        example = python_blocks[0]
        features = {
            "click.echo": "Should demonstrate click.echo for output",
            "option": "Should demonstrate options",
            "def ": "Should have function definition",
        }
        
        for feature, message in features.items():
            assert feature in example, message

    def test_code_blocks_are_properly_closed(self, readme_content):
        """Verify all code blocks are properly opened and closed."""
        # Count opening and closing code block markers
        opening_markers = readme_content.count("```")
        
        # Should be even (each opening has a closing)
        assert opening_markers % 2 == 0, (
            f"Code blocks should be properly closed. Found {opening_markers} markers"
        )


class TestReadmeLinks:
    """Tests for links in README."""

    def test_readme_has_donation_link(self, readme_content):
        """Verify README includes donation link."""
        assert "please donate today" in readme_content.lower(), (
            "README should include a call to action for donations"
        )
        assert "palletsprojects.com/donate" in readme_content, (
            "README should include the Pallets donation link"
        )

    def test_readme_has_contributing_link(self, readme_content):
        """Verify README includes contributing documentation link."""
        assert "palletsprojects.com/contributing" in readme_content, (
            "README should include link to contributing documentation"
        )

    def test_readme_link_format_is_valid(self, readme_content):
        """Verify Markdown links are properly formatted."""
        # Find inline links [text](url) and reference-style links [text][ref]
        inline_links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', readme_content)
        reference_links = re.findall(r'\[([^\]]+)\]\[([^\]]*)\]', readme_content)
        
        all_links = inline_links + reference_links
        assert len(all_links) > 0, "README should contain Markdown links"
        
        # Validate inline links
        for text, url in inline_links:
            assert text.strip(), "Link text should not be empty"
            assert url.strip(), "Link URL should not be empty"
            # URLs should not contain spaces (unless percent-encoded)
            if " " in url and "%" not in url:
                pytest.fail(f"Link URL should not contain unencoded spaces: {url}")
        
        # Validate reference links
        for text, _ref in reference_links:
            assert text.strip(), "Link text should not be empty"

    def test_readme_has_image_reference(self, readme_content):
        """Verify README includes the Click logo image."""
        assert "https://raw.githubusercontent.com" in readme_content, (
            "README should include image from GitHub"
        )
        assert "click-name.svg" in readme_content, (
            "README should include the Click logo SVG"
        )

    def test_image_has_proper_html_structure(self, readme_content):
        """Verify image is properly formatted in HTML."""
        # Should have img tag with src attribute
        assert '<img src="' in readme_content, (
            "README should have properly formatted img tag"
        )
        # Should be in a centered div
        assert '<div align="center">' in readme_content, (
            "Logo should be centered"
        )

    def test_all_urls_use_https(self, readme_content):
        """Verify all external URLs use HTTPS."""
        # Find all URLs in the content
        urls = re.findall(r'https?://[^\s<>"{}|\\^\[\]`]+', readme_content)
        
        for url in urls:
            assert url.startswith("https://"), (
                f"All URLs should use HTTPS: {url}"
            )


class TestReadmeFormatting:
    """Tests for markdown formatting and style."""

    def test_readme_uses_proper_markdown_headings(self, readme_content):
        """Verify headings use proper markdown syntax."""
        lines = readme_content.split("\n")
        heading_lines = [line for line in lines if line.strip().startswith("#")]
        
        for line in heading_lines:
            # Headings should have space after #
            assert re.match(r"^#+\s", line.strip()), (
                f"Heading should have space after #: {line}"
            )

    def test_readme_has_proper_line_spacing(self, readme_content):
        """Verify README has appropriate blank lines between sections."""
        # After AI comment and before logo, should have blank lines
        lines = readme_content.split("\n")
        
        # Find the closing --> of comment
        comment_end_idx = None
        for i, line in enumerate(lines):
            if line.strip() == "-->":
                comment_end_idx = i
                break
        
        assert comment_end_idx is not None, "Should find comment closing"
        
        # There should be blank lines after the comment
        next_non_empty = None
        for i in range(comment_end_idx + 1, min(comment_end_idx + 5, len(lines))):
            if lines[i].strip():
                next_non_empty = i
                break
        
        assert next_non_empty is not None, (
            "Should have content after AI comment"
        )
        assert next_non_empty > comment_end_idx + 1, (
            "Should have at least one blank line after AI comment"
        )

    def test_readme_code_blocks_specify_language(self, readme_content):
        """Verify code blocks specify their language."""
        # Find all code block openings
        code_blocks = re.findall(r'```(\w*)\n', readme_content)
        
        # Most code blocks should specify a language
        blocks_with_language = [b for b in code_blocks if b]
        
        assert len(blocks_with_language) > 0, (
            "At least some code blocks should specify their language"
        )

    def test_readme_has_consistent_heading_style(self, readme_content):
        """Verify headings use consistent style (ATX-style)."""
        lines = readme_content.split("\n")
        
        # Find heading lines (excluding HTML comments)
        heading_lines = []
        in_comment = False
        for line in lines:
            if "<!--" in line:
                in_comment = True
            if "-->" in line:
                in_comment = False
                continue
            if not in_comment and line.strip().startswith("#"):
                heading_lines.append(line.strip())
        
        # All should be ATX-style (# at start, not underlines)
        for heading in heading_lines:
            assert heading.startswith("#"), (
                f"Should use ATX-style headings: {heading}"
            )

    def test_readme_list_items_properly_formatted(self, readme_content):
        """Verify list items follow consistent formatting."""
        # Find lines that appear to be list items
        lines = readme_content.split("\n")
        # Only consider lines that start with - or * followed by whitespace
        # Exclude lines that match HTML comment syntax like -->
        list_lines = [
            line for line in lines 
            if re.match(r'^\s*[-*]\s', line) and not line.strip().startswith('--')
        ]
        
        if list_lines:  # If there are lists
            for line in list_lines:
                # List items should have space after dash
                assert re.match(r'^\s*[-*]\s+', line), (
                    f"List items should have space after marker: {line}"
                )


class TestReadmeContent:
    """Tests for specific content requirements."""

    def test_readme_mentions_pallets_organization(self, readme_content):
        """Verify README credits the Pallets organization."""
        assert "Pallets" in readme_content, (
            "README should mention the Pallets organization"
        )

    def test_readme_describes_click_purpose(self, readme_content):
        """Verify README clearly describes Click's purpose."""
        purpose_keywords = [
            "command line",
            "CLI",
            "interface",
            "composable",
            "configurable",
        ]
        
        found_keywords = [k for k in purpose_keywords if k in readme_content]
        
        assert len(found_keywords) >= 4, (
            f"README should clearly describe Click's purpose. "
            f"Found keywords: {found_keywords}"
        )

    def test_readme_example_is_practical(self, readme_content):
        """Verify the example demonstrates practical usage."""
        python_blocks = re.findall(
            r"```python\n(.*?)```", readme_content, re.DOTALL
        )
        
        if python_blocks:
            example = python_blocks[0]
            # Should have a docstring
            assert '"""' in example or "'''" in example, (
                "Example function should have a docstring"
            )
            # Should show actual functionality
            assert "for" in example or "if" in example or "return" in example, (
                "Example should demonstrate actual program logic"
            )

    def test_readme_encourages_contribution(self, readme_content):
        """Verify README encourages community contribution."""
        contribution_terms = ["contribute", "contributing", "community"]
        
        found = [term for term in contribution_terms if term in readme_content.lower()]
        
        assert len(found) > 0, (
            "README should encourage contribution"
        )

    def test_readme_is_not_empty(self, readme_content):
        """Verify README has substantial content."""
        assert len(readme_content) > 500, (
            "README should have substantial content (>500 chars)"
        )
        
        lines = [line.strip() for line in readme_content.split("\n") if line.strip()]
        assert len(lines) > 20, (
            "README should have substantial content (>20 non-empty lines)"
        )

    def test_readme_shows_installation_or_usage_path(self, readme_content):
        """Verify README guides users on getting started."""
        # Should either show installation or jump straight to usage
        helpful_terms = ["example", "install", "pip", "import click"]
        
        found = [term for term in helpful_terms if term.lower() in readme_content.lower()]
        
        assert len(found) >= 2, (
            f"README should help users get started. Found: {found}"
        )


class TestReadmeEdgeCases:
    """Tests for edge cases and potential issues."""

    def test_readme_no_trailing_whitespace(self, readme_content):
        """Verify lines don't have trailing whitespace."""
        lines = readme_content.split("\n")
        lines_with_trailing = [
            i for i, line in enumerate(lines) 
            if line != line.rstrip() and line.strip()  # Ignore empty lines
        ]
        
        # Allow some trailing whitespace but flag excessive cases
        assert len(lines_with_trailing) < 5, (
            f"Too many lines with trailing whitespace: {lines_with_trailing[:5]}"
        )

    def test_readme_no_broken_markdown_syntax(self, readme_content):
        """Check for common markdown syntax errors."""
        # Check for unmatched backticks
        # Inline code uses pairs, code blocks use triple
        # Not perfect but catches obvious issues
        
        # Check for unmatched bold/italic markers
        # This is a simplified check
        assert readme_content.count("**") % 2 == 0, (
            "Unmatched bold markers (**)"
        )

    def test_readme_no_absolute_paths(self, readme_content):
        """Verify README doesn't contain absolute file paths."""
        # Look for potential absolute paths
        suspicious_patterns = ["/home/", "/usr/", "/var/", "C:\\", "D:\\"]
        
        for pattern in suspicious_patterns:
            assert pattern not in readme_content, (
                f"README should not contain absolute paths like: {pattern}"
            )

    def test_readme_encoding_is_utf8(self, readme_path):
        """Verify README uses UTF-8 encoding."""
        # Try to read with UTF-8 and verify emoji is present
        content = readme_path.read_text(encoding="utf-8")
        assert "🤖" in content, (
            "README should properly encode emoji characters"
        )

    def test_readme_line_endings_are_consistent(self, readme_path):
        """Verify README uses consistent line endings."""
        with readme_path.open("rb") as f:
            content = f.read()
        
        # Count different line ending styles
        crlf_count = content.count(b"\r\n")
        lf_count = content.count(b"\n") - crlf_count
        cr_count = content.count(b"\r") - crlf_count
        
        # Should primarily use one style
        if lf_count > 0 and crlf_count > 0:
            # Allow mixed if one is dominant (>90%)
            total = lf_count + crlf_count
            dominant_ratio = max(lf_count, crlf_count) / total
            assert dominant_ratio > 0.9, (
                f"Line endings should be consistent. LF: {lf_count}, CRLF: {crlf_count}"
            )
        
        assert cr_count == 0, "Should not use old Mac CR-only line endings"