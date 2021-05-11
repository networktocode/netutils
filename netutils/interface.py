"""Functions for working with interface."""

import itertools
from .variables import BASE_INTERFACES, REVERSE_MAPPING


def interface_tail_addition(interface_number):
    """Takes the tail end of the interface and sums it up to use for sorting a list of interfaces.

    Args:
        interface_number (str): Interface number I.E: 1/0/1, 1/0, 0/1

    Returns:
        int: Sum of number in interface tail with each one getting a priority of magnitude 10 from right to left.
    """
    priority_values = []
    factor_value = 1
    split_post_sub = []

    split_pre_sub = split_interface(interface_number)[1].split("/")
    for item in split_pre_sub:
        if "." in item:
            split_post_sub.append(item.split(".")[0])
        else:
            split_post_sub.append(item)

    values = [int(i) for i in split_post_sub]
    for i in reversed(values):
        i = i * factor_value
        factor_value = factor_value * 10
        priority_values.insert(0, i)
    return sum(priority_values)


def list_alphabetical(interfaces, reverse=False):
    """Takes list of interfaces and ensures they are in alphabetical order.

    Args:
        interfaces (list): List of interfaces
        reverse (bool): Determines if list alphabetical list should be reversed. Defaults to False.

    Returns:
        list: Interfaces listed in alphabetical order.
    """
    separate_interfaces_list = []
    contained_interfaces = set()

    for interface in interfaces:
        interface_name = split_interface(interface)[0]
        contained_interfaces.add(interface_name)

    for interface_name in contained_interfaces:
        new_list = [x for x in interfaces if split_interface(x)[0] == interface_name]
        if new_list:
            separate_interfaces_list.append(new_list)

    for separate_list in separate_interfaces_list:
        separate_list.sort(key=interface_tail_addition)

    if reverse:
        sorted_separate_list = reversed(sorted(separate_interfaces_list, key=lambda x: x[0]))
    else:
        sorted_separate_list = sorted(separate_interfaces_list, key=lambda x: x[0])

    return list(itertools.chain.from_iterable(sorted_separate_list))


INTERFACE_LIST_ORDERING_OPTIONS = {"alphabetical": list_alphabetical}


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


def canonical_interface_name_list(interfaces, addl_name_map=None, verify=False, order=None, reverse=None):
    """Function to return a list of interface's canonical name (fully expanded name).

    Use of explicit matches used to indicate a clear understanding on any potential
    match. Regex and other looser matching methods were not implmented to avoid false
    positive matches. As an example, it would make sense to do "[P|p][O|o]" which would
    incorrectly match PO = POS and Po = Port-channel, leading to a false positive, not
    easily troubleshot, found, or known.

    Args:
        interfaces (list): List of interfaces you are attempting to expand.
        addl_name_map (dict, optional): A dict containing key/value pairs that updates the base mapping. Used if an OS has specific differences. e.g. {"Po": "PortChannel"} vs {"Po": "Port-Channel"}. Defaults to None.
        verify (bool, optional): Whether or not to verify the interface matches a known interface standard. Defaults to False.
        order (str, optional): Determines what order the list of interfaces should be returned in. Defaults to None.
        reverse (bool, optional): Specify if the order of the list should be reversed when setting an order. Defaults to None.

    Returns:
        list: List of the interfaces in their long form.

    Raises:
        ValueError: Raised if any interface name in list cannot be converted to its long form and verify parameter is set to true.

    Example:
        >>> from net_utility.interface import canonical_interface_name_list
        >>> canonical_interface_name_list(["Gi1/0/1", "Gi1/0/2", "Eth1"])
        ['GigabitEthernet1/0/1', 'GigabitEthernet1/0/2', 'Ethernet1']
        >>> canonical_interface_name_list(["Gi1/0/1", "Po40", "Lo10"])
        ['GigabitEthernet1/0/1', 'Port-channel40', 'Loopback10']
        >>>
    """
    name_map = {}
    name_map.update(BASE_INTERFACES)
    canonical_interface_list = []
    no_match_list = []

    if reverse and not order:
        raise ValueError("Order must be set to use reverse.")

    if order and order not in INTERFACE_LIST_ORDERING_OPTIONS.keys():
        raise ValueError(f"{order} is not one of the supported orderings")

    if isinstance(addl_name_map, dict):
        name_map.update(addl_name_map)

    for interface in interfaces:
        interface_type, interface_number = split_interface(interface)
        if name_map.get(interface_type):
            long_int = name_map.get(interface_type)
            canonical_interface_list.append(long_int + str(interface_number))
        else:
            canonical_interface_list.append(interface)
            no_match_list.append(interface)

    if verify:
        no_match_string = ", ".join(no_match_list)
        raise ValueError(f"Verify interface on and no match found for {no_match_string}")

    if order:
        canonical_interface_list = INTERFACE_LIST_ORDERING_OPTIONS.get(order)(canonical_interface_list, reverse)
    return canonical_interface_list


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


