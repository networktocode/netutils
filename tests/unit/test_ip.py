"""Test for the IP functions."""

import ipaddress

import pytest

from netutils import ip

IP_ADDRESS = [
    {
        "sent": {"ip": "10.1.1.1", "attr": "is_loopback"},
        "received": False,
    },
    {
        "sent": {"ip": "10.1.1.1", "attr": "__int__"},
        "received": 167837953,
    },
    {
        "sent": {"ip": "10.1.1.1", "attr": "is_private"},
        "received": True,
    },
    {
        "sent": {"ip": "10.1.1.1", "attr": "__str__"},
        "received": "10.1.1.1",
    },
]

IP_INTERFACE = [
    {
        "sent": {"ip": "10.1.1.1/24", "attr": "is_loopback"},
        "received": False,
    },
    {
        "sent": {"ip": "10.1.1.1/24", "attr": "__int__"},
        "received": 167837953,
    },
    {
        "sent": {"ip": "10.1.1.1/24", "attr": "network.__str__"},
        "received": "10.1.1.0/24",
    },
    {
        "sent": {"ip": "10.1.1.1/24", "attr": "netmask.__str__"},
        "received": "255.255.255.0",
    },
]

IP_NETWORK_WITH_KWARGS = [
    {
        "sent": {"ip": "10.1.1.0/28", "attr": "subnets", "new_prefix": 30},
        "received": "[IPv4Network('10.1.1.0/30'), IPv4Network('10.1.1.4/30'), IPv4Network('10.1.1.8/30'), IPv4Network('10.1.1.12/30')]",
    },
    {
        "sent": {"ip": "10.1.1.0/28", "attr": "subnets"},
        "received": "[IPv4Network('10.1.1.0/29'), IPv4Network('10.1.1.8/29')]",
    },
]

IP_NETWORK = [
    {
        "sent": {"ip": "10.1.1.0/24", "attr": "hostmask.__str__"},
        "received": "0.0.0.255",
    },
    {
        "sent": {"ip": "10.1.1.0/24", "attr": "network_address.__int__"},
        "received": 167837952,
    },
    {
        "sent": {"ip": "10.1.1.0/24", "attr": "version"},
        "received": 4,
    },
]

IP_TO_HEX = [
    {
        "sent": {"ip": "10.1.1.1"},
        "received": "0a010101",
    },
    {
        "sent": {"ip": "2001:db8:3333:4444:5555:6666:7777:8888"},
        "received": "20010db8333344445555666677778888",
    },
]

IP_ADDITION = [
    {
        "sent": {"ip": "10.1.1.1", "val": 10},
        "received": "10.1.1.11",
    },
    {
        "sent": {"ip": "2001:db8:3333:4444:5555:6666:7777:8888", "val": 10},
        "received": "2001:db8:3333:4444:5555:6666:7777:8892",
    },
]

IP_FIRST_USABLE = [
    {
        "sent": {"ip_network": "10.1.1.0/24"},
        "received": "10.1.1.1",
    },
    {
        "sent": {"ip_network": "10.1.1.0/255.255.255.0"},
        "received": "10.1.1.1",
    },
    {
        "sent": {"ip_network": "10.1.1.0/31"},
        "received": "10.1.1.0",
    },
    {
        "sent": {"ip_network": "2001:db8:3c4d:15::/64"},
        "received": "2001:db8:3c4d:15::1",
    },
    {
        "sent": {"ip_network": "2001:db8:3c4d:15::/127"},
        "received": "2001:db8:3c4d:15::",
    },
]

IP_TO_BIN = [
    {
        "sent": {
            "ip": "10.1.1.1",
        },
        "received": "00001010000000010000000100000001",
    },
    {
        "sent": {
            "ip": "2001:db8:3333:4444:5555:6666:7777:8888",
        },
        "received": "00100000000000010000110110111000001100110011001101000100010001000101010101010101011001100110011001110111011101111000100010001000",
    },
]

IP_SUBTRACT = [
    {
        "sent": {"ip": "10.1.1.1", "val": 10},
        "received": "10.1.0.247",
    },
    {
        "sent": {"ip": "2001:db8:3333:4444:5555:6666:7777:8888", "val": 10},
        "received": "2001:db8:3333:4444:5555:6666:7777:887e",
    },
]

