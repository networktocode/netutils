"""Functions for working with IP addresses."""

import ipaddress
import typing as t
from operator import attrgetter

from netutils.constants import IPV4_MASKS, IPV6_MASKS

IPAddress = t.Union[ipaddress.IPv4Address, ipaddress.IPv6Address]


def ipaddress_address(ip: str, attr: str) -> t.Any:
    """Convenience function primarily built to expose ipaddress.ip_address to Jinja.

    Args:
        ip: IP Address str compliant with ipaddress.ip_address inputs.
        attr: An attribute in string dotted format.

    Returns:
        Returns the value provided by the ipaddress.ip_address attribute provided.

    Examples:
        >>> from netutils.ip import ipaddress_address
        >>> ipaddress_address('10.1.1.1', 'version')
        4
        >>> ipaddress_address('10.1.1.1', '__int__')
        167837953
        >>> ipaddress_address('10.1.1.1', 'is_loopback')
        False
        >>>
    """
    retriever = attrgetter(attr)
    retrieved_method = retriever(ipaddress.ip_address(ip))
    if callable(retrieved_method):
        return retrieved_method()
    return retrieved_method


def ipaddress_interface(ip: str, attr: str) -> t.Any:
    """Convenience function primarily built to expose ipaddress.ip_interface to Jinja.

    Args:
        ip: IP interface str compliant with ipaddress.ip_interface inputs.
        attr: An attribute in string dotted format.

    Returns:
        Returns the value provided by the ipaddress.ip_interface attribute provided.

    Examples:
        >>> from netutils.ip import ipaddress_interface
        >>> ipaddress_interface('10.1.1.1/24', 'version')
        4
        >>> ipaddress_interface('10.1.1.1/24', '__int__')
        167837953
    """
    retriever = attrgetter(attr)
    retrieved_method = retriever(ipaddress.ip_interface(ip))
    if callable(retrieved_method):
        return retrieved_method()
    return retrieved_method


def ipaddress_network(ip: str, attr: str) -> t.Any:
    """Convenience function primarily built to expose ipaddress.ip_network to Jinja.

    Args:
        ip: IP network str compliant with ipaddress.ip_network inputs.
        attr: An attribute in string dotted format.

    Returns:
        Returns the value provided by the ipaddress.ip_network attribute provided.

    Examples:
        >>> from netutils.ip import ipaddress_network
        >>> ipaddress_network('10.1.1.0/24', 'version')
        4
        >>> ipaddress_network('10.1.1.0/24', '__str__')
        '10.1.1.0/24'
        >>>
    """
    retriever = attrgetter(attr)
    retrieved_method = retriever(ipaddress.ip_network(ip))
    if callable(retrieved_method):
        return retrieved_method()
    return retrieved_method


def ip_to_hex(ip: str) -> str:
    """Converts an IP address in string format to a hex string.

    Args:
        ip: An IP address in string format that is able to be converted by `ipaddress` library.

    Returns:
        HEX value of the IP address.

    Examples:
        >>> from netutils.ip import ip_to_hex
        >>> ip_to_hex("10.100.100.100")
        '0a646464'
        >>>
    """
    ip_obj = ipaddress.ip_address(ip)
    return str(hex(int(ip_obj)))[2:].zfill(int(ip_obj.max_prefixlen / 4))


def ip_addition(ip: str, val: int) -> str:
    """Adds an integer to an IP address.

    Args:
        ip: An IP address in string format that is able to be converted by `ipaddress` library.
        val: An integer of which the IP address should be added by.

    Returns:
        IP address formatted string with the newly added IP address.

    Examples:
        >>> from netutils.ip import ip_addition
        >>> ip_addition("10.100.100.100", 200)
        '10.100.101.44'
        >>>
    """
    return str(ipaddress.ip_address(ip) + val)


def ip_to_bin(ip: str) -> str:
    """Converts an IP address in string format to a binary string.

    Args:
        ip: An IP address in string format that is able to be converted by `ipaddress` library.

    Returns:
        Binary value of the IP address.

    Examples:
        >>> from netutils.ip import ip_to_bin
        >>> ip_to_bin("10.100.100.100")
        '00001010011001000110010001100100'
        >>>
    """
    ip_obj = ipaddress.ip_address(ip)
    return bin(int(ip_obj))[2:].zfill(ip_obj.max_prefixlen)


