"""Test for the interface functions."""
import pytest

from netutils import interface

SPLIT_INTERFACE = [
    {"sent": {"interface": "GigabitEthernet1/0/1"}, "received": ("GigabitEthernet", "1/0/1")},
    {
        "sent": {"interface": "GigabitEthernet 1/0/1"},
        "received": ("GigabitEthernet", "1/0/1"),
    },
    {"sent": {"interface": "Gi1/0/1"}, "received": ("Gi", "1/0/1")},
]

CANONICAL_INTERFACE_NAME = [
    {
        "sent": {"interface": "GigabitEthernet1/0/1"},
        "received": "GigabitEthernet1/0/1",
    },
    {"sent": {"interface": "Gi1/0/1"}, "received": "GigabitEthernet1/0/1"},
    {
        "sent": {"interface": "SuperFastEth 1/0/1", "addl_name_map": {"SuperFastEth": "SuperFastEthernet"}},
        "received": "SuperFastEthernet1/0/1",
    },
    {"sent": {"interface": "Noninterface1/0/1"}, "received": "Noninterface1/0/1"},
]

ABBREVIATED_INTERFACE_NAME = [
    {
        "sent": {"interface": "GigabitEthernet1/0/1"},
        "received": "Gi1/0/1",
    },
    {"sent": {"interface": "Gi1/0/1"}, "received": "Gi1/0/1"},
    {
        "sent": {
            "interface": "SuperFastEth 1/0/1",
            "addl_name_map": {"SuperFastEth": "SuperFastEthernet"},
            "addl_reverse_map": {"SuperFastEthernet": "SupE"},
        },
        "received": "SupE1/0/1",
    },
    {"sent": {"interface": "Noninterface1/0/1"}, "received": "Noninterface1/0/1"},
]


@pytest.mark.parametrize("data", SPLIT_INTERFACE)
def test_split_interface(data):
    assert interface.split_interface(**data["sent"]) == data["received"]


@pytest.mark.parametrize("data", CANONICAL_INTERFACE_NAME)
def test_canonical_interface_name(data):
    assert interface.canonical_interface_name(**data["sent"]) == data["received"]


def test_canonical_interface_name_failure():
    with pytest.raises(ValueError, match=r"Verify interface on and no match found for*"):
        data = {"interface": "SuperFastEth 1/0/1", "verify": True}
        interface.canonical_interface_name(**data)


@pytest.mark.parametrize("data", ABBREVIATED_INTERFACE_NAME)
def test_abbreviated_interface_name(data):
    assert interface.abbreviated_interface_name(**data["sent"]) == data["received"]


def test_abbreviated_interface_name_failure():
    with pytest.raises(ValueError, match=r"Verify interface on and no match found for*"):
        data = {"interface": "SuperFastEth 1/0/1", "verify": True}
        interface.abbreviated_interface_name(**data)
