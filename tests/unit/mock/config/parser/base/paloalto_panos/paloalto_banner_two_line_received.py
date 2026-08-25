from netutils.config.parser import ConfigLine

data = [
    ConfigLine(config_line="set deviceconfig system hostname pa-ntc", parents=()),
    ConfigLine(
        config_line="set deviceconfig system login-banner !#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~",
        parents=(),
    ),
    ConfigLine(
        config_line="!#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~",
        parents=(
            "set deviceconfig system login-banner !#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~",
        ),
    ),
    ConfigLine(config_line="set deviceconfig system domain ntc", parents=()),
]
