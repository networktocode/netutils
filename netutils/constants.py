"""Constant definitions used in project."""

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
