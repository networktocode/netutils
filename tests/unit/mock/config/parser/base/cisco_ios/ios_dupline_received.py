from netutils.config.parser import ConfigLine

data = [
    ConfigLine(config_line="hostname dupline", parents=()),
    ConfigLine(config_line="logging source-interface Loopback0", parents=()),
    ConfigLine(config_line="logging host 10.10.10.10", parents=()),
    ConfigLine(config_line="logging host 10.20.10.10 transport udp port 58512", parents=()),
    ConfigLine(config_line="access-list 93 remark Admin ACL Golden Template Version", parents=()),
    ConfigLine(config_line="access-list 93 remark Another Remark", parents=()),
    ConfigLine(config_line="access-list 93 permit 10.0.0.0 0.255.255.255", parents=()),
    ConfigLine(config_line="access-list 93 permit 192.168.1.0 0.0.255.255", parents=()),
    ConfigLine(config_line="access-list 93 remark Admin ACL Golden Template Version", parents=()),
    ConfigLine(config_line="access-list 93 deny any log", parents=()),
]
