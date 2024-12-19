"""Test for the network os parser functions."""

import glob
import os

import pytest

from netutils.config import compliance

MOCK_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "mock", "config", "parser"
)
TXT_FILE = "_sent.txt"

base_parameters = []
find_all_children_parameters = []
find_children_w_parents_parameters = []
for network_os in list(compliance.parser_map.keys()):
    for _file in glob.glob(f"{MOCK_DIR}/base/{network_os}/*{TXT_FILE}"):
        base_parameters.append([_file, network_os])
    for _file in glob.glob(f"{MOCK_DIR}/find_all_children/{network_os}/*{TXT_FILE}"):
        find_all_children_parameters.append([_file, network_os])
    for _file in glob.glob(
        f"{MOCK_DIR}/find_children_w_parents/{network_os}/*{TXT_FILE}"
    ):
        find_children_w_parents_parameters.append([_file, network_os])


@pytest.mark.parametrize("_file, network_os", base_parameters)
def test_parser(_file, network_os, get_text_data, get_python_data):  # pylint: disable=redefined-outer-name
    truncate_file = os.path.join(MOCK_DIR, "base", _file[: -len(TXT_FILE)])

    device_cfg = get_text_data(os.path.join(MOCK_DIR, "base", _file))
    received_data = get_python_data(truncate_file + "_received.py", "data")
    os_parser = compliance.parser_map[network_os]
    assert os_parser(device_cfg).config_lines == received_data


@pytest.mark.parametrize("_file, network_os", find_all_children_parameters)
def test_find_all_children(_file, network_os, get_text_data, get_json_data):  # pylint: disable=redefined-outer-name
    truncate_file = os.path.join(MOCK_DIR, "find_all_children", _file[: -len(TXT_FILE)])

    device_cfg = get_text_data(os.path.join(MOCK_DIR, "find_all_children", _file))
    received_data = get_text_data(
        os.path.join(MOCK_DIR, "find_all_children", truncate_file + "_received.txt")
    )
    kwargs = get_json_data(truncate_file + "_args.json")
    os_parser = compliance.parser_map[network_os]
    assert "\n".join(os_parser(device_cfg).find_all_children(**kwargs)) == received_data


@pytest.mark.parametrize("_file, network_os", find_children_w_parents_parameters)
def test_find_children_w_parents(_file, network_os, get_text_data, get_json_data):  # pylint: disable=redefined-outer-name
    truncate_file = os.path.join(
        MOCK_DIR, "find_children_w_parents", _file[: -len(TXT_FILE)]
    )

    device_cfg = get_text_data(os.path.join(MOCK_DIR, "find_children_w_parents", _file))
    received_data = get_text_data(
        os.path.join(
            MOCK_DIR, "find_children_w_parents", truncate_file + "_received.txt"
        )
    )
    kwargs = get_json_data(truncate_file + "_args.json")
    os_parser = compliance.parser_map[network_os]
    assert (
        "\n".join(os_parser(device_cfg).find_children_w_parents(**kwargs))
        == received_data
    )


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


def test_duplicate_line():
    logging = (
        "!\n"
        "snmp-server community <<REPLACED>> RO SNMP_ACL_RO\n"
        "snmp-server community <<REPLACED>> RO SNMP_ACL_RO\n"
        "snmp-server community <<REPLACED>> RW SNMP_ACL_RW\n"
    )
    with pytest.raises(
        IndexError, match=r".*This error is likely from a duplicate line detected.*"
    ):
        compliance.parser_map["cisco_ios"](logging).config_lines  # pylint: disable=expression-not-assigned


# def test_nested_banner():
#     banner: str = (
#         "group-policy Grs-POLICY attributes\n" " banner value This is an\n" " banner value example nested banner.\n"
#     )

#     generated_config_lines: list[ConfigLine] = compliance.parser_map["cisco_asa"](
#         banner,
#     ).config_lines

#     parent: str = "group-policy Grs-POLICY attributes"
#     mock_config_lines: list[ConfigLine] = [
#         ConfigLine(config_line=parent, parents=()),
#         ConfigLine(config_line=" banner value This is an", parents=(parent,)),
#         ConfigLine(config_line=" banner value example nested banner.", parents=(parent,)),
#     ]
#     assert generated_config_lines == mock_config_lines
