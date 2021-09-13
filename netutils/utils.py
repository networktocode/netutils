"""Utilities for the netutils library."""
from importlib import import_module

_JINJA2_FUNCTION_MAPPINGS = {
    "asn_to_int": "asn.asn_to_int",
    "config": {
        "clean_config": "clean.clean_config",
        "sanitize_config": "clean.sanitize_config",
        "config_compliance": "compliance.compliance",
        "config_section_not_parsed": "compliance.config_section_not_parsed",
        "diff_network_config": "compliance.diff_network_config",
        "feature_compliance": "compliance.feature_compliance",
        "find_unordered_cfg_lines": "compliance.find_unordered_cfg_lines",
        "section_config": "compliance.section_config",
    },
    "fqdn_to_ip": "dns.fqdn_to_ip",
    "is_fqdn_valid": "dns.is_fqdn_valid",
    "is_fqdn_resolvable": "dns.is_fqdn_resolvable",
    "interface_range_expansion": "interface.interface_range_expansion",
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
    "get_all_host_ip_network": "ip.get_all_host",
    "get_broadcast_address_ip_network": "ip.get_broadcast_address",
    "get_first_usable_ip_network": "ip.get_first_usable",
    "get_usable_range_ip_network": "ip.get_usable_range",
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
}


def jinja2_convenience_function(jinja_mappings_dict=None, parent_folder=None):
    """Convenience function that allows netutils filter to be used easily with jinja2.

    Returns:
        Any: Return value depends on the function called.

    """
    if not jinja_mappings_dict:
        jinja_mappings_dict = _JINJA2_FUNCTION_MAPPINGS

    result = {}

    for function_name, function_import_path in jinja_mappings_dict.items():
        if isinstance(function_import_path, dict):
            recursive_dict = jinja2_convenience_function(function_import_path, function_name)
            result.update(recursive_dict)
        else:
            function_import_module, function_import_name = function_import_path.split(".", 1)
            if parent_folder:
                imported_module = import_module(f"netutils.{parent_folder}.{function_import_module}")
            else:
                imported_module = import_module(f"netutils.{function_import_module}")
            function_object = getattr(imported_module, function_import_name)
        result[function_name] = function_object
    return result
