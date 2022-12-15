"""Test for the ping based functions."""

import socket
import pytest

from netutils import ping

ping_data = [
    {"sent": {"ip": "1.1.1.1", "port": 443}, "received": True},
    {"sent": {"ip": "nevergonnagiveyouup.pizza", "port": 443}, "received": None, "raises": socket.gaierror},
    {"sent": {"ip": "192.0.2.0", "port": 443}, "received": False},
    {"sent": {"ip": "1.1.1.1", "port": 443, "timeout": 3}, "received": True},
]


@pytest.mark.parametrize("data", ping_data)
def test_tcp_ping(data):
    raised = None
    try:
        assert ping.tcp_ping(**data["sent"]) == data["received"]
    except Exception as ex:
        raised = ex

    assert isinstance(raised, data.get("raises", None.__class__))
