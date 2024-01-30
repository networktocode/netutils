"""Functions building NIST URLs from the os platform values."""
import re
import typing as t


def get_nist_urls_juniper_junos(  # pylint: disable=R0911
    os_platform_data: t.Dict[str, t.Any], api_key: str
) -> t.List[str]:
    """Create a list of possible NIST Url strings for JuniperPlatform.

    Args:
        api_key: NIST-API-KEY - Request here https://nvd.nist.gov/developers/request-an-api-key

    Returns:
        List of NIST CPE URLs that may contain platform data.
    """
    nist_urls = []
    base_url = f"""https://services.nvd.nist.gov/rest/json/cpes/1.0?apiKey={api_key}&addOns=cves&cpeMatchString=cpe:2.3:o:juniper:junos"""

    # BASE
    _main = os_platform_data.get("main")
    _minor = os_platform_data.get("minor")
    if os_platform_data["type"]:
        _type = os_platform_data["type"].lower()
    _build = os_platform_data.get("build")

    # SERVICE
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


def get_nist_urls_default(os_platform_data: t.Dict[str, t.Any], api_key: str) -> t.List[str]:
    r"""Create a list of possible NIST Url strings.

    Child models with NIST URL customizations need their own "get_nist_urls" method.

    Args:
        api_key: NIST-API-KEY - Request here https://nvd.nist.gov/developers/request-an-api-key

    Returns:
        List of NIST CPE URLs that may contain platform data.
    """
    nist_urls = []
    escape_list = [r"\(", r"\)"]
    base_url = (
        f"""https://services.nvd.nist.gov/rest/json/cpes/1.0?apiKey={api_key}&addOns=cves&cpeMatchString=cpe:2.3:o:"""
    )
    os_platform_data = {"base_url": base_url, **os_platform_data}
    delim_seven = ":*" * 7
    os_platform_data["version_string"] = os_platform_data.get("version_string").replace("-", ":")  # type: ignore

    version_string = os_platform_data.get("version_string", "")
    for escape_char in escape_list:
        version_string = re.sub(escape_char, "\\" + escape_char, version_string)

    os_platform_data["version_string"] = version_string

    nist_urls.append(
        f"{base_url}{os_platform_data['vendor']}:{os_platform_data['os_type']}:{os_platform_data['version_string']}{delim_seven}"
    )

    return nist_urls


get_nist_url_funcs: t.Dict[str, t.Any] = {
    "default": get_nist_urls_default,
    "juniper": {"junos": get_nist_urls_juniper_junos},
}
