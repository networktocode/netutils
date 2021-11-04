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
    ConfigLine(config_line="end", parents=()),
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
    ConfigLine(config_line="end", parents=()),
    ConfigLine(config_line="config system switch-interface", parents=()),
    ConfigLine(config_line="end", parents=()),
    ConfigLine(config_line="config system lte-modem", parents=()),
    ConfigLine(config_line="    set status disable", parents=("config system lte-modem",)),
    ConfigLine(config_line="    set extra-init ''", parents=("config system lte-modem",)),
    ConfigLine(config_line="    set authtype none", parents=("config system lte-modem",)),
    ConfigLine(config_line="    set apn ''", parents=("config system lte-modem",)),
    ConfigLine(config_line="    set modem-port 255", parents=("config system lte-modem",)),
    ConfigLine(config_line="end", parents=()),
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
    ConfigLine(config_line="        end", parents=("config system interface", '    edit "mgmt"')),
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
    ConfigLine(config_line="    next", parents=("config system interface",)),
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
    ConfigLine(config_line="        end", parents=("config system interface", '    edit "ha"')),
    ConfigLine(config_line="        set speed auto", parents=("config system interface", '    edit "ha"')),
    ConfigLine(config_line="        set mtu-override disable", parents=("config system interface", '    edit "ha"')),
    ConfigLine(config_line="        set wccp disable", parents=("config system interface", '    edit "ha"')),
    ConfigLine(
        config_line="        set drop-overlapped-fragment disable", parents=("config system interface", '    edit "ha"')
    ),
    ConfigLine(config_line="        set drop-fragment disable", parents=("config system interface", '    edit "ha"')),
    ConfigLine(config_line="    next", parents=("config system interface",)),
    ConfigLine(config_line="end", parents=()),
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
        config_line="            next",
        parents=("config system virtual-switch", '    edit "lan"', "        config port"),
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
        config_line="            next",
        parents=("config system virtual-switch", '    edit "lan"', "        config port"),
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
        config_line="            next",
        parents=("config system virtual-switch", '    edit "lan"', "        config port"),
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
        config_line="            next",
        parents=("config system virtual-switch", '    edit "lan"', "        config port"),
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
        config_line="            next",
        parents=("config system virtual-switch", '    edit "lan"', "        config port"),
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
        config_line="            next",
        parents=("config system virtual-switch", '    edit "lan"', "        config port"),
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
        config_line="            next",
        parents=("config system virtual-switch", '    edit "lan"', "        config port"),
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
        config_line="            next",
        parents=("config system virtual-switch", '    edit "lan"', "        config port"),
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
        config_line="            next",
        parents=("config system virtual-switch", '    edit "lan"', "        config port"),
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
        config_line="            next",
        parents=("config system virtual-switch", '    edit "lan"', "        config port"),
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
        config_line="            next",
        parents=("config system virtual-switch", '    edit "lan"', "        config port"),
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
        config_line="            next",
        parents=("config system virtual-switch", '    edit "lan"', "        config port"),
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
        config_line="            next",
        parents=("config system virtual-switch", '    edit "lan"', "        config port"),
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
        config_line="            next",
        parents=("config system virtual-switch", '    edit "lan"', "        config port"),
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
        config_line="            next",
        parents=("config system virtual-switch", '    edit "lan"', "        config port"),
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
    ConfigLine(
        config_line="            next",
        parents=("config system virtual-switch", '    edit "lan"', "        config port"),
    ),
    ConfigLine(config_line="        end", parents=("config system virtual-switch", '    edit "lan"')),
    ConfigLine(config_line="    next", parents=("config system virtual-switch",)),
    ConfigLine(config_line="end", parents=()),
]
