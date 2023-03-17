"""Functions for working with VLANs."""

import re
import typing as t
from itertools import groupby
from operator import itemgetter


def vlanlist_to_config(
    vlan_list: t.List[int],
    first_line_len: int = 48,
    other_line_len: int = 44,
    min_grouping_size: int = 3,
    return_empty: bool = False,
) -> t.List[str]:
    """Given a List of VLANs, build the IOS-like vlan list of configurations.

    Args:
        vlan_list: Unsorted list of vlan integers.
        first_line_len: The maximum length of the line of the first element of within the return list. Defaults to 48.
        other_line_len: The maximum length of the line of all other elements of within the return list. Defaults to 44.
        min_grouping_size: The minimum consecutive VLANs to aggregate with a hyphen. Defaults to Cisco's minimum grouping size of 3.
        return_empty: Whether or not to return an empty list instead of an `ValueError` when vlan_list is empty. Defaults to False.

    Returns:
        Sorted string list of integers according to IOS-like vlan list rules

    Examples:
        >>> from netutils.vlan import vlanlist_to_config
        >>> vlanlist_to_config([1, 2, 3, 5, 6, 1000, 1002, 1004, 1006, 1008, 1010, 1012, 1014, 1016, 1018])
        ['1-3,5,6,1000,1002,1004,1006,1008,1010,1012,1014', '1016,1018']
        >>> vlanlist_to_config([1,3,5,6,100,101,102,103,104,105,107,109], min_grouping_size=2)
        ['1,3,5-6,100-105,107,109']
        >>> vlanlist_to_config([1,3,5,6,100,101,102,103,104,105,107,109], min_grouping_size=1)
        ['1,3,5,6,100,101,102,103,104,105,107,109']
        >>> vlan_list = [1, 2, 3, 5, 6, 1000, 1002, 1004, 1006, 1008, 1010, 1012, 1014, 1016, 1018]
        >>> for index, vlan in enumerate(vlanlist_to_config(vlan_list)):
        ...     if index == 0:
        ...         print(f"switchport trunk allowed vlan {vlan}")
        ...     else:
        ...         print(f"switchport trunk allowed vlan add {vlan}")
        ...
        switchport trunk allowed vlan 1-3,5,6,1000,1002,1004,1006,1008,1010,1012,1014
        switchport trunk allowed vlan add 1016,1018
    """

    def build_final_vlan_cfg(vlan_cfg: str) -> t.List[str]:
        if len(vlan_cfg) <= first_line_len:
            return [vlan_cfg]

        # Split VLAN config if lines are too long
        first_line = re.match(f"^.{{0,{first_line_len}}}(?=,)", vlan_cfg)
        if not first_line:
            raise ValueError(
                f"Line with comma seperated vlans is expected.(E.g. 1-3,5,6,1000,1002) Received {vlan_cfg}"
            )
        vlan_cfg_lines = [first_line.group(0)]
        next_lines = re.compile(f"(?<=,).{{0,{other_line_len}}}(?=,|$)")
        for line in next_lines.findall(vlan_cfg, first_line.end()):
            vlan_cfg_lines.append(line)
        return vlan_cfg_lines

    if len(vlan_list) == 0 and return_empty:
        return []

    if len(vlan_list) == 0:
        raise ValueError("The `vlan_list` argument provided is empty, a list of vlans is required, e.g. [10,20,30].")

    # Fail if min_grouping_size is less than 1.
    if min_grouping_size < 1:
        raise ValueError("Minimum grouping size must be equal to or greater than one.")

    # Sort and de-dup VLAN list
    vlan_list = sorted(set(vlan_list))

    # If grouping size is zero, sort, and return the config list as no other processing is required.
    if min_grouping_size == 1:
        return build_final_vlan_cfg(",".join([str(vlan) for vlan in vlan_list]))

    # Group consecutive VLANs
    vlan_groups = []
    for _, vlan in groupby(enumerate(vlan_list), lambda vlan: vlan[0] - vlan[1]):
        vlan_groups.append(list(map(itemgetter(1), vlan)))

    # Check for invalid VLAN IDs
    if vlan_list[0] < 1 or vlan_list[-1] > 4094:
        raise ValueError("Valid VLAN range is 1-4094")

    # Create VLAN portion of config
    vlan_strings = []
    for group in vlan_groups:
        group_length = len(group)
        group_string = f"{group[0]}"
        # Compress based on grouping_size
        if group_length >= min_grouping_size:
            group_string += f"-{group[-1]}"
        # If it does not match grouping_size, and is greater than one
        elif group_length != 1:
            group_string += f",{group[1]}"
        vlan_strings.append(group_string)

    return build_final_vlan_cfg(",".join(vlan_strings))


def vlanconfig_to_list(vlan_config: str) -> t.List[int]:
    """Given an IOS-like vlan list of configurations, return the list of VLANs.

    Args:
        vlan_config: IOS-like vlan list of configurations.

    Returns:
        Sorted string list of integers according to IOS-like vlan list rules

    Examples:
        >>> vlan_config = '''switchport trunk allowed vlan 1025,1069-1072,1114,1173-1181,1501,1502'''
        >>> vlanconfig_to_list(vlan_config)
        [1025, 1069, 1070, 1071, 1072, 1114, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1501, 1502]
        >>>
    """
    # Check for invalid data within the vlan_config
    # example: switchport trunk allowed vlan 1025,1069-1072,BADDATA
    invalid_data = re.findall(r",?[^0-9\-],?$", vlan_config)
    # Regular VLANs that are not condensed and can be converted to integers
    vlans = list(map(int, re.findall(r"\d+", vlan_config)))

    # Fail if invalid data is found
    if invalid_data and vlans:
        raise ValueError(f"There were non-digits and dashes found in `{vlan_config}`.")
    if invalid_data:
        raise ValueError(f"No digits found in `{vlan_config}`")

    vlan_ranges = re.findall(r"\d+-\d+", vlan_config)
    for v_range in vlan_ranges:
        first, second = v_range.split("-")
        # Add one to first to prevent duplicates that already exist within vlans
        vlans.extend(list(range(*[int(first) + 1, int(second)])))

    vlans = sorted(vlans)
    if vlans[-1] > 4094:
        raise ValueError(f"Valid VLAN range is 1-4094, found {vlans[-1]}")
    return vlans
