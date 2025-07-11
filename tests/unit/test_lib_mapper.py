"""Test for the lib_mapper definitions."""

import pytest

from netutils import lib_mapper
from netutils.config.compliance import parser_map

LIBRARIES = [
    "AERLEON",
    "ANSIBLE",
    "CAPIRCA",
    "FORWARDNETWORKS",
    "HIERCONFIG",
    "NETMIKO",
    "NETUTILSPARSER",
    "NTCTEMPLATES",
    "NAPALM",
    "PYATS",
    "PYNTC",
    "SCRAPLI",
]

MAPPERS = {}
REVERSE_MAPPERS = {}

# Collect all variables ending with _LIB_MAPPER and _LIB_MAPPER_REVERSE
for name in dir(lib_mapper):
    value = getattr(lib_mapper, name)

    if not isinstance(value, dict) or any(
        name.startswith(prefix) for prefix in ["NAME_TO", "KEY_TO", "_", "MAIN", "DNA_CENTER"]
    ):
        continue
    if name.endswith("_LIB_MAPPER") and isinstance(value, dict):
        lib_name = name.replace("_LIB_MAPPER", "").lower()
        MAPPERS[lib_name] = value
    elif name.endswith("_LIB_MAPPER_REVERSE") and isinstance(value, dict):
        lib_name = name.replace("_LIB_MAPPER_REVERSE", "").lower()
        REVERSE_MAPPERS[lib_name] = value


def test_lib_mapper():
    assert len(lib_mapper.MAIN_LIB_MAPPER.keys()) > 40
    assert len(lib_mapper.ANSIBLE_LIB_MAPPER.keys()) > 10
    assert len(lib_mapper.NETMIKO_LIB_MAPPER.keys()) > 30
    assert len(lib_mapper.NTCTEMPLATES_LIB_MAPPER.keys()) > 30
    assert len(lib_mapper.NAPALM_LIB_MAPPER.keys()) > 4
    assert len(lib_mapper.PYATS_LIB_MAPPER.keys()) > 10
    assert len(lib_mapper.PYNTC_LIB_MAPPER.keys()) > 5
    assert len(lib_mapper.HIERCONFIG_LIB_MAPPER.keys()) > 4
    assert len(lib_mapper.NETUTILSPARSER_LIB_MAPPER.keys()) > 10
    assert lib_mapper.ANSIBLE_LIB_MAPPER["cisco.ios.ios"] == "cisco_ios"
    assert lib_mapper.NAPALM_LIB_MAPPER["ios"] == "cisco_ios"
    assert lib_mapper.PYNTC_LIB_MAPPER["arista_eos_eapi"] == "arista_eos"
    assert lib_mapper.NAPALM_LIB_MAPPER_REVERSE[lib_mapper.ANSIBLE_LIB_MAPPER["cisco.ios.ios"]] == "ios"
    assert lib_mapper.HIERCONFIG_LIB_MAPPER["ios"] == "cisco_ios"
    assert lib_mapper.HIERCONFIG_LIB_MAPPER_REVERSE[lib_mapper.HIERCONFIG_LIB_MAPPER["ios"]] == "ios"
    assert lib_mapper.FORWARDNETWORKS_LIB_MAPPER["IOS"] == "cisco_ios"
    assert lib_mapper.FORWARDNETWORKS_LIB_MAPPER_REVERSE[lib_mapper.FORWARDNETWORKS_LIB_MAPPER["IOS"]] == "IOS"


@pytest.mark.parametrize("lib", LIBRARIES)
def test_lib_mapper_reverse(lib):
    """Test that the forward is same as reverse, some accommodations must be made."""
    rev_mapper = getattr(lib_mapper, f"{lib}_LIB_MAPPER_REVERSE").copy()
    _mapper = getattr(lib_mapper, f"{lib}_LIB_MAPPER").copy()
    if lib == "NAPALM":
        _mapper.pop("nxos_ssh")
    if lib == "NETMIKO":
        _mapper.pop("f5_ltm")
        _mapper.pop("f5_tmsh")
        _mapper.pop("f5_linux")
    if lib == "NTCTEMPLATES":
        _mapper.pop("f5_ltm")
        _mapper.pop("f5_tmsh")
        _mapper.pop("f5_linux")
        _mapper.pop("cisco_xe")
    if lib in [
        "AERLEON",
        "ANSIBLE",
        "CAPIRCA",
        "FORWARDNETWORKS",
        "HIERCONFIG",
        "NETUTILSPARSER",
        "NTCTEMPLATES",
        "NAPALM",
        "PYATS",
        "PYNTC",
        "SCRAPLI",
    ]:
        rev_mapper.pop("cisco_xe")
    if lib in ["HIERCONFIG"]:
        _mapper.pop("iosxe")
    if lib in ["FORWARDNETWORKS"]:
        _mapper.pop("LINUX_OVS_OFCTL")
        _mapper.pop("IOS_XE")
        _mapper.pop("SRX")
    if lib in ["AERLEON", "CAPIRCA"]:
        _mapper.pop("juniperevo")
        _mapper.pop("srx")
        _mapper.pop("srxlo")
        _mapper.pop("msmpc")
        _mapper.pop("windows_advfirewall")
    mapper = dict((v, k) for k, v in _mapper.items())

    assert mapper == rev_mapper


