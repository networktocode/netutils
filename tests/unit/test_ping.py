"""Test for the ping based functions."""

import socket
import pytest

from netutils import ping
from unittest import mock

ping_data = [
    {"sent": {"ip": "1.1.1.1", "port": 443}, "received": {"retval": True}},
    {"sent": {"ip": "192.0.2.0", "port": 443}, "received": {"retval": False}, "raises": socket.timeout},
    {"sent": {"ip": "1.1.1.1", "port": 443, "timeout": 3}, "received": {"retval": True}},
    {
        "sent": {"ip": "nevergonnagiveyouup.pizza", "port": 443},
        "received": {"retval": None, "raised": socket.gaierror},
        "raises": socket.gaierror,
    },
]


@pytest.mark.parametrize("data", ping_data)
def test_tcp_ping(data):
    with mock.patch("netutils.ping.socket.socket") as socket_mock:
        instance = socket_mock.return_value
        instance.connect.side_effect = data.get("raises")
        raised = data["received"].get("raised")
        if raised:
            pytest.raises(raised, ping.tcp_ping, **data["sent"])
        else:
            assert ping.tcp_ping(**data["sent"]) == data["received"]["retval"]

        if not data.get("raises"):
            instance.shutdown.assert_called_with(socket.SHUT_RDWR)

        timeout = data["sent"].get("timeout") or 1
        instance.settimeout.assert_called_with(timeout)

        ip = data["sent"].get("ip")
        port = data["sent"].get("port")
        instance.connect.assert_called_with((ip, port))

        instance.close.assert_called()
