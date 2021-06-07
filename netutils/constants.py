"""Constant definitions used in project."""

# This variable provides mapping for known interface variants, to the associated long form.
BASE_INTERFACES = {
    "ATM": "ATM",
    "AT": "ATM",
    "B": "Bdi",
    "Bd": "Bdi",
    "Bdi": "Bdi",
    "Bridge-Aggregation": "Port-channel",
    "EOBC": "EOBC",
    "EO": "EOBC",
    "Ethernet": "Ethernet",
    "Eth": "Ethernet",
    "eth": "Ethernet",
    "Et": "Ethernet",
    "et": "Ethernet",
    "FastEthernet": "FastEthernet",
    "FastEth": "FastEthernet",
    "FastE": "FastEthernet",
    "Fast": "FastEthernet",
    "Fas": "FastEthernet",
    "FE": "FastEthernet",
    "Fa": "FastEthernet",
    "fa": "FastEthernet",
    "Fddi": "Fddi",
    "FD": "Fddi",
    "FortyGigabitEthernet": "FortyGigabitEthernet",
    "FortyGigEthernet": "FortyGigabitEthernet",
    "FortyGigEth": "FortyGigabitEthernet",
    "FortyGigE": "FortyGigabitEthernet",
    "FortyGig": "FortyGigabitEthernet",
    "FGE": "FortyGigabitEthernet",
    "FO": "FortyGigabitEthernet",
    "Fo": "FortyGigabitEthernet",
    "FiftyGigabitEthernet": "FiftyGigabitEthernet",
    "FiftyGigEthernet": "FiftyGigabitEthernet",
    "FiftyGigEth": "FiftyGigabitEthernet",
    "FiftyGigE": "FiftyGigabitEthernet",
    "FI": "FiftyGigabitEthernet",
    "Fi": "FiftyGigabitEthernet",
    "fi": "FiftyGigabitEthernet",
    "GigabitEthernet": "GigabitEthernet",
    "GigEthernet": "GigabitEthernet",
    "GigEth": "GigabitEthernet",
    "GigE": "GigabitEthernet",
    "Gig": "GigabitEthernet",
    "GE": "GigabitEthernet",
    "Ge": "GigabitEthernet",
    "ge": "GigabitEthernet",
    "Gi": "GigabitEthernet",
    "gi": "GigabitEthernet",
    "HundredGigabitEthernet": "HundredGigabitEthernet",
    "HundredGigEthernet": "HundredGigabitEthernet",
    "HundredGigEth": "HundredGigabitEthernet",
    "HundredGigE": "HundredGigabitEthernet",
    "HundredGig": "HundredGigabitEthernet",
    "Hu": "HundredGigabitEthernet",
    "TwentyFiveGigabitEthernet": "TwentyFiveGigE",
    "TwentyFiveGigEthernet": "TwentyFiveGigE",
    "TwentyFiveGigEth": "TwentyFiveGigE",
    "TwentyFiveGigE": "TwentyFiveGigE",
    "TwentyFiveGig": "TwentyFiveGigE",
    "TF": "TwentyFiveGigE",
    "Tf": "TwentyFiveGigE",
    "tf": "TwentyFiveGigE",
    "TwoHundredGigabitEthernet": "TwoHundredGigabitEthernet",
    "TwoHundredGigEthernet": "TwoHundredGigabitEthernet",
    "TwoHundredGigEth": "TwoHundredGigabitEthernet",
    "TwoHundredGigE": "TwoHundredGigabitEthernet",
    "TwoHundredGig": "TwoHundredGigabitEthernet",
    "TH": "TwoHundredGigabitEthernet",
    "Th": "TwoHundredGigabitEthernet",
    "th": "TwoHundredGigabitEthernet",
    "FourHundredGigabitEthernet": "FourHundredGigabitEthernet",
    "FourHundredGigEthernet": "FourHundredGigabitEthernet",
    "FourHundredGigEth": "FourHundredGigabitEthernet",
    "FourHundredGigE": "FourHundredGigabitEthernet",
    "FourHundredGig": "FourHundredGigabitEthernet",
    "F": "FourHundredGigabitEthernet",
    "f": "FourHundredGigabitEthernet",
    "Loopback": "Loopback",
    "loopback": "Loopback",
    "Lo": "Loopback",
    "lo": "Loopback",
    "Management": "Management",
    "Mgmt": "Management",
    "mgmt": "Management",
    "Ma": "Management",
    "Management_short": "Ma",
    "MFR": "MFR",
    "Multilink": "Multilink",
    "Mu": "Multilink",
    "n": "nve",
    "nv": "nve",
    "nve": "nve",
    "PortChannel": "Port-channel",
    "Port-channel": "Port-channel",
    "Port-Channel": "Port-channel",
    "port-channel": "Port-channel",
    "po": "Port-channel",
    "Po": "Port-channel",
    "POS": "POS",
    "PO": "POS",
    "Serial": "Serial",
    "Se": "Serial",
    "S": "Serial",
    "Sync": "Sy",
    "Ten-GigabitEthernet": "TenGigabitEthernet",
    "TenGigabitEthernet": "TenGigabitEthernet",
    "TenGigEthernet": "TenGigabitEthernet",
    "TenGigEth": "TenGigabitEthernet",
    "TenGig": "TenGigabitEthernet",
    "TeGig": "TenGigabitEthernet",
    "Ten": "TenGigabitEthernet",
    "T": "TenGigabitEthernet",
    "Te": "TenGigabitEthernet",
    "te": "TenGigabitEthernet",
    "Tunnel": "Tunnel",
    "Tun": "Tunnel",
    "Tu": "Tunnel",
    "Twe": "TwentyFiveGigE",
    "Tw": "TwoGigabitEthernet",
    "Two": "TwoGigabitEthernet",
    "Virtual-Access": "Virtual-Access",
    "Vi": "Virtual-Access",
    "Virtual-Template": "Virtual-Template",
    "Vt": "Virtual-Template",
    "VLAN": "VLAN",
    "V": "VLAN",
    "Vl": "VLAN",
    "Vlan-interface": "VLAN",
    "vlan": "VLAN",
    "Wlan-GigabitEthernet": "Wlan-GigabitEthernet",
    "XGE": "TenGigabitEthernet",
}

