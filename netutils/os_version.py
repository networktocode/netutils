"""Functions for working with OS Versions."""

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
