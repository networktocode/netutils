from netutils.config.parser import ConfigLine

data = [
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="configure system", parents=()),
    ConfigLine(config_line='  prompt "ADVA-SW1"', parents=("configure system",)),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="configure system", parents=()),
    ConfigLine(config_line="  ftp enabled", parents=("configure system",)),
    ConfigLine(config_line="  system-tod-type ntp", parents=("configure system",)),
    ConfigLine(config_line="  http disabled", parents=("configure system",)),
    ConfigLine(config_line="  telnet enabled", parents=("configure system",)),
    ConfigLine(
        config_line='  security-banner "Warning Notice: This system is restricted solely to Rainbow Industries\\\\nauthorized users for legitimate business purposes only. The actual or attempted\\\\nunauthorized access, use, or modification of this system is strictly prohibited\\\\nby Techno Cosmic Research Institute. Unauthorized users are subject to company\\\\ndisciplinary proceedings and/or criminal and civil penalties under state,\\\\nfederal, or other applicable domestic and foreign laws. The use of this system\\\\nmay be monitored and recorded for administrative and security reasons. Anyone\\\\naccessing this system expressly consents to such monitoring and is advised that\\\\nif such monitoring reveals possible evidence of criminal activity, Techno Cosmic\\\\nResearch Institute may provide the evidence to law enforcement officials. All users\\\\nmust comply with Rainbow Industries security instructions regarding the\\\\nprotection of Rainbow Industries information. Call Network Operations Center\\\\nat 1-888-555-1138 for any information regarding this notice."',
        parents=("configure system",),
    ),
    ConfigLine(config_line="  long-if-alias enabled", parents=("configure system",)),
    ConfigLine(config_line="  ntp-client", parents=("configure system",)),
    ConfigLine(config_line="    primary-server ipv4 198.51.100.5", parents=("configure system", "  ntp-client")),
    ConfigLine(config_line="    backup-server ipv4 192.0.2.5", parents=("configure system", "  ntp-client")),
    ConfigLine(config_line="    control enabled", parents=("configure system", "  ntp-client")),
    ConfigLine(config_line="    back", parents=("configure system", "  ntp-client")),
    ConfigLine(config_line="  alarm-attributes access-port sfp-non-qualified nsa nr", parents=("configure system",)),
    ConfigLine(config_line="  alarm-attributes network-port sfp-non-qualified nsa nr", parents=("configure system",)),
    ConfigLine(config_line="  syslog-server 1", parents=("configure system",)),
    ConfigLine(
        config_line="    configure ipv4-address 198.51.100.3 514", parents=("configure system", "  syslog-server 1")
    ),
    ConfigLine(config_line="    back", parents=("configure system", "  syslog-server 1")),
    ConfigLine(config_line="  audit-log", parents=("configure system",)),
    ConfigLine(config_line="    syslog-control enabled", parents=("configure system", "  audit-log")),
    ConfigLine(config_line="    back", parents=("configure system", "  audit-log")),
    ConfigLine(config_line="  security-log", parents=("configure system",)),
    ConfigLine(config_line="    syslog-control enabled", parents=("configure system", "  security-log")),
    ConfigLine(config_line="    back", parents=("configure system", "  security-log")),
    ConfigLine(config_line="  alarm-log", parents=("configure system",)),
    ConfigLine(config_line="    syslog-control enabled", parents=("configure system", "  alarm-log")),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="configure user-security", parents=()),
    ConfigLine(config_line="  tacacs-privilege-control disabled", parents=("configure user-security",)),
    ConfigLine(config_line="  tacacs-user-privilege superuser", parents=("configure user-security",)),
    ConfigLine(config_line="  auth-protocol tacacs", parents=("configure user-security",)),
    ConfigLine(config_line="  security-strength low", parents=("configure user-security",)),
    ConfigLine(config_line="  config-rap 1", parents=("configure user-security",)),
    ConfigLine(config_line="    ip-address 203.0.113.201", parents=("configure user-security", "  config-rap 1")),
    ConfigLine(config_line="    port 49", parents=("configure user-security", "  config-rap 1")),
    ConfigLine(config_line="    accounting-port 49", parents=("configure user-security", "  config-rap 1")),
    ConfigLine(config_line="    timeout 2", parents=("configure user-security", "  config-rap 1")),
    ConfigLine(config_line="    retries 1", parents=("configure user-security", "  config-rap 1")),
    ConfigLine(config_line="    control enabled", parents=("configure user-security", "  config-rap 1")),
    ConfigLine(config_line="    back", parents=("configure user-security", "  config-rap 1")),
    ConfigLine(config_line="  config-rap 2", parents=("configure user-security",)),
    ConfigLine(config_line="    port 49", parents=("configure user-security", "  config-rap 2")),
    ConfigLine(config_line="    accounting-port 49", parents=("configure user-security", "  config-rap 2")),
    ConfigLine(config_line="    back", parents=("configure user-security", "  config-rap 2")),
    ConfigLine(config_line="  config-rap 3", parents=("configure user-security",)),
    ConfigLine(config_line="    port 49", parents=("configure user-security", "  config-rap 3")),
    ConfigLine(config_line="    accounting-port 49", parents=("configure user-security", "  config-rap 3")),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="configure snmp", parents=()),
    ConfigLine(config_line='  delete community "private"', parents=("configure snmp",)),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="configure snmp", parents=()),
    ConfigLine(config_line='  delete community "public"', parents=("configure snmp",)),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="configure snmp", parents=()),
    ConfigLine(config_line='  add community "snmp-comm-1" readwrite', parents=("configure snmp",)),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="configure snmp", parents=()),
    ConfigLine(config_line='  add community "snmp-comm-2" readwrite', parents=("configure snmp",)),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="configure snmp", parents=()),
    ConfigLine(config_line='  add community "snmp-comm-3" trap-only', parents=("configure snmp",)),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="configure snmp", parents=()),
    ConfigLine(config_line='  add community "snmp-comm-4" readonly', parents=("configure snmp",)),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="configure snmp", parents=()),
    ConfigLine(
        config_line='  add target-params "Rainbow" snmpv2c snmpv2c "snmp-comm-4" no-auth', parents=("configure snmp",)
    ),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="configure snmp", parents=()),
    ConfigLine(
        config_line='  add target-params "Trapstation" snmpv2c snmpv2c "snmp-comm-4" no-auth',
        parents=("configure snmp",),
    ),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="configure snmp", parents=()),
    ConfigLine(
        config_line='  add target-params "snmp-comm-3" snmpv2c snmpv2c "snmp-comm-3" no-auth',
        parents=("configure snmp",),
    ),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="configure snmp", parents=()),
    ConfigLine(
        config_line='  add target-address "Anycast" "198.51.100.140:162" ipv4 3 3 "trap" "snmp-comm-3" enabled',
        parents=("configure snmp",),
    ),
    ConfigLine(
        config_line='  configure target-address "Anycast" bulk-traps-control disabled', parents=("configure snmp",)
    ),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="network-element ne-1", parents=()),
    ConfigLine(config_line='  name "ADVA-SW1"', parents=("network-element ne-1",)),
    ConfigLine(config_line='  contact "b.stockman@tcri.com"', parents=("network-element ne-1",)),
    ConfigLine(config_line='  location "123 Fake St., Springfield, USA"', parents=("network-element ne-1",)),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="network-element ne-1", parents=()),
    ConfigLine(config_line="  configure nte nte114pro-1-1-1", parents=("network-element ne-1",)),
    ConfigLine(
        config_line="    snmp-dying-gasp enabled", parents=("network-element ne-1", "  configure nte nte114pro-1-1-1")
    ),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="network-element ne-1", parents=()),
    ConfigLine(config_line="  configure nte nte114pro-1-1-1", parents=("network-element ne-1",)),
    ConfigLine(
        config_line="    configure network-port network-1-1-1-2",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1"),
    ),
    ConfigLine(
        config_line="      switch-type access yes",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure network-port network-1-1-1-2",
        ),
    ),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="network-element ne-1", parents=()),
    ConfigLine(config_line="  configure nte nte114pro-1-1-1", parents=("network-element ne-1",)),
    ConfigLine(
        config_line="    configure access-port access-1-1-1-2",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1"),
    ),
    ConfigLine(
        config_line="      llf",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-2"),
    ),
    ConfigLine(
        config_line="        llf-trigger-event none",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-2",
            "      llf",
        ),
    ),
    ConfigLine(
        config_line="        remote-link-ids none",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-2",
            "      llf",
        ),
    ),
    ConfigLine(
        config_line="        back",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-2",
            "      llf",
        ),
    ),
    ConfigLine(
        config_line="      lpbk",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-2"),
    ),
    ConfigLine(
        config_line="        dst-mac-control disabled",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-2",
            "      lpbk",
        ),
    ),
    ConfigLine(
        config_line="        src-mac-control disabled",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-2",
            "      lpbk",
        ),
    ),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="network-element ne-1", parents=()),
    ConfigLine(config_line="  configure nte nte114pro-1-1-1", parents=("network-element ne-1",)),
    ConfigLine(
        config_line="    configure access-port access-1-1-1-3",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1"),
    ),
    ConfigLine(
        config_line="      admin-state unassigned",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      service-type evpl",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line='      alias "INTERFACE DESC"',
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      auto-diagnostic disabled",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      mtu 9612",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      rx-dei-action ignore",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      tx-dei-action set-to-zero",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      tx-dei-tag-type ctag-or-stag",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      a2n-push-port-vid disabled",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      priority-mapping-profile prio_map_profile-1",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="network-element ne-1", parents=()),
    ConfigLine(config_line="  configure nte nte114pro-1-1-1", parents=("network-element ne-1",)),
    ConfigLine(
        config_line="    configure access-port access-1-1-1-3",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-00 pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-01 pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-02 pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-03 pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-04 pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-05 pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-06 pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-07 pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-08 pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-09 pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-0a pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-0b pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-0c pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-0d pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-0e pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-0f pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="network-element ne-1", parents=()),
    ConfigLine(config_line="  configure nte nte114pro-1-1-1", parents=("network-element ne-1",)),
    ConfigLine(
        config_line="    configure access-port access-1-1-1-4",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1"),
    ),
    ConfigLine(
        config_line="      admin-state unassigned",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-4"),
    ),
    ConfigLine(
        config_line="      service-type evpl",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-4"),
    ),
    ConfigLine(
        config_line="      auto-diagnostic disabled",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-4"),
    ),
    ConfigLine(
        config_line="      media fiber auto-1000-full",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-4"),
    ),
    ConfigLine(
        config_line='      alias "INTERFACE DESC"',
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-4"),
    ),
    ConfigLine(
        config_line="      tx-dei-tag-type ctag-or-stag",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-4"),
    ),
    ConfigLine(
        config_line="      priority-mapping-profile prio_map_profile-1",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-4"),
    ),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="network-element ne-1", parents=()),
    ConfigLine(config_line="  configure nte nte114pro-1-1-1", parents=("network-element ne-1",)),
    ConfigLine(
        config_line="    configure access-port access-1-1-1-4",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-00 pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-4"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-01 pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-4"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-02 pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-4"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-03 pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-4"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-04 pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-4"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-05 pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-4"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-06 pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-4"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-07 pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-4"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-08 pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-4"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-09 pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-4"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-0a pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-4"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-0b pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-4"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-0c pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-4"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-0d pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-4"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-0e pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-4"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-0f pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-4"),
    ),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="network-element ne-1", parents=()),
    ConfigLine(config_line="  configure nte nte114pro-1-1-1", parents=("network-element ne-1",)),
    ConfigLine(
        config_line="    configure access-port access-1-1-1-5",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1"),
    ),
    ConfigLine(
        config_line="      service-type evpl",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-5"),
    ),
    ConfigLine(
        config_line="      speed auto-1000-full",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-5"),
    ),
    ConfigLine(
        config_line="      priority-mapping-profile prio_map_profile-1",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-5"),
    ),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="network-element ne-1", parents=()),
    ConfigLine(config_line="  configure nte nte114pro-1-1-1", parents=("network-element ne-1",)),
    ConfigLine(
        config_line="    configure access-port access-1-1-1-5",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-00 pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-5"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-01 pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-5"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-02 pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-5"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-03 pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-5"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-04 pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-5"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-05 pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-5"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-06 pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-5"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-07 pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-5"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-08 pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-5"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-09 pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-5"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-0a pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-5"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-0b pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-5"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-0c pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-5"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-0d pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-5"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-0e pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-5"),
    ),
    ConfigLine(
        config_line="      cpd-filter 01-80-c2-00-00-0f pass-thru",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-5"),
    ),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="network-element ne-1", parents=()),
    ConfigLine(config_line="  configure nte nte114pro-1-1-1", parents=("network-element ne-1",)),
    ConfigLine(
        config_line="    configure network-port network-1-1-1-1",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1"),
    ),
    ConfigLine(
        config_line="      mtu 9638",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure network-port network-1-1-1-1",
        ),
    ),
    ConfigLine(
        config_line="      auto-diagnostic disabled",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure network-port network-1-1-1-1",
        ),
    ),
    ConfigLine(
        config_line="      media fiber auto-1000-full",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure network-port network-1-1-1-1",
        ),
    ),
    ConfigLine(
        config_line='      alias "INTERFACE DESC"',
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure network-port network-1-1-1-1",
        ),
    ),
    ConfigLine(
        config_line="      rx-dei-action ignore",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure network-port network-1-1-1-1",
        ),
    ),
    ConfigLine(
        config_line="      tx-dei-action set-to-zero",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure network-port network-1-1-1-1",
        ),
    ),
    ConfigLine(
        config_line="      tx-dei-tag-type ctag-or-stag",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure network-port network-1-1-1-1",
        ),
    ),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="network-element ne-1", parents=()),
    ConfigLine(config_line="  configure tm-params bwp-mode information-rate", parents=("network-element ne-1",)),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="configure communication", parents=()),
    ConfigLine(config_line="  configure mgmttnl mgmt_tnl-1", parents=("configure communication",)),
    ConfigLine(
        config_line="    dhcp-client-id-control disabled",
        parents=("configure communication", "  configure mgmttnl mgmt_tnl-1"),
    ),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="network-element ne-1", parents=()),
    ConfigLine(config_line="  configure nte nte114pro-1-1-1", parents=("network-element ne-1",)),
    ConfigLine(
        config_line="    configure access-port access-1-1-1-2",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1"),
    ),
    ConfigLine(
        config_line="      configure flow flow-1-1-1-2-1",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-2"),
    ),
    ConfigLine(
        config_line="        access-interface access-1-1-1-2 network-interface network-1-1-1-1 push 2-0 none n2a-prio-mapping-profile none a2n-prio-mapping-profile none eompls-pw none",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-2",
            "      configure flow flow-1-1-1-2-1",
        ),
    ),
    ConfigLine(
        config_line="        access-max-forwarding-entries 4096",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-2",
            "      configure flow flow-1-1-1-2-1",
        ),
    ),
    ConfigLine(
        config_line="        network-max-forwarding-entries 4096",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-2",
            "      configure flow flow-1-1-1-2-1",
        ),
    ),
    ConfigLine(
        config_line="        cpd-filter bpdu use-mac-setting",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-2",
            "      configure flow flow-1-1-1-2-1",
        ),
    ),
    ConfigLine(
        config_line="        cpd-filter pause use-mac-setting",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-2",
            "      configure flow flow-1-1-1-2-1",
        ),
    ),
    ConfigLine(
        config_line="        cpd-filter lacp use-mac-setting",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-2",
            "      configure flow flow-1-1-1-2-1",
        ),
    ),
    ConfigLine(
        config_line="        cpd-filter lacp-marker use-mac-setting",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-2",
            "      configure flow flow-1-1-1-2-1",
        ),
    ),
    ConfigLine(
        config_line="        cpd-filter efm-oam use-mac-setting",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-2",
            "      configure flow flow-1-1-1-2-1",
        ),
    ),
    ConfigLine(
        config_line="        cpd-filter port-authen use-mac-setting",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-2",
            "      configure flow flow-1-1-1-2-1",
        ),
    ),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="network-element ne-1", parents=()),
    ConfigLine(config_line="  configure nte nte114pro-1-1-1", parents=("network-element ne-1",)),
    ConfigLine(
        config_line="    configure access-port access-1-1-1-2",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1"),
    ),
    ConfigLine(
        config_line="      configure flow flow-1-1-1-2-1",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-2"),
    ),
    ConfigLine(
        config_line="        configure a2n-policer a2n_policer-1-1-1-2-1-0",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-2",
            "      configure flow flow-1-1-1-2-1",
        ),
    ),
    ConfigLine(
        config_line="          cir 0",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-2",
            "      configure flow flow-1-1-1-2-1",
            "        configure a2n-policer a2n_policer-1-1-1-2-1-0",
        ),
    ),
    ConfigLine(
        config_line="          eir 0",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-2",
            "      configure flow flow-1-1-1-2-1",
            "        configure a2n-policer a2n_policer-1-1-1-2-1-0",
        ),
    ),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="network-element ne-1", parents=()),
    ConfigLine(config_line="  configure nte nte114pro-1-1-1", parents=("network-element ne-1",)),
    ConfigLine(
        config_line="    configure access-port access-1-1-1-3",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1"),
    ),
    ConfigLine(
        config_line='      add flow flow-1-1-1-3-1 "WTRL" regular-evc disabled disabled disabled disabled 0 disabled none none "1138-*" 100160000 0 access-interface access-1-1-1-3 network-interface network-1-1-1-1 flow-based n2a-prio-mapping-profile none a2n-prio-mapping-profile none',
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      configure flow flow-1-1-1-3-1",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="        policing-control a2n",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-3",
            "      configure flow flow-1-1-1-3-1",
        ),
    ),
    ConfigLine(
        config_line="        access-max-forwarding-entries 4096",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-3",
            "      configure flow flow-1-1-1-3-1",
        ),
    ),
    ConfigLine(
        config_line="        network-max-forwarding-entries 4096",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-3",
            "      configure flow flow-1-1-1-3-1",
        ),
    ),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="network-element ne-1", parents=()),
    ConfigLine(config_line="  configure nte nte114pro-1-1-1", parents=("network-element ne-1",)),
    ConfigLine(
        config_line="    configure access-port access-1-1-1-3",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1"),
    ),
    ConfigLine(
        config_line="      configure flow flow-1-1-1-3-1",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="        configure a2n-shaper a2n_shaper-1-1-1-3-1-0",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-3",
            "      configure flow flow-1-1-1-3-1",
        ),
    ),
    ConfigLine(
        config_line="          buffersize 512",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-3",
            "      configure flow flow-1-1-1-3-1",
            "        configure a2n-shaper a2n_shaper-1-1-1-3-1-0",
        ),
    ),
    ConfigLine(
        config_line="          back",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-3",
            "      configure flow flow-1-1-1-3-1",
            "        configure a2n-shaper a2n_shaper-1-1-1-3-1-0",
        ),
    ),
    ConfigLine(
        config_line="        configure a2n-shaper a2n_shaper-1-1-1-3-1-0",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-3",
            "      configure flow flow-1-1-1-3-1",
        ),
    ),
    ConfigLine(
        config_line="          soam-cir 128000",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-3",
            "      configure flow flow-1-1-1-3-1",
            "        configure a2n-shaper a2n_shaper-1-1-1-3-1-0",
        ),
    ),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="network-element ne-1", parents=()),
    ConfigLine(config_line="  configure nte nte114pro-1-1-1", parents=("network-element ne-1",)),
    ConfigLine(
        config_line="    configure access-port access-1-1-1-3",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1"),
    ),
    ConfigLine(
        config_line="      configure flow flow-1-1-1-3-1",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="        configure a2n-policer a2n_policer-1-1-1-3-1-0",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-3",
            "      configure flow flow-1-1-1-3-1",
        ),
    ),
    ConfigLine(
        config_line="          cbs 512",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-3",
            "      configure flow flow-1-1-1-3-1",
            "        configure a2n-policer a2n_policer-1-1-1-3-1-0",
        ),
    ),
    ConfigLine(
        config_line="          cir 100032000",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-3",
            "      configure flow flow-1-1-1-3-1",
            "        configure a2n-policer a2n_policer-1-1-1-3-1-0",
        ),
    ),
    ConfigLine(
        config_line="          color-mode color-blind",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-3",
            "      configure flow flow-1-1-1-3-1",
            "        configure a2n-policer a2n_policer-1-1-1-3-1-0",
        ),
    ),
    ConfigLine(
        config_line="          eir 0",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-3",
            "      configure flow flow-1-1-1-3-1",
            "        configure a2n-policer a2n_policer-1-1-1-3-1-0",
        ),
    ),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="network-element ne-1", parents=()),
    ConfigLine(config_line="  configure nte nte114pro-1-1-1", parents=("network-element ne-1",)),
    ConfigLine(
        config_line="    configure access-port access-1-1-1-3",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1"),
    ),
    ConfigLine(
        config_line="      configure flow flow-1-1-1-3-1",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="        configure n2a-policer n2a_policer-1-1-1-3-1-0",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-3",
            "      configure flow flow-1-1-1-3-1",
        ),
    ),
    ConfigLine(
        config_line="          policing-enabled disabled",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-3",
            "      configure flow flow-1-1-1-3-1",
            "        configure n2a-policer n2a_policer-1-1-1-3-1-0",
        ),
    ),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="network-element ne-1", parents=()),
    ConfigLine(config_line="  configure nte nte114pro-1-1-1", parents=("network-element ne-1",)),
    ConfigLine(
        config_line="    configure access-port access-1-1-1-3",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1"),
    ),
    ConfigLine(
        config_line='      add flow flow-1-1-1-3-2 "MGMT" regular-evc disabled disabled disabled disabled 0 disabled none none "42-*" 10176000 0 access-interface access-1-1-1-3 network-interface network-1-1-1-1 flow-based n2a-prio-mapping-profile none a2n-prio-mapping-profile none',
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="      configure flow flow-1-1-1-3-2",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="        policing-control a2n",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-3",
            "      configure flow flow-1-1-1-3-2",
        ),
    ),
    ConfigLine(
        config_line="        access-max-forwarding-entries 4096",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-3",
            "      configure flow flow-1-1-1-3-2",
        ),
    ),
    ConfigLine(
        config_line="        network-max-forwarding-entries 4096",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-3",
            "      configure flow flow-1-1-1-3-2",
        ),
    ),
    ConfigLine(
        config_line="        cpd-filter bpdu use-mac-setting",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-3",
            "      configure flow flow-1-1-1-3-2",
        ),
    ),
    ConfigLine(
        config_line="        cpd-filter pause use-mac-setting",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-3",
            "      configure flow flow-1-1-1-3-2",
        ),
    ),
    ConfigLine(
        config_line="        cpd-filter lacp use-mac-setting",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-3",
            "      configure flow flow-1-1-1-3-2",
        ),
    ),
    ConfigLine(
        config_line="        cpd-filter lacp-marker use-mac-setting",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-3",
            "      configure flow flow-1-1-1-3-2",
        ),
    ),
    ConfigLine(
        config_line="        cpd-filter efm-oam use-mac-setting",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-3",
            "      configure flow flow-1-1-1-3-2",
        ),
    ),
    ConfigLine(
        config_line="        cpd-filter port-authen use-mac-setting",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-3",
            "      configure flow flow-1-1-1-3-2",
        ),
    ),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="network-element ne-1", parents=()),
    ConfigLine(config_line="  configure nte nte114pro-1-1-1", parents=("network-element ne-1",)),
    ConfigLine(
        config_line="    configure access-port access-1-1-1-3",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1"),
    ),
    ConfigLine(
        config_line="      configure flow flow-1-1-1-3-2",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="        configure a2n-shaper a2n_shaper-1-1-1-3-2-0",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-3",
            "      configure flow flow-1-1-1-3-2",
        ),
    ),
    ConfigLine(
        config_line="          buffersize 512",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-3",
            "      configure flow flow-1-1-1-3-2",
            "        configure a2n-shaper a2n_shaper-1-1-1-3-2-0",
        ),
    ),
    ConfigLine(
        config_line="          back",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-3",
            "      configure flow flow-1-1-1-3-2",
            "        configure a2n-shaper a2n_shaper-1-1-1-3-2-0",
        ),
    ),
    ConfigLine(
        config_line="        configure a2n-shaper a2n_shaper-1-1-1-3-2-0",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-3",
            "      configure flow flow-1-1-1-3-2",
        ),
    ),
    ConfigLine(
        config_line="          soam-cir 128000",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-3",
            "      configure flow flow-1-1-1-3-2",
            "        configure a2n-shaper a2n_shaper-1-1-1-3-2-0",
        ),
    ),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="network-element ne-1", parents=()),
    ConfigLine(config_line="  configure nte nte114pro-1-1-1", parents=("network-element ne-1",)),
    ConfigLine(
        config_line="    configure access-port access-1-1-1-3",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1"),
    ),
    ConfigLine(
        config_line="      configure flow flow-1-1-1-3-2",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="        configure a2n-policer a2n_policer-1-1-1-3-2-0",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-3",
            "      configure flow flow-1-1-1-3-2",
        ),
    ),
    ConfigLine(
        config_line="          cbs 512",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-3",
            "      configure flow flow-1-1-1-3-2",
            "        configure a2n-policer a2n_policer-1-1-1-3-2-0",
        ),
    ),
    ConfigLine(
        config_line="          cir 10048000",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-3",
            "      configure flow flow-1-1-1-3-2",
            "        configure a2n-policer a2n_policer-1-1-1-3-2-0",
        ),
    ),
    ConfigLine(
        config_line="          color-mode color-blind",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-3",
            "      configure flow flow-1-1-1-3-2",
            "        configure a2n-policer a2n_policer-1-1-1-3-2-0",
        ),
    ),
    ConfigLine(
        config_line="          eir 0",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-3",
            "      configure flow flow-1-1-1-3-2",
            "        configure a2n-policer a2n_policer-1-1-1-3-2-0",
        ),
    ),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="network-element ne-1", parents=()),
    ConfigLine(config_line="  configure nte nte114pro-1-1-1", parents=("network-element ne-1",)),
    ConfigLine(
        config_line="    configure access-port access-1-1-1-3",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1"),
    ),
    ConfigLine(
        config_line="      configure flow flow-1-1-1-3-2",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="        configure n2a-policer n2a_policer-1-1-1-3-2-0",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-3",
            "      configure flow flow-1-1-1-3-2",
        ),
    ),
    ConfigLine(
        config_line="          policing-enabled disabled",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-3",
            "      configure flow flow-1-1-1-3-2",
            "        configure n2a-policer n2a_policer-1-1-1-3-2-0",
        ),
    ),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="network-element ne-1", parents=()),
    ConfigLine(config_line="  configure nte nte114pro-1-1-1", parents=("network-element ne-1",)),
    ConfigLine(
        config_line="    configure access-port access-1-1-1-4",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1"),
    ),
    ConfigLine(
        config_line='      add flow flow-1-1-1-4-1 "INITECH" regular-evc disabled disabled disabled disabled 0 disabled none push 1-0 "1999-*" 200000000 0 access-interface access-1-1-1-4 network-interface network-1-1-1-1 flow-based n2a-prio-mapping-profile none a2n-prio-mapping-profile none',
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-4"),
    ),
    ConfigLine(
        config_line="      configure flow flow-1-1-1-4-1",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-4"),
    ),
    ConfigLine(
        config_line="        access-max-forwarding-entries 4096",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-4",
            "      configure flow flow-1-1-1-4-1",
        ),
    ),
    ConfigLine(
        config_line="        network-max-forwarding-entries 4096",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-4",
            "      configure flow flow-1-1-1-4-1",
        ),
    ),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="network-element ne-1", parents=()),
    ConfigLine(config_line="  configure nte nte114pro-1-1-1", parents=("network-element ne-1",)),
    ConfigLine(
        config_line="    configure access-port access-1-1-1-4",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1"),
    ),
    ConfigLine(
        config_line="      configure flow flow-1-1-1-4-1",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-4"),
    ),
    ConfigLine(
        config_line="        configure a2n-shaper a2n_shaper-1-1-1-4-1-0",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-4",
            "      configure flow flow-1-1-1-4-1",
        ),
    ),
    ConfigLine(
        config_line="          buffersize 512",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-4",
            "      configure flow flow-1-1-1-4-1",
            "        configure a2n-shaper a2n_shaper-1-1-1-4-1-0",
        ),
    ),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="network-element ne-1", parents=()),
    ConfigLine(config_line="  configure nte nte114pro-1-1-1", parents=("network-element ne-1",)),
    ConfigLine(
        config_line="    configure access-port access-1-1-1-4",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1"),
    ),
    ConfigLine(
        config_line="      configure flow flow-1-1-1-4-1",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-4"),
    ),
    ConfigLine(
        config_line="        configure a2n-policer a2n_policer-1-1-1-4-1-0",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-4",
            "      configure flow flow-1-1-1-4-1",
        ),
    ),
    ConfigLine(
        config_line="          cbs 512",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-4",
            "      configure flow flow-1-1-1-4-1",
            "        configure a2n-policer a2n_policer-1-1-1-4-1-0",
        ),
    ),
    ConfigLine(
        config_line="          cir 200000000",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-4",
            "      configure flow flow-1-1-1-4-1",
            "        configure a2n-policer a2n_policer-1-1-1-4-1-0",
        ),
    ),
    ConfigLine(
        config_line="          eir 0",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-4",
            "      configure flow flow-1-1-1-4-1",
            "        configure a2n-policer a2n_policer-1-1-1-4-1-0",
        ),
    ),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="network-element ne-1", parents=()),
    ConfigLine(config_line="  configure nte nte114pro-1-1-1", parents=("network-element ne-1",)),
    ConfigLine(
        config_line="    configure access-port access-1-1-1-2",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1"),
    ),
    ConfigLine(
        config_line="      configure n2a-shaper port_n2a_shaper-1-1-1-2-0",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-2"),
    ),
    ConfigLine(
        config_line="        buffersize 10",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-2",
            "      configure n2a-shaper port_n2a_shaper-1-1-1-2-0",
        ),
    ),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="network-element ne-1", parents=()),
    ConfigLine(config_line="  configure nte nte114pro-1-1-1", parents=("network-element ne-1",)),
    ConfigLine(
        config_line="    configure access-port access-1-1-1-3",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1"),
    ),
    ConfigLine(
        config_line="      configure n2a-shaper port_n2a_shaper-1-1-1-3-0",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(
        config_line="        buffersize 1024",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-3",
            "      configure n2a-shaper port_n2a_shaper-1-1-1-3-0",
        ),
    ),
    ConfigLine(
        config_line="        soam-cir 128000",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-3",
            "      configure n2a-shaper port_n2a_shaper-1-1-1-3-0",
        ),
    ),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="network-element ne-1", parents=()),
    ConfigLine(config_line="  configure nte nte114pro-1-1-1", parents=("network-element ne-1",)),
    ConfigLine(
        config_line="    configure access-port access-1-1-1-4",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1"),
    ),
    ConfigLine(
        config_line="      configure n2a-shaper port_n2a_shaper-1-1-1-4-0",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-4"),
    ),
    ConfigLine(
        config_line="        buffersize 512",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure access-port access-1-1-1-4",
            "      configure n2a-shaper port_n2a_shaper-1-1-1-4-0",
        ),
    ),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="network-element ne-1", parents=()),
    ConfigLine(config_line="  configure nte nte114pro-1-1-1", parents=("network-element ne-1",)),
    ConfigLine(
        config_line="    configure access-port access-1-1-1-3",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1"),
    ),
    ConfigLine(
        config_line="      admin-state in-service",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-3"),
    ),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="network-element ne-1", parents=()),
    ConfigLine(config_line="  configure nte nte114pro-1-1-1", parents=("network-element ne-1",)),
    ConfigLine(
        config_line="    configure access-port access-1-1-1-4",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1"),
    ),
    ConfigLine(
        config_line="      admin-state in-service",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1", "    configure access-port access-1-1-1-4"),
    ),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="network-element ne-1", parents=()),
    ConfigLine(config_line="  configure nte nte114pro-1-1-1", parents=("network-element ne-1",)),
    ConfigLine(
        config_line="    configure network-port network-1-1-1-1",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1"),
    ),
    ConfigLine(
        config_line="      lldp",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure network-port network-1-1-1-1",
        ),
    ),
    ConfigLine(
        config_line="        configure net-port-config 1",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure network-port network-1-1-1-1",
            "      lldp",
        ),
    ),
    ConfigLine(
        config_line="          admin-status tx-and-rx",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure network-port network-1-1-1-1",
            "      lldp",
            "        configure net-port-config 1",
        ),
    ),
    ConfigLine(
        config_line="          basic-tlv-supported port-description,sys-cap,sys-description,sys-name",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure network-port network-1-1-1-1",
            "      lldp",
            "        configure net-port-config 1",
        ),
    ),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="network-element ne-1", parents=()),
    ConfigLine(config_line="  configure nte nte114pro-1-1-1", parents=("network-element ne-1",)),
    ConfigLine(
        config_line="    configure network-port network-1-1-1-1",
        parents=("network-element ne-1", "  configure nte nte114pro-1-1-1"),
    ),
    ConfigLine(
        config_line="      lldp",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure network-port network-1-1-1-1",
        ),
    ),
    ConfigLine(
        config_line="        configure net-port-config 1",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure network-port network-1-1-1-1",
            "      lldp",
        ),
    ),
    ConfigLine(
        config_line="          add management-address-interface mgmt_tnl-1 enabled",
        parents=(
            "network-element ne-1",
            "  configure nte nte114pro-1-1-1",
            "    configure network-port network-1-1-1-1",
            "      lldp",
            "        configure net-port-config 1",
        ),
    ),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="configure communication", parents=()),
    ConfigLine(
        config_line='  add ip-route nexthop 0.0.0.0 0.0.0.0 203.0.113.49 "LTP" 1 disabled',
        parents=("configure communication",),
    ),
    ConfigLine(config_line="home", parents=()),
    ConfigLine(config_line="admin config-file", parents=()),
]
