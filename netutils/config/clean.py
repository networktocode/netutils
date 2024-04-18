"""Functions for working with configuration to clean the config."""

# pylint: disable=anomalous-backslash-in-string

import re
import typing as t


def clean_config(config: str, filters: t.List[t.Dict[str, str]]) -> str:
    r"""Given a list of regex patterns, delete those lines that match.

    Args:
        config: A string representation of a device configuration.
        filters: A list of regex patterns used to delete remove configuration.

    Returns:
         Stripped down configuration.

    Examples:
        >>> from netutils.config.clean import clean_config
        >>> config = '''Building configuration...
        ... Current configuration : 1582 bytes
        ... !
        ... version 12.4
        ... service timestamps debug datetime msec
        ... service timestamps log datetime msec
        ... no service password-encryption
        ... !
        ... hostname CSR1
        ... !
        ... !
        ... !'''
        >>> clean_filters = [
        ...         {"regex": r"^Current\s+configuration.*\n"},
        ...         {"regex": r"^Building\s+configuration.*\n"},
        ...         {"regex": r"^ntp\s+clock-period.*\n"},
        ... ]
        >>> print(clean_config(config, clean_filters))
        !
        version 12.4
        service timestamps debug datetime msec
        service timestamps log datetime msec
        no service password-encryption
        !
        hostname CSR1
        !
        !
        !
        >>>
    """
    for item in filters:
        config = re.sub(item["regex"], "", config, flags=re.MULTILINE)
    return config


def sanitize_config(config: str, filters: t.Optional[t.List[t.Dict[str, str]]] = None) -> str:
    r"""Given a dictionary of filters, remove sensitive data from the provided config.

    Args:
        config: A string representation of a device configuration.
        filters: A list of dictionaries of regex patterns used to sanitize configuration, namely secrets. Defaults to an empty list.

    Returns:
        str: Sanitized configuration.

    Examples:
        >>> from netutils.config.clean import sanitize_config
        >>> config = '''enable secret 5 $1$nc08$bizeEFbgCBKjZP4nurNCd.!'''
        >>> SANITIZE_FILTERS = [
        ...    {
        ...         "regex": r"^(enable (password|secret)( level \d+)? \d) .+$",
        ...         "replace": r"\1 <removed>",
        ...    }
        ... ]
        >>> sanitize_config(config, SANITIZE_FILTERS)
        'enable secret 5 <removed>'
        >>>
    """
    if not filters:
        filters = []
    for item in filters:
        config = re.sub(item["regex"], item["replace"], config, flags=re.MULTILINE)
    return config
