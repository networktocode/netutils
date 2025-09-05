"""Classes and functions used for building NIST URLs from the os platform values."""

import abc
import dataclasses
import re
import typing as t

from netutils.lib_mapper import NIST_LIB_MAPPER_REVERSE
from netutils.os_version import version_metadata

# Setting up the dataclass values for specific parsers
PLATFORM_FIELDS: t.Dict[str, t.Any] = {
    "default": [
        ("vendor", str),
        ("os_type", str),
        ("version_string", str),
        ("major", str, dataclasses.field(default=None)),  # pylint: disable=[E3701]
        ("minor", str, dataclasses.field(default=None)),  # pylint: disable=[E3701]
        ("patch", str, dataclasses.field(default=None)),  # pylint: disable=[E3701]
        ("prerelease", str, dataclasses.field(default=None)),  # pylint: disable=[E3701]
        ("buildmetadata", str, dataclasses.field(default=None)),  # pylint: disable=[E3701]
        ("vendor_metadata", bool, dataclasses.field(default=False)),  # pylint: disable=[E3701]
    ],
    "juniper": {
        "junos": [
            ("main", str, dataclasses.field(default=None)),  # pylint: disable=[E3701]
            ("type", str, dataclasses.field(default=None)),  # pylint: disable=[E3701]
            ("build", str, dataclasses.field(default=None)),  # pylint: disable=[E3701]
            ("service", str, dataclasses.field(default=None)),  # pylint: disable=[E3701]
            ("service_build", int, dataclasses.field(default=None)),  # pylint: disable=[E3701]
            ("service_respin", str, dataclasses.field(default=None)),  # pylint: disable=[E3701]
            ("isservice", bool, dataclasses.field(default=False)),  # pylint: disable=[E3701]
            ("ismaintenance", bool, dataclasses.field(default=False)),  # pylint: disable=[E3701]
            ("isfrs", bool, dataclasses.field(default=False)),  # pylint: disable=[E3701]
            ("isspecial", bool, dataclasses.field(default=False)),  # pylint: disable=[E3701]
        ]
    },
}


class OsPlatform(metaclass=abc.ABCMeta):
    """Base class for dynamically generated vendor specific platform data classes."""

    def asdict(self) -> t.Dict[str, t.Any]:
        """Returns dictionary representation of the class attributes."""
        return dataclasses.asdict(self)  # type: ignore

    @abc.abstractmethod
    def get_nist_urls(self) -> t.List[str]:
        """Returns list of NIST URLs for the platform."""

    def get(self, key: str) -> t.Any:
        """Return value of the attribute matching provided name or None if no attribute is found."""
        return getattr(self, key, None)

    def keys(self) -> t.KeysView[t.Any]:
        """Return attributes and their values as dict keys."""
        # Disabling pylint no-member due to BUG: https://github.com/pylint-dev/pylint/issues/7126
        return self.__annotations__.keys()  # pylint: disable=no-member

    def __getitem__(self, key: str) -> t.Any:
        """Allow retrieving attributes using subscript notation."""
        return getattr(self, key)


