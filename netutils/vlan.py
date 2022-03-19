"""Functions for working with VLANs."""

import re

from operator import itemgetter
from itertools import groupby


def vlanlist_to_config(vlan_list, first_line_len=48, other_line_len=44, min_grouping_size=3):
    """Given a List of VLANs, build the IOS-like vlan list of configurations.

    Args:
        vlan_list (list): Unsorted list of vlan integers.
        first_line_len (int, optional): The maximum length of the line of the first element of within the return list. Defaults to 48.
        other_line_len (int, optional): The maximum length of the line of all other elements of within the return list. Defaults to 44.
        min_grouping_size (int, optional): The minimum grouping size. Defaults to Cisco's minimum grouping size of 3.

    Returns:
        list: Sorted string list of integers according to IOS-like vlan list rules

    Example:
        >>> from netutils.vlan import vlanlist_to_config
        >>> vlanlist_to_config([1, 2, 3, 5, 6, 1000, 1002, 1004, 1006, 1008, 1010, 1012, 1014, 1016, 1018])
        ['1-3,5,6,1000,1002,1004,1006,1008,1010,1012,1014', '1016,1018']
        >>> vlanlist_to_config([1,3,5,6,100,101,102,103,104,105,107,109], min_grouping_size=2)
        ['1,3,5-6,100-105,107,109']
        >>> vlanlist_to_config([1,3,5,6,100,101,102,103,104,105,107,109], min_grouping_size=1)
        ['1,3,5,6,100,101,102,103,104,105,107,109']
    """

    def build_final_vlan_cfg(vlan_cfg):
        if len(vlan_cfg) <= first_line_len:
            return [vlan_cfg]

        # Split VLAN config if lines are too long
        first_line = re.match(f"^.{{0,{first_line_len}}}(?=,)", vlan_cfg)
        vlan_cfg_lines = [first_line.group(0)]
        next_lines = next_lines = re.compile(f"(?<=,).{{0,{other_line_len}}}(?=,|$)")
        for line in next_lines.findall(vlan_cfg, first_line.end()):
            vlan_cfg_lines.append(line)
        return vlan_cfg_lines

    # Fail if min_grouping_size is less than 1.
    if min_grouping_size < 1:
        raise ValueError("Minimum grouping size must be equal to or greater than one.")

    # Sort and de-dup VLAN list
    vlan_list = sorted(set(vlan_list))

    # If grouping size is zero, sort, and return the config list as no other processing is required.
    if min_grouping_size == 1:
        return build_final_vlan_cfg(",".join([str(x) for x in vlan_list]))

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


def vlanconfig_to_list(vlan_config):
    """Given an IOS-like vlan list of configurations, return the list of VLANs.

    Args:
        vlan_config (list): IOS-like vlan list of configurations.

    Returns:
        dict: Sorted string list of integers according to IOS-like vlan list rules

    Example:
        >>> vlan_config = '''switchport trunk allowed vlan 1025,1069-1072,1114,1173-1181,1501,1502'''
        >>> vlanconfig_to_list(vlan_config)
        [1025, 1069, 1070, 1071, 1072, 1114, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1501, 1502]
        >>>
    """
    vlans = []
    for line in vlan_config.splitlines():
        match = re.search(r"\d", line)
        if not match:
            raise ValueError(f"No digits found in line `{line}`")
        for parsed in line[match.start() :].split(","):  # noqa: E203
            if any(char not in "0123456789-" for char in parsed):
                raise ValueError(f"There were non-digits and dashes found in `{parsed}`")
            if re.search("-", parsed):
                vlans.extend(list(range(*[int(i) for i in parsed.split("-")])))
                vlans.append(int(parsed.split("-")[1]))
            else:
                vlans.append(int(parsed))
    vlans = sorted(vlans)
    if vlans[-1] > 4094:
        raise ValueError(f"Valid VLAN range is 1-4094, found {vlans[-1]}")
    return vlans
