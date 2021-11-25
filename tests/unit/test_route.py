"""Test for the longest_prefix_match definitions."""
from ipaddress import AddressValueError, NetmaskValueError, IPv4Network, IPv6Network

import pytest

from netutils.route import NoRouteFound, longest_prefix_match, prefix_aggregate, find_prefix_gaps


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


def test_prefix_aggregate_empty():
    assert prefix_aggregate([]) == set()


def test_prefix_aggregate_bad_prefix():
    prefixes = ["300.0.0.0/24"]
    with pytest.raises(AddressValueError):
        prefix_aggregate(prefixes)


def test_prefix_aggregate_bad_netmask():
    prefixes = ["100.0.0.0/33"]
    with pytest.raises(AddressValueError):
        prefix_aggregate(prefixes)


def test_prefix_aggregate_bad_minimum_preflength():
    prefixes = ["10.0.0.0/24"]
    with pytest.raises(AssertionError) as execinfo:
        prefix_aggregate(prefixes, min_aggr_pref_len=33)
    assert execinfo.match("^min_aggr_pref_len is bigger than expected")


def test_prefix_aggregate_too_big_min_prefix_length():
    prefixes = ["300.0.0.0/24"]
    with pytest.raises(AddressValueError):
        prefix_aggregate(prefixes)


def test_prefix_aggregate_mixed():
    prefixes = [IPv4Network("10.0.0.0/24"), IPv6Network("beef::0/64")]
    with pytest.raises(AddressValueError):
        prefix_aggregate(prefixes)


def test_prefix_aggregate_continuous_ipv4():
    prefixes = [IPv4Network("10.0.0.0/24"), IPv4Network("10.0.1.0/24")]
    assert prefix_aggregate(prefixes) == {IPv4Network("10.0.0.0/23")}


def test_prefix_aggregate_continuous_ipv6():
    prefixes = ["2001:db8:0:0::/64", "2001:db8:0:1::/64"]
    assert prefix_aggregate(prefixes) == {IPv6Network("2001:db8::/63")}


def test_prefix_aggregate_non_continuous_ipv4():
    prefixes = [IPv4Network("10.0.0.0/24"), IPv4Network("10.0.2.0/24")]
    assert prefix_aggregate(prefixes) == {IPv4Network("10.0.0.0/24"), IPv4Network("10.0.2.0/24")}


def test_prefix_aggregate_non_continuous_ipv6():
    prefixes = ["2001:db8:0:0::/64", "2001:db8:0:2::/64"]
    assert prefix_aggregate(prefixes, force_continuous=False) == {IPv6Network("2001:db8::/62")}


def test_prefix_aggregate_allow_non_continuous_ipv4():
    prefixes = [IPv4Network("10.0.0.0/24"), IPv4Network("10.0.2.0/24")]
    assert prefix_aggregate(prefixes, force_continuous=False) == {IPv4Network("10.0.0.0/22")}


def test_prefix_aggregate_split_if_input_can_be_aggregated_too_long():
    prefixes = [
        IPv4Network("10.0.0.0/24"),
        IPv4Network("10.0.2.0/24"),
        IPv4Network("10.0.4.0/24"),
        IPv4Network("10.0.5.0/24"),
        IPv4Network("10.0.6.0/24"),
        IPv4Network("10.0.104.0/22"),
        IPv4Network("10.0.108.0/22"),
    ]
    assert prefix_aggregate(prefixes, min_aggr_pref_len=22, force_continuous=False) == {
        IPv4Network("10.0.0.0/22"),
        IPv4Network("10.0.4.0/22"),
        IPv4Network("10.0.104.0/22"),
        IPv4Network("10.0.108.0/22"),
    }


def test_prefix_aggregate_smaller_minimum_still_find_the_longest_possible_prefixes():
    prefixes = [
        IPv4Network("10.0.0.0/24"),
        IPv4Network("10.0.2.0/24"),
        IPv4Network("10.0.4.0/24"),
        IPv4Network("10.0.5.0/24"),
        IPv4Network("10.0.6.0/24"),
        IPv4Network("10.0.104.0/22"),
        IPv4Network("10.0.108.0/22"),
    ]
    assert prefix_aggregate(prefixes, min_aggr_pref_len=19, force_continuous=False) == {
        IPv4Network("10.0.0.0/21"),
        IPv4Network("10.0.104.0/21"),
    }


def test_prefix_aggregate_ask_for_longer_prefix_length_will_generate_more_prefixes():
    prefixes = [
        IPv4Network("10.0.0.0/24"),
        IPv4Network("10.0.1.0/24"),
    ]
    assert prefix_aggregate(prefixes, min_aggr_pref_len=25, force_continuous=False) == {
        IPv4Network("10.0.0.0/25"),
        IPv4Network("10.0.0.128/25"),
        IPv4Network("10.0.1.0/25"),
        IPv4Network("10.0.1.128/25"),
    }


def test_find_gaps_with_gap():
    prefixes = [
        IPv4Network("10.0.0.0/25"),
        # IPv4Network("10.0.0.128/25"),  # gap
        IPv4Network("10.0.1.0/24"),
    ]
    assert find_prefix_gaps(prefixes=prefixes, min_gap_size=25) == {
        IPv4Network("10.0.0.0/23"): [IPv4Network("10.0.0.128/25")]
    }


def test_find_gaps_ipv6():
    prefixes = ["2001:db8:0:1::/64", "2001:db8:0:2::/64"]
    assert find_prefix_gaps(prefixes, min_gap_size=80) == {
        IPv6Network("2001:db8::/62"): [IPv6Network("2001:db8::/64"), IPv6Network("2001:db8:0:3::/64")]
    }


def test_find_gaps_with_no_gap():
    prefixes = [
        IPv4Network("10.0.0.0/24"),
        IPv4Network("10.0.1.0/24"),
    ]
    assert find_prefix_gaps(prefixes=prefixes, min_gap_size=32) == {}


def test_find_gaps_with_scope_change():
    prefixes = [
        IPv4Network("10.0.0.0/25"),
        # IPv4Network("10.0.0.128/25"),  # gap, but we look for gaps in minimum /25 long prefixes
        IPv4Network("10.0.1.0/24"),
    ]
    assert find_prefix_gaps(prefixes=prefixes, scope=25, min_gap_size=30) == {}


def test_find_gaps_with_two_gaps():
    prefixes = [
        IPv4Network("10.0.0.0/25"),
        # IPv4Network("10.0.0.128/25"),  # gap
        IPv4Network("10.0.1.0/24"),
        IPv4Network("10.0.2.0/25"),
        # IPv4Network("10.0.2.128/25"),  # gap
        IPv4Network("10.0.3.0/24"),
    ]
    assert find_prefix_gaps(prefixes=prefixes, scope=23, min_gap_size=25) == {
        IPv4Network("10.0.0.0/23"): [IPv4Network("10.0.0.128/25")],
        IPv4Network("10.0.2.0/23"): [IPv4Network("10.0.2.128/25")],
    }


def test_find_gaps_with_filtering():
    prefixes = [
        IPv4Network("10.0.0.1"),  # gap filtered
        IPv4Network("10.0.0.2"),  # gap filtered
        IPv4Network("10.0.0.3"),  # gap filtered
        # IPv4Network("10.0.0.4/30"),  # gap
        IPv4Network("10.0.0.8/29"),
    ]
    assert find_prefix_gaps(prefixes=prefixes, min_gap_size=30) == {
        IPv4Network("10.0.0.0/28"): [IPv4Network("10.0.0.4/30")],
    }
