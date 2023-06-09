"""Test for the Hostname based functions."""

from netutils import hostname


def test_truthy_happy_path_case():
    match = hostname.hostname_regex("USSCAMS07", ".+SC.+\d\d")
    assert bool(match) is True


def test_truthy_sad_path_case():
    match = hostname.hostname_regex("USSCAMS07", "foobar")
    assert bool(match) is False


def test_capture_group_happy_path_case():
    match = hostname.hostname_regex("USSCAMS07", "([A-Z]{2})([A-Z]{2})([A-Z]{3})(\d*)")
    assert match[1] == "US"


def test_capture_group_sad_path_case():
    match = hostname.hostname_regex("USSCAMS07", "(foobar)")
    assert match is None
