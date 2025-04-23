"""Tests for the running configuration command mapping."""

import pytest
from netutils import lib_mapper
from netutils.running_config import get_running_config_command


def test_running_config_mapper_keys_are_known():
    """Ensure all keys in RUNNING_CONFIG_MAPPER are in MAIN_LIB_MAPPER values."""
    unknown_keys = [
        key for key in lib_mapper.RUNNING_CONFIG_MAPPER
        if key not in lib_mapper.MAIN_LIB_MAPPER.values()
    ]
    assert not unknown_keys, f"Unexpected keys in RUNNING_CONFIG_MAPPER: {unknown_keys}"


@pytest.mark.parametrize("platform,expected_command", list(lib_mapper.RUNNING_CONFIG_MAPPER.items()))
def test_get_running_config_command_known_platforms(platform, expected_command):
    """Test get_running_config_command returns correct command for known platforms."""
    assert get_running_config_command(platform) == expected_command
    assert get_running_config_command(platform.upper()) == expected_command  # test case insensitivity


def test_get_running_config_command_unknown_platform():
    """Test get_running_config_command returns 'UNKNOWN' for unsupported platform."""
    assert get_running_config_command("totally_unknown_platform") == "UNKNOWN"
    assert get_running_config_command("ArIsTa_EoZ") == "UNKNOWN"
