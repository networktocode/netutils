"""Functions for performing bandwidth calculations."""

import re
import typing as t


def _get_bits_mapping() -> t.Dict[str, t.Dict[str, int]]:
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


def _get_bytes_mapping() -> t.Dict[str, t.Dict[str, int]]:
    bytes_value = 0
    bytes_mapping = {}
    for _byte in ["Bps", "KBps", "MBps", "GBps", "TBps", "PBps", "EBps", "ZBps"]:
        bytes_mapping[_byte] = {"low": bytes_value}
        if bytes_value == 0:
            bytes_value = 8000
        else:
            bytes_value = bytes_value * 1000
        bytes_mapping[_byte]["high"] = bytes_value
    return bytes_mapping


BYTES_MAPPING = _get_bytes_mapping()


def _normalize_bw(speed: str) -> str:
    per_second_mapping = {
        "b": "bps",
        "Kb": "Kbps",
        "Mb": "Mbps",
        "Gb": "Gbps",
        "Tb": "Tbps",
        "Pb": "Pbps",
        "Eb": "Ebps",
        "Zb": "Zbps",
        "B": "Bps",
        "KB": "KBps",
        "MB": "MBps",
        "GB": "GBps",
        "TB": "TBps",
        "PB": "PBps",
        "EB": "EBps",
        "ZB": "ZBps",
    }
    speed = speed.replace(" ", "")
    tail = speed.lstrip(r"0123456789")
    head = speed[: -len(tail)].rstrip()
    tail = per_second_mapping.get(tail, tail)
    return f"{head}{tail}"


def name_to_bits(speed: str) -> int:
    """Method to convert a short bandwidth name to int value in bps.

    Args:
        speed: Bandwidth to be converted like `100Gbps` to bps.

    Returns:
        value of bandwidth to be converted to bps

    Examples:
        >>> from netutils.bandwidth import name_to_bits
        >>> name_to_bits("10Gbps")
        10000000000
        >>> name_to_bits("33.6Kbps")
        33600
        >>> name_to_bits("2.5Gbps")
        2500000000
        >>> name_to_bits('100 MB')
        800000000
    """
    if not isinstance(speed, str):
        raise ValueError(f"Speed of {speed} was not a valid speed representation.")
    speed = _normalize_bw(speed)
    match = re.match(r"([0-9.]+)([A-Z]?[bB]ps)", speed)
    if not match:
        raise ValueError(f"Speed of {speed} was not a valid speed representation.")
    bit_speed, bit_name = match.groups()
    if bit_name in BITS_MAPPING.keys():
        return int(float(bit_speed) * BITS_MAPPING[bit_name]["low"])
    if bit_name in BYTES_MAPPING.keys():
        return int(float(bit_speed) * BYTES_MAPPING[bit_name]["low"])
    raise ValueError(f"Speed of {speed} was not a valid speed representation.")


def name_to_bytes(speed: str) -> float:
    """Method to convert a short bandwidth name to float value in Bps.

    Args:
        speed: Bandwidth to be converted like `100GBps` to Bps.

    Returns:
        value of bandwidth to be converted to Bps

    Examples:
        >>> from netutils.bandwidth import name_to_bytes
        >>> name_to_bytes("10Gbps")
        1250000000.0
        >>> name_to_bytes("100Mbps")
        12500000.0
        >>> name_to_bytes("100GBps")
        100000000000.0
        >>> name_to_bytes('100 GB')
        100000000000.0
    """
    if not isinstance(speed, str):
        raise ValueError(f"Speed of {speed} was not a valid speed representation.")
    speed = _normalize_bw(speed)
    match = re.match(r"([0-9.]+)([A-Z]?[bB]ps)", speed)
    if not match:
        raise ValueError(f"Speed of {speed} was not a valid speed representation.")
    byte_speed, byte_name = match.groups()
    if byte_name in BYTES_MAPPING.keys():
        return (float(byte_speed) * BYTES_MAPPING[byte_name]["low"]) / 8
    if byte_name in BITS_MAPPING.keys():
        return (float(byte_speed) * BITS_MAPPING[byte_name]["low"]) * 0.125
    raise ValueError(f"Speed of {speed} was not a valid speed representation.")


def bits_to_name(  # pylint: disable=too-many-branches,too-many-return-statements
    speed: int, nbr_decimal: t.Optional[int] = 0
) -> str:
    """Method to convert an int value for speed int bits to the name value.

    Args:
        speed: Speed in bits to be converted.
        nbr_decimal: Precision of end result, ie number of decimal points to round to. Defaults to 0.

    Returns:
        Name value for speed in bits

    Examples:
        >>> from netutils.bandwidth import bits_to_name
        >>> bits_to_name(125000)
        '125Kbps'
        >>> bits_to_name(1000000000)
        '1Gbps'
    """
    if not isinstance(speed, int):
        raise ValueError(f"Speed of {speed} was not a valid speed integer.")
    if nbr_decimal == 0:
        nbr_decimal = None

    for bit_type, val in BITS_MAPPING.items():
        if val["low"] <= speed < val["high"]:
            if val["low"] == 0:
                return f"{round(speed, nbr_decimal)}{bit_type}"
            return f"{round(speed / val['low'], nbr_decimal)}{bit_type}"
    raise ValueError(f"Speed of {speed} was not a valid speed representation.")


def bytes_to_name(speed: float, nbr_decimal: int = 0) -> str:
    """Method to convert an int value for speed in bytes to the name value.

    Args:
        speed: Speed in bytes to be converted.
        nbr_decimal: Precision of end result, ie number of decimal points to round to. Defaults to 0.

    Returns:
        Name value for speed in bytes

    Examples:
        >>> from netutils.bandwidth import bytes_to_name
        >>> bytes_to_name(10000.0)
        '10.0KBps'
        >>> bytes_to_name(10000000.0)
        '10.0MBps'
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
    raise ValueError(f"Speed of {speed} was not a valid speed representation.")


def name_to_name(speed: str, speed_type: str, nbr_decimal: int = 0) -> str:
    """Method to convert a short bandwidth name to another bandwidth name.

    Args:
        speed: Bandwidth to be converted like `100GBps`.
        speed_type: Name to convert the bandwidth to like `MBps`.
        nbr_decimal: Precision of end result, ie number of decimal points to round to. Defaults to 0.

    Returns:
        The named value which user wishes to return to.

    Examples:
        >>> from netutils.bandwidth import name_to_name
        >>> name_to_name("10Gbps", "Kbps")
        '10000000.0Kbps'
        >>> name_to_name("10GBps", "Kbps")
        '80000000.0Kbps'
        >>> name_to_name("10KBps", "Gbps", 4)
        '0.0001Gbps'
    """
    if not isinstance(speed, str):
        raise ValueError(f"Speed of {speed} was not a valid speed representation.")
    speed = speed.replace(" ", "")
    match = re.match(r"([0-9.]+)([A-Z]?[bB]ps)", speed)
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
    else:
        raise ValueError(f"Speed type of {speed_type} was not a valid type.")

    try:
        return f"{round(bit_value / bit_multiplier, nbr_decimal)}{speed_type}"
    except ZeroDivisionError:
        return f"{round(bit_value, nbr_decimal)}{speed_type}"
