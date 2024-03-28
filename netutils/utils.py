"""Utilities for the netutils library."""

import typing as t
from importlib import import_module

_JINJA2_FUNCTION_MAPPINGS = {
    "asn_to_int": "asn.asn_to_int",
    "int_to_asdot": "asn.int_to_asdot",
    "name_to_bits": "bandwidth.name_to_bits",
    "name_to_bytes": "bandwidth.name_to_bytes",
    "bits_to_name": "bandwidth.bits_to_name",
    "bytes_to_name": "bandwidth.bytes_to_name",
    "name_to_name": "bandwidth.name_to_name",
    "clean_config": "config.clean.clean_config",
    "sanitize_config": "config.clean.sanitize_config",
    "config_compliance": "config.compliance.compliance",
    "config_section_not_parsed": "config.compliance.config_section_not_parsed",
    "diff_network_config": "config.compliance.diff_network_config",
    "feature_compliance": "config.compliance.feature_compliance",
    "find_unordered_cfg_lines": "config.compliance.find_unordered_cfg_lines",
    "section_config": "config.compliance.section_config",
    "fqdn_to_ip": "dns.fqdn_to_ip",
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
    "is_classful": "ip.is_classful",
    "is_ip": "ip.is_ip",
    "is_ip_range": "ip.is_ip_range",
    "is_ip_within": "ip.is_ip_within",
    "is_netmask": "ip.is_netmask",
    "is_network": "ip.is_network",
    "netmask_to_cidr": "ip.netmask_to_cidr",
    "cidr_to_netmask": "ip.cidr_to_netmask",
    "cidr_to_netmaskv6": "ip.cidr_to_netmaskv6",
    "get_all_host": "ip.get_all_host",
    "get_broadcast_address": "ip.get_broadcast_address",
    "get_first_usable": "ip.get_first_usable",
    "get_peer_ip": "ip.get_peer_ip",
    "get_range_ips": "ip.get_range_ips",
    "get_usable_range": "ip.get_usable_range",
    "ipaddress_address": "ip.ipaddress_address",
    "ipaddress_interface": "ip.ipaddress_interface",
    "ipaddress_network": "ip.ipaddress_network",
    "is_valid_mac": "mac.is_valid_mac",
    "mac_to_format": "mac.mac_to_format",
    "mac_to_int": "mac.mac_to_int",
    "mac_type": "mac.mac_type",
    "mac_normalize": "mac.mac_normalize",
    "get_oui": "mac.get_oui",
    "compare_type5": "password.compare_type5",
    "compare_type7": "password.compare_type7",
    "compare_cisco_type5": "password.compare_cisco_type5",
    "compare_cisco_type7": "password.compare_cisco_type7",
    "compare_cisco_type9": "password.compare_cisco_type9",
    "decrypt_type7": "password.decrypt_type7",
    "decrypt_cisco_type7": "password.decrypt_cisco_type7",
    "decrypt_juniper_type9": "password.decrypt_juniper_type9",
    "encrypt_type5": "password.encrypt_type5",
    "encrypt_type7": "password.encrypt_type7",
    "encrypt_cisco_type5": "password.encrypt_cisco_type5",
    "encrypt_cisco_type7": "password.encrypt_cisco_type7",
    "encrypt_cisco_type9": "password.encrypt_cisco_type9",
    "encrypt_juniper_type9": "password.encrypt_juniper_type9",
    "get_hash_salt": "password.get_hash_salt",
    "tcp_ping": "ping.tcp_ping",
    "regex_findall": "regex.regex_findall",
    "regex_match": "regex.regex_match",
    "regex_search": "regex.regex_search",
    "regex_split": "regex.regex_split",
    "regex_sub": "regex.regex_sub",
    "longest_prefix_match": "route.longest_prefix_match",
    "vlanlist_to_config": "vlan.vlanlist_to_config",
    "vlanconfig_to_list": "vlan.vlanconfig_to_list",
    "normalise_delimiter_caret_c": "banner.normalise_delimiter_caret_c",
    "delimiter_change": "banner.delimiter_change",
    "uptime_seconds_to_string": "time.uptime_seconds_to_string",
    "uptime_string_to_seconds": "time.uptime_string_to_seconds",
    "get_napalm_getters": "lib_helpers.get_napalm_getters",
    "paloalto_panos_clean_newlines": "config.conversion.paloalto_panos_clean_newlines",
    "paloalto_panos_brace_to_set": "config.conversion.paloalto_panos_brace_to_set",
    "compare_version_loose": "os_version.compare_version_loose",
    "compare_version_strict": "os_version.compare_version_strict",
    "get_upgrade_path": "os_version.get_upgrade_path",
    "hash_data": "hash.hash_data",
    "get_ips_sorted": "ip.get_ips_sorted",
}


def jinja2_convenience_function() -> t.Dict[str, t.Callable[..., t.Any]]:
    """Convenience function that allows netutils filter to be used easily with jinja2.

    Returns:
        Keys are the function names for the Jinja2 filter and values are the function objects.

    Examples:
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