IS_IP = [
    {
        "sent": {
            "ip": "10.1.1.1",
        },
        "received": True,
    },
    {
        "sent": {
            "ip": "255.255.255.255",
        },
        "received": True,
    },
    {
        "sent": {
            "ip": "2001:db8:3333:4444:5555:6666:7777:8888",
        },
        "received": True,
    },
    {
        "sent": {
            "ip": "NOT AN IP",
        },
        "received": False,
    },
    {
        "sent": {
            "ip": "255.255.255.256",
        },
        "received": False,
    },
]

IS_IP_RANGE = [
    {
        "sent": {
            "ip_range": "10.1.1.1",
        },
        "received": False,
    },
    {
        "sent": {
            "ip_range": "10.1.100.10-10.1.100.1",
        },
        "received": False,
    },
    {
        "sent": {
            "ip_range": "2001::10-2001::1",
        },
        "received": False,
    },
    {
        "sent": {
            "ip_range": "10.500.100.10-10.1.100.1",
        },
        "received": False,
    },
    {
        "sent": {
            "ip_range": "NOT AN IP",
        },
        "received": False,
    },
    {
        "sent": {
            "ip_range": "255.255.255.256",
        },
        "received": False,
    },
    {
        "sent": {
            "ip_range": "10.1.100.10-10.1.100.100",
        },
        "received": True,
    },
    {
        "sent": {
            "ip_range": "2001::10-2001::100",
        },
        "received": True,
    },
]

GET_RANGE_IPS = [
    {
        "sent": {
            "ip_range": "2001::10-2001::100",
        },
        "received": (ipaddress.IPv6Address("2001::10"), ipaddress.IPv6Address("2001::100")),
    },
    {
        "sent": {
            "ip_range": "10.1.100.10-10.1.100.100",
        },
        "received": (ipaddress.IPv4Address("10.1.100.10"), ipaddress.IPv4Address("10.1.100.100")),
    },
]

IS_IP_WITHIN = [
    {
        "sent": {
            "ip": "192.168.1.10",
            "ip_compare": "192.168.1.10",
        },
        "received": True,
    },
    {
        "sent": {
            "ip": "192.168.1.10",
            "ip_compare": "192.168.1.0-192.168.1.20",
        },
        "received": True,
    },
    {
        "sent": {
            "ip": "192.168.1.0/24",
            "ip_compare": ["192.168.1.0-192.168.1.20", "192.168.2.0-192.168.2.20"],
        },
        "received": False,
    },
    {
        "sent": {
            "ip": "192.168.1.10-192.168.1.15",
            "ip_compare": ["192.168.1.0-192.168.1.20", "192.168.2.0-192.168.2.20"],
        },
        "received": True,
    },
    {
        "sent": {
            "ip": "10.0.0.0/8",
            "ip_compare": ["192.168.1.0/24", "172.16.0.0/12"],
        },
        "received": False,
    },
    {
        "sent": {
            "ip": "192.168.1.10",
            "ip_compare": "192.168.1.20",
        },
        "received": False,
    },
    {
        "sent": {
            "ip": "192.168.1.10",
            "ip_compare": "192.168.2.0-192.168.2.20",
        },
        "received": False,
    },
    {
        "sent": {
            "ip": "192.168.1.0/24",
            "ip_compare": ["192.168.2.0-192.168.2.20", "192.168.3.0-192.168.3.20"],
        },
        "received": False,
    },
    {
        "sent": {
            "ip": "192.168.1.50-192.168.1.60",
            "ip_compare": ["192.168.2.0-192.168.2.20", "192.168.3.0-192.168.3.20"],
        },
        "received": False,
    },
    {
        "sent": {
            "ip": "192.168.1.10",
            "ip_compare": "192.168.2.0/24",
        },
        "received": False,
    },
]

GET_BROADCAST_ADDRESS = [
    {
        "sent": {"ip_network": "10.1.1.0/24"},
        "received": "10.1.1.255",
    },
    {
        "sent": {"ip_network": "10.1.1.0/255.255.255.0"},
        "received": "10.1.1.255",
    },
    {
        "sent": {"ip_network": "10.1.1.0/31"},
        "received": "10.1.1.1",
    },
    {
        "sent": {"ip_network": "2001:db8:3c4d:15::/64"},
        "received": "2001:db8:3c4d:15:ffff:ffff:ffff:ffff",
    },
    {
        "sent": {"ip_network": "2001:db8:3c4d:15::/127"},
        "received": "2001:db8:3c4d:15::1",
    },
]

