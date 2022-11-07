# Protocol Mappers

These protocol mappers can be used when you have either the application protocol name or number but need the corresponding value. Something to note is that these mappings are divided up per IP protocol.
The reasoning behind this is that the same port number could be tied to two different application protocols depending on the underlying IP protocol. For example, when using UDP, port 13400 is the application protocol `doip-disc`. Looking at the same port using TCP the application protocol is `doip-data`.


Here are currently available mappers:

- **DCCP_NAME_TO_NUM** - Allows mapping from a known DCCP application protocol name to DCCP application protocol number.

- **DCCP_NUM_TO_NAME** - Allows mapping from a known DCCP application protocol name to DCCP application protocol number.

- **PROTO_NAME_TO_NUM** - Allows mapping from a known IP protocol name to IP protocol number.

- **PROTO_NUM_TO_NAME** - Allows mapping from a known IP protocol number to IP protocol name.

- **SCTP_NAME_TO_NUM** -  Allows mapping from a known SCTP application protocol name to SCTP application protocol number.

- **SCTP_NUM_TO_NAME** - Allows mapping from a known SCTP application protocol number to SCTP application protocol name.

- **TCP_NAME_TO_NUM** - Allows mapping from a known TCP application protocol name to TCP application protocol number.

- **TCP_NUM_TO_NAME** - Allows mapping from a known TCP application protocol number to TCP application protocol name.

- **UDP_NAME_TO_NUM** - Allows mapping from a known UDP application protocol name to UDP application protocol number.

- **UDP_NUM_TO_NAME** - Allows mapping from a known UDP application protocol number to UDP application protocol name.


Here are a few examples showing how you would use these in your python code.

```python

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

# Get DCCP protocol port from known DCCP application name
LTP_DEEPSPACE_PORT = DCCP_NAME_TO_NUM("ltp-deepspace")
print(LTP_DEEPSPACE_PORT)
# 1113

# Get TCP protocol port from known TCP application name
SSH_PORT = TCP_NAME_TO_NUM["ssh"]
print(SSH_PORT)
# 22

# Get SCTP protocol name from known SCTP application port.
SCTP_PORT_1021_APPLICATION_NAME = SCTP_NUM_TO_NAME[1021]
print(SCTP_PORT_1021_APPLICATION_NAME)
# "exp1"

# Get UDP protocol name from known UDP application port
UDP_PORT_20_APPLICATION_NAME = UDP_NUM_TO_NAME[20]
print(UDP_PORT_20_APPLICATION_NAME)
# "ftp-data
```