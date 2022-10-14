# Config Parsers Development

## Current Included Parsers

--8<-- "docs/dev/include_parser_list.md"

## Building for Actual Use Cases

The library attempts to model actual configuration as shown in the running configuration, traditionally shown with a `show run` or similar command. Accounting for use cases that do not exist in the running configuration, are generally outside the scope of the project.

There are occasions where there will be a exceptions for valid running configuration and will be documented below.

### Fortinet Fortios Parser

In order to support html blocks that exist in Fortios configurations, some preprocessing is executed, this is a regex that specifically grabs everything between quotes after the 'set buffer' sub-command. It's explicitly looking for double quote followed by a newline ("\n) to end the captured data.  This support for html data will not support any other html that doesn't follow this convention.

### F5 Parser

The "ltm rule" configuration sections are not uniform nor standardized; therefor, these sections are completely removed from the configuration in a preprocessing event.

### Nokia SROS Parser

The section banners have been simplified to extract the section header itself. This means that `echo "System Configuration"` will be converted to just "System Configuration".

### Citrix NetScaler Parser

As the NetScaler configuration uses each line to make a specific configuration change there is no support for parent/child relationships in the parser.

### Duplicate Line Detection

In some circumstances replacing lines, such as secrets without uniqueness in the replacement, will result in duplicated lines that are invalid configuration, such as::

```text
snmp-server community <<REPLACED>> RO SNMP_ACL_RO
snmp-server community <<REPLACED>> RO SNMP_ACL_RO
```

There are some known use cases, such as the below that are considered::

```text
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
```

Documented use cases that are actual configuration on a network device are considered valid and should be opened for bug fixes. However, configuration that does not actually exist on the running config of network devices are out of scope for the parser.

## New Parsers

There are a series of considerations documented below, when developing a new parser.

- Creation of a new class that must be created in `netutils/config/parser.py` file.
- Creation of a parser class that inherits from the class `BaseConfigParser` in the Python Method Resolution Order (MRO).
  - In nearly all cases should inherit directory off of `BaseSpaceConfigParser` or `BaseBraceConfigParser`.
  - `BaseSpaceConfigParser` is for Cisco IOS-like configurations.
  - `BaseBraceConfigParser` is for JUNOS-like configurations that use curly braces.
- Create the class name in the format of `{os_name.title()}ConfigParser`.
  - The classes `__init__` method must keep true to the signature or `__init__(self, config)`.
  - The class must provide a `self.config_lines` that is a list of `ConfigLine` named tuples.
- Build tests for the `tests/unit/mock/config/compliance/{os_name}/*` and `tests/unit/mock/config/parser/{os_name}/*`.
- Add to `netutils/config/compliance.py` the `parser_map`, that maps the name of the parser to the Plugin.
- Fill out docstrings in the class and methods within the class that describe the parameters and an Example that compiles.
- The following tips will generally be applicable.
  - Generally a class method should provide a `comment_chars` and `banner_start` as well as sometimes `banner_end`.
  - Generally on the `__init__` should call the `build_config_relationship` method.
  - Often can inherit directly from `CiscoConfigParser`.
  - Observe the existing patterns, make use of `super`, and inheritance to reuse existing code.
