from netutils.config.parser import ConfigLine

data = [
    ConfigLine(config_line="hostname banner_with_newline", parents=()),
    ConfigLine(config_line='banner login ^C', parents=()),
    ConfigLine(config_line='****************************************************\nWARNING TO UNAUTHORIZED USERS:\nThis system is for use by authorized users only.\n****************************************************\n^C', parents=('banner login ^C',)),
    ConfigLine(config_line="line vty 0 4", parents=()),
    ConfigLine(config_line=" transport ssh", parents=("line vty 0 4",)),
]
