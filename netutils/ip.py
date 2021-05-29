"""Functions for working with IP addresses."""
# pylint: disable=invalid-name
import ipaddress


def ip_to_hex(ip):
    """Converts an IP address in string format to a hex string.

    Args:
        ip (str): An IP address in string format that is able to be converted by `ipaddress` library.

    Returns:
        str: HEX value of the IP address.

    Example:
        >>> from netutils.ip import ip_to_hex
        >>> ip_to_hex("10.100.100.100")
        'a646464'
        >>>
    """
    return str(hex(int(ipaddress.ip_address(ip))))[2:]


def ip_addition(ip, val):
    """Adds an integer to an IP address.

    Args:
        ip (str): An IP address in string format that is able to be converted by `ipaddress` library.
        val (int): An integer of which the IP address should be added by.

    Returns:
        str: IP address formatted string with the newly added IP address.

    Example:
        >>> from netutils.ip import ip_addition
        >>> ip_addition("10.100.100.100", 200)
        '10.100.101.44'
        >>>
    """
    return str(ipaddress.ip_address(ip) + val)


def ip_to_bin(ip):
    """Converts an IP address in string format to a binary string.

    Args:
        ip (str): An IP address in string format that is able to be converted by `ipaddress` library.

    Returns:
        str: Binary value of the IP address.

    Example:
        >>> from netutils.ip import ip_to_bin
        >>> ip_to_bin("10.100.100.100")
        '1010011001000110010001100100'
        >>>
    """
    return str(bin(int(ipaddress.ip_address(ip))))[2:]


def ip_subtract(ip, val):
    """Subtract an integer to an IP address.

    Args:
        ip (str): An IP address in string format that is able to be converted by `ipaddress` library.
        val (int): An integer of which the IP address should be subtracted by.

    Returns:
        str: IP address formatted string with the newly subtracted IP address.

    Example:
        >>> from netutils.ip import ip_subtract
        >>> ip_subtract("10.100.100.100", 200)
        '10.100.99.156'
        >>>
    """
    return str(ipaddress.ip_address(ip) - val)


def is_ip(ip):
    """Verifies whether or not a string is a valid IP address.

    Args:
        ip (str): An IP address in string format that is able to be converted by `ipaddress` library.

    Returns:
        bool: The result as to whether or not the string is a valid IP address.

    Example:
        >>> from netutils.ip import is_ip
        >>> is_ip("10.100.100.256")
        False
        >>> is_ip("10.100.100.255")
        True
        >>>
    """
    try:
        ip = ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


def is_netmask(netmask):
    """Verifies whether or not a string is a valid subnet mask.

    Args:
        netmask (str): A subnet mask in

    Returns:
        bool: True if string is a valid subnet mask. Otherwise, false.

    Example:
        >>> from netutils.ip import is_netmask
        >>> is_netmask('255.255.255.0')
        True
        >>> is_netmask('24')
        False
        >>> is_netmask('255.255.266.0')
        False
    """
    try:
        return netmask == str(ipaddress.IPv4Network(f"0.0.0.0/{netmask}").netmask)
    except ipaddress.NetmaskValueError:
        return False


def netmask_to_cidr(netmask):
    """Creates a CIDR notation of a given subnet mask in decimal format.

    Args:
        netmask (str): A subnet mask in decimal format.

    Returns:
      cidr (str): CIDR representation of subnet mask.

    Example:
        >>> from netutils.ip import netmask_to_cidr
        >>> netmask_to_cidr("255.255.255.0")
        24
        >>> netmask_to_cidr("255.255.254.0")
        23
    """
    if is_netmask(netmask):
        return sum(bin(int(x)).count("1") for x in netmask.split("."))
    raise ValueError("Subnet mask is not valid.")


def cidr_to_netmask(cidr):
    """Creates a decimal format of a CIDR value.

    Args:
        cidr (int): A CIDR value.

    Returns:
      netmask (str): Decimal format representation of CIDR value.

    Example:
        >>> from netutils.ip import netmask_to_cidr
        >>> cidr_to_netmask(24)
        '255.255.255.0'
        >>> cidr_to_netmask(17)
        '255.255.128.0'
    """
    if isinstance(cidr, int) and 0 <= cidr <= 32:
        return ".".join([str((0xFFFFFFFF << (32 - cidr) >> i) & 0xFF) for i in [24, 16, 8, 0]])
    raise ValueError("Parameter must be an integer between 0 and 32.")


def get_all_host(ip_network):
    """Given a network, return the list of usable IP addresses.

    Args:
        ip_network (str): An IP network in string format that is able to be converted by `ipaddress` library.

    Returns:
        list: List of usable IP Addresses within network.

    Example:
        >>> from netutils.ip import get_all_host
        >>> print(get_all_host("10.100.100.0/29"))
        ['10.100.100.1', '10.100.100.2', '10.100.100.3', '10.100.100.4', '10.100.100.5', '10.100.100.6']
        >>>
    """
    return [str(ip) for ip in ipaddress.ip_network(ip_network).hosts()]


def get_broadcast_address(ip_network):
    """Given a network, determine the broadcast IP address.

    Args:
        ip_network (str): An IP network in string format that is able to be converted by `ipaddress` library.

    Returns:
        str: IP address formatted string with the broadcast IP address in the network.

    Example:
        >>> from netutils.ip import get_broadcast_address
        >>> get_broadcast_address("10.100.0.0/16")
        '10.100.255.255'
        >>>
    """
    return str(ipaddress.ip_network(ip_network).broadcast_address)


def get_first_usable(ip_network):
    """Given a network, determine the first usable IP address.

    Args:
        ip_network (str): An IP network in string format that is able to be converted by `ipaddress` library.

    Returns:
        str: IP address formatted string with the first usable IP address in the network.

    Example:
        >>> from netutils.ip import get_first_usable
        >>> get_first_usable("10.100.0.0/16")
        '10.100.0.1'
        >>>
    """
    net = ipaddress.ip_network(ip_network)
    if net.prefixlen == 31 or net.prefixlen == 127:
        return str(net[0])
    return str(net[1])


def get_usable_range(ip_network):
    """Given a network, return the string of usable IP addresses.

    Args:
        ip_network (str): An IP network in string format that is able to be converted by `ipaddress` library.

    Returns:
        str: String of usable IP Addresses within network.

    Example:
        >>> from netutils.ip import get_usable_range
        >>> get_usable_range("10.100.100.0/29")
        '10.100.100.1 - 10.100.100.6'
        >>>
    """
    net = ipaddress.ip_network(ip_network)
    if net.prefixlen == 31 or net.prefixlen == 127:
        lower_bound = str(net[0])
        upper_bound = str(net[1])
    else:
        lower_bound = str(net[1])
        upper_bound = str(net[-2])
    return f"{lower_bound} - {upper_bound}"