GET_ALL_HOST = [
    {
        "sent": {"ip_network": "10.1.1.0/30"},
        "received": ["10.1.1.1", "10.1.1.2"],
    },
    {
        "sent": {"ip_network": "10.1.1.0/255.255.255.252"},
        "received": ["10.1.1.1", "10.1.1.2"],
    },
    {
        "sent": {"ip_network": "10.1.1.0/31"},
        "received": ["10.1.1.0", "10.1.1.1"],
    },
    {
        "sent": {"ip_network": "2001:db8:3c4d:15::/126"},
        "received": ["2001:db8:3c4d:15::1", "2001:db8:3c4d:15::2", "2001:db8:3c4d:15::3"],
    },
    {
        "sent": {"ip_network": "2001:db8:3c4d:15::/127"},
        "received": ["2001:db8:3c4d:15::", "2001:db8:3c4d:15::1"],
    },
]

GET_PEER = [
    {
        "sent": {"ip_interface": "10.0.0.1/255.255.255.252"},
        "received": "10.0.0.2",
    },
    {
        "sent": {"ip_interface": "10.0.0.2/30"},
        "received": "10.0.0.1",
    },
    {
        "sent": {"ip_interface": "10.0.0.1/31"},
        "received": "10.0.0.0",
    },
    {
        "sent": {"ip_interface": "10.0.0.0/255.255.255.254"},
        "received": "10.0.0.1",
    },
    {
        "sent": {"ip_interface": "2001::1/126"},
        "received": "2001::2",
    },
    {
        "sent": {"ip_interface": "2001::1/127"},
        "received": "2001::",
    },
]
GET_PEER_BAD_MASK = [
    {
        "sent": {"ip_interface": "10.0.0.1/255.255.255.255"},
    },
    {
        "sent": {"ip_interface": "10.0.0.2/24"},
    },
    {
        "sent": {"ip_interface": "2001::/64"},
    },
]

GET_PEER_BAD_IP = [
    {
        "sent": {"ip_interface": "10.0.0.0/255.255.255.252"},
    },
    {
        "sent": {"ip_interface": "10.0.0.3/30"},
    },
    {
        "sent": {"ip_interface": "2001::/126"},
    },
]


USABLE_RANGE = [
    {
        "sent": {"ip_network": "10.1.1.0/24"},
        "received": "10.1.1.1 - 10.1.1.254",
    },
    {
        "sent": {"ip_network": "10.1.1.0/255.255.255.0"},
        "received": "10.1.1.1 - 10.1.1.254",
    },
    {
        "sent": {"ip_network": "10.1.1.0/31"},
        "received": "10.1.1.0 - 10.1.1.1",
    },
    {
        "sent": {"ip_network": "2001:db8:3c4d:15::/64"},
        "received": "2001:db8:3c4d:15::1 - 2001:db8:3c4d:15:ffff:ffff:ffff:fffe",
    },
    {
        "sent": {"ip_network": "2001:db8:3c4d:15::/127"},
        "received": "2001:db8:3c4d:15:: - 2001:db8:3c4d:15::1",
    },
]

IS_NETMASK = [
    {"sent": {"netmask": "255.255.255.0"}, "received": True},
    {"sent": {"netmask": "255.192.0.0"}, "received": True},
    {"sent": {"netmask": "255.266.0.0"}, "received": False},
    {"sent": {"netmask": "255.0.128.0"}, "received": False},
    {"sent": {"netmask": "44"}, "received": False},
    {"sent": {"netmask": "mynetmask"}, "received": False},
    {"sent": {"netmask": "dead:beef:cafe::"}, "received": False},
    {"sent": {"netmask": "ff00::"}, "received": True},
    {"sent": {"netmask": "ffff:ffff:ffff:ffff:ffff::"}, "received": True},
]

IS_REVERSIBLE_WILDCARDMASK = [
    {"sent": {"wildcardmask": "0.0.0.255"}, "received": True},
    {"sent": {"wildcardmask": "0.0.0.0"}, "received": True},
    {"sent": {"wildcardmask": "0.0.0.1"}, "received": True},
    {"sent": {"wildcardmask": "0.0.0.2"}, "received": False},
    {"sent": {"wildcardmask": "0.0.255.0"}, "received": False},
]