def abbreviated_interface_name_list(  # pylint: disable=R0913, R0914
    interfaces, addl_name_map=None, addl_reverse_map=None, verify=False, order=None, reverse=None
):
    """Function to return a list of interface's abbreviated name.

    Args:
        interfaces (list): List of interface names you are attempting to abbreviate.
        addl_name_map (dict, optional): A dict containing key/value pairs that updates the base mapping. Used if an OS has specific differences. e.g. {"Po": "PortChannel"} vs {"Po": "Port-Channel"}. Defaults to None.
        addl_reverse_map (dict, optional): A dict containing key/value pairs that updates the abbreviated mapping. Defaults to None.
        verify (bool, optional): Whether or not to verify the interface matches a known interface standard. Defaults to False.
        order (str, optional): Determines what order the list of interfaces should be returned in. Defaults to None.
        reverse (bool, optional): Specify if the order of the list should be reversed when setting an order. Defaults to None.

    Returns:
        list: List of the interfaces in their abbreviated form.

    Raises:
        ValueError: Raised if any interface name in list cannot be converted to its abbreviated form and verify parameter is set to true.

    Example:
        >>> from netutils.interface import abbreviated_interface_name_list
        >>> abbreviated_interface_name_list(["GigabitEthernet1/0/1", "GigabitEthernet1/0/2", "Ethernet1"])
        ['Gi1/0/1', 'Gi1/0/2', 'Et1']
        >>> abbreviated_interface_name_list(['GigabitEthernet1/0/1', 'Port-channel40', 'Loopback10'])
        ['Gi1/0/1', 'Po40', 'Lo10']
        >>>
    """
    name_map = {}
    name_map.update(BASE_INTERFACES)
    abbreviated_interface_list = []
    no_match_list = []

    if reverse and not order:
        raise ValueError("Order must be set to use reverse.")

    if order and order not in INTERFACE_LIST_ORDERING_OPTIONS.keys():
        raise ValueError(f"{order} is not one of the supported orderings")

    if isinstance(addl_name_map, dict):
        name_map.update(addl_name_map)

    rev_name_map = {}
    rev_name_map.update(REVERSE_MAPPING)

    if isinstance(addl_reverse_map, dict):
        rev_name_map.update(addl_reverse_map)

    for interface in interfaces:
        interface_type, interface_number = split_interface(interface)
        # Try to ensure canonical type.
        if name_map.get(interface_type):
            canonical_type = name_map.get(interface_type)
        else:
            canonical_type = interface_type

        try:
            abbreviated_name = rev_name_map[canonical_type] + str(interface_number)
            abbreviated_interface_list.append(abbreviated_name)
        except KeyError:
            abbreviated_interface_list.append(interface)
            no_match_list.append(interface)

    if verify:
        no_match_string = ", ".join(no_match_list)
        raise ValueError(f"Verify interface on and no match found for {no_match_string}")

    if order:
        abbreviated_interface_list = INTERFACE_LIST_ORDERING_OPTIONS.get(order)(abbreviated_interface_list, reverse)
    return abbreviated_interface_list
