"""Filter Plugins for compliance checks."""

from . import parser  # pylint: disable=relative-beyond-top-level

parser_map = {
    "arista_eos": parser.EOSConfigParser,
    "cisco_ios": parser.IOSConfigParser,
    "cisco_nxos": parser.NXOSConfigParser,
    "cisco_aireos": parser.AIREOSConfigParser,
    "linux": parser.LINUXConfigParser,
    "bigip_f5": parser.F5ConfigParser,
    "juniper_junos": parser.JunosConfigParser,
    "cisco_asa": parser.ASAConfigParser,
}

default_feature = {
    "compliant": None,
    "missing": None,
    "extra": None,
    "cannot_parse": True,
    "unordered_compliant": None,
    "ordered_compliant": None,
    "actual": None,
    "intended": None,
}


def _check_configs_differences(intended_cfg, actual_cfg, network_os):
    r"""Find differences between intended and actual config lines.

    Args:
        intended_cfg (str): Feature intended configuration.
        actual_cfg: (str): Feature actual configuration.
        network_os (str): Device network operating system that is in parser_map keys.

    Returns:
        dict: Config fragments that are missing, extra or unordered_compliant.

    Example:
        >>> from netutils.config.compliance import _check_configs_differences
        >>> intended_cfg = '''ntp server 10.10.10.10
        ... ntp server 10.10.10.11'''
        >>>
        >>> actual_cfg = '''ntp server 10.10.10.10
        ... ntp server 192.168.0.1'''
        >>>
        >>> network_os = 'cisco_ios'
        >>> import pprint
        >>> _check_configs_differences(intended_cfg, actual_cfg, network_os) == \
        ... {
        ...     "missing": "ntp server 10.10.10.11",
        ...     "extra": "ntp server 192.168.0.1",
        ...     "unordered_compliant": False,
        ... }
        True
    """
    missing = diff_network_config(intended_cfg, actual_cfg, network_os)
    extra = diff_network_config(actual_cfg, intended_cfg, network_os)
    if not missing and not extra:
        unordered_compliant, _ = find_unordered_cfg_lines(intended_cfg, actual_cfg)
    else:
        unordered_compliant = False
    return {
        "missing": missing,
        "extra": extra,
        "unordered_compliant": unordered_compliant,
    }


def _is_feature_ordered_compliant(feature_intended_cfg, feature_actual_cfg):
    """Check if feature intended cfg is compliant with feature actual cfg.

    Args:
        feature_intended_cfg (str): Feature intended configuration.
        feature_actual_cfg: (str): Feature actual configuration.

    Returns:
        bool

    Example:
        >>> feature_intended_cfg = '''router bgp 100
        ...   bgp router-id 10.6.6.5'''
        >>>
        >>> feature_actual_cfg = '''router bgp 100
        ...   bgp router-id 10.6.6.5'''
        >>>
        >>> print(_is_feature_ordered_compliant(feature_intended_cfg, feature_actual_cfg))
        True
        >>>
    """
    if not feature_intended_cfg and not feature_actual_cfg:
        return True
    if feature_intended_cfg == feature_actual_cfg:
        return True
    return False


def _open_file_config(cfg_path):
    """Open config file from local disk."""
    try:
        with open(cfg_path) as filehandler:
            device_cfg = filehandler.read()
    except IOError:
        return False
    return device_cfg.strip()


def compliance(features, backup, intended, network_os, cfg_type="file"):
    r"""Report compliance for all features provided as input.

    Args:
        features (list): List of features for particular network os.
        backup (path): running config or config backup file  to compare against intended.
        intended (path): intended config to compare against backup.
        network_os (str): Device network operating system that is in parser_map keys.
        cfg_type (str, optional): A string that is effectively a choice between `file` and `string`. Defaults to `file`.

    Returns:
        dict: Compliance information per feature.

    Example:
        >>> features = [
        ...     {
        ...         "name": "hostname",
        ...         "ordered": True,
        ...         "section": [
        ...             "hostname"
        ...         ]
        ...     },
        ...     {
        ...         "name": "ntp",
        ...         "ordered": True,
        ...         "section": [
        ...             "ntp"
        ...         ]
        ...     }
        ... ]
        >>> backup = "ntp server 192.168.1.1\nntp server 192.168.1.2 prefer"
        >>> intended = "ntp server 192.168.1.1\nntp server 192.168.1.5 prefer"
        >>> network_os = "cisco_ios"
        >>> from pprint import pprint
        >>> compliance(features, backup, intended, network_os, "string") == \
        ... {'hostname': {'actual': '',
        ...     'cannot_parse': True,
        ...     'compliant': True,
        ...     'extra': '',
        ...     'intended': '',
        ...     'missing': '',
        ...     'ordered_compliant': True,
        ...     'unordered_compliant': True},
        ... 'ntp': {'actual': 'ntp server 192.168.1.1\nntp server 192.168.1.2 prefer',
        ...     'cannot_parse': True,
        ...     'compliant': False,
        ...     'extra': 'ntp server 192.168.1.2 prefer',
        ...     'intended': 'ntp server 192.168.1.1\nntp server 192.168.1.5 prefer',
        ...     'missing': 'ntp server 192.168.1.5 prefer',
        ...     'ordered_compliant': False,
        ...     'unordered_compliant': False}}
        True
    """
    if cfg_type not in ["file", "string"]:
        raise ValueError("The variable `cfg_type` must be either `file` or `string`.")
    if cfg_type == "file":
        backup_cfg = _open_file_config(backup)
        intended_cfg = _open_file_config(intended)
    else:
        backup_cfg = backup
        intended_cfg = intended

    compliance_results = dict()

    for feature in features:
        backup_str = section_config(feature, backup_cfg, network_os)
        intended_str = section_config(feature, intended_cfg, network_os)
        compliance_results.update({feature["name"]: feature_compliance(feature, backup_str, intended_str, network_os)})

    return compliance_results


