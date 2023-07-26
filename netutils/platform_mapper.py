"""Platform Mappers."""
# The intent of this script is to take a given platform, determine the format, and reformat it for another purpose
# An example of this is a platform being formatted for NIST Database Query
from dataclasses import make_dataclass, field, asdict
from functools import partial
import re
import typing as t


def juniper_junos_version_parser(version: str) -> t.Dict:
    """Parses JunOS Version into usable bits matching JunOS Standars.

    Args:
        version

    Returns:
        A dictionary containing parsed version information

    Examples:
        >>> parsed_version = juniper_junos_version_parser("12.3R4")
    """
    # Use regex to group the main, minor, type and build into useable pieces
    # re_main_minor_type_build = re.search(r"^(\d+)\.(\d+)([xXrRsS])?(\d+)?", split_version[0])
    re_main_minor_type_build = re.compile(
        r"""
        ^
        (?P<main>\d+)           # main train
        \.                      # dot separator
        (?P<minor>\d+)          # minor version
        (?P<type>[xXrRsS])?     # version type (optional)
        (?P<build>\d+)?         # build (optional)
        """,
        re.VERBOSE,
    )
    re_service_build_respin = re.compile(
        r"""
        (?P<service>[sSdD])?        # service (optional)
        (?P<service_build>\d+)?     # service build (optional)
        \.?                     
        (?P<service_respin>\d+)?    # service respin (optional)
        """,
        re.VERBOSE,
    )
    # Set empty params for service pieces and complete them if a second indice exists from the version split
    # Define isservice, isfrs, isspecial, ismaintenance
    parsed_version = {
        "isservice": False,
        "ismaintenance": False,
        "isfrs": False,
        "isspecial": False,
        "service": None,
        "service_build": None,
        "service_respin": None,
    }

    # Juniper junos marks the division between main, minor, type and build from the service build and respin with a -
    version_core_part, *version_service_part = re.split("-|:", version)

    # Parse out junos into sections that can be used for logic
    parsed_version.update(re_main_minor_type_build.search(version_core_part).groupdict())

    if version_service_part:
        parsed_version.update(re_service_build_respin.search(version_service_part[0]).groupdict())
        if parsed_version.get("service", "").lower() == "s":
            parsed_version["isservice"] = True
        # Juniper looks at the D in special releases like it's the R in normal releases; Use it as the frs identifier
        elif parsed_version.get("service").lower() == "d" and (
            parsed_version.get("service_build") is None or int(parsed_version.get("service_build", 1)) <= 1
        ):
            parsed_version["isfrs"] = True

    if parsed_version.get("type") is None:
        return parsed_version

    if parsed_version["type"].lower() == "x":
        parsed_version["isspecial"] = True
    elif parsed_version["type"].lower() == "s":
        parsed_version["isservice"] = True

    if parsed_version["type"].lower() == "r" and (parsed_version.get("build") or int(parsed_version.get("build")) <= 1):
        parsed_version["isfrs"] = True
    else:
        parsed_version["ismaintenance"] = True

    return parsed_version


version_parser_vendor_platform = {
    "juniper": {
        "junos": juniper_junos_version_parser,
    }
}


