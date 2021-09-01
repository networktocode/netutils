*****************
Protocol Mappers
*****************

These protocol mappers can be used whenver you have either the application protocol name or number but need the corresponding value. Something to note is that these mappings are broken up per IP protocol.
The reasoning behind this is that the same port number could be tied to two different application protocols depending on if you are using TCP or UDP. An example of this is port 13400. When using UDP, the application protocol name is `doip-disc`
but when using TCP it is `doip-data`.

Here are a few examples showing how you would use these in your python code.

.. code-block:: python

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

    # Get TCP protocol name from known port number
    SSH_PORT = TCP_NAME_TO_NUM["ssh"]
    print(SSH_PORT)
    # 22

    # Get SCTP protocol number from known name
    SCTP_NAME = SCTP_NUM_TO_NAME["EXP1"]
    print(SCTP_PORT)
    # 1021

    # Get UDP protocol number from known name
    FTP_DATA_PORT = UDP_NAME_TO_NUM["ftp-data"]
    print(FTP_DATA_PORT)
    # 20


TCP Number to Name
===================
.. exec::
    import json
    from netutils.protocol_mapper import TCP_NUM_TO_NAME
    json_obj = json.dumps(TCP_NUM_TO_NAME, sort_keys=True, indent=4)
    json_obj = json_obj[:-1] + "    }"
    print(f".. code-block:: JavaScript\n\n    {json_obj}\n\n")

TCP Name to Number
===================
.. exec::
    import json
    from netutils.protocol_mapper import TCP_NAME_TO_NUM
    json_obj = json.dumps(TCP_NAME_TO_NUM, sort_keys=True, indent=4)
    json_obj = json_obj[:-1] + "    }"
    print(f".. code-block:: JavaScript\n\n    {json_obj}\n\n")

UDP Number to Name
===================
.. exec::
    import json
    from netutils.protocol_mapper import UDP_NUM_TO_NAME
    json_obj = json.dumps(UDP_NUM_TO_NAME, sort_keys=True, indent=4)
    json_obj = json_obj[:-1] + "    }"
    print(f".. code-block:: JavaScript\n\n    {json_obj}\n\n")

UDP Name to Number
===================
.. exec::
    import json
    from netutils.protocol_mapper import UDP_NAME_TO_NUM
    json_obj = json.dumps(UDP_NAME_TO_NUM, sort_keys=True, indent=4)
    json_obj = json_obj[:-1] + "    }"
    print(f".. code-block:: JavaScript\n\n    {json_obj}\n\n")

SCTP Number to Name
===================
.. exec::
    import json
    from netutils.protocol_mapper import SCTP_NUM_TO_NAME
    json_obj = json.dumps(SCTP_NUM_TO_NAME, sort_keys=True, indent=4)
    json_obj = json_obj[:-1] + "    }"
    print(f".. code-block:: JavaScript\n\n    {json_obj}\n\n")

SCTP Name to Number
===================
.. exec::
    import json
    from netutils.protocol_mapper import SCTP_NAME_TO_NUM
    json_obj = json.dumps(SCTP_NAME_TO_NUM, sort_keys=True, indent=4)
    json_obj = json_obj[:-1] + "    }"
    print(f".. code-block:: JavaScript\n\n    {json_obj}\n\n")

DCCP Number to Name
===================
.. exec::
    import json
    from netutils.protocol_mapper import DCCP_NUM_TO_NAME
    json_obj = json.dumps(DCCP_NUM_TO_NAME, sort_keys=True, indent=4)
    json_obj = json_obj[:-1] + "    }"
    print(f".. code-block:: JavaScript\n\n    {json_obj}\n\n")

DCCP Name to Number
===================
.. exec::
    import json
    from netutils.protocol_mapper import DCCP_NAME_TO_NUM
    json_obj = json.dumps(DCCP_NAME_TO_NUM, sort_keys=True, indent=4)
    json_obj = json_obj[:-1] + "    }"
    print(f".. code-block:: JavaScript\n\n    {json_obj}\n\n")

Protocol Name to Number
=======================
.. exec::
    import json
    from netutils.protocol_mapper import PROTO_NAME_TO_NUM
    json_obj = json.dumps(PROTO_NAME_TO_NUM, sort_keys=True, indent=4)
    json_obj = json_obj[:-1] + "    }"
    print(f".. code-block:: JavaScript\n\n    {json_obj}\n\n")

Protocol Number to Name
========================
.. exec::
    import json
    from netutils.protocol_mapper import PROTO_NUM_TO_NAME
    json_obj = json.dumps(PROTO_NUM_TO_NAME, sort_keys=True, indent=4)
    json_obj = json_obj[:-1] + "    }"
    print(f".. code-block:: JavaScript\n\n    {json_obj}\n\n")
