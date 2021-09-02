"""Protocol Mappers."""
from netutils.constants import PROTOCOLS


def _number_to_name_mapper(proto: str) -> dict:
    """Create a dictionary that maps protocol port number to a name.

    Args:
        proto: Protocol to map ['tcp', 'udp', 'sctp', 'dccp']

    Returns:
        proto_num_to_name: Dictionary of the number to name mapping.
    """
    proto_num_to_name = {}

    for item in PROTOCOLS:
        if proto.lower() in PROTOCOLS[item]["protocols"]:
            proto_num_to_name[PROTOCOLS[item]["port_number"]] = item.upper()

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

"""Mappers used to take protocol number-->name and vice-versa.  Number needed for test command, name needed for test command if querying by application-id."""

# Protocol mapping based on https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml.
PROTO_NAME_TO_NUM = {
    "ICMP": 1,
    "IGMP": 2,
    "GGP": 3,
    "TCP": 6,
    "CBT": 7,
    "EGP": 8,
    "IGP": 9,
    "BBN-RCC-MON": 10,
    "NVP-II": 11,
    "PUP": 12,
    "EMCON": 14,
    "XNET": 15,
    "CHAOS": 16,
    "UDP": 17,
    "MUX": 18,
    "DCN-MEAS": 19,
    "HMP": 20,
    "PRM": 21,
    "XNS-IDP": 22,
    "TRUNK-1": 23,
    "TRUNK-2": 24,
    "LEAF-1": 25,
    "LEAF-2": 26,
    "RDP": 27,
    "IRTP": 28,
    "ISO-TP4": 29,
    "NETBLT": 30,
    "MFE-NSP": 31,
    "MERIT-INP": 32,
    "DCCP": 33,
    "3PC": 34,
    "IDPR": 35,
    "XTP": 36,
    "DDP": 37,
    "IDPR-CMTP": 38,
    "TP++": 39,
    "IL": 40,
    "SDRP": 42,
    "IDRP": 45,
    "RSVP": 46,
    "GRE": 47,
    "DSR": 48,
    "BNA": 49,
    "ESP": 50,
    "AH": 51,
    "I-NLSP": 52,
    "NARP": 54,
    "MOBILE": 55,
    "TLSP": 56,
    "SKIP": 57,
    "CFTP": 62,
    "SAT-EXPAK": 64,
    "KRYPTOLAN": 65,
    "RVD": 66,
    "IPPC": 67,
    "SAT-MON": 69,
    "VISA": 70,
    "IPCV": 71,
    "CPNX": 72,
    "CPHB": 73,
    "WSN": 74,
    "PVP": 75,
    "BR-SAT-MON": 76,
    "SUN-ND": 77,
    "WB-MON": 78,
    "WB-EXPAK": 79,
    "ISO-IP": 80,
    "VMTP": 81,
    "SECURE-VMTP": 82,
    "VINES": 83,
    "TTP": 84,
    "NSFNET-IGP": 85,
    "DGP": 86,
    "TCF": 87,
    "EIGRP": 88,
    "OSPFIGP": 89,
    "Sprite-RPC": 90,
    "LARP": 91,
    "MTP": 92,
    "AX.25": 93,
    "IPIP": 94,
    "SCC-SP": 96,
    "ETHERIP": 97,
    "ENCAP": 98,
    "GMTP": 100,
    "IFMP": 101,
    "PNNI": 102,
    "PIM": 103,
    "ARIS": 104,
    "SCPS": 105,
    "QNX": 106,
    "A/N": 107,
    "IPComp": 108,
    "SNP": 109,
    "Compaq-Peer": 110,
    "IPX-in-IP": 111,
    "PGM": 113,
    "L2TP": 115,
    "DDX": 116,
    "IATP": 117,
    "STP": 118,
    "SRP": 119,
    "UTI": 120,
    "SMP": 121,
    "SM": 122,
    "PTP": 123,
    "FIRE": 125,
    "CRTP": 126,
    "CRUDP": 127,
    "SSCOPMCE": 128,
    "IPLT": 129,
    "SPS": 130,
    "PIPE": 131,
    "SCTP": 132,
    "FC": 133,
    "RSVP-E2E-IGNORE": 134,
    "UDPLite": 136,
    "manet": 138,
    "HIP": 139,
    "WESP": 141,
    "ROHC": 142,
    "Ethernet": 143,
}

# Reverse the key value pair for reverse lookup.
PROTO_NUM_TO_NAME = {value: key for (key, value) in PROTO_NAME_TO_NUM.items()}
