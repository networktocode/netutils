from netutils.config.parser import ConfigLine

data = [
    ConfigLine(
        config_line="set mgt-config users admin phash *",
        parents=(),
    ),
    ConfigLine(
        config_line="set mgt-config users admin permissions role-based superuser yes",
        parents=(),
    ),
    ConfigLine(
        config_line="set mgt-config users admin public-key thisisasuperduperlongbase64encodedstring",
        parents=(),
    ),
    ConfigLine(
        config_line="set mgt-config users panadmin permissions role-based superuser yes",
        parents=(),
    ),
    ConfigLine(
        config_line="set mgt-config users panadmin phash passwordhash",
        parents=(),
    ),
    ConfigLine(
        config_line="set devices localhost.localdomain deviceconfig system hostname firewall1",
        parents=(),
    ),
    ConfigLine(
        config_line='set devices localhost.localdomain deviceconfig system login-banner "',
        parents=(),
    ),
    ConfigLine(
        config_line=" ************************************************************************\n *                        firewall1.example.com                       *                         [PROD VM500  firewalls]\n ************************************************************************\n *                               WARNING                                *\n *   Unauthorized access to this device or devices attached to          *\n *   or accessible from this network is strictly prohibited.            *\n *   Possession of passwords or devices enabling access to this         *\n *   device or devices does not constitute authorization. Unauthorized  *\n *   access will be prosecuted to the fullest extent of the law.        *\n *                                                                      *\n ************************************************************************^C",
        parents=('set devices localhost.localdomain deviceconfig system login-banner "',),
    ),
    ConfigLine(
        config_line="set devices localhost.localdomain deviceconfig system panorama local-panorama panorama-server 10.0.0.1",
        parents=(),
    ),
    ConfigLine(
        config_line="set devices localhost.localdomain deviceconfig system panorama local-panorama panorama-server-2 10.0.0.2",
        parents=(),
    ),
]