def ip_subtract(ip: str, val: int) -> str:
    """Subtract an integer to an IP address.

    Args:
        ip: An IP address in string format that is able to be converted by `ipaddress` library.
        val: An integer of which the IP address should be subtracted by.

    Returns:
        IP address formatted string with the newly subtracted IP address.

    Examples:
        >>> from netutils.ip import ip_subtract
        >>> ip_subtract("10.100.100.100", 200)
        '10.100.99.156'
        >>>
    """
    return str(ipaddress.ip_address(ip) - val)


def is_classful(ip_network: str) -> bool:  # noqa: D300,D301
    """Determines if a CIDR network address is within unicast classful boundaries.

       The following class boundaries are checked:

       * Class A: 0.0.0.0/8 -> 127.0.0.0/8
       * Class B: 128.0.0.0/16 -> 191.255.0.0/16
       * Class C: 192.0.0.0/24 -> 223.255.255.0/24

    Args:
        ip_network: A network string that can be parsed by ipaddress.ip_network.

    Returns:
        Whether or not the network falls within classful boundaries.

    Examples:
        >>> from netutils.ip import is_classful
        >>> is_classful("192.168.0.0/24")
        True

        >>> from jinja2 import Environment
        >>> from netutils.utils import jinja2_convenience_function
        >>>
        >>> env = Environment(trim_blocks=True, lstrip_blocks=True)
        >>> env.filters.update(jinja2_convenience_function())
        >>>
        >>> template_str = \"\"\"
        ... {%- for net in networks %}
        ...   {% if net | is_classful %}
        ...   network {{ net | ipaddress_network('network_address') }}
        ...   {% else %}
        ...   network {{ net | ipaddress_network('network_address') }} mask {{ net | ipaddress_network('netmask') }}
        ...   {% endif %}
        ... {% endfor -%}
        ... \"\"\"
        >>> template = env.from_string(template_str)
        >>> result = template.render({"networks": ["192.168.1.0/24", "172.16.1.0/24"]})
        >>> print(result, end="")
          network 192.168.1.0
          network 172.16.1.0 mask 255.255.255.0
    """
    net = ipaddress.ip_network(ip_network)
    # Only IPv4 addresses can be classified as classful
    if net.version != 4:
        return False
    first_octet = net.network_address.packed[0]
    netmask = int(net.netmask)
    return (
        ((first_octet & 0x80 == 0x00) and (netmask == 0xFF000000))  # Class A
        or ((first_octet & 0xC0 == 0x80) and (netmask == 0xFFFF0000))  # Class B
        or ((first_octet & 0xE0 == 0xC0) and (netmask == 0xFFFFFF00))  # Class C
    )


def is_ip(ip: str) -> bool:
    """Verifies whether or not a string is a valid IP address.

    Args:
        ip: An IP address in string format that is able to be converted by `ipaddress` library.

    Returns:
        The result as to whether or not the string is a valid IP address.

    Examples:
        >>> from netutils.ip import is_ip
        >>> is_ip("10.100.100.256")
        False
        >>> is_ip("10.100.100.255")
        True
        >>>
    """
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


def is_ip_range(ip_range: str) -> bool:
    """Verifies whether or not a string is a valid IP address range.

    An `ip_range` is in the format of `{ip_start}-{ip_end}`, IPs in str format, same IP version, and
    ip_start is before ip_end.

    Args:
        ip_range: An IP address range in string format that is properly formatted.

    Returns:
        The result as to whether or not the string is a valid IP address.

    Examples:
        >>> from netutils.ip import is_ip_range
        >>> is_ip_range("10.100.100.255")
        False
        >>> is_ip_range("10.100.100.255-10.100.101.1")
        True
        >>>
    """
    if "-" not in ip_range:
        return False
    start_ip, end_ip = ip_range.split("-")
    if not is_ip(start_ip) or not is_ip(end_ip):
        return False
    start_ip_obj = ipaddress.ip_address(start_ip)
    end_ip_obj = ipaddress.ip_address(end_ip)
    if not isinstance(start_ip_obj, type(end_ip_obj)):
        return False
    # IP version being the same is enforced above, mypy disagrees, can safely ignore
    if not start_ip_obj < end_ip_obj:  # type: ignore
        return False
    return True


