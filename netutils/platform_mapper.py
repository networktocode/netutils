"""Platform Mappers."""
# The intent of this script is to take a given platform, determine the format, and reformat it for another purpose
# An example of this is a platform being formatted for NIST Database Query
import dataclasses
import typing as t

from netutils.nist import get_nist_url_funcs
from netutils.os_version_parser import os_version_parsers

PLATFORM_FIELDS: t.Dict[str, t.Any] = {
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
            ("isservice", bool, dataclasses.field(default=False)),
            ("ismaintenance", bool, dataclasses.field(default=False)),
            ("isfrs", bool, dataclasses.field(default=False)),
            ("isspecial", bool, dataclasses.field(default=False)),
        ]
    },
}


@dataclasses.dataclass
class OsPlatform:
    """Base class for dynamically generated vendor specific platform data classes."""

    @property
    def asdict(self) -> t.Dict[str, t.Any]:
        """Returns dictionary representation of the class attributes."""
        return dataclasses.asdict(self)

    def get_nist_urls(self, api_key: str) -> t.List[str]:
        """Returns list of NIST URLs for the platform."""
        return self.get_nist_urls_fn(api_key)  # type: ignore

    def get(self, key: str) -> t.Any:
        """Return value of the attribute matching provided name or None if no attribute is found."""
        return getattr(self, key, None)

    def keys(self) -> t.KeysView[t.Any]:
        """Return attributes and their values as dict keys."""
        return self.__annotations__.keys()

    def __getitem__(self, key: str) -> t.Any:
        """Allow retrieving attributes using subscript notation."""
        return getattr(self, key)


def os_platform_object_builder(vendor: str, platform: str, version: str) -> object:
    """Creates a platform object relative to its need and definition.

    Args:
        vendor

    Returns:
        A platform object

    Examples:
        >>> jp = os_platform_object_builder("juniper", "junos", "12.1R3-S4.1")
        >>> jp.get_nist_urls("AAA-BBB-CCC-DDD")
        ['https://services.nvd.nist.gov/rest/json/cpes/1.0?apiKey=AAA-BBB-CCC-DDD&addOns=cves&cpeMatchString=cpe:2.3:o:juniper:junos:12.1R3:S4.1:*:*:*:*:*:*', 'https://services.nvd.nist.gov/rest/json/cpes/1.0?apiKey=AAA-BBB-CCC-DDD&addOns=cves&cpeMatchString=cpe:2.3:o:juniper:junos:12.1R3-S4.1:*:*:*:*:*:*:*']
    """
    platform = platform.lower()

    class_fields = [*PLATFORM_FIELDS["default"]]
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

    base_class = OsPlatform
    class_name = f"{vendor.capitalize()}{platform.capitalize()}"
    get_nist_urls_fn = get_nist_url_funcs.get(vendor, {}).get(platform, None) or get_nist_url_funcs["default"]
    base_class.get_nist_urls_fn = get_nist_urls_fn  # type: ignore

    platform_cls = dataclasses.make_dataclass(
        cls_name=class_name,
        fields=class_fields,
        bases=(OsPlatform,),
    )

    return platform_cls(**field_values)
