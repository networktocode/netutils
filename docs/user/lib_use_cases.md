# Using the Library

As the Python library is intended to be a low-level implementation, the primary use case is within Code. On this page as well as subsequent pages we will provide an overview on the type of functions and examples.

# Function Groupings

Functions are grouped with like functions, such as IP or MAC address based functions. Included to date are groupings of:

- ASN - Provides the ability to convert BGP ASN from integer to dot notation and back.
- Bandwidth - Provides the ability to convert between various bandwidth values.
- Banner - Provides the ability to normalize the various banner delimiters.
- Configuration
    - Cleaning - Provides the ability to remove or replace lines based on regex matches.
    - Compliance - Provides the ability to compare two configurations to sanely understand the differences.
    - Conversion - Provides the ability to convert between different syntax's within the same OS.
    - Parsing - Provides the ability to parse configuration for the minor differences that are there.
- DNS - Provides the ability to work with DNS, such as validating that a FQDN is resolvable.
- Hash - Provide a convenience method for hashlib to be used in Jinja2
- Interface - Provides the ability to work with interface names, expanding, abbreviating, and splitting the names.
- IP Address - Provides the ability to work with IP addresses, primarily exposing Python `ipaddress` functionality.
- Library Helpers - Provides helpers to pull useful information, e.g. NAPALM getters.
- Library Mapper - Provides mappings in expected vendor names between Netmiko, NAPALM, pyntc, ntc-templates, pyats, and scrapli.
- MAC Address - Provides the ability to work with MAC addresses such as validating or converting to integer.
- NIST - Provides the ability to obtain a URL formatted for NIST CPE Query.
- OS Version - Provides the ability to work with OS version, such as defining an upgrade path.
- Password - Provides the ability to compare and encrypt common password schemas such as type5 and type7 Cisco passwords.
- Ping - Provides the ability to ping, currently only tcp ping.
- Platform Mapper - Provides custom parsers for breakdown of OS Software Versions/Revisions.
- Protocol Mapper - Provides a mapping for protocol names to numbers and vice versa.
- Regex - Provide convenience methods for regex to be used in Jinja2.
- Route - Provides the ability to provide a list of routes and an IP Address and return the longest prefix matched route.
- Time - Provides the ability to convert between integer time and string times.
- VLANs - Provide the ability to convert configuration into lists or lists into configuration.

## Examples

While all functions come with examples in the docstrings, for quick reference of the types of problems this library intends to solve the following examples are provided.

The following function will help in deploying list of VLANs and match the configuration style in a standard IOS-like configurations.

```python
>>> from netutils.vlan import vlanlist_to_config
>>>
>>> vlan_cfg = vlanlist_to_config([1, 2, 3, 5, 6, 1000, 1002, 1004, 1006, 1008, 1010, 1012, 1014, 1016, 1018])
>>>
>>> vlan_cfg
["1-3,5,6,1000,1002,1004,1006,1008,1010,1012,1014", "1016,1018"]
>>>
>>> for index, line in enumerate(vlan_cfg):
...     if index == 0:
...         print(f"  switchport trunk allowed vlan {line}")
...     else:
...         print(f"  switchport trunk allowed vlan add {line}")
...
  switchport trunk allowed vlan 1-3,5,6,1000,1002,1004,1006,1008,1010,1012,1014
  switchport trunk allowed vlan add 1016,1018
>>>
```

You may want to compare a known password with a given encrypted password. This can help in verifying if the passwords are as expected for compliance reasons.

```python
>>> from netutils.password import compare_cisco_type5
>>>
>>> compare_cisco_type5("cisco","$1$nTc1$Z28sUTcWfXlvVe2x.3XAa.")
True
>>>
>>> compare_cisco_type5("not_cisco","$1$nTc1$Z28sUTcWfXlvVe2x.3XAa.")
False
>>>
```

Often times interfaces will come in various different shortened names, and it is helpful to normalize them.

```python
>>> from netutils.interface import canonical_interface_name
>>>
>>> canonical_interface_name("Gi1/0/1")
'GigabitEthernet1/0/1'
>>>
>>> canonical_interface_name("Eth1")
'Ethernet1'
>>>
```

!!! tip
    These are just some examples of the many functions provided by this library. Please review the Developer code for Examples on every public function
