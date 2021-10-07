"""Functions for performing bandwidth calculations."""
import re


def bps_to_kbps(speed: int) -> float:
    """Method to convert `speed` from bps to Kbps value.

    Args:
        speed (int): Speed in bps to convert to Kbps.

    Returns:
        float: Speed in Kbps converted from bps.
    """
    return speed / 1000


def bps_to_kbytes(speed: int) -> float:
    """Method to convert `speed` from bps to Kbps value.

    Args:
        speed (int): Speed in bps to convert to KBps.

    Returns:
        float: Speed in KBps converted from bps.
    """
    return speed / 8000


def bps_to_mbps(speed: int) -> float:
    """Method to convert `speed` from bps to Mbps value.

    Args:
        init_speed (int): Speed in bps to convert to Mbps.

    Returns:
        float: Speed in Mbps converted from bps.
    """
    return speed / 1000000


def bps_to_mbytes(speed: int) -> float:
    """Method to convert `speed` from bps to MBps value.

    Args:
        init_speed (int): Speed in bps to convert to MBps.

    Returns:
        float: Speed in MBps converted from bps.
    """
    return speed / 8000000


def bps_to_gbps(speed: int) -> float:
    """Method to convert `speed` from bps to Gbps value.

    Args:
        init_speed (int): Speed in bps to convert to Gbps.

    Returns:
        float: Speed in Gbps converted from bps.
    """
    return speed / 1000000000


def bps_to_gbytes(speed: int) -> float:
    """Method to convert `speed` from bps to GBps value.

    Args:
        init_speed (int): Speed in bps to convert to GBps.

    Returns:
        float: Speed in GBps converted from bps.
    """
    return speed / 8000000000


def bps_to_tbps(speed: int) -> float:
    """Method to convert `speed` from bps to Tbps value.

    Args:
        init_speed (int): Speed in bps to convert to Tbps.

    Returns:
        float: Speed in Tbps converted from bps.
    """
    return speed / 1000000000000


def bps_to_tbytes(speed: int) -> float:
    """Method to convert `speed` from bps to TBps value.

    Args:
        init_speed (int): Speed in bps to convert to TBps.

    Returns:
        float: Speed in TBps converted from bps.
    """
    return speed / 8000000000000


def kbps_to_mbps(speed: float) -> float:
    """Method to convert `speed` from Kbps to Mbps value.

    Args:
        init_speed (float): Speed in Kbps to convert to Mbps.

    Returns:
        float: Speed in Mbps converted from Kbps.
    """
    return speed / 1000


def kbps_to_mbytes(speed: float) -> float:
    """Method to convert `speed` from Kbps to MBps value.

    Args:
        init_speed (float): Speed in Kbps to convert to MBps.

    Returns:
        float: Speed in MBps converted from Kbps.
    """
    return speed / 8000


def kbps_to_gbps(speed: float) -> float:
    """Method to convert `speed` from Kbps to Gbps value.

    Args:
        init_speed (float): Speed in Kbps to convert to Gbps.

    Returns:
        float: Speed in Gbps converted from Kbps.
    """
    return speed / 1000000


def kbps_to_gbytes(speed: float) -> float:
    """Method to convert `speed` from Kbps to GBps value.

    Args:
        init_speed (float): Speed in Kbps to convert to GBps.

    Returns:
        float: Speed in GBps converted from Kbps.
    """
    return speed / 8000000


def kbps_to_tbps(speed: float) -> float:
    """Method to convert `speed` from Kbps to Tbps value.

    Args:
        init_speed (float): Speed in Kbps to convert to Tbps.

    Returns:
        float: Speed in Tbps converted from Kbps.
    """
    return speed / 1000000000


def kbps_to_tbytes(speed: float) -> float:
    """Method to convert `speed` from Kbps to TBps value.

    Args:
        init_speed (float): Speed in Kbps to convert to TBps.

    Returns:
        float: Speed in TBps converted from Kbps.
    """
    return speed / 8000000000


def mbps_to_gbps(speed: float) -> float:
    """Method to convert `speed` from Mbps to Gbps value.

    Args:
        init_speed (float): Speed in Mbps to convert to Gbps.

    Returns:
        float: Speed in Gbps converted from Mbps.
    """
    return speed / 1000


def mbps_to_gbytes(speed: float) -> float:
    """Method to convert `speed` from Mbps to GBps value.

    Args:
        init_speed (float): Speed in Mbps to convert to GBps.

    Returns:
        float: Speed in GBps converted from Mbps.
    """
    return speed / 8000


def mbps_to_tbps(speed: float) -> float:
    """Method to convert `speed` from Mbps to Tbps value.

    Args:
        init_speed (float): Speed in Mbps to convert to Tbps.

    Returns:
        float: Speed in Tbps converted from Mbps.
    """
    return speed / 1000000


