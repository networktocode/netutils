"""Variable definitions to map from network automation library to network automation library."""

import copy
import typing as t

# AERLEON | Normalized
AERLEON_LIB_MAPPER: t.Dict[str, str] = {
    "arista": "arista_eos",
    "aruba": "aruba_aoscx",
    "brocade": "brocade_nos",
    "cisco": "cisco_ios",
    "ciscoasa": "cisco_asa",
    "cisconx": "cisco_nxos",
    "ciscoxr": "cisco_xr",
    "cloudarmor": "cloudarmor",
    "gce": "gce",
    "gcp_hf": "gcp_hf",
    "ipset": "ipset",
    "iptables": "iptables",
    "juniper": "juniper_junos",
    "juniperevo": "juniper_junos",  # no reverse
    "k8s": "k8s",
    "msmpc": "juniper_junos",  # no reverse
    "nsxt": "vmware_nsxt",
    "nsxv": "vmware_nsxv",
    "openconfig": "openconfig",
    "packetfilter": "packetfilter",
    "paloalto": "paloalto_panos",
    "pcap": "pcap",
    "sonic": "sonic",
    "speedway": "speedway",
    "srx": "juniper_junos",  # no reverse
    "srxlo": "juniper_junos",  # no reverse
    "windows": "windows",
    "windows_advfirewall": "windows",  # no reverse
}

# Normalized | AERLEON
AERLEON_LIB_MAPPER_REVERSE: t.Dict[str, str] = {
    "arista_eos": "arista",
    "aruba_aoscx": "aruba",
    "brocade_nos": "brocade",
    "cisco_asa": "ciscoasa",
    "cisco_ios": "cisco",
    "cisco_nxos": "cisconx",
    "cisco_xe": "cisco",
    "cisco_xr": "ciscoxr",
    "cloudarmor": "cloudarmor",
    "gce": "gce",
    "gcp_hf": "gcp_hf",
    "ipset": "ipset",
    "iptables": "iptables",
    "juniper_junos": "juniper",
    "k8s": "k8s",
    "openconfig": "openconfig",
    "packetfilter": "packetfilter",
    "paloalto_panos": "paloalto",
    "pcap": "pcap",
    "sonic": "sonic",
    "speedway": "speedway",
    "vmware_nsxt": "nsxt",
    "vmware_nsxv": "nsxv",
    "windows": "windows",
}


# CAPIRCA | Normalized
CAPIRCA_LIB_MAPPER: t.Dict[str, str] = {
    "arista": "arista_eos",
    "aruba": "aruba_aoscx",
    "brocade": "brocade_nos",
    "cisco": "cisco_ios",
    "ciscoasa": "cisco_asa",
    "cisconx": "cisco_nxos",
    "ciscoxr": "cisco_xr",
    "cloudarmor": "cloudarmor",
    "gce": "gce",
    "gcp_hf": "gcp_hf",
    "ipset": "ipset",
    "iptables": "iptables",
    "juniper": "juniper_junos",
    "juniperevo": "juniper_junos",  # no reverse
    "k8s": "k8s",
    "msmpc": "juniper_junos",
    "nsxt": "vmware_nsxt",
    "nsxv": "vmware_nsxv",
    "openconfig": "openconfig",
    "packetfilter": "packetfilter",
    "paloalto": "paloalto_panos",
    "pcap": "pcap",
    "sonic": "sonic",
    "speedway": "speedway",
    "srx": "juniper_junos",  # no reverse
    "srxlo": "juniper_junos",  # no reverse
    "windows": "windows",
    "windows_advfirewall": "windows",  # no reverse
}

# Normalized | CAPIRCA
CAPIRCA_LIB_MAPPER_REVERSE: t.Dict[str, str] = {
    "arista_eos": "arista",
    "aruba_aoscx": "aruba",
    "brocade_nos": "brocade",
    "cisco_asa": "ciscoasa",
    "cisco_ios": "cisco",
    "cisco_nxos": "cisconx",
    "cisco_xe": "cisco",
    "cisco_xr": "ciscoxr",
    "cloudarmor": "cloudarmor",
    "gce": "gce",
    "gcp_hf": "gcp_hf",
    "ipset": "ipset",
    "iptables": "iptables",
    "juniper_junos": "juniper",
    "k8s": "k8s",
    "openconfig": "openconfig",
    "packetfilter": "packetfilter",
    "paloalto_panos": "paloalto",
    "pcap": "pcap",
    "sonic": "sonic",
    "speedway": "speedway",
    "vmware_nsxt": "nsxt",
    "vmware_nsxv": "nsxv",
    "windows": "windows",
}

