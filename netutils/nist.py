"""Functions building NIST URLs from the os platform values."""
import re
import typing as t


def get_nist_urls_juniper_junos(os_platform_data: t.Dict[str, t.Any], api_key: str) -> t.List[str]:
    """Create a list of possible NIST Url strings for JuniperPlatform.

    Args:
        api_key: NIST-API-KEY - Request here https://nvd.nist.gov/developers/request-an-api-key

    Returns:
        List of NIST CPE URLs that may contain platform data.
    """
    nist_urls = []
    base_url = f"""https://services.nvd.nist.gov/rest/json/cpes/1.0?apiKey={api_key}&addOns=cves&cpeMatchString=cpe:2.3:o:juniper:junos"""

    url_args = {"base_url": base_url, **os_platform_data}
    url_args["delim_six"] = ":*" * 6
    url_args["delim_seven"] = ":*" * 7

    if os_platform_data.get("isspecial"):
        url_args["type"] = url_args.get("type").lower()  # type: ignore
        # juniper:junos:12.1x47
        base_ext = f"{url_args['base_url']}:{url_args.get('main')}.{url_args.get('minor')}{url_args.get('type')}{url_args.get('build')}"
    else:
        base_ext = f"{url_args['base_url']}:{url_args.get('main')}.{url_args.get('minor')}"

    url_args["base_ext"] = base_ext

    # X Series (Special) Examples: 12.1x47:d40, 12.2x50:d41.1
    if url_args["isspecial"]:
        if url_args["service_respin"] is not None:
            # juniper:junos:12.2x50:d41.1:*:*:*:*:*:*
            nist_urls.append(
                f"{url_args['base_ext']}:{url_args.get('service')}{url_args.get('service_build')}.{url_args.get('service_respin')}{url_args['delim_six']}"
            )
            # juniper:junos:12.2x50-d41.1:*:*:*:*:*:*:*
            nist_urls.append(
                f"{url_args['base_ext']}-{url_args.get('service')}{url_args.get('service_build')}.{url_args.get('service_respin')}{url_args['delim_seven']}"
            )
        else:
            # juniper:junos:12.1x47:d40:*:*:*:*:*:*
            nist_urls.append(
                f"{url_args['base_ext']}:{url_args.get('service')}{url_args.get('service_build')}{url_args['delim_six']}"
            )
            # juniper:junos:12.1x47-d40:*:*:*:*:*:*:*
            nist_urls.append(
                f"{url_args['base_ext']}-{url_args.get('service')}{url_args.get('service_build')}{url_args['delim_seven']}"
            )
        return nist_urls

    if url_args.get("type") is None:
        # juniper:junos:12.1:-:*:*:*:*:*:*
        nist_urls.append(f"{url_args['base_ext']}:-{url_args['delim_six']}")
        return nist_urls

    if url_args.get("build") is None:
        # juniper:junos:10.4s:*:*:*:*:*:*:*
        nist_urls.append(f"{url_args['base_ext']}{url_args.get('type')}{url_args['delim_seven']}")
        return nist_urls

    if url_args.get("build") is not None and url_args.get("service") is None:
        # juniper:junos:12.3r12:*:*:*:*:*:*:*
        nist_urls.append(
            f"{url_args['base_ext']}{url_args.get('type')}{url_args.get('build')}{url_args['delim_seven']}"
        )
        # juniper:junos:12.2:r1:*:*:*:*:*:*
        nist_urls.append(f"{url_args['base_ext']}:{url_args.get('type')}{url_args.get('build')}{url_args['delim_six']}")
        return nist_urls

    if url_args.get("service") is not None and url_args.get("service_respin") is not None:
        # juniper:junos:11.4r13:s2.1:*:*:*:*:*:*
        nist_urls.append(
            f"{url_args['base_ext']}{url_args.get('type')}{url_args.get('build')}:{url_args.get('service')}{url_args.get('service_build')}.{url_args.get('service_respin')}{url_args['delim_six']}"
        )
        # juniper:junos:12.2:r8-s2.1:*:*:*:*:*:*
        nist_urls.append(
            f"{url_args['base_ext']}{url_args.get('type')}{url_args.get('build')}-{url_args.get('service')}{url_args.get('service_build')}.{url_args.get('service_respin')}{url_args['delim_seven']}"
        )
        return nist_urls

    if url_args.get("service") is not None:
        # juniper:junos:11.4r13:s2:*:*:*:*:*:*
        nist_urls.append(
            f"{url_args['base_ext']}{url_args.get('type')}{url_args.get('build')}:{url_args.get('service')}{url_args.get('service_build')}{url_args['delim_six']}"
        )
        # juniper:junos:12.2:r8-s2:*:*:*:*:*:*
        nist_urls.append(
            f"{url_args['base_ext']}{url_args.get('type')}{url_args.get('build')}-{url_args.get('service')}{url_args.get('service_build')}{url_args['delim_seven']}"
        )
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
    url_args = {"base_url": base_url, **os_platform_data}
    url_args["delim_seven"] = ":*" * 7
    url_args["version_string"] = url_args.get("version_string").replace("-", ":")  # type: ignore

    for escape_char in escape_list:
        if re.search(escape_char, url_args.get("version_string")):  # type: ignore
            url_args["version_string"] = re.sub(escape_char, "\\" + escape_char, url_args["version_string"])
    nist_urls.append(
        f"{url_args['base_url']}{url_args['vendor']}:{url_args['os_type']}:{url_args['version_string']}{url_args['delim_seven']}"
    )

    return nist_urls


get_nist_url_funcs: t.Dict[str, t.Any] = {
    "default": get_nist_urls_default,
    "juniper": {"junos": get_nist_urls_juniper_junos},
}
