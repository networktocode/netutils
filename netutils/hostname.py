import re


def hostname_regex(hostname, match_regex_string):
    """Given a hostname string and regex string, return the regex match object or `None` if no match found
    
    This is useful in two primary use cases:

    1. Truthy conditional check that a hostname matches a given regex
    2. Returning regex capture groups from the hostname string

    Args:
        hostname: String representation of the device hostname
        match_regex_string: Regex string to match against

    Returns:
        Regex match object or None if no match found

    Extamples:
        >>> from netutils.hostname import hostname_regex
        >>> print("South Carolina" if hostname_regex("USSCAMS07", ".+SC.+\d\d") else "Not South Carolina")
        South Carolina
        >>>
        >>> match = hostname_regex("USSCAMS07", "([A-Z]{2})([A-Z]{2})([A-Z]{3})(\d*)")
        >>> match[1]
        'US'
        >>> match[2]
        'SC'
        >>> match[3]
        'AMS'
        >>> match[4]
        '07'

    """
    return re.match(match_regex_string, hostname)