# Normalized | Netmiko
NETMIKO_LIB_MAPPER: t.Dict[str, str] = {
    "a10": "a10",
    "accedian": "accedian",
    "adtran_os": "adtran_os",
    "alcatel_aos": "alcatel_aos",
    "alcatel_sros": "alcatel_sros",
    "allied_telesis_awplus": "allied_telesis_awplus",
    "apresia_aeos": "apresia_aeos",
    "arista_eos": "arista_eos",
    "aruba_os": "aruba_os",
    "aruba_osswitch": "aruba_osswitch",
    "aruba_procurve": "aruba_procurve",
    "avaya_ers": "avaya_ers",
    "avaya_vsp": "avaya_vsp",
    "bigip_f5": "bigip_f5",  # not in netmiko
    "broadcom_icos": "broadcom_icos",
    "brocade_fastiron": "brocade_fastiron",
    "brocade_fos": "brocade_fos",
    "brocade_netiron": "brocade_netiron",
    "brocade_nos": "brocade_nos",
    "brocade_vdx": "brocade_vdx",
    "brocade_vyos": "brocade_vyos",
    "calix_b6": "calix_b6",
    "centec_os": "centec_os",
    "checkpoint_gaia": "checkpoint_gaia",
    "ciena_saos": "ciena_saos",
    "cisco_asa": "cisco_asa",
    "cisco_ftd": "cisco_ftd",
    "cisco_ios": "cisco_ios",
    "cisco_nxos": "cisco_nxos",
    "cisco_s300": "cisco_s300",
    "cisco_tp": "cisco_tp",
    "cisco_wlc": "cisco_wlc",
    "cisco_xe": "cisco_xe",
    "cisco_xr": "cisco_xr",
    "cloudgenix_ion": "cloudgenix_ion",
    "coriant": "coriant",
    "dell_dnos9": "dell_dnos9",
    "dell_force10": "dell_force10",
    "dell_isilon": "dell_isilon",
    "dell_os10": "dell_os10",
    "dell_os6": "dell_os6",
    "dell_os9": "dell_os9",
    "dell_powerconnect": "dell_powerconnect",
    "dlink_ds": "dlink_ds",
    "eltex": "eltex",
    "eltex_esr": "eltex_esr",
    "endace": "endace",
    "enterasys": "enterasys",
    "ericsson_ipos": "ericsson_ipos",
    "extreme": "extreme",
    "extreme_ers": "extreme_ers",
    "extreme_exos": "extreme_exos",
    "extreme_netiron": "extreme_netiron",
    "extreme_nos": "extreme_nos",
    "extreme_slx": "extreme_slx",
    "extreme_vdx": "extreme_vdx",
    "extreme_vsp": "extreme_vsp",
    "extreme_wing": "extreme_wing",
    "f5_linux": "bigip_f5",  # no reverse
    "f5_ltm": "bigip_f5",  # no reverse
    "f5_tmsh": "bigip_f5",  # no reverse
    "flexvnf": "flexvnf",
    "fortinet": "fortinet",
    "generic": "generic",
    "generic_termserver": "generic_termserver",
    "hp_comware": "hp_comware",
    "hp_procurve": "hp_procurve",
    "huawei": "huawei",
    "huawei_olt": "huawei_olt",
    "huawei_smartax": "huawei_smartax",
    "huawei_vrpv8": "huawei_vrpv8",
    "ipinfusion_ocnos": "ipinfusion_ocnos",
    "juniper": "juniper",
    "juniper_junos": "juniper_junos",
    "juniper_screenos": "juniper_screenos",
    "keymile": "keymile",
    "keymile_nos": "keymile_nos",
    "linux": "linux",
    "mellanox": "mellanox",
    "mellanox_mlnxos": "mellanox_mlnxos",
    "mikrotik_routeros": "mikrotik_routeros",
    "mikrotik_switchos": "mikrotik_switchos",
    "mrv_lx": "mrv_lx",
    "mrv_optiswitch": "mrv_optiswitch",
    "netapp_cdot": "netapp_cdot",
    "netgear_prosafe": "netgear_prosafe",
    "netscaler": "netscaler",
    "nokia_sros": "nokia_sros",
    "oneaccess_oneos": "oneaccess_oneos",
    "ovs_linux": "ovs_linux",
    "paloalto_panos": "paloalto_panos",
    "pluribus": "pluribus",
    "quanta_mesh": "quanta_mesh",
    "rad_etx": "rad_etx",
    "raisecom_roap": "raisecom_roap",
    "ruckus_fastiron": "ruckus_fastiron",
    "ruijie_os": "ruijie_os",
    "sixwind_os": "sixwind_os",
    "sophos_sfos": "sophos_sfos",
    "tplink_jetstream": "tplink_jetstream",
    "ubiquiti_edge": "ubiquiti_edge",
    "ubiquiti_edgerouter": "ubiquiti_edgerouter",
    "ubiquiti_edgeswitch": "ubiquiti_edgeswitch",
    "ubiquiti_unifiswitch": "ubiquiti_unifiswitch",
    "vyatta_vyos": "vyatta_vyos",
    "vyos": "vyos",
    "watchguard_fireware": "watchguard_fireware",
    "yamaha": "yamaha",
    "zte_zxros": "zte_zxros",
}
# netmiko is the base name, so every key is a value, this ensure that.
# Netmiko | Normalized
NETMIKO_LIB_MAPPER_REVERSE: t.Dict[str, str] = {
    value: key for key, value in NETMIKO_LIB_MAPPER.items() if key not in ["f5_ltm", "f5_tmsh", "f5_linux"]
}

