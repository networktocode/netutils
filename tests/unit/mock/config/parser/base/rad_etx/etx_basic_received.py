from netutils.config.parser import ConfigLine

data = [
    ConfigLine(config_line="config flows", parents=()),
    ConfigLine(config_line='    classifier-profile "all" match-any', parents=("config flows",)),
    ConfigLine(config_line="        match all", parents=("config flows", '    classifier-profile "all" match-any')),
    ConfigLine(config_line='    flow "1__1_2"', parents=("config flows",)),
    ConfigLine(config_line='        classifier "all"', parents=("config flows", '    flow "1__1_2"')),
    ConfigLine(config_line="        ingress-port ethernet 1/1", parents=("config flows", '    flow "1__1_2"')),
    ConfigLine(
        config_line="        egress-port ethernet 1/3 queue 0 block 0/1", parents=("config flows", '    flow "1__1_2"')
    ),
    ConfigLine(config_line="        no shutdown", parents=("config flows", '    flow "1__1_2"')),
    ConfigLine(config_line='    flow "1__2_1"', parents=("config flows",)),
    ConfigLine(config_line='        classifier "all"', parents=("config flows", '    flow "1__2_1"')),
    ConfigLine(config_line="        ingress-port ethernet 1/3", parents=("config flows", '    flow "1__2_1"')),
    ConfigLine(
        config_line="        egress-port ethernet 1/1 queue 0 block 0/1", parents=("config flows", '    flow "1__2_1"')
    ),
    ConfigLine(config_line="        no shutdown", parents=("config flows", '    flow "1__2_1"')),
    ConfigLine(config_line='    flow "1__3_4"', parents=("config flows",)),
    ConfigLine(config_line='        classifier "all"', parents=("config flows", '    flow "1__3_4"')),
    ConfigLine(config_line="        ingress-port ethernet 1/4", parents=("config flows", '    flow "1__3_4"')),
    ConfigLine(
        config_line="        egress-port ethernet 1/5 queue 0 block 0/1", parents=("config flows", '    flow "1__3_4"')
    ),
    ConfigLine(config_line="        no shutdown", parents=("config flows", '    flow "1__3_4"')),
    ConfigLine(config_line='    flow "1__4_3"', parents=("config flows",)),
    ConfigLine(config_line='        classifier "all"', parents=("config flows", '    flow "1__4_3"')),
    ConfigLine(config_line="        ingress-port ethernet 1/5", parents=("config flows", '    flow "1__4_3"')),
    ConfigLine(
        config_line="        egress-port ethernet 1/4 queue 0 block 0/1", parents=("config flows", '    flow "1__4_3"')
    ),
    ConfigLine(config_line="        no shutdown", parents=("config flows", '    flow "1__4_3"')),
    ConfigLine(config_line='    flow "1__5_6"', parents=("config flows",)),
    ConfigLine(config_line='        classifier "all"', parents=("config flows", '    flow "1__5_6"')),
    ConfigLine(config_line="        ingress-port ethernet 1/6", parents=("config flows", '    flow "1__5_6"')),
    ConfigLine(
        config_line="        egress-port ethernet 1/7 queue 0 block 0/1", parents=("config flows", '    flow "1__5_6"')
    ),
    ConfigLine(config_line="        no shutdown", parents=("config flows", '    flow "1__5_6"')),
    ConfigLine(config_line='    flow "1__6_5"', parents=("config flows",)),
    ConfigLine(config_line='        classifier "all"', parents=("config flows", '    flow "1__6_5"')),
    ConfigLine(config_line="        ingress-port ethernet 1/7", parents=("config flows", '    flow "1__6_5"')),
    ConfigLine(
        config_line="        egress-port ethernet 1/6 queue 0 block 0/1", parents=("config flows", '    flow "1__6_5"')
    ),
    ConfigLine(config_line="        no shutdown", parents=("config flows", '    flow "1__6_5"')),
    ConfigLine(config_line='    flow "1__7_8"', parents=("config flows",)),
    ConfigLine(config_line='        classifier "all"', parents=("config flows", '    flow "1__7_8"')),
    ConfigLine(config_line="        ingress-port ethernet 1/8", parents=("config flows", '    flow "1__7_8"')),
    ConfigLine(
        config_line="        egress-port ethernet 1/2 queue 0 block 0/1", parents=("config flows", '    flow "1__7_8"')
    ),
    ConfigLine(config_line="        no shutdown", parents=("config flows", '    flow "1__7_8"')),
    ConfigLine(config_line='    flow "1__8_7"', parents=("config flows",)),
    ConfigLine(config_line='        classifier "all"', parents=("config flows", '    flow "1__8_7"')),
    ConfigLine(config_line="        ingress-port ethernet 1/2", parents=("config flows", '    flow "1__8_7"')),
    ConfigLine(
        config_line="        egress-port ethernet 1/8 queue 0 block 0/1", parents=("config flows", '    flow "1__8_7"')
    ),
    ConfigLine(config_line="        no shutdown", parents=("config flows", '    flow "1__8_7"')),
    ConfigLine(config_line='    flow "1_9__3_1"', parents=("config flows",)),
    ConfigLine(config_line='        classifier "all"', parents=("config flows", '    flow "1_9__3_1"')),
    ConfigLine(config_line="        ingress-port ethernet 1/9", parents=("config flows", '    flow "1_9__3_1"')),
    ConfigLine(
        config_line="        egress-port ethernet 3/1 queue 0 block 0/1",
        parents=("config flows", '    flow "1_9__3_1"'),
    ),
    ConfigLine(config_line="        no shutdown", parents=("config flows", '    flow "1_9__3_1"')),
    ConfigLine(config_line='    flow "3_1__1_9"', parents=("config flows",)),
    ConfigLine(config_line='        classifier "all"', parents=("config flows", '    flow "3_1__1_9"')),
    ConfigLine(config_line="        ingress-port ethernet 3/1", parents=("config flows", '    flow "3_1__1_9"')),
    ConfigLine(
        config_line="        egress-port ethernet 1/9 queue 0 block 0/1",
        parents=("config flows", '    flow "3_1__1_9"'),
    ),
    ConfigLine(config_line="        no shutdown", parents=("config flows", '    flow "3_1__1_9"')),
    ConfigLine(config_line='        flow "1_10__4_1"', parents=("config flows", '    flow "3_1__1_9"')),
    ConfigLine(config_line='        classifier "all"', parents=("config flows", '    flow "3_1__1_9"')),
    ConfigLine(config_line="        ingress-port ethernet 1/10", parents=("config flows", '    flow "3_1__1_9"')),
    ConfigLine(
        config_line="        egress-port ethernet 4/1 queue 0 block 0/1",
        parents=("config flows", '    flow "3_1__1_9"'),
    ),
    ConfigLine(config_line="        no shutdown", parents=("config flows", '    flow "3_1__1_9"')),
    ConfigLine(config_line='    flow "4_1__1_10"', parents=("config flows",)),
    ConfigLine(config_line='        classifier "all"', parents=("config flows", '    flow "4_1__1_10"')),
    ConfigLine(config_line="        ingress-port ethernet 4/1", parents=("config flows", '    flow "4_1__1_10"')),
    ConfigLine(
        config_line="        egress-port ethernet 1/10 queue 0 block 0/1",
        parents=("config flows", '    flow "4_1__1_10"'),
    ),
    ConfigLine(config_line="        no shutdown", parents=("config flows", '    flow "4_1__1_10"')),
    ConfigLine(config_line="    config port ethernet 4/2", parents=("config flows",)),
    ConfigLine(config_line="    loopback remote", parents=("config flows",)),
]
