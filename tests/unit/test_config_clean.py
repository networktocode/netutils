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
