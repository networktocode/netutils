"""Functions for working with the banner configuration."""

import re

from netutils.constants import CARET_C


def delimiter_change(config: str, from_delimiter: str, to_delimiter: str) -> str:
    r"""Change the banner delimiter.

    Args:
        config: Configuration line containing banner delimiter.
        from_delimiter: Delimiter to replace in the banner.
        to_delimiter: Delimiter to include in the config.

    Returns:
        Configuration with delimiter replaced.

    Examples:
        >>> from netutils.banner import delimiter_change
        >>> delimiter_change("banner login ^\n******************\n    TEST BANNER\n******************^", "^", "^C")
        'banner login ^C\n******************\n    TEST BANNER\n******************^C'
        >>> delimiter_change("banner login #\n******************\n    TEST BANNER\n******************#", "#", "^C")
        'banner login ^C\n******************\n    TEST BANNER\n******************^C'
        >>> delimiter_change("banner login ^CCCCC\n******************\n    TEST BANNER\n******************^C", "^C", "^C")
        'banner login ^C\n******************\n    TEST BANNER\n******************^C'
    """
    config_line = config.replace(from_delimiter, to_delimiter)
    if to_delimiter == CARET_C:
        config_line = re.sub(r"\^C+", CARET_C, config_line)
    return config_line


def normalise_delimiter_caret_c(delimiter: str, config: str) -> str:
    r"""Normalise delimiter to ^C.

    Args:
        delimiter: Banner delimiter.
        config: Configuration line containing banner delimiter.

    Returns:
        Configuration with delimiter normalised to ^C.

    Examples:
        >>> from netutils.banner import normalise_delimiter_caret_c
        >>> normalise_delimiter_caret_c("^", "banner login ^\n******************\n    TEST BANNER\n******************^")
        'banner login ^C\n******************\n    TEST BANNER\n******************^C'
        >>> normalise_delimiter_caret_c("^C", "banner login ^CCCCC\n******************\n    TEST BANNER\n******************^C")
        'banner login ^C\n******************\n    TEST BANNER\n******************^C'
    """
    config_line = delimiter_change(config, delimiter, CARET_C)
    return config_line