def _get_nist_urls_juniper_junos(os_platform_data: t.Dict[str, t.Any]) -> t.List[str]:  # pylint: disable=R0911
    """Create a list of possible NIST Url strings for JuniperPlatform.

    Returns:
        List of NIST CPE URLs that may contain platform data.
    """
    nist_urls = []
    base_url = f"{'https://services.nvd.nist.gov/rest/json/cves/2.0?cpeName=cpe:2.3:o:juniper:junos'}"

    # BASE
    _main = os_platform_data.get("main")
    _minor = os_platform_data.get("minor")
    _type = ""  # Check if this is an issue as used below with potentially no definition
    if os_platform_data["type"]:
        _type = os_platform_data["type"].lower()
    _build = os_platform_data.get("build")

    # SERVICE
    _service = ""  # Check if this is an issue as used below with potentially no definition
    if os_platform_data["service"]:
        _service = os_platform_data["service"].lower()
    _service_build = os_platform_data.get("service_build")
    _service_respin = os_platform_data.get("service_respin")

    # EXTRAS
    delim_six = ":*" * 6
    delim_seven = ":*" * 7

    if os_platform_data["isspecial"]:
        # e.g. base_ext = juniper:junos:12.1x47
        base_ext = f"{base_url}:{_main}.{_minor}{_type}{_build}"
    else:
        # e.g. base_ext = juniper:junos:12.1
        base_ext = f"{base_url}:{_main}.{_minor}"

    # X Series (Special) Examples: 12.1x47:d40, 12.2x50:d41.1
    if os_platform_data["isspecial"] and os_platform_data["service_respin"]:  # pylint: disable=R1705
        # nist_urls.append(juniper:junos:12.2x50:d41.1:*:*:*:*:*:*)
        nist_urls.append(f"{base_ext}:{_service}{_service_build}.{_service_respin}{delim_six}")

        # nist_urls.append(juniper:junos:12.2x50-d41.1:*:*:*:*:*:*:*)
        nist_urls.append(f"{base_ext}-{_service}{_service_build}.{_service_respin}{delim_seven}")

        return nist_urls

    elif os_platform_data["isspecial"]:
        # nist_urls.append(juniper:junos:12.1x47:d40:*:*:*:*:*:*)
        nist_urls.append(f"{base_ext}:{_service}{_service_build}{delim_six}")

        # nist_urls.append(juniper:junos:12.1x47-d40:*:*:*:*:*:*:*)
        nist_urls.append(f"{base_ext}-{_service}{_service_build}{delim_seven}")

        return nist_urls  #

    if not os_platform_data.get("type"):
        # nist_urls.append(juniper:junos:12.1:-:*:*:*:*:*:*)
        nist_urls.append(f"{base_ext}:-{delim_six}")

        return nist_urls

    if not os_platform_data.get("build"):
        # nist_urls.append(juniper:junos:10.4s:*:*:*:*:*:*:*)
        nist_urls.append(f"{base_ext}{_type}{delim_seven}")

        return nist_urls

    if os_platform_data.get("build") and not os_platform_data.get("service"):
        # nist_urls.append(juniper:junos:12.3r12:*:*:*:*:*:*:*)
        nist_urls.append(f"{base_ext}{_type}{_build}{delim_seven}")

        # nist_urls.append(juniper:junos:12.2:r1:*:*:*:*:*:*)
        nist_urls.append(f"{base_ext}:{_type}{_build}{delim_six}")

        return nist_urls

    if os_platform_data.get("service") and os_platform_data.get("service_respin"):
        # nist_urls.append(juniper:junos:11.4r13:s2.1:*:*:*:*:*:*)
        nist_urls.append(f"{base_ext}{_type}{_build}:{_service}{_service_build}.{_service_respin}{delim_six}")

        # nist_urls.append(juniper:junos:12.2:r8-s2.1:*:*:*:*:*:*)
        nist_urls.append(f"{base_ext}{_type}{_build}-{_service}{_service_build}.{_service_respin}{delim_seven}")

        return nist_urls

    if os_platform_data.get("service"):
        # nist_urls.append(juniper:junos:11.4r13:s2:*:*:*:*:*:*)
        nist_urls.append(f"{base_ext}{_type}{_build}:{_service}{_service_build}{delim_six}")

        # nist_urls.append(juniper:junos:12.2:r8-s2:*:*:*:*:*:*)
        nist_urls.append(f"{base_ext}{_type}{_build}-{_service}{_service_build}{delim_seven}")

        return nist_urls

    raise ValueError("Failure creating Juniper JunOS Version. Format is unknown.")


def _get_nist_urls_default(os_platform_data: t.Dict[str, t.Any]) -> t.List[str]:
    r"""Create a list of possible NIST Url strings.

    Child models with NIST URL customizations need their own "get_nist_urls" method.

    Returns:
        List of NIST CPE URLs that may contain platform data.
    """
    nist_urls = []
    escape_list = [r"\(", r"\)"]
    base_url = f"{'https://services.nvd.nist.gov/rest/json/cves/2.0?cpeName=cpe:2.3:o:'}"

    os_platform_data = {"base_url": base_url, **os_platform_data}
    os_platform_data["version_string"] = os_platform_data.get("version_string").replace("-", ":")  # type: ignore

    version_string = os_platform_data.get("version_string", "").lower()
    for escape_char in escape_list:
        version_string = re.sub(escape_char, "\\" + escape_char, version_string)

    os_platform_data["version_string"] = version_string

    nist_urls.append(
        f"{base_url}{os_platform_data['vendor']}:{os_platform_data['os_type']}:{os_platform_data['version_string']}:*"
    )

    return nist_urls


