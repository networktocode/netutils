from netutils.config.parser import ConfigLine

data = [
    ConfigLine(config_line="rsyslog 10.1.1.5", parents=()),
    ConfigLine(config_line="hostname MRV-OS904-1", parents=()),
    ConfigLine(config_line="service advanced-vty", parents=()),
    ConfigLine(config_line="service password-encryption", parents=()),
    ConfigLine(config_line="line vty", parents=()),
    ConfigLine(config_line=" exec-timeout global 90", parents=("line vty",)),
    ConfigLine(config_line="port media-select copper 1-2", parents=()),
    ConfigLine(config_line="port description 1 TO-CUSTOMER", parents=()),
    ConfigLine(config_line="port description 2 TO-POP", parents=()),
    ConfigLine(config_line="port state disable 3-4", parents=()),
    ConfigLine(config_line="no port advertise speed 1000 duplex half 1", parents=()),
    ConfigLine(config_line="no port advertise speed 1000 duplex full 1", parents=()),
    ConfigLine(config_line="port speed 100 1-2", parents=()),
    ConfigLine(config_line="port duplex full 1-2", parents=()),
    ConfigLine(config_line="port flood-limiting rate 10m 1", parents=()),
    ConfigLine(config_line="port flood-limiting unknown-unicast 1", parents=()),
    ConfigLine(config_line="port flood-limiting multicast 1", parents=()),
    ConfigLine(config_line="port flood-limiting broadcast 1", parents=()),
    ConfigLine(config_line="port tag-outbound-mode hybrid 1-2 1737", parents=()),
    ConfigLine(config_line="interface vlan vif416", parents=()),
    ConfigLine(config_line=" name CONTROL-VL", parents=("interface vlan vif416",)),
    ConfigLine(config_line=" tag 416", parents=("interface vlan vif416",)),
    ConfigLine(config_line=" ip 10.1.1.91/24", parents=("interface vlan vif416",)),
    ConfigLine(config_line=" ports 2", parents=("interface vlan vif416",)),
    ConfigLine(config_line=" management ssh 10.0.0.0/8", parents=("interface vlan vif416",)),
    ConfigLine(config_line=" management telnet 10.0.0.0/8", parents=("interface vlan vif416",)),
    ConfigLine(config_line=" management tftp 10.0.0.0/8", parents=("interface vlan vif416",)),
    ConfigLine(config_line=" management snmp 10.0.0.0/8", parents=("interface vlan vif416",)),
    ConfigLine(config_line="interface vlan vif1738", parents=()),
    ConfigLine(config_line=" name SERVICE", parents=("interface vlan vif1738",)),
    ConfigLine(config_line=" tag 1738", parents=("interface vlan vif1738",)),
    ConfigLine(config_line=" ports 1-2", parents=("interface vlan vif1738",)),
    ConfigLine(config_line="ip route 10.0.0.0/8 10.1.1.1", parents=()),
    ConfigLine(config_line="ip route 19.23.8.25/32 10.1.1.1", parents=()),
    ConfigLine(config_line="ntp", parents=()),
    ConfigLine(config_line=" server 10.1.1.2", parents=("ntp",)),
    ConfigLine(config_line=" enable", parents=("ntp",)),
    ConfigLine(config_line="ingress-counters set1 port 1 tag all", parents=()),
    ConfigLine(config_line="password long-mode", parents=()),
    ConfigLine(config_line="radius-server host 10.1.1.2 key ASU4602O551PTV6", parents=()),
    ConfigLine(config_line="radius-server host 10.1.1.15 key ASU4602O551PTV6", parents=()),
    ConfigLine(config_line="aaa", parents=()),
    ConfigLine(config_line=" authentication login default local radius", parents=("aaa",)),
    ConfigLine(config_line="snmp", parents=()),
    ConfigLine(config_line=" location dc1", parents=("snmp",)),
    ConfigLine(config_line=" community 10 read-only 10.0.0.0/8 secret", parents=("snmp",)),
    ConfigLine(config_line=" authtrap", parents=("snmp",)),
    ConfigLine(config_line=" trapsess 10.1.1.2 2 secret", parents=("snmp",)),
    ConfigLine(config_line=" trapsess 10.1.1.15 2 secret", parents=("snmp",)),
    ConfigLine(config_line="fan temperature 30 27", parents=()),
    ConfigLine(config_line="lldp", parents=()),
    ConfigLine(config_line=" port 1 receive", parents=("lldp",)),
    ConfigLine(config_line=" port 2 receive", parents=("lldp",)),
    ConfigLine(config_line=" port 3 receive", parents=("lldp",)),
    ConfigLine(config_line=" port 4 receive", parents=("lldp",)),
    ConfigLine(config_line=" enable", parents=("lldp",)),
]