def mbps_to_tbytes(speed: float) -> float:
    """Method to convert `speed` from Mbps to TBps value.

    Args:
        init_speed (float): Speed in Mbps to convert to TBps.

    Returns:
        float: Speed in TBps converted from Mbps.
    """
    return speed / 8000000


def mbps_to_kbps(speed: float) -> float:
    """Method to convert `speed` from Mbps to Kbps value.

    Args:
        speed (float): Speed in Mbps to convert to Kbps.

    Returns:
        float: Speed in Kbps converted from Mbps.
    """
    return speed * 1000


def mbps_to_kbytes(speed: float) -> float:
    """Method to convert `speed` from Mbps to KBps value.

    Args:
        speed (float): Speed in Mbps to convert to KBps.

    Returns:
        float: Speed in KBps converted from Mbps.
    """
    return speed * 125


def gbps_to_kbps(speed: float) -> float:
    """Method to convert `speed` from Gbps to Kbps value.

    Args:
        speed (float): Speed in Gbps to convert to Kbps.

    Returns:
        float: Speed in Kbps converted from Gbps.
    """
    return speed * 1000000


def gbps_to_kbytes(speed: float) -> float:
    """Method to convert `speed` from Gbps to KBps value.

    Args:
        speed (float): Speed in Gbps to convert to KBps.

    Returns:
        float: Speed in KBps converted from Gbps.
    """
    return speed * 125000


def gbps_to_mbps(speed: float) -> float:
    """Method to convert `speed` from Gbps to Mbps value.

    Args:
        speed (float): Speed in Gbps to convert to Mbps.

    Returns:
        float: Speed in Mbps converted from Gbps.
    """
    return speed * 1000


def gbps_to_mbytes(speed: float) -> float:
    """Method to convert `speed` from Gbps to MBps value.

    Args:
        speed (float): Speed in Gbps to convert to MBps.

    Returns:
        float: Speed in MBps converted from Gbps.
    """
    return speed * 125


def gbps_to_tbps(speed: float) -> float:
    """Method to convert `speed` from Gbps to Tbps value.

    Args:
        speed (float): Speed in Gbps to convert to Tbps.

    Returns:
        float: Speed in Tbps converted from Gbps.
    """
    return speed / 1000


def gbps_to_tbytes(speed: float) -> float:
    """Method to convert `speed` from Gbps to TBps value.

    Args:
        speed (float): Speed in Gbps to convert to TBps.

    Returns:
        float: Speed in TBps converted from Gbps.
    """
    return speed / 8000


def tbps_to_kbps(speed: float) -> float:
    """Method to convert `speed` from Tbps to Kbps value.

    Args:
        speed (float): Speed in Tbps to convert to Kbps.

    Returns:
        float: Speed in Kbps converted from Tbps.
    """
    return speed * 1000000000


def tbps_to_kbytes(speed: float) -> float:
    """Method to convert `speed` from Tbps to KBps value.

    Args:
        speed (float): Speed in Tbps to convert to KBps.

    Returns:
        float: Speed in KBps converted from Tbps.
    """
    return speed * 125000000


def tbps_to_mbps(speed: float) -> float:
    """Method to convert `speed` from Tbps to Mbps value.

    Args:
        speed (float): Speed in Tbps to convert to Mbps.

    Returns:
        float: Speed in Mbps converted from Tbps.
    """
    return speed * 1000000


def tbps_to_mbytes(speed: float) -> float:
    """Method to convert `speed` from Tbps to MBps value.

    Args:
        speed (float): Speed in Tbps to convert to MBps.

    Returns:
        float: Speed in MBps converted from Tbps.
    """
    return speed * 125000


def tbps_to_gbps(speed: float) -> float:
    """Method to convert `speed` from Tbps to Gbps value.

    Args:
        speed (float): Speed in Tbps to convert to Gbps.

    Returns:
        float: Speed in Gbps converted from Tbps.
    """
    return speed * 1000


def tbps_to_gbytes(speed: float) -> float:
    """Method to convert `speed` from Tbps to GBps value.

    Args:
        speed (float): Speed in Tbps to convert to GBps.

    Returns:
        float: Speed in GBps converted from Tbps.
    """
    return speed * 125


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
        _value = name_to_kbits(speed) * 1000000
    return _value


def name_to_kbytes(speed: str) -> float:
    """Method to convert a short bandwidth name to int value in KBps.

    Args:
        speed (str): Bandwidth to be converted like `100GBps` to KBps.

    Returns:
        int: int value of bandwidth to be converted to KBps
    """
    if re.search("[mM]Bps", speed):
        _value = mbps_to_kbytes(float(re.sub("[mM]Bps", "", speed)))
    if re.search("[gG]Bps", speed):
        _value = gbps_to_kbytes(float(re.sub("[gG]Bps", "", speed)))
    return _value


