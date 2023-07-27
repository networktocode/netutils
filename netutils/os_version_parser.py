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

    if parsed_version["type"].lower() == "r" and (
        parsed_version.get("build") is None or int(parsed_version.get("build")) <= 1
    ):
        parsed_version["isfrs"] = True
    elif parsed_version["type"].lower() == "r":
        parsed_version["ismaintenance"] = True

    return parsed_version


os_version_parsers = {
    "juniper": {
        "junos": juniper_junos_version_parser,
    }
}