# ntc templates is primarily based on netmiko, so a copy is in order
_NTCTEMPLATES_LIB_MAPPER = copy.deepcopy(NETMIKO_LIB_MAPPER)
_NTCTEMPLATES_LIB_MAPPER["aruba_aoscx"] = "aruba_aoscx"
_NTCTEMPLATES_LIB_MAPPER["huawei_vrp"] = "huawei_vrp"
_NTCTEMPLATES_LIB_MAPPER["vmware_nsxv"] = "vmware_nsxv"
_NTCTEMPLATES_LIB_MAPPER["watchguard_firebox"] = "watchguard_firebox"

# NTCTemplates | Normalized
NTCTEMPLATES_LIB_MAPPER: t.Dict[str, str] = {
    key: _NTCTEMPLATES_LIB_MAPPER[key] for key in sorted(_NTCTEMPLATES_LIB_MAPPER)
}
# Normalized | NTCTemplates
NTCTEMPLATES_LIB_MAPPER_REVERSE: t.Dict[str, str] = {
    value: key for key, value in NTCTEMPLATES_LIB_MAPPER.items() if key not in ["f5_ltm", "f5_tmsh", "f5_linux"]
}


# NAPALM | Normalized
NAPALM_LIB_MAPPER: t.Dict[str, str] = {
    "aoscx": "aruba_aoscx",
    "asa": "cisco_asa",
    "cisco_wlc_ssh": "cisco_wlc",
    "eos": "arista_eos",
    "f5": "bigip_f5",
    "fortios": "fortinet",
    "huawei_vrp": "huawei",
    "ios": "cisco_ios",
    "iosxr": "cisco_xr",
    "junos": "juniper_junos",
    "nxos": "cisco_nxos",
    "nxos_ssh": "cisco_nxos",  # no reverse
    "panos": "paloalto_panos",
    "ros": "mikrotik_routeros",
    "sros": "nokia_sros",
    "vyos": "vyos",
}

