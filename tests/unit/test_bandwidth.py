"""Test for the Bandwidth functions."""

import pytest
from netutils import bandwidth


name_to_bits = [
    {"sent": "10Mbps", "received": 10000000},
    {"sent": "10 Mbps", "received": 10000000},
    {"sent": "1Gbps", "received": 1000000000000},
    {"sent": "1 Gbps", "received": 1000000000000},
    {"sent": "100Gbps", "received": 100000000000000},
    {"sent": "100 Gbps", "received": 100000000000000},
]


@pytest.mark.parametrize("data", name_to_bits)
def test_name_to_bits(data):
    assert bandwidth.name_to_bits(data["sent"]) == data["received"]


bits_to_name = [
    {"sent": {"speed": 950}, "received": "950bps"},
    {"sent": {"speed": 1000}, "received": "1Kbps"},
    {"sent": {"speed": 1000, "nbr_decimal": 1}, "received": "1.0Kbps"},
    {"sent": {"speed": 1000000}, "received": "1Mbps"},
    {"sent": {"speed": 1000000, "nbr_decimal": 1}, "received": "1.0Mbps"},
    {"sent": {"speed": 1000000000}, "received": "1Gbps"},
    {"sent": {"speed": 1000000000, "nbr_decimal": 1}, "received": "1.0Gbps"},
    {"sent": {"speed": 1000000000000}, "received": "1Tbps"},
    {"sent": {"speed": 1000000000000, "nbr_decimal": 1}, "received": "1.0Tbps"},
]


@pytest.mark.parametrize("data", bits_to_name)
def test_bits_to_name(data):
    assert bandwidth.bits_to_name(**data["sent"]) == data["received"]


name_to_bytes = [
    {"sent": "10MBps", "received": 1250.0},
    {"sent": "10 MBps", "received": 1250.0},
    {"sent": "1GBps", "received": 125000.0},
    {"sent": "1 GBps", "received": 125000.0},
    {"sent": "2.5GBps", "received": 312500.0},
    {"sent": "2.5 GBps", "received": 312500.0},
    {"sent": "100GBps", "received": 12500000.0},
    {"sent": "100 GBps", "received": 12500000.0},
    {"sent": "1TBps", "received": 125000000.0},
    {"sent": "1 TBps", "received": 125000000.0},
]


@pytest.mark.parametrize("data", name_to_bytes)
def test_name_to_bytes(data):
    assert bandwidth.name_to_bytes(data["sent"]) == data["received"]
