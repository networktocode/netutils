"""Functions for working with configuration to clean the config."""

# pylint: disable=anomalous-backslash-in-string

import re
import typing as t

from netutils.utils import jinja2_convenience_function

try:
    from jinja2.sandbox import SandboxedEnvironment

    HAS_JINJA2 = True
except ImportError:
    HAS_JINJA2 = False

# A `re.sub` backreference, such as \1, within a replacement template.
_RE_BACKREF = re.compile(r"\\(\d+)")

# The regions of a replacement template that are not literal text. The raw alternative is listed
# first so that a `{% raw %}` block is matched whole instead of as a bare statement.
_RE_JINJA_SEGMENT = re.compile(
    r"({%-?\s*raw\s*-?%}.*?{%-?\s*endraw\s*-?%})"  # raw block
    r"|({{.*?}})"  # expression
    r"|({%.*?%})",  # statement
    re.DOTALL,
)


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


def _prepare_template(replace: str) -> str:
    r"""Rewrite the `re.sub` backreferences in a replacement template into Jinja references.

    Positional groups are reached through `_re_groups`, so how a backreference is rewritten
    depends on where it sits: inside a Jinja expression or statement it becomes a bare
    subscript, and in literal text it becomes an expression of its own. A `{% raw %}` block
    is emitted verbatim, so anything inside it stays literal.

    Args:
        replace: A Jinja-aware replacement template.

    Returns:
        str: The template with its backreferences rewritten, ready to render.
    """
    parts = []
    position = 0
    for segment in _RE_JINJA_SEGMENT.finditer(replace):
        parts.append(_RE_BACKREF.sub(r"{{ _re_groups[\1] }}", replace[position : segment.start()]))
        raw_block, expression, statement = segment.groups()
        if raw_block is not None:
            parts.append(raw_block)
        else:
            parts.append(_RE_BACKREF.sub(r"_re_groups[\1]", expression or statement))
        position = segment.end()
    parts.append(_RE_BACKREF.sub(r"{{ _re_groups[\1] }}", replace[position:]))
    return "".join(parts)


def sanitize_config_jinja(config: str, filters: t.Optional[t.List[t.Dict[str, t.Any]]] = None) -> str:
    r"""Like `sanitize_config`, but renders opted-in `replace` values as Jinja2 templates.

    This allows the replacement text to transform the matched data, e.g. hashing a secret
    with the `hash_data` filter instead of dropping it with a static placeholder. A filter
    opts in by setting `jinja` to `True`; every other filter is substituted with plain
    `re.sub`, so a mixed list of filters works as expected.

    The regex capture groups are exposed to the template so the original values can be
    transformed in place. References to capture groups follow the familiar `re.sub`
    backreference syntax (`\1`, `\2`, ...) and may be used both inside and outside a
    `{{ ... }}` expression. Named groups (`(?P<name>...)`) are additionally available by
    name, so a user-defined group name can never shadow a positional backreference.

    Jinja that should reach the sanitized configuration as literal text, such as a
    placeholder rendered later by a separate templating pass, must be wrapped in
    `{% raw %}...{% endraw %}`. The contents of a raw block, backreferences included, are
    passed through untouched.

    This function requires the optional `jinja2` dependency
    (`pip install netutils[optionals]`) when at least one filter opts in.

    Args:
        config: A string representation of a device configuration.
        filters: A list of dictionaries of regex patterns and replacement templates used to
            sanitize configuration, each optionally setting `jinja` to `True` to render its
            replacement as a Jinja template. Defaults to an empty list.

    Returns:
        str: Sanitized configuration.

    Examples:
        >>> from netutils.config.clean import sanitize_config_jinja
        >>> config = "username admin privilege 15 secret 9 SuperSecret"
        >>> SANITIZE_FILTERS = [
        ...     {
        ...         "regex": r"^(username \S+ privilege 15 secret 9 )(\S+)$",
        ...         "replace": r"\1{{ \2 | hash_data('md5') }}",
        ...         "jinja": True,
        ...     }
        ... ]
        >>> sanitize_config_jinja(config, SANITIZE_FILTERS)
        'username admin privilege 15 secret 9 2257151269b83ef0e139c3eec8bbcbcb'
    """
    if not filters:
        return config

    # Only the Jinja path needs jinja2; if no filter opts in, behave like sanitize_config.
    if not any(item.get("jinja", False) for item in filters):
        return sanitize_config(config, filters)

    if not HAS_JINJA2:
        raise ImportError(
            "The optional 'jinja2' dependency is required to use sanitize_config_jinja. "
            "Install it with `pip install netutils[optionals]` or `pip install jinja2`."
        )

    env = SandboxedEnvironment(autoescape=False)  # noqa: S701  # config text must not be HTML-escaped
    env.filters.update(jinja2_convenience_function())

    def _make_replacer(template_str: str) -> t.Callable[[t.Match[str]], str]:
        template = env.from_string(_prepare_template(template_str))

        def _replace(match: t.Match[str]) -> str:
            # Named groups are exposed by name; positional groups are reached via `_re_groups`,
            # indexed like a `re.Match` object (index 0 is the whole match, 1 is \1, and so on).
            context: t.Dict[str, t.Any] = dict(match.groupdict())
            context["_re_groups"] = (match.group(0), *match.groups())
            return template.render(**context)

        return _replace

    for item in filters:
        if item.get("jinja", False):
            config = re.sub(item["regex"], _make_replacer(item["replace"]), config, flags=re.MULTILINE)
        else:
            config = re.sub(item["regex"], item["replace"], config, flags=re.MULTILINE)
    return config
