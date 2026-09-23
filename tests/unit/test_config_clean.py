"""Test for the config cleaning functions."""

import glob
import os

import pytest

from netutils.config import clean
from netutils.constants import _PROVIDED_CLEAN_FILTERS, _PROVIDED_SANITIZE_FILTERS

MOCK_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "mock", "config")
TXT_FILE = "_sent.txt"


@pytest.mark.parametrize("_file", glob.glob(f"{MOCK_DIR}/clean/*{TXT_FILE}"))
def test_clean_config(_file, get_text_data):
    truncate_file = os.path.join(MOCK_DIR, _file[: -len(TXT_FILE)])

    sent_data = get_text_data(os.path.join(MOCK_DIR, _file))
    received_data = get_text_data(truncate_file + "_received.txt")
    assert clean.clean_config(sent_data, filters=_PROVIDED_CLEAN_FILTERS) == received_data


@pytest.mark.parametrize("_file", glob.glob(f"{MOCK_DIR}/sanitize/*{TXT_FILE}"))
def test_sanitize_config(_file, get_text_data):
    truncate_file = os.path.join(MOCK_DIR, _file[: -len(TXT_FILE)])

    sent_data = get_text_data(os.path.join(MOCK_DIR, _file))
    received_data = get_text_data(truncate_file + "_received.txt")
    assert clean.sanitize_config(sent_data, filters=_PROVIDED_SANITIZE_FILTERS) == received_data


# md5 hashes of the cleartext secrets used in the tests below.
MD5_FOO = "acbd18db4cc2f85cedef654fccc4a4d8"
MD5_BAR = "37b51d194a7513e45b56f6524f2d51f2"


# A Golden Config postprocessing placeholder: the backup must carry this through verbatim so it
# matches the intended config, which holds the same literal string for `render_secrets` to fill in.
POSTPROCESSING_REPLACE = r'\1{{ secrets_group["name"] | get_secret_by_secret_group_name("password") }}'
POSTPROCESSING_REGEX = r"^(username \S+ password 7 )\S+$"
POSTPROCESSING_CONFIG = "username foo password 7 bar"
POSTPROCESSING_EXPECTED = (
    'username foo password 7 {{ secrets_group["name"] | get_secret_by_secret_group_name("password") }}'
)


def test_sanitize_config_jinja_hashes_capture_group():
    config = "username foo privilege 15 secret 9 bar"
    filters = [
        {
            "regex": r"^username (\S+) privilege 15 secret 9 (\S+)$",
            "replace": r"username {{ \1 | hash_data('md5') }} privilege 15 secret 9 {{ \2 | hash_data('md5') }}",
            "render_jinja": True,
        }
    ]
    assert clean.sanitize_config_jinja(config, filters) == f"username {MD5_FOO} privilege 15 secret 9 {MD5_BAR}"


def test_sanitize_config_jinja_carries_static_group_through():
    # Compact-template technique: capture middle static text into a group and re-emit it unchanged.
    config = "username foo privilege 15 secret 9 bar"
    filters = [
        {
            "regex": r"^username (\S+) (.+) secret 9 (\S+)$",
            "replace": r"username {{ \1 | hash_data('md5') }} {{ \2 }} secret 9 {{ \3 | hash_data('md5') }}",
            "render_jinja": True,
        }
    ]
    assert clean.sanitize_config_jinja(config, filters) == f"username {MD5_FOO} privilege 15 secret 9 {MD5_BAR}"


def test_sanitize_config_jinja_named_group():
    # A named group can be referenced by name and mixed with a positional backreference.
    config = "username foo privilege 15 secret 9 bar"
    filters = [
        {
            "regex": r"^username (?P<user>\S+) privilege 15 secret 9 (\S+)$",
            "replace": r"username {{ user }} privilege 15 secret 9 {{ \2 | hash_data('md5') }}",
            "render_jinja": True,
        }
    ]
    assert clean.sanitize_config_jinja(config, filters) == f"username foo privilege 15 secret 9 {MD5_BAR}"


