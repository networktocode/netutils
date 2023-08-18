# Architecture Decision Records

The intention is to document deviations from a standard pattern.

## Optional Import for OUI Mapping

The following code is purposeful to ensure that we only import the large `OUI_MAPPINGS` if required. This does not effect the jinja mappings which will load the larger oui_mappings file.

```python
@_valid_mac
def get_oui(mac: str) -> str:
    from netutils.oui_mappings import OUI_MAPPINGS  # pylint: disable=import-outside-toplevel
```
## Has Lib

_Pending updates from napalm inclusion_