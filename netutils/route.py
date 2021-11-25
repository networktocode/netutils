"""Utilities to get best route from routing table."""

import ipaddress
from typing import Union, List, Set, Dict


class NoRouteFound(BaseException):
    """Custom Exception for No Route Found."""


def longest_prefix_match(ip_addr, routes):
    """From a list of networks and an IP address, find the most specific route.

    Args:
        ip_addr (str): String representation of an IP address.
        routes (list): list of dictionaries with network and mask as keys. Subnet can also be CIDR(number) notation.

    Returns:
        [IPv4Network object]: Longest Match Route

    Example:
        >>> from netutils.route import longest_prefix_match
        >>> lookup = "10.1.1.245"
        >>> routes = [{"network": "192.168.1.1", "mask": "255.255.255.255"},{"network": "10.1.1.0", "mask": "24"}]
        >>> longest_prefix_match(lookup, routes)
        '10.1.1.0/24'
    """
    if not isinstance(routes, list):
        raise TypeError(f"'routing_table' should be a list, got {type(routes)}")
    if not len(routes) > 0:
        raise IndexError(f"'routing_table' should have more than zero indexes. Got {len(routes)}")
    if isinstance(ip_addr, str):
        ip_addr = ipaddress.ip_address(ip_addr)
    else:
        if not isinstance(ip_addr, (ipaddress.IPv4Address, ipaddress.IPv6Address)):
            raise TypeError(f"'ip_addr' should be a str, got {type(ip_addr)}")

    networks = [
        ipaddress.IPv4Network(f'{route["network"]}/{route["mask"]}')
        for route in routes
        if ip_addr in ipaddress.IPv4Network(f'{route["network"]}/{route["mask"]}')
    ]
    try:
        return str(sorted(networks)[-1])
    except IndexError as error:
        raise NoRouteFound("No Matching Route Found.") from error


IPNetwork = Union[ipaddress.IPv4Network, ipaddress.IPv6Network]


def prefix_aggregate(
    prefixes: List[Union[ipaddress.IPv4Network, ipaddress.IPv6Network, str]],
    force_continuous: bool = True,
    min_aggr_pref_len: int = 0,
) -> Set[Union[ipaddress.IPv4Network, ipaddress.IPv6Network]]:
    """Aggregate prefixes based on set minimum length and continuity

    Args:
        prefixes (str): list of prefixes as string or ``ipaddress`` network object
        force_continuous (boot): If ``True``, only consider continuous address range and don't make "holes" in the result
        min_aggr_pref_len (int): output should contain this big prefixes only

    Returns:
        Set of IPv4 or IPv6 Network objects which are aggregates for the input

    Example:
        >>> prefix_aggregate(["10.0.0.0/24", "10.0.1.0/24"])
        {IPv4Network('10.0.0.0/23')}

        >>> prefix_aggregate(["10.0.0.0/24", "10.0.2.0/24"])
        {IPv4Network('10.0.0.0/24'), IPv4Network('10.0.2.0/24')}

        >>> prefix_aggregate(["10.0.0.0/24", "10.0.2.0/24"], force_continuous=False)
        {IPv4Network('10.0.0.0/22')}

        >>> prefix_aggregate(["10.0.0.0/24", "10.0.2.0/24", "10.0.3.0/24"], force_continuous=False, min_aggr_pref_len=23)
        {IPv4Network('10.0.0.0/24'), IPv4Network('10.0.2.0/23')}
    """

    def eliminate_contained(_aggregate, _min_aggr_pref_len, _prefixes):
        _eliminated = False
        while _prefixes:
            if _aggregate.prefixlen < _min_aggr_pref_len:  # don't eliminate if we crossed the limit
                break
            if _prefixes[0].subnet_of(_aggregate):
                _prefixes.pop(0)  # eliminate contained prefix
                _eliminated = True
            else:  # skip checking the following elements as those are guaranteed not contained
                break
        return _eliminated

    aggregates = set()
    # validate input
    if not prefixes:
        return aggregates
    # check address family
    try:
        # assume ipv4
        family = type(ipaddress.IPv4Network(prefixes[0]))
    except (ipaddress.AddressValueError, ipaddress.NetmaskValueError):
        # try to use ipv6
        try:
            family = type(ipaddress.IPv6Network(prefixes[0]))
        except (ipaddress.AddressValueError, ipaddress.NetmaskValueError, ValueError) as err:
            raise ipaddress.AddressValueError("Please specify valid IPv4 or IPv6 networks!") from err
    assert (
        min_aggr_pref_len <= family(0).max_prefixlen
    ), f"min_aggr_pref_len is bigger than expected ({family.max_prefixlen})"
    # convert all input elements to ipaddress object
    prefixes = {family(prefix) for prefix in prefixes}
    prefixes = list(ipaddress.collapse_addresses(prefixes))

    # split prefixes where prefix length is too small
    while prefixes:
        aggregate = prefixes.pop(0)
        if aggregate.prefixlen < min_aggr_pref_len:
            aggregates.update(aggregate.subnets(prefixlen_diff=min_aggr_pref_len - aggregate.prefixlen))
        else:
            aggregates.add(aggregate)
    if force_continuous:
        return aggregates

    prefixes = list(aggregates)
    prefixes.sort()
    aggregates = set()

    min_aggregate = None  # store minimum prefix while searching for other contained prefixes
    while prefixes:
        aggregate: IPNetwork = prefixes.pop(0)
        eliminated = eliminate_contained(aggregate, min_aggr_pref_len, prefixes)
        if eliminated:
            min_aggregate = aggregate
        if aggregate.prefixlen > min_aggr_pref_len and prefixes:
            prefixes.insert(0, aggregate.supernet())
            if not min_aggregate:
                min_aggregate = aggregate
        else:
            aggregates.add(min_aggregate or aggregate)
            min_aggregate = None

    return aggregates


