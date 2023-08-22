"""Functions for working with OS Versions."""

import re
import typing as t

from netutils._private.version import LooseVersion, StrictVersion  # type: ignore


def get_upgrade_path(current_version: str, target_version: str, firmware_list: t.List[str]) -> t.List[str]:
    """Utility to return the upgrade path from the current to target firmware version.

    Returns:
        List of firmware versions to upgrade from current to target.

    Args:
        current_version: Current firmware version.
        target_version: Target firmware version.
        firmware_list: List of firmware versions to use as the upgrade path.

    Raises:
        ValueError: If target version is older than current version.
        ValueError: If target version equals current version.

    Examples:
        >>> from netutils.os_version import get_upgrade_path
        >>> get_upgrade_path("9.1.6", "10.1.9", ["9.1.10", "9.1.15-h1", "10.0.0", "10.1.9"])
        ['9.1.10', '9.1.15-h1', '10.0.0', '10.1.9']
        >>> from netutils.constants import UPGRADE_PATHS
        >>> get_upgrade_path("9.1.6", "10.1.9", UPGRADE_PATHS["PANOS_OFFICIAL_V1"])
        ['9.1.15-h1', '10.0.0', '10.0.12', '10.1.0', '10.1.9']
    """
    if LooseVersion(current_version) > LooseVersion(target_version):
        raise ValueError("Target version must be newer than current version.")

    if LooseVersion(current_version) == LooseVersion(target_version):
        raise ValueError("Target version equals current version. No upgrade necessary.")

    upgrade_path = [
        version
        for version in firmware_list
        if LooseVersion(version) > LooseVersion(current_version)
        and LooseVersion(version) <= LooseVersion(target_version)
    ]

    if target_version not in upgrade_path:
        upgrade_path.append(target_version)

    return upgrade_path


def _compare_version(current_version: str, comparison: str, target_version: str, version_type: str) -> bool:
    # Convert version strings to Version objects for comparison
    if version_type == "loose":
        current_ver_obj = LooseVersion(current_version)
        target_ver_obj = LooseVersion(target_version)
    elif version_type == "strict":
        current_ver_obj = StrictVersion(current_version)
        target_ver_obj = StrictVersion(target_version)

    # Perform the comparison based on the comparison operation
    if comparison == "<":
        return bool(current_ver_obj < target_ver_obj)
    if comparison == "<=":
        return bool(current_ver_obj <= target_ver_obj)
    if comparison == "==":
        return bool(current_ver_obj == target_ver_obj)
    if comparison == "!=":
        return bool(current_ver_obj != target_ver_obj)
    if comparison == ">":
        return bool(current_ver_obj > target_ver_obj)
    if comparison == ">=":
        return bool(current_ver_obj >= target_ver_obj)
    raise ValueError(f"Invalid comparison operator: {comparison}")


def compare_version_loose(current_version: str, comparison: str, target_version: str) -> bool:
    """
    Compares two version strings using the specified comparison operation, based on LooseVersion.

    Args:
        current_version (str): The current version string to compare.
        comparison (str): The comparison operation as a string (<, <=, ==, !=, >, >=).
        target_version (str): The target version string to compare against.

    Returns:
        bool: The result of the comparison.

    Raises:
        ValueError: If there is an invalid comparison.
        TypeError: If not a valid version.

    Example:
        >>> from netutils.os_version import compare_version_loose
        >>> compare_version_loose("3.3.3a", "==", "3.3.3a")
        True
        >>> compare_version_loose("3.3.2", "<=", "3.3.3")
        True
        >>> compare_version_loose("3.3.2", ">=", "3.3.3")
        False
        >>>
    """
    return _compare_version(current_version, comparison, target_version, "loose")


def compare_version_strict(current_version: str, comparison: str, target_version: str) -> bool:
    """
    Compares two version strings using the specified comparison operation, based on LooseVersion.

    Args:
        current_version (str): The current version string to compare.
        comparison (str): The comparison operation as a string (<, <=, ==, !=, >, >=).
        target_version (str): The target version string to compare against.

    Returns:
        bool: The result of the comparison.

    Raises:
        ValueError: If there is an invalid comparison.
        ValueError: If not a valid version.

    Example:
        >>> from netutils.os_version import compare_version_strict
        >>> compare_version_strict("3.3.3", "==", "3.3.3")
        True
        >>> compare_version_strict("3.3.2", "<=", "3.3.3")
        True
        >>> compare_version_strict("3.3.2", ">=", "3.3.3")
        False
        >>>
    """
    return _compare_version(current_version, comparison, target_version, "strict")


def juniper_junos_version_parser(version: str) -> t.Dict[str, t.Any]:
    """Parses JunOS Version into usable bits matching JunOS Standards.

    Args:
        version

    Returns:
        A dictionary containing parsed version information

    Examples:
        >>> parsed_version = juniper_junos_version_parser("12.3R4")
    """
    # Use regex to group the main, minor, type and build into useable pieces
    # re_main_minor_type_build = re.search(r"^(\d+)\.(\d+)([xXrRsS])?(\d+)?", split_version[0])
    re_main_minor_type_build: re.Pattern[str] = re.compile(
        r"""
        ^
        (?P<main>\d+)           # main train
        \.                      # dot separator
        (?P<minor>\d+)          # minor version
        (?P<type>[xXrRsS])?     # version type (optional)
        (?P<build>\d+)?         # build (optional)
        """,
        re.VERBOSE,
    )
    re_service_build_respin: re.Pattern[str] = re.compile(
        r"""
        (?P<service>[sSdD])?        # service (optional)
        (?P<service_build>\d+)?     # service build (optional)
        \.?
        (?P<service_respin>\d+)?    # service respin (optional)
        """,
        re.VERBOSE,
    )
    # Set empty params for service pieces and complete them if a second indice exists from the version split
    # Define isservice, isfrs, isspecial, ismaintenance
    parsed_version: t.Dict[str, t.Any] = {
        "isservice": False,
        "ismaintenance": False,
        "isfrs": False,
        "isspecial": False,
        "service": None,
        "service_build": None,
        "service_respin": None,
    }

    # Juniper junos marks the division between main, minor, type and build from the service build and respin with a -
    version_core_part, *version_service_part = re.split("-|:", version)

    # Parse out junos into sections that can be used for logic
    parsed_version.update(re_main_minor_type_build.search(version_core_part).groupdict())  # type:ignore

    if version_service_part:
        parsed_version.update(re_service_build_respin.search(version_service_part[0]).groupdict())  # type:ignore
        if parsed_version.get("service", "").lower() == "s":
            parsed_version["isservice"] = True
        # Juniper looks at the D in special releases like it's the R in normal releases; Use it as the frs identifier
        elif parsed_version.get("service").lower() == "d" and (  # type:ignore
            parsed_version.get("service_build") is None or int(parsed_version.get("service_build", 1)) <= 1
        ):
            parsed_version["isfrs"] = True

    if parsed_version.get("type") is None:
        return parsed_version

    if parsed_version["type"].lower() == "x":
        parsed_version["isspecial"] = True
    elif parsed_version["type"].lower() == "s":
        parsed_version["isservice"] = True

    if parsed_version["type"].lower() == "r" and (
        parsed_version.get("build") is None or int(parsed_version.get("build")) <= 1  # type:ignore
    ):
        parsed_version["isfrs"] = True
    elif parsed_version["type"].lower() == "r":
        parsed_version["ismaintenance"] = True

    return parsed_version


os_version_parsers = {
    "juniper": {
        "junos": juniper_junos_version_parser,
    }
}
