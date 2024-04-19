"""Python code used to postprocess Flat github action data related to Protocol mappings."""

import csv
import os
import sys
from urllib.request import urlopen


if __name__ == "__main__":
    if len(sys.argv) == 2:
        URL = "https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.csv"
        oui_textfile = urlopen(URL).read().decode("utf-8")  # nosec: pylint: disable=consider-using-with
        with open(sys.argv[1], "w", encoding="utf-8") as proto_mappings:
            proto_mappings.write(oui_textfile)

    protocol_mapping = {}
    with open(sys.argv[1], encoding="utf-8") as file:
        next(file)
        reader = csv.reader(file)
        for row in reader:
            name = row[0]
            port = row[1]
            protocol = row[2]
            if not port.isnumeric():
                continue
            if name and port and protocol:
                if protocol_mapping.get(name) and protocol_mapping[name]["port_number"] != int(port):
                    name = name + "-secondary"
                if not protocol_mapping.get(name):
                    protocol_mapping[name] = {"port_number": int(port), "protocols": []}
                protocol_mapping[name]["protocols"].append(protocol)

    with open(sys.argv[1], "w", encoding="utf-8") as proto_mappings:
        proto_mappings.write('"""Dictionary object to store Protocol information."""\n')
        proto_mappings.write("# pylint: disable=too-many-lines\n")
        proto_mappings.write("from typing import Any, Dict\n\n")
        proto_mappings.write(f"PROTOCOLS: Dict[str, Any] = {protocol_mapping}")

    os.system(f"black {sys.argv[1]}")  # nosec
