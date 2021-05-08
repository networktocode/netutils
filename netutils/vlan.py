"""Functions for working with VLANs."""

import re

from operator import itemgetter
from itertools import groupby






















































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