NETMASK_CIDR = [
    {"sent": {"netmask": "255.255.255.0"}, "received": 24},
    {"sent": {"netmask": "255.192.0.0"}, "received": 10},
    {"sent": {"netmask": "255.255.255.252"}, "received": 30},
    {"sent": {"netmask": "ff00::"}, "received": 8},
    {"sent": {"netmask": "ffff:ffff:ffff:ffff:ffff::"}, "received": 80},
]

CIDR_NETMASK = [
    {"sent": {"cidr": 24}, "received": "255.255.255.0"},
    {"sent": {"cidr": 28}, "received": "255.255.255.240"},
    {"sent": {"cidr": 10}, "received": "255.192.0.0"},
    {"sent": {"cidr": 17}, "received": "255.255.128.0"},
]

CIDR_NETMASK6 = [
    {"sent": {"cidr": 8}, "received": "ff00::"},
    {"sent": {"cidr": 80}, "received": "ffff:ffff:ffff:ffff:ffff::"},
]

NETMASK_WILDCARDMASK = [
    {"sent": {"netmask": "255.255.255.254"}, "received": "0.0.0.1"},
    {"sent": {"netmask": "255.255.255.252"}, "received": "0.0.0.3"},
    {"sent": {"netmask": "255.255.255.0"}, "received": "0.0.0.255"},
    {"sent": {"netmask": "255.255.254.0"}, "received": "0.0.1.255"},
    {"sent": {"netmask": "255.255.252.0"}, "received": "0.0.3.255"},
    {"sent": {"netmask": "255.255.0.0"}, "received": "0.0.255.255"},
    {"sent": {"netmask": "255.254.0.0"}, "received": "0.1.255.255"},
    {"sent": {"netmask": "255.0.0.0"}, "received": "0.255.255.255"},
]

WILDCARDMASK_NETMASK = [
    {"sent": {"wildcardmask": "0.0.0.1"}, "received": "255.255.255.254"},
    {"sent": {"wildcardmask": "0.0.0.3"}, "received": "255.255.255.252"},
    {"sent": {"wildcardmask": "0.0.0.255"}, "received": "255.255.255.0"},
    {"sent": {"wildcardmask": "0.0.1.255"}, "received": "255.255.254.0"},
    {"sent": {"wildcardmask": "0.0.3.255"}, "received": "255.255.252.0"},
    {"sent": {"wildcardmask": "0.0.255.255"}, "received": "255.255.0.0"},
    {"sent": {"wildcardmask": "0.1.255.255"}, "received": "255.254.0.0"},
    {"sent": {"wildcardmask": "0.255.255.255"}, "received": "255.0.0.0"},
]

COUNT_BITS = [
    {"sent": 0, "received": 0},
    {"sent": 234, "received": 5},
    {"sent": 255, "received": 8},
    {"sent": 0xFFFFFFFFFFFFFFFF, "received": 64},
]

IS_CLASSFUL = [
    {"sent": {"ip_network": "0.0.0.0/8"}, "received": True},
    {"sent": {"ip_network": "127.0.0.0/8"}, "received": True},
    {"sent": {"ip_network": "128.0.0.0/8"}, "received": False},
    {"sent": {"ip_network": "128.0.0.0/16"}, "received": True},
    {"sent": {"ip_network": "191.255.0.0/16"}, "received": True},
    {"sent": {"ip_network": "192.0.0.0/26"}, "received": False},
    {"sent": {"ip_network": "192.0.0.0/24"}, "received": True},
    {"sent": {"ip_network": "223.255.255.0/24"}, "received": True},
    {"sent": {"ip_network": "224.0.0.0/24"}, "received": False},
]

