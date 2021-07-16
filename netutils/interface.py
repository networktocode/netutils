"""Functions for working with interface."""
import re
import itertools
from typing import Union, List, Tuple
from operator import itemgetter
from .constants import BASE_INTERFACES, REVERSE_MAPPING


def interface_range_expansion(interface_pattern):
    """Expand interface pattern into a list of interfaces.

    Args:
        interface_pattern (str): The string pattern that will be parsed to create the list of interfaces.

    Returns:
        list: Contains the expanded list of interfaces.

    Example:
        >>> from netutils.interface import interface_range_expansion
        >>> interface_range_expansion("Gi0/[1-4]")
        ['Gi0/1', 'Gi0/2', 'Gi0/3', 'Gi0/4']
        >>> interface_range_expansion("FastEthernet[1-2]/0/[10-15]")
        ['FastEthernet1/0/10', 'FastEthernet1/0/11', 'FastEthernet1/0/12', 'FastEthernet1/0/13', 'FastEthernet1/0/14', 'FastEthernet1/0/15', 'FastEthernet2/0/10', 'FastEthernet2/0/11', 'FastEthernet2/0/12', 'FastEthernet2/0/13', 'FastEthernet2/0/14', 'FastEthernet2/0/15']
    """

    def _range_expand(regex_match):
        number_range = []
        for value in regex_match.split(","):
            if "-" in value[1:]:
                first_number, second_number = value[1:].split("-", 1)
                number_range += range(int(value[0] + first_number), int(second_number) + 1)
            else:
                number_range.append(int(value))
        return number_range

    def _pairwise(interface_constant):
        interface_constant_it = iter(interface_constant)
        return list(zip(interface_constant_it, interface_constant_it))

    match_pattern = r"(\[(?:\d|,|-)+\])"
    re_compiled = re.compile(match_pattern)
    # Use case when sent without an actual range, e.g. Gi1
    if not re_compiled.search(interface_pattern):
        return [interface_pattern]

    cartesian_list = []
    interface_constant = [0]
    for match in re_compiled.finditer(interface_pattern):
        interface_constant.append(match.start())
        interface_constant.append(match.end())
        cartesian_list.append(_range_expand(match.group()[1:-1]))

    interface_constant_out = _pairwise(interface_constant)
    expanded_interfaces = []
    for element in itertools.product(*cartesian_list):
        current_interface = ""
        for count, item in enumerate(interface_constant_out):
            current_interface += interface_pattern[item[0] : item[1]]  # noqa: E203
            current_interface += str(element[count])
        expanded_interfaces.append(current_interface)

    return expanded_interfaces


def split_interface(interface):
    """Split an interface name based on first digit, slash, or space match.

    Args:
        interface (str): The interface you are attempting to split.

    Returns:
        tuple: The split between the name of the interface the value.

    Example:
        >>> from netutils.interface import split_interface
        >>> split_interface("GigabitEthernet1/0/1")
        ('GigabitEthernet', '1/0/1')
        >>> split_interface("Eth1")
        ('Eth', '1')
        >>>
    """
    head = interface.rstrip(r"/\0123456789. ")
    tail = interface[len(head) :].lstrip()  # noqa: E203
    return (head, tail)


def canonical_interface_name(interface, addl_name_map=None, verify=False):
    """Function to return an interface's canonical name (fully expanded name).

    Use of explicit matches used to indicate a clear understanding on any potential
    match. Regex and other looser matching methods were not implemented to avoid false
    positive matches. As an example, it would make sense to do "[P|p][O|o]" which would
    incorrectly match PO = POS and Po = Port-channel, leading to a false positive, not
    easily troubleshot, found, or known.

    Args:
        interface (str): The interface you are attempting to expand.
        addl_name_map (dict, optional): A dict containing key/value pairs that updates the base mapping. Used if an OS has specific differences. e.g. {"Po": "PortChannel"} vs {"Po": "Port-Channel"}. Defaults to None.
        verify (bool, optional): Whether or not to verify the interface matches a known interface standard. Defaults to False.

    Returns:
        str: The name of the interface in the long form.

    Example:
        >>> from netutils.interface import canonical_interface_name
        >>> canonical_interface_name("Gi1/0/1")
        'GigabitEthernet1/0/1'
        >>> canonical_interface_name("Eth1")
        'Ethernet1'
        >>>
    """
    name_map = {}
    name_map.update(BASE_INTERFACES)
    interface_type, interface_number = split_interface(interface)

    if isinstance(addl_name_map, dict):
        name_map.update(addl_name_map)
    # check in dict for mapping
    if name_map.get(interface_type):
        long_int = name_map.get(interface_type)
        return long_int + str(interface_number)
    if verify:
        raise ValueError(f"Verify interface on and no match found for {interface}")
    # if nothing matched, return the original name
    return interface


