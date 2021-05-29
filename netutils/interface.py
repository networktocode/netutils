"""Functions for working with interface."""

from .constants import BASE_INTERFACES, REVERSE_MAPPING


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