def test_sanitize_config_jinja_named_group_piped_through_hash_data():
    # A named group can itself be piped through a filter such as hash_data.
    config = "username foo privilege 15 secret 9 bar"
    filters = [
        {
            "regex": r"^username (?P<user>\S+) privilege 15 secret 9 (?P<secret>\S+)$",
            "replace": r"username {{ user | hash_data('md5') }} privilege 15 secret 9 {{ secret | hash_data('md5') }}",
            "render_jinja": True,
        }
    ]
    assert clean.sanitize_config_jinja(config, filters) == f"username {MD5_FOO} privilege 15 secret 9 {MD5_BAR}"


def test_sanitize_config_jinja_mixed_filters():
    # A list mixing a plain (non-Jinja) replace and a Jinja replace.
    config = "enable secret 5 supersecret\nusername foo privilege 15 secret 9 bar"
    filters = [
        {"regex": r"^(enable secret 5 ).+$", "replace": r"\1<removed>"},
        {
            "regex": r"^username (\S+) privilege 15 secret 9 (\S+)$",
            "replace": r"username {{ \1 }} privilege 15 secret 9 {{ \2 | hash_data('md5') }}",
            "render_jinja": True,
        },
    ]
    assert (
        clean.sanitize_config_jinja(config, filters)
        == f"enable secret 5 <removed>\nusername foo privilege 15 secret 9 {MD5_BAR}"
    )


def test_sanitize_config_jinja_no_jinja_matches_sanitize_config():
    # With no filter opting in, the result matches plain sanitize_config.
    config = "enable secret 5 supersecret"
    filters = [{"regex": r"^(enable secret 5 ).+$", "replace": r"\1<removed>"}]
    assert clean.sanitize_config_jinja(config, filters) == clean.sanitize_config(config, filters)


def test_sanitize_config_jinja_empty_filters():
    config = "username foo privilege 15 secret 9 bar"
    assert clean.sanitize_config_jinja(config, None) == config
    assert clean.sanitize_config_jinja(config, []) == config


def test_sanitize_config_jinja_unflagged_jinja_is_not_rendered():
    # Without the `render_jinja` key, a replace containing Jinja is substituted literally. Rendering
    # would raise, since `get_secret_by_secret_group_name` is not a netutils filter.
    filters = [{"regex": POSTPROCESSING_REGEX, "replace": POSTPROCESSING_REPLACE}]
    assert clean.sanitize_config_jinja(POSTPROCESSING_CONFIG, filters) == POSTPROCESSING_EXPECTED


def test_sanitize_config_jinja_explicitly_disabled_is_not_rendered():
    filters = [{"regex": POSTPROCESSING_REGEX, "replace": POSTPROCESSING_REPLACE, "render_jinja": False}]
    assert clean.sanitize_config_jinja(POSTPROCESSING_CONFIG, filters) == POSTPROCESSING_EXPECTED


def test_sanitize_config_jinja_unflagged_jinja_alongside_flagged_filter():
    # One filter opting in does not drag an unflagged postprocessing placeholder into the renderer.
    config = f"{POSTPROCESSING_CONFIG}\nenable secret 9 foo"
    filters = [
        {"regex": POSTPROCESSING_REGEX, "replace": POSTPROCESSING_REPLACE},
        {"regex": r"^(enable secret 9 )(\S+)$", "replace": r"\1{{ \2 | hash_data('md5') }}", "render_jinja": True},
    ]
    assert clean.sanitize_config_jinja(config, filters) == f"{POSTPROCESSING_EXPECTED}\nenable secret 9 {MD5_FOO}"


def test_sanitize_config_jinja_filters_are_applied_in_order():
    config = "secret foo"
    filters = [
        {"regex": r"^secret (\S+)$", "replace": r"secret {{ \1 | hash_data('md5') }}", "render_jinja": True},
        {"regex": f"^secret {MD5_FOO}$", "replace": "secret <removed>"},
    ]
    assert clean.sanitize_config_jinja(config, filters) == "secret <removed>"


def test_sanitize_config_jinja_requires_jinja2_when_a_filter_opts_in(monkeypatch):
    monkeypatch.setattr(clean, "HAS_JINJA2", False)
    filters = [{"regex": r"^(enable secret 9 )(\S+)$", "replace": r"\1{{ \2 }}", "render_jinja": True}]
    with pytest.raises(ImportError, match="jinja2"):
        clean.sanitize_config_jinja("enable secret 9 foo", filters)