# PYTNC | Normalized
PYNTC_LIB_MAPPER: t.Dict[str, str] = {
    "arista_eos_eapi": "arista_eos",
    "cisco_aireos_ssh": "cisco_wlc",
    "cisco_asa_ssh": "cisco_asa",
    "cisco_ios_ssh": "cisco_ios",
    "cisco_nxos_nxapi": "cisco_nxos",
    "f5_tmos_icontrol": "bigip_f5",
    "juniper_junos_netconf": "juniper_junos",
}

# Ansible | Normalized
ANSIBLE_LIB_MAPPER: t.Dict[str, str] = {
    "a10.acos_axapi.a10": "a10",
    "arista.eos.eos": "arista_eos",
    "arubanetworks.aoscx": "aruba_aoscx",
    "ciena.saos6.saos6": "ciena_saos",
    "cisco.asa.asa": "cisco_asa",
    "cisco.ios.ios": "cisco_ios",
    "cisco.iosxr.iosxr": "cisco_xr",
    "cisco.meraki.meraki": "cisco_meraki",
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
    "dellemc.enterprise_sonic.sonic": "sonic",
    "dellemc.os10.0s10": "dell_os10",
    "dellemc.os6.os6": "dell_os6",
    "dellemc.os9.os9": "dell_os9",
    "f5networks.f5_bigip.bigip": "bigip_f5",
    "fortinet.fortios.fortios": "fortinet",
    "junipernetworks.junos.junos": "juniper_junos",
    "paloaltonetworks.panos.panos": "paloalto_panos",
    "vyos.vyos.vyos": "vyos",
}