SORTED_IPS = [
    {
        "sent": "10.0.10.0/24,10.0.100.0/24,10.0.12.0/24,10.0.200.0/24",
        "expected": ["10.0.10.0/24", "10.0.12.0/24", "10.0.100.0/24", "10.0.200.0/24"],
        "sort_type": "network",
    },
    {
        "sent": "10.0.10.0/24, 10.0.100.0/24, 10.0.12.0/24, 10.0.200.0/24",
        "expected": ["10.0.10.0/24", "10.0.12.0/24", "10.0.100.0/24", "10.0.200.0/24"],
        "sort_type": "network",
    },
    {
        "sent": "192.168.1.1,10.1.1.2,172.16.10.1",
        "expected": ["10.1.1.2", "172.16.10.1", "192.168.1.1"],
        "sort_type": "address",
    },
    {
        "sent": "192.168.1.1/24,10.1.1.2/32,172.16.10.1/16",
        "expected": ["10.1.1.2/32", "172.16.10.1/16", "192.168.1.1/24"],
        "sort_type": "interface",
    },
    {
        "sent": "10.0.0.0/24, 10.0.0.0/16, 10.0.0.0/18",
        "expected": ["10.0.0.0/16", "10.0.0.0/18", "10.0.0.0/24"],
        "sort_type": "network",
    },
    {
        "sent": ["10.0.10.0/24", "10.0.100.0/24", "10.0.12.0/24", "10.0.200.0/24"],
        "expected": ["10.0.10.0/24", "10.0.12.0/24", "10.0.100.0/24", "10.0.200.0/24"],
        "sort_type": "network",
    },
    {
        "sent": ["192.168.1.1", "10.1.1.2", "172.16.10.1"],
        "expected": ["10.1.1.2", "172.16.10.1", "192.168.1.1"],
        "sort_type": "address",
    },
    {
        "sent": ["192.168.1.1/24", "10.1.1.2/32", "172.16.10.1/16"],
        "expected": ["10.1.1.2/32", "172.16.10.1/16", "192.168.1.1/24"],
        "sort_type": "interface",
    },
]


@pytest.mark.parametrize("data", IP_TO_HEX)
def test_ip_to_hex(data):
    assert ip.ip_to_hex(**data["sent"]) == data["received"]


@pytest.mark.parametrize("data", IP_ADDITION)
def test_ip_addition(data):
    assert ip.ip_addition(**data["sent"]) == data["received"]


@pytest.mark.parametrize("data", IP_TO_BIN)
def test_ip_to_bin(data):
    assert ip.ip_to_bin(**data["sent"]) == data["received"]


@pytest.mark.parametrize("data", IP_SUBTRACT)
def test_ip_subtract(data):
    assert ip.ip_subtract(**data["sent"]) == data["received"]


@pytest.mark.parametrize("data", IS_IP)
def test_is_ip(data):
    assert ip.is_ip(**data["sent"]) == data["received"]


@pytest.mark.parametrize("data", IS_IP_RANGE)
def test_is_ip_range(data):
    assert ip.is_ip_range(**data["sent"]) == data["received"]


@pytest.mark.parametrize("data", GET_RANGE_IPS)
def test_get_range_ips(data):
    assert ip.get_range_ips(**data["sent"]) == data["received"]


def test_get_range_ips_fail():
    with pytest.raises(ValueError, match=r"Not a valid IP range format of .*"):
        data = {"ip_range": "10.1.100.10-10.1.100.1"}
        ip.get_range_ips(**data)


@pytest.mark.parametrize("data", IS_IP_WITHIN)
def test_is_ip_within(data):
    assert ip.is_ip_within(**data["sent"]) == data["received"]


def test_is_ip_within_fail():
    with pytest.raises(ValueError):
        data = {"ip": "10.1.100.100", "ip_compare": "10.1.100.10-2001::1"}
        ip.is_ip_within(**data)


@pytest.mark.parametrize("data", GET_ALL_HOST)
def test_get_all_host(data):
    assert list(ip.get_all_host(**data["sent"])) == data["received"]


@pytest.mark.parametrize("data", GET_BROADCAST_ADDRESS)
def test_get_broadcast_address(data):
    assert ip.get_broadcast_address(**data["sent"]) == data["received"]


@pytest.mark.parametrize("data", IP_FIRST_USABLE)
def test_get_first_usable(data):
    assert ip.get_first_usable(**data["sent"]) == data["received"]


@pytest.mark.parametrize("data", USABLE_RANGE)
def test_get_usable_range(data):
    assert ip.get_usable_range(**data["sent"]) == data["received"]


@pytest.mark.parametrize("data", IS_NETMASK)
def test_is_netmask(data):
    assert ip.is_netmask(**data["sent"]) == data["received"]


@pytest.mark.parametrize("data", IS_REVERSIBLE_WILDCARDMASK)
def test_is_reversible_wildcardmask(data):
    assert ip.is_reversible_wildcardmask(**data["sent"]) == data["received"]


