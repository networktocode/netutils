"""Python code used to postprocess Flat github action data related to OUI mappings."""
import sys
import re

HEX_RE = r"^(?P<hex>[A-Fa-f0-9]{6})\s+\(.*\)[^a-zA-Z0-9]+(?P<company>.*)$"
OUI_MAPPINGS = {}

if __name__ == "__main__":
    with open(sys.argv[1], "r", encoding="utf-8") as oui_file:
        for line in oui_file:
            if re.search(HEX_RE, line):
                group_regex_values = re.search(HEX_RE, line).groupdict()
                if group_regex_values.get("hex") and group_regex_values.get("company"):
                    OUI_MAPPINGS.update({group_regex_values.get("hex").lower(): group_regex_values.get("company")})

    with open(sys.argv[1], "w", encoding="utf-8") as oui_mappings:
        oui_mappings.write('"""Dictionary object to store OUI information."""\n')
        oui_mappings.write("# pylint: disable=too-many-lines")
        oui_mappings.write("import typing\n\n")
        oui_mappings.write("OUI_MAPPINGS: typing.Dict[str, str] = {\n")
        for mac, company in OUI_MAPPINGS.items():
            oui_mappings.write(f'    "{mac}": "{company}",\n')
        oui_mappings.write("}\n")
