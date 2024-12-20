from netutils.config.parser import ConfigLine

data = [
    ConfigLine(config_line="group-policy Grs-POLICY attributes", parents=()),
    ConfigLine(
        config_line=" banner value This is an",
        parents=("group-policy Grs-POLICY attributes",),
    ),
    ConfigLine(
        config_line=" banner value example nested banner",
        parents=("group-policy Grs-POLICY attributes",),
    ),
]
