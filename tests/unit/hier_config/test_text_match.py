from netutils.hier_config import text_match


text = "  ip address 192.168.100.1/24"
expression1 = text
expression2 = "  ip address"
expression3 = "ip access-list"
expression4 = "/30"


def test_equals():
    assert text_match.equals(text, expression1)
    assert not text_match.equals(text, expression2)


def test_startswith():
    assert text_match.startswith(text, expression2)
    assert not text_match.startswith(text, expression3)


def test_endswith():
    assert text_match.endswith(text, expression1)
    assert not text_match.endswith(text, expression4)


def test_contains():
    assert text_match.contains(text, expression2)
    assert not text_match.contains(text, expression3)


def test_re_search():
    assert text_match.re_search(text, expression2)
    assert not text_match.re_search(text, expression3)


def test_anything():
    assert text_match.anything(text, expression1)
    assert text_match.anything(text, expression2)


def test_nothing():
    assert not text_match.nothing(text, expression1)
    assert not text_match.nothing(text, expression2)
    assert not text_match.nothing(text, expression3)
    assert not text_match.nothing(text, expression4)
