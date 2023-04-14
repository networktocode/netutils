from netutils.config.parser import ConfigLine

data = [
    ConfigLine(config_line="/interface bridge add name=google-vpc-peering-iface", parents=()),
    ConfigLine(config_line="/interface bridge add name=loopback", parents=()),
    ConfigLine(config_line="/interface bonding add mode=802.3ad name=Po1 slaves=sfp-sfpplus1,sfp-sfpplus2", parents=()),
    ConfigLine(config_line="/interface vlan add interface=Po1 name=vlan11-mgmt vlan-id=11", parents=()),
    ConfigLine(
        config_line="/interface vlan add interface=vlan2933-Transit-to-CC-NNI name=vlan3049-Transit-to-XXX vlan-id=3049",
        parents=(),
    ),
    ConfigLine(
        config_line="/interface vlan add disabled=yes interface=Po1 name=vlan3051-Transit-to-CSW-through-QoE-Disabled vlan-id=3051",
        parents=(),
    ),
    ConfigLine(
        config_line="/interface vlan add interface=Po1 mtu=1300 name=vlan3225-Transit-CORE-Agg1-to-COREXXX vlan-id=3225",
        parents=(),
    ),
    ConfigLine(
        config_line="/interface wireless security-profiles set [ find default=yes ] supplicant-identity=MikroTik",
        parents=(),
    ),
    ConfigLine(
        config_line="/ip ipsec peer add address=50.157.100.38/32 exchange-mode=ike2 local-address=55.106.77.11 name=google-vpc-peer",
        parents=(),
    ),
    ConfigLine(config_line="/ip pool add name=BNEdgeLiteTest ranges=192.168.69.254", parents=()),
    ConfigLine(config_line="/ip pool add name=BNEdgeLiteTest2 ranges=192.168.70.254", parents=()),
    ConfigLine(
        config_line="/ip dhcp-server add address-pool=BNEdgeLiteTest disabled=no interface=ether1 name=dhcp1",
        parents=(),
    ),
    ConfigLine(
        config_line="/ip dhcp-server add address-pool=BNEdgeLiteTest2 disabled=no interface=ether2 name=dhcp2",
        parents=(),
    ),
    ConfigLine(config_line="/routing bgp instance set default as=1234 router-id=10.127.1.3", parents=()),
    ConfigLine(config_line="/routing ospf instance set [ find default=yes ] router-id=10.127.1.3", parents=()),
    ConfigLine(config_line="/snmp community add addresses=::/0 name=somestringa", parents=()),
    ConfigLine(
        config_line="/system logging action set 3 bsd-syslog=yes remote=172.16.11.1 remote-port=5140", parents=()
    ),
    ConfigLine(
        config_line="/user group set full policy=local,telnet,ssh,ftp,reboot,read,write,policy,test,winbox,password,web,sniff,sensitive,api,romon,dude,tikapp",
        parents=(),
    ),
    ConfigLine(
        config_line="/user group add name=prom policy=ssh,read,winbox,api,!local,!telnet,!ftp,!reboot,!write,!policy,!test,!password,!web,!sniff,!sensitive,!romon,!dude,!tikapp",
        parents=(),
    ),
    ConfigLine(config_line="/ip neighbor discovery-settings set discover-interface-list=!dynamic", parents=()),
    ConfigLine(config_line="/ip address add address=10.0.11.13/24 interface=vlan11-mgmt network=10.0.11.0", parents=()),
    ConfigLine(config_line="/ip address add address=192.168.69.1/24 interface=ether1 network=192.168.69.0", parents=()),
    ConfigLine(config_line="/ip dhcp-server network add address=192.168.69.0/24 gateway=192.168.69.1", parents=()),
    ConfigLine(config_line="/ip dhcp-server network add address=192.168.70.0/24 gateway=192.168.70.1", parents=()),
    ConfigLine(config_line="/ip dns set servers=8.8.8.8", parents=()),
    ConfigLine(config_line="/ip firewall address-list add address=34.157.17.38 list=whitelist", parents=()),
    ConfigLine(config_line="/ip firewall address-list add address=72.202.79.109 list=google-vpc-acl", parents=()),
    ConfigLine(config_line="/ip firewall address-list add address=34.157.17.38 list=google-vpc-acl", parents=()),
    ConfigLine(
        config_line="/ip firewall filter add action=drop chain=input dst-address=50.106.77.11 src-address-list=!google-vpc-acl",
        parents=(),
    ),
    ConfigLine(
        config_line="/ip firewall nat add action=dst-nat chain=dstnat dst-address=50.106.77.11 dst-port=443 protocol=tcp to-addresses=10.1.15.10",
        parents=(),
    ),
    ConfigLine(
        config_line="/ip firewall nat add action=masquerade chain=srcnat out-interface=vlan12-Servers", parents=()
    ),
    ConfigLine(
        config_line="/ip firewall nat add action=src-nat chain=srcnat src-address=50.64.0.75 to-addresses=55.106.77.11",
        parents=(),
    ),
    ConfigLine(config_line="/ip ipsec identity add peer=google-vpc-peer secret=*****", parents=()),
    ConfigLine(config_line="/ip ipsec policy set 0 disabled=yes", parents=()),
    ConfigLine(
        config_line="/ip ipsec policy add disabled=yes dst-address=169.254.1.1/32 peer=google-vpc-peer src-address=169.254.1.2/32 tunnel=yes",
        parents=(),
    ),
    ConfigLine(
        config_line="/ip ipsec policy add disabled=yes dst-address=10.150.0.0/20 peer=google-vpc-peer src-address=0.0.0.0/0 tunnel=yes",
        parents=(),
    ),
    ConfigLine(config_line="/ip service set telnet disabled=yes", parents=()),
    ConfigLine(config_line="/ip service set ftp disabled=yes", parents=()),
    ConfigLine(config_line="/ip service set www disabled=yes", parents=()),
    ConfigLine(config_line="/ip service set api address=10.1.15.5/32,10.120.16.0/20,172.16.11.0/24", parents=()),
    ConfigLine(config_line="/ip service set api-ssl disabled=yes", parents=()),
    ConfigLine(config_line="/routing bgp network add network=55.106.77.11/32 synchronize=no", parents=()),
    ConfigLine(config_line="/routing bgp network add network=55.106.77.12/32 synchronize=no", parents=()),
    ConfigLine(
        config_line="/routing bgp peer add in-filter=ibgp-allow-default-in name=CSW out-filter=ibgp-no-default-out remote-address=10.127.1.10 remote-as=12345 update-source=loopback",
        parents=(),
    ),
    ConfigLine(
        config_line="/routing filter add action=discard chain=ibgp-no-default-out prefix=10.127.1.0/24", parents=()
    ),
    ConfigLine(
        config_line="/routing filter add action=accept chain=ibgp-no-default-out prefix=10.64.0.0/10 prefix-length=22-32",
        parents=(),
    ),
    ConfigLine(
        config_line="/routing ospf interface add dead-interval=8s hello-interval=2s interface=vlan3049-Transit-to-85Presidential network-type=point-to-point",
        parents=(),
    ),
    ConfigLine(
        config_line="/routing ospf interface add cost=11 dead-interval=8s hello-interval=2s interface=vlan3166-Transit-HalseyCore-Agg1-to-Indigo-5 network-type=point-to-point",
        parents=(),
    ),
    ConfigLine(config_line="/routing ospf network add area=backbone network=10.126.0.16/29", parents=()),
    ConfigLine(config_line="/routing ospf network add area=backbone network=10.127.1.3/32", parents=()),
    ConfigLine(config_line="/snmp set enabled=yes trap-community=somestring", parents=()),
    ConfigLine(config_line="/system clock set time-zone-name=America/New_York", parents=()),
    ConfigLine(config_line="/system identity set name=ag1.123site.nwk.nj", parents=()),
    ConfigLine(config_line="/system logging add action=remote topics=error", parents=()),
    ConfigLine(config_line="/system logging add action=remote topics=info", parents=()),
    ConfigLine(
        config_line='/system note set note="This is a \\\\\\"System Note\\\\\\" for a Mikrotik router.\\\\n\\\\\\\n    \\nIt includes double quotes (\\\\\\") and special characters such as:\\\\n\\\\\\\n    \\n@, #, \\$, %, ^, &, *, (, ), _, +, [, ], {, }, |, ;, \',\', ., /, <, >, and \\?.\\\\n\\\\\\\n    \\n\\\\n\\\\\\\n    \\nRemember to escape any special characters with a backslash (\\\\\\\\) when necessary.\\\\n\\\\\\\n    \\n\\\\n\\\\\\\n    \\nThis is a multiline note with several lines of text.\\\\n\\\\\\\n    \\nWow, what a great example of a note to ensure proper parsing by NetUtils!\n    \\nWe are treating this as a banner."',
        parents=(),
    ),
]
