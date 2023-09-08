"""Utilities to expose regex functions, primarily for Jinja2 filters."""

import re
import typing as t


def _match_object(match: t.Optional[t.Match[str]]) -> t.Union[t.List[str], str, None]:
    """Helper method to better 'serialize' a re.Match object."""
    if not match:
        return None
    if match.groups():
        results = []
        for group in match.groups():
            results.append(group)
        return results
    return str(match.group())


def regex_findall(pattern: str, string: str) -> t.List[str]:
    r"""Given a regex pattern and string, return all non-overlapping matches of pattern in the string, as a list of strings.

    The main purpose of this function is provide a Jinja2 filter as this is simply a wrapper around `re.findall`.

    Args:
        pattern: Regex string to match against.
        string: String to check against.

    Returns:
        List of matches, when there is no match the list will be empty.

    Examples:
        >>> from netutils.regex import regex_findall
        >>> match = regex_findall("\w\w\w-RT\d\d", "NYC-RT01,NYC-RT02,SFO-SW01,SFO-RT01")
        >>> len(match)
        3
        >>> match[0]
        'NYC-RT01'

    """
    return re.findall(pattern, string)


def regex_match(pattern: str, string: str) -> t.Union[t.List[str], str, None]:
    r"""Given a regex pattern and string, return `None` if there is no matching `re.Match.groups()` if using capture groups or regex match via `re.Match.group()` on start of string.

    This is useful in the following use cases:

    1. Truthy conditional check that a string matches a given regex.
    2. Returning regex capture groups from the string.
    3. Matching for the start of a string, see `regex_search` when you do not want only start of string matching.

    The main purpose of this function is provide a Jinja2 filter as this is simply a wrapper around `re.match`.

    Args:
        pattern: Regex string to match against.
        string: String to check against.

    Returns:
        List of matches, match, or None no match found

    Examples:
        >>> from netutils.regex import regex_match
        >>> print("South Carolina" if regex_match(".+SC.+\d\d", "USSCAMS07") else "Not South Carolina")
        South Carolina
        >>>
        >>> match = regex_match("([A-Z]{2})([A-Z]{2})([A-Z]{3})(\d*)", "USSCAMS07")
        >>> match[0]
        'US'
        >>> match[1]
        'SC'
        >>> match[2]
        'AMS'
        >>> match[3]
        '07'

    """
    return _match_object(re.match(pattern, string))


def regex_search(pattern: str, string: str) -> t.Union[t.List[str], str, None]:
    r"""Given a regex pattern and string, return `None` if there is no matching `re.Match.groups()` if using capture groups or regex match via `re.Match.group()`.

    The main purpose of this function is provide a Jinja2 filter as this is simply a wrapper around `re.search`.

    Args:
        pattern: Regex string to match against.
        string: String to check against.

    Returns:
        List of matches, match, or None no match found.

    Examples:
        >>> from netutils.regex import regex_search
        >>> print("South Carolina" if regex_search(".+SC.+\d\d", "USSCAMS07") else "Not South Carolina")
        South Carolina
        >>>
        >>> match = regex_search("^([A-Z]{2})([A-Z]{2})([A-Z]{3})(\d*)", "USSCAMS07")
        >>> match[0]
        'US'
        >>> match[1]
        'SC'
        >>> match[2]
        'AMS'
        >>> match[3]
        '07'

    """
    return _match_object(re.search(pattern, string))


def regex_split(pattern: str, string: str, maxsplit: int = 0) -> t.List[str]:
    """Given a regex pattern and string, return the split the object based on the pattern a single element or single element of original value if there is no match.

    The main purpose of this function is provide a Jinja2 filter as this is simply a wrapper around `re.split`.

    Args:
        pattern: Regex string to match against.
        string: String to check against.
        maxsplit: The maximum time to split.

    Returns:
        List of string of the match or single element list of original value if no match

    Examples:
        >>> from netutils.regex import regex_split
        >>> match = regex_split(",", "NYC-RT01,NYC-RT02,SFO-SW01,SFO-RT01")
        >>> match[0]
        'NYC-RT01'
        >>> match[3]
        'SFO-RT01'
    """
    return re.split(pattern, string, maxsplit)


def regex_sub(pattern: str, repl: str, string: str, count: int = 0) -> str:
    """Given a regex pattern, replacement, and string replace the pattern within the string and return.

    The main purpose of this function is provide a Jinja2 filter as this is simply a wrapper around `re.sub`.

    Args:
        pattern: Regex string to match against.
        repl: Replacement characters that were matched in the pattern.
        string: String to check against.
        count: The maximum time to replace.

    Returns:
        List of string of the match or single element list of original value if no match

    Examples:
        >>> from netutils.regex import regex_sub
        >>> match = regex_sub(",", " ", "NYC-RT01,NYC-RT02,SFO-SW01,SFO-RT01")
        >>> match
        'NYC-RT01 NYC-RT02 SFO-SW01 SFO-RT01'
        >>> match = regex_sub("(ROUTER|RTR)", "RT", "NYC-ROUTER01,NYC-ROUTER02,NYC-RTR03")
        >>> match
        'NYC-RT01,NYC-RT02,NYC-RT03'
    """
    return re.sub(pattern, repl, string, count)
