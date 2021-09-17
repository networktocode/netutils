"""Variable definitions to map from network automation library to network automation library."""

import copy

_NETMIKO_LIB_MAPPER = {
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
NETMIKO_LIB_MAPPER = {}
for key in list(_NETMIKO_LIB_MAPPER.keys()):
    NETMIKO_LIB_MAPPER[key] = key

# ntc templates is primarily based on netmiko, so a copy is in order
NTCTEMPLATES_LIB_MAPPER = copy.deepcopy(NETMIKO_LIB_MAPPER)
NTCTEMPLATES_LIB_MAPPER["watchguard_firebox"] = "watchguard_firebox"
NTCTEMPLATES_LIB_MAPPER["huawei_vrp"] = "huawei_vrp"
NTCTEMPLATES_LIB_MAPPER["vmware_nsxv"] = "vmware_nsxv"

NAPALM_LIB_MAPPER = {
    "asa": "cisco_asa",
    "cisco_wlc_ssh": "cisco_wlc",
    "eos": "arista_eos",
    "fortios": "fortinet",
    "huawei": "huawei_vrp",
    "ios": "cisco_ios",
    "nxos": "cisco_nxos",
    "iosxr": "cisco_xr",
    "junos": "juniper_junos",
    "panos": "paloalto_panos",
    "sros": "nokia_sros",
    "vyos": "brocade_vyos",
}

PYNTC_LIB_MAPPER = {
    "cisco_asa_ssh": "cisco_asa",
    "arista_eos_eapi": "arista_eos",
    "f5_tmos_icontrol": "f5_tmsh",
    "cisco_ios_ssh": "cisco_ios",
    "juniper_junos_netconf": "juniper_junos",
    "cisco_nxos_nxapi": "cisco_nxos",
    "cisco_aireos_ssh": "cisco_wlc",
}
ANSIBLE_LIB_MAPPER = {
    "arista.eos.eos": "arista_eos",
    "ciena.saos6.saos6": "ciena_saos",
    "cisco.asa.asa": "cisco_asa",
    "cisco.ios.ios": "cisco_ios",
    "cisco.iosxr.iosxr": "cisco_xr",
    "cisco.nxos.nxos": "cisco_nxos",
    "community.network.ce": "huawei",
    "dellemc.os6.os6": "dell_os6",
    "dellemc.os9.os9": "dell_os9",
    "dellemc.os10.0s10": "dell_os10",
    "community.network.eric_eccli": "ericsson_ipos",
    "community.network.exos": "extreme_exos",
    "community.network.ironware": "extreme_netiron",
    "community.network.nos": "extreme_nos",
    "community.network.slxos": "extreme_slx",
    "community.network.voss": "extreme_vsp",
    "junipernetworks.junos.junos": "juniper_junos",
    "community.network.cnos": "lenovo_cnos",
    "community.network.enos": "lenovo_enos",
    "community.network.routeros": "mikrotik_routeros",
    "community.network.netvisor": "pluribus",
    "community.network.icx": "ruckus_icx",
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
    "cisco_iosxe": "cisco_ios",
    "cisco_iosxr": "cisco_xr",
    "cisco_nxos": "cisco_nxos",
    "arista_eos": "arista_eos",
    "juniper_junos": "juniper_junos",
}

NAPALM_LIB_MAPPER_REVERSE = {
    "arista_eos": "eos",
    "brocade_vyos": "vyos",
    "cisco_asa": "asa",
    "cisco_ios": "ios",
    "cisco_nxos": "nxos",
    "cisco_xr": "iosxr",
    "cisco_wlc": "cisco_wlc_ssh",
    "fortinet": "fortios",
    "huawei_vrp": "huawei",
    "juniper_junos": "junos",
    "paloalto_panos": "panos",
    "nokia_sros": "sros",
}

PYNTC_LIB_MAPPER_REVERSE = {
    "cisco_asa": "cisco_asa_ssh",
    "arista_eos": "arista_eos_eapi",
    "f5_tmsh": "f5_tmos_icontrol",
    "cisco_ios": "cisco_ios_ssh",
    "juniper_junos": "juniper_junos_netconf",
    "cisco_nxos": "cisco_nxos_nxapi",
    "cisco_wlc": "cisco_aireos_ssh",
}
ANSIBLE_LIB_MAPPER_REVERSE = {
    "arista_eos": "arista.eos.eos",
    "ciena_saos": "ciena.saos6.saos6",
    "cisco_asa": "cisco.asa.asa",
    "cisco_ios": "cisco.ios.ios",
    "cisco_xr": "cisco.iosxr.iosxr",
    "cisco_nxos": "cisco.nxos.nxos",
    "huawei": "community.network.ce",
    "dell_os6": "dellemc.os6.os6",
    "dell_os9": "dellemc.os9.os9",
    "dell_os10": "dellemc.os10.0s10",
    "ericsson_ipos": "community.network.eric_eccli",
    "extreme_exos": "community.network.exos",
    "extreme_netiron": "community.network.ironware",
    "extreme_nos": "community.network.nos",
    "extreme_slx": "community.network.slxos",
    "extreme_vsp": "community.network.voss",
    "juniper_junos": "junipernetworks.junos.junos",
    "lenovo_cnos": "community.network.cnos",
    "lenovo_enos": "community.network.enos",
    "mikrotik_routeros": "community.network.routeros",
    "pluribus": "community.network.netvisor",
    "ruckus_icx": "community.network.icx",
    "vyos": "vyos.vyos.vyos",
}

PYATS_LIB_MAPPER_REVERSE = {
    "cisco_asa": "asa",
    "f5_tmsh": "bigip",
    "cisco_dnac": "dnac",
    "cisco_ios": "iosxe",
    "cisco_xr": "iosxr",
    "juniper_junos": "junos",
    "linux": "linux",
    "cisco_nxos": "nxos",
    "nokia_sros": "sros",
    "cisco_viptella": "viptela",
}

SCRAPLI_LIB_MAPPER_REVERSE = {
    "cisco_ios": "cisco_iosxe",
    "cisco_xr": "cisco_iosxr",
    "cisco_nxos": "cisco_nxos",
    "arista_eos": "arista_eos",
    "juniper_junos": "juniper_junos",
}

# Deep copy the reverse, where there is no actual translation happening.
NETMIKO_LIB_MAPPER_REVERSE = copy.deepcopy(NETMIKO_LIB_MAPPER)
NTCTEMPLATES_LIB_MAPPER_REVERSE = copy.deepcopy(NTCTEMPLATES_LIB_MAPPER)

# Deep copy the reverse, where there is no actual translation happening with special
# consideration for OS's not in netmiko.
MAIN_LIB_MAPPER = copy.deepcopy(NETMIKO_LIB_MAPPER)
MAIN_LIB_MAPPER["cisco_dnac"] = "cisco_dnac"
MAIN_LIB_MAPPER["cisco_viptella"] = "cisco_viptella"
MAIN_LIB_MAPPER["huawei_vrp"] = "huawei_vrp"
MAIN_LIB_MAPPER["lenovo_cnos"] = "lenovo_cnos"
MAIN_LIB_MAPPER["lenovo_enos"] = "lenovo_enos"
MAIN_LIB_MAPPER["ruckus_icx"] = "ruckus_icx"
MAIN_LIB_MAPPER["vmware_nsxv"] = "vmware_nsxv"
MAIN_LIB_MAPPER["watchguard_firebox"] = "watchguard_firebox"
