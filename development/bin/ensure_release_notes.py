"""Ensure that release notes exist for a given version.

This script will do the following:
    Ensure a release notes file exists at `docs/admin/release_notes/version_{version}.md`.
    Ensure the `mkdocs.yml` file is updated to add the release notes file to the navigation.
    Ensure the `pyproject.toml` `tool.towncrier.filename` is updated to reference the release notes file.

It shouldn't be necessary to run this file manually. It is automatically called by `invoke generate-release-notes`.

Example:
    $ python ensure_release_notes.py --version '1.0.0'
"""

import argparse

try:
    import tomllib
except ImportError:
    import tomli as tomllib

from pathlib import Path


def release_notes_pyproject_toml(version):
    """Update the pyproject.toml file to set the towncrier filename for the given version."""
    pyproject_file = Path(__file__).parent.parent.parent / "pyproject.toml"
    pyproject_content = pyproject_file.read_text()
    pyproject_data = tomllib.loads(pyproject_content)
    release_notes_file = f"docs/admin/release_notes/version_{version}.md"

    # Update the towncrier filename
    if pyproject_data["tool"]["towncrier"].get("filename", "") != release_notes_file:
        pyproject_data["tool"]["towncrier"]["filename"] = release_notes_file

        # Write back the updated content to pyproject.toml
        # tomllib is not used to write the file because it is not roundtrippable
        new_pyproject_content = []
        in_towncrier_section = False
        for line in pyproject_content.splitlines():
            if line.strip() == "[tool.towncrier]":
                in_towncrier_section = True
                new_pyproject_content.append(line)
                continue
            if in_towncrier_section:
                if line.strip().startswith("filename"):
                    new_pyproject_content.append(f'filename = "docs/admin/release_notes/version_{version}.md"')
                    in_towncrier_section = False  # Only replace the first occurrence
                else:
                    new_pyproject_content.append(line)
            else:
                new_pyproject_content.append(line)

        pyproject_file.write_text("\n".join(new_pyproject_content))
        # Add a newline at the end of the file if it doesn't exist
        if not pyproject_file.read_text().endswith("\n"):
            pyproject_file.write_text(pyproject_file.read_text() + "\n")
        # Remind the user to update the release notes file.
        print(
            f"\033[33mRemember to update the Release Overview section in the release notes file: {release_notes_file}\033[0m"
        )


def ensure_release_notes_file(version):
    """Ensure that the release notes file for the given version exists and is referenced in mkdocs.yml."""
    release_notes_file = (
        Path(__file__).parent.parent.parent / "docs" / "admin" / "release_notes" / f"version_{version}.md"
    )
    if not release_notes_file.exists():
        # Create a new release notes file with a basic template from towncrier_header.txt
        towncrier_header = Path(__file__).parent.parent / "towncrier_header.txt"
        content = towncrier_header.read_text().format(version=version)
        release_notes_file.write_text(content)


def ensure_mkdocs_version(version):
    """Ensure that mkdocs.yml includes the new release notes file in the navigation."""
    mkdocs_yml_file = Path(__file__).parent.parent.parent / "mkdocs.yml"
    mkdocs_yml_content = mkdocs_yml_file.read_text()
    release_notes_nav_entry = f'          - v{version}: "admin/release_notes/version_{version}.md"\n'
    if release_notes_nav_entry in mkdocs_yml_content:
        return

    # Add the new release notes entry to the mkdocs.yml content
    if "Release Notes:" in mkdocs_yml_content:
        mkdocs_yml_content = mkdocs_yml_content.replace(
            '          - "admin/release_notes/index.md"\n',
            f'          - "admin/release_notes/index.md"\n{release_notes_nav_entry}',
        )

    mkdocs_yml_file.write_text(mkdocs_yml_content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ensure release notes exist for a given version.")
    parser.add_argument("--version", help="The version number (e.g. 2.2)")
    args = parser.parse_args()
    ensure_release_notes_file(args.version)
    ensure_mkdocs_version(args.version)
    release_notes_pyproject_toml(args.version)
