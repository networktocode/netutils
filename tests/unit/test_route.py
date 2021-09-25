"""Test for the longest_prefix_match definitions."""
from ipaddress import AddressValueError, NetmaskValueError

import pytest

from netutils.route import NoRouteFound, longest_prefix_match


def test_longest_prefix_match():
    """Test Success."""
    lookup = "10.1.1.245"
    routes = [{"network": "192.168.1.1", "mask": "255.255.255.255"}, {"network": "10.1.1.0", "mask": "24"}]
    winner = longest_prefix_match(lookup, routes)
    assert str(winner) == "10.1.1.0/24"


def test_route_table_not_list():
    """Test raise when routing_table is not a list."""
    with pytest.raises(TypeError):
        lookup = "10.1.1.245"
        routes = {"network": "192.168.1.1"}
        longest_prefix_match(lookup, routes)


def test_route_table_no_len():
    """Test raise when routing_table is empty list."""
    with pytest.raises(IndexError):
        lookup = "10.1.1.245"
        routes = []
        longest_prefix_match(lookup, routes)


def test_route_table_ip_bad_type():
    """Test raise when ip not string or ipaddress object."""
    with pytest.raises(TypeError):
        lookup = ["10.1.1.245"]
        routes = [{"network": "192.168.1.1", "mask": "255.255.255.255"}]
        longest_prefix_match(lookup, routes)


@pytest.mark.parametrize("test_input", ["/24", "/255.255.255.0"])
def test_route_table_except_address_value(test_input):
    """Test raise on address value."""
    with pytest.raises(AddressValueError):
        lookup = "10.1.1.245"
        routes = [
            {"network": "192.168.1.1", "mask": "255.255.255.255"},
            {"network": "10.1.1.0", "mask": test_input},
        ]
        longest_prefix_match(lookup, routes)


@pytest.mark.parametrize("test_input", ["100", "255.255.255.155"])
def test_route_table_except_mask_error(test_input):
    """Test raise on address value."""
    with pytest.raises(NetmaskValueError):
        lookup = "10.1.1.245"
        routes = [
            {"network": "192.168.1.1", "mask": "255.255.255.255"},
            {"network": "10.1.1.0", "mask": test_input},
        ]
        longest_prefix_match(lookup, routes)


@pytest.mark.parametrize("test_input", ["259.1.1.0", "1.1.1.256"])
def test_route_table_bad_ip_address(test_input):
    """Test raise on address value."""
    with pytest.raises(AddressValueError):
        lookup = "10.1.1.245"
        routes = [{"network": "192.168.1.1", "mask": "255.255.255.255"}, {"network": test_input, "mask": "24"}]
        longest_prefix_match(lookup, routes)


def test_route_bad_ip_addr():
    """Test bad 'search' IP address."""
    with pytest.raises(ValueError):
        lookup = "299.1.1.245"
        routes = [{"network": "192.168.1.1", "mask": "255.255.255.255"}, {"network": "10.1.1.0", "mask": "24"}]
        longest_prefix_match(lookup, routes)


def test_route_multiple_overlapping():
    """Test longest route with overlapping routes."""
    lookup = "10.1.1.245"
    routes = [
        {"network": "10.1.1.240", "mask": "255.255.255.240"},
        {"network": "10.1.1.128", "mask": "255.255.255.128"},
        {"network": "10.1.1.0", "mask": "24"},
    ]
    winner = longest_prefix_match(lookup, routes)
    assert str(winner) == "10.1.1.240/28"


def test_route_no_best_route_found():
    """Test no route found."""
    with pytest.raises(NoRouteFound):
        lookup = "192.168.1.245"
        routes = [
            {"network": "10.1.1.240", "mask": "255.255.255.240"},
            {"network": "10.1.1.128", "mask": "255.255.255.128"},
            {"network": "10.1.1.0", "mask": "24"},
        ]
        longest_prefix_match(lookup, routes)


def test_route_non_ip_sent():
    """Test when sending a non-ip."""
    with pytest.raises(TypeError):
        lookup = 12345
        routes = [
            {"network": "10.1.1.240", "mask": "255.255.255.240"},
        ]
        longest_prefix_match(lookup, routes)
