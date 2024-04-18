"""Test for the lib_mapper definitions."""

import pytest

from netutils.protocol_mapper import (
    PROTO_NAME_TO_NUM,
    PROTO_NUM_TO_NAME,
    TCP_NAME_TO_NUM,
    TCP_NUM_TO_NAME,
    UDP_NAME_TO_NUM,
    UDP_NUM_TO_NAME,
    SCTP_NAME_TO_NUM,
    SCTP_NUM_TO_NAME,
    DCCP_NAME_TO_NUM,
    DCCP_NUM_TO_NAME,
)


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


def test_tcp_name_to_num():
    """Simple test of TCP protocol to number mapper."""
    assert TCP_NAME_TO_NUM["SSH"] == 22


def test_tcp_to_num_name():
    """Simple test of TCP protocol to name mapper."""
    assert TCP_NUM_TO_NAME[22] == "SSH"


def test_udp_name_to_num():
    """Simple test of UDP protocol to number mapper."""
    assert UDP_NAME_TO_NUM["SSH"] == 22


def test_udp_to_num_name():
    """Simple test of UDP protocol to name mapper."""
    assert UDP_NUM_TO_NAME[22] == "SSH"


def test_sctp_name_to_num():
    """Simple test of UDP protocol to number mapper."""
    assert SCTP_NAME_TO_NUM["SSH"] == 22


def test_sctp_to_num_name():
    """Simple test of UDP protocol to name mapper."""
    assert SCTP_NUM_TO_NAME[22] == "SSH"


def test_dccp_name_to_num():
    """Simple test of DCCP protocol to number mapper."""
    assert DCCP_NAME_TO_NUM["DISCARD"] == 9


def test_dccp_to_num_name():
    """Simple test of DCCP protocol to name mapper."""
    assert DCCP_NUM_TO_NAME[9] == "DISCARD"
