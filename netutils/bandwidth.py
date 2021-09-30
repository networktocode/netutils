"""Functions for performing bandwidth calculations."""
import math


def convert_Kbps_to_Mbps(speed: float) -> float:
    """Method to convert `speed` from Kbps to Mbps value.

    Args:
        init_speed (float): Speed in Kbps to convert to Mbps.

    Returns:
        float: Speed in Mbps converted from Kbps.
    """
    return speed / 1000


def convert_Kbps_to_Gbps(speed: float) -> float:
    """Method to convert `speed` from Kbps to Gbps value.

    Args:
        init_speed (float): Speed in Kbps to convert to Gbps.

    Returns:
        float: Speed in Gbps converted from Kbps.
    """
    return speed / 1000000


def convert_Kbps_to_Tbps(speed: float) -> float:
    """Method to convert `speed` from Kbps to Tbps value.

    Args:
        init_speed (float): Speed in Kbps to convert to Tbps.

    Returns:
        float: Speed in Tbps converted from Kbps.
    """
    return speed / 1000000000


def convert_Mbps_to_Gbps(speed: float) -> float:
    """Method to convert `speed` from Mbps to Gbps value.

    Args:
        init_speed (float): Speed in Mbps to convert to Gbps.

    Returns:
        float: Speed in Mbps converted from Kbps.
    """
    return speed / 1000


def convert_Mbps_to_Tbps(speed: float) -> float:
    """Method to convert `speed` from Mbps to Tbps value.

    Args:
        init_speed (float): Speed in Mbps to convert to Tbps.

    Returns:
        float: Speed in Tbps converted from Kbps.
    """
    return speed / 1000000


def convert_Mbps_to_Kbps(speed: float) -> float:
    """Method to convert `speed` from Mbps to Kbps value.

    Args:
        speed (float): Speed in Mbps to convert to Kbps.

    Returns:
        float: Speed in Kbps converted from Mbps.
    """
    return speed * 1000


def convert_Gbps_to_Kbps(speed: float) -> float:
    """Method to convert `speed` from Gbps to Kbps value.

    Args:
        speed (float): Speed in Gbps to convert to Kbps.

    Returns:
        float: Speed in Kbps converted from Gbps.
    """
    return speed * 1000000


def convert_Gbps_to_Mbps(speed: float) -> float:
    """Method to convert `speed` from Gbps to Mbps value.

    Args:
        speed (float): Speed in Gbps to convert to Mbps.

    Returns:
        float: Speed in Mbps converted from Gbps.
    """
    return speed * 1000


def convert_Gbps_to_Tbps(speed: float) -> float:
    """Method to convert `speed` from Gbps to Tbps value.

    Args:
        speed (float): Speed in Gbps to convert to Tbps.

    Returns:
        float: Speed in Tbps converted from Gbps.
    """
    return speed / 1000


def convert_Tbps_to_Kbps(speed: float) -> float:
    """Method to convert `speed` from Tbps to Kbps value.

    Args:
        speed (float): Speed in Tbps to convert to Kbps.

    Returns:
        float: Speed in Kbps converted from Tbps.
    """
    return speed * 1000000000


def convert_Tbps_to_Mbps(speed: float) -> float:
    """Method to convert `speed` from Tbps to Mbps value.

    Args:
        speed (float): Speed in Tbps to convert to Mbps.

    Returns:
        float: Speed in Mbps converted from Tbps.
    """
    return speed * 1000000


def convert_Tbps_to_Gbps(speed: float) -> float:
    """Method to convert `speed` from Tbps to Gbps value.

    Args:
        speed (float): Speed in Tbps to convert to Gbps.

    Returns:
        float: Speed in Gbps converted from Tbps.
    """
    return speed * 1000
