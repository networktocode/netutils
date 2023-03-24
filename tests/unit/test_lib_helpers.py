"""Test for the lib_helpers definitions."""
from unittest import mock

import pytest
from netutils.lib_helpers import get_napalm_getters, get_panos_upgrade_path


@mock.patch("netutils.lib_helpers.HAS_NAPALM", False)
def test_get_napalm_getters_napalm_not_installed():
    with pytest.raises(ImportError) as exc:
        get_napalm_getters()
    assert "Napalm must be install for this function to operate." == str(exc.value)


def test_get_panos_upgrade_path():
    assert get_panos_upgrade_path("9.1.6", "10.1.9") == ["9.1.15-h1", "10.0.0", "10.0.12", "10.1.0", "10.1.9"]
    assert get_panos_upgrade_path("9.1.6", "10.1.9", fast_upgrade=True) == ["10.0.0", "10.1.0", "10.1.9"]


def test_get_panos_upgrade_path_current_greater_than_target():
    with pytest.raises(ValueError, match="Target version must be newer than current version."):
        get_panos_upgrade_path("10.1.9", "9.1.6")


def test_get_panos_upgrade_path_current_equals_target():
    with pytest.raises(ValueError, match="Target version equals current version. No upgrade necessary."):
        get_panos_upgrade_path("10.1.9", "10.1.9")


def test_get_panos_upgrade_path_fast_upgrade_and_custom_upgrade_path():
    with pytest.raises(ValueError, match="Cannot use fast_upgrade and custom_upgrade_path together."):
        get_panos_upgrade_path(
            "9.1.6", "10.1.9", fast_upgrade=True, custom_upgrade_path=["9.1.10", "9.1.15-h1", "10.0.0", "10.1.9"]
        )


def test_get_panos_upgrade_path_custom_upgrade_path():
    assert get_panos_upgrade_path(
        "9.1.6", "10.1.9", custom_upgrade_path=["9.1.10", "9.1.15-h1", "10.0.0", "10.1.9"]
    ) == ["9.1.10", "9.1.15-h1", "10.0.0", "10.1.9"]
