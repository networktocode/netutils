"""Test for the network os parser functions."""
import glob
import os

import pytest
from netutils.config import compliance

MOCK_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "mock", "config", "parser")
TXT_FILE = "_sent.txt"

parameters = []
for network_os in list(compliance.parser_map.keys()):
    for _file in glob.glob(f"{MOCK_DIR}/{network_os}/*{TXT_FILE}"):
        parameters.append([_file, network_os])


@pytest.mark.parametrize("_file, network_os", parameters)
def test_parser(_file, network_os, get_text_data, get_python_data):  # pylint: disable=redefined-outer-name
    truncate_file = os.path.join(MOCK_DIR, _file[: -len(TXT_FILE)])

    device_cfg = get_text_data(os.path.join(MOCK_DIR, _file))
    received_data = get_python_data(truncate_file + "_received.py", "data")
    os_parser = compliance.parser_map[network_os]
    assert os_parser(device_cfg).config_lines == received_data


def test_incorrect_banner_ios():
    banner_cfg = (
        "aaa new-model\n"
        "!\n"
        "banner exec $\n"
        "**************************************************************************\n"
        "* IOSv is strictly limited to use for evaluation, demonstration and IOS.  *\n"
        "**************************************************************************c\n"
        "!\n"
        "ip route 0.0.0.0 0.0.0.0 192.168.1.1\n"
    )
    with pytest.raises(ValueError):
        compliance.parser_map["cisco_ios"](banner_cfg).config_lines  # pylint: disable=expression-not-assigned
