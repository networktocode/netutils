"""Test for the banner functions."""

import pytest
from netutils import banner


BANNER_CARET_C = "banner login ^C\n******************\n    TEST BANNER\n******************^C"

banner_config_and_delimiter = [
    {
        "sent": ["banner login ^\n******************\n    TEST BANNER\n******************^", "^", "^C"],
        "received": BANNER_CARET_C,
    },
    {
        "sent": ["banner login ^\n******************\n    TEST BANNER\n******************\n^", "^", "^C"],
        "received": "banner login ^C\n******************\n    TEST BANNER\n******************\n^C",
    },
    {
        "sent": ["banner login ^C\n******************\n    TEST BANNER\n******************^C", "^C", "^C"],
        "received": BANNER_CARET_C,
    },
    {
        "sent": ["banner login ^C\n******************\n    TEST BANNER\n******************\n^C", "^C", "^C"],
        "received": "banner login ^C\n******************\n    TEST BANNER\n******************\n^C",
    },
    {
        "sent": ["banner login \x03\n******************\n    TEST BANNER\n******************\x03", "\x03", "^C"],
        "received": BANNER_CARET_C,
    },
    {
        "sent": ["banner login ^CCCCC\n******************\n    TEST BANNER\n******************^C", "^C", "^C"],
        "received": BANNER_CARET_C,
    },
    {
        "sent": ["banner login ^C\n******************\n    TEST BANNER\n******************^C", "^C", "^"],
        "received": "banner login ^\n******************\n    TEST BANNER\n******************^",
    },
    {
        "sent": ["banner login ^C\n******************\n    TEST BANNER\n******************^C", "^C", "\x03"],
        "received": "banner login \x03\n******************\n    TEST BANNER\n******************\x03",
    },
    {
        "sent": ["banner login #\n******************\n    TEST BANNER\n******************#", "#", "^C"],
        "received": BANNER_CARET_C,
    },
    {
        "sent": ["banner login $\n******************\n    TEST BANNER\n******************\n$", "$", "^C"],
        "received": "banner login ^C\n******************\n    TEST BANNER\n******************\n^C",        
    },
]

banner_config = [
    {"sent": ["^", "banner login ^\n******************\n    TEST BANNER\n******************^"], "received": BANNER_CARET_C},
    {"sent": ["^C", "banner login ^C\n******************\n    TEST BANNER\n******************^C"], "received": BANNER_CARET_C},
    {
        "sent": ["\x03", "banner login \x03\n******************\n    TEST BANNER\n******************\x03"],
        "received": BANNER_CARET_C,
    },
    {
        "sent": ["^C", "banner login ^CCCCC\n******************\n    TEST BANNER\n******************^C"],
        "received": BANNER_CARET_C,
    },
    {"sent": ["#", "banner login #\n******************\n    TEST BANNER\n******************#"], "received": BANNER_CARET_C},
    {"sent": ["Z", "banner login Z\n******************\n    TEST BANNER\n******************Z"], "received": BANNER_CARET_C},
]


@pytest.mark.parametrize("data", banner_config_and_delimiter)
def test_banner_delimitier_change(data):
    assert banner.delimiter_change(*data["sent"]) == data["received"]


@pytest.mark.parametrize("data", banner_config)
def test_banner_normalise_delimiter_caret_c(data):
    assert banner.normalise_delimiter_caret_c(*data["sent"]) == data["received"]