def config_section_not_parsed(features, device_cfg, network_os):
    r"""Return device config section that is not checked by compliance.

    Args:
        features (list): List of features for particular network os.
        device_cfg (str): Device configuration.
        network_os (str): Device network operating system that is in parser_map keys.

    Returns:
        dict: Config that was not parsed or section not found.

    Example:
        >>> features = [{
        ...    "name": "BGP",
        ...    "ordered": True,
        ...    "section": [
        ...        "router bgp "
        ...    ]
        ... }]
        >>> network_os = 'cisco_ios'
        >>> device_cfg = '''router bgp 100
        ...  bgp router-id 10.6.6.5
        ... !
        ... access-list 1 permit 10.10.10.10
        ... access-list 1 permit 10.10.10.11'''
        >>> config_section_not_parsed(features, device_cfg, network_os)
        {'remaining_cfg': '!\naccess-list 1 permit 10.10.10.10\naccess-list 1 permit 10.10.10.11', 'section_not_found': []}
    """
    remaining_cfg = device_cfg
    section_not_found = list()
    for feature in features:
        feature_cfg = section_config(feature, device_cfg, network_os)
        if not feature_cfg:
            section_not_found.append(feature["name"])
        remaining_cfg = remaining_cfg.replace(feature_cfg, "")
    return {
        "remaining_cfg": remaining_cfg.strip(),
        "section_not_found": section_not_found,
    }


def diff_network_config(compare_config, base_config, network_os):
    """Identify which lines in compare_config are not in base_config.

    Args:
        compare_config (str): The config to evaluate against base_config.
        base_config (str): The config to compare compare_config against.
        network_os (str): Device network operating system that is in parser_map keys.

    Returns:
        base_config (str): The string of additional commands in compare_config separated by a newline.

    Example:
        >>> compare_config = '''router bgp 100
        ...  bgp router-id 10.6.6.5
        ... !
        ... snmp-server ifindex persist
        ... snmp-server packetsize 4096
        ... snmp-server location SFO
        ... access-list 1 permit 10.15.20.20
        ... access-list 1 permit 10.15.20.21'''
        >>>
        >>> base_config = '''router bgp 100
        ...  bgp router-id 10.6.6.5
        ... !
        ... snmp-server packetsize 4096
        ... snmp-server location SFO
        ... access-list 1 permit 10.15.20.20
        ... access-list 1 permit 10.15.20.21'''
        >>>
        >>> network_os = "cisco_ios"
        >>> diff_network_config(compare_config, base_config, network_os)
        'snmp-server ifindex persist'
        >>>
    """
    os_parser = parser_map[network_os]
    compare_parser = os_parser(compare_config)
    base_parser = os_parser(base_config)
    base = set(base_parser.config_lines)

    needed_lines = []
    for line in compare_parser.config_lines:
        if line not in base:
            for parent in line.parents:
                if parent not in needed_lines:
                    needed_lines.append(parent)
            needed_lines.append(line.config_line)

    return "\n".join(needed_lines)


