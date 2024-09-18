from netutils.config.parser import ConfigLine

data = [
    ConfigLine(config_line="set mgt-config users admin phash *", parents=()),
    ConfigLine(config_line="set mgt-config users admin permissions role-based superuser yes", parents=()),
    ConfigLine(
        config_line="set mgt-config users admin public-key thisisasuperduperlongbase64encodedstring=", parents=()
    ),
    ConfigLine(config_line="set mgt-config users panadmin permissions role-based superuser yes", parents=()),
    ConfigLine(config_line="set mgt-config users panadmin phash passwordhash", parents=()),
    ConfigLine(config_line="set shared botnet configuration http dynamic-dns enabled yes", parents=()),
    ConfigLine(config_line="set shared botnet configuration http dynamic-dns threshold 5", parents=()),
    ConfigLine(config_line="set shared botnet configuration http malware-sites enabled yes", parents=()),
    ConfigLine(config_line="set shared botnet configuration http malware-sites threshold 5", parents=()),
    ConfigLine(config_line="set shared botnet configuration http recent-domains enabled yes", parents=()),
    ConfigLine(config_line="set shared botnet configuration http recent-domains threshold 5", parents=()),
    ConfigLine(config_line="set shared botnet configuration http ip-domains enabled yes", parents=()),
    ConfigLine(config_line="set shared botnet configuration http ip-domains threshold 10", parents=()),
    ConfigLine(
        config_line="set shared botnet configuration http executables-from-unknown-sites enabled yes", parents=()
    ),
    ConfigLine(
        config_line="set shared botnet configuration http executables-from-unknown-sites threshold 5", parents=()
    ),
    ConfigLine(config_line="set shared botnet configuration other-applications irc yes", parents=()),
    ConfigLine(
        config_line="set shared botnet configuration unknown-applications unknown-tcp destinations-per-hour 10",
        parents=(),
    ),
    ConfigLine(
        config_line="set shared botnet configuration unknown-applications unknown-tcp sessions-per-hour 10", parents=()
    ),
    ConfigLine(
        config_line="set shared botnet configuration unknown-applications unknown-tcp session-length maximum-bytes 100",
        parents=(),
    ),
    ConfigLine(
        config_line="set shared botnet configuration unknown-applications unknown-tcp session-length minimum-bytes 50",
        parents=(),
    ),
    ConfigLine(
        config_line="set shared botnet configuration unknown-applications unknown-udp destinations-per-hour 10",
        parents=(),
    ),
    ConfigLine(
        config_line="set shared botnet configuration unknown-applications unknown-udp sessions-per-hour 10", parents=()
    ),
    ConfigLine(
        config_line="set shared botnet configuration unknown-applications unknown-udp session-length maximum-bytes 100",
        parents=(),
    ),
    ConfigLine(
        config_line="set shared botnet configuration unknown-applications unknown-udp session-length minimum-bytes 50",
        parents=(),
    ),
    ConfigLine(config_line="set shared botnet report topn 100", parents=()),
    ConfigLine(config_line="set shared botnet report scheduled yes", parents=()),
    ConfigLine(config_line="set shared application-status awesun", parents=()),
    ConfigLine(config_line="set shared application-status hikvision-http", parents=()),
    ConfigLine(config_line="set shared application-status notion-base", parents=()),
    ConfigLine(config_line="set shared application-status notion-delete", parents=()),
    ConfigLine(config_line="set shared application-status notion-download", parents=()),
    ConfigLine(config_line="set shared application-status notion-logout", parents=()),
    ConfigLine(config_line="set shared application-status notion-upload", parents=()),
    ConfigLine(
        config_line="set network interface ethernet ethernet1/1 layer3 ipv6 neighbor-discovery router-advertisement enable no",
        parents=(),
    ),
    ConfigLine(
        config_line="set network interface ethernet ethernet1/1 layer3 ndp-proxy enabled no",
        parents=(),
    ),
    ConfigLine(
        config_line="set network interface ethernet ethernet1/1 layer3 dhcp-client create-default-route yes",
        parents=(),
    ),
    ConfigLine(
        config_line="set network interface ethernet ethernet1/1 layer3 lldp enable no",
        parents=(),
    ),
    ConfigLine(
        config_line="set network interface ethernet ethernet1/2 layer3 ipv6 neighbor-discovery router-advertisement enable no",
        parents=(),
    ),
    ConfigLine(
        config_line="set network interface ethernet ethernet1/2 layer3 ndp-proxy enabled no",
        parents=(),
    ),
    ConfigLine(
        config_line="set network interface ethernet ethernet1/2 layer3 dhcp-client create-default-route no",
        parents=(),
    ),
    ConfigLine(
        config_line="set network interface ethernet ethernet1/2 layer3 lldp enable no",
        parents=(),
    ),
    ConfigLine(
        config_line="set network interface ethernet ethernet1/2 layer3 interface-management-profile mgt",
        parents=(),
    ),
    ConfigLine(
        config_line="set network interface ethernet ethernet1/2 link-state auto",
        parents=(),
    ),
    ConfigLine(config_line="set network profiles monitor-profile default interval 3", parents=()),
    ConfigLine(config_line="set network profiles monitor-profile default threshold 5", parents=()),
    ConfigLine(
        config_line="set network profiles monitor-profile default action wait-recover",
        parents=(),
    ),
    ConfigLine(config_line="set network profiles interface-management-profile", parents=()),
    ConfigLine(
        config_line="set network ike crypto-profiles ike-crypto-profiles default encryption [ aes-128-cbc 3des]",
        parents=(),
    ),
    ConfigLine(
        config_line="set network ike crypto-profiles ike-crypto-profiles default hash sha1",
        parents=(),
    ),
    ConfigLine(
        config_line="set network ike crypto-profiles ike-crypto-profiles default dh-group group2",
        parents=(),
    ),
    ConfigLine(
        config_line="set network ike crypto-profiles ike-crypto-profiles default lifetime hours 8",
        parents=(),
    ),
    ConfigLine(
        config_line="set network ike crypto-profiles ike-crypto-profiles Suite-B-GCM-128 encryption aes-128-cbc",
        parents=(),
    ),
    ConfigLine(
        config_line="set network ike crypto-profiles ike-crypto-profiles Suite-B-GCM-128 hash sha256",
        parents=(),
    ),
    ConfigLine(
        config_line="set network ike crypto-profiles ike-crypto-profiles Suite-B-GCM-128 dh-group group19",
        parents=(),
    ),
    ConfigLine(
        config_line="set network ike crypto-profiles ike-crypto-profiles Suite-B-GCM-128 lifetime hours 8",
        parents=(),
    ),
    ConfigLine(
        config_line="set network ike crypto-profiles ike-crypto-profiles Suite-B-GCM-256 encryption aes-256-cbc",
        parents=(),
    ),
    ConfigLine(
        config_line="set network ike crypto-profiles ike-crypto-profiles Suite-B-GCM-256 hash sha384",
        parents=(),
    ),
    ConfigLine(
        config_line="set network ike crypto-profiles ike-crypto-profiles Suite-B-GCM-256 dh-group group20",
        parents=(),
    ),
    ConfigLine(
        config_line="set network ike crypto-profiles ike-crypto-profiles Suite-B-GCM-256 lifetime hours 8",
        parents=(),
    ),
    ConfigLine(
        config_line="set network ike crypto-profiles ipsec-crypto-profiles default esp encryption [ aes-128-cbc 3des]",
        parents=(),
    ),
    ConfigLine(
        config_line="set network ike crypto-profiles ipsec-crypto-profiles default esp authentication sha1",
        parents=(),
    ),
    ConfigLine(
        config_line="set network ike crypto-profiles ipsec-crypto-profiles default dh-group group2",
        parents=(),
    ),
    ConfigLine(
        config_line="set network ike crypto-profiles ipsec-crypto-profiles default lifetime hours 1",
        parents=(),
    ),
    ConfigLine(
        config_line="set network ike crypto-profiles ipsec-crypto-profiles Suite-B-GCM-128 esp encryption aes-128-gcm",
        parents=(),
    ),
    ConfigLine(
        config_line="set network ike crypto-profiles ipsec-crypto-profiles Suite-B-GCM-128 esp authentication none",
        parents=(),
    ),
    ConfigLine(
        config_line="set network ike crypto-profiles ipsec-crypto-profiles Suite-B-GCM-128 dh-group group19",
        parents=(),
    ),
    ConfigLine(
        config_line="set network ike crypto-profiles ipsec-crypto-profiles Suite-B-GCM-128 lifetime hours 1",
        parents=(),
    ),
    ConfigLine(
        config_line="set network ike crypto-profiles ipsec-crypto-profiles Suite-B-GCM-256 esp encryption aes-256-gcm",
        parents=(),
    ),
    ConfigLine(
        config_line="set network ike crypto-profiles ipsec-crypto-profiles Suite-B-GCM-256 esp authentication none",
        parents=(),
    ),
    ConfigLine(
        config_line="set network ike crypto-profiles ipsec-crypto-profiles Suite-B-GCM-256 dh-group group20",
        parents=(),
    ),
    ConfigLine(
        config_line="set network ike crypto-profiles ipsec-crypto-profiles Suite-B-GCM-256 lifetime hours 1",
        parents=(),
    ),
    ConfigLine(
        config_line="set network ike crypto-profiles global-protect-app-crypto-profiles default encryption aes-128-cbc",
        parents=(),
    ),
    ConfigLine(
        config_line="set network ike crypto-profiles global-protect-app-crypto-profiles default authentication sha1",
        parents=(),
    ),
    ConfigLine(
        config_line="set network qos profile default class-bandwidth-type mbps class class1 priority real-time",
        parents=(),
    ),
    ConfigLine(
        config_line="set network qos profile default class-bandwidth-type mbps class class2 priority high",
        parents=(),
    ),
    ConfigLine(
        config_line="set network qos profile default class-bandwidth-type mbps class class3 priority high",
        parents=(),
    ),
    ConfigLine(
        config_line="set network qos profile default class-bandwidth-type mbps class class4 priority medium",
        parents=(),
    ),
    ConfigLine(
        config_line="set network qos profile default class-bandwidth-type mbps class class5 priority medium",
        parents=(),
    ),
    ConfigLine(
        config_line="set network qos profile default class-bandwidth-type mbps class class6 priority low",
        parents=(),
    ),
    ConfigLine(
        config_line="set network qos profile default class-bandwidth-type mbps class class7 priority low",
        parents=(),
    ),
    ConfigLine(
        config_line="set network qos profile default class-bandwidth-type mbps class class8 priority low",
        parents=(),
    ),
    ConfigLine(config_line="set network virtual-router", parents=()),
    ConfigLine(
        config_line="set deviceconfig system type dhcp-client send-hostname yes",
        parents=(),
    ),
    ConfigLine(
        config_line="set deviceconfig system type dhcp-client send-client-id yes",
        parents=(),
    ),
    ConfigLine(
        config_line="set deviceconfig system type dhcp-client accept-dhcp-hostname no",
        parents=(),
    ),
    ConfigLine(
        config_line="set deviceconfig system type dhcp-client accept-dhcp-domain yes",
        parents=(),
    ),
    ConfigLine(
        config_line="set deviceconfig system update-server updates.paloaltonetworks.com",
        parents=(),
    ),
    ConfigLine(config_line="set deviceconfig system update-schedule", parents=()),
    ConfigLine(config_line="set deviceconfig system service disable-telnet yes", parents=()),
    ConfigLine(config_line="set deviceconfig system service disable-http yes", parents=()),
    ConfigLine(config_line="set deviceconfig system hostname firewall1", parents=()),
    ConfigLine(config_line='set deviceconfig system login-banner "', parents=()),
    ConfigLine(
        config_line="************************************************************************\n*                        firewall1.example.com                       *                         [PROD VM500  firewalls]\n************************************************************************\n*                               WARNING                                *\n*   Unauthorized access to this device or devices attached to          *\n*   or accessible from this network is strictly prohibited.            *\n*   Possession of passwords or devices enabling access to this         *\n*   device or devices does not constitute authorization. Unauthorized  *\n*   access will be prosecuted to the fullest extent of the law.        *\n*                                                                      *\n************************************************************************\n\n^C",
        parents=('set deviceconfig system login-banner "',),
    ),
    ConfigLine(
        config_line="set deviceconfig system panorama local-panorama panorama-server 10.0.0.1",
        parents=(),
    ),
    ConfigLine(
        config_line="set deviceconfig system panorama local-panorama panorama-server-2 10.0.0.2",
        parents=(),
    ),
    ConfigLine(config_line="set deviceconfig setting config rematch yes", parents=()),
    ConfigLine(
        config_line="set deviceconfig setting management hostname-type-in-syslog FQDN",
        parents=(),
    ),
    ConfigLine(
        config_line="set deviceconfig setting management initcfg public-key thisisasuperduperlongbase64encodedstring=",
        parents=(),
    ),
    ConfigLine(
        config_line="set deviceconfig setting management initcfg type dhcp-client send-hostname yes",
        parents=(),
    ),
    ConfigLine(
        config_line="set deviceconfig setting management initcfg type dhcp-client send-client-id yes",
        parents=(),
    ),
    ConfigLine(
        config_line="set deviceconfig setting management initcfg type dhcp-client accept-dhcp-hostname yes",
        parents=(),
    ),
    ConfigLine(
        config_line="set deviceconfig setting management initcfg type dhcp-client accept-dhcp-domain yes",
        parents=(),
    ),
    ConfigLine(
        config_line="set deviceconfig setting management initcfg dns-primary 8.8.8.8",
        parents=(),
    ),
    ConfigLine(
        config_line="set deviceconfig setting management initcfg op-command-modes mgmt-interface-swap",
        parents=(),
    ),
    ConfigLine(config_line="set vsys vsys1 zone", parents=()),
    ConfigLine(
        config_line="set vsys vsys1 import network interface [ ethernet1/1 ethernet1/2 vlan loopback tunnel]",
        parents=(),
    ),
    ConfigLine(config_line="set vsys vsys1 import network vlan", parents=()),
    ConfigLine(config_line="set vsys vsys1 import network virtual-router", parents=()),
    ConfigLine(config_line="set vsys vsys1 import network virtual-wire", parents=()),
    ConfigLine(config_line="set vsys vsys1 address", parents=()),
    ConfigLine(config_line="set vsys vsys1 rulebase security rules", parents=()),
    ConfigLine(config_line="set vsys vsys1 service", parents=()),
]
