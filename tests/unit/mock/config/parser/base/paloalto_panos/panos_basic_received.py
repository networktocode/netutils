from netutils.config.parser import ConfigLine

data = [
    ConfigLine(config_line="set mgt-config users admin phash *", parents=(),),
    ConfigLine(config_line="set mgt-config users admin permissions role-based superuser yes", parents=(),),
    ConfigLine(
        config_line="set mgt-config users admin public-key thisisasuperduperlongbase64encodedstring", parents=(),
    ),
    ConfigLine(config_line="set mgt-config users panadmin permissions role-based superuser yes", parents=(),),
    ConfigLine(config_line="set mgt-config users panadmin phash passwordhash", parents=(),),
    ConfigLine(config_line="set devices localhost.localdomain deviceconfig system hostname firewall1", parents=(),),
    ConfigLine(config_line='set devices localhost.localdomain deviceconfig system login-banner "', parents=(),),
    ConfigLine(
        config_line=" ************************************************************************",
        parents=("set devices localhost.localdomain deviceconfig system login-banner \"",),
    ),
    ConfigLine(
        config_line=" *                        firewall1.example.com                       *                         [PROD VM500  firewalls]",
        parents=("set devices localhost.localdomain deviceconfig system login-banner \"",),
    ),
    ConfigLine(
        config_line=" ************************************************************************",
        parents=("set devices localhost.localdomain deviceconfig system login-banner \"",),
    ),
    ConfigLine(
        config_line=" *                               WARNING                                *",
        parents=("set devices localhost.localdomain deviceconfig system login-banner \"",),
    ),
    ConfigLine(
        config_line=" *   Unauthorized access to this device or devices attached to          *",
        parents=("set devices localhost.localdomain deviceconfig system login-banner \"",),
    ),
    ConfigLine(
        config_line=" *   or accessible from this network is strictly prohibited.            *",
        parents=("set devices localhost.localdomain deviceconfig system login-banner \"",),
    ),
    ConfigLine(
        config_line=" *   Possession of passwords or devices enabling access to this         *",
        parents=("set devices localhost.localdomain deviceconfig system login-banner \"",),
    ),
    ConfigLine(
        config_line=" *   device or devices does not constitute authorization. Unauthorized  *",
        parents=("set devices localhost.localdomain deviceconfig system login-banner \"",),
    ),
    ConfigLine(
        config_line=" *   access will be prosecuted to the fullest extent of the law.        *",
        parents=("set devices localhost.localdomain deviceconfig system login-banner \"",),
    ),
    ConfigLine(
        config_line=" *                                                                      *",
        parents=("set devices localhost.localdomain deviceconfig system login-banner \"",),
    ),
    ConfigLine(
        config_line=" ************************************************************************",
        parents=("set devices localhost.localdomain deviceconfig system login-banner \"",),
    ),
    ConfigLine(config_line=' "', parents=("set devices localhost.localdomain deviceconfig system login-banner \"",),),
    ConfigLine(
        config_line="set devices localhost.localdomain deviceconfig system panorama local-panorama panorama-server 10.0.0.1",
        parents=(),
    ),
    ConfigLine(
        config_line="set devices localhost.localdomain deviceconfig system panorama local-panorama panorama-server-2 10.0.0.2",
        parents=(),
    ),
]
