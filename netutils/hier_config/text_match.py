import re
from typing import Tuple, Union, Set


def equals(text: str, expression: Union[str, Set[str]]) -> bool:
    """Text equivalence test"""
    if isinstance(expression, str):
        return text == expression
    return text in expression


def startswith(text: str, expression: Union[str, Tuple[str, ...]]) -> bool:
    """Text starts with test"""
    return text.startswith(expression)


def endswith(text: str, expression: Union[str, Tuple[str, ...]]) -> bool:
    """Text ends with test"""
    return text.endswith(expression)


def contains(text: str, expression: str) -> bool:
    """Text contains test"""
    return expression in text


def anything(text: str, expression: str) -> bool:  # pylint: disable=unused-argument
    """Always returns True"""
    return True


def nothing(text: str, expression: str) -> bool:  # pylint: disable=unused-argument
    """Always returns False"""
    return False


def re_search(text: str, expression: str) -> bool:
    """
    Test regex match. This method is comparatively
    very slow and should be avoided where possible.
    """
    return re.search(expression, text) is not None


def dict_call(test: str, text: str, expression: str) -> bool:
    """
    Allows test methods to be called easily from variables
    """
    return {
        "equals": equals,
        "startswith": startswith,
        "endswith": endswith,
        "contains": contains,
        "re_search": re_search,
        "anything": anything,
        "nothing": nothing,
    }[test](text, expression)
