"""Platform Mappers."""
# The intent of this script is to take a given platform, determine the format, and reformat it for another purpose
# An example of this is a platform being formatted for NIST Database Query
import re
import typing as t

# When a platform needs mapped items for NIST URL parsing, add to the following dictionary
custom_nist_platforms = {
    "juniper": ["junos"],
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
    manufacturer = vendor.lower()
    platform = platform.lower()
    platform_obj = None

    if platform in custom_nist_platforms.get(manufacturer, {}):
        platform_obj = eval(  # pylint: disable=W0123 # nosec B307
            f"{manufacturer.capitalize()}Platform(platform, version)"
        )
    else:
        platform_obj = OSPlatform(manufacturer, platform, version)

    return platform_obj


def juniper_junos_version_parser(version: str) -> t.Dict:
    """Parses JunOS Version into usable bits matching JunOS Standars.

    Args:
        version

    Returns:
        A dictionary containing parsed version information

    Examples:
        >>> parsed_version = juniper_junos_version_parser("12.3R4")
    """
    # Parse out junos into sections that can be used for logic
    # Juniper junos marks the division between main, minor, type and build from the service build and respin with a -
    parsed_version = {}
    split_version = list(filter(None, re.split("-|:", version)))

    # Use regex to group the main, minor, type and build into useable pieces
    re_main_minor_type_build = re.search(r"^(\d+)\.(\d+)([xXrRsS])?(\d+)?", split_version[0])

    parsed_version.update({"main": re_main_minor_type_build.group(1)})  # type: ignore[union-attr]
    parsed_version.update({"minor": re_main_minor_type_build.group(2)})  # type: ignore[union-attr]
    parsed_version.update({"type": re_main_minor_type_build.group(3)})  # type: ignore[union-attr]
    parsed_version.update({"build": re_main_minor_type_build.group(4)})  # type: ignore[union-attr]

    # Set empty params for service pieces and complete them if a second indice exists from the version split
    # Define isservice, isfrs, isspecial, ismaintenance
    parsed_version.update({"isservice": False})
    parsed_version.update({"ismaintenance": False})
    parsed_version.update({"isfrs": False})
    parsed_version.update({"isspecial": False})

    parsed_version.update({"service": None})
    parsed_version.update({"service_build": None})
    parsed_version.update({"service_respin": None})

    if len(split_version) > 1:
        re_service_respin = re.search(r"([sSdD])?(\d+)?(\.)?(\d+)?", split_version[1])
        parsed_version["service"] = re_service_respin.group(1)  # type: ignore[union-attr]
        parsed_version["service_build"] = re_service_respin.group(2)  # type: ignore[union-attr]
        parsed_version["service_respin"] = re_service_respin.group(4)  # type: ignore[union-attr]

        if parsed_version.get("service").lower() == "s":
            parsed_version["isservice"] = True

        # Juniper looks at the D in special releases like it's the R in normal releases; Use it as the frs identifier
        elif parsed_version.get("service").lower() == "d":
            if parsed_version.get("service_build") is None or int(parsed_version.get("service_build")) <= 1:
                parsed_version["isfrs"] = True

    if parsed_version.get("type"):
        if parsed_version["type"].lower() == "x":
            parsed_version["isspecial"] = True
        elif parsed_version["type"].lower() == "s":
            parsed_version["isservice"] = True

        if parsed_version["type"].lower() == "r" and hasattr(parsed_version, "build"):
            if parsed_version.get("build") is None or int(parsed_version.get("build")) <= 1:
                parsed_version["isfrs"] = True
            else:
                parsed_version["ismaintenance"] = True

    return parsed_version


class OSPlatform:
    """Class to create a generic platform for identification and manipulation."""

    def __init__(self, vendor: str, platform: str, version: str):
        """Initialize OSPlatform Object with vendor, platform, and version."""
        self._properties = {"vendor": vendor, "platform": platform, "version": version}

    @property
    def vendor(self) -> str:
        return self._properties.get("vendor")

    @property
    def platform(self) -> str:
        return self._properties.get("platform")

    @property
    def version(self) -> str:
        return self._properties.get("version")

    @property
    def info(self) -> t.Dict[str, str]:
        r"""Display Platform Information.

        Can be used with any Child class that inits super().

        Returns:
            Dictionary of platform breakdown

        Examples:
            >>> OSPlatform('cisco','nxos','15.1(7)').info
            {'vendor': 'cisco', 'platform': 'nxos', 'version': '15.1(7)'}

            >>> JuniperPlatform('junos','12.1R3-S4.1').info
            {'vendor': 'juniper', 'platform': 'junos', 'version': '12.1R3-S4.1', 'isservice': True, 'ismaintenance': True, 'isfrs': False, 'isspecial': False, 'main': '12', 'minor': '1', 'type': 'R', 'build': '3', 'service': 'S', 'service_build': '4', 'service_respin': '1'}
        """
        return self.__dict__

    def get_nist_urls(self, api_key: str) -> t.List[str]:
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
        base_url = f"""https://services.nvd.nist.gov/rest/json/cpes/1.0?apiKey={api_key}&addOns=cves&cpeMatchString=cpe:2.3:o:"""

        if self.platform in custom_nist_platforms.get(self.vendor.lower(), []):
            return self.get_nist_urls(api_key)

        for escape_char in escape_list:
            if re.search(escape_char, self.version):
                self.version = re.sub(escape_char, "\\" + escape_char, self.version)
        nist_urls.append(f"{base_url}{self.vendor}:{self.platform}:{self.version.replace('-', ':')}:*:*:*:*:*:*:*")

        return nist_urls


class JuniperPlatform(OSPlatform):  # pylint: disable=R0902
    """Class for Juniper Platform additional work/info."""

    def __init__(self, platform: str, version: str):
        """Initialize JuniperPlatform Object with platform, and version."""

        super().__init__("juniper", platform, version)

        # JUNOS BREAKDOWN
        if self.platform == "junos":
            for k, v in juniper_junos_version_parser(version).items():
                self._properties.update({k: v})

    def get_nist_urls(self, api_key: str) -> t.List[str]:
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
        base_extension = f"{base_url}:{self.main}.{self.minor}"

        # X Series (Special) Examples: 12.1x47:d40, 12.2x50:d41.1
        if self.isspecial:
            # juniper:junos:12.1x47
            base_extension = f"{base_url}:{self.main}.{self.minor}{self.type.lower()}{self.build}"
            if self.service_respin is not None:
                # juniper:junos:12.2x50:d41.1:*:*:*:*:*:*
                nist_urls.append(
                    f"{base_extension}:{self.service}{self.service_build}.{self.service_respin}:*:*:*:*:*:*"
                )
                # juniper:junos:12.2x50-d41.1:*:*:*:*:*:*:*
                nist_urls.append(
                    f"{base_extension}-{self.service}{self.service_build}.{self.service_respin}:*:*:*:*:*:*:*"
                )
            else:
                # juniper:junos:12.1x47:d40:*:*:*:*:*:*
                nist_urls.append(f"{base_extension}:{self.service}{self.service_build}:*:*:*:*:*:*")
                # juniper:junos:12.1x47-d40:*:*:*:*:*:*:*
                nist_urls.append(f"{base_extension}-{self.service}{self.service_build}:*:*:*:*:*:*:*")
            return nist_urls

        if self.type is None:
            # juniper:junos:12.1:-:*:*:*:*:*:*
            nist_urls.append(f"{base_extension}:-:*:*:*:*:*:*")
            return nist_urls

        if self.build is None:
            # juniper:junos:10.4s:*:*:*:*:*:*:*
            nist_urls.append(f"{base_extension}{self.type}:*:*:*:*:*:*:*")
            return nist_urls

        if self.build is not None and self.service is None:
            # juniper:junos:12.3r12:*:*:*:*:*:*:*
            nist_urls.append(f"{base_extension}{self.type}{self.build}:*:*:*:*:*:*:*")
            # juniper:junos:12.2:r1:*:*:*:*:*:*
            nist_urls.append(f"{base_extension}:{self.type}{self.build}:*:*:*:*:*:*")
            return nist_urls

        if self.service is not None:
            if self.service_respin is not None:
                # juniper:junos:11.4r13:s2.1:*:*:*:*:*:*
                nist_urls.append(
                    f"{base_extension}{self.type}{self.build}:{self.service}{self.service_build}.{self.service_respin}:*:*:*:*:*:*"
                )
                # juniper:junos:12.2:r8-s2.1:*:*:*:*:*:*
                nist_urls.append(
                    f"{base_extension}{self.type}{self.build}-{self.service}{self.service_build}.{self.service_respin}:*:*:*:*:*:*:*"
                )
                return nist_urls

            # juniper:junos:11.4r13:s2:*:*:*:*:*:*
            nist_urls.append(f"{base_extension}{self.type}{self.build}:{self.service}{self.service_build}:*:*:*:*:*:*")
            # juniper:junos:12.2:r8-s2:*:*:*:*:*:*
            nist_urls.append(
                f"{base_extension}{self.type}{self.build}-{self.service}{self.service_build}:*:*:*:*:*:*:*"
            )
            return nist_urls

        raise EOFError


jp = JuniperPlatform("junos", "12.3R4")
print(jp.info)
print(vars(jp))
print(jp._properties)
print(jp.main)
jp.main = 13
print(jp.main)
print(jp.info)