def is_ip_within(ip: str, ip_compare: t.Union[str, t.List[str]]) -> bool:
    """
    Check if an IP address, IP subnet, or IP range is within the range of a list of IP addresses, IP subnets, and IP ranges.

    Args:
        ip: IP address, IP subnet, or IP range to check.
        ip_compare: String or list of IP addresses, IP subnets, and IP ranges to compare against.

    Returns:
        True if the IP is in range, False otherwise.

    Examples:
        >>> from netutils.ip import is_ip_within
        >>> is_ip_within("10.100.100.10", "10.100.100.0/24")
        True
        >>> is_ip_within("10.100.100.0/25", ["10.100.100.0/24", "10.100.200.0/24"])
        True
        >>>
        >>> is_ip_within("10.100.100.10", ["10.100.100.8-10.100.100.20", "10.100.200.0/24"])
        True
        >>> is_ip_within("10.100.100.8-10.100.100.20", ["10.100.100.0/24"])
        True
        >>> is_ip_within("1.1.1.1", ["2.2.2.2", "3.3.3.3"])
        False
        >>>
    """

    def _convert_ip(ip: str) -> str:
        if is_ip(ip):
            if "." in ip:
                mask = "32"
            if ":" in ip:
                mask = "128"
            return f"{ip}/{mask}"
        return ip

    if "-" in ip:
        ip_obj_start, ip_obj_end = get_range_ips(ip)
    else:
        ip_obj = ipaddress.ip_network(_convert_ip(ip))
        ip_obj_start = ip_obj[0]
        ip_obj_end = ip_obj[-1]

    if isinstance(ip_compare, str):
        ip_compare = [ip_compare]

    for item in ip_compare:
        if "-" in item:
            item_obj_start, item_obj_end = get_range_ips(item)

        else:
            item_obj = ipaddress.ip_network(_convert_ip(item))
            item_obj_start = item_obj[0]
            item_obj_end = item_obj[-1]
        if not isinstance(item_obj_start, type(item_obj_end)):
            raise ValueError(
                f"IP range start `{item_obj_start}` and end `{item_obj_end}` IPs must both be same IPVersion."
            )
        # Use this validation method, since it is consitent with ranges
        # vs the `.subnet_of` method which is not.
        if item_obj_start <= ip_obj_start <= ip_obj_end <= item_obj_end:  # type: ignore
            return True
    return False


def is_netmask(netmask: str) -> bool:
    """Verifies whether or not a string is a valid subnet mask.

    Args:
        netmask: A subnet mask in

    Returns:
        True if string is a valid subnet mask. Otherwise, false.

    Examples:
        >>> from netutils.ip import is_netmask
        >>> is_netmask('255.255.255.0')
        True
        >>> is_netmask('24')
        False
        >>> is_netmask('255.255.266.0')
        False
    """
    try:
        return int(ipaddress.ip_address(netmask)) in IPV4_MASKS or int(ipaddress.ip_address(netmask)) in IPV6_MASKS
    except ValueError:
        return False


def is_network(ip_network: str) -> bool:
    """Verifies whether or not a string is a valid IP Network with a Mask.

    Args:
        ip: An IP network in string format that is able to be converted by `ipaddress` library.

    Returns:
        The result as to whether or not the string is a valid IP network.

    Examples:
        >>> from netutils.ip import is_network
        >>> is_network("10.100.100.0")
        False
        >>> is_network("10.100.100.0/24")
        True
        >>>
    """
    if "/" not in ip_network:
        return False
    try:
        ipaddress.ip_network(ip_network)
        return True
    except ValueError:
        return False


def netmask_to_cidr(netmask: str) -> int:
    """Creates a CIDR notation of a given subnet mask in decimal format.

    Args:
        netmask: A subnet mask in decimal format.

    Returns:
        CIDR representation of subnet mask.

    Examples:
        >>> from netutils.ip import netmask_to_cidr
        >>> netmask_to_cidr("255.255.255.0")
        24
        >>> netmask_to_cidr("255.255.254.0")
        23
    """
    if is_netmask(netmask):
        return bin(int(ipaddress.ip_address(netmask))).count("1")
    raise ValueError("Subnet mask is not valid.")


def cidr_to_netmask(cidr: int) -> str:
    """Creates a decimal format of a CIDR value.

    **IPv4** only.  For IPv6, please use `cidr_to_netmaskv6`.

    Args:
        cidr: A CIDR value.

    Returns:
        Decimal format representation of CIDR value.

    Examples:
        >>> from netutils.ip import cidr_to_netmask
        >>> cidr_to_netmask(24)
        '255.255.255.0'
        >>> cidr_to_netmask(17)
        '255.255.128.0'
    """
    if isinstance(cidr, int) and 0 <= cidr <= 32:
        return ".".join([str((0xFFFFFFFF << (32 - cidr) >> i) & 0xFF) for i in [24, 16, 8, 0]])
    raise ValueError("Parameter must be an integer between 0 and 32.")


