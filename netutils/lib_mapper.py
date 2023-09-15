"""Variable definitions to map from network automation library to network automation library."""

import copy
import typing as t

_NETMIKO_LIB_MAPPER: t.Dict[str, t.Dict[str, str]] = {
    "a10": {},
    "accedian": {},
    "adtran_os": {},
    "alcatel_aos": {},
    "alcatel_sros": {},
    "apresia_aeos": {},
    "arista_eos": {},
    "aruba_os": {},
    "aruba_osswitch": {},
    "aruba_procurve": {},
    "avaya_ers": {},
    "avaya_vsp": {},
    "allied_telesis_awplus": {},
    "broadcom_icos": {},
    "brocade_fos": {},
    "brocade_fastiron": {},
    "brocade_netiron": {},
    "brocade_nos": {},
    "brocade_vdx": {},
    "brocade_vyos": {},
    "checkpoint_gaia": {},
    "calix_b6": {},
    "centec_os": {},
    "ciena_saos": {},
    "cisco_asa": {},
    "cisco_ftd": {},
    "cisco_ios": {},
    "cisco_nxos": {},
    "cisco_s300": {},
    "cisco_tp": {},
    "cisco_wlc": {},
    "cisco_xe": {},
    "cisco_xr": {},
    "cloudgenix_ion": {},
    "coriant": {},
    "dell_dnos9": {},
    "dell_force10": {},
    "dell_os6": {},
    "dell_os9": {},
    "dell_os10": {},
    "dell_powerconnect": {},
    "dell_isilon": {},
    "dlink_ds": {},
    "endace": {},
    "eltex": {},
    "eltex_esr": {},
    "enterasys": {},
    "ericsson_ipos": {},
    "extreme": {},
    "extreme_ers": {},
    "extreme_exos": {},
    "extreme_netiron": {},
    "extreme_nos": {},
    "extreme_slx": {},
    "extreme_vdx": {},
    "extreme_vsp": {},
    "extreme_wing": {},
    "f5_ltm": {},
    "f5_tmsh": {},
    "f5_linux": {},
    "flexvnf": {},
    "fortinet": {},
    "generic": {},
    "generic_termserver": {},
    "hp_comware": {},
    "hp_procurve": {},
    "huawei": {},
    "huawei_smartax": {},
    "huawei_olt": {},
    "huawei_vrpv8": {},
    "ipinfusion_ocnos": {},
    "juniper": {},
    "juniper_junos": {},
    "juniper_screenos": {},
    "keymile": {},
    "keymile_nos": {},
    "linux": {},
    "mikrotik_routeros": {},
    "mikrotik_switchos": {},
    "mellanox": {},
    "mellanox_mlnxos": {},
    "mrv_lx": {},
    "mrv_optiswitch": {},
    "netapp_cdot": {},
    "netgear_prosafe": {},
    "netscaler": {},
    "nokia_sros": {},
    "oneaccess_oneos": {},
    "ovs_linux": {},
    "paloalto_panos": {},
    "pluribus": {},
    "quanta_mesh": {},
    "rad_etx": {},
    "raisecom_roap": {},
    "ruckus_fastiron": {},
    "ruijie_os": {},
    "sixwind_os": {},
    "sophos_sfos": {},
    "tplink_jetstream": {},
    "ubiquiti_edge": {},
    "ubiquiti_edgerouter": {},
    "ubiquiti_edgeswitch": {},
    "ubiquiti_unifiswitch": {},
    "vyatta_vyos": {},
    "vyos": {},
    "watchguard_fireware": {},
    "zte_zxros": {},
    "yamaha": {},
}
# netmiko is the base name, so every key is a value, this ensure that.
NETMIKO_LIB_MAPPER = {key: key for key in sorted(_NETMIKO_LIB_MAPPER)}

