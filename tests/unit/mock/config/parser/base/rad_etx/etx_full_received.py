from netutils.config.parser import ConfigLine

data = [
    ConfigLine(config_line='echo "Terminal Configuration"', parents=()),
    ConfigLine(config_line="terminal", parents=()),
    ConfigLine(config_line="    timeout forever", parents=("terminal",)),
    ConfigLine(config_line='echo "System Configuration"', parents=()),
    ConfigLine(config_line="system", parents=()),
    ConfigLine(config_line='    name "ETX001"', parents=("system",)),
    ConfigLine(config_line='    echo "LLDP Configuration"', parents=("system",)),
    ConfigLine(config_line="    lldp", parents=("system",)),
    ConfigLine(config_line="        no shutdown", parents=("system", "    lldp")),
    ConfigLine(config_line='echo "Management configuration"', parents=()),
    ConfigLine(config_line="management", parents=()),
    ConfigLine(config_line='    login-user "net-creds-1"', parents=("management",)),
    ConfigLine(config_line="        level su", parents=("management", '    login-user "net-creds-1"')),
    ConfigLine(
        config_line='        password "abcdefghijklmnopqrstuvwxyz123456789abcde" hash',
        parents=("management", '    login-user "net-creds-1"'),
    ),
    ConfigLine(config_line="        no shutdown", parents=("management", '    login-user "net-creds-1"')),
    ConfigLine(config_line='    login-user "net-creds-2"', parents=("management",)),
    ConfigLine(config_line="        level oper", parents=("management", '    login-user "net-creds-2"')),
    ConfigLine(
        config_line='        password "abcdefghijklmnopqrstuvwxyz123456789zyxwv" hash',
        parents=("management", '    login-user "net-creds-2"'),
    ),
    ConfigLine(config_line="        no shutdown", parents=("management", '    login-user "net-creds-2"')),
    ConfigLine(config_line='    echo "SNMP Configuration"', parents=("management",)),
    ConfigLine(config_line="    snmp", parents=("management",)),
    ConfigLine(config_line='        user "snmpv2" none-auth', parents=("management", "    snmp")),
    ConfigLine(
        config_line="            no shutdown", parents=("management", "    snmp", '        user "snmpv2" none-auth')
    ),
    ConfigLine(config_line='        access-group "snmpv2" snmpv2c no-auth-no-priv', parents=("management", "    snmp")),
    ConfigLine(
        config_line='            read-view "ntc"',
        parents=("management", "    snmp", '        access-group "snmpv2" snmpv2c no-auth-no-priv'),
    ),
    ConfigLine(
        config_line='            write-view "ntc"',
        parents=("management", "    snmp", '        access-group "snmpv2" snmpv2c no-auth-no-priv'),
    ),
    ConfigLine(
        config_line='            notify-view "ntc"',
        parents=("management", "    snmp", '        access-group "snmpv2" snmpv2c no-auth-no-priv'),
    ),
    ConfigLine(
        config_line="            no shutdown",
        parents=("management", "    snmp", '        access-group "snmpv2" snmpv2c no-auth-no-priv'),
    ),
    ConfigLine(
        config_line='        access-group "v2_read" snmpv2c no-auth-no-priv', parents=("management", "    snmp")
    ),
    ConfigLine(
        config_line='            write-view "ntc"',
        parents=("management", "    snmp", '        access-group "v2_read" snmpv2c no-auth-no-priv'),
    ),
    ConfigLine(config_line='        security-to-group snmpv2c sec-name "snmpv2"', parents=("management", "    snmp")),
    ConfigLine(
        config_line='            group-name "snmpv2"',
        parents=("management", "    snmp", '        security-to-group snmpv2c sec-name "snmpv2"'),
    ),
    ConfigLine(
        config_line="            no shutdown",
        parents=("management", "    snmp", '        security-to-group snmpv2c sec-name "snmpv2"'),
    ),
    ConfigLine(config_line='        community "ntccommunity"', parents=("management", "    snmp")),
    ConfigLine(
        config_line='            name "ntccommunity"',
        parents=("management", "    snmp", '        community "ntccommunity"'),
    ),
    ConfigLine(
        config_line='            sec-name "v2_write"',
        parents=("management", "    snmp", '        community "ntccommunity"'),
    ),
    ConfigLine(
        config_line="            no shutdown", parents=("management", "    snmp", '        community "ntccommunity"')
    ),
    ConfigLine(config_line='        community "public"', parents=("management", "    snmp")),
    ConfigLine(
        config_line='            name "public"', parents=("management", "    snmp", '        community "public"')
    ),
    ConfigLine(
        config_line='            sec-name "v2_read"', parents=("management", "    snmp", '        community "public"')
    ),
    ConfigLine(config_line="            no shutdown", parents=("management", "    snmp", '        community "public"')),
    ConfigLine(config_line='        community "read"', parents=("management", "    snmp")),
    ConfigLine(
        config_line='            name "private"', parents=("management", "    snmp", '        community "read"')
    ),
    ConfigLine(
        config_line='            sec-name "v2_read"', parents=("management", "    snmp", '        community "read"')
    ),
    ConfigLine(config_line="            no shutdown", parents=("management", "    snmp", '        community "read"')),
    ConfigLine(config_line='        community "trap"', parents=("management", "    snmp")),
    ConfigLine(
        config_line='            name "private"', parents=("management", "    snmp", '        community "trap"')
    ),
    ConfigLine(
        config_line='            sec-name "v2_trap"', parents=("management", "    snmp", '        community "trap"')
    ),
    ConfigLine(config_line="            no shutdown", parents=("management", "    snmp", '        community "trap"')),
    ConfigLine(config_line='        community "trapCommunity"', parents=("management", "    snmp")),
    ConfigLine(
        config_line='            name "trapCommunity"',
        parents=("management", "    snmp", '        community "trapCommunity"'),
    ),
    ConfigLine(
        config_line='            sec-name "v2_trap"',
        parents=("management", "    snmp", '        community "trapCommunity"'),
    ),
    ConfigLine(
        config_line="            no shutdown", parents=("management", "    snmp", '        community "trapCommunity"')
    ),
    ConfigLine(config_line='        community "write"', parents=("management", "    snmp")),
    ConfigLine(
        config_line='            name "private"', parents=("management", "    snmp", '        community "write"')
    ),
    ConfigLine(
        config_line='            sec-name "v2_write"', parents=("management", "    snmp", '        community "write"')
    ),
    ConfigLine(config_line="            no shutdown", parents=("management", "    snmp", '        community "write"')),
    ConfigLine(config_line='        target-params "example1"', parents=("management", "    snmp")),
    ConfigLine(
        config_line="            message-processing-model snmpv2c",
        parents=("management", "    snmp", '        target-params "example1"'),
    ),
    ConfigLine(
        config_line="            version snmpv2c",
        parents=("management", "    snmp", '        target-params "example1"'),
    ),
    ConfigLine(
        config_line='            security name "v2_trap" level no-auth-no-priv',
        parents=("management", "    snmp", '        target-params "example1"'),
    ),
    ConfigLine(
        config_line="            no shutdown", parents=("management", "    snmp", '        target-params "example1"')
    ),
    ConfigLine(config_line='        target-params "example2"', parents=("management", "    snmp")),
    ConfigLine(
        config_line="            message-processing-model snmpv2c",
        parents=("management", "    snmp", '        target-params "example2"'),
    ),
    ConfigLine(
        config_line="            version snmpv2c",
        parents=("management", "    snmp", '        target-params "example2"'),
    ),
    ConfigLine(
        config_line='            security name "v2_trap" level no-auth-no-priv',
        parents=("management", "    snmp", '        target-params "example2"'),
    ),
    ConfigLine(
        config_line="            no shutdown", parents=("management", "    snmp", '        target-params "example2"')
    ),
    ConfigLine(config_line="        config-change-notification", parents=("management", "    snmp")),
    ConfigLine(config_line='echo "Port Configuration"', parents=()),
    ConfigLine(config_line="port", parents=()),
    ConfigLine(config_line='    l2cp-profile "network"', parents=("port",)),
    ConfigLine(config_line='        mac "01-80-c2-00-00-02" peer', parents=("port", '    l2cp-profile "network"')),
    ConfigLine(config_line='        mac "01-80-c2-00-00-0e" peer', parents=("port", '    l2cp-profile "network"')),
    ConfigLine(config_line='    l2cp-profile "EXAMPLE-ONE"', parents=("port",)),
    ConfigLine(
        config_line='        mac "01-80-c2-00-00-01" discard', parents=("port", '    l2cp-profile "EXAMPLE-ONE"')
    ),
    ConfigLine(config_line='    l2cp-profile "EXAMPLE-TWO"', parents=("port",)),
    ConfigLine(config_line='        mac "01-80-c2-00-00-02" peer', parents=("port", '    l2cp-profile "EXAMPLE-TWO"')),
    ConfigLine(config_line='        mac "01-80-c2-00-00-0e" peer', parents=("port", '    l2cp-profile "EXAMPLE-TWO"')),
    ConfigLine(config_line='    l2cp-profile "EXAMPLE-THREE"', parents=("port",)),
    ConfigLine(
        config_line='        mac "01-80-c2-00-00-00" discard', parents=("port", '    l2cp-profile "EXAMPLE-THREE"')
    ),
    ConfigLine(
        config_line='        mac "01-80-c2-00-00-01" discard', parents=("port", '    l2cp-profile "EXAMPLE-THREE"')
    ),
    ConfigLine(
        config_line='        mac "01-80-c2-00-00-02" discard', parents=("port", '    l2cp-profile "EXAMPLE-THREE"')
    ),
    ConfigLine(
        config_line='        mac "01-80-c2-00-00-03" discard', parents=("port", '    l2cp-profile "EXAMPLE-THREE"')
    ),
    ConfigLine(
        config_line='        mac "01-80-c2-00-00-04" discard', parents=("port", '    l2cp-profile "EXAMPLE-THREE"')
    ),
    ConfigLine(
        config_line='        mac "01-80-c2-00-00-05" discard', parents=("port", '    l2cp-profile "EXAMPLE-THREE"')
    ),
    ConfigLine(
        config_line='        mac "01-80-c2-00-00-06" discard', parents=("port", '    l2cp-profile "EXAMPLE-THREE"')
    ),
    ConfigLine(
        config_line='        mac "01-80-c2-00-00-07" discard', parents=("port", '    l2cp-profile "EXAMPLE-THREE"')
    ),
    ConfigLine(
        config_line='        mac "01-80-c2-00-00-08" discard', parents=("port", '    l2cp-profile "EXAMPLE-THREE"')
    ),
    ConfigLine(
        config_line='        mac "01-80-c2-00-00-09" discard', parents=("port", '    l2cp-profile "EXAMPLE-THREE"')
    ),
    ConfigLine(
        config_line='        mac "01-80-c2-00-00-0a" discard', parents=("port", '    l2cp-profile "EXAMPLE-THREE"')
    ),
    ConfigLine(
        config_line='        mac "01-80-c2-00-00-0b" discard', parents=("port", '    l2cp-profile "EXAMPLE-THREE"')
    ),
    ConfigLine(
        config_line='        mac "01-80-c2-00-00-0c" discard', parents=("port", '    l2cp-profile "EXAMPLE-THREE"')
    ),
    ConfigLine(
        config_line='        mac "01-80-c2-00-00-0d" discard', parents=("port", '    l2cp-profile "EXAMPLE-THREE"')
    ),
    ConfigLine(
        config_line='        mac "01-80-c2-00-00-0e" discard', parents=("port", '    l2cp-profile "EXAMPLE-THREE"')
    ),
    ConfigLine(
        config_line='        mac "01-80-c2-00-00-0f" discard', parents=("port", '    l2cp-profile "EXAMPLE-THREE"')
    ),
    ConfigLine(
        config_line='        mac "01-80-c2-00-00-10" discard', parents=("port", '    l2cp-profile "EXAMPLE-THREE"')
    ),
    ConfigLine(
        config_line='        mac "01-80-c2-00-00-20" discard', parents=("port", '    l2cp-profile "EXAMPLE-THREE"')
    ),
    ConfigLine(
        config_line='        mac "01-80-c2-00-00-21" discard', parents=("port", '    l2cp-profile "EXAMPLE-THREE"')
    ),
    ConfigLine(
        config_line='        mac "01-80-c2-00-00-22" discard', parents=("port", '    l2cp-profile "EXAMPLE-THREE"')
    ),
    ConfigLine(
        config_line='        mac "01-80-c2-00-00-23" discard', parents=("port", '    l2cp-profile "EXAMPLE-THREE"')
    ),
    ConfigLine(
        config_line='        mac "01-80-c2-00-00-24" discard', parents=("port", '    l2cp-profile "EXAMPLE-THREE"')
    ),
    ConfigLine(
        config_line='        mac "01-80-c2-00-00-25" discard', parents=("port", '    l2cp-profile "EXAMPLE-THREE"')
    ),
    ConfigLine(
        config_line='        mac "01-80-c2-00-00-26" discard', parents=("port", '    l2cp-profile "EXAMPLE-THREE"')
    ),
    ConfigLine(
        config_line='        mac "01-80-c2-00-00-27" discard', parents=("port", '    l2cp-profile "EXAMPLE-THREE"')
    ),
    ConfigLine(
        config_line='        mac "01-80-c2-00-00-28" discard', parents=("port", '    l2cp-profile "EXAMPLE-THREE"')
    ),
    ConfigLine(
        config_line='        mac "01-80-c2-00-00-29" discard', parents=("port", '    l2cp-profile "EXAMPLE-THREE"')
    ),
    ConfigLine(
        config_line='        mac "01-80-c2-00-00-2a" discard', parents=("port", '    l2cp-profile "EXAMPLE-THREE"')
    ),
    ConfigLine(
        config_line='        mac "01-80-c2-00-00-2b" discard', parents=("port", '    l2cp-profile "EXAMPLE-THREE"')
    ),
    ConfigLine(
        config_line='        mac "01-80-c2-00-00-2c" discard', parents=("port", '    l2cp-profile "EXAMPLE-THREE"')
    ),
    ConfigLine(
        config_line='        mac "01-80-c2-00-00-2d" discard', parents=("port", '    l2cp-profile "EXAMPLE-THREE"')
    ),
    ConfigLine(
        config_line='        mac "01-80-c2-00-00-2e" discard', parents=("port", '    l2cp-profile "EXAMPLE-THREE"')
    ),
    ConfigLine(
        config_line='        mac "01-80-c2-00-00-2f" discard', parents=("port", '    l2cp-profile "EXAMPLE-THREE"')
    ),
    ConfigLine(
        config_line='        mac "01-00-0c-cc-cc-cc" discard', parents=("port", '    l2cp-profile "EXAMPLE-THREE"')
    ),
    ConfigLine(
        config_line='        mac "01-00-0c-cc-cc-cd" discard', parents=("port", '    l2cp-profile "EXAMPLE-THREE"')
    ),
    ConfigLine(config_line="        default discard", parents=("port", '    l2cp-profile "EXAMPLE-THREE"')),
    ConfigLine(config_line='    l2cp-profile "EXAMPLE-FOUR"', parents=("port",)),
    ConfigLine(config_line="    ethernet 1/1", parents=("port",)),
    ConfigLine(config_line="        shutdown", parents=("port", "    ethernet 1/1")),
    ConfigLine(config_line="        no auto-negotiation", parents=("port", "    ethernet 1/1")),
    ConfigLine(config_line="        speed-duplex 1000-full-duplex", parents=("port", "    ethernet 1/1")),
    ConfigLine(config_line="        egress-mtu 9200", parents=("port", "    ethernet 1/1")),
    ConfigLine(config_line='        l2cp profile "network"', parents=("port", "    ethernet 1/1")),
    ConfigLine(config_line="        lldp", parents=("port", "    ethernet 1/1")),
    ConfigLine(
        config_line="            nearest-bridge-mode tx-rx", parents=("port", "    ethernet 1/1", "        lldp")
    ),
    ConfigLine(
        config_line="            nearest-bridge-basic-management port-description sys-name sys-description sys-capabilities management-address",
        parents=("port", "    ethernet 1/1", "        lldp"),
    ),
    ConfigLine(
        config_line="            nearest-bridge-802.3 max-frame-size",
        parents=("port", "    ethernet 1/1", "        lldp"),
    ),
    ConfigLine(config_line="    ethernet 1/2", parents=("port",)),
    ConfigLine(config_line="        shutdown", parents=("port", "    ethernet 1/2")),
    ConfigLine(config_line='        name "description for eth1/2"', parents=("port", "    ethernet 1/2")),
    ConfigLine(config_line="        egress-mtu 9000", parents=("port", "    ethernet 1/2")),
    ConfigLine(config_line="    ethernet 1/3", parents=("port",)),
    ConfigLine(config_line='        name "description for eth1/3"', parents=("port", "    ethernet 1/3")),
    ConfigLine(config_line="        speed-duplex 1000-full-duplex", parents=("port", "    ethernet 1/3")),
    ConfigLine(config_line="        egress-mtu 12000", parents=("port", "    ethernet 1/3")),
    ConfigLine(config_line='        l2cp profile "network"', parents=("port", "    ethernet 1/3")),
    ConfigLine(config_line="        lldp", parents=("port", "    ethernet 1/3")),
    ConfigLine(
        config_line="            nearest-bridge-mode tx-rx", parents=("port", "    ethernet 1/3", "        lldp")
    ),
    ConfigLine(
        config_line="            nearest-bridge-basic-management port-description sys-name sys-description sys-capabilities management-address",
        parents=("port", "    ethernet 1/3", "        lldp"),
    ),
    ConfigLine(
        config_line="            nearest-bridge-802.3 max-frame-size",
        parents=("port", "    ethernet 1/3", "        lldp"),
    ),
    ConfigLine(config_line="    ethernet 1/4", parents=("port",)),
    ConfigLine(config_line='        name "description for eth1/4"', parents=("port", "    ethernet 1/4")),
    ConfigLine(config_line="        tag-ethernet-type 0x88a8", parents=("port", "    ethernet 1/4")),
    ConfigLine(config_line="        egress-mtu 12000", parents=("port", "    ethernet 1/4")),
    ConfigLine(config_line='        l2cp profile "EXAMPLE-THREE"', parents=("port", "    ethernet 1/4")),
    ConfigLine(config_line="    ethernet 1/5", parents=("port",)),
    ConfigLine(config_line='        name "description for eth1/5"', parents=("port", "    ethernet 1/5")),
    ConfigLine(config_line="        egress-mtu 12000", parents=("port", "    ethernet 1/5")),
    ConfigLine(config_line='        l2cp profile "EXAMPLE-ONE"', parents=("port", "    ethernet 1/5")),
    ConfigLine(config_line="    ethernet 1/6", parents=("port",)),
    ConfigLine(config_line='        name "description for eth1/6"', parents=("port", "    ethernet 1/6")),
    ConfigLine(config_line="        egress-mtu 9000", parents=("port", "    ethernet 1/6")),
    ConfigLine(config_line="    ethernet 1/7", parents=("port",)),
    ConfigLine(config_line='        name "description for eth1/7"', parents=("port", "    ethernet 1/7")),
    ConfigLine(config_line="        egress-mtu 12000", parents=("port", "    ethernet 1/7")),
    ConfigLine(config_line='        l2cp profile "EXAMPLE-ONE"', parents=("port", "    ethernet 1/7")),
    ConfigLine(config_line="    ethernet 1/8", parents=("port",)),
    ConfigLine(config_line='        name "description for eth1/8"', parents=("port", "    ethernet 1/8")),
    ConfigLine(config_line="        egress-mtu 9008", parents=("port", "    ethernet 1/8")),
    ConfigLine(config_line='        l2cp profile "EXAMPLE-THREE"', parents=("port", "    ethernet 1/8")),
    ConfigLine(config_line="        lldp", parents=("port", "    ethernet 1/8")),
    ConfigLine(
        config_line="            nearest-bridge-mode tx-rx", parents=("port", "    ethernet 1/8", "        lldp")
    ),
    ConfigLine(
        config_line="            nearest-bridge-basic-management port-description sys-name sys-description sys-capabilities management-address",
        parents=("port", "    ethernet 1/8", "        lldp"),
    ),
    ConfigLine(
        config_line="            nearest-bridge-802.3 max-frame-size",
        parents=("port", "    ethernet 1/8", "        lldp"),
    ),
    ConfigLine(config_line="    ethernet 1/10", parents=("port",)),
    ConfigLine(config_line='        name "description for eth1/9"', parents=("port", "    ethernet 1/10")),
    ConfigLine(config_line="        egress-mtu 12000", parents=("port", "    ethernet 1/10")),
    ConfigLine(config_line='        l2cp profile "EXAMPLE-ONE"', parents=("port", "    ethernet 1/10")),
    ConfigLine(config_line="    ethernet 3/1", parents=("port",)),
    ConfigLine(config_line="        shutdown", parents=("port", "    ethernet 3/1")),
    ConfigLine(config_line="    ethernet 3/2", parents=("port",)),
    ConfigLine(config_line='        name "description for eth3/2"', parents=("port", "    ethernet 3/2")),
    ConfigLine(config_line="        egress-mtu 12000", parents=("port", "    ethernet 3/2")),
    ConfigLine(config_line='        l2cp profile "EXAMPLE-ONE"', parents=("port", "    ethernet 3/2")),
    ConfigLine(config_line="    ethernet 4/1", parents=("port",)),
    ConfigLine(config_line='        name "description for eth4/1"', parents=("port", "    ethernet 4/1")),
    ConfigLine(config_line="        egress-mtu 12000", parents=("port", "    ethernet 4/1")),
    ConfigLine(config_line='        l2cp profile "network"', parents=("port", "    ethernet 4/1")),
    ConfigLine(config_line="        lldp", parents=("port", "    ethernet 4/1")),
    ConfigLine(
        config_line="            nearest-bridge-mode tx-rx", parents=("port", "    ethernet 4/1", "        lldp")
    ),
    ConfigLine(
        config_line="            nearest-bridge-basic-management port-description sys-name sys-description sys-capabilities management-address",
        parents=("port", "    ethernet 4/1", "        lldp"),
    ),
    ConfigLine(
        config_line="            nearest-bridge-802.3 max-frame-size",
        parents=("port", "    ethernet 4/1", "        lldp"),
    ),
    ConfigLine(config_line="    ethernet 4/2", parents=("port",)),
    ConfigLine(config_line='        name "description for eth4/2"', parents=("port", "    ethernet 4/2")),
    ConfigLine(config_line='    echo "Service Virtual Interface- Port Configuration"', parents=("port",)),
    ConfigLine(config_line="    svi 1", parents=("port",)),
    ConfigLine(config_line='        name "1"', parents=("port", "    svi 1")),
    ConfigLine(config_line="        no shutdown", parents=("port", "    svi 1")),
    ConfigLine(config_line="    svi 3", parents=("port",)),
    ConfigLine(config_line='        name "3"', parents=("port", "    svi 3")),
    ConfigLine(config_line='    echo "LAG - Port Configuration"', parents=("port",)),
    ConfigLine(config_line="    lag 1", parents=("port",)),
    ConfigLine(config_line="        shutdown", parents=("port", "    lag 1")),
    ConfigLine(config_line="        bind ethernet 1/1", parents=("port", "    lag 1")),
    ConfigLine(config_line="        bind ethernet 1/2", parents=("port", "    lag 1")),
    ConfigLine(config_line="        anchor-port ethernet 1/1", parents=("port", "    lag 1")),
    ConfigLine(config_line="    lag 7", parents=("port",)),
    ConfigLine(config_line="        shutdown", parents=("port", "    lag 7")),
    ConfigLine(config_line="        no anchor-port", parents=("port", "    lag 7")),
    ConfigLine(config_line='echo "Bridge Configuration"', parents=()),
    ConfigLine(config_line="bridge 1", parents=()),
    ConfigLine(config_line='    name "MGMT"', parents=("bridge 1",)),
    ConfigLine(config_line='    echo "Bridge Port Configuration"', parents=("bridge 1",)),
    ConfigLine(config_line="    port 1", parents=("bridge 1",)),
    ConfigLine(config_line='        name "svi 1"', parents=("bridge 1", "    port 1")),
    ConfigLine(config_line="        no shutdown", parents=("bridge 1", "    port 1")),
    ConfigLine(config_line="    port 2", parents=("bridge 1",)),
    ConfigLine(config_line='        name "example"', parents=("bridge 1", "    port 2")),
    ConfigLine(config_line="        no shutdown", parents=("bridge 1", "    port 2")),
    ConfigLine(config_line="    port 3", parents=("bridge 1",)),
    ConfigLine(config_line='        name "example"', parents=("bridge 1", "    port 3")),
    ConfigLine(config_line="        no shutdown", parents=("bridge 1", "    port 3")),
    ConfigLine(config_line="    port 4", parents=("bridge 1",)),
    ConfigLine(config_line='        name "example"', parents=("bridge 1", "    port 4")),
    ConfigLine(config_line="        no shutdown", parents=("bridge 1", "    port 4")),
    ConfigLine(config_line="    port 5", parents=("bridge 1",)),
    ConfigLine(config_line='        name "example"', parents=("bridge 1", "    port 5")),
    ConfigLine(config_line="        no shutdown", parents=("bridge 1", "    port 5")),
    ConfigLine(config_line='    echo "VLAN Configuration"', parents=("bridge 1",)),
    ConfigLine(config_line="    vlan 99", parents=("bridge 1",)),
    ConfigLine(config_line='echo "Flows Configuration"', parents=()),
    ConfigLine(config_line="flows", parents=()),
    ConfigLine(config_line="    rate-sampling-window 1", parents=("flows",)),
    ConfigLine(config_line='    echo "Classifier Profile Configuration"', parents=("flows",)),
    ConfigLine(config_line='    classifier-profile "mgmt" match-any', parents=("flows",)),
    ConfigLine(config_line="        match untagged", parents=("flows", '    classifier-profile "mgmt" match-any')),
    ConfigLine(config_line='    classifier-profile "CP-ONE" match-any', parents=("flows",)),
    ConfigLine(config_line="        match vlan 1103", parents=("flows", '    classifier-profile "CP-ONE" match-any')),
    ConfigLine(config_line='    classifier-profile "CP-TWO" match-any', parents=("flows",)),
    ConfigLine(config_line="        match vlan 1103", parents=("flows", '    classifier-profile "CP-TWO" match-any')),
    ConfigLine(config_line='    classifier-profile "CP-THREE" match-any', parents=("flows",)),
    ConfigLine(config_line="        match vlan 1201", parents=("flows", '    classifier-profile "CP-THREE" match-any')),
    ConfigLine(config_line='    classifier-profile "CP-FOUR" match-any', parents=("flows",)),
    ConfigLine(config_line="        match vlan 1201", parents=("flows", '    classifier-profile "CP-FOUR" match-any')),
    ConfigLine(config_line='    classifier-profile "CP-FIVE" match-any', parents=("flows",)),
    ConfigLine(config_line="        match vlan 1103", parents=("flows", '    classifier-profile "CP-FIVE" match-any')),
    ConfigLine(config_line='    classifier-profile "CP-SIX" match-any', parents=("flows",)),
    ConfigLine(config_line="        match vlan 1103", parents=("flows", '    classifier-profile "CP-SIX" match-any')),
    ConfigLine(config_line='    classifier-profile "CP-SEVEN" match-any', parents=("flows",)),
    ConfigLine(
        config_line="        match vlan 1155 dst-ip 192.168.192.2 to-dst-ip 192.168.192.2",
        parents=("flows", '    classifier-profile "CP-SEVEN" match-any'),
    ),
    ConfigLine(config_line='    classifier-profile "CP-EIGHT" match-any', parents=("flows",)),
    ConfigLine(config_line="        match all", parents=("flows", '    classifier-profile "CP-EIGHT" match-any')),
    ConfigLine(config_line='    classifier-profile "CP-NINE" match-any', parents=("flows",)),
    ConfigLine(config_line="        match all", parents=("flows", '    classifier-profile "CP-NINE" match-any')),
    ConfigLine(config_line='    classifier-profile "CP-TEN" match-any', parents=("flows",)),
    ConfigLine(config_line="        match vlan 1155", parents=("flows", '    classifier-profile "CP-TEN" match-any')),
    ConfigLine(config_line='    classifier-profile "CP-ELEVEN" match-any', parents=("flows",)),
    ConfigLine(
        config_line="        match vlan 1202", parents=("flows", '    classifier-profile "CP-ELEVEN" match-any')
    ),
    ConfigLine(config_line='    classifier-profile "CP-TWELVE" match-any', parents=("flows",)),
    ConfigLine(config_line="        match all", parents=("flows", '    classifier-profile "CP-TWELVE" match-any')),
    ConfigLine(config_line='    classifier-profile "CP-A" match-any', parents=("flows",)),
    ConfigLine(config_line="        match vlan 22", parents=("flows", '    classifier-profile "CP-A" match-any')),
    ConfigLine(config_line='    classifier-profile "CP-B" match-any', parents=("flows",)),
    ConfigLine(config_line="        match all", parents=("flows", '    classifier-profile "CP-B" match-any')),
    ConfigLine(config_line='    classifier-profile "CP-C" match-any', parents=("flows",)),
    ConfigLine(config_line="        match vlan 777", parents=("flows", '    classifier-profile "CP-C" match-any')),
    ConfigLine(config_line='    classifier-profile "CP-D" match-any', parents=("flows",)),
    ConfigLine(config_line="        match all", parents=("flows", '    classifier-profile "CP-D" match-any')),
    ConfigLine(config_line='    classifier-profile "CP-E" match-any', parents=("flows",)),
    ConfigLine(config_line="        match vlan 1102", parents=("flows", '    classifier-profile "CP-E" match-any')),
    ConfigLine(config_line='    classifier-profile "CP-F" match-any', parents=("flows",)),
    ConfigLine(config_line="        match vlan 88", parents=("flows", '    classifier-profile "CP-F" match-any')),
    ConfigLine(config_line='    classifier-profile "CP-G" match-any', parents=("flows",)),
    ConfigLine(config_line="        match vlan 88", parents=("flows", '    classifier-profile "CP-G" match-any')),
    ConfigLine(config_line='    echo "Flow Configuration"', parents=("flows",)),
    ConfigLine(config_line='    flow "flow1"', parents=("flows",)),
    ConfigLine(config_line='        classifier "mgmt"', parents=("flows", '    flow "flow1"')),
    ConfigLine(config_line='        policer profile "mgmt_policer"', parents=("flows", '    flow "flow1"')),
    ConfigLine(config_line="        vlan-tag push vlan 99 p-bit fixed 7", parents=("flows", '    flow "flow1"')),
    ConfigLine(config_line="        ingress-port svi 1", parents=("flows", '    flow "flow1"')),
    ConfigLine(config_line="        egress-port bridge-port 1 1", parents=("flows", '    flow "flow1"')),
    ConfigLine(config_line="        reverse-direction", parents=("flows", '    flow "flow1"')),
    ConfigLine(config_line="        no shutdown", parents=("flows", '    flow "flow1"')),
    ConfigLine(config_line='    flow "flow2"', parents=("flows",)),
    ConfigLine(config_line='        classifier "CP-THREE"', parents=("flows", '    flow "flow2"')),
    ConfigLine(config_line='        policer profile "50m"', parents=("flows", '    flow "flow2"')),
    ConfigLine(config_line="        mark all", parents=("flows", '    flow "flow2"')),
    ConfigLine(config_line="            vlan 1201", parents=("flows", '    flow "flow2"', "        mark all")),
    ConfigLine(config_line="            p-bit 1", parents=("flows", '    flow "flow2"', "        mark all")),
    ConfigLine(config_line="        ingress-port ethernet 3/1", parents=("flows", '    flow "flow2"')),
    ConfigLine(config_line="        egress-port ethernet 4/1 queue 1 block 0/1", parents=("flows", '    flow "flow2"')),
    ConfigLine(config_line='        service-name "R"', parents=("flows", '    flow "flow2"')),
    ConfigLine(config_line="        no shutdown", parents=("flows", '    flow "flow2"')),
    ConfigLine(config_line='    flow "flow3"', parents=("flows",)),
    ConfigLine(config_line='        classifier "mgmt"', parents=("flows", '    flow "flow3"')),
    ConfigLine(config_line='        policer profile "mgmt_policer"', parents=("flows", '    flow "flow3"')),
    ConfigLine(config_line="        vlan-tag push vlan 99 p-bit fixed 7", parents=("flows", '    flow "flow3"')),
    ConfigLine(config_line="        ingress-port ethernet 4/1", parents=("flows", '    flow "flow3"')),
    ConfigLine(config_line="        egress-port bridge-port 1 2", parents=("flows", '    flow "flow3"')),
    ConfigLine(config_line="        reverse-direction block 0/1", parents=("flows", '    flow "flow3"')),
    ConfigLine(config_line="        no shutdown", parents=("flows", '    flow "flow3"')),
    ConfigLine(config_line='    flow "flow4"', parents=("flows",)),
    ConfigLine(config_line='        classifier "mgmt"', parents=("flows", '    flow "flow4"')),
    ConfigLine(config_line='        policer profile "mgmt_policer"', parents=("flows", '    flow "flow4"')),
    ConfigLine(config_line="        vlan-tag push vlan 99 p-bit fixed 7", parents=("flows", '    flow "flow4"')),
    ConfigLine(config_line="        ingress-port ethernet 1/1", parents=("flows", '    flow "flow4"')),
    ConfigLine(config_line="        egress-port bridge-port 1 4", parents=("flows", '    flow "flow4"')),
    ConfigLine(config_line="        reverse-direction block 0/1", parents=("flows", '    flow "flow4"')),
    ConfigLine(config_line="        no shutdown", parents=("flows", '    flow "flow4"')),
    ConfigLine(config_line='    flow "flow5"', parents=("flows",)),
    ConfigLine(config_line='        classifier "CP-ONE"', parents=("flows", '    flow "flow5"')),
    ConfigLine(config_line="        no policer", parents=("flows", '    flow "flow5"')),
    ConfigLine(config_line="        ingress-port ethernet 1/3", parents=("flows", '    flow "flow5"')),
    ConfigLine(
        config_line='        egress-port ethernet 4/1 queue-map-profile "MTU" block 0/1',
        parents=("flows", '    flow "flow5"'),
    ),
    ConfigLine(config_line='        service-name "Q"', parents=("flows", '    flow "flow5"')),
    ConfigLine(config_line="        no shutdown", parents=("flows", '    flow "flow5"')),
    ConfigLine(config_line='    flow "flow6"', parents=("flows",)),
    ConfigLine(config_line='        classifier "CP-TWO"', parents=("flows", '    flow "flow6"')),
    ConfigLine(config_line="        no policer", parents=("flows", '    flow "flow6"')),
    ConfigLine(config_line="        ingress-port ethernet 4/1", parents=("flows", '    flow "flow6"')),
    ConfigLine(
        config_line='        egress-port ethernet 1/3 queue-map-profile "MTU" block 0/1',
        parents=("flows", '    flow "flow6"'),
    ),
    ConfigLine(config_line='        service-name "P"', parents=("flows", '    flow "flow6"')),
    ConfigLine(config_line="        no shutdown", parents=("flows", '    flow "flow6"')),
    ConfigLine(config_line='    flow "flow7"', parents=("flows",)),
    ConfigLine(config_line='        classifier "CP-FOUR"', parents=("flows", '    flow "flow7"')),
    ConfigLine(config_line="        no policer", parents=("flows", '    flow "flow7"')),
    ConfigLine(config_line="        mark all", parents=("flows", '    flow "flow7"')),
    ConfigLine(config_line="            vlan 1201", parents=("flows", '    flow "flow7"', "        mark all")),
    ConfigLine(config_line="        ingress-port ethernet 4/1", parents=("flows", '    flow "flow7"')),
    ConfigLine(config_line="        egress-port ethernet 3/1 queue 1 block 0/1", parents=("flows", '    flow "flow7"')),
    ConfigLine(config_line='        service-name "O"', parents=("flows", '    flow "flow7"')),
    ConfigLine(config_line="        no shutdown", parents=("flows", '    flow "flow7"')),
    ConfigLine(config_line='    flow "flow8"', parents=("flows",)),
    ConfigLine(config_line='        classifier "mgmt"', parents=("flows", '    flow "flow8"')),
    ConfigLine(config_line='        policer profile "mgmt_policer"', parents=("flows", '    flow "flow8"')),
    ConfigLine(config_line="        vlan-tag push vlan 99 p-bit fixed 7", parents=("flows", '    flow "flow8"')),
    ConfigLine(config_line="        ingress-port ethernet 1/8", parents=("flows", '    flow "flow8"')),
    ConfigLine(config_line="        egress-port bridge-port 1 5", parents=("flows", '    flow "flow8"')),
    ConfigLine(config_line="        reverse-direction block 0/1", parents=("flows", '    flow "flow8"')),
    ConfigLine(config_line="        no shutdown", parents=("flows", '    flow "flow8"')),
    ConfigLine(config_line='    flow "flow9"', parents=("flows",)),
    ConfigLine(config_line="        shutdown", parents=("flows", '    flow "flow9"')),
    ConfigLine(config_line='        classifier "mgmt"', parents=("flows", '    flow "flow9"')),
    ConfigLine(config_line='        policer profile "Policer1"', parents=("flows", '    flow "flow9"')),
    ConfigLine(config_line="        vlan-tag push vlan 1111 p-bit fixed 4", parents=("flows", '    flow "flow9"')),
    ConfigLine(config_line="        ingress-port ethernet 3/1", parents=("flows", '    flow "flow9"')),
    ConfigLine(config_line="        egress-port ethernet 4/2 queue 1 block 0/1", parents=("flows", '    flow "flow9"')),
    ConfigLine(config_line='        service-name "N"', parents=("flows", '    flow "flow9"')),
    ConfigLine(config_line="        pm-collection interval 300", parents=("flows", '    flow "flow9"')),
    ConfigLine(config_line='    flow "flow10"', parents=("flows",)),
    ConfigLine(config_line='        classifier "CP-EIGHT"', parents=("flows", '    flow "flow10"')),
    ConfigLine(config_line='        policer profile "10m"', parents=("flows", '    flow "flow10"')),
    ConfigLine(config_line="        vlan-tag push vlan 1202 p-bit fixed 3", parents=("flows", '    flow "flow10"')),
    ConfigLine(config_line="        ingress-port ethernet 3/2", parents=("flows", '    flow "flow10"')),
    ConfigLine(
        config_line="        egress-port ethernet 4/1 queue 1 block 0/1", parents=("flows", '    flow "flow10"')
    ),
    ConfigLine(config_line='        service-name "M"', parents=("flows", '    flow "flow10"')),
    ConfigLine(config_line="        no shutdown", parents=("flows", '    flow "flow10"')),
    ConfigLine(config_line='    flow "flow11"', parents=("flows",)),
    ConfigLine(config_line='        classifier "CP-ELEVEN"', parents=("flows", '    flow "flow11"')),
    ConfigLine(config_line="        no policer", parents=("flows", '    flow "flow11"')),
    ConfigLine(config_line="        vlan-tag pop vlan", parents=("flows", '    flow "flow11"')),
    ConfigLine(config_line="        ingress-port ethernet 4/1", parents=("flows", '    flow "flow11"')),
    ConfigLine(
        config_line="        egress-port ethernet 3/2 queue 1 block 0/1", parents=("flows", '    flow "flow11"')
    ),
    ConfigLine(config_line='        service-name "L"', parents=("flows", '    flow "flow11"')),
    ConfigLine(config_line="        no shutdown", parents=("flows", '    flow "flow11"')),
    ConfigLine(config_line='    flow "flow12"', parents=("flows",)),
    ConfigLine(config_line="        shutdown", parents=("flows", '    flow "flow12"')),
    ConfigLine(config_line='        classifier "CP-FIVE"', parents=("flows", '    flow "flow12"')),
    ConfigLine(config_line="        no policer", parents=("flows", '    flow "flow12"')),
    ConfigLine(config_line="        ingress-port ethernet 1/3", parents=("flows", '    flow "flow12"')),
    ConfigLine(
        config_line='        egress-port ethernet 4/1 queue-map-profile "MTU" block 0/1',
        parents=("flows", '    flow "flow12"'),
    ),
    ConfigLine(config_line='        service-name "K"', parents=("flows", '    flow "flow12"')),
    ConfigLine(config_line='    flow "flow13"', parents=("flows",)),
    ConfigLine(config_line='        classifier "CP-SEVEN"', parents=("flows", '    flow "flow13"')),
    ConfigLine(config_line='        policer profile "2g"', parents=("flows", '    flow "flow13"')),
    ConfigLine(config_line="        mark all", parents=("flows", '    flow "flow13"')),
    ConfigLine(config_line="            mac swap", parents=("flows", '    flow "flow13"', "        mark all")),
    ConfigLine(config_line="            ip swap", parents=("flows", '    flow "flow13"', "        mark all")),
    ConfigLine(config_line="        ingress-port ethernet 4/1", parents=("flows", '    flow "flow13"')),
    ConfigLine(
        config_line="        egress-port ethernet 4/1 queue 0 block 0/1", parents=("flows", '    flow "flow13"')
    ),
    ConfigLine(config_line="        no shutdown", parents=("flows", '    flow "flow13"')),
    ConfigLine(config_line='    flow "flow14"', parents=("flows",)),
    ConfigLine(config_line="        shutdown", parents=("flows", '    flow "flow14"')),
    ConfigLine(config_line='        classifier "CP-SIX"', parents=("flows", '    flow "flow14"')),
    ConfigLine(config_line="        no policer", parents=("flows", '    flow "flow14"')),
    ConfigLine(config_line="        ingress-port ethernet 4/1", parents=("flows", '    flow "flow14"')),
    ConfigLine(
        config_line='        egress-port ethernet 1/3 queue-map-profile "MTU" block 0/1',
        parents=("flows", '    flow "flow14"'),
    ),
    ConfigLine(config_line='        service-name "J"', parents=("flows", '    flow "flow14"')),
    ConfigLine(config_line='    flow "flow15"', parents=("flows",)),
    ConfigLine(config_line='        classifier "CP-NINE"', parents=("flows", '    flow "flow15"')),
    ConfigLine(config_line='        policer profile "2g"', parents=("flows", '    flow "flow15"')),
    ConfigLine(config_line="        vlan-tag push vlan 1155 p-bit fixed 1", parents=("flows", '    flow "flow15"')),
    ConfigLine(config_line="        ingress-port ethernet 1/5", parents=("flows", '    flow "flow15"')),
    ConfigLine(
        config_line="        egress-port ethernet 4/1 queue 1 block 0/1", parents=("flows", '    flow "flow15"')
    ),
    ConfigLine(config_line='        service-name "I"', parents=("flows", '    flow "flow15"')),
    ConfigLine(config_line="        no shutdown", parents=("flows", '    flow "flow15"')),
    ConfigLine(config_line='    flow "flow16"', parents=("flows",)),
    ConfigLine(config_line='        classifier "CP-TEN"', parents=("flows", '    flow "flow16"')),
    ConfigLine(config_line="        no policer", parents=("flows", '    flow "flow16"')),
    ConfigLine(config_line="        vlan-tag pop vlan", parents=("flows", '    flow "flow16"')),
    ConfigLine(config_line="        ingress-port ethernet 4/1", parents=("flows", '    flow "flow16"')),
    ConfigLine(
        config_line="        egress-port ethernet 1/5 queue 1 block 0/1", parents=("flows", '    flow "flow16"')
    ),
    ConfigLine(config_line='        service-name "H"', parents=("flows", '    flow "flow16"')),
    ConfigLine(config_line="        no shutdown", parents=("flows", '    flow "flow16"')),
    ConfigLine(config_line='    flow "flow17"', parents=("flows",)),
    ConfigLine(config_line='        classifier "CP-D"', parents=("flows", '    flow "flow17"')),
    ConfigLine(config_line='        policer profile "100m"', parents=("flows", '    flow "flow17"')),
    ConfigLine(config_line="        vlan-tag push vlan 1102 p-bit fixed 1", parents=("flows", '    flow "flow17"')),
    ConfigLine(config_line="        ingress-port ethernet 1/7", parents=("flows", '    flow "flow17"')),
    ConfigLine(
        config_line="        egress-port ethernet 4/1 queue 1 block 0/1", parents=("flows", '    flow "flow17"')
    ),
    ConfigLine(config_line='        service-name "G"', parents=("flows", '    flow "flow17"')),
    ConfigLine(config_line="        no shutdown", parents=("flows", '    flow "flow17"')),
    ConfigLine(config_line='    flow "flow18"', parents=("flows",)),
    ConfigLine(config_line='        classifier "CP-TWELVE"', parents=("flows", '    flow "flow18"')),
    ConfigLine(config_line='        policer profile "50m"', parents=("flows", '    flow "flow18"')),
    ConfigLine(config_line="        vlan-tag push vlan 22 p-bit fixed 3", parents=("flows", '    flow "flow18"')),
    ConfigLine(config_line="        ingress-port ethernet 1/8", parents=("flows", '    flow "flow18"')),
    ConfigLine(
        config_line="        egress-port ethernet 4/1 queue 1 block 0/1", parents=("flows", '    flow "flow18"')
    ),
    ConfigLine(config_line='        service-name "F"', parents=("flows", '    flow "flow18"')),
    ConfigLine(config_line="        no shutdown", parents=("flows", '    flow "flow18"')),
    ConfigLine(config_line='    flow "flow19"', parents=("flows",)),
    ConfigLine(config_line='        classifier "CP-A"', parents=("flows", '    flow "flow19"')),
    ConfigLine(config_line="        no policer", parents=("flows", '    flow "flow19"')),
    ConfigLine(config_line="        vlan-tag pop vlan", parents=("flows", '    flow "flow19"')),
    ConfigLine(config_line="        ingress-port ethernet 4/1", parents=("flows", '    flow "flow19"')),
    ConfigLine(
        config_line="        egress-port ethernet 1/8 queue 1 block 0/1", parents=("flows", '    flow "flow19"')
    ),
    ConfigLine(config_line='        service-name "E"', parents=("flows", '    flow "flow19"')),
    ConfigLine(config_line="        no shutdown", parents=("flows", '    flow "flow19"')),
    ConfigLine(config_line='    flow "flow20"', parents=("flows",)),
    ConfigLine(config_line='        classifier "CP-E"', parents=("flows", '    flow "flow20"')),
    ConfigLine(config_line="        no policer", parents=("flows", '    flow "flow20"')),
    ConfigLine(config_line="        vlan-tag pop vlan", parents=("flows", '    flow "flow20"')),
    ConfigLine(config_line="        ingress-port ethernet 4/1", parents=("flows", '    flow "flow20"')),
    ConfigLine(
        config_line="        egress-port ethernet 1/7 queue 1 block 0/1", parents=("flows", '    flow "flow20"')
    ),
    ConfigLine(config_line='        service-name "D"', parents=("flows", '    flow "flow20"')),
    ConfigLine(config_line="        no shutdown", parents=("flows", '    flow "flow20"')),
    ConfigLine(config_line='    flow "flow21"', parents=("flows",)),
    ConfigLine(config_line='        classifier "CP-B"', parents=("flows", '    flow "flow21"')),
    ConfigLine(config_line='        policer profile "100_Mbps"', parents=("flows", '    flow "flow21"')),
    ConfigLine(config_line="        vlan-tag push vlan 777 p-bit fixed 3", parents=("flows", '    flow "flow21"')),
    ConfigLine(config_line="        ingress-port ethernet 1/10", parents=("flows", '    flow "flow21"')),
    ConfigLine(
        config_line="        egress-port ethernet 4/1 queue 1 block 0/1", parents=("flows", '    flow "flow21"')
    ),
    ConfigLine(config_line='        service-name "C"', parents=("flows", '    flow "flow21"')),
    ConfigLine(config_line="        no shutdown", parents=("flows", '    flow "flow21"')),
    ConfigLine(config_line='    flow "flow22"', parents=("flows",)),
    ConfigLine(config_line='        classifier "CP-C"', parents=("flows", '    flow "flow22"')),
    ConfigLine(config_line="        no policer", parents=("flows", '    flow "flow22"')),
    ConfigLine(config_line="        vlan-tag pop vlan", parents=("flows", '    flow "flow22"')),
    ConfigLine(config_line="        ingress-port ethernet 4/1", parents=("flows", '    flow "flow22"')),
    ConfigLine(
        config_line="        egress-port ethernet 1/10 queue 1 block 0/1", parents=("flows", '    flow "flow22"')
    ),
    ConfigLine(config_line='        service-name "B"', parents=("flows", '    flow "flow22"')),
    ConfigLine(config_line="        no shutdown", parents=("flows", '    flow "flow22"')),
    ConfigLine(config_line='    flow "flow23"', parents=("flows",)),
    ConfigLine(config_line='        classifier "CP-F"', parents=("flows", '    flow "flow23"')),
    ConfigLine(config_line="        no policer", parents=("flows", '    flow "flow23"')),
    ConfigLine(config_line="        ingress-port ethernet 1/3", parents=("flows", '    flow "flow23"')),
    ConfigLine(
        config_line="        egress-port ethernet 4/1 queue 1 block 0/1", parents=("flows", '    flow "flow23"')
    ),
    ConfigLine(config_line='        service-name "A"', parents=("flows", '    flow "flow23"')),
    ConfigLine(config_line="        no shutdown", parents=("flows", '    flow "flow23"')),
    ConfigLine(config_line='    flow "flow24"', parents=("flows",)),
    ConfigLine(config_line='        classifier "CP-G"', parents=("flows", '    flow "flow24"')),
    ConfigLine(config_line="        no policer", parents=("flows", '    flow "flow24"')),
    ConfigLine(config_line="        ingress-port ethernet 4/1", parents=("flows", '    flow "flow24"')),
    ConfigLine(
        config_line="        egress-port ethernet 1/3 queue 1 block 0/1", parents=("flows", '    flow "flow24"')
    ),
    ConfigLine(config_line='        service-name "A"', parents=("flows", '    flow "flow24"')),
    ConfigLine(config_line="        no shutdown", parents=("flows", '    flow "flow24"')),
    ConfigLine(config_line="router 1", parents=()),
    ConfigLine(config_line='    name "Router#1"', parents=("router 1",)),
    ConfigLine(config_line="    interface 1", parents=("router 1",)),
    ConfigLine(config_line='        name "ROUTER:DESCRIPTION"', parents=("router 1", "    interface 1")),
    ConfigLine(config_line="        bind svi 1", parents=("router 1", "    interface 1")),
    ConfigLine(config_line="        dhcp", parents=("router 1", "    interface 1")),
    ConfigLine(config_line="        dhcp-client", parents=("router 1", "    interface 1")),
    ConfigLine(config_line="            client-id mac", parents=("router 1", "    interface 1", "        dhcp-client")),
    ConfigLine(config_line="        no shutdown", parents=("router 1", "    interface 1")),
    ConfigLine(config_line="    static-route 0.0.0.0/0 address 1.1.1.1 metric 1", parents=("router 1",)),
    ConfigLine(config_line="oam", parents=()),
    ConfigLine(config_line='    echo "OAM CFM Configuration"', parents=("oam",)),
    ConfigLine(config_line="    cfm", parents=("oam",)),
    ConfigLine(config_line="        md-level-mip 2", parents=("oam", "    cfm")),
    ConfigLine(config_line='        measurement-bin-profile "cfm1"', parents=("oam", "    cfm")),
    ConfigLine(
        config_line="            thresholds 8000,10000,11200,14000",
        parents=("oam", "    cfm", '        measurement-bin-profile "cfm1"'),
    ),
    ConfigLine(config_line='        measurement-bin-profile "cfm2"', parents=("oam", "    cfm")),
    ConfigLine(
        config_line="            thresholds 1600,2000,2400,3000",
        parents=("oam", "    cfm", '        measurement-bin-profile "cfm2"'),
    ),
    ConfigLine(config_line='        measurement-bin-profile "cfm3"', parents=("oam", "    cfm")),
    ConfigLine(
        config_line="            thresholds 20000,25000,28000,35000",
        parents=("oam", "    cfm", '        measurement-bin-profile "cfm3"'),
    ),
    ConfigLine(config_line='        measurement-bin-profile "cfm4"', parents=("oam", "    cfm")),
    ConfigLine(
        config_line="            thresholds 3200,4000,6400,8000",
        parents=("oam", "    cfm", '        measurement-bin-profile "cfm4"'),
    ),
    ConfigLine(config_line='        measurement-bin-profile "cfm5"', parents=("oam", "    cfm")),
    ConfigLine(
        config_line="            thresholds 61600,77000,110400,138000",
        parents=("oam", "    cfm", '        measurement-bin-profile "cfm5"'),
    ),
    ConfigLine(config_line='        measurement-bin-profile "cfm5"', parents=("oam", "    cfm")),
    ConfigLine(
        config_line="            thresholds 8000,10000",
        parents=("oam", "    cfm", '        measurement-bin-profile "cfm5"'),
    ),
    ConfigLine(config_line='        measurement-bin-profile "cfm6"', parents=("oam", "    cfm")),
    ConfigLine(
        config_line="            thresholds 16000,20000,32000,40000",
        parents=("oam", "    cfm", '        measurement-bin-profile "cfm6"'),
    ),
    ConfigLine(config_line='        measurement-bin-profile "cfm7"', parents=("oam", "    cfm")),
    ConfigLine(
        config_line="            thresholds 6400,8000",
        parents=("oam", "    cfm", '        measurement-bin-profile "cfm7"'),
    ),
    ConfigLine(config_line='        measurement-bin-profile "cfm8"', parents=("oam", "    cfm")),
    ConfigLine(
        config_line="            thresholds 60000,75000,120000,150000",
        parents=("oam", "    cfm", '        measurement-bin-profile "cfm8"'),
    ),
    ConfigLine(config_line='        measurement-bin-profile "cfm9"', parents=("oam", "    cfm")),
    ConfigLine(
        config_line="            thresholds 32000,40000",
        parents=("oam", "    cfm", '        measurement-bin-profile "cfm9"'),
    ),
    ConfigLine(config_line='        measurement-bin-profile "cfma"', parents=("oam", "    cfm")),
    ConfigLine(
        config_line="            thresholds 92000,115000,184000,230000",
        parents=("oam", "    cfm", '        measurement-bin-profile "cfma"'),
    ),
    ConfigLine(config_line='        measurement-bin-profile "cfmb"', parents=("oam", "    cfm")),
    ConfigLine(
        config_line="            thresholds 32000,40000",
        parents=("oam", "    cfm", '        measurement-bin-profile "cfmb"'),
    ),
    ConfigLine(config_line='        measurement-bin-profile "cfmc"', parents=("oam", "    cfm")),
    ConfigLine(
        config_line="            thresholds 29600,37000,59200,74000",
        parents=("oam", "    cfm", '        measurement-bin-profile "cfmc"'),
    ),
    ConfigLine(config_line='        measurement-bin-profile "cfmd"', parents=("oam", "    cfm")),
    ConfigLine(
        config_line="            thresholds 100000,110400,125000,138000",
        parents=("oam", "    cfm", '        measurement-bin-profile "cfmd"'),
    ),
    ConfigLine(config_line='        measurement-bin-profile "cfme"', parents=("oam", "    cfm")),
    ConfigLine(
        config_line="            thresholds 184000,230000,368000,460000",
        parents=("oam", "    cfm", '        measurement-bin-profile "cfme"'),
    ),
    ConfigLine(config_line='        measurement-bin-profile "cfmf"', parents=("oam", "    cfm")),
    ConfigLine(
        config_line="            thresholds 8000,10000,40000,50000",
        parents=("oam", "    cfm", '        measurement-bin-profile "cfmf"'),
    ),
    ConfigLine(config_line='        measurement-bin-profile "cfmg"', parents=("oam", "    cfm")),
    ConfigLine(
        config_line="            thresholds 9600,12000",
        parents=("oam", "    cfm", '        measurement-bin-profile "cfmg"'),
    ),
    ConfigLine(config_line='        measurement-bin-profile "cfmh"', parents=("oam", "    cfm")),
    ConfigLine(
        config_line="            thresholds 40000,50000",
        parents=("oam", "    cfm", '        measurement-bin-profile "cfmh"'),
    ),
    ConfigLine(config_line='        measurement-bin-profile "cfmi"', parents=("oam", "    cfm")),
    ConfigLine(
        config_line="            thresholds 59200,74000",
        parents=("oam", "    cfm", '        measurement-bin-profile "cfmi"'),
    ),
    ConfigLine(config_line='        measurement-bin-profile "cfmj"', parents=("oam", "    cfm")),
    ConfigLine(
        config_line="            thresholds 9600,12000",
        parents=("oam", "    cfm", '        measurement-bin-profile "cfmj"'),
    ),
    ConfigLine(config_line='        measurement-bin-profile "cfmk"', parents=("oam", "    cfm")),
    ConfigLine(
        config_line="            thresholds 200000,250000",
        parents=("oam", "    cfm", '        measurement-bin-profile "cfmk"'),
    ),
    ConfigLine(config_line='        measurement-bin-profile "cfml"', parents=("oam", "    cfm")),
    ConfigLine(
        config_line="            thresholds 40000,50000",
        parents=("oam", "    cfm", '        measurement-bin-profile "cfml"'),
    ),
    ConfigLine(config_line='        measurement-bin-profile "cfmm"', parents=("oam", "    cfm")),
    ConfigLine(
        config_line="            thresholds 368000,460000",
        parents=("oam", "    cfm", '        measurement-bin-profile "cfmm"'),
    ),
    ConfigLine(config_line='        measurement-bin-profile "cfmn"', parents=("oam", "    cfm")),
    ConfigLine(
        config_line="            thresholds 40000,50000",
        parents=("oam", "    cfm", '        measurement-bin-profile "cfmn"'),
    ),
    ConfigLine(config_line="        maintenance-domain 1", parents=("oam", "    cfm")),
    ConfigLine(config_line='            name string "MD1"', parents=("oam", "    cfm", "        maintenance-domain 1")),
    ConfigLine(
        config_line="            maintenance-association 1", parents=("oam", "    cfm", "        maintenance-domain 1")
    ),
    ConfigLine(
        config_line='                name string "MA1"',
        parents=("oam", "    cfm", "        maintenance-domain 1", "            maintenance-association 1"),
    ),
    ConfigLine(
        config_line="                mep 1",
        parents=("oam", "    cfm", "        maintenance-domain 1", "            maintenance-association 1"),
    ),
    ConfigLine(
        config_line="                    no bind",
        parents=(
            "oam",
            "    cfm",
            "        maintenance-domain 1",
            "            maintenance-association 1",
            "                mep 1",
        ),
    ),
    ConfigLine(
        config_line="                    client-md-level 4",
        parents=(
            "oam",
            "    cfm",
            "        maintenance-domain 1",
            "            maintenance-association 1",
            "                mep 1",
        ),
    ),
    ConfigLine(config_line="        maintenance-domain 2", parents=("oam", "    cfm")),
    ConfigLine(config_line="            md-level 2", parents=("oam", "    cfm", "        maintenance-domain 2")),
    ConfigLine(
        config_line='            name string "ABC-DEF"', parents=("oam", "    cfm", "        maintenance-domain 2")
    ),
    ConfigLine(
        config_line="            maintenance-association 2", parents=("oam", "    cfm", "        maintenance-domain 2")
    ),
    ConfigLine(
        config_line='                name string "MA2"',
        parents=("oam", "    cfm", "        maintenance-domain 2", "            maintenance-association 2"),
    ),
    ConfigLine(
        config_line="                mep 1",
        parents=("oam", "    cfm", "        maintenance-domain 2", "            maintenance-association 2"),
    ),
    ConfigLine(
        config_line="                    bind ethernet 1/8",
        parents=(
            "oam",
            "    cfm",
            "        maintenance-domain 2",
            "            maintenance-association 2",
            "                mep 1",
        ),
    ),
    ConfigLine(
        config_line='                    flow uni-direction rx "MA2-out"',
        parents=(
            "oam",
            "    cfm",
            "        maintenance-domain 2",
            "            maintenance-association 2",
            "                mep 1",
        ),
    ),
    ConfigLine(
        config_line='                    flow uni-direction tx "MA2-in"',
        parents=(
            "oam",
            "    cfm",
            "        maintenance-domain 2",
            "            maintenance-association 2",
            "                mep 1",
        ),
    ),
    ConfigLine(
        config_line="                    remote-mep 2",
        parents=(
            "oam",
            "    cfm",
            "        maintenance-domain 2",
            "            maintenance-association 2",
            "                mep 1",
        ),
    ),
    ConfigLine(
        config_line="                    direction up",
        parents=(
            "oam",
            "    cfm",
            "        maintenance-domain 2",
            "            maintenance-association 2",
            "                mep 1",
        ),
    ),
    ConfigLine(
        config_line="                    customer-tags-excluded",
        parents=(
            "oam",
            "    cfm",
            "        maintenance-domain 2",
            "            maintenance-association 2",
            "                mep 1",
        ),
    ),
    ConfigLine(
        config_line="                    client-md-level 3",
        parents=(
            "oam",
            "    cfm",
            "        maintenance-domain 2",
            "            maintenance-association 2",
            "                mep 1",
        ),
    ),
    ConfigLine(
        config_line="                    no shutdown",
        parents=(
            "oam",
            "    cfm",
            "        maintenance-domain 2",
            "            maintenance-association 2",
            "                mep 1",
        ),
    ),
    ConfigLine(
        config_line="                    service 1",
        parents=(
            "oam",
            "    cfm",
            "        maintenance-domain 2",
            "            maintenance-association 2",
            "                mep 1",
        ),
    ),
    ConfigLine(
        config_line="                        classification priority-bit 3",
        parents=(
            "oam",
            "    cfm",
            "        maintenance-domain 2",
            "            maintenance-association 2",
            "                mep 1",
            "                    service 1",
        ),
    ),
    ConfigLine(
        config_line="                        lmm-interval 100ms",
        parents=(
            "oam",
            "    cfm",
            "        maintenance-domain 2",
            "            maintenance-association 2",
            "                mep 1",
            "                    service 1",
        ),
    ),
    ConfigLine(
        config_line="                        dest-ne 1",
        parents=(
            "oam",
            "    cfm",
            "        maintenance-domain 2",
            "            maintenance-association 2",
            "                mep 1",
            "                    service 1",
        ),
    ),
    ConfigLine(
        config_line="                            no delay",
        parents=(
            "oam",
            "    cfm",
            "        maintenance-domain 2",
            "            maintenance-association 2",
            "                mep 1",
            "                    service 1",
            "                        dest-ne 1",
        ),
    ),
    ConfigLine(
        config_line="                            no loss",
        parents=(
            "oam",
            "    cfm",
            "        maintenance-domain 2",
            "            maintenance-association 2",
            "                mep 1",
            "                    service 1",
            "                        dest-ne 1",
        ),
    ),
    ConfigLine(
        config_line="                            remote mep-id 2",
        parents=(
            "oam",
            "    cfm",
            "        maintenance-domain 2",
            "            maintenance-association 2",
            "                mep 1",
            "                    service 1",
            "                        dest-ne 1",
        ),
    ),
    ConfigLine(
        config_line="                        no shutdown",
        parents=(
            "oam",
            "    cfm",
            "        maintenance-domain 2",
            "            maintenance-association 2",
            "                mep 1",
            "                    service 1",
        ),
    ),
    ConfigLine(config_line="        maintenance-domain 3", parents=("oam", "    cfm")),
    ConfigLine(
        config_line='            name string "ABC-DEF"', parents=("oam", "    cfm", "        maintenance-domain 3")
    ),
    ConfigLine(
        config_line="            maintenance-association 2", parents=("oam", "    cfm", "        maintenance-domain 3")
    ),
    ConfigLine(
        config_line='                name string "MD3"',
        parents=("oam", "    cfm", "        maintenance-domain 3", "            maintenance-association 2"),
    ),
    ConfigLine(
        config_line="                mep 2",
        parents=("oam", "    cfm", "        maintenance-domain 3", "            maintenance-association 2"),
    ),
    ConfigLine(
        config_line="                    bind ethernet 1/10",
        parents=(
            "oam",
            "    cfm",
            "        maintenance-domain 3",
            "            maintenance-association 2",
            "                mep 2",
        ),
    ),
    ConfigLine(
        config_line='                    flow uni-direction rx "MD3-out"',
        parents=(
            "oam",
            "    cfm",
            "        maintenance-domain 3",
            "            maintenance-association 2",
            "                mep 2",
        ),
    ),
    ConfigLine(
        config_line='                    flow uni-direction tx "MD3-in"',
        parents=(
            "oam",
            "    cfm",
            "        maintenance-domain 3",
            "            maintenance-association 2",
            "                mep 2",
        ),
    ),
    ConfigLine(
        config_line="                    remote-mep 1",
        parents=(
            "oam",
            "    cfm",
            "        maintenance-domain 3",
            "            maintenance-association 2",
            "                mep 2",
        ),
    ),
    ConfigLine(
        config_line="                    ccm-priority 3",
        parents=(
            "oam",
            "    cfm",
            "        maintenance-domain 3",
            "            maintenance-association 2",
            "                mep 2",
        ),
    ),
    ConfigLine(
        config_line="                    direction up",
        parents=(
            "oam",
            "    cfm",
            "        maintenance-domain 3",
            "            maintenance-association 2",
            "                mep 2",
        ),
    ),
    ConfigLine(
        config_line="                    customer-tags-excluded",
        parents=(
            "oam",
            "    cfm",
            "        maintenance-domain 3",
            "            maintenance-association 2",
            "                mep 2",
        ),
    ),
    ConfigLine(
        config_line="                    client-md-level 4",
        parents=(
            "oam",
            "    cfm",
            "        maintenance-domain 3",
            "            maintenance-association 2",
            "                mep 2",
        ),
    ),
    ConfigLine(
        config_line="                    no shutdown",
        parents=(
            "oam",
            "    cfm",
            "        maintenance-domain 3",
            "            maintenance-association 2",
            "                mep 2",
        ),
    ),
    ConfigLine(
        config_line="                    service 1",
        parents=(
            "oam",
            "    cfm",
            "        maintenance-domain 3",
            "            maintenance-association 2",
            "                mep 2",
        ),
    ),
    ConfigLine(
        config_line="                        delay-threshold 26000",
        parents=(
            "oam",
            "    cfm",
            "        maintenance-domain 3",
            "            maintenance-association 2",
            "                mep 2",
            "                    service 1",
        ),
    ),
    ConfigLine(
        config_line="                        delay-var-threshold 8000",
        parents=(
            "oam",
            "    cfm",
            "        maintenance-domain 3",
            "            maintenance-association 2",
            "                mep 2",
            "                    service 1",
        ),
    ),
    ConfigLine(
        config_line="                        classification priority-bit 3",
        parents=(
            "oam",
            "    cfm",
            "        maintenance-domain 3",
            "            maintenance-association 2",
            "                mep 2",
            "                    service 1",
        ),
    ),
    ConfigLine(
        config_line="                        dest-ne 1",
        parents=(
            "oam",
            "    cfm",
            "        maintenance-domain 3",
            "            maintenance-association 2",
            "                mep 2",
            "                    service 1",
        ),
    ),
    ConfigLine(
        config_line="                            loss single-ended slm",
        parents=(
            "oam",
            "    cfm",
            "        maintenance-domain 3",
            "            maintenance-association 2",
            "                mep 2",
            "                    service 1",
            "                        dest-ne 1",
        ),
    ),
    ConfigLine(
        config_line="                            remote mep-id 1",
        parents=(
            "oam",
            "    cfm",
            "        maintenance-domain 3",
            "            maintenance-association 2",
            "                mep 2",
            "                    service 1",
            "                        dest-ne 1",
        ),
    ),
    ConfigLine(
        config_line='                            delay-measurement-bin profile "cfm1"',
        parents=(
            "oam",
            "    cfm",
            "        maintenance-domain 3",
            "            maintenance-association 2",
            "                mep 2",
            "                    service 1",
            "                        dest-ne 1",
        ),
    ),
    ConfigLine(
        config_line='                            delay-var-measurement-bin profile "cfm2"',
        parents=(
            "oam",
            "    cfm",
            "        maintenance-domain 3",
            "            maintenance-association 2",
            "                mep 2",
            "                    service 1",
            "                        dest-ne 1",
        ),
    ),
    ConfigLine(
        config_line="                        no shutdown",
        parents=(
            "oam",
            "    cfm",
            "        maintenance-domain 3",
            "            maintenance-association 2",
            "                mep 2",
            "                    service 1",
        ),
    ),
]