def cidr_to_netmaskv6(cidr: int) -> str:
    """Creates a decimal format of a CIDR value.

    Args:
        cidr: A CIDR value.

    Returns:
        Decimal format (IPv6) representation of CIDR value.

    Examples:
        >>> from netutils.ip import cidr_to_netmaskv6
        >>> cidr_to_netmaskv6(24)
        'ffff:ff00::'
        >>> cidr_to_netmaskv6(17)
        'ffff:8000::'
    """
    if isinstance(cidr, int) and 0 <= cidr <= 128:
        return str(ipaddress.IPv6Address(((1 << cidr) - 1) << (128 - cidr)))
    raise ValueError("Parameter must be an integer between 0 and 128.")


def get_all_host(ip_network: str) -> t.Generator[str, None, None]:
    """Given a network, return the list of usable IP addresses.

    Args:
        ip_network: An IP network in string format that is able to be converted by `ipaddress` library.

    Returns:
        Generator of usable IP Addresses within network.

    Examples:
        >>> from netutils.ip import get_all_host
        >>> print(list(get_all_host("10.100.100.0/29")))
        ['10.100.100.1', '10.100.100.2', '10.100.100.3', '10.100.100.4', '10.100.100.5', '10.100.100.6']
        >>>
    """
    return (str(ip) for ip in ipaddress.ip_network(ip_network).hosts())


def get_broadcast_address(ip_network: str) -> str:
    """Given a network, determine the broadcast IP address.

    Args:
        ip_network: An IP network in string format that is able to be converted by `ipaddress` library.

    Returns:
        IP address formatted string with the broadcast IP address in the network.

    Examples:
        >>> from netutils.ip import get_broadcast_address
        >>> get_broadcast_address("10.100.0.0/16")
        '10.100.255.255'
        >>>
    """
    return str(ipaddress.ip_network(ip_network).broadcast_address)


def get_first_usable(ip_network: str) -> str:
    """Given a network, determine the first usable IP address.

    Args:
        ip_network: An IP network in string format that is able to be converted by `ipaddress` library.

    Returns:
        IP address formatted string with the first usable IP address in the network.

    Examples:
        >>> from netutils.ip import get_first_usable
        >>> get_first_usable("10.100.0.0/16")
        '10.100.0.1'
        >>>
    """
    net = ipaddress.ip_network(ip_network)
    if net.prefixlen in [31, 127]:
        return str(net[0])
    return str(net[1])


def get_peer_ip(ip_interface: str) -> str:
    """Given an IP interface (an ip address, with subnet mask) that is on a peer network, return the peer IP.

    Args:
        ip_interface: An IP interface in string format that is able to be converted by `ipaddress` library.

    Returns:
        IP address formatted string with the corresponding peer IP.

    Examples:
        >>> from netutils.ip import get_peer_ip
        >>> get_peer_ip('10.0.0.1/255.255.255.252')
        '10.0.0.2'
        >>> get_peer_ip('10.0.0.2/30')
        '10.0.0.1'
        >>> get_peer_ip('10.0.0.1/255.255.255.254')
        '10.0.0.0'
        >>> get_peer_ip('10.0.0.0/31')
        '10.0.0.1'
        >>>
    """
    ip_obj = ipaddress.ip_interface(ip_interface)
    if isinstance(ip_obj, ipaddress.IPv4Address) and ip_obj.network.prefixlen not in [30, 31]:
        raise ValueError(f"{ip_obj} did not conform to IPv4 acceptable masks of 30 or 31")
    if isinstance(ip_obj, ipaddress.IPv6Address) and ip_obj.network.prefixlen not in [126, 127]:
        raise ValueError(f"{ip_obj} did not conform to IPv6 acceptable masks of 126 or 127")
    if ip_obj.network.prefixlen in [30, 126] and ip_obj.ip in [
        ip_obj.network.network_address,
        ip_obj.network.broadcast_address,
    ]:
        raise ValueError(f"{ip_obj} is not an IP in the point-to-point link usable range.")
    # The host lists returns all usable IPs, remove the matching one, return the first element. This can be optimized greatly, but left
    # like this for simplicity. Note: IPv6 technically does not have a broadcast address, but for ptp, this is not considered.
    val = list(get_all_host(str(ip_obj.network)))
    val.remove(str(ip_obj.ip))
    return val[0]


