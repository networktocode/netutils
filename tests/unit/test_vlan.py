"""Test for the VLAN functions."""
import os
import glob

import pytest

from netutils import vlan

MOCK_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "mock", "vlan")
JSON_FILE = "_sent.json"
TXT_FILE = "_sent.txt"


@pytest.mark.parametrize("_file", glob.glob(f"{MOCK_DIR}/to_config/*{JSON_FILE}"))
def test_to_config_success(_file, get_json_data):
    truncate_file = os.path.join(MOCK_DIR, _file[: -len(JSON_FILE)])

    sent_data = get_json_data(os.path.join(MOCK_DIR, _file))
    received_data = get_json_data(truncate_file + "_received.json")
    assert vlan.vlanlist_to_config(**sent_data) == received_data


@pytest.mark.parametrize("sent_data", [{"vlan_list": [4095]}, {"vlan_list": [0]}])
def test_to_config_failure(sent_data):
    with pytest.raises(ValueError, match=r"Valid VLAN range*"):
        vlan.vlanlist_to_config(**sent_data)
    with pytest.raises(ValueError, match="Minimum grouping size must be equal to or greater than one."):
        vlan.vlanlist_to_config("switchport trunk allowed vlan 1025,1069-1072", min_grouping_size=0)


@pytest.mark.parametrize("_file", glob.glob(f"{MOCK_DIR}/to_list/*{TXT_FILE}"))
def test_to_list_success(_file, get_text_data, get_json_data):
    truncate_file = os.path.join(MOCK_DIR, _file[: -len(TXT_FILE)])

    sent_data = get_text_data(os.path.join(MOCK_DIR, _file))
    received_data = get_json_data(truncate_file + "_received.json")
    assert vlan.vlanconfig_to_list(sent_data) == received_data


def test_to_list_failure():
    with pytest.raises(ValueError, match=r"Valid VLAN range*"):
        vlan.vlanconfig_to_list("switchport trunk allowed vlan 1025,1069-1072,4099")
    with pytest.raises(ValueError, match=r"There were non-digits and dashes*"):
        vlan.vlanconfig_to_list("switchport trunk allowed vlan 1025,1069-1072,BADDATA")
    with pytest.raises(ValueError, match=r"No digits found in `switchport trunk allowed vlan BADDATA`"):
        vlan.vlanconfig_to_list("switchport trunk allowed vlan BADDATA")
