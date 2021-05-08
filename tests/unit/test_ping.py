"""Test for the ping based functions."""

import pytest

from netutils import ping

ping_data = [
    {"sent": {"ip": "1.1.1.1", "port": 443}, "received": True},
    {"sent": {"ip": "nevergonnagiveyouup.pizza", "port": 443}, "received": False},
]


@pytest.mark.parametrize("data", ping_data)
def test_tcp_ping(data):
    assert ping.tcp_ping(**data["sent"]) == data["received"]
