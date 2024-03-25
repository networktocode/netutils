# OS Version Tools

The OS Version Tools are used for working with versioning systems.

## Version Parsing/Deconstruction
Version parsing takes the software version given as a string, and deconstructs that value into the standards of the vendor.  The version parsing takes place in the `netutils.os_version` module.  This is necessary when specific values or flags from a software version are required to make a logical decision.  

Current Version Parsers:

- Juniper JunOS

**See the following Juniper JunOS parsed version:**

```python
>>> from os_version import juniper_junos_version_parser
>>> juniper_junos_version_parser("12.2x50:d41.1")
{
    "isservice": false,
    "ismaintenance": false,
    "isfrs": false,
    "isspecial": true,
    "service": "d",
    "service_build": "41",
    "service_respin": "1",
    "main": "12",
    "minor": "2",
    "type": "x",
    "build": "50"
}
```
