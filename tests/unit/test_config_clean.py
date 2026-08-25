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


def test_sanitize_config_jinja_hashes_capture_group():
    config = "username foo privilege 15 secret 9 bar"
    filters = [
        {
            "regex": r"^username (\S+) privilege 15 secret 9 (\S+)$",
            "replace": r"username {{ \1 | hash_data('md5') }} privilege 15 secret 9 {{ \2 | hash_data('md5') }}",
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
        },
    ]
    assert (
        clean.sanitize_config_jinja(config, filters)
        == f"enable secret 5 <removed>\nusername foo privilege 15 secret 9 {MD5_BAR}"
    )


def test_sanitize_config_jinja_no_jinja_matches_sanitize_config():
    # With no Jinja in any replace, the result matches plain sanitize_config.
    config = "enable secret 5 supersecret"
    filters = [{"regex": r"^(enable secret 5 ).+$", "replace": r"\1<removed>"}]
    assert clean.sanitize_config_jinja(config, filters) == clean.sanitize_config(config, filters)


def test_sanitize_config_jinja_empty_filters():
    config = "username foo privilege 15 secret 9 bar"
    assert clean.sanitize_config_jinja(config, None) == config
    assert clean.sanitize_config_jinja(config, []) == config
