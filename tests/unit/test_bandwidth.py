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
    {"sent": "100 Gb", "received": 100000000000},
    {"sent": "10GBps", "received": 80000000000},
    {"sent": "10GB", "received": 80000000000},
]


@pytest.mark.parametrize("data", name_to_bits)
def test_name_to_bits(data):
    assert bandwidth.name_to_bits(data["sent"]) == data["received"]


name_to_bits_exceptions = [
    {"speed": "1 Bbps"},
    {"speed": "1 Qbps"},
    {"speed": "9"},
    {"speed": "bps"},
    {"speed": 1.0},
    {"speed": ("10Kbps",)},
]


@pytest.mark.parametrize("data", name_to_bits_exceptions)
def test_name_to_bits_exceptions(data):
    with pytest.raises(ValueError):
        assert bandwidth.name_to_bits(**data)


bits_to_name = [
    {"sent": {"speed": 950}, "received": "950bps"},
    {"sent": {"speed": 1000}, "received": "1Kbps"},
    {"sent": {"speed": 1000, "nbr_decimal": 1}, "received": "1.0Kbps"},
    {"sent": {"speed": 1000000}, "received": "1Mbps"},
    {"sent": {"speed": 1000000, "nbr_decimal": 1}, "received": "1.0Mbps"},
    {"sent": {"speed": 1000000000}, "received": "1Gbps"},
    {"sent": {"speed": 1100000000, "nbr_decimal": 1}, "received": "1.1Gbps"},
    {"sent": {"speed": 1000000000, "nbr_decimal": 1}, "received": "1.0Gbps"},
    {"sent": {"speed": 1000000000000}, "received": "1Tbps"},
    {"sent": {"speed": 1000000000000, "nbr_decimal": 1}, "received": "1.0Tbps"},
    {"sent": {"speed": 1234, "nbr_decimal": 0}, "received": "1Kbps"},
]


@pytest.mark.parametrize("data", bits_to_name)
def test_bits_to_name(data):
    assert bandwidth.bits_to_name(**data["sent"]) == data["received"]


bits_to_name_exceptions = [
    {"speed": "1 Bbps"},
    {"speed": "1 Qbps"},
    {"speed": "9"},
    {"speed": "bps"},
    {"speed": 1.0},
    {"speed": ("10Kbps",)},
    {"speed": -10.0},
    {"speed": 9999999999999999999999999999},
]


@pytest.mark.parametrize("data", bits_to_name_exceptions)
def test_bits_to_name_exceptions(data):
    with pytest.raises(ValueError):
        assert bandwidth.bits_to_name(**data)


bytes_to_name = [
    {"sent": {"speed": 950.0}, "received": "7600.0Bps"},
    {"sent": {"speed": 1000.0}, "received": "8000.0Bps"},
    {"sent": {"speed": 1000000.0}, "received": "1000.0KBps"},
    {"sent": {"speed": 1000000000.0}, "received": "1000.0MBps"},
    {"sent": {"speed": 1000000000000.0}, "received": "1000.0GBps"},
]


@pytest.mark.parametrize("data", bytes_to_name)
def test_bytes_to_name(data):
    assert bandwidth.bytes_to_name(**data["sent"]) == data["received"]


bytes_to_name_exceptions = [
    {"speed": "1 BBps"},
    {"speed": "1 QBps"},
    {"speed": "9"},
    {"speed": "Bps"},
    {"speed": 10},
    {"speed": ("10KBps",)},
    {"speed": -10.0},
]


@pytest.mark.parametrize("data", bytes_to_name_exceptions)
def test_bytes_to_name_exceptions(data):
    with pytest.raises(ValueError):
        assert bandwidth.bytes_to_name(**data)


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
    {"sent": "1 TB", "received": 1000000000000.0},
    {"sent": "10Gbps", "received": 1250000000.0},
    {"sent": "10Gb", "received": 1250000000.0},
]


@pytest.mark.parametrize("data", name_to_bytes)
def test_name_to_bytes(data):
    assert bandwidth.name_to_bytes(data["sent"]) == data["received"]


name_to_bytes_exceptions = [
    {"speed": "1 BBps"},
    {"speed": "1 QBps"},
    {"speed": "9"},
    {"speed": "Bps"},
    {"speed": 1.0},
    {"speed": ("10Kbps",)},
    {"speed": "1 bbps"},
    {"speed": "kBps"},
]


@pytest.mark.parametrize("data", name_to_bytes_exceptions)
def test_name_to_bytes_exceptions(data):
    with pytest.raises(ValueError):
        assert bandwidth.name_to_bytes(**data)


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


named_exceptions = [
    {"speed": "1 Bbps", "speed_type": "Kbps"},
    {"speed": "1 Qbps", "speed_type": "KBps"},
    {"speed": "9", "speed_type": "bps"},
    {"speed": "bps", "speed_type": "Mbps"},
    {"speed": 10.0, "speed_type": "Mbps"},
    {"speed": (10.0,), "speed_type": "Mbps"},
    {"speed": 10, "speed_type": "Mbps"},
    {"speed": "-bps", "speed_type": "Mbps"},
    {"speed": "10Mbps", "speed_type": "Qbps"},
    {"speed": "10kBps", "speed_type": "Gbps"},
]


@pytest.mark.parametrize("data", named_exceptions)
def test_name_to_name_exceptions(data):
    with pytest.raises(ValueError):
        assert bandwidth.name_to_name(**data)
