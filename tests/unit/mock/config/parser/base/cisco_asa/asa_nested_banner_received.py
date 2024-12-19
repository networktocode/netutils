from netutils.config.parser import ConfigLine

parent: str = "group-policy Grs-POLICY attributes"
data: list[ConfigLine] = [
    ConfigLine(config_line=parent, parents=()),
    ConfigLine(config_line=" banner value This is an", parents=(parent,)),
    ConfigLine(config_line=" banner value example nested banner", parents=(parent,)),
]