def _os_platform_object_builder(vendor: str, platform: str, version: str) -> object:
    """Creates a platform object relative to its need and definition.

    Args:
        vendor (str): Name of vendor
        platform (str): Name of os/other platform
        version (str): Version value

    Returns:
        object: Platform object

    Examples:
        >>> jp = _os_platform_object_builder("juniper", "junos", "12.1R3-S4.1")
        >>> jp.get_nist_urls()
        ['https://services.nvd.nist.gov/rest/json/cves/2.0?cpeName=cpe:2.3:o:juniper:junos:12.1r3:s4.1:*:*:*:*:*:*', 'https://services.nvd.nist.gov/rest/json/cves/2.0?cpeName=cpe:2.3:o:juniper:junos:12.1r3-s4.1:*:*:*:*:*:*:*']
    """
    platform = platform.lower()
    vendor = vendor.lower()

    class_fields = [*PLATFORM_FIELDS["default"]]
    vendor_platform_fields = PLATFORM_FIELDS.get(vendor, {}).get(platform, [])
    class_fields.extend(vendor_platform_fields)

    version_parser = version_metadata(vendor, platform, version)

    field_values = {
        "vendor": vendor,
        "os_type": platform,
        "version_string": version,
    }

    if version_parser:
        field_values.update(version_parser)

    class_name = f"{vendor.capitalize()}{platform.capitalize()}"
    get_nist_urls_func = get_nist_url_funcs.get(vendor, {}).get(platform) or get_nist_url_funcs["default"]

    platform_cls = dataclasses.make_dataclass(
        cls_name=class_name, fields=class_fields, bases=(OsPlatform,), namespace={"get_nist_urls": get_nist_urls_func}
    )

    return platform_cls(**field_values)


get_nist_url_funcs: t.Dict[str, t.Any] = {
    "default": _get_nist_urls_default,
    "juniper": {"junos": _get_nist_urls_juniper_junos},
}


def get_nist_vendor_platform_urls(vendor: str, platform: str, version: str) -> t.List[str]:
    """Generate list of possible NIST URLs for the Vendor, OS Platform, and Version.

    Args:
        vendor (str): OS Software Platform Vendor/Manufacturer
        platform (str): OS Software Platform Name
        version (str): OS Software Platform Version

    Returns:
        t.List[str]: NIST URLs to search for possible CVE matches

    Examples:
        >>> from netutils.nist import get_nist_vendor_platform_urls
        >>> get_nist_vendor_platform_urls('cisco', 'ios', '15.3')
        ['https://services.nvd.nist.gov/rest/json/cves/2.0?cpeName=cpe:2.3:o:cisco:ios:15.3:*']
        >>>
    """
    platform_data = _os_platform_object_builder(vendor, platform, version).__dict__

    if vendor.lower() == "juniper" and platform.lower() == "junos":
        return _get_nist_urls_juniper_junos(platform_data)
    return _get_nist_urls_default(platform_data)


def get_nist_urls(network_driver: str, version: str) -> t.List[str]:
    """Generate list of possible NIST URLs for the Network Driver, and Version.

    Args:
        network_driver (str): Value of device network_driver (Ex: cisco_ios, arista_eos)
        version (str): OS Software Platform Version

    Returns:
        t.List[str]: NIST URLs to search for possible CVE matches

    Examples:
        >>> from netutils.nist import get_nist_urls
        >>> get_nist_urls('cisco_ios', '15.3')
        ['https://services.nvd.nist.gov/rest/json/cves/2.0?cpeName=cpe:2.3:o:cisco:ios:15.3:*']
        >>>
    """
    # DICTIONARY FOR VENDOR/PLATFORM TO NETWORK_DRIVER; UPDATE AS NEEDED
    vendor_os: str = NIST_LIB_MAPPER_REVERSE.get(network_driver, "")
    if not vendor_os:
        raise ValueError(
            f"The network driver `{network_driver}` has no associated mapping, the supported drivers are {list(NIST_LIB_MAPPER_REVERSE.keys())}."
        )
    vendor, os_name = vendor_os.split(":")

    return get_nist_vendor_platform_urls(vendor, os_name, version)
