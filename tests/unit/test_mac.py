"""Test for the MAC address functions."""
import pytest

from netutils import mac

IS_VALID_MAC = [
    # MAC_COLON_TWO
    {
        "sent": {"mac": "aa:bb:cc:11:22:33"},
        "received": True,
    },
    # MAC_COLON_FOUR
    {
        "sent": {"mac": "aabb:cc11:2233"},
        "received": True,
    },
    # MAC_DASH_TWO
    {
        "sent": {"mac": "aa-bb-cc-11-22-33"},
        "received": True,
    },
    # MAC_DASH_FOUR
    {
        "sent": {"mac": "aabb-cc11-2233"},
        "received": True,
    },
    # MAC_DOT_TWO
    {
        "sent": {"mac": "aa.bb.cc.11.22.33"},
        "received": True,
    },
    # MAC_DOT_FOUR
    {
        "sent": {"mac": "aabb.cc11.2233"},
        "received": True,
    },
    # MAC_NO_SPECIAL
    {
        "sent": {"mac": "aabbcc112233"},
        "received": True,
    },
    # NOT ENOUGH CHARS
    {
        "sent": {"mac": "aabbcc11223"},
        "received": False,
    },
    # INVALID CHARACTERS
    {
        "sent": {"mac": "aabbcc11223g"},
        "received": False,
    },
    # INVALID UNDERSCORE
    {
        "sent": {"mac": "aa_bb_cc_11_22_33"},
        "received": False,
    },
]

MAC_FORMAT = [
    {
        "received": "aa:bb:cc:11:22:33",
        "format": "MAC_COLON_TWO",
        "sent": "aabbcc112233",
    },
    {
        "received": "aabb:cc11:2233",
        "format": "MAC_COLON_FOUR",
        "sent": "aabbcc112233",
    },
    {
        "received": "aa-bb-cc-11-22-33",
        "format": "MAC_DASH_TWO",
        "sent": "aabbcc112233",
    },
    {
        "received": "aabb-cc11-2233",
        "format": "MAC_DASH_FOUR",
        "sent": "aabbcc112233",
    },
    {
        "received": "aa.bb.cc.11.22.33",
        "format": "MAC_DOT_TWO",
        "sent": "aabbcc112233",
    },
    {
        "received": "aabb.cc11.2233",
        "format": "MAC_DOT_FOUR",
        "sent": "aabbcc112233",
    },
    {
        "received": "aabbcc112233",
        "format": "MAC_NO_SPECIAL",
        "sent": "aabbcc112233",
    },
]

MAC_TYPE = [
    {
        "sent": {"mac": "aa:bb:cc:11:22:33"},
        "received": "MAC_COLON_TWO",
    },
    {
        "sent": {"mac": "aabb:cc11:2233"},
        "received": "MAC_COLON_FOUR",
    },
    {
        "sent": {"mac": "aa-bb-cc-11-22-33"},
        "received": "MAC_DASH_TWO",
    },
    {
        "sent": {"mac": "aabb-cc11-2233"},
        "received": "MAC_DASH_FOUR",
    },
    {
        "sent": {"mac": "aa.bb.cc.11.22.33"},
        "received": "MAC_DOT_TWO",
    },
    {
        "sent": {"mac": "aabb.cc11.2233"},
        "received": "MAC_DOT_FOUR",
    },
    {
        "sent": {"mac": "aabbcc112233"},
        "received": "MAC_NO_SPECIAL",
    },
]

MAC_NORMALIZE = [
    {
        "sent": {"mac": "aa:bb:cc:11:22:33"},
        "received": "aabbcc112233",
    },
    {
        "sent": {"mac": "aa-bb-cc-11-22-33"},
        "received": "aabbcc112233",
    },
    {
        "sent": {"mac": "aa.bb.cc.11.22.33"},
        "received": "aabbcc112233",
    },
    {
        "sent": {"mac": "aabbcc112233"},
        "received": "aabbcc112233",
    },
]

MAC_TO_INT = [
    {
        "sent": {"mac": "aa:bb:cc:11:22:33"},
        "received": 187723559281203,
    },
    {
        "sent": {"mac": "ffffffffffff"},
        "received": 281474976710655,
    },
    {
        "sent": {"mac": "000000000000"},
        "received": 0,
    },
]

OUI = [
    {"sent": {"mac": "64.b2.1d.aa.bb.cc"}, "received": "Chengdu Phycom Tech Co., Ltd."},
    {"sent": {"mac": "68.db.f5.ff.32.44"}, "received": "Amazon Technologies Inc."},
    {"sent": {"mac": "98e8facc87af"}, "received": "Nintendo Co.,Ltd"},
    {"sent": {"mac": "4c:24:98:68:77:ff"}, "received": "Texas Instruments"},
    {"sent": {"mac": "c8-aa-cc-33-54-67"}, "received": "Private"},
]


@pytest.mark.parametrize("data", IS_VALID_MAC)
def test_is_valid_mac(data):
    assert mac.is_valid_mac(**data["sent"]) == data["received"]


@pytest.mark.parametrize("data", MAC_TYPE)
def test_mac_type(data):
    assert mac.mac_type(**data["sent"]) == data["received"]


@pytest.mark.parametrize("data", MAC_NORMALIZE)
def test_mac_normalize(data):
    assert mac.mac_normalize(**data["sent"]) == data["received"]


@pytest.mark.parametrize("data", MAC_FORMAT)
def test_mac_to_format(data):
    assert mac.mac_to_format(data["sent"], data["format"]) == data["received"]


@pytest.mark.parametrize("data", MAC_TO_INT)
def test_mac_to_int(data):
    assert mac.mac_to_int(**data["sent"]) == data["received"]


def test_to_list_failure():
    with pytest.raises(ValueError, match=r"There was not a valid mac address in"):
        mac.mac_to_int("aa.bb.cc.dd.ee.gg")


def test_to_format_failure():
    with pytest.raises(ValueError, match=r"An invalid mac format was provided in"):
        mac.mac_to_format("aa.bb.cc.dd.ee.ff", "NON_FORMAT")


@pytest.mark.parametrize("data", OUI)
def test_get_oui(data):
    assert mac.get_oui(**data["sent"]) == data["received"]


def test_get_oui_failure():
    with pytest.raises(ValueError, match=r"There was no matching entry in OUI_MAPPINGS for ffffff"):
        mac.get_oui("ff-ff-ff-aa-56-67")
