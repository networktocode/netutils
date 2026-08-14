"""Python code used to postprocess Flat github action data related to OUI mappings."""

import json
import re
import subprocess
import sys

HEX_RE = re.compile(
    r"^[^,]*,(?P<hex>[0-9A-Fa-f]{6})," + r'(?:"(?P<company_q>(?:[^"]|"")*)"|(?P<company_u>[^,]*))(?:,|$)'
)

OUI_MAPPINGS = {}
URL = "https://standards-oui.ieee.org/oui/oui.csv"


def download_csv_text(url: str = URL) -> str:
    """Download the CSV text from the given URL."""
    proc = subprocess.run(  # noqa: S603
        [  # noqa: S607
            "curl",
            "-fsSL",
            "--retry",
            "5",
            "--retry-all-errors",
            "--retry-max-time",
            "300",
            "--connect-timeout",
            "15",
            "--max-time",
            "120",
            url,
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    return proc.stdout


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("Usage: python oui_postprocess.py <output_file> [--stdin]")

    output_path = sys.argv[1]

    if "--stdin" in sys.argv[2:]:
        csv_text = sys.stdin.read()
    else:
        csv_text = download_csv_text(URL)

    for line in csv_text.splitlines():
        match = HEX_RE.match(line)
        if not match:
            continue
        company = match.group("company_q") or match.group("company_u") or ""
        company = company.replace('""', '"').strip()
        hex_value = match.group("hex")
        if hex_value and company:
            OUI_MAPPINGS[hex_value.lower()] = company

    if not OUI_MAPPINGS:
        raise SystemExit("No OUI records parsed; refusing to write empty mappings.")

    with open(output_path, "w", encoding="utf-8") as oui_mappings:
        oui_mappings.write('"""Dictionary object to store OUI information."""\n')
        oui_mappings.write("# pylint: disable=too-many-lines\n")
        oui_mappings.write("import typing\n\n")
        oui_mappings.write("OUI_MAPPINGS: typing.Dict[str, str] = {\n")
        for mac, company in sorted(OUI_MAPPINGS.items()):
            oui_mappings.write(f"    {json.dumps(mac)}: {json.dumps(company)},\n")
        oui_mappings.write("}\n")
