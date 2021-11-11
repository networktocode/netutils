from netutils.config.parser import ConfigLine

data = [
    ConfigLine(config_line="config system global", parents=()),
    ConfigLine(config_line="    set admin-concurrent enable", parents=("config system global",)),
    ConfigLine(config_line="    set admin-console-timeout 0", parents=("config system global",)),
    ConfigLine(config_line="    set admin-hsts-max-age 15552000", parents=("config system global",)),
    ConfigLine(config_line="    set admin-https-pki-required disable", parents=("config system global",)),
    ConfigLine(config_line="    set admin-https-redirect enable", parents=("config system global",)),
    ConfigLine(
        config_line="    set admin-https-ssl-versions tlsv1-1 tlsv1-2 tlsv1-3", parents=("config system global",)
    ),
    ConfigLine(config_line="    set admin-lockout-duration 60", parents=("config system global",)),
    ConfigLine(config_line="    set admin-lockout-threshold 3", parents=("config system global",)),
    ConfigLine(config_line="    set admin-login-max 100", parents=("config system global",)),
    ConfigLine(config_line="config wireless-controller global", parents=()),
    ConfigLine(config_line="    set name ''", parents=("config wireless-controller global",)),
    ConfigLine(config_line="    set location ''", parents=("config wireless-controller global",)),
    ConfigLine(config_line="    set image-download enable", parents=("config wireless-controller global",)),
    ConfigLine(config_line="    set max-retransmit 3", parents=("config wireless-controller global",)),
    ConfigLine(
        config_line="    set control-message-offload ebp-frame aeroscout-tag ap-list sta-list sta-cap-list stats aeroscout-mu sta-health spectral-analysis",
        parents=("config wireless-controller global",),
    ),
    ConfigLine(config_line="    set data-ethernet-II enable", parents=("config wireless-controller global",)),
    ConfigLine(config_line="    set link-aggregation disable", parents=("config wireless-controller global",)),
    ConfigLine(config_line="    set mesh-eth-type 8755", parents=("config wireless-controller global",)),
    ConfigLine(config_line="    set fiapp-eth-type 5252", parents=("config wireless-controller global",)),
    ConfigLine(config_line="    set discovery-mc-addr 224.0.1.140", parents=("config wireless-controller global",)),
    ConfigLine(config_line="    set max-clients 0", parents=("config wireless-controller global",)),
    ConfigLine(config_line="    set rogue-scan-mac-adjacency 7", parents=("config wireless-controller global",)),
    ConfigLine(config_line="    set ipsec-base-ip 169.254.0.1", parents=("config wireless-controller global",)),
    ConfigLine(config_line="    set wtp-share disable", parents=("config wireless-controller global",)),
    ConfigLine(config_line="    set ap-log-server disable", parents=("config wireless-controller global",)),
    ConfigLine(config_line="config system switch-interface", parents=()),
    ConfigLine(config_line="config system lte-modem", parents=()),
    ConfigLine(config_line="    set status disable", parents=("config system lte-modem",)),
    ConfigLine(config_line="    set extra-init ''", parents=("config system lte-modem",)),
    ConfigLine(config_line="    set authtype none", parents=("config system lte-modem",)),
    ConfigLine(config_line="    set apn ''", parents=("config system lte-modem",)),
    ConfigLine(config_line="    set modem-port 255", parents=("config system lte-modem",)),
    ConfigLine(config_line="config system interface", parents=()),
    ConfigLine(config_line='    edit "mgmt"', parents=("config system interface",)),
    ConfigLine(config_line="        set vrf 0", parents=("config system interface", '    edit "mgmt"')),
    ConfigLine(config_line="        set distance 5", parents=("config system interface", '    edit "mgmt"')),
    ConfigLine(config_line="        set priority 0", parents=("config system interface", '    edit "mgmt"')),
    ConfigLine(
        config_line="        set dhcp-relay-service disable", parents=("config system interface", '    edit "mgmt"')
    ),
    ConfigLine(
        config_line="        set ip 10.0.0.41 255.255.252.0", parents=("config system interface", '    edit "mgmt"')
    ),
    ConfigLine(
        config_line="        set allowaccess ping https ssh snmp http fgfm",
        parents=("config system interface", '    edit "mgmt"'),
    ),
    ConfigLine(config_line="        set fail-detect disable", parents=("config system interface", '    edit "mgmt"')),
    ConfigLine(config_line="        set arpforward enable", parents=("config system interface", '    edit "mgmt"')),
    ConfigLine(
        config_line="        set broadcast-forward disable", parents=("config system interface", '    edit "mgmt"')
    ),
    ConfigLine(config_line="        set bfd global", parents=("config system interface", '    edit "mgmt"')),
    ConfigLine(config_line="        set l2forward disable", parents=("config system interface", '    edit "mgmt"')),
    ConfigLine(
        config_line="        set icmp-send-redirect enable", parents=("config system interface", '    edit "mgmt"')
    ),
    ConfigLine(
        config_line="        set icmp-accept-redirect enable", parents=("config system interface", '    edit "mgmt"')
    ),
    ConfigLine(config_line="        set vlanforward disable", parents=("config system interface", '    edit "mgmt"')),
    ConfigLine(config_line="        set stpforward disable", parents=("config system interface", '    edit "mgmt"')),
    ConfigLine(
        config_line="        set ips-sniffer-mode disable", parents=("config system interface", '    edit "mgmt"')
    ),
    ConfigLine(config_line="        set ident-accept disable", parents=("config system interface", '    edit "mgmt"')),
    ConfigLine(config_line="        set ipmac disable", parents=("config system interface", '    edit "mgmt"')),
    ConfigLine(config_line="        set subst disable", parents=("config system interface", '    edit "mgmt"')),
    ConfigLine(
        config_line="        set substitute-dst-mac 00:00:00:00:00:00",
        parents=("config system interface", '    edit "mgmt"'),
    ),
    ConfigLine(config_line="        set status up", parents=("config system interface", '    edit "mgmt"')),
    ConfigLine(
        config_line="        set netbios-forward disable", parents=("config system interface", '    edit "mgmt"')
    ),
    ConfigLine(config_line="        set wins-ip 0.0.0.0", parents=("config system interface", '    edit "mgmt"')),
    ConfigLine(config_line="        set type physical", parents=("config system interface", '    edit "mgmt"')),
    ConfigLine(
        config_line="        set dedicated-to management", parents=("config system interface", '    edit "mgmt"')
    ),
    ConfigLine(
        config_line="        set netflow-sampler disable", parents=("config system interface", '    edit "mgmt"')
    ),
    ConfigLine(config_line="        set sflow-sampler disable", parents=("config system interface", '    edit "mgmt"')),
    ConfigLine(config_line="        set src-check enable", parents=("config system interface", '    edit "mgmt"')),
    ConfigLine(config_line="        set sample-rate 2000", parents=("config system interface", '    edit "mgmt"')),
    ConfigLine(config_line="        set polling-interval 20", parents=("config system interface", '    edit "mgmt"')),
    ConfigLine(config_line="        set sample-direction both", parents=("config system interface", '    edit "mgmt"')),
    ConfigLine(
        config_line="        set explicit-web-proxy disable", parents=("config system interface", '    edit "mgmt"')
    ),
    ConfigLine(
        config_line="        set explicit-ftp-proxy disable", parents=("config system interface", '    edit "mgmt"')
    ),
    ConfigLine(
        config_line="        set proxy-captive-portal disable", parents=("config system interface", '    edit "mgmt"')
    ),
    ConfigLine(config_line="        set tcp-mss 0", parents=("config system interface", '    edit "mgmt"')),
    ConfigLine(config_line="        set inbandwidth 0", parents=("config system interface", '    edit "mgmt"')),
    ConfigLine(config_line="        set outbandwidth 0", parents=("config system interface", '    edit "mgmt"')),
    ConfigLine(
        config_line="        set egress-shaping-profile ''", parents=("config system interface", '    edit "mgmt"')
    ),
    ConfigLine(
        config_line="        set ingress-shaping-profile ''", parents=("config system interface", '    edit "mgmt"')
    ),
    ConfigLine(
        config_line="        set disconnect-threshold 0", parents=("config system interface", '    edit "mgmt"')
    ),
    ConfigLine(config_line="        set spillover-threshold 0", parents=("config system interface", '    edit "mgmt"')),
    ConfigLine(
        config_line="        set ingress-spillover-threshold 0", parents=("config system interface", '    edit "mgmt"')
    ),
    ConfigLine(config_line="        set weight 0", parents=("config system interface", '    edit "mgmt"')),
    ConfigLine(config_line="        set external disable", parents=("config system interface", '    edit "mgmt"')),
    ConfigLine(config_line="        set description ''", parents=("config system interface", '    edit "mgmt"')),
    ConfigLine(config_line="        set alias ''", parents=("config system interface", '    edit "mgmt"')),
    ConfigLine(
        config_line="        set device-identification disable", parents=("config system interface", '    edit "mgmt"')
    ),
    ConfigLine(config_line="        set lldp-reception vdom", parents=("config system interface", '    edit "mgmt"')),
    ConfigLine(
        config_line="        set lldp-transmission vdom", parents=("config system interface", '    edit "mgmt"')
    ),
    ConfigLine(
        config_line="        set estimated-upstream-bandwidth 0", parents=("config system interface", '    edit "mgmt"')
    ),
    ConfigLine(
        config_line="        set estimated-downstream-bandwidth 0",
        parents=("config system interface", '    edit "mgmt"'),
    ),
    ConfigLine(
        config_line="        set measured-upstream-bandwidth 0", parents=("config system interface", '    edit "mgmt"')
    ),
    ConfigLine(
        config_line="        set measured-downstream-bandwidth 0",
        parents=("config system interface", '    edit "mgmt"'),
    ),
    ConfigLine(
        config_line="        set bandwidth-measure-time 0", parents=("config system interface", '    edit "mgmt"')
    ),
    ConfigLine(
        config_line="        set monitor-bandwidth disable", parents=("config system interface", '    edit "mgmt"')
    ),
    ConfigLine(
        config_line="        set vrrp-virtual-mac disable", parents=("config system interface", '    edit "mgmt"')
    ),
    ConfigLine(config_line="        set role lan", parents=("config system interface", '    edit "mgmt"')),
    ConfigLine(config_line="        set snmp-index 1", parents=("config system interface", '    edit "mgmt"')),
    ConfigLine(config_line="        set secondary-IP disable", parents=("config system interface", '    edit "mgmt"')),
    ConfigLine(
        config_line="        set preserve-session-route disable", parents=("config system interface", '    edit "mgmt"')
    ),
    ConfigLine(
        config_line="        set auto-auth-extension-device disable",
        parents=("config system interface", '    edit "mgmt"'),
    ),
    ConfigLine(config_line="        set ap-discover enable", parents=("config system interface", '    edit "mgmt"')),
    ConfigLine(
        config_line="        set switch-controller-igmp-snooping-proxy disable",
        parents=("config system interface", '    edit "mgmt"'),
    ),
    ConfigLine(
        config_line="        set switch-controller-igmp-snooping-fast-leave disable",
        parents=("config system interface", '    edit "mgmt"'),
    ),
    ConfigLine(config_line="        config ipv6", parents=("config system interface", '    edit "mgmt"')),
    ConfigLine(
        config_line="            set ip6-mode static",
        parents=("config system interface", '    edit "mgmt"', "        config ipv6"),
    ),
    ConfigLine(
        config_line="            set nd-mode basic",
        parents=("config system interface", '    edit "mgmt"', "        config ipv6"),
    ),
    ConfigLine(
        config_line="            set ip6-address ::/0",
        parents=("config system interface", '    edit "mgmt"', "        config ipv6"),
    ),
    ConfigLine(
        config_line="            unset ip6-allowaccess",
        parents=("config system interface", '    edit "mgmt"', "        config ipv6"),
    ),
    ConfigLine(
        config_line="            set icmp6-send-redirect enable",
        parents=("config system interface", '    edit "mgmt"', "        config ipv6"),
    ),
    ConfigLine(
        config_line="            set ip6-reachable-time 0",
        parents=("config system interface", '    edit "mgmt"', "        config ipv6"),
    ),
    ConfigLine(
        config_line="            set ip6-retrans-time 0",
        parents=("config system interface", '    edit "mgmt"', "        config ipv6"),
    ),
    ConfigLine(
        config_line="            set ip6-hop-limit 0",
        parents=("config system interface", '    edit "mgmt"', "        config ipv6"),
    ),
    ConfigLine(
        config_line="            set vrrp-virtual-mac6 disable",
        parents=("config system interface", '    edit "mgmt"', "        config ipv6"),
    ),
    ConfigLine(
        config_line="            set vrip6_link_local ::",
        parents=("config system interface", '    edit "mgmt"', "        config ipv6"),
    ),
    ConfigLine(
        config_line="            set ip6-send-adv disable",
        parents=("config system interface", '    edit "mgmt"', "        config ipv6"),
    ),
    ConfigLine(
        config_line="            set autoconf disable",
        parents=("config system interface", '    edit "mgmt"', "        config ipv6"),
    ),
    ConfigLine(config_line="        set defaultgw enable", parents=("config system interface", '    edit "mgmt"')),
    ConfigLine(
        config_line="        set dns-server-override enable", parents=("config system interface", '    edit "mgmt"')
    ),
    ConfigLine(config_line="        set speed auto", parents=("config system interface", '    edit "mgmt"')),
    ConfigLine(
        config_line="        set trust-ip-1 0.0.0.0 0.0.0.0", parents=("config system interface", '    edit "mgmt"')
    ),
    ConfigLine(
        config_line="        set trust-ip-2 0.0.0.0 0.0.0.0", parents=("config system interface", '    edit "mgmt"')
    ),
    ConfigLine(
        config_line="        set trust-ip-3 0.0.0.0 0.0.0.0", parents=("config system interface", '    edit "mgmt"')
    ),
    ConfigLine(config_line="        set trust-ip6-1 ::/0", parents=("config system interface", '    edit "mgmt"')),
    ConfigLine(config_line="        set trust-ip6-2 ::/0", parents=("config system interface", '    edit "mgmt"')),
    ConfigLine(config_line="        set trust-ip6-3 ::/0", parents=("config system interface", '    edit "mgmt"')),
    ConfigLine(config_line="        set mtu-override disable", parents=("config system interface", '    edit "mgmt"')),
    ConfigLine(config_line="        set wccp disable", parents=("config system interface", '    edit "mgmt"')),
    ConfigLine(
        config_line="        set drop-overlapped-fragment disable",
        parents=("config system interface", '    edit "mgmt"'),
    ),
    ConfigLine(config_line="        set drop-fragment disable", parents=("config system interface", '    edit "mgmt"')),
    ConfigLine(config_line='    edit "ha"', parents=("config system interface",)),
    ConfigLine(config_line='        set vdom "root"', parents=("config system interface", '    edit "ha"')),
    ConfigLine(config_line="        set vrf 0", parents=("config system interface", '    edit "ha"')),
    ConfigLine(config_line="        set fortilink disable", parents=("config system interface", '    edit "ha"')),
    ConfigLine(config_line="        set mode static", parents=("config system interface", '    edit "ha"')),
    ConfigLine(
        config_line="        set dhcp-relay-service disable", parents=("config system interface", '    edit "ha"')
    ),
    ConfigLine(
        config_line="        set management-ip 0.0.0.0 0.0.0.0", parents=("config system interface", '    edit "ha"')
    ),
    ConfigLine(config_line="        set ip 0.0.0.0 0.0.0.0", parents=("config system interface", '    edit "ha"')),
    ConfigLine(config_line="        unset allowaccess", parents=("config system interface", '    edit "ha"')),
    ConfigLine(config_line="        set fail-detect disable", parents=("config system interface", '    edit "ha"')),
    ConfigLine(config_line="        set arpforward enable", parents=("config system interface", '    edit "ha"')),
    ConfigLine(
        config_line="        set broadcast-forward disable", parents=("config system interface", '    edit "ha"')
    ),
    ConfigLine(config_line="        set bfd global", parents=("config system interface", '    edit "ha"')),
    ConfigLine(config_line="        set l2forward disable", parents=("config system interface", '    edit "ha"')),
    ConfigLine(
        config_line="        set icmp-send-redirect enable", parents=("config system interface", '    edit "ha"')
    ),
    ConfigLine(
        config_line="        set icmp-accept-redirect enable", parents=("config system interface", '    edit "ha"')
    ),
    ConfigLine(config_line="        set vlanforward disable", parents=("config system interface", '    edit "ha"')),
    ConfigLine(config_line="        set stpforward disable", parents=("config system interface", '    edit "ha"')),
    ConfigLine(
        config_line="        set ips-sniffer-mode disable", parents=("config system interface", '    edit "ha"')
    ),
    ConfigLine(config_line="        set ident-accept disable", parents=("config system interface", '    edit "ha"')),
    ConfigLine(config_line="        set ipmac disable", parents=("config system interface", '    edit "ha"')),
    ConfigLine(config_line="        set subst disable", parents=("config system interface", '    edit "ha"')),
    ConfigLine(
        config_line="        set substitute-dst-mac 00:00:00:00:00:00",
        parents=("config system interface", '    edit "ha"'),
    ),
    ConfigLine(config_line="        set status up", parents=("config system interface", '    edit "ha"')),
    ConfigLine(config_line="        set netbios-forward disable", parents=("config system interface", '    edit "ha"')),
    ConfigLine(config_line="        set wins-ip 0.0.0.0", parents=("config system interface", '    edit "ha"')),
    ConfigLine(config_line="        set type physical", parents=("config system interface", '    edit "ha"')),
    ConfigLine(config_line="        set netflow-sampler disable", parents=("config system interface", '    edit "ha"')),
    ConfigLine(config_line="        set sflow-sampler disable", parents=("config system interface", '    edit "ha"')),
    ConfigLine(config_line="        set src-check enable", parents=("config system interface", '    edit "ha"')),
    ConfigLine(config_line="        set sample-rate 2000", parents=("config system interface", '    edit "ha"')),
    ConfigLine(config_line="        set polling-interval 20", parents=("config system interface", '    edit "ha"')),
    ConfigLine(config_line="        set sample-direction both", parents=("config system interface", '    edit "ha"')),
    ConfigLine(
        config_line="        set explicit-web-proxy disable", parents=("config system interface", '    edit "ha"')
    ),
    ConfigLine(
        config_line="        set explicit-ftp-proxy disable", parents=("config system interface", '    edit "ha"')
    ),
    ConfigLine(
        config_line="        set proxy-captive-portal disable", parents=("config system interface", '    edit "ha"')
    ),
    ConfigLine(config_line="        set tcp-mss 0", parents=("config system interface", '    edit "ha"')),
    ConfigLine(config_line="        set inbandwidth 0", parents=("config system interface", '    edit "ha"')),
    ConfigLine(config_line="        set outbandwidth 0", parents=("config system interface", '    edit "ha"')),
    ConfigLine(
        config_line="        set egress-shaping-profile ''", parents=("config system interface", '    edit "ha"')
    ),
    ConfigLine(
        config_line="        set ingress-shaping-profile ''", parents=("config system interface", '    edit "ha"')
    ),
    ConfigLine(config_line="        set disconnect-threshold 0", parents=("config system interface", '    edit "ha"')),
    ConfigLine(config_line="        set spillover-threshold 0", parents=("config system interface", '    edit "ha"')),
    ConfigLine(
        config_line="        set ingress-spillover-threshold 0", parents=("config system interface", '    edit "ha"')
    ),
    ConfigLine(config_line="        set weight 0", parents=("config system interface", '    edit "ha"')),
    ConfigLine(config_line="        set external disable", parents=("config system interface", '    edit "ha"')),
    ConfigLine(config_line="        set description ''", parents=("config system interface", '    edit "ha"')),
    ConfigLine(config_line="        set alias ''", parents=("config system interface", '    edit "ha"')),
    ConfigLine(config_line="        set security-mode none", parents=("config system interface", '    edit "ha"')),
    ConfigLine(
        config_line="        set device-identification disable", parents=("config system interface", '    edit "ha"')
    ),
    ConfigLine(config_line="        set lldp-reception vdom", parents=("config system interface", '    edit "ha"')),
    ConfigLine(config_line="        set lldp-transmission vdom", parents=("config system interface", '    edit "ha"')),
    ConfigLine(
        config_line="        set estimated-upstream-bandwidth 0", parents=("config system interface", '    edit "ha"')
    ),
    ConfigLine(
        config_line="        set estimated-downstream-bandwidth 0", parents=("config system interface", '    edit "ha"')
    ),
    ConfigLine(
        config_line="        set measured-upstream-bandwidth 0", parents=("config system interface", '    edit "ha"')
    ),
    ConfigLine(
        config_line="        set measured-downstream-bandwidth 0", parents=("config system interface", '    edit "ha"')
    ),
    ConfigLine(
        config_line="        set bandwidth-measure-time 0", parents=("config system interface", '    edit "ha"')
    ),
    ConfigLine(
        config_line="        set monitor-bandwidth disable", parents=("config system interface", '    edit "ha"')
    ),
    ConfigLine(
        config_line="        set vrrp-virtual-mac disable", parents=("config system interface", '    edit "ha"')
    ),
    ConfigLine(config_line="        set role undefined", parents=("config system interface", '    edit "ha"')),
    ConfigLine(config_line="        set snmp-index 2", parents=("config system interface", '    edit "ha"')),
    ConfigLine(config_line="        set secondary-IP disable", parents=("config system interface", '    edit "ha"')),
    ConfigLine(
        config_line="        set preserve-session-route disable", parents=("config system interface", '    edit "ha"')
    ),
    ConfigLine(
        config_line="        set auto-auth-extension-device disable",
        parents=("config system interface", '    edit "ha"'),
    ),
    ConfigLine(config_line="        set ap-discover enable", parents=("config system interface", '    edit "ha"')),
    ConfigLine(
        config_line="        set ip-managed-by-fortiipam disable", parents=("config system interface", '    edit "ha"')
    ),
    ConfigLine(
        config_line="        set switch-controller-mgmt-vlan 4094", parents=("config system interface", '    edit "ha"')
    ),
    ConfigLine(
        config_line="        set switch-controller-igmp-snooping-proxy disable",
        parents=("config system interface", '    edit "ha"'),
    ),
    ConfigLine(
        config_line="        set switch-controller-igmp-snooping-fast-leave disable",
        parents=("config system interface", '    edit "ha"'),
    ),
    ConfigLine(config_line="        set swc-first-create 0", parents=("config system interface", '    edit "ha"')),
    ConfigLine(config_line="        config ipv6", parents=("config system interface", '    edit "ha"')),
    ConfigLine(
        config_line="            set ip6-mode static",
        parents=("config system interface", '    edit "ha"', "        config ipv6"),
    ),
    ConfigLine(
        config_line="            set nd-mode basic",
        parents=("config system interface", '    edit "ha"', "        config ipv6"),
    ),
    ConfigLine(
        config_line="            set ip6-address ::/0",
        parents=("config system interface", '    edit "ha"', "        config ipv6"),
    ),
    ConfigLine(
        config_line="            unset ip6-allowaccess",
        parents=("config system interface", '    edit "ha"', "        config ipv6"),
    ),
    ConfigLine(
        config_line="            set icmp6-send-redirect enable",
        parents=("config system interface", '    edit "ha"', "        config ipv6"),
    ),
    ConfigLine(
        config_line="            set ip6-reachable-time 0",
        parents=("config system interface", '    edit "ha"', "        config ipv6"),
    ),
    ConfigLine(
        config_line="            set ip6-retrans-time 0",
        parents=("config system interface", '    edit "ha"', "        config ipv6"),
    ),
    ConfigLine(
        config_line="            set ip6-hop-limit 0",
        parents=("config system interface", '    edit "ha"', "        config ipv6"),
    ),
    ConfigLine(
        config_line="            set dhcp6-prefix-delegation disable",
        parents=("config system interface", '    edit "ha"', "        config ipv6"),
    ),
    ConfigLine(
        config_line="            set dhcp6-information-request disable",
        parents=("config system interface", '    edit "ha"', "        config ipv6"),
    ),
    ConfigLine(
        config_line="            set vrrp-virtual-mac6 disable",
        parents=("config system interface", '    edit "ha"', "        config ipv6"),
    ),
    ConfigLine(
        config_line="            set vrip6_link_local ::",
        parents=("config system interface", '    edit "ha"', "        config ipv6"),
    ),
    ConfigLine(
        config_line="            set ip6-send-adv disable",
        parents=("config system interface", '    edit "ha"', "        config ipv6"),
    ),
    ConfigLine(
        config_line="            set autoconf disable",
        parents=("config system interface", '    edit "ha"', "        config ipv6"),
    ),
    ConfigLine(
        config_line="            set dhcp6-relay-service disable",
        parents=("config system interface", '    edit "ha"', "        config ipv6"),
    ),
    ConfigLine(config_line="        set speed auto", parents=("config system interface", '    edit "ha"')),
    ConfigLine(config_line="        set mtu-override disable", parents=("config system interface", '    edit "ha"')),
    ConfigLine(config_line="        set wccp disable", parents=("config system interface", '    edit "ha"')),
    ConfigLine(
        config_line="        set drop-overlapped-fragment disable", parents=("config system interface", '    edit "ha"')
    ),
    ConfigLine(config_line="        set drop-fragment disable", parents=("config system interface", '    edit "ha"')),
    ConfigLine(config_line="config system virtual-switch", parents=()),
    ConfigLine(config_line='    edit "lan"', parents=("config system virtual-switch",)),
    ConfigLine(
        config_line='        set physical-switch "sw0"', parents=("config system virtual-switch", '    edit "lan"')
    ),
    ConfigLine(config_line="        set span disable", parents=("config system virtual-switch", '    edit "lan"')),
    ConfigLine(config_line="        config port", parents=("config system virtual-switch", '    edit "lan"')),
    ConfigLine(
        config_line='            edit "port1"',
        parents=("config system virtual-switch", '    edit "lan"', "        config port"),
    ),
    ConfigLine(
        config_line="                set speed auto",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port1"'),
    ),
    ConfigLine(
        config_line="                set status up",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port1"'),
    ),
    ConfigLine(
        config_line="                set alias ''",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port1"'),
    ),
    ConfigLine(
        config_line='            edit "port2"',
        parents=("config system virtual-switch", '    edit "lan"', "        config port"),
    ),
    ConfigLine(
        config_line="                set speed auto",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port2"'),
    ),
    ConfigLine(
        config_line="                set status up",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port2"'),
    ),
    ConfigLine(
        config_line="                set alias ''",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port2"'),
    ),
    ConfigLine(
        config_line='            edit "port3"',
        parents=("config system virtual-switch", '    edit "lan"', "        config port"),
    ),
    ConfigLine(
        config_line="                set speed auto",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port3"'),
    ),
    ConfigLine(
        config_line="                set status up",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port3"'),
    ),
    ConfigLine(
        config_line="                set alias ''",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port3"'),
    ),
    ConfigLine(
        config_line='            edit "port4"',
        parents=("config system virtual-switch", '    edit "lan"', "        config port"),
    ),
    ConfigLine(
        config_line="                set speed auto",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port4"'),
    ),
    ConfigLine(
        config_line="                set status up",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port4"'),
    ),
    ConfigLine(
        config_line="                set alias ''",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port4"'),
    ),
    ConfigLine(
        config_line='            edit "port5"',
        parents=("config system virtual-switch", '    edit "lan"', "        config port"),
    ),
    ConfigLine(
        config_line="                set speed auto",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port5"'),
    ),
    ConfigLine(
        config_line="                set status up",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port5"'),
    ),
    ConfigLine(
        config_line="                set alias ''",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port5"'),
    ),
    ConfigLine(
        config_line='            edit "port6"',
        parents=("config system virtual-switch", '    edit "lan"', "        config port"),
    ),
    ConfigLine(
        config_line="                set speed auto",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port6"'),
    ),
    ConfigLine(
        config_line="                set status up",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port6"'),
    ),
    ConfigLine(
        config_line="                set alias ''",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port6"'),
    ),
    ConfigLine(
        config_line='            edit "port7"',
        parents=("config system virtual-switch", '    edit "lan"', "        config port"),
    ),
    ConfigLine(
        config_line="                set speed auto",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port7"'),
    ),
    ConfigLine(
        config_line="                set status up",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port7"'),
    ),
    ConfigLine(
        config_line="                set alias ''",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port7"'),
    ),
    ConfigLine(
        config_line='            edit "port8"',
        parents=("config system virtual-switch", '    edit "lan"', "        config port"),
    ),
    ConfigLine(
        config_line="                set speed auto",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port8"'),
    ),
    ConfigLine(
        config_line="                set status up",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port8"'),
    ),
    ConfigLine(
        config_line="                set alias ''",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port8"'),
    ),
    ConfigLine(
        config_line='            edit "port9"',
        parents=("config system virtual-switch", '    edit "lan"', "        config port"),
    ),
    ConfigLine(
        config_line="                set speed auto",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port9"'),
    ),
    ConfigLine(
        config_line="                set status up",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port9"'),
    ),
    ConfigLine(
        config_line="                set alias ''",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port9"'),
    ),
    ConfigLine(
        config_line='            edit "port10"',
        parents=("config system virtual-switch", '    edit "lan"', "        config port"),
    ),
    ConfigLine(
        config_line="                set speed auto",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port10"'),
    ),
    ConfigLine(
        config_line="                set status up",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port10"'),
    ),
    ConfigLine(
        config_line="                set alias ''",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port10"'),
    ),
    ConfigLine(
        config_line='            edit "port11"',
        parents=("config system virtual-switch", '    edit "lan"', "        config port"),
    ),
    ConfigLine(
        config_line="                set speed auto",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port11"'),
    ),
    ConfigLine(
        config_line="                set status up",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port11"'),
    ),
    ConfigLine(
        config_line="                set alias ''",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port11"'),
    ),
    ConfigLine(
        config_line='            edit "port12"',
        parents=("config system virtual-switch", '    edit "lan"', "        config port"),
    ),
    ConfigLine(
        config_line="                set speed auto",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port12"'),
    ),
    ConfigLine(
        config_line="                set status up",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port12"'),
    ),
    ConfigLine(
        config_line="                set alias ''",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port12"'),
    ),
    ConfigLine(
        config_line='            edit "port13"',
        parents=("config system virtual-switch", '    edit "lan"', "        config port"),
    ),
    ConfigLine(
        config_line="                set speed auto",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port13"'),
    ),
    ConfigLine(
        config_line="                set status up",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port13"'),
    ),
    ConfigLine(
        config_line="                set alias ''",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port13"'),
    ),
    ConfigLine(
        config_line='            edit "port14"',
        parents=("config system virtual-switch", '    edit "lan"', "        config port"),
    ),
    ConfigLine(
        config_line="                set speed auto",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port14"'),
    ),
    ConfigLine(
        config_line="                set status up",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port14"'),
    ),
    ConfigLine(
        config_line="                set alias ''",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port14"'),
    ),
    ConfigLine(
        config_line='            edit "port15"',
        parents=("config system virtual-switch", '    edit "lan"', "        config port"),
    ),
    ConfigLine(
        config_line="                set speed auto",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port15"'),
    ),
    ConfigLine(
        config_line="                set status up",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port15"'),
    ),
    ConfigLine(
        config_line="                set alias ''",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port15"'),
    ),
    ConfigLine(
        config_line='            edit "port16"',
        parents=("config system virtual-switch", '    edit "lan"', "        config port"),
    ),
    ConfigLine(
        config_line="                set speed auto",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port16"'),
    ),
    ConfigLine(
        config_line="                set status up",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port16"'),
    ),
    ConfigLine(
        config_line="                set alias ''",
        parents=("config system virtual-switch", '    edit "lan"', "        config port", '            edit "port16"'),
    ),
    ConfigLine(config_line='config system replacemsg auth "auth-sms-token-page"', parents=()),
    ConfigLine(
        config_line='    set buffer "<!DOCTYPE html>\n<html lang=\\"en\\">\n    <head>\n        <meta charset=\\"UTF-8\\">\n        <meta http-equiv=\\"X-UA-Compatible\\" content=\\"IE=8; IE=EDGE\\">\n        <meta name=\\"viewport\\" content=\\"width=device-width, initial-scale=1\\">\n        <link href=\\"https://fonts.googleapis.com/css?family=Roboto&display=swap\\" rel=\\"stylesheet\\">\n        <style type=\\"text/css\\">\n            body {\n                height: 100%;\n                font-family: Roboto, Helvetica, Arial, sans-serif;\n                color: #6a6a6a;\n                margin: 0;\n                display: flex;\n                align-items: center;\n                justify-content: center;\n            }\n            input[type=date], input[type=email], input[type=number], input[type=password], input[type=search], input[type=tel], input[type=text], input[type=time], input[type=url], select, textarea {\n                color: #262626;\n                vertical-align: baseline;\n                margin: .2em;\n                border-style: solid;\n                border-width: 1px;\n                border-color: #a9a9a9;\n                background-color: #fff;\n                box-sizing: border-box;\n                padding: 2px .5em;\n                appearance: none;\n                border-radius: 0;\n            }\n            input:focus {\n                border-color: #646464;\n                box-shadow: 0 0 1px 0 #a2a2a2;\n                outline: 0;\n            }\n            button {\n                padding: .5em 1em;\n                border: 1px solid;\n                border-radius: 3px;\n                min-width: 6em;\n                font-weight: 400;\n                font-size: .8em;\n                cursor: pointer;\n            }\n            button.primary {\n                color: #fff;\n                background-color: rgb(47, 113, 178);\n                border-color: rgb(34, 103, 173);\n            }\n            .message-container {\n                height: 500px;\n                width: 600px;\n                padding: 0;\n                margin: 10px;\n            }\n            .logo {\n                background: url(%%IMAGE:logo_v3_fguard_app%%) no-repeat left center;\n                height: 267px;\n                object-fit: contain;\n            }\n            table {\n                background-color: #fff;\n                border-spacing: 0;\n                margin: 1em;\n            }\n            table > tbody > tr > td:first-of-type:not([colspan]) {\n                white-space: nowrap;\n                color: rgba(0,0,0,.5);\n            }\n            table > tbody > tr > td:first-of-type {\n                vertical-align: top;\n            }\n            table > tbody > tr > td {\n                padding: .3em .3em;\n            }\n            .field {\n                display: table-row;\n            }\n            .field > :first-child {\n                display: table-cell;\n                width: 20%;\n            }\n            .field.single > :first-child {\n                display: inline;\n            }\n            .field > :not(:first-child) {\n                width: auto;\n                max-width: 100%;\n                display: inline-flex;\n                align-items: baseline;\n                virtical-align: top;\n                box-sizing: border-box;\n                margin: .3em;\n            }\n            .field > :not(:first-child) > input {\n                width: 230px;\n            }\n            .form-footer {\n                display: inline-flex;\n                justify-content: flex-start;\n            }\n            .form-footer > * {\n                margin: 1em;\n            }\n            .text-scrollable {\n                overflow: auto;\n                height: 150px;\n                border: 1px solid rgb(200, 200, 200);\n                padding: 5px;\n                font-size: 1em;\n            }\n            .text-centered {\n                text-align: center;\n            }\n            .text-container {\n                margin: 1em 1.5em;\n            }\n            .flex-container {\n                display: flex;\n            }\n            .flex-container.column {\n                flex-direction: column;\n            }\n        </style>\n        <title>Firewall Authentication</title>\n    </head>\n    <body><div class=\\"message-container\\">\n    <div class=\\"logo\\"></div>\n    <h1>SMS Token Code Required</h1>\n    <form action=\\"%%AUTH_POST_URL%%\\" method=\\"post\\">\n        <input type=\\"hidden\\" name=\\"%%REQUESTID%%\\" value=\\"%%REQUESTVAL%%\\">\n        <input type=\\"hidden\\" name=\\"%%REDIRID%%\\" value=\\"%%PROTURI%%\\">\n        <input type=\\"hidden\\" name=\\"%%MAGICID%%\\" value=\\"%%MAGICVAL%%\\">\n        <input type=\\"hidden\\" name=\\"%%METHODID%%\\" value=\\"%%METHODVAL%%\\">\n        <p>%%QUESTION%%</p>\n        <div class=\\"field single\\">\n            <label for=\\"ft_un\\">Token Code</label>\n            <div>\n                <input name=\\"%%TOKENCODE%%\\" id=\\"ft_tc\\">\n            </div>\n        </div>\n        <p>%%EXTRAINFO%%</p>\n        <div class=\\"form-footer\\">\n            <button class=\\"primary\\" type=\\"submit\\" id=\\"ft_ci\\">Continue</button>\n        </div>\n    </form>\n</div></body>\n</html>\n"\n',
        parents=('config system replacemsg auth "auth-sms-token-page"',),
    ),
    ConfigLine(config_line="    set header http", parents=('config system replacemsg auth "auth-sms-token-page"',)),
    ConfigLine(config_line="    set format html", parents=('config system replacemsg auth "auth-sms-token-page"',)),
]
