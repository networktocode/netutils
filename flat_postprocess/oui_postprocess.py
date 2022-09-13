"""Python code used to postprocess Flat github action data related to OUI mappings."""
import sys
import re
import json

HEX_RE = r"^(?P<hex>[A-Fa-f0-9]{6})\s+\(.*\)[^a-zA-Z0-9]+(?P<company>.*)$"
OUI_MAPPINGS = {}

if __name__ == "__main__":
    print(f"argv: {sys.argv}")
    with open(sys.argv[1], "r", encoding="utf-8") as oui_file:
        for line in oui_file:
            if re.search(HEX_RE, line):
                group_regex_values = re.search(HEX_RE, line).groupdict()
                if group_regex_values.get("hex") and group_regex_values.get("company"):
                    OUI_MAPPINGS.update({group_regex_values.get("hex").lower(): group_regex_values.get("company")})

    with open(sys.argv[1], "w", encoding="utf-8") as oui_mappings:
        json.dump(OUI_MAPPINGS, oui_mappings, indent=2)