def get_nist_urls_juniper_junos(platform, api_key: str) -> t.List[str]:
    """Create a list of possible NIST Url strings for JuniperPlatform.

    Args:
        api_key: NIST-API-KEY - Request here https://nvd.nist.gov/developers/request-an-api-key

    Returns:
        List of NIST CPE URLs that may contain platform data.

    Examples:
        >>> JuniperPlatform('junos','12.1R3-S4.3').get_nist_urls('YOURKEY')
        ['https://services.nvd.nist.gov/rest/json/cpes/1.0?apiKey=YOURKEY&addOns=cves&cpeMatchString=cpe:2.3:o:juniper:junos:12.1R3:S4.3:*:*:*:*:*:*', 'https://services.nvd.nist.gov/rest/json/cpes/1.0?apiKey=YOURKEY&addOns=cves&cpeMatchString=cpe:2.3:o:juniper:junos:12.1R3-S4.3:*:*:*:*:*:*:*']

        >>> JuniperPlatform('junos','12.1').get_nist_urls('YOURKEY')
        ['https://services.nvd.nist.gov/rest/json/cpes/1.0?apiKey=YOURKEY&addOns=cves&cpeMatchString=cpe:2.3:o:juniper:junos:12.1:-:*:*:*:*:*:*']
    """
    nist_urls = []
    base_url = f"""https://services.nvd.nist.gov/rest/json/cpes/1.0?apiKey={api_key}&addOns=cves&cpeMatchString=cpe:2.3:o:juniper:junos"""

    if platform.isspecial:
        # juniper:junos:12.1x47
        base_ext = f"{base_url}:{platform.main}.{platform.minor}{platform.type.lower()}{platform.build}"
    else:
        base_ext = f"{base_url}:{platform.main}.{platform.minor}"

    # X Series (Special) Examples: 12.1x47:d40, 12.2x50:d41.1
    if platform.isspecial:
        if platform.service_respin is not None:
            # juniper:junos:12.2x50:d41.1:*:*:*:*:*:*
            nist_urls.append(f"{base_ext}:{platform.service}{platform.service_build}.{platform.service_respin}{':*'*6}")
            # juniper:junos:12.2x50-d41.1:*:*:*:*:*:*:*
            nist_urls.append(f"{base_ext}-{platform.service}{platform.service_build}.{platform.service_respin}{':*'*7}")
        else:
            # juniper:junos:12.1x47:d40:*:*:*:*:*:*
            nist_urls.append(f"{base_ext}:{platform.service}{platform.service_build}{':*'*6}")
            # juniper:junos:12.1x47-d40:*:*:*:*:*:*:*
            nist_urls.append(f"{base_ext}-{platform.service}{platform.service_build}{':*'*7}")
        return nist_urls

    if platform.type is None:
        # juniper:junos:12.1:-:*:*:*:*:*:*
        nist_urls.append(f"{base_ext}:-{':*'*6}")
        return nist_urls

    if platform.build is None:
        # juniper:junos:10.4s:*:*:*:*:*:*:*
        nist_urls.append(f"{base_ext}{platform.type}{':*'*7}")
        return nist_urls

    if platform.build is not None and platform.service is None:
        # juniper:junos:12.3r12:*:*:*:*:*:*:*
        nist_urls.append(f"{base_ext}{platform.type}{platform.build}{':*'*7}")
        # juniper:junos:12.2:r1:*:*:*:*:*:*
        nist_urls.append(f"{base_ext}:{platform.type}{platform.build}{':*'*6}")
        return nist_urls

    if platform.service is not None and platform.service_respin is not None:
        # juniper:junos:11.4r13:s2.1:*:*:*:*:*:*
        nist_urls.append(
            f"{base_ext}{platform.type}{platform.build}:{platform.service}{platform.service_build}.{platform.service_respin}{':*'*6}"
        )
        # juniper:junos:12.2:r8-s2.1:*:*:*:*:*:*
        nist_urls.append(
            f"{base_ext}{platform.type}{platform.build}-{platform.service}{platform.service_build}.{platform.service_respin}{':*'*7}"
        )
        return nist_urls

    if platform.service is not None:
        # juniper:junos:11.4r13:s2:*:*:*:*:*:*
        nist_urls.append(
            f"{base_ext}{platform.type}{platform.build}:{platform.service}{platform.service_build}{':*'*6}"
        )
        # juniper:junos:12.2:r8-s2:*:*:*:*:*:*
        nist_urls.append(
            f"{base_ext}{platform.type}{platform.build}-{platform.service}{platform.service_build}{':*'*7}"
        )
        return nist_urls

    raise EOFError


def get_nist_urls_default(self, api_key: str) -> t.List[str]:
    r"""Create a list of possible NIST Url strings.

    Child models with NIST URL customizations need their own "get_nist_urls" method.

    Args:
        api_key: NIST-API-KEY - Request here https://nvd.nist.gov/developers/request-an-api-key

    Returns:
        List of NIST CPE URLs that may contain platform data.

    Examples:
        >>> OSPlatform('cisco','nxos','15.1(7)').get_nist_urls('YOURKEY')
        ['https://services.nvd.nist.gov/rest/json/cpes/1.0?apiKey=YOURKEY&addOns=cves&cpeMatchString=cpe:2.3:o:cisco:nxos:15.1\\(7\\):*:*:*:*:*:*:*']
    """
    nist_urls = []
    escape_list = [r"\(", r"\)"]
    base_url = (
        f"""https://services.nvd.nist.gov/rest/json/cpes/1.0?apiKey={api_key}&addOns=cves&cpeMatchString=cpe:2.3:o:"""
    )

    for escape_char in escape_list:
        if re.search(escape_char, self.version):
            self.version = re.sub(escape_char, "\\" + escape_char, self.version)
    nist_urls.append(f"{base_url}{self.vendor}:{self.platform}:{self.version.replace('-', ':')}{':*'*7}")

    return nist_urls


vendor_platform_to_nist_url_fn = {"default": get_nist_urls_default, "juniper": {"junos": get_nist_urls_juniper_junos}}

fields_vendor_platform = {
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
    class_fields.extend(fields_vendor_platform["default"])
    vendor_platform_fields = fields_vendor_platform.get(vendor, {}).get(platform, [])
    class_fields.extend(vendor_platform_fields)

    version_parser = version_parser_vendor_platform.get(vendor, {}).get(platform, None)
    field_values = {
        "vendor": vendor,
        "os_type": platform,
        "version_string": version,
    }
    if version_parser:
        field_values.update(version_parser(version))

    class_name = f"{vendor.capitalize()}{platform.capitalize()}"
    get_nist_url_fn = (
        vendor_platform_to_nist_url_fn.get(vendor, {}).get(platform, None) or vendor_platform_to_nist_url_fn["default"]
    )

    platform_obj = make_dataclass(
        cls_name=class_name, fields=class_fields, namespace={"get_nist_urls": get_nist_url_fn, "asdict": asdict}
    )
    return platform_obj(**field_values)


version = "12.3R4"
jp = create_platform_object("juniper", "junos", version)
print(jp.get_nist_urls("aaa"))
print(version, jp.asdict())
version = "12.1x47:d40"
jp = create_platform_object("juniper", "junos", version)
print(version, jp.asdict())
version = "12.1R3-S4.1"
jp = create_platform_object("juniper", "junos", version)
print(version, jp.asdict())
version = "12.1"
jp = create_platform_object("juniper", "junos", version)
print(version, jp.asdict())
