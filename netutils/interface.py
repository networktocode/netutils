"""Functions for working with interface."""

import itertools
import re
import typing as t
from abc import ABC, abstractmethod
from functools import total_ordering
from operator import itemgetter

from .constants import BASE_INTERFACES, REVERSE_MAPPING


def interface_range_expansion(interface_pattern: str) -> t.List[str]:
    """Expand interface pattern into a list of interfaces.

    Args:
        interface_pattern: The string pattern that will be parsed to create the list of interfaces.

    Returns:
        Contains the expanded list of interfaces.

    Examples:
        >>> from netutils.interface import interface_range_expansion
        >>> interface_range_expansion("Gi0/[1-4]")
        ['Gi0/1', 'Gi0/2', 'Gi0/3', 'Gi0/4']
        >>> interface_range_expansion("FastEthernet[1-2]/0/[10-15]")
        ['FastEthernet1/0/10', 'FastEthernet1/0/11', 'FastEthernet1/0/12', 'FastEthernet1/0/13', 'FastEthernet1/0/14', 'FastEthernet1/0/15', 'FastEthernet2/0/10', 'FastEthernet2/0/11', 'FastEthernet2/0/12', 'FastEthernet2/0/13', 'FastEthernet2/0/14', 'FastEthernet2/0/15']
    """

    def _range_expand(regex_match: str) -> t.List[int]:
        number_range: t.List[int] = []
        for value in regex_match.split(","):
            if "-" in value[1:]:
                first_number, second_number = value[1:].split("-", 1)
                number_range += range(int(value[0] + first_number), int(second_number) + 1)
            else:
                number_range.append(int(value))
        return number_range

    def _pairwise(interface_constant: t.List[int]) -> t.List[t.Tuple[int, int]]:
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

    # accommodate trailing constants
    if interface_constant[-1] < len(interface_pattern):
        interface_constant.append(len(interface_pattern))

    interface_constant_out = _pairwise(interface_constant)
    expanded_interfaces = []
    for element in itertools.product(*cartesian_list):
        current_interface = ""
        for count, item in enumerate(interface_constant_out):
            current_interface += interface_pattern[item[0] : item[1]]  # noqa: E203
            # only append the next item if the current constant
            # doesn't fall at the end of the line
            if count < len(element):
                current_interface += str(element[count])
        expanded_interfaces.append(current_interface)

    return expanded_interfaces


def split_interface(interface: str) -> t.Tuple[str, str]:
    """Split an interface name based on first digit, slash, or space match.

    Args:
        interface: The interface you are attempting to split.

    Returns:
        The split between the name of the interface the value.

    Examples:
        >>> from netutils.interface import split_interface
        >>> split_interface("GigabitEthernet1/0/1")
        ('GigabitEthernet', '1/0/1')
        >>> split_interface("Eth1")
        ('Eth', '1')
        >>>
    """
    head = interface.rstrip(r"/\0123456789.: ")
    tail = interface[len(head) :].lstrip()  # noqa: E203
    return (head, tail)


