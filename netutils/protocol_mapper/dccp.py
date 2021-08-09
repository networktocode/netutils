"""DCCP port to name and name to port mapper."""

# https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml
# DCCP port to name mapping.
DCCP_NUM_TO_NAME = {
    9: "DISCARD",
    1021: "EXP1",
    1022: "EXP2",
    1113: "LTP-DEEPSPACE",
    4195: "AWS-WSP",
    4556: "DTN-BUNDLE",
    5004: "AVT-PROFILE-1",
    5005: "AVT-PROFILE-2",
    6514: "SYSLOG-TLS",
}
# DCCP port name to number mapping
DCCP_NAME_TO_NUM = {value: key for (key, value) in DCCP_NUM_TO_NAME.items()}
