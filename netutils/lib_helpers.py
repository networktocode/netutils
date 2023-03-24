"""Helpers to expose network automation library functionality support."""

import inspect
import typing as t
from distutils.version import LooseVersion

from netutils.lib_mapper import NAPALM_LIB_MAPPER

try:
    from napalm import get_network_driver
    from napalm.base.exceptions import ModuleImportError
except ImportError:
    HAS_NAPALM = False
else:
    HAS_NAPALM = True


def get_napalm_getters() -> t.Dict[str, t.Dict[str, bool]]:
    """Utility to return a dictionary of napalm getters based on install napalm version.

    Returns:
        Keys are OS and values are a dictionary of supported napalm getters.

    Raises:
        ImportError: If optional dependency Napalm is not installed.

    Examples:
        >>> from netutils.lib_helpers import get_napalm_getters
        >>> napalm_getters = get_napalm_getters()  # doctest: +SKIP
        >>> napalm_getters["eos"]["get_arp_table"]  # doctest: +SKIP
        >>> True  # doctest: +SKIP
        >>> napalm_getters["eos"]["get_ipv6_neighbors_table"]  # doctest: +SKIP
        >>> False  # doctest: +SKIP
    """
    if not HAS_NAPALM:
        raise ImportError("Napalm must be install for this function to operate.")

    napalm_dict: t.Dict[str, t.Dict[str, bool]] = {}
    oses = NAPALM_LIB_MAPPER.keys()
    for my_os in oses:
        try:
            get_network_driver(my_os)
        except ModuleImportError:
            continue
        napalm_dict[my_os] = {}
        for getter in inspect.getmembers(get_network_driver(my_os), predicate=inspect.isfunction):
            if getter[0].startswith("get_"):
                # If the module is only in the base class it has not been implemented by the child class.
                state = bool(getter[1].__module__ == "napalm.base.base")
                napalm_dict[my_os][getter[0]] = state
    return napalm_dict


def get_panos_upgrade_path(
    current_version: str,
    target_version: str,
    fast_upgrade: bool = False,
    custom_upgrade_path: t.Union[t.List[str], None] = None,
) -> t.List[str]:
    """Utility to return the upgrade path from the current to target PANOS version.

    Returns:
        List of PANOS versions to upgrade from current to target.

    Args:
        current_version: Current PANOS version.
        target_version: Target PANOS version.
        fast_upgrade: If True only major versions will be returned.
        custom_upgrade_path: List of PANOS versions to use as the upgrade path.

    Raises:
        ValueError: If target version is older than current version.
        ValueError: If target version equals current version.
        ValueError: If fast_upgrade and custom_upgrade_path are both True.

    Examples:
        >>> from netutils.lib_helpers import get_panos_upgrade_path
        >>> get_panos_upgrade_path("9.1.6", "10.1.9")
        ['9.1.15-h1', '10.0.0', '10.0.12', '10.1.0', '10.1.9']
        >>> get_panos_upgrade_path("9.1.6", "10.1.9", fast_upgrade=True)
        ['10.0.0', '10.1.0', '10.1.9']
        >>> get_panos_upgrade_path("9.1.6", "10.1.9", custom_upgrade_path=["9.1.10", "9.1.15-h1", "10.0.0", "10.1.9"])
        ['9.1.10', '9.1.15-h1', '10.0.0', '10.1.9']
    """
    all_palo_versions = [
        "8.0.0",
        "8.0.20",
        "8.1.0",
        "8.1.24-h1",
        "9.0.0",
        "9.0.16-h3",
        "9.1.0",
        "9.1.15-h1",
        "10.0.0",
        "10.0.12",
        "10.1.0",
        "10.1.9",
    ]

    major_palo_versions = [
        "8.0.0",
        "8.1.0",
        "9.0.0",
        "9.1.0",
        "10.0.0",
        "10.1.0",
    ]

    if fast_upgrade and custom_upgrade_path:
        raise ValueError("Cannot use fast_upgrade and custom_upgrade_path together.")
    if fast_upgrade:
        palo_versions = major_palo_versions
    elif custom_upgrade_path:
        palo_versions = custom_upgrade_path
    else:
        palo_versions = all_palo_versions

    if LooseVersion(current_version) > LooseVersion(target_version):
        raise ValueError("Target version must be newer than current version.")

    if LooseVersion(current_version) == LooseVersion(target_version):
        raise ValueError("Target version equals current version. No upgrade necessary.")

    upgrade_path = [
        version
        for version in palo_versions
        if LooseVersion(version) > LooseVersion(current_version)
        and LooseVersion(version) <= LooseVersion(target_version)
    ]

    if target_version not in upgrade_path:
        upgrade_path.append(target_version)

    return upgrade_path
