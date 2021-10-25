"""Utilities for the netutils library."""
from importlib import import_module

_JINJA2_FUNCTION_MAPPINGS = {
    "asn_to_int": "asn.asn_to_int",
    "clean_config": "config.clean.clean_config",
    "sanitize_config": "config.clean.sanitize_config",
    "config_compliance": "config.compliance.compliance",
    "config_section_not_parsed": "config.compliance.config_section_not_parsed",
    "diff_network_config": "config.compliance.diff_network_config",
    "feature_compliance": "config.compliance.feature_compliance",
    "find_unordered_cfg_lines": "config.compliance.find_unordered_cfg_lines",
    "section_config": "config.compliance.section_config",
    "fqdn_to_ip": "dns.fqdn_to_ip",
    "is_fqdn_valid": "dns.is_fqdn_valid",
    "is_fqdn_resolvable": "dns.is_fqdn_resolvable",
    "interface_range_expansion": "interface.interface_range_expansion",
    "interface_range_compress": "interface.interface_range_compress",
    "split_interface": "interface.split_interface",
    "canonical_interface_name": "interface.canonical_interface_name",
    "canonical_interface_name_list": "interface.canonical_interface_name_list",
    "abbreviated_interface_name": "interface.abbreviated_interface_name",
    "abbreviated_interface_name_list": "interface.abbreviated_interface_name_list",
    "sort_interface_list": "interface.sort_interface_list",
    "ip_to_hex": "ip.ip_to_hex",
    "ip_addition": "ip.ip_addition",
    "ip_to_bin": "ip.ip_to_bin",
    "ip_subtract": "ip.ip_subtract",
    "is_ip": "ip.is_ip",
    "is_netmask": "ip.is_netmask",
    "netmask_to_cidr": "ip.netmask_to_cidr",
    "cidr_to_netmask": "ip.cidr_to_netmask",
    "cidr_to_netmaskv6": "ip.cidr_to_netmaskv6",
    "get_all_host": "ip.get_all_host",
    "get_broadcast_address": "ip.get_broadcast_address",
    "get_first_usable": "ip.get_first_usable",
    "get_peer_ip": "ip.get_peer_ip",
    "get_usable_range": "ip.get_usable_range",
    "is_valid_mac": "mac.is_valid_mac",
    "mac_to_format": "mac.mac_to_format",
    "mac_to_int": "mac.mac_to_int",
    "mac_type": "mac.mac_type",
    "mac_normalize": "mac.mac_normalize",
    "compare_type5": "password.compare_type5",
    "compare_type7": "password.compare_type7",
    "decrypt_type7": "password.decrypt_type7",
    "encrypt_type5": "password.encrypt_type5",
    "encrypt_type7": "password.encrypt_type7",
    "get_hash_salt": "password.get_hash_salt",
    "tcp_ping": "ping.tcp_ping",
    "longest_prefix_match": "route.longest_prefix_match",
    "vlanlist_to_config": "vlan.vlanlist_to_config",
    "vlanconfig_to_list": "vlan.vlanconfig_to_list",
    "bps_to_kbps": "bandwidth.bps_to_kbps",
    "bps_to_kbytes": "bandwidth.bps_to_kbytes",
    "bps_to_mbps": "bandwidth.bps_to_mbps",
    "bps_to_mbytes": "bandwidth.bps_to_mbytes",
    "bps_to_gbps": "bandwidth.bps_to_gbps",
    "bps_to_gbytes": "bandwidth.bps_to_gbytes",
    "bps_to_tbps": "bandwidth.bps_to_tbps",
    "bps_to_tbytes": "bandwidth.bps_to_tbytes",
    "kbps_to_mbps": "bandwidth.kbps_to_mbps",
    "kbps_to_mbytes": "bandwidth.kbps_to_mbytes",
    "kbps_to_gbps": "bandwidth.kbps_to_gbps",
    "kbps_to_gbytes": "bandwidth.kbps_to_gbytes",
    "kbps_to_tbps": "bandwidth.kbps_to_tbps",
    "kbps_to_tbytes": "bandwidth.kbps_to_tbytes",
    "mbps_to_gbps": "bandwidth.mbps_to_gbps",
    "mbps_to_gbytes": "bandwidth.mbps_to_gbytes",
    "mbps_to_tbps": "bandwidth.mbps_to_tbps",
    "mbps_to_tbytes": "bandwidth.mbps_to_tbytes",
    "mbps_to_kbps": "bandwidth.mbps_to_kbps",
    "mbps_to_kbytes": "bandwidth.mbps_to_kbytes",
    "gbps_to_kbps": "bandwidth.gbps_to_kbps",
    "gbps_to_kbytes": "bandwidth.gbps_to_kbytes",
    "gbps_to_mbps": "bandwidth.gbps_to_mbps",
    "gbps_to_mbytes": "bandwidth.gbps_to_mbytes",
    "gbps_to_tbps": "bandwidth.gbps_to_tbps",
    "gbps_to_tbytes": "bandwidth.gbps_to_tbytes",
    "tbps_to_kbps": "bandwidth.tbps_to_kbps",
    "tbps_to_kbytes": "bandwidth.tbps_to_kbytes",
    "tbps_to_mbps": "bandwidth.tbps_to_mbps",
    "tbps_to_mbytes": "bandwidth.tbps_to_mbytes",
    "tbps_to_gbps": "bandwidth.tbps_to_gbps",
    "tbps_to_gbytes": "bandwidth.tbps_to_gbytes",
    "name_to_kbits": "bandwidth.name_to_kbits",
    "name_to_bits": "bandwidth.name_to_bits",
    "name_to_kbytes": "bandwidth.name_to_kbytes",
    "name_to_bytes": "bandwidth.name_to_bytes",
    "kbits_to_name": "bandwidth.kbits_to_name",
    "bits_to_name": "bandwidth.bits_to_name",
    "bytes_to_name": "bandwidth.bytes_to_name",
}


def jinja2_convenience_function():
    """Convenience function that allows netutils filter to be used easily with jinja2.

    Returns:
        dict: Keys are the function names for the Jinja2 filter and values are the function objects.

    Example:
        >>> from netutils.utils import jinja2_convenience_function
        >>> function_mappings = jinja2_convenience_function()
        >>> function_mappings["get_first_usable"]("192.168.0.0/24")
        '192.168.0.1'
        >>> function_mappings["get_broadcast_address"]("192.168.0.0/24")
        '192.168.0.255'
    """
    result = {}

    for jinja2_function_name, function_import_path in _JINJA2_FUNCTION_MAPPINGS.items():
        module, function_name = function_import_path.rsplit(".", 1)
        imported_module = import_module(f"netutils.{module}")
        function_object = getattr(imported_module, function_name)
        result[jinja2_function_name] = function_object
    return result