def canonical_interface_name(
    interface: str, addl_name_map: t.Optional[t.Dict[str, str]] = None, verify: bool = False
) -> str:
    """Function to return an interface's canonical name (fully expanded name).

    Use of explicit matches used to indicate a clear understanding on any potential
    match. Regex and other looser matching methods were not implemented to avoid false
    positive matches. As an example, it would make sense to do "[P|p][O|o]" which would
    incorrectly match PO = POS and Po = Port-channel, leading to a false positive, not
    easily troubleshot, found, or known.

    Args:
        interface: The interface you are attempting to expand.
        addl_name_map: A dict containing key/value pairs that updates the base mapping. Used if an OS has specific differences. e.g. {"Po": "PortChannel"} vs {"Po": "Port-Channel"}. Defaults to None.
        verify: Whether or not to verify the interface matches a known interface standard. Defaults to False.

    Returns:
        The name of the interface in the long form.

    Examples:
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
    if interface_type in name_map:
        long_int = name_map[interface_type]
        return long_int + str(interface_number)
    if verify:
        raise ValueError(f"Verify interface on and no match found for {interface}")
    # if nothing matched, return the original name
    return interface


def canonical_interface_name_list(
    interfaces: t.List[str],
    addl_name_map: t.Optional[t.Dict[str, str]] = None,
    verify: bool = False,
    order: t.Optional[str] = None,
    reverse: bool = False,
) -> t.List[str]:
    """Function to return a list of interface's canonical name (fully expanded name).

    Use of explicit matches used to indicate a clear understanding on any potential
    match. Regex and other looser matching methods were not implemented to avoid false
    positive matches. As an example, it would make sense to do `[P|p][O|o]` which would
    incorrectly match PO = POS and Po = Port-channel, leading to a false positive, not
    easily troubleshot, found, or known.

    Args:
        interfaces: List of interfaces you are attempting to expand.
        addl_name_map: A dict containing key/value pairs that updates the base mapping. Used if an OS has specific differences. e.g. {"Po": "PortChannel"} vs {"Po": "Port-Channel"}. Defaults to None.
        verify: Whether or not to verify the interface matches a known interface standard. Defaults to False.
        order: Determines what order the list of interfaces should be returned in. Defaults to None.
        reverse: Specify if the order of the list should be reversed when setting an order. Defaults to None.

    Returns:
        List of the interfaces in their long form.

    Raises:
        ValueError: Raised if any interface name in list cannot be converted to its long form and verify parameter is set to true.

    Examples:
        >>> from netutils.interface import canonical_interface_name_list
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

    if order:
        _check_order_option_exists(order)

    for interface in interfaces:
        canonical_interface_list.append(canonical_interface_name(interface, addl_name_map=addl_name_map))
        if interface == canonical_interface_name(interface):
            no_match_list.append(interface)

    if verify:
        no_match_string = ", ".join(no_match_list)
        raise ValueError(f"Verify interface on and no match found for {no_match_string}")

    if order:
        order_function = INTERFACE_LIST_ORDERING_OPTIONS.get(order, None)
        if not order_function:
            raise ValueError(f"No order function available called {order}")
        canonical_interface_list = order_function(canonical_interface_list)

    if reverse:
        canonical_interface_list = _reverse_list(canonical_interface_list)

    return canonical_interface_list


