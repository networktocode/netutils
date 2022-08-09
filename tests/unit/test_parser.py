"""Test for the network os parser functions."""
import glob
import os

import pytest
from netutils.config import compliance
from netutils.config.parser import IOSConfigParser

MOCK_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "mock", "config", "parser")
MOCK_GETPATH_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "mock", "config", "parser", "find_children"
)
TXT_FILE = "_sent.txt"
CONFIG_FILE = "full_config.txt"

parameters = []
for network_os in list(compliance.parser_map.keys()):
    for _file in glob.glob(f"{MOCK_DIR}/{network_os}/*{TXT_FILE}"):
        parameters.append([_file, network_os])


find_all_children_parameters = []
find_all_children_test_cases = [
    ("crypto pki", "certificate.txt"),
]
for network_os in list(compliance.parser_map.keys()):
    for _file in glob.glob(f"{MOCK_GETPATH_DIR}/{network_os}/{CONFIG_FILE}"):
        for test_case in find_all_children_test_cases:
            find_all_children_parameters.append(
                (_file, test_case[0], f"{MOCK_GETPATH_DIR}/{network_os}/{test_case[1]}")
            )

find_children_parents_parameters = []
find_children_parents_test_cases = [
    ("interface", " no ip", "interface.txt"),
]
for network_os in list(compliance.parser_map.keys()):
    for _file in glob.glob(f"{MOCK_GETPATH_DIR}/{network_os}/{CONFIG_FILE}"):
        for test_case in find_children_parents_test_cases:
            find_children_parents_parameters.append(
                (_file, test_case[0], test_case[1], f"{MOCK_GETPATH_DIR}/{network_os}/{test_case[2]}")
            )


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


@pytest.mark.parametrize("_file, pattern, expected", find_all_children_parameters)
def test_find_all_children(_file, pattern, expected, get_text_data):
    """Tests get_path method."""
    device_cfg = get_text_data(os.path.join(MOCK_DIR, _file))
    config_tree = IOSConfigParser(str(device_cfg))
    returned_path = config_tree.find_all_children(pattern=pattern, match_type="regex")
    expected_path = get_text_data(os.path.join(MOCK_DIR, expected))

    assert returned_path == expected_path.split("\n")


@pytest.mark.parametrize("_file, parent_pattern, child_pattern, expected", find_children_parents_parameters)
def test_find_children_w_parents(_file, parent_pattern, child_pattern, expected, get_text_data):
    """Tests get_path_with_children method."""
    device_cfg = get_text_data(os.path.join(MOCK_DIR, _file))
    config_tree = IOSConfigParser(str(device_cfg))
    returned_path = config_tree.find_children_w_parents(
        parent_pattern=parent_pattern, child_pattern=child_pattern, match_type="regex"
    )
    expected_path = get_text_data(os.path.join(MOCK_DIR, expected))

    assert returned_path == expected_path.split("\n")
