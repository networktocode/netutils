from netutils.config.parser import ConfigLine

data = [
    ConfigLine(config_line="set deviceconfig system hostname pa-ntc", parents=()),
    ConfigLine(
        config_line="set deviceconfig system login-banner '\"BANNER\"'",
        parents=(),
    ),
    ConfigLine(config_line="set deviceconfig system domain ntc", parents=()),
]
