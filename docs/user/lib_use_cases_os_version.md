# OS Version Tools

The OS Version Tools are used for working with versioning systems.

## Version Parsing/Deconstruction
Version parsing takes the software version given as a string, and deconstructs that value into the standards of the vendor.  The version parsing takes place in the `netutils.os_version` module.  This is necessary when specific values or flags from a software version are required to make a logical decision.  

Current Version Parsers:

- Default Parser
- Juniper JunOS

**See the following Default and Juniper JunOS parsed versions:**

```python
>>> from os_version import default_os_metadata, juniper_junos_metadata

>>> default_os_metadata("cisco", "ios", "15.5")
{
    "major": "15",
    "minor": "5",
    "patch": None,
}
>>> juniper_junos_metadata("juniper", "junos", "12.2x50:d41.1")
{
    "isservice": false,
    "ismaintenance": false,
    "isfrs": false,
    "isspecial": true,
    "service": "d",
    "service_build": "41",
    "service_respin": "1",
    "main": "12",
    "major": "12",
    "minor": "2",
    "type": "x",
    "build": "50",
    "patch": "50"
}
```