def get_range_ips(ip_range: str) -> t.Tuple[IPAddress, IPAddress]:
    """Get's the two IPs as a tuple of IPAddress objects.

    Args:
        ip_range: An IP address range in string format that is properly formatted.

    Returns:
        The start and end IP address of the range provided.

    Examples:
        >>> from netutils.ip import get_range_ips
        >>> get_range_ips("10.100.100.255-10.100.101.1")
        (IPv4Address('10.100.100.255'), IPv4Address('10.100.101.1'))
        >>> get_range_ips("2001::1-2001::10")
        (IPv6Address('2001::1'), IPv6Address('2001::10'))
        >>>
    """
    if not is_ip_range(ip_range):
        raise ValueError(r"Not a valid IP range format of `{start_ip}-{end_ip}`")
    start_ip, end_ip = ip_range.split("-")
    start_ip_obj = ipaddress.ip_address(start_ip)
    end_ip_obj = ipaddress.ip_address(end_ip)
    return start_ip_obj, end_ip_obj


def get_usable_range(ip_network: str) -> str:
    """Given a network, return the string of usable IP addresses.

    Args:
        ip_network: An IP network in string format that is able to be converted by `ipaddress` library.

    Returns:
        String of usable IP Addresses within network.

    Examples:
        >>> from netutils.ip import get_usable_range
        >>> get_usable_range("10.100.100.0/29")
        '10.100.100.1 - 10.100.100.6'
        >>>
    """
    net = ipaddress.ip_network(ip_network)
    if net.prefixlen in [31, 127]:
        lower_bound = str(net[0])
        upper_bound = str(net[1])
    else:
        lower_bound = str(net[1])
        upper_bound = str(net[-2])
    return f"{lower_bound} - {upper_bound}"


def get_ips_sorted(ips: t.Union[str, t.List[str]], sort_type: str = "network") -> t.List[str]:
    """Given a concatenated list of CIDRs sorts them into the correct order and returns them as a list.

    Examples:
        >>> from netutils.ip import get_ips_sorted
        >>> get_ips_sorted("3.3.3.3,2.2.2.2,1.1.1.1")
        ['1.1.1.1/32', '2.2.2.2/32', '3.3.3.3/32']
        >>> get_ips_sorted("10.0.20.0/24,10.0.20.0/23,10.0.19.0/24")
        ['10.0.19.0/24', '10.0.20.0/23', '10.0.20.0/24']
        >>> get_ips_sorted("10.0.20.0/24,10.0.20.0/23,10.0.19.0/24", "interface")
        ['10.0.19.0/24', '10.0.20.0/23', '10.0.20.0/24']
        >>> get_ips_sorted("10.0.20.20/24,10.0.20.1/23,10.0.19.5/24", "interface")
        ['10.0.19.5/24', '10.0.20.1/23', '10.0.20.20/24']
        >>> get_ips_sorted(["10.0.20.20", "10.0.20.1", "10.0.19.5"], "address")
        ['10.0.19.5', '10.0.20.1', '10.0.20.20']

    Args:
        ips (t.Union[str, t.List[str]]): Concatenated string list of CIDRs, IPAddresses, or Interfaces or list of the same strings.
        sort_type (str): Whether the passed list are networks, IP addresses, or interfaces, ie "address", "interface", or "network".

    Returns:
        t.List[str]: Sorted list of sort_type IPs.
    """
    if sort_type not in ["address", "interface", "network"]:
        raise ValueError("Invalid sort type passed. Must be `address`, `interface`, or `network`.")
    if isinstance(ips, list):
        ips_list = ips
    elif (isinstance(ips, str) and "," not in ips) or not isinstance(ips, str):
        raise ValueError("Not a concatenated list of IPs as expected.")
    elif isinstance(ips, str):
        ips_list = ips.replace(" ", "").split(",")

    functions: t.Dict[str, t.Callable[[t.Any], t.Any]] = {
        "address": ipaddress.ip_address,
        "interface": ipaddress.ip_interface,
        "network": ipaddress.ip_network,
    }

    try:
        sorted_list = sorted(functions[sort_type](ip) for ip in ips_list)
        if sort_type in ["interface", "network"]:
            return [cidrs.with_prefixlen for cidrs in sorted_list]
        return [str(ip) for ip in sorted_list]
    except ValueError as err:
        raise ValueError(f"Invalid IP of {sort_type} input: {err}") from err
