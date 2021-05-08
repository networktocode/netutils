"""Test for the lib_mapper definitions."""
import pytest

from netutils.protocol_mapper import PROTO_NAME_TO_NUM, PROTO_NUM_TO_NAME


def test_proto_name_to_num():
    """Simple test of protocol to number mapper."""
    assert PROTO_NAME_TO_NUM["ICMP"] == 1


def test_name_not_exist_name_to_num():
    """Test not existed key raises error."""
    with pytest.raises(KeyError):
        PROTO_NAME_TO_NUM["TEST"]  # pylint: disable=pointless-statement


def test_proto_num_to_name():
    """Simple test of protocol number to name mappper."""
    assert PROTO_NUM_TO_NAME[1] == "ICMP"


def test_name_not_exist_num_to_nam():
    """Test not existed key raises error."""
    with pytest.raises(KeyError):
        PROTO_NUM_TO_NAME[257]  # pylint: disable=pointless-statement
