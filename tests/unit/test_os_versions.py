"""Test for the lib_helpers definitions."""
import pytest
from netutils.os_version import get_upgrade_path
from netutils.constants import UPGRADE_PATHS


def test_get_upgrade_path():
    return_values = ["9.1.15-h1", "10.0.0", "10.0.12", "10.1.0", "10.1.9"]
    assert get_upgrade_path("9.1.6", "10.1.9", UPGRADE_PATHS["PANOS_OFFICIAL_V1"]) == return_values
    assert get_upgrade_path("9.1.6", "10.1.9", UPGRADE_PATHS["PANOS_MAJOR_ONLY_V1"]) == [
        "10.0.0",
        "10.1.0",
        "10.1.9",
    ]


def test_get_upgrade_path_current_greater_than_target():
    with pytest.raises(ValueError, match="Target version must be newer than current version."):
        get_upgrade_path("10.1.9", "9.1.6", UPGRADE_PATHS["PANOS_MAJOR_ONLY_V1"])


def test_get_upgrade_path_current_equals_target():
    with pytest.raises(ValueError, match="Target version equals current version. No upgrade necessary."):
        get_upgrade_path("10.1.9", "10.1.9", UPGRADE_PATHS["PANOS_MAJOR_ONLY_V1"])
