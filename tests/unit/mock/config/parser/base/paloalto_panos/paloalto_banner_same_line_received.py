from netutils.config.parser import ConfigLine

data = [
    ConfigLine(config_line="set deviceconfig system ip-address 192.0.2.72", parents=()),
    ConfigLine(config_line="set deviceconfig system netmask 255.255.255.0", parents=()),
    ConfigLine(config_line="set deviceconfig system update-server updates.paloaltonetworks.com", parents=()),
    ConfigLine(
        config_line="set deviceconfig system update-schedule threats recurring weekly day-of-week wednesday", parents=()
    ),
    ConfigLine(config_line="set deviceconfig system update-schedule threats recurring weekly at 01:02", parents=()),
    ConfigLine(
        config_line="set deviceconfig system update-schedule threats recurring weekly action download-only", parents=()
    ),
    ConfigLine(config_line="set deviceconfig system timezone UTC", parents=()),
    ConfigLine(config_line="set deviceconfig system service disable-telnet yes", parents=()),
    ConfigLine(config_line="set deviceconfig system service disable-http yes", parents=()),
    ConfigLine(config_line="set deviceconfig system service disable-snmp no", parents=()),
    ConfigLine(config_line="set deviceconfig system hostname pa-ntc", parents=()),
    ConfigLine(config_line="set deviceconfig system type static", parents=()),
    ConfigLine(config_line="set deviceconfig system default-gateway 192.0.2.1", parents=()),
    ConfigLine(config_line="set deviceconfig system domain ntc", parents=()),
    ConfigLine(config_line="set deviceconfig system locale en", parents=()),
    ConfigLine(config_line="set deviceconfig system speed-duplex auto-negotiate", parents=()),
    ConfigLine(config_line="set deviceconfig system dns-setting servers primary 8.8.8.8", parents=()),
    ConfigLine(config_line="set deviceconfig system dns-setting servers secondary 1.1.1.1", parents=()),
    ConfigLine(config_line="set deviceconfig system device-telemetry device-health-performance yes", parents=()),
    ConfigLine(config_line="set deviceconfig system device-telemetry product-usage yes", parents=()),
    ConfigLine(config_line="set deviceconfig system device-telemetry threat-prevention yes", parents=()),
    ConfigLine(config_line="set deviceconfig system device-telemetry region Americas", parents=()),
    ConfigLine(config_line="set deviceconfig system panorama local-panorama panorama-server 192.0.2.58", parents=()),
    ConfigLine(config_line="set deviceconfig system server-verification no", parents=()),
    ConfigLine(
        config_line="set deviceconfig system ntp-servers primary-ntp-server ntp-server-address time.google.com",
        parents=(),
    ),
    ConfigLine(
        config_line="set deviceconfig system ntp-servers primary-ntp-server authentication-type none", parents=()
    ),
    ConfigLine(
        config_line='set deviceconfig system login-banner "####################################################',
        parents=(),
    ),
    ConfigLine(
        config_line='WARNING TO UNAUTHORIZED USERS:\nThis system is for use by authorized users only.\nAny individual using this system, by such use,\nacknowledges and consents to the right of the\ncompany to monitor, access, use, and disclose any\ninformation generated, received, or stored on the\nsystems, and waives any right of privacy or\nexpectation of privacy on the part of that\nindividual in connection with his or her use of\nthis system. Unauthorized and/or improper use of\nthis system, as delineated by corporate policies,\nis not tolerated and the company may take formal\naction against such individuals.\n####################################################\n"',
        parents=('set deviceconfig system login-banner "####################################################',),
    ),
    ConfigLine(
        config_line="set deviceconfig system snmp-setting access-setting version v2c snmp-community-string ntc1234",
        parents=(),
    ),
    ConfigLine(config_line="set deviceconfig system snmp-setting snmp-system location ntc", parents=()),
    ConfigLine(config_line='set deviceconfig system snmp-setting snmp-system contact "john smith"', parents=()),
]
