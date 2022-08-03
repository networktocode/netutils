"""Test for the network os parser functions."""
import glob
import os

import pytest
from netutils.config import compliance
from netutils.config.parser import IOSConfigParser

MOCK_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "mock", "config", "parser")
TXT_FILE = "_sent.txt"

parameters = []
for network_os in list(compliance.parser_map.keys()):
    for _file in glob.glob(f"{MOCK_DIR}/{network_os}/*{TXT_FILE}"):
        parameters.append([_file, network_os])


# TODO: add more tests with different patterns
get_path_parameters = [
    ("get_path/ios_full_config.txt", "crypto pki", "get_path/certificate_wo_parents.txt"),
]

get_path_with_parents_parameters = [
    ("get_path/ios_full_config.txt", "crypto pki", "get_path/certificate_with_parents.txt"),
]


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


@pytest.mark.parametrize("_file, pattern, expected", get_path_parameters)
def test_get_path(_file, pattern, expected, get_text_data):
    """Tests get_path method."""
    device_cfg = get_text_data(os.path.join(MOCK_DIR, _file))
    config_tree = IOSConfigParser(str(device_cfg))
    returned_path = config_tree.get_path(pattern)
    expected_path = get_text_data(os.path.join(MOCK_DIR, expected))

    assert returned_path == expected_path.split("\n")


@pytest.mark.parametrize("_file, pattern, expected", get_path_with_parents_parameters)
def test_get_path_with_children(_file, pattern, expected, get_text_data):
    """Tests get_path_with_children method."""
    device_cfg = get_text_data(os.path.join(MOCK_DIR, _file))
    config_tree = IOSConfigParser(str(device_cfg))
    returned_path = config_tree.get_path_with_parents(pattern)
    expected_path = get_text_data(os.path.join(MOCK_DIR, expected))

    assert returned_path == expected_path.split("\n")
