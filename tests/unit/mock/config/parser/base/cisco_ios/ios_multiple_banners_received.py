from netutils.config.parser import ConfigLine

data = [
    ConfigLine(config_line="hostname multi-banner", parents=()),
    ConfigLine(config_line="banner exec ^C", parents=()),
    ConfigLine(config_line="* exec banner line 1 *\n* exec banner line 2 *\n^C", parents=("banner exec ^C",)),
    ConfigLine(config_line="banner incoming ^C", parents=()),
    ConfigLine(
        config_line="* incoming banner line 1 *\n* incoming banner line 2 *\n^C", parents=("banner incoming ^C",)
    ),
    ConfigLine(config_line="banner login ^C", parents=()),
    ConfigLine(config_line="* login banner line 1 *\n* login banner line 2 *\n^C", parents=("banner login ^C",)),
    ConfigLine(config_line="banner motd ^C", parents=()),
    ConfigLine(config_line="* motd banner line 1 *\n* motd banner line 2 *\n^C", parents=("banner motd ^C",)),
    ConfigLine(config_line="banner prompt-timeout ^C", parents=()),
    ConfigLine(config_line="* prompt-timeout banner line 1 *\n^C", parents=("banner prompt-timeout ^C",)),
    ConfigLine(config_line="ip route 0.0.0.0 0.0.0.0 192.168.1.1", parents=()),
]
