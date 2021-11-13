"""Test for the config compliance functions."""
import glob
import os

import pytest
from netutils.config import compliance

MOCK_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "mock", "config", "compliance")

TXT_FILE = "_sent.txt"
INTEND_FILE = "_intended.txt"

section_config_parameters = []
config_section_not_parsed_parameters = []
diff_network_config_parameters = []
compliance_parameters = []
config_section_not_parsed_parameters = []

for network_os in list(compliance.parser_map.keys()):
    for _file in glob.glob(f"{MOCK_DIR}/section/{network_os}/*{TXT_FILE}"):
        section_config_parameters.append([_file, network_os])
    for _file in glob.glob(f"{MOCK_DIR}/compliance/{network_os}/*{INTEND_FILE}"):
        compliance_parameters.append([_file, network_os])
    for _file in glob.glob(f"{MOCK_DIR}/diff_network_config/{network_os}/*{INTEND_FILE}"):
        diff_network_config_parameters.append([_file, network_os])
    for _file in glob.glob(f"{MOCK_DIR}/config_section_not_parsed/{network_os}/*{TXT_FILE}"):
        config_section_not_parsed_parameters.append([_file, network_os])


@pytest.mark.parametrize("_file, network_os", section_config_parameters)
def test_section_config(_file, network_os, get_text_data, get_python_data):  # pylint: disable=redefined-outer-name
    truncate_file = os.path.join(MOCK_DIR, _file[: -len(TXT_FILE)])

    device_cfg = get_text_data(os.path.join(MOCK_DIR, _file))
    received_data = get_text_data(truncate_file + "_received.txt")
    feature = get_python_data(truncate_file + "_feature.py", "feature")
    assert compliance.section_config(feature, device_cfg, network_os) == received_data


@pytest.mark.parametrize("_file, network_os", compliance_parameters)
def test_compliance(
    _file, network_os, get_json_data, get_text_data, get_python_data
):  # pylint: disable=redefined-outer-name
    truncate_file = os.path.join(MOCK_DIR, _file[: -len(INTEND_FILE)])

    intended_cfg = get_text_data(os.path.join(MOCK_DIR, _file))
    backup_cfg = get_text_data(truncate_file + "_backup.txt")
    received_data = get_json_data(truncate_file + "_received.json")
    features = get_python_data(truncate_file + "_feature.py", "features")
    assert compliance.compliance(features, backup_cfg, intended_cfg, network_os, "string") == received_data


@pytest.mark.parametrize("_file, network_os", diff_network_config_parameters)
def test_diff_network_config(_file, network_os, get_text_data):  # pylint: disable=redefined-outer-name
    truncate_file = os.path.join(MOCK_DIR, _file[: -len(INTEND_FILE)])

    compare_config = get_text_data(os.path.join(MOCK_DIR, _file))
    base_config = get_text_data(truncate_file + "_base.txt")
    received_data = get_text_data(truncate_file + "_received.txt")
    assert compliance.diff_network_config(compare_config, base_config, network_os) == received_data


@pytest.mark.parametrize("_file", glob.glob(f"{MOCK_DIR}/find_unordered_cfg_lines/*{INTEND_FILE}"))
def test_find_unordered_cfg_lines(_file, get_text_data, get_python_data):
    truncate_file = os.path.join(MOCK_DIR, _file[: -len(INTEND_FILE)])

    intended_config = get_text_data(os.path.join(MOCK_DIR, _file))
    actual_config = get_text_data(truncate_file + "_actual.txt")
    received_data = get_python_data(truncate_file + "_received.py", "data")
    assert compliance.find_unordered_cfg_lines(intended_config, actual_config) == received_data


@pytest.mark.parametrize("_file, network_os", config_section_not_parsed_parameters)
def test_config_section_not_parsed(
    _file, network_os, get_json_data, get_text_data, get_python_data
):  # pylint: disable=redefined-outer-name
    truncate_file = os.path.join(MOCK_DIR, _file[: -len(TXT_FILE)])

    device_cfg = get_text_data(os.path.join(MOCK_DIR, _file))
    received_data = get_json_data(truncate_file + "_received.json")
    features = get_python_data(truncate_file + "_feature.py", "features")
    assert compliance.config_section_not_parsed(features, device_cfg, network_os) == received_data


def test_incorrect_cfg_type():
    with pytest.raises(ValueError):
        compliance.compliance({}, "backup_cfg", "intended_cfg", "cisco_ios", "text")
