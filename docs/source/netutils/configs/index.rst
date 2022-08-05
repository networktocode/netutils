*******
Configs
*******

.. automodule:: netutils.config.clean
    :members:

.. automodule:: netutils.config.compliance
    :members:

.. automodule:: netutils.config.parser
    :members:

Edge Cases
==============

Fortinet Fortios Parser
-----------------------
- In order to support html blocks that exist in Fortios configurations, some preprocessing is executed, this is a regex that specifically grabs everything between quotes after the 'set buffer' sub-command. It's explicitly looking for double quote followed by a newline ("\n) to end the captured data.  This support for html data will not support any other html that doesn't follow this convention.

F5 Parser
-----------------------
- The "ltm rule" configuration sections are not uniform nor standardized; therefor, these sections are completely removed from the configuration in a preprocessing event.

Nokia SROS Parser
-----------------
- The section banners have been simplified to extract the section header itself. This means that `echo "System Configuration"` will be converted to just "System Configuration".

Duplicate Line Detection
--------------------------
In some circumstances replacing lines, such as secrets without uniqueness in the replacement, will result in duplicated lines that are invalid configuration, such as::

    snmp-server community <<REPLACED>> RO SNMP_ACL_RO
    snmp-server community <<REPLACED>> RO SNMP_ACL_RO

There are some known use cases, such as the below that are considered::

    router bgp 6500
     bgp router-id 10.0.0.11
     !
     address-family ipv4 unicast
      redistribute connected
     exit-address-family <--- duplicated hierarchy
     !
     address-family l2vpn evpn
      neighbor underlay activate
     exit-address-family <--- duplicated hierarchy

Documented use cases that are actual configuration on a network device are considered valid and should be opened for bug fixes. However, configuration that does not actually exist on the running config of network devices are out of scope for the parser.
