from netutils.config.parser import ConfigLine

data = [
    ConfigLine(config_line="hostname multi-banner-xr", parents=()),
    ConfigLine(config_line="banner exec ~", parents=()),
    ConfigLine(config_line="* exec banner line 1 *\n* exec banner line 2 *\n~", parents=("banner exec ~",)),
    ConfigLine(config_line="banner login ~", parents=()),
    ConfigLine(config_line="* login banner line 1 *\n* login banner line 2 *\n~", parents=("banner login ~",)),
    ConfigLine(config_line="banner motd ~", parents=()),
    ConfigLine(config_line="* motd banner line 1 *\n* motd banner line 2 *\n~", parents=("banner motd ~",)),
    ConfigLine(config_line="banner prompt-timeout ~", parents=()),
    ConfigLine(config_line="* prompt-timeout banner line 1 *\n~", parents=("banner prompt-timeout ~",)),
    ConfigLine(config_line="logging trap informational", parents=()),
]
