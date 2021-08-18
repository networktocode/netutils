"""Test for the port_mapper definitions."""
from pytest import raises

from netutils.port_mapper import PORT_NAME_TO_NUM, PORT_NUM_TO_NAME, PORT_NAME_TO_PROTO_NAME


def test_port_name_to_num_success():
    """Simple test of protocol to number mapper."""
    assert PORT_NAME_TO_NUM["SSH"] == 22


def test_name_not_exist_name_to_num_fail():
    """Test not existed key raises error."""
    with raises(KeyError):
        PORT_NAME_TO_NUM["TEST"]  # pylint: disable=pointless-statement


def test_port_num_to_name_success():
    """Simple test of port number to name mapper."""
    assert PORT_NUM_TO_NAME[161] == "SNMP"


def test_name_not_exist_num_to_name_fail():
    """Test not existed key raises error."""
    with raises(KeyError):
        PORT_NUM_TO_NAME[999]  # pylint: disable=pointless-statement


def test_port_name_to_proto_name_success():
    """Simple test of port name to protocol name mapper."""
    assert PORT_NAME_TO_PROTO_NAME["ISAKMP"] == "udp"
    assert PORT_NAME_TO_PROTO_NAME["KERBEROS"] == "tcp-udp"
    assert PORT_NAME_TO_PROTO_NAME["SSH"] == "tcp"


def test_port_name_to_proto_name_fail():
    """Test not existed key raises error."""
    with raises(KeyError):
        PORT_NAME_TO_PROTO_NAME["TEST"]  # pylint: disable=pointless-statement

        
