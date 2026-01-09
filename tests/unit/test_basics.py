<<<<<<< HEAD
<<<<<<< HEAD
"""Basic tests that do not require netutils."""
=======
"""Basic tests that do not require Netutils."""
>>>>>>> 1476cba (Cookie updated targeting develop by NetworkToCode Cookie Drift Manager Tool)
=======
"""Basic tests that do not require Netutils."""
>>>>>>> 35e1395 (Cookie updated targeting develop by NetworkToCode Cookie Drift Manager Tool)

import os
import re
import unittest

import toml


class TestDocsReleaseNotes(unittest.TestCase):
    """Test that mkdocs has the release notes for the current version."""

    def test_version_file_found(self):
        """Verify that if the current version has no letters, which would see in alpha or beta has an associated release note file."""
        parent_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
        poetry_path = os.path.join(parent_path, "pyproject.toml")
        project_version = toml.load(poetry_path)["tool"]["poetry"]["version"]

        docs_path = os.path.join(parent_path, "docs")
        release_notes_files = [file for file in os.listdir(f"{docs_path}/admin/release_notes/") if file.endswith(".md")]
        version_pattern = re.compile(r"^(\d+)\.(\d+)\.\d+$")

        match = version_pattern.match(project_version)
        # If there is no match, then it is likely an alpha or beta version and we can skip this test.
        if match:
            major, minor = match.groups()
            version_str = f"version_{major}.{minor}.md"
            if version_str not in release_notes_files:
                self.fail(f"Release note file for version {version_str} not found in release notes folder.")
