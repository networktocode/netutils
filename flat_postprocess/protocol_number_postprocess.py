"""Python code used to postprocess Flat github action data related to Protocol mappings."""

import csv
import os
import sys
from urllib.request import urlopen

if __name__ == "__main__":
    if len(sys.argv) == 2:
        URL = "https://www.iana.org/assignments/protocol-numbers/protocol-numbers-1.csv"
        oui_textfile = urlopen(URL).read().decode("utf-8")  # noqa: S310 pylint: disable=consider-using-with
        with open(sys.argv[1], "w", encoding="utf-8") as proto_mappings:
            proto_mappings.write(oui_textfile)

    protocol_mapping = {}
    reverse_mapping = {}
    with open(sys.argv[1], encoding="utf-8") as file:
        next(file)
        reader = csv.reader(file)
        for row in reader:
            number = row[0]
            name = row[1]
            if not number.isnumeric():
                continue
            if not name:
                continue
            name = name.replace(" (deprecated)", "")
            protocol_mapping[name] = int(number)
            reverse_mapping[int(number)] = name

    with open(sys.argv[1], "w", encoding="utf-8") as proto_mappings:
        proto_mappings.write('"""Dictionary object to store Protocol Number."""\n')
        proto_mappings.write("from typing import Dict\n")
        proto_mappings.write(f"PROTO_NAME_TO_NUM: Dict[str, int] = {protocol_mapping}")
        proto_mappings.write("\n")
        proto_mappings.write(f"PROTO_NUM_TO_NAME: Dict[int, str] = {reverse_mapping}")

    os.system(f"ruff format {sys.argv[1]}")  # noqa: S605
