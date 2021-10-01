"""Test for the Bandwidth functions."""

import pytest
from netutils import bandwidth

kbps_to_mbps = [
    {"sent": 1.0, "received": 0.001},
    {"sent": 2.0, "received": 0.002},
    {"sent": 100.0, "received": 0.1},
]


@pytest.mark.parametrize("data", kbps_to_mbps)
def test_kbps_to_mbps(data):
    assert bandwidth.kbps_to_mbps(data["sent"]) == data["received"]


kbps_to_gbps = [
    {"sent": 1.0, "received": 0.000001},
    {"sent": 2.0, "received": 0.000002},
    {"sent": 100.0, "received": 0.0001},
]


@pytest.mark.parametrize("data", kbps_to_gbps)
def test_kbps_to_gbps(data):
    assert bandwidth.kbps_to_gbps(data["sent"]) == data["received"]


kbps_to_tbps = [
    {"sent": 1.0, "received": 0.000000001},
    {"sent": 2.0, "received": 0.000000002},
    {"sent": 100.0, "received": 0.0000001},
]


@pytest.mark.parametrize("data", kbps_to_tbps)
def test_kbps_to_tbps(data):
    assert bandwidth.kbps_to_tbps(data["sent"]) == data["received"]


mbps_to_gbps = [
    {"sent": 1.0, "received": 0.001},
    {"sent": 2.0, "received": 0.002},
    {"sent": 100.0, "received": 0.1},
]


@pytest.mark.parametrize("data", mbps_to_gbps)
def test_mbps_to_gbps(data):
    assert bandwidth.mbps_to_gbps(data["sent"]) == data["received"]


mbps_to_tbps = [
    {"sent": 1.0, "received": 0.000001},
    {"sent": 2.0, "received": 0.000002},
    {"sent": 100.0, "received": 0.0001},
]


@pytest.mark.parametrize("data", mbps_to_tbps)
def test_mbps_to_tbps(data):
    assert bandwidth.mbps_to_tbps(data["sent"]) == data["received"]


mbps_to_kbps = [
    {"sent": 1.0, "received": 1000.0},
    {"sent": 2.0, "received": 2000.0},
    {"sent": 100.0, "received": 100000.0},
]


@pytest.mark.parametrize("data", mbps_to_kbps)
def test_mbps_to_kbps(data):
    assert bandwidth.mbps_to_kbps(data["sent"]) == data["received"]


gbps_to_kbps = [
    {"sent": 1.0, "received": 1000000.0},
    {"sent": 2.0, "received": 2000000.0},
    {"sent": 100.0, "received": 100000000.0},
]


@pytest.mark.parametrize("data", gbps_to_kbps)
def test_gbps_to_kbps(data):
    assert bandwidth.gbps_to_kbps(data["sent"]) == data["received"]


gbps_to_mbps = [
    {"sent": 1.0, "received": 1000.0},
    {"sent": 2.0, "received": 2000.0},
    {"sent": 100.0, "received": 100000.0},
]


@pytest.mark.parametrize("data", gbps_to_mbps)
def test_gbps_to_mbps(data):
    assert bandwidth.gbps_to_mbps(data["sent"]) == data["received"]


gbps_to_tbps = [
    {"sent": 1.0, "received": 0.001},
    {"sent": 2.0, "received": 0.002},
    {"sent": 100.0, "received": 0.1},
]


@pytest.mark.parametrize("data", gbps_to_tbps)
def test_gbps_to_tbps(data):
    assert bandwidth.gbps_to_tbps(data["sent"]) == data["received"]


name_to_kbits = [
    {"sent": "10Mbps", "received": 10000},
    {"sent": "10 Mbps", "received": 10000},
    {"sent": "1Gbps", "received": 1000000},
    {"sent": "1 Gbps", "received": 1000000},
    {"sent": "100Gbps", "received": 100000000},
    {"sent": "100 Gbps", "received": 100000000},
]


@pytest.mark.parametrize("data", name_to_kbits)
def test_name_to_kbits(data):
    assert bandwidth.name_to_kbits(data["sent"]) == data["received"]


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