def abbreviated_interface_name(
    interface: str,
    addl_name_map: t.Optional[t.Dict[str, str]] = None,
    addl_reverse_map: t.Optional[t.Dict[str, str]] = None,
    verify: bool = False,
) -> str:
    """Function to return an abbreviated representation of the interface name.

    Args:
        interface: The interface you are attempting to shorten.
        addl_name_map: A dict containing key/value pairs that updates the base mapping. Used if an OS has specific differences. e.g. {"Po": "PortChannel"} vs {"Po": "Port-Channel"}. Defaults to None.
        addl_reverse_map: A dict containing key/value pairs that updates the abbreviated mapping. Defaults to None.
        verify: Whether or not to verify the interface matches a known interface standard. Defaults to False.

    Returns:
        The name of the interface in the abbreviated form.

    Examples:
        >>> from netutils.interface import abbreviated_interface_name
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
    canonical_type = name_map.get(interface_type, None)
    if not canonical_type:
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


@total_ordering
class CharacterClass(ABC):
    """CharacterClass embodies the state needed to sort interfaces."""

    def __init__(self, val: str, terminal: bool = False) -> None:  # noqa: D107
        self.val = val
        self._terminal = terminal
        super().__init__()

    @abstractmethod
    def __lt__(self, other: "CharacterClass") -> bool:  # noqa: D105
        ...

    def __eq__(self, other: t.Any) -> t.Any:  # noqa: D105
        return self.weight == other.weight and self.val == other.val

    @property
    @abstractmethod
    def weight(self) -> int:
        """Weight property."""

    @property
    def terminal(self) -> bool:
        """Flag whether a node is terminal."""
        return self._terminal

    @terminal.setter
    def terminal(self, val: bool) -> None:
        """This is a one-way switch to prevent overwriting a terminal node."""
        if not self._terminal:
            self._terminal = val

    def __str__(self) -> str:  # noqa: D105
        return str(self.val)

    def __hash__(self) -> int:  # noqa: D105
        return self.val.__hash__()


class CCString(CharacterClass):
    """Strings are sorted lexicographically."""

    def __lt__(self, other: "CharacterClass") -> bool:  # noqa: D105
        return self.weight < other.weight or self.val < other.val

    def __repr__(self) -> str:  # noqa: D105
        return f'CCString("{self.val}", {self.terminal})'

    @property
    def weight(self) -> int:  # noqa: D107,D102
        return 10


class CCInt(CharacterClass):
    """Ints must be sorted canonically because '11' < '5'."""

    def __lt__(self, other: "CharacterClass") -> bool:  # noqa: D105
        return self.weight < other.weight or int(self.val) < int(other.val)

    def __repr__(self) -> str:  # noqa: D105
        return f"CCInt({self.val}, {self.terminal})"

    @property
    def weight(self) -> int:  # noqa: D107,D102
        return 20


class CCSeparator(CharacterClass):
    """Separators require custom logic, so we sort them by arbitrary weight."""

    weights: t.Dict[str, int] = {".": 10, "/": 20}

    def __lt__(self, other: "CharacterClass") -> bool:  # noqa: D105
        return self.weight < other.weight or self.weights.get(self.val, 0) < self.weights.get(other.val, 0)

    def __repr__(self) -> str:  # noqa: D105
        return f'CCSeparator("{self.val}", {self.terminal})'

    @property
    def weight(self) -> int:  # noqa: D102
        return 30


def _CCfail(*args: t.Any) -> t.NoReturn:  # pylint: disable=C0103
    """Helper to raise an exception on a bad character match."""
    raise ValueError(f"unknown character '{args[0][0]}'.")


def _split_interface_tuple(interface: str) -> t.Tuple[CharacterClass, ...]:
    """Parser-combinator hack, keeping dependencies light."""
    idx = 0
    # we mutate tail's reference, so mypy needs help
    tail: t.Tuple[CharacterClass, ...] = ()
    regexes = [
        (r"[a-zA-Z\-]", CCString),
        (r"[0-9]", CCInt),
        (r"[./]", CCSeparator),
        # Fallthrough case, keep it at the end!
        (r".*", _CCfail),
    ]
    while idx < len(interface):
        for regex, cls in regexes:
            # Hint for Mypy to realize that both the classes and the function on the right side of the regexes tuples
            # are in fact callable.
            assert callable(cls)  # nosec
            part = ""
            while idx < len(interface) and re.match(regex, interface[idx]):
                part += interface[idx]
                idx += 1
            if part and idx == len(interface):
                tail = (*tail, cls(part, True))
                break
            if part:
                tail = (*tail, cls(part))
                break
    return tail


def _reverse_list(interface_list: t.List[str]) -> t.List[str]:
    """Reverses an alphabetical list of interfaces.

    Args:
        interface_list: Alphabetically sorted list of interfaces.
    """
    # Convert interface name into Tuple of : Text, Int and Separator
    split_intf = re.compile(r"([^\W0-9]+|[0-9]+|\W)")
    mytuple = [tuple(split_intf.findall(intf)) for intf in interface_list]

    # Sort the list of tuple
    mytuple.sort(key=itemgetter(0), reverse=True)

    return ["".join(x) for x in mytuple]


def _insert_nodes(node: t.Dict[CharacterClass, t.Any], values: t.Tuple[CharacterClass, ...]) -> None:
    """Recursively updates a tree from a list of values.

    This function mutates the node dict in place.  A terminal value needs to be
    preserved from overwrites, hence the one-way switch in CharacterClass.  These
    classes are compared only by weight and value, so dict updates are a little tricky.
    We need to pop the key and add a new pointer, or `terminal` will not be updated
    in the new entry.
    """
    if not values:
        return
    key = values[0]
    if key not in node:
        node[key] = {}
    if not values[1:]:  # This is the last node
        val = node[key]
        key.terminal = True
        node.pop(key)
        node[key] = val
    _insert_nodes(node[key], values[1:])


def _iter_tree(node: t.Dict[CharacterClass, t.Any], parents: t.List[CharacterClass]) -> t.Generator[str, None, None]:
    """Walk a tree of interface name parts.

    Weights are assigned based on domain logic to produce a
    'canonical' ordering of names.
    """
    for _, items in itertools.groupby(sorted(node.keys()), lambda t: t.weight):
        for item in sorted(items):
            if item.terminal:
                yield "".join(map(str, parents + [item]))
            parents.append(item)
            yield from _iter_tree(node[item], list(parents))
            parents.pop()


def sort_interface_list(interfaces: t.List[str]) -> t.List[str]:
    """This function sorts and cleans a list of interfaces.

    Note that a new list of interfaces is returned and that duplicates
    nodes are removed.

    Args:
        interfaces: A list of interfaces to be sorted.  The input list is not mutated by this function.

    Returns:
        A **new** sorted, unique list elements from the input.

    Examples:
        >>> from netutils.interface import sort_interface_list
        >>> sort_interface_list(["Gi1/0/1", "Gi1/0/3", "Gi1/0/3.100", "Gi1/0/2", "Gi1/0/2.50", "Gi2/0/2", "Po40", "Po160", "Lo10"])
        ['Gi1/0/1', 'Gi1/0/2', 'Gi1/0/2.50', 'Gi1/0/3', 'Gi1/0/3.100', 'Gi2/0/2', 'Lo10', 'Po40', 'Po160']
        >>> sort_interface_list(['GigabitEthernet1/0/1', 'GigabitEthernet1/0/3', 'GigabitEthernet1/0/2', "GigabitEthernet3/0/5", 'GigabitEthernet3/0/7', 'GigabitEthernet2/0/8.5',  'Port-channel40', 'Vlan20', 'Loopback10'])
        ['GigabitEthernet1/0/1', 'GigabitEthernet1/0/2', 'GigabitEthernet1/0/3', 'GigabitEthernet2/0/8.5', 'GigabitEthernet3/0/5', 'GigabitEthernet3/0/7', 'Loopback10', 'Port-channel40', 'Vlan20']
    """
    root: t.Dict[CharacterClass, t.Any] = {}
    for ifname in interfaces:
        _insert_nodes(root, _split_interface_tuple(ifname))
    return list(_iter_tree(root, []))


INTERFACE_LIST_ORDERING_OPTIONS = {"alphabetical": sort_interface_list}


def abbreviated_interface_name_list(  # pylint: disable=R0913, R0914
    interfaces: t.List[str],
    addl_name_map: t.Optional[t.Dict[str, str]] = None,
    addl_reverse_map: t.Optional[t.Dict[str, str]] = None,
    verify: bool = False,
    order: t.Optional[str] = None,
    reverse: bool = False,
) -> t.List[str]:
    """Function to return a list of interface's abbreviated name.

    Args:
        interfaces: List of interface names you are attempting to abbreviate.
        addl_name_map: A dict containing key/value pairs that updates the base mapping. Used if an OS has specific differences. e.g. {"Po": "PortChannel"} vs {"Po": "Port-Channel"}. Defaults to None.
        addl_reverse_map: A dict containing key/value pairs that updates the abbreviated mapping. Defaults to None.
        verify: Whether or not to verify the interface matches a known interface standard. Defaults to False.
        order: Determines what order the list of interfaces should be returned in. Defaults to None.
        reverse: Specify if the order of the list should be reversed when setting an order. Defaults to None.

    Returns:
        List of the interfaces in their abbreviated form.

    Raises:
        ValueError: Raised if any interface name in list cannot be converted to its abbreviated form and verify parameter is set to true.

    Examples:
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

    if order:
        _check_order_option_exists(order)

    if isinstance(addl_name_map, dict):
        name_map.update(addl_name_map)

    rev_name_map = {}
    rev_name_map.update(REVERSE_MAPPING)

    if isinstance(addl_reverse_map, dict):
        rev_name_map.update(addl_reverse_map)

    for interface in interfaces:
        interface_type, interface_number = split_interface(interface)
        # Try to ensure canonical type.
        canonical_type = name_map.get(interface_type, None)
        if not canonical_type:
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
        order_function = INTERFACE_LIST_ORDERING_OPTIONS.get(order, None)
        if not order_function:
            raise ValueError(f"No order function available called {order}")
        abbreviated_interface_list = order_function(abbreviated_interface_list)

    if reverse:
        abbreviated_interface_list = _reverse_list(abbreviated_interface_list)

    return abbreviated_interface_list


