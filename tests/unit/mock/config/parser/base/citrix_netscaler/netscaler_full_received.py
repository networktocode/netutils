from netutils.config.parser import ConfigLine

data = [
    ConfigLine(config_line="#NS13.0 Build 84.11", parents=()),
    ConfigLine(config_line="# Last modified Fri Dec  31 12:00:01 2021", parents=()),
    ConfigLine(config_line='set system parameter -promptString "%u@%h-%T" -maxClient 40 -doppler DISABLED', parents=()),
    ConfigLine(config_line="set ns httpProfile nshttp_default_profile -dropInvalReqs ENABLED", parents=()),
    ConfigLine(config_line='set ns param -timezone "GMT+00:00-UTC"', parents=()),
    ConfigLine(config_line="set ssl service nshttps-::1l-443 -ssl3 disabled -tls1 disabled", parents=()),
    ConfigLine(config_line="set ssl service nshttps-127.0.0.1-443 -ssl3 disabled -tls1 disabled", parents=()),
    ConfigLine(config_line="set ssl parameter -defaultProfile ENABLED", parents=()),
    ConfigLine(config_line="enable ns feature WL SP LB CS SSL CF REWRITE RESPONDER", parents=()),
    ConfigLine(config_line="add route 192.168.0.0 255.255.0.0", parents=()),
    ConfigLine(
        config_line="set ns encryptionParams -method AES256 -keyValue abcdef1234 -encrypted -encryptmethod ENCMTHD_3 -kek -suffix some_string",
        parents=(),
    ),
    ConfigLine(
        config_line="set system user nsroot abcdef1234 -encrypted -hashmethod SHA512 -externalAuth DISABLED -timeout 900",
        parents=(),
    ),
    ConfigLine(config_line="set HA node -failSafe ON", parents=()),
    ConfigLine(
        config_line="set ns rpcNode 203.0.113.1 -password abcdef1234 -encrypted -encryptmethod ENCMTHD_3 -kek -suffix some_string -srcIP 203.0.113.1",
        parents=(),
    ),
    ConfigLine(
        config_line="set ns rpcNode 203.0.113.1 -password abcdef1234 -encrypted -encryptmethod ENCMTHD_3 -kek -suffix some_string -srcIP 203.0.113.1",
        parents=(),
    ),
    ConfigLine(
        config_line="add authentication tacacsAction AAA_ACT_TACACS_01 -serverIP 203.0.113.1 -authTimeout 10 -tacacsSecret abcdef1234 -authorization OFF -accounting ON -groupAttrName memberof",
        parents=(),
    ),
    ConfigLine(
        config_line="add authentication tacacsAction AAA_ACT_TACACS_02 -serverIP 203.0.113.1 -authTimeout 10 -tacacsSecret abcdef1234 -authorization OFF -accounting ON -groupAttrName memberof",
        parents=(),
    ),
    ConfigLine(
        config_line="add authentication Policy AAA_POL_TACACS_01 -rule true -action AAA_ACT_TACACS_01", parents=()
    ),
    ConfigLine(
        config_line="add authentication Policy AAA_POL_TACACS_02 -rule true -action AAA_ACT_TACACS_02", parents=()
    ),
    ConfigLine(
        config_line="bind system global AAA_POL_TACACS_01 -priority 10 -gotoPriorityExpression NEXT", parents=()
    ),
    ConfigLine(
        config_line="bind system global AAA_POL_TACACS_02 -priority 20 -gotoPriorityExpression NEXT", parents=()
    ),
    ConfigLine(config_line="add system group Admin -timeout 900", parents=()),
    ConfigLine(config_line="bind system group Admin -policyName superuser 100", parents=()),
    ConfigLine(config_line="add system group Support -timeout 900", parents=()),
    ConfigLine(config_line="bind system group Support -policyName XX-CMD-read-only 100", parents=()),
    ConfigLine(config_line="bind system group Support -policyName XX-CMD-partition-read-only 110", parents=()),
    ConfigLine(config_line="add system group Networking -timeout 900", parents=()),
    ConfigLine(config_line="bind system group Networking -policyName XX-CMD-operator 100", parents=()),
    ConfigLine(config_line="bind system group Networking -policyName XX-CMD-partition-operator 110", parents=()),
    ConfigLine(
        config_line="add system cmdPolicy XX-CMD-read-only ALLOW (^man.*)|(^show\\s+(\\?!system)(\\?!configstatus)(\\?!audit messages)(\\?!techsupport).*)|(^stat.*)",
        parents=(),
    ),
    ConfigLine(
        config_line="add system cmdPolicy XX-CMD-operator ALLOW (^show.*)|(^stat.*)|(^(enable|disable) (server|service).*)",
        parents=(),
    ),
    ConfigLine(
        config_line="add system cmdPolicy XX-CMD-partition-read-only ALLOW (^man.*)|(^switch)|(^show\\s+(\\?!system)(\\?!configstatus)(\\?!audit messages)(\\?!techsupport).*)|(^stat.*)",
        parents=(),
    ),
    ConfigLine(
        config_line="add system cmdPolicy XX-CMD-partition-operator ALLOW (^man.*)|(^switch)|(^show\\s+(\\?!system)(\\?!configstatus)(\\?!audit messages)(\\?!techsupport).*)|(^stat.*)|(^(enable|disable) (server|service).*)",
        parents=(),
    ),
    ConfigLine(config_line="set audit syslogParams -userDefinedAuditlog YES", parents=()),
    ConfigLine(config_line="set audit nslogParams -userDefinedAuditlog YES", parents=()),
    ConfigLine(
        config_line="add audit syslogAction sys_act_fdi_rsyslog 203.0.113.1 -logLevel EMERGENCY ALERT CRITICAL ERROR WARNING NOTICE INFORMATIONAL -timeZone LOCAL_TIME -userDefinedAuditlog YES -transport UDP",
        parents=(),
    ),
    ConfigLine(config_line="add audit syslogPolicy sys_pol_fdi true sys_act_fdi_rsyslog", parents=()),
    ConfigLine(config_line="bind audit syslogGlobal -policyName sys_pol_fdi -priority 2000000010", parents=()),
    ConfigLine(
        config_line="set snmp alarm CPU-USAGE -thresholdValue 95 -normalValue 35 -severity Informational", parents=()
    ),
    ConfigLine(config_line="set snmp alarm HA-STATE-CHANGE -severity Informational", parents=()),
    ConfigLine(config_line="set snmp alarm IP-CONFLICT -severity Warning", parents=()),
    ConfigLine(config_line="set snmp alarm MEMORY -thresholdValue 95 -normalValue 35 -severity Critical", parents=()),
    ConfigLine(config_line="set snmp alarm POWER-SUPPLY-FAILURE -severity Minor", parents=()),
    ConfigLine(config_line="set snmp alarm SSL-CARD-FAILED -severity Minor", parents=()),
    ConfigLine(config_line="set snmp alarm SSL-CERT-EXPIRY -severity Warning", parents=()),
    ConfigLine(config_line="add snmp view READ 1 -type included", parents=()),
    ConfigLine(config_line="add snmp group NETMON-GROUP authpriv -readViewName READ", parents=()),
    ConfigLine(
        config_line="add snmp user monitoring -group NETMON-GROUP -authType SHA -authpasswd abcdef1234 -privType AES -privpasswd abcdef1234",
        parents=(),
    ),
    ConfigLine(config_line="add ssl cipher XX-CIPHER-GROUP_1.0_v01", parents=()),
    ConfigLine(
        config_line="bind ssl cipher XX-CIPHER-GROUP_1.0_v01 -cipherName TLS1.2-ECDHE-RSA-AES256-GCM-SHA384", parents=()
    ),
    ConfigLine(
        config_line="bind ssl cipher XX-CIPHER-GROUP_1.0_v01 -cipherName TLS1.2-ECDHE-RSA-AES128-GCM-SHA256", parents=()
    ),
    ConfigLine(
        config_line="bind ssl cipher XX-CIPHER-GROUP_1.0_v01 -cipherName TLS1.2-ECDHE-RSA-AES-256-SHA384", parents=()
    ),
    ConfigLine(
        config_line="bind ssl cipher XX-CIPHER-GROUP_1.0_v01 -cipherName TLS1.2-ECDHE-RSA-AES-128-SHA256", parents=()
    ),
    ConfigLine(config_line="bind ssl cipher XX-CIPHER-GROUP_1.0_v01 -cipherName TLS1-ECDHE-RSA-AES256-SHA", parents=()),
    ConfigLine(config_line="bind ssl cipher XX-CIPHER-GROUP_1.0_v01 -cipherName TLS1-ECDHE-RSA-AES128-SHA", parents=()),
    ConfigLine(
        config_line="bind ssl cipher XX-CIPHER-GROUP_1.0_v01 -cipherName TLS1.2-DHE-RSA-AES256-GCM-SHA384", parents=()
    ),
    ConfigLine(
        config_line="bind ssl cipher XX-CIPHER-GROUP_1.0_v01 -cipherName TLS1.2-DHE-RSA-AES128-GCM-SHA256", parents=()
    ),
    ConfigLine(
        config_line="bind ssl cipher XX-CIPHER-GROUP_1.0_v01 -cipherName TLS1-DHE-RSA-AES-256-CBC-SHA", parents=()
    ),
    ConfigLine(
        config_line="bind ssl cipher XX-CIPHER-GROUP_1.0_v01 -cipherName TLS1-DHE-RSA-AES-128-CBC-SHA", parents=()
    ),
    ConfigLine(config_line="bind ssl cipher XX-CIPHER-GROUP_1.0_v01 -cipherName TLS1-AES-256-CBC-SHA", parents=()),
    ConfigLine(config_line="bind ssl cipher XX-CIPHER-GROUP_1.0_v01 -cipherName TLS1-AES-128-CBC-SHA", parents=()),
    ConfigLine(config_line="bind ssl cipher XX-CIPHER-GROUP_1.0_v01 -cipherName SSL3-DES-CBC3-SHA", parents=()),
    ConfigLine(config_line="add ssl cipher XX-CIPHER-GROUP_1.2_v01", parents=()),
    ConfigLine(
        config_line="bind ssl cipher XX-CIPHER-GROUP_1.2_v01 -cipherName TLS1.2-ECDHE-RSA-AES256-GCM-SHA384", parents=()
    ),
    ConfigLine(
        config_line="bind ssl cipher XX-CIPHER-GROUP_1.2_v01 -cipherName TLS1.2-ECDHE-RSA-AES128-GCM-SHA256", parents=()
    ),
    ConfigLine(
        config_line="bind ssl cipher XX-CIPHER-GROUP_1.2_v01 -cipherName TLS1.2-ECDHE-RSA-AES-256-SHA384", parents=()
    ),
    ConfigLine(
        config_line="bind ssl cipher XX-CIPHER-GROUP_1.2_v01 -cipherName TLS1.2-ECDHE-RSA-AES-128-SHA256", parents=()
    ),
    ConfigLine(config_line="add ssl cipher XX-CIPHER-GROUP_1.2_v02", parents=()),
    ConfigLine(
        config_line="bind ssl cipher XX-CIPHER-GROUP_1.0_v03 -cipherName TLS1.2-ECDHE-RSA-CHACHA20-POLY1305", parents=()
    ),
    ConfigLine(
        config_line="bind ssl cipher XX-CIPHER-GROUP_1.0_v03 -cipherName TLS1.2-ECDHE-RSA-AES256-GCM-SHA384", parents=()
    ),
    ConfigLine(
        config_line="bind ssl cipher XX-CIPHER-GROUP_1.0_v03 -cipherName TLS1.2-ECDHE-RSA-AES128-GCM-SHA256", parents=()
    ),
    ConfigLine(
        config_line="bind ssl cipher XX-CIPHER-GROUP_1.0_v03 -cipherName TLS1.2-ECDHE-RSA-AES-256-SHA384", parents=()
    ),
    ConfigLine(
        config_line="bind ssl cipher XX-CIPHER-GROUP_1.0_v03 -cipherName TLS1.2-ECDHE-RSA-AES-128-SHA256", parents=()
    ),
    ConfigLine(config_line="bind ssl cipher XX-CIPHER-GROUP_1.0_v03 -cipherName TLS1-ECDHE-RSA-AES256-SHA", parents=()),
    ConfigLine(config_line="bind ssl cipher XX-CIPHER-GROUP_1.0_v03 -cipherName TLS1-ECDHE-RSA-AES128-SHA", parents=()),
    ConfigLine(config_line="add ssl cipher XX-CIPHER-LIST_256", parents=()),
    ConfigLine(
        config_line="bind ssl cipher XX-CIPHER-LIST_256 -cipherName TLS1.2-ECDHE-RSA-AES256-GCM-SHA384 -cipherPriority 1",
        parents=(),
    ),
    ConfigLine(
        config_line="bind ssl cipher XX-CIPHER-LIST_256 -cipherName TLS1.2-ECDHE-RSA-AES-256-SHA384 -cipherPriority 2",
        parents=(),
    ),
    ConfigLine(
        config_line="bind ssl cipher XX-CIPHER-LIST_256 -cipherName TLS1-ECDHE-RSA-AES256-SHA -cipherPriority 3",
        parents=(),
    ),
    ConfigLine(
        config_line="bind ssl cipher XX-CIPHER-LIST_256 -cipherName TLS1.2-AES256-GCM-SHA384 -cipherPriority 4",
        parents=(),
    ),
    ConfigLine(
        config_line="bind ssl cipher XX-CIPHER-LIST_256 -cipherName TLS1.2-AES-256-SHA256 -cipherPriority 5", parents=()
    ),
    ConfigLine(
        config_line="bind ssl cipher XX-CIPHER-LIST_256 -cipherName TLS1-AES-256-CBC-SHA -cipherPriority 6", parents=()
    ),
    ConfigLine(
        config_line="add ssl profile XX-SSL-Profile_1.0_v01 -eRSA ENABLED -eRSACount 1800 -sessReuse ENABLED -sessTimeout 1800 -ssl3 DISABLED -denySSLReneg ALL",
        parents=(),
    ),
    ConfigLine(
        config_line="add ssl profile XX-SSL-Profile_1.2_v01 -eRSA ENABLED -eRSACount 1800 -sessReuse ENABLED -sessTimeout 1800 -ssl3 DISABLED -tls1 DISABLED -tls11 DISABLED -denySSLReneg ALL",
        parents=(),
    ),
    ConfigLine(
        config_line="add ssl profile XX-SSL-Profile_1.2_v02 -eRSA ENABLED -eRSACount 1800 -sessReuse ENABLED -sessTimeout 1800 -ssl3 DISABLED -tls1 DISABLED -tls11 DISABLED -denySSLReneg NONSECURE",
        parents=(),
    ),
]
