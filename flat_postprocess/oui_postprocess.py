"""Python code used to postprocess Flat github action data related to OUI mappings."""

import re
import subprocess
import sys

HEX_RE = re.compile(r"^[^,]*,(?P<hex>[0-9A-Fa-f]{6})," r'(?:"(?P<company_q>(?:[^"]|"")*)"|(?P<company_u>[^,]*))(?:,|$)')

OUI_MAPPINGS = {}
URL = "https://standards-oui.ieee.org/oui/oui.csv"


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
            match = HEX_RE.search(line)
            if not match:
                continue
            groups = match.groupdict()
            hex_value = groups.get("hex")
            company = groups.get("company_q") or groups.get("company_u") or ""
            company = company.replace('""', '"').strip()
            if hex_value and company:
                OUI_MAPPINGS[hex_value.lower()] = company

    with open(output_path, "w", encoding="utf-8") as oui_mappings:
        oui_mappings.write('"""Dictionary object to store OUI information."""\n')
        oui_mappings.write("# pylint: disable=too-many-lines\n")
        oui_mappings.write("import typing\n\n")
        oui_mappings.write("OUI_MAPPINGS: typing.Dict[str, str] = {\n")
        for mac, company in sorted(OUI_MAPPINGS.items()):
            oui_mappings.write(f'    "{mac}": "{company}",\n')
        oui_mappings.write("}\n")