@pytest.mark.parametrize("data", NETMASK_CIDR)
def test_netmask_to_cidr(data):
    assert ip.netmask_to_cidr(**data["sent"]) == data["received"]


def test_netmask_to_cidr_fail():
    with pytest.raises(ValueError, match=r"Subnet mask is not valid"):
        data = {"netmask": "255.266.0.0"}
        ip.netmask_to_cidr(**data)


@pytest.mark.parametrize("data", CIDR_NETMASK)
def test_cidr_to_netmask(data):
    assert ip.cidr_to_netmask(**data["sent"]) == data["received"]


@pytest.mark.parametrize("data", CIDR_NETMASK6)
def test_cidr_to_netmaskv6(data):
    assert ip.cidr_to_netmaskv6(**data["sent"]) == data["received"]


def test_cidr_to_netmaskv6_fail():
    with pytest.raises(ValueError, match=r"Parameter must be an integer between 0 and 128.*"):
        data = {"cidr": 129}
        ip.cidr_to_netmaskv6(**data)


def test_cidr_to_netmask_fail():
    with pytest.raises(ValueError, match=r"Parameter must be an integer between 0 and 32."):
        data = {"cidr": 37}
        ip.cidr_to_netmask(**data)


@pytest.mark.parametrize("data", NETMASK_WILDCARDMASK)
def test_netmask_to_wildcardmask(data):
    assert ip.netmask_to_wildcardmask(**data["sent"]) == data["received"]


@pytest.mark.parametrize("data", WILDCARDMASK_NETMASK)
def test_wildcardmask_to_netmask(data):
    assert ip.wildcardmask_to_netmask(**data["sent"]) == data["received"]


def test_wildcardmask_to_netmask_invalid():
    with pytest.raises(ValueError, match="Wildcard mask is not valid."):
        ip.wildcardmask_to_netmask("0.0.255.0")


@pytest.mark.parametrize("data", GET_PEER)
def test_get_peer_ip(data):
    assert ip.get_peer_ip(**data["sent"]) == data["received"]


@pytest.mark.parametrize("data", GET_PEER_BAD_MASK)
def test_get_peer_ip_fail_subnet(data):
    with pytest.raises(ValueError, match=r".*acceptable masks.*"):
        ip.get_peer_ip(**data["sent"])


@pytest.mark.parametrize("data", GET_PEER_BAD_IP)
def test_get_peer_ip_fail_ip(data):
    with pytest.raises(ValueError, match=r".*usable range.*"):
        ip.get_peer_ip(**data["sent"])


@pytest.mark.parametrize("data", IP_ADDRESS)
def test_ipaddress_address(data):
    assert ip.ipaddress_address(**data["sent"]) == data["received"]


@pytest.mark.parametrize("data", IP_INTERFACE)
def test_ipaddress_interface(data):
    assert ip.ipaddress_interface(**data["sent"]) == data["received"]


@pytest.mark.parametrize("data", IP_NETWORK)
def test_ipaddress_network(data):
    assert ip.ipaddress_network(**data["sent"]) == data["received"]


@pytest.mark.parametrize("data", IP_NETWORK_WITH_KWARGS)
def test_ipaddress_network_with_kwargs(data):
    assert str(list(ip.ipaddress_network(**data["sent"]))) == data["received"]


@pytest.mark.parametrize("data", IS_CLASSFUL)
def test_is_classful(data):
    assert ip.is_classful(**data["sent"]) == data["received"]


@pytest.mark.parametrize("data", SORTED_IPS)
def test_get_ips_sorted(data):
    assert data["expected"] == ip.get_ips_sorted(data["sent"], sort_type=data["sort_type"])


def test_get_ips_sorted_exception_invalid_list():
    with pytest.raises(ValueError, match="Not a concatenated list of IPs as expected."):
        ip.get_ips_sorted("10.1.1.1/24 10.2.2.2/16")


def test_get_ips_sorted_exception_invalid_instance_type():
    with pytest.raises(ValueError, match="Not a concatenated list of IPs as expected."):
        ip.get_ips_sorted({"10.1.1.1/24", "10.2.2.2/16"})


def test_get_ips_sorted_invalid_sort_type():
    with pytest.raises(ValueError, match="Invalid sort type passed. Must be `address`, `interface`, or `network`."):
        ip.get_ips_sorted("10.0.0.0/24,192.168.0.0/16", sort_type="wrong_type")
