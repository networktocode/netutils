"""Test for the DNS based functions."""

import socket
import pytest

from netutils import dns, ip


test_is_fqdn = [
    {"sent": "google.com", "received": True},
    {"sent": "yahoo.com", "received": True},
    {"sent": "nevergonnagiveyouup.pizza", "received": False},
]

test_fqdn = [
    {"sent": "google.com"},
    {"sent": "yahoo.com"},
]


@pytest.mark.parametrize("data", test_is_fqdn)
def test_is_fqdn_resolvable(data):
    assert dns.is_fqdn_resolvable(data["sent"]) == data["received"]


@pytest.mark.parametrize("data", test_fqdn)
def test_fqdn_to_ip(data):
    assert ip.is_ip(dns.fqdn_to_ip(data["sent"])) is True


def test_bad_hostname():
    """Test raise when routing_table is not a list."""
    with pytest.raises(socket.error):
        dns.fqdn_to_ip("nevergonnagiveyouup.pizza")
