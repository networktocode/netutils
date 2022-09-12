import sys
import re
import json

from Sandbox.p.p10 import OUI_MAPPINGS

hex_re = r"^(?P<hex>[A-Fa-f0-9]{6})\s+\(.*\)[^a-zA-Z0-9]+(?P<company>.*)$"
OUI_MAPPINGS = {}

if __name__ == "__main__":
    with open(sys.argv[1], "r") as oui_file:
        for line in oui_file:
            if re.search(hex_re, line):
                group_regex_values = re.search(hex_re, line).groupdict()
                if group_regex_values.get("hex") and group_regex_values.get("company"):
                    OUI_MAPPINGS.update({group_regex_values.get("hex"): group_regex_values.get("company")})

    with open(sys.argv[1], "w") as oui_mappings:
        json.dump(OUI_MAPPINGS, oui_mappings, indent=4)
