"""Test for the lib_mapper definitions."""

import pytest

from netutils import lib_mapper
from netutils.config.compliance import parser_map

LIBRARIES = ["ANSIBLE", "NETMIKO", "NTCTEMPLATES", "NAPALM", "PYATS", "PYNTC", "HIERCONFIG", "NETUTILSPARSER"]


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
    _mapper = getattr(lib_mapper, f"{lib}_LIB_MAPPER").copy()
    if lib == "NAPALM":
        _mapper.pop("nxos_ssh")
    mapper = dict((v, k) for k, v in _mapper.items())
    rev_mapper = getattr(lib_mapper, f"{lib}_LIB_MAPPER_REVERSE")
    if lib in ["ANSIBLE", "NAPALM", "PYATS", "PYNTC"]:
        rev_mapper.pop("cisco_xe")
    assert mapper == rev_mapper


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