# ntc templates is primarily based on netmiko, so a copy is in order
_NTCTEMPLATES_LIB_MAPPER = copy.deepcopy(NETMIKO_LIB_MAPPER)
_NTCTEMPLATES_LIB_MAPPER["aruba_aoscx"] = "aruba_aoscx"
_NTCTEMPLATES_LIB_MAPPER["huawei_vrp"] = "huawei_vrp"
_NTCTEMPLATES_LIB_MAPPER["vmware_nsxv"] = "vmware_nsxv"
_NTCTEMPLATES_LIB_MAPPER["watchguard_firebox"] = "watchguard_firebox"
NTCTEMPLATES_LIB_MAPPER = {key: _NTCTEMPLATES_LIB_MAPPER[key] for key in sorted(_NTCTEMPLATES_LIB_MAPPER)}

NAPALM_LIB_MAPPER = {
    "aoscx": "aruba_aoscx",
    "asa": "cisco_asa",
    "cisco_wlc_ssh": "cisco_wlc",
    "eos": "arista_eos",
    "f5": "bigip_f5",
    "fortios": "fortinet",
    "huawei": "huawei_vrp",
    "ios": "cisco_ios",
    "iosxr": "cisco_xr",
    "junos": "juniper_junos",
    "nxos": "cisco_nxos",
    "nxos_ssh": "cisco_nxos",
    "panos": "paloalto_panos",
    "ros": "mikrotik_routeros",
    "sros": "nokia_sros",
    "vyos": "brocade_vyos",
}

PYNTC_LIB_MAPPER = {
    "arista_eos_eapi": "arista_eos",
    "cisco_aireos_ssh": "cisco_wlc",
    "cisco_asa_ssh": "cisco_asa",
    "cisco_ios_ssh": "cisco_ios",
    "cisco_nxos_nxapi": "cisco_nxos",
    "f5_tmos_icontrol": "f5_tmsh",
    "juniper_junos_netconf": "juniper_junos",
}

ANSIBLE_LIB_MAPPER = {
    "arista.eos.eos": "arista_eos",
    "arubanetworks.aoscx": "aruba_aoscx",
    "ciena.saos6.saos6": "ciena_saos",
    "cisco.asa.asa": "cisco_asa",
    "cisco.ios.ios": "cisco_ios",
    "cisco.iosxr.iosxr": "cisco_xr",
    "cisco.nxos.nxos": "cisco_nxos",
    "community.network.ce": "huawei",
    "community.network.cnos": "lenovo_cnos",
    "community.network.enos": "lenovo_enos",
    "community.network.eric_eccli": "ericsson_ipos",
    "community.network.exos": "extreme_exos",
    "community.network.icx": "ruckus_icx",
    "community.network.ironware": "extreme_netiron",
    "community.network.netvisor": "pluribus",
    "community.network.nos": "extreme_nos",
    "community.network.routeros": "mikrotik_routeros",
    "community.network.slxos": "extreme_slx",
    "community.network.sros": "nokia_sros",
    "community.network.voss": "extreme_vsp",
    "dellemc.os10.0s10": "dell_os10",
    "dellemc.os6.os6": "dell_os6",
    "dellemc.os9.os9": "dell_os9",
    "junipernetworks.junos.junos": "juniper_junos",
    "vyos.vyos.vyos": "vyos",
}

PYATS_LIB_MAPPER = {
    "asa": "cisco_asa",
    "bigip": "f5_tmsh",
    "dnac": "cisco_dnac",
    "ios": "cisco_ios",
    "iosxe": "cisco_ios",
    "iosxr": "cisco_xr",
    "junos": "juniper_junos",
    "linux": "linux",
    "nxos": "cisco_nxos",
    "sros": "nokia_sros",
    "viptela": "cisco_viptella",
}

SCRAPLI_LIB_MAPPER = {
    "arista_eos": "arista_eos",
    "aruba_aoscx": "aruba_aoscx",
    "cisco_iosxe": "cisco_ios",
    "cisco_iosxr": "cisco_xr",
    "cisco_nxos": "cisco_nxos",
    "juniper_junos": "juniper_junos",
}