def abbreviated_interface_name(interface, addl_name_map=None, addl_reverse_map=None, verify=False):
    """Function to return an abbreviated representation of the interface name.

    Args:
        interface (str): The interface you are attempting to shorten.
        addl_name_map (dict, optional): A dict containing key/value pairs that updates the base mapping. Used if an OS has specific differences. e.g. {"Po": "PortChannel"} vs {"Po": "Port-Channel"}. Defaults to None.
        addl_reverse_map (dict, optional): A dict containing key/value pairs that updates the abbreviated mapping. Defaults to None.
        verify (bool, optional): Whether or not to verify the interface matches a known interface standard. Defaults to False.

    Returns:
        str: The name of the interface in the abbreviated form.

    Example:
        >>> abbreviated_interface_name("GigabitEthernet1/0/1")
        'Gi1/0/1'
        >>> abbreviated_interface_name("Eth1")
        'Et1'
        >>>
    """
    name_map = {}
    name_map.update(BASE_INTERFACES)
    interface_type, interface_number = split_interface(interface)

    if isinstance(addl_name_map, dict):
        name_map.update(addl_name_map)

    rev_name_map = {}
    rev_name_map.update(REVERSE_MAPPING)

    if isinstance(addl_reverse_map, dict):
        rev_name_map.update(addl_reverse_map)

    # Try to ensure canonical type.
    if name_map.get(interface_type):
        canonical_type = name_map.get(interface_type)
    else:
        canonical_type = interface_type

    try:
        abbreviated_name = rev_name_map[canonical_type] + str(interface_number)
        return abbreviated_name

    except KeyError:
        pass

    if verify:
        raise ValueError(f"Verify interface on and no match found for {interface}")
    # If abbreviated name lookup fails, return original name
    return interface


def interface_range_generator(
    interfaces: Union[str, List[str]] = None, prefix: str = "interface range ", max_ranges: int = 5
) -> List[str]:
    """Function which takes interfaces and return interface ranges.
    Ranges are based on last interface part (aka ports).
    Whitespace and special characters are ignored in the input.

    Example:
        >>> interface_range_generator("Gi1/0/1 Gi1/0/2 Gi1/0/4")
        'interface range Gi1/0/1-2,Gi1/0/4'
        >>> interface_range_generator(["Gi1/0/1 Gi1/0/2","Gi1/0/3,Gi1/0/4"])
        'interface range Gi1/0/1-4'

    Args:
        prefix: prefix string used in each line of the output
        interfaces: interfaces in a line or in a list of lines
        max_ranges: maximum number of ranges in one line in the output

    Returns:
        lines of interface range commands (or ranges with specified prefix)
    """

    def to_port(port_in: Tuple[str, int, int, int, int]):
        """Assemble exploded port_in
        Separator is `/`. -1 value means that value is not used.
        Only physical ports are supported.
        Example: Gi, 1, 0, 1, -1 will become: Gi1/0/1

        Args:
            port_in: tuple of port name and fex, chasses, module, interface numbers

        Returns:
            string of assembled interface
        """
        out = port_in[0]
        if port_in[1] >= 0:
            out += str(port_in[1])
            if port_in[2] >= 0:
                out += "/" + str(port_in[2])
                if port_in[3] >= 0:
                    out += "/" + str(port_in[3])
                    if port_in[4] >= 0:
                        out += "/" + str(port_in[4])
        return out

    ports = []  # collect exploded interfaces
    # case insensitive port parsing. We do a hard assumption that we only have ports in the input.
    # we support 4 module depth. This is enough for Cisco FEX.
    port_regex = re.compile(r"(?i)([a-z]+)([0-9]+)(?:/([0-9]+))?(?:/([0-9]+))?(?:/([0-9]+))?")
    output = []
    if interfaces is None:
        return output
    ports_in = [interfaces] if type(interfaces) is str else interfaces
    # read all lines and explode all interfaces as preparation for sorting
    for line in ports_in:
        matches = port_regex.findall(line)
        for match in matches:
            port_name = match[0]
            port1 = int(match[1]) if len(match[1]) > 0 else -1
            port2 = int(match[2]) if len(match[2]) > 0 else -1
            port3 = int(match[3]) if len(match[3]) > 0 else -1
            port4 = int(match[4]) if len(match[4]) > 0 else -1
            ports.append((port_name, port1, port2, port3, port4))

    # sort exploded interface data in order to prepare for finding ranges
    ports = sorted(ports, key=itemgetter(0, 1, 2, 3, 4))  # Sort interfaces
    if not ports:  # could not read interfaces from input
        return []
    range_start = ports[0]  # contains interface range start (Gi0/0)
    range_index = 1  # counts number of ranges on line (gi0/0-1,g0/3-5 = 2)
    current_port = range_start
    last_port_index = 1
    outline = "%s%s" % (prefix, to_port(range_start))
    i = 0  # range counter
    for port in ports[1:]:
        # interface name
        if range_start[0] != port[0]:
            if i > 0:  # it's a range
                outline += "-%d" % current_port[last_port_index]
                i = 0  # reset range counter
            if range_index >= 5:
                range_index = 1
                output.append(outline)
                outline = "%s%s" % (prefix, to_port(port))
            else:
                range_index += 1
                outline += ", %s" % to_port(port)
            range_start = port
            current_port = port
            continue  # move ahead for next port

        # interface numbers
        for port_index in range(1, 5):
            if current_port[port_index] == port[port_index]:
                pass
            # check if we found a subsequent interface number (we are at max supported depth)
            elif port[port_index] == (current_port[port_index] + 1) and port_index == 4:
                i += 1
                current_port = port
                last_port_index = port_index
                break
            # check if we found a subsequent interface number
            elif port[port_index] == (current_port[port_index] + 1) and \
                    port[port_index + 1] < 0 and current_port[port_index + 1] < 0:
                i += 1
                current_port = port
                last_port_index = port_index
                break
            else:
                if i > 0:  # set last port number
                    outline += "-%d" % current_port[last_port_index]
                    i = 0  # reset range counter
                if range_index >= max_ranges:  # max no of ranges reached, start a new range cmd
                    range_index = 1
                    output.append(outline)
                    outline = "%s%s" % (prefix, to_port(port))
                else:  # just append new range to current line
                    range_index += 1
                    outline += ", %s" % to_port(port)
                range_start = port
                current_port = port
                break  # move ahead for next port

    if i > 0:
        outline += "-%d" % current_port[last_port_index]
    output.append(outline)
    return output
