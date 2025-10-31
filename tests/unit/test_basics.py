"""Basic tests that do not require netutils."""

import os
import re
import unittest

import toml


class TestDocsPackaging(unittest.TestCase):
    """Test Version in doc requirements is the same pyproject."""

    def test_version(self):
        """Verify that pyproject.toml dev dependencies have the same versions as in the docs requirements.txt."""
        parent_path = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        )
        poetry_path = os.path.join(parent_path, "pyproject.toml")
        poetry_details = toml.load(poetry_path)["tool"]["poetry"]["group"]["dev"][
            "dependencies"
        ]
        with open(
            f"{parent_path}/docs/requirements.txt", "r", encoding="utf-8"
        ) as file:
            requirements = [
                line
                for line in file.read().splitlines()
                if (len(line) > 0 and not line.startswith("#"))
            ]
        for pkg in requirements:
            package_name = pkg
            if len(pkg.split("==")) == 2:  # noqa: PLR2004
                package_name, version = pkg.split("==")
            else:
                version = "*"
            self.assertEqual(poetry_details[package_name], version)


class TestDocsReleaseNotes(unittest.TestCase):
    """Test that mkdocs has the release notes for the current version."""

    def test_version_file_found(self):
        """Verify that if the current version has no letters, which would see in alpha or beta has an associated release note file."""
        parent_path = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        )
        poetry_path = os.path.join(parent_path, "pyproject.toml")
        project_version = toml.load(poetry_path)["tool"]["poetry"]["version"]

        docs_path = os.path.join(parent_path, "docs")
        release_notes_files = [
            file
            for file in os.listdir(f"{docs_path}/admin/release_notes/")
            if file.endswith(".md")
        ]
        version_pattern = re.compile(r"^(\d+)\.(\d+)\.\d+$")

        match = version_pattern.match(project_version)
        # If there is no match, then it is likely an alpha or beta version and we can skip this test.
        if match:
            major, minor = match.groups()
            version_str = f"version_{major}.{minor}.md"
            if version_str not in release_notes_files:
                self.fail(
                    f"Release note file for version {version_str} not found in release notes folder."
                )
