"""Functions for working with time."""

import re
import typing as t

from .constants import TIME_MAPPINGS, UPTIME_REGEX_PATTERNS


def uptime_seconds_to_string(uptime_seconds: int) -> str:
    """Converts uptime in seconds to uptime in string format.

    Args:
        uptime_seconds: Uptime in seconds.

    Returns:
        Uptime in string format.

    Examples:
        >>> from netutils.time import uptime_seconds_to_string
        >>> uptime_seconds_to_string(7250)
        '2 hours, 50 seconds'
    """
    result = []
    for interval, count in TIME_MAPPINGS:
        value = uptime_seconds // count
        if value:
            uptime_seconds -= value * count
            if value == 1:
                interval = interval.rstrip("s")
            result.append(f"{value} {interval}")

    return ", ".join(result)


def uptime_string_to_seconds(uptime_string: str) -> int:
    """Converts uptime string seconds.

    Args:
        uptime_string: Uptime in string format

    Returns:
        Uptime string converted to seconds.

    Examples:
        >>> from netutils.time import uptime_string_to_seconds
        >>> uptime_string_to_seconds("58 minutes")
        3480
        >>> from netutils.time import uptime_string_to_seconds
        >>> uptime_string_to_seconds("4m15s")
        255

    Raises:
        ValueError: When uptime_string is unable to be parsed by regex.
    """
    compiled_regex_list = [re.compile(reg_pattern) for reg_pattern in UPTIME_REGEX_PATTERNS]

    uptime_dict: t.Dict[str, str] = {}
    for regex in compiled_regex_list:
        match = regex.search(uptime_string)

        if match:
            uptime_dict = match.groupdict()
            break

    if not match:
        raise ValueError("Unable to parse uptime string.")

    uptime_seconds = 0
    for time_interval, value in TIME_MAPPINGS:
        time_interval_as_int = uptime_dict.get(time_interval)
        if time_interval_as_int:
            uptime_seconds += int(time_interval_as_int) * value
    return uptime_seconds