HIERCONFIG_LIB_MAPPER = {
    "eos": "arista_eos",
    "fastiron": "ruckus_fastiron",
    "ios": "cisco_ios",
    "iosxe": "cisco_xe",
    "iosxr": "cisco_xr",
    "nxos": "cisco_nxos",
}

NETUTILSPARSER_LIB_MAPPER = {
    "arista_eos": "arista_eos",
    "aruba_aoscx": "aruba_aoscx",
    "bigip_f5": "bigip_f5",
    "cisco_aireos": "cisco_aireos",
    "cisco_asa": "cisco_asa",
    "cisco_ios": "cisco_ios",
    "cisco_iosxr": "cisco_iosxr",
    "cisco_nxos": "cisco_nxos",
    "citrix_netscaler": "citrix_netscaler",
    "extreme_netiron": "extreme_netiron",
    "fortinet_fortios": "fortinet_fortios",
    "juniper_junos": "juniper_junos",
    "linux": "linux",
    "mikrotik_routeros": "mikrotik_routeros",
    "mrv_optiswitch": "mrv_optiswitch",
    "netscaler": "netscaler",
    "nokia_sros": "nokia_sros",
    "paloalto_panos": "paloalto_panos",
    "ruckus_fastiron": "ruckus_fastiron",
    "ubiquiti_airos": "ubiquiti_airos",
}

NAPALM_LIB_MAPPER_REVERSE = {
    "arista_eos": "eos",
    "aruba_aoscx": "aoscx",
    "bigip_f5": "f5",
    "brocade_vyos": "vyos",
    "cisco_asa": "asa",
    "cisco_ios": "ios",
    "cisco_nxos": "nxos",
    "cisco_wlc": "cisco_wlc_ssh",
    "cisco_xr": "iosxr",
    "fortinet": "fortios",
    "huawei_vrp": "huawei",
    "juniper_junos": "junos",
    "mikrotik_routeros": "ros",
    "nokia_sros": "sros",
    "paloalto_panos": "panos",
}

PYNTC_LIB_MAPPER_REVERSE = {
    "arista_eos": "arista_eos_eapi",
    "cisco_asa": "cisco_asa_ssh",
    "cisco_ios": "cisco_ios_ssh",
    "cisco_nxos": "cisco_nxos_nxapi",
    "cisco_wlc": "cisco_aireos_ssh",
    "f5_tmsh": "f5_tmos_icontrol",
    "juniper_junos": "juniper_junos_netconf",
}

ANSIBLE_LIB_MAPPER_REVERSE = {
    "arista_eos": "arista.eos.eos",
    "aruba_aoscx": "arubanetworks.aoscx",
    "ciena_saos": "ciena.saos6.saos6",
    "cisco_asa": "cisco.asa.asa",
    "cisco_ios": "cisco.ios.ios",
    "cisco_nxos": "cisco.nxos.nxos",
    "cisco_xr": "cisco.iosxr.iosxr",
    "dell_os10": "dellemc.os10.0s10",
    "dell_os6": "dellemc.os6.os6",
    "dell_os9": "dellemc.os9.os9",
    "ericsson_ipos": "community.network.eric_eccli",
    "extreme_exos": "community.network.exos",
    "extreme_netiron": "community.network.ironware",
    "extreme_nos": "community.network.nos",
    "extreme_slx": "community.network.slxos",
    "extreme_vsp": "community.network.voss",
    "huawei": "community.network.ce",
    "juniper_junos": "junipernetworks.junos.junos",
    "lenovo_cnos": "community.network.cnos",
    "lenovo_enos": "community.network.enos",
    "mikrotik_routeros": "community.network.routeros",
    "nokia_sros": "community.network.sros",
    "pluribus": "community.network.netvisor",
    "ruckus_icx": "community.network.icx",
    "vyos": "vyos.vyos.vyos",
}