def feature_compliance(feature, backup_cfg, intended_cfg, network_os):
    r"""Report compliance for all features provided as input.

    Args:
        feature (dict): A dictionary with the attributes of the feature check
        backup_cfg (str): running config or config backup of a specific feature to compare.
        intended_cfg (str): intended config of a specific feature to compare.
        network_os (str): Device network operating system that is in parser_map keys.

    Returns:
        dict: Compliance information of a single feature.

    Example:
        >>> feature = {
        ...     "name": "ntp",
        ...     "ordered": True,
        ...     "section": [
        ...         "ntp"
        ...     ]
        ... }
        >>> backup = "ntp server 192.168.1.1\nntp server 192.168.1.2 prefer"
        >>> intended = "ntp server 192.168.1.1\nntp server 192.168.1.5 prefer"
        >>> network_os = "cisco_ios"
        >>> from pprint import pprint
        >>> feature_compliance(feature, backup, intended, network_os) == \
        ... {'actual': 'ntp server 192.168.1.1\nntp server 192.168.1.2 prefer',
        ...     'cannot_parse': True,
        ...     'compliant': False,
        ...     'extra': 'ntp server 192.168.1.2 prefer',
        ...     'intended': 'ntp server 192.168.1.1\nntp server 192.168.1.5 prefer',
        ...     'missing': 'ntp server 192.168.1.5 prefer',
        ...     'ordered_compliant': False,
        ...     'unordered_compliant': False}
        True
    """
    feature_data = default_feature.copy()
    feature_data["actual"] = backup_cfg
    feature_data["intended"] = intended_cfg
    # Check for ordered compliant which is accomplished with a simple exact match
    feature_data["ordered_compliant"] = _is_feature_ordered_compliant(intended_cfg, backup_cfg)

    if feature_data["ordered_compliant"]:
        feature_data.update(
            {
                "missing": "",
                "extra": "",
                "unordered_compliant": True,
            }
        )
    else:
        if backup_cfg and intended_cfg:
            feature_data.update(_check_configs_differences(intended_cfg, backup_cfg, network_os))
    if feature["ordered"] is True:
        feature_data["compliant"] = feature_data["ordered_compliant"]
    elif feature["ordered"] is False:
        feature_data["compliant"] = feature_data["unordered_compliant"]
    else:
        raise  # pylint: disable=misplaced-bare-raise

    return feature_data


def find_unordered_cfg_lines(intended_cfg, actual_cfg):
    """Check if config lines are miss-ordered, i.e in ACL-s.

    Args:
        intended_cfg (str): Feature intended configuration.
        actual_cfg: (str): Feature actual configuration.

    Returns:
        list: List of tuples with unordered_compliant cfg lines.

    Example:
        >>> intended_cfg = '''
        ... ntp server 10.10.10.10
        ... ntp server 10.10.10.11
        ... ntp server 10.10.10.12'''
        >>>
        >>> actual_cfg = '''
        ... ntp server 10.10.10.12
        ... ntp server 10.10.10.11
        ... ntp server 10.10.10.10'''
        >>>
        >>> find_unordered_cfg_lines(intended_cfg, actual_cfg)
        (True, [('ntp server 10.10.10.10', 'ntp server 10.10.10.12'), ('ntp server 10.10.10.12', 'ntp server 10.10.10.10')])
    """
    intended_lines = intended_cfg.splitlines()
    actual_lines = actual_cfg.splitlines()
    unordered_lines = list()
    if len(intended_lines) == len(actual_lines):
        # Process to find actual lines that are misordered
        unordered_lines = [(e1, e2) for e1, e2 in zip(intended_lines, actual_lines) if e1 != e2]
    # Process to find determine if there are any different lines, regardless of order
    if not set(intended_lines).difference(actual_lines):
        return (True, unordered_lines)
    return (False, unordered_lines)


def section_config(feature, device_cfg, network_os):
    """Parse feature section config from device cfg.

        In case section attribute of the the feature is not provided
        entire content of the device_cfg is returned.

    Args:
        feature (dict): Feature name and cfg lines that should be parsed.
        device_cfg (str): Device configuration.
        network_os (str): Device network operating system that is in parser_map keys.

    Returns:
        list: The hash report data mapping file hashes to report data.

    Example:
        >>> feature =  {
        ...    "name": "BGP",
        ...    "ordered": False,
        ...    "section": [
        ...        "router bgp "
        ...    ]
        ... }
        >>>
        >>> device_cfg = '''router bgp 100
        ...  bgp router-id 10.6.6.5
        ... !
        ... snmp-server ifindex persist
        ... snmp-server packetsize 4096
        ... snmp-server location SFO
        ... access-list 1 permit 10.10.15.15
        ... access-list 1 permit 10.10.20.20'''
        >>>
        >>> print(section_config(feature, device_cfg, "cisco_ios"))# ==
        router bgp 100
         bgp router-id 10.6.6.5
    """
    section_starts_with = feature.get("section")
    if not section_starts_with:
        return device_cfg

    match = False
    section_config_list = []
    os_parser = parser_map[network_os]
    config_parsed = os_parser(device_cfg)
    for line in config_parsed.config_lines:
        if match:
            if line.parents:  # pylint: disable=no-else-continue
                section_config_list.append(line.config_line)
                continue
            else:
                match = False
        for line_start in section_starts_with:
            if not match and line.config_line.startswith(line_start):
                section_config_list.append(line.config_line)
                match = True
    return "\n".join(section_config_list).strip()
