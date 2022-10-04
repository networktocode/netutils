"""Test for the lib_helpers definitions."""

from unittest import mock

from netutils.lib_helpers import get_napalm_getters


@mock.patch("netutils.lib_helpers.get_network_driver", mock.Mock())
def test_get_napalm_getters_napalm_installed_default():
    napalm_getters = get_napalm_getters()
    assert napalm_getters == {
        "asa": {},
        "cisco_wlc_ssh": {},
        "eos": {},
        "fortios": {},
        "huawei": {},
        "ios": {},
        "iosxr": {},
        "junos": {},
        "nxos": {},
        "nxos_ssh": {},
        "panos": {},
        "sros": {},
        "vyos": {},
    }


def test_get_napalm_getters_napalm_installed_nxos_keys():
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
