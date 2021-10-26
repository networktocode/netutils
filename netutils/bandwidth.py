"""Functions for performing bandwidth calculations."""
import re


def _get_bits_mapping():
    bits_value = 0
    bits_mapping = {}
    for _bit in ["bps", "Kbps", "Mbps", "Gbps", "Tbps", "Pbps", "Ebps", "Zbps"]:
        bits_mapping[_bit] = {"low": bits_value}
        if bits_value == 0:
            bits_value = 1000
        else:
            bits_value = bits_value * 1000
        bits_mapping[_bit]["high"] = bits_value
    return bits_mapping


BITS_MAPPING = _get_bits_mapping()

BITS_VALUE = 0
for bit in ["bps", "Kbps", "Mbps", "Gbps", "Tbps", "Pbps", "Ebps", "Zbps"]:
    BITS_MAPPING[bit] = {"low": BITS_VALUE}
    if BITS_VALUE == 0:
        BITS_VALUE = 1000
    else:
        BITS_VALUE = BITS_VALUE * 1000
    BITS_MAPPING[bit]["high"] = BITS_VALUE

BYTES_MAPPING = {}
BYTES_VALUE = 0
for bit in ["Bps", "KBps", "MBps", "GBps", "TBps", "PBps", "EBps", "ZBps"]:
    BYTES_MAPPING[bit] = {"low": BYTES_VALUE}
    if BYTES_VALUE == 0:
        BYTES_VALUE = 8000
    else:
        BYTES_VALUE = BYTES_VALUE * 1000
    BYTES_MAPPING[bit]["high"] = BYTES_VALUE


def name_to_bits(speed: str) -> int:
    """Method to convert a short bandwidth name to int value in bps.

    Args:
        speed (str): Bandwidth to be converted like `100Gbps` to bps.

    Returns:
        int: value of bandwidth to be converted to bps
    """
    if " " in speed:
        match = re.match(r"([0-9.]+) ([A-Z]bps)", speed)
    else:
        match = re.match(r"([0-9.]+)([A-Z]bps)", speed)
    if not match:
        raise ValueError(f"Speed of {speed} was not a valid speed representation.")
    bit_speed, bit_name = match.groups()
    return int(float(bit_speed) * BITS_MAPPING[bit_name]["low"])


def name_to_bytes(speed: str) -> float:
    """Method to convert a short bandwidth name to float value in Bps.

    Args:
        speed (str): Bandwidth to be converted like `100GBps` to Bps.

    Returns:
        float: value of bandwidth to be converted to Bps
    """
    if " " in speed:
        match = re.match(r"([0-9.]+) ([A-Z]Bps)", speed)
    else:
        match = re.match(r"([0-9.]+)([A-Z]Bps)", speed)
    if not match:
        raise ValueError(f"Speed of {speed} was not a valid speed representation.")
    bit_speed, bit_name = match.groups()
    return (float(bit_speed) * BYTES_MAPPING[bit_name]["low"]) / 8


def bits_to_name(  # pylint: disable=too-many-branches,too-many-return-statements
    speed: int, nbr_decimal: int = 0
) -> str:
    """Method to convert an int value for speed int bits to the name value.

    Args:
        speed (int): Speed in bits to be converted.
        nbr_decimal (int, optional): Precision of end result, ie number of decimal points to round to. Defaults to 0.

    Returns:
        str: Name value for speed in bits
    """
    if not isinstance(speed, int):
        raise ValueError(f"Speed of {speed} was not a valid speed integer.")

    for bit_type, val in BITS_MAPPING.items():
        if val["low"] <= speed < val["high"]:
            try:
                return f"{round(speed / val['low'], nbr_decimal)}{bit_type}"
            except ZeroDivisionError:
                return f"{round(speed, nbr_decimal)}{bit_type}"
    return None


def bytes_to_name(speed: float, nbr_decimal: int = 0) -> str:
    """Method to convert an int value for speed in bytes to the name value.

    Args:
        speed (int): Speed in bytes to be converted.
        nbr_decimal (int, optional): Precision of end result, ie number of decimal points to round to. Defaults to 0.

    Returns:
        str: Name value for speed in bytes
    """
    if not isinstance(speed, float):
        raise ValueError(f"Speed of {speed} was not a valid speed.")

    byte_speed = speed * 8
    for bit_type, val in BYTES_MAPPING.items():
        if val["low"] <= speed < val["high"]:
            try:
                return f"{round(byte_speed / val['low'], nbr_decimal)}{bit_type}"
            except ZeroDivisionError:
                return f"{round(byte_speed, nbr_decimal)}{bit_type}"
    return None


def name_to_name(speed: str, speed_type: str, nbr_decimal: int = 0) -> str:
    """Method to convert a short bandwidth name to another bandwdth name.

    Args:
        speed (str): Bandwidth to be converted like `100GBps`.
        speed_type (str): Name to convert the bandwdth to like `MBps`.
        nbr_decimal (int, optional): Precision of end result, ie number of decimal points to round to. Defaults to 0.

    Returns:
        str: The named value which user wishes to return to.
    """
    if " " in speed:
        match = re.match(r"([0-9.]+) ([A-Z][bB]ps)", speed)
    else:
        match = re.match(r"([0-9.]+)([A-Z][bB]ps)", speed)
    if not match:
        raise ValueError(f"Speed of {speed} was not a valid speed representation.")
    _, name = match.groups()
    # Find out if the `original` value is a bit or a byte
    if name in BYTES_MAPPING.keys():
        bit_value = name_to_bytes(speed) * 8
    elif name in BITS_MAPPING.keys():
        bit_value = name_to_bits(speed)
    else:
        raise ValueError(f"Speed of {speed} was not a valid speed representation.")

    # Find out if the `expected` value is a bit or a byte
    if speed_type in BYTES_MAPPING.keys():
        bit_multiplier = BYTES_MAPPING[speed_type]["low"]
    elif speed_type in BITS_MAPPING.keys():
        bit_multiplier = BITS_MAPPING[speed_type]["low"]

    try:
        return f"{round(bit_value / bit_multiplier, nbr_decimal)}{speed_type}"
    except ZeroDivisionError:
        return f"{round(bit_value, nbr_decimal)}{speed_type}"
