from netutils.config.parser import ConfigLine

data = [
    ConfigLine(config_line="hostname dual-banner", parents=()),
    ConfigLine(config_line="banner exec ^C", parents=()),
    ConfigLine(config_line="=========\nintended config exec banner\n-========\n^C", parents=("banner exec ^C",)),
    ConfigLine(config_line="banner motd ^C", parents=()),
    ConfigLine(
        config_line="======\nintended config motd banner\n======\n   || ($hostname) ||\n^C", parents=("banner motd ^C",)
    ),
    ConfigLine(config_line=None, parents=()),
]