def test_sanitize_config_jinja_does_not_require_jinja2_when_no_filter_opts_in(monkeypatch):
    monkeypatch.setattr(clean, "HAS_JINJA2", False)
    filters = [{"regex": r"^(enable secret 5 ).+$", "replace": r"\1<removed>"}]
    assert clean.sanitize_config_jinja("enable secret 5 supersecret", filters) == "enable secret 5 <removed>"


def test_sanitize_config_jinja_backreference_outside_expression():
    config = "username foo privilege 15 secret 9 bar"
    filters = [
        {
            "regex": r"^(username \S+ privilege 15 secret 9 )(\S+)$",
            "replace": r"\1{{ \2 | hash_data('md5') }}",
            "render_jinja": True,
        }
    ]
    assert clean.sanitize_config_jinja(config, filters) == f"username foo privilege 15 secret 9 {MD5_BAR}"


def test_sanitize_config_jinja_backreference_without_any_expression():
    # An opted-in filter whose replace holds no Jinja at all still resolves its backreferences.
    config = "enable secret 5 supersecret"
    filters = [{"regex": r"^(enable secret 5 ).+$", "replace": r"\1<removed>", "render_jinja": True}]
    assert clean.sanitize_config_jinja(config, filters) == "enable secret 5 <removed>"


def test_sanitize_config_jinja_whole_match_backreference():
    config = "enable secret 5 supersecret"
    filters = [{"regex": r"^enable secret 5 .+$", "replace": r"! \0", "render_jinja": True}]
    assert clean.sanitize_config_jinja(config, filters) == "! enable secret 5 supersecret"


def test_sanitize_config_jinja_two_digit_backreference():
    config = "a b c d e f g h i j"
    filters = [
        {
            "regex": r"^" + r" ".join(r"(\S+)" for _ in range(10)) + r"$",
            "replace": r"\10 \1",
            "render_jinja": True,
        }
    ]
    assert clean.sanitize_config_jinja(config, filters) == "j a"


def test_sanitize_config_jinja_raw_block_passes_jinja_through():
    # The opt-in escape hatch: wrap postprocessing Jinja in `{% raw %}` so it survives rendering.
    raw_replace = r'\1{% raw %}{{ secrets_group["name"] | get_secret_by_secret_group_name("password") }}{% endraw %}'
    filters = [{"regex": POSTPROCESSING_REGEX, "replace": raw_replace, "render_jinja": True}]
    assert clean.sanitize_config_jinja(POSTPROCESSING_CONFIG, filters) == POSTPROCESSING_EXPECTED


def test_sanitize_config_jinja_raw_block_with_whitespace_control():
    raw_replace = r"\1{%- raw -%}{{ secret }}{%- endraw -%}"
    filters = [{"regex": POSTPROCESSING_REGEX, "replace": raw_replace, "render_jinja": True}]
    assert clean.sanitize_config_jinja(POSTPROCESSING_CONFIG, filters) == "username foo password 7 {{ secret }}"


def test_sanitize_config_jinja_backreference_inside_raw_block_stays_literal():
    filters = [{"regex": POSTPROCESSING_REGEX, "replace": r"{% raw %}\1{% endraw %}", "render_jinja": True}]
    assert clean.sanitize_config_jinja(POSTPROCESSING_CONFIG, filters) == r"\1"


def test_sanitize_config_jinja_backreference_inside_statement_block():
    config = "enable secret 5 supersecret\nenable secret 5 "
    filters = [
        {
            "regex": r"^(enable secret 5 )(.*)$",
            "replace": r"\1{% if \2 %}<removed>{% else %}<empty>{% endif %}",
            "render_jinja": True,
        }
    ]
    assert clean.sanitize_config_jinja(config, filters) == "enable secret 5 <removed>\nenable secret 5 <empty>"


def test_sanitize_config_jinja_captured_value_is_not_treated_as_jinja():
    # Device output that happens to look like Jinja must not be rendered as part of the template.
    config = "banner motd {{ 7 * 7 }}"
    filters = [{"regex": r"^(banner motd )(.+)$", "replace": r"\1\2", "render_jinja": True}]
    assert clean.sanitize_config_jinja(config, filters) == config
