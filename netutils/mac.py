"""Functions for working with MAC addresses."""

import re
import typing as t
from functools import wraps

from .constants import MAC_CREATE, MAC_REGEX


def _valid_mac(func: t.Callable[..., t.Any]) -> t.Callable[..., t.Any]:
    """Decorator to validate a MAC address is valid."""

    @wraps(func)
    def decorated(*args: t.Any, **kwargs: t.Any) -> t.Any:
        if kwargs.get("mac"):
            mac = kwargs.get("mac")
        else:
            mac = args[0]
        assert isinstance(mac, str)  # nosec
        if not is_valid_mac(mac):
            raise ValueError(f"There was not a valid mac address in: `{mac}`")
        return func(*args, **kwargs)

    return decorated


def is_valid_mac(mac: str) -> bool:
    """Verifies whether or not a string is a valid MAC address.

    Args:
        mac: A MAC address in string format that matches one of the defined regex patterns.

    Returns:
        The result as to whether or not the string is a valid MAC address.

    Example:
        >>> from netutils.mac import is_valid_mac
        >>> is_valid_mac("aa.bb.cc.dd.ee.ff")
        True
        >>> is_valid_mac("aa.bb.cc.dd.ee.gg")
        False
        >>>
    """
    for pattern in list(MAC_REGEX.values()):
        if re.fullmatch(pattern, mac):
            return True
    return False


@_valid_mac
def mac_to_format(mac: str, frmt: str = "MAC_NO_SPECIAL") -> str:
    """Converts the MAC address to a specific format.

    Args:
        mac: A MAC address in string format that matches one of the defined regex patterns.
        frmt: A format in which the MAC address should be returned in.

    Returns:
        A MAC address in the specified format.

    Example:
        >>> from netutils.mac import mac_to_format
        >>> mac_to_format("aa.bb.cc.dd.ee.ff", "MAC_DASH_FOUR")
        'aabb-ccdd-eeff'
        >>>
    """
    if not MAC_CREATE.get(frmt):
        raise ValueError(f"An invalid mac format was provided in: `{frmt}`")
    mac = mac_normalize(mac)
    count = MAC_CREATE[frmt]["count"]
    char = MAC_CREATE[frmt]["char"]
    return char.join([mac[i : i + count] for i in range(0, len(mac), count)])  # type: ignore # noqa: E203


@_valid_mac
def mac_to_int(mac: str) -> int:
    """Converts the MAC address to an integer.

    Args:
        mac: A MAC address in string format that matches one of the defined regex patterns.

    Returns:
        The valid MAC address converted to an integer.

    Example:
        >>> from netutils.mac import mac_to_int
        >>> mac_to_int("aa.bb.cc.dd.ee.ff")
        187723572702975
        >>>
    """
    return int(mac_normalize(mac), 16)


@_valid_mac
def mac_type(mac: str) -> t.Optional[str]:
    """Retuns the "type" of MAC address, as defined by the regex pattern names.

    Args:
        mac: A MAC address in string format that matches one of the defined regex patterns.

    Returns:
        The regex pattern type of the MAC address.

    Example:
        >>> from netutils.mac import mac_type
        >>> mac_type("aa.bb.cc.dd.ee.ff")
        'MAC_DOT_TWO'
        >>> mac_type("aabb.ccdd.eeff")
        'MAC_DOT_FOUR'
        >>>
    """
    for name, pattern in MAC_REGEX.items():
        if re.fullmatch(pattern, mac):
            return name
    return None


@_valid_mac
def mac_normalize(mac: str) -> str:
    """Retuns the MAC address with only the address, and no special characters.

    Args:
        mac: A MAC address in string format that matches one of the defined regex patterns.

    Returns:
        The MAC address with no special characters.

    Example:
        >>> from netutils.mac import mac_normalize
        >>> mac_normalize("aa.bb.cc.dd.ee.ff")
        'aabbccddeeff'
        >>>
    """
    chars = ":-."
    for char in chars:
        if char in mac:
            mac = mac.replace(char, "")
    return mac
