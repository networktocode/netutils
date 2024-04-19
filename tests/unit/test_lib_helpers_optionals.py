"""Test for the lib_helpers definitions when optional packages are installed."""

from unittest import mock

import pytest
from netutils.lib_helpers import get_napalm_getters


def test_get_napalm_getters_napalm_installed_default():
    pytest.importorskip("napalm")
    with mock.patch("napalm.get_network_driver"):
        napalm_getters = get_napalm_getters()
        assert all(item in napalm_getters.keys() for item in ["asa", "eos", "fortios"])


def test_get_napalm_getters_napalm_installed_nxos_keys():
    pytest.importorskip("napalm")
    napalm_getters = get_napalm_getters()
    assert list(napalm_getters["nxos"].keys()) == [
        "get_arp_table",
        "get_bgp_config",
        "get_bgp_neighbors",
        "get_bgp_neighbors_detail",
        "get_config",
        "get_environment",
        "get_facts",
        "get_firewall_policies",
        "get_interfaces",
        "get_interfaces_counters",
        "get_interfaces_ip",
        "get_ipv6_neighbors_table",
        "get_lldp_neighbors",
        "get_lldp_neighbors_detail",
        "get_mac_address_table",
        "get_network_instances",
        "get_ntp_peers",
        "get_ntp_servers",
        "get_ntp_stats",
        "get_optics",
        "get_probes_config",
        "get_probes_results",
        "get_route_to",
        "get_snmp_information",
        "get_users",
        "get_vlans",
    ]
