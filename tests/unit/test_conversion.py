"""Test that configurations properly convert from undesired format to desired"""
import glob
import os

import pytest
from netutils.config import conversion

MOCK_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "mock", "config", "conversion")

TXT_FILE = "_sent.txt"
CONVERTED_FILE = "_converted.txt"

conversion_files = []

for network_os in list(conversion.parser_map.keys()):
    for _file in glob.glob(f"{MOCK_DIR}/config/conversion/{network_os}/*{TXT_FILE}"):
        conversion_files.append([_file, network_os])


@pytest.mark.parametrize("_file, network_os", conversion_files)
def test_config_conversion(_file, get_text_data):  # pylint: disable=redefined-outer-name
    truncate_file = os.path.join(MOCK_DIR, _file[: -len(TXT_FILE)])

    sent_cfg = get_text_data(os.path.join(MOCK_DIR, _file))
    converted_cfg = conversion.paloalto_panos_brace_to_set(sent_cfg)
    received_data = get_text_data(truncate_file + "_converted.txt")
    assert converted_cfg == received_data