PYATS_LIB_MAPPER_REVERSE = {
    "cisco_asa": "asa",
    "cisco_dnac": "dnac",
    "cisco_ios": "iosxe",
    "cisco_nxos": "nxos",
    "cisco_viptella": "viptela",
    "cisco_xr": "iosxr",
    "f5_tmsh": "bigip",
    "juniper_junos": "junos",
    "linux": "linux",
    "nokia_sros": "sros",
}

SCRAPLI_LIB_MAPPER_REVERSE = {
    "arista_eos": "arista_eos",
    "aruba_aoscx": "aruba_aoscx",
    "cisco_ios": "cisco_iosxe",
    "cisco_nxos": "cisco_nxos",
    "cisco_xr": "cisco_iosxr",
    "juniper_junos": "juniper_junos",
}

HIERCONFIG_LIB_MAPPER_REVERSE = {
    "arista_eos": "eos",
    "cisco_ios": "ios",
    "cisco_nxos": "nxos",
    "cisco_xe": "iosxe",
    "cisco_xr": "iosxr",
    "ruckus_fastiron": "fastiron",
}

NETUTILSPARSER_LIB_MAPPER_REVERSE = {
    "arista_eos": "arista_eos",
    "aruba_aoscx": "aruba_aoscx",
    "bigip_f5": "bigip_f5",
    "cisco_aireos": "cisco_aireos",
    "cisco_asa": "cisco_asa",
    "cisco_ios": "cisco_ios",
    "cisco_iosxr": "cisco_iosxr",
    "cisco_nxos": "cisco_nxos",
    "citrix_netscaler": "citrix_netscaler",
    "extreme_netiron": "extreme_netiron",
    "fortinet_fortios": "fortinet_fortios",
    "juniper_junos": "juniper_junos",
    "linux": "linux",
    "mikrotik_routeros": "mikrotik_routeros",
    "mrv_optiswitch": "mrv_optiswitch",
    "netscaler": "netscaler",
    "nokia_sros": "nokia_sros",
    "paloalto_panos": "paloalto_panos",
    "ruckus_fastiron": "ruckus_fastiron",
    "ubiquiti_airos": "ubiquiti_airos",
}

# Deep copy the reverse, where there is no actual translation happening.
NETMIKO_LIB_MAPPER_REVERSE = copy.deepcopy(NETMIKO_LIB_MAPPER)
NTCTEMPLATES_LIB_MAPPER_REVERSE = copy.deepcopy(NTCTEMPLATES_LIB_MAPPER)

# Deep copy the reverse, where there is no actual translation happening with special
# consideration for OS's not in netmiko.
_MAIN_LIB_MAPPER = copy.deepcopy(NETMIKO_LIB_MAPPER)
_MAIN_LIB_MAPPER["aruba_aoscx"] = "aruba_aoscx"
_MAIN_LIB_MAPPER["cisco_dnac"] = "cisco_dnac"
_MAIN_LIB_MAPPER["cisco_viptella"] = "cisco_viptella"
_MAIN_LIB_MAPPER["huawei_vrp"] = "huawei_vrp"
_MAIN_LIB_MAPPER["lenovo_cnos"] = "lenovo_cnos"
_MAIN_LIB_MAPPER["lenovo_enos"] = "lenovo_enos"
_MAIN_LIB_MAPPER["ruckus_icx"] = "ruckus_icx"
_MAIN_LIB_MAPPER["ruckus_smartzone"] = "ruckus_smartzone"
_MAIN_LIB_MAPPER["vmware_nsxv"] = "vmware_nsxv"
_MAIN_LIB_MAPPER["watchguard_firebox"] = "watchguard_firebox"
MAIN_LIB_MAPPER = {key: _MAIN_LIB_MAPPER[key] for key in sorted(_MAIN_LIB_MAPPER)}