def _check_order_option_exists(order: str) -> None:
    """Check if the given order for an interface list exists.

    Args:
        order: Requested ordering of the interface list.

    Raises:
        ValueError: Raised the given order is not a proper ordering type.
    """
    if order not in INTERFACE_LIST_ORDERING_OPTIONS.keys():
        raise ValueError(f"{order} is not one of the supported orderings")


def _ranges_in_list(numbers: t.List[int]) -> t.List[t.List[int]]:
    """Find contiguous ranges in a list of numbers.

    Examples:
        >>> from netutils.interface import _ranges_in_list
        >>> _ranges_in_list([1, 2, 3, 5, 6, 8])
        [[1, 2, 3], [5, 6], [8]]

    Args:
        numbers: list of numbers

    Returns:
        list of ranges in input
    """
    return [list(map(itemgetter(1), g)) for k, g in itertools.groupby(enumerate(numbers), lambda x: x[0] - x[1])]


def interface_range_compress(interface_list: t.List[str]) -> t.List[str]:
    """Function which takes interfaces and return interface ranges.

    Whitespace and special characters are ignored in the input. Input must contain only interfaces,
    there is no check against correct interface names! Also interface names must use the same abbreviation!
    E.g. Gi =! GigabitEthernet

    Examples:
        >>> from netutils.interface import interface_range_compress
        >>> interface_range_compress(["Gi1/0/1", "Gi1/0/2", "Gi1/0/3", "Gi1/0/5"])
        ['Gi1/0/1-3', 'Gi1/0/5']
        >>> interface_range_compress(["Gi0/1", "Gi0/2", "Gi0/4", "Gi1/0", "Gi1/1"])
        ['Gi0/1-2', 'Gi0/4', 'Gi1/0-1']

    Args:
        interface_list: list of interfaces

    Returns:
        list of interface ranges
    """
    result_dict: t.Dict[str, t.List[int]] = {}
    final_result_list = []
    sorted_ints = [_split_interface_tuple(x) for x in sort_interface_list(interface_list)]
    if not sorted_ints:
        return []
    current_match = sorted_ints[0][0:-1]
    for interface in sorted_ints:
        if interface[0:-1] == current_match:
            module = "".join([x.val for x in current_match])
            if result_dict.get(module):
                result_dict[module] += [int(interface[-1].val)]
            else:
                result_dict[module] = [int(interface[-1].val)]
        else:
            current_match = interface[0:-1]
            result_dict["".join([x.val for x in current_match])] = [int(interface[-1].val)]
    for module, ports in result_dict.items():
        # find ranges in this port list
        ranges = _ranges_in_list(ports)
        # assemble module and port ranges
        for range_group in ranges:
            if len(range_group) > 1:
                final_result_list.append(f"{module}{range_group[0]}-{range_group[-1]}")
            else:
                final_result_list.append(f"{module}{range_group[0]}")
    return final_result_list
