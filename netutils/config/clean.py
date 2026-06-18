"""Functions for working with configuration to clean the config."""

# pylint: disable=anomalous-backslash-in-string

import re
import typing as t

from netutils.utils import jinja2_convenience_function

try:
    import jinja2

    HAS_JINJA2 = True
except ImportError:
    HAS_JINJA2 = False


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


def sanitize_config_jinja(config: str, filters: t.Optional[t.List[t.Dict[str, str]]] = None) -> str:
    r"""Like ``sanitize_config``, but renders each ``replace`` value as a Jinja2 template.

    This allows the replacement text to transform the matched data, e.g. hashing a secret
    with the ``hash_data`` filter instead of dropping it with a static placeholder. The regex
    capture groups are exposed to the template so the original values can be transformed in
    place. References to capture groups follow the familiar ``re.sub`` backreference syntax
    (``\1``, ``\2``, ...) and may be used anywhere inside a ``{{ ... }}`` expression. Named
    groups (``(?P<name>...)``) are additionally available by name, so a user-defined group
    name can never shadow a positional backreference.

    A ``replace`` value that contains no Jinja expression (``{{``) falls back to plain
    ``re.sub`` string substitution, so a mixed list of filters works as expected.

    This function requires the optional ``jinja2`` dependency
    (``pip install netutils[optionals]``).

    Args:
        config: A string representation of a device configuration.
        filters: A list of dictionaries of regex patterns and Jinja-aware replacement
            templates used to sanitize configuration. Defaults to an empty list.

    Returns:
        str: Sanitized configuration.

    Examples:
        >>> from netutils.config.clean import sanitize_config_jinja
        >>> config = "username admin privilege 15 secret 9 SuperSecret"
        >>> SANITIZE_FILTERS = [
        ...     {
        ...         "regex": r"^username (\S+) privilege 15 secret 9 (\S+)$",
        ...         "replace": r"username {{ \1 }} privilege 15 secret 9 {{ \2 | hash_data('md5') }}",
        ...     }
        ... ]
        >>> sanitize_config_jinja(config, SANITIZE_FILTERS)
        'username admin privilege 15 secret 9 2257151269b83ef0e139c3eec8bbcbcb'
    """
    if not filters:
        return config

    # Only the Jinja path needs jinja2; if every filter is plain, behave like sanitize_config.
    if not any("{{" in item["replace"] for item in filters):
        return sanitize_config(config, filters)

    if not HAS_JINJA2:
        raise ImportError(
            "The optional 'jinja2' dependency is required to use sanitize_config_jinja. "
            "Install it with `pip install netutils[optionals]` or `pip install jinja2`."
        )

    env = jinja2.Environment(autoescape=False)  # noqa: S701  # config text must not be HTML-escaped
    env.filters.update(jinja2_convenience_function())

    def _make_replacer(template_str: str) -> t.Callable[[t.Match[str]], str]:
        jinja_ready = re.sub(r"\\(\d+)", r"_re_groups[\1]", template_str)
        template = env.from_string(jinja_ready)

        def _replace(match: t.Match[str]) -> str:
            # Named groups are exposed by name; positional groups are reached via `_re_groups`,
            # indexed like a `re.Match` object (index 0 is the whole match, 1 is \1, and so on).
            context: t.Dict[str, t.Any] = dict(match.groupdict())
            context["_re_groups"] = (match.group(0), *match.groups())
            return template.render(**context)

        return _replace

    for item in filters:
        if "{{" in item["replace"]:
            config = re.sub(item["regex"], _make_replacer(item["replace"]), config, flags=re.MULTILINE)
        else:
            config = re.sub(item["regex"], item["replace"], config, flags=re.MULTILINE)
    return config
