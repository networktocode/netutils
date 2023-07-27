"""Platform Mappers."""
# The intent of this script is to take a given platform, determine the format, and reformat it for another purpose
# An example of this is a platform being formatted for NIST Database Query
from dataclasses import asdict, field, make_dataclass

from netutils.nist import get_nist_url_funcs
from netutils.os_version_parser import os_version_parsers

PLATFORM_FIELDS = {
    "default": [
        ("vendor", str),
        ("os_type", str),
        ("version_string", str),
    ],
    "juniper": {
        "junos": [
            ("main", str),
            ("minor", str),
            ("type", str),
            ("build", str),
            ("service", str),
            ("service_build", int),
            ("service_respin", str),
            ("isservice", bool, field(default=False)),
            ("ismaintenance", bool, field(default=False)),
            ("isfrs", bool, field(default=False)),
            ("isspecial", bool, field(default=False)),
        ]
    },
}


def create_platform_object(vendor: str, platform: str, version: str) -> object:
    """Creates a platform object relative to its need and definition.

    Args:
        vendor

    Returns:
        A platform object

    Examples:
        >>> jp = create_platform_object("juniper", "junos", "12.1R3-S4.1")
        >>> jp.get_nist_urls("AAA-BBB-CCC-DDD")
        ['https://services.nvd.nist.gov/rest/json/cpes/1.0?apiKey=AAA-BBB-CCC-DDD&addOns=cves&cpeMatchString=cpe:2.3:o:juniper:junos:12.1R3:S4.1:*:*:*:*:*:*', 'https://services.nvd.nist.gov/rest/json/cpes/1.0?apiKey=AAA-BBB-CCC-DDD&addOns=cves&cpeMatchString=cpe:2.3:o:juniper:junos:12.1R3-S4.1:*:*:*:*:*:*:*']
    """
    platform = platform.lower()
    platform_obj = None

    class_fields = []
    class_fields.extend(PLATFORM_FIELDS["default"])
    vendor_platform_fields = PLATFORM_FIELDS.get(vendor, {}).get(platform, [])
    class_fields.extend(vendor_platform_fields)

    version_parser = os_version_parsers.get(vendor, {}).get(platform, None)
    field_values = {
        "vendor": vendor,
        "os_type": platform,
        "version_string": version,
    }
    if version_parser:
        field_values.update(version_parser(version))

    class_name = f"{vendor.capitalize()}{platform.capitalize()}"
    get_nist_url_fn = get_nist_url_funcs.get(vendor, {}).get(platform, None) or get_nist_url_funcs["default"]
    get_item_fn = lambda self, key: getattr(self, key)
    keys_fn = lambda self: self.__annotations__.keys()

    platform_obj = make_dataclass(
        cls_name=class_name,
        fields=class_fields,
        namespace={
            "get_nist_urls": get_nist_url_fn,
            "asdict": asdict,
            "__getitem__": get_item_fn,
            "get": get_item_fn,
            "keys": keys_fn,
        },
    )
    return platform_obj(**field_values)


version = "12.3R4"
jp = create_platform_object("juniper", "junos", version)
print(version, jp.asdict())
print(jp.get_nist_urls("aaa"))
version = "12.1x47:d40"
jp = create_platform_object("juniper", "junos", version)
print(version, jp.asdict())
print(jp.get_nist_urls("aa"))
version = "12.1R3-S4.1"
jp = create_platform_object("juniper", "junos", version)
print(version, jp.asdict())
print(jp.get_nist_urls("aa"))
version = "12.1"
jp = create_platform_object("juniper", "junos", version)
print(version, jp.asdict())
print(jp.get_nist_urls("aa"))
version = "16.7md"
jp = create_platform_object("cisco", "ios", version)
print(version, jp.asdict())
print(jp.get_nist_urls("aa"))
