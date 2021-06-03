"""Utilities to get best route from routing table."""

import ipaddress


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
        if not isinstance(ipaddress.ip_address, ip_addr):
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
