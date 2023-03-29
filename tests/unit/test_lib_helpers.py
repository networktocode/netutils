"""Test for the lib_helpers definitions."""
from unittest import mock

import pytest
from netutils.lib_helpers import (
    get_napalm_getters,
    get_upgrade_path,
    PANOS_FIRMWARE_LIST_OFFICIAL,
    PANOS_FIRMWARE_LIST_MAJOR_ONLY,
)


@mock.patch("netutils.lib_helpers.HAS_NAPALM", False)
def test_get_napalm_getters_napalm_not_installed():
    with pytest.raises(ImportError) as exc:
        get_napalm_getters()
    assert "Napalm must be install for this function to operate." == str(exc.value)


def test_get_upgrade_path():
    assert get_upgrade_path("9.1.6", "10.1.9", PANOS_FIRMWARE_LIST_OFFICIAL) == [  # pylint: disable=duplicate-code
        "9.1.15-h1",  # pylint: disable=duplicate-code
        "10.0.0",  # pylint: disable=duplicate-code
        "10.0.12",  # pylint: disable=duplicate-code
        "10.1.0",  # pylint: disable=duplicate-code
        "10.1.9",  # pylint: disable=duplicate-code
    ]  # pylint: disable=duplicate-code
    assert get_upgrade_path("9.1.6", "10.1.9", PANOS_FIRMWARE_LIST_MAJOR_ONLY) == ["10.0.0", "10.1.0", "10.1.9"]


def test_get_upgrade_path_current_greater_than_target():
    with pytest.raises(ValueError, match="Target version must be newer than current version."):
        get_upgrade_path("10.1.9", "9.1.6", PANOS_FIRMWARE_LIST_MAJOR_ONLY)


def test_get_upgrade_path_current_equals_target():
    with pytest.raises(ValueError, match="Target version equals current version. No upgrade necessary."):
        get_upgrade_path("10.1.9", "10.1.9", PANOS_FIRMWARE_LIST_MAJOR_ONLY)
