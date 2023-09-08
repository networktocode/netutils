"""Functions for working with BGP ASNs."""


def asn_to_int(asplain: str) -> int:
    """Convert AS Number to standardized asplain notation as an integer.

    Args:
        asplain: An `asplain` notated BGP ASN with community.

    Returns:
        Integer value within of the given asplain value provided.

    Examples:
        >>> from netutils.asn import asn_to_int
        >>> asn_to_int("65000")
        65000
        >>> asn_to_int("65000.111")
        4259840111
        >>>
    """
    # ASN is in asdot notation
    if "." in asplain:
        asn_list = asplain.split(".")
        asn = int(f"{int(asn_list[0]):016b}{int(asn_list[1]):016b}", 2)
        return asn
    return int(asplain)


def int_to_asdot(asn_int: int) -> str:
    """Convert integer to standardized asdot notation for BGP ASN.

    Args:
        asn_int: Integer value of the BGP ASN.

    Returns:
        `asdot` notated BGP ASN as a string.

    Examples:
        >>> from netutils.asn import int_to_asdot
        >>> int_to_asdot(65000)
        '65000'
        >>> int_to_asdot(4259840111)
        '65000.111'
        >>>
    """
    if isinstance(asn_int, str):
        asn_int = int(asn_int)
    if asn_int > 2**32 - 1 or asn_int < 1:
        raise ValueError(f"`{str(asn_int)}` is not within range of 1 - 2^32-1")
    if asn_int >= 2**16:
        asn1 = asn_int >> 16
        asn2 = asn_int & ((1 << 16) - 1)
        return f"{asn1}.{asn2}"
    return str(asn_int)
