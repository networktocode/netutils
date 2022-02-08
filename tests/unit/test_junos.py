"""Test for the Junos functions."""
import pytest

from netutils.junos import junos_list

LIST_TO_JUNOS_SYNTAX = [
    {"sent": ["VLAN1", "VLAN2", "VLAN3", "VLAN4"], "received": "[ VLAN1 VLAN2 VLAN3 VLAN4 ]"},
    {"sent": ["VLAN1", "VLAN1", "VLAN2", "VLAN3", "VLAN4"], "received": "[ VLAN1 VLAN2 VLAN3 VLAN4 ]"},
    {"sent": ["VLAN1"], "received": "VLAN1"},
    {
        "sent": [
            # fmt: off
            '\"chacha20-poly1305@openssh.com\"',
            '\"aes256-gcm@openssh.com\"',
            '\"aes128-gcm@openssh.com\"',
            # fmt: on
            "aes256-ctr",
            "aes192-ctr",
            "aes128-ctr",
        ],
        "received": '[ "chacha20-poly1305@openssh.com" "aes256-gcm@openssh.com" "aes128-gcm@openssh.com" aes256-ctr aes192-ctr aes128-ctr ]',
    },
]


@pytest.mark.parametrize("data", LIST_TO_JUNOS_SYNTAX)
def test_junos_list(data):
    print(data["sent"], data["received"])
    assert junos_list(data["sent"]) == data["received"]