def name_to_bytes(speed: str) -> float:
    """Method to convert a short bandwidth name to int value in Bps.

    Args:
        speed (str): Bandwidth to be converted like `100GBps` to Bps.

    Returns:
        int: int value of bandwidth to be converted to Bps
    """
    if re.search("[mM]Bps", speed):
        _value = mbps_to_kbytes(float(re.sub("[mM]Bps", "", speed)))
    if re.search("[gG]Bps", speed):
        _value = gbps_to_kbytes(float(re.sub("[gG]Bps", "", speed)))
    if re.search("[tT]Bps", speed):
        _value = tbps_to_kbytes(float(re.sub("[tT]Bps", "", speed)))
    return _value


def kbits_to_name(speed: int, nbr_decimal: int = 0) -> str:  # pylint: disable=too-many-branches
    """Method to convert an int value for speed int kbits to the name value.

    Args:
        speed (int): Speed in kbits to be converted.
        nbr_decimal (int, optional): Precision of end result, ie number of decimal points to round to. Defaults to 0.

    Returns:
        str: Name value for speed in kbits
    """
    if not isinstance(speed, int):
        return None

    if speed < 1000:
        return f"{speed}Kbps"
    if 1000 >= speed < 1000000:
        if nbr_decimal == 0:
            results = f"{round(kbps_to_mbps(speed))}Mbps"
        else:
            results = f"{round(kbps_to_mbps(speed), nbr_decimal)}Mbps"
        return results
    if 1000000 >= speed < 1000000000:
        if nbr_decimal == 0:
            results = f"{round(kbps_to_gbps(speed))}Gbps"
        else:
            results = f"{round(kbps_to_gbps(speed), nbr_decimal)}Gbps"
        return results
    if speed >= 1000000000:
        if nbr_decimal == 0:
            results = f"{round(kbps_to_tbps(speed))}Tbps"
        else:
            results = f"{round(kbps_to_tbps(speed), nbr_decimal)}Tbps"
        return results
    return None


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
        return None

    if speed < 1000:
        return f"{speed}bps"
    if 1000 >= speed < 1000000:
        if nbr_decimal == 0:
            results = f"{round(bps_to_kbps(speed))}Kbps"
        else:
            results = f"{round(bps_to_kbps(speed), nbr_decimal)}Kbps"
        return results
    if 1000000 >= speed < 1000000000:
        if nbr_decimal == 0:
            results = f"{round(bps_to_mbps(speed))}Mbps"
        else:
            results = f"{round(bps_to_mbps(speed), nbr_decimal)}Mbps"
        return results
    if 1000000000 >= speed < 1000000000000:
        if nbr_decimal == 0:
            results = f"{round(bps_to_gbps(speed))}Gbps"
        else:
            results = f"{round(bps_to_gbps(speed), nbr_decimal)}Gbps"
        return results
    if speed >= 1000000000000:
        if nbr_decimal == 0:
            results = f"{round(bps_to_tbps(speed))}Tbps"
        else:
            results = f"{round(bps_to_tbps(speed), nbr_decimal)}Tbps"
        return results
    return None


def bytes_to_name(speed: int, nbr_decimal: int = 0) -> str:
    """Method to convert an int value for speed in bytes to the name value.

    Args:
        speed (int): Speed in bytes to be converted.
        nbr_decimal (int, optional): Precision of end result, ie number of decimal points to round to. Defaults to 0.

    Returns:
        str: Name value for speed in bytes
    """
    if speed <= 8000:
        if nbr_decimal == 0:
            result = f"{round(bps_to_kbytes(speed))}KBps"
        else:
            result = f"{round(bps_to_kbytes(speed), nbr_decimal)}KBps"
        return result
    if speed <= 8000000:
        if nbr_decimal == 0:
            result = f"{round(bps_to_mbytes(speed))}MBps"
        else:
            result = f"{round(bps_to_mbytes(speed), nbr_decimal)}MBps"
        return result
    if speed <= 8000000000:
        if nbr_decimal == 0:
            result = f"{round(bps_to_gbytes(speed))}GBps"
        else:
            result = f"{round(bps_to_gbytes(speed), nbr_decimal)}GBps"
        return result
    if speed <= 8000000000000:
        if nbr_decimal == 0:
            result = f"{round(bps_to_tbytes(speed))}TBps"
        else:
            result = f"{round(bps_to_tbytes(speed), nbr_decimal)}TBps"
        return result
    return None