# The default mac format
DEFAULT_MAC_FORMAT = "MAC_DOT_FOUR"

# A dictionary to describe the MAC format to it's characteristics.
MAC_CREATE = dict(
    MAC_COLON_TWO={"count": 2, "char": ":"},
    MAC_COLON_FOUR={"count": 4, "char": ":"},
    MAC_DASH_TWO={"count": 2, "char": "-"},
    MAC_DASH_FOUR={"count": 4, "char": "-"},
    MAC_DOT_TWO={"count": 2, "char": "."},
    MAC_DOT_FOUR={"count": 4, "char": "."},
    MAC_NO_SPECIAL={"count": 12, "char": ""},
)

# A dictionary to describe the MAC format REGEX pattern.
MAC_REGEX = dict(
    MAC_COLON_TWO=r"([a-fA-F0-9]{2}[:]){5}([a-fA-F0-9]{2})",
    MAC_COLON_FOUR=r"([a-fA-F0-9]{4}[:]){2}([a-fA-F0-9]{4})",
    MAC_DASH_TWO=r"([a-fA-F0-9]{2}[\-]){5}([a-fA-F0-9]{2})",
    MAC_DASH_FOUR=r"([a-fA-F0-9]{4}[\-]){2}([a-fA-F0-9]{4})",
    MAC_DOT_TWO=r"([a-fA-F0-9]{2}[\.]){5}([a-fA-F0-9]{2})",
    MAC_DOT_FOUR=r"([a-fA-F0-9]{4}[\.]){2}([a-fA-F0-9]{4})",
    MAC_NO_SPECIAL=r"([a-fA-F0-9]{12})",
)

"""Variable definitions used in project, purposely not constants to signal to use these variables can be overridden."""

# This variable maps a full interface name, to an opinionated shortened name.
REVERSE_MAPPING = {
    "ATM": "At",
    "EOBC": "EO",
    "Ethernet": "Et",
    "FastEthernet": "Fa",
    "Fddi": "FD",
    "FortyGigabitEthernet": "Fo",
    "GigabitEthernet": "Gi",
    "HundredGigabitEthernet": "Hu",
    "Loopback": "Lo",
    "Management": "Ma",
    "MFR": "MFR",
    "Multilink": "Mu",
    "Port-channel": "Po",
    "POS": "PO",
    "Serial": "Se",
    "Sync": "Sy",
    "TenGigabitEthernet": "Te",
    "Tunnel": "Tu",
    "TwoGigabitEthernet": "Two",
    "TwentyFiveGigE": "Twe",
    "Virtual-Access": "Vi",
    "Virtual-Template": "Vt",
    "VLAN": "Vl",
    "Wlan-GigabitEthernet": "Wl-Gi",
}

# These are base level filters to provide documentation of how a CLEAN_FILTER can be used, This is a private variable, and subject
# to change without notice between revisions.
_PROVIDED_CLEAN_FILTERS = [
    {"regex": r"^Current\s+configuration.*\n"},
    {"regex": r"^Building\s+configuration.*\n"},
    {"regex": r"^ntp\s+clock-period.*\n"},
]

# These are base level filters to provide documentation of how a SANITIZE_FILTERS can be used, This is a private variable, and subject
# to change without notice between revisions.
_PROVIDED_SANITIZE_FILTERS = [
    {"regex": r"(username\s+\S+\spassword\s+5\s+)\S+(\s+role\s+\S+)", "replace": "\\1<redacted_config>\\2"},
    {"regex": r"(username\s+\S+\s+privilege\s+15\s+password\s+0\s+)\S+", "replace": "\\1<redacted_config>"},
]
