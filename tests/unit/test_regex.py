"""Test for the regex based functions."""

from netutils import regex


def test_regex_findall_bool_true():
    match = regex.regex_findall(r"CAMS\d\d", "USSCAMS07")
    assert bool(match) is True


def test_regex_findall_bool_false():
    match = regex.regex_findall("foobar", "USSCAMS07")
    assert bool(match) is False


def test_regex_findall_list():
    match = regex.regex_findall(r"\w\w\w-RT\d\d", "NYC-RT01,NYC-RT02,SFO-SW01,SFO-RT01")
    assert match[0] == "NYC-RT01"
    assert match[1] == "NYC-RT02"


def test_regex_findall_is_none():
    match = regex.regex_findall("(foobar)", "USSCAMS07")
    assert match == []


def test_regex_match_bool_true():
    match = regex.regex_match(r".+SC.+\d\d", "USSCAMS07")
    assert bool(match) is True


def test_regex_match_bool_false():
    match = regex.regex_match("foobar", "USSCAMS07")
    assert bool(match) is False


def test_regex_match_list():
    match = regex.regex_match(r"([A-Z]{2})([A-Z]{2})([A-Z]{3})(\d*)", "USSCAMS07")
    assert match[0] == "US"
    assert match[1] == "SC"
    match = regex.regex_match(r"[A-Z]{2}[A-Z]{2}[A-Z]{3}\d*", "USSCAMS07")
    assert match == "USSCAMS07"


def test_regex_match_is_none():
    match = regex.regex_match("(foobar)", "USSCAMS07")
    assert match is None


def test_regex_search_bool_true():
    match = regex.regex_search(r"CAMS\d\d", "USSCAMS07")
    assert bool(match) is True


def test_regex_search_bool_false():
    match = regex.regex_search("foobar", "USSCAMS07")
    assert bool(match) is False


def test_regex_search_list():
    match = regex.regex_search(r"([A-Z]{2})([A-Z]{2})([A-Z]{3})(\d*)", "USSCAMS07")
    assert match[0] == "US"
    assert match[1] == "SC"
    match = regex.regex_search(r"[A-Z]{2}[A-Z]{2}[A-Z]{3}\d*", "USSCAMS07")
    assert match == "USSCAMS07"


def test_regex_search_is_none():
    match = regex.regex_search("(foobar)", "USSCAMS07")
    assert match is None


def test_regex_split_list():
    match = regex.regex_split(",", "NYC-RT01,NYC-RT02,SFO-SW01,SFO-RT01")
    assert match[0] == "NYC-RT01"
    assert match[1] == "NYC-RT02"
    match = regex.regex_split("(.)", "NYC-RT01,NYC-RT02,SFO-SW01,SFO-RT01")
    assert match[1] == "N"
    match = regex.regex_split(",", "NYC-RT01,NYC-RT02,SFO-SW01,SFO-RT01", 1)
    assert match[0] == "NYC-RT01"
    assert match[1] == "NYC-RT02,SFO-SW01,SFO-RT01"


def test_regex_split_no_match():
    match = regex.regex_split(r"(\.)", "NYC-RT01,NYC-RT02,SFO-SW01,SFO-RT01")
    assert match == ["NYC-RT01,NYC-RT02,SFO-SW01,SFO-RT01"]


def test_regex_sub_list():
    match = regex.regex_sub(",", " ", "NYC-RT01,NYC-RT02,SFO-SW01,SFO-RT01")
    assert match == "NYC-RT01 NYC-RT02 SFO-SW01 SFO-RT01"
    match = regex.regex_sub("(ROUTER|RTR)", "RT", "NYC-ROUTER01,NYC-ROUTER02,NYC-RTR03")
    assert match == "NYC-RT01,NYC-RT02,NYC-RT03"


def test_regex_sub_no_match():
    match = regex.regex_sub("ABBA", "CADABBA", "NYC-RT01,NYC-RT02,SFO-SW01,SFO-RT01")
    assert match == "NYC-RT01,NYC-RT02,SFO-SW01,SFO-RT01"