def find_prefix_gaps(
    prefixes: List[Union[ipaddress.IPv4Network, ipaddress.IPv6Network, str]], min_gap_size: int, scope: int = 0
) -> Dict[IPNetwork, List[IPNetwork]]:
    """Find gaps in given prefix list

    By default this function will find the longer possible aggregate prefix for the input. Then looks for gaps in
    that aggregate.
    The ``scope`` parameter can influence how long aggregates do we want to check at minimum.
    To limit how small gaps would be returned, set ``min_gap_size`` to a minimum prefix length.

    Args:
        prefixes: list of prefixes to be checked
        min_gap_size: filter out longer prefixes than that
        scope: determine the minimum prefix length

    Returns:
        list of IPvXNetwork objects which represents gaps in the given range

    Example:
        >>> find_prefix_gaps(["10.0.0.0/30", "10.0.0.12/30"], min_gap_size=30)
        {IPv4Network('10.0.0.0/28'): [IPv4Network('10.0.0.4/30'), IPv4Network('10.0.0.8/30')]}

        >>> find_prefix_gaps(["10.0.0.1", "10.0.0.1", "10.0.0.1", "10.0.0.8/29"], min_gap_size=30)
        {IPv4Network('10.0.0.0/28'): [IPv4Network('10.0.0.4/30')]}

        Without the scope, we would get a /21 aggregate with more gaps. With scope, we want /22 aggregates
        10.0.4.0/24 is not part of the 10.0.0.0/22 and as being a /24 itself has no gaps.

        >>> find_prefix_gaps(["10.0.0.0/24", "10.0.2.0/24", "10.0.3.0/24", "10.0.4.0/24"], min_gap_size=24, scope=22)
        {IPv4Network('10.0.0.0/22'): [IPv4Network('10.0.1.0/24')]}
    """
    gaps = {}
    assert 0 <= min_gap_size <= 128
    assert 0 <= scope <= 128

    supernets = prefix_aggregate(prefixes, min_aggr_pref_len=scope, force_continuous=False)
    continuous_prefs = prefix_aggregate(prefixes, min_aggr_pref_len=scope, force_continuous=True)

    for supernet in supernets:
        cps = {prefix for prefix in continuous_prefs if prefix.subnet_of(supernet)}
        max_prefix_len = max([prefix.prefixlen for prefix in cps])
        agg_split = prefix_aggregate([supernet], min_aggr_pref_len=max_prefix_len)
        pref_pool = set()
        for prefix in cps:
            pref_pool.update(prefix_aggregate([prefix], min_aggr_pref_len=max_prefix_len))
        gap_list = [
            prefix for prefix in ipaddress.collapse_addresses(agg_split - pref_pool) if prefix.prefixlen <= min_gap_size
        ]
        gap_list.sort()
        if gap_list:
            gaps[supernet] = gap_list
    return gaps
