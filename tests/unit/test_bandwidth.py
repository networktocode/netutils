"""Test for the Bandwidth functions."""

import pytest
from netutils import bandwidth


name_to_bits = [
    {"sent": "10Mbps", "received": 10000000},
    {"sent": "10 Mbps", "received": 10000000},
    {"sent": "1Gbps", "received": 1000000000},
    {"sent": "1 Gbps", "received": 1000000000},
    {"sent": "100Gbps", "received": 100000000000},
    {"sent": "100 Gbps", "received": 100000000000},
]


@pytest.mark.parametrize("data", name_to_bits)
def test_name_to_bits(data):
    assert bandwidth.name_to_bits(data["sent"]) == data["received"]


bits_to_name = [
    {"sent": {"speed": 950}, "received": "950bps"},
    {"sent": {"speed": 1000}, "received": "1.0Kbps"},
    {"sent": {"speed": 1000, "nbr_decimal": 1}, "received": "1.0Kbps"},
    {"sent": {"speed": 1000000}, "received": "1.0Mbps"},
    {"sent": {"speed": 1000000, "nbr_decimal": 1}, "received": "1.0Mbps"},
    {"sent": {"speed": 1000000000}, "received": "1.0Gbps"},
    {"sent": {"speed": 1000000000, "nbr_decimal": 1}, "received": "1.0Gbps"},
    {"sent": {"speed": 1000000000000}, "received": "1.0Tbps"},
    {"sent": {"speed": 1000000000000, "nbr_decimal": 1}, "received": "1.0Tbps"},
]


@pytest.mark.parametrize("data", bits_to_name)
def test_bits_to_name(data):
    assert bandwidth.bits_to_name(**data["sent"]) == data["received"]


name_to_bytes = [
    {"sent": "10MBps", "received": 10000000.0},
    {"sent": "10 MBps", "received": 10000000.0},
    {"sent": "1GBps", "received": 1000000000.0},
    {"sent": "1 GBps", "received": 1000000000.0},
    {"sent": "2.5GBps", "received": 2500000000.0},
    {"sent": "2.5 GBps", "received": 2500000000.0},
    {"sent": "100GBps", "received": 100000000000.0},
    {"sent": "100 GBps", "received": 100000000000.0},
    {"sent": "1TBps", "received": 1000000000000.0},
    {"sent": "1 TBps", "received": 1000000000000.0},
]


@pytest.mark.parametrize("data", name_to_bytes)
def test_name_to_bytes(data):
    assert bandwidth.name_to_bytes(data["sent"]) == data["received"]


name_to_name = [
    {"sent": {"speed": "10Mbps", "speed_type": "Kbps"}, "received": "10000.0Kbps"},
    {"sent": {"speed": "10Mbps", "speed_type": "KBps"}, "received": "1250.0KBps"},
    {"sent": {"speed": "10MBps", "speed_type": "Kbps"}, "received": "80000.0Kbps"},
    {"sent": {"speed": "10MBps", "speed_type": "KBps"}, "received": "10000.0KBps"},
    {"sent": {"speed": "1Gbps", "speed_type": "Kbps"}, "received": "1000000.0Kbps"},
    {"sent": {"speed": "1Gbps", "speed_type": "KBps"}, "received": "125000.0KBps"},
    {"sent": {"speed": "2.5Gbps", "speed_type": "Kbps"}, "received": "2500000.0Kbps"},
    {"sent": {"speed": "2.5Gbps", "speed_type": "KBps"}, "received": "312500.0KBps"},
]


@pytest.mark.parametrize("data", name_to_name)
def test_name_to_name(data):
    assert bandwidth.name_to_name(**data["sent"]) == data["received"]
