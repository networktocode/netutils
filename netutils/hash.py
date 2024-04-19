"""Functions for hashing data."""

import hashlib
import typing as t


def hash_data(data: bytes, algorithm: str) -> t.Any:
    """Convenience function primarily built to expose hashlib to Jinja.

    Args:
        data (bytes): Data to hash.
        algorithm (str): Hashing algorithm to use.

    Returns:
        bytes: Hashed data.

    Raises:
        AttributeError: Invalid algorithm specified.

    Examples:
        >>> from netutils.hash import hash_data
        >>> hash_data("test", "md5")
        '098f6bcd4621d373cade4e832627b4f6'

        >>> from jinja2 import Environment
        >>> from netutils.utils import jinja2_convenience_function
        >>>
        >>> env = Environment(trim_blocks=True, lstrip_blocks=True)
        >>> env.filters.update(jinja2_convenience_function())
        >>> template_str = "{{ 'test' | hash_data('md5') }}"
        >>> template = env.from_string(template_str)
        >>> result = template.render()
        >>> print(result)
        098f6bcd4621d373cade4e832627b4f6
    """
    if not isinstance(data, bytes):
        data = str(data).encode()
    algorithm = algorithm.lower()
    hasher = getattr(hashlib, algorithm)
    return hasher(data).hexdigest()
