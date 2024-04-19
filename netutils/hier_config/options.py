base_options: dict = {
    "style": None,
    "negation": "no",
    "syntax_style": "cisco",
    "sectional_overwrite": [],
    "sectional_overwrite_no_negate": [],
    "ordering": [],
    "indent_adjust": [],
    "parent_allows_duplicate_child": [],
    "sectional_exiting": [],
    "full_text_sub": [],
    "per_line_sub": [],
    "idempotent_commands_blacklist": [],
    "idempotent_commands": [],
    "negation_default_when": [],
    "negation_negate_with": [],
}
ios_options: dict = {
    "style": "ios",
    "ordering": [
        {"lineage": [{"startswith": "no vlan filter"}], "order": 700},
        {
            "lineage": [
                {"startswith": "interface"},
                {"startswith": "no shutdown"},
            ],
            "order": 700,
        },
    ],
    "sectional_exiting": [
        {
            "lineage": [
                {"startswith": "router bgp"},
                {"startswith": "template peer-policy"},
            ],
            "exit_text": "exit-peer-policy",
        },
        {
            "lineage": [
                {"startswith": "router bgp"},
                {"startswith": "template peer-session"},
            ],
            "exit_text": "exit-peer-session",
        },
        {
            "lineage": [
                {"startswith": "router bgp"},
                {"startswith": "address-family"},
            ],
            "exit_text": "exit-address-family",
        },
    ],
    "per_line_sub": [
        {"search": "^Building configuration.*", "replace": ""},
        {"search": "^Current configuration.*", "replace": ""},
        {"search": "^! Last configuration change.*", "replace": ""},
        {"search": "^! NVRAM config last updated.*", "replace": ""},
        {"search": "^ntp clock-period .*", "replace": ""},
        {"search": "^version.*", "replace": ""},
        {"search": "^ logging event link-status$", "replace": ""},
        {"search": "^ logging event subif-link-status$", "replace": ""},
        {"search": "^\\s*ipv6 unreachables disable$", "replace": ""},
        {"search": "^end$", "replace": ""},
        {"search": "^\\s*[#!].*", "replace": ""},
        {"search": "^ no ip address", "replace": ""},
        {"search": "^ exit-peer-policy", "replace": ""},
        {"search": "^ exit-peer-session", "replace": ""},
        {"search": "^ exit-address-family", "replace": ""},
        {"search": "^crypto key generate rsa general-keys.*$", "replace": ""},
    ],
    "idempotent_commands": [
        {"lineage": [{"startswith": "vlan"}, {"startswith": "name"}]},
        {"lineage": [{"startswith": "interface"}, {"startswith": "description"}]},
        {"lineage": [{"startswith": "interface"}, {"startswith": "ip address"}]},
    ],
}
iosxe_options: dict = {
    "style": "ios",
    "sectional_overwrite": [{"lineage": [{"startswith": "ipv6 access-list"}]}],
    "sectional_exiting": [
        {
            "lineage": [
                {"startswith": "router bgp"},
                {"startswith": "template peer-policy"},
            ],
            "exit_text": "exit-peer-policy",
        },
        {
            "lineage": [
                {"startswith": "router bgp"},
                {"startswith": "template peer-session"},
            ],
            "exit_text": "exit-peer-session",
        },
        {
            "lineage": [{"startswith": "router bgp"}, {"startswith": "address-family"}],
            "exit_text": "exit-address-family",
        },
    ],
    "per_line_sub": [
        {"search": "^Building configuration.*", "replace": ""},
        {"search": "^Current configuration.*", "replace": ""},
        {"search": "^! Last configuration change.*", "replace": ""},
        {"search": "^! NVRAM config last updated.*", "replace": ""},
        {"search": "^ntp clock-period .*", "replace": ""},
        {"search": "^version.*", "replace": ""},
        {"search": "^ logging event link-status$", "replace": ""},
        {"search": "^ logging event subif-link-status$", "replace": ""},
        {"search": "^\\s*ipv6 unreachables disable$", "replace": ""},
        {"search": "^end$", "replace": ""},
        {"search": "^ no ip address", "replace": ""},
        {"search": "^ exit-peer-policy", "replace": ""},
        {"search": "^ exit-peer-session", "replace": ""},
        {"search": "^ exit-address-family", "replace": ""},
    ],
    "idempotent_commands": [
        {
            "lineage": [
                {"startswith": "router ospf"},
                {"startswith": ["log-adjacency-changes"]},
            ]
        },
        {"lineage": [{"startswith": "router ospf"}, {"startswith": ["router-id"]}]},
        {
            "lineage": [
                {"startswith": "ipv6 router ospf"},
                {"startswith": ["log-adjacency-changes"]},
            ]
        },
        {
            "lineage": [
                {"startswith": "ipv6 router ospf"},
                {"startswith": ["router-id"]},
            ]
        },
        {"lineage": [{"startswith": "router bgp"}, {"startswith": "bgp router-id"}]},
        {
            "lineage": [
                {"startswith": "router bgp"},
                {"re_search": "neighbor \\S+ description"},
            ]
        },
        {"lineage": [{"startswith": ["hostname"]}]},
        {"lineage": [{"contains": ["source-interface", "trap-source"]}]},
        {"lineage": [{"startswith": ["snmp-server community"]}]},
        {"lineage": [{"startswith": ["mac address-table aging-time"]}]},
        {"lineage": [{"startswith": ["aaa authentication"]}]},
        {"lineage": [{"startswith": ["aaa authorization"]}]},
        {"lineage": [{"startswith": ["errdisable recovery"]}]},
        {"lineage": [{"startswith": "line"}, {"startswith": ["access-class"]}]},
        {"lineage": [{"startswith": "line"}, {"startswith": ["ipv6 access-class"]}]},
        {"lineage": [{"startswith": "interface"}, {"startswith": ["ip ospf cost"]}]},
        {"lineage": [{"startswith": "interface"}, {"startswith": ["ipv6 ospf cost"]}]},
        {
            "lineage": [
                {"startswith": "interface"},
                {"re_search": ["standby \\d authentication"]},
            ]
        },
        {
            "lineage": [
                {"startswith": "interface"},
                {"re_search": ["standby \\d priority"]},
            ]
        },
        {"lineage": [{"startswith": "username admin "}]},
        {
            "lineage": [
                {"startswith": "policy-map system-cpp-policy"},
                {"startswith": "class"},
                {"startswith": "police"},
            ]
        },
        {"lineage": [{"startswith": "banner"}]},
        {"lineage": [{"startswith": "logging facility"}]},
        {"lineage": [{"startswith": "ip tftp source-interface"}]},
        {"lineage": [{"startswith": "snmp-server trap-source"}]},
        {"lineage": [{"startswith": "power redundancy-mode"}]},
    ],
}
iosxr_options: dict = {
    "style": "iosxr",
    "ordering": [
        {"lineage": [{"startswith": "vrf "}], "order": 300},
        {"lineage": [{"startswith": "no vrf "}], "order": 700},
    ],
    "sectional_overwrite": [{"lineage": [{"startswith": "template"}]}],
    "sectional_overwrite_no_negate": [
        {"lineage": [{"startswith": "as-path-set"}]},
        {"lineage": [{"startswith": "prefix-set"}]},
        {"lineage": [{"startswith": "route-policy"}]},
        {"lineage": [{"startswith": "extcommunity-set"}]},
        {"lineage": [{"startswith": "community-set"}]},
    ],
    "parent_allows_duplicate_child": [{"lineage": [{"startswith": "route-policy"}]}],
    "sectional_exiting": [
        {"lineage": [{"startswith": "route-policy"}], "exit_text": "end-policy"},
        {"lineage": [{"startswith": "prefix-set"}], "exit_text": "end-set"},
        {"lineage": [{"startswith": "policy-map"}], "exit_text": "end-policy-map"},
        {"lineage": [{"startswith": "class-map"}], "exit_text": "end-class-map"},
        {"lineage": [{"startswith": "community-set"}], "exit_text": "end-set"},
        {"lineage": [{"startswith": "extcommunity-set"}], "exit_text": "end-set"},
        {"lineage": [{"equals": "rsvp"}], "exit_text": "exit"},
        {"lineage": [{"equals": "mpls traffic-eng"}], "exit_text": "exit"},
        {"lineage": [{"startswith": "mpls ldp"}], "exit_text": "exit"},
        {"lineage": [{"startswith": "router ospf"}], "exit_text": "exit"},
        {"lineage": [{"startswith": "router ospfv3"}], "exit_text": "exit"},
        {"lineage": [{"startswith": "template"}], "exit_text": "end-template"},
        {"lineage": [{"startswith": "interface"}], "exit_text": "root"},
        {"lineage": [{"startswith": "router bgp"}], "exit_text": "root"},
    ],
    "indent_adjust": [{"start_expression": "^\\s*template", "end_expression": "^\\s*end-template"}],
    "per_line_sub": [
        {"search": "^Building configuration.*", "replace": ""},
        {"search": "^Current configuration.*", "replace": ""},
        {"search": "^ntp clock-period .*", "replace": ""},
        {"search": ".*speed.*", "replace": ""},
        {"search": ".*duplex.*", "replace": ""},
        {"search": ".*negotiation auto.*", "replace": ""},
        {"search": ".*parity none.*", "replace": ""},
        {"search": "^end-policy$", "replace": " end-policy"},
        {"search": "^end-set$", "replace": " end-set"},
        {"search": "^end$", "replace": ""},
        {"search": "^\\s*[#!].*", "replace": ""},
    ],
    "idempotent_commands": [
        {
            "lineage": [
                {"startswith": "router bgp"},
                {"startswith": "vrf"},
                {"startswith": "address-family"},
                {"startswith": "additional-paths selection route-policy"},
            ]
        },
        {"lineage": [{"startswith": "router bgp"}, {"startswith": "bgp router-id"}]},
        {
            "lineage": [
                {"startswith": "router bgp"},
                {"startswith": "neighbor-group"},
                {"startswith": "address-family"},
                {"startswith": "soft-reconfiguration inbound"},
            ]
        },
        {
            "lineage": [
                {"startswith": "router bgp"},
                {"startswith": "vrf"},
                {"startswith": "neighbor"},
                {"startswith": "address-family"},
                {"startswith": ["soft-reconfiguration inbound", "maximum-prefix"]},
            ]
        },
        {
            "lineage": [
                {"startswith": "router bgp"},
                {"startswith": "vrf"},
                {"startswith": "neighbor"},
                {"startswith": ["password", "description"]},
            ]
        },
        {
            "lineage": [
                {"startswith": "router bgp"},
                {"startswith": "neighbor"},
                {"startswith": ["description", "password"]},
            ]
        },
        {
            "lineage": [
                {"startswith": "router ospf"},
                {"startswith": "area"},
                {"startswith": "interface"},
                {"startswith": "cost"},
            ]
        },
        {"lineage": [{"startswith": "router ospf"}, {"startswith": "router-id"}]},
        {
            "lineage": [
                {"startswith": "router ospf"},
                {"startswith": "area"},
                {"startswith": "message-digest-key"},
            ]
        },
        {
            "lineage": [
                {"startswith": "router ospf"},
                {"startswith": "max-metric router-lsa"},
            ]
        },
        {"lineage": [{"equals": "l2vpn"}, {"startswith": "router-id"}]},
        {"lineage": [{"re_search": "logging \\d+.\\d+.\\d+.\\d+ vrf MGMT"}]},
        {
            "lineage": [
                {"equals": "line default"},
                {"startswith": "access-class ingress"},
            ]
        },
        {"lineage": [{"equals": "line default"}, {"startswith": "transport input"}]},
        {"lineage": [{"startswith": "hostname"}]},
        {"lineage": [{"startswith": "logging source-interface"}]},
        {"lineage": [{"startswith": "interface"}, {"startswith": "ipv4 address"}]},
        {"lineage": [{"startswith": "snmp-server community"}]},
        {"lineage": [{"startswith": "snmp-server location"}]},
        {"lineage": [{"equals": "line console"}, {"startswith": "exec-timeout"}]},
        {
            "lineage": [
                {"equals": "mpls ldp"},
                {"startswith": "session protection duration"},
            ]
        },
        {"lineage": [{"equals": "mpls ldp"}, {"startswith": "igp sync delay"}]},
        {"lineage": [{"startswith": "interface"}, {"startswith": ["mtu"]}]},
        {"lineage": [{"startswith": "banner"}]},
    ],
}
nxos_options: dict = {
    "style": "nxos",
    "per_line_sub": [
        {"search": "^Building configuration.*", "replace": ""},
        {"search": "^Current configuration.*", "replace": ""},
        {"search": "^ntp clock-period .*", "replace": ""},
        {"search": "^snmp-server location  ", "replace": "snmp-server location "},
        {"search": "^version.*", "replace": ""},
        {"search": "^boot (system|kickstart) .*", "replace": ""},
        {"search": "!.*", "replace": ""},
    ],
    "idempotent_commands_blacklist": [
        {
            "lineage": [
                {"startswith": "interface"},
                {"re_search": "ip address.*secondary"},
            ]
        }
    ],
    "idempotent_commands": [
        {
            "lineage": [
                {
                    "startswith": [
                        "power redundancy-mode",
                        "cli alias name wr ",
                        "aaa authentication login console",
                        "port-channel load-balance",
                        "hostname",
                        "ip tftp source-interface",
                        "ip telnet source-interface",
                        "ip tacacs source-interface",
                        "logging source-interface",
                    ],
                    "re_search": "^spanning-tree vlan ([\\d,-]+) priority",
                }
            ]
        },
        {"lineage": [{"startswith": ["hardware access-list tcam region ifacl"]}]},
        {"lineage": [{"startswith": ["hardware access-list tcam region vacl"]}]},
        {"lineage": [{"startswith": ["hardware access-list tcam region qos"]}]},
        {"lineage": [{"startswith": ["hardware access-list tcam region racl"]}]},
        {"lineage": [{"startswith": ["hardware access-list tcam region ipv6-racl"]}]},
        {"lineage": [{"startswith": ["hardware access-list tcam region e-ipv6-racl"]}]},
        {"lineage": [{"startswith": ["hardware access-list tcam region l3qos"]}]},
        {
            "lineage": [
                {"startswith": "router ospf"},
                {"startswith": "vrf"},
                {"startswith": ["maximum-paths", "log-adjacency-changes"]},
            ]
        },
        {
            "lineage": [
                {"startswith": "router ospf"},
                {"startswith": ["maximum-paths", "log-adjacency-changes"]},
            ]
        },
        {
            "lineage": [
                {"startswith": "router bgp"},
                {"startswith": "vrf"},
                {"startswith": "address-family"},
                {"startswith": ["maximum-paths"]},
            ]
        },
        {
            "lineage": [
                {"startswith": "router bgp"},
                {"startswith": "address-family"},
                {"startswith": ["maximum-paths"]},
            ]
        },
        {
            "lineage": [
                {"startswith": "router bgp"},
                {"startswith": "template"},
                {"startswith": "address-family"},
                {"startswith": "send-community"},
            ]
        },
        {
            "lineage": [
                {"startswith": "interface"},
                {"re_search": "^hsrp \\d+"},
                {"startswith": ["ip", "priority", "authentication md5 key-string"]},
            ]
        },
        {
            "lineage": [
                {"startswith": "interface"},
                {
                    "startswith": [
                        "ip address",
                        "duplex",
                        "speed",
                        "switchport mode",
                        "switchport access vlan",
                        "switchport trunk native vlan",
                        "switchport trunk allowed vlan",
                        "udld port",
                        "ip ospf cost",
                        "ipv6 link-local",
                        "ospfv3 cost",
                    ]
                },
            ]
        },
        {"lineage": [{"startswith": "interface"}, {"startswith": "mtu"}]},
        {"lineage": [{"equals": "line console"}, {"startswith": "exec-timeout"}]},
        {
            "lineage": [
                {"startswith": "line vty"},
                {
                    "startswith": [
                        "transport input",
                        "ipv6 access-class",
                        "access-class",
                    ]
                },
            ]
        },
        {
            "lineage": [
                {"startswith": "router bgp"},
                {
                    "startswith": "bgp router-id",
                    "re_search": "neighbor \\S+ description",
                },
            ]
        },
        {
            "lineage": [
                {"startswith": "router ospf"},
                {"startswith": ["router-id", "log-adjacency-changes"]},
            ]
        },
        {
            "lineage": [
                {"startswith": "ipv6 router ospf"},
                {"startswith": ["router-id", "log-adjacency-changes"]},
            ]
        },
        {
            "lineage": [
                {
                    "startswith": [
                        "mac address-table aging-time",
                        "snmp-server community",
                        "snmp-server location",
                    ]
                }
            ]
        },
        {"lineage": [{"startswith": "vpc domain"}, {"startswith": "role priority"}]},
        {"lineage": [{"startswith": "banner"}]},
        {"lineage": [{"startswith": "username admin password 5"}]},
        {
            "lineage": [
                {"equals": "policy-map type control-plane copp-system-policy"},
                {"startswith": "class"},
                {"startswith": "police"},
            ]
        },
        {
            "lineage": [
                {"startswith": "router bgp"},
                {"startswith": "vrf"},
                {"startswith": "neighbor"},
                {"startswith": "address-family"},
                {"startswith": "soft-reconfiguration inbound"},
            ]
        },
        {
            "lineage": [
                {"startswith": "router bgp"},
                {"startswith": "vrf"},
                {"startswith": "neighbor"},
                {"startswith": "password"},
            ]
        },
    ],
    "negation_default_when": [
        {
            "lineage": [
                {"startswith": "interface"},
                {
                    "startswith": "ip ospf bfd",
                    "re_search": "standby \\d+ authentication md5 key-string",
                },
            ]
        },
        {
            "lineage": [
                {"startswith": "router bgp"},
                {"startswith": "neighbor"},
                {"startswith": "address-family"},
                {"equals": "send-community"},
            ]
        },
        {
            "lineage": [
                {"startswith": "interface"},
                {"contains": "ip ospf passive-interface"},
            ]
        },
        {
            "lineage": [
                {"startswith": "interface"},
                {"contains": "ospfv3 passive-interface"},
            ]
        },
    ],
    "negation_negate_with": [
        {
            "lineage": [
                {"startswith": "router bgp"},
                {"startswith": "address-family"},
                {"startswith": "maximum-paths ibgp"},
            ],
            "use": "default maximum-paths ibgp",
        },
        {
            "lineage": [
                {"startswith": "router bgp"},
                {"startswith": "vrf"},
                {"startswith": "address-family"},
                {"startswith": "maximum-paths ibgp"},
            ],
            "use": "default maximum-paths ibgp",
        },
        {
            "lineage": [{"equals": "line vty"}, {"startswith": "session-limit"}],
            "use": "session-limit 32",
        },
    ],
}
eos_options: dict = {
    "style": "eos",
    "sectional_exiting": [
        {
            "lineage": [
                {"startswith": "router bgp"},
                {"startswith": "template peer-policy"},
            ],
            "exit_text": "exit-peer-policy",
        },
        {
            "lineage": [
                {"startswith": "router bgp"},
                {"startswith": "template peer-session"},
            ],
            "exit_text": "exit-peer-session",
        },
        {
            "lineage": [{"startswith": "router bgp"}, {"startswith": "address-family"}],
            "exit_text": "exit-address-family",
        },
    ],
    "per_line_sub": [
        {"search": "^Building configuration.*", "replace": ""},
        {"search": "^Current configuration.*", "replace": ""},
        {"search": "^! Last configuration change.*", "replace": ""},
        {"search": "^! NVRAM config last updated.*", "replace": ""},
        {"search": "^ntp clock-period .*", "replace": ""},
        {"search": "^version.*", "replace": ""},
        {"search": "^ logging event link-status$", "replace": ""},
        {"search": "^ logging event subif-link-status$", "replace": ""},
        {"search": "^\\s*ipv6 unreachables disable$", "replace": ""},
        {"search": "^end$", "replace": ""},
        {"search": "^\\s*[#!].*", "replace": ""},
        {"search": "^ no ip address", "replace": ""},
        {"search": "^ exit-peer-policy", "replace": ""},
        {"search": "^ exit-peer-session", "replace": ""},
        {"search": "^ exit-address-family", "replace": ""},
    ],
    "idempotent_commands": [
        {"lineage": [{"startswith": "hostname"}]},
        {"lineage": [{"startswith": "logging source-interface"}]},
        {"lineage": [{"startswith": "interface"}, {"startswith": "ip address"}]},
        {
            "lineage": [
                {"startswith": "line vty"},
                {
                    "startswith": [
                        "transport input",
                        "access-class",
                        "ipv6 access-class",
                    ]
                },
            ]
        },
        {
            "lineage": [
                {"startswith": "interface"},
                {"re_search": "standby \\d+ (priority|authentication md5)"},
            ]
        },
        {"lineage": [{"startswith": "router bgp"}, {"startswith": "bgp router-id"}]},
        {
            "lineage": [
                {"startswith": "router ospf"},
                {"startswith": ["router-id", "max-lsa", "maximum-paths"]},
            ]
        },
        {"lineage": [{"startswith": "ipv6 router ospf"}, {"startswith": "router-id"}]},
        {
            "lineage": [
                {"startswith": "router ospf"},
                {"startswith": "log-adjacency-changes"},
            ]
        },
        {
            "lineage": [
                {"startswith": "ipv6 router ospf"},
                {"startswith": "log-adjacency-changes"},
            ]
        },
        {
            "lineage": [
                {"startswith": "router bgp"},
                {"re_search": "neighbor \\S+ description"},
            ]
        },
        {"lineage": [{"startswith": "snmp-server community"}]},
        {"lineage": [{"startswith": "snmp-server location"}]},
        {"lineage": [{"equals": "line con 0"}, {"startswith": "exec-timeout"}]},
        {
            "lineage": [
                {"startswith": "interface"},
                {"startswith": "ip ospf message-digest-key"},
            ]
        },
        {"lineage": [{"startswith": "logging buffered"}]},
        {"lineage": [{"startswith": "tacacs-server key"}]},
        {"lineage": [{"startswith": "logging facility"}]},
        {"lineage": [{"startswith": "vlan internal allocation policy"}]},
        {"lineage": [{"startswith": "username admin"}]},
        {"lineage": [{"startswith": "snmp-server user"}]},
        {"lineage": [{"startswith": "banner"}]},
        {"lineage": [{"startswith": "ntp source"}]},
        {"lineage": [{"startswith": "management"}, {"startswith": "idle-timeout"}]},
        {"lineage": [{"startswith": "aaa authentication enable default group tacacs+"}]},
        {
            "lineage": [
                {"equals": "control-plane"},
                {"equals": "ip access-group CPP in"},
            ]
        },
        {"lineage": [{"startswith": "interface"}, {"startswith": "mtu"}]},
        {"lineage": [{"startswith": "snmp-server source-interface"}]},
        {"lineage": [{"startswith": "ip tftp client source-interface"}]},
    ],
    "negation_default_when": [
        {
            "lineage": [
                {"startswith": "interface"},
                {"equals": "logging event link-status"},
            ]
        }
    ],
}


junos_options: dict = {
    "style": "junos",
    "negation": "delete",
    "syntax_style": "juniper",
}


vyos_options: dict = {
    "style": "vyos",
    "negation": "delete",
    "syntax_style": "juniper",
}


def options_for(os: str) -> dict:
    """Create base options on an OS level."""
    options: dict = {
        "ios": ios_options,
        "iosxe": iosxe_options,
        "iosxr": iosxr_options,
        "nxos": nxos_options,
        "eos": eos_options,
        "junos": junos_options,
        "vyos": vyos_options,
    }

    if options.get(os):
        return {**base_options, **options[os]}

    return {**base_options, "style": os}
