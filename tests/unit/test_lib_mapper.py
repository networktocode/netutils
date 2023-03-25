"""Test for the lib_mapper definitions."""
import pytest

from netutils import lib_mapper


def test_lib_mapper():
    assert len(lib_mapper.MAIN_LIB_MAPPER.keys()) > 40
    assert len(lib_mapper.ANSIBLE_LIB_MAPPER.keys()) > 10
    assert len(lib_mapper.NETMIKO_LIB_MAPPER.keys()) > 30
    assert len(lib_mapper.NTCTEMPLATES_LIB_MAPPER.keys()) > 30
    assert len(lib_mapper.NAPALM_LIB_MAPPER.keys()) > 4
    assert len(lib_mapper.PYATS_LIB_MAPPER.keys()) > 10
    assert len(lib_mapper.PYNTC_LIB_MAPPER.keys()) > 5
    assert len(lib_mapper.HIERCONFIG_LIB_MAPPER.keys()) > 4
    assert lib_mapper.ANSIBLE_LIB_MAPPER["cisco.ios.ios"] == "cisco_ios"
    assert lib_mapper.NAPALM_LIB_MAPPER["ios"] == "cisco_ios"
    assert lib_mapper.PYNTC_LIB_MAPPER["arista_eos_eapi"] == "arista_eos"
    assert lib_mapper.NAPALM_LIB_MAPPER_REVERSE[lib_mapper.ANSIBLE_LIB_MAPPER["cisco.ios.ios"]] == "ios"
    assert lib_mapper.HIERCONFIG_LIB_MAPPER["ios"] == "cisco_ios"
    assert lib_mapper.HIERCONFIG_LIB_MAPPER_REVERSE[lib_mapper.HIERCONFIG_LIB_MAPPER["ios"]] == "ios"


@pytest.mark.parametrize("lib", ["ANSIBLE", "NETMIKO", "NTCTEMPLATES", "NAPALM", "PYATS", "PYNTC", "HIERCONFIG"])
def test_lib_mapper_reverse(lib):
    mapper = dict((v, k) for k, v in getattr(lib_mapper, f"{lib}_LIB_MAPPER").items())
    rev_mapper = getattr(lib_mapper, f"{lib}_LIB_MAPPER_REVERSE")
    assert mapper == rev_mapper