def test_lib_mapper_ntctemplates_reverse_only():
    """Cisco XE is the only one that has a reverse ONLY mapping."""
    assert lib_mapper.NTCTEMPLATES_LIB_MAPPER_REVERSE["cisco_xe"] == "cisco_ios"
    assert lib_mapper.NTCTEMPLATES_LIB_MAPPER_REVERSE["cisco_ios"] == "cisco_ios"
    assert lib_mapper.NTCTEMPLATES_LIB_MAPPER["cisco_ios"] == "cisco_ios"
    assert lib_mapper.NTCTEMPLATES_LIB_MAPPER["cisco_xe"] == "cisco_xe"


def test_name_to_all_lib_mapper():
    """Test that the data structure returns as expected in NAME_TO_ALL_LIB_MAPPER."""
    assert lib_mapper.NAME_TO_ALL_LIB_MAPPER["arista_eos"]["ansible"] == "arista.eos.eos"
    assert lib_mapper.NAME_TO_ALL_LIB_MAPPER["arista_eos"]["pyntc"] == "arista_eos_eapi"
    assert lib_mapper.NAME_TO_ALL_LIB_MAPPER["cisco_ios"]["dna_center"] == "IOS"


@pytest.mark.parametrize("lib", LIBRARIES)
def test_lib_mapper_alpha(lib):
    original = list(getattr(lib_mapper, f"{lib}_LIB_MAPPER").keys())
    sorted_keys = sorted(original)
    rev_original = list(getattr(lib_mapper, f"{lib}_LIB_MAPPER_REVERSE").keys())
    rev_sorted_keys = sorted(rev_original)
    assert original == sorted_keys
    assert rev_original == rev_sorted_keys


def test_netutils_parser():
    """Test that the parser_map in compliance have been added to NETUTILSPARSER lib mappers."""
    assert parser_map.keys() == lib_mapper.NETUTILSPARSER_LIB_MAPPER.keys()
    assert list(parser_map.keys()) == sorted(list(lib_mapper.NETUTILSPARSER_LIB_MAPPER.keys()))


@pytest.mark.parametrize("lib", LIBRARIES)
def test_lib_mapper_normalized_name(lib):
    """Ensure that MAIN_LIB_MAPPER is kept up to date."""
    for key in getattr(lib_mapper, f"{lib}_LIB_MAPPER_REVERSE").keys():
        assert key in lib_mapper.MAIN_LIB_MAPPER
    for attr in getattr(lib_mapper, f"{lib}_LIB_MAPPER").values():
        assert attr in lib_mapper.MAIN_LIB_MAPPER


def test_all_mappers_included():
    """Ensure NAME_TO_LIB_MAPPER includes all _LIB_MAPPER dictionaries."""
    expected_libs = set(MAPPERS.keys())
    actual_libs = {lib.replace("_", "") for lib in lib_mapper.NAME_TO_LIB_MAPPER.keys()}

    # Check for missing libraries
    missing = expected_libs - actual_libs
    assert len(missing) == 0, f"NAME_TO_LIB_MAPPER is missing libraries: {missing}"


def test_all_reverse_mappers_included():
    """Ensure NAME_TO_LIB_MAPPER_REVERSE includes all _LIB_MAPPER_REVERSE dictionaries."""
    expected_libs = set(MAPPERS.keys())
    actual_libs = {lib.replace("_", "") for lib in lib_mapper.NAME_TO_LIB_MAPPER_REVERSE.keys()}

    # Check for missing libraries
    missing = expected_libs - actual_libs
    assert len(missing) == 0, f"NAME_TO_LIB_MAPPER_REVERSE is missing libraries: {missing}"
