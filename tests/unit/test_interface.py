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

INTERFACE_EXPANSION = [
    {"sent": "Ethernet0/[1-4]", "received": ["Ethernet0/1", "Ethernet0/2", "Ethernet0/3", "Ethernet0/4"]},
    {
        "sent": "GigabitEthernet[1,2]/0/[1-10]",
        "received": [
            "GigabitEthernet1/0/1",
            "GigabitEthernet1/0/2",
            "GigabitEthernet1/0/3",
            "GigabitEthernet1/0/4",
            "GigabitEthernet1/0/5",
            "GigabitEthernet1/0/6",
            "GigabitEthernet1/0/7",
            "GigabitEthernet1/0/8",
            "GigabitEthernet1/0/9",
            "GigabitEthernet1/0/10",
            "GigabitEthernet2/0/1",
            "GigabitEthernet2/0/2",
            "GigabitEthernet2/0/3",
            "GigabitEthernet2/0/4",
            "GigabitEthernet2/0/5",
            "GigabitEthernet2/0/6",
            "GigabitEthernet2/0/7",
            "GigabitEthernet2/0/8",
            "GigabitEthernet2/0/9",
            "GigabitEthernet2/0/10",
        ],
    },
    {
        "sent": "FortyGig[1,2]/[4-6]/[8-10]",
        "received": [
            "FortyGig1/4/8",
            "FortyGig1/4/9",
            "FortyGig1/4/10",
            "FortyGig1/5/8",
            "FortyGig1/5/9",
            "FortyGig1/5/10",
            "FortyGig1/6/8",
            "FortyGig1/6/9",
            "FortyGig1/6/10",
            "FortyGig2/4/8",
            "FortyGig2/4/9",
            "FortyGig2/4/10",
            "FortyGig2/5/8",
            "FortyGig2/5/9",
            "FortyGig2/5/10",
            "FortyGig2/6/8",
            "FortyGig2/6/9",
            "FortyGig2/6/10",
        ],
    },
    {"sent": "Gi1", "received": ["Gi1"]},
    {"sent": "Gi[1,3-5]", "received": ["Gi1", "Gi3", "Gi4", "Gi5"]},
    {"sent": "Gi[1,3-5,8]", "received": ["Gi1", "Gi3", "Gi4", "Gi5", "Gi8"]},
    {"sent": "[1,2]/0/[1-2]", "received": ["1/0/1", "1/0/2", "2/0/1", "2/0/2"]},
]

INTERFACE_SORT = [
    {"sent": [], "received": []},
    {"sent": ["Fa0/0/1.200", "Fa0/0/1.200", "Fa0/0/1.200"], "received": ["Fa0/0/1.200"]},
    {
        "sent": [
            "Fa0/0/2.200",
            "Fa1/0/1.100",
            "Fa1/0.100",
            "Gi1/1",
            "Gi0/1",
            "Gi0/0/1",
            "Gi1/0/2",
            "Vlan42",
            "Te/42",
            "loopback99",
            "Port-channel75",
            "Gi1/0/1",
            "Fa0/0/2",
            "Fa0/0/1",
            "Fa0/0/1.101",
            "Fa0/0/1.100",
            "Fa0/0/1.10",
            "Fa0/0/1.500",
            "Fa0/0/1.999",
            "Gi/42",
            "Loopback101",
            "Loopback102",
            "Loopback98",
            "Loopback99",
            "Port-channel160",
            "Port-channel40",
            "Fa0/0/1.4",
            "Fa42",
            "Gi1/0/3",
            "Gi1/0/3.100",
            "Fa1",
            "Gi1/0/2",
            "Gi1/0/2.50",
            "Zf.42",
            "Fa1.42",
            "Po40",
            "Po160",
            "Lo10",
            "Fa1/42",
            "Gi0/0/2",
            "Gi1/0/1",
            "Te1/0/1",
        ],
        "received": [
            "Fa0/0/1",
            "Fa0/0/1.4",
            "Fa0/0/1.10",
            "Fa0/0/1.100",
            "Fa0/0/1.101",
            "Fa0/0/1.500",
            "Fa0/0/1.999",
            "Fa0/0/2",
            "Fa0/0/2.200",
            "Fa1",
            "Fa1.42",
            "Fa1/0.100",
            "Fa1/0/1.100",
            "Fa1/42",
            "Fa42",
            "Gi0/0/1",
            "Gi0/0/2",
            "Gi0/1",
            "Gi1/0/1",
            "Gi1/0/2",
            "Gi1/0/2.50",
            "Gi1/0/3",
            "Gi1/0/3.100",
            "Gi1/1",
            "Gi/42",
            "Lo10",
            "Loopback98",
            "Loopback99",
            "Loopback101",
            "Loopback102",
            "Po40",
            "Po160",
            "Port-channel40",
            "Port-channel75",
            "Port-channel160",
            "Te1/0/1",
            "Te/42",
            "Vlan42",
            "Zf.42",
            "loopback99",
        ],
    },
]

BAD_INTERFACE_NAMES = [
    "fa?",
    "Gi1^",
    "Fa0/0*/42",
    "Te42/55.32/77@99",
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


@pytest.mark.parametrize("data", INTERFACE_EXPANSION)
def test_interface_range_expansion(data):
    assert interface.interface_range_expansion(data["sent"]) == data["received"]


@pytest.mark.parametrize("data", BAD_INTERFACE_NAMES)
def test_split_interface_tuple_fails(data):
    with pytest.raises(ValueError):
        interface.split_interface_tuple(data)


def test_interface_sort_empty():
    assert interface.sort_interface_list([]) == []


@pytest.mark.parametrize("data", INTERFACE_SORT)
def test_interface_sort_prune(data):
    """Assert that duplicate nodes are pruned from the tree."""
    assert set(interface.sort_interface_list(data["sent"])) == set(data["received"])


@pytest.mark.parametrize("data", INTERFACE_SORT)
def test_interface_sort_order(data):
    """Assert that the tree iterates in canonical order."""
    assert interface.sort_interface_list(data["sent"]) == data["received"]
