"""Configuration command lookup."""

from netutils.lib_mapper import RUNNING_CONFIG_MAPPER


def get_running_config_command(platform: str) -> str:
    """
    Get the running config command for a specific network platform.

    Args:
        platform: Platform name, like 'cisco_ios' or 'juniper_junos'.

    Returns:
        The corresponding command as a string, or 'show run' by default.
    """
    return RUNNING_CONFIG_MAPPER.get(platform.lower(), "show run")
