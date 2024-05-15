# OS Version Tools

The OS Version Tools are used for working with versioning systems.

## Version Parsing/Deconstruction
Version parsing takes the software version given as a string, and deconstructs that value into the standards of the vendor.  The version parsing takes place in the `netutils.os_version` module.  This is necessary when specific values or flags from a software version are required to make a logical decision.  

Current Version Parsers:

- Default Parser
- Juniper JunOS

**See the following Default and Juniper JunOS parsed versions:**

```python
>>> from netutils.os_version import version_metadata

>>> version_metadata("Cisco", "IOS", "15.5")
{
    "major": "15",
    "minor": "5",
    "vendor_metadata": False,
}
>>> version_metadata("juniper", "junos", "12.4R")
{
    "isservice": False,
    "ismaintenance": False,
    "isfrs": True,
    "isspecial": False,
    "service": None,
    "service_build": None,
    "service_respin": None,
    "main": "12",
    "minor": "4",
    "type": "R",
    "build": None,
    "major": "12",
    "patch": None,
    "vendor_metadata": True,
}
```
