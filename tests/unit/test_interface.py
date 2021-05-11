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

CANONICAL_INTERFACE_NAME_LIST = [
    {
        "sent": {"interfaces": ["GigabitEthernet1/0/1", "GigabitEthernet1/0/2"]},
        "received": ["GigabitEthernet1/0/1", "GigabitEthernet1/0/2"],
    },
    {
        "sent": {"interfaces": ["Gi1/0/1", "Po40", "Lo10"]},
        "received": ["GigabitEthernet1/0/1", "Port-channel40", "Loopback10"],
    },
    {
        "sent": {"interfaces": ["Gi1/0/1", "Gi1/0/3", "Gi1/0/2", "Po40", "Po160", "Lo10"], "order": "alphabetical"},
        "received": [
            "GigabitEthernet1/0/1",
            "GigabitEthernet1/0/2",
            "GigabitEthernet1/0/3",
            "Loopback10",
            "Port-channel40",
            "Port-channel160",
        ],
    },
    {
        "sent": {
            "interfaces": ["Gi1/0/1", "Gi1/0/3", "Gi1/0/3.100", "Gi1/0/2", "Gi1/0/2.50", "Po40", "Po160", "Lo10"],
            "order": "alphabetical",
        },
        "received": [
            "GigabitEthernet1/0/1",
            "GigabitEthernet1/0/2",
            "GigabitEthernet1/0/2.50",
            "GigabitEthernet1/0/3",
            "GigabitEthernet1/0/3.100",
            "Loopback10",
            "Port-channel40",
            "Port-channel160",
        ],
    },
    {
        "sent": {
            "interfaces": ["Gi1/0/1", "Gi1/0/3", "Gi1/0/2", "Po40", "Po160", "Lo10"],
            "order": "alphabetical",
            "reverse": True,
        },
        "received": [
            "Port-channel40",
            "Port-channel160",
            "Loopback10",
            "GigabitEthernet1/0/1",
            "GigabitEthernet1/0/2",
            "GigabitEthernet1/0/3",
        ],
    },
    {
        "sent": {
            "interfaces": ["Gi1/0/1", "Gi1/0/3", "Gi1/0/3.100", "Gi1/0/2", "Gi1/0/2.50", "Po40", "Po160", "Lo10"],
            "order": "alphabetical",
            "reverse": True,
        },
        "received": [
            "Port-channel40",
            "Port-channel160",
            "Loopback10",
            "GigabitEthernet1/0/1",
            "GigabitEthernet1/0/2",
            "GigabitEthernet1/0/2.50",
            "GigabitEthernet1/0/3",
            "GigabitEthernet1/0/3.100",
        ],
    },
    {
        "sent": {
            "interfaces": ["SuperFastEth 1/0/1", "SuperFastEth 1/0/2"],
            "addl_name_map": {"SuperFastEth": "SuperFastEthernet"},
        },
        "received": ["SuperFastEthernet1/0/1", "SuperFastEthernet1/0/2"],
    },
    {
        "sent": {"interfaces": ["Noninterface1/0/1", "Noninterface1/0/2"]},
        "received": ["Noninterface1/0/1", "Noninterface1/0/2"],
    },
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

ABBREVIATED_INTERFACE_NAME_LIST = [
    {
        "sent": {"interfaces": ["Gi1/0/1", "Gi1/0/2"]},
        "received": ["Gi1/0/1", "Gi1/0/2"],
    },
    {
        "sent": {"interfaces": ["GigabitEthernet1/0/1", "Po40", "Loopback10"]},
        "received": ["Gi1/0/1", "Po40", "Lo10"],
    },
    {
        "sent": {
            "interfaces": [
                "GigabitEthernet1/0/1",
                "GigabitEthernet1/0/3",
                "GigabitEthernet1/0/2",
                "Loopback10",
                "Port-channel160",
                "Port-channel40",
            ],
            "order": "alphabetical",
        },
        "received": ["Gi1/0/1", "Gi1/0/2", "Gi1/0/3", "Lo10", "Po40", "Po160"],
    },
    {
        "sent": {
            "interfaces": [
                "GigabitEthernet1/0/1",
                "GigabitEthernet1/0/3",
                "GigabitEthernet1/0/3.100",
                "GigabitEthernet1/0/2",
                "GigabitEthernet1/0/2.50",
                "Loopback10",
                "Port-channel160",
                "Port-channel40",
            ],
            "order": "alphabetical",
        },
        "received": ["Gi1/0/1", "Gi1/0/2", "Gi1/0/2.50", "Gi1/0/3", "Gi1/0/3.100", "Lo10", "Po40", "Po160"],
    },
    {
        "sent": {
            "interfaces": [
                "GigabitEthernet1/0/1",
                "GigabitEthernet1/0/3",
                "GigabitEthernet1/0/2",
                "Loopback10",
                "Port-channel160",
                "Port-channel40",
            ],
            "order": "alphabetical",
            "reverse": True,
        },
        "received": ["Po40", "Po160", "Lo10", "Gi1/0/1", "Gi1/0/2", "Gi1/0/3"],
    },
    {
        "sent": {
            "interfaces": [
                "GigabitEthernet1/0/1",
                "GigabitEthernet1/0/3",
                "GigabitEthernet1/0/3.100",
                "GigabitEthernet1/0/2",
                "GigabitEthernet1/0/2.50",
                "Loopback10",
                "Port-channel160",
                "Port-channel40",
            ],
            "order": "alphabetical",
            "reverse": True,
        },
        "received": [
            "Po40",
            "Po160",
            "Lo10",
            "Gi1/0/1",
            "Gi1/0/2",
            "Gi1/0/2.50",
            "Gi1/0/3",
            "Gi1/0/3.100",
        ],
    },
    {
        "sent": {
            "interfaces": ["SuperFastEthernet1/0/1", "SuperFastEthernet1/0/2"],
            "addl_name_map": {"SupFaEth": "SuperFastEthernet"},
            "addl_reverse_map": {"SuperFastEthernet": "SupFaEth"},
        },
        "received": ["SupFaEth1/0/1", "SupFaEth1/0/2"],
    },
    {
        "sent": {"interfaces": ["Noninterface1/0/1", "Noninterface1/0/2"]},
        "received": ["Noninterface1/0/1", "Noninterface1/0/2"],
    },
]

ORDERED_INTERFACE_NAME_LIST = [
    {
        "sent": {
            "interfaces": [
                "FastEthernet0/0",
                "GigabitEthernet0/0",
                "FortyGigabitEthernet0/0",
                "HundredGigabitEthernet0/0",
                "FourHundredGigabitEthernet0/0",
                "Loopback0/0",
                "Ethernet0/0",
            ]
        },
        "received": [
            "Ethernet0/0",
            "FastEthernet0/0",
            "FortyGigabitEthernet0/0",
            "FourHundredGigabitEthernet0/0",
            "GigabitEthernet0/0",
            "HundredGigabitEthernet0/0",
            "Loopback0/0",
        ],
    },
    {
        "sent": {
            "interfaces": [
                "FastEthernet1/1",
                "FastEthernet1/3",
                "FastEthernet1/2",
                "FastEthernet0/1",
                "FastEthernet0/3",
                "FastEthernet0/2",
                "HundredGigabitEthernet1/0/0",
                "HundredGigabitEthernet1/0/2",
                "HundredGigabitEthernet1/0/1",
                "Ethernet0",
                "Ethernet2",
                "Ethernet1",
            ]
        },
        "received": [
            "Ethernet0",
            "Ethernet1",
            "Ethernet2",
            "FastEthernet0/1",
            "FastEthernet0/2",
            "FastEthernet0/3",
            "FastEthernet1/1",
            "FastEthernet1/2",
            "FastEthernet1/3",
            "HundredGigabitEthernet1/0/0",
            "HundredGigabitEthernet1/0/1",
            "HundredGigabitEthernet1/0/2",
        ],
    },
    {
        "sent": {
            "interfaces": [
                "FastEthernet0/1",
                "FastEthernet0/3",
                "FastEthernet0/2",
                "HundredGigabitEthernet1/0/0",
                "HundredGigabitEthernet1/0/2",
                "HundredGigabitEthernet1/0/1",
                "Ethernet0",
                "Ethernet2",
                "Ethernet1",
            ],
            "reverse": True,
        },
        "received": [
            "HundredGigabitEthernet1/0/0",
            "HundredGigabitEthernet1/0/1",
            "HundredGigabitEthernet1/0/2",
            "FastEthernet0/1",
            "FastEthernet0/2",
            "FastEthernet0/3",
            "Ethernet0",
            "Ethernet1",
            "Ethernet2",
        ],
    },
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


@pytest.mark.parametrize("data", CANONICAL_INTERFACE_NAME_LIST)
def test_canonical_interface_name_list(data):
    assert interface.canonical_interface_name_list(**data["sent"]) == data["received"]


def test_canonical_interface_name_list_failure():
    with pytest.raises(ValueError, match=r"Verify interface on and no match found for [^,]*, [^ ]*"):
        data = {"interfaces": ["SuperFastEth1/0/1", "SuperFastEth1/0/2"], "verify": True}
        interface.canonical_interface_name_list(**data)


def test_canonical_interface_name_list_order_failure():
    with pytest.raises(ValueError, match=r"weight is not one of the supported orderings"):
        data = {"interfaces": ["SuperFastEth1/0/1", "SuperFastEth1/0/2"], "order": "weight"}
        interface.canonical_interface_name_list(**data)


@pytest.mark.parametrize("data", ABBREVIATED_INTERFACE_NAME_LIST)
def test_abbreviated_interface_name_list(data):
    assert interface.abbreviated_interface_name_list(**data["sent"]) == data["received"]


def test_abbreviated_interface_name_list_failure():
    with pytest.raises(ValueError, match=r"Verify interface on and no match found for [^,]*, [^ ]*"):
        data = {"interfaces": ["SuperFastEth1/0/1", "SuperFastEth1/0/2"], "verify": True}
        interface.canonical_interface_name_list(**data)


@pytest.mark.parametrize("data", ABBREVIATED_INTERFACE_NAME)
def test_abbreviated_interface_name(data):
    assert interface.abbreviated_interface_name(**data["sent"]) == data["received"]


def test_abbreviated_interface_name_failure():
    with pytest.raises(ValueError, match=r"Verify interface on and no match found for*"):
        data = {"interface": "SuperFastEth 1/0/1", "verify": True}
        interface.abbreviated_interface_name(**data)


def test_abbreviated_interface_name_order_failure():
    with pytest.raises(ValueError, match=r"weight is not one of the supported orderings"):
        data = {"interfaces": "SuperFastEth 1/0/1", "order": "weight"}
        interface.abbreviated_interface_name_list(**data)


@pytest.mark.parametrize("data", ORDERED_INTERFACE_NAME_LIST)
def test_list_alphabetical(data):
    assert interface.list_alphabetical(**data["sent"]) == data["received"]
