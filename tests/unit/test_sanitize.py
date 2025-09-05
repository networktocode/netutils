"""Test for the network os sanitize functions."""

import glob
import os

import pytest

from netutils.config import compliance
from netutils.config.conversion import paloalto_panos_clean_newlines

MOCK_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "mock", "config", "sanitize")

TXT_FILE = "_sent.txt"
SANITIZE_FILE = "_sanitized.txt"

sanitize_files = []

for network_os in list(compliance.parser_map.keys()):
    for _file in glob.glob(f"{MOCK_DIR}/{network_os}/*{TXT_FILE}"):
        sanitize_files.append([_file, network_os])


@pytest.mark.parametrize("_file", sanitize_files)
def test_panos_newline_character(_file, get_text_data):
    truncate_file = os.path.join(MOCK_DIR, _file[0][: -len(TXT_FILE)])

    sent_cfg = get_text_data(os.path.join(MOCK_DIR, _file[0]))
    sanitized_cfg = paloalto_panos_clean_newlines(cfg=sent_cfg)
    received_data = get_text_data(truncate_file + "_sanitized.txt")
    assert sanitized_cfg == received_data
