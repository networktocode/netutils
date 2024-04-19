"""Protocol Mappers."""

import typing as t

from netutils.constants import PROTOCOLS
from netutils.data_files.protocol_number_mappings import (  # noqa: F401 # pylint:disable=unused-import
    PROTO_NAME_TO_NUM,
    PROTO_NUM_TO_NAME,
)


def _number_to_name_mapper(proto: str) -> t.Dict[int, str]:
    """Create a dictionary that maps protocol port number to a name.

    Args:
        proto: Protocol to map ['tcp', 'udp', 'sctp', 'dccp']

    Returns:
        Dictionary of the number to name mapping.
    """
    proto_num_to_name = {}

    for key, value in PROTOCOLS.items():
        if proto.lower() in value["protocols"]:
            proto_num_to_name[value["port_number"]] = key.upper()

    return proto_num_to_name


# https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml
# TCP port to name mapping.
TCP_NUM_TO_NAME = _number_to_name_mapper("tcp")

# TCP port name to number mapping
TCP_NAME_TO_NUM = {value: key for (key, value) in TCP_NUM_TO_NAME.items()}

# UDP port to name mapping.
UDP_NUM_TO_NAME = _number_to_name_mapper("udp")

# UDP port name to number mapping
UDP_NAME_TO_NUM = {value: key for (key, value) in UDP_NUM_TO_NAME.items()}

# SCTP port to name mapping.
SCTP_NUM_TO_NAME = _number_to_name_mapper("sctp")

# SCTP port name to number mapping
SCTP_NAME_TO_NUM = {value: key for (key, value) in SCTP_NUM_TO_NAME.items()}

# DCCP port to name mapping.
DCCP_NUM_TO_NAME = _number_to_name_mapper("dccp")

# DCCP port name to number mapping
DCCP_NAME_TO_NUM = {value: key for (key, value) in DCCP_NUM_TO_NAME.items()}
