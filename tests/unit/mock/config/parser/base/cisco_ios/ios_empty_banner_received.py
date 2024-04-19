from netutils.config.parser import ConfigLine

data = [
    ConfigLine(config_line="hostname emptybanner", parents=()),
    ConfigLine(config_line="banner motd ^C^C", parents=()),
    ConfigLine(config_line="line vty 0 4", parents=()),
    ConfigLine(config_line=" transport ssh", parents=("line vty 0 4",)),
]
