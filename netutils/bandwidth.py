"""Functions for performing bandwidth calculations."""
import re


def kbps_to_mbps(speed: float) -> float:
    """Method to convert `speed` from Kbps to Mbps value.

    Args:
        init_speed (float): Speed in Kbps to convert to Mbps.

    Returns:
        float: Speed in Mbps converted from Kbps.
    """
    return speed / 1000


def kbps_to_gbps(speed: float) -> float:
    """Method to convert `speed` from Kbps to Gbps value.

    Args:
        init_speed (float): Speed in Kbps to convert to Gbps.

    Returns:
        float: Speed in Gbps converted from Kbps.
    """
    return speed / 1000000


def kbps_to_tbps(speed: float) -> float:
    """Method to convert `speed` from Kbps to Tbps value.

    Args:
        init_speed (float): Speed in Kbps to convert to Tbps.

    Returns:
        float: Speed in Tbps converted from Kbps.
    """
    return speed / 1000000000


def mbps_to_gbps(speed: float) -> float:
    """Method to convert `speed` from Mbps to Gbps value.

    Args:
        init_speed (float): Speed in Mbps to convert to Gbps.

    Returns:
        float: Speed in Mbps converted from Kbps.
    """
    return speed / 1000


def mbps_to_tbps(speed: float) -> float:
    """Method to convert `speed` from Mbps to Tbps value.

    Args:
        init_speed (float): Speed in Mbps to convert to Tbps.

    Returns:
        float: Speed in Tbps converted from Kbps.
    """
    return speed / 1000000


def mbps_to_kbps(speed: float) -> float:
    """Method to convert `speed` from Mbps to Kbps value.

    Args:
        speed (float): Speed in Mbps to convert to Kbps.

    Returns:
        float: Speed in Kbps converted from Mbps.
    """
    return speed * 1000


def gbps_to_kbps(speed: float) -> float:
    """Method to convert `speed` from Gbps to Kbps value.

    Args:
        speed (float): Speed in Gbps to convert to Kbps.

    Returns:
        float: Speed in Kbps converted from Gbps.
    """
    return speed * 1000000


def gbps_to_mbps(speed: float) -> float:
    """Method to convert `speed` from Gbps to Mbps value.

    Args:
        speed (float): Speed in Gbps to convert to Mbps.

    Returns:
        float: Speed in Mbps converted from Gbps.
    """
    return speed * 1000


def gbps_to_tbps(speed: float) -> float:
    """Method to convert `speed` from Gbps to Tbps value.

    Args:
        speed (float): Speed in Gbps to convert to Tbps.

    Returns:
        float: Speed in Tbps converted from Gbps.
    """
    return speed / 1000


def tbps_to_kbps(speed: float) -> float:
    """Method to convert `speed` from Tbps to Kbps value.

    Args:
        speed (float): Speed in Tbps to convert to Kbps.

    Returns:
        float: Speed in Kbps converted from Tbps.
    """
    return speed * 1000000000


def tbps_to_mbps(speed: float) -> float:
    """Method to convert `speed` from Tbps to Mbps value.

    Args:
        speed (float): Speed in Tbps to convert to Mbps.

    Returns:
        float: Speed in Mbps converted from Tbps.
    """
    return speed * 1000000


def tbps_to_gbps(speed: float) -> float:
    """Method to convert `speed` from Tbps to Gbps value.

    Args:
        speed (float): Speed in Tbps to convert to Gbps.

    Returns:
        float: Speed in Gbps converted from Tbps.
    """
    return speed * 1000


def name_to_kbits(speed: str) -> int:
    """Method to convert a short bandwidth name to int value in Kbps.

    Args:
        speed (str): Bandwidth to be converted like `100Gbps` to Kbps.

    Returns:
        int: int value of bandwidth to be converted to Kbps
    """
    if re.search("[mM]bps", speed):
        _value = int(mbps_to_kbps(int(re.sub("[mM]bps", "", speed))))
    if re.search("[gG]bps", speed):
        _value = int(gbps_to_kbps(int(re.sub("[gG]bps", "", speed))))
    return _value


def name_to_bits(speed: str) -> int:
    """Method to convert a short bandwidth name to int value in bps.

    Args:
        speed (str): Bandwidth to be converted like `100Gbps` to bps.

    Returns:
        int: int value of bandwidth to be converted to bps
    """
    if re.search("[mM]bps", speed):
        _value = name_to_kbits(speed) * 1000
    if re.search("[gG]bps", speed):
        _value = name_to_kbits(speed) * 1000
    return _value
