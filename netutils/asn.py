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