# PYATS | Normalized
PYATS_LIB_MAPPER: t.Dict[str, str] = {
    "asa": "cisco_asa",
    "bigip": "bigip_f5",
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

# SCRAPLI | Normalized
SCRAPLI_LIB_MAPPER: t.Dict[str, str] = {
    "arista_eos": "arista_eos",
    "aruba_aoscx": "aruba_aoscx",
    "cisco_iosxe": "cisco_ios",
    "cisco_iosxr": "cisco_xr",
    "cisco_nxos": "cisco_nxos",
    "juniper_junos": "juniper_junos",
}

# HIERCONFIG | Normalized
HIERCONFIG_LIB_MAPPER: t.Dict[str, str] = {
    "eos": "arista_eos",
    "fastiron": "ruckus_fastiron",
    "ios": "cisco_ios",
    "iosxe": "cisco_ios",  # no reverse
    "iosxr": "cisco_xr",
    "junos": "juniper_junos",
    "nxos": "cisco_nxos",
    "vyos": "vyos",
}

# Netutils Parser | Normalized
NETUTILSPARSER_LIB_MAPPER: t.Dict[str, str] = {
    "arista_eos": "arista_eos",
    "aruba_aoscx": "aruba_aoscx",
    "bigip_f5": "bigip_f5",
    "cisco_aireos": "cisco_aireos",
    "cisco_asa": "cisco_asa",
    "cisco_ios": "cisco_ios",
    "cisco_iosxr": "cisco_xr",
    "cisco_nxos": "cisco_nxos",
    "citrix_netscaler": "citrix_netscaler",
    "extreme_netiron": "extreme_netiron",
    "fortinet_fortios": "fortinet",
    "hp_comware": "hp_comware",
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

# Forward Networks Parser | Normalized
FORWARDNETWORKS_LIB_MAPPER: t.Dict[str, str] = {
    "ARISTA_EOS": "arista_eos",
    "ARUBA_SWITCH": "aruba_aoscx",
    "ASA": "cisco_asa",
    "EXTREME_NOS": "extreme_netiron",
    "F5": "bigip_f5",
    "FORTINET": "fortinet",
    "IOS": "cisco_ios",
    "IOS_XE": "cisco_ios",  # no reverse
    "IOS_XR": "cisco_xr",
    "JUNOS": "juniper_junos",
    "LINUX": "linux",
    "LINUX_OVS_OFCTL": "linux",  # no reverse
    "NETSCALER": "netscaler",
    "NXOS": "cisco_nxos",
    "PAN_OS": "paloalto_panos",
    "SRX": "juniper_junos",  # no reverse
}

# Normalized | NAPALM
NAPALM_LIB_MAPPER_REVERSE: t.Dict[str, str] = {
    "arista_eos": "eos",
    "aruba_aoscx": "aoscx",
    "bigip_f5": "f5",
    "cisco_asa": "asa",
    "cisco_ios": "ios",
    "cisco_nxos": "nxos",
    "cisco_wlc": "cisco_wlc_ssh",
    "cisco_xe": "ios",  # no reverse
    "cisco_xr": "iosxr",
    "fortinet": "fortios",
    "huawei": "huawei_vrp",
    "juniper_junos": "junos",
    "mikrotik_routeros": "ros",
    "nokia_sros": "sros",
    "paloalto_panos": "panos",
    "vyos": "vyos",
}

# Normalized | PYTNC
PYNTC_LIB_MAPPER_REVERSE: t.Dict[str, str] = {
    "arista_eos": "arista_eos_eapi",
    "bigip_f5": "f5_tmos_icontrol",
    "cisco_asa": "cisco_asa_ssh",
    "cisco_ios": "cisco_ios_ssh",
    "cisco_nxos": "cisco_nxos_nxapi",
    "cisco_wlc": "cisco_aireos_ssh",
    "cisco_xe": "cisco_ios_ssh",  # no reverse
    "juniper_junos": "juniper_junos_netconf",
}

# Normalized | ANSIBLE
ANSIBLE_LIB_MAPPER_REVERSE: t.Dict[str, str] = {
    "a10": "a10.acos_axapi.a10",
    "arista_eos": "arista.eos.eos",
    "aruba_aoscx": "arubanetworks.aoscx",
    "bigip_f5": "f5networks.f5_bigip.bigip",
    "ciena_saos": "ciena.saos6.saos6",
    "cisco_asa": "cisco.asa.asa",
    "cisco_ios": "cisco.ios.ios",
    "cisco_meraki": "cisco.meraki.meraki",
    "cisco_nxos": "cisco.nxos.nxos",
    "cisco_xe": "cisco.ios.ios",  # no reverse
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
    "fortinet": "fortinet.fortios.fortios",
    "huawei": "community.network.ce",
    "juniper_junos": "junipernetworks.junos.junos",
    "lenovo_cnos": "community.network.cnos",
    "lenovo_enos": "community.network.enos",
    "mikrotik_routeros": "community.network.routeros",
    "nokia_sros": "community.network.sros",
    "paloalto_panos": "paloaltonetworks.panos.panos",
    "pluribus": "community.network.netvisor",
    "ruckus_icx": "community.network.icx",
    "sonic": "dellemc.enterprise_sonic.sonic",
    "vyos": "vyos.vyos.vyos",
}

# Normalized | PYATS
PYATS_LIB_MAPPER_REVERSE: t.Dict[str, str] = {
    "bigip_f5": "bigip",
    "cisco_asa": "asa",
    "cisco_dnac": "dnac",
    "cisco_ios": "iosxe",
    "cisco_nxos": "nxos",
    "cisco_viptella": "viptela",
    "cisco_xe": "iosxe",  # no reverse
    "cisco_xr": "iosxr",
    "juniper_junos": "junos",
    "linux": "linux",
    "nokia_sros": "sros",
}

# Normalized | Scrapli
SCRAPLI_LIB_MAPPER_REVERSE: t.Dict[str, str] = {
    "arista_eos": "arista_eos",
    "aruba_aoscx": "aruba_aoscx",
    "cisco_ios": "cisco_iosxe",
    "cisco_nxos": "cisco_nxos",
    "cisco_xe": "cisco_iosxe",
    "cisco_xr": "cisco_iosxr",
    "juniper_junos": "juniper_junos",
}

# Normalized | HIERCONFIG
HIERCONFIG_LIB_MAPPER_REVERSE: t.Dict[str, str] = {
    "arista_eos": "eos",
    "cisco_ios": "ios",
    "cisco_nxos": "nxos",
    "cisco_xe": "ios",
    "cisco_xr": "iosxr",
    "juniper_junos": "junos",
    "ruckus_fastiron": "fastiron",
    "vyos": "vyos",
}

# Normalized | Netutils Parser
NETUTILSPARSER_LIB_MAPPER_REVERSE: t.Dict[str, str] = {
    "arista_eos": "arista_eos",
    "aruba_aoscx": "aruba_aoscx",
    "bigip_f5": "bigip_f5",
    "cisco_aireos": "cisco_aireos",
    "cisco_asa": "cisco_asa",
    "cisco_ios": "cisco_ios",
    "cisco_nxos": "cisco_nxos",
    "cisco_xe": "cisco_ios",
    "cisco_xr": "cisco_iosxr",
    "citrix_netscaler": "citrix_netscaler",
    "extreme_netiron": "extreme_netiron",
    "fortinet": "fortinet_fortios",
    "hp_comware": "hp_comware",
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

# Normalized | Forward Networks Parser
FORWARDNETWORKS_LIB_MAPPER_REVERSE: t.Dict[str, str] = {
    "arista_eos": "ARISTA_EOS",
    "aruba_aoscx": "ARUBA_SWITCH",
    "bigip_f5": "F5",
    "cisco_asa": "ASA",
    "cisco_ios": "IOS",
    "cisco_nxos": "NXOS",
    "cisco_xe": "IOS",
    "cisco_xr": "IOS_XR",
    "extreme_netiron": "EXTREME_NOS",
    "fortinet": "FORTINET",
    "juniper_junos": "JUNOS",
    "linux": "LINUX",
    "netscaler": "NETSCALER",
    "paloalto_panos": "PAN_OS",
}

# Deep copy the reverse, where there is no actual translation happening with special
# consideration for OS's not in netmiko.
_MAIN_LIB_MAPPER = copy.deepcopy(NETMIKO_LIB_MAPPER)
_MAIN_LIB_MAPPER["aruba_aoscx"] = "aruba_aoscx"
_MAIN_LIB_MAPPER["cisco_aireos"] = "cisco_aireos"
_MAIN_LIB_MAPPER["cisco_dnac"] = "cisco_dnac"
_MAIN_LIB_MAPPER["cisco_meraki"] = "cisco_meraki"
_MAIN_LIB_MAPPER["cisco_viptella"] = "cisco_viptella"
_MAIN_LIB_MAPPER["citrix_netscaler"] = "citrix_netscaler"
_MAIN_LIB_MAPPER["cloudarmor"] = "cloudarmor"
_MAIN_LIB_MAPPER["gce"] = "gce"
_MAIN_LIB_MAPPER["gcp_hf"] = "gcp_hf"
_MAIN_LIB_MAPPER["huawei_vrp"] = "huawei_vrp"
_MAIN_LIB_MAPPER["ipset"] = "ipset"
_MAIN_LIB_MAPPER["iptables"] = "iptables"
_MAIN_LIB_MAPPER["k8s"] = "k8s"
_MAIN_LIB_MAPPER["lenovo_cnos"] = "lenovo_cnos"
_MAIN_LIB_MAPPER["lenovo_enos"] = "lenovo_enos"
_MAIN_LIB_MAPPER["openconfig"] = "openconfig"
_MAIN_LIB_MAPPER["packetfilter"] = "packetfilter"
_MAIN_LIB_MAPPER["pcap"] = "pcap"
_MAIN_LIB_MAPPER["speedway"] = "speedway"
_MAIN_LIB_MAPPER["ruckus_icx"] = "ruckus_icx"
_MAIN_LIB_MAPPER["ruckus_smartzone"] = "ruckus_smartzone"
_MAIN_LIB_MAPPER["sonic"] = "sonic"
_MAIN_LIB_MAPPER["ubiquiti_airos"] = "ubiquiti_airos"
_MAIN_LIB_MAPPER["vmware_nsxv"] = "vmware_nsxv"
_MAIN_LIB_MAPPER["vmware_nsxt"] = "vmware_nsxt"
_MAIN_LIB_MAPPER["watchguard_firebox"] = "watchguard_firebox"
_MAIN_LIB_MAPPER["windows"] = "windows"
MAIN_LIB_MAPPER: t.Dict[str, str] = {key: _MAIN_LIB_MAPPER[key] for key in sorted(_MAIN_LIB_MAPPER)}
