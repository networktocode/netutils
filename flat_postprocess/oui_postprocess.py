"""Python code used to postprocess Flat github action data related to OUI mappings."""

import re
import subprocess
import sys

HEX_RE = r"^MA-L,(?P<hex>[0-9A-Fa-f]{6}),\"(?P<company>[^\"]+)\",.*$"

OUI_MAPPINGS = {}
URL = "https://standards-oui.ieee.org/oui/oui.txt"


def download_csv_text(url: str = URL) -> str:
    """Download the CSV text from the given URL."""
    proc = subprocess.run(  # noqa: S603
        ["curl", "-fsSL", url],  # noqa: S607
        check=True,
        capture_output=True,
        text=True,
    )
    return proc.stdout


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("Usage: python oui_postprocess.py <output_file> [<download_latest>]")

    output_path = sys.argv[1]
    download = "--download" in sys.argv[2:]

    if download:
        csv_text = download_csv_text(URL)
        with open(output_path, "w", encoding="utf-8", newline="") as oui_textfile:
            oui_textfile.write(csv_text)

    with open(output_path, "r", encoding="utf-8", newline="") as oui_file:
        for line in oui_file:
            if re.search(HEX_RE, line):
                print()
                group_regex_values = re.search(HEX_RE, line).groupdict()
                if group_regex_values.get("hex") and group_regex_values.get("company"):
                    OUI_MAPPINGS.update({group_regex_values.get("hex").lower(): group_regex_values.get("company")})

    with open(output_path, "w", encoding="utf-8") as oui_mappings:
        oui_mappings.write('"""Dictionary object to store OUI information."""\n')
        oui_mappings.write("# pylint: disable=too-many-lines\n")
        oui_mappings.write("import typing\n\n")
        oui_mappings.write("OUI_MAPPINGS: typing.Dict[str, str] = {\n")
        for mac, company in sorted(OUI_MAPPINGS.items()):
            oui_mappings.write(f'    "{mac}": "{company}",\n')
        oui_mappings.write("}\n